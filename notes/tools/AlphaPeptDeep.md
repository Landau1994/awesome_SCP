---
title: AlphaPeptDeep
aliases:
  - AlphaPeptDeep
tags:
  - tools
  - software
category: tool
url: https://github.com/MannLabs/alphapeptdeep
date_created: 2026-03-25
---

# AlphaPeptDeep

**A modular deep-learning framework for predicting peptide properties in proteomics.**

## Overview

AlphaPeptDeep provides model components for predicting fragmentation patterns, retention time, and other peptide properties to support DIA/DDA workflows.

## Key Features

- **Deep Learning Models**: Predicts MS-relevant peptide properties.
- **Modular Design**: Supports extensible model development.
- **Workflow Utility**: Useful for spectral library generation and rescoring.
- **Environment**: Follow the official release requirements; operating-system support depends on the package and its dependencies.

## Installation

The Python distribution is named `peptdeep`. Follow the [official repository installation instructions](https://github.com/MannLabs/alphapeptdeep) for the selected release and its dependencies.

## Input/Output

**Input:**

- Peptide sequences / modifications
- Training or calibration datasets

**Output:**

- Predicted spectra / RT / CCS
- Model-assisted identification support files

## Key Publications

> [!cite] Primary Reference
> Zeng et al. (2022). AlphaPeptDeep: a modular deep learning framework to predict peptide properties for proteomics. *Nature Communications* 13, 7238.
> DOI: [10.1038/s41467-022-34904-3](https://doi.org/10.1038/s41467-022-34904-3)

## Links

- GitHub: https://github.com/MannLabs/alphapeptdeep
- Documentation/source: https://github.com/MannLabs/alphapeptdeep

## Related Tools

- [[AlphaPept]]
- [[DIA-NN]]
- [[PyTorch]]

## Source Check

- Source checked on 2026-10-20: [AlphaPeptDeep documentation or source](https://github.com/MannLabs/alphapeptdeep).
- [Original AlphaPeptDeep article](https://www.nature.com/articles/s41467-022-34904-3).
