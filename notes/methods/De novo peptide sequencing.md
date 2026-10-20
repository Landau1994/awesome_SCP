---
title: De novo peptide sequencing
aliases:
- de novo sequencing of peptides
tags:
- methods
category: method
url: https://www.nature.com/articles/s41467-024-49731-x
date_created: '2026-10-20'
---

# De novo peptide sequencing

## Overview

De novo peptide sequencing infers an amino-acid sequence from an MS/MS spectrum without requiring the peptide to be present in a searched sequence database. Algorithms may use fragmentation rules, optimization or learned models; Casanovo is a transformer-based example.

Incomplete fragmentation, modifications, noise and isobaric residues can create sequence ambiguity. Confidence calibration and validation remain necessary, and a predicted peptide sequence does not automatically identify its parent protein or proteoform.

## Reference

- *Sequence-to-sequence translation from mass spectra to peptides with a transformer model* (2024). [10.1038/s41467-024-49731-x](https://doi.org/10.1038/s41467-024-49731-x).

## Related Methods

- [[LC-MS-MS]]
- [[Open Search]]
- [[Spectral Deconvolution]]
- [[Transformer]]
