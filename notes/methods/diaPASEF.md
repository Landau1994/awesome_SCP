---
title: diaPASEF
aliases: ["diaPASEF"]
tags:
  - methods
category: method
url: https://www.nature.com/articles/s41592-020-00998-0
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

The original work evaluated ion usage, coverage and quantitative performance under defined timsTOF acquisition conditions. Protein depth, throughput and completeness in single-cell applications depend on subsequent sample preparation and acquisition choices.

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
> Meier F, Brunner AD, Frank M, et al. (2020). diaPASEF: parallel accumulation–serial fragmentation combined with data-independent acquisition. *Nature Methods* 17, 1229–1236.
> [10.1038/s41592-020-00998-0](https://doi.org/10.1038/s41592-020-00998-0)

## Related Methods

- [[PASEF]]
- [[DIA]]
- [[diagonal-PASEF]]

## Sources

- [Reference for diaPASEF](https://www.nature.com/articles/s41592-020-00998-0)
