---
title: CITE-seq
aliases:
  - Cellular Indexing of Transcriptomes and Epitopes by Sequencing
tags:
  - methods
  - multi-omics
  - single-cell
category: method
url: https://doi.org/10.1038/nmeth.4380
date_created: 2026-01-19
---

# CITE-seq

**Cellular Indexing of Transcriptomes and Epitopes by Sequencing — a widely adopted single-cell multi-omics method that simultaneously measures surface protein expression and mRNA transcriptome using DNA-barcoded antibodies and droplet-based sequencing.**

## Overview

CITE-seq was developed by Stoeckius et al. (2017) at the New York Genome Center. Cells are stained with antibodies conjugated to unique DNA oligonucleotide tags (Antibody-Derived Tags, ADTs). After droplet-based single-cell capture (e.g., 10x Genomics), both mRNA and ADT sequences are captured and sequenced, providing paired protein and RNA measurements for each cell. CITE-seq data serves as the primary training data for transcriptome-to-proteome translation models such as scTranslator, [[sciPENN]], [[totalVI]], and [[cTP-net]].

## Key Features

- **Dual Readout**: mRNA transcriptome + surface protein abundance per cell
- **DNA-Barcoded Antibodies**: Antibodies conjugated to unique oligo tags via streptavidin chemistry
- **Platform Compatibility**: Works with 10x Genomics, Drop-seq, and other droplet platforms
- **Scalable Protein Panels**: TotalSeq panels from BioLegend with >200 antibodies available

## Workflow

```
Antibody-DNA conjugation → Cell surface staining → Washing →
Droplet encapsulation → Cell lysis & mRNA capture →
Reverse transcription → cDNA amplification →
Separate RNA & ADT libraries → Sequencing → Joint analysis
```

## Performance

- **Proteins per cell**: Routinely 100–250+ surface proteins (TotalSeq panels)
- **Throughput**: 1,000–50,000+ cells per experiment
- **Data completeness**: Near-complete for targeted protein panel; genome-wide for RNA

## Advantages

- Simultaneous protein and RNA from the same single cell
- Leverages existing droplet-based scRNA-seq infrastructure
- Growing commercial antibody panel availability (BioLegend TotalSeq)
- Well-established analysis pipelines ([[Seurat]] WNN, [[totalVI]])

## Limitations

- Limited to surface and extracellular epitopes (antibody-accessible)
- Non-specific antibody binding generates background noise
- Cost scales with antibody panel size
- Cannot measure intracellular proteins (see [[NEAT-seq]] for nuclear proteins)

## Key Publications

> [!cite] Primary Reference
> Stoeckius M, Hafemeister C, Stephenson W, et al. (2017) *Nature Methods* 14, 865–868
> DOI: [10.1038/nmeth.4380](https://doi.org/10.1038/nmeth.4380)

## Related Methods

- [[REAP-seq]] — Conceptually similar; different conjugation chemistry (published same year)
- [[ECCITE-seq]] — Extended CITE-seq with CRISPR guide and hashtag detection
- [[Perturb-CITE-seq]] — Combines CRISPR perturbation screening with CITE-seq
- [[NEAT-seq]] — Extends to intranuclear proteins + chromatin accessibility
- [[Spatial CITE-seq]] — Adds spatial resolution to CITE-seq
