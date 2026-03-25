---
title: cellenONE
aliases:
  - cellenONE
  - CellenONE
tags:
  - tools
  - software
category: tool
url: 
date_created: 2026-01-18
---

# cellenONE

**A high-precision single-cell dispensing platform for low-volume sample preparation workflows.**

## Overview

cellenONE is used for automated, image-guided single-cell isolation and nanoliter-scale dispensing in single-cell proteomics pipelines.

## Key Features

- **Single-Cell Dispensing**: Accurate isolation into multiwell formats.
- **Image-Guided Selection**: Improves quality control during sorting.
- **Low-Volume Handling**: Supports nanoliter-scale workflows.
- **Automation Ready**: Fits high-throughput SCP setups.

## Installation

```bash
# Vendor-managed hardware/software installation
```

## Usage

```r
# Instrument operation is configured through vendor software
```

## Input/Output

**Input:**
- Raw files (.raw, .d, .mzML)
- Cell suspensions and dispensing protocols

**Output:**
- Protein/peptide matrices
- Quality metrics

## Key Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| droplet_volume | protocol-dependent | Dispensing volume per event |
| selection_criteria | protocol-dependent | Image-based cell selection filters |

## Key Publications

> [!cite] Primary Reference
> See nPOP and low-input SCP method literature notes.

## Links

- GitHub:
- Documentation: https://www.cellenion.com

## Related Tools

- [[MaxQuant]]
- [[DIA-NN]]
- [[scp Package]]
