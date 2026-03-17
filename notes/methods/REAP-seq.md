---
title: REAP-seq
aliases:
  - RNA Expression and Protein Sequencing
tags:
  - methods
  - multi-omics
  - single-cell
category: method
url: https://doi.org/10.1038/nbt.3973
date_created: 2026-03-17
---

# REAP-seq

**RNA Expression and Protein Sequencing assay — a single-cell multi-omics method for simultaneous measurement of mRNA transcriptome and protein epitopes using DNA-barcoded antibodies.**

## Overview

REAP-seq (RNA Expression And Protein sequencing) was developed by Peterson et al. (2017) at the New York Genome Center. It enables simultaneous measurement of protein and RNA expression in single cells by conjugating DNA-barcoded antibodies to cell surface proteins, followed by droplet-based single-cell sequencing. It is conceptually similar to [[CITE-seq]], both published in the same year, but uses a different antibody-DNA conjugation chemistry.

## Key Features

- **Dual Readout**: Simultaneous capture of mRNA transcriptome and surface protein abundance from the same single cell
- **DNA-Barcoded Antibodies**: Antibodies conjugated to unique DNA tags via a streptavidin-biotin linkage
- **Droplet Compatibility**: Compatible with droplet-based single-cell platforms (10x Genomics, Drop-seq)

## Workflow

```
Antibody-DNA conjugation → Cell staining → Droplet encapsulation →
Lysis & RT → cDNA + ADT library prep → Sequencing → Deconvolution
```

## Performance

- **Proteins per cell**: Up to 82 proteins demonstrated
- **Throughput**: Thousands of cells per experiment
- **Data completeness**: High for targeted protein panel; genome-wide for RNA

## Advantages

- Simultaneous RNA and protein measurement at single-cell resolution
- Leverages existing droplet-based scRNA-seq platforms
- No additional specialized instrumentation required

## Limitations

- Limited to surface proteins (antibody-accessible epitopes)
- Protein panel size limited by antibody availability and cross-reactivity
- Background noise from non-specific antibody binding

## Key Publications

> [!cite] Primary Reference
> Peterson VM, Zhang KX, Kumar N, et al. (2017) *Nature Biotechnology* 35, 936–939
> DOI: [10.1038/nbt.3973](https://doi.org/10.1038/nbt.3973)

## Related Methods

- [[CITE-seq]] — Conceptually similar; uses different conjugation chemistry
- [[ECCITE-seq]] — Extended version supporting CRISPR guide detection
- [[Perturb-CITE-seq]] — Combines perturbation screening with CITE-seq
