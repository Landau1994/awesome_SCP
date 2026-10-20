---
title: DIA-NN
aliases:
  - Deep Learning-based DIA Analysis
  - DIANN
tags:
  - tools
  - software
  - DIA
  - deep-learning
category: tool
url: https://github.com/vdemichev/DiaNN
---

# DIA-NN

**Deep Learning-based DIA Analysis**

## Overview

DIA-NN is software for data-independent acquisition (DIA) proteomics that uses deep neural networks for peptide identification. It has become the primary analysis tool for [[plexDIA]] experiments.

## Key Features

- **Neural Network Scoring**: Deep learning-based identification
- **Library-Free Mode**: Can search directly from FASTA
- **plexDIA Support**: Native module for multiplexed DIA
- **Speed**: Highly optimized, processes data rapidly
- **Environment**: Official distributions support Windows and Linux; check release-specific input-format and dependency requirements.

## plexDIA Module

DIA-NN supports multiplexed DIA with configured isotope labels and channel-specific quantification. Use the official plexDIA documentation for label definitions, channel handling, transfer and FDR settings; the earlier four-step sequence should not be treated as a verified algorithm specification.

## Typical Parameters

Choose mass tolerances, protein inference/quantification settings and channel definitions from the [documentation for the exact release](https://github.com/vdemichev/DiaNN). The previous `--quantification-strategy Any` and `--pg-level Genes` examples were not verified command-line syntax. A 20 ppm tolerance is not a universal default.

## Input/Output

**Input:**

- Raw files (.raw, .d, .mzML)
- Spectral library or FASTA
- mTRAQ/dimethyl label definitions

**Output:**

- Protein/peptide matrices
- Quality metrics
- Visualization reports

## Key Publications

> [!cite] Primary Reference
> Demichev et al. (2020) *Nature Methods*
> DOI: [10.1038/s41592-019-0638-x](https://doi.org/10.1038/s41592-019-0638-x)

## Links

- GitHub: https://github.com/vdemichev/DiaNN
- Documentation: https://github.com/vdemichev/DiaNN/wiki

## Related Tools

- [[MaxQuant]] - DDA analysis
- [[scp Package]] - Downstream analysis
- [[plexDIA]] - Primary use case

## Source Check

- Source checked on 2026-10-20: [DIA-NN documentation or source](https://github.com/vdemichev/DiaNN).
