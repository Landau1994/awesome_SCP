---
title: Hybrid Spectral Library
aliases:
  - Hybrid Spectral Library
tags:
  - methods
category: method
url: 
date_created: 2026-03-25
---

# Hybrid Spectral Library

**A spectral library strategy combining empirical and predicted spectra to improve coverage.**

## Overview

Hybrid spectral libraries merge experimentally acquired spectra with in silico predicted entries, balancing confidence and proteome depth.

## Key Features

- **Broader Coverage**: Expands identifiable peptide space.
- **Flexible Construction**: Integrates multiple data sources.
- **DIA-Friendly**: Enhances peptide detection in DIA pipelines.

## Workflow

```
Empirical spectra + Predicted spectra → Library merge/curation → DIA search
```

## Performance

- **Proteins per cell**: Can improve depth for low-input datasets
- **Throughput**: High once library is built
- **Data completeness**: Improved in challenging samples

## Advantages

- Extends beyond purely empirical libraries
- Supports rare/modified peptide identification
- Reusable across cohorts

## Limitations

- Requires strict QC and curation
- Prediction quality affects performance
- Potential increase in false positives if poorly filtered

## Key Publications

> [!cite] Primary Reference
> See AlphaPeptDeep/OpenSpec-related workflow papers.

## Related Methods

- [[Open Search]]
- [[DIA]]
- [[Spectral Deconvolution]]
