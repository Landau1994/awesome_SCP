---
title: DDA
aliases:
  - "Data-Dependent Acquisition"
  - "Shotgun Proteomics"
tags:
  - methods
category: method
url:
date_created: 2026-03-02
---


# DDA

**Data-Dependent Acquisition (DDA)** is a stochastic mode of mass spectrometry operation where the instrument selects the most abundant precursor ions from a survey scan (MS1) for subsequent fragmentation and analysis (MS2).

## Overview

Data-Dependent Acquisition (DDA), often referred to as "shotgun proteomics," is the classical approach for untargeted protein identification. In a typical DDA cycle, the mass spectrometer performs a full MS1 scan to detect peptide ions eluting from the liquid chromatography (LC) column. The instrument's control software then selects the $N$ most intense precursor ions (Top-$N$) and isolates them individually for fragmentation. The resulting fragment ion spectra (MS/MS or MS2) are recorded and matched against a protein sequence database to identify the peptides. While DDA is highly sensitive for abundant proteins, its stochastic nature leads to the "missing value problem" in complex samples.

## Key Features

- **Top-N Selection**: The instrument automatically selects the $N$ most abundant ions from the MS1 survey scan for fragmentation, prioritizing high-intensity signals.
- **Stochastic Sampling**: Due to the complexity of the proteome and speed limits of the instrument, precursor selection is semi-random, leading to run-to-run variability.
- **Dynamic Exclusion**: To maximize proteome coverage, previously fragmented ions are temporarily excluded from selection to allow the instrument to analyze lower-abundance peptides.

## Workflow

```
LC Separation -> MS1 Survey Scan -> Selection of Top-N Ions -> MS2 Fragmentation -> Database Search
```

## Performance

- **Proteins per cell**: Typically lower than DIA methods in single-cell contexts due to ion sampling limitations; highly dependent on carrier proteome usage (e.g., in SCoPE-MS).
- **Throughput**: Moderate; limited by the cycle time required to sequentially isolate and fragment individual precursors.
- **Data completeness**: Low to Moderate; suffers from high rates of missing values across replicates due to stochastic precursor selection.

## Advantages

- **Established Ecosystem**: Supported by mature software pipelines (e.g., MaxQuant, Proteome Discoverer) and spectral libraries are not required for identification.
- **High Sensitivity**: Excellent for identifying high-abundance proteins and generating spectral libraries for downstream DIA analysis.
- **Direct Identification**: Peptide sequences are identified directly from MS2 spectra via database searching, reducing false discovery rate (FDR) complexities compared to DIA.

## Limitations

- **Missing Values**: The stochastic nature of ion selection results in poor reproducibility between runs, especially for low-abundance peptides.
- **Undersampling**: In complex mixtures, the instrument cannot fragment all eluting peptides, leading to a bias towards high-abundance proteins.
- **Cycle Time Constraints**: Increasing the number of MS2 scans (Top-$N$) extends the cycle time, potentially reducing the sampling frequency across the chromatographic peak.

## Key Publications

> [!cite] Primary Reference
> Yates, J. R., Ruse, C. I., & Nakorchevsky, A. (2009). Proteomics by mass spectrometry: approaches, advances, and applications. *Annual Review of Biomedical Engineering*.
> DOI: [10.1146/annurev-bioeng-061008-124934](https://doi.org/10.1146/annurev-bioeng-061008-124934)
