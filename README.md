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

**最新收录 · 2026-11-15** · [ReconVLA 的两条 Insight](#recent-updates)

**最近核查 · 2026-11-15** · 首批条目及交叉链接

**目录**

- [按论文领域浏览](#papers-by-domain)
  - [机器人学](#robotics)
- [按技术类型浏览](#insights-by-technical-category)
  - [损失函数](#loss-functions)
  - [模块](#modules)
- [关注会议与收录节奏](#conference-sources)
- [最近更新](#recent-updates)
- [参与贡献](#contributing)

<a id="papers-by-domain"></a>

## 按论文领域浏览

按论文的主要研究领域查找，再跳到对应的技术条目。

<a id="robotics"></a>

### 机器人学

| 论文 | 首次公开 / 发表 | 可借鉴的技术 | 资源 |
| :--- | :--- | :--- | :--- |
| [**ReconVLA**](papers/robotics.md#vision-language-action-models)<br><sub>Song et al.</sub> | 2025-08-14<br><sub>[AAAI 2026](https://ojs.aaai.org/index.php/AAAI/article/download/38921/42883)</sub> | [用目标区域重建做辅助监督](insights/loss-functions.md#target-region-reconstruction-as-auxiliary-supervision)<br>[用指令前缀让视觉表征感知任务](insights/modules.md#instruction-prefixes-for-causal-visual-grounding) | [论文](https://arxiv.org/abs/2508.10333) · [项目](https://zionchow.github.io/ReconVLA/) · [代码](https://github.com/OpenHelix-Team/ReconVLA) |

**全部论文领域**

| 领域 | 收录论文 | 收录范围 |
| :--- | ---: | :--- |
| <a id="large-language-models"></a>[大语言模型](papers/llm.md) | 0 | 语言建模、后训练与推理。 |
| <a id="computer-vision"></a>[计算机视觉](papers/computer-vision.md) | 0 | 视觉识别、表征学习与生成。 |
| <a id="natural-language-processing"></a>[自然语言处理](papers/nlp.md) | 0 | 语言处理、检索与结构化预测。 |
| <a id="reinforcement-learning"></a>[强化学习](papers/reinforcement-learning.md) | 0 | 从交互、反馈和离线经验中学习。 |
| [机器人学](papers/robotics.md) | 1 | 机器人感知、策略学习、规划与控制。 |
| <a id="multimodal-learning"></a>[多模态学习](papers/multimodal.md) | 0 | 结合图像、文本、音频等模态进行学习。 |

<p align="right"><a href="#top">↑ 回到顶部</a></p>

<a id="insights-by-technical-category"></a>

## 按技术类型浏览

从想借用的技术入手，比如辅助损失、模块改动或训练策略。

<a id="loss-functions"></a>

### 损失函数

| Insight | 一句话概括 | 来源 |
| :--- | :--- | :--- |
| [**用目标区域重建做辅助监督**](insights/loss-functions.md#target-region-reconstruction-as-auxiliary-supervision) | 用目标物体裁剪区域的潜变量重建，给策略表征增加训练监督。 | [ReconVLA](papers/robotics.md#vision-language-action-models) |

<a id="modules"></a>

### 模块

| Insight | 一句话概括 | 来源 |
| :--- | :--- | :--- |
| [**用指令前缀让视觉表征感知任务**](insights/modules.md#instruction-prefixes-for-causal-visual-grounding) | 把指令 token 放在图像 token 前，使视觉隐藏状态能通过因果注意力读取任务信息。 | [ReconVLA](papers/robotics.md#vision-language-action-models) |

**全部技术分类**

| 技术分类 | 收录范围 |
| :--- | :--- |
| <a id="architectures"></a>[模型架构](insights/architecture.md) | 整体架构与信息流。 |
| [模块](insights/modules.md) | 可复用组件与局部连接方式。 |
| [损失函数](insights/loss-functions.md) | 训练目标、辅助监督与正则化。 |
| <a id="optimization"></a>[优化](insights/optimization.md) | 梯度更新、参数化与优化过程。 |
| <a id="reinforcement-learning-methods"></a>[强化学习方法](insights/reinforcement-learning.md) | 奖励、探索、信用分配与策略改进。 |
| <a id="training-strategies"></a>[训练策略](insights/training-strategies.md) | 训练日程、课程学习与多阶段训练。 |
| <a id="data-strategies"></a>[数据策略](insights/data-strategies.md) | 数据筛选、标注、增强与采样。 |
| <a id="inference-strategies"></a>[推理策略](insights/inference.md) | 解码、测试时适配与高效执行。 |

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

会议公布官方主会录用名单或论文集后，按技术主题筛选。有公开全文、能定位原文依据、且有具体迁移场景的技术点可以收录。更新批次随会议出榜安排。

<a id="recent-updates"></a>

## 最近更新

- **2026-11-15** · 收录 ReconVLA（AAAI 2026）的两条 Insight。 [用目标区域重建做辅助监督](insights/loss-functions.md#target-region-reconstruction-as-auxiliary-supervision) · [用指令前缀让视觉表征感知任务](insights/modules.md#instruction-prefixes-for-causal-visual-grounding)

<a id="contributing"></a>

## 参与贡献

欢迎补充论文、提取可复用技术或修正已有条目。见 [贡献指南](CONTRIBUTING.md)。

[MIT License](LICENSE)
