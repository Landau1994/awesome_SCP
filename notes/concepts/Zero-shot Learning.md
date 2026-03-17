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
---

# Zero-shot Learning

**A machine learning paradigm where a model makes predictions on classes or tasks it has never seen during training, relying on learned representations and auxiliary information to generalize beyond the training distribution.**

## Overview

In zero-shot learning, the model must predict labels or outputs for which no training examples were provided. This is possible when the model learns a generalizable representation space that captures the underlying structure of the problem. In NLP, zero-shot capability is a hallmark of large language models. In computational biology, it enables prediction on new genes, proteins, or tissues not in the training set.

## Types

| Type | Description |
|------|-------------|
| **Standard Zero-shot** | No target-domain training data at all |
| **Generalized Zero-shot** | Test set includes both seen and unseen classes |
| **Few-shot** | Very small number of target examples (1–20) |

## Application in SCP

scTranslator achieves zero-shot protein prediction through its **re-indexed Gene Positional Encoding (GPE)** module, which maps NCBI Gene IDs to embedding vectors. This gene-identity-aware design allows the model to:

- Predict proteins not present in the fine-tuning dataset
- Apply to entirely new datasets without gradient updates (e.g., pan-cancer analysis predicting 14,000 proteins)
- Generalize across tissues and species (human → mouse)

## Related Concepts

- [[Transfer Learning]] — Broader paradigm; zero-shot is an extreme case
- [[Transformer]] — Architecture enabling zero-shot via learned representations
