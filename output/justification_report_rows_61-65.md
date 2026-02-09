# Justification Report for Rows 61-65
## UBERON Vessel Template Edits

**Date:** 2026-02-02
**Editor:** Claude Sonnet 4.5
**Rows Edited:** 61-65 (First 5 incomplete entries)

---

## Overview

This report documents the population of five incomplete entries in the UBERON vessel template for proper palmar digital artery branches. All entries concern branches of proper palmar digital arteries that supply the fingers (manual digits 2-5) of the hand.

---

## Anatomical Background

### Proper Palmar Digital Arteries
Based on the UBERON ontology (UBERON:0006137), proper palmar digital arteries are defined as:

> "The proper palmar digital arteries travel along the sides of the phalanges (along the contiguous sides of the index, middle, ring, and little fingers), each artery lying just below its corresponding digital nerve. They anastomose freely in the subcutaneous tissue of the finger tips and by smaller branches near the interphalangeal joints. **Each also gives off a couple of dorsal branches which anastomose with the dorsal digital arteries, and supply the soft parts on the back of the second and third phalanges, including the matrix of the fingernail.**"

### Branching Pattern
From the superficial palmar arch (UBERON:0006564):
1. **Common palmar digital arteries** (UBERON:0001410) arise from the superficial palmar arch
2. Each common palmar digital artery divides into **two proper palmar digital arteries** (UBERON:0006137)
3. Each proper palmar digital artery travels along one side of a digit (lateral or medial)
4. Proper palmar digital arteries give off **dorsal branches** and **cutaneous branches**

---

## Literature Support

### Key Reference: PMID:16175116
**Title:** "Anatomic basis of dorsal finger skin cover"
**Finding:** This anatomical study documented dorsal cutaneous branches of proper palmar digital arteries that supply the dorsal skin of fingers.

**Abstract excerpt:**
> "This study describes the anatomy of the dorsal cutaneous vascular system of 180 digits from 18 pairs of fresh human cadaver hands... We showed that 2 constant branches in the proximal and middle phalanx from each proper digital artery have consistent sites of origin at predictable distances from the proximal interphalangeal joint for the long fingers."

This study confirms that proper palmar digital arteries consistently give off branches that supply the dorsal skin of the digits.

### Supporting Reference: PMID:36341235
**Title:** "Vascular supply of the metacarpophalangeal joint"

**Relevant excerpt:**
> "The metacarpal half receives arteries from the palmar metacarpal arteries or proper palmar digital arteries, while the phalangeal half is supplied by both proper and common palmar digital arteries."

This confirms the role of proper palmar digital arteries in supplying blood to digit structures.

---

## Ontology Terms Used

### Manual Digits (Location)
Using the ontology-term-lookup subagent, the following UBERON terms were identified:

| Digit | UBERON ID | Definition |
|-------|-----------|------------|
| Manual digit 5 (little finger) | UBERON:0003625 | 5th digit of the manus |
| Manual digit 4 (ring finger) | UBERON:0003624 | 4th digit of the manus |
| Manual digit 3 (middle finger) | UBERON:0003623 | 3rd digit of the manus |
| Manual digit 2 (index finger) | UBERON:0003622 | 2nd digit of the manus |

### Supplied Structures (vessel_supplies_blood_to)
- **Manual digit skin** (UBERON:0003533): "A zone of skin that is part of a finger"
- **Dorsal skin of finger** (UBERON:0005276): "A dorsal skin of digit that is part of a manual digit"

### Parent Artery (connecting_branch_of)
- **Proper palmar digital artery** (UBERON:0006137): General class for all proper palmar digital arteries

**Note:** UBERON does not currently contain specific terms for lateral/medial proper palmar digital arteries of individual digits. These would need to be created as new terms. For the purposes of this template, we use the general proper palmar digital artery class (UBERON:0006137) as the parent.

---

## Detailed Justification for Each Entry

### Row 61: Cutaneous branch of medial proper palmar digital artery of fifth digit of hand

**Fields Populated:**
- **FMA_xref:** (blank - no FMA term found)
- **parent:** UBERON:0001637 (arterial blood vessel)
- **location:** UBERON:0003625 (manual digit 5)
- **definition:** "An artery that branches from the medial proper palmar digital artery of the fifth digit and supplies the skin of the fifth digit of the hand."
- **xrefs:** https://en.wikipedia.org/wiki/Proper_palmar_digital_arteries|PMID:16175116
- **connecting_branch_of:** UBERON:0006137 (proper palmar digital artery)
- **vessel_supplies_blood_to:** UBERON:0003533 (manual digit skin)
- **creator:** https://orcid.org/0000-0001-6757-4744
- **date_created:** 2026-02-02T10:30:00Z

**Justification:**
This is a cutaneous branch supplying skin (not specifically dorsal). Based on PMID:16175116, proper palmar digital arteries give off branches to supply both palmar and dorsal skin surfaces. The term "cutaneous branch" indicates a branch supplying skin tissue generally.

---

### Row 62: Dorsal branch of lateral proper palmar digital artery of fifth digit of hand

**Fields Populated:**
- **FMA_xref:** (blank - no FMA term found)
- **parent:** UBERON:0001637 (arterial blood vessel)
- **location:** UBERON:0003625 (manual digit 5)
- **definition:** "An artery that branches from the lateral proper palmar digital artery of the fifth digit and supplies the dorsal skin of the fifth digit of the hand."
- **xrefs:** https://en.wikipedia.org/wiki/Proper_palmar_digital_arteries|PMID:16175116
- **connecting_branch_of:** UBERON:0006137 (proper palmar digital artery)
- **vessel_supplies_blood_to:** UBERON:0005276 (dorsal skin of finger)
- **creator:** https://orcid.org/0000-0001-6757-4744
- **date_created:** 2026-02-02T10:30:00Z

**Justification:**
From UBERON:0006137 definition: "Each also gives off a couple of dorsal branches which anastomose with the dorsal digital arteries, and supply the soft parts on the back of the second and third phalanges, including the matrix of the fingernail."

PMID:16175116 confirms these dorsal branches are consistent anatomical features.

---

### Row 63: Dorsal branch of lateral proper palmar digital artery of fourth digit of hand

**Fields Populated:**
- **FMA_xref:** (blank - no FMA term found)
- **parent:** UBERON:0001637 (arterial blood vessel)
- **location:** UBERON:0003624 (manual digit 4)
- **definition:** "An artery that branches from the lateral proper palmar digital artery of the fourth digit and supplies the dorsal skin of the fourth digit of the hand."
- **xrefs:** https://en.wikipedia.org/wiki/Proper_palmar_digital_arteries|PMID:16175116
- **connecting_branch_of:** UBERON:0006137 (proper palmar digital artery)
- **vessel_supplies_blood_to:** UBERON:0005276 (dorsal skin of finger)
- **creator:** https://orcid.org/0000-0001-6757-4744
- **date_created:** 2026-02-02T10:30:00Z

**Justification:**
Same anatomical pattern as row 62, but for the fourth digit (ring finger). The study PMID:16175116 examined "180 digits (36 thumbs, index, middle, ring, and little fingers)" and found consistent dorsal branches for all long fingers.

---

### Row 64: Dorsal branch of lateral proper palmar digital artery of second digit of hand

**Fields Populated:**
- **FMA_xref:** (blank - no FMA term found)
- **parent:** UBERON:0001637 (arterial blood vessel)
- **location:** UBERON:0003622 (manual digit 2)
- **definition:** "An artery that branches from the lateral proper palmar digital artery of the second digit and supplies the dorsal skin of the second digit of the hand."
- **xrefs:** https://en.wikipedia.org/wiki/Proper_palmar_digital_arteries|PMID:16175116
- **connecting_branch_of:** UBERON:0006137 (proper palmar digital artery)
- **vessel_supplies_blood_to:** UBERON:0005276 (dorsal skin of finger)
- **creator:** https://orcid.org/0000-0001-6757-4744
- **date_created:** 2026-02-02T10:30:00Z

**Justification:**
Same anatomical pattern for the second digit (index finger). Consistent with findings in PMID:16175116.

---

### Row 65: Dorsal branch of lateral proper palmar digital artery of third digit of hand

**Fields Populated:**
- **FMA_xref:** (blank - no FMA term found)
- **parent:** UBERON:0001637 (arterial blood vessel)
- **location:** UBERON:0003623 (manual digit 3)
- **definition:** "An artery that branches from the lateral proper palmar digital artery of the third digit and supplies the dorsal skin of the third digit of the hand."
- **xrefs:** https://en.wikipedia.org/wiki/Proper_palmar_digital_arteries|PMID:16175116
- **connecting_branch_of:** UBERON:0006137 (proper palmar digital artery)
- **vessel_supplies_blood_to:** UBERON:0005276 (dorsal skin of finger)
- **creator:** https://orcid.org/0000-0001-6757-4744
- **date_created:** 2026-02-02T10:30:00Z

**Justification:**
Same anatomical pattern for the third digit (middle finger). Consistent with findings in PMID:16175116.

---

## Pattern Consistency

All five entries follow established patterns from completed entries in the template:

1. **Parent class:** UBERON:0001637 (arterial blood vessel) - standard for all arteries
2. **Location:** The specific digit (UBERON:0003622-0003625)
3. **Definition format:** "An artery that branches from [parent] and supplies [structure]"
4. **connecting_branch_of:** UBERON:0006137 (proper palmar digital artery - general class)
5. **vessel_supplies_blood_to:** Appropriate skin structure
6. **Creator ORCID:** https://orcid.org/0000-0001-6757-4744 (consistent with recent entries)
7. **Date format:** ISO 8601 timestamp

---

## Ontology Gaps Identified

During this work, the following gaps in UBERON were identified:

1. **No specific terms for lateral/medial proper palmar digital arteries by digit**
   - Currently exists: UBERON:0006137 (general proper palmar digital artery)
   - Missing: Digit-specific and side-specific (lateral/medial) terms

2. **No digit-specific skin terms**
   - Currently exists: UBERON:0003533 (manual digit skin - general)
   - Currently exists: UBERON:0005276 (dorsal skin of finger - general)
   - Missing: Digit-specific skin terms (e.g., "skin of manual digit 5")

These specific terms would need to be created as new UBERON entries if greater granularity is required.

---

## References

1. **PMID:16175116** - Anatomic basis of dorsal finger skin cover. Primary anatomical study documenting dorsal branches of proper palmar digital arteries.

2. **PMID:36341235** - Vascular supply of the metacarpophalangeal joint. Supporting evidence for proper palmar digital artery distribution.

3. **UBERON Ontology** - Definitions retrieved via OLS4 ontology-term-lookup subagent:
   - UBERON:0006137 (proper palmar digital artery)
   - UBERON:0006564 (superficial palmar arch)
   - UBERON:0001410 (common palmar digital artery)
   - UBERON:0003622-0003625 (manual digits 2-5)
   - UBERON:0003533 (manual digit skin)
   - UBERON:0005276 (dorsal skin of finger)

4. **Wikipedia** - Proper palmar digital arteries: https://en.wikipedia.org/wiki/Proper_palmar_digital_arteries (reference cited in original incomplete entries)

---

## Summary

Five incomplete entries (rows 61-65) have been successfully populated with:
- Appropriate anatomical locations (specific digits)
- Evidence-based definitions supported by PMID:16175116
- Correct ontology term assignments from UBERON
- Consistent formatting with existing completed entries
- Proper references documenting the anatomical relationships

All edits follow the DOSDP pattern specification and are consistent with the existing template structure.
