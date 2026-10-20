---
title: pSCoPE
aliases:
  - Prioritized SCoPE
  - Targeted SCoPE
tags:
  - methods
  - targeted
  - TMT
  - validation
category: method
url: https://www.nature.com/articles/s41592-023-01830-1
---

# pSCoPE

**Prioritized Single-Cell ProtEomics**

## Overview

pSCoPE schedules previously identified peptides by priority and retention time to improve the consistency and efficiency of MS/MS sampling. It combines targeted prioritization with broad proteome coverage; it is not restricted to a small validation panel.

## Key Features

- Prioritizes thousands of peptides rather than selecting precursors solely by instantaneous intensity.
- Uses real-time acquisition control implemented with MaxQuant.Live.
- Can improve sensitivity, completeness and depth together; gains depend on the priority list and instrument settings.

## Workflow

```text
Single-cell preparation and TMT labeling → Priority-list construction → MaxQuant.Live acquisition → Identification and quantitative QC
```

## Reported Benchmark

Huffman et al. evaluated HEK and melanoma cells prepared using nPOP, with 60-minute active gradients and 0.5-Th isolation windows. Relative to the compared shotgun workflow, the study reported more than twofold improvements in several sampling and coverage metrics. These results describe that experiment and are not a fixed per-cell protein count.

## Limitations

Priority lists can bias coverage toward previously observed peptides. Transfer to another instrument, sample type or gradient requires acquisition and quantitative validation.

## Primary Reference

> [!cite]
> Huffman RG, Leduc A, Wichmann C, et al. (2023). Prioritized mass spectrometry increases the depth, sensitivity and data completeness of single-cell proteomics. *Nature Methods* 20, 714–722.
> [10.1038/s41592-023-01830-1](https://doi.org/10.1038/s41592-023-01830-1)

## Related Methods

- [[SCoPE2]]
- [[nPOP]]
- [[plexDIA]]
