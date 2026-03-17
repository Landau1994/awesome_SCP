---
title: Perturb-CITE-seq
aliases:
  - Perturb CITE-seq
tags:
  - methods
  - multi-omics
  - single-cell
  - perturbation
  - CRISPR
category: method
url: https://doi.org/10.1038/s41592-020-0837-5
date_created: 2026-03-17
---

# Perturb-CITE-seq

**A single-cell multi-modal perturbation screening method that combines CRISPR-based genetic perturbations with simultaneous measurement of RNA transcriptome and surface protein levels, enabling high-throughput mapping of gene function at multi-omics resolution.**

## Overview

Perturb-CITE-seq integrates CRISPR guide RNA detection, transcriptome profiling, and surface protein quantification in single cells. By assigning each cell a CRISPR perturbation identity alongside its RNA and protein readout, the method enables systematic dissection of gene regulatory effects on both transcriptomic and proteomic levels. It was developed by Frangieh et al. (2021) and is related to [[ECCITE-seq]].

## Key Features

- **Tri-Modal Readout**: CRISPR guide identity + RNA expression + surface protein levels per cell
- **Functional Genomics**: Maps causal gene-to-phenotype relationships at single-cell resolution
- **Scalability**: Pools many perturbations in a single experiment

## Workflow

```
CRISPR library transduction → Antibody staining (DNA-barcoded) →
Droplet capture → Library prep (RNA + ADT + guide) →
Sequencing → Perturbation assignment → Multi-modal analysis
```

## Performance

- **Perturbations**: Hundreds of gene knockouts per experiment
- **Throughput**: Thousands of cells per perturbation condition
- **Data completeness**: Three modalities per single cell

## Advantages

- Direct causal inference of gene function on protein and RNA levels
- Pooled screening reduces experimental cost and time
- Multi-omics readout captures post-transcriptional regulation

## Limitations

- Requires efficient CRISPR delivery and guide detection
- Surface protein panel size limited
- Incomplete perturbation (partial knockdown) can confound results

## Key Publications

> [!cite] Primary Reference
> Frangieh CJ, Melms JC, Thakore PI, et al. (2021) *Nature Genetics* 53, 332–341
> DOI: [10.1038/s41588-021-00779-1](https://doi.org/10.1038/s41588-021-00779-1)

> [!cite] Related
> Mimitou EP, Cheng A, Montalbano A, et al. (2019) *Nature Methods* 16, 409–412
> DOI: [10.1038/s41592-019-0392-0](https://doi.org/10.1038/s41592-019-0392-0)

## Related Methods

- [[CITE-seq]] — Protein + RNA without perturbation component
- [[ECCITE-seq]] — Extended CITE-seq with CRISPR guide capture
- [[REAP-seq]] — Alternative protein + RNA multi-omics
