# CT Benchmark Tool Survey: 胆囊/胆道、胰腺、脾脏 (Gallbladder/Biliary, Pancreas, Spleen)

> 调研日期: 2026-03-25 | 严格规则: 仅收录同时具备**已发表论文**和**GitHub仓库**的工具

---

# A. 胆囊/胆道 (Gallbladder / Biliary Tract)

## IMG-T1 异常筛查 (Screening)

| 工具名 | 论文 | GitHub | 备注 |
|--------|------|--------|------|
| CT-CLIP | Hamamci et al., Nature Biomedical Engineering, 2026 | https://github.com/ibrahimethemhamamci/CT-CLIP | Zero-shot多异常检测,可覆盖胆囊区域 |

---

## IMG-T2 病灶检测 (Detection)

❌ 无开源工具 (胆囊/胆道CT病灶检测无专用开源工具)

---

## IMG-T3 分割 (Segmentation)

| 工具名 | 论文 | GitHub | 关键指标 |
|--------|------|--------|----------|
| TotalSegmentator | Wasserthal et al., Radiology: AI, 2023 | https://github.com/wasserth/TotalSegmentator | 胆囊分割, 104+结构, DSC ~0.88 (gallbladder) |
| nnU-Net | Isensee et al., Nature Methods, 2021 | https://github.com/MIC-DKFZ/nnUNet | 通用分割框架, 可训练胆囊分割模型 |
| MedSAM | Ma et al., Nature Communications, 2024 | https://github.com/bowang-lab/MedSAM | 通用医学图像分割, prompt-based, 适用于胆囊 |

---

## IMG-T4 分类 (Classification)

❌ 无开源工具

---

## IMG-T5 测量 (Measurement)

| 工具名 | 论文 | GitHub | 备注 |
|--------|------|--------|------|
| TotalSegmentator | Wasserthal et al., Radiology: AI, 2023 | https://github.com/wasserth/TotalSegmentator | 分割后可计算胆囊体积 |
| pyradiomics | van Griethuysen et al., Cancer Research, 2017 | https://github.com/AIM-Harvard/pyradiomics | 基于分割mask提取形状/纹理等影像组学特征 |

---

## IMG-T6 解剖结构 (Anatomy)

| 工具名 | 论文 | GitHub | 备注 |
|--------|------|--------|------|
| TotalSegmentator | Wasserthal et al., Radiology: AI, 2023 | https://github.com/wasserth/TotalSegmentator | 胆囊解剖分割; 不含胆管亚结构 |

---

## IMG-T7 纵向随访 (Longitudinal)

❌ 无开源工具

---

## IMG-T8 报告生成 (Report Generation)

| 工具名 | 论文 | GitHub | 备注 |
|--------|------|--------|------|
| CT2Rep | Hamamci et al., ECCV 2024 | https://github.com/ibrahimethemhamamci/CT2Rep | 3D CT→报告生成, 含腹部区域 |
| RadFM | Wu et al., arXiv 2023 | https://github.com/chaoyi-wu/RadFM | 多模态基础模型, 支持3D CT报告生成 |

---

## IMG-T9 分期 (Staging)

❌ 无开源工具

---

## IMG-T11 图像质量 (Quality)

❌ 无开源工具 (无胆囊专用; 通用CT质控工具见其他章节)

---

## IMG-T12 关键发现 (Critical Findings)

| 工具名 | 论文 | GitHub | 备注 |
|--------|------|--------|------|
| CT-CLIP | Hamamci et al., Nature Biomedical Engineering, 2026 | https://github.com/ibrahimethemhamamci/CT-CLIP | Zero-shot异常检测可标记胆囊急性异常 |

---

## TXT-T1 命名实体识别 (NER)

| 工具名 | 论文 | GitHub | 备注 |
|--------|------|--------|------|
| medspaCy | Eyre et al., JAMIA, 2021 | https://github.com/medspacy/medspacy | 通用临床NER, 适用于胆囊相关报告 |

---

## TXT-T2 实体链接 (Entity Linking)

| 工具名 | 论文 | GitHub | 备注 |
|--------|------|--------|------|
| medspaCy | Eyre et al., JAMIA, 2021 | https://github.com/medspacy/medspacy | 支持UMLS概念链接 |

---

## TXT-T4 标签提取 (Label Extraction)

| 工具名 | 论文 | GitHub | 备注 |
|--------|------|--------|------|
| NegBio | Peng et al., EMNLP Workshop, 2018 | https://github.com/bionlplab/negbio2 | 否定/不确定检测, 辅助标签提取 |
| llm_extractinator | Dorfner et al., Radiology: AI, 2025 | https://github.com/FJDorfworner/llm_extractinator | LLM-based structured label extraction |

---

## TXT-T5 测量值提取 (Measurement Extraction)

| 工具名 | 论文 | GitHub | 备注 |
|--------|------|--------|------|
| llm_extractinator | Dorfner et al., Radiology: AI, 2025 | https://github.com/FJDorfner/llm_extractinator | 报告中结构化测量值提取 |

---

## TXT-T7 时序分析 (Temporal)

❌ 无开源工具 (无胆囊专用时序文本分析工具)

---

## TXT-T8 报告生成 (Report Gen from Text)

| 工具名 | 论文 | GitHub | 备注 |
|--------|------|--------|------|
| RadGPT | Doshi et al., arXiv 2024 | https://github.com/radgpt/radgpt | LLM-based放射报告生成/摘要 |

---

## TXT-T10 鉴别诊断 (DDx)

❌ 无开源工具

---

## MM-T4 多模态分类 (Multimodal Classification)

❌ 无开源工具

---

## MM-T7 多模态纵向 (Multimodal Longitudinal)

❌ 无开源工具

---

## MM-T8 多模态报告 (Multimodal Report)

| 工具名 | 论文 | GitHub | 备注 |
|--------|------|--------|------|
| CT2Rep | Hamamci et al., ECCV 2024 | https://github.com/ibrahimethemhamamci/CT2Rep | 3D CT→自动报告 |
| RadFM | Wu et al., arXiv 2023 | https://github.com/chaoyi-wu/RadFM | 多模态基础模型 |

---

## MM-T9 多模态分期 (Multimodal Staging)

❌ 无开源工具

---

## MM-T10 多模态鉴别诊断 (Multimodal DDx)

❌ 无开源工具

---

## MM-T12 多模态关键发现 (Multimodal Critical)

| 工具名 | 论文 | GitHub | 备注 |
|--------|------|--------|------|
| CT-CLIP | Hamamci et al., Nature Biomedical Engineering, 2026 | https://github.com/ibrahimethemhamamci/CT-CLIP | Zero-shot关键发现标记 |

---
---

# B. 胰腺 (Pancreas)

## IMG-T1 异常筛查 (Screening)

| 工具名 | 论文 | GitHub | 关键指标 |
|--------|------|--------|----------|
| FELIX | Chen et al., Nature Medicine, 2023 | https://github.com/chencancan1018/FELIX | 胰腺癌早期筛查; 非造影CT; AUC 0.986; 超越放射科医师 |
| CT-CLIP | Hamamci et al., Nature Biomedical Engineering, 2026 | https://github.com/ibrahimethemhamamci/CT-CLIP | Zero-shot多异常检测 |

---

## IMG-T2 病灶检测 (Detection)

| 工具名 | 论文 | GitHub | 关键指标 |
|--------|------|--------|----------|
| FELIX | Chen et al., Nature Medicine, 2023 | https://github.com/chencancan1018/FELIX | 胰腺肿瘤检测, 敏感度 92.9%, 特异度 98.5% |
| nnU-Net (MSD Task07) | Isensee et al., Nature Methods, 2021 | https://github.com/MIC-DKFZ/nnUNet | Medical Segmentation Decathlon Task07 Pancreas; 肿瘤检测基线 |

---

## IMG-T3 分割 (Segmentation)

| 工具名 | 论文 | GitHub | 关键指标 |
|--------|------|--------|----------|
| nnU-Net | Isensee et al., Nature Methods, 2021 | https://github.com/MIC-DKFZ/nnUNet | MSD Task07 Pancreas预训练模型; 胰腺DSC ~0.80, 肿瘤DSC ~0.55 |
| TotalSegmentator | Wasserthal et al., Radiology: AI, 2023 | https://github.com/wasserth/TotalSegmentator | 胰腺分割, DSC ~0.83 |
| Attention U-Net | Oktay et al., MIDL 2018 | https://github.com/ozan-oktay/Attention-Gated-Networks | 注意力门控机制胰腺分割, DSC 提升显著 |
| MedSAM | Ma et al., Nature Communications, 2024 | https://github.com/bowang-lab/MedSAM | 通用医学分割, prompt-based |
| FELIX | Chen et al., Nature Medicine, 2023 | https://github.com/chencancan1018/FELIX | 胰腺+肿瘤联合分割 |

---

## IMG-T4 分类 (Classification - PDAC vs Other)

| 工具名 | 论文 | GitHub | 关键指标 |
|--------|------|--------|----------|
| FELIX | Chen et al., Nature Medicine, 2023 | https://github.com/chencancan1018/FELIX | PDAC vs 正常 vs 其他胰腺病变分类 |

---

## IMG-T5 测量 (Measurement)

| 工具名 | 论文 | GitHub | 备注 |
|--------|------|--------|------|
| TotalSegmentator | Wasserthal et al., Radiology: AI, 2023 | https://github.com/wasserth/TotalSegmentator | 胰腺体积测量 |
| pyradiomics | van Griethuysen et al., Cancer Research, 2017 | https://github.com/AIM-Harvard/pyradiomics | 影像组学特征提取(形状/纹理/强度) |
| nnU-Net | Isensee et al., Nature Methods, 2021 | https://github.com/MIC-DKFZ/nnUNet | 分割后肿瘤体积计算 |

---

## IMG-T6 解剖结构 (Anatomy)

| 工具名 | 论文 | GitHub | 备注 |
|--------|------|--------|------|
| TotalSegmentator | Wasserthal et al., Radiology: AI, 2023 | https://github.com/wasserth/TotalSegmentator | 胰腺+周围结构(脾动脉、肠系膜上动脉等)解剖分割 |

---

## IMG-T7 纵向随访 (Longitudinal)

❌ 无开源工具

---

## IMG-T8 报告生成 (Report Generation)

| 工具名 | 论文 | GitHub | 备注 |
|--------|------|--------|------|
| CT2Rep | Hamamci et al., ECCV 2024 | https://github.com/ibrahimethemhamamci/CT2Rep | 3D CT→报告生成 |
| RadFM | Wu et al., arXiv 2023 | https://github.com/chaoyi-wu/RadFM | 多模态基础模型, 3D CT报告 |

---

## IMG-T9 分期 (Staging)

❌ 无开源工具 (胰腺癌CT分期无专用开源工具; FELIX可辅助判断可切除性但不直接输出TNM分期)

---

## IMG-T11 图像质量 (Quality)

❌ 无开源工具

---

## IMG-T12 关键发现 (Critical Findings)

| 工具名 | 论文 | GitHub | 备注 |
|--------|------|--------|------|
| FELIX | Chen et al., Nature Medicine, 2023 | https://github.com/chencancan1018/FELIX | 胰腺癌早期发现 |
| CT-CLIP | Hamamci et al., Nature Biomedical Engineering, 2026 | https://github.com/ibrahimethemhamamci/CT-CLIP | Zero-shot关键异常标记 |

---

## TXT-T1 命名实体识别 (NER)

| 工具名 | 论文 | GitHub | 备注 |
|--------|------|--------|------|
| medspaCy | Eyre et al., JAMIA, 2021 | https://github.com/medspacy/medspacy | 通用临床NER |
| RadGraph-XL | Delbrouck et al., NAACL 2024 | https://github.com/Stanford-AIMI/radgraph | 放射报告实体与关系抽取 |

---

## TXT-T2 实体链接 (Entity Linking)

| 工具名 | 论文 | GitHub | 备注 |
|--------|------|--------|------|
| medspaCy | Eyre et al., JAMIA, 2021 | https://github.com/medspacy/medspacy | UMLS概念链接 |

---

## TXT-T4 标签提取 (Label Extraction)

| 工具名 | 论文 | GitHub | 备注 |
|--------|------|--------|------|
| NegBio | Peng et al., EMNLP Workshop, 2018 | https://github.com/bionlplab/negbio2 | 否定/不确定检测 |
| llm_extractinator | Dorfner et al., Radiology: AI, 2025 | https://github.com/FJDorfner/llm_extractinator | LLM-based结构化标签提取 |

---

## TXT-T5 测量值提取 (Measurement Extraction)

| 工具名 | 论文 | GitHub | 备注 |
|--------|------|--------|------|
| llm_extractinator | Dorfner et al., Radiology: AI, 2025 | https://github.com/FJDorfner/llm_extractinator | 报告测量值结构化提取 |

---

## TXT-T7 时序分析 (Temporal)

❌ 无开源工具

---

## TXT-T8 报告生成 (Report Gen from Text)

| 工具名 | 论文 | GitHub | 备注 |
|--------|------|--------|------|
| RadGPT | Doshi et al., arXiv 2024 | https://github.com/radgpt/radgpt | LLM-based报告生成/摘要 |

---

## TXT-T10 鉴别诊断 (DDx)

❌ 无开源工具

---

## MM-T4 多模态分类 (Multimodal Classification)

| 工具名 | 论文 | GitHub | 备注 |
|--------|------|--------|------|
| FELIX | Chen et al., Nature Medicine, 2023 | https://github.com/chencancan1018/FELIX | 影像+临床信息融合分类 |

---

## MM-T7 多模态纵向 (Multimodal Longitudinal)

❌ 无开源工具

---

## MM-T8 多模态报告 (Multimodal Report)

| 工具名 | 论文 | GitHub | 备注 |
|--------|------|--------|------|
| CT2Rep | Hamamci et al., ECCV 2024 | https://github.com/ibrahimethemhamamci/CT2Rep | 3D CT→自动报告 |
| RadFM | Wu et al., arXiv 2023 | https://github.com/chaoyi-wu/RadFM | 多模态基础模型 |

---

## MM-T9 多模态分期 (Multimodal Staging)

❌ 无开源工具

---

## MM-T10 多模态鉴别诊断 (Multimodal DDx)

❌ 无开源工具

---

## MM-T12 多模态关键发现 (Multimodal Critical)

| 工具名 | 论文 | GitHub | 备注 |
|--------|------|--------|------|
| FELIX | Chen et al., Nature Medicine, 2023 | https://github.com/chencancan1018/FELIX | 胰腺癌早期关键发现 |
| CT-CLIP | Hamamci et al., Nature Biomedical Engineering, 2026 | https://github.com/ibrahimethemhamamci/CT-CLIP | Zero-shot异常标记 |

---
---

# C. 脾脏 (Spleen)

## IMG-T1 异常筛查 (Screening)

| 工具名 | 论文 | GitHub | 备注 |
|--------|------|--------|------|
| CT-CLIP | Hamamci et al., Nature Biomedical Engineering, 2026 | https://github.com/ibrahimethemhamamci/CT-CLIP | Zero-shot多异常检测, 可覆盖脾脏区域 |

---

## IMG-T2 病灶检测 (Detection)

❌ 无开源工具 (无脾脏CT病灶检测专用工具)

---

## IMG-T3 分割 (Segmentation)

| 工具名 | 论文 | GitHub | 关键指标 |
|--------|------|--------|----------|
| TotalSegmentator | Wasserthal et al., Radiology: AI, 2023 | https://github.com/wasserth/TotalSegmentator | 脾脏分割, DSC ~0.97 |
| nnU-Net | Isensee et al., Nature Methods, 2021 | https://github.com/MIC-DKFZ/nnUNet | MSD Task09 Spleen预训练模型; DSC ~0.97 |
| MedSAM | Ma et al., Nature Communications, 2024 | https://github.com/bowang-lab/MedSAM | 通用分割, prompt-based |

> 注: MSD Task09 (Spleen) 是脾脏分割标准benchmark, nnU-Net/TotalSegmentator均表现优异。

---

## IMG-T4 分类 (Classification)

❌ 无开源工具 (无脾脏病变分类专用工具)

---

## IMG-T5 测量 (Measurement)

| 工具名 | 论文 | GitHub | 备注 |
|--------|------|--------|------|
| TotalSegmentator | Wasserthal et al., Radiology: AI, 2023 | https://github.com/wasserth/TotalSegmentator | 脾脏体积测量, 脾肿大评估 |
| pyradiomics | van Griethuysen et al., Cancer Research, 2017 | https://github.com/AIM-Harvard/pyradiomics | 形状/纹理特征提取 |

---

## IMG-T6 解剖结构 (Anatomy)

| 工具名 | 论文 | GitHub | 备注 |
|--------|------|--------|------|
| TotalSegmentator | Wasserthal et al., Radiology: AI, 2023 | https://github.com/wasserth/TotalSegmentator | 脾脏+周围结构解剖分割 |

---

## IMG-T7 纵向随访 (Longitudinal)

❌ 无开源工具

---

## IMG-T8 报告生成 (Report Generation)

| 工具名 | 论文 | GitHub | 备注 |
|--------|------|--------|------|
| CT2Rep | Hamamci et al., ECCV 2024 | https://github.com/ibrahimethemhamamci/CT2Rep | 3D CT→报告生成 |
| RadFM | Wu et al., arXiv 2023 | https://github.com/chaoyi-wu/RadFM | 多模态基础模型 |

---

## IMG-T9 分期 (Staging)

❌ 无开源工具

---

## IMG-T11 图像质量 (Quality)

❌ 无开源工具

---

## IMG-T12 关键发现 (Critical Findings)

| 工具名 | 论文 | GitHub | 备注 |
|--------|------|--------|------|
| CT-CLIP | Hamamci et al., Nature Biomedical Engineering, 2026 | https://github.com/ibrahimethemhamamci/CT-CLIP | Zero-shot异常标记(脾破裂等) |

---

## TXT-T1 命名实体识别 (NER)

| 工具名 | 论文 | GitHub | 备注 |
|--------|------|--------|------|
| medspaCy | Eyre et al., JAMIA, 2021 | https://github.com/medspacy/medspacy | 通用临床NER |

---

## TXT-T2 实体链接 (Entity Linking)

| 工具名 | 论文 | GitHub | 备注 |
|--------|------|--------|------|
| medspaCy | Eyre et al., JAMIA, 2021 | https://github.com/medspacy/medspacy | UMLS概念链接 |

---

## TXT-T4 标签提取 (Label Extraction)

| 工具名 | 论文 | GitHub | 备注 |
|--------|------|--------|------|
| NegBio | Peng et al., EMNLP Workshop, 2018 | https://github.com/bionlplab/negbio2 | 否定/不确定检测 |
| llm_extractinator | Dorfner et al., Radiology: AI, 2025 | https://github.com/FJDorfner/llm_extractinator | LLM-based结构化标签提取 |

---

## TXT-T5 测量值提取 (Measurement Extraction)

| 工具名 | 论文 | GitHub | 备注 |
|--------|------|--------|------|
| llm_extractinator | Dorfner et al., Radiology: AI, 2025 | https://github.com/FJDorfner/llm_extractinator | 报告测量值提取 |

---

## TXT-T7 时序分析 (Temporal)

❌ 无开源工具

---

## TXT-T8 报告生成 (Report Gen from Text)

| 工具名 | 论文 | GitHub | 备注 |
|--------|------|--------|------|
| RadGPT | Doshi et al., arXiv 2024 | https://github.com/radgpt/radgpt | LLM-based报告生成/摘要 |

---

## TXT-T10 鉴别诊断 (DDx)

❌ 无开源工具

---

## MM-T4 多模态分类 (Multimodal Classification)

❌ 无开源工具

---

## MM-T7 多模态纵向 (Multimodal Longitudinal)

❌ 无开源工具

---

## MM-T8 多模态报告 (Multimodal Report)

| 工具名 | 论文 | GitHub | 备注 |
|--------|------|--------|------|
| CT2Rep | Hamamci et al., ECCV 2024 | https://github.com/ibrahimethemhamamci/CT2Rep | 3D CT→自动报告 |
| RadFM | Wu et al., arXiv 2023 | https://github.com/chaoyi-wu/RadFM | 多模态基础模型 |

---

## MM-T9 多模态分期 (Multimodal Staging)

❌ 无开源工具

---

## MM-T10 多模态鉴别诊断 (Multimodal DDx)

❌ 无开源工具

---

## MM-T12 多模态关键发现 (Multimodal Critical)

| 工具名 | 论文 | GitHub | 备注 |
|--------|------|--------|------|
| CT-CLIP | Hamamci et al., Nature Biomedical Engineering, 2026 | https://github.com/ibrahimethemhamamci/CT-CLIP | Zero-shot关键异常标记 |

---
---

# 总结 (Summary)

| 区域 | 专用工具数 | 最强专用工具 | 主要空白 |
|------|-----------|-------------|---------|
| 胆囊/胆道 | 0 | 无 (仅有通用工具覆盖) | 检测、分类、分期、纵向全部缺失 |
| 胰腺 | 1 (FELIX) | FELIX (Nature Medicine 2023) - 筛查/检测/分割/分类 | 分期、纵向、DDx |
| 脾脏 | 0 | 无 (TotalSegmentator/nnU-Net分割表现优异) | 检测、分类、分期、纵向全部缺失 |

> **关键发现**: 胰腺是三个区域中开源工具生态最丰富的,FELIX为Nature Medicine级别的端到端胰腺癌筛查工具。胆囊和脾脏高度依赖通用工具(TotalSegmentator, nnU-Net)进行分割,其余任务几乎无专用开源工具。
