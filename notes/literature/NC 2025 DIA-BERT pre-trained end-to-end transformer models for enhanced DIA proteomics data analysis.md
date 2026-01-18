---
title: "DIA-BERT: pre-trained end-to-end transformer models for enhanced DIA proteomics data analysis"
authors:
  - Zhiwei Liu
  - Pu Liu
  - Yingying Sun
  - Zongxiang Nie
  - Xiaofan Zhang
  - Yuqi Zhang
  - Yi Chen
  - Tiannan Guo
aliases:
   - DIA-BERT
   - transformer-based DIA analysis
tags:
  - literature
  - paper
  - proteomics
  - deep-learning
  - mass-spectrometry
category: literature
date_created: 2024-05-22
Journal: Nature Communications
Year: 2025
---

# DIA-BERT: pre-trained end-to-end transformer models for enhanced DIA proteomics data analysis

## Citation

> [!cite] Reference
> **Title**: DIA-BERT: pre-trained end-to-end transformer models for enhanced DIA proteomics data analysis
> **Authors**: Zhiwei Liu, Pu Liu, Yingying Sun, Zongxiang Nie, Xiaofan Zhang, Yuqi Zhang, Yi Chen, & Tiannan Guo
> **Year**: 2025
> **Journal**: Nature Communications
> **DOI**: https://doi.org/10.1038/s41467-025-58866-4

## Abstract

Data-independent acquisition mass spectrometry (DIA-MS) is essential for quantitative proteomics, but current analysis tools often rely on file-specific scoring models and handcrafted features. In this study, the authors present **DIA-BERT**, a transformer-based pre-trained AI model for end-to-end DIA data analysis. The identification model was pre-trained on over 276 million peptide precursors from 952 DIA-MS files, while the quantification model utilized 34 million synthetic peptide precursors. Compared to the current state-of-the-art tool DIA-NN, DIA-BERT achieved a 51% increase in protein identifications and 22% more peptide precursors on average across multiple human cancer datasets, while maintaining high quantitative accuracy and enhancing the detection of low-abundance proteins.

## Key Points

- **End-to-End Learning**: Unlike traditional tools that use independent representation and scoring models, DIA-BERT uses a unified transformer architecture to concurrently optimize representation and scoring, eliminating the need for handcrafted features.
- **Large-Scale Pre-training**: The model leverages "big data" by pre-training on hundreds of millions of precursors, allowing it to capture intricate peptide-peak-group matching patterns that single-file training cannot.
- **Improved Sensitivity**: Demonstrates significant superiority in identifying "one-hit-wonder" proteins and low-abundance precursors compared to library-based and library-free methods like DIA-NN.

## Methods

### Sample Preparation
- **Method used**: Data-independent acquisition mass spectrometry (DIA-MS).
- **Cell/Tissue type**: 
    - Five human cancer types: cervical cancer, pancreatic adenocarcinoma, myosarcoma, gallbladder cancer, and gastric carcinoma.
    - Three-species dataset (human, yeast, and *C. elegans*).
    - Mouse-yeast hybrid proteome dataset.
- **Training Data**: 952 DIA-MS files from various human specimens; 360 simulated mzML files (6.87 TB) generated via a modified *Synthedia* package for quantification training.

### Data Analysis
- **Software**: **DIA-BERT** (Transformer-based architecture: 8 self-attention blocks, convolutional layers, and encoder-only transformer).
- **Comparison Benchmarks**: DIA-NN (v1.8.1 and v1.9.2), Spectronaut (v14.6), DreamDIA, and Alpha-XIC.
- **Downstream**: Protein inference, FDR control (q-value < 0.01), and cross-run normalization using MaxLFQ-like algorithms.

## Results

### Main Findings
1. **Superior Identification**: DIA-BERT identified 51% more proteins and 22% more peptide precursors than DIA-NN in library-based modes, and 73% more proteins in library-free modes.
2. **Quantitative Accuracy**: Achieved average Spearman’s correlation coefficients of 0.94 for peptide quantification, matching or exceeding the precision of current benchmarks while offering lower CV values (4-9%).
3. **Data Volume Dependency**: Performance improved linearly with the log-scale increase of pre-training data volume, suggesting potential for further enhancement with even larger datasets.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Workflow of DIA-BERT (identification and quantification modules) and performance comparison on five human cancer datasets against DIA-NN. |
| Fig 2 | Quantification precision and benchmarking using three-species and mouse-yeast hybrid datasets, showing high correlation with theoretical ratios. |

## Discussion

### Strengths
- **Reduced Overfitting**: Pre-training on massive datasets prevents the overfitting common in tools that train models on individual MS files.
- **Information Feedback**: The end-to-end nature allows for a joint learning loop between representation and scoring.
- **User-Friendly**: Includes a graphical user interface (GUI) and standard CSV output.

### Limitations
- **Instrument Specificity**: Currently optimized for Orbitrap data; not yet fully optimized for timsTOF (which includes CCS values) or tripleTOF data.
- **Computational Requirements**: Requires GPU resources for both training and inference due to the processing of large volumes of raw spectra.

### Future Work
- **Expansion of Scope**: Extending the model to handle post-translational modifications (PTMs) and non-trypsin peptides.
- **Optimization**: Improving inference efficiency through model quantization and pruning; adapting the pipeline for TOF-based instruments.

## Personal Notes

- The use of synthetic data (via Synthedia) to train the quantification regression model is a clever way to provide "ground truth" labels that are otherwise unavailable in real MS files.
- The 51% increase in protein ID is massive, particularly for low-abundance proteins which are usually the "dark matter" of proteomics.

## Related Papers

- Demichev, V. et al. (2019). DIA-NN: neural networks and interference correction enable deep proteome coverage. *Nat. Methods*.
- Devlin, J. et al. (2019). BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. *NAACL-HLT*.
- Leeming, M. G. et al. (2023). Simulation of mass spectrometry-based proteomics data with Synthedia. *Bioinform. Adv.*