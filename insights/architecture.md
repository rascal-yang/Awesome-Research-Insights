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
- [解码前让行为、隐状态和记忆迭代对齐](../conferences/icml-2026/cards/1901-2000.md#jiang26aw-architecture) · BRIDGE: Triangular Fixed-Point Refinement for Long-Horizon Persona Consistency
- [将协作步骤做成可检索的潜通信原语](../conferences/icml-2026/cards/1901-2000.md#jin26c-architecture) · Agent Primitives: Reusable Latent Building Blocks for Multi-Agent Systems
- [循环保留了迭代结构的中间层](../conferences/icml-2026/cards/2001-2100.md#kapl26a-architecture) · From Growing to Looping: A Unified View of Iterative Computation in LLMs
- [共享键和值以减少自回归缓存](../conferences/icml-2026/cards/2001-2100.md#kayyam26a-architecture) · Do Transformers Need Three Projections? Systematic Study of QKV Variants
- [让稀疏解码器显式建模特征交互](../conferences/icml-2026/cards/2201-2300.md#koromilas26a-architecture) · PolySAE: Modeling Feature Interactions in Sparse Autoencoders via Polynomial Decoding
- [共享残差块的双流归一化](../conferences/icml-2026/cards/2401-2500.md#li26ba-architecture) · SiameseNorm: Breaking the Barrier to Reconciling Pre/Post-Norm
- [用概率电路耦合同步解除掩码的词元](../conferences/icml-2026/cards/2501-2600.md#li26fd-architecture) · Breaking the Factorization Barrier in Diffusion Language Models
- [让代理生成任务拓扑并用层级图保留上下文](../conferences/icml-2026/cards/2501-2600.md#li26gk-architecture) · OpenSage: Self-programming Agent Generation Engine
- [让位置编码随上下文依赖重新排布](../conferences/icml-2026/cards/2601-2700.md#li26jq-architecture) · RePo: Language Models with Context Re-Positioning
- [在数据代理任务图上局部重配失败分支](../conferences/icml-2026/cards/2801-2900.md#liu26at-architecture) · $R^3$DAO: Reactive Recovery and Reconstruction for Long-horizon Data Agent Orchestration
- [残差流分叉的并行潜空间计算](../conferences/icml-2026/cards/2801-2900.md#liu26cx-architecture) · Thoughtbubbles: an Unsupervised Method for Parallel Thinking in Latent Space
- [用多视图索引压缩交互记忆并按意图检索](../conferences/icml-2026/cards/2901-3000.md#liu26dx-architecture) · SimpleMem: Efficient Lifelong Memory for LLM Agents
- [用超网络将上下文映射为 LoRA](../conferences/icml-2026/cards/2901-3000.md#liu26ek-architecture) · SHINE: A Scalable In-Context Hypernetwork for Mapping Context to LoRA in a Single Pass
- [把上下文键值视为逐步实例化的两层网络](../conferences/icml-2026/cards/3001-3100.md#lu26aq-architecture) · HyperMLP: An Integrated Perspective for Sequence Modeling
- [以自激活秩一键值原子积累持续学习记忆](../conferences/icml-2026/cards/3001-3100.md#lu26au-architecture) · Little By Little: Continual Learning via Incremental Mixture of Rank-1 Associative Memory Experts
- [线性注意头内记忆分组](../conferences/icml-2026/cards/3201-3300.md#mei26a-architecture) · Head-in-Head in Linear Attention
- [用结构化技能和非参数 PPO 门升级代理记忆](../conferences/icml-2026/cards/3201-3300.md#mi26d-architecture) · Skill-Pro: Learning Reusable Skills from Experience via Non-Parametric PPO for LLM Agents
- [跨词元高层反馈](../conferences/icml-2026/cards/3301-3400.md#mohan26b-architecture) · Turbo Connection: Reasoning as Information Flow from Higher to Lower Layers
- [有限自动机状态注入](../conferences/icml-2026/cards/3301-3400.md#mohri26a-architecture) · Rational Transductors

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
- [用整体生成约束零件配准](../conferences/icml-2026/cards/1901-2000.md#jiang26ab-architecture) · CRAG: Can 3D Generative Models Help 3D Assembly?
- [用平衡层给不同生成尺度分配步数](../conferences/icml-2026/cards/1901-2000.md#jiang26ah-architecture) · Visual Implicit Autoregressive Modeling
- [用关节身份锚定状态更新并显式暴露深度](../conferences/icml-2026/cards/1901-2000.md#jiang26bb-architecture) · StructMamPose: From Sequential Perception to Structural Reasoning for 3D Human Pose Estimation
- [让等变视觉与符号决策共同驱动旋转](../conferences/icml-2026/cards/2001-2100.md#khazoum26a-architecture) · A Deep Learning Model of Mental Rotation Informed by Interactive VR Experiments
- [以重建手的接触力驱动可变形物体并反向校正手](../conferences/icml-2026/cards/2301-2400.md#lee26ao-architecture) · PhysHanDI: Physics-Based Reconstruction of Hand-Deformable Object Interactions
- [先分开学习几何和语义关系再交互](../conferences/icml-2026/cards/2301-2400.md#lei26b-architecture) · Synergistic Space-Vision Processing for Predicate Inference
- [共享去噪轨迹以联合生成可编辑视频层](../conferences/icml-2026/cards/2401-2500.md#li26l-architecture) · LayerT2V: A Unified Multi-Layer Video Generation Framework
- [为不均衡检测任务分配异构专家路由](../conferences/icml-2026/cards/2401-2500.md#li26o-architecture) · DroneDINO: Towards Heterogeneous Routed Mixture of Experts for Drone-based Unified Object Detection
- [把二维重叠对象按 Z 顺序分开生成再合成](../conferences/icml-2026/cards/2401-2500.md#li26ah-architecture) · OcclusionFormer: Arranging Z-Order for Layout-Grounded Image Generation
- [透明物体法线预测的密集视觉条件](../conferences/icml-2026/cards/2401-2500.md#li26ao-architecture) · TransNormal: Dense Visual Semantics for Diffusion-based Transparent Object Normal Estimation
- [预训练注意力的线性化迁移](../conferences/icml-2026/cards/2401-2500.md#li26bc-architecture) · Linearizing Vision Transformer with Test-Time Training
- [用实例深度锚初始化人体网格](../conferences/icml-2026/cards/2401-2500.md#li26bq-architecture) · DGG-HMR: Multi-Person Human Mesh Recovery with Depth-Guided Geometric Anchoring
- [先聚焦视频关系区间再生成稀有事件补样](../conferences/icml-2026/cards/2401-2500.md#li26bx-architecture) · SegPVSG: Panoptic Video Scene Graph Generation via Temporal Focusing and Generative Augmentation
- [在潜令牌上求解空间光谱融合](../conferences/icml-2026/cards/2501-2600.md#li26en-architecture) · Solving Spatial-Spectral Fusion with Latent Spectral Operators
- [可识别虚拟人脸的身份绑定水印](../conferences/icml-2026/cards/2501-2600.md#li26gt-architecture) · Towards Trustworthy and Identifiable Virtual Face Generation
- [以分层射线交点同时预测可见与遮挡表面](../conferences/icml-2026/cards/2601-2700.md#li26jg-architecture) · LaRI: Layered Ray Intersections for Single-view 3D Geometric Reasoning
- [共享波段前缀并连续查询空间分辨率](../conferences/icml-2026/cards/2601-2700.md#liang26c-architecture) · Hyperspectral Image Fusion with Spectral-Band and Fusion-Scale Agnosticism
- [把静态墨迹转成少步脉冲并压缩空白](../conferences/icml-2026/cards/2601-2700.md#liang26j-architecture) · Spike-HTR: Spiking Neural Transformer for Handwritten Text Recognition
- [在世界坐标分开编辑人物轨迹和动作](../conferences/icml-2026/cards/2701-2800.md#liang26ad-architecture) · RealisMotion: Decomposed Human Motion Control and Video Generation in the World Space
- [任意几何先验的前馈三维重建](../conferences/icml-2026/cards/2801-2900.md#liu26cw-architecture) · WorldMirror: Universal 3D World Reconstruction with Any-Prior Prompting
- [将二维旋转位置编码扩展到均匀斜向投影](../conferences/icml-2026/cards/2801-2900.md#liu26dj-architecture) · Spiral RoPE: Rotate Your Rotary Positional Embeddings in the 2D Plane
- [把单调性硬编码到盲逆问题的前向算子](../conferences/icml-2026/cards/2901-3000.md#liu26eb-architecture) · Resolving Blind Inverse Problems under Dynamic Range Compression via Structured Forward Operator Modeling
- [用边分解三角候选和固定步偏移替代测试时优化](../conferences/icml-2026/cards/2901-3000.md#liu26gs-architecture) · FastSESR: Fast Scene-level Explicit Surface Reconstruction
- [从原视频到去物视频直接学习随机桥](../conferences/icml-2026/cards/2901-3000.md#lou26b-architecture) · Learning Stochastic Bridges for Video Object Removal via Video-to-Video Translation
- [用两级路由将长序列任务接入不同专家](../conferences/icml-2026/cards/2901-3000.md#lou26c-architecture) · Scaling Continual Learning to 300+ Tasks with Bi-Level Routing Mixture-of-Experts
- [稀疏动作的逐尺度自回归](../conferences/icml-2026/cards/3001-3100.md#luo26af-architecture) · MotionMAR: Multi-scale Auto-Regressive Human Motion Reconstruction from Sparse Observations
- [单目四维几何运动查询](../conferences/icml-2026/cards/3001-3100.md#luo26al-architecture) · 4RC: 4D Reconstruction via Conditional Querying Anytime and Anywhere
- [用降噪脉冲单元和双向多尺度网络处理事件相机](../conferences/icml-2026/cards/3101-3200.md#ma26x-architecture) · Bio-Vision-Inspired Spiking Neural Networks for Object Detection with Event Cameras
- [红外小目标背景流形](../conferences/icml-2026/cards/3101-3200.md#ma26au-architecture) · CodeMamba: Shifting from Target Semantics to Self-Supervised Background Manifold Learning for Singularity Detection in Infrared Sequences
- [让二维 RoPE 在大图分辨率均匀分配方向](../conferences/icml-2026/cards/3301-3400.md#min26f-architecture) · Compass-RoPE: Isotropic Rotary Position Embeddings for Vision Transformers
- [证据混合校准](../conferences/icml-2026/cards/3301-3400.md#mohammed26a-architecture) · GEM-FI: Gated Evidential Mixtures with Fisher Modulation

<a id="by-nlp"></a>

### 自然语言处理

- [文本编码与掩码重建解耦](../conferences/icml-2026/cards/0801-0900.md#dervishi26a-architecture) · Separating Representation from Reconstruction Enables Scalable Text Encoders
- [纯因果 Transformer 的音频分词](../conferences/icml-2026/cards/1301-1400.md#gong26c-architecture) · Scaling Transformers for End-to-End Discrete Audio Tokenization
- [去噪网络与解掩顺序共同训练](../conferences/icml-2026/cards/1501-1600.md#hong26f-architecture) · Unifying Masked Diffusion Models with Various Generation Orders and Beyond
- [按符号建共享流使改名可交换](../conferences/icml-2026/cards/1801-1900.md#isik26a-architecture) · Names Don’t Matter: Symbol-Invariant Transformer for Open-Vocabulary Learning
- [用声学原型和快慢反馈落实复合语音指令](../conferences/icml-2026/cards/2001-2100.md#kang26p-architecture) · AgentSteerTTS: A Multi-Agent Closed-Loop Framework for Composite-Instruction Text-to-Speech

<a id="by-reinforcement-learning"></a>

### 强化学习

- [连续控制动作表示](../conferences/icml-2026/cards/0201-0300.md#bian26a-architecture) · RN-D: Discretized Categorical Actors for On-Policy Reinforcement Learning
- [以潜状态分布替代像素重构并允许替换约束先验](../conferences/icml-2026/cards/1701-1800.md#huang26ba-architecture) · VJEPA: Variational Joint Embedding Predictive Architectures as Probabilistic World Models
- [用输入门在固定参考路径和可学投影间插值](../conferences/icml-2026/cards/2101-2200.md#koeppe26a-architecture) · Mitigating Plasticity Loss through Architectural Design in Continual Learning
- [把可梯度训练的连续策略编译成查表电路](../conferences/icml-2026/cards/2201-2300.md#kresse26a-architecture) · Differentiable Weightless Controllers: Learning Logic Circuits for Continuous Control
- [离线控制中的目标可达性](../conferences/icml-2026/cards/2301-2400.md#lei26g-architecture) · QHyer: Q-conditioned Hybrid Attention-mamba Transformer for Offline Goal-conditioned RL
- [连续控制演员评论家专家扩展](../conferences/icml-2026/cards/3101-3200.md#ma26an-architecture) · ScaleMoE: Mixture-of-Experts for Scalable Continuous Control in Actor-Critic Reinforcement Learning
- [路口共享策略动态路由](../conferences/icml-2026/cards/3101-3200.md#ma26az-architecture) · Scalable Traffic Signal Control with Shared Policy Framework
- [以状态原型解释连续控制策略](../conferences/icml-2026/cards/3201-3300.md#marzo26a-architecture) · This State Looks Like That: Self-Interpretable Reinforcement Learning Agents using Prototype Soft Actor-Critic

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
- [在驾驶仿真中按需补绘车道与交通参与者](../conferences/icml-2026/cards/1901-2000.md#jiang26bf-architecture) · VectorWorld: Efficient Streaming World Model via Diffusion Flow on Vector Graphs
- [由状态哨兵按需触发推理与纠错](../conferences/icml-2026/cards/2501-2600.md#li26fm-architecture) · Sentinel-VLA: A Metacognitive VLA Model with Active Status Monitoring for Dynamic Reasoning and Error Recovery
- [用独立条件路径和插拔触觉适配器驱动双臂](../conferences/icml-2026/cards/2501-2600.md#li26fs-architecture) · DECO: Decoupled Multimodal Diffusion Transformer for Bimanual Dexterous Manipulation with a Plugin Tactile Adapter
- [以稀疏三维子目标规划动作](../conferences/icml-2026/cards/2601-2700.md#li26hk-architecture) · Structured 4D Latent Predictive Model for Robot Planning
- [用轻量时序三维流把慢规划接入快控制](../conferences/icml-2026/cards/2701-2800.md#lin26g-architecture) · RoboFlow4D: A Lightweight Flow World Model Toward Real-Time Flow-Guided Robotic Manipulation
- [长时机器人动作的连续粗到细生成](../conferences/icml-2026/cards/2701-2800.md#lin26ab-architecture) · MSP: Probabilistically Consistent Multi-Scale Action Generation
- [稀疏三维路点与可复用动作专家](../conferences/icml-2026/cards/2801-2900.md#liu26bf-architecture) · GAE: Unleashing Physical Potential of VLM with Generalizable Action Expert
- [用低频潜在时空推理支持高频机器人控制](../conferences/icml-2026/cards/2801-2900.md#liu26ch-architecture) · LaST$_0$: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model
- [观察条件作为动作扩散桥端点](../conferences/icml-2026/cards/2801-2900.md#liu26db-architecture) · Sample from What You See: Visuomotor Policy Learning via Diffusion Bridge with Observation-Embedded Stochastic Differential Equation
- [用可微连续时间函数表示机器人动作块](../conferences/icml-2026/cards/2901-3000.md#liu26gf-architecture) · Neural Implicit Action Fields: From Discrete Waypoints to Continuous Functions for Vision-Language-Action Models
- [无投影多面体流匹配](../conferences/icml-2026/cards/3101-3200.md#ma26ar-architecture) · PolyFlow: Safe and Efficient Polytope-Constrained Flow Matching with Constraint Embedding and Projection-free Update

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
- [把 GUI 历史动作和跨任务经验分层检索](../conferences/icml-2026/cards/1901-2000.md#jin26m-architecture) · SE-GA: Memory-Augmented Self-Evolution for GUI Agents
- [让移动界面模型输出可渲染代码来预测下一屏](../conferences/icml-2026/cards/2101-2200.md#koh26a-architecture) · Generative Visual Code Mobile World Models
- [多变量时序与文本的交错建模](../conferences/icml-2026/cards/2201-2300.md#langer26a-architecture) · OpenTSLM: Time-Series Language Models for Reasoning over Multivariate Medical Text- and Time-Series Data
- [在低频语音潜变量上分层补回波形](../conferences/icml-2026/cards/2301-2400.md#lee26f-architecture) · ReGen: Hierarchical Multi-Prompt Representation Generation for Efficient Waveform Diffusion Models
- [全景空间音频流式生成](../conferences/icml-2026/cards/2301-2400.md#lei26i-architecture) · Towards Streaming Synchronized Spatial Audio Generation via Autoregressive Diffusion Transformer
- [以主体身份查询把视频词元稀疏路由给对应参照](../conferences/icml-2026/cards/2501-2600.md#li26df-architecture) · DiasR: Dual-Modal Identity-Anchored Sparse Routing for Efficient Multi-Subject Video Generation
- [跨模态离散掩码的联合生成](../conferences/icml-2026/cards/2501-2600.md#li26dv-architecture) · Omni-Diffusion: Unified Multimodal Understanding and Generation with Masked Discrete Diffusion
- [为脉冲多模态网络拆开时序与注意力设计](../conferences/icml-2026/cards/2601-2700.md#liang26i-architecture) · SMM Transformer: Leveraging Spiking Neural Networks for Multimodal Tasks
- [用空频门预测缺失传感器特征](../conferences/icml-2026/cards/2601-2700.md#liang26k-architecture) · AnyMod-LLVE: Low-Light Video Enhancement with Modality-Agnostic Inference
- [分别用文本与历史数列路由预测专家](../conferences/icml-2026/cards/2701-2800.md#lin26al-architecture) · TiMi: Empower Time Series Transformers with Multimodal Mixture of Experts
- [从高层注入绕过语义压缩的取证特征](../conferences/icml-2026/cards/2701-2800.md#lin26an-architecture) · Deep Residual Injection for Full-Spectrum Forensic Signal Perception in Multimodal Large Language Models
- [让模型在二维线索不足时主动调用几何通道](../conferences/icml-2026/cards/2801-2900.md#liu26as-architecture) · GeoSense: Internalizing Geometric Necessity Perception for Multimodal Reasoning
- [联合 RGB-D 和神经声强向量定位三维声源](../conferences/icml-2026/cards/2901-3000.md#liu26ea-architecture) · JAEGER: Joint 3D Audio-Visual Grounding and Reasoning in Simulated Physical Environments
- [移动界面阶段专家](../conferences/icml-2026/cards/2901-3000.md#liu26fc-architecture) · CoME: Empowering Channel-of-Mobile-Experts with Informative Hybrid-Capabilities Reasoning
- [语音和文本的分组加共享专家路由](../conferences/icml-2026/cards/2901-3000.md#lou26h-architecture) · MoST: Mixing Speech and Text with Modality-Aware Mixture of Experts
- [文本控制音乐修复与母带](../conferences/icml-2026/cards/3201-3300.md#melechovsky26a-architecture) · SonicMaster: Towards Controllable All-in-One Music Restoration and Mastering
- [跨模态消息门控](../conferences/icml-2026/cards/3201-3300.md#meng26a-architecture) · Group Cognition Learning: Making Everything Better Through Governed Two-Stage Agents Collaboration
- [按实际效用维护可组合的界面操作记忆](../conferences/icml-2026/cards/3201-3300.md#mi26b-architecture) · Darwinian Memory: A Training-Free Self-Regulating Memory System for GUI Agent Evolution

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
- [让软斜树承担因果效应网络的特征路由](../conferences/icml-2026/cards/2001-2100.md#kano26a-architecture) · Gradient-Based Causal Tree Ensembles: A Backbone Architecture for Heterogeneous Treatment Effects
- [先限定对称族再学习可解释生成元](../conferences/icml-2026/cards/2001-2100.md#karjol26a-architecture) · Interpretable Discovery of One-parameter Subgroups: A Modular Framework for Elliptical, Hyperbolic, and Parabolic Symmetries
- [把对齐后的权重矩阵当可变尺寸局部场](../conferences/icml-2026/cards/2101-2200.md#kim26ay-architecture) · NNiT: Width-Agnostic Neural Network Generation with Structurally Aligned Weight Spaces
- [对一般线性共轭保留矩阵中心特征](../conferences/icml-2026/cards/2101-2200.md#kim26ca-architecture) · Equivariant Neural Networks for General Linear Symmetries on Lie Algebras
- [固定非零权重预算下扩宽网络](../conferences/icml-2026/cards/2101-2200.md#kong26f-architecture) · Expand Neurons, Not Parameters
- [用乘积节点和稀疏样本辨别奇偶支持](../conferences/icml-2026/cards/2201-2300.md#larue26a-architecture) · Learning High-Dimensional Parity Functions with Product Networks using Gradient Descent
- [用单个可学离散 Gaussian 核替换固定多尺度分支](../conferences/icml-2026/cards/2301-2400.md#lee26al-architecture) · Generalizing Multi-Scale Time-Series Modeling with a Single Operator
- [用不同分数奇异度的输入投影分工记忆远近信息](../conferences/icml-2026/cards/2401-2500.md#li26cx-architecture) · FRACTAL: State Space Model with Fractional Recurrent Architecture for Computational Temporal Analysis of Long Sequences
- [用共享矩阵多项式推广状态空间对偶](../conferences/icml-2026/cards/2501-2600.md#li26ft-architecture) · MIMOMamba: From Scalar Duality to Matrix-Valued Attention
- [将 KV 绑定测试时训练改写成线性注意力扫描](../conferences/icml-2026/cards/2801-2900.md#liu26ae-architecture) · Test-Time Training with KV Binding Is Secretly Linear Attention
- [先拆分时序成分再生成未来的动态相位](../conferences/icml-2026/cards/2801-2900.md#liu26dn-architecture) · PULSE: Generative Phase Evolution for Non-Stationary Time Series Forecasting
- [用少量普通 LIF 反馈回路提供长期记忆](../conferences/icml-2026/cards/2801-2900.md#liu26do-architecture) · LIF Recurrent Memory Enables Long-Horizon Spiking Computation
- [用行注意力与全局寄存器支持表格逐样本退出](../conferences/icml-2026/cards/2901-3000.md#liu26fm-architecture) · TabSwift: An Efficient Tabular Foundation Model with Row-Wise Attention
- [用可调平稳噪声核统一掩码与均匀扩散](../conferences/icml-2026/cards/2901-3000.md#liu26gi-architecture) · Balancing Understanding and Generation in Discrete Diffusion Models
- [逐段扩展直接时序预测](../conferences/icml-2026/cards/3001-3100.md#lu26w-architecture) · ReNF: Rethinking the Design of Neural Long-Term Time Series Forecasters
- [用独立特征嵌入与组 Lasso 强化表格轴归纳](../conferences/icml-2026/cards/3001-3100.md#lui26a-architecture) · LassoFlexNet: a Flexible Neural Architecture for Tabular Data
- [用 LUT 卷积与可学习分组连接构造无权重神经网络](../conferences/icml-2026/cards/3101-3200.md#ma26e-architecture) · Convolutional Learnable-Group Weightless Neural Network
- [不规则点集傅里叶卷积](../conferences/icml-2026/cards/3301-3400.md#mohseni26a-architecture) · Revisiting Neural Processes via Fourier Transform and Volterra Series
- [流式神经过程的因果缓存](../conferences/icml-2026/cards/3301-3400.md#mortimer26a-architecture) · Incremental Transformer Neural Processes

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
- [分开建模用户兴趣与可持续阈值](../conferences/icml-2026/cards/1901-2000.md#jin26d-architecture) · Eating for a Sustainable Planet: Personalized Sustainable Diet Recommendation via Constraint-Aware Decision-Making Modeling
- [先对齐局部坐标再扩散向量信号](../conferences/icml-2026/cards/1901-2000.md#johnson26a-architecture) · VDW-GNNs: Vector diffusion wavelets for geometric graph neural networks
- [在多尺度子图之图中路由曲率专家](../conferences/icml-2026/cards/2801-2900.md#liu26x-architecture) · Learning Graph Foundation Models on Riemannian Graph-of-Graphs
- [关系数据库状态空间模型](../conferences/icml-2026/cards/2901-3000.md#liu26ep-architecture) · Ramba: Selective State-Space Models for Relational Deep Learning
- [用全局调制 token 让扩散生成满足网络链路约束](../conferences/icml-2026/cards/3201-3300.md#marcoccia26a-architecture) · NetDiff: Graph Diffusion with Improved Global Capabilities to Generate and Update Mobile Network Topologies
- [在知识图查询执行合约中显式绑定否定范围](../conferences/icml-2026/cards/3201-3300.md#miao26e-architecture) · LLM-MatLogic: Executable Exchange Contracts for Knowledge-Graph Query Answering with Scoped Negation
- [动态图的结构频谱时序解耦](../conferences/icml-2026/cards/3301-3400.md#mo26a-architecture) · Entangled No More: Multi-Domain Decoupling for Robust Dynamic Graph Neural Networks

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
- [把短期功能动态和长期脑图融合](../conferences/icml-2026/cards/1901-2000.md#jiang26r-architecture) · ADHD Disease Detection Based on Short- and Long-Term Brain Function Encoding and Memory Graph Network
- [在相邻光刻工序的状态变化上学习干预](../conferences/icml-2026/cards/1901-2000.md#jiang26ae-architecture) · LithoDreamer: A Physics-Informed World Model for Multi-Stage Computational Lithography
- [用速度状态隔开时序位置与变化方向](../conferences/icml-2026/cards/1901-2000.md#jiang26au-architecture) · KineFlow: Kinematic Second-Order Flow Matching for Time-Series Forecasting
- [以 Wiener 可靠性调节宽域和细节时频视图](../conferences/icml-2026/cards/1901-2000.md#jin26g-architecture) · Robust Signal Enhancement via Fractional Detail Views and Knowledge Guided Multi-view Fusion
- [让分子流的目标分布逐步集中](../conferences/icml-2026/cards/1901-2000.md#jin26i-architecture) · EvoEGF-Mol: Evolving Exponential Geodesic Flow for Structure-based Drug Design
- [把晶体张量等变性放到笛卡尔基组装](../conferences/icml-2026/cards/1901-2000.md#jin26p-architecture) · Efficient Equivariant High-Order Crystal Tensor Prediction via Cartesian Local-Environment Many-Body Coupling
- [按全原子结构复杂度分配语言连接词元](../conferences/icml-2026/cards/1901-2000.md#jing26h-architecture) · Scaling-Aware Adapter for Structure-Grounded LLM Reasoning
- [用局部网格传播和全局注意共享物理算子](../conferences/icml-2026/cards/2001-2100.md#ju26a-architecture) · Adaptive Physics Transformer with Fused Global-Local Attention for Subsurface Energy Systems
- [用可分离谱因子解析计算高维物理残差](../conferences/icml-2026/cards/2001-2100.md#kaminsky26a-architecture) · Overcoming PINNs Failure Modes In High Dimension With Low-Rank Fourier Sum
- [将临床事件的时间与内容分别预训练](../conferences/icml-2026/cards/2001-2100.md#kang26a-architecture) · Time-Conditioned Foreseeing: An EHR-Specific Foundation Model for Irregular Dynamics and Calendrical Time
- [吸附体与催化表面联合生成](../conferences/icml-2026/cards/2101-2200.md#kim26z-architecture) · CatFlow: Co-generation of Slab-Adsorbate Systems via Flow Matching
- [直接评估哈密顿量误差向能量与力传播](../conferences/icml-2026/cards/2101-2200.md#kim26an-architecture) · Machine Learning Hamiltonians are Accurate Energy-Force Predictors
- [让傅里叶核在等半径频率上共享权重](../conferences/icml-2026/cards/2101-2200.md#kim26bp-architecture) · EqGINO: Equivariant Geometry-Informed Fourier Neural Operators for 3D PDEs
- [用连续卷积和频谱池化适配采样率](../conferences/icml-2026/cards/2201-2300.md#kumar26b-architecture) · NeurOCNN: A Neural-Operator-Based Model for Physiological Time Series
- [守恒 PDE 的容量约束累积输运](../conferences/icml-2026/cards/2201-2300.md#lan26c-architecture) · FluxNet: Learning Capacity-Constrained Local Transport Operators for Conservative and Bounded PDE Surrogates
- [用等算量固定边界隔离基因组动态分块的价值](../conferences/icml-2026/cards/2301-2400.md#ledneva26a-architecture) · LDARNet: DNA Adaptive Representation Network with Learnable Tokenization for Genomic Modeling
- [用跨层持久记忆检验脑信号参与解码](../conferences/icml-2026/cards/2301-2400.md#lee26v-architecture) · BIT-LLM: Brain Instruction Tuned LLM with persistent Cross-Attention for fMRI-to-Text Decoding
- [用李群前缀扫描并行合成长时演化](../conferences/icml-2026/cards/2301-2400.md#lee26aa-architecture) · Lie-Algebraic Acceleration of Neural Koopman Dynamics
- [用惯性坐标系把三维分子写成原子序列](../conferences/icml-2026/cards/2401-2500.md#li26am-architecture) · InertialAR: Autoregressive 3D Molecule Generation with Inertial Frames
- [PDE 算子的高斯模态投影](../conferences/icml-2026/cards/2401-2500.md#li26aq-architecture) · From Basis to Basis: Gaussian Particle Representation for Interpretable PDE Operators
- [在同一潜空间用稀疏场解 PDE 正向和反向问题](../conferences/icml-2026/cards/2501-2600.md#li26dk-architecture) · Di-BiLPS: Denoising induced Bidirectional Latent-PDE-Solver under Sparse Observations
- [在候选原子处查询冷冻电镜密度](../conferences/icml-2026/cards/2501-2600.md#li26eh-architecture) · CryoACE: An Atom-centric Framework for Accurate and Automated Model Building in Cryo-EM
- [用预训练 fMRI 解码器和状态提示重建脑活动](../conferences/icml-2026/cards/2501-2600.md#li26gp-architecture) · Mind the State: Towards Unified, Context-Aware EEG-to-fMRI Synthesis
- [以应力和内力为接口训练神经模拟器](../conferences/icml-2026/cards/2601-2700.md#li26ho-architecture) · Neural Modular Physics for Elastic Simulation
- [让 CAD 程序用文字查询锚定边界基元](../conferences/icml-2026/cards/2601-2700.md#li26jd-architecture) · Towards High-Fidelity CAD Generation via LLM-Driven Program Generation and Text-Based B-Rep Primitive Grounding
- [用共享锚点近似细胞全局注意力](../conferences/icml-2026/cards/2601-2700.md#liang26a-architecture) · Bipartite Graph Attention-based Clustering for Large-scale scRNA-seq Data
- [按判别频谱设定脉冲膜衰减](../conferences/icml-2026/cards/2701-2800.md#liao26e-architecture) · Frequency Matching in Spiking Neural Networks for mmWave Sensing
- [部分可观测世界模型的流等变记忆](../conferences/icml-2026/cards/2701-2800.md#lillemark26a-architecture) · Flow Equivariant World Models: Structured Memory for Dynamic Environments
- [神经 ODE 同时估计扰动轨迹和调控模块](../conferences/icml-2026/cards/2701-2800.md#lin26e-architecture) · Interpretable Neural ODEs for Gene Regulatory Network Discovery under Perturbations
- [蛋白质轨迹的分窗频谱生成](../conferences/icml-2026/cards/2701-2800.md#lin26x-architecture) · BioDynaSpec: Harmonic-Guided Spatio-Spectral Autoregressive Diffusion for Protein Dynamics Generation
- [把周期变量嵌入单位圆后累积精度](../conferences/icml-2026/cards/2701-2800.md#lin26ar-architecture) · Periodic Bayesian Flow Networks with Additive Accuracy
- [用粗粒度运动描述约束降水预报](../conferences/icml-2026/cards/2701-2800.md#ling26a-architecture) · LangPrecip: Language-Aware Multimodal Precipitation Nowcasting
- [以硬件连续动力学分担空间算子和时间积分](../conferences/icml-2026/cards/2701-2800.md#liu26s-architecture) · Solving Time-Dependent Differential Equations with Physical Dynamical Systems
- [用轮廓、前景和场景锚分层对齐脑电信号](../conferences/icml-2026/cards/2801-2900.md#liu26ap-architecture) · ViEEG: Hierarchical Visual Neural Representation for EEG Brain Decoding
- [几何张量的等变正定协方差](../conferences/icml-2026/cards/2801-2900.md#liu26bk-architecture) · Equivariant Covariance Tensors: Guaranteed SPD Uncertainty for Tensor-Valued Geometric Learning
- [按共享配体条件联合编码多个口袋](../conferences/icml-2026/cards/2801-2900.md#liu26ce-architecture) · Geometric Pocket-Centric Protein Encoding for Polypharmacology-Guided Multi-Target Drug Design
- [非平稳交通时空预测](../conferences/icml-2026/cards/2901-3000.md#liu26er-architecture) · Decoupling Universal Laws and Environmental Heterogeneity: A Physics-Inspired Framework for Robust Spatio-Temporal Forecasting
- [心电到毫米波雷达合成](../conferences/icml-2026/cards/2901-3000.md#liu26ey-architecture) · Cardio-mmFlow: A Gaussian-Prior-Free Physics-Informed Flow Matching Framework for Electrocardiogram to mmWave Radar Synthesis
- [由所有非配对点云快照共同初始化连续轨迹](../conferences/icml-2026/cards/2901-3000.md#liu26fl-architecture) · FlowCloud: Learning Continuous Spatiotemporal Dynamics from Unpaired Sparse Point Cloud Snapshots
- [用多尺度切片和频谱指纹预测陌生混沌系统](../conferences/icml-2026/cards/2901-3000.md#liu26gg-architecture) · ChaosNexus: A Foundation Model for ODE-based Chaotic System Forecasting with Hierarchical Multi-scale Awareness
- [将序列局部模体、频域模式与显著度分开适配](../conferences/icml-2026/cards/2901-3000.md#liu26gj-architecture) · Adaptive DNA Sequence Modeling via Synergistic Plasticity Units
- [细胞分子监督与病理多尺度证据](../conferences/icml-2026/cards/2901-3000.md#lou26d-architecture) · Cello: A Universal Cell-wise Feature Aggregation framework for Reliable Pathology Images Analysis
- [用目标掩码切换脑图文编解码任务](../conferences/icml-2026/cards/3001-3100.md#lu26d-architecture) · Mind-Omni: A Unified Multi-Task Framework for Brain-Vision-Language Modeling via Discrete Diffusion
- [函数 Koopman 记忆闭合](../conferences/icml-2026/cards/3001-3100.md#lu26u-architecture) · Interpretable Functional Koopman Learning with Non-Markovian Closure for Spatiotemporal Systems
- [在数据空间预测干净雷达图并用弱平流稳住降水输运](../conferences/icml-2026/cards/3001-3100.md#luo26l-architecture) · Physically-Guided Data-Space Rectified Flow for Precipitation Nowcasting
- [可追溯病灶概念的多视角分级](../conferences/icml-2026/cards/3001-3100.md#luo26ac-architecture) · ProConMV: Provenance-Enabled Conceptual Framework for Interpretable Multi-View Diabetic Retinopathy Diagnosis
- [跨领域连续动力学的共享体素与网格抖动](../conferences/icml-2026/cards/3201-3300.md#mccabe26a-architecture) · Walrus: A Cross-domain Foundation Model for Continuum Dynamics
- [用表型条件化脑图的多跳路由](../conferences/icml-2026/cards/3201-3300.md#meng26f-architecture) · PhenoBrain: Phenotype-Conditioned Long-Range Communication for Multi-Modal Brain Network Analysis
- [显式控制深层 PINN 的输入雅可比](../conferences/icml-2026/cards/3201-3300.md#meng26i-architecture) · Deep Coupling Learning for Solving PDEs
- [按近端分裂连接物理与神经求解块](../conferences/icml-2026/cards/3201-3300.md#mezidi26a-architecture) · Proximal Splitting Methods for Hybrid Differentiable Models
- [用对称耦合放大电池早期微弱退化差异](../conferences/icml-2026/cards/3201-3300.md#miao26d-architecture) · DITING: A Weak Degradation Listener for Battery Lifetime Early Prediction
<!-- classification:end -->
