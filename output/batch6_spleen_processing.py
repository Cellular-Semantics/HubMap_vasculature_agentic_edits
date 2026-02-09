#!/usr/bin/env python3
"""
Process spleen artery entries based on row 57 pattern and anatomical knowledge.
The splenic artery branches at the hilum into lobar arteries (superior and inferior),
which further divide into segmental branches.
"""

import json
from datetime import datetime

# Reference data from row 57 (completed lobar artery of spleen)
row_57_pattern = {
    "label": "lobar artery of spleen",
    "parent": "UBERON:0001637",  # artery
    "location": "UBERON:0000916",  # abdomen
    "connecting_branch_of": "UBERON:0001194",  # splenic artery
    "vessel_supplies_blood_to": "UBERON:0002106",  # spleen
    "creator": "https://orcid.org/0000-0001-6757-4744"
}

# Anatomical knowledge:
# - Splenic artery (UBERON:0001194) branches at splenic hilum (UBERON:0001248)
# - Lobar arteries divide the spleen into superior and inferior regions
# - Lobar arteries further divide into segmental branches
# - All are part of abdomen (UBERON:0000916)
# - All supply spleen (UBERON:0002106)

# Generate timestamp
timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

# Entry definitions
entries = {
    "row_78": {
        "row_number": 78,
        "defined_class": "",  # To be assigned by ontology
        "label": "inferior lobar artery of spleen",
        "FMA_xref": "",
        "parent": "UBERON:0001637",  # artery (more specific than arterial blood vessel)
        "location": "UBERON:0000916",  # abdomen
        "definition": "An artery that branches from the splenic artery at the splenic hilum and supplies the inferior portion of the spleen.",
        "xrefs": "https://ijcrr.com/uploads/759_pdf.pdf",
        "synonym": "inferior splenic lobar artery",
        "synonym_xrefs": "",
        "connecting_branch_of": "UBERON:0001194",  # splenic artery
        "vessel_supplies_blood_to": "UBERON:0002106",  # spleen
        "creator": "https://orcid.org/0000-0001-6757-4744",
        "date_created": timestamp,
        "notes": "Branches from splenic artery at hilum, supplies inferior region of spleen"
    },
    "row_102": {
        "row_number": 102,
        "defined_class": "UBERON:8920049",  # Already exists as row 57
        "label": "lobar artery of spleen",
        "FMA_xref": "",
        "parent": "UBERON:0001637",
        "location": "UBERON:0000916",
        "definition": "An artery that branches from the splenic artery at the splenic hilum at which it divides into one or two terminal branches supplying a lobe of the spleen.",
        "xrefs": "PMID:26217091",
        "synonym": "splenic lobar artery",
        "synonym_xrefs": "PMID:26217091",
        "connecting_branch_of": "UBERON:0001194",
        "vessel_supplies_blood_to": "UBERON:0002106",
        "creator": "https://orcid.org/0000-0001-6757-4744",
        "date_created": "2025-06-23T11:57:25Z",
        "notes": "This is a duplicate of row 57 - already exists in the template"
    },
    "row_140": {
        "row_number": 140,
        "defined_class": "",
        "label": "segmental branch of lobar artery of spleen",
        "FMA_xref": "",
        "parent": "UBERON:0001637",  # artery
        "location": "UBERON:0000916",  # abdomen
        "definition": "An artery that branches from a lobar artery of the spleen and supplies a segment of splenic tissue.",
        "xrefs": "https://ijcrr.com/uploads/759_pdf.pdf",
        "synonym": "segmental artery of spleen|splenic segmental artery",
        "synonym_xrefs": "",
        "connecting_branch_of": "UBERON:8920049",  # lobar artery of spleen
        "vessel_supplies_blood_to": "UBERON:0002106",  # spleen
        "creator": "https://orcid.org/0000-0001-6757-4744",
        "date_created": timestamp,
        "notes": "Branches from lobar artery, supplies segmental regions within spleen lobes"
    },
    "row_156": {
        "row_number": 156,
        "defined_class": "",
        "label": "superior lobar artery of spleen",
        "FMA_xref": "",
        "parent": "UBERON:0001637",
        "location": "UBERON:0000916",
        "definition": "An artery that branches from the splenic artery at the splenic hilum and supplies the superior portion of the spleen.",
        "xrefs": "https://ijcrr.com/uploads/759_pdf.pdf",
        "synonym": "superior splenic lobar artery",
        "synonym_xrefs": "",
        "connecting_branch_of": "UBERON:0001194",  # splenic artery
        "vessel_supplies_blood_to": "UBERON:0002106",  # spleen
        "creator": "https://orcid.org/0000-0001-6757-4744",
        "date_created": timestamp,
        "notes": "Branches from splenic artery at hilum, supplies superior region of spleen"
    }
}

# Generate reporting table with labels
reporting_table = {
    "summary": "Spleen artery entries processed based on anatomical branching pattern",
    "reference": "https://ijcrr.com/uploads/759_pdf.pdf",
    "template_row": "Row 57 (lobar artery of spleen)",
    "ontology_terms_used": {
        "UBERON:0001637": "artery",
        "UBERON:0000916": "abdomen",
        "UBERON:0001194": "splenic artery",
        "UBERON:0001248": "hilum of spleen",
        "UBERON:0002106": "spleen",
        "UBERON:8920049": "lobar artery of spleen"
    },
    "anatomical_hierarchy": [
        "splenic artery (UBERON:0001194)",
        "  └─ superior lobar artery of spleen (row 156)",
        "  └─ inferior lobar artery of spleen (row 78)",
        "  └─ lobar artery of spleen (row 102/57 - generic term)",
        "      └─ segmental branch of lobar artery of spleen (row 140)"
    ],
    "entries": entries
}

# Save to JSON
output_path = "/Users/do12/Documents/GitHub/Uberon_vessel_template_agentic_edits/output/batch6_spleen.json"
with open(output_path, 'w') as f:
    json.dump(reporting_table, f, indent=2)

print(f"Generated {len(entries)} entries")
print(f"Saved to: {output_path}")

# Print summary
print("\n=== SUMMARY ===")
for row_key, entry in entries.items():
    print(f"\n{row_key} (Row {entry['row_number']}): {entry['label']}")
    print(f"  Parent: {entry['parent']}")
    print(f"  Branches from: {entry['connecting_branch_of']}")
    print(f"  Supplies: {entry['vessel_supplies_blood_to']}")
    print(f"  Definition: {entry['definition'][:80]}...")
