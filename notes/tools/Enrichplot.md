---
title: Enrichplot
aliases:
  - Enrichplot
tags:
  - tools
  - software
category: tool
url: https://bioconductor.org/packages/enrichplot/
date_created: 2026-01-18
---

# Enrichplot

**An R visualization package for enrichment analysis results from clusterProfiler-like workflows.**

## Overview

Enrichplot provides publication-ready plots for pathway and ontology enrichment outputs, including dot plots, cnetplots, and enrichment maps.

## Key Features

- **Enrichment Visualization**: Dot plots, ridge plots, cnetplots, and more.
- **Ontology/Pathway Support**: Works with GO/KEGG enrichment outputs.
- **Interpretability**: Helps summarize complex enrichment signatures.
- **R Ecosystem Fit**: Integrates naturally with clusterProfiler outputs.

## Installation

```bash
R -e "if (!requireNamespace('BiocManager', quietly=TRUE)) install.packages('BiocManager'); BiocManager::install('enrichplot')"
```

## Usage

```r
# Example code
library(enrichplot)
```

## Input/Output

**Input:**

- Supported enrichment/GSEA result objects (for example from clusterProfiler)

**Output:**

- Visualizations of enrichment results

## Key Publications

> [!cite] Primary Reference
> Yu et al. enrichplot package documentation.

## Links

- Documentation: https://bioconductor.org/packages/enrichplot/

## Related Tools

- [[MaxQuant]]
- [[DIA-NN]]
- [[scp Package]]

## Source Check

- Source checked on 2026-10-20: [Enrichplot documentation or source](https://bioconductor.org/packages/enrichplot/).
