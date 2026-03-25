---
title: Pathview
aliases:
  - Pathview
tags:
  - tools
  - software
category: tool
url: 
date_created: 2026-01-18
---

# Pathview

**An R package for pathway-based data integration and visualization on KEGG maps.**

## Overview

Pathview maps omics statistics or abundances onto biological pathways, enabling interpretable functional visualization.

## Key Features

- **Pathway Mapping**: Projects quantitative data onto KEGG pathways.
- **Integrated Visualization**: Combines statistics and network context.
- **Omics Flexibility**: Supports transcriptomics/proteomics style inputs.
- **R Workflow Integration**: Works with enrichment and differential pipelines.

## Installation

```bash
R -e "if (!requireNamespace('BiocManager', quietly=TRUE)) install.packages('BiocManager'); BiocManager::install('pathview')"
```

## Usage

```r
# Example code
library(Pathview)
```

## Input/Output

**Input:**
- Raw files (.raw, .d, .mzML)
- Differential expression/abundance tables

**Output:**
- Protein/peptide matrices
- Quality metrics

## Key Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| pathway_id | KEGG ID | Target pathway map |
| species | organism code | Organism selection for mapping |

## Key Publications

> [!cite] Primary Reference
> Luo and Brouwer (2013) *Bioinformatics*.

## Links

- Documentation: https://bioconductor.org/packages/pathview/

## Related Tools

- [[MaxQuant]]
- [[DIA-NN]]
- [[scp Package]]
