---
title: DAPAR
aliases:
  - DAPAR
tags:
  - tools
  - software
category: tool
url: 
date_created: 2026-01-18
---

# DAPAR

**An R package for preprocessing, normalization, and differential analysis of proteomics data.**

## Overview

DAPAR provides a workflow for quantitative proteomics matrix processing including filtering, normalization, imputation, and statistical testing.

## Key Features

- **Data Preprocessing**: Filtering and quality control utilities.
- **Normalization/Imputation**: Supports proteomics-specific handling strategies.
- **Differential Analysis**: Integrates statistical comparison modules.
- **R Ecosystem Integration**: Works with broader Bioconductor workflows.

## Installation

```bash
R -e "if (!requireNamespace('BiocManager', quietly=TRUE)) install.packages('BiocManager'); BiocManager::install('DAPAR')"
```

## Usage

```r
# Example code
library(DAPAR)
```

## Input/Output

**Input:**
- Raw files (.raw, .d, .mzML)
- Protein/peptide abundance tables

**Output:**
- Protein/peptide matrices
- Quality metrics

## Key Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| normalization_method | workflow-dependent | Intensity normalization strategy |
| imputation_method | workflow-dependent | Missing-value handling |

## Key Publications

> [!cite] Primary Reference
> Wieczorek et al. DAPAR package documentation and methodology.

## Links

- GitHub:
- Documentation: https://bioconductor.org/packages/DAPAR/

## Related Tools

- [[MaxQuant]]
- [[DIA-NN]]
- [[scp Package]]
