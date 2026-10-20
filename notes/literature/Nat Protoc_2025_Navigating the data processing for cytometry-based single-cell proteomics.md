---
title: Navigating the data processing for cytometry-based single-cell proteomics
authors:
  - Huaicheng Sun
  - Yuan Zhou
  - Ruoyu Jiang
  - Yuxuan Liu
  - Chengbin Gu
  - Ziqi Pan
  - Minjie Mou
  - Xichen Lian
  - Bohan Chen
  - Tianle Niu
  - Ying Zhang
  - Yintao Zhang
  - Baoliang Zhang
  - Xiuna Sun
  - Hao Yang
  - Xin Shen
  - Yangbo Dai
  - Jiannan Deng
  - Siqi Liu
  - Yang Zhang
  - Mang Xiao
  - Wanqing Xie
  - Qingxia Yang
  - Tingting Fu
  - Feng Zhu
aliases:
   - ANPELA
   - Single-cell proteomics data processing
tags:
  - literature
  - paper
  - SCP
  - Proteomics
  - Cytometry
category: literature
date_created: 2024-05-23
Journal: Nature Protocols
Year: 2026
DOI: 10.1038/s41596-025-01257-2
doi: "10.1038/s41596-025-01257-2"
url: "https://doi.org/10.1038/s41596-025-01257-2"
publication_status: "published"
published_online: "2025-10-16"
published_print: "2026-03"
---

# Navigating the data processing for cytometry-based single-cell proteomics

> [!info] Verification scope — 2026-10-20
> Bibliographic metadata and the public abstract were checked. This does not verify every experimental detail, figure, parameter or performance claim in the full note.
> See the [per-note audit record](../../audit/literature-audit.json) for evidence and unresolved items.

## Citation

> [!cite] Reference
> **Title**: Navigating the data processing for cytometry-based single-cell proteomics
> **Authors**: Huaicheng Sun, Yuan Zhou, Ruoyu Jiang, et al.
> **Year**: 2026 (volume year; online 2025-10-16)
> **Journal**: Nature Protocols
> **DOI**: [10.1038/s41596-025-01257-2](https://doi.org/10.1038/s41596-025-01257-2)
## Abstract

Cytometry-based single-cell proteomics (SCP) has become an important technology for understanding complex biological systems. Although many methods have been developed to process these data, identifying the best-performing workflow for a particular dataset remains challenging. This study developed **ANPELA**, a ready-to-use approach that guides proteomics data processing through large-scale screening. It uses machine learning to systematically evaluate thousands of processing workflows for cell subpopulation identification (CSI) and pseudotime trajectory inference (PTI). ANPELA is available as desktop software, an R package and an online server, providing options for different use settings, data security and a user-friendly interface. It is intended for a broad audience, including users without programming experience, to help researchers obtain reliable biological insights from SCP studies.

## Key Points

- **Guidance through large-scale screening**: ANPELA can automatically generate and screen more than 3,000 combinations of data-processing workflows spanning four key steps: compensation, transformation, normalization and signal cleaning.
- **Multidimensional evaluation**: Comprehensive evaluation frameworks were established for CSI and PTI, incorporating metrics such as accuracy, tightness, robustness and correspondence.
- **Deployment options and security**: The tool provides a desktop GUI requiring no programming experience, an online Web interface and an open-source R package supporting parallel computing. Local execution protects the security of users' private data.

## Methods

### Experimental Design and Data Preparation

- **Input data**: Flow Cytometry Standard (FCS) files and metadata (`metadata.csv`) are required. CSI analysis requires at least two experimental conditions, and PTI analysis requires at least two time points.
- **Benchmark datasets**: Validation used 10 representative cytometry-based SCP datasets spanning different detection technologies, such as TOF, APD and PMT, and study types.
- **Cell-count requirements**: At least 200 cells per FCS file are recommended to ensure reliable evaluation, particularly of robustness.

### Data Analysis and Workflow Screening

- **Software**: ANPELA (Web/Desktop/R package).
- **Processing steps**:
    1. **Data compensation**: Seven methods, including AutoSpill and FlowCore.
    2. **Data transformation**: Sixteen methods, including Arcsinh and Logicle.
    3. **Data normalization**: Seven methods, including GaussNorm and WarpSet.
    4. **Signal cleaning**: Five methods, including FlowAI and FlowClean.
- **Performance metrics**:
    - **CSI**: Accuracy (AUC), Tightness (silhouette coefficient), Robustness and Correspondence.
    - **PTI**: Conformance (time conformance score), Smoothness, Robustness and Correspondence.
- **Downstream analysis methods**: Options include FlowSOM and PhenoGraph for CSI, and Slingshot and SCORPIUS for PTI.

## Results

### Main Findings

1. **Dataset-dependent workflow performance**: A workflow that performs well on one dataset may perform poorly on another, demonstrating the need to select workflows for the specific study.
2. **CSI optimization**: The top-ranked workflow selected by ANPELA, such as `NON+LGT+MEA+FCU`, can significantly reduce cell-classification error compared with lower-ranked workflows or default methods. In the reported example, the error rate decreased from 22.2% to 16.4%.
3. **PTI trajectory reconstruction**: The best-performing workflow can accurately reconstruct the complex differentiation trajectories of mouse embryonic stem cells into three germ layers. Poor-performing workflows may completely obscure the biological context and even lead to incorrect biological conclusions.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | **ANPELA architecture**: The complete workflow from raw-data input and screening combinations of four processing steps to the final CSI and PTI performance evaluation. |
| Fig 2 | **Protocol overview**: Comparison of the steps and expected timings for GUI-based Procedure 1 and R-package-based Procedure 2. |
| Fig 3 | **Multicriteria performance evaluation**: The evaluation logic for CSI dimensions, including accuracy and tightness, and PTI dimensions, including conformance and smoothness. |
| Fig 4 | **CSI case study**: Dimensionality-reduction plots and Sankey diagrams show differences among workflows of different ranks in identifying PBMC subpopulations. |
| Fig 5 | **PTI case study**: Differences among workflows in the accuracy of reconstructing mESC differentiation paths. |

## Discussion

### Strengths

- **Comprehensiveness**: Currently the only tool covering the full process from preprocessing to evaluation while offering screening of more than 3,000 workflows.
- **Ease of use**: The GUI substantially lowers the barrier to use for biologists and clinicians, while the R package provides flexibility for data scientists.
- **Transparency**: All code is open source, and the evaluation metrics are based on established, published algorithms, supporting reproducible and interpretable results.

### Limitations

- **Computational time**: Screening thousands of workflows may take tens of minutes to several hours, depending on data volume and hardware.
- **System restrictions**: The desktop version currently supports only Windows.
- **Potential bias**: Some evaluation metrics, such as Ca accuracy, may be biased when detecting very subtle phenotypic differences and require interpretation in the biological context.

### Future Work

- **Extension to other fields**: Planned extensions of the ANPELA methodology include spatial proteomics and other emerging high-dimensional data domains.
- **Algorithm updates**: Continued integration of newly developed preprocessing algorithms and downstream analysis tools is intended to keep the protocol current.

## Personal Notes

- The protocol emphasizes the importance of dataset dependence in single-cell data preprocessing: there is no universally optimal processing method.
- ANPELA shifts workflow selection from unguided trial and error toward choices informed by quantitative evaluation.

## Related Papers

- Zhang, Y. et al. *Adv. Sci.* **10**, e2207061 (2023). (Earlier ANPELA version and performance benchmarks)
- Van Gassen, S. et al. *Cytom. A* **87**, 636–645 (2015). (FlowSOM algorithm)
- Ji, Z. & Ji, H. *Nucleic Acids Res.* **44**, e117 (2016). (Related to TSCAN/PTI)
