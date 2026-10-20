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

- Processed expression or abundance matrix and an experimental design/contrasts

**Output:**

- Model coefficients, differential-analysis statistics and adjusted P values

## Key Publications

> [!cite] Primary Reference
> Ritchie et al. (2015). limma powers differential expression analyses for RNA-sequencing and microarray studies. *Nucleic Acids Research*.
> DOI: [10.1093/nar/gkv007](https://doi.org/10.1093/nar/gkv007)

## Links

- Documentation: https://bioconductor.org/packages/limma/

## Related Tools

- [[MaxQuant]]
- [[DIA-NN]]
- [[scp Package]]

## Source Check

- Source checked on 2026-10-20: [limma documentation or source](https://bioconductor.org/packages/limma/).
