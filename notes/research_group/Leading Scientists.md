# Leading Scientists in Single-Cell Proteomics

> [!IMPORTANT]
> **Disclaimer:** This analysis is intended for **reference only**. The statistics and research group assignments are automatically generated based on the current selection of literature notes in this vault and may not reflect the full scope of the field or real-world academic hierarchies.

This note aggregates identifying leading scientists and key contributors based on the literature notes stored in `notes/literature/`.

## Dynamic Author Statistics (Dataview)

This table is generated dynamically using the Dataview plugin. It flattens the `authors` field from all notes in the literature folder, groups them by name, and counts the number of papers associated with each.

```dataview
TABLE length(rows) as "Paper Count", rows.file.link as "Papers"
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
        ["Author", "Count", "Frequent Collaborators (Shared Papers)", "Associated Papers"],
        tableData
    );
}
```


## Research Groups & Key Figures (Snapshot)

While the table above updates dynamically, this section provides context on the major research clusters identified in the current literature (as of Jan 2026, **the list i no particular order**,**The statistics and research group assignments are automatically generated based on the current selection of literature notes in this vault and may not reflect the full scope of the field or real-world academic hierarchies**.):


### 🇨‍🇳  Suzhou Institute of Systems6Medicine, Chinese Academy of Medical Sciences & Peking Union Medical College, Suzhou, China
+ **Key Figures:** Zilu Ye
+ Focus:High-sensitivity hardware workflows. They are the primary drivers behind the **Orbitrap Astral** methods, **SC-pSILAC** (turnover), and the **Chip-Tip** workflow

### 🇩🇰 Center for Protein Research (Copenhagen)
* **Key Figures:** Pierre Sabatier, Maico Lechner, Jesper V. Olsen, Zilu Ye.
* **Focus:** High-sensitivity hardware workflows. They are the primary drivers behind the **Orbitrap Astral** methods, **SC-pSILAC** (turnover), and the **Chip-Tip** workflow.


### 🇩🇪 Max Planck Institute (Biochemistry)
* **Key Figures:** Matthias Mann.
* **Focus:** Integration of Deep Learning in proteomics. Associated with **AlphaPeptDeep** and AI-driven peptide property prediction.

### 🇬🇧/🇦🇹 Glioblastoma & Neutrophil Group
* **Key Figures:** Sarah R. Walmsley, Karl Mechtler.
* **Focus:** Applied clinical proteomics. Specifically mapping functional states of tumor-associated neutrophils (TANs) in Glioblastoma.

### 🇩🇰 Hematopoietic Stem Cell Group
* **Key Figures:** Bo T. Porse, Erwin M. Schoof.
* **Focus:** Biological application of single-cell proteomics (**scp-MS**) to map differentiation hierarchies and translation dynamics (**scProtVelo**).

---

## Methodology
- **Data Source**: `notes/literature/`
- **Field**: `authors` (YAML frontmatter)
- **Tool**: Obsidian Dataview Plugin
