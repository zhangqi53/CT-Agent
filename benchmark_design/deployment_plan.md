# CT-Agent MCP 工具部署计划

> 125 个工具 → 3 个 Docker 容器 + LLM API
>
> 更新日期：2026-03-26

---

## 1. 容器架构总览

```
┌──────────────────────────────────────────────────────┐
│                   MCP Gateway                         │
│        (路由层：接收 agent 调用，分发到容器)            │
└───────┬──────────┬──────────┬──────────┬─────────────┘
        │          │          │          │
   ┌────▼────┐ ┌──▼────┐ ┌──▼────┐ ┌───▼────────┐
   │gpu-main │ │gpu-xl │ │  cpu  │ │ LLM API    │
   │ 66 tools│ │4 tools│ │24 tool│ │ (外部调用)  │
   │ 8-24GB  │ │ ≥40GB │ │ 0 GPU │ │ OpenAI/等  │
   └─────────┘ └───────┘ └───────┘ └────────────┘
```

---

## 2. 容器一：gpu-main（常规 GPU）

**镜像基础**：`nvcr.io/nvidia/pytorch:24.05-py3`（PyTorch 2.3 + CUDA 12.4 + Python 3.10）

**硬件需求**：NVIDIA GPU ≥ 16GB VRAM（推荐 A5000/A6000/L40），RAM ≥ 64GB，SSD ≥ 500GB

### 2.1 影像分割工具（18 个）

| # | 工具 | pip / 安装方式 | 权重来源 | VRAM | 输入 | 输出 |
|---|------|--------------|---------|------|------|------|
| 1 | TotalSegmentator | `pip install TotalSegmentator` | 自动下载 ~/.totalsegmentator | 4GB | NIfTI | NIfTI mask + JSON stats |
| 2 | CADS | `pip install cads` 或 GitHub clone | GitHub Releases ~3GB | 6GB | NIfTI | 167 类 NIfTI mask |
| 3 | MONAI VISTA3D | `monai.bundle.download("vista3d")` | HuggingFace MONAI/VISTA3D-HF | 8GB | NIfTI + prompt | NIfTI mask |
| 4 | nnU-Net v2 | `pip install nnunetv2` | 各任务权重单独下载 | 4-8GB | NIfTI | NIfTI mask |
| 5 | MedSAM | GitHub clone + `pip install -e .` | Google Drive checkpoint | 6GB | NIfTI + bbox/point prompt | NIfTI mask |
| 6 | SAM-Med3D-turbo | GitHub clone | HuggingFace blueyo0/SAM-Med3D | 8GB | NIfTI + point prompt | NIfTI mask |
| 7 | MedSAM2 | GitHub clone | HuggingFace wanglab/MedSAM2 | 6GB | NIfTI + prompt | NIfTI mask |
| 8 | lungmask | `pip install lungmask` | 自动下载 | 2GB | NIfTI | NIfTI mask (肺/肺叶) |
| 9 | MULLET | GitHub clone | Google Drive | 4GB | 多期 NIfTI | NIfTI mask (肝脏病灶) |
| 10 | TotalSpineSeg | `pip install totalspineseg` | 内置 | 4GB | NIfTI | NIfTI mask (椎体/椎间盘/脊髓) |
| 11 | Skellytour | GitHub clone + `pip install .` | 自动下载 ~1.2GB/model | 4GB | NIfTI | NIfTI mask (17/38/60 骨标签) |
| 12 | OvSeg | `pip install ovseg` | 自动下载 3 模型 | 4GB | NIfTI | NIfTI mask (卵巢癌多部位) |
| 13 | livermask | `pip install livermask` | 自动下载 | 2GB | NIfTI | NIfTI mask (肝实质) |
| 14 | FracSegNet | GitHub clone | 权重下载 | 4GB | NIfTI | NIfTI mask (骨盆骨折) |
| 15 | CTPelvic1K | GitHub clone | baseline 模型 | 4GB | NIfTI | NIfTI mask (骨盆骨骼) |
| 16 | U-SAM/CARE | GitHub clone | 代码+数据 | 4GB | NIfTI | NIfTI mask (直肠癌) |
| 17 | HiLab Head-Neck-GTV | GitHub clone | 百度盘 | 4GB | NIfTI | NIfTI mask (鼻咽癌 GTV) |
| 18 | Parotid Seg | GitHub clone | 内置权重 | 2GB | NIfTI | NIfTI mask (腮腺) |

### 2.2 MONAI Bundle 模型（9 个，统一接口）

| # | Bundle 名 | 下载命令 | 覆盖部位 | VRAM |
|---|----------|---------|---------|------|
| 19 | lung_nodule_ct_detection | `monai.bundle.download(...)` | 肺（结节检测） | 4GB |
| 20 | spleen_ct_segmentation | 同上 | 脾脏 | 2GB |
| 21 | pancreas_ct_dints_segmentation | 同上 | 胰腺+肿瘤 | 4GB |
| 22 | swin_unetr_btcv_segmentation | 同上 | 腹部 13 器官 | 6GB |
| 23 | multi_organ_segmentation | 同上 | 腹部 7 器官 | 4GB |
| 24 | renalStructures_CECT_segmentation | 同上 | 肾脏结构 | 4GB |
| 25 | renalStructures_UNEST_segmentation | 同上 | 肾脏皮质/髓质 | 4GB |
| 26 | wholeBody_ct_segmentation | 同上 | 全身 104 类 | 6GB |
| 27 | pediatric_abdominal_ct_segmentation | 同上 | 儿童腹部 | 4GB |

### 2.3 影像检测/分类工具（16 个）

| # | 工具 | 安装方式 | 覆盖 | VRAM |
|---|------|---------|------|------|
| 28 | RSNA ICH 1st | GitHub clone | 脑 ICH 5 亚型分类 | 4GB |
| 29 | BLAST-CT | `pip install blast-ct` | 脑 TBI 检测+分割 | 4GB |
| 30 | DeepBleed | GitHub clone | 脑 ICH 分割+体积 | 4GB |
| 31 | PENet | GitHub clone | 肺栓塞检测 | 4GB |
| 32 | PanDx | GitHub clone | 胰腺癌检测 (PANORAMA 1st) | 4GB |
| 33 | CE-CT PDAC Detection | GitHub clone | PDAC 检测 (10 模型) | 4GB |
| 34 | AI-in-Lung-Health | GitHub clone | 肺结节恶性分类 | 4GB |
| 35 | Lung Nodule Clf | GitHub clone | 肺结节分割+分类 | 2GB |
| 36 | Kidney Tumor Clf | GitHub clone | 肾脏肿瘤检测+分类 | 2GB |
| 37 | CT Colonography Polyp | GitHub clone | CTC 息肉良恶性 | 2GB |
| 38 | Maskrcnn_RibFrac | GitHub clone | 肋骨骨折检测 | 4GB |
| 39 | VCFNet | GitHub clone | 椎体压缩骨折分类 | 2GB |
| 40 | sato_j-mid_ad | GitHub clone | 多器官异常检测(7 器官) | 4GB |
| 41 | DL_BoneLesion (NIH) | GitHub clone | 骨转移检测+分类 | 4GB |
| 42 | pleuraleffusion | GitHub clone | 胸腔积液检测+分割+分类 | 4GB |
| 43 | Ascites Model | GitHub clone | 腹水检测+体积量化 | 4GB |

### 2.4 纵向追踪/配准工具（5 个）

| # | 工具 | 安装方式 | 覆盖 | VRAM |
|---|------|---------|------|------|
| 44 | LesionLocator | GitHub clone | 全身肿瘤纵向追踪 (CVPR 2025) | 8GB |
| 45 | uniGradICON | `pip install unigradicon` | CT 形变配准基础模型 | 4GB |
| 46 | detect-then-track | GitHub clone | RECIST 纵向评估 (肝脏) | 4GB |
| 47 | LongiSeg | GitHub clone | 纵向分割 (时间差异加权) | 4GB |
| 48 | RAMAC (FDA) | GitHub clone | 病灶匹配 (经典算法) | CPU |

### 2.5 分期/分级工具（6 个）

| # | 工具 | 安装方式 | 覆盖 | VRAM |
|---|------|---------|------|------|
| 49 | StrokeViT | GitHub clone | ASPECTS 卒中评分 | 2GB |
| 50 | Acute-stroke Pipeline | GitHub clone | 卒中检测+分割 | 2GB |
| 51 | NoduleNet | GitHub clone | 肺结节检测+分割 | 4GB |
| 52 | RadiomicsLiverFibrosis | GitHub clone | 肝纤维化分级 | CPU |
| 53 | GTRNet | GitHub clone | 胃癌 T 分期 (Zenodo 权重) | 4GB |
| 54 | RSNA Trauma 1st | GitHub clone | 脾/肝/肾损伤分级 | 8GB |

### 2.6 Grand Challenge 方案（8 个）

| # | 工具 | 安装方式 | 覆盖 | VRAM |
|---|------|---------|------|------|
| 55 | FLARE22 Champion | GitHub clone | 腹部 13 器官分割 | 6GB |
| 56 | HECKTOR 2020 Winner | GitHub clone | 头颈肿瘤 PET/CT | 4GB |
| 57 | autoPET III (DKFZ) | GitHub clone | 全身肿瘤 PET/CT | 8GB |
| 58 | SEG.A Winner | GitHub clone | 主动脉分割 | 4GB |
| 59 | STOIC 2nd Place | GitHub clone | COVID 严重程度预测 | 4GB |
| 60 | AbdomenCT-1K | GitHub clone | 肝/肾/脾/胰分割 | 4GB |
| 61 | Parse2022 | GitHub clone | 肺动脉分割 | 4GB |
| 62 | LUNA16 | GitHub clone | 肺结节检测 | 4GB |

### 2.7 基础模型/Backbone（6 个）

| # | 工具 | 安装方式 | 用途 | VRAM |
|---|------|---------|------|------|
| 63 | CT-FM (Harvard) | GitHub clone | CT 自监督基础模型 (148K CT) | 8GB |
| 64 | SuPreM | GitHub clone | 预训练 backbone (ICLR 2024) | 6GB |
| 65 | STU-Net | GitHub clone | 1.4B 参数分割模型 | 12GB |
| 66 | CT-SAM3D (达摩院) | GitHub clone | 107 类交互式分割 | 8GB |
| 67 | Models Genesis | GitHub clone | 经典 CT 预训练 | 4GB |
| 68 | PUMIT | GitHub clone | 通用医学图像 Transformer | 6GB |

**gpu-main 合计：68 个工具**

---

## 3. 容器二：gpu-large（大显存 GPU）

**镜像基础**：`nvcr.io/nvidia/pytorch:24.05-py3`（同 gpu-main）

**硬件需求**：NVIDIA A100 80GB 或 H100（≥40GB VRAM），RAM ≥ 128GB

| # | 工具 | 安装方式 | VRAM | 用途 |
|---|------|---------|------|------|
| 69 | **Merlin** | `pip install merlin-vlm` | 40GB+ | 30 发现零样本分类 + 报告生成 + 分割 |
| 70 | **RadFM** | GitHub clone | 80GB (A100) | 通用放射 VLM (诊断/VQA/报告/鉴别) |
| 71 | **MedGemma 1.5** | HuggingFace download | 40GB+ | 3D CT VQA + 报告生成 |
| 72 | **BiomedGPT** | GitHub clone | 40GB+ | 通用生物医学多模态 |

**gpu-large 合计：4 个工具**

---

## 4. 容器三：cpu（纯 CPU）

**镜像基础**：`python:3.10-slim` + 系统依赖

**硬件需求**：CPU ≥ 8 核，RAM ≥ 32GB，SSD ≥ 100GB

### 4.1 工具库（无需模型权重）

| # | 工具 | pip 命令 | 功能 |
|---|------|---------|------|
| 73 | pyradiomics | `pip install pyradiomics` | 1500+ 影像组学特征 |
| 74 | ANTsPy | `pip install antspyx` | 配准（刚性/仿射/SyN） |
| 75 | SimpleITK | `pip install SimpleITK` | 格式转换/窗宽窗位/重采样 |
| 76 | pydicom | `pip install pydicom` | DICOM tag 读写 |
| 77 | vmtk | `pip install vmtk` | 血管分析（中心线/截面积） |
| 78 | WORC | `pip install WORC` | 自动化影像组学分类流水线 |

### 4.2 NLP 文本工具

| # | 工具 | pip 命令 | 功能 |
|---|------|---------|------|
| 79 | medspaCy | `pip install medspacy` | 临床 NER + ConText 否定检测 |
| 80 | NegBio | `pip install negbio` | 否定/不确定检测 |
| 81 | CheXbert | GitHub clone | 报告 14 类标签分类 (BERT) |
| 82 | RadGraph-XL | `pip install radgraph` | 报告 NER + 关系抽取 |
| 83 | Radiology_Bart | HuggingFace download | 报告 Findings→Impression 摘要 |
| 84 | SARLE | GitHub clone | 83 异常 × 52 部位文本标签 |
| 85 | FaMeSumm | GitHub clone | 多器官报告摘要 |
| 86 | multi-label-body-ct | GitHub clone | 3 系统多标签分类 |

### 4.3 适配/胶水工具

| # | 工具 | pip 命令 | 功能 |
|---|------|---------|------|
| 87 | dicom2nifti | `pip install dicom2nifti` | DICOM→NIfTI |
| 88 | cc3d | `pip install connected-components-3d` | 3D 连通域过滤 |
| 89 | highdicom | `pip install highdicom` | DICOM SR/SEG 创建 |
| 90 | fhirpy | `pip install fhirpy fhir.resources` | HL7 FHIR 导出 |
| 91 | TorchIO | `pip install torchio` | 预处理/增强流水线 |
| 92 | nibabel | `pip install nibabel` | NIfTI/MGZ 读写 |

### 4.4 其他 CPU 工具

| # | 工具 | 安装 | 功能 |
|---|------|------|------|
| 93 | Comp2Comp | GitHub clone | 体成分 + 骨密度 + 主动脉钙化 |
| 94 | bpreg | `pip install bpreg` | CT 体区识别 |
| 95 | body-organ-analysis | `pip install body-organ-analysis` | 全身器官+体成分 |
| 96 | DeepCAC | GitHub clone | 冠脉钙化定量 |
| 97 | AI-CAC | GitHub clone | 非门控钙化评分 |
| 98 | SEGMENT-CACS | GitHub clone | 冠脉段级钙化评分 |
| 99 | KiTS23 2nd Place | GitHub clone | 肾脏/肿瘤/囊肿分割评估 |
| 100 | AbdomenAtlas | GitHub clone | 25 器官分割 backbone |
| 101 | OrganSegRSTN | GitHub clone | 小器官分割（肾上腺） |
| 102 | PACT-3D | GitHub clone | 气腹检测 |
| 103 | liver lesion detection | GitHub clone | 肝脏病灶检测 |
| 104 | ct_mediastinal_structures | GitHub clone + Docker | 纵隔淋巴结分割 |

**cpu 合计：32 个工具**

---

## 5. LLM API 调用（无需本地部署）

| # | 工具 | API | 功能 |
|---|------|-----|------|
| 105 | llm_extractinator | Ollama API / OpenAI API | 报告测量值/纵向抽取 |
| 106 | LEAVS | Qwen2-72B API | 9 腹部器官文本异常抽取 |

---

## 6. 多模态 VLM 报告工具（gpu-main 或 gpu-large）

| # | 工具 | 部署容器 | VRAM | 功能 |
|---|------|---------|------|------|
| 107 | CT-CLIP | gpu-main | 8GB | 零样本 18 病变分类 (胸部) |
| 108 | CT-CHAT | gpu-main | 16GB | CT VQA + 报告 (胸部) |
| 109 | M3D-LaMed | gpu-main | 16GB | 3D VLM 多任务 |
| 110 | Med3DVLM | gpu-main | 16GB | 3D VLM（优于 M3D） |
| 111 | FORTE/BrainGPT | gpu-main | 8GB | 脑 CT 报告生成 |
| 112 | RadGPT | gpu-main | 16GB | 腹部 CT 肿瘤报告 |
| 113 | CT-GRAPH | gpu-main | 16GB | 解剖引导报告生成 |
| 114 | UniverSeg | gpu-main | 4GB | 少样本分割 |
| 115 | GrayNet | gpu-main | 2GB | CT DenseNet121 backbone |
| 116 | MIS-FM | gpu-main | 4GB | 腹部+胸部分割预训练 |
| 117 | PaNSegNet | gpu-main | 4GB | 胰腺分割 |
| 118 | MI_prediction | gpu-main | 4GB | 冠脉狭窄→心梗预测 |

---

## 7. 不部署（砍掉）

| 工具 | 原因 |
|------|------|
| DeepCAC (旧版) | Python 2.7 + CUDA 10.1，严重过时 |
| GrayNet (Keras) | Keras 旧版，已被 Med3D/SuPreM 替代 |
| DeepMedic | Theano 后端，已停更 |

---

## 8. 部署流程

### 8.1 构建阶段

```
Phase 1: 基础镜像 (Day 1-2)
├── gpu-main: nvcr.io/nvidia/pytorch:24.05-py3 + 共用依赖
├── gpu-large: 同上
└── cpu: python:3.10-slim + 系统依赖

Phase 2: 工具安装 (Day 3-5)
├── pip install 类: 一次 requirements.txt 搞定
├── GitHub clone 类: 批量 clone + pip install -e .
└── 权重下载: 并行下载到共享存储

Phase 3: MCP 接口封装 (Day 6-10)
├── 每个工具写一个 MCP tool 定义 (name/description/inputSchema/outputSchema)
├── 统一输入: volume_id / text / mask_id → 内部路由到具体工具
└── 统一输出: JSON (结构化结果) + NIfTI (mask/volume)

Phase 4: 测试 (Day 11-14)
├── 每个工具单独测试 (sample input → expected output)
├── 端到端流水线测试 (DICOM → 分割 → 测量 → 报告)
└── 负载/并发测试
```

### 8.2 存储规划

| 存储 | 用途 | 估算大小 |
|------|------|---------|
| 模型权重 | 所有工具的预训练权重 | ~200GB |
| 工具代码 | GitHub repos + pip 包 | ~20GB |
| 临时数据 | 推理中间结果 (NIfTI/JSON) | ~100GB (可清理) |
| 评测数据 | benchmark 数据集 | ~500GB |
| **合计** | | **~820GB SSD** |

### 8.3 网络架构

```
Agent (LLM)
    │
    ▼
MCP Gateway (FastAPI / gRPC)
    │
    ├── /tools/list          → 返回所有可用工具
    ├── /tools/{name}/call   → 路由到对应容器
    │
    ├── gpu-main:8001  ─── PyTorch 推理服务
    ├── gpu-large:8002 ─── 大模型推理服务
    ├── cpu:8003       ─── CPU 工具服务
    └── LLM API        ─── 外部调用 (OpenAI/Anthropic/Ollama)
```

---

## 9. 资源需求汇总

| 项目 | 最低配置 | 推荐配置 |
|------|---------|---------|
| GPU (gpu-main) | 1× A5000 24GB | 2× A6000 48GB |
| GPU (gpu-large) | 1× A100 80GB | 1× H100 80GB |
| CPU | 16 核 | 32 核 |
| RAM | 128GB | 256GB |
| SSD | 1TB | 2TB NVMe |
| 网络 | 1Gbps | 10Gbps (权重下载) |
