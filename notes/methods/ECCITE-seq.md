---
title: ECCITE-seq
aliases:
  - Expanded CRISPR-compatible CITE-seq
tags:
  - methods
  - multi-omics
  - single-cell
  - CRISPR
category: method
url: https://doi.org/10.1038/s41592-019-0392-0
date_created: 2026-03-17
---

# ECCITE-seq

**Expanded CRISPR-compatible Cellular Indexing of Transcriptomes and Epitopes by Sequencing — a multi-modal single-cell method that simultaneously captures transcriptome, surface proteins, sample identity (hashtag), and CRISPR sgRNA in the same cell.**

## Overview

ECCITE-seq was developed by Mimitou et al. (2019) as an extension of [[CITE-seq]]. It adds the ability to detect CRISPR single-guide RNAs (sgRNAs) alongside protein and RNA measurements, enabling functional genomics screens at multi-omics resolution. It also supports cell hashing for sample multiplexing.

## Key Features

- **Five-Modal Readout**: Transcriptome, surface protein, sgRNA, cell hashtag, and TCR/BCR in a single experiment
- **CRISPR Compatibility**: Direct capture of sgRNA sequences for perturbation assignment
- **Sample Multiplexing**: Hashtag antibodies enable pooling of multiple samples

## Workflow

```
CRISPR transduction → Cell hashing → Antibody staining →
Droplet capture → Library prep (RNA + ADT + sgRNA + HTO) →
Sequencing → Demultiplexing → Multi-modal analysis
```

## Advantages

- Most comprehensive single-cell multi-modal readout available
- Enables pooled perturbation screens with protein-level readout
- Sample multiplexing reduces batch effects and cost

## Limitations

- Complex library preparation with multiple modalities
- sgRNA detection efficiency can vary
- Surface protein panel size still limited by antibody availability

## Key Publications

> [!cite] Primary Reference
> Mimitou EP, Cheng A, Montalbano A, et al. (2019) *Nature Methods* 16, 409–412
> DOI: [10.1038/s41592-019-0392-0](https://doi.org/10.1038/s41592-019-0392-0)

## Related Methods

- [[CITE-seq]] — Surface protein + RNA; ECCITE-seq extends with CRISPR and hashing
- [[Perturb-CITE-seq]] — Similar perturbation + multi-omics approach
- [[REAP-seq]] — Alternative protein + RNA method
