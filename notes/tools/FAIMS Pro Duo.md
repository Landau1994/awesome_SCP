---
title: FAIMS Pro Duo
aliases:
  - FAIMS Pro Duo
tags:
  - tools
  - equipment
category: tool
url: 
date_created: 2026-01-18
---

# FAIMS Pro Duo

**A FAIMS interface for gas-phase ion filtering that improves selectivity and sensitivity in LC-MS workflows.**

## Overview

FAIMS Pro Duo adds differential ion mobility separation before mass analysis, reducing chemical noise and improving detection of low-abundance peptides.

## Key Features

- **Ion Mobility Filtering**: Improves spectral clarity and selectivity.
- **Low-Abundance Support**: Enhances identification in complex samples.
- **Workflow Compatibility**: Integrates with Orbitrap-class platforms.
- **Method Flexibility**: Compensation voltage strategies for targeted goals.

## Installation

```bash
# Vendor-installed hardware accessory and control integration
```

## Usage

```r
# Configure compensation voltage scheme in instrument methods
```

## Input/Output

**Input:**
- Raw files (.raw, .d, .mzML)
- LC-MS methods with FAIMS compensation settings

**Output:**
- Protein/peptide matrices
- Quality metrics

## Key Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| compensation_voltage | method-dependent | Ion filtering condition |
| cv_cycle_scheme | method-dependent | Number and order of CV steps |

## Key Publications

> [!cite] Primary Reference
> See FAIMS-enabled low-input proteomics studies in literature notes.

## Links

- GitHub:
- Documentation: https://www.thermofisher.com

## Related Tools

- [[MaxQuant]]
- [[DIA-NN]]
- [[scp Package]]
