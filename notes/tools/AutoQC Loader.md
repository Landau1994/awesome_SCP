---
title: AutoQC Loader
aliases:
  - AutoQC Loader
tags:
  - tools
  - software
category: tool
url: https://pmc.ncbi.nlm.nih.gov/articles/PMC5406750/
date_created: 2026-03-25
---

# AutoQC Loader

**An automation utility for continuous QC data loading in targeted proteomics workflows.**

## Overview

AutoQC Loader is used with Skyline ecosystems to automatically ingest QC runs and monitor instrument performance over time.

## Key Features

- **Automated QC Ingestion**: Continuous import of QC files.
- **Trend Monitoring**: Tracks longitudinal performance metrics.
- **Workflow Integration**: Fits targeted assay operations.
- **Environment**: Follow the official release requirements; operating-system support depends on the package and its dependencies.

## Input/Output

**Input:**

- Newly acquired QC raw files in a watched folder
- A configured Skyline template document and a Panorama destination

**Output:**

- Skyline documents with imported QC results, uploaded to Panorama
- Longitudinal QC metrics/flags viewed through the Panorama QC dashboard

## Key Publications

> [!cite] Related Study Context
> See LFQ benchmark-related resource notes.

## Links

- Source availability: See the official source below; no separate public repository was confirmed.
- Documentation/source: https://pmc.ncbi.nlm.nih.gov/articles/PMC5406750/

## Related Tools

- [[Skyline]]
- [[Panorama Web]]
- [[ProteoBench]]

## Source Check

- Source checked on 2026-10-20: [AutoQC Loader documentation or source](https://pmc.ncbi.nlm.nih.gov/articles/PMC5406750/).
