---
title: single-cell proteomics
aliases: ["single-cell proteomics"]
tags:
  - methods
category: method
url: https://doi.org/10.1186/s13059-021-02267-5
date_created: 2026-03-25
---

# single-cell proteomics

**Proteome measurement at single-cell resolution to capture cellular heterogeneity and functional states.**

## Overview

Single-cell proteomics measures proteins in individual cells. This vault emphasizes mass-spectrometry-based SCP with specialized low-input workflows; antibody-based methods such as [[CITE-seq]] provide complementary targeted protein measurements.

## Key Features

- **Single-Cell Resolution**: Reveals cell-state heterogeneity directly at protein level.
- **Functional Readout**: Captures post-transcriptional regulation effects.
- **Method Diversity**: Includes labeling and label-free acquisition strategies.

## Workflow

```text
Single-cell isolation → Low-input sample prep → LC-MS/MS acquisition → Quantification and cell-state analysis
```

## Performance

Coverage varies from a targeted antibody panel to thousands of proteins in specific MS workflows. Compare measured proteins, quantitative quality, cell recovery and throughput using the same definitions and experimental context.

## Advantages

- Directly measures proteins instead of transcript proxies
- Enables discovery of proteome-level cell subtypes
- Supports multimodal integration with transcriptomics

## Limitations

- No amplification equivalent to nucleic acids
- Technical sensitivity and missingness challenges
- Requires stringent contamination control

## Key Publications

Specht et al. (2021). [Single-cell proteomic and transcriptomic analysis of macrophage heterogeneity using SCoPE2](https://doi.org/10.1186/s13059-021-02267-5), one MS-based example.

## Related Methods

- [[SCoPE2]]
- [[plexDIA]]
- [[Label-free single-cell proteomics]]

## Sources

- [Reference for single-cell proteomics](https://doi.org/10.1186/s13059-021-02267-5)
