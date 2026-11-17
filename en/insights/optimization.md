# Optimization

[Home](../../README.en.md) · [Contributing](../CONTRIBUTING.md) · [简体中文](../../insights/optimization.md)

Gradient updates, parameterization, and optimization dynamics.

<!-- classification:start -->
## Browse by Research Domain

[Large Language Models](#by-llm) · [Computer Vision](#by-computer-vision) · [Natural Language Processing](#by-nlp) · [Reinforcement Learning](#by-reinforcement-learning) · [Robotics](#by-robotics) · [Multimodal Learning](#by-multimodal) · [Machine Learning Foundations and Statistics](#by-ml-foundations) · [Graph Learning and Recommendation](#by-graph-and-recommendation) · [Scientific Machine Learning](#by-scientific-ml)

<a id="by-llm"></a>

### Large Language Models

- [Zero Sum SVD: Balancing Loss Sensitivity for Low Rank LLM Compression](../../conferences/icml-2026/cards/0001-0100.md#abbasi26a-optimization) · 中文
- [AdaMeZO: Adam-style Zeroth-Order Optimizer for LLM Fine-tuning Without Maintaining the Moments](../../conferences/icml-2026/cards/0301-0400.md#cai26a-optimization) · 中文
- [Balanced LoRA: Removing Parameter Invariance to Accelerate Convergence](../../conferences/icml-2026/cards/0401-0500.md#castin26a-optimization) · 中文
- [WUSH: Near-Optimal Adaptive Transforms for LLM Quantization](../../conferences/icml-2026/cards/0401-0500.md#chen26z-optimization) · 中文
- [SPARD: Defending Harmful Fine-Tuning Attack via Safety Projection with Relevance–Diversity Data Selection](../../conferences/icml-2026/cards/0501-0600.md#chen26ba-optimization) · 中文
- [Reward-free Alignment for Conflicting Objectives](../../conferences/icml-2026/cards/0501-0600.md#chen26bl-optimization) · 中文
- [BPDQ: Bit-Plane Decomposition Quantization on a Variable Grid for Large Language Models](../../conferences/icml-2026/cards/0501-0600.md#chen26bt-optimization) · 中文
- [Escaping the Subspace Trap: The Role of Optimizer Geometry in Model Width Expansion](../../conferences/icml-2026/cards/0601-0700.md#chen26eq-optimization) · 中文
- [SCHUR-A*: Layer-wise Optimal Expert Pruning for MoEs via Schur-Complement Guided A* Search](../../conferences/icml-2026/cards/0601-0700.md#chen26ew-optimization) · 中文
- [QiMeng-PerceptOS: Semantic-Aware Kernel Optimization for OS-Intensive Workloads via Hardware-Software Alignment](../../conferences/icml-2026/cards/0601-0700.md#chen26ex-optimization) · 中文
- [Towards Disentangled Preference Optimization Dynamics: Suppress the Loser, Preserve the Winner](../../conferences/icml-2026/cards/0601-0700.md#chen26fe-optimization) · 中文
- [$A_2$DEPT: Large Language Model–Driven Automated Algorithm Design via Evolutionary Program Trees](../../conferences/icml-2026/cards/0601-0700.md#chen26hb-optimization) · 中文
- [NanoQuant: Efficient Sub-1-Bit Quantization of Large Language Models](../../conferences/icml-2026/cards/0701-0800.md#chong26a-optimization) · 中文
- [Attribution-Guided and Coverage-Maximized Pruning for Structural MoE Compression](../../conferences/icml-2026/cards/0901-1000.md#ding26q-optimization) · 中文
- [CoCoQuant: Breaking the Bandwidth Wall via Co-Optimized Communication and Computation Quantization](../../conferences/icml-2026/cards/0901-1000.md#duanmu26a-optimization) · 中文
- [LOZO+: Provably Efficient Zeroth-Order Fine-Tuning via Greedy Low-Rank Subspace Selection](../../conferences/icml-2026/cards/1001-1100.md#fang26k-optimization) · 中文
- [Convex Optimization for Alignment and Preference Learning on a Single GPU](../../conferences/icml-2026/cards/1101-1200.md#feng26l-optimization) · 中文
- [Lookahead-GCG: Improving Universal Multi-Model Optimization-Based Jailbreaking Attacks via Stochastic Nesterov Optimization](../../conferences/icml-2026/cards/1101-1200.md#feng26y-optimization) · 中文
- [Memory-Efficient LLM Pretraining via Minimalist Optimizer Design](../../conferences/icml-2026/cards/1201-1300.md#glentis26a-optimization) · 中文
- [LATMiX: Learnable Affine Transformations for Microscaling Quantization of LLMs](../../conferences/icml-2026/cards/1301-1400.md#gordon26b-optimization) · 中文
- [OPIC: Enhancing Language Model Merging via Optimizing In-Context Capability](../../conferences/icml-2026/cards/1401-1500.md#he26a-optimization) · 中文
- [One LR Doesn’t Fit All: Heavy-Tail Guided Layerwise Learning Rates for LLMs](../../conferences/icml-2026/cards/1501-1600.md#he26ak-optimization) · 中文
- [Factored Gossip DiLoCo: Reducing Blocking Communication in DiLoCo](../../conferences/icml-2026/cards/1501-1600.md#hewa-koneputugodage26a-optimization) · 中文
- [MASPOB: Bandit-Based Prompt Optimization for Multi-Agent Systems with Graph Neural Networks](../../conferences/icml-2026/cards/1501-1600.md#hong26l-optimization) · 中文
- [EvoMAS: Evolutionary Generation of Multi-Agent Systems](../../conferences/icml-2026/cards/1601-1700.md#hu26bg-optimization) · 中文
- [RaGEP: Rank-aware Geometric Expert Pruning for Mixture-of-Experts Language Models](../../conferences/icml-2026/cards/1601-1700.md#hu26bj-optimization) · 中文
- [Spectra: Rethinking Optimizers for LLMs Under Spectral Anisotropy](../../conferences/icml-2026/cards/1601-1700.md#huang26d-optimization) · 中文
- [TextResNet: Decoupling and Routing Optimization Signals in Compound AI Systems via Deep Residual Tuning](../../conferences/icml-2026/cards/1701-1800.md#huang26aa-optimization) · 中文
- [When Model Merging Breaks Routing: Training-Free Calibration for MoE](../../conferences/icml-2026/cards/1701-1800.md#huang26au-optimization) · 中文
- [FAIR-Calib: Frontier-Aware Instability-Reweighted Calibration for Post-Training Quantization of Diffusion Large Language Models](../../conferences/icml-2026/cards/1701-1800.md#huang26br-optimization) · 中文
- [Deterministic Differentiable Structured Pruning for Large Language Models](../../conferences/icml-2026/cards/1701-1800.md#huang26cg-optimization) · 中文
- [CrispEdit: Low-Curvature Projections for Scalable Non-Destructive LLM Editing](../../conferences/icml-2026/cards/1801-1900.md#ikram26a-optimization) · 中文
- [Stabilizing Native Low-Rank LLM Pretraining](../../conferences/icml-2026/cards/1801-1900.md#janson26a-optimization) · 中文
- [DeltaEvolve: Accelerating Scientific Discovery through Momentum-Driven Evolution](../../conferences/icml-2026/cards/1901-2000.md#jiang26g-optimization) · 中文
- [Distributed Direct Preference Optimization](../../conferences/icml-2026/cards/1901-2000.md#jiang26h-optimization) · 中文
- [Enhancing LLM Training via Spectral Clipping](../../conferences/icml-2026/cards/1901-2000.md#jiang26am-optimization) · 中文
- [EvoGM: Learning to Merge LLMs via Evolutionary Generative Optimization](../../conferences/icml-2026/cards/1901-2000.md#jiang26az-optimization) · 中文
- [LoRDO: Distributed Low-Rank Optimization with Infrequent Communication](../../conferences/icml-2026/cards/2001-2100.md#jovanovic26a-optimization) · 中文
- [Mitigating Staleness in Asynchronous Pipeline Parallelism via Basis Rotation](../../conferences/icml-2026/cards/2001-2100.md#jung26h-optimization) · 中文
- [Automatic Pruning Discovery for Large Language Models](../../conferences/icml-2026/cards/2001-2100.md#kang26l-optimization) · 中文
- [Towards Solving the Gilbert-Pollak Conjecture via Large Language Models](../../conferences/icml-2026/cards/2001-2100.md#ke26a-optimization) · 中文
- [Game-Theoretic Co-Evolution for LLM-Based Heuristic Discovery](../../conferences/icml-2026/cards/2001-2100.md#ke26b-optimization) · 中文
- [TokenDrop: Token-Level Importance-Aware Backward Propagation Skipping for Efficient LLM Fine-Tuning](../../conferences/icml-2026/cards/2101-2200.md#kim26bc-optimization) · 中文
- [GSRQ: Gain-Shape Residual Quantization for Sub-1-bit KV Cache](../../conferences/icml-2026/cards/2101-2200.md#kim26bf-optimization) · 中文
- [Persona-Pruner: Sculpting Lightweight Models for Role-Playing](../../conferences/icml-2026/cards/2101-2200.md#kim26br-optimization) · 中文
- [ReSpinQuant: Efficient Layer-Wise LLM Quantization via Subspace Residual Rotation Approximation](../../conferences/icml-2026/cards/2101-2200.md#kim26bv-optimization) · 中文
- [Evolving Interpretable Constitutions for Multi-Agent Coordination](../../conferences/icml-2026/cards/2201-2300.md#kumar26f-optimization) · 中文
- [LittleBit-2: Maximizing the Spectral Energy Gain in Sub-1-Bit LLMs via Latent Geometry Alignment](../../conferences/icml-2026/cards/2301-2400.md#lee26y-optimization) · 中文
- [OSAQ: Outlier Self-Absorption for Accurate Low-bit LLM Quantization](../../conferences/icml-2026/cards/2401-2500.md#li26aj-optimization) · 中文
- [Low-cost Full Fine-tuning: Learning What to Update for LLMs](../../conferences/icml-2026/cards/2401-2500.md#li26ax-optimization) · 中文
- [OMAC: A Holistic Optimization Framework for LLM-Based Multi-Agent Collaboration](../../conferences/icml-2026/cards/2401-2500.md#li26bf-optimization) · 中文
- [Textual Stochastic Gradient Descent: Discrete Optimization of External Memory for Reasoning Language Agents](../../conferences/icml-2026/cards/2401-2500.md#li26bo-optimization) · 中文
- [Verbalized Bayesian Persuasion](../../conferences/icml-2026/cards/2401-2500.md#li26cw-optimization) · 中文
- [NorMuon: Making Muon more efficient and scalable](../../conferences/icml-2026/cards/2501-2600.md#li26dh-optimization) · 中文
- [WinQ: Accelerating Quantization-Aware Training of Language Models Around Saddle Points](../../conferences/icml-2026/cards/2501-2600.md#li26dr-optimization) · 中文
- [PRAC: Principal-Random Subspace for LLM Activation Compression and Memory-Efficient Training](../../conferences/icml-2026/cards/2601-2700.md#li26je-optimization) · 中文
- [Multilingual Safety Alignment Via Sparse Weight Editing](../../conferences/icml-2026/cards/2701-2800.md#liang26x-optimization) · 中文
- [WaterSIC: Information-Theoretically (Near) Optimal Linear Layer Quantization](../../conferences/icml-2026/cards/2701-2800.md#lifar26a-optimization) · 中文
- [NeUQI: Near-Optimal Uniform Quantization Parameter Initialization for Low-Bit LLMs](../../conferences/icml-2026/cards/2701-2800.md#lin26l-optimization) · 中文
- [AGoQ: Activation and Gradient Quantization for Memory-Efficient Distributed Training of LLMs](../../conferences/icml-2026/cards/2701-2800.md#lin26m-optimization) · 中文
- [AGZO: Activation-Guided Zeroth-Order Optimization for LLM Fine-Tuning](../../conferences/icml-2026/cards/2701-2800.md#lin26n-optimization) · 中文
- [From Backward Spreading to Forward Replay: Revisiting Target Construction in LLM Parameter Editing](../../conferences/icml-2026/cards/2801-2900.md#liu26ax-optimization) · 中文
- [Structured Progressive Knowledge Activation for LLM-Driven Neural Architecture Search](../../conferences/icml-2026/cards/2801-2900.md#liu26cm-optimization) · 中文

<a id="by-computer-vision"></a>

### Computer Vision

- [Scalable and Differentiable Point-Cloud Registration Using Maximum Mean Discrepancy](../../conferences/icml-2026/cards/0701-0800.md#crane26a-optimization) · 中文
- [TextMesh4D: Zero-shot Text-to-4D Mesh Generation](../../conferences/icml-2026/cards/0801-0900.md#dai26h-optimization) · 中文
- [Trajectory Stitching for Solving Inverse Problems with Flow-Based Models](../../conferences/icml-2026/cards/0801-0900.md#denker26a-optimization) · 中文
- [Improving Explicit Dynamic Gaussian Splatting Optimization via Update Mixture](../../conferences/icml-2026/cards/0901-1000.md#ding26p-optimization) · 中文
- [Navigating the Flatlands: Dual Adaptive Sharpness-Aware Minimization for Domain Generalization](../../conferences/icml-2026/cards/1501-1600.md#he26m-optimization) · 中文
- [Newton-coupled Dual-Teacher Semi-supervised Learning Framework](../../conferences/icml-2026/cards/1501-1600.md#he26ad-optimization) · 中文
- [AdLift: Lifting Adversarial Perturbations to Safeguard 3D Gaussian Splatting Assets Against Instruction-Driven Editing](../../conferences/icml-2026/cards/1501-1600.md#hong26c-optimization) · 中文
- [3DGS$^2$-TR: Scalable Second-Order Trust-Region Method for 3D Gaussian Splatting](../../conferences/icml-2026/cards/1601-1700.md#hsiao26a-optimization) · 中文
- [Gradient Preconditioning for Efficient and Reliable Reward-Guided Generation](../../conferences/icml-2026/cards/1701-1800.md#hwang26h-optimization) · 中文
- [Z-Erase: Enabling Concept Erasure in Single Stream Diffusion Transformers](../../conferences/icml-2026/cards/1901-2000.md#jiang26i-optimization) · 中文
- [A$^2$SG: Adaptive and Asymmetric Surrogate Gradients for Training Deep Spiking Neural Networks](../../conferences/icml-2026/cards/2001-2100.md#kang26g-optimization) · 中文
- [Crowd4D: Scene-Aware Monocular 4D Crowd Reconstruction](../../conferences/icml-2026/cards/2001-2100.md#kang26s-optimization) · 中文
- [Unlearning in Diffusion Models: A Unified Framework with KL Divergence and Likelihood Constraints](../../conferences/icml-2026/cards/2001-2100.md#khalafi26a-optimization) · 中文
- [MoCo-EA: Exploiting Adversarial Mode Connectivity for Efficient Evolutionary Attacks](../../conferences/icml-2026/cards/2101-2200.md#kim26ax-optimization) · 中文
- [Guaranteed Optimal Compositional Explanations for Neurons](../../conferences/icml-2026/cards/2201-2300.md#la-rosa26a-optimization) · 中文
- [MoCL: Metabolic Optimization for Curvature-Aware Continual Learning](../../conferences/icml-2026/cards/2201-2300.md#lai26d-optimization) · 中文
- [UOTIP: Unbalanced Optimal Transport Map for Unpaired Inverse Problems](../../conferences/icml-2026/cards/2301-2400.md#lee26ak-optimization) · 中文
- [Spatially-Adaptive Gradient Re-parameterization for 3D Large Kernel Optimization](../../conferences/icml-2026/cards/2301-2400.md#lee26as-optimization) · 中文
- [Prism-MoE: Efficient Dense-to-MoE Conversion for Visual Autoregressive Generation](../../conferences/icml-2026/cards/2501-2600.md#li26gy-optimization) · 中文
- [Unlocking the Potential of Continual Model Merging: An ODE Perspective](../../conferences/icml-2026/cards/2701-2800.md#lin26o-optimization) · 中文

<a id="by-nlp"></a>

### Natural Language Processing

- [Convex Low-resource Accent-Robust Language Detection in Speech Recognition](../../conferences/icml-2026/cards/1101-1200.md#feng26p-optimization) · 中文

<a id="by-reinforcement-learning"></a>

### Reinforcement Learning

- [Fast Mixing Steady-State Control in Markov Decision Processes](../../conferences/icml-2026/cards/0701-0800.md#corso26a-optimization) · 中文
- [Second-Order Smooth Planning with Optimal-Transport Bellman Smoothing](../../conferences/icml-2026/cards/0801-0900.md#dam26a-optimization) · 中文
- [Beyond the Bellman Recursion: A Pontryagin-Guided Framework for Non-Exponential Discounting](../../conferences/icml-2026/cards/2101-2200.md#ko26a-optimization) · 中文

<a id="by-robotics"></a>

### Robotics

- [Blending Neural Control Density Functions for Stabilization and Safety](../../conferences/icml-2026/cards/0401-0500.md#chaudhary26a-optimization) · 中文
- [De4D-SLAM: Gradient-Isolated Static-Dynamic Decoupling for Monocular SLAM in Dynamic Environments](../../conferences/icml-2026/cards/1001-1100.md#fan26g-optimization) · 中文
- [Optimal and Scalable MAPF via Multi-Marginal Optimal Transport and Schrödinger Bridges](../../conferences/icml-2026/cards/2001-2100.md#khan26a-optimization) · 中文

<a id="by-multimodal"></a>

### Multimodal Learning

- [MFH-NAS:A Hybrid Neural Architecture Search Framework for Multimodal Fusion Object Detection](../../conferences/icml-2026/cards/1201-1300.md#gao26an-optimization) · 中文
- [Spectral Imbalance Causes Forgetting in Low-Rank Continual Adaptation](../../conferences/icml-2026/cards/1301-1400.md#gu26i-optimization) · 中文
- [FRISM: Fine-Grained Reasoning Injection via Subspace-Level Model Merging for Vision–Language Models](../../conferences/icml-2026/cards/1701-1800.md#huang26bu-optimization) · 中文
- [Modality-Decoupled Online Recursive Editing](../../conferences/icml-2026/cards/2601-2700.md#li26ji-optimization) · 中文
- [UniFLoW: Universal Multi-Modal Federated LoRA Fine-Tuning Framework with Analytical Aggregation](../../conferences/icml-2026/cards/2701-2800.md#liang26ab-optimization) · 中文

<a id="by-ml-foundations"></a>

### Machine Learning Foundations and Statistics

- [QuantumBoost: A lazy, yet fast, quantum algorithm for learning with weak hypotheses](../../conferences/icml-2026/cards/0001-0100.md#abbas26a-optimization) · 中文
- [Asymmetric Perturbation in Solving Bilinear Saddle-Point Optimization](../../conferences/icml-2026/cards/0001-0100.md#abe26a-optimization) · 中文
- [Bridging Spherical Black-Box Optimizers](../../conferences/icml-2026/cards/0001-0100.md#ackermann26b-optimization) · 中文
- [SparseOpt: Addressing Normalization-induced Gradient Skew in Sparse Training](../../conferences/icml-2026/cards/0001-0100.md#adnan26a-optimization) · 中文
- [A Robust Optimization Guided Pruning Framework for Vision and Large Language Models](../../conferences/icml-2026/cards/0001-0100.md#afriat26a-optimization) · 中文
- [An Efficient Joint Learning Approach for Item Response Theory](../../conferences/icml-2026/cards/0001-0100.md#agarwal26d-optimization) · 中文
- [Improved Analysis of the Accelerated Noisy Power Method with Applications to Decentralized PCA](../../conferences/icml-2026/cards/0001-0100.md#aguie26a-optimization) · 中文
- [Why Do We Need Warm-up? A Theoretical Perspective](../../conferences/icml-2026/cards/0001-0100.md#alimisis26a-optimization) · 中文
- [Non-Parametric Optimization for Scalable Learning in Stochastic Decision Problems](../../conferences/icml-2026/cards/0001-0100.md#amidzadeh26a-optimization) · 中文
- [Diffusion Differentiable Resampling](../../conferences/icml-2026/cards/0001-0100.md#andersson26b-optimization) · 中文
- [Momentum Further Constrains Sharpness at the Edge of Stochastic Stability](../../conferences/icml-2026/cards/0001-0100.md#andreyev26a-optimization) · 中文
- [Taming Stochastic Gradient Descent: Almost Sure Convergence and Saddle-Point Avoidance under $(L_0,L_1)$-Smoothness](../../conferences/icml-2026/cards/0101-0200.md#apidopoulos26a-optimization) · 中文
- [High-Probability Convergence Guarantees of Decentralized SGD](../../conferences/icml-2026/cards/0101-0200.md#armacki26a-optimization) · 中文
- [Exploiting weight-space symmetries for approximating curvature](../../conferences/icml-2026/cards/0101-0200.md#artemev26a-optimization) · 中文
- [Learning Rate Annealing Improves Tuning Robustness in Stochastic Optimization](../../conferences/icml-2026/cards/0101-0200.md#attia26a-optimization) · 中文
- [Reducing Per-Sample Interference in Stochastic Optimization](../../conferences/icml-2026/cards/0101-0200.md#avranas26a-optimization) · 中文
- [Taking the GP Out of the Loop](../../conferences/icml-2026/cards/0101-0200.md#bafna26a-optimization) · 中文
- [Towards Understanding Adam Convergence on Highly Degenerate Polynomials](../../conferences/icml-2026/cards/0101-0200.md#bai26m-optimization) · 中文
- [Adaptive Preconditioners Trigger Loss Spikes in Adam](../../conferences/icml-2026/cards/0101-0200.md#bai26o-optimization) · 中文
- [Dimension-Free Multimodal Sampling via Preconditioned Annealed Langevin Dynamics](../../conferences/icml-2026/cards/0101-0200.md#baldassari26a-optimization) · 中文
- [Local-Minima-Preserving Polynomial Relaxation of Ising Problems](../../conferences/icml-2026/cards/0201-0300.md#banerjee26a-optimization) · 中文
- [Improved Dynamic Algorithm for Non-monotone Submodular Maximization under Cardinality Constraint](../../conferences/icml-2026/cards/0201-0300.md#banihashem26c-optimization) · 中文
- [CLoVE: Personalized Federated Learning through Clustering of Loss Vector Embeddings](../../conferences/icml-2026/cards/0201-0300.md#bhatia26a-optimization) · 中文
- [FedFit: Federated Dynamic Sparse Training via Fisher Information scoring](../../conferences/icml-2026/cards/0201-0300.md#bi26b-optimization) · 中文
- [Rex: A Family of Reversible Exponential (Stochastic) Runge-Kutta Solvers](../../conferences/icml-2026/cards/0201-0300.md#blasingame26a-optimization) · 中文
- [Batched First-Order Methods for Parallel LP Solving in MIP](../../conferences/icml-2026/cards/0201-0300.md#blin26a-optimization) · 中文
- [Variational inference via Gaussian interacting particles in the Bures-Wasserstein geometry](../../conferences/icml-2026/cards/0301-0400.md#borghi26a-optimization) · 中文
- [JADAI: Jointly Amortizing Adaptive Design and Bayesian Inference](../../conferences/icml-2026/cards/0301-0400.md#bracher26a-optimization) · 中文
- [Spectral Gradient Descent Mitigates Anisotropy-Driven Misalignment: A Case Study in Phase Retrieval](../../conferences/icml-2026/cards/0301-0400.md#braun26a-optimization) · 中文
- [Flatness-Aware Stochastic Gradient Langevin Dynamics](../../conferences/icml-2026/cards/0301-0400.md#bruno26a-optimization) · 中文
- [Fast Spectrally Sparse Signal Reconstruction via Jacobi-Preconditioned Gradient Descent](../../conferences/icml-2026/cards/0301-0400.md#cai26j-optimization) · 中文
- [Diversity-Aware Recursive Feature Multiple Kernel Learning](../../conferences/icml-2026/cards/0401-0500.md#cao26ae-optimization) · 中文
- [Bregman meets Lévy: Stochastic Mirror Descent with Heavy-Tailed Noise in Continuous and Discrete Time](../../conferences/icml-2026/cards/0401-0500.md#cauvin26a-optimization) · 中文
- [Geometric Convergence of Gauss–Newton for Neural Networks: Riemannian Geometry and Adaptive Damping](../../conferences/icml-2026/cards/0401-0500.md#cayci26a-optimization) · 中文
- [Efficient Online Variational Estimation via Monte Carlo Sampling](../../conferences/icml-2026/cards/0401-0500.md#chagneux26a-optimization) · 中文
- [Randomized Feasibility Methods for Constrained Optimization with Adaptive Step Sizes](../../conferences/icml-2026/cards/0401-0500.md#chakraborty26c-optimization) · 中文
- [Last-iterate Convergence of ADMM on Multi-affine Quadratic Equality Constrained Problem](../../conferences/icml-2026/cards/0401-0500.md#chao26a-optimization) · 中文
- [Iterated Population Based Training with Task-Agnostic Restarts](../../conferences/icml-2026/cards/0401-0500.md#chebykin26a-optimization) · 中文
- [Scalable Kronecker-Factored Fisher Approximation for Neural Network Parameter Sensitivity](../../conferences/icml-2026/cards/0401-0500.md#chekalina26a-optimization) · 中文
- [Bulk-Calibrated Credal Ambiguity Sets: Fast, Tractable Decision Making under Out-of-Sample Contamination](../../conferences/icml-2026/cards/0401-0500.md#chen26e-optimization) · 中文
- [Data-driven Mixed Integer Optimization through Probabilistic Multi-variable Branching](../../conferences/icml-2026/cards/0501-0600.md#chen26ah-optimization) · 中文
- [IO-Adam: Rethinking Memory-Efficient Adaptive Optimizers from Gradient Computation](../../conferences/icml-2026/cards/0501-0600.md#chen26ax-optimization) · 中文
- [Thinned Mean Field Langevin Dynamics](../../conferences/icml-2026/cards/0501-0600.md#chen26bd-optimization) · 中文
- [Understanding SAM through Minimax Perspective](../../conferences/icml-2026/cards/0501-0600.md#chen26bo-optimization) · 中文
- [How Hard Can It Be? Hardness-Aware Multi-Objective Unlearning](../../conferences/icml-2026/cards/0501-0600.md#chen26de-optimization) · 中文
- [Learning Rate Scaling across LoRA Ranks and Transfer to Full Finetuning](../../conferences/icml-2026/cards/0601-0700.md#chen26ei-optimization) · 中文
- [HO-SFL: Hybrid-Order Split Federated Learning with Backprop-Free Clients and Dimension-Free Aggregation](../../conferences/icml-2026/cards/0601-0700.md#chen26fd-optimization) · 中文
- [JANUS-LORA: A Balanced Low-Rank Adaptation for Continual Learning](../../conferences/icml-2026/cards/0601-0700.md#chen26fz-optimization) · 中文
- [Distributionally Robust Set Representation Learning Under Inference-Time Element Corruption](../../conferences/icml-2026/cards/0601-0700.md#chen26gg-optimization) · 中文
- [Achieving Structurally Robust Gromov Wasserstein Distance via Adaptive Dual-Mask](../../conferences/icml-2026/cards/0601-0700.md#cheng26f-optimization) · 中文
- [Parameter Decorrelation via Transition-Variance Alignment for Multivariate Time-series Forecasting](../../conferences/icml-2026/cards/0701-0800.md#choi26j-optimization) · 中文
- [Learning Unanimously Acceptable Lotteries via Queries](../../conferences/icml-2026/cards/0701-0800.md#choo26b-optimization) · 中文
- [Convex Distance Operator Transport: A Convex and Geometry-Preserving Formulation](../../conferences/icml-2026/cards/0701-0800.md#chung26d-optimization) · 中文
- [Conformal Prediction for Early Stopping in Mixed Integer Optimization](../../conferences/icml-2026/cards/0701-0800.md#clarke26a-optimization) · 中文
- [Learning-Augmented Online Minimization with Dual Predictions](../../conferences/icml-2026/cards/0701-0800.md#coester26a-optimization) · 中文
- [Beyond Binary: Continuous State Optimization with Graph-Structured Objectives](../../conferences/icml-2026/cards/0701-0800.md#cortes26a-optimization) · 中文
- [An Exploration of Non-Euclidean Gradient Descent: Muon and its Many Variants](../../conferences/icml-2026/cards/0701-0800.md#crawshaw26a-optimization) · 中文
- [Budget-Feasible Mechanisms for Submodular Welfare Maximization in Procurement Auctions](../../conferences/icml-2026/cards/0701-0800.md#cui26b-optimization) · 中文
- [Efficient Stochastic Optimisation via Sequential Monte Carlo](../../conferences/icml-2026/cards/0801-0900.md#cuin26a-optimization) · 中文
- [SVRG and Beyond via Posterior Correction](../../conferences/icml-2026/cards/0801-0900.md#daheim26a-optimization) · 中文
- [Convex Basins in Single-Index Model Loss Landscapes: Applications to Robust Recovery under Strong Adversarial Corruption](../../conferences/icml-2026/cards/0801-0900.md#das26a-optimization) · 中文
- [Variational Inference for Uncertain Optimal Transport via Sinkhorn Parametrization](../../conferences/icml-2026/cards/0801-0900.md#de26a-optimization) · 中文
- [Continual Learning through Control Minimization](../../conferences/icml-2026/cards/0801-0900.md#de-haan26a-optimization) · 中文
- [A Unified Density Operator View of Flow Control and Merging](../../conferences/icml-2026/cards/0801-0900.md#de-santi26a-optimization) · 中文
- [RMNP: Row-Momentum Normalized Preconditioning for Scalable Matrix-Based Optimization](../../conferences/icml-2026/cards/0801-0900.md#deng26q-optimization) · 中文
- [Operator Splitting with Hamilton-Jacobi-based Proximals](../../conferences/icml-2026/cards/0801-0900.md#di26a-optimization) · 中文
- [Near-Optimal and Efficient First-Order Algorithm for Multi-Task Learning with Shared Linear Representation](../../conferences/icml-2026/cards/0901-1000.md#ding26b-optimization) · 中文
- [DMCO: Budget-Aware Co-Optimization of Data Cleaning and AutoML](../../conferences/icml-2026/cards/0901-1000.md#ding26l-optimization) · 中文
- [Diffusion-based learning framework for Constrained Nonconvex Optimization with Weighted Bootstrapped Refinement](../../conferences/icml-2026/cards/0901-1000.md#ding26aa-optimization) · 中文
- [FIBER: A Differentially Private Optimizer with Filter-Aware Innovation Bias Correction](../../conferences/icml-2026/cards/0901-1000.md#dm26a-optimization) · 中文
- [Romberg-Extrapolated Zeroth-Order Gradient Estimator: Higher-Order Bias Reduction with Preserved Leading Directional Variance](../../conferences/icml-2026/cards/0901-1000.md#dong26j-optimization) · 中文
- [Algorithmic Recourse of In-Context Learning for Tabular Data](../../conferences/icml-2026/cards/0901-1000.md#dong26n-optimization) · 中文
- [Fast kernel methods: Sobolev, physics-informed, and additive models](../../conferences/icml-2026/cards/0901-1000.md#doumeche26a-optimization) · 中文
- [Meta-Black-Box Optimization Can Do Search Guidance for Expensive Constrained Multi-Objective Optimization](../../conferences/icml-2026/cards/0901-1000.md#du26r-optimization) · 中文
- [A General Framework for Dynamic Consistent Submodular Maximization](../../conferences/icml-2026/cards/0901-1000.md#duetting26a-optimization) · 中文
- [Mixtures Closest To A Given Measure: A Semidefinite Programming Approach](../../conferences/icml-2026/cards/0901-1000.md#durasinovic26a-optimization) · 中文
- [Variational Entropic Optimal Transport](../../conferences/icml-2026/cards/1001-1100.md#dyachenko26a-optimization) · 中文
- [Learning Permutation from Structure Without Supervision](../../conferences/icml-2026/cards/1001-1100.md#eisenberg26a-optimization) · 中文
- [TSP with Predictions: Heatmap to Tour with Provable Guarantees](../../conferences/icml-2026/cards/1001-1100.md#elias26a-optimization) · 中文
- [Solving Positive Linear Programs with Differential Privacy](../../conferences/icml-2026/cards/1001-1100.md#ene26a-optimization) · 中文
- [Learning Randomized Reductions](../../conferences/icml-2026/cards/1001-1100.md#erata26a-optimization) · 中文
- [Clipping Makes Distributed and Federated Asynchronous SGD Robust to Stragglers](../../conferences/icml-2026/cards/1001-1100.md#erickson26a-optimization) · 中文
- [Robust Bayesian Optimisation with Unbounded Corruptions](../../conferences/icml-2026/cards/1001-1100.md#ezzerg26a-optimization) · 中文
- [ASAP: Exploiting the Satisficing Generalization Edge in Neural Combinatorial Optimization](../../conferences/icml-2026/cards/1001-1100.md#fang26t-optimization) · 中文
- [Solving the Offline and Online Min-Max Problem of Non-smooth Submodular-Concave Functions: A Zeroth-Order Approach](../../conferences/icml-2026/cards/1001-1100.md#farzin26a-optimization) · 中文
- [Dissecting Quantization Error: A Concentration-Alignment Perspective](../../conferences/icml-2026/cards/1001-1100.md#federici26a-optimization) · 中文
- [Learning in the Fisher Subspace: A Guided Initialization for LoRA Fine-Tuning](../../conferences/icml-2026/cards/1101-1200.md#feng26h-optimization) · 中文
- [Unsupervised Diffusion Solver for Combinatorial Optimization via Combinatorial Adjoint Matching](../../conferences/icml-2026/cards/1101-1200.md#feng26o-optimization) · 中文
- [Softsign: Smooth Sign in Your Optimizer For Better Parameter Heterogeneity Handling](../../conferences/icml-2026/cards/1101-1200.md#feoktistov26a-optimization) · 中文
- [CLASP: Online learning algorithms for Convex Losses And Squared Penalties](../../conferences/icml-2026/cards/1101-1200.md#ferreira26a-optimization) · 中文
- [Capacitated Fair-Range Clustering: Hardness and Approximation Algorithms](../../conferences/icml-2026/cards/1101-1200.md#gadekar26a-optimization) · 中文
- [Flatland: The Adventures of Gradient Descent with Large Step Sizes](../../conferences/icml-2026/cards/1101-1200.md#galli26a-optimization) · 中文
- [Inference from Quantized Data via Normal Variance-Mean Mixtures](../../conferences/icml-2026/cards/1201-1300.md#gao26ah-optimization) · 中文
- [Projection-Free Algorithms for Minimax Problems](../../conferences/icml-2026/cards/1201-1300.md#giang-tran26a-optimization) · 中文
- [Improved Stochastic Optimization of LogSumExp](../../conferences/icml-2026/cards/1201-1300.md#gladin26a-optimization) · 中文
- [ePC: Fast and Deep Predictive Coding in Digital Simulation](../../conferences/icml-2026/cards/1201-1300.md#goemaere26a-optimization) · 中文
- [A Sketch-and-Project Analysis of Subsampled Natural Gradient Algorithms](../../conferences/icml-2026/cards/1201-1300.md#goldshlager26a-optimization) · 中文
- [FlashOptim: Optimizers for Memory-Efficient Training](../../conferences/icml-2026/cards/1301-1400.md#gonzalez-ortiz26a-optimization) · 中文
- [Black-Box Combinatorial Optimization with Order-Invariant Reinforcement Learning](../../conferences/icml-2026/cards/1301-1400.md#goudet26a-optimization) · 中文
- [Categorical Reparameterization with Denoising Diffusion Models](../../conferences/icml-2026/cards/1301-1400.md#gourevitch26a-optimization) · 中文
- [Multi-marginal temporal Schrödinger Bridge Matching from unpaired data](../../conferences/icml-2026/cards/1301-1400.md#gravier26a-optimization) · 中文
- [Tensor Train Diffusion: Leveraging Low-Rank Structures for High-Dimensional Score-Based Sampling](../../conferences/icml-2026/cards/1301-1400.md#gruhlke26a-optimization) · 中文
- [Mirror Mean-Field Langevin Dynamics](../../conferences/icml-2026/cards/1301-1400.md#gu26e-optimization) · 中文
- [Parameter-Masked Decoupled Optimization for Cross-Domain Class-Incremental Learning](../../conferences/icml-2026/cards/1301-1400.md#gu26n-optimization) · 中文
- [Constrained Bayesian Experimental Design via Online Planning](../../conferences/icml-2026/cards/1301-1400.md#guo26g-optimization) · 中文
- [Discrete Adjoint Schrödinger Bridge Sampler](../../conferences/icml-2026/cards/1401-1500.md#guo26al-optimization) · 中文
- [Maximin Relative Improvement: Fair Learning as a Bargaining Problem](../../conferences/icml-2026/cards/1401-1500.md#han26a-optimization) · 中文
- [Optimal Pricing for Data-Augmented AutoML Marketplaces](../../conferences/icml-2026/cards/1401-1500.md#han26w-optimization) · 中文
- [Geodesic Calculus on Implicitly Defined Latent Manifolds](../../conferences/icml-2026/cards/1401-1500.md#hartwig26a-optimization) · 中文
- [Bottleneck Communication Delay Minimization for Communication-Efficient Decentralized Learning](../../conferences/icml-2026/cards/1401-1500.md#hata26a-optimization) · 中文
- [Minibatch Optimal Transport and Perplexity Bound Estimation in Discrete Flow Matching](../../conferences/icml-2026/cards/1401-1500.md#haxholli26a-optimization) · 中文
- [Compress then Merge: From Multiple LoRAs into One Low-Rank Adapter](../../conferences/icml-2026/cards/1501-1600.md#he26h-optimization) · 中文
- [From Rashomon Theory to PRAXIS: Efficient Decision Tree Rashomon Sets](../../conferences/icml-2026/cards/1501-1600.md#heile26a-optimization) · 中文
- [Ambiguous Strategic Classification](../../conferences/icml-2026/cards/1501-1600.md#hikri26a-optimization) · 中文
- [Near-Universal Multiplicative Updates for Nonnegative Einsum Factorization](../../conferences/icml-2026/cards/1501-1600.md#hood26a-optimization) · 中文
- [Gromov-Wasserstein at Scale, Beyond Squared Norms](../../conferences/icml-2026/cards/1601-1700.md#houry26a-optimization) · 中文
- [Score-Repellent Monte Carlo: Toward Efficient Non-Markovian Sampler with Constant Memory in General State Spaces](../../conferences/icml-2026/cards/1601-1700.md#hu26g-optimization) · 中文
- [Learning the Best Under Constraints: A Duality-Based Framework](../../conferences/icml-2026/cards/1601-1700.md#hu26bi-optimization) · 中文
- [Unsupervised Neural Langevin Sampler for Mixed Integer Linear Programming](../../conferences/icml-2026/cards/1601-1700.md#huang26j-optimization) · 中文
- [ALAS: Additive Learnable Alpha-Stable Kernels for Flexible Bayesian Optimization](../../conferences/icml-2026/cards/1701-1800.md#huang26o-optimization) · 中文
- [Robust Learning via Nested Distributionally Robust Optimization](../../conferences/icml-2026/cards/1701-1800.md#huang26u-optimization) · 中文
- [SURGE: Surrogate Gradient Adaptation in Binary Neural Networks](../../conferences/icml-2026/cards/1701-1800.md#huang26ah-optimization) · 中文
- [LiMuon: Light and Fast Muon Optimizer for Large Models](../../conferences/icml-2026/cards/1701-1800.md#huang26aj-optimization) · 中文
- [Local Minima in Quadratic-Penalty Relaxations of Binary Linear Programs](../../conferences/icml-2026/cards/1701-1800.md#huang26aw-optimization) · 中文
- [GradientStabilizer: Fix the Norm, Not the Gradient](../../conferences/icml-2026/cards/1701-1800.md#huang26bb-optimization) · 中文
- [Discretely-Refined Multi-view Clustering via Aligned Anchor Learning](../../conferences/icml-2026/cards/1701-1800.md#huang26bg-optimization) · 中文
- [HONet: Data-Efficient Learning for Exact Cover Tasks via Hypergraph Optimization](../../conferences/icml-2026/cards/1701-1800.md#huang26cn-optimization) · 中文
- [A hitchhiker’s guide to Poisson gradient estimation](../../conferences/icml-2026/cards/1801-1900.md#ibrahim26a-optimization) · 中文
- [Unlearning with Asymmetric Sources: Improved Unlearning-Utility Trade-off with Public Data](../../conferences/icml-2026/cards/1801-1900.md#inane26a-optimization) · 中文
- [On the Role of Batch Size in Stochastic Conditional Gradient Methods](../../conferences/icml-2026/cards/1801-1900.md#islamov26b-optimization) · 中文
- [An Embarrassingly Simple Way to Optimize Orthogonal Matrices at Scale](../../conferences/icml-2026/cards/1801-1900.md#javaloy26a-optimization) · 中文
- [SC-FAGC: Size Constrained Fast Anchor Graph Clustering](../../conferences/icml-2026/cards/1901-2000.md#jiachen26a-optimization) · 中文
- [Private Learning with Public Feature Conditioning](../../conferences/icml-2026/cards/1901-2000.md#jiang26w-optimization) · 中文
- [Local Constrained Bayesian Optimization](../../conferences/icml-2026/cards/1901-2000.md#jing26c-optimization) · 中文
- [Multimarginal flow matching with optimal transport potentials](../../conferences/icml-2026/cards/2001-2100.md#kansal26a-optimization) · 中文
- [Adaptive Momentum and Nonlinear Damping for Neural Network Training](../../conferences/icml-2026/cards/2001-2100.md#karoni26a-optimization) · 中文
- [Align Forward, Adapt Backward: Closing the Discretization Gap in Logic Gate Networks](../../conferences/icml-2026/cards/2001-2100.md#kim26a-optimization) · 中文
- [Riemannian Diffusion Models on General Manifolds via Physics-Informed Neural Networks](../../conferences/icml-2026/cards/2101-2200.md#ko26d-optimization) · 中文
- [LILO: Bayesian Optimization with Natural Language Feedback](../../conferences/icml-2026/cards/2101-2200.md#kobalczyk26a-optimization) · 中文
- [Incorporating Importance Weighting in Optimal Transport Based Domain Alignment](../../conferences/icml-2026/cards/2101-2200.md#koc26a-optimization) · 中文
- [Natural Hypergradient Descent: Algorithm Design, Convergence Analysis, and Parallel Implementation](../../conferences/icml-2026/cards/2101-2200.md#kong26a-optimization) · 中文
- [Finding Most Influential Sets](../../conferences/icml-2026/cards/2101-2200.md#konrad26a-optimization) · 中文
- [The Theory and Practice of MAP Inference over Non-Convex Constraints](../../conferences/icml-2026/cards/2201-2300.md#kurscheidt26a-optimization) · 中文
- [Search Space Synthesis for Parametric Functions](../../conferences/icml-2026/cards/2201-2300.md#laarmann26a-optimization) · 中文
- [Path-conditioned training: a principled way to rescale ReLU neural networks](../../conferences/icml-2026/cards/2201-2300.md#lebeurrier26a-optimization) · 中文
- [Decision-Focused Learning via Tangent-Space Projection of Prediction Error](../../conferences/icml-2026/cards/2301-2400.md#lee26q-optimization) · 中文
- [Optimal Design for Multinomial Logit Model with Applications to Best Assortment Identification](../../conferences/icml-2026/cards/2301-2400.md#lee26ba-optimization) · 中文
- [Two-Stage Unit Tying for Simplifying Differentiable Logic Gate Networks](../../conferences/icml-2026/cards/2301-2400.md#lee26bg-optimization) · 中文
- [Near-Optimal Private Linear Regression via Iterative Hessian Mixing](../../conferences/icml-2026/cards/2301-2400.md#lev26a-optimization) · 中文
- [Improving the Robustness-Utility Trade-off in Decentralized Learning over Sparse Networks](../../conferences/icml-2026/cards/2401-2500.md#li26i-optimization) · 中文
- [MoSSP: A Momentum-Based Single-Loop Stochastic Penalty Method for Nonconvex Constrained DC-regularized Optimization](../../conferences/icml-2026/cards/2401-2500.md#li26ab-optimization) · 中文
- [Large Scale Manifold Balanced Clustering](../../conferences/icml-2026/cards/2401-2500.md#li26as-optimization) · 中文
- [Breaking Multi-Task Curse: Reward-Weighted Evolution for Black-Box Many-Task Optimization](../../conferences/icml-2026/cards/2401-2500.md#li26dc-optimization) · 中文
- [Cross-task Calibration for Asynchronous Federated Continual Learning](../../conferences/icml-2026/cards/2501-2600.md#li26gx-optimization) · 中文
- [Probability of Matching for Batch Multi-Objective Bayesian Optimization](../../conferences/icml-2026/cards/2601-2700.md#li26iu-optimization) · 中文
- [Eliminating Solution Bias in Differentially Private Optimization](../../conferences/icml-2026/cards/2601-2700.md#li26iy-optimization) · 中文
- [M+Adam: Low-Precision Training via Additive–Multiplicative Optimization](../../conferences/icml-2026/cards/2701-2800.md#liang26p-optimization) · 中文
- [Turning Stale Gradients into Stable Gradients: Coherent Coordinate Descent with Implicit Landscape Smoothing for Lightweight Zeroth-Order Optimization](../../conferences/icml-2026/cards/2701-2800.md#liang26u-optimization) · 中文
- [L-SR1: Learned Symmetric-Rank-One Preconditioning](../../conferences/icml-2026/cards/2701-2800.md#lifshitz26a-optimization) · 中文
- [SAGE-NAS: Synergizing LLM-Based Semantic Agent with Graph-Based Evaluator for Neural Architecture Search](../../conferences/icml-2026/cards/2701-2800.md#lin26ac-optimization) · 中文
- [A Penalty Approach For Differentiation Through Black-box Quadratic Programming Solvers](../../conferences/icml-2026/cards/2701-2800.md#linghu26b-optimization) · 中文
- [Less Data, Faster Training: repeating smaller datasets speeds up learning via sampling biases](../../conferences/icml-2026/cards/2801-2900.md#liu26ad-optimization) · 中文
- [Minimizing Upper Confidence Bounds: A Data-Driven Framework for Stochastic Programming](../../conferences/icml-2026/cards/2801-2900.md#liu26al-optimization) · 中文
- [Row-Stochastic Matrices Can Provably Outperform Doubly Stochastic Matrices in Decentralized Learning](../../conferences/icml-2026/cards/2801-2900.md#liu26bv-optimization) · 中文
- [Hom-PGD$^+$: Fast Reparameterized Optimization over Non-convex Ball-Homeomorphic Set](../../conferences/icml-2026/cards/2801-2900.md#liu26cd-optimization) · 中文

<a id="by-graph-and-recommendation"></a>

### Graph Learning and Recommendation

- [Rethinking Efficient Graph Coarsening via a Non-Selfishness Principle](../../conferences/icml-2026/cards/0101-0200.md#bai26g-optimization) · 中文
- [Fairness in Aggregation: Optimal Top-$k$ and Improved Full Ranking](../../conferences/icml-2026/cards/0401-0500.md#chakraborty26b-optimization) · 中文
- [Differentially Private Range Subgraph Counting](../../conferences/icml-2026/cards/0401-0500.md#chen26b-optimization) · 中文
- [What Makes a Desired Graph for Relational Deep Learning?](../../conferences/icml-2026/cards/0601-0700.md#cheng26j-optimization) · 中文
- [Adapting to Evolving Graphs: A Scalable Framework for Dynamic Coarsening](../../conferences/icml-2026/cards/1401-1500.md#gupta26b-optimization) · 中文
- [Neural Dispersion on Graphs](../../conferences/icml-2026/cards/1601-1700.md#hosseini26b-optimization) · 中文
- [Homophily-Heterogeneity Gradient Surgery for Federated Graph Learning](../../conferences/icml-2026/cards/1601-1700.md#huang26k-optimization) · 中文
- [Attributed Network Alignment: Statistical Limits and Efficient Algorithm](../../conferences/icml-2026/cards/1701-1800.md#huang26az-optimization) · 中文
- [Towards Generative Graph Matching for Graph Edit Distance Computation](../../conferences/icml-2026/cards/1701-1800.md#huang26bi-optimization) · 中文
- [Optimal Transport–Guided Stochastic Control for Graph Combinatorial Optimization](../../conferences/icml-2026/cards/1701-1800.md#huang26bz-optimization) · 中文
- [Generative Large Neighborhood Search: Scalable Set Cover Optimization via Discrete Diffusion](../../conferences/icml-2026/cards/1801-1900.md#jaziri26a-optimization) · 中文
- [An Approximation Algorithm for Graph Label Selection](../../conferences/icml-2026/cards/1901-2000.md#john26a-optimization) · 中文
- [Fully Dynamic Coreset Spectral Clustering](../../conferences/icml-2026/cards/2001-2100.md#jourdan26a-optimization) · 中文
- [FairRARI: A Plug and Play Framework for Fairness-Aware PageRank](../../conferences/icml-2026/cards/2001-2100.md#kariotakis26a-optimization) · 中文
- [GraphFLEx: Unsupervised Structure Learning $\underline\textF$ramework for $\underline\textL$arge $\underline\textEx$panding $\underline\textGraph$s](../../conferences/icml-2026/cards/2001-2100.md#kataria26a-optimization) · 中文
- [COPF: An Online Framework for Deployment-Stable Counterfactual Fairness in Evolving Graphs](../../conferences/icml-2026/cards/2601-2700.md#li26kb-optimization) · 中文

<a id="by-scientific-ml"></a>

### Scientific Machine Learning

- [Learning-Guided Integration Contours Construction for Fast Large-Scale Generalized Eigensolvers](../../conferences/icml-2026/cards/0501-0600.md#chen26ck-optimization) · 中文
- [LABO: LLM-Accelerated Bayesian Optimization through Broad Exploration and Selective Experimentation](../../conferences/icml-2026/cards/0601-0700.md#chen26fx-optimization) · 中文
- [Plug-and-Play Diffusion Meets ADMM: Dual-Variable Coupling for Robust Medical Image Reconstruction](../../conferences/icml-2026/cards/0901-1000.md#du26n-optimization) · 中文
- [Automatic Construction of Clinical Scoring Systems with LLM Agents](../../conferences/icml-2026/cards/1001-1100.md#estevez26a-optimization) · 中文
- [RAPNet: Accelerating Algebraic Multigrid with Learned Sparse Corrections](../../conferences/icml-2026/cards/1101-1200.md#fink26a-optimization) · 中文
- [Excited Pfaffians: Generalized Neural Wave Functions Across Structure and State](../../conferences/icml-2026/cards/1201-1300.md#gao26j-optimization) · 中文
- [Torus Graphs for Large Scale Neural Phase Analysis](../../conferences/icml-2026/cards/1201-1300.md#goffinet26b-optimization) · 中文
- [Geometry-Aware Neural Optimizer for Shape Optimization and Inversion](../../conferences/icml-2026/cards/1401-1500.md#guoze26a-optimization) · 中文
- [Constrained Flow Optimization via Sequential Fine-Tuning for Molecular Design](../../conferences/icml-2026/cards/1401-1500.md#gutjahr26a-optimization) · 中文
- [Target-Aware Bandit Allocation for Scalable Surrogate Optimization in Chemical Space](../../conferences/icml-2026/cards/1401-1500.md#haddadnia26a-optimization) · 中文
- [Optimizing Network Simulation: Enhancing Performance Prediction Accuracy via Neural Architecture Search](../../conferences/icml-2026/cards/1501-1600.md#he26bb-optimization) · 中文
- [LLM4Branch: Large Language Model for Discovering Efficient Branching Policies of Integer Programs](../../conferences/icml-2026/cards/1601-1700.md#hou26d-optimization) · 中文
- [Steering Large Language Models through the DMTA Cycle: Structure-Based Drug Design via Knowledge-Driven Bi-Level Thompson Sampling](../../conferences/icml-2026/cards/1601-1700.md#hu26av-optimization) · 中文
- [Decision-focused Sparse Tangent Portfolio Optimization](../../conferences/icml-2026/cards/1801-1900.md#jeon26a-optimization) · 中文
- [Efficient Diffusion Models under Nonconvex Equality and Inequality constraints via Landing](../../conferences/icml-2026/cards/1801-1900.md#jeon26d-optimization) · 中文
- [SwitchCraft: A Programmatic Framework for Designing State-Switching Proteins](../../conferences/icml-2026/cards/1901-2000.md#jing26a-optimization) · 中文
- [Credit Assignment via Neural Manifold Noise Correlation](../../conferences/icml-2026/cards/2001-2100.md#kang26n-optimization) · 中文
- [LeakGFN: Robust Molecular Generation in Generative Flow Networks via Flow Decomposition](../../conferences/icml-2026/cards/2001-2100.md#kim26j-optimization) · 中文
- [Causal Structure Learning for Sparse Matrix Fill-in Reduction](../../conferences/icml-2026/cards/2501-2600.md#li26el-optimization) · 中文
- [G-RANS: Generalizable Residual-Aware Neural Solvers for Sparse Systems](../../conferences/icml-2026/cards/2701-2800.md#liao26a-optimization) · 中文
- [Stabilizing Equation Learning via Zero-Point Constraints](../../conferences/icml-2026/cards/2701-2800.md#liu26n-optimization) · 中文
- [UniDrag: Unified Multi-Field Prediction and Robust Shape Optimization for Vehicle Aerodynamics](../../conferences/icml-2026/cards/2801-2900.md#liu26cn-optimization) · 中文
<!-- classification:end -->
