#!/usr/bin/env python3
"""
Process plantar digital artery entries for UBERON vessel template.
Based on anatomical references from Radiopaedia and NCBI sources.
"""

import json
from datetime import datetime

# Anatomical information from references
ANATOMICAL_INFO = {
    "common_plantar_digital": {
        "parent": "UBERON:0035195",  # plantar metatarsal artery
        "parent_label": "plantar metatarsal artery",
        "location": "UBERON:0002387",  # foot
        "location_label": "foot",
        "connecting_branch_of": "UBERON:0035195",  # plantar metatarsal artery
        "connecting_branch_of_label": "plantar metatarsal artery",
        "definition_template": "An artery that is a branch of the {ordinal} plantar metatarsal artery and divides into medial and lateral proper plantar digital arteries to supply the adjacent sides of the {digit_pair}.",
        "justification": "Plantar metatarsal arteries branch from the plantar arch and each divides into a pair of plantar digital arteries (common plantar digital arteries) which supply the adjacent sides of the toes. This anatomical organization is analogous to the palmar digital arteries in the hand."
    },
    "proper_plantar_digital": {
        "parent": "UBERON:0004540",  # proper plantar digital artery
        "parent_label": "proper plantar digital artery",
        "location": "UBERON:0002387",  # foot
        "location_label": "foot",
        "connecting_branch_of": "UBERON:0002455",  # common plantar digital arteries
        "connecting_branch_of_label": "common plantar digital arteries",
        "definition_template": "An artery that is a branch of a common plantar digital artery and supplies the {side} side of the {digit_name}.",
        "justification": "Common plantar digital arteries divide into pairs of proper plantar digital arteries which supply the medial and lateral sides of the toes. This pattern mirrors the proper palmar digital arteries in the hand."
    }
}

# Digit information
DIGITS = {
    1: {"name": "first digit of foot", "uberon": "UBERON:0003631", "common_name": "hallux (big toe)"},
    2: {"name": "second digit of foot", "uberon": "UBERON:0003632", "common_name": "second toe"},
    3: {"name": "third digit of foot", "uberon": "UBERON:0003633", "common_name": "third toe"},
    4: {"name": "fourth digit of foot", "uberon": "UBERON:0003634", "common_name": "fourth toe"},
    5: {"name": "fifth digit of foot", "uberon": "UBERON:0003635", "common_name": "fifth toe (little toe)"}
}

ORDINALS = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth"
}

def create_common_plantar_digital_entry(digit_num, row_num):
    """Create entry for common plantar digital artery."""
    ordinal = ORDINALS[digit_num]
    digit_info = DIGITS[digit_num]
    next_digit = DIGITS[digit_num + 1]

    # Common plantar digital arteries supply between two adjacent digits
    digit_pair = f"{digit_info['common_name']} and {next_digit['common_name']}"

    entry = {
        "row_number": row_num,
        "label": f"{ordinal} common plantar digital artery",
        "FMA_xref": "Not found in FMA",
        "parent": ANATOMICAL_INFO["common_plantar_digital"]["parent"],
        "parent_label": ANATOMICAL_INFO["common_plantar_digital"]["parent_label"],
        "location": ANATOMICAL_INFO["common_plantar_digital"]["location"],
        "location_label": ANATOMICAL_INFO["common_plantar_digital"]["location_label"],
        "definition": ANATOMICAL_INFO["common_plantar_digital"]["definition_template"].format(
            ordinal=ordinal,
            digit_pair=digit_pair
        ),
        "connecting_branch_of": ANATOMICAL_INFO["common_plantar_digital"]["connecting_branch_of"],
        "connecting_branch_of_label": ANATOMICAL_INFO["common_plantar_digital"]["connecting_branch_of_label"],
        "vessel_supplies_blood_to": f"{digit_info['uberon']}|{next_digit['uberon']}",
        "vessel_supplies_blood_to_label": f"{digit_info['name']}|{next_digit['name']}",
        "justification": ANATOMICAL_INFO["common_plantar_digital"]["justification"] + f" The {ordinal} common plantar digital artery supplies the adjacent sides of the {digit_pair}."
    }

    return entry

def create_proper_plantar_digital_entry(side, digit_num, row_num):
    """Create entry for proper plantar digital artery (lateral or medial)."""
    digit_info = DIGITS[digit_num]

    entry = {
        "row_number": row_num,
        "label": f"{side} proper plantar digital artery of {digit_info['name']}",
        "FMA_xref": "Not found in FMA",
        "parent": ANATOMICAL_INFO["proper_plantar_digital"]["parent"],
        "parent_label": ANATOMICAL_INFO["proper_plantar_digital"]["parent_label"],
        "location": ANATOMICAL_INFO["proper_plantar_digital"]["location"],
        "location_label": ANATOMICAL_INFO["proper_plantar_digital"]["location_label"],
        "definition": ANATOMICAL_INFO["proper_plantar_digital"]["definition_template"].format(
            side=side,
            digit_name=digit_info['common_name']
        ),
        "connecting_branch_of": ANATOMICAL_INFO["proper_plantar_digital"]["connecting_branch_of"],
        "connecting_branch_of_label": ANATOMICAL_INFO["proper_plantar_digital"]["connecting_branch_of_label"],
        "vessel_supplies_blood_to": digit_info['uberon'],
        "vessel_supplies_blood_to_label": digit_info['name'],
        "justification": ANATOMICAL_INFO["proper_plantar_digital"]["justification"] + f" The {side} proper plantar digital artery supplies the {side} side of the {digit_info['common_name']}."
    }

    return entry

def main():
    """Process all plantar digital artery entries."""
    entries = []

    # Common plantar digital arteries (between adjacent digits)
    # Row 73: first common plantar digital artery (between digits 1 and 2)
    entries.append(create_common_plantar_digital_entry(1, 73))

    # Row 138: second common plantar digital artery (between digits 2 and 3)
    entries.append(create_common_plantar_digital_entry(2, 138))

    # Row 160: third common plantar digital artery (between digits 3 and 4)
    entries.append(create_common_plantar_digital_entry(3, 160))

    # Row 75: fourth common plantar digital artery (between digits 4 and 5)
    entries.append(create_common_plantar_digital_entry(4, 75))

    # Lateral proper plantar digital arteries
    # Row 91: lateral proper plantar digital artery of first digit
    entries.append(create_proper_plantar_digital_entry("lateral", 1, 91))

    # Row 93: lateral proper plantar digital artery of second digit
    entries.append(create_proper_plantar_digital_entry("lateral", 2, 93))

    # Row 94: lateral proper plantar digital artery of third digit
    entries.append(create_proper_plantar_digital_entry("lateral", 3, 94))

    # Row 92: lateral proper plantar digital artery of fourth digit
    entries.append(create_proper_plantar_digital_entry("lateral", 4, 92))

    # Row 90: lateral proper plantar digital artery of fifth digit
    entries.append(create_proper_plantar_digital_entry("lateral", 5, 90))

    # Medial proper plantar digital arteries
    # Row 114: medial proper plantar digital artery of first digit
    entries.append(create_proper_plantar_digital_entry("medial", 1, 114))

    # Row 116: medial proper plantar digital artery of second digit
    entries.append(create_proper_plantar_digital_entry("medial", 2, 116))

    # Row 117: medial proper plantar digital artery of third digit
    entries.append(create_proper_plantar_digital_entry("medial", 3, 117))

    # Row 115: medial proper plantar digital artery of fourth digit
    entries.append(create_proper_plantar_digital_entry("medial", 4, 115))

    # Row 113: medial proper plantar digital artery of fifth digit
    entries.append(create_proper_plantar_digital_entry("medial", 5, 113))

    # Save to JSON file
    output_file = "/Users/do12/Documents/GitHub/Uberon_vessel_template_agentic_edits/output/batch5_plantar.json"
    with open(output_file, 'w') as f:
        json.dump(entries, f, indent=2)

    print(f"Successfully processed {len(entries)} plantar digital artery entries")
    print(f"Output saved to: {output_file}")

    # Print summary
    print("\nSummary:")
    print(f"  Common plantar digital arteries: 4")
    print(f"  Lateral proper plantar digital arteries: 5")
    print(f"  Medial proper plantar digital arteries: 5")
    print(f"  Total entries: {len(entries)}")

if __name__ == "__main__":
    main()
