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
url: https://do-ms.slavovlab.net/
---

# DO-MS

**Data-driven Optimization of Mass Spectrometry**

## Overview

DO-MS is an open-source interactive platform for quality control and optimization of LC-MS/MS proteomics experiments. Essential for troubleshooting and improving SCP workflows.

## Key Features

- **Interactive Dashboards**: Real-time data visualization
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

### R Shiny App

```r
# Install
devtools::install_github("SlavovLab/DO-MS")

# Run
DO_MS::DO_MS()
```

### Online Version

Available at: https://do-ms.slavovlab.net/

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
