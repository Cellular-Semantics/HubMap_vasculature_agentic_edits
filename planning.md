# UBERON Vessel Template Completion - Planning Document

## Project Overview
This project involves completing a DOSDP (Dead Simple OWL Design Pattern) template for generating UBERON ontology terms for arterial blood vessels and arterioles.

## Files Involved
- **artery_and_arteriole_pattern.yaml**: DOSDP pattern specification defining the template structure
- **artery_and_arteriole_pattern.tsv**: Data table with 164 rows (104 incomplete entries)

## DOSDP Pattern Structure

### Pattern Purpose
Generates terms for arterial blood vessels that supply blood to tissues and branch from other arterial blood vessels.

### Required Variables (Must be filled for each entry)
- **defined_class**: UBERON ID for the new term
- **label**: Name of the vessel (xsd:string)
- **parent**: Parent arterial blood vessel class (default: UBERON:0001637 = arterial blood vessel)
- **location**: Anatomical entity where vessel is located (UBERON term)
- **connecting_branch_of**: Blood vessel this branches from (UBERON term)
- **definition**: Text definition (xsd:string)
- **creator**: ORCID identifier
- **date_created**: Timestamp (ISO 8601 format)

### Optional Variables
- **vessel_supplies_blood_to**: Anatomical structures supplied (pipe-separated list of UBERON terms)
- **synonym**: Alternative names (pipe-separated list)
- **synonym_xrefs**: Cross-references for synonyms (pipe-separated)
- **FMA_xref**: Foundational Model of Anatomy cross-reference
- **xrefs**: Cross-references for definition (pipe-separated)

### Logical Axioms Generated
Each term will be defined as:
1. `subClassOf: [parent arterial blood vessel]`
2. `subClassOf: 'part of' some [location]`
3. `subClassOf: 'connecting branch of' some [connecting_branch_of]`
4. `subClassOf: 'vessel supplies blood to' some [vessel_supplies_blood_to]` (if present)

## Current Status

### Complete Entries: Rows 2-60 (59 entries)
All fields populated, following consistent patterns.

### Incomplete Entries: Rows 61-164 (104 entries)
Only have:
- **label**: Name of the artery/arteriole
- **xrefs**: Reference URLs (Wikipedia, DOIs, PMIDs, web pages)

Missing:
- FMA_xref (if available)
- parent (usually UBERON:0001637)
- location
- definition
- synonym (if available)
- synonym_xrefs (if applicable)
- connecting_branch_of
- vessel_supplies_blood_to
- creator
- date_created

## Task Breakdown

### For Each Incomplete Entry (rows 61-164):

1. **Retrieve Reference Content**
   - For DOIs/PMIDs: Use `artl-mcp` tools (get_full_text_from_doi, get_abstract_from_pubmed_id, etc.)
   - For Wikipedia URLs: Use `fetch-wiki-info` skill
   - For complex web pages: Use playwright MCP
   - Extract anatomical information about the vessel

2. **Find Ontology Terms**
   - Use **ontology-term-lookup subagent** to find UBERON terms for:
     - Anatomical structures (location)
     - Blood vessels (connecting_branch_of)
     - Tissues/organs supplied (vessel_supplies_blood_to)
   - Use **ontology-term-lookup subagent** to search for FMA terms matching the vessel name
   - Pass the textual description/label of the structure to the subagent

3. **Extract Information from References**
   - **connecting_branch_of**: Which vessel does it branch from?
   - **location**: Where is it anatomically located?
   - **vessel_supplies_blood_to**: What structures does it supply?
   - **definition**: Comprehensive definition following pattern from completed entries
   - **synonym**: Alternative names for the vessel
   - **FMA_xref**: FMA identifier (if found)

4. **Populate Fields Following Patterns**
   - **parent**: Usually UBERON:0001637 (arterial blood vessel) or UBERON:0001980 (arteriole)
   - **creator**: Use https://orcid.org/0000-0001-6757-4744 (from recent entries)
   - **date_created**: Current timestamp in ISO 8601 format (e.g., 2025-06-16T09:40:19Z)
   - **xrefs**: Keep existing references, may add more if needed
   - **synonym_xrefs**: Use FMA_xref or source references

5. **Generate Justification Report**
   - Document each edit with supporting evidence from references
   - Include direct quotes from sources supporting the definitions
   - Note any uncertainties or assumptions

## Examples from Completed Entries

### Example 1: atrioventricular nodal artery (row 2)
- **parent**: UBERON:0001637 (arterial blood vessel)
- **location**: UBERON:0000948 (heart)
- **connecting_branch_of**: UBERON:0001625 (right coronary artery)
- **vessel_supplies_blood_to**: UBERON:0002352 (atrioventricular node)
- **definition**: "An artery that branches from the right coronary artery and supplies the atrioventricular node."

### Example 2: pulmonary arteriole (row 7)
- **parent**: UBERON:0010369 (arteriole) [Note: arterioles have different parent]
- **location**: UBERON:0010369 (arteriole)
- **connecting_branch_of**: UBERON:8600060 (subsegmental pulmonary artery)
- **vessel_supplies_blood_to**: UBERON:0016405 (pulmonary capillaries) | UBERON:0002299 (alveolar capillaries)
- **synonym**: "set of all pulmonary arterioles"

## Definition Pattern
Standard format: "An artery [or arteriole] that branches from the [parent vessel] and supplies [structures supplied]."

Additional anatomical details can be included for precision.

## Important Notes

1. **Parent assignment**:
   - Arteries: UBERON:0001637 (arterial blood vessel)
   - Arterioles: UBERON:0010369 (arteriole) or UBERON:0001980 (systemic arteriole)

2. **Multiple values**: Use pipe separator (|) for:
   - vessel_supplies_blood_to
   - synonym
   - xrefs
   - synonym_xrefs

3. **FMA_xref**:
   - Search using ontology-term-lookup subagent for FMA matches
   - Leave blank if no match found
   - Format: FMA:##### (numeric only, no "FMA:" prefix sometimes)

4. **Reference types**:
   - Wikipedia URLs: Use fetch-wiki-info skill
   - DOI: Use artl-mcp tools (doi: prefix or full URL)
   - PMID: Use artl-mcp tools (PMID: prefix)
   - Complex web pages: Use playwright MCP

## Tools Available

### ontology-term-lookup subagent
- Find ontology terms by textual labels or descriptions
- Searches UBERON and FMA ontologies via OLS4
- Automatically handles search variations and synonyms

### artl-mcp
- `get_doi_metadata`: Get metadata for papers
- `get_full_text_from_doi`: Get full text (requires email)
- `get_abstract_from_pubmed_id`: Get abstracts
- `extract_pdf_text`: Extract text from PDF URLs
- `search_keywords_for_ids`: Find papers by keywords
- And many more...

### fetch-wiki-info skill
- Fetch structured information from Wikipedia and Wikidata
- Use for all Wikipedia references

### playwright MCP
- Browser automation for complex web pages
- Use when standard fetching methods fail

## Python Helper Script: process_vessels.py

A Python helper script has been created to assist with workflow management:

### Key Features:
- **VesselProcessor class**: Manages TSV file loading and processing
- **get_incomplete_entries()**: Identifies entries missing definitions (rows 61-164)
- **Progress tracking**: Saves progress to JSON file (progress.json)
- **Justification tracking**: Stores justifications keyed by vessel label
- **save_justifications()**: Generates markdown report (justification_report.md)
- **save_updated_tsv()**: Saves completed TSV to new file

### Usage:
```python
from process_vessels import VesselProcessor

processor = VesselProcessor('artery_and_arteriole_pattern.tsv')
incomplete = processor.get_incomplete_entries()

# Process entries, then:
processor.entries[idx]['definition'] = "..."
processor.justifications[label] = "Supporting evidence..."

processor.save_progress()
processor.save_justifications()
processor.save_updated_tsv()
```

### Python Environment:
- Virtual environment: `.venv`
- Use `uv` to install dependencies if needed

## Workflow Summary

1. Create todo list for tracking progress (use TodoWrite)
2. Process entries in batches (e.g., 10 at a time)
3. For each entry:
   - Fetch reference content (artl-mcp for papers, fetch-wiki-info skill for Wikipedia, playwright MCP for complex sites)
   - Extract anatomical information
   - Use ontology-term-lookup subagent to find UBERON and FMA terms
   - Populate all fields
   - Validate against pattern
4. Generate comprehensive justification report
5. Save updated TSV file using process_vessels.py

## Next Steps After MCP Configuration

1. Verify both artl-mcp and ols4-mcp are accessible
2. Test MCP tools with a sample entry
3. Begin systematic processing of incomplete entries (rows 61-164)
4. Generate justification report as work progresses
