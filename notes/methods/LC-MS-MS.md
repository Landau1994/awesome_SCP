---
title: LC-MS/MS
aliases:
  - LC-MS/MS
  - LC-MS-MS
tags:
  - methods
category: method
url: 
date_created: 2026-03-25
---

# LC-MS/MS

**Tandem mass spectrometry coupled with liquid chromatography for peptide identification and quantification.**

## Overview

LC-MS/MS extends LC-MS by fragmenting precursor ions to obtain sequence-informative MS2 spectra, enabling proteome-scale analysis.

## Key Features

- **MS2 Fragmentation**: Provides identification-level peptide evidence.
- **Proteomics Standard**: Core platform for DDA and DIA analyses.
- **High-Information Output**: Supports sequence-level annotation.

## Workflow

```text
LC separation → MS1 survey → Precursor selection/windowing → MS2 fragmentation → Database/library search
```

## Performance

- **Proteins per cell**: Strongly depends on acquisition strategy
- **Throughput**: Moderate to high
- **Data completeness**: Better in DIA-like implementations

## Advantages

- Enables confident peptide/protein identification
- Supports discovery and targeted analyses
- Compatible with advanced computational pipelines

## Limitations

- Complex spectra require robust software support
- Sensitivity and depth depend on instrument/method tuning
- Computational burden can be high for large cohorts

## Key Publications

> [!cite] Primary Reference
> Foundational platform across modern proteomics studies.

## Related Methods

- [[LC-MS]]
- [[DDA]]
- [[DIA]]
