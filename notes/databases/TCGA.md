---
title: TCGA
aliases:
  - The Cancer Genome Atlas
  - The Cancer Genome Atlas Program
tags:
  - database
  - resource
  - cancer
  - genomics
  - multi-omics
category: database
url: https://www.cancer.gov/ccg/research/genome-sequencing/tcga
date_created: 2026-03-17
---

# TCGA

**The Cancer Genome Atlas — a landmark NCI/NHGRI program that molecularly characterized over 20,000 primary cancer and matched normal samples spanning 33 cancer types, generating multi-omics data (genomics, transcriptomics, proteomics, epigenomics) freely available to the research community.**

## Overview

TCGA (2006–2018) is one of the largest and most comprehensive cancer genomics programs. It provided foundational multi-omics profiles including whole-genome/exome sequencing, RNA-seq, miRNA-seq, DNA methylation, copy number variation, and reverse-phase protein array (RPPA) proteomics for 33 cancer types. The data is publicly accessible through the Genomic Data Commons (GDC).

## Statistics

- **Samples**: >20,000 primary tumor and matched-normal samples in the overall program; not 20,000 matched pairs (NCI overview, checked 2026-10-20)
- **Cancer Types**: 33 (e.g., BRCA, LUAD, COAD, GBM, PRAD)
- **Data Types**: WGS/WES, RNA-seq, miRNA-seq, methylation, CNV, RPPA proteomics, clinical
- **Species**: Human

## Access

**Portal**: https://portal.gdc.cancer.gov/
**Data documentation**: https://docs.gdc.cancer.gov/

## Application in SCP

TCGA-derived bulk data contribute to RNA–protein modeling studies. The scTranslator total of 18,227 patient-level bulk samples across 31 cancer types refers to its multi-source assembled corpus, not TCGA alone. Dataset inclusion, RNA/protein pairing and training splits require the original study supplement.

## Key Publications

> [!cite] Primary Reference
> The Cancer Genome Atlas Research Network (2013) *Nature Genetics* 45, 1113–1120
> DOI: [10.1038/ng.2764](https://doi.org/10.1038/ng.2764)

## Related Resources

- [[CPTAC]] — Proteogenomic characterization complementing TCGA tumors
- [[MSKCC]] — Clinical genomics resource

## Sources

- [NCI TCGA overview](https://www.cancer.gov/ccg/research/genome-sequencing/tcga)
- [TCGA pan-cancer analysis project](https://doi.org/10.1038/ng.2764)
- [scTranslator official repository](https://github.com/TencentAILabHealthcare/sctranslator)
