---
title: Zero-shot Learning
aliases:
  - zero-shot
  - zero-shot inference
tags:
  - concept
  - machine-learning
  - deep-learning
category: concept
date_created: 2026-03-17
url: https://arxiv.org/abs/1707.00600
---

# Zero-shot Learning

**A machine learning paradigm where a model makes predictions on classes or tasks it has never seen during training, relying on learned representations and auxiliary information to generalize beyond the training distribution.**

## Overview

In classical zero-shot classification, the target classes lack labeled training examples, and auxiliary information connects them to learned representations. In model applications, zero-shot may instead mean using a pretrained model on a new dataset without target-specific parameter updates. Reports should specify which meaning is intended; this does not by itself show that every gene, tissue or species was absent from pretraining.

## Types

| Type | Description |
|------|-------------|
| **Standard Zero-shot** | No target-domain training data at all |
| **Generalized Zero-shot** | Test set includes both seen and unseen classes |


## Application in SCP

scTranslator reports applications to new datasets using gene-aware representations. The absence of target-specific fine-tuning must be distinguished from absence of the gene or protein from pretraining. Its reported pan-cancer and cross-species evaluations should be interpreted using the original train/test splits; they are not a guarantee of arbitrary unseen-protein prediction.

Few-shot learning uses a small number of target examples and is a separate setting, not a type of zero-shot learning.

## Related Concepts

- [[Transfer Learning]] — Broader paradigm; zero-shot is an extreme case
- [[Transformer]] — Architecture enabling zero-shot via learned representations

## Sources

- [Xian et al.: zero-shot learning evaluation](https://arxiv.org/abs/1707.00600)
- [scTranslator official repository](https://github.com/TencentAILabHealthcare/sctranslator)
