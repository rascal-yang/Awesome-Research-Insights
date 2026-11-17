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
- [科研 Agent 搜索](../conferences/icml-2026/cards/0401-0500.md#chen26r-architecture) · MARS: Modular Agent with Reflective Search for Automated AI Research
- [局部注意力与参数化记忆](../conferences/icml-2026/cards/0501-0600.md#chen26cg-architecture) · LoKiFormer: Locality-aware Attention with Decoupled Knowledge Memory for Efficient Large Language Model Pretraining
- [混合专家的按头并行](../conferences/icml-2026/cards/0701-0800.md#cui26c-architecture) · Multi-Head LatentMoE and Head Parallel: Communication-Efficient and Deterministic MoE Parallelism
- [预测分块上下文辅助逐词解码](../conferences/icml-2026/cards/0801-0900.md#dai26g-architecture) · Context-level Language Modeling by Learning Predictive Context Embeddings
- [长上下文的块级混合注意力](../conferences/icml-2026/cards/0801-0900.md#deng26v-architecture) · Neural Attention Search Linear: Towards Adaptive Token-Level Hybrid Attention Models
- [低维潜空间专家计算](../conferences/icml-2026/cards/1001-1100.md#elango26a-architecture) · Revisiting Efficiency–Accuracy Scaling in Mixture-of-Experts Architectures
- [可结构化高阶递推的词元混合](../conferences/icml-2026/cards/1001-1100.md#fagnou26a-architecture) · Trading Complexity for Expressivity Through Structured Generalized Linear Token Mixing
- [窗口注意力与递归长时记忆](../conferences/icml-2026/cards/1001-1100.md#fang26w-architecture) · Artificial Hippocampus Networks for Efficient Long-Context Modeling
- [仅对困难词元启动隐空间迭代](../conferences/icml-2026/cards/1101-1200.md#fu26t-architecture) · Think-at-Hard: Dynamic Looped Transformers for Improved Reasoning
- [频域乘法实现因果序列混合](../conferences/icml-2026/cards/1101-1200.md#gan26c-architecture) · Caracal: Causal Architecture via Spectral Mixing
- [用独立执行验证连接漏洞发现与代理记忆](../conferences/icml-2026/cards/1501-1600.md#he26i-architecture) · Co-RedTeam: Orchestrated Security Discovery and Exploitation with LLM Agents
- [为 MoE 解耦共用主谱与专家剩余分量](../conferences/icml-2026/cards/1601-1700.md#huang26i-architecture) · SD-MoE: Spectral Decomposition for Effective Expert Specialization
- [通过带噪吸引子迭代扩展潜空间推理](../conferences/icml-2026/cards/1601-1700.md#huang26l-architecture) · Equilibrium Reasoners: Learning Attractors Enables Scalable Reasoning
- [按块重排带动量的线性注意力递推](../conferences/icml-2026/cards/1701-1800.md#huang26af-architecture) · MDN: Parallelizing Stepwise Momentum for Delta Linear Attention
- [把金融工具调用写成带依赖的可并行计划](../conferences/icml-2026/cards/1701-1800.md#huang26ap-architecture) · Towards Professional-Grade Financial Agents: Benchmarking, Tooling, and Structured Reasoning
- [解耦代理图拓扑与节点实现](../conferences/icml-2026/cards/1701-1800.md#huang26by-architecture) · MAS-Architect: Declarative Multi-Agent System Design via Separation of Concerns
- [把局部相似 token 压成概念后再做重计算](../conferences/icml-2026/cards/1701-1800.md#huang26cl-architecture) · ConceptMoE: Adaptive Token-to-Concept Compression for Implicit Compute Allocation
- [从分项语义差异生成跨语言反例测试](../conferences/icml-2026/cards/1801-1900.md#ibrahimzada26a-architecture) · MatchFixAgent: Language-Agnostic Autonomous Repository-Level Code Translation Validation and Repair
- [把无上下文前馈支路预计算为词表](../conferences/icml-2026/cards/1801-1900.md#jaiswal26a-architecture) · MemoryLLM: Plug-n-Play Interpretable Feed-Forward Memory for Transformers
- [让离散发词策略读取连续演化状态](../conferences/icml-2026/cards/1801-1900.md#jia26h-architecture) · Text Generation as Continuous Latent Dynamics via Reinforcement Learning

<a id="by-computer-vision"></a>

### 计算机视觉

- [视频分词](../conferences/icml-2026/cards/0101-0200.md#atanov26a-architecture) · VideoFlexTok: Flexible-Length Coarse-to-Fine Video Tokenization
- [像素空间扩散](../conferences/icml-2026/cards/0101-0200.md#baade26a-architecture) · Latent Forcing: Reordering the Diffusion Trajectory for Pixel-Space Image Generation
- [少样本布局生成](../conferences/icml-2026/cards/0201-0300.md#bao26f-architecture) · Envisioning Beyond the Few: Disentangled Semantics and Primitives for Few-Shot Atypical Layout-to-Image Generation
- [按空间分组的同位词元预测](../conferences/icml-2026/cards/0501-0600.md#chen26du-architecture) · Autoregression with Self-Token Prediction
- [压缩成像的连续光谱先验](../conferences/icml-2026/cards/0601-0700.md#chen26ga-architecture) · Phy-CoSF: Physics-Guided Continuous Spectral Fields Reconstruction and Spectral Super-Resolution for Snapshot Compressive Imaging
- [开放词汇三维实例分割](../conferences/icml-2026/cards/0701-0800.md#choy26a-architecture) · SpaCeFormer: Fast Proposal-Free Open-Vocabulary 3D Instance Segmentation
- [原生四维体素自编码](../conferences/icml-2026/cards/0901-1000.md#ding26u-architecture) · Native Spatio-Temporal 4D Variational Autoencoder
- [照片结构重构的动作条件编辑](../conferences/icml-2026/cards/0901-1000.md#du26c-architecture) · AesFormer: Transform Everyday Photos into Beautiful Memories
- [病理去焦模糊的局部积分算子](../conferences/icml-2026/cards/0901-1000.md#duan26e-architecture) · Discontinuous Galerkin Neural Operator for Pathology Defocus Deblurring
- [单步伪装物体掩码预测](../conferences/icml-2026/cards/1101-1200.md#fu26l-architecture) · CODiff: One-Step Diffusion Model for Camouflaged Object Detection
- [按类别难度隔离位姿学习梯度](../conferences/icml-2026/cards/1201-1300.md#gao26aq-architecture) · DecomPose: Disentangling Cross-Category Optimization Contention for Category-Level 6D Object Pose Estimation
- [持久三维状态的交互视频世界模型](../conferences/icml-2026/cards/1201-1300.md#garcin26a-architecture) · Beyond Pixel Histories: World Models with Persistent 3D State
- [姿态可控插入的三路视觉条件](../conferences/icml-2026/cards/1301-1400.md#gong26f-architecture) · Direct 3D-Aware Object Insertion via Decomposed Visual Proxies
- [内容伪迹分离的生成图像鉴别](../conferences/icml-2026/cards/1401-1500.md#guo26ag-architecture) · OmniAID: Decoupling Semantics and Artifacts for Universal AI-Generated Image Detection in the Wild
- [压缩高光谱重建的局部与全局协调](../conferences/icml-2026/cards/1401-1500.md#han26c-architecture) · Bridging Local–Global Dissonance: Learning from Compressive Measurements for Hyperspectral Reconstruction
- [按下游生成容量选择视觉潜通道](../conferences/icml-2026/cards/1401-1500.md#hansen-estruch26a-architecture) · ViTok-v2: Scaling Native Resolution Autoencoders to 5 Billion Parameters
- [沿同心环聚合后做短径向状态扫描](../conferences/icml-2026/cards/1601-1700.md#hsieh26a-architecture) · Partial Ring Scan: Revisiting Scan Order in Vision State Space Models
- [让卷积滤波器随观察角连续变化](../conferences/icml-2026/cards/1701-1800.md#hwang26f-architecture) · Continuous Viewpoint Adaptation for Single View 3D Object Reconstruction
- [把相机射线变成可共同去噪的像素](../conferences/icml-2026/cards/1801-1900.md#jang26f-architecture) · Rays as Pixels: Learning A Joint Distribution of Videos and Camera Trajectories
- [级联空间边界与频域全局信息做杂乱分割](../conferences/icml-2026/cards/1801-1900.md#javaid26a-architecture) · Towards Effective Waste Segmentation for Automated Waste Recycling in Cluttered Background
- [给轻量扩散编解码器预训练重建任务](../conferences/icml-2026/cards/1801-1900.md#jia26i-architecture) · CoD-Lite: Real-Time Diffusion-Based Generative Image Compression

<a id="by-nlp"></a>

### 自然语言处理

- [文本编码与掩码重建解耦](../conferences/icml-2026/cards/0801-0900.md#dervishi26a-architecture) · Separating Representation from Reconstruction Enables Scalable Text Encoders
- [纯因果 Transformer 的音频分词](../conferences/icml-2026/cards/1301-1400.md#gong26c-architecture) · Scaling Transformers for End-to-End Discrete Audio Tokenization
- [去噪网络与解掩顺序共同训练](../conferences/icml-2026/cards/1501-1600.md#hong26f-architecture) · Unifying Masked Diffusion Models with Various Generation Orders and Beyond
- [按符号建共享流使改名可交换](../conferences/icml-2026/cards/1801-1900.md#isik26a-architecture) · Names Don’t Matter: Symbol-Invariant Transformer for Open-Vocabulary Learning

<a id="by-reinforcement-learning"></a>

### 强化学习

- [连续控制动作表示](../conferences/icml-2026/cards/0201-0300.md#bian26a-architecture) · RN-D: Discretized Categorical Actors for On-Policy Reinforcement Learning
- [以潜状态分布替代像素重构并允许替换约束先验](../conferences/icml-2026/cards/1701-1800.md#huang26ba-architecture) · VJEPA: Variational Joint Embedding Predictive Architectures as Probabilistic World Models

<a id="by-robotics"></a>

### 机器人学

- [VLA 潜空间推理](../conferences/icml-2026/cards/0101-0200.md#bai26h-architecture) · Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models
- [频域分层动作策略](../conferences/icml-2026/cards/0401-0500.md#cao26u-architecture) · Hierarchical Policy Learning via Spectral Decomposition
- [SE(3) 位姿扩散策略](../conferences/icml-2026/cards/0701-0800.md#chuang26a-architecture) · The Lie We Tell: Correcting the Euclidean Fallacy in Vision Language Action Policies via Score Matching on Tangent Space
- [第一视角三维检测的时序记忆](../conferences/icml-2026/cards/0901-1000.md#ding26x-architecture) · Embodied-DETR: End-to-End Temporal 3D Object Detection in Egocentric Views
- [把长演示学习的行为原型按在线阶段实例化](../conferences/icml-2026/cards/1601-1700.md#hu26ad-architecture) · From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model
- [在同一软体仿真状态接入环境力和动作](../conferences/icml-2026/cards/1701-1800.md#huang26bh-architecture) · SoMA: A Real-to-Sim Neural Simulator for Robotic Soft-Body Manipulation
- [让高频动作复用低频理解注意力缓存](../conferences/icml-2026/cards/1701-1800.md#huang26cb-architecture) · AutoMoT: A Unified Vision-Language-Action Model with Asynchronous Mixture -of-Transformers for End-to-End Autonomous Driving
- [按子任务进展触发规划并整理长期记忆](../conferences/icml-2026/cards/1801-1900.md#ji26k-architecture) · HiMe: Hierarchical Embodied Memory for Long-Horizon Vision-Language-Action Control
- [用动作条件潜状态评价驾驶计划](../conferences/icml-2026/cards/1801-1900.md#jia26f-architecture) · DriveWorld-VLA: Unified Latent-Space World Modeling with Vision–Language–Action for Autonomous Driving

<a id="by-multimodal"></a>

### 多模态学习

- [交互式人物检索](../conferences/icml-2026/cards/0101-0200.md#bai26j-architecture) · Interactive Person Retrieval via Multi-Turn Multimodal Conversation
- [遥感跨模态的共享潜空间扩散](../conferences/icml-2026/cards/0601-0700.md#chen26go-architecture) · Any2Any: Unified Arbitrary Modality Translation for Remote Sensing
- [阵列几何条件化的空间音频词元](../conferences/icml-2026/cards/0801-0900.md#dementyev26a-architecture) · PhaseCoder: Microphone Geometry-Agnostic Spatial Audio Understanding for Multimodal LLMs
- [持续学习专家的置信加权协作](../conferences/icml-2026/cards/1101-1200.md#forhad26a-architecture) · Mixing Expertise with Confidence: A Mixture of Experts Framework for Robust Multi-Modal Continual Learning
- [交替状态与转移的视觉世界模型](../conferences/icml-2026/cards/1201-1300.md#gao26am-architecture) · DynaVieW: Schema-Guided World Modeling for Understanding Hierarchical Visual Dynamics
- [用去噪轨迹保留视觉推理状态](../conferences/icml-2026/cards/1501-1600.md#he26ac-architecture) · DiffThinker: Towards Generative Multimodal Reasoning with Diffusion Models
- [用轻量状态判断何时重做视频推理](../conferences/icml-2026/cards/1601-1700.md#hu26q-architecture) · RVAS: Referring Video Active Exploration and Segmentation
- [把语义提示留在视频编码侧](../conferences/icml-2026/cards/1601-1700.md#hu26u-architecture) · MoVie: Multimodal Video Compression with Text Guidance
- [按文本词元和三维潜块的粒度拆分自回归分支](../conferences/icml-2026/cards/1701-1800.md#huang26be-architecture) · CG-MLLM: Captioning and Generating 3D content via Multi-modal Large Language Models

<a id="by-ml-foundations"></a>

### 机器学习基础与统计

- [脉冲状态空间模型](../conferences/icml-2026/cards/0001-0100.md#agrawal26c-architecture) · A Spiking Heterogeneous Harmonic Resonate-and-Fire State Space Model for Time Series
- [可解释风险排序](../conferences/icml-2026/cards/0101-0200.md#babbar26a-architecture) · Falling Trees: A Model Class for Interpretable Risk Prioritization
- [世界模型](../conferences/icml-2026/cards/0101-0200.md#baek26b-architecture) · Learning to Theorize the World from Observation
- [可线性化网络](../conferences/icml-2026/cards/0201-0300.md#berman26c-architecture) · Who Said Neural Networks Aren’t Linear?
- [非高斯扩散](../conferences/icml-2026/cards/0201-0300.md#bertholom26a-architecture) · M-Star: Markovian Projection of Star-Shaped Diffusion for Exponential Family Distributions
- [离散函数近似](../conferences/icml-2026/cards/0301-0400.md#candogan26b-architecture) · Deep Flow Networks
- [受约束域回归](../conferences/icml-2026/cards/0401-0500.md#chakraborty26a-architecture) · Probabilistically-routed Bayesian Additive Spanning Trees for Learning on Constrained Domains
- [时序计数分解](../conferences/icml-2026/cards/0401-0500.md#chaussard26a-architecture) · Independent Component Discovery in Temporal Count Data
- [自回归与流匹配耦合预测](../conferences/icml-2026/cards/0601-0700.md#cheng26h-architecture) · CoGenCast: A Coupled Autoregressive–Flow Generative Framework for Time Series Forecasting
- [外生时序的历史条件生成](../conferences/icml-2026/cards/0601-0700.md#cheng26t-architecture) · KITE: Knowledge-Guided Probabilistic Modeling for Time Series Forecasting with Exogenous Variables
- [用 Transformer 电路实现 Lloyd 迭代](../conferences/icml-2026/cards/0701-0800.md#clarkson26a-architecture) · Transformer Circuits Can Realize Clustering Algorithms
- [混合专家式概念瓶颈](../conferences/icml-2026/cards/0801-0900.md#de-santis26a-architecture) · Mixture of Concept Bottleneck Experts
- [联邦学习的弹性共享专家](../conferences/icml-2026/cards/0901-1000.md#du26d-architecture) · FedEMoE: Improving Personalization on Heterogeneous Federated Learning via Elastic Mixture of Experts Architecture
- [带长历史压缩的时序插补](../conferences/icml-2026/cards/1001-1100.md#fan26h-architecture) · Rethinking Time-Series Imputation as Conditional Inference along Temporal Evolution
- [跨尺度共享的递归状态空间模型](../conferences/icml-2026/cards/1001-1100.md#fang26p-architecture) · Dynamic Fractal Mamba: A Neural Renormalization Group Flow for Scale-Invariant Sequence Modeling
- [符号置换等变的循环推理](../conferences/icml-2026/cards/1101-1200.md#freinschlag26a-architecture) · Symbol-Equivariant Recurrent Reasoning Models
- [可解析径向归一化流](../conferences/icml-2026/cards/1201-1300.md#gerdes26a-architecture) · Analytic Bijections for Smooth and Interpretable Normalizing Flows
- [时序预测的可调连续时间基](../conferences/icml-2026/cards/1301-1400.md#graf26a-architecture) · FlowState: Sampling-Rate-Equivariant Time-Series Forecasting
- [连续秩噪声配合前缀条件的排列采样](../conferences/icml-2026/cards/1501-1600.md#he26ax-architecture) · Learning Permutation Distributions via Reflected Diffusion on Ranks
- [以样条局部支撑减少片上单样本更新](../conferences/icml-2026/cards/1501-1600.md#hoang26a-architecture) · Ultrafast On-Chip Online Learning via Spline Locality in Kolmogorov–Arnold Networks
- [按周期尺度掩码并门控辅助通道](../conferences/icml-2026/cards/1601-1700.md#hu26bf-architecture) · TeamWork: Multivariate Time Series Anomaly Detection via Asymmetric Role-aware Channel Modeling
- [并行建模同类型元素和跨类型约束](../conferences/icml-2026/cards/1701-1800.md#huang26bl-architecture) · A General Neural Backbone for Mixed-Integer Linear Optimization via Dual Attention
- [训练注意力密度估计器来复用跨分布核行为](../conferences/icml-2026/cards/1801-1900.md#ilin26a-architecture) · DiScoFormer: Plug-In Density and Score Estimation with Transformers
- [把几何对称落实为注意力参考系共享](../conferences/icml-2026/cards/1801-1900.md#islam26a-architecture) · Platonic Transformers: A Solid Choice For Equivariance
- [用并行代理写入近似迭代状态更新](../conferences/icml-2026/cards/1901-2000.md#jiang26e-architecture) · PRISM: Parallel Residual Iterative Sequence Model

<a id="by-graph-and-recommendation"></a>

### 图学习与推荐

- [知识图谱多跳问答](../conferences/icml-2026/cards/0201-0300.md#bandyopadhyay26a-architecture) · RSF-GLLM: Bridging the Semantic Gap in Multi-Hop Knowledge Graph QA via Recurrent Soft-Flow and Decoupled LLM Generation
- [生成式电商检索](../conferences/icml-2026/cards/0501-0600.md#chen26al-architecture) · OneSearch: A Preliminary Exploration of the Unified End-to-End Generative Framework for E-commerce Search
- [动态图的可学习信息耗散](../conferences/icml-2026/cards/0801-0900.md#de-castelli26a-architecture) · Adaptive Memory Retention in Dynamic Graphs
- [图动力学的能量与切向流](../conferences/icml-2026/cards/1001-1100.md#eliasof26a-architecture) · Graph Neural Dynamics via Learned Energy and Tangential Flows
- [超边潜类型与多通道传播](../conferences/icml-2026/cards/1001-1100.md#fang26g-architecture) · MC-HNN: Learning Latent Structural Semantics and High-Rank Representations for Hypergraph Neural Networks
- [图傅里叶变换的柯西分解](../conferences/icml-2026/cards/1101-1200.md#fernandez26a-architecture) · L2G-NET: Local to Global Spectral Graph Neural Networks via Cauchy Factorizations
- [超图生成的多尺度展开](../conferences/icml-2026/cards/1101-1200.md#gailhard26a-architecture) · Feature-Aware (Hyper)graph Generation via Next-Scale Prediction
- [以分层极大团表示超边](../conferences/icml-2026/cards/1201-1300.md#gantes26a-architecture) · SuperHype: Hypergraph Generation via Graph-Superposition Decomposition
- [异配图的有符号分层 Haar 滤波](../conferences/icml-2026/cards/1601-1700.md#hossen26a-architecture) · Hierarchical Multi Scale Graph Neural Networks: Scalable Heterophilous Learning with Oversmoothing and Oversquashing Mitigation
- [在保全关系语义的前提下学习表的节点和边角色](../conferences/icml-2026/cards/1701-1800.md#huang26ax-architecture) · Is Fixing Schema Graphs Necessary? Full-Resolution Graph Structure Learning for Relational Deep Learning
- [用地理条件和轴向注意力表达出行流竞争](../conferences/icml-2026/cards/1701-1800.md#huang26cj-architecture) · GeoFlow: Geo-Aware Modeling of Inter-Area Relationships in Origin-Destination Flow Prediction and Generation

<a id="by-scientific-ml"></a>

### 科学机器学习

- [物理约束学习](../conferences/icml-2026/cards/0001-0100.md#abijuru26a-architecture) · Physics-Informed Residual Flows
- [时空预测](../conferences/icml-2026/cards/0001-0100.md#ai26f-architecture) · Nested Spatio-Temporal Time Series Forecasting
- [单细胞反事实编辑](../conferences/icml-2026/cards/0001-0100.md#andersson26a-architecture) · scCBGM: Single-Cell Editing via Concept Bottlenecks
- [量子生成先验](../conferences/icml-2026/cards/0101-0200.md#bacarreza26a-architecture) · Quantum latent distributions in deep generative models
- [单细胞时间建模](../conferences/icml-2026/cards/0201-0300.md#balik26a-architecture) · Modeling Temporal scRNA-seq Data with Latent Gaussian Process and Optimal Transport
- [多保真数据同化](../conferences/icml-2026/cards/0201-0300.md#bao26d-architecture) · Cheap2Rich: A Multi-Fidelity Framework for Data Assimilation and System Identification of Multiscale Physics - Rotating Detonation Engines
- [固体力学代理模型](../conferences/icml-2026/cards/0201-0300.md#bazzi26a-architecture) · Physics-Informed Coarsening for Multigrid Graph Neural Surrogates
- [随机动力学生成](../conferences/icml-2026/cards/0201-0300.md#berman26b-architecture) · Stochastic Lifting for Generating Trajectories of Stochastic Physical Systems
- [连续时间动力学](../conferences/icml-2026/cards/0301-0400.md#brandle26a-architecture) · Continuous-Time Piecewise-Linear Recurrent Neural Networks
- [几何轨迹生成](../conferences/icml-2026/cards/0301-0400.md#brinke26a-architecture) · STFlow: Data-Coupled Flow Matching for Geometric Trajectory Simulation
- [无线传播建模](../conferences/icml-2026/cards/0301-0400.md#bu26d-architecture) · Stochastic Neural Ray Tracing for Radio Frequency Channel Modeling
- [实验室布局生成](../conferences/icml-2026/cards/0401-0500.md#cao26ad-architecture) · LabBuilder: Protocol-Grounded 3D Layout Generation for Interactable and Safe Laboratory
- [生物声学定位](../conferences/icml-2026/cards/0401-0500.md#chasmai26b-architecture) · Bioacoustic Geolocation: Species Sounds as Geographic Signals
- [对流风暴短时预报](../conferences/icml-2026/cards/0401-0500.md#chen26aa-architecture) · StormInsight: Hierarchical Environmental Forcing and Vertical Coupling for Convective Systems Evolution
- [电子密度条件分子生成](../conferences/icml-2026/cards/0501-0600.md#chen26ai-architecture) · From Holo Pockets to Electron Density: GPT-style Drug Design with Density
- [功能条件蛋白质共生成](../conferences/icml-2026/cards/0501-0600.md#chen26cu-architecture) · Co-Generative De Novo Functional Protein Design
- [基因组性状到土壤碳动力学](../conferences/icml-2026/cards/0701-0800.md#collart26a-architecture) · Constrained hybrid modelling to predict microbial dynamics and organic matter turnover in soil systems
- [分子构象与合成路线的联合潜空间](../conferences/icml-2026/cards/0701-0800.md#cretu26a-architecture) · SynLaD: Latent Diffusion for Generating Synthesizable Molecules Conditioned on 3D Pharmacophore Profiles
- [机械属性场的自适应稀疏体素](../conferences/icml-2026/cards/0801-0900.md#dagli26a-architecture) · Adaptive Volumetric Mechanical Property Fields Invariant to Resolution
- [时间驱动空间网络参数](../conferences/icml-2026/cards/0801-0900.md#dai26a-architecture) · TINNs: Time-Induced Neural Networks for Solving Time-Dependent PDEs
- [工况条件下的分层图流匹配](../conferences/icml-2026/cards/0801-0900.md#deng26c-architecture) · Condition-Aware Graph Flow Matching for Modeling the Distributions of Complex Fluid Systems
- [周期晶体电荷密度的傅里叶重建](../conferences/icml-2026/cards/1001-1100.md#elsborg26a-architecture) · Global Plane Waves from Local Gaussians: Periodic Charge Densities in a Blink
- [生物序列模型的异构架构搜索](../conferences/icml-2026/cards/1001-1100.md#fang26u-architecture) · BIOARC: Discovering Optimal Neural Architectures for Biological Foundation Models
- [脑电潜事件的电生理先验](../conferences/icml-2026/cards/1001-1100.md#feng26b-architecture) · LERD: Latent Event-Relational Dynamics for Neurodegenerative Classification
- [辛降维的 Hamilton 动力学](../conferences/icml-2026/cards/1101-1200.md#friedl26a-architecture) · Learning Hamiltonian Dynamics at Scale: A Differential-Geometric Approach
- [飞行器拓扑与连续参数的层级扩散](../conferences/icml-2026/cards/1201-1300.md#ghiglino26a-architecture) · "Do Diffusion Models Dream of Electric Planes?" Discrete and Continuous Simulation-Based Inference for Aircraft Design
- [点云到气动场的跨层解码](../conferences/icml-2026/cards/1401-1500.md#hagnberger26a-architecture) · SMART: Scalable Mesh-free Aerodynamic Simulations from Raw Geometries using a Transformer-based Surrogate Model
- [分距离层覆盖稠密原子相互作用](../conferences/icml-2026/cards/1501-1600.md#hong26h-architecture) · Large-Scale Molecular Dynamics Simulation: Direct Interatomic Modeling with Dilated Message Passing
- [按局部组织形态路由生成速度场](../conferences/icml-2026/cards/1601-1700.md#hu26at-architecture) · MoLF: Mixture-of-Latent-Flow for Pan-Cancer Spatial Gene Expression Prediction from Histology
- [基于局部轴对齐流式计算等变注意力](../conferences/icml-2026/cards/1701-1800.md#huang26p-architecture) · E2Former-V2: On-the-Fly Equivariant Attention with Linear Activation Memory
- [用结构约束和功能需求共同求潜在脑网络流](../conferences/icml-2026/cards/1701-1800.md#huang26am-architecture) · Uncovering Latent Communication Patterns in Brain Networks via Adaptive Flow Routing
- [把系统辨识摊销为轨迹条件下的向量场查询](../conferences/icml-2026/cards/1701-1800.md#hubers26a-architecture) · Foundation Inference Models for Ordinary Differential Equations
<!-- classification:end -->
