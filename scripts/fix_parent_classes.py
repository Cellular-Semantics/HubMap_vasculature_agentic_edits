#!/usr/bin/env python3
"""
Fix parent class values in batch JSON files to comply with DOSDP requirements.
Parent class must ONLY be UBERON:0001637 (artery) or UBERON:0001980 (arteriole).
"""

import json
from pathlib import Path

def fix_batch_file(file_path):
    """Fix parent values in a batch JSON file."""
    with open(file_path, 'r') as f:
        data = json.load(f)

    fixed_count = 0

    # Handle different JSON structures
    if isinstance(data, list):
        # Array of entries
        for entry in data:
            if fix_entry_parent(entry):
                fixed_count += 1

    elif 'tsv_format_entries' in data:
        # Batch6-style with tsv_format_entries
        for entry in data['tsv_format_entries']:
            if fix_entry_parent(entry):
                fixed_count += 1

    elif 'entries' in data:
        # Nested entries
        if isinstance(data['entries'], dict):
            for entry in data['entries'].values():
                if fix_entry_parent(entry):
                    fixed_count += 1
        elif isinstance(data['entries'], list):
            for entry in data['entries']:
                if fix_entry_parent(entry):
                    fixed_count += 1

    # Save back if changes were made
    if fixed_count > 0:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"✓ Fixed {fixed_count} entries in {file_path.name}")
        return fixed_count

    return 0

def fix_entry_parent(entry):
    """
    Fix parent field in an entry.
    Returns True if changed, False otherwise.
    """
    parent = entry.get('parent', '')
    label = entry.get('label', '')

    # Determine correct parent based on label
    if 'arteriole' in label.lower():
        correct_parent = 'UBERON:0001980'  # arteriole
        correct_label = 'arteriole'
    else:
        correct_parent = 'UBERON:0001637'  # artery
        correct_label = 'artery'

    # Check if needs fixing
    if parent and parent not in ['UBERON:0001637', 'UBERON:0001980']:
        entry['parent'] = correct_parent
        if 'parent_label' in entry:
            entry['parent_label'] = correct_label
        return True
    elif parent and parent != correct_parent:
        # Has a valid DOSDP parent but wrong one (artery vs arteriole)
        entry['parent'] = correct_parent
        if 'parent_label' in entry:
            entry['parent_label'] = correct_label
        return True

    return False

def main():
    output_dir = Path(__file__).parent.parent / 'output'
    batch_files = sorted(output_dir.glob('batch*.json'))

    print(f"Checking {len(batch_files)} batch files...\n")

    total_fixed = 0
    for batch_file in batch_files:
        fixed = fix_batch_file(batch_file)
        total_fixed += fixed

    print(f"\n=== Summary ===")
    print(f"Total entries fixed: {total_fixed}")
    print(f"\nAll parent values now comply with DOSDP requirement:")
    print(f"  - UBERON:0001637 (artery) for arteries")
    print(f"  - UBERON:0001980 (arteriole) for arterioles")

if __name__ == '__main__':
    main()
