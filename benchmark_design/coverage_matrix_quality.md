# CT-Agent Quality Coverage Matrix: 104 Tools × 336 Task Cells

> Generated: 2026-03-26
>
> Classification Rules:
> - **✅ 专用** = Tool specifically trained/validated on this body region + task combination (paper explicitly mentions it, or training dataset includes it)
> - **⚠️ 通用** = General-purpose/foundation model COULD do this but NOT specifically trained/validated for this exact scenario
> - **❌ 无** = No tool at all, not even a general one

## Task Type Legend

| Code | Task |
|------|------|
| IMG-T1 | Anomaly screening |
| IMG-T2 | Lesion detection |
| IMG-T3 | Lesion segmentation |
| IMG-T4 | Anatomy segmentation |
| IMG-T5 | Quantitative measurement |
| IMG-T6 | Longitudinal change tracking |
| IMG-T7 | Classification/characterization |
| IMG-T8 | Report generation (image-only) |
| IMG-T9 | Staging/grading |
| IMG-T11 | Radiomics feature extraction |
| IMG-T12 | Incidental finding detection |
| TXT-T1 | NER extraction |
| TXT-T2 | Relation extraction |
| TXT-T4 | Measurement value extraction |
| TXT-T5 | Temporal report alignment |
| TXT-T7 | Classification label extraction |
| TXT-T8 | Report summarization/generation |
| TXT-T10 | Negation/assertion detection |
| MM-T4 | Multimodal quantitative measurement |
| MM-T7 | Multimodal classification |
| MM-T8 | Multimodal report generation |
| MM-T9 | Multimodal staging/grading |
| MM-T10 | Multimodal differential diagnosis |
| MM-T12 | Multimodal incidental finding management |

---

## 1. Image-only Tasks (IMG) — 14 × 11 = 154 cells

| 部位 | IMG-T1 异常筛查 | IMG-T2 病灶检测 | IMG-T3 病灶分割 | IMG-T4 解剖分割 | IMG-T5 定量测量 | IMG-T6 纵向追踪 | IMG-T7 分类/定性 | IMG-T8 报告生成 | IMG-T9 分期/分级 | IMG-T11 影像组学 | IMG-T12 关键发现 |
|------|---|---|---|---|---|---|---|---|---|---|---|
| **脑/颅内** | ✅ RSNA ICH 1st | ✅ BLAST-CT | ✅ DeepBleed | ✅ TotalSegmentator | ⚠️ TotalSeg+SimpleITK | ⚠️ ANTsPy | ✅ RSNA ICH 1st | ✅ FORTE/BrainGPT | ✅ StrokeViT | ✅ pyradiomics | ✅ RSNA ICH 1st |
| **头颈部** | ⚠️ CT-CLIP | ✅ HECKTOR Winner | ✅ HiLab Head-Neck-GTV | ✅ TotalSegmentator | ⚠️ TotalSeg+SimpleITK | ⚠️ ANTsPy | ⚠️ Merlin | ⚠️ M3D-LaMed | ❌ 无 | ✅ pyradiomics | ⚠️ Merlin |
| **肺** | ✅ CT-CLIP | ✅ lung_nodule_ct_detection | ✅ lungmask | ✅ TotalSegmentator | ✅ TotalSeg+SimpleITK | ⚠️ ANTsPy | ✅ AI-in-Lung-Health | ✅ CT-CHAT | ⚠️ Merlin | ✅ pyradiomics | ✅ PENet |
| **纵隔/心脏** | ⚠️ CT-CLIP | ✅ PENet | ✅ ct_mediastinal_structures | ✅ TotalSegmentator | ✅ DeepCAC | ⚠️ ANTsPy | ✅ PENet | ✅ CT-CHAT | ⚠️ Merlin | ✅ pyradiomics | ✅ PENet |
| **肝脏** | ✅ Merlin | ✅ liver lesion detection | ✅ MULLET | ✅ TotalSegmentator | ✅ TotalSeg+SimpleITK | ⚠️ ANTsPy | ✅ RadiomicsLiverFibrosis | ✅ RadGPT | ✅ RadiomicsLiverFibrosis | ✅ pyradiomics | ✅ RSNA Trauma 1st |
| **胆囊/胆道** | ✅ sato_j-mid_ad | ✅ sato_j-mid_ad | ⚠️ MedSAM | ✅ TotalSegmentator | ⚠️ TotalSeg+SimpleITK | ⚠️ ANTsPy | ✅ sato_j-mid_ad | ⚠️ RadGPT | ❌ 无 | ✅ pyradiomics | ✅ sato_j-mid_ad |
| **胰腺** | ✅ PanDx | ✅ CE-CT PDAC Detection | ✅ pancreas_ct_dints_seg | ✅ TotalSegmentator | ✅ TotalSeg+SimpleITK | ⚠️ ANTsPy | ✅ PanDx | ✅ RadGPT | ⚠️ Merlin | ✅ pyradiomics | ✅ PanDx |
| **脾脏** | ⚠️ Merlin | ⚠️ Merlin | ⚠️ MedSAM | ✅ TotalSegmentator | ✅ TotalSeg+SimpleITK | ⚠️ ANTsPy | ✅ RSNA Trauma 1st | ⚠️ RadGPT | ✅ RSNA Trauma 1st | ✅ pyradiomics | ✅ RSNA Trauma 1st |
| **肾脏/肾上腺** | ⚠️ Merlin | ✅ Kidney Tumor Clf | ✅ KiTS23 2nd | ✅ TotalSegmentator | ✅ TotalSeg+SimpleITK | ⚠️ ANTsPy | ✅ Kidney Tumor Clf | ⚠️ RadGPT | ⚠️ Merlin | ✅ pyradiomics | ✅ RSNA Trauma 1st |
| **胃肠道** | ⚠️ Merlin | ✅ CT Colonography Polyp | ⚠️ MedSAM | ✅ TotalSegmentator | ⚠️ TotalSeg+SimpleITK | ⚠️ ANTsPy | ✅ CT Colonography Polyp | ⚠️ RadGPT | ⚠️ Merlin | ✅ pyradiomics | ⚠️ Merlin |
| **盆腔** | ⚠️ Merlin | ✅ OvSeg | ✅ OvSeg | ✅ TotalSegmentator | ⚠️ TotalSeg+SimpleITK | ⚠️ ANTsPy | ⚠️ Merlin | ⚠️ M3D-LaMed | ⚠️ Merlin | ✅ pyradiomics | ⚠️ Merlin |
| **脊柱** | ⚠️ CT-CLIP | ✅ VCFNet | ⚠️ MedSAM | ✅ TotalSpineSeg | ✅ Comp2Comp | ⚠️ ANTsPy | ✅ VCFNet | ⚠️ M3D-LaMed | ⚠️ Merlin | ✅ pyradiomics | ✅ VCFNet |
| **骨骼/关节** | ⚠️ CT-CLIP | ✅ Maskrcnn_RibFrac | ⚠️ MedSAM | ✅ Skellytour | ⚠️ TotalSeg+SimpleITK | ⚠️ ANTsPy | ✅ FracSegNet | ⚠️ M3D-LaMed | ⚠️ Merlin | ✅ pyradiomics | ✅ Maskrcnn_RibFrac |
| **全身/多部位** | ✅ Merlin | ⚠️ Merlin | ⚠️ MedSAM | ✅ TotalSegmentator | ✅ body-organ-analysis | ⚠️ ANTsPy | ✅ Merlin | ✅ Merlin | ⚠️ Merlin | ✅ pyradiomics | ⚠️ Merlin |

---

## 2. Text-only Tasks (TXT) — 14 × 7 = 98 cells

> Note: Text NLP tools (medspaCy, NegBio, CheXbert, RadGraph-XL, llm_extractinator, Radiology_Bart) are body-region-agnostic by nature. However, strict ✅ 专用 requires the tool to be specifically validated on text from this body region.

| 部位 | TXT-T1 NER提取 | TXT-T2 关系抽取 | TXT-T4 测量值抽取 | TXT-T5 时序对齐 | TXT-T7 分类标签 | TXT-T8 报告摘要 | TXT-T10 否定检测 |
|------|---|---|---|---|---|---|---|
| **脑/颅内** | ✅ RadGraph-XL | ✅ RadGraph-XL | ✅ llm_extractinator | ⚠️ llm_extractinator | ⚠️ CheXbert | ✅ Radiology_Bart | ✅ medspaCy |
| **头颈部** | ✅ RadGraph-XL | ✅ RadGraph-XL | ✅ llm_extractinator | ⚠️ llm_extractinator | ⚠️ CheXbert | ⚠️ Radiology_Bart | ✅ medspaCy |
| **肺** | ✅ RadGraph-XL | ✅ RadGraph-XL | ✅ llm_extractinator | ⚠️ llm_extractinator | ✅ CheXbert | ✅ Radiology_Bart | ✅ medspaCy |
| **纵隔/心脏** | ✅ RadGraph-XL | ✅ RadGraph-XL | ✅ llm_extractinator | ⚠️ llm_extractinator | ✅ CheXbert | ✅ Radiology_Bart | ✅ medspaCy |
| **肝脏** | ✅ RadGraph-XL | ✅ RadGraph-XL | ✅ llm_extractinator | ⚠️ llm_extractinator | ⚠️ CheXbert | ⚠️ Radiology_Bart | ✅ medspaCy |
| **胆囊/胆道** | ✅ RadGraph-XL | ✅ RadGraph-XL | ✅ llm_extractinator | ⚠️ llm_extractinator | ⚠️ CheXbert | ⚠️ Radiology_Bart | ✅ medspaCy |
| **胰腺** | ✅ RadGraph-XL | ✅ RadGraph-XL | ✅ llm_extractinator | ⚠️ llm_extractinator | ⚠️ CheXbert | ⚠️ Radiology_Bart | ✅ medspaCy |
| **脾脏** | ✅ RadGraph-XL | ✅ RadGraph-XL | ✅ llm_extractinator | ⚠️ llm_extractinator | ⚠️ CheXbert | ⚠️ Radiology_Bart | ✅ medspaCy |
| **肾脏/肾上腺** | ✅ RadGraph-XL | ✅ RadGraph-XL | ✅ llm_extractinator | ⚠️ llm_extractinator | ⚠️ CheXbert | ⚠️ Radiology_Bart | ✅ medspaCy |
| **胃肠道** | ✅ RadGraph-XL | ✅ RadGraph-XL | ✅ llm_extractinator | ⚠️ llm_extractinator | ⚠️ CheXbert | ⚠️ Radiology_Bart | ✅ medspaCy |
| **盆腔** | ✅ RadGraph-XL | ✅ RadGraph-XL | ✅ llm_extractinator | ⚠️ llm_extractinator | ⚠️ CheXbert | ⚠️ Radiology_Bart | ✅ medspaCy |
| **脊柱** | ✅ RadGraph-XL | ✅ RadGraph-XL | ✅ llm_extractinator | ⚠️ llm_extractinator | ⚠️ CheXbert | ⚠️ Radiology_Bart | ✅ medspaCy |
| **骨骼/关节** | ✅ RadGraph-XL | ✅ RadGraph-XL | ✅ llm_extractinator | ⚠️ llm_extractinator | ⚠️ CheXbert | ⚠️ Radiology_Bart | ✅ medspaCy |
| **全身/多部位** | ✅ RadGraph-XL | ✅ RadGraph-XL | ✅ llm_extractinator | ⚠️ llm_extractinator | ⚠️ CheXbert | ⚠️ Radiology_Bart | ✅ medspaCy |

### TXT Classification Rationale

- **TXT-T1 (NER):** RadGraph-XL was trained on radiology reports including CT reports across body regions. Its training set explicitly covers CT. → ✅ for all regions.
- **TXT-T2 (Relation extraction):** RadGraph-XL performs entity-relation extraction validated on radiology reports. → ✅ for all regions.
- **TXT-T4 (Measurement extraction):** llm_extractinator was validated on measurement extraction from radiology reports with 93.7% accuracy across body regions. → ✅ for all.
- **TXT-T5 (Temporal alignment):** llm_extractinator can extract longitudinal values, but temporal report alignment was not its primary validated task. → ⚠️ for all.
- **TXT-T7 (Classification labels):** CheXbert was trained specifically on chest X-ray/radiology reports (14 labels). Lung and mediastinum/heart are ✅; other body regions are ⚠️ as the labels are chest-specific.
- **TXT-T8 (Report summarization):** Radiology_Bart was trained on radiology report Findings→Impression summarization. Its training data is primarily chest radiology. Brain reports may also be included in general radiology training. Lung/mediastinum/brain → ✅; others → ⚠️.
- **TXT-T10 (Negation detection):** medspaCy's ConText algorithm is a rule-based clinical NLP tool validated across medical text broadly. → ✅ for all.

---

## 3. Multimodal Tasks (MM) — 14 × 6 = 84 cells

| 部位 | MM-T4 多模态定量 | MM-T7 多模态分类 | MM-T8 多模态报告 | MM-T9 多模态分期 | MM-T10 多模态鉴别诊断 | MM-T12 多模态关键发现 |
|------|---|---|---|---|---|---|
| **脑/颅内** | ⚠️ Merlin | ✅ Merlin | ✅ FORTE/BrainGPT | ⚠️ Merlin | ⚠️ RadFM | ⚠️ Merlin |
| **头颈部** | ⚠️ Merlin | ⚠️ Merlin | ⚠️ M3D-LaMed | ❌ 无 | ⚠️ RadFM | ⚠️ Merlin |
| **肺** | ⚠️ Merlin | ✅ Merlin | ✅ CT-CHAT | ⚠️ Merlin | ⚠️ RadFM | ✅ Merlin |
| **纵隔/心脏** | ⚠️ Merlin | ✅ Merlin | ✅ CT-CHAT | ⚠️ Merlin | ⚠️ RadFM | ✅ Merlin |
| **肝脏** | ✅ Merlin | ✅ Merlin | ✅ RadGPT | ⚠️ Merlin | ⚠️ RadFM | ✅ Merlin |
| **胆囊/胆道** | ⚠️ Merlin | ✅ Merlin | ⚠️ RadGPT | ❌ 无 | ⚠️ RadFM | ⚠️ Merlin |
| **胰腺** | ⚠️ Merlin | ✅ Merlin | ✅ RadGPT | ⚠️ Merlin | ⚠️ RadFM | ✅ Merlin |
| **脾脏** | ⚠️ Merlin | ✅ Merlin | ⚠️ RadGPT | ⚠️ Merlin | ⚠️ RadFM | ✅ Merlin |
| **肾脏/肾上腺** | ⚠️ Merlin | ✅ Merlin | ⚠️ RadGPT | ⚠️ Merlin | ⚠️ RadFM | ✅ Merlin |
| **胃肠道** | ⚠️ Merlin | ⚠️ Merlin | ⚠️ RadGPT | ❌ 无 | ⚠️ RadFM | ⚠️ Merlin |
| **盆腔** | ⚠️ Merlin | ⚠️ Merlin | ⚠️ M3D-LaMed | ❌ 无 | ⚠️ RadFM | ⚠️ Merlin |
| **脊柱** | ⚠️ Merlin | ⚠️ Merlin | ⚠️ M3D-LaMed | ❌ 无 | ⚠️ RadFM | ⚠️ Merlin |
| **骨骼/关节** | ⚠️ Merlin | ⚠️ Merlin | ⚠️ M3D-LaMed | ❌ 无 | ⚠️ RadFM | ⚠️ Merlin |
| **全身/多部位** | ✅ Merlin | ✅ Merlin | ✅ Merlin | ⚠️ Merlin | ⚠️ RadFM | ✅ Merlin |

### MM Classification Rationale

- **MM-T4 (Multimodal quantitative):** Merlin was validated on 692 phenotypes including organ volumes. Liver and whole-body are explicitly in its training → ✅. Other specific organs → ⚠️.
- **MM-T7 (Multimodal classification):** Merlin covers 31 findings across 20 organs. Brain (hemorrhage), lung (nodule, effusion), mediastinum (PE, cardiomegaly), liver (lesion), gallbladder, pancreas, spleen, kidney are explicitly in its 20-organ coverage → ✅. GI tract, pelvis, spine, bone/joint are NOT in its explicit organ list → ⚠️.
- **MM-T8 (Multimodal report):** FORTE/BrainGPT is brain-specific → ✅ for brain. CT-CHAT is chest-specific → ✅ for lung and mediastinum. RadGPT is abdomen-specific (AbdomenAtlas) → ✅ for liver, pancreas; ⚠️ for gallbladder/spleen/kidney/GI (less validated). Others → ⚠️ via M3D-LaMed. Merlin covers whole-body → ✅ for whole-body.
- **MM-T9 (Multimodal staging):** No tool has validated multimodal staging for most specific organs. Merlin can do some phenotyping but not formal staging systems. Head/neck, gallbladder, GI, pelvis, spine, bone → ❌ no tool at all does validated staging.
- **MM-T10 (Multimodal differential diagnosis):** RadFM claims differential diagnosis capability but is not validated on specific body-region differentials → ⚠️ for all.
- **MM-T12 (Multimodal incidental finding):** Merlin's 31-finding classification covers incidentals for its 20 organs → ✅ for organs in its explicit coverage (brain, lung, mediastinum, liver, pancreas, spleen, kidney, whole-body). Others → ⚠️.

---

## 4. Summary Statistics

### Overall Counts

| Level | Count | Percentage |
|-------|-------|-----------|
| ✅ 专用 | 178 | 53.0% |
| ⚠️ 通用 | 150 | 44.6% |
| ❌ 无 | 8 | 2.4% |
| **Total** | **336** | **100%** |

### By Task Category

| Category | Cells | ✅ 专用 | ⚠️ 通用 | ❌ 无 |
|----------|-------|--------|---------|------|
| IMG (Image-only) | 154 | 93 | 59 | 2 |
| TXT (Text-only) | 98 | 61 | 37 | 0 |
| MM (Multimodal) | 84 | 24 | 54 | 6 |
| **Total** | **336** | **178** | **150** | **8** |

### By Body Region (across all 24 task types)

| 部位 | ✅ 专用 | ⚠️ 通用 | ❌ 无 | 专用率 |
|------|--------|---------|------|--------|
| 脑/颅内 | 16 | 8 | 0 | 66.7% |
| 头颈部 | 8 | 14 | 2 | 33.3% |
| 肺 | 18 | 6 | 0 | 75.0% |
| 纵隔/心脏 | 17 | 7 | 0 | 70.8% |
| 肝脏 | 18 | 6 | 0 | 75.0% |
| 胆囊/胆道 | 11 | 11 | 2 | 45.8% |
| 胰腺 | 16 | 8 | 0 | 66.7% |
| 脾脏 | 12 | 12 | 0 | 50.0% |
| 肾脏/肾上腺 | 13 | 11 | 0 | 54.2% |
| 胃肠道 | 8 | 15 | 1 | 33.3% |
| 盆腔 | 8 | 15 | 1 | 33.3% |
| 脊柱 | 10 | 13 | 1 | 41.7% |
| 骨骼/关节 | 9 | 14 | 1 | 37.5% |
| 全身/多部位 | 14 | 10 | 0 | 58.3% |

### By Task Type (across all 14 body regions)

| 任务 | ✅ 专用 | ⚠️ 通用 | ❌ 无 | 专用率 |
|------|--------|---------|------|--------|
| IMG-T1 异常筛查 | 6 | 8 | 0 | 42.9% |
| IMG-T2 病灶检测 | 12 | 2 | 0 | 85.7% |
| IMG-T3 病灶分割 | 8 | 6 | 0 | 57.1% |
| IMG-T4 解剖分割 | 14 | 0 | 0 | 100.0% |
| IMG-T5 定量测量 | 8 | 6 | 0 | 57.1% |
| IMG-T6 纵向追踪 | 0 | 14 | 0 | 0.0% |
| IMG-T7 分类/定性 | 12 | 2 | 0 | 85.7% |
| IMG-T8 报告生成 | 6 | 8 | 0 | 42.9% |
| IMG-T9 分期/分级 | 3 | 9 | 2 | 21.4% |
| IMG-T11 影像组学 | 14 | 0 | 0 | 100.0% |
| IMG-T12 关键发现 | 10 | 4 | 0 | 71.4% |
| TXT-T1 NER提取 | 14 | 0 | 0 | 100.0% |
| TXT-T2 关系抽取 | 14 | 0 | 0 | 100.0% |
| TXT-T4 测量值抽取 | 14 | 0 | 0 | 100.0% |
| TXT-T5 时序对齐 | 0 | 14 | 0 | 0.0% |
| TXT-T7 分类标签 | 2 | 12 | 0 | 14.3% |
| TXT-T8 报告摘要 | 3 | 11 | 0 | 21.4% |
| TXT-T10 否定检测 | 14 | 0 | 0 | 100.0% |
| MM-T4 多模态定量 | 2 | 12 | 0 | 14.3% |
| MM-T7 多模态分类 | 9 | 5 | 0 | 64.3% |
| MM-T8 多模态报告 | 6 | 8 | 0 | 42.9% |
| MM-T9 多模态分期 | 0 | 8 | 6 | 0.0% |
| MM-T10 多模态鉴别 | 0 | 14 | 0 | 0.0% |
| MM-T12 多模态关键发现 | 7 | 7 | 0 | 50.0% |

---

## 5. Gap Analysis: ❌ 无 Cells (8 total)

| 部位 | 任务 | 说明 |
|------|------|------|
| 头颈部 | IMG-T9 分期/分级 | 无头颈肿瘤CT分期的开源工具（HECKTOR仅做分割不做分期） |
| 胆囊/胆道 | IMG-T9 分期/分级 | LI-RADS等胆道分期工具均未开源 |
| 头颈部 | MM-T9 多模态分期 | 同IMG-T9，无任何工具 |
| 胆囊/胆道 | MM-T9 多模态分期 | 同IMG-T9，无任何工具 |
| 胃肠道 | MM-T9 多模态分期 | 无胃肠道肿瘤CT分期开源工具 |
| 盆腔 | MM-T9 多模态分期 | 无盆腔肿瘤CT分期开源工具 |
| 脊柱 | MM-T9 多模态分期 | 无脊柱肿瘤分期开源工具 |
| 骨骼/关节 | MM-T9 多模态分期 | 无骨肿瘤分期开源工具 |

## 6. Key Weakness Areas (高 ⚠️ 通用率)

| 维度 | 弱点 | 原因 |
|------|------|------|
| **IMG-T6 纵向追踪** | 100% 通用 (0% 专用) | ANTsPy是通用配准工具，无任何部位专用的CT纵向追踪模型 |
| **TXT-T5 时序对齐** | 100% 通用 (0% 专用) | llm_extractinator可做纵向值抽取但非其验证任务 |
| **MM-T9 多模态分期** | 0% 专用, 43% ❌ | 分期任务极度缺乏开源工具，多数仅有论文无代码 |
| **MM-T10 多模态鉴别诊断** | 100% 通用 (0% 专用) | RadFM理论上可做但无任何部位的专门验证 |
| **盆腔** | 仅33.3% 专用 | 检测/分割有OvSeg等，但分类/报告/分期严重不足 |
| **胃肠道** | 仅33.3% 专用 | 仅CT Colonography Polyp覆盖息肉，其余任务几乎无专用工具 |

---

## 7. Comparison with Previous Matrix

Previous (non-quality) matrix reported **322/336 = 95.8% covered** with nearly all cells marked ✅.

This quality matrix reveals the true picture:
- **✅ 专用 (validated):** 178/336 = **53.0%** — just over half have truly validated tools
- **⚠️ 通用 (theoretical):** 150/336 = **44.6%** — nearly half rely on general-purpose models
- **❌ 无 (none):** 8/336 = **2.4%** — a small number have no tool at all

The previous matrix conflated ⚠️ 通用 with ✅ 专用, overstating real validated coverage by ~43 percentage points.
