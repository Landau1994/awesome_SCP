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
url: https://doi.org/10.48550/arXiv.2009.14794
date_created: 2026-03-17
---

# Performer

**A Transformer architecture variant that uses [[FAVOR+]] (Fast Attention Via positive Orthogonal Random features) to achieve linear-complexity attention, enabling efficient processing of very long sequences.**

## Overview

The Performer (Choromanski et al., 2021) addresses the quadratic scaling bottleneck of standard [[Transformer]] self-attention. By replacing the softmax attention kernel with [[FAVOR+]] random feature approximation, it achieves $O(N)$ time and memory complexity while maintaining competitive accuracy. This makes it suitable for domains with very long sequences, such as genomics (thousands of genes) and protein sequences.

## Key Features

- **Linear Attention**: $O(N)$ time and space complexity via FAVOR+ kernel approximation
- **Drop-in Replacement**: Can replace standard attention in any Transformer architecture
- **Unbiased Estimation**: Provides an unbiased approximation of softmax attention
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
