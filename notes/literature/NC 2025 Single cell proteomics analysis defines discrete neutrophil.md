---
title: Single cell proteomic analysis defines discrete neutrophil functional states in human glioblastoma
authors:
  - Pranvera Sadiku
  - Alejandro J. Brenes
  - Rupert L. Mayer
  - Leila Reyes
  - Patricia Coelho
  - Gabi van Stralen
  - Ailiang Zhang
  - Manuel A. Sanchez-Garcia
  - Emily R. Watts
  - Imran Liaquat
  - Andrew J. M. Howden
  - Ikeoluwa Adekoya
  - Anuka Boldbaatar
  - Allan MacRaild
  - Sarah Risbridger
  - Gillian M. Morrison
  - Heather MacPherson
  - Caroline M. Bruce
  - Shonna Johnston
  - Robert Grecian
  - Fiona A. Murphy
  - Steven M. Pollard
  - Paul M. Brennan
  - Karl Mechtler
  - Sarah R. Walmsley
aliases:
   - Single cell proteomic analysis defines discrete neutrophil functional states in human glioblastoma
   - Sadiku et al. 2025
tags:
  - literature
  - paper
  - proteomics
  - glioblastoma
  - neutrophils
category: literature
date_created: 2024-05-22
Journal: Nature Communications
Year: 2025
---

# Single cell proteomic analysis defines discrete neutrophil functional states in human glioblastoma

## Citation

> [!cite] Reference
> **Title**：Single cell proteomic analysis defines discrete neutrophil functional states in human glioblastoma
> **Authors**: Pranvera Sadiku, Alejandro J. Brenes, Rupert L. Mayer, et al.
> **Year**: 2025
> **Journal**: Nature Communications
> **DOI**: https://doi.org/10.1038/s41467-025-67367-3

## Abstract

Neutrophils are vital innate immune cells shown to infiltrate glioblastomas, however we currently lack the molecular understanding of their functional states within the tumour niche. Given that neutrophils are known to display a prominent discordance between mRNA and protein abundance, we develop ultra-sensitive mini-bulk and single cell proteomic (SCP) workflows to study the heterogeneity of peripheral blood and tumour associated neutrophils (TAN) from patients with glioblastoma. Mini-bulk analysis enable a deeper protein coverage of circulating immature, mature and TAN populations, defining signatures of maturity and demonstrating that TANs resemble mature circulating neutrophils. Analysis of the SCP data results in the detection of >1,100 proteins from a single TAN providing a detailed characterization of neutrophil subsets in glioblastoma. Our approach shows evidence of pathogenic and anti-tumorigenic clusters and discovers cell states invisible to scRNAseq, opening new opportunities to selectively target pro-tumoural neutrophil states.

## Key Points

- **Ultra-sensitive Proteomics**: Developed workflows to analyze low-input (500 cells, "mini-bulk") and single-cell neutrophils, which have very low protein content (~60pg/cell).
- **Functional Heterogeneity**: Identified seven discrete functional states of tumor-associated neutrophils (TANs) in glioblastoma (GBM): armed, engaged, vital NETs, exhausted, lytic NETs, immunosuppressive/angiogenic, and vascular immature.
- **Transcriptome-Proteome Discordance**: SCP identified states (like NETotic versus degranulating cells) that are often "invisible" to single-cell RNA sequencing due to the long-term storage of proteins in granules and low mRNA-protein correlation in neutrophils.

## Methods

### Sample Preparation
- **Method used**: FACS (Fluorescence-activated cell sorting) directly into 384-well plates followed by automated sample processing on a cellenONE X1.
- **Cell type**: Human peripheral blood neutrophils (NDN, LDN) and tumor-associated neutrophils (TAN) from glioblastoma patients.
- **Number of cells**: 2 million (Bulk), 500 cells (Mini-bulk), and 1 cell (SCP).

### Data Analysis
- **Software**: Spectronaut 19.4/19.7 for Data-Independent Acquisition (DIA) search; Seurat v5.2.1 for single-cell clustering and UMAP visualization; Harmony for batch correction.
- **Downstream**: riBAQ (relative Intensity Based Absolute Quantification) for normalization; Limma for differential expression; WebGestalt for Gene Ontology (GO) enrichment.

## Results

### Main Findings
1. **TAN Maturity**: Mini-bulk analysis revealed that GBM TANs primarily resemble mature CD10+ circulating neutrophils rather than immature low-density neutrophils (LDNs), but they exhibit a distinct "intermediate" mitochondrial phenotype.
2. **Cluster Identification**: SCP successfully identified 7 functional states. The "Armed" cluster is the most abundant and poised for response, while "Immunosuppressive & Angiogenic" clusters show high levels of Arginase 1 and pro-angiogenic factors (ECM1, S100A10).
3. **NETosis Differentiation**: The study distinguished between "Vital NETing" (retaining some histones/membranes) and "Lytic NETosis" (massive loss of histones and granules with a vascular signature of complement and coagulation proteins).
4. **Exhaustion State**: Identified an "Exhausted" neutrophil state characterized by metabolic anergy (low glycolysis/glycogenolysis enzymes) and reduced capacity to respond to stimuli.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Workflow comparison between Bulk, Mini-bulk, and SCP, demonstrating sensitivity and protein coverage. |
| Fig 2 | Proteomic signatures of mature (CD10+) vs immature (CD10-) blood neutrophils. |
| Fig 3 | Comparison of TANs to circulating populations, highlighting the mitochondrial phenotype. |
| Fig 4 | SCP UMAP showing 7 discrete functional clusters of TANs and their protein signatures (histones, granules, ribosomes). |
| Fig 5 | Predicted functional trajectory from Armed -> Engaged -> Vital NETs or Exhaustion. |
| Fig 6 | Detailed proteomic analysis of the Immunosuppressive and Angiogenic neutrophil subset. |
| Fig 7 | Summary schematic showing the spatial and functional landscape of neutrophils in the GBM niche. |

## Discussion

### Strengths
- **Technical Innovation**: Overcomes the challenge of low protein content in neutrophils to achieve single-cell resolution.
- **Biological Insight**: Uncovers functional states (like specific NETosis types and exhaustion) that cannot be accurately identified by transcriptomics alone.
- **Resource Generation**: Provides a pioneering single-cell proteomic resource for human tissue-associated neutrophils.

### Limitations
- **Sample Size**: SCP analysis was performed on 277 cells from 6 patients; while robust, it is smaller in scale than typical scRNAseq studies.
- **Spatial Resolution**: The current study uses dissociated tissue; future work using spatial proteomics is needed to confirm the exact location of these states (e.g., peri-vascular vs. necrotic core).

### Future Work
- Investigating how these neutrophil states evolve during tumor progression and treatment.
- Exploring the potential to selectively target pro-tumoural states (like lytic NETosis or immunosuppressive clusters) to improve GBM outcomes.

## Personal Notes

- The discovery of the "vascular immature" cluster (only 8% of TANs) suggests that immature neutrophils might be restricted to the vasculature and excluded from the tumor parenchyma in GBM.
- The discordance between mRNA and protein is a critical takeaway for anyone studying myeloid cells in cancer.

## Related Papers

- **Ng, M. S. F. et al. (2024)**: Deterministic reprogramming of neutrophils within tumors. *Science*.
- **Ugolini, A. et al. (2025)**: Functional Reprogramming of Neutrophils within the Brain Tumor Microenvironment. *Cancer Discovery*.
- **Wisniewski, J. R. et al. (2014)**: The "proteomic ruler" for protein copy number estimation. *MCP*.