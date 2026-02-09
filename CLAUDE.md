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

This project contains a DOSDP template for generating UBERON terms for vessels and arteries and the dosdp YAML file specifying the pattern used to convert terms from the template into OWL.  Some entries have missing content.

Each entry with missing content includes one or more references. Use the appropriate tool:
 - Wikipedia URLs: Use the 'fetch-wiki-info' skill
 - Academic papers (DOIs, PMIDs): Use 'artl-mcp'
 - Complex web pages: Use playwright MCP

Use the refs to retrieve information to populate the missing content, based on patterns earlier in the table and the associated DOSDP pattern.

For ontology terms, use the **ontology-term-lookup subagent** with the text description of the anatomical structure you need to find.

As well as editing the table, generate a report justifying the edits with supporting text from the references.
