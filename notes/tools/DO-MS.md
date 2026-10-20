---
title: DO-MS
aliases:
  - Data-driven Optimization of Mass Spectrometry
  - DOMS
tags:
  - tools
  - QC
  - optimization
  - visualization
category: tool
url: https://github.com/SlavovLab/DO-MS
---

# DO-MS

**Data-driven Optimization of Mass Spectrometry**

## Overview

DO-MS is an open-source interactive platform for quality control and optimization of LC-MS/MS proteomics experiments. Essential for troubleshooting and improving SCP workflows.

## Key Features

- **Interactive Dashboards**: Interactive inspection of loaded result files
- **QC Metrics**: Comprehensive quality assessment
- **Optimization Guidance**: Identify bottlenecks
- **Report Generation**: Shareable HTML reports
- **DDA & DIA Support**: Works with both acquisition modes

## QC Modules

### Instrument Performance
- MS1/MS2 injection times
- Cycle times
- Ion accumulation

### Chromatography
- Peak widths
- Retention time stability
- Gradient optimization

### Identification
- PSM rates
- Peptide/protein counts
- Search engine scores

### Quantification
- Missing value patterns
- Intensity distributions
- Coefficient of variation

## Usage

Clone or download the [official repository](https://github.com/SlavovLab/DO-MS), install its documented R dependencies, and launch the Shiny application as described there (for example through the RStudio project and app launch files). The project website hosts documentation. The earlier `DO_MS::DO_MS()` package call was not the documented launch route.

## Input Files

- [[MaxQuant]] evidence.txt
- [[MaxQuant]] msms.txt
- [[DIA-NN]] output files

## Key Publications

> [!cite] Primary Reference
> Huffman et al. (2019) *J Proteome Research*
> DOI: [10.1021/acs.jproteome.9b00039](https://doi.org/10.1021/acs.jproteome.9b00039)

## Links

- Website: https://do-ms.slavovlab.net/
- GitHub: https://github.com/SlavovLab/DO-MS

## Related Tools

- [[MaxQuant]] - Data source
- [[scp Package]] - Downstream analysis

## Source Check

- Source checked on 2026-10-20: [DO-MS documentation or source](https://github.com/SlavovLab/DO-MS).
