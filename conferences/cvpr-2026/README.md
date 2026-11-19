# CVPR 2026

[首页](../../README.md) · [官方论文目录](https://openaccess.thecvf.com/CVPR2026?day=all) · [筛选底册](papers.tsv)

CVF Open Access 主会目录含 4,042 个不同的论文页面。已筛选 927 篇，其中 602 篇暂收录、325 篇排除，另有 3,115 篇待筛。最终按贡献指南统一排名，收录上限为 50%。

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
| 机器人学 | 表征学习 | [ConceptPose: Training-Free Zero-Shot Object Pose Estimation using Concept Vectors](cards.md#paper-conceptpose) | 无对象专用训练时，检验开放词汇概念显著向量能否替代外观特征作跨视角三维对应。见表 1–3。 |
| 多模态学习 | 强化学习方法 | [JoPPO: Hierarchical Photography Assessment via Contrastive Joint Conditional Probabilistic Reinforcement Learning](cards.md#paper-joppo) | 多属性视觉评分可按各属性条件下的总分胜率给强化学习信号，而不是直接优化一个整体分。见表 3–4。 |
| 机器学习基础与统计 | 损失函数 | [Functional Mean Flow in Hilbert Space](cards.md#paper-functional-mean-flow) | 不规则坐标或多分辨率函数生成需要单步采样时，可对照 Hilbert 空间 Mean Flow 的终点预测与速度预测。见函数域构造和表 3–4。 |
| 机器人学 | 训练策略 | [CausalVAD: De-confounding End-to-End Autonomous Driving via Causal Intervention](cards.md#paper-causalvad-shortcut-intervention) | 动作策略训练应对速度等容易形成捷径的输入做分桶和反事实扰动，并比较上下文原型干预前后退化。见表 2–5。 |
| 机器学习基础与统计 | 训练策略 | [AdaBet: Gradient-free Layer Selection for Efficient Training of Deep Neural Networks](cards.md#paper-adabet) | 端侧适配前可先用无标签前向激活的拓扑特征挑选待训练层，避免完整反传才能决定选哪些层。见表 2–3。 |
| 计算机视觉 | 优化 | [Dual Ascent Diffusion for Inverse Problems](cards.md#paper-dual-ascent-diffusion) | 扩散先验求逆问题时，分别消融观测一致性的对偶变量及噪声步骤，避免把所有收益归因于去噪器。见 §3、表 2。 |
| 多模态学习 | 表征学习 | [One Patch to Caption Them All: A Unified Zero-Shot Captioning Framework](cards.md#paper-patch-ioner) | 开放词汇区域描述可先在对齐空间聚合局部 patch，再用同一解码器描述离散区域或轨迹。见表 1–2。 |
| 计算机视觉 | 模型架构 | [Masked Region Transformer for Layered Image Generation and Editing at Scale](cards.md#paper-masked-region-transformer-layer-editing) | 独立透明图层的生成、分解和局部编辑可用同一条件掩码参数化；任务混训比例要验证负迁移。见表 2–3。 |
| 多模态学习 | 模型架构 | [Grounded 3D-Aware Spatial Vision-Language Modeling](cards.md#paper-gr3d) | 先落到图像区域再做三维推断，并将区域词元接回文本推理。 |
| 多模态学习 | 量化推理 | [Fine-Grained Post-Training Quantization for Large Vision Language Models with Quantization-Aware Integrated Gradients](cards.md#paper-qig-ptq) | 用实际量化误差归因逐词元校准，检查模态标签是否足以反映量化敏感度。 |
| 多模态学习 | 训练策略 | [Dr. Seg: Revisiting GRPO Training for Visual Large Language Models through Perception-Oriented Design](cards.md#paper-dr-seg) | 把尝试定位后的视觉确认和稳定排序奖励作为可分离因素，检验语言推理式 GRPO 能否迁移到感知。 |
| 机器学习基础与统计 | 训练策略 | [GR-Gauge: Cost-efficient Training Configuration By Gauging the Gradient Redundancy](cards.md#paper-gr-gauge) | 按跨样本与跨更新两种梯度冗余估计学习率和批大小，验证能否降低搜索开销。 |
| 计算机视觉 | 模型架构 | [DROID-SLAM in the Wild](cards.md#paper-droid-w) | 用多视特征不一致估计几何观测的不确定度，直接降低不可靠像素在位姿优化中的权重。 |
| 多模态学习 | 训练策略 | [Towards Robust Multi-Modal Semantic Segmentation with Teacher-Student Framework and Hybrid Prototype Distillation](cards.md#paper-robustseg) | 缺失模态训练分开蒸馏共享语义和模态专属变化，并验证弱模态反馈方向。 |
| 计算机视觉 | 模型架构 | [Kontinuous Kontext: Continuous Strength Control for Instruction-based Image Editing](cards.md#paper-kontinuous-kontext) | 将编辑强度映射到模型调制空间，直接对照在文本嵌入或成图之间做插值。 |
| 多模态学习 | 模型架构 | [RAYNOVA: Scale-Temporal Autoregressive World Modeling in Ray Space](cards.md#paper-raynova) | 在统一射线坐标中按尺度和时间联合自回归，避免相机换位时复用固定视图索引。 |
| 计算机视觉 | 测试时适应与推理 | [SPEGC: Continual Test-Time Adaptation via Semantic-Prompt-Enhanced Graph Clustering for Medical Image Segmentation](cards.md#paper-spegc) | 持续域漂移时先构造稳健图，再以簇级一致性更新决策边界。 |
| 计算机视觉 | 模型架构 | [ExtrinSplat: Decoupling Geometry and Semantics for Open-Vocabulary Understanding in 3D Gaussian Splatting](cards.md#paper-extrinsplat) | 把空间几何和可多义的对象语义分开存，语义可以多粒度重建索引。 |
| 多模态学习 | 训练策略 | [Vocabulary Scaling Law: Tuning Open-vocabulary Predictors for Their Openness](cards.md#paper-svft) | 按子模覆盖挑选训练类之外的词表进行微调，随词表扩大验开放性。 |
| 多模态学习 | 训练策略 | [The Consistency Critic: Correcting Inconsistencies in Generated Images via Reference-Guided Attentive Alignment](cards.md#paper-imagecritic) | 训练参考校正器时用可控降质作监督，并分开核对布局与细节。 |
| 多模态学习 | 训练策略 | [StyleDoctor: Towards Specialist Reward Model for Style-centric Generation Tasks](cards.md#paper-styledoctor) | 需要风格时单独学习奖励并把图图风格对应和图文风格对齐分验。 |
| 多模态学习 | 可解释性 | [Where Does Vision Meet Language? Understanding and Refining Visual Fusion in MLLMs via Contrastive Attention](cards.md#paper-contrastive-attention-fusion) | 逐层屏蔽视觉再做末层对照，定位真正参与融合的层及无关注意噪声。 |
| 计算机视觉 | 模型架构 | [From Events to Clarity: The Event-Guided Diffusion Framework for Dehazing](cards.md#paper-evdehaze) | 把高动态事件边缘作为独立生成条件，按无事件和无跨注意分别量化。 |
| 多模态学习 | 强化学习 | [Taming Preference Mode Collapse via Directional Decoupling Alignment in Diffusion Reinforcement Learning](cards.md#paper-d2-align) | 对生成偏好奖励的偏置方向单独校正，分开监测奖励增益与多样性。 |
| 多模态学习 | 推理压缩 | [DocPrune: Efficient Document Question Answering via Background, Question, and Comprehension-aware Token Pruning](cards.md#paper-docprune) | 先裁文档背景，再按问题挑证据，最后依模型理解程度调起始层。 |
| 机器学习基础与统计 | 表征学习 | [POUR: A Provably Optimal Method for Unlearning Representation via Neural Collapse](cards.md#paper-pour-representation-unlearning) | 类别遗忘验收应分别检查输出、可恢复表征和保留类结构；神经坍塌近似成立时再比较投影与蒸馏。见定理 4.2 和表 1。 |
| 计算机视觉 | 推理策略 | [FlowMotion: Training-Free Flow Guidance for Video Motion Transfer](cards.md#paper-flowmotion) | 无训练视频运动迁移可直接用早期潜预测构造时间引导，并分开消融速度正则。见表 1、3–4。 |
| 多模态学习 | 训练策略 | [Skyra: AI-Generated Video Detection via Grounded Artifact Reasoning](cards.md#paper-skyra-grounded-video-detection) | 合成视频检测应将判断依据作为带人工标注的中间监督，并分别比较二分类和解释训练。见表 3–4。 |
| 计算机视觉 | 表征学习 | [LATTICE: Democratize High-Fidelity 3D Generation at Scale](cards.md#paper-lattice-voxset) | 三维资产生成可给压缩潜令牌绑定粗体素位置再生成精细几何，分别检查同分布重建和稀疏锚推理差异。见图 10、表 1–3。 |
| 计算机视觉 | 表征学习 | [A Frame is Worth One Token: Efficient Generative World Modeling with Delta Tokens](cards.md#paper-deltaworld-delta-tokens) | 多未来世界模型可压缩相邻冻结视觉表示的差值，再对均值和最佳样本同时验收，避免奖励随机发散。见表 2–3。 |
| 多模态学习 | 推理策略 | [Harmony: Harmonizing Audio and Video Generation through Cross-Task Synergy](cards.md#paper-harmony-synccfg) | 音视频联合扩散可把跨模态时间对齐引导与各模态的条件引导分开，并以同步指标独立消融。见 §3.4、表 3。 |
| 计算机视觉 | 模型架构 | [MAMMA: Markerless Accurate Multi-person Motion Acquisition](cards.md#paper-mamma) | 用逐人掩码及可见性约束密集表面对应，优先解决互相遮挡中的身份串扰。 |
| 计算机视觉 | 模型架构 | [Dual Graph Regularized Deep Unfolding Network for Guided Depth Map Super-resolution](cards.md#paper-lapnet) | 分别编码导引图像结构和深度本身的结构，再将图正则求解展开成可训练迭代。 |
| 计算机视觉 | 训练策略 | [Towards Robust Vision Transformers: Path Dependency Analysis and a Simple Two-Stage Adversarial Training](cards.md#paper-vit-robustness-paths) | 防御训练中分别审计残差通路与变换通路，验证统一扰动训练是否损伤早期表征。 |
| 计算机视觉 | 训练策略 | [First Frame Is the Place to Go for Video Content Customization](cards.md#paper-ffgo) | 把视频模型首帧当作视觉实体记忆，可用少量示例训练模型复用其中实体。 |
| 计算机视觉 | 模型架构 | [High-Quality and Efficient Turbulence Mitigation with Events](cards.md#paper-ehetm) | 把事件极性交替当作边缘线索、事件方向用于去除扰动运动，在同等时延下比较帧序列重建。 |
| 计算机视觉 | 模型架构 | [Bidirectional Query-Driven Generation of Parametric CAD Sketch](cards.md#paper-cadsketcher) | 将草图续写改为缺口两侧的候选扩展，并用执行检查决定保留方向。 |
| 计算机视觉 | 数据与评测 | [Illustrator's Depth: Monocular Layer Index Prediction for Image Decomposition](cards.md#paper-illustrators-depth) | 编辑任务使用离散图层次序而不是物理深度，用可编辑渲染检验分解。 |
| 机器学习基础与统计 | 训练策略 | [On the Role of Temporal Granularity in the Robustness of Spiking Neural Networks](cards.md#paper-tg-reg) | 按时间步监测脉冲网络敏感度并正则不稳定步，同时保留干净准确率验收。 |
| 计算机视觉 | 模型架构 | [SRGCD: Stability-Driven Region Growth Framework for 3D Change Detection](cards.md#paper-srgcd) | 变化检测从可信种子生长连通区域，再显式约束边界。 |
| 多模态学习 | 模型架构 | [MoCoDiff: A Controllable Autoregressive Diffusion Model for Expressive Motion Generation](cards.md#paper-mocodiff) | 冻结动作生成骨干时分开注入文本、风格及历史，对历史采用时步相关校正。 |
| 机器人学 | 模型架构 | [SHARP: Short-Window Streaming for Accurate and Robust Prediction in Motion Forecasting](cards.md#paper-sharp) | 流式轨迹预测按主体更新记忆，并联合训练不同历史长度。 |
| 机器学习基础与统计 | 训练策略 | [Dual-Estimator: Decoupling Global and Local Semantic Shift for Drift Compensation in Class-Incremental Learning](cards.md#paper-dual-e) | 无回放增量学习把局部语义漂移和类级全局变化分开校正。 |
| 计算机视觉 | 模型架构 | [SAM 3D Body: Robust Full-Body Human Mesh Recovery](cards.md#paper-sam-3d-body) | 人体网格模型用骨骼与表面解耦的身体表示，并把二维提示用于难例修正。 |
| 计算机视觉 | 训练策略 | [Boosting Quantitive and Spatial Awareness for Zero-Shot Object Counting](cards.md#paper-qica) | 开放词汇计数直接处理图文相似度图，并让不同读出层的总量一致。 |
| 多模态学习 | 评测与诊断 | [GuardTrace-VL: Detecting Unsafe Multimodel Reasoning via Iterative Safety Supervision](cards.md#paper-guardtrace-vl) | 多模态审核可分别检查推理过程与最终回答，并对照仅提供图片描述的文本审核器。见表 1–2。 |
| 计算机视觉 | 损失函数 | [SPAN: Spatial-Projection Alignment for Monocular 3D Object Detection](cards.md#paper-span-staged-geometric-alignment) | 对解耦回归头加整体几何损失时，应在低阶属性学稳后逐步启用，并对比一开始就启用的方案。见 §3.4、表 3–4。 |
| 多模态学习 | 理论与统计 | [Is the Modality Gap a Bug or a Feature? A Robustness Perspective](cards.md#paper-modality-gap-robustness) | 视觉语言模型做低精度部署前，可用零样本基线检验沿模态均值方向缩小间隔是否保留干净准确率并改善扰动稳定性。见定理 3.4–3.5、图 8–9。 |
| 机器学习基础与统计 | 数据策略 | [Federated Active Learning Under Extreme Non-IID and Global Class Imbalance](cards.md#paper-fairfal-local-global-querying) | 联邦主动学习先按全局长尾与客户端异质性分别测本地和全局询标器，避免固定选全局模型。见观察 1、表 1–3。 |
| 机器人学 | 训练策略 | [Explore with Long-term Memory: A Benchmark and Multimodal LLM-based Reinforcement Learning Framework for Embodied Exploration](cards.md#paper-lmee-memory-retrieval-training) | 长程探索应分别训练和测量记忆检索与导航，使用不同问答监督检查哪类记忆任务真正提升行动。见表 4。 |
| 多模态学习 | 损失函数 | [Multi-Modal Image Fusion via Intervention-Stable Feature Learning](cards.md#paper-intervention-stable-modal-fusion) | 多模态融合训练应分别测试互补、共同缺失与整模态缺失，用独立约束衡量稳定性及模态必要性。见 §3、表 2。 |
| 计算机视觉 | 训练策略 | [Dark3R: Learning Structure from Motion in the Dark](cards.md#paper-dark3r) | 用配对曝光训练低信噪比几何模型，在没有三维训练标签时迁移干净图像的匹配信号。 |
| 计算机视觉 | 模型架构 | [Efficient and Training-Free Single-Image Diffusion Models](cards.md#paper-single-image-patch-diffusion) | 单图生成可用多尺度图块经验分布构造闭式去噪器，替换逐图训练。 |
| 计算机视觉 | 模型架构 | [OSA: Echocardiography Video Segmentation via Orthogonalized State Update and Anatomical Prior-aware Feature Enhancement](cards.md#paper-osa) | 监控线性循环记忆秩，并考虑以正交状态更新抵消长序列衰减。 |
| 计算机视觉 | 训练策略 | [Detecting Compressed AI-Generated Images via Phase Spectrum Robustness](cards.md#paper-compression-phase-detection) | 防御性合成图检测可将不同图像质量分层验收，并测阶段频谱线索是否保持。 |
| 机器学习基础与统计 | 模型架构 | [Tunable Soft Equivariance with Guarantees](cards.md#paper-tunable-soft-equivariance) | 用可调权重投影平衡对称误差与原始任务性能，避免在数据近似对称时硬性约束。 |
| 计算机视觉 | 优化算法 | [Generalized-CVO: Fast and Correspondence-Free Local Point Cloud Registration with Second Order Riemannian Optimization](cards.md#paper-generalized-cvo) | 将点云核的法向和切向灵敏度分开，并在相同目标下比较一阶与二阶流形求解。 |
| 多模态学习 | 模型架构 | [MultiAnimate: Pose-Guided Image Animation Made Extensible](cards.md#paper-multianimate) | 为每个角色分配显式标识和遮挡位置，用少角色训练外推多角色。 |
| 多模态学习 | 评测与诊断 | [Exposing and Evaluating Hallucinations for GUI Grounding](cards.md#paper-gui-hallubench) | GUI 定位区分点错现有控件和凭空定位不存在控件。 |
| 计算机视觉 | 模型架构 | [Beyond Sequential Tools: A Unified VLM Agent System for Photographic Post-Processing via Dynamic Multi-Expert Fusion](cards.md#paper-dynamic-expert-restoration) | 对复合退化一次融合专家，用独立 K/V 适配替代逐个工具执行。 |
| 计算机视觉 | 模型架构 | [ReAttnCLIP: Training-Free Open-Vocabulary Remote Sensing Image Segmentation via Re-defined Attention in CLIP](cards.md#paper-reattnclip) | 冻结 CLIP 时按局部关系与类定位分别替换注意力来源。 |
| 机器人学 | 评测与诊断 | [LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models](cards.md#paper-libero-plus) | 操作策略上线评测加入可复现单轴扰动，测正常与扰动成功率差。 |
| 计算机视觉 | 训练策略 | [AnyLift: Scaling Motion Reconstruction from Internet Videos via 2D Diffusion](cards.md#paper-anylift) | 难动作缺三维数据时先扩增多视二维轨迹，再用相机条件扩散提升到世界坐标。 |
| 多模态学习 | 推理优化 | [Accelerating Diffusion via Hybrid Data-Pipeline Parallelism Based on Conditional Guidance Scheduling](cards.md#paper-hybridiff) | 将有条件和无条件导引先映射到两设备，再按去噪差异切换流水调度。 |
| 多模态学习 | 训练策略 | [UniVerse: Empower Unified Generation with Reasoning and Knowledge](cards.md#paper-universe) | 把隐含请求转成明确视觉描述作为中间监督，比较需要和不需要推理链的配方。 |
| 计算机视觉 | 评测与诊断 | [Inside-Out: Measuring Generalization in Vision Transformers Through Inner Workings](cards.md#paper-inside-out-vit-generalization) | 目标域无标签时，比较内部依赖结构与置信度作为选模代理，并将部署后漂移单独校准。见表 1、3。 |
| 计算机视觉 | 训练策略 | [Building Robust Vision Encoders for Cross-Dataset Evaluation in Immunofluorescent Microscopy](cards.md#paper-c3r-variable-sensor-channels) | 针对设备通道配置不统一的视觉编码，可区分稳定参考与变化观测，训练时做掩蔽蒸馏，并用从未见过的通道组合验收。见表 1–3。 |
| 机器学习基础与统计 | 模型架构 | [Gated KalmaNet: A Fading Memory Layer through Test-time Ridge Regression](cards.md#paper-gated-kalmanet) | 低精度长序列状态层若用在线岭回归，应对条件数做输入相关正则，并把实际召回和合成任务测开。见表 2、图 3。 |
| 计算机视觉 | 模型架构 | [The Missing Point in Vision Transformers for Universal Image Segmentation](cards.md#paper-vit-p-point-mask-classification) | 现有分割器的掩码几何已足够时，可用点级 ViT 对候选掩码再分类，并对照粗注释和精细掩码。见表 4。 |
| 计算机视觉 | 模型架构 | [Reviving ConvNeXt for Efficient Convolutional Diffusion Models](cards.md#paper-fcdm-convolutional-diffusion) | 做固定训练资源的图像扩散时，应把条件化 ConvNeXt 纳入骨干对照，分别看迭代数、单步 FLOPs 和吞吐。见表 2–4。 |
| 计算机视觉 | 训练策略 | [DetAny4D: Detect Anything 4D Temporally in a Streaming RGB Video](cards.md#paper-detany4d-temporal-box-stability) | 流式三维检测的训练应以跨帧抖动单独验收几何辅助头，避免仅按每帧 AP 选择模型。见表 3。 |
| 多模态学习 | 推理压缩 | [Rethinking Token Reduction for Large Vision-Language Models](cards.md#paper-metacompress) | 跨轮视觉问答应在未知后续问题的情况下学习压缩，按轮检查信息丢失。 |
| 多模态学习 | 评测与诊断 | [CaptionQA: Is Your Caption as Useful as the Image Itself?](cards.md#paper-captionqa) | 同题分别用图像和描述作输入，用分域问答差值决定是否能把图像替换成文本。 |
| 多模态学习 | 训练策略 | [Dynamics-Aware Preference Optimization for Vision-Language Models](cards.md#paper-cw-dpo) | 偏好训练即使易负例损失很低，也应审计其梯度，通过能力相关权重减少无信息更新。 |
| 计算机视觉 | 推理策略 | [FlowDC: Flow-Based Decoupling-Decay for Complex Image Editing](cards.md#paper-flowdc) | 并行叠加多个编辑方向，并独立抑制造成源结构偏移的正交速度。 |
| 多模态学习 | 训练策略 | [PDCR: Perception-Decomposed Confidence Reward for Vision-Language Reasoning](cards.md#paper-pdcr) | 用视觉依赖划分感知和文字推理，在各类内部标准化同一个信心增长奖励。 |
| 计算机视觉 | 训练策略 | [MeanFlow Transformers with Representation Autoencoders](cards.md#paper-mf-rae) | 少步生成更换潜表示后应先检验梯度稳定性，再决定从轨迹初始化还是直接训练。 |
| 多模态学习 | 推理优化 | [CLAY: Conditional Visual Similarity Modulation in Vision-Language Embedding Space](cards.md#paper-clay) | 固定图像索引后，以查询文字改变相似度定义，避免为每种条件重建索引。 |
| 机器学习基础与统计 | 训练策略 | [The Surprising Effectiveness of Noise Pretraining for Implicit Neural Representations](cards.md#paper-noise-pretraining-inr) | 缺领域数据时按任务选择无结构或自然频谱噪声预训练，分开验拟合和逆问题。 |
| 计算机视觉 | 训练策略 | [Learning from Semantic Dictionaries: Discriminative Codebook Contrastive Learning for Unified Visual Representation and Generation](cards.md#paper-lease) | 将生成字典的细节重建与判别字典的语义对齐作为可独立验收目标。 |
| 计算机视觉 | 模型架构 | [ZipMap: Linear-Time Stateful 3D Reconstruction via Test-Time Training](cards.md#paper-zipmap) | 将多视重建压入可查询隐状态，使一次前向和流式累计共享表示。 |
| 机器人学 | 训练策略 | [SGDrive: Scene-to-Goal Hierarchical World Cognition for Autonomous Driving](cards.md#paper-sgdrive) | 驾驶规划监督分场景、主体和局部目标，并显式消融未来状态。 |
| 计算机视觉 | 模型架构 | [OnlinePG: Online Open-Vocabulary Panoptic Mapping with 3D Gaussian Splatting](cards.md#paper-onlinepg) | 在线语义地图从局部成实例，再以双向匹配更新全局身份。 |
| 多模态学习 | 推理优化 | [Are Image-to-Video Models Good Zero-Shot Image Editors?](cards.md#paper-if-edit) | 以视频运动先验执行静态图难以描述的编辑，再选帧并修复锐度。 |
| 多模态学习 | 模型架构 | [PyraTok: Language-Aligned Pyramidal Tokenizer for Video Understanding and Generation](cards.md#paper-pyratok) | 视频词元跨时空尺度共用码本，同时验重建和语言下游。 |
| 计算机视觉 | 模型架构 | [RT-Splatting: Joint Reflection-Transmission Modeling with Gaussian Splatting](cards.md#paper-rt-splatting) | 把高斯的几何占据和光学透明度分开，并按反光程度限制跨支路误梯度。 |
| 机器人学 | 训练策略 | [From Observation to Action: Latent Action-based Primitive Segmentation for VLA Pre-training in Industrial Settings](cards.md#paper-laps) | 无标人演示以潜动作能量切分，允许和光流边界做等标签对照。 |
| 多模态学习 | 推理策略 | [Retrieve and Segment: Are a Few Examples Enough to Bridge the Supervision Gap in Open-Vocabulary Segmentation?](cards.md#paper-retrieve-and-segment) | 当像素标注只有几例时，以查询为条件检索并融合视觉支持与类别文本，见图 5、表 1。 |
| 机器人学 | 数据策略 | [Shoe Style-Invariant and Ground-Aware Learning for Dense Foot Contact Estimation](cards.md#paper-feco-contact-style-randomization) | 接触点学习可分别扰动外观风格与接触部件内容，测外观捷径；同时分开评估地面约束。见表 2–4。 |
| 计算机视觉 | 推理策略 | [ShiftLUT: Spatial Shift Enhanced Look-Up Tables for Efficient Image Restoration](cards.md#paper-shiftlut) | 端侧 LUT 图像恢复可用通道位移传递局部信息，并以误差有界采样在表大小、延迟和质量间选点。见表 4 和图 8。 |
| 计算机视觉 | 表征学习 | [NaTex: Seamless Texture Generation as Latent Color Diffusion](cards.md#paper-natex-native-color-diffusion) | 三维纹理可直接在原生表面颜色点上生成，避免跨视角烘焙拼接，再用遮挡区域验收。见 §3.2、表 2 与图 8。 |
| 多模态学习 | 数据策略 | [HoneyBee: Data Recipes for Vision-Language Reasoners](cards.md#paper-honeybee-data-interventions) | 视觉推理训练在扩数据前可比较增加图像描述和纯文本解题，警惕更长思维链或更多干扰项反而降低收益。见表 3。 |
| 计算机视觉 | 推理策略 | [One-Shot Flow, Any-Time Frame: A Bidirectional Warping Framework for Event-Based Video Frame Interpolation](cards.md#paper-one-shot-flow-any-time-frame) | 需要在同一输入区间产出多帧时，先缓存可按时间查询的双向流轨迹，减少每个时刻重复流估计。见表 3–4。 |
| 多模态学习 | 表征学习 | [RI-Mamba: Rotation-Invariant Mamba for Robust Text-to-Shape Retrieval](cards.md#paper-ri-mamba-point-ordering) | 对任意旋转点云可先在局部坐标建立稳定序列，再以独立分支回注方向信息，见 §4.5 和表 5。 |
| 多模态学习 | 强化学习方法 | [PointThinker: Point-Incentivized Parallel Thinking for Multimodal Large Language Model](cards.md#paper-pointthinker-pointwise-credit) | 并行视觉推理可按视觉关键点分支，并对同一整条轨迹内各点分配不同奖励。见表 3–4。 |
| 计算机视觉 | 损失函数 | [Balanced Hierarchical Contrastive Learning with Decoupled Queries for Fine-grained Object Detection in Remote Sensing Images](cards.md#paper-balanced-hierarchical-contrast) | 对层次类别按批次均衡梯度，并将层次语义学习与定位查询解耦。 |
| 计算机视觉 | 推理策略 | [A Training-Free Style-Personalization via SVD-Based Feature Decomposition](cards.md#paper-svd-style-personalization) | 用逐生成尺度的奇异值诊断选择风格注入位置，细尺度单独验结构。 |
| 计算机视觉 | 训练策略 | [Beyond the Ground Truth: Enhanced Supervision for Image Restoration](cards.md#paper-frequency-mixup-supervision) | 修复训练标签本身有退化时，分频融合原标签与超分版本，并独立验细节真实性。 |
| 多模态学习 | 训练策略 | [SineProject: Machine Unlearning for Stable Vision-Language Alignment](cards.md#paper-sineproject) | 进行防御性遗忘时监控跨模态投影器条件数，并把无关正常查询误拒纳入验收。 |
| 大语言模型 | 训练策略 | [Unlocking Token Rewards via Training-Free Reward Attribution](cards.md#paper-p2t-reward-attribution) | 用过程奖励对词元替换的一阶近似提供信用分配，可避免逐词元运行奖励模型。 |
| 科学与医学 AI | 训练与数据策略 | [Delving Aleatoric Uncertainty in Medical Image Segmentation via Vision Foundation Models](cards.md#paper-aleatoric-uncertainty-spectrum) | 用解码特征的奇异值能量估计训练样本难度，决定筛除样本还是逐类调权。 |
| 多模态学习 | 可解释性与诊断 | [Language Models Can Explain Visual Features via Steering](cards.md#paper-visual-feature-steering) | 解释视觉 SAE 特征时，在最高激活示例外加入因果干预来减少共现概念误归因。 |
| 机器人学 | 迁移与泛化 | [PanDA: Unsupervised Domain Adaptation for Multimodal 3D Panoptic Segmentation in Autonomous Driving](cards.md#paper-panda-multimodal-domain-adaptation) | 单传感器退化的目标域适配中，用实例补全修复伪掩码，并模拟模态局部失真。 |
| 机器人学 | 表示学习 | [FreeArtGS: Articulated Gaussian Splatting Under Free-moving Scenario](cards.md#paper-freeartgs) | 从自由移动的 RGB-D 视频识别关节时，先用部件相对运动消去物体全局位姿变化。 |
| 多模态学习 | 模型架构 | [ReCoFuse: Ultra-Robust Image Fusion via Restorative Multi-Modal Diffusion Reciprocal Coupling](cards.md#paper-recofuse) | 单路信号退化的多模态融合中，把跨模态信息反馈给每次恢复迭代，而非只融合最终恢复结果。 |
| 多模态学习 | 可解释性与诊断 | [The Drift Kernel: Why Diffusion Models Change Even When Told Not To](cards.md#paper-diffusion-drift-kernel) | 评价扩散编辑时，先测空编辑漂移并按模型和噪声强度建立身份保真基线。 |
| 多模态学习 | 推理优化 | [Accelerating Autoregressive Video Diffusion via History-Guided Cache and Residual Correction](cards.md#paper-arcache) | 滚动生成视频时，以历史偏差决定每段何时重算，并校正向后传播的残差。 |
| 机器学习基础 | 表示学习 | [HyperNAS: Enhancing Architecture Representation for NAS Predictor via Hypernetwork](cards.md#paper-hypernas) | 昂贵的架构试验样本不足时，用共享超网络作为排序预测器的训练辅助目标。 |
| 计算机视觉 | 损失函数 | [Dehallu3D: Hallucination-Mitigated 3D Generation from a Single Image via Cyclic View Consistency Refinement](cards.md#paper-dehallu3d-cyclic-view-consistency) | 稀疏视角三维生成应联合检查视角间连续性和锐利几何保留，测视角加密收益和耗时。见表 2–3。 |
| 计算机视觉 | 数据策略 | [Does YOLO Really Need to See Every Training Image in Every Epoch?](cards.md#paper-afss-anti-forgetting-sampling) | 检测训练按图像是否已学会动态降频，并优先复看最长未见的易例，见表 3–5。 |
| 机器学习基础与统计 | 训练策略 | [Personalized Federated Training of Diffusion Models with Privacy Guarantees](cards.md#paper-private-personalized-federated-diffusion) | 私有多方生成训练可把共享成分与客户端个性化条件分开，并按少数类别检查隐私约束下的质量。见理论部分、表 1。 |
| 计算机视觉 | 评测与诊断 | [KaLOS finds Consensus: A Meta-Algorithm for Evaluating Inter-Annotator Agreement in Complex Vision Tasks](cards.md#paper-kalos-localization-first-agreement) | 检测或空间标注评估先校准跨标注者的实例对应，再计类别一致性，用人为注入噪声验证指标。见 §4、图 3–6。 |
| 机器学习基础与统计 | 表征学习 | [Rank-Guided Pseudo-Bias Learning for Robust Black-Box Adaptation](cards.md#paper-pld-blackbox-debias) | 只有冻结特征时，可先训练偏差放大探测器构造伪分组，再用最差组验证去偏收益。见表 1、4。 |
| 计算机视觉 | 训练策略 | [Learning What Helps: Task-Aligned Context Selection for Vision Tasks](cards.md#paper-tacs-learned-context-selection) | 可将检索上下文按下游预测收益学习，且须对照重复输入、空输入和相似检索。见表 4–5。 |
| 多模态学习 | 推理策略 | [Breaking the Regional Perception Bottleneck of Multimodal Large Language Models via External Reasoning Framework](cards.md#paper-r-ground-region-search) | 区域定位相比继续扩模型，可对同一骨干测试把额外计算放到搜索局部证据的收益，见表 2–4。 |
| 多模态学习 | 评测与诊断 | [Scaling Spatial Intelligence with Multimodal Foundation Models](cards.md#paper-sensenova-si-spatial-diagnostics) | 扩张空间训练数据时，应同时追踪能力分项，并在去掉视觉或改变视角顺序后复测。 |
| 机器人学 | 模型架构 | [Semantic Audio-Visual Navigation in Continuous Environments](cards.md#paper-savn-ce-magnet) | 为断续声源保留时序记忆并用自运动更新目标方位，按有声和静默分别验收。 |
| 智能体 | 训练策略 | [Training High-Level Schedulers with Execution-Feedback Reinforcement Learning for Long-Horizon GUI Automation](cards.md#paper-ces-execution-feedback) | 长程良性 GUI 自动化可冻结执行器，把训练资源集中在有执行反馈的调度与状态维护。 |
| 计算机视觉 | 推理策略 | [Direct Segmentation without Logits Optimization for Training-Free Open-Vocabulary Semantic Segmentation](cards.md#paper-direct-ovss) | 在开放词表分割中将分布差异作为直接解码信号，对照迭代优化或直接取 logits 最大值。 |
| 计算机视觉 | 训练策略 | [Moving Border Ownership for Event-based Motion Segmentation](cards.md#paper-moving-border-ownership) | 用有符号边界归属场表示运动前景在哪一侧，并控制网络和数据比较二值监督。 |
| 计算机视觉 | 训练策略 | [TGTrack: Temporal Generative Learning for Unified Single Object Tracking](cards.md#paper-tgtrack) | 跟踪模型除跨帧传递状态外，训练时可加入预测未来的生成监督，并与仅时间位置标记比较。 |
| 机器人学 | 损失函数与优化 | [OrienPose: Orientation-Guided Novel View Synthesis for Single-Image Unseen Object Pose Estimation](cards.md#paper-orienpose) | 在合成位姿匹配模板时，为相对视角变换增加同一坐标域里的几何监督。 |
| 多模态学习 | 损失函数与优化 | [What Is It Like to Be a Noise? An Entropy-based Gaussian Noise Regularization for Diffusion Models](cards.md#paper-entropy-based-gaussianity) | 推理时优化扩散初始噪声，用局部熵与跨尺度相关性约束代替只约束噪声范数。 |
| 多模态学习 | 条件生成 | [PhysVid: Physics Aware Local Conditioning for Generative Video Models](cards.md#paper-physvid) | 视频中物理约束随时间变化时，将状态和相互作用描述分段注入注意力。 |
| 机器人学 | 评测与分析 | [Towards Motion Turing Test: Evaluating Human-Likeness in Humanoid Robots](cards.md#paper-motion-turing-test) | 检验人形运动自然度时统一骨架去除外观，按动态动作类别分层，并用人评核对自动评分器。 |
| 计算机视觉 | 表示学习 | [CrossHOI: Learning Cross-View Representations for Monocular 3D Human-Object Interaction Reconstruction](cards.md#paper-crosshoi) | 单目接触估计受遮挡时，生成补充视角的特征并在网格顶点层融合。 |
| 多模态学习 | 模型架构 | [DDT: Decoupled Diffusion Transformer](cards.md#paper-decoupled-diffusion-transformer) | 扩散 Transformer 中将语义编码与速度解码拆开，缓存相邻去噪步可复用的语义条件。 |
| 多模态学习 | 训练与数据策略 | [DiT360: High-Fidelity Panoramic Image Generation via Hybrid Training](cards.md#paper-dit360) | 数据稀缺的周期视觉生成中，将边界周期先验与几何变换一致性同时纳入训练。 |
| 多模态学习 | 推理策略 | [ANTS: Adaptive Negative Textual Space Shaping for OOD Detection via Test-Time MLLM Understanding and Reasoning](cards.md#paper-ants-ood-negative-labels) | 开放集检测应分开构造近域难负标签和远域描述，分别验收误报。见表 4。 |
| 计算机视觉 | 推理策略 | [HTTM: Head-wise Temporal Token Merging for Faster VGGT](cards.md#paper-httm-vggt-headwise-merging) | 多视角注意力合并应允许各头保留不同信息，并在相同令牌长度对照离群信息的保留。见表 2–4。 |
| 计算机视觉 | 推理策略 | [SenCache: Accelerating Diffusion Model Inference via Sensitivity-Aware Caching](cards.md#paper-sencache) | 扩散缓存何时刷新可按去噪器对当前输入的敏感度预估误差，并固定实际函数调用数评估。见表 1。 |
| 机器人学 | 评测与诊断 | [PAI-Bench: A Comprehensive Benchmark For Physical AI](cards.md#paper-pai-bench-physical-grounding) | 物理视频及具身推理验收应分别看视觉逼真、物理约束和预测，把启用思考与不用思考拆开。见表 3–6。 |
| 机器学习基础与统计 | 训练策略 | [Basis-Oriented Low-rank Transfer for Few-Shot and Test-Time Adaptation](cards.md#paper-bolt-spectral-transfer) | 多个同源已微调模型用于新任务时，可重用更新方向而保留独立的可学习尺度，比较直接合并与从头学习低秩方向。见表 1。 |
| 多模态学习 | 模型架构 | [SpatialStack: Layered Geometry-Language Fusion for 3D VLM Spatial Reasoning](cards.md#paper-spatialstack-geometry-layer-injection) | 接入多层三维几何时，比较在视觉端一次融合与逐层接入语言解码器，见表 1–2。 |
| 多模态学习 | 模型架构 | [Hint2Gen: Bridging Understanding and Generation via Code-structured Hints](cards.md#paper-hint2gen) | 把图像推理结果编码成与画面坐标对齐的结构化提示，比只传递文字更容易保留空间约束。 |
| 计算机视觉 | 评测与诊断 | [Goldilocks Test Sets for Face Verification](cards.md#paper-goldilocks-verification-audit) | 防御性核验用受控难例区分身份判别与外观相似性，并限制少数样本反复影响分数。 |
| 计算机视觉 | 模型架构 | [LRDUN: A Low-Rank Deep Unfolding Network for Efficient Spectral Compressive Imaging](cards.md#paper-lrdun) | 将物理重建的秩约束和学习先验的特征宽度分开设定，避免低秩物理模型限制网络容量。 |
| 多模态学习 | 训练策略 | [Exploring Spatial Intelligence from a Generative Perspective](cards.md#paper-gsi-spatial-transfer) | 空间生成监督能迁移到部分理解任务，但可能损伤逻辑，选数据时应按空间能力分项比较。 |
| 多模态学习 | 训练策略 | [The Blind Spot of Adaptation: Quantifying and Mitigating Forgetting in Fine-tuned Driving Models](cards.md#paper-driving-adaptation-forgetting) | 驾驶适配应在同一评测上同时记录专项增益和通用知识遗忘，并比较改权重与运行时路由。 |
| 计算机视觉 | 评测与诊断 | [Investigating Self-Supervised Representations for Audio-Visual Deepfake Detection](cards.md#paper-av-deepfake-representation-audit) | 防御检测先用相同线性探针比较冻结表示，并把同域和域外拆分，避免复杂检测头掩盖表征差距。 |
| 计算机视觉 | 评测与诊断 | [CLP: A Real-World Dataset of Contaminated Lens Protectors for Robust Semantic Segmentation](cards.md#paper-clp-restore-segment-tradeoff) | 真实镜头污染下先分污染类型比较恢复后的分割与直接分割，避免只按恢复质量接入前处理。 |
| 机器人学 | 自监督学习 | [QueryOcc: Query-based Self-Supervision for 3D Semantic Occupancy](cards.md#paper-queryocc) | 训练相机三维占据模型时，用跨帧独立四维查询监督连续占据，减少稠密体素和渲染依赖。 |
| 机器人学 | 条件生成 | [Structure-to-Intensity Diffusion for Adverse-Weather LiDAR Generation](cards.md#paper-structure-to-intensity-diffusion) | 当传感器强度取决于几何时，在每个去噪步先估结构，再让强度分支以该结构为条件。 |
| 多模态学习 | 自监督学习 | [InstAP: Instance-Aware Vision-Language Pre-Train for Spatial-Temporal Understanding](cards.md#paper-instap) | 需要实例指代或时空检索时，在全局图文对齐外用区域和文本提及做对比学习。 |
| 多模态学习 | 评测与分析 | [AV-Reasoner: Improving and Benchmarking Clue-Grounded Audio-Visual Counting for MLLMs](cards.md#paper-av-reasoner) | 给长视频计数模型做诊断时分开测试线索定位和给定线索后的计数，并在外部数据验证语言推理收益。 |
| 多模态学习 | 知识蒸馏 | [WaDi: Weight Direction-aware Distillation for One-step Image Synthesis](cards.md#paper-wadi) | 从多步扩散蒸馏到一步时，根据教师到学生的权重变化选择低秩旋转适配器。 |
| 计算机视觉 | 条件生成 | [VIAFormer: Voxel-Image Alignment Transformer for High-Fidelity Voxel Refinement](cards.md#paper-viaformer) | 修复已有粗三维表示时，使生成轨迹从受损潜变量直接走向干净目标，并显式对齐校准图像。 |
| 计算机视觉 | 表示学习 | [MV-TAP: Tracking Any Point in Multi-View Videos](cards.md#paper-mv-tap) | 多相机追踪遇到遮挡时，将相机几何作为跨视角注意力的约束，联合更新轨迹和可见性。 |
| 计算机视觉 | 优化 | [MHopReg: Efficient Hierarchical Multi-Hop Graph Search for Point Cloud Registration](cards.md#paper-mhopreg) | 低重叠点云存在分散内点时，比较簇平衡种子及分层多跳扩张和穷举全局搜索。见图 5、表 4。 |
| 计算机视觉 | 模型架构 | [PPISP: Physically-Plausible Compensation and Control of Photometric Variations in Radiance Field Reconstruction](cards.md#paper-ppisp-photometric-reconstruction) | 多视角重建宜把传感器固有偏差与拍摄条件变化分开估计，并在未知目标视图单独测试光度控制。见表 1–2。 |
| 计算机视觉 | 表征学习 | [EVATok: Adaptive Length Video Tokenization for Efficient Visual Autoregressive Generation](cards.md#paper-evatok-adaptive-video-token-budget) | 视频生成可按时间块分配不同离散词元长度，再测等生成骨干下的质量与成本。见表 1–3。 |
| 机器人学 | 训练策略 | [End-to-End Language-Action Model for Humanoid Whole Body Control](cards.md#paper-sentinel-language-action-history) | 语言驱动全身控制应把语义对齐与动作执行成功分开验收，并在固定骨干上对照本体观测时窗。见表 2–3。 |
| 计算机视觉 | 优化 | [Self-Diffusion Driven Blind Imaging](cards.md#paper-deblursdi-blind-self-diffusion) | 未知成像退化下，可测试同一观测自扩散同时更新图像与核，作为预训练恢复先验的对照。见表 4。 |
| 计算机视觉 | 推理策略 | [Delta Rectified Flow Sampling for Text-to-Image Editing](cards.md#paper-drfs-path-aware-editing) | 无需反演的流编辑可独立调整源目标轨迹位移，并分别检查保背景和改语义；见表 1–2。 |
| 机器人学 | 评测与诊断 | [EgoProx: Evaluating MLLMs on Egocentric 3D Proximity Reasoning Across a Cognitive Hierarchy](cards.md#paper-egoprox-transfer-diagnostic) | 具身空间推理微调须区分一阶接近判断和多步动作链，跨子任务对照迁移与遗忘。见表 3–4。 |
| 计算机视觉 | 模型架构 | [IDESplat: Iterative Depth Probability Estimation for Generalizable 3D Gaussian Splatting](cards.md#paper-idesplat-iterative-depth) | 前馈高斯重建遇到单次跨视图对齐不可靠时，比较迭代深度候选和多次匹配置信连乘。见表 5–6。 |
| 计算机视觉 | 模型架构 | [LacTokGen: Latent Consistency Tokenizer for 1024-pixel Image Generation by 256 Tokens](cards.md#paper-lactok) | 压低视觉词元数时可用一步或两步一致性解码器支持直接像素监督，检查保真是否受解码器瓶颈限制。 |
| 机器人学 | 模型架构 | [ForeHOI: Feed-forward 3D Object Reconstruction from Daily Hand-Object Interaction Videos](cards.md#paper-forehoi) | 严重遮挡时可以让二维遮罩补全与三维形状补全交换信息，再与独立重建比较。 |
| 计算机视觉 | 训练策略 | [Learning Generalizable 3D Medical Image Representations from Mask-Guided Self-Supervision](cards.md#paper-mass-mask-guided-ssl) | 用无需语义类别的区域掩码做上下文分割预训练，可测试不完美结构伪标签能否支持少样本迁移。 |
| 计算机视觉 | 训练策略 | [Toward Diffusible High-Dimensional Latent Spaces: A Frequency Perspective](cards.md#paper-freqwarm) | 潜空间越大未必越适合生成，先拆开测频带的编码覆盖和解码依赖，再以高频热身调整训练。 |
| 计算机视觉 | 推理策略 | [Suppressing Non-Semantic Noise in Masked Image Modeling Representations](cards.md#paper-soap-mim-artifacts) | 用无语义输入估计表征中的伪影方向，并在冻结骨干上先做投影对照。 |
| 多模态学习 | 推理优化 | [CORE: Compact Object-centric REpresentations as a New Paradigm for Token Merging in LVLMs](cards.md#paper-core-object-token-merging) | 压缩视觉 token 时按对象掩码合并，并用对象质心恢复合并后序列的空间顺序。 |
| 科学与医学 AI | 表示学习 | [Harmonized Feature Conditioning and Frequency-Prompt Personalization for Multi-Rater Medical Segmentation](cards.md#paper-frequency-prompt-multi-rater-segmentation) | 多标注者分割中降除扫描差异，同时显式用频域提示保存标注者的边界偏好。 |
| 计算机视觉 | 表示学习 | [Velox: Learning Representations of 4D Geometry and Appearance](cards.md#paper-velox-4d-representation) | 压缩动态物体点云时，用时变表面与可渲染外观两条监督共同训练一组 4D token。 |
| 机器人学 | 推理优化 | [TRM-VLA: Temporal-Aware Chain-of-Thought Reasoning and Memorization for Vision-Language-Action Models](cards.md#paper-trm-vla) | 机器人滚动决策时，仅在任务进展关键帧触发推理，并按粒度检索历史推理状态。 |
| 机器学习基础 | 可解释性与诊断 | [Make it SING: Analyzing Semantic Invariants in Classifiers](cards.md#paper-sing-classifier-invariants) | 审计分类器特征时，通过读出层零空间区分已表征的属性与最终分类采用的属性。 |
| 计算机视觉 | 可解释性与诊断 | [PRISM: Prototype-based Reasoning with Inter-modal Semantic Mining for Interpretable Image Recognition](cards.md#paper-prism-semantic-prototypes) | 让细粒度分类的部件原型对齐文本相关区域，并用紧致性约束减少原型重复。 |
| 多模态学习 | 表示学习 | [Aligning Text, Images and 3D Structure Token-by-Token](cards.md#paper-kyvo-3d-token-alignment) | 把结构化三维场景加入多模态语言模型时，分别选对象形状和位姿的离散粒度，并以重建辅助目标检验。 |
| 计算机视觉 | 评测与分析 | [Event Structural Valley: A Unified Theoretical and Practical Framework for Event Camera Autofocus](cards.md#paper-event-structural-valley) | 事件相机扫描焦距时，找两峰之间的事件率谷，而非将事件率峰值当焦点。 |
| 多模态学习 | 损失函数与优化 | [Linking Perception, Confidence and Accuracy in MLLMs](cards.md#paper-confidence-driven-visual-reasoning) | 多模态推理训练用清晰与扰动图像的配对置信奖励，推理时按置信度分配验证预算。 |
| 计算机视觉 | 表征学习 | [BiMotion: B-spline Motion for Text-guided Dynamic 3D Character Generation](cards.md#paper-bimotion-spline-motion) | 变长三维动作可用固定数量 B 样条控制点做生成表示，在同容量下单测连续时域重建。见图 5、表 2。 |
| 计算机视觉 | 评测与诊断 | [AVA-Bench: Atomic Visual Ability Benchmark for Vision Foundation Models](cards.md#paper-ava-bench-atomic-abilities) | 选视觉骨干时可保持语言头和训练任务分布一致，拆测单项能力，并用给定框的对照定位复合任务瓶颈。见图 5–8。 |
| 计算机视觉 | 训练策略 | [MacTok: Robust Continuous Tokenization for Image Generation](cards.md#paper-mactok-mask-alignment) | 极少连续图像词元容易后验坍塌，可混合随机与语义遮盖并同时验收重建与下游生成。见表 4–5。 |
| 计算机视觉 | 数据策略 | [JRM: Joint Reconstruction Model for Multiple Objects without Alignment](cards.md#paper-jrm-negative-support-reconstruction) | 跨观测联合重建的支持项可能匹配错误，训练时应混入一定比例错配组合，并单独测误匹配和正确匹配两类表现。见表 5。 |
| 机器学习基础与统计 | 训练策略 | [MOMO: Mars Orbital MOdel Foundation Model for Mars Orbital Applications](cards.md#paper-momo-validation-loss-checkpoint-alignment) | 跨传感器权重合并可比较按验证损失匹配收敛阶段与直接用各自末次或早停检查点。见表 2。 |
| 多模态学习 | 模型架构 | [LLaDA-V: Large Language Diffusion Models with Visual Instruction Tuning](cards.md#paper-llada-v-attention-mask-tradeoff) | 多模态扩散语言模型先在同数据和骨干下消融对话因果掩码与双向注意力，再测有效并行增益。见表 3–4。 |
| 计算机视觉 | 推理策略 | [C-GenReg: Training-Free 3D Point Cloud Registration by Multi-View-Consistent Geometry-to-Image Generation with Probabilistic Modalities Fusion](cards.md#paper-c-genreg) | 几何与生成图像两路先各自匹配再融置信，不在特征层提前混合。 |
| 计算机视觉 | 模型架构 | [LiDAR Prompted Spatio-Temporal Multi-View Stereo for Autonomous Driving](cards.md#paper-drivemvs) | 把稀疏度量观测分别作为代价体的几何锚和软特征，独立检验尺度精度与跨帧稳定性。 |
| 智能体 | 训练策略 | [LongVideo-R1: Smart Navigation for Low-cost Long Video Understanding](cards.md#paper-longvideo-r1) | 给逐步缩窄长视频检索范围的代理加入证据定位奖励，用同一问答测试检查额外导航监督。 |
| 计算机视觉 | 训练策略 | [Zero-Shot Image Denoising via Hybrid Prior-Guided Pseudo Sample Generation](cards.md#paper-zs-hpd) | 单张图像的零样本复原可同时构造局部邻域对与全局自相似对，按噪声强度做失效对照。 |
| 多模态学习 | 损失函数与优化 | [When Local Rules Create Global Order: Self-Organized Representation Learning for Latent Diffusion Models](cards.md#paper-sorl-latent-diffusion) | 训练扩散模型的自编码器时同时检验邻近重建平滑性与潜变量分散度。 |
| 计算机视觉 | 表示学习 | [MeshFlow: Efficient Artistic Mesh Generation via MeshVAE and Flow-based Diffusion Transformer](cards.md#paper-meshflow) | 生成拓扑离散、坐标连续的网格时，先学共享潜变量，再选择并行流生成替代顶点序列生成。 |
| 多模态学习 | 推理优化 | [ReMoRa: Multimodal Large Language Model based on Refined Motion Representation for Long-Video Understanding](cards.md#paper-remora-compressed-motion) | 长视频问答用稀疏 RGB 取外观、压缩码流运动取动态，避免解码全部帧。 |
| 机器人学 | 表示学习 | [Seeing without Pixels: Perception from Camera Trajectories](cards.md#paper-camformer) | 视频行为检索或具身轨迹学习中，将相机位姿序列对齐文本，并用轨迹单模态作旁路基线。 |
| 多模态学习 | 训练与数据策略 | [UniLS: End-to-End Audio-Driven Avatars for Unified Listening and Speaking](cards.md#paper-unils) | 当条件模态与输出弱相关时，先无条件学自然动态，再微调用弱条件修饰，而非从头强条件拟合。 |
| 机器人学 | 强化学习 | [NIL: No-data Imitation Learning](cards.md#paper-no-data-imitation-learning) | 缺少动作捕捉演示时，可用合成视频作为视觉奖励参照，由仿真器负责约束物理可行性。 |
| 计算机视觉 | 模型架构 | [CrackSSM: Reviving SSMs for Crack Segmentation via Dynamic Scanning](cards.md#paper-crackssm-dynamic-scan) | 对细长结构使用视觉状态空间模型时，依当前样本方向响应改变序列顺序。 |
| 机器学习基础 | 训练与数据策略 | [A Unified Framework for Knowledge Transfer in Bidirectional Model Scaling](cards.md#paper-bidirectional-wavelet-model-scaling) | 缩放预训练模型时，把同层权重当作多分辨率信号，用小波重采样初始化大小两种目标。 |
| 计算机视觉 | 损失函数 | [MoECLIP: Patch-Specialized Experts for Zero-shot Anomaly Detection](cards.md#paper-moeclip-expert-diversity) | 逐 patch 的 LoRA 专家出现冗余时，可分别消融输入子空间正交化和输出等角约束。见表 2。 |
| 计算机视觉 | 损失函数 | [Rectifying Latent Space for Generative Single-Image Reflection Removal](cards.md#paper-reflection-equivariant-latents) | 用生成模型分离叠加成像时，应检测编码器能否保留物理混合关系，并与仅重建微调比较。见表 4。 |
| 多模态学习 | 评测与诊断 | [Unstitching the Chimera: Frame-Level Risk and Train-Free Mitigation for Video Hallucination](cards.md#paper-chimera-temporal-risk) | 视频问答可单独检测把本来存在但互不相干的片段拼成同一叙事的失效，并比较先分段再校准的顺序。见表 2–3。 |
| 计算机视觉 | 推理策略 | [Refracting Reality: Generating Images with Realistic Transparent Objects](cards.md#paper-physical-refraction-generation) | 当图像生成受可计算成像方程约束时，可以在去噪过程中显式同步图内和旁视角的同源像素，并分开检查物理与感知指标。见表 2。 |
| 计算机视觉 | 优化 | [Stochastic Ray Tracing for the Reconstruction of 3D Gaussian Splatting](cards.md#paper-stochastic-gaussian-raytracing) | 训练可微高斯光追时，可用每条光线的无偏随机梯度替代确定性遍历排序，并对照时间与画质。见表 1–2。 |
| 计算机视觉 | 推理策略 | [Training-free Mixed-Resolution Latent Upsampling for Spatially Accelerated Diffusion Transformers](cards.md#paper-ralu-edge-aware-latent-upsampling) | 扩散空间加速应分别处理边缘混叠和上采样后噪声时刻失配；对比不同区域预算和噪声匹配。见图 8、表 3。 |
| 多模态学习 | 训练策略 | [ProM3E: Probabilistic Masked MultiModal Embedding Model for Ecology](cards.md#paper-prom3e) | 缺失模态不必重建原始信号，可学习潜表示分布并以检索对照判断融合哪些模态。 |
| 计算机视觉 | 模型架构 | [Unified Camera Positional Encoding for Controlled Video Generation](cards.md#paper-unified-camera-positional-encoding) | 以相对射线表达相机姿态、内参和镜头畸变，并将初始绝对朝向单独编码。 |
| 计算机视觉 | 训练策略 | [Refining Few-Step Text-to-Multiview Diffusion via Reinforcement Learning](cards.md#paper-mvc-zigal) | 少步多视图生成的奖励要同时测视图保真和跨视一致，可在同一采样预算验证约束取舍。 |
| 机器人学 | 模型架构 | [Rethinking Intermediate Representation for VLM-based Robot Manipulation](cards.md#paper-seam) | 在高层 VLM 和机器执行之间分别定义操作词汇与组合语法，检验新任务重组是否可执行。 |
| 计算机视觉 | 损失函数 | [Learning Diffeomorphism for Medical Image Registration with Time-Embedded Architectures Using Semigroup Regularization](cards.md#paper-sgdir) | 连续形变用时间半群一致性约束取代显式积分，并按正则强度验拓扑与配准精度。 |
| 机器学习基础 | 训练与数据策略 | [Revisiting Unknowns: Towards Effective and Efficient Open-Set Active Learning](cards.md#paper-e2oal) | 开放集主动学习中保存人工确认的未知样本，用其校准查询池并训练辅助类别头。 |
| 机器人学 | 推理优化 | [Driving on Registers](cards.md#paper-drivor-camera-registers) | 多相机行为模型让相机感知的寄存器 token 先压缩视图，再让同一紧凑表示服务候选与打分。 |
| 多模态学习 | 强化学习 | [MoE-GRPO: Optimizing Mixture-of-Experts via Reinforcement Learning in Vision-Language Models](cards.md#paper-moe-grpo-routing) | 稀疏多模态专家中，用奖励反馈探索专家组合，并按模态约束不必要的探索。 |
| 科学与医学 AI | 迁移与泛化 | [Sparse Task Vector Mixup with Hypernetworks for Efficient Knowledge Transfer in Whole-Slide Image Prognosis](cards.md#paper-steph-sparse-task-mixup) | 目标数据少且已有多个任务模型时，先混合源与目标的任务向量，再稀疏选择贡献。 |
| 多模态学习 | 条件生成 | [TokenTrace: Multi-Concept Attribution through Watermarked Token Recovery](cards.md#paper-tokentrace) | 生成图的多概念归因需要按查询解码，先区分概念级可验证性与整图水印存在性。 |
| 多模态学习 | 损失函数与优化 | [Twin-T & TwintVQA: A Reliable Structure-Detail Separating VLM and a Comprehensive Benchmark for Chart and Table Tasks](cards.md#paper-twin-t-structure-detail) | 训练图表问答时，把布局理解与数字细节分开建模，并在偏好目标中显式核对数值和关键词。 |
| 多模态学习 | 推理优化 | [NanoSD: Edge Efficient Foundation Model for Real Time Image Restoration](cards.md#paper-nanosd-latency-aware-distillation) | 边缘扩散部署时把 VAE 和去噪器共同蒸馏，并用目标硬件实测延迟选结构。 |
| 多模态学习 | 推理优化 | [MAD: Modality-Adaptive Decoding for Mitigating Cross-Modal Hallucinations in Multimodal Large Language Models](cards.md#paper-mad-modality-adaptive-decoding) | 音视频问答先估计问题需要哪些模态，再按该概率调整不同解码分支。 |
| 计算机视觉 | 优化 | [Solving Minimal Problems Without Matrix Inversion Using FFT-Based Interpolation](cards.md#paper-fft-minimal-polynomial-solvers) | 小规模几何最小问题的消元可比较用 FFT 插值重建行列式多项式和传统在线矩阵求逆。见表 1–2。 |
| 计算机视觉 | 训练策略 | [Teacher-Guided Routing for Sparse Vision Mixture-of-Experts](cards.md#paper-tgr-moe-teacher-routing) | 稀疏专家反馈只覆盖已选路由时，可加冻结稠密教师派生的路由监督，单独测路由稳定性及迁移。见图 3、表 3。 |
| 计算机视觉 | 推理策略 | [DeltaQuant: 4-bit Video Diffusion Models with Spatiotemporal Delta Smoothing](cards.md#paper-deltaquant-video-local-residual) | 视频低位宽量化可把邻近时空激活的共量保留高精度，只量化局部残差。见表 1。 |
| 机器人学 | 表征学习 | [AstraNav-Memory: Contexts Compression for Long Memory](cards.md#paper-astranav-memory-compression) | 长程导航的图像记忆可联合扫描保留长度与每帧压缩率，避免把更长历史当成自动收益。见表 3–4。 |
| 计算机视觉 | 推理策略 | [Improving Motion in Image-to-Video Models via Adaptive Low-Pass Guidance](cards.md#paper-adaptive-lowpass-i2v-motion) | 图生视频不动时，可测试早期衰减参考图高频信息、大体运动形成后再恢复，与注意力路径调整区分。见表 2–3。 |
| 计算机视觉 | 优化 | [Globally Optimal Pose from Orthographic Silhouettes](cards.md#paper-orthographic-silhouette-pose-search) | 已知几何在无对应轮廓场景中，可预计算旋转对应的全局轮廓签名以约束分支搜索。见 §4、表 1–4。 |
| 计算机视觉 | 推理策略 | [Otil: Accelerating Diffusion Model Inference via Communication-Efficient Multi-GPU Parallelism](cards.md#paper-otil-selective-latent-synchronization) | 多 GPU 扩散加速可只同步变化大的潜块并轮询全区，用通信时延和质量共同调块大小。见表 3–4。 |
| 计算机视觉 | 推理压缩 | [VDE: Training-Free Accelerating Rectified Flow Model via Velocity Decomposition and Estimation](cards.md#paper-vde-rectified-flow) | 沿当前输入方向分解速度并随输入估计，可与直接复用陈旧速度缓存比较。 |
| 机器人学 | 优化算法 | [Task-Driven Implicit Representations for Automated Design of LiDAR Systems](cards.md#paper-implicit-lidar-design) | 传感器设计可先学习任务下的有效采样分布，再在明确硬件约束内拟合配置。 |
| 计算机视觉 | 训练策略 | [Mind the Gap: Transferring Labels to Align Object Detection Datasets](cards.md#paper-label-aligned-transfer) | 合并有标签冲突的数据集时，可在候选区域内对齐到目标定义，并保留不同来源的粒度。 |
| 多模态学习 | 模型架构 | [Proxy3D: Efficient 3D Representations for Vision-Language Models via Semantic Clustering and Alignment](cards.md#paper-proxy3d) | 将多帧中语义相似的三维特征聚成代理词元，可在固定长度下比较与像素词元的空间一致性。 |
| 计算机视觉 | 训练策略 | [HiCoGen: Hierarchical Compositional Text-to-Image Generation in Diffusion Models via Reinforcement Learning](cards.md#paper-hicogen-decaying-stochasticity) | 扩散强化学习可把探索噪声更多放在早期决策，评估与固定噪声下的结构覆盖差异。 |
| 计算机视觉 | 自监督学习 | [From None to All: Self-Supervised 3D Reconstruction via Novel View Synthesis](cards.md#paper-nas3r) | 没有相机参数标注时，让几何和相机预测共用骨干，由目标视图的重投影误差同时监督。 |
| 计算机视觉 | 表示学习 | [RetimeGS: Continuous-Time Reconstruction of 4D Gaussian Splatting](cards.md#paper-retimegs) | 拟合动态高斯场景时，用连续时间参数化和中间时刻监督缓解离散帧拟合的混叠。 |
| 计算机视觉 | 表示学习 | [MV3DIS: Multi-View Mask Matching via 3D Guides for Zero-Shot 3D Instance Segmentation](cards.md#paper-mv3dis-3d-guided-masks) | 从二维分割融合三维实例时，用同一个粗三维分段配准各视图掩码，并按深度一致性定权。 |
| 计算机视觉 | 推理优化 | [InvAD: Inversion-based Reconstruction-Free Anomaly Detection with Diffusion Models](cards.md#paper-invad-latent-inversion) | 用扩散模型做异常分数时，检验反演潜变量偏离先验能否取代往返像素重建。 |
| 多模态学习 | 推理优化 | [Trainable Log-linear Sparse Attention for Efficient Diffusion Transformers](cards.md#paper-log-linear-sparse-attention) | 长视觉序列不止稀疏注意力，还要把块筛选做成多层细化，并保留未选区域的粗粒度上下文。 |
| 多模态学习 | 训练与数据策略 | [PLACID: Identity-Preserving Multi-Object Compositing via Video Diffusion with Synthetic Trajectories](cards.md#paper-placid-synthetic-trajectories) | 训练视频模型做静态组合时，将初始随机摆放过渡到目标布局，复用时序一致性来保留各实体。 |
| 多模态学习 | 推理策略 | [OmniZip: Audio-Guided Dynamic Token Compression for Fast Omnimodal Large Language Models](cards.md#paper-omnizip-audio-guided-pruning) | 音视频长上下文压缩可按音频事件时窗调节视频预算，并同时报告预填充与端到端延迟。见表 3–4。 |
| 多模态学习 | 训练策略 | [Think with 3D: Geometric Imagination Grounded Spatial Reasoning from Limited Views](cards.md#paper-3dthinker-distilled-geometry) | 只在训练能获得昂贵三维教师时，可蒸馏中间几何表示并在推理时移除教师；与推理调用深度先验比较。见表 3–4。 |
| 计算机视觉 | 表征学习 | [Prune Wisely, Reconstruct Sharply: Compact 3D Gaussian Splatting via Adaptive Pruning and Difference-of-Gaussian Primitives](cards.md#paper-difference-of-gaussians-primitives) | 三维高斯压缩在边缘质量下降时，可对照同剪枝配置下用正负联合原语增强表达。见表 2。 |
| 机器学习基础与统计 | 评测与诊断 | [Deconstructing the Failure of Ideal Noise Correction: A Three-Pillar Diagnosis](cards.md#paper-ideal-noise-correction-failure) | 标签噪声校正实验先用真值转移矩阵排除估计误差，再分别检查训练轨迹与每样本标签信息。见 §5.3、图 3。 |
| 计算机视觉 | 模型架构 | [Temporal Interaction in Spiking Transformers with Multi-Delay Mixer](cards.md#paper-md-mixer-spiking-temporal-delays) | 事件驱动 Transformer 可在空间注意力前混合不同延迟的脉冲，并用跨时刻依赖测量确认是否超出逐帧空间处理。见表 2–3。 |
| 强化学习与决策 | 强化学习方法 | [Fine-Grained GRPO for Precise Preference Alignment in Flow Models](cards.md#paper-g2rpo-stepwise-preference) | 流模型偏好训练可把噪声搜索限制在可比较的局部去噪步骤，并对多个偏好维度分开衡量。见表 1–3。 |
| 机器人学 | 推理策略 | [Paparazzo: Active Mapping of Moving 3D Objects](cards.md#paper-paparazzo) | 主动重建动态物体时，依据预测轨迹选择能补足覆盖的未来视角。 |
| 机器学习基础与统计 | 模型架构 | [Efficient Equivariant Transformer for Self-Driving Agent Modeling](cards.md#paper-drivegatr) | 以几何代数编码各实体以实现平面刚体变换等变性，单独核查成对位置编码的计算代价。 |
| 机器学习基础与统计 | 训练策略 | [Temporal Representation Enhancement (TRE): Learning to Forget Dominant Patterns for Enhanced Temporal Spiking Features](cards.md#paper-tre-spiking) | 时序表征易重复同一判别线索时，可训练时抑制长期占优响应，再测不同时步是否互补。 |
| 多模态学习 | 推理策略 | [Dynamic Token Reweighting for Robust Vision-Language Models](cards.md#paper-dtr-safe-token-reweighting) | 部署视觉语言防护时，同时检查推理干预对防御可靠性、正常视觉任务与时延的影响。 |
| 计算机视觉 | 训练策略 | [Chorus: Multi-Teacher Pretraining for Holistic 3D Gaussian Scene Encoding](cards.md#paper-chorus-3dgs) | 共享三维编码器接受不同二维教师的专属投影，并以少标注探针检查语义和实例细节能否共存。 |
| 多模态学习 | 条件生成 | [Residual Diffusion Bridge Model for Image Restoration](cards.md#paper-residual-diffusion-bridge) | 当输入多数位置无需改变时，用端点残差调制扩散桥的加噪与恢复强度。 |
| 计算机视觉 | 自监督学习 | [Rewis3d: Reconstruction Improves Weakly-Supervised Semantic Segmentation](cards.md#paper-rewis3d) | 训练稀疏标注分割时，把视频可重建三维点云用作跨视图语义传播，部署仍只用二维模型。 |
| 多模态学习 | 表示学习 | [Keep it SymPL: Symbolic Projective Layout for Allocentric Spatial Reasoning in Vision-Language Models](cards.md#paper-sympl) | 物体中心视角推理时，先显式变换参考系并以符号布局缩短视觉推导。 |
| 计算机视觉 | 训练与数据策略 | [Portable Active Learning for Object Detection](cards.md#paper-portable-active-learning-detection) | 不能读取检测器内部时，用输出框的类别校准不确定性和输入多样性选标注批次。 |
| 机器人学 | 表示学习 | [LASAR: Towards Spatio-temporal Reasoning with Latent Cognitive Map](cards.md#paper-lasar-cognitive-map) | 训练导航智能体时分开存情节记忆和语义地图，再用关系对比目标直接约束地图。 |
| 多模态学习 | 模型架构 | [DREAM: Document Recognition with Explicit Adaptive Memory](cards.md#paper-dream-prototype-memory) | 文档识别反复遇到相似版式时，可为局部视觉块添加多尺度原型记忆。 |
| 多模态学习 | 推理优化 | [YOSE: You Only Select Essential Tokens for Efficient DiT-based Video Object Removal](cards.md#paper-yose-essential-tokens) | 局部视频编辑只计算掩码内关键 token，并用低成本路径近似掩码外上下文影响。 |
| 多模态学习 | 训练策略 | [Geoint-R1: Formalizing Multimodal Geometric Reasoning with Dynamic Auxiliary Constructions](cards.md#paper-geoint-verified-auxiliary-geometry) | 视觉几何证明可把辅助构造作为程序可验的中间步骤，并单独比较需要与不需要辅助线的题。见表 3–4。 |
| 机器人学 | 表征学习 | [Geometric Neural Distance Fields for Learning Human Motion Priors](cards.md#paper-nrmf-motion-distance-fields) | 拟合含噪或局部人体运动可把旋转、速度和加速度分别作为可投影的几何先验，并同时测位置和运动误差。见表 1–3。 |
| 计算机视觉 | 模型架构 | [FARMER: Flow AutoRegressive Transformer over Pixels](cards.md#paper-farmer-likelihood-latent-partition) | 可逆像素生成可把信息性潜通道与冗余通道拆开建模，在显式似然与自回归计算之间做比较。见表 2。 |
| 多模态学习 | 强化学习方法 | [CCCaption: Dual-Reward Reinforcement Learning for Complete and Correct Image Captioning](cards.md#paper-cccaption-symmetric-visual-rewards) | 描述生成奖励可分开计来自图像的事实覆盖和来自文本的事实真实性，避免单边奖励鼓励遗漏或编造。见表 2–3。 |
| 计算机视觉 | 训练策略 | [LinVideo: A Post-Training Framework towards O(n) Attention in Efficient Video Generation](cards.md#paper-linvideo-selective-linear-attention) | 后训练转换视频注意力时可逐步选择容易替换的层，同时让学生在不同去噪时刻贴近教师。见表 3–4。 |
| 机器人学 | 表征学习 | [Probing and Bridging Geometry-Interaction Cues for Affordance Reasoning in Vision Foundation Models](cards.md#paper-affordance-geometry-interaction-probing) | 无动作标签的可供性定位可把部件几何和动词条件热图作为两路证据，再与单路探针对照。见表 2。 |
| 机器人学 | 表征学习 | [Unifying Perception and Action: A Hybrid-Modality Pipeline with Implicit Visual Chain-of-Thought for Robotic Action Generation](cards.md#paper-vita-shared-action-vision-latents) | 机器人策略可测试让动作与未来图像共用离散词元，并用同一分段的两路监督对照仅动作目标。见 §4 与消融。 |
| 机器学习基础与统计 | 优化算法 | [The Devil Is in Gradient Entanglement: Energy-Aware Gradient Coordinator for Robust Generalized Category Discovery](cards.md#paper-eagc-gcd) | 混合有标注与无标注目标时诊断梯度纠缠，再调无标注更新方向。 |
| 计算机视觉 | 训练策略 | [MatAnyone 2: Scaling Video Matting via a Learned Quality Evaluator](cards.md#paper-matanyone2-mqe) | 把像素级质量评估器同时用于在线监督和离线筛标签，分别验收边缘质量收益。 |
| 多模态学习 | 训练策略 | [VOLD: Reasoning Transfer from LLMs to Vision-Language Models via On-Policy Distillation](cards.md#paper-vold) | 用纯文本教师在线蒸馏视觉语言策略前，先检查学生是否与教师输出分布对齐。 |
| 计算机视觉 | 模型架构 | [FoV-Net: Rotation-Invariant CAD B-rep Learning via Field-of-View Ray Casting](cards.md#paper-fov-net) | 通过面局部坐标系表达边界表示，并用局部射线保留全局几何；评测须包含任意三维旋转。 |
| 计算机视觉 | 模型架构 | [VideoCoF: Unified Video Editing with Temporal Reasoner](cards.md#paper-videocof) | 复杂视频编辑先生成定位表征再出成片，比较是否比无定位的时序生成更能保护非目标区域。 |
| 机器学习基础与统计 | 训练策略 | [Scaling-Aware Data Selection for End-to-End Autonomous Driving Systems](cards.md#paper-mosaic-scaling-aware-selection) | 数据采集可按域拟合多个指标的规模曲线，再用边际收益确定下一批选择。 |
| 机器学习基础 | 损失函数与优化 | [A Faster Path to Continual Learning](cards.md#paper-c-flat-turbo) | 当平坦度优化的梯度方向可复用时，跨扰动步骤共享计算，并随任务逐渐加大复用步。 |
| 机器学习基础 | 知识蒸馏 | [HAD: Heterogeneity-Aware Distillation for Lifelong Heterogeneous Learning](cards.md#paper-heterogeneity-aware-distillation) | 连续训练异构密集任务时，按每项输出分布平衡蒸馏，同时保护显著边界。 |
| 计算机视觉 | 模型架构 | [PaQ-DETR: Learning Pattern and Quality-Aware Dynamic Queries for Object Detection](cards.md#paper-paq-detr) | 集合预测中固定查询利用率偏斜时，用少量共享模式组合按图生成查询，再按分类定位匹配质量分配正例。 |
| 多模态学习 | 评测与分析 | [VCU-Bridge: Hierarchical Visual Connotation Understanding via Semantic Bridging](cards.md#paper-vcu-bridge) | 诊断抽象视觉推理时，把低层观察、中间语义和抽象结论标注为可追踪链，并测试低层训练能否向上传导。 |
| 多模态学习 | 强化学习 | [Seeing What Matters: Visual Preference Policy Optimization for Visual Generation](cards.md#paper-vipo-visual-advantages) | 视觉生成后训练可把整图或整段标量优势分配为局部优势，以强调感知重要区域。 |
| 计算机视觉 | 表示学习 | [Motion 3-to-4: 3D Motion Reconstruction for 4D Synthesis](cards.md#paper-motion-3-to-4) | 从单目视频重建动态资产时，把静态网格生成与逐顶点时序变形分开建模。 |
| 机器学习基础与统计 | 评测与诊断 | [Generative Modeling of Weights: Generalization or Memorization?](cards.md#paper-generated-weights-memorization) | 权重生成方法必须与权重加噪和均值插值比较，并同时用参数近邻与功能相似判断新颖性。见 §3、表 1。 |
| 计算机视觉 | 评测与诊断 | [OnlineHMR: Video-based Online World-Grounded Human Mesh Recovery](cards.md#paper-onlinehmr-causal-delay-evaluation) | 流式人体网格恢复应同时验收因果性、单帧等待时间与世界坐标误差，不能只看处理 FPS。见表 3。 |
| 计算机视觉 | 评测与诊断 | [I'm a Map! Interpretable Motion-Attentive Maps: Spatio-Temporally Localizing Concepts in Video Diffusion Transformers](cards.md#paper-imap-motion-token-diagnostics) | 视频扩散的概念解释应分别找在哪帧、哪里、哪个对象发生动作，并把动作相关头与全头对照。见表 1–2。 |
| 计算机视觉 | 推理策略 | [Parallel Jacobi Decoding for Fast Autoregressive Image Generation](cards.md#paper-parallel-jacobi-image-decoding) | 对自回归图像尝试从一维连续草稿切到二维局部并行更新，并在相同骨干测收敛与 FID。见表 1–2。 |
| 多模态学习 | 训练策略 | [Addressing Exacerbated Attention Sink for Source-Free Cross-Domain Few-Shot Learning](cards.md#paper-few-shot-attention-sink) | 用少量目标域样本微调视觉语言模型时，应诊断是否进一步集中注意到原本容易对齐的词元，再分别测试抑制与增强。见表 2。 |
| 多模态学习 | 推理策略 | [MODIX: A Training-Free Multimodal Information-Driven Positional Index Scaling for Vision-Language Models](cards.md#paper-modix-position-stride) | 视觉语言推理可只改位置索引跨度来检验信息分配作用，避免与删词元的效果混在一起。见表 2–4。 |
| 机器学习基础与统计 | 理论与统计 | [CGU-Bayes: Causal Graph Uncertainty-Guided Bayesian Inference for Domain Generalization](cards.md#paper-cgu-bayes-graph-uncertainty) | 域泛化若依赖推断的因果图，应比较固定图、等权候选图和不确定性加权，区分真实数据与已知机制仿真。见表 1–3。 |
| 多模态学习 | 推理策略 | [Activation Matters: Test-time Activated Negative Labels for OOD Detection with Vision-Language Models](cards.md#paper-tanl) | 开放集检测选负类时用测试分布的激活统计，检查固定文本负类是否与真实外域样本脱节。 |
| 计算机视觉 | 模型架构 | [3D-Aware Multi-Task Learning with Cross-View Correlations for Dense Scene Understanding](cards.md#paper-cvm-dense-mtl) | 多任务密集预测共享跨视相关信息，不只在同一图像特征上学习任务关系。 |
| 机器人学 | 训练策略 | [CoIn3D: Revisiting Configuration-Invariant Multi-Camera 3D Object Detection](cards.md#paper-coin3d) | 换相机阵列部署三维检测时，分别验证观测增广与显式相机特征调制。 |
| 计算机视觉 | 模型架构 | [FisherPoser: Human Motion Estimation from Sparse Observations with Hierarchical Region-Wise Fisher-Matrix Uncertainty Modeling](cards.md#paper-fisherposer) | 稀疏姿态估计可直接预测旋转分布，再沿运动链条件化传播不确定性。 |
| 计算机视觉 | 训练策略 | [Action Motifs: Self-Supervised Hierarchical Representation of Human Body Movements](cards.md#paper-action-motifs) | 运动序列先学习可变长的局部动作单位，再对其组合做掩码预测，以检查跨动作的复用。 |
| 多模态学习 | 训练策略 | [Improving Vision-language Models with Perception-centric Process Reward Models](cards.md#paper-perceval) | 用视觉声明核验定位错误片段，按词元调优势并对照整轨迹奖励。 |
| 计算机视觉 | 模型架构 | [RnG: A Unified Transformer for Complete 3D Modeling from Partial Observations](cards.md#paper-rng-3d-kv-cache) | 稀疏视图三维推理时，隔离观测重建和不可见区域生成，并用同一缓存支持反复视角查询。 |
| 机器学习基础 | 微调与适配 | [S2FT: Parameter-Efficient Fine-Tuning in Sparse Spectrum Domain](cards.md#paper-s2ft-sparse-spectrum) | 傅里叶微调前先测权重增量的频谱，若不稀疏则以可逆神经元重排聚拢能量。 |
| 机器学习基础 | 自监督学习 | [PAF: Perturbation-Aware Filtering for Open-Set Semi-Supervised Learning](cards.md#paper-perturbation-aware-filtering) | 开放集半监督数据清理可用语义保持扰动下的表示不稳定性评估样本是否域外。 |
| 机器学习基础 | 可解释性与诊断 | [Global Information Thresholding for Sufficient and Necessary Circuits](cards.md#paper-global-information-thresholding) | 定位模型电路时，用行为保留阈值自动决定边数，并分开报告充分性与必要性。 |
| 多模态学习 | 损失函数与优化 | [M3Grounder: Mask-Based Multi-Span and Multi-Granular Grounding for Document QA](cards.md#paper-m3grounder) | 文档问答需要可定位证据时，让每个答案短语输出掩码，并约束粒度间的包含关系。 |
| 多模态学习 | 推理优化 | [GeoRK2: Geometry-Guided Runge-Kutta Integration for Diffusion Transformer Acceleration](cards.md#paper-geork2) | 为扩散推理减少步数时，用经验激活协方差定义积分几何，检验大步长下保真度。 |
| 计算机视觉 | 表征学习 | [WonderZoom: Multi-Scale 3D World Generation](cards.md#paper-wonderzoom-scale-adaptive-surfels) | 多尺度场景渲染可按当前尺度调节粗细基元不透明度，并分别测切尺度的一致性和显存。见表 3。 |
| 多模态学习 | 数据策略 | [Concept-Aware Batch Sampling Improves Language-Image Pretraining](cards.md#paper-concept-aware-batch-sampling) | 图文预训练可按目标概念直方图动态抽批，分别调节覆盖种类和批内出现频次。见表 2–4。 |
| 多模态学习 | 表征学习 | [GeoFree-CoSeg: Unsupervised Point Cloud-Image Cross-Modal Co-Segmentation Without Geometric Alignment](cards.md#paper-geofree-coseg-semantic-correspondence) | 点云和图像缺乏标定对应时，可先各自发现粗语义，再用公共语义图筛选共有区域。见表 1–3。 |
| 机器学习基础与统计 | 模型架构 | [Negative Binomial Variational Autoencoders for Overdispersed Latent Modeling](cards.md#paper-negative-binomial-count-latents) | 离散计数潜变量若呈过度离散，可比较负二项和泊松先验，同时测重建与生成而非只看其中一项。见表 1–3。 |
| 计算机视觉 | 模型架构 | [Any Resolution Any Geometry: From Multi-View To Multi-Patch](cards.md#paper-urgt-multipatch-geometry) | 高分图像深度与法线可把图块当多视图共享几何注意力，并随机化图块网格测接缝。见表 3–4。 |
| 计算机视觉 | 模型架构 | [ReHyAt: Recurrent Hybrid Attention for Video Diffusion Transformers](cards.md#paper-rehyat-chunk-recurrent-hybrid-attention) | 长视频扩散可以混合精确局部注意力与递归跨块线性状态，并按设备跨帧数测延迟。见表 4。 |
| 智能体 | 评测与诊断 | [Benchmarking PhD-Level Coding in 3D Geometric Computer Vision](cards.md#paper-geocodebench) | 复现科学算法时验收论文的核心函数及边界条件，和整仓运行成功分开。 |
| 计算机视觉 | 训练策略 | [Mitigating Error Amplification in Fast Adversarial Training](cards.md#paper-ddg-fast-robust-training) | 防御训练按样本置信分层检查精度与鲁棒性，避免低置信样本主导错误放大。 |
| 计算机视觉 | 模型架构 | [Rethinking Position Embedding as a Context Controller for Multi-Reference and Multi-Shot Video Generation](cards.md#paper-poco-reference-positioning) | 当多路参考外观相似时，可用独立位置信息约束引用关系，按参考混淆和跨段一致性验收。 |
| 多模态学习 | 训练策略 | [MSRL: Scaling Generative Multimodal Reward Modeling via Multi-Stage Reinforcement Learning](cards.md#paper-msrl-multimodal-reward) | 多模态偏好标签少时，可先训练文本奖励推理，再依次检验描述桥接和原始图像阶段。 |
| 计算机视觉 | 推理压缩 | [PixelRush: Ultra-Fast, Training-Free High-Resolution Image Generation via One-step Diffusion](cards.md#paper-pixelrush) | 极少步数的分块生成须单独处理拼接重叠和低频平滑，不能套用多步循环。 |
| 计算机视觉 | 模型架构 | [Cross-Scale Pansharpening via ScaleFormer and the PanScale Benchmark](cards.md#paper-scaleformer) | 跨图像分辨率泛化时固定局部块尺度，把尺寸变化转成序列长度外推。 |
| 多模态学习 | 损失函数与优化 | [MatLat: Material Latent Space for PBR Texture Generation](cards.md#paper-matlat-locality-regularization) | 给预训练图像生成器新增空间通道时，用裁剪潜片并解码的局部一致性避免跨视角对应失效。 |
| 多模态学习 | 推理优化 | [It's Never Too Late: Noise Optimization for Collapse Recovery in Trained Diffusion Models](cards.md#paper-diffusion-noise-diversity-recovery) | 已训练扩散模型在同提示下重复时，直接优化多样性目标的初噪，并比较噪声频谱。 |
| 多模态学习 | 训练与数据策略 | [StaR-KVQA: Structured Reasoning Traces for Implicit-Knowledge Visual Question Answering](cards.md#paper-star-kvqa) | 视觉问答自蒸馏时，同时监督符号实体关系与依该路径写的自然语言解释。 |
| 多模态学习 | 迁移与泛化 | [A Causal Marriage between VLM and IRM from Understanding to Reasoning](cards.md#paper-clip-irm) | 当图文模型依赖背景时，按词元分开类别语义和环境线索，对比目标显式引入不变性。 |
| 多模态学习 | 推理优化 | [CamDirector: Towards Long-Term Coherent Video Trajectory Editing](cards.md#paper-camdirector-world-cache) | 长视频相机重拍时用世界坐标缓存静态背景、单独变换动态区域，并让后段复用历史。 |
| 多模态学习 | 推理优化 | [Denoising, Fast and Slow: Difficulty-Aware Adaptive Sampling for Image Generation](cards.md#paper-patch-forcing) | 扩散以块为单位动态分配步数时，训练先限制跨块可见信息，避免产生推理见不到的提示。 |
| 多模态学习 | 数据策略 | [Revisiting the Necessity of Lengthy Chain-of-Thought in Vision-centric Reasoning Generalization](cards.md#paper-minimal-grounding-cot-generalization) | 制作视觉推理监督时应对比最少可核验落点与完整长轨迹，同时测收敛速度和未见难度的最终上限。见 §4.2、表 1。 |
| 计算机视觉 | 训练策略 | [Uni-DAD: Unified Distillation and Adaptation of Diffusion Models for Few-step Few-shot Image Generation](cards.md#paper-uni-dad-dual-domain-distillation) | 少目标样本又要求少步采样时，应比较同时保留源教师和目标教师监督，与先迁移再蒸馏的效果。见表 1–2。 |
| 计算机视觉 | 表征学习 | [Real-Time Generation of Streamable Talking Portrait Video with Reference-Guided Deep Compression VAEs](cards.md#paper-reference-guided-causal-video-vae) | 压缩参考条件下的流视频时可绕过重复的静态外观编码，用参考图辅助因果 VAE 表示动态残差。见表 2。 |
| 计算机视觉 | 数据策略 | [AE2VID: Event-based Video Reconstruction via Aperture Modulation](cards.md#paper-ae2vid-active-event-acquisition) | 事件视觉对静态区域信息不足时，可主动调节采集条件产生强度事件，并与仅靠场景运动的事件对照。见 §4、表 1–2。 |
| 计算机视觉 | 推理策略 | [Anchoring and Rescaling Attention for Semantically Coherent Inbetweening](cards.md#paper-keyframe-anchored-inbetweening) | 生成式补帧跨度较大时，可分别对照关键帧条件强化和时间位置重缩放，估计语义与连贯性的取舍。见表 3。 |
| 机器学习基础与统计 | 评测与诊断 | [Verifying Neural Network Robustness with Dual Perturbations](cards.md#paper-veridou-combined-verification) | 模型鲁棒验收应区分单一变化条件和复合变化条件的保证，单独报告求解超时。见实验部分、图 7。 |
| 多模态学习 | 模型架构 | [Beyond Graph Model: Reliable VLM Fine-Tuning via Random Graph Adapter](cards.md#paper-vertex-random-graph-adapter) | 少样本提示存在同名多属性时，可把每类文本适配为分布并传播类间消息，再和确定性图及辅助分类器做消融。见表 3。 |
| 多模态学习 | 模型架构 | [VGent: Visual Grounding via Modular Design for Disentangling Reasoning and Prediction](cards.md#paper-vgent) | 把视觉推理留在冻结编码器，用候选框选择替代逐词元生成坐标，分别测召回上限和选择质量。 |
| 多模态学习 | 推理策略 | [HulluEdit: Single-Pass Evidence-Consistent Subspace Editing for Mitigating Hallucinations in Large Vision-Language Models](cards.md#paper-hulluedit) | 抑制视觉幻觉时先隔离与证据正交的冲突分量，在同一次推理验收真实证据保留。 |
| 计算机视觉 | 模型架构 | [LiveGesture: Streamable Co-Speech Gesture Generation Model](cards.md#paper-livegesture) | 实时多区域动作应同时满足局部词元因果和跨区协调，分别评估无前瞻条件下的同步性。 |
| 计算机视觉 | 评测与诊断 | [ActivityForensics: A Comprehensive Benchmark for Localizing Manipulated Activity in Videos](cards.md#paper-activityforensics-eval) | 防御评测要检验篡改时间段的定位和域外泛化，不能只验整段真假。 |
| 计算机视觉 | 优化算法 | [Affine Perspective-Three-Point Problem](cards.md#paper-affine-p3p) | 将便宜的近似几何闭式解作为初值，再用少次校正恢复精确相机模型。 |
| 多模态学习 | 条件生成 | [Refacade: Editing Object with Given Reference Texture](cards.md#paper-refacade) | 参考图纹理迁移时打乱参考全局结构，用局部纹理统计防止复制参考形状。 |
| 机器学习基础 | 训练与数据策略 | [Mitigating The Distribution Shift of Diffusion-based Dataset Distillation](cards.md#paper-diffusion-dataset-distribution-shift) | 合成少量蒸馏样本时，联合去噪整批以控制覆盖，并在训练限制模型对原分布复杂性的拟合。 |
| 机器人学 | 表示学习 | [MoEActok: A MoE-based Action Tokenizer for Vision-Language-Action Models](cards.md#paper-moeactok) | 多个技能共用动作词元时，按动作块聚类训练专家量化器，再映回共享动作空间。 |
| 计算机视觉 | 损失函数与优化 | [COG: Confidence-aware Optimal Geometric Correspondence for Unsupervised Single-reference Novel Object Pose Estimation](cards.md#paper-confidence-aware-optimal-correspondence) | 存在未重叠视野的位姿配准时，把点置信度作为最优传输边际，而非一一硬匹配。 |
| 多模态学习 | 表示学习 | [Generative Video Compression with One-Dimensional Latent Representation](cards.md#paper-gvc1d) | 高压缩率下用不绑定二维位置的词元和长程记忆，减少局部及跨帧冗余。 |
| 计算机视觉 | 强化学习 | [ExPose: Reinforcing Video Generation Models for Extreme Pose Estimation](cards.md#paper-expose-pose-consistency) | 用生成中间帧辅助稀疏位姿估计时，用下游几何一致性奖励优化插值模型。 |
| 多模态学习 | 微调与适配 | [Improving Calibration in Test-Time Prompt Tuning for Vision-Language Models via Data-Free Flatness-Aware Prompt Pretraining](cards.md#paper-flatness-aware-prompt-pretraining) | 测试时提示词调优前，选平坦度更高的无数据初始化以改善置信校准。 |
| 机器人学 | 推理策略 | [Cross-Domain Demo-to-Code via Neurosymbolic Counterfactual Reasoning](cards.md#paper-nesycr-cross-domain-procedure-checks) | 示范迁移时，可先测试符号任务条件和可执行替代行为，再生成机器人任务代码。见表 3。 |
| 多模态学习 | 推理策略 | [Aligning What Vision-Language Models See and Perceive with Adaptive Information Flow](cards.md#paper-adaptive-vlm-information-flow) | 图文模型定位正确但作答错时，应对照屏蔽关键与次要视觉词元，区分信息流和定位失败。见图 3、表 1。 |
| 计算机视觉 | 数据策略 | [Long-Tail Internet Photo Reconstruction](cards.md#paper-megadepth-x-sparse-view-sampling) | 真实稀疏场景难获深度监督时，可从可重建密集场景按真实长尾的视角分布抽样，并保留清洗和抽样对照。见表 2。 |
| 多模态学习 | 训练策略 | [DocSeeker: Structured Visual Reasoning with Evidence Grounding for Long Document Understanding](cards.md#paper-docseeker-evidence-resolution) | 长视觉文档训练应同步验收页证据和回答，并只给相关页高分辨率。见表 3–4。 |
| 计算机视觉 | 训练策略 | [FlashIn: Fast and Accurate Image Inversion for Real-time Image Editing](cards.md#paper-flashin-learned-inversion) | 需交互速度的图像编辑可用合成图和已知起始噪声训练直接反演，再以真实图像验背景保真。见表 1–2。 |
| 计算机视觉 | 强化学习方法 | [Write Where It Matters: Policy-Guided Watermarks for 3D Gaussian Splatting](cards.md#paper-adaptive-3d-watermark-quality-tradeoff) | 为三维资产做内容溯源时，可用区域级嵌入预算避免逐基元训练，并同时验收画质和提取率。见表 4–5。 |
| 多模态学习 | 训练策略 | [CoVFT: Context-aware Visual Fine-tuning for Multimodal Large Language Models](cards.md#paper-covft) | 视觉骨干解冻前先和同配置冻结基线比较；当不同多模态上下文梯度冲突时，考虑上下文条件化适配。 |
| 计算机视觉 | 推理压缩 | [Faster-GS: Analyzing and Improving Gaussian Splatting Optimization](cards.md#paper-faster-gs-optimization) | 三维优化提速应固定重建质量，再单独对照算子实现、优化器更新和数值近似。 |
| 计算机视觉 | 训练策略 | [DiverseGRPO: Mitigating Mode Collapse in Image Generation via Diversity-Aware GRPO](cards.md#paper-diversegrpo) | 生成强化学习同时验收样本质量和同提示分布覆盖，并把多样性正则按去噪阶段分配。 |
| 计算机视觉 | 评测与诊断 | [Breaking Smooth-Motion Assumptions: A UAV Benchmark for Multi-Object Tracking in Complex and Adverse Conditions](cards.md#paper-dynuav-motion-failure-audit) | 良性移动相机跟踪应把检测和关联拆开，在不平滑自运动下验收两者。 |
| 机器人学 | 表示学习 | [Action-Geometry Prediction with 3D Geometric Prior for Bimanual Manipulation](cards.md#paper-action-geometry-prediction) | 双臂策略学习时把未来三维几何和动作块作为同一预测问题。 |
| 多模态学习 | 自监督学习 | [Unleashing the Intrinsic Visual Representation Capability of Multimodal Large Language Models](cards.md#paper-laver-latent-visual-reconstruction) | 纯文本词元训练让视觉表示退化时，在共享语义空间加入掩码视觉重建。 |
| 多模态学习 | 训练与数据策略 | [MotionEdit: Benchmarking and Learning Motion-Centric Image Editing](cards.md#paper-motionnft) | 动作编辑后训练中，用独立运动对齐信号区分动作正确和仅在外观上像目标。 |
| 科学与医学 AI | 迁移与泛化 | [Revisiting 2D Foundation Models for Scalable 3D Medical Image Classification](cards.md#paper-anymc3d-frozen-2d-transfer) | 三维分类资源有限时，先以冻结通用二维基础模型和轻量多视角适配作受控基线。 |
| 科学与医学 AI | 条件生成 | [Anatomica: Localized Control over Geometric and Topological Properties for Anatomical Diffusion Models](cards.md#paper-anatomica-local-constraints) | 需要区域级三维形状控制时，只解码目标子域并组合可微几何与拓扑约束。 |
| 多模态学习 | 强化学习 | [Leveraging Verifier-Based Reinforcement Learning in Image Editing](cards.md#paper-edit-r1-verifier-reward) | 多条件图像编辑策略训练时，把一条指令拆成可核查要求再聚合奖励。 |
| 多模态学习 | 表征学习 | [UniCompress: Token Compression for Unified Vision-Language Understanding and Generation](cards.md#paper-unicompress-bidirectional-token-bottleneck) | 统一图像理解和生成可在主模型前压缩、在生成解码前恢复局部视觉词元，独立测两条路径的墙钟时间。见表 1–3。 |
| 机器人学 | 表征学习 | [Envisioning the Future, One Step at a Time](cards.md#paper-sparse-point-future-ensembles) | 探索大量未来时，可以把稠密视频预测换成短步自回归点轨迹，并同时比较等样本和等墙钟的最好候选。见表 1、图 10。 |
| 多模态学习 | 推理策略 | [MeToM: Metadata-Guided Token Merging for Efficient Video LLMs](cards.md#paper-metom-codec-guided-token-merging) | 视频问答压缩可用现成编码元数据决定每帧预算与空间合并位置，再用端到端首词元时延核算。见表 1–4。 |
| 计算机视觉 | 推理策略 | [Progressive Multi-cue Alignment for Unaligned RGBT Tracking](cards.md#paper-pmatrack-progressive-rgbt-alignment) | 视野未标定的红外可见跟踪宜分开估计平移、尺度和局部残差，并依对齐难度选择提示。见表 3。 |
| 计算机视觉 | 训练策略 | [DynamicVGGT: Learning Dynamic Point Maps for 4D Scene Reconstruction in Autonomous Driving](cards.md#paper-dynamicvggt-future-point-map) | 动态三维网络可在共享世界坐标直接联合预测当前和未来点图，显式测对应连续性而非只评逐帧几何。见表 4。 |
| 计算机视觉 | 训练策略 | [Self-Evaluation Unlocks Any-Step Text-to-Image Generation](cards.md#paper-self-e-any-step-self-evaluation) | 希望从头训练可任意步数生成的模型时，应试验局部流目标加自评全局匹配，分别看极少步和多步质量。见表 2。 |
| 多模态学习 | 训练策略 | [AVATAR: Reinforcement Learning to See, Hear, and Reason Over Video](cards.md#paper-avatar-av-rl) | 组内优势消失时从含不同奖励的历史轨迹补信号，并单独检验推理首尾的信用权重。 |
| 计算机视觉 | 训练策略 | [Semantics Lead the Way: Harmonizing Semantic and Texture Modeling with Asynchronous Latent Diffusion](cards.md#paper-semantic-first-diffusion) | 语义和纹理采用错开的去噪日程，对照同步去噪能否改善细节形成。 |
| 计算机视觉 | 训练策略 | [Geometry-Aligned and Anomaly-Aware Reconstruction for 3D Anomaly Detection](cards.md#paper-aard-geometry-noise) | 点云复原的扰动分布可按局部表面几何约束，再测是否兼顾结构保留和异常定位。 |
| 计算机视觉 | 模型架构 | [VerseCrafter: Dynamic Realistic Video World Model with 4D Geometric Control](cards.md#paper-versecrafter-4d-control) | 视频世界模型把静态几何、对象轨迹和镜头变化分开表示，在同一条件下核查几何与观感。 |
| 计算机视觉 | 模型架构 | [PhysSkin: Real-Time and Generalizable Physics-Based Animation via Self-Supervised Neural Skinning](cards.md#paper-physskin) | 把连续形变基从离散网格中分离，检验同一子空间是否可迁移到不同几何采样。 |
| 计算机视觉 | 推理优化 | [Learning Where to Look and How to Judge: Resolution-agnostic Image Quality Assessment with Quality-aware Saliency](cards.md#paper-reliqs-quality-aware-saliency) | 高分辨率质量评估使用按预算选择的原尺寸小块，并以潜在评分轴联合不同数据集。 |
| 科学与医学 AI | 训练与数据策略 | [FBTA: Enabling Single-GPU End-to-End Gigapixel WSI Classification with Feature Bridging and Translation Alignment](cards.md#paper-fbta-feature-bridging) | 高分辨率多实例学习显存不足时，将端到端、冻结以及可部署的翻译特征袋分别用于优化、稳定和推理。 |
| 多模态学习 | 训练与数据策略 | [Beyond the Golden Data: Resolving the Motion-Vision Quality Dilemma via Timestep Selective Training](cards.md#paper-tqd-video-diffusion) | 视频去噪训练时根据样本的运动和画质差异调整采样时间步。 |
| 计算机视觉 | 训练与数据策略 | [Agile Deliberation: Concept Deliberation for Subjective Visual Classification](cards.md#paper-agile-deliberation) | 主观概念标注中先分解待定义概念，再用边界样例迭代修正概念及分类器。 |
| 机器学习基础 | 表示学习 | [EMMA: Extracting Multiple physical parameters from Multimodal Data](cards.md#paper-emma-multimodal-dynamics) | 从异构时间序列推断动力参数时，让观测通道共享连续时间隐状态并以已知物理方程约束。 |
| 机器人学 | 表示学习 | [TraceGen: World Modeling in 3D Trace Space Enables Learning from Cross-Embodiment Videos](cards.md#paper-tracegen-3d-trace-space) | 跨机器人和人类视频预训练时，预测场景三维点轨迹而非像素，以复用运动先验。 |
| 多模态学习 | 评测与诊断 | [HAVE-Bench: Hierarchical Audio-Visual Evaluation from Perception to Interaction](cards.md#paper-have-bench-speech-text-controlled) | 选择语音控制视觉代理时，应将同题的语音输入、转录文本与语言推理分开对照。见表 2。 |
| 计算机视觉 | 推理策略 | [Diffusion Probe: Generated Image Result Prediction Using CNN Probes](cards.md#paper-diffusion-probe-early-quality) | 多候选生成可预测早期去噪的终局质量，再决定是否继续完成整段去噪。见表 1–2。 |
| 机器学习基础与统计 | 模型架构 | [Frequency Switching Mechanism for Parameter-Efficient Multi-Task Learning](cards.md#paper-free-sinewich-task-modulation) | 多任务低秩更新可测试以任务频率生成不同权重，比较等参数下任务干扰与低秩容量。见表 3。 |
| 科学深度学习 | 评测与诊断 | [FluidGaussian: Propagating Simulation-Based Uncertainty Toward Functionally-Intelligent 3D Reconstruction](cards.md#paper-fluidgaussian-functional-reconstruction) | 三维数字孪生面向后续物理模拟时，应将功能区模拟一致性与外观误差分开评估。见表 3–4。 |
| 机器人学 | 模型架构 | [Describe Anything Anywhere At Any Moment](cards.md#paper-daaam-queryable-spatiotemporal-memory) | 长期场景记忆应保存对象描述及可查询的位置和观测时刻，并用时间误差核验索引。见表 1–4。 |
| 机器人学 | 训练策略 | [TerraSeg: Self-Supervised Ground Segmentation for Any LiDAR](cards.md#paper-terraseg-offline-pseudolabel-distillation) | 逐扫描核验代价高时，可用慢几何估计离线生成跨设备伪标签，再训练实时学生。见表 3–4。 |
| 大语言模型与Agent | 推理策略 | [META: Meta Evolution of Tool Trajectory Adaptation for Long-Video Understanding](cards.md#paper-meta-tool-trajectory-abstraction) | 工具代理可以复用既往操作序列并记录失败原因，分别消融宏工具和微工具改良。见表 2–3。 |
| 机器人学 | 评测与诊断 | [Wanderland: Geometrically Grounded Simulation for Open-World Embodied AI](cards.md#paper-wanderland-geometry-audit) | 实景仿真应将几何重建质量对视图合成和闭环表现的影响分层验证。 |
| 机器学习基础与统计 | 训练策略 | [Mining Attribute Subspaces for Efficient Fine-tuning of 3D Foundation Models](cards.md#paper-attribute-lora-subspaces) | 低秩适配可先用单因素可控数据找属性方向，再组合为受约束微调子空间。 |
| 计算机视觉 | 损失函数 | [Rethinking Box Supervision: Bias-Free Weakly Supervised Medical Segmentation](cards.md#paper-weakmed) | 用预测掩码导出可与框比较的量，再用跨尺度一致性约束掩码，而避免学习矩形形状。 |
| 多模态学习 | 训练策略 | [CVA: Context-aware Video-text Alignment for Video Temporal Grounding](cards.md#paper-cva-temporal-grounding) | 训练时替换视频背景先检验与查询无关，并在时间边界做反事实一致性。 |
| 多模态学习 | 推理策略 | [PAS: A Training-Free Stabilizer for Temporal Encoding in Video LLMs](cards.md#paper-pas-temporal-encoding) | 视频位置编码可按帧时刻扰动诊断相位不稳，并利用跨注意头聚合平滑。 |
| 机器学习基础 | 损失函数与优化 | [Every Error has Its Magnitude: Asymmetric Mistake Severity Training for Multiclass Multiple Instance Learning](cards.md#paper-asymmetric-mistake-severity) | 误分类代价不等时，使用有方向的分层损失和配套代价指标。 |
| 多模态学习 | 表示学习 | [Towards Unified Human Perception and Machine Understanding: Token Flow Guided Compression Framework](cards.md#paper-tfgc-token-flow-compression) | 要求人机共用压缩流时，允许 VLM 直接读可变数量的潜词元，由上下文预测未传词元。 |
| 计算机视觉 | 损失函数与优化 | [Physically-Grounded Turbulence Mitigation with Frame-Shared Degradation Parameters](cards.md#paper-tmfs-shared-degradation) | 同场景多帧恢复中，把共享退化结构与逐帧随机项分开估计。 |
| 机器人学 | 表示学习 | [Point4Cast: Streaming Dynamic Scene Reconstruction and Forecasting](cards.md#paper-point4cast) | 流式世界模型用持续更新的潜状态，把观测更新与任意时间几何读出分开。 |
| 计算机视觉 | 推理优化 | [Speeding Up the Learning of 3D Gaussians with Much Shorter Gaussian Lists](cards.md#paper-short-gaussian-lists) | 优化高斯泼溅速度时，直接减少每条射线的候选长度而不只约束总体高斯数。 |
| 多模态学习 | 条件生成 | [Guiding a Diffusion Transformer with the Internal Dynamics of Itself](cards.md#paper-internal-guidance-dit) | 扩散 Transformer 采样时可使用同一次前向的浅层预测作引导参照。 |
| 计算机视觉 | 训练与数据策略 | [Generalizable Video Quality Assessment via Weak-to-Strong Learning](cards.md#paper-weak-to-strong-video-quality) | 没有统一标注时，先把不同弱教师信号转为相对排序，再检验强学生的域外表现和迭代收益。 |
| 多模态学习 | 数据策略 | [DiG: Differential Grounding for Enhancing Fine-Grained Perception in Multimodal Large Language Models](cards.md#paper-dig-differential-grounding) | 细粒度视觉训练可用可控变更的成对图像，循序训练找出和定位数量未知的全部差异。见图 3、表 4。 |
| 多模态学习 | 强化学习方法 | [From Failure to Feedback: Group Revision Unlocks Hard Cases in Object-Level Grounding](cards.md#paper-group-revision-relative-reward) | 一组定位候选都达不到正确阈值时，可以按相对原始尝试的改进给有效信号，见表 4。 |
| 多模态学习 | 训练策略 | [VisPlay: Self-Evolving Vision-Language Models](cards.md#paper-visplay-questioner-reasoner-self-training) | 使用无标注图像自训练时，可同时测问题难度进阶与伪答案准确度下降。见表 2–3。 |
| 计算机视觉 | 损失函数 | [Consistency Beyond Contrast: Enhancing Open-Vocabulary Object Detection Robustness via Contextual Consistency Learning](cards.md#paper-ccl-background-invariance) | 开放词汇检测若依赖背景，可生成保对象改背景的成对样本，比较只做数据增强和追加对象一致性损失。见表 3。 |
| 机器人学 | 表征学习 | [NeuROK: Generative 4D Neural Object Kinematics](cards.md#paper-neurok-latent-object-kinematics) | 对象可动几何可先学形状到运动状态可解码的低维先验，再以同先验比较逆运动恢复。见表 1。 |
| 多模态学习 | 推理策略 | [Rationale-Enhanced Decoding for Multi-modal Chain-of-Thought](cards.md#paper-red-rationale-conditional-decoding) | 多模态思维链应通过无关依据替换检查模型是否实际用到解释，再对照显式联合两种条件分布。见表 1、4。 |
| 计算机视觉 | 模型架构 | [Spherical Voronoi: Directional Appearance as a Differentiable Partition of the Sphere](cards.md#paper-spherical-voronoi) | 用可微球面分区表达视角相关外观，镜面成分以反射方向建模。 |
| 多模态学习 | 评测与诊断 | [Understanding Counting Mechanisms in Large Language and Vision-Language Models](cards.md#paper-countscope) | 计数可先用受控重复项探测中间计数信号，再做因果干预区分局部计数和最终聚合。 |
| 多模态学习 | 推理策略 | [Test-time Ego-Exo-centric Adaptation for Action Anticipation via Multi-Label Prototype Growing and Dual-Clue Consistency](cards.md#paper-dc-pgn) | 跨第一与第三视角时，原型更新应允许多个候选动作，并用第二模态复核伪标签。 |
| 计算机视觉 | 推理压缩 | [DreamStereo: Towards Real-Time Stereo Inpainting for HD Videos](cards.md#paper-dreamstereo) | 立体视频补全可让昂贵计算优先覆盖小面积遮挡区域，再独立校验边缘一致性。 |
| 计算机视觉 | 推理策略 | [Free-Lunch Long Video Generation via Layer-Adaptive O.O.D Correction](cards.md#paper-freeloc) | 长视频扩散的外推失败应分别诊断帧相对距离和总上下文长度，按层选修正。 |
| 多模态学习 | 推理策略 | [Boosting Reasoning in Large Multimodal Models via Activation Replay](cards.md#paper-activation-replay) | 诊断 RLVR 是否改写低熵证据表征，再用基础模型同位置激活做无训练替换对照。 |
| 多模态学习 | 表示学习 | [Enhancing Part-Level Point Grounding for Any Open-Source MLLMs](cards.md#paper-part-grounding-attention-to-point) | 冻结多模态主干时，用文本条件中层注意力热图预测部件坐标。 |
| 计算机视觉 | 可解释性与诊断 | [Detecting AI-Generated Forgeries via Iterative Manifold Deviation Amplification](cards.md#paper-ifa-net-forgery-localization) | 取证检测可从自然图像重建残差出发，用初步区域预测引导第二轮定位。 |
| 多模态学习 | 模型架构 | [OneCAT: Decoder-Only Auto-Regressive Model for Unified Understanding and Generation](cards.md#paper-onecat-scale-aware-autoregression) | 统一多模态模型可在解码器内用模态专家和尺度适配，减少外部视觉组件及逐像素解码开销。 |
| 多模态学习 | 损失函数与优化 | [A Closed-Form Solution for Debiasing Vision-Language Models with Utility Guarantees Across Modalities and Tasks](cards.md#paper-closed-form-vlm-debiasing) | 跨模态去偏前确定可接受任务效用下限，再用闭式变换评估公平性取舍。 |
| 计算机视觉 | 表示学习 | [Tracking through Severe Occlusion via Event-Derived Transient Cues](cards.md#paper-evotrack-occlusion-cues) | 强遮挡时分开检查事件运动提示与外观匹配，避免遮挡模板污染。 |
| 多模态学习 | 表示学习 | [Inconsistency-aware Multimodal Schrodinger Bridge for Deepfake Localization](cards.md#paper-iamsb-asymmetric-multimodal-localization) | 多模态防御定位时依据两路证据的一致性决定融合强度和各路计算预算。 |
| 多模态学习 | 推理策略 | [ViTPrompt: Training-Free Prompt Refinement with Visual Tokens for Open-Vocabulary Detection](cards.md#paper-vitprompt-test-time-visual-box-refresh) | 开放词汇检测测试时适配应分别检查框定位和类别分数，可用首轮可信候选的视觉特征更新第二轮提示。见表 4。 |
| 多模态学习 | 模型架构 | [FoleyDirector: Fine-Grained Temporal Steering for Video-to-Audio Generation via Structured Scripts](cards.md#paper-foleydirector-temporal-audio-scripts) | 视频生成配音应将事件发生时段作为显式脚本条件，并在可见与画外事件上分别检查同步。见表 3。 |
| 机器学习基础与统计 | 训练策略 | [HCL-FF: Hierarchical and Contrastive Learning for Forward-Forward Algorithm](cards.md#paper-hcl-ff-local-hierarchical-training) | 无法端到端反传的逐层学习，可对照浅层粗类、深层细类的协调监督与局部对比学习。见表 2–4。 |
| 计算机视觉 | 优化 | [HumanBA: Human-Aware Bundle Adjustment via Global Human-Camera Decoupling](cards.md#paper-humanba-dynamic-landmark-recovery) | 动态主体占据画面时，可测试先分离主体运动后重新利用其残余观测，而不是一律掩蔽前景。见表 1–2。 |
| 机器人学 | 优化 | [Stability-Driven Motion Generation for Object-Guided Human-Human Co-Manipulation](cards.md#paper-co-manipulation-simulation-stability) | 联合操作动作生成应分别试接触先验与仿真修正，并同时检查穿模、接触与自然度。见表 2。 |
| 多模态学习 | 评测与诊断 | [Diagnosing and Repairing Unsafe Channels in Vision-Language Models via Causal Discovery and Dual-Modal Safety Subspace Projection](cards.md#paper-care-dual-modal-safety-evaluation) | 多模态安全修复验收应分别测试图像端、文本端和组合干预，再比较任务保留。见表 1–2。 |
| 机器人学 | 训练策略 | [Resolving the Stability-Plasticity Dilemma in Reinforcement Learning via Complementary Continual Critics](cards.md#paper-cd-cca) | 把快速适应与长期保留交给不同评论网络，再按观测融合价值。 |
| 多模态学习 | 训练策略 | [Hierarchically Robust Zero-shot Vision-language Models](cards.md#paper-hierarchical-robust-vlm) | 防御验收应分别测父类和叶类的鲁棒正确率，视觉语义对齐可按层级分别约束。 |
| 多模态学习 | 训练策略 | [PACT: Phase-Like Transition Constraints in Adapter-Based Continual Learning of Vision-Language Models](cards.md#paper-pact-continuous-adapters) | 持续适配不必把所有任务的方向都做正交，应检验共享方向是否改善正迁移。 |
| 计算机视觉 | 训练策略 | [Recurrent Video Masked Autoencoders](cards.md#paper-recurrent-video-mae) | 把循环状态与非对称视频掩码共同用于预训练，再分测时间任务及静态空间任务。 |
| 计算机视觉 | 优化算法 | [Lens Component Deletion based on Differentiable Ray Tracing](cards.md#paper-lens-component-deletion) | 设计紧凑成像系统时按部件对任务的贡献做消融，再联合优化剩余光学器件与恢复模型。 |
| 多模态学习 | 评测与分析 | [Beyond Caption-Based Queries in Video Moment Retrieval](cards.md#paper-beyond-caption-video-moment-retrieval) | 视频片段检索应以真实搜索语句和多答案标注检验解码器查询是否坍缩。 |
| 机器学习基础 | 评测与分析 | [Vision-Oriented Lightweight Neural Architecture Search with Budget-Adaptive Evaluation](cards.md#paper-budget-adaptive-micro-task-nas) | 算力有限时，用一组短视觉探针给候选模型排序，并按可用预算选择评估配置。 |
| 计算机视觉 | 推理优化 | [NVGS: Neural Visibility for Occlusion Culling in 3D Gaussian Splatting](cards.md#paper-nvgs-neural-visibility) | 对于重复资产，用共享视点可见性模型在高斯光栅化前过滤，不把半透明遮挡硬当作二值深度。 |
| 多模态学习 | 损失函数与优化 | [GlyphPrinter: Region-Grouped Direct Preference Optimization for Glyph-Accurate Visual Text Rendering](cards.md#paper-glyphprinter-region-grouped-dpo) | 视觉生成的瑕疵局部集中时，将偏好比较分组到区域，不让全图得分稀释字形错误。 |
| 机器学习基础 | 模型架构 | [CHEEM: Continual Learning by Reuse, New, Adapt and Skip - A Hierarchical Exploration-Exploitation Approach](cards.md#paper-cheem-hierarchical-continual-learning) | 持续学习为每个任务分别选择层的复用、新建、适配或跳过，显式平衡旧知识与容量。 |
| 计算机视觉 | 迁移与泛化 | [Mitigating Objectness Bias and Region-to-Text Misalignment for Open-Vocabulary Panoptic Segmentation](cards.md#paper-ovrcoat) | 开放词汇检测分别校准前景提议和区域文本分类，防止新类别在分类前被筛掉。 |
| 多模态学习 | 评估与诊断 | [Relational Visual Similarity](cards.md#paper-relational-visual-similarity-structural-metric) | 评估类比编辑时，把部件关系是否保持作为独立指标。表 2 显示关系得分与外观得分会出现不同排序。 |
| 机器人学 | 训练策略 | [Evo-1: Lightweight Vision-Language-Action Model with Preserved Semantic Alignment](cards.md#paper-evo1-staged-vlm-action-alignment) | 接入新动作头时，可比较先冻结语义骨干对齐动作头、再联合微调，与一开始联合训练的差异。见图 7 和图 8(b)。 |
| 计算机视觉 | 三维重建与几何建模 | [Variational Graph-based Normal Integration](cards.md#paper-variational-graph-normal-integration) | 对不规则域上的法线积分，可用区分可连续边与深度断裂边的后验，检验是否改善边界误差。见表 2。 |
| 计算机视觉 | 鲁棒性与安全 | [ReMoE: Region-Mixture Experts for Adversarially-Robust Vision Transformers](cards.md#paper-remoe-region-aware-defensive-vision) | 设计防御性视觉骨干时，可比较区域与全局特征建模，并在干净准确率之外单列鲁棒准确率。见表 4。 |
| 多模态学习 | 表征学习 | [Hyperbolic Gramian Volumes for Multimodal Alignment](cards.md#paper-hypergram-mixed-geometry-alignment) | 多模态高阶对齐可消融欧氏和双曲 Gram 体积，并比较可学习混合权重对双向检索的影响。见表 4、5。 |
| 智能体 | 评估与诊断 | [ProSoftArena: Benchmarking Hierarchical Capabilities of Multi-modal Agents in Professional Software Environments](cards.md#paper-prosoftarena-hierarchical-agent-evaluation) | 评估专业软件智能体时，单列软件内与跨软件的执行成功率，避免简单交互覆盖掉复杂工作流的低成功率。见表 3。 |
| 多模态学习 | 推理策略 | [DynamicGTR: Leveraging Graph Topology Representation Preferences to Boost VLM Capabilities on Graph QAs](cards.md#paper-dynamicgtr-query-adaptive-graph-rendering) | 图推理先按任务与模型选择输入表示，再用准确率和词元量对比固定格式。见表 4。 |
| 计算机视觉 | 模型架构 | [OpenVO: Open-World Visual Odometry with Temporal Dynamics Awareness](cards.md#paper-openvo) | 从不同帧率的视频估计运动时显式输入帧间时间，并按未见帧率和相机配置验收。 |
| 计算机视觉 | 模型架构 | [Hg-I2P: Bridging Modalities for Generalizable Image-to-Point-Cloud Registration via Heterogeneous Graphs](cards.md#paper-hg-i2p) | 跨模态配准可用区域级异构图一起校正特征及局部对应，再核查图条件是否保留有效匹配。 |
| 多模态学习 | 推理压缩 | [ZOO-Prune: Training-Free Token Pruning via Zeroth-Order Gradient Estimation in Vision-Language Models](cards.md#paper-zoo-prune) | 裁剪视觉词元前用轻量投影层的零阶响应估计敏感度，并比较直接利用注意分数。 |
| 计算机视觉 | 训练策略 | [OntoAug: Rethinking Generative Data Augmentation via Ontology Guidance](cards.md#paper-ontoaug) | 图像增强应优先保持主体语义，分开控制背景变化，再验收标签漂移。 |
| 机器人学 | 训练策略 | [EnergyAction: Unimanual to Bimanual Composition with Energy-Based Models](cards.md#paper-energyaction) | 双臂示范少时可分别利用单臂策略的能量并学习协调约束，再与双臂直接训练对照。 |
| 机器学习基础与统计 | 训练策略 | [Immunizing Models Against Harmful Long-Horizon Fine-Tuning via Contractive Optimization Dynamics](cards.md#paper-clamp-defense) | 防御性模型保护应把长程微调纳入验收，短程表现不足以代表持续保护。 |
| 计算机视觉 | 表示学习 | [From Rays to Projections: Better Inputs for Feed-Forward View Synthesis](cards.md#paper-projective-conditioning-view-synthesis) | 前馈新视角生成用目标图像平面的投影线索替代世界坐标射线。 |
| 机器学习基础 | 表示学习 | [NexusFlow: Unifying Disparate Tasks under Partial Supervision via Invertible Flow Networks](cards.md#paper-nexusflow) | 多任务标注不重叠时，以可逆坐标变换对齐特征，避免对齐损失直接丢弃原信息。 |
| 计算机视觉 | 训练与数据策略 | [MDS-VQA: Model-Informed Data Selection for Video Quality Assessment](cards.md#paper-mds-vqa) | 制定小规模新域标注预算时，以排序预测模型失败程度，再用语义多样性避免重复采样。 |
| 多模态学习 | 损失函数与优化 | [Aligning Multi-Character Narrative Image Generation with Multi-Aspect Human Preferences](cards.md#paper-adpo-multi-aspect-preferences) | 多目标生成偏好不一致时，用维度优势和奖励边际分配训练强度。 |
| 机器学习 | 训练策略 | [Mitigating Instance Entanglement in Instance-Dependent Partial Label Learning](cards.md#paper-cad-ambiguity-weighted-partial-label-learning) | 候选标签随样本特征而变化时，可对照统一加权与偏重高歧义标签的间隔惩罚。见附录表 5。 |
| 多模态学习 | 损失与奖励 | [InterRVOS: Interaction-Aware Referring Video Object Segmentation](cards.md#paper-interrvos-role-conditioned-segmentation) | 语言指令指定交互时，可给施动者和受动目标分配不同输出标记，并用角色级注意力监督和分项指标核对证据。见表 3。 |
| 机器人学 | 生成建模 | [VideoWeaver: Multimodal Multi-View Video-to-Video Transfer for Embodied Agents](cards.md#paper-videoweaver-asynchronous-view-conditioning) | 需要从已有相机视角补齐新视角时，可训练各视角位于不同加噪阶段，并对照统一阶段的跨视角一致性。见表 2。 |
| 表征学习 | 自监督学习 | [TopoSlide: Topologically-Informed Histopathology Whole Slide Image Representation Learning](cards.md#paper-toposlide-cluster-topology-pretext) | 超大图像的局部块聚合可增加拓扑自监督，让全局表示预测各语义簇的空间形态。见第 3 节与表 1。 |
| 生成模型 | 推理策略 | [ResDiT: Evoking the Intrinsic Resolution Scalability in Diffusion Transformers](cards.md#paper-resdit-position-extrapolation-resolution) | 扩散 Transformer 外推分辨率时，可先检查位置编码，再比较局部细节模块是否必要。见正文位置编码分析及表 1。 |
| 机器人学 | 推理策略 | [REACH: Explicit Recovery Behavior for Diffusion Policies](cards.md#paper-reach-error-conditioned-action-recovery) | 扩散策略执行错位时，先检测异常历史，再把不希望延续的动作模式作为负条件；可分别测提示和检测贡献。见表 4。 |
| 多模态学习 | 评估与诊断 | [Same Content, Different Answers: Cross-Modal Inconsistency in MLLMs](cards.md#paper-rest-render-equivalence-consistency) | 诊断多模态推理时，把同一题变成文本、图片、混合输入，再在 OCR 完全正确子集检查跨模态一致性。见表 1、4。 |
| 计算机视觉 | 模型架构 | [VibeToken: Scaling 1D Image Tokenizers and Autoregressive Models for Dynamic Resolution Generations](cards.md#paper-vibetoken) | 将生成分辨率和视觉词元数分开设定，按长宽比和预算验收重建及生成。 |
| 计算机视觉 | 训练策略 | [Tracking by Predicting 3-D Gaussians Over Time](cards.md#paper-video-gmae) | 把视频隐表示建模成动态三维高斯，测试追踪是否能不经显式轨迹标注自然形成。 |
| 计算机视觉 | 模型架构 | [TokenSplat: Token-aligned 3D Gaussian Splatting for Feed-forward Pose-free Reconstruction](cards.md#paper-tokensplat) | 将相机词元和场景词元采用有方向的信息交换，并分开验收位姿与渲染质量。 |
| 计算机视觉 | 训练策略 | [Iris: Bringing Real-World Priors into Diffusion Model for Monocular Depth Estimation](cards.md#paper-iris-spectral-depth) | 实域先验与合成真值可分别用于低频和高频约束，验证是否改善仿真到实拍的深度精细度。 |
| 机器人学 | 评测与诊断 | [Diagnose, Correct, and Learn from Manipulation Failures via Visual Symbols](cards.md#paper-vifailback) | 操控失败应分开考核识别、空间定位和纠正反馈，单独验证人能否把标注转为可执行信号。 |
| 多模态学习 | 评测与诊断 | [PAS: Prelim Attention Score for Detecting Object Hallucinations in Large Vision-Language Models](cards.md#paper-prelim-attention-hallucination) | 检测物体幻觉时区分视觉条件与前文条件，先测额外推理前能否用历史注意做代理。 |
| 多模态学习 | 评测与分析 | [When Understanding Becomes a Risk: Authenticity and Safety Risks in the Emerging Image Generation Paradigm](cards.md#paper-unified-image-generation-risk-audit) | 比较生成器安全性时单独统计损坏输出，并按生成架构验证取证检测器。 |
| 机器人学 | 损失函数与优化 | [PAMotion: Physics-Aware Motion Generation for Full-Body Interaction with Multiple Objects](cards.md#paper-pamotion-contact-acceleration) | 人体物体运动生成时，将物体非重力加速度作为接触一致性的软监督。 |
| 机器学习基础 | 推理优化 | [Rejection Mixing: Fast Semantic Propagation of Mask Tokens for Efficient DLLM Inference](cards.md#paper-remix-continuous-decoding) | 扩散语言模型并行解码时，先交换连续候选的信息，再提交离散词元，不确定位置退回掩码。 |
| 计算机视觉 | 知识蒸馏 | [Bootstrapping Video Semantic Segmentation Model via Distillation-assisted Test-Time Adaptation](cards.md#paper-ditta-video-distillation) | 只能短时调用视频教师时，用开头片段蒸馏时序一致性，随后让轻量学生独立预测。 |
| 计算机视觉 | 评测与分析 | [Scaling View Synthesis Transformers](cards.md#paper-svsm-compute-matched-scaling) | 比较新视角模型架构时对齐训练 FLOPs，检验编码器—解码器是否真的不如纯解码器。 |
| 多模态学习 | 微调与适配 | [Multi-modal Test-time Adaptation via Adaptive Probabilistic Gaussian Calibration](cards.md#paper-multimodal-gaussian-tta) | 测试时音视频质量不对称时，用类别条件高斯校准并纠正跨模态分布偏差。 |
| 计算机视觉 | 训练策略 | [Cross-Domain Few-Shot Segmentation via Multi-view Progressive Adaptation](cards.md#paper-mpa-progressive-query-view-adaptation) | 目标域只有少量监督时，可分别提高增强视图的难度和数量，并比较各进度对适配效果的影响。见表 7。 |
| 多模态学习 | 对比学习 | [No Hard Negatives Required: Concept Centric Learning Leads to Compositionality without Degrading Zero-shot Capabilities of Contrastive Models](cards.md#paper-c2lip-concept-phrase-contrastive-binding) | 视觉语言模型的属性绑定不佳时，可先增加短概念短语监督，再核对概念条件池化的边际收益和通用检索表现。见表 5。 |
| 多模态学习 | 训练策略 | [CCF: Complementary Collaborative Fusion for Domain Generalized Multi-Modal 3D Object Detection](cards.md#paper-ccf-complementary-sensor-masking) | 一个传感器主导融合时，可对照互补空间遮盖与原训练，检验弱模态是否成为有用后备。见表 3。 |
| 多模态学习 | 推理策略 | [Hilbert-Geo: Solving Solid Geometric Problems by Neural-Symbolic Reasoning](cards.md#paper-hilbert-geo-formal-parse-solver-control) | 对图文推理接符号求解器时，可以用人工形式化输入测试求解上限，再与真实解析的端到端结果对照。见表 1 及第 6.3 节。 |
| 机器人学 | 表征学习 | [OpenT2M: No-frill Motion Generation with Open-source, Large-scale, High-quality Data](cards.md#paper-opent2m-partwise-2d-motion-quantization) | 动作表示可以按身体部位保留空间轴并与时间联合量化；先在不同动作复杂度的数据上实测重建，再决定是否换分词器。见表 6。 |
| 计算机视觉 | 训练策略 | [GenMask: Adapting DiT for Segmentation via Direct Mask Generation](cards.md#paper-genmask) | 根据输出潜分布设定扩散采样日程，二值掩码与自然图像分开对照。 |
| 多模态学习 | 模型架构 | [DPL: Decoupled Prototype Learning for Enhancing Robustness of Vision-Language Transformers to Missing Modalities](cards.md#paper-dpl-missing-modality) | 缺失模态时不仅调整输入提示，也应让分类原型按实际可用模态变化。 |
| 机器学习基础与统计 | 训练策略 | [FedCART: Tackling Long-Tailed Distributions in Federated Adversarial Training via Classifier Refinement](cards.md#paper-fedcart-defense) | 联邦稳健训练要按类别频率分拆干净与稳健表现，再判断是否进行分类器精化。 |
| 机器学习基础与统计 | 训练策略 | [Reading Your Actions: Learning Generalizable Action Representations via Pre-training AEMG](cards.md#paper-aemg) | 生理时序预训练可先将局部收缩与跨时模式分成不同层级，再按未见受试者和设备分别验证。 |
| 计算机视觉 | 训练策略 | [Frequency-Aware Affinity for Weakly Supervised Semantic Segmentation](cards.md#paper-dfa-frequency-affinity) | 弱监督分割扩散伪标签时可将低频语义和高频边界作为不同传播信号。 |
| 多模态学习 | 训练与数据策略 | [OpenVision 2: A Family of Generative Pretrained Visual Encoders for Multimodal Learning](cards.md#paper-openvision-2-generative-pretraining) | 面向多模态解码器预训练视觉编码器时，把只用描述损失作为单独受控的低成本基线。 |
| 多模态学习 | 评测与分析 | [FailureAtlas: Mapping the Failure Landscape of T2I Models via Active Exploration](cards.md#paper-failureatlas) | 审计生成模型时搜索导致稳定错误的最小概念组合，并用训练分布频次检查覆盖缺口。 |
| 机器人学 | 强化学习 | [Saliency-Guided Representation with Consistency Policy Learning for Visual Unsupervised Reinforcement Learning](cards.md#paper-srcp-visual-unsupervised-rl) | 视觉无监督强化学习先单独学习动力相关表征，再估计后继测度和训练技能策略。 |
| 计算机视觉 | 表示学习 | [I-Scene: 3D Instance Models are Implicit Generalizable Spatial Learners](cards.md#paper-i-scene-instance-generator) | 场景训练数据少时，用预训练单物体生成器的几何先验在随机组合场景中学习布局。 |
| 机器学习基础 | 评测与分析 | [When Pretty Isn't Useful: Investigating Why Modern Text-to-Image Models Fail as Reliable Training Data Generators](cards.md#paper-synthetic-data-aesthetic-bias) | 选择合成训练数据生成器时，用真实下游准确率及覆盖度作门槛，不以图好看或提示匹配选型。 |
| 机器学习基础 | 训练与数据策略 | [Cleaning the Pool: Progressive Filtering of Unlabeled Pools in Deep Active Learning](cards.md#paper-refine-active-learning) | 每轮主动学习先用多个策略交替缩小未标注池，再按不同信息价值的覆盖选最终批次。 |
| 多模态学习 | 推理策略 | [Thinking with Drafts: Speculative Temporal Reasoning for Efficient Long Video Understanding](cards.md#paper-spectemp-draft-frame-proposal) | 长视频推理可以把密集找帧交给轻量模型，将判断和复核留给大模型，并以准确率和实际时延一起评价。见表 3、4。 |
| 机器学习 | 数据蒸馏 | [Dataset Distillation by Influence Matching](cards.md#paper-infmatch-terminal-data-influence) | 合成数据蒸馏可直接匹配样本对最终参数的影响，并用下游检索与分类对比轨迹匹配。见第 4、5 节。 |
| 计算机视觉 | 模型效率 | [Efficient Video Object Segmentation and Tracking with Recurrent Dynamic Submodel](cards.md#paper-rds-mask-conditioned-video-routing) | 视频推理的条件路由可以使用上一帧的预测掩膜和当前帧特征，比较更长预测记忆是否值得。见表 4、5 和图 7。 |
| 多模态学习 | 表征学习 | [Zero-Shot Depth Completion with Vision-Language Model](cards.md#paper-sparse-depth-vlm-mask-guidance) | 当几何传感器只给出少量观测时，可以把观测数值和观测位置分开编码，测量位置本身对补全误差的影响。见表 5。 |
| 生成模型 | 推理策略 | [Towards Holistic Modeling for Video Frame Interpolation with Auto-regressive Diffusion Transformers](cards.md#paper-ldf-vfi-skip-concatenate-sampling) | 长序列自回归生成出现漂移时，可以检验跳过最近生成片段作为条件的采样次序，并比较块边界一致性。见图 5、表 3。 |
| 机器人学 | 检索增强 | [R4: Retrieval-Augmented Reasoning for Vision-Language Models in 4D Spatio-Temporal Space](cards.md#paper-r4-semantic-spatiotemporal-memory-retrieval) | 空间问答的情景记忆应分别评估语义、空间和时间索引，并检验定位键加入语义检索后的增量。见表 5。 |
| 机器人学 | 模型架构 | [SemanticVLA: Towards Semantic Reasoning over Action Memorization via Synergistic Explicit Trace and Latent Action Planning](cards.md#paper-semanticvla) | 把可解释轨迹和隐动作计划作为两路接口，分别检验语义泛化与精细控制。 |
| 计算机视觉 | 表示学习 | [AERGS-SLAM: Auto-Exposure-Robust Stereo 3D Gaussian Splatting SLAM](cards.md#paper-aergs-slam) | 让定位用光照鲁棒特征，渲染端单独估计曝光。 |
| 多模态学习 | 模型架构 | [Rosetta Stone For Unified MLLMs: A Unified Tokenizer to Decipher Understanding and Generation](cards.md#paper-rosetta-unified-tokenizer) | 按量化层分配语义和纹理目标，并分开审计理解与生成。 |
| 计算机视觉 | 异常检测 | [Anomaly as Non-Conformity via Training-Free Graph Laplacian Energy Minimization](cards.md#paper-anoco) | 少正常样本时，试用与固定参考对齐所需的位移替代最近邻距离。 |
| 多模态学习 | 训练策略 | [TTL: Test-time Textual Learning for OOD Detection with Pretrained Vision-Language Models](cards.md#paper-ttl-ood) | 面对未知类变化，可用冻结视觉编码和自更新负文本提示校准，而非增加固定负类词表。 |
| 计算机视觉 | 自监督学习 | [Towards Stable Self-Supervised Object Representations in Unconstrained Egocentric Video](cards.md#paper-egovit) | 跨帧一致性应作用在可信对象原型上，同时单测几何先验是否必要。 |
| 计算机视觉 | 推理压缩 | [Ultra-Low Bitrate Perceptual Image Compression with Shallow Encoder](cards.md#paper-aeic) | 边缘端预算更紧时可把容量移向解码端，并用跨端蒸馏稳定浅编码。 |
| 多模态学习 | 输入表示 | [T2SGrid: Temporal-to-Spatial Gridification for Video Temporal Grounding](cards.md#paper-t2sgrid) | 当视觉模型更擅长空间注意力时，把局部时间顺序编码为图像排布，并保留全局时间锚。 |
| 机器人学 | 推理优化 | [OVI-MAP: Open-Vocabulary Instance-Semantic Mapping](cards.md#paper-ovi-map) | 在线语义建图先更新类别无关实例，再从少量代表视图给实例添加语义。 |
| 多模态学习 | 可解释性与诊断 | [What Do Visual Tokens Really Encode? Uncovering Sparsity and Redundancy in Multimodal Large Language Models](cards.md#paper-embedlens-visual-token-sparsity) | 压缩视觉词元或跳层前，先用语义探针和随机等量裁剪定位真正承载实例信息的词元。 |
| 多模态学习 | 训练与数据策略 | [Less is More: Data-Efficient Adaptation for Controllable Text-to-Video Generation](cards.md#paper-simple-synthetic-video-controls) | 学习新视频物理控制时，先用因素独立的简单合成数据，对照逼真数据是否引入混杂。 |
| 多模态学习 | 训练与数据策略 | [Socratic-Geo: Synthetic Data Generation and Cross-Modal Geometric Reasoning via Multi-Agent Interaction](cards.md#paper-socratic-geo-failure-directed-synthesis) | 训练几何推理时利用求解失败轨迹驱动可验证的合成数据补齐。 |
| 机器学习基础 | 损失函数与优化 | [Drainage: A Unifying Framework for Addressing Class Uncertainty](cards.md#paper-drainage-class-uncertainty) | 噪声标签或类歧义明显时，给输出层预留可学习的拒判概率。 |
| 计算机视觉 | 自监督学习 | [Learning Cross-View Object Correspondence via Cycle-Consistent Mask Prediction](cards.md#paper-cycle-consistent-cross-view-masks) | 跨视角对象对应缺少标注时，用预测掩码回映原视角约束训练和测试时适配。 |
| 多模态学习 | 生成建模 | [Can We Build Scene Graphs, Not Classify Them? FlowSG: Progressive Image-Conditioned Scene Graph Generation with Flow Matching](cards.md#paper-flowsg-mixed-state-scene-graph-flow) | 如果输出含连续坐标和离散关系，可各自定义流更新，再用共享的节点与边消息协调两类变量。见表 4。 |
| 表征学习 | 推理策略 | [SATTC: Structure-Aware Label-Free Test-Time Calibration for Cross-Subject EEG-to-Image Retrieval](cards.md#paper-sattc-frozen-retrieval-hubness-calibration) | 跨分布检索先建立归一化和候选白化基线，再用邻域结构重排，并分别核查 Top-1 与 Top-5。见表 1。 |
| 机器人学 | 持续学习 | [Lifelong Imitation Learning with Multimodal Latent Replay and Incremental Adjustment](cards.md#paper-latent-replay-angular-task-margin) | 顺序模仿学习可在有限回放内存下存多模态潜表示，再用角间隔约束任务表示更新并单测遗忘。见表 1、2。 |
| 多模态学习 | 评估与诊断 | [Concept Regions Matter: Benchmarking CLIP with a New Cluster-Importance Approach](cards.md#paper-cci-concept-cluster-occlusion-diagnosis) | 诊断图文模型的背景依赖时，可以按特征簇做区域删除，并独立改变前景和背景以区分错误来源。见表 2–4。 |
| 多模态学习 | 评估与诊断 | [Fine-Grained Multi Image Object Hallucination Benchmark](cards.md#paper-mioh-joint-versus-decomposed-visual-verification) | 多图任务出现物体幻觉时，用完全相同图片对照联合回答与逐图作答后汇总，可检查错误是在感知还是跨图整合发生。见图 5。 |
| 计算机视觉 | 模型效率 | [Co-Me: Confidence Guided Token Merging for Visual Geometric Transformers](cards.md#paper-come-confidence-guided-geometric-token-merging) | 多视角几何模型加速时，可按置信度选择合并对象，并随相机重叠程度报告耗时和深度误差。见表 1。 |
| 计算机视觉 | 模型架构 | [Stereo World Model: Camera-Guided Stereo Video Generation](cards.md#paper-stereoworld) | 双目生成可用极线结构节省跨视注意力，把相机姿态作为相对位置条件。 |
| 多模态学习 | 训练策略 | [MotionEnhancer: Leveraging Video Diffusion for Motion-Enhanced Vision-Language Models](cards.md#paper-motionenhancer) | 动作细节不足时，可用视频生成模型的运动注意力监督理解模型。 |
| 多模态学习 | 模型架构 | [OrionEdit: Bridging Reference and Source Images for Generalized Cross-Image Editing](cards.md#paper-orionedit) | 参考图与源图各有不同职责时，可分别约束参数子空间和信息流向，并与随机遮罩对照。 |
| 多模态学习 | 推理加速 | [Accelerating Streaming Video Large Language Models via Hierarchical Token Compression](cards.md#paper-streaming-token-compression) | 先测哪段延迟占主导，再分别压缩视觉编码重算和语言模型输入。 |
| 多模态学习 | 检索 | [G-MIXER: Geodesic Mixup-based Implicit Semantic Expansion and Explicit Semantic Re-ranking for Zero-Shot Composed Image Retrieval](cards.md#paper-g-mixer) | 图文组合意图不唯一时，先用多个几何插值候选覆盖语义，再用显式语义排序。 |
| 计算机视觉 | 表示学习 | [Reconstructing CLIP for Open-Vocabulary Dense Perception](cards.md#paper-denserc) | 重用 CLIP 做开放词汇定位时，先检查值嵌入与空间聚合，再决定是否改变注意力头权重。 |
| 多模态学习 | 损失函数 | [Cross-Axis Feature Fusion with Joint-Wise Motion Difference Prediction for Text-Based 3D Human Motion Editing](cards.md#paper-jointwise-motion-delta) | 局部动作编辑可用对齐后的部件变化量做辅助监督，保护未编辑关节。 |
| 计算机视觉 | 损失函数与优化 | [GeCo: Geometry-Consistent Regularization for Domain Generalized Semantic Segmentation](cards.md#paper-geco-geometry-consistent-regularization) | 对基础特征作域泛化微调时，用局部曲率控制扰动、用测地关系保持结构。 |
| 计算机视觉 | 表示学习 | [Gen3R: 3D Scene Generation Meets Feed-Forward Reconstruction](cards.md#paper-gen3r-aligned-geometry-latents) | 生成动态视图又需要可查询几何时，学习对齐的外观及几何潜变量，并在同一轨迹联合采样。 |
| 科学与医学 AI | 微调与适配 | [Unlocking Positive Transfer in Incrementally Learning Surgical Instruments: A Self-reflection Hierarchical Prompt Framework](cards.md#paper-hierarchical-prompts-positive-transfer) | 增量类别有共享部件时，按类别及部件搭建提示树，用前向和反向迁移指标检查新增知识。 |
| 计算机视觉 | 推理优化 | [AVGGT: Rethinking Global Attention for Accelerating VGGT](cards.md#paper-avggt-global-attention) | 多视图模型加速时先测各层跨视图作用，再将早层改为逐帧并对其余全局键值采样。 |
| 计算机视觉 | 模型架构 | [Restore, Assess, Repeat: A Unified Framework for Iterative Image Restoration](cards.md#paper-rar-latent-restoration-assessment) | 多步图像恢复时在潜空间内同时判断退化和复核质量，减少反复解码。 |
| 计算机视觉 | 自监督学习 | [TimeBridge: Self-Supervised Video Representation Learning via Start-End Joint Embedding and In-Between Frame Prediction](cards.md#paper-timebridge) | 自监督视频学习时同时对齐起止帧表示，并要求从两端恢复中间帧。 |
| 多模态学习 | 强化学习 | [Thinking With Videos: Multimodal Tool-Augmented Reinforcement Learning for Long Video Reasoning](cards.md#paper-vital-difficulty-balanced-multitask-grpo) | 联合优化问答正确率与时间定位时，可先比较普通 GRPO 和任务、样本难度加权，核对不同奖励量尺上的表现。见表 5。 |
| 多模态学习 | 推理策略 | [Wavelet-based Frame Selection by Detecting Semantic Boundary for Long Video Understanding](cards.md#paper-wfs-semantic-boundary-wavelet-selection) | 按查询压缩视频时，可先在相关性序列里找低频语义变化，再在段内选帧，比较直接用原始分数找边界。见表 4。 |
| 智能体 | 损失与奖励 | [CodeV: Code with Images for Faithful Visual Reasoning via Tool-Aware Policy Optimization](cards.md#paper-codev-evidence-based-visual-tool-reward) | 视觉工具智能体可把奖励落在工具输出是否包含问题证据，并把忠实调用率与答案准确率分开报告。见图 5、表 2。 |
| 机器学习 | 模型效率 | [Neural Differentiation in Deep Networks: A Theoretical Framework for Expressivity and Representational Diversity](cards.md#paper-neural-differentiation-loss-aware-pruning) | 结构化剪枝可以基于损失与表征差异估计删除代价，同时检查给定稀疏度的准确率和实际吞吐。见理论章节与表 2。 |
| 多模态学习 | 损失与奖励 | [STAR-R1: Multi-View Spatial TrAnsformation Reasoning by Reinforcing Multimodal LLMs](cards.md#paper-star-r1-referent-selection-rewards) | 训练多视角推理时，可分别奖励指代物体选择和最终答案，避免仅靠答案奖励时对齐错误。见表 3。 |
| 计算机视觉 | 生成模型 | [ShapeAR: Generating Editable Shape Layers via Autoregressive Diffusion](cards.md#paper-shapear) | 把难以一次求解的可编辑分解改写为依赖当前合成画布的逐层生成。 |
| 计算机视觉 | 生成模型 | [L3DR: 3D-aware LiDAR Diffusion and Rectification](cards.md#paper-l3dr) | 快速生成保留二维范围视图，纠正边缘与表面伪影时再回到三维空间。 |
| 机器学习基础与统计 | 测试时适应与推理 | [Towards Stable Federated Continual Test-Time Adaptation in Wild World](cards.md#paper-bpfedctta) | 把无标签局部自适应与是否写回共享模型分成两个决策。 |
| 计算机视觉 | 训练策略 | [Beyond Ground-Truth: Leveraging Image Quality Priors for Real-World Image Restoration](cards.md#paper-iqpir) | 当配对标签质量参差不齐时，用显式质量条件保留不同等级的数据，推理选择目标质量。 |
| 机器人学 | 推理与规划 | [MindDriver: Introducing Progressive Multimodal Reasoning for Autonomous Driving](cards.md#paper-minddriver) | 需把语义推理转成动作时，可尝试预测与决策直接相关的物理中间态，并对各阶段分开消融。 |
| 多模态学习 | 推理压缩 | [Hybrid Token Compression for Vision-Language Models](cards.md#paper-htc-vlm) | 极端视觉 token 压缩时为可辨对象保留离散语义锚点，并留连续通道承载细节。 |
| 计算机视觉 | 训练策略 | [Trust-calibrated Collaborative Learning for Long-Tailed Visual Recognition](cards.md#paper-tcl-long-tail) | 互蒸馏时应筛掉专家的错误共识，并对尾类单独补偿监督。 |
| 多模态学习 | 微调与适配 | [Parameter-Efficient Adaptation for MLLMs via Implicit Modality Decomposition](cards.md#paper-imod-modality-decomposition) | 多模态 LoRA 中将文本、非文本和共享更新分开，并约束干扰与对齐。 |
| 多模态学习 | 损失函数与优化 | [Resolving Endpoint Underfitting in Diffusion Bridges via Noise Alignment](cards.md#paper-nadb-noise-aligned-bridge) | 扩散桥终点附近欠拟合时，先核对输入和回归目标的噪声尺度，再修正监督。 |
| 计算机视觉 | 损失函数与优化 | [FaithFusion: Harmonizing Reconstruction and Generation via Pixel-wise Information Gain](cards.md#paper-faithfusion-information-gain) | 混合重建与生成时，以同一个像素级信息增益分数选择修补位置，以及控制编辑蒸馏回三维模型的权重。 |
| 机器学习基础 | 表示学习 | [Pointer-CAD: Unifying B-Rep and Command Sequences via Pointer-based Edges & Faces Selection](cards.md#paper-pointer-cad) | 让序列模型输出操作时，用指针选择当前结构中的实体，避免把动态对象列表硬编码到词表。 |
| 机器人学 | 表示学习 | [VarSplat: Uncertainty-aware 3D Gaussian Splatting for Robust RGB-D SLAM](cards.md#paper-varsplat-uncertainty) | 高斯 SLAM 中学习逐图元方差，并用与渲染一致的像素不确定度为追踪和回环定权。 |
| 多模态学习 | 推理优化 | [StreamDiT: Real-Time Streaming Text-to-Video Generation](cards.md#paper-streamdit-moving-buffer) | 流式视频生成用移动缓冲区维护多噪声级片段，再按片段蒸馏减少函数评估。 |
| 机器人学 | 规划与控制 | [GuideFlow: Constraint-Guided Flow Matching for Planning in End-to-End Autonomous Driving](cards.md#paper-guideflow-constraints-inside-trajectory-generation) | 可在候选轨迹生成期间约束状态和速度场，并将进度与约束指标分开比较。见表 5。 |
| 生成模型 | 损失与奖励 | [The Image as Its Own Reward: Reinforcement Learning with Adversarial Reward for Image Generation](cards.md#paper-adv-grpo-reference-updated-image-reward) | 固定偏好分数引发图像质量失真时，可比较加入由真实参照图与当前产物持续更新的奖励，并做独立人评。见表 1 和第 4.3 节。 |
| 多模态学习 | 表征学习 | [Decompose and Transfer: CoT-Prompting Enhanced Alignment for Open-Vocabulary Temporal Action Detection](cards.md#paper-pda-phasewise-open-vocabulary-action-alignment) | 对未见动作做时间定位时，可以把类级标签拆为阶段，再用阶段数消融去确定效果与开销。见表 3。 |
| 计算机视觉 | 时序建模 | [Event Stream Filtering via Probability Flux Estimation](cards.md#paper-edfilter-inter-event-probability-flux) | 过滤异步感知时，将事件间隔作为重建连续状态的证据并比较能否保留快速动态。见表 1、4。 |
| 生成模型 | 推理策略 | [Layer-wise Instance Binding for Regional and Occlusion Control in Text-to-Image Diffusion Transformers](cards.md#paper-layerbind-early-latent-occlusion-composition) | 要控制对象遮挡顺序，可在去噪早期按深度顺序合并局部实例潜状态，再共享语义细化。见表 1、3。 |
| 计算机视觉 | 三维重建与几何建模 | [Efficient Unrolled Networks for Large-Scale 3D Inverse Problems](cards.md#paper-partitioned-unrolling-global-normal-operator) | 大体积逆问题可将域分块与全局数据一致性联合起来，先验证分块节省显存，再看近似算子值不值得。见表 4。 |
| 生成模型 | 参数高效微调 | [SliderEdit: Continuous Image Editing with Fine-Grained Instruction Control](cards.md#paper-slideredit-shared-continuous-instruction-adapters) | 多指令编辑可给每条指令保留独立连续强度，用共享低秩参数支持新编辑，并单测连续性和编辑串扰。见表 1、2。 |
| 多模态学习 | 生成模型 | [Open the Motion Door: Atomic Motion Decomposition and Recomposition for Open-Vocabulary Motion Generation](cards.md#paper-atomic-motion-recomposition) | 新指令超出训练词汇时，将文本先映射到可重组的身体部位动作，再检查组合泛化。 |
| 计算机视觉 | 表示学习 | [Faithful Contouring: Near-Lossless 3D Voxel Representation Free from Iso-surface](cards.md#paper-faithful-contouring) | 输入可能非水密且需保留内层或锐边时，考虑直接编码局部表面而非依赖隐式等值面。 |
| 多模态学习 | 推理策略 | [Image Generation from Contextually-Contradictory Prompts](cards.md#paper-stage-aware-prompt-decomposition) | 罕见组合被生成先验覆盖时，可把冲突概念放到不同去噪阶段表达，并对去噪时间段做扰动验证。 |
| 多模态学习 | 损失函数 | [See Less, See Right: Bi-directional Perceptual Shaping For Multimodal Reasoning](cards.md#paper-bips) | 同时训练证据充分性与必要性，让模型对保留答案证据的裁剪稳定，对遮掉关键证据敏感。 |
| 机器学习基础与统计 | 强化学习 | [Mesh-Pro: Asynchronous Advantage-guided Ranking Preference Optimization for Artist-style Quadrilateral Mesh Generation](cards.md#paper-mesh-pro-arpo) | 生成样本昂贵时，可比较异步在线偏好排序和同步策略更新，并监测训练效率与几何奖励。 |
| 多模态学习 | 模型架构 | [Causality in Video Diffusers is Separable from Denoising](cards.md#paper-separable-causal-diffusion) | 先逐层测去噪步间冗余与跨帧依赖，再将可复用的时序编码移出迭代循环。 |
| 多模态学习 | 模型分析 | [An Empirical Study on How Video-LLMs Answer Video Questions](cards.md#paper-video-llm-layer-knockout) | 决定何处丢弃或缩窗视频 token 前，先按层定位时空信息进入推理的关键窗口。 |
| 计算机视觉 | 条件生成 | [Task-Oriented Data Synthesis and Control-Rectify Sampling for Remote Sensing Semantic Segmentation](cards.md#paper-todsynth-control-rectify) | 合成带分割标签的训练样本时，在采样早期以任务损失校正语义掩码一致性。 |
| 机器学习基础 | 损失函数与优化 | [Robust Spiking Neural Networks by Temporal Mutual Information](cards.md#paper-temporal-mutual-information-snn) | 训练脉冲网络追求鲁棒性时，针对时序潜表示施加互信息正则。 |
| 机器人学 | 表示学习 | [Recurrent Reasoning with Vision-Language Models for Estimating Long-Horizon Embodied Task Progress](cards.md#paper-r2vlm-recurrent-progress) | 估计长程任务进度时逐段处理视频，只向下一段传递可更新的任务状态摘要。 |
| 多模态学习 | 训练与数据策略 | [SRA 2: Variational Autoencoder Self-Representation Alignment  for Efficient Diffusion Training](cards.md#paper-sra2-vae-feature-alignment) | 训练扩散模型时先尝试把中层对齐到已有 VAE 特征，省去额外表征编码器。 |
| 多模态学习 | 损失函数与优化 | [Correspondence-Attention Alignment for Multi-View Diffusion Models](cards.md#paper-cameo-correspondence-attention) | 多视角扩散训练中直接监督一层跨视图注意力的几何对应，作为提高视角一致性的低开销选择。 |
| 机器学习基础 | 可解释性与诊断 | [CIGMA: Causal Information-Gain Mechanistic Attribution of Attention Heads in Vision Transformers](cards.md#paper-cigma-causal-head-attribution) | 模型依赖背景捷径时，用去对象和去背景两种成对干预区分注意力头处理的证据。 |
| 多模态学习 | 损失与奖励 | [AToken: A Unified Tokenizer for Vision](cards.md#paper-atoken-covariance-loss-visual-tokenizer) | 视觉编码重建若在对抗训练中不稳定，可先分解重建误差，再检验特征二阶统计损失能否代替判别器。见图 3、表 1。 |
| 计算机视觉 | 表征学习 | [Towards Generalized Representations for Low-Light Understanding: When Signal Constancy Meets Semantic Enrichment](cards.md#paper-uniprior-invariant-target-self-correlation-alignment) | 光照分布变化时，可以对照直接对齐特征与对齐图像内部关系，并用重建不变量为模型提供稳定目标。见表 3。 |
| 多模态学习 | 表征学习 | [Tri-Subspaces Disentanglement for Multimodal Sentiment Analysis](cards.md#paper-tsd-pair-specific-shared-subspaces) | 三模态以上的融合可检验是否保留两两共享的表示，而不把信号只分为全局共有与模态私有。见表 3。 |
| 计算机视觉 | 三维重建与几何建模 | [Event-based Visual Deformation Measurement](cards.md#paper-ais-neighbor-seeded-deformation-optimization) | 局部形变拟合不稳时，可以让高置信的子域引导邻域搜索，用收敛时间和有效子域比例核对。见表 3。 |
| 多模态学习 | 表征学习 | [Masking Matters: Unlocking the Spatial Reasoning Capabilities of LLMs for 3D Scene-Language Understanding](cards.md#paper-3d-slim-geometry-instruction-attention-mask) | LLM 接收无序对象集合时，可将对象间注意力从因果顺序改为随空间密度调整的邻域，并允许对象直接关注指令。见表 3、4。 |
| 机器人学 | 生成建模 | [GeoDexGrasp: Geometry-aware Generation for Data-efficient and Physics-plausible Dexterous Grasping](cards.md#paper-geodexgrasp-factorized-geometric-conditioning) | 抓取生成可按几何因素分配条件，先用姿态和交互方向规划根部旋转，再用形状和尺寸拟合手型。见表 3。 |
| 机器学习基础与统计 | 损失函数 | [Beyond Soft Label: Dataset Distillation via Orthogonal Gradient Matching](cards.md#paper-orthogonal-gradient-matching) | 预算有限且只用硬标签时，数据蒸馏应测梯度方向是否随合成集保留。 |
| 机器人学 | 模型架构 | [CUBic: Coordinated Unified Bimanual Perception and Control Framework](cards.md#paper-cubic-bimanual) | 两控制臂既需局部自治也需协调时，可保留各自离散码本，用共享映射协调。 |
| 多模态学习 | 训练策略 | [CHIPS: Efficient CLIP Adaptation via Curvature-aware Hybrid Influence-based Data Selection](cards.md#paper-chips-data-selection) | 领域适配预算有限时，按影响力同时考虑目标收益与通用能力保留。 |
| 机器人学 | 推理与规划 | [Fast-ThinkAct: Efficient Vision-Language-Action Reasoning via Verbalizable Latent Planning](cards.md#paper-fast-thinkact) | 把可解释推理留作训练监督，部署使用能解码为语言的潜计划以减小决策时延。 |
| 多模态学习 | 推理压缩 | [Geometry-Guided 3D Visual Token Pruning for Video-Language Models](cards.md#paper-geo3dpruner) | 多视角输入压缩先按同一3D位置去重，再按空间覆盖选保留 token。 |
| 计算机视觉 | 生成模型 | [DiP: Taming Diffusion Models in Pixel Space](cards.md#paper-dip-pixel-diffusion) | 高分辨率像素扩散中，用大 patch 构造全局上下文，让局部头承担像素细节。 |
| 计算机视觉 | 强化学习 | [ReasonX: MLLM-Guided Intrinsic Image Decomposition](cards.md#paper-reasonx) | 真实图像无密集真值时，可收集教师相对判断，并与预测中可算出的物理关系比较作为奖励。 |
| 机器学习基础与统计 | 强化学习 | [ReLaX: Reasoning with Latent Exploration for Large Reasoning Models](cards.md#paper-relax-latent-exploration) | 策略探索应同时看生成 token 多样性和中间状态动态的多样性。 |
| 计算机视觉 | 表示学习 | [Residual Primitive Fitting of 3D Shapes with SuperFrusta](cards.md#paper-resfit-superfrusta) | 拟合可编辑的几何基元时，从未解释残差增添基元，直接平衡覆盖和基元数量。 |
| 计算机视觉 | 表示学习 | [BrickNet: Graph-Backed Generative Brick Assembly](cards.md#paper-bricknet-connectivity-programs) | 当零件装配受连接约束时，用连接关系而非裸三维位姿作为自回归生成单位。 |
| 多模态学习 | 可解释性与诊断 | [Diffusion Mental Averages](cards.md#paper-diffusion-mental-averages) | 审计生成器的概念原型时，比较去噪轨迹的语义中心，避免直接均值造成模糊。 |
| 多模态学习 | 表示学习 | [RNED: Rotary Number Encoding and Decoding for Medical VLMs](cards.md#paper-rned-continuous-number-tokens) | 多模态回归用数值相关旋转编码连续数，在隐层解码实数，避免把数值当普通离散字符串。 |
| 计算机视觉 | 自监督学习 | [LumiMotion: Improving Gaussian Relighting with Scene Dynamics](cards.md#paper-lumimotion-dynamic-inverse-rendering) | 动态逆渲染利用同一表面随运动经过不同光照的观测，辅助分离材质和照明。 |
