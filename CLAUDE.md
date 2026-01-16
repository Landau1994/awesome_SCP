# Awesome Single-Cell Proteomics

This is an Obsidian knowledge base and GitHub awesome-list for single-cell proteomics (SCP) research.

## Project Structure

```
awesome_SCP/
├── README.md                    # GitHub awesome-list
├── Home.md                      # Obsidian index/MOC
├── Project Overview.base        # Obsidian Bases dynamic view
├── canvas/                      # Obsidian canvas files
│   ├── SCP Overview.canvas
│   ├── Methods Workflow.canvas
│   └── Tools and Software.canvas
├── notes/
│   ├── methods/                 # Experimental methods
│   ├── tools/                   # Software & analysis tools
│   ├── databases/               # Data resources
│   └── applications/            # Research applications
└── templates/                   # Templater templates
    ├── Method Template.md
    ├── Tool Template.md
    ├── Database Template.md
    ├── Application Template.md
    ├── Literature Note.md
    └── Quick Note.md
```

## Content Guidelines

### Markdown Notes
- Use YAML frontmatter with: `title`, `aliases`, `tags`, `category`, `url`
- Use `[[wikilinks]]` for internal linking
- Use `> [!cite]` callouts for publications with DOI links
- Add Related Methods/Tools sections at the bottom

### Templates (Templater)
Configure Templater plugin to use `templates/` folder:
- **Method Template**: For new experimental methods
- **Tool Template**: For software and analysis tools
- **Database Template**: For data resources
- **Application Template**: For research applications
- **Literature Note**: For paper annotations
- **Quick Note**: For simple notes

### Canvas Files
- JSON format with `nodes` and `edges` arrays
- Node types: `text`, `file`, `link`, `group`
- Use color codes 1-6 for visual organization
- Connect related concepts with labeled edges

### Bases Files
- YAML format for dynamic note queries
- Use `Project Overview.base` for vault statistics

## Key Topics

- **Methods**: SCoPE2, plexDIA, nPOP, nanoPOTS, mPOP, pSCoPE
- **Tools**: MaxQuant, DIA-NN, scp (R), DO-MS, FragPipe
- **Databases**: SPDB, SingPro, scpdata
- **Applications**: Cancer, cell differentiation, immunology

## Resources

- Slavov Lab: https://scp.slavovlab.net/
- scp Bioconductor: https://bioconductor.org/packages/scp/
- SPDB: https://scproteomicsdb.com/

## Commands

When working with this project:
- Keep notes concise but comprehensive
- Maintain consistent formatting across notes
- Update canvas files when adding new notes
- Ensure cross-references are bidirectional
- Use templates for new notes
