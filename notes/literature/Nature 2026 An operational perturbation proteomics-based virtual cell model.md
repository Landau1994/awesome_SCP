---
title: An operational perturbation proteomics-based virtual cell model
aliases:
  - ProteinTalks
authors:
  - Rui Sun
  - Liujia Qian
  - Yongge Li
  - Tong Liu
  - Honghan Cheng
  - Xuedong Zhang
  - Xueya Zhou
  - Yuecheng Zhan
  - Guangmei Zhang
  - Zhengchao Luo
  - Kunpeng Ma
  - Chunlong Wu
  - Dongchen Ji
  - Zhangzhi Xue
  - Hongxue Meng
  - Yuhang Xiang
  - Dingwei Lei
  - Qianhe Zhou
  - Wenbin Hu
  - Yuhan Deng
  - Lingling Tan
  - Qi Xiao
  - Zhiwei Liu
  - Lei Zeng
  - Liqin Qian
  - Xuan Zheng
  - Qiong Hu
  - Nianzi Luo
  - Weinan E
  - Peijie Zhou
  - Han Wen
  - Yi Zhu
  - Tiannan Guo
year: 2026
journal: Nature
doi: 10.1038/s41586-026-11001-9
url: https://doi.org/10.1038/s41586-026-11001-9
tags:
  - paper
  - AIVC
status: unread
rating:
date_added: 2024-05-22
date_read:
---

# An operational perturbation proteomics-based virtual cell model

## Quick Summary
> ProteinTalks is a deep-learning-based "virtual cell" model designed to advance in silico drug discovery by leveraging large-scale, time-resolved perturbation proteomics. By generating a massive dataset of temporal protein-abundance measurements from perturbed breast cancer cell lines, the model employs a [[Neural ODE]] architecture to learn transferable dynamical latent representations. This enables the model to effectively predict drug efficacy, identify drug resistance mechanisms, prioritize drug combinations, and stratify patient responses across various contexts, including cell lines, patient-derived organoids (PDOs), and clinical biopsies.

## Key Points
- Generated the ProteinTalks dataset (PTDS): 38 million temporal protein-abundance measurements from 18 breast cancer cell lines treated with 63 FDA-approved drugs.
- Developed ProteinTalks: A virtual cell model utilizing a neural ODE framework to bridge the gap between static transcriptomic models and dynamic cellular responses.
- Enables operational drug discovery tasks: drug synergy prediction, patient-specific candidate nomination, and biomarker identification (e.g., AKR1C3).
- Demonstrates superior performance compared to existing transcriptomics-based foundation models (e.g., [[Geneformer]], [[GeneCompass]], [[UCE]]) in generalization across cell lines and cancer types.
- Validated via experimental knockdown studies (e.g., AKR1C3, TYMS) and clinical prognosis stratification in a 501-patient TNBC cohort.

## Methods
### Data
- PTDS: 16 TNBC and 2 non-TNBC cell lines treated with 63 drugs at 0, 6, 24, and 48 hours.
- mtPTDS: Multi-time-point dataset for deep temporal resolution (11 time points) across 3 TNBC cell lines.
- Independent validation datasets: PTNC (81 anticancer compounds in 4 TNBC lines) and PTPC (708 repurposed compounds in 5 non-breast cancer lines).

### Model Architecture
- [[Neural ODE]]: Used to model the time-dependent evolution of protein expression following drug perturbation.
- Module 1 (Encoder-Decoder): Models temporal dynamics; takes baseline proteome and drug targets as input to project to hidden states.
- Module 2 (MLP): Integrates drug molecular fingerprints (via [[SMILES]]) and predicted proteomic trajectories to output efficacy and synergy scores.

### Training Strategy
- Joint learning of temporal reconstruction ([[MSE]]) and drug response classification ([[BCE]]).
- Optimization using [[AdamW]] and [[SWAG]] (Stochastic Weight Averaging-Gaussian) for robustness.
- Hyperparameter tuning conducted via discrete factorial sweep.

## Results
| Metric | Value | Baseline |
|--------|-------|----------|
| Cross-cell-line AUPRC | 0.89 (avg) | Varies (outperforms 7 benchmarks) |
| Untrained drug AUPRC (PTNC) | 0.94 | 0.70 (Geneformer) |
| Non-breast cancer AUPRC | 0.41 | 0.19 (UCE) |

## Figures


| Figure | Description |
| ------ | ----------- |
| Fig 1  | Overview of the ProteinTalks workflow including data generation, model architecture, and downstream applications. |
| Fig 2  | Longitudinal proteomic responses to drug perturbation, showing pathway enrichment and temporal protein expression clusters. |


## Critical Analysis
### Strengths
- Uniquely addresses the "snapshot" limitation of transcriptomic models by incorporating longitudinal proteomic data.
- Compact architecture compared to parameter-heavy LLM/foundation models, yet achieves higher predictive accuracy.
- Robust validation pipeline spanning cell lines, patient-derived models (PDX/PDO), and clinical cohorts.

### Weaknesses
- DIA-MS throughput prioritization may limit depth compared to "ultra-deep" proteomic methods.
- Does not explicitly model dose-dependent or sequence-dependent treatment effects in the current framework.
- Heavy reliance on TNBC context; generalizability to non-cancer biological contexts remains to be seen.

### Questions
- How easily can this model be adapted to non-drug perturbation types (e.g., nutrient deprivation, environmental stressors)?
- Could multi-omics integration (beyond proteomics) further improve the predictive capabilities, and at what computational cost?

## Connections
### Related Papers
- [[Geneformer]]
- [[GeneCompass]]
- [[UCE]]
- [[DeepSynergy]]
- [[Neural ODEs]]

### Related Concepts
- [[Perturbation Proteomics]]
- [[Virtual Cell]]
- [[In Silico Drug Discovery]]

### Potential Applications
- Personalized drug repurposing for patient-derived tumor models.
- Biomarker discovery for treatment resistance.
- Prognostic stratification in clinical oncology.

## Notes
-