#!/usr/bin/env python3
"""
Script to consolidate batch results from all agents and generate:
1. Updated TSV template with populated fields
2. Reporting table with ontology labels
3. Justification report with supporting text from references
"""

import csv
import json
from pathlib import Path
from datetime import datetime

def load_template(template_path):
    """Load the original TSV template."""
    with open(template_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        fieldnames = list(reader.fieldnames)
        rows = list(reader)
    return fieldnames, rows

def load_batch_results(output_dir):
    """Load all batch result JSON files."""
    batch_files = list(Path(output_dir).glob('batch*.json'))
    all_results = {}

    for batch_file in sorted(batch_files):
        try:
            with open(batch_file, 'r', encoding='utf-8') as f:
                batch_data = json.load(f)
                # Handle different JSON structures
                if isinstance(batch_data, list):
                    # Array of entries
                    for entry in batch_data:
                        row_num = entry.get('row_number')
                        if row_num:
                            all_results[row_num] = entry
                elif isinstance(batch_data, dict):
                    # Check for various nested structures
                    if 'tsv_format_entries' in batch_data:
                        # Batch6-style with tsv_format_entries array
                        for entry in batch_data['tsv_format_entries']:
                            row_num = entry.get('row') or entry.get('row_number')
                            if row_num:
                                # Convert 'row' to 'row_number' for consistency
                                entry_copy = dict(entry)
                                entry_copy['row_number'] = row_num
                                all_results[row_num] = entry_copy
                    elif 'entries' in batch_data:
                        entries_data = batch_data['entries']
                        if isinstance(entries_data, dict):
                            # Entries stored as object with row keys
                            for row_key, entry in entries_data.items():
                                row_num = entry.get('row_number')
                                if row_num:
                                    all_results[row_num] = entry
                        elif isinstance(entries_data, list):
                            # Entries stored as array
                            for entry in entries_data:
                                row_num = entry.get('row_number')
                                if row_num:
                                    all_results[row_num] = entry
                    else:
                        # Single entry or other structure
                        row_num = batch_data.get('row_number')
                        if row_num:
                            all_results[row_num] = batch_data
        except Exception as e:
            print(f"Warning: Could not load {batch_file}: {e}")

    return all_results

def update_template_row(row, result_entry):
    """Update a template row with results from batch processing."""
    if not result_entry:
        return row

    # Update fields if they exist in the result
    field_mappings = {
        'FMA_xref': 'FMA_xref',
        'parent': 'parent',
        'location': 'location',
        'definition': 'definition',
        'connecting_branch_of': 'connecting_branch_of',
        'vessel_supplies_blood_to': 'vessel_supplies_blood_to',
        'synonym': 'synonym',
        'synonym_xrefs': 'synonym_xrefs'
    }

    for result_key, row_key in field_mappings.items():
        if result_key in result_entry and result_entry[result_key]:
            row[row_key] = result_entry[result_key]

    # Set default creator and date if not already set
    if not row.get('creator'):
        row['creator'] = 'https://orcid.org/0000-0001-6677-8489'
    if not row.get('date_created'):
        row['date_created'] = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')

    return row

def generate_updated_template(template_path, output_dir, results):
    """Generate updated template TSV file."""
    fieldnames, rows = load_template(template_path)

    updated_count = 0
    for idx, row in enumerate(rows, start=2):  # Row 1 is header
        if idx in results:
            row = update_template_row(row, results[idx])
            updated_count += 1

    output_path = Path(output_dir) / 'artery_and_arteriole_pattern_updated.tsv'
    with open(output_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()
        writer.writerows(rows)

    print(f"Updated template saved to: {output_path}")
    print(f"Updated {updated_count} rows")

    return output_path, rows

def extract_ontology_labels(ontology_id):
    """Extract label from ontology ID for reporting."""
    # This is a placeholder - in practice, we'd look up actual labels
    # from the ontology or from the results
    if not ontology_id or ontology_id == '':
        return ''

    # For now, just return the ID
    return f"[Label for {ontology_id}]"

def generate_reporting_table(rows, output_dir, results):
    """Generate reporting table with ontology labels."""
    report_rows = []

    for idx, row in enumerate(rows, start=2):
        report_row = {
            'row_number': idx,
            'defined_class': row.get('defined_class', ''),
            'label': row.get('label', ''),
            'parent': row.get('parent', ''),
            'parent_label': extract_ontology_labels(row.get('parent', '')),
            'location': row.get('location', ''),
            'location_label': extract_ontology_labels(row.get('location', '')),
            'connecting_branch_of': row.get('connecting_branch_of', ''),
            'connecting_branch_of_label': extract_ontology_labels(row.get('connecting_branch_of', '')),
            'vessel_supplies_blood_to': row.get('vessel_supplies_blood_to', ''),
            'vessel_supplies_blood_to_label': extract_ontology_labels(row.get('vessel_supplies_blood_to', '')),
            'definition': row.get('definition', ''),
            'xrefs': row.get('xrefs', ''),
            'updated': 'Yes' if idx in results else 'No'
        }
        report_rows.append(report_row)

    output_path = Path(output_dir) / 'reporting_table.tsv'
    fieldnames = list(report_rows[0].keys())

    with open(output_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()
        writer.writerows(report_rows)

    print(f"Reporting table saved to: {output_path}")

    return output_path

def generate_justification_report(results, output_dir):
    """Generate markdown justification report."""
    report_lines = [
        "# Justification Report for DOSDP Template Updates",
        "",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        f"Total entries updated: {len(results)}",
        "",
        "---",
        ""
    ]

    for row_num in sorted(results.keys()):
        entry = results[row_num]
        report_lines.extend([
            f"## Row {row_num}: {entry.get('label', 'Unknown')}",
            "",
            f"**Reference:** {entry.get('xrefs', 'N/A')}",
            "",
            "### Populated Fields:",
            ""
        ])

        if entry.get('definition'):
            report_lines.append(f"- **Definition:** {entry['definition']}")
        if entry.get('parent'):
            report_lines.append(f"- **Parent:** {entry['parent']}")
        if entry.get('location'):
            report_lines.append(f"- **Location:** {entry['location']}")
        if entry.get('connecting_branch_of'):
            report_lines.append(f"- **Connecting branch of:** {entry['connecting_branch_of']}")
        if entry.get('vessel_supplies_blood_to'):
            report_lines.append(f"- **Supplies:** {entry['vessel_supplies_blood_to']}")

        report_lines.append("")

        if entry.get('justification'):
            report_lines.extend([
                "### Justification:",
                "",
                entry['justification'],
                ""
            ])

        report_lines.extend(["---", ""])

    output_path = Path(output_dir) / 'justification_report.md'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report_lines))

    print(f"Justification report saved to: {output_path}")

    return output_path

def main():
    base_dir = Path(__file__).parent.parent
    template_path = base_dir / 'source' / 'artery_and_arteriole_pattern.tsv'
    output_dir = base_dir / 'output'

    print("Loading batch results...")
    results = load_batch_results(output_dir)
    print(f"Loaded results for {len(results)} entries")

    print("\nGenerating updated template...")
    updated_template_path, rows = generate_updated_template(template_path, output_dir, results)

    print("\nGenerating reporting table...")
    reporting_table_path = generate_reporting_table(rows, output_dir, results)

    print("\nGenerating justification report...")
    justification_report_path = generate_justification_report(results, output_dir)

    print("\n=== Summary ===")
    print(f"Updated template: {updated_template_path}")
    print(f"Reporting table: {reporting_table_path}")
    print(f"Justification report: {justification_report_path}")

if __name__ == '__main__':
    main()
