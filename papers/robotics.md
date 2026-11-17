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
| <a id="cao26u-architecture"></a>[Hierarchical Policy Learning via Spectral Decomposition](https://proceedings.mlr.press/v306/cao26u.html) | 频域分层动作策略 | 将动作序列经 DCT 拆为低频粗运动和高频修正，再根据观察与语言生成粗轨迹、以粗轨迹为条件补上对齐和接触所需细节。 |

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

<a id="by-optimization"></a>

### 优化

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="chaudhary26a-optimization"></a>[Blending Neural Control Density Functions for Stabilization and Safety](https://proceedings.mlr.press/v306/chaudhary26a.html) | 安全控制器混合 | 用可积的神经密度函数作为几乎处处稳定的证书，可平滑混合多个控制器并保住各自吸引域的并集，再与控制障碍函数结合处理安全。 |

<a id="by-reinforcement-learning"></a>

### 强化学习方法

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="aichmuller26a-reinforcement-learning"></a>[Learning to Search and Searching to Learn for Generalization in Planning](https://proceedings.mlr.press/v306/aichmuller26a.html) | 规划与强化学习 | 用关系图网络预测价值启发式来指导加权 A*，再用搜索产生的经验做 Q-learning，形成可自我改进的规划循环。 |

<a id="by-training-strategies"></a>

### 训练策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="chen26d-training-strategies"></a>[NOMAD: Lifelong Trajectory Planning via Non-Parametric Bayesian Memory-Adaptive Diffusion Experts](https://proceedings.mlr.press/v306/chen26d.html) | 终身轨迹规划 | 让非参数贝叶斯记忆按新驾驶场景增长簇，扩散规划器按簇专门化，并用旧簇生成回放样本以保留此前技能。 |

<a id="by-data-strategies"></a>

### 数据策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="chen26j-data-strategies"></a>[RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation](https://proceedings.mlr.press/v306/chen26j.html) | 双臂仿真数据生成 | 让多模态模型编写任务程序，由仿真执行结果反馈失败并引导改写。程序通过后再沿杂物、光照、背景、台面高度和语言等维度生成变体。 |
| <a id="chen26ab-data-strategies"></a>[PhyScene3D: Physically Consistent Interactive 3D Tabletop Scene Generation](https://proceedings.mlr.press/v306/chen26ab.html) | 物理可用的桌面场景 | 先按锚点依赖顺序放置物体，再用可微 SDF 在测试时优化碰撞并约束语义关系，使生成布局更容易直接载入物理仿真。 |

<a id="by-inference"></a>

### 推理策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="aissi26a-inference"></a>[PRISM: Perception Reasoning Interleaved for Sequential Decision Making.](https://proceedings.mlr.press/v306/aissi26a.html) | 具身 Agent 感知 | 让决策模型检查初始图像描述，围绕当前任务追问视觉模型，再用得到的细节做动作决策。 |
| <a id="balim26a-inference"></a>[Model-Based Diffusion Sampling for Predictive Control in Offline Decision Making](https://proceedings.mlr.press/v306/balim26a.html) | 扩散预测控制 | 在去噪过程中交替做任务规划和动力学修正，再按目标排序候选轨迹。动力学模型可以独立使用额外数据训练。 |
| <a id="beyer26a-inference"></a>[Motion Planning in Compressed Representation Spaces](https://proceedings.mlr.press/v306/beyer26a.html) | 压缩空间运动规划 | 用自编码器把轨迹压成粗到细的离散 token，在潜空间按测试时指定的目标搜索，兼顾训练数据里的行为先验与可更换的规划目标。 |
| <a id="chai26a-inference"></a>[N2M: Bridging Navigation and Manipulation by Learning Pose Preference from Rollout](https://proceedings.mlr.press/v306/chai26a.html) | 移动操作站位 | 用操控策略的 rollout 给候选站位打分，并通过视角增强学习对视角不敏感的站位偏好，把策略能否成功执行纳入导航目标。 |
| <a id="chen26i-inference"></a>[PSG-Nav: Probabilistic Scene Graph Navigation via Multiverse Decision Making](https://proceedings.mlr.press/v306/chen26i.html) | 概率场景图导航 | 保留每个节点的完整类别分布，从联合分布选取多个可能世界来评估候选地标，再用过去成败轨迹校准当前检测结果。 |

<a id="by-evaluation"></a>

### 评测与诊断

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="bai26e-evaluation"></a>[SafeLab: An Interactive High-Fidelity Benchmark for Embodied Safety in Scientific Robotics](https://proceedings.mlr.press/v306/bai26e.html) | 机器人轨迹安全 | 将全轨迹内的安全约束计入成功条件，再冻结原策略训练有界残差纠正动作，可以修复最终任务虽完成、过程却发生违规的轨迹。 |
| <a id="cao26w-evaluation"></a>[DLO-Lab: Benchmarking Deformable Linear Object Manipulations with Differentiable Physics](https://proceedings.mlr.press/v306/cao26w.html) | 柔性线状物体操作 | 在同一个可微仿真中改变线状物体的伸缩、弯曲塑性和交互条件，从而检验策略能否跨材料泛化。规划时还可显式选择有控制权的抓点。 |
<!-- classification:end -->
