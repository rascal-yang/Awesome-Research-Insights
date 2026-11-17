# 机器人学

[首页](../README.md) · [参与贡献](../CONTRIBUTING.md) · [English](../en/papers/robotics.md)

机器人感知、策略学习、规划与控制。

<a id="vision-language-action-models"></a>

## 视觉—语言—动作模型

| 论文 | 首次公开 / 发表 | 可借鉴的技术 | 资源 |
| :--- | :--- | :--- | :--- |
| [**ReconVLA**](https://arxiv.org/abs/2508.10333) · [论文卡](reconvla.md#paper-reconvla)<br><sub>Song et al., ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver</sub> | 2025-08-14<br><sub>[AAAI 2026](https://ojs.aaai.org/index.php/AAAI/article/download/38921/42883)</sub> | [用目标区域重建做辅助监督](../insights/loss-functions.md#target-region-reconstruction-as-auxiliary-supervision)<br>[用指令前缀让视觉表征感知任务](../insights/modules.md#instruction-prefixes-for-causal-visual-grounding) | [论文](https://arxiv.org/abs/2508.10333) · [项目](https://zionchow.github.io/ReconVLA/) · [代码](https://github.com/OpenHelix-Team/ReconVLA) |
| [**LARA**](https://proceedings.mlr.press/v306/liu26bl.html) · [论文卡](../conferences/icml-2026/cards/2801-2900.md#paper-liu26bl)<br><sub>Mengya Liu 等, LARA: Latent Action Representation Alignment for Vision-Language-Action Models</sub> | [2026-06-05](https://arxiv.org/abs/2606.07100)<br><sub>[ICML 2026](https://proceedings.mlr.press/v306/liu26bl.html)</sub> | [用潜动作监督动作专家的中间层](../insights/loss-functions.md#align-action-features-with-latent-actions) | [PMLR](https://proceedings.mlr.press/v306/liu26bl.html) · [arXiv](https://arxiv.org/abs/2606.07100) · [代码](https://github.com/lmy1001/LARA) |

<!-- classification:start -->
## 按技术类型浏览

<a id="by-architecture"></a>

### 模型架构

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="bai26h-architecture"></a>[Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models](https://proceedings.mlr.press/v306/bai26h.html) | VLA 潜空间推理 | 按课程将显式文本和视觉思维链监督过渡到连续潜推理，再用这些潜状态条件化动作生成，推理时省去显式思维链解码。 |
| <a id="cao26u-architecture"></a>[Hierarchical Policy Learning via Spectral Decomposition](https://proceedings.mlr.press/v306/cao26u.html) | 频域分层动作策略 | 将动作序列经 DCT 拆为低频粗运动和高频修正，再根据观察与语言生成粗轨迹、以粗轨迹为条件补上对齐和接触所需细节。 |
| <a id="chuang26a-architecture"></a>[The Lie We Tell: Correcting the Euclidean Fallacy in Vision Language Action Policies via Score Matching on Tangent Space](https://proceedings.mlr.press/v306/chuang26a.html) | SE(3) 位姿扩散策略 | 在 SE(3) 上用左不变随机微分方程给机器人位姿加噪，在切空间预测反向去噪分数，再用指数映射更新位姿，使采样过程中的旋转保持在 SO(3) 上。 |
| <a id="ding26x-architecture"></a>[Embodied-DETR: End-to-End Temporal 3D Object Detection in Egocentric Views](https://proceedings.mlr.press/v306/ding26x.html) | 第一视角三维检测的时序记忆 | 将先前帧的稀疏点特征存入统一坐标系，在当前视锥内检索聚合，并从仍可见的历史实例构造动态查询，与发现新实例的查询共同解码，以兼顾遮挡下的定位与身份一致性。 |

<a id="by-modules"></a>

### 模块

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="feng26x-modules"></a>[See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model](https://proceedings.mlr.press/v306/feng26x.html) | 视觉动作策略的连续网格采样 | 由任务条件预测少量连续采样坐标，并对各坐标周围四个视觉特征做双线性插值。可微采样允许动作监督调整坐标，也能保留位于图块边界的抓取线索。 |
| <a id="fu26x-modules"></a>[StableVLA: Towards Robust Vision-Language-Action Models without Extra Data](https://proceedings.mlr.press/v306/fu26x.html) | 视觉动作模型的通道相关门控 | 将视觉投影特征分成多个通道子空间，沿空间词元计算通道相关性，再经 sigmoid 门控筛选信息。用这一轻量适配器增强稳健的视觉语义，在论文扰动测试中提升操作策略的鲁棒性。 |
| <a id="gyenes26a-modules"></a>[Fourier Features Let Agents Learn High Precision Policies with Imitation Learning](https://proceedings.mlr.press/v306/gyenes26a.html) | 精密操作的点云傅里叶编码 | 在点云送入策略编码器前，对每个笛卡尔坐标独立计算多波长正余弦特征。高频分量为模仿学习提供更直接的细微几何差异，便于区分插入与重新对位等动作。 |
| <a id="reconvla-modules"></a>[ReconVLA](https://arxiv.org/abs/2508.10333) · [论文卡](reconvla.md#paper-reconvla) | 指令前缀 | 把指令 token 放在图像 token 前，使视觉隐藏状态通过因果注意力读取任务信息。 [详细解读](../insights/modules.md#instruction-prefixes-for-causal-visual-grounding) |

<a id="by-loss-functions"></a>

### 损失函数

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="amad26a-loss-functions"></a>[DT²: Decision-Targeted Digital Twins](https://proceedings.mlr.press/v306/amad26a.html) | 面向决策的数字孪生 | 用离线价值评估给策略排序，再训练数字孪生保住这些成对排序。当模型容量受限时，单步预测精度和策略选择质量可以分离。 |
| <a id="fang26h-loss-functions"></a>[OMP: One-step Meanflow Policy with Directional Alignment](https://proceedings.mlr.press/v306/fang26h.html) | 单步操作策略的速度方向监督 | 在 MeanFlow 重建目标外，用预测速度与真实平均速度的余弦相似度单独监督方向，使低速精细动作仍获得方向梯度。论文还用有限差分近似训练所需的导数，以减轻显存开销。 |
| <a id="liu26bl-loss-functions"></a>[LARA: Latent Action Representation Alignment for Vision-Language-Action Models](https://proceedings.mlr.press/v306/liu26bl.html) · [论文卡](../conferences/icml-2026/cards/2801-2900.md#paper-liu26bl) | 动作表征监督 | 用视频前后帧提取潜动作，监督动作专家的中间层，使策略表征能利用额外的运动信号。 [详细解读](../insights/loss-functions.md#align-action-features-with-latent-actions) |
| <a id="reconvla-loss-functions"></a>[ReconVLA](https://arxiv.org/abs/2508.10333) · [论文卡](reconvla.md#paper-reconvla) | 目标区域重建 | 用目标物体裁剪区域的潜变量重建，给策略表征增加训练监督。 [详细解读](../insights/loss-functions.md#target-region-reconstruction-as-auxiliary-supervision) |

<a id="by-optimization"></a>

### 优化

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="chaudhary26a-optimization"></a>[Blending Neural Control Density Functions for Stabilization and Safety](https://proceedings.mlr.press/v306/chaudhary26a.html) | 安全控制器混合 | 用可积的神经密度函数作为几乎处处稳定的证书，可平滑混合多个控制器并保住各自吸引域的并集，再与控制障碍函数结合处理安全。 |
| <a id="fan26g-optimization"></a>[De4D-SLAM: Gradient-Isolated Static-Dynamic Decoupling for Monocular SLAM in Dynamic Environments](https://proceedings.mlr.press/v306/fan26g.html) | 动态 SLAM 的残差梯度隔离 | 用仅含静态模型的渲染残差监督运动预测分支，并在残差处停止梯度，使掩码学习无法靠改变背景几何减小损失。高静态残差可作为移动区域线索，用于调节后续静态和动态重建。 |

<a id="by-reinforcement-learning"></a>

### 强化学习方法

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="aichmuller26a-reinforcement-learning"></a>[Learning to Search and Searching to Learn for Generalization in Planning](https://proceedings.mlr.press/v306/aichmuller26a.html) | 规划与强化学习 | 用关系图网络预测价值启发式来指导加权 A*，再用搜索产生的经验做 Q-learning，形成可自我改进的规划循环。 |
| <a id="chowdhury26a-reinforcement-learning"></a>[LAGEA: Language Guided Embodied Agents for Robotic Manipulation](https://proceedings.mlr.press/v306/chowdhury26a.html) | 按关键帧分配语言反馈奖励 | 让视觉语言模型对一次操作尝试生成结构化反思，把反思和机器人观测映射到同一表征空间。用状态与反馈相似度的时序变化构造奖励，并用关键帧权重把训练信号集中到关键步骤。 |
| <a id="ge26a-reinforcement-learning"></a>[Dyn-VPP: Video Prediction Policy Optimization for Improved Visual Dynamics](https://proceedings.mlr.press/v306/ge26a.html) | 以专家动态奖励后训练视频预测 | 把多步视频去噪视为策略，用同一编码空间里生成轨迹与专家未来帧的动态一致性作为终局奖励。这样可针对下游操作敏感的预测误差更新生成器，论文在仿真与真机操作中观察到成功率提升。 |
| <a id="guo26ae-reinforcement-learning"></a>[CorrectionPlanner: Self-Correction Planner with Reinforcement Learning in Autonomous Driving](https://proceedings.mlr.press/v306/guo26ae.html) | 碰撞预测驱动的驾驶动作自纠正 | 自回归规划器提出运动 token 后用碰撞评论家检查短期风险。未通过的提议保留在注意力上下文中供下一次提议修正，实际执行最终接受的动作，再用世界模型轨迹对这段纠正过程做强化学习。 |

<a id="by-training-strategies"></a>

### 训练策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="chen26d-training-strategies"></a>[NOMAD: Lifelong Trajectory Planning via Non-Parametric Bayesian Memory-Adaptive Diffusion Experts](https://proceedings.mlr.press/v306/chen26d.html) | 终身轨迹规划 | 让非参数贝叶斯记忆按新驾驶场景增长簇，扩散规划器按簇专门化，并用旧簇生成回放样本以保留此前技能。 |
| <a id="chen26fw-training-strategies"></a>[Generalizable and Actionable Parts Pose Estimation with Symmetry Annotation-Free Learning Strategy](https://proceedings.mlr.press/v306/chen26fw.html) | 部件位姿的弱监督对称估计 | 仅给出对称类型，让模型从点云和预测旋转估计对称轴概率。对镜面对称的候选平面，用原点云与镜像点云的 Chamfer 距离评估一致性，抑制缺少几何支持的平面。 |
| <a id="feng26n-training-strategies"></a>[Knowledge Diversion for Efficient Morphology Control and Policy Transfer](https://proceedings.mlr.press/v306/feng26n.html) | 跨构型控制的奇异分量门控 | 将形态感知 Transformer 的权重拆成 SVD 秩一分量，训练时把分量分为通用、构型专用和任务专用三组。用肢体与关节参数以及任务文本生成软门控，部署时可重组与当前机器人和任务相关的控制器。 |
| <a id="guo26i-training-strategies"></a>[VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model](https://proceedings.mlr.press/v306/guo26i.html) | 视觉动作策略与世界模型的交替改进 | 先用当前机器人策略采集真实成功与失败轨迹，更新动作条件视频世界模型，再用它生成策略的额外滚动轨迹。将奖励模型筛出的成功合成轨迹和真实成功轨迹一起用于下一轮策略微调。 |

<a id="by-data-strategies"></a>

### 数据策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="chen26j-data-strategies"></a>[RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation](https://proceedings.mlr.press/v306/chen26j.html) | 双臂仿真数据生成 | 让多模态模型编写任务程序，由仿真执行结果反馈失败并引导改写。程序通过后再沿杂物、光照、背景、台面高度和语言等维度生成变体。 |
| <a id="chen26ab-data-strategies"></a>[PhyScene3D: Physically Consistent Interactive 3D Tabletop Scene Generation](https://proceedings.mlr.press/v306/chen26ab.html) | 物理可用的桌面场景 | 先按锚点依赖顺序放置物体，再用可微 SDF 在测试时优化碰撞并约束语义关系，使生成布局更容易直接载入物理仿真。 |
| <a id="chen26cy-data-strategies"></a>[Escaping the Diversity Trap in Robotic Manipulation via Anchor-Centric Adaptation](https://proceedings.mlr.press/v306/chen26cy.html) | 固定预算下的机器人示范分配 | 先在少数核心条件重复采集示范以稳定策略，再按教师强制下的动作偏差找出高风险边界，补采示范并用受约束的残差更新扩展覆盖。真机实验中，同等预算下的成功率优于分散采样。 |
| <a id="choi26i-data-strategies"></a>[EMBGuard: Constructing Hazard-Aware Guardrails for Safe Planning in Embodied Agents](https://proceedings.mlr.press/v306/choi26i.html) | 具身动作风险的组合数据构造 | 为同类场景组合不同危险配置与动作，包括在危险仍存在时改用不会触发它的动作。将图像和动作配对并标注风险，使监督信号针对特定交互的后果，也覆盖容易引发误报的安全动作。 |
| <a id="fan26b-data-strategies"></a>[Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds](https://proceedings.mlr.press/v306/fan26b.html) | 跨来源点云的 VLA 训练 | 在统一训练流程中混合仿真、深度传感器和模型估计的点云，并以形状和尺度变化扩展输入。将学到的三维表征与对应的二维特征融合，可减轻部署时深度来源和尺度差异对操作策略的影响。 |
| <a id="gao26q-data-strategies"></a>[DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos](https://proceedings.mlr.press/v306/gao26q.html) | 人类视频的潜动作监督 | 将相邻视频帧之间的变化通过信息瓶颈编码成连续潜动作，作为未标注人类视频的控制信号预训练机器人世界模型，再以目标机器人真动作做适配。 |
| <a id="guan26f-data-strategies"></a>[LIMMT: Less Is More for Motion Tracking](https://proceedings.mlr.press/v306/guan26f.html) | 人形运动跟踪的可行性与难度选样 | 先过滤违反物理约束的轨迹，再用运动嵌入的最近距离和关节速度、加速度衡量多样性与动态难度。每次优先补充覆盖不足且复杂的动作，在论文的 AMASS 实验中，约 3% 的样本已能超过全量训练的跟踪基线。 |

<a id="by-inference"></a>

### 推理策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="aissi26a-inference"></a>[PRISM: Perception Reasoning Interleaved for Sequential Decision Making.](https://proceedings.mlr.press/v306/aissi26a.html) | 具身 Agent 感知 | 让决策模型检查初始图像描述，围绕当前任务追问视觉模型，再用得到的细节做动作决策。 |
| <a id="balim26a-inference"></a>[Model-Based Diffusion Sampling for Predictive Control in Offline Decision Making](https://proceedings.mlr.press/v306/balim26a.html) | 扩散预测控制 | 在去噪过程中交替做任务规划和动力学修正，再按目标排序候选轨迹。动力学模型可以独立使用额外数据训练。 |
| <a id="beyer26a-inference"></a>[Motion Planning in Compressed Representation Spaces](https://proceedings.mlr.press/v306/beyer26a.html) | 压缩空间运动规划 | 用自编码器把轨迹压成粗到细的离散 token，在潜空间按测试时指定的目标搜索，兼顾训练数据里的行为先验与可更换的规划目标。 |
| <a id="chai26a-inference"></a>[N2M: Bridging Navigation and Manipulation by Learning Pose Preference from Rollout](https://proceedings.mlr.press/v306/chai26a.html) | 移动操作站位 | 用操控策略的 rollout 给候选站位打分，并通过视角增强学习对视角不敏感的站位偏好，把策略能否成功执行纳入导航目标。 |
| <a id="chen26i-inference"></a>[PSG-Nav: Probabilistic Scene Graph Navigation via Multiverse Decision Making](https://proceedings.mlr.press/v306/chen26i.html) | 概率场景图导航 | 保留每个节点的完整类别分布，从联合分布选取多个可能世界来评估候选地标，再用过去成败轨迹校准当前检测结果。 |
| <a id="chen26co-inference"></a>[Rethinking Instruction Drift as a Sampling Error: SNR-Aware Power Distributions for Long-Horizon Robotic Planning](https://proceedings.mlr.press/v306/chen26co.html) | 长程机器人轨迹采样 | 当信噪比降至阈值以下时才触发 MCMC 重采样，用整段条件轨迹概率的幂分布比较候选动作序列，让局部决策容易偏离指令的时刻获得更多搜索计算。 |
| <a id="chi26b-inference"></a>[EvoCF: Multi-Agent Collaboration via Agentic Memory-Driven Evolutionary Counterfactual Planning](https://proceedings.mlr.press/v306/chi26b.html) | 多智能体协作的反事实规划 | 把执行失败归纳成可检索的符号约束，再以这些约束为条件对联合计划做变异，用相关历史执行证据给候选排序。在具身协作仿真中，该搜索提高了计划的可执行性。 |
| <a id="choi26a-inference"></a>[SCALE: Self-uncertainty Conditioned Adaptive Looking and Execution for Vision-Language-Action Models](https://proceedings.mlr.press/v306/choi26a.html) | VLA 不确定性调节感知与动作 | 用当前动作分布对高、低不确定性参考分布的 KL 距离差调节动作采样温度，并用上一控制步的不确定性相对历史均值的偏差调节当前视觉注意力温度。这样可在一次视觉编码内同时适配感知和动作探索。 |
| <a id="choi26c-inference"></a>[Efficient Skill Grounding via Code Refactoring with Small Language Models](https://proceedings.mlr.press/v306/choi26c.html) | 机器人技能代码的局部重绑定 | 把技能的控制流程保存为可执行代码，部署时用本体比对目标机器人的能力和原语 API。对确定的冲突，让小语言模型只填补受影响的代码片段，依赖现场感知的条件留到执行时检验和调整。 |
| <a id="chun26a-inference"></a>[Functional Cache Grafting: Robust and Rapid Code-Policy Synthesis for Embodied Agents](https://proceedings.mlr.press/v306/chun26a.html) | 函数级 KV 缓存拼接与修补 | 缓存已验证函数的接口和实现。合成机器人代码策略时，将相关接口的 KV 状态拼入上下文并链接现成函数，执行反馈指出需调整的位置后，只重解码受影响的代码片段。 |
| <a id="ding26r-inference"></a>[AdaNav: Adaptive Reasoning with Uncertainty for Vision-Language Navigation](https://proceedings.mlr.press/v306/ding26r.html) | 导航中的熵驱动推理 | 将当前动作词元的平均熵与历史熵走势作为触发推理的先验，用奖励兼顾接近目标与推理成本，再逐步交由学习到的策略选择何时推理。 |
| <a id="guo26l-inference"></a>[Reflex: Real-Time Vision-Language-Action Control through Streaming Inference](https://proceedings.mlr.press/v306/guo26l.html) | 视觉动作模型的流式分区缓存 | 把上下文分成固定指令、滑动视觉观测和动态流状态，只对第三部分注入去噪时刻并随迭代重算。感知前缀因此可增量复用，在固定输入下保持与整批注意力等价。 |

<a id="by-representation-learning"></a>

### 表征学习

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="fan26f-representation-learning"></a>[XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations](https://proceedings.mlr.press/v306/fan26f.html) | 跨机器人共享的视觉运动码 | 用双分支 VQ-VAE 将图像动态和机器人动作压入共享离散码本，再用这些码引导跨本体 VLA 预训练。统一的中间运动表示让不同机器人或视觉来源的动态知识可服务于下游控制。 |
| <a id="habashy26a-representation-learning"></a>[Geodesic Flow Matching for Denoising High-Dimensional Structured Representations](https://proceedings.mlr.press/v306/habashy26a.html) | 空间语义指针的测地流去噪 | 沿单位球上源向量与目标向量间的大圆弧构造训练路径，让模型回归切向速度并在采样中保持单位范数，有助于抑制脉冲神经 SLAM 路径积分的漂移。 |

<a id="by-evaluation"></a>

### 评测与诊断

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="bai26e-evaluation"></a>[SafeLab: An Interactive High-Fidelity Benchmark for Embodied Safety in Scientific Robotics](https://proceedings.mlr.press/v306/bai26e.html) | 机器人轨迹安全 | 将全轨迹内的安全约束计入成功条件，再冻结原策略训练有界残差纠正动作，可以修复最终任务虽完成、过程却发生违规的轨迹。 |
| <a id="cao26w-evaluation"></a>[DLO-Lab: Benchmarking Deformable Linear Object Manipulations with Differentiable Physics](https://proceedings.mlr.press/v306/cao26w.html) | 柔性线状物体操作 | 在同一个可微仿真中改变线状物体的伸缩、弯曲塑性和交互条件，从而检验策略能否跨材料泛化。规划时还可显式选择有控制权的抓点。 |
| <a id="dai26c-evaluation"></a>[RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies](https://proceedings.mlr.press/v306/dai26c.html) | 长程操作记忆的分项评测 | 用动作计数、遮挡后定位、跨时刻身份指代和动作模仿分别考查时间、空间、物体与程序记忆，再在同一 VLA 主干上比较记忆形式和接入方式。实验显示记忆机制的收益随任务类型变化。 |
| <a id="deng26r-evaluation"></a>[Rethinking Video Generation Model for the Embodied World](https://proceedings.mlr.press/v306/deng26r.html) | 机器人生成视频的物理与任务评测 | 将均匀抽样的视频帧组成时间网格，以问答清单分别检查物体穿透、未接触搬运等物理失真和关键动作是否按顺序完成。由此能定位画面流畅但动作不符合任务要求的机器人视频。 |
| <a id="feng26ab-evaluation"></a>[Demystifying Action Space Design for Robotic Manipulation Policies](https://proceedings.mlr.press/v306/feng26ab.html) | 动作块增量的基准姿态 | 在模仿学习的动作块中，让未来各步都相对块起点表示增量，可避免逐步累加预测误差。论文的真机对照中，这种表示比相对前一步的增量更稳定。 |
| <a id="fu26u-evaluation"></a>[CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation](https://proceedings.mlr.press/v306/fu26u.html) | 机器人代码策略的分层脚手架评测 | 将任务按控制接口的抽象层级、感知来源和是否提供示例分层，逐步撤去高层操作原语与示例。结合多轮执行反馈的对照，可区分能力下降来自感知误差、接口组合还是长程控制。 |

<a id="by-theory-statistics"></a>

### 理论与统计

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="francis-meretzki26a-theory-statistics"></a>[Temporal Difference Calibration in Sequential Tasks: Application to Vision-Language-Action Models](https://proceedings.mlr.press/v306/francis-meretzki26a.html) | 用时序差分校准机器人任务成功率 | 对每个部分轨迹预测最终二元成败。在序列版 Brier 风险下，最优置信度等于当前策略的成功价值，因此可用时序差分把终局标签的监督传给途中各步。 |
<!-- classification:end -->
