---
title: Mapping early human blood cell differentiation using single-cell proteomics and transcriptomics
authors:
  - Benjamin Furtwängler
  - Nil Üresin
  - Sabrina Richter
  - Mikkel Bruhn Schuster
  - Despoina Barmpouri
  - Henrietta Holze
  - Anne Wenzel
  - Kirsten Grønbæk
  - Kim Theilgaard-Mönch
  - Fabian J. Theis
  - Erwin M. Schoof
  - Bo T Porse
aliases:
   - Furtwängler et al. 2025
   - scp-MS HSPC differentiation
   - scProtVelo paper
tags:
  - literature
  - paper
  - proteomics
  - single-cell
  - hematopoiesis
category: literature
date_created: 2025-08-21
Journal: Science
Year: 2025
---

# Mapping early human blood cell differentiation using single-cell proteomics and transcriptomics

## Citation

> [!cite] Reference
> **Title**：Mapping early human blood cell differentiation using single-cell proteomics and transcriptomics
> **Authors**: Benjamin Furtwängler, Nil Üresin, Sabrina Richter, Mikkel Bruhn Schuster, Despoina Barmpouri, Henrietta Holze, Anne Wenzel, Kirsten Grønbæk, Kim Theilgaard-Mönch, Fabian J. Theis, Erwin M. Schoof, Bo T Porse
> **Year**: 2025
> **Journal**: Science
> **DOI**: 10.1126/science.adr8785

## Abstract

Single-cell transcriptomics (scRNA-seq) has revolutionized the characterization of cell state heterogeneity and differentiation trajectories. However, mRNA measurements miss important biological information regarding the proteome. Here, the authors leveraged recent advances in single-cell proteomics by Mass Spectrometry ([[scp-MS]]) to generate a dataset of an in vivo differentiation hierarchy encompassing over 2500 human CD34+ hematopoietic stem and progenitor cells (HSPCs). Through integration with scRNA-seq, they identified proteins important for stem cell function not indicated by mRNA transcripts. Furthermore, they showed that modeling translation dynamics can infer cell progression during differentiation and explain substantially more protein variation than linear correlation. This work offers a framework for single-cell multi-omics studies across biological systems.

## Key Points

- Generated a comprehensive [[scp-MS]] dataset of >2500 human CD34+ HSPCs, identifying over 2900 proteins.
- Integrated scp-MS with [[CITE-seq]] data using a joint latent space to map lineage specification and protein-mRNA covariance.
- Identified and validated (via CRISPR/Cas9) key proteins for HSC maintenance (e.g., [[SOD1]], [[TALDO1]], [[H1F0]]) that showed low correlation with their mRNA levels.
- Developed [[scProtVelo]], a model for translation kinetics (single-cell protein velocity), to infer differentiation trajectories and cell progression.
- Demonstrated that modeling translation dynamics explains significantly more protein variance (40-50%) compared to linear mRNA-protein correlation models (36%).

## Methods

### Sample Preparation
- Method used: [[scp-MS]] (using [[TMTPro]] labeling and [[RETICLE]] acquisition), [[CITE-seq]], [[FACS]].
- Cell type: Human CD34+ hematopoietic stem and progenitor cells (HSPCs) from bone marrow.
- Number of cells: >2500 cells for scp-MS (2934 proteins across 2506 cells); 9086 cells for CITE-seq.

### Data Analysis
- Software: [[SCeptre]] (for scp-MS processing), [[Scanpy]], [[GLUE]] (for multi-omics integration), [[scVI]] (for mRNA modeling), [[Proteome Discoverer]].
- Downstream: [[scProtVelo]] (custom translation dynamics modeling), [[cellrank]] (trajectory analysis), [[GSEA]].

## Results

### Main Findings
1. **Recapitulation of HSPC Hierarchy**: scp-MS data successfully reconstructed the hematopoietic differentiation hierarchy. It revealed phenotypical information, such as the correlation between total protein signal and cell size (FSC-A), and identified [[Endomucin]] as a surface marker for enrichment of LT-HSCs.
2. **Protein-Specific Regulatory Mechanisms**: Integration with transcriptomics revealed low mRNA-protein correlation for many genes. scp-MS highlighted metabolic pathways (glycolysis, oxidative stress response) as critical for HSCs, which were not enriched at the mRNA level. Functional knockout of identified targets ([[SOD1]], [[TALDO1]], [[H1F0]]) impaired HSC function in long-term culture assays.
3. **Modeling Translation Dynamics**: The authors introduced [[scProtVelo]], which models protein abundance changes over time considering transcription, translation, and degradation. This model successfully inferred differentiation directionality (velocity) and explained protein abundance changes during erythroid differentiation better than simple linear correlations.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Overview of the [[scp-MS]] dataset of FACS-isolated human HSPCs, showing experimental workflow, data completeness, and UMAP embeddings. |
| Fig 2 | Unsupervised clustering of scp-MS data revealing distinct differentiation stages and functional protein covariance/pathway enrichment. |
| Fig 3 | Integration of scp-MS and [[CITE-seq]] data using [[GLUE]], establishing a joint latent space and transferring labels between modalities. |
| Fig 4 | Trajectory analysis on the joint latent space using [[cellrank]], identifying differentiation probabilities and lineage-specific gene expression. |
| Fig 5 | Analysis of HSC quiescence/differentiation, highlighting discordance between mRNA and protein (e.g., metabolic enzymes), with functional validation via CRISPR. |
| Fig 6 | Protein-level trajectory analysis showing lineage-specific functional covariance (e.g., MHC class I discordance) and ranking proteins by mRNA-protein correlation. |
| Fig 7 | [[scProtVelo]] modeling of translation dynamics, showing inferred protein velocity and improved explanation of protein variance compared to linear models. |

## Discussion

### Strengths
- **Multi-omics Integration**: Provides a robust framework for integrating unpaired scRNA-seq and scp-MS data.
- **Functional Validation**: Goes beyond descriptive analysis by functionally validating proteome-specific targets using CRISPR/Cas9.
- **Novel Methodology**: Introduces [[scProtVelo]] to model translation kinetics, adding a temporal dimension to static protein snapshots similar to [[RNA Velocity]].

### Limitations
- **Throughput**: scp-MS throughput (thousands of cells) is still lower than scRNA-seq (tens/hundreds of thousands).
- **Data Completeness**: scp-MS data contains missing values (on average 68% missing values per cell) requiring imputation or specific handling.
- **Model Assumptions**: The translation model assumes constant kinetic rates per gene across the modeled trajectory, which may not hold for all biological processes.

### Future Work
- Upscaling scp-MS for more robust data generation in complex biological systems.
- Applying the framework to disease states (e.g., leukemia) to understand pathological deviations.
- Refining the kinetic model to handle more complex temporal dynamics.

## Personal Notes



## Related Papers

- [[SCoPE2]] (Specht et al., 2021) - Methodological basis for single-cell proteomics.
- [[GLUE]] (Cao & Gao, 2022) - The integration framework used for multi-omics.
- [[RNA Velocity]] (La Manno et al., 2018; Bergen et al., 2020) - Conceptual basis for the velocity modeling.
- [[CITE-seq]] (Stoeckius et al., 2017) - Method for simultaneous epitope and transcriptome measurement.