---
title: CITE-seq
aliases:
  - Cellular Indexing of Transcriptomes and Epitopes by Sequencing
tags:
  - methods
  - multi-omics
  - single-cell
category: method
url: https://www.nature.com/articles/nmeth.4380
date_created: 2026-01-19
---

# CITE-seq

**Cellular Indexing of Transcriptomes and Epitopes by Sequencing — a widely adopted single-cell multi-omics method that simultaneously measures surface protein expression and mRNA transcriptome using DNA-barcoded antibodies and droplet-based sequencing.**

## Overview

CITE-seq was developed by Stoeckius et al. (2017) at the New York Genome Center. Cells are stained with antibodies conjugated to unique DNA oligonucleotide tags (Antibody-Derived Tags, ADTs). After droplet-based single-cell capture (e.g., 10x Genomics), both mRNA and ADT sequences are captured and sequenced, providing paired protein and RNA measurements for each cell. The paired RNA and antibody-derived measurements can support joint modeling, for example with [[totalVI]], [[sciPENN]] and [[cTP-net]]; individual models use different training data and assumptions.

## Key Features

- **Dual Readout**: mRNA transcriptome + surface protein abundance per cell
- **DNA-Barcoded Antibodies**: Antibodies conjugated to unique oligo tags via streptavidin chemistry
- **Platform Compatibility**: Works with 10x Genomics, Drop-seq, and other droplet platforms
- **Scalable Protein Panels**: Panel size depends on antibody availability, validation and the specific protocol.

## Workflow

```
Antibody-DNA conjugation → Cell surface staining → Washing →
Droplet encapsulation → Cell lysis & mRNA capture →
Reverse transcription → cDNA amplification →
Separate RNA & ADT libraries → Sequencing → Joint analysis
```

## Performance

- **Protein coverage**: Targeted antibody-panel coverage, not an untargeted whole-proteome measurement; panel size differs from proteins detected in each cell.
- **Throughput**: Depends on capture platform, loading, recovery and sequencing depth.
- **Data completeness**: Neither antibody nor RNA measurements are guaranteed complete; background and sampling must be evaluated.

## Advantages

- Simultaneous protein and RNA from the same single cell
- Leverages existing droplet-based scRNA-seq infrastructure
- Growing commercial antibody panel availability (BioLegend TotalSeq)
- Well-established analysis pipelines ([[Seurat]] WNN, [[totalVI]])

## Limitations

- Limited to surface and extracellular epitopes (antibody-accessible)
- Non-specific antibody binding generates background noise
- Cost scales with antibody panel size
- The original surface-staining protocol does not measure intracellular epitopes; related protocols such as [[NEAT-seq]] address nuclear proteins.

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

## Sources

- [Reference for CITE-seq](https://www.nature.com/articles/nmeth.4380)
