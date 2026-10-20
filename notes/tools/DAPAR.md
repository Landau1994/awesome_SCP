---
title: DAPAR
aliases:
  - DAPAR
tags:
  - tools
  - software
category: tool
url: https://bioconductor.org/packages/DAPAR/
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

- Quantified peptide/protein abundance tables and sample metadata

**Output:**

- Processed quantitative data, diagnostic plots and statistical results

## Key Publications

> [!cite] Primary Reference
> Wieczorek et al. DAPAR package documentation and methodology.

## Links

- Source availability: See the official source below; no separate public repository was confirmed.
- Documentation: https://bioconductor.org/packages/DAPAR/

## Related Tools

- [[MaxQuant]]
- [[DIA-NN]]
- [[scp Package]]

## Source Check

- Source checked on 2026-10-20: [DAPAR documentation or source](https://bioconductor.org/packages/DAPAR/).
