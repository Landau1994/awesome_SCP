---
title: Large-scale proteomics across neurological disorders uncovers biomarker panel and targets in multiple sclerosis
authors:
  - Jakob Maximilian Bader
  - Christine Makarov
  - Sabrina Richter
  - Maximilian Thomas Strauss
  - Friederike Held
  - Maria Wahle
  - Michael Baggio Lorenz
  - Lara Pöschl
  - Patricia Skowronek
  - Marvin Thielert
  - Achim Berthele
  - Wen-Feng Zeng
  - Constantin Ammar
  - Isabell Bludau
  - Benjamin Schubert
  - Fabian J. Theis
  - Christiane Gasperi
  - Bernhard Hemmer
  - Matthias Mann
aliases:
   - Bader et al. 2026
   - CSF proteomics MS biomarker panel
tags:
  - literature
  - paper
  - proteomics
  - multiple_sclerosis
  - biomarker
  - CSF
category: literature
date_created: 2026-04-02
Journal: Cell
Year: 2026
---

# Large-scale proteomics across neurological disorders uncovers biomarker panel and targets in multiple sclerosis

## Citation

> [!cite] Reference
> **Title**： Large-scale proteomics across neurological disorders uncovers biomarker panel and targets in multiple sclerosis
> **Authors**: Jakob Maximilian Bader, Christine Makarov, Sabrina Richter, et al., Christiane Gasperi, Bernhard Hemmer, Matthias Mann
> **Year**: 2026
> **Journal**: Cell
> **DOI**: https://doi.org/10.1016/j.cell.2026.01.017

## Abstract

Deep proteome profiling of over 5,000 cerebrospinal fluid samples by mass spectrometry maps protein alterations across major neurological disorders, resolving key sources of variation as well as shared and disease-specific signatures. This framework yields a 22-protein assay that improves the differential diagnosis of multiple sclerosis from other inflammatory conditions, particularly in diagnostically challenging oligoclonal band-negative individuals.

## Key Points

- High-throughput mass spectrometry workflow characterizing ~1,500 to ~2,100 proteins per CSF sample across >5,000 individuals.
- Identification of blood-CSF barrier (BCB) impairment as the dominant source of proteomic variation, surpassing disease effects.
- Development of a 22-protein biomarker panel that outperforms established clinical markers in diagnosing Oligoclonal Band (OCB)-negative Multiple Sclerosis (MS).
- Validation of the panel using a targeted assay on the [[Stellar]] mass spectrometer in an independent replication cohort.
- Proteome-based "pseudo-time" staging of MS patients correlates with disability scores and disease progression.

## Methods

### Sample Preparation
- **Method used**: Automated robotic sample preparation on [[Agilent Bravo]].
- **Sample Type**: Cerebrospinal fluid (CSF) (supernatant after centrifugation to remove cells).
- **Digestion**: Trypsin and LysC.
- **Cleanup**: [[StageTips]] with [[SDB-RPS]] resin.
- **Number of Samples**: 5,045 (Discovery cohort) and 616 (Replication cohort).

### Data Analysis
- **Mass Spectrometry**: [[timsTOF Pro 2]] (Discovery, 60 samples/day) and [[Orbitrap Astral]] (Deep profiling, 100 samples/day). Targeted assay on [[Stellar]].
- **Software**: [[DIA-NN]] (processing), [[MSFragger]] / [[FragPipe]] (library generation), [[AlphaPeptDeep]] (spectral library prediction), [[Skyline]] (targeted assay analysis).
- **Downstream**: [[DirectLFQ]] (normalization), [[XGBoost]] (classification), [[SHAP]] (feature importance/interpretability), [[Perseus]] (statistical analysis).

## Results

### Main Findings
1.  **Dominant Sources of Variance**: Blood-CSF barrier (BCB) impairment accounts for approximately three times the variance explained by clinical diagnosis. Age and sex also significantly influence the proteome.
2.  **MS Biomarker Panel**: A 22-protein panel was derived (including immunoglobulins, [[CTSW]], [[FCRL5]], [[CD27]], [[CD7]], [[SDC1]], [[MBP]]) which distinguishes MS from other inflammatory CNS diseases. It specifically improved diagnosis accuracy (0.1–0.2 ROC AUC increase) for OCB-negative MS cases compared to standard clinical markers.
3.  **MS Disease Progression**: A proteomic "pseudo-time" metric was developed that aligns with the Relapsing-Remitting (RRMS) to Progressive (PMS) continuum. This staging correlated with the Age-Related Multiple Sclerosis Severity Score (ARMSS) and predicted time to conversion from RRMS to SPMS.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Study design, workflow comparison ([[timsTOF]] vs [[Orbitrap Astral]]), and the impact of BCB impairment (albumin ratio) on protein detection. |
| Fig 2 | Analysis of covariates (age, sex, QAlb) and their contribution to proteomic variance; shared vs. disease-specific signatures. |
| Fig 3 | MS-specific proteome alterations, highlighting immunoglobulin enrichment and specific markers like [[CTSW]] and [[RYR2]]. |
| Fig 4 | Multi-class machine learning prediction of neurological conditions and pseudo-time analysis of MS progression. |
| Fig 5 | Discovery of the protein panel specifically separating OCB-positive and OCB-negative MS from other CNS inflammatory diseases. |
| Fig 6 | Development and validation of the targeted [[Stellar]] mass spectrometry assay for the 22-protein panel in an independent cohort. |
| Fig 7 | Differential signatures between Relapsing-Remitting (RRMS) and Progressive MS (PMS); proteome-based staging of disease evolution. |

## Discussion

### Strengths
- **Scale and Depth**: The study represents one of the largest CSF proteomic datasets (over 5,000 samples) with high depth (>2,000 proteins/sample using [[Orbitrap Astral]]).
- **Clinical Relevance**: Directly addresses the diagnostic gap for OCB-negative MS patients.
- **Translational Pathway**: Demonstrated the transfer of discovery findings to a routine-compatible targeted assay ([[Stellar]] PRM).
- **Robustness**: Rigorous handling of covariates, particularly the correction for BCB impairment which is often overlooked.

### Limitations
- **BCB Impairment**: While corrected for, the dominance of plasma protein leakage in CSF remains a significant analytical challenge.
- **Cross-sectional Design**: Most data is cross-sectional; while pseudo-time provides insights, longitudinal samples are needed for direct progression prediction.
- **Quantification**: The targeted assay uses spike-in standards but absolute quantification with defined concentration standards is needed for clinical qualification.

### Future Work
- Large-scale validation of the 22-protein panel in prospective, multi-center studies.
- Integration of CSF proteomics with MRI findings.
- Further investigation of identified therapeutic targets like [[RYR2]] and [[CSF1R]] in MS.

## Personal Notes



## Related Papers

- [[Held et al. 2024]] - Proteomics reveals age as major modifier of inflammatory CSF signatures in MS.
- [[Åkesson et al. 2023]] - Proteomics reveal biomarkers for diagnosis, disease activity and long-term disability outcomes in MS.
- [[Teunissen and Khalil 2012]] - Neurofilaments as biomarkers in multiple sclerosis.