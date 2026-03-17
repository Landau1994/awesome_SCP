---
title: Central Dogma
aliases:
  - Central Dogma of Molecular Biology
tags:
  - concept
  - biology
  - molecular-biology
category: concept
date_created: 2026-03-17
---

# Central Dogma

**The central dogma of molecular biology describes the flow of genetic information: DNA → RNA → Protein. This unidirectional information transfer is the biological foundation for computational methods that predict protein abundance from transcriptomic data.**

## Overview

Proposed by Francis Crick in 1958, the central dogma states that sequence information flows from nucleic acids to proteins but not in reverse. In practice:

1. **Transcription**: DNA → mRNA (in the nucleus)
2. **Translation**: mRNA → Protein (at ribosomes)

While there are exceptions (reverse transcription, RNA replication), the general DNA → RNA → Protein flow holds for protein-coding genes.

## Relevance to SCP

The central dogma provides the theoretical basis for transcriptome-to-proteome translation models like **scTranslator**. However, the relationship between mRNA and protein levels is not perfectly linear due to:

- **Post-transcriptional regulation**: miRNA silencing, RNA stability, alternative splicing
- **Translational regulation**: Ribosome occupancy, codon usage, initiation factors
- **Post-translational modification**: Phosphorylation, ubiquitination, protein degradation rates
- **Temporal dynamics**: mRNA and protein half-lives differ substantially

These complexities are why deep learning models (rather than simple linear regression) are needed to capture the mRNA-protein relationship at single-cell resolution.

## Related Concepts

- [[Transfer Learning]] — ML strategy used to learn this biological relationship at scale
- [[CITE-seq]] — Experimental method providing paired RNA-protein ground truth
