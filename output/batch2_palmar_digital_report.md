# Proper Palmar Digital Artery Branches Processing Report

**Date:** 2026-02-09
**Batch:** batch2_palmar_digital
**Rows Processed:** 61-69
**Reference:** https://en.wikipedia.org/wiki/Proper_palmar_digital_arteries

## Summary

This report documents the completion of 9 entries (rows 61-69) in the UBERON vessel template for proper palmar digital artery branches. All entries reference the Wikipedia article on proper palmar digital arteries, which provides detailed anatomical information about these vessels.

## Reference Information

### From Wikipedia (Wikidata: Q6577825)

The proper palmar digital arteries travel along the sides of the phalanges (along the contiguous sides of the index, middle, ring, and little fingers), each artery lying just below (dorsal to) its corresponding digital nerve.

**Key Anatomical Facts:**

1. **Origin:** The proper palmar digital artery for the medial side of the little finger (5th digit) arises directly from the ulnar artery deep to the palmaris brevis muscle, but the rest arise from the common palmar digital arteries.

2. **Course:** They travel along the sides of the phalanges of the fingers.

3. **Branches:**
   - **Dorsal branches:** Anastomose with the dorsal digital arteries and supply the soft parts on the back of the second and third phalanges, including the matrix of the fingernail.
   - **Cutaneous branches:** Supply the skin of the fingers.

4. **Anastomoses:** They anastomose freely in the subcutaneous tissue of the finger tips and by smaller branches near the interphalangeal joints.

### From UBERON:0006137 (Proper Palmar Digital Artery)

The UBERON definition confirms: "Each also gives off a couple of dorsal branches which anastomose with the dorsal digital arteries, and supply the soft parts on the back of the second and third phalanges, including the matrix of the fingernail."

## Completed Entries Table

| Row | Label | Parent | Parent Label | Location | Location Label | Connecting Branch Of | Vessel Supplies |
|-----|-------|--------|--------------|----------|----------------|---------------------|----------------|
| 61 | cutaneous branch of medial proper palmar digital artery of fifth digit of hand | UBERON:0001637 | artery | UBERON:0003625 | manual digit 5 | UBERON:0006137 (proper palmar digital artery) | UBERON:0003533 (skin of finger) |
| 62 | dorsal branch of lateral proper palmar digital artery of fifth digit of hand | UBERON:0001637 | artery | UBERON:0003625 | manual digit 5 | UBERON:0006137 (proper palmar digital artery) | UBERON:0003625 (manual digit 5) |
| 63 | dorsal branch of lateral proper palmar digital artery of fourth digit of hand | UBERON:0001637 | artery | UBERON:0003624 | manual digit 4 | UBERON:0006137 (proper palmar digital artery) | UBERON:0003624 (manual digit 4) |
| 64 | dorsal branch of lateral proper palmar digital artery of second digit of hand | UBERON:0001637 | artery | UBERON:0003622 | manual digit 2 | UBERON:0006137 (proper palmar digital artery) | UBERON:0003622 (manual digit 2) |
| 65 | dorsal branch of lateral proper palmar digital artery of third digit of hand | UBERON:0001637 | artery | UBERON:0003623 | manual digit 3 | UBERON:0006137 (proper palmar digital artery) | UBERON:0003623 (manual digit 3) |
| 66 | dorsal branch of medial proper palmar digital artery of fifth digit of hand | UBERON:0001637 | artery | UBERON:0003625 | manual digit 5 | UBERON:0006137 (proper palmar digital artery) | UBERON:0003625 (manual digit 5) |
| 67 | dorsal branch of medial proper palmar digital artery of fourth digit of hand | UBERON:0001637 | artery | UBERON:0003624 | manual digit 4 | UBERON:0006137 (proper palmar digital artery) | UBERON:0003624 (manual digit 4) |
| 68 | dorsal branch of medial proper palmar digital artery of second digit of hand | UBERON:0001637 | artery | UBERON:0003622 | manual digit 2 | UBERON:0006137 (proper palmar digital artery) | UBERON:0003622 (manual digit 2) |
| 69 | dorsal branch of medial proper palmar digital artery of third digit of hand | UBERON:0001637 | artery | UBERON:0003623 | manual digit 3 | UBERON:0006137 (proper palmar digital artery) | UBERON:0003623 (manual digit 3) |

## Detailed Entry Justifications

### Row 61: Cutaneous Branch of Medial Proper Palmar Digital Artery of Fifth Digit

**Definition:** An artery that branches from the medial proper palmar digital artery and supplies the skin of the medial side of the fifth digit of the hand.

**Justification:** According to Wikipedia, proper palmar digital arteries have cutaneous branches. The medial proper palmar digital artery of the fifth digit (little finger) arises directly from the ulnar artery and supplies the medial (ulnar) side of the digit. Cutaneous branches specifically supply the skin of the finger.

**Ontology Mapping:**
- Parent: UBERON:0001637 (artery)
- Location: UBERON:0003625 (manual digit 5)
- Connecting branch of: UBERON:0006137 (proper palmar digital artery)
- Supplies: UBERON:0003533 (skin of finger)

---

### Rows 62-69: Dorsal Branches

All dorsal branch entries follow the same anatomical pattern with digit-specific variations.

**General Definition Pattern:** An artery that branches from the [lateral/medial] proper palmar digital artery of the [digit number] and anastomoses with the dorsal digital artery, supplying the soft tissue on the dorsal aspect of the second and third phalanges of the [digit number] of the hand.

**Justification:** Wikipedia explicitly states that proper palmar digital arteries "give off a couple of dorsal branches which anastomose with the dorsal digital arteries, and supply the soft parts on the back of the second and third phalanges, including the matrix of the fingernail." This is confirmed by the UBERON definition for proper palmar digital artery (UBERON:0006137).

**Anatomical Pattern:**
- Each finger has two proper palmar digital arteries: lateral (radial side) and medial (ulnar side)
- Each proper palmar digital artery gives off dorsal branches
- Dorsal branches anastomose with dorsal digital arteries (UBERON:0006146)
- They supply soft tissue on the dorsal aspect of the phalanges

**Ontology Mapping (consistent across all dorsal branches):**
- Parent: UBERON:0001637 (artery)
- Location: Digit-specific UBERON term (manual digit 2, 3, 4, or 5)
- Connecting branch of: UBERON:0006137 (proper palmar digital artery)
- Supplies: The same digit (as these branches supply soft tissue of that digit's dorsal aspect)

### Digit-Specific Details

**Second Digit (Index Finger - UBERON:0003622):**
- Rows 64, 68: Lateral and medial dorsal branches

**Third Digit (Middle Finger - UBERON:0003623):**
- Rows 65, 69: Lateral and medial dorsal branches

**Fourth Digit (Ring Finger - UBERON:0003624):**
- Rows 63, 67: Lateral and medial dorsal branches

**Fifth Digit (Little Finger - UBERON:0003625):**
- Rows 62, 66: Lateral and medial dorsal branches
- Note: The medial proper palmar digital artery of the fifth digit has special anatomy - it arises directly from the ulnar artery (UBERON:0001406) rather than from the common palmar digital artery

## Ontology Terms Used

| UBERON ID | Label | Usage |
|-----------|-------|-------|
| UBERON:0001637 | artery | Parent class for all entries |
| UBERON:0006137 | proper palmar digital artery | Connecting branch of for all entries |
| UBERON:0001406 | ulnar artery | Origin of medial proper palmar digital artery of 5th digit |
| UBERON:0001410 | common palmar digital artery | Origin of most proper palmar digital arteries |
| UBERON:0003622 | manual digit 2 | Index finger location |
| UBERON:0003623 | manual digit 3 | Middle finger location |
| UBERON:0003624 | manual digit 4 | Ring finger location |
| UBERON:0003625 | manual digit 5 | Little finger location |
| UBERON:0003533 | skin of finger | Supplied by cutaneous branch |
| UBERON:0006146 | dorsal digital artery of manus | Anastomoses with dorsal branches |

## Pattern Compliance

All entries follow the DOSDP pattern specified in `artery_and_arteriole_pattern.yaml`:

1. **defined_class:** To be generated
2. **label:** Provided from original template
3. **parent:** UBERON:0001637 (artery)
4. **location:** Digit-specific UBERON term
5. **connecting_branch_of:** UBERON:0006137 (proper palmar digital artery)
6. **vessel_supplies_blood_to:** Digit-specific or skin of finger
7. **definition:** Follows pattern: "An artery that branches from [parent] and supplies [tissues] of the [digit]"

## Data Quality Notes

1. **Consistency:** All entries follow consistent naming and ontology term usage
2. **Anatomical Accuracy:** Definitions reflect the anatomical course and function described in Wikipedia
3. **Laterality:** Proper distinction between lateral (radial side) and medial (ulnar side) branches
4. **Special Cases:** Correctly noted that the medial proper palmar digital artery of the 5th digit arises from ulnar artery
5. **Anastomoses:** Documented anastomotic connections with dorsal digital arteries

## References

1. **Primary Reference:** Wikipedia - Proper palmar digital arteries (https://en.wikipedia.org/wiki/Proper_palmar_digital_arteries)
2. **Wikidata:** Q6577825
3. **UBERON Ontology Terms:** Verified via OLS4 (Ontology Lookup Service)
4. **Cross-reference:** UBERON:0006137 definition confirms dorsal branch anatomy
5. **Cross-reference:** UBERON:0006146 (dorsal digital artery of manus) for anastomotic connections

## Output Files

1. **JSON Data:** `/Users/do12/Documents/GitHub/Uberon_vessel_template_agentic_edits/output/batch2_palmar_digital.json`
   - Contains structured data for all 9 entries
   - Includes metadata, justifications, and ontology term mappings

2. **This Report:** `/Users/do12/Documents/GitHub/Uberon_vessel_template_agentic_edits/output/batch2_palmar_digital_report.md`
   - Comprehensive documentation of processing decisions
   - Supporting evidence from references
   - Quality assurance documentation
