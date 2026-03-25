# Tool Survey: Brain/Intracranial CT (脑/颅内)

> Auto-generated tool survey for CT-Agent benchmark design.
> Inclusion criteria: published paper (with venue+year) AND working GitHub repository.

---

## IMG-T1 异常筛查 (Binary Normal vs Abnormal Classification)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| RSNA-ICH 1st Place | Wang et al., NeuroImage: Clinical, 2021 | https://github.com/SeuTao/RSNA2019_Intracranial-Hemorrhage-Detection | AUC 0.988 (ICH detection) |
| Chilamkurthy et al. (Qure.ai) | Chilamkurthy et al., The Lancet, 2018 | Dataset only (CQ500): https://headctstudy.qure.ai/dataset; Related code: https://github.com/anoubhav/AI-for-head-trauma | AUC 0.94 (ICH on CQ500) |

> Note: Chilamkurthy/Qure.ai released the CQ500 dataset and paper but their training code is proprietary. The CQ500 dataset and third-party reimplementations exist.

---

## IMG-T2 病灶检测 (Lesion Detection with 3D Bounding Boxes)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| MedYOLO | Sobek et al., JIIM, 2024 | https://github.com/JDSobek/MedYOLO | 3D YOLO for medical images; validated on CT |
| DeepLesion 3D Test Set | Yan et al., IEEE TMI, 2020 | https://github.com/viggin/DeepLesion_manual_test_set | 5,447 3D lesion boxes in 1000 CT sub-volumes |

> Note: MedYOLO is a generic 3D detector; not brain-CT-specific but applicable.

---

## IMG-T3 病灶分割 (Lesion Segmentation, Voxel-Level)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| BLAST-CT | Monteiro et al., Lancet Digital Health, 2020 | https://github.com/biomedia-mira/blast-ct | Multi-class TBI segmentation; multicentre validation (839 scans) |
| DeepMedic | Kamnitsas et al., Medical Image Analysis, 2017 | https://github.com/deepmedic/deepmedic | Brain lesion segmentation; BraTS top performer |
| nnU-Net | Isensee et al., Nature Methods, 2021 | https://github.com/MIC-DKFZ/nnUNet | DSC 0.88 (ICH), 0.80 (IVH) on brain CT (external validation) |
| BHSD (benchmark + models) | Wu et al., MLMI (MICCAI Workshop), 2023 | https://github.com/White65534/BHSD | 192 volumes, 5-class ICH; nnU-Net/TransBTS baselines |
| TBI CT Lesion Seg | Remedios et al., Medical Physics, 2020 | https://github.com/MASILab/tbi_ct_lesion_segmentation | Multi-site hemorrhage segmentation |

---

## IMG-T4 分类/良恶性 (Lesion Classification / Subtype)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| RSNA-ICH 1st Place | Wang et al., NeuroImage: Clinical, 2021 | https://github.com/SeuTao/RSNA2019_Intracranial-Hemorrhage-Detection | AUC: EDH 0.984, IPH 0.992, IVH 0.996, SAH 0.985, SDH 0.983 |
| CNN+LSTM ICH Subtyping | Burduja et al., Sensors, 2020 | https://github.com/warchildmd/ihd | Weighted log loss 0.04989 (top 2% RSNA) |

---

## IMG-T5 测量/定量 (Lesion Measurement: Diameter, Volume, HU)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| BLAST-CT | Monteiro et al., Lancet Digital Health, 2020 | https://github.com/biomedia-mira/blast-ct | Outputs per-class lesion volume (CSV); validated on TBI |
| CTseg | Brudfors et al., MICCAI, 2020 | https://github.com/WCHN/CTseg | Computes TBV and ICV from brain CT |

> Note: Dedicated diameter/HU measurement tools for brain CT with paper+code were not found. Volume is typically derived from segmentation masks (BLAST-CT, nnU-Net).

---

## IMG-T6 解剖结构 (Anatomy Segmentation)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| TotalSegmentator (brain_structures subtask) | Wasserthal et al., Radiology: AI, 2023 | https://github.com/wasserth/TotalSegmentator | 16 brain structures on CT (ventricle, cerebellum, lobes, etc.); Dice ~0.94 (overall) |
| CTseg | Brudfors et al., MICCAI, 2020 | https://github.com/WCHN/CTseg | GM/WM/CSF segmentation, skull-stripping, TBV/ICV |
| SynthSeg | Billot et al., Medical Image Analysis, 2023 | https://github.com/BBillot/SynthSeg | CT-validated (--ct flag); median Dice 0.76 on CT (vs MRI ground truth) |
| DiffusionSynCTSeg | (HealthX-Lab), MICCAI, 2024 | https://github.com/HealthX-Lab/DiffusionSynCTSeg | CT ventricle segmentation via diffusion bridge |

---

## IMG-T7 对比随访 (Longitudinal Comparison)

> No open-source tool was found with both a published paper and GitHub code specifically for longitudinal brain CT comparison.

> Closest related works: SimU-Net (longitudinal brain metastases on MRI, Springer 2024) -- no public code confirmed for brain CT.

❌ 无开源工具 (brain CT specific)

---

## IMG-T8 报告生成 (Report Generation from CT)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| BrainGPT / FORTE | Wei et al., Nature Communications, 2025 | https://github.com/charlierabea/FORTE | FORTE F1 0.71; brain CT specific; 18,885 scan-text pairs |
| MEPNet | Zhang et al., AAAI, 2025 (oral) | https://github.com/YanzhaoShi/MEPNet | Brain CT report generation; LLaMA 3 backbone |
| CT2Rep | Hamamci et al., MICCAI, 2024 | https://github.com/ibrahimethemhamamci/CT2Rep | First 3D CT report generation (chest CT; architecture applicable) |

---

## IMG-T9 分期/分级 (Staging/Grading, e.g., ASPECTS)

> No dedicated open-source tool was found with both a published paper and working GitHub code for automated ASPECTS scoring on brain CT.

> Research exists (e.g., DLAD for ASPECTS in JCM 2022; automated ASPECTS on NITRC) but no confirmed paper+GitHub combination.

❌ 无开源工具

---

## IMG-T11 扫描质量 (Scan Quality Assessment)

> No open-source tool was found with both a published paper and GitHub code specifically for brain CT quality assessment.

> BrainQCNet (https://github.com/garciaml/BrainQCNet, Imaging Neuroscience 2025) exists for MRI QC. CT-specific QC tools with paper+code were not identified.

❌ 无开源工具 (brain CT specific)

---

## IMG-T12 关键发现 (Critical/Urgent Finding Detection)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| Midline Shift Detection | Pisov et al., UNSURE (MICCAI Workshop), 2019 | https://github.com/neuro-ml/midline-shift-detection | MLS detection; error approaches inter-expert variability |
| CAR-Net (Brain Midline) | Wang et al., MICCAI, 2020 | https://github.com/ShawnBIT/Brain-Midline-Detection | Midline delineation on brain CT; connectivity-regularized |
| RSNA-ICH 1st Place | Wang et al., NeuroImage: Clinical, 2021 | https://github.com/SeuTao/RSNA2019_Intracranial-Hemorrhage-Detection | ICH + subtype detection (critical finding); AUC 0.988 |

---

## TXT-T1 异常信号 (Clinical Text Signal Extraction)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| NegBio | Peng et al., AMIA Informatics Summit, 2018 | https://github.com/ncbi-nlp/NegBio | Negation/uncertainty detection in radiology reports; +5.1% F1 over NegEx |
| CheXbert | Smit et al., EMNLP, 2020 | https://github.com/stanfordmlgroup/CheXbert | BERT-based report labeler; 14 observations; F1 improvement 0.055 over CheXpert labeler |

---

## TXT-T2 病灶抽取 (Report NER / Lesion Entity Extraction)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| John Snow Labs ner_radiology | (Spark NLP, commercial+open models) | https://github.com/JohnSnowLabs/spark-nlp-workshop | Radiology NER: ImagingFindings, BodyPart, Measurements, etc. |

> Note: ner_radiology requires Spark NLP Healthcare license for full functionality. Open-source alternatives with published papers specifically for brain CT report NER are limited.

> Partially applicable: CheXpert labeler (rule-based NER for chest findings).

---

## TXT-T4 分类标签 (Classification Label Extraction from Text)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| CheXpert Labeler | Irvin et al., AAAI, 2019 | https://github.com/stanfordmlgroup/chexpert-labeler | Rule-based; 14 chest observations; basis for 224K label dataset |
| CheXbert | Smit et al., EMNLP, 2020 | https://github.com/stanfordmlgroup/CheXbert | BERT-based; outperforms CheXpert labeler by F1 +0.055 |
| NegBio | Peng et al., AMIA, 2018 | https://github.com/ncbi-nlp/NegBio | Negation/uncertainty classification for radiology findings |

> Note: These tools are chest-radiology oriented. For brain CT, the architecture is transferable but no brain-CT-specific text labeler with paper+code was found.

---

## TXT-T5 测量抽取 (Measurement Extraction from Text)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| MARVE | Hundman & Mattmann, KDD, 2017 | https://github.com/khundman/marve | CRF-based measurement + unit + context extraction from text |

> Note: MARVE was designed for Earth science but the extraction pipeline is domain-agnostic (values, units, related entities). No radiology-specific measurement extraction tool with paper+code was found.

---

## TXT-T7 随访对比 (Temporal Report Comparison)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| THYME | Styler et al., AMIA/SemEval shared tasks, 2014-2016 | https://github.com/stylerw/thymedata | Temporal relation annotation corpus; brain cancer + colon cancer notes |

> Note: THYME provides annotated data and schema for temporal NLP but is not a ready-to-use tool. No dedicated brain CT temporal report comparison tool with paper+code was found.

---

## TXT-T8 报告生成 (Report Generation from Text / Impression from Findings)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| Summarize Radiology Findings | Zhang et al., EMNLP Workshop, 2018 | https://github.com/yuhaozhang/summarize-radiology-findings | Findings-to-impression; pretrained on 87K Stanford reports |
| R2Gen | Chen et al., EMNLP, 2020 | https://github.com/cuhksz-nlp/R2Gen | Memory-driven Transformer for report generation |

---

## TXT-T10 鉴别诊断 (Differential Diagnosis from Text)

❌ 无开源工具

> No open-source tool with paper+code specifically for text-based differential diagnosis of brain CT findings was identified.

---

## MM-T4 分类 (Multimodal Classification: Image + Text)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| BiomedCLIP | Zhang et al., NEJM AI, 2024 | https://github.com/microsoft/BiomedCLIP_data_pipeline | Multimodal (15M image-text pairs); zero-shot classification; outperforms PubMedCLIP |
| CT-CLIP | Hamamci et al., Nature Biomedical Engineering, 2026 | https://github.com/ibrahimethemhamamci/CT-CLIP | 3D CT + report contrastive learning; zero-shot multi-abnormality detection |
| MedCLIP | Wang et al., EMNLP, 2022 | https://github.com/RyanWangZf/MedCLIP | Unpaired image-text contrastive learning; outperforms CLIP on medical tasks |

> Note: These are general medical multimodal models, not brain-CT specific. CT-CLIP is chest-CT focused. Brain CT multimodal classification tools are covered by BrainGPT/FORTE under MM-T8.

---

## MM-T7 随访 (Multimodal Longitudinal Analysis)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| Libra | Zhang et al., ACL (Findings), 2025 | https://github.com/X-iZhang/Libra | Temporal Alignment Connector; RadCliQ +12.9%; CXR focused |

> Note: Libra is designed for chest X-ray longitudinal analysis. No brain CT multimodal longitudinal tool with paper+code was found.

---

## MM-T8 报告生成 (Multimodal Report Generation)

| Tool | Paper | GitHub | Key Metric |
|------|-------|--------|------------|
| BrainGPT / FORTE | Wei et al., Nature Communications, 2025 | https://github.com/charlierabea/FORTE | 3D Brain CT + text; FORTE F1 0.71; 74% indistinguishable from human |
| MEPNet | Zhang et al., AAAI, 2025 (oral) | https://github.com/YanzhaoShi/MEPNet | Brain CT report generation; entity-balanced prompting + LLaMA 3 |
| CT2Rep | Hamamci et al., MICCAI, 2024 | https://github.com/ibrahimethemhamamci/CT2Rep | 3D chest CT report generation; cross-attention fusion |

---

## MM-T9 分期 (Multimodal Staging)

❌ 无开源工具

> No open-source tool combining brain CT images and text for staging (e.g., multimodal ASPECTS) with paper+code was identified.

---

## MM-T10 鉴别诊断 (Multimodal Differential Diagnosis)

❌ 无开源工具

> No open-source tool specifically for multimodal differential diagnosis on brain CT with paper+code was identified. Closest: RSNA-ICH model performs ICH subtype classification (image-only).

---

## MM-T12 关键发现 (Multimodal Critical Findings)

❌ 无开源工具

> No open-source multimodal (image+text) critical findings detection tool for brain CT with paper+code was identified. Image-only critical finding detection is covered under IMG-T12.

---

## Summary Table

| Task | # Tools Found | Best Brain-CT Tool |
|------|--------------|---------------------|
| IMG-T1 异常筛查 | 2 | RSNA-ICH 1st Place (AUC 0.988) |
| IMG-T2 病灶检测 | 2 | MedYOLO (generic 3D) |
| IMG-T3 病灶分割 | 5 | BLAST-CT (brain CT specific) |
| IMG-T4 分类/良恶性 | 2 | RSNA-ICH 1st Place (5 subtypes) |
| IMG-T5 测量/定量 | 2 | BLAST-CT (volume output) |
| IMG-T6 解剖结构 | 4 | TotalSegmentator (16 brain structures) |
| IMG-T7 对比随访 | 0 | -- |
| IMG-T8 报告生成 | 3 | BrainGPT/FORTE (brain CT specific) |
| IMG-T9 分期/分级 | 0 | -- |
| IMG-T11 扫描质量 | 0 | -- |
| IMG-T12 关键发现 | 3 | Midline Shift Detection + RSNA-ICH |
| TXT-T1 异常信号 | 2 | NegBio / CheXbert |
| TXT-T2 病灶抽取 | 1 | Spark NLP ner_radiology (partial) |
| TXT-T4 分类标签 | 3 | CheXpert Labeler / CheXbert |
| TXT-T5 测量抽取 | 1 | MARVE (generic) |
| TXT-T7 随访对比 | 1 | THYME (corpus only) |
| TXT-T8 报告生成 | 2 | Summarize Radiology Findings |
| TXT-T10 鉴别诊断 | 0 | -- |
| MM-T4 分类 | 3 | BiomedCLIP / CT-CLIP |
| MM-T7 随访 | 1 | Libra (CXR, not brain CT) |
| MM-T8 报告生成 | 3 | BrainGPT/FORTE (brain CT specific) |
| MM-T9 分期 | 0 | -- |
| MM-T10 鉴别诊断 | 0 | -- |
| MM-T12 关键发现 | 0 | -- |

### Key Gaps (No tools with paper+code)
- **IMG-T7**: Longitudinal brain CT comparison
- **IMG-T9**: ASPECTS / stroke grading automation
- **IMG-T11**: Brain CT scan quality assessment
- **TXT-T10**: Text-based differential diagnosis
- **MM-T9**: Multimodal staging
- **MM-T10**: Multimodal differential diagnosis
- **MM-T12**: Multimodal critical findings
