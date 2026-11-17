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

### 计算机视觉

- [视频分词](../papers/computer-vision.md#atanov26a-architecture) · VideoFlexTok: Flexible-Length Coarse-to-Fine Video Tokenization
- [像素空间扩散](../papers/computer-vision.md#baade26a-architecture) · Latent Forcing: Reordering the Diffusion Trajectory for Pixel-Space Image Generation
- [少样本布局生成](../papers/computer-vision.md#bao26f-architecture) · Envisioning Beyond the Few: Disentangled Semantics and Primitives for Few-Shot Atypical Layout-to-Image Generation
- [按空间分组的同位词元预测](../papers/computer-vision.md#chen26du-architecture) · Autoregression with Self-Token Prediction
- [压缩成像的连续光谱先验](../papers/computer-vision.md#chen26ga-architecture) · Phy-CoSF: Physics-Guided Continuous Spectral Fields Reconstruction and Spectral Super-Resolution for Snapshot Compressive Imaging

### 强化学习

- [连续控制动作表示](../papers/reinforcement-learning.md#bian26a-architecture) · RN-D: Discretized Categorical Actors for On-Policy Reinforcement Learning

### 机器人学

- [VLA 潜空间推理](../papers/robotics.md#bai26h-architecture) · Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models
- [频域分层动作策略](../papers/robotics.md#cao26u-architecture) · Hierarchical Policy Learning via Spectral Decomposition

### 多模态学习

- [交互式人物检索](../papers/multimodal.md#bai26j-architecture) · Interactive Person Retrieval via Multi-Turn Multimodal Conversation
- [遥感跨模态的共享潜空间扩散](../papers/multimodal.md#chen26go-architecture) · Any2Any: Unified Arbitrary Modality Translation for Remote Sensing

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

### 图学习与推荐

- [知识图谱多跳问答](../papers/graph-and-recommendation.md#bandyopadhyay26a-architecture) · RSF-GLLM: Bridging the Semantic Gap in Multi-Hop Knowledge Graph QA via Recurrent Soft-Flow and Decoupled LLM Generation
- [生成式电商检索](../papers/graph-and-recommendation.md#chen26al-architecture) · OneSearch: A Preliminary Exploration of the Unified End-to-End Generative Framework for E-commerce Search

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
<!-- classification:end -->
