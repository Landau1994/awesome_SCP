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

```r
library(scp)
library(QFeatures)

# Read data
scp <- readSCP(assayData, colData, ...)

# Quality control
scp <- filterFeatures(scp, ~ !is.na(intensity))

# Normalization
scp <- normalize(scp, method = "center.median")

# Aggregation
scp <- aggregateFeatures(scp, fcol = "protein")

# Batch correction
scp <- batchCorrect(scp, batch = "batch")
```

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
> - Vanderaa & Gatto (2021) - scp package paper
> - Vanderaa & Gatto (2024) - Standardized workflow
>   DOI: [10.1002/cpz1.658](https://doi.org/10.1002/cpz1.658)

## Related Tools

- [[MaxQuant]] - Upstream data processing
- [[DIA-NN]] - DIA data processing
- [[DO-MS]] - Quality control
