# UBERON Vessel Template - Agentic Edits

This repository contains a Dead Simple OWL Design Pattern (DOSDP) template for generating UBERON ontology terms for arterial blood vessels. The project is designed to work with AI assistants (Claude-Code or Codex) to semi-automatically populate incomplete template entries using scientific literature and ontology references.

## Overview

The repository includes:
- **DOSDP template** (`source/artery_and_arteriole_pattern.yaml`) - Pattern specification for vessel terms
- **TSV data file** (`source/artery_and_arteriole_pattern.tsv`) - Template entries with some incomplete content
- **Python helper script** (`scripts/process_vessels.py`) - Workflow management utilities
- **MCP server integration** - For literature search, ontology lookup, and web research

## Design Philosophy

This project is optimized for **agentic workflows** using:
- **Claude-Code** (primary, most tested)
- **Codex** (compatible)

The AI assistant uses multiple MCP (Model Context Protocol) servers to:
- Look up ontology terms (UBERON, FMA) by textual descriptions
- Retrieve scientific literature (abstracts, full text, PDFs)
- Fetch Wikipedia and Wikidata references
- Navigate complex web pages

## Prerequisites

- **Python 3.11 or higher**
- **uv** (Python package installer) - Install via: `pip install uv` or `curl -LsSf https://astral.sh/uv/install.sh | sh`
- **Claude-Code** or **Codex** (for agentic editing)
- **Node.js** (for Playwright MCP server, if using web automation)

## Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Uberon_vessel_template_agentic_edits
```

### 2. Set Up Python Virtual Environment

Create and activate a Python virtual environment:

```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate
```

### 3. Install Python Dependencies

Since this project uses `uv` for package management, install dependencies as needed:

```bash
# Install uv if not already installed
pip install uv

# The helper script uses only standard library modules
# Additional dependencies can be installed via uv as needed:
# uv pip install <package-name>
```

### 4. Configure MCP Servers

The `.mcp.json` file configures MCP servers for:
- **OLS4** - Ontology Lookup Service for term searches
- **artl-mcp** - Academic literature retrieval (Europe PMC)
- **Playwright** - Web automation for complex pages

These are automatically configured when using Claude-Code.

## Project Structure

```
.
├── source/                                 # Source data and specifications
│   ├── artery_and_arteriole_pattern.yaml  # DOSDP pattern specification
│   └── artery_and_arteriole_pattern.tsv   # Template data (main file)
├── scripts/                                # Python helper scripts
│   └── process_vessels.py                 # Workflow management utilities
├── output/                                 # Generated output files
│   ├── artery_and_arteriole_pattern_updated.tsv  # Updated version
│   ├── justification_report_rows_61-65.md # Justification reports
│   └── progress.json                      # Progress tracking (generated)
├── CLAUDE.md                               # Instructions for Claude-Code
├── planning.md                             # Project planning notes
├── .mcp.json                               # MCP server configuration
├── .gitignore                              # Git ignore rules
├── LICENSE                                 # MIT License
└── README.md                               # This file
```

## Usage

### Working with Claude-Code

1. **Open the project in Claude-Code:**
   ```bash
   claude-code
   ```

2. **The AI assistant will:**
   - Read incomplete entries from the TSV file
   - Use MCP servers to look up references (papers, Wikipedia, ontologies)
   - Populate missing fields (definitions, synonyms, xrefs)
   - Generate justification reports citing sources

3. **Example workflow:**
   ```
   User: "Complete the entries for rows 61-65"

   Claude will:
   - Identify incomplete entries
   - Fetch references using appropriate MCP tools
   - Find ontology terms using ontology-term-lookup agent
   - Fill in missing content following DOSDP patterns
   - Generate justification report with citations
   ```

### Using the Helper Script

Run the helper script to analyze incomplete entries:

```bash
# From the project root directory
python scripts/process_vessels.py
```

This will:
- Load the TSV file from `source/`
- Identify entries with missing definitions
- Display statistics and incomplete entries
- Save outputs to `output/` directory

## DOSDP Pattern

The template follows this pattern for arterial blood vessels:

- **Pattern name:** `artery_and_arteriole_pattern`
- **Description:** Arterial blood vessels that supply blood to a tissue and branch from other arterial vessels

**Key fields:**
- `label` - Vessel name
- `definition` - Formal definition with references
- `parent` - Parent arterial blood vessel class
- `connecting_branch_of` - Blood vessel this branches from
- `vessel_supplies_blood_to` - Anatomical structure(s) supplied
- `location` - Anatomical location
- `synonym` - Alternative names
- `xrefs` - External references (FMA, Wikipedia, etc.)

## MCP Servers Used

### 1. OLS4 (Ontology Lookup Service)
- Search ontology terms by label/description
- Get term ancestors and descendants
- Retrieve term metadata

### 2. artl-mcp (Literature Retrieval)
- Search Europe PMC by keywords
- Get paper metadata by DOI/PMID/PMCID
- Retrieve full text and convert PDFs to Markdown
- Translate between identifier types

### 3. Playwright (Web Automation)
- Navigate complex web pages
- Take screenshots and snapshots
- Handle dynamic content

### 4. fetch-wiki-info (Wikipedia/Wikidata)
- Retrieve structured data from Wikidata
- Fetch Wikipedia content and references

## Tips for Working with AI Assistants

1. **Be specific about rows:** "Complete entries for rows 61-65"
2. **Request justifications:** "Generate a report justifying the edits"
3. **Verify ontology terms:** The AI will use the ontology-term-lookup agent to find correct UBERON/FMA terms
4. **Check references:** All edits should be backed by cited sources

## Contributing

When making edits:
1. Ensure all definitions include proper references (xrefs)
2. Follow the existing pattern for similar entries
3. Generate justification reports for transparency
4. Verify ontology term IRIs are correct

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## References

- [DOSDP Documentation](https://github.com/INCATools/dead_simple_owl_design_patterns)
- [UBERON Ontology](http://uberon.github.io/)
- [OBO Foundry](http://www.obofoundry.org/)
