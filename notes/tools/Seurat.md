---
title: Seurat
aliases:
  - Seurat v5
  - Seurat R package
tags:
  - tools
  - software
  - single-cell
  - R
  - multi-omics
category: tool
url: https://satijalab.org/seurat/
date_created: 2026-01-18
---

# Seurat

**A comprehensive R toolkit for single-cell genomics analysis, supporting QC, normalization, dimensionality reduction, clustering, visualization, and multi-modal integration (Weighted Nearest Neighbor analysis for CITE-seq data).**

## Overview

Seurat (Hao, Hao et al., Satija Lab) is one of the most widely used single-cell analysis frameworks. It supports the complete single-cell analysis workflow from raw counts to biological interpretation. Seurat v4/v5 introduced Weighted Nearest Neighbor (WNN) analysis for integrating multiple data modalities (e.g., RNA + protein from [[CITE-seq]]), making it a standard tool for multi-omics single-cell data.

## Key Features

- **Standard scRNA-seq Pipeline**: QC, normalization (SCTransform), PCA, UMAP, clustering, DE testing
- **Multi-Modal Integration**: WNN for joint RNA + protein (CITE-seq) analysis
- **Dataset Integration**: CCA, RPCA, and Harmony-based batch correction
- **Spatial Analysis**: Support for Visium, MERFISH, and other [[Spatial Transcriptomics]] data
- **Scalable**: BPCells backend for on-disk analysis of millions of cells (v5)

## Installation

```r
install.packages("Seurat")
# or development version
remotes::install_github("satijalab/seurat", "seurat5")
```

## Usage

```r
library(Seurat)
obj <- CreateSeuratObject(counts = counts_matrix)
obj <- NormalizeData(obj) |> FindVariableFeatures() |> ScaleData() |> RunPCA()
obj <- FindNeighbors(obj) |> FindClusters() |> RunUMAP()
DimPlot(obj, group.by = "seurat_clusters")
```

## Key Publications

> [!cite] Seurat v4 (WNN)
> Hao Y, Hao S, Andersen-Nissen E, et al. (2021) *Cell* 184, 3573–3587
> DOI: [10.1016/j.cell.2021.04.048](https://doi.org/10.1016/j.cell.2021.04.048)

> [!cite] Seurat v3 (Integration)
> Stuart T, Butler A, Hoffman P, et al. (2019) *Cell* 177, 1888–1902
> DOI: [10.1016/j.cell.2019.05.031](https://doi.org/10.1016/j.cell.2019.05.031)

## Links

- Website: https://satijalab.org/seurat/
- GitHub: https://github.com/satijalab/seurat

## Related Tools

- [[scp Package]] — Bioconductor package specifically for single-cell proteomics
- [[totalVI]] — Deep learning alternative for CITE-seq integration
- [[sciPENN]] — Neural network for protein imputation
- [[DIA-NN]] — MS-based proteomics search engine (different domain)
