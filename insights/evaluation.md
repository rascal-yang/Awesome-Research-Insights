# 评测与诊断

[首页](../README.md) · [English](../en/insights/evaluation.md)

基准、评测协议、消融与失效诊断。

<!-- classification:start -->
## 按研究领域浏览

### 大语言模型

- [推理系统评测](../papers/llm.md#abramovich26a-evaluation) · SPEED-Bench: A Unified and Diverse Benchmark for Speculative Decoding
- [表征分析](../papers/llm.md#acevedo26a-evaluation) · Differential syntactic and semantic encoding in LLMs
- [分阶段评测](../papers/llm.md#acharya26a-evaluation) · CauSciBench: Can LLMs Automate Causal Inference in Real-World Scientific Research?
- [一致性训练](../papers/llm.md#africa26a-evaluation) · Consistency Training Can Entrench Misalignment
- [持续记忆评测](../papers/llm.md#ai26e-evaluation) · MemoryBench: A Benchmark for Memory and Continual Learning in LLM Systems
- [Agent 合规评测](../papers/llm.md#aka26a-evaluation) · Evaluating Contextual Illegality: AI Compliance in Corporate Law Scenarios
- [基准饱和](../papers/llm.md#akhtar26a-evaluation) · When AI Benchmarks Plateau: A Systematic Study of Benchmark Saturation
- [提示攻击检测](../papers/llm.md#alshaalan26a-evaluation) · Detecting Fluent Optimization-Based Adversarial Prompts via Sequential Entropy Changes
- [长文本不确定性评测](../papers/llm.md#amit26a-evaluation) · Evaluating LLM Uncertainty in Long-Form Generation Using Deterministic Ground Truth
- [形式化证明评测](../papers/llm.md#ammanamanchi26a-evaluation) · Faults in Our Formal Benchmarking: Dataset Defects and Evaluation Failures in Lean Theorem Proving
- [模型输出尾部风险](../papers/llm.md#angell26a-evaluation) · Estimating Tail Risks in Language Model Output Distributions
- [求解器反馈与 Agent RL](../papers/llm.md#ao26a-evaluation) · ORLoopBench: Solver-in-the-Loop Benchmarks for Self-Correction and Behavioral Rationality in Operations Research
- [归纳头形成](../papers/llm.md#aoyama26a-evaluation) · Predicting the Emergence of Induction Heads in Language Model Pretraining
- [隐性偏差审计](../papers/llm.md#arcuschin26a-evaluation) · Biases in the Blind Spot: Detecting What LLMs Fail to Mention
- [推理忠实性](../papers/llm.md#arcuschin26b-evaluation) · Chain-of-Thought Reasoning In The Wild Is Not Always Faithful
- [Agent 目标表征](../papers/llm.md#arghal26a-evaluation) · A Behavioural and Representational Evaluation of Goal-Directedness in Language Model Agents
- [Agent 执行监控](../papers/llm.md#arike26a-evaluation) · How does information access affect LLM monitors’ ability to detect sabotage?
- [语言模型电路](../papers/llm.md#arora26c-evaluation) · Language Model Circuits Are Sparse in the Neuron Basis
- [LoRA 知识记忆](../papers/llm.md#back26a-evaluation) · Understanding LoRA as Knowledge Memory: An Empirical Analysis
- [LLM 裁判校准](../papers/llm.md#badshah26a-evaluation) · SCOPE: Selective Conformal Optimized Pairwise LLM Judging
- [对齐行为诊断](../papers/llm.md#baek26d-evaluation) · Sycophancy Towards Researchers Drives Performative Misalignment
- [机制可解释性](../papers/llm.md#bair26a-evaluation) · Compressed Sensing for Capability Localization in Large Language Models
- [形式化证明评测](../papers/llm.md#baksys26a-evaluation) · miniF2F-Dafny: LLM-Guided Mathematical Theorem Proving via Auto-Active Verification
- [相关裁判聚合](../papers/llm.md#balasubramanian26a-evaluation) · Dependence-Aware Label Aggregation for LLM-as-a-Judge via Ising Models
- [注意力电路稳定性](../papers/llm.md#bali26a-evaluation) · Quantifying LLM Attention-Head Stability: Implications for Circuit Universality
- [偏好预测](../papers/llm.md#ball26a-evaluation) · Reading Between the Tokens: Improving Preference Predictions through Mechanistic Forecasting
- [Agent 澄清评测](../papers/llm.md#bao26e-evaluation) · DRIFT-BENCH: Diagnosing CoopeRative Breakdowns in LLM Agents under Input Faults via Multi-Turn Interaction
- [训练数据记忆评测](../papers/llm.md#barbero26a-evaluation) · Extracting alignment data in open models
- [人机协作 Agent 评测](../papers/llm.md#barres26a-evaluation) · $τ^2$-Bench: Evaluating Conversational Agents in a Dual-Control Environment
- [逻辑归纳评测](../papers/llm.md#batzoglou26a-evaluation) · INDUCTION: Finite-Structure Concept Synthesis in First-Order Logic
- [推理过程评测](../papers/llm.md#berdoz26b-evaluation) · Reasoning Structure of Large Language Models
- [语言表征几何](../papers/llm.md#bernas26a-evaluation) · Revisiting Anisotropy in Language Transformers: The Geometry of Learning Dynamics
- [长文本事实性诊断](../papers/llm.md#bhardwaj26a-evaluation) · Embedding Trust: Semantic Isotropy Predicts Nonfactuality in Long-Form Text Generation
- [推理自评](../papers/llm.md#bi26e-evaluation) · The Geometry of Reasoning: Self-Evaluation via Layerwise Trajectory Evolution
- [幻觉检测](../papers/llm.md#binkowski26a-evaluation) · Attention Sinks as Internal Signals for Hallucination Detection in Large Language Models
- [基准概念覆盖](../papers/llm.md#bohacek26a-evaluation) · Uncovering Competency Gaps in Large Language Models and Their Benchmarks
- [推理忠实性](../papers/llm.md#boppana26a-evaluation) · Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought
- [多 Agent 行为监控](../papers/llm.md#bridgeford26a-evaluation) · Detecting Perspective Shifts in Multi-Agent Systems
- [事实召回评测](../papers/llm.md#calderon26a-evaluation) · Empty Shelves or Lost Keys? Recall Is the Bottleneck for Parametric Factuality
- [动态调度评测](../papers/llm.md#cao26z-evaluation) · DynaSchedBench: Calibrated Dynamic Scheduling Benchmarks and Observability Paradox in LLM-based Scheduling Agents
- [科学发现 Agent 评测](../papers/llm.md#carlsson26a-evaluation) · SEDRAS: Symbolically Evaluated Deep Research And Science
- [LLM 标注评测](../papers/llm.md#casanova26a-evaluation) · On the Limits of LLM Adaptability: Impact of Model-Internalized Priors on Annotation Task Performance
- [操作步骤评测](../papers/llm.md#chang26e-evaluation) · How2Everything: Mining the Web for How-to Procedures to Evaluate and Improve LLMs
- [稀疏自编码器可解释性](../papers/llm.md#chanin26a-evaluation) · Sparse but Wrong: Incorrect L0 Leads to Incorrect Features in Sparse Autoencoders
- [LLM API 变化检测](../papers/llm.md#chauvin26a-evaluation) · Token-Efficient Change Detection in LLM APIs
- [Agent 因果推断评测](../papers/llm.md#chen26l-evaluation) · CausalGame: Benchmarking Causal Thinking of LLM Agents in Games
- [幻觉逐步定位](../papers/llm.md#chen26n-evaluation) · Mind the Gap: Catching Hallucinations via Evidence Drop on the Reasoning Manifold
- [优化建模 Agent 评测](../papers/llm.md#chen26o-evaluation) · OPT-Engine: Benchmarking the Limits of LLMs in Optimization Modeling via Complexity Scaling
- [长上下文容量评测](../papers/llm.md#chen26q-evaluation) · L-CUBE: Isolating Long-Context Capacity from Knowledge with Controllable Mutual Information Scaling
- [激活干预下的安全评测](../papers/llm.md#chen26x-evaluation) · Adaptive Probe-based Steering for Robust LLM Jailbreaking
- [RLVR 的难学样本](../papers/llm.md#chen26aq-evaluation) · The Unlearnability Phenomenon in RLVR for Language Models
- [机制电路的非唯一性](../papers/llm.md#chen26bb-evaluation) · All Circuits Lead to Rome: Rethinking Functional Anisotropy in Circuit and Sheaf Discovery for LLMs
- [对齐奖励的隐含目标诊断](../papers/llm.md#chen26bg-evaluation) · Discovering Implicit Large Language Model Alignment Objectives
- [欠定问题的假设覆盖](../papers/llm.md#chen26bz-evaluation) · HypoSpace: A Diagnostic Benchmark for Set-Valued Hypothesis Generation under Underdetermination and Sublinear Coverage Bounds
- [交互式科学代码评测](../papers/llm.md#chen26cf-evaluation) · InteractScience: Programmatic and Visually-Grounded Evaluation of Interactive Scientific Demonstration Code Generation
- [可解释注意力头的训练数据归因](../papers/llm.md#chen26cv-evaluation) · Mechanistic Data Attribution: Tracing the Training Origins of Interpretable LLM Units
- [人机协作智能体评测](../papers/llm.md#chen26da-evaluation) · How can we assess human-agent interactions? Case studies in software agent design
- [用逐层预测变化衡量推理投入](../papers/llm.md#chen26di-evaluation) · Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens
- [代码生成的诈骗链接审计](../papers/llm.md#chen26dp-evaluation) · Scam2Prompt: A Scalable Framework for Auditing Malicious Scam Endpoints in Production LLMs
- [工具智能体的用户交互评测](../papers/llm.md#chen26eg-evaluation) · AppWorld-UL: Benchmarking Diverse Agent-User Interactions for Tool-Use
- [分块低比特量化格式比较](../papers/llm.md#chen26fa-evaluation) · INT vs. FP: A Comprehensive Study of Fine-Grained Low-bit Quantization Formats
- [量化感知训练的激活异常值诊断](../papers/llm.md#chen26gl-evaluation) · Scaling Law for Quantization-Aware Training
- [语言模型强化学习的采样预算分配](../papers/llm.md#cheng26n-evaluation) · IsoCompute Playbook: Optimally Scaling Sampling Compute for LLM RL
- [智能体劳务市场的策略诊断](../papers/llm.md#chiu26a-evaluation) · When AI Agents Compete for Jobs: Strategic Capabilities and Economic Dynamics of AI Labour Markets
- [续写分布的语义与机制聚类](../papers/llm.md#cho26g-evaluation) · Shared Semantics, Divergent Mechanisms: Unsupervised Feature Discovery by Aligning Semantics and Mechanisms
- [语言模型评委的潜在质量诊断](../papers/llm.md#choi26n-evaluation) · Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory
- [冻结演化轨迹的反馈归因](../papers/llm.md#chong26b-evaluation) · Towards Feedback-to-Plan Decisions for Self-Evolving LLM Agents in CUDA Kernel Generation
- [注意力输出的有符号贡献](../papers/llm.md#cunningham26a-evaluation) · Contribution Weights: A Geometrical Analysis of Self-Attention Transformers
- [社会影响信号的在线序贯监测](../papers/llm.md#dai26d-evaluation) · Three Years of r/ChatGPT: Societal Impact Evaluations from Social Media Data
- [图路径诊断推理幻觉](../papers/llm.md#dai26k-evaluation) · When Do Hallucinations Arise? A Graph Perspective on the Evolution of Path Reuse and Path Compression
- [持续软件演进的里程碑评测](../papers/llm.md#deng26d-evaluation) · SWE-Milestone: Evaluating AI Agents on Continuous Software Evolution
- [跨文件软件工程的补丁验证](../papers/llm.md#deng26f-evaluation) · SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?
- [歧义搜索的交互必要性检测](../papers/llm.md#deng26h-evaluation) · InteractComp: Evaluating Search Agents With Ambiguous Queries
- [审稿意见的分类校验](../papers/llm.md#deng26j-evaluation) · CoCoReviewBench: A Completeness- and Correctness-Oriented Benchmark for AI Reviewers
- [多模型投票的相关错误诊断](../papers/llm.md#denisov-blanch26a-evaluation) · Truthfulness Does Not Scale Like Reasoning: Why Polling Fails as a Proxy Verifier
- [奖励投机的对照轨迹评测](../papers/llm.md#deshpande26a-evaluation) · Benchmarking Reward Hack Detection in Code Environments via Contrastive Analysis
- [可切换适配器的模型自审计](../papers/llm.md#dietz26a-evaluation) · Split Personality Training: Revealing Latent Knowledge Through Alternate Personalities
- [从空工作区生成 Python 仓库的评测](../papers/llm.md#ding26j-evaluation) · NL2Repo-Bench: Towards Long-Horizon Repository Generation Evaluation of Coding Agents
- [RLVR 训练目标劫持诊断](../papers/llm.md#dong26b-evaluation) · Probing RLVR Training Instability through the Lens of Objective-Level Hacking
- [搜索智能体的沙箱红队评测](../papers/llm.md#dong26c-evaluation) · SafeSearch: Automated Red-Teaming of LLM-Based Search Agents
- [用成对推理比较降低评测方差](../papers/llm.md#dong26o-evaluation) · Evaluating LLMs When They Do Not Know the Answer: Statistical Evaluation of Mathematical Reasoning via Comparative Signals
- [用超额描述长度区分能力诱发与学习](../papers/llm.md#donoway26a-evaluation) · Bits That Count: Quantifying and Predicting Capabilities of Language Models
- [语言模型罕见事件的重要性估计](../papers/llm.md#dorman26a-evaluation) · Rare Event Analysis of Large Language Models
- [多智能体通信协议的受控评测](../papers/llm.md#du26l-evaluation) · ProtocolBench: Which LLM MultiAgent Protocol to Choose?
- [语言不确定性词的正确率校准](../papers/llm.md#duan26b-evaluation) · "very likely" Means "uncertain"? How LLMs Diverge from Humans in Linguistic Uncertainty Quantification
- [可控 2-SAT 结构鲁棒性评测](../papers/llm.md#es-sebbani26a-evaluation) · Evaluating Robustness of Reasoning Models on Parameterized Logical Problems
- [越狱论文到可复现评测模块](../papers/llm.md#fang26y-evaluation) · Jailbreak Foundry: From Papers to Runnable Attacks for Reproducible Benchmarking
- [奖励模型偏差的激活投影](../papers/llm.md#fein26a-evaluation) · One Bias After Another: Mechanistic Reward Shaping and Persistent Biases in Language Reward Models
- [外部技能组合的后门评测](../papers/llm.md#feng26c-evaluation) · SkillTrojan: Backdoor Attacks on Skill-Based Agent Systems
- [推理链的失败步骤比例](../papers/llm.md#feng26e-evaluation) · What Characterizes Effective Reasoning? Revisiting Length, Review, and Structure of CoT
- [关系推理的元数控制评测](../papers/llm.md#fesser26a-evaluation) · Evaluating Relational Reasoning in LLMs with REL
- [注意力奇异向量的特征对齐诊断](../papers/llm.md#franco26a-evaluation) · Singular Vectors of Attention Heads Align with Features
- [代码智能体的迭代锦标赛](../papers/llm.md#fu26a-evaluation) · CATArena: Evaluating Evolutionary Capabilities of Code Agents via Iterative Tournaments

### 计算机视觉

- [视觉推理评测](../papers/computer-vision.md#acuaviva26a-evaluation) · Rethinking Visual Intelligence: Insights from Video Pretraining
- [分割模型诊断](../papers/computer-vision.md#ahmed26a-evaluation) · Med-SegLens: Latent-Level Model Diffing for Interpretable Medical Image Segmentation
- [扩散模型域外检测](../papers/computer-vision.md#alexis26a-evaluation) · GEPC: Group-Equivariant Posterior Consistency for Out-of-Distribution Detection in Diffusion Models
- [深伪防御评测](../papers/computer-vision.md#baek26e-evaluation) · Proactive Defense Benchmark against Deepfake Generation
- [扩散模型概念遗忘](../papers/computer-vision.md#braun26b-evaluation) · Erased but Not Forgotten: How Backdoors Compromise Concept Erasure
- [生成模型后门评测](../papers/computer-vision.md#chen26az-evaluation) · Semantic-level Backdoor Attack against Text-to-Image Diffusion Models
- [人脸数据集内在质量估计](../papers/computer-vision.md#chen26gw-evaluation) · Efficient, Validation-Free Intrinsic Quality Estimation for Large-Scale Face Recognition Datasets
- [视觉表征的组合绑定诊断](../papers/computer-vision.md#chung26a-evaluation) · Global Geometry Is Not Enough for Vision Representations
- [类别遗忘的近邻输出泄漏](../papers/computer-vision.md#ebrahimpour-boroojeny26a-evaluation) · Unlearning Isn’t Forgetting: Revealing Hidden Leakage in Class Unlearning Evaluations
- [概念感知的显著性图](../papers/computer-vision.md#elisha26a-evaluation) · ConEx: Human-Interpretable Saliency Maps via Concept-Aware Attribution
- [交互世界模型的统一动作编码](../papers/computer-vision.md#fang26l-evaluation) · iWorld-Bench: A Benchmark for Interactive World Models with a Unified Action Generation Framework

### 自然语言处理

- [分词器评测](../papers/nlp.md#altintas26a-evaluation) · TokSuite: Measuring the Impact of Tokenizer Choice on Language Model Behavior
- [音频表征评测](../papers/nlp.md#basha26a-evaluation) · VocSim A Training-free Benchmark for Zero-shot Content Identity in Single-source Audio
- [检索增强生成安全评测](../papers/nlp.md#chen26av-evaluation) · Eyes-on-Me: Scalable RAG Poisoning through Transferable Attention-Steering Attractors
- [生成文本的惊异度转移检测](../papers/nlp.md#chen26bf-evaluation) · Black-Box Detection of LLM-Generated Text Using Generalized Jensen Shannon Divergence
- [音频深伪检测的多样性压力测试](../papers/nlp.md#dehdashtian26a-evaluation) · FoeGlass: Simple In-Context Learning Is Enough for Red Teaming Audio Deepfake Detectors
- [同行评审来源的声明级检测](../papers/nlp.md#duarte26a-evaluation) · Sem-Detect: Semantic Level Detection of AI Generated Peer-Reviews
- [重写式事后文本水印评测](../papers/nlp.md#fernandez26b-evaluation) · How Good is Post-Hoc Watermarking With Language Model Rephrasing?

### 强化学习

- [防御强化学习奖励](../papers/reinforcement-learning.md#bates26a-evaluation) · Beyond Rewards in RL for Cyber Defence
- [像素策略的单因素泛化评测](../papers/reinforcement-learning.md#cherepanov26a-evaluation) · KAGE-Bench: Fast Known-Axis Visual Generalization Evaluation for Reinforcement Learning

### 机器人学

- [机器人轨迹安全](../papers/robotics.md#bai26e-evaluation) · SafeLab: An Interactive High-Fidelity Benchmark for Embodied Safety in Scientific Robotics
- [柔性线状物体操作](../papers/robotics.md#cao26w-evaluation) · DLO-Lab: Benchmarking Deformable Linear Object Manipulations with Differentiable Physics
- [长程操作记忆的分项评测](../papers/robotics.md#dai26c-evaluation) · RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies
- [机器人生成视频的物理与任务评测](../papers/robotics.md#deng26r-evaluation) · Rethinking Video Generation Model for the Embodied World
- [动作块增量的基准姿态](../papers/robotics.md#feng26ab-evaluation) · Demystifying Action Space Design for Robotic Manipulation Policies

### 多模态学习

- [视觉语言安全评测](../papers/multimodal.md#azulay26a-evaluation) · Jailbreaking Vision-Language Models Through the Visual Modality
- [文档 Agent 评测](../papers/multimodal.md#borchmann26a-evaluation) · Strategic Navigation or Stochastic Search? How Agents and Humans Reason Over Document Collections
- [视觉语言模型量化](../papers/multimodal.md#bouguerra26a-evaluation) · Less Precise Can Be More Reliable: A Systematic Evaluation of Quantization’s Impact on VLMs Beyond Accuracy
- [图像感知评测](../papers/multimodal.md#cao26i-evaluation) · UniPercept: Towards Unified Perceptual-Level Image Understanding across Aesthetics, Quality, Structure, and Texture
- [音视频生成评测](../papers/multimodal.md#cao26v-evaluation) · T2AV-Compass: Towards Unified Evaluation for Text-to-Audio-Video Generation
- [音视频未来预测评测](../papers/multimodal.md#chen26ad-evaluation) · FutureOmni: Evaluating Future Forecasting from Omni-Modal Context for Multimodal LLMs
- [误导视觉线索的配对评测](../papers/multimodal.md#chen26dh-evaluation) · MVI-Bench: A Comprehensive Benchmark for Evaluating Robustness to Misleading Visual Inputs in LVLMs
- [基于物体提示的幻觉检测](../papers/multimodal.md#chen26dl-evaluation) · DOUBT: Decoupled Object-level Understanding and Bridging via vMF-based Trustworthiness for Hallucination Detection in MLLMs
- [文生图工具链越狱评测](../papers/multimodal.md#chen26en-evaluation) · OrchJail: Jailbreaking Tool-Calling Text-to-Image Agents by Orchestration-Guided Fuzzing
- [基础视觉推理诊断](../papers/multimodal.md#chen26fj-evaluation) · BabyVision: Visual Reasoning Beyond Language
- [文生图人口属性多样性评测](../papers/multimodal.md#chen26gz-evaluation) · HoloFair: Unified T2I Fairness Evaluation and Fair-GRPO Debiasing
- [视觉语言模型的选择偏好审计](../papers/multimodal.md#cherep26a-evaluation) · Visual Persuasion: What Influences Decisions of Vision-Language Models?
- [游戏开发智能体的运行时反馈](../papers/multimodal.md#chi26a-evaluation) · GameDevBench: Evaluating Agentic Capabilities Through Game Development
- [视觉实体追踪的感知与推理解耦](../papers/multimodal.md#cohen26d-evaluation) · MET-Bench: Multimodal Entity Tracking for Evaluating the Limitations of Vision-Language and Reasoning Models
- [视觉历史中的跨图检索评测](../papers/multimodal.md#deng26g-evaluation) · DeepImageSearch: Benchmarking Multimodal Agents for Context-Aware Image Retrieval in Visual Histories
- [科学视频推理的视觉依赖校验](../papers/multimodal.md#deng26w-evaluation) · SciVideoBench: Benchmarking Scientific Video Reasoning in Large Multimodal Models
- [语义近邻校准标注判错](../papers/multimodal.md#di26b-evaluation) · Detecting Errors in AI-Generated Annotations: When and Why Semantic Neighbors Help
- [由图像主动决定开放网页检索](../papers/multimodal.md#fan26a-evaluation) · NAVIGATE: Evaluating Visual-Guided Search Decision-Making on the Open Web
- [用图像证据约束欺骗辩论](../papers/multimodal.md#fang26f-evaluation) · Debate with Images: Detecting Deceptive Behaviors in Multimodal Large Language Models
- [音频安全评测的稀疏梯度诊断](../papers/multimodal.md#fang26r-evaluation) · Sparse Tokens Suffice: Jailbreaking Audio Language Models via Token-Aware Gradient Optimization
- [文本条件下的音视频信息分解](../papers/multimodal.md#fang26x-evaluation) · Towards Understanding Modality Interaction in Multimodal Language Models via Partial Information Decomposition
- [区分旧事实更新和未知事实学习](../papers/multimodal.md#fu26c-evaluation) · MMKU-Bench: A Multimodal Update Benchmark for Diverse Visual Knowledge

### 机器学习基础与统计

- [交互式评测](../papers/ml-foundations.md#agrawal26b-evaluation) · A Benchmark and Framework for Evaluating Next Action Predictions in Spreadsheets
- [表征相似性](../papers/ml-foundations.md#almudevar26a-evaluation) · Bridging Functional and Representational Similarity via Usable Information
- [机制可解释性](../papers/ml-foundations.md#anani26a-evaluation) · Certified Circuits: Stability Guarantees for Mechanistic Circuits
- [参数扰动稳健性](../papers/ml-foundations.md#arpit26a-evaluation) · TPV: Parameter Perturbations Through the Lens of Test Prediction Variance
- [模型拼接评测](../papers/ml-foundations.md#athanasiadis26a-evaluation) · Grounding Functional Similarity by Invariance-Aware Model Stitching
- [影响函数](../papers/ml-foundations.md#bado26a-evaluation) · Clustered Influence Functions
- [表格基础模型](../papers/ml-foundations.md#balef26a-evaluation) · Is One Layer Enough? Understanding Inference Dynamics in Tabular Foundation Models
- [时序基础模型压缩](../papers/ml-foundations.md#bao26c-evaluation) · Universal Redundancies in Time Series Foundation Models
- [可验证模型解释](../papers/ml-foundations.md#boetius26a-evaluation) · Verified SHAP: Provable Bounds for Exact Shapley Values of Neural Networks
- [人评聚合](../papers/ml-foundations.md#bonagiri26a-evaluation) · STABLEVAL: Disagreement-Aware and Stable Evaluation of AI Systems
- [共形覆盖诊断](../papers/ml-foundations.md#braun26c-evaluation) · Conditional Coverage Diagnostics for Conformal Prediction
- [榜单评测前的统一微调](../papers/ml-foundations.md#chen26gf-evaluation) · Leaderboard Incentives: Model Rankings under Strategic Post-Training
- [用合成记忆任务诊断可塑性](../papers/ml-foundations.md#cheng26i-evaluation) · Local Redundancy: An Information-Theoretic Measure of Plasticity from Synthetic Memorization
- [元胞自动机可学习性的频谱诊断](../papers/ml-foundations.md#disselhoff26a-evaluation) · Probing the Inductive Bias of Neural Networks through Learning Random Cellular Automata
- [按数据结构难度诊断聚类](../papers/ml-foundations.md#durani26a-evaluation) · CHB: A Diagnostic Toolkit for Hardness-Aware Clustering Evaluation
- [序列状态跟踪的跨长度共享诊断](../papers/ml-foundations.md#ebrahimi26a-evaluation) · On the "Induction Bias" in Sequence Models
- [沿 AdamW 训练路径联合归因](../papers/ml-foundations.md#eichin26a-evaluation) · ExPLAIND: Unifying Model, Data, and Training Attribution to Study Model Behavior
- [时序预测的分频可预测性诊断](../papers/ml-foundations.md#feng26u-evaluation) · Beyond Model Ranking: Predictability-Aligned Evaluation for Time Series Forecasting
- [评分模型的架构各向异性](../papers/ml-foundations.md#floros26a-evaluation) · On the Anisotropy of Score-Based Generative Models

### 图学习与推荐

- [图模型隐私评测](../papers/graph-and-recommendation.md#agbaje26a-evaluation) · Revisiting Asymmetries in Black-box Link Stealing against Graph Neural Networks
- [图模型迁移](../papers/graph-and-recommendation.md#akula26a-evaluation) · Same Graph Cross-Task Transfer in GNNs: Protocols and Predictors
- [缺失节点特征的压力测试](../papers/graph-and-recommendation.md#ferrini26a-evaluation) · Rethinking GNNs and Missing Features: Challenges, Evaluation and a Robust Solution
- [图 Mixup 插值质量诊断](../papers/graph-and-recommendation.md#forbat26a-evaluation) · Is Graph Mixup Beneficial? Investigating Interpolation And Empirical Performance of Graph Mixup Methods

### 科学机器学习

- [时间序列预测评测](../papers/scientific-ml.md#ahamed26a-evaluation) · TFRBench: A Reasoning Benchmark for Evaluating Forecasting Systems
- [格密码机器学习分析](../papers/scientific-ml.md#alfarano26a-evaluation) · Improving ML Attacks on LWE with Data Repetition and Stepwise Regression
- [恶意软件谱系重建](../papers/scientific-ml.md#amalan26a-evaluation) · MalTree: Tracing Malware Evolution from Embeddings at Scale
- [生存模型评测](../papers/scientific-ml.md#bahrini26a-evaluation) · When Can We Trust Survival Model Evaluation ?
- [CAD 操作评测](../papers/scientific-ml.md#bai26a-evaluation) · Op-CAD: Benchmarking and Investigating Operation-oriented CAD Generation
- [流体控制强化学习](../papers/scientific-ml.md#becktepe26a-evaluation) · Plug-and-Play Benchmarking of Reinforcement Learning Algorithms for Large-Scale Flow Control
- [仿真 Agent 成本评测](../papers/scientific-ml.md#cao26g-evaluation) · SimulCost: A Cost-Aware Benchmark and Toolkit for Automating Physics Simulations with LLMs
- [科学标注行为克隆](../papers/scientific-ml.md#chandok26a-evaluation) · A Systematic Study of Behavioral Cloning for Scientific Data Annotation
- [自然感官数据的跨刺激神经预测](../papers/scientific-ml.md#chen26fp-evaluation) · Real-World Unsupervised Models Generalize to Predict Brain Responses to Out-of-Distribution Stimuli
- [语言与语音层表征的脑响应对齐](../papers/scientific-ml.md#cheng26l-evaluation) · Abstraction Induces the Brain Alignment of Language and Speech Models
- [长程脑电癫痫检测的泛化评测](../papers/scientific-ml.md#dan26a-evaluation) · Quantifying the Generalization Gap in Seizure Detection: A Large-Scale Empirical Benchmark via the SzCORE Challenge
- [蛋白适应度的外推切分](../papers/scientific-ml.md#didi26a-evaluation) · FLIP2: Expanding Protein Fitness Landscape Benchmarks for Real-World Machine Learning Applications
- [生物基础模型的双类扰动诊断](../papers/scientific-ml.md#duan26f-evaluation) · (Be Cautious!) Bio-Foundation Models Are Not Yet Robust to Biologically Plausible Perturbations and ML Transformations
- [生物信息学智能体的流程稳健性评测](../papers/scientific-ml.md#fa26a-evaluation) · BioAgent Bench: An AI Agent Evaluation Suite for Bioinformatics
<!-- classification:end -->
