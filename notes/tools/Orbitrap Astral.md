---
title: Orbitrap Astral
aliases: []
tags:
  - tools
  - equipment
category: tool
url: https://www.nature.com/articles/s41587-023-02099-7
date_created: 2026-01-18
---

# Orbitrap Astral

**A high-speed, high-sensitivity hybrid mass spectrometry platform used for deep and high-throughput proteomics.**

## Overview

Orbitrap Astral is a Thermo Scientific mass spectrometry platform that combines Orbitrap mass accuracy with Astral high-speed MS/MS acquisition. In single-cell and low-input proteomics, it is frequently used with DIA or narrow-window DIA workflows to improve depth, quantitative precision, and throughput.

## Key Features

- **High MS/MS Scan Speed**: Supports rapid acquisition for short-gradient and high-throughput workflows.
- **High Sensitivity**: Improves detection in low-input and single-cell-equivalent samples.
- **DIA-Ready Performance**: Works well with DIA, nDIA, and related deconvolution-heavy pipelines.
- **Proteomics-Oriented Ecosystem**: Widely used with modern tools such as DIA-NN and FragPipe.

## Input/Output

**Input:**

- Tryptic peptide samples from bulk/low-input/single-cell workflows
- LC gradients (short or long) with DIA/DDA acquisition methods
- Instrument method settings (scan windows, resolution, cycle time)

**Output:**

- Raw MS files (commonly `.raw`) for downstream search/quantification
- Peptide/protein quantification matrices after software processing
- QC metrics (coverage, CV, ID rate, missingness)

## Key Publications

> [!cite] Primary Reference
> Guzman et al. (2024). Ultra-fast label-free quantification and comprehensive proteome coverage with narrow-window data-independent acquisition. *Nature Biotechnology*.
> DOI: [10.1038/s41587-023-02099-7](https://doi.org/10.1038/s41587-023-02099-7)

## Links

- Application/reference: [Original nDIA study](https://www.nature.com/articles/s41587-023-02099-7)
- Product-family overview: [[Orbitrap]]

## Related Tools

- [[timsTOF]]
- [[DIA-NN]]
- [[FragPipe]]
- [[Skyline]]

## Source Check

- Source checked on 2026-10-20: [Orbitrap Astral documentation or source](https://www.nature.com/articles/s41587-023-02099-7).
