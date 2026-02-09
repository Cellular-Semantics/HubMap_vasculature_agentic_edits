# Batch 1 Artery Entries - Detailed Report

## Processing Summary
This report documents the research and ontology term identification for 5 artery entries from the UBERON vessel template, using Wikipedia references and the Ontology Lookup Service (OLS).

---

## Entry 1: Row 71 - Dorsal Meningeal Artery

### Source Reference
- **Wikipedia URL**: https://en.wikipedia.org/wiki/Meningohypophyseal_artery

### Anatomical Information Extracted
The Wikipedia article states:
> "The meningohypophyseal artery, or meningohypophyseal trunk, is an inconstant branch of the cavernous segment of the internal carotid artery. Classically, the meningohypophyseal artery has three named branches: Dorsal meningeal artery, Inferior hypophyseal artery, Tentorial artery."

### Ontology Terms Identified
- **Parent vessel**: UBERON:0001532 (internal carotid artery)
  - Definition: "A terminal branch of the left or right common carotid artery which supplies oxygenated blood to the brain and eyes"
- **Location**: UBERON:0003712 (cavernous sinus)
  - Definition: "The cavernous sinus (or lateral sellar compartment), within the human head, is a large collection of thin-walled veins creating a cavity bordered by the temporal bone of the skull and the sphenoid bone, lateral to the sella turcica"
- **Supplies**: UBERON:0002363 (dura mater)
- **FMA Cross-reference**: Not found in FMA database

### Proposed Definition
"An artery that is a branch of the meningohypophyseal artery, which itself arises from the cavernous segment of the internal carotid artery, and supplies the dura mater of the meninges."

### Justification
The dorsal meningeal artery is one of three branches of the meningohypophyseal artery, which arises from the cavernous (C4) segment of the internal carotid artery. This branch specifically supplies the dura mater covering the clivus and posterior cranial fossa region. The anatomical location is within or adjacent to the cavernous sinus region.

---

## Entry 2: Row 77 - Hypoglossal Branch of Ascending Pharyngeal Artery

### Source Reference
- **Wikipedia URL**: https://en.wikipedia.org/wiki/Ascending_pharyngeal_artery

### Anatomical Information Extracted
The Wikipedia article states:
> "The artery most typically bifurcates into embryologically distinct pharyngeal and neuromeningeal trunks. The neuromeningeal trunk classically consists of jugular and hypoglossal divisions, which enter the jugular and hypoglossal foramina to supply regional meningeal and neural structures."

Additional context:
> "The ascending pharyngeal artery is an artery of the neck that supplies the pharynx. It is the smallest and first medial branch of proximal external carotid artery, arising from the medial surface of the artery."

From the infobox:
- **Source**: External carotid artery (FMA:49497 for ascending pharyngeal)
- **Supplies**: Pharynx

### Ontology Terms Identified
- **Parent vessel**: UBERON:8600078 (ascending pharyngeal artery)
  - Definition: "An artery of the neck that branches from the external carotid artery and supplies the pharynx"
- **Location**: UBERON:0006682 (hypoglossal canal)
- **Supplies**: UBERON:0002363 (dura mater)
- **Connecting branch of**: UBERON:8600078 (ascending pharyngeal artery)
- **FMA Cross-reference**: Parent artery is FMA:49497

### Proposed Definition
"An artery that is a branch of the neuromeningeal trunk of the ascending pharyngeal artery, which enters the hypoglossal canal to supply regional meningeal and neural structures."

### Justification
The hypoglossal branch is part of the neuromeningeal trunk division of the ascending pharyngeal artery. It enters the skull through the hypoglossal canal (also known as the anterior condylar foramen) and supplies the dura mater in this region along with neural structures associated with the hypoglossal nerve.

---

## Entry 3: Row 82 - Jugular Branch of Ascending Pharyngeal Artery

### Source Reference
- **Wikipedia URL**: https://en.wikipedia.org/wiki/Ascending_pharyngeal_artery (same as entry 2)

### Anatomical Information Extracted
As noted above, the Wikipedia article states:
> "The neuromeningeal trunk classically consists of jugular and hypoglossal divisions, which enter the jugular and hypoglossal foramina to supply regional meningeal and neural structures."

### Ontology Terms Identified
- **Parent vessel**: UBERON:8600078 (ascending pharyngeal artery)
- **Location**: UBERON:0005456 (jugular foramen)
- **Supplies**: UBERON:0002363 (dura mater)
- **Connecting branch of**: UBERON:8600078 (ascending pharyngeal artery)
- **FMA Cross-reference**: Parent artery is FMA:49497

### Proposed Definition
"An artery that is a branch of the neuromeningeal trunk of the ascending pharyngeal artery, which enters the jugular foramen to supply regional meningeal and neural structures."

### Justification
The jugular branch is the other main division of the neuromeningeal trunk of the ascending pharyngeal artery. It enters the skull through the jugular foramen and supplies the dura mater of the posterior cranial fossa. This branch is in hemodynamic equilibrium with branches from other arteries including the vertebral, occipital, and posterior meningeal arteries.

---

## Entry 4: Row 96 - Lateral Sural Artery

### Source Reference
- **Wikipedia URL**: https://en.wikipedia.org/wiki/Sural_arteries

### Anatomical Information Extracted
The Wikipedia article states:
> "The sural arteries (inferior muscular arteries) are two large branches, lateral and medial, which are distributed to the gastrocnemius, soleus, and plantaris muscles. Sural means related to the calf. The term applies to any of four or five arteries arising from the popliteal artery, with distribution to the muscles and integument of the calf, and with anastomoses to the posterior tibial, medial and lateral inferior genicular arteries."

From the infobox:
- **Source**: Popliteal artery
- **FMA**: 22570 (for sural arteries collectively)

### Ontology Terms Identified
- **Parent vessel**: UBERON:0002250 (popliteal artery)
  - Definition: "The continuation of the femoral artery coursing through the popliteal fossa; it divides into the anterior and posterior tibial arteries"
- **Location**: UBERON:8480048 (calf)
- **Supplies**:
  - UBERON:0001388 (gastrocnemius) - "The most superficial muscle of the triceps surae group, in the posterior portion of the lower hindleg"
  - UBERON:0001389 (soleus muscle) - "A deep muscle of the triceps surae group, in the superficial posterior compartment of the leg"
  - UBERON:0011905 (plantaris) - A vestigial plantar flexor muscle
- **Connecting branch of**: UBERON:0002250 (popliteal artery)
- **FMA Cross-reference**: FMA:22570 (sural arteries, collective term)

### Proposed Definition
"An artery that is one of the lateral branches of the sural arteries arising from the popliteal artery, distributed to the gastrocnemius, soleus, and plantaris muscles in the calf of the leg."

### Justification
The lateral sural artery is explicitly described as one of the two large branches (lateral and medial) of the sural arterial system. These arteries arise from the popliteal artery in the popliteal fossa and descend to supply the three muscles of the posterior superficial compartment of the leg: gastrocnemius, soleus, and plantaris. The term "sural" derives from the Latin "sura" meaning calf.

---

## Entry 5: Row 118 - Medial Sural Artery

### Source Reference
- **Wikipedia URL**: https://en.wikipedia.org/wiki/Sural_arteries (same as entry 4)

### Anatomical Information Extracted
As noted for the lateral sural artery, the Wikipedia article describes:
> "The sural arteries (inferior muscular arteries) are two large branches, lateral and medial, which are distributed to the gastrocnemius, soleus, and plantaris muscles."

### Ontology Terms Identified
- **Parent vessel**: UBERON:0002250 (popliteal artery)
- **Location**: UBERON:8480048 (calf)
- **Supplies**:
  - UBERON:0001388 (gastrocnemius)
  - UBERON:0001389 (soleus muscle)
  - UBERON:0011905 (plantaris)
- **Connecting branch of**: UBERON:0002250 (popliteal artery)
- **FMA Cross-reference**: FMA:22570 (sural arteries, collective term)

### Proposed Definition
"An artery that is one of the medial branches of the sural arteries arising from the popliteal artery, distributed to the gastrocnemius, soleus, and plantaris muscles in the calf of the leg."

### Justification
The medial sural artery is the paired branch to the lateral sural artery. Both arise from the popliteal artery and supply the same muscle groups in the posterior calf. The medial branch typically supplies more of the medial head of the gastrocnemius muscle, while the lateral branch supplies more of the lateral head, but there is overlap in their distribution territories.

---

## Methodology Notes

### Data Sources
1. **Wikipedia**: Used to extract anatomical relationships, parent vessels, location, and tissues supplied
2. **OLS (Ontology Lookup Service)**: Used to identify and verify UBERON and FMA terms
3. **Search strategy**: Searched for parent vessels, anatomical locations, and tissues supplied

### Ontology Term Selection Criteria
- Prioritized UBERON terms as specified in the project requirements
- Used OLS search and fetch functions to verify term definitions
- Selected the most specific anatomical terms available
- For multiple tissue targets, used pipe-separated (|) format

### Challenges and Limitations
1. **FMA terms**: Some specific arterial branches are not present in FMA, though parent arteries are well-represented
2. **Meningeal arteries**: These are often described as branches of branches, requiring careful parsing of the hierarchical relationships
3. **Sural arteries**: FMA provides only a collective term for all sural arteries, not individual lateral/medial branches

### Recommendations for Template Updates
1. All five entries can be populated with the identified terms
2. Definitions follow the standard DOSDP pattern for vessels
3. Additional cross-references to SNOMED-CT could be added if needed
4. Consider adding anatomical hierarchy information (e.g., specifying the meningohypophyseal trunk as an intermediate branch)

---

## Summary Table

| Row | Artery Name | Parent (UBERON) | Location (UBERON) | Supplies (UBERON) |
|-----|-------------|-----------------|-------------------|-------------------|
| 71  | dorsal meningeal artery | 0001532 (internal carotid) | 0003712 (cavernous sinus) | 0002363 (dura mater) |
| 77  | hypoglossal branch of ascending pharyngeal | 8600078 (ascending pharyngeal) | 0006682 (hypoglossal canal) | 0002363 (dura mater) |
| 82  | jugular branch of ascending pharyngeal | 8600078 (ascending pharyngeal) | 0005456 (jugular foramen) | 0002363 (dura mater) |
| 96  | lateral sural artery | 0002250 (popliteal artery) | 8480048 (calf) | 0001388\|0001389\|0011905 |
| 118 | medial sural artery | 0002250 (popliteal artery) | 8480048 (calf) | 0001388\|0001389\|0011905 |

---

## Files Generated
1. `batch1_results.json` - Structured JSON data for all 5 entries
2. `batch1_detailed_report.md` - This comprehensive report with justifications

Date: 2026-02-09
