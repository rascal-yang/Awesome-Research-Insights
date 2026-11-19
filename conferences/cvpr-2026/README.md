# CVPR 2026

[首页](../../README.md) · [官方论文目录](https://openaccess.thecvf.com/CVPR2026?day=all) · [筛选底册](papers.tsv)

CVF Open Access 主会目录含 4,042 个不同的论文页面。已筛选 60 篇，其中 49 篇暂收录、11 篇排除，另有 3,982 篇待筛。最终按贡献指南统一排名，收录上限为 50%。

| 领域 | 技术类型 | 论文卡 | 能改变的技术选择 |
| --- | --- | --- | --- |
| 计算机视觉 | 训练策略 | [EcoSplat: Efficiency-controllable Feed-forward 3D Gaussian Splatting from Multi-view Images](cards.md#paper-ecosplat) | 将基元预算作为模型输入，比较预算感知预测和事后剪枝。 |
| 多模态学习 | 推理解码 | [SEASON: Mitigating Temporal Hallucination in Video Large Language Models via Self-Diagnostic Contrastive Decoding](cards.md#paper-season) | 对照正常和时序负样本的解码，诊断逐词时序依赖。 |
| 机器学习基础与统计 | 表征学习 | [HyCal: A Training-Free Prototype Calibration Method for Cross-Discipline Few-Shot Class-Incremental Learning](cards.md#paper-hycal) | 冻结特征时比较余弦、协方差距离与动态融合。 |
| 多模态学习 | 评测与诊断 | [QUANTIPHY: A Quantitative Benchmark Evaluating Physical Reasoning Abilities of Vision-Language Models](cards.md#paper-quantiphy) | 用仅先验和反事实先验对照，检验数值回答是否依赖视频。 |
| 计算机视觉 | 模块 | [Generalizable Structure-Aware Keypoint Correspondence for Category-Unified 3D Single Object Tracking](cards.md#paper-unikpt) | 稀疏点云跟踪时，比较尺度适配关键点的渐进匹配与密集对应。 |
| 计算机视觉 | 优化 | [DirectFisheye-GS: Enabling Native Fisheye Input in Gaussian Splatting with Cross-View Joint Optimization](cards.md#paper-directfisheye-gs) | 用特征重叠挑选联合优化视角，并测试跨视角约束能否抑制边缘漂浮伪影。 |
| 多模态学习 | 评测与诊断 | [CompBench: Benchmarking Complex Instruction-guided Image Editing](cards.md#paper-compbench) | 把编辑指令拆成位置、外观、动态和对象条件，并分别验收目标变化与背景保留。 |
| 计算机视觉 | 训练策略 | [Choreographing a World of Dynamic Objects](cards.md#paper-chord) | 从冻结视频生成器蒸馏持久的三维运动表示，并把跨视角一致性作为独立验收项。 |
| 计算机视觉 | 模型架构 | [Spk2VidNet: A Hierarchical Recurrent Architecture for High-Fidelity Video Reconstruction from Long Spike-Camera Streams](cards.md#paper-spk2vidnet) | 在显存固定时分段传递循环状态，并把跨帧对齐与可用历史长度分开消融。 |
| 机器学习基础与统计 | 训练策略 | [Continual Distillation of Teachers from Different Domains](cards.md#paper-se2d) | 连续蒸馏时保留相关外部样本上的输出，并把旧域遗忘和当前域适配分开衡量。 |
| 多模态学习 | 训练策略 | [GT-SVJ: Generative-Transformer-Based Self-Supervised Video Judge For Efficient Video Reward Modeling](cards.md#paper-gt-svj) | 复用视频生成骨干做偏好评分，用受控时序退化训练评审器，并以人类偏好排序验证。 |
| 机器学习基础与统计 | 优化 | [Beyond Euclidean Gossip: KL-Barycentric Consensus on Heterogeneous and Imbalanced Images](cards.md#paper-kl-barycentric-consensus) | 去中心化训练时，用后验期望参数做共识，并在相同通信预算下对照欧氏平均。 |
| 机器人学 | 推理规划 | [HybridDriveVLA: Vision-Language-Action Model with Visual CoT reasoning and ToT Evaluation for Autonomous Driving](cards.md#paper-hybriddrivevla) | 固定候选轨迹评分流程，对照是否加入视觉未来预测，并分别监测安全、进度和舒适。 |
| 计算机视觉 | 推理策略 | [Training-free, Perceptually Consistent Low-Resolution Previews with High-Resolution Image for Efficient Workflows of Diffusion Models](cards.md#paper-commutator-zero-diffusion-preview) | 扩散预览切换空间分辨率时，用可测的速度场交换误差选择降采样并校正潜变量；见 §3.3–3.4、表 2 和表 5。 |
| 计算机视觉 | 模型架构 | [Catalyst4D: High-Fidelity 3D-to-4D Scene Editing via Dynamic Propagation](cards.md#paper-catalyst4d) | 静态编辑向动态重建传播变形时，以区域锚及最优传输替代逐点近邻，避免把相邻肢体的运动混在一起；见 §5.4、图 6。 |
| 强化学习与决策 | 训练策略 | [Cloning Deterministic Worlds: The Critical Role of Latent Geometry in Long-Horizon World Models](cards.md#paper-grwm-latent-geometry) | 长时世界模型应单独对潜在状态的时间几何做监督和探测，而不是只用逐帧重建误差挑选编码器；见 §5.2、§6.4。 |
| 计算机视觉 | 数据策略 | [Unique Lives, Shared World: Learning from Single-Life Videos](cards.md#paper-single-life-geometry) | 采集几何表征训练数据时，可对照等规模多样网络视频，先测试单一长程第一视角流中的时间配对；见 §5.2、图 7–9。 |
| 多模态学习 | 训练策略 | [Quantized Residuals to Continuous Prompts for Few-Shot Class Incremental Learning in Vision-Language Models](cards.md#paper-qr-prompt) | 少样本增量分类时，将视觉与文本间残差信号量化后生成可适配的连续提示；用等架构直接量化视觉特征作对照，见表 2。 |
| 计算机视觉 | 推理压缩 | [UniComp: Rethinking Video Compression Through Informational Uniqueness](cards.md#paper-unicomp) | 在视觉词元总预算固定时，按跨帧与帧内的信息独特性分配预算，可与均匀分配做受控对照。 |
| 计算机视觉 | 模型架构 | [AD-GBC: Anisotropic Granular-Ball Skip-Connection Refiner for UNet-Based Medical Image Segmentation](cards.md#paper-ad-gbc) | 用逐轴尺度把点原型推广为可微区域，并单独验证区域几何、正则与额外计算的收益。 |
| 计算机视觉 | 推理策略 | [White-Balance First, Adjust Later: Cross-Camera Color Constancy via Vision-Language Evaluation](cards.md#paper-vlm-cc) | 从初始估计渲染可读反馈，再用离散残差方向修正连续变量，可对照直接让视觉语言模型回归数值。 |
| 多模态学习 | 推理策略 | [Reallocating Attention Across Layers to Reduce Multimodal Hallucination](cards.md#paper-attention-head-reallocation) | 感知和推理错误可按注意力头功能分开干预，并以双向消融验证同一模型在看图和推理任务上的取舍。 |
| 多模态学习 | 训练策略 | [PanoEnv: Exploring 3D Spatial Intelligence in Panoramic Environments with Reinforcement Learning](cards.md#paper-panoenv) | 用结构化任务预热开放式空间问答时保留结构化回放，并以反向课程和单阶段对照检查格式熟练是否带来开放题迁移。 |
| 多模态学习 | 模型编辑与训练 | [Erasing Thousands of Concepts: Towards Scalable and Practical Concept Erasure for Text-to-Image Diffusion Models](cards.md#paper-etc) | 大规模概念移除时把目标移除与邻近概念保留作为独立目标。 |
| 计算机视觉 | 测试时适应与推理 | [TALON: Test-time Adaptive Learning for On-the-Fly Category Discovery](cards.md#paper-talon) | 在线类别发现应分开选择新类判阈和更新旧类表示。 |
| 多模态学习 | 强化学习 | [SenseSearch: Empowering Vision-Language Models with High-Resolution Agentic Search-Reasoning via Reinforcement Learning](cards.md#paper-sensesearch) | 工具混用时批量归一优势，独立检查检索和细粒度感知是否一起改善。 |
| 计算机视觉 | 模型架构 | [REArtGS++: Generalizable Articulation Reconstruction with Temporal Geometry Constraint via Planar Gaussian Splatting](cards.md#paper-reartgs-plus) | 把关节类型统一为可分解螺旋运动，利用深度与法线时间一致性约束未见状态。 |
| 多模态学习 | 量化推理 | [Quant Experts: Token-aware Adaptive Error Reconstruction with Mixture of Experts for Large Vision-Language Models Quantization](cards.md#paper-quant-experts) | 区分跨词元共享误差与特定词元的量化误差，再决定修复是否路由。 |
| 多模态学习 | 模型架构 | [Efficient and High-Fidelity Omni Modality Retrieval](cards.md#paper-omniret) | 分开验收固定长度重采样和分布式池化，避免多模态检索的单向量读出损失。 |
| 多模态学习 | 损失函数 | [SynCLIP: Synonym-Coherent Language-Image Pretraining for Robust Open-Vocabulary Dense Perception](cards.md#paper-synclip) | 开放词汇定位应对同义改写单独验收，并训练同义提示间的空间注意力一致性。见 §4.3.2、表 3–4。 |
| 计算机视觉 | 推理策略 | [AdaSpot: Spend Resolution Where It Matters for Precise Event Spotting](cards.md#paper-adaspot) | 视频事件定位时，以时空平滑的低分辨率响应分配高分辨率裁剪，按事件规模测试固定和自适应窗口。见 §4、表 3。 |
| 机器学习基础与统计 | 评测与诊断 | [What Is the Optimal Ranking Score Between Precision and Recall? We Can Always Find It and It Is Rarely F1](cards.md#paper-precision-recall-rank-tradeoff) | 如果综合排名希望兼顾精确率与召回率的排序，应针对候选集合计算 Fβ，而非默认 F1。见 §3.3–3.4、式 12、表 1。 |
| 计算机视觉 | 优化 | [Rethinking Pose Refinement in 3D Gaussian Splatting under Pose Prior and Geometric Uncertainty](cards.md#paper-probabilistic-gs-pose-refinement) | 定位精化应分开处理初始位姿偏差与高斯深度不确定性，分别用多候选和加权 PnP，见 §3.2–3.3。 |
| 多模态学习 | 强化学习 | [RetouchIQ: MLLM Agents for Instruction-Based Image Retouching with Generalist Reward](cards.md#paper-retouchiq-generalist-reward) | 主观编辑任务中，奖励模型可先生成指令相关的评判维度，再对执行结果评分，并用策略当前样本检查奖励排序。见 §4、图 5。 |
| 计算机视觉 | 表征学习 | [Anomaly-Related Residual Fields for Cross-domain Anomaly Detection](cards.md#paper-anomaly-residual-evolution-field) | 做跨域视觉异常检测可比较末步重建残差与残差随去噪时间持续性的证据。见 §3、表 1–2。 |
| 计算机视觉 | 模型架构 | [LongStream: Long-Sequence Streaming Autoregressive Visual Geometry](cards.md#paper-longstream) | 流式几何以局部关键帧作为位姿参考，将尺度估计独立处理，并在训练复现部署缓存状态。 |
| 多模态学习 | 推理策略 | [VisRef: Visual Refocusing while Thinking Improves Test-Time Scaling in Multi-Modal Large Reasoning Models](cards.md#paper-visref) | 推理中访问图像时同时按当前上下文相关性和视觉覆盖选证据，可在固定预算对照纯文本反思。 |
| 计算机视觉 | 推理策略 | [Ultra Diffusion Poser: Diffusion-Based Human Motion Tracking from Sparse Inertial Sensors and Ranging-based Between-sensor Distances](cards.md#paper-ultra-diffusion-poser) | 同一距离观测可先解析出几何布局，再作为扩散采样一致性约束，并和把测距只当输入的方案做对照。 |
| 机器人学 | 训练策略 | [Beyond Mimicry: Learning Whole-Body Human-Humanoid Interaction from Human-Human Demonstrations](cards.md#paper-pair-d-star) | 跨形态重定向先保留接触关系，策略再将接触时机和空间位置解耦学习。 |
| 计算机视觉 | 剪枝与推理加速 | [Pluggable Pruning with Contiguous Layer Distillation for Diffusion Transformers](cards.md#paper-ppcl) | 为多档部署预算训练可插拔连续层块，在一次联合蒸馏中覆盖深宽切换。 |
| 多模态学习 | 训练策略 | [APPO: Attention-guided Perception Policy Optimization for Video Reasoning](cards.md#paper-appo) | 把组内不同回答中关注同一关键视频帧的词元放在一起分配感知信用，可与全序列共享奖励直接比较。 |
| 多模态学习 | 评测与诊断 | [GraphVLM: Benchmarking Vision Language Models for Multimodal Graph Learning](cards.md#paper-graphvlm) | 以角色对照选择让视觉语言模型直接预测，还是只作为图模型的编码器或对齐器。 |
| 计算机视觉 | 量化与剪枝推理 | [Rethinking Asymmetric Quantization: Hidden Symmetry in Vision Model Weights](cards.md#paper-dasq) | 先检查权重异常值移除后是否近对称，再选择无零点的低位算子。 |
| 多模态学习 | 模型架构 | [Hierarchical Enhancement of Semantic Priors for Disentangled Text-Driven Motion Generation](cards.md#paper-hesp) | 动作生成若有独立语义因素，可先替换潜先验，再分别测语言融合和分层注意。 |
| 多模态学习 | 评测与诊断 | [MovieRecapsQA: A Multimodal Open-Ended Video Question-Answering Benchmark](cards.md#paper-movierecapsqa) | 开放问答逐条验必要事实，并控制可见剪辑与对话范围，区分检索和多模态作答。 |
| 多模态学习 | 模型架构 | [Scalable Object Relation Encoding for Better 3D Spatial Reasoning in Large Language Models](cards.md#paper-quatrope) | 将关系计算放到注意力相互作用里，保留对象线性长度，避免为对象对另加输入词元。 |
| 多模态学习 | 训练策略 | [Physical Simulator In-the-Loop Video Generation](cards.md#paper-psivg) | 先由物理模拟产生轨迹，再以投影对应约束视频外观，单独核运动与纹理。 |
| 计算机视觉 | 训练策略 | [PR-IQA: Partial-Reference Image Quality Assessment for Diffusion-Based Novel View Synthesis](cards.md#paper-pr-iqa) | 只采用其他真实视角能验证的伪视图局部，并用空间质量映射决定监督掩码。 |
| 机器人学 | 训练策略 | [FloVerse: Floor Plan-Guided Multi-Modal Navigation](cards.md#paper-floverse) | 隔离平面图先验和近场反馈，检验同一规划器对不同目标模态的收益。 |
