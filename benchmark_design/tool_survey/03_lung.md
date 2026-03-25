# CT Benchmark Tool Survey -- Body Region: 肺 (Lung)

## Image Tasks (IMG-T)

### IMG-T1 异常筛查 (Anomaly Screening)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| **WSAD** | Hibi et al., "Automated screening of CT using weakly supervised anomaly detection," IJCARS, 2023 | https://github.com/hibiat/wsad | AUC superior to conventional anomaly detection on brain/lung CT |
| **AI-in-Lung-Health** | Tushar et al., "VLST: Virtual Lung Screening Trial," Medical Imaging (SPIE), 2024 | https://github.com/fitushar/AI-in-Lung-Health-Benchmarking-Detection-and-Diagnostic-Models-Across-Multiple-CT-Scan-Datasets | Benchmarked on DLCSD, LUNA16, NLST |

---

### IMG-T2 病灶检测 (Lesion Detection: nodules / PE / etc.)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| **DeepLung** | Zhu et al., "DeepLung: Deep 3D Dual Path Nets for Automated Pulmonary Nodule Detection and Classification," WACV, 2018 | https://github.com/wentaozhu/DeepLung | FROC CPM 84.2% (LUNA16) |
| **nnDetection** | Baumgartner et al., "nnDetection: A Self-configuring Method for Medical Object Detection," MICCAI, 2021 | https://github.com/MIC-DKFZ/nnDetection | SOTA on LUNA16 & ADAM; self-configuring |
| **MONAI Lung Nodule Detection** | Myronenko et al. (NVIDIA/MONAI), MONAI Model Zoo bundle, 2022 | https://github.com/Project-MONAI/tutorials (bundle: lung_nodule_ct_detection) | RetinaNet-based; trained on LUNA16 |
| **PENet** (PE) | Huang et al., "PENet -- a scalable deep-learning model for automated diagnosis of PE," npj Digital Medicine, 2020 | https://github.com/marshuang80/penet | AUROC 0.84 (internal), 0.85 (external) |
| **Turku PE Detection** (PE) | Huhtanen et al., "Automated detection of PE from CT-angiograms using deep learning," BMC Medical Imaging, 2022 | https://github.com/turku-rad-ai/pe-detection | Weakly-labelled; InceptionResNetV2+LSTM |
| **Medical Detection Toolkit** | Jaeger et al., "Retina U-Net: Embarrassingly Simple Exploitation of Segmentation Supervision for Medical Object Detection," arXiv 1811.08661, 2018 | https://github.com/MIC-DKFZ/medicaldetectiontoolkit | Retina U-Net, Mask R-CNN, Faster R-CNN |

---

### IMG-T3 病灶分割 (Lesion Segmentation)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| **nnU-Net** | Isensee et al., "nnU-Net: a self-configuring method for DL-based biomedical image segmentation," Nature Methods, 2021 | https://github.com/MIC-DKFZ/nnUNet | SOTA across multiple segmentation benchmarks |
| **TotalSegmentator** | Wasserthal et al., "TotalSegmentator: Robust Segmentation of 104 Anatomic Structures in CT Images," Radiology: AI, 2023 | https://github.com/wasserth/TotalSegmentator | Dice 0.943 avg; includes lung_nodules subtask |
| **PET-CT Lung Tumor Seg** | Carles et al., "Development and evaluation of two open-source nnU-Net models for lung tumor segmentation," Eur Radiol, 2024 | https://github.com/MonCarFa/PET-CT-Lung-Segmentation-Models | DSC 0.61-0.63 on lung tumors |

---

### IMG-T4 分类/良恶性 (Nodule Malignancy Classification)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| **DeepLung** | Zhu et al., "DeepLung: Deep 3D Dual Path Nets," WACV, 2018 | https://github.com/wentaozhu/DeepLung | Nodule classification accuracy surpasses radiologists on LIDC-IDRI |
| **C-Lung-RADS** | Data-driven risk stratification of pulmonary nodules, Nature Medicine, 2024 | https://github.com/simonsf/C-Lung-RADS | AUC 0.918 (internal test); 45,064-case cohort |

---

### IMG-T5 测量/定量 (Measurement / Quantification)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| **ACM-LSTK** (Accumetra Lesion Sizing Toolkit) | Avila et al., "An open-source toolkit for the volumetric measurement of CT lung lesions," Optics Express, 2010 | https://github.com/accumetra/ACM-LSTK | Meets QIBA CT small lung nodule profile; validated on phantom |
| **ITK LesionSizingToolkit** | Same as above (ITK module version) | https://github.com/InsightSoftwareConsortium/LesionSizingToolkit | Modular ITK-based; `pip install itk-lesionsizingtoolkit` |

---

### IMG-T6 解剖结构 (Lobe / Airway Segmentation)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| **lungmask** | Hofmanninger et al., "Automatic lung segmentation in routine imaging is primarily a data diversity problem," Eur Radiol Exp, 2020 | https://github.com/JoHof/lungmask | Dice 0.97+; 5-lobe segmentation; pip-installable |
| **TotalSegmentator** | Wasserthal et al., Radiology: AI, 2023 | https://github.com/wasserth/TotalSegmentator | 117 structures including lobes |
| **ATM'22 Challenge** (Airway) | Zhang et al., "Multi-site, Multi-domain Airway Tree Modeling," Medical Image Analysis, 2023 | https://github.com/EndoluminalSurgicalVision-IMR/ATM-22-Related-Work | 500 CTs; TD/BD metrics; curated SOTA collection |
| **AeroPath** (Airway) | Aeropath benchmark, PLOS ONE, 2024 | https://github.com/raidionics/AeroPath | 27 CTs with challenging pathology; nnU-Net baseline |
| **BronchiNet** (Airway) | Garcia-Uceda et al., "Automatic airway segmentation from CT using robust 3D CNNs," Scientific Reports, 2021 | https://github.com/antonioguj/bronchinet | 3D U-Net based airway extraction |

---

### IMG-T7 对比随访 (Nodule Tracking / Longitudinal Comparison)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| **ACM-LSTK** | Avila et al., Optics Express, 2010 (supports longitudinal volumetry) | https://github.com/accumetra/ACM-LSTK | Volume change measurement over time |

> Note: Dedicated open-source deep-learning tools specifically for nodule matching/registration across longitudinal CT scans are very limited. Commercial CAD systems (e.g., Veye, AVIEW) perform this but are not open-source.

---

### IMG-T8 报告生成 (Report Generation)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| **CT2Rep** | Hamamci et al., "CT2Rep: Automated Radiology Report Generation for 3D Medical Imaging," MICCAI, 2024 | https://github.com/ibrahimethemhamamci/CT2Rep | First 3D CT report generation; trained on CT-RATE |
| **CT-CHAT** | Hamamci et al., Nature Biomedical Engineering, 2025 | https://github.com/ibrahimethemhamamci/CT-CHAT | VQA + report generation for 3D chest CT; LLaVA-based |
| **M3D-LaMed** | Bai et al., "M3D: Advancing 3D Medical Image Analysis with Multi-Modal LLMs," arXiv 2404.00578, 2024 | https://github.com/BAAI-DCAI/M3D | 120K image-text pairs; 8-task generalist model |

---

### IMG-T9 分期/分级 (Lung-RADS)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| **C-Lung-RADS** | "Data-driven risk stratification and precision management of pulmonary nodules," Nature Medicine, 2024 | https://github.com/simonsf/C-Lung-RADS | AUC 0.918; stepwise risk grading (low/mid/high/extremely-high) |

---

### IMG-T11 扫描质量 (Scan Quality)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| **Noise2Quality (N2Q)** | Haque et al., "Noise2Quality: Non-Reference, Pixel-Wise Assessment of Low Dose CT Image Quality," SPIE Medical Imaging, 2022 | https://github.com/ayaanzhaque/Noise2Quality | Self-supervised; pixel-wise IQA on LDCT |

---

### IMG-T12 关键发现 (Critical Findings: PE / Pneumothorax)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| **PENet** (PE) | Huang et al., npj Digital Medicine, 2020 | https://github.com/marshuang80/penet | AUROC 0.84-0.85 |
| **Turku PE Detection** (PE) | Huhtanen et al., BMC Medical Imaging, 2022 | https://github.com/turku-rad-ai/pe-detection | InceptionResNetV2+LSTM on CTPA |
| **RSNA PE 2nd Place** (PE) | Pan et al., "Deep Learning for PE Detection: Tackling the RSNA 2020 AI Challenge," Radiology: AI, 2021 | https://github.com/i-pan/kaggle-rsna-pe | Top-2 on 9000+ CTPA exams |

> Note: For **pneumothorax on CT**, EFA-Net (Sci Rep, 2023) reports Dice 90.03% but has no public GitHub repo. Most open-source pneumothorax tools target CXR, not CT.

---

## Text Tasks (TXT-T)

### TXT-T1 信息抽取 (Information Extraction / NER)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| **RadGraph / RadGraph-XL** | Jain et al., "RadGraph-XL: A Large-Scale Expert-Annotated Dataset for Entity and Relation Extraction from Radiology Reports," ACL Findings, 2024 | https://github.com/Stanford-AIMI/radgraph | 410K+ entities; covers chest CT; outperforms GPT-4 by up to 52% |
| **NegBio** | Peng et al., "NegBio: a high-performance tool for negation and uncertainty detection in radiology reports," AMIA, 2018 | https://github.com/ncbi-nlp/NegBio | High-performance negation/uncertainty detection |
| **GLiNER** | Zaratiana et al., "GLiNER: Generalist Model for Named Entity Recognition," NAACL, 2024 | https://github.com/urchade/GLiNER | Zero-shot NER; GLiNER-biomed F1 59.77% |

---

### TXT-T2 文本分类 (Text Classification)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| **CheXbert** | Smit et al., "CheXbert: Combining Automatic Labelers and Expert Annotations for Accurate Radiology Report Labeling Using BERT," EMNLP, 2020 | https://github.com/stanfordmlgroup/CheXbert | Trained on 187K reports; multi-label classification |
| **CheXpert Labeler** | Irvin et al., "CheXpert: A Large Chest Radiograph Dataset with Uncertainty Labels," AAAI, 2019 | https://github.com/stanfordmlgroup/chexpert-labeler | Rule-based; extracts 14 observations |
| **RAD-BERT** | Chambon et al., "Highly accurate classification of chest radiographic reports using a deep learning NLP model," Bioinformatics, 2021 | https://github.com/fast-raidiology/bert-for-radiology | AUC 0.97-0.99 for key findings (pneumothorax, consolidation, etc.) |

---

### TXT-T4 报告摘要 (Report Summarization)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| **Summarize Radiology Findings** | Zhang et al., "Learning to Summarize Radiology Findings," EMNLP, 2018 | https://github.com/yuhaozhang/summarize-radiology-findings | Pretrained on 4.5M Stanford reports; Findings-to-Impression |
| **XrayGPT** | Thawkar et al., "XrayGPT: Chest Radiographs Summarization using Medical Vision-Language Models," BioNLP-ACL, 2024 | https://github.com/mbzuai-oryx/XrayGPT | 217K report summaries; MedClip+Vicuna |

---

### TXT-T5 报告生成 (Text-based Report Generation / Drafting)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| **R2Gen** | Chen et al., "Generating Radiology Reports via Memory-driven Transformer," EMNLP, 2020 | https://github.com/cuhksz-nlp/R2Gen | Memory-driven Transformer; IU X-Ray & MIMIC-CXR |

> Note: Most report generation tools are multimodal (image+text); see IMG-T8 and MM-T8 sections.

---

### TXT-T7 质量控制 / 错误检测 (Report QC / Error Detection)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| **RaTEScore** | Zhao et al., "RaTEScore: A Metric for Radiology Report Generation," EMNLP, 2024 | https://github.com/MAGIC-AI4Med/RaTEScore | Entity-aware metric; robust to synonyms & negation |

> Note: Dedicated error-detection tools are emerging but primarily use general-purpose LLMs (Llama-3, GPT-4). The European Radiology 2025 study (Langenbach et al.) showed Llama-3-70b is competitive with GPT-4, but no standalone open-source error-detection tool with paper+code was found specifically for this task.

---

### TXT-T8 去标识化 (De-identification / Anonymization)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| **NLP-vs-LLM Anonymization** | Langenbach et al., "Automated anonymization of radiology reports: comparison of NLP and LLMs," European Radiology, 2024 | https://github.com/ibro45/NLP-vs-LLM-Medical-Report-Anonymization | Compared spaCy NLP vs Llama-2 on 400 CT reports |
| **Microsoft Presidio** | Microsoft (general PII detection framework) | https://github.com/microsoft/presidio | Modular; supports NLP + pattern matching + custom pipelines |

---

### TXT-T10 否定/不确定性检测 (Negation / Uncertainty Detection)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| **NegBio** | Peng et al., AMIA, 2018 | https://github.com/ncbi-nlp/NegBio | High-performance; basis for CheXpert labeler |
| **CheXpert Labeler** | Irvin et al., AAAI, 2019 | https://github.com/stanfordmlgroup/chexpert-labeler | Handles positive/negative/uncertain labels |

---

## Multimodal Tasks (MM-T)

### MM-T4 多模态分类 (Multimodal Classification -- Image + Text)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| **CT-CLIP** | Hamamci et al., "Developing Generalist Foundation Models from a Multimodal Dataset for 3D CT," Nature Biomedical Engineering, 2025 | https://github.com/ibrahimethemhamamci/CT-CLIP | Zero-shot multi-abnormality detection; outperforms supervised SOTA |

---

### MM-T7 多模态报告生成 (Multimodal Report Generation)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| **CT2Rep** | Hamamci et al., MICCAI, 2024 | https://github.com/ibrahimethemhamamci/CT2Rep | First 3D CT-to-report model; cross-attention + hierarchical memory |
| **CT-CHAT** | Hamamci et al., Nature Biomedical Engineering, 2025 | https://github.com/ibrahimethemhamamci/CT-CHAT | VQA + report generation; LLaVA-adapted for 3D CT |
| **M3D-LaMed** | Bai et al., arXiv 2404.00578, 2024 | https://github.com/BAAI-DCAI/M3D | 8-task generalist; 120K 3D image-text pairs |

---

### MM-T8 多模态VQA (Multimodal Visual Question Answering)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| **CT-CHAT** | Hamamci et al., Nature Biomedical Engineering, 2025 | https://github.com/ibrahimethemhamamci/CT-CHAT | 3D chest CT VQA; LLaVA + CT-ViT encoder |
| **M3D-LaMed** | Bai et al., arXiv 2404.00578, 2024 | https://github.com/BAAI-DCAI/M3D | Supports VQA on 3D medical images; M3D-Bench |
| **PMC-VQA** | Zhang et al., "PMC-VQA: Visual Instruction Tuning for Medical VQA," arXiv, 2023 | https://github.com/xiaoman-zhang/PMC-VQA | 227K VQA pairs; multi-modality including CT |

---

### MM-T9 多模态检索 (Multimodal Retrieval)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| **CT-CLIP** | Hamamci et al., Nature Biomedical Engineering, 2025 | https://github.com/ibrahimethemhamamci/CT-CLIP | Supports image-to-text & text-to-image retrieval on 3D chest CT |

---

### MM-T10 图文一致性 (Image-Text Consistency / Cross-modal Verification)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| **RaTEScore** | Zhao et al., EMNLP, 2024 | https://github.com/MAGIC-AI4Med/RaTEScore | Entity-aware; sensitive to negation; aligns with human preference |
| **RadGraph** | Jain et al., ACL Findings, 2024 | https://github.com/Stanford-AIMI/radgraph | Entity+relation extraction enables structured comparison |

---

### MM-T12 多模态关键发现 (Multimodal Critical Finding Detection)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| **CT-CLIP** | Hamamci et al., Nature Biomedical Engineering, 2025 | https://github.com/ibrahimethemhamamci/CT-CLIP | Zero-shot abnormality detection across 3D CT volumes |
| **CheXbert** (text side) | Smit et al., EMNLP, 2020 | https://github.com/stanfordmlgroup/CheXbert | Labels critical findings (PE, pneumothorax, etc.) from text |

---

## Summary of Tasks Without Qualified Tools

The following tasks have **no open-source tool that satisfies both criteria** (published paper + working GitHub repo) specifically for lung CT:

- **IMG-T7 对比随访**: Only volumetry tools (ACM-LSTK) partially cover this; no dedicated DL-based nodule tracking/matching tool with paper+code exists. (**Partial coverage listed above**)
- **Pneumothorax on CT** (part of IMG-T12): EFA-Net paper exists (Sci Rep 2023) but no public code repository.