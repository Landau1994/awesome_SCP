---
title: cellrank
aliases:
  - CellRank
  - cellrank
tags:
  - tools
  - software
category: tool
url: 
date_created: 2026-03-25
---

# cellrank

**A toolkit for probabilistic fate mapping and trajectory inference in single-cell data.**

## Overview

cellrank estimates cell-state transition probabilities and terminal fates using graph-based and velocity-informed models.

## Key Features

- **Fate Probability Estimation**: Quantifies lineage commitment likelihoods.
- **Trajectory Integration**: Works with pseudotime and velocity information.
- **Single-Cell Focus**: Supports developmental and differentiation analyses.
- **Cross-Platform**: Windows, Linux, macOS

## Installation

```bash
# Installation commands
# pip install cellrank
```

## Usage

```r
# Example code
# Use in Python single-cell analysis pipelines
```

## Input/Output

**Input:**
- Single-cell embedding/graph
- Optional velocity or transition priors

**Output:**
- Fate probabilities
- Absorption/lineage statistics

## Key Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| n_states | user-defined | Number of macrostates/terminal states |
| kernel | user-defined | Transition kernel definition |

## Key Publications

> [!cite] Primary Reference
> Lange et al. (2022) *Nature Methods*

## Links

- GitHub:
- Documentation:

## Related Tools

- [[Scanpy]]
- [[RNA Velocity]]
- [[scProtVelo]]
