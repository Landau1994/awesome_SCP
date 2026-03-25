---
title: scDVP
aliases:
  - scDVP
tags:
  - methods
category: method
url: 
date_created: 2026-03-25
---

# scDVP

**Single-cell Deep Visual Proteomics workflow for spatially resolved single-cell proteome mapping.**

## Overview

scDVP adapts Deep Visual Proteomics to single-cell-level sampling and analysis, enabling zonation and microenvironment proteome studies.

## Key Features

- **Single-Cell Spatial Resolution**: Captures cell-level proteomic gradients.
- **Imaging-Guided Selection**: Uses tissue context to prioritize cells.
- **Disease Context Utility**: Suitable for architecture-disrupted tissues.

## Workflow

```text
Tissue staining/imaging → Cell selection strategy → Microdissection → LC-MS analysis → Spatial gradient modeling
```

## Performance

- **Proteins per cell**: Typically high for spatial single-cell proteomics
- **Throughput**: Moderate
- **Data completeness**: Good with optimized prep/acquisition

## Advantages

- Preserves tissue architecture information
- Connects morphology to proteome programs
- Enables continuous spatial gradient analysis

## Limitations

- Technically demanding end-to-end pipeline
- Lower throughput than dissociated-cell workflows
- Requires substantial image-analysis infrastructure

## Key Publications

> [!cite] Primary Reference
> See Nat Metab 2026 human liver scDVP literature note.

## Related Methods

- [[Deep Visual Proteomics]]
- [[Laser Microdissection]]
- [[Spatial proteomics]]
