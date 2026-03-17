---
title: Navigating the data processing for cytometry-based single-cell proteomics
authors:
  - Huaicheng Sun
  - Yuan Zhou
  - Ruoyu Jiang
  - Yuxuan Liu
  - Chengbin Gu
  - Ziqi Pan
  - Minjie Mou
  - Xichen Lian
  - Bohan Chen
  - Tianle Niu
  - Ying Zhang
  - Yintao Zhang
  - Baoliang Zhang
  - Xiuna Sun
  - Hao Yang
  - Xin Shen
  - Yangbo Dai
  - Jiannan Deng
  - Siqi Liu
  - Yang Zhang
  - Mang Xiao
  - Wanqing Xie
  - Qingxia Yang
  - Tingting Fu
  - Feng Zhu
aliases:
   - ANPELA
   - Single-cell proteomics data processing
tags:
  - literature
  - paper
  - SCP
  - Proteomics
  - Cytometry
category: literature
date_created: 2024-05-23
Journal: Nature Protocols
Year: 2026
DOI: 10.1038/s41596-025-01257-2
---

# Navigating the data processing for cytometry-based single-cell proteomics

## Citation

> [!cite] Reference
> **Title**：Navigating the data processing for cytometry-based single-cell proteomics
> **Authors**: Huaicheng Sun, Yuan Zhou, Ruoyu Jiang, et al.
> **Year**: 2026
> **Journal**: Nature Protocols
> **DOI**: 10.1038/s41596-025-01257-2

## Abstract

基于细胞计数的单细胞蛋白质组学（SCP）已成为深入理解复杂生物系统的重要技术。虽然目前已开发出多种处理此类数据的方法，但为特定数据集确定表现最佳的处理工作流仍极具挑战。本研究开发了 **ANPELA**，一种开箱即用的方法，用于通过大规模筛选导航蛋白质组数据处理。它能够通过机器学习系统评估数千种处理工作流在识别细胞亚群（CSI）和推断伪时间轨迹（PTI）方面的性能。ANPELA 提供了桌面软件、R 包和在线服务器，具备多场景可用性、数据安全性和用户友好界面。该工具可供包括无编程基础在内的广泛受众使用，旨在帮助研究人员从 SCP 研究中获取可靠的生物学见解。

## Key Points

- **大规模筛选导航**：ANPELA 可以自动生成并筛选超过 3000 种数据处理工作流组合，涵盖了补偿（Compensation）、转换（Transformation）、标准化（Normalization）和信号清洗（Signal clean）四个关键步骤。
- **多维度评估体系**：针对细胞亚群识别（CSI）和伪时间轨迹推断（PTI）两项核心任务，分别建立了包含准确性、紧凑性、鲁棒性和对应性等指标的综合评价体系。
- **全平台支持与安全性**：提供 GUI 桌面版（无需编程基础）、在线 Web 端和开源 R 包（支持并行计算），且本地运行模式确保了用户私有数据的安全性。

## Methods

### 实验设计与数据准备
- **输入数据**：必须包含流式细胞术标准（FCS）文件和元数据（metadata.csv）。对于 CSI 分析，至少需要两个实验条件；对于 PTI 分析，至少需要两个时间点。
- **基准数据集**：使用了 10 个具有代表性的 cytometry-based SCP 数据集进行验证，涵盖了不同的检测技术（如 TOF, APD, PMT）和研究类型。
- **细胞数量要求**：建议每个 FCS 文件至少包含 200 个细胞，以确保评估结果（尤其是鲁棒性）的可靠性。

### 数据分析与工作流筛选
- **软件工具**：ANPELA (Web/Desktop/R package)。
- **处理步骤**：
    1. **数据补偿**（如 AutoSpill, FlowCore 等 7 种方法）。
    2. **数据转换**（如 Arcsinh, Logicle 等 16 种方法）。
    3. **数据标准化**（如 GaussNorm, WarpSet 等 7 种方法）。
    4. **信号清洗**（如 FlowAI, FlowClean 等 5 种方法）。
- **性能评估指标**：
    - **CSI**：Accuracy (AUC), Tightness (Silhouette coefficient), Robustness, Correspondence。
    - **PTI**：Conformance (Time conformance score), Smoothness, Robustness, Correspondence。
- **下游分析方法**：CSI 可选 FlowSOM, PhenoGraph；PTI 可选 Slingshot, SCORPIUS 等。

## Results

### Main Findings
1. **工作流表现的数据依赖性**：研究发现，在某一数据集上表现优异的工作流在另一数据集上可能表现不佳，证明了为特定研究筛选最优工作流的必要性。
2. **CSI 分析优化**：通过 ANPELA 筛选出的排名第一的工作流（如 `NON+LGT+MEA+FCU`）能比排名靠后或默认方法显著降低细胞分类的错误率（案例中错误率从 22.2% 降至 16.4%）。
3. **PTI 轨迹还原**：最优工作流能准确还原小鼠胚胎干细胞分化为三个胚层的复杂轨迹，而性能差的工作流会完全掩盖生物学背景，甚至导致错误的生物学结论。

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | **ANPELA 架构示意图**：展示了从原始数据输入、四个处理步骤的组合筛选，到最终 CSI 和 PTI 性能评估的完整流程。 |
| Fig 2 | **方案操作流程概览**：对比了基于 GUI 的程序 1 和基于 R 包的程序 2 的步骤及预期耗时。 |
| Fig 3 | **多标准性能评估体系**：详细描述了 CSI（准确性、紧密性等）和 PTI（一致性、平滑度等）各维度的评估逻辑。 |
| Fig 4 | **CSI 案例分析结果**：通过降维图、Sankey 图展示了不同排名工作流在识别 PBMC 亚群中的表现差异。 |
| Fig 5 | **PTI 轨迹推断案例**：展示了不同工作流在还原 mESC 分化路径时的准确度差异。 |

## Discussion

### Strengths
- **全面性**：目前唯一涵盖了从预处理到评估全流程且提供超过 3000 种工作流筛选的工具。
- **易用性**：GUI 版本极大地降低了生物学家和临床医生的使用门槛；R 包版本则为数据科学家提供了灵活性。
- **透明度**：所有代码开源，评估指标均基于已发表的成熟算法，结果可复现且具有可解释性。

### Limitations
- **计算耗时**：筛选数千个工作流可能需要几十分钟到数小时，具体取决于数据量和硬件配置。
- **系统限制**：目前桌面版本仅支持 Windows 操作系统。
- **潜在偏倚**：某些评估指标（如 Ca accuracy）可能在检测极细微表型差异时存在偏倚，需结合生物学背景解读。

### Future Work
- **领域扩展**：计划将 ANPELA 的方法论扩展到空间蛋白质组学（Spatial Proteomics）等新兴的高维数据领域。
- **算法更新**：持续集成新开发的预处理算法和下游分析工具，保持协议的先进性。

## Personal Notes
- 该协议强调了单细胞数据预处理中“数据依赖性”的重要性，即没有一种通用的最佳处理方法。
- ANPELA 的引入使得数据处理从“盲目尝试”转向了“定量评估驱动的科学选择”。

## Related Papers

- Zhang, Y. et al. *Adv. Sci.* **10**, e2207061 (2023). (ANPELA 的早期版本和性能基准)
- Van Gassen, S. et al. *Cytom. A* **87**, 636–645 (2015). (FlowSOM 算法)
- Ji, Z. & Ji, H. *Nucleic Acids Res.* **44**, e117 (2016). (TSCAN/PTI 相关)