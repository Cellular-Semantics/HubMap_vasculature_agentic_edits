# DOSDP template editor

You are an expert in OWL and OBO ontology building, with a focus on generating Dead Simple OWL Design Pattern (DOSDP) templates.

DOSDP documentaion can be found here:
 - https://github.com/INCATools/dead_simple_owl_design_patterns/blob/master/src/schema/dosdp_schema.yaml # YAML format JSON schema.

You have available a python venv (.venv). Use this to run any Python scripts you may need. Use UV to install dependencies.

You also have available:
 - **ontology-term-lookup subagent**: For finding ontology terms (UBERON, FMA) by textual labels or descriptions
 - **artl-mcp**: For retrieving scientific literature (abstracts, full text, PDFs, metadata) using DOIs, PMIDs, or keywords
 - **fetch-wiki-info skill**: For Wikipedia and Wikidata references
 - **playwright MCP**: For complex web pages where standard fetching fails

This project contains a DOSDP template for generating UBERON terms for vessels and arteries and the dosdp YAML file specifying the pattern used to convert terms from the template into OWL.  Some entries have missing content. Your job is to complete missing content where references support that content.

Each entry with missing content includes one or more references. Use the appropriate tool:
 - Wikipedia URLs: Use the 'fetch-wiki-info' skill
 - Academic papers (DOIs, PMIDs): Use 'artl-mcp'
 - Complex web pages: Use playwright MCP

Use the refs to retrieve information to populate the missing content, based on patterns earlier in the table and the associated DOSDP pattern.

For the parent class ONLY USE either artery (UBERON:0001637) or areriole (UBERON:0001980) as appropriate to the term name & references.

For all other ontology terms, use the **ontology-term-lookup subagent** with the name of the anatomical structure you need to find.

As well as editing the table, generate an separate reporting table with the additional label columns adjacent to each ontology ID column.  Also generate a report justifying the edits with supporting text from the references.

---

## Workflow for Populating Template Entries

### Overview
The project uses a parallel agent-based workflow to systematically populate missing template entries. This approach scales to handle 100+ entries efficiently.

### Scripts Directory Structure
```
scripts/
├── process_template.py              # 1. Analyze template, identify incomplete rows
├── populate_template_entries.py     # 2. Extract anatomical patterns from labels
├── consolidate_results.py           # 3. Merge all batch results into final output
└── agent_generated/                 # Optional: Agent-created processing scripts
    └── batch6_spleen_processing.py  # Example: Domain-specific data generation
```

### Workflow Steps

#### 1. Analysis Phase
```bash
python scripts/process_template.py
```
- Identifies incomplete rows (missing parent, location, definition, etc.)
- Groups by reference type (Wikipedia, DOI, PMID, etc.)
- Output: `output/incomplete_rows.json`

#### 2. Parallel Processing Phase
Spawn multiple background agents to process batches in parallel:
- **Batch size**: 4-15 entries per agent
- **Grouping**: By anatomical domain or reference type
- **Agents use**: ontology-term-lookup, artl-mcp, playwright, WebFetch
- **Output**: `output/batch*.json` files

Example agent task structure:
```python
Task(subagent_type="general-purpose",
     description="Process hepatic arteries",
     prompt="Process entries for hepatic artery branches...",
     run_in_background=True)
```

#### 3. Consolidation Phase
```bash
python scripts/consolidate_results.py
```
- Loads all `batch*.json` files (handles multiple JSON formats)
- Merges results into template
- Generates three outputs:
  - `artery_and_arteriole_pattern_updated.tsv` - Updated template
  - `reporting_table.tsv` - With ontology labels for review
  - `justification_report.md` - Supporting evidence from references

### Current Progress (as of last run)
- **Completed**: 21/104 entries populated across 9 batch files
- **Remaining**: 83 entries (agents hit API rate limits)
- **Batch coverage**:
  - Batch 1: Wikipedia references (5 entries)
  - Batch 2: Palmar digital arteries (9 entries)
  - Batch 3: Hepatic arteries (7 entries)
  - Batch 4: Cerebral arteries (8 entries)
  - Batch 6: Spleen arteries (4 entries)
  - Batch 7: Pancreatic arteries (5 entries)
  - Batch 8: Pharyngeal arteries (5 entries)
  - Batch 9: Dorsal hand arteries (9 entries)
  - Others: Various anatomical domains

### To Complete Remaining Entries
Resume or spawn new agents for unprocessed batches:
1. Check `output/incomplete_rows.json` for remaining entries
2. Identify which anatomical domains need processing
3. Spawn new background agents with appropriate batches
4. Run consolidation script after agents complete
5. Review and validate populated entries

### Ontology Term Lookup Strategy
When using the ontology-term-lookup agent:
- Provide clear anatomical descriptions (e.g., "hepatic artery", "fifth digit of hand")
- Search in UBERON first, then FMA if needed
- Common parent: UBERON:0001637 (artery) for most entries
- Location depends on body region (head, thorax, abdomen, limbs)
- Supplied tissues: specific organs or structures

### Quality Assurance
- Cross-reference with completed rows for pattern consistency
- Verify definitions follow DOSDP format: "An artery that branches from [parent] and supplies [tissue]"
- Check ontology IDs exist in UBERON/FMA
- Ensure justifications cite specific text from references

---

## FINAL TASK: Image Enrichment (Run ONLY After All Template Blanks Are Filled)

**CRITICAL**: This task must ONLY be executed after all missing content in the template has been populated. Do NOT modify the template structure or add new columns until all current work is complete.

### Task Overview
Once all template entries are complete, extend the template with image metadata from Wikipedia to enrich UBERON terms with visual representations.

### New Columns to Add
Add the following columns to the template:
1. **`AI FOAF:depiction`** - Full IRI/URL to the Wikipedia Commons SVG or image file
2. **`>A has_license`** - License information (e.g., "Public Domain", "CC-BY-SA 4.0")
3. **`rdfs:comment`** - Legend/caption text describing the image
4. *Additional column(s) as needed for image metadata*

### Image Retrieval Process
For each template entry that has a Wikipedia reference:

1. **Use Playwright MCP** to navigate to the Wikipedia page
2. **Extract images** from the page using browser automation
3. **Navigate to image detail pages** on Wikimedia Commons to get:
   - Full resolution image URL (prefer SVG format)
   - License information
   - Image description/caption
4. **Prefer Public Domain images** - These can be freely used in ontologies
5. **Prefer SVG format** - Vector images scale better than raster formats

### Tool Selection for Images
- **playwright MCP**: Primary tool for Wikipedia image extraction
- Navigate to Wikipedia article → Extract images → Visit Commons page → Get metadata
- See successful test case: "cutaneous branch of medial proper palmar digital artery of fifth digit of hand"

### Example Image Metadata
From test case (Gray1237.svg):
- **FOAF:depiction**: `https://upload.wikimedia.org/wikipedia/commons/a/a9/Gray1237.svg`
- **has_license**: `Public Domain`
- **rdfs:comment**: `Palm of left hand, showing position of skin creases and bones, and surface markings for the volar arches. Only the proximal origin parts of the proper palmar digital arteries are shown.`

### Important Notes
- This task modifies the template structure - coordinate with any existing scripts/schemas
- Not all entries may have suitable images - that's acceptable
- When multiple images are available, prioritize:
  1. Public Domain or open licenses
  2. SVG (vector) over raster formats
  3. Anatomical diagrams over photographs
  4. Images that clearly show the specific anatomical structure

### Execution Order
1. ✓ Complete all missing template content (current task)
2. ✓ Generate reporting tables with ontology labels
3. ✓ Generate justification reports
4. → THEN add image enrichment columns (this task)
5. → Populate image metadata for entries with Wikipedia refs
6. → Generate final report documenting added images
