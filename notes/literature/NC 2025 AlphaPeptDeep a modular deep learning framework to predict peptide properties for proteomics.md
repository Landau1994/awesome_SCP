---
title: AlphaPeptDeep:a modular deep learning framework to predict peptide properties for proteomics
aliases:
   - AlphaPeptDeep
   - AlphaPeptDeep paper
   - Zeng et al. 2022
tags:
  - literature
  - paper
category: literature
date_created: 2023-10-25
Journal: Nature Communications
Year: 2022
authors:
  - Wen-Feng Zeng
  - Xie-Xuan Zhou
  - Sander Willems
  - Constantin Ammar
  - Maria Wahle
  - Isabell Bludau
  - Eugenia Voytik
  - Maximillian T. Strauss
  - Matthias Mann
---


# AlphaPeptDeep: a modular deep learning framework to predict peptide properties for proteomics

## Citation

> [!cite] Reference
> **Authors**: Wen-Feng Zeng, Xie-Xuan Zhou, Sander Willems, Constantin Ammar, Maria Wahle, Isabell Bludau, Eugenia Voytik, Maximillian T. Strauss & Matthias Mann
> **Year**: 2022
> **Journal**: Nature Communications
> **DOI**: https://doi.org/10.1038/s41467-022-34904-3

## Abstract

Machine learning, particularly deep learning (DL), has become essential in MS-based proteomics for predicting peptide properties like retention time (RT), ion mobility, and fragment intensities. However, integrating new architectures remains challenging for researchers. This paper introduces **AlphaPeptDeep**, a modular Python framework built on [[PyTorch]] that allows easy creation and training of DL models. A key feature is its ability to handle post-translational modifications (PTMs) generically and use transfer learning to refine models with small datasets. The study demonstrates that AlphaPeptDeep performs on par with existing tools while offering significant advantages in speed and flexibility. It specifically highlights the framework's utility in improving HLA peptide identification in both data-dependent (DDA) and data-independent acquisition (DIA) modes through a specialized HLA peptide prediction model.

## Key Points

- **Modular Framework**: AlphaPeptDeep is built on [[PyTorch]], offering a "model shop" that allows non-specialists to create and train models with minimal code.
- **PTM Handling & Transfer Learning**: The framework utilizes a generic method to embed PTMs and employs transfer learning (few-shot learning) to accurately predict properties for modified peptides (e.g., phosphorylation) without requiring massive training datasets.
- **HLA Peptide Identification**: A specialized model was developed to predict HLA peptides, significantly boosting identification rates in DDA open searches and enabling predicted spectral library generation for DIA analysis.
- **Performance & Speed**: The pre-trained MS2 model is roughly 40 times faster than the [[Prosit]]-Transformer model while maintaining comparable accuracy.

## Methods

### Sample Preparation
- **Method used**: [[LC-MS/MS]] (DDA, DIA, dda-PASEF).
- **Cell type**: [[HeLa]], [[U2OS]], [[RA957]] (HLA cell line), and model organisms ([[E. coli]], [[Yeast]], [[Drosophila]]).
- **Number of cells**: N/A (Peptide inputs derived from bulk lysates and synthetic libraries like [[ProteomeTools]]).

### Data Analysis
- **Software**: [[AlphaPeptDeep]], [[AlphaBase]], [[PyTorch]], [[AlphaPept]], [[MaxQuant]], [[Open-pFind]], [[DIA-NN]], [[Spectronaut]], [[DIA-Umpire]], [[PEAKS-Online]], [[DeepLC]].
- **Downstream**: [[Percolator]] rescoring, [[Transfer Learning]], Spectral Library Generation, HLA peptide prediction.

## Results

### Main Findings
1.  **High Accuracy with Low Overhead**: The MS2, RT, and CCS prediction models achieved high correlation with experimental data (PCC > 0.9 for MS2 intensities in 97% of PSMs). The models are lightweight (4M parameters for MS2 vs 64M in Prosit) and fast.
2.  **Robust PTM Prediction**: Using transfer learning, the models could accurately predict properties for peptides with various PTMs (e.g., phosphorylation, ubiquitylation) even when fine-tuned on as few as 10-50 peptides.
3.  **Improved HLA Analysis**: 
    - In **DDA**: Rescoring with AlphaPeptDeep improved HLA peptide identification by ~94% compared to standard searches and outperformed [[Prosit]] in coverage.
    - In **DIA**: A pipeline using predicted HLA spectral libraries identified significantly more unique HLA sequences compared to library-free approaches like [[DIA-Umpire]] and [[PEAKS-Online]].

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Overview of the AlphaPeptDeep framework, showing the encoding of peptide sequences/PTMs and the build/train/predict workflow. |
| Fig 2 | Architectures of the built-in pre-trained models for MS2 (Transformer-based), RT, and CCS (CNN + BiLSTM). |
| Fig 3 | Performance benchmarking of MS2, RT, and CCS models against datasets like [[ProteomeTools]] and [[HeLa]], showing high correlations. |
| Fig 4 | Demonstration of transfer learning performance on 21 different PTM types, showing significant accuracy improvements with few-shot training. |
| Fig 5 | Comparison of HLA peptide identification in DDA mode, showing AlphaPeptDeep drastically improves results over [[MaxQuant]] and [[Open-pFind]]. |
| Fig 6 | The HLA prediction model pipeline and its application to boosting HLA identification in [[DIA]] datasets (RA957). |

## Discussion

### Strengths
- **Flexibility**: Can handle arbitrary PTMs via composition-based embedding, unlike models restricted to specific modifications.
- **Accessibility**: Open-source, modular design allows users to swap NN architectures (LSTM, Transformer, CNN) easily.
- **Efficiency**: Significantly faster training and prediction times compared to current state-of-the-art models, running efficiently on consumer GPUs.

### Limitations
- **Overfitting Risk**: Like all DL models, standard issues such as overfitting need to be managed (though the framework includes fine-tuning safeguards).
- **Library Size**: For HLA DIA, the predicted library is limited to known binders to keep search space manageable, whereas DDA databases are larger.

### Future Work
- Expanding the application of the framework to other peptide property prediction problems.
- Further integration into the AlphaPept ecosystem for seamless end-to-end analysis.

## Personal Notes

## Related Papers

- [[AlphaPept]] - Strauss et al. (2021)
- [[Prosit]] - Gessulat et al. (2019)
- [[pDeep]] - Zhou et al. (2017)
- [[DeepLC]] - Bouwmeester et al. (2021)