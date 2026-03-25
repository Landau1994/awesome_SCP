---
title: timsTOF
aliases:
  - timsTOF
  - timsTOF Ultra 2
  - Bruker timsTOF Ultra 2
  - timsTOF Ultra2
  - Bruker timsTOF Ultra2
  - timsTOF Pro 2
tags:
  - tools
  - software
category: tool
url: 
date_created: 2026-01-18
---

# timsTOF

**A timsTOF-family mass spectrometry platform combining trapped ion mobility with fast acquisition for sensitive proteomics.**

## Overview

timsTOF instruments are widely used for high-sensitivity DIA/PASEF proteomics and are particularly effective in low-input and high-throughput workflows.

## Key Features

- **Ion Mobility Separation**: Adds an orthogonal dimension for better selectivity.
- **PASEF Compatibility**: Supports efficient, fast MS/MS acquisition.
- **Low-Input Performance**: Strong sensitivity for SCP-adjacent applications.
- **Workflow Breadth**: Supports discovery and targeted-style analyses.

## Installation

```bash
# Vendor-managed hardware/software installation
```

## Usage

```r
# Acquisition is configured in instrument software.
# Downstream analysis is handled by external tools.
```

## Input/Output

**Input:**
- Raw files (.raw, .d, .mzML)
- Method settings (DIA/PASEF windows, cycle time)

**Output:**
- Protein/peptide matrices
- Quality metrics

## Key Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| acquisition_mode | PASEF/diaPASEF | Selects acquisition strategy |
| cycle_time | method-dependent | Balances depth and precision |

## Key Publications

> [!cite] Primary Reference
> Meier et al. (2018, 2020) timsTOF/PASEF foundational papers.

## Links

- GitHub:
- Documentation: https://www.bruker.com

## Related Tools

- [[MaxQuant]]
- [[DIA-NN]]
- [[scp Package]]
