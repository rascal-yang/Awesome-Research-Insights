# 机器人学

[首页](../README.md) · [参与贡献](../CONTRIBUTING.md) · [English](../en/papers/robotics.md)

机器人感知、策略学习、规划与控制。

<a id="vision-language-action-models"></a>

## 视觉—语言—动作模型

| 论文 | 首次公开 / 发表 | 可借鉴的技术 | 资源 |
| :--- | :--- | :--- | :--- |
| [**ReconVLA**](https://arxiv.org/abs/2508.10333)<br><sub>Song et al., ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver</sub> | 2025-08-14<br><sub>[AAAI 2026](https://ojs.aaai.org/index.php/AAAI/article/download/38921/42883)</sub> | [用目标区域重建做辅助监督](../insights/loss-functions.md#target-region-reconstruction-as-auxiliary-supervision)<br>[用指令前缀让视觉表征感知任务](../insights/modules.md#instruction-prefixes-for-causal-visual-grounding) | [论文](https://arxiv.org/abs/2508.10333) · [项目](https://zionchow.github.io/ReconVLA/) · [代码](https://github.com/OpenHelix-Team/ReconVLA) |
| [**LARA**](https://proceedings.mlr.press/v306/liu26bl.html)<br><sub>Mengya Liu 等, LARA: Latent Action Representation Alignment for Vision-Language-Action Models</sub> | [2026-06-05](https://arxiv.org/abs/2606.07100)<br><sub>[ICML 2026](https://proceedings.mlr.press/v306/liu26bl.html)</sub> | [用潜动作监督动作专家的中间层](../insights/loss-functions.md#align-action-features-with-latent-actions) | [PMLR](https://proceedings.mlr.press/v306/liu26bl.html) · [arXiv](https://arxiv.org/abs/2606.07100) · [代码](https://github.com/lmy1001/LARA) |

<!-- classification:start -->
## 按技术类型浏览

<a id="by-architecture"></a>

### 模型架构

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="bai26h-architecture"></a>[Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models](https://proceedings.mlr.press/v306/bai26h.html) | VLA 潜空间推理 | 按课程将显式文本和视觉思维链监督过渡到连续潜推理，再用这些潜状态条件化动作生成，推理时省去显式思维链解码。 |

<a id="by-modules"></a>

### 模块

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="reconvla-modules"></a>[ReconVLA](https://arxiv.org/abs/2508.10333) | 指令前缀 | 把指令 token 放在图像 token 前，使视觉隐藏状态通过因果注意力读取任务信息。 [详细解读](../insights/modules.md#instruction-prefixes-for-causal-visual-grounding) |

<a id="by-loss-functions"></a>

### 损失函数

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="amad26a-loss-functions"></a>[DT²: Decision-Targeted Digital Twins](https://proceedings.mlr.press/v306/amad26a.html) | 面向决策的数字孪生 | 用离线价值评估给策略排序，再训练数字孪生保住这些成对排序。当模型容量受限时，单步预测精度和策略选择质量可以分离。 |
| <a id="liu26bl-loss-functions"></a>[LARA: Latent Action Representation Alignment for Vision-Language-Action Models](https://proceedings.mlr.press/v306/liu26bl.html) | 动作表征监督 | 用视频前后帧提取潜动作，监督动作专家的中间层，使策略表征能利用额外的运动信号。 [详细解读](../insights/loss-functions.md#align-action-features-with-latent-actions) |
| <a id="reconvla-loss-functions"></a>[ReconVLA](https://arxiv.org/abs/2508.10333) | 目标区域重建 | 用目标物体裁剪区域的潜变量重建，给策略表征增加训练监督。 [详细解读](../insights/loss-functions.md#target-region-reconstruction-as-auxiliary-supervision) |

<a id="by-reinforcement-learning"></a>

### 强化学习方法

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="aichmuller26a-reinforcement-learning"></a>[Learning to Search and Searching to Learn for Generalization in Planning](https://proceedings.mlr.press/v306/aichmuller26a.html) | 规划与强化学习 | 用关系图网络预测价值启发式来指导加权 A*，再用搜索产生的经验做 Q-learning，形成可自我改进的规划循环。 |

<a id="by-inference"></a>

### 推理策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="aissi26a-inference"></a>[PRISM: Perception Reasoning Interleaved for Sequential Decision Making.](https://proceedings.mlr.press/v306/aissi26a.html) | 具身 Agent 感知 | 让决策模型检查初始图像描述，围绕当前任务追问视觉模型，再用得到的细节做动作决策。 |
| <a id="balim26a-inference"></a>[Model-Based Diffusion Sampling for Predictive Control in Offline Decision Making](https://proceedings.mlr.press/v306/balim26a.html) | 扩散预测控制 | 在去噪过程中交替做任务规划和动力学修正，再按目标排序候选轨迹。动力学模型可以独立使用额外数据训练。 |
| <a id="beyer26a-inference"></a>[Motion Planning in Compressed Representation Spaces](https://proceedings.mlr.press/v306/beyer26a.html) | 压缩空间运动规划 | 用自编码器把轨迹压成粗到细的离散 token，在潜空间按测试时指定的目标搜索，兼顾训练数据里的行为先验与可更换的规划目标。 |

<a id="by-evaluation"></a>

### 评测与诊断

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="bai26e-evaluation"></a>[SafeLab: An Interactive High-Fidelity Benchmark for Embodied Safety in Scientific Robotics](https://proceedings.mlr.press/v306/bai26e.html) | 机器人轨迹安全 | 将全轨迹内的安全约束计入成功条件，再冻结原策略训练有界残差纠正动作，可以修复最终任务虽完成、过程却发生违规的轨迹。 |
<!-- classification:end -->
