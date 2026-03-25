# CT Benchmark Tool Survey: 肝脏 (Liver)

> 调研日期: 2026-03-25 | 严格规则: 仅收录同时具备**已发表论文**和**GitHub仓库**的工具

---

## IMG-T1 异常筛查 (Anomaly Screening)

| 工具名 | 论文 | GitHub | 关键指标 |
|--------|------|--------|----------|
| CT-CLIP | Hamamci et al., Nature Biomedical Engineering, 2026 | https://github.com/ibrahimethemhamamci/CT-CLIP | Zero-shot multi-abnormality detection; 超越全监督SOTA |
| SyntheticTumors | Hu et al., CVPR 2023 | https://github.com/MrGiovanni/SyntheticTumors | 无标注训练DSC 57.3% (vs 真实标注56.4%); 合成肿瘤通过Visual Turing Test |

> 注: 肝脏CT专用的无监督异常筛查工具较少,上述为可迁移的通用/肝脏方案。

---

## IMG-T2 病灶检测 (Lesion Detection)

| 工具名 | 论文 | GitHub | 关键指标 |
|--------|------|--------|----------|
| MULLET | Wang et al., iScience, 2023 | https://github.com/shenhai1895/Multi-phase-Liver-Lesion-Segmentation | DPC 78.47%, Recall 89.90%, 超越放射科医师水平 |
| SALSA | Balaguer-Montero et al., Cell Reports Medicine, 2025 | https://github.com/radiomicsgroup/liver-SALSA | Patient-wise precision 99.65%, Lesion-level 81.72%, DSC 0.760 |
| Detection-aided Liver Seg | Bellver et al., NIPS Workshop, 2017 | https://github.com/imatge-upc/liverseg-2017-nipsws | LiTS challenge; 检测辅助去除假阳性 |

---

## IMG-T3 病灶分割 (Liver Tumor Segmentation / LiTS)

| 工具名 | 论文 | GitHub | 关键指标 |
|--------|------|--------|----------|
| nnU-Net | Isensee et al., Nature Methods, 2021 | https://github.com/MIC-DKFZ/nnUNet | LiTS Task029预训练模型; 23个数据集SOTA; MICCAI 2020 9/10获胜方案基础 |
| SALSA | Balaguer-Montero et al., Cell Reports Medicine, 2025 | https://github.com/radiomicsgroup/liver-SALSA | DSC 0.760, 基于nnU-Net 3D cascade |
| MULLET | Wang et al., iScience, 2023 | https://github.com/shenhai1895/Multi-phase-Liver-Lesion-Segmentation | 多期CT, Dice 比SOTA高5.80% |
| SyntheticTumors | Hu et al., CVPR 2023 | https://github.com/MrGiovanni/SyntheticTumors | Label-free肝肿瘤分割, DSC 57.3% |
| PVTFormer | Jha et al., arXiv, 2024 | https://github.com/DebeshJha/PVTFormer | LiTS DSC 86.78%, mIoU 78.46%, HD 3.50 |
| livermask | Pedersen & Pérez de Frutos, Zenodo/Software, 2023 | https://github.com/andreped/livermask | 肝实质DSC 0.946; CLI工具, pip安装 |

---

## IMG-T4 分类/良恶性 (HCC vs Metastasis vs Benign)

| 工具名 | 论文 | GitHub | 关键指标 |
|--------|------|--------|----------|
| HCC-deep-learning | Chen et al., npj Precision Oncology, 2020 | https://github.com/drmaxchen-gbc/HCC-deep-learning | HCC病理分类与基因突变预测 |
| MCT-LTDiag (dataset+baseline) | Li et al., Nature Scientific Data, 2025 | Harvard Dataverse (dataset); 基线代码随论文发布 | 517例, 5种肝肿瘤亚型(HCC/ICC/CRLM/BCLM/HH), radiomics+DL baseline |

> 注: 大多数CT肝肿瘤分类研究未公开完整代码。MCT-LTDiag提供了数据集和基线实验代码,HCC-deep-learning基于病理图像。纯CT影像的HCC/met/benign分类目前 **缺少成熟的开源工具**。

---

## IMG-T5 测量/定量 (Measurement / Quantification)

| 工具名 | 论文 | GitHub | 关键指标 |
|--------|------|--------|----------|
| TotalSegmentator | Wasserthal et al., Radiology: AI, 2023 | https://github.com/wasserth/TotalSegmentator | 肝脏体积测量; 104+结构分割; DSC ~0.96(liver) |
| SALSA | Balaguer-Montero et al., Cell Reports Medicine, 2025 | https://github.com/radiomicsgroup/liver-SALSA | 肿瘤体积定量, 优于RECIST单径测量 |
| nnU-Net | Isensee et al., Nature Methods, 2021 | https://github.com/MIC-DKFZ/nnUNet | 分割后可计算体积/三径; 通用分割框架 |

---

## IMG-T6 解剖结构 (Liver Couinaud Segments)

| 工具名 | 论文 | GitHub | 关键指标 |
|--------|------|--------|----------|
| TotalSegmentator | Wasserthal et al., Radiology: AI, 2023; Defined et al., JIIM, 2025 (liver segments扩展) | https://github.com/wasserth/TotalSegmentator | Couinaud S1-S8分割; CT+MRI支持 |
| GLC-UNet (dataset) | Tian et al., MLMI/MICCAI Workshop, 2019 | https://github.com/GLCUnet/dataset | Liver DSC 98.51%, Couinaud DSC 92.46% (仅数据集公开) |

---

## IMG-T7 对比随访 (Longitudinal Follow-up Comparison)

| 工具名 | 论文 | GitHub | 关键指标 |
|--------|------|--------|----------|
| LiFE-Net | Yassine et al., MIDL 2025 (OpenReview) | https://github.com/walid-yassine/LiFE-Net | 首个融合纵向基线CT信息的肝病灶检测框架; self-attention特征融合 |

> 注: RECORD pipeline (npj Precision Oncology, 2024) 可做纵向治疗响应评估(AUC-response 0.981),但**未找到公开GitHub代码**。

---

## IMG-T8 报告生成 (Report Generation from Images)

| 工具名 | 论文 | GitHub | 关键指标 |
|--------|------|--------|----------|
| CT2Rep | Hamamci et al., MICCAI 2024 | https://github.com/ibrahimethemhamamci/CT2Rep | 首个3D CT报告生成方法; auto-regressive causal transformer |
| RadGPT | Bassi et al., ICCV 2025 | https://github.com/MrGiovanni/RadGPT | 9262 CT + 报告; 腹部CT(含肝脏)报告生成; "superhuman" reports |
| CT-CHAT | Hamamci et al., Nature Biomedical Engineering, 2026 | https://github.com/ibrahimethemhamamci/CT-CHAT | 基于CT-CLIP+LLM, 2.7M QA pairs微调 |
| M3D-LaMed | Bai et al., arXiv, 2024 | https://github.com/BAAI-DCAI/M3D | 120K image-text pairs, 662K指令对, 3D医学图像多任务 |
| RadFM | Wu et al., Nature Communications, 2025 | https://github.com/chaoyi-wu/RadFM | 16M 2D/3D图像, 多模态, 超越GPT-4V |

---

## IMG-T9 分期/分级 (LI-RADS Scoring)

| 工具名 | 论文 | GitHub | 关键指标 |
|--------|------|--------|----------|

> **没有找到同时具备论文和GitHub代码的LI-RADS自动评分开源工具。** 已发表的LI-RADS AI工作(如JHEP Reports 2023多中心CT LI-RADS评分、Frontiers in Oncology 2023 MRI LI-RADS自动化)均未公开源代码。

---

## IMG-T11 扫描质量 (Scan Quality Assessment)

| 工具名 | 论文 | GitHub | 关键指标 |
|--------|------|--------|----------|
| LDCT-IQA Winner | Galdran et al., MICCAI 2024 | https://github.com/agaldran/ldct_iqa | LDCT-IQA Challenge冠军; Multi-Head Multi-Loss模型校准 |
| MKCNet | Che et al., CVPR 2023 | https://github.com/chehx/MKCNet | 图像质量感知诊断; Meta-knowledge Co-embedding |

---

## IMG-T12 关键发现 (Critical Findings from Images)

| 工具名 | 论文 | GitHub | 关键指标 |
|--------|------|--------|----------|
| CT-CLIP | Hamamci et al., Nature Biomedical Engineering, 2026 | https://github.com/ibrahimethemhamamci/CT-CLIP | Zero-shot多异常检测, 可用于critical findings筛查 |
| RadFM | Wu et al., Nature Communications, 2025 | https://github.com/chaoyi-wu/RadFM | 多模态VQA, 可回答关键发现相关问题 |

---

## TXT-T1 文本实体抽取 (Named Entity Recognition)

| 工具名 | 论文 | GitHub | 关键指标 |
|--------|------|--------|----------|
| RadGraph | Jain et al., NeurIPS 2021 Datasets Track | https://github.com/Stanford-AIMI/radgraph | Micro-F1 0.82 (MIMIC-CXR); 解剖+观察实体+关系 |
| RadGraph-XL | Jain et al., ACL 2024 Findings | https://github.com/Stanford-AIMI/radgraph | 扩展至胸部CT/腹盆CT/脑MR; 410K entities/relations |
| MedCAT | Kraljevic et al., Artificial Intelligence in Medicine, 2021 | https://github.com/CogStack/MedCAT | NER+Linking; SNOMED-CT/UMLS; 多医院部署验证 |
| CheXpert Labeler | Irvin et al., AAAI 2019 | https://github.com/stanfordmlgroup/chexpert-labeler | 规则NLP, 14种胸部观察提取 |
| CheXbert | Smit et al., EMNLP 2020 | https://github.com/stanfordmlgroup/CheXbert | BERT-based, SOTA报告标签; 超越规则方法 |

---

## TXT-T2 文本分类 (Text Classification / ICD Coding)

| 工具名 | 论文 | GitHub | 关键指标 |
|--------|------|--------|----------|
| PLM-ICD | Huang et al., Clinical NLP Workshop, 2022 | https://github.com/MiuLab/PLM-ICD | MIMIC-3 ICD编码SOTA; RoBERTa/BERT/Longformer |
| CheXbert | Smit et al., EMNLP 2020 | https://github.com/stanfordmlgroup/CheXbert | 14类chest observation分类; 超越规则labeler |

---

## TXT-T4 文本摘要 (Report Summarization)

| 工具名 | 论文 | GitHub | 关键指标 |
|--------|------|--------|----------|
| Summarize-Radiology-Findings | Zhang et al., LOUHI@EMNLP, 2018 | https://github.com/yuhaozhang/summarize-radiology-findings | 放射科医师认为67%生成摘要≥人工水平; Seq2Seq + background encoding |
| XrayGPT | Thawkar et al., BioNLP@ACL, 2024 | https://github.com/mbzuai-oryx/XrayGPT | MedClip+Vicuna; 217K报告摘要训练 |

---

## TXT-T5 数值/测量抽取 (Numeric Extraction)

| 工具名 | 论文 | GitHub | 关键指标 |
|--------|------|--------|----------|
| RadioVicuna | Le Guellec et al., Radiology: AI, 2024 | https://github.com/BastienLeGuellec/RadioVicuna | 开源LLM (Vicuna-13B)信息提取; 无需微调可提取数值/造影剂/异常 |
| RadGraph | Jain et al., NeurIPS 2021 | https://github.com/Stanford-AIMI/radgraph | 实体提取含anatomy修饰, 可提取关联数值 |

> 注: 放射报告中专门的测量值/数值提取工具较少,通用NER+正则表达式方案更常见。

---

## TXT-T7 时序文本对比 (Temporal Text Comparison)

| 工具名 | 论文 | GitHub | 关键指标 |
|--------|------|--------|----------|

> **没有找到同时具备论文和GitHub代码的放射报告时序对比专用工具。** RadGraph的关系类型中包含temporal信息(definitely present/absent),但无专门的时序对比模块。

---

## TXT-T8 文本报告生成 (Text Report Generation)

| 工具名 | 论文 | GitHub | 关键指标 |
|--------|------|--------|----------|
| Summarize-Radiology-Findings | Zhang et al., LOUHI@EMNLP, 2018 | https://github.com/yuhaozhang/summarize-radiology-findings | Findings->Impression生成 |

> 注: 纯文本到文本的报告生成(非图像驱动)见TXT-T4。图像驱动报告生成见IMG-T8。

---

## TXT-T10 文本质量/错误检测 (Report Error Detection)

| 工具名 | 论文 | GitHub | 关键指标 |
|--------|------|--------|----------|
| ReXErr-V1 | Rajpurkar Lab, arXiv, 2024 | https://github.com/rajpurkarlab/ReXErr-V1 | GPT-4o合成临床有意义的报告错误; 错误生成benchmark |

> 注: RRED (Min et al., Clinical NLP 2022) 提出了报告错误检测框架 (AUROC 0.95) 但**未公开代码**。ReXErr侧重错误合成而非检测。该任务目前 **缺少成熟的开源检测工具**。

---

## MM-T4 多模态融合摘要 (Multimodal Summarization)

| 工具名 | 论文 | GitHub | 关键指标 |
|--------|------|--------|----------|
| CT2Rep | Hamamci et al., MICCAI 2024 | https://github.com/ibrahimethemhamamci/CT2Rep | 3D CT→报告; 支持多模态纵向融合 |
| RadGPT | Bassi et al., ICCV 2025 | https://github.com/MrGiovanni/RadGPT | 分割+报告生成融合; 腹部CT含肝脏 |

---

## MM-T7 多模态纵向对比 (Multimodal Longitudinal Comparison)

| 工具名 | 论文 | GitHub | 关键指标 |
|--------|------|--------|----------|
| LiFE-Net | Yassine et al., MIDL 2025 | https://github.com/walid-yassine/LiFE-Net | 纵向CT特征融合+病灶检测 |
| CT2Rep | Hamamci et al., MICCAI 2024 | https://github.com/ibrahimethemhamamci/CT2Rep | 支持hierarchical memory纵向多模态输入 |

---

## MM-T8 多模态报告生成 (Multimodal Report Generation)

| 工具名 | 论文 | GitHub | 关键指标 |
|--------|------|--------|----------|
| CT-CHAT | Hamamci et al., Nature Biomedical Engineering, 2026 | https://github.com/ibrahimethemhamamci/CT-CHAT | CT-CLIP视觉+LLM文本; 2.7M QA对微调 |
| RadFM | Wu et al., Nature Communications, 2025 | https://github.com/chaoyi-wu/RadFM | 2D+3D多模态; 16M图像; 报告生成+VQA |
| M3D-LaMed | Bai et al., arXiv, 2024 | https://github.com/BAAI-DCAI/M3D | 3D VLM; 报告生成+VQA+分割 |
| RadGPT | Bassi et al., ICCV 2025 | https://github.com/MrGiovanni/RadGPT | 9262 CT; segmentation-guided报告生成 |
| FORTE | Li et al., Nature Communications, 2025 | https://github.com/charlierabea/FORTE | 3D脑CT多模态LLM报告生成 (脑部,非肝) |

---

## MM-T9 多模态分期/分级 (Multimodal Staging)

| 工具名 | 论文 | GitHub | 关键指标 |
|--------|------|--------|----------|

> **没有找到同时具备论文和GitHub代码的肝脏多模态分期/分级工具(如LI-RADS结合影像+文本)。**

---

## MM-T10 多模态匹配/检索 (Multimodal Matching / Retrieval)

| 工具名 | 论文 | GitHub | 关键指标 |
|--------|------|--------|----------|
| CT-CLIP | Hamamci et al., Nature Biomedical Engineering, 2026 | https://github.com/ibrahimethemhamamci/CT-CLIP | 3D CT-Report对比学习; case retrieval; zero-shot分类 |
| BiomedCLIP | Zhang et al., arXiv, 2023 | https://github.com/microsoft/BiomedCLIP_data_pipeline (HuggingFace model) | 15M图文对预训练; 跨模态检索; 超越MedCLIP/PubMedCLIP |
| MedCLIP | Wang et al., EMNLP 2022 | https://github.com/RyanWangZf/MedCLIP | 解耦图文对比学习; 语义匹配loss |
| M3D-CLIP | Bai et al., arXiv, 2024 | https://github.com/BAAI-DCAI/M3D | 3D医学图像CLIP; image-text retrieval |

---

## MM-T12 多模态关键发现 (Multimodal Critical Findings)

| 工具名 | 论文 | GitHub | 关键指标 |
|--------|------|--------|----------|
| CT-CHAT | Hamamci et al., Nature Biomedical Engineering, 2026 | https://github.com/ibrahimethemhamamci/CT-CHAT | 3D CT VQA, 可查询关键发现 |
| RadFM | Wu et al., Nature Communications, 2025 | https://github.com/chaoyi-wu/RadFM | 多模态VQA, 2D+3D, 可识别关键发现 |

---

## 汇总: 无开源工具的任务

| 任务 | 状态 |
|------|------|
| **IMG-T9** 分期/分级 (LI-RADS) | 没有找到同时具备论文+GitHub的开源工具 |
| **TXT-T7** 时序文本对比 | 没有找到同时具备论文+GitHub的开源工具 |
| **TXT-T10** 文本质量/错误检测 | 没有找到成熟的开源检测工具 (仅有错误合成工具ReXErr) |
| **MM-T9** 多模态分期/分级 | 没有找到同时具备论文+GitHub的开源工具 |

---

Sources:
- [nnU-Net - GitHub](https://github.com/MIC-DKFZ/nnUNet)
- [TotalSegmentator - GitHub](https://github.com/wasserth/TotalSegmentator)
- [TotalSegmentator Paper - Radiology: AI](https://pubs.rsna.org/doi/full/10.1148/ryai.230024)
- [SALSA - GitHub](https://github.com/radiomicsgroup/liver-SALSA)
- [SALSA Paper - Cell Reports Medicine](https://www.cell.com/cell-reports-medicine/fulltext/S2666-3791(25)00105-3)
- [MULLET - GitHub](https://github.com/shenhai1895/Multi-phase-Liver-Lesion-Segmentation)
- [MULLET Paper - iScience](https://www.sciencedirect.com/science/article/pii/S2589004223022605)
- [CT-CLIP / CT-CHAT - GitHub](https://github.com/ibrahimethemhamamci/CT-CLIP)
- [CT-CLIP Paper - arXiv](https://arxiv.org/abs/2403.17834)
- [CT2Rep - GitHub](https://github.com/ibrahimethemhamamci/CT2Rep)
- [CT2Rep Paper - MICCAI 2024](https://papers.miccai.org/miccai-2024/181-Paper2185.html)
- [RadFM - GitHub](https://github.com/chaoyi-wu/RadFM)
- [RadFM Paper - Nature Communications](https://www.nature.com/articles/s41467-025-62385-7)
- [M3D-LaMed - GitHub](https://github.com/BAAI-DCAI/M3D)
- [M3D Paper - arXiv](https://arxiv.org/abs/2404.00578)
- [RadGPT - GitHub](https://github.com/MrGiovanni/RadGPT)
- [RadGraph - GitHub](https://github.com/Stanford-AIMI/radgraph)
- [RadGraph Paper - arXiv](https://arxiv.org/abs/2106.14463)
- [MedCAT - GitHub](https://github.com/CogStack/MedCAT)
- [CheXbert - GitHub](https://github.com/stanfordmlgroup/CheXbert)
- [CheXbert Paper - arXiv](https://arxiv.org/abs/2004.09167)
- [PLM-ICD - GitHub](https://github.com/MiuLab/PLM-ICD)
- [PLM-ICD Paper - ACL Anthology](https://aclanthology.org/2022.clinicalnlp-1.2/)
- [Summarize Radiology Findings - GitHub](https://github.com/yuhaozhang/summarize-radiology-findings)
- [Zhang et al. Paper - ACL Anthology](https://aclanthology.org/W18-5623/)
- [SyntheticTumors - GitHub](https://github.com/MrGiovanni/SyntheticTumors)
- [SyntheticTumors Paper - CVPR 2023](https://openaccess.thecvf.com/content/CVPR2023/html/Hu_Label-Free_Liver_Tumor_Segmentation_CVPR_2023_paper.html)
- [livermask - GitHub](https://github.com/andreped/livermask)
- [PVTFormer - GitHub](https://github.com/DebeshJha/PVTFormer)
- [Detection-aided Liver Seg - GitHub](https://github.com/imatge-upc/liverseg-2017-nipsws)
- [LDCT-IQA Winner - GitHub](https://github.com/agaldran/ldct_iqa)
- [MKCNet - GitHub](https://github.com/chehx/MKCNet)
- [LiFE-Net - GitHub](https://github.com/walid-yassine/LiFE-Net)
- [LiFE-Net Paper - OpenReview](https://openreview.net/forum?id=32h0bBn6YZ)
- [BiomedCLIP Paper - arXiv](https://arxiv.org/abs/2303.00915)
- [MedCLIP - GitHub](https://github.com/RyanWangZf/MedCLIP)
- [RadioVicuna - GitHub](https://github.com/BastienLeGuellec/RadioVicuna)
- [XrayGPT - GitHub](https://github.com/mbzuai-oryx/XrayGPT)
- [ReXErr-V1 - GitHub](https://github.com/rajpurkarlab/ReXErr-V1)
- [HCC-deep-learning - GitHub](https://github.com/drmaxchen-gbc/HCC-deep-learning)
- [MCT-LTDiag Paper - Nature Scientific Data](https://www.nature.com/articles/s41597-025-06343-4)
- [GLC-UNet dataset - GitHub](https://github.com/GLCUnet/dataset)
- [FORTE - GitHub](https://github.com/charlierabea/FORTE)
- [CheXpert Labeler - GitHub](https://github.com/stanfordmlgroup/chexpert-labeler)