---
title: scDVP
aliases:
  - scDVP
tags:
  - methods
category: method
url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13031132/
date_created: 2026-03-25
---

# scDVP

**Single-cell Deep Visual Proteomics workflow for spatially resolved single-cell proteome mapping.**

## Overview

scDVP adapts Deep Visual Proteomics to individual, image-selected cell slices isolated from tissue sections. It combines microscopy, laser microdissection and ultrasensitive MS; a microdissected cell slice is not necessarily an intact whole cell.

## Key Features

- **Single-Cell Spatial Resolution**: Captures cell-level proteomic gradients.
- **Imaging-Guided Selection**: Uses tissue context to prioritize cells.
- **Disease Context Utility**: Suitable for architecture-disrupted tissues.

## Workflow

```text
Tissue staining/imaging → Cell selection strategy → Microdissection → LC-MS analysis → Spatial gradient modeling
```

## Performance

The 2023 mouse-liver study reported approximately 1,700 proteins from a hepatocyte cell slice. This is a study-specific result; tissue, slice thickness, selection, multiplexing and MS settings affect depth. The later human-liver study is a separate application and should not be treated as an interchangeable benchmark.

## Advantages

- Preserves tissue architecture information
- Connects morphology to proteome programs
- Enables continuous spatial gradient analysis

## Limitations

- Technically demanding end-to-end pipeline
- Lower throughput than dissociated-cell workflows
- Requires substantial image-analysis infrastructure

## Key Publications

- *Spatial single-cell mass spectrometry defines zonation of the hepatocyte proteome* (2023). [Nature Methods](https://www.nature.com/articles/s41592-023-02007-6).
- [2026 human-liver scDVP study](https://pmc.ncbi.nlm.nih.gov/articles/PMC13031132/).

## Related Methods

- [[Deep Visual Proteomics]]
- [[Laser Microdissection]]
- [[Spatial proteomics]]

## Sources

- [Reference for scDVP](https://pmc.ncbi.nlm.nih.gov/articles/PMC13031132/)
