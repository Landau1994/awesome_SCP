---
title: SPDB
aliases:
  - Single-cell Proteomic DataBase
  - scProteomicsDB
tags:
  - database
  - resource
  - datasets
  - reference
category: database
url: https://scproteomicsdb.com/
---

# SPDB

**Single-cell Proteomic DataBase**

## Overview

SPDB is a database for single-cell proteomics data, integrating datasets from both mass spectrometry-based and antibody-based technologies.

## Statistics

Snapshot of the public homepage, checked 2026-10-20:

- **Datasets**: 143
- **Cells**: 398,038,707
- **Proteins**: 8,304
- **Species**: Human, mouse, rhesus macaque and pig
- **Technologies**: 12

These are database-wide totals across mass-spectrometry and antibody-based technologies. They are not the number of MS-measured single-cell proteomes, and the protein total is not a per-cell depth.

## Technologies Covered

### Mass Spectrometry-Based
- [[SCoPE2]]
- [[plexDIA]]
- [[nanoPOTS]]
- Label-free DIA

### Antibody-Based
- CyTOF (Mass Cytometry)
- Flow Cytometry
- CITE-seq (protein component)

## Features

- **Unified Format**: Standardized data structure
- **Search**: Query by protein, cell type, tissue
- **Visualization**: Interactive plots
- **Download**: Bulk data export

## Data Format

Dataset downloads include expression data and annotations. Processing and normalization should be checked for each study and technology; a single universal analysis pipeline should not be assumed. Available data include:
- Normalized expression matrices
- Annotated metadata
- Quality metrics

## Access

**Website**: https://scproteomicsdb.com/

## Use Cases

1. Benchmark datasets for method development
2. Reference data for cell type annotation
3. Meta-analysis across studies
4. Training data for ML models

## Key Publications

> [!cite] Primary Reference
> Wang et al. (2024) *Nucleic Acids Research*
> DOI: [10.1093/nar/gkad1018](https://doi.org/10.1093/nar/gkad1018)

## Related Resources

- [[SingPro]] - Related resource with its own scope and release history
- scpdata - Bioconductor datasets

## Sources

- [SPDB official homepage, checked 2026-10-20](https://scproteomicsdb.com/)
- [SPDB original database paper](https://doi.org/10.1093/nar/gkad1018)
