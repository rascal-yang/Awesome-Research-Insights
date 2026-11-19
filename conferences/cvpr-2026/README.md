# CVPR 2026

[首页](../../README.md) · [官方论文目录](https://openaccess.thecvf.com/CVPR2026?day=all) · [筛选底册](papers.tsv)

CVF Open Access 主会目录含 4,042 个不同的论文页面。已筛选 299 篇，其中 219 篇暂收录、80 篇排除，另有 3,743 篇待筛。最终按贡献指南统一排名，收录上限为 50%。

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
