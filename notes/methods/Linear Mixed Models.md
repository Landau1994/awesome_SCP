---
title: Linear Mixed Models
aliases:
  - Linear Mixed Models
  - LMM
tags:
  - methods
category: method
url: https://www.jstatsoft.org/article/view/v067i01
date_created: 2026-03-25
---

# Linear Mixed Models

**A statistical framework combining fixed and random effects for structured biological data.**

## Overview

Linear Mixed Models (LMMs) are useful for continuous gradient analysis, repeated measures, and cohort-structured proteomics datasets.

## Key Features

- **Fixed + Random Effects**: Separates global and group-specific variance.
- **Hierarchical Data Support**: Handles donor/batch/sample structure.
- **Dependence Modeling**: Can account for specified grouping structure when model assumptions and replication are adequate.

## Workflow

```text
Define formula and random structure → Fit model → Estimate effects → Multiple testing control
```

## Performance

A fitted mixed model does not create missing measurements. Inference depends on the fixed/random-effect structure, the number of independent groups, residual assumptions and the missing-data mechanism. Unbalanced observations can be modeled under appropriate assumptions.

## Advantages

- Appropriate for nested and repeated designs
- Can reduce pseudoreplication when the dependence structure is specified appropriately
- Interpretable coefficients and uncertainty

## Limitations

- Model specification can be non-trivial
- Assumption checks are important
- Computational cost rises with model complexity

## Key Publications

Bates et al. (2015). [Fitting Linear Mixed-Effects Models Using lme4](https://www.jstatsoft.org/article/view/v067i01).

## Related Methods

- [[GSEA]]
- [[WGCNA]]
- [[RNA Velocity]]

## Sources

- [Reference for Linear Mixed Models](https://www.jstatsoft.org/article/view/v067i01)
