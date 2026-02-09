#!/usr/bin/env python3
"""
Script to process incomplete DOSDP template entries.
Reads the template TSV, identifies rows with missing content,
and helps organize the data for population.
"""

import csv
import json
from pathlib import Path

def read_template(file_path):
    """Read the TSV template file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        return list(reader)

def identify_incomplete_rows(rows):
    """Identify rows with missing required fields."""
    incomplete = []
    required_fields = ['parent', 'location', 'definition', 'connecting_branch_of']

    for idx, row in enumerate(rows, start=2):  # Start at 2 (row 1 is header)
        missing_fields = []
        for field in required_fields:
            if not row.get(field) or row[field].strip() == '':
                missing_fields.append(field)

        if missing_fields:
            incomplete.append({
                'row_number': idx,
                'label': row.get('label', ''),
                'xrefs': row.get('xrefs', ''),
                'missing_fields': missing_fields
            })

    return incomplete

def main():
    template_path = Path(__file__).parent.parent / 'source' / 'artery_and_arteriole_pattern.tsv'
    rows = read_template(template_path)

    print(f"Total rows: {len(rows)}")

    incomplete = identify_incomplete_rows(rows)
    print(f"\nIncomplete rows: {len(incomplete)}")

    # Group by reference type
    wikipedia_refs = []
    doi_refs = []
    pmid_refs = []
    other_refs = []

    for item in incomplete:
        ref = item['xrefs']
        if 'wikipedia' in ref.lower():
            wikipedia_refs.append(item)
        elif 'doi:' in ref.lower() or 'doi.org' in ref.lower():
            doi_refs.append(item)
        elif 'pmid:' in ref.lower() or 'pubmed' in ref.lower():
            pmid_refs.append(item)
        else:
            other_refs.append(item)

    print(f"\nBy reference type:")
    print(f"  Wikipedia: {len(wikipedia_refs)}")
    print(f"  DOI: {len(doi_refs)}")
    print(f"  PMID: {len(pmid_refs)}")
    print(f"  Other: {len(other_refs)}")

    # Save organized data
    output_path = Path(__file__).parent.parent / 'output' / 'incomplete_rows.json'
    output_path.parent.mkdir(exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump({
            'total_incomplete': len(incomplete),
            'wikipedia_refs': wikipedia_refs,
            'doi_refs': doi_refs,
            'pmid_refs': pmid_refs,
            'other_refs': other_refs
        }, f, indent=2)

    print(f"\nSaved organized data to: {output_path}")

if __name__ == '__main__':
    main()
