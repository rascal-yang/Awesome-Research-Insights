# 模型架构

[首页](../README.md) · [参与贡献](../CONTRIBUTING.md) · [English](../en/insights/architecture.md)

整体架构与信息流。

<!-- classification:start -->
## 按研究领域浏览

### 大语言模型

- [离散扩散解码](../papers/llm.md#arriola26a-architecture) · Set Diffusion: Interpolating Token Orderings between Autoregression and Diffusion for Fast and Flexible Decoding
- [长任务 Agent 协作](../papers/llm.md#bui26b-architecture) · HiMAP-Travel: Hierarchical Multi-Agent Planning for Long-Horizon Constrained Travel
- [科研 Agent 搜索](../papers/llm.md#chen26r-architecture) · MARS: Modular Agent with Reflective Search for Automated AI Research
- [局部注意力与参数化记忆](../papers/llm.md#chen26cg-architecture) · LoKiFormer: Locality-aware Attention with Decoupled Knowledge Memory for Efficient Large Language Model Pretraining
- [混合专家的按头并行](../papers/llm.md#cui26c-architecture) · Multi-Head LatentMoE and Head Parallel: Communication-Efficient and Deterministic MoE Parallelism
- [预测分块上下文辅助逐词解码](../papers/llm.md#dai26g-architecture) · Context-level Language Modeling by Learning Predictive Context Embeddings
- [长上下文的块级混合注意力](../papers/llm.md#deng26v-architecture) · Neural Attention Search Linear: Towards Adaptive Token-Level Hybrid Attention Models
- [低维潜空间专家计算](../papers/llm.md#elango26a-architecture) · Revisiting Efficiency–Accuracy Scaling in Mixture-of-Experts Architectures
- [可结构化高阶递推的词元混合](../papers/llm.md#fagnou26a-architecture) · Trading Complexity for Expressivity Through Structured Generalized Linear Token Mixing
- [窗口注意力与递归长时记忆](../papers/llm.md#fang26w-architecture) · Artificial Hippocampus Networks for Efficient Long-Context Modeling
- [仅对困难词元启动隐空间迭代](../papers/llm.md#fu26t-architecture) · Think-at-Hard: Dynamic Looped Transformers for Improved Reasoning
- [频域乘法实现因果序列混合](../papers/llm.md#gan26c-architecture) · Caracal: Causal Architecture via Spectral Mixing

### 计算机视觉

- [视频分词](../papers/computer-vision.md#atanov26a-architecture) · VideoFlexTok: Flexible-Length Coarse-to-Fine Video Tokenization
- [像素空间扩散](../papers/computer-vision.md#baade26a-architecture) · Latent Forcing: Reordering the Diffusion Trajectory for Pixel-Space Image Generation
- [少样本布局生成](../papers/computer-vision.md#bao26f-architecture) · Envisioning Beyond the Few: Disentangled Semantics and Primitives for Few-Shot Atypical Layout-to-Image Generation
- [按空间分组的同位词元预测](../papers/computer-vision.md#chen26du-architecture) · Autoregression with Self-Token Prediction
- [压缩成像的连续光谱先验](../papers/computer-vision.md#chen26ga-architecture) · Phy-CoSF: Physics-Guided Continuous Spectral Fields Reconstruction and Spectral Super-Resolution for Snapshot Compressive Imaging
- [开放词汇三维实例分割](../papers/computer-vision.md#choy26a-architecture) · SpaCeFormer: Fast Proposal-Free Open-Vocabulary 3D Instance Segmentation
- [原生四维体素自编码](../papers/computer-vision.md#ding26u-architecture) · Native Spatio-Temporal 4D Variational Autoencoder
- [照片结构重构的动作条件编辑](../papers/computer-vision.md#du26c-architecture) · AesFormer: Transform Everyday Photos into Beautiful Memories
- [病理去焦模糊的局部积分算子](../papers/computer-vision.md#duan26e-architecture) · Discontinuous Galerkin Neural Operator for Pathology Defocus Deblurring
- [单步伪装物体掩码预测](../papers/computer-vision.md#fu26l-architecture) · CODiff: One-Step Diffusion Model for Camouflaged Object Detection
- [按类别难度隔离位姿学习梯度](../papers/computer-vision.md#gao26aq-architecture) · DecomPose: Disentangling Cross-Category Optimization Contention for Category-Level 6D Object Pose Estimation
- [持久三维状态的交互视频世界模型](../papers/computer-vision.md#garcin26a-architecture) · Beyond Pixel Histories: World Models with Persistent 3D State
- [姿态可控插入的三路视觉条件](../papers/computer-vision.md#gong26f-architecture) · Direct 3D-Aware Object Insertion via Decomposed Visual Proxies

### 自然语言处理

- [文本编码与掩码重建解耦](../papers/nlp.md#dervishi26a-architecture) · Separating Representation from Reconstruction Enables Scalable Text Encoders
- [纯因果 Transformer 的音频分词](../papers/nlp.md#gong26c-architecture) · Scaling Transformers for End-to-End Discrete Audio Tokenization

### 强化学习

- [连续控制动作表示](../papers/reinforcement-learning.md#bian26a-architecture) · RN-D: Discretized Categorical Actors for On-Policy Reinforcement Learning

### 机器人学

- [VLA 潜空间推理](../papers/robotics.md#bai26h-architecture) · Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models
- [频域分层动作策略](../papers/robotics.md#cao26u-architecture) · Hierarchical Policy Learning via Spectral Decomposition
- [SE(3) 位姿扩散策略](../papers/robotics.md#chuang26a-architecture) · The Lie We Tell: Correcting the Euclidean Fallacy in Vision Language Action Policies via Score Matching on Tangent Space
- [第一视角三维检测的时序记忆](../papers/robotics.md#ding26x-architecture) · Embodied-DETR: End-to-End Temporal 3D Object Detection in Egocentric Views

### 多模态学习

- [交互式人物检索](../papers/multimodal.md#bai26j-architecture) · Interactive Person Retrieval via Multi-Turn Multimodal Conversation
- [遥感跨模态的共享潜空间扩散](../papers/multimodal.md#chen26go-architecture) · Any2Any: Unified Arbitrary Modality Translation for Remote Sensing
- [阵列几何条件化的空间音频词元](../papers/multimodal.md#dementyev26a-architecture) · PhaseCoder: Microphone Geometry-Agnostic Spatial Audio Understanding for Multimodal LLMs
- [持续学习专家的置信加权协作](../papers/multimodal.md#forhad26a-architecture) · Mixing Expertise with Confidence: A Mixture of Experts Framework for Robust Multi-Modal Continual Learning
- [交替状态与转移的视觉世界模型](../papers/multimodal.md#gao26am-architecture) · DynaVieW: Schema-Guided World Modeling for Understanding Hierarchical Visual Dynamics

### 机器学习基础与统计

- [脉冲状态空间模型](../papers/ml-foundations.md#agrawal26c-architecture) · A Spiking Heterogeneous Harmonic Resonate-and-Fire State Space Model for Time Series
- [可解释风险排序](../papers/ml-foundations.md#babbar26a-architecture) · Falling Trees: A Model Class for Interpretable Risk Prioritization
- [世界模型](../papers/ml-foundations.md#baek26b-architecture) · Learning to Theorize the World from Observation
- [可线性化网络](../papers/ml-foundations.md#berman26c-architecture) · Who Said Neural Networks Aren’t Linear?
- [非高斯扩散](../papers/ml-foundations.md#bertholom26a-architecture) · M-Star: Markovian Projection of Star-Shaped Diffusion for Exponential Family Distributions
- [离散函数近似](../papers/ml-foundations.md#candogan26b-architecture) · Deep Flow Networks
- [受约束域回归](../papers/ml-foundations.md#chakraborty26a-architecture) · Probabilistically-routed Bayesian Additive Spanning Trees for Learning on Constrained Domains
- [时序计数分解](../papers/ml-foundations.md#chaussard26a-architecture) · Independent Component Discovery in Temporal Count Data
- [自回归与流匹配耦合预测](../papers/ml-foundations.md#cheng26h-architecture) · CoGenCast: A Coupled Autoregressive–Flow Generative Framework for Time Series Forecasting
- [外生时序的历史条件生成](../papers/ml-foundations.md#cheng26t-architecture) · KITE: Knowledge-Guided Probabilistic Modeling for Time Series Forecasting with Exogenous Variables
- [用 Transformer 电路实现 Lloyd 迭代](../papers/ml-foundations.md#clarkson26a-architecture) · Transformer Circuits Can Realize Clustering Algorithms
- [混合专家式概念瓶颈](../papers/ml-foundations.md#de-santis26a-architecture) · Mixture of Concept Bottleneck Experts
- [联邦学习的弹性共享专家](../papers/ml-foundations.md#du26d-architecture) · FedEMoE: Improving Personalization on Heterogeneous Federated Learning via Elastic Mixture of Experts Architecture
- [带长历史压缩的时序插补](../papers/ml-foundations.md#fan26h-architecture) · Rethinking Time-Series Imputation as Conditional Inference along Temporal Evolution
- [跨尺度共享的递归状态空间模型](../papers/ml-foundations.md#fang26p-architecture) · Dynamic Fractal Mamba: A Neural Renormalization Group Flow for Scale-Invariant Sequence Modeling
- [符号置换等变的循环推理](../papers/ml-foundations.md#freinschlag26a-architecture) · Symbol-Equivariant Recurrent Reasoning Models
- [可解析径向归一化流](../papers/ml-foundations.md#gerdes26a-architecture) · Analytic Bijections for Smooth and Interpretable Normalizing Flows
- [时序预测的可调连续时间基](../papers/ml-foundations.md#graf26a-architecture) · FlowState: Sampling-Rate-Equivariant Time-Series Forecasting

### 图学习与推荐

- [知识图谱多跳问答](../papers/graph-and-recommendation.md#bandyopadhyay26a-architecture) · RSF-GLLM: Bridging the Semantic Gap in Multi-Hop Knowledge Graph QA via Recurrent Soft-Flow and Decoupled LLM Generation
- [生成式电商检索](../papers/graph-and-recommendation.md#chen26al-architecture) · OneSearch: A Preliminary Exploration of the Unified End-to-End Generative Framework for E-commerce Search
- [动态图的可学习信息耗散](../papers/graph-and-recommendation.md#de-castelli26a-architecture) · Adaptive Memory Retention in Dynamic Graphs
- [图动力学的能量与切向流](../papers/graph-and-recommendation.md#eliasof26a-architecture) · Graph Neural Dynamics via Learned Energy and Tangential Flows
- [超边潜类型与多通道传播](../papers/graph-and-recommendation.md#fang26g-architecture) · MC-HNN: Learning Latent Structural Semantics and High-Rank Representations for Hypergraph Neural Networks
- [图傅里叶变换的柯西分解](../papers/graph-and-recommendation.md#fernandez26a-architecture) · L2G-NET: Local to Global Spectral Graph Neural Networks via Cauchy Factorizations
- [超图生成的多尺度展开](../papers/graph-and-recommendation.md#gailhard26a-architecture) · Feature-Aware (Hyper)graph Generation via Next-Scale Prediction
- [以分层极大团表示超边](../papers/graph-and-recommendation.md#gantes26a-architecture) · SuperHype: Hypergraph Generation via Graph-Superposition Decomposition

### 科学机器学习

- [物理约束学习](../papers/scientific-ml.md#abijuru26a-architecture) · Physics-Informed Residual Flows
- [时空预测](../papers/scientific-ml.md#ai26f-architecture) · Nested Spatio-Temporal Time Series Forecasting
- [单细胞反事实编辑](../papers/scientific-ml.md#andersson26a-architecture) · scCBGM: Single-Cell Editing via Concept Bottlenecks
- [量子生成先验](../papers/scientific-ml.md#bacarreza26a-architecture) · Quantum latent distributions in deep generative models
- [单细胞时间建模](../papers/scientific-ml.md#balik26a-architecture) · Modeling Temporal scRNA-seq Data with Latent Gaussian Process and Optimal Transport
- [多保真数据同化](../papers/scientific-ml.md#bao26d-architecture) · Cheap2Rich: A Multi-Fidelity Framework for Data Assimilation and System Identification of Multiscale Physics - Rotating Detonation Engines
- [固体力学代理模型](../papers/scientific-ml.md#bazzi26a-architecture) · Physics-Informed Coarsening for Multigrid Graph Neural Surrogates
- [随机动力学生成](../papers/scientific-ml.md#berman26b-architecture) · Stochastic Lifting for Generating Trajectories of Stochastic Physical Systems
- [连续时间动力学](../papers/scientific-ml.md#brandle26a-architecture) · Continuous-Time Piecewise-Linear Recurrent Neural Networks
- [几何轨迹生成](../papers/scientific-ml.md#brinke26a-architecture) · STFlow: Data-Coupled Flow Matching for Geometric Trajectory Simulation
- [无线传播建模](../papers/scientific-ml.md#bu26d-architecture) · Stochastic Neural Ray Tracing for Radio Frequency Channel Modeling
- [实验室布局生成](../papers/scientific-ml.md#cao26ad-architecture) · LabBuilder: Protocol-Grounded 3D Layout Generation for Interactable and Safe Laboratory
- [生物声学定位](../papers/scientific-ml.md#chasmai26b-architecture) · Bioacoustic Geolocation: Species Sounds as Geographic Signals
- [对流风暴短时预报](../papers/scientific-ml.md#chen26aa-architecture) · StormInsight: Hierarchical Environmental Forcing and Vertical Coupling for Convective Systems Evolution
- [电子密度条件分子生成](../papers/scientific-ml.md#chen26ai-architecture) · From Holo Pockets to Electron Density: GPT-style Drug Design with Density
- [功能条件蛋白质共生成](../papers/scientific-ml.md#chen26cu-architecture) · Co-Generative De Novo Functional Protein Design
- [基因组性状到土壤碳动力学](../papers/scientific-ml.md#collart26a-architecture) · Constrained hybrid modelling to predict microbial dynamics and organic matter turnover in soil systems
- [分子构象与合成路线的联合潜空间](../papers/scientific-ml.md#cretu26a-architecture) · SynLaD: Latent Diffusion for Generating Synthesizable Molecules Conditioned on 3D Pharmacophore Profiles
- [机械属性场的自适应稀疏体素](../papers/scientific-ml.md#dagli26a-architecture) · Adaptive Volumetric Mechanical Property Fields Invariant to Resolution
- [时间驱动空间网络参数](../papers/scientific-ml.md#dai26a-architecture) · TINNs: Time-Induced Neural Networks for Solving Time-Dependent PDEs
- [工况条件下的分层图流匹配](../papers/scientific-ml.md#deng26c-architecture) · Condition-Aware Graph Flow Matching for Modeling the Distributions of Complex Fluid Systems
- [周期晶体电荷密度的傅里叶重建](../papers/scientific-ml.md#elsborg26a-architecture) · Global Plane Waves from Local Gaussians: Periodic Charge Densities in a Blink
- [生物序列模型的异构架构搜索](../papers/scientific-ml.md#fang26u-architecture) · BIOARC: Discovering Optimal Neural Architectures for Biological Foundation Models
- [脑电潜事件的电生理先验](../papers/scientific-ml.md#feng26b-architecture) · LERD: Latent Event-Relational Dynamics for Neurodegenerative Classification
- [辛降维的 Hamilton 动力学](../papers/scientific-ml.md#friedl26a-architecture) · Learning Hamiltonian Dynamics at Scale: A Differential-Geometric Approach
- [飞行器拓扑与连续参数的层级扩散](../papers/scientific-ml.md#ghiglino26a-architecture) · "Do Diffusion Models Dream of Electric Planes?" Discrete and Continuous Simulation-Based Inference for Aircraft Design
<!-- classification:end -->
