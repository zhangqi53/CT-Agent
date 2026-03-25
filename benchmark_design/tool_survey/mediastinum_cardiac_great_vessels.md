# Tool Survey: 纵隔/心脏大血管 (Mediastinum / Cardiac / Great Vessels)

> Body region scope: heart chambers, coronary arteries, thoracic aorta, pulmonary arteries, pericardium, mediastinal lymph nodes, mediastinal masses.
>
> Date: 2026-03-25

---

## IMG-T1 异常筛查 (Abnormality Screening)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| CT-CLIP | Hamamci et al., arXiv 2024 (CT-RATE/CT-CLIP) | https://github.com/ibrahimethemhamamci/CT-CLIP | Zero-shot multi-abnormality detection on chest CT (18 pathologies incl. coronary calcification); outperforms fully supervised baselines |
| CT-CHAT | Hamamci et al., 2024 (extension of CT-CLIP) | https://github.com/ibrahimethemhamamci/CT-CLIP | Vision-language chat model for 3D chest CT; can flag cardiac/mediastinal abnormalities via text queries |

> Note: No dedicated cardiac-only anomaly screening tool exists with paper+GitHub. CT-CLIP covers chest CT including cardiac findings and is the closest open-source solution.

---

## IMG-T2 病灶检测 (Lesion Detection -- Calcium / Coronary Lesions)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| DeepCAC | Zeleznik et al., **Nature Communications** 2021 | https://github.com/AIM-Harvard/DeepCAC | Automated CAC detection on gated & non-gated CT; HR up to 4.3 for CV events across 20,084 individuals (Framingham, NLST, PROMISE, ROMICAT-II) |
| Lessmann CalciumScoring | Lessmann et al., **IEEE TMI** 2018 | https://github.com/qurAI-amsterdam/calcium-scoring | Automatic coronary/aortic/valve calcium detection in low-dose chest CT; trained on 1,744 NLST scans |
| SEGMENT-CACS | Follmer et al., **Insights into Imaging** 2024 | https://github.com/Berni1557/SEGMENT-CACS | Segment-level CAC scoring; weighted Cohen kappa 0.808 on 455-patient test set from 26-center DISCHARGE trial |
| DeepLesion (universal) | Yan et al., **J Med Imaging** 2018 | https://github.com/rsummers11/CADLab | Universal lesion detection (32,735 lesions); covers mediastinal lesions |
| MULAN | Yan et al., **MICCAI** 2019 | https://github.com/ke-yan/MULAN | Multi-organ lesion detection + tagging; includes mediastinal/cardiac region |

---

## IMG-T3 病灶分割 (Lesion Segmentation)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| ULS23 + nnU-Net | ULS23 Challenge, **MedIA** 2025; Isensee et al., **Nature Methods** 2021 | https://github.com/DIAGNijmegen/ULS23 / https://github.com/MIC-DKFZ/nnUNet | Universal lesion segmentation; nnU-Net is SOTA across 23+ segmentation benchmarks |
| PlaqueDetection | Huang et al. (snake-constrained WHD loss) | https://github.com/kkhuang1990/PlaqueDetection | Coronary plaque boundary + segmentation; U-Net/Res-UNet/Tiramisu/DeepLab v2 (2D & 3D); evaluated via Dice, AVD, HD95, ASD |
| MedSAM | Ma et al., **Nature Communications** 2024 | https://github.com/bowang-lab/MedSAM | Interactive prompt-based 3D segmentation; applicable to cardiac/vascular structures |

---

## IMG-T4 分类 (Classification)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| CT-CLIP | Hamamci et al., arXiv 2024 | https://github.com/ibrahimethemhamamci/CT-CLIP | Zero-shot & fine-tuned classification of 18 chest CT pathologies incl. cardiomegaly, coronary calcification |
| RadFM | Wu et al., **Nature Communications** 2025 | https://github.com/chaoyi-wu/RadFM | Generalist radiology foundation model; supports 2D+3D CT classification, VQA; outperforms GPT-4V |

> Note: No dedicated cardiac-specific CT classifier with paper+GitHub found. The above generalist models cover cardiac pathologies.

---

## IMG-T5 测量/定量 (Measurement / Quantification -- Calcium Score / Cardiac Volume)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| DeepCAC | Zeleznik et al., **Nature Communications** 2021 | https://github.com/AIM-Harvard/DeepCAC | Agatston-equivalent calcium scoring; R=0.92-0.97 vs. manual across 4 cohorts |
| Lessmann CalciumScoring | Lessmann et al., **IEEE TMI** 2018 | https://github.com/qurAI-amsterdam/calcium-scoring | Agatston score computation; Cohen kappa 0.85 for risk category agreement |
| SEGMENT-CACS | Follmer et al., **Insights into Imaging** 2024 | https://github.com/Berni1557/SEGMENT-CACS | Segment-level Agatston scores per coronary artery branch |
| TotalSegmentator | Wasserthal et al., **Radiology:AI** 2023 | https://github.com/wasserth/TotalSegmentator | Cardiac chamber volumes via segmentation (4 chambers + great vessels); Dice 0.87-0.94 |
| VMTK | Izzo et al., **JOSS** 2018; Antiga et al., IEEE TMI 2004 | https://github.com/vmtk/vmtk | Aortic diameter, centerline, cross-sectional area measurement; 400+ citations |
| pyradiomics | van Griethuysen et al., **Cancer Research** 2017 | https://github.com/AIM-Harvard/pyradiomics | Radiomics feature extraction (shape, volume, HU statistics) for any segmented ROI |

---

## IMG-T6 解剖结构分割 (Anatomy Segmentation -- Chambers / Vessels)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| TotalSegmentator | Wasserthal et al., **Radiology:AI** 2023 | https://github.com/wasserth/TotalSegmentator | 117 structures incl. 4 cardiac chambers, aorta, pulmonary artery; Dice 0.87-0.94 for cardiac |
| MONAI VISTA3D | MONAI Consortium, **CVPR** 2025 | https://github.com/Project-MONAI/VISTA | 127-class CT segmentation foundation model; includes cardiac/vascular structures |
| PlatiPy (cardiac substructures) | Finnegan et al., **Phys Eng Sci Med** 2023 | https://github.com/pyplati/platipy | 18 cardiac substructures (chambers, great vessels, valves, coronary ostia); DSC 0.81-0.93 for chambers |
| ImageCAS | Zeng et al., **Comput Med Imaging Graph** 2023 | https://github.com/XiaoweiXu/ImageCAS-A-Large-Scale-Dataset-and-Benchmark-for-Coronary-Artery-Segmentation | Coronary artery tree segmentation from CTA; 1,000-case dataset + benchmark |
| CNNTracker (coronary centerline) | Wolterink et al., **Medical Image Analysis** 2019 | https://github.com/iolag/CNNTracker | Coronary centerline extraction; 93.7% overlap with reference, 0.21 mm mean error |

---

## IMG-T7 对比随访 (Longitudinal Comparison / Follow-up)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| ANTsPy | Avants et al., **NeuroImage** 2011 | https://github.com/ANTsX/ANTsPy | SyN deformable registration; gold-standard for longitudinal CT alignment; 10,000+ citations |
| VoxelMorph | Balakrishnan et al., **IEEE TMI** 2019 | https://github.com/voxelmorph/voxelmorph | Learning-based deformable registration; temporal consistency variant for longitudinal cardiac studies |

> Note: No dedicated cardiac CT follow-up comparison tool exists with paper+GitHub. Registration tools above must be combined with cardiac segmentation + measurement tools (TotalSegmentator + pyradiomics) for a complete pipeline.

---

## IMG-T8 报告生成 (Report Generation)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| CT2Rep | Hamamci et al., **MICCAI** 2024 | https://github.com/ibrahimethemhamamci/CT2Rep | First automated 3D chest CT report generation; trained on 25,692 CT-RATE volumes; supports longitudinal reports (CT2RepLong) |
| RadFM | Wu et al., **Nature Communications** 2025 | https://github.com/chaoyi-wu/RadFM | Generalist 2D+3D radiology report generation; supports CT including cardiac findings |

---

## IMG-T9 分期/分级 (Staging / Grading -- Coronary Stenosis Grading)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| DL-Coronary-Stenosis | Vibha et al., **Open Heart / BMJ** 2025 | https://github.com/Vibha190685/DL-for-Detection-of-Coronary-Artery-Stenosis | Stenosis detection (>=50% / >=70%) on CCTA using EfficientNet/ResNet/DenseNet; AUC > 0.94 |

> Note: Commercial systems (e.g., Cleerly, HeartFlow) dominate this space but are not open-source.

---

## IMG-T11 扫描质量 (Scan Quality Assessment)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| MONAI DataAnalyzer | Cardoso et al., **arXiv** 2022 | https://github.com/Project-MONAI/MONAI | Artifact detection, noise estimation, slice thickness analysis; rule-based + DL-based quality checks |

> Note: No dedicated cardiac CT quality assessment tool with paper+GitHub. MONAI provides general CT quality utilities. Motion artifact recognition for coronary CTA has been published (e.g., CoMoFACT) but without open-source code release.

---

## IMG-T12 关键发现 (Critical Findings -- Aortic Dissection / PE)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| aortic_dissection_det | Brainma et al., **Diagnostics** 2024 | https://github.com/brainma/aortic_dissection_det_pytorch | Stanford A/B dissection detection on CTA; Sens 0.969/0.946, Spec 0.982/0.996 |
| PENet | Huang et al., **npj Digital Medicine** 2020 | https://github.com/marshuang80/PENet | Pulmonary embolism detection on CTPA; AUROC 0.84 (internal), 0.85 (external) |
| RSNA PE 2nd-place | Pan et al., **Radiology:AI** 2021 | https://github.com/i-pan/kaggle-rsna-pe | PE detection + subtype classification; top-2 on 9,000+ CTPA competition |

---

## TXT-T1 临床文本异常信号提取 (Clinical Text Abnormality Signal Extraction)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| medspaCy | Eyre et al., **AMIA** 2021 | https://github.com/medspacy/medspacy | Clinical NLP pipeline with negation/uncertainty detection via ConText; applicable to cardiac CT reports |
| NegBio | Peng et al., **AMIA** 2018 | https://github.com/ncbi-nlp/NegBio | Negation + uncertainty detection in radiology reports; 9.5% precision improvement over NegEx |

---

## TXT-T2 报告实体抽取 (Report NER / Entity Extraction)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| RadGraph / RadGraph-XL | Jain et al., **ACL** 2024 (XL); Jain et al., NeurIPS 2021 (original) | https://github.com/Stanford-AIMI/radgraph | 410K+ entities/relations across 2,300 reports; covers chest CT; outperforms GPT-4 by up to 52% |

---

## TXT-T4 测量数值抽取 (Measurement Value Extraction from Reports)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| llm_extractinator | Builtjes et al., **JAMIA Open** 2025 | https://github.com/DIAGNijmegen/llm_extractinator | LLM-based extraction from radiology reports; 93.7% accuracy for target lesion attributes; supports Dutch + English |

---

## TXT-T5 时序报告对齐 (Temporal Report Alignment)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| llm_extractinator (longitudinal) | van Driel et al., **arXiv** 2025 ("Tracking Cancer Through Text") | https://github.com/DIAGNijmegen/llm_extractinator | Longitudinal lesion extraction from report pairs; 93.7% target, 94.9% non-target, 94.0% new lesion accuracy |

---

## TXT-T7 文本分类/标签 (Text Classification / Label Extraction)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| NegBio | Peng et al., **AMIA** 2018 | https://github.com/ncbi-nlp/NegBio | Assertion classification (positive/negative/uncertain) for radiology findings; used by CheXpert labeler |

---

## TXT-T8 报告生成 (Report Generation -- Text-only / NLP)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| CT2Rep | Hamamci et al., **MICCAI** 2024 | https://github.com/ibrahimethemhamamci/CT2Rep | 3D chest CT auto-report generation; cross-modal (image-conditioned text) |
| RadFM | Wu et al., **Nature Communications** 2025 | https://github.com/chaoyi-wu/RadFM | Supports report generation for 2D+3D medical images including CT |

---

## TXT-T10 知识检索 (Medical Knowledge Lookup)

> ---- 无开源工具 (No open-source tool with paper+GitHub specifically for cardiac CT knowledge retrieval. Typically addressed via RAG pipelines with general medical LLMs or guideline databases.)

---

## MM-T4 多模态分类 (Multimodal Classification)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| CT-CLIP | Hamamci et al., arXiv 2024 | https://github.com/ibrahimethemhamamci/CT-CLIP | Contrastive image-text pretraining on 25,692 CT volumes; zero-shot + fine-tuned classification of cardiac/chest pathologies |
| RadFM | Wu et al., **Nature Communications** 2025 | https://github.com/chaoyi-wu/RadFM | Multimodal 2D+3D foundation model; supports classification, VQA, diagnosis |

---

## MM-T7 多模态对比随访 (Multimodal Longitudinal Follow-up)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| CT2RepLong | Hamamci et al., **MICCAI** 2024 | https://github.com/ibrahimethemhamamci/CT2Rep | Longitudinal multimodal fusion (prior CT + prior report) for temporal-aware report generation |
| llm_extractinator | van Driel et al., arXiv 2025 | https://github.com/DIAGNijmegen/llm_extractinator | Longitudinal lesion tracking from serial report pairs |

> Note: No dedicated end-to-end multimodal cardiac follow-up tool. Above components can be combined with ANTsPy registration + TotalSegmentator segmentation.

---

## MM-T8 多模态报告生成 (Multimodal Report Generation)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| CT2Rep | Hamamci et al., **MICCAI** 2024 | https://github.com/ibrahimethemhamamci/CT2Rep | Image-to-text report generation from 3D chest CT volumes |
| RadFM | Wu et al., **Nature Communications** 2025 | https://github.com/chaoyi-wu/RadFM | Multimodal report generation supporting 2D+3D medical images |

---

## MM-T9 多模态分期/分级 (Multimodal Staging / Grading)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| DL-Coronary-Stenosis | Vibha et al., **Open Heart / BMJ** 2025 | https://github.com/Vibha190685/DL-for-Detection-of-Coronary-Artery-Stenosis | Image-based stenosis grading; AUC > 0.94 |

> Note: True multimodal (image + text) coronary grading tools with paper+GitHub do not exist. Practical pipelines combine image-based stenosis grading with text-based clinical context via LLMs.

---

## MM-T10 多模态鉴别诊断 (Multimodal Differential Diagnosis)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| RadFM | Wu et al., **Nature Communications** 2025 | https://github.com/chaoyi-wu/RadFM | Differential diagnosis with supporting evidence; processes 3D CT + text prompts; outperforms GPT-4V |

---

## MM-T12 多模态关键发现 (Multimodal Critical Findings)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| CT-CLIP | Hamamci et al., arXiv 2024 | https://github.com/ibrahimethemhamamci/CT-CLIP | Zero-shot detection of critical chest findings including coronary calcification, cardiomegaly |
| aortic_dissection_det + PENet | (see IMG-T12 above) | (see IMG-T12 above) | Specialized detectors for aortic dissection and PE; can be wrapped with text output for critical alerting |

---

## Summary: Gap Analysis

| Task | Status | Notes |
|------|--------|-------|
| IMG-T1 异常筛查 | Covered (CT-CLIP) | Generalist; no cardiac-specific screener |
| IMG-T2 病灶检测 | **Well covered** | DeepCAC, Lessmann, SEGMENT-CACS for calcium; DeepLesion/MULAN for universal |
| IMG-T3 病灶分割 | Covered | nnU-Net/ULS23 (universal); PlaqueDetection (coronary plaque) |
| IMG-T4 分类 | Covered (CT-CLIP, RadFM) | Generalist models; no cardiac-specific classifier |
| IMG-T5 测量/定量 | **Well covered** | Multiple calcium scoring tools + TotalSegmentator volumes + VMTK aortic metrics |
| IMG-T6 解剖结构 | **Well covered** | TotalSegmentator, PlatiPy, ImageCAS, VISTA3D, CNNTracker |
| IMG-T7 对比随访 | Gap -- indirect only | ANTsPy/VoxelMorph registration + segmentation pipeline assembly required |
| IMG-T8 报告生成 | Covered | CT2Rep (chest CT); RadFM (generalist) |
| IMG-T9 分期/分级 | Covered (1 tool) | DL-Coronary-Stenosis; no CAD-RADS or Agatston risk-category grading tool |
| IMG-T11 扫描质量 | Gap -- indirect only | MONAI provides general utilities; no cardiac-CT-specific quality tool |
| IMG-T12 关键发现 | **Well covered** | Aortic dissection detector + PENet for PE |
| TXT-T1 | Covered | medspaCy, NegBio |
| TXT-T2 | Covered | RadGraph-XL |
| TXT-T4 | Covered | llm_extractinator |
| TXT-T5 | Covered | llm_extractinator (longitudinal) |
| TXT-T7 | Covered | NegBio |
| TXT-T8 | Covered | CT2Rep, RadFM |
| TXT-T10 | Gap | No open-source cardiac knowledge base tool |
| MM-T4 | Covered | CT-CLIP, RadFM |
| MM-T7 | Partial | CT2RepLong + llm_extractinator; no end-to-end tool |
| MM-T8 | Covered | CT2Rep, RadFM |
| MM-T9 | Partial (1 tool) | Only image-based stenosis grading; no true multimodal grading |
| MM-T10 | Covered | RadFM |
| MM-T12 | Covered | CT-CLIP + specialized detectors |
