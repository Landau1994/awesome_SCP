---
title: Single cell proteomic analysis defines discrete neutrophil functional states in human glioblastoma
aliases:
   - Single cell proteomic analysis of GBM neutrophils
   - Sadiku et al., 2025
tags:
  - literature
  - paper
  - proteomics
  - neutrophils
  - glioblastoma
  - single-cell
category: literature
date_created: 2025-11-28
Journal: Nature Communications
Year: 2025
---

# Single cell proteomic analysis defines discrete neutrophil functional states in human glioblastoma

## Citation

> [!cite] Reference
> **Title**：Single cell proteomic analysis defines discrete neutrophil functional states in human glioblastoma
> **Authors**: Pranvera Sadiku, Alejandro J. Brenes, Rupert L. Mayer, Leila Reyes, Patricia Coelho, Gabi van Stralen, Ailiang Zhang, Manuel A. Sanchez-Garcia, Emily R. Watts, Imran Liaquat, Andrew J. M. Howden, Ikeoluwa Adekoya, Anuka Boldbaatar, Allan MacRaild, Sarah Risbridger, Gillian M. Morrison, Heather MacPherson, Caroline M. Bruce, Shonna Johnston, Robert Grecian, Fiona A. Murphy, Steven M. Pollard, Paul M. Brennan, Karl Mechtler & Sarah R. Walmsley
> **Year**: 2025
> **Journal**: Nature Communications
> **DOI**: https://doi.org/10.1038/s41467-025-67367-3

## Abstract

Neutrophils are vital innate immune cells shown to infiltrate glioblastomas, however we currently lack the molecular understanding of their functional states within the tumour niche. Given that neutrophils are known to display a prominent discordance between mRNA and protein abundance, we develop ultra-sensitive mini-bulk and single cell proteomic (SCP) workflows to study the heterogeneity of peripheral blood and tumour associated neutrophils (TAN) from patients with glioblastoma. Mini-bulk analysis enable a deeper protein coverage of circulating immature, mature and TAN populations, defining signatures of maturity and demonstrating that TANs resemble mature circulating neutrophils. Analysis of the SCP data results in the detection of >1,100 proteins from a single TAN providing a detailed characterization of neutrophil subsets in glioblastoma. Our approach shows evidence of pathogenic and anti-tumorigenic clusters and discovers cell states invisible to scRNAseq, opening new opportunities to selectively target pro-tumoural neutrophil states.

## Key Points

- Development of ultra-sensitive mini-bulk (500 cells) and [[Single Cell Proteomics]] (SCP) workflows capable of identifying >1,100 proteins per single human neutrophil.
- Glioblastoma (GBM) Tumor Associated Neutrophils (TANs) largely resemble mature circulating neutrophils (CD10+) rather than immature ones, but possess a distinct mitochondrial phenotype.
- SCP revealed seven distinct neutrophil functional states within the tumor: armed, engaged, vital NETs, exhausted, lytic NETs, immunosuppressive & angiogenic, and vascular immature.
- The study highlights the divergence between neutrophil transcriptomes and proteomes, identifying functional states (like lytic NETosis and exhaustion) that are invisible to [[scRNAseq]].

## Methods

### Sample Preparation
- **Method used**: Fluorescence-activated cell sorting ([[FACS]]) followed by automated nanoliter liquid handling for lysis and digestion.
- **Cell type**: Human neutrophils (CD66b+, CD11b+, CD49d-, CD10+/-) from peripheral blood and Glioblastoma (GBM) tumor tissue.
- **Number of cells**: 
    - **Mini-bulk**: 500 cells per sample.
    - **SCP**: Single cells (1 cell per well).
- **Processing**: Sorted into 384-well plates, processed on [[cellenONE X1]], digested with trypsin.
- **Instrumentation**: Analyzed using [[Vanquish Neo UHPLC]] coupled to an [[Orbitrap Astral]] mass spectrometer equipped with a [[FAIMS Pro Duo]] interface.

### Data Analysis
- **Software**: [[Spectronaut]] (v19.7 for bulk/mini-bulk, v19.4 for SCP) using directDIA.
- **Downstream**: 
    - Normalization: relative iBAQ ([[riBAQ]]).
    - Dimensionality Reduction & Clustering: [[Seurat]] (v5.2.1), [[Harmony]] (for batch correction), [[PCA]], [[UMAP]].
    - Differential Expression: [[Limma]] (Empirical Bayes), [[WebGestalt]] (GO analysis).
    - Statistical testing: Welch's T-test, Logistic regression (Seurat FindMarkers).

## Results

### Main Findings
1.  **Mini-bulk Sensitivity & Phenotyping**: The workflow identified >3,000 proteins from 500 cells. It defined a proteomic signature of neutrophil maturity (distinguishing CD10+ vs CD10-), showing that CD10- immature cells have high ribosomal and mitochondrial content, while CD10+ cells are enriched in granule proteins and migration markers.
2.  **TAN Profile**: Despite the expansion of immature neutrophils in GBM patient blood, Tumor Associated Neutrophils (TANs) proteomically resemble mature circulating neutrophils (CD10+) but with significantly elevated mitochondrial metabolic proteins.
3.  **Single Cell Heterogeneity**: SCP identified 7 distinct functional clusters:
    *   **Armed**: Most abundant, high granule content, motility proteins (integrins).
    *   **Engaged**: Signs of degranulation (reduced MPO/S100A8), trajectory toward vital NETs.
    *   **Vital NETs**: Loss of granule/nuclear membrane proteins but retained histones.
    *   **Exhausted**: Retained histones but metabolic anergy (low glycolysis/glycogenolysis enzymes) and signaling dysfunction.
    *   **Lytic NETs**: Massive loss of granules, histones, and nuclear envelope; high complement/coagulation factors (suggesting vascular occlusion).
    *   **Immunosuppressive & Angiogenic**: High Arginase 1 (ARG1), pro-angiogenic factors (ECM1, S100A10), and enhanced lysosomal/phagocytic capacity.
    *   **Vascular Immature**: Rare (8%), high ribosomal/mitochondrial content, vascular signature.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Overview of low cell number workflows (Mini-bulk & SCP); comparison of protein coverage (granules, metabolism, signaling) against bulk proteomics. |
| Fig 2 | Mini-bulk proteomic analysis defining signatures of mature (CD10+) and immature (CD10-) neutrophils in blood and tumor. |
| Fig 3 | Comparison showing TANs resemble mature neutrophils (CD10+) but with increased mitochondrial phenotype and reduced proliferation markers. |
| Fig 4 | SCP analysis of TANs identifying 7 functional clusters; heatmaps of maturity, mitochondrial, and ribosomal markers; characterization of Lytic NETs. |
| Fig 5 | Predicted trajectory analysis: from Armed -> Engaged -> Vital NETs or Exhausted. Dot plots of metabolic enzymes (GLUT3, PYGL) and signaling proteins (RAC2). |
| Fig 6 | Characterization of the "Immunosuppressive & Angiogenic" subset showing high ARG1, S100A7, MMPs, and lysosomal proteins. |
| Fig 7 | Schematic summary of the proposed neutrophil functional states in human glioblastoma. |

## Discussion

### Strengths
- **Sensitivity**: Achieved >1,100 proteins per single neutrophil (a cell with very low protein content, ~30-60pg), providing the first deep single-cell proteomic map of human neutrophils.
- **Functional Insight**: Overcomes the limitations of transcriptomics in neutrophils (where mRNA correlates poorly with protein) to identify functional states like NETosis and degranulation based on actual protein abundance/loss.
- **Novel Subsets**: Identification of specific "Exhausted" and "Lytic NETs" populations that are compartment-restricted or functionally distinct in ways not previously mapped in humans.

### Limitations
- **Low Abundance Detection**: While coverage was excellent for granules and histones, low abundance proteins like chemokine receptors were difficult to detect in mini-bulk and SCP compared to bulk.
- **Sample Size**: The study analyzed a relatively small cohort (6 patients).
- **Spatial Context**: The exact spatial location of these specific clusters within the tumor (e.g., necrotic core vs. perivascular) is inferred from protein signatures but not directly visualized.

### Future Work
- Application of [[Spatial Proteomics]] to map these functional clusters to specific tumor niches (e.g., does the Lytic NETs cluster reside specifically in occluded vessels?).
- Investigation of the drivers of these states (e.g., hypoxia, cell-cell interactions).
- Determining if these states can be therapeutically targeted to shift pro-tumoral neutrophils toward anti-tumoral phenotypes.

## Personal Notes

## Related Papers

- [[Hoogendijk et al. 2019]] - "Dynamic Transcriptome-Proteome Correlation Networks Reveal Human Myeloid Differentiation and Neutrophil-Specific Programming" (Regarding mRNA/protein discordance).
- [[Ng et al. 2024]] - "Deterministic reprogramming of neutrophils within tumors" (Regarding neutrophil states in cancer).
- [[Adrover et al. 2025]] - "Neutrophils drive vascular occlusion, tumour necrosis and metastasis" (Related to the Lytic NETs/vascular occlusion finding).