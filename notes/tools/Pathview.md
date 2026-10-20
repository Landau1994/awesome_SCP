---
title: Pathview
aliases:
  - Pathview
tags:
  - tools
  - software
category: tool
url: https://bioconductor.org/packages/pathview/
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
library(pathview)
```

## Input/Output

**Input:**

- Gene or compound measurements and pathway/organism identifiers

**Output:**

- Pathway diagrams with mapped data

## Key Publications

> [!cite] Primary Reference
> Luo et al. (2013). Pathview: an R/Bioconductor package for pathway-based data integration and visualization. *Bioinformatics*.
> DOI: [10.1093/bioinformatics/btt285](https://doi.org/10.1093/bioinformatics/btt285)

## Links

- Documentation: https://bioconductor.org/packages/pathview/

## Related Tools

- [[MaxQuant]]
- [[DIA-NN]]
- [[scp Package]]

## Source Check

- Source checked on 2026-10-20: [Pathview documentation or source](https://bioconductor.org/packages/pathview/).
