---
title: limma
aliases:
  - limma
tags:
  - tools
  - software
category: tool
url: https://bioconductor.org/packages/limma/
date_created: 2026-01-18
---

# limma

**A Bioconductor package for linear-model-based differential analysis in high-dimensional omics data.**

## Overview

limma is widely used for robust differential expression/abundance testing with empirical Bayes variance moderation.

## Key Features

- **Linear Modeling Framework**: Handles complex designs and contrasts.
- **Empirical Bayes Shrinkage**: Improves variance estimation stability.
- **Omics-Ready**: Applicable to transcriptomics and proteomics matrices.
- **Mature Ecosystem**: Standard component in reproducible R workflows.

## Installation

```bash
R -e "if (!requireNamespace('BiocManager', quietly=TRUE)) install.packages('BiocManager'); BiocManager::install('limma')"
```

## Usage

```r
# Example code
library(limma)
```

## Input/Output

**Input:**
- Raw files (.raw, .d, .mzML)
- Processed expression/abundance matrices with sample design metadata

**Output:**
- Protein/peptide matrices
- Quality metrics

## Key Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| design_matrix | user-defined | Experimental design specification |
| contrast_matrix | user-defined | Hypothesis testing contrasts |

## Key Publications

> [!cite] Primary Reference
> Ritchie et al. (2015) *Nucleic Acids Research*.

## Links

- Documentation: https://bioconductor.org/packages/limma/

## Related Tools

- [[MaxQuant]]
- [[DIA-NN]]
- [[scp Package]]
