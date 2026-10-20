---
title: scp Package
aliases:
  - scp R package
  - Bioconductor scp
tags:
  - tools
  - R
  - Bioconductor
  - analysis
  - workflow
category: tool
url: https://bioconductor.org/packages/scp/
---

# scp Package

**Bioconductor Package for Single-Cell Proteomics**

## Overview

The `scp` package provides a standardized framework for processing and analyzing mass spectrometry-based single-cell proteomics data in R. Developed by Vanderaa and Gatto at UCLouvain.

## Key Features

- **QFeatures Integration**: Builds on established Bioconductor infrastructure
- **SingleCellExperiment Compatibility**: Access to scRNA-seq tools
- **Modular Workflow**: Flexible processing pipeline
- **Normalization Methods**: Multiple approaches for batch correction
- **Imputation**: Handle missing data common in SCP

## Installation

```r
if (!require("BiocManager"))
    install.packages("BiocManager")
BiocManager::install("scp")
```

## Basic Workflow

Import search-engine result tables and sample metadata into `scp`/`QFeatures`; inspect run and cell quality; filter features; normalize the appropriate assays; aggregate peptides to proteins; then fit statistical models or perform other downstream analysis. Required identifiers, assay names and function arguments depend on the data. Use the [official vignette](https://bioconductor.org/packages/scp/) for an executable example.

## Key Functions

| Function | Purpose |
|----------|---------|
| `readSCP()` | Import data |
| `filterFeatures()` | QC filtering |
| `normalize()` | Normalization |
| `aggregateFeatures()` | Peptide → Protein |
| `impute()` | Handle missing values |

## Companion Packages

- **scpdata**: Pre-formatted SCP datasets
- **QFeatures**: Underlying data structure
- **SingleCellExperiment**: Integration point

## Documentation

- Vignette: https://uclouvain-cbio.github.io/scp/
- Workshop: https://github.com/lgatto/2024_scpworkshop_EUBIC

## Key Publications

> [!cite] Primary References
> - Vanderaa & Gatto (2021) - Replication of single-cell proteomics data reveals important computational challenges.
> - Vanderaa & Gatto (2023) - The current state of single-cell proteomics data analysis. *Current Protocols* 3(1), e658.
>   DOI: [10.1002/cpz1.658](https://doi.org/10.1002/cpz1.658)

## Related Tools

- [[MaxQuant]] - Upstream data processing
- [[DIA-NN]] - DIA data processing
- [[DO-MS]] - Quality control

## Source Check

- Source checked on 2026-10-20: [scp Package documentation or source](https://bioconductor.org/packages/scp/).
- [Author conference abstract with publication list](https://eurobioc2023.bioconductor.org/abstracts/paper19/).
