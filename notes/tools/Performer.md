---
title: Performer
aliases:
  - Performer model
tags:
  - tools
  - deep-learning
  - efficient-transformer
  - attention
category: concept
url: https://arxiv.org/abs/2009.14794
date_created: 2026-03-17
---

# Performer

**A Transformer architecture variant that uses [[FAVOR+]] (Fast Attention Via positive Orthogonal Random features) to achieve linear-complexity attention, enabling efficient processing of very long sequences.**

## Overview

The Performer (Choromanski et al., 2021) addresses the quadratic scaling bottleneck of standard [[Transformer]] self-attention. By replacing the softmax attention kernel with [[FAVOR+]] random feature approximation, it achieves $O(N)$ time and memory complexity while maintaining competitive accuracy. This makes it suitable for domains with very long sequences, such as genomics (thousands of genes) and protein sequences.

## Key Features

- **Linear Attention**: $O(N)$ scaling in sequence length at fixed feature count and dimensions via FAVOR+ approximation
- **Drop-in Replacement**: Can be used in Transformer architectures, with implementation and approximation choices requiring validation
- **Approximation Guarantees**: The paper distinguishes unbiased or nearly unbiased estimators; normalized softmax attention should not be described as universally unbiased.
- **Backward Compatible**: Supports both causal (autoregressive) and bidirectional attention

## Application in SCP

scTranslator adopted the Performer's FAVOR+ mechanism to handle input sequences of ~20,000 genes in its encoder-decoder architecture for transcriptome-to-proteome translation, which would be infeasible with standard quadratic attention.

## Key Publications

> [!cite] Primary Reference
> Choromanski K, Likhosherstov V, Dohan D, et al. (2021) "Rethinking Attention with Performers" *ICLR 2021*
> DOI: [10.48550/arXiv.2009.14794](https://doi.org/10.48550/arXiv.2009.14794)

## Related Concepts

- [[FAVOR+]] — The specific attention mechanism used in Performer
- [[Transformer]] — The base architecture Performer optimizes
- [[Transfer Learning]] — Common training paradigm for Performer models

## Source Check

- Source checked on 2026-10-20: [Performer documentation or source](https://arxiv.org/abs/2009.14794).
