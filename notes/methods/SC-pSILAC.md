---
title: SC-pSILAC
aliases:
  - SC-pSILAC
tags:
  - methods
category: method
url: https://doi.org/10.1016/j.cell.2025.03.002
date_created: 2026-01-18
---

# SC-pSILAC

**A single-cell adaptation of pulse SILAC for measuring protein synthesis and turnover dynamics.**

## Overview

SC-pSILAC combines stable isotope labeling with single-cell proteomics to estimate newly synthesized versus pre-existing protein pools. It is especially useful for studying temporal regulation, differentiation, and early developmental transitions.

## Key Features

- **Dynamic Proteome Readout**: Captures synthesis/turnover rather than static abundance only.
- **Single-Cell Resolution**: Resolves temporal heterogeneity across cell states.
- **Mechanistic Insight**: Links protein kinetics to lineage progression and functional shifts.

## Workflow

```text
Isotope pulse labeling -> Single-cell isolation -> LC-MS quantification of light/heavy peptides -> Turnover modeling
```

## Performance

- The 2025 study demonstrated detection of two SILAC labels in up to approximately 4,000 proteins in individual HeLa cells; this is not the average in every benchmark.
- In the initial single-HeLa-cell experiment, the paper reported averages of 3,041 quantified proteins and 2,781 proteins with both labels quantified.
- A single-cell endpoint gives a relative turnover readout from light/heavy ratios; it does not directly provide a longitudinal half-life for that same cell.

## Advantages

- Directly measures proteome dynamics.
- Complements transcriptomic velocity-style analyses.
- Valuable for developmental and perturbation studies.

## Limitations

- Experimental complexity (labeling design and timing).
- Requires robust quantification of isotopologue pairs.
- Can reduce depth compared to standard abundance-only workflows.

## Key Publications

> [!cite] Primary Reference
> Sabatier P, Ye Z, et al. (2025). Global analysis of protein turnover dynamics in single cells. *Cell* 188, 2433–2450.e21.
> [10.1016/j.cell.2025.03.002](https://doi.org/10.1016/j.cell.2025.03.002)

## Related Methods

- [[SCoPE2]]
- [[plexDIA]]
- [[nPOP]]

## Sources

- [Reference for SC-pSILAC](https://doi.org/10.1016/j.cell.2025.03.002)
