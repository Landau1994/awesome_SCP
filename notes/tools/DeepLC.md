---
title: DeepLC
aliases:
  - DeepLC
tags:
  - tools
  - software
category: tool
url: https://github.com/compomics/DeepLC
date_created: 2026-03-25
---

# DeepLC

**A deep-learning tool for peptide retention time prediction in LC-MS workflows.**

## Overview

DeepLC predicts peptide retention times to improve identification confidence, library construction, and rescoring workflows.

## Key Features

- **Retention Time Prediction**: Improves alignment and confidence.
- **ML-Driven Calibration**: Adapts to specific LC setups.
- **Workflow Integration**: Useful in both DDA and DIA pipelines.
- **Environment**: Follow the official release requirements; operating-system support depends on the package and its dependencies.

## Input/Output

**Input:**

- Peptide sequences/modifications
- Calibration peptides (optional)

**Output:**

- Predicted retention times
- RT features for downstream scoring

## Key Publications

> [!cite] Primary Reference
> Bouwmeester et al. (2021). DeepLC can predict retention times for peptides that carry as-yet unseen modifications. *Nature Methods*.
> DOI: [10.1038/s41592-021-01301-5](https://doi.org/10.1038/s41592-021-01301-5)

## Links

- GitHub: https://github.com/compomics/DeepLC
- Documentation/source: https://github.com/compomics/DeepLC

## Related Tools

- [[AlphaPeptDeep]]
- [[Prosit]]
- [[Percolator]]

## Source Check

- Source checked on 2026-10-20: [DeepLC documentation or source](https://github.com/compomics/DeepLC).
