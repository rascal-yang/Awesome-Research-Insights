# 优化

[首页](../README.md) · [参与贡献](../CONTRIBUTING.md) · [English](../en/insights/optimization.md)

梯度更新、参数化与优化过程。

<!-- classification:start -->
## 按研究领域浏览

[大语言模型](#by-llm) · [计算机视觉](#by-computer-vision) · [自然语言处理](#by-nlp) · [强化学习](#by-reinforcement-learning) · [机器人学](#by-robotics) · [多模态学习](#by-multimodal) · [机器学习基础与统计](#by-ml-foundations) · [图学习与推荐](#by-graph-and-recommendation) · [科学机器学习](#by-scientific-ml)

<a id="by-llm"></a>

### 大语言模型

- [模型压缩](../conferences/icml-2026/cards/0001-0100.md#abbasi26a-optimization) · Zero Sum SVD: Balancing Loss Sensitivity for Low Rank LLM Compression
- [低显存零阶微调](../conferences/icml-2026/cards/0301-0400.md#cai26a-optimization) · AdaMeZO: Adam-style Zeroth-Order Optimizer for LLM Fine-tuning Without Maintaining the Moments
- [LoRA 收敛](../conferences/icml-2026/cards/0401-0500.md#castin26a-optimization) · Balanced LoRA: Removing Parameter Invariance to Accelerate Convergence
- [权重激活联合量化](../conferences/icml-2026/cards/0401-0500.md#chen26z-optimization) · WUSH: Near-Optimal Adaptive Transforms for LLM Quantization
- [有约束的安全微调](../conferences/icml-2026/cards/0501-0600.md#chen26ba-optimization) · SPARD: Defending Harmful Fine-Tuning Attack via Safety Projection with Relevance–Diversity Data Selection
- [多目标偏好梯度裁剪](../conferences/icml-2026/cards/0501-0600.md#chen26bl-optimization) · Reward-free Alignment for Conflicting Objectives
- [可变网格低比特量化](../conferences/icml-2026/cards/0501-0600.md#chen26bt-optimization) · BPDQ: Bit-Plane Decomposition Quantization on a Variable Grid for Large Language Models
- [宽度扩展后的优化器几何](../conferences/icml-2026/cards/0601-0700.md#chen26eq-optimization) · Escaping the Subspace Trap: The Role of Optimizer Geometry in Model Width Expansion
- [MoE 专家组合剪枝](../conferences/icml-2026/cards/0601-0700.md#chen26ew-optimization) · SCHUR-A*: Layer-wise Optimal Expert Pruning for MoEs via Schur-Complement Guided A* Search
- [偏好更新的梯度激励校准](../conferences/icml-2026/cards/0601-0700.md#chen26fe-optimization) · Towards Disentangled Preference Optimization Dynamics: Suppress the Loser, Preserve the Winner
- [求解器程序树进化](../conferences/icml-2026/cards/0601-0700.md#chen26hb-optimization) · $A_2$DEPT: Large Language Model–Driven Automated Algorithm Design via Evolutionary Program Trees
- [低秩二值权重量化](../conferences/icml-2026/cards/0701-0800.md#chong26a-optimization) · NanoQuant: Efficient Sub-1-Bit Quantization of Large Language Models
- [MoE 通道贡献覆盖剪枝](../conferences/icml-2026/cards/0901-1000.md#ding26q-optimization) · Attribution-Guided and Coverage-Maximized Pruning for Structural MoE Compression
- [张量并行的计算通信联合量化](../conferences/icml-2026/cards/0901-1000.md#duanmu26a-optimization) · CoCoQuant: Breaking the Bandwidth Wall via Co-Optimized Communication and Computation Quantization
- [零阶微调的贪心子空间筛选](../conferences/icml-2026/cards/1001-1100.md#fang26k-optimization) · LOZO+: Provably Efficient Zeroth-Order Fine-Tuning via Greedy Low-Rank Subspace Selection
- [冻结主干的凸偏好对齐](../conferences/icml-2026/cards/1101-1200.md#feng26l-optimization) · Convex Optimization for Alignment and Preference Learning on a Single GPU
- [多模型红队搜索的嵌入动量](../conferences/icml-2026/cards/1101-1200.md#feng26y-optimization) · Lookahead-GCG: Improving Universal Multi-Model Optimization-Based Jailbreaking Attacks via Stochastic Nesterov Optimization
- [逐列归一化与末层动量](../conferences/icml-2026/cards/1201-1300.md#glentis26a-optimization) · Memory-Efficient LLM Pretraining via Minimalist Optimizer Design
- [微缩放量化的可逆仿射校准](../conferences/icml-2026/cards/1301-1400.md#gordon26b-optimization) · LATMiX: Learnable Affine Transformations for Microscaling Quantization of LLMs
- [以自生成上下文任务作为模型合并的搜索代理](../conferences/icml-2026/cards/1401-1500.md#he26a-optimization) · OPIC: Enhancing Language Model Merging via Optimizing In-Context Capability
- [用权重谱分配逐层学习率](../conferences/icml-2026/cards/1501-1600.md#he26ak-optimization) · One LR Doesn’t Fit All: Heavy-Tail Guided Layerwise Learning Rates for LLMs
- [把同步拆成可重叠的混合和按需阻塞校准](../conferences/icml-2026/cards/1501-1600.md#hewa-koneputugodage26a-optimization) · Factored Gossip DiLoCo: Reducing Blocking Communication in DiLoCo
- [从执行轨迹进化代理协作图](../conferences/icml-2026/cards/1601-1700.md#hu26bg-optimization) · EvoMAS: Evolutionary Generation of Multi-Agent Systems
- [按有效秩跨层分配专家保留额](../conferences/icml-2026/cards/1601-1700.md#hu26bj-optimization) · RaGEP: Rank-aware Geometric Expert Pruning for Mixture-of-Experts Language Models
- [跟踪并抑制主导梯度谱方向](../conferences/icml-2026/cards/1601-1700.md#huang26d-optimization) · Spectra: Rethinking Optimizers for LLMs Under Spectral Anisotropy
- [让文本优化反馈按责任节点传递](../conferences/icml-2026/cards/1701-1800.md#huang26aa-optimization) · TextResNet: Decoupling and Routing Optimization Signals in Compound AI Systems via Deep Residual Tuning
- [合并专家后按局部曲率重校准离散路由](../conferences/icml-2026/cards/1701-1800.md#huang26au-optimization) · When Model Merging Breaks Routing: Training-Free Calibration for MoE
- [量化时重视不可逆写入前沿](../conferences/icml-2026/cards/1701-1800.md#huang26br-optimization) · FAIR-Calib: Frontier-Aware Instability-Reweighted Calibration for Post-Training Quantization of Diffusion Large Language Models
- [用确定性门优化结构化剪枝](../conferences/icml-2026/cards/1701-1800.md#huang26cg-optimization) · Deterministic Differentiable Structured Pruning for Large Language Models
- [将知识编辑梯度投影到能力损失的低曲率方向](../conferences/icml-2026/cards/1801-1900.md#ikram26a-optimization) · CrispEdit: Low-Curvature Projections for Scalable Non-Destructive LLM Editing
- [在低秩因子空间限制合成权重的谱更新](../conferences/icml-2026/cards/1801-1900.md#janson26a-optimization) · Stabilizing Native Low-Rank LLM Pretraining
- [把程序搜索历史压缩为可复用的语义差量](../conferences/icml-2026/cards/1901-2000.md#jiang26g-optimization) · DeltaEvolve: Accelerating Scientific Discovery through Momentum-Driven Evolution
- [把偏好异质性与通信混合拆进 DPO 收敛](../conferences/icml-2026/cards/1901-2000.md#jiang26h-optimization) · Distributed Direct Preference Optimization
- [分别对梯度和更新施加软谱裁剪](../conferences/icml-2026/cards/1901-2000.md#jiang26am-optimization) · Enhancing LLM Training via Spectral Clipping
- [用历次合并成败学习下一组权重](../conferences/icml-2026/cards/1901-2000.md#jiang26az-optimization) · EvoGM: Learning to Merge LLMs via Evolutionary Generative Optimization
- [给低频同步的低秩更新保留全秩方向](../conferences/icml-2026/cards/2001-2100.md#jovanovic26a-optimization) · LoRDO: Distributed Low-Rank Optimization with Infrequent Communication
- [将自适应优化坐标旋向 Hessian 主轴](../conferences/icml-2026/cards/2001-2100.md#jung26h-optimization) · Mitigating Staleness in Asynchronous Pipeline Parallelism via Basis Rotation
- [搜索剪枝规则时按层的异常程度分配稀疏度](../conferences/icml-2026/cards/2001-2100.md#kang26l-optimization) · Automatic Pruning Discovery for Large Language Models
- [让模型提议可由外部程序验证的几何引理](../conferences/icml-2026/cards/2001-2100.md#ke26a-optimization) · Towards Solving the Gilbert-Pollak Conjecture via Large Language Models
- [让求解器和生成器在程序空间共同进化](../conferences/icml-2026/cards/2001-2100.md#ke26b-optimization) · Game-Theoretic Co-Evolution for LLM-Based Heuristic Discovery
- [用跨层残差证据挑值得反传的词元](../conferences/icml-2026/cards/2101-2200.md#kim26bc-optimization) · TokenDrop: Token-Level Importance-Aware Backward Propagation Skipping for Efficient LLM Fine-Tuning
- [在残差量化码本中分开学方向和尺度](../conferences/icml-2026/cards/2101-2200.md#kim26bf-optimization) · GSRQ: Gain-Shape Residual Quantization for Sub-1-bit KV Cache
- [用角色数据学习专属 FFN 剪枝掩码](../conferences/icml-2026/cards/2101-2200.md#kim26br-optimization) · Persona-Pruner: Sculpting Lightweight Models for Role-Playing
- [离线融合逐层旋转并只在线补低秩差](../conferences/icml-2026/cards/2101-2200.md#kim26bv-optimization) · ReSpinQuant: Efficient Layer-Wise LLM Quantization via Subspace Residual Rotation Approximation
- [先旋转奇异子空间再二值化低秩因子](../conferences/icml-2026/cards/2301-2400.md#lee26y-optimization) · LittleBit-2: Maximizing the Spectral Energy Gain in Sub-1-Bit LLMs via Latent Geometry Alignment
- [在 Hessian 弱方向内吸收量化离群权重](../conferences/icml-2026/cards/2401-2500.md#li26aj-optimization) · OSAQ: Outlier Self-Absorption for Accurate Low-bit LLM Quantization
- [逐步选择组的低成本全微调](../conferences/icml-2026/cards/2401-2500.md#li26ax-optimization) · Low-cost Full Fine-tuning: Learning What to Update for LLMs
- [外部经验库的选择性改写](../conferences/icml-2026/cards/2401-2500.md#li26bo-optimization) · Textual Stochastic Gradient Descent: Discrete Optimization of External Memory for Reasoning Language Agents
- [在博弈求解器中滚动优化可读的语言信号](../conferences/icml-2026/cards/2401-2500.md#li26cw-optimization) · Verbalized Bayesian Persuasion
- [先正交化矩阵更新，再按神经元二阶矩归一](../conferences/icml-2026/cards/2501-2600.md#li26dh-optimization) · NorMuon: Making Muon more efficient and scalable
- [量化训练在近平坦鞍点的加速](../conferences/icml-2026/cards/2501-2600.md#li26dr-optimization) · WinQ: Accelerating Quantization-Aware Training of Language Models Around Saddle Points
- [压缩激活时保留主方向并无偏估计谱尾部](../conferences/icml-2026/cards/2601-2700.md#li26je-optimization) · PRAC: Principal-Random Subspace for LLM Activation Compression and Memory-Efficient Training
- [在效用零空间内跨语种编辑安全方向](../conferences/icml-2026/cards/2701-2800.md#liang26x-optimization) · Multilingual Safety Alignment Via Sparse Weight Editing
- [激活协方差引导的线性层量化](../conferences/icml-2026/cards/2701-2800.md#lifar26a-optimization) · WaterSIC: Information-Theoretically (Near) Optimal Linear Layer Quantization
- [固定尺度先解析零点再搜索量化初值](../conferences/icml-2026/cards/2701-2800.md#lin26l-optimization) · NeUQI: Near-Optimal Uniform Quantization Parameter Initialization for Low-Bit LLMs
- [按层保存低比特激活并在高精度归约梯度](../conferences/icml-2026/cards/2701-2800.md#lin26m-optimization) · AGoQ: Activation and Gradient Quantization for Memory-Efficient Distributed Training of LLMs
- [将零阶扰动限制在输入激活张成的子空间](../conferences/icml-2026/cards/2701-2800.md#lin26n-optimization) · AGZO: Activation-Guided Zeroth-Order Optimization for LLM Fine-Tuning
- [从首编辑层前向传播兼容的知识编辑目标](../conferences/icml-2026/cards/2801-2900.md#liu26ax-optimization) · From Backward Spreading to Forward Replay: Revisiting Target Construction in LLM Parameter Editing
- [先选功能因子再生成架构搜索补丁](../conferences/icml-2026/cards/2801-2900.md#liu26cm-optimization) · Structured Progressive Knowledge Activation for LLM-Driven Neural Architecture Search
- [窄域微调退化的谱方向诊断](../conferences/icml-2026/cards/2801-2900.md#liu26cs-optimization) · The Geometry of Narrow Fine-Tuning Degradation: Trajectory Lock-in and Spectral Bifurcation
- [分层进化共享元启发式和各任务程序](../conferences/icml-2026/cards/2901-3000.md#liu26ge-optimization) · Hierarchical Representations for Cross-task Automated Heuristic Design using LLMs
- [预训练中联合诱导稀疏与低秩权重](../conferences/icml-2026/cards/3101-3200.md#ma26a-optimization) · SALAAD: Sparse And Low-Rank Adaptation via ADMM for Large Language Model Inference
- [用持续梯度白化保护顺序编辑中的旧知识](../conferences/icml-2026/cards/3101-3200.md#ma26f-optimization) · More Edits, More Stable: Understanding the Lifelong Normalization in Sequential Model Editing
- [在分布邻域内稳健优化偏好](../conferences/icml-2026/cards/3201-3300.md#mandal26a-optimization) · Distributionally Robust Reinforcement Learning from Human Feedback
- [多目标微调调度](../conferences/icml-2026/cards/3301-3400.md#monteiro26a-optimization) · Landmark-Guided Policy Optimization for Multi-Objective Language Model Selection
- [在可验证奖励强化学习中用无状态 SGD 替换 AdamW](../conferences/icml-2026/cards/3301-3400.md#mukherjee26c-optimization) · Do We Need Adam? Surprisingly Strong and Sparse Reinforcement Learning with SGD in LLMs
- [把量化舍入误差累积到动量以省掉 master weights](../conferences/icml-2026/cards/3401-3500.md#nikdan26a-optimization) · ECO: Quantized Training without Full-Precision Master Weights
- [编译遍历证据引导](../conferences/icml-2026/cards/3501-3600.md#pan26f-optimization) · ECCO: Evidence-Driven Causal Reasoning for Compiler Optimization
- [把无偏修正融入四位量化的微尺度](../conferences/icml-2026/cards/3501-3600.md#panferov26a-optimization) · Quartet II: Accurate LLM Pre-Training in NVFP4 by Improved Unbiased Gradient Estimation
- [用可重放参数扰动扩展全参进化微调](../conferences/icml-2026/cards/3701-3800.md#qiu26f-optimization) · Evolution Strategies at Scale: LLM Fine-Tuning Beyond Reinforcement Learning
- [用分块置换结构减少正交等价训练的内存](../conferences/icml-2026/cards/3701-3800.md#qiu26o-optimization) · POET-X: Memory-efficient LLM Training by Scaling Orthogonal Transformation
- [相似性筛选的多模型离散搜索](../conferences/icml-2026/cards/3801-3900.md#ran26a-optimization) · MCCE: A Framework for Multi-LLM Collaborative Search in Discrete Spaces with Similarity-Filtered Preference Learning
- [硬件计数器约束的 GPU 算子搜索](../conferences/icml-2026/cards/3801-3900.md#ran26b-optimization) · KernelBand: Steering LLM-based Kernel Optimization via Hardware-Aware Multi-Armed Bandits
- [用优先队列和近邻摘要迭代改写有噪声的候选系统](../conferences/icml-2026/cards/3801-3900.md#ren26l-optimization) · POLCA: Stochastic Generative Optimization with LLM
- [用逐层广义光滑性分析线性最小化优化器](../conferences/icml-2026/cards/3801-3900.md#riabinin26a-optimization) · From Muon to Gluon: Bridging Theory and Practice of LMO-based Optimizers for LLMs
- [用语言知识构造 LoRA 贝叶斯搜索空间](../conferences/icml-2026/cards/4001-4100.md#seong-eun26a-optimization) · A Language-Guided Bayesian Optimization for Efficient LoRA Hyperparameter Search
- [inner-optimizer-worker-scaling](../conferences/icml-2026/cards/4401-4500.md#therien26a-optimization) · MuLoCo: Muon is a Practical Inner Optimizer for DiLoCo
- [calibrated-svd-rank-allocation](../conferences/icml-2026/cards/4401-4500.md#thoma26a-optimization) · Advancing SVD-based LLM Compression via Layer-Wise Error Model Search
- [跨客户端闲置专家伪梯度](../conferences/icml-2026/cards/4401-4500.md#tran26f-optimization) · UB-SMoE: Universally Balanced Sparse Mixture-of-Experts for Resource-adaptive Federated Fine-tuning of Foundation Models
- [end-to-end-rounding-curvature](../conferences/icml-2026/cards/4401-4500.md#tseng26b-optimization) · Model-Preserving Adaptive Rounding
- [analytic-plus-learned-binary-scaling](../conferences/icml-2026/cards/4501-4600.md#tu26b-optimization) · Rethinking 1-bit Optimization Leveraging Pre-trained Large Language Models
- [time-shared-ssm-pruning](../conferences/icml-2026/cards/4501-4600.md#tuo26a-optimization) · SparseSSM: Efficient Selective Structured State Space Models Can Be Pruned in One-Shot
- [QK与OV相对学习速度控制注意力](../conferences/icml-2026/cards/4501-4600.md#vashisht26a-optimization) · Faster Query-Key Learning Sharpens Attention in Self-Attention Models
- [CurvZO: Adaptive Curvature-Guided Sparse Zeroth-Order Optimization for Efficient LLM Fine-Tuning](../conferences/icml-2026/cards/4601-4700.md#wang26z-optimization) · CurvZO: Adaptive Curvature-Guided Sparse Zeroth-Order Optimization for Efficient LLM Fine-Tuning

<a id="by-computer-vision"></a>

### 计算机视觉

- [可微的随机特征点云配准](../conferences/icml-2026/cards/0701-0800.md#crane26a-optimization) · Scalable and Differentiable Point-Cloud Registration Using Maximum Mean Discrepancy
- [动态网格的逐面雅可比形变](../conferences/icml-2026/cards/0801-0900.md#dai26h-optimization) · TextMesh4D: Zero-shot Text-to-4D Mesh Generation
- [流模型逆问题的分段轨迹拼接](../conferences/icml-2026/cards/0801-0900.md#denker26a-optimization) · Trajectory Stitching for Solving Inverse Problems with Flow-Based Models
- [动态高斯属性平均](../conferences/icml-2026/cards/0901-1000.md#ding26p-optimization) · Improving Explicit Dynamic Gaussian Splatting Optimization via Update Mixture
- [按域损失缩放并探测多方向尖锐度](../conferences/icml-2026/cards/1501-1600.md#he26m-optimization) · Navigating the Flatlands: Dual Adaptive Sharpness-Aware Minimization for Domain Generalization
- [双教师置信度融合的曲率预条件](../conferences/icml-2026/cards/1501-1600.md#he26ad-optimization) · Newton-coupled Dual-Teacher Semi-supervised Learning Framework
- [先在渲染平面约束扰动，再把结果拟合回三维](../conferences/icml-2026/cards/1501-1600.md#hong26c-optimization) · AdLift: Lifting Adversarial Perturbations to Safeguard 3D Gaussian Splatting Assets Against Instruction-Driven Editing
- [对角曲率配合高斯参数信赖域](../conferences/icml-2026/cards/1601-1700.md#hsiao26a-optimization) · 3DGS$^2$-TR: Scalable Second-Order Trust-Region Method for 3D Gaussian Splatting
- [把奖励梯度投影成保持噪声统计的方向](../conferences/icml-2026/cards/1701-1800.md#hwang26h-optimization) · Gradient Preconditioning for Efficient and Reliable Reward-Guided Generation
- [在共享参数的单流生成器解耦擦除更新](../conferences/icml-2026/cards/1901-2000.md#jiang26i-optimization) · Z-Erase: Enabling Concept Erasure in Single Stream Diffusion Transformers
- [按时空梯度变化调整发放阈值附近的替代梯度](../conferences/icml-2026/cards/2001-2100.md#kang26g-optimization) · A$^2$SG: Adaptive and Asymmetric Surrogate Gradients for Training Deep Spiking Neural Networks
- [用场景交互点约束单目群体重建尺度](../conferences/icml-2026/cards/2001-2100.md#kang26s-optimization) · Crowd4D: Scene-Aware Monocular 4D Crowd Reconstruction
- [用显式遗忘约束校准保留程度](../conferences/icml-2026/cards/2001-2100.md#khalafi26a-optimization) · Unlearning in Diffusion Models: A Unified Framework with KL Divergence and Likelihood Constraints
- [沿优化后的连续路径重组对抗扰动](../conferences/icml-2026/cards/2101-2200.md#kim26ax-optimization) · MoCo-EA: Exploiting Adversarial Mode Connectivity for Efficient Evolutionary Attacks
- [按解释 IoU 上下界剪枝求全局最优规则](../conferences/icml-2026/cards/2201-2300.md#la-rosa26a-optimization) · Guaranteed Optimal Compositional Explanations for Neurons
- [按历史曲率对增量任务的更新作软抑制](../conferences/icml-2026/cards/2201-2300.md#lai26d-optimization) · MoCL: Metabolic Optimization for Curvature-Aware Continual Learning
- [放松传输边际并用观测似然约束反演](../conferences/icml-2026/cards/2301-2400.md#lee26ak-optimization) · UOTIP: Unbalanced Optimal Transport Map for Unpaired Inverse Problems
- [按感受野位置调节三维大卷积核的梯度](../conferences/icml-2026/cards/2301-2400.md#lee26as-optimization) · Spatially-Adaptive Gradient Re-parameterization for 3D Large Kernel Optimization
- [按视觉生成轨迹初始化稀疏专家](../conferences/icml-2026/cards/2501-2600.md#li26gy-optimization) · Prism-MoE: Efficient Dense-to-MoE Conversion for Visual Autoregressive Generation
- [沿损失障碍修正的参数路径选择合并点](../conferences/icml-2026/cards/2701-2800.md#lin26o-optimization) · Unlocking the Potential of Continual Model Merging: An ODE Perspective
- [在任务向量合并前降低目标子群敏感性](../conferences/icml-2026/cards/2801-2900.md#liu26dl-optimization) · FairMerging: Rethinking Model Merging through the Lens of Fairness
- [用权重条件数降低低比特激活误差](../conferences/icml-2026/cards/2901-3000.md#liu26eh-optimization) · Condition Number Based Low-Bit Quantization for Image Super-Resolution
- [沿预测敏感方向补偿量化误差](../conferences/icml-2026/cards/3101-3200.md#lv26j-optimization) · SHARP-Q: Spectral Hessian Alignment and Rectification for Post-training Quantization
- [残差网格反解 CAD](../conferences/icml-2026/cards/3401-3500.md#nehme26a-optimization) · CADFit: Precise Mesh-to-CAD Program Generation with Hybrid Optimization
- [用置信和梯度共同限学习率](../conferences/icml-2026/cards/4001-4100.md#shaoran26a-optimization) · CONGA:Confidence-and-Gradient-Aware Learning Rate Schedule for Test Time Adaptation
- [部分几何能量场与梯度隔离](../conferences/icml-2026/cards/4201-4300.md#song26b-optimization) · EnerGS: Energy-Based Gaussian Splatting with Partial Geometric Priors
- [正交旋转的概念编辑](../conferences/icml-2026/cards/4301-4400.md#sun26ax-optimization) · Orthogonal Concept Erasure for Diffusion Models
- [先解阈值再尾风险微调](../conferences/icml-2026/cards/4601-4700.md#wang26al-optimization) · Efficient Tail-Aware Generative Optimization via Flow Model Fine-Tuning

<a id="by-nlp"></a>

### 自然语言处理

- [低资源语音语言识别的凸检测头](../conferences/icml-2026/cards/1101-1200.md#feng26p-optimization) · Convex Low-resource Accent-Robust Language Detection in Speech Recognition

<a id="by-reinforcement-learning"></a>

### 强化学习

- [目标稳态分布约束下的快速混合](../conferences/icml-2026/cards/0701-0800.md#corso26a-optimization) · Fast Mixing Steady-State Control in Markov Decision Processes
- [二阶平滑 Bellman 规划](../conferences/icml-2026/cards/0801-0900.md#dam26a-optimization) · Second-Order Smooth Planning with Optimal-Transport Bellman Smoothing
- [用决策时点锚定的伴随量优化非指数折扣](../conferences/icml-2026/cards/2101-2200.md#ko26a-optimization) · Beyond the Bellman Recursion: A Pontryagin-Guided Framework for Non-Exponential Discounting
- [离线价值学习的解耦正交校正](../conferences/icml-2026/cards/3701-3800.md#qiao26j-optimization) · AdamO: A Collapse-Suppressed Optimizer for Offline RL
- [按预期输出变化反算单步步长](../conferences/icml-2026/cards/4001-4100.md#sharifnassab26a-optimization) · Intentional Updates for Streaming Reinforcement Learning
- [有限步优势预条件求解](../conferences/icml-2026/cards/4301-4400.md#sun26ak-optimization) · Randomized Advantage Transformation (RAT): Computing Natural Policy Gradients via Direct Backpropagation

<a id="by-robotics"></a>

### 机器人学

- [安全控制器混合](../conferences/icml-2026/cards/0401-0500.md#chaudhary26a-optimization) · Blending Neural Control Density Functions for Stabilization and Safety
- [动态 SLAM 的残差梯度隔离](../conferences/icml-2026/cards/1001-1100.md#fan26g-optimization) · De4D-SLAM: Gradient-Isolated Static-Dynamic Decoupling for Monocular SLAM in Dynamic Environments
- [由熵正则分数运输引导整数路径](../conferences/icml-2026/cards/2001-2100.md#khan26a-optimization) · Optimal and Scalable MAPF via Multi-Marginal Optimal Transport and Schrödinger Bridges
- [把长程规划中间状态设为并行变量](../conferences/icml-2026/cards/3601-3700.md#psenka26a-optimization) · Parallel Stochastic Gradient-Based Planning for World Models
- [用模拟器裁决形态与奖励的多智能体辩论](../conferences/icml-2026/cards/3701-3800.md#qiu26c-optimization) · Debate2Create: Robot Co-design via Multi-Agent LLM Debate
- [分支依赖平衡序列代理伴随](../conferences/icml-2026/cards/4401-4500.md#tong26j-optimization) · Neural Control: Adjoint Learning Through Equilibrium Constraints

<a id="by-multimodal"></a>

### 多模态学习

- [多模态检测的跨阶段融合搜索](../conferences/icml-2026/cards/1201-1300.md#gao26an-optimization) · MFH-NAS:A Hybrid Neural Architecture Search Framework for Multimodal Fusion Object Detection
- [持续低秩适配的谱均衡约束](../conferences/icml-2026/cards/1301-1400.md#gu26i-optimization) · Spectral Imbalance Causes Forgetting in Low-Rank Continual Adaptation
- [在奇异子空间选择注入哪些推理能力](../conferences/icml-2026/cards/1701-1800.md#huang26bu-optimization) · FRISM: Fine-Grained Reasoning Injection via Subspace-Level Model Merging for Vision–Language Models
- [按模态维护编辑约束并在固定低秩空间递推](../conferences/icml-2026/cards/2601-2700.md#li26ji-optimization) · Modality-Decoupled Online Recursive Editing
- [用完整增量对齐联邦低秩适配器聚合](../conferences/icml-2026/cards/2701-2800.md#liang26ab-optimization) · UniFLoW: Universal Multi-Modal Federated LoRA Fine-Tuning Framework with Analytical Aggregation
- [视觉语言模型的跨模态攻击迁移](../conferences/icml-2026/cards/3701-3800.md#qin26a-optimization) · MADA-Attack: Transferable Multi-modal Attention Distraction Adversarial Attack against Vision Language Models

<a id="by-ml-foundations"></a>

### 机器学习基础与统计

- [极小极大优化](../conferences/icml-2026/cards/0001-0100.md#abe26a-optimization) · Asymmetric Perturbation in Solving Bilinear Saddle-Point Optimization
- [黑盒优化](../conferences/icml-2026/cards/0001-0100.md#ackermann26b-optimization) · Bridging Spherical Black-Box Optimizers
- [动态稀疏训练](../conferences/icml-2026/cards/0001-0100.md#adnan26a-optimization) · SparseOpt: Addressing Normalization-induced Gradient Skew in Sparse Training
- [一次性剪枝](../conferences/icml-2026/cards/0001-0100.md#afriat26a-optimization) · A Robust Optimization Guided Pruning Framework for Vision and Large Language Models
- [分布式主成分分析](../conferences/icml-2026/cards/0001-0100.md#aguie26a-optimization) · Improved Analysis of the Accelerated Noisy Power Method with Applications to Decentralized PCA
- [学习率预热](../conferences/icml-2026/cards/0001-0100.md#alimisis26a-optimization) · Why Do We Need Warm-up? A Theoretical Perspective
- [时变随机优化](../conferences/icml-2026/cards/0001-0100.md#amidzadeh26a-optimization) · Non-Parametric Optimization for Scalable Learning in Stochastic Decision Problems
- [可微粒子滤波](../conferences/icml-2026/cards/0001-0100.md#andersson26b-optimization) · Diffusion Differentiable Resampling
- [随机优化稳定性](../conferences/icml-2026/cards/0001-0100.md#andreyev26a-optimization) · Momentum Further Constrains Sharpness at the Edge of Stochastic Stability
- [随机梯度收敛](../conferences/icml-2026/cards/0101-0200.md#apidopoulos26a-optimization) · Taming Stochastic Gradient Descent: Almost Sure Convergence and Saddle-Point Avoidance under $(L_0,L_1)$-Smoothness
- [去中心化优化](../conferences/icml-2026/cards/0101-0200.md#armacki26a-optimization) · High-Probability Convergence Guarantees of Decentralized SGD
- [曲率估计](../conferences/icml-2026/cards/0101-0200.md#artemev26a-optimization) · Exploiting weight-space symmetries for approximating curvature
- [学习率调参](../conferences/icml-2026/cards/0101-0200.md#attia26a-optimization) · Learning Rate Annealing Improves Tuning Robustness in Stochastic Optimization
- [样本间梯度冲突](../conferences/icml-2026/cards/0101-0200.md#avranas26a-optimization) · Reducing Per-Sample Interference in Stochastic Optimization
- [贝叶斯优化](../conferences/icml-2026/cards/0101-0200.md#bafna26a-optimization) · Taking the GP Out of the Loop
- [Adam 收敛](../conferences/icml-2026/cards/0101-0200.md#bai26m-optimization) · Towards Understanding Adam Convergence on Highly Degenerate Polynomials
- [优化稳定性](../conferences/icml-2026/cards/0101-0200.md#bai26o-optimization) · Adaptive Preconditioners Trigger Loss Spikes in Adam
- [高维多模态采样](../conferences/icml-2026/cards/0101-0200.md#baldassari26a-optimization) · Dimension-Free Multimodal Sampling via Preconditioned Annealed Langevin Dynamics
- [组合优化松弛](../conferences/icml-2026/cards/0201-0300.md#banerjee26a-optimization) · Local-Minima-Preserving Polynomial Relaxation of Ising Problems
- [动态次模优化](../conferences/icml-2026/cards/0201-0300.md#banihashem26c-optimization) · Improved Dynamic Algorithm for Non-monotone Submodular Maximization under Cardinality Constraint
- [个性化联邦学习](../conferences/icml-2026/cards/0201-0300.md#bhatia26a-optimization) · CLoVE: Personalized Federated Learning through Clustering of Loss Vector Embeddings
- [联邦动态稀疏训练](../conferences/icml-2026/cards/0201-0300.md#bi26b-optimization) · FedFit: Federated Dynamic Sparse Training via Fisher Information scoring
- [可逆扩散求解](../conferences/icml-2026/cards/0201-0300.md#blasingame26a-optimization) · Rex: A Family of Reversible Exponential (Stochastic) Runge-Kutta Solvers
- [混合整数规划加速](../conferences/icml-2026/cards/0201-0300.md#blin26a-optimization) · Batched First-Order Methods for Parallel LP Solving in MIP
- [变分推断](../conferences/icml-2026/cards/0301-0400.md#borghi26a-optimization) · Variational inference via Gaussian interacting particles in the Bures-Wasserstein geometry
- [贝叶斯自适应实验](../conferences/icml-2026/cards/0301-0400.md#bracher26a-optimization) · JADAI: Jointly Amortizing Adaptive Design and Bayesian Inference
- [谱梯度优化](../conferences/icml-2026/cards/0301-0400.md#braun26a-optimization) · Spectral Gradient Descent Mitigates Anisotropy-Driven Misalignment: A Case Study in Phase Retrieval
- [Langevin 优化](../conferences/icml-2026/cards/0301-0400.md#bruno26a-optimization) · Flatness-Aware Stochastic Gradient Langevin Dynamics
- [谱稀疏信号重建](../conferences/icml-2026/cards/0301-0400.md#cai26j-optimization) · Fast Spectrally Sparse Signal Reconstruction via Jacobi-Preconditioned Gradient Descent
- [多核学习](../conferences/icml-2026/cards/0401-0500.md#cao26ae-optimization) · Diversity-Aware Recursive Feature Multiple Kernel Learning
- [重尾随机镜像下降](../conferences/icml-2026/cards/0401-0500.md#cauvin26a-optimization) · Bregman meets Lévy: Stochastic Mirror Descent with Heavy-Tailed Noise in Continuous and Discrete Time
- [Gauss–Newton 训练](../conferences/icml-2026/cards/0401-0500.md#cayci26a-optimization) · Geometric Convergence of Gauss–Newton for Neural Networks: Riemannian Geometry and Adaptive Damping
- [在线变分估计](../conferences/icml-2026/cards/0401-0500.md#chagneux26a-optimization) · Efficient Online Variational Estimation via Monte Carlo Sampling
- [随机约束优化](../conferences/icml-2026/cards/0401-0500.md#chakraborty26c-optimization) · Randomized Feasibility Methods for Constrained Optimization with Adaptive Step Sizes
- [多仿射等式约束](../conferences/icml-2026/cards/0401-0500.md#chao26a-optimization) · Last-iterate Convergence of ADMM on Multi-affine Quadratic Equality Constrained Problem
- [种群超参优化](../conferences/icml-2026/cards/0401-0500.md#chebykin26a-optimization) · Iterated Population Based Training with Task-Agnostic Restarts
- [低秩压缩的 Fisher 近似](../conferences/icml-2026/cards/0401-0500.md#chekalina26a-optimization) · Scalable Kronecker-Factored Fisher Approximation for Neural Network Parameter Sensitivity
- [污染下的分布鲁棒优化](../conferences/icml-2026/cards/0401-0500.md#chen26e-optimization) · Bulk-Calibrated Credal Ambiguity Sets: Fast, Tractable Decision Making under Out-of-Sample Contamination
- [混合整数规划分支](../conferences/icml-2026/cards/0501-0600.md#chen26ah-optimization) · Data-driven Mixed Integer Optimization through Probabilistic Multi-variable Branching
- [Adam 状态压缩](../conferences/icml-2026/cards/0501-0600.md#chen26ax-optimization) · IO-Adam: Rethinking Memory-Efficient Adaptive Optimizers from Gradient Computation
- [核稀疏化的朗之万更新](../conferences/icml-2026/cards/0501-0600.md#chen26bd-optimization) · Thinned Mean Field Langevin Dynamics
- [多步 SAM 邻域搜索](../conferences/icml-2026/cards/0501-0600.md#chen26bo-optimization) · Understanding SAM through Minimax Perspective
- [受遗忘进度约束的模型更新](../conferences/icml-2026/cards/0501-0600.md#chen26de-optimization) · How Hard Can It Be? Hardness-Aware Multi-Objective Unlearning
- [LoRA 学习率的秩缩放](../conferences/icml-2026/cards/0601-0700.md#chen26ei-optimization) · Learning Rate Scaling across LoRA Ranks and Transfer to Full Finetuning
- [分割联邦学习的混阶更新](../conferences/icml-2026/cards/0601-0700.md#chen26fd-optimization) · HO-SFL: Hybrid-Order Split Federated Learning with Backprop-Free Clients and Dimension-Free Aggregation
- [持续学习的 LoRA 梯度修正](../conferences/icml-2026/cards/0601-0700.md#chen26fz-optimization) · JANUS-LORA: A Balanced Low-Rank Adaptation for Continual Learning
- [集合元素污染的鲁棒优化](../conferences/icml-2026/cards/0601-0700.md#chen26gg-optimization) · Distributionally Robust Set Representation Learning Under Inference-Time Element Corruption
- [结构鲁棒的 Gromov–Wasserstein 对齐](../conferences/icml-2026/cards/0601-0700.md#cheng26f-optimization) · Achieving Structurally Robust Gromov Wasserstein Distance via Adaptive Dual-Mask
- [按梯度噪声调节更新方差](../conferences/icml-2026/cards/0701-0800.md#choi26j-optimization) · Parameter Decorrelation via Transition-Variance Alignment for Multivariate Time-series Forecasting
- [一致可接受的随机方案查询](../conferences/icml-2026/cards/0701-0800.md#choo26b-optimization) · Learning Unanimously Acceptable Lotteries via Queries
- [距离算子的凸最优传输](../conferences/icml-2026/cards/0701-0800.md#chung26d-optimization) · Convex Distance Operator Transport: A Convex and Geometry-Preserving Formulation
- [混合整数求解的共形提前停止](../conferences/icml-2026/cards/0701-0800.md#clarke26a-optimization) · Conformal Prediction for Early Stopping in Mixed Integer Optimization
- [在线最小化的对偶预测](../conferences/icml-2026/cards/0701-0800.md#coester26a-optimization) · Learning-Augmented Online Minimization with Dual Predictions
- [带移动成本的图结构连续优化](../conferences/icml-2026/cards/0701-0800.md#cortes26a-optimization) · Beyond Binary: Continuous State Optimization with Graph-Structured Objectives
- [Muon 的跨层范数步长](../conferences/icml-2026/cards/0701-0800.md#crawshaw26a-optimization) · An Exploration of Non-Euclidean Gradient Descent: Muon and its Many Variants
- [预算可行的次模采购拍卖](../conferences/icml-2026/cards/0701-0800.md#cui26b-optimization) · Budget-Feasible Mechanisms for Submodular Welfare Maximization in Procurement Auctions
- [跨优化迭代复用蒙特卡洛粒子](../conferences/icml-2026/cards/0801-0900.md#cuin26a-optimization) · Efficient Stochastic Optimisation via Sequential Monte Carlo
- [SVRG 的变分后验校正](../conferences/icml-2026/cards/0801-0900.md#daheim26a-optimization) · SVRG and Beyond via Posterior Correction
- [强污染下的单指标模型恢复](../conferences/icml-2026/cards/0801-0900.md#das26a-optimization) · Convex Basins in Single-Index Model Loss Landscapes: Applications to Robust Recovery under Strong Adversarial Corruption
- [不确定最优传输的 Sinkhorn 变分推断](../conferences/icml-2026/cards/0801-0900.md#de26a-optimization) · Variational Inference for Uncertain Optimal Transport via Sinkhorn Parametrization
- [持续学习的平衡态控制更新](../conferences/icml-2026/cards/0801-0900.md#de-haan26a-optimization) · Continual Learning through Control Minimization
- [生成流的奖励引导合并](../conferences/icml-2026/cards/0801-0900.md#de-santi26a-optimization) · A Unified Density Operator View of Flow Control and Merging
- [矩阵动量的逐行归一化预条件](../conferences/icml-2026/cards/0801-0900.md#deng26q-optimization) · RMNP: Row-Momentum Normalized Preconditioning for Scalable Matrix-Based Optimization
- [无导数近端算子的分裂迭代](../conferences/icml-2026/cards/0801-0900.md#di26a-optimization) · Operator Splitting with Hamilton-Jacobi-based Proximals
- [多任务分解的两阶段梯度校正](../conferences/icml-2026/cards/0901-1000.md#ding26b-optimization) · Near-Optimal and Efficient First-Order Algorithm for Multi-Task Learning with Shared Linear Representation
- [数据清洗与 AutoML 的分时调度](../conferences/icml-2026/cards/0901-1000.md#ding26l-optimization) · DMCO: Budget-Aware Co-Optimization of Data Cleaning and AutoML
- [约束优化的扩散自举精炼](../conferences/icml-2026/cards/0901-1000.md#ding26aa-optimization) · Diffusion-based learning framework for Constrained Nonconvex Optimization with Weighted Bootstrapped Refinement
- [差分隐私梯度的滤波二阶矩校准](../conferences/icml-2026/cards/0901-1000.md#dm26a-optimization) · FIBER: A Differentially Private Optimizer with Filter-Aware Innovation Bias Correction
- [同方向 Romberg 零阶梯度估计](../conferences/icml-2026/cards/0901-1000.md#dong26j-optimization) · Romberg-Extrapolated Zeroth-Order Gradient Estimator: Higher-Order Bias Reduction with Preserved Leading Directional Variance
- [表格上下文预测的稀疏反事实改动](../conferences/icml-2026/cards/0901-1000.md#dong26n-optimization) · Algorithmic Recourse of In-Context Learning for Tabular Data
- [核回归的非均匀傅里叶求解](../conferences/icml-2026/cards/0901-1000.md#doumeche26a-optimization) · Fast kernel methods: Sobolev, physics-informed, and additive models
- [约束多目标搜索的区域先验](../conferences/icml-2026/cards/0901-1000.md#du26r-optimization) · Meta-Black-Box Optimization Can Do Search Guidance for Expensive Constrained Multi-Objective Optimization
- [动态子模优化的分级平滑切换](../conferences/icml-2026/cards/0901-1000.md#duetting26a-optimization) · A General Framework for Dynamic Consistent Submodular Maximization
- [从有限矩拟合混合测度](../conferences/icml-2026/cards/0901-1000.md#durasinovic26a-optimization) · Mixtures Closest To A Given Measure: A Semidefinite Programming Approach
- [熵正则最优传输的变分归一化](../conferences/icml-2026/cards/1001-1100.md#dyachenko26a-optimization) · Variational Entropic Optimal Transport
- [软排列求解的局部熵温度](../conferences/icml-2026/cards/1001-1100.md#eisenberg26a-optimization) · Learning Permutation from Structure Without Supervision
- [边预测引导的度量旅行商求解](../conferences/icml-2026/cards/1001-1100.md#elias26a-optimization) · TSP with Predictions: Heatmap to Tour with Provable Guarantees
- [随机自归约的稀疏回归搜索](../conferences/icml-2026/cards/1001-1100.md#erata26a-optimization) · Learning Randomized Reductions
- [异步 SGD 的梯度裁剪](../conferences/icml-2026/cards/1001-1100.md#erickson26a-optimization) · Clipping Makes Distributed and Federated Asynchronous SGD Robust to Stragglers
- [容忍无界异常幅度的贝叶斯优化](../conferences/icml-2026/cards/1001-1100.md#ezzerg26a-optimization) · Robust Bayesian Optimisation with Unbounded Corruptions
- [组合优化的候选提出与在线选择](../conferences/icml-2026/cards/1001-1100.md#fang26t-optimization) · ASAP: Exploiting the Satisficing Generalization Edge in Neural Combinatorial Optimization
- [次模凹鞍点的零阶求解](../conferences/icml-2026/cards/1001-1100.md#farzin26a-optimization) · Solving the Offline and Online Min-Max Problem of Non-smooth Submodular-Concave Functions: A Zeroth-Order Approach
- [量化前的权重激活协方差对齐](../conferences/icml-2026/cards/1001-1100.md#federici26a-optimization) · Dissecting Quantization Error: A Concentration-Alignment Perspective
- [下游 Fisher 子空间初始化 LoRA](../conferences/icml-2026/cards/1101-1200.md#feng26h-optimization) · Learning in the Fisher Subspace: A Guided Initialization for LoRA Fine-Tuning
- [离散扩散求解的单轨迹伴随估计](../conferences/icml-2026/cards/1101-1200.md#feng26o-optimization) · Unsupervised Diffusion Solver for Combinatorial Optimization via Combinatorial Adjoint Matching
- [动量符号更新的平滑过渡](../conferences/icml-2026/cards/1101-1200.md#feoktistov26a-optimization) · Softsign: Smooth Sign in Your Optimizer For Better Parameter Heterogeneity Handling
- [按局部光滑性选梯度下降步长](../conferences/icml-2026/cards/1101-1200.md#galli26a-optimization) · Flatland: The Adventures of Gradient Descent with Large Step Sizes
- [极小极大问题的免投影平滑](../conferences/icml-2026/cards/1201-1300.md#giang-tran26a-optimization) · Projection-Free Algorithms for Minimax Problems
- [LogSumExp 的平滑随机近似](../conferences/icml-2026/cards/1201-1300.md#gladin26a-optimization) · Improved Stochastic Optimization of LogSumExp
- [预测编码的误差变量重参数化](../conferences/icml-2026/cards/1201-1300.md#goemaere26a-optimization) · ePC: Fast and Deep Predictive Coding in Digital Simulation
- [同批自然梯度的草图投影分析](../conferences/icml-2026/cards/1201-1300.md#goldshlager26a-optimization) · A Sketch-and-Project Analysis of Subsampled Natural Gradient Algorithms
- [按舍入间隔编码主权重残差](../conferences/icml-2026/cards/1301-1400.md#gonzalez-ortiz26a-optimization) · FlashOptim: Optimizers for Memory-Efficient Training
- [无固定生成顺序的组合搜索](../conferences/icml-2026/cards/1301-1400.md#goudet26a-optimization) · Black-Box Combinatorial Optimization with Order-Invariant Reinforcement Learning
- [分类采样的去噪重参数化](../conferences/icml-2026/cards/1301-1400.md#gourevitch26a-optimization) · Categorical Reparameterization with Denoising Diffusion Models
- [未配对快照的多边际薛定谔桥](../conferences/icml-2026/cards/1301-1400.md#gravier26a-optimization) · Multi-marginal temporal Schrödinger Bridge Matching from unpaired data
- [张量列车求解扩散分数方程](../conferences/icml-2026/cards/1301-1400.md#gruhlke26a-optimization) · Tensor Train Diffusion: Leveraging Low-Rank Structures for High-Dimensional Score-Based Sampling
- [凸约束域上的镜像平均场朗之万动力学](../conferences/icml-2026/cards/1301-1400.md#gu26e-optimization) · Mirror Mean-Field Langevin Dynamics
- [跨域增量学习的掩码与轨迹调节](../conferences/icml-2026/cards/1301-1400.md#gu26n-optimization) · Parameter-Masked Decoupled Optimization for Cross-Domain Class-Incremental Learning
- [动态约束下的贝叶斯实验规划](../conferences/icml-2026/cards/1301-1400.md#guo26g-optimization) · Constrained Bayesian Experimental Design via Online Planning
- [离散 Schrödinger 桥的伴随匹配](../conferences/icml-2026/cards/1401-1500.md#guo26al-optimization) · Discrete Adjoint Schrödinger Bridge Sampler
- [群体公平的最大最小相对改善](../conferences/icml-2026/cards/1401-1500.md#han26a-optimization) · Maximin Relative Improvement: Fair Learning as a Bargaining Problem
- [用去噪投影表达潜空间流形](../conferences/icml-2026/cards/1401-1500.md#hartwig26a-optimization) · Geodesic Calculus on Implicitly Defined Latent Manifolds
- [把异质网络的节点放置分成环排序和跨步调整](../conferences/icml-2026/cards/1401-1500.md#hata26a-optimization) · Bottleneck Communication Delay Minimization for Communication-Efficient Decentralized Learning
- [用小批量最优传输为离散流选择低跳数配对](../conferences/icml-2026/cards/1401-1500.md#haxholli26a-optimization) · Minibatch Optimal Transport and Perplexity Bound Estimation in Discrete Flow Matching
- [在共享低秩坐标内直接合并多个 LoRA](../conferences/icml-2026/cards/1501-1600.md#he26h-optimization) · Compress then Merge: From Multiple LoRAs into One Low-Rank Adapter
- [以代理补全搜索近优树集合](../conferences/icml-2026/cards/1501-1600.md#heile26a-optimization) · From Rashomon Theory to PRAXIS: Efficient Decision Tree Rashomon Sets
- [把披露集合引发的用户响应写进分类损失](../conferences/icml-2026/cards/1501-1600.md#hikri26a-optimization) · Ambiguous Strategic Classification
- [由张量收缩和损失分解生成非负更新](../conferences/icml-2026/cards/1501-1600.md#hood26a-optimization) · Near-Universal Multiplicative Updates for Nonnegative Einsum Factorization
- [在提升特征空间迭代匹配几何结构](../conferences/icml-2026/cards/1601-1700.md#houry26a-optimization) · Gromov-Wasserstein at Scale, Beyond Squared Norms
- [用平均分数编码采样的访问历史](../conferences/icml-2026/cards/1601-1700.md#hu26g-optimization) · Score-Repellent Monte Carlo: Toward Efficient Non-Markovian Sampler with Constant Memory in General State Spaces
- [用两类备择调度带约束测量](../conferences/icml-2026/cards/1601-1700.md#hu26bi-optimization) · Learning the Best Under Constraints: A Duality-Based Framework
- [只用学习求解器采样整数变量](../conferences/icml-2026/cards/1601-1700.md#huang26j-optimization) · Unsupervised Neural Langevin Sampler for Mixed Integer Linear Programming
- [学习谱尾以适配目标函数粗糙度](../conferences/icml-2026/cards/1701-1800.md#huang26o-optimization) · ALAS: Additive Learnable Alpha-Stable Kernels for Flexible Bayesian Optimization
- [分离离群清洗与几何鲁棒化](../conferences/icml-2026/cards/1701-1800.md#huang26u-optimization) · Robust Learning via Nested Distributionally Robust Optimization
- [用全精度辅助支路校准二值反向梯度](../conferences/icml-2026/cards/1701-1800.md#huang26ah-optimization) · SURGE: Surrogate Gradient Adaptation in Binary Neural Networks
- [为矩阵优化器压缩方差缩减状态](../conferences/icml-2026/cards/1701-1800.md#huang26aj-optimization) · LiMuon: Light and Fast Muon Optimizer for Large Models
- [用罚项的局部可修复性排除不可行的盒极小点](../conferences/icml-2026/cards/1701-1800.md#huang26aw-optimization) · Local Minima in Quadratic-Penalty Relaxations of Binary Linear Programs
- [用范数的均方比稳定步幅，同时保留随机梯度方向](../conferences/icml-2026/cards/1701-1800.md#huang26bb-optimization) · GradientStabilizer: Fix the Norm, Not the Gradient
- [用离散聚类指派反哺连续共识图](../conferences/icml-2026/cards/1701-1800.md#huang26bg-optimization) · Discretely-Refined Multi-view Clustering via Aligned Anchor Learning
- [把固定规则放入可微精确覆盖层](../conferences/icml-2026/cards/1701-1800.md#huang26cn-optimization) · HONet: Data-Efficient Learning for Exact Cover Tasks via Hypergraph Optimization
- [用紧支撑到达时间平滑保持 Poisson 一阶矩](../conferences/icml-2026/cards/1801-1900.md#ibrahim26a-optimization) · A hitchhiker’s guide to Poisson gradient estimation
- [共享公开集稀释删除扰动](../conferences/icml-2026/cards/1801-1900.md#inane26a-optimization) · Unlearning with Asymmetric Sources: Improved Unlearning-Utility Trade-off with Public Data
- [按噪声与更新频率一起调批量](../conferences/icml-2026/cards/1801-1900.md#islamov26b-optimization) · On the Role of Batch Size in Stochastic Conditional Gradient Methods
- [用近流形回缩包装自适应优化器](../conferences/icml-2026/cards/1801-1900.md#javaloy26a-optimization) · An Embarrassingly Simple Way to Optimize Orthogonal Matrices at Scale
- [在锚图传输子问题中约束簇大小](../conferences/icml-2026/cards/1901-2000.md#jiachen26a-optimization) · SC-FAGC: Size Constrained Fast Anchor Graph Clustering
- [用公开特征谱重参数化隐私回归](../conferences/icml-2026/cards/1901-2000.md#jiang26w-optimization) · Private Learning with Public Feature Conditioning
- [在局部代理下降之间插入约束探索](../conferences/icml-2026/cards/1901-2000.md#jing26c-optimization) · Local Constrained Bayesian Optimization
- [把中间边际变成流动轨迹的局部力](../conferences/icml-2026/cards/2001-2100.md#kansal26a-optimization) · Multimarginal flow matching with optimal transport potentials
- [用动能决定各参数的阻尼强度](../conferences/icml-2026/cards/2001-2100.md#karoni26a-optimization) · Adaptive Momentum and Nonlinear Damping for Neural Network Training
- [用硬前向和自适应软梯度训练门网络](../conferences/icml-2026/cards/2001-2100.md#kim26a-optimization) · Align Forward, Adapt Backward: Closing the Discretization Gap in Logic Gate Networks
- [用热方程代理支持通用流形扩散训练](../conferences/icml-2026/cards/2101-2200.md#ko26d-optimization) · Riemannian Diffusion Models on General Manifolds via Physics-Informed Neural Networks
- [把自然语言反馈变成高斯过程的成对偏好](../conferences/icml-2026/cards/2101-2200.md#kobalczyk26a-optimization) · LILO: Bayesian Optimization with Natural Language Feedback
- [在最优传输中重分配源域输出质量](../conferences/icml-2026/cards/2101-2200.md#koc26a-optimization) · Incorporating Importance Weighting in Optimal Transport Based Domain Alignment
- [复用内层 SGD 的梯度并行更新逆 Hessian 近似](../conferences/icml-2026/cards/2101-2200.md#kong26a-optimization) · Natural Hypergradient Descent: Algorithm Design, Convergence Analysis, and Parallel Implementation
- [有限样本的最有影响观测集合](../conferences/icml-2026/cards/2101-2200.md#konrad26a-optimization) · Finding Most Influential Sets
- [用逻辑多面体分解约束 MAP 搜索](../conferences/icml-2026/cards/2201-2300.md#kurscheidt26a-optimization) · The Theory and Practice of MAP Inference over Non-Convex Constraints
- [用类型谓词合成满足条件的架构搜索空间](../conferences/icml-2026/cards/2201-2300.md#laarmann26a-optimization) · Search Space Synthesis for Parametric Functions
- [在保持 ReLU 函数时改善路径空间的条件](../conferences/icml-2026/cards/2201-2300.md#lebeurrier26a-optimization) · Path-conditioned training: a principled way to rescale ReLU neural networks
- [把预测误差投影到活跃约束的切空间](../conferences/icml-2026/cards/2301-2400.md#lee26q-optimization) · Decision-Focused Learning via Tangent-Space Projection of Prediction Error
- [多项 Logit 组合试验的最优设计](../conferences/icml-2026/cards/2301-2400.md#lee26ba-optimization) · Optimal Design for Multinomial Logit Model with Applications to Best Assortment Identification
- [可微逻辑门的两阶段常量绑定](../conferences/icml-2026/cards/2301-2400.md#lee26bg-optimization) · Two-Stage Unit Tying for Simplifying Differentiable Logic Gate Networks
- [用多轮私有 Hessian 草图修正回归参数](../conferences/icml-2026/cards/2301-2400.md#lev26a-optimization) · Near-Optimal Private Linear Regression via Iterative Hessian Mixing
- [缩放去中心化偏差校正的对偶更新](../conferences/icml-2026/cards/2401-2500.md#li26i-optimization) · Improving the Robustness-Utility Trade-off in Decentralized Learning over Sparse Networks
- [把惩罚项包络和差分正则两部分并行更新](../conferences/icml-2026/cards/2401-2500.md#li26ab-optimization) · MoSSP: A Momentum-Based Single-Loop Stochastic Penalty Method for Nonconvex Constrained DC-regularized Optimization
- [锚点流形上的均衡聚类](../conferences/icml-2026/cards/2401-2500.md#li26as-optimization) · Large Scale Manifold Balanced Clustering
- [用历史进展共同调配评估与跨任务迁移](../conferences/icml-2026/cards/2401-2500.md#li26dc-optimization) · Breaking Multi-Task Curse: Reward-Weighted Evolution for Black-Box Many-Task Optimization
- [异步联邦持续学习的双重漂移校准](../conferences/icml-2026/cards/2501-2600.md#li26gx-optimization) · Cross-task Calibration for Asynchronous Federated Continual Learning
- [用 Pareto 集匹配概率选择高质量多样批次](../conferences/icml-2026/cards/2601-2700.md#li26iu-optimization) · Probability of Matching for Batch Multi-Objective Bayesian Optimization
- [耦合剪裁与偏移阈值消除 DP 解偏差](../conferences/icml-2026/cards/2601-2700.md#li26iy-optimization) · Eliminating Solution Bias in Differentially Private Optimization
- [在低精度优化中配合尺度与加法更新](../conferences/icml-2026/cards/2701-2800.md#liang26p-optimization) · M+Adam: Low-Precision Training via Additive–Multiplicative Optimization
- [用衰减梯度缓冲复用循环坐标差分](../conferences/icml-2026/cards/2701-2800.md#liang26u-optimization) · Turning Stale Gradients into Stable Gradients: Coherent Coordinate Descent with Implicit Landscape Smoothing for Lightweight Zeroth-Order Optimization
- [保留正半定结构的可学习拟牛顿预条件](../conferences/icml-2026/cards/2701-2800.md#lifshitz26a-optimization) · L-SR1: Learned Symmetric-Rank-One Preconditioning
- [语义提议和图评估协同的网络搜索](../conferences/icml-2026/cards/2701-2800.md#lin26ac-optimization) · SAGE-NAS: Synergizing LLM-Based Semantic Agent with Graph-Based Evaluator for Neural Architecture Search
- [用罚函数 Hessian 给黑盒 QP 反传](../conferences/icml-2026/cards/2701-2800.md#linghu26b-optimization) · A Penalty Approach For Differentiation Through Black-box Quadratic Programming Solvers
- [通过子集采样偏置改变各层学习速度](../conferences/icml-2026/cards/2801-2900.md#liu26ad-optimization) · Less Data, Faster Training: repeating smaller datasets speeds up learning via sampling biases
- [把节点权重放进平稳混合分布](../conferences/icml-2026/cards/2801-2900.md#liu26bv-optimization) · Row-Stochastic Matrices Can Provably Outperform Doubly Stochastic Matrices in Decentralized Learning
- [在近球空间更新并沿可行锚纠正](../conferences/icml-2026/cards/2801-2900.md#liu26cd-optimization) · Hom-PGD$^+$: Fast Reparameterized Optimization over Non-convex Ball-Homeomorphic Set
- [梯度更新跨步并行](../conferences/icml-2026/cards/3001-3100.md#lu26h-optimization) · PASO: Step Parallel Stochastic Optimization
- [分支定界浅层增强](../conferences/icml-2026/cards/3001-3100.md#lu26v-optimization) · Dynamic Stratified Contrastive Learning with Upstream Augmentation for MILP Branching
- [用历史曲率偏置修正联邦平坦度失配](../conferences/icml-2026/cards/3001-3100.md#lu26ap-optimization) · FedScar: Correcting Geometric Bias for Flatness-Consistent Federated Learning
- [先聚组父模型神经元再拟合融合模型的内部表示](../conferences/icml-2026/cards/3001-3100.md#luenam26a-optimization) · Model Fusion via Retrofitting
- [凸差正则后验采样](../conferences/icml-2026/cards/3001-3100.md#luu26b-optimization) · DC-LA: Difference-of-Convex Langevin Algorithm
- [复制扩宽模型并用 μP 对齐噪声和学习率](../conferences/icml-2026/cards/3101-3200.md#ma26d-optimization) · $μ$pscaling small models: Principled warm starts and hyperparameter transfer
- [动态图上用一阶推拉做双层优化](../conferences/icml-2026/cards/3101-3200.md#ma26ak-optimization) · FAB: A First-Order AB-based Gradient Algorithm for Distributed Bilevel Optimization over Time-Varying Directed Graphs
- [用层级二分简化类别分布的梯度几何](../conferences/icml-2026/cards/3201-3300.md#manenti26a-optimization) · Beyond Softmax: A Natural Parameterization for Categorical Random Variables
- [用历史试验的辅助时序提高设计搜索效率](../conferences/icml-2026/cards/3201-3300.md#mani26a-optimization) · Few-Shot Design Optimization by Exploiting Auxiliary Information
- [正交权重更新缓解隐式表征的低秩限制](../conferences/icml-2026/cards/3201-3300.md#mcginnis26a-optimization) · Optimizing Rank for High-Fidelity Implicit Neural Representations
- [梯度归因隐式曲率正则](../conferences/icml-2026/cards/3201-3300.md#mehrpanah26a-optimization) · Improving Adversarial Robustness of Attribution via Implicit Regularization
- [在相邻重复块之间平滑优化器更新](../conferences/icml-2026/cards/3201-3300.md#meng26j-optimization) · Gradient Smoothing: Coupling Layer-wise Updates for Improved Optimization
- [先保证粒子更新可逆再估计熵](../conferences/icml-2026/cards/3201-3300.md#messaoud26a-optimization) · Particles Don’t Care About Z: Towards Scaling Entropy Estimation of Unnormalized Densities
- [预条件器批求逆根](../conferences/icml-2026/cards/3301-3400.md#modoranu26a-optimization) · DASH: Faster Shampoo via Batched Block Preconditioning and Efficient Inverse-Root Solvers
- [硬重置脉冲网络的分块并行](../conferences/icml-2026/cards/3301-3400.md#morrill26a-optimization) · Bullet Trains: Parallelizing Training of Temporally Precise Spiking Neural Networks
- [Bures–Wasserstein 的低秩单调协方差迭代](../conferences/icml-2026/cards/3301-3400.md#na26a-optimization) · ITSPACE: Monotone Gaussian Optimal Transport Updates
- [用优化器对偶范数调批大小](../conferences/icml-2026/cards/3301-3400.md#naganuma26a-optimization) · Adaptive Batch Sizes Using Non-Euclidean Gradient Noise Scales for Stochastic Sign and Spectral Descent
- [陈旧预条件器阻尼](../conferences/icml-2026/cards/3401-3500.md#nam26a-optimization) · FOAM: Frequency and Operator-Error Based Adaptive Damping Method for Reducing Staleness-Oriented Error for Shampoo
- [给多目标分布下降加入 Wasserstein 动量](../conferences/icml-2026/cards/3401-3500.md#nguyen26k-optimization) · Accelerated Multiple Wasserstein Gradient Flows for Multi-objective Distributional Optimization
- [用对数正态乘性权重稳定低精度前向训练](../conferences/icml-2026/cards/3401-3500.md#nishida26a-optimization) · Log-Normal Multiplicative Dynamics for Stable Low-Precision Deep Learning
- [损失感知运输歧义集](../conferences/icml-2026/cards/3401-3500.md#ohnemus26a-optimization) · Loss-Aware Distributionally Robust Optimization via Trainable Optimal Transport Ambiguity Sets
- [扰动点 Polyak 步长](../conferences/icml-2026/cards/3501-3600.md#oikonomou26b-optimization) · Adaptive Sharpness-Aware Minimization with a Polyak-type Step size: A Theory-Grounded Scheduler
- [次梯度分母保护](../conferences/icml-2026/cards/3501-3600.md#oikonomou26c-optimization) · Safeguarded Stochastic Polyak Step Sizes for Non-smooth Optimization: Robust Performance Without Small (Sub)Gradients
- [用衰减的缓存动量稳定部分参与聚合](../conferences/icml-2026/cards/3501-3600.md#otsuka26a-optimization) · Delayed Momentum Aggregation: Communication-efficient Byzantine-robust Federated Learning with Partial Participation
- [同时监测 SAM 原点和扰动点梯度](../conferences/icml-2026/cards/3501-3600.md#park26e-optimization) · Sharpness-Aware Minimization Can Hallucinate Minimizers
- [在客户端用分组归一动量平衡稀类](../conferences/icml-2026/cards/3501-3600.md#park26g-optimization) · Class-Grouped Normalized Momentum and Faster Hyperparameter Exploration to Tackle Class Imbalance in Federated Learning
- [硬操作的软梯度与软索引](../conferences/icml-2026/cards/3601-3700.md#paulus26a-optimization) · SoftJAX & SoftTorch: Empowering Automatic Differentiation Libraries with Informative Gradients
- [黑盒平滑的扰动预算](../conferences/icml-2026/cards/3601-3700.md#petersen26a-optimization) · Generalizing Stochastic Smoothing for Differentiation and Gradient Estimation
- [为期望改进校准 GP 预测低尾](../conferences/icml-2026/cards/3601-3700.md#pion26a-optimization) · Goal-Oriented Lower-Tail Calibration of Gaussian Processes for Bayesian Optimization
- [用原始–对偶训练使 Transformer 层间目标期望下降](../conferences/icml-2026/cards/3601-3700.md#porras-valenzuela26a-optimization) · A Constrained Optimization Perspective of Unrolled Transformers
- [沿奖励倾斜路径匹配概率流的速度增量](../conferences/icml-2026/cards/3601-3700.md#potaptchik26a-optimization) · Tilt Matching for Scalable Sampling and Fine-Tuning
- [用特征有效秩与 L2 共同缓解持续学习谱塌陷](../conferences/icml-2026/cards/3601-3700.md#prakash26b-optimization) · Spectral Collapse Drives Loss of Plasticity in Deep Continual Learning
- [用随机批与零阶反馈减轻 Markov 噪声混合开销](../conferences/icml-2026/cards/3601-3700.md#prokhorov26a-optimization) · Gradient-Free Approaches is a Key to an Efficient Interaction with Markovian Stochasticity
- [分开比较谱压缩强度和输入归一](../conferences/icml-2026/cards/3701-3800.md#qi26c-optimization) · Delving into Muon and Beyond: Deep Analysis and Extensions
- [对齐局部误差信号的到达时刻](../conferences/icml-2026/cards/3701-3800.md#qi26f-optimization) · Towards the Training of Deeper Predictive Coding Neural Networks
- [联邦双层学习的部署分布固定点](../conferences/icml-2026/cards/3701-3800.md#qian26b-optimization) · Federated Bilevel Performative Prediction
- [只在权重轨迹主方向上试探](../conferences/icml-2026/cards/3701-3800.md#qin26l-optimization) · Zeroth-Order Forward-Only SNN Training Inspiring Neuromorphic On-Chip Learning
- [轮换修改算子并用组合收益打分](../conferences/icml-2026/cards/3701-3800.md#qiu26a-optimization) · Evolving Interdependent Operators with Large Language Models for Multi-Objective Combinatorial Optimization
- [用单步策略视角推导低方差零阶 Hessian](../conferences/icml-2026/cards/3701-3800.md#qiu26h-optimization) · Revisiting Zeroth-Order Hessian Approximation: A Single-Step Policy Optimization Lens
- [摊销稀疏符号分析并融合 GPU 最优传输核](../conferences/icml-2026/cards/3701-3800.md#qiu26y-optimization) · cuRegOT: A GPU-Accelerated Solver for Entropic-Regularized Optimal Transport
- [用低秩适配缓解 Adam 与 Muon 的错配](../conferences/icml-2026/cards/3701-3800.md#qu26e-optimization) · Can Muon Fine-tune Adam-Pretrained Models?
- [把信息增益估计蒸馏为一次前向](../conferences/icml-2026/cards/3801-3900.md#rakotoarison26a-optimization) · $α$-PFN: Fast Entropy Search via In-Context Learning
- [让有标签锚点随比例约束移动](../conferences/icml-2026/cards/3801-3900.md#rakotomamonjy26a-optimization) · Particle Flow for Learning from Label Proportions
- [用 Lyapunov 下降设计极小极大算法](../conferences/icml-2026/cards/3801-3900.md#rankawat26a-optimization) · From Lyapunov Analysis to Algorithm Design in two-sided PL Minimax Optimization
- [只用比较反馈沿黎曼流形求下降方向](../conferences/icml-2026/cards/3801-3900.md#ren26m-optimization) · Riemannian Dueling Optimization
- [把保塑性的等距更新移出 Adam 矩估计](../conferences/icml-2026/cards/3801-3900.md#rosseau26a-optimization) · Preserving Plasticity in Continual Learning via Dynamical Isometry
- [先降低梯度噪声再取符号](../conferences/icml-2026/cards/3801-3900.md#roulet26a-optimization) · Per-example Gradients: a New Frontier for Understanding and Improving Optimizers
- [用低方差零阶 Langevin 做黑盒后验采样](../conferences/icml-2026/cards/3901-4000.md#sahin26a-optimization) · Zeroth-Order Non-Log-Concave Sampling with Variance Reduction and Applications to Inverse Problems
- [流匹配预训练的展开式优化器](../conferences/icml-2026/cards/3901-4000.md#saravanos26a-optimization) · Learning-to-Optimize via Deep Unfolded Flows
- [面向大模型的低秩进化策略](../conferences/icml-2026/cards/3901-4000.md#sarkar26a-optimization) · Evolution Strategies at the Hyperscale
- [未知时域的对抗约束在线优化](../conferences/icml-2026/cards/3901-4000.md#sarkar26c-optimization) · Optimal Anytime Algorithms for Online Convex Optimization with Adversarial Constraints
- [先传输配准再做低秩共聚类](../conferences/icml-2026/cards/3901-4000.md#schmidt26a-optimization) · Transport Clustering: Solving Low-Rank Optimal Transport via Clustering
- [按外推学习曲线保留慢热模型](../conferences/icml-2026/cards/3901-4000.md#schram26a-optimization) · Active Budget Allocation for Efficient Scaling Law Estimation via Surrogate-Guided Pruning
- [在受扰相补回非互易作用](../conferences/icml-2026/cards/3901-4000.md#scurria26a-optimization) · Equilibrium Propagation for Non-Conservative Systems
- [沿随机游走传播可靠深度标签](../conferences/icml-2026/cards/3901-4000.md#seddiqi26a-optimization) · Trajectory-Aware Heuristic Learning for Combinatorial Search
- [将带衰减的 Lion/Muon 写成重尾稳健的 Frank–Wolfe](../conferences/icml-2026/cards/4001-4100.md#sfyraki26a-optimization) · Lions and Muons: Optimization via Stochastic Frank-Wolfe under Heavy-Tailed Noise
- [利用流形量化规律加速 k-means 种子选择](../conferences/icml-2026/cards/4001-4100.md#shah26a-optimization) · Fast k-means Seeding Under The Manifold Hypothesis
- [用混合配置的影子价格做接纳](../conferences/icml-2026/cards/4001-4100.md#shen26x-optimization) · A Two-Layer Framework for Joint Online Configuration Selection and Admission Control
- [用同一突触预算稀疏权重与脉冲](../conferences/icml-2026/cards/4101-4200.md#shi26a-optimization) · UniSparse: Combining Weight Pruning and Spike Sparsification in Spiking Neural Networks
- [用判别子空间稳定估计标签漂移权重](../conferences/icml-2026/cards/4101-4200.md#shi26f-optimization) · Regularized Discriminative Alignment for Deep Representations under Label Shift
- [沿非线性参数路径选遗忘折中点](../conferences/icml-2026/cards/4101-4200.md#shi26x-optimization) · Exploring Nonlinear Pathway in Parameter Space for Machine Unlearning
- [脉冲网络双向初始化](../conferences/icml-2026/cards/4101-4200.md#shi26ae-optimization) · Training Deep Spiking Neural Networks without Normalization
- [按梯度噪声的状态依赖性联合调批量和动量](../conferences/icml-2026/cards/4101-4200.md#shulgin26a-optimization) · General Analysis of LMO-based Optimizers: Beyond Bounded Variance
- [缩小动量梯度差修正需要权衡剩余误差](../conferences/icml-2026/cards/4101-4200.md#shulgin26b-optimization) · Understanding MARS: When Scaling Momentum Correction Provably Helps
- [分解bandit协调昂贵设计搜索](../conferences/icml-2026/cards/4101-4200.md#singh26h-optimization) · Divide and Learn: Multi-Objective Combinatorial Optimization at Scale
- [锚定双时间尺度乐观更新](../conferences/icml-2026/cards/4101-4200.md#sohrabi26a-optimization) · Accelerated and Stable Convergence with Anchored Generalized Optimistic Method
- [解耦谱方向与方差适应](../conferences/icml-2026/cards/4201-4300.md#song26a-optimization) · Decoupling Variance and Scale-Invariant Updates in Adaptive Gradient Descent for Unified Vector and Matrix Optimization
- [近似局部GW与残余边际](../conferences/icml-2026/cards/4201-4300.md#song26h-optimization) · LoBCD-GW: A Fast and Data-Dependent Algorithm for Computing Gromov-Wasserstein Distance via Localized Block Coordinate Descent
- [零阶均方稳定边界](../conferences/icml-2026/cards/4201-4300.md#song26ac-optimization) · Zeroth-Order Optimization at the Edge of Stability
- [core-subspace-preservation](../conferences/icml-2026/cards/4201-4300.md#sun26r-optimization) · Revisiting the Role of Pretrained Weights in Model Merging: On Near-Optimality within the Core Subspace
- [密度约束反事实轨迹](../conferences/icml-2026/cards/4301-4400.md#tan26a-optimization) · Density-Guided Robust Counterfactual Explanations on Tabular Data under Model Multiplicity
- [stratified-particle-descent](../conferences/icml-2026/cards/4401-4500.md#tao26d-optimization) · Latent Space Robust Optimization of Neural Processes with Aligned Stratified Order-Statistic Loss Reduction
- [layerwise-variance-preserving-connectivity](../conferences/icml-2026/cards/4401-4500.md#tian26a-optimization) · Connecting Independently Trained Modes via Layer-Wise Connectivity
- [特征与样本双侧ARD](../conferences/icml-2026/cards/4401-4500.md#timans26a-optimization) · Joint Model and Data Sparsification via the Marginal Likelihood
- [位置编码约束的权重匹配](../conferences/icml-2026/cards/4401-4500.md#tran26d-optimization) · Functional Equivalence in Attention: A Comprehensive Study with Applications to Linear Mode Connectivity
- [accelerate-after-local-smoothness-entry](../conferences/icml-2026/cards/4501-4600.md#tyurin26b-optimization) · Near-Optimal Convergence of Accelerated Gradient Methods under Generalized and $(L_0,L_1)$-Smoothness
- [double-batch-dictionary-learning](../conferences/icml-2026/cards/4501-4600.md#valentin26a-optimization) · DB-KSVD: Scalable Alternating Optimization for Disentangling High-Dimensional Embedding Spaces
- [无真实数据的KFAC预条件](../conferences/icml-2026/cards/4501-4600.md#van-den-bosch26a-optimization) · DP-KFC: Data-Free Preconditioning for Privacy-Preserving Deep Learning
- [遗忘梯度作零均值控制变量](../conferences/icml-2026/cards/4501-4600.md#van-waerebeke26a-optimization) · Variance-Reduced $(\varepsilon, δ)-$Unlearning using Forget Set Gradients
- [在有效DAG空间内优化](../conferences/icml-2026/cards/4501-4600.md#vinas-torne26a-optimization) · PACER: Acyclic Causal Discovery from Large-scale Interventional Data
- [private-ridge-curvature-guard](../conferences/icml-2026/cards/4501-4600.md#wang26f-optimization) · Decoupling Regularization and Privacy in Differentially Private Ridge Regression and ERM
- [临界RNN的局部闭环教学信号](../conferences/icml-2026/cards/4601-4700.md#wang26be-optimization) · Global Credit Assignment via Dynamical Criticality

<a id="by-graph-and-recommendation"></a>

### 图学习与推荐

- [图粗化](../conferences/icml-2026/cards/0101-0200.md#bai26g-optimization) · Rethinking Efficient Graph Coarsening via a Non-Selfishness Principle
- [公平排序聚合](../conferences/icml-2026/cards/0401-0500.md#chakraborty26b-optimization) · Fairness in Aggregation: Optimal Top-$k$ and Improved Full Ranking
- [隐私图查询](../conferences/icml-2026/cards/0401-0500.md#chen26b-optimization) · Differentially Private Range Subgraph Counting
- [关系数据库的任务感知图结构优化](../conferences/icml-2026/cards/0601-0700.md#cheng26j-optimization) · What Makes a Desired Graph for Relational Deep Learning?
- [演化图的粗化映射增量更新](../conferences/icml-2026/cards/1401-1500.md#gupta26b-optimization) · Adapting to Evolving Graphs: A Scalable Framework for Dynamic Coarsening
- [用生成轨迹累积结构互斥的候选图](../conferences/icml-2026/cards/1601-1700.md#hosseini26b-optimization) · Neural Dispersion on Graphs
- [先按同配性归组再修正组间联邦梯度](../conferences/icml-2026/cards/1601-1700.md#huang26k-optimization) · Homophily-Heterogeneity Gradient Surgery for Federated Graph Learning
- [用同一个排列变量融合边权和节点属性证据](../conferences/icml-2026/cards/1701-1800.md#huang26az-optimization) · Attributed Network Alignment: Statistical Limits and Efficient Algorithm
- [用扩散采样生成多样图编辑候选](../conferences/icml-2026/cards/1701-1800.md#huang26bi-optimization) · Towards Generative Graph Matching for Graph Edit Distance Computation
- [用传输控制穿越组合松弛能量面](../conferences/icml-2026/cards/1701-1800.md#huang26bz-optimization) · Optimal Transport–Guided Stochastic Control for Graph Combinatorial Optimization
- [用扩散轨迹不稳定性寻找集合覆盖修复区](../conferences/icml-2026/cards/1801-1900.md#jaziri26a-optimization) · Generative Large Neighborhood Search: Scalable Set Cover Optimization via Discrete Diffusion
- [用树流动态规划分配定额标签预算](../conferences/icml-2026/cards/1901-2000.md#john26a-optimization) · An Approximation Algorithm for Graph Label Selection
- [动态图只在查询时抽取聚类核心集](../conferences/icml-2026/cards/2001-2100.md#jourdan26a-optimization) · Fully Dynamic Coreset Spectral Clustering
- [经粗化邻域限制新增节点的结构学习](../conferences/icml-2026/cards/2001-2100.md#kataria26a-optimization) · GraphFLEx: Unsupervised Structure Learning $\underline\textF$ramework for $\underline\textL$arge $\underline\textEx$panding $\underline\textGraph$s
- [动态图曝光下的反事实公平控制](../conferences/icml-2026/cards/2601-2700.md#li26kb-optimization) · COPF: An Online Framework for Deployment-Stable Counterfactual Fairness in Evolving Graphs
- [用期望采样成本训练设施开设概率](../conferences/icml-2026/cards/3701-3800.md#qian26d-optimization) · Learning to Approximate Uniform Facility Location via Graph Neural Networks

<a id="by-scientific-ml"></a>

### 科学机器学习

- [广义特征值积分轮廓](../conferences/icml-2026/cards/0501-0600.md#chen26ck-optimization) · Learning-Guided Integration Contours Construction for Fast Large-Scale Generalized Eigensolvers
- [语言模型预测与真实实验的门控](../conferences/icml-2026/cards/0601-0700.md#chen26fx-optimization) · LABO: LLM-Accelerated Bayesian Optimization through Broad Exploration and Selective Experimentation
- [扩散重建的对偶反馈与频谱均衡](../conferences/icml-2026/cards/0901-1000.md#du26n-optimization) · Plug-and-Play Diffusion Meets ADMM: Dual-Variable Coupling for Robust Medical Image Reconstruction
- [代数多重网格的稀疏粗层修正](../conferences/icml-2026/cards/1101-1200.md#fink26a-optimization) · RAPNet: Accelerating Algebraic Multigrid with Learned Sparse Corrections
- [量子激发态的多态重要性采样](../conferences/icml-2026/cards/1201-1300.md#gao26j-optimization) · Excited Pfaffians: Generalized Neural Wave Functions Across Structure and State
- [几何潜变量到 PDE 场的可微优化](../conferences/icml-2026/cards/1401-1500.md#guoze26a-optimization) · Geometry-Aware Neural Optimizer for Shape Optimization and Inversion
- [约束分子生成的顺序微调](../conferences/icml-2026/cards/1401-1500.md#gutjahr26a-optimization) · Constrained Flow Optimization via Sequential Fine-Tuning for Molecular Design
- [分区赌博机分配化学筛选预算](../conferences/icml-2026/cards/1401-1500.md#haddadnia26a-optimization) · Target-Aware Bandit Allocation for Scalable Surrogate Optimization in Chemical Space
- [在相近架构间评估共享权重的排名](../conferences/icml-2026/cards/1501-1600.md#he26bb-optimization) · Optimizing Network Simulation: Enhancing Performance Prediction Accuracy via Neural Architecture Search
- [用实际求解反馈优化语言模型生成的分支骨架](../conferences/icml-2026/cards/1601-1700.md#hou26d-optimization) · LLM4Branch: Large Language Model for Discovering Efficient Branching Policies of Integer Programs
- [分开探索候选谱系和编辑规则](../conferences/icml-2026/cards/1601-1700.md#hu26av-optimization) · Steering Large Language Models through the DMTA Cycle: Structure-Based Drug Design via Knowledge-Driven Bi-Level Thompson Sampling
- [让资产筛选与 Sharpe 目标贯通梯度](../conferences/icml-2026/cards/1801-1900.md#jeon26a-optimization) · Decision-focused Sparse Tangent Portfolio Optimization
- [用廉价法向回拉代替逐步求可行投影](../conferences/icml-2026/cards/1801-1900.md#jeon26d-optimization) · Efficient Diffusion Models under Nonconvex Equality and Inequality constraints via Landing
- [把状态切换写成可组合的结构约束](../conferences/icml-2026/cards/1901-2000.md#jing26a-optimization) · SwitchCraft: A Programmatic Framework for Designing State-Switching Proteins
- [沿神经活动主方向施加信用分配噪声](../conferences/icml-2026/cards/2001-2100.md#kang26n-optimization) · Credit Assignment via Neural Manifold Noise Correlation
- [用两条流拆分分子生成与完成概率](../conferences/icml-2026/cards/2001-2100.md#kim26j-optimization) · LeakGFN: Robust Molecular Generation in Generative Flow Networks via Flow Decomposition
- [用局部消元三元组限制稀疏填充](../conferences/icml-2026/cards/2501-2600.md#li26el-optimization) · Causal Structure Learning for Sparse Matrix Fill-in Reduction
- [用残差预测稀疏线性校正子空间](../conferences/icml-2026/cards/2701-2800.md#liao26a-optimization) · G-RANS: Generalizable Residual-Aware Neural Solvers for Sparse Systems
- [用零点约束稳定符号回归的稀疏路径](../conferences/icml-2026/cards/2701-2800.md#liu26n-optimization) · Stabilizing Equation Learning via Zero-Point Constraints
- [用几何扰动期望稳定代理驱动的形状优化](../conferences/icml-2026/cards/2801-2900.md#liu26cn-optimization) · UniDrag: Unified Multi-Field Prediction and Robust Shape Optimization for Vehicle Aerodynamics
- [按树突结构调度 GPU 仿真并推导梯度](../conferences/icml-2026/cards/3001-3100.md#lu26ar-optimization) · HelioX: A GPU-Native Framework for Simulation and Training of Biophysically Detailed Networks
- [用不变密度的测地结构补足稀疏随机轨迹](../conferences/icml-2026/cards/3201-3300.md#maoutsa26a-optimization) · From geometry to dynamics: Learning overdamped Langevin dynamics from sparse observations with geometric constraints
- [芯片宏布局排序](../conferences/icml-2026/cards/3301-3400.md#mo26d-optimization) · Order Matters: Unveiling the Hidden Impact of Macro Placement Sequences via Proxy-Guided LLM Evolution
- [沿解码器诱导的流形搜索抗菌肽](../conferences/icml-2026/cards/3301-3400.md#mozejko26a-optimization) · PepCompass: Navigating Peptide Embedding Spaces Using Riemannian Geometry
- [微分方程符号解搜索](../conferences/icml-2026/cards/3401-3500.md#oikonomou26a-optimization) · Neuro-Symbolic AI for Analytical Solutions of Differential Equations
- [用序列归因指导进化的变异位置](../conferences/icml-2026/cards/3501-3600.md#pandey26a-optimization) · Interpretability Driven Evolutionary Approach for the Design of Biological Sequences
- [把函数候选生成同诊断和搜索分开](../conferences/icml-2026/cards/3501-3600.md#pang26f-optimization) · Deliberate Evolution: Agentic Reasoning for Sample-Efficient Symbolic Regression with LLMs
- [把伴随采样推广到满足端点条件的路径空间](../conferences/icml-2026/cards/3501-3600.md#park26k-optimization) · Functional Adjoint Sampler: Scalable Sampling on Infinite Dimensional Spaces
- [序贯实验设计复用粒子后验](../conferences/icml-2026/cards/3601-3700.md#perez-vieites26a-optimization) · Online Bayesian Experimental Design for Partially Observed Dynamical Systems
- [用预测异常触发科学原理扩展](../conferences/icml-2026/cards/3601-3700.md#pu26a-optimization) · Principle-Evolvable Scientific Discovery via Uncertainty Minimization
- [以目标梯度保留拓扑条件的信息](../conferences/icml-2026/cards/3801-3900.md#rashed26a-optimization) · On the Generalization in Topology Optimization via Sensitivity-Conditioned Bernoulli Flow Matching
- [在参数零空间注入历史动量](../conferences/icml-2026/cards/3801-3900.md#raviola26a-optimization) · A Dirac-Frenkel-Onsager Principle: Instantaneous Residual Minimization with Gauge Momentum for Nonlinear Parametrizations of PDE Solutions
- [分离算术结构搜索与误差认证](../conferences/icml-2026/cards/3801-3900.md#real26a-optimization) · AutoNumerics-Zero: Automated Discovery of State-of-the-Art Mathematical Functions
- [按过阈概率选择后续实验](../conferences/icml-2026/cards/3901-4000.md#rubbi26a-optimization) · Many Needles in a Haystack: Active Hit Discovery for Perturbation Experiments
- [逐项影响反馈驱动的符号回归](../conferences/icml-2026/cards/3901-4000.md#saveliev26a-optimization) · Influence-Guided Symbolic Regression: Scientific Discovery via LLM-Driven Equation Search with Granular Feedback
<!-- classification:end -->
