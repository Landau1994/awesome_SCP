# Leading Scientists in Single-Cell Proteomics

> [!IMPORTANT]
> **Disclaimer:** This analysis is intended for **reference only**. The statistics and research group assignments are automatically generated based on the current selection of literature notes in this vault and may not reflect the full scope of the field or real-world academic hierarchies.

This note aggregates identifying leading scientists and key contributors based on the literature notes stored in `notes/literature/`.

## Dynamic Author Statistics (Dataview)

This table is generated dynamically using the Dataview plugin. It flattens the `authors` field from all notes in the literature folder, groups them by name, and counts associated literature notes. A preprint and its journal version may have separate notes, so these are not deduplicated publication counts.

```dataview
TABLE length(rows) as "Note Count", rows.file.link as "Notes"
FROM "notes/literature"
FLATTEN authors as author
GROUP BY author
SORT length(rows) DESC
LIMIT 50
```

## Dynamic Network Analysis

This section uses **DataviewJS** to analyze co-authorship networks in real-time. It filters for authors who appear in multiple papers and lists their most frequent collaborators, helping to identify research groups and core teams.

```dataviewjs
// --- Configuration ---
const minPapers = 2; // Minimum papers to appear in this list
const folder = "notes/literature";
// ---------------------

const pages = dv.pages(`"${folder}"`);
const authorStats = {};

// 1. Build the graph
for (const page of pages) {
    if (page.authors) {
        // Ensure authors is an array (handle single strings if necessary)
        const authors = Array.isArray(page.authors) ? page.authors : [page.authors];
        
        for (const author of authors) {
            if (!authorStats[author]) {
                authorStats[author] = { 
                    name: author, 
                    papers: [], 
                    coAuthors: {} 
                };
            }
            
            // Add paper link
            authorStats[author].papers.push(page.file.link);
            
            // Tally co-authors
            for (const coAuthor of authors) {
                if (author !== coAuthor) {
                    authorStats[author].coAuthors[coAuthor] = (authorStats[author].coAuthors[coAuthor] || 0) + 1;
                }
            }
        }
    }
}

// 2. Process and Sort Data
const sortedAuthors = Object.values(authorStats)
    .sort((a, b) => b.papers.length - a.papers.length)
    .filter(a => a.papers.length >= minPapers);

// 3. Render Table
if (sortedAuthors.length === 0) {
    dv.paragraph(`*No authors found with ${minPapers} or more papers yet.*`);
} else {
    const tableData = sortedAuthors.map(a => {
        // Get top 5 co-authors sorted by frequency
        const topCoAuthors = Object.entries(a.coAuthors)
            .sort(([, countA], [, countB]) => countB - countA)
            .slice(0, 5)
            .map(([name, count]) => `${name} (${count})`)
            .join(", ");
            
        return [
            `**${a.name}**`, 
            a.papers.length, 
            topCoAuthors || "*No Co-Authors*",
            a.papers.join(", ")
        ];
    });

    dv.table(
        ["Author", "Note Count", "Frequent Collaborators (Shared Notes)", "Associated Notes"],
        tableData
    );
}
```


## Research Groups & Key Figures (Snapshot)

The examples below describe authorship in selected publications, checked 2026-10-20. They are not an exhaustive ranking, a statement of current employment, or a claim that one group exclusively developed a technology.

| Publication context | Selected authors | Source |
|---------------------|------------------|--------|
| Chip-Tip and high-sensitivity workflows | Zilu Ye, Jesper V. Olsen and collaborators | Linked [[Chip-Tip]] method and original article |
| AlphaPeptDeep | Wen-Feng Zeng, Xie-Xuan Zhou, Sander Willems, Constantin Ammar, Maria Wahle, Isabell Bludau, Eugenia Voytik, Maximillian T. Strauss and Matthias Mann | [Nature Communications (2022)](https://doi.org/10.1038/s41467-022-34904-3) |
| Glioblastoma neutrophil states | Pranvera Sadiku, Karl Mechtler, Sarah R. Walmsley and collaborators | [Nature Communications](https://doi.org/10.1038/s41467-025-67367-3), online 2025 / volume 2026 |
| Cellular differentiation hierarchies | Erwin M. Schoof, Bo T. Porse and collaborators | [Nature Communications (2021)](https://doi.org/10.1038/s41467-021-23667-y) |

## Methodology
- **Data Source**: `notes/literature/`
- **Field**: `authors` (YAML frontmatter)
- **Tool**: Obsidian Dataview Plugin

## Sources

- [AlphaPeptDeep author list](https://doi.org/10.1038/s41467-022-34904-3)
- [Neutrophil study author list](https://doi.org/10.1038/s41467-025-67367-3)
- [Cellular hierarchies author list](https://doi.org/10.1038/s41467-021-23667-y)
