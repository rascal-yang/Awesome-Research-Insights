<a id="top"></a>

<p align="center">
  <img src="assets/banner.svg" width="100%" alt="论文、技术与迁移应用">
</p>

<h1 align="center">Awesome Research Insights</h1>

<p align="center"><strong>从不同领域的论文中，提取值得借鉴的技术。</strong></p>

<p align="center">
  <strong>简体中文</strong> · <a href="README.en.md">English</a> · <a href="CONTRIBUTING.md">参与贡献</a>
</p>

跨领域科研技术灵感库，收录论文中可迁移的模块、损失、优化方法与训练策略。

**最新收录 · 2026-11-17** · [ICML 2026 · 303 / 6,552 篇已有 Insight](conferences/icml-2026/README.md)

**最近核查 · 2026-11-15** · 首批条目及交叉链接

**目录**

- [全部论文领域](#papers-by-domain)
- [ICML 2026 论文 Insight](conferences/icml-2026/README.md)
- [大语言模型](#large-language-models)
- [计算机视觉](#computer-vision)
- [自然语言处理](#natural-language-processing)
- [强化学习](#reinforcement-learning)
- [机器人学](#robotics)
- [多模态学习](#multimodal-learning)
- [机器学习基础与统计](#ml-foundations)
- [图学习与推荐](#graph-and-recommendation)
- [科学机器学习](#scientific-ml)
- [跨领域技术索引](#insights-by-technical-category)
- [关注会议与收录节奏](#conference-sources)
- [最近更新](#recent-updates)
- [参与贡献](#contributing)

<a id="papers-by-domain"></a>

## 全部论文领域

| 领域 | 收录论文 | 收录范围 |
| :--- | ---: | :--- |
| [大语言模型](#large-language-models) | 80 | 语言模型、工具调用与智能体。 |
| [计算机视觉](#computer-vision) | 16 | 视觉识别、表征学习与生成。 |
| [自然语言处理](#natural-language-processing) | 11 | 语言、语音、检索与文本处理。 |
| [强化学习](#reinforcement-learning) | 28 | 交互决策、奖励、策略学习与博弈。 |
| [机器人学](#robotics) | 9 | 机器人感知、策略学习、规划与控制。 |
| [多模态学习](#multimodal-learning) | 14 | 跨视觉、文本、音频等模态的学习与推理。 |
| [机器学习基础与统计](#ml-foundations) | 101 | 通用学习方法、优化、学习理论与统计推断。 |
| [图学习与推荐](#graph-and-recommendation) | 17 | 图模型、知识图谱与推荐系统。 |
| [科学机器学习](#scientific-ml) | 28 | 物理、医学、生物与工程中的机器学习。 |

**共 304 篇论文、305 条 Insight。** 每篇论文按主要研究问题计入一个领域。

<a id="large-language-models"></a>

## 大语言模型

[全部论文 (80)](papers/llm.md)

[模型架构 (1)](papers/llm.md#by-architecture) · [损失函数 (2)](papers/llm.md#by-loss-functions) · [优化 (1)](papers/llm.md#by-optimization) · [强化学习方法 (10)](papers/llm.md#by-reinforcement-learning) · [训练策略 (9)](papers/llm.md#by-training-strategies) · [数据策略 (7)](papers/llm.md#by-data-strategies) · [推理策略 (11)](papers/llm.md#by-inference) · [表征学习 (1)](papers/llm.md#by-representation-learning) · [评测与诊断 (35)](papers/llm.md#by-evaluation) · [理论与统计 (3)](papers/llm.md#by-theory-statistics)

<a id="computer-vision"></a>

## 计算机视觉

[全部论文 (16)](papers/computer-vision.md)

[模型架构 (3)](papers/computer-vision.md#by-architecture) · [模块 (2)](papers/computer-vision.md#by-modules) · [损失函数 (1)](papers/computer-vision.md#by-loss-functions) · [强化学习方法 (1)](papers/computer-vision.md#by-reinforcement-learning) · [训练策略 (1)](papers/computer-vision.md#by-training-strategies) · [推理策略 (3)](papers/computer-vision.md#by-inference) · [表征学习 (1)](papers/computer-vision.md#by-representation-learning) · [评测与诊断 (4)](papers/computer-vision.md#by-evaluation)

<a id="computer-vision-modules"></a>

### 模块

| Insight | 一句话概括 | 来源 |
| :--- | :--- | :--- |
| [**只加宽学生模型的蒸馏接口**](insights/modules.md#widen-the-student-distillation-interface) | 做特征蒸馏时，只加宽学生模型的特征接口或最后一个 Transformer 块。 | [Lift / WideLast](papers/computer-vision.md#vision-model-distillation) |

<a id="natural-language-processing"></a>

## 自然语言处理

[全部论文 (11)](papers/nlp.md)

[模块 (1)](papers/nlp.md#by-modules) · [数据策略 (1)](papers/nlp.md#by-data-strategies) · [推理策略 (3)](papers/nlp.md#by-inference) · [评测与诊断 (2)](papers/nlp.md#by-evaluation) · [理论与统计 (4)](papers/nlp.md#by-theory-statistics)

<a id="reinforcement-learning"></a>

## 强化学习

[全部论文 (28)](papers/reinforcement-learning.md)

[模型架构 (1)](papers/reinforcement-learning.md#by-architecture) · [强化学习方法 (14)](papers/reinforcement-learning.md#by-reinforcement-learning) · [数据策略 (1)](papers/reinforcement-learning.md#by-data-strategies) · [表征学习 (1)](papers/reinforcement-learning.md#by-representation-learning) · [评测与诊断 (1)](papers/reinforcement-learning.md#by-evaluation) · [理论与统计 (10)](papers/reinforcement-learning.md#by-theory-statistics)

<a id="reward-and-advantage-estimation"></a>

### 奖励与优势估计

| Insight | 一句话概括 | 来源 |
| :--- | :--- | :--- |
| [**多奖励先分别归一化再聚合**](insights/reinforcement-learning.md#normalize-each-reward-before-aggregation) | 先在轨迹组内归一化各项奖励，再合并优势。 | [GDPO](papers/reinforcement-learning.md#group-relative-policy-optimization) |

<a id="robotics"></a>

## 机器人学

[全部论文 (9)](papers/robotics.md)

[模型架构 (1)](papers/robotics.md#by-architecture) · [模块 (1)](papers/robotics.md#by-modules) · [损失函数 (3)](papers/robotics.md#by-loss-functions) · [强化学习方法 (1)](papers/robotics.md#by-reinforcement-learning) · [推理策略 (3)](papers/robotics.md#by-inference) · [评测与诊断 (1)](papers/robotics.md#by-evaluation)

<a id="loss-functions"></a>

### 损失函数

| Insight | 一句话概括 | 来源 |
| :--- | :--- | :--- |
| [**用目标区域重建做辅助监督**](insights/loss-functions.md#target-region-reconstruction-as-auxiliary-supervision) | 用目标物体裁剪区域的潜变量重建，给策略表征增加训练监督。 | [ReconVLA](papers/robotics.md#vision-language-action-models) |
| [**用潜动作监督动作专家的中间层**](insights/loss-functions.md#align-action-features-with-latent-actions) | 用前后帧提取的潜动作监督动作模型的中间层。 | [LARA](papers/robotics.md#vision-language-action-models) |

<a id="modules"></a>

### 模块

| Insight | 一句话概括 | 来源 |
| :--- | :--- | :--- |
| [**用指令前缀让视觉表征感知任务**](insights/modules.md#instruction-prefixes-for-causal-visual-grounding) | 把指令 token 放在图像 token 前，使视觉隐藏状态能通过因果注意力读取任务信息。 | [ReconVLA](papers/robotics.md#vision-language-action-models) |

<a id="multimodal-learning"></a>

## 多模态学习

[全部论文 (14)](papers/multimodal.md)

[模型架构 (1)](papers/multimodal.md#by-architecture) · [模块 (1)](papers/multimodal.md#by-modules) · [训练策略 (2)](papers/multimodal.md#by-training-strategies) · [数据策略 (2)](papers/multimodal.md#by-data-strategies) · [推理策略 (7)](papers/multimodal.md#by-inference) · [评测与诊断 (1)](papers/multimodal.md#by-evaluation)

<a id="ml-foundations"></a>

## 机器学习基础与统计

[全部论文 (101)](papers/ml-foundations.md)

[模型架构 (5)](papers/ml-foundations.md#by-architecture) · [模块 (6)](papers/ml-foundations.md#by-modules) · [损失函数 (3)](papers/ml-foundations.md#by-loss-functions) · [优化 (26)](papers/ml-foundations.md#by-optimization) · [训练策略 (5)](papers/ml-foundations.md#by-training-strategies) · [数据策略 (1)](papers/ml-foundations.md#by-data-strategies) · [推理策略 (2)](papers/ml-foundations.md#by-inference) · [表征学习 (5)](papers/ml-foundations.md#by-representation-learning) · [评测与诊断 (8)](papers/ml-foundations.md#by-evaluation) · [理论与统计 (40)](papers/ml-foundations.md#by-theory-statistics)

<a id="graph-and-recommendation"></a>

## 图学习与推荐

[全部论文 (17)](papers/graph-and-recommendation.md)

[模型架构 (1)](papers/graph-and-recommendation.md#by-architecture) · [模块 (2)](papers/graph-and-recommendation.md#by-modules) · [优化 (1)](papers/graph-and-recommendation.md#by-optimization) · [强化学习方法 (2)](papers/graph-and-recommendation.md#by-reinforcement-learning) · [训练策略 (1)](papers/graph-and-recommendation.md#by-training-strategies) · [数据策略 (1)](papers/graph-and-recommendation.md#by-data-strategies) · [推理策略 (2)](papers/graph-and-recommendation.md#by-inference) · [表征学习 (1)](papers/graph-and-recommendation.md#by-representation-learning) · [评测与诊断 (2)](papers/graph-and-recommendation.md#by-evaluation) · [理论与统计 (4)](papers/graph-and-recommendation.md#by-theory-statistics)

<a id="scientific-ml"></a>

## 科学机器学习

[全部论文 (28)](papers/scientific-ml.md)

[模型架构 (8)](papers/scientific-ml.md#by-architecture) · [模块 (1)](papers/scientific-ml.md#by-modules) · [损失函数 (2)](papers/scientific-ml.md#by-loss-functions) · [强化学习方法 (1)](papers/scientific-ml.md#by-reinforcement-learning) · [推理策略 (3)](papers/scientific-ml.md#by-inference) · [表征学习 (4)](papers/scientific-ml.md#by-representation-learning) · [评测与诊断 (6)](papers/scientific-ml.md#by-evaluation) · [理论与统计 (3)](papers/scientific-ml.md#by-theory-statistics)

<a id="insights-by-technical-category"></a>

## 跨领域技术索引

按技术类型查找不同领域的条目。

| 技术分类 | Insight 数 | 收录范围 |
| :--- | ---: | :--- |
| <a id="architectures"></a>[模型架构](insights/architecture.md) | 21 | 整体架构与信息流。 |
| [模块](insights/modules.md) | 14 | 局部组件、连接与参数化。 |
| [损失函数](insights/loss-functions.md) | 11 | 训练目标、辅助监督与正则化。 |
| <a id="optimization"></a>[优化](insights/optimization.md) | 28 | 梯度更新、求解器与优化过程。 |
| <a id="reinforcement-learning-methods"></a>[强化学习方法](insights/reinforcement-learning.md) | 29 | 奖励、探索、信用分配与策略更新。 |
| <a id="training-strategies"></a>[训练策略](insights/training-strategies.md) | 18 | 训练日程、微调、蒸馏与迁移。 |
| <a id="data-strategies"></a>[数据策略](insights/data-strategies.md) | 13 | 数据构造、筛选、标注与采样。 |
| <a id="inference-strategies"></a>[推理策略](insights/inference.md) | 34 | 解码、搜索、推理时适配与高效执行。 |
| [表征学习](insights/representation-learning.md) | 13 | 表征提取、对齐、迁移与解耦。 |
| [评测与诊断](insights/evaluation.md) | 60 | 基准、评测协议、消融与失效诊断。 |
| [理论与统计](insights/theory-statistics.md) | 64 | 学习保证、反例、估计与统计检验。 |

<p align="right"><a href="#top">↑ 回到顶部</a></p>

<a id="conference-sources"></a>

## 关注会议与收录节奏

首批从 **2025–2026 年 CCF A 类会议的主会论文**中筛选，年份按会议届次计算。以下专题来源也会按研究主题查阅。

| 来源 | 会议 | 优先关注 |
| :--- | :--- | :--- |
| CCF A 类 · 通用机器学习与人工智能 | ICML、NeurIPS、ICLR、AAAI | 损失函数、表征学习、优化、训练策略与强化学习 |
| CCF A 类 · 计算机视觉 | CVPR、ICCV | 视觉监督、视频与时序表征、三维感知 |
| CCF A 类 · 自然语言处理 | ACL | 指令理解、推理与语言表征 |
| 机器人学习与系统 | CoRL、RSS | 策略学习、模仿学习、规划与机器人操作 |
| 专题补充 | EMNLP、ECCV、ICRA、IROS | 语言与多模态技术、感知与控制、接触及真机执行 |

会议公布官方主会录用名单或论文集后，按批次更新。ICML 2026 按论文集逐篇分析。

**收录标准。** 一篇论文只要有一条能独立讲清、能在原文中核实的技术洞见，就足以收录。记录它在什么条件下成立，以及实验、定理或反例支持什么结论。迁移场景可选。

<a id="recent-updates"></a>

## 最近更新

- **2026-11-17** · 按研究领域和技术类型整理 304 篇论文与 305 条 Insight。

- **2026-11-17** · 新增 ICML 2026 第 161–300 篇的 Insight。[会议索引](conferences/icml-2026/README.md)

- **2026-11-17** · 新增 ICML 2026 逐篇目录，第 1–160 篇已有 Insight，另附此前专题收录的 3 篇。 [ICML 2026 论文 Insight](conferences/icml-2026/README.md)

<a id="icml-2026-first-batch"></a>

- **2026-11-15** · 新增 3 篇论文、3 条 Insight，来自 [ICML 2026](https://proceedings.mlr.press/v306/)。 [用潜动作监督动作专家的中间层](insights/loss-functions.md#align-action-features-with-latent-actions) · [只加宽学生模型的蒸馏接口](insights/modules.md#widen-the-student-distillation-interface) · [多奖励先分别归一化再聚合](insights/reinforcement-learning.md#normalize-each-reward-before-aggregation)

- **2026-11-15** · 收录 ReconVLA（AAAI 2026）的两条 Insight。 [用目标区域重建做辅助监督](insights/loss-functions.md#target-region-reconstruction-as-auxiliary-supervision) · [用指令前缀让视觉表征感知任务](insights/modules.md#instruction-prefixes-for-causal-visual-grounding)

<a id="contributing"></a>

## 参与贡献

欢迎补充论文、提取可复用技术或修正已有条目。见 [贡献指南](CONTRIBUTING.md)。

[MIT License](LICENSE)
