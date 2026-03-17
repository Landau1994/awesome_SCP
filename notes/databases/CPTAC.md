---
title: CPTAC
aliases:
  - Clinical Proteomic Tumor Analysis Consortium
tags:
  - database
  - resource
  - cancer
  - proteomics
  - proteogenomics
category: database
url: https://proteomics.cancer.gov/programs/cptac
date_created: 2026-03-17
---

# CPTAC

**Clinical Proteomic Tumor Analysis Consortium — an NCI program that performs comprehensive proteogenomic characterization of major cancer types, providing paired genomic, transcriptomic, and deep proteomic/phosphoproteomic data on TCGA-characterized tumors and beyond.**

## Overview

CPTAC extends [[TCGA]]'s genomic analyses with deep mass-spectrometry-based proteomics and phosphoproteomics. By generating quantitative protein-level data alongside matched genomic and transcriptomic profiles, CPTAC enables the study of how genomic alterations translate into functional protein changes in cancer. The data is publicly available through the Proteomic Data Commons (PDC).

## Statistics

- **Cancer Types**: >10 (breast, ovarian, colon, lung, pancreas, brain, kidney, head/neck, etc.)
- **Data Types**: TMT-based quantitative proteomics, phosphoproteomics, acetylproteomics, glycoproteomics, WGS/WES, RNA-seq, methylation
- **Samples**: Hundreds of tumor + matched normal per cancer type
- **Species**: Human

## Access

**Portal**: https://pdc.cancer.gov/
**CPTAC Data Portal**: https://cptac-data-portal.georgetown.edu/

## Application in SCP

In scTranslator, CPTAC bulk RNA-protein paired data contributed to the Stage 1 pre-training corpus alongside [[TCGA]], [[MSKCC]], and Broad Institute datasets for learning RNA-to-protein translation patterns.

## Key Publications

> [!cite] Primary Reference
> Edwards NJ, Oberti M, Thangudu RR, et al. (2015) *Journal of Proteome Research* 14, 2707–2713
> DOI: [10.1021/acs.jproteome.5b00056](https://doi.org/10.1021/acs.jproteome.5b00056)

## Related Resources

- [[TCGA]] — Genomic characterization program; CPTAC adds proteomics to TCGA tumors
- [[MSKCC]] — Clinical genomics resource
