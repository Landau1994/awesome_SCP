---
title: Transformer
aliases:
  - Transformer architecture
  - Transformer model
tags:
  - tools
  - deep-learning
  - architecture
  - attention
category: concept
url: https://doi.org/10.48550/arXiv.1706.03762
date_created: 2026-03-17
---

# Transformer

**A neural network architecture based entirely on self-attention mechanisms, replacing recurrence and convolutions. It has become the dominant architecture in NLP, computer vision, and increasingly in computational biology including single-cell analysis.**

## Overview

The Transformer was introduced by Vaswani et al. (2017) in "Attention Is All You Need." Its core innovation is the **self-attention mechanism**, which computes pairwise relationships between all elements in a sequence in parallel, enabling long-range dependency modeling. The encoder-decoder structure has been adapted for diverse tasks beyond NLP, including protein language models (ESM), single-cell foundation models (scGPT, Geneformer), and multi-omics translation (scTranslator).

## Key Components

- **Self-Attention**: Computes Query-Key-Value attention scores: $\text{Attention}(Q,K,V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$
- **Multi-Head Attention**: Multiple parallel attention heads capture different relationship patterns
- **Positional Encoding**: Injects sequence position information (sinusoidal or learned)
- **Feed-Forward Network**: Two-layer MLP applied independently to each position
- **Layer Normalization**: Stabilizes training dynamics

## Architecture Variants

| Variant | Type | Use Case |
|---------|------|----------|
| Encoder-only | BERT, ESM | Classification, embeddings |
| Decoder-only | GPT | Autoregressive generation |
| Encoder-Decoder | Original, scTranslator | Sequence-to-sequence translation |

## Complexity

- **Standard Attention**: $O(N^2)$ time and space — quadratic in sequence length
- **Linear Attention**: [[FAVOR+]] ([[Performer]]) reduces to $O(N)$ via kernel approximation

## Key Publications

> [!cite] Primary Reference
> Vaswani A, Shazeer N, Parmar N, et al. (2017) *NeurIPS*
> DOI: [10.48550/arXiv.1706.03762](https://doi.org/10.48550/arXiv.1706.03762)

## Related Concepts

- [[FAVOR+]] — Linear attention approximation for efficient Transformers
- [[Performer]] — Transformer variant using FAVOR+ attention
- [[Transfer Learning]] — Common training paradigm for Transformer models
