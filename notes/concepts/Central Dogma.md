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
url: https://doi.org/10.1038/227561a0
---

# Central Dogma

**The central dogma describes constraints on the transfer of sequence information, not a universal one-way path or a quantitative law relating RNA and protein abundance.**

## Overview

The central dogma concerns transfer of biological sequence information: information transferred into protein does not flow back from protein into nucleic acid or into another protein sequence. DNA → RNA → protein is a common route, but reverse transcription and RNA replication are compatible with the dogma. It does not assert that RNA abundance quantitatively determines protein abundance.

## Relevance to SCP

RNA-to-protein prediction models such as **scTranslator** estimate a statistical relationship. Several processes can decouple mRNA and protein abundance:

- **Post-transcriptional regulation**: miRNA silencing, RNA stability, alternative splicing
- **Translational regulation**: Ribosome occupancy, codon usage, initiation factors
- **Post-translational modification**: Phosphorylation, ubiquitination, protein degradation rates
- **Temporal dynamics**: mRNA and protein half-lives differ substantially

These processes motivate explicit evaluation of predictive models. The central dogma does not establish that deep learning is necessary or that it will outperform simpler models.

## Related Concepts

- [[Transfer Learning]] — ML strategy used to learn this biological relationship at scale
- [[CITE-seq]] — Experimental method providing paired RNA-protein ground truth

## Sources

- [Crick (1970), Central dogma of molecular biology](https://doi.org/10.1038/227561a0)
