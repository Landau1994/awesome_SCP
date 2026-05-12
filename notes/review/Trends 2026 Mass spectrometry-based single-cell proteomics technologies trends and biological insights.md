---
title: Mass spectrometry-based single-cell proteomics technologies, trends, and biological insights
authors:
  - Rui Hu
  - Christian Montes
  - Justin W. Walley
aliases:
  - 
tags:
  - literature
  - paper
  - single-cell-proteomics
  - mass-spectrometry
  - multi-omics
category: literature
date_created: 2025-05-12
Journal: Trends in Biochemical Sciences
Year: 2026
---

# Mass spectrometry-based single-cell proteomics technologies, trends, and biological insights

## Citation

> [!cite] Reference
> **Title**: Mass spectrometry-based single-cell proteomics technologies, trends, and biological insights
> **Authors**: Rui Hu, Christian Montes, Justin W. Walley
> **Year**: 2026
> **Journal**: Trends in Biochemical Sciences
> **DOI**: 10.1016/j.tibs.2026.04.011

## Abstract

Single-cell proteomics (SCP) has emerged as a transformative approach for characterizing cellular heterogeneity at the protein level. Recent advances in mass spectrometry workflows, with improvements spanning sample preparation, peptide separation, data acquisition, and data interpretation, have enabled unprecedented proteome depth and throughput at single-cell resolution. Beyond technological innovations, SCP is now addressing complex biological questions in oncology, developmental biology, and neuroscience, revealing dynamic cellular states and regulatory mechanisms. Integration with other single-cell omics is bridging the gap between genotype–phenotype relationships and uncovering multilayered regulation. In this review, we summarize recent progress in SCP technologies and highlight emerging applications and integrative strategies that mark a transition from technological development to broad biological understanding.

## Key Points

- Driven by recent technological progress, mass spectrometry-based single-cell proteomics can now robustly profile cellular heterogeneity to resolve fundamental biological questions.
- A variety of experimental strategies, including novel sample preparation workflows, faster liquid chromatography, and advanced data acquisition methods (e.g., DIA, plexDIA, and novel mass analyzers like Astral), are enhancing analytical power.
- Single-cell proteomics is emerging as a critical component in multi-omics integration, providing essential functional insights and overcoming the discordance often observed between mRNA and protein levels.

## Methods

### Sample Preparation
- Method used: Review of multiple techniques including [[FACS]], [[cellenONE]], microfluidics, [[SCoPE]], [[isobaric labeling]] (e.g., [[TMTpro]]), and label-free approaches (e.g., droplet-based and plate-based digestion).
- Cell type: N/A (Review covering various types, e.g., HeLa, hepatocytes, mouse oocytes, human motor neurons).
- Number of cells: N/A (Discusses throughput capabilities of >500 cells per day).

### Data Analysis
- Software: Review covers traditional tools like [[MaxQuant]], [[DIA-NN]], [[FragPipe]], [[Spectronaut]], and [[Proteome Discoverer]], as well as SCP-specific packages like [[scp]], [[scPROTEIN]], and [[SCPline]].
- Downstream: Missing value imputation (e.g., [[DART-ID]], PIMMS), batch effect correction, spectral clustering, and cell-size normalization.

## Results

### Main Findings
1. Proteome coverage has increased dramatically, with cutting-edge setups (such as the Orbitrap Astral or timsTOF Ultra 2) now able to profile over 5,000 protein groups from a single cell.
2. Advanced data acquisition strategies, transitioning from standard DDA to [[DIA]], narrow-window DIA ([[nDIA]]), and multiplexed DIA ([[plexDIA]]), have significantly improved identification consistency and reduced missing values in low-input samples.
3. SCP has matured past technological benchmarking into direct biological application, enabling spatial mapping of tissue microenvironments, analysis of protein turnover dynamics, and the precise study of rare or precious cells in developmental biology and oncology.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | General workflow of mass spectrometry (MS)-based single-cell proteomics (SCP), detailing single cell isolation, enzymatic digestion, LC separation, and MS acquisition/data interpretation. |
| Fig 2 | Common data acquisition methods in SCP, illustrating the mechanisms of DDA, DIA, WWA, plexDIA, prioritized DDA, and nDIA. |
| Fig 3 | Single-cell multiomic integration, showcasing how parallel or nonparallel measurements of chromatin, mRNA, proteins, and metabolites are combined for predictive regulatory networking and pathway reconstruction. |

## Discussion

### Strengths
- Enables direct measurement of functional phenotypes and dynamic states (e.g., protein turnover) that cannot be accurately inferred from transcriptomics alone.
- Uncovers complex cellular heterogeneity and signaling dynamics previously obscured by the averaging effects of bulk proteomics.

### Limitations
- The high cost of LC and MS instrumentation currently restricts the widespread adoption and scaling of SCP to the same degree as scRNA-seq.
- Cell size variability dictates total protein abundance and significantly complicates data normalization.
- Significant computational challenges remain regarding handling complex data structures, severe batch effects, and high rates of missing values.

### Future Work
- Streamlining workflows to significantly lower the per-sample cost and increase instrument throughput.
- Developing more intuitive, user-friendly software packages that require less specialized programming expertise.
- Moving beyond descriptive multi-omics to mechanistically identify post-transcriptional regulatory hubs driving biological processes.

## Personal Notes



## Related Papers

- Budnik, B. et al. (2018) SCoPE-MS: mass spectrometry of single mammalian cells quantifies proteome heterogeneity during cell differentiation. Genome Biol. 19, 161.
- Bubis, J.A. et al. (2025) Challenging the Astral mass analyzer to quantify up to 5,300 proteins per single cell at unseen accuracy to uncover cellular heterogeneity. Nat. Methods 22, 510–519.
- Specht, H. et al. (2021) Single-cell proteomic and transcriptomic analysis of macrophage heterogeneity using SCoPE2. Genome Biol. 22, 50.