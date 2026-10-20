---
title: SingPro
aliases:
  - Single-cell Proteomics Knowledge Base
tags:
  - database
  - resource
  - raw-data
  - protocols
category: database
url: https://singpro.idrblab.net/
---

# SingPro

**Single-cell Proteomics Knowledge Base**

## Overview

SingPro is a specialized database for single-cell proteomics that provides links to original data and detailed experimental metadata for both MS-based and flow cytometry-based studies.

## Key Features

- **Original Data Links**: Availability depends on the contributing study
- **Experimental Details**: Comprehensive protocol information
- **Expression Profiles**: Processed protein quantification
- **Multi-Technology**: MS and flow cytometry coverage

## Data Content

### Metadata Fields
- Sample type and organism
- Cell isolation method
- MS instrument parameters
- Data processing pipeline
- Quality metrics

### Expression Data
- Protein-level quantification
- Cell-level annotations
- Batch information

## Access

> [!info] Publication
> [Nucleic Acids Research 2024](https://academic.oup.com/nar/article/52/D1/D552/7306671)

## Unique Strengths

The resource organizes study descriptions, original-data links and expression profiles. Availability of raw data, protocols and processed matrices must be checked on the selected study record.

As checked on 2026-10-20, the homepage presents **SingPro 2.0**: it describes an existing foundation of 204 SCP studies with over 625 million cells and over 16,000 proteins, plus 814 newly incorporated multimodal studies with approximately 81.5 million cells. These are separately described collections and are not counts of MS-only single-cell proteomes. The original 2024 database article should not be cited as evidence for every later release statistic.

## Comparison with SPDB

Both SingPro and [[SPDB]] integrate studies measured with different technologies. Compare releases, included studies, measurement modalities and download availability before comparing totals. The presence of an original-data link is study-specific; an unsupported yes/no ranking of the two resources is not appropriate.

## Use Cases

- Method benchmarking
- Protocol optimization
- Training data curation
- Reproducibility studies

## Key Publications

> [!cite] Primary Reference
> *Nucleic Acids Research* (2024) Database Issue
> DOI: [10.1093/nar/gkad830](https://doi.org/10.1093/nar/gkad830)

## Related Resources

- [[SPDB]] - Related database; release and modality must be matched before comparison
- scpdata - R/Bioconductor access

## Sources

- [SingPro official homepage and release description, checked 2026-10-20](https://singpro.idrblab.net/)
- [SingPro original database paper](https://doi.org/10.1093/nar/gkad830)
