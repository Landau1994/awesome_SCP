---
title: minProb
aliases: ["MinProb"]
tags:
date_created: 2026-03-25
url: https://rformassspectrometry.github.io/MsCoreUtils/reference/imputation.html
category: concept
---

# minProb

## Summary

MinProb imputes left-censored missing values by drawing random values from a distribution centered on a low intensity quantile. It is appropriate only when a low-abundance, missing-not-at-random mechanism is a defensible assumption. Imputation can affect downstream statistical results and should be evaluated against the experimental design.

## Notes

- Imputes missing values from a low-intensity distribution tail.
- Commonly applied before differential abundance analysis.

## References

- MinProb and Perseus-style downshifted-normal imputation are related approaches but are not automatically identical implementations.

## Related

- [[Perseus]]
- [[WGCNA]]

## Sources

- [MsCoreUtils: imputation methods](https://rformassspectrometry.github.io/MsCoreUtils/reference/imputation.html)
