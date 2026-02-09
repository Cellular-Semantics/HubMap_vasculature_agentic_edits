#!/usr/bin/env python3
"""
Process cerebral artery entries for UBERON vessel template.
Based on anatomical information and ontology terms.
"""

import json
from datetime import datetime

# Define the entries to process
entries = {
    79: {
        "label": "inferior parietal artery",
        "parent": "UBERON:0001637",  # artery
        "location": "UBERON:0000955",  # brain
        "definition": "An artery that branches from the middle cerebral artery and supplies the inferior parietal cortex.",
        "xrefs": "https://doi.org/10.3171/jns.1978.49.2.0204",
        "connecting_branch_of": "UBERON:0001627",  # middle cerebral artery
        "vessel_supplies_blood_to": "UBERON:0006088",  # inferior parietal cortex
        "reference": "DOI:10.3171/jns.1978.49.2.0204 - Neurosurgery paper on cerebral artery anatomy",
        "justification": "The inferior parietal artery is a cortical branch of the middle cerebral artery that supplies the inferior parietal lobule/cortex."
    },
    111: {
        "label": "medial lenticulostriate artery",
        "parent": "UBERON:0001637",  # artery
        "location": "UBERON:0000955",  # brain
        "definition": "An artery that branches from the anterior cerebral artery and supplies the striatum.",
        "xrefs": "https://en.wikipedia.org/wiki/Anterior_cerebral_artery",
        "connecting_branch_of": "UBERON:0001624",  # anterior cerebral artery
        "vessel_supplies_blood_to": "UBERON:0002435",  # striatum
        "reference": "Wikipedia - Anterior cerebral artery",
        "justification": "The medial lenticulostriate arteries (also known as recurrent artery of Heubner) branch from the anterior cerebral artery and supply the striatum (caudate nucleus and putamen)."
    },
    120: {
        "label": "middle internal frontal artery",
        "parent": "UBERON:0001637",  # artery
        "location": "UBERON:0000955",  # brain
        "definition": "An artery that branches from the anterior cerebral artery and supplies the middle portion of the frontal lobe on the medial surface.",
        "xrefs": "https://doi.org/10.3171/jns.1978.49.2.0204",
        "connecting_branch_of": "UBERON:0001624",  # anterior cerebral artery
        "vessel_supplies_blood_to": "UBERON:0016525",  # frontal lobe
        "reference": "DOI:10.3171/jns.1978.49.2.0204 - Neurosurgery paper on cerebral artery anatomy",
        "justification": "The middle internal frontal artery is a cortical branch of the anterior cerebral artery supplying the medial frontal lobe."
    },
    122: {
        "label": "orbitofrontal branch of anterior cerebral artery",
        "parent": "UBERON:0001637",  # artery
        "location": "UBERON:0000955",  # brain
        "definition": "An artery that branches from the anterior cerebral artery and supplies the medial orbital frontal cortex.",
        "xrefs": "http://radiopaedia.org/articles/orbitofrontal-artery",
        "connecting_branch_of": "UBERON:0001624",  # anterior cerebral artery
        "vessel_supplies_blood_to": "UBERON:0022352",  # medial orbital frontal cortex
        "reference": "Radiopaedia - Orbitofrontal artery",
        "justification": "The orbitofrontal artery branches from the A2 segment of the anterior cerebral artery and supplies the medial orbital frontal cortex."
    },
    123: {
        "label": "orbitofrontal branch of middle cerebral artery",
        "parent": "UBERON:0001637",  # artery
        "location": "UBERON:0000955",  # brain
        "definition": "An artery that branches from the middle cerebral artery and supplies the lateral orbital frontal cortex.",
        "xrefs": "https://en.wikipedia.org/wiki/Middle_cerebral_artery",
        "connecting_branch_of": "UBERON:0001627",  # middle cerebral artery
        "vessel_supplies_blood_to": "UBERON:0022352",  # medial orbital frontal cortex (using same as no specific lateral OFC found)
        "reference": "Wikipedia - Middle cerebral artery",
        "justification": "The orbitofrontal artery can arise from the middle cerebral artery and supplies portions of the orbital frontal cortex."
    },
    124: {
        "label": "paracentral artery",
        "parent": "UBERON:0001637",  # artery
        "location": "UBERON:0000955",  # brain
        "definition": "An artery that branches from the anterior cerebral artery and supplies the paracentral lobule.",
        "xrefs": "https://doi.org/10.3171/jns.1978.49.2.0204",
        "connecting_branch_of": "UBERON:0001624",  # anterior cerebral artery
        "vessel_supplies_blood_to": "UBERON:0035933",  # paracentral lobule
        "reference": "DOI:10.3171/jns.1978.49.2.0204 - Neurosurgery paper on cerebral artery anatomy",
        "justification": "The paracentral artery is a medial cortical branch of the anterior cerebral artery that supplies the paracentral lobule, which includes portions of the primary motor and sensory cortex."
    },
    128: {
        "label": "posterior internal frontal artery",
        "parent": "UBERON:0001637",  # artery
        "location": "UBERON:0000955",  # brain
        "definition": "An artery that branches from the anterior cerebral artery and supplies the posterior portion of the frontal lobe on the medial surface.",
        "xrefs": "https://doi.org/10.3171/jns.1978.49.2.0204",
        "connecting_branch_of": "UBERON:0001624",  # anterior cerebral artery
        "vessel_supplies_blood_to": "UBERON:0016525",  # frontal lobe
        "reference": "DOI:10.3171/jns.1978.49.2.0204 - Neurosurgery paper on cerebral artery anatomy",
        "justification": "The posterior internal frontal artery is a cortical branch of the anterior cerebral artery supplying the posterior medial frontal lobe."
    },
    157: {
        "label": "superior parietal artery",
        "parent": "UBERON:0001637",  # artery
        "location": "UBERON:0000955",  # brain
        "definition": "An artery that branches from the middle cerebral artery and supplies the superior parietal cortex.",
        "xrefs": "https://doi.org/10.3171/jns.1978.49.2.0204",
        "connecting_branch_of": "UBERON:0001627",  # middle cerebral artery
        "vessel_supplies_blood_to": "UBERON:0006094",  # superior parietal cortex
        "reference": "DOI:10.3171/jns.1978.49.2.0204 - Neurosurgery paper on cerebral artery anatomy",
        "justification": "The superior parietal artery is a cortical branch of the middle cerebral artery that supplies the superior parietal lobule/cortex."
    }
}

# Add creator and date
creator = "https://orcid.org/0000-0001-6677-8489"
date_created = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

# Format entries for TSV update
tsv_entries = {}
for row_num, data in entries.items():
    tsv_entries[row_num] = {
        "label": data["label"],
        "parent": data["parent"],
        "location": data["location"],
        "definition": data["definition"],
        "xrefs": data["xrefs"],
        "connecting_branch_of": data["connecting_branch_of"],
        "vessel_supplies_blood_to": data["vessel_supplies_blood_to"],
        "creator": creator,
        "date_created": date_created
    }

# Ontology term labels for reporting
ontology_labels = {
    "UBERON:0001637": "artery",
    "UBERON:0000955": "brain",
    "UBERON:0001624": "anterior cerebral artery",
    "UBERON:0001627": "middle cerebral artery",
    "UBERON:0001636": "posterior cerebral artery",
    "UBERON:0016525": "frontal lobe",
    "UBERON:0001872": "parietal lobe",
    "UBERON:0006088": "inferior parietal cortex",
    "UBERON:0006094": "superior parietal cortex",
    "UBERON:0022352": "medial orbital frontal cortex",
    "UBERON:0035933": "paracentral lobule",
    "UBERON:0002435": "striatum"
}

# Create output with labels
output = {
    "metadata": {
        "batch": "batch4_cerebral",
        "description": "Cerebral artery branches processed from DOI 10.3171/jns.1978.49.2.0204 and Wikipedia references",
        "date_processed": datetime.now().isoformat(),
        "processor": "Claude Sonnet 4.5"
    },
    "entries": [],
    "ontology_labels": ontology_labels,
    "justifications": {}
}

# Add entries with labels
for row_num, data in entries.items():
    entry = {
        "row": row_num,
        "label": data["label"],
        "parent": data["parent"],
        "parent_label": ontology_labels.get(data["parent"], ""),
        "location": data["location"],
        "location_label": ontology_labels.get(data["location"], ""),
        "definition": data["definition"],
        "xrefs": data["xrefs"],
        "connecting_branch_of": data["connecting_branch_of"],
        "connecting_branch_of_label": ontology_labels.get(data["connecting_branch_of"], ""),
        "vessel_supplies_blood_to": data["vessel_supplies_blood_to"],
        "vessel_supplies_blood_to_label": ontology_labels.get(data["vessel_supplies_blood_to"], ""),
        "creator": creator,
        "date_created": date_created
    }
    output["entries"].append(entry)

    # Add justification
    output["justifications"][str(row_num)] = {
        "label": data["label"],
        "reference": data["reference"],
        "justification": data["justification"]
    }

# Save to JSON
output_file = "/Users/do12/Documents/GitHub/Uberon_vessel_template_agentic_edits/output/batch4_cerebral.json"
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

print(f"Output saved to: {output_file}")
print(f"Processed {len(entries)} entries")
print("\nEntries processed:")
for row_num, data in entries.items():
    print(f"  Row {row_num}: {data['label']}")
