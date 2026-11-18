# 模型架构

[首页](../README.md) · [参与贡献](../CONTRIBUTING.md) · [English](../en/insights/architecture.md)

整体架构与信息流。

<!-- classification:start -->
## 按研究领域浏览

[大语言模型](#by-llm) · [计算机视觉](#by-computer-vision) · [自然语言处理](#by-nlp) · [强化学习](#by-reinforcement-learning) · [机器人学](#by-robotics) · [多模态学习](#by-multimodal) · [机器学习基础与统计](#by-ml-foundations) · [图学习与推荐](#by-graph-and-recommendation) · [科学机器学习](#by-scientific-ml)

<a id="by-llm"></a>

### 大语言模型

- [离散扩散解码](../conferences/icml-2026/cards/0101-0200.md#arriola26a-architecture) · Set Diffusion: Interpolating Token Orderings between Autoregression and Diffusion for Fast and Flexible Decoding
- [长任务 Agent 协作](../conferences/icml-2026/cards/0301-0400.md#bui26b-architecture) · HiMAP-Travel: Hierarchical Multi-Agent Planning for Long-Horizon Constrained Travel
- [预测分块上下文辅助逐词解码](../conferences/icml-2026/cards/0801-0900.md#dai26g-architecture) · Context-level Language Modeling by Learning Predictive Context Embeddings
- [长上下文的块级混合注意力](../conferences/icml-2026/cards/0801-0900.md#deng26v-architecture) · Neural Attention Search Linear: Towards Adaptive Token-Level Hybrid Attention Models
- [低维潜空间专家计算](../conferences/icml-2026/cards/1001-1100.md#elango26a-architecture) · Revisiting Efficiency–Accuracy Scaling in Mixture-of-Experts Architectures
- [可结构化高阶递推的词元混合](../conferences/icml-2026/cards/1001-1100.md#fagnou26a-architecture) · Trading Complexity for Expressivity Through Structured Generalized Linear Token Mixing
- [仅对困难词元启动隐空间迭代](../conferences/icml-2026/cards/1101-1200.md#fu26t-architecture) · Think-at-Hard: Dynamic Looped Transformers for Improved Reasoning
- [频域乘法实现因果序列混合](../conferences/icml-2026/cards/1101-1200.md#gan26c-architecture) · Caracal: Causal Architecture via Spectral Mixing
- [为 MoE 解耦共用主谱与专家剩余分量](../conferences/icml-2026/cards/1601-1700.md#huang26i-architecture) · SD-MoE: Spectral Decomposition for Effective Expert Specialization
- [通过带噪吸引子迭代扩展潜空间推理](../conferences/icml-2026/cards/1601-1700.md#huang26l-architecture) · Equilibrium Reasoners: Learning Attractors Enables Scalable Reasoning
- [按块重排带动量的线性注意力递推](../conferences/icml-2026/cards/1701-1800.md#huang26af-architecture) · MDN: Parallelizing Stepwise Momentum for Delta Linear Attention
- [把局部相似 token 压成概念后再做重计算](../conferences/icml-2026/cards/1701-1800.md#huang26cl-architecture) · ConceptMoE: Adaptive Token-to-Concept Compression for Implicit Compute Allocation
- [把无上下文前馈支路预计算为词表](../conferences/icml-2026/cards/1801-1900.md#jaiswal26a-architecture) · MemoryLLM: Plug-n-Play Interpretable Feed-Forward Memory for Transformers
- [让离散发词策略读取连续演化状态](../conferences/icml-2026/cards/1801-1900.md#jia26h-architecture) · Text Generation as Continuous Latent Dynamics via Reinforcement Learning
- [共享键和值以减少自回归缓存](../conferences/icml-2026/cards/2001-2100.md#kayyam26a-architecture) · Do Transformers Need Three Projections? Systematic Study of QKV Variants
- [让稀疏解码器显式建模特征交互](../conferences/icml-2026/cards/2201-2300.md#koromilas26a-architecture) · PolySAE: Modeling Feature Interactions in Sparse Autoencoders via Polynomial Decoding
- [共享残差块的双流归一化](../conferences/icml-2026/cards/2401-2500.md#li26ba-architecture) · SiameseNorm: Breaking the Barrier to Reconciling Pre/Post-Norm
- [用概率电路耦合同步解除掩码的词元](../conferences/icml-2026/cards/2501-2600.md#li26fd-architecture) · Breaking the Factorization Barrier in Diffusion Language Models
- [让位置编码随上下文依赖重新排布](../conferences/icml-2026/cards/2601-2700.md#li26jq-architecture) · RePo: Language Models with Context Re-Positioning
- [残差流分叉的并行潜空间计算](../conferences/icml-2026/cards/2801-2900.md#liu26cx-architecture) · Thoughtbubbles: an Unsupervised Method for Parallel Thinking in Latent Space
- [用超网络将上下文映射为 LoRA](../conferences/icml-2026/cards/2901-3000.md#liu26ek-architecture) · SHINE: A Scalable In-Context Hypernetwork for Mapping Context to LoRA in a Single Pass
- [把上下文键值视为逐步实例化的两层网络](../conferences/icml-2026/cards/3001-3100.md#lu26aq-architecture) · HyperMLP: An Integrated Perspective for Sequence Modeling
- [以自激活秩一键值原子积累持续学习记忆](../conferences/icml-2026/cards/3001-3100.md#lu26au-architecture) · Little By Little: Continual Learning via Incremental Mixture of Rank-1 Associative Memory Experts
- [线性注意头内记忆分组](../conferences/icml-2026/cards/3201-3300.md#mei26a-architecture) · Head-in-Head in Linear Attention
- [跨词元高层反馈](../conferences/icml-2026/cards/3301-3400.md#mohan26b-architecture) · Turbo Connection: Reasoning as Information Flow from Higher to Lower Layers
- [有限自动机状态注入](../conferences/icml-2026/cards/3301-3400.md#mohri26a-architecture) · Rational Transductors
- [把栈操作写成可并行的递归更新](../conferences/icml-2026/cards/3401-3500.md#nguyen26i-architecture) · Push, Pop, Parallelize: Stack-Augmented Linear Attention via the Delta Rule
- [给语言模型加可读写数值时序的 patch 接口](../conferences/icml-2026/cards/3601-3700.md#parker26a-architecture) · TsLLM: Augmenting LLMs for General Time Series Understanding and Prediction
- [用任意顺序因果注意力实现扩散文本的精确 KV 缓存](../conferences/icml-2026/cards/3901-4000.md#sahoo26b-architecture) · Esoteric Language Models: A Family of Any-Order Diffusion LLMs
- [用信息形式的并行卡尔曼滤波保存序列置信状态](../conferences/icml-2026/cards/4001-4100.md#shaj26a-architecture) · Kalman Linear Attention: Parallel Bayesian Filtering For Efficient Language Modeling and State Tracking
- [把知识缺口与报告提纲分图维护](../conferences/icml-2026/cards/4101-4200.md#shi26n-architecture) · A Tale of Two Graphs: Separating Knowledge Exploration from Outline Structure for Open-Ended Deep Research
- [把原子专家按专家重排执行](../conferences/icml-2026/cards/4101-4200.md#shi26q-architecture) · OmniMoE: An Efficient MoE by Orchestrating Atomic Experts at Scale
- [保持因果性的动态旧key](../conferences/icml-2026/cards/4201-4300.md#song26y-architecture) · Causal Attention with Lookahead Keys
- [外源注意力锚与归一化](../conferences/icml-2026/cards/4201-4300.md#su26a-architecture) · Attention Projection Mixing with Exogenous Anchors
- [static-contextual-lookup](../conferences/icml-2026/cards/4401-4500.md#tseng26a-architecture) · $L^3$: Large Lookup Layers
- [diagonal-preconditioned-delta](../conferences/icml-2026/cards/4501-4600.md#tumma26a-architecture) · Preconditioned DeltaNet: Curvature-aware Sequence Modeling for Linear Recurrences
- [信息漂移分段的有界多状态记忆](../conferences/icml-2026/cards/4701-4800.md#wang26gr-architecture) · Dynamic Linear Attention
- [密集稀疏联合循环注意力](../conferences/icml-2026/cards/4901-5000.md#wei26h-architecture) · RAT+: Train Dense, Infer Sparse - Recurrence Augmented Attention for Dilated Inference
- [同decoder骨干的任意顺序建模](../conferences/icml-2026/cards/5301-5400.md#xue26k-architecture) · Any-Order GPT as Masked Diffusion Model: Decoupling Formulation and Architecture
- [活跃上下文与递归栈的分离](../conferences/icml-2026/cards/5401-5500.md#yang26bp-architecture) · Recursive Models for Long-Horizon Reasoning
- [递归记忆生成FFN低秩调制](../conferences/icml-2026/cards/5401-5500.md#yao26g-architecture) · Integrated Episodic and Semantic Memory via Modulating Transformer FeedForward Layers
- [用随机mask latent提供并行解码共享随机性](../conferences/icml-2026/cards/5501-5600.md#yoo26b-architecture) · Infinite Mask Diffusion for Few-Step Distillation
- [同步点门控的有界路由记忆](../conferences/icml-2026/cards/5701-5800.md#zeng26h-architecture) · Attention with Routed-Memory for Learnable Sparse Control
- [GLU共激活分簇的免训练专家构造](../conferences/icml-2026/cards/6001-6100.md#zhao26ce-architecture) · ExpertWeaver: Unlocking the Inherent MoE in Dense LLMs with GLU Activation Patterns

<a id="by-computer-vision"></a>

### 计算机视觉

- [视频分词](../conferences/icml-2026/cards/0101-0200.md#atanov26a-architecture) · VideoFlexTok: Flexible-Length Coarse-to-Fine Video Tokenization
- [像素空间扩散](../conferences/icml-2026/cards/0101-0200.md#baade26a-architecture) · Latent Forcing: Reordering the Diffusion Trajectory for Pixel-Space Image Generation
- [按空间分组的同位词元预测](../conferences/icml-2026/cards/0501-0600.md#chen26du-architecture) · Autoregression with Self-Token Prediction
- [原生四维体素自编码](../conferences/icml-2026/cards/0901-1000.md#ding26u-architecture) · Native Spatio-Temporal 4D Variational Autoencoder
- [按类别难度隔离位姿学习梯度](../conferences/icml-2026/cards/1201-1300.md#gao26aq-architecture) · DecomPose: Disentangling Cross-Category Optimization Contention for Category-Level 6D Object Pose Estimation
- [持久三维状态的交互视频世界模型](../conferences/icml-2026/cards/1201-1300.md#garcin26a-architecture) · Beyond Pixel Histories: World Models with Persistent 3D State
- [按下游生成容量选择视觉潜通道](../conferences/icml-2026/cards/1401-1500.md#hansen-estruch26a-architecture) · ViTok-v2: Scaling Native Resolution Autoencoders to 5 Billion Parameters
- [把相机射线变成可共同去噪的像素](../conferences/icml-2026/cards/1801-1900.md#jang26f-architecture) · Rays as Pixels: Learning A Joint Distribution of Videos and Camera Trajectories
- [给轻量扩散编解码器预训练重建任务](../conferences/icml-2026/cards/1801-1900.md#jia26i-architecture) · CoD-Lite: Real-Time Diffusion-Based Generative Image Compression
- [用平衡层给不同生成尺度分配步数](../conferences/icml-2026/cards/1901-2000.md#jiang26ah-architecture) · Visual Implicit Autoregressive Modeling
- [预训练注意力的线性化迁移](../conferences/icml-2026/cards/2401-2500.md#li26bc-architecture) · Linearizing Vision Transformer with Test-Time Training
- [以分层射线交点同时预测可见与遮挡表面](../conferences/icml-2026/cards/2601-2700.md#li26jg-architecture) · LaRI: Layered Ray Intersections for Single-view 3D Geometric Reasoning
- [共享波段前缀并连续查询空间分辨率](../conferences/icml-2026/cards/2601-2700.md#liang26c-architecture) · Hyperspectral Image Fusion with Spectral-Band and Fusion-Scale Agnosticism
- [把静态墨迹转成少步脉冲并压缩空白](../conferences/icml-2026/cards/2601-2700.md#liang26j-architecture) · Spike-HTR: Spiking Neural Transformer for Handwritten Text Recognition
- [任意几何先验的前馈三维重建](../conferences/icml-2026/cards/2801-2900.md#liu26cw-architecture) · WorldMirror: Universal 3D World Reconstruction with Any-Prior Prompting
- [将二维旋转位置编码扩展到均匀斜向投影](../conferences/icml-2026/cards/2801-2900.md#liu26dj-architecture) · Spiral RoPE: Rotate Your Rotary Positional Embeddings in the 2D Plane
- [把单调性硬编码到盲逆问题的前向算子](../conferences/icml-2026/cards/2901-3000.md#liu26eb-architecture) · Resolving Blind Inverse Problems under Dynamic Range Compression via Structured Forward Operator Modeling
- [用边分解三角候选和固定步偏移替代测试时优化](../conferences/icml-2026/cards/2901-3000.md#liu26gs-architecture) · FastSESR: Fast Scene-level Explicit Surface Reconstruction
- [从原视频到去物视频直接学习随机桥](../conferences/icml-2026/cards/2901-3000.md#lou26b-architecture) · Learning Stochastic Bridges for Video Object Removal via Video-to-Video Translation
- [用两级路由将长序列任务接入不同专家](../conferences/icml-2026/cards/2901-3000.md#lou26c-architecture) · Scaling Continual Learning to 300+ Tasks with Bi-Level Routing Mixture-of-Experts
- [稀疏动作的逐尺度自回归](../conferences/icml-2026/cards/3001-3100.md#luo26af-architecture) · MotionMAR: Multi-scale Auto-Regressive Human Motion Reconstruction from Sparse Observations
- [单目四维几何运动查询](../conferences/icml-2026/cards/3001-3100.md#luo26al-architecture) · 4RC: 4D Reconstruction via Conditional Querying Anytime and Anywhere
- [让二维 RoPE 在大图分辨率均匀分配方向](../conferences/icml-2026/cards/3301-3400.md#min26f-architecture) · Compass-RoPE: Isotropic Rotary Position Embeddings for Vision Transformers
- [局部支撑与功能关系合成室内场景](../conferences/icml-2026/cards/3801-3900.md#ran26d-architecture) · Pair2Scene: Learning Local Object Relations for Procedural Scene Generation
- [冻结参考与对称非扩张去噪](../conferences/icml-2026/cards/4101-4200.md#sinha26a-architecture) · Trainable Nonexpansive Denoisers for Contractive Image Reconstruction
- [条件路由化解多教师冲突](../conferences/icml-2026/cards/4301-4400.md#tang26j-architecture) · PRISM: Synergizing Vision Foundation Models via Self-organized Expert Specialization
- [局部方向几何与全局顺序的拆分](../conferences/icml-2026/cards/5301-5400.md#yan26v-architecture) · Rethinking Serialization in Linear 3D Vision: Decoupling Anisotropic Geometry from Isotropic Semantics
- [用条件掩码bit头建模大码本内依赖](../conferences/icml-2026/cards/5501-5600.md#yu26z-architecture) · Autoregressive Image Generation with Masked Bit Modeling
- [共享投影的多尺度窗口改造](../conferences/icml-2026/cards/6001-6100.md#zhang26jj-architecture) · Transform Trained Transformer for Accelerating Native 4K Video Generation
- [视频VAE按分辨率与时间上采样位置替换算子](../conferences/icml-2026/cards/6201-6300.md#zhu26v-architecture) · Flash-VAED: Plug-and-Play VAE Decoders for Efficient Video Generation
- [已解码祖先backbone与轻量因果head分离](../conferences/icml-2026/cards/6201-6300.md#zhu26az-architecture) · PACE: Post-Causal Entropy Modeling for Learned LiDAR Point Cloud Compression

<a id="by-nlp"></a>

### 自然语言处理

- [文本编码与掩码重建解耦](../conferences/icml-2026/cards/0801-0900.md#dervishi26a-architecture) · Separating Representation from Reconstruction Enables Scalable Text Encoders
- [纯因果 Transformer 的音频分词](../conferences/icml-2026/cards/1301-1400.md#gong26c-architecture) · Scaling Transformers for End-to-End Discrete Audio Tokenization
- [去噪网络与解掩顺序共同训练](../conferences/icml-2026/cards/1501-1600.md#hong26f-architecture) · Unifying Masked Diffusion Models with Various Generation Orders and Beyond
- [按符号建共享流使改名可交换](../conferences/icml-2026/cards/1801-1900.md#isik26a-architecture) · Names Don’t Matter: Symbol-Invariant Transformer for Open-Vocabulary Learning
- [复数频谱分支的相位消融](../conferences/icml-2026/cards/5501-5600.md#yildirim26a-architecture) · Language as a Wave Phenomenon: Semantic Phase Locking and Interference in Neural Networks

<a id="by-reinforcement-learning"></a>

### 强化学习

- [以潜状态分布替代像素重构并允许替换约束先验](../conferences/icml-2026/cards/1701-1800.md#huang26ba-architecture) · VJEPA: Variational Joint Embedding Predictive Architectures as Probabilistic World Models
- [用输入门在固定参考路径和可学投影间插值](../conferences/icml-2026/cards/2101-2200.md#koeppe26a-architecture) · Mitigating Plasticity Loss through Architectural Design in Continual Learning
- [把可梯度训练的连续策略编译成查表电路](../conferences/icml-2026/cards/2201-2300.md#kresse26a-architecture) · Differentiable Weightless Controllers: Learning Logic Circuits for Continuous Control
- [用路径状态缓解离散采样策略的表征混叠](../conferences/icml-2026/cards/4101-4200.md#silva26a-architecture) · Path-dependent Discrete Amortized Inference
- [公共历史共享的结构策略梯度](../conferences/icml-2026/cards/4901-5000.md#wibault26a-architecture) · Recurrent Structural Policy Gradient for Partially Observable Mean Field Games

<a id="by-robotics"></a>

### 机器人学

- [频域分层动作策略](../conferences/icml-2026/cards/0401-0500.md#cao26u-architecture) · Hierarchical Policy Learning via Spectral Decomposition
- [第一视角三维检测的时序记忆](../conferences/icml-2026/cards/0901-1000.md#ding26x-architecture) · Embodied-DETR: End-to-End Temporal 3D Object Detection in Egocentric Views
- [在驾驶仿真中按需补绘车道与交通参与者](../conferences/icml-2026/cards/1901-2000.md#jiang26bf-architecture) · VectorWorld: Efficient Streaming World Model via Diffusion Flow on Vector Graphs
- [长时机器人动作的连续粗到细生成](../conferences/icml-2026/cards/2701-2800.md#lin26ab-architecture) · MSP: Probabilistically Consistent Multi-Scale Action Generation
- [稀疏三维路点与可复用动作专家](../conferences/icml-2026/cards/2801-2900.md#liu26bf-architecture) · GAE: Unleashing Physical Potential of VLM with Generalizable Action Expert
- [用低频潜在时空推理支持高频机器人控制](../conferences/icml-2026/cards/2801-2900.md#liu26ch-architecture) · LaST$_0$: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model
- [观察条件作为动作扩散桥端点](../conferences/icml-2026/cards/2801-2900.md#liu26db-architecture) · Sample from What You See: Visuomotor Policy Learning via Diffusion Bridge with Observation-Embedded Stochastic Differential Equation
- [用可微连续时间函数表示机器人动作块](../conferences/icml-2026/cards/2901-3000.md#liu26gf-architecture) · Neural Implicit Action Fields: From Discrete Waypoints to Continuous Functions for Vision-Language-Action Models
- [无投影多面体流匹配](../conferences/icml-2026/cards/3101-3200.md#ma26ar-architecture) · PolyFlow: Safe and Efficient Polytope-Constrained Flow Matching with Constraint Embedding and Projection-free Update
- [文本推理视觉子目标分专家](../conferences/icml-2026/cards/4101-4200.md#shou26a-architecture) · HALO: A Unified Vision-Language-Action Model for Embodied Multimodal Chain-of-Thought Reasoning
- [预测趋势与历史细节分源](../conferences/icml-2026/cards/4201-4300.md#song26q-architecture) · TF-FACE: Time-Frequency Fusion Learning via Frequency-Domain Adaptive and Controllable Enhancement for Trajectory Prediction
- [calculus-matched-rough-dynamics](../conferences/icml-2026/cards/4401-4500.md#thompson26a-architecture) · Learning Manifold and Itô Dynamics with Branched Neural Rough Differential Equations
- [形态编码与系统条件动力专家](../conferences/icml-2026/cards/4601-4700.md#wang26dc-architecture) · WestWorld: A Knowledge-Encoded Scalable Trajectory World Model for Diverse Robotic Systems
- [按独立变化学习分解潜动作](../conferences/icml-2026/cards/4701-4800.md#wang26gs-architecture) · Factored Latent Action World Models
- [按到达延迟分支的动作包](../conferences/icml-2026/cards/4901-5000.md#wikman26a-architecture) · Adaptive Reinforcement Learning for Unobservable Random Delays
- [稀疏主动力学与背景上下文修正](../conferences/icml-2026/cards/5501-5600.md#yin26l-architecture) · DDP-WM: Disentangled Dynamics Prediction for Efficient World Models

<a id="by-multimodal"></a>

### 多模态学习

- [阵列几何条件化的空间音频词元](../conferences/icml-2026/cards/0801-0900.md#dementyev26a-architecture) · PhaseCoder: Microphone Geometry-Agnostic Spatial Audio Understanding for Multimodal LLMs
- [从高层注入绕过语义压缩的取证特征](../conferences/icml-2026/cards/2701-2800.md#lin26an-architecture) · Deep Residual Injection for Full-Spectrum Forensic Signal Perception in Multimodal Large Language Models
- [让模型在二维线索不足时主动调用几何通道](../conferences/icml-2026/cards/2801-2900.md#liu26as-architecture) · GeoSense: Internalizing Geometric Necessity Perception for Multimodal Reasoning
- [生成码原位参与后续推理](../conferences/icml-2026/cards/3601-3700.md#peng26k-architecture) · Unified Multimodal Autoregressive Modeling with Shared Context—Visual Tokenizer is Key to Unification
- [按流匹配时间分配 Transformer 层组](../conferences/icml-2026/cards/4001-4100.md#shen26w-architecture) · LaTtE-Flow: Layerwise Timestep-Expert Flow-based Transformer
- [路径隔离与视觉分区的并行推理](../conferences/icml-2026/cards/5201-5300.md#xu26bh-architecture) · Visual Para-Thinker: Divide-and-Conquer Reasoning for Visual Comprehension
- [只让文本query访问分层对齐的视觉输入](../conferences/icml-2026/cards/5601-5700.md#yuan26c-architecture) · Towards Multimodal Large Language Models with Both Training and Inference Efficiency

<a id="by-ml-foundations"></a>

### 机器学习基础与统计

- [世界模型](../conferences/icml-2026/cards/0101-0200.md#baek26b-architecture) · Learning to Theorize the World from Observation
- [非高斯扩散](../conferences/icml-2026/cards/0201-0300.md#bertholom26a-architecture) · M-Star: Markovian Projection of Star-Shaped Diffusion for Exponential Family Distributions
- [离散函数近似](../conferences/icml-2026/cards/0301-0400.md#candogan26b-architecture) · Deep Flow Networks
- [受约束域回归](../conferences/icml-2026/cards/0401-0500.md#chakraborty26a-architecture) · Probabilistically-routed Bayesian Additive Spanning Trees for Learning on Constrained Domains
- [用 Transformer 电路实现 Lloyd 迭代](../conferences/icml-2026/cards/0701-0800.md#clarkson26a-architecture) · Transformer Circuits Can Realize Clustering Algorithms
- [跨尺度共享的递归状态空间模型](../conferences/icml-2026/cards/1001-1100.md#fang26p-architecture) · Dynamic Fractal Mamba: A Neural Renormalization Group Flow for Scale-Invariant Sequence Modeling
- [符号置换等变的循环推理](../conferences/icml-2026/cards/1101-1200.md#freinschlag26a-architecture) · Symbol-Equivariant Recurrent Reasoning Models
- [可解析径向归一化流](../conferences/icml-2026/cards/1201-1300.md#gerdes26a-architecture) · Analytic Bijections for Smooth and Interpretable Normalizing Flows
- [时序预测的可调连续时间基](../conferences/icml-2026/cards/1301-1400.md#graf26a-architecture) · FlowState: Sampling-Rate-Equivariant Time-Series Forecasting
- [连续秩噪声配合前缀条件的排列采样](../conferences/icml-2026/cards/1501-1600.md#he26ax-architecture) · Learning Permutation Distributions via Reflected Diffusion on Ranks
- [训练注意力密度估计器来复用跨分布核行为](../conferences/icml-2026/cards/1801-1900.md#ilin26a-architecture) · DiScoFormer: Plug-In Density and Score Estimation with Transformers
- [把几何对称落实为注意力参考系共享](../conferences/icml-2026/cards/1801-1900.md#islam26a-architecture) · Platonic Transformers: A Solid Choice For Equivariance
- [用并行代理写入近似迭代状态更新](../conferences/icml-2026/cards/1901-2000.md#jiang26e-architecture) · PRISM: Parallel Residual Iterative Sequence Model
- [先限定对称族再学习可解释生成元](../conferences/icml-2026/cards/2001-2100.md#karjol26a-architecture) · Interpretable Discovery of One-parameter Subgroups: A Modular Framework for Elliptical, Hyperbolic, and Parabolic Symmetries
- [对一般线性共轭保留矩阵中心特征](../conferences/icml-2026/cards/2101-2200.md#kim26ca-architecture) · Equivariant Neural Networks for General Linear Symmetries on Lie Algebras
- [固定非零权重预算下扩宽网络](../conferences/icml-2026/cards/2101-2200.md#kong26f-architecture) · Expand Neurons, Not Parameters
- [用乘积节点和稀疏样本辨别奇偶支持](../conferences/icml-2026/cards/2201-2300.md#larue26a-architecture) · Learning High-Dimensional Parity Functions with Product Networks using Gradient Descent
- [用单个可学离散 Gaussian 核替换固定多尺度分支](../conferences/icml-2026/cards/2301-2400.md#lee26al-architecture) · Generalizing Multi-Scale Time-Series Modeling with a Single Operator
- [用不同分数奇异度的输入投影分工记忆远近信息](../conferences/icml-2026/cards/2401-2500.md#li26cx-architecture) · FRACTAL: State Space Model with Fractional Recurrent Architecture for Computational Temporal Analysis of Long Sequences
- [用共享矩阵多项式推广状态空间对偶](../conferences/icml-2026/cards/2501-2600.md#li26ft-architecture) · MIMOMamba: From Scalar Duality to Matrix-Valued Attention
- [将 KV 绑定测试时训练改写成线性注意力扫描](../conferences/icml-2026/cards/2801-2900.md#liu26ae-architecture) · Test-Time Training with KV Binding Is Secretly Linear Attention
- [用少量普通 LIF 反馈回路提供长期记忆](../conferences/icml-2026/cards/2801-2900.md#liu26do-architecture) · LIF Recurrent Memory Enables Long-Horizon Spiking Computation
- [用行注意力与全局寄存器支持表格逐样本退出](../conferences/icml-2026/cards/2901-3000.md#liu26fm-architecture) · TabSwift: An Efficient Tabular Foundation Model with Row-Wise Attention
- [用可调平稳噪声核统一掩码与均匀扩散](../conferences/icml-2026/cards/2901-3000.md#liu26gi-architecture) · Balancing Understanding and Generation in Discrete Diffusion Models
- [逐段扩展直接时序预测](../conferences/icml-2026/cards/3001-3100.md#lu26w-architecture) · ReNF: Rethinking the Design of Neural Long-Term Time Series Forecasters
- [用独立特征嵌入与组 Lasso 强化表格轴归纳](../conferences/icml-2026/cards/3001-3100.md#lui26a-architecture) · LassoFlexNet: a Flexible Neural Architecture for Tabular Data
- [不规则点集傅里叶卷积](../conferences/icml-2026/cards/3301-3400.md#mohseni26a-architecture) · Revisiting Neural Processes via Fourier Transform and Volterra Series
- [可稀疏化的非平稳高斯过程核](../conferences/icml-2026/cards/3401-3500.md#noack26a-architecture) · gp2Scale: A Class of Compactly Supported Non-Stationary Kernels and Distributed Computing for Exact Gaussian Processes on 10 Million Data Points
- [把精确零值移出扩散状态](../conferences/icml-2026/cards/3501-3600.md#ostheimer26a-architecture) · Skipping the Zeros in Diffusion Models for Sparse Data Generation
- [用随机二元潜变量和极化信道编码](../conferences/icml-2026/cards/3501-3600.md#ozyilkan26a-architecture) · SoftBinary Coding: A New Information-Theoretic Paradigm for Neural Compression via Fast Channel Simulation
- [对角复递推的并行储备池](../conferences/icml-2026/cards/3601-3700.md#pinna26a-architecture) · ParalESN: Enabling parallel information processing in Reservoir Computing
- [分开调度离散身份和连续几何噪声](../conferences/icml-2026/cards/3601-3700.md#pynadath26a-architecture) · CANDI: Hybrid Discrete-Continuous Diffusion Models
- [用证据边际和 Copula 建模成组概念](../conferences/icml-2026/cards/3701-3800.md#qiu26u-architecture) · Evidential Copula Concept Embedding Models
- [把历史外生变量关联注入未来预测](../conferences/icml-2026/cards/3701-3800.md#qiu26x-architecture) · DAG: A Dual Correlation Network for Time Series Forecasting with Exogenous Variables
- [注意力多视图平滑的 Neural CDE](../conferences/icml-2026/cards/4001-4100.md#serov26a-architecture) · Efficient Neural Controlled Differential Equations via Attentive Kernel Smoothing
- [混合连续序列的终止校准](../conferences/icml-2026/cards/4101-4200.md#shin26a-architecture) · Infinite-Precision Autoregressive Modeling for Vector Graphics and Layouts
- [观测频带编码与扩展查询](../conferences/icml-2026/cards/4101-4200.md#shin26c-architecture) · Query-Based Asymmetric Modeling with Decoupled Input–Output Rates for Speech Restoration
- [小波局部记忆SSM](../conferences/icml-2026/cards/4101-4200.md#solozabal26a-architecture) · WaveSSM: Multiscale State-Space Models for Non-stationary Signal Attention
- [differentiable-parity-projection](../conferences/icml-2026/cards/4401-4500.md#troxell26a-architecture) · Differentiable Optimization Layers for Guaranteed Fairness in Deep Learning
- [显式谱因子的预测头](../conferences/icml-2026/cards/4601-4700.md#wang26ax-architecture) · Ellipsoidal Time Series Forecasting
- [变量排序后再池化压缩](../conferences/icml-2026/cards/4701-4800.md#wang26fy-architecture) · ConFlux: Multivariate Time Series in Flux, One Unified Forecast in Confluence
- [混合分布token的后验变换](../conferences/icml-2026/cards/4901-5000.md#whittle26a-architecture) · Distribution Transformers: Fast Approximate Bayesian Inference With On-The-Fly Prior Adaptation
- [双随机残差流混合](../conferences/icml-2026/cards/5101-5200.md#xie26aa-architecture) · mHC: Manifold-Constrained Hyper-Connections
- [树路径拓扑的全叶softmax路由](../conferences/icml-2026/cards/5301-5400.md#yan26o-architecture) · Arboreal Neural Network
- [可变事件数的集合扩散](../conferences/icml-2026/cards/5401-5500.md#yang26bl-architecture) · Branching Diffusion for Point Processes in Time and Space
- [联合生成样本与NCDE混合动力学参数](../conferences/icml-2026/cards/5701-5800.md#zhang26ab-architecture) · Diff-MN: Diffusion Parameterized MoE-NCDE for Continuous Time Series Generation with Irregular Observations
- [可训练零空间的约束候选选择](../conferences/icml-2026/cards/6001-6100.md#zhao26v-architecture) · CAffNet: Hard Constraint-Affine Neural Networks
- [latent条件Phase-Type decoder的有限尾部拟合](../conferences/icml-2026/cards/6301-6400.md#ziani26a-architecture) · Phase-Type Variational Autoencoders for Heavy-Tailed Data

<a id="by-graph-and-recommendation"></a>

### 图学习与推荐

- [动态图的可学习信息耗散](../conferences/icml-2026/cards/0801-0900.md#de-castelli26a-architecture) · Adaptive Memory Retention in Dynamic Graphs
- [图动力学的能量与切向流](../conferences/icml-2026/cards/1001-1100.md#eliasof26a-architecture) · Graph Neural Dynamics via Learned Energy and Tangential Flows
- [图傅里叶变换的柯西分解](../conferences/icml-2026/cards/1101-1200.md#fernandez26a-architecture) · L2G-NET: Local to Global Spectral Graph Neural Networks via Cauchy Factorizations
- [超图生成的多尺度展开](../conferences/icml-2026/cards/1101-1200.md#gailhard26a-architecture) · Feature-Aware (Hyper)graph Generation via Next-Scale Prediction
- [以分层极大团表示超边](../conferences/icml-2026/cards/1201-1300.md#gantes26a-architecture) · SuperHype: Hypergraph Generation via Graph-Superposition Decomposition
- [在保全关系语义的前提下学习表的节点和边角色](../conferences/icml-2026/cards/1701-1800.md#huang26ax-architecture) · Is Fixing Schema Graphs Necessary? Full-Resolution Graph Structure Learning for Relational Deep Learning
- [先对齐局部坐标再扩散向量信号](../conferences/icml-2026/cards/1901-2000.md#johnson26a-architecture) · VDW-GNNs: Vector diffusion wavelets for geometric graph neural networks
- [关系数据库状态空间模型](../conferences/icml-2026/cards/2901-3000.md#liu26ep-architecture) · Ramba: Selective State-Space Models for Relational Deep Learning
- [用可逆图层同时支持 1-WL 表达和节点生成](../conferences/icml-2026/cards/3401-3500.md#nikolentzos26a-architecture) · InvGNN: Learning Invertible Node Representations on Graphs
- [正定矩阵层扩散](../conferences/icml-2026/cards/3601-3700.md#peng26e-architecture) · Sheaf Neural Networks on SPD Manifolds: Second-Order Geometric Representation Learning
- [将交通的空间互联与时间方向分开](../conferences/icml-2026/cards/3701-3800.md#qi26j-architecture) · Lightweight and Interpretable Transformer via Mixed Graph Algorithm Unrolling for Traffic Forecast
- [半定规划索引对消息传递](../conferences/icml-2026/cards/3701-3800.md#qian26e-architecture) · On the Expressive Power of GNNs to Solve Linear SDPs
- [动态图状态并行更新时距与拓扑](../conferences/icml-2026/cards/3701-3800.md#raghuvanshi26a-architecture) · Learning Long Range Spatio-Temporal Representations over Continuous Time Dynamic Graphs with State Space Models
- [让邻居只对兼容的潜变量达成共识](../conferences/icml-2026/cards/3901-4000.md#seely26a-architecture) · Learning Multi-Agent Coordination via Sheaf-ADMM
- [用低秩全局混合替代昂贵谱传播](../conferences/icml-2026/cards/4101-4200.md#shi26t-architecture) · S$^3$GNN: Efficient Global Mixing and Local Message Passing for Long-Range Graph Learning
- [归一化步信息的递归图更新](../conferences/icml-2026/cards/4201-4300.md#sun26e-architecture) · Adaptive Recurrent Message Passing for Test Time Computing on Graphs
- [Full-Spectrum Graph Neural Networks: Expressive and Scalable](../conferences/icml-2026/cards/4501-4600.md#wang26m-architecture) · Full-Spectrum Graph Neural Networks: Expressive and Scalable
- [随机节点标识的噪声等变约束](../conferences/icml-2026/cards/4801-4900.md#wang26kj-architecture) · Expressive Graph Neural Networks via Equivariant Use of Noise

<a id="by-scientific-ml"></a>

### 科学机器学习

- [连续时间动力学](../conferences/icml-2026/cards/0301-0400.md#brandle26a-architecture) · Continuous-Time Piecewise-Linear Recurrent Neural Networks
- [机械属性场的自适应稀疏体素](../conferences/icml-2026/cards/0801-0900.md#dagli26a-architecture) · Adaptive Volumetric Mechanical Property Fields Invariant to Resolution
- [周期晶体电荷密度的傅里叶重建](../conferences/icml-2026/cards/1001-1100.md#elsborg26a-architecture) · Global Plane Waves from Local Gaussians: Periodic Charge Densities in a Blink
- [点云到气动场的跨层解码](../conferences/icml-2026/cards/1401-1500.md#hagnberger26a-architecture) · SMART: Scalable Mesh-free Aerodynamic Simulations from Raw Geometries using a Transformer-based Surrogate Model
- [基于局部轴对齐流式计算等变注意力](../conferences/icml-2026/cards/1701-1800.md#huang26p-architecture) · E2Former-V2: On-the-Fly Equivariant Attention with Linear Activation Memory
- [让分子流的目标分布逐步集中](../conferences/icml-2026/cards/1901-2000.md#jin26i-architecture) · EvoEGF-Mol: Evolving Exponential Geodesic Flow for Structure-based Drug Design
- [把晶体张量等变性放到笛卡尔基组装](../conferences/icml-2026/cards/1901-2000.md#jin26p-architecture) · Efficient Equivariant High-Order Crystal Tensor Prediction via Cartesian Local-Environment Many-Body Coupling
- [用可分离谱因子解析计算高维物理残差](../conferences/icml-2026/cards/2001-2100.md#kaminsky26a-architecture) · Overcoming PINNs Failure Modes In High Dimension With Low-Rank Fourier Sum
- [吸附体与催化表面联合生成](../conferences/icml-2026/cards/2101-2200.md#kim26z-architecture) · CatFlow: Co-generation of Slab-Adsorbate Systems via Flow Matching
- [让傅里叶核在等半径频率上共享权重](../conferences/icml-2026/cards/2101-2200.md#kim26bp-architecture) · EqGINO: Equivariant Geometry-Informed Fourier Neural Operators for 3D PDEs
- [守恒 PDE 的容量约束累积输运](../conferences/icml-2026/cards/2201-2300.md#lan26c-architecture) · FluxNet: Learning Capacity-Constrained Local Transport Operators for Conservative and Bounded PDE Surrogates
- [用李群前缀扫描并行合成长时演化](../conferences/icml-2026/cards/2301-2400.md#lee26aa-architecture) · Lie-Algebraic Acceleration of Neural Koopman Dynamics
- [PDE 算子的高斯模态投影](../conferences/icml-2026/cards/2401-2500.md#li26aq-architecture) · From Basis to Basis: Gaussian Particle Representation for Interpretable PDE Operators
- [以应力和内力为接口训练神经模拟器](../conferences/icml-2026/cards/2601-2700.md#li26ho-architecture) · Neural Modular Physics for Elastic Simulation
- [按判别频谱设定脉冲膜衰减](../conferences/icml-2026/cards/2701-2800.md#liao26e-architecture) · Frequency Matching in Spiking Neural Networks for mmWave Sensing
- [部分可观测世界模型的流等变记忆](../conferences/icml-2026/cards/2701-2800.md#lillemark26a-architecture) · Flow Equivariant World Models: Structured Memory for Dynamic Environments
- [把周期变量嵌入单位圆后累积精度](../conferences/icml-2026/cards/2701-2800.md#lin26ar-architecture) · Periodic Bayesian Flow Networks with Additive Accuracy
- [几何张量的等变正定协方差](../conferences/icml-2026/cards/2801-2900.md#liu26bk-architecture) · Equivariant Covariance Tensors: Guaranteed SPD Uncertainty for Tensor-Valued Geometric Learning
- [函数 Koopman 记忆闭合](../conferences/icml-2026/cards/3001-3100.md#lu26u-architecture) · Interpretable Functional Koopman Learning with Non-Markovian Closure for Spatiotemporal Systems
- [显式控制深层 PINN 的输入雅可比](../conferences/icml-2026/cards/3201-3300.md#meng26i-architecture) · Deep Coupling Learning for Solving PDEs
- [按近端分裂连接物理与神经求解块](../conferences/icml-2026/cards/3201-3300.md#mezidi26a-architecture) · Proximal Splitting Methods for Hybrid Differentiable Models
- [用多头稀疏位移近似 PDE 中的输运](../conferences/icml-2026/cards/3301-3400.md#muser26a-architecture) · Flowers: A Warp Drive for Neural PDE Solvers
- [以可训练幂指数从物理约束恢复奇异性](../conferences/icml-2026/cards/3301-3400.md#n-guessan26a-architecture) · Discovering Scaling Exponents with Physics-Informed Müntz-Szász Networks
- [WiFi 振幅和相位的双流状态空间建模](../conferences/icml-2026/cards/3301-3400.md#n-d-26a-architecture) · Interleaved Selective State Space Models for Efficient WiFi-Based 3D Multi-Person Pose Estimation
- [误差驱动网格增边](../conferences/icml-2026/cards/3401-3500.md#nguyen26a-architecture) · Error-Driven Graph Augmentation for Mesh-Based PDE Surrogates
- [物理网格的拓扑接线与本构度量](../conferences/icml-2026/cards/3401-3500.md#noguchi26a-architecture) · Mesh Field Theory: Port–Hamiltonian Formulation of Mesh-Based Physics
- [用李群前缀扫描加速可逆动力学演化](../conferences/icml-2026/cards/3501-3600.md#park26j-architecture) · Euler–Poincaré Neural Dynamics: A Geometric-Mechanics Framework for Scientific Simulation
- [分别编码全夜睡眠轨迹与短时波形](../conferences/icml-2026/cards/3501-3600.md#park26n-architecture) · SleepMaMi: A Universal Sleep Foundation Model for Integrating Macro- and Micro-structures
- [在神经算子末层的随机系数上做扩散](../conferences/icml-2026/cards/3601-3700.md#park26aa-architecture) · Generative Neural Operators through Diffusion Last Layer
- [联合学习可变长序列的插入与揭示顺序](../conferences/icml-2026/cards/3601-3700.md#patel26a-architecture) · Insertion Based Sequence Generation with Learnable Order Dynamics
- [用双曲半径组织算子近远场注意力](../conferences/icml-2026/cards/3601-3700.md#pei26b-architecture) · Hyperbolic Neural Operator
- [用几何网格兼容的有限元空间保住神经 PDE 守恒](../conferences/icml-2026/cards/4001-4100.md#shaffer26a-architecture) · Structure-Preserving Learning Improves Geometry Generalization in Neural PDEs
- [把驱动噪声编码为Wick特征再学随机解算子](../conferences/icml-2026/cards/4101-4200.md#shi26i-architecture) · Expanding the Chaos: Neural Operator for Stochastic (Partial) Differential Equations
- [分层半可分神经算子](../conferences/icml-2026/cards/4101-4200.md#sittoni26a-architecture) · Neural-HSS: Hierarchical Semi-Separable Neural PDE Solver
- [latent-conditioned-operator-splitting](../conferences/icml-2026/cards/4301-4400.md#sun26aa-architecture) · Origo: Interpretable Multi-physics PDE Foundation Model through Neural Operator Splitting
- [sign-equivariant-orbital-attention](../conferences/icml-2026/cards/4401-4500.md#thiede26a-architecture) · Coupled Cluster con MoLe: Molecular Orbital Learning for Neural Wavefunctions
- [共享算子策略的跨数量PDE控制](../conferences/icml-2026/cards/5601-5700.md#zanotta26a-architecture) · CINOC: Cardinality-Invariant Neural Operator Policies for Scalable PDE Control
- [分离相空间流的逆问题重建](../conferences/icml-2026/cards/5901-6000.md#zhang26fo-architecture) · FlowPET: Physics-Informed Symplectic Flow Matching for Low-Count PET Reconstruction
- [固定网格上的部分多尺度PDE token](../conferences/icml-2026/cards/6001-6100.md#zhao26ak-architecture) · MeshTok: Efficient Multi-Scale Tokenization for Scalable PDE Transformers
- [物理mesh分块选择的原分辨率注意力](../conferences/icml-2026/cards/6001-6100.md#zhdanov26a-architecture) · (Sparse) Attention to the Details: Preserving Spectral Fidelity in ML-based Weather Forecasting Models
<!-- classification:end -->

<!-- conference-classification:start -->
## CoRL 2026

- [CoRE-VLA](../conferences/corl-2026/cards.md#paper-qku6lifnpu)
- [Learning Physics-Guided Residual Dynamics for Deformable Object Simulation](../conferences/corl-2026/cards.md#paper-3hsq75gmr9)
- [What Do You Need for Compositional Generalization in Diffusion Planning?](../conferences/corl-2026/cards.md#paper-hbhr1gxas0)
- [ProxiDex: Learning Dynamics-Guided Proximity Policy for Dexterous Manipulation](../conferences/corl-2026/cards.md#paper-ulcexirzjd)
- [ORD-WM: Learning Object-Centric Rigid Dynamics for 3D World Modeling in Robotic Manipulation](../conferences/corl-2026/cards.md#paper-xhjeeyhkhy)
- [Going with the Flow: Koopman Behavioral Models as Pseudo Planners for Visuo-Motor Dexterity](../conferences/corl-2026/cards.md#paper-8t3fxlyk9k)
- [HumanoidNDM: Closing the Training-Deployment Gap of Motion Tracking via Humanoid Neural Dynamics Model](../conferences/corl-2026/cards.md#paper-xcdyj95l5p)
- [FADA: Few-Shot Domain Adaptation via Dynamics Alignment for Humanoid Control](../conferences/corl-2026/cards.md#paper-mmrhlrwlfx)
- [Actuator Dynamics Curricula for Narrow-Viability Tasks in Legged Robot Learning](../conferences/corl-2026/cards.md#paper-mru8ihzsqr)

## NeurIPS 2026（暂收录）

- [Theory Guided and Interpretable Neural Operator Design for Partial Differential Equation Learning](../conferences/neurips-2026/cards.md#paper-151006)
- [Adaptive Coordinate Transforms for Neural Operators](../conferences/neurips-2026/cards.md#paper-156121)
- [Adaptive multiscale operator correction via learned spectral subspace and physics-informed optimization.](../conferences/neurips-2026/cards.md#paper-149265)
- [Advectra: Asymmetric Latent Transport for Non-Stationary Physics](../conferences/neurips-2026/cards.md#paper-148631)
- [ANCRe: Adaptive Neural Connection Reassignment for Efficient Depth Scaling](../conferences/neurips-2026/cards.md#paper-152945)
- [A Novel Schur-Decomposition-Based Weight Projection Method for Stable State-Space Neural-Network Architectures](../conferences/neurips-2026/cards.md#paper-151951)
- [AOT-POT: Adaptive Operator Transformation for Large-Scale PDE Pre-training](../conferences/neurips-2026/cards.md#paper-153792)
- [Approximate Memory Suffices for Universal Approximation with State Space Models](../conferences/neurips-2026/cards.md#paper-148575)
- [Beyond Single-Step Likelihood: Gibbs Variational Last Layers for Long-Horizon Dynamics Learning](../conferences/neurips-2026/cards-0002.md#paper-152213)
- [Beyond Unit-Circle Eigenvalues: Invariant Bases for Stable State Space Dynamics](../conferences/neurips-2026/cards-0002.md#paper-149242)
- [BitShift-RoPE: Zero-FLOP Relative Positional Encoding for Spiking Neural Network Transformers](../conferences/neurips-2026/cards-0002.md#paper-150476)
- [Causal Effects with Unobserved Unit Types in Interacting Human–AI Systems](../conferences/neurips-2026/cards-0003.md#paper-149288)
- [Closing the Approximation Gap in Simulation-free Latent SDEs](../conferences/neurips-2026/cards-0003.md#paper-150349)
- [Closing the Loop with Fixed-Point Self-Attention](../conferences/neurips-2026/cards-0003.md#paper-153850)
- [Coarse-to-Fine 3D MRI Reconstruction via Resolution-Agnostic Neural Operators](../conferences/neurips-2026/cards-0003.md#paper-151950)
- [Constrained Modulatory Reservoirs for Context-Dependent Computation](../conferences/neurips-2026/cards-0003.md#paper-152484)
- [CP-MLPs: A Tensor-Rank Theory of Tied and Untied MLP Blocks](../conferences/neurips-2026/cards-0003.md#paper-151658)
- [Decentralized Coupled Representation Learning](../conferences/neurips-2026/cards-0004.md#paper-151009)
- [Decomposing Effects in Neural Causal Models](../conferences/neurips-2026/cards-0004.md#paper-151693)
- [Deep-Koopman-KANDy: Dictionary Discovery for Deep-Koopman Operators with Kolmogorov-Arnold Networks for Dynamics](../conferences/neurips-2026/cards-0004.md#paper-152578)
- [Déjà View: Looping Transformers for Multi-View 3D Reconstruction](../conferences/neurips-2026/cards-0004.md#paper-154303)
- [DIAGNO: Diagonal Spherical Neural Operators for Heterogeneous Earth Dynamics Modeling](../conferences/neurips-2026/cards-0004.md#paper-154008)
- [Differentiating Network Design Objectives for Balancing Cost and Distance](../conferences/neurips-2026/cards-0004.md#paper-151671)
- [Diffusion Transformers with Residual Adaptive Layer Normalization](../conferences/neurips-2026/cards-0004.md#paper-151083)
- [DTA-GT: Direction- and Topology-Aware Graph Transformer for Neural Network Representation Learning](../conferences/neurips-2026/cards-0004.md#paper-153021)
- [Dynamic Convolutions Improve Transformers](../conferences/neurips-2026/cards-0004.md#paper-153747)
- [Efficient Generative Transformer Operators for Million-Point PDEs](../conferences/neurips-2026/cards-0004.md#paper-153950)
- [Efficient Training of Deep Spiking Neural Networks with Input-Driven Derivative-Free Updates](../conferences/neurips-2026/cards-0004.md#paper-152821)
- [End-to-End Identifiable and Consistent Recurrent Switching Dynamical Systems](../conferences/neurips-2026/cards-0005.md#paper-148468)
- [Equivariant Spherical Transformer for Efficient Molecular Modeling](../conferences/neurips-2026/cards-0005.md#paper-155430)
- [Extracting Governing Equations from Latent Dynamics via Multi-View Contrastive Learning](../conferences/neurips-2026/cards-0005.md#paper-155982)
- [Fast Reconstruction of Exact Maxwell Dynamics from Sparse Data](../conferences/neurips-2026/cards-0005.md#paper-148197)
- [FineRMoE: Dimension Expansion for Finer-Grained Expert with an Upcycling Approach](../conferences/neurips-2026/cards-0005.md#paper-156104)
- [FlashFFN: Multi-Head Decomposition Enables I/O-Aware Feed-Forward Network](../conferences/neurips-2026/cards-0005.md#paper-151360)
- [Foveal-Mamba: Inside-Out Ring Scanning with Recurrent Offset Prediction for Visual State Space Models](../conferences/neurips-2026/cards-0005.md#paper-148775)
- [Fractional State Space Transition for Long Sequence Modeling](../conferences/neurips-2026/cards-0005.md#paper-150427)
- [Frequency Domain Reservoir Computing](../conferences/neurips-2026/cards-0005.md#paper-151162)
- [From Cortical Synchronous Rhythm to Brain Inspired Learning Mechanism: An Oscillatory Spiking Neural Network with Time-Delayed Coordination](../conferences/neurips-2026/cards-0005.md#paper-151501)
- [Gaeta-Lie Neural SDEs: Symmetry-Regularized Learning of Stochastic Dynamics](../conferences/neurips-2026/cards-0006.md#paper-155867)
- [GAIA: Geometry-Adaptive Operator Learning for Forward and Inverse Problems](../conferences/neurips-2026/cards-0006.md#paper-149536)
- [GEAR: Generator-Adaptive State Space Models for Associative Recall](../conferences/neurips-2026/cards-0006.md#paper-155668)
- [GeoMamba: Geometry-Aware State Space Modeling for Image Restoration](../conferences/neurips-2026/cards-0006.md#paper-148154)
- [Geometry-Constrained Kolmogorov–Arnold Networks: Learning Edge Geometry via Banach Duality](../conferences/neurips-2026/cards-0006.md#paper-153809)
- [GeoTransolver: Learning Physics on Irregular Domains using Multi-scale Geometry Aware Physics Attention Transformer](../conferences/neurips-2026/cards-0006.md#paper-152562)
- [GPU Hierarchy Meets Structured Matrices: Fast Algorithms for State-Space Models](../conferences/neurips-2026/cards-0006.md#paper-149931)
- [GraDE: A Graph Diffusion Estimator for Frequent Subgraph Discovery in Neural Architectures](../conferences/neurips-2026/cards-0006.md#paper-148527)
- [GRNAgent: A Multimodal Graph Reasoning Agent for Gene Regulatory Network Inference](../conferences/neurips-2026/cards-0006.md#paper-149734)
- [Grounded-Exo2Ego: Structured Semantic Grounding for Robust Exocentric-to-Egocentric Video Generation](../conferences/neurips-2026/cards-0006.md#paper-152856)
- [Grounding Driving VLA via Inverse Kinematics](../conferences/neurips-2026/cards-0006.md#paper-152499)
- [Growing a Neural Network in Breadth, Depth, and Time](../conferences/neurips-2026/cards-0006.md#paper-148445)
- [HAI: Hierarchical Anchored Interaction for Multi-View Bimanual World Models](../conferences/neurips-2026/cards-0006.md#paper-152516)
- [HaM-World: Soft-Hamiltonian World Models with Selective Memory for Planning](../conferences/neurips-2026/cards-0006.md#paper-151714)
- [Harmonic Torsional Diffusion for Flexible Protein-Ligand Docking](../conferences/neurips-2026/cards-0006.md#paper-153661)
- [Hear, Localize, and Reason: Spatially Aware Scene Understanding for Audio-visual LLMs](../conferences/neurips-2026/cards-0006.md#paper-154862)
- [Heavy-Tailed Flow Matching via Random Clocks](../conferences/neurips-2026/cards-0006.md#paper-154575)
- [Hierarchical Denoising For Multi-Step Visual Reasoning](../conferences/neurips-2026/cards-0006.md#paper-151418)
- [Hierarchical Regime-Conditioned Dynamics for Spatiotemporal Graphs](../conferences/neurips-2026/cards-0006.md#paper-150192)
- [Higher-Order Cell Tracking Transformer](../conferences/neurips-2026/cards-0006.md#paper-150453)
- [HIMMEL: Hierarchical Interleaved Multi-stream Motion Encoding for Long Video Understanding](../conferences/neurips-2026/cards-0006.md#paper-151828)
- [Holo4D: Holistic 4D Reconstruction as Geometric Control for Video Diffusion](../conferences/neurips-2026/cards-0006.md#paper-154530)
- [HOPE: Hand-Object Pressure Estimation from Monocular Videos](../conferences/neurips-2026/cards-0006.md#paper-148354)
- [Horizon-Stream: Long-Horizon Attention for Streaming 3D Reconstruction](../conferences/neurips-2026/cards-0006.md#paper-153911)
- [Hybrid Probabilistic Zonotopes for Identifiable and Refinable Predictive Uncertainty](../conferences/neurips-2026/cards-0006.md#paper-154293)
- [HYDRA: Representation Harmonized Tokenization for Multimodal Generation and Understanding](../conferences/neurips-2026/cards-0006.md#paper-149164)
- [Hydra-X: Native Unified Multimodal Models with Holistic Visual Tokenizers](../conferences/neurips-2026/cards-0006.md#paper-155676)
- [HyFAD: Hybrid Time-Frequency Diffusion with Frequency-Aware Embedding for Time Series Imputation](../conferences/neurips-2026/cards-0006.md#paper-150001)
- [HyperGen: Learning Structure-Aware Spectral Flows for Hypergraph Generation](../conferences/neurips-2026/cards-0006.md#paper-150850)
- [Hypergraph Generation via Structured Stochastic Diffusion](../conferences/neurips-2026/cards-0006.md#paper-148881)
- [Hypergraph Generation with Latent Diffusion](../conferences/neurips-2026/cards-0006.md#paper-154651)
- [Hyper Input Convex Neural Networks for Shape Constrained Learning and Optimal Transport](../conferences/neurips-2026/cards-0006.md#paper-154124)
- [Hypernetworks for Dynamic Feature Selection](../conferences/neurips-2026/cards-0006.md#paper-154296)
- [IADR: Interface-Augmented Neural Operator for Phase-Field Mean-Curvature Flow](../conferences/neurips-2026/cards-0006.md#paper-149902)
- [Identifying Latent Neural Dynamics with Recognition-Parameterized Gaussian Process Dynamical Systems](../conferences/neurips-2026/cards-0007.md#paper-151974)
- [IGGT4D: Streaming 4D Instance-Grounded Geometry Transformer](../conferences/neurips-2026/cards-0007.md#paper-155215)
- [Image2Sim: Scaling Embodied Navigation via Generative Neural Simulator](../conferences/neurips-2026/cards-0007.md#paper-151849)
- [Imagine Before You Draw: Visual Prompt Engineering for Image Generation](../conferences/neurips-2026/cards-0007.md#paper-156043)
- [Improved State Mixing in Higher-order and Block Diagonal Linear Recurrent Networks](../conferences/neurips-2026/cards-0007.md#paper-152218)
- [In-Context Multi-Operator Learning with DeepOSets](../conferences/neurips-2026/cards-0007.md#paper-154682)
- [Inferring Computational Structure from Neural Recordings with Gain-Modulated Linear Dynamical Systems](../conferences/neurips-2026/cards-0007.md#paper-153994)
- [Inside the Loop: A Mechanistic Study of Weight-Tied Transformers on Depth-Bound Algorithmic Tasks](../conferences/neurips-2026/cards-0007.md#paper-150577)
- [Interactive 4D Volumetric Liquid Forecasting under Moving-Solid Interaction](../conferences/neurips-2026/cards-0007.md#paper-155706)
- [Inter-domain Inference for Gaussian Process Variational Autoencoders](../conferences/neurips-2026/cards-0007.md#paper-151321)
- [Interpretability-by-Design with Accurate Locally Additive Models and Conditional Feature Effects](../conferences/neurips-2026/cards-0007.md#paper-150129)
- [Interpretable Relational Inference with LLM-Guided Symbolic Dynamics Modeling](../conferences/neurips-2026/cards-0007.md#paper-154449)
- [Intrinsic-Preserving Schrödinger Bridge for Direct Part-Aware 3D Generation](../conferences/neurips-2026/cards-0007.md#paper-152274)
- [Isotropic Activation Functions Enable Deindividuated Neurons and Adaptive Topologies](../conferences/neurips-2026/cards-0007.md#paper-154076)
- [Iterative Latent Refinement for Value Learning in Offline Goal-Conditioned RL](../conferences/neurips-2026/cards-0007.md#paper-154947)
- [Iterative Nonlinear Computation Underlying Abstract Reasoning](../conferences/neurips-2026/cards-0007.md#paper-151990)
- [JODA: Composable Joint Dynamics for Articulated Objects](../conferences/neurips-2026/cards-0007.md#paper-148410)
- [KerONet: A Single Softmax Readout Suffices for Physics-Informed Operator Learning](../conferences/neurips-2026/cards-0007.md#paper-150115)
- [Koopman Generative Operators for Efficient Probabilistic Time-Series Forecasting](../conferences/neurips-2026/cards-0007.md#paper-153665)
- [K-PWM: Control-Oriented Structured World Models under Partial Observation](../conferences/neurips-2026/cards-0007.md#paper-152141)
- [Language Models Need Sleep](../conferences/neurips-2026/cards-0007.md#paper-154950)
- [Large Language Models as Graph Computational Solvers via Topology-aware Residual Attention](../conferences/neurips-2026/cards-0007.md#paper-149081)
- [LARGO: Low-Rank Hypernetwork for Handling Missing Modalities](../conferences/neurips-2026/cards-0007.md#paper-149154)
- [Latent Generative Solvers for Generalizable Long-Term Physics Simulation](../conferences/neurips-2026/cards-0007.md#paper-152793)
- [Layout Before Pixels: Topology-Anchored Transcriptome-to-Histology Generation](../conferences/neurips-2026/cards-0007.md#paper-152155)
- [LDM-is-AE: Latent Diffusion is an Intrinsic Auto-Encoder for End-to-End Image Generation](../conferences/neurips-2026/cards-0007.md#paper-155308)
- [Learning Agentic World Vision-Language-Action Models for Autonomous Driving](../conferences/neurips-2026/cards-0007.md#paper-150102)
- [Learning a Trajectory-Geometric Condition from Reasoning for VLA Planning](../conferences/neurips-2026/cards-0007.md#paper-153125)
- [Learning Causal Orderings for In-Context Tabular Prediction](../conferences/neurips-2026/cards-0007.md#paper-153895)
- [Learning Compositional Latent Structure with Vector Networks](../conferences/neurips-2026/cards-0007.md#paper-154634)
- [Learning Discrete Riemannian Metrics for Physical Fields with Cochain-Frame Equivariance](../conferences/neurips-2026/cards-0007.md#paper-150499)
- [Learning Event-to-Field Operators Without Interpolation](../conferences/neurips-2026/cards-0007.md#paper-155189)

<!-- conference-classification:end -->
