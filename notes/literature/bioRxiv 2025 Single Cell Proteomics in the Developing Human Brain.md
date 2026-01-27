---
title: Single Cell Proteomics in the Developing Human Brain
authors:
  - Tianzhi Wu
  - Lihua Jiang
  - Tanzila Mukhtar
  - Li Wang
  - Ruiqi Jian
  - Cheng Wang
  - Tiffany Trinh
  - Arnold R. Kriegstein
  - Michael Snyder
  - Jingjing Li
aliases:
   - Single Cell Proteomics in the Developing Human Brain
   - Wu et al. 2025
tags:
  - literature
  - paper
  - single-cell-proteomics
  - neuroscience
  - developmental-biology
category: literature
date_created: 2025-06-24
Journal: bioRxiv
Year: 2025
---

# Single Cell Proteomics in the Developing Human Brain

## Citation

> [!cite] Reference
> **Title**：Single Cell Proteomics in the Developing Human Brain
> **Authors**: Tianzhi Wu, Lihua Jiang, Tanzila Mukhtar, Li Wang, Ruiqi Jian, Cheng Wang, Tiffany Trinh, Arnold R. Kriegstein, Michael Snyder, and Jingjing Li
> **Year**: 2025
> **Journal**: bioRxiv
> **DOI**: https://doi.org/10.1101/2025.06.23.660079

## Abstract

Proteins are the functional effectors of virtually all biological processes, and accurately measuring their abundance and dynamics is essential for understanding development and disease. Although mRNA levels have historically been used as proxies for protein expression, growing evidence, especially from studies of the human cerebral cortex, has revealed widespread discordance between transcript and protein abundance. To directly address this limitation, the authors developed a rigorously optimized workflow that combines single-cell mass spectrometry with precise sample preparation to resolve, for the first time, quantitative proteomes of individual cells from the developing human brain. The platform achieved deep proteomic coverage (~800 proteins per cell) even in immature prenatal human neurons (5–10 μm diameter, ~100 pg of protein per cell), capturing major brain cell types and enabling proteome-wide characterization at single-cell resolution. This approach revealed extensive transcriptome–proteome discordance across cell types, with particularly strong discrepancies in genes associated with neurodevelopmental disorders, a finding validated through orthogonal experiments. Proteins exhibited markedly higher cell-type specificity than their mRNA counterparts. By reconstructing developmental trajectories from radial glia to excitatory neurons, the study identified dynamic stage-specific protein co-expression modules and pinpointed the intermediate progenitor-to-neuron transition as a molecularly vulnerable phase linked to autism.

## Key Points

- Development of an optimized label-free [[single-cell proteomics]] workflow capable of analyzing small primary cells (~5–10 µm) from developing human brain tissue, resolving ~800 proteins per cell.
- Identification of widespread discordance between mRNA and protein abundance, particularly in genes associated with neurodevelopmental disorders (e.g., ASD); proteins often showed higher cell-type specificity than their corresponding transcripts.
- Discovery of "primed-but-silent" genes (e.g., *TBR1*) where mRNA is abundant in progenitors but protein is restricted to mature neurons, and genes with high mRNA but low protein turnover (e.g., *CHD3*).
- Reconstruction of the developmental trajectory revealed a specific protein module (Module 4) active during the intermediate progenitor-to-neuron transition that is enriched for ASD risk genes and de novo mutations.

## Methods

### Sample Preparation
- **Method used**: Fresh prenatal human brain tissue (GW 13, 15, and 19) was microdissected (Germinal Zone and Cortical Plate). Tissue was dissociated into single cells. Individual cells were sorted using [[FACS]] into low protein-binding microwells preloaded with lysis buffer.
- **Cell type**: Primary human brain cells (Radial Glia, Excitatory Neurons, Interneurons, Oligodendrocyte Precursor Cells, Microglia, Vascular cells) and Erythroid cells.
- **Number of cells**: 2,310 single cells profiled (1,505 brain cells and 805 erythroid cells post-QC).

### Data Analysis
- **Software**: [[DIA-NN]] (v1.8.1) for protein quantification from MS2 fragment-ion intensities. [[Seurat]] for clustering and dimensional reduction. [[Scanpy]] for trajectory analysis. [[WGCNA]] for protein co-expression network analysis.
- **Downstream**: Dimensionality reduction ([[UMAP]]), differential expression analysis, trajectory inference, Gene Ontology ([[GO]]) enrichment analysis, and evolutionary rate (dN/dS) calculation. Validation performed using [[Immunohistochemistry]] and [[RNAscope]].

## Results

### Main Findings
1.  **Deep Proteomic Coverage in Primary Cells**: The workflow successfully quantified ~800 protein groups per cell in small primary neurons, distinguishing major cell types including distinct fetal vs. maternal erythroid lineages and specific brain cell subtypes (e.g., oRG, IPC-EN, CGE-IN).
2.  **mRNA-Protein Discordance**: 
    *   **Group A (Low RNA/High Protein)**: Enriched for splicing factors; suggests stable protein pools despite low transcription.
    *   **Group B (High RNA/Low Protein)**: Enriched for neurodevelopmental and ASD-risk genes (e.g., *TBR1*, *CHD3*, *SCGN*). These proteins are dosage-sensitive (high pLI scores) and subject to rapid turnover or translational repression.
    *   Proteins generally exhibited sharper cell-type specificity (higher tau scores) compared to promiscuous mRNA expression.
3.  **Developmental Trajectory and ASD Vulnerability**: 
    *   Trajectory inference mapped the transition from Radial Glia (RG) $\to$ Intermediate Progenitors (IPC) $\to$ Excitatory Neurons (EN).
    *   **Module 4**: A protein co-expression module identified via [[WGCNA]] that activates at the IPC-to-EN transition. It is highly conserved evolutionarily and significantly enriched for high-confidence ASD risk genes (SFARI) and de novo mutations found in ASD probands.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Workflow overview of label-free single-cell proteomics in developing brain; protein yield metrics (~800 proteins/cell); comparison with prior studies (which used larger cells). |
| Fig 2 | Proteomic atlas of the developing brain; UMAP clustering of Erythroid and Brain cells; heatmaps of cell-type specific protein markers (e.g., HOPX, TBR1, SCGN). |
| Fig 3 | Comparison of paired scProteomics and scRNA-seq; highlights discordance in markers like *MKI67* (high RNA in RG, low protein) and *TBR1*/*SCGN*. |
| Fig 4 | Validation of RNA-protein discordance via Immunostaining and RNAscope for markers *TBR1*, *SCGN*, *TRIM33*, *ZBTB18*, *CHD3*, and *MAPT*. |
| Fig 5 | Global correlation analysis; identification of outlier groups (Group A/B); functional enrichment of discordant genes; analysis of cell-type specificity (tau scores) showing proteins are more specific than RNA. |
| Fig 6 | Proteomic trajectory inference (RG to EN); [[WGCNA]] module analysis; identification of Module 4 (IPC-EN transition) enriched for ASD genes and evolutionary conservation. |

## Discussion

### Strengths
- **First in-vivo application**: Demonstrates SCP on small, physiologically relevant primary human cells rather than large oocytes or cell lines.
- **Rigorous Validation**: Extensive use of orthogonal methods (IHC, RNAscope) to validate the specific instances of mRNA-protein discordance.
- **Biological Insight**: Moves beyond technical benchmarking to provide specific biological insights into ASD vulnerability windows that are not visible via transcriptomics alone.

### Limitations
- **Coverage**: While high for SCP (~800 proteins/cell), coverage is still significantly lower than scRNA-seq (~2000+ genes/cell), potentially missing low-abundance regulatory proteins.
- **Throughput**: Analyzed ~2,300 cells, which is substantial for SCP but orders of magnitude lower than current scRNA-seq atlases.

### Future Work
- Improving sensitivity and scalability of the SCP technology.
- Applying the workflow to other complex tissues and disease models to uncover post-transcriptional regulatory mechanisms.
- Further investigation of the specific molecular mechanisms regulating the "Group B" (High RNA/Low Protein) ASD-associated genes.

## Personal Notes

## Related Papers

- **Wang, L. et al. (2025)**: *Molecular and cellular dynamics of the developing human neocortex.* (Nature) - Provided the snRNA-seq reference atlas used for comparison.
- **Demichev, V. et al. (2020)**: *DIA-NN: neural networks and interference correction enable deep proteome coverage in high throughput.* (Nature Methods) - The core software used for protein quantification.
- **GTEx Consortium (2020/2024)**: Studies cited regarding the general correlation (or lack thereof) between mRNA and protein levels in bulk tissues.