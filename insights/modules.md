# 模块

[首页](../README.md) · [参与贡献](../CONTRIBUTING.md) · [English](../en/insights/modules.md)

可复用组件与局部连接方式。

<!-- classification:start -->
## 按研究领域浏览

[大语言模型](#by-llm) · [计算机视觉](#by-computer-vision) · [自然语言处理](#by-nlp) · [强化学习](#by-reinforcement-learning) · [机器人学](#by-robotics) · [多模态学习](#by-multimodal) · [机器学习基础与统计](#by-ml-foundations) · [图学习与推荐](#by-graph-and-recommendation) · [科学机器学习](#by-scientific-ml)

<a id="by-llm"></a>

### 大语言模型

- [线性注意力记忆](../conferences/icml-2026/cards/0301-0400.md#bonnet26a-modules) · Learning to Remember, Learn, and Forget in Attention-Based Models
- [归一化替换](../conferences/icml-2026/cards/0301-0400.md#byun26a-modules) · Bounded Hyperbolic Tangent: A Stable and Efficient Alternative to Pre-Layer Normalization in Large Language Models
- [深层 Transformer 归一化](../conferences/icml-2026/cards/0401-0500.md#chao26b-modules) · SpanNorm: Reconciling Training Stability and Performance in Deep Transformers
- [上下文转 LoRA](../conferences/icml-2026/cards/0401-0500.md#charakorn26a-modules) · Doc-to-LoRA: Learning to Instantly Internalize Contexts
- [MoE 持续学习](../conferences/icml-2026/cards/0501-0600.md#chen26aw-modules) · Multi-Head Attention as a Source of Catastrophic Forgetting in MoE Transformers
- [线性投影后的局部归一化](../conferences/icml-2026/cards/0501-0600.md#chen26dj-modules) · SimpleGPT: Improving GPT via A Simple Normalization Strategy
- [独立价值空间的桥接词元](../conferences/icml-2026/cards/0501-0600.md#chen26dw-modules) · Toward Stable Value Alignment: Introducing Independent Modules for Consistent Value Guidance
- [逐词元全局注意力路由](../conferences/icml-2026/cards/0701-0800.md#choudhary26a-modules) · Learning When to Attend: Conditional Memory Access for Long-Context LLMs
- [连分式因果 token 混合](../conferences/icml-2026/cards/0801-0900.md#dhurandhar26a-modules) · CoFrGeNet: Continued Fraction Architectures for Language Generation
- [基于专家权重谱的免训练路由](../conferences/icml-2026/cards/0901-1000.md#do26a-modules) · Eigenvectors of Experts are Training-free Non-collapsing Routers
- [键相似度预调节注意力](../conferences/icml-2026/cards/1001-1100.md#duvvuri26a-modules) · LUCID: Attention with Preconditioned Representations
- [逐解码步的潜空间经验检索](../conferences/icml-2026/cards/1101-1200.md#feng26i-modules) · ExpWeaver: LLM Agents Learn from Experience via Latent RAG
- [MoE 专家输出的有向图聚合](../conferences/icml-2026/cards/1101-1200.md#feng26v-modules) · DAG-MoE: From Simple Mixture to Structural Aggregation in Mixture-of-Experts
- [Softplus 注意力的两阶段重加权](../conferences/icml-2026/cards/1201-1300.md#gao26y-modules) · Softplus Attention with Re-weighting Boosts Length Extrapolation in Large Language Models
- [稀疏 entmax 的直方图阈值初始化](../conferences/icml-2026/cards/1301-1400.md#goncalves26a-modules) · AdaSplash-2: Faster Differentiable Sparse Attention
- [把重遮盖位置的高熵表征留给下轮去噪](../conferences/icml-2026/cards/1601-1700.md#hu26as-modules) · Residual Context Diffusion Language Models
- [在自回归推理中保存耗散的连续隐状态](../conferences/icml-2026/cards/1601-1700.md#huang26m-modules) · Thinking in Flow: A Dissipative Stabilization Operator for Robust Autoregressive Reasoning
- [以分块偏置校准抑制压缩误差累积](../conferences/icml-2026/cards/1701-1800.md#huang26q-modules) · Representation Drift Compensation: A Near-Zero Inference Cost Enhancement for LLM Decomposition
- [让超网络按文本调节前馈门控斜率](../conferences/icml-2026/cards/1801-1900.md#ji26i-modules) · Learn-to-learn on Arbitrary Textual Conditioning: A Hypernetwork-Driven Meta-gated LLM
- [用反馈锁定 MoE 动态路由的平均预算](../conferences/icml-2026/cards/1901-2000.md#jin26f-modules) · DTop-p MoE: Sparsity-Controlled Dynamic Top-p MoE for Foundation Model Pre-training
- [用共同激活记录抑制 MoE 专家组合冗余](../conferences/icml-2026/cards/2001-2100.md#kang26q-modules) · Breaking the Echo Chamber: A Dynamic Ensemble Pruning Perspective on MoE
- [用可相加的推理 logits 复用轻量模块](../conferences/icml-2026/cards/2001-2100.md#kim26f-modules) · Universal Reasoner: A Single, Composable Plug-and-Play Reasoner for Frozen LLMs
- [把注意力权重当高阶张量做 Tucker 分解](../conferences/icml-2026/cards/2101-2200.md#klein26a-modules) · Tucker Attention: A generalization of approximate attention mechanisms
- [用结构探针定位表格超图的注入层](../conferences/icml-2026/cards/2301-2400.md#lee26p-modules) · HInT: Hypergraph Infusion at the Structural Layers Improves Table Understanding
- [在值聚合后修正位置方差](../conferences/icml-2026/cards/2401-2500.md#li26bs-modules) · The Structural Origin of Attention Sink: Variance Discrepancy, Super Neurons, and Dimension Disparity
- [按查询路由从多域抽取的注意力方向](../conferences/icml-2026/cards/2401-2500.md#li26cd-modules) · Train Once, Reuse Everywhere: Generalizable Implicit In-Context Learning by Routing Attention
- [借 RMSNorm 的尺度消除把逐维遗忘施加在值上](../conferences/icml-2026/cards/2501-2600.md#li26dl-modules) · FiX: Introducing Fine-grained Forget Gate into Softmax Attention
- [只对专家选择建模贝叶斯不确定性](../conferences/icml-2026/cards/2601-2700.md#li26hj-modules) · Variational Routing: A Scalable Bayesian Framework for Calibrated Mixture-of-Experts Transformers
- [用激活缩放和位移竞争构建脉冲注意力](../conferences/icml-2026/cards/2701-2800.md#liang26ae-modules) · SpikingLM: Towards Fully Spiking Language Model
- [把 LoRA 权重增量写成稀疏高斯过程后验](../conferences/icml-2026/cards/2701-2800.md#lin26j-modules) · Bayesian-LoRA: Probabilistic Low-Rank Adaptation of Large Language Models
- [把结构先验从注意力语义键中拆出](../conferences/icml-2026/cards/2701-2800.md#litman26a-modules) · You Need Better Attention Priors
- [查询依赖的多极近似注意力](../conferences/icml-2026/cards/3301-3400.md#mitchell26a-modules) · Multipole Semantic Attention: A Fast Approximation of Softmax Attention for Pretraining
- [让查询读出反馈参与线性记忆写入](../conferences/icml-2026/cards/3501-3600.md#park26f-modules) · Q-Delta: Beyond Key–Value Associative State Evolution
- [用在线主子空间辅助 MoE 路由](../conferences/icml-2026/cards/3501-3600.md#park26u-modules) · STAR: Rethinking MoE Routing as Structure-Aware Subspace Learning
- [概念方向进入解释提示的校准](../conferences/icml-2026/cards/3601-3700.md#pepper26a-modules) · Learning Self-Interpretation from Interpretability Artifacts: Training Lightweight Adapters on Vector-Label Pairs
- [传输历史表示再按预测精度注意](../conferences/icml-2026/cards/3701-3800.md#racioppo26a-modules) · Robust Filter Attention: Self-Attention as Precision-Weighted State Estimation
- [按归一化权重适度削弱注意力汇聚](../conferences/icml-2026/cards/4101-4200.md#shi26y-modules) · A Single Layer to Explain Them All: Understanding Massive Activations in Large Language Models
- [用频率幅度调制形成多尺度位置核](../conferences/icml-2026/cards/4101-4200.md#shujun26a-modules) · The Hippocampal Place Field Gradient: A Bio-inspired Framework Building Multiscale Representation for Better Sample Efficiency
- [潜图后验条件化适配](../conferences/icml-2026/cards/4201-4300.md#song26ad-modules) · iLoRA: Bayesian Low-Rank Adaptation with Latent Interaction Graphs for Microbiome Diagnosis
- [triangular-mixing-sidepath](../conferences/icml-2026/cards/4401-4500.md#tao26b-modules) · The Devil is in the Spectrum: Mitigating Representation Collapse in LLMs via Topologically Regularized Side-Path
- [潜空间最优控制层](../conferences/icml-2026/cards/4801-4900.md#wang26jt-modules) · Beyond Test-Time Memory: State-Space Optimal Control for LLM Reasoning
- [跨层共享噪声条件低秩核心](../conferences/icml-2026/cards/4901-5000.md#wang26lt-modules) · NaRA: Noise-Aware LoRA for Parameter-Efficient Fine-Tuning of Diffusion LLMs
- [以功能对而非单矩阵压缩](../conferences/icml-2026/cards/4901-5000.md#wong26b-modules) · A3: an Analytical Low-Rank Approximation Framework for Attention
- [Khatri-Rao结构的参数高效更新](../conferences/icml-2026/cards/5201-5300.md#xu26ae-modules) · Low Kruskal-Rank Adaptation
- [无查表trellis计算码](../conferences/icml-2026/cards/5301-5400.md#yang26ah-modules) · Proteus: Lookup-Free Trellis-Coded Quantization by Lattice-Breaking Compute Codes for 2-Bit LLMs
- [token索引的逐层残差调制向量](../conferences/icml-2026/cards/5401-5500.md#yang26cj-modules) · Inner-layer Token Self-modulation as Another Scaling Axis for LLMs
- [软topk预算与跨层激活分配](../conferences/icml-2026/cards/5601-5700.md#zasada26a-modules) · SoftMoE: Soft Differentiable Routing for Mixture-of-Experts in LLMs

<a id="by-computer-vision"></a>

### 计算机视觉

- [主动视觉分辨率](../conferences/icml-2026/cards/0201-0300.md#blauch26a-modules) · FOVI: A biologically-inspired foveated interface for deep vision models
- [小型视觉 Transformer](../conferences/icml-2026/cards/0301-0400.md#candogan26a-modules) · Spatial Priors via Space Filling Curves for Small and Limited Data Vision Transformers
- [分层三维语义分割](../conferences/icml-2026/cards/0301-0400.md#cao26j-modules) · Multi-Label Learning with Contrastive Cluster Self-Supervision for 3D Hierarchical Semantic Segmentation
- [轻量视频超分](../conferences/icml-2026/cards/0301-0400.md#cao26n-modules) · LiteVSR: Lightweight Adaptation of Frozen Diffusion Transformers for Video Super-Resolution
- [结构化图像生成](../conferences/icml-2026/cards/0401-0500.md#cao26ab-modules) · StructMAR: Structure-Aware Masked Autoregression for Explicit Layout Alignment in Text-to-Image Generation
- [视频超分的小波编码前端](../conferences/icml-2026/cards/0501-0600.md#chen26ce-modules) · WEVSR: Video Diffusion Generators for Real-World Video Super-Resolution with Wavelet-Enhanced VAE Encoder
- [ViT 多层注意力探针](../conferences/icml-2026/cards/0701-0800.md#ciernik26a-modules) · Attentive Multi-Layer Fusion for Vision Transformers
- [视觉概念瓶颈的原型证据](../conferences/icml-2026/cards/0701-0800.md#colamonaco26a-modules) · Prototype-Grounded Concept Models for Verifiable Concept Alignment
- [卷积权重与特征的双空间扰动](../conferences/icml-2026/cards/0801-0900.md#dhar26a-modules) · Does a Hybrid Space-Aware Randomized Defense Improve Empirical and Certified Adversarial Robustness?
- [偏振物理先验的透明物体深度](../conferences/icml-2026/cards/0901-1000.md#dong26i-modules) · PolarDepth: Monocular Transparent Object Depth from Polar-Physics Priors
- [人体视频的非对称身份注意力](../conferences/icml-2026/cards/1401-1500.md#guo26ad-modules) · WildActor: Unconstrained Identity-Preserving Video Generation
- [超分辨率的跨尺度词元前缀](../conferences/icml-2026/cards/1401-1500.md#hadji26a-modules) · Hierarchical Image Tokenization for Multi-Scale Image Super Resolution
- [用三维表面坐标连接跨姿态参考](../conferences/icml-2026/cards/1401-1500.md#han26ab-modules) · Pose-ICL: 3D-Aware In-Context Learning for Pose-Controllable Subject Customization
- [用局部退化控制分块采样与回写](../conferences/icml-2026/cards/1501-1600.md#he26an-modules) · Bend the Basics: Degradation-Aware Deformable Tokenization for All-in-One Image Restoration
- [把修正点击变成连通误差区](../conferences/icml-2026/cards/1601-1700.md#hu26au-modules) · Interactive Segmentation with Elaborate Focus Prior
- [用逐元素门控降低脉冲注意力通信](../conferences/icml-2026/cards/1901-2000.md#jiang26an-modules) · Efficient Transformer Attention for SNNs via Hadamard Simplification
- [从局部频谱提取风格并路由检测适配词元](../conferences/icml-2026/cards/1901-2000.md#jiang26ay-modules) · SCoA: Revisiting Domain Generalized Object Detection with Style-Conditioned Adaptation
- [用上下文偏移决定状态空间模型读哪里](../conferences/icml-2026/cards/2001-2100.md#ke26d-modules) · Deformba: Vision State Space Model with Adaptive State Fusion
- [按可靠度门控视频预测记忆](../conferences/icml-2026/cards/2101-2200.md#kim26by-modules) · Memory as Dynamics: Learning Reliability-Guided Predictive Models for Online Video Perception
- [用可分解转换器编辑内部生成特征](../conferences/icml-2026/cards/2201-2300.md#kumar26c-modules) · Concept Removal for Frontier Image Generative Models
- [按模态对临时组合协同感知转换器](../conferences/icml-2026/cards/2401-2500.md#li26cm-modules) · One Model to Translate Them All: Universal Any-to-Any Translation for Heterogeneous Collaborative Perception
- [协同感知协议里的模态统计干预](../conferences/icml-2026/cards/2401-2500.md#li26cn-modules) · CauseCollab: Causal Unified and Modality-Agnostic Network for Heterogeneous Collaborative Perception
- [从输入残差和视觉子空间双重恢复失真信号](../conferences/icml-2026/cards/2501-2600.md#li26ff-modules) · Bridging the Perceptual Gap: Residual-Enhanced Downscaling and Manifold-Aware Perception Alignment Adaptation for NR-IQA
- [惯性补全与脉冲置信门联合修复退化感知](../conferences/icml-2026/cards/2501-2600.md#li26fi-modules) · NeuroMamba: A Universal Spatiotemporal Module for Robust Perception in Degraded Sensory Streams
- [按几何置信度调节驾驶视频编辑的纹理参考](../conferences/icml-2026/cards/2701-2800.md#liang26z-modules) · SceneDirector: Bridging Explicit Geometry and Generative Priors for Unified Driving Scene Editing
- [用可变形采样找回错位的多视图渲染线索](../conferences/icml-2026/cards/2701-2800.md#lim26c-modules) · GADA: Geometry-Aware Deformable Aggregation for Image-Based Gaussian Splatting
- [异构车路感知的逐像素对齐](../conferences/icml-2026/cards/2701-2800.md#lin26y-modules) · X-MoGe: A Cross-Modal Adaptation Framework with Mixture-of-Experts and Geometry Guidance for Heterogeneous Collaborative Perception
- [用相机位姿引导时空深度特征匹配](../conferences/icml-2026/cards/2801-2900.md#liu26v-modules) · GemDepth: Geometry-Embedded Features for 3D-Consistent Video Depth
- [体素化前径向缩放保留近处小目标细节](../conferences/icml-2026/cards/2901-3000.md#liu26gn-modules) · Radial Scaling Voxelization for Accurate Small Object 3D Detection
- [视觉适配器的阶段共享与动态权重](../conferences/icml-2026/cards/2901-3000.md#lou26i-modules) · Parameters as Experts: Adapting Vision Models with Dynamic Parameter Routing
- [恢复线性注意力中的查询范数](../conferences/icml-2026/cards/3201-3300.md#meng26g-modules) · Norm$\times$Direction: Restoring the Missing Query Norm in Vision Linear Attention
- [矢量地图不确定性](../conferences/icml-2026/cards/3301-3400.md#mo26e-modules) · MapUQ: Map with Uncertainty Quantification for Robust BEV Vectorized Construction
- [联合通道激活统计与决策权重控制激活门](../conferences/icml-2026/cards/3701-3800.md#qiu26e-modules) · Activation with Intrinsic-Extrinsic Consensus
- [在任意图像骨干前后包裹归一化来保证等变](../conferences/icml-2026/cards/3901-4000.md#saied26a-modules) · Normalization Equivariance for Arbitrary Backbones, with Application to Image Denoising
- [把球面大圆距离嵌进注意力点积](../conferences/icml-2026/cards/3901-4000.md#sekikawa26a-modules) · Spherical SO(3) Equivariant Local Attention
- [将脉冲通道稀疏变为边缘设备可执行的结构压缩](../conferences/icml-2026/cards/4001-4100.md#she26b-modules) · Spik4lite: Refactoring Neuromorphic Sparsity for Efficient Spiking Neural Networks on Commodity Edge Devices
- [将软视差指导与分层像素选择分开](../conferences/icml-2026/cards/4101-4200.md#shi26h-modules) · ImmersePro: End-to-End Stereo Video Synthesis Via Implicit Disparity Learning
- [窗口Toeplitz矩阵缓存](../conferences/icml-2026/cards/4201-4300.md#song26ae-modules) · WBMM: Windowed Batch Matrix Multiplication for Efficient Large Receptive Field Convolution
- [连续肢体采样补充关节点](../conferences/icml-2026/cards/4301-4400.md#tang26p-modules) · Glimpse: Geometry Learning of Multi-scale Structural Priors for 3D Pose Estimation
- [primitive-membership-calibration](../conferences/icml-2026/cards/4301-4400.md#tang26ai-modules) · CoGe-GCD: Reframing Generalized Category Discovery with Compositional Generalization
- <a id="widen-the-student-distillation-interface"></a><a id="distillation-interface-design"></a>[只加宽学生模型的蒸馏接口](../conferences/icml-2026/cards/4401-4500.md#tian26k-modules) · From Per-Image Low-Rank to Encoding Mismatch: Rethinking Feature Distillation in Vision Transformers
- [局部注意力加全局值均值](../conferences/icml-2026/cards/4401-4500.md#tran26g-modules) · SEMA: a Scalable and Efficient Mamba like Attention via Token Localization and Averaging
- [可见区域限制控制残差](../conferences/icml-2026/cards/4601-4700.md#wang26af-modules) · EPiC: Efficient Video Camera Control Learning with Precise Anchor-Video Guidance
- [语义簇软路由分类器残差](../conferences/icml-2026/cards/4601-4700.md#wang26bg-modules) · Granularity-Aware Adaptive Classifier Expansion via Zero-Shot Learning
- [异质感受野乘法与深层稳定化](../conferences/icml-2026/cards/4601-4700.md#wang26bj-modules) · Activation-Free Backbones for Image Recognition: Polynomial Alternatives within MetaFormer-Style Vision Models
- [局部单纯形几何提示](../conferences/icml-2026/cards/4601-4700.md#wang26br-modules) · TopAdapter: Topology-Aware Prompt Tuning for Efficient Point Cloud Understanding
- [双层事件微动态解耦](../conferences/icml-2026/cards/4601-4700.md#wang26cx-modules) · EvReflection: Event-Driven Micro-Dynamics for Reflection Removal
- [可测退化指标路由修复专家](../conferences/icml-2026/cards/4801-4900.md#wang26hr-modules) · Degradation-Aware Metric Prompting for Hyperspectral Image Restoration
- [输入条件化各向异性频域门](../conferences/icml-2026/cards/4801-4900.md#wang26hx-modules) · Butterworth as Attention: Anisotropic Spectral Gating for Pansharpening
- [饱和局部像素差作为编辑痕迹](../conferences/icml-2026/cards/4801-4900.md#wang26iy-modules) · Order within Chaos: Capturing Intrinsic Energy Anomalies for AI-Manipulated Image Forgery Localization
- [静态不变分支相减](../conferences/icml-2026/cards/4901-5000.md#wei26y-modules) · Return of Frustratingly Easy Unsupervised Video Domain Adaptation
- [非稀疏视频head的帧块原型复用](../conferences/icml-2026/cards/5101-5200.md#xia26c-modules) · EchoAttention: Exploiting Token-Pair Redundancy and Frame-Block Similarity for Efficient Video Generation
- [两时间源特征的三维编辑引导](../conferences/icml-2026/cards/5101-5200.md#xia26h-modules) · Towards Scalable and Consistent 3D Editing
- [逐层同步的相位注意力](../conferences/icml-2026/cards/5101-5200.md#xiao26r-modules) · Kuramoto Oscillatory Phase Encoding: Neuro-inspired Synchronization for Improved Learning Efficiency
- [按维度KL预算约束的随机码本量化](../conferences/icml-2026/cards/5201-5300.md#xu26cn-modules) · Training-Free Vector Quantization via Gaussian VAEs
- [全景球面距离与轨迹条件注意力](../conferences/icml-2026/cards/5501-5600.md#yin26a-modules) · PanoWorld-X: Generating Explorable Panoramic Worlds via Sphere-Aware Video Diffusion
- [单扫描交换摘要并折叠短序列batch](../conferences/icml-2026/cards/5501-5600.md#yoshimura26a-modules) · SF-Mamba: Rethinking State Space Model for Vision
- [随机子空间补投影的压缩扩张层](../conferences/icml-2026/cards/5601-5700.md#yu26bp-modules) · PACEAttention: Principled and Adaptive Feature Compression-Expansion Grounded in the Geometry of $\textMCR^2$

<a id="by-nlp"></a>

### 自然语言处理

- [Agent 词表适配](../conferences/icml-2026/cards/0201-0300.md#bian26c-modules) · AgentVocab: Structure-Aware Vocabulary Adaptation for Efficient LLM Agents
- [把低资源语种锚到英语语义并用语言感知头融合](../conferences/icml-2026/cards/2601-2700.md#li26jh-modules) · Toward Robust Multilingual Adaptation of LLMs for Low-Resource Languages
- [用固定二维格点替代独立标量量化](../conferences/icml-2026/cards/4101-4200.md#shuster26a-modules) · Two-dimensional quantization for geometry-aware audio coding

<a id="by-reinforcement-learning"></a>

### 强化学习

- [扩大动作值均值以共享 TD 信号](../conferences/icml-2026/cards/3301-3400.md#nagarajan26a-modules) · Accelerating Q-learning through Efficient Value-Sharing across Actions
- [surrogate-equilibrium-gradient](../conferences/icml-2026/cards/4401-4500.md#thoma26b-modules) · Deep Incentive Design with Differentiable Equilibrium Blocks

<a id="by-robotics"></a>

### 机器人学

- [视觉动作策略的连续网格采样](../conferences/icml-2026/cards/1101-1200.md#feng26x-modules) · See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model
- [视觉动作模型的通道相关门控](../conferences/icml-2026/cards/1101-1200.md#fu26x-modules) · StableVLA: Towards Robust Vision-Language-Action Models without Extra Data
- [精密操作的点云傅里叶编码](../conferences/icml-2026/cards/1401-1500.md#gyenes26a-modules) · Fourier Features Let Agents Learn High Precision Policies with Imitation Learning
- [用行为检索和上下文间隔约束动作](../conferences/icml-2026/cards/1801-1900.md#jang26c-modules) · RA-VLA: Retrieval-Augmented VLA for Test-Time Adaptation
- [按多时域动作预测的共识决定执行长度](../conferences/icml-2026/cards/1901-2000.md#jing26f-modules) · Mixture of Horizons in Action Chunking
- [视野外操作的持续空间记忆](../conferences/icml-2026/cards/2401-2500.md#li26ay-modules) · Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action
- [constrained-koopman-variable-elimination](../conferences/icml-2026/cards/4401-4500.md#tian26f-modules) · QPKO: Differentiable QP-Embedded Deep Koopman Framework for Modeling Nonlinear Systems
- [微平面残余应力适配](../conferences/icml-2026/cards/4601-4700.md#wang26bv-modules) · MoSA: Motion-constrained Stress Adaptation for Mitigating Real-to-Sim Gap in Continuum Dynamics via Learning Residual Anisotropy
- <a id="instruction-prefixes-for-causal-visual-grounding"></a><a id="multimodal-token-layout"></a>[用指令前缀让视觉表征感知任务](../papers/reconvla.md#reconvla-modules) · ReconVLA

<a id="by-multimodal"></a>

### 多模态学习

- [细粒度视觉定位](../conferences/icml-2026/cards/0201-0300.md#barrios26a-modules) · MoDA: Modulation Adapter for Fine-Grained Visual Understanding in Instructional MLLMs
- [非对称 RGB-D 特征融合](../conferences/icml-2026/cards/0501-0600.md#chen26ch-modules) · Hamiltonian Asymmetric Fusion: One-Way Safe Directed Refinement under Modality Imbalance
- [缺失模态的结构化提示](../conferences/icml-2026/cards/0501-0600.md#chen26dv-modules) · SPR: A Structured Prompt Refinement Network for Modality Missing
- [音视频非对称 token 压缩](../conferences/icml-2026/cards/0901-1000.md#ding26e-modules) · OmniSIFT: Modality-Asymmetric Token Compression for Efficient Omni-modal Large Language Models
- [视听稀疏采样的 RoPE 抗混叠](../conferences/icml-2026/cards/1301-1400.md#gong26g-modules) · EchoingPixels: Aliasing-Resistant Joint Token Reduction for Audio-Visual LLMs
- [用位置编码绑定人物与音色](../conferences/icml-2026/cards/1401-1500.md#guo26af-modules) · DreamID-Omni: Unified Framework for Controllable Human-Centric Audio-Video Generation
- [放松传输边缘约束以减少不可靠视图的影响](../conferences/icml-2026/cards/1401-1500.md#han26aa-modules) · Robust Multi-View Fusion via Prototype-Anchored Unbalanced Optimal Transport
- [分开抽取实例和文本角色来推断假设编辑](../conferences/icml-2026/cards/1401-1500.md#he26b-modules) · Reasoning to Edit: Hypothetical Instruction-Based Image Editing with Visual Reasoning
- [将追踪专家与模态专家分工](../conferences/icml-2026/cards/1501-1600.md#hong26g-modules) · Unified Multimodal Visual Tracking with Dual Mixture-of-Experts
- [让推理过程主动发起稀疏查证](../conferences/icml-2026/cards/1601-1700.md#hu26ba-modules) · TVI-CoT: Text-Visual Interleaved Chain-of-Thought Reasoning for Multimodal Understanding
- [用专家向量调制共享适配器](../conferences/icml-2026/cards/2201-2300.md#kowsher26a-modules) · LiME: Lightweight Mixture of Experts for Efficient Multimodal Multi-task Learning
- [用同帧查询和重要性门按需读取几何](../conferences/icml-2026/cards/2401-2500.md#li26j-modules) · Thinking with Geometry: Active Geometry Integration for Spatial Reasoning
- [以可微软投影保留稀疏点云的视觉连接](../conferences/icml-2026/cards/2601-2700.md#li26io-modules) · SplAttN: Bridging 2D and 3D with Gaussian Soft Splatting and Attention for Point Cloud Completion
- [脉冲集合相似度纠正注意力密度偏差](../conferences/icml-2026/cards/2701-2800.md#lim26a-modules) · Rethinking Attention in Spiking Transformers: Overcoming Density Bias with Set Similarity
- [视觉证据与推理约束的双潜记忆](../conferences/icml-2026/cards/3101-3200.md#ma26ac-modules) · Dual-Latent Memory Routing for Vision-Language Reasoning
- [共用跨模态适配器学习视频质量而非类别语义](../conferences/icml-2026/cards/3201-3300.md#mi26c-modules) · Q-CLIP: Unleashing the Power of Vision-Language Models for Video Quality Assessment through Unified Cross-Modal Adaptation
- [频谱可靠性融合门控](../conferences/icml-2026/cards/3501-3600.md#pan26d-modules) · Difference-Aware Decision Learning for Multimodal Image Fusion
- [分割词元跨层选择空间热图](../conferences/icml-2026/cards/3701-3800.md#qian26m-modules) · UGround: Towards Unified Visual Grounding with Unrolled Transformers
- [按查询近似风险调注意力算量](../conferences/icml-2026/cards/4001-4100.md#shao26k-modules) · LIVEditor-14B: Lightning Unified Video Editing via In-Context Sparse Attention
- [用时间片段补充音源语义](../conferences/icml-2026/cards/4101-4200.md#shi26u-modules) · SAM Audio: Segment Anything in Audio
- [运动同步度调节场景条件强度](../conferences/icml-2026/cards/4101-4200.md#singh26g-modules) · VIBE: Disentangling Social Dynamics via Kinematics-Informed Variational Inference for Behavioral Emotion
- [跨模态低秩中间矩阵](../conferences/icml-2026/cards/4201-4300.md#suharitdamrong26a-modules) · CoLA: Cross-Modal Low-rank Adaptation for Multimodal Downstream Tasks
- [long-span-fast-weight-memory](../conferences/icml-2026/cards/4201-4300.md#sun26s-modules) · video-SALMONN S: Memory-Enhanced Streaming Audio-Visual LLM
- [conflict-aware-evidence-fusion](../conferences/icml-2026/cards/4401-4500.md#tian26i-modules) · A Conflict-aware Evidential Framework for Reliable Sleep Stage Classification
- [类时序原型的定向插补](../conferences/icml-2026/cards/4601-4700.md#wang26az-modules) · API: Adaptive Prototype Imputation for Incomplete Multimodal Sentiment Analysis
- [等半径圆周索引与交替几何](../conferences/icml-2026/cards/4601-4700.md#wang26bo-modules) · Circle-RoPE: Cone-like Decoupled Rotary Positional Embedding for Vision-Language Models
- [原型漂移下解析ETF旋转](../conferences/icml-2026/cards/4601-4700.md#wang26ce-modules) · Spherical Procrustes Alignment for Reliable Medical Audio Diagnosis
- [相似特征的非对称最优传输](../conferences/icml-2026/cards/4601-4700.md#wang26cj-modules) · TranX-Adapter: Bridging Artifacts and Semantics within MLLMs for Robust AI-generated Image Detection
- [共享分量循环交换的重建融合](../conferences/icml-2026/cards/5201-5300.md#xiong26m-modules) · Multimodal Fusion via Self-Consistent Task-Gradient Fields
- [CP编辑因子兼作专家路由](../conferences/icml-2026/cards/5201-5300.md#xu26bi-modules) · TIME: Tensor-Factorized Mixture-of-Experts with Intrinsic Routing for Lifelong Multimodal Knowledge Editing
- [分离对齐与反对齐的跨模态补偿](../conferences/icml-2026/cards/5201-5300.md#xu26bt-modules) · Neural-Inspired Modeling of Auditory Selection and Compensation for Audio-Visual Speech Separation
- [按反相关群对比定位并修正CLIP头](../conferences/icml-2026/cards/5501-5600.md#yeo26a-modules) · Locate then Correct: Debiasing Attention Heads in CLIP
- [双隐状态记忆与按需注入](../conferences/icml-2026/cards/5601-5700.md#yu26bf-modules) · Dual Latent Memory for Visual Multi-agent System

<a id="by-ml-foundations"></a>

### 机器学习基础与统计

- [注意力参数化](../conferences/icml-2026/cards/0101-0200.md#bae26d-modules) · Affine-Scaled Attention: Towards Flexible and Stable Transformer Attention
- [克罗内克适配器](../conferences/icml-2026/cards/0101-0200.md#bai26l-modules) · Diving into Kronecker Adapters: Component Design Matters
- [稠密模型转 MoE](../conferences/icml-2026/cards/0201-0300.md#bamba26a-modules) · DOT-MoE: Differentiable Optimal Transport for MoEfication
- [连续深度模型](../conferences/icml-2026/cards/0201-0300.md#banerjee26b-modules) · Efficient Continuous-Depth Modeling with GRU Equivalents
- [循环模型长程记忆](../conferences/icml-2026/cards/0201-0300.md#behrouz26a-modules) · Memory Caching: RNNs with Growing Memory
- [测试时记忆更新](../conferences/icml-2026/cards/0201-0300.md#behrouz26b-modules) · ATLAS: Learning to Optimally Memorize the Context at Test Time
- [时间序列预测](../conferences/icml-2026/cards/0301-0400.md#brachet26a-modules) · Time Series Forecasting Through the Lens of Dynamics
- [低功耗循环网络](../conferences/icml-2026/cards/0301-0400.md#brandoit26a-modules) · Improving the Performance and Learning Stability of Parallelizable RNNs Designed for Ultra-Low Power Applications
- [多实例部分标签](../conferences/icml-2026/cards/0401-0500.md#cao26af-modules) · Enhanced Multi-Instance Partial Label Learning via Average Gradient Outer Product
- [自监督投影头](../conferences/icml-2026/cards/0401-0500.md#chaudhry26a-modules) · The Geometry of Projection Heads: Conditioning, Invariance, and Collapse
- [相关矩阵流形全连接层](../conferences/icml-2026/cards/0601-0700.md#chen26fb-modules) · Riemannian Networks over Full-Rank Correlation Matrices
- [时间序列的后续轨迹检索](../conferences/icml-2026/cards/0701-0800.md#chong26c-modules) · Beyond Extrapolation: Knowledge Utilization Paradigm with Bidirectional Inspiration for Time Series Forecasting
- [无需旧样本的持续学习适配器](../conferences/icml-2026/cards/0701-0800.md#cosentino26a-modules) · PLATE: Plasticity-Tunable Efficient Adapters for Geometry-Aware Continual Learning
- [词元与专家的联合稀疏路由](../conferences/icml-2026/cards/0901-1000.md#do26b-modules) · Rethinking Sparse Mixture of Experts from a Unified Perspective
- [GPU 友好的块置换随机投影](../conferences/icml-2026/cards/1001-1100.md#dwaraknath26a-modules) · FlashSketch: Sketch-Kernel Co-Design for Fast Sparse Sketching on GPUs
- [可微的逐样本特征选择](../conferences/icml-2026/cards/1001-1100.md#ellinson26a-modules) · Hide&Seek: Learning to Explain in an End-to-End Differentiable Network
- [局部坐标对齐的向量丛注意力](../conferences/icml-2026/cards/1001-1100.md#fang26q-modules) · VBA: Vector Bundle Attention for Intrinsically Geometric Representation Learning
- [跨数据集时序谱结构对齐](../conferences/icml-2026/cards/1001-1100.md#fei26b-modules) · Olivia: Harmonizing Time Series Foundation Models with Power Spectral Density
- [时序分类的定长词元生成](../conferences/icml-2026/cards/1101-1200.md#feofanov26a-modules) · Mantis: Lightweight Foundation Model for Time Series Classification
- [显著性变速的多项式记忆](../conferences/icml-2026/cards/1201-1300.md#goffinet26a-modules) · HiPPO Zoo: Explicit Memory Mechanisms for Interpretable State Space Models
- [位置与内容分离的极坐标编码](../conferences/icml-2026/cards/1301-1400.md#gopalakrishnan26a-modules) · Decoupling The "What" and "Where" With Polar Coordinate Positional Embedding
- [时序预测的可变长模式词元](../conferences/icml-2026/cards/1301-1400.md#gotz26a-modules) · Byte Pair Encoding for Efficient Time Series Forecasting
- [ANN 到 SNN 的递推时序编码](../conferences/icml-2026/cards/1301-1400.md#gu26d-modules) · Temporal Weighted Encoding: Towards Maximal-Capacity Spike Coding for ANN–SNN Conversion
- [高维表格的相关特征分组压缩](../conferences/icml-2026/cards/1401-1500.md#habib26a-modules) · GOTabPFN: From Feature Ordering to Compact Tokenization for Tabular Foundation Models on High-Dimensional Data
- [用双曲几何实现层级记忆检索](../conferences/icml-2026/cards/1401-1500.md#hao26d-modules) · Hyperbolic Associative Memory Networks
- [用高阶随机草图补足线性原型注意力](../conferences/icml-2026/cards/1701-1800.md#huang26ao-modules) · PLASH: Provably Linear-Time Attention with Selective Higher-Order Feature Sketching
- [只在稀疏路由决策边界引入连续过渡](../conferences/icml-2026/cards/1701-1800.md#huu26a-modules) · Geometric and Stochastic Analysis of Discontinuities in Sparse Mixture-of-Experts
- [从输入块预估累加部分和的量化尺度](../conferences/icml-2026/cards/1701-1800.md#hwang26a-modules) · PsumQuant: In-line Post-training Partial Sum Quantizer for Energy Efficient NPU Inference
- [把目标偏好写进边注意力](../conferences/icml-2026/cards/1801-1900.md#jia26l-modules) · Preference-Modulated Structural Attention for Multi-Objective Combinatorial Optimization
- [在中间层用互斥正交子空间分离变因](../conferences/icml-2026/cards/2001-2100.md#jung26g-modules) · Layer-Centric Factors of Variation Disentanglement for Task- and Model-Agnostic Generalization
- [用输入驱动的辛变换伸缩注意力时间轴](../conferences/icml-2026/cards/2101-2200.md#kim26bk-modules) · StretchTime: Adaptive Time Series Forecasting via Symplectic Attention
- [用关系条件调制注意力投影](../conferences/icml-2026/cards/2301-2400.md#lee26h-modules) · Dynamic Relational Priming Improves Transformer in Multivariate Time Series
- [在冻结时序模型上学习域条件通道关系](../conferences/icml-2026/cards/2401-2500.md#li26bu-modules) · Channel Adapter for Time Series Foundation Models in Zero-Shot Multivariate Forecasting
- [用单纯形频率构造多维旋转位置编码](../conferences/icml-2026/cards/2601-2700.md#li26hn-modules) · nD-RoPE: A Generalized RoPE for n-Dimensional Position Embedding
- [先消除视图尺度再按不确定性融合证据](../conferences/icml-2026/cards/2701-2800.md#liu26r-modules) · Beyond Magnitude: Scale-Invariant Evidential Fusion for Multi-View Classification
- [用局部距离置信限制注意力全局同步](../conferences/icml-2026/cards/2901-3000.md#liu26fs-modules) · Krause Synchronization Transformers
- [脉冲神经元的超离散化](../conferences/icml-2026/cards/3301-3400.md#minoza26a-modules) · UltraLIF: Fully Differentiable Spiking Neural Networks via Ultradiscretization and Max-Plus Algebra
- [结构注意力高阶求导](../conferences/icml-2026/cards/3301-3400.md#mogilevsky26a-modules) · d$^2$p: Structured Soft Attention Is All You Need
- [在复域内部做几何批归一化](../conferences/icml-2026/cards/3401-3500.md#nguyen26e-modules) · Batch Normalization for Neural Networks on Complex Domains
- [在状态注入端做动量和谱调节](../conferences/icml-2026/cards/3401-3500.md#nguyen26t-modules) · MuonSSM: Orthogonalizing State Space Models for Sequence Modeling
- [以可微析取投影嵌入硬规则](../conferences/icml-2026/cards/3501-3600.md#pal26a-modules) · DisjunctiveNet: Neural Symbolic Learning via Differentiable Convexified Optimization Layers
- [按中间分布调节等变](../conferences/icml-2026/cards/3601-3700.md#pertigkiozoglou26a-modules) · Recurrent Equivariant Constraint Modulation: Learning Per-Layer Symmetry Relaxation from Data
- [用观察值调节显式状态时长](../conferences/icml-2026/cards/4101-4200.md#slupinski26a-modules) · RED-HDP-HMM: Observation-Dependent Durations for Bayesian Nonparametric Sequential Models
- [硬稀疏可微真值表](../conferences/icml-2026/cards/4101-4200.md#soegeng26a-modules) · TT-Sparse: Learning Sparse Rule Models with Differentiable Truth Tables
- [gaussian-associative-memory](../conferences/icml-2026/cards/4401-4500.md#tankala26a-modules) · Dense associative memory for Gaussian distributions
- [group-shared-sparse-output](../conferences/icml-2026/cards/4501-4600.md#ullah26b-modules) · HASTE: Hardware-Aware Dynamic Sparse Training for Large Output Spaces
- [先去趋势匹配再压缩变量协同](../conferences/icml-2026/cards/4601-4700.md#wang26cs-modules) · PESD-TSF: A Period-Aware and Explicit Structured Decomposition Framework for Long-Term Time Series Forecasting
- [频谱一致性稀疏交互](../conferences/icml-2026/cards/4701-4800.md#wang26ec-modules) · Crisp: A Spectral-Based Interaction Strategy for Multivariate Time Series Forecasting
- [规则候选格上的特定扩展确定度](../conferences/icml-2026/cards/4901-5000.md#weitekamp26a-modules) · STAND: Self-Aware Precondition Induction for Interactive Task Learning
- [双曲Karcher流关联记忆](../conferences/icml-2026/cards/5001-5100.md#wu26x-modules) · Hyperbolic neural population geometry benefits computation
- [依赖图引导的因果token排序](../conferences/icml-2026/cards/5001-5100.md#wu26ci-modules) · LagLLM: LLM-empowered lead–lag dependency learning for spatial-temporal time series forecasting
- [在适应基系数中求解attention](../conferences/icml-2026/cards/5101-5200.md#xiao26f-modules) · Functional Attention: From Pairwise Affinities to Functional Correspondences
- [用向量球谐补全快速张量积](../conferences/icml-2026/cards/5101-5200.md#xie26h-modules) · Asymptotically Fast Clebsch-Gordan Tensor Products with Vector Spherical Harmonics
- [四元数分量共享实值注意力](../conferences/icml-2026/cards/5301-5400.md#yamauchi26a-modules) · Quaternion Self-Attention with Shared Scores
- [两步膜电位捷径与周期遗忘](../conferences/icml-2026/cards/5501-5600.md#ye26k-modules) · Resolving the Timestep Scaling Paradox in Spiking Neural Networks with a Timestep-Scalable Neuron Model
- [用稳定模态参数生成不规则时间轨迹](../conferences/icml-2026/cards/5501-5600.md#you26f-modules) · Latent Laplace Diffusion for Irregular Multivariate Time Series
- [在局部SO2表示中融合高阶特征再映回](../conferences/icml-2026/cards/5501-5600.md#yu26y-modules) · Efficient Prediction of SO(3)-Equivariant Hamiltonian Matrices via SO(2) Local Frames
- [用脉冲算术原语替换Transformer非线性](../conferences/icml-2026/cards/5601-5700.md#yuan26e-modules) · Plug-and-Play Spiking Operators: Breaking the Nonlinearity Bottleneck in Spiking Transformers
- [对持久latent的预测固定点误差做Jacobian校正](../conferences/icml-2026/cards/5701-5800.md#zeng26r-modules) · CoEvol-NO: State and Coordinate Co-Evolution with an Error-Driven Predictor-Corrector Paradigm for Neural Operator Transformer
- [Laplace inducing GP的稀疏基索引](../conferences/icml-2026/cards/6001-6100.md#zhao26at-modules) · SIKA-GP: Accelerating Gaussian Process Inference with Sparse Inducing Kernel Approximations for Bayesian Deep Learning
- [隐式resolvent聚类的显式低秩因子](../conferences/icml-2026/cards/6001-6100.md#zhao26az-modules) · Contractive Anchor Resolvent Diffusion for Incomplete Multi-View Clustering

<a id="by-graph-and-recommendation"></a>

### 图学习与推荐

- [图卷积](../conferences/icml-2026/cards/0101-0200.md#bai26i-modules) · GI-GCN: Global Interacted Graph Convolutional Networks via Dominant Sets for Graph Classification
- [图神经网络表达力](../conferences/icml-2026/cards/0201-0300.md#barcelo26a-modules) · Message Passing on the Edge: Towards Scalable and Expressive GNNs
- [兼顾图拓扑与因果顺序的注意力](../conferences/icml-2026/cards/0601-0700.md#chen26gm-modules) · Weaving Graph over Tokens: Contextualizing Structured Sequences for LLMs
- [异配图消息的自成分消除](../conferences/icml-2026/cards/0701-0800.md#choi26d-modules) · Gauge-Equivariant Graph Networks via Self-Interference Cancellation
- [有向带属性图的酉卷积](../conferences/icml-2026/cards/1101-1200.md#fesser26b-modules) · Unitary Convolutions for Message-passing and Positional Encodings on Directed Graphs
- [用 Schur 补把高阶作用折回顶点](../conferences/icml-2026/cards/2201-2300.md#krahn26a-modules) · Collapsed Effective Operators for Higher-order Structures
- [双向建模图异常的局部谱能量偏移](../conferences/icml-2026/cards/2901-3000.md#liu26gb-modules) · Modeling Spectral Energy Shifts in Spatio-Temporal Graph Anomaly Detection
- [让图谱坐标旋转查询和键](../conferences/icml-2026/cards/3801-3900.md#reid26a-modules) · Rotary Position Encodings for Graphs
- [在可学习图谱尺度上生成软超边](../conferences/icml-2026/cards/4101-4200.md#sim26b-modules) · Learning Multi-Scale Hypergraph for High-Order Brain Connectivity Analysis
- [生成LoRA的范数参照](../conferences/icml-2026/cards/4201-4300.md#sun26f-modules) · Enhancing LLMs for Graph Tasks via Graph-aware LoRA Generation
- [跨层关系EMA与属性结构分支](../conferences/icml-2026/cards/5301-5400.md#yan26i-modules) · MV-FGAD: Towards Efficient and Effective Federated Graph Anomaly Detection via Multi-view Learning
- [极坐标分解的曲率注意力计算](../conferences/icml-2026/cards/5401-5500.md#yang26cg-modules) · Fast Mixture of Curvature-Aware Experts for Diverse and Dynamic Graph Topologies

<a id="by-scientific-ml"></a>

### 科学机器学习

- [网格动力学平滑](../conferences/icml-2026/cards/0201-0300.md#berman26d-modules) · Smoothness Errors in Dynamics Models and How to Avoid Them
- [医学视觉定位](../conferences/icml-2026/cards/0401-0500.md#chang26b-modules) · MedSIGHT: Towards Grounded Visual Comprehension in Medical Large Vision-Language Models
- [脑电信号的复数频谱细化](../conferences/icml-2026/cards/0601-0700.md#chen26fr-modules) · PCRNet: Phase-aware Complex Refinement Network for EEG-based Auditory Attention Decoding
- [原子间势的自适应贝叶斯失活](../conferences/icml-2026/cards/0701-0800.md#coscia26a-modules) · BLIPs: Bayesian Learned Interatomic Potentials
- [用虚拟三跳路径编码蛋白交互先验](../conferences/icml-2026/cards/1201-1300.md#gao26ap-modules) · Learning the Interaction Prior for Protein-Protein Interaction Prediction: A Model-Agnostic Approach
- [按当前流向为网格图加局部二跳边](../conferences/icml-2026/cards/2401-2500.md#li26cu-modules) · Graph Rewiring based on Flow Alignment for Improving Fluid Simulation
- [学习分数阶算子输入](../conferences/icml-2026/cards/3201-3300.md#mehouachi26a-modules) · Fractional is Better: Learnable Derivative Orders in Neural Operator Learning
- [把边界条件学成域内函数扩展](../conferences/icml-2026/cards/3301-3400.md#mousavi26a-modules) · Imposing Boundary Conditions on Neural Operators via Learned Function Extensions
- [用综合征预测匹配解码边权](../conferences/icml-2026/cards/3601-3700.md#peled26a-modules) · Neural Minimum Weight Perfect Matching for Quantum Error Codes
- [按小波能量给各频带加噪](../conferences/icml-2026/cards/3701-3800.md#qin26e-modules) · Not All Frequencies Are Equal: Energy-Adaptive Diffusion for Time Series Forecasting
- [在通量空间融合粗细尺度](../conferences/icml-2026/cards/4101-4200.md#shu26b-modules) · HybridOM: Hybrid Physics-Based and Data-Driven Global Ocean Modeling with Efficient Spatial Downscaling
- [conditional-clifford-kernels](../conferences/icml-2026/cards/4301-4400.md#szarvas26a-modules) · Conditional Clifford-Steerable CNNs for PDE Modeling
<!-- classification:end -->
