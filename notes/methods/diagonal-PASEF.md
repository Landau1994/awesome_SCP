---
title: diagonal-PASEF
aliases:
  - diagonal-PASEF
tags:
  - methods
category: method
url: 
date_created: 2026-03-25
---

# diagonal-PASEF

**A DIA/PASEF acquisition variant leveraging ion mobility-mass correlation for improved selectivity.**

## Overview

diagonal-PASEF is designed to improve low-input and short-gradient performance by constraining acquisition along informative mobility-m/z trajectories.

## Key Features

- **Mobility-Aware Windowing**: Better signal separation in complex samples.
- **Low-Input Utility**: Useful in single-cell-equivalent benchmarks.
- **DIA-Compatible**: Integrates with modern DIA processing tools.

## Workflow

```text
Ion mobility-aware window design → PASEF-style acquisition → DIA deconvolution/quantification
```

## Performance

- **Proteins per cell**: Improved in low-input comparisons
- **Throughput**: High
- **Data completeness**: Strong with optimized settings

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
> See LFQ benchmark and related method papers.

## Related Methods

- [[PASEF]]
- [[diaPASEF]]
- [[ZT Scan DIA]]
