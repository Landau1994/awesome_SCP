---
title: MSE
aliases:
  - Mean Squared Error
  - mean squared error
tags:
  - concept
  - machine-learning
  - loss-function
  - metric
category: concept
date_created: 2026-03-17
---

# MSE

**Mean Squared Error — a standard regression loss function that measures the average of the squared differences between predicted and actual values. Widely used as a training objective in continuous-valued prediction tasks.**

## Definition

$$\text{MSE} = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2$$

Where $y_i$ = true value, $\hat{y}_i$ = predicted value, $n$ = number of samples.

## Properties

- **Non-negative**: Always ≥ 0; equals 0 only for perfect predictions
- **Differentiable**: Smooth gradient for backpropagation
- **Penalizes large errors**: Squared term amplifies outlier deviations
- **Scale-dependent**: Sensitive to the scale of the target variable

## Application in SCP

scTranslator uses MSE as the loss function for training its [[Transformer]] encoder-decoder to predict protein abundance values from gene expression inputs. The continuous nature of protein quantification (as opposed to discrete classification) makes MSE a natural choice.

## Related Metrics

| Metric | Formula | Notes |
|--------|---------|-------|
| **MSE** | $\frac{1}{n}\sum(y-\hat{y})^2$ | Training loss |
| **RMSE** | $\sqrt{\text{MSE}}$ | Same units as target |
| **MAE** | $\frac{1}{n}\sum|y-\hat{y}|$ | Robust to outliers |
| **Cosine Similarity** | $\frac{y \cdot \hat{y}}{||y|| \cdot ||\hat{y}||}$ | Direction agreement |
| **PCC** | Pearson correlation | Linear association |

## Related Concepts

- [[Transformer]] — Architecture trained with MSE loss in scTranslator
