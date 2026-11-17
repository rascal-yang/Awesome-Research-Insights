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
- [张量并行的计算通信联合量化](../papers/llm.md#duanmu26a-optimization) · CoCoQuant: Breaking the Bandwidth Wall via Co-Optimized Communication and Computation Quantization
- [零阶微调的贪心子空间筛选](../papers/llm.md#fang26k-optimization) · LOZO+: Provably Efficient Zeroth-Order Fine-Tuning via Greedy Low-Rank Subspace Selection
- [冻结主干的凸偏好对齐](../papers/llm.md#feng26l-optimization) · Convex Optimization for Alignment and Preference Learning on a Single GPU
- [多模型红队搜索的嵌入动量](../papers/llm.md#feng26y-optimization) · Lookahead-GCG: Improving Universal Multi-Model Optimization-Based Jailbreaking Attacks via Stochastic Nesterov Optimization
- [逐列归一化与末层动量](../papers/llm.md#glentis26a-optimization) · Memory-Efficient LLM Pretraining via Minimalist Optimizer Design
- [微缩放量化的可逆仿射校准](../papers/llm.md#gordon26b-optimization) · LATMiX: Learnable Affine Transformations for Microscaling Quantization of LLMs

### 计算机视觉

- [可微的随机特征点云配准](../papers/computer-vision.md#crane26a-optimization) · Scalable and Differentiable Point-Cloud Registration Using Maximum Mean Discrepancy
- [动态网格的逐面雅可比形变](../papers/computer-vision.md#dai26h-optimization) · TextMesh4D: Zero-shot Text-to-4D Mesh Generation
- [流模型逆问题的分段轨迹拼接](../papers/computer-vision.md#denker26a-optimization) · Trajectory Stitching for Solving Inverse Problems with Flow-Based Models
- [动态高斯属性平均](../papers/computer-vision.md#ding26p-optimization) · Improving Explicit Dynamic Gaussian Splatting Optimization via Update Mixture

### 自然语言处理

- [低资源语音语言识别的凸检测头](../papers/nlp.md#feng26p-optimization) · Convex Low-resource Accent-Robust Language Detection in Speech Recognition

### 强化学习

- [目标稳态分布约束下的快速混合](../papers/reinforcement-learning.md#corso26a-optimization) · Fast Mixing Steady-State Control in Markov Decision Processes
- [二阶平滑 Bellman 规划](../papers/reinforcement-learning.md#dam26a-optimization) · Second-Order Smooth Planning with Optimal-Transport Bellman Smoothing

### 机器人学

- [安全控制器混合](../papers/robotics.md#chaudhary26a-optimization) · Blending Neural Control Density Functions for Stabilization and Safety
- [动态 SLAM 的残差梯度隔离](../papers/robotics.md#fan26g-optimization) · De4D-SLAM: Gradient-Isolated Static-Dynamic Decoupling for Monocular SLAM in Dynamic Environments

### 多模态学习

- [多模态检测的跨阶段融合搜索](../papers/multimodal.md#gao26an-optimization) · MFH-NAS:A Hybrid Neural Architecture Search Framework for Multimodal Fusion Object Detection
- [持续低秩适配的谱均衡约束](../papers/multimodal.md#gu26i-optimization) · Spectral Imbalance Causes Forgetting in Low-Rank Continual Adaptation

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
- [核回归的非均匀傅里叶求解](../papers/ml-foundations.md#doumeche26a-optimization) · Fast kernel methods: Sobolev, physics-informed, and additive models
- [约束多目标搜索的区域先验](../papers/ml-foundations.md#du26r-optimization) · Meta-Black-Box Optimization Can Do Search Guidance for Expensive Constrained Multi-Objective Optimization
- [动态子模优化的分级平滑切换](../papers/ml-foundations.md#duetting26a-optimization) · A General Framework for Dynamic Consistent Submodular Maximization
- [从有限矩拟合混合测度](../papers/ml-foundations.md#durasinovic26a-optimization) · Mixtures Closest To A Given Measure: A Semidefinite Programming Approach
- [熵正则最优传输的变分归一化](../papers/ml-foundations.md#dyachenko26a-optimization) · Variational Entropic Optimal Transport
- [软排列求解的局部熵温度](../papers/ml-foundations.md#eisenberg26a-optimization) · Learning Permutation from Structure Without Supervision
- [边预测引导的度量旅行商求解](../papers/ml-foundations.md#elias26a-optimization) · TSP with Predictions: Heatmap to Tour with Provable Guarantees
- [约束级隐私的正线性规划](../papers/ml-foundations.md#ene26a-optimization) · Solving Positive Linear Programs with Differential Privacy
- [随机自归约的稀疏回归搜索](../papers/ml-foundations.md#erata26a-optimization) · Learning Randomized Reductions
- [异步 SGD 的梯度裁剪](../papers/ml-foundations.md#erickson26a-optimization) · Clipping Makes Distributed and Federated Asynchronous SGD Robust to Stragglers
- [容忍无界异常幅度的贝叶斯优化](../papers/ml-foundations.md#ezzerg26a-optimization) · Robust Bayesian Optimisation with Unbounded Corruptions
- [组合优化的候选提出与在线选择](../papers/ml-foundations.md#fang26t-optimization) · ASAP: Exploiting the Satisficing Generalization Edge in Neural Combinatorial Optimization
- [次模凹鞍点的零阶求解](../papers/ml-foundations.md#farzin26a-optimization) · Solving the Offline and Online Min-Max Problem of Non-smooth Submodular-Concave Functions: A Zeroth-Order Approach
- [量化前的权重激活协方差对齐](../papers/ml-foundations.md#federici26a-optimization) · Dissecting Quantization Error: A Concentration-Alignment Perspective
- [下游 Fisher 子空间初始化 LoRA](../papers/ml-foundations.md#feng26h-optimization) · Learning in the Fisher Subspace: A Guided Initialization for LoRA Fine-Tuning
- [离散扩散求解的单轨迹伴随估计](../papers/ml-foundations.md#feng26o-optimization) · Unsupervised Diffusion Solver for Combinatorial Optimization via Combinatorial Adjoint Matching
- [动量符号更新的平滑过渡](../papers/ml-foundations.md#feoktistov26a-optimization) · Softsign: Smooth Sign in Your Optimizer For Better Parameter Heterogeneity Handling
- [在线凸优化的平方违约控制](../papers/ml-foundations.md#ferreira26a-optimization) · CLASP: Online learning algorithms for Convex Losses And Squared Penalties
- [容量公平聚类的树度量化](../papers/ml-foundations.md#gadekar26a-optimization) · Capacitated Fair-Range Clustering: Hardness and Approximation Algorithms
- [按局部光滑性选梯度下降步长](../papers/ml-foundations.md#galli26a-optimization) · Flatland: The Adventures of Gradient Descent with Large Step Sizes
- [量化数据的潜变量条件极大化](../papers/ml-foundations.md#gao26ah-optimization) · Inference from Quantized Data via Normal Variance-Mean Mixtures
- [极小极大问题的免投影平滑](../papers/ml-foundations.md#giang-tran26a-optimization) · Projection-Free Algorithms for Minimax Problems
- [LogSumExp 的平滑随机近似](../papers/ml-foundations.md#gladin26a-optimization) · Improved Stochastic Optimization of LogSumExp
- [预测编码的误差变量重参数化](../papers/ml-foundations.md#goemaere26a-optimization) · ePC: Fast and Deep Predictive Coding in Digital Simulation
- [同批自然梯度的草图投影分析](../papers/ml-foundations.md#goldshlager26a-optimization) · A Sketch-and-Project Analysis of Subsampled Natural Gradient Algorithms
- [按舍入间隔编码主权重残差](../papers/ml-foundations.md#gonzalez-ortiz26a-optimization) · FlashOptim: Optimizers for Memory-Efficient Training
- [无固定生成顺序的组合搜索](../papers/ml-foundations.md#goudet26a-optimization) · Black-Box Combinatorial Optimization with Order-Invariant Reinforcement Learning
- [分类采样的去噪重参数化](../papers/ml-foundations.md#gourevitch26a-optimization) · Categorical Reparameterization with Denoising Diffusion Models
- [未配对快照的多边际薛定谔桥](../papers/ml-foundations.md#gravier26a-optimization) · Multi-marginal temporal Schrödinger Bridge Matching from unpaired data
- [张量列车求解扩散分数方程](../papers/ml-foundations.md#gruhlke26a-optimization) · Tensor Train Diffusion: Leveraging Low-Rank Structures for High-Dimensional Score-Based Sampling
- [凸约束域上的镜像平均场朗之万动力学](../papers/ml-foundations.md#gu26e-optimization) · Mirror Mean-Field Langevin Dynamics
- [跨域增量学习的掩码与轨迹调节](../papers/ml-foundations.md#gu26n-optimization) · Parameter-Masked Decoupled Optimization for Cross-Domain Class-Incremental Learning

### 图学习与推荐

- [图粗化](../papers/graph-and-recommendation.md#bai26g-optimization) · Rethinking Efficient Graph Coarsening via a Non-Selfishness Principle
- [公平排序聚合](../papers/graph-and-recommendation.md#chakraborty26b-optimization) · Fairness in Aggregation: Optimal Top-$k$ and Improved Full Ranking
- [隐私图查询](../papers/graph-and-recommendation.md#chen26b-optimization) · Differentially Private Range Subgraph Counting
- [关系数据库的任务感知图结构优化](../papers/graph-and-recommendation.md#cheng26j-optimization) · What Makes a Desired Graph for Relational Deep Learning?

### 科学机器学习

- [广义特征值积分轮廓](../papers/scientific-ml.md#chen26ck-optimization) · Learning-Guided Integration Contours Construction for Fast Large-Scale Generalized Eigensolvers
- [语言模型预测与真实实验的门控](../papers/scientific-ml.md#chen26fx-optimization) · LABO: LLM-Accelerated Bayesian Optimization through Broad Exploration and Selective Experimentation
- [扩散重建的对偶反馈与频谱均衡](../papers/scientific-ml.md#du26n-optimization) · Plug-and-Play Diffusion Meets ADMM: Dual-Variable Coupling for Robust Medical Image Reconstruction
- [临床二元规则的等权清单搜索](../papers/scientific-ml.md#estevez26a-optimization) · Automatic Construction of Clinical Scoring Systems with LLM Agents
- [代数多重网格的稀疏粗层修正](../papers/scientific-ml.md#fink26a-optimization) · RAPNet: Accelerating Algebraic Multigrid with Learned Sparse Corrections
- [量子激发态的多态重要性采样](../papers/scientific-ml.md#gao26j-optimization) · Excited Pfaffians: Generalized Neural Wave Functions Across Structure and State
- [大规模神经振荡相位图的随机分数匹配](../papers/scientific-ml.md#goffinet26b-optimization) · Torus Graphs for Large Scale Neural Phase Analysis
<!-- classification:end -->
