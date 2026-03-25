# CT-Agent MCP 工具包设计

> 版本: 0.1-draft | 日期: 2025-03-25
>
> 本文档定义 CT 智能体 benchmark 所需的全部 MCP 工具。
> 智能体在执行 336 个评测任务（14 部位 × 3 模态 × 12 任务类型）时，
> 需要从本工具包中**自主选择并编排**正确的工具调用链。

---

## 1. 工具体系总览

### 1.1 设计原则

| 原则 | 说明 |
|------|------|
| **原子化** | 每个工具只做一件事，复杂任务由智能体编排多个工具完成 |
| **无状态** | 工具本身不保存中间状态，所有中间结果通过输入/输出显式传递 |
| **标准 MCP** | 每个工具符合 MCP Tool schema（name / description / inputSchema / outputSchema） |
| **可测评** | 每个工具的输入输出可被 benchmark harness 拦截和评分 |
| **含干扰项** | 工具包中故意包含"看似相关但不该被选用"的干扰工具，测试智能体的工具选择能力 |

### 1.2 分层架构

工具按功能分为 **7 层**，每层内部的工具互不依赖，跨层通过数据流串联：

```
┌─────────────────────────────────────────────────────────┐
│  L7  输出层        报告生成 · FHIR导出 · 关键发现告警      │
├─────────────────────────────────────────────────────────┤
│  L6  推理层        分类判断 · 分期分级 · 鉴别诊断          │
├─────────────────────────────────────────────────────────┤
│  L5  融合层        跨模态证据聚合 · 模态置信度归因          │
├─────────────────────────────────────────────────────────┤
│  L4  定量层        三径测量 · 体积计算 · CT值统计 · 变化率   │
├─────────────────────────────────────────────────────────┤
│  L3  感知层        异常筛查 · 病灶检测 · 病灶分割 · 解剖分割 │
├─────────────────────────────────────────────────────────┤
│  L2  文本层        NER抽取 · 关系抽取 · 数值抽取 · 时序对齐  │
├─────────────────────────────────────────────────────────┤
│  L1  预处理层      DICOM解析 · 窗宽窗位 · 配准 · 质量评估    │
└─────────────────────────────────────────────────────────┘
```

### 1.3 工具清单速览

共 **28 个正式工具 + 6 个干扰工具 = 34 个工具**。

| 层 | ID | 工具名 | 一句话描述 | 覆盖任务 |
|----|-----|--------|-----------|---------|
| L1 | P01 | `dicom_loader` | 加载 DICOM 序列为标准化 3D 体积 | 所有 IMG/MM |
| L1 | P02 | `window_level` | 应用窗宽窗位变换 | 所有 IMG/MM |
| L1 | P03 | `image_registration` | 刚性/形变配准两个时间点的 CT 序列 | T7 |
| L1 | P04 | `scan_quality_check` | 评估扫描质量（伪影/噪声/层厚/对比剂时相） | T11 |
| L3 | V01 | `abnormality_screening` | 全局二分类：正常 vs 异常 | T1 (IMG) |
| L3 | V02 | `lesion_detection` | 检测所有可疑病灶，输出 3D bbox | T2 (IMG) |
| L3 | V03 | `lesion_segmentation` | 对病灶进行体素级 3D 分割 | T3 (IMG) |
| L3 | V04 | `anatomy_segmentation` | 多类别解剖结构分割 | T6 (IMG) |
| L2 | T01 | `clinical_signal_extractor` | 从病历文本中提取异常临床信号 | T1 (TXT) |
| L2 | T02 | `report_ner` | 从 CT 报告中抽取病灶实体（位置/大小/形态/密度） | T2 (TXT) |
| L2 | T03 | `classification_label_extractor` | 从文本中抽取分类标签及证据 | T4 (TXT) |
| L2 | T04 | `measurement_extractor` | 从报告中抽取测量数值三元组 | T5 (TXT) |
| L2 | T05 | `temporal_report_aligner` | 多份时序报告对齐与变化抽取 | T7 (TXT) |
| L4 | Q01 | `lesion_measurement` | 三径测量 + 体积 + CT 值统计 | T5 (IMG) |
| L4 | Q02 | `volume_change_calculator` | 计算两个时间点的体积/径线变化率 | T7 (IMG/MM) |
| L4 | Q03 | `recist_evaluator` | 按 RECIST 1.1 标准评估治疗响应 | T7 (IMG/MM) |
| L5 | F01 | `multimodal_evidence_fusion` | 聚合影像特征与文本证据，输出融合置信度 | T4/T9/T10/T12 (MM) |
| L5 | F02 | `modality_attribution` | 分析各模态对最终结论的贡献度 | 所有 MM |
| L6 | R01 | `malignancy_classifier` | 良恶性及亚型分类 | T4 (IMG/MM) |
| L6 | R02 | `staging_engine` | 按 TNM/Lung-RADS/LI-RADS 等分期 | T9 (IMG/MM) |
| L6 | R03 | `differential_diagnosis` | 生成鉴别诊断列表及支持/反对证据 | T10 (TXT/MM) |
| L7 | O01 | `report_generator` | 生成四段式结构化影像报告 | T8 (IMG/TXT/MM) |
| L7 | O02 | `fhir_exporter` | 将结构化报告导出为 HL7 FHIR 格式 | T8 |
| L7 | O03 | `critical_finding_alert` | 识别紧急/偶发关键发现并分级告警 | T12 (IMG/MM) |
| L7 | O04 | `report_quality_scorer` | 对生成的报告进行质量自评 | T8 辅助 |
| — | U01 | `medical_knowledge_lookup` | 查询医学知识库（分期标准/指南/鉴别要点） | T9/T10 辅助 |
| — | U02 | `body_region_classifier` | 自动识别 CT 扫描覆盖的身体部位 | 预处理辅助 |
| — | U03 | `dicom_metadata_reader` | 读取 DICOM 元数据（患者信息/扫描参数） | 预处理辅助 |

**干扰工具（不应被选用，用于测试工具选择能力）：**

| ID | 工具名 | 伪描述（故意误导） | 为什么是干扰 |
|----|--------|------------------|-------------|
| D01 | `mri_lesion_detection` | 在 MRI 序列中检测病灶 | 模态错误：本系统只处理 CT |
| D02 | `xray_abnormality_screen` | 对 X 光片进行异常筛查 | 模态错误：不是 CT |
| D03 | `pet_ct_fusion` | PET-CT 代谢与形态融合分析 | 模态错误：没有 PET 数据 |
| D04 | `lesion_detection_2d` | 在单张 2D 切片上检测病灶 | 降维错误：应该用 3D 检测 |
| D05 | `deprecated_segmentation_v1` | [已废弃] 旧版分割工具 | 版本错误：已标记废弃 |
| D06 | `ct_reconstruction` | 从稀疏视角正弦图重建 CT 图像 | 任务错误：重建不属于诊断流程 |

---

## 2. 工具详细 Schema 定义

> 每个工具遵循 MCP Tool 协议，定义 `name` / `description` / `inputSchema` / `outputSchema`。
> Schema 使用 JSON Schema draft-2020-12。

---

### 2.1 L1 预处理层

#### P01 `dicom_loader`

加载 DICOM 序列，执行排序、去重、像素归一化，输出标准化 3D 体积数组。

```jsonc
{
  "name": "dicom_loader",
  "description": "Load a DICOM series from a directory path or study UID. Returns a normalized 3D volume array with standardized orientation (LPS+), voxel spacing, and HU calibration.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "source": {
        "type": "string",
        "description": "DICOM 数据源。可以是目录路径或 StudyInstanceUID"
      },
      "series_uid": {
        "type": "string",
        "description": "可选。指定 SeriesInstanceUID，当一个 Study 包含多个序列时用于选择"
      },
      "target_spacing": {
        "type": "array",
        "items": { "type": "number" },
        "minItems": 3,
        "maxItems": 3,
        "description": "可选。目标体素间距 [x, y, z] mm，触发重采样。默认保留原始间距"
      }
    },
    "required": ["source"]
  },
  "outputSchema": {
    "type": "object",
    "properties": {
      "volume_id": {
        "type": "string",
        "description": "生成的体积 ID，后续工具通过此 ID 引用"
      },
      "shape": {
        "type": "array",
        "items": { "type": "integer" },
        "description": "体积尺寸 [D, H, W]"
      },
      "spacing": {
        "type": "array",
        "items": { "type": "number" },
        "description": "体素间距 [x, y, z] mm"
      },
      "orientation": {
        "type": "string",
        "enum": ["LPS"],
        "description": "标准化方向"
      },
      "hu_range": {
        "type": "array",
        "items": { "type": "number" },
        "minItems": 2,
        "maxItems": 2,
        "description": "HU 值范围 [min, max]"
      },
      "metadata": {
        "type": "object",
        "description": "关键 DICOM 元信息子集（患者ID/检查日期/层厚/对比剂）"
      }
    },
    "required": ["volume_id", "shape", "spacing", "orientation", "hu_range"]
  }
}
```

---

#### P02 `window_level`

对 3D 体积应用窗宽窗位变换，可使用预设或自定义参数。

```jsonc
{
  "name": "window_level",
  "description": "Apply window/level (WW/WL) transformation to a CT volume. Supports preset names (lung, mediastinum, bone, liver, brain, subdural) or custom WW/WL values.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "volume_id": {
        "type": "string",
        "description": "输入体积 ID（来自 dicom_loader 输出）"
      },
      "preset": {
        "type": "string",
        "enum": ["lung", "mediastinum", "bone", "liver", "brain", "subdural", "soft_tissue", "stroke"],
        "description": "预设窗宽窗位名称。与 custom_ww/custom_wl 二选一"
      },
      "custom_ww": {
        "type": "number",
        "description": "自定义窗宽。需与 custom_wl 同时提供"
      },
      "custom_wl": {
        "type": "number",
        "description": "自定义窗位。需与 custom_ww 同时提供"
      }
    },
    "required": ["volume_id"],
    "oneOf": [
      { "required": ["preset"] },
      { "required": ["custom_ww", "custom_wl"] }
    ]
  },
  "outputSchema": {
    "type": "object",
    "properties": {
      "volume_id": {
        "type": "string",
        "description": "变换后的体积 ID（新 ID，不覆盖原始体积）"
      },
      "applied_ww": { "type": "number" },
      "applied_wl": { "type": "number" }
    },
    "required": ["volume_id", "applied_ww", "applied_wl"]
  }
}
```

---

#### P03 `image_registration`

配准两个时间点的 CT 序列，用于纵向对比（T7 变化追踪任务）。

```jsonc
{
  "name": "image_registration",
  "description": "Register two CT volumes (baseline and follow-up) using rigid or deformable registration. Returns the aligned follow-up volume and the transformation field.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "fixed_volume_id": {
        "type": "string",
        "description": "基准时间点（fixed）体积 ID"
      },
      "moving_volume_id": {
        "type": "string",
        "description": "随访时间点（moving）体积 ID，将被配准到 fixed 空间"
      },
      "method": {
        "type": "string",
        "enum": ["rigid", "affine", "deformable"],
        "default": "affine",
        "description": "配准方法"
      },
      "body_region": {
        "type": "string",
        "description": "可选。提示配准器关注的身体区域，提高配准精度"
      }
    },
    "required": ["fixed_volume_id", "moving_volume_id"]
  },
  "outputSchema": {
    "type": "object",
    "properties": {
      "aligned_volume_id": {
        "type": "string",
        "description": "配准后的 moving 体积 ID（在 fixed 空间中）"
      },
      "transform_id": {
        "type": "string",
        "description": "变换场 ID，可用于将 ROI/mask 同步变换"
      },
      "registration_quality": {
        "type": "object",
        "properties": {
          "dice_overlap": { "type": "number", "description": "骨骼/身体轮廓 Dice 重叠度" },
          "tre_mm": { "type": "number", "description": "目标配准误差（mm）" }
        }
      }
    },
    "required": ["aligned_volume_id", "transform_id", "registration_quality"]
  }
}
```

---

#### P04 `scan_quality_check`

评估 CT 扫描的技术质量，输出质量报告和可用性判断。

```jsonc
{
  "name": "scan_quality_check",
  "description": "Assess technical quality of a CT scan including artifacts, noise level, slice thickness, contrast phase, and completeness. Returns a quality report with pass/fail verdict.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "volume_id": {
        "type": "string",
        "description": "待评估的体积 ID"
      },
      "expected_phase": {
        "type": "string",
        "enum": ["non_contrast", "arterial", "portal_venous", "delayed", "any"],
        "default": "any",
        "description": "期望的对比剂时相，用于验证是否匹配"
      }
    },
    "required": ["volume_id"]
  },
  "outputSchema": {
    "type": "object",
    "properties": {
      "overall_verdict": {
        "type": "string",
        "enum": ["pass", "warn", "fail"],
        "description": "总体质量判定"
      },
      "checks": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "item": {
              "type": "string",
              "enum": ["motion_artifact", "metal_artifact", "noise_level", "slice_thickness", "contrast_phase", "coverage_completeness", "reconstruction_kernel"]
            },
            "status": { "type": "string", "enum": ["pass", "warn", "fail"] },
            "detail": { "type": "string" }
          }
        },
        "description": "逐项质量检查结果"
      },
      "detected_phase": {
        "type": "string",
        "enum": ["non_contrast", "arterial", "portal_venous", "delayed", "unknown"],
        "description": "检测到的实际对比剂时相"
      },
      "noise_hu_std": {
        "type": "number",
        "description": "背景区域 HU 标准差（噪声指标）"
      }
    },
    "required": ["overall_verdict", "checks", "detected_phase"]
  }
}
```

---

*L1 预处理层完。下一批：L2 文本层。*
