# 计算机视觉

[首页](../README.md) · [参与贡献](../CONTRIBUTING.md) · [English](../en/papers/computer-vision.md)

视觉识别、表征学习与生成。

<!-- classification:start -->
## 按技术类型浏览

[模型架构](#by-architecture) · [模块](#by-modules) · [损失函数](#by-loss-functions) · [优化](#by-optimization) · [强化学习方法](#by-reinforcement-learning) · [训练策略](#by-training-strategies) · [数据策略](#by-data-strategies) · [推理策略](#by-inference) · [表征学习](#by-representation-learning) · [评测与诊断](#by-evaluation) · [理论与统计](#by-theory-statistics)

<a id="by-architecture"></a>

### 模型架构

- <a id="atanov26a-architecture"></a>[VideoFlexTok: Flexible-Length Coarse-to-Fine Video Tokenization](../conferences/icml-2026/cards/0101-0200.md#paper-atanov26a)
- <a id="baade26a-architecture"></a>[Latent Forcing: Reordering the Diffusion Trajectory for Pixel-Space Image Generation](../conferences/icml-2026/cards/0101-0200.md#paper-baade26a)
- <a id="bao26f-architecture"></a>[Envisioning Beyond the Few: Disentangled Semantics and Primitives for Few-Shot Atypical Layout-to-Image Generation](../conferences/icml-2026/cards/0201-0300.md#paper-bao26f)
- <a id="chen26du-architecture"></a>[Autoregression with Self-Token Prediction](../conferences/icml-2026/cards/0501-0600.md#paper-chen26du)
- <a id="chen26ga-architecture"></a>[Phy-CoSF: Physics-Guided Continuous Spectral Fields Reconstruction and Spectral Super-Resolution for Snapshot Compressive Imaging](../conferences/icml-2026/cards/0601-0700.md#paper-chen26ga)
- <a id="choy26a-architecture"></a>[SpaCeFormer: Fast Proposal-Free Open-Vocabulary 3D Instance Segmentation](../conferences/icml-2026/cards/0701-0800.md#paper-choy26a)
- <a id="ding26u-architecture"></a>[Native Spatio-Temporal 4D Variational Autoencoder](../conferences/icml-2026/cards/0901-1000.md#paper-ding26u)
- <a id="du26c-architecture"></a>[AesFormer: Transform Everyday Photos into Beautiful Memories](../conferences/icml-2026/cards/0901-1000.md#paper-du26c)
- <a id="duan26e-architecture"></a>[Discontinuous Galerkin Neural Operator for Pathology Defocus Deblurring](../conferences/icml-2026/cards/0901-1000.md#paper-duan26e)
- <a id="fu26l-architecture"></a>[CODiff: One-Step Diffusion Model for Camouflaged Object Detection](../conferences/icml-2026/cards/1101-1200.md#paper-fu26l)
- <a id="gao26aq-architecture"></a>[DecomPose: Disentangling Cross-Category Optimization Contention for Category-Level 6D Object Pose Estimation](../conferences/icml-2026/cards/1201-1300.md#paper-gao26aq)
- <a id="garcin26a-architecture"></a>[Beyond Pixel Histories: World Models with Persistent 3D State](../conferences/icml-2026/cards/1201-1300.md#paper-garcin26a)
- <a id="gong26f-architecture"></a>[Direct 3D-Aware Object Insertion via Decomposed Visual Proxies](../conferences/icml-2026/cards/1301-1400.md#paper-gong26f)
- <a id="guo26ag-architecture"></a>[OmniAID: Decoupling Semantics and Artifacts for Universal AI-Generated Image Detection in the Wild](../conferences/icml-2026/cards/1401-1500.md#paper-guo26ag)
- <a id="han26c-architecture"></a>[Bridging Local–Global Dissonance: Learning from Compressive Measurements for Hyperspectral Reconstruction](../conferences/icml-2026/cards/1401-1500.md#paper-han26c)

<a id="by-modules"></a><a id="vision-model-distillation"></a>

### 模块

- <a id="blauch26a-modules"></a>[FOVI: A biologically-inspired foveated interface for deep vision models](../conferences/icml-2026/cards/0201-0300.md#paper-blauch26a)
- <a id="candogan26a-modules"></a>[Spatial Priors via Space Filling Curves for Small and Limited Data Vision Transformers](../conferences/icml-2026/cards/0301-0400.md#paper-candogan26a)
- <a id="cao26j-modules"></a>[Multi-Label Learning with Contrastive Cluster Self-Supervision for 3D Hierarchical Semantic Segmentation](../conferences/icml-2026/cards/0301-0400.md#paper-cao26j)
- <a id="cao26n-modules"></a>[LiteVSR: Lightweight Adaptation of Frozen Diffusion Transformers for Video Super-Resolution](../conferences/icml-2026/cards/0301-0400.md#paper-cao26n)
- <a id="cao26ab-modules"></a>[StructMAR: Structure-Aware Masked Autoregression for Explicit Layout Alignment in Text-to-Image Generation](../conferences/icml-2026/cards/0401-0500.md#paper-cao26ab)
- <a id="chen26ce-modules"></a>[WEVSR: Video Diffusion Generators for Real-World Video Super-Resolution with Wavelet-Enhanced VAE Encoder](../conferences/icml-2026/cards/0501-0600.md#paper-chen26ce)
- <a id="ciernik26a-modules"></a>[Attentive Multi-Layer Fusion for Vision Transformers](../conferences/icml-2026/cards/0701-0800.md#paper-ciernik26a)
- <a id="colamonaco26a-modules"></a>[Prototype-Grounded Concept Models for Verifiable Concept Alignment](../conferences/icml-2026/cards/0701-0800.md#paper-colamonaco26a)
- <a id="dhar26a-modules"></a>[Does a Hybrid Space-Aware Randomized Defense Improve Empirical and Certified Adversarial Robustness?](../conferences/icml-2026/cards/0801-0900.md#paper-dhar26a)
- <a id="dong26i-modules"></a>[PolarDepth: Monocular Transparent Object Depth from Polar-Physics Priors](../conferences/icml-2026/cards/0901-1000.md#paper-dong26i)
- <a id="duan26a-modules"></a>[MobileFusion: Mobile-Friendly Infrared and Visible Image Fusion via Structural Re-parameterization](../conferences/icml-2026/cards/0901-1000.md#paper-duan26a)
- <a id="guo26ad-modules"></a>[WildActor: Unconstrained Identity-Preserving Video Generation](../conferences/icml-2026/cards/1401-1500.md#paper-guo26ad)
- <a id="hadji26a-modules"></a>[Hierarchical Image Tokenization for Multi-Scale Image Super Resolution](../conferences/icml-2026/cards/1401-1500.md#paper-hadji26a)
- <a id="tian26k-modules"></a>[From Per-Image Low-Rank to Encoding Mismatch: Rethinking Feature Distillation in Vision Transformers](../conferences/icml-2026/cards/4401-4500.md#paper-tian26k)

<a id="by-loss-functions"></a>

### 损失函数

- <a id="bai26c-loss-functions"></a>[Threshold-Guided Optimization for Visual Generative Models](../conferences/icml-2026/cards/0101-0200.md#paper-bai26c)
- <a id="bo26a-loss-functions"></a>[Benchmarking Dense and Indiscernible Object Counting with Blueberries](../conferences/icml-2026/cards/0301-0400.md#paper-bo26a)
- <a id="deng26e-loss-functions"></a>[Joint Geometric and Trajectory Consistency Learning for One-Step Real-World Super-Resolution](../conferences/icml-2026/cards/0801-0900.md#paper-deng26e)
- <a id="gushchin26a-loss-functions"></a>[BiRQA: Bidirectional Robust Quality Assessment for Images](../conferences/icml-2026/cards/1401-1500.md#paper-gushchin26a)
- <a id="ha26b-loss-functions"></a>[Unlearning’s Blind Spots: Over-Unlearning and Prototypical Relearning Attack](../conferences/icml-2026/cards/1401-1500.md#paper-ha26b)

<a id="by-optimization"></a>

### 优化

- <a id="crane26a-optimization"></a>[Scalable and Differentiable Point-Cloud Registration Using Maximum Mean Discrepancy](../conferences/icml-2026/cards/0701-0800.md#paper-crane26a)
- <a id="dai26h-optimization"></a>[TextMesh4D: Zero-shot Text-to-4D Mesh Generation](../conferences/icml-2026/cards/0801-0900.md#paper-dai26h)
- <a id="denker26a-optimization"></a>[Trajectory Stitching for Solving Inverse Problems with Flow-Based Models](../conferences/icml-2026/cards/0801-0900.md#paper-denker26a)
- <a id="ding26p-optimization"></a>[Improving Explicit Dynamic Gaussian Splatting Optimization via Update Mixture](../conferences/icml-2026/cards/0901-1000.md#paper-ding26p)

<a id="by-reinforcement-learning"></a>

### 强化学习方法

- <a id="ba26a-reinforcement-learning"></a>[Pareto-Guided Optimal Transport for Multi-Reward Alignment](../conferences/icml-2026/cards/0101-0200.md#paper-ba26a)
- <a id="chen26as-reinforcement-learning"></a>[Test-Time Reinforcement Learning for Flow Matching](../conferences/icml-2026/cards/0501-0600.md#paper-chen26as)
- <a id="chen26ea-reinforcement-learning"></a>[RELO: Reinforcement Learning to Localize for Visual Object Tracking](../conferences/icml-2026/cards/0501-0600.md#paper-chen26ea)
- <a id="choi26o-reinforcement-learning"></a>[Rethinking the Design Space of Reinforcement Learning for Diffusion Models: On the Importance of Likelihood Estimation Beyond Loss Design](../conferences/icml-2026/cards/0701-0800.md#paper-choi26o)
- <a id="guo26h-reinforcement-learning"></a>[Probabilistic Salient Object Ranking](../conferences/icml-2026/cards/1301-1400.md#paper-guo26h)
- <a id="han26o-reinforcement-learning"></a>[ForceForget: Reinforcement Concept Removal for Enhancing Safety in Text-to-Image Models](../conferences/icml-2026/cards/1401-1500.md#paper-han26o)

<a id="by-training-strategies"></a>

### 训练策略

- <a id="bai26n-training-strategies"></a>[Optimizing Few-Step Generation with Adaptive Matching Distillation](../conferences/icml-2026/cards/0101-0200.md#paper-bai26n)
- <a id="cai26h-training-strategies"></a>[Mode Seeking meets Mean Seeking for Fast Long Video Generation](../conferences/icml-2026/cards/0301-0400.md#paper-cai26h)
- <a id="cao26o-training-strategies"></a>[Beyond Static Allocation: Dynamic Sensitivity-Aware Fine-Tuning for Vision Transformers](../conferences/icml-2026/cards/0301-0400.md#paper-cao26o)
- <a id="chavhan26a-training-strategies"></a>[NanoFLUX: Distillation-Driven Compression of Large Text-to-Image Generation Models for Mobile Devices](../conferences/icml-2026/cards/0401-0500.md#paper-chavhan26a)
- <a id="chen26cn-training-strategies"></a>[Focusing: View-Consistent Sparse Voxels for Efficient 3D VAE Training](../conferences/icml-2026/cards/0501-0600.md#paper-chen26cn)
- <a id="chen26dm-training-strategies"></a>[3DGS-HPC: Distractor-free 3D Gaussian Splatting with Hybrid Patch-wise Classification](../conferences/icml-2026/cards/0501-0600.md#paper-chen26dm)
- <a id="chen26eu-training-strategies"></a>[Context Forcing: Consistent Autoregressive Video Generation with Long Context](../conferences/icml-2026/cards/0601-0700.md#paper-chen26eu)
- <a id="chu26b-training-strategies"></a>[End-to-End Autoregressive Image Generation with 1D Semantic Tokenizer](../conferences/icml-2026/cards/0701-0800.md#paper-chu26b)
- <a id="cui26g-training-strategies"></a>[Hard Labels In! Rethinking the Role of Hard Labels in Mitigating Local Semantic Drift](../conferences/icml-2026/cards/0701-0800.md#paper-cui26g)
- <a id="ding26t-training-strategies"></a>[SpeedVFI: One-step Diffusion for Efficient Video Frame Interpolation](../conferences/icml-2026/cards/0901-1000.md#paper-ding26t)
- <a id="dong26k-training-strategies"></a>[TurboGS: Accelerating 3D Gaussian Splatting via Error-Guided Sparse Pixel Sampling and Optimization](../conferences/icml-2026/cards/0901-1000.md#paper-dong26k)
- <a id="dong26l-training-strategies"></a>[RePack then Refine: Efficient Diffusion Transformers with Vision Foundation Models](../conferences/icml-2026/cards/0901-1000.md#paper-dong26l)
- <a id="du26g-training-strategies"></a>[Can We Build a Monolithic Model for Fake Image Detection? SICA: Semantic-Induced Constrained Adaptation for Unified-Yet-Discriminative Artifact Feature Space Reconstruction](../conferences/icml-2026/cards/0901-1000.md#paper-du26g)
- <a id="du26q-training-strategies"></a>[VideoGPA: Distilling Geometry Priors for 3D-Consistent Video Generation](../conferences/icml-2026/cards/0901-1000.md#paper-du26q)
- <a id="esteves26a-training-strategies"></a>[Spectrally-Guided Diffusion Noise Schedules](../conferences/icml-2026/cards/1001-1100.md#paper-esteves26a)
- <a id="gong26j-training-strategies"></a>[Light Up Your Face: A Physically Consistent Dataset and Diffusion Model for Face Fill-Light Enhancement](../conferences/icml-2026/cards/1301-1400.md#paper-gong26j)

<a id="by-data-strategies"></a>

### 数据策略

- <a id="cai26m-data-strategies"></a>[FUSE: Full-spectrum Unlearnable Examples via Spectral Equalization](../conferences/icml-2026/cards/0301-0400.md#paper-cai26m)
- <a id="cao26s-data-strategies"></a>[Where Detectors Fail: Probing Generative Space for Generalizable AI-Generated Image Detection](../conferences/icml-2026/cards/0401-0500.md#paper-cao26s)
- <a id="chen26s-data-strategies"></a>[When Preference Labels Fall Short: Aligning Diffusion Models from Real Data](../conferences/icml-2026/cards/0401-0500.md#paper-chen26s)
- <a id="chen26bj-data-strategies"></a>[Amodal Instance Segmentation with IRAIS Dataset for Sim-to-Real Transfer](../conferences/icml-2026/cards/0501-0600.md#paper-chen26bj)
- <a id="cui26f-data-strategies"></a>[Geometry-Aware Dataset Condensation for Diffusion Model Training](../conferences/icml-2026/cards/0701-0800.md#paper-cui26f)
- <a id="fang26s-data-strategies"></a>[Real Data Lies: Unveiling and Closing the Quality Shortcut in Generalizable AI-Generated Video Detection](../conferences/icml-2026/cards/1001-1100.md#paper-fang26s)
- <a id="gan26d-data-strategies"></a>[Set-Coupled Guidance: Set-Level Coordination in Diffusion-Based Dataset Distillation](../conferences/icml-2026/cards/1101-1200.md#paper-gan26d)

<a id="by-inference"></a>

### 推理策略

- <a id="alesiani26a-inference"></a>[Logical Guidance for the Exact Composition of Diffusion Models](../conferences/icml-2026/cards/0001-0100.md#paper-alesiani26a)
- <a id="bae26b-inference"></a>[Training-Free Coverless Multi-Image Steganography with Access Control](../conferences/icml-2026/cards/0101-0200.md#paper-bae26b)
- <a id="bang26a-inference"></a>[Triadic Dynamics Aware Diffusion Posterior Sampling for Inverse Problems: Optimizing Guidance and Stochasticity Schedules](../conferences/icml-2026/cards/0201-0300.md#paper-bang26a)
- <a id="briq26a-inference"></a>[Exploring and Exploiting Stability in Latent Flow Matching](../conferences/icml-2026/cards/0301-0400.md#paper-briq26a)
- <a id="cai26g-inference"></a>[Improving Classifier-Free Guidance of Flow Matching via Manifold Projection](../conferences/icml-2026/cards/0301-0400.md#paper-cai26g)
- <a id="cai26n-inference"></a>[TIMI: Training-Free Image-to-3D Multi-Instance Generation with Spatial Fidelity](../conferences/icml-2026/cards/0301-0400.md#paper-cai26n)
- <a id="cao26e-inference"></a>[Efficient Learned Image Compression without Entropy Coding](../conferences/icml-2026/cards/0301-0400.md#paper-cao26e)
- <a id="chang26c-inference"></a>[ContrastiveCFG: Guiding Diffusion Sampling by Contrasting Positive and Negative Concepts](../conferences/icml-2026/cards/0401-0500.md#paper-chang26c)
- <a id="chen26v-inference"></a>[PRISM: Training-Free Video Anomaly Detection via Intrinsic Statistical Modeling](../conferences/icml-2026/cards/0401-0500.md#paper-chen26v)
- <a id="chen26aj-inference"></a>[Normalizing Flows with Iterative Denoising](../conferences/icml-2026/cards/0501-0600.md#paper-chen26aj)
- <a id="chen26bp-inference"></a>[Bi-Anchor Interpolation Solver for Accelerating Generative Modeling](../conferences/icml-2026/cards/0501-0600.md#paper-chen26bp)
- <a id="chen26dn-inference"></a>[XSpecMesh: Quality-Preserving Auto-Regressive Mesh Generation Acceleration via Multi-Head Speculative Decoding](../conferences/icml-2026/cards/0501-0600.md#paper-chen26dn)
- <a id="chen26ey-inference"></a>[SemanticNVS: Improving Semantic Scene Understanding in Generative Novel View Synthesis](../conferences/icml-2026/cards/0601-0700.md#paper-chen26ey)
- <a id="chen26fc-inference"></a>[ScalingAR: Scaling Confidence for Autoregressive Image Generation](../conferences/icml-2026/cards/0601-0700.md#paper-chen26fc)
- <a id="chen26fq-inference"></a>[GuidedBridge: Training-freely Improving Bridge Models with Prior Guidance](../conferences/icml-2026/cards/0601-0700.md#paper-chen26fq)
- <a id="cheng26b-inference"></a>[FS-I2P: A Hierarchical Focus–Sweep Registration Network with Dynamically Allocated Depth](../conferences/icml-2026/cards/0601-0700.md#paper-cheng26b)
- <a id="cho26a-inference"></a>[TAG: Tangential Amplifying Guidance for Hallucination-Resistant Sampling](../conferences/icml-2026/cards/0701-0800.md#paper-cho26a)
- <a id="cho26d-inference"></a>[Balancing Fidelity and Diversity in Diffusion Models via Symmetric Attention Decomposition: Hopfield Perspective](../conferences/icml-2026/cards/0701-0800.md#paper-cho26d)
- <a id="choi26m-inference"></a>[Concept Removal Guidance: Evidence-Calibrated Negative Guidance for Safe Diffusion Sampling](../conferences/icml-2026/cards/0701-0800.md#paper-choi26m)
- <a id="cong26a-inference"></a>[RT-Lynx: Putting GEMM Sparsity in the Right Place for Diffusion Models](../conferences/icml-2026/cards/0701-0800.md#paper-cong26a)
- <a id="damblon26a-inference"></a>[SG2Loc: Sequential Visual Localization on 3D Scene Graphs](../conferences/icml-2026/cards/0801-0900.md#paper-damblon26a)
- <a id="deng26a-inference"></a>[STORM: Segment, Track, and Object Re-Localization from a Single Image](../conferences/icml-2026/cards/0801-0900.md#paper-deng26a)
- <a id="deng26i-inference"></a>[Forget-It-All: Multi-Concept Machine Unlearning via Concept-Aware Neuron Masking](../conferences/icml-2026/cards/0801-0900.md#paper-deng26i)
- <a id="duan26d-inference"></a>[SlerpFlow: Spherical Trajectory Correction for Rectified Flow Inversion](../conferences/icml-2026/cards/0901-1000.md#paper-duan26d)
- <a id="elbrachter26a-inference"></a>[MAD: Manifold Attracted Diffusion](../conferences/icml-2026/cards/1001-1100.md#paper-elbrachter26a)
- <a id="fang26n-inference"></a>[Trajectory-Aware Spiking DiTs Conversion via Membrane Potential Error-Feedback](../conferences/icml-2026/cards/1001-1100.md#paper-fang26n)
- <a id="fang26z-inference"></a>[StreamFlow: Theory, Algorithm, and Implementation for High-Efficiency Rectified Flow Generation](../conferences/icml-2026/cards/1001-1100.md#paper-fang26z)
- <a id="feng26g-inference"></a>[Explainable Forensics of Manipulated Segments in Untrimmed Long Videos](../conferences/icml-2026/cards/1101-1200.md#paper-feng26g)
- <a id="feng26r-inference"></a>[HEDP: A Hybrid Energy-Distance Prompt-based Framework for Domain Incremental Learning](../conferences/icml-2026/cards/1101-1200.md#paper-feng26r)
- <a id="feng26t-inference"></a>[Fast-SAM3D: 3Dfy Anything in Images but Faster](../conferences/icml-2026/cards/1101-1200.md#paper-feng26t)
- <a id="feng26w-inference"></a>[Bridging RGB and RAW: Single-step Deterministic Flow with Homogeneous Representation Alignment](../conferences/icml-2026/cards/1101-1200.md#paper-feng26w)
- <a id="feng26ac-inference"></a>[Enhancing Train-Free Infinite-Frame Generation for Consistent Long Videos](../conferences/icml-2026/cards/1101-1200.md#paper-feng26ac)
- <a id="frumkin26a-inference"></a>[Q-Sched: Pushing the Boundaries of Few-Step Diffusion Models with Quantization-Aware Scheduling](../conferences/icml-2026/cards/1101-1200.md#paper-frumkin26a)
- <a id="fu26o-inference"></a>[Dual Optimal Transport for Multi-Concept Composition: Structure Alignment and Texture Injection in Diffusion Models](../conferences/icml-2026/cards/1101-1200.md#paper-fu26o)
- <a id="gao26e-inference"></a>[Taming I2V models for Image HOI Editing: A Cognitive Benchmark and Agentic Self-Correcting Framework](../conferences/icml-2026/cards/1201-1300.md#paper-gao26e)
- <a id="gao26x-inference"></a>[(1D) Ordered Tokens Enable Efficient Test-Time Search](../conferences/icml-2026/cards/1201-1300.md#paper-gao26x)
- <a id="gu26f-inference"></a>[Mitigating Noise-Induced Layout Priors for Object Counting in Diffusion Models](../conferences/icml-2026/cards/1301-1400.md#paper-gu26f)
- <a id="gu26m-inference"></a>[R$^3$L: Reasoning 3D Layouts from Relative Spatial Relations](../conferences/icml-2026/cards/1301-1400.md#paper-gu26m)
- <a id="guo26s-inference"></a>[Sample Margin-Aware Recalibration of Temperature Scaling](../conferences/icml-2026/cards/1301-1400.md#paper-guo26s)
- <a id="gupta26a-inference"></a>[Divide-and-Denoise: A Game-Theoretic Method for Fairly Composing Diffusion Models](../conferences/icml-2026/cards/1401-1500.md#paper-gupta26a)
- <a id="han26l-inference"></a>[Physics in 2-Steps: Locking Motion Priors Before Visual Refinement Erases Them](../conferences/icml-2026/cards/1401-1500.md#paper-han26l)

<a id="by-representation-learning"></a>

### 表征学习

- <a id="bian26d-representation-learning"></a>[CURE: Consistency-under-Unified Semantic Regularization for Generalized Category Discovery](../conferences/icml-2026/cards/0201-0300.md#paper-bian26d)
- <a id="boduljak26a-representation-learning"></a>[VFMF: Dense Forecasting by Generating Vision Foundation Model Features](../conferences/icml-2026/cards/0301-0400.md#paper-boduljak26a)
- <a id="cao26h-representation-learning"></a>[On the Power of Statistics in Class-Incremental Learning with Pretrained Models](../conferences/icml-2026/cards/0301-0400.md#paper-cao26h)
- <a id="cassano26a-representation-learning"></a>[SAEmnesia: Erasing Concepts in Diffusion Models with Supervised Sparse Autoencoders](../conferences/icml-2026/cards/0401-0500.md#paper-cassano26a)
- <a id="cendra26a-representation-learning"></a>[PartCo: Part-Level Correspondence Priors Enhance Category Discovery](../conferences/icml-2026/cards/0401-0500.md#paper-cendra26a)
- <a id="chen26ca-representation-learning"></a>[Rotation-Invariant Spherical Watermarking via Third-Order SO(3) Representation Coupling](../conferences/icml-2026/cards/0501-0600.md#paper-chen26ca)
- <a id="chen26ee-representation-learning"></a>[DynaTok: Token-Based 4D Reconstruction from Partial Point Clouds](../conferences/icml-2026/cards/0601-0700.md#paper-chen26ee)
- <a id="chen26ek-representation-learning"></a>[Multiview Self-Representation Learning across Heterogeneous Views](../conferences/icml-2026/cards/0601-0700.md#paper-chen26ek)
- <a id="chen26fh-representation-learning"></a>[TrustworthyQENN: A Quantum Evidential Neural Network Based on Complex-Valued Contrastive Learning for Uncertainty Pattern Classification](../conferences/icml-2026/cards/0601-0700.md#paper-chen26fh)
- <a id="cui26k-representation-learning"></a>[Bayesian Gated Non-Negative Contrastive Learning](../conferences/icml-2026/cards/0801-0900.md#paper-cui26k)
- <a id="dai26b-representation-learning"></a>[Identifying Latent Concepts and Structures for Generalized Category Discovery](../conferences/icml-2026/cards/0801-0900.md#paper-dai26b)
- <a id="ding26f-representation-learning"></a>[DDSVM: A Differentiable Framework for Deep Support Vector Machines with Iterative Geometry-Aware Optimization](../conferences/icml-2026/cards/0901-1000.md#paper-ding26f)
- <a id="ding26n-representation-learning"></a>[Learning Gaussian Mixture-distributed Prototypes for 3D Scene Graph Generation from RGB-D Sequences](../conferences/icml-2026/cards/0901-1000.md#paper-ding26n)
- <a id="dou26b-representation-learning"></a>[DNA: Uncovering Universal Latent Forgery Knowledge](../conferences/icml-2026/cards/0901-1000.md#paper-dou26b)
- <a id="fang26o-representation-learning"></a>[Event2Vec: Processing neuromorphic events directly by representations in vector space](../conferences/icml-2026/cards/1001-1100.md#paper-fang26o)
- <a id="gao26ad-representation-learning"></a>[ArcDAE: Asymmetric Rectified Contrastive Diffusion Autoencoder for Unified Representation Learning](../conferences/icml-2026/cards/1201-1300.md#paper-gao26ad)
- <a id="garrido26a-representation-learning"></a>[Learning Latent Action World Models in the Wild](../conferences/icml-2026/cards/1201-1300.md#paper-garrido26a)
- <a id="guo26e-representation-learning"></a>[Compression as Adaptation: Implicit Visual Representation with Diffusion Foundation Models](../conferences/icml-2026/cards/1301-1400.md#paper-guo26e)

<a id="by-evaluation"></a>

### 评测与诊断

- <a id="acuaviva26a-evaluation"></a>[Rethinking Visual Intelligence: Insights from Video Pretraining](../conferences/icml-2026/cards/0001-0100.md#paper-acuaviva26a)
- <a id="ahmed26a-evaluation"></a>[Med-SegLens: Latent-Level Model Diffing for Interpretable Medical Image Segmentation](../conferences/icml-2026/cards/0001-0100.md#paper-ahmed26a)
- <a id="alexis26a-evaluation"></a>[GEPC: Group-Equivariant Posterior Consistency for Out-of-Distribution Detection in Diffusion Models](../conferences/icml-2026/cards/0001-0100.md#paper-alexis26a)
- <a id="baek26e-evaluation"></a>[Proactive Defense Benchmark against Deepfake Generation](../conferences/icml-2026/cards/0101-0200.md#paper-baek26e)
- <a id="braun26b-evaluation"></a>[Erased but Not Forgotten: How Backdoors Compromise Concept Erasure](../conferences/icml-2026/cards/0301-0400.md#paper-braun26b)
- <a id="chen26az-evaluation"></a>[Semantic-level Backdoor Attack against Text-to-Image Diffusion Models](../conferences/icml-2026/cards/0501-0600.md#paper-chen26az)
- <a id="chen26gw-evaluation"></a>[Efficient, Validation-Free Intrinsic Quality Estimation for Large-Scale Face Recognition Datasets](../conferences/icml-2026/cards/0601-0700.md#paper-chen26gw)
- <a id="chung26a-evaluation"></a>[Global Geometry Is Not Enough for Vision Representations](../conferences/icml-2026/cards/0701-0800.md#paper-chung26a)
- <a id="ebrahimpour-boroojeny26a-evaluation"></a>[Unlearning Isn’t Forgetting: Revealing Hidden Leakage in Class Unlearning Evaluations](../conferences/icml-2026/cards/1001-1100.md#paper-ebrahimpour-boroojeny26a)
- <a id="elisha26a-evaluation"></a>[ConEx: Human-Interpretable Saliency Maps via Concept-Aware Attribution](../conferences/icml-2026/cards/1001-1100.md#paper-elisha26a)
- <a id="fang26l-evaluation"></a>[iWorld-Bench: A Benchmark for Interactive World Models with a Unified Action Generation Framework](../conferences/icml-2026/cards/1001-1100.md#paper-fang26l)
- <a id="han26t-evaluation"></a>[GaussTrace: Provenance Analysis of 3D Gaussian Splatting Models with Evidence-based LLM Reasoning](../conferences/icml-2026/cards/1401-1500.md#paper-han26t)

<a id="by-theory-statistics"></a>

### 理论与统计

- <a id="bradley26a-theory-statistics"></a>[Local Mechanisms of Compositional Generalization in Conditional Diffusion](../conferences/icml-2026/cards/0301-0400.md#paper-bradley26a)
- <a id="brady26b-theory-statistics"></a>[Is Generation Required for Data-Efficient Perception?](../conferences/icml-2026/cards/0301-0400.md#paper-brady26b)
<!-- classification:end -->
