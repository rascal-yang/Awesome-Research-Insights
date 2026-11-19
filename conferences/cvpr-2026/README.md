# CVPR 2026

[首页](../../README.md) · [官方论文目录](https://openaccess.thecvf.com/CVPR2026?day=all) · [筛选底册](papers.tsv)

CVF Open Access 主会目录含 4,042 个不同的论文页面。已筛选 2,757 篇，其中 1,744 篇暂收录、1,013 篇排除，另有 1,285 篇待筛。最终按贡献指南统一排名，收录上限为 50%。

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
| 多模态学习 | 表征学习 | [Distribution-Aligned Multimodal Fusion for Robust Object Detection](cards.md#paper-clean-pretraining-feature-target-multimodal-fusion) | 训练只包含少数退化时，可让融合特征对齐冻结检测器已熟悉的正常分布，并用未见退化对照。见表 3。 |
| 生成模型 | 模型效率 | [DRiffusion: Draft-and-Refine Process Parallelizes Diffusion Models with Ease](cards.md#paper-driffusion-parallel-draft-noise-refinement) | 多设备扩散加速可比较先草拟未来状态并批量计算去噪，再以常规轨迹细化，检查延迟、显存和图像质量。见表 2。 |
| 机器学习 | 持续学习 | [From Selection to Scheduling: Federated Geometry-Aware Correction Makes Exemplar Replay Work Better under Continual Dynamic Heterogeneity](cards.md#paper-feat-shared-prototype-geometry-replay) | 联邦回放发生少数类塌缩时，可用跨客户端共享固定原型作角度锚点，再单测训练时几何对齐和推理校正。见表 2。 |
| 多模态学习 | 推理策略 | [STAR: Test-Time Adaptation Can Enhance Universal Prompt Learning for Vision-Language Models](cards.md#paper-star-separability-gated-test-time-prompts) | 测试流混有域外数据时，用可分性门控划分提示更新与伪标注，避免把低熵直接当作高可信。见表 3。 |
| 机器学习 | 持续学习 | [Anti-Degradation Lifelong Multi-View Clustering](cards.md#paper-almc-nullspace-retained-view-updates) | 持续新增视图时，可把更新限制在旧表征的零空间，再与同模型不投影的版本比较聚类稳定性。见表 3。 |
| 机器学习 | 图学习 | [FedSDR: Federated Graph Learning with Structural Noise Detection and Reconstruction](cards.md#paper-fedsdr-spectral-fidelity-client-aggregation) | 联邦图协作时可单独比较结构质量加权聚合和本地拓扑重建，分清全局与客户端收益。见表 2。 |
| 计算机视觉 | 推理加速 | [SpeeDe3DGS: Speedy Deformable 3D Gaussian Splatting with Temporal Pruning and Motion Grouping](cards.md#paper-speede3dgs) | 动态场景可先按跨时间贡献裁剪，再把多点的形变蒸馏为共享刚体运动。 |
| 多模态学习 | 模型架构 | [Semantic Context Matters: Improving Conditioning for Autoregressive Models](cards.md#paper-scar-semantic-context) | 自回归视觉编辑可同时压缩语义前缀，并使解码隐藏状态对齐目标语义。 |
| 多模态学习 | 模型架构 | [SRA-Det: Learning Omni-Grained Open-Vocabulary Detection Beyond Category Names](cards.md#paper-sra-det) | 组合检索或检测含多个必要属性时，评估可微合取，防止一项高分掩盖缺少的约束。 |
| 计算机视觉 | 表示学习 | [ReScene4D: Temporally Consistent Semantic Instance Segmentation of Evolving Indoor 3D Scenes](cards.md#paper-rescene4d) | 低频观测的对象跟踪可把跨次扫描的关联融入分割训练，并用带身份约束的指标检验。 |
| 计算机视觉 | 推理加速 | [LiteVGGT: Boosting Vanilla VGGT via Geometry-aware Cached Token Merging](cards.md#paper-lite-vggt) | 长多视图网络先测相邻层合并决策是否稳定，再缓存索引，避免重复匹配。 |
| 机器学习基础与统计 | 鲁棒性 | [Lipschitz Optimization for Formal Verification of Homographies](cards.md#paper-homography-verification) | 对近似平面视觉任务，把相机位姿扰动直接编码进形式验证范围。 |
| 机器人学 | 强化学习 | [PlannerRFT: Reinforcing Diffusion Planners through Closed-Loop and Sample-Efficient Fine-Tuning](cards.md#paper-planner-rft) | 闭环奖励稀疏时，训练阶段专门控制去噪探索分布并保留部署路径。 |
| 机器学习基础 | 可解释性与诊断 | [Improving Sparse Autoencoder with Dynamic Attention](cards.md#paper-dynamic-attention-sae) | 训练稀疏自编码器时，用 sparsemax 求输入依赖的激活数量，比较固定 TopK。 |
| 多模态学习 | 推理优化 | [SwitchCraft: Training-Free Multi-Event Video Generation with Attention Controls](cards.md#paper-switchcraft-event-aligned-steering) | 多事件视频按帧段注入各自事件条件，并动态控制强度以维持时间连贯。 |
| 多模态学习 | 微调与适配 | [HiFICL: High-Fidelity In-Context Learning for Multimodal Tasks](cards.md#paper-hificl-virtual-kv) | 近似多模态示例学习时，拟合虚拟键值以保留依查询而变的注意力分量。 |
| 多模态学习 | 评测与分析 | [Hear you are: Teaching LLMs Spatial Reasoning with Vision and Spatial Sound](cards.md#paper-binaural-spatial-reasoning) | 验证视听空间推理时设置语义不匹配但位置吻合的样本，并比较双耳和单声道。 |
| 机器学习基础 | 微调与适配 | [Energy Waveify and Redistribution for Test-Time Adaptation: A Control System Perspective](cards.md#paper-energy-wave-test-time-adaptation) | 能量式测试时适配可检验确定性概率流更新能否减少逐样本随机采样。 |
| 多模态学习 | 自监督学习 | [OlmoEarth: Stable Latent Image Modeling for Multimodal Earth Observation](cards.md#paper-olmoearth-modality-masked-latent-modeling) | 多传感器预训练可优先实测整模态遮盖，并区分潜空间预测方案本身是否存在训练坍塌。见表 4。 |
| 多模态学习 | 评估与诊断 | [InfiniBench: Infinite Benchmarking for Visual Spatial Reasoning with Customizable Scene Complexity](cards.md#paper-infinibench-irrelevant-object-spatial-stress-test) | 空间推理测试可固定目标关系，只分别改变无关物体数，避免总体分数掩盖对时空跟踪的特定影响。见表 5。 |
| 机器人学 | 生成建模 | [DICArt: Advancing Category-level Articulated Object Pose Estimation in Discrete State-Spaces](cards.md#paper-dicart-discrete-kinematic-pose-diffusion) | 估计具有运动学约束的姿态时，可对照离散扩散与连续扩散，并用部件间层次关系减少独立搜索。见表 2。 |
| 机器人学 | 数据增强 | [AffordGen: Generating Diverse Demonstrations for Generalizable Object Manipulation with Affordance Correspondence](cards.md#paper-affordgen-geometry-demonstration-budget) | 示教增强时可固定总轨迹数，分别试验多对象网格与每对象多轨迹如何分配预算。见表 1。 |
| 多模态学习 | 检索增强 | [Beyond Semantic Search: Towards Referential Anchoring in Composed Image Retrieval](cards.md#paper-oacir-instance-anchor-retrieval) | 当检索必须找回同一实例，可在查询中提供显式局部锚点，并对相似实例干扰单列身份召回。见表 3。 |
| 计算机视觉 | 模型效率 | [UPLiFT: Efficient Pixel-Dense Feature Upsampling with Local Attenders](cards.md#paper-uplift-local-attender-iterative-feature-upsampling) | 稠密下游任务可比较逐级局部上采样和大规模跨注意力，联合看时延、分割精度与深度误差。见表 1。 |
| 多模态学习 | 模型架构 | [Rethinking MLLM Itself as a Segmenter with a Single Segmentation Token](cards.md#paper-self1e) | 想去掉外部分割头时，保留未压缩视觉网格，并把语言侧语义作为残差补回。 |
| 机器学习基础与统计 | 损失函数 | [Temporal Imbalance of Positive and Negative Supervision in Class-Incremental Learning](cards.md#paper-temporal-adjusted-loss) | 类别分期到达时，统计旧类被当负样本的累计监督，再决定是否重加权交叉熵。 |
| 计算机视觉 | 推理与规划 | [Global-Aware Edge Prioritization for Pose Graph Initialization](cards.md#paper-global-edge-prior) | 昂贵几何验证前按全图约束排序候选边，优先补弱连通区域而非仅做节点最近邻。 |
| 多模态学习 | 推理策略 | [AdaptVision: Efficient Vision-Language Models via Adaptive Visual Acquisition](cards.md#paper-adaptvision) | 按问题主动获取视觉细节，把何时裁剪与答题质量的优化信号分开。 |
| 机器学习基础与统计 | 持续学习 | [Geometry-driven OOD Detectors Are Class-Incremental Learners](cards.md#paper-geometry-driven-ood-heads) | 增量分类可将任务头同时训练成域内分类器与域外拒绝器，并联合考察类间分离和类内紧致。 |
| 计算机视觉 | 训练策略 | [ReAlign: Generalizable Image Forgery Detection via Reasoning-Aligned Representation](cards.md#paper-realign-forgery-detection) | 只在训练使用教师提供语义异常解释，用对比蒸馏比较解释、描述和类别标签的贡献。 |
| 计算机视觉 | 推理优化 | [Saliency-Driven Token Merging for Vision Transformers](cards.md#paper-sad-tm-saliency-merging) | 免训练裁并视觉词元时，将输入显著性异常作为补充，并推迟早层的合并。 |
| 计算机视觉 | 推理优化 | [FastGS: Training 3D Gaussian Splatting in 100 Seconds](cards.md#paper-fastgs-multiview-consistency) | 三维高斯训练时使用多视图一致性定新增和剪枝优先级，而非先锁定统一数量预算。 |
| 多模态学习 | 知识蒸馏 | [Learning from Itself: Mining Internal Knowledge from Vision Language Models for Continual Learning](cards.md#paper-learning-from-itself-clip-continual) | 持续适配图文模型时，根据当前强弱动态调整视觉分类支路与文本支路之间的蒸馏方向。 |
| 多模态学习 | 强化学习 | [Reinforcing Video Object Segmentation to Think before it Segments](cards.md#paper-veason-r1-sequential-segmentation) | 视频分割需要多步推理时，把关键帧选择、框定位和传播一致性变成分别可核查的奖励。 |
| 机器人学 | 规划与决策 | [Edit-As-Act: Goal-Regressive Planning for Open-Vocabulary 3D Indoor Scene Editing](cards.md#paper-edit-as-act-goal-regressive) | 编辑三维环境时先写目标状态，再反向规划最少可验操作，保留未涉及对象。 |
| 计算机视觉 | 自监督学习 | [Scene-Centric Unsupervised Video Panoptic Segmentation](cards.md#paper-videocups-video-droploss) | 时序全景伪标签噪声大时，在训练损失侧排除不可靠监督，并单独评估关联和语义。 |
| 计算机视觉 | 三维重建与几何建模 | [B$^3$-Seg: Camera-Free, Training-Free 3DGS Segmentation via Analytic EIG and Beta-Bernoulli Bayesian Updates](cards.md#paper-b3seg-information-gain-view-selection) | 需要主动挑选有限视角时，可按可见点的预期后验信息增益选下一视角，与固定或重建视角采样对照。见表 1 和第 5.4 节。 |
| 机器学习 | 时序建模 | [Towards Uncertainty-aware Unsupervised Domain Adaptation for Videos and Time-Series with Causal Optimal Transport](cards.md#paper-causal-ot-cross-channel-alignment) | 跨域时序适配除了匹配特征边缘分布，也可约束通道依赖在迁移前后保持，比较不同传输求解方式。见表 4。 |
| 计算机视觉 | 数据增强 | [What Makes Good Synthetic Training Data for Zero-Shot Stereo Matching?](cards.md#paper-synthetic-stereo-camera-baseline-distribution) | 渲染训练数据时固定样本规模，依据目标场景分布选择相机基线范围，并分别报告各目标域误差。见表 1。 |
| 生成模型 | 损失与奖励 | [Improving Text-to-Image Generation with Intrinsic Self-Confidence Rewards](cards.md#paper-solace-denoising-self-confidence-reward) | 缺少可靠偏好模型时，可以把生成结果重新加噪后的恢复误差当作内在奖励，并与外部指标分开验证。见表 1、2。 |
| 计算机视觉 | 检索增强 | [Retrieve-to-Restore: Efficient All-in-One Image Restoration with a Retrieval-Based Degradation Bank](cards.md#paper-r2r-retrieved-degradation-prior-bank) | 多个退化任务共用骨干时，可把退化先验移到外部字典，通过检索做条件调整，再核对容量和失真干扰。见表 5、6。 |
| 机器人学 | 生成建模 | [GenieDrive: Towards Physics-Aware Driving World Model with 4D Occupancy Guided Video Generation](cards.md#paper-geniedrive-normalized-multiview-occupancy-conditioning) | 世界模型可用可编辑的占据中间表示约束多视角合成，并消融归一化以检查跨视角注意力稳定性。见表 5。 |
| 多模态学习 | 推理与规划 | [Human-like Abstract Visual Reasoning via Understanding and Solving Reasoning Loop](cards.md#paper-usrl) | 少样本规则推断可交替更新规则假设与暂定解，并对仅求解的模型做对照。 |
| 多模态学习 | 生成模型 | [MotionHiFlow: Text-to-Motion via Hierarchical Flow Matching](cards.md#paper-motionhiflow) | 分层生成动作时，把跨尺度噪声连续性当作设计变量。 |
| 多模态学习 | 检索增强生成 | [MR-RAG: Multimodal Relevance-Aware Retrieval-Augmented Generation for Medical Visual Question Answering](cards.md#paper-mr-rag) | 分别校准检索相关性与生成阶段对每份证据的依赖，避免弱证据均匀注入。 |
| 多模态学习 | 训练策略 | [OctoMed: Data Recipes for State-of-the-Art Multimodal Medical Reasoning](cards.md#paper-octomed-reasoning-length) | 微调时可混合不同长度的结构化轨迹，并按任务分别审计直接输出与推理模式。 |
| 计算机视觉 | 训练策略 | [Let it Snow! Animating 3D Gaussian Scenes with Dynamic Weather Effects via Physics-Guided Score Distillation](cards.md#paper-physics-guided-sds) | 编辑动态3D场景时可让物理模拟给运动先验，同时允许视觉蒸馏更新外观和运动。 |
| 计算机视觉 | 自监督学习 | [Flow3r: Factored Flow Prediction for Scalable Visual Geometry Learning](cards.md#paper-flow3r-factored-flow) | 用无标签视频学习几何时，将对应流的预测分解为一侧几何与另一侧位姿。 |
| 科学与医学 AI | 表示学习 | [Spatial-SAM: Spatially Consistent 3D Electron Microscopy Segmentation with SDF Memory and Semi-Supervised Learning](cards.md#paper-spatial-sam-sdf-memory) | 逐切片分割要保持三维连贯时，用显式距离场替代通用传播记忆。 |
| 计算机视觉 | 条件生成 | [Face2Scene: Using Facial Degradation as an Oracle for Diffusion-Based Scene Restoration](cards.md#paper-face2scene-degradation-oracle) | 若局部目标有可靠复原参照，从该局部估计退化后条件化整图恢复。 |
| 计算机视觉 | 损失函数与优化 | [WaTeRFlow: Watermark Temporal Robustness via Flow Consistency](cards.md#paper-waterflow-temporal-watermark) | 需要从图生视频保留来源证据时，将水印恢复视作沿运动对应的跨帧稳定问题。 |
| 多模态学习 | 推理优化 | [LoL: Longer than Longer, Scaling Video Generation to Hour](cards.md#paper-long-video-sink-collapse) | 自回归视频出现周期回跳时，先诊断多头位置编码是否共同锁到同一注意力锚点。 |
| 多模态学习 | 评测与分析 | [Bias at the End of the Score](cards.md#paper-reward-model-demographic-audit) | 选择文生图奖励模型时，按群体检查打分及优化后生成分布，避免总体质量掩盖偏差。 |
| 生成模型 | 模型效率 | [Markovian Scale Prediction: A New Era of Visual Autoregressive Generation](cards.md#paper-markov-var-sliding-scale-history) | 逐尺度生成时可以只保留临近尺度的压缩历史，比较全量、局部或无历史对画质和显存的影响。见表 3、4。 |
| 机器人学 | 规划与控制 | [Ground Reaction Inertial Poser: Physics-based Human Motion Capture from Sparse IMUs and Insole Pressure Sensors](cards.md#paper-grip-foot-contact-versus-inertial-sensors) | 可穿戴动作捕捉应比较增加接触模态与再加同类惯性测量哪种更能改善物理稳定性。见表 3。 |
| 计算机视觉 | 训练策略 | [See Through the Noise: Improving Domain Generalization in Gaze Estimation](cards.md#paper-seetn-continuous-label-affinity-denoising) | 连续回归标签有噪声时，可用标签近邻与特征近邻的相容性筛样，避免把连续目标硬当成纠错类别。见表 4。 |
| 机器人学 | 三维重建与几何建模 | [Monocular Open Vocabulary Occupancy Prediction for Indoor Scenes](cards.md#paper-poisson-gaussian-to-occupancy-weak-supervision) | 只有占据几何标签时，可比较高斯到体素的聚合概率模型和语义温度调度，避免弱监督训练坍塌。见表 2、3。 |
| 智能体 | 检索增强 | [EvoGraph-R1: Self-Evolving Multimodal Knowledge Hypergraphs for Agentic Retrieval](cards.md#paper-evograph-online-multimodal-graph-refinement) | 多跳回答遇到新证据时，可让检索策略在当前问答中更新图结构，并检查各更新操作对答案和检索轮数的影响。见表 3。 |
| 计算机视觉 | 模型效率 | [Edge-RecViT: Efficient Vision Transformer via Semantic-Refined Dynamic Recursion](cards.md#paper-edge-recvit-boundary-aware-token-depth) | 视觉标记早退时可以给含结构信息的边缘标记更深预算，并对照固定深度的精度与 FLOPs。见表 3。 |
| 智能体 | 评测与诊断 | [RAAS: LLM Agentic System Architecture Search with GRPO](cards.md#paper-raas-agent-architecture) | 搜索工作流时，对同一问题比较候选架构，并在多个独立运行中汇总。 |
| 机器人学 | 推理与规划 | [Beyond Success: Refining Elegant Robot Manipulation from Mixed-Quality Data via Just-in-Time Intervention](cards.md#paper-jiti-elegant-execution) | 成功率相近时，可独立评估执行约束，仅在关键动作由置信度门控触发修正。 |
| 多模态学习 | 强化学习 | [Select Less, Reason More: Prioritizing Evidence Purity for Video Reasoning](cards.md#paper-earl-video-evidence) | 视频取证应允许在已选时间附近重新高频采样，并奖励证据定位而不只答对。 |
| 多模态学习 | 模型架构 | [MultiShotMaster: A Controllable Multi-Shot Video Generation Framework](cards.md#paper-multishot-narrative-rope) | 有分段结构的序列可用显式位置相位标识段边界，同时维持段内时空参考。 |
| 多模态学习 | 生成模型 | [Cubic Discrete Diffusion: Discrete Visual Generation on High-Dimensional Representation Tokens](cards.md#paper-cubic-discrete-diffusion) | 高维理解特征用于离散生成时，可按位置和特征坐标共同遮罩，使生成轮数不随维数线性增加。 |
| 智能体 | 自动化工作流 | [NERFIFY: A Multi-Agent Framework for Turning NeRF Papers into Code](cards.md#paper-nerfify) | 论文到代码应先将目标框架的模块契约形式化，然后按依赖顺序生成并验证各节点。 |
| 多模态学习 | 模型架构 | [Gated Condition Injection without Multimodal Attention: Towards Controllable Linear-Attention Transformers](cards.md#paper-gated-condition-linear-attention) | 在线性注意力骨干上做异构条件控制时，比较独立条件支路加门控与传统条件注入。 |
| 计算机视觉 | 模型架构 | [Unleashing the Power of Chain-of-Prediction for Monocular 3D Object Detection](cards.md#paper-monocop-uncertainty-routing) | 多属性预测中，低不确定时利用属性链，高不确定样本切换并行以阻断传播误差。 |
| 计算机视觉 | 表示学习 | [Any4D: Unified Feed-Forward Metric 4D Reconstruction](cards.md#paper-any4d-modular-coordinate-factors) | 多传感器动态几何建模中，按局部相机系和全局世界系因子化预测。 |
| 计算机视觉 | 知识蒸馏 | [Progressive Mask Distillation for Self-supervised Video Representation](cards.md#paper-progressive-mask-distillation) | 掩码视频预训练时，让低遮盖阶段的学生教高遮盖阶段，避免大遮盖初期无法学习。 |
| 多模态学习 | 训练与数据策略 | [GThinker: Towards General Multimodal Reasoning via Cue-Guided Rethinking](cards.md#paper-gthinker-cue-rethinking) | 多模态模型推理初始观察可能错误时，引入证据冲突触发的视觉重新检查。 |
| 机器人学 | 规划与决策 | [Physically Ground Commonsense Knowledge for Articulated Object Manipulation with Analytic Concepts](cards.md#paper-analytic-concepts-articulation) | 把语言常识作为对象功能假设，再用可计算几何与物理概念约束操作。 |
| 机器学习 | 数据蒸馏 | [OS-Fed: One Snapshot Is All You Need](cards.md#paper-osfed-compact-learned-update-snapshot) | 联邦通信受限时，可比较把更新编码成少量可学习样本与发送稀疏梯度，并同时计入编码、解码和精度。见表 4。 |
| 计算机视觉 | 训练策略 | [BackSplit: The Importance of Sub-dividing the Background in Biomedical Lesion Segmentation](cards.md#paper-backsplit-fine-grained-background-supervision) | 稀疏目标分割可在训练时细分异质背景，仅在输出时合并，验证辅助标签加到现有分割器是否有效。见表 1。 |
| 生成模型 | 模型效率 | [FlashDecoder: Real-Time Latent-to-Pixel Streaming Decoder with Transformers](cards.md#paper-flashdecoder-rolling-kv-streaming-video-decode) | 流式视频解码可对照固定长度的滚动 KV 窗口，按窗口大小测画质、峰值显存和帧率。见表 3、4。 |
| 机器人学 | 表征学习 | [DiffuView: Multi-View Diffusion Pretraining for 3D Aware Robotic Manipulation](cards.md#paper-diffuview-camera-conditioned-diffusion-features) | 视觉操控可从相机条件多视角扩散取特征，再分别检查机器人数据和相机编码对新视角的贡献。见表 5。 |
| 生成模型 | 模型蒸馏 | [FlowSteer: Guiding Few-Step Image Synthesis with Authentic Trajectories](cards.md#paper-flowsteer-online-teacher-trajectory-alignment) | 少步流模型蒸馏可检验在线对齐真实教师轨迹，以减少分段重流与推理时轨迹的分布差。见表 3。 |
| 机器人学 | 时序建模 | [SyncMos: Scalable Motion Synchronisation for Multi-Agent Scene Interaction](cards.md#paper-syncmos-dependency-conditioned-time-warp) | 用单个动作模型生成多角色交互时，可以先显式列出事件依赖，再根据同步目标做时间变形，单测偏移范围。见表 2、3。 |
| 机器学习 | 模型蒸馏 | [Cross-Architecture Adaptation: Cloud-Edge Continual Test-Time Adaptation with Dynamic Sampling and Heterogeneous Distillation](cards.md#paper-cloud-edge-cross-architecture-distillation) | 边缘模型遇到持续分布漂移时，可选择只上传有价值的样本，由更强异构云模型提供蒸馏信号，再逐项测适配收益和传输。见表 1–3。 |
| 多模态学习 | 训练策略 | [UZ3DVG: Unaided Zero-Shot 3D Visual Grounding with Generated Language Conditions](cards.md#paper-uz3dvg) | 把跨模态教师移到离线数据生成，部署只留点云和指令，单测外部依赖与定位准确率。 |
| 计算机视觉 | 训练策略 | [Learning from Noisy Supervision: A Denoising-Debiasing Framework for Weakly Supervised Video Anomaly Detection](cards.md#paper-d2mil) | 在弱监督多实例训练中，把大损失样本暂缓训练并用独立教师复核，保留难正例。 |
| 计算机视觉 | 训练策略 | [CoLoR: The Devil is in Scene Coordinate Regression for Large-Scale Visual Localization](cards.md#paper-color-scene-coordinate-regression) | 按观察冗余分开训练可靠多视点与弱单视点，再统一局部和全局检索特征。 |
| 计算机视觉 | 模型分析 | [Revisiting Pose Sensitivity in Splat-based Computed Tomography under Sparse-view Reconstruction](cards.md#paper-splat-ct-pose-sensitivity) | 稀疏视角重建遇到条纹时，应先把姿态误差和视图数量作为独立因素诊断。 |
| 机器人学 | 数据增强 | [Real2Edit2Real: Generating Robotic Demonstrations via a 3D Control Interface](cards.md#paper-real2edit2real) | 扩增操作演示时，可先在度量3D空间编辑轨迹和姿态，再用校准深度作视频生成主约束。 |
| 机器人学 | 条件生成 | [U4D: Uncertainty-Aware 4D World Modeling from LiDAR Sequences](cards.md#paper-u4d-uncertainty-first) | 生成时序三维场景时，先从高不确定区域构建结构锚点，再用其条件化剩余区域。 |
| 计算机视觉 | 表示学习 | [Disentangle-then-Align: Non-Iterative Hybrid Multimodal Image Registration via Cross-Scale Feature Disentanglement](cards.md#paper-hrnet-hybrid-multimodal-registration) | 同时存在大尺度错位和局部形变时，先对齐去模态差异的特征，再联合预测两类变换。 |
| 多模态学习 | 训练与数据策略 | [IntroSVG: Learning from Rendering Feedback for Text-to-SVG Generation via an Introspective Generator-Critic Framework](cards.md#paper-introsvg-render-feedback) | 生成可执行视觉程序时，用渲染反馈构造自我修正数据并训练同一模型扮演生成器与评审。 |
| 多模态学习 | 迁移与泛化 | [Progressive Cross-Modal Causal Intervention for Long-Term Action Recognition](cards.md#paper-pcmci-action-confounders) | 长视频动作识别要减轻场景共现捷径时，先校正动作文本关系，再作为视觉去混淆的中介。 |
| 多模态学习 | 强化学习 | [Learning What to Trust: Bayesian Prior-Guided Optimization for Visual Generation](cards.md#paper-bpgo-reward-trust) | 组相对策略优化可分别估计组间奖励可信度与组内样本区分度。 |
| 计算机视觉 | 推理优化 | [BinaryAttention: One-Bit QK-Attention for Vision and Diffusion Transformers](cards.md#paper-binaryattention-one-bit-qk) | 若硬件支持位运算，可只二值化查询键相似度，再用学习补偿和自蒸馏恢复质量。 |
| 生成模型 | 推理策略 | [FlowPortal: Residual-Corrected Flow for Training-Free Video Relighting and Background Replacement](cards.md#paper-flowportal-source-residual-video-editing) | 在无训练流编辑中，可以用同条件重建误差校正编辑流，并检查保真与指令匹配的取舍。见图 2、表 3。 |
| 生成模型 | 表征学习 | [STCDiT: Spatio-Temporally Consistent Diffusion Transformer for High-Quality Video Super-Resolution](cards.md#paper-stcdit-first-latent-anchor-guidance) | 视频潜变量存在时间压缩不均时，可比较优先取未压缩锚帧和均匀取帧对低清视频恢复的影响。见表 3。 |
| 机器学习 | 模型融合 | [BD-Merging: Bias-Aware Dynamic Model Merging with Evidence-Guided Contrastive Learning](cards.md#paper-bdmerging-evidence-routed-model-merging) | 合并专家模型时可用统一标签空间中的不确定性决定路由，并把干净、偏移和未知任务分开评估。见表 3。 |
| 机器人学 | 损失与奖励 | [PromptDepth: Efficient and Promptable Geometric 3D Vision Model for Embodied Intelligence](cards.md#paper-promptdepth-joint-dense-prediction-alignment) | 一个骨干共学深度和交互分割时，可测两任务表示的二阶结构对齐能否缓解负迁移。见表 4。 |
| 生成模型 | 模型效率 | [One Model, Many Budgets: Elastic Latent Interfaces for Diffusion Transformers](cards.md#paper-elit-tail-drop-budgeted-latent-interface) | 给 DiT 提供多档推理预算时，可训练固定顺序的潜变量并随机截断尾部，比较删到同样比例时的质量。见表 4。 |
| 多模态学习 | 生成建模 | [OmniSonic: Towards Universal and Holistic Audio Generation from Video and Text](cards.md#paper-omnisonic-audio-source-gated-conditioning) | 联合生成说话、镜头内和镜头外声音时，可按来源分别建条件并用门控融合，检查环境对齐和语音字错率。见表 3。 |
| 多模态学习 | 推理策略 | [Residual Decoding: Mitigating Hallucinations in Large Vision-Language Models via History-Aware Residual Guidance](cards.md#paper-residual-decoding) | 视觉生成答复被语言先验带偏时，对照历史 logits 残差和常规解码，再检查幻觉与任务性能。 |
| 计算机视觉 | 表示学习 | [A2GC: Asymmetric Aggregation with Geometric Constraints for Locally Aggregated Descriptors](cards.md#paper-a2gc-vpr) | 源特征和目标原型分布差异大时，比较非对称聚合和标准双边 Sinkhorn。 |
| 多模态学习 | 测试时适应与推理 | [Decoupling Stability and Plasticity for Multi-Modal Test-Time Adaptation](cards.md#paper-dasp-multimodal-tta) | 多模态漂移时先诊断哪个模态偏移，再决定哪组适配参数更新。 |
| 机器人学 | 推理与规划 | [ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation](cards.md#paper-activevla) | 三维操作中先定位动作关键区域，再按目标需要选择可用视角与分辨率。 |
| 机器人学 | 训练策略 | [MaskAdapt: Learning Flexible Motion Adaptation via Mask-Invariant Prior for Physics-Based Characters](cards.md#paper-maskadapt) | 需要局部改动作而保全身技能时，先训练不随局部缺失显著改变的基础策略，再学被掩码部件的残差。 |
| 多模态学习 | 强化学习 | [MedLoc-R1: Performance-Aware Curriculum Reward Scheduling for GRPO-Based Medical Visual Grounding](cards.md#paper-medloc-r1) | 稀疏奖励下按模型近期表现收紧定位门槛，并与固定步数调度对照。 |
| 多模态学习 | 强化学习 | [REVISOR: Beyond Textual Reflection, Towards Multimodal Introspective Reasoning in Long-Form Video Understanding](cards.md#paper-revisor-dual-attribution) | 长视频复查时分别奖励选对需重看片段与根据片段修正答案，避免只强化文本自检。 |
| 机器学习基础 | 可解释性与诊断 | [Hierarchical Concept Embedding & Pursuit for Interpretable Image Classification](cards.md#paper-hcep-hierarchical-concepts) | 用概念向量解释分类时，如果概念有层级，应在表示与稀疏解码同时保证父子一致。 |
| 多模态学习 | 推理优化 | [One Layer's Trash is Another Layer's Treasure: Adaptive Layer-wise Visual Token Selection in LVLMs](cards.md#paper-alvts-layer-wise-token-routing) | 按层压缩视觉计算时让未选 token 跳过本层并保留给后层重新选择。 |
| 机器学习基础 | 可解释性与诊断 | [Bias In, Bias Out? Finding Unbiased Subnetworks in Vanilla Models](cards.md#paper-bise-bias-invariant-subnetworks) | 训练后去捷径可先比较从冻结模型抽取的稀疏子网与重新训练，而非假设整网均依赖偏置。 |
| 多模态学习 | 损失函数与优化 | [ConceptPrism: Concept Disentanglement in Personalized Diffusion Models via Residual Token Optimization](cards.md#paper-conceptprism-residual-tokens) | 少量参考图个性化时，给共享概念及每个实例分别分配 token，并阻止实例 token 吞掉共享属性。 |
| 机器学习 | 训练策略 | [Revisiting Learning with Noisy Labels: Active Forgetting and Noise Suppression](cards.md#paper-fine-active-forgetting-noisy-supervision) | 对已被模型拟合的错标样本，可比较主动清除已学噪声与仅抑制后续学习，再用不同噪声类型验证。见表 3。 |
| 多模态学习 | 偏好优化 | [FINER: MLLMs Hallucinate under Fine-grained Negative Queries](cards.md#paper-finer-paired-fine-grained-visual-negatives) | 视觉幻觉训练可用同时包含真细节和局部错误的正负问题对，并比较 DPO 与只给正确答案的监督微调。见表 4。 |
| 计算机视觉 | 三维重建与几何建模 | [MoRel: Long-Range Flicker-Free 4D Motion Modeling via Anchor Relay-based Bidirectioanl Blending with Hierarchical Densification](cards.md#paper-morel-bidirectional-keyframe-anchor-relay) | 建模长期动态场景时可转发多个局部基准，并双向融合段间形变，比较一次全局建模和独立分段。见表 2。 |
| 生成模型 | 模型效率 | [Multi-Scale Local Speculative Decoding for Image Generation](cards.md#paper-mulo-sd-spatial-local-draft-verification) | 图像自回归加速可用低分辨率草稿，并把拒绝后的重采样局限在空间邻域，与按序全量重试比较。见表 1。 |
| 机器学习 | 隐私保护 | [Fully Decentralized Certified Unlearning](cards.md#paper-decentralized-certified-unlearning-client-views) | 无中心协调的数据删除可采用客户端消息视图定义认证边界，并比较通用差分隐私与专门事后遗忘的可承受规模。见定理 3.5 与表 2。 |
| 多模态学习 | 表征学习 | [CoV-Align: Efficient Fine-grained Cross-Modal Alignment with Cohesive Visual Semantics Priority](cards.md#paper-cov-align-query-independent-visual-grouping) | 大量图文匹配前可先独立压缩视觉块为语义区域，比较区域数对双向检索的作用。见表 3、4。 |
| 多模态学习 | 时序建模 | [Question-guided Visual Compression with Memory Feedback for Long-Term Video Understanding](cards.md#paper-qvic-memory-feedback-visual-compression) | 长视频的记忆可以在压缩之前反向引导视觉注意，而非只供解码读取；应在固定采样率上比较效果。见表 3。 |
| 计算机视觉 | 异常检测 | [A Difference-in-Difference Approach to Detecting AI-Generated Images](cards.md#paper-did-generated-image-detection) | 当重建误差的样本间方差掩盖来源差别时，用二阶差分抵消共同误差。 |
| 计算机视觉 | 模型架构 | [CompetitorFormer: Mitigating Query Conflicts for 3D Instance Segmentation via Competitive Strategy](cards.md#paper-competitorformer) | 并行查询争抢同一实例时，可在每层解码前建查询间竞争，而非只在输出去重。 |
| 智能体 | 自动化工作流 | [LensWalk: Agentic Video Understanding by Planning How You See in Videos](cards.md#paper-lenswalk) | 视频代理应控制取证的时间范围和密度，并保留可核验的异时证据。 |
| 计算机视觉 | 表示学习 | [Hilbert Curve-Based Attention Enabling Topology-Preserving Image Tensor Representation for Semantic Segmentation Network](cards.md#paper-tpsegformer) | 将二维网格展平进入序列模块前，对照局部性更强的 Hilbert 排序与普通逐行排序。 |
| 多模态学习 | 评测与诊断 | [Ego-Grounding for Personalized Question-Answering in Egocentric Videos](cards.md#paper-myego-evidence-audit) | 第一视角记忆问答可用已知答案时刻作对照，区分证据检索失败与对证据的推理失败。 |
| 计算机视觉 | 表示学习 | [Gaussian Mapping for Evolving Scenes](cards.md#paper-game-evolving-scenes) | 维护长期3D记忆时，按局部变化淘汰过时观测并保留仍有效的关键帧。 |
| 计算机视觉 | 损失函数 | [MERIT: Multi-domain Efficient RAW Image Translation](cards.md#paper-merit-raw-translation) | 跨传感器统一映射时，可将信号依赖噪声匹配单独作为目标，并按方向验收。 |
| 机器学习基础 | 知识蒸馏 | [Memory-Efficient Transfer Learning with Fading Side Networks via Masked Dual Path Distillation](cards.md#paper-masked-dual-path-distillation) | 用轻量旁路节省微调显存时，可在训练阶段做双路蒸馏，部署时移除旁路。 |
| 机器人学 | 自监督学习 | [LAOF: Robust Latent Action Learning with Optical Flow Constraints](cards.md#paper-laof-latent-action-flow) | 从无动作标签视频学潜动作时，用智能体相关光流隔离任务无关运动。 |
| 多模态学习 | 评测与分析 | [X-AVDT: Audio-Visual Cross-Attention for Robust Deepfake Detection](cards.md#paper-x-avdt-cross-modal-forensics) | 评估合成视频检测时，应把音画一致性信号与视觉残差一起做跨生成器验证。 |
| 多模态学习 | 推理优化 | [SURF: Signature-Retained Fast Video Generation](cards.md#paper-surf-noise-reshifting) | 预览生成先按模型原分辨率完成早期去噪，之后降分辨率再用映射细化。 |
| 智能体 | 规划与决策 | [See, Think, Act: Teaching Multimodal Agents to Effectively Interact with GUI by Identifying Toggles](cards.md#paper-star-gui-state-aware) | 执行二元界面目标前先读当前状态；若已符合目标，输出不操作。 |
| 多模态学习 | 少样本学习 | [Meta-Learning In-Context Enables Training-Free Cross Subject Brain Decoding](cards.md#paper-braincodec-contextual-sensor-encoding-inversion) | 传感维度跨个体变化时，可先按维度从少量配对示例估计个体编码，再从新观测逆推，而无需对齐坐标或更新权重。见表 1。 |
| 机器学习 | 训练策略 | [CLEX: Complementary Label Exchange Learning for Noisy Facial Expression Recognition](cards.md#paper-clex-non-target-logit-consistency) | 带噪标签分类可以增加增强视图间的非目标类别约束，区分 logit 交换、归一化与完整损失的作用。见表 3。 |
| 表征学习 | 评估与诊断 | [Reevaluating the Intra-Modal Misalignment Hypothesis in CLIP](cards.md#paper-clip-intramodal-misalignment-task-axis-control) | 图像检索变差时先测试嵌入评测的语义轴是否与任务匹配，并用图像内对比模型做对照，再决定是否改训练损失。见表 3。 |
| 计算机视觉 | 鲁棒性与安全 | [Rel-Zero: Harnessing Patch-Pair Invariance for Robust Zero-Watermarking Against AI Editing](cards.md#paper-relzero-patch-relations-defensive-authentication) | 图像来源验证可比较局部特征关系与整图表示，按固定误报率报告编辑后检测效果。见表 1、2。 |
| 计算机视觉 | 三维重建与几何建模 | [Joint Spectral Image Reconstruction and Semantic Segmentation with Cooperative Unfolding](cards.md#paper-cooperative-unrolling-task-feature-exchange) | 测量重建与语义任务强相关时，可比较平行交互更新和单向先重建后识别，按质量和语义指标共同评估。见表 2。 |
| 机器学习 | 持续学习 | [Representation-Steered Incremental Adapter-Tuning for Class-Incremental Learning with Pre-Trained Models](cards.md#paper-rsiat-fixed-shared-incremental-adapter) | 类增量学习可以保持一个共享适配器，通过对齐新旧表示控制遗忘，比较残差对齐和不对齐的差异。见表 3。 |
| 多模态学习 | 模型架构 | [SeD-UD: An Influence-Driven and Hierarchically-Decoupled Information Bottleneck for Multimodal Intent Recognition](cards.md#paper-sed-ud) | 把跨模态重复与各模态噪声分开压缩，并按输入决定瓶颈维度。 |
| 多模态学习 | 评测与诊断 | [When Visualizing is the First Step to Reasoning: MIRA, a Benchmark for Visual Chain-of-Thought](cards.md#paper-mira-visual-cot) | 评估生成式视觉草图时，另给人工中间图作上界，以区分草图生成和后续推断。 |
| 计算机视觉 | 损失函数 | [Spectral Scalpel: Amplifying Adjacent Action Discrepancy via Frequency-Selective Filtering for Skeleton-Based Action Segmentation](cards.md#paper-spectral-scalpel) | 相邻动作边界不清时，专门压低相邻动作共享频谱，而非统一增强高频。 |
| 多模态学习 | 生成模型 | [DuetSVG: Unified Multimodal SVG Generation with Internal Visual Guidance](cards.md#paper-duetsvg) | 需要输出结构化程序时，可让同一模型生成视觉参考并在测试时指导结构解码。 |
| 计算机视觉 | 推理压缩 | [FACE: A Face-based Autoregressive Representation for High-Fidelity and Efficient Mesh Generation](cards.md#paper-face-mesh-token) | 结构序列按基本部件而不是每个标量分词，同时用解码结果验证压缩是否造成质量损失。 |
| 机器学习基础与统计 | 参数高效微调 | [FAAR: Efficient Frequency-Aware Multi-Task Fine-Tuning via Automatic Rank Selection](cards.md#paper-faar-rank-shrinking) | 多任务适配先为各任务及层保留选择空间，再按绩效缩减秩。 |
| 多模态学习 | 推理与规划 | [GeoWorld: Geometric World Models](cards.md#paper-geoworld) | 潜世界模型用于长时计划时，可用非欧几何表示层级关系，并与欧氏表征对照。 |
| 计算机视觉 | 表示学习 | [MeshMosaic: Scaling Artist Mesh Generation via Local-to-Global Assembly](cards.md#paper-meshmosaic-boundary-conditioned-patches) | 大网格生成按局部区域量化与自回归，再用共享边界保持装配一致。 |
| 计算机视觉 | 表示学习 | [GenMatter: Perceiving Physical Objects with Generative Matter Models](cards.md#paper-genmatter-motion-grouping) | 按可共同独立移动的层级从粒子归并出对象，使稀疏运动与自然视频共享同一推断。 |
| 多模态学习 | 推理优化 | [IFCSR: Inference-Free Fidelity-Realism Control for One-Step Diffusion-based Real-World Image Super-Resolution](cards.md#paper-ifcsr-endpoint-image-control) | 交互改变复原的保真—自然感平衡时，预生成两个端点，在图像空间调整以免重推理。 |
| 计算机视觉 | 表示学习 | [4D Local Modeling Toward Dynamic Global Perception for Ambiguity-free Rotation-Invariant Point Cloud Analysis](cards.md#paper-ga4dpf-global-pose-reference) | 做旋转不变点云任务时，以可转向局部表示配合概率化全局姿态参考，处理对称引起的不确定。 |
| 智能体 | 强化学习 | [OS-Oracle: A Comprehensive Framework for Cross-Platform GUI Critic Models](cards.md#paper-os-oracle-consistent-critics) | 长程 GUI 操作可在执行前检查单步，并对不同平台验证评审的一致性。 |
| 计算机视觉 | 表示学习 | [Mocap-2-to-3: Multi-view Lifting for Monocular Motion Recovery with 2D Pretraining](cards.md#paper-mocap-2-to-3) | 真实三维动作标签不足时，把单目动作升维写成多视图合成，以大量二维动作预训练。 |
| 多模态学习 | 检索增强 | [Stitch-a-Demo: Creating Video Demonstrations from Multistep Descriptions](cards.md#paper-stitch-a-demo-coherence-hard-negatives) | 组装多步骤视频时，可以训练模型拒绝单步正确但状态衔接错误的组合，再分别评估步骤与整体连贯。见图 3、表 1。 |
| 生成模型 | 推理策略 | [Few-Step Diffusion Sampling Through Instance-Aware Discretizations](cards.md#paper-indis-instance-conditioned-sampling-grid) | 少步采样应对照全局最优时点和按样本分配时点，尤其在极小函数评估预算下实测。见表 4。 |
| 计算机视觉 | 三维重建与几何建模 | [Revisiting 3D Reconstruction Kernels as Low-Pass Filters](cards.md#paper-reconstruction-kernel-frequency-shape) | 选择三维重建核时可单独比较频域截止形状和空间衰减，并在不同骨干检查是否减少混叠。见表 1、3。 |
| 计算机视觉 | 三维重建与几何建模 | [P2GS: Physical Prior-guided Gaussian Splatting for Photometrically Consistent Urban Reconstruction](cards.md#paper-p2gs-factorized-camera-photometric-rendering) | 多相机观测外观不一致时，可把曝光与相机响应设为成像变量，避免重建把采集偏差写入场景。见表 3。 |
| 多模态学习 | 评估与诊断 | [UNI-OOD: Unified Object- and Image-level Out-of-Distribution Detection via Cross-Context Attentive Vision-Language Modeling](cards.md#paper-uni-ood-object-and-context-diagnostic) | 多对象场景不能用单个全图域外分数，可分别估计目标与背景的证据，在同一模型上按两个粒度验证。见表 1–3。 |
| 多模态学习 | 训练策略 | [Air-Know: Arbiter-Calibrated Knowledge-Internalizing Robust Network for Composed Image Retrieval](cards.md#paper-airknow-external-arbitration-partial-match-triplets) | 图文三元组部分匹配常使低损失分不出错标，可用离线独立验证与双流训练处理不确定数据。见表 3。 |
| 计算机视觉 | 三维重建与几何建模 | [MeshSplatting: Differentiable Rendering with Opaque Meshes](cards.md#paper-meshsplatting-connected-opaque-geometry-optimization) | 若输出要进网格引擎，可在可微渲染中直接优化互相连接的不透明网格，比较导出、显存和视角结果。见表 1–4。 |
| 多模态学习 | 评测与诊断 | [ReasonMap: Towards Fine-Grained Visual Reasoning from Transit Maps](cards.md#paper-reasonmap) | 细粒度图图推理应测有图与无图，并比较相同系列基础版和推理版。 |
| 计算机视觉 | 自监督学习 | [3D sans 3D Scans: Scalable Pre-training from Video-Generated Point Clouds](cards.md#paper-lam3c-video-pointcloud) | 缺扫描数据时，视频重建可作3D预训练输入，但应对几何噪声验证正则。 |
| 计算机视觉 | 生成模型 | [CUPID: Generative 3D Reconstruction via Joint Object and Pose Modeling](cards.md#paper-cupid-object-pose) | 由粗几何对应先估计相机位姿，再对齐像素条件细化对象。 |
| 机器学习基础与统计 | 表示学习 | [Gaussian Splatting-based Low-Rank Tensor Representation for Multi-Dimensional Image Recovery](cards.md#paper-gslr-low-rank-tensor) | 低秩张量补全时同时检验潜张量和变换基底能否表征局部高频。 |
| 多模态学习 | 模型架构 | [MUST: Modality-Specific Representation-Aware Transformer for Diffusion-Enhanced Survival Prediction with Missing Modality](cards.md#paper-must-missing-modality) | 填补缺失模态之前先分解可从其他模态推断的共有信息与不可观测的私有部分。 |
| 机器人学 | 推理与规划 | [FM-Steer: Enhance Generalist Policies with Value-Guided Cascaded Denoising](cards.md#paper-fm-steer) | 实时控制可以在早期含噪动作上做价值筛选，再精化保留候选。 |
| 计算机视觉 | 推理优化 | [LASER: Layer-wise Scale Alignment for Training-Free Streaming 4D Reconstruction](cards.md#paper-laser-layer-wise-scale-alignment) | 离线重建改成滑窗流式时，按深度层对齐尺度，避免整窗只拟合一个相似变换。 |
| 多模态学习 | 模型架构 | [Efficient Encoder-Free Fourier-based 3D Large Multimodal Model](cards.md#paper-fase3d-fourier-tokenizer) | 场景点云太长时，使用空间序列化及频域混合设计轻量 tokenizer，并测不依赖重型视觉编码器的代价。 |
| 多模态学习 | 推理优化 | [SparVAR: Exploring Sparsity in Visual AutoRegressive Modeling for Training-Free Acceleration](cards.md#paper-sparvar-cross-scale-sparsity) | 多尺度自回归生图应从中间尺度推断后续稀疏注意力，保留高分辨率生成步骤。 |
| 多模态学习 | 模型架构 | [Head-wise Adaptive Rotary Positional Encoding for Fine-Grained Image Generation](cards.md#paper-harope-head-wise-position) | 生成任务的位置编码可按注意力头拟合坐标投影，在保持相对性时允许空间轴耦合。 |
| 多模态学习 | 评测与分析 | [SO-Bench: A Structural Output Evaluation of Multimodal LLM](cards.md#paper-so-bench-structured-output-diagnostics) | 评估视觉智能体的结构化输出时，将模式合规与字段事实正确分别验收。 |
| 计算机视觉 | 损失函数与优化 | [Eulerian Gaussian Splatting using Hashed Probability Pyramids](cards.md#paper-eulerian-gaussian-splatting) | 优化离散渲染图元分布时，把图元位置视作可训练连续密度的样本。 |
| 生成模型 | 强化学习 | [RebRL: Reinforcing Discrete Visual Diffusion Models with Rebalanced Timestep Credits](cards.md#paper-rebrl-discrete-token-timestep-credit) | 给离散扩散做强化学习时，可按掩膜阶段重配信用并核对早期决策是否在训练中被低估。见图 5、表 1。 |
| 多模态学习 | 损失与奖励 | [COPO: Causal-Oriented Policy Optimization for Hallucinations of MLLMs](cards.md#paper-copo-token-sufficiency-necessity-grounding) | 若只奖励答对导致模型利用背景捷径，可分别检验相关证据的充分性和必要性，并将结果加入训练奖励。见表 3。 |
| 机器人学 | 表征学习 | [AutoTraces: Autoregressive Trajectory Forecasting via Multimodal Large Language Models](cards.md#paper-autotraces-hybrid-continuous-waypoint-tokens) | 接入轨迹回归时可对照文字序列与专用标记加连续坐标嵌入，保留自回归生成以支持可变长度。见表 2 和图 4。 |
| 多模态学习 | 推理策略 | [Think Visually, Reason Textually: Vision-Language Synergy in Abstract Reasoning](cards.md#paper-arc-modality-routed-rule-reasoning) | 可在同一空间推理任务中用视觉归纳规则、文本精确执行，并切换模态复核错误。见表 2。 |
| 多模态学习 | 评估与诊断 | [Lyapunov Probes for Hallucination Detection in Large Foundation Models](cards.md#paper-lyapunov-probes-perturbation-stability-for-hallucination) | 幻觉探针可同时检查隐状态的局部稳定性和静态可分性，比较显式稳定约束及跨域迁移。见表 3、4。 |
| 多模态学习 | 评估与诊断 | [Do VLMs Perceive or Recall? Probing Visual Perception vs. Memory with Classic Visual Illusions](cards.md#paper-vi-probe-perception-versus-template-recall) | 判断模型依赖视觉还是图式记忆时，可翻转视觉线索并保留无诱因匹配控制，分别报告翻转一致性与固定答法。见表 2。 |
| 机器人学 | 表征学习 | [Bidirectional Cross-Modal Prompting for Event-Frame Asymmetric Stereo](cards.md#paper-cross-modal-stereo-dual-domain-projection) | 异构相机匹配可同时在两个传感域映射对方的信息，比较只做单域对齐时的视差误差。见表 5。 |
| 机器人学 | 生成模型 | [MaskDexGrasp: Generative Masked Modeling for Part-Aware Dexterous Grasp Synthesis](cards.md#paper-maskdexgrasp) | 抓取动作可按手掌与各指分词，使用掩码建模支持补全和局部改动。 |
| 多模态学习 | 推理策略 | [Infinity-RoPE: Action-Controllable Infinite Video Generation Emerges From Autoregressive Self-Rollout](cards.md#paper-infinity-rope) | 长序列滚动生成可将位置编码动态重基准化，并只在切换任务时有限重置缓存。 |
| 多模态学习 | 训练策略 | [PureCC: Pure Learning for Text-to-Image Concept Customization](cards.md#paper-purecc) | 注入个性概念时，将新概念增量和原条件预测分离，并将旧能力漂移纳入评价。 |
| 计算机视觉 | 训练策略 | [U^2Flow: Uncertainty-Aware Unsupervised Optical Flow Estimation](cards.md#paper-u2flow) | 无标签位移估计可先由增强一致性学习逐像素不确定性，再用于细化和融合。 |
| 机器学习基础与统计 | 生成模型 | [Back to Basics: Let Denoising Generative Models Denoise](cards.md#paper-jit-denoise-clean-data) | 选择扩散网络输出时要单独比较干净数据预测与噪声预测，损失的计算空间可另选。 |
| 机器人学 | 强化学习 | [PvP: Data-Efficient Humanoid Robot Learning with Proprioceptive-Privileged Contrastive Representations](cards.md#paper-pvp-privileged-proprioception) | 训练时将本体观测与特权状态配对做对比学习，减少手写增强并保持部署输入简单。 |
| 计算机视觉 | 知识蒸馏 | [Scaling Dense Event-Stream Pretraining from Visual Foundation Models](cards.md#paper-structure-aware-event-distillation) | 将稠密视觉教师蒸馏到稀疏传感器时，对齐语义结构而非只逐位置回归。 |
| 机器学习基础 | 评测与分析 | [When Do Models Actually Decide? Mapping the Layer-Wise Decision Timeline in Pretrained Neural Networks](cards.md#paper-layer-wise-decision-timeline) | 设计早退时按多层稳定协议报告哪些样本可早退，避免单层探针首次命中等同于已决策。 |
| 计算机视觉 | 模型架构 | [CoWTracker: Tracking by Warping instead of Correlation](cards.md#paper-cowtracker-warping) | 高分辨率点跟踪用当前轨迹回变目标特征并迭代更新，避免显式相关体。 |
| 多模态学习 | 可解释性与诊断 | [Understanding Temporal Logic Consistency in Video-Language Models through Cross-Modal Attention Discriminability](cards.md#paper-tcas-temporal-attention-discriminability) | 视频答案改写后不一致时，检查跨模态注意力是否区分时间点，再实验性增强时序区分。 |
| 机器人学 | 评测与分析 | [CapNav: Benchmarking Vision Language Models on Capability-conditioned Indoor Navigation](cards.md#paper-capnav-capability-conditioned-navigation) | 衡量跨机体导航时按具体尺寸和越障能力划分可行路径，避免用统一可达标签。 |
| 多模态学习 | 可解释性与诊断 | [Where Culture Fades: Revealing the Cultural Gap in Text-to-Image Generation](cards.md#paper-cultural-representation-activation) | 跨语言生图出现文化泛化时，先探测表征是否可激活，再决定做定层调整还是更新整网。 |
| 机器人学 | 三维重建与几何建模 | [Depth Hypothesis Guided Iterative Refinement for Event-Image Monocular Depth Estimation](cards.md#paper-hypodepth-discrete-hypothesis-residual-search) | 单目传感深度可先保留离散候选，再做逐尺度残差搜索，用同骨干的连续深度反馈验证收敛与误差。见表 4。 |
| 生成模型 | 模型蒸馏 | [Transition Matching Distillation for Fast Video Generation](cards.md#paper-tmd-backbone-reuse-inner-transition-head) | 少步视频蒸馏可在外层更新语义、内层只用轻量头细化，并按实际执行的主干块数计算成本。见表 1。 |
| 机器人学 | 三维重建与几何建模 | [MoCapAnything: Unified 3D Motion Capture for Arbitrary Skeletons from Monocular Videos](cards.md#paper-mocapanything-reference-conditioned-skeleton-ik) | 面向变化骨架时，可将关节轨迹估计与目标资产旋转解算分开，以参考几何条件控制输出。见表 1、2。 |
| 多模态学习 | 三维重建与几何建模 | [No Calibration, No Depth, No Problem: Cross-Sensor View Synthesis with 3D Consistency](cards.md#paper-cross-sensor-confidence-densification-and-self-match) | 跨传感器难标定时，可以把稀疏跨域匹配先用置信度补稠，再用同域自匹配剔除不一致，分别查看增益。见表 5。 |
| 计算机视觉 | 表征学习 | [From Static to Dynamic: Exploring Self-supervised Image-to-Video Representation Transfer Learning](cards.md#paper-cosettle-temporal-consistency-semantic-separability) | 图像骨干转到视频时，可冻结骨干并同时考核跨视频可分性和同视频时序一致性，避免只优化同视频匹配。见表 4、5。 |
| 生成模型 | 训练策略 | [Transition Models: Rethinking the Generative Learning Objective](cards.md#paper-tim-finite-interval-generation-objective) | 希望同一模型可一次生成或多步逐级改进时，可直接学习任意有限区间的生成转移，并画出函数评估数与质量的关系。见表 6。 |
| 多模态学习 | 模型效率 | [Unified Spatiotemporal Token Compression for Video-LLMs at Ultra-Low Retention](cards.md#paper-global-video-token-selection-with-redundancy-refill) | 视频标记保留率很低时，可在统一时空池分配预算，把显著性与去冗余及合并协同，并测哪些任务仍丢证据。见表 5。 |
| 多模态学习 | 训练策略 | [Bootstrapping Multi-view Learning for Test-time Noisy Correspondence](cards.md#paper-bml-noisy-correspondence) | 将模态本身质量与视图配错视为异质误差，使用人为控制的错配标注训练两类可靠性。 |
| 多模态学习 | 持续学习 | [Octopus: History-Free Gradient Orthogonalization for Continual Learning in Multimodal Large Language Models](cards.md#paper-octopus-hifgo) | 不能存旧数据时，分阶段执行当前任务适配和梯度去干扰，并显式比较任务顺序。 |
| 计算机视觉 | 推理策略 | [Guiding a Diffusion Model by Swapping Its Tokens](cards.md#paper-self-swap-guidance) | 没有可用条件分支时，可用语义错配潜 token 生成对照预测，再利用两支差异指导扩散。 |
| 智能体 | 自动化工作流 | [CLiViS: Unleashing Cognitive Map through Linguistic-Visual Synergy for Embodied Visual Reasoning](cards.md#paper-clivis-cognitive-map) | 跨时刻具身推理可让计划器按需调视觉模型，再累计可更新的结构化场景记忆。 |
| 计算机视觉 | 自监督学习 | [Next-Scale Prediction: A Self-Supervised Approach for Real-World Image Denoising](cards.md#paper-next-scale-prediction) | 去噪自监督可分别选择输入和目标尺度，以较粗输入降低噪声相关，同时保留细目标监督。 |
| 机器学习基础 | 可解释性与诊断 | [Mitigating Simplicity Bias in OOD Detection through Object Co-occurrence Analysis](cards.md#paper-oco-object-cooccurrence-ood) | 单个对象看起来都熟悉时，用对象组合共现的异常程度判断近分布外。 |
| 多模态学习 | 评测与分析 | [GroundingME: Exposing the Visual Grounding Gap in MLLMs through Multi-Dimensional Evaluation](cards.md#paper-groundingme-rejection-tests) | 视觉指代评估单设不可定位的拒答场景，避免常规准确率掩盖强行输出。 |
| 多模态学习 | 微调与适配 | [AGFT: Alignment-Guided Fine-Tuning for Zero-Shot Adversarial Robustness of Vision-Language Models](cards.md#paper-agft-soft-alignment) | 视觉语言模型做防御微调时保留原模型对全部文本的软语义对齐，并校准新的输出分布。 |
| 计算机视觉 | 自监督学习 | [GEM-TFL: Bridging Weak and Full Supervision for Forgery Localization through EM-Guided Decomposition and Temporal Refinement](cards.md#paper-gem-tfl-weak-temporal-localization) | 只有视频级标签但要定位时段时，用潜属性丰富训练信号并联合重排相邻候选。 |
| 机器学习基础 | 模型架构 | [Coupling Liquid Time-Constant Encoders with Modern Hopfield Memory](cards.md#paper-ltc-hopfield-memory) | 连续时间模型中可把快速动态与较长期内容检索分开，避免单隐状态互相覆盖。 |
| 机器人学 | 推理策略 | [VLM-Loc: Localization in Point Cloud Maps via Vision-Language Models](cards.md#paper-vlm-loc-partial-scene-node-assignment) | 用描述在地图中找位置时，应允许只对齐一部分图节点，避免未被描述的对象强制参与。见表 2。 |
| 生成模型 | 时序建模 | [FloodDiffusion: Tailored Diffusion Forcing for Streaming Motion Generation](cards.md#paper-flooddiffusion-streaming-motion-noise-schedule) | 把视频扩散强制迁移到流式动作前，可对照训练内双向注意力和下三角噪声计划，验证条件变化与动作衔接。见表 3。 |
| 多模态学习 | 数据增强 | [From Panel to Pixel: Zoom-In Vision-Language Pretraining from Biomedical Scientific Literature](cards.md#paper-panel2patch-hierarchical-figure-supervision) | 图文语料存在图、面板、局部标记多级结构时，可为各级保留分别对应的文本并单测局部检索。见表 4。 |
| 计算机视觉 | 三维重建与几何建模 | [PQDT: Pseudo-Query Dual Transformer for Robust Point Cloud Restoration](cards.md#paper-pqdt-pseudo-query-spatial-restoration) | 点云退化时可让重建查询从局部种子出发，而非压缩进单一全局表示，并逐项比较种子和位置编码。见表 3。 |
| 多模态学习 | 少样本学习 | [Love Me, Love My Label: Rethinking the Role of Labels in Prompt Retrieval for Visual In-Context Learning](cards.md#paper-lapr-label-consistent-demonstration-retrieval) | 挑视觉上下文示例时可把标签兼容性与外观相似性分开考虑，以相同示例预算检验标签信息的增量。见表 3。 |
| 生成模型 | 表征学习 | [MeshRipple: Structured Autoregressive Generation of Artist-Meshes](cards.md#paper-meshripple-frontier-topology-tokenization) | 生成连通离散结构时可把顺序设为沿当前拓扑边界扩张，而非机械串行化，并把生成质量和长程记忆开销分开测。见表 2、4。 |
| 计算机视觉 | 异常检测 | [VisualAD: Language-Free Zero-Shot Anomaly Detection via Vision Transformer](cards.md#paper-visualad) | 零样本异常检测可先检验纯视觉正常/异常锚 token 能否替代文本提示。 |
| 多模态学习 | 推理加速 | [Adaptive Spectral Feature Forecasting for Diffusion Sampling Acceleration](cards.md#paper-spectrum-diffusion-forecast) | 跳过多个去噪步时以全局光滑基预测特征，并用实际误差自适应安排重算。 |
| 机器学习基础与统计 | 模型架构 | [Progressive Neural Architecture Generation](cards.md#paper-progressive-architecture-generation) | 架构生成先产粗子结构后扩张，在每次扩张时检查有效性。 |
| 计算机视觉 | 训练策略 | [Shape-of-You: Fused Gromov-Wasserstein Optimal Transport for Semantic Correspondence in-the-Wild](cards.md#paper-shape-of-you-fgw) | 伪标签匹配时，将特征相似和结构相似合并，并保留软分配而非硬最近邻。 |
| 计算机视觉 | 推理加速 | [EDGS: Eliminating Densification for Efficient Convergence of 3DGS](cards.md#paper-edgs-dense-initialization) | 若可获得高质量稠密像素对应，可从初始化解决细几何覆盖，减少逐步增密。 |
| 多模态学习 | 推理策略 | [When Numbers Speak: Aligning Textual Numerals and Visual Instances in Text-to-Video Diffusion Models](cards.md#paper-numina) | 生成对数量敏感时，先从隐场定位可计数实例，再调整布局并重生成。 |
| 多模态学习 | 模型架构 | [Text-Image Conditioned 3D Generation](cards.md#paper-tigon-conditioned-3d) | 联合图文条件前先做各自独立推理及晚融合，测两个模态在几何和语义上的互补。 |
| 多模态学习 | 模型架构 | [Soft Modality-Guided Expert Specialization in MoE-VLMs](cards.md#paper-smoes-soft-modality-routing) | 多模态 MoE 训练可用随层变化的软模态分数引导专家分组，以减少跨设备通信。 |
| 机器学习基础 | 微调与适配 | [Critical Patch-Aware Sparse Prompting with Decoupled Training for Continual Learning on the Edge](cards.md#paper-cps-prompt-edge-continual) | 边缘持续学习时按任务选择训练图块，并将提示和分类头反传拆开。 |
| 机器人学 | 评测与分析 | [Failure Modes for Deep Learning-Based Online Mapping: How to Measure and Address Them](cards.md#paper-online-mapping-failure-mode-controls) | 地图模型的域外评估同时控制地理邻近和几何相似度，并分别报告两种过拟合。 |
| 多模态学习 | 评测与分析 | [Think 360deg: Beyond Depth: Evaluating the Width-centric Reasoning Capability of MLLMs](cards.md#paper-think360-reasoning-width) | 评估多模态搜索时除了推理步数，还控制需要探索的并行候选和回溯。 |
| 计算机视觉 | 自监督学习 | [Multi-Prototype Compactness and Boundary-Aware Synthesis for Unsupervised Anomaly Detection](cards.md#paper-pgbl-boundary-anomaly-synthesis) | 正常类别有多个模式时，以多原型建模，并在簇边界构造难伪异常。 |
| 计算机视觉 | 评测与分析 | [ORBIT: Benchmarking SfM in the Wild with 360deg Video](cards.md#paper-orbit-panoramic-pose-reference) | 要低成本获得窄视场视频难例的位姿参照，可用同一全景视频先估轨迹再进行裁剪重投影。 |
| 多模态学习 | 数据增强 | [VideoNet: A Large-Scale Dataset for Domain-Specific Action Recognition](cards.md#paper-videonet-single-action-filtering) | 训练细粒度视频识别时应对照按单一动作净化与仅按字幕定位扩样，分开测数据量和任务准确率。见表 5。 |
| 机器人学 | 规划与控制 | [DynBridge: Bridging Imagination and Control through Interaction Dynamics for Robot Manipulation](cards.md#paper-dynbridge-shared-interaction-dynamics) | 将未来预测用于动作时，可共享对象位移与交互表征，比较面向控制的变化模型和仅预测画面或轨迹的方案。见第 4.2 节、表 1。 |
| 多模态学习 | 评估与诊断 | [Deeper Thought, Weaker Aim: Understanding and Mitigating Perceptual Impairment during Reasoning in Multimodal Large Language Models](cards.md#paper-vrga-reasoning-visual-attention-dispersion) | 长推理若降低视觉题表现，可用空间聚焦而非只用图像注意总量定位关键头，再做遮蔽对照。见表 2。 |
| 生成模型 | 生成建模 | [BulletTime: Decoupled Control of Time and Camera Pose for Video Generation](cards.md#paper-bullettime-independent-world-time-camera-control) | 视频世界模型可将世界时间与相机轨迹独立采样和输入，并单独验证时间控制、位置编码与归一化。见表 4、5。 |
| 机器人学 | 规划与控制 | [Adaptive Action Chunking at Inference-time for Vision-Language-Action Models](cards.md#paper-aac-action-entropy-adaptive-horizon) | 视觉动作控制可用多个候选动作块的分歧决定执行多久后重新观测，同时测选样开销。见表 3、4。 |
| 多模态学习 | 模型融合 | [Beyond Layer-Wise Merging: Chain-of-Merging for Vision-Language Models](cards.md#paper-chain-of-merging-activation-matched-layers) | 融合语言模型与视觉语言模型时，可按输入的层激活结构选配层，再决定每层合并权重。见第 3.3、3.4 节与表 1。 |
| 计算机视觉 | 数据增强 | [Synthetic Object Compositions for Scalable and Accurate Learning in Detection, Segmentation, and Grounding](cards.md#paper-soc-label-preserving-object-composition) | 需要准确掩膜的合成训练可从独立对象片段与可控布局出发，再做保标签的外观协调。见表 4。 |
| 多模态学习 | 训练策略 | [WeaveTime: Streaming from Earlier Frames into Emergent Memory in VideoLLMs](cards.md#paper-weavetime) | 先用打乱帧对照诊断时序盲区，再对在线缓存分别处理当前帧和历史证据。 |
| 计算机视觉 | 数据增强 | [Towards Generalized Multimodal Homography Estimation](cards.md#paper-multimodal-homography-synthesis) | 没有目标传感器配对监督时，可保留几何结构并合成外观差异，再在真实未知模态上测试。 |
| 机器人学 | 训练策略 | [FLARE: A Failure-Aware Framework for Autonomous Correction and Recovery in Visual-Language Robotic Manipulation](cards.md#paper-flare-retry-reset) | 按错误是否能从现有环境状态继续，把可重试偏差和需重置的失败分开收集。 |
| 计算机视觉 | 测试时适应与推理 | [Render-to-Adapt: Unsupervised Personal Adaptation for Gaze Estimation](cards.md#paper-render-to-adapt) | 个体适配缺标注时，可从模型预测渲染对照，再按观测局部一致性优化，并报告个体退化。 |
| 多模态学习 | 强化学习 | [VideoAuto-R1: Video Auto Reasoning via Thinking Once, Answering Twice](cards.md#paper-videoauto-r1) | 训练时同时奖励首答与复核答案，推理按首答置信度决定是否继续长链。 |
| 智能体 | 自动化工作流 | [ReFAct: Empowering Multimodal Web Agents with Visual and Context Focusing](cards.md#paper-refact) | 网页视觉噪声大时，代理应能聚焦判断相关区域，并将暂时无关信息放入可回读记忆。 |
| 计算机视觉 | 表示学习 | [SharpTimeGS: Sharp and Stable Dynamic Gaussian Splatting via Lifespan Modulation](cards.md#paper-sharptimegs-lifespan-modulation) | 动态场景用平顶时域可见性记录图元何时存在，并以寿命调节运动先验。 |
| 多模态学习 | 表示学习 | [Extending One-Step Image Generation from Class Labels to Text via Discriminative Text Representation](cards.md#paper-meanflow-discriminative-text) | 把一步生图扩展到开放文本时，单独测条件的区分性，而不只扩大文本编码器。 |
| 计算机视觉 | 可解释性与诊断 | [FILTR: Extracting Topological Features from Pretrained 3D Models](cards.md#paper-filtr-topology-probes) | 几何任务表现好也应探测冻结点云特征是否包含需要的拓扑环和空腔。 |
| 机器人学 | 表示学习 | [MSGNav: Unleashing the Power of Multi-modal 3D Scene Graph for Zero-Shot Embodied Navigation](cards.md#paper-msgnav-visual-scene-graph-edges) | 导航场景图的关系边保留可重查图像，决策终点时另检查目标可见性。 |
| 机器学习基础 | 评测与分析 | [A Combination of Noise and Bilateral Filters Achieve Supralinear and Scalable Adversarial Robustness in CNNs](cards.md#paper-noise-bilateral-defense-synergy) | 鲁棒视觉防御可比较随机化和保边去噪的组合收益，单项增益不足以预测叠加。 |
| 计算机视觉 | 知识蒸馏 | [Distilling Quasi-Conformal Mapping: A Generalizable and Efficient Solution for Wide-Angle Correction](cards.md#paper-qdwc-geometric-teacher-distillation) | 昂贵几何求解器无需人工标签也可当教师，蒸馏预测连续校正流。 |
| 多模态学习 | 持续学习 | [Subspace Alignment for CLIP-based Continual Learning via Canonical Correlation Analysis](cards.md#paper-cca-cl-crossmodal-drift-sufficient-statistics) | 一侧模态持续漂移时，可累计图文协方差并用 CCA 重建共享子空间，先对照不作任何对齐的基线。见表 2。 |
| 智能体 | 持续学习 | [CGL: Advancing Continual GUI Learning via Reinforcement Fine-Tuning](cards.md#paper-cgl-constrained-rl-for-continual-gui-retention) | 连续学习 GUI 操作时，可把新任务成功率和旧技能遗忘一起测，验证受约束强化学习与监督微调比例。见表 4。 |
| 计算机视觉 | 三维重建与几何建模 | [From Feature Learning to Spectral Basis Learning: A Unifying and Flexible Framework for Efficient and Robust Shape Matching](cards.md#paper-advanced-functional-maps-learned-spectral-basis) | 形状对应可在优化特征的同时学习映射所用基函数，对照固定谱基在跨数据、各向异性网格下的表现。见表 4。 |
| 机器人学 | 规划与控制 | [Diffusion Forcing Planner: History-Annealed Planning with Time-Dependent Guidance for Autonomous Driving](cards.md#paper-dfp-annealed-history-conditioning-for-planning) | 历史既提供平滑性也会诱使规划器照搬旧轨迹，可以比较固定历史引导和随去噪阶段变化的引导。见表 3。 |
| 生成模型 | 模型效率 | [TC-Pade: Trajectory-Consistent Pade Approximation for Diffusion Acceleration](cards.md#paper-tc-pade-rational-feature-trajectory-extrapolation) | 低步扩散缓存可以比较有理与多项式外推，并根据轨迹变化动态刷新，统计时延和输出质量。见表 1、5。 |
| 生成模型 | 三维重建与几何建模 | [Splatent: Splatting Diffusion Latents for Novel View Synthesis](cards.md#paper-splatent-geometry-detail-split-latent-rendering) | 潜空间多视图重建可把低频几何交给三维渲染，仅以参考图引导扩散补充高频，单测参考数量与跨视角一致性。见表 2、3。 |
| 计算机视觉 | 自监督学习 | [Franca: Nested Matryoshka Clustering for Scalable Visual Representation Learning](cards.md#paper-franca-nested-clustering) | 自监督聚类用多粒度嵌套标签处理语义歧义，并分离与内容无关的空间位置偏差。 |
| 机器人学 | 推理与规划 | [Towards Open Environments and Instructions: General Vision-Language Navigation via Fast-Slow Interactive Reasoning](cards.md#paper-slow4fast-vln) | 陌生环境导航可用慢推理提供开放语义策略，再让快策略在闭环按最新观测执行。 |
| 多模态学习 | 评测与诊断 | [StreamReady: Learning What to Answer and When in Long Streaming Videos](cards.md#paper-streamready) | 在线答复应把证据出现前猜测与出现后延迟分开处罚，结合正确性报告有效准确率。 |
| 多模态学习 | 评测与诊断 | [Benchmarking Single-Factor Physical Video-to-Audio Generation](cards.md#paper-flatsounds-single-factor) | 评估跨模态物理推理时用单因素反事实和有无文本对照，同时监测正确性与时序。 |
| 计算机视觉 | 训练策略 | [UniSH: Unifying Scene and Human Reconstruction in a Feed-Forward Pass](cards.md#paper-unish-real-geometry-supervision) | 合成数据学粗几何后，用真实无标签数据上可量化的跨表示对应缩小域差。 |
| 多模态学习 | 模型架构 | [SpaceMind: Camera-Guided Modality Fusion for Spatial Reasoning in Vision-Language Models](cards.md#paper-spacemind) | 将相机嵌入用于几何 token 选择与融合门控，而非仅作附带信息。 |
| 计算机视觉 | 训练策略 | [Concept-Guided Fine-Tuning: Steering ViTs away from Spurious Correlations to Improve Robustness](cards.md#paper-concept-guided-vit) | 为降低背景捷径，用多个属性级概念区域监督相关性，而不是只提供前景掩码。 |
| 机器学习基础 | 损失函数与优化 | [Confusion-Aware Spectral Regularizer for Long-Tailed Recognition](cards.md#paper-car-spectral-confusion-regularizer) | 关注长尾最差类别时，把频率加权的混淆谱范数纳入训练。 |
| 机器人学 | 强化学习 | [SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models](cards.md#paper-srpo-self-referential-policy) | 二元成功奖励太稀疏时，可用同批成功轨迹给失败轨迹的进度分级。 |
| 计算机视觉 | 推理优化 | [FlashVGGT: Efficient and Scalable Visual Geometry Transformers with Compressed Descriptor Attention](cards.md#paper-flashvggt-descriptor-attention) | 前馈多视图重建可将跨帧的全局键值替换为每帧压缩描述符，并缓存跨块。 |
| 多模态学习 | 评测与分析 | [Differences That Matter: Auditing Models for Capability Gap Discovery and Rectification](cards.md#paper-auditdm-model-disagreement) | 对照多个模型的相互分歧，主动构造诊断样例，再把找到的失败用于定向修正训练。 |
| 多模态学习 | 自监督学习 | [Semantic Noise Reduction via Teacher-Guided Dual-Path Audio-Visual Representation Learning](cards.md#paper-tg-dp-decoupled-masking) | 同时做掩码恢复和跨模态对比时，分开为两路选择可见 token。 |
| 机器学习基础 | 模型架构 | [Parallelised Differentiable Straightest Geodesics for 3D Meshes](cards.md#paper-differentiable-straightest-geodesics) | 网格模型需要沿曲面卷积或流动时，使用可并行、可微的指数映射代替欧氏邻域。 |
| 机器人学 | 三维重建与几何建模 | [Fusion of Depth and Semantics for Probabilistic Floorplan Localization](cards.md#paper-floorplan-distribution-aware-depth-semantic-fusion) | 用二维地图定位时，可匹配射线概率分布并按不确定性降权，减少遮挡导致的虚假几何约束。见表 4。 |
| 多模态学习 | 表征学习 | [MTA: Multimodal Task Alignment for BEV Perception and Captioning](cards.md#paper-mta-intermediate-alignment-for-joint-perception-captioning) | 让语言与三维感知共享信息时，可以在跨模态桥的不同深度挂对齐目标，分别检查感知与描述的变化。见表 4、5。 |
| 计算机视觉 | 参数高效微调 | [GeoSAM2: Unleashing the Power of SAM2 for 3D Part Segmentation](cards.md#paper-geosam2-geometry-aware-prompted-part-segmentation) | 把二维提示分割用到无纹理物体，可渲染不同几何视图，以残差适配复用分割先验，再回投到三维。见表 3。 |
| 计算机视觉 | 自监督学习 | [Time Without Time: Pseudo-Temporal Representation for Space-Time Super-Resolution](cards.md#paper-pseudo-time-masked-image-pretraining-for-video-sr) | 缺少视频标注时，可把一张图变成互补缺失的伪时序预训练输入，尤其检查低数据微调是否改善。见表 1。 |
| 多模态学习 | 隐私保护 | [Unsafe2Safe: Controllable Image Anonymization for Downstream Utility](cards.md#paper-unsafe2safe-privacy-utility-edit-evaluation) | 训练图像匿名化可只编辑敏感区域，并以模型效用和身份残留分别对比不同文本条件。见表 3。 |
| 多模态学习 | 推理压缩 | [GaussianVision: Vision-Language Alignment from Compressed Image Representations using 2D Gaussian Splatting](cards.md#paper-gaussianvision) | 视觉输入压缩可从空间自适应表示直接接到跨模态骨干，并对照解码回像素的成本。 |
| 计算机视觉 | 测试时适应与推理 | [Learning 3D Reconstruction with Priors in Test Time](cards.md#paper-test-time-3d-priors) | 相机姿态、内参和深度不规则可用时，将它们转为输出约束，避免为每种输入组合重训。 |
| 机器学习基础与统计 | 联邦学习 | [Domain Sensitive Federated Learning with Fisher-Informed Pruning](cards.md#paper-fedfip) | 联邦模型需要结构对齐又有域偏差时，共享稀疏核心并允许客户端恢复少数域特异通道。 |
| 计算机视觉 | 评测与诊断 | [EgoXtreme: A Dataset for Robust Object Pose Estimation in Egocentric Views under Extreme Conditions](cards.md#paper-egoxtreme-pose-evaluation) | 可穿戴位姿评估按光照、模糊和遮挡分层，检查预处理能否真正改善下游位姿。 |
| 多模态学习 | 模型架构 | [PAVAS: Physics-Aware Video-to-Audio Synthesis](cards.md#paper-pavas-physical-video-audio) | 视频到音频生成可加入物体级物理条件，并用声学物理一致性与同步指标分别验收。 |
| 计算机视觉 | 自监督学习 | [Exploring Adaptive Masked Reconstruction for Self-Supervised Skeleton-Based Action Recognition](cards.md#paper-amr-skeleton) | 自监督重建可用更大输出块加速，再以运动信息聚焦解码监督。 |
| 机器人学 | 推理优化 | [Global Prior Meets Local Consistency: Dual-Memory Augmented Vision-Language-Action Model for Efficient Robotic Manipulation](cards.md#paper-optimusvla-dual-memory) | 将相似任务轨迹检索为动作生成先验，再用已执行动作约束当前生成。 |
| 多模态学习 | 自监督学习 | [3D-IDE: 3D Implicit Depth Emergent](cards.md#paper-3d-ide-privileged-geometry) | 视觉语言模型需要空间理解时，可在训练提供几何特权信息，而部署只读二维观察。 |
| 机器学习基础 | 损失函数与优化 | [CoRiM: Conflict-driven Risk Minimization for Dynamic Multimodal Fusion](cards.md#paper-corim-conflict-risk-fusion) | 按样本动态融合时权重应同时反映预测分布冲突及不确定性。 |
| 多模态学习 | 模型架构 | [Sculpt4D: Generating 4D Shapes via Sparse-Attention Diffusion Transformers](cards.md#paper-sculpt4d-sparse-time-mask) | 动态对象生成可同时保留首帧身份锚点和随时间衰减的局部上下文。 |
| 机器学习基础 | 迁移与泛化 | [FedARA: Resource-adaptive Low-rank Personalized Federated Learning via Anchor-driven Representation Alignment on Heterogeneous Edge Devices](cards.md#paper-fedara-anchor-rank-adaptation) | 异构设备共同训练时，让不同客户端选低秩容量，以公共锚表征对齐不同子模型。 |
| 机器人学 | 推理优化 | [WhisperNet: A Scalable Solution for Bandwidth-Efficient Collaboration](cards.md#paper-whispernet-receiver-centric-budget) | 多智能体共享观察时，由接收者看低带宽摘要再全局分配请求，而非各发送端彼此独立筛选。 |
| 生成模型 | 自监督学习 | [One-to-All Animation: Alignment-Free Character Animation and Image Pose Transfer](cards.md#paper-one-to-all-reference-misalignment-as-outpainting) | 参考图与控制序列布局不同，可把错位训练统一为遮挡外扩任务，并检查保留参考姿态作为条件的贡献。见表 3、4。 |
| 多模态学习 | 表征学习 | [SegCompass: Exploring Interpretable Alignment with Sparse Autoencoders for Enhanced Reasoning Segmentation](cards.md#paper-segcompass-sparse-visual-grounding-bottleneck) | 让推理指令连接分割时，可用可检查的稀疏激活中间层，并共同检验激活覆盖与最终掩膜。见图 5、表 4。 |
| 多模态学习 | 表征学习 | [MultiModalPFN: Extending Prior-Data Fitted Networks for Multimodal Tabular Learning](cards.md#paper-mmpfn-modality-token-count-control) | 把图像或文本接入表格模型时，可用重复同一表示作为对照，区分标记数增加与内容变强，并考虑跨注意力压缩。见表 4。 |
| 机器学习 | 对比学习 | [Multi-Hierarchical Contrastive Spectral Fusion for Multi-View Clustering](cards.md#paper-mcsf-neighborhood-spectral-clustering-regularization) | 多视图聚类可同时约束单视图近邻结构与跨视图共识，对照仅优化重建或对比时是否破坏原有邻域。见表 3。 |
| 生成模型 | 时序建模 | [Causal Motion Diffusion Models for Autoregressive Motion Generation](cards.md#paper-cmdm-framewise-sampling-horizon-stability) | 长程动作生成可以分配按帧变化的去噪预算，同时测文本匹配和关节瞬变，避免只看短片质量。见表 4。 |
| 生成模型 | 自监督学习 | [Rethinking UMM Visual Generation: Masked Modeling for Efficient Image-Only Pre-training](cards.md#paper-iomm-image-only-pretrain-mixed-finetune) | 图文配对有限时可先在图像上做掩码预训练，但后续微调仍应留配对监督，并单测知识与组合能力。见表 2。 |
| 机器人学 | 持续学习 | [GeCo-SRT: Geometry-aware Continual Adaptation for Cross-Task Sim-to-Real Transfer](cards.md#paper-geco-srt) | 跨多个仿真到实机任务时，让专家按可复用局部几何分工，并用专家信号决定回放优先级。 |
| 多模态学习 | 表示学习 | [Dynamics: Language-Based Representation for Inferring Rigid-Body Dynamics From Videos](cards.md#paper-dynamics-language-physics) | 从视频推断动态时，让模型输出可在物理引擎复演的结构化场景，并用复演比较候选。 |
| 机器学习基础与统计 | 推理加速 | [E$^2$-SCI: Elastic Edge-Cloud Speculative Decoding via Credit Inertia](cards.md#paper-e2-sci) | 边云推测解码可用相邻窗口的接受率相关性分配核验预算，并独立测质量。 |
| 计算机视觉 | 生成模型 | [CARD: Correlation Aware Restoration with Diffusion](cards.md#paper-card-correlated-noise) | 传感器噪声明显相关时，为扩散恢复先白化观测并在相同坐标中更新。 |
| 计算机视觉 | 模型架构 | [3D Gaussian Splatting at Arbitrary Resolutions with Compact Proxy Anchors](cards.md#paper-resolution-adaptive-gaussians) | 多分辨率渲染时把目标像素覆盖作为条件，按需生成局部细节并检查锚存储。 |
| 多模态学习 | 强化学习 | [Specificity-aware reinforcement learning for fine-grained open-world classification](cards.md#paper-specialrl) | 开放分类奖励需区分回答是否正确与是否具体，并用同组候选校准具体性。 |
| 机器人学 | 模型架构 | [TopoHR: Hierarchical Centerline Representation for Cyclic Topology Reasoning in Driving Scenes with Point-to-Instance Relations](cards.md#paper-topohr) | 预测结构图时，在元素查询和实例连接之间多轮传递关系，联合修正检测和拓扑。 |
| 智能体 | 强化学习 | [Thinking with Programming Vision: Towards a Unified View for Thinking with Images](cards.md#paper-codevision-visual-transformations) | 视觉工具代理训练应包含可逆图像变换、连续工具调用和出错后的恢复。 |
| 计算机视觉 | 推理优化 | [Pip-Stereo: Progressive Iterations Pruner for Iterative Optimization based Stereo Matching](cards.md#paper-pipstereo-iteration-pruning) | 迭代立体匹配可先定位有效视差更新时空位置，再减少冗余迭代并使用稀疏算子。 |
| 多模态学习 | 知识蒸馏 | [Fast Reasoning Segmentation for Images and Videos](cards.md#paper-fastreasonseg-reasoning-distillation) | 蒸馏分割推理时先将感知转成紧凑可推理场景表示，再保留教师的多步定位过程。 |
| 多模态学习 | 推理优化 | [Blink: Dynamic Visual Token Resolution for Enhanced Multimodal Understanding](cards.md#paper-blink-dynamic-token-resolution) | 视觉语言推理根据各层关注区域临时提升部分 token 解析度，失去关注时回收。 |
| 多模态学习 | 损失函数与优化 | [Towards Fine-Grained Attribution: Instance-Aware Preference Optimization for Aligning Diffusion Models](cards.md#paper-iapo-instance-credit) | 偏好数据只有整图排序时，进一步标注对应实例的偏好差异，避免把整图偏好误分到局部。 |
| 计算机视觉 | 表示学习 | [MoRGS: Efficient Per-Gaussian Motion Reasoning for Streamable Dynamic 3D Scenes](cards.md#paper-morgs-per-gaussian-motion) | 在线动态三维重建用少数视点流监督图元运动，并显式吸收二维与三维投影的差异。 |
| 生成模型 | 模型效率 | [TimeRipples: Accelerating vDiTs by Understanding the Spatio-Temporal Correlations in Latent Space](cards.md#paper-timeripples-channel-structured-video-attention-reuse) | 视频扩散加速可根据潜空间中空间与时间相关性分别判断注意力重用，记录实际时延和质量。见表 2。 |
| 计算机视觉 | 推理策略 | [PromptMoE: A Segmentation Refinement Framework Leveraging Mixture of Experts for Improved Prompting](cards.md#paper-promptmoe-image-conditioned-refinement-expert-selection) | 粗掩膜错误多样时，可先用框、点、掩膜作基线，再决定是否值得用图像动态选专家生成追加提示。见表 2。 |
| 多模态学习 | 隐私保护 | [Towards Reasoning-Preserving Unlearning in Multimodal Large Language Models](cards.md#paper-reasoning-preserving-unlearning-leakage-retention) | 验证模型遗忘时可分别度量中间证据的残留披露和正常任务推理保留。见表 2。 |
| 计算机视觉 | 参数高效微调 | [TAS-LoRA: Transformer Architecture Search with Mixture-of-LoRA Experts](cards.md#paper-tas-lora-architecture-conditioned-supernet-experts) | 多子网共用权重产生特征坍塌时，可让架构配置选择小型适配器，并用不同子网预估和真实表现核对。见表 1、5。 |
| 多模态学习 | 推理策略 | [Geometrically-Constrained Agent for Spatial Reasoning](cards.md#paper-gca-formal-geometric-task-constraints) | 空间问答可先让模型把含混语言转换为可核验的几何任务约束，再执行工具，并检查错误是否源于约束生成。见表 2。 |
| 计算机视觉 | 三维重建与几何建模 | [Beyond Reassembly: Fractured Object Recovery with Missing Parts](cards.md#paper-fracture-recovery-joint-missing-part-token-modeling) | 组装任务中部件缺失时，可把缺失项设为可推断标记，与已见部件位姿共同更新，直接对照先装配再补全。见表 1、2。 |
| 计算机视觉 | 生成模型 | [Learning Hierarchical Hyperbolic Mixture Model for Part-aware 3D Generation](cards.md#paper-hierarchical-hyperbolic-mixture) | 有部件树的3D生成可比较欧氏与双曲潜表示，并分别测语义与几何误差。 |
| 计算机视觉 | 参数高效微调 | [Frame2Freq: Spectral Adapters for Fine-Grained Video Understanding](cards.md#paper-frame2freq) | 把图像骨干适配到视频时，测时间域适配器漏掉的中速运动，再决定用频带条件。 |
| 多模态学习 | 损失函数 | [More Than Meets the Eye: A Unified Image Fusion Framework via Semantic-Pixel Entropy Trade-off for Zero-Shot Generalization](cards.md#paper-semantic-pixel-entropy-fusion) | 图像融合可把保留像素信息和保持语义判定明确拆成目标，在未见融合类型上验收。 |
| 计算机视觉 | 鲁棒性 | [From Measurement to Mitigation: Quantifying and Reducing Identity Leakage in Image Representation Encoders with Linear Subspace Removal](cards.md#paper-identity-sanitization-projection) | 冻结表征要发布给检索系统时，可移除经评估的隐私相关线性子空间，并同时审计保留效用。 |
| 多模态学习 | 强化学习 | [PhyCritic: Multimodal Critic Models for Physical AI](cards.md#paper-phycritic) | 多模态评审可先独立生成参考结论，再评候选，并拆分领域技能训练与评审训练。 |
| 计算机视觉 | 推理加速 | [Scaling Parallel Sequence Models to Vision Foundation Models](cards.md#paper-compact-gspn) | 保留二维传播拓扑时，先降低传播状态宽度，再用跨算子蒸馏恢复表达。 |
| 计算机视觉 | 推理压缩 | [DA-VAE: Plug-in Latent Compression for Diffusion via Detail Alignment](cards.md#paper-da-vae) | 提高潜压缩率前先对齐已有扩散空间的结构，再补充细节维度。 |
| 机器人学 | 强化学习 | [IPR-1: Interactive Physical Reasoner](cards.md#paper-ipr-physcode) | 跨环境训练交互推理时，让策略和世界模型共用按物理效果定义的动作码。 |
| 计算机视觉 | 可解释性与诊断 | [Making Training-Free Diffusion Segmentors Scale with the Generative Power](cards.md#paper-diffusion-segmentor-attention-calibration) | 借扩散模型做开放分割前，先校准跨词元分数，再合并多层注意力。 |
| 多模态学习 | 自监督学习 | [InternVideo-Next: Towards World-Understanding Video Models](cards.md#paper-internvideo-next-epd) | 视频掩码预训练把预测器与像素解码器分离，另用语义对齐保留空间时间信息。 |
| 计算机视觉 | 损失函数与优化 | [VLIC: Vision-Language Models As Perceptual Judges for Human-Aligned Image Compression](cards.md#paper-vlic-pairwise-perceptual-judge) | 要训练匹配人类感知的图像压缩器时，可比较视觉语言模型的二选一判断与人工偏好，再直接用判断做后训练。 |
| 多模态学习 | 训练与数据策略 | [ReMatch: Boosting Representation through Matching for Multimodal Retrieval](cards.md#paper-rematch-generative-retrieval-supervision) | 学习检索向量时，让同一模型另做生成式成对相关性判断，以补足难负例。 |
| 计算机视觉 | 推理优化 | [VGG-T$^3$: Offline Feed-Forward 3D Reconstruction at Scale](cards.md#paper-vgg-t3-fixed-scene-memory) | 长多视角重建在测试时将可变长度键值蒸馏进定长场景 MLP，再用新图查询。 |
| 多模态学习 | 评估与诊断 | [Same Attention, Different Truths: Put Logit-Lens over Visual Attention to Detect and Mitigate LVLM Object Hallucination](cards.md#paper-llcc-attended-region-logit-lens-check) | 视觉幻觉诊断应核验高注意区域能否解码为输出对象，避免以注意力大小替代证据。见表 1。 |
| 计算机视觉 | 参数高效微调 | [Emergent Extreme-View Geometry in 3D Foundation Models](cards.md#paper-extreme-view-bias-only-geometric-alignment) | 视角重叠很低时可先探查预训练骨干的潜在几何信号，再比较仅调整骨干偏置能否改善相对位姿并保持深度。见表 1、4。 |
| 智能体 | 强化学习 | [HiconAgent: History Context-aware Policy Optimization for GUI Agents](cards.md#paper-hcpo-compressed-history-policy-alignment) | 界面历史太长时，可以让压缩策略对齐完整历史分支，并以可变历史长度训练，测成功率与计算。见表 4、5。 |
| 机器人学 | 规划与控制 | [CLaD: Planning with Grounded Foresight via Cross-Modal Latent Dynamics](cards.md#paper-clad-observable-anchoring-for-latent-foresight) | 把潜在未来接入动作策略时可加辅助观测重建，对照潜空间预测单独训练是否失去可用物理信号。见表 4。 |
| 多模态学习 | 损失与奖励 | [Rethinking BCE Loss for Multi-Label Image Recognition with Fine-Tuning](cards.md#paper-ccr-semantic-class-covariance-calibration) | 多标签模型微调可在匹配标签之外，约束类置信度的协方差与预训练文本几何一致。见表 2。 |
| 机器人学 | 三维重建与几何建模 | [Unblur-SLAM: Dense Neural SLAM for Blurry Inputs](cards.md#paper-unblur-slam-quality-triggered-formation-model) | 模糊感知可先做帧级恢复，只将仍不可靠的帧交给显式三维成像模型，比较轨迹漂移和恢复质量。见表 2、3。 |
| 生成模型 | 偏好优化 | [GDPO-SR: Group Direct Preference Optimization for One-Step Generative Image Super-Resolution](cards.md#paper-gdpo-sr-local-online-preference-for-one-step-restoration) | 一步图像恢复可在同一输入上采样候选做分组偏好，并对细节保真和感知评价分别检查。见表 5。 |
| 多模态学习 | 评测与诊断 | [SEA: Evaluating Sketch Abstraction Efficiency via Element-level Commonsense Visual Question Answering](cards.md#paper-sea-sketch-abstraction) | 评估视觉抽象或压缩时，把类别关键元素保留与表示成本放在同一协议。 |
| 多模态学习 | 强化学习 | [POCA: Pareto-Optimal Curriculum Alignment for Visual Text Generation](cards.md#paper-poca) | 多个目标冲突且提示预算有限时，以 Pareto 前沿筛掉被全面支配的候选，再按难度排序学习。 |
| 多模态学习 | 推理加速 | [AdaSpark: Adaptive Sparsity for Efficient Long-Video Understanding](cards.md#paper-adaspark) | 长视频想保留可回用信息时，用逐查询稀疏注意力和逐块稀疏 FFN 替代全局永久裁剪。 |
| 计算机视觉 | 模型分析 | [Solvability of the Viewing Graph Under the Affine Camera Model](cards.md#paper-affine-viewing-graph-solvability) | 多视重建前用线性可解性检验判断给定相机图是否足以确定相机。 |
| 多模态学习 | 输入表示 | [Direction-aware 3D Large Multimodal Models](cards.md#paper-direction-aware-3d-posealign) | 要回答左/右等方向问题，先把点云变换到提问者坐标，再与文本注入姿态对照。 |
| 多模态学习 | 参数高效微调 | [DeAR: Fine-Grained VLM Adaptation by Decomposing Attention Head Roles](cards.md#paper-dear-head-roles) | 适配预训练 VLM 时，按头识别概念与泛化功能再限制任务 token 的信息流。 |
| 多模态学习 | 推理策略 | [Thinking in Uncertainty: Mitigating Hallucinations in MLRMs with Latent Entropy-Aware Decoding](cards.md#paper-lead-entropy-decoding) | 在候选词概率分散的中间步保留连续语义混合，置信后恢复离散推理。 |
| 计算机视觉 | 损失函数与优化 | [Hierarchical Action Learning for Weakly-Supervised Action Segmentation](cards.md#paper-hal-slow-action-latents) | 弱监督视频分段可为高阶动作状态加稀疏跳转约束，同时保留下层快速视觉变化。 |
| 多模态学习 | 表示学习 | [ParaUni: Enhance Generation in Unified Multimodal Model with Reinforcement-driven Hierarchical Parallel Information Interaction](cards.md#paper-parauni-parallel-layer-conditioning) | 把视觉语言模型接到扩散生成器时，可同时从不同层提取细节与语义，并分别核验作用。 |
| 多模态学习 | 训练与数据策略 | [MuCo: Multi-turn Contrastive Learning for Multimodal Embedding Model](cards.md#paper-muco-multi-turn-contrastive) | 同图对应多个检索问题时，可在一个前向复用图像上下文，并分别读出相关对比嵌入。 |
| 计算机视觉 | 模型架构 | [Efficiency Follows Global-Local Decoupling](cards.md#paper-convneur-global-local-decoupling) | 高分辨率视觉骨干用少量全局记忆词元控制局部细节分支，避免全部图块都做全局交互。 |
| 智能体 | 评估与诊断 | [GUIDE: A Benchmark for Understanding and Assisting Users in Open-Ended GUI Tasks](cards.md#paper-guide-oracle-context-for-assistance-triage) | 协作型界面助手应分开测试行为状态识别与求助判断，再用真实状态和意图作对照定位瓶颈。见表 3。 |
| 多模态学习 | 三维重建与几何建模 | [Ov3R: Open-Vocabulary Semantic 3D Reconstruction from RGB Videos](cards.md#paper-ov3r-semantic-conditioning-before-reconstruction) | 语义三维重建可将语义特征提前注入几何预测，同时施加跨片段语义监督，比较简单后续贴标签。见表 5。 |
| 生成模型 | 生成建模 | [GeoRelight: Learning Joint Geometrical Relighting and Reconstruction with Flexible Multi-Modal Diffusion Transformers](cards.md#paper-georelight-joint-geometry-relighting-diffusion) | 几何和照明互补时，可比较把两者一起建模与只把几何作为外部条件，并分别考核两种输出。见表 2。 |
| 生成模型 | 模型效率 | [Yume1.5: A Text-Controlled Interactive World Generation Model](cards.md#paper-yume-temporal-spatial-channel-context-compression) | 互动世界生成可联合压缩历史的时间、空间与通道，先评测只压空间是否损害连续控制。见表 2。 |
| 机器人学 | 自监督学习 | [UST-Hand: An Uncertainty-aware Spatiotemporal Point Cloud Interaction Network for 3D Self-supervised Hand Pose Estimation](cards.md#paper-usthand-uncertainty-aware-pseudolabel-geometry) | 多视角三维姿态学习可把伪标签的不确定性建模成分布，检验换不同质量的伪标注后误差。见表 3。 |
| 机器人学 | 表征学习 | [MotionCrafter: Dense Geometry and Motion Reconstruction with a 4D VAE](cards.md#paper-motioncrafter-geometry-latent-normalization) | 迁移 RGB 视频生成器去做三维动态重建时，可单独校准几何与运动潜变量，再检验它们是否必须对齐 RGB 潜空间。见表 3。 |
| 多模态学习 | 损失函数 | [PowerCLIP: Powerset Alignment for Contrastive Pre-Training](cards.md#paper-powerclip) | 图文对齐从局部 patch 对词扩展到区域集合对短语时，可用线性代价近似所有子集。 |
| 多模态学习 | 强化学习 | [Monet: Reasoning in Latent Visual Space Beyond Image and Language](cards.md#paper-monet-visual-latent) | 让模型生成连续视觉中间态时，分别优化文本与潜视觉轨迹，检查常规 RL 是否只改善文本。 |
| 计算机视觉 | 表示学习 | [GLINT: Modeling Scene-Scale Transparency via Gaussian Radiance Transport](cards.md#paper-glint-radiance-transport) | 透明表面重建时，明确分开界面、反射和透射，而非用单高斯表示合成外观。 |
| 多模态学习 | 推理与规划 | [Copy-Transform-Paste: Zero-Shot Object-Object Alignment Guided by Vision-Language and Geometric Constraints](cards.md#paper-copy-transform-paste) | 零样本空间摆放时，先用语义定位正确关系，再逐步加强接触和防穿透。 |
| 多模态学习 | 推理策略 | [When to Think and When to Look: Uncertainty-Guided Lookback](cards.md#paper-uncertainty-guided-lookback) | 遇到视觉推理不确定时，比较回看原图与继续生成更长文本链。 |
| 机器人学 | 评测与分析 | [MangoBench: A Benchmark for Multi-Agent Goal-Conditioned Offline Reinforcement Learning](cards.md#paper-mangobench-multi-goal-offline) | 比较离线多智能体控制时，分开测未见组合目标、协作时间关系及集中训练的收益。 |
| 机器学习基础 | 训练与数据策略 | [FedRG: Unleashing the Representation Geometry for Federated Learning with Noisy Clients](cards.md#paper-fedrg-geometry-first-noisy-labels) | 客户端数据异质时，比较无标签表示几何和标注条件分布，再确定哪些样本需要校正。 |
| 计算机视觉 | 表示学习 | [MUFASA: A Multi-Layer Framework for Slot Attention](cards.md#paper-mufasa-multilayer-slots) | 对象中心学习可在多个视觉层分别提槽，再融合对象表示，不只从最后层读。 |
| 多模态学习 | 表示学习 | [RAMEN: Resolution-Adjustable Multimodal Encoder for Earth Observation](cards.md#paper-ramen-adjustable-output-resolution) | 异构传感编码时将输入分辨率和期望输出分辨率分别条件化，可按下游预算调节输出。 |
| 机器学习基础 | 模型架构 | [Designing to Forget: Deep Semi-parametric Models for Unlearning](cards.md#paper-semi-parametric-design-for-unlearning) | 预计需要逐样本删除时，把可移除训练信息放到显式查询组件，在部署时删除相关项。 |
| 机器人学 | 评测与分析 | [DriveCombo: Benchmarking Compositional Traffic Rule Reasoning in Autonomous Driving](cards.md#paper-drivecombo-compositional-rules) | 复杂规则评估应分开测试单条识别、多规则并发及冲突消解，并有纯文本对照。 |
| 生成模型 | 模型效率 | [Forecast the Principal, Stabilize the Residual: Subspace-Aware Feature Caching for Diffusion Transformers](cards.md#paper-svd-cache-forecast-principal-stabilize-residual) | 扩散缓存可将稳定主空间和波动残差分开处理，比较统一外推在相同计算量下的收益。见表 1。 |
| 智能体 | 检索增强 | [ViLoMem: Agentic Learner with Grow-and-Refine Multimodal Semantic Memory](cards.md#paper-vilomem-visual-and-logical-memory-streams) | 智能体经验可把视觉线索与推理规则分别存储、独立检索，并和重用完整历史轨迹比较。见表 2。 |
| 多模态学习 | 评估与诊断 | [Time Blindness: Why Video-Language Models Can't See What Humans Can?](cards.md#paper-spookybench-single-frame-uninformative-temporal-testing) | 要区分视频模型是否真正利用时序信息，可构造单帧无明确语义的对照，再验证外部时序特征能否补救。见表 5。 |
| 机器人学 | 主动学习 | [Learnability-Driven Submodular Optimization for Active Roadside 3D Detection](cards.md#paper-learnability-aware-active-geometry-labeling) | 标注预算有限时，可把单视角可学习性和模型不确定性分开，不把传感器本身不可观察的样本误选为高价值。见表 1。 |
| 生成模型 | 强化学习 | [Stepwise Credit Assignment for GRPO on Flow-Matching Models](cards.md#paper-stepwise-flow-grpo-reward-gain-credit) | 流模型强化学习可按相邻去噪步的奖励增量归因，比较最终奖励平均分配时的收敛。见表 1。 |
| 生成模型 | 参数高效微调 | [Tea-Adapter: Teacher Adapter for Efficient Conditional Generation](cards.md#paper-tea-adapter-small-to-large-control-distillation) | 可先让小模型学会新控制，再通过适配器把控制能力迁入冻结大模型，避免重训大生成器。见表 2。 |
| 机器学习 | 表征学习 | [Enhancing Visual Representation with Textual Semantics: Textual Semantics-Powered Prototypes for Heterogeneous Federated Learning](cards.md#paper-fedtsp-semantic-preserving-federated-prototypes) | 联邦特征原型可在提高类间可分性之外保存语义相近关系，比较语言编码器与提示是否弥合模态差。见表 2。 |
| 机器人学 | 表示学习 | [PointWorld: Scaling 3D World Models for In-The-Wild Robotic Manipulation](cards.md#paper-pointworld) | 跨机器人共享世界模型时，将低层控制编码成同一3D坐标系中的点运动。 |
| 多模态学习 | 训练策略 | [BAgger: Backwards Aggregation for Mitigating Drift in Autoregressive Video Diffusion Models](cards.md#paper-bagger-video) | 滚动生成的长程漂移可用模型自生成轨迹构造纠偏监督。 |
| 多模态学习 | 模型架构 | [TAG-MoE: Task-Aware Gating for Unified Generative Mixture-of-Experts](cards.md#paper-tag-moe) | 统一生成编辑模型发生任务冲突时，以描述任务意图的监督约束专家路由。 |
| 多模态学习 | 训练策略 | [Image-to-Point Cloud Feature Back-Projection for Multimodal Training of 3D Semantic Segmentation](cards.md#paper-ipfp-backprojection) | 部署缺某个传感器时，把训练辅助模态转为主模态表示，设计可关闭的数据路径。 |
| 计算机视觉 | 训练策略 | [GeoGuide: Hierarchical Geometric Guidance for Open-Vocabulary 3D Semantic Segmentation](cards.md#paper-geoguide-3d) | 用三维超点的不确定性筛选二维语义监督，再在实例层检查三维几何完整性。 |
| 多模态学习 | 测试时适应与推理 | [Memory Matters: Boosting Training-Free Zero-Shot Temporal Action Localization with a Learnable Lookup Table](cards.md#paper-llt-temporal-action) | 测试流中的共同动作可积累置信且多样的证据，当前视频只做残差调节。 |
| 计算机视觉 | 表示学习 | [Volumetric Functional Maps](cards.md#paper-volumetric-functional-maps) | 有内部体结构时，用体拉普拉斯谱进行对应，并独立测表面匹配是否受益。 |
| 多模态学习 | 损失函数与优化 | [Improved Mean Flows: On the Challenges of Fastforward Generative Models](cards.md#paper-imf-instantaneous-regression) | 一步流生成可改成由平均速度参数化的瞬时速度回归，并把引导系数当条件。 |
| 智能体 | 表示学习 | [Don't Show Pixels, Show Cues: Unlocking Visual Tool Reasoning in Language Models via Perception Programs](cards.md#paper-perception-programs-structured-cues) | 当视觉工具已有可靠信号时，用结构化关系和证据摘要代替把原始密集图直接交给语言模型。 |
| 多模态学习 | 评测与分析 | [FAVE: A Structured Benchmark for Fine-Grained Audio-Visual Temporal Evaluation in Multimodal LLMs](cards.md#paper-fave-av-temporal-diagnostics) | 评估视听模型时分别测音画同步、事件顺序和时段描述，避免总体视频问答掩盖定位错误。 |
| 机器人学 | 自监督学习 | [Bootstrap Dynamic-Aware 3D Visual Representation for Scalable Robot Learning](cards.md#paper-afro-latent-dynamics) | 预训练机器人三维表征时，用共享潜空间中的正逆动力代替显式三维重建，并用特征差防泄漏。 |
| 计算机视觉 | 模型架构 | [DAGE: Dual-Stream Architecture for Efficient and Fine-Grained Geometry Estimation](cards.md#paper-dage-dual-stream-geometry) | 跨视图几何用低分辨率流保持一致，高分辨率流只逐帧处理边缘，再做轻量跨注意力。 |
| 智能体 | 规划与决策 | [Proof-of-Perception: Certified Tool-Using Multimodal Reasoning with Compositional Conformal Guarantees](cards.md#paper-proof-of-perception-conformal-tools) | 工具推理图上给每步输出不确定集合，仅在集合无法支持结论时追加工具调用。 |
| 计算机视觉 | 三维重建与几何建模 | [2D-LFM: Lifting Foundation Model without 3D Supervision](cards.md#paper-2dlfm-layerwise-correspondence-position-encoding) | 只用二维关键点训练三维恢复时，可比较每层注入对应位置与只在输入注入的几何误差。见表 1。 |
| 计算机视觉 | 模型效率 | [Gradient Knows Best: Mixed-Precision Quantization via Gradient-Guided Bit Allocation for Super-Resolution](cards.md#paper-gradient-guided-weight-activation-bit-allocation) | 混合精度应分别测权重、激活位宽对损失的敏感度，而不只看静态张量统计。见表 4。 |
| 机器人学 | 表征学习 | [StaMo: Unsupervised Learning of Generalizable Robot Motion from Compact State Representation](cards.md#paper-stamo-compact-latent-state-and-motion-difference) | 操控可试用紧凑状态差表示运动，在同一 VLA 上区分普通图像特征、状态和运动条件的作用。见表 2。 |
| 多模态学习 | 评估与诊断 | [Mind the Way You Select Negative Texts: Pursuing the Distance Consistency in OOD Detection with VLMs](cards.md#paper-interneg-cross-modal-distance-consistency) | 选域外负文本时可使用图像到文本距离，与最终打分的几何一致，分别测试负文本筛选和额外负表示。见表 3。 |
| 计算机视觉 | 三维重建与几何建模 | [DualPrim: Compact 3D Reconstruction with Positive and Negative Primitives](cards.md#paper-dualprim-additive-subtractive-editable-reconstruction) | 需输出简洁可编辑几何时，可以同时使用加法和减法基元，并按形状误差与编辑性检查是否值得。见表 2。 |
| 计算机视觉 | 三维重建与几何建模 | [TagSplat: Topology-Aware Gaussian Splatting for Dynamic Mesh Modeling and Tracking](cards.md#paper-tagsplat-topology-preserving-dynamic-gaussians) | 动态图形要导出时序一致网格时，可在高斯致密化和删减中显式保存连接，再用跨帧约束衡量轨迹稳定性。见表 3、4。 |
| 智能体 | 评测与诊断 | [VS-Bench: Evaluating VLMs for Strategic Abilities in Multi-Agent Environments](cards.md#paper-vs-bench) | 多智能体能力应分别测看懂画面、预测他人动作和实际交互收益。 |
| 机器学习基础与统计 | 训练策略 | [Machine Unlearning via Adaptive Gradient Reweighting and Multi-stage Objective Optimization](cards.md#paper-adaptive-gradient-unlearning) | 遗忘任务应按样本记忆程度及邻近保留类风险加权，并分阶段优化两个目标。 |
| 多模态学习 | 评测与诊断 | [CURVE: A Benchmark for Cultural and Multilingual Long Video Reasoning](cards.md#paper-curve-evidence-graphs) | 文化视频问答可保留原语解释和证据关系，用逐步核查区分转述错误和地方知识缺失。 |
| 计算机视觉 | 数据增强 | [Diffusion-Based Native Adversarial Synthesis for Enhanced Medical Segmentation Generalization](cards.md#paper-synthetic-hard-example-utility) | 评价合成增强时独立比较原分布支持的难样本和仅有逼真外观的样本。 |
| 多模态学习 | 训练策略 | [Proxy-Tuning: Tailoring Multimodal Autoregressive Models for Subject-Driven Image Generation](cards.md#paper-proxy-tuning-ar) | 迁移生成任务能力时，可用另一类生成器作监督，并让学生与教师按相同提示比较。 |
| 多模态学习 | 表示学习 | [Missing No More: Dictionary-Guided Cross-Modal Image Fusion under Missing Infrared](cards.md#paper-dictionary-missing-infrared) | 缺模态时在共享字典系数域估计信息，并保留可见结构作为独立来源。 |
| 多模态学习 | 评测与诊断 | [TimeLens: Rethinking Video Temporal Grounding with Multimodal LLMs](cards.md#paper-timelens-benchmark-audit) | 训练前先抽检时间区间标注并重排基线，再在同数据条件下比较时间戳表示和训练方式。 |
| 多模态学习 | 训练与数据策略 | [PropFly: Learning to Propagate via On-the-Fly Supervision from Pre-trained Video Diffusion Models](cards.md#paper-propfly-online-paired-supervision) | 没配对编辑视频时，利用同一冻结扩散模型的不同条件强度构造共享运动结构的训练对。 |
| 多模态学习 | 表示学习 | [Qwen-Image-Layered: Towards Inherent Editability via Layer Decomposition](cards.md#paper-qwen-image-layered-rgba) | 编辑模型需保留其余内容时，直接生成可独立操控的可变数量 RGBA 图层。 |
| 计算机视觉 | 表示学习 | [LocateAnything3D: Vision-Language 3D Detection with Chain-of-Sight](cards.md#paper-locateanything3d-chain-of-sight) | 统一视觉语言检测可先输出二维证据，再分解三维中心、尺度和姿态，并检验近远顺序。 |
| 多模态学习 | 可解释性与诊断 | [Dictionary-Aligned Concept Control for Safeguarding Multimodal LLMs](cards.md#paper-daco-concept-aligned-safety) | 评估推理时安全调节时，同时测目标概念的可控性和非目标任务是否受损。 |
| 机器学习基础 | 训练与数据策略 | [Image-based Outlier Synthesis With Training Data](cards.md#paper-ascood-inlier-derived-outliers) | 没有外部异常样本时，训练检测器应检验从正常数据构造的反例是否覆盖细粒度和伪相关两种失败。 |
| 机器人学 | 规划与控制 | [AwareVLN: Reasoning with Self-awareness for Vision-Language Navigation](cards.md#paper-awarevln-progress-gated-reasoning) | 导航训练可对进度、偏航和停止分别提供监督，并比较只在关键节点推理与每步都推理。见表 3、4。 |
| 生成模型 | 推理策略 | [Thinking-while-Generating: Interleaving Textual Reasoning throughout Visual Generation](cards.md#paper-twig-interleaved-regional-reasoning) | 空间组合生成可在合成过程中交替写局部计划与复核已完成区域，避免把所有规划放在开头。见表 3。 |
| 机器人学 | 时序建模 | [Adaptive Spatial-Temporal Window: Unlocking the Potential of Event Cameras in Heterogeneous Velocity Scenarios](cards.md#paper-astw-local-event-time-window) | 同场景运动速度不同，可按图像局部密度设事件整合窗口，并对比全局时窗。见表 3。 |
| 生成模型 | 时序建模 | [Dual-Granularity Memory for Efficient Video Generation](cards.md#paper-dual-granularity-memory-video-generation) | 分块视频生成可分开维护块边界与跨段潜状态检索，并根据相关性设置回忆预算。见表 4。 |
| 计算机视觉 | 时序建模 | [RS-SSM: Refining Forgotten Specifics in State Space Model for Video Semantic Segmentation](cards.md#paper-rs-ssm-complementary-forgotten-detail) | 状态空间模型压缩后做像素任务时，可另建遗忘细节支路，比较双向常规模型是否足够。见表 3。 |
| 多模态学习 | 评估与诊断 | [VinQA: Visual Elements Interleaved Long-form Answer Generation for Real-World Multimodal Document QA](cards.md#paper-vinqa-page-versus-element-citation-encoding) | 文档答案需可核查图表时，可对照整页带框与各模态单独编码，检查引用与答复质量是否同步改善。见表 3。 |
| 机器人学 | 检索增强 | [RAG-TP: A General Framework for Vehicle Trajectory Prediction via Retrieval-Augmented Generation](cards.md#paper-rag-tp-retrieved-trajectory-experts) | 轨迹预测可按当前场景检索相似拓扑和历史运动，再比较直接融合与对检索候选加权。见表 2。 |
| 多模态学习 | 强化学习 | [Re-Align: Structured Reasoning-guided Alignment for In-Context Image Generation and Editing](cards.md#paper-realign-in-context-editing) | 图文交织编辑先区分要实现的语义目标与各参考图对应关系，再单测生成是否遵守。 |
| 计算机视觉 | 输入表示 | [A Bit is All You Need! Efficient Video Capture via Single Bit Imaging](cards.md#paper-one-bit-computational-video) | 高带宽传感可比较时变阈值量化与同预算固定阈值，然后用时间冗余恢复。 |
| 多模态学习 | 模型架构 | [PositionIC: Unified Position and Identity Consistency for Image Customization](cards.md#paper-positionic) | 多主体定制可改用带可见性约束的注意力，分别验位置和身份，不只验全局图像相似。 |
| 多模态学习 | 训练策略 | [CLIP Is Shortsighted: Paying Attention Beyond the First Sentence](cards.md#paper-debias-clip) | 长描述训练先审计首句是否成为捷径，考虑移除摘要、随机采样句子及按位置补齐。 |
| 计算机视觉 | 训练策略 | [Unlocking the Power of Critical Factors for 3D Visual Geometry Estimation](cards.md#paper-carve-geometry-ablation) | 三维时序模型可同时监督序列与帧级对齐，单独比较局部和置信度损失是否帮助。 |
| 计算机视觉 | 数据增强 | [No Need For Real Anomaly: MLLM Empowered Zero-Shot Video Anomaly Detection](cards.md#paper-lavida-pseudo-anomalies) | 稀有异常可以先在正常视频上构造语义伪异常，并在全新基准测是否能识别未见类型。 |
| 多模态学习 | 输入表示 | [LottieGPT: Tokenizing Vector Animation for Autoregressive Generation](cards.md#paper-lottiegpt-native-animation) | 生成可编辑动态内容时直接预测图层与关键帧参数，评估文本与图像条件的差异。 |
| 计算机视觉 | 表示学习 | [Matching Every Pair to Track Every Point: PairFormer for All-Pairs Tracking and Video Trajectory Fields](cards.md#paper-pairformer-all-pairs-tracking) | 多个查询要复用同一视频运动时，直接输出全帧对位移和可见性场。 |
| 计算机视觉 | 微调与适配 | [Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling](cards.md#paper-upsample-anything) | 将低分辨率特征升到像素时，先试逐图拟合可借原图边界的各向异性核。 |
| 计算机视觉 | 推理优化 | [Sparsity-Aware Voxel Attention and Foreground Modulation for 3D Semantic Scene Completion](cards.md#paper-voxsamnet-empty-voxel-shortcut) | 占据预测的空体素极多时，让空区共享旁路，把可变形注意力留给可能占据的位置。 |
| 机器人学 | 微调与适配 | [Exploring Conditions for Diffusion Models in Robotic Control](cards.md#paper-orca-task-adaptive-diffusion-features) | 把冻结生成模型当机器人视觉编码器时，分开测试任务可学提示和当前帧视觉提示。 |
| 多模态学习 | 模型架构 | [TV2TV: A Unified Framework for Interleaved Language and Video Generation](cards.md#paper-tv2tv-interleaved-video-language) | 生成长叙事可让语言计划和像素生成交织，推理期间也允许更新计划。 |
| 多模态学习 | 推理优化 | [LESA: Learnable Stage-Aware Predictors for Diffusion Model Acceleration](cards.md#paper-lesa-stage-aware-forecasting) | 加速扩散缓存时可按噪声阶段分别学习特征预测器，避免用单个外推规则。 |
| 表征学习 | 训练策略 | [Residual Connections Harm Generative Representation Learning](cards.md#paper-decayed-identity-shortcuts-semantic-representations) | 自编码重建表现好但语义探针弱时，可调低残差块内部恒等支路的贡献，分别测重建与迁移。见表 1、4。 |
| 多模态学习 | 主动学习 | [Learning What Matters: Prioritized Concept Learning via Relative Error-driven Sample Selection](cards.md#paper-progress-relative-error-curriculum-selection) | 指令微调可按当前技能的相对误差更新数据选择，避免固定选择最易或最难样本。见表 3。 |
| 多模态学习 | 强化学习 | [Learning to Focus and Precise Cropping:A Reinforcement Learning Framework with Information Gaps and Grounding Loss for MLLMs](cards.md#paper-information-gap-crop-dependency-evaluation) | 视觉裁剪训练可检查将裁剪替换为真实区域与噪声时答案的变化，验证模型是否真正使用了工具。见表 4、5。 |
| 生成模型 | 模型效率 | [SeaCache: Spectral-Evolution-Aware Cache for Accelerating Diffusion Models](cards.md#paper-seacache-spectrum-aware-refresh-decision) | 选择缓存刷新时可比较原始特征差和随去噪阶段过滤频谱后的差，避免噪声主导判断。见表 1。 |
| 多模态学习 | 三维重建与几何建模 | [LangRef3DGS: Natural Language-Guided 3D Referential Segmentation from Partial Observations via 3D Gaussian Splatting](cards.md#paper-langref3dgs-category-discovery-under-partial-views) | 三维语言指代缺少视角时，可比较适应性类别发现和抑制冗余梯度，以及两者在移除视角后的增量。见表 4。 |
| 计算机视觉 | 表征学习 | [RawMetaDiff: Unlocking Extreme Darkness from Dual-Exposure RAW with Meta-Guided Diffusion](cards.md#paper-rawmetadiff-metadata-conditioned-asymmetric-observations) | 融合不同曝光传感器读数时可显式给出成像元数据，分别检验配准不确定性和颜色恢复。见表 3。 |
| 多模态学习 | 模型架构 | [Premier: Personalized Preference Modulation with Learnable User Embedding in Text-to-Image Generation](cards.md#paper-premier-user-preference) | 有少量新用户反馈时，可先用已有用户嵌入的组合初始化偏好，再按一致性审计。 |
| 计算机视觉 | 模型架构 | [NimbusGS: Unified 3D Scene Reconstruction under Hybrid Weather](cards.md#paper-nimbusgs-hybrid-weather) | 多视重建把视角共享的衰减与单视图瞬变干扰分支建模，并分别监督几何。 |
| 计算机视觉 | 输入表示 | [Computer Vision with a Superpixelation Camera](cards.md#paper-supercam) | 传感器带宽不足可保留空间自适应区域统计，并以同内存预算检验下游效用。 |
| 机器学习基础与统计 | 推理压缩 | [DuetMerging: Synergizing Dynamic and Static Strategies for Mitigating Task Interference in Model Merging](cards.md#paper-duetmerging) | 合并多个任务模型时，先在共享张量内分解共用与特异方向，再按激活稀疏化。 |
| 多模态学习 | 推理策略 | [ViRC: Enhancing Visual Interleaved Mathematical CoT with Reason Chunking](cards.md#paper-virc) | 视觉数学题可按可校验的中间命题分块，并在块间主动追加图面证据。 |
| 计算机视觉 | 强化学习 | [FinPercep-RM: A Fine-grained Reward Model and Co-evolutionary Curriculum for RL-based Real-world Super-Resolution](cards.md#paper-finpercep-rm) | 当全局视觉评分会奖励局部伪影时，加入可定位局部缺陷的奖励，并分阶段训练。 |
| 智能体 | 强化学习 | [ARM-Thinker: Reinforcing Multimodal Generative Reward Models with Agentic Tool Use and Visual Reasoning](cards.md#paper-arm-thinker-tool-grounded-reward) | 训练多模态奖励模型时，把何时调用视觉工具及如何用证据判断作为优化目标。 |
| 多模态学习 | 推理优化 | [Denoising as Path Planning: Training-Free Acceleration of Diffusion Models with DPCache](cards.md#paper-dpcache-path-aware-scheduling) | 扩散缓存按上次重算点估计跳步代价并做全局调度，避免只看当前步。 |
| 机器学习基础 | 表示学习 | [GPFlow: Gaussian Prototype Probability Flow for Unsupervised Multi-Modal Anomaly Detection](cards.md#paper-gpflow-gaussian-prototypes) | 少样本正常特征建模时，用带协方差的高斯原型替代点原型，保留方向相关的正常变化。 |
| 多模态学习 | 表示学习 | [Machine Mental Imagery: Empower Multimodal Reasoning with Latent Visual Tokens](cards.md#paper-mirage-latent-visual-thought) | 视觉规划需要内部空间表示时，让模型交织隐视觉词元和语言词元，无需生成像素供自己读取。 |
| 机器学习基础 | 评测与分析 | [InTrain: Intrinsic Trainability for Zero-Cost Neural Architecture Search](cards.md#paper-intrain-zero-cost-nas) | 零成本比较架构时同时检测激活有效维度与梯度传播，而非单用容量或单用梯度。 |
| 多模态学习 | 知识蒸馏 | [Flow Map Distillation Without Data](cards.md#paper-data-free-flow-map-distillation) | 蒸馏生成流时可直接从教师原生先验采轨迹，避免外部数据与教师支持集错配。 |
| 机器学习 | 表征学习 | [Cluster-aware Anchor Learning for Multi-View Clustering](cards.md#paper-cal-adaptive-cluster-anchor-budget) | 多视图聚类的锚点可按簇分配，让复杂簇保留更多锚点。见表 3。 |
| 计算机视觉 | 训练策略 | [Learning from Synthetic Data via Provenance-Based Input Gradient Guidance](cards.md#paper-synthetic-provenance-gradient-guidance) | 合成数据时可用生成来源标注直接约束模型的输入梯度，检验模型是否仍依赖背景。见表 3。 |
| 机器人学 | 规划与控制 | [MAGICIAN: Efficient Long-Term Planning with Imagined Gaussians for Active Mapping](cards.md#paper-magician-long-horizon-coverage-planning) | 主动建图可基于不完整场景预测预期表面覆盖，并对照树搜索与每步贪心。见表 2。 |
| 机器人学 | 规划与控制 | [ForeAct: Steering Your VLA with Efficient Visual Foresight Planning](cards.md#paper-foreact-goal-image-and-subtask-conditioning) | 语言策略需要目标定位时，可比较目标图像和直接提供空间文本，并保留分步子任务。见表 4。 |
| 生成模型 | 模型效率 | [RAPID: Reusing Attention Sparsity with Inter-step Adaptation for Efficient Video Diffusion](cards.md#paper-rapid-early-attention-mask-reuse) | 视频去噪可早期估计注意力块并在后续步复用，随阶段调节密度，避免反复筛块。见表 2。 |
| 机器人学 | 表征学习 | [C-LaV: Conditional Latent Velocity Field Denoising for Weather-Robust LiDAR Place Recognition](cards.md#paper-clav-weather-invariant-latent-place-recognition) | 恶劣天气定位可先恢复冻结编码器的清晰域潜表示，再比较直接检索和不同去噪目标。见表 3。 |
| 多模态学习 | 训练策略 | [Uncertainty-Aware Knowledge Distillation for Multimodal Large Language Models](cards.md#paper-beta-kd) | 蒸馏时按样本比较标签和教师可靠性，避免固定权重。 |
| 多模态学习 | 推理策略 | [Adaptive Auxiliary Prompt Blending for Target-Faithful Diffusion Generation](cards.md#paper-adaptive-auxiliary-prompt-blending) | 低密度概念生成可用辅助语义支持，再按去噪步调节锚与目标的混合。 |
| 计算机视觉 | 优化策略 | [Fast Markov Random Field Optimisation for Topologically Noisy 3D Shape Matching](cards.md#paper-affine-alpha-expansion-shape) | 有拓扑噪声时把表面对应改写为离散邻域一致性，保持近似保证同时利用标签结构加速。 |
| 计算机视觉 | 生成模型 | [DVAR: Dynamic Visual Autoregressive Modeling for Image Super-Resolution](cards.md#paper-dvar-canonical-scale) | 多目标分辨率训练可学习相对尺度进程，再按目标尺寸呼叫同模型。 |
| 智能体 | 强化学习 | [GUI-SAGE: Enhancing GUI Automation with Self-Explanatory Learning](cards.md#paper-gui-sage) | 探索完全无正确动作时，以真动作提示诱导模型自己解释，再用信心和成功联合归因。 |
| 智能体 | 自动化工作流 | [3DrawAgent: Teaching LLM to Draw in 3D with Early Contrastive Experience](cards.md#paper-3drawagent) | 不方便微调工具代理时，可保存相对更好和更差的产物对，更新经验再生成。 |
| 多模态学习 | 损失函数与优化 | [UniFusion: A Unified Image Fusion Framework with Robust Representation and Source-Aware Preservation](cards.md#paper-unifusion-source-preserving) | 让融合输出通过各来源重建约束保持信息，同时用双层训练平衡融合及重建。 |
| 计算机视觉 | 推理优化 | [Layered 4D-Rotor Gaussian Splatting: A Compressed Representation for Long Dynamic Scenes](cards.md#paper-l4drotorgs-temporal-buckets) | 长动态场景按图元寿命建立时间桶，渲染只读当前活跃集合并分别量化。 |
| 多模态学习 | 推理优化 | [Just-in-Time: Training-Free Spatial Acceleration for Diffusion Transformers](cards.md#paper-jit-spatial-diffusion-anchors) | 扩散早期从稀疏空间锚点更新全局结构，按需要插入细节词元。 |
| 计算机视觉 | 知识蒸馏 | [SigLino: Efficient Multi-Teacher Distillation for Agglomerative Vision Foundation Models](cards.md#paper-siglino-asymmetric-relations) | 多视觉教师几何不同，先蒸馏各自关系结构，配合等词元预算训练。 |
| 多模态学习 | 推理优化 | [First Logit Boosting: Visual Grounding Method to Mitigate Object Hallucination in Large Vision-Language Models](cards.md#paper-first-logit-boosting) | 开放式回答随长度丢失视觉信息时，可对照将早期视觉条件的分数作为后续解码先验。 |
| 多模态学习 | 表示学习 | [Gravitation-Driven Semantic Alignment for Text Video Retrieval](cards.md#paper-gravialign-probabilistic-retrieval) | 一对多语义检索可同时要求分布中心接近和支持重叠，任一不足都降低匹配。 |
| 生成模型 | 生成建模 | [FlexTraj: Image-to-Video Generation with Flexible Point Trajectory Control](cards.md#paper-flextraj-trajectory-sequence-conditioning) | 图像到视频的轨迹控制可把稀疏与稠密轨迹统一为可对应点序列，再与独立条件网络对照。见表 3。 |
| 机器学习 | 评估与诊断 | [Enhancing Accuracy of Uncertainty Estimation in Appearance-based Gaze Tracking with Probabilistic Evaluation and Calibration](cards.md#paper-gaze-conditional-distribution-coverage-calibration) | 连续回归的置信度遇到域漂移时，可用少量数据校准误差条件分布，并检查名义覆盖是否达标。见表 2。 |
| 多模态学习 | 推理策略 | [Seeing is Improving: Visual Feedback for Iterative Text Layout Refinement](cards.md#paper-vflm-render-feedback-layout-refinement) | 生成可渲染布局时，可让模型看见自己的渲染结果后再修订，并分开测可读性和排版。见表 3。 |
| 机器学习 | 表征学习 | [Hier-COS: Making Deep Features Hierarchy-aware via Composition of Orthogonal Subspaces](cards.md#paper-hiercos-orthogonal-feature-hierarchy) | 类别层次应同时约束表示和评估，可用正交子空间组合保障粗到细关系，再单测层级一致性。见表 4。 |
| 生成模型 | 推理策略 | [DBMSolver: A Training-free Diffusion Bridge Sampler for High-Quality Image-to-Image Translation](cards.md#paper-dbmsolver-semilinear-exponential-bridge-sampling) | 扩散桥少步推理时可利用半线性结构分别积分线性项和非线性项，以相同函数评估预算对照。见表 2。 |
| 计算机视觉 | 模型效率 | [UETrack: A Unified and Efficient Framework for Single Object Tracking](cards.md#paper-uetrack-token-pooled-multimodal-tracking) | 资源受限追踪可在共享模型内用池化标记路由专家，而不是为每种模态部署独立骨干，并实测多种设备。见表 3。 |
| 机器人学 | 推理压缩 | [CoLC: Communication-Efficient Collaborative Perception with LiDAR Completion](cards.md#paper-colc-lidar-completion) | 协作感知可传稀疏关键测量，在接收端用密集观测作为训练目标补全。 |
| 计算机视觉 | 表示学习 | [Consistent Instance Field for Dynamic Scene Understanding](cards.md#paper-consistent-instance-field) | 持续对象记忆把占用和存在条件下的身份分别表示，避免不可见等于身份消失。 |
| 计算机视觉 | 推理压缩 | [Multinex: Lightweight Low-light Image Enhancement via Multi-prior Retinex](cards.md#paper-multinex) | 部署极小视觉网络时，先用解析先验提供互补通道，由网络学习少量残差。 |
| 多模态学习 | 表示学习 | [HSI-GPT2: A Dual-Granularity Large Motion Reasoning Model with Diffusion Refinement for Human-Scene Interaction](cards.md#paper-hsi-gpt2-dual-motion-token) | 统一动作理解与生成时，可分别编码与文字对齐的语义层和构成连续动作的细节层。 |
| 机器学习基础与统计 | 损失函数 | [Streamlined Knowledge Distillation](cards.md#paper-streamlined-kd) | 蒸馏可把实例分布和跨类别方向相关性拆开，避免多套重复目标。 |
| 计算机视觉 | 训练策略 | [Closed-Form Concept Erasure via Double Projections](cards.md#paper-double-projection-concept-erasure) | 概念删除时定义需保留的方向，并按目标删除率和邻近概念效用分别评估。 |
| 机器学习基础 | 迁移与泛化 | [Prototype-based Causal Intervention for Multi-Label Image Classification](cards.md#paper-proci-context-prototypes) | 多标签分类缺少对象框时，可用动态的类条件背景原型估计样本级共现偏差。 |
| 多模态学习 | 训练与数据策略 | [BriMA: Bridged Modality Adaptation for Multi-Modal Continual Action Quality Assessment](cards.md#paper-brima-modality-aware-replay) | 模态会中途异步缺失时，将补全记忆与按失真和漂移挑选的回放联合考虑。 |
| 机器学习基础 | 迁移与泛化 | [HFedATM: Hierarchical Federated Domain Generalization via Optimal Transport and Regularized Mean Aggregation](cards.md#paper-hfedatm-hierarchical-aggregation) | 多个联邦站点聚合时，先对齐卷积滤波器，再用结构相关的线性聚合替代逐权重平均。 |
| 多模态学习 | 推理优化 | [Scaling the Long Video Understanding of Multimodal Large Language Models via Visual Memory Mechanism](cards.md#paper-flexmem-visual-kv-memory) | 视频问答可分开设计视觉键值压缩写入和按查询或流任务读取。 |
| 计算机视觉 | 评测与分析 | [Learning 3D Shape Fidelity Metric from Real-world Distortions](cards.md#paper-locase-real-shape-fidelity) | 三维质量评价可以真实重建错误和人评训练局部连接指标，补充 Chamfer 距离。 |
| 计算机视觉 | 持续学习 | [Hyperbolic Prototype Learning with Uncertainty-Aware Consistency for Continual Test-Time Segmentation](cards.md#paper-hyperprotoseg-hyperbolic-test-time-class-prototypes) | 持续测试时分割可比较双曲与欧氏类别原型，再检验几何改变是否减少伪监督误差累积。见表 2。 |
| 机器人学 | 规划与控制 | [Learning to Assist: Physics-Grounded Human-Human Control via Multi-Agent Reinforcement Learning](cards.md#paper-assistive-control-contact-aware-reference-retargeting) | 需要身体接触的协作可动态改写参照轨迹，并在接触持续和伙伴运动较大时分别测是否有用。见第 4 节。 |
| 机器人学 | 评估与诊断 | [SAGE: Scalable Agentic 3D Scene Generation for Embodied AI](cards.md#paper-sage-visual-and-physics-critic-separation) | 生成仿真场景时可为视觉语义和物理稳定性安排独立评估，并检验二者的联合反馈。见表 3。 |
| 机器人学 | 检索增强 | [Multi-Scale Gaussian-Language Map for Zero-shot Embodied Navigation and Reasoning](cards.md#paper-glmap-instance-region-memory-navigation) | 开放词汇导航可同时保留对象与区域语义，并用共同几何坐标同时返回文本和可渲染视图。见表 1。 |
| 表征学习 | 自监督学习 | [Can You Learn to See Without Images? Procedural Warm-Up for Vision Transformers](cards.md#paper-procedural-nonvisual-warmup-for-vit) | 可用非视觉程序序列热启动 Transformer，再与合成图像初始化及同架构随机初始化比较样本效率。见表 2、3。 |
| 计算机视觉 | 三维重建与几何建模 | [LagerNVS: Latent Geometry for Fully Neural Real-time Novel View Synthesis](cards.md#paper-lagernvs-three-dimensional-pretraining-and-direct-rendering) | 快速新视角推理可以复用显式三维预训练特征，却让轻量解码器直接渲染，并验证冻结与端到端适配。见表 2。 |
| 计算机视觉 | 损失函数 | [Structure-Aware Representation Distillation for Tiny-Dense Object Segmentation](cards.md#paper-sard-structure-distillation) | 给密集小物体蒸馏时，用结构重要性给特征对齐分配预算。 |
| 计算机视觉 | 生成模型 | [Linear Image Generation by Synthesizing Exposure Brackets](cards.md#paper-linear-exposure-bracket-generation) | 需物理可编辑的图像时，先联合合成曝光包围与辐射尺度，再融合到线性空间。 |
| 智能体 | 强化学习 | [SpaceTools: Tool-Augmented Spatial Reasoning via Double Interactive RL](cards.md#paper-spacetools-dirl) | 多视觉工具探索可先训练会探索的教师，再用其轨迹初始化通用策略并做第二次交互优化。 |
| 多模态学习 | 测试时适应与推理 | [Adapting Point Cloud Analysis via Multimodal Bayesian Distribution Learning](cards.md#paper-bayesmm) | 在线缓存不足时可维护每类的分布统计，再以贝叶斯方式融合文本先验和视觉观测。 |
| 计算机视觉 | 表示学习 | [Part$^{2}$GS: Part-aware Modeling of Articulated Objects using 3D Gaussian Splatting](cards.md#paper-part2gs) | 建可关节运动的数字孪生时，给高斯附加部件身份，并在统一姿态中约束接触及运动。 |
| 多模态学习 | 训练策略 | [Anchor-Guided Gradient Alignment for Incomplete Multimodal Learning](cards.md#paper-anga-incomplete-multimodal) | 模态补全数据很多时，以真实完整样本及少数可信补全样本的梯度作训练锚。 |
| 机器学习基础与统计 | 损失函数 | [Stake the Points: Structure-Faithful Instance Unlearning](cards.md#paper-structure-faithful-unlearning) | 遗忘实例后要保留其他实例间的语义组织，可用描述生成的锚点辅助验证。 |
| 机器学习基础 | 损失函数与优化 | [Understanding and Enforcing Weight Disentanglement in Task Arithmetic](cards.md#paper-orthoreg-task-vector-disentanglement) | 训练可组合任务向量时，先测向量干扰，再对任务增量施加正交正则。 |
| 机器学习基础 | 微调与适配 | [Back to Source: Open-Set Continual Test-Time Adaptation via Domain Compensation](cards.md#paper-doco-open-set-domain-compensation) | 连续开放集测试适配先用可能是已知类的样本估域偏差，再以同一补偿测试可疑样本的新颖性。 |
| 计算机视觉 | 训练与数据策略 | [HAD: Hallucination-Aware Diffusion Priors for 3D Reconstruction](cards.md#paper-had-multiview-hallucination-masks) | 用生成视图训练三维模型时，按像素对生成内容做几何可信度掩码，并聚合不同输入视图的证据。 |
| 计算机视觉 | 微调与适配 | [Degradation-Consistent Test-Time Adaptation for All-in-One Image Restoration](cards.md#paper-dctta-redegradation-consistency) | 无源数据的恢复适配用同一场景的多种再退化训练一致性，并只更新对退化敏感的参数。 |
| 计算机视觉 | 损失函数与优化 | [ManifoldNeuS: Manifold-aware View Optimizability for Pose-Free Neural Surface Reconstruction](cards.md#paper-manifoldneus-view-optimizability) | 联合估位姿和表面时，为视图调度同时看当前可拟合性与补足未来表面覆盖的价值。 |
| 机器学习 | 隐私保护 | [Unlearning without Forgetting: Securely Removing Targeted Concepts from Large-Scale Vision-Language Open-Vocabulary Detectors](cards.md#paper-safedetect-retained-subspace-unlearning) | 移除目标概念时可把保留语义作为更新空间的约束，并分别评估忘记、保留与零样本能力。见表 2、3。 |
| 多模态学习 | 三维重建与几何建模 | [PE3R: Perception-Efficient 3D Reconstruction](cards.md#paper-pe3r-multilevel-crossview-semantic-disambiguation) | 二维语义监督回投三维时可以分开消除多粒度与跨视角歧义，再检查语义分割质量。见表 5。 |
| 多模态学习 | 评估与诊断 | [VKG-QA: Visual Knowledge Graph-based Question Answer for Large Multimodal Models](cards.md#paper-vkgqa-rendered-knowledge-graph-reasoning) | 结构化问答可同时测试图像和关系线性化两种输入，逐一比较连通、环和多跳任务。见表 2。 |
| 生成模型 | 模型效率 | [AdaCluster: Adaptive Query-Key Clustering for Sparse Attention in Video Generation](cards.md#paper-adacluster-asymmetric-query-key-clustering) | 注意力压缩可以分别依角度和距离聚类查询与键，并按层调整容量。见表 3。 |
| 生成模型 | 模型蒸馏 | [InstantViR: Real-Time Video Inverse Problem Solver with Distilled Diffusion Prior](cards.md#paper-instantvir-bidirectional-prior-causal-restoration) | 实时视频恢复可把双向教师的视频先验蒸馏给只读过去帧的学生，分别考核时序质量和帧率。见表 1。 |
| 计算机视觉 | 三维重建与几何建模 | [TWINGS: Thin Plate Splines Warp-aligned Initialization for Sparse-View Gaussian Splatting](cards.md#paper-twings-nonrigid-depth-anchor-initialization) | 稀疏新视角可先用可靠三角化点校正密集单目深度，而非直接拿深度点作为高斯初值。见表 1。 |
| 计算机视觉 | 损失函数 | [CUE: Concept-Aware Multi-Label Expansion to Mitigate Concept Confusion in Long-Tailed Learning](cards.md#paper-cue-long-tail) | 长尾微调时保留预训练表征中的相关类局部邻域，让监督允许共享概念。 |
| 多模态学习 | 参数高效微调 | [LOREAL: Mitigating Low-Resolution Challenges in Vision-Language Models with Attribute-driven Prompt Self-Distillation](cards.md#paper-loreal-low-resolution) | 部署分辨率受限时，用同一内容的异分辨率学生互蒸馏，并检查文字属性是否仍可观测。 |
| 计算机视觉 | 生成模型 | [VOSR: A Vision-Only Generative Model for Image Super-Resolution](cards.md#paper-vosr-restoration-guidance) | 对恢复任务设计辅助引导分支时，保留弱观测结构而只移除高层语义。 |
| 计算机视觉 | 输入表示 | [Cov2Pose: Leveraging Spatial Covariance for Direct Manifold-aware 6-DoF Object Pose Estimation](cards.md#paper-cov2pose) | 直接回归位姿可保留空间二阶统计，并选连续、可做几何运算的输出表示。 |
| 计算机视觉 | 测试时适应与推理 | [Mixture of Prototypes for Test-time Adaptive Segmentation](cards.md#paper-mixture-of-prototypes-tta) | 域偏移时每类保留多原型并逐样本加权，而非用一个全局中心。 |
| 机器学习基础与统计 | 参数高效微调 | [OrthoFuse: Training-free Riemannian Fusion of Orthogonal Style-Concept Adapters for Diffusion Models](cards.md#paper-orthofuse) | 合并正交适配器时在结构允许的流形内插值，并核查融合后谱。 |
| 计算机视觉 | 推理压缩 | [Generative Neural Video Compression via Video Diffusion Prior](cards.md#paper-gnvc-video-diffusion) | 压缩后生成式增强可从已解码潜变量开始，按序列而非逐帧修正。 |
| 机器学习基础 | 评测与分析 | [Conditional Factuality Controlled LLMs with Generalization Certificates via Conformal Sampling](cards.md#paper-cfc-conditional-conformal-sampling) | 模型假事实率随请求类型变化时，用特征条件阈值替代统一阈值，输出经过覆盖校准的答案集合。 |
| 多模态学习 | 强化学习 | [Stable and Efficient Single-Rollout RL for Multimodal Reasoning](cards.md#paper-mssr-entropy-advantage) | 单轨迹可验证奖励训练若不稳，可按熵约束优势幅度，再比较相同算力下的多轨迹方案。 |
| 多模态学习 | 可解释性与诊断 | [Understanding and Mitigating Hallucinations in Multimodal Chain-of-Thought Models](cards.md#paper-multimodal-cot-divergent-hallucination) | 检测多模态长推理幻觉时，把跨线索联想步骤与其他步骤分开核查，避免对全链统一干预。 |
| 计算机视觉 | 评测与分析 | [BlackMirror: Black-Box Backdoor Detection for Text-to-Image Models via Instruction-Response Deviation](cards.md#paper-blackmirror-instruction-response-audit) | 黑盒生成服务防御审计应比较指令偏离是否在多种情形保持，而非只看整图相似。 |
| 机器人学 | 评测与分析 | [From Where Things Are to What They Are For: Benchmarking Spatial-Functional Intelligence in Multimodal LLMs](cards.md#paper-sfi-bench-spatial-functional-diagnostics) | 评估室内代理同时测试空间布局与物体用途，并加打乱帧和描述输入以诊断缺口。 |
| 多模态学习 | 损失函数与优化 | [Phrase-Grounding-Aware Supervised Fine-Tuning for Chart Recognition via Side-Masked Attention](cards.md#paper-smam-phrase-grounded-logits) | 训练视觉语言生成时，可在同层让短语只读对应图块的辅助 logit，再与全图生成目标联训。 |
| 计算机视觉 | 三维重建与几何建模 | [SparseSplat: Towards Applicable Feed-Forward 3D Gaussian Splatting with Pixel-Unaligned Prediction](cards.md#paper-sparsesplat-entropy-based-primitive-allocation) | 紧凑三维重建可按局部内容熵分配基元，直接比较均匀、边缘和熵采样。见表 3。 |
| 生成模型 | 推理策略 | [Taming Video Models for 3D and 4D Generation via Zero-Shot Camera Control](cards.md#paper-worldforge-intrastep-camera-motion-refinement) | 免训练相机控制可在单步内部校正视图运动，同时分开保持场景自身动态。见表 3。 |
| 机器学习 | 自监督学习 | [Learning Eigenstructures of Unstructured Data Manifolds](cards.md#paper-spectral-basis-learning-via-probe-reconstruction) | 无显式网格时可用一组探测函数重建误差学习谱结构，并对照不同截断阶数。见表 1。 |
| 生成模型 | 模型效率 | [DPAR: Dynamic Patchification for Efficient Autoregressive Visual Generation](cards.md#paper-dpar-entropy-dynamic-visual-token-patches) | 自回归图像生成可用标记预测熵决定可合并跨度，并限制连续块长度与行边缘。见表 3。 |
| 计算机视觉 | 自监督学习 | [TrackMAE: Video Representation Learning via Track Mask and Predict](cards.md#paper-trackmae-trajectory-targets-for-masked-video-modeling) | 遮罩视频预训练可引入点轨迹重建与运动感知遮罩，分别测动作线索收益。见表 4。 |
| 机器学习 | 持续学习 | [Spectral Mixture-of-Experts for Continual Learning](cards.md#paper-spectral-moe-disjoint-expert-updates) | 增量训练的专家可分配互不重叠的频域参数空间，并单独跟踪路由漂移和专家干扰。见表 4。 |
| 计算机视觉 | 表示学习 | [Learning Convex Decomposition via Feature Fields](cards.md#paper-convex-decomposition-feature-fields) | 把离散几何分解改为先学习连续相容特征，再做聚类。 |
| 机器学习基础与统计 | 优化策略 | [PrivSynth: Alternating and Control-Based Optimization for Privacy and Utility in Synthetic Data](cards.md#paper-privsynth) | 发布合成训练数据前，应把隐私风险和任务效用共同纳入生成及样本选择。 |
| 多模态学习 | 表示学习 | [Nonparametric Deep Fine-grained Clustering with Low-Rank Guided Vision-Language Model](cards.md#paper-nonparametric-vlm-fine-clustering) | 无细粒度标签时，使用非参数聚类选择簇数，并仅对低秩方向施加适配。 |
| 计算机视觉 | 数据增强 | [FreeScale: Scaling 3D Scenes via Certainty-Aware Free-View Generation](cards.md#paper-freescale-certainty-views) | 把不完美重建当数据集增广器，需要先筛高几何确定性和有用的自由视角。 |
| 计算机视觉 | 自监督学习 | [Beyond Binary Contrast: Modeling Continuous Skeleton Action Spaces with Transitional Anchors](cards.md#paper-tranclr) | 连续动作表示中构造转场锚点，避免二元对比把过渡硬切成离散簇。 |
| 机器学习基础与统计 | 模型架构 | [Enhancing Mixture-of-Experts Specialization via Cluster-Aware Upcycling](cards.md#paper-cluster-aware-upcycling) | 将稠密模型转成 MoE 时，让专家初始化匹配数据激活簇，路由从同一簇中心起步。 |
| 计算机视觉 | 表示学习 | [Deep Feature Deformation Weights](cards.md#paper-deep-feature-deformation-weights) | 网格交互编辑可按表面特征相似度即时生成新控制柄的变形权重。 |
| 计算机视觉 | 推理优化 | [ELiC: Efficient LiDAR Geometry Compression via Cross-Bit-depth Feature Propagation and Bag-of-Encoders](cards.md#paper-elic-cross-bit-depth-propagation) | 层次点云压缩在粗细位深间重用上下文特征，让编码器容量匹配该层占据统计。 |
| 机器人学 | 表示学习 | [PhysGS: Bayesian-Inferred Gaussian Splatting for Physical Property Estimation](cards.md#paper-physgs-bayesian-properties) | 在可用于操作的三维地图中存物理属性分布，按多观测更新并保留不同来源的不确定性。 |
| 多模态学习 | 强化学习 | [Eliciting Complex Spatial Reasoning in MLLMs through Wide-Baseline Matching](cards.md#paper-dcrl-wide-baseline-curriculum) | 训练空间对应时按基线视角差和点级难度分配课程，使用已知对应作可验证奖励。 |
| 计算机视觉 | 表示学习 | [Learning Differentiable Hierarchies in 3D Gaussian Splatting](cards.md#paper-differentiable-gaussian-lod) | 若需在不同容量下部署三维场景，可直接学习图元贡献排序，让训练覆盖从低到高预算。 |
| 机器人学 | 条件生成 | [GraspLDP: Towards Generalizable Grasping Policy via Latent Diffusion](cards.md#paper-graspldp-grasp-priors) | 扩散动作生成可同时条件化可行抓姿和抓取位置的视觉重建，分别约束轨迹与局部几何。 |
| 生成模型 | 评估与诊断 | [Attention, May I Have Your Decision? Localizing Generative Choices in Diffusion Models](cards.md#paper-implicit-diffusion-decisions-self-attention-localization) | 扩散模型的隐含属性决策可先用探针定位，再比较自注意和跨注意干预。见表 2。 |
| 多模态学习 | 表征学习 | [Multi-speaker Attention Alignment for Multimodal Social Interaction](cards.md#paper-speaker-consistent-video-text-attention) | 多人视频问答可明确把说话位置与对白绑定，再与同样提供说话框的骨干比较。见表 2。 |
| 机器学习 | 训练策略 | [Few-for-Many Personalized Federated Learning](cards.md#paper-fedfew-pareto-model-bank-for-heterogeneous-clients) | 客户端很多时可先训练少量不同权衡的共享模型，衡量分配后的均值、最差客户端和服务器存储。见表 1。 |
| 生成模型 | 表征学习 | [Video Generation with Stable Transparency via Shiftable RGB-A Distribution Learner](cards.md#paper-rgba-alpha-specific-latent-and-noise-distributions) | 若生成目标对不同通道有不同语义，可单独调整辅助通道的潜变量及噪声分布，并检查主通道是否退化。见表 3。 |
| 多模态学习 | 表征学习 | [Lenses: Toward Polysemous Vision-Language Understanding](cards.md#paper-lenses-category-slots-for-image-polysemy) | 同图有不同语义解释时，可以保留分视角的嵌入槽，而非压成单描述，再单测每个解释视角。见表 3。 |
| 机器学习 | 模型融合 | [Preference-Aligned LoRA Merging: Preserving Subspace Coverage and Addressing Directional Anisotropy](cards.md#paper-tara-merging-subspace-coverage-anisotropy) | 融合多个低秩适配器需要检查合并子空间是否覆盖各任务，以及每个方向的贡献是否失衡。见表 3。 |
| 计算机视觉 | 表示学习 | [AnchorSplat: Feed-Forward 3D Gaussian Splatting With 3D Geometric Priors](cards.md#paper-anchorsplat) | 视角数量增长时用三维锚生成高斯，防止表征规模跟每视图像素线性绑定。 |
| 多模态学习 | 训练策略 | [Circular-DPO: Aligning Multi-Stage 3D Generative Models via Preference Feedback Loop](cards.md#paper-circular-dpo) | 多阶段生成被不可微步骤隔开时，用后阶段偏好优化后的输出重构前阶段偏好样本。 |
| 计算机视觉 | 模型架构 | [Align Images Before You Generate](cards.md#paper-corradapter) | 先在生成模型中寻找区域匹配，再对匹配处传递特征，避免用全图平均强行做一致。 |
| 机器人学 | 训练策略 | [Recover to Predict: Progressive Retrospective Learning for Variable-Length Trajectory Prediction](cards.md#paper-progressive-retrospective-trajectory) | 历史长度不稳定的预测任务可用渐进回溯恢复中间表征，再从完整观测教师蒸馏。 |
| 计算机视觉 | 表示学习 | [CoSMo3D: Open-World Promptable 3D Semantic Segmentation through LLM-Guided Canonical Spatial Modeling](cards.md#paper-cosmo3d) | 开放式部件分割可比较传感器坐标与对象统一坐标，利用功能位置而非绝对朝向。 |
| 计算机视觉 | 测试时适应与推理 | [Stabilizing Streaming Video Geometry via Dynamic Feature Normalization](cards.md#paper-dyfn-streaming-geometry) | 视频深度比例和平移漂移时，先测中间特征均值和方差，优先用因果归一化缓解。 |
| 机器学习基础与统计 | 优化策略 | [Learning to Solve PDEs on Neural Shape Representations](cards.md#paper-pde-neural-shape) | 输入是神经隐式形状时，可验证基于局部形状特征的网格无关 PDE 更新。 |
| 机器人学 | 推理优化 | [FantasyVLN: Unified Multimodal Chain-of-Thought Reasoning for Vision-and-Language Navigation](cards.md#paper-fantasyvln-latent-navigation-reasoning) | 导航训练可引入压缩的视觉想象表征，部署时避免显式解码想象帧。 |
| 多模态学习 | 强化学习 | [Mimic Human Cognition, Master Multi-Image Reasoning: A Meta-Action Framework for Enhanced Visual Understanding](cards.md#paper-cinema-structured-visual-meta-actions) | 多图推理可显式区分全局扫视、局部聚焦和证据提示，再安排探索与利用阶段。 |
| 多模态学习 | 评测与分析 | [ELV-Halluc: Benchmarking Semantic Aggregation Hallucinations in Video Understanding](cards.md#paper-elv-halluc-semantic-aggregation) | 视频幻觉诊断先确认帧级事实，再测跨事件合并是否错误。 |
| 机器学习基础 | 可解释性与诊断 | [Select, Hypothesize and Verify: Towards Verified Neuron Concept Interpretation](cards.md#paper-verified-neuron-concepts) | 为神经元生成概念解释后，独立测该概念能否诱发目标激活，并允许没有可信概念。 |
| 多模态学习 | 评测与分析 | [M4-RAG: A Massive-Scale Multilingual Multi-Cultural Multimodal RAG](cards.md#paper-m4-rag-model-scale-diagnostics) | 是否为多语视觉问答开启检索应按模型规模、语言和证据质量实测，允许跳过。 |
| 计算机视觉 | 损失函数与优化 | [SparseOIT: Improving Order-Independent Transparency 3DGS via Active Set Method](cards.md#paper-sparseoit-active-set) | 改用透明度渲染近似后重新测变量依赖；依赖稀疏时只优化活跃图元。 |
| 智能体 | 评估与诊断 | [Simple Agents Outperform Experts in Biomedical Imaging Workflow Optimization](cards.md#paper-workflow-agents-separate-structure-and-parameter-search) | 优化已有图像工作流时应比较基础搜索代理和专家函数、函数库、反思等增强，按可选操作与参数复杂度分层。见表 2。 |
| 多模态学习 | 检索增强 | [M^3KG-RAG: Multi-hop Multimodal Knowledge Graph-enhanced Retrieval-Augmented Generation](cards.md#paper-m3kg-rag-modality-retrieval-graph-filtering) | 音视频检索可保留模态专属入口，在检索后用图结构筛选知识，并单测两者是否互补。见表 4。 |
| 生成模型 | 推理策略 | [Guiding Token-Sparse Diffusion Models](cards.md#paper-sparse-guidance-token-capacity-gap) | 稀疏训练的扩散模型不能从普通 CFG 获益时，可用疏密不同的视觉标记预测形成指导信号。见表 1。 |
| 机器学习 | 表征学习 | [FedDAP: Domain-Aware Prototype Learning for Federated Learning under Domain Shift](cards.md#paper-feddap-domain-specific-prototype-alignment) | 异质联邦识别可保留每个域的类原型，避免全局平均掩盖域内结构，再比较聚合策略。见表 4。 |
| 多模态学习 | 评估与诊断 | [RealUnify: Do Unified Models Truly Benefit from Unification? A Comprehensive Benchmark](cards.md#paper-realunify-bidirectional-understanding-generation-evaluation) | 评估统一理解与生成模型可分别测试理解帮助生成和生成帮助理解，再和专用模型对照。见表 3。 |
| 多模态学习 | 评估与诊断 | [Grounded Chain-of-Thought for Multimodal Large Language Models](cards.md#paper-grounded-cot-separate-answer-and-evidence-accuracy) | 视觉推理可要求各步给坐标，并将答案正确、定位正确和两者一致分开计分。见表 1。 |
| 计算机视觉 | 模型架构 | [Node-RF: Learning Generalized Continuous Space-Time Scene Dynamics with Neural ODE-based NeRFs](cards.md#paper-node-rf) | 需要连续时间外推时，可将场景动力学与渲染分开学习，并在长于训练窗的轨迹上验收。 |
| 计算机视觉 | 数据增强 | [EventHub: Data Factory for Generalizable Event-Based Stereo Networks without Active Sensors](cards.md#paper-eventhub) | 普通相机可作为训练辅助，通过新视角生成分离估计视差标签与生成事件数据两条路径。 |
| 计算机视觉 | 自监督学习 | [Boosting Self-Supervised Tracking with Contextual Prompts and Noise Learning](cards.md#paper-pntrack) | 无标签跟踪可先用实例 patch 形成语义关联，再逐渐加入上下文噪声。 |
| 计算机视觉 | 生成模型 | [EI-Part:Explode for Completion and Implode for Refinement](cards.md#paper-ei-part) | 多部件生成可在分散规范态补齐零件，再回装配态细化对接几何。 |
| 机器学习基础与统计 | 表示学习 | [Assignment-Driven Hash Learning in a Hyper-Semantic Space for On-the-Fly Category Discovery](cards.md#paper-assignment-driven-category-discovery) | 流式开放类别发现时，分别检验已知类是否占满表示空间，以及连续表示到哈希的损失。 |
| 多模态学习 | 推理压缩 | [MASQuant: Modality-Aware Smoothing Quantization for Multimodal Large Language Models](cards.md#paper-masquant) | 低比特多模态模型要先测各模态激活尺度差异，再决定平滑因子能否共享。 |
| 多模态学习 | 参数高效微调 | [CRAFT-LoRA: Content-Style Personalization via Rank-Constrained Adaptation and Training-Free Fusion](cards.md#paper-craft-lora) | 融合主体和风格适配器时，先约束训练得到的子空间，再按去噪阶段分配权重。 |
| 计算机视觉 | 模型架构 | [PCA-Seg: Revisiting Cost Aggregation for Open-Vocabulary Semantic and Part Segmentation](cards.md#paper-pca-seg-parallel-cost) | 开放词汇分割的代价体可并行聚合空间与类别维度，比较是否减少串行语义干扰。 |
| 多模态学习 | 条件生成 | [LaRP: Efficient Multi-View Inpainting with Latent Reprojection Priors](cards.md#paper-larp-latent-reprojection) | 多视图补绘在生成阶段输入跨视角重投影潜变量，避免各图独立补后再耗时对齐。 |
| 多模态学习 | 条件生成 | [Breaking Semantic Boundaries: Distribution-Guided Semantic Exploration for Creative Generation](cards.md#paper-distok-distribution-conditional-generation) | 探索生成语义时，把软类别分布作为连续条件，而非只串接两个现有概念名。 |
| 计算机视觉 | 表示学习 | [ResiHMR: Residual-Limb Aware Single-Image 3D Human Mesh Recovery for Individuals with Limb Loss](cards.md#paper-resihmr-topology-adaptive) | 形体拓扑与标准模板不符时，先定义可见且有效的关节子图，再单独建模末端表面。 |
| 机器人学 | 模型架构 | [Motus: A Unified Latent Action World Model](cards.md#paper-motus-unified-latent-action) | 统一策略和世界模型时，用模态噪声日程切换动作、视频及联合预测，跨数据共享潜动作。 |
| 机器人学 | 评估与诊断 | [Neural Distribution Prior for LiDAR Out-of-Distribution Detection](cards.md#paper-ndp-imbalanced-lidar-ood-score-prior) | 长尾感知的域外分数可根据已知类预测分布校准，比较阈值之外的 AP 与误报率。见表 5。 |
| 计算机视觉 | 推理策略 | [Physics-Consistent Diffusion for Efficient Fluid Super-Resolution via Multiscale Residual Correction](cards.md#paper-remd-multigrid-physical-residual-correction) | 重建连续物理场时，可以在去噪中施加多尺度残差校正，并对照像素、频谱与物理指标。见表 2。 |
| 生成模型 | 模型效率 | [LazyVAR: Accelerating Visual Autoregressive Models via Scale-wise Token Pruning and Parallel Group Decoding](cards.md#paper-lazyvar-parallel-adjacent-scale-decoding) | 逐尺度视觉解码可利用相邻尺度的聚合潜表示相似性，合并并行处理并剪除重复标记。见表 1。 |
| 多模态学习 | 训练策略 | [HiSpatial: Taming Hierarchical 3D Spatial Understanding in Vision-Language Models](cards.md#paper-hispatial-lower-level-spatial-supervision-dependencies) | 高层空间推理训练可分别消融底层几何和关系监督，避免只堆高层推理数据。见表 5、6。 |
| 机器学习 | 训练策略 | [FedRAC: Rolling Submodel Allocation for Collaborative Fairness in Federated Learning](cards.md#paper-fedrac-rolling-submodel-allocation-fairness) | 联邦训练的子模型容量可按贡献调整，同时轮转激活单元，以避免同一部分参数总由少数客户端更新。见表 4、5。 |
| 生成模型 | 损失与奖励 | [SpeeDiff: Scalable Pixel-Anchored End-to-End Latent Diffusion Model](cards.md#paper-speediff-pixel-anchored-joint-latent-training) | VAE 与扩散器联训若使潜变量坍塌，可用像素重建约束扩散估计，再与断开梯度比较。见表 1。 |
| 机器学习基础与统计 | 推理压缩 | [AdaSVD: Singular Value Decomposition with Adaptive Mechanisms for Large Multimodal Models](cards.md#paper-adasvd) | 固定总压缩预算时分别学习各层压缩率，并用交替更新补偿截断误差。 |
| 多模态学习 | 输入表示 | [ARC Is a Vision Problem!](cards.md#paper-vision-arc) | 棋盘式推理任务可先做空间画布到画布的视觉基线，再与序列化指令比较。 |
| 多模态学习 | 强化学习 | [Reinforce to Learn, Elect to Reason: A Dual Paradigm for Video Reasoning](cards.md#paper-rler-video-evidence-election) | 训练模型生成可解析帧证据，推理时再以证据一致性加权聚合候选。 |
| 多模态学习 | 模型架构 | [VIRST: Video-Instructed Reasoning Assistant for SpatioTemporal Segmentation](cards.md#paper-virst-dynamic-anchors) | 视频分割跟踪可按最近可靠时刻更新锚，在遮挡与重现中测试。 |
| 计算机视觉 | 持续学习 | [Beyond Prompt Degradation: Prototype-guided Dual-pool Prompting for Incremental Object Detection](cards.md#paper-pdp-dual-prompt-pool) | 增量检测时分共享与任务专有提示，并修复新任务把旧类当背景的监督。 |
| 机器人学 | 模型架构 | [MergeVLA: Cross-Skill Model Merging Toward a Generalist Vision-Language-Action Agent](cards.md#paper-mergevla) | 若最终要合并机器人技能，训练时就限制视觉适配器和动作专家之间的跨层干扰。 |
| 多模态学习 | 模型架构 | [HieraMamba: Video Temporal Grounding via Hierarchical Anchor-Mamba Pooling](cards.md#paper-hieramamba) | 长视频压缩保留跨层时序锚，并以局部段与全局文本双目标训练。 |
| 计算机视觉 | 推理优化 | [WeDetect: Fast Open-Vocabulary Object Detection as Retrieval](cards.md#paper-wedetect-region-retrieval) | 开放词汇检测需要事后切换查询时，缓存候选区域向量，在同一空间做文本检索。 |
| 多模态学习 | 表示学习 | [Latent Implicit Visual Reasoning](cards.md#paper-latent-implicit-visual-reasoning) | 视觉推理训练可让隐词元按任务重寻图像线索，并以最终任务监督取代人工绘制中间图。 |
| 计算机视觉 | 训练与数据策略 | [Guardians of the Hair: Rescuing Soft Boundaries in Depth, Stereo, and Novel Views](cards.md#paper-hairguard-soft-boundary-correction) | 薄边界的深度适配训练复用抠图软边界标注，用门控残差只修局部。 |
| 计算机视觉 | 损失函数与优化 | [Real-Time Dynamic Scene Rendering with Controlled Compressibility and Contact Awareness](cards.md#paper-dynamic-gaussian-velocity-projection) | 动态场景的图元速度可投影至具有不同压缩性约束的物理分量，再做渲染。 |
| 多模态学习 | 推理优化 | [Rethinking Prompt Design for Inference-time Scaling in Text-to-Visual Generation](cards.md#paper-pris-elementwise-prompt-revision) | 生成推理扩展可按属性聚合多个候选的共同失误，再重写提示，而非持续抽样原提示。 |
| 计算机视觉 | 可解释性与诊断 | [Finding Distributed Object-Centric Properties in Self-Supervised Transformers](cards.md#paper-object-dino-distributed-patch-attention) | 提取无监督对象线索时，先检查跨层 patch 注意力的 Q/K/V 相似关系，避免只用末层全局词元。 |
| 生成模型 | 模型效率 | [DisCa: Accelerating Video Diffusion Transformers with Distillation-Compatible Learnable Feature Caching](cards.md#paper-disca-distillation-compatible-video-feature-cache) | 视频扩散少步蒸馏完成后，决定缓存残余特征是否需要学预测器。见表 3。 |
| 计算机视觉 | 表征学习 | [Spike-driven Discrete Aggregation for Event-based Object Detection](cards.md#paper-spike-driven-discrete-event-aggregation) | 异步传感器转稠密特征时，可先测选事件是否优于等时间分辨率的全事件累积。见表 3。 |
| 机器学习 | 训练策略 | [Reframing Long-Tailed Learning via Loss Landscape Geometry](cards.md#paper-grouped-sharpness-long-tail-training) | 稀有类后期退化时，可以比较组特异扰动与被头类主导的全局 SAM 扰动。见表 4–5。 |
| 计算机视觉 | 评估与诊断 | [KLIP: Localized Distribution Shift Detection via KL-Divergence with Diffusion Priors in Inverse Problems](cards.md#paper-klip-local-diffusion-posterior-shift) | 间接观测下，可比较全局异常分数与基于先验到后验变化的局部分块评分。见表 2–3。 |
| 生成模型 | 推理策略 | [Precise Object and Effect Removal with Adaptive Target-Aware Attention](cards.md#paper-objectclear-effect-aware-diffusion-compositing) | 消除物体时，可用可超出物体掩模的效应图限制实际重绘范围，单独验证背景保真。见表 2。 |
| 计算机视觉 | 表征学习 | [Scaling Up AI-Generated Image Detection with Generator-Aware Prototypes](cards.md#paper-gapl-diverse-source-detector-prototypes) | 防御性图像检测扩充来源之前，应把多源原型与单个聚合边界一起评估，检查盲目扩充导致的性能反转。 |
| 多模态学习 | 输入表示 | [ViKey: Enhancing Temporal Understanding in Videos via Visual Prompting](cards.md#paper-vikey-visual-temporal-prompt) | 视频只采少量帧时可把原始顺序写到视觉输入，并对照词语到帧的检索定位。 |
| 机器人学 | 推理与规划 | [SceMoS: Scene-Aware 3D Human Motion Synthesis by Planning with Geometry-Grounded Tokens](cards.md#paper-scemos-geometry-tokens) | 动作生成可用全局鸟瞰规划与局部高度图接触建模取代统一高维3D输入。 |
| 多模态学习 | 评测与诊断 | [TriDF: Evaluating Perception, Detection, and Hallucination for Interpretable DeepFake Detection](cards.md#paper-tridf-explanation-audit) | 检测系统同时测判别、证据识别和解释幻觉，避免把分类正确当作证据可靠。 |
| 多模态学习 | 评测与诊断 | [Re-evaluating Continual VQA: Toward Fair and Robust Evaluation for Multimodal Continual Learning](cards.md#paper-uco-vqa-evaluation) | 持续问答评估应分开检查跨任务答案重叠与任务内先验变化，再据此度量遗忘。 |
| 多模态学习 | 强化学习 | [Let VLMs Grade Their Own Thoughts: A Self-Quantification Approach to Reasoning-Aware Reward Modeling](cards.md#paper-video-raise) | 采用模型自评分奖励前，区分逐步信心约束与组内相对排序，并和外部评分对照。 |
| 多模态学习 | 强化学习 | [PSR: Scaling Multi-Subject Personalized Image Generation with Pairwise Subject-Consistency Rewards](cards.md#paper-psr-pairwise-subject) | 多个个性化对象同画面时按主体配对评分，再与整个画面审美和提示一致性分开衡量。 |
| 机器学习基础 | 模型架构 | [UniMMAD: Unified Multi-Modal and Multi-Class Anomaly Detection via MoE-Driven Feature Decompression](cards.md#paper-unimmad-expert-feature-decompression) | 多个感知域共用异常模型时，把通用特征压缩与模态和类别特定的恢复分开。 |
| 多模态学习 | 可解释性与诊断 | [Where MLLMs Attend and What They Rely On: Explaining Autoregressive Token Generation](cards.md#paper-eagle-autoregressive-token-attribution) | 解读特定生成词时，用同一个局部区域分别验证保留后是否足够与删除后的影响。 |
| 多模态学习 | 条件生成 | [SymphoMotion: Joint Control of Camera Motion and Object Dynamics for Coherent Video Generation](cards.md#paper-symphomotion-camera-object-control) | 视频生成时把相机运动和物体轨迹分开输入，再检查深度感知的运动可控性。 |
| 多模态学习 | 推理优化 | [Tell Model Where to Look: Mitigating Hallucinations in MLLMs by Vision-Guided Attention](cards.md#paper-vision-guided-attention-coverage) | 描述图像时先由视觉词元定位证据，并抑制已经描述的区域，减少重复及幻觉。 |
| 计算机视觉 | 微调与适配 | [Measure The Feature Universe: Topology-based Pseudo Labeling and Gravity Consistency for Source-Free Domain Adaptation](cards.md#paper-feature-universe-source-free-adaptation) | 无源适配的伪标签优先沿高置信特征区传播，并按特征相似性加权一致约束。 |
| 计算机视觉 | 微调与适配 | [Boosting Vision-Language Models Towards Cross-Domain Incremental Object Detection](cards.md#paper-dgs-cross-domain-incremental-detection) | 类别与域同时变化的检测中，按任务分布动态分组适配器，定期合并共享子空间。 |
| 生成模型 | 模型效率 | [D2Cache: Second-Order Delta Caching for Higher Video Diffusion Acceleration](cards.md#paper-d2cache-second-difference-video-cache) | 同一缓存间隔下可测试残差二阶差分预测，避免为加速另训预测器。见表 1。 |
| 多模态学习 | 损失与奖励 | [StructXLIP: Enhancing Vision-language Models with Multimodal Structural Cues](cards.md#paper-structxlip-structure-aware-contrastive-retrieval) | 长描述检索可比较额外结构对齐与纯图文对比，在同样召回设置观察结构线索收益。见表 4。 |
| 计算机视觉 | 表征学习 | [Deformation-based In-Context Learning for Point Cloud Understanding](cards.md#paper-deformpic-query-deformation-point-cloud-icl) | 点云任务共享上下文示例时，优先验证统一输入形变能否替代依赖目标掩码的重建。见表 3。 |
| 多模态学习 | 推理策略 | [M3DocDep: Multi-modal, Multi-page, Multi-document Dependency Chunking with Large Vision-Language Models](cards.md#paper-m3docdep-dependency-tree-before-rag-chunking) | 长文档 RAG 可以先恢复跨页树依赖再分块，用共享版面块控制 OCR 和解析差异。见表 1–4。 |
| 计算机视觉 | 损失与奖励 | [Differentiable Laplacian Matrix Guided Superpixel Segmentation](cards.md#paper-differentiable-graph-laplacian-superpixel-connectivity) | 若分割后端依赖连通性修补，可先在软分配上使用图拉普拉斯损失，再测离散碎片数。见表 3。 |
| 生成模型 | 表征学习 | [PoseAnything: General Pose-guided Video Generation with Part-aware Temporal Coherence](cards.md#paper-poseanything-part-matched-temporal-coherence) | 姿态控制视频可比较按对应部位分配时序注意力与整物体注意力。见表 3。 |
| 多模态学习 | 推理加速 | [Content-Aware Dynamic Patchification for Efficient Video Diffusion](cards.md#paper-dynapatch) | 视频分词时依内容复杂度分配块尺寸，先减少静态区域的计算。 |
| 计算机视觉 | 生成模型 | [Object-WIPER: Training-Free Object and Associated Effect Removal in Videos](cards.md#paper-object-wiper) | 编辑对象时另显式找反光、阴影等关联区域，同时冻结无关的背景 token。 |
| 多模态学习 | 推理加速 | [EarlyTom: Early Token Compression Completes Fast Video Understanding](cards.md#paper-earlytom) | 优化首 token 延迟前把视觉编码与语言预填充分开计时，必要时在视觉骨干内部合并。 |
| 多模态学习 | 推理策略 | [ReaGEN: Adaptive Generation of Structured Chains-of-Thought for Efficient Multimodal Reasoning](cards.md#paper-reagen) | 如不改基座，可用教师离线搜索结构化推理流程，让轻模型在推理时生成。 |
| 计算机视觉 | 模型架构 | [WorldStereo: Bridging Camera-Guided Video Generation and Scene Reconstruction via 3D Geometric Memories](cards.md#paper-worldstereo) | 从多轨迹生成一致场景时，将显式全局几何记忆与对应区域的局部外观记忆分开。 |
| 多模态学习 | 训练策略 | [CoFiDA-M: Concept-Aware Feature Modulation for Cross-Domain Adaptation with Image-Only Inference](cards.md#paper-cofida-m) | 训练时可用语义属性引导特征调制，再让只看图像的学生蒸馏调制结果。 |
| 计算机视觉 | 训练与数据策略 | [FoundIR-v2: Optimizing Pre-Training Data Mixtures for Image Restoration Foundation Model](cards.md#paper-foundir-v2-data-equilibrium) | 统一图像恢复预训练可先估算任务数据配比对各自表现的影响，再动态重分训练份额。 |
| 机器学习基础 | 模型架构 | [Learning Coordinate-based Convolutional Kernels for Continuous SE(3) Equivariant and Efficient Point Cloud Analysis](cards.md#paper-eckconv-coordinate-equivariant-kernels) | 点云卷积需要严格 SE(3) 等变时，用坐标网络参数化双陪集上的等变核。 |
| 多模态学习 | 评测与分析 | [SALMUBench: A Benchmark for Sensitive Association-Level Multimodal Unlearning](cards.md#paper-salmubench-association-unlearning) | 验证多模态遗忘时拆分具体身份—属性关联、未见身份和应保留邻近关联。 |
| 多模态学习 | 损失函数与优化 | [Stay in your Lane: Role Specific Queries with Overlap Suppression Loss for Dense Video Captioning](cards.md#paper-dense-video-role-specific-queries) | 视频事件定位和描述可分别用角色查询，并监督二者对齐和区间去重。 |
| 多模态学习 | 模型架构 | [Group Diffusion: Enhancing Image Generation by Unlocking Cross-Sample Collaboration](cards.md#paper-group-diffusion-cross-sample-attention) | 重复采样可比较样本间注意力协作，避免默认批中每张图独立去噪。 |
| 计算机视觉 | 表示学习 | [MoRe: Motion-aware Feed-forward 4D Reconstruction Transformer](cards.md#paper-more-motion-aware-reconstruction) | 动态重建要稳定估相机时，可通过注意力监督区分随视图一致的结构和独立运动。 |
| 生成模型 | 表征学习 | [SIMPLEPOSTER: A SIMPLE BASELINE FOR PRODUCT POSTER GENERATION](cards.md#paper-simpleposter-character-position-encoding) | 多行文字生成时可用逐字符位置编码替代额外的布局控制器，并直接比较文字正确率。见表 3。 |
| 多模态学习 | 评估与诊断 | [Towards Policy-Adaptive Image Guardrail: Benchmark and Method](cards.md#paper-policy-conditioned-visual-moderation-diagnostics) | 动态审核应保留变更规则的独立测试，通过视觉匹配对照诊断模型学的是当前政策还是固定标签。见表 6。 |
| 多模态学习 | 评估与诊断 | [Beyond Single-View Sufficiency: CVBench for Cross-View Human Understanding](cards.md#paper-cvbench-verified-single-view-insufficiency) | 多视角评测可逐项要求单视角不足，并对空间和时间错误分别统计。见表 4。 |
| 机器学习 | 训练策略 | [Adaptive Data Augmentation with Multi-armed Bandit: Sample-Efficient Embedding Calibration for Implicit Pattern Recognition](cards.md#paper-adamab-bandit-augmentation-frozen-embeddings) | 只有少数样本且编码器不可训练时，可比较自适应增强分配和随机增强的效果。见表 2。 |
| 计算机视觉 | 评估与诊断 | [Sparsity as a Key: Unlocking New Insights from Latent Structures for Out-of-Distribution Detection](cards.md#paper-sae-class-activation-profile-ood-diagnosis) | 异常分数可从全局距离切换到稀疏类别激活结构偏差，并应跨骨干检查稳定性。 |
| 多模态学习 | 训练策略 | [TIPSv2: Advancing Vision-Language Pretraining with Enhanced Patch-Text Alignment](cards.md#paper-tipsv2-visible-patch-distillation) | 视觉语言的局部词义对齐可测试可见 patch 是否也纳入蒸馏目标。见表 2。 |
| 生成模型 | 模型效率 | [NAMI: Efficient Image Generation via Bridged Progressive Rectified Flow Transformers](cards.md#paper-nami-bridgeflow-resolution-depth-schedule) | 大分辨率生成可把模型深度预算推迟到高分辨率，并测试阶段桥接成本。见表 7。 |
| 机器学习基础与统计 | 生成模型 | [Temporal Equilibrium MeanFlow: Bridging the Scale Gap for One-Step Generation](cards.md#paper-temf) | 单步生成训练要按时间跨度审计梯度贡献，再分别调权和安排课程。 |
| 多模态学习 | 推理压缩 | [Mostly Text, Smart Visuals: Asymmetric Text-Visual Pruning for Large Vision-Language Models](cards.md#paper-atv-pruning) | VLM 权重裁剪应拆开文本和视觉校准，并根据各自敏感性决定是否共享样本。 |
| 多模态学习 | 评测与诊断 | [The LLM Bottleneck: Why Open-Source Vision LLMs Struggle with Hierarchical Visual Recognition](cards.md#paper-hierarchical-recognition-llm-bottleneck) | 层级视觉识别先用对应纯文本题诊断语言骨干的分类树知识，再做图文适配。 |
| 多模态学习 | 测试时适应与推理 | [Test-Time Alignment of Text-to-Image Diffusion Models via Null-Text Embedding Optimisation](cards.md#paper-null-tta) | 推理期优化奖励时，可调整生成引导的语义锚并检查辅助奖励与人评，避免像素噪声虚高。 |
| 机器学习基础与统计 | 联邦学习 | [FedHarmony: Harmonizing Heterogeneous Label Correlations in Federated Multi-Label Learning](cards.md#paper-fedharmony) | 联邦多标签宜按标签相关统计质量加权，并将共享相关结构作为本地约束。 |
| 机器人学 | 训练策略 | [SPEAR-1: Scaling Beyond Robot Demonstrations via 3D Understanding](cards.md#paper-spear-1) | 机器人数据昂贵时，先在普通图像补三维定位监督，再比较对操作迁移的贡献。 |
| 计算机视觉 | 输入表示 | [MuViT: Multi-Resolution Vision Transformers for Learning Across Scales in Microscopy](cards.md#paper-muvit-world-resolution) | 对真实多尺度输入共享物理坐标位置编码，使细节直接与粗视野对齐。 |
| 计算机视觉 | 表示学习 | [SuP: Sub-cloud Driven Point Cloud Registration](cards.md#paper-sup-subcloud-registration) | 全局低重叠时，先挖高重叠局部锚块，再合并对应做全局配准。 |
| 多模态学习 | 可解释性与诊断 | [When Token Pruning is Worse than Random: Understanding Visual Token Information in VLLMs](cards.md#paper-visual-token-information-horizon) | 剪视觉词元时用同预算随机剪枝作逐层对照，别假定深层依旧需要显著性排序。 |
| 计算机视觉 | 条件生成 | [Rethinking Diffusion Model-Based Video Super-Resolution: Leveraging Dense Guidance from Aligned Features](cards.md#paper-dgaf-vsr-feature-compensation) | 视频扩散恢复中优先在特征空间补偿跨帧信息，逐级复核变换分辨率的收益。 |
| 机器学习基础 | 损失函数与优化 | [Revisiting F-measure Optimization in Multi-Label Classification: A Sampling-based Approach](cards.md#paper-fft-sampled-f-measure-optimization) | 多标签以 F 值作目标时，利用其预测规则矩阵的结构转为卷积，并避免难估的直接多项分布。 |
| 多模态学习 | 微调与适配 | [TANGO: Text-Anchored Guided Optimization for Robust Fine-tuning Vision-Language Models under Label Noise](cards.md#paper-tango-text-anchored-noisy-labels) | 图文模型的噪声标签微调可用固定文本语义锚校正，避免仅依赖模型的视觉自纠。 |
| 多模态学习 | 评测与分析 | [Too Vivid to Be Real? Benchmarking and Calibrating Generative Color Fidelity](cards.md#paper-generative-color-fidelity-audit) | 评估照片风格生成时，独立衡量色彩真实感，而不将鲜艳高对比与质量等同。 |
| 机器人学 | 模型架构 | [EgoRoC: Towards Egocentric Robotic Control via Task-Agnostic Visual Alignment](cards.md#paper-egoroc-reusable-visual-alignment) | 跨任务控制可将腕部视觉对齐训练成共享头，给冻结策略传六自由度位姿。 |
| 计算机视觉 | 评估与诊断 | [FluoCLIP: Stain-Aware Focus Quality Assessment in Fluorescence Microscopy](cards.md#paper-fluoclip-condition-dependent-ordinal-quality) | 不同传感条件的质量排序若有反转，应比较共享序数轴和条件化序数轴。 |
| 生成模型 | 推理策略 | [PoseD-Flow: Versatile and Guided Flow Matching Model of Human Pose](cards.md#paper-posed-flow-manifold-ode-inference-guidance) | 旋转约束的逆问题可比较内禀流先验和欧氏流，并通过采样 ODE 注入观测损失。 |
| 计算机视觉 | 损失与奖励 | [Toward Real-world Infrared Image Super-Resolution: A Unified Autoregressive Framework and Benchmark Dataset](cards.md#paper-real-iisr-relative-order-under-drift) | 相机响应有漂移时，可用相对强度顺序约束补充绝对像素误差。见第 4.5 节和图 7。 |
| 机器人学 | 表征学习 | [Dense Metric Depth Completion from Sparse Direct Time-of-Flight Sensors](cards.md#paper-dtof-directional-attention-preserves-depth-anchor) | 可对传感器锚点使用定向注意力，防止密集 RGB 特征覆盖可靠的稀疏深度。见表 3。 |
| 生成模型 | 损失与奖励 | [Omni-Supervised Motion Editing: Balancing Change and Invariance through Positive-Negative Learning](cards.md#paper-omnime-edit-preserve-triplet-supervision) | 局部编辑可单独对照源目标相似性引导的保持项，以及指导改变方向的三元组约束。见表 3。 |
| 机器学习 | 训练策略 | [FedRE: A Representation Entanglement Framework for Model-Heterogeneous Federated Learning](cards.md#paper-fedre-shared-weight-client-representation-and-label-mix) | 异构联邦客户端可比较一次上传联合混合表征与按类上传原型，分别计量上下行。见表 2。 |
| 计算机视觉 | 生成模型 | [Scale Space Diffusion](cards.md#paper-scale-space-diffusion) | 高噪声阶段先检验空间信息带宽，可从低分辨率去噪并按时恢复细节。 |
| 机器学习基础与统计 | 训练策略 | [SelecTKD: Selective Token-Weighted Knowledge Distillation for LLMs](cards.md#paper-selectkd) | 师生能力有差距时，按教师能否验证学生候选决定 token 监督强度。 |
| 多模态学习 | 强化学习 | [Reinforcing Structured Chain-of-Thought for Video Understanding](cards.md#paper-sdrl-structured-video-cot) | 强化训练时可约束共享视觉事实一致，同时允许推理路线多样。 |
| 计算机视觉 | 模型架构 | [LitePT: Lighter Yet Stronger Point Transformer](cards.md#paper-litept) | 点云骨干可在高分辨率阶段用卷积提取局部几何，在降采样后再用注意力。 |
| 多模态学习 | 评测与诊断 | [VisRes Bench: On Evaluating the Visual Reasoning Capabilities of VLMs](cards.md#paper-visres-controlled-visual-reasoning) | 判断视觉推理是否依赖语言时，拿掉语言线索，将局部感知、单规则和组合分别测试。 |
| 多模态学习 | 损失函数 | [Guiding Diffusion-based Reconstruction with Contrastive Signals for Balanced Visual Representation](cards.md#paper-dcr-contrastive-reconstruction) | 重建和判别目标冲突时，把对比信号施加到重建结果，再分别测能力。 |
| 多模态学习 | 自监督学习 | [MoBind: Motion Binding for Fine-Grained IMU-Video Pose Alignment](cards.md#paper-mobind-hierarchical-motion-alignment) | 将视觉和可穿戴信号先在身体部位及短时间片对齐，再聚合到全身。 |
| 多模态学习 | 强化学习 | [Learning to Refuse: Refusal-Aware Reinforcement Fine-Tuning for Hard-Irrelevant Queries in Video Temporal Grounding](cards.md#paper-ra-rft-hard-irrelevant-queries) | 给视频片段检索增加与内容相似但事实不成立的负请求，单独训练和测拒绝。 |
| 机器学习基础 | 损失函数与优化 | [FedAdamom: Adaptive Momentum for Improved Generalization in Federated Optimization](cards.md#paper-fedadamom-momentum-generalization) | 联邦自适应更新应分开检验逃离鞍点和偏好平坦极小值，并联调全局动量。 |
| 机器学习基础 | 可解释性与诊断 | [Rethinking Concept Bottleneck Models: From Pitfalls to Solutions](cards.md#paper-cbm-suite-bottleneck-bypass) | 概念瓶颈模型选择概念集前测适用性，并检查线性头是否等价绕过瓶颈。 |
| 计算机视觉 | 自监督学习 | [WildRayZer: Self-supervised Large View Synthesis in Dynamic Environments](cards.md#paper-wildrayzer-static-residual-masks) | 从动态视频学静态三维一致性时，用仅相机运动解释后的渲染残差生成运动掩码。 |
| 计算机视觉 | 评测与分析 | [Attribution as Retrieval: Model-Agnostic AI-Generated Image Attribution](cards.md#paper-lida-generator-attribution-retrieval) | 生成图来源随新模型增加时，用可更新的参考库检索替代固定分类头。 |
| 多模态学习 | 训练策略 | [Spectrally Distilled Representations Aligned with Instruction-Augmented LLMs for Satellite Imagery](cards.md#paper-sattxt-privileged-spectrum-rgb-distillation) | 部署只剩 RGB 时，可比较仅训练可见的多光谱教师是否能补偿模态缺失。见表 4。 |
| 多模态学习 | 损失与奖励 | [Multimodal Distribution Matching for Vision-Language Dataset Distillation](cards.md#paper-mdm-joint-hyperspherical-paired-distillation) | 减少成对训练数据时，可对照匹配两模态共同与分歧方向是否比只保存各自边际更有效。 |
| 机器人学 | 模型架构 | [Localizing, Structuring, and Rendering: Bridging 3D and 2D Vision-Language-Action Models for Robotic Manipulation](cards.md#paper-diffrender-vla-differentiable-spatial-visual-interface) | 复用 2D VLA 接收 3D 上下文时，可以比较可反传的渲染接口和固定视角或分阶段连接。见表 3。 |
| 机器学习 | 训练策略 | [Towards Knowledge-augmented Bayesian Deep Learning For Computer Vision](cards.md#paper-knowledge-constrained-prior-and-adaptive-likelihood) | 安全有效的几何约束可同时用于先验预训练及后验约束，消融仅后者确认额外贡献。见表 5。 |
| 计算机视觉 | 训练策略 | [Masked-Diffusion Autoencoders for 3D Medical Vision Representation Learning](cards.md#paper-mdae-masked-structure-visible-texture-corruption) | 自监督体数据可把遮挡区的结构学习和可见区的纹理去噪同时训练，并比较可变遮挡率。见表 4。 |
| 机器人学 | 损失与奖励 | [BEV-CAR: Enhancing Monocular Bird's Eye View Segmentation with Context-Aware Rasterization](cards.md#paper-bev-car-ray-context-layout-supervision) | 单目 BEV 要恢复被遮挡的布局时，可增加沿射线的栅格监督，并分别报告布局和物体。见表 5–7。 |
| 多模态学习 | 推理加速 | [IF-Prune: Information-Flow Guided Token Pruning for Efficient Vision-Language Models](cards.md#paper-if-prune) | 用小模型辅助裁剪时，让其预测哪些 token 无信息，并与直接取注意力强度比较。 |
| 机器学习基础与统计 | 测试时适应与推理 | [Curvature-Aware Zeroth-Order Optimization for Memory-Efficient Test-Time Adaptation](cards.md#paper-cazo-tta) | 无反传在线更新时，利用适配损失的曲率统计减少零阶方向估计的方差。 |
| 机器学习基础与统计 | 模型分析 | [Hidden Monotonicity: Explaining Deep Neural Networks via their DC Decomposition](cards.md#paper-hidden-monotonicity-dc) | 需要解释非单调网络时，分解为两个单调凸分量，再检查归因数值稳定性。 |
| 多模态学习 | 评测与诊断 | [VL-RouterBench: A Benchmark for Vision-Language Model Routing](cards.md#paper-vl-routerbench) | 要做模型路由，先建同一题对所有候选的质量和开销矩阵，画出预算变化下的性能。 |
| 计算机视觉 | 表示学习 | [Neural Gabor Splatting: Enhanced Gaussian Splatting with Neural Gabor for High-frequency Surface Reconstruction](cards.md#paper-neural-gabor-splatting) | 高频纹理区域可给单几何基元内部的颜色函数，降低依赖增加基元数量。 |
| 计算机视觉 | 表示学习 | [RaUF: Learning the Spatial Uncertainty Field of Radar](cards.md#paper-rauf-anisotropic-uncertainty) | 测距传感误差随方向变化时，训练各向异性不确定场并独立验证压制杂波。 |
| 多模态学习 | 推理加速 | [Attention-aware Inference Optimizations for Large Vision-Language Models with Memory-efficient Decoding](cards.md#paper-attentionpack) | 长视觉上下文可低秩存跨头 KV，仅对当前较重要 token 加解压计算。 |
| 机器学习基础 | 损失函数与优化 | [Your Dissimilarities Define You: Complementary Learning Exploiting Class Diversities](cards.md#paper-opposite-class-complementary-learning) | 分类器除了学习正确类别，还可显式约束非目标类别的分数分布。 |
| 多模态学习 | 模型架构 | [Asynchronous Temporal Modeling with Two-Agent Framework for Streaming Dense Video Captioning](cards.md#paper-takusen-asynchronous-captioning) | 流式理解把低成本事件触发与高成本详细输出分给异步模块，以减少静默阈值失配。 |
| 机器人学 | 知识蒸馏 | [SkillSight: Efficient First-Person Skill Assessment with Gaze](cards.md#paper-skillsight-gaze-only-distillation) | 低功耗第一人称技能评估可用视频和凝视共同做教师，再蒸馏部署时只读凝视的学生。 |
| 多模态学习 | 条件生成 | [TGT: Text-Grounded Trajectories for Locally Controlled Video Generation](cards.md#paper-tgt-local-text-trajectory-guidance) | 控制多主体视频时把局部文本与每条轨迹绑定，调节局部与全局引导强度。 |
| 智能体 | 强化学习 | [Training One Model to Master Cross-Level Agentic Actions via Reinforcement Learning](cards.md#paper-crossha-agent-action-granularity) | 游戏代理可按当前进度选择高层宏动作或低层控制，用多轮训练学习切换。 |
| 计算机视觉 | 表征学习 | [Beyond Text: Visual Description Assembly by Probabilistic Model for CLIP-based Weakly Supervised Semantic Segmentation](cards.md#paper-vda-instance-visual-prototypes) | 在弱监督区域定位中比较实例条件视觉原型与所有图像共享的文本原型。 |
| 多模态学习 | 推理策略 | [R4-CGQA: Retrieval-based Vision Language Models for Computer Graphics Image Quality Assessment](cards.md#paper-r4-cgqa-retrieved-quality-evidence) | 给图像质量诊断提供视觉相似例的质量解释，分开消融内容和质量检索。 |
| 多模态学习 | 推理策略 | [ARGUS: Defending Against Multimodal Indirect Prompt Injection via Steering Instruction-Following Behavior](cards.md#paper-argus-instruction-adherence-defense) | 选择多模态防护时，同时测用户指令遵从和干预引起的效用下降。 |
| 多模态学习 | 训练策略 | [MonoVLM: Monocular 3D Visual Grounding with Vision Language Models](cards.md#paper-monovlm-localize-then-lift) | 单目三维定位训练可先学习二维落点，再学习结构，最后拟合全三维框。 |
| 多模态学习 | 评测与诊断 | [SLVMEval: Synthetic Meta Evaluation Benchmark for Text-to-Long Video Generation](cards.md#paper-slvmeval-perceptible-pairwise-audit) | 用人类可辨的受控反事实视频对检验长视频评分器，而不只依赖生成样本平均排名。 |
| 计算机视觉 | 推理压缩 | [Discovering Adaptive Task Dependencies for Efficient Multi-Task Representation Compression](cards.md#paper-atdc-image-dependent-task-graph) | 对多任务特征共享引入逐图编码顺序，并与固定顺序比较率失真和额外延迟。 |
| 机器学习基础 | 优化 | [Single-Round Scalable Analytic Federated Learning](cards.md#paper-safle-one-round-analytic-aggregation) | 在单轮通信约束下比较带稀疏分组特征的解析头与线性解析头。 |
| 计算机视觉 | 推理策略 | [HierEdit: Region-Aware Hierarchical Diffusion for Efficient High-Resolution Editing](cards.md#paper-hieredit) | 先低分辨率定位改动，再只细化高分辨率的局部窗口。 |
| 计算机视觉 | 训练策略 | [BluRef: Unsupervised Image Deblurring with Dense-Matching References](cards.md#paper-bluref) | 同类场景的未配对清晰参考经对应筛选可构造去模糊伪监督。 |
| 多模态学习 | 强化学习方法 | [Talk2Move: Reinforcement Learning for Text-Instructed Object-Level Geometric Transformation in Scenes](cards.md#paper-talk2move) | 把几何可判定的空间编辑指标用于探索，并拆分编辑成功与背景保真。 |
| 计算机视觉 | 优化 | [Linear Fundamental Matrix Estimation from 7 or 5 Points](cards.md#paper-linear-fundamental-minimal) | 在最小求解前检测结构化对应，并按几何成立条件启用线性解。 |
| 多模态学习 | 推理策略 | [Training-free Motion Factorization for Compositional Video Generation](cards.md#paper-motion-factorization) | 把静止、刚体与非刚体运动显式分解后，再以结构化计划指导合成。 |
| 多模态学习 | 训练策略 | [Cluster-Wise Spatio-Temporal Masking for Efficient Video-Language Pretraining](cards.md#paper-clusterstm) | 高掩码率下先保留簇级视觉覆盖，再比较时序代表 token 与均匀采样。 |
| 计算机视觉 | 模型架构 | [Selection-as-Nonlinearity: Bridging Attention and Activation via a Joint Game-Decision Lens for Interpretable, Discriminative Visual Representations](cards.md#paper-selection-as-nonlinearity) | 替换注意力和 FFN 时分别核对非线性表达、算力预算与下游复用。 |
| 机器学习基础 | 持续学习 | [Decouple Your Discovery and Memory in Continual Generalized Category Discovery](cards.md#paper-dydm-decouple-discovery-memory) | 把新类发现和长期记忆交给不同分支，避免同一分支被旧类稳定性目标牵制。 |
| 计算机视觉 | 可控视频生成 | [Let Your Image Move with Your Motion! -- Implicit Multi-Object Multi-Motion Transfer](cards.md#paper-fleximmt-object-masked-motion) | 用对象特定的掩码约束条件作用范围，让多个动作可独立组合。 |
| 多模态学习 | 神经符号推理 | [Synthesizing Visual Concepts as Vision-Language Programs](cards.md#paper-vision-language-program-synthesis) | 让模型描述可见事实，再合成可执行逻辑，便于验证规则是否满足正负示例。 |
| 计算机视觉 | 三维重建 | [Learning Scene Coordinate Reconstruction from Unposed Images via Pose Graph Optimization](cards.md#paper-ace-zero-uncertainty-pose-graph) | 把神经场景坐标产生的相对位姿接入图优化，并以几何置信度抑制不可靠约束。 |
| 多模态学习 | 视频理解与检索 | [Follow the Saliency: Supervised Saliency for Retrieval-augmented Dense Video Captioning](cards.md#paper-starc-saliency-segment-retrieve) | 把已标事件边界转成显著性监督，让同一信号协调检索片段与生成提示。 |
| 计算机视觉 | 动作生成 | [Focal-General Diffusion Model with Semantic Consistent Guidance for Sign Language Production](cards.md#paper-fgdm-focal-global-sign-motion) | 将局部骨架细化和全序列协调分配给不同去噪阶段。 |
| 计算机视觉 | 数据策略 | [MatchMask: Mask-Centric Generative Data Augmentation for Label-Scarce Semantic Segmentation](cards.md#paper-matchmask-gradient-probe) | 少量分割标签下，先探测生成器各层对掩码对齐的贡献，再决定适配位置。 |
| 计算机视觉 | 模型架构 | [E-3DPSM: A State Machine for Event-based Egocentric 3D Human Pose Estimation](cards.md#paper-event-driven-pose-state-machine) | 异步观测下融合连续状态增量与绝对位置锚定，并分别测抖动和漂移。 |
| 计算机视觉 | 推理策略 | [The Devil is in Attention Sharing: Improving Complex Non-rigid Image Editing Faithfulness via Attention Synergy](cards.md#paper-synps-stepwise-attention-balance) | 对非刚性编辑按去噪步估计修改需求，并消融位置与语义注意的权衡。 |
| 多模态学习 | 训练策略 | [GTR-Turbo: Merged Checkpoint is Secretly a Free Teacher for Agentic VLM Training](cards.md#paper-gtr-turbo-merged-checkpoint-teacher) | 多轮强化学习中对照内部检查点合并教师与外部教师，记录同任务训练成本。 |
| 计算机视觉 | 训练策略 | [ReMoGen: Real-time Human Interaction-to-Reaction Generation via Modular Learning from Diverse Data](cards.md#paper-remogen-modular-interaction-prior) | 将通用动作先验与独立交互模块分开训练，并核对混合交互和端到端延迟。 |
| 机器人学 | 训练策略 | [PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation](cards.md#paper-palm-affordance-subtask-progress) | 长程操作把交互可供性与子任务进度分开建模，以遗漏、重复和过早结束为诊断。 |
| 多模态学习 | 表征学习 | [Decoupling Vision and Language: Codebook Anchored Visual Adaptation](cards.md#paper-craft-codebook-stable-vision-interface) | 跨语言骨干复用领域视觉编码器时，比较固定离散码本接口与联合重对齐。 |
| 计算机视觉 | 损失函数 | [Reliev3R: Relieving Feed-forward 3D Reconstruction from Multi-View Geometric Annotations](cards.md#paper-reliev3r) | 缺少跨视图标注时，可把相对深度和稀疏对应拆作互补的几何监督。 |
| 多模态学习 | 模型架构 | [OmniZip: Learning a Unified and Lightweight Lossless Compressor for Multi-Modal Data](cards.md#paper-omnizip) | 比较统一可逆标记与模态专用上下文，区分接口复用和概率建模收益。 |
| 计算机视觉 | 模型架构 | [AdapTok: Learning Adaptive and Temporally Causal Video Tokenization in a 1D Latent Space](cards.md#paper-adaptok) | 固定总词元预算时，用前缀质量评分在时间块间分配容量。 |
| 多模态学习 | 评测与诊断 | [Revisiting Visual Corruptions in LVLMs: A Shape-Texture Perspective on Model Failures](cards.md#paper-shape-texture-corruptions) | 把扰动按形状和纹理分层诊断，再与单一对比视图解码比较。 |
| 计算机视觉 | 推理策略 | [ProjFlow: Projection Sampling with Flow Matching for Zero-Shot Exact Spatial Motion Control](cards.md#paper-projflow) | 对线性硬约束先选结构感知的投影度量，再验局部精确性与整体自然度。 |
| 多模态学习 | 推理策略 | [Attend Before Attention: Efficient and Scalable Video Understanding via Autoregressive Gazing](cards.md#paper-autogaze) | 在重视觉骨干前用重建误差预算选多尺度视频区域，并独立核对问答保真。 |
| 多模态学习 | 强化学习方法 | [Diverse Video Generation with Determinantal Point Process-Guided Policy Optimization](cards.md#paper-dpp-grpo) | 对同提示的多样生成采用集合级奖励，并同时验对齐、质量与多样性。 |
| 计算机视觉 | 三维重建 | [Proxy-GS: Unified Occlusion Priors for Training and Inference in Structured 3D Gaussian Splatting](cards.md#paper-proxygs-unified-occlusion-prior) | 可视性代理同时给训练增密和推理剔除提供同一遮挡信号。 |
| 机器学习基础 | 压缩与域适配 | [AnyPcc: Compressing Any Point Cloud with a Single Universal Model](cards.md#paper-anypcc-instance-weight-bits) | 测试时更新可用少量模型参数的码率换取数据码率，评估时应把两者一并计入。 |
| 计算机视觉 | 三维重建 | [SparseCam4D: Spatio-Temporally Consistent 4D Reconstruction from Sparse Cameras](cards.md#paper-sparsecam4d-generative-distortion-fields) | 生成观测用于重建时，可先显式建模它相对真实观测的偏差。 |
| 计算机视觉 | 三维重建 | [ART: Articulated Reconstruction Transformer](cards.md#paper-art-part-slot-articulated-reconstruction) | 把稀疏多状态观测映射到部件槽位，再联合解码部件几何和运动参数。 |
| 计算机视觉 | 高效感知 | [RAVEN: Radar Adaptive Vision Encoders for Efficient Chirp-wise Object Detection and Segmentation](cards.md#paper-raven-calibrated-streaming-early-exit) | 用校准的早退规则处理逐步到达的传感器信号，减少等待完整帧的开销。 |
| 计算机视觉 | 持续学习 | [SAIDO: Generalizable Detection of AI-Generated Images via Scene-Aware and Importance-Guided Dynamic Optimization in Continual Learning](cards.md#paper-saido-scene-experts-continual-detection) | 面向防御检测，可按场景分配专家，并用参数重要性约束持续更新导致的遗忘。 |
| 计算机视觉 | 可控视频生成 | [Generative Video Motion Editing with 3D Point Tracks](cards.md#paper-edit-by-track-paired-3d-correspondence) | 用成对的三维轨迹描述源与目标对应，以深度帮助维持遮挡顺序。 |
| 计算机视觉 | 模型架构 | [Event6D: Event-based Novel Object 6D Pose Tracking](cards.md#paper-eventtrack6d-dual-reconstruction) | 异步事件与低频深度共同跟踪时，对照仅恢复强度和同时恢复深度。 |
| 计算机视觉 | 推理策略 | [Occluded Human Body Capture with Frequency Domain Denoising Prior](cards.md#paper-ocmotion-frequency-domain-prior) | 当时序轨迹被长段遮挡时，对照时域先验和小波域选择，并同时测位置与加速度。 |
| 机器人学 | 训练策略 | [Unsupervised Multi-agent and Single-agent Perception from Cooperative Views](cards.md#paper-ums-cooperative-view-pseudo-labels) | 训练时用更完整的多视角观测为单视角提供伪标签，分距离和单端部署效果复验。 |
| 机器人学 | 推理策略 | [MeanFuser: Fast One-Step Multi-Modal Trajectory Generation and Adaptive Reconstruction via MeanFlow for End-to-End Autonomous Driving](cards.md#paper-meanfuser-continuous-trajectory-prior) | 低延迟生成规划中对照离散候选锚点与单步连续分布，并同时衡量覆盖和速度。 |
| 多模态学习 | 表征学习 | [MedCLIPSeg: Probabilistic Vision-Language Adaptation for Data-Efficient and Generalizable Medical Image Segmentation](cards.md#paper-medclipseg-probabilistic-cross-modal-adapter) | 标注不足的密集预测中，将概率跨模态适配和门控分别消融，并测域外退化。 |
| 多模态学习 | 数据策略 | [CLIP-like Model as a Foundational Density Ratio Estimator](cards.md#paper-clip-foundational-density-ratio) | 数据筛选与重要性加权时，比较对比式图文相似度支持的条件分布差异和普通相似过滤。 |
| 计算机视觉 | 损失函数 | [Edges Compete for Trust: Group Relative Edge Optimization for Building Reconstruction from Point Clouds](cards.md#paper-greo-wireframe) | 把一对一匹配的边监督扩展到全部几何候选，并分验目标分布和置信度稳定性。 |
| 机器人学 | 训练策略 | [CycleManip: Enabling Cycle-based Manipulation via Effective History Perception and Understanding](cards.md#paper-cyclemanip) | 对循环操作同时监督历史阶段与终止判断，单独统计停止准确性。 |
| 计算机视觉 | 训练策略 | [ARMFlow: AutoRegressive MeanFlow for Online 3D Human Reaction Generation](cards.md#paper-armflow) | 自回归动作生成用模型历史训练因果上下文，并对照真值历史下的误差累积。 |
| 多模态学习 | 训练策略 | [Decoupled and Reusable Adaptation for Efficient Cross-Modal Transfer](cards.md#paper-reusable-modal-lora) | 先以无标签目标模态学习可共享适配器，再按下游任务添加小规模适配。 |
| 多模态学习 | 训练策略 | [UnityVideo: Unified Multi-Modal Multi-Task Learning for Enhancing World-Aware Video Generation](cards.md#paper-unityvideo) | 以可调加噪让不同视频任务共用训练目标，再独立检查模态共享收益。 |
| 计算机视觉 | 训练策略 | [ELVIS: Enhance Low-Light for Video Instance Segmentation in the Dark](cards.md#paper-elvis-low-light-vis) | 低照域适配同时模拟帧内和帧间退化，并与独立增强预处理做对照。 |
| 多模态学习 | 评测设计 | [CrossHOI-Bench: A Unified Benchmark for HOI Evaluation across Vision-Language Models and HOI-Specific Methods](cards.md#paper-crosshoi-explicit-negative-evaluation) | 用确认的正负选项缩小缺标对跨范式比较的影响，并单列人物归属与并发动作。 |
| 计算机视觉 | 时序建模 | [Drift-Resilient Temporal Priors for Visual Tracking](cards.md#paper-dtptrack-history-reliability) | 在聚合历史状态之前校准每帧可靠性，并让可信初始模板约束后续远期漂移。 |
| 多模态学习 | 推理优化 | [MuKV: Multi-Grained KV Cache Compression for Long Streaming Video Question-Answering](cards.md#paper-mukv-multigrained-streaming-cache) | 为视频缓存保留多级表示，按问题从粗到细地选择上下文。 |
| 机器人学 | 表征学习 | [Joint-Aligned Latent Action: Towards Scalable VLA Pretraining in the Wild](cards.md#paper-jala-joint-latent-action-alignment) | 以逆动力学和可用动作标签共同对齐潜在动作，使大量弱标签视频能参与策略预训练。 |
| 多模态学习 | 可控图像生成 | [SIGMA: Selective-Interleaved Generation with Multi-Attribute Tokens](cards.md#paper-sigma-selective-attribute-tokens) | 为交错图像来源标注可迁移属性，让模型区分需要保留的风格、内容与主体。 |
| 机器学习基础 | 损失函数与优化 | [TaskForce: Cooperative Multi-agent Reinforcement Learning for Multi-task Optimization](cards.md#paper-taskforce-gradient-gram-policy) | 用梯度 Gram 矩阵和损失变化作反馈，学习多任务更新权重。 |
| 机器学习基础与统计 | 训练策略 | [Flow Matching for Multimodal Distributions](cards.md#paper-mm-fm-source-coupling-codesign) | 多峰潜分布用自适应源分布时，应同步消融模态条件耦合并记录少步采样质量。 |
| 计算机视觉 | 模型架构 | [Spatia: Video Generation with Updatable Spatial Memory](cards.md#paper-spatia-updatable-static-scene-memory) | 长视频生成可把静态场景持久存为几何记忆，并把动态对象一致性分开评测。 |
| 机器学习基础与统计 | 训练策略 | [GaussianMatch: Semi-Supervised Regression with Pseudo-Label Filtering via Multi-View Gaussian Consistency](cards.md#paper-gaussianmatch-multiview-regression-filter) | 连续预测无天然置信度时，用多视图一致性过滤伪标签，并检查过滤和采样的独立作用。 |
| 计算机视觉 | 优化 | [Fresco: Frequency-Spatial Consistent Optimization for Fine-Grained Head Avatar Modeling](cards.md#paper-fresco-frequency-curriculum-uv-consistency) | 多视角外观拟合先稳定低频，再加共享表面纹理一致性和高频细节约束。 |
| 多模态学习 | 评测与诊断 | [Long-RVOS: A Comprehensive Benchmark for Long-term Referring Video Object Segmentation](cards.md#paper-long-rvos-reappearance-evaluation) | 长程指代分割把重现与镜头切换稳定性单测，并分属性、运动和关系描述。 |
| 机器人学 | 模型架构 | [ORV: 4D Occupancy-centric Robot Video Generation](cards.md#paper-orv-occupancy-visual-action-conditioning) | 生成机器人视频时评估中间占据表示是否弥合稀疏动作到稠密像素的差距。 |
| 多模态学习 | 模型架构 | [Curvature-Aware Captioning: Leveraging Geodesic Attention for 3D Scene Understanding](cards.md#paper-curvature-aware-captioning) | 将局部几何关系与全局语义层级分配给不同几何空间，再分别诊断定位和文本质量。 |
| 多模态学习 | 训练策略 | [Personalized Image Descriptions from Attention Sequences](cards.md#paper-deper) | 用辅助注意预测把个人的感知偏好和语言风格共同编码，再适配冻结视觉语言模型。 |
| 计算机视觉 | 损失函数 | [RiskProp: Collision-Anchored Self-Supervised Risk Propagation For Early Accident Anticipation](cards.md#paper-riskprop) | 事件起点标签不稳定时，可用可靠终点做锚，联合软目标传播和阶段性顺序约束。 |
| 计算机视觉 | 模型架构 | [MER-Tracker: Towards High-Speed 3D Point Tracking via Multi-View Event-RGB Hybrid Cameras](cards.md#paper-mer-tracker) | 将不同采样率的视觉输入先对齐到同一三维表示，再保留快模态时间锚点。 |
| 计算机视觉 | 推理策略 | [MorphAny3D: Unleashing the Power of Structured Latent in 3D Morphing](cards.md#paper-morphany3d) | 三维形变可分别融合两端结构信息和相邻帧时序信息，而后对齐姿态。 |
| 多模态学习 | 损失函数 | [THE MORE, THE MERRIER: CONTRASTIVE FUSION FOR HIGHER-ORDER MULTIMODAL ALIGNMENT](cards.md#paper-confu-higher-order) | 保留模态对齐目标，另把成对融合表示与第三模态对比，以测出高阶互补。 |
| 多模态学习 | 评测与诊断 | [Beyond Global Similarity: Multi-Conditional Retrieval for Fine-Grained Cross-Modal Understanding](cards.md#paper-mcmr-conditional-retrieval) | 用必须同时满足多个属性的检索查询，对照不同候选模态可见性。 |
| 多模态学习 | 智能体记忆 | [Experience Transfer for Multimodal LLM Agents in Minecraft Game](cards.md#paper-echo-structured-analogical-experience) | 将过去轨迹归纳成可检索的关系和过程，再通过案例对照适配新任务。 |
| 计算机视觉 | 三维重建 | [SCE-SLAM: Scale-Consistent Monocular SLAM via Scene Coordinate Embeddings](cards.md#paper-sce-slam-coordinate-scale-anchor) | 复用统一尺度的历史场景坐标，以限制局部视觉估计的尺度漂移。 |
| 计算机视觉 | 推理优化 | [HeSS: Head Sensitivity Score for Sparsity Redistribution in VGGT](cards.md#paper-hess-headwise-sparsity-budget) | 将相同注意力预算重新分配给不同敏感度的注意力头。 |
| 机器人学 | 时序建模 | [InterAgent: Physics-based Multi-agent Command Execution via Diffusion on Interaction Graphs](cards.md#paper-interagent-multistream-interaction-context) | 对本体状态、外部观测和动作分流建模，检验何时显式跨角色关系有帮助。 |
| 多模态学习 | 持续学习 | [Towards Dynamic Modality Alignment in Multimodal Continual Learning](cards.md#paper-dagr-layerwise-modality-alignment) | 将模态配对看作随深度及任务改变的关系图，并对关系演化施加正则。 |
| 机器人学 | 测试时适配 | [Test-Time Perturbation Tuning with Delayed Feedback for Vision-Language-Action Models](cards.md#paper-pdf-delayed-feedback-perturbation) | 用迟到的反馈回顾动作分数，并按当前不确定度调节测试时额外计算。 |
| 机器人学 | 主动感知 | [AREA3D: Active Reconstruction Agent with Unified Feed-Forward 3D Perception and Vision-Language Guidance](cards.md#paper-area3d-decoupled-view-uncertainty) | 用独立模块估计视点不确定性，再组合前馈几何和视觉语言语义引导。 |
| 计算机视觉 | 训练策略 | [Towards High-resolution and Disentangled Reference-based Sketch Colorization](cards.md#paper-sketch-colorization-dual-branch-gram) | 参考图与目标结构不一致时，将匹配和不匹配样本分支建模，再约束两路特征统计。 |
| 计算机视觉 | 训练策略 | [ExpoCM: Exposure-Aware One-Step Generative Single-Image HDR Reconstruction](cards.md#paper-expocm-degradation-aware-consistency) | 单步逆问题可按空间退化强度设计一致性训练轨迹，分别检验不同退化区间的恢复。 |
| 机器人学 | 表征学习 | [Open-world Hand-Object Interaction Video Generation Based on Structure and Contact-aware Representation](cards.md#paper-hoi-contact-structure-supervision) | 交互视频生成可把接触、遮挡和整体结构作为辅助监督，并和其他交互表示做隔离对照。 |
| 多模态学习 | 表征学习 | [LaMoGen: Language to Motion Generation Through LLM-Guided Symbolic Inference](cards.md#paper-lamogen-symbolic-motion-interface) | 细粒度文字到动作可先生成可检查的身体部位符号，再由专门模型解码为轨迹。 |
| 计算机视觉 | 训练策略 | [DNF-SR: Dual-Input and Negative-Aware Feature Fine-Tuning for Real-World Image Super-Resolution](cards.md#paper-dnfsr-clean-noisy-dual-conditioning) | 低质量条件需匹配生成器输入分布时，保留原条件并加入带噪副本以区分先验适配与内容丢失。 |
| 机器人学 | 模型架构 | [Unifying Language-Action Understanding and Generation for Autonomous Driving](cards.md#paper-linkvla-shared-action-language-codebook) | 用共享离散接口联合动作与语言，另以理解生成双任务检验控制语义对齐。 |
| 机器人学 | 推理策略 | [ProFocus: Proactive Perception and Focused Reasoning in Vision-and-Language Navigation](cards.md#paper-profocus-missing-evidence-query) | 导航代理先列出当前决策缺失的视觉证据，再请求对应局部观察，以分离感知开销与推理表现。 |
| 计算机视觉 | 模型架构 | [PackUV: Packed Gaussian UV Maps for 4D Volumetric Video](cards.md#paper-packuv) | 把动态三维基元打包成保结构的二维图集，用现成视频编解码链分开测成本和画质。 |
| 机器人学 | 训练策略 | [Recovering Physically Plausible Human-Object Interactions from Monocular Videos](cards.md#paper-adaptive-hoi-refinement) | 将运动估计用于物理策略时，按帧信息量和可靠性动态选监督。 |
| 多模态学习 | 评测与诊断 | [Ego2Web: A Web Agent Benchmark Grounded in Egocentric Videos](cards.md#paper-ego2web) | 把第一视角所见物体与后续网页任务绑定，再分别衡量任务成功与自动评分一致性。 |
| 机器学习基础与统计 | 推理策略 | [Beyond Fixed Formulas: Data-Driven Linear Predictor for Efficient Diffusion Models](cards.md#paper-l2p-diffusion) | 缓存加速时先实测历史特征可预测性，再对照固定公式和少量轨迹拟合。 |
| 计算机视觉 | 损失函数 | [Diversity over Uniformity: Rethinking Representation in Generated Image Detection](cards.md#paper-diverse-forgery-representation) | 检测器应分开检验冗余线索抑制和任务无关成分约束，并用未见生成器验泛化。 |
| 多模态学习 | 推理策略 | [LaSM: Layer-wise Scaling Mechanism for Defending Pop-up Attack on GUI Agents](cards.md#paper-lasm-gui-defense) | 评估 GUI 助手的防御时，核对逐层任务证据关注，并同步监测正常任务效用。 |
| 机器人学 | 推理策略 | [AGiLe: Learning Robust Long-Horizon Manipulation via Affordance-Grounded Bidirectional Latent Planning](cards.md#paper-agile-bidirectional-planning) | 长时操作中从最终目标倒推子目标，再由前向可达性评估拒绝难以执行的计划。 |
| 多模态学习 | 训练数据 | [Unlocking Strong Supervision: A Data-Centric Study of General-Purpose Audio Pre-Training Methods](cards.md#paper-audio-strong-supervision-objective-tradeoffs) | 先比较音频标注覆盖与质量，再按下游偏重的能力选择预训练目标。 |
| 计算机视觉 | 深度估计 | [UniDAC: Universal Metric Depth Estimation for Any Camera](cards.md#paper-unidac-local-metric-scale) | 把相对深度与空间变化的度量尺度分开预测，以应对不同相机投影。 |
| 计算机视觉 | 内容溯源 | [MaxMark: High-Capacity Diffusion-Native Watermarking via Robust and Invertible Latent Embedding](cards.md#paper-maxmark-latent-distribution-preservation) | 用可逆分布变换在提高水印容量时约束生成潜变量的分布变化。 |
| 多模态学习 | 表征学习 | [See What I Mean: Aligning Vision and Language Representations for Video Fine-grained Object Understanding](cards.md#paper-swim-training-only-mask-grounding) | 只在训练期用掩码对齐对象名词的注意力，推理仍可只输入自然语言。 |
| 多模态学习 | 推理优化 | [StreamingTOM: Streaming Token Compression for Efficient Video Understanding](cards.md#paper-streamingtom-prefill-and-cache-bounds) | 同步限制因果流式输入的每帧预算和可访问历史缓存。 |
| 机器人学 | 表征学习 | [Local Motion Matters: A Deconstruct-Recompose Paradigm for Reinforcement Learning Pre-training from Videos](cards.md#paper-drp-local-motion-recomposition) | 从视频抽取局部运动再重组为可适配下游动作空间的动态表征。 |
| 多模态学习 | 评测设计 | [VirtueBench: Evaluating Trustworthiness under Uncertainty in Long Video Understanding](cards.md#paper-virtuebench-evidence-conditioned-abstention) | 评估时根据模型实际收到的帧区分可答和不可答，单独衡量拒答。 |
| 机器人学 | 模型架构 | [Haptic Neural Fields: Bringing Tactile Interactions to 3D Rendered Scenes](cards.md#paper-haptic-fields-action-conditioned-response) | 让触觉场同时依赖场景几何和交互动态，并分别验证材料及动作可辨性。 |
| 机器人学 | 训练策略 | [Goal Force: Teaching Video Models To Accomplish Physics-Conditioned Goals](cards.md#paper-goal-force-physical-goal-conditioning) | 物理目标难以写成文本或指定终帧时，用直接的作用条件，并单测条件遵从与视觉质量。 |
| 计算机视觉 | 表征学习 | [Selectively Extracting and Injecting Visual Attributes into Text-to-Image Models](cards.md#paper-reference-attribute-distilled-residual-embeddings) | 参照图只提供单一属性时，用目标嵌入和剩余嵌入分离目标特征与伴随信号。 |
| 计算机视觉 | 训练策略 | [LoFA: Learning to Predict Personalized Prior for Fast Adaptation of Visual Generative Models](cards.md#paper-lofa-relative-adaptation-prior) | 快速个性化时先预测相对基座的适配参数分布，再据此产生更新。 |
| 机器人学 | 训练策略 | [VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling](cards.md#paper-vla-viewpoint-visual-feature-recalibration) | 新视点下先冻结动作网络，只用一次示范重新校准视觉词元，再决定是否端到端微调。 |
| 计算机视觉 | 推理策略 | [ResCa: Residual Caching for Diffusion Transformers Acceleration](cards.md#paper-resca-proxy-token-residual-caching) | 扩散加速可让同轨迹词元共享一个代理的最新残差，而不是全部使用旧缓存。 |
| 多模态学习 | 训练策略 | [Composing Concepts from Images and Videos via Concept-prompt Binding](cards.md#paper-bind-compose) | 将可复用概念绑定到对应提示词，并给无关细节独立的吸收通道。 |
| 计算机视觉 | 训练策略 | [LogCD: Local-to-global Consistency Distillation for Few-step Image Generation](cards.md#paper-logcd) | 少步蒸馏先拟合局部一致性，再对推理路径作全局一致校正。 |
| 多模态学习 | 推理策略 | [Universal Guideline-Driven Image Clustering via a Hybrid LLM Agent](cards.md#paper-guideline-clustering-agent) | 指南约束图像聚类时，先构造概念代理，再只对有歧义的邻接关系调用大模型。 |
| 计算机视觉 | 模型架构 | [GOR-IS: 3D Gaussian Object Removal In the Intrinsic Space](cards.md#paper-gor-is) | 三维内容修补时分别重建材质与光传输，分开验跨视角一致性和表面外观。 |
| 多模态学习 | 评测与诊断 | [Understanding the Role of Hallucination in Reinforcement Post-Training of Multimodal Reasoning Models](cards.md#paper-hallucination-as-cue) | 多模态强化后训练应用遮蔽必要证据的配对对照，检查涨分能否归因于视觉推理。 |
| 多模态学习 | 推理策略 | [QuietPrune: Query-Guided Early Token Pruning for Vision-Language Models](cards.md#paper-quietprune) | 早剪视觉词元可先引入问题语义，再与等剪枝率的晚剪对照延迟和精度。 |
| 多模态学习 | 损失函数 | [b-CLIP: Text-Conditioned Contrastive Learning for Multi-Granular Vision-Language Alignment](cards.md#paper-beta-clip) | 让句子和短语查询从同一图像动态池化局部证据，并独立保留整图匹配。 |
| 计算机视觉 | 推理优化 | [From Sketch to Fresco: Efficient Diffusion Transformer with Progressive Resolution](cards.md#paper-fresco-consistent-progressive-resolution) | 让多阶段分辨率采样共享最终目标，并优先细化尚未收敛的区域。 |
| 多模态学习 | 模型对齐 | [DSO: Direct Steering Optimization for Bias Mitigation](cards.md#paper-dso-fairness-capability-steering) | 直接用公平性和能力联合反馈学习激活变换，并在推理时调节取舍。 |
| 多模态学习 | 损失函数与优化 | [From Pixel to Precision: Enhancing Handwritten Mathematical Expression Recognition with Image-Level Reward](cards.md#paper-impo-rendered-structure-reward) | 若文本序列与真实产物不一一对应，可在渲染后的结构上定义反馈。 |
| 多模态学习 | 模型选择 | [Rethinking Model Selection in VLM Through the Lens of Gromov-Wasserstein Distance](cards.md#paper-gw-vision-encoder-selection) | 用跨模态表示几何相似性筛选视觉骨干，在完整训练前比较接入成本。 |
| 机器人学 | 强化学习 | [TSTM: Temporal Segmentation for Task-relevant Mask in Visual Reinforcement Learning Generalization](cards.md#paper-tstm-temporal-task-relevance-mask) | 用历史视觉信息帮助识别与策略相关的区域，并用轻量学生控制推理成本。 |
| 多模态学习 | 损失函数与优化 | [Cross-modal Identity Mapping: Minimizing Information Loss in Modality Conversion via Reinforcement Learning](cards.md#paper-cim-caption-information-retrieval-reward) | 用描述反向检索相关图像，作为跨模态转换信息保留的弱反馈。 |
| 多模态学习 | 检索增强 | [CC-VQA: Conflict- and Correlation-Aware Method for Mitigating Knowledge Conflict in Knowledge-Based Visual Question Answering](cards.md#paper-ccvqa-visual-evidence-conflict) | 当检索证据与模型知识冲突时，用图像相关性参与识别冲突和过滤。 |
| 计算机视觉 | 推理策略 | [Ghosts in the Point Clouds: De-glaring LiDAR in the Transient Domain](cards.md#paper-transient-glare-calibrated-operator) | 将传感器内部伪影建模为可标定的暂态算子，在生成几何前消除其影响。 |
| 机器人学 | 模型架构 | [ModularAgent: A Task-Aware Modular Framework for Joint Optimization of Multimodal Large Language Models and World Models](cards.md#paper-modularagent-bidirectional-semantic-dynamics) | 联用语义模型和动力学模型时，分别消融语义到动力学、状态反馈到语义两个方向。 |
| 机器学习基础与统计 | 训练策略 | [Bridging Domains through Subspace-Aware Model Merging](cards.md#paper-score-shared-singular-subspace-merging) | 合并不同数据域微调模型时，先核对更新子空间冲突，并在留一域上验证共享基。 |
| 机器人学 | 训练策略 | [Spatial-Aware VLA Pretraining through Visual-Physical Alignment from Human Videos](cards.md#paper-vipa-vla-human-video-3d-pretraining) | 在机器人策略学习前用人体视频提供三维视觉和动作监督，并分单视点及多视点验收。 |
| 计算机视觉 | 优化 | [PnP-CM: Consistency Models as Plug-and-Play Priors for Inverse Problems](cards.md#paper-pnp-cm-consistency-proximal-prior) | 把预训练一致性模型作为即插即用的恢复先验，分别检查数据一致性和网络调用成本。 |
| 计算机视觉 | 模型架构 | [Hist2Style: Histogram-Guided Stylization with Bilateral Grids](cards.md#paper-hist2style-editable-histogram-bilateral-grid) | 若只需高速外观调整，将编辑限制为分区局部仿射颜色变换，并给可编辑的直方图条件。 |
| 计算机视觉 | 评测与诊断 | [Back to the Feature: Explaining Video Classifiers with Video Counterfactual Explanations](cards.md#paper-back-to-the-feature) | 解释视频分类时联合衡量预测变化、时间一致性与可理解性。 |
| 机器人学 | 模型架构 | [Planning in 8 Tokens: A Compact Discrete Tokenizer for Latent World Model](cards.md#paper-compact-world-tokenizer) | 为决策时规划单独设词元预算，并同时验重建、规划成功及端到端耗时。 |
| 计算机视觉 | 模型架构 | [Mamba Learns in Context: Structure-Aware Domain Generalization for Multi-Task Point Cloud Understanding](cards.md#paper-structure-aware-mamba) | 点云序列化可用结构连续性替代绝对坐标顺序，并跨域测对局部缺失的敏感性。 |
| 多模态学习 | 训练策略 | [Vision-Speech Models: Teaching Speech Models to Converse about Images](cards.md#paper-moshivis) | 以少量图像语音配对补充更丰富的图文监督，并按话题动态打开视觉条件。 |
| 计算机视觉 | 模型架构 | [Geometric-Photometric Event-based 3D Gaussian Ray Tracing](cards.md#paper-gpert-event-rays) | 非同步传感渲染可让快速的几何查询与较慢的辐射估计分别采样。 |
| 计算机视觉 | 损失函数 | [MatchED: Crisp Edge Detection Using End-to-End, Matching-based Supervision](cards.md#paper-matched-crisp-edges) | 若希望输出细边界，可把唯一对应关系放进训练监督，再检验省略细化后处理的表现。 |
| 计算机视觉 | 训练策略 | [Robust Promptable Video Object Segmentation](cards.md#paper-moga-robust-pvos) | 可提示视频分割的域适配按记忆对象调节参数容量，并分别验证退化与时序一致性。 |
| 计算机视觉 | 三维匹配 | [SAG-GNN: Semantic-Aware Guided GNN for Descriptor-Free 2D-3D Matching](cards.md#paper-saggnn-compact-semantic-correspondence) | 以低维类别概率辅助几何匹配，缓解无描述符方法的对应歧义。 |
| 机器学习基础 | 不确定性估计 | [Evidential Transformation Network: Turning Pretrained Models into Evidential Models for Post-hoc Uncertainty Estimation](cards.md#paper-etn-posthoc-dirichlet-logits) | 在冻结模型外学习样本相关的证据映射，避免重新训练骨干。 |
| 多模态学习 | 弱监督定位 | [Reasoning-Driven Anomaly Detection and Localization with Image-Level Supervision](cards.md#paper-real-reasoning-attention-localization) | 以与异常有关的推理词元为索引，从跨模态注意力生成像素热图。 |
| 多模态学习 | 损失函数与优化 | [DEVA: Fine-tuning Multimodal Large Language Models for Visual Perception Tasks](cards.md#paper-deva-perception-rl-diversity-reward) | 诊断视觉强化微调中的探索收缩，并在训练目标和奖励聚合上同时保留多样性。 |
| 计算机视觉 | 可控图像生成 | [SplitFlux: Learning to Decouple Content and Style from a Single Image](cards.md#paper-splitflux-layerwise-content-style) | 按层识别内容与风格作用，再把两类更新限制在不同的层段。 |
| 计算机视觉 | 三维重建 | [BA-GS: Bayesian Adaptive Gaussian Splatting for SFM-Free 3D Reconstruction](cards.md#paper-bags-global-local-uncertainty) | 将云团级初始化的不确定性与基元级更新的不确定性分层处理。 |
| 计算机视觉 | 推理策略 | [CFG-Ctrl: Control-Based Classifier-Free Diffusion Guidance](cards.md#paper-cfg-ctrl-nonlinear-guidance) | 生成引导增益过高时，把条件差作为控制误差并比较非线性替代方案。 |
| 计算机视觉 | 模型架构 | [VGGT-Segmentor: Geometry-Enhanced Cross-View Segmentation](cards.md#paper-vggt-object-attention-mask-refinement) | 跨视角局部投影不可靠时，先借用对象级对齐，再由掩码解码器恢复像素细节。 |
| 多模态学习 | 表征学习 | [FlowComposer: Composable Flows for Compositional Zero-Shot Learning](cards.md#paper-flowcomposer-primitive-composition) | 开放组合识别可在嵌入空间显式组合属性和物体变换。 |
| 计算机视觉 | 模型架构 | [Generalizable Sparse-View 3D Reconstruction from Unconstrained Images](cards.md#paper-genwildsplat-canonical-geometry-appearance) | 稀疏无位姿重建将规范空间几何与目标光照适配分开，以降低逐场景优化依赖。 |
| 计算机视觉 | 模型架构 | [XPaintNet: An eXtreme Lightweight Framework for Stereoscopic Conversion without Inpainting Network](cards.md#paper-xpaintnet-bidirectional-warp-fusion) | 实时跨视角合成可在两个方向分别变形，再按像素融合替代重型补洞。 |
| 多模态学习 | 推理策略 | [MoDES: Accelerating Mixture-of-Experts Multimodal Large Language Models via Dynamic Expert Skipping](cards.md#paper-modes-layer-token-expert-skipping) | 多模态专家跳过时同时考虑层全局重要性和词元局部路由，并分别评估视觉任务。 |
| 多模态学习 | 训练策略 | [Why Does RL Generalize Better Than SFT? A Data-Centric Perspective on VLM Post-Training](cards.md#paper-dc-sft-difficulty-curated-ood) | 比较强化与监督微调的泛化前，先控制样本难度构成，并分开评内外分布。 |
| 机器人学 | 模型架构 | [Cross-Hand Latent Representation for Vision-Language-Action Models](cards.md#paper-xl-vla) | 跨机械手共享动作潜空间，并按目标手验证潜变量能否被可靠解码。 |
| 计算机视觉 | 训练策略 | [NoOVD: Novel Category Discovery and Embedding for Open-Vocabulary Object Detection](cards.md#paper-noovd) | 开放词表检测同时诊断候选召回与分类错误，减轻学习时把未标注物体当背景的问题。 |
| 计算机视觉 | 模型架构 | [Space-Time Forecasting of Dynamic Scenes with Motion-aware Gaussian Grouping](cards.md#paper-mogaf-motion-groups) | 先按运动一致性组织动态场景的基元，再以组为单位做超出观测窗的外推。 |
| 多模态学习 | 训练策略 | [POGA: Paraphrased and Oppositional Graph Alignment for Fine-Grained Cross-Modal Retrieval](cards.md#paper-poga-graph-alignment) | 细粒度检索同时使用保持事实的改写与改变局部事实的难负例，显式监督关系结构。 |
| 计算机视觉 | 训练策略 | [PatchAlign3D: Local Feature Alignment for Dense 3D Shape Understanding](cards.md#paper-patchalign3d) | 用二维教师的局部区域线索预训练三维补丁表示，推理时只运行点云编码器。 |
| 计算机视觉 | 模型架构 | [Nonlinear Color Transfer via Learnable Bezier Flows](cards.md#paper-bezier-color-flows) | 将固定直线改为可学习曲线路径，并用重建及感知指标分别检验收益。 |
| 机器人学 | 损失函数 | [TACO: Task-Aware Contrastive Learning for Joint LiDAR Localization and 3D Object Detection](cards.md#paper-taco-lidar) | 激光雷达定位和检测共享骨干时，用任务对比约束分离静态地理与物体特征。 |
| 多模态学习 | 评测设计 | [WiseEdit: Benchmarking Cognition- and Creativity-Informed Image Editing](cards.md#paper-wiseedit-failure-stage-evaluation) | 将知识驱动的编辑能力按感知、解释与创意分阶段考查。 |
| 多模态学习 | 音视频生成 | [UniAVGen: Unified Audio and Video Generation with Asymmetric Cross-Modal Interactions](cards.md#paper-uniavgen-asymmetric-timed-fusion) | 音画模态分开建模，再对齐时序后按方向做交互。 |
| 多模态学习 | 推理优化 | [Interpretable Prompts made Edit-Friendly: Token-to-Token Similarity Reduction in dLLMs for Edit-Friendly Hard Prompt Inversion](cards.md#paper-editable-hard-prompt-token-decorrelation) | 为后续词元编辑显式约束反演提示的词元冗余，并分别衡量重建和可编辑性。 |
| 计算机视觉 | 表征学习 | [Egocentric Visibility-Aware Human Pose Estimation](cards.md#paper-evapose-visibility-conditioned-keypoints) | 将可见和不可见关键点区分建模和评估，避免遮挡监督压低有证据的定位。 |
| 多模态学习 | 训练策略 | [CoLoGen: Progressive Learning of Concept-Localization Duality for Unified Image Generation](cards.md#paper-cologen-staged-concept-localization) | 先培养概念与定位子能力，再逐步接入条件和复杂指令，缓解共享表征冲突。 |
| 计算机视觉 | 三维匹配 | [Topology-aware Feature Propagation for Unsupervised Non-rigid Point Cloud Correspondence](cards.md#paper-topology-propagation-deformable-correspondence) | 用可学习拓扑替代欧氏邻接，减少非刚性变形下的跨表面错误传播。 |
| 多模态学习 | 评测设计 | [LifeEval: A Multimodal Benchmark for Assistive AI in Egocentric Daily Life Tasks](cards.md#paper-lifeeval-online-assistive-interaction) | 将任务导向、多轮互动和当前可见信息共同纳入第一视角助手评测。 |
| 计算机视觉 | 模型架构 | [FSFSplatter: Geometrically Accurate Reconstruction with Free Sparse-view Images within 2 minutes](cards.md#paper-fsfsplatter-geometric-pruning-sparse-views) | 稀疏三维重建可先从多视图联合初始化，再按实际贡献修剪漂浮基元，分开验几何和新视图。 |
| 多模态学习 | 评测与诊断 | [Visual Grounding for Object Questions](cards.md#paper-vgoq-graded-visual-evidence) | 将物体问题建模为视觉证据定位，并允许按可见证据充分程度区分样本。 |
| 计算机视觉 | 训练策略 | [HySeg: Learning Generative Priors for Structure-Aware Remote Sensing Segmentation](cards.md#paper-hyseg-generative-topology-prior) | 给判别分割器加入可学习结构先验时，用拓扑指标和区域重叠一起消融。 |
| 机器人学 | 模型架构 | [R4Det: 4D Radar-Camera Fusion for High-Performance 3D Object Detection](cards.md#paper-r4det-relative-absolute-depth-fusion) | 稀疏测距融合时对照绝对深度和相对深度，并单测低回波与姿态缺失。 |
| 机器学习基础与统计 | 数据策略 | [Decision Boundary-aware Generation for Long-tailed Learning](cards.md#paper-dbg-long-tail-boundary-aware-generation) | 长尾增强应检查合成样本是否加剧类别边界重叠，优先评估有判别力的近边界数据。 |
| 多模态学习 | 推理策略 | [When CLIP Sees More, It Fights Back Harder: Multi-View Guided Adaptive Counterattacks for Test-Time Adversarial Robustness](cards.md#paper-mac-defensive-multiview-adaptive-fusion) | 视觉模型鲁棒部署时比较单视图硬选择和根据可靠性加权的多视图聚合。 |
| 机器学习基础与统计 | 训练策略 | [Attribution-Guided Model Rectification of Unreliable Neural Network Behaviors](cards.md#paper-attribution-guided-defensive-layer-selection) | 修复网络已知不可靠行为时，先验证归因定位的可编辑层，再衡量干净任务保留。 |
| 计算机视觉 | 模型架构 | [DeCo: Frequency-Decoupled Pixel Diffusion for End-to-End Image Generation](cards.md#paper-deco-pixel-diffusion) | 像素扩散可让主干专注低频语义，再用轻量条件解码器恢复细节。 |
| 机器学习基础与统计 | 训练策略 | [Fine-Tuning Impairs the Balancedness of Foundation Models in Long-tailed Personalized Federated Learning](cards.md#paper-fedpurel) | 长尾联邦微调需以冻结零样本分布为对照，检查共享权重是否把头部偏差传给个体。 |
| 多模态学习 | 模型架构 | [Modeling Cross-vision Synergy for Unified Large Vision Model](cards.md#paper-polyv-cross-vision) | 统一图像、视频、三维骨干时，用模态专长和交互同时检验共享收益。 |
| 计算机视觉 | 模型架构 | [D2FANet: Enhancing Video Object Detection with Dual-Domain Feature Aggregation Network](cards.md#paper-d2fanet) | 视频特征融合时同时对照时空区域证据与频域运动线索。 |
| 计算机视觉 | 推理策略 | [Radar-Guided Polynomial Fitting for Metric Depth Estimation](cards.md#paper-polar-radar-depth) | 单目估计已有局部结构时，用稀疏公制锚非线性校准不同深度段。 |
| 计算机视觉 | 优化 | [QuadSync: Quadrifocal Tensor Synchronization via Tucker Decomposition](cards.md#paper-quadsync) | 多视几何可先同步固定低秩的高阶关系，再结合不同视图阶数的观测。 |
| 机器学习基础与统计 | 优化 | [A Polynomial Chaos Framework for Causal Discovery in Nonlinear Uncertain Systems](cards.md#paper-polynomial-chaos-causal-discovery) | 非线性结构方程可表示异质噪声，并在稀疏假设下评估可识别性。 |
| 高效深度学习 | 数据筛选 | [LoPrune: Efficient Data Pruning for LoRA-Based Fine-Tuning of Vision Transformer](cards.md#paper-loprune-trainable-subspace-alignment) | 按可训练子空间估计样本价值，适用于低秩适配的选样。 |
| 机器学习 | 校准与鲁棒性 | [Enhancing Out-of-Distribution Detection with Extended Logit Normalization](cards.md#paper-elogitnorm-feature-distance-calibration) | 决定在沿用现有 OOD 后处理时是否替换训练目标。 |
| 机器学习 | 评测设计 | [Bridging Domain Expertise and Generalization for Performance Estimation](cards.md#paper-frap-calibrated-reference-performance-estimation) | 为无标签部署监测提供双模型准确率估计。 |
| 多模态学习 | 记忆与工具调用 | [VideoARM: Agentic Reasoning over Hierarchical Memory for Long-Form Video Understanding](cards.md#paper-videoarm-hierarchical-multimodal-memory) | 将长序列理解改为按需工具调用，对 Agent 的观察和记忆预算选择有直接参考。 |
| 生成模型 | 参数高效适配 | [Test-Time Instance-Specific Parameter Composition: A New Paradigm for Adaptive Generative Modeling](cards.md#paper-composer-one-shot-parameter-adaptation) | 在迭代生成之前一次性合成输入相关的参数更新。 |
| 机器人学 | 自监督表征 | [LA-Pose: Latent Action Pretraining Meets Pose Estimation](cards.md#paper-la-pose-inverse-dynamics-features) | 用逆动力学的动作表征替代部分三维监督来估计位姿。 |
| 计算机视觉 | 推理策略 | [VVS: Accelerating Speculative Decoding for Visual Autoregressive Generation via Partial Verification Skipping](cards.md#paper-vvs-visual-speculative-verification-skipping) | 视觉自回归中把目标网络校验安排和草稿计算分开优化，联验质量与实际耗时。 |
| 机器学习基础与统计 | 评测与诊断 | [Beyond Top Activations: Efficient and Reliable Crowdsourced Evaluation of Automated Interpretability](cards.md#paper-mgis-interpretability-crowd-evaluation) | 评估单元解释不要只展示最大激活样本，改用信息驱动抽样并实测人评预算。 |
| 计算机视觉 | 数据策略 | [Balanced Dataset Distillation via Modeling Multiple Visual Pattern Distribution](cards.md#paper-bps-balanced-visual-pattern-coresets) | 少图蒸馏按类内多模式同时保留典型和边缘样本，而非只设每类配额。 |
| 计算机视觉 | 模型架构 | [NOVA: Sparse Control, Dense Synthesis for Pair-Free Video Editing](cards.md#paper-nova-sparse-keyframe-dense-source-conditioning) | 无配对视频编辑将稀疏编辑意图与稠密源视频运动及纹理条件分开。 |
| 计算机视觉 | 训练策略 | [FE2E: From Editor to Dense Geometry Estimator](cards.md#paper-fe2e-editor-initialization-dense-geometry) | 稠密几何估计先比较图像编辑与纯生成骨干的初始化，而不只比微调配方。 |
| 多模态学习 | 训练策略 | [Adaptive Confidence Regularization for Multimodal Failure Detection](cards.md#paper-acr-cross-modal-confidence-degradation) | 把融合置信度低于单模态分支作为故障信号，并用风险覆盖曲线验证。 |
| 机器学习基础与统计 | 训练策略 | [ACE-Merging: Data-Free Model Merging with Adaptive Covariance Estimation](cards.md#paper-ace-merging-covariance-from-task-updates) | 无数据合并可从微调更新估计任务统计，再以协方差归一检查跨任务干扰。 |
| 机器学习基础与统计 | 模型架构 | [Hyperbolic Busemann Neural Networks](cards.md#paper-busemann-networks) | 层级表示中可替换为基于 Busemann 函数的分类和全连接层，并同步衡量精度与复杂度。 |
| 计算机视觉 | 训练策略 | [ChimeraLoRA: Multi-Head LoRA-Guided Synthetic Datasets](cards.md#paper-chimeralora) | 少样本合成可把共享类先验和单样本细节分层建模，再组装生成。 |
| 计算机视觉 | 模型架构 | [TTAPFormer: Robust Arbitrary Point Tracking via Transient Asynchronous Fusion of Frames and Events](cards.md#paper-tapformer-asynchronous) | 异步视觉融合可让事件更新帧间状态，并按局部可靠性调节模态权重。 |
| 多模态学习 | 评测与诊断 | [CREval: An Automated Interpretable Evaluation for Creative Image Manipulation under Complex Instructions](cards.md#paper-creval-qa-editing) | 复杂编辑评测将要求拆成可追溯的问答，并用人工偏好核对自动分数。 |
| 计算机视觉 | 模型架构 | [FVAR: Next-Focus Prediction for Visual Autoregressive Modeling](cards.md#paper-fvar-next-focus) | 自回归视觉金字塔用逐步去模糊代替直接下采样，单独建模高频残差。 |
| 计算机视觉 | 优化 | [Landscape-Awareness for Geometric View Diffusion Model](cards.md#paper-landscape-aware-view-diffusion) | 扩散模型做双视图姿态优化时显式诊断对称引起的局部极小，再调整搜索目标。 |
| 多模态学习 | 强化学习方法 | [MedGRPO: Multi-Task Reinforcement Learning for Heterogeneous Medical Video Understanding](cards.md#paper-medgrpo-cross-dataset-reward) | 异质任务联合强化训练时，先校准各数据集的奖励中位点，再分数据监测崩溃。 |
| 多模态学习 | 推理策略 | [One Algorithm to Align Them All](cards.md#paper-rectified-flow-paired-alignment) | 同骨干生成结构配对样本时，可联合输运潜空间中的关联表示，再同时评结构与质量。 |
| 计算机视觉 | 表征学习 | [Beyond [CLS] Token: Query-Driven Token-Level Forgery Purification for Generalizable Deepfake Detection](cards.md#paper-qtfp-local-patch-evidence-queries) | 当预训练全局表示掩盖稀疏局部线索时，用独立查询重新聚合 patch 证据。 |
| 三维视觉 | 表征学习 | [LoST: Level of Semantics Tokenization for 3D Shapes](cards.md#paper-lost-semantic-prefix-tokenization) | 以语义而非空间细节决定 token 顺序，使短前缀也能恢复完整对象。 |
| 机器人学 | 规划与记忆 | [Predict Before You Explore: Predictive Planning with Specialized Memory for Embodied Question Answering](cards.md#paper-pred-eqa-prediction-correction-memory) | 将长期空间先验与当前问题证据拆开，让预测落空成为明确的重规划信号。 |
| 生成模型 | 条件生成 | [RenderFlow: Single-Step Neural Rendering via Flow Matching](cards.md#paper-renderflow-sparse-keyframe-guidance) | 用少量高质量关键帧指导确定性的一步生成，权衡精度和推理延迟。 |
| 三维视觉 | 高效注意力 | [iLRM: An Iterative Large 3D Reconstruction Model](cards.md#paper-ilrm-iterative-compact-scene-tokens) | 将跨视角场景状态与输入分离，用分解注意力持续注入细节。 |
| 多模态学习 | 动态推理 | [Adaptive Depth Lightweight RGB-T Tracking with Holistic Token Routing](cards.md#paper-adtrack-holistic-token-early-exit) | 把退出置信度与跨模态压缩分开设计，可迁移到边缘多传感器推理。 |
| 多模态学习 | 训练策略 | [Towards an Incremental Unified Multimodal Anomaly Detection: Augmenting Multimodal Denoising From an Information Bottleneck Perspective](cards.md#paper-incremental-multimodal-anomaly-denoising) | 增量异常检测先对照单模态、朴素融合及去冗余融合，再判断遗忘来自何处。 |
| 多模态学习 | 训练策略 | [Unified Multimodal Models as Auto-Encoders](cards.md#paper-unified-grpo-text-as-latent) | 统一理解与生成的后训练可把文本当中间表示，用图文往返保持结构来验两侧。 |
| 机器人学 | 推理策略 | [Test-Time 3D Occupancy Prediction](cards.md#paper-tt-occ-gaussian-runtime-voxelization) | 分辨率或类别变化时以连续场景基元存储占据，并将体素分辨率留到测试时指定。 |
| 机器学习基础与统计 | 推理策略 | [PhaseWin Search Framework Enable Efficient Object-Level Interpretation](cards.md#paper-phasewin-coarse-to-fine-attribution) | 在区域归因的前向预算有限时，先粗筛再在保留窗口精搜，并量化与完整贪心的差距。 |
| 机器学习基础与统计 | 训练策略 | [DGS: Dual Gradient and Semantic-Shift Guided Low-Rank Adaptation for Class Incremental Learning](cards.md#paper-dgs-soft-projected-gradient-lora) | 增量低秩适配比较硬投影与原梯度和投影梯度的插值，并同时测遗忘与末轮性能。 |
| 多模态学习 | 训练策略 | [Vision-Language Model Guided Source-Free Domain Adaptation via Optimal Transport](cards.md#paper-vsfot-vision-language-transport-guidance) | 无源数据适配把源原型、目标表示和语言语义联合匹配，避免直接强化初始伪标签。 |
| 计算机视觉 | 数据策略 | [Learning to Generate Highly Dynamic Videos using Synthetic Motion Data](cards.md#paper-dynavid-synthetic-motion-without-appearance) | 视频动态样本稀少时，将合成运动用于控制信号，外观仍由真实数据提供。 |
| 计算机视觉 | 训练策略 | [Adapting Lightweight Image-based Counting Models for Video Crowd Counting](cards.md#paper-lightweight-temporal-counting) | 把视频时序规律放在训练损失里，让实际推理保留逐帧接口。 |
| 多模态学习 | 训练策略 | [FedAFD: Multimodal Federated Learning via Adversarial Fusion and Distillation](cards.md#paper-fedafd) | 客户端保留个性化特征，服务端以蒸馏协调不同模型，并分别验证各端收益。 |
| 机器人学 | 模型架构 | [ConsisVLA-4D: Advancing Spatiotemporal Consistency in Efficient 3D-Perception and 4D-Reasoning for Robotic Manipulation](cards.md#paper-consisvla-4d) | 对指令相关物体显式核对跨视角身份、空间布局与时间演化，再测试对操作的贡献。 |
| 机器人学 | 训练策略 | [ActiveAD: Planning-Oriented Active Learning for End-to-End Autonomous Driving](cards.md#paper-activead-planning-label-budget) | 标注预算固定时，将起始多样性与后续规划相关性作为独立选样信号。 |
| 机器学习基础与统计 | 优化 | [Plug-and-Play Incomplete Multi-View Clustering via Janus-Faced Affinity Learning with Topology Harmonization](cards.md#paper-pjfth-incomplete-clustering) | 多视图图聚类先区分共享关系与视图私有关系，再校正不同视图锚点次序。 |
| 计算机视觉 | 优化 | [Cross-Instance Gaussian Splatting Registration via Geometry-Aware Feature-Guided Alignment](cards.md#paper-gsa-cross-instance) | 跨实例配准先以局部对应粗估尺度与姿态，再在固定表示上做多视特征一致性精化。 |
| 计算机视觉 | 推理策略 | [DDiT: Dynamic Patch Scheduling for Efficient Diffusion Transformers](cards.md#paper-ddit-dynamic-patch) | 扩散推理按时间步和局部内容分配图块尺寸，并用画质及总计算核对。 |
| 多模态学习 | 评测设计 | [Spot The Ball: A Benchmark for Visual Social Inference](cards.md#paper-spot-the-ball-heuristic-controls) | 用删除目标和空间捷径对照，判断模型是否真的使用人的姿态与互动证据。 |
| 多模态学习 | 表征学习 | [Bridging the Modality Gap in Compositional Zero-Shot Learning via Sparse Alignment and Unimodal Memory Bank](cards.md#paper-sam-sparse-crossmodal-alignment) | 让语言监督只对齐语义相关图像 patch，可用于标签只描述画面一部分的视觉任务。 |
| 智能体 | 视觉 Token 筛选 | [FocusUI: Efficient UI Grounding via Position-Preserving Visual Token Selection](cards.md#paper-focusui-position-preserving-selection) | 裁掉高分辨率观察中无关 patch 时保留坐标，避免节省算力却破坏行动定位。 |
| 多模态学习 | 记忆机制 | [VisMem: Latent Vision Memory Unlocks Potential of Vision-Language Models](cards.md#paper-vismem-dual-latent-vision-memory) | 把视觉证据的短期保存和语义巩固分开，按推理需要调用潜在记忆。 |
| 机器人学 | 伪标签学习 | [Real-World Point Tracking with Verifier-Guided Pseudo-Labeling](cards.md#paper-verifier-per-frame-pseudo-label-selection) | 混合教师时按局部预测可信度选标签，避免一位教师在所有样本上占优的假设。 |
| 多模态学习 | 表征学习 | [Multi-Modal Representation Learning via Semi-Supervised Rate Reduction for Generalized Category Discovery](cards.md#paper-rate-reduction-category-discovery) | 开放类别发现可同时优化模态内类别结构与跨模态对齐。 |
| 计算机视觉 | 模型架构 | [ShotDirector: Directorially Controllable Multi-Shot Video Generation with Cinematographic Transitions](cards.md#paper-hierarchical-multi-shot-control) | 将局部镜头控制与跨镜头共享信息分开处理，可改进视频生成的剪辑控制。 |
| 多模态学习 | 评测与诊断 | [4DWorldBench: A Comprehensive Evaluation Framework for 3D/4D World Generation Models](cards.md#paper-adaptive-world-model-rubrics) | 世界模型评测可以按条件动态挑选维度，并逐项校准与人工评分的相关性。 |
| 多模态学习 | 优化 | [TaskIT: Memory-Efficient Fine-Tuning of Multi-LoRA LLMs via Cross-Task Importance Transfer](cards.md#paper-budgeted-lora-module-selection) | 预算有限时可用任务间迁移证据选择已有和新增 LoRA 模块，再按峰值显存约束分配训练。 |
| 多模态学习 | 数据策略 | [Style-GRPO: Semantic-Aware Preference Optimization for Image Style Transfer Guided by Reward Modeling](cards.md#paper-targeted-style-preference-pairs) | 多目标生成奖励可用定向违例偏好对来独立监督风格、内容与视觉质量。 |
| 多模态学习 | 推理策略 | [AXG-Reasoner: Error Detection and Explanation in Long Task Videos with Vision-Language Models](cards.md#paper-normal-execution-graph-video-errors) | 长视频异常推理可用正常执行图先找出证据稀疏的动作片段，再交给冻结视觉语言模型解释。 |
| 计算机视觉 | 表征学习 | [Mesh4D: 4D Mesh Reconstruction and Tracking from Monocular Video](cards.md#paper-skeletal-training-prior-motion-latent) | 动态重建可以只在训练期用骨架监督动画潜空间，推理时仍接受普通单目视频。 |
| 计算机视觉 | 训练策略 | [Learning to See Through a Baby's Eyes: Early Visual Diets Enable Robust Visual Intelligence in Humans and Machines](cards.md#paper-catdiet) | 通过改变自监督目标，检验模型学到的物体属性，而非仅比较分类分数。 |
| 多模态学习 | 损失函数 | [Conflict-Aware Adaptive Cross-Reconstruction for Multimodal Sentiment Analysis](cards.md#paper-cacr-cross-reconstruction) | 存在模态冲突时，可用跨模态重建约束区分共享信息与私有信息。 |
| 计算机视觉 | 模型架构 | [MV-RoMa: From Pairwise Matching into Multi-View Track Reconstruction](cards.md#paper-mv-roma) | 把可靠的两视图对应当成多视图优化的初值，以跨视图信息减少几何不一致。 |
| 计算机视觉 | 模型架构 | [FlexAvatar: Learning Complete 3D Head Avatars with Partial Supervision](cards.md#paper-flexavatar-bias-tokens) | 训练时为已知数据来源分配专门的可学习表征，有助于隔离采集域偏差。 |
| 多模态学习 | 奖励函数 | [AnyDoc: Enhancing Document Generation via Large-Scale HTML/CSS Data Synthesis and Height-Aware Reinforcement Optimization](cards.md#paper-anydoc-height-reward) | 对生成物执行渲染后测量具体失效，可将布局错误变成可优化的标量信号。 |
| 机器人学 | 模型架构 | [Cross from Left to Right Brain: Adaptive Text Dreamer for Vision-and-Language Navigation](cards.md#paper-adaptive-text-dreamer) | 用预期未来语义代替逐像素预测，可降低想象模块的输出负担。 |
| 计算机视觉 | 弱监督学习 | [The Road Less Seen: Segment Exploration for Weakly Supervised Video Anomaly Detection](cards.md#paper-dual-exploration-low-fpr-video-anomaly) | 用部署工作点检验不平衡检测器，并以多样性和不确定性拓宽弱监督选样。 |
| 三维视觉 | 多尺度表征 | [Scenes as Tokens: Multi-Scale Normal Distributions Transform Tokenizer for General 3D Vision-Language Understanding](cards.md#paper-ndtokenizer-multiscale-scene-tokens) | 用多尺度分布统一场景压缩、交互提示与掩码解码。 |
| 机器人学 | 不确定性校准 | [Query2Uncertainty: Robust Uncertainty Quantification and Calibration for 3D Object Detection under Distribution Shift](cards.md#paper-query2uncertainty-query-density-calibration) | 用目标级潜在特征的密度修正分布偏移下的检测置信度和框不确定性。 |
| 机器人学 | 跨视角表征 | [V^2-SAM: Marrying SAM2 with Multi-Prompt Experts for Cross-View Object Correspondence](cards.md#paper-v2sam-cyclic-consistency-prompt-selection) | 融合互补的跨视角提示时，用往返一致性为每个样本选择专家。 |
| 机器人学 | 多传感器融合 | [PTC-Depth: Pose-Refined Monocular Depth Estimation with Temporal Consistency](cards.md#paper-ptc-depth-bayesian-metric-scale) | 将相对深度模型与具噪稀疏几何结合，用递归估计稳定米制尺度。 |
| 生成模型 | 条件生成 | [LumiX: Structured and Coherent Text-to-Intrinsic Generation](cards.md#paper-lumix-broadcast-query-tensor-lora) | 让多个互补输出共享空间查询与低秩适配，降低跨输出结构不一致。 |
| 多模态学习 | 训练策略 | [ViterbiPlanNet: Injecting Procedural Knowledge via Differentiable Viterbi for Planning in Instructional Videos](cards.md#paper-differentiable-viterbi-procedure-prior) | 可把流程图放入结构化解码层，让动作预测模型在训练时学习合法转移约束。 |
| 计算机视觉 | 训练策略 | [CycleBEV: Regularizing View Transformation Networks via View Cycle Consistency for Bird's-Eye-View Semantic Segmentation](cards.md#paper-cycle-consistency-view-lifting) | 正向的透视到俯视变换可在训练时接受逆向重投影监督，减少仅靠目标视角标签时的几何歧义。 |
| 多模态学习 | 表征学习 | [A Mixed Diet Makes DINO An Omnivorous Vision Encoder](cards.md#paper-frozen-teacher-cross-sensor-alignment) | 对齐不同传感器的同场景特征时，可用冻结的单模态教师作为语义锚点。 |
| 机器人学 | 表征学习 | [Unlocking 3D Affordance Segmentation with 2D Semantic Knowledge](cards.md#paper-lifted-affinity-distillation-affordance) | 给稀疏三维骨干蒸馏二维语义时，可传递点与点的语义亲和结构。 |
| 多模态学习 | 推理策略 | [GaussianDWM: 3D Gaussian Driving World Model for Unified Scene Understanding and Multi-Modal Generation](cards.md#paper-task-aware-gaussian-token-sampling) | 把三维场景转成有限数量的模型 token 时，可按任务切换全局覆盖与局部相似性采样。 |
| 多模态学习 | 数据策略 | [Watch and Learn: Learning to Use Computers from Online Videos](cards.md#paper-inverse-dynamics-ui-demonstrations) | 有状态画面但缺少动作标签时，可以训练逆动力学标注器，从状态变化恢复示范轨迹。 |
| 多模态学习 | 评测与诊断 | [VRR-QA: Visual Relational Reasoning in Videos Beyond Explicit Cues](cards.md#paper-vrr-qa) | 用依赖跨帧隐含证据的样例检验视频模型是否真正使用时序关系。 |
| 机器人学 | 模型架构 | [ESAM++: Efficient Online 3D Perception on the Edge](cards.md#paper-esam-plus-plus) | 用边缘设备实测定位在线三维感知瓶颈，并受控替换其中的三维特征编码器。 |
| 机器人学 | 推理策略 | [Towards Highly-Constrained Human Motion Generation with Retrieval-Guided Diffusion Noise Optimization](cards.md#paper-rg-dno) | 将难满足的约束交给检索初始化，再用可微目标修正动作。 |
| 机器人学 | 推理策略 | [History to Future: Evolving Agent with Experience and Thought for Zero-shot Vision-and-Language Navigation](cards.md#paper-evonav) | 将历史经验与前向假设分别维护，用作智能体动作选择的两种反馈。 |
| 多模态学习 | 损失函数 | [CTCal: Rethinking Text-to-Image Diffusion Models via Cross-Timestep Self-Calibration](cards.md#paper-ctcal-cross-timestep) | 可用同一模型低噪声状态中更可靠的对齐信号监督高噪声状态。 |
| 机器人学 | 模型架构 | [Learning Spatial-Temporal Consistency for 3D Semantic Scene Completion](cards.md#paper-conssc) | 将历史信息对齐到当前三维体素，并用可见性和相似性筛选再融合。 |
| 三维视觉 | 测试时适配 | [Low-Rank Test-Time Training for Pre-Trained Point Cloud Models](cards.md#paper-lott-pc-masked-latent-alignment) | 用预训练编码器的掩蔽不变性代替解码重建，降低无标签测试时适配成本。 |
| 机器人学 | 专家路由 | [DriveMoE: Mixture-of-Experts for Vision-Language-Action Model in End-to-End Autonomous Driving](cards.md#paper-drivemoe-view-skill-routing) | 分别按场景选择输入视角、按技能选择行动专家，可指导多摄像头 VLA 的路由粒度。 |
| 科学机器学习 | 智能体验证 | [Pixel2Phys: Distilling Governing Laws from Visual Dynamics](cards.md#paper-pixel2phys-hypothesis-validation-loop) | 将高维观测到低维规律分成可检验的候选构造与验证，适用于可仿真的视觉动态。 |
| 生成模型 | 强化学习与奖励 | [Are We Ready for RL in Text-to-3D Generation? A Progressive Investigation](cards.md#paper-higrpo-token-and-semantic-policy-optimization) | 为长生成序列区分 token 级优化和高层语义规划，并先检查奖励与人工偏好的对应关系。 |
| 多模态学习 | 长度外推 | [Echoes Over Time: Unlocking Length Generalization in Video-to-Audio Generation Models](cards.md#paper-mmhnet-train-short-test-long) | 长时音画生成可先尝试层级状态空间记忆，在短训练样本下验证推理长度外推。 |
| 计算机视觉 | 表征学习 | [Vision Foundation Models Can Be Good Tokenizers for Latent Diffusion Models](cards.md#paper-frozen-foundation-tokenizer-diffusion) | 图像扩散 tokenizer 可直接冻结语义编码器，把像素恢复交给解码器。 |
| 计算机视觉 | 模型架构 | [Flowception: Temporally Expansive Flow Matching for Video Generation](cards.md#paper-interleaved-frame-insertion-flow) | 用逐步插帧保持稀疏的全局时间上下文，并与连续去噪联合训练。 |
| 多模态学习 | 训练策略 | [OSPO: Object-Centric Self-Improving Preference Optimization for Text-to-Image Generation](cards.md#paper-object-localized-self-preference) | 模型自生成偏好数据时可按实体核查属性、关系和数量，减少整体评分掩盖细粒度错误。 |
| 多模态学习 | 数据策略 | [EVLF: Early Vision-Language Fusion for Generative Dataset Distillation](cards.md#paper-early-conditioning-dataset-distillation) | 合成训练集时，可提前融合图文条件以减少文本模板压过真实视觉纹理。 |
| 多模态学习 | 模型架构 | [DeRVOS: Decoupling Consistent Trajectory Generation and Multimodal Understanding for Referring Video Object Segmentation](cards.md#paper-separate-track-representations-language-grounding) | 将视频候选轨迹一致性与语言接地拆开，便于分别选择预训练骨干。 |
| 多模态学习 | 推理策略 | [Divide, then Ground: Adapting Frame Selection to Query Types for Long-Form Video Understanding](cards.md#paper-query-type-routing-long-video-frames) | 先判断问题需要全局覆盖还是局部证据，再决定是否支付查询相关的视觉搜索成本。 |
| 计算机视觉 | 训练策略 | [Diffusion Guided Chain-of-Vision for Large Autoregressive Vision Models](cards.md#paper-diffusion-intermediate-visual-supervision) | 可用预训练扩散模型的中间图像给纯视觉自回归模型构造逐步监督。 |
| 机器人学 | 模型架构 | [Spatial Retrieval Augmented Autonomous Driving](cards.md#paper-spatial-retrieval-driving) | 用离线地理记忆补足现场感知，并按静态与动态任务分别测量先验的收益。 |
| 计算机视觉 | 模型架构 | [WeatherCity: Urban Scene Reconstruction with Controllable Multi-Weather Transformation](cards.md#paper-weathercity) | 让模拟器共享几何与场景内容，并将条件特有外观交给独立解码器。 |
| 多模态学习 | 评测与诊断 | [RMIR: A Benchmark Dataset for Reasoning-Intensive Multimodal Image Retrieval](cards.md#paper-rmir-reasoning-retrieval) | 以功能、时间和因果查询分别验证推理训练与参数扩张哪个更能改善检索。 |
| 计算机视觉 | 模型架构 | [MeshWeaver: Sparse-Voxel-Guided Surface Weaving for Autoregressive Mesh Generation](cards.md#paper-meshweaver) | 给自回归几何生成加入局部稀疏结构约束，并在解码中直接预测顶点。 |
| 计算机视觉 | 模型架构 | [TM-BSN: Triangular-Masked Blind-Spot Network for Real-World Self-Supervised Image Denoising](cards.md#paper-tm-bsn) | 按测量噪声的相关几何设计盲区，保留原分辨率下未相关的邻域信息。 |
| 多模态学习 | 训练策略 | [ReMoT: Reinforcement Learning with Motion Contrast Triplets](cards.md#paper-remot-motion-contrast) | 用仅改变细微运动属性的对照训练视觉语言模型，并比较 SFT 与 GRPO 对此能力的影响。 |
| 多模态学习 | 推理策略 | [LLMind: Bio-inspired Training-free Adaptive Visual Representations for Vision-Language Models](cards.md#paper-llmind-adaptive-sampling) | 让冻结模型的语义反馈决定像素预算分配，兼顾关注区域和全局布局。 |
| 高效深度学习 | 参数高效适配 | [Decompose, Mix, Adapt: A Unified Framework for Parameter-Efficient Neural Network Recombination and Compression](cards.md#paper-crisp-shared-basis-recombination) | 让模型压缩和适配共享权重基底，以减少压缩后附加适配器的参数占比。 |
| 计算机视觉 | 动态推理 | [Adaptive Capacity Autoregressive Visual Tracking](cards.md#paper-artrack-ac-forecast-inference-capacity) | 提前预测观测难度，再调度昂贵和轻量追踪器，同时维持轨迹状态。 |
| 生成模型 | 优化与正则化 | [Stable Mean Flow: Lyapunov-Inspired One-Step Flow Matching](cards.md#paper-stable-mean-flow-local-nonexpansivity) | 用局部不扩张约束减少一步生成映射对扰动的放大。 |
| 三维视觉 | 空间位置编码 | [SoPE: Spherical Coordinate-Based Positional Embedding for Enhancing Spatial Perception of 3D LVLMs](cards.md#paper-sope-spherical-positional-encoding) | 为 3D 多模态模型选择同时表达距离和角度的位置编码。 |
| 多模态学习 | 评测设计 | [EduDiag: A Benchmark for Educational Diagnostic Reasoning with Error Tracing and Correction on Large Multimodal Models](cards.md#paper-edudiag-error-reconstruction-and-correction) | 把反馈能力拆为错误定位、重建错误逻辑及纠正，可迁移到智能体失败诊断。 |
| 机器人学 | 行动规划 | [ColaVLA: Leveraging Cognitive Latent Reasoning for Hierarchical Parallel Trajectory Planning in Autonomous Driving](cards.md#paper-colavla-latent-meta-action-planning) | 将语言推理压缩为潜在元动作，用层级并行解码生成连续轨迹，减少自回归延迟。 |
| 多模态学习 | 推理策略 | [Breaking the Illusion: When Positive Meets Negative in Multimodal Decoding](cards.md#paper-dual-evidence-counterfactual-decoding) | 多模态解码可以同时用增强证据与移除证据的视图校正语言先验。 |
| 机器人学 | 表征学习 | [UniPixie: Unified and Probabilistic 3D Physics Learning via Flow Matching](cards.md#paper-probabilistic-material-fields-single-view) | 单张图像无法辨识材料刚度时，可以预测可控的仿真参数分布以测试多个物理假设。 |
| 计算机视觉 | 训练策略 | [SimLBR: Learning to Detect Fake Images by Learning to Detect Real Images](cards.md#paper-inlier-boundary-latent-blending) | 开放集判别可围绕可信正类学习紧致边界，用潜空间混合正则弱化对单一负类分布的依赖。 |
| 多模态学习 | 表征学习 | [Boosting Visual Reprogramming for CLIP with Dual Granularity Alignment](cards.md#paper-multiscale-hierarchical-clip-reprogramming) | 冻结图文模型做少样本适配时，可同时利用图像尺度不确定性和标签父类结构。 |
| 多模态学习 | 模型架构 | [Granulon: Awakening Pixel-Level Visual Encoders with Adaptive Multi-Granularity Semantics for MLLM](cards.md#paper-query-conditioned-dino-token-granularity) | 视觉语言模型可按文本问题选择视觉 token 的聚合粒度，以兼顾局部细节和全局语义。 |
| 机器人学 | 模型架构 | [AtomicVLA: Unlocking the Potential of Atomic Skill Learning in Robots](cards.md#paper-atomic-skill-expert-routing-vla) | 把连续动作解码拆成可独立训练和扩展的原子技能专家，让高层规划承担技能编排。 |
| 计算机视觉 | 训练策略 | [Phased DMD: Few-step Distribution Matching Distillation via Score Matching within Subintervals](cards.md#paper-phase-local-distribution-distillation) | 少步生成蒸馏可按去噪阶段匹配分布，避免随机截断跨步梯度时丢失整体动作动态。 |
| 计算机视觉 | 训练策略 | [EffectErase: Joint Video Object Removal and Insertion for High-Quality Effect Erasing](cards.md#paper-effecterase) | 把插入和移除作为成对的训练方向，显式监督物体造成的间接视觉变化。 |
| 多模态学习 | 模型架构 | [SOUPLE: Enhancing Audio-Visual Localization and Segmentation with Learnable Prompt Contexts](cards.md#paper-souple-audio-visual) | 让视觉上下文调节音频条件提示，再将其送入掩膜解码器。 |
| 计算机视觉 | 模型架构 | [ReDirector: Creating Any-Length Video Retakes with Rotary Camera Encoding](cards.md#paper-redirector-roce) | 将相机关系写进注意力位置编码，并对齐输入视频与目标视频的时空基准。 |
| 多模态学习 | 模型架构 | [Heuristic-inspired Reasoning Priors Facilitate Data-Efficient Referring Object Detection](cards.md#paper-herod-reasoning-priors) | 把可解释的语言空间先验同时用于候选、输出和监督匹配，以降低定位标签需求。 |
| 多模态学习 | 损失函数 | [SoC: Semantic Orthogonal Calibration for Test-Time Prompt Tuning](cards.md#paper-soc-semantic-orthogonal) | 调整类原型几何时，对相近类使用平滑约束，并同时检查准确率与校准误差。 |
| 机器人学 | 损失函数 | [Learning a Unified Latent Action Space from Videos with Action-centric Cycle Consistency](cards.md#paper-latent-action-cycle-consistency) | 把同一潜动作施加于不同观察并回编码约束，以测试潜动作能否跨场景和本体复用。 |
| 多模态学习 | 推理策略 | [Language-Free Generative Editing from One Visual Example](cards.md#paper-visual-diffusion-conditioning) | 用一组视觉前后对表达语言难以精确刻画的变换，可作为冻结编辑模型的条件。 |
| 多模态学习 | 损失函数 | [ORION: ORthonormal Text Encoding for Universal VLM AdaptatION](cards.md#paper-orion-text-prototypes) | 只用类名调整 VLM 文本原型，联合检验类间可分性与原有语义结构保留。 |
| 三维视觉 | 几何表征 | [RINO: Rotation-Invariant Non-Rigid Correspondences](cards.md#paper-rino-so3-invariant-nonrigid-correspondence) | 结合旋转不变特征和方向感知映射，取消非刚性匹配前的预对齐。 |
| 三维视觉 | 结构化生成 | [Native and Compact Structured Latents for 3D Generation](cards.md#paper-o-voxel-native-structured-latent) | 将几何与材质一起写入稀疏三维潜变量，覆盖开放和非流形资产。 |
| 机器人学 | 点云配准 | [DualReg: Dual-Space Filtering and Reinforcement for Rigid Registration](cards.md#paper-dualreg-filtered-anchors-geometric-refinement) | 用可靠特征匹配作为局部几何精配准的锚点。 |
| 机器人学 | 时序状态建模 | [UFO: Unifying Feed-Forward and Optimization-based Methods for Large Driving Scene Modeling](cards.md#paper-ufo-visible-recurrent-scene-tokens) | 保留可被后续观测修正的场景 token，并按可见性筛选更新。 |
| 生成模型 | 分布式训练 | [Heterogeneous Decentralized Diffusion Models](cards.md#paper-heterogeneous-diffusion-topk-expert-fusion) | 统一异构目标专家的推理接口，并在融合前验证专家选择数量。 |
| 计算机视觉 | 推理策略 | [Zoo3D: Zero-Shot 3D Object Detection at Scene Level](cards.md#paper-multiview-mask-consensus-zero-shot-3d) | 场景三维检测可以先聚合多视角二维掩码，再用视角共识标注开放词汇类别。 |
| 多模态学习 | 模型架构 | [TimeViper: A Hybrid Mamba-Transformer Vision-Language Model for Efficient Long Video Understanding](cards.md#paper-vision-to-instruction-token-transfer) | 压缩长视频时，可以先让中间层把视觉信息转入指令 token，再删减冗余视觉 token。 |
| 机器人学 | 训练策略 | [Goal-Driven Reward by Video Diffusion Models for Reinforcement Learning](cards.md#paper-video-diffusion-goal-reward) | 可将生成视频的阶段语义和目标帧可达性一起用于强化学习奖励。 |
| 计算机视觉 | 模型架构 | [Enhancing Hands in 3D Whole-Body Pose Estimation with Conditional Hands Modulator](cards.md#paper-specialist-modulation-global-pose) | 局部专家和全局估计器互补时，可用专家特征调制全局网络，保留跨部位姿态约束。 |
| 机器人学 | 推理策略 | [GeniNav: Generative Model Driven Image-Goal Navigation via Imagination-Guided Consistency Flow Matching](cards.md#paper-subgoal-and-consistent-trajectory-ranking) | 闭环目标导航可把高层视觉子目标、时间一致性生成和候选轨迹排序分别设计。 |
| 机器学习基础与统计 | 模型架构 | [Reparameterized Tensor Ring Functional Decomposition for Multi-Dimensional Data Recovery](cards.md#paper-reptrfd) | 将连续低秩分解的固定频谱基与可训练权重分离，改善对高频信息的拟合。 |
| 机器学习基础与统计 | 评测与诊断 | [Semi-Supervised Conformal Prediction With Unlabeled Nonconformity Score](cards.md#paper-semicp-nearest-neighbor) | 少量标签校准置信区间时，通过近邻给未标数据匹配非一致性分数。 |
| 机器人学 | 模型架构 | [EfficientVPR: Toward Efficient Visual Place Recognition via Scene-Aware Prompt Tuning and Adaptive Feature Enhancement](cards.md#paper-efficientvpr) | 在线地点检索中用输入条件化提示和局部增强替代高开销二次排序。 |
| 计算机视觉 | 损失函数 | [MU-GeNeRF: Multi-view Uncertainty-guided Generalizable Neural Radiance Fields for Distractor-aware Scene](cards.md#paper-mu-generf) | 把输入视图内部冲突与目标观察异常分开估计，避免用单视图残差决定是否剔除静态结构。 |
| 多模态学习 | 模型架构 | [VQRAE: Representation Quantization Autoencoders for Multimodal Understanding, Generation and Reconstruction](cards.md#paper-vqrae-unified-tokenizer) | 共享视觉编码器输出连续理解特征及离散生成令牌，并用自蒸馏限制量化训练改变语义。 |
| 多模态学习 | 推理策略 | [Sparse-LaViDa: Sparse Multimodal Discrete Diffusion Language Models](cards.md#paper-sparse-lavida) | 以少量寄存令牌代理未参与本轮计算的掩码位置，并在训练中模拟同一稀疏过程。 |
| 机器人学 | 训练策略 | [Test-Time Training for LiDAR Semantic Segmentation under Corruption via Geometric Inlier Discrimination](cards.md#paper-geoid-lidar-test-time) | 测试时用可控几何扰动构造自监督目标，并筛除原始与合成两侧的不可靠点。 |
| 机器人学 | 鲁棒损失 | [LEADER: Learning Reliable Local-to-Global Correspondences for LiDAR Relocalization](cards.md#paper-leader-truncated-relative-reliability) | 用相对可靠性分配点对应监督，降低不确定匹配对位姿估计的影响。 |
| 智能体 | 奖励与自我改进 | [JarvisEvo: Towards a Self-Evolving Photo Editing Agent with Synergistic Editor-Evaluator Optimization](cards.md#paper-jarvisevo-joint-editor-evaluator-optimization) | 让编辑策略和评价策略交替改进，并把每次编辑的视觉证据放回决策过程。 |
| 机器人学 | 时空表征 | [SwiftVLA: Unlocking Spatiotemporal Dynamics for Lightweight VLA Models at Minimal Overhead](cards.md#paper-swiftvla-future-trained-fusion-tokens) | 用未来预测监督少量融合 token，并测试缺失显式 4D 输入时的策略性能。 |
| 多模态学习 | 评测设计 | [SpatiaLQA: A Benchmark for Evaluating Spatial Logical Reasoning in Vision-Language Models](cards.md#paper-spatialqa-content-precondition-evaluation) | 把空间任务的步骤内容和前置条件分开评分，用来定位规划失败由感知还是约束引起。 |
| 机器学习 | 持续学习 | [Robustness Under Data Scarcity: Few-Shot Continual Adversarial Training for Evolving Threats](cards.md#paper-few-shot-continual-mixture-prototype-replay) | 阶段样本很少时以混合分布回放特征，并平衡旧域保留和新域适应。 |
| 计算机视觉 | 训练策略 | [Mirai: Autoregressive Visual Generation Needs Foresight](cards.md#paper-spatial-foresight-autoregressive-generation) | 可在训练阶段把图像网格中后续位置的信息监督到自回归模型的中间表征。 |
| 机器人学 | 推理策略 | [SIMPACT: Simulation-Enabled Action Planning using Vision-Language Models](cards.md#paper-simulation-in-loop-vlm-action-ranking) | 当视觉语言模型缺少动作后果知识时，可在执行前用物理仿真比较备选方案。 |
| 计算机视觉 | 数据策略 | [What's Wrong with Synthetic Data for Scene Text Recognition? A Strong Synthetic Engine with Diverse Simulations and Self-Evolution](cards.md#paper-factorized-synthetic-real-data-gap) | 合成数据迁移不足时，可逐因素诊断语料、样式和布局覆盖度，再补采困难组合。 |
| 机器学习基础与统计 | 优化 | [Fed-ADE: Adaptive Learning Rate for Federated Post-adaptation under Distribution Shift](cards.md#paper-uncertainty-feature-drift-learning-rate) | 无标签在线适配可用预测不确定性和特征漂移分别追踪变化，并按客户端动态调学习率。 |
| 多模态学习 | 表征学习 | [Beyond Duality: A Hybrid Framework of Leveraging Shared and Private Features for RGB-Event Object Detection](cards.md#paper-frequency-coherence-shared-private-fusion) | 异质传感器融合可先估计共有与模态私有成分，再分别编码互补信息。 |
| 计算机视觉 | 推理策略 | [HierUQ: Hierarchical Uncertainty Quantification with Adaptive Granularity Reconciliation for Degraded Image Classification](cards.md#paper-uncertainty-triggered-hierarchy-backoff) | 当证据无法支持细分类时，可以依据分层校准的置信度退回更可靠的父类。 |
| 机器学习基础与统计 | 模型架构 | [Spatiotemporal Pyramid Flow Matching for Climate Emulation](cards.md#paper-spatiotemporal-pyramid-flow) | 让生成轨迹各阶段对应不同时间和空间粒度，可按所需时间尺度直接采样。 |
| 机器学习基础与统计 | 损失函数 | [Stable Spike: Dual Consistency Optimization via Bitwise AND Operations for Spiking Neural Networks](cards.md#paper-stable-spike-consistency) | 提取跨步共同激活作稳定目标，再在受控扰动下约束预测一致，可指导低延迟事件模型训练。 |
| 多模态学习 | 训练策略 | [Factorized Context Aggregation for Robust Cancer Risk Estimation via Soft Re-Ranked Retrieval and Hierarchical Anchors](cards.md#paper-factorized-privileged-modality) | 部署端只保留常见传感器时，可将其他模态作为训练期信息，并按缺失比例验证性能。 |
| 计算机视觉 | 损失函数 | [Selfi: Self-improving Reconstruction Engine via 3D Geometric Feature Alignment](cards.md#paper-selfi-geometric-alignment) | 利用三维基础模型自身输出构造重投影监督，单独训练轻量适配器改善多视图对齐。 |
| 多模态学习 | 推理策略 | [Token Reduction via Local and Global Contexts Optimization for Efficient Video Large Language Models](cards.md#paper-aot-video-token-reduction) | 压缩前先将被删令牌的信息映射到锚点，并保留不同于关键帧的运动信号。 |
| 计算机视觉 | 推理策略 | [Match-and-Fuse: Consistent Generation from Unstructured Image Sets](cards.md#paper-match-and-fuse) | 以图连接共享内容的观测，用可靠对应在相邻视角的生成过程间融合特征。 |
| 多模态学习 | 联邦学习 | [OmniFM: Toward Modality-Robust and Task-Agnostic Federated Learning for Heterogeneous Medical Imaging](cards.md#paper-omnifm-low-frequency-global-knowledge) | 当各客户端模态不同时，检验能否先交换跨模态稳定的低频公共先验。 |
| 三维视觉 | 测试时状态更新 | [tttLRM: Test-Time Training for Long Context and Autoregressive 3D Reconstruction](cards.md#paper-tttlrm-streaming-3d-fast-weights) | 将连续多视图观测压缩进快权重，避免每次重新处理全部历史帧。 |
| 生成模型 | 采样与强化学习 | [Designing Instance-Level Sampling Schedules via REINFORCE with James-Stein Shrinkage](cards.md#paper-instance-schedules-james-stein-reinforce) | 冻结生成器，按提示词和噪声学习采样时间表，并压低强化学习奖励基线的估计误差。 |
| 机器人学 | 跨模态策略训练 | [MM-ACT: Learn from Multimodal Parallel Generation to Act](cards.md#paper-mm-act-shared-context-parallel-decoding) | 用共享上下文训练图像、文本和动作生成，但给动作采用单步并行解码。 |
| 多模态学习 | 噪声鲁棒学习 | [Rethinking Cross-Modal Anchor Alignment for Mitigating Error Accumulation](cards.md#paper-gsl-geometric-cross-modal-anchor-correction) | 清洁图文配对也可能传播错误，纠噪时应检查各自邻域几何是否一致。 |
| 多模态学习 | 推理策略 | [CountGD++: Generalized Prompting for Open-World Counting](cards.md#paper-positive-negative-exemplar-counting) | 开放词汇感知可同时支持正例、反例和自动生成的参考样本，降低目标描述歧义。 |
| 计算机视觉 | 数据策略 | [PRISM: Video Dataset Condensation with Progressive Refinement and Insertion for Sparse Motion](cards.md#paper-adaptive-video-condensation-anchors) | 视频数据压缩可从少量时间锚点开始，只在插值无法表达非线性运动时添加关键帧。 |
| 机器人学 | 训练策略 | [D3D-VLP: Dynamic 3D Vision-Language-Planning Model for Embodied Grounding and Navigation](cards.md#paper-masked-fragmented-embodied-supervision) | 具身任务不同数据源只标了个别中间变量时，可共享输出结构并屏蔽缺失监督。 |
| 计算机视觉 | 模型架构 | [WorldReel: 4D Video Generation with Consistent Geometry and Motion Modeling](cards.md#paper-joint-4d-geometry-rgb-video-generation) | 世界生成器可以把可核查的三维几何和运动当作联合输出，用合成精标与真实视频分别补强。 |
| 计算机视觉 | 模型架构 | [Off The Grid: Detection of Primitives for Feed-Forward 3D Gaussian Splatting](cards.md#paper-entropy-budgeted-off-grid-primitives) | 稀疏三维重建可按图像块的复杂性分配几何原语，并让原语位置脱离像素网格。 |
| 计算机视觉 | 推理策略 | [Improving Diffusion Generalization with Weak-to-Strong Segmented Guidance](cards.md#paper-diffusion-guidance-step-regimes) | 扩散推理可根据去噪阶段选择不同的弱参照，减少用单一引导机制覆盖全程的误差。 |
| 机器学习基础与统计 | 推理策略 | [DMGD: Train-Free Dataset Distillation with Semantic-Distribution Matching in Diffusion Models](cards.md#paper-dmgd-dataset-distillation) | 合成蒸馏数据时分别约束类别语义与目标样本分布，避免只追求单张图像的类别可辨识性。 |
| 计算机视觉 | 模型架构 | [Learning Compact 3D Representations from Feed-Forward Novel View Synthesis](cards.md#paper-c3g-compact-gaussians) | 用共享的跨视图令牌决定三维表达的稀疏位置，再复用注意力把二维语义投影至三维。 |
| 智能体 | 模型架构 | [ShowUI-p: Flow-based Generative Models as GUI Dexterous Hands](cards.md#paper-showui-p-continuous-actions) | 根据动作类型组合离散决策和连续反馈控制，用轻量动作专家处理细粒度轨迹。 |
| 多模态学习 | 训练策略 | [How Far Can We Go With Synthetic Data for Audio-Visual Sound Source Localization?](cards.md#paper-synthetic-audiovisual-clones) | 以同源样本的合成克隆做等规模对照，再改变真实与合成比例，测定合成数据在何处增益。 |
| 多模态学习 | 损失函数 | [Global-Graph Guided and Local-Graph Weighted Contrastive Learning for Unified Clustering on Incomplete and Noise Multi-View Data](cards.md#paper-global-local-graph-contrastive) | 将缺对和错对视为不同错误来源，用全局补配对、局部置信度调权。 |
| 计算机视觉 | 损失函数 | [ReFlow: Self-correction Motion Learning for Dynamic Scene Reconstruction](cards.md#paper-reflow-motion-self-correction) | 将总投影运动和静态区域的相机诱导运动拆开监督，可在重建中自校正运动。 |
| 机器学习基础与统计 | 训练策略 | [Is Bin Generation Indispensable? A Bin-Generation-Free Dataset Quantization via Semantic Perspective](cards.md#paper-bgfdq-neighbor-coresets) | 用语义邻域直接决定核心样本，并按样本内部冗余决定图块保留率。 |
| 生成模型 | 视觉 Token 化 | [CaTok: Taming Mean Flows for One-Dimensional Causal Image Tokenization](cards.md#paper-catok-time-bound-causal-tokenization) | 将视觉 token 前缀与生成时间区间绑定，兼容因果生成与不同解码预算。 |
| 机器人学 | 检索与记忆 | [TrajRAG: Retrieving Geometric-Semantic Experience for Zero-Shot Object Navigation](cards.md#paper-trajrag-topopolar-experience-retrieval) | 检索历史导航轨迹的拓扑几何和语义，而不是只依赖语言模型的常识。 |
| 三维视觉 | 场景表征 | [SceneTok: A Compressed, Diffusable Token Space for 3D Scenes](cards.md#paper-scenetok-unordered-compressed-view-tokens) | 从多视图压缩出与空间网格脱钩的无序场景 token，可同时用于渲染与生成。 |
| 多模态学习 | 合成监督 | [See and Fix the Flaws: Enabling VLMs and Diffusion Models to Comprehend Visual Artifacts via Agentic Data Synthesis](cards.md#paper-artiagent-localized-synthetic-artifact-pairs) | 合成局部缺陷并保留干净反事实，联合监督缺陷定位、描述与修复。 |
| 生成模型 | 强化学习与奖励 | [DRM: Diffusion-based Reward Model With Step-wise Guidance](cards.md#paper-drm-intermediate-latent-stepwise-reward) | 在去噪轨迹中间估计偏好，为逐步优化提供比终点奖励更近的反馈。 |
| 机器人学 | 表征学习 | [Gallant: Voxel Grid-based Humanoid Locomotion and Local-navigation across 3-D Constrained Terrains](cards.md#paper-vertical-grouped-voxel-locomotion) | 机器人局部避障可保留完整高度体素，并用按高度分组的二维卷积控制算力。 |
| 计算机视觉 | 训练策略 | [A Closer Look at Cross-Domain Few-Shot Object Detection: Fine-Tuning Matters and Parallel Decoder Helps](cards.md#paper-few-shot-parallel-denoising-decoder-ensemble) | 少样本检测微调可以在共享解码后保留多条查询轨迹，将多样预测集成以降低小样本波动。 |
| 多模态学习 | 评测与诊断 | [Do Vision-Language Models Measure Up? Benchmarking Visual Measurement Reading with MeasureBench](cards.md#paper-measurement-error-factorized-vlm-probes) | 检验感知数值时可单独评分数值与单位，并以可控合成样本定位真实任务中的误差。 |
| 计算机视觉 | 训练策略 | [Spe-BEVHead: Rethinking the Detection Head Design for Bird's-Eye-View Object Detection](cards.md#paper-shape-aligned-dense-bev-supervision) | 旋转目标检测可将正例核匹配到物体的实际方向和形状，再显式抑制局部重复响应。 |
| 多模态学习 | 推理策略 | [MVP: Multiple View Prediction Improves GUI Grounding](cards.md#paper-multiview-consensus-gui-grounding) | 当 GUI 坐标对轻微裁剪不稳定时，可通过多个局部视图的一致性筛出离群预测。 |
| 多模态学习 | 训练策略 | [Towards GUI Agents: Vision-Language Diffusion Models for GUI Grounding](cards.md#paper-geometry-structured-diffusion-masking) | 离散扩散输出结构化坐标时，可按几何层次设计掩码，而非只按均匀的噪声进度训练。 |
| 计算机视觉 | 模型架构 | [Compressed-Domain-Aware Online Video Super-Resolution](cards.md#paper-codec-motion-residual-online-video) | 在线视频模型可复用压缩码流的运动向量与残差作为对齐及融合先验。 |
| 机器人学 | 模型架构 | [Efficient Hybrid SE(3)-Equivariant Visuomotor Flow Policy via Spherical Harmonics for Robot Manipulation](cards.md#paper-e3flow-equivariant-policy) | 用不变特征控制图像与点云信息的融合权重，保留动作生成的旋转等变性。 |
| 机器人学 | 损失函数 | [PAD-Hand: Physics-Aware Diffusion for Hand Motion Recovery](cards.md#paper-pad-hand-physics-variance) | 用动力学残差作可观测量，并输出其不确定性，避免将错误模型当成硬约束。 |
| 多模态学习 | 评测与诊断 | [SVBench: Evaluation of Video Generation Models on Social Reasoning](cards.md#paper-svbench-social-video) | 把社会行为实验转成仅可通过视觉行为验证的短视频测试，以发现画面逼真但互动逻辑错误的情况。 |
| 机器人学 | 推理策略 | [GeoFlow: Real-Time Fine-Grained Cross-View Geolocalization via Iterative Flow Prediction](cards.md#paper-geoflow-iterative-localization) | 定位时预测任意候选的纠偏位移，按计算预算迭代多个候选直至达成共识。 |
| 智能体 | 训练策略 | [Scaling Agentic Reinforcement Learning for Tool-Integrated Reasoning in VLMs](cards.md#paper-vista-gym-tool-reasoning) | 用统一执行接口和可验证反馈训练多步视觉工具选择，并单独评估域外任务。 |
| 机器人学 | 推理策略 | [TESO: Online Tracking of Essential Matrix by Stochastic Optimization](cards.md#paper-teso-online-stereo) | 使用低成本流形在线优化连续估计双目外参漂移，可在长期运行时刷新标定。 |
| 机器人学 | 评测与诊断 | [AGENTSAFE: Benchmarking the Safety of Embodied Agents on Hazardous Instructions](cards.md#paper-agentsafe-stage-diagnosis) | 分别验证危险识别、安全规划和执行结果，以找出安全判断在哪一阶段失去约束。 |
| 多模态学习 | 评测与诊断 | [RealBirdID: Benchmarking Bird Species Identification in the Era of MLLMs](cards.md#paper-realbirdid-abstention) | 把正确识别、是否应拒答、拒答理由三项分开评分，防止分类精度掩盖证据缺失。 |
| 机器人学 | 强化学习与反馈 | [Unleashing VLA Potentials in Autonomous Driving via Explicit Learning from Failures](cards.md#paper-elf-vla-structured-failure-feedback) | 当长尾场景的标量奖励全为零时，增加结构化失败原因来区分改进方向。 |
| 生成模型 | 空间位置编码 | [OPRO: Orthogonal Panel-Relative Operators for Panel-Aware In-Context Image Generation](cards.md#paper-opro-orthogonal-panel-relative-operators) | 为多面板输入学习相对位置，同时用正交约束保护同一面板内的已有行为。 |
| 生成模型 | 训练目标 | [Improving Controllable Generation: Faster Training and Better Performance via x0-Supervision](cards.md#paper-x0-supervision-controllable-generation) | 训练可控生成适配器时，比较直接预测干净结果与沿用骨干的去噪目标。 |
| 多模态学习 | 推理时干预 | [AdaIAT: Adaptively Increasing Attention to Generated Text to Alleviate Hallucinations in LVLM](cards.md#paper-adaiat-generated-text-attention) | 低成本纠正生成式视觉幻觉时，比较加强图像注意与按需加强已生成文本的注意。 |
| 机器人学 | 运动规划 | [Visual-RRT: Finding Paths toward Visual-Goals via Differentiable Rendering](cards.md#paper-visual-rrt-rendering-gradient-tree) | 只有目标图像时，用渲染梯度引导随机树搜索，同时保留探索未覆盖区域的能力。 |
| 机器人学 | 推理策略 | [Action-Sketcher: From Reasoning to Action via Visual Sketches for Robotic Manipulation](cards.md#paper-grounded-visual-sketch-robotic-planning) | 可把自然语言意图转为当前画面上可检查的点、框和箭头，作为规划及动作的中间接口。 |
| 计算机视觉 | 表征学习 | [GP-4DGS: Probabilistic 4D Gaussian Splatting from Monocular Video via Variational Gaussian Processes](cards.md#paper-probabilistic-dynamic-gaussian-deformation) | 对动态场景形变可使用带不确定性的时空先验，便于区别真实运动和观测外插。 |
| 多模态学习 | 训练策略 | [Asking like Socrates: Socrates helps VLMs understand remote sensing images](cards.md#paper-iterative-visual-evidence-trace-supervision) | 视觉推理监督可交错记录检查区域与更新判断，以避免模型只学到流畅的文字解释。 |
| 多模态学习 | 推理策略 | [STiTch: Semantic Transition and Transportation in Collaboration for Training-Free Zero-Shot Composed Image Retrieval](cards.md#paper-transition-transport-multimodal-retrieval) | 组合检索可同时修正生成描述的语义偏移，并用多个局部匹配表达属性组合。 |
| 多模态学习 | 模型架构 | [Language-guided Frequency Modulation for Large Vision-Language Models](cards.md#paper-language-conditioned-frequency-modulation) | 问题匹配的视觉证据可通过频带调制，在同一编码器中切换全局结构与局部细节。 |
| 计算机视觉 | 训练策略 | [Masked Representation Modeling for Domain-Adaptive Segmentation](cards.md#paper-semantic-latent-masking-domain-adaptation) | 领域适配可把掩码重建放到高层语义特征上，使自监督目标贴近下游任务。 |
| 多模态学习 | 推理策略 | [Test-Time Attention Purification for Backdoored Large Vision Language Models](cards.md#paper-inference-attention-integrity-monitor) | 可以把跨模态注意力异常作为多模态模型部署时的防御监测信号，并同步检查正常任务效用。 |
| 多模态学习 | 推理策略 | [SCoRe: Salience-Coverage Reduction for Vision Token Pruning in Vision-Language Models](cards.md#paper-score-vision-token-pruning) | 在一项选择目标内兼顾显著性与覆盖性，保护次要但有用的视觉语义簇。 |
| 多模态学习 | 模型架构 | [Hear What Matters! Text-conditioned Selective Video-to-Audio Generation](cards.md#paper-selva-selective-video-audio) | 把文本作为目标选择信号注入编码端，并用混合数据生成保留单源的自监督标签。 |
| 机器人学 | 评测与诊断 | [Exploring 6D Object Pose Estimation with Deformation](cards.md#paper-desope-deformation-failure) | 按物体相对规范形状的变形程度分层评测，决定抓取感知是否应使用刚体姿态模型。 |
| 多模态学习 | 训练策略 | [Role-SynthCLIP: A Role-Play Driven Diverse Synthetic Data Approach](cards.md#paper-role-synthclip-caption-diversity) | 图像数量固定时，用互补描述角色扩展监督语义，并分别测量检索和分类。 |
| 机器人学 | 模型架构 | [Perceiving the Near, Reasoning the Distant: Coherent Long-Horizon Trajectory Prediction for Autonomous Driving](cards.md#paper-ndpnet-horizon-transition) | 按时间距离选择短期动力学与长期语义两条预测路径，并在交接处显式约束运动连续。 |
| 智能体 | 推理策略 | [DRS-GUI: Dynamic Region Search for Training-Free GUI Grounding](cards.md#paper-drs-gui-region-search) | 用可控预算渐进搜索高分辨率画面的相关区域，并以指令条件奖励裁掉无关区域。 |
| 机器学习基础与统计 | 损失函数 | [DiverseDiT: Towards Diverse Representation Learning in Diffusion Transformers](cards.md#paper-diversedit-block-diversity) | 对齐外部视觉表示时，同时测量层间同质化，可用跨层残差及差异约束保持分工。 |
| 机器人学 | 主动感知 | [LiDAS: Lighting-driven Dynamic Active Sensing for Nighttime Perception](cards.md#paper-lidas-task-directed-active-illumination) | 用冻结感知模型的下游表现选择照明分配，在固定功率下改善可见性。 |
| 智能体 | 工具调度 | [RoboAgent: Chaining Basic Capabilities for Embodied Task Planning](cards.md#paper-roboagent-capability-local-context-scheduling) | 为每项基础能力维护自己的上下文，用调度器把长任务拆成局部视觉语言问题。 |
| 机器人学 | 时序记忆 | [AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention](cards.md#paper-avavla-recurrent-belief-visual-attention) | 用递归信念状态按指令和动作历史重加权当前视觉 token。 |
| 多模态学习 | 主动感知 | [Act2See: Emergent Active Visual Perception for Video Reasoning](cards.md#paper-act2see-retrieve-or-synthesize-frames) | 训练模型在推理中按需获取视觉帧，并把检索的观测和生成的假设分开使用。 |
| 多模态学习 | 评测设计 | [From Indoor to Open World: Revealing the Spatial Reasoning Gap in MLLMs](cards.md#paper-osi-bench-metric-spatial-reasoning-gap) | 用度量真值及盲视对照诊断空间推理是否使用了视觉证据。 |
| 多模态学习 | 训练策略 | [Noise-Aware Few-Shot Learning through Bi-directional Multi-View Prompt Alignment](cards.md#paper-bidirectional-region-prompt-noise-control) | 少样本提示微调遇到噪声标签时，可以以区域与提示的部分匹配保留可靠信号。 |
| 多模态学习 | 表征学习 | [RaGS: Unleashing 3D Gaussian Splatting from 4D Radar and Monocular Cue for 3D Object Detection](cards.md#paper-adaptive-gaussians-radar-camera-fusion) | 可通过稀疏而可移动的三维原语，把异质传感器的计算预算集中于目标附近。 |
| 机器人学 | 模型架构 | [WAM-Flow: Parallel Coarse-to-Fine Motion Planning via Discrete Flow Matching for Autonomous Driving](cards.md#paper-metric-discrete-flow-trajectory-planning) | 连续轨迹若需离散生成，可让 token 表征保留数值距离，再并行粗到细去噪。 |
| 机器学习基础与统计 | 优化 | [Parameter-efficient Continual Learning for Enhancing Plasticity without Forgetting under Limited Model Capacity](cards.md#paper-gradient-guided-frozen-parameter-reuse) | 容量受限的持续学习可把冻结权重复用与新增参数分配作为两个独立决策。 |
| 计算机视觉 | 模型架构 | [ActionMesh: Animated 3D Mesh Generation with Temporal 3D Diffusion](cards.md#paper-temporal-shapes-to-reference-deformation) | 可将时间同步的独立三维形状转换成对同一参考网格的形变，以得到一致拓扑的动画。 |
| 计算机视觉 | 表征学习 | [Towards Intrinsic-Aware Monocular 3D Object Detection](cards.md#paper-intrinsic-conditioned-monocular-spatial-model) | 单目模型跨设备部署可用相机内参的视觉几何条件做分层适配，并按焦距外插单独评测。 |
| 计算机视觉 | 训练策略 | [From Few-way to Many-way: Rethinking Few-shot Fine-grained Image Classification](cards.md#paper-sceg-many-way-few-shot) | 少样本任务的训练类别数显著小于部署类别数时，加入全局分离约束并直接测试多类泛化。 |
| 机器人学 | 损失函数 | [Boosting Vision-Language-Action Finetuning with Feasible Action Neighborhood Prior](cards.md#paper-fan-action-neighborhood) | 当相邻动作具有同等进展时，可让动作输出分布反映局部容忍度以提高示教利用效率。 |
| 计算机视觉 | 损失函数 | [High-Precision Dichotomous Image Segmentation via Depth Integrity-Prior and Fine-Grained Patch Strategy](cards.md#paper-pdfnet-depth-integrity) | 用深度结构先验辅助 RGB 掩膜学习，在局部修复前检查目标内外的几何连续性。 |
| 多模态学习 | 评测与诊断 | [Multimodal RewardBench 2: Evaluating Omni Reward Models for Interleaved Text and Image](cards.md#paper-mmrb2-interleaved-judges) | 奖励模型需用专家匹配的跨模态偏好对做分任务校准，避免把单一生成评分推广到交错推理。 |
| 多模态学习 | 推理策略 | [VideoITG: Multimodal Video Understanding with Instructed Temporal Grounding](cards.md#paper-videoitg-instructed-sampling) | 视频读入预算有限时，按指令查找关键片段并选择帧，将选帧和回答分开比较。 |
| 计算机视觉 | 推理策略 | [Accelerating Diffusion-based Video Editing via Heterogeneous Caching: Beyond Full Computing at Sampled Denoising Timestep](cards.md#paper-hetcache-video-editing) | 在扩散的选定计算步内按令牌作用分配刷新，避免每次刷新重算全部上下文。 |
| 多模态学习 | 奖励函数 | [Saliency-R1: Enforcing Interpretable and Faithful Vision-language Reasoning via Saliency-map Alignment Reward](cards.md#paper-saliency-r1-alignment) | 将关键区域与生成时实际用到的视觉证据对齐，作为答案正确性之外的奖励。 |
| 计算机视觉 | 优化策略 | [Plug-and-Play PDE Optimization for 3D Gaussian Splatting: Toward High-Quality Rendering and Reconstruction](cards.md#paper-pde-gaussian-optimization) | 点基元优化出现结构漂浮时，用局部粘性约束稳定更新，再评估渲染与几何两种目标。 |
| 计算机视觉 | 分布外检测 | [A Debiased Reconstruction-based Framework for Training-Free Detection of AI-Generated Images](cards.md#paper-rdd-instance-reconstruction-debiasing) | 用保留背景的同图扰动建立参照，减少内容复杂度对重建异常分数的影响。 |
| 计算机视觉 | 高效注意力 | [UniMERNet: A Universal Network for Real-World Mathematical Expression Recognition](cards.md#paper-unimernet-horizontal-vertical-raster-attention) | 依据视觉读取顺序将二维全局注意力拆为先横向再纵向。 |
| 机器人学 | 仿真与数据增广 | [SimScale: Learning to Drive via Real-World Simulation at Scale](cards.md#paper-simscale-reactive-perturbations-pseudo-expert) | 对日志中的自车状态施加反事实偏移，并给出新状态下的恢复轨迹监督。 |
| 生成模型 | 强化学习与奖励 | [Unified Customized Generation by Disentangled Reward Modeling](cards.md#paper-uso-disentangled-subject-style-rewards) | 联合学习多个参考维度时，为容易互相泄漏的因素使用分离的反馈。 |
| 机器学习 | 测试时适配 | [Neural Collapse in Test-Time Adaptation](cards.md#paper-nctta-sample-alignment-pseudolabels) | 在置信度自训练前检查样本特征和分类器权重是否仍对齐。 |
| 机器人学 | 训练策略 | [Learning to Control Physically-simulated 3D Characters via Generating and Mimicking 2D Motions](cards.md#paper-image-plane-tracking-physics-control) | 缺少可靠三维动作标注时，可以在物理模拟内把投影轨迹作为模仿监督。 |
| 多模态学习 | 训练策略 | [Towards Decompositional Human Motion Generation with Energy-Based Diffusion Models](cards.md#paper-energy-composition-motion-without-part-labels) | 只有整体动作配对时，可用能量叠加学习组成分布，避免逐动作收集分解标签。 |
| 计算机视觉 | 数据策略 | [ManifoldGD: Training-Free Hierarchical Manifold Guidance for Diffusion-Based Dataset Distillation](cards.md#paper-hierarchical-latent-prototypes-distillation) | 合成数据去噪可同时利用粗粒度原型与细粒度代表样本，避免单中心丢掉类内模式。 |
| 计算机视觉 | 训练策略 | [Flash-DMD: Towards High-Fidelity Few-Step Image Generation with Efficient Distillation and Joint Reinforcement Learning](cards.md#paper-step-aware-distillation-joint-refinement) | 少步蒸馏与奖励对齐可以共同设计；在蒸馏时保留质量约束，有助于稳定后续奖励优化。 |
| 计算机视觉 | 推理策略 | [TAP: A Token-Adaptive Predictor Framework for Training-Free Diffusion Acceleration](cards.md#paper-shallow-probe-token-adaptive-diffusion-cache) | 扩散缓存可以用一次浅层探测给不同视觉 token 自适应挑选预测器。 |
| 机器学习基础与统计 | 训练策略 | [Debiased Sample Selection for Learning with Noisy Labels](cards.md#paper-class-instance-bias-noisy-selection) | 按训练损失筛选干净样本会偏向易学类，可分别修正类覆盖和个体错选。 |
| 计算机视觉 | 训练策略 | [GeodesicNVS: Probability Density Geodesic Flow Matching for Novel View Synthesis](cards.md#paper-geodesicnvs-density-flow) | 在成对观测之间直接学习流，以数据密度约束中间状态的几何一致性。 |
| 多模态学习 | 训练策略 | [Text-Printed Image: Bridging the Image-Text Modality Gap for Text-centric Training of Large Vision-Language Models](cards.md#paper-text-printed-image) | 缺少真实图像时，将描述渲染为伪图送入视觉分支，比仅走文本通道更贴近下游接口。 |
| 多模态学习 | 模型架构 | [HBridge: H-Shape Bridging of Heterogeneous Experts for Unified Multimodal Understanding and Generation](cards.md#paper-hbridge-heterogeneous-experts) | 统一理解与生成时保留各自骨干结构，仅连接可信的中间交互层。 |
| 多模态学习 | 损失函数 | [InsCal: Calibrated Multi-Source Fully Test-Time Prompt Tuning for Object Detection](cards.md#paper-inscal-instance-calibration) | 测试时适配按实例校准熵目标，同时比较准确度及校准，防止强制错误预测变得确定。 |
| 机器人学 | 推理策略 | [ActivePolicy: Active Gaussian Reconstruction and Optimization Strategy Based on Global-Local Information Gain](cards.md#paper-activepolicy-global-local-gain) | 选新视点时将覆盖、渲染质量和观测冗余合并，避免机器人持续访问对最终重建无益的视角。 |
| 机器人学 | 模型架构 | [Unified Number-Free Text-to-Motion Generation Via Flow Matching](cards.md#paper-umf-variable-count-motion) | 将基础运动和后续参与者反应解耦生成，在反应建模中同时重建上下文来缓解级联误差。 |
| 多模态学习 | 推理策略 | [Thinking Diffusion: Penalize and Guide Visual-Grounded Reasoning in Diffusion Multimodal Language Models](cards.md#paper-thinking-diffusion-grounding) | 检查并行解码何时生成答案、何时使用视觉信息，按位置和步骤延后未经验证的答案。 |
| 多模态学习 | 模型架构 | [Mixture of States: Routing Token-Level Dynamics for Multimodal Generation](cards.md#paper-mos-token-state-routing) | 让每个令牌按输入与去噪步决定读取哪一层的其他模态状态。 |
| 多模态学习 | 生成与反馈 | [Visual-Aware CoT: Achieving High-Fidelity Visual Consistency in Unified Models](cards.md#paper-visual-aware-cot-checklist-correction) | 用视觉检查清单追踪生成过程中必须保留的参考属性，再按检查结果迭代修正。 |
| 机器人学 | 时序一致性 | [From Contrast to Consistency: Rethinking Event-based Continuous-Time Optical Flow Estimation](cards.md#paper-stsc-continuous-event-flow-structure) | 对事件相机的连续估计同时约束局部结构和轨迹连贯，避免用锐度代替运动正确性。 |
| 多模态学习 | 训练数据筛选 | [ReCALL: Recalibrating Capability Degradation for MLLM-based Composed Image Retrieval](cards.md#paper-recall-diagnose-generate-refine-retrieval) | 生成模型压缩为检索器后，先定位原有推理能力退化的位置，再按困难样本补训。 |
| 多模态学习 | 解耦训练 | [Wan-Weaver: Interleaved Multi-modal Generation via Decoupled Training](cards.md#paper-wanweaver-text-proxy-visualizer-decoupling) | 用文字代理学习长程图文规划，用参考图学习视觉一致性，缓解交错图文数据不足。 |
| 生成模型 | 免训练编辑 | [ChordEdit: One-Step Low-Energy Transport for Image Editing](cards.md#paper-chordedit-low-energy-single-step-transport) | 将一步编辑视为低能量运输，避免直接做高步幅引导导致背景变化。 |
| 机器人学 | 模型架构 | [RobotSeg: A Model and Dataset for Segmenting Robots in Image and Video](cards.md#paper-articulation-aware-segmentation-memory) | 视频分割可让记忆关联显式适配关节结构和快速形变，减少逐帧掩码及手工提示负担。 |
| 机器学习基础与统计 | 训练策略 | [Tutor-Student Reinforcement Learning: A Dynamic Curriculum for Robust Deepfake Detection](cards.md#paper-learning-history-curriculum-weighting) | 动态课程可根据样本历史损失和遗忘次数调整权重，并由学习反馈更新课程。 |
| 多模态学习 | 模型架构 | [WalkGPT: Grounded Vision-Language Conversation with Depth-Aware Segmentation for Pedestrian Navigation](cards.md#paper-joint-language-mask-relative-depth-grounding) | 空间对话可以同时输出文字、像素区域与相对深度，让用户核查建议的视觉依据。 |
| 机器学习基础与统计 | 优化 | [Learning to Learn Weight Generation via Local Consistency Diffusion](cards.md#paper-local-global-consistency-weight-generation) | 元学习生成权重时，可用局部目标增加密集监督，再以一致性约束保留最终目标。 |
| 计算机视觉 | 推理策略 | [ProOOD: Prototype-Guided Out-of-Distribution 3D Occupancy Prediction](cards.md#paper-separate-rare-classes-voxel-open-set) | 空间开放集预测可同时检查局部 logits 与类别原型，避免将异常吸收到罕见类。 |
| 计算机视觉 | 推理策略 | [3D-LATTE: Latent Space 3D Editing from Textual Instructions](cards.md#paper-3d-latte-latent-editing) | 编辑一致性受视图条件影响时，可在原生三维潜空间中约束目标与源的注意力。 |
| 智能体 | 推理策略 | [Active Intelligence in Video Avatars via Closed-loop World Modeling](cards.md#paper-orca-closed-loop-avatar) | 在生成式环境中预测下一状态，再用真实输出修正信念，减轻长时计划的误差传播。 |
| 计算机视觉 | 优化策略 | [Minimal Constraint Relaxation for Multiview Autocalibration](cards.md#paper-kruppa-minimal-relaxation) | 过约束几何求解可先判断删约束后的有限解与条件数，再选择运行时方程组。 |
| 计算机视觉 | 推理策略 | [SODA: Sensitivity-Oriented Dynamic Acceleration for Diffusion Transformer](cards.md#paper-soda-diffusion-sensitivity) | 离线测每层、每步对近似的敏感度，再按误差预算联合决定缓存和剪枝。 |
| 机器人学 | 模型架构 | [PhysHO: Physics-Based Dynamic 3D Gaussian Human and Object from Monocular Video](cards.md#paper-physho-actuation-prior) | 用人体轨迹作为内部驱动先验，将接触传播与材质响应交给可微物理模型。 |
| 多模态学习 | 评测与诊断 | [CaST-Bench: Benchmarking Causal Chain-Grounded Spatio-Temporal Reasoning for Video Question Answering](cards.md#paper-cast-bench-causal-evidence) | 视频因果问答同时评分结论和时空证据链，以区分真正视觉推理与答案猜测。 |
| 机器学习 | 知识蒸馏 | [Generalizable Knowledge Distillation from Vision Foundation Models for Semantic Segmentation](cards.md#paper-gkd-freeze-domain-general-representations) | 先蒸馏稳健视觉表示并冻结，再训练任务头，避免域内任务直接改写表示。 |
| 机器人学 | 主动感知 | [Coverage Optimization for Camera View Selection](cards.md#paper-converge-underobserved-geometry-coverage) | 下一视角优先覆盖相机尚未充分看见的几何，避免每次估计复杂的透射率。 |
| 计算机视觉 | 训练目标 | [MEMO: Human-like Crisp Edge Detection Using Masked Edge Prediction](cards.md#paper-memo-masked-edge-prediction) | 预测精细稀疏几何时，试用带不同掩蔽率的边缘补全而无需自定义损失。 |
| 多模态学习 | 测试时强化学习 | [TTRV: Test-Time Reinforcement Learning for Vision Language Models](cards.md#paper-ttrv-consensus-based-test-time-reward) | 没有部署标签时，用同一输入多次采样的经验分布建立适配奖励。 |
| 三维视觉 | 点云配准 | [FUSER: Feed-Forward Multiview 3D Registration Transformer and SE(3)$^N$ Diffusion Refinement](cards.md#paper-fuser-joint-se3-multiview-registration) | 在共享潜表征中一次预测多扫描位姿，联合细化避免逐对构图。 |
| 计算机视觉 | 表征学习 | [PointCSP: Cross-Sample Semantic Propagation and Stability Preservation in Self-Supervised Point Cloud Learning](cards.md#paper-cross-sample-state-space-point-ssl) | 点云预训练可在同批不同场景之间传播语义状态，以约束跨场景表征一致性。 |
| 多模态学习 | 训练策略 | [Enhance-then-Balance Modality Collaboration for Robust Multimodal Sentiment Analysis](cards.md#paper-energy-equilibrium-modality-gradient-balancing) | 可先补强弱模态表征，再在可微平衡中协调主导模态与弱模态梯度。 |
| 计算机视觉 | 训练策略 | [EvObj: Learning Evolving Object-centric Representations for 3D Instance Segmentation without Scene Supervision](cards.md#paper-evolve-complete-object-priors-target-domain) | 合成到真实的三维分割可迭代更新对象先验，再以补全判断局部候选是否符合完整物体。 |
| 计算机视觉 | 模型架构 | [Joint Learning of General and Diverse Patterns with Mixture of Memory Experts for Weakly-Supervised Video Anomaly Detection](cards.md#paper-shared-private-memory-expert-routing) | 弱标签任务可给专家分配私有记忆以保持专长，同时用共享记忆提炼跨类规律。 |
| 多模态学习 | 训练策略 | [Efficient Frame Selection for Long Video Understanding via Reinforcement Learning](cards.md#paper-combination-frame-selection-reward) | 关键帧选择器可同时接收单帧相关性和整组答案质量反馈，避免选出重复但各自相关的帧。 |
| 多模态学习 | 训练策略 | [Mask to Align, Weight to Disambiguate: Reliable Unsupervised Cross-Modal Hashing with Masked-Weight Contrast](cards.md#paper-mask-before-fusion-affinity-negative-weighting) | 无监督跨模态对比可在融合前遮蔽输入，再以语义亲和权重降低疑似假负样本的影响。 |
| 机器学习基础与统计 | 优化 | [Neighbor GRPO: Contrastive ODE Policy Optimization Aligns Flow Models](cards.md#paper-initial-noise-neighbors-ode-policy-alignment) | 确定性流生成的候选多样性可以来自初始噪声邻域，使对齐训练兼容原来的 ODE 求解器。 |
| 多模态学习 | 模型架构 | [PIX-TAB: Efficient PIXel-Precise TABle Structure Recognition Approach with Speculative Decoding and Region-Based Image Segmentation](cards.md#paper-pix-tab-coordinate-tokens) | 将语言内容与几何结构解耦，用位置令牌表达结构，并用仅训练期的框监督稳定定位。 |
| 机器人学 | 模型架构 | [SeeGroup: Multi-Layer Depth Estimation of Transparent Surfaces via Self-Determined Grouping](cards.md#paper-seegroup-layered-depth) | 当一个像素对应多个可见表面时，使用按层分解的深度预测，而非以单深度逼近。 |
| 多模态学习 | 训练策略 | [CrossVL: Complexity-Aware Feature Routing and Paired Curriculum for Cross-View Vision-Language Detection](cards.md#paper-crossvl-paired-curriculum) | 跨视角训练先用空间同步对稳定语义，再逐步随机化；运行时可按场景复杂度分配特征路径。 |
| 多模态学习 | 模型架构 | [Grounding Everything in Tokens for Multimodal Large Language Models](cards.md#paper-getok-spatial-vocabulary) | 在自回归输出中以粗网格加细偏移表达坐标，可让空间定位逐步细化。 |
| 多模态学习 | 优化策略 | [VLM-PTQ: Efficient Post-Training Quantization for Large Vision-Language Models](cards.md#paper-vlm-ptq-modality-aware) | 非对称量化应先按已积累的输出残差修正舍入目标，再分别估计视觉和语言通道的重要性。 |
| 计算机视觉 | 模型架构 | [MoVieS: Motion-Aware 4D Dynamic View Synthesis in One Second](cards.md#paper-movies-explicit-motion) | 让前馈三维表示显式预测基元运动，以共享几何支持视角合成与点跟踪。 |
| 机器人学 | 模型架构 | [Affostruction: 3D Affordance Grounding with Generative Reconstruction](cards.md#paper-affostruction-active-affordance) | 对未见区域生成多个可供性假设，并据预测结果选择下一观察视角。 |
| 三维视觉 | 高效几何表示 | [PointCNN++: Performant Convolution on Native Points](cards.md#paper-pointcnn-native-point-convolution) | 在保有原始点坐标的前提下，将点卷积重写为便于并行的矩阵向量运算。 |
| 生成模型 | 偏好优化 | [Mind the Generative Details: Direct Localized Detail Preference Optimization for Video Diffusion Models](cards.md#paper-localdpo-counterfactual-video-regions) | 保留干净样本其余区域，只修改局部以构造明确偏好的反事实视频对。 |
| 机器学习 | 持续学习 | [Is Parameter Isolation Better for Prompt-Based Continual Learning?](cards.md#paper-continual-shared-prompt-activation-protection) | 用稀疏共享提示池替代固定分任务参数，再依据历史使用率保护高复用提示。 |
| 机器人学 | 策略纠错 | [Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation](cards.md#paper-afi-on-demand-spatial-affordance-intervention) | 用执行信号识别重复失误，只在需要时调用三维可供性场修正策略。 |
| 高效深度学习 | 模型量化 | [CAR-SAM: Cross-Attention Reconstruction for Post-Training Quantization of the Segment Anything Model](cards.md#paper-carsam-cross-attention-quantization-reconstruction) | 量化交叉注意力解码器时，重建注意力信息，并将双向耦合误差纳入校准。 |
| 计算机视觉 | 表征学习 | [Vision Transformers Need More Than Registers](cards.md#paper-selective-cls-background-shortcut) | ViT 中异常高范数并非伪影的充分诊断，限制背景块参与 CLS 聚合可直接抑制捷径。 |
| 计算机视觉 | 表征学习 | [Evidential Neural Radiance Fields](cards.md#paper-single-pass-evidential-radiance-uncertainty) | 三维渲染可在一次前向中同时估算数据噪声和模型知识不足，避免把二者混成单一质量分。 |
| 计算机视觉 | 推理策略 | [ThinkingViT: Matryoshka Thinking Vision Transformer for Elastic Inference](cards.md#paper-confidence-routed-nested-attention-heads) | 弹性 ViT 可以用小头集合先判别，再仅对低置信度样本激活更多头。 |
| 多模态学习 | 推理策略 | [Progress by Pieces: Test-Time Scaling for Autoregressive Image Generation](cards.md#paper-grid-progressive-partial-image-search) | 自回归图像的推理时搜索可以比较同一网格区域的多个局部进度并提前剪枝。 |
| 多模态学习 | 训练策略 | [Cluster-Aware Neural Collapse Prompt Tuning for Long-Tailed Generalization of Vision-Language Models](cards.md#paper-cluster-local-neural-collapse-prompts) | 长尾提示微调可按预训练语义簇施加类间几何约束，保护全局泛化结构。 |
| 多模态学习 | 表征学习 | [Prompt Yourself: Awakening Textual Semantics in 1D Visual Tokenizers](cards.md#paper-train-only-language-alignment-visual-tokenizer) | 图像 tokenizer 可在训练期生成文本表征辅助视觉编码，使推理仍只需要图像。 |
| 多模态学习 | 表征学习 | [Uncertainty-Aware Modality Fusion for Unaligned RGB-T Salient Object Detection](cards.md#paper-uncertainty-gating-unaligned-sensors) | 传感器空间未对齐时，可估计局部表示不确定性，只在有共识区域增强跨模态融合。 |
| 计算机视觉 | 表征学习 | [MD2E: Modeling Depth-to-Edge Cues for Monocular Metric Depth Estimation](cards.md#paper-edge-spectrum-metric-depth-scale) | 单目深度尺度未知时，可用预测边缘的频谱统计作为附加尺度证据。 |
| 计算机视觉 | 训练策略 | [GenSplat: Bridging the Generalization Gap in 3DGS Language Comprehension](cards.md#paper-gensplat-progressive-grounding) | 先对齐类别，再对齐实例，最后对齐自由形式查询，以减少三维语言模型对单场景的过拟合。 |
| 计算机视觉 | 推理策略 | [Coupled Diffusion Sampling for Training-Free Multi-View Image Editing](cards.md#paper-coupled-diffusion-multiview) | 部署时让具有不同能力的两个扩散模型交互采样，以保留编辑语义和跨视角一致性。 |
| 多模态学习 | 推理策略 | [Video Panels for Long Video Understanding](cards.md#paper-video-panels-temporal-budget) | 固定视觉输入预算下，用多帧面板换取时间覆盖，并根据问题是否依赖细节选择拼接程度。 |
| 计算机视觉 | 模型架构 | [PhyGaP: Physically-Grounded Gaussians with Polarization Cues](cards.md#paper-phygap-polarization) | 反光物体光度约束不足时，可增加部分偏振观测来分解材质与反射。 |
| 机器学习基础与统计 | 损失函数 | [Distilling Balanced Knowledge from a Biased Teacher](cards.md#paper-ltkd-groupwise-distillation) | 蒸馏时分离组间先验和组内判别，校准教师在长尾类别上的偏置。 |
| 多模态学习 | 训练策略 | [Learning Transferable Temporal Primitives for Video Reasoning via Synthetic Videos](cards.md#paper-synrl-temporal-primitives) | 用时间标签可精确生成的简单视频训练基础运动推理，再用真实数据验证迁移。 |
| 计算机视觉 | 训练策略 | [UnReflectAnything: RGB-Only Highlight Removal by Rendering Synthetic Specular Supervision](cards.md#paper-unreflectanything-specular-supervision) | 用几何一致的合成高光监督局部干扰定位，再在特征中恢复受损区域。 |
| 机器学习基础与统计 | 训练策略 | [Understanding, Accelerating, and Improving MeanFlow Training](cards.md#paper-meanflow-velocity-curriculum) | 先学习瞬时和短间隔平均速度，再强化长间隔目标，可减少少步生成中的梯度冲突。 |
| 高效深度学习 | 测试时适配 | [FOZO: Forward-Only Zeroth-Order Prompt Optimization for Test-Time Adaptation](cards.md#paper-fozo-forward-only-prompt-adaptation) | 部署端只能运行前向时，用零阶扰动更新小型提示参数。 |
| 多模态学习 | 评测设计 | [VisualOverload: Probing Visual Understanding of VLMs in Really Dense Scenes](cards.md#paper-visualoverload-dense-detail-diagnostic) | 用知识需求低但视觉负载高的场景检验细节识别，并用分辨率消融区分输入瓶颈。 |
| 机器人学 | 动作表征 | [Language-Grounded Decoupled Action Representation for Robotic Manipulation](cards.md#paper-lada-language-grounded-action-primitives) | 把平移、旋转和夹爪分开建模，并用语言相似性定义动作软标签。 |
| 生成模型 | 多尺度架构 | [PixelDiT: Pixel Diffusion Transformers for Image Generation](cards.md#paper-pixeldit-patch-pixel-hierarchical-diffusion) | 将全局语义放在 patch 级，把细纹理留给压缩后的像素 token，从而在像素空间端到端训练。 |
| 多模态学习 | 时序推理 | [Video-CoE: Reinforcing Video Event Prediction via Chain of Events](cards.md#paper-video-coe-event-chain-training) | 将未来预测的中间监督写成连续事件链，让模型显式关联观察与后续事件。 |
