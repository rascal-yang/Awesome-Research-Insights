# 优化

[首页](../README.md) · [参与贡献](../CONTRIBUTING.md) · [English](../en/insights/optimization.md)

梯度更新、参数化与优化过程。

<!-- classification:start -->
## 按研究领域浏览

### 大语言模型

- [模型压缩](../papers/llm.md#abbasi26a-optimization) · Zero Sum SVD: Balancing Loss Sensitivity for Low Rank LLM Compression
- [低显存零阶微调](../papers/llm.md#cai26a-optimization) · AdaMeZO: Adam-style Zeroth-Order Optimizer for LLM Fine-tuning Without Maintaining the Moments
- [LoRA 收敛](../papers/llm.md#castin26a-optimization) · Balanced LoRA: Removing Parameter Invariance to Accelerate Convergence
- [权重激活联合量化](../papers/llm.md#chen26z-optimization) · WUSH: Near-Optimal Adaptive Transforms for LLM Quantization
- [有约束的安全微调](../papers/llm.md#chen26ba-optimization) · SPARD: Defending Harmful Fine-Tuning Attack via Safety Projection with Relevance–Diversity Data Selection
- [多目标偏好梯度裁剪](../papers/llm.md#chen26bl-optimization) · Reward-free Alignment for Conflicting Objectives
- [可变网格低比特量化](../papers/llm.md#chen26bt-optimization) · BPDQ: Bit-Plane Decomposition Quantization on a Variable Grid for Large Language Models

### 机器人学

- [安全控制器混合](../papers/robotics.md#chaudhary26a-optimization) · Blending Neural Control Density Functions for Stabilization and Safety

### 机器学习基础与统计

- [约束优化](../papers/ml-foundations.md#abbas26a-optimization) · QuantumBoost: A lazy, yet fast, quantum algorithm for learning with weak hypotheses
- [极小极大优化](../papers/ml-foundations.md#abe26a-optimization) · Asymmetric Perturbation in Solving Bilinear Saddle-Point Optimization
- [黑盒优化](../papers/ml-foundations.md#ackermann26b-optimization) · Bridging Spherical Black-Box Optimizers
- [动态稀疏训练](../papers/ml-foundations.md#adnan26a-optimization) · SparseOpt: Addressing Normalization-induced Gradient Skew in Sparse Training
- [一次性剪枝](../papers/ml-foundations.md#afriat26a-optimization) · A Robust Optimization Guided Pruning Framework for Vision and Large Language Models
- [项目反应理论](../papers/ml-foundations.md#agarwal26d-optimization) · An Efficient Joint Learning Approach for Item Response Theory
- [分布式主成分分析](../papers/ml-foundations.md#aguie26a-optimization) · Improved Analysis of the Accelerated Noisy Power Method with Applications to Decentralized PCA
- [学习率预热](../papers/ml-foundations.md#alimisis26a-optimization) · Why Do We Need Warm-up? A Theoretical Perspective
- [时变随机优化](../papers/ml-foundations.md#amidzadeh26a-optimization) · Non-Parametric Optimization for Scalable Learning in Stochastic Decision Problems
- [可微粒子滤波](../papers/ml-foundations.md#andersson26b-optimization) · Diffusion Differentiable Resampling
- [随机优化稳定性](../papers/ml-foundations.md#andreyev26a-optimization) · Momentum Further Constrains Sharpness at the Edge of Stochastic Stability
- [随机梯度收敛](../papers/ml-foundations.md#apidopoulos26a-optimization) · Taming Stochastic Gradient Descent: Almost Sure Convergence and Saddle-Point Avoidance under $(L_0,L_1)$-Smoothness
- [去中心化优化](../papers/ml-foundations.md#armacki26a-optimization) · High-Probability Convergence Guarantees of Decentralized SGD
- [曲率估计](../papers/ml-foundations.md#artemev26a-optimization) · Exploiting weight-space symmetries for approximating curvature
- [学习率调参](../papers/ml-foundations.md#attia26a-optimization) · Learning Rate Annealing Improves Tuning Robustness in Stochastic Optimization
- [样本间梯度冲突](../papers/ml-foundations.md#avranas26a-optimization) · Reducing Per-Sample Interference in Stochastic Optimization
- [贝叶斯优化](../papers/ml-foundations.md#bafna26a-optimization) · Taking the GP Out of the Loop
- [Adam 收敛](../papers/ml-foundations.md#bai26m-optimization) · Towards Understanding Adam Convergence on Highly Degenerate Polynomials
- [优化稳定性](../papers/ml-foundations.md#bai26o-optimization) · Adaptive Preconditioners Trigger Loss Spikes in Adam
- [高维多模态采样](../papers/ml-foundations.md#baldassari26a-optimization) · Dimension-Free Multimodal Sampling via Preconditioned Annealed Langevin Dynamics
- [组合优化松弛](../papers/ml-foundations.md#banerjee26a-optimization) · Local-Minima-Preserving Polynomial Relaxation of Ising Problems
- [动态次模优化](../papers/ml-foundations.md#banihashem26c-optimization) · Improved Dynamic Algorithm for Non-monotone Submodular Maximization under Cardinality Constraint
- [个性化联邦学习](../papers/ml-foundations.md#bhatia26a-optimization) · CLoVE: Personalized Federated Learning through Clustering of Loss Vector Embeddings
- [联邦动态稀疏训练](../papers/ml-foundations.md#bi26b-optimization) · FedFit: Federated Dynamic Sparse Training via Fisher Information scoring
- [可逆扩散求解](../papers/ml-foundations.md#blasingame26a-optimization) · Rex: A Family of Reversible Exponential (Stochastic) Runge-Kutta Solvers
- [混合整数规划加速](../papers/ml-foundations.md#blin26a-optimization) · Batched First-Order Methods for Parallel LP Solving in MIP
- [变分推断](../papers/ml-foundations.md#borghi26a-optimization) · Variational inference via Gaussian interacting particles in the Bures-Wasserstein geometry
- [贝叶斯自适应实验](../papers/ml-foundations.md#bracher26a-optimization) · JADAI: Jointly Amortizing Adaptive Design and Bayesian Inference
- [谱梯度优化](../papers/ml-foundations.md#braun26a-optimization) · Spectral Gradient Descent Mitigates Anisotropy-Driven Misalignment: A Case Study in Phase Retrieval
- [Langevin 优化](../papers/ml-foundations.md#bruno26a-optimization) · Flatness-Aware Stochastic Gradient Langevin Dynamics
- [谱稀疏信号重建](../papers/ml-foundations.md#cai26j-optimization) · Fast Spectrally Sparse Signal Reconstruction via Jacobi-Preconditioned Gradient Descent
- [多核学习](../papers/ml-foundations.md#cao26ae-optimization) · Diversity-Aware Recursive Feature Multiple Kernel Learning
- [重尾随机镜像下降](../papers/ml-foundations.md#cauvin26a-optimization) · Bregman meets Lévy: Stochastic Mirror Descent with Heavy-Tailed Noise in Continuous and Discrete Time
- [Gauss–Newton 训练](../papers/ml-foundations.md#cayci26a-optimization) · Geometric Convergence of Gauss–Newton for Neural Networks: Riemannian Geometry and Adaptive Damping
- [在线变分估计](../papers/ml-foundations.md#chagneux26a-optimization) · Efficient Online Variational Estimation via Monte Carlo Sampling
- [随机约束优化](../papers/ml-foundations.md#chakraborty26c-optimization) · Randomized Feasibility Methods for Constrained Optimization with Adaptive Step Sizes
- [多仿射等式约束](../papers/ml-foundations.md#chao26a-optimization) · Last-iterate Convergence of ADMM on Multi-affine Quadratic Equality Constrained Problem
- [种群超参优化](../papers/ml-foundations.md#chebykin26a-optimization) · Iterated Population Based Training with Task-Agnostic Restarts
- [低秩压缩的 Fisher 近似](../papers/ml-foundations.md#chekalina26a-optimization) · Scalable Kronecker-Factored Fisher Approximation for Neural Network Parameter Sensitivity
- [污染下的分布鲁棒优化](../papers/ml-foundations.md#chen26e-optimization) · Bulk-Calibrated Credal Ambiguity Sets: Fast, Tractable Decision Making under Out-of-Sample Contamination
- [混合整数规划分支](../papers/ml-foundations.md#chen26ah-optimization) · Data-driven Mixed Integer Optimization through Probabilistic Multi-variable Branching
- [Adam 状态压缩](../papers/ml-foundations.md#chen26ax-optimization) · IO-Adam: Rethinking Memory-Efficient Adaptive Optimizers from Gradient Computation
- [核稀疏化的朗之万更新](../papers/ml-foundations.md#chen26bd-optimization) · Thinned Mean Field Langevin Dynamics
- [多步 SAM 邻域搜索](../papers/ml-foundations.md#chen26bo-optimization) · Understanding SAM through Minimax Perspective
- [受遗忘进度约束的模型更新](../papers/ml-foundations.md#chen26de-optimization) · How Hard Can It Be? Hardness-Aware Multi-Objective Unlearning

### 图学习与推荐

- [图粗化](../papers/graph-and-recommendation.md#bai26g-optimization) · Rethinking Efficient Graph Coarsening via a Non-Selfishness Principle
- [公平排序聚合](../papers/graph-and-recommendation.md#chakraborty26b-optimization) · Fairness in Aggregation: Optimal Top-$k$ and Improved Full Ranking
- [隐私图查询](../papers/graph-and-recommendation.md#chen26b-optimization) · Differentially Private Range Subgraph Counting

### 科学机器学习

- [广义特征值积分轮廓](../papers/scientific-ml.md#chen26ck-optimization) · Learning-Guided Integration Contours Construction for Fast Large-Scale Generalized Eigensolvers
<!-- classification:end -->
