---
title: FAVOR+
aliases:
  - Fast Attention Via positive Orthogonal Random features
  - FAVOR
tags:
  - tools
  - deep-learning
  - attention
  - efficient-transformer
category: concept
url: https://arxiv.org/abs/2009.14794
date_created: 2026-03-17
---

# FAVOR+

**Fast Attention Via positive Orthogonal Random features — a mechanism to approximate softmax attention with linear complexity $O(N)$, enabling Transformers to scale to very long sequences such as full gene expression vectors (20,000+ genes).**

## Overview

FAVOR+ was introduced as part of the [[Performer]] architecture (Choromanski et al., 2021). Standard [[Transformer]] self-attention has $O(N^2)$ complexity, making it infeasible for sequences with tens of thousands of elements. FAVOR+ replaces the softmax kernel with a random feature map using positive orthogonal random features, approximating the softmax kernel with positive random features. Unbiasedness of a kernel estimator does not by itself make the normalized attention ratio unbiased. Time and space scale linearly with $N$ when feature count and embedding dimensions are fixed.

## Key Ideas

- **Kernel Approximation**: Decomposes softmax attention into $\phi(Q) \cdot \phi(K)^T$ using random feature maps, avoiding explicit $N \times N$ attention matrix computation
- **Positive Features**: Uses positive random features to ensure non-negative attention weights, critical for stable training
- **Orthogonal Randomness**: Orthogonal random feature vectors reduce variance of the approximation compared to i.i.d. random features

## Complexity Comparison

| Mechanism | Time Complexity | Space Complexity |
|-----------|----------------|-----------------|
| Standard Attention | $O(N^2 d)$ | $O(N^2)$ |
| FAVOR+ | $O(N r d)$ | $O(Nr)$ |

Where $N$ = sequence length, $d$ = dimension, $r$ = number of random features (typically $r \ll N$).

## Application in SCP

In **scTranslator**, FAVOR+ enables the [[Transformer]] to process input sequences of ~20,000 genes without quadratic memory explosion, which is essential for whole-transcriptome-to-proteome translation.

## Key Publications

> [!cite] Primary Reference
> Choromanski K, Likhosherstov V, Dohan D, et al. (2021) *ICLR*
> DOI: [10.48550/arXiv.2009.14794](https://doi.org/10.48550/arXiv.2009.14794)

## Related Concepts

- [[Performer]] — The Transformer variant that implements FAVOR+
- [[Transformer]] — The base architecture FAVOR+ optimizes

## Source Check

- Source checked on 2026-10-20: [FAVOR+ documentation or source](https://arxiv.org/abs/2009.14794).
