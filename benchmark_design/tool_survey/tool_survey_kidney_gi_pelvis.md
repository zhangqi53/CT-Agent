# CT-Agent Benchmark 工具调研：肾脏/肾上腺、胃肠道、盆腔

> 版本: 1.0 | 日期: 2026-03-25
>
> 选入标准 (STRICT): 必须**同时**具备 (1) 已发表论文 (2) 公开 GitHub 仓库。不满足者标注 "无开源工具"。
>
> 任务编码说明: IMG = 仅图像输入, TXT = 仅文本输入, MM = 图文融合输入。

---

## 一、肾脏/肾上腺 (Kidney/Adrenal) — 区域编号 09

### IMG 类任务

| 任务 | 工具名 | 论文 (作者, 期刊, 年份) | GitHub URL | 关键指标 |
|------|--------|------------------------|------------|----------|
| **IMG-T1 异常筛查** | NHS Adrenal Lesion Screening | NHS AI Lab Skunkworks, medRxiv 2023 | https://github.com/nhsx/skunkworks-adrenal-lesions-detection | AUC 0.95 (adrenal) |
| | DeepLesion (通用) | Yan et al., J Med Imaging 2018 | https://github.com/rsummers11/CADLab | Sens 0.84 @ 4 FP/vol |
| **IMG-T2 病灶检测/定位** | DeepLesion (ULD) | Yan et al., J Med Imaging 2018 | https://github.com/rsummers11/CADLab | Sens 0.84 @ 4 FP/vol |
| | Kidney Stone Detection | Yildirim et al., Comput Biol Med 2021 | https://github.com/muhammedtalo/Kidney_stone_detection | Acc 96.82% |
| | Auto-Adrenal-Screen-Tool | Ruf et al., Eur J Radiol 2025 (nnU-Net) | https://github.com/XmySz/Auto-Adrenal-Screen-Tool | nnU-Net adrenal volumetry |
| **IMG-T3 病灶分割** | KiTS23 + nnU-Net | Heller et al., MedIA 2023 (KiTS19/23 Challenge) | https://github.com/neheller/kits23 | Dice 0.835 (kidney+tumor) |
| | nnU-Net (通用框架) | Isensee et al., Nature Methods 2021 | https://github.com/MIC-DKFZ/nnUNet | KiTS Dice ~0.87 |
| | ULS23 (通用病灶分割) | de Grauw et al., MedIA 2025 | https://github.com/DIAGNijmegen/ULS23 | Dice 0.703 (全身) |
| | MedSAM (交互式) | Ma et al., Nature Communications 2024 | https://github.com/bowang-lab/MedSAM | Dice 0.85+ (prompted) |
| **IMG-T4 分类/良恶性判断** | Renal-Mass-AI | Wang et al., Nature Communications 2025 | https://github.com/shuowang26/renal-mass-ai | AUC 0.783-0.847 (malignancy) |
| | Kidney-Cancer-AI (SRM) | Wang et al., Radiology 2024 | https://github.com/shuowang26/kidney-cancer-ai | AUC 0.80 (benign SRM) |
| **IMG-T5 测量/定量分析** | pyradiomics | van Griethuysen et al., Cancer Research 2017 | https://github.com/AIM-Harvard/pyradiomics | ~1500 features/image |
| | TotalSegmentator + 体积计算 | Wasserthal et al., Radiology:AI 2023 | https://github.com/wasserth/TotalSegmentator | Dice 0.943 (含 kidney L/R, adrenal L/R) |
| **IMG-T6 解剖结构识别** | TotalSegmentator | Wasserthal et al., Radiology:AI 2023 | https://github.com/wasserth/TotalSegmentator | Dice 0.943; 含 kidney, adrenal 等 117 类 |
| | MONAI VISTA3D | MONAI Consortium, CVPR 2025 | https://github.com/Project-MONAI/VISTA | 127 类 CT 分割 |
| **IMG-T7 对比随访分析** | LesionLocator | Rokuss et al., CVPR 2025 | https://github.com/MIC-DKFZ/LesionLocator | SOTA longitudinal tracking; ~10 Dice points > prior |
| | detect-then-track | Zhou et al., J Digit Imaging Inform Med 2025 | https://github.com/alibool/detect-then-track | RECIST Acc 82.1% |
| **IMG-T8 报告生成** | RadGPT | Bassi et al., ICCV 2025 (AbdomenAtlas 9262 vols) | https://github.com/MrGiovanni/RadGPT | Kidney tumor Sens 92% (large), 92/78% (small) |
| | CT2Rep | Hamamci et al., MICCAI 2024 | https://github.com/ibrahimethemhamamci/CT2Rep | 25,692 CT volumes trained |
| **IMG-T9 分期/分级** | BB-TEN (TNM from text) | Kefeli & Tatonetti, Nature Communications 2024 | https://github.com/tatonetti-lab/tnm-stage-classifier | AUC 0.815-0.942 (23 cancer types) |
| **IMG-T11 扫描质量评估** | MONAI DataAnalyzer | Cardoso et al., arXiv 2022 | https://github.com/Project-MONAI/MONAI | 伪影/噪声/层厚评估 |
| **IMG-T12 关键发现提醒** | TotalSegmentator + 阈值规则 | Wasserthal et al., Radiology:AI 2023 | https://github.com/wasserth/TotalSegmentator | 肾脏/肾上腺体积异常告警 |

### TXT 类任务

| 任务 | 工具名 | 论文 (作者, 期刊, 年份) | GitHub URL | 关键指标 |
|------|--------|------------------------|------------|----------|
| **TXT-T1 异常信号识别** | medspaCy | Eyre et al., AMIA 2021 | https://github.com/medspacy/medspacy | ConText negation; F1 ~0.85 |
| **TXT-T2 病灶信息抽取** | RadGraph-XL | Jain et al., ACL 2024 | https://github.com/Stanford-AIMI/radgraph | NER micro-F1 0.94 (MIMIC-CXR); 含 CT 标注 |
| **TXT-T4 分类标签抽取** | NegBio | Peng et al., EMNLP 2018 | https://github.com/ncbi-nlp/NegBio | 否定/不确定断言检测 |
| **TXT-T5 测量数据抽取** | llm_extractinator | Builtjes et al., JAMIA Open 2025 | https://github.com/DIAGNijmegen/llm_extractinator | Acc 93.7% (target lesion extraction) |
| **TXT-T7 随访文本对比** | llm_extractinator (Tracking Cancer Through Text) | van Driel et al., arXiv 2025 | https://github.com/DIAGNijmegen/llm_extractinator | RECIST attr acc >93% |
| **TXT-T8 报告生成** | RadFM | Wu et al., Nature Communications 2025 | https://github.com/chaoyi-wu/RadFM | 支持 3D CT; 多任务 VQA + 报告 |
| **TXT-T10 鉴别诊断推理** | RadFM | Wu et al., Nature Communications 2025 | https://github.com/chaoyi-wu/RadFM | 2D+3D 多任务鉴别诊断 |

### MM 类任务 (图文融合)

| 任务 | 工具名 | 论文 (作者, 期刊, 年份) | GitHub URL | 关键指标 |
|------|--------|------------------------|------------|----------|
| **MM-T4 分类 (影像+临床)** | Renal-Mass-AI | Wang et al., Nature Communications 2025 | https://github.com/shuowang26/renal-mass-ai | AUC 0.847 (multi-phase + clinical) |
| **MM-T7 随访 (影像+报告)** | LesionLocator | Rokuss et al., CVPR 2025 | https://github.com/MIC-DKFZ/LesionLocator | End-to-end 4D tracking |
| | detect-then-track | Zhou et al., J Digit Imaging Inform Med 2025 | https://github.com/alibool/detect-then-track | RECIST Acc 82.1% |
| **MM-T8 报告生成 (完整版)** | RadGPT | Bassi et al., ICCV 2025 | https://github.com/MrGiovanni/RadGPT | Kidney tumor Sens 92% (large) |
| **MM-T9 分期 (影像+临床)** | BB-TEN | Kefeli & Tatonetti, Nature Communications 2024 | https://github.com/tatonetti-lab/tnm-stage-classifier | AUC 0.815-0.942 |
| **MM-T10 鉴别诊断 (影像+病史)** | RadFM | Wu et al., Nature Communications 2025 | https://github.com/chaoyi-wu/RadFM | 支持 3D CT + text 融合 |
| **MM-T12 关键发现 (含临床背景)** | TotalSegmentator + RadGPT | Wasserthal 2023 / Bassi 2025 | https://github.com/wasserth/TotalSegmentator / https://github.com/MrGiovanni/RadGPT | 解剖分割 + 报告联合 |

---

## 二、胃肠道 (GI Tract) — 区域编号 10

### IMG 类任务

| 任务 | 工具名 | 论文 (作者, 期刊, 年份) | GitHub URL | 关键指标 |
|------|--------|------------------------|------------|----------|
| **IMG-T1 异常筛查** | DeepLesion (通用) | Yan et al., J Med Imaging 2018 | https://github.com/rsummers11/CADLab | Sens 0.84 @ 4 FP/vol |
| | CT-CLIP (zero-shot, 胸部为主) | Hamamci et al., arXiv 2024 | https://github.com/ibrahimethemhamamci/CT-CLIP | 18 pathology zero-shot |
| **IMG-T2 病灶检测/定位** | DeepLesion / MULAN | Yan et al., MICCAI 2019 | https://github.com/ke-yan/MULAN | 多器官病灶联合检测 |
| | ALIEN (胃癌) | Chen et al., Biomed Signal Process Control 2024 | https://github.com/ZHChen-294/ALIEN | 胃癌 CT 3D 分割 |
| **IMG-T3 病灶分割** | nnU-Net (通用框架) | Isensee et al., Nature Methods 2021 | https://github.com/MIC-DKFZ/nnUNet | SOTA on 多项 GI 分割 |
| | ULS23 (通用病灶分割) | de Grauw et al., MedIA 2025 | https://github.com/DIAGNijmegen/ULS23 | Dice 0.703; 含 colon/pancreas lesions |
| | U-SAM / CARE (直肠癌) | Zhang et al., Comms Medicine (Nature) 2025 | https://github.com/kanydao/U-SAM | Dice ~0.69 (rectal cancer seg) |
| | MedSAM (交互式) | Ma et al., Nature Communications 2024 | https://github.com/bowang-lab/MedSAM | Promptable 3D segmentation |
| **IMG-T4 分类/良恶性判断** | DL-CT-Colonography (结直肠息肉良恶性) | Wesp et al., European Radiology 2022 | https://github.com/pwesp/deep-learning-in-ct-colonography | AUC 0.91 (benign vs premalignant) |
| **IMG-T5 测量/定量分析** | pyradiomics | van Griethuysen et al., Cancer Research 2017 | https://github.com/AIM-Harvard/pyradiomics | ~1500 features; 体积/径线/形状 |
| **IMG-T6 解剖结构识别** | TotalSegmentator | Wasserthal et al., Radiology:AI 2023 | https://github.com/wasserth/TotalSegmentator | 含 stomach, duodenum, colon, small bowel 等 |
| | MONAI VISTA3D | MONAI Consortium, CVPR 2025 | https://github.com/Project-MONAI/VISTA | 127 类分割 |
| **IMG-T7 对比随访分析** | LesionLocator | Rokuss et al., CVPR 2025 | https://github.com/MIC-DKFZ/LesionLocator | 全身 4D tracking |
| | detect-then-track | Zhou et al., J Digit Imaging Inform Med 2025 | https://github.com/alibool/detect-then-track | RECIST Acc 82.1% |
| **IMG-T8 报告生成** | RadGPT | Bassi et al., ICCV 2025 | https://github.com/MrGiovanni/RadGPT | AbdomenAtlas 9262 vols; 胃肠适用 |
| | CT2Rep | Hamamci et al., MICCAI 2024 | https://github.com/ibrahimethemhamamci/CT2Rep | 3D CT 报告生成 |
| **IMG-T9 分期/分级** | BB-TEN (TNM NLP) | Kefeli & Tatonetti, Nature Communications 2024 | https://github.com/tatonetti-lab/tnm-stage-classifier | AUC 0.815-0.942; 含 colorectal |
| **IMG-T11 扫描质量评估** | MONAI DataAnalyzer | Cardoso et al., arXiv 2022 | https://github.com/Project-MONAI/MONAI | 伪影/噪声/层厚评估 |
| **IMG-T12 关键发现提醒** | TotalSegmentator + 阈值规则 | Wasserthal et al., Radiology:AI 2023 | https://github.com/wasserth/TotalSegmentator | 器官体积异常检出 |

### TXT 类任务

| 任务 | 工具名 | 论文 (作者, 期刊, 年份) | GitHub URL | 关键指标 |
|------|--------|------------------------|------------|----------|
| **TXT-T1 异常信号识别** | medspaCy | Eyre et al., AMIA 2021 | https://github.com/medspacy/medspacy | ConText negation; F1 ~0.85 |
| **TXT-T2 病灶信息抽取** | RadGraph-XL | Jain et al., ACL 2024 | https://github.com/Stanford-AIMI/radgraph | NER micro-F1 0.94; 含 abdomen/pelvis CT |
| **TXT-T4 分类标签抽取** | NegBio | Peng et al., EMNLP 2018 | https://github.com/ncbi-nlp/NegBio | 否定/不确定断言 |
| **TXT-T5 测量数据抽取** | llm_extractinator | Builtjes et al., JAMIA Open 2025 | https://github.com/DIAGNijmegen/llm_extractinator | Acc 93.7% |
| **TXT-T7 随访文本对比** | llm_extractinator (Tracking Cancer) | van Driel et al., arXiv 2025 | https://github.com/DIAGNijmegen/llm_extractinator | RECIST attr acc >93% |
| **TXT-T8 报告生成** | RadFM | Wu et al., Nature Communications 2025 | https://github.com/chaoyi-wu/RadFM | 多模态医学基础模型 |
| **TXT-T10 鉴别诊断推理** | RadFM | Wu et al., Nature Communications 2025 | https://github.com/chaoyi-wu/RadFM | 2D+3D 鉴别诊断 |

### MM 类任务 (图文融合)

| 任务 | 工具名 | 论文 (作者, 期刊, 年份) | GitHub URL | 关键指标 |
|------|--------|------------------------|------------|----------|
| **MM-T4 分类 (影像+临床)** | Multimodal-Medicine-AI (胃癌) | Chen et al., Signal Transduct Target Ther 2024 | https://github.com/czifan/Multimodal-Medicine-AI | 多模态胃癌疗效预测 |
| **MM-T7 随访 (影像+报告)** | LesionLocator | Rokuss et al., CVPR 2025 | https://github.com/MIC-DKFZ/LesionLocator | End-to-end 4D tracking |
| | detect-then-track | Zhou et al., J Digit Imaging Inform Med 2025 | https://github.com/alibool/detect-then-track | RECIST Acc 82.1% |
| **MM-T8 报告生成 (完整版)** | RadGPT | Bassi et al., ICCV 2025 | https://github.com/MrGiovanni/RadGPT | AbdomenAtlas; 含 GI 器官 |
| **MM-T9 分期 (影像+临床)** | BB-TEN | Kefeli & Tatonetti, Nature Communications 2024 | https://github.com/tatonetti-lab/tnm-stage-classifier | AUC 0.815-0.942 |
| **MM-T10 鉴别诊断 (影像+病史)** | RadFM | Wu et al., Nature Communications 2025 | https://github.com/chaoyi-wu/RadFM | 3D CT + text 鉴别诊断 |
| **MM-T12 关键发现 (含临床背景)** | TotalSegmentator + RadGPT | Wasserthal 2023 / Bassi 2025 | https://github.com/wasserth/TotalSegmentator / https://github.com/MrGiovanni/RadGPT | 联合管线 |

---

## 三、盆腔 (Pelvis) — 区域编号 11

### IMG 类任务

| 任务 | 工具名 | 论文 (作者, 期刊, 年份) | GitHub URL | 关键指标 |
|------|--------|------------------------|------------|----------|
| **IMG-T1 异常筛查** | DeepLesion (通用) | Yan et al., J Med Imaging 2018 | https://github.com/rsummers11/CADLab | Sens 0.84 @ 4 FP/vol |
| **IMG-T2 病灶检测/定位** | DeepLesion / MULAN | Yan et al., MICCAI 2019 | https://github.com/ke-yan/MULAN | 多器官联合检测+标签 |
| | FracSegNet (骨盆骨折) | Liu et al., Frontiers in Medicine 2025 | https://github.com/YzzLiu/FracSegNet | PENGWIN IoU 0.930 (top) |
| | OvSeg (卵巢癌) | Buddenkotte et al., Eur Radiol Exp 2023 | https://github.com/ThomasBudd/ovseg | DSC 0.71 (pelvic/ovarian) |
| **IMG-T3 病灶分割** | CTPelvic1K (骨盆骨) | Liu et al., IJCARS 2021 | https://github.com/MIRACLE-Center/CTPelvic1K | Dice 0.987 (metal-free pelvic bone) |
| | nnU-Net (通用框架) | Isensee et al., Nature Methods 2021 | https://github.com/MIC-DKFZ/nnUNet | 多项盆腔分割 SOTA |
| | OvSeg (卵巢癌) | Buddenkotte et al., Eur Radiol Exp 2023 | https://github.com/ThomasBudd/ovseg | DSC 0.71 (pelvic/ovarian) |
| | ULS23 (通用病灶分割) | de Grauw et al., MedIA 2025 | https://github.com/DIAGNijmegen/ULS23 | Dice 0.703 (全身) |
| | MedSAM (交互式) | Ma et al., Nature Communications 2024 | https://github.com/bowang-lab/MedSAM | Promptable 3D segmentation |
| **IMG-T4 分类/良恶性判断** | OvSeg (卵巢癌分割+分类) | Buddenkotte et al., Eur Radiol Exp 2023 | https://github.com/ThomasBudd/ovseg | 多部位 HGSOC 分割 |
| **IMG-T5 测量/定量分析** | pyradiomics | van Griethuysen et al., Cancer Research 2017 | https://github.com/AIM-Harvard/pyradiomics | ~1500 features; 体积/径线 |
| | TotalSegmentator (体积) | Wasserthal et al., Radiology:AI 2023 | https://github.com/wasserth/TotalSegmentator | 含 bladder, prostate, uterus 体积 |
| **IMG-T6 解剖结构识别** | TotalSegmentator | Wasserthal et al., Radiology:AI 2023 | https://github.com/wasserth/TotalSegmentator | 含 bladder, prostate, uterus, femur, sacrum 等 |
| | CTPelvic1K | Liu et al., IJCARS 2021 | https://github.com/MIRACLE-Center/CTPelvic1K | 骨盆 4 类 (lumbar/sacrum/hip L+R) |
| | MONAI VISTA3D | MONAI Consortium, CVPR 2025 | https://github.com/Project-MONAI/VISTA | 127 类 CT 分割 |
| **IMG-T7 对比随访分析** | LesionLocator | Rokuss et al., CVPR 2025 | https://github.com/MIC-DKFZ/LesionLocator | 全身 4D tracking |
| | detect-then-track | Zhou et al., J Digit Imaging Inform Med 2025 | https://github.com/alibool/detect-then-track | RECIST Acc 82.1% |
| **IMG-T8 报告生成** | RadGPT | Bassi et al., ICCV 2025 | https://github.com/MrGiovanni/RadGPT | AbdomenAtlas 含盆腔器官 |
| | CT2Rep | Hamamci et al., MICCAI 2024 | https://github.com/ibrahimethemhamamci/CT2Rep | 3D CT 报告 |
| **IMG-T9 分期/分级** | BB-TEN (TNM NLP) | Kefeli & Tatonetti, Nature Communications 2024 | https://github.com/tatonetti-lab/tnm-stage-classifier | AUC 0.815-0.942 |
| **IMG-T11 扫描质量评估** | MONAI DataAnalyzer | Cardoso et al., arXiv 2022 | https://github.com/Project-MONAI/MONAI | 伪影/噪声/层厚评估 |
| **IMG-T12 关键发现提醒** | TotalSegmentator + 阈值规则 | Wasserthal et al., Radiology:AI 2023 | https://github.com/wasserth/TotalSegmentator | 器官体积/骨折异常告警 |

### TXT 类任务

| 任务 | 工具名 | 论文 (作者, 期刊, 年份) | GitHub URL | 关键指标 |
|------|--------|------------------------|------------|----------|
| **TXT-T1 异常信号识别** | medspaCy | Eyre et al., AMIA 2021 | https://github.com/medspacy/medspacy | ConText negation; F1 ~0.85 |
| **TXT-T2 病灶信息抽取** | RadGraph-XL | Jain et al., ACL 2024 | https://github.com/Stanford-AIMI/radgraph | NER micro-F1 0.94; 含 abdomen/pelvis CT |
| **TXT-T4 分类标签抽取** | NegBio | Peng et al., EMNLP 2018 | https://github.com/ncbi-nlp/NegBio | 否定/不确定断言检测 |
| **TXT-T5 测量数据抽取** | llm_extractinator | Builtjes et al., JAMIA Open 2025 | https://github.com/DIAGNijmegen/llm_extractinator | Acc 93.7% |
| **TXT-T7 随访文本对比** | llm_extractinator (Tracking Cancer) | van Driel et al., arXiv 2025 | https://github.com/DIAGNijmegen/llm_extractinator | RECIST attr acc >93% |
| **TXT-T8 报告生成** | RadFM | Wu et al., Nature Communications 2025 | https://github.com/chaoyi-wu/RadFM | 多模态基础模型 |
| **TXT-T10 鉴别诊断推理** | RadFM | Wu et al., Nature Communications 2025 | https://github.com/chaoyi-wu/RadFM | 2D+3D 鉴别诊断 |

### MM 类任务 (图文融合)

| 任务 | 工具名 | 论文 (作者, 期刊, 年份) | GitHub URL | 关键指标 |
|------|--------|------------------------|------------|----------|
| **MM-T4 分类 (影像+临床)** | OvSeg (卵巢癌, 可融合临床) | Buddenkotte et al., Eur Radiol Exp 2023 | https://github.com/ThomasBudd/ovseg | DSC 0.71 (pelvic/ovarian) |
| **MM-T7 随访 (影像+报告)** | LesionLocator | Rokuss et al., CVPR 2025 | https://github.com/MIC-DKFZ/LesionLocator | End-to-end 4D tracking |
| | detect-then-track | Zhou et al., J Digit Imaging Inform Med 2025 | https://github.com/alibool/detect-then-track | RECIST Acc 82.1% |
| **MM-T8 报告生成 (完整版)** | RadGPT | Bassi et al., ICCV 2025 | https://github.com/MrGiovanni/RadGPT | 含盆腔器官报告 |
| **MM-T9 分期 (影像+临床)** | BB-TEN | Kefeli & Tatonetti, Nature Communications 2024 | https://github.com/tatonetti-lab/tnm-stage-classifier | AUC 0.815-0.942; 含 cervical/ovarian/bladder |
| **MM-T10 鉴别诊断 (影像+病史)** | RadFM | Wu et al., Nature Communications 2025 | https://github.com/chaoyi-wu/RadFM | 3D CT + text 鉴别诊断 |
| **MM-T12 关键发现 (含临床背景)** | TotalSegmentator + RadGPT | Wasserthal 2023 / Bassi 2025 | https://github.com/wasserth/TotalSegmentator / https://github.com/MrGiovanni/RadGPT | 联合管线 |

---

## 四、补充说明

### 4.1 跨区域通用工具清单

以下工具适用于上述三个区域的多项任务:

| 工具 | 覆盖任务 | 论文 | GitHub |
|------|---------|------|--------|
| **TotalSegmentator** | T6 解剖分割, T5 体积, T12 告警 | Wasserthal et al., Radiology:AI 2023 | https://github.com/wasserth/TotalSegmentator |
| **nnU-Net** | T3 分割 (通用框架) | Isensee et al., Nature Methods 2021 | https://github.com/MIC-DKFZ/nnUNet |
| **MedSAM** | T3 交互式分割 | Ma et al., Nature Communications 2024 | https://github.com/bowang-lab/MedSAM |
| **ULS23** | T2 检测, T3 分割 (通用病灶) | de Grauw et al., MedIA 2025 | https://github.com/DIAGNijmegen/ULS23 |
| **DeepLesion/CADLab** | T1 筛查, T2 检测 | Yan et al., J Med Imaging 2018 | https://github.com/rsummers11/CADLab |
| **pyradiomics** | T5 定量测量 | van Griethuysen et al., Cancer Research 2017 | https://github.com/AIM-Harvard/pyradiomics |
| **LesionLocator** | T7 随访追踪 | Rokuss et al., CVPR 2025 | https://github.com/MIC-DKFZ/LesionLocator |
| **RadGPT** | T8 报告生成 | Bassi et al., ICCV 2025 | https://github.com/MrGiovanni/RadGPT |
| **RadFM** | T8 报告, T10 鉴别诊断 | Wu et al., Nature Communications 2025 | https://github.com/chaoyi-wu/RadFM |
| **BB-TEN** | T9 分期 | Kefeli & Tatonetti, Nature Communications 2024 | https://github.com/tatonetti-lab/tnm-stage-classifier |
| **medspaCy** | TXT-T1 异常信号 | Eyre et al., AMIA 2021 | https://github.com/medspacy/medspacy |
| **RadGraph-XL** | TXT-T2 NER | Jain et al., ACL 2024 | https://github.com/Stanford-AIMI/radgraph |
| **llm_extractinator** | TXT-T5 测量, TXT-T7 随访 | Builtjes et al., JAMIA Open 2025 | https://github.com/DIAGNijmegen/llm_extractinator |

### 4.2 注意: AppendiXNet 不满足入选条件

AppendiXNet (Rajpurkar et al., Scientific Reports 2020) 是一个用于 CT 阑尾炎诊断的 3D CNN 模型 (AUC 0.810), 但**未找到公开 GitHub 仓库**, 因此未纳入本调研。

### 4.3 区域特有工具亮点

| 区域 | 特有工具 | 特色 |
|------|---------|------|
| 肾脏/肾上腺 | KiTS23, Renal-Mass-AI, NHS Adrenal | 肾肿瘤分割 Challenge + 良恶性分类 + 肾上腺筛查 |
| 胃肠道 | ALIEN, U-SAM/CARE, DL-CT-Colonography | 胃癌 3D 分割 + 直肠癌分割 + 结直肠息肉分类 |
| 盆腔 | CTPelvic1K, FracSegNet, OvSeg | 骨盆骨分割 + 骨折检测 + 卵巢癌多部位分割 |
