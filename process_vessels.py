#!/usr/bin/env python3
"""
Helper script for processing vessel template entries.
Manages workflow for populating incomplete DOSDP template entries.
"""

import csv
import json
from datetime import datetime
from pathlib import Path

class VesselProcessor:
    def __init__(self, tsv_path):
        self.tsv_path = Path(tsv_path)
        self.entries = []
        self.progress = {}
        self.justifications = {}

        # Load existing data
        self.load_entries()

    def load_entries(self):
        """Load entries from TSV file"""
        with open(self.tsv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter='\t')
            self.entries = list(reader)

    def get_incomplete_entries(self):
        """Get list of incomplete entries (missing definition)"""
        incomplete = []
        for idx, entry in enumerate(self.entries):
            if not entry.get('definition') or entry.get('definition').strip() == '':
                incomplete.append((idx, entry))
        return incomplete

    def save_progress(self, progress_file='progress.json'):
        """Save progress to JSON file"""
        with open(progress_file, 'w') as f:
            json.dump({
                'progress': self.progress,
                'last_updated': datetime.now().isoformat()
            }, f, indent=2)

    def load_progress(self, progress_file='progress.json'):
        """Load progress from JSON file"""
        try:
            with open(progress_file, 'r') as f:
                data = json.load(f)
                self.progress = data.get('progress', {})
        except FileNotFoundError:
            pass

    def save_justifications(self, report_file='justification_report.md'):
        """Save justification report"""
        with open(report_file, 'w') as f:
            f.write("# Vessel Template Completion - Justification Report\n\n")
            f.write(f"Generated: {datetime.now().isoformat()}\n\n")
            f.write("---\n\n")

            for label, justification in sorted(self.justifications.items()):
                f.write(f"## {label}\n\n")
                f.write(justification)
                f.write("\n\n---\n\n")

    def save_updated_tsv(self, output_path=None):
        """Save updated TSV file"""
        if output_path is None:
            output_path = self.tsv_path.parent / f"{self.tsv_path.stem}_updated.tsv"

        fieldnames = list(self.entries[0].keys())
        with open(output_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='\t')
            writer.writeheader()
            writer.writerows(self.entries)

        print(f"Updated TSV saved to: {output_path}")


if __name__ == '__main__':
    processor = VesselProcessor('artery_and_arteriole_pattern.tsv')

    incomplete = processor.get_incomplete_entries()
    print(f"Total entries: {len(processor.entries)}")
    print(f"Incomplete entries: {len(incomplete)}")

    # Show first few incomplete
    print("\nFirst 10 incomplete entries:")
    for idx, entry in incomplete[:10]:
        print(f"  Row {idx+2}: {entry['label']}")
