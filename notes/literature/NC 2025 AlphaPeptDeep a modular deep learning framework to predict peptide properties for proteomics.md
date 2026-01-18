---
title: NC 2025 AlphaPeptDeep a modular deep learning framework to predict peptide properties for proteomics
aliases:
  - <article>
  - <paper>
  - <literature>
tags:
  - literature
  - paper
category: literature
date_created: 2026-01-18
Journal: Nature Communications
Year: "2025"
---
# AlphaPeptDeep: a modular deep learning framework to predict peptide properties for proteomics

## Citation

> [!cite] Reference
> **Authors**: Wen-Feng Zeng, Xie-Xuan Zhou, Sander Willems, Constantin Ammar, Maria Wahle, Isabell Bludau, Eugenia Voytik, Maximillian T. Strauss & Matthias Mann
> **Year**: 2022
> **Journal**: Nature Communications
> **DOI**: 10.1038/s41467-022-34904-3

## Abstract

Machine learning and deep learning (DL) are becoming essential in mass spectrometry-based proteomics for predicting peptide properties such as retention time, ion mobility, and fragment intensities. However, integrating new architectures is challenging for researchers. The authors introduce AlphaPeptDeep, a modular Python framework built on PyTorch that predicts peptide properties with high accuracy. It features a "model shop" for easy creation of models, generic handling of post-translational modifications (PTMs), and extensive use of transfer learning to reduce data requirements. The framework demonstrates performance on par with existing tools and significantly improves HLA peptide identification in data-independent acquisition (DIA) workflows.

## Key Points

- Introduces **AlphaPeptDeep**, a modular framework based on [[PyTorch]] for predicting peptide properties (RT, CCS, MS2 intensities).
- Utilizes [[Transformer]] models for MS2 prediction and [[LSTM]]/[[CNN]] architectures for RT and CCS prediction.
- Features a generic embedding strategy that supports arbitrary post-translational modifications ([[PTMs]]).
- Implements transfer learning to refine models with small datasets (few-shot learning) for specific experimental conditions or rare PTMs.
- Demonstrates a specialized pipeline for [[HLA]] peptide prediction that improves identification in [[DIA]] (data-independent acquisition) datasets.

## Methods

### Sample Preparation
- Method used: Validation performed on public datasets involving [[Trypsin]], [[LysC]], [[Chymotrypsin]], and [[GluC]] digests.
- Cell type: [[HeLa]] (general benchmarks), [[U2OS]] (phosphoproteomics), [[RA957]] (HLA analysis).
- Number of cells: N/A (Computational study utilizing MS raw data).

### Data Analysis
- Software: [[AlphaPeptDeep]], [[AlphaBase]], [[PyTorch]], [[MaxQuant]], [[pFind]] (open search), [[DIA-NN]], [[Spectronaut]], [[Prosit]], [[DeepLC]].
- Downstream: [[Percolator]] (integrated for semi-supervised rescoring), [[AlphaViz]] (visualization).

## Results

### Main Findings
1. **High Prediction Accuracy**: The MS2 prediction model (Transformer-based) is significantly faster (40x) and smaller than comparable models like Prosit-Transformer while maintaining high accuracy (PCC > 0.9 for 97% of PSMs on ProteomeTools data).
2. **Transfer Learning Efficacy**: Transfer learning with as few as 10 to 50 peptides significantly improved prediction accuracy for rare or complex PTMs (improving PCC > 0.9 rates from ~48% to ~87%).
3. **HLA Identification**: A dedicated HLA prediction pipeline reduced the search space for DIA analysis, outperforming standard DDA library generation and existing tools like PEAKS Online and DIA-Umpire in identifying unique HLA sequences.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Overview of the AlphaPeptDeep framework, showing encoding, model building blocks (Transformers, LSTM), and the training/prediction workflow. |
| Fig 2 | Architectures of the pre-trained models: MS2 (Transformer-based), RT (CNN + BiLSTM), and CCS (CNN + BiLSTM). |
| Fig 3 | Performance benchmarks showing high correlation (PCC/R2) for MS2, RT, and CCS predictions across various datasets (ProteomeTools, HeLa, timsTOF). |
| Fig 4 | Demonstration of transfer learning performance on 21 different PTMs, showing significant accuracy gains with few-shot training. |
| Fig 5 | Comparison of HLA peptide identification in DDA data, showing AlphaPeptDeep improves results over MaxQuant and Prosit, especially in open-search modes. |
| Fig 6 | The HLA prediction pipeline for DIA analysis, illustrating the reduction of the search space and superior identification performance compared to other methods. |

## Discussion

### Strengths
- **Modularity**: The framework allows users to easily build, train, and refine models using a "model shop" concept.
- **Flexibility**: Uniquely handles arbitrary PTMs via composition-based embedding, unlike tools restricted to specific modifications.
- **Efficiency**: Models are lightweight and fast, enabling training and prediction on standard hardware (including CPUs).

### Limitations
- **Overfitting**: Standard DL risks like overfitting remain; users must carefully manage data splitting and hyperparameters (though the "model shop" provides robust baselines).
- **Data Dependency**: While transfer learning helps, the highest accuracy still relies on the availability of some representative experimental data for fine-tuning.

### Future Work
- The framework is designed to be a community resource, encouraging the development of new models for various proteomic properties.
- Potential integration into more search engines to support predicted libraries natively for DDA.

## Personal Notes

## Related Papers

- [[Prosit]] (Gessulat et al., 2019) - Deep learning for MS2 prediction.
- [[pDeep]] (Zhou et al., 2017) - Predecessor model using BiLSTM.
- [[DeepLC]] (Bouwmeester et al., 2021) - Retention time prediction.
- [[AlphaPept]] (Strauss et al., 2021) - The ecosystem this framework integrates with.