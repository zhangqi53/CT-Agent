# CT-Agent MCP 工具包设计

> 版本: 0.2 | 日期: 2025-03-25
>
> 本文档定义 CT 智能体 benchmark 所需的全部 MCP 工具，
> 以及每个工具背后对应的**开源项目选型**。
>
> 智能体在执行任务时，需要**自主决定**调用哪些工具、以什么顺序调用——
> 这正是 benchmark 要评测的核心能力。

---

## 1. 设计原则

| 原则 | 说明 |
|------|------|
| **原子化** | 每个工具只做一件事，复杂任务由智能体自主编排 |
| **无状态** | 工具不保存中间状态，所有数据通过输入/输出显式传递 |
| **标准 MCP** | 符合 MCP Tool 协议（name / description / inputSchema / outputSchema） |
| **可测评** | 输入输出可被 benchmark harness 拦截和评分 |
| **含干扰项** | 包含不该被选用的干扰工具，测试工具选择能力 |

---

## 2. 七层架构

```
┌─────────────────────────────────────────────────────────┐
│  L7  输出层        报告生成 · FHIR导出 · 关键发现告警      │
├─────────────────────────────────────────────────────────┤
│  L6  推理层        分类判断 · 分期分级 · 鉴别诊断          │
├─────────────────────────────────────────────────────────┤
│  L5  融合层        跨模态证据聚合 · 模态置信度归因          │
├─────────────────────────────────────────────────────────┤
│  L4  定量层        三径测量 · 体积计算 · CT值统计 · 变化率   │
├─────────────────────────────────────────────────────────┤
│  L3  感知层        异常筛查 · 病灶检测 · 病灶分割 · 解剖分割 │
├─────────────────────────────────────────────────────────┤
│  L2  文本层        NER抽取 · 关系抽取 · 数值抽取 · 时序对齐  │
├─────────────────────────────────────────────────────────┤
│  L1  预处理层      DICOM解析 · 窗宽窗位 · 配准 · 质量评估    │
└─────────────────────────────────────────────────────────┘
```

---

## 3. MCP 工具清单与开源项目选型

### 3.1 L1 预处理层

| ID | 工具名 | 功能 | 首选项目 | 备选 | 说明 |
|----|--------|------|---------|------|------|
| P01 | `dicom_loader` | 加载 DICOM → 标准化 3D 体积（LPS+ 方向、HU 校准） | **SimpleITK** `ImageSeriesReader` | pydicom | SimpleITK 一个调用完成方向归一化+重采样；pydicom 用于元数据级访问 |
| P02 | `window_level` | 窗宽窗位变换（预设 / 自定义 WW/WL） | **MONAI** `ScaleIntensityRange` | SimpleITK `IntensityWindowing` | MONAI 内置常见 CT 预设，callable 模式易包装 |
| P03 | `image_registration` | 刚性 / 仿射 / 形变配准（纵向对比用） | **ANTsPy** `ants.registration()` | SimpleITK `ImageRegistrationMethod` | ANTsPy SyN 是医学配准金标准，单函数调用 |
| P04 | `scan_quality_check` | 伪影 / 噪声 / 层厚 / 对比剂时相评估 | **MONAI** `DataAnalyzer` + 自定义规则 | TorchIO 强度统计 | 暂无专用开源工具，需基于 MONAI 统计模块 + 规则引擎组装 |

### 3.2 L2 文本层

| ID | 工具名 | 功能 | 首选项目 | 备选 | 说明 |
|----|--------|------|---------|------|------|
| T01 | `clinical_signal_extractor` | 从病历文本提取异常临床信号 | **medspaCy** | scispaCy | 规则 + ConText 否定检测，适合临床信号筛查 |
| T02 | `report_ner` | 从 CT 报告抽取病灶实体（位置/大小/形态/密度） | **RadGraph-XL** (Stanford AIMI) | medspaCy TargetMatcher | RadGraph-XL 是少数**在 CT 报告上训练过**的 NER/RE 模型（ACL 2024） |
| T03 | `classification_label_extractor` | 从文本抽取分类标签及证据 | **NegBio** + RadLex 术语表 | CheXbert（胸部限定） | NegBio 否定/不确定检测是模态无关的；CheXbert 仅覆盖 14 个 CXR 观察项 |
| T04 | `measurement_extractor` | 从报告抽取测量数值（"3.2 × 2.1 cm 肿块"） | **llm_extractinator** (DIAG Nijmegen) | medspaCy 正则规则 | 在 CT 胸腹报告上验证过 RECIST 测量抽取，准确率 93.7% |
| T05 | `temporal_report_aligner` | 多份时序报告对齐与变化抽取 | **llm_extractinator** 纵向管线 | — | 唯一在纵向 CT 报告对上验证过的开源工具（arXiv 2025） |

### 3.3 L3 感知层

| ID | 工具名 | 功能 | 首选项目 | 备选 | 说明 |
|----|--------|------|---------|------|------|
| V01 | `abnormality_screening` | 全局二分类：正常 vs 异常 | **MONAI** 分类网络 (DenseNet121/ViT) | — | 无专用项目，用 MONAI 3D 分类器 + 预训练权重微调 |
| V02 | `lesion_detection` | 3D 病灶检测 → bbox | **nnDetection** (DKFZ) | MONAI Detection (RetinaNet) | nnDetection 自配置，LUNA16 等多个挑战赛冠军 |
| V03 | `lesion_segmentation` | 3D 病灶体素级分割 | **nnU-Net v2** (DKFZ) | SAM-Med3D / MedSAM2 | nnU-Net 是医学分割金标准；SAM-Med3D 适合交互式 prompt 分割 |
| V04 | `anatomy_segmentation` | 多器官 / 解剖结构分割（117 类） | **TotalSegmentator** | MONAI Auto3DSeg | 一个命令分割 117 个解剖结构，Radiology 2023 发表 |

### 3.4 L4 定量层

| ID | 工具名 | 功能 | 首选项目 | 备选 | 说明 |
|----|--------|------|---------|------|------|
| Q01 | `lesion_measurement` | 三径测量 + 体积 + CT 值统计 | **MONAI VISTA3D** + pyradiomics | MedSAM2 (RECIST→3D) | VISTA3D 分割后用 pyradiomics 提取形状和密度特征 |
| Q02 | `volume_change_calculator` | 两时间点体积 / 径线变化率 | **自建**（基于 Q01 + P03 输出计算） | — | 纯数值计算，无需专用项目 |
| Q03 | `recist_evaluator` | RECIST 1.1 治疗响应评估 | **detect-then-track** (alibool) | ULS23 (DIAG Nijmegen) | 唯一端到端 RECIST 评估开源管线（JIMM 2025），肝脏验证 |

### 3.5 L5 融合层

| ID | 工具名 | 功能 | 首选项目 | 备选 | 说明 |
|----|--------|------|---------|------|------|
| F01 | `multimodal_evidence_fusion` | 聚合影像特征 + 文本证据 → 融合置信度 | **自建**（LLM 推理链） | — | 无成熟开源项目；由 LLM 基于各工具输出做结构化推理 |
| F02 | `modality_attribution` | 各模态对结论的贡献度分析 | **自建**（LLM 推理链） | — | 同上，由 LLM 输出归因分析 |

### 3.6 L6 推理层

| ID | 工具名 | 功能 | 首选项目 | 备选 | 说明 |
|----|--------|------|---------|------|------|
| R01 | `malignancy_classifier` | 良恶性及亚型分类 | **肺**: AI-in-Lung-Health (fitushar) | **肝**: T-CACE (xiaojiao929) | 肺结节多数据集验证 AUC 0.71-0.90；肝脏无造影剂方案 |
| R02 | `staging_engine` | TNM / Lung-RADS / LI-RADS 分期 | **tnm-stage-classifier** (tatonetti-lab) | — | BERT 系 NLP 分期（Nature Comms）；⚠️ 影像分期无开源方案，Lung-RADS/LI-RADS 是已知空白 |
| R03 | `differential_diagnosis` | 鉴别诊断列表 + 支持/反对证据 | **RadFM** (chaoyi-wu) | LLaVA-Med (Microsoft) | RadFM 支持 3D CT 直接输入，Nature Comms 2025；LLaVA-Med 仅 2D |

### 3.7 L7 输出层

| ID | 工具名 | 功能 | 首选项目 | 备选 | 说明 |
|----|--------|------|---------|------|------|
| O01 | `report_generator` | 四段式结构化影像报告生成 | **FORTE/BrainGPT** (charlierabea) | RaDialog | FORTE 从 3D CT 生成报告（Nature Comms 2025），目前仅脑部；体部报告是空白 |
| O02 | `fhir_exporter` | 结构化报告 → HL7 FHIR 格式 | **自建**（JSON 模板映射） | — | 纯格式转换，无需 ML 模型 |
| O03 | `critical_finding_alert` | 紧急 / 偶发关键发现分级告警 | **TotalSegmentator** + 阈值规则 | INFORM-CT（未开源） | 通过解剖测量触发告警（如主动脉直径 > 阈值）；INFORM-CT 最直接但代码未公开 |
| O04 | `report_quality_scorer` | 报告质量自评 | **自建**（LLM 评分） | — | 用 LLM 按结构化 rubric 评分 |

### 3.8 辅助工具

| ID | 工具名 | 功能 | 首选项目 | 说明 |
|----|--------|------|---------|------|
| U01 | `medical_knowledge_lookup` | 查询分期标准 / 指南 / 鉴别要点 | **自建** RAG 或知识表 | 静态知识库，不需要 ML |
| U02 | `body_region_classifier` | 自动识别 CT 覆盖的身体部位 | **TotalSegmentator** 输出推断 | 根据分割到的解剖结构判断部位 |
| U03 | `dicom_metadata_reader` | 读取 DICOM 元数据 | **pydicom** | 纯元数据读取 |

---

## 4. 干扰工具（Distractor Tools）

这些工具故意包含在工具包中，智能体**不应选用**它们。用于测试工具选择能力。

| ID | 工具名 | 伪描述 | 干扰类型 |
|----|--------|--------|---------|
| D01 | `mri_lesion_detection` | 在 MRI 序列中检测病灶 | **模态错误**：本系统只处理 CT |
| D02 | `xray_abnormality_screen` | 对 X 光片进行异常筛查 | **模态错误**：不是 CT |
| D03 | `pet_ct_fusion` | PET-CT 代谢与形态融合 | **模态错误**：没有 PET 数据 |
| D04 | `lesion_detection_2d` | 在单张 2D 切片上检测病灶 | **降维错误**：应该用 3D 检测 |
| D05 | `deprecated_segmentation_v1` | [已废弃] 旧版分割工具 | **版本错误**：已标记废弃 |
| D06 | `ct_reconstruction` | 从正弦图重建 CT 图像 | **任务错误**：重建不属于诊断流程 |

---

## 5. 已知空白与风险

| 空白 | 影响 | 缓解方案 |
|------|------|---------|
| **Lung-RADS / LI-RADS 影像分期**无开源方案 | T9 影像模态无法用现成模型 | 用 TotalSegmentator 提取解剖特征 + LLM 规则推理 |
| **体部 CT 报告生成**无 3D→text 开源模型 | T8 IMG/MM 模态需要自建 | FORTE 架构迁移或 LLM + 结构化 prompt |
| **关键发现检测** INFORM-CT 代码未公开 | T12 无端到端方案 | TotalSegmentator 测量 + 阈值规则 + LLM 分级 |
| **端到端 RECIST** detect-then-track 仅验证肝脏 | T7 其他部位泛化性未知 | 需额外验证或用 nnDetection + ULS23 组装 |

---

## 6. 依赖项目汇总

以下是所有需要集成的外部项目，按使用频次排序：

| 项目 | GitHub | 使用次数 | 许可证 |
|------|--------|---------|--------|
| **MONAI** | Project-MONAI/MONAI | 5 个工具 | Apache 2.0 |
| **TotalSegmentator** | wasserth/TotalSegmentator | 3 个工具 | Apache 2.0 |
| **SimpleITK** | SimpleITK/SimpleITK | 2 个工具 | Apache 2.0 |
| **nnU-Net v2** | MIC-DKFZ/nnUNet | 1 个工具 | Apache 2.0 |
| **nnDetection** | MIC-DKFZ/nnDetection | 1 个工具 | Apache 2.0 |
| **ANTsPy** | ANTsX/ANTsPy | 1 个工具 | Apache 2.0 |
| **pydicom** | pydicom/pydicom | 2 个工具 | MIT |
| **RadGraph-XL** | Stanford-AIMI/radgraph | 1 个工具 | PhysioNet 协议 |
| **medspaCy** | medspacy/medspacy | 1 个工具 | MIT |
| **NegBio** | ncbi-nlp/NegBio | 1 个工具 | MIT (公共域) |
| **llm_extractinator** | DIAGNijmegen/llm_extractinator | 2 个工具 | Apache 2.0 |
| **RadFM** | chaoyi-wu/RadFM | 1 个工具 | — |
| **FORTE/BrainGPT** | charlierabea/FORTE | 1 个工具 | — |
| **detect-then-track** | alibool/detect-then-track | 1 个工具 | — |
| **AI-in-Lung-Health** | fitushar/AI-in-Lung-Health-Benchmarking... | 1 个工具 | — |
| **tnm-stage-classifier** | tatonetti-lab/tnm-stage-classifier | 1 个工具 | — |
| **pyradiomics** | AIM-Harvard/pyradiomics | 1 个工具 | BSD |
