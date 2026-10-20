---
title: DIA-Umpire
aliases:
  - DIA-Umpire
tags:
  - tools
  - software
category: tool
url: https://github.com/Nesvilab/DIA-Umpire
date_created: 2026-03-25
---

# DIA-Umpire

**Software for converting DIA data into pseudo-MS/MS features for identification workflows.**

## Overview

DIA-Umpire deconvolutes DIA data into precursor-fragment groups, enabling peptide identification with DDA-style search engines.

## Key Features

- **Pseudo-Spectra Generation**: Converts DIA to pseudo-MS/MS data.
- **Compatibility Layer**: Bridges DIA data with conventional search workflows.
- **Feature Extraction**: Supports peptide-centric and signal-centric processing.
- **Environment**: Follow the official release requirements; operating-system support depends on the package and its dependencies.

## Input/Output

**Input:**

- DIA spectra converted to the supported mzXML input format and signal-extraction settings
- A sequence database for the subsequent search-engine step

**Output:**

- Pseudo-MS/MS spectra and precursor-fragment groups
- Identification/quantification results after the documented downstream search steps

## Key Publications

> [!cite] Project Documentation
> Official project/source documentation: https://github.com/Nesvilab/DIA-Umpire

## Links

- GitHub: https://github.com/Nesvilab/DIA-Umpire
- Documentation/source: https://github.com/Nesvilab/DIA-Umpire

## Related Tools

- [[DIA-NN]]
- [[OpenSpec]]
- [[Spectronaut]]

## Source Check

- Source checked on 2026-10-20: [DIA-Umpire documentation or source](https://github.com/Nesvilab/DIA-Umpire).
