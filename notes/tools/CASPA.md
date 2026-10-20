---
title: CASPA
aliases:
  - CASPA
  - context-aware single-cell proteomics analysis
tags:
  - tools
  - software
category: tool
url: https://github.com/vonkriegsheim/CASPA
date_created: 2026-10-18
---

# CASPA

## Overview

CASPA is a context-aware single-cell proteomics analysis pipeline that leverages [[Large Language Models|LLMs]] to make context-aware decisions when processing and interpreting SCP data, implemented as a [[Snakemake]] workflow.

> [!cite] Primary Reference
> bioRxiv (2026)
> See [[bioRxiv 2026 A context aware single-cell proteomics analysis pipeline]]

## Related Tools

- [[Snakemake]]
- [[Scanpy]]
- [[scikit-learn]]
- [[scp Package]]

## Source Check

- Source checked on 2026-10-20: [CASPA documentation or source](https://github.com/vonkriegsheim/CASPA).

The repository accepts exported quantification/result tables (for example DIA-NN, FragPipe or Spectronaut exports). A Spectronaut “raw TSV” is a result table, not a vendor raw mass-spectrum file. The associated 2026 report is a preprint.
