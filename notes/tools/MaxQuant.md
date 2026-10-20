---
title: MaxQuant
aliases:
  - Max Quant
  - MQ
tags:
  - tools
  - software
  - TMT
  - DDA
  - quantification
category: tool
url: https://maxquant.org/
---

# MaxQuant

**Quantitative Proteomics Software**

## Overview

MaxQuant is a comprehensive software platform for mass spectrometry-based proteomics developed by the Cox lab. It's widely used for TMT-based single-cell proteomics including [[SCoPE2]].

## Key Features

- **Andromeda Search Engine**: Peptide identification
- **TMT/iTRAQ Support**: Isobaric label quantification
- **LFQ**: Label-free quantification
- **Match Between Runs**: Transfers IDs across samples
- **Protein Groups**: Handles protein inference

## SCoPE2 Analysis Settings

The following retained values are illustrative study settings, not universal SCoPE2 defaults. Match the labeling chemistry, instrument and protocol before use:
- Reporter ion quantification: TMTpro 16-plex
- MS/MS tolerance: 20 ppm
- Minimum peptide length: 7
- FDR: 1% at PSM and protein level

## Workflow

```
Raw Files → Andromeda Search →
Reporter Ion Extraction → Protein Quantification →
evidence.txt / proteinGroups.txt
```

## Output Files

| File | Description |
|------|-------------|
| evidence.txt | Peptide-feature/evidence-level records, which may combine supporting spectra |
| peptides.txt | Peptide summaries |
| proteinGroups.txt | Protein-level data |
| msms.txt | MS/MS identification (spectrum/PSM-level) records |

## Limitations for SCP

- GUI and command-line platform support differ; Linux command-line workflows are available. Check the selected release.
- Runtime depends on dataset size, search space and hardware
- Memory requirements depend on the selected workflow
- DIA workflows use [[MaxDIA]]; suitability depends on acquisition and analysis settings.

## Installation

Download from: https://maxquant.org/

## Key Publications

> [!cite] Primary Reference
> Cox & Mann (2008) *Nature Biotechnology*
> DOI: [10.1038/nbt.1511](https://doi.org/10.1038/nbt.1511)

## Related Tools

- [[DIA-NN]] - For DIA data
- [[scp Package]] - Downstream analysis in R
- [[DO-MS]] - Quality control

## Source Check

- Source checked on 2026-10-20: [MaxQuant documentation or source](https://maxquant.org/).
- [Official Linux installation guide](https://www.maxquant.org/static/main/pdf/Linux_MQ_Installation.pdf).
