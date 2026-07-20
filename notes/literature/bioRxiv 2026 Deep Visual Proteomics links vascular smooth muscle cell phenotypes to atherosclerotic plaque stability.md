---
title: Deep Visual Proteomics links vascular smooth muscle cell phenotypes to atherosclerotic plaque stability
authors:
  - Elena Kratz
  - Ankit Sinha
  - Trusha Adeshara
  - Valentina Paloschi
  - Nadja Sachs
  - Jessica Pauli
  - Nadyia Glukha
  - Annalena Huber
  - Sara Schanda
  - Andreas Metousis
  - Tim Heymann
  - Daniela Branzan
  - Tore Bleckwehl
  - Sikander Hayat
  - Lars Maegdefessel
  - Matthias Mann
aliases:
  - DeepVisAtherosclerotic
tags:
  - literature
  - paper
category: literature
date_created: 2025-05-14
Journal: bioRxiv
Year: 2026
---

# Deep Visual Proteomics links vascular smooth muscle cell phenotypes to atherosclerotic plaque stability

## Citation

> [!cite] Reference
> **Title**：Deep Visual Proteomics links vascular smooth muscle cell phenotypes to atherosclerotic plaque stability
> **Authors**: Elena Kratz, Ankit Sinha, Trusha Adeshara, Valentina Paloschi, Nadja Sachs, Jessica Pauli, Nadyia Glukha, Annalena Huber, Sara Schanda, Andreas Metousis, Tim Heymann, Daniela Branzan, Tore Bleckwehl, Sikander Hayat, Lars Maegdefessel, Matthias Mann
> **Year**: 2026
> **Journal**: bioRxiv
> **DOI**: https://doi.org/10.64898/2026.07.17.738909

## Abstract

Vascular smooth muscle cells (VSMCs) drive atherosclerosis through phenotypic switching, yet their spatial organization and protein signatures within plaques remain poorly characterized. Here, we applied Deep Visual Proteomics (DVP) to dissect more than 500 VSMC neighborhoods across 24 human carotid plaques and profile VSMC plasticity in disease. To functionally interpret these tissue proteomes, we built a reference atlas of primary VSMCs driven toward five phenotypes by TGF-β, PDGF-BB, osteogenic stimuli, IL-1β, or cholesterol, quantifying over 10,000 proteins. We integrated tissue and reference proteomes with a deep-learning framework that assigns functional phenotypes to each neighborhood. This revealed spatially distinct phenotype distributions and a shift toward dedifferentiated states in unstable plaques. Knockdown of four candidates (TNC, TNFAIP2, AEBP1, PLK1) validated operational roles during phenotypic switching. Our approach functionally annotates spatial proteomes and links VSMC plasticity to plaque instability in carotid artery disease.

## Key Points

- Applied [[Deep Visual Proteomics]] (DVP) to profile over 500 VSMC-enriched neighborhoods from 24 human carotid plaques.
- Developed a reference atlas of five VSMC functional phenotypes (contractile, proliferative, osteogenic, inflammatory, foam cell-like) using [[LC-MS/MS]].
- Implemented a semi-supervised [[Conditional Variational Autoencoder]] (CVAE) to integrate tissue and in vitro proteomes for functional annotation.
- Identified a clear contractile-to-dedifferentiated continuum in plaque VSMCs, with unstable plaques showing significantly reduced contractile VSMC proportions.
- Validated key regulators of phenotypic switching (TNC, TNFAIP2, AEBP1, PLK1) via siRNA-mediated [[knockdown]] experiments.

## Methods

### Sample Preparation
- Method used: [[Deep Visual Proteomics]] (DVP) combining [[Immunofluorescence]] (IF), [[Laser Microdissection]], and [[Data-Independent Acquisition]] (DIA) mass spectrometry.
- Cell type: Vascular smooth muscle cells (VSMCs).
- Number of cells: 400 ACTA2+ shapes per neighborhood (545 neighborhoods total).

### Data Analysis
- Software: [[DIA-NN]], [[Python]], [[R]], [[GraphPad Prism]], [[Perseus]], [[QuPath]], [[Hyperopt]].
- Downstream: [[Principal Component Analysis]] (PCA), [[Gene Set Enrichment Analysis]] (GSEA), [[Single-sample GSEA]] (ssGSEA), [[Conditional Variational Autoencoder]] (CVAE), [[Ingenuity Pathway Analysis]] (IPA).

## Results

### Main Findings
1. VSMC proteomes exhibit a "contractile-to-dedifferentiated" continuum that correlates with spatial positioning within the plaque.
2. Unstable plaques display a marked reduction in contractile VSMCs and an expansion of dedifferentiated, disease-associated states, particularly in the fibrous cap.
3. TNC functions as a pan-phenotypic regulator of VSMC switching, while PLK1, AEBP1, and TNFAIP2 govern specific proliferative, osteogenic, and inflammatory programs, respectively.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | DVP workflow and capture of VSMC neighborhood proteomes. |
| Fig 2 | PCA and molecular heterogeneity of VSMCs. |
| Fig 3 | Spatial organization and functional pathway mappings. |
| Fig 4 | Proteomic atlas of primary VSMC phenotype models. |
| Fig 5 | Deep learning framework (CVAE) for phenotype assignment. |
| Fig 6 | Functional validation via siRNA perturbation of candidate proteins. |

## Discussion

### Strengths
- Unprecedented resolution of VSMC phenotypic states within intact tissue architecture.
- Integrative approach combining in situ spatial data with highly controlled in vitro reference models.
- Validated therapeutic targets using a robust, phenotype-resolved knockdown workflow.

### Limitations
- The cohort size of 24 plaques is relatively small, necessitating future external validation.
- Heavy reliance on ACTA2 for defining the VSMC lineage.
- CVAE provides probabilistic assignments rather than ground-truth discrete calls.

### Future Work
- Testing candidate targets in human plaque *ex vivo* culture models.
- Assessing the potential of these identified targets to stabilize vulnerable lesions in *in vivo* systems.

## Personal Notes

-

## Related Papers

- Mund, A. et al. "Deep Visual Proteomics defines single-cell identity and heterogeneity." *Nat. Biotechnol.* (2022).
- Sinha, A. et al. "Spatially resolved proteomic signatures of atherosclerotic carotid artery disease." (Preprint).
- Pauli, J. et al. "Single cell spatial transcriptomics integration deciphers the morphological heterogeneity of atherosclerotic carotid arteries." *Nat. Commun.* (2025).
- [[ncardiores 2026 Proteomics reveals spatial and molecular heterogeneities in advanced atherosclerotic carotid artery plaques]]