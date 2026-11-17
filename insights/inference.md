# 推理策略

[首页](../README.md) · [参与贡献](../CONTRIBUTING.md) · [English](../en/insights/inference.md)

解码、测试时适配与高效执行。

<!-- classification:start -->
## 按研究领域浏览

[大语言模型](#by-llm) · [计算机视觉](#by-computer-vision) · [自然语言处理](#by-nlp) · [强化学习](#by-reinforcement-learning) · [机器人学](#by-robotics) · [多模态学习](#by-multimodal) · [机器学习基础与统计](#by-ml-foundations) · [图学习与推荐](#by-graph-and-recommendation) · [科学机器学习](#by-scientific-ml)

<a id="by-llm"></a>

### 大语言模型

- [表征干预](../conferences/icml-2026/cards/0001-0100.md#abdullaev26a-inference) · Concept Heterogeneity-aware Representation Steering
- [交互式研究 Agent](../conferences/icml-2026/cards/0001-0100.md#ai26a-inference) · An Interactive Paradigm for Deep Research
- [多模型答案聚合](../conferences/icml-2026/cards/0001-0100.md#ai26d-inference) · Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information
- [动态推理预算](../conferences/icml-2026/cards/0001-0100.md#akhauri26a-inference) · Compute Where it Counts: Self Optimizing Language Models
- [小模型 Agent 路由](../conferences/icml-2026/cards/0001-0100.md#alazraki26a-inference) · Scaling Small Agents Through Strategy Auctions
- [模型文本溯源](../conferences/icml-2026/cards/0101-0200.md#ardoin26a-inference) · LLM Self-Recognition: Steering and Retrieving Activation Signatures
- [多 Agent 红队](../conferences/icml-2026/cards/0101-0200.md#asad26a-inference) · RedDebate: Safer Responses Through Multi-Agent Red Teaming Debates
- [离散扩散搜索](../conferences/icml-2026/cards/0101-0200.md#bai26f-inference) · PRISM: Efficient Test-Time Scaling via Hierarchical Search and Self-Verification for Discrete Diffusion Language Models
- [偏好对齐解码](../conferences/icml-2026/cards/0201-0300.md#berdoz26a-inference) · Alignment-Aware Decoding
- [KV 缓存压缩](../conferences/icml-2026/cards/0201-0300.md#bhatnagar26a-inference) · STAR-KV: Low-Rank KV Cache Compression via Soft Thresholding for Adaptive Rank Control
- [推理预算分配](../conferences/icml-2026/cards/0201-0300.md#bilal26a-inference) · What If We Allocate Test-Time Compute Adaptively?
- [冷启动个性化](../conferences/icml-2026/cards/0301-0400.md#bose26a-inference) · Cold-Start Personalization via Bayesian Adaptive Questioning
- [MoE 稀疏推理](../conferences/icml-2026/cards/0301-0400.md#cai26i-inference) · Mining Tensor/Neuron-Level Sparsity to Maximize Mixture-of-Experts Potential in Post-Training and Inference
- [扩散语言模型解码](../conferences/icml-2026/cards/0301-0400.md#cao26d-inference) · Search or Accelerate: Confidence-Switched Position Beam Search for Diffusion Language Models
- [LLM 推理隐私](../conferences/icml-2026/cards/0301-0400.md#cao26q-inference) · OSNIP: Balancing the Privacy-Utility-Efficiency Trilemma in LLM Inference via Obfuscated Semantic Null Space
- [模型路由](../conferences/icml-2026/cards/0401-0500.md#cao26ac-inference) · Models Under SCOPE: Scalable and Controllable Routing via Pre-hoc Reasoning
- [非结构化稀疏推理](../conferences/icml-2026/cards/0401-0500.md#cetin26a-inference) · Sparser, Faster, Lighter Transformer Language Models
- [自投机解码](../conferences/icml-2026/cards/0401-0500.md#cha26a-inference) · KnapSpec: Self-Speculative Decoding via Adaptive Layer Selection as a Knapsack Problem
- [跨层 KV 缓存压缩](../conferences/icml-2026/cards/0401-0500.md#chang26d-inference) · xKV: Cross-Layer KV-Cache Compression via Aligned Singular Vector Extraction
- [GUI 流程复用](../conferences/icml-2026/cards/0501-0600.md#chen26ar-inference) · AutoRPA: Efficient GUI Automation through LLM-Driven Code Synthesis from Interactions
- [分级披露文本水印](../conferences/icml-2026/cards/0501-0600.md#chen26bs-inference) · Selective Disclosure Watermarking for Large Language Models
- [块扩散投机解码](../conferences/icml-2026/cards/0501-0600.md#chen26bv-inference) · DFlash: Block Diffusion for Flash Speculative Decoding
- [树搜索 KV 缓存管理](../conferences/icml-2026/cards/0501-0600.md#chen26cd-inference) · ArborKV: Structure-Aware KV Cache Management for Scaling Tree-based LLM Reasoning
- [扩散语言模型解码](../conferences/icml-2026/cards/0501-0600.md#chen26ci-inference) · Beyond Confidence: Adaptive and Coherent Decoding for Diffusion Language Models
- [堆内存循环不变量生成](../conferences/icml-2026/cards/0501-0600.md#chen26cm-inference) · MALICE: Memory-aware Loop Invariants Generation on Symbolic Execution Traces
- [动态检索抗投毒](../conferences/icml-2026/cards/0501-0600.md#chen26cw-inference) · RADAR: Defending RAG Dynamically against Retrieval Corruption
- [指令与上下文示例联合选择](../conferences/icml-2026/cards/0501-0600.md#chen26dt-inference) · SMILE: Extended Deep Submodular Function-Based Instruction and In-context Learning Demonstration Selection
- [神经元一致性解码](../conferences/icml-2026/cards/0601-0700.md#chen26eo-inference) · Do LLMs Signal When They’re Right? Evidence from Neuron Agreement
- [细粒度 MoE 专家采样](../conferences/icml-2026/cards/0601-0700.md#chen26er-inference) · Certain Head, Uncertain Tail: Expert-Sample for Test-Time Scaling in Fine-Grained MoE
- [检索证据净化与推导](../conferences/icml-2026/cards/0601-0700.md#chen26et-inference) · From Extraction to Deduction: Resolving Functional Misalignment in RAG via a Collaborative Critic-Reasoner Framework
- [投机解码的动态草稿词表](../conferences/icml-2026/cards/0601-0700.md#chen26fm-inference) · NanoSpec: Accelerating Speculative Decoding using Minimalist In-Context Vocabularies
- [智能体批推理的缓存拥塞控制](../conferences/icml-2026/cards/0601-0700.md#chen26fs-inference) · CONCUR: High-Throughput Agentic Batch Inference of LLM via Congestion-Based Concurrency Control
- [批容量与缓存的影子价格路由](../conferences/icml-2026/cards/0601-0700.md#chen26ft-inference) · Online Linear Programming for Multi-Objective Routing in LLM Serving
- [逐题技能路由与专家批处理](../conferences/icml-2026/cards/0601-0700.md#chen26fy-inference) · Skill-Based Mixture-of-Experts: Adaptive Routing for Heterogeneous Reasoning via Inferred Skills
- [语言模型 SVD 压缩的分级秩分配](../conferences/icml-2026/cards/0601-0700.md#chen26ge-inference) · CGSVD: Cascaded Granular Singular Value Decomposition for Large Language Model Compression
- [风险聚合引导的解码回滚](../conferences/icml-2026/cards/0601-0700.md#chen26ha-inference) · RBCBF: Decoding Time Safety Alignment via Risk Guided Rollback and Barrier Control
- [代码文档的依赖感知搜索](../conferences/icml-2026/cards/0601-0700.md#cheng26c-inference) · Escaping Whack-a-Mole: Optimizing Documentation as Repo-Specific Playbooks for Coding Agents
- [MXFP4 的溢出感知缩放](../conferences/icml-2026/cards/0701-0800.md#chhugani26a-inference) · Unveiling the Potential of Quantization with MXFP4: Strategies for Quantization Error Reduction
- [证据排列混合的拒答门控](../conferences/icml-2026/cards/0701-0800.md#chlon26a-inference) · Predictable Compression Failures: Order Sensitivity and Information Budgeting for Evidence-Grounded Binary Adjudication
- [主奇异子空间保留后再量化](../conferences/icml-2026/cards/0701-0800.md#cho26e-inference) · Preserve-Then-Quantize: Balancing Rank Budgets for Quantization Error Reconstruction in LLMs
- [相关筛选与干预验证的 SAE 引导](../conferences/icml-2026/cards/0701-0800.md#cho26h-inference) · CorrSteer: Generation-Time LLM Steering via Correlated Sparse Autoencoder Features
- [低延迟分词的绑核与轮询](../conferences/icml-2026/cards/0701-0800.md#choi26b-inference) · PinTok: Tokenizers Deserve Dedicated Pinned CPU-Compute and Memory
- [同谱系模型的上下文忠实性门控](../conferences/icml-2026/cards/0701-0800.md#choi26e-inference) · The Truth Stays in the Family: Enhancing Contextual Truthfulness via Inherited Heads in Model Lineages
- [RAG 段落注意力方差过滤](../conferences/icml-2026/cards/0701-0800.md#choudhary26b-inference) · Through the Stealth Lens: Attention-Aware Defenses Against Poisoning in RAG
- [多层原型输入审核](../conferences/icml-2026/cards/0701-0800.md#chrabaszcz26a-inference) · Efficient LLM Moderation with Multi-Layer Latent Prototypes
- [长上下文思维链示例排序](../conferences/icml-2026/cards/0701-0800.md#chung26c-inference) · Many-Shot CoT-ICL: Making In-Context Learning Truly Learn
- [概率常识溯因推理](../conferences/icml-2026/cards/0701-0800.md#cotnareanu26a-inference) · Abductive Reasoning with Probabilistic Commonsense
- [含平局偏好的分布校准聚合](../conferences/icml-2026/cards/0801-0900.md#dadkhahi26a-inference) · Distribution-Calibrated Inference Time Compute for Thinking LLM-as-a-Judge
- [全局约束的序贯蒙特卡洛解码](../conferences/icml-2026/cards/0801-0900.md#dang26c-inference) · Mitigating Bias in Locally Constrained Decoding via Tractable Proposals
- [KV 缓存的窗口离群保留](../conferences/icml-2026/cards/0801-0900.md#datta26b-inference) · ManifoldKV: Training-Free KV Cache Compression via Euclidean Outlier Detection
- [推理生成中的动态弃答](../conferences/icml-2026/cards/0801-0900.md#davidov26a-inference) · Knowing When to Quit: A Principled Framework for Dynamic Abstention in LLM Reasoning
- [词元几何感知的截断解码](../conferences/icml-2026/cards/0801-0900.md#davoodi26a-inference) · Geometry-Aware Decoding with Wasserstein-Regularized Truncation and Mass Penalties for Large Language Models
- [用注意力温度缓解上下文分布偏移](../conferences/icml-2026/cards/0801-0900.md#demir26a-inference) · Optimal Attention Temperature Improves the Robustness of In-Context Learning under Distribution Shift in High Dimensions
- [混合专家的全局渐进量化](../conferences/icml-2026/cards/0801-0900.md#deng26t-inference) · GEMQ: Global Expert-Level Mixed-Precision Quantization for MoE LLMs
- [预算约束下的自适应群体提问](../conferences/icml-2026/cards/0901-1000.md#ding26d-inference) · Whom to Query for What: Adaptive Group Elicitation via Multi-Turn LLM Interactions
- [端云推理的依赖感知子任务路由](../conferences/icml-2026/cards/0901-1000.md#dong26g-inference) · HybridFlow: Resource-Adaptive Subtask Routing for Efficient Edge-Cloud LLM Inference
- [以未来注意力训练 KV 淘汰](../conferences/icml-2026/cards/0901-1000.md#dong26h-inference) · ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution
- [反向关系的反射检索](../conferences/icml-2026/cards/0901-1000.md#du26a-inference) · Chiral Symmetry Breaking in Transformers: A Group-Equivariant Framework for Addressing the Reversal Curse via Adjoint Manifold Mappings
- [按推理贡献分配注意力缓存](../conferences/icml-2026/cards/0901-1000.md#du26e-inference) · Which Heads Matter for Reasoning? RL-Guided KV Cache Compression
- [值缓存的低秩阻尼解码](../conferences/icml-2026/cards/0901-1000.md#du26m-inference) · Escaping Mode Collapse in LLM Generation via Geometric Regulation
- [基于词元熵的动态搜索分支](../conferences/icml-2026/cards/1001-1100.md#evans26a-inference) · Entropy-informed Decoding: Adaptive Information-Driven Branching
- [用稀疏特征做流式安全检测](../conferences/icml-2026/cards/1001-1100.md#fang26a-inference) · NExT-Guard: Streaming Safeguard without Token-Level Labels
- [联合规划的知识缺口澄清](../conferences/icml-2026/cards/1001-1100.md#fang26i-inference) · MINT: Minimal Information Neuro-Symbolic Tree for Objective-Driven Knowledge-Gap Reasoning and Active Elicitation
- [反事实推理的共形 token 筛选](../conferences/icml-2026/cards/1001-1100.md#fayyazi26a-inference) · COFT: Counterfactual–Conformal Decoding for Fair Chain-of-Thought Reasoning in Large Language Models
- [跨问题分配自洽采样预算](../conferences/icml-2026/cards/1001-1100.md#feng26a-inference) · Optimal Self-Consistency for Efficient Reasoning with Large Language Models
- [按输出扰动分配 KV 缓存预算](../conferences/icml-2026/cards/1101-1200.md#feng26j-inference) · CriticalKV: Optimizing KV Cache Eviction from an Output Perturbation Perspective
- [扩散解码的前瞻探索](../conferences/icml-2026/cards/1101-1200.md#fu26h-inference) · From Bits to Rounds: Parallel Decoding with Exploration for Diffusion Language Models
- [逐词元采样的语言模型集成](../conferences/icml-2026/cards/1101-1200.md#fu26j-inference) · Rethinking LLM Ensembling from the Perspective of Mixture Models
- [按注意力熵分配 KV 保留预算](../conferences/icml-2026/cards/1201-1300.md#gao26a-inference) · EntroKV: Entropy-Guided Dynamic Budget Allocation for KV-Cache Compression
- [按生成时延动态划分 GPU](../conferences/icml-2026/cards/1201-1300.md#gao26m-inference) · DuetServe: Harmonizing Prefill and Decode for LLM Serving via Adaptive GPU Multiplexing
- [代码图解释引导恶意行为分析](../conferences/icml-2026/cards/1201-1300.md#gao26u-inference) · Efficient Code Analysis via Graph Representation Learning-Guided Large Language Models
- [循环深度模型的并行采样](../conferences/icml-2026/cards/1201-1300.md#geiping26a-inference) · Efficient Parallel Samplers for Recurrent-Depth Models and Their Connection to Diffusion Language Models
- [跨智能体的解码缓存复用](../conferences/icml-2026/cards/1201-1300.md#geng26a-inference) · RelayCaching: Accelerating LLM Collaboration via Decoding KV Cache Reuse
- [推理粒子的自适应重采样退火](../conferences/icml-2026/cards/1201-1300.md#giannone26b-inference) · Mitigating Premature Exploitation in Particle-based Monte Carlo for Inference-Time Scaling
- [用嵌入探针做多 token 投机解码](../conferences/icml-2026/cards/1201-1300.md#goel26a-inference) · Efficient Training-Free Multi-Token Prediction via Embedding-Space Probing
- [语言模型猜测与形式验证的循环上界](../conferences/icml-2026/cards/1301-1400.md#gong26e-inference) · LLM-Guided Loop Bound Generation for Program Termination Verification
- [切断多轮越狱的评委反馈](../conferences/icml-2026/cards/1301-1400.md#gong26h-inference) · D-Judge: Disrupting Multi-Turn Jailbreaks using Semantics-Preserving Output Rewriting
- [概率电路联合草拟多字节](../conferences/icml-2026/cards/1301-1400.md#grivas26a-inference) · Fast and Expressive Multi-Byte Prediction with Probabilistic Circuits
- [MoE 二维分块低秩量化](../conferences/icml-2026/cards/1301-1400.md#gu26c-inference) · TileQ: Efficient Low-Rank Quantization of Mixture-of-Experts with 2D Tiling
- [按注意力输出扰动裁剪 KV 缓存](../conferences/icml-2026/cards/1301-1400.md#gu26h-inference) · OBCache: Optimal Brain KV Cache Pruning for Efficient Long-Context LLM Inference
- [由隐藏更新几何判定提前退出](../conferences/icml-2026/cards/1301-1400.md#gu26k-inference) · Detecting the Semantic Fixed Point: A Geometric Framework for Efficient Inference
- [多智能体的多跳消息合并](../conferences/icml-2026/cards/1301-1400.md#guan26i-inference) · MOC: Multi-Order Communication in LLM-based Multi-Agent Systems
- [启发式生成的推导图规划](../conferences/icml-2026/cards/1301-1400.md#gungordu26a-inference) · PathWise: Planning through World Model for Automated Heuristic Design via Self-Evolving LLMs
- [推理词元的重要性缓存淘汰](../conferences/icml-2026/cards/1301-1400.md#guo26b-inference) · Dynamic Thinking-Token Selection for Efficient Reasoning in Large Reasoning Models
- [代码安全的案例检索与动态核验](../conferences/icml-2026/cards/1301-1400.md#guo26o-inference) · BlueCodeAgent: A Blue Teaming Agent Powered by Automated Red Teaming for CodeGen AI
- [专家引导的分阶段 GPU 内核生成](../conferences/icml-2026/cards/1401-1500.md#han26h-inference) · EGG: An Expert-Guided Agent Framework for Kernel Generation
- [端云投机解码的流水与双阈值验证](../conferences/icml-2026/cards/1401-1500.md#han26k-inference) · PipeSD: An Efficient Cloud-Edge Collaborative Pipeline Inference Framework with Speculative Decoding
- [按可恢复性分配词元计算](../conferences/icml-2026/cards/1401-1500.md#han26p-inference) · Bring Future Vision: Dynamic Computation Allocation Guided by Lightweight Feature Forecaster
- [把温和剪枝分解到现有稀疏内核](../conferences/icml-2026/cards/1401-1500.md#hao26a-inference) · SlideSparse: Fast and Flexible (2N-2):2N Structured Sparsity
- [把单模型路由扩为可校准的候选集](../conferences/icml-2026/cards/1401-1500.md#hao26c-inference) · RACER: Risk-Aware Calibrated Efficient Routing for Large Language Models
- [边缘化合法词元覆盖以消除提示边界偏置](../conferences/icml-2026/cards/1401-1500.md#hayase26a-inference) · Sampling from Your Language Model One Byte at a Time
- [以违反程序属性的最小反例驱动代码修复](../conferences/icml-2026/cards/1401-1500.md#he26d-inference) · PGS: Effective LLM Code Refinement via Property-Oriented and Structurally Minimal Feedback
- [把全序列参考分布约束分解为逐步解码预算](../conferences/icml-2026/cards/1501-1600.md#he26k-inference) · Anchored Decoding: Provably Reducing Copyright Risk for Any Language Model
- [按延迟余量路由增量预填充](../conferences/icml-2026/cards/1501-1600.md#he26r-inference) · Efficient Multi-round LLM Inference over Disaggregated Serving
- [按算子特征拆分推理记忆流水线](../conferences/icml-2026/cards/1501-1600.md#he26ab-inference) · Understand and Accelerate Memory Processing Pipeline for Large Language Model Inference
- [按章节状态调节长文解码](../conferences/icml-2026/cards/1501-1600.md#he26ar-inference) · On Stable Long-Form Generation: Benchmarking and Mitigating Length Volatility
- [扩散并行规划配合局部自回归解码](../conferences/icml-2026/cards/1501-1600.md#hersche26a-inference) · Locally Coherent Parallel Decoding in Diffusion Language Models
- [让引导强度由当前词元激活决定](../conferences/icml-2026/cards/1501-1600.md#heyman26a-inference) · Steer Like the LLM: Activation Steering that Mimics Prompting
- [按前向轮次和层位置淘汰 MoE 专家](../conferences/icml-2026/cards/1501-1600.md#hoang26d-inference) · SpecMD: A Comprehensive Study On Speculative Expert Prefetching
- [以解掩位置选择编码文本水印](../conferences/icml-2026/cards/1501-1600.md#hong26i-inference) · dgMARK: Decoding-Guided Watermarking for Diffusion Language Models
- [在已偏转的残差流上学习后续人格方向](../conferences/icml-2026/cards/1501-1600.md#hoppe26a-inference) · Controllable and Explainable Personality Sliders for LLMs at Inference Time
- [用残差流风险信号有条件地启用慢推理](../conferences/icml-2026/cards/1601-1700.md#hu26m-inference) · PrivGate: Steering Contextual Integrity in LLMs via Latent Space Geometry
- [稀疏门控后在同批请求间重分配验证预算](../conferences/icml-2026/cards/1601-1700.md#hu26ar-inference) · ECHO: Elastic Speculative Decoding with Sparse Gating for High-Concurrency Scenarios
- [用隐状态偏移触发短程去迎合](../conferences/icml-2026/cards/1601-1700.md#hu26bb-inference) · Real-Time Monitoring and Calibration of Chain-of-Thought Sycophancy in Large Reasoning Models
- [预编译词元等价类供约束解码查表](../conferences/icml-2026/cards/1601-1700.md#hua26b-inference) · Gram2Token: Enabling Run-time GPU-Native Grammar-Constrained Decoding for LLMs
- [用前两名计数近似答案众数的停采后验](../conferences/icml-2026/cards/1701-1800.md#huang26ak-inference) · Optimal Bayesian Stopping for Efficient Inference of Consistent LLM Answers
- [让并行验证器独立找错，并将长证明分段审核](../conferences/icml-2026/cards/1701-1800.md#huang26ay-inference) · Pessimistic Verification for Open-Ended Math Questions
- [将模型选择与推理预算学习为一个在线动作](../conferences/icml-2026/cards/1701-1800.md#huang26bd-inference) · UniScale: Adaptive Unified Inference Scaling via Online Joint Optimization of Model Routing and Test-Time Scaling
- [按编辑意图选择水印嵌入强度](../conferences/icml-2026/cards/1701-1800.md#huang26ck-inference) · IACW: Intent-Aware Controllable Watermarking for Scalable Authorial Intent Attribution
- [用学习价值函数重采黑盒代理轨迹](../conferences/icml-2026/cards/1701-1800.md#hwang26i-inference) · Agentic Monte Carlo: Simulating Reinforcement Learning for Black-Box Agents
- [定位风格注意力头后再做人格引导](../conferences/icml-2026/cards/1801-1900.md#izawa26a-inference) · Steering at the Source: Style Modulation Heads for Robust Persona Control
- [按共享底座与适配器分解代理缓存](../conferences/icml-2026/cards/1801-1900.md#jeon26b-inference) · LRAgent: Efficient KV Cache Sharing for Multi-LoRA LLM Agents
- [用动态测试校准代码回答的接受阈值](../conferences/icml-2026/cards/1801-1900.md#jeong26a-inference) · Towards Functional Correctness of Code Models with Selective Generation
- [按新证据逐步重建代理记忆](../conferences/icml-2026/cards/1801-1900.md#ji26d-inference) · Memory is Reconstructed, Not Retrieved: Graph Memory for LLM Agents
- [用续写路径的概率集中度校正局部低温采样](../conferences/icml-2026/cards/1801-1900.md#ji26j-inference) · Scalable Power Sampling: Unlocking Efficient, Training-Free Reasoning for LLMs via Distribution Sharpening
- [用低位分数预筛可跳过的注意力块](../conferences/icml-2026/cards/1801-1900.md#ji26m-inference) · SALE : Low-bit Estimation for Efficient Sparse Attention in Long-context LLM Prefilling
- [把逐句引证核验写成多重检验](../conferences/icml-2026/cards/1901-2000.md#jiang26f-inference) · CiteGuard: Conformal False-Discovery Control for Faithful Retrieval-Augmented Generation
- [按实时请求组合切换异构模型部署](../conferences/icml-2026/cards/1901-2000.md#jiang26k-inference) · OServe: Accelerating LLM Serving via Spatial-Temporal Workload Orchestration
- [分组件监控和扩缩推理工作组](../conferences/icml-2026/cards/1901-2000.md#jiang26z-inference) · HexGen-3: A Fully Disaggregated LLM Serving Framework with Fine-Grained Heterogeneous Resource Autoscaling
- [在代理执行工具前纠正可见的中间推理](../conferences/icml-2026/cards/1901-2000.md#jiang26bc-inference) · Think Twice Before You Act: Enhancing Agent Behavioral Safety with Thought Correction
- [用依赖图重组失效的工具调用路径](../conferences/icml-2026/cards/1901-2000.md#jiang26be-inference) · NaviAgent: Graph-Driven Bilevel Planning for Scalable Tool Orchestration
- [用多目标统计依赖筛选缓和价值冲突的提示](../conferences/icml-2026/cards/1901-2000.md#jiang26bh-inference) · PICACO: Pluralistic In-Context Value Alignment via Total Correlation Optimization
- [让未提交草稿维持扩散解码的双向上下文](../conferences/icml-2026/cards/1901-2000.md#jiao26g-inference) · DC-Leap: Training-Free Acceleration of dLLMs via Draft-Guided Contiguous Leaping Decoding
- [给提示生成器同时输入模型配置和资源偏好](../conferences/icml-2026/cards/1901-2000.md#jiao26h-inference) · TAMPO: Task- and Model-Aware Automatic Prompt Optimization for Auto-Routing in LLM-based Systems
- [每层临时压缩注意力词元再还原](../conferences/icml-2026/cards/1901-2000.md#jo26a-inference) · Token Sparse Attention: Efficient Long-Context Inference with Interleaved Token Selection
- [按置信差设计私有生成后的句级修补](../conferences/icml-2026/cards/1901-2000.md#joo26a-inference) · PEARL: Differentially Private and Entropy-Aware Regulated Language Generation
- [用扩散答案草稿提前检索桥接实体](../conferences/icml-2026/cards/2001-2100.md#junger26a-inference) · Self-Augmenting Retrieval for Diffusion Language Models
- [在字节小块内并行猜测并按需验证](../conferences/icml-2026/cards/2001-2100.md#kallini26a-inference) · Fast Byte Latent Transformer
- [用代理失败轨迹反推上下文保留规则](../conferences/icml-2026/cards/2001-2100.md#kang26b-inference) · ACON: Optimizing Context Compression for Long-horizon LLM Agents

<a id="by-computer-vision"></a>

### 计算机视觉

- [扩散模型逻辑控制](../conferences/icml-2026/cards/0001-0100.md#alesiani26a-inference) · Logical Guidance for the Exact Composition of Diffusion Models
- [图像隐写](../conferences/icml-2026/cards/0101-0200.md#bae26b-inference) · Training-Free Coverless Multi-Image Steganography with Access Control
- [扩散逆问题](../conferences/icml-2026/cards/0201-0300.md#bang26a-inference) · Triadic Dynamics Aware Diffusion Posterior Sampling for Inverse Problems: Optimizing Guidance and Stochasticity Schedules
- [潜空间流匹配](../conferences/icml-2026/cards/0301-0400.md#briq26a-inference) · Exploring and Exploiting Stability in Latent Flow Matching
- [无分类器引导](../conferences/icml-2026/cards/0301-0400.md#cai26g-inference) · Improving Classifier-Free Guidance of Flow Matching via Manifold Projection
- [多实例图像到三维](../conferences/icml-2026/cards/0301-0400.md#cai26n-inference) · TIMI: Training-Free Image-to-3D Multi-Instance Generation with Spatial Fidelity
- [低延迟图像压缩](../conferences/icml-2026/cards/0301-0400.md#cao26e-inference) · Efficient Learned Image Compression without Entropy Coding
- [扩散正负概念引导](../conferences/icml-2026/cards/0401-0500.md#chang26c-inference) · ContrastiveCFG: Guiding Diffusion Sampling by Contrasting Positive and Negative Concepts
- [免训练视频异常检测](../conferences/icml-2026/cards/0401-0500.md#chen26v-inference) · PRISM: Training-Free Video Anomaly Detection via Intrinsic Statistical Modeling
- [归一化流采样](../conferences/icml-2026/cards/0501-0600.md#chen26aj-inference) · Normalizing Flows with Iterative Denoising
- [流匹配的双锚点积分](../conferences/icml-2026/cards/0501-0600.md#chen26bp-inference) · Bi-Anchor Interpolation Solver for Accelerating Generative Modeling
- [网格词元的投机解码](../conferences/icml-2026/cards/0501-0600.md#chen26dn-inference) · XSpecMesh: Quality-Preserving Auto-Regressive Mesh Generation Acceleration via Multi-Head Speculative Decoding
- [新视角扩散的语义条件](../conferences/icml-2026/cards/0601-0700.md#chen26ey-inference) · SemanticNVS: Improving Semantic Scene Understanding in Generative Novel View Synthesis
- [自回归图像采样的轨迹剪枝](../conferences/icml-2026/cards/0601-0700.md#chen26fc-inference) · ScalingAR: Scaling Confidence for Autoregressive Image Generation
- [桥式生成模型的分频先验引导](../conferences/icml-2026/cards/0601-0700.md#chen26fq-inference) · GuidedBridge: Training-freely Improving Bridge Models with Prior Guidance
- [图像到点云配准的动态交互深度](../conferences/icml-2026/cards/0601-0700.md#cheng26b-inference) · FS-I2P: A Hierarchical Focus–Sweep Registration Network with Dynamically Allocated Depth
- [扩散采样的切向增量放大](../conferences/icml-2026/cards/0701-0800.md#cho26a-inference) · TAG: Tangential Amplifying Guidance for Hallucination-Resistant Sampling
- [扩散注意力的反对称分量调节](../conferences/icml-2026/cards/0701-0800.md#cho26d-inference) · Balancing Fidelity and Diversity in Diffusion Models via Symmetric Attention Decomposition: Hopfield Perspective
- [扩散负引导的阈值投影](../conferences/icml-2026/cards/0701-0800.md#choi26m-inference) · Concept Removal Guidance: Evidence-Calibrated Negative Guidance for Safe Diffusion Sampling
- [扩散 Transformer 激活稀疏推理](../conferences/icml-2026/cards/0701-0800.md#cong26a-inference) · RT-Lynx: Putting GEMM Sparsity in the Right Place for Diffusion Models
- [场景图粒子滤波定位](../conferences/icml-2026/cards/0801-0900.md#damblon26a-inference) · SG2Loc: Sequential Visual Localization on 3D Scene Graphs
- [六维位姿跟踪的漂移重定位](../conferences/icml-2026/cards/0801-0900.md#deng26a-inference) · STORM: Segment, Track, and Object Re-Localization from a Single Image
- [多概念遗忘的掩码合并](../conferences/icml-2026/cards/0801-0900.md#deng26i-inference) · Forget-It-All: Multi-Concept Machine Unlearning via Concept-Aware Neuron Masking
- [整流流反演的球面校正](../conferences/icml-2026/cards/0901-1000.md#duan26d-inference) · SlerpFlow: Spherical Trajectory Correction for Rectified Flow Inversion
- [带噪训练数据的扩散采样修正](../conferences/icml-2026/cards/1001-1100.md#elbrachter26a-inference) · MAD: Manifold Attracted Diffusion
- [脉冲扩散的膜电位误差反馈](../conferences/icml-2026/cards/1001-1100.md#fang26n-inference) · Trajectory-Aware Spiking DiTs Conversion via Membrane Potential Error-Feedback
- [异构时间步的整流流批处理](../conferences/icml-2026/cards/1001-1100.md#fang26z-inference) · StreamFlow: Theory, Algorithm, and Implementation for High-Efficiency Rectified Flow Generation
- [长视频篡改的边界感知定位](../conferences/icml-2026/cards/1101-1200.md#feng26g-inference) · Explainable Forensics of Manipulated Segments in Untrimmed Long Videos
- [增量域预测的能量距离加权](../conferences/icml-2026/cards/1101-1200.md#feng26r-inference) · HEDP: A Hybrid Energy-Distance Prompt-based Framework for Domain Incremental Learning
- [单图三维生成的分量差异缓存](../conferences/icml-2026/cards/1101-1200.md#feng26t-inference) · Fast-SAM3D: 3Dfy Anything in Images but Faster
- [RGB 到 RAW 的一步潜空间传输](../conferences/icml-2026/cards/1101-1200.md#feng26w-inference) · Bridging RGB and RAW: Single-step Deterministic Flow with Homogeneous Representation Alignment
- [长视频队列的双向一致性引导](../conferences/icml-2026/cards/1101-1200.md#feng26ac-inference) · Enhancing Train-Free Infinite-Frame Generation for Consistent Long Videos
- [低比特少步扩散的调度校准](../conferences/icml-2026/cards/1101-1200.md#frumkin26a-inference) · Q-Sched: Pushing the Boundaries of Few-Step Diffusion Models with Quantization-Aware Scheduling
- [低频几何引导的参考纹理迁移](../conferences/icml-2026/cards/1101-1200.md#fu26o-inference) · Dual Optimal Transport for Multi-Concept Composition: Structure Alignment and Texture Injection in Diffusion Models
- [用图生视频过程纠正人和物的交互编辑](../conferences/icml-2026/cards/1201-1300.md#gao26e-inference) · Taming I2V models for Image HOI Editing: A Cognitive Benchmark and Agentic Self-Correcting Framework
- [粗到细图像词元的前缀搜索](../conferences/icml-2026/cards/1201-1300.md#gao26x-inference) · (1D) Ordered Tokens Enable Efficient Test-Time Search
- [扩散生成的实例数布局控制](../conferences/icml-2026/cards/1301-1400.md#gu26f-inference) · Mitigating Noise-Induced Layout Priors for Object Counting in Diffusion Models
- [三维相对关系链的坐标分解](../conferences/icml-2026/cards/1301-1400.md#gu26m-inference) · R$^3$L: Reasoning 3D Layouts from Relative Spatial Relations
- [按分类间隔自适应温度校准](../conferences/icml-2026/cards/1301-1400.md#guo26s-inference) · Sample Margin-Aware Recalibration of Temperature Scaling
- [多扩散模型的公平区域分工](../conferences/icml-2026/cards/1401-1500.md#gupta26a-inference) · Divide-and-Denoise: A Game-Theoretic Method for Fairly Composing Diffusion Models
- [用两步视频生成约束后续运动相位](../conferences/icml-2026/cards/1401-1500.md#han26l-inference) · Physics in 2-Steps: Locking Motion Priors Before Visual Refinement Erases Them
- [蒸馏全注意力的块级结构](../conferences/icml-2026/cards/1401-1500.md#han26y-inference) · Veda: Scalable Video Diffusion via Distilled Sparse Attention
- [以一步随机后验映射并行估计生成价值](../conferences/icml-2026/cards/1501-1600.md#holderrieth26a-inference) · Diamond Maps: Efficient Reward Alignment via Stochastic Flow Maps
- [重排视频词元再分层选择稀疏块](../conferences/icml-2026/cards/1601-1700.md#hu26p-inference) · DFSAttn: Dynamic Fine-grained Sparse Attention for Efficient Video Generation
- [用少量上下文样本低秩校正扩散缓存](../conferences/icml-2026/cards/1601-1700.md#huang26f-inference) · LearniBridge: Learnable Calibration of Feature Caching for Diffusion Models Acceleration
- [利用流映射预测终点并施加奖励引导](../conferences/icml-2026/cards/1701-1800.md#huang26ae-inference) · How to Guide Your Flow: Few-Step Alignment via Flow Map Reward Guidance
- [按零样本置信度维护测试时类原型](../conferences/icml-2026/cards/1701-1800.md#huang26cc-inference) · Prototype-Based Test-Time Adaptation of Vision-Language Models
- [将逆问题先验修正限制在测量梯度的正交方向](../conferences/icml-2026/cards/1801-1900.md#hyoseok26a-inference) · Measurement-Consistent Langevin Corrector for Stabilizing Latent Diffusion Inverse Problem Solvers
- [随去噪阶段伸缩高分辨率位置编码](../conferences/icml-2026/cards/1801-1900.md#issachar26a-inference) · DyPE: Dynamic Position Extrapolation for Ultra High Resolution Diffusion
- [由视频生成器自校正高不确定区域](../conferences/icml-2026/cards/1801-1900.md#jang26d-inference) · Self-Refining Video Sampling
- [按局部度量预条件扩散引导](../conferences/icml-2026/cards/1801-1900.md#jia26g-inference) · Manifold-Optimal Guidance: A Unified Riemannian Control View of Diffusion Guidance
- [把去噪器评估挪到估计的目标端点](../conferences/icml-2026/cards/1901-2000.md#jiao26e-inference) · Are First-Order Diffusion Samplers Really Slower? A Fast Forward-Value Approach

<a id="by-nlp"></a>

### 自然语言处理

- [排序与检索](../conferences/icml-2026/cards/0001-0100.md#agrawal26d-inference) · BlitzRank: Principled Zero-shot Ranking Agents with Tournament Graphs
- [文本水印](../conferences/icml-2026/cards/0001-0100.md#ai26b-inference) · PASA: A Principled Embedding-Space Watermarking Approach for LLM-Generated Text under Semantic-Invariant Attacks
- [句子级水印](../conferences/icml-2026/cards/0001-0100.md#an26a-inference) · IPMark: A Sentence-Level Watermark for LLMs with Hierarchical Personalization and Efficient Detection
- [全双工语音的异步检索](../conferences/icml-2026/cards/0701-0800.md#chien26b-inference) · MoshiRAG: Asynchronous Knowledge Retrieval for Full-Duplex Speech Language Models
- [语音情感的稀疏特征干预](../conferences/icml-2026/cards/0901-1000.md#du26i-inference) · Sparse Autoencoders for Interpretable Emotion Control in Text-to-Speech
- [稀疏编码的多向量倒排检索](../conferences/icml-2026/cards/1301-1400.md#guo26x-inference) · No More K-means: Single-Stage Sparse Coding for Efficient Multi-Vector Retrieval
- [把经过正确性验证的查询扩展逐项写回检索键](../conferences/icml-2026/cards/1601-1700.md#hu26ac-inference) · RAG without Forgetting: Continual Query-Infused Key Memory
- [把晚交互打分蒸馏成可索引相似度](../conferences/icml-2026/cards/1801-1900.md#jaasaari26a-inference) · LEMUR: Learned Multi-Vector Retrieval
- [用词元后缀路径维护流式 BPE 前沿](../conferences/icml-2026/cards/1901-2000.md#jiang26l-inference) · Incremental BPE Tokenization
- [把集合奖励编入扩散检索监督](../conferences/icml-2026/cards/1901-2000.md#jiang26aa-inference) · Efficient, Property-Aligned Fan-Out Retrieval via RL-Compiled Diffusion
- [对话记忆按话题检索、修订和写回](../conferences/icml-2026/cards/2001-2100.md#jung26e-inference) · Context-Driven Incremental Compression for Multi-Turn Dialogue Generation

<a id="by-reinforcement-learning"></a>

### 强化学习

- [强化学习提前退出](../conferences/icml-2026/cards/0301-0400.md#brosseit26a-inference) · Mind the Budget: Accelerating Deep Reinforcement Learning using Constrained Early Exit Neural Networks
- [模型强化学习搜索](../conferences/icml-2026/cards/0401-0500.md#chang26a-inference) · The Surprising Difficulty of Search in Model-Based Reinforcement Learning
- [离线竞价的候选生成与价值筛选](../conferences/icml-2026/cards/0701-0800.md#cui26h-inference) · DRIVE: Distributional and Retrieval-Augmented Bidding with Value Evaluation
- [空域避碰策略的运动学约束](../conferences/icml-2026/cards/1301-1400.md#gu26a-inference) · SARL: Structure-Aligned Reinforcement Learning for Bridging the Perception-Action Gap in Airspace
- [为离线控制检索可达高回报子目标](../conferences/icml-2026/cards/1301-1400.md#guo26r-inference) · RAD: Retrieval High-quality Demonstrations to Enhance Decision-making
- [用先验扩树后从叶向根统一重估](../conferences/icml-2026/cards/1601-1700.md#howard26a-inference) · Recursive Monte-Carlo Tree Search

<a id="by-robotics"></a>

### 机器人学

- [具身 Agent 感知](../conferences/icml-2026/cards/0001-0100.md#aissi26a-inference) · PRISM: Perception Reasoning Interleaved for Sequential Decision Making.
- [扩散预测控制](../conferences/icml-2026/cards/0201-0300.md#balim26a-inference) · Model-Based Diffusion Sampling for Predictive Control in Offline Decision Making
- [压缩空间运动规划](../conferences/icml-2026/cards/0201-0300.md#beyer26a-inference) · Motion Planning in Compressed Representation Spaces
- [移动操作站位](../conferences/icml-2026/cards/0401-0500.md#chai26a-inference) · N2M: Bridging Navigation and Manipulation by Learning Pose Preference from Rollout
- [概率场景图导航](../conferences/icml-2026/cards/0401-0500.md#chen26i-inference) · PSG-Nav: Probabilistic Scene Graph Navigation via Multiverse Decision Making
- [长程机器人轨迹采样](../conferences/icml-2026/cards/0501-0600.md#chen26co-inference) · Rethinking Instruction Drift as a Sampling Error: SNR-Aware Power Distributions for Long-Horizon Robotic Planning
- [多智能体协作的反事实规划](../conferences/icml-2026/cards/0701-0800.md#chi26b-inference) · EvoCF: Multi-Agent Collaboration via Agentic Memory-Driven Evolutionary Counterfactual Planning
- [VLA 不确定性调节感知与动作](../conferences/icml-2026/cards/0701-0800.md#choi26a-inference) · SCALE: Self-uncertainty Conditioned Adaptive Looking and Execution for Vision-Language-Action Models
- [机器人技能代码的局部重绑定](../conferences/icml-2026/cards/0701-0800.md#choi26c-inference) · Efficient Skill Grounding via Code Refactoring with Small Language Models
- [函数级 KV 缓存拼接与修补](../conferences/icml-2026/cards/0701-0800.md#chun26a-inference) · Functional Cache Grafting: Robust and Rapid Code-Policy Synthesis for Embodied Agents
- [导航中的熵驱动推理](../conferences/icml-2026/cards/0901-1000.md#ding26r-inference) · AdaNav: Adaptive Reasoning with Uncertainty for Vision-Language Navigation
- [视觉动作模型的流式分区缓存](../conferences/icml-2026/cards/1301-1400.md#guo26l-inference) · Reflex: Real-Time Vision-Language-Action Control through Streaming Inference
- [用未来去噪路径的终局成本引导当前步](../conferences/icml-2026/cards/1501-1600.md#hoshino26a-inference) · Training-Free Guided Diffusion for Planning: A Unified Framework via Doob’s h-Transform with Safety Guarantees
- [把过往测试时适配保存为可插值提示](../conferences/icml-2026/cards/1601-1700.md#hu26w-inference) · Turning Adaptation into Assets: Cross-Domain Bridging for Online Vision-Language Navigation
- [按环境变化异步更新动作模型通道稀疏度](../conferences/icml-2026/cards/1601-1700.md#huang26h-inference) · EcoVLA: Environment-Aware Adaptive Pruning with Interleaved Inference Orchestration for Vision-Language-Action Models
- [在生成时间加入轨迹约束控制](../conferences/icml-2026/cards/1701-1800.md#huang26t-inference) · SAD-Flower: Flow Matching for Safe, Admissible, and Dynamically Consistent Planning
- [将部署故障校正放进受限的局部残差](../conferences/icml-2026/cards/1801-1900.md#jayasinghe26a-inference) · Cerebellar-Inspired Residual Control for Fault Recovery: From Inference-Time Adaptation to Structural Consolidation
- [按当前观察预测整条去噪剪枝图](../conferences/icml-2026/cards/1801-1900.md#ji26o-inference) · Sparse ActionGen: Accelerating Diffusion Policy with Real-time Pruning
- [逐级缩小符号规划范围并验证关键规则](../conferences/icml-2026/cards/1901-2000.md#jiang26av-inference) · DecoVer: A Decompose-and-Verify Neuro-Symbolic Framework for Embodied Task Planning with BC+

<a id="by-multimodal"></a>

### 多模态学习

- [视觉语言检索](../conferences/icml-2026/cards/0001-0100.md#alshehri26a-inference) · Similarity Is Not Logic: Factored Inference for Dual-Encoder Vision-Language Models
- [流式语音工具调用](../conferences/icml-2026/cards/0101-0200.md#arora26a-inference) · Stream RAG: Instant and Accurate Spoken Dialogue Systems with Streaming Tool Usage
- [视觉推理预算](../conferences/icml-2026/cards/0101-0200.md#avogaro26a-inference) · SPARC: Separating Perception And Reasoning Circuits for Test-time Scaling of VLMs
- [文本到图像生成](../conferences/icml-2026/cards/0101-0200.md#baek26c-inference) · Diagnosing and Correcting Concept Omission in Multimodal Diffusion Transformers
- [扩散对抗净化](../conferences/icml-2026/cards/0101-0200.md#bai26b-inference) · Two Modalities Are Better Than One: Efficient Adversarial Purification via Multimodal Diffusion Models
- [三维生成引导](../conferences/icml-2026/cards/0101-0200.md#bai26d-inference) · Let Language Constrain Geometry: Vision–Language Models as Semantic and Spatial Critics for 3D Generation
- [视觉语言推理控制](../conferences/icml-2026/cards/0201-0300.md#bi26d-inference) · Does Reasoning Improve Seeing? Understanding When Vision-Language Models Benefit from Thinking
- [多模态上下文记忆](../conferences/icml-2026/cards/0401-0500.md#chen26m-inference) · Task-Aware Structured Memory for Dynamic Multi-modal In-Context Learning
- [教学视频布局修正](../conferences/icml-2026/cards/0501-0600.md#chen26bx-inference) · Code2Video: A Code-centric Paradigm for Educational Video Creation
- [注意力层对比解码](../conferences/icml-2026/cards/0501-0600.md#chen26dx-inference) · Beyond Logits: Coherent Hallucination Mitigation via Attention Contrastive Decoding
- [双编码器视觉幻觉校正](../conferences/icml-2026/cards/0501-0600.md#chen26dz-inference) · Beyond Blind Noising: Disentangled Visual Rectification for Hallucination Mitigation in MLLMs
- [图像生成的潜空间推理调度](../conferences/icml-2026/cards/0601-0700.md#chen26fv-inference) · Show, Don’t Tell: Morphing Latent Reasoning into Image Generation
- [视觉语言模型注意力通路门控](../conferences/icml-2026/cards/0601-0700.md#cheng26d-inference) · Mitigating Hallucinations in Large Vision-Language Models via Causal Route Gating
- [视觉词元删减后的注意力校准](../conferences/icml-2026/cards/0701-0800.md#cho26b-inference) · Improving Visual Token Reduction via Rectifying Distortions for Efficient Multimodal LLM Inference
- [超高分遥感词元分区压缩](../conferences/icml-2026/cards/0801-0900.md#dang26a-inference) · UHR-BAT: Budget-Aware Token Compression Vision-Language model for Ultra-High-Resolution Remote Sensing
- [多模态文档问答的内容图与规划图](../conferences/icml-2026/cards/0901-1000.md#du26k-inference) · $G^2$-Reader: Dual Evolving Graphs for Multimodal Document QA
- [稀疏视频帧的语义轨迹插值](../conferences/icml-2026/cards/1001-1100.md#fang26c-inference) · SLAP: The Semantic Least Action Principle for Variational Video-Language Modeling
- [世界模型缓存的曲率漂移判据](../conferences/icml-2026/cards/1101-1200.md#feng26d-inference) · WorldCache: Accelerating World Models for Free via Heterogeneous Token Caching
- [视频问答的结构化记忆与核验](../conferences/icml-2026/cards/1101-1200.md#forouzandeh26a-inference) · LINGUA: Bridging the Grounding Gap in VideoQA via Typed Memory and Belief-State Reasoning
- [视觉关系的函数向量干预](../conferences/icml-2026/cards/1101-1200.md#fu26e-inference) · Multimodal Function Vectors for Visual Relations
- [移动端智能体的流程充分性判断](../conferences/icml-2026/cards/1101-1200.md#fu26m-inference) · Hierarchical Procedural Meta-Reasoning for Generalizable Multimodal Agents
- [视觉词元压缩的平坦度路由](../conferences/icml-2026/cards/1201-1300.md#gao26r-inference) · AD-BTS: Adaptive Dual-Branch Token Sparsification via Spatial Information Density
- [安全阈值触发的早期推理纠偏](../conferences/icml-2026/cards/1201-1300.md#ghosal26a-inference) · Safety Recovery in Reasoning Models Is Only a Few Early Steering Steps Away
- [文本反事实下的时序预测归因](../conferences/icml-2026/cards/1301-1400.md#gu26r-inference) · What if Tomorrow is the World Cup Final? Counterfactual Time Series Forecasting with Textual Conditions
- [异常检测的跨模态重建替换](../conferences/icml-2026/cards/1401-1500.md#guo26ai-inference) · Remove the Ambiguity: Few-shot Multimodal Anomaly Detection Using Crossmodal Feature Replacer
- [注意力引导的测试时提示适配](../conferences/icml-2026/cards/1401-1500.md#hai26a-inference) · Towards Fine-Grained Robustness: Attention-Guided Test-Time Prompt Tuning for Vision-Language Models
- [用不同信号分别判断视觉迟进与早退](../conferences/icml-2026/cards/1401-1500.md#hartman26a-inference) · Skip-It? Theoretical Conditions for Layer Skipping in Vision–Language Models
- [用组内局部密度校正零样本相似度](../conferences/icml-2026/cards/1401-1500.md#hasanebrahimi26a-inference) · Density-Aware Translation of Spurious Correlations in Zero-Shot VLMs
- [按层刷新视觉缓存并用相邻帧降低重算成本](../conferences/icml-2026/cards/1401-1500.md#he26c-inference) · VidLaDA: Bidirectional Diffusion Large Language Models for Efficient Video Understanding
- [以双模型概率一致性接入单步视觉草稿](../conferences/icml-2026/cards/1401-1500.md#he26g-inference) · Self-Prophetic Decoding to Unlock Visual Search in LVLMs
- [在解码时削弱掩码先验并调整位置频率](../conferences/icml-2026/cards/1501-1600.md#hong26k-inference) · Mitigating Mask Prior Drift and Positional Attention Collapse in Large Diffusion Vision-Language Models
- [先推理次级运动，再按置信度调节轨迹引导](../conferences/icml-2026/cards/1601-1700.md#hsin-ying26a-inference) · MotiMotion: Motion-Controlled Video Generation with Visual Reasoning
- [为各注意力头保底，再按熵分配弹性缓存](../conferences/icml-2026/cards/1601-1700.md#hu26ab-inference) · EAKV: An Entropy-Driven Adaptive KV Compression Framework for Long Video Understanding
- [并行准备草稿和目标回退，用证据比率决定提交](../conferences/icml-2026/cards/1601-1700.md#hu26ai-inference) · DREAM-R: Multimodal Speculative Reasoning with RL-Based Refined Drafting, Precise Verification, and Fully Parallel Execution
- [用测试流的软预测将文本原型校准到视觉空间](../conferences/icml-2026/cards/1601-1700.md#hu26aq-inference) · Respecting Modality Gap in Post-hoc Out-of-distribution Detection with Pre-trained Vision-Language Models
- [以实体名称绑定视觉检索](../conferences/icml-2026/cards/1601-1700.md#hu26ay-inference) · EntRAG: Entity-Centric Retrieval-Augmented Generation for Knowledge-based Visual Question Answering
- [按局部刚度自适应扩散求解的时间带宽](../conferences/icml-2026/cards/1701-1800.md#huang26ad-inference) · Robust Parallel Diffusion Sampling via Dynamic Jacobian Bandwidth
- [向先验动态收缩低置信类别的测试时估计](../conferences/icml-2026/cards/1701-1800.md#huang26ag-inference) · Von Mises-Fisher Mixture Model with Dynamic Shrinkage for Realistic Test-Time Transduction
- [让流式生成随音频变化调节历史依赖](../conferences/icml-2026/cards/1801-1900.md#ji26h-inference) · DiscoForcing: A Unified Framework for Real-Time Audio-Driven Character Control with Diffusion Forcing
- [在适配与预测时用同一视图集成](../conferences/icml-2026/cards/1901-2000.md#jiang26ac-inference) · USE: A Unified Self-Ensembling Framework for Test-Time Prompt Tuning
- [在视觉代理记忆里分开局部经验与任务技能](../conferences/icml-2026/cards/1901-2000.md#jiang26aq-inference) · XSkill: Continual Learning from Experience and Skills in Multimodal Agents

<a id="by-ml-foundations"></a>

### 机器学习基础与统计

- [未归一化分布采样](../conferences/icml-2026/cards/0201-0300.md#blessing26a-inference) · Bridge Matching Sampler: Scalable Sampling via Generalized Fixed-Point Diffusion Matching
- [生成式模型遗忘](../conferences/icml-2026/cards/0201-0300.md#block26a-inference) · Temper-Then-Tilt: Principled Unlearning for Generative Models through Tempering and Classifier Guidance
- [条件扩散采样](../conferences/icml-2026/cards/0401-0500.md#castro-maci-as26a-inference) · Conditional Diffusion Sampling
- [贝叶斯逆问题采样](../conferences/icml-2026/cards/0401-0500.md#chen26f-inference) · Proximal-IMH: Proximal Posterior Proposals for Independent Metropolis–Hastings with Approximate Operators
- [分块扩散注意力缓存](../conferences/icml-2026/cards/0401-0500.md#chen26g-inference) · FlashBlock: Attention Caching for Efficient Long-Context Block Diffusion
- [摊销采样器与粒子采样互训](../conferences/icml-2026/cards/0701-0800.md#choi26l-inference) · Reinforced Sequential Monte Carlo for Amortised Sampling
- [动态集成的路径聚合与早退](../conferences/icml-2026/cards/0701-0800.md#colaco26a-inference) · Unifying Stacking and Cascading for Efficient Ensemble Inference
- [离散扩散的免训练 logit 引导](../conferences/icml-2026/cards/0901-1000.md#dou26a-inference) · Plug-and-Play Guidance for Discrete Diffusion Models via Gradient-Informed Logit Correction
- [离散神经采样的历史势垒调节](../conferences/icml-2026/cards/0901-1000.md#du26h-inference) · MetaDNS: Enhancing Exploration in Discrete Neural Samplers via Well-Tempered Metadynamics
- [无目标观测站点的时序扩散重建](../conferences/icml-2026/cards/1001-1100.md#fan26d-inference) · ZeroDiff: Zero-Shot Time Series Reconstruction via Informed-Prior Diffusion
- [离散流的重参数化强度外推](../conferences/icml-2026/cards/1101-1200.md#fu26d-inference) · A Time-Reparameterized Cumulative Intensity Extrapolation Sampler for Discrete Flow Matching
- [最小扰动的仿射概念引导](../conferences/icml-2026/cards/1101-1200.md#gaintseva26a-inference) · MidSteer: Optimal Affine Framework for Steering Generative Models
- [用低阶配点做高精度扩散采样](../conferences/icml-2026/cards/1201-1300.md#gatmiry26a-inference) · High-accuracy and dimension-free sampling with diffusions
- [扩散后验引导的似然边缘化](../conferences/icml-2026/cards/1201-1300.md#geyfman26a-inference) · Calibrated Test-Time Guidance for Bayesian Inference
- [生成式规划的按深度分桶搜索](../conferences/icml-2026/cards/1201-1300.md#gieselmann26a-inference) · Efficient Test-time Inference for Generative Planning Models with OCL Search
- [量化置信度的样本自适应缩放](../conferences/icml-2026/cards/1301-1400.md#gu26j-inference) · Precision-Induced Miscalibration: Understanding and Correcting Confidence Distortion in Quantized Neural Networks
- [联邦测试时的原型拓扑扩散](../conferences/icml-2026/cards/1301-1400.md#guo26m-inference) · FedPAT: Federated Test-Time Adaptation via Prototype Affinity Topology
- [先定位知识组件，再生成最小范围的纠正](../conferences/icml-2026/cards/1501-1600.md#hiranaka26a-inference) · Fix the Mind, Not the Move: Interpretable AI Assistance via Knowledge-Gap Localization
- [以同一样本多次受扰后的去噪偏差衡量异常](../conferences/icml-2026/cards/1501-1600.md#hirth26a-inference) · Denoising without Diffusion: Fixed-Noise Denoiser Anomaly Detection in Tabular Data

<a id="by-graph-and-recommendation"></a>

### 图学习与推荐

- [图模型测试时适应](../conferences/icml-2026/cards/0001-0100.md#ai26c-inference) · PromptDyG: Test-Time Prompt Adaptation on Dynamic Graphs
- [在线推荐校准](../conferences/icml-2026/cards/0201-0300.md#bisht26b-inference) · CARE: Adaptive Calibration for Reliable Recommendations
- [图注意力的 I/O 融合优化](../conferences/icml-2026/cards/1101-1200.md#fomina26a-inference) · On Efficient Scaling of GNNs via IO-Aware Layers Implementations
- [知识图多跳搜索的语义补边](../conferences/icml-2026/cards/1201-1300.md#gao26t-inference) · Beyond Explicit Edges: Robust Reasoning over Noisy and Sparse Knowledge Graphs
- [按需探查图拓扑的工具推理](../conferences/icml-2026/cards/1301-1400.md#guo26t-inference) · GRASP: Graph Reasoning via Agentic Solving and Probing of LLMs
- [冻结图网络的后验不确定性证据](../conferences/icml-2026/cards/1301-1400.md#guo26ac-inference) · X-EviProbe: Post-hoc Parameter-Free Evidential Uncertainty Quantification for Frozen Graph Neural Networks
- [用目标图的有标注和无标注节点适配提示](../conferences/icml-2026/cards/1901-2000.md#jiang26al-inference) · GFMate: Empowering Graph Foundation Models with Test-time Prompt Tuning

<a id="by-scientific-ml"></a>

### 科学机器学习

- [大气生成模型](../conferences/icml-2026/cards/0001-0100.md#aich26a-inference) · WIND: Weather Inverse Diffusion for Zero-Shot Atmospheric Modeling
- [数据同化](../conferences/icml-2026/cards/0001-0100.md#andrae26a-inference) · DAISI: Data Assimilation with Inverse Sampling using Stochastic Interpolants
- [函数空间逆问题](../conferences/icml-2026/cards/0101-0200.md#baker26a-inference) · Supervised Guidance Training for Infinite-Dimensional Diffusion Models
- [质谱到分子生成](../conferences/icml-2026/cards/0301-0400.md#bohde26a-inference) · FRIGID: Scaling Diffusion-Based Molecular Generation from Mass Spectra at Training and Inference Time
- [蛋白结合物设计](../conferences/icml-2026/cards/0301-0400.md#cao26c-inference) · Chamaileon: Cross-Context Binder Design with Contextualized Modeling and Mixed Sampling
- [对接预测梯度反演](../conferences/icml-2026/cards/0501-0600.md#chen26bu-inference) · Towards Docking-oriented De Novo Ligand Design via Gradient Inversion
- [粗粒化玻尔兹曼重要性采样](../conferences/icml-2026/cards/0601-0700.md#chen26gs-inference) · Coarse-Grained Boltzmann Generators
- [流行病模拟器的流图验证](../conferences/icml-2026/cards/0801-0900.md#datta26a-inference) · Agentic Framework for Epidemiological Modeling
- [逆设计流的零锚定置信度](../conferences/icml-2026/cards/0801-0900.md#de-campos26a-inference) · Generative Inverse Design with Abstention via Diagonal Flow Matching
- [重尾扩散桥的肠鸣音分离](../conferences/icml-2026/cards/0901-1000.md#ding26a-inference) · Listening Through the Noise: Cauchy-Driven Diffusion Bridges for Robust Gastrointestinal Auscultation and Clinical Benchmarking
- [谱空间扩散的 PDE 后验引导](../conferences/icml-2026/cards/1101-1200.md#gallon26a-inference) · Physics-Informed Diffusion Models in Spectral Space
- [港口和航路节点条件下的航迹外推](../conferences/icml-2026/cards/1101-1200.md#gan26b-inference) · SKETCH: Semantic Key-Point Conditioning for Long-Horizon Vessel Trajectory Prediction
- [干旱预测的多分辨率残差校正](../conferences/icml-2026/cards/1201-1300.md#gao26p-inference) · Residual-Guided Multi-Resolution Refinement of Foundation Models: A Case Study in Drought Forecasting
- [超大病理切片的动态倍率推理](../conferences/icml-2026/cards/1201-1300.md#ge26b-inference) · Thinking in Scales: Accelerating Gigapixel Pathology Image Analysis via Adaptive Continuous Reasoning
- [稀疏传感条件下的城市风场扩散](../conferences/icml-2026/cards/1201-1300.md#giral26a-inference) · GenDA: Generative Data Assimilation on Complex Urban Areas via Classifier-Free Diffusion Guidance
- [原子势的平滑动态截断](../conferences/icml-2026/cards/1401-1500.md#han26g-inference) · Smooth Dynamic Cutoffs for Machine Learning Interatomic Potentials
- [在共享逆合成搜索图上自适应采样目标权重](../conferences/icml-2026/cards/1401-1500.md#hastedt26a-inference) · From Feasible to Practical: Pareto-Optimal Synthesis Planning
- [保留信道符号来积分连续解码场](../conferences/icml-2026/cards/1501-1600.md#helvits26a-inference) · Score Based Error Correcting Code Decoder
- [把谱峰基序证据带入分段去噪搜索](../conferences/icml-2026/cards/1801-1900.md#jia26e-inference) · MAST: Motif-Augmented Diffusion with Search Tree for Spectroscopic Molecular Structure Elucidation
<!-- classification:end -->
