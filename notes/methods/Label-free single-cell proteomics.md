---
title: Label-free single-cell proteomics
aliases: ["Label-free single-cell proteomics"]
tags:
  - methods
category: method
url: https://www.nature.com/articles/s41592-024-02558-2
date_created: 2026-01-18
---

# Label-free single-cell proteomics

**A single-cell proteomics strategy without sample-multiplexing isotope or isobaric labels, relying on high-sensitivity LC-MS workflows for direct quantification.**

## Overview

Label-free single-cell proteomics quantifies proteins in individual cells without sample-multiplexing isotope or isobaric tags. It emphasizes sample recovery, low-background processing, and highly sensitive MS acquisition (often DIA-based) to improve protein coverage and quantitative fidelity at very low input amounts.

## Key Features

- **Direct Quantification**: Avoids carrier-induced ratio compression in isobaric workflows.
- **High Quantitative Fidelity**: Preserves relative abundance differences between cells.
- **Instrument-Driven Sensitivity**: Benefits from modern platforms (e.g., Orbitrap Astral, timsTOF).

## Workflow

```text
Single-cell isolation -> Low-loss lysis/digestion -> Cleanup/desalting -> LC-MS/MS acquisition -> Quantification and downstream analysis
```

## Performance

- **Proteins per cell**: Highly workflow-dependent; the 2025 [[Chip-Tip]] HeLa benchmark exceeds 5,000 protein identifications per cell.
- **Throughput**: Moderate to high with short-gradient optimized methods.
- **Data completeness**: Must distinguish directly measured values from imputed estimates; imputation does not create experimental detections.

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
> Brunner et al. (2022). Ultra-high sensitivity mass spectrometry quantifies single-cell proteome changes upon perturbation. *Molecular Systems Biology* 18, e10798. [10.15252/msb.202110798](https://doi.org/10.15252/msb.202110798)
> Ye et al. (2025). Chip-Tip workflow. [10.1038/s41592-024-02558-2](https://doi.org/10.1038/s41592-024-02558-2)

## Related Methods

- [[SCoPE2]]
- [[plexDIA]]
- [[nPOP]]

## Sources

- [Reference for Label-free single-cell proteomics](https://www.nature.com/articles/s41592-024-02558-2)
