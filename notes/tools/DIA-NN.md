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

DIA-NN is a universal software for data-independent acquisition (DIA) proteomics that uses deep neural networks for peptide identification. It has become the primary analysis tool for [[plexDIA]] experiments.

## Key Features

- **Neural Network Scoring**: Deep learning-based identification
- **Library-Free Mode**: Can search directly from FASTA
- **plexDIA Support**: Native module for multiplexed DIA
- **Speed**: Highly optimized, processes data rapidly
- **Cross-Platform**: Windows, Linux, macOS

## plexDIA Module

The plexDIA module handles multiplexed samples by:
1. Splitting spectral library into label channels
2. Generating decoy channels for FDR control
3. Neural network-based scoring
4. Channel-specific quantification

## Typical Parameters

```bash
--mass-acc 20
--mass-acc-ms1 20
--quantification-strategy Any
--pg-level Genes
```

## Input/Output

**Input:**
- Raw files (.raw, .d, .mzML)
- Spectral library or FASTA
- mTRAQ/dimethyl label definitions

**Output:**
- Protein/peptide matrices
- Quality metrics
- Visualization reports

## Installation

```bash
# Download from GitHub
# https://github.com/vdemichev/DiaNN
```

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
