---
title: ClusterProfiler
aliases: ["ClusterProfiler"]
tags:
  - tools
  - software
category: tool
url: https://bioconductor.org/packages/clusterProfiler/
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
library(clusterProfiler)
```

## Input/Output

**Input:**

- Gene identifiers, ranked gene statistics and an organism/annotation or user gene sets

**Output:**

- Enrichment or gene-set test results and comparison objects

## Key Publications

> [!cite] Primary Reference
> Yu et al. (2012). clusterProfiler: an R Package for Comparing Biological Themes Among Gene Clusters. *OMICS: A Journal of Integrative Biology*.
> DOI: [10.1089/omi.2011.0118](https://doi.org/10.1089/omi.2011.0118)

## Links

- GitHub: https://github.com/YuLab-SMU/clusterProfiler
- Documentation: https://yulab-smu.top/biomedical-knowledge-mining-book/

## Related Tools

- [[MaxQuant]]
- [[DIA-NN]]
- [[scp Package]]

## Source Check

- Source checked on 2026-10-20: [ClusterProfiler documentation or source](https://bioconductor.org/packages/clusterProfiler/).
