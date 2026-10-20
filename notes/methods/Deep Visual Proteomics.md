---
title: Deep Visual Proteomics
aliases:
  - Deep Visual Proteomics
  - DVP
tags:
  - methods
category: method
url: https://www.nature.com/articles/s41587-022-01302-5
date_created: 2026-03-25
---

# Deep Visual Proteomics

**A spatially resolved workflow integrating imaging, AI-guided selection, and mass spectrometry.**

## Overview

Deep Visual Proteomics (DVP) combines microscopy-based phenotyping with targeted microdissection and LC-MS analysis to map proteomes in tissue context. The original workflow pools cells with similar image-derived phenotypes for proteomic measurement; imaging at cellular resolution does not by itself mean that every MS sample is a single cell. [[scDVP]] extends the approach to individual microdissected cell slices.

## Key Features

- **Image-to-Proteome Mapping**: Connects morphology and molecular profiles.
- **AI-Guided Selection**: Prioritizes cells/regions based on image features.
- **Spatial Resolution**: Preserves tissue architecture information.

## Workflow

```text
Tissue imaging → Computational phenotyping → Targeted microdissection → LC-MS analysis → Spatial proteome interpretation
```

## Performance

Coverage depends on the number and size of pooled targets, tissue preparation and MS settings. Protein depth from a pooled DVP sample must not be reported as a per-cell measurement. Throughput includes imaging, selection, microdissection and MS acquisition.

## Advantages

- Directly links phenotype and proteome
- Useful for heterogeneous tissue studies
- Supports disease microenvironment analysis

## Limitations

- Requires integrated imaging and MS infrastructure
- Selection bias possible if phenotype model is limited
- Throughput lower than bulk-only pipelines

## Key Publications

> [!cite] Primary Reference
> Mund et al. (2022), *Deep Visual Proteomics defines single-cell identity and heterogeneity*. [Nature Biotechnology](https://www.nature.com/articles/s41587-022-01302-5).

> [!cite] Single-cell extension
> *Spatial single-cell mass spectrometry defines zonation of the hepatocyte proteome* (2023). [Nature Methods](https://www.nature.com/articles/s41592-023-02007-6).

## Related Methods

- [[scDVP]]
- [[Laser Microdissection]]
- [[Spatial proteomics]]

## Sources

- [Reference for Deep Visual Proteomics](https://www.nature.com/articles/s41587-022-01302-5)
