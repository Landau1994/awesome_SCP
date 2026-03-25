---
title: ClusterProfiler
aliases:
  - ClusterProfiler
  - clusterProfiler
tags:
  - tools
  - software
category: tool
url: 
date_created: 2026-01-18
---

# ClusterProfiler

**An R/Bioconductor package for enrichment analysis and biological theme comparison.**

## Overview

ClusterProfiler supports GO/KEGG enrichment, GSEA-style analyses, and comparative interpretation across gene/protein sets.

## Key Features

- **Enrichment Analysis**: Over-representation and rank-based methods.
- **Multi-Database Support**: GO, KEGG and custom gene sets.
- **Visualization Ecosystem**: Integrates with enrichplot and related tools.
- **Reproducible R Workflow**: Scriptable and publication-friendly.

## Installation

```bash
R -e "if (!requireNamespace('BiocManager', quietly=TRUE)) install.packages('BiocManager'); BiocManager::install('clusterProfiler')"
```

## Usage

```r
# Example code
library(ClusterProfiler)
```

## Input/Output

**Input:**
- Raw files (.raw, .d, .mzML)
- Gene/protein lists and ranking statistics

**Output:**
- Protein/peptide matrices
- Quality metrics

## Key Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| pvalueCutoff | 0.05 | Significance threshold |
| pAdjustMethod | BH | Multiple-testing correction |

## Key Publications

> [!cite] Primary Reference
> Yu et al. (2012) *OMICS*.

## Links

- GitHub: https://github.com/YuLab-SMU/clusterProfiler
- Documentation: https://yulab-smu.top/biomedical-knowledge-mining-book/

## Related Tools

- [[MaxQuant]]
- [[DIA-NN]]
- [[scp Package]]
