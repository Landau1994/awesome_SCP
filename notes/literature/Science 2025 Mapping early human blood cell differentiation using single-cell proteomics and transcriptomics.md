---
title: Mapping early human blood cell differentiation using single-cell proteomics and transcriptomics
aliases:
   - Furtwängler et al 2025
   - scProtVelo paper
   - scp-MS of HSPCs
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
> **Authors**: B. Furtwängler, N. Üresin, S. Richter, M. B. Schuster, D. Barmpouri, H. Holze, A. Wenzel, K. Grønbæk, K. Theilgaard-Mönch, F. J. Theis, E. M. Schoof, B. T. Porse
> **Year**: 2025
> **Journal**: Science
> **DOI**: 10.1126/science.adr8785

## Abstract

Single-cell transcriptomics (scRNA-seq) has revolutionized the understanding of cellular heterogeneity, particularly in hematopoiesis, but mRNA levels often do not correlate perfectly with protein abundance due to post-transcriptional regulation. Here, the authors leveraged advances in single-cell proteomics by Mass Spectrometry ([[scp-MS]]) to generate a dataset of over 2500 CD34+ human hematopoietic stem and progenitor cells (HSPCs). By integrating this data with CITE-seq, they identified proteins critical for stem cell function—such as SOD1, TALDO1, and H1F0—that were not highlighted by transcriptomic data alone. Furthermore, they introduced [[scProtVelo]], a model that infers cell progression by modeling translation dynamics, explaining significantly more protein variation than linear correlation models. This work establishes a framework for integrating single-cell multi-omics to study biological systems.

## Key Points

- Generation of an in vivo differentiation hierarchy [[scp-MS]] dataset encompassing >2500 human CD34+ HSPCs with >2900 proteins quantified.
- Integration of scp-MS with [[CITE-seq]] using [[GLUE]] revealed phenotype-specific protein markers and discordant mRNA-protein correlations during lineage specification.
- Functional validation (CRISPR/Cas9) confirmed the importance of proteins identified via proteomics (e.g., [[SOD1]], [[TALDO1]]) for HSC maintenance, which were not evident from mRNA data.
- Development of [[scProtVelo]], a tool that models translation dynamics (conceptually similar to RNA velocity) to infer differentiation trajectories and explain protein abundance changes better than linear models.

## Methods

### Sample Preparation
- Method used: [[scp-MS]] (single-cell proteomics by Mass Spectrometry) with [[TMTPro]] labeling and the RETICLE acquisition method.
- Cell type: CD34+ human bone marrow Hematopoietic Stem and Progenitor Cells ([[HSPCs]]).
- Number of cells: ~2500 cells for the main scp-MS dataset (plus a second dataset of 922 cells); integrated with a [[CITE-seq]] dataset of 9086 cells.

### Data Analysis
- Software: [[Proteome Discoverer]], [[Scanpy]], [[SCeptre]] (custom pipeline), [[GLUE]] (for integration), [[CellRank]], [[scvi-tools]].
- Downstream: Unsupervised clustering, trajectory inference, gene set enrichment analysis ([[GSEA]]), and translation dynamics modeling via the newly developed [[scProtVelo]] Python package.

## Results

### Main Findings
1. **Recapitulation of HSPC Hierarchy**: The scp-MS data successfully reconstructed the hematopoietic differentiation tree, identifying classic populations (HSCs, MPPs, LMPPs, etc.) and revealing protein-level heterogeneity that FACS markers alone could not resolve.
2. **Discordant Regulation**: There is a low correlation (r ~0.25) between mRNA and protein abundance in quiescent HSCs. Specific pathways, such as oxidative stress handling (SOD1) and chromatin structure (H1F0), show protein-level enrichment in HSCs without corresponding high mRNA levels.
3. **Translation Dynamics Modeling**: The [[scProtVelo]] model demonstrated that accounting for translation and degradation rates (time delays between mRNA and protein) explains ~40% more variance in protein abundance during differentiation compared to simple linear models.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Overview of the [[scp-MS]] dataset of FACS-isolated human HSPCs, showing UMAP embeddings, data completeness, and gating strategies. |
| Fig 2 | Unsupervised clustering showing distinct cellular differentiation stages and functional protein covariation not fully captured by FACS. |
| Fig 3 | Integration of transcriptomics (scRNA-seq) and proteomics (scp-MS) using a joint latent space via [[GLUE]], showing label transfer and consistency. |
| Fig 4 | Trajectory analysis on the joint latent space using [[CellRank]], recapitulating differentiation paths and identifying lineage-specific factors. |
| Fig 5 | Analysis of HSC quiescence and differentiation, highlighting low mRNA-protein correlation in HSCs and functional validation of targets ([[SOD1]], [[TALDO1]], [[H1F0]]) via CRISPR knockout assays. |
| Fig 6 | Protein level-specific functional covariation, showing lineage markers (e.g., MHC Class I members) where protein abundance is maintained despite mRNA downregulation. |
| Fig 7 | **scProtVelo** results: modeling translation dynamics to infer cell progression (velocity) and explaining protein variance better than linear models. |

## Discussion

### Strengths
- **Multi-omics Integration**: Demonstrates a robust framework for bridging the gap between scRNA-seq and scp-MS, overcoming the sparsity of proteomic data by leveraging the depth of transcriptomics.
- **Novel Tool**: Introduction of [[scProtVelo]] adds a new dimension to trajectory inference by explicitly modeling the "delay" of translation, similar to how RNA velocity models splicing.
- **Functional Proof**: Goes beyond observation by functionally validating protein hits that would have been missed by RNA-seq alone, proving the biological necessity of the proteomic layer.

### Limitations
- **Throughput/Coverage**: While state-of-the-art, the protein coverage (~2900 proteins) and cell throughput (~2500 cells) are still lower than standard scRNA-seq experiments.
- **Imputation Reliance**: The integration and some analyses rely on computational imputation (e.g., kNN, GLUE) to bridge missing values typical in mass spectrometry.

### Future Work
- Upscaling [[scp-MS]] for more robust data generation in complex biological systems.
- Applying the scProtVelo framework to disease states, such as leukemia, to understand dysregulated translation dynamics.
- Further investigating the specific molecular mechanisms driving the observed uncoupling of mRNA and protein abundances in HSCs.

## Personal Notes



## Related Papers

- [[SCoPE2]]: Specht et al., 2021 (Methodological basis for multiplexed scp-MS).
- [[RNA Velocity]]: La Manno et al., 2018 (Conceptual basis for velocity modeling).
- [[GLUE]]: Cao & Gao, 2022 (Method used for multi-omics integration).