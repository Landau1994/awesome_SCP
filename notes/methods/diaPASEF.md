---
title: diaPASEF
aliases:
  - diaPASEF
  - dia-PASEF
tags:
  - methods
category: method
url: 
date_created: 2026-03-25
---

# diaPASEF

**A data-independent acquisition strategy that combines DIA with PASEF ion mobility separation.**

## Overview

diaPASEF synchronizes DIA windowing with ion mobility, improving selectivity and sensitivity in complex proteomics measurements.

## Key Features

- **DIA + Mobility Coupling**: Enhances peptide separation and identification.
- **Efficient Duty Cycle**: Improves ion usage in acquisition.
- **Low-Input Compatibility**: Useful for sensitive SCP-adjacent analyses.

## Workflow

```text
Mobility-aware DIA window setup → PASEF acquisition → DIA deconvolution and quantification
```

## Performance

- **Proteins per cell**: High, depending on sample/instrument settings
- **Throughput**: High
- **Data completeness**: Improved relative to many conventional modes

## Advantages

- Better selectivity and quantitative robustness
- Compatible with high-throughput gradient strategies
- Strong fit for modern timsTOF workflows

## Limitations

- Requires specific instrument capabilities
- Acquisition optimization can be complex
- Software support quality affects final performance

## Key Publications

> [!cite] Primary Reference
> Meier et al. (2020) *Molecular & Cellular Proteomics*

## Related Methods

- [[PASEF]]
- [[DIA]]
- [[diagonal-PASEF]]
