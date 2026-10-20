---
title: diagonal-PASEF
aliases:
  - diagonal-PASEF
tags:
  - methods
category: method
url: https://www.bruker.com/en/products-and-solutions/mass-spectrometry/timstof/pasef.html
date_created: 2026-03-25
---

# diagonal-PASEF

**A DIA/PASEF acquisition variant leveraging ion mobility-mass correlation for improved selectivity.**

## Overview

diagonal-PASEF synchronizes a moving quadrupole isolation window with the TIMS ramp to follow the diagonal mobility–m/z distribution of peptide precursors. Bruker uses the term for methods including midia-PASEF and synchro-PASEF.

## Key Features

- **Mobility-Aware Windowing**: Better signal separation in complex samples.
- **Low-Input Utility**: Useful in single-cell-equivalent benchmarks.
- **DIA-Compatible**: Integrates with modern DIA processing tools.

## Workflow

```text
Ion mobility-aware window design → PASEF-style acquisition → DIA deconvolution/quantification
```

## Performance

Performance depends on the particular implementation, quadrupole/mobility synchronization, gradient, input and analysis. A study of one diagonal-PASEF implementation does not establish the same gain for every member of this method family.

## Advantages

- Better quantification in challenging inputs
- Adds orthogonal separation information
- Supports high-throughput gradients

## Limitations

- Instrument/method dependency
- Requires careful method optimization
- Analysis software support is essential

## Key Publications

> [!cite] Primary Reference
> [Bruker PASEF technology documentation](https://www.bruker.com/en/products-and-solutions/mass-spectrometry/timstof/pasef.html)
> Performance example: [10.1016/j.mcpro.2025.101480](https://doi.org/10.1016/j.mcpro.2025.101480)

## Related Methods

- [[PASEF]]
- [[diaPASEF]]
- [[ZT Scan DIA]]

## Sources

- [Reference for diagonal-PASEF](https://www.bruker.com/en/products-and-solutions/mass-spectrometry/timstof/pasef.html)
