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
url: https://www.cancer.gov/tcga
date_created: 2026-03-17
---

# TCGA

**The Cancer Genome Atlas — a landmark NCI/NHGRI program that molecularly characterized over 20,000 primary cancer and matched normal samples spanning 33 cancer types, generating multi-omics data (genomics, transcriptomics, proteomics, epigenomics) freely available to the research community.**

## Overview

TCGA (2006–2018) is one of the largest and most comprehensive cancer genomics programs. It provided foundational multi-omics profiles including whole-genome/exome sequencing, RNA-seq, miRNA-seq, DNA methylation, copy number variation, and reverse-phase protein array (RPPA) proteomics for 33 cancer types. The data is publicly accessible through the Genomic Data Commons (GDC).

## Statistics

- **Samples**: >20,000 primary tumor + matched normal
- **Cancer Types**: 33 (e.g., BRCA, LUAD, COAD, GBM, PRAD)
- **Data Types**: WGS/WES, RNA-seq, miRNA-seq, methylation, CNV, RPPA proteomics, clinical
- **Species**: Human

## Access

**Portal**: https://portal.gdc.cancer.gov/
**Legacy Archive**: https://portal.gdc.cancer.gov/legacy-archive

## Application in SCP

In scTranslator, TCGA bulk RNA-protein paired data was used as part of the Stage 1 (bulk) pre-training corpus, providing 18,227 patient-level samples across 31 cancer types to learn general RNA-to-protein relationships.

## Key Publications

> [!cite] Primary Reference
> The Cancer Genome Atlas Research Network (2013) *Nature Genetics* 45, 1113–1120
> DOI: [10.1038/ng.2764](https://doi.org/10.1038/ng.2764)

## Related Resources

- [[CPTAC]] — Proteogenomic characterization complementing TCGA tumors
- [[MSKCC]] — Clinical genomics resource
