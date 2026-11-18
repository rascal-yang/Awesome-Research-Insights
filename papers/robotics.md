# 机器人学

[首页](../README.md) · [参与贡献](../CONTRIBUTING.md) · [English](../en/papers/robotics.md)

机器人感知、策略学习、规划与控制。

<!-- classification:start -->
## 按技术类型浏览

[模型架构](#by-architecture) · [模块](#by-modules) · [损失函数](#by-loss-functions) · [优化](#by-optimization) · [强化学习方法](#by-reinforcement-learning) · [训练策略](#by-training-strategies) · [数据策略](#by-data-strategies) · [推理策略](#by-inference) · [表征学习](#by-representation-learning) · [评测与诊断](#by-evaluation) · [理论与统计](#by-theory-statistics)

<a id="by-architecture"></a>

### 模型架构

- <a id="cao26u-architecture"></a>[Hierarchical Policy Learning via Spectral Decomposition](../conferences/icml-2026/cards/0401-0500.md#paper-cao26u)
- <a id="ding26x-architecture"></a>[Embodied-DETR: End-to-End Temporal 3D Object Detection in Egocentric Views](../conferences/icml-2026/cards/0901-1000.md#paper-ding26x)
- <a id="jiang26bf-architecture"></a>[VectorWorld: Efficient Streaming World Model via Diffusion Flow on Vector Graphs](../conferences/icml-2026/cards/1901-2000.md#paper-jiang26bf)
- <a id="lin26ab-architecture"></a>[MSP: Probabilistically Consistent Multi-Scale Action Generation](../conferences/icml-2026/cards/2701-2800.md#paper-lin26ab)
- <a id="liu26bf-architecture"></a>[GAE: Unleashing Physical Potential of VLM with Generalizable Action Expert](../conferences/icml-2026/cards/2801-2900.md#paper-liu26bf)
- <a id="liu26ch-architecture"></a>[LaST$_0$: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model](../conferences/icml-2026/cards/2801-2900.md#paper-liu26ch)
- <a id="liu26db-architecture"></a>[Sample from What You See: Visuomotor Policy Learning via Diffusion Bridge with Observation-Embedded Stochastic Differential Equation](../conferences/icml-2026/cards/2801-2900.md#paper-liu26db)
- <a id="liu26gf-architecture"></a>[Neural Implicit Action Fields: From Discrete Waypoints to Continuous Functions for Vision-Language-Action Models](../conferences/icml-2026/cards/2901-3000.md#paper-liu26gf)
- <a id="ma26ar-architecture"></a>[PolyFlow: Safe and Efficient Polytope-Constrained Flow Matching with Constraint Embedding and Projection-free Update](../conferences/icml-2026/cards/3101-3200.md#paper-ma26ar)
- <a id="shou26a-architecture"></a>[HALO: A Unified Vision-Language-Action Model for Embodied Multimodal Chain-of-Thought Reasoning](../conferences/icml-2026/cards/4101-4200.md#paper-shou26a)
- <a id="song26q-architecture"></a>[TF-FACE: Time-Frequency Fusion Learning via Frequency-Domain Adaptive and Controllable Enhancement for Trajectory Prediction](../conferences/icml-2026/cards/4201-4300.md#paper-song26q)
- <a id="thompson26a-architecture"></a>[Learning Manifold and Itô Dynamics with Branched Neural Rough Differential Equations](../conferences/icml-2026/cards/4401-4500.md#paper-thompson26a)
- <a id="wang26dc-architecture"></a>[WestWorld: A Knowledge-Encoded Scalable Trajectory World Model for Diverse Robotic Systems](../conferences/icml-2026/cards/4601-4700.md#paper-wang26dc)
- <a id="wang26gs-architecture"></a>[Factored Latent Action World Models](../conferences/icml-2026/cards/4701-4800.md#paper-wang26gs)
- <a id="wikman26a-architecture"></a>[Adaptive Reinforcement Learning for Unobservable Random Delays](../conferences/icml-2026/cards/4901-5000.md#paper-wikman26a)
- <a id="yin26l-architecture"></a>[DDP-WM: Disentangled Dynamics Prediction for Efficient World Models](../conferences/icml-2026/cards/5501-5600.md#paper-yin26l)

<a id="by-modules"></a>

### 模块

- <a id="feng26x-modules"></a>[See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model](../conferences/icml-2026/cards/1101-1200.md#paper-feng26x)
- <a id="jang26c-modules"></a>[RA-VLA: Retrieval-Augmented VLA for Test-Time Adaptation](../conferences/icml-2026/cards/1801-1900.md#paper-jang26c)
- <a id="jing26f-modules"></a>[Mixture of Horizons in Action Chunking](../conferences/icml-2026/cards/1901-2000.md#paper-jing26f)
- <a id="tian26f-modules"></a>[QPKO: Differentiable QP-Embedded Deep Koopman Framework for Modeling Nonlinear Systems](../conferences/icml-2026/cards/4401-4500.md#paper-tian26f)
- <a id="wang26bv-modules"></a>[MoSA: Motion-constrained Stress Adaptation for Mitigating Real-to-Sim Gap in Continuum Dynamics via Learning Residual Anisotropy](../conferences/icml-2026/cards/4601-4700.md#paper-wang26bv)

<a id="by-loss-functions"></a><a id="vision-language-action-models"></a>

### 损失函数

- <a id="amad26a-loss-functions"></a>[DT²: Decision-Targeted Digital Twins](../conferences/icml-2026/cards/0001-0100.md#paper-amad26a)
- <a id="fang26h-loss-functions"></a>[OMP: One-step Meanflow Policy with Directional Alignment](../conferences/icml-2026/cards/1001-1100.md#paper-fang26h)
- <a id="liu26bl-loss-functions"></a>[LARA: Latent Action Representation Alignment for Vision-Language-Action Models](../conferences/icml-2026/cards/2801-2900.md#paper-liu26bl)
- <a id="sun26al-loss-functions"></a>[From Prior to Pro: Efficient Skill Mastery via Distribution Contractive RL Finetuning](../conferences/icml-2026/cards/4301-4400.md#paper-sun26al)
- <a id="wan26f-loss-functions"></a>[Multi-view Consistent Latent Action Learning for World Modeling and Control](../conferences/icml-2026/cards/4501-4600.md#paper-wan26f)
- <a id="wang26n-loss-functions"></a>[Temporal Straightening for Latent Planning](../conferences/icml-2026/cards/4501-4600.md#paper-wang26n)
- <a id="wang26dk-loss-functions"></a>[ECo-MoE: Embodiment-Conditioned Mixture of Experts Increases the Evolvability of Robots](../conferences/icml-2026/cards/4601-4700.md#paper-wang26dk)
- <a id="wang26dy-loss-functions"></a>[Learning Attribute–Affordance Hierarchies in Hyperbolic Space for Open-Vocabulary 3D Object Affordance Grounding](../conferences/icml-2026/cards/4701-4800.md#paper-wang26dy)
- <a id="yang26ax-loss-functions"></a>[Counterfactual Occlusion-Aware Learning via Visibility Intervention for LiDAR Anomaly Detection](../conferences/icml-2026/cards/5301-5400.md#paper-yang26ax)
- <a id="zhang26if-loss-functions"></a>[A Generalist Pair-wise Progress Critic Model for Vision-Language-Action Robots](../conferences/icml-2026/cards/5901-6000.md#paper-zhang26if)
- <a id="reconvla-loss-functions"></a><a id="reconvla-modules"></a>[ReconVLA](reconvla.md#paper-reconvla)

<a id="by-optimization"></a>

### 优化

- <a id="chaudhary26a-optimization"></a>[Blending Neural Control Density Functions for Stabilization and Safety](../conferences/icml-2026/cards/0401-0500.md#paper-chaudhary26a)
- <a id="fan26g-optimization"></a>[De4D-SLAM: Gradient-Isolated Static-Dynamic Decoupling for Monocular SLAM in Dynamic Environments](../conferences/icml-2026/cards/1001-1100.md#paper-fan26g)
- <a id="khan26a-optimization"></a>[Optimal and Scalable MAPF via Multi-Marginal Optimal Transport and Schrödinger Bridges](../conferences/icml-2026/cards/2001-2100.md#paper-khan26a)
- <a id="psenka26a-optimization"></a>[Parallel Stochastic Gradient-Based Planning for World Models](../conferences/icml-2026/cards/3601-3700.md#paper-psenka26a)
- <a id="tong26j-optimization"></a>[Neural Control: Adjoint Learning Through Equilibrium Constraints](../conferences/icml-2026/cards/4401-4500.md#paper-tong26j)
- <a id="zhao26cd-optimization"></a>[Dual Quaternion SE(3) Synchronization with Recovery Guarantees](../conferences/icml-2026/cards/6001-6100.md#paper-zhao26cd)

<a id="by-reinforcement-learning"></a>

### 强化学习方法

- <a id="guo26ae-reinforcement-learning"></a>[CorrectionPlanner: Self-Correction Planner with Reinforcement Learning in Autonomous Driving](../conferences/icml-2026/cards/1401-1500.md#paper-guo26ae)
- <a id="heald26a-reinforcement-learning"></a>[Joint-Space Empowerment for Dexterous Coordination in Tendon-Driven Hands](../conferences/icml-2026/cards/1501-1600.md#paper-heald26a)
- <a id="ji26e-reinforcement-learning"></a>[Recovering Hidden Reward in Diffusion-Based Policies](../conferences/icml-2026/cards/1801-1900.md#paper-ji26e)
- <a id="lian26c-reinforcement-learning"></a>[MapDream: Task-Driven Map Learning for Vision-Language Navigation](../conferences/icml-2026/cards/2601-2700.md#paper-lian26c)
- <a id="liu26et-reinforcement-learning"></a>[TimeRewarder: Learning Dense Reward from Passive Videos via Frame-wise Temporal Distance](../conferences/icml-2026/cards/2901-3000.md#paper-liu26et)
- <a id="longhini26a-reinforcement-learning"></a>[Behavioral Mode Discovery for Fine-tuning Multimodal Generative Policies](../conferences/icml-2026/cards/2901-3000.md#paper-longhini26a)
- <a id="luo26v-reinforcement-learning"></a>[DF-ExpEnse: Diffusion Filtered Exploration for Sample Efficient Finetuning](../conferences/icml-2026/cards/3001-3100.md#paper-luo26v)
- <a id="luu26a-reinforcement-learning"></a>[Video-Based Optimal Transport for Feedback-Efficient Offline Preference-Based Reinforcement Learning](../conferences/icml-2026/cards/3001-3100.md#paper-luu26a)
- <a id="mandi26a-reinforcement-learning"></a>[DexMachina: Functional Retargeting for Bimanual Dexterous Manipulation](../conferences/icml-2026/cards/3201-3300.md#paper-mandi26a)
- <a id="patil26a-reinforcement-learning"></a>[OGPO: Sample Efficient Full-Finetuning of Generative Control Policies](../conferences/icml-2026/cards/3601-3700.md#paper-patil26a)
- <a id="ruan26c-reinforcement-learning"></a>[ScenePilot: Controllable Boundary-Driven Critical Scenario Generation for Autonomous Driving](../conferences/icml-2026/cards/3801-3900.md#paper-ruan26c)
- <a id="shen26e-reinforcement-learning"></a>[Plan in Sandbox, Navigate in Open Worlds: Learning Physics-Grounded Abstracted Experience for Embodied Navigation](../conferences/icml-2026/cards/4001-4100.md#paper-shen26e)
- <a id="simsir26a-reinforcement-learning"></a>[Lagrangian Perturbation Diffusion Steering: Latent Reinforcement Learning for Generative Policies](../conferences/icml-2026/cards/4101-4200.md#paper-simsir26a)
- <a id="sun26n-reinforcement-learning"></a>[Uncertainty-Guided Exploration and Stable Planning for Sparse-Reward Manipulation from Limited Demonstrations](../conferences/icml-2026/cards/4201-4300.md#paper-sun26n)
- <a id="tang26o-reinforcement-learning"></a>[ReLAM: Learning Anticipation Model for Rewarding Visual Robotic Manipulation](../conferences/icml-2026/cards/4301-4400.md#paper-tang26o)
- <a id="taranovic26a-reinforcement-learning"></a>[PAWS: Preference Learning with Advantage-Weighted Segments](../conferences/icml-2026/cards/4401-4500.md#paper-taranovic26a)

<a id="by-training-strategies"></a>

### 训练策略

- <a id="chen26fw-training-strategies"></a>[Generalizable and Actionable Parts Pose Estimation with Symmetry Annotation-Free Learning Strategy](../conferences/icml-2026/cards/0601-0700.md#paper-chen26fw)
- <a id="guo26i-training-strategies"></a>[VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model](../conferences/icml-2026/cards/1301-1400.md#paper-guo26i)
- <a id="he26aq-training-strategies"></a>[FocalPolicy: Frequency-Optimized Chunking and Locally Anchored Flow Matching for Coherent Visuomotor Policy](../conferences/icml-2026/cards/1501-1600.md#paper-he26aq)
- <a id="huang26cd-training-strategies"></a>[TIC-VLA: A Think-in-Control Vision-Language-Action Model for Robot Navigation in Dynamic Environments](../conferences/icml-2026/cards/1701-1800.md#paper-huang26cd)
- <a id="lei26d-training-strategies"></a>[A Mechanistic Analysis of Sim-and-Real Co-Training in Generative Robot Policies](../conferences/icml-2026/cards/2301-2400.md#paper-lei26d)
- <a id="lian26d-training-strategies"></a>[LangForce: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries](../conferences/icml-2026/cards/2601-2700.md#paper-lian26d)
- <a id="morin26a-training-strategies"></a>[On the Sample Efficiency of Inverse Dynamics Models for Semi-Supervised Imitation Learning](../conferences/icml-2026/cards/3301-3400.md#paper-morin26a)
- <a id="wagenmaker26a-training-strategies"></a>[Posterior Behavioral Cloning: Pretraining BC Policies for Efficient RL Finetuning](../conferences/icml-2026/cards/4501-4600.md#paper-wagenmaker26a)
- <a id="wan26n-training-strategies"></a>[Adversarial Dual On-Policy Distillation from Expressive Teacher](../conferences/icml-2026/cards/4501-4600.md#paper-wan26n)
- <a id="wang26kz-training-strategies"></a>[Co-Evolving Latent Action World Models](../conferences/icml-2026/cards/4801-4900.md#paper-wang26kz)
- <a id="wu26m-training-strategies"></a>[VLANeXt: Recipes for Building Strong VLA Models](../conferences/icml-2026/cards/5001-5100.md#paper-wu26m)
- <a id="wu26ck-training-strategies"></a>[PACT: Self-Evolving Physical Safety Alignment for Diffusion Policies in Embodied Manipulation](../conferences/icml-2026/cards/5001-5100.md#paper-wu26ck)
- <a id="zheng26z-training-strategies"></a>[CoIRL-AD: Collaborative-Competitive Imitation-Reinforcement Learning in Latent World Models for Autonomous Driving](../conferences/icml-2026/cards/6101-6200.md#paper-zheng26z)

<a id="by-data-strategies"></a>

### 数据策略

- <a id="chen26cy-data-strategies"></a>[Escaping the Diversity Trap in Robotic Manipulation via Anchor-Centric Adaptation](../conferences/icml-2026/cards/0501-0600.md#paper-chen26cy)
- <a id="ji26g-data-strategies"></a>[OXE-AugE: A Large-Scale Robot Augmentation of OXE for Scaling Cross-Embodiment Policy Learning](../conferences/icml-2026/cards/1801-1900.md#paper-ji26g)
- <a id="liang26n-data-strategies"></a>[PRISM: Learning Realistic Depth via Physics-Grounded Noise Disentanglement with Semantic-Geometric Collaboration](../conferences/icml-2026/cards/2601-2700.md#paper-liang26n)
- <a id="tsai26a-data-strategies"></a>[Creat3r: Confidence Reaggregation for Exploration-aware Active 3D Reconstruction](../conferences/icml-2026/cards/4401-4500.md#paper-tsai26a)
- <a id="van-huffel26a-data-strategies"></a>[Neural Low-Discrepancy Sequences](../conferences/icml-2026/cards/4501-4600.md#paper-van-huffel26a)
- <a id="zhang26b-data-strategies"></a>[BALLAST: Bayesian Active Learning with Look-ahead Amendment for Sea-drifter Trajectories under Spatio-Temporal Vector Fields](../conferences/icml-2026/cards/5701-5800.md#paper-zhang26b)
- <a id="zhu26s-data-strategies"></a>[Making Learner Weakness Actionable for Learning from Demonstration with Novice Teachers](../conferences/icml-2026/cards/6201-6300.md#paper-zhu26s)

<a id="by-inference"></a>

### 推理策略

- <a id="balim26a-inference"></a>[Model-Based Diffusion Sampling for Predictive Control in Offline Decision Making](../conferences/icml-2026/cards/0201-0300.md#paper-balim26a)
- <a id="chen26co-inference"></a>[Rethinking Instruction Drift as a Sampling Error: SNR-Aware Power Distributions for Long-Horizon Robotic Planning](../conferences/icml-2026/cards/0501-0600.md#paper-chen26co)
- <a id="choi26a-inference"></a>[SCALE: Self-uncertainty Conditioned Adaptive Looking and Execution for Vision-Language-Action Models](../conferences/icml-2026/cards/0701-0800.md#paper-choi26a)
- <a id="guo26l-inference"></a>[Reflex: Real-Time Vision-Language-Action Control through Streaming Inference](../conferences/icml-2026/cards/1301-1400.md#paper-guo26l)
- <a id="hoshino26a-inference"></a>[Training-Free Guided Diffusion for Planning: A Unified Framework via Doob’s h-Transform with Safety Guarantees](../conferences/icml-2026/cards/1501-1600.md#paper-hoshino26a)
- <a id="hu26w-inference"></a>[Turning Adaptation into Assets: Cross-Domain Bridging for Online Vision-Language Navigation](../conferences/icml-2026/cards/1601-1700.md#paper-hu26w)
- <a id="huang26t-inference"></a>[SAD-Flower: Flow Matching for Safe, Admissible, and Dynamically Consistent Planning](../conferences/icml-2026/cards/1701-1800.md#paper-huang26t)
- <a id="jayasinghe26a-inference"></a>[Cerebellar-Inspired Residual Control for Fault Recovery: From Inference-Time Adaptation to Structural Consolidation](../conferences/icml-2026/cards/1801-1900.md#paper-jayasinghe26a)
- <a id="kapoor26a-inference"></a>[SafeDec: Constrained Decoding for Safe Autoregressive Generalist Robot Navigation Policies](../conferences/icml-2026/cards/2001-2100.md#paper-kapoor26a)
- <a id="li26aa-inference"></a>[STEP: Warm-Started Visuomotor Policies with Spatiotemporal Consistency Prediction](../conferences/icml-2026/cards/2401-2500.md#paper-li26aa)
- <a id="liang26l-inference"></a>[Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies](../conferences/icml-2026/cards/2601-2700.md#paper-liang26l)
- <a id="liu26fo-inference"></a>[When Replanning Becomes the Bottleneck: Budgeted Replanning for Embodied Agents](../conferences/icml-2026/cards/2901-3000.md#paper-liu26fo)
- <a id="luo26ab-inference"></a>[STABLE: Simulation-Ready Tabletop Layout Generation via a Semantics–Physics Dual System](../conferences/icml-2026/cards/3001-3100.md#paper-luo26ab)
- <a id="panchal26b-inference"></a>[Mosaic: Runtime-Efficient Multi-Agent Embodied Planning](../conferences/icml-2026/cards/3501-3600.md#paper-panchal26b)
- <a id="ren26a-inference"></a>[Fisher-Preserving Guidance: Training-Free Manifold Constraints for Safe Diffusion Control](../conferences/icml-2026/cards/3801-3900.md#paper-ren26a)
- <a id="shen26ab-inference"></a>[Plug-and-Play Label Map Diffusion for Universal Goal-Oriented Navigation](../conferences/icml-2026/cards/4001-4100.md#paper-shen26ab)
- <a id="song26e-inference"></a>[EnsembleVLA: Ensemble Learning for Vision-Language Action Models](../conferences/icml-2026/cards/4201-4300.md#paper-song26e)
- <a id="spieler26a-inference"></a>[Dream-MPC: Gradient-Based Model Predictive Control with Latent Imagination](../conferences/icml-2026/cards/4201-4300.md#paper-spieler26a)
- <a id="sun26y-inference"></a>[Ask Less, See More: Communication-Conditioned Token Pruning for Vehicle-to-Vehicle Cooperative Autonomous Driving with Multimodal Large Language Models](../conferences/icml-2026/cards/4201-4300.md#paper-sun26y)
- <a id="sun26ad-inference"></a>[Energy-based Compositional Diffusion Planning](../conferences/icml-2026/cards/4301-4400.md#paper-sun26ad)
- <a id="wang26jj-inference"></a>[SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning](../conferences/icml-2026/cards/4801-4900.md#paper-wang26jj)
- <a id="wang26lj-inference"></a>[Learning High-Frequency Continuous Action Chunks in Latent Space](../conferences/icml-2026/cards/4901-5000.md#paper-wang26lj)
- <a id="wu26bt-inference"></a>[Speedup Patch: Learning a Plug-and-Play Policy to Accelerate Embodied Manipulation](../conferences/icml-2026/cards/5001-5100.md#paper-wu26bt)
- <a id="xiong26o-inference"></a>[VGGT-Motion: Motion-Aware Calibration-Free Monocular SLAM for Long-Range Consistency](../conferences/icml-2026/cards/5201-5300.md#paper-xiong26o)
- <a id="xu26u-inference"></a>[Error Amplification Limits ANN-to-SNN Conversion in Continuous Control](../conferences/icml-2026/cards/5201-5300.md#paper-xu26u)
- <a id="zhang26gi-inference"></a>[Langevin Rollout Optimization for Modelic Reinforcement Learning](../conferences/icml-2026/cards/5901-6000.md#paper-zhang26gi)
- <a id="zhu26bj-inference"></a>[ProAct: A Benchmark and Multimodal Framework for Structure-Aware Proactive Response](../conferences/icml-2026/cards/6201-6300.md#paper-zhu26bj)

<a id="by-representation-learning"></a>

### 表征学习

- <a id="lee26am-representation-learning"></a>[MVP-LAM: Learning Action-Centric Latent Action via Cross-Viewpoint Reconstruction](../conferences/icml-2026/cards/2301-2400.md#paper-lee26am)
- <a id="lin26s-representation-learning"></a>[From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models](../conferences/icml-2026/cards/2701-2800.md#paper-lin26s)
- <a id="lou26a-representation-learning"></a>[Predicting What Matters: Robust Generalist Robot Policy Learning via Future Semantic Mask](../conferences/icml-2026/cards/2901-3000.md#paper-lou26a)
- <a id="lyu26a-representation-learning"></a>[General Covariant Action Modeling: Constructing Generalized Manifolds via Spatio-Temporal Decoupling](../conferences/icml-2026/cards/3101-3200.md#paper-lyu26a)
- <a id="lyu26b-representation-learning"></a>[LAST: Bridging Vision-Language and Action Manifolds via Gromov-Wasserstein Alignment](../conferences/icml-2026/cards/3101-3200.md#paper-lyu26b)
- <a id="su26c-representation-learning"></a>[World Guidance: World Modeling in Condition Space for Action Generation](../conferences/icml-2026/cards/4201-4300.md#paper-su26c)
- <a id="tarale26a-representation-learning"></a>[Bio-Inspired Self-Supervised Learning for Wrist-worn Accelerometer Data](../conferences/icml-2026/cards/4401-4500.md#paper-tarale26a)
- <a id="wang26er-representation-learning"></a>[DADP: Domain Adaptive Diffusion Policy](../conferences/icml-2026/cards/4701-4800.md#paper-wang26er)
- <a id="zhang26ec-representation-learning"></a>[DiLA: Disentangled Latent Action World Models](../conferences/icml-2026/cards/5801-5900.md#paper-zhang26ec)
- <a id="zhang26gn-representation-learning"></a>[GeoMoLa: Geometry-Aware Motion Latents for Learning Robust Manipulation Policies](../conferences/icml-2026/cards/5901-6000.md#paper-zhang26gn)
- <a id="zhong26g-representation-learning"></a>[From Noise to Intent: Anchoring Generative VLA Policies with Residual Bridges](../conferences/icml-2026/cards/6101-6200.md#paper-zhong26g)

<a id="by-evaluation"></a>

### 评测与诊断

- <a id="feng26ab-evaluation"></a>[Demystifying Action Space Design for Robotic Manipulation Policies](../conferences/icml-2026/cards/1101-1200.md#paper-feng26ab)
- <a id="huang26cm-evaluation"></a>[TRAP: Hijacking VLA CoT-Reasoning via Adversarial Patches](../conferences/icml-2026/cards/1701-1800.md#paper-huang26cm)
- <a id="liu26bu-evaluation"></a>[Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning](../conferences/icml-2026/cards/2801-2900.md#paper-liu26bu)
- <a id="meng26n-evaluation"></a>[Distinguishing Imitation Error from Intrinsic Motion Learning Difficulty](../conferences/icml-2026/cards/3201-3300.md#paper-meng26n)
- <a id="sun26an-evaluation"></a>[AIR-VLA: Vision-Language-Action Systems for Aerial Manipulation](../conferences/icml-2026/cards/4301-4400.md#paper-sun26an)
- <a id="tang26a-evaluation"></a>[See, Act, Adapt: Active Perception for Unsupervised Cross-Domain Visual Adaptation via Personalized VLM-Guided Agent](../conferences/icml-2026/cards/4301-4400.md#paper-tang26a)
- <a id="yan26r-evaluation"></a>[Can VLMs Diagnose and Recover from VLA Manipulation Faults?](../conferences/icml-2026/cards/5301-5400.md#paper-yan26r)
- <a id="yan26y-evaluation"></a>[CE$^4$L: Continual Ego, Exo, and Ego-Exo Learning](../conferences/icml-2026/cards/5301-5400.md#paper-yan26y)
- <a id="zhou26e-evaluation"></a>[Characterizing Vision-Language-Action Models across XPUs: Constraints and Acceleration for On-Robot Deployment](../conferences/icml-2026/cards/6101-6200.md#paper-zhou26e)
- <a id="zhou26az-evaluation"></a>[Dismantling the Illusion of Vision-Language-Action Models Competence via Explicit Distributional Shifts](../conferences/icml-2026/cards/6201-6300.md#paper-zhou26az)
- <a id="tian26o-evaluation"></a>[Position: Good Embodied Reward Models Need Bad Behavior Data](../conferences/icml-2026/cards/6501-6552.md#paper-tian26o)

<a id="by-theory-statistics"></a>

### 理论与统计

- <a id="francis-meretzki26a-theory-statistics"></a>[Temporal Difference Calibration in Sequential Tasks: Application to Vision-Language-Action Models](../conferences/icml-2026/cards/1101-1200.md#paper-francis-meretzki26a)
- <a id="stein26a-theory-statistics"></a>[Well-Posed KL-Regularized Control via Wasserstein and Kalman–Wasserstein KL Divergences](../conferences/icml-2026/cards/4201-4300.md#paper-stein26a)
- <a id="teng26a-theory-statistics"></a>[Embedding Hybrid Systems into Continuous Latent Vector Fields](../conferences/icml-2026/cards/4401-4500.md#paper-teng26a)
- <a id="teutsch26a-theory-statistics"></a>[On Uniform Error Bounds for Kernel Regression under Non-Gaussian Noise](../conferences/icml-2026/cards/4401-4500.md#paper-teutsch26a)
- <a id="zhou26au-theory-statistics"></a>[Neural Vector Lyapunov–Razumikhin Certificates for Delayed Interconnected Systems](../conferences/icml-2026/cards/6201-6300.md#paper-zhou26au)
<!-- classification:end -->
