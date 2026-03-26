# CT-Agent MCP 工具清单（严格筛选版）

> 筛选标准：**论文 + GitHub 代码 + 预训练权重/可直接推理**，缺一不可。
>
> 更新日期：2026-03-26

---

## A. 影像分割工具（有权重，直接推理）

| # | 工具 | 论文 | 安装/权重 | 能力 | 覆盖部位 |
|---|------|------|----------|------|---------|
| 1 | **TotalSegmentator** | Wasserthal, Radiology:AI 2023 | `pip install TotalSegmentator`，权重自动下载 | 117 类解剖结构分割 | 全身 |
| 2 | **CADS** | Xu et al., arXiv:2507.22953 | [GitHub](https://github.com/murong-xu/CADS)，权重 GitHub Releases + 3D Slicer 插件 | **167 类**解剖结构分割（最全） | 全身（头→膝） |
| 3 | **MONAI VISTA3D** | CVPR 2025 | [HuggingFace](https://huggingface.co/MONAI/VISTA3D-HF)，`monai.bundle.download()` | 127 类分割基础模型 + 交互式 prompt | 全身 |
| 4 | **nnU-Net v2** | Isensee, **Nature Methods** 2021 | `pip install nnunetv2`，框架 + Model Zoo | 通用分割框架（金标准） | 任意 |
| 5 | **MedSAM** | Ma et al., **Nature Comms** 2024 | [GitHub](https://github.com/bowang-lab/MedSAM)，Google Drive 权重 | 交互式 prompt 分割 | 任意 |
| 6 | **SAM-Med3D-turbo** | Wang et al., ECCV BIC 2024 Oral | [HuggingFace](https://huggingface.co/blueyo0/SAM-Med3D)，[GitHub](https://github.com/uni-medical/SAM-Med3D) | 3D prompt 分割，少量点击 | 任意 |
| 7 | **MedSAM2** | arXiv 2025 | [HuggingFace](https://huggingface.co/wanglab/MedSAM2) | 3D 分割 + CT 病灶专用 checkpoint | 任意 |
| 8 | **lungmask** | Hofmanninger, Eur Radiol 2020 | `pip install lungmask`，权重自动下载 | 肺/肺叶分割（含病理肺） | 肺 |
| 9 | **MULLET** | Wang et al., iScience 2023 | [GitHub](https://github.com/shenhai1895/Multi-phase-Liver-Lesion-Segmentation)，Google Drive 权重 | 多期肝脏病灶分割 | 肝脏 |

### MONAI Bundle 分割模型（全部 `monai.bundle.download()` 一键下载）

| # | Bundle | 论文 | 能力 | 覆盖部位 |
|---|--------|------|------|---------|
| 10 | `lung_nodule_ct_detection` | Lin, ICCV 2017 (RetinaNet) | 肺结节 3D 检测 (mAP 0.852) | 肺 |
| 11 | `spleen_ct_segmentation` | MSD Task09 | 脾脏分割 (Dice ~0.96) | 脾脏 |
| 12 | `pancreas_ct_dints_segmentation` | He, CVPR 2021 (DiNTS) | 胰腺+肿瘤分割 | 胰腺 |
| 13 | `swin_unetr_btcv_segmentation` | Hatamizadeh 2022 | 13 个腹部器官分割 | 腹部 |
| 14 | `multi_organ_segmentation` | He 2021; Roth 2018 | 7 个腹部器官（含胆囊） | 腹部 |
| 15 | `renalStructures_CECT_segmentation` | Chernenkiy 2023 | 肾脏实质/肿瘤/动脉/静脉/输尿管 | 肾脏 |
| 16 | `renalStructures_UNEST_segmentation` | Yu 2022; Zhang AAAI 2022 | 肾脏皮质/髓质/肾盂 | 肾脏 |
| 17 | `wholeBody_ct_segmentation` | Wasserthal 2022 (SegResNet) | 104 类全身分割 | 全身 |
| 18 | `pediatric_abdominal_ct_segmentation` | Somasundaram, AJR 2024 | 儿童肝脾胰分割 | 腹部(儿童) |

---

## B. 影像检测/分类工具（有权重）

| # | 工具 | 论文 | 安装/权重 | 能力 | 覆盖部位 |
|---|------|------|----------|------|---------|
| 19 | **RSNA ICH 1st** | Wang, NeuroImage:Clinical 2021 | [GitHub](https://github.com/SeuTao/RSNA2019_Intracranial-Hemorrhage-Detection)，Google Drive | 颅内出血 5 亚型分类 (AUC 0.988) | 脑 |
| 20 | **BLAST-CT** | Monteiro, **Lancet Digital Health** 2020 | [GitHub](https://github.com/biomedia-mira/blast-ct)，内置权重 | TBI 病灶检测+分割（4类） | 脑 |
| 21 | **DeepBleed** | Sharrock, Neuroinformatics 2021 | [GitHub](https://github.com/msharrock/deepbleed)，Dropbox 权重 | ICH 分割+体积量化 (Dice 0.914) | 脑 |
| 22 | **PENet** | Huang, npj Digital Medicine 2020 | [GitHub](https://github.com/marshuang80/penet)，Stanford Box 权重 | 肺栓塞检测 (AUROC 0.85) | 肺/纵隔 |

---

## C. 多模态 VLM / 报告生成（有权重）

| # | 工具 | 论文 | 安装/权重 | 能力 | 覆盖 |
|---|------|------|----------|------|------|
| 23 | **Merlin** | Blankemeier, **Nature** 2026 | `pip install merlin-vlm`，[HuggingFace](https://huggingface.co/stanfordmimi/Merlin) | 31 种发现零样本分类 + 692 表型 + 报告生成 + 20 器官分割 + 5 年预测 | 全身 |
| 24 | **RadFM** | Wu, **Nature Comms** 2025 | [HuggingFace](https://huggingface.co/chaoyi-wu/RadFM-checkpoint) | 通用放射 VLM（诊断/VQA/报告/鉴别诊断），支持 3D CT | 全身 |
| 25 | **CT-CLIP** | Hamamci, Nature BME 2025 | [HuggingFace](https://huggingface.co/ibrahimethemhamamci/CT-CLIP) | 零样本 CT 异常分类 + 检索 | 胸部 |
| 26 | **CT-CHAT** | Hamamci, Nature BME 2025 | [HuggingFace](https://huggingface.co/ibrahimethemhamamci/CT-CHAT) | CT VQA + 报告生成 (LLaVA 架构) | 胸部 |
| 27 | **M3D-LaMed** | Bai, arXiv 2024 | [HuggingFace](https://huggingface.co/GoodBaiBai88/M3D-LaMed-Phi-3-4B) | 3D 医学 VLM 多任务（报告/VQA/分割） | 全身 |
| 28 | **FORTE/BrainGPT** | Rabea, **Nature Comms** 2025 | [HuggingFace](https://huggingface.co/charlierabea/FORTE) | 脑 CT → 结构化报告 (F1 0.71) | 脑 |
| 29 | **MedGemma 1.5** | Google, 2025 | [HuggingFace](https://huggingface.co/google/medgemma-1.5-4b-it) | 支持 3D CT 的 VQA + 报告生成 | 全身 |
| 30 | **RadGPT** | Bassi, **ICCV** 2025 | [GitHub](https://github.com/MrGiovanni/RadGPT) | 腹部 CT 肿瘤报告生成 (AbdomenAtlas 9262 volumes) | 腹部 |

---

## D. 基础模型 / 特征提取（有权重，可做下游微调）

| # | 工具 | 论文 | 权重 | 能力 |
|---|------|------|------|------|
| 31 | **CT-FM** | Harvard AIM, arXiv:2501.09001 | [HuggingFace](https://huggingface.co/collections/fthksu/ct-fm-6729ed66e87f932e27d6cbc8)，[GitHub](https://github.com/project-lighter/CT-FM) | 148K CT 自监督基础模型，下游可做分割/分类/检索 |
| 32 | **TAP-CT** | arXiv:2512.00872 | [HuggingFace](https://huggingface.co/fomofo/tap-ct-b-3d) | DINOv2 适配 3D CT，冻结特征做分割/分类 |
| 33 | **SuPreM** | ICLR 2024 Oral | [GitHub](https://github.com/MrGiovanni/SuPreM) | 预训练 U-Net/SegResNet/Swin UNETR backbone，腹部 25 器官 |
| 34 | **Med3D** | Tencent, arXiv:1904.00625 | [HuggingFace](https://huggingface.co/TencentMedicalNet/) | 3D ResNet 预训练 backbone（7 个变体） |
| 35 | **BiomedCLIP** | Microsoft, NeurIPS 2023 | [HuggingFace](https://huggingface.co/microsoft/BiomedCLIP-PubMedBERT_256-vit_base_patch16_224) | 生物医学图文匹配（2D） |

---

## E. 工具库（无需权重，pip 安装直接调用）

| # | 工具 | 论文 | 安装 | 能力 |
|---|------|------|------|------|
| 36 | **pyradiomics** | van Griethuysen, Cancer Research 2017 | `pip install pyradiomics` | 1500+ 影像组学特征 |
| 37 | **ANTsPy** | Avants, NeuroImage 2011 | `pip install antspyx` | 刚性/仿射/SyN 形变配准 |
| 38 | **SimpleITK** | Lowekamp, Frontiers 2013 | `pip install SimpleITK` | DICOM 加载/窗宽窗位/重采样 |
| 39 | **pydicom** | Mason et al. | `pip install pydicom` | DICOM 元数据读写 |
| 40 | **vmtk** | Antiga et al. | `pip install vmtk` | 血管分析（中心线/截面积/动脉瘤） |
| 41 | **WORC** | Starmans, Eur Radiol 2021 | `pip install WORC` | 自动化影像组学分类流水线 |

---

## F. 文本 NLP 工具（有模型或规则引擎）

| # | 工具 | 论文 | 安装/权重 | 能力 |
|---|------|------|----------|------|
| 42 | **medspaCy** | Eyre, AMIA 2021 | `pip install medspacy` | 临床 NER + ConText 否定检测 |
| 43 | **NegBio** | Peng, AMIA 2018 | `pip install negbio` | 否定/不确定检测 |
| 44 | **CheXbert** | Smit, EMNLP 2020 | [GitHub](https://github.com/stanfordmlgroup/CheXbert)，内置 BERT 权重 | 报告 14 类标签分类 |
| 45 | **RadGraph-XL** | Jain, ACL 2024 | [GitHub](https://github.com/Stanford-AIMI/radgraph)，有模型 | 报告 NER + 关系抽取（含 CT） |
| 46 | **llm_extractinator** | van Driel, JAMIA Open 2025 | `pip install llm-extractinator`，用 Ollama 本地 LLM | 测量值/纵向抽取 (93.7% acc) |
| 47 | **Radiology_Bart** | HuggingFace 社区 | [HuggingFace](https://huggingface.co/Mbilal755/Radiology_Bart) | 报告 Findings→Impression 摘要 |

---

---

## G. 新增 pip 可安装工具（有权重，直接推理）

| # | 工具 | 论文 | 安装 | 能力 | 覆盖部位 |
|---|------|------|------|------|---------|
| 48 | **PlatiPy** | Chlap & Finnegan, 2023 | `pip install platipy[cardiac]` | 心脏 17 亚结构分割（自动下载 nnUNet 权重） | 心脏(RT CT) |
| 49 | **MONAILabel** | Diaz-Pinto et al., 2022 | `pip install monailabel` | 交互式标注服务器 + 预训练自动分割模型 | 多器官 |
| 50 | **body-organ-analysis** | SHIP-AI, Greifswald | `pip install body-organ-analysis` | 全身器官+体成分分割（基于 TotalSegmentator） | 全身 |
| 51 | **bpreg** | Schuhegger, MIC-DKFZ 2021 | `pip install bpreg` | CT 体区识别（骨盆→头部），Zenodo 权重自动下载 | 全身 |
| 52 | **TotalSpineSeg** | Warszawer et al., 2025 | `pip install totalspineseg` | 椎体/椎间盘/脊髓/椎管实例分割+标记 | 脊柱 |
| 53 | **Skellytour** | Wardell, Radiology:AI 2025 | [GitHub](https://github.com/cpwardell/Skellytour) | 骨骼分割 17/38/60 标签（优于 TotalSegmentator） | 骨骼 |
| 54 | **Comp2Comp** | Blankemeier, arXiv:2302.06568 | [GitHub](https://github.com/StanfordMIMI/Comp2Comp)，HuggingFace 权重自动下载 | 体成分（肌肉/脂肪）+ 骨密度 + 主动脉钙化 | 脊柱/腹部 |
| 55 | **DeepCAC** | Zeleznik, **Nature Comms** 2021 | [GitHub](https://github.com/AIM-Harvard/DeepCAC)，权重内置 | 冠脉钙化定量（20,084 例验证） | 心脏 |
| 56 | **AI-CAC** | Hagopian et al. | [GitHub](https://github.com/Raffi-Hagopian/AI-CAC) | 非门控胸部 CT 钙化评分 | 心脏/胸部 |

---

## 合计：56 个可直接包装为 MCP 的工具

| 类别 | 数量 |
|------|------|
| A. 影像分割 | 18 |
| B. 影像检测/分类 | 4 |
| C. 多模态 VLM/报告 | 8 |
| D. 基础模型/backbone | 5 |
| E. 工具库 | 6 |
| F. 文本 NLP | 6 |
| G. 新增 pip 工具 | 9 |
| **合计** | **56** |
