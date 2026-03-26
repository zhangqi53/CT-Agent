# CT Benchmark Tool Survey: Spine / Bone-Joint / Whole-body

> Date: 2025-03-25
>
> Scope: Three body regions with 24 task types each.
> Strict inclusion: **published paper + public GitHub repo** required.
>
> Task type key (inferred from benchmark architecture):
> - **IMG-T1** Anomaly screening | **IMG-T2** Lesion detection | **IMG-T3** Lesion segmentation | **IMG-T4** Anatomy segmentation | **IMG-T5** Quantitative measurement | **IMG-T6** Longitudinal change tracking | **IMG-T7** Classification/characterization | **IMG-T8** Report generation (image-only) | **IMG-T9** Staging/grading | **IMG-T11** Radiomics feature extraction | **IMG-T12** Incidental finding detection
> - **TXT-T1** NER extraction | **TXT-T2** Relation extraction | **TXT-T4** Measurement value extraction | **TXT-T5** Temporal report alignment | **TXT-T7** Classification label extraction | **TXT-T8** Report summarization/generation (text) | **TXT-T10** Negation/assertion detection
> - **MM-T4** Multimodal quantitative measurement | **MM-T7** Multimodal classification | **MM-T8** Multimodal report generation | **MM-T9** Multimodal staging/grading | **MM-T10** Multimodal differential diagnosis | **MM-T12** Multimodal incidental finding management

---

## 1. 脊柱 (Spine)

### IMG Tasks

| Task | Tool | Paper | GitHub | Key Metric |
|------|------|-------|--------|------------|
| **IMG-T1** Anomaly screening | CT-CLIP | Hamamci et al., *ECCV* 2024 | https://github.com/ibrahimethemhamamci/CT-CLIP | Zero-shot AUC ~0.70 on chest abnormalities; applicable to spine via text prompts |
| **IMG-T2** Lesion detection (vertebral fracture) | FracNet (adapted) | Jin et al., *EBioMedicine* 2020 | https://github.com/M3DV/FracNet | Detection sens 92.9% (rib; spine via transfer) |
| **IMG-T2** Lesion detection (vertebral fracture) | VerSe + Genant grading | Sekuboyina et al., *MedIA* 2021, 300+ cites | https://github.com/anjany/verse | Vertebra ID rate 96.4%; fracture via height-loss |
| **IMG-T3** Lesion segmentation | nnU-Net | Isensee et al., *Nature Methods* 2021, 7000+ cites | https://github.com/MIC-DKFZ/nnUNet | SOTA on 23+ medical segmentation benchmarks |
| **IMG-T3** Lesion segmentation | MedSAM | Ma et al., *Nature Communications* 2024, 300+ cites | https://github.com/bowang-lab/MedSAM | DSC 0.87 on universal 3D segmentation with prompts |
| **IMG-T4** Anatomy segmentation (vertebrae C1-L5) | VerSe | Sekuboyina et al., *MedIA* 2021 | https://github.com/anjany/verse | Vertebra seg DSC ~0.90 |
| **IMG-T4** Anatomy segmentation | TotalSegmentator | Wasserthal et al., *Radiology:AI* 2023, 600+ cites | https://github.com/wasserth/TotalSegmentator | 117 classes including all vertebrae, spinal canal; DSC 0.943 |
| **IMG-T4** Anatomy segmentation | VISTA3D | MONAI VISTA3D, *CVPR* 2025 | https://github.com/Project-MONAI/VISTA | 127-class CT segmentation foundation model |
| **IMG-T5** Quantitative measurement | pyradiomics | van Griethuysen et al., *Cancer Research* 2017, 3000+ cites | https://github.com/AIM-Harvard/pyradiomics | 1400+ features; shape/size/HU statistics |
| **IMG-T5** Quantitative measurement (bone density) | Comp2Comp | Koitka et al., *Radiology* 2021 / Stanford AIMI | https://github.com/StanfordMIMI/Comp2Comp | Vertebral HU → BMD estimation; muscle/fat at L3 |
| **IMG-T6** Longitudinal change tracking | ❌ 无开源工具 | — | — | No dedicated open-source spine longitudinal tracking tool with paper+code |
| **IMG-T7** Classification (fracture type/osteoporosis) | CT-CLIP | Hamamci et al., *ECCV* 2024 | https://github.com/ibrahimethemhamamci/CT-CLIP | Zero-shot classification via text prompt |
| **IMG-T8** Report generation | ❌ 无开源工具 | — | — | No spine-specific CT report generator with paper+code |
| **IMG-T9** Staging/grading (Genant fracture grading) | ❌ 无开源工具 | — | — | Indirect: VerSe segmentation + height-ratio rule, but no integrated grading tool |
| **IMG-T11** Radiomics feature extraction | pyradiomics | van Griethuysen et al., *Cancer Research* 2017 | https://github.com/AIM-Harvard/pyradiomics | 1400+ radiomic features; vertebral ROI input |
| **IMG-T11** Radiomics feature extraction | WORC | Martijn Starmans et al., *European Radiology* 2022, 100+ cites | https://github.com/MStarmans91/WORC | Automated radiomics pipeline with 20+ classifiers |
| **IMG-T12** Incidental finding detection | DeepLesion | Yan et al., *J Med Imaging* 2018, 400+ cites | https://github.com/rsummers11/CADLab | Universal lesion detection; 32K+ lesion annotations |

### TXT Tasks

| Task | Tool | Paper | GitHub | Key Metric |
|------|------|-------|--------|------------|
| **TXT-T1** NER extraction | RadGraph-XL | Jain et al., *ACL* 2024 (training set includes CT) | https://github.com/Stanford-AIMI/radgraph | F1 ~0.85 on radiology entity extraction |
| **TXT-T1** NER extraction | medspaCy | Eyre et al., *JAMIA* 2021 | https://github.com/medspacy/medspacy | Clinical NLP pipeline with sectionizer, context detection |
| **TXT-T2** Relation extraction | RadGraph-XL | Jain et al., *ACL* 2024 | https://github.com/Stanford-AIMI/radgraph | Entity-relation graph from radiology reports |
| **TXT-T4** Measurement extraction | llm_extractinator | van Driel et al., *arXiv* 2025 | https://github.com/DIAGNijmegen/llm_extractinator | 93.7% accuracy on measurement extraction |
| **TXT-T5** Temporal alignment | llm_extractinator | van Driel et al., *arXiv* 2025 ("Tracking Cancer Through Text") | https://github.com/DIAGNijmegen/llm_extractinator | Multi-timepoint report change extraction |
| **TXT-T7** Classification label extraction | NegBio | Peng et al., *EMNLP* 2018 | https://github.com/ncbi-nlp/NegBio | Diagnosis label + assertion extraction |
| **TXT-T8** Report summarization | ❌ 无开源工具 | — | — | No spine-specific text report generation with paper+code |
| **TXT-T10** Negation/assertion detection | medspaCy (ConText) | Eyre et al., *JAMIA* 2021 | https://github.com/medspacy/medspacy | Negation, hypothetical, historical assertion detection |
| **TXT-T10** Negation/assertion detection | NegBio | Peng et al., *EMNLP* 2018 | https://github.com/ncbi-nlp/NegBio | Rule-based negation detection for clinical text |

### MM (Multimodal) Tasks

| Task | Tool | Paper | GitHub | Key Metric |
|------|------|-------|--------|------------|
| **MM-T4** Multimodal measurement | ❌ 无开源工具 | — | — | Achievable by chaining pyradiomics + llm_extractinator, no integrated tool |
| **MM-T7** Multimodal classification | CT-CLIP | Hamamci et al., *ECCV* 2024 | https://github.com/ibrahimethemhamamci/CT-CLIP | Vision-language contrastive model for CT; zero-shot classification |
| **MM-T7** Multimodal classification | Merlin | Blankemeier et al., *ECCV* 2024 | https://github.com/StanfordMIMI/Merlin | 3D VL model, 6 CT tasks, top-5 AUC 0.91 |
| **MM-T8** Multimodal report generation | RadFM | Wu et al., *Nature Communications* 2025 | https://github.com/chaoyi-wu/RadFM | Supports 3D CT input; multi-modal report generation |
| **MM-T9** Multimodal staging/grading | ❌ 无开源工具 | — | — | No integrated multimodal spine staging tool |
| **MM-T10** Multimodal differential diagnosis | RadFM | Wu et al., *Nature Communications* 2025 | https://github.com/chaoyi-wu/RadFM | 3D medical VLM; differential diagnosis via prompting |
| **MM-T12** Multimodal incidental finding | ❌ 无开源工具 | — | — | Possible via DeepLesion + RadFM pipeline, but no integrated tool |

---

## 2. 骨骼/关节 (Bone/Joint)

### IMG Tasks

| Task | Tool | Paper | GitHub | Key Metric |
|------|------|-------|--------|------------|
| **IMG-T1** Anomaly screening | CT-CLIP | Hamamci et al., *ECCV* 2024 | https://github.com/ibrahimethemhamamci/CT-CLIP | Zero-shot abnormality screening via text prompts |
| **IMG-T2** Lesion detection (fracture) | FracNet | Jin et al., *EBioMedicine* 2020, 100+ cites | https://github.com/M3DV/FracNet | Rib fracture detection sens 92.9%, prec 75.0% |
| **IMG-T2** Lesion detection (pelvic fracture) | CTPelvic1K | Liu et al., *MICCAI* 2021 | https://github.com/ICT-MIRACLE-lab/CTPelvic1K | Pelvic bone seg DSC ~0.98; fracture detection pipeline |
| **IMG-T3** Lesion segmentation | nnU-Net | Isensee et al., *Nature Methods* 2021 | https://github.com/MIC-DKFZ/nnUNet | Self-configuring; SOTA on bone lesion segmentation tasks |
| **IMG-T3** Lesion segmentation | MedSAM | Ma et al., *Nature Communications* 2024 | https://github.com/bowang-lab/MedSAM | Prompt-based 3D segmentation, DSC 0.87 |
| **IMG-T4** Anatomy segmentation (bones) | TotalSegmentator | Wasserthal et al., *Radiology:AI* 2023 | https://github.com/wasserth/TotalSegmentator | 117 classes: ribs, pelvis, femur, humerus, scapula, etc.; DSC 0.943 |
| **IMG-T4** Anatomy segmentation (pelvis) | CTPelvic1K | Liu et al., *MICCAI* 2021 | https://github.com/ICT-MIRACLE-lab/CTPelvic1K | 4 pelvic bone classes, 1184 scans, DSC ~0.98 |
| **IMG-T4** Anatomy segmentation | VISTA3D | MONAI VISTA3D, *CVPR* 2025 | https://github.com/Project-MONAI/VISTA | 127-class foundation model including skeletal structures |
| **IMG-T5** Quantitative measurement | pyradiomics | van Griethuysen et al., *Cancer Research* 2017 | https://github.com/AIM-Harvard/pyradiomics | Shape/volume/HU from bone ROIs |
| **IMG-T6** Longitudinal change tracking | ❌ 无开源工具 | — | — | No dedicated bone longitudinal tracking tool with paper+code |
| **IMG-T7** Classification (fracture type) | RibFrac (classification head) | Jin et al., *Radiology:AI* 2021 & *MedIA* 2024 | https://github.com/M3DV/FracNet | 4-type fracture classification (buckle/non-displaced/displaced/segmental) |
| **IMG-T8** Report generation | ❌ 无开源工具 | — | — | No bone-specific CT report generator with paper+code |
| **IMG-T9** Staging/grading | ❌ 无开源工具 | — | — | No open-source fracture grading (AO/OTA) tool with paper+code |
| **IMG-T11** Radiomics feature extraction | pyradiomics | van Griethuysen et al., *Cancer Research* 2017 | https://github.com/AIM-Harvard/pyradiomics | 1400+ features from bone lesion masks |
| **IMG-T11** Radiomics feature extraction | WORC | Starmans et al., *European Radiology* 2022 | https://github.com/MStarmans91/WORC | End-to-end radiomics workflow; tested on bone tumors |
| **IMG-T12** Incidental finding detection | DeepLesion | Yan et al., *J Med Imaging* 2018 | https://github.com/rsummers11/CADLab | Universal lesion detection including bone lesions |

### TXT Tasks

| Task | Tool | Paper | GitHub | Key Metric |
|------|------|-------|--------|------------|
| **TXT-T1** NER extraction | RadGraph-XL | Jain et al., *ACL* 2024 | https://github.com/Stanford-AIMI/radgraph | Radiology entity extraction (location, morphology) |
| **TXT-T1** NER extraction | medspaCy | Eyre et al., *JAMIA* 2021 | https://github.com/medspacy/medspacy | Clinical NLP pipeline |
| **TXT-T2** Relation extraction | RadGraph-XL | Jain et al., *ACL* 2024 | https://github.com/Stanford-AIMI/radgraph | Entity-relation graph |
| **TXT-T4** Measurement extraction | llm_extractinator | van Driel et al., *arXiv* 2025 | https://github.com/DIAGNijmegen/llm_extractinator | 93.7% measurement extraction accuracy |
| **TXT-T5** Temporal alignment | llm_extractinator | van Driel et al., *arXiv* 2025 | https://github.com/DIAGNijmegen/llm_extractinator | Multi-timepoint change extraction |
| **TXT-T7** Classification label extraction | NegBio | Peng et al., *EMNLP* 2018 | https://github.com/ncbi-nlp/NegBio | Label + assertion extraction |
| **TXT-T8** Report summarization | ❌ 无开源工具 | — | — | No bone/joint-specific text report tool |
| **TXT-T10** Negation/assertion detection | medspaCy (ConText) | Eyre et al., *JAMIA* 2021 | https://github.com/medspacy/medspacy | Negation, assertion detection |
| **TXT-T10** Negation/assertion detection | NegBio | Peng et al., *EMNLP* 2018 | https://github.com/ncbi-nlp/NegBio | Rule-based negation |

### MM (Multimodal) Tasks

| Task | Tool | Paper | GitHub | Key Metric |
|------|------|-------|--------|------------|
| **MM-T4** Multimodal measurement | ❌ 无开源工具 | — | — | No integrated multimodal bone measurement tool |
| **MM-T7** Multimodal classification | CT-CLIP | Hamamci et al., *ECCV* 2024 | https://github.com/ibrahimethemhamamci/CT-CLIP | Zero-shot bone classification via VL matching |
| **MM-T7** Multimodal classification | Merlin | Blankemeier et al., *ECCV* 2024 | https://github.com/StanfordMIMI/Merlin | 3D VL model covering musculoskeletal findings |
| **MM-T8** Multimodal report generation | RadFM | Wu et al., *Nature Communications* 2025 | https://github.com/chaoyi-wu/RadFM | 3D CT multimodal report generation |
| **MM-T9** Multimodal staging/grading | ❌ 无开源工具 | — | — | No multimodal fracture staging tool |
| **MM-T10** Multimodal differential diagnosis | RadFM | Wu et al., *Nature Communications* 2025 | https://github.com/chaoyi-wu/RadFM | 3D medical VLM for differential diagnosis |
| **MM-T12** Multimodal incidental finding | ❌ 无开源工具 | — | — | No integrated tool; pipeline possible via DeepLesion + RadFM |

---

## 3. 全身/多部位 (Whole-body / Multi-region)

### IMG Tasks

| Task | Tool | Paper | GitHub | Key Metric |
|------|------|-------|--------|------------|
| **IMG-T1** Anomaly screening | CT-CLIP | Hamamci et al., *ECCV* 2024 | https://github.com/ibrahimethemhamamci/CT-CLIP | Zero-shot whole-body CT abnormality screening |
| **IMG-T2** Lesion detection (universal) | DeepLesion | Yan et al., *J Med Imaging* 2018, 400+ cites | https://github.com/rsummers11/CADLab | 32,735 lesion annotations across body; universal 3D bbox detection |
| **IMG-T2** Lesion detection (universal) | MULAN | Yan et al., *MICCAI* 2019, 150+ cites | https://github.com/rsummers11/CADLab | Multi-organ lesion detection + automatic tagging |
| **IMG-T3** Lesion segmentation (universal) | ULS23 | DIAG, *MedIA* 2025 | https://github.com/DIAGNijmegen/ULS23 | Universal lesion segmentation challenge; nnU-Net based |
| **IMG-T3** Lesion segmentation | nnU-Net | Isensee et al., *Nature Methods* 2021, 7000+ cites | https://github.com/MIC-DKFZ/nnUNet | Self-configuring; SOTA on 23+ benchmarks |
| **IMG-T3** Lesion segmentation | MedSAM | Ma et al., *Nature Communications* 2024 | https://github.com/bowang-lab/MedSAM | Prompt-based universal 3D segmentation, DSC 0.87 |
| **IMG-T4** Anatomy segmentation (117 classes) | TotalSegmentator | Wasserthal et al., *Radiology:AI* 2023, 600+ cites | https://github.com/wasserth/TotalSegmentator | 117 whole-body structures; DSC 0.943; 1228 training CTs |
| **IMG-T4** Anatomy segmentation (127 classes) | VISTA3D | MONAI VISTA3D, *CVPR* 2025 | https://github.com/Project-MONAI/VISTA | 127-class whole-body CT foundation model |
| **IMG-T5** Quantitative measurement | pyradiomics | van Griethuysen et al., *Cancer Research* 2017, 3000+ cites | https://github.com/AIM-Harvard/pyradiomics | 1400+ features; body-region agnostic |
| **IMG-T5** Quantitative measurement (body composition) | Comp2Comp | Koitka et al., *Radiology* 2021 / Stanford AIMI | https://github.com/StanfordMIMI/Comp2Comp | Muscle/fat/bone density at L3; body composition analysis |
| **IMG-T6** Longitudinal change tracking (RECIST) | detect-then-track | alibool, *JIMM* 2025 | https://github.com/alibool/detect-then-track | RECIST-based lesion tracking across timepoints |
| **IMG-T7** Classification/characterization | CT-CLIP | Hamamci et al., *ECCV* 2024 | https://github.com/ibrahimethemhamamci/CT-CLIP | Zero-shot multi-label classification |
| **IMG-T8** Report generation (chest CT) | CT2Rep | Hamamci et al., *MICCAI* 2024 | https://github.com/ibrahimethemhamamci/CT2Rep | 3D chest CT to structured report; 25,692 volumes |
| **IMG-T8** Report generation (abdomen CT) | RadGPT | Bassi et al., *ICCV* 2025 | https://github.com/MrGiovanni/RadGPT | AbdomenAtlas 9262 volumes; tumor-focused report |
| **IMG-T9** Staging/grading (TNM) | ❌ 无开源工具 | — | — | No universal imaging-only staging tool; TNM requires text (see TXT/MM) |
| **IMG-T11** Radiomics feature extraction | pyradiomics | van Griethuysen et al., *Cancer Research* 2017 | https://github.com/AIM-Harvard/pyradiomics | 1400+ features; universal application |
| **IMG-T11** Radiomics feature extraction | WORC | Starmans et al., *European Radiology* 2022 | https://github.com/MStarmans91/WORC | Full radiomics workflow: feature extraction + classification |
| **IMG-T12** Incidental finding detection | DeepLesion | Yan et al., *J Med Imaging* 2018 | https://github.com/rsummers11/CADLab | Universal lesion detection across 8 body regions |

### TXT Tasks

| Task | Tool | Paper | GitHub | Key Metric |
|------|------|-------|--------|------------|
| **TXT-T1** NER extraction | RadGraph-XL | Jain et al., *ACL* 2024 | https://github.com/Stanford-AIMI/radgraph | Entity extraction from any radiology report; F1 ~0.85 |
| **TXT-T1** NER extraction | medspaCy | Eyre et al., *JAMIA* 2021 | https://github.com/medspacy/medspacy | General clinical NLP pipeline |
| **TXT-T2** Relation extraction | RadGraph-XL | Jain et al., *ACL* 2024 | https://github.com/Stanford-AIMI/radgraph | Entity-relation graph; location-finding-attribute triples |
| **TXT-T4** Measurement extraction | llm_extractinator | van Driel et al., *arXiv* 2025 | https://github.com/DIAGNijmegen/llm_extractinator | 93.7% accuracy; RECIST measurements |
| **TXT-T5** Temporal alignment | llm_extractinator | van Driel et al., *arXiv* 2025 | https://github.com/DIAGNijmegen/llm_extractinator | Cross-timepoint report change tracking |
| **TXT-T7** Classification label extraction | NegBio | Peng et al., *EMNLP* 2018 | https://github.com/ncbi-nlp/NegBio | Universal diagnosis label extraction |
| **TXT-T8** Report summarization | ❌ 无开源工具 | — | — | No dedicated whole-body text report summarizer with paper+code |
| **TXT-T10** Negation/assertion detection | medspaCy (ConText) | Eyre et al., *JAMIA* 2021 | https://github.com/medspacy/medspacy | Negation, hypothetical, historical detection |
| **TXT-T10** Negation/assertion detection | NegBio | Peng et al., *EMNLP* 2018 | https://github.com/ncbi-nlp/NegBio | Rule-based negation for clinical text |

### MM (Multimodal) Tasks

| Task | Tool | Paper | GitHub | Key Metric |
|------|------|-------|--------|------------|
| **MM-T4** Multimodal measurement | ❌ 无开源工具 | — | — | Achievable via chaining (pyradiomics + llm_extractinator), no single tool |
| **MM-T7** Multimodal classification | CT-CLIP | Hamamci et al., *ECCV* 2024 | https://github.com/ibrahimethemhamamci/CT-CLIP | Vision-language contrastive model; zero-shot classification |
| **MM-T7** Multimodal classification | Merlin | Blankemeier et al., *ECCV* 2024 | https://github.com/StanfordMIMI/Merlin | 3D VL model, 752K image-text pairs, top-5 AUC 0.91 |
| **MM-T8** Multimodal report generation | RadFM | Wu et al., *Nature Communications* 2025 | https://github.com/chaoyi-wu/RadFM | 3D CT multimodal medical VLM; text+image report gen |
| **MM-T8** Multimodal report generation | CT2Rep | Hamamci et al., *MICCAI* 2024 | https://github.com/ibrahimethemhamamci/CT2Rep | 3D CT → report (chest); multimodal architecture |
| **MM-T9** Multimodal staging (TNM) | TNM Stage Classifier | Tatonetti Lab, *Nature Communications* (BBTEN, 23 cancer types) | https://github.com/tatonetti-lab/tnm-stage-classifier | NLP-based TNM extraction; needs pairing with imaging |
| **MM-T10** Multimodal differential diagnosis | RadFM | Wu et al., *Nature Communications* 2025 | https://github.com/chaoyi-wu/RadFM | 3D VLM supporting differential diagnosis prompting |
| **MM-T12** Multimodal incidental finding | ❌ 无开源工具 | — | — | Pipeline possible (DeepLesion + RadFM + report NER), no integrated tool |

---

## 4. Cross-cutting Summary: Gap Analysis

| Gap | Regions Affected | Notes |
|-----|-----------------|-------|
| **IMG-T6 Longitudinal tracking** | Spine, Bone/Joint | No dedicated open-source tool; `detect-then-track` only validated for liver lesions |
| **IMG-T8 Report generation** | Spine, Bone/Joint | CT2Rep (chest) and RadGPT (abdomen) exist but no spine/bone-specific generators |
| **IMG-T9 Staging/grading** | All three regions | No pure-imaging open-source staging tools for bone/spine (AO/OTA, Genant) or universal TNM |
| **MM-T4 Multimodal measurement** | All three regions | No single integrated tool; requires pipeline orchestration |
| **MM-T12 Multimodal incidental finding** | All three regions | No integrated open-source tool; requires multi-tool pipeline |
| **TXT-T8 Report summarization** | All three regions | No region-specific text summarization tool with paper+code |

---

## 5. Tool Reference Index

| Tool | Primary Paper | GitHub | Regions |
|------|--------------|--------|---------|
| TotalSegmentator | Wasserthal et al., *Radiology:AI* 2023 | https://github.com/wasserth/TotalSegmentator | All (117 structures) |
| nnU-Net | Isensee et al., *Nature Methods* 2021 | https://github.com/MIC-DKFZ/nnUNet | All (self-configuring) |
| MedSAM | Ma et al., *Nature Communications* 2024 | https://github.com/bowang-lab/MedSAM | All (interactive) |
| VISTA3D | MONAI, *CVPR* 2025 | https://github.com/Project-MONAI/VISTA | All (127 classes) |
| DeepLesion/CADLab | Yan et al., *J Med Imaging* 2018 | https://github.com/rsummers11/CADLab | All (universal detection) |
| ULS23 | DIAG, *MedIA* 2025 | https://github.com/DIAGNijmegen/ULS23 | Whole-body (universal seg) |
| CT-CLIP | Hamamci et al., *ECCV* 2024 | https://github.com/ibrahimethemhamamci/CT-CLIP | All (zero-shot VL) |
| Merlin | Blankemeier et al., *ECCV* 2024 | https://github.com/StanfordMIMI/Merlin | All (3D VL) |
| RadFM | Wu et al., *Nature Communications* 2025 | https://github.com/chaoyi-wu/RadFM | All (3D VLM) |
| VerSe | Sekuboyina et al., *MedIA* 2021 | https://github.com/anjany/verse | Spine |
| FracNet | Jin et al., *EBioMedicine* 2020 | https://github.com/M3DV/FracNet | Spine, Bone |
| CTPelvic1K | Liu et al., *MICCAI* 2021 | https://github.com/ICT-MIRACLE-lab/CTPelvic1K | Bone (pelvis) |
| Comp2Comp | Stanford AIMI / Koitka et al. | https://github.com/StanfordMIMI/Comp2Comp | Spine, Whole-body |
| pyradiomics | van Griethuysen et al., *Cancer Research* 2017 | https://github.com/AIM-Harvard/pyradiomics | All (radiomics) |
| WORC | Starmans et al., *European Radiology* 2022 | https://github.com/MStarmans91/WORC | All (radiomics workflow) |
| RadGraph-XL | Jain et al., *ACL* 2024 | https://github.com/Stanford-AIMI/radgraph | All (NLP) |
| medspaCy | Eyre et al., *JAMIA* 2021 | https://github.com/medspacy/medspacy | All (NLP) |
| NegBio | Peng et al., *EMNLP* 2018 | https://github.com/ncbi-nlp/NegBio | All (NLP) |
| llm_extractinator | van Driel et al., *arXiv* 2025 | https://github.com/DIAGNijmegen/llm_extractinator | All (NLP) |
| CT2Rep | Hamamci et al., *MICCAI* 2024 | https://github.com/ibrahimethemhamamci/CT2Rep | Whole-body (chest) |
| RadGPT | Bassi et al., *ICCV* 2025 | https://github.com/MrGiovanni/RadGPT | Whole-body (abdomen) |
| TNM Stage Classifier | Tatonetti Lab, *Nature Communications* | https://github.com/tatonetti-lab/tnm-stage-classifier | Whole-body (MM staging) |
| detect-then-track | alibool, *JIMM* 2025 | https://github.com/alibool/detect-then-track | Whole-body (RECIST tracking) |
| MULAN | Yan et al., *MICCAI* 2019 | https://github.com/rsummers11/CADLab | Whole-body (multi-lesion) |
| AASCE2019 (Cobb angle) | AASCE Challenge, *MICCAI* 2019 | https://github.com/hust-linyi/Seg4Reg | Spine (scoliosis; X-ray based, not CT) |
