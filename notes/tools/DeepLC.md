---
title: DeepLC
aliases:
  - DeepLC
tags:
  - tools
  - software
category: tool
url: 
date_created: 2026-03-25
---

# DeepLC

**A deep-learning tool for peptide retention time prediction in LC-MS workflows.**

## Overview

DeepLC predicts peptide retention times to improve identification confidence, library construction, and rescoring workflows.

## Key Features

- **Retention Time Prediction**: Improves alignment and confidence.
- **ML-Driven Calibration**: Adapts to specific LC setups.
- **Workflow Integration**: Useful in both DDA and DIA pipelines.
- **Cross-Platform**: Windows, Linux, macOS

## Installation

```bash
# Installation commands
# pip install deeplc
```

## Usage

```r
# Example code
# Typically used in Python-based pipelines
```

## Input/Output

**Input:**
- Peptide sequences/modifications
- Calibration peptides (optional)

**Output:**
- Predicted retention times
- RT features for downstream scoring

## Key Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| calibration_set | user-defined | Peptides used for RT calibration |
| model_profile | user-defined | Retention time prediction profile |

## Key Publications

> [!cite] Primary Reference
> Bouwmeester et al. (2021) *Nature Methods*

## Links

- GitHub:
- Documentation:

## Related Tools

- [[AlphaPeptDeep]]
- [[Prosit]]
- [[Percolator]]
