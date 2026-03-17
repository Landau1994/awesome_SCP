---
title: NEAT-seq
aliases:
  - Sequencing of Nuclear protein Epitope, chromatin Accessibility and the Transcriptome
tags:
  - methods
  - multi-omics
  - single-cell
  - epigenomics
category: method
url: https://doi.org/10.1038/s41592-022-01461-y
date_created: 2026-03-17
---

# NEAT-seq

**Sequencing of Nuclear protein Epitope, chromatin Accessibility and the Transcriptome in single cells — a tri-modal single-cell method integrating nuclear protein quantification, chromatin accessibility, and gene expression.**

## Overview

NEAT-seq was developed by Chen AF, Parks B, et al. (2022) to enable simultaneous profiling of three modalities in single cells: intranuclear protein levels (via antibody-derived tags), chromatin accessibility (via ATAC-seq), and gene expression (via RNA-seq). This extends multi-omics beyond surface proteins to nuclear regulators such as transcription factors, providing a more complete picture of gene regulation.

## Key Features

- **Tri-Modal**: Measures nuclear proteins, chromatin accessibility, and transcriptome simultaneously
- **Nuclear Protein Quantification**: Accesses intranuclear targets (e.g., transcription factors) unlike surface-only methods like [[CITE-seq]]
- **Regulatory Insight**: Links transcription factor abundance to chromatin state and gene expression

## Workflow

```
Nuclei isolation → Nuclear protein staining (DNA-barcoded antibodies) →
ATAC transposition → Droplet capture → Library prep (RNA + ATAC + Protein) →
Sequencing → Multi-modal integration
```

## Performance

- **Proteins**: Intranuclear targets (transcription factors, histone modifications)
- **Throughput**: Thousands of cells per experiment
- **Data completeness**: Three modalities from each single nucleus

## Advantages

- Access to intranuclear proteins beyond the surface epitope limitation
- Direct linking of transcription factor protein levels to chromatin and gene expression
- Compatible with 10x Multiome platform

## Limitations

- Requires nuclei isolation (loses cytoplasmic information)
- Nuclear protein antibody panel availability is more limited
- Complex library preparation with three modalities

## Key Publications

> [!cite] Primary Reference
> Chen AF, Parks B, Kathiria AS, et al. (2022) *Nature Methods* 19, 547–553
> DOI: [10.1038/s41592-022-01461-y](https://doi.org/10.1038/s41592-022-01461-y)

## Related Methods

- [[CITE-seq]] — Surface protein + RNA; NEAT-seq extends to nuclear proteins + ATAC
- [[Spatial CITE-seq]] — Spatial variant of protein + RNA multi-omics
- [[REAP-seq]] — Another surface protein + RNA multi-omics method
