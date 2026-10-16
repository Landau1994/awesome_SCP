---
title: Surfaceome CRISPR activation screening uncovers ligands regulating tumor sensitivity to NK cell killing
authors:
  - Ravi K. Dinesh
  - Xiaotong Wang
  - Imran A. Mohammad
  - Pari Gunasekaran
  - Kostas Stiklioraitis
  - Jeremy R. Villafuerte
  - Anirudh Rao
  - Rogelio A. Hernandez-Lopez
  - John B. Sunwoo
  - Le Cong
aliases:
  - NK_Surfaceome screeen
tags:
  - literature
  - paper
category: literature
date_created: 2025-05-14
Journal: Nature Communications
Year: 2026
---

# Surfaceome CRISPR activation screening uncovers ligands regulating tumor sensitivity to NK cell killing

## Citation

> [!cite] Reference
> **Title**：Surfaceome CRISPR activation screening uncovers ligands regulating tumor sensitivity to NK cell killing
> **Authors**: Ravi K. Dinesh, Xiaotong Wang, Imran A. Mohammad, Pari Gunasekaran, Kostas Stiklioraitis, Jeremy R. Villafuerte, Anirudh Rao, Rogelio A. Hernandez-Lopez, John B. Sunwoo, Le Cong
> **Year**: 2026
> **Journal**: Nature Communications
> **DOI**: https://doi.org/10.1038/s41467-026-76374-x

## Abstract

Natural killer (NK) cell-based immunotherapies are promising for cancer treatment, but the molecular determinants governing tumor susceptibility to NK cytotoxicity remain incompletely understood. In this study, the authors employ [[CRISPRa]] (CRISPR activation) screening with a surfaceome-focused library to identify cancer cell surface regulators of NK killing. Screening in human and murine cancer cell lines identified both established factors (e.g., [[CD43]]) and previously uncharacterized regulators (e.g., [[CD44]], [[PDPN]], [[Siglec-1]]). Validation confirms that these factors alter NK killing susceptibility in vitro and in humanized mouse models. Mechanistically, the authors find that [[CD43]]-mediated resistance functions independently of its interaction with [[Siglec-7]], acting instead as a large, glycosylated physical barrier to NK-target interactions. Furthermore, targeting [[CD43]] on [[NK cells]] or [[CAR T cells]] significantly enhances cytotoxic activity against leukemia. These results establish gain-of-function surfaceome screening as a robust strategy for identifying therapeutic targets in immunotherapy.

## Key Points

- Gain-of-function [[CRISPRa]] screening successfully identified novel surface ligands that modulate NK cell cytotoxicity across multiple tumor types.
- The resistance factor [[CD43]] works primarily through a steric "physical barrier" mechanism mediated by its N-terminal extracellular domain, rather than through specific signaling with [[Siglec-7]].
- Genetic or antibody-mediated targeting of [[CD43]] or [[CD44]] on immune effector cells (NK or CAR T cells) is a viable therapeutic strategy to enhance antitumor efficacy in hematologic malignancies.
- Combining [[CRISPRa]] screening with surface protein databases effectively reduces experimental noise compared to traditional genome-wide screens.

## Methods

### Sample Preparation
- Method used: [[CRISPR activation (CRISPRa)]], [[flow cytometry]], [[in vivo cytotoxicity assays]], [[CIBERSORTx]].
- Cell type: K562, HGC-27, YAC-1, B16F0, OCI-AML2, MV4-11, HAP1, SUPB15, Nalm6.
- Number of cells: Typically 10^6 cells per condition/well for screening.

### Data Analysis
- Software: [[R]] (packages: [[ggplot2]], [[pheatmap]], [[DESeq2]], [[TCGAbiolinks]], [[dplyr]]), [[MAGeCK]], [[CIBERSORTx]], [[IncuCyte]].
- Downstream: [[RNA-Seq]] normalization, [[survival analysis]] using Kaplan-Meier method, [[Cox proportional hazards regression]], and correlation analysis with immune infiltration.

## Results

### Main Findings
1. Identified a curated list of sensitizing and resistance ligands, including [[CD43]], [[CD44]], [[PDPN]], and [[Siglec-1]], which showed relevance across human and murine models.
2. Characterized [[CD43]] as a potent resistance ligand that functions via steric inhibition of NK-tumor cell contact, independent of the Siglec-7 inhibitory receptor.
3. Demonstrated that silencing or blocking [[CD43]] significantly increases the killing efficacy of both primary NK cells and CD19-targeted CAR T cells against various leukemia lines.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Workflow of [[CRISPRa]] screening and volcano plots of hits in K562 cells; validation of hits (SPN, CD44, etc.) via cytotoxicity assays. |
| Fig 2 | Ablation of [[CD43]] and [[CD44]] leads to increased sensitivity to NK cells in vitro and reduces tumor growth in vivo. |

## Discussion

### Strengths
- Focused surfaceome-based library design reduces noise and improves the identification of relevant targets compared to whole-genome approaches.
- Extensive cross-validation including in vitro assays, humanized mouse models, and clinical data analysis from [[TCGA]].
- Mechanistic depth provided for the CD43-mediated resistance phenomenon using truncation mutants.

### Limitations
- Discrepancies between screen results and other published genome-wide screens may reflect variations in methodology or cell-line specific contexts.
- Interpretation of some C-terminal mutant data was complicated by simultaneous changes in surface expression levels.

### Future Work
- Investigate the potential for combining targeting of multiple ligands (e.g., CD43 and CD44) to further enhance immunotherapeutic responses.
- Further explore the role of [[Siglec-1]]/[[CD169]] in tumor stroma as a potential therapeutic target in solid tumors.

## Personal Notes

## Related Papers

- [[Sheffer et al. (2021)]] - Genome-scale screens identify factors regulating tumor cell responses to natural killer cells.
- [[Dufva et al. (2023)]] - Single-cell functional genomics reveals determinants of sensitivity and resistance to natural killer cells in blood cancers.
- [[Wisnovsky et al. (2021)]] - Genome-wide CRISPR screens reveal a specific ligand for the glycan-binding immune checkpoint receptor Siglec-7.