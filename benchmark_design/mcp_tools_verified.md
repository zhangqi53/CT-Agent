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

## H. 精确搜索新增——盆腔/胃肠/头颈/肾脏/分期/关键发现

### H1. 盆腔专用

| # | 工具 | 论文 | GitHub | 权重 | 能力 |
|---|------|------|--------|------|------|
| 57 | **OvSeg** | Buddenkotte, Eur Radiol Exp 2023 | [ThomasBudd/ovseg](https://github.com/ThomasBudd/ovseg) | ✅ 3 模型自动下载 | 卵巢癌 CT 分割（骨盆/网膜/腹腔/淋巴结） |
| 58 | **FracSegNet** | Liu, MICCAI 2023 + Frontiers Med 2025 | [YzzLiu/FracSegNet](https://github.com/YzzLiu/FracSegNet) | ✅ 权重可下载 | 骨盆骨折分割 (IoU 0.930) |
| 59 | **U-SAM/CARE** | Zhang, **Comms Medicine (Nature)** 2025 | [kanydao/U-SAM](https://github.com/kanydao/U-SAM) | ✅ 代码+数据 | 直肠癌 CT 分割 (398 例, 33K slices) |
| 60 | **CTPelvic1K** | Liu, IJCARS 2021 | [MIRACLE-Center/CTPelvic1K](https://github.com/MIRACLE-Center/CTPelvic1K) | ✅ baseline 模型 | 骨盆骨骼分割 (1184 volumes) |

### H2. 胃肠道专用

| # | 工具 | 论文 | GitHub | 权重 | 能力 |
|---|------|------|--------|------|------|
| 61 | **CT Colonography Polyp** | Wesp, **Eur Radiol** 2022 | [pwesp/deep-learning-in-ct-colonography](https://github.com/pwesp/deep-learning-in-ct-colonography) | ✅ weights/ 目录 | CTC 息肉良恶性分类 (AUC 0.91) |

### H3. 头颈部专用

| # | 工具 | 论文 | GitHub | 权重 | 能力 |
|---|------|------|--------|------|------|
| 62 | **HiLab Head-Neck-GTV** | Fang et al., StructSeg 2019 | [HiLab-git/Head-Neck-GTV](https://github.com/HiLab-git/Head-Neck-GTV) | ✅ 百度盘权重 | 鼻咽癌 GTV 分割 (Dice 0.65) |
| 63 | **Parotid Segmentation** | Tyagi, Diagnostics 2023 | [1aryantyagi/Segmentation-Paper](https://github.com/1aryantyagi/Segmentation-Paper) | ✅ 有权重 | 腮腺 CT 分割 (Dice 0.88) |

### H4. 肾脏/脾脏专用

| # | 工具 | 论文 | GitHub | 权重 | 能力 |
|---|------|------|--------|------|------|
| 64 | **RSNA 2023 Trauma 1st** | Radiology:AI 2024 | [Nischaydnk/RSNA-2023-1st-place-solution](https://github.com/Nischaydnk/RSNA-2023-1st-place-solution) | ✅ 有权重 | 脾脏/肝脏/肾脏损伤分级 (AUC 0.98) |
| 65 | **KiTS23 2nd Place** | MICCAI 2023 KiTS Challenge | [khuhm/KiTS23-2nd-place](https://github.com/khuhm/KiTS23-2nd-place) | ✅ pretrained_models/ | 肾脏/肿瘤/囊肿分割 |
| 66 | **AbdomenAtlas** | NeurIPS 2023 | [MrGiovanni/AbdomenAtlas](https://github.com/MrGiovanni/AbdomenAtlas) | ✅ checkpoint 下载 | 25 器官 + 7 肿瘤分割 (9262 volumes) |
| 67 | **OrganSegRSTN** | Xia et al. | [198808xc/OrganSegRSTN](https://github.com/198808xc/OrganSegRSTN) | ✅ 有权重 | 小器官分割（肾上腺等） |

### H5. 胆囊/多器官异常检测

| # | 工具 | 论文 | GitHub | 权重 | 能力 |
|---|------|------|--------|------|------|
| 68 | **sato_j-mid_ad** | Sato et al. | [jun-sato/sato_j-mid_ad](https://github.com/jun-sato/sato_j-mid_ad) | ✅ pCloud 权重 | 多器官异常检测（胆结石/息肉/胆管扩张/肝脏等） |

### H6. 分期/分级

| # | 工具 | 论文 | GitHub | 权重 | 能力 |
|---|------|------|--------|------|------|
| 69 | **StrokeViT** | arXiv | [rishiraj-cs/StrokeViT_With_AutoML](https://github.com/rishiraj-cs/StrokeViT_With_AutoML) | ✅ 权重内置 | ASPECTS 卒中评分 |
| 70 | **Acute-stroke Pipeline** | Liu et al. | [Chin-Fu-Liu/Acute-stroke_Detection_Segmentation](https://github.com/Chin-Fu-Liu/Acute-stroke_Detection_Segmentation) | ✅ .h5 权重 | 卒中检测+分割 (CPU 20-30s) |
| 71 | **NoduleNet** | Tang, MICCAI 2019 | [uci-cbcl/NoduleNet](https://github.com/uci-cbcl/NoduleNet) | ✅ Google Drive | 肺结节检测+分割 (Fleischner 前置) |
| 72 | **RadiomicsLiverFibrosis** | IMICSLab | [IMICSLab/RadiomicsLiverFibrosisDetection](https://github.com/IMICSLab/RadiomicsLiverFibrosisDetection) | ✅ 模型公开 | 肝纤维化 CT 分级 |
| 73 | **MI_prediction** | Omarraita | [Omarraita/MI_prediction](https://github.com/Omarraita/MI_prediction) | ✅ 预训练模型 | 冠脉狭窄→心梗预测 |

### H7. 关键发现检测

| # | 工具 | 论文 | GitHub | 权重 | 能力 |
|---|------|------|--------|------|------|
| 74 | **VCFNet** | Xiong, Frontiers Endocrinol 2023 | [Xiongyuchao/VCFNet](https://github.com/Xiongyuchao/VCFNet) | ✅ 模型+评估代码 | 椎体压缩骨折分类 |
| 75 | **Maskrcnn_RibFrac** | ESWA 2025 | [sshuaichai/Maskrcnn_RibFrac](https://github.com/sshuaichai/Maskrcnn_RibFrac) | ✅ PyTorch 权重 | 肋骨骨折检测 (>97% acc) |
| 76 | **PACT-3D** | **Nature Comms** 2024 | [IMinChiu/pact-3d](https://github.com/IMinChiu/pact-3d) | ⚠️ 需确认 | 气腹(游离气体)检测 (Sens 0.81-0.98) |

---

### H8. 深度搜索补充

| # | 工具 | 论文 | GitHub | 权重 | 能力 |
|---|------|------|--------|------|------|
| 77 | **PaNSegNet** | NUBagciLab | [NUBagciLab/PaNSegNet](https://github.com/NUBagciLab/PaNSegNet) | ✅ Google Drive | 胰腺分割（CT+MRI） |
| 78 | **livermask** | Pedersen & Pérez de Frutos | [andreped/livermask](https://github.com/andreped/livermask) | ✅ pip install | 肝实质分割 (Dice 0.946) |

### 确认不存在的场景（穷尽搜索）

| 场景 | 搜索次数 | 结论 |
|------|---------|------|
| 肠梗阻检测 | 8 次 WebSearch | ❌ 无开源工具。最近替代：RSNA 2023 肠损伤(#64) |
| 阑尾炎检测 | 9 次 WebSearch | ❌ 无。阑尾不在任何现有分割工具标签列表中 |
| CT 气胸检测 | 9 次 WebSearch | ❌ 无。EFA-Net repo 已 404；仅有 X 光版本 |
| LI-RADS 自动评分 | 7 次 WebSearch | ❌ 无。论文有但代码全未公开 |
| 胰腺炎 CTSI | 6 次 WebSearch | ❌ 无。DenseNet 论文(Sci Rep 2023)未释出权重 |

---

---

## I. 第三轮搜索新增——检测/分类/比赛方案/中文平台

### I1. 检测工具（有权重）

| # | 工具 | 论文 | GitHub | 权重 | 能力 |
|---|------|------|--------|------|------|
| 79 | **nnDetection (淋巴结)** | Baumgartner, MICCAI 2021 | [MIC-DKFZ/nnDetection](https://github.com/MIC-DKFZ/nnDetection) Task025 | ✅ 有下载链接 | 淋巴结 3D 检测 |
| 80 | **ct_mediastinal_structures** | Bouget et al. | [dbouget/ct_mediastinal_structures_segmentation](https://github.com/dbouget/ct_mediastinal_structures_segmentation) | ✅ 多个模型 + Docker | 纵隔淋巴结分割+检测 |
| 81 | **Ascites Model** | Summers, Radiology:AI 2024 | [rsummers11/Ascites](https://github.com/rsummers11/Ascites) + [HuggingFace](https://huggingface.co/farrell236/AscitesModel) | ✅ HuggingFace | 腹水检测+体积量化 |
| 82 | **pleuraleffusion** | Sexauer, Invest Radiol 2022 | [usb-radiology/pleuraleffusion](https://github.com/usb-radiology/pleuraleffusion) | ✅ nnU-Net 模型 | 胸腔积液检测+分割+分类 |
| 83 | **liver lesion detection** | Bellver, NIPS ML4H 2017 | [imatge-upc/liverseg-2017-nipsws](https://github.com/imatge-upc/liverseg-2017-nipsws) | ✅ checkpoints | 肝脏病灶检测（含检测分支） |

### I2. 分类工具（有权重）

| # | 工具 | 论文 | GitHub | 权重 | 能力 |
|---|------|------|--------|------|------|
| 84 | **PanDx** | Han Liu, PANORAMA 1st | [han-liu/PanDx](https://github.com/han-liu/PanDx) | ✅ 有模型 | 胰腺癌检测 (AUROC 0.926) |
| 85 | **CE-CT PDAC Detection** | DIAG Nijmegen | [DIAGNijmegen/CE-CT_PDAC_AutomaticDetection_nnUnet](https://github.com/DIAGNijmegen/CE-CT_PDAC_AutomaticDetection_nnUnet) | ✅ 10 个模型 | PDAC 自动检测 (242 例) |
| 86 | **AI-in-Lung-Health** | Tushar et al. | [fitushar/AI-in-Lung-Health...](https://github.com/fitushar/AI-in-Lung-Health-Benchmarking-Detection-and-Diagnostic-Models-Across-Multiple-CT-Scan-Datasets) | ✅ 多种 backbone | 肺结节恶性分类 (AUC 0.71-0.90) |
| 87 | **Kidney Tumor Clf** | Alzubi et al. | [DaliaAlzubi/Kidney_Tumor_Detection_And_Classification](https://github.com/DaliaAlzubi/Kidney_Tumor_Detection_And_Classification) | ✅ CNN/ResNet/VGG | 肾脏肿瘤检测+分类 (97% det) |
| 88 | **Lung Nodule Clf** | Fazil-kagdi | [Fazil-kagdi/lung-nodule-segmentation-classification](https://github.com/Fazil-kagdi/lung-nodule-segmentation-classification) | ✅ UNet+ResNet18 | 肺结节分割+恶性分类 (~85%) |

### I3. Grand Challenge 比赛方案（有权重）

| # | 工具 | 比赛 | GitHub | 权重 | 能力 |
|---|------|------|--------|------|------|
| 89 | **FLARE22 Champion** | FLARE 2022 | [Ziyan-Huang/FLARE22](https://github.com/Ziyan-Huang/FLARE22) | ✅ 百度盘 | 腹部 13 器官分割 |
| 90 | **HECKTOR 2020 Winner** | HECKTOR | [iantsen/hecktor](https://github.com/iantsen/hecktor) | ✅ 8 fold 权重 | 头颈肿瘤 PET/CT 分割 |
| 91 | **autoPET III (DKFZ)** | autoPET | [MIC-DKFZ/autopet-3-submission](https://github.com/MIC-DKFZ/autopet-3-submission) | ✅ checkpoint | 全身肿瘤 PET/CT 分割 |
| 92 | **SEG.A Winner** | SEG.A 2023 | [MWod/SEGA_MW_2023](https://github.com/MWod/SEGA_MW_2023) | ✅ 预训练模型 | 主动脉分割 (Dice 0.920) |
| 93 | **STOIC 2nd Place** | STOIC 2021 | [KieDani/Submission_2nd_Covid19_Competition](https://github.com/KieDani/Submission_2nd_Covid19_Competition) | ✅ download script | COVID 严重程度预测 |
| 94 | **AbdomenCT-1K** | AbdomenCT-1K | [JunMa11/AbdomenCT-1K](https://github.com/JunMa11/AbdomenCT-1K) | ✅ baseline 模型 | 肝/肾/脾/胰分割 (1K+ 例) |
| 95 | **Parse2022** | Parse 2022 | [MICLab-Unicamp/medseg](https://github.com/MICLab-Unicamp/medseg) | ✅ .ckpt 权重 | 肺动脉分割 |
| 96 | **LUNA16** | LUNA16 | [nauyan/Luna16](https://github.com/nauyan/Luna16) | ✅ Google Drive | 肺结节检测 |

### I4. 中文平台 + 基础模型

| # | 工具 | 论文 | GitHub / 平台 | 权重 | 能力 |
|---|------|------|-------------|------|------|
| 97 | **CT-SAM3D** (达摩院) | Alibaba DAMO | [alibaba-damo-academy/ct-sam3d](https://github.com/alibaba-damo-academy/ct-sam3d) + ModelScope | ✅ ModelScope 下载 | 107 类交互式 3D 分割 |
| 98 | **STU-Net** | arXiv:2304.06716 | [uni-medical/STU-Net](https://github.com/uni-medical/STU-Net) | ✅ S/B/L/H 全尺寸 | 最大 1.4B 参数 CT 分割 |
| 99 | **MIS-FM** | OpenMEDLab | [openmedlab/MIS-FM](https://github.com/openmedlab/MIS-FM) | ✅ Google Drive | 腹部+胸部分割预训练 |
| 100 | **CT-GRAPH** | ICCV Workshop 2025 | [hakal104/CT-GRAPH](https://github.com/hakal104/CT-GRAPH) | ✅ LoRA 权重 | 解剖引导 CT 报告生成 (+7.9% F1) |
| 101 | **UniverSeg** | ICCV 2023 | [JJGO/UniverSeg](https://github.com/JJGO/UniverSeg) | ✅ `universeg(pretrained=True)` | 少样本分割（无需重训） |
| 102 | **Models Genesis** | MICCAI 2019 Best + MEDIA 2020 | [MrGiovanni/ModelsGenesis](https://github.com/MrGiovanni/ModelsGenesis) | ✅ 2D+3D 权重 | 经典 CT 自监督预训练 (1000+ cites) |
| 103 | **PUMIT** | arXiv | [function2-llx/PUMIT](https://github.com/function2-llx/PUMIT) | ✅ GitHub Releases | 通用医学图像 Transformer (55 数据集) |
| 104 | **GrayNet** | MGH-LMIC | [MGH-LMIC/graynet_keras](https://github.com/MGH-LMIC/graynet_keras) | ✅ Keras 权重 | CT 专用 DenseNet121 预训练 |

---

## 合计：104 个可直接包装为 MCP 的工具

| 类别 | 数量 |
|------|------|
| A. 影像分割 | 18 |
| B. 影像检测/分类 | 4 |
| C. 多模态 VLM/报告 | 8 |
| D. 基础模型/backbone | 5 |
| E. 工具库 | 6 |
| F. 文本 NLP | 6 |
| G. pip 可安装 | 9 |
| H. 精确搜索新增 | 22 |
| I. 第三轮新增 | 26 |
| **合计** | **104** |
