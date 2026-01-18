---
title: papers
aliases:
  - <article>
  - <paper>
  - <literature>
tags:
  - literature
  - paper
category: literature
date_created: 2026-01-18
related_topics: applications
Journal: Nature Communications
---
# Single cell proteomic analysis defines discrete neutrophil functional states in human glioblastoma

## Citation

> [!cite] Reference
> **Authors**: Sadiku, P., Brenes, A.J., Mayer, R.L., Reyes, L., Coelho, P., van Stralen, G., Zhang, A., Sanchez-Garcia, M.A., Watts, E.R., Liaquat, I., Howden, A.J.M., Adekoya, I., Boldbaatar, A., MacRaild, A., Risbridger, S., Morrison, G.M., MacPherson, H., Bruce, C.M., Johnston, S., Grecian, R., Murphy, F.A., Pollard, S.M., Brennan, P.M., Mechtler, K. & Walmsley, S.R.
> **Year**: 2025
> **Journal**: Nature Communications
> **DOI**: https://doi.org/10.1038/s41467-025-67367-3

## Abstract

This study addresses the lack of molecular understanding regarding neutrophil functional states within the glioblastoma (GBM) tumor niche. Recognizing the discordance between mRNA and protein abundance in neutrophils, the authors developed ultra-sensitive mini-bulk and single-cell proteomic (SCP) workflows. They analyzed peripheral blood and tumor-associated neutrophils (TANs) from GBM patients. Mini-bulk analysis revealed that TANs resemble mature circulating neutrophils rather than immature populations, despite the expansion of immature neutrophils in the blood. SCP analysis of TANs (identifying >1,100 proteins per cell) uncovered seven distinct functional clusters, including pathogenic and anti-tumorigenic states. Crucially, these proteomic states—such as those defined by granule content and histone levels—are often invisible to scRNAseq, highlighting the necessity of proteomic resolution to understand neutrophil biology in cancer.

## Key Points

- Development of an ultra-sensitive mass spectrometry workflow capable of analyzing **mini-bulk (500 cells)** and **single cells** of neutrophils, which have very low protein content (~30-60 pg/cell).
- **Tumor Associated Neutrophils (TANs)** in GBM proteomically resemble mature CD10+ circulating neutrophils but display increased mitochondrial content, distinct from the expanded immature CD10- population in patient blood.
- Identification of **seven discrete functional neutrophil clusters** in GBM via SCP: Armed, Engaged, Vital NETs, Exhausted, Lytic NETs, Immunosuppressive & Angiogenic, and Vascular Immature.
- Discovery of cell states invisible to **scRNAseq**, particularly differentiating between "Vital NETs" and "Lytic NETs" based on the retention or loss of granule and histone proteins.

## Methods

### Sample Preparation
- **Method used**: [[Label-free single-cell proteomics]] (SCP) and mini-bulk proteomics.
- **Cell type**: Human neutrophils isolated from peripheral blood and Glioblastoma (GBM) tumor tissue.
- **Number of cells**:
    - **Mini-bulk**: 500 cells per sample.
    - **SCP**: Single cells sorted (330 processed, 277 analyzed after filtering).
- **Processing**: Cells sorted into 384-well plates containing lysis master mix. Processed using the [[cellenONE]] platform for nanoliter-scale lysis and tryptic digestion. Analyzed on a [[Thermo Scientific Vanquish Neo UHPLC]] coupled to an [[Orbitrap Astral]] mass spectrometer with a [[FAIMS Pro Duo]] interface.

### Data Analysis
- **Software**: [[Spectronaut]] (v19.4 for SCP, v19.7 for bulk/mini-bulk) using DirectDIA.
- **Downstream**: Analysis performed in R using [[limma]] for differential expression, [[WebGestalt]] for GO analysis, and [[Seurat]] (v5.2.1) for single-cell clustering and visualization. Normalization used a relative iBAQ (riBAQ) approach.

## Results

### Main Findings
1. **Workflow Sensitivity**: The optimized workflow identified >3,000 proteins from 500 cells (mini-bulk) and >1,100 proteins from single neutrophils. This provided high coverage of granule proteins (80% of bulk), metabolic proteins (75%), and immune signaling proteins.
2. **TAN Phenotype**: In GBM patients, an immature CD10- neutrophil population expands in the blood (Low Density Neutrophils). However, mini-bulk proteomics showed that TANs clusters closely with mature CD10+ neutrophils rather than the immature subset, though TANs exhibit higher mitochondrial metabolic proteins.
3. **Single Cell Heterogeneity**: SCP revealed distinct functional states:
    - **Armed**: Most abundant, high cytoskeletal and granule proteins (poised to respond).
    - **Engaged**: Signs of degranulation (reduced MPO/S100A8) but intact histones.
    - **Vital NETs**: Loss of granules and secretory vesicles, reduced histones.
    - **Exhausted**: Retained histones but significant reduction in metabolic enzymes (glycolysis/pentose phosphate pathway) and signaling proteins (RAC2, Calmodulin).
    - **Lytic NETs**: Massive loss of nuclear, granule, and cytoplasmic proteins; enriched for complement and coagulation factors (suggesting vascular localization/occlusion).
    - **Immunosuppressive & Angiogenic (I&A)**: High Arginase 1 (ARG1), S100A7, and angiogenic factors (ECM1, MMP9), with enhanced lysosomal/phagocytic machinery.
    - **Vascular Immature**: Small population (8%) retaining immature markers (PCNA, CEBPE) and ribosomal proteins.

### Figures

| Figure | Description |
|--------|-------------|
| **Fig 1** | Schematic of the mini-bulk and SCP workflows; comparison of protein coverage and copy number estimation against bulk proteomics. |
| **Fig 2** | Proteomic comparison of mature (CD10+) and immature (CD10-) blood neutrophils vs. TANs using mini-bulk (500 cells). Shows immature cells have high ribosomal/mitochondrial content. |
| **Fig 3** | Comparison of TANs to blood neutrophils. TANs resemble mature neutrophils but with elevated mitochondrial proteins and reduced proliferation markers compared to immature cells. |
| **Fig 4** | SCP analysis of TANs (n=277) showing 7 clusters. Heatmaps and dot plots define signatures for immature (PCNA), NETotic (histone loss), and metabolic states. |
| **Fig 5** | Functional trajectory analysis. Visualizes the transition from "Armed" to "Engaged" and potential endpoints of "Vital NETs" (histone loss) or "Exhausted" (metabolic anergy). |
| **Fig 6** | Characterization of the "Immunosuppressive and Angiogenic" cluster, highlighting high ARG1, S100A7, ECM1, and lysosomal proteins. |
| **Fig 7** | Schematic overview of the proposed neutrophil functional states and trajectories within the GBM tumor microenvironment. |

## Discussion

### Strengths
- **Single-cell resolution for low-protein cells**: Successfully applied SCP to neutrophils (~60pg protein/cell), a cell type typically excluded from SCP studies due to low protein content.
- **Functional definition beyond mRNA**: Demonstrates that proteomic analysis captures functional states (e.g., degranulation, NETosis) that rely on pre-formed proteins and are therefore invisible to transcriptomic methods (scRNAseq).
- **Novel cluster identification**: Differentiated between "Lytic NETosis" (vascular, necrotic) and "Vital NETosis" (tissue infiltrating), and identified a specific immunosuppressive/angiogenic subset.

### Limitations
- **Sample size**: Analysis was limited to 277 single cells after filtering, which is lower than typical scRNAseq throughput.
- **Low abundance detection**: While coverage was high for granules/metabolism, low abundance proteins like chemokine receptors were difficult to detect even in mini-bulk.
- **Missing immature/vascular context**: The immature population found in tumors was small (8%); it is unclear if they are actively excluded or rapidly differentiate.

### Future Work
- Application of **spatial proteomics** to understand if specific neutrophil states (e.g., Lytic NETs) are spatially restricted to the perivascular niche or necrotic core.
- Investigation into the drivers of these states (e.g., hypoxia, cell-cell interactions) and how they evolve during tumor progression and treatment.

## Personal Notes

## Related Papers

- [Adrover, J. M. et al. Neutrophils drive vascular occlusion, tumour necrosis and metastasis. Nature (2025)](https://doi.org/10.1038/s41586-025-09278-3) - *Referred to in text regarding vascular occlusion by NETs.*
- [Ng, M. S. F. et al. Deterministic reprogramming of neutrophils within tumors. Science (2024)](https://doi.org/10.1126/science.adf6493) - *Regarding neutrophil reprogramming in the tumor niche.*
- [Bubis, J. A. et al. Challenging the Astral mass analyzer... Nat Methods (2025)](https://doi.org/10.1038/s41592-024-02559-1) - *Regarding Orbitrap Astral sensitivity for SCP.*