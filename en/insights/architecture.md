# Architectures

[Home](../../README.en.md) · [Contributing](../CONTRIBUTING.md) · [简体中文](../../insights/architecture.md)

Model-wide design and information flow.

<!-- classification:start -->
## Browse by Research Domain

[Large Language Models](#by-llm) · [Computer Vision](#by-computer-vision) · [Natural Language Processing](#by-nlp) · [Reinforcement Learning](#by-reinforcement-learning) · [Robotics](#by-robotics) · [Multimodal Learning](#by-multimodal) · [Machine Learning Foundations and Statistics](#by-ml-foundations) · [Graph Learning and Recommendation](#by-graph-and-recommendation) · [Scientific Machine Learning](#by-scientific-ml)

<a id="by-llm"></a>

### Large Language Models

- [Set Diffusion: Interpolating Token Orderings between Autoregression and Diffusion for Fast and Flexible Decoding](../../conferences/icml-2026/cards/0101-0200.md#arriola26a-architecture) · 中文
- [HiMAP-Travel: Hierarchical Multi-Agent Planning for Long-Horizon Constrained Travel](../../conferences/icml-2026/cards/0301-0400.md#bui26b-architecture) · 中文
- [MARS: Modular Agent with Reflective Search for Automated AI Research](../../conferences/icml-2026/cards/0401-0500.md#chen26r-architecture) · 中文
- [LoKiFormer: Locality-aware Attention with Decoupled Knowledge Memory for Efficient Large Language Model Pretraining](../../conferences/icml-2026/cards/0501-0600.md#chen26cg-architecture) · 中文
- [Multi-Head LatentMoE and Head Parallel: Communication-Efficient and Deterministic MoE Parallelism](../../conferences/icml-2026/cards/0701-0800.md#cui26c-architecture) · 中文
- [Context-level Language Modeling by Learning Predictive Context Embeddings](../../conferences/icml-2026/cards/0801-0900.md#dai26g-architecture) · 中文
- [Neural Attention Search Linear: Towards Adaptive Token-Level Hybrid Attention Models](../../conferences/icml-2026/cards/0801-0900.md#deng26v-architecture) · 中文
- [Revisiting Efficiency–Accuracy Scaling in Mixture-of-Experts Architectures](../../conferences/icml-2026/cards/1001-1100.md#elango26a-architecture) · 中文
- [Trading Complexity for Expressivity Through Structured Generalized Linear Token Mixing](../../conferences/icml-2026/cards/1001-1100.md#fagnou26a-architecture) · 中文
- [Artificial Hippocampus Networks for Efficient Long-Context Modeling](../../conferences/icml-2026/cards/1001-1100.md#fang26w-architecture) · 中文
- [Think-at-Hard: Dynamic Looped Transformers for Improved Reasoning](../../conferences/icml-2026/cards/1101-1200.md#fu26t-architecture) · 中文
- [Caracal: Causal Architecture via Spectral Mixing](../../conferences/icml-2026/cards/1101-1200.md#gan26c-architecture) · 中文
- [SD-MoE: Spectral Decomposition for Effective Expert Specialization](../../conferences/icml-2026/cards/1601-1700.md#huang26i-architecture) · 中文
- [Equilibrium Reasoners: Learning Attractors Enables Scalable Reasoning](../../conferences/icml-2026/cards/1601-1700.md#huang26l-architecture) · 中文
- [MDN: Parallelizing Stepwise Momentum for Delta Linear Attention](../../conferences/icml-2026/cards/1701-1800.md#huang26af-architecture) · 中文
- [MAS-Architect: Declarative Multi-Agent System Design via Separation of Concerns](../../conferences/icml-2026/cards/1701-1800.md#huang26by-architecture) · 中文
- [ConceptMoE: Adaptive Token-to-Concept Compression for Implicit Compute Allocation](../../conferences/icml-2026/cards/1701-1800.md#huang26cl-architecture) · 中文
- [MatchFixAgent: Language-Agnostic Autonomous Repository-Level Code Translation Validation and Repair](../../conferences/icml-2026/cards/1801-1900.md#ibrahimzada26a-architecture) · 中文
- [MemoryLLM: Plug-n-Play Interpretable Feed-Forward Memory for Transformers](../../conferences/icml-2026/cards/1801-1900.md#jaiswal26a-architecture) · 中文
- [Text Generation as Continuous Latent Dynamics via Reinforcement Learning](../../conferences/icml-2026/cards/1801-1900.md#jia26h-architecture) · 中文
- [BRIDGE: Triangular Fixed-Point Refinement for Long-Horizon Persona Consistency](../../conferences/icml-2026/cards/1901-2000.md#jiang26aw-architecture) · 中文
- [From Growing to Looping: A Unified View of Iterative Computation in LLMs](../../conferences/icml-2026/cards/2001-2100.md#kapl26a-architecture) · 中文
- [Do Transformers Need Three Projections? Systematic Study of QKV Variants](../../conferences/icml-2026/cards/2001-2100.md#kayyam26a-architecture) · 中文
- [PolySAE: Modeling Feature Interactions in Sparse Autoencoders via Polynomial Decoding](../../conferences/icml-2026/cards/2201-2300.md#koromilas26a-architecture) · 中文
- [SiameseNorm: Breaking the Barrier to Reconciling Pre/Post-Norm](../../conferences/icml-2026/cards/2401-2500.md#li26ba-architecture) · 中文
- [Breaking the Factorization Barrier in Diffusion Language Models](../../conferences/icml-2026/cards/2501-2600.md#li26fd-architecture) · 中文
- [OpenSage: Self-programming Agent Generation Engine](../../conferences/icml-2026/cards/2501-2600.md#li26gk-architecture) · 中文
- [RePo: Language Models with Context Re-Positioning](../../conferences/icml-2026/cards/2601-2700.md#li26jq-architecture) · 中文
- [$R^3$DAO: Reactive Recovery and Reconstruction for Long-horizon Data Agent Orchestration](../../conferences/icml-2026/cards/2801-2900.md#liu26at-architecture) · 中文
- [Thoughtbubbles: an Unsupervised Method for Parallel Thinking in Latent Space](../../conferences/icml-2026/cards/2801-2900.md#liu26cx-architecture) · 中文
- [SimpleMem: Efficient Lifelong Memory for LLM Agents](../../conferences/icml-2026/cards/2901-3000.md#liu26dx-architecture) · 中文
- [SHINE: A Scalable In-Context Hypernetwork for Mapping Context to LoRA in a Single Pass](../../conferences/icml-2026/cards/2901-3000.md#liu26ek-architecture) · 中文
- [HyperMLP: An Integrated Perspective for Sequence Modeling](../../conferences/icml-2026/cards/3001-3100.md#lu26aq-architecture) · 中文
- [Little By Little: Continual Learning via Incremental Mixture of Rank-1 Associative Memory Experts](../../conferences/icml-2026/cards/3001-3100.md#lu26au-architecture) · 中文
- [Head-in-Head in Linear Attention](../../conferences/icml-2026/cards/3201-3300.md#mei26a-architecture) · 中文
- [Skill-Pro: Learning Reusable Skills from Experience via Non-Parametric PPO for LLM Agents](../../conferences/icml-2026/cards/3201-3300.md#mi26d-architecture) · 中文
- [Turbo Connection: Reasoning as Information Flow from Higher to Lower Layers](../../conferences/icml-2026/cards/3301-3400.md#mohan26b-architecture) · 中文
- [Rational Transductors](../../conferences/icml-2026/cards/3301-3400.md#mohri26a-architecture) · 中文
- [Push, Pop, Parallelize: Stack-Augmented Linear Attention via the Delta Rule](../../conferences/icml-2026/cards/3401-3500.md#nguyen26i-architecture) · 中文
- [MaMa: A Game-Theoretic Approach for Designing Safe Agentic Systems](../../conferences/icml-2026/cards/3401-3500.md#nother26a-architecture) · 中文
- [TsLLM: Augmenting LLMs for General Time Series Understanding and Prediction](../../conferences/icml-2026/cards/3601-3700.md#parker26a-architecture) · 中文
- [Esoteric Language Models: A Family of Any-Order Diffusion LLMs](../../conferences/icml-2026/cards/3901-4000.md#sahoo26b-architecture) · 中文
- [Kalman Linear Attention: Parallel Bayesian Filtering For Efficient Language Modeling and State Tracking](../../conferences/icml-2026/cards/4001-4100.md#shaj26a-architecture) · 中文
- [A Tale of Two Graphs: Separating Knowledge Exploration from Outline Structure for Open-Ended Deep Research](../../conferences/icml-2026/cards/4101-4200.md#shi26n-architecture) · 中文
- [OmniMoE: An Efficient MoE by Orchestrating Atomic Experts at Scale](../../conferences/icml-2026/cards/4101-4200.md#shi26q-architecture) · 中文
- [Causal Attention with Lookahead Keys](../../conferences/icml-2026/cards/4201-4300.md#song26y-architecture) · 中文

<a id="by-computer-vision"></a>

### Computer Vision

- [VideoFlexTok: Flexible-Length Coarse-to-Fine Video Tokenization](../../conferences/icml-2026/cards/0101-0200.md#atanov26a-architecture) · 中文
- [Latent Forcing: Reordering the Diffusion Trajectory for Pixel-Space Image Generation](../../conferences/icml-2026/cards/0101-0200.md#baade26a-architecture) · 中文
- [Envisioning Beyond the Few: Disentangled Semantics and Primitives for Few-Shot Atypical Layout-to-Image Generation](../../conferences/icml-2026/cards/0201-0300.md#bao26f-architecture) · 中文
- [Autoregression with Self-Token Prediction](../../conferences/icml-2026/cards/0501-0600.md#chen26du-architecture) · 中文
- [Phy-CoSF: Physics-Guided Continuous Spectral Fields Reconstruction and Spectral Super-Resolution for Snapshot Compressive Imaging](../../conferences/icml-2026/cards/0601-0700.md#chen26ga-architecture) · 中文
- [SpaCeFormer: Fast Proposal-Free Open-Vocabulary 3D Instance Segmentation](../../conferences/icml-2026/cards/0701-0800.md#choy26a-architecture) · 中文
- [Native Spatio-Temporal 4D Variational Autoencoder](../../conferences/icml-2026/cards/0901-1000.md#ding26u-architecture) · 中文
- [Discontinuous Galerkin Neural Operator for Pathology Defocus Deblurring](../../conferences/icml-2026/cards/0901-1000.md#duan26e-architecture) · 中文
- [CODiff: One-Step Diffusion Model for Camouflaged Object Detection](../../conferences/icml-2026/cards/1101-1200.md#fu26l-architecture) · 中文
- [DecomPose: Disentangling Cross-Category Optimization Contention for Category-Level 6D Object Pose Estimation](../../conferences/icml-2026/cards/1201-1300.md#gao26aq-architecture) · 中文
- [Beyond Pixel Histories: World Models with Persistent 3D State](../../conferences/icml-2026/cards/1201-1300.md#garcin26a-architecture) · 中文
- [Direct 3D-Aware Object Insertion via Decomposed Visual Proxies](../../conferences/icml-2026/cards/1301-1400.md#gong26f-architecture) · 中文
- [OmniAID: Decoupling Semantics and Artifacts for Universal AI-Generated Image Detection in the Wild](../../conferences/icml-2026/cards/1401-1500.md#guo26ag-architecture) · 中文
- [Bridging Local–Global Dissonance: Learning from Compressive Measurements for Hyperspectral Reconstruction](../../conferences/icml-2026/cards/1401-1500.md#han26c-architecture) · 中文
- [ViTok-v2: Scaling Native Resolution Autoencoders to 5 Billion Parameters](../../conferences/icml-2026/cards/1401-1500.md#hansen-estruch26a-architecture) · 中文
- [Partial Ring Scan: Revisiting Scan Order in Vision State Space Models](../../conferences/icml-2026/cards/1601-1700.md#hsieh26a-architecture) · 中文
- [Continuous Viewpoint Adaptation for Single View 3D Object Reconstruction](../../conferences/icml-2026/cards/1701-1800.md#hwang26f-architecture) · 中文
- [Rays as Pixels: Learning A Joint Distribution of Videos and Camera Trajectories](../../conferences/icml-2026/cards/1801-1900.md#jang26f-architecture) · 中文
- [Towards Effective Waste Segmentation for Automated Waste Recycling in Cluttered Background](../../conferences/icml-2026/cards/1801-1900.md#javaid26a-architecture) · 中文
- [CoD-Lite: Real-Time Diffusion-Based Generative Image Compression](../../conferences/icml-2026/cards/1801-1900.md#jia26i-architecture) · 中文
- [CRAG: Can 3D Generative Models Help 3D Assembly?](../../conferences/icml-2026/cards/1901-2000.md#jiang26ab-architecture) · 中文
- [Visual Implicit Autoregressive Modeling](../../conferences/icml-2026/cards/1901-2000.md#jiang26ah-architecture) · 中文
- [StructMamPose: From Sequential Perception to Structural Reasoning for 3D Human Pose Estimation](../../conferences/icml-2026/cards/1901-2000.md#jiang26bb-architecture) · 中文
- [A Deep Learning Model of Mental Rotation Informed by Interactive VR Experiments](../../conferences/icml-2026/cards/2001-2100.md#khazoum26a-architecture) · 中文
- [PhysHanDI: Physics-Based Reconstruction of Hand-Deformable Object Interactions](../../conferences/icml-2026/cards/2301-2400.md#lee26ao-architecture) · 中文
- [Synergistic Space-Vision Processing for Predicate Inference](../../conferences/icml-2026/cards/2301-2400.md#lei26b-architecture) · 中文
- [LayerT2V: A Unified Multi-Layer Video Generation Framework](../../conferences/icml-2026/cards/2401-2500.md#li26l-architecture) · 中文
- [DroneDINO: Towards Heterogeneous Routed Mixture of Experts for Drone-based Unified Object Detection](../../conferences/icml-2026/cards/2401-2500.md#li26o-architecture) · 中文
- [OcclusionFormer: Arranging Z-Order for Layout-Grounded Image Generation](../../conferences/icml-2026/cards/2401-2500.md#li26ah-architecture) · 中文
- [TransNormal: Dense Visual Semantics for Diffusion-based Transparent Object Normal Estimation](../../conferences/icml-2026/cards/2401-2500.md#li26ao-architecture) · 中文
- [Linearizing Vision Transformer with Test-Time Training](../../conferences/icml-2026/cards/2401-2500.md#li26bc-architecture) · 中文
- [DGG-HMR: Multi-Person Human Mesh Recovery with Depth-Guided Geometric Anchoring](../../conferences/icml-2026/cards/2401-2500.md#li26bq-architecture) · 中文
- [SegPVSG: Panoptic Video Scene Graph Generation via Temporal Focusing and Generative Augmentation](../../conferences/icml-2026/cards/2401-2500.md#li26bx-architecture) · 中文
- [Solving Spatial-Spectral Fusion with Latent Spectral Operators](../../conferences/icml-2026/cards/2501-2600.md#li26en-architecture) · 中文
- [Towards Trustworthy and Identifiable Virtual Face Generation](../../conferences/icml-2026/cards/2501-2600.md#li26gt-architecture) · 中文
- [LaRI: Layered Ray Intersections for Single-view 3D Geometric Reasoning](../../conferences/icml-2026/cards/2601-2700.md#li26jg-architecture) · 中文
- [Hyperspectral Image Fusion with Spectral-Band and Fusion-Scale Agnosticism](../../conferences/icml-2026/cards/2601-2700.md#liang26c-architecture) · 中文
- [Spike-HTR: Spiking Neural Transformer for Handwritten Text Recognition](../../conferences/icml-2026/cards/2601-2700.md#liang26j-architecture) · 中文
- [RealisMotion: Decomposed Human Motion Control and Video Generation in the World Space](../../conferences/icml-2026/cards/2701-2800.md#liang26ad-architecture) · 中文
- [WorldMirror: Universal 3D World Reconstruction with Any-Prior Prompting](../../conferences/icml-2026/cards/2801-2900.md#liu26cw-architecture) · 中文
- [Spiral RoPE: Rotate Your Rotary Positional Embeddings in the 2D Plane](../../conferences/icml-2026/cards/2801-2900.md#liu26dj-architecture) · 中文
- [Resolving Blind Inverse Problems under Dynamic Range Compression via Structured Forward Operator Modeling](../../conferences/icml-2026/cards/2901-3000.md#liu26eb-architecture) · 中文
- [FastSESR: Fast Scene-level Explicit Surface Reconstruction](../../conferences/icml-2026/cards/2901-3000.md#liu26gs-architecture) · 中文
- [Learning Stochastic Bridges for Video Object Removal via Video-to-Video Translation](../../conferences/icml-2026/cards/2901-3000.md#lou26b-architecture) · 中文
- [Scaling Continual Learning to 300+ Tasks with Bi-Level Routing Mixture-of-Experts](../../conferences/icml-2026/cards/2901-3000.md#lou26c-architecture) · 中文
- [MotionMAR: Multi-scale Auto-Regressive Human Motion Reconstruction from Sparse Observations](../../conferences/icml-2026/cards/3001-3100.md#luo26af-architecture) · 中文
- [4RC: 4D Reconstruction via Conditional Querying Anytime and Anywhere](../../conferences/icml-2026/cards/3001-3100.md#luo26al-architecture) · 中文
- [Bio-Vision-Inspired Spiking Neural Networks for Object Detection with Event Cameras](../../conferences/icml-2026/cards/3101-3200.md#ma26x-architecture) · 中文
- [CodeMamba: Shifting from Target Semantics to Self-Supervised Background Manifold Learning for Singularity Detection in Infrared Sequences](../../conferences/icml-2026/cards/3101-3200.md#ma26au-architecture) · 中文
- [Compass-RoPE: Isotropic Rotary Position Embeddings for Vision Transformers](../../conferences/icml-2026/cards/3301-3400.md#min26f-architecture) · 中文
- [GEM-FI: Gated Evidential Mixtures with Fisher Modulation](../../conferences/icml-2026/cards/3301-3400.md#mohammed26a-architecture) · 中文
- [Learning Global Representation from Queries for Vectorized HD Map Construction](../../conferences/icml-2026/cards/3701-3800.md#qiu26m-architecture) · 中文
- [Pair2Scene: Learning Local Object Relations for Procedural Scene Generation](../../conferences/icml-2026/cards/3801-3900.md#ran26d-architecture) · 中文
- [Scalable Event Cloud Network for Event-based Classification](../../conferences/icml-2026/cards/3801-3900.md#ren26j-architecture) · 中文
- [SphericalDreamer: Generating Navigable Immersive 3D Worlds with Panorama Fusion](../../conferences/icml-2026/cards/3901-4000.md#schnepf26a-architecture) · 中文
- [TEFormer: Structured Bidirectional Temporal Enhancement Modeling in Spiking Transformers](../../conferences/icml-2026/cards/4001-4100.md#shen26l-architecture) · 中文
- [Trainable Nonexpansive Denoisers for Contractive Image Reconstruction](../../conferences/icml-2026/cards/4101-4200.md#sinha26a-architecture) · 中文

<a id="by-nlp"></a>

### Natural Language Processing

- [Separating Representation from Reconstruction Enables Scalable Text Encoders](../../conferences/icml-2026/cards/0801-0900.md#dervishi26a-architecture) · 中文
- [Scaling Transformers for End-to-End Discrete Audio Tokenization](../../conferences/icml-2026/cards/1301-1400.md#gong26c-architecture) · 中文
- [Unifying Masked Diffusion Models with Various Generation Orders and Beyond](../../conferences/icml-2026/cards/1501-1600.md#hong26f-architecture) · 中文
- [Names Don’t Matter: Symbol-Invariant Transformer for Open-Vocabulary Learning](../../conferences/icml-2026/cards/1801-1900.md#isik26a-architecture) · 中文
- [AgentSteerTTS: A Multi-Agent Closed-Loop Framework for Composite-Instruction Text-to-Speech](../../conferences/icml-2026/cards/2001-2100.md#kang26p-architecture) · 中文
- [Smoothie: Smoothing Diffusion on Token Embeddings for Text Generation](../../conferences/icml-2026/cards/4001-4100.md#shabalin26a-architecture) · 中文

<a id="by-reinforcement-learning"></a>

### Reinforcement Learning

- [RN-D: Discretized Categorical Actors for On-Policy Reinforcement Learning](../../conferences/icml-2026/cards/0201-0300.md#bian26a-architecture) · 中文
- [VJEPA: Variational Joint Embedding Predictive Architectures as Probabilistic World Models](../../conferences/icml-2026/cards/1701-1800.md#huang26ba-architecture) · 中文
- [Mitigating Plasticity Loss through Architectural Design in Continual Learning](../../conferences/icml-2026/cards/2101-2200.md#koeppe26a-architecture) · 中文
- [Differentiable Weightless Controllers: Learning Logic Circuits for Continuous Control](../../conferences/icml-2026/cards/2201-2300.md#kresse26a-architecture) · 中文
- [QHyer: Q-conditioned Hybrid Attention-mamba Transformer for Offline Goal-conditioned RL](../../conferences/icml-2026/cards/2301-2400.md#lei26g-architecture) · 中文
- [ScaleMoE: Mixture-of-Experts for Scalable Continuous Control in Actor-Critic Reinforcement Learning](../../conferences/icml-2026/cards/3101-3200.md#ma26an-architecture) · 中文
- [Scalable Traffic Signal Control with Shared Policy Framework](../../conferences/icml-2026/cards/3101-3200.md#ma26az-architecture) · 中文
- [This State Looks Like That: Self-Interpretable Reinforcement Learning Agents using Prototype Soft Actor-Critic](../../conferences/icml-2026/cards/3201-3300.md#marzo26a-architecture) · 中文
- [Path-dependent Discrete Amortized Inference](../../conferences/icml-2026/cards/4101-4200.md#silva26a-architecture) · 中文

<a id="by-robotics"></a>

### Robotics

- [Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models](../../conferences/icml-2026/cards/0101-0200.md#bai26h-architecture) · 中文
- [Hierarchical Policy Learning via Spectral Decomposition](../../conferences/icml-2026/cards/0401-0500.md#cao26u-architecture) · 中文
- [The Lie We Tell: Correcting the Euclidean Fallacy in Vision Language Action Policies via Score Matching on Tangent Space](../../conferences/icml-2026/cards/0701-0800.md#chuang26a-architecture) · 中文
- [Embodied-DETR: End-to-End Temporal 3D Object Detection in Egocentric Views](../../conferences/icml-2026/cards/0901-1000.md#ding26x-architecture) · 中文
- [From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model](../../conferences/icml-2026/cards/1601-1700.md#hu26ad-architecture) · 中文
- [SoMA: A Real-to-Sim Neural Simulator for Robotic Soft-Body Manipulation](../../conferences/icml-2026/cards/1701-1800.md#huang26bh-architecture) · 中文
- [AutoMoT: A Unified Vision-Language-Action Model with Asynchronous Mixture -of-Transformers for End-to-End Autonomous Driving](../../conferences/icml-2026/cards/1701-1800.md#huang26cb-architecture) · 中文
- [HiMe: Hierarchical Embodied Memory for Long-Horizon Vision-Language-Action Control](../../conferences/icml-2026/cards/1801-1900.md#ji26k-architecture) · 中文
- [DriveWorld-VLA: Unified Latent-Space World Modeling with Vision–Language–Action for Autonomous Driving](../../conferences/icml-2026/cards/1801-1900.md#jia26f-architecture) · 中文
- [VectorWorld: Efficient Streaming World Model via Diffusion Flow on Vector Graphs](../../conferences/icml-2026/cards/1901-2000.md#jiang26bf-architecture) · 中文
- [Sentinel-VLA: A Metacognitive VLA Model with Active Status Monitoring for Dynamic Reasoning and Error Recovery](../../conferences/icml-2026/cards/2501-2600.md#li26fm-architecture) · 中文
- [DECO: Decoupled Multimodal Diffusion Transformer for Bimanual Dexterous Manipulation with a Plugin Tactile Adapter](../../conferences/icml-2026/cards/2501-2600.md#li26fs-architecture) · 中文
- [Structured 4D Latent Predictive Model for Robot Planning](../../conferences/icml-2026/cards/2601-2700.md#li26hk-architecture) · 中文
- [RoboFlow4D: A Lightweight Flow World Model Toward Real-Time Flow-Guided Robotic Manipulation](../../conferences/icml-2026/cards/2701-2800.md#lin26g-architecture) · 中文
- [MSP: Probabilistically Consistent Multi-Scale Action Generation](../../conferences/icml-2026/cards/2701-2800.md#lin26ab-architecture) · 中文
- [GAE: Unleashing Physical Potential of VLM with Generalizable Action Expert](../../conferences/icml-2026/cards/2801-2900.md#liu26bf-architecture) · 中文
- [LaST$_0$: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model](../../conferences/icml-2026/cards/2801-2900.md#liu26ch-architecture) · 中文
- [Sample from What You See: Visuomotor Policy Learning via Diffusion Bridge with Observation-Embedded Stochastic Differential Equation](../../conferences/icml-2026/cards/2801-2900.md#liu26db-architecture) · 中文
- [Neural Implicit Action Fields: From Discrete Waypoints to Continuous Functions for Vision-Language-Action Models](../../conferences/icml-2026/cards/2901-3000.md#liu26gf-architecture) · 中文
- [PolyFlow: Safe and Efficient Polytope-Constrained Flow Matching with Constraint Embedding and Projection-free Update](../../conferences/icml-2026/cards/3101-3200.md#ma26ar-architecture) · 中文
- [DynVLA: Learning World Dynamics for Action Reasoning in Autonomous Driving](../../conferences/icml-2026/cards/4001-4100.md#shang26f-architecture) · 中文
- [HALO: A Unified Vision-Language-Action Model for Embodied Multimodal Chain-of-Thought Reasoning](../../conferences/icml-2026/cards/4101-4200.md#shou26a-architecture) · 中文
- [TF-FACE: Time-Frequency Fusion Learning via Frequency-Domain Adaptive and Controllable Enhancement for Trajectory Prediction](../../conferences/icml-2026/cards/4201-4300.md#song26q-architecture) · 中文

<a id="by-multimodal"></a>

### Multimodal Learning

- [Interactive Person Retrieval via Multi-Turn Multimodal Conversation](../../conferences/icml-2026/cards/0101-0200.md#bai26j-architecture) · 中文
- [Any2Any: Unified Arbitrary Modality Translation for Remote Sensing](../../conferences/icml-2026/cards/0601-0700.md#chen26go-architecture) · 中文
- [PhaseCoder: Microphone Geometry-Agnostic Spatial Audio Understanding for Multimodal LLMs](../../conferences/icml-2026/cards/0801-0900.md#dementyev26a-architecture) · 中文
- [Mixing Expertise with Confidence: A Mixture of Experts Framework for Robust Multi-Modal Continual Learning](../../conferences/icml-2026/cards/1101-1200.md#forhad26a-architecture) · 中文
- [DynaVieW: Schema-Guided World Modeling for Understanding Hierarchical Visual Dynamics](../../conferences/icml-2026/cards/1201-1300.md#gao26am-architecture) · 中文
- [DiffThinker: Towards Generative Multimodal Reasoning with Diffusion Models](../../conferences/icml-2026/cards/1501-1600.md#he26ac-architecture) · 中文
- [RVAS: Referring Video Active Exploration and Segmentation](../../conferences/icml-2026/cards/1601-1700.md#hu26q-architecture) · 中文
- [CG-MLLM: Captioning and Generating 3D content via Multi-modal Large Language Models](../../conferences/icml-2026/cards/1701-1800.md#huang26be-architecture) · 中文
- [SE-GA: Memory-Augmented Self-Evolution for GUI Agents](../../conferences/icml-2026/cards/1901-2000.md#jin26m-architecture) · 中文
- [Generative Visual Code Mobile World Models](../../conferences/icml-2026/cards/2101-2200.md#koh26a-architecture) · 中文
- [ReGen: Hierarchical Multi-Prompt Representation Generation for Efficient Waveform Diffusion Models](../../conferences/icml-2026/cards/2301-2400.md#lee26f-architecture) · 中文
- [Towards Streaming Synchronized Spatial Audio Generation via Autoregressive Diffusion Transformer](../../conferences/icml-2026/cards/2301-2400.md#lei26i-architecture) · 中文
- [DiasR: Dual-Modal Identity-Anchored Sparse Routing for Efficient Multi-Subject Video Generation](../../conferences/icml-2026/cards/2501-2600.md#li26df-architecture) · 中文
- [Omni-Diffusion: Unified Multimodal Understanding and Generation with Masked Discrete Diffusion](../../conferences/icml-2026/cards/2501-2600.md#li26dv-architecture) · 中文
- [SMM Transformer: Leveraging Spiking Neural Networks for Multimodal Tasks](../../conferences/icml-2026/cards/2601-2700.md#liang26i-architecture) · 中文
- [AnyMod-LLVE: Low-Light Video Enhancement with Modality-Agnostic Inference](../../conferences/icml-2026/cards/2601-2700.md#liang26k-architecture) · 中文
- [TiMi: Empower Time Series Transformers with Multimodal Mixture of Experts](../../conferences/icml-2026/cards/2701-2800.md#lin26al-architecture) · 中文
- [Deep Residual Injection for Full-Spectrum Forensic Signal Perception in Multimodal Large Language Models](../../conferences/icml-2026/cards/2701-2800.md#lin26an-architecture) · 中文
- [GeoSense: Internalizing Geometric Necessity Perception for Multimodal Reasoning](../../conferences/icml-2026/cards/2801-2900.md#liu26as-architecture) · 中文
- [JAEGER: Joint 3D Audio-Visual Grounding and Reasoning in Simulated Physical Environments](../../conferences/icml-2026/cards/2901-3000.md#liu26ea-architecture) · 中文
- [CoME: Empowering Channel-of-Mobile-Experts with Informative Hybrid-Capabilities Reasoning](../../conferences/icml-2026/cards/2901-3000.md#liu26fc-architecture) · 中文
- [MoST: Mixing Speech and Text with Modality-Aware Mixture of Experts](../../conferences/icml-2026/cards/2901-3000.md#lou26h-architecture) · 中文
- [Group Cognition Learning: Making Everything Better Through Governed Two-Stage Agents Collaboration](../../conferences/icml-2026/cards/3201-3300.md#meng26a-architecture) · 中文
- [Darwinian Memory: A Training-Free Self-Regulating Memory System for GUI Agent Evolution](../../conferences/icml-2026/cards/3201-3300.md#mi26b-architecture) · 中文
- [Unified Multimodal Autoregressive Modeling with Shared Context—Visual Tokenizer is Key to Unification](../../conferences/icml-2026/cards/3601-3700.md#peng26k-architecture) · 中文
- [SVL: Empowering Spiking Neural Networks for Efficient 3D Open-World Understanding](../../conferences/icml-2026/cards/3701-3800.md#qiu26g-architecture) · 中文
- [LaTtE-Flow: Layerwise Timestep-Expert Flow-based Transformer](../../conferences/icml-2026/cards/4001-4100.md#shen26w-architecture) · 中文

<a id="by-ml-foundations"></a>

### Machine Learning Foundations and Statistics

- [A Spiking Heterogeneous Harmonic Resonate-and-Fire State Space Model for Time Series](../../conferences/icml-2026/cards/0001-0100.md#agrawal26c-architecture) · 中文
- [Falling Trees: A Model Class for Interpretable Risk Prioritization](../../conferences/icml-2026/cards/0101-0200.md#babbar26a-architecture) · 中文
- [Learning to Theorize the World from Observation](../../conferences/icml-2026/cards/0101-0200.md#baek26b-architecture) · 中文
- [Who Said Neural Networks Aren’t Linear?](../../conferences/icml-2026/cards/0201-0300.md#berman26c-architecture) · 中文
- [M-Star: Markovian Projection of Star-Shaped Diffusion for Exponential Family Distributions](../../conferences/icml-2026/cards/0201-0300.md#bertholom26a-architecture) · 中文
- [Deep Flow Networks](../../conferences/icml-2026/cards/0301-0400.md#candogan26b-architecture) · 中文
- [Probabilistically-routed Bayesian Additive Spanning Trees for Learning on Constrained Domains](../../conferences/icml-2026/cards/0401-0500.md#chakraborty26a-architecture) · 中文
- [Independent Component Discovery in Temporal Count Data](../../conferences/icml-2026/cards/0401-0500.md#chaussard26a-architecture) · 中文
- [CoGenCast: A Coupled Autoregressive–Flow Generative Framework for Time Series Forecasting](../../conferences/icml-2026/cards/0601-0700.md#cheng26h-architecture) · 中文
- [KITE: Knowledge-Guided Probabilistic Modeling for Time Series Forecasting with Exogenous Variables](../../conferences/icml-2026/cards/0601-0700.md#cheng26t-architecture) · 中文
- [Transformer Circuits Can Realize Clustering Algorithms](../../conferences/icml-2026/cards/0701-0800.md#clarkson26a-architecture) · 中文
- [Mixture of Concept Bottleneck Experts](../../conferences/icml-2026/cards/0801-0900.md#de-santis26a-architecture) · 中文
- [FedEMoE: Improving Personalization on Heterogeneous Federated Learning via Elastic Mixture of Experts Architecture](../../conferences/icml-2026/cards/0901-1000.md#du26d-architecture) · 中文
- [Rethinking Time-Series Imputation as Conditional Inference along Temporal Evolution](../../conferences/icml-2026/cards/1001-1100.md#fan26h-architecture) · 中文
- [Dynamic Fractal Mamba: A Neural Renormalization Group Flow for Scale-Invariant Sequence Modeling](../../conferences/icml-2026/cards/1001-1100.md#fang26p-architecture) · 中文
- [Symbol-Equivariant Recurrent Reasoning Models](../../conferences/icml-2026/cards/1101-1200.md#freinschlag26a-architecture) · 中文
- [Analytic Bijections for Smooth and Interpretable Normalizing Flows](../../conferences/icml-2026/cards/1201-1300.md#gerdes26a-architecture) · 中文
- [FlowState: Sampling-Rate-Equivariant Time-Series Forecasting](../../conferences/icml-2026/cards/1301-1400.md#graf26a-architecture) · 中文
- [Learning Permutation Distributions via Reflected Diffusion on Ranks](../../conferences/icml-2026/cards/1501-1600.md#he26ax-architecture) · 中文
- [TeamWork: Multivariate Time Series Anomaly Detection via Asymmetric Role-aware Channel Modeling](../../conferences/icml-2026/cards/1601-1700.md#hu26bf-architecture) · 中文
- [A General Neural Backbone for Mixed-Integer Linear Optimization via Dual Attention](../../conferences/icml-2026/cards/1701-1800.md#huang26bl-architecture) · 中文
- [DiScoFormer: Plug-In Density and Score Estimation with Transformers](../../conferences/icml-2026/cards/1801-1900.md#ilin26a-architecture) · 中文
- [Platonic Transformers: A Solid Choice For Equivariance](../../conferences/icml-2026/cards/1801-1900.md#islam26a-architecture) · 中文
- [PRISM: Parallel Residual Iterative Sequence Model](../../conferences/icml-2026/cards/1901-2000.md#jiang26e-architecture) · 中文
- [Gradient-Based Causal Tree Ensembles: A Backbone Architecture for Heterogeneous Treatment Effects](../../conferences/icml-2026/cards/2001-2100.md#kano26a-architecture) · 中文
- [Interpretable Discovery of One-parameter Subgroups: A Modular Framework for Elliptical, Hyperbolic, and Parabolic Symmetries](../../conferences/icml-2026/cards/2001-2100.md#karjol26a-architecture) · 中文
- [NNiT: Width-Agnostic Neural Network Generation with Structurally Aligned Weight Spaces](../../conferences/icml-2026/cards/2101-2200.md#kim26ay-architecture) · 中文
- [Equivariant Neural Networks for General Linear Symmetries on Lie Algebras](../../conferences/icml-2026/cards/2101-2200.md#kim26ca-architecture) · 中文
- [Expand Neurons, Not Parameters](../../conferences/icml-2026/cards/2101-2200.md#kong26f-architecture) · 中文
- [Learning High-Dimensional Parity Functions with Product Networks using Gradient Descent](../../conferences/icml-2026/cards/2201-2300.md#larue26a-architecture) · 中文
- [Generalizing Multi-Scale Time-Series Modeling with a Single Operator](../../conferences/icml-2026/cards/2301-2400.md#lee26al-architecture) · 中文
- [FRACTAL: State Space Model with Fractional Recurrent Architecture for Computational Temporal Analysis of Long Sequences](../../conferences/icml-2026/cards/2401-2500.md#li26cx-architecture) · 中文
- [MIMOMamba: From Scalar Duality to Matrix-Valued Attention](../../conferences/icml-2026/cards/2501-2600.md#li26ft-architecture) · 中文
- [Test-Time Training with KV Binding Is Secretly Linear Attention](../../conferences/icml-2026/cards/2801-2900.md#liu26ae-architecture) · 中文
- [PULSE: Generative Phase Evolution for Non-Stationary Time Series Forecasting](../../conferences/icml-2026/cards/2801-2900.md#liu26dn-architecture) · 中文
- [LIF Recurrent Memory Enables Long-Horizon Spiking Computation](../../conferences/icml-2026/cards/2801-2900.md#liu26do-architecture) · 中文
- [TabSwift: An Efficient Tabular Foundation Model with Row-Wise Attention](../../conferences/icml-2026/cards/2901-3000.md#liu26fm-architecture) · 中文
- [Balancing Understanding and Generation in Discrete Diffusion Models](../../conferences/icml-2026/cards/2901-3000.md#liu26gi-architecture) · 中文
- [ReNF: Rethinking the Design of Neural Long-Term Time Series Forecasters](../../conferences/icml-2026/cards/3001-3100.md#lu26w-architecture) · 中文
- [LassoFlexNet: a Flexible Neural Architecture for Tabular Data](../../conferences/icml-2026/cards/3001-3100.md#lui26a-architecture) · 中文
- [Convolutional Learnable-Group Weightless Neural Network](../../conferences/icml-2026/cards/3101-3200.md#ma26e-architecture) · 中文
- [Revisiting Neural Processes via Fourier Transform and Volterra Series](../../conferences/icml-2026/cards/3301-3400.md#mohseni26a-architecture) · 中文
- [Incremental Transformer Neural Processes](../../conferences/icml-2026/cards/3301-3400.md#mortimer26a-architecture) · 中文
- [Cascaded Flow Matching for Heterogeneous Tabular Data with Mixed-Type Features](../../conferences/icml-2026/cards/3301-3400.md#mueller26a-architecture) · 中文
- [Cluster-Aware Causal Mixer for Online Anomaly Detection in Multivariate Time Series](../../conferences/icml-2026/cards/3301-3400.md#murad26a-architecture) · 中文
- [gp2Scale: A Class of Compactly Supported Non-Stationary Kernels and Distributed Computing for Exact Gaussian Processes on 10 Million Data Points](../../conferences/icml-2026/cards/3401-3500.md#noack26a-architecture) · 中文
- [Skipping the Zeros in Diffusion Models for Sparse Data Generation](../../conferences/icml-2026/cards/3501-3600.md#ostheimer26a-architecture) · 中文
- [SoftBinary Coding: A New Information-Theoretic Paradigm for Neural Compression via Fast Channel Simulation](../../conferences/icml-2026/cards/3501-3600.md#ozyilkan26a-architecture) · 中文
- [CauScale: Neural Causal Discovery at Scale](../../conferences/icml-2026/cards/3601-3700.md#peng26c-architecture) · 中文
- [ParalESN: Enabling parallel information processing in Reservoir Computing](../../conferences/icml-2026/cards/3601-3700.md#pinna26a-architecture) · 中文
- [CANDI: Hybrid Discrete-Continuous Diffusion Models](../../conferences/icml-2026/cards/3601-3700.md#pynadath26a-architecture) · 中文
- [SEER: Transformer-based Robust Time Series Forecasting via Automated Patch Enhancement and Replacement](../../conferences/icml-2026/cards/3701-3800.md#qiu26n-architecture) · 中文
- [Bridging Time and Frequency: A Joint Modeling Framework for Irregular Multivariate Time Series Forecasting](../../conferences/icml-2026/cards/3701-3800.md#qiu26t-architecture) · 中文
- [Evidential Copula Concept Embedding Models](../../conferences/icml-2026/cards/3701-3800.md#qiu26u-architecture) · 中文
- [DAG: A Dual Correlation Network for Time Series Forecasting with Exogenous Variables](../../conferences/icml-2026/cards/3701-3800.md#qiu26x-architecture) · 中文
- [TabICLv2: A Better, Faster, Scalable, and Open Tabular Foundation Model](../../conferences/icml-2026/cards/3701-3800.md#qu26a-architecture) · 中文
- [Efficient Neural Controlled Differential Equations via Attentive Kernel Smoothing](../../conferences/icml-2026/cards/4001-4100.md#serov26a-architecture) · 中文
- [TimeMRA: LLM-Empowered Time Series Forecasting via Multi-Scale Retrieval-Augmented Representations](../../conferences/icml-2026/cards/4001-4100.md#shang26b-architecture) · 中文
- [Infinite-Precision Autoregressive Modeling for Vector Graphics and Layouts](../../conferences/icml-2026/cards/4101-4200.md#shin26a-architecture) · 中文
- [Query-Based Asymmetric Modeling with Decoupled Input–Output Rates for Speech Restoration](../../conferences/icml-2026/cards/4101-4200.md#shin26c-architecture) · 中文
- [Geometry-Aware Probabilistic Circuits via Voronoi Tessellations](../../conferences/icml-2026/cards/4101-4200.md#sidheekh26a-architecture) · 中文
- [WaveSSM: Multiscale State-Space Models for Non-stationary Signal Attention](../../conferences/icml-2026/cards/4101-4200.md#solozabal26a-architecture) · 中文

<a id="by-graph-and-recommendation"></a>

### Graph Learning and Recommendation

- [RSF-GLLM: Bridging the Semantic Gap in Multi-Hop Knowledge Graph QA via Recurrent Soft-Flow and Decoupled LLM Generation](../../conferences/icml-2026/cards/0201-0300.md#bandyopadhyay26a-architecture) · 中文
- [OneSearch: A Preliminary Exploration of the Unified End-to-End Generative Framework for E-commerce Search](../../conferences/icml-2026/cards/0501-0600.md#chen26al-architecture) · 中文
- [Adaptive Memory Retention in Dynamic Graphs](../../conferences/icml-2026/cards/0801-0900.md#de-castelli26a-architecture) · 中文
- [Graph Neural Dynamics via Learned Energy and Tangential Flows](../../conferences/icml-2026/cards/1001-1100.md#eliasof26a-architecture) · 中文
- [MC-HNN: Learning Latent Structural Semantics and High-Rank Representations for Hypergraph Neural Networks](../../conferences/icml-2026/cards/1001-1100.md#fang26g-architecture) · 中文
- [L2G-NET: Local to Global Spectral Graph Neural Networks via Cauchy Factorizations](../../conferences/icml-2026/cards/1101-1200.md#fernandez26a-architecture) · 中文
- [Feature-Aware (Hyper)graph Generation via Next-Scale Prediction](../../conferences/icml-2026/cards/1101-1200.md#gailhard26a-architecture) · 中文
- [SuperHype: Hypergraph Generation via Graph-Superposition Decomposition](../../conferences/icml-2026/cards/1201-1300.md#gantes26a-architecture) · 中文
- [Hierarchical Multi Scale Graph Neural Networks: Scalable Heterophilous Learning with Oversmoothing and Oversquashing Mitigation](../../conferences/icml-2026/cards/1601-1700.md#hossen26a-architecture) · 中文
- [Is Fixing Schema Graphs Necessary? Full-Resolution Graph Structure Learning for Relational Deep Learning](../../conferences/icml-2026/cards/1701-1800.md#huang26ax-architecture) · 中文
- [GeoFlow: Geo-Aware Modeling of Inter-Area Relationships in Origin-Destination Flow Prediction and Generation](../../conferences/icml-2026/cards/1701-1800.md#huang26cj-architecture) · 中文
- [VDW-GNNs: Vector diffusion wavelets for geometric graph neural networks](../../conferences/icml-2026/cards/1901-2000.md#johnson26a-architecture) · 中文
- [Learning Graph Foundation Models on Riemannian Graph-of-Graphs](../../conferences/icml-2026/cards/2801-2900.md#liu26x-architecture) · 中文
- [Ramba: Selective State-Space Models for Relational Deep Learning](../../conferences/icml-2026/cards/2901-3000.md#liu26ep-architecture) · 中文
- [NetDiff: Graph Diffusion with Improved Global Capabilities to Generate and Update Mobile Network Topologies](../../conferences/icml-2026/cards/3201-3300.md#marcoccia26a-architecture) · 中文
- [LLM-MatLogic: Executable Exchange Contracts for Knowledge-Graph Query Answering with Scoped Negation](../../conferences/icml-2026/cards/3201-3300.md#miao26e-architecture) · 中文
- [Entangled No More: Multi-Domain Decoupling for Robust Dynamic Graph Neural Networks](../../conferences/icml-2026/cards/3301-3400.md#mo26a-architecture) · 中文
- [InvGNN: Learning Invertible Node Representations on Graphs](../../conferences/icml-2026/cards/3401-3500.md#nikolentzos26a-architecture) · 中文
- [Sheaf Neural Networks on SPD Manifolds: Second-Order Geometric Representation Learning](../../conferences/icml-2026/cards/3601-3700.md#peng26e-architecture) · 中文
- [Lightweight and Interpretable Transformer via Mixed Graph Algorithm Unrolling for Traffic Forecast](../../conferences/icml-2026/cards/3701-3800.md#qi26j-architecture) · 中文
- [On the Expressive Power of GNNs to Solve Linear SDPs](../../conferences/icml-2026/cards/3701-3800.md#qian26e-architecture) · 中文
- [Learning Long Range Spatio-Temporal Representations over Continuous Time Dynamic Graphs with State Space Models](../../conferences/icml-2026/cards/3701-3800.md#raghuvanshi26a-architecture) · 中文
- [Learning Multi-Agent Coordination via Sheaf-ADMM](../../conferences/icml-2026/cards/3901-4000.md#seely26a-architecture) · 中文
- [S$^3$GNN: Efficient Global Mixing and Local Message Passing for Long-Range Graph Learning](../../conferences/icml-2026/cards/4101-4200.md#shi26t-architecture) · 中文

<a id="by-scientific-ml"></a>

### Scientific Machine Learning

- [Physics-Informed Residual Flows](../../conferences/icml-2026/cards/0001-0100.md#abijuru26a-architecture) · 中文
- [Nested Spatio-Temporal Time Series Forecasting](../../conferences/icml-2026/cards/0001-0100.md#ai26f-architecture) · 中文
- [scCBGM: Single-Cell Editing via Concept Bottlenecks](../../conferences/icml-2026/cards/0001-0100.md#andersson26a-architecture) · 中文
- [Quantum latent distributions in deep generative models](../../conferences/icml-2026/cards/0101-0200.md#bacarreza26a-architecture) · 中文
- [Modeling Temporal scRNA-seq Data with Latent Gaussian Process and Optimal Transport](../../conferences/icml-2026/cards/0201-0300.md#balik26a-architecture) · 中文
- [Cheap2Rich: A Multi-Fidelity Framework for Data Assimilation and System Identification of Multiscale Physics - Rotating Detonation Engines](../../conferences/icml-2026/cards/0201-0300.md#bao26d-architecture) · 中文
- [Physics-Informed Coarsening for Multigrid Graph Neural Surrogates](../../conferences/icml-2026/cards/0201-0300.md#bazzi26a-architecture) · 中文
- [Stochastic Lifting for Generating Trajectories of Stochastic Physical Systems](../../conferences/icml-2026/cards/0201-0300.md#berman26b-architecture) · 中文
- [Continuous-Time Piecewise-Linear Recurrent Neural Networks](../../conferences/icml-2026/cards/0301-0400.md#brandle26a-architecture) · 中文
- [STFlow: Data-Coupled Flow Matching for Geometric Trajectory Simulation](../../conferences/icml-2026/cards/0301-0400.md#brinke26a-architecture) · 中文
- [Stochastic Neural Ray Tracing for Radio Frequency Channel Modeling](../../conferences/icml-2026/cards/0301-0400.md#bu26d-architecture) · 中文
- [LabBuilder: Protocol-Grounded 3D Layout Generation for Interactable and Safe Laboratory](../../conferences/icml-2026/cards/0401-0500.md#cao26ad-architecture) · 中文
- [Bioacoustic Geolocation: Species Sounds as Geographic Signals](../../conferences/icml-2026/cards/0401-0500.md#chasmai26b-architecture) · 中文
- [StormInsight: Hierarchical Environmental Forcing and Vertical Coupling for Convective Systems Evolution](../../conferences/icml-2026/cards/0401-0500.md#chen26aa-architecture) · 中文
- [From Holo Pockets to Electron Density: GPT-style Drug Design with Density](../../conferences/icml-2026/cards/0501-0600.md#chen26ai-architecture) · 中文
- [Co-Generative De Novo Functional Protein Design](../../conferences/icml-2026/cards/0501-0600.md#chen26cu-architecture) · 中文
- [SynLaD: Latent Diffusion for Generating Synthesizable Molecules Conditioned on 3D Pharmacophore Profiles](../../conferences/icml-2026/cards/0701-0800.md#cretu26a-architecture) · 中文
- [Adaptive Volumetric Mechanical Property Fields Invariant to Resolution](../../conferences/icml-2026/cards/0801-0900.md#dagli26a-architecture) · 中文
- [TINNs: Time-Induced Neural Networks for Solving Time-Dependent PDEs](../../conferences/icml-2026/cards/0801-0900.md#dai26a-architecture) · 中文
- [Condition-Aware Graph Flow Matching for Modeling the Distributions of Complex Fluid Systems](../../conferences/icml-2026/cards/0801-0900.md#deng26c-architecture) · 中文
- [Global Plane Waves from Local Gaussians: Periodic Charge Densities in a Blink](../../conferences/icml-2026/cards/1001-1100.md#elsborg26a-architecture) · 中文
- [BIOARC: Discovering Optimal Neural Architectures for Biological Foundation Models](../../conferences/icml-2026/cards/1001-1100.md#fang26u-architecture) · 中文
- [LERD: Latent Event-Relational Dynamics for Neurodegenerative Classification](../../conferences/icml-2026/cards/1001-1100.md#feng26b-architecture) · 中文
- [Learning Hamiltonian Dynamics at Scale: A Differential-Geometric Approach](../../conferences/icml-2026/cards/1101-1200.md#friedl26a-architecture) · 中文
- ["Do Diffusion Models Dream of Electric Planes?" Discrete and Continuous Simulation-Based Inference for Aircraft Design](../../conferences/icml-2026/cards/1201-1300.md#ghiglino26a-architecture) · 中文
- [SMART: Scalable Mesh-free Aerodynamic Simulations from Raw Geometries using a Transformer-based Surrogate Model](../../conferences/icml-2026/cards/1401-1500.md#hagnberger26a-architecture) · 中文
- [Large-Scale Molecular Dynamics Simulation: Direct Interatomic Modeling with Dilated Message Passing](../../conferences/icml-2026/cards/1501-1600.md#hong26h-architecture) · 中文
- [E2Former-V2: On-the-Fly Equivariant Attention with Linear Activation Memory](../../conferences/icml-2026/cards/1701-1800.md#huang26p-architecture) · 中文
- [Uncovering Latent Communication Patterns in Brain Networks via Adaptive Flow Routing](../../conferences/icml-2026/cards/1701-1800.md#huang26am-architecture) · 中文
- [Foundation Inference Models for Ordinary Differential Equations](../../conferences/icml-2026/cards/1701-1800.md#hubers26a-architecture) · 中文
- [LithoDreamer: A Physics-Informed World Model for Multi-Stage Computational Lithography](../../conferences/icml-2026/cards/1901-2000.md#jiang26ae-architecture) · 中文
- [KineFlow: Kinematic Second-Order Flow Matching for Time-Series Forecasting](../../conferences/icml-2026/cards/1901-2000.md#jiang26au-architecture) · 中文
- [Robust Signal Enhancement via Fractional Detail Views and Knowledge Guided Multi-view Fusion](../../conferences/icml-2026/cards/1901-2000.md#jin26g-architecture) · 中文
- [EvoEGF-Mol: Evolving Exponential Geodesic Flow for Structure-based Drug Design](../../conferences/icml-2026/cards/1901-2000.md#jin26i-architecture) · 中文
- [Efficient Equivariant High-Order Crystal Tensor Prediction via Cartesian Local-Environment Many-Body Coupling](../../conferences/icml-2026/cards/1901-2000.md#jin26p-architecture) · 中文
- [Scaling-Aware Adapter for Structure-Grounded LLM Reasoning](../../conferences/icml-2026/cards/1901-2000.md#jing26h-architecture) · 中文
- [Adaptive Physics Transformer with Fused Global-Local Attention for Subsurface Energy Systems](../../conferences/icml-2026/cards/2001-2100.md#ju26a-architecture) · 中文
- [Overcoming PINNs Failure Modes In High Dimension With Low-Rank Fourier Sum](../../conferences/icml-2026/cards/2001-2100.md#kaminsky26a-architecture) · 中文
- [Time-Conditioned Foreseeing: An EHR-Specific Foundation Model for Irregular Dynamics and Calendrical Time](../../conferences/icml-2026/cards/2001-2100.md#kang26a-architecture) · 中文
- [CatFlow: Co-generation of Slab-Adsorbate Systems via Flow Matching](../../conferences/icml-2026/cards/2101-2200.md#kim26z-architecture) · 中文
- [Machine Learning Hamiltonians are Accurate Energy-Force Predictors](../../conferences/icml-2026/cards/2101-2200.md#kim26an-architecture) · 中文
- [EqGINO: Equivariant Geometry-Informed Fourier Neural Operators for 3D PDEs](../../conferences/icml-2026/cards/2101-2200.md#kim26bp-architecture) · 中文
- [NeurOCNN: A Neural-Operator-Based Model for Physiological Time Series](../../conferences/icml-2026/cards/2201-2300.md#kumar26b-architecture) · 中文
- [FluxNet: Learning Capacity-Constrained Local Transport Operators for Conservative and Bounded PDE Surrogates](../../conferences/icml-2026/cards/2201-2300.md#lan26c-architecture) · 中文
- [LDARNet: DNA Adaptive Representation Network with Learnable Tokenization for Genomic Modeling](../../conferences/icml-2026/cards/2301-2400.md#ledneva26a-architecture) · 中文
- [BIT-LLM: Brain Instruction Tuned LLM with persistent Cross-Attention for fMRI-to-Text Decoding](../../conferences/icml-2026/cards/2301-2400.md#lee26v-architecture) · 中文
- [Lie-Algebraic Acceleration of Neural Koopman Dynamics](../../conferences/icml-2026/cards/2301-2400.md#lee26aa-architecture) · 中文
- [InertialAR: Autoregressive 3D Molecule Generation with Inertial Frames](../../conferences/icml-2026/cards/2401-2500.md#li26am-architecture) · 中文
- [From Basis to Basis: Gaussian Particle Representation for Interpretable PDE Operators](../../conferences/icml-2026/cards/2401-2500.md#li26aq-architecture) · 中文
- [Di-BiLPS: Denoising induced Bidirectional Latent-PDE-Solver under Sparse Observations](../../conferences/icml-2026/cards/2501-2600.md#li26dk-architecture) · 中文
- [CryoACE: An Atom-centric Framework for Accurate and Automated Model Building in Cryo-EM](../../conferences/icml-2026/cards/2501-2600.md#li26eh-architecture) · 中文
- [Mind the State: Towards Unified, Context-Aware EEG-to-fMRI Synthesis](../../conferences/icml-2026/cards/2501-2600.md#li26gp-architecture) · 中文
- [Neural Modular Physics for Elastic Simulation](../../conferences/icml-2026/cards/2601-2700.md#li26ho-architecture) · 中文
- [Towards High-Fidelity CAD Generation via LLM-Driven Program Generation and Text-Based B-Rep Primitive Grounding](../../conferences/icml-2026/cards/2601-2700.md#li26jd-architecture) · 中文
- [Bipartite Graph Attention-based Clustering for Large-scale scRNA-seq Data](../../conferences/icml-2026/cards/2601-2700.md#liang26a-architecture) · 中文
- [Frequency Matching in Spiking Neural Networks for mmWave Sensing](../../conferences/icml-2026/cards/2701-2800.md#liao26e-architecture) · 中文
- [Flow Equivariant World Models: Structured Memory for Dynamic Environments](../../conferences/icml-2026/cards/2701-2800.md#lillemark26a-architecture) · 中文
- [Interpretable Neural ODEs for Gene Regulatory Network Discovery under Perturbations](../../conferences/icml-2026/cards/2701-2800.md#lin26e-architecture) · 中文
- [BioDynaSpec: Harmonic-Guided Spatio-Spectral Autoregressive Diffusion for Protein Dynamics Generation](../../conferences/icml-2026/cards/2701-2800.md#lin26x-architecture) · 中文
- [Periodic Bayesian Flow Networks with Additive Accuracy](../../conferences/icml-2026/cards/2701-2800.md#lin26ar-architecture) · 中文
- [LangPrecip: Language-Aware Multimodal Precipitation Nowcasting](../../conferences/icml-2026/cards/2701-2800.md#ling26a-architecture) · 中文
- [Solving Time-Dependent Differential Equations with Physical Dynamical Systems](../../conferences/icml-2026/cards/2701-2800.md#liu26s-architecture) · 中文
- [ViEEG: Hierarchical Visual Neural Representation for EEG Brain Decoding](../../conferences/icml-2026/cards/2801-2900.md#liu26ap-architecture) · 中文
- [Equivariant Covariance Tensors: Guaranteed SPD Uncertainty for Tensor-Valued Geometric Learning](../../conferences/icml-2026/cards/2801-2900.md#liu26bk-architecture) · 中文
- [Decoupling Universal Laws and Environmental Heterogeneity: A Physics-Inspired Framework for Robust Spatio-Temporal Forecasting](../../conferences/icml-2026/cards/2901-3000.md#liu26er-architecture) · 中文
- [Cardio-mmFlow: A Gaussian-Prior-Free Physics-Informed Flow Matching Framework for Electrocardiogram to mmWave Radar Synthesis](../../conferences/icml-2026/cards/2901-3000.md#liu26ey-architecture) · 中文
- [FlowCloud: Learning Continuous Spatiotemporal Dynamics from Unpaired Sparse Point Cloud Snapshots](../../conferences/icml-2026/cards/2901-3000.md#liu26fl-architecture) · 中文
- [ChaosNexus: A Foundation Model for ODE-based Chaotic System Forecasting with Hierarchical Multi-scale Awareness](../../conferences/icml-2026/cards/2901-3000.md#liu26gg-architecture) · 中文
- [Adaptive DNA Sequence Modeling via Synergistic Plasticity Units](../../conferences/icml-2026/cards/2901-3000.md#liu26gj-architecture) · 中文
- [Cello: A Universal Cell-wise Feature Aggregation framework for Reliable Pathology Images Analysis](../../conferences/icml-2026/cards/2901-3000.md#lou26d-architecture) · 中文
- [Mind-Omni: A Unified Multi-Task Framework for Brain-Vision-Language Modeling via Discrete Diffusion](../../conferences/icml-2026/cards/3001-3100.md#lu26d-architecture) · 中文
- [Interpretable Functional Koopman Learning with Non-Markovian Closure for Spatiotemporal Systems](../../conferences/icml-2026/cards/3001-3100.md#lu26u-architecture) · 中文
- [Physically-Guided Data-Space Rectified Flow for Precipitation Nowcasting](../../conferences/icml-2026/cards/3001-3100.md#luo26l-architecture) · 中文
- [ProConMV: Provenance-Enabled Conceptual Framework for Interpretable Multi-View Diabetic Retinopathy Diagnosis](../../conferences/icml-2026/cards/3001-3100.md#luo26ac-architecture) · 中文
- [Walrus: A Cross-domain Foundation Model for Continuum Dynamics](../../conferences/icml-2026/cards/3201-3300.md#mccabe26a-architecture) · 中文
- [PhenoBrain: Phenotype-Conditioned Long-Range Communication for Multi-Modal Brain Network Analysis](../../conferences/icml-2026/cards/3201-3300.md#meng26f-architecture) · 中文
- [Deep Coupling Learning for Solving PDEs](../../conferences/icml-2026/cards/3201-3300.md#meng26i-architecture) · 中文
- [Proximal Splitting Methods for Hybrid Differentiable Models](../../conferences/icml-2026/cards/3201-3300.md#mezidi26a-architecture) · 中文
- [DITING: A Weak Degradation Listener for Battery Lifetime Early Prediction](../../conferences/icml-2026/cards/3201-3300.md#miao26d-architecture) · 中文
- [Flowers: A Warp Drive for Neural PDE Solvers](../../conferences/icml-2026/cards/3301-3400.md#muser26a-architecture) · 中文
- [Discovering Scaling Exponents with Physics-Informed Müntz-Szász Networks](../../conferences/icml-2026/cards/3301-3400.md#n-guessan26a-architecture) · 中文
- [Interleaved Selective State Space Models for Efficient WiFi-Based 3D Multi-Person Pose Estimation](../../conferences/icml-2026/cards/3301-3400.md#n-d-26a-architecture) · 中文
- [Learning Dynamic Stability Landscapes in Synchronization Networks](../../conferences/icml-2026/cards/3401-3500.md#nauck26a-architecture) · 中文
- [Error-Driven Graph Augmentation for Mesh-Based PDE Surrogates](../../conferences/icml-2026/cards/3401-3500.md#nguyen26a-architecture) · 中文
- [Flexibility-Aware Geometric Latent Diffusion for Full-Atom Peptide Design](../../conferences/icml-2026/cards/3401-3500.md#niu26e-architecture) · 中文
- [Mesh Field Theory: Port–Hamiltonian Formulation of Mesh-Based Physics](../../conferences/icml-2026/cards/3401-3500.md#noguchi26a-architecture) · 中文
- [Scalable Single-Cell Gene Expression Generation with Latent Diffusion Models](../../conferences/icml-2026/cards/3501-3600.md#palla26a-architecture) · 中文
- [Euler–Poincaré Neural Dynamics: A Geometric-Mechanics Framework for Scientific Simulation](../../conferences/icml-2026/cards/3501-3600.md#park26j-architecture) · 中文
- [SleepMaMi: A Universal Sleep Foundation Model for Integrating Macro- and Micro-structures](../../conferences/icml-2026/cards/3501-3600.md#park26n-architecture) · 中文
- [Generative Neural Operators through Diffusion Last Layer](../../conferences/icml-2026/cards/3601-3700.md#park26aa-architecture) · 中文
- [Insertion Based Sequence Generation with Learnable Order Dynamics](../../conferences/icml-2026/cards/3601-3700.md#patel26a-architecture) · 中文
- [Hyperbolic Neural Operator](../../conferences/icml-2026/cards/3601-3700.md#pei26b-architecture) · 中文
- [Learning Adaptive Perturbation-Conditioned Contexts for Robust Transcriptional Response Prediction](../../conferences/icml-2026/cards/3601-3700.md#piao26a-architecture) · 中文
- [Protein Autoregressive Modeling via Multiscale Structure Generation](../../conferences/icml-2026/cards/3701-3800.md#qu26b-architecture) · 中文
- [A recipe for scalable attention-based ML potentials: unlocking long-range accuracy with all-to-all node attention](../../conferences/icml-2026/cards/3701-3800.md#qu26g-architecture) · 中文
- [TerraBind: Fast and Accurate Binding Affinity Prediction through Coarse Structural Representations](../../conferences/icml-2026/cards/3801-3900.md#rossi26a-architecture) · 中文
- [Multimodal Crystal Flow: Any-to-Any Modality Generation for Unified Crystal Modeling](../../conferences/icml-2026/cards/4001-4100.md#seong26a-architecture) · 中文
- [Structure-Preserving Learning Improves Geometry Generalization in Neural PDEs](../../conferences/icml-2026/cards/4001-4100.md#shaffer26a-architecture) · 中文
- [Tri-Scale Neural ODEs for Continuous Multi-Omics Disease Modeling](../../conferences/icml-2026/cards/4001-4100.md#shaffiey26a-architecture) · 中文
- [dnaHNet: A Scalable and Hierarchical Foundation Model for Genomic Sequence Learning](../../conferences/icml-2026/cards/4001-4100.md#shah26b-architecture) · 中文
- [SpaEF: Spatially Resolved Transcriptomics Data Element-Wise Denoising Framework Powered by Large Models](../../conferences/icml-2026/cards/4001-4100.md#shang26a-architecture) · 中文
- [Expanding the Chaos: Neural Operator for Stochastic (Partial) Differential Equations](../../conferences/icml-2026/cards/4101-4200.md#shi26i-architecture) · 中文
- [FLAG: Foundation model representation with Latent diffusion Alignment via Graph for spatial gene expression prediction](../../conferences/icml-2026/cards/4101-4200.md#si26a-architecture) · 中文
- [Neural-HSS: Hierarchical Semi-Separable Neural PDE Solver](../../conferences/icml-2026/cards/4101-4200.md#sittoni26a-architecture) · 中文
<!-- classification:end -->
