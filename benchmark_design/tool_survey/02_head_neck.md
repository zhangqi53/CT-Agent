# 头颈部 (Head & Neck) CT — 逐格工具调研

> 严格标准：论文 + GitHub 代码缺一不可。无开源工具标 ❌。

## IMG 影像任务

### IMG-T1 异常筛查
| 工具 | 论文 | GitHub | 指标 |
|------|------|--------|------|
| SA-MIL | Wu et al., MICCAI 2023 | [SA-MIL](https://github.com/YunanWu2168/sa-mil) | Scan-level AUC (ICH) |
| RSNA ICH 1st Place | Wang et al., NeuroImage: Clinical 2021 | [RSNA ICH](https://github.com/SeuTao/RSNA2019_Intracranial-Hemorrhage-Detection) | AUC 0.988 |

### IMG-T2 病灶检测
| 工具 | 论文 | GitHub | 指标 |
|------|------|--------|------|
| BLAST-CT | Monteiro et al., **Lancet Digital Health** 2020 | [blast-ct](https://github.com/biomedia-mira/blast-ct) | 多类 TBI 病灶检测+分割, 680 CTs |
| DeepLesion/MULAN | Yan et al., J Med Imaging 2018 / MICCAI 2019 | [CADLab](https://github.com/rsummers11/CADLab) | Sens 81.1% @ 5FP (通用) |
| nnDetection | Baumgartner et al., MICCAI 2021 | [nnDetection](https://github.com/MIC-DKFZ/nnDetection) | 自配置 3D 检测 |

### IMG-T3 病灶分割
| 工具 | 论文 | GitHub | 指标 |
|------|------|--------|------|
| DeepBleed | Sharrock et al., Neuroinformatics 2021 | [deepbleed](https://github.com/msharrock/deepbleed) | Dice 0.914 (ICH+IVH) |
| DeepMedic | Kamnitsas et al., MedIA 2017 | [deepmedic](https://github.com/deepmedic/deepmedic) | 脑部病灶通用, 2500+ cites |
| BLAST-CT | Monteiro et al., **Lancet Digital Health** 2020 | [blast-ct](https://github.com/biomedia-mira/blast-ct) | 4类 TBI 分割 |
| nnU-Net | Isensee et al., **Nature Methods** 2021 | [nnUNet](https://github.com/MIC-DKFZ/nnUNet) | 通用分割金标准 |
| MedSAM | Ma et al., **Nature Comms** 2024 | [MedSAM](https://github.com/bowang-lab/MedSAM) | 交互式 prompt 分割 |

### IMG-T4 分类/良恶性
| 工具 | 论文 | GitHub | 指标 |
|------|------|--------|------|
| RSNA ICH (5亚型) | Wang et al., NeuroImage: Clinical 2021 | [RSNA ICH](https://github.com/SeuTao/RSNA2019_Intracranial-Hemorrhage-Detection) | AUC 0.98+ (各亚型) |
| HECKTOR25 (HPV) | Dexl et al., HECKTOR/MICCAI 2025 | [HECKTOR25](https://github.com/JakobDexl/HECKTOR25) | HPV 分类 + 生存预测 (PET/CT) |

### IMG-T5 测量/定量
| 工具 | 论文 | GitHub | 指标 |
|------|------|--------|------|
| pyradiomics | van Griethuysen et al., Cancer Research 2017 | [pyradiomics](https://github.com/AIM-Harvard/pyradiomics) | 1500+ 特征, 3000+ cites |
| DiffusionMLS | Gong et al., IPMI 2023 | [DiffusionMLS](https://github.com/med-air/DiffusionMLS) | 中线偏移定量(mm) |
| midline-shift | Kurenkov et al., MICCAI Workshop 2019 | [midline-shift](https://github.com/neuro-ml/midline-shift-detection) | 中线偏移检测 |

### IMG-T6 解剖结构
| 工具 | 论文 | GitHub | 指标 |
|------|------|--------|------|
| TotalSegmentator | Wasserthal et al., Radiology:AI 2023 | [TotalSegmentator](https://github.com/wasserth/TotalSegmentator) | 117类含头颈结构 |
| AnatomyNet | Zhu et al., Medical Physics 2019 | [AnatomyNet](https://github.com/wentaozhu/AnatomyNet-for-anatomical-segmentation) | 9个 HaN OAR, +3.3% Dice |
| DentalSegmentator | Dot et al., J Dentistry 2024 | [DentalSegmentator](https://github.com/gaudot/SlicerDentalSegmentator) | DSC 92-94% 颌骨/牙齿 |
| CTseg | Brudfors et al., NeuroImage 2020 | [CTseg](https://github.com/WCHN/CTseg) | GM/WM/CSF + TBV/TIV |
| MONAI VISTA3D | MONAI, CVPR 2025 | [VISTA](https://github.com/Project-MONAI/VISTA) | 127类基础模型 |

### IMG-T7 对比随访
| 工具 | 论文 | GitHub | 指标 |
|------|------|--------|------|
| ANTsPy | Avants et al., NeuroImage 2011 | [ANTsPy](https://github.com/ANTsX/ANTsPy) | 配准 (需组合其他工具) |

### IMG-T8 报告生成
| 工具 | 论文 | GitHub | 指标 |
|------|------|--------|------|
| FORTE/BrainGPT | Rabea et al., **Nature Comms** 2025 | [FORTE](https://github.com/charlierabea/FORTE) | F1 0.71, 18885 对 |
| RadFM | Wu et al., **Nature Comms** 2025 | [RadFM](https://github.com/chaoyi-wu/RadFM) | 通用 3D CT 报告+VQA |

### IMG-T9 分期/分级
❌ 无开源工具（ASPECTS DA-Net 代码未确认公开；Lung-RADS/LI-RADS 不适用）

### IMG-T11 扫描质量
| 工具 | 论文 | GitHub | 指标 |
|------|------|--------|------|
| IQA-PyTorch | Chaofeng et al., 多刊 | [IQA-PyTorch](https://github.com/chaofengc/IQA-PyTorch) | 通用 IQA（非 CT 专用） |

### IMG-T12 关键发现
| 工具 | 论文 | GitHub | 指标 |
|------|------|--------|------|
| RSNA ICH | Wang et al., 2021 | [RSNA ICH](https://github.com/SeuTao/RSNA2019_Intracranial-Hemorrhage-Detection) | AUC 0.988 颅内出血 |
| BLAST-CT | Monteiro et al., **Lancet Digital Health** 2020 | [blast-ct](https://github.com/biomedia-mira/blast-ct) | TBI 关键病灶 |
| DiffusionMLS | Gong et al., IPMI 2023 | [DiffusionMLS](https://github.com/med-air/DiffusionMLS) | 中线偏移(神经外科急症) |

---

## TXT 文本任务

### TXT-T1 异常信号识别
| 工具 | 论文 | GitHub | 指标 |
|------|------|--------|------|
| medspaCy | Eyre et al., AMIA 2021 | [medspaCy](https://github.com/medspacy/medspacy) | NER + ConText 否定检测 |

### TXT-T2 病灶信息抽取
| 工具 | 论文 | GitHub | 指标 |
|------|------|--------|------|
| RadGraph-XL | Jain et al., ACL 2024 | [RadGraph](https://github.com/Stanford-AIMI/radgraph) | F1 0.94 NER, 含 CT 报告 |

### TXT-T4 分类标签抽取
| 工具 | 论文 | GitHub | 指标 |
|------|------|--------|------|
| NegBio | Peng et al., AMIA 2018 | [NegBio](https://github.com/ncbi-nlp/NegBio) | 否定/不确定检测 |
| RadGraph-XL | Jain et al., ACL 2024 | [RadGraph](https://github.com/Stanford-AIMI/radgraph) | 断言状态标签 |

### TXT-T5 测量数据抽取
| 工具 | 论文 | GitHub | 指标 |
|------|------|--------|------|
| llm_extractinator | van Driel et al., arXiv 2025 | [llm_extractinator](https://github.com/DIAGNijmegen/llm_extractinator) | 93.7% RECIST 测量抽取 |

### TXT-T7 随访文本对比
| 工具 | 论文 | GitHub | 指标 |
|------|------|--------|------|
| llm_extractinator | van Driel et al., arXiv 2025 | [llm_extractinator](https://github.com/DIAGNijmegen/llm_extractinator) | 纵向报告对比, 94% 属性准确率 |

### TXT-T8 报告生成
❌ 无开源文本→报告专用工具（可用 RadFM 文本模式）

### TXT-T10 鉴别诊断
| 工具 | 论文 | GitHub | 指标 |
|------|------|--------|------|
| RadFM | Wu et al., **Nature Comms** 2025 | [RadFM](https://github.com/chaoyi-wu/RadFM) | 支持文本推理 |

---

## MM 多模态任务

### MM-T4 分类（影像+临床）
| 工具 | 论文 | GitHub | 指标 |
|------|------|--------|------|
| RadFM | Wu et al., **Nature Comms** 2025 | [RadFM](https://github.com/chaoyi-wu/RadFM) | 3D CT + 文本联合诊断 |

### MM-T7 随访（影像+报告）
❌ 无端到端开源工具（需组合 ANTsPy + llm_extractinator）

### MM-T8 报告生成（完整版）
| 工具 | 论文 | GitHub | 指标 |
|------|------|--------|------|
| FORTE/BrainGPT | Rabea et al., **Nature Comms** 2025 | [FORTE](https://github.com/charlierabea/FORTE) | 3D 脑 CT + 临床文本 → 报告 |

### MM-T9 分期（影像+临床）
| 工具 | 论文 | GitHub | 指标 |
|------|------|--------|------|
| tnm-stage-classifier | Tatonetti Lab, **Nature Comms** | [tnm-stage-classifier](https://github.com/tatonetti-lab/tnm-stage-classifier) | NLP 端 TNM, 23 癌种含头颈 |

### MM-T10 鉴别诊断（影像+病史）
| 工具 | 论文 | GitHub | 指标 |
|------|------|--------|------|
| RadFM | Wu et al., **Nature Comms** 2025 | [RadFM](https://github.com/chaoyi-wu/RadFM) | 3D CT + 文本鉴别诊断 |

### MM-T12 关键发现（含临床背景）
| 工具 | 论文 | GitHub | 指标 |
|------|------|--------|------|
| FORTE/BrainGPT | Rabea et al., **Nature Comms** 2025 | [FORTE](https://github.com/charlierabea/FORTE) | 印象生成 F1 0.779 |

---

## 覆盖统计

| 状态 | 格子数 |
|------|--------|
| ✅ 有开源工具 | 19/24 |
| ❌ 无开源工具 | 5/24 (T8-TXT, T9-IMG, T11, MM-T7, MM-T9仅NLP端) |
