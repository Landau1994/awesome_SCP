---
title: A pre-trained large generative model for translating single-cell transcriptomes to proteomes
aliases:
  - sctranslator
authors:
  - Linjing Liu
  - Wei Li
  - Fang Wang
  - Yiming Li
  - Long-Kai Huang
  - Ka-Chun Wong
  - Fan Yang
  - Jianhua Yao
year: 2025
journal: Nature Biomedical Engineering
doi: 10.1038/s41551-025-01528-z
url: https://doi.org/10.1038/s41551-025-01528-z
tags:
  - paper
  - AIVC
  - Single-cell
  - Proteomics
  - Transformer
  - Generative-Model
  - scp
status: unread
rating:
date_added: 2025-11-05
date_read:
---

# A pre-trained large generative model for translating single-cell transcriptomes to proteomes

## Quick Summary
> The authors propose **scTranslator**, a large-scale generative model based on the [[Transformer]] architecture, designed to translate single-cell transcriptomic data (scRNA-seq) into proteomic data. Inspired by the central dogma and natural language translation, the model uses a two-stage pre-training strategy on extensive paired bulk and single-cell datasets. It demonstrates superior performance over state-of-the-art methods in predicting protein abundance, handling unaligned features, and performing few-shot learning, while enabling downstream applications like perturbation prediction and gene regulatory network inference.

## Key Points
- **Architecture**: A customized encoder-decoder [[Transformer]] using [[FAVOR+]] attention for linear complexity and a non-autoregressive decoder for efficient generation.
- **Novel Embedding**: Introduces a **re-indexed Gene Positional Encoding (GPE)** module that maps gene IDs to vectors, preserving gene identity and enabling the model to handle unaligned data (genes/proteins not seen during fine-tuning).
- **Two-Stage Pre-training**:
    1.  **Bulk Stage**: Trained on ~18,000 paired bulk samples (31 cancer types) to learn general biological patterns.
    2.  **Single-Cell Stage**: Continual learning on ~2.4 million single cells (10 CITE-seq datasets) to capture cellular heterogeneity.
- **Versatility**: Validated across various modalities ([[CITE-seq]], [[REAP-seq]], [[NEAT-seq]], [[Spatial CITE-seq]]), tissues, and species (transfer from human to mouse).
- **Interpretability**: The attention mechanism allows for the inference of gene regulatory networks (GRNs) and protein-protein interactions (PPIs).

## Methods
### Data
- **Pre-training (Bulk)**: 72 datasets from [[TCGA]], [[CPTAC]], [[MSKCC]], and Broad Institute, comprising 18,227 patient-level samples across 31 cancer types.
- **Pre-training (Single-cell)**: 10 [[CITE-seq]] datasets comprising 2,405,115 cells from blood, bone marrow, brain, and liver.
- **Benchmarking & Validation**: Independent datasets including CITE-seq PBMCs, REAP-seq PBMCs, CITE-seq CBMCs, CITE-seq DCs, CITE-seq MCs, ECCITE-seq, Spatial CITE-seq, and Perturb-CITE-seq.

### Model Architecture
- **Backbone**: Encoder-Decoder [[Transformer]] structure.
- **Attention**: Utilizes **FAVOR+** (Fast Attention Via positive Orthogonal Random features) to reduce computational complexity from quadratic to linear ($O(N)$), accommodating sequence lengths up to 20,000 genes.
- **Embeddings**:
    - **Re-indexed GPE**: Converts NCBI Gene IDs into position vectors.
    - **Expression Embedding**: Projects scalar expression values into vectors.
- **Decoder**: Non-autoregressive generation (predicts all proteins in one forward pass) for efficiency.

### Training Strategy
- **Stage 1 (Bulk)**: Supervised learning on paired RNA/Protein bulk data to establish robust baselines (200 epochs).
- **Stage 2 (Single-cell)**: Continual learning on paired single-cell data to refine granular relationships (stopped when cosine similarity > 0.85).
- **Stage 3 (Inference/Fine-tuning)**:
    - **Fine-tuning**: Used for benchmarking (aligned/unaligned/few-shot modes).
    - **Zero-shot**: Direct prediction on unseen datasets (e.g., Pan-cancer analysis) without further gradient updates.
- **Loss Function**: Mean Squared Error ([[MSE]]).

## Results
| Metric | Value (scTranslator) | Baseline (Others) | Context |
|--------|----------------------|-------------------|---------|
| Cosine Similarity | > 0.98 | N/A | Bulk Test Set |
| Cosine Similarity | > 0.87 | N/A | Single-cell Test Set |
| Cosine Similarity | ~0.78 - 0.95 | ~0.2 - 0.7 | Few-shot learning (20 cells) vs Seurat/sciPENN |
| PCC | > 0.80 | < 0.70 | ECCITE-seq (Leave-one-batch-out) |
| PCC | > 0.90 | < 0.60 | Unaligned experiment (Dataset 1) |
| Accuracy | High consistency | Low consistency | Spatial CITE-seq generalization |

*Baselines include [[sciPENN]], [[cTP-net]], [[totalVI]], [[BABEL]], [[Seurat]].*

## Figures

| Figure | Description |
| ------ | ----------- |
| **Fig 1** | Overview of scTranslator architecture (Encoder-Decoder, GPE, FAVOR+), the three-stage framework (Bulk Pre-training -> SC Pre-training -> Inference), and downstream applications. |
| **Fig 2** | Performance evaluation on training/test sets for bulk and single-cell data. Shows high correlation (>0.98 bulk, >0.87 sc) and ablation studies confirming the benefit of the two-stage pre-training. |
| **Fig 3** | Systematic benchmarking against SOTA methods (sciPENN, cTP-net, etc.) in aligned, unaligned, and few-shot scenarios. scTranslator consistently outperforms, especially in few-shot settings. |
| **Fig 4** | Validation on independent datasets (ECCITE-seq, Mouse, Spatial, NEAT-seq) using "leave-one-type-out" strategies (batch, tissue, time). Demonstrates robustness across domains. |
| **Fig 5** | Interpretability and Perturbation analysis. Visualizes attention maps to infer regulatory networks. accurately predicts protein level changes after gene knockouts (e.g., STAT1, JAK1) compared to Perturb-CITE-seq ground truth. |
| **Fig 6** | Downstream applications: Pseudo-protein quantification improves cell clustering and batch correction. Application to a pan-cancer dataset for zero-shot prediction of 14,000 proteins to identify cell origin (Tumor vs Normal). |

## Critical Analysis
### Strengths
- **Scale and Generalization**: The massive pre-training corpus allows the model to generalize well to unseen datasets, tissues, and even species (mouse), which is a significant limitation in previous small-scale models.
- **Architecture Efficiency**: The use of FAVOR+ attention and re-indexed GPE solves the scalability issue of Transformers with high-dimensional single-cell data (20k genes).
- **Unaligned Capability**: Unlike many competitors, scTranslator can predict proteins not present in the training set (zero-shot) or fine-tune on datasets with different feature sets due to its gene-identity-aware embedding.
- **Perturbation Prediction**: Demonstrated ability to predict the impact of gene knockouts on protein levels in silico, potentially saving experimental costs.

### Weaknesses
- **Resource Intensity**: Pre-training required 32 GPUs for approximately one month, making it difficult for average labs to retrain or modify the core model from scratch.
- **Zero-shot Bias**: The authors acknowledge that zero-shot performance depends heavily on the diversity of the training data; biases in the training set (e.g., specific cancer types) could affect predictions on disparate biological contexts.
- **Experimental Validation**: While regulatory networks were inferred, wet-lab validation of novel findings (outside of literature comparison) is mentioned as a future step.

### Questions
- How does the model handle isoforms with identical or highly similar gene sequences but distinct functional protein products if the input is gene-level quantification? (Fig 2b suggests it handles CD45 isoforms well, likely via context from other genes).
- What is the impact of technical noise (dropout) in the input scRNA-seq on the zero-shot inference compared to fine-tuned models?

## Connections
### Related Papers
- **[[cTP-net]]**: A deep learning baseline for single-cell surface protein imputation.
- **[[sciPENN]]**: A method for protein prediction and integration.
- **[[totalVI]]**: Probabilistic modeling of single-cell multi-omics data.
- **[[Performer]]**: The source of the FAVOR+ mechanism used for linear attention.
- **[[Perturb-CITE-seq]]**: Source of the validation dataset for gene perturbation.

### Related Concepts
- [[Central Dogma]]: The biological flow of information (DNA -> RNA -> Protein) serving as the theoretical basis.
- [[Transfer Learning]]: The core ML strategy used (Bulk -> Single Cell).
- [[Zero-shot Learning]]: Predicting unseen labels/proteins.
- [[Spatial Transcriptomics]]: Validated generalization to spatial data.

### Potential Applications
- **In silico drug screening**: Predicting protein responses to gene perturbations without physical experiments.
- **Data Augmentation**: Enhancing scRNA-seq datasets with predicted proteomes for better cell typing.
- **Pan-cancer Analysis**: Identifying cell origins and biomarkers in large-scale public datasets where proteomics is absent.

## Notes
- The use of "re-indexed GPE" is a clever adaptation of Positional Encodings from NLP. Instead of word order, it encodes Gene ID, effectively treating the "order" as a semantic identity in the lookup table.
- The perturbation results (Fig 5) are particularly impressive, showing high correlation with ground truth despite the model only seeing control data during fine-tuning.
