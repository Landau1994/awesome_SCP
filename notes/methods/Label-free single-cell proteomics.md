---
title: Label-free single-cell proteomics
aliases:
  - Label-free single-cell proteomics
  - label-free single-cell mass spectrometry
tags:
  - methods
category: method
url: 
date_created: 2026-01-18
---

# Label-free single-cell proteomics

**A single-cell proteomics strategy without isobaric carrier labeling, relying on high-sensitivity LC-MS workflows for direct quantification.**

## Overview

Label-free single-cell proteomics quantifies proteins in individual cells without multiplexed isobaric tags. It emphasizes sample recovery, low-background processing, and highly sensitive MS acquisition (often DIA-based) to improve protein coverage and quantitative fidelity at very low input amounts.

## Key Features

- **Direct Quantification**: Avoids carrier-induced ratio compression in isobaric workflows.
- **High Quantitative Fidelity**: Preserves relative abundance differences between cells.
- **Instrument-Driven Sensitivity**: Benefits from modern platforms (e.g., Orbitrap Astral, timsTOF).

## Workflow

```text
Single-cell isolation -> Low-loss lysis/digestion -> Cleanup/desalting -> LC-MS/MS acquisition -> Quantification and downstream analysis
```

## Performance

- **Proteins per cell**: Typically hundreds to ~1,500+ depending on workflow and instrument.
- **Throughput**: Moderate to high with short-gradient optimized methods.
- **Data completeness**: Improves with DIA and robust normalization/imputation strategies.

## Advantages

- No carrier channel required, simplifying interpretation.
- Compatible with modern DIA-centric computational pipelines.
- Strong fit for cell-state heterogeneity and trajectory studies.

## Limitations

- Sensitive to sample loss and contamination at ultra-low input.
- More challenging missing-value handling than bulk proteomics.
- Requires careful method optimization across prep, LC, and acquisition.

## Key Publications

> [!cite] Primary Reference
> Brunner et al. (2022) *Molecular Systems Biology*.
> Zhu et al. (2026) label-free SCP studies in developing brain contexts.

## Related Methods

- [[SCoPE2]]
- [[plexDIA]]
- [[nPOP]]
