# CT-Agent MCP 工具包设计

> 版本: 0.3 | 日期: 2025-03-25
>
> 本文档定义 CT 智能体 benchmark 所需的全部 MCP 工具，
> 以及每个工具背后对应的**权威论文 + 开源实现**。
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

## 3. 完整工具清单

### 3.1 L1 预处理层（通用）

| ID | 工具名 | 功能 | 论文/来源 | 开源实现 |
|----|--------|------|----------|---------|
| P01 | `dicom_loader` | 加载 DICOM → 标准化 3D 体积（LPS+、HU 校准） | SimpleITK (Lowekamp et al., Frontiers 2013) | [SimpleITK](https://github.com/SimpleITK/SimpleITK) |
| P02 | `dicom_metadata_reader` | 读取 DICOM tag（患者/扫描参数/对比剂） | pydicom (Mason et al.) | [pydicom](https://github.com/pydicom/pydicom) |
| P03 | `window_level` | 窗宽窗位变换（8 种预设 + 自定义） | MONAI (Cardoso et al., arXiv 2022) | [MONAI](https://github.com/Project-MONAI/MONAI) |
| P04 | `image_registration` | 刚性/仿射/SyN 形变配准 | ANTs (Avants et al., NeuroImage 2011, 10000+ cites) | [ANTsPy](https://github.com/ANTsX/ANTsPy) |
| P05 | `scan_quality_check` | 伪影/噪声/层厚/对比剂时相评估 | MONAI DataAnalyzer + 自定义规则 | [MONAI](https://github.com/Project-MONAI/MONAI) |
| P06 | `body_region_classifier` | 自动识别 CT 覆盖的身体部位 | 基于 TotalSegmentator 输出推断 | [TotalSegmentator](https://github.com/wasserth/TotalSegmentator) |

### 3.2 L2 文本层

| ID | 工具名 | 功能 | 论文/来源 | 开源实现 |
|----|--------|------|----------|---------|
| T01 | `clinical_signal_extractor` | 病历文本异常信号提取 + 否定检测 | medspaCy (Eyre et al., JAMIA 2021) | [medspaCy](https://github.com/medspacy/medspacy) |
| T02 | `report_ner` | CT 报告实体抽取（位置/大小/形态/密度/关系） | RadGraph-XL (Jain et al., ACL 2024，训练集含 CT) | [RadGraph](https://github.com/Stanford-AIMI/radgraph) |
| T03 | `classification_label_extractor` | 从文本抽取诊断标签 + 断言状态 | NegBio (Peng et al., EMNLP 2018) | [NegBio](https://github.com/ncbi-nlp/NegBio) |
| T04 | `measurement_extractor` | 报告测量数值抽取（RECIST 径线等） | llm_extractinator (van Driel et al., arXiv 2025, 93.7% acc) | [llm_extractinator](https://github.com/DIAGNijmegen/llm_extractinator) |
| T05 | `temporal_report_aligner` | 多份时序报告对齐 + 变化抽取 | "Tracking Cancer Through Text" (van Driel et al., arXiv 2025) | [llm_extractinator](https://github.com/DIAGNijmegen/llm_extractinator) |
| T06 | `medical_knowledge_lookup` | 查询分期标准/指南/鉴别要点 | 自建 RAG 知识库 | — |

### 3.3 L3 感知层 — 通用工具

| ID | 工具名 | 功能 | 论文/来源 | 开源实现 |
|----|--------|------|----------|---------|
| V01 | `anatomy_segmentation` | 117 类全身解剖结构分割 | TotalSegmentator (Wasserthal et al., Radiology:AI 2023, 600+ cites) | [TotalSegmentator](https://github.com/wasserth/TotalSegmentator) |
| V02 | `universal_lesion_detection` | 全身通用病灶检测 (3D bbox) | DeepLesion (Yan et al., J Med Imaging 2018, 400+ cites) | [CADLab](https://github.com/rsummers11/CADLab) |
| V03 | `universal_lesion_segmentation` | 全身通用病灶分割 | ULS23 (DIAG, MedIA 2025) + nnU-Net v2 | [ULS23](https://github.com/DIAGNijmegen/ULS23) |
| V04 | `abnormality_screening` | 全局二分类：正常 vs 异常 | MONAI 3D 分类网络 (DenseNet121/ViT) | [MONAI](https://github.com/Project-MONAI/MONAI) |
| V05 | `interactive_segmentation` | 基于 prompt（点击/bbox）的交互式 3D 分割 | MedSAM (Ma et al., Nature Comms 2024, 300+ cites) | [MedSAM](https://github.com/bowang-lab/MedSAM) |
| V06 | `ct_zero_shot_diagnosis` | CT 零样本/少样本异常诊断 | CT-CLIP/CT-RATE (Hamamci et al., 2024) | [CT-CLIP](https://github.com/ibrahimethemhamamci/CT-CLIP) |
| V07 | `vista3d_segmentation` | 127 类 CT 分割基础模型 | MONAI VISTA3D (CVPR 2025) | [VISTA](https://github.com/Project-MONAI/VISTA) |

### 3.4 L3 感知层 — 肺部专用工具

| ID | 工具名 | 功能 | 论文/来源 | 开源实现 |
|----|--------|------|----------|---------|
| V-LU01 | `lung_nodule_detection` | 肺结节 3D 检测 | nnDetection (Baumgartner et al., MICCAI 2021, 200+ cites) | [nnDetection](https://github.com/MIC-DKFZ/nnDetection) |
| V-LU02 | `lung_nodule_segmentation` | 肺结节体素级分割 | nnU-Net (Isensee et al., Nature Methods 2021, 7000+ cites) | [nnU-Net](https://github.com/MIC-DKFZ/nnUNet) |
| V-LU03 | `lung_lobe_segmentation` | 肺叶分割（5 叶） | TotalSegmentator / MONAI Lung Lobe bundle | [TotalSegmentator](https://github.com/wasserth/TotalSegmentator) |
| V-LU04 | `pulmonary_embolism_detection` | 肺栓塞检测（CTA） | PENet (Huang et al., npj Digital Medicine 2020, 150+ cites) | [PENet](https://github.com/marshuang80/PENet) |
| V-LU05 | `pneumonia_quantification` | 肺炎/COVID 病灶分割与体积量化 | Inf-Net (Fan et al., **TMI** 2020, 1500+ cites) | [Inf-Net](https://github.com/DengPingFan/Inf-Net) |
| V-LU06 | `lung_segmentation` | 鲁棒肺实质分割（含病理肺） | lungmask (Hofmanninger et al., Eur Radiol 2020, 400+ cites) | [lungmask](https://github.com/JoHof/lungmask) |
| V-LU07 | `airway_segmentation` | 气道树提取与分割 | ATM'22 Challenge (Zhang et al., MedIA 2023) | [ATM'22](https://github.com/Puzzled-Hui/ATM-22-Related-Work) |
| V-LU08 | `emphysema_quantification` | 肺气肿/COPD 定量（LAA-950/Pi10） | Chest Imaging Platform (Ross et al., BWH/Harvard) | [CIP](https://github.com/acil-bwh/ChestImagingPlatform) |
| V-LU09 | `lung_nodule_classification` | 肺结节良恶性分类 + 风险预测 | DeepLung (Zhu et al., WACV 2018, 600+ cites) | [DeepLung](https://github.com/wentaozhu/DeepLung) |

### 3.5 L3 感知层 — 肝脏/腹部专用工具

| ID | 工具名 | 功能 | 论文/来源 | 开源实现 |
|----|--------|------|----------|---------|
| V-LI01 | `liver_tumor_segmentation` | 肝脏肿瘤分割 | LiTS Benchmark (Bilic et al., MedIA 2023, 600+ cites) + nnU-Net | [nnU-Net](https://github.com/MIC-DKFZ/nnUNet) |
| V-LI02 | `pancreas_lesion_detection` | 胰腺癌检测（非增强 CT） | FELIX (Cao et al., **Nature Medicine** 2023, 150+ cites) | [FELIX](https://github.com/chencancan1018/FELIX) |
| V-LI03 | `kidney_tumor_segmentation` | 肾脏肿瘤分割 | KiTS Challenge (Heller et al., MedIA 2023, 400+ cites) + nnU-Net | [KiTS](https://github.com/neheller/kits19) |
| V-LI04 | `lymph_node_detection` | 腹部淋巴结检测 | NIH CADLab (Summers et al., Radiology:AI) | [CADLab](https://github.com/rsummers11/CADLab) |
| V-LI05 | `aortic_measurement` | 主动脉直径/形态测量 | VMTK (Antiga et al., 800+ cites) | [VMTK](https://github.com/vmtk/vmtk) |
| V-LI06 | `multi_lesion_detection_tagging` | 多器官病灶联合检测+标签 | MULAN (Yan et al., MICCAI 2019, 150+ cites) | [MULAN](https://github.com/ke-yan/MULAN) |
| V-LI07 | `pancreas_segmentation` | 胰腺实质分割 | Attention U-Net (Oktay et al., MIDL 2018, 5000+ cites) | [Attention-Gated-Networks](https://github.com/ozan-oktay/Attention-Gated-Networks) |
| V-LI08 | `pelvic_fracture_detection` | 骨盆骨折检测 | CTPelvic1K (Liu et al., MICCAI 2021) | [CTPelvic1K](https://github.com/ICT-MIRACLE-lab/CTPelvic1K) |

### 3.6 L3 感知层 — 头颅/脑部专用工具

| ID | 工具名 | 功能 | 论文/来源 | 开源实现 |
|----|--------|------|----------|---------|
| V-BR01 | `intracranial_hemorrhage_detection` | 颅内出血检测与 5 亚型分类 | Chilamkurthy et al., **Lancet** 2018, 900+ cites; RSNA ICH 2019 | [RSNA ICH Top1](https://github.com/SeuTao/RSNA2019_Intracranial-Hemorrhage-Detection) |
| V-BR02 | `hemorrhage_segmentation` | 出血体素级分割 + 体积量化 | DeepBleed (3D U-Net) | [DeepBleed](https://github.com/msharrock/deepbleed) |
| V-BR03 | `brain_lesion_segmentation` | 脑部病灶通用分割 | DeepMedic (Kamnitsas et al., MedIA 2017, 2500+ cites) | [DeepMedic](https://github.com/deepmedic/deepmedic) |
| V-BR04 | `midline_shift_measurement` | 脑中线偏移测量 (mm) | Wei et al., MICCAI/TMI 2018-2020 | [midline-shift](https://github.com/xf4j/midline-shift) |
| V-BR05 | `aneurysm_detection` | CTA 脑动脉瘤检测 | Shi et al., **Nature Communications** 2020, 300+ cites | 部分代码公开 |
| V-BR06 | `hydrocephalus_detection` | 脑室扩张/脑积水检测（Evans Index） | 脑室分割 + 几何分析 | TotalSegmentator + 自建 |
| V-BR07 | `skull_fracture_detection` | 颅骨骨折检测 | Chilamkurthy et al., **Lancet** 2018 (AUC>0.95) | [AutoImplant](https://github.com/Jianningli/autoimplant) |

### 3.7 L3 感知层 — 心脏专用工具

| ID | 工具名 | 功能 | 论文/来源 | 开源实现 |
|----|--------|------|----------|---------|
| V-CA01 | `calcium_scoring` | 冠脉钙化积分（Agatston Score） | Lessmann et al., **TMI** 2018, 350+ cites | [CalciumScoring](https://github.com/lessmann/CalciumScoring) |
| V-CA02 | `coronary_segmentation` | 冠脉树分割（CTA） | ImageCAS (Zeng et al., MedIA 2023) | [ImageCAS](https://github.com/XiaoweiXu/ImageCAS-A-Large-Scale-Dataset-and-Benchmark-for-Coronary-Artery-Segmentation) |
| V-CA03 | `cardiac_chamber_segmentation` | 心腔分割（4 腔 + 大血管） | MM-WHS (Zhuang & Shen, TMI 2019, 400+ cites) | [TotalSegmentator](https://github.com/wasserth/TotalSegmentator) |
| V-CA04 | `coronary_centerline_tracking` | 冠脉中心线提取 | Wolterink et al., MedIA 2019, 200+ cites | [coronary-tracking](https://github.com/jmwolterink/coronary-artery-tracking) |

### 3.8 L3 感知层 — 脊柱/骨骼专用工具

| ID | 工具名 | 功能 | 论文/来源 | 开源实现 |
|----|--------|------|----------|---------|
| V-SP01 | `vertebra_segmentation_labeling` | 椎体实例分割 + 解剖标记 (C1-L5) | VerSe (Sekuboyina et al., MedIA 2021, 300+ cites) | [VerSe](https://github.com/anjany/verse) |
| V-SP02 | `vertebral_fracture_detection` | 椎体压缩性骨折检测 | Burns et al., Radiology 2020 / VerSe 衍生 | [VerSe](https://github.com/anjany/verse) |
| V-SP03 | `rib_fracture_detection` | 肋骨骨折检测 + 分类 | RibFrac Challenge (Jin et al., Radiology:AI 2021, MedIA 2024) | [FracNet](https://github.com/M3DV/FracNet) |
| V-SP04 | `bone_density_estimation` | CT 机会性骨密度估计 | Löffler et al., Radiology 2022; Pickhardt et al., AIM 2013, 700+ cites | TotalSegmentator + HU 分析 |
| V-SP05 | `body_composition_analysis` | 肌肉/脂肪量化（L3 层面） | Koitka et al., Radiology 2021 / Stanford AIMI | [Comp2Comp](https://github.com/StanfordMIMI/Comp2Comp) |
| V-SP06 | `cobb_angle_measurement` | 脊柱侧弯 Cobb 角测量 | AASCE Challenge (MICCAI 2019) | [AASCE2019](https://github.com/SHTCyuyh/AASCE2019) |

### 3.9 L4 定量层

| ID | 工具名 | 功能 | 论文/来源 | 开源实现 |
|----|--------|------|----------|---------|
| Q01 | `lesion_measurement` | 三径测量 + 体积 + CT 值 + 形状特征 | pyradiomics (van Griethuysen et al., Cancer Research 2017, 3000+ cites) | [pyradiomics](https://github.com/AIM-Harvard/pyradiomics) |
| Q02 | `volume_change_calculator` | 两时间点体积/径线变化率 | 纯数值计算（基于 Q01 + P04 输出） | 自建 |
| Q03 | `recist_evaluator` | RECIST 1.1 治疗响应评估 | detect-then-track (alibool, JIMM 2025) | [detect-then-track](https://github.com/alibool/detect-then-track) |

### 3.10 L5 融合层

| ID | 工具名 | 功能 | 论文/来源 | 开源实现 |
|----|--------|------|----------|---------|
| F01 | `multimodal_evidence_fusion` | 影像特征 + 文本证据 → 融合置信度 | LLM 结构化推理链 | 自建 |
| F02 | `modality_attribution` | 各模态对结论的贡献度分析 | LLM 归因分析 | 自建 |

### 3.11 L6 推理层

| ID | 工具名 | 功能 | 论文/来源 | 开源实现 |
|----|--------|------|----------|---------|
| R01 | `malignancy_classifier` | 良恶性及亚型分类 | **肺**: AI-in-Lung-Health (fitushar, multi-dataset AUC 0.71-0.90) | [AI-Lung-Health](https://github.com/fitushar/AI-in-Lung-Health-Benchmarking-Detection-and-Diagnostic-Models-Across-Multiple-CT-Scan-Datasets) |
| R02 | `staging_engine` | TNM 分期（NLP 方式） | BBTEN (Tatonetti Lab, **Nature Comms**, 23 癌种) | [tnm-stage-classifier](https://github.com/tatonetti-lab/tnm-stage-classifier) |
| R03 | `differential_diagnosis` | 鉴别诊断列表 + 支持/反对证据 | RadFM (Wu et al., **Nature Comms** 2025, 支持 3D CT) | [RadFM](https://github.com/chaoyi-wu/RadFM) |
| R04 | `lung_nodule_malignancy` | Lung-RADS 评级 + 恶性概率 | Sybil (Mikhael et al., **J Clin Oncol** 2023) | [Sybil](https://github.com/reginabarzilaygroup/Sybil) |

### 3.12 L7 输出层

| ID | 工具名 | 功能 | 论文/来源 | 开源实现 |
|----|--------|------|----------|---------|
| O01 | `report_generator` | 3D CT → 结构化影像报告 | FORTE/BrainGPT (charlierabea, **Nature Comms** 2025) | [FORTE](https://github.com/charlierabea/FORTE) |
| O02 | `fhir_exporter` | 结构化报告 → HL7 FHIR 格式 | 纯模板映射 | 自建 |
| O03 | `critical_finding_alert` | 紧急/偶发发现分级告警 | TotalSegmentator 测量 + 阈值规则 | [TotalSegmentator](https://github.com/wasserth/TotalSegmentator) |
| O04 | `report_quality_scorer` | 报告质量自评 | LLM rubric 评分 | 自建 |

---

## 4. 干扰工具（Distractor Tools）

不应被选用，测试工具选择能力。

| ID | 工具名 | 伪描述 | 干扰类型 |
|----|--------|--------|---------|
| D01 | `mri_lesion_detection` | 在 MRI 序列中检测病灶 | **模态错误**：本系统只处理 CT |
| D02 | `xray_abnormality_screen` | 对 X 光片进行异常筛查 | **模态错误** |
| D03 | `pet_ct_fusion` | PET-CT 代谢融合分析 | **模态错误**：没有 PET 数据 |
| D04 | `lesion_detection_2d` | 在单张 2D 切片上检测 | **降维错误**：应用 3D |
| D05 | `deprecated_segmentation_v1` | [已废弃] 旧版分割 | **版本错误** |
| D06 | `ct_reconstruction` | 正弦图重建 CT 图像 | **任务错误**：不属于诊断 |
| D07 | `ultrasound_liver_screen` | 超声肝脏筛查 | **模态错误** |
| D08 | `mammography_detection` | 乳腺 X 光检测 | **模态+部位错误** |

---

## 5. 工具统计

| 类别 | 数量 |
|------|------|
| L1 预处理层 | 6 |
| L2 文本层 | 6 |
| L3 感知层 — 通用 | 7 |
| L3 感知层 — 肺部 | 9 |
| L3 感知层 — 肝脏/腹部 | 8 |
| L3 感知层 — 头颅/脑部 | 7 |
| L3 感知层 — 心脏 | 4 |
| L3 感知层 — 脊柱/骨骼 | 6 |
| L4 定量层 | 3 |
| L5 融合层 | 2 |
| L6 推理层 | 4 |
| L7 输出层 | 4 |
| **正式工具合计** | **66** |
| 干扰工具 | 8 |
| **总计** | **74** |

---

## 6. 已知空白与风险

| 空白 | 影响 | 缓解方案 |
|------|------|---------|
| **LI-RADS 影像自动分期** | 肝脏 T9 IMG/MM 无现成模型 | TotalSegmentator 特征 + LLM 规则推理 |
| **Lung-RADS 影像自动评级** | 肺部 T9 IMG（Sybil 可部分覆盖） | Sybil 恶性概率 + 结节形态特征 |
| **体部 CT 报告生成** | T8 IMG/MM 无 3D→text 模型（FORTE 仅脑部） | FORTE 架构迁移或 LLM + 结构化 prompt |
| **ASPECTS 自动评分** | 脑部 T9 无开源方案（RAPID 商用） | DeepMedic 分割 + 区域 HU 分析 |
| **端到端 RECIST** | detect-then-track 仅验证肝脏 | nnDetection + ULS23 组装 |
| **肠梗阻检测** | 腹部专用检测无开源 | 通用病灶检测 + LLM 判断 |
| **心包积液检测** | 心脏专用无独立工具 | TotalSegmentator 心包分割 + 体积阈值 |
| **脊柱管狭窄分级** | 无成熟开源方案 | TotalSegmentator 椎管分割 + 截面积计算 |

---

## 7. 核心依赖项目汇总

按引用量/重要性排序：

| 项目 | 论文 | 发表刊物 | 引用量 | 许可证 | 覆盖工具数 |
|------|------|---------|--------|--------|-----------|
| **nnU-Net v2** | Isensee et al. | Nature Methods 2021 | 7000+ | Apache 2.0 | 5+ |
| **TotalSegmentator** | Wasserthal et al. | Radiology:AI 2023 | 600+ | Apache 2.0 | 6+ |
| **ANTs/ANTsPy** | Avants et al. | NeuroImage 2011 | 10000+ | Apache 2.0 | 1 |
| **pyradiomics** | van Griethuysen et al. | Cancer Research 2017 | 3000+ | BSD | 1 |
| **MONAI** | Cardoso et al. | arXiv 2022 | 300+ | Apache 2.0 | 4 |
| **SimpleITK** | Lowekamp et al. | Frontiers 2013 | — | Apache 2.0 | 1 |
| **DeepMedic** | Kamnitsas et al. | MedIA 2017 | 2500+ | BSD | 1 |
| **nnDetection** | Baumgartner et al. | MICCAI 2021 | 200+ | Apache 2.0 | 1 |
| **RadFM** | Wu et al. | Nature Comms 2025 | — | — | 1 |
| **FELIX** | Cao et al. | Nature Medicine 2023 | 150+ | — | 1 |
| **RadGraph-XL** | Jain et al. | ACL 2024 | — | PhysioNet | 1 |
| **Sybil** | Mikhael et al. | J Clin Oncol 2023 | — | MIT | 1 |
| **MedSAM** | Ma et al. | Nature Comms 2024 | 300+ | Apache 2.0 | 1 |
| **Comp2Comp** | Stanford AIMI | Radiology 2021 | 150+ | — | 1 |
| **FORTE** | charlierabea | Nature Comms 2025 | — | — | 1 |
| **llm_extractinator** | van Driel et al. | arXiv 2025 | — | Apache 2.0 | 2 |
| **pydicom** | Mason et al. | — | — | MIT | 1 |
