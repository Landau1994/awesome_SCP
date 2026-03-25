---
title: Linear Mixed Models
aliases:
  - Linear Mixed Models
  - LMM
tags:
  - methods
category: method
url: 
date_created: 2026-03-25
---

# Linear Mixed Models

**A statistical framework combining fixed and random effects for structured biological data.**

## Overview

Linear Mixed Models (LMMs) are useful for continuous gradient analysis, repeated measures, and cohort-structured proteomics datasets.

## Key Features

- **Fixed + Random Effects**: Separates global and group-specific variance.
- **Hierarchical Data Support**: Handles donor/batch/sample structure.
- **Robust Inference**: Suitable for biological replicates with dependence.

## Workflow

```text
Define formula and random structure → Fit model → Estimate effects → Multiple testing control
```

## Performance

- **Proteins per cell**: Not directly applicable
- **Throughput**: High (software-dependent)
- **Data completeness**: Can better accommodate unbalanced designs

## Advantages

- Appropriate for nested and repeated designs
- Reduces false positives from ignored dependency
- Interpretable coefficients and uncertainty

## Limitations

- Model specification can be non-trivial
- Assumption checks are important
- Computational cost rises with model complexity

## Key Publications

> [!cite] Primary Reference
> See spatial liver proteomics literature note using LMM.

## Related Methods

- [[GSEA]]
- [[WGCNA]]
- [[RNA Velocity]]
