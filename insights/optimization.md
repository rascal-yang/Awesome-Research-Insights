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
- [宽度扩展后的优化器几何](../papers/llm.md#chen26eq-optimization) · Escaping the Subspace Trap: The Role of Optimizer Geometry in Model Width Expansion
- [MoE 专家组合剪枝](../papers/llm.md#chen26ew-optimization) · SCHUR-A*: Layer-wise Optimal Expert Pruning for MoEs via Schur-Complement Guided A* Search
- [遥测反馈驱动内核调优](../papers/llm.md#chen26ex-optimization) · QiMeng-PerceptOS: Semantic-Aware Kernel Optimization for OS-Intensive Workloads via Hardware-Software Alignment
- [偏好更新的梯度激励校准](../papers/llm.md#chen26fe-optimization) · Towards Disentangled Preference Optimization Dynamics: Suppress the Loser, Preserve the Winner
- [求解器程序树进化](../papers/llm.md#chen26hb-optimization) · $A_2$DEPT: Large Language Model–Driven Automated Algorithm Design via Evolutionary Program Trees
- [低秩二值权重量化](../papers/llm.md#chong26a-optimization) · NanoQuant: Efficient Sub-1-Bit Quantization of Large Language Models
- [MoE 通道贡献覆盖剪枝](../papers/llm.md#ding26q-optimization) · Attribution-Guided and Coverage-Maximized Pruning for Structural MoE Compression

### 计算机视觉

- [可微的随机特征点云配准](../papers/computer-vision.md#crane26a-optimization) · Scalable and Differentiable Point-Cloud Registration Using Maximum Mean Discrepancy
- [动态网格的逐面雅可比形变](../papers/computer-vision.md#dai26h-optimization) · TextMesh4D: Zero-shot Text-to-4D Mesh Generation
- [流模型逆问题的分段轨迹拼接](../papers/computer-vision.md#denker26a-optimization) · Trajectory Stitching for Solving Inverse Problems with Flow-Based Models
- [动态高斯属性平均](../papers/computer-vision.md#ding26p-optimization) · Improving Explicit Dynamic Gaussian Splatting Optimization via Update Mixture

### 强化学习

- [目标稳态分布约束下的快速混合](../papers/reinforcement-learning.md#corso26a-optimization) · Fast Mixing Steady-State Control in Markov Decision Processes
- [二阶平滑 Bellman 规划](../papers/reinforcement-learning.md#dam26a-optimization) · Second-Order Smooth Planning with Optimal-Transport Bellman Smoothing

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
- [LoRA 学习率的秩缩放](../papers/ml-foundations.md#chen26ei-optimization) · Learning Rate Scaling across LoRA Ranks and Transfer to Full Finetuning
- [分割联邦学习的混阶更新](../papers/ml-foundations.md#chen26fd-optimization) · HO-SFL: Hybrid-Order Split Federated Learning with Backprop-Free Clients and Dimension-Free Aggregation
- [持续学习的 LoRA 梯度修正](../papers/ml-foundations.md#chen26fz-optimization) · JANUS-LORA: A Balanced Low-Rank Adaptation for Continual Learning
- [集合元素污染的鲁棒优化](../papers/ml-foundations.md#chen26gg-optimization) · Distributionally Robust Set Representation Learning Under Inference-Time Element Corruption
- [结构鲁棒的 Gromov–Wasserstein 对齐](../papers/ml-foundations.md#cheng26f-optimization) · Achieving Structurally Robust Gromov Wasserstein Distance via Adaptive Dual-Mask
- [按梯度噪声调节更新方差](../papers/ml-foundations.md#choi26j-optimization) · Parameter Decorrelation via Transition-Variance Alignment for Multivariate Time-series Forecasting
- [一致可接受的随机方案查询](../papers/ml-foundations.md#choo26b-optimization) · Learning Unanimously Acceptable Lotteries via Queries
- [距离算子的凸最优传输](../papers/ml-foundations.md#chung26d-optimization) · Convex Distance Operator Transport: A Convex and Geometry-Preserving Formulation
- [混合整数求解的共形提前停止](../papers/ml-foundations.md#clarke26a-optimization) · Conformal Prediction for Early Stopping in Mixed Integer Optimization
- [在线最小化的对偶预测](../papers/ml-foundations.md#coester26a-optimization) · Learning-Augmented Online Minimization with Dual Predictions
- [带移动成本的图结构连续优化](../papers/ml-foundations.md#cortes26a-optimization) · Beyond Binary: Continuous State Optimization with Graph-Structured Objectives
- [Muon 的跨层范数步长](../papers/ml-foundations.md#crawshaw26a-optimization) · An Exploration of Non-Euclidean Gradient Descent: Muon and its Many Variants
- [预算可行的次模采购拍卖](../papers/ml-foundations.md#cui26b-optimization) · Budget-Feasible Mechanisms for Submodular Welfare Maximization in Procurement Auctions
- [跨优化迭代复用蒙特卡洛粒子](../papers/ml-foundations.md#cuin26a-optimization) · Efficient Stochastic Optimisation via Sequential Monte Carlo
- [SVRG 的变分后验校正](../papers/ml-foundations.md#daheim26a-optimization) · SVRG and Beyond via Posterior Correction
- [强污染下的单指标模型恢复](../papers/ml-foundations.md#das26a-optimization) · Convex Basins in Single-Index Model Loss Landscapes: Applications to Robust Recovery under Strong Adversarial Corruption
- [不确定最优传输的 Sinkhorn 变分推断](../papers/ml-foundations.md#de26a-optimization) · Variational Inference for Uncertain Optimal Transport via Sinkhorn Parametrization
- [持续学习的平衡态控制更新](../papers/ml-foundations.md#de-haan26a-optimization) · Continual Learning through Control Minimization
- [生成流的奖励引导合并](../papers/ml-foundations.md#de-santi26a-optimization) · A Unified Density Operator View of Flow Control and Merging
- [矩阵动量的逐行归一化预条件](../papers/ml-foundations.md#deng26q-optimization) · RMNP: Row-Momentum Normalized Preconditioning for Scalable Matrix-Based Optimization
- [无导数近端算子的分裂迭代](../papers/ml-foundations.md#di26a-optimization) · Operator Splitting with Hamilton-Jacobi-based Proximals
- [多任务分解的两阶段梯度校正](../papers/ml-foundations.md#ding26b-optimization) · Near-Optimal and Efficient First-Order Algorithm for Multi-Task Learning with Shared Linear Representation
- [数据清洗与 AutoML 的分时调度](../papers/ml-foundations.md#ding26l-optimization) · DMCO: Budget-Aware Co-Optimization of Data Cleaning and AutoML
- [约束优化的扩散自举精炼](../papers/ml-foundations.md#ding26aa-optimization) · Diffusion-based learning framework for Constrained Nonconvex Optimization with Weighted Bootstrapped Refinement
- [差分隐私梯度的滤波二阶矩校准](../papers/ml-foundations.md#dm26a-optimization) · FIBER: A Differentially Private Optimizer with Filter-Aware Innovation Bias Correction
- [同方向 Romberg 零阶梯度估计](../papers/ml-foundations.md#dong26j-optimization) · Romberg-Extrapolated Zeroth-Order Gradient Estimator: Higher-Order Bias Reduction with Preserved Leading Directional Variance
- [表格上下文预测的稀疏反事实改动](../papers/ml-foundations.md#dong26n-optimization) · Algorithmic Recourse of In-Context Learning for Tabular Data

### 图学习与推荐

- [图粗化](../papers/graph-and-recommendation.md#bai26g-optimization) · Rethinking Efficient Graph Coarsening via a Non-Selfishness Principle
- [公平排序聚合](../papers/graph-and-recommendation.md#chakraborty26b-optimization) · Fairness in Aggregation: Optimal Top-$k$ and Improved Full Ranking
- [隐私图查询](../papers/graph-and-recommendation.md#chen26b-optimization) · Differentially Private Range Subgraph Counting
- [关系数据库的任务感知图结构优化](../papers/graph-and-recommendation.md#cheng26j-optimization) · What Makes a Desired Graph for Relational Deep Learning?

### 科学机器学习

- [广义特征值积分轮廓](../papers/scientific-ml.md#chen26ck-optimization) · Learning-Guided Integration Contours Construction for Fast Large-Scale Generalized Eigensolvers
- [语言模型预测与真实实验的门控](../papers/scientific-ml.md#chen26fx-optimization) · LABO: LLM-Accelerated Bayesian Optimization through Broad Exploration and Selective Experimentation
<!-- classification:end -->
