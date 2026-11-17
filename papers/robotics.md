# 机器人学

[首页](../README.md) · [参与贡献](../CONTRIBUTING.md) · [English](../en/papers/robotics.md)

机器人感知、策略学习、规划与控制。

<!-- classification:start -->
## 按技术类型浏览

[模型架构](#by-architecture) · [模块](#by-modules) · [损失函数](#by-loss-functions) · [优化](#by-optimization) · [强化学习方法](#by-reinforcement-learning) · [训练策略](#by-training-strategies) · [数据策略](#by-data-strategies) · [推理策略](#by-inference) · [表征学习](#by-representation-learning) · [评测与诊断](#by-evaluation) · [理论与统计](#by-theory-statistics)

<a id="by-architecture"></a>

### 模型架构

- <a id="bai26h-architecture"></a>[Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models](../conferences/icml-2026/cards/0101-0200.md#paper-bai26h)
- <a id="cao26u-architecture"></a>[Hierarchical Policy Learning via Spectral Decomposition](../conferences/icml-2026/cards/0401-0500.md#paper-cao26u)
- <a id="chuang26a-architecture"></a>[The Lie We Tell: Correcting the Euclidean Fallacy in Vision Language Action Policies via Score Matching on Tangent Space](../conferences/icml-2026/cards/0701-0800.md#paper-chuang26a)
- <a id="ding26x-architecture"></a>[Embodied-DETR: End-to-End Temporal 3D Object Detection in Egocentric Views](../conferences/icml-2026/cards/0901-1000.md#paper-ding26x)
- <a id="hu26ad-architecture"></a>[From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model](../conferences/icml-2026/cards/1601-1700.md#paper-hu26ad)
- <a id="huang26bh-architecture"></a>[SoMA: A Real-to-Sim Neural Simulator for Robotic Soft-Body Manipulation](../conferences/icml-2026/cards/1701-1800.md#paper-huang26bh)
- <a id="huang26cb-architecture"></a>[AutoMoT: A Unified Vision-Language-Action Model with Asynchronous Mixture -of-Transformers for End-to-End Autonomous Driving](../conferences/icml-2026/cards/1701-1800.md#paper-huang26cb)
- <a id="ji26k-architecture"></a>[HiMe: Hierarchical Embodied Memory for Long-Horizon Vision-Language-Action Control](../conferences/icml-2026/cards/1801-1900.md#paper-ji26k)
- <a id="jia26f-architecture"></a>[DriveWorld-VLA: Unified Latent-Space World Modeling with Vision–Language–Action for Autonomous Driving](../conferences/icml-2026/cards/1801-1900.md#paper-jia26f)
- <a id="jiang26bf-architecture"></a>[VectorWorld: Efficient Streaming World Model via Diffusion Flow on Vector Graphs](../conferences/icml-2026/cards/1901-2000.md#paper-jiang26bf)
- <a id="li26fm-architecture"></a>[Sentinel-VLA: A Metacognitive VLA Model with Active Status Monitoring for Dynamic Reasoning and Error Recovery](../conferences/icml-2026/cards/2501-2600.md#paper-li26fm)
- <a id="li26fs-architecture"></a>[DECO: Decoupled Multimodal Diffusion Transformer for Bimanual Dexterous Manipulation with a Plugin Tactile Adapter](../conferences/icml-2026/cards/2501-2600.md#paper-li26fs)
- <a id="li26hk-architecture"></a>[Structured 4D Latent Predictive Model for Robot Planning](../conferences/icml-2026/cards/2601-2700.md#paper-li26hk)
- <a id="lin26g-architecture"></a>[RoboFlow4D: A Lightweight Flow World Model Toward Real-Time Flow-Guided Robotic Manipulation](../conferences/icml-2026/cards/2701-2800.md#paper-lin26g)
- <a id="lin26ab-architecture"></a>[MSP: Probabilistically Consistent Multi-Scale Action Generation](../conferences/icml-2026/cards/2701-2800.md#paper-lin26ab)
- <a id="liu26bf-architecture"></a>[GAE: Unleashing Physical Potential of VLM with Generalizable Action Expert](../conferences/icml-2026/cards/2801-2900.md#paper-liu26bf)
- <a id="liu26ch-architecture"></a>[LaST$_0$: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model](../conferences/icml-2026/cards/2801-2900.md#paper-liu26ch)
- <a id="liu26db-architecture"></a>[Sample from What You See: Visuomotor Policy Learning via Diffusion Bridge with Observation-Embedded Stochastic Differential Equation](../conferences/icml-2026/cards/2801-2900.md#paper-liu26db)
- <a id="liu26gf-architecture"></a>[Neural Implicit Action Fields: From Discrete Waypoints to Continuous Functions for Vision-Language-Action Models](../conferences/icml-2026/cards/2901-3000.md#paper-liu26gf)
- <a id="ma26ar-architecture"></a>[PolyFlow: Safe and Efficient Polytope-Constrained Flow Matching with Constraint Embedding and Projection-free Update](../conferences/icml-2026/cards/3101-3200.md#paper-ma26ar)
- <a id="shang26f-architecture"></a>[DynVLA: Learning World Dynamics for Action Reasoning in Autonomous Driving](../conferences/icml-2026/cards/4001-4100.md#paper-shang26f)

<a id="by-modules"></a>

### 模块

- <a id="feng26x-modules"></a>[See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model](../conferences/icml-2026/cards/1101-1200.md#paper-feng26x)
- <a id="fu26x-modules"></a>[StableVLA: Towards Robust Vision-Language-Action Models without Extra Data](../conferences/icml-2026/cards/1101-1200.md#paper-fu26x)
- <a id="gyenes26a-modules"></a>[Fourier Features Let Agents Learn High Precision Policies with Imitation Learning](../conferences/icml-2026/cards/1401-1500.md#paper-gyenes26a)
- <a id="jang26c-modules"></a>[RA-VLA: Retrieval-Augmented VLA for Test-Time Adaptation](../conferences/icml-2026/cards/1801-1900.md#paper-jang26c)
- <a id="jing26f-modules"></a>[Mixture of Horizons in Action Chunking](../conferences/icml-2026/cards/1901-2000.md#paper-jing26f)
- <a id="li26ay-modules"></a>[Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action](../conferences/icml-2026/cards/2401-2500.md#paper-li26ay)

<a id="by-loss-functions"></a><a id="vision-language-action-models"></a>

### 损失函数

- <a id="amad26a-loss-functions"></a>[DT²: Decision-Targeted Digital Twins](../conferences/icml-2026/cards/0001-0100.md#paper-amad26a)
- <a id="fang26h-loss-functions"></a>[OMP: One-step Meanflow Policy with Directional Alignment](../conferences/icml-2026/cards/1001-1100.md#paper-fang26h)
- <a id="kim26ao-loss-functions"></a>[Contrastive Representation Regularization for Vision-Language-Action Models](../conferences/icml-2026/cards/2101-2200.md#paper-kim26ao)
- <a id="liu26bl-loss-functions"></a>[LARA: Latent Action Representation Alignment for Vision-Language-Action Models](../conferences/icml-2026/cards/2801-2900.md#paper-liu26bl)
- <a id="reconvla-loss-functions"></a><a id="reconvla-modules"></a>[ReconVLA](reconvla.md#paper-reconvla)

<a id="by-optimization"></a>

### 优化

- <a id="chaudhary26a-optimization"></a>[Blending Neural Control Density Functions for Stabilization and Safety](../conferences/icml-2026/cards/0401-0500.md#paper-chaudhary26a)
- <a id="fan26g-optimization"></a>[De4D-SLAM: Gradient-Isolated Static-Dynamic Decoupling for Monocular SLAM in Dynamic Environments](../conferences/icml-2026/cards/1001-1100.md#paper-fan26g)
- <a id="khan26a-optimization"></a>[Optimal and Scalable MAPF via Multi-Marginal Optimal Transport and Schrödinger Bridges](../conferences/icml-2026/cards/2001-2100.md#paper-khan26a)
- <a id="psenka26a-optimization"></a>[Parallel Stochastic Gradient-Based Planning for World Models](../conferences/icml-2026/cards/3601-3700.md#paper-psenka26a)
- <a id="qiu26c-optimization"></a>[Debate2Create: Robot Co-design via Multi-Agent LLM Debate](../conferences/icml-2026/cards/3701-3800.md#paper-qiu26c)

<a id="by-reinforcement-learning"></a>

### 强化学习方法

- <a id="aichmuller26a-reinforcement-learning"></a>[Learning to Search and Searching to Learn for Generalization in Planning](../conferences/icml-2026/cards/0001-0100.md#paper-aichmuller26a)
- <a id="chowdhury26a-reinforcement-learning"></a>[LAGEA: Language Guided Embodied Agents for Robotic Manipulation](../conferences/icml-2026/cards/0701-0800.md#paper-chowdhury26a)
- <a id="ge26a-reinforcement-learning"></a>[Dyn-VPP: Video Prediction Policy Optimization for Improved Visual Dynamics](../conferences/icml-2026/cards/1201-1300.md#paper-ge26a)
- <a id="guo26ae-reinforcement-learning"></a>[CorrectionPlanner: Self-Correction Planner with Reinforcement Learning in Autonomous Driving](../conferences/icml-2026/cards/1401-1500.md#paper-guo26ae)
- <a id="heald26a-reinforcement-learning"></a>[Joint-Space Empowerment for Dexterous Coordination in Tendon-Driven Hands](../conferences/icml-2026/cards/1501-1600.md#paper-heald26a)
- <a id="hossain26a-reinforcement-learning"></a>[Learning Anisotropic Value Geometry with Finsler Reinforcement Learning](../conferences/icml-2026/cards/1501-1600.md#paper-hossain26a)
- <a id="ji26e-reinforcement-learning"></a>[Recovering Hidden Reward in Diffusion-Based Policies](../conferences/icml-2026/cards/1801-1900.md#paper-ji26e)
- <a id="lei26e-reinforcement-learning"></a>[Think Less, Act Early: Reinforced Latent Reasoning with Early Exit in Vision-Language-Action Models](../conferences/icml-2026/cards/2301-2400.md#paper-lei26e)
- <a id="li26jr-reinforcement-learning"></a>[UAV$^2$: A Unified and Adaptive Scheduling Framework for UAV Autopilot Systems with Reinforcement Learning](../conferences/icml-2026/cards/2601-2700.md#paper-li26jr)
- <a id="lian26c-reinforcement-learning"></a>[MapDream: Task-Driven Map Learning for Vision-Language Navigation](../conferences/icml-2026/cards/2601-2700.md#paper-lian26c)
- <a id="lin26af-reinforcement-learning"></a>[DyGRO-VLA: Cross-Task Scaling of Vision–Language–Action Models via Dynamic Grouped Residual Optimization](../conferences/icml-2026/cards/2701-2800.md#paper-lin26af)
- <a id="liu26et-reinforcement-learning"></a>[TimeRewarder: Learning Dense Reward from Passive Videos via Frame-wise Temporal Distance](../conferences/icml-2026/cards/2901-3000.md#paper-liu26et)
- <a id="longhini26a-reinforcement-learning"></a>[Behavioral Mode Discovery for Fine-tuning Multimodal Generative Policies](../conferences/icml-2026/cards/2901-3000.md#paper-longhini26a)
- <a id="luo26v-reinforcement-learning"></a>[DF-ExpEnse: Diffusion Filtered Exploration for Sample Efficient Finetuning](../conferences/icml-2026/cards/3001-3100.md#paper-luo26v)
- <a id="luu26a-reinforcement-learning"></a>[Video-Based Optimal Transport for Feedback-Efficient Offline Preference-Based Reinforcement Learning](../conferences/icml-2026/cards/3001-3100.md#paper-luu26a)
- <a id="mandi26a-reinforcement-learning"></a>[DexMachina: Functional Retargeting for Bimanual Dexterous Manipulation](../conferences/icml-2026/cards/3201-3300.md#paper-mandi26a)
- <a id="ni26d-reinforcement-learning"></a>[CoRe: Combined Rewards with Vision-Language Model Feedback for Preference-Aligned Reinforcement Learning](../conferences/icml-2026/cards/3401-3500.md#paper-ni26d)
- <a id="patil26a-reinforcement-learning"></a>[OGPO: Sample Efficient Full-Finetuning of Generative Control Policies](../conferences/icml-2026/cards/3601-3700.md#paper-patil26a)
- <a id="pranger26a-reinforcement-learning"></a>[Efficient and Safe Molecular Assembly via Reinforcement Learning and Constraint Solving](../conferences/icml-2026/cards/3601-3700.md#paper-pranger26a)
- <a id="qiao26f-reinforcement-learning"></a>[Focus-Then-Contact: Speeding Up Robotic Contact-Rich Task Learning with Affordance-Guided Real-World Residual Reinforcement Learning](../conferences/icml-2026/cards/3701-3800.md#paper-qiao26f)
- <a id="ruan26c-reinforcement-learning"></a>[ScenePilot: Controllable Boundary-Driven Critical Scenario Generation for Autonomous Driving](../conferences/icml-2026/cards/3801-3900.md#paper-ruan26c)
- <a id="shen26e-reinforcement-learning"></a>[Plan in Sandbox, Navigate in Open Worlds: Learning Physics-Grounded Abstracted Experience for Embodied Navigation](../conferences/icml-2026/cards/4001-4100.md#paper-shen26e)

<a id="by-training-strategies"></a>

### 训练策略

- <a id="chen26d-training-strategies"></a>[NOMAD: Lifelong Trajectory Planning via Non-Parametric Bayesian Memory-Adaptive Diffusion Experts](../conferences/icml-2026/cards/0401-0500.md#paper-chen26d)
- <a id="chen26fw-training-strategies"></a>[Generalizable and Actionable Parts Pose Estimation with Symmetry Annotation-Free Learning Strategy](../conferences/icml-2026/cards/0601-0700.md#paper-chen26fw)
- <a id="feng26n-training-strategies"></a>[Knowledge Diversion for Efficient Morphology Control and Policy Transfer](../conferences/icml-2026/cards/1101-1200.md#paper-feng26n)
- <a id="guo26i-training-strategies"></a>[VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model](../conferences/icml-2026/cards/1301-1400.md#paper-guo26i)
- <a id="he26aq-training-strategies"></a>[FocalPolicy: Frequency-Optimized Chunking and Locally Anchored Flow Matching for Coherent Visuomotor Policy](../conferences/icml-2026/cards/1501-1600.md#paper-he26aq)
- <a id="huang26v-training-strategies"></a>[Self-CriTeach: LLM Self-Teaching and Self-Critiquing for Improving Robotic Planning via Automated Domain Generation](../conferences/icml-2026/cards/1701-1800.md#paper-huang26v)
- <a id="huang26cd-training-strategies"></a>[TIC-VLA: A Think-in-Control Vision-Language-Action Model for Robot Navigation in Dynamic Environments](../conferences/icml-2026/cards/1701-1800.md#paper-huang26cd)
- <a id="lei26d-training-strategies"></a>[A Mechanistic Analysis of Sim-and-Real Co-Training in Generative Robot Policies](../conferences/icml-2026/cards/2301-2400.md#paper-lei26d)
- <a id="lian26d-training-strategies"></a>[LangForce: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries](../conferences/icml-2026/cards/2601-2700.md#paper-lian26d)
- <a id="liu26am-training-strategies"></a>[NeurVLA: Unleashing Failure-Handling Capability of Vision-Language-Action Models via Neural-Symbolic Reasoning](../conferences/icml-2026/cards/2801-2900.md#paper-liu26am)
- <a id="liu26bx-training-strategies"></a>[RDT2: Exploring the Scaling Limit of UMI Data Towards Zero-Shot Cross-Embodiment Generalization](../conferences/icml-2026/cards/2801-2900.md#paper-liu26bx)
- <a id="luo26e-training-strategies"></a>[Vision-Language-Action Pretraining from Large-Scale Human Videos](../conferences/icml-2026/cards/3001-3100.md#paper-luo26e)
- <a id="morin26a-training-strategies"></a>[On the Sample Efficiency of Inverse Dynamics Models for Semi-Supervised Imitation Learning](../conferences/icml-2026/cards/3301-3400.md#paper-morin26a)
- <a id="nguyen26b-training-strategies"></a>[FOCA: Future-Oriented Conditioning for Data-Efficient Vision-Language-Action Adaptation](../conferences/icml-2026/cards/3401-3500.md#paper-nguyen26b)

<a id="by-data-strategies"></a>

### 数据策略

- <a id="chen26j-data-strategies"></a>[RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation](../conferences/icml-2026/cards/0401-0500.md#paper-chen26j)
- <a id="chen26ab-data-strategies"></a>[PhyScene3D: Physically Consistent Interactive 3D Tabletop Scene Generation](../conferences/icml-2026/cards/0401-0500.md#paper-chen26ab)
- <a id="chen26cy-data-strategies"></a>[Escaping the Diversity Trap in Robotic Manipulation via Anchor-Centric Adaptation](../conferences/icml-2026/cards/0501-0600.md#paper-chen26cy)
- <a id="choi26i-data-strategies"></a>[EMBGuard: Constructing Hazard-Aware Guardrails for Safe Planning in Embodied Agents](../conferences/icml-2026/cards/0701-0800.md#paper-choi26i)
- <a id="fan26b-data-strategies"></a>[Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds](../conferences/icml-2026/cards/1001-1100.md#paper-fan26b)
- <a id="gao26q-data-strategies"></a>[DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos](../conferences/icml-2026/cards/1201-1300.md#paper-gao26q)
- <a id="guan26f-data-strategies"></a>[LIMMT: Less Is More for Motion Tracking](../conferences/icml-2026/cards/1301-1400.md#paper-guan26f)
- <a id="hui26b-data-strategies"></a>[Seeing Realism from Simulation: Efficient Video Transfer for Vision-Language-Action Data Augmentation](../conferences/icml-2026/cards/1701-1800.md#paper-hui26b)
- <a id="ji26g-data-strategies"></a>[OXE-AugE: A Large-Scale Robot Augmentation of OXE for Scaling Cross-Embodiment Policy Learning](../conferences/icml-2026/cards/1801-1900.md#paper-ji26g)
- <a id="liang26n-data-strategies"></a>[PRISM: Learning Realistic Depth via Physics-Grounded Noise Disentanglement with Semantic-Geometric Collaboration](../conferences/icml-2026/cards/2601-2700.md#paper-liang26n)

<a id="by-inference"></a>

### 推理策略

- <a id="aissi26a-inference"></a>[PRISM: Perception Reasoning Interleaved for Sequential Decision Making.](../conferences/icml-2026/cards/0001-0100.md#paper-aissi26a)
- <a id="balim26a-inference"></a>[Model-Based Diffusion Sampling for Predictive Control in Offline Decision Making](../conferences/icml-2026/cards/0201-0300.md#paper-balim26a)
- <a id="beyer26a-inference"></a>[Motion Planning in Compressed Representation Spaces](../conferences/icml-2026/cards/0201-0300.md#paper-beyer26a)
- <a id="chai26a-inference"></a>[N2M: Bridging Navigation and Manipulation by Learning Pose Preference from Rollout](../conferences/icml-2026/cards/0401-0500.md#paper-chai26a)
- <a id="chen26i-inference"></a>[PSG-Nav: Probabilistic Scene Graph Navigation via Multiverse Decision Making](../conferences/icml-2026/cards/0401-0500.md#paper-chen26i)
- <a id="chen26co-inference"></a>[Rethinking Instruction Drift as a Sampling Error: SNR-Aware Power Distributions for Long-Horizon Robotic Planning](../conferences/icml-2026/cards/0501-0600.md#paper-chen26co)
- <a id="chi26b-inference"></a>[EvoCF: Multi-Agent Collaboration via Agentic Memory-Driven Evolutionary Counterfactual Planning](../conferences/icml-2026/cards/0701-0800.md#paper-chi26b)
- <a id="choi26a-inference"></a>[SCALE: Self-uncertainty Conditioned Adaptive Looking and Execution for Vision-Language-Action Models](../conferences/icml-2026/cards/0701-0800.md#paper-choi26a)
- <a id="choi26c-inference"></a>[Efficient Skill Grounding via Code Refactoring with Small Language Models](../conferences/icml-2026/cards/0701-0800.md#paper-choi26c)
- <a id="chun26a-inference"></a>[Functional Cache Grafting: Robust and Rapid Code-Policy Synthesis for Embodied Agents](../conferences/icml-2026/cards/0701-0800.md#paper-chun26a)
- <a id="ding26r-inference"></a>[AdaNav: Adaptive Reasoning with Uncertainty for Vision-Language Navigation](../conferences/icml-2026/cards/0901-1000.md#paper-ding26r)
- <a id="guo26l-inference"></a>[Reflex: Real-Time Vision-Language-Action Control through Streaming Inference](../conferences/icml-2026/cards/1301-1400.md#paper-guo26l)
- <a id="hoshino26a-inference"></a>[Training-Free Guided Diffusion for Planning: A Unified Framework via Doob’s h-Transform with Safety Guarantees](../conferences/icml-2026/cards/1501-1600.md#paper-hoshino26a)
- <a id="hu26w-inference"></a>[Turning Adaptation into Assets: Cross-Domain Bridging for Online Vision-Language Navigation](../conferences/icml-2026/cards/1601-1700.md#paper-hu26w)
- <a id="huang26h-inference"></a>[EcoVLA: Environment-Aware Adaptive Pruning with Interleaved Inference Orchestration for Vision-Language-Action Models](../conferences/icml-2026/cards/1601-1700.md#paper-huang26h)
- <a id="huang26t-inference"></a>[SAD-Flower: Flow Matching for Safe, Admissible, and Dynamically Consistent Planning](../conferences/icml-2026/cards/1701-1800.md#paper-huang26t)
- <a id="jayasinghe26a-inference"></a>[Cerebellar-Inspired Residual Control for Fault Recovery: From Inference-Time Adaptation to Structural Consolidation](../conferences/icml-2026/cards/1801-1900.md#paper-jayasinghe26a)
- <a id="ji26o-inference"></a>[Sparse ActionGen: Accelerating Diffusion Policy with Real-time Pruning](../conferences/icml-2026/cards/1801-1900.md#paper-ji26o)
- <a id="jiang26av-inference"></a>[DecoVer: A Decompose-and-Verify Neuro-Symbolic Framework for Embodied Task Planning with BC+](../conferences/icml-2026/cards/1901-2000.md#paper-jiang26av)
- <a id="kapoor26a-inference"></a>[SafeDec: Constrained Decoding for Safe Autoregressive Generalist Robot Navigation Policies](../conferences/icml-2026/cards/2001-2100.md#paper-kapoor26a)
- <a id="lee26ax-inference"></a>[Bring My Cup! Personalizing Vision-Language-Action Models with Visual Attentive Prompting](../conferences/icml-2026/cards/2301-2400.md#paper-lee26ax)
- <a id="li26aa-inference"></a>[STEP: Warm-Started Visuomotor Policies with Spatiotemporal Consistency Prediction](../conferences/icml-2026/cards/2401-2500.md#paper-li26aa)
- <a id="li26fl-inference"></a>[VLA-ATTC: Adaptive Test-Time Compute for VLA Models with Relative Action Critic Model](../conferences/icml-2026/cards/2501-2600.md#paper-li26fl)
- <a id="li26id-inference"></a>[Embodied Task Planning via Graph-Informed Action Generation with Large Language Models](../conferences/icml-2026/cards/2601-2700.md#paper-li26id)
- <a id="liang26l-inference"></a>[Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies](../conferences/icml-2026/cards/2601-2700.md#paper-liang26l)
- <a id="liu26fo-inference"></a>[When Replanning Becomes the Bottleneck: Budgeted Replanning for Embodied Agents](../conferences/icml-2026/cards/2901-3000.md#paper-liu26fo)
- <a id="luo26ab-inference"></a>[STABLE: Simulation-Ready Tabletop Layout Generation via a Semantics–Physics Dual System](../conferences/icml-2026/cards/3001-3100.md#paper-luo26ab)
- <a id="nandiraju26a-inference"></a>[HDFlow: Hierarchical Diffusion-Flow Planning for Long-horizon Tasks](../conferences/icml-2026/cards/3401-3500.md#paper-nandiraju26a)
- <a id="panchal26b-inference"></a>[Mosaic: Runtime-Efficient Multi-Agent Embodied Planning](../conferences/icml-2026/cards/3501-3600.md#paper-panchal26b)
- <a id="pfaff26a-inference"></a>[SceneSmith: Agentic Generation of Simulation-Ready Indoor Scenes](../conferences/icml-2026/cards/3601-3700.md#paper-pfaff26a)
- <a id="ren26a-inference"></a>[Fisher-Preserving Guidance: Training-Free Manifold Constraints for Safe Diffusion Control](../conferences/icml-2026/cards/3801-3900.md#paper-ren26a)
- <a id="shen26ab-inference"></a>[Plug-and-Play Label Map Diffusion for Universal Goal-Oriented Navigation](../conferences/icml-2026/cards/4001-4100.md#paper-shen26ab)

<a id="by-representation-learning"></a>

### 表征学习

- <a id="fan26f-representation-learning"></a>[XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations](../conferences/icml-2026/cards/1001-1100.md#paper-fan26f)
- <a id="habashy26a-representation-learning"></a>[Geodesic Flow Matching for Denoising High-Dimensional Structured Representations](../conferences/icml-2026/cards/1401-1500.md#paper-habashy26a)
- <a id="he26ao-representation-learning"></a>[Motion Dynamics Learning for Few-Shot Embodied Adaptation](../conferences/icml-2026/cards/1501-1600.md#paper-he26ao)
- <a id="huang26bv-representation-learning"></a>[Cross-Embodiment Robot Foundation World Models with Latent Actions](../conferences/icml-2026/cards/1701-1800.md#paper-huang26bv)
- <a id="lee26am-representation-learning"></a>[MVP-LAM: Learning Action-Centric Latent Action via Cross-Viewpoint Reconstruction](../conferences/icml-2026/cards/2301-2400.md#paper-lee26am)
- <a id="li26jf-representation-learning"></a>[From Imagined Futures to Executable Actions: Mixture of Latent Actions for Robot Manipulation](../conferences/icml-2026/cards/2601-2700.md#paper-li26jf)
- <a id="lin26s-representation-learning"></a>[From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models](../conferences/icml-2026/cards/2701-2800.md#paper-lin26s)
- <a id="lou26a-representation-learning"></a>[Predicting What Matters: Robust Generalist Robot Policy Learning via Future Semantic Mask](../conferences/icml-2026/cards/2901-3000.md#paper-lou26a)
- <a id="lyu26a-representation-learning"></a>[General Covariant Action Modeling: Constructing Generalized Manifolds via Spatio-Temporal Decoupling](../conferences/icml-2026/cards/3101-3200.md#paper-lyu26a)
- <a id="lyu26b-representation-learning"></a>[LAST: Bridging Vision-Language and Action Manifolds via Gromov-Wasserstein Alignment](../conferences/icml-2026/cards/3101-3200.md#paper-lyu26b)
- <a id="nam26c-representation-learning"></a>[Causal-JEPA: Learning World Models through Object-Level Latent Masking](../conferences/icml-2026/cards/3401-3500.md#paper-nam26c)

<a id="by-evaluation"></a>

### 评测与诊断

- <a id="bai26e-evaluation"></a>[SafeLab: An Interactive High-Fidelity Benchmark for Embodied Safety in Scientific Robotics](../conferences/icml-2026/cards/0101-0200.md#paper-bai26e)
- <a id="cao26w-evaluation"></a>[DLO-Lab: Benchmarking Deformable Linear Object Manipulations with Differentiable Physics](../conferences/icml-2026/cards/0401-0500.md#paper-cao26w)
- <a id="dai26c-evaluation"></a>[RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies](../conferences/icml-2026/cards/0801-0900.md#paper-dai26c)
- <a id="deng26r-evaluation"></a>[Rethinking Video Generation Model for the Embodied World](../conferences/icml-2026/cards/0801-0900.md#paper-deng26r)
- <a id="feng26ab-evaluation"></a>[Demystifying Action Space Design for Robotic Manipulation Policies](../conferences/icml-2026/cards/1101-1200.md#paper-feng26ab)
- <a id="fu26u-evaluation"></a>[CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation](../conferences/icml-2026/cards/1101-1200.md#paper-fu26u)
- <a id="huang26cm-evaluation"></a>[TRAP: Hijacking VLA CoT-Reasoning via Adversarial Patches](../conferences/icml-2026/cards/1701-1800.md#paper-huang26cm)
- <a id="kang26i-evaluation"></a>[Moving Out: Physically-grounded Human-AI Collaboration](../conferences/icml-2026/cards/2001-2100.md#paper-kang26i)
- <a id="li26hi-evaluation"></a>[Scaling Robot Policy Evaluation via Discrete Diffusion World Model](../conferences/icml-2026/cards/2601-2700.md#paper-li26hi)
- <a id="liu26bu-evaluation"></a>[Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning](../conferences/icml-2026/cards/2801-2900.md#paper-liu26bu)
- <a id="meng26n-evaluation"></a>[Distinguishing Imitation Error from Intrinsic Motion Learning Difficulty](../conferences/icml-2026/cards/3201-3300.md#paper-meng26n)
- <a id="qi26p-evaluation"></a>[BEAR: Dissecting Embodied Abilities in Multimodal Language Models through Skill-level Evaluation and Diagnosis](../conferences/icml-2026/cards/3701-3800.md#paper-qi26p)

<a id="by-theory-statistics"></a>

### 理论与统计

- <a id="francis-meretzki26a-theory-statistics"></a>[Temporal Difference Calibration in Sequential Tasks: Application to Vision-Language-Action Models](../conferences/icml-2026/cards/1101-1200.md#paper-francis-meretzki26a)
<!-- classification:end -->
