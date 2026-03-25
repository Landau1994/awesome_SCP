---
title: SC-pSILAC
aliases:
  - SC-pSILAC
tags:
  - methods
category: method
url: 
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

- **Proteins per cell**: Typically lower than static SCP due to kinetic quantification constraints.
- **Throughput**: Moderate.
- **Data completeness**: Depends on labeling efficiency and peptide detectability.

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
> Foundational pSILAC and single-cell turnover studies (see linked literature notes).

## Related Methods

- [[SCoPE2]]
- [[plexDIA]]
- [[nPOP]]
