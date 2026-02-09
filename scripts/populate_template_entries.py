#!/usr/bin/env python3
"""
Script to populate missing DOSDP template entries by processing references
and extracting anatomical information systematically.

This script will create a comprehensive data structure for each incomplete entry
that can be used to populate the template fields.
"""

import csv
import json
from pathlib import Path
from datetime import datetime

def load_template(template_path):
    """Load the TSV template."""
    with open(template_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        fieldnames = reader.fieldnames
        rows = list(reader)
    return fieldnames, rows

def analyze_completed_entries(rows):
    """Analyze completed entries to understand patterns."""
    patterns = {
        'parent_values': {},
        'common_locations': {},
        'common_connecting_branches': {}
    }

    for row in rows:
        if row.get('parent'):
            parent = row['parent']
            patterns['parent_values'][parent] = patterns['parent_values'].get(parent, 0) + 1

        if row.get('location'):
            loc = row['location']
            patterns['common_locations'][loc] = patterns['common_locations'].get(loc, 0) + 1

        if row.get('connecting_branch_of'):
            cb = row['connecting_branch_of']
            patterns['common_connecting_branches'][cb] = patterns['common_connecting_branches'].get(cb, 0) + 1

    return patterns

def extract_anatomical_info_from_label(label):
    """Extract anatomical clues from the artery label."""
    info = {
        'digit_specific': None,
        'side': None,
        'likely_location': None,
        'likely_parent': None
    }

    # Check for digit-specific arteries
    digit_terms = ['first', 'second', 'third', 'fourth', 'fifth']
    for i, term in enumerate(digit_terms, 1):
        if term in label.lower():
            info['digit_specific'] = i

    # Check for anatomical sides
    if 'lateral' in label.lower():
        info['side'] = 'lateral'
    elif 'medial' in label.lower():
        info['side'] = 'medial'
    elif 'anterior' in label.lower():
        info['side'] = 'anterior'
    elif 'posterior' in label.lower():
        info['side'] = 'posterior'
    elif 'superior' in label.lower():
        info['side'] = 'superior'
    elif 'inferior' in label.lower():
        info['side'] = 'inferior'

    # Determine location based on label keywords
    if 'hand' in label.lower():
        info['likely_location'] = 'hand'
    elif 'foot' in label.lower():
        info['likely_location'] = 'foot'
    elif 'digit' in label.lower():
        if 'palmar' in label.lower():
            info['likely_location'] = 'hand'
        elif 'plantar' in label.lower():
            info['likely_location'] = 'foot'
    elif 'cerebral' in label.lower() or 'frontal' in label.lower() or 'parietal' in label.lower():
        info['likely_location'] = 'brain'
    elif 'spleen' in label.lower():
        info['likely_location'] = 'spleen'
    elif 'hepatic' in label.lower() or 'liver' in label.lower():
        info['likely_location'] = 'liver'
    elif 'renal' in label.lower() or 'kidney' in label.lower():
        info['likely_location'] = 'kidney'
    elif 'pancrea' in label.lower():
        info['likely_location'] = 'pancreas'
    elif 'pharyngeal' in label.lower():
        info['likely_location'] = 'pharynx'
    elif 'meningeal' in label.lower():
        info['likely_location'] = 'meninges'
    elif 'pulmonary' in label.lower():
        info['likely_location'] = 'lung'
    elif 'coronary' in label.lower() or 'cardiac' in label.lower():
        info['likely_location'] = 'heart'
    elif 'colon' in label.lower() or 'colic' in label.lower():
        info['likely_location'] = 'colon'
    elif 'uterus' in label.lower() or 'uterine' in label.lower():
        info['likely_location'] = 'uterus'
    elif 'spinal' in label.lower() or 'medullary' in label.lower():
        info['likely_location'] = 'spinal cord'

    # Determine likely parent based on label
    if 'branch of' in label.lower():
        # Extract parent from label
        parts = label.lower().split('branch of')
        if len(parts) > 1:
            parent_name = parts[1].strip()
            info['likely_parent'] = parent_name
    elif 'palmar digital' in label.lower():
        if 'proper' in label.lower():
            info['likely_parent'] = 'common palmar digital artery'
        elif 'common' in label.lower():
            info['likely_parent'] = 'superficial palmar arch'
    elif 'plantar digital' in label.lower():
        if 'proper' in label.lower():
            info['likely_parent'] = 'common plantar digital artery'
        elif 'common' in label.lower():
            info['likely_parent'] = 'plantar arch'
    elif 'metacarpal' in label.lower():
        info['likely_parent'] = 'deep palmar arch'
    elif 'lobar' in label.lower() and 'spleen' in label.lower():
        info['likely_parent'] = 'splenic artery'
    elif 'segmental' in label.lower() and 'hepatic' in label.lower():
        info['likely_parent'] = 'hepatic artery'
    elif 'cerebral' in label.lower():
        if 'anterior' in label.lower():
            info['likely_parent'] = 'anterior cerebral artery'
        elif 'middle' in label.lower():
            info['likely_parent'] = 'middle cerebral artery'
        elif 'posterior' in label.lower():
            info['likely_parent'] = 'posterior cerebral artery'

    return info

def create_entry_template(row, row_number):
    """Create a template for an incomplete entry with extracted information."""
    label = row.get('label', '')
    xrefs = row.get('xrefs', '')

    anatomical_info = extract_anatomical_info_from_label(label)

    entry = {
        'row_number': row_number,
        'label': label,
        'xrefs': xrefs,
        'anatomical_clues': anatomical_info,
        'needs': {
            'FMA_xref': not row.get('FMA_xref'),
            'parent': not row.get('parent'),
            'location': not row.get('location'),
            'definition': not row.get('definition'),
            'connecting_branch_of': not row.get('connecting_branch_of'),
            'vessel_supplies_blood_to': not row.get('vessel_supplies_blood_to')
        },
        'suggested_values': {},
        'reference_info': None
    }

    return entry

def main():
    template_path = Path(__file__).parent.parent / 'source' / 'artery_and_arteriole_pattern.tsv'
    fieldnames, rows = load_template(template_path)

    print(f"Loaded {len(rows)} rows from template")

    # Analyze patterns in completed entries
    patterns = analyze_completed_entries(rows)

    print("\nMost common parent values:")
    for parent, count in sorted(patterns['parent_values'].items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  {parent}: {count}")

    # Process incomplete entries
    incomplete_entries = []

    for idx, row in enumerate(rows, start=2):
        required_fields = ['parent', 'location', 'definition']
        missing_fields = [f for f in required_fields if not row.get(f) or row[f].strip() == '']

        if missing_fields:
            entry = create_entry_template(row, idx)
            incomplete_entries.append(entry)

    print(f"\nFound {len(incomplete_entries)} incomplete entries")

    # Save the structured data
    output_path = Path(__file__).parent.parent / 'output' / 'entries_to_populate.json'
    output_path.parent.mkdir(exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump({
            'timestamp': datetime.now().isoformat(),
            'total_entries': len(incomplete_entries),
            'patterns': patterns,
            'entries': incomplete_entries
        }, f, indent=2)

    print(f"\nSaved structured data to: {output_path}")

    # Group by reference type for processing strategy
    ref_types = {'wikipedia': [], 'doi': [], 'pmid': [], 'ncbi': [], 'radiopaedia': [], 'other': []}

    for entry in incomplete_entries:
        ref = entry['xrefs'].lower()
        if 'wikipedia' in ref:
            ref_types['wikipedia'].append(entry)
        elif 'doi' in ref:
            ref_types['doi'].append(entry)
        elif 'pmid' in ref or 'pubmed' in ref:
            ref_types['pmid'].append(entry)
        elif 'ncbi.nlm.nih.gov' in ref:
            ref_types['ncbi'].append(entry)
        elif 'radiopaedia' in ref:
            ref_types['radiopaedia'].append(entry)
        else:
            ref_types['other'].append(entry)

    print("\nReference type distribution:")
    for ref_type, entries in ref_types.items():
        if entries:
            print(f"  {ref_type}: {len(entries)}")

if __name__ == '__main__':
    main()
