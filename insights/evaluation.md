# 评测与诊断

[首页](../README.md) · [English](../en/insights/evaluation.md)

基准、评测协议、消融与失效诊断。

<!-- classification:start -->
## 按研究领域浏览

[大语言模型](#by-llm) · [计算机视觉](#by-computer-vision) · [自然语言处理](#by-nlp) · [强化学习](#by-reinforcement-learning) · [机器人学](#by-robotics) · [多模态学习](#by-multimodal) · [机器学习基础与统计](#by-ml-foundations) · [图学习与推荐](#by-graph-and-recommendation) · [科学机器学习](#by-scientific-ml)

<a id="by-llm"></a>

### 大语言模型

- [推理系统评测](../conferences/icml-2026/cards/0001-0100.md#abramovich26a-evaluation) · SPEED-Bench: A Unified and Diverse Benchmark for Speculative Decoding
- [表征分析](../conferences/icml-2026/cards/0001-0100.md#acevedo26a-evaluation) · Differential syntactic and semantic encoding in LLMs
- [分阶段评测](../conferences/icml-2026/cards/0001-0100.md#acharya26a-evaluation) · CauSciBench: Can LLMs Automate Causal Inference in Real-World Scientific Research?
- [一致性训练](../conferences/icml-2026/cards/0001-0100.md#africa26a-evaluation) · Consistency Training Can Entrench Misalignment
- [持续记忆评测](../conferences/icml-2026/cards/0001-0100.md#ai26e-evaluation) · MemoryBench: A Benchmark for Memory and Continual Learning in LLM Systems
- [Agent 合规评测](../conferences/icml-2026/cards/0001-0100.md#aka26a-evaluation) · Evaluating Contextual Illegality: AI Compliance in Corporate Law Scenarios
- [基准饱和](../conferences/icml-2026/cards/0001-0100.md#akhtar26a-evaluation) · When AI Benchmarks Plateau: A Systematic Study of Benchmark Saturation
- [提示攻击检测](../conferences/icml-2026/cards/0001-0100.md#alshaalan26a-evaluation) · Detecting Fluent Optimization-Based Adversarial Prompts via Sequential Entropy Changes
- [长文本不确定性评测](../conferences/icml-2026/cards/0001-0100.md#amit26a-evaluation) · Evaluating LLM Uncertainty in Long-Form Generation Using Deterministic Ground Truth
- [形式化证明评测](../conferences/icml-2026/cards/0001-0100.md#ammanamanchi26a-evaluation) · Faults in Our Formal Benchmarking: Dataset Defects and Evaluation Failures in Lean Theorem Proving
- [模型输出尾部风险](../conferences/icml-2026/cards/0001-0100.md#angell26a-evaluation) · Estimating Tail Risks in Language Model Output Distributions
- [求解器反馈与 Agent RL](../conferences/icml-2026/cards/0101-0200.md#ao26a-evaluation) · ORLoopBench: Solver-in-the-Loop Benchmarks for Self-Correction and Behavioral Rationality in Operations Research
- [归纳头形成](../conferences/icml-2026/cards/0101-0200.md#aoyama26a-evaluation) · Predicting the Emergence of Induction Heads in Language Model Pretraining
- [隐性偏差审计](../conferences/icml-2026/cards/0101-0200.md#arcuschin26a-evaluation) · Biases in the Blind Spot: Detecting What LLMs Fail to Mention
- [推理忠实性](../conferences/icml-2026/cards/0101-0200.md#arcuschin26b-evaluation) · Chain-of-Thought Reasoning In The Wild Is Not Always Faithful
- [Agent 目标表征](../conferences/icml-2026/cards/0101-0200.md#arghal26a-evaluation) · A Behavioural and Representational Evaluation of Goal-Directedness in Language Model Agents
- [Agent 执行监控](../conferences/icml-2026/cards/0101-0200.md#arike26a-evaluation) · How does information access affect LLM monitors’ ability to detect sabotage?
- [语言模型电路](../conferences/icml-2026/cards/0101-0200.md#arora26c-evaluation) · Language Model Circuits Are Sparse in the Neuron Basis
- [LoRA 知识记忆](../conferences/icml-2026/cards/0101-0200.md#back26a-evaluation) · Understanding LoRA as Knowledge Memory: An Empirical Analysis
- [LLM 裁判校准](../conferences/icml-2026/cards/0101-0200.md#badshah26a-evaluation) · SCOPE: Selective Conformal Optimized Pairwise LLM Judging
- [对齐行为诊断](../conferences/icml-2026/cards/0101-0200.md#baek26d-evaluation) · Sycophancy Towards Researchers Drives Performative Misalignment
- [机制可解释性](../conferences/icml-2026/cards/0101-0200.md#bair26a-evaluation) · Compressed Sensing for Capability Localization in Large Language Models
- [形式化证明评测](../conferences/icml-2026/cards/0101-0200.md#baksys26a-evaluation) · miniF2F-Dafny: LLM-Guided Mathematical Theorem Proving via Auto-Active Verification
- [相关裁判聚合](../conferences/icml-2026/cards/0101-0200.md#balasubramanian26a-evaluation) · Dependence-Aware Label Aggregation for LLM-as-a-Judge via Ising Models
- [注意力电路稳定性](../conferences/icml-2026/cards/0201-0300.md#bali26a-evaluation) · Quantifying LLM Attention-Head Stability: Implications for Circuit Universality
- [偏好预测](../conferences/icml-2026/cards/0201-0300.md#ball26a-evaluation) · Reading Between the Tokens: Improving Preference Predictions through Mechanistic Forecasting
- [Agent 澄清评测](../conferences/icml-2026/cards/0201-0300.md#bao26e-evaluation) · DRIFT-BENCH: Diagnosing CoopeRative Breakdowns in LLM Agents under Input Faults via Multi-Turn Interaction
- [训练数据记忆评测](../conferences/icml-2026/cards/0201-0300.md#barbero26a-evaluation) · Extracting alignment data in open models
- [人机协作 Agent 评测](../conferences/icml-2026/cards/0201-0300.md#barres26a-evaluation) · $τ^2$-Bench: Evaluating Conversational Agents in a Dual-Control Environment
- [逻辑归纳评测](../conferences/icml-2026/cards/0201-0300.md#batzoglou26a-evaluation) · INDUCTION: Finite-Structure Concept Synthesis in First-Order Logic
- [推理过程评测](../conferences/icml-2026/cards/0201-0300.md#berdoz26b-evaluation) · Reasoning Structure of Large Language Models
- [语言表征几何](../conferences/icml-2026/cards/0201-0300.md#bernas26a-evaluation) · Revisiting Anisotropy in Language Transformers: The Geometry of Learning Dynamics
- [长文本事实性诊断](../conferences/icml-2026/cards/0201-0300.md#bhardwaj26a-evaluation) · Embedding Trust: Semantic Isotropy Predicts Nonfactuality in Long-Form Text Generation
- [推理自评](../conferences/icml-2026/cards/0201-0300.md#bi26e-evaluation) · The Geometry of Reasoning: Self-Evaluation via Layerwise Trajectory Evolution
- [幻觉检测](../conferences/icml-2026/cards/0201-0300.md#binkowski26a-evaluation) · Attention Sinks as Internal Signals for Hallucination Detection in Large Language Models
- [基准概念覆盖](../conferences/icml-2026/cards/0301-0400.md#bohacek26a-evaluation) · Uncovering Competency Gaps in Large Language Models and Their Benchmarks
- [推理忠实性](../conferences/icml-2026/cards/0301-0400.md#boppana26a-evaluation) · Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought
- [多 Agent 行为监控](../conferences/icml-2026/cards/0301-0400.md#bridgeford26a-evaluation) · Detecting Perspective Shifts in Multi-Agent Systems
- [事实召回评测](../conferences/icml-2026/cards/0301-0400.md#calderon26a-evaluation) · Empty Shelves or Lost Keys? Recall Is the Bottleneck for Parametric Factuality
- [动态调度评测](../conferences/icml-2026/cards/0401-0500.md#cao26z-evaluation) · DynaSchedBench: Calibrated Dynamic Scheduling Benchmarks and Observability Paradox in LLM-based Scheduling Agents
- [科学发现 Agent 评测](../conferences/icml-2026/cards/0401-0500.md#carlsson26a-evaluation) · SEDRAS: Symbolically Evaluated Deep Research And Science
- [LLM 标注评测](../conferences/icml-2026/cards/0401-0500.md#casanova26a-evaluation) · On the Limits of LLM Adaptability: Impact of Model-Internalized Priors on Annotation Task Performance
- [操作步骤评测](../conferences/icml-2026/cards/0401-0500.md#chang26e-evaluation) · How2Everything: Mining the Web for How-to Procedures to Evaluate and Improve LLMs
- [稀疏自编码器可解释性](../conferences/icml-2026/cards/0401-0500.md#chanin26a-evaluation) · Sparse but Wrong: Incorrect L0 Leads to Incorrect Features in Sparse Autoencoders
- [LLM API 变化检测](../conferences/icml-2026/cards/0401-0500.md#chauvin26a-evaluation) · Token-Efficient Change Detection in LLM APIs
- [Agent 因果推断评测](../conferences/icml-2026/cards/0401-0500.md#chen26l-evaluation) · CausalGame: Benchmarking Causal Thinking of LLM Agents in Games
- [幻觉逐步定位](../conferences/icml-2026/cards/0401-0500.md#chen26n-evaluation) · Mind the Gap: Catching Hallucinations via Evidence Drop on the Reasoning Manifold
- [优化建模 Agent 评测](../conferences/icml-2026/cards/0401-0500.md#chen26o-evaluation) · OPT-Engine: Benchmarking the Limits of LLMs in Optimization Modeling via Complexity Scaling
- [长上下文容量评测](../conferences/icml-2026/cards/0401-0500.md#chen26q-evaluation) · L-CUBE: Isolating Long-Context Capacity from Knowledge with Controllable Mutual Information Scaling
- [激活干预下的安全评测](../conferences/icml-2026/cards/0401-0500.md#chen26x-evaluation) · Adaptive Probe-based Steering for Robust LLM Jailbreaking
- [RLVR 的难学样本](../conferences/icml-2026/cards/0501-0600.md#chen26aq-evaluation) · The Unlearnability Phenomenon in RLVR for Language Models
- [机制电路的非唯一性](../conferences/icml-2026/cards/0501-0600.md#chen26bb-evaluation) · All Circuits Lead to Rome: Rethinking Functional Anisotropy in Circuit and Sheaf Discovery for LLMs
- [对齐奖励的隐含目标诊断](../conferences/icml-2026/cards/0501-0600.md#chen26bg-evaluation) · Discovering Implicit Large Language Model Alignment Objectives
- [欠定问题的假设覆盖](../conferences/icml-2026/cards/0501-0600.md#chen26bz-evaluation) · HypoSpace: A Diagnostic Benchmark for Set-Valued Hypothesis Generation under Underdetermination and Sublinear Coverage Bounds
- [交互式科学代码评测](../conferences/icml-2026/cards/0501-0600.md#chen26cf-evaluation) · InteractScience: Programmatic and Visually-Grounded Evaluation of Interactive Scientific Demonstration Code Generation
- [可解释注意力头的训练数据归因](../conferences/icml-2026/cards/0501-0600.md#chen26cv-evaluation) · Mechanistic Data Attribution: Tracing the Training Origins of Interpretable LLM Units
- [人机协作智能体评测](../conferences/icml-2026/cards/0501-0600.md#chen26da-evaluation) · How can we assess human-agent interactions? Case studies in software agent design
- [用逐层预测变化衡量推理投入](../conferences/icml-2026/cards/0501-0600.md#chen26di-evaluation) · Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens
- [代码生成的诈骗链接审计](../conferences/icml-2026/cards/0501-0600.md#chen26dp-evaluation) · Scam2Prompt: A Scalable Framework for Auditing Malicious Scam Endpoints in Production LLMs
- [工具智能体的用户交互评测](../conferences/icml-2026/cards/0601-0700.md#chen26eg-evaluation) · AppWorld-UL: Benchmarking Diverse Agent-User Interactions for Tool-Use
- [分块低比特量化格式比较](../conferences/icml-2026/cards/0601-0700.md#chen26fa-evaluation) · INT vs. FP: A Comprehensive Study of Fine-Grained Low-bit Quantization Formats
- [量化感知训练的激活异常值诊断](../conferences/icml-2026/cards/0601-0700.md#chen26gl-evaluation) · Scaling Law for Quantization-Aware Training
- [语言模型强化学习的采样预算分配](../conferences/icml-2026/cards/0601-0700.md#cheng26n-evaluation) · IsoCompute Playbook: Optimally Scaling Sampling Compute for LLM RL
- [智能体劳务市场的策略诊断](../conferences/icml-2026/cards/0701-0800.md#chiu26a-evaluation) · When AI Agents Compete for Jobs: Strategic Capabilities and Economic Dynamics of AI Labour Markets
- [续写分布的语义与机制聚类](../conferences/icml-2026/cards/0701-0800.md#cho26g-evaluation) · Shared Semantics, Divergent Mechanisms: Unsupervised Feature Discovery by Aligning Semantics and Mechanisms
- [语言模型评委的潜在质量诊断](../conferences/icml-2026/cards/0701-0800.md#choi26n-evaluation) · Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory
- [冻结演化轨迹的反馈归因](../conferences/icml-2026/cards/0701-0800.md#chong26b-evaluation) · Towards Feedback-to-Plan Decisions for Self-Evolving LLM Agents in CUDA Kernel Generation
- [注意力输出的有符号贡献](../conferences/icml-2026/cards/0801-0900.md#cunningham26a-evaluation) · Contribution Weights: A Geometrical Analysis of Self-Attention Transformers
- [社会影响信号的在线序贯监测](../conferences/icml-2026/cards/0801-0900.md#dai26d-evaluation) · Three Years of r/ChatGPT: Societal Impact Evaluations from Social Media Data
- [图路径诊断推理幻觉](../conferences/icml-2026/cards/0801-0900.md#dai26k-evaluation) · When Do Hallucinations Arise? A Graph Perspective on the Evolution of Path Reuse and Path Compression
- [持续软件演进的里程碑评测](../conferences/icml-2026/cards/0801-0900.md#deng26d-evaluation) · SWE-Milestone: Evaluating AI Agents on Continuous Software Evolution
- [跨文件软件工程的补丁验证](../conferences/icml-2026/cards/0801-0900.md#deng26f-evaluation) · SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?
- [歧义搜索的交互必要性检测](../conferences/icml-2026/cards/0801-0900.md#deng26h-evaluation) · InteractComp: Evaluating Search Agents With Ambiguous Queries
- [审稿意见的分类校验](../conferences/icml-2026/cards/0801-0900.md#deng26j-evaluation) · CoCoReviewBench: A Completeness- and Correctness-Oriented Benchmark for AI Reviewers
- [多模型投票的相关错误诊断](../conferences/icml-2026/cards/0801-0900.md#denisov-blanch26a-evaluation) · Truthfulness Does Not Scale Like Reasoning: Why Polling Fails as a Proxy Verifier
- [奖励投机的对照轨迹评测](../conferences/icml-2026/cards/0801-0900.md#deshpande26a-evaluation) · Benchmarking Reward Hack Detection in Code Environments via Contrastive Analysis
- [可切换适配器的模型自审计](../conferences/icml-2026/cards/0801-0900.md#dietz26a-evaluation) · Split Personality Training: Revealing Latent Knowledge Through Alternate Personalities
- [从空工作区生成 Python 仓库的评测](../conferences/icml-2026/cards/0901-1000.md#ding26j-evaluation) · NL2Repo-Bench: Towards Long-Horizon Repository Generation Evaluation of Coding Agents
- [RLVR 训练目标劫持诊断](../conferences/icml-2026/cards/0901-1000.md#dong26b-evaluation) · Probing RLVR Training Instability through the Lens of Objective-Level Hacking
- [搜索智能体的沙箱红队评测](../conferences/icml-2026/cards/0901-1000.md#dong26c-evaluation) · SafeSearch: Automated Red-Teaming of LLM-Based Search Agents
- [用成对推理比较降低评测方差](../conferences/icml-2026/cards/0901-1000.md#dong26o-evaluation) · Evaluating LLMs When They Do Not Know the Answer: Statistical Evaluation of Mathematical Reasoning via Comparative Signals
- [用超额描述长度区分能力诱发与学习](../conferences/icml-2026/cards/0901-1000.md#donoway26a-evaluation) · Bits That Count: Quantifying and Predicting Capabilities of Language Models
- [语言模型罕见事件的重要性估计](../conferences/icml-2026/cards/0901-1000.md#dorman26a-evaluation) · Rare Event Analysis of Large Language Models
- [多智能体通信协议的受控评测](../conferences/icml-2026/cards/0901-1000.md#du26l-evaluation) · ProtocolBench: Which LLM MultiAgent Protocol to Choose?
- [语言不确定性词的正确率校准](../conferences/icml-2026/cards/0901-1000.md#duan26b-evaluation) · "very likely" Means "uncertain"? How LLMs Diverge from Humans in Linguistic Uncertainty Quantification
- [可控 2-SAT 结构鲁棒性评测](../conferences/icml-2026/cards/1001-1100.md#es-sebbani26a-evaluation) · Evaluating Robustness of Reasoning Models on Parameterized Logical Problems
- [越狱论文到可复现评测模块](../conferences/icml-2026/cards/1001-1100.md#fang26y-evaluation) · Jailbreak Foundry: From Papers to Runnable Attacks for Reproducible Benchmarking
- [奖励模型偏差的激活投影](../conferences/icml-2026/cards/1001-1100.md#fein26a-evaluation) · One Bias After Another: Mechanistic Reward Shaping and Persistent Biases in Language Reward Models
- [外部技能组合的后门评测](../conferences/icml-2026/cards/1001-1100.md#feng26c-evaluation) · SkillTrojan: Backdoor Attacks on Skill-Based Agent Systems
- [推理链的失败步骤比例](../conferences/icml-2026/cards/1101-1200.md#feng26e-evaluation) · What Characterizes Effective Reasoning? Revisiting Length, Review, and Structure of CoT
- [关系推理的元数控制评测](../conferences/icml-2026/cards/1101-1200.md#fesser26a-evaluation) · Evaluating Relational Reasoning in LLMs with REL
- [注意力奇异向量的特征对齐诊断](../conferences/icml-2026/cards/1101-1200.md#franco26a-evaluation) · Singular Vectors of Attention Heads Align with Features
- [代码智能体的迭代锦标赛](../conferences/icml-2026/cards/1101-1200.md#fu26a-evaluation) · CATArena: Evaluating Evolutionary Capabilities of Code Agents via Iterative Tournaments
- [幻灯片代理任务的分项评分](../conferences/icml-2026/cards/1201-1300.md#gandhi26a-evaluation) · PPT-Eval: A Benchmark for Computer-Use Agents on PowerPoint Tasks
- [长上下文中少量困难干扰的影响](../conferences/icml-2026/cards/1201-1300.md#gao26b-evaluation) · The First Drop of Ink: Nonlinear Impact of Distracting Information in Long-Context Reasoning
- [权重稀疏模型的电路提取](../conferences/icml-2026/cards/1201-1300.md#gao26w-evaluation) · Weight-sparse transformers have interpretable circuits
- [大学数学证明的双量规评判](../conferences/icml-2026/cards/1301-1400.md#gonzalez26a-evaluation) · QEDBench: Quantifying the Alignment Gap in Automated Evaluation of University-Level Mathematical Proofs
- [直接偏好对齐的可控比较](../conferences/icml-2026/cards/1301-1400.md#gorbatovski26a-evaluation) · The Differences Between Direct Alignment Algorithms are a Blur
- [词元扰动的成分响应分析](../conferences/icml-2026/cards/1301-1400.md#gordon26a-evaluation) · Towards Spectroscopy: Susceptibility Clusters in Language Models
- [表格语言模型的任务级泄漏核查](../conferences/icml-2026/cards/1301-1400.md#gorla26a-evaluation) · The Illusion of Generalization in Tabular Language Models
- [智能体对训练接口的依赖诊断](../conferences/icml-2026/cards/1301-1400.md#gu26g-evaluation) · What Do Agents Learn from Trajectory-SFT: Semantics or Interfaces?
- [跨推理框架的静默错误定位](../conferences/icml-2026/cards/1301-1400.md#gu26q-evaluation) · Ekka: Automated Diagnosis of Silent Errors in LLM Inference
- [带执行反馈的 Triton 代码智能体评测](../conferences/icml-2026/cards/1301-1400.md#guan26d-evaluation) · TritonGym: A Benchmark for Agentic LLM Workflows in Triton GPU Code Generation
- [推理轨迹的可监测性评测](../conferences/icml-2026/cards/1301-1400.md#guan26h-evaluation) · Monitoring Monitorability
- [工具故障下的智能体失败披露评测](../conferences/icml-2026/cards/1301-1400.md#guo26k-evaluation) · Are Your Agents Upward Deceivers?
- [并发代码的数据竞争定位](../conferences/icml-2026/cards/1301-1400.md#guo26z-evaluation) · DRPBench: Evaluating LLMs in Concurrent Code Comprehension via Fine-Grained Data Race Prediction
- [确定性状态追踪的轨迹漂移度量](../conferences/icml-2026/cards/1301-1400.md#guo26ab-evaluation) · The Deterministic Horizon: When Extended Reasoning Fails and Tool Delegation Becomes Necessary
- [金融问答的真实查询与在线评测](../conferences/icml-2026/cards/1401-1500.md#guo26ah-evaluation) · BizFinBench.v2: Towards Reliable LLMs in Finance via Real-User Data and Offline/Online Bilingual Evaluation
- [部署实例的伪随机指纹](../conferences/icml-2026/cards/1401-1500.md#gurvan26a-evaluation) · FLIPS: Instance-Fingerprinting for LLMs via Pseudo-random Sequences
- [多智能体辩论的修订距离](../conferences/icml-2026/cards/1401-1500.md#ha26a-evaluation) · Beyond Correctness: Distance-Based Social Dynamics of Multi-Agent Debate
- [多智能体安全的分阶段评测](../conferences/icml-2026/cards/1401-1500.md#hagag26a-evaluation) · Architecture Matters for Multi-Agent Security
- [异质偏好的局部稳定排行榜](../conferences/icml-2026/cards/1401-1500.md#haghtalab26a-evaluation) · Pluralistic Leaderboards
- [偏好数据中的质量与偏见混杂](../conferences/icml-2026/cards/1401-1500.md#hahm26a-evaluation) · Alignment Tampering: How Reinforcement Learning from Human Feedback Is Exploited to Optimize Misaligned Biases
- [从旋转频率核识别长上下文注意力头](../conferences/icml-2026/cards/1401-1500.md#han26e-evaluation) · Revealing Long-context Potential of Attention Heads via Frequency Kernels
- [专家报告的细粒度核查](../conferences/icml-2026/cards/1401-1500.md#han26m-evaluation) · DEER: A Benchmark for Evaluating Deep Research Agents on Expert Report Generation
- [语言模型自述人格的行为验证](../conferences/icml-2026/cards/1401-1500.md#han26n-evaluation) · The Personality Illusion: Revealing Dissociation Between Self-Reports & Behavior in LLMs
- [内生和提示诱发价值的机制分解](../conferences/icml-2026/cards/1401-1500.md#han26q-evaluation) · Dual Mechanisms of Value Expression: Intrinsic vs. Prompted Values in Large Language Models
- [为排行榜趋势拆分潜在能力和测量噪声](../conferences/icml-2026/cards/1401-1500.md#hardy26a-evaluation) · AI Cartography: Mapping the Latent Landscape of AI Benchmark Ecosystems
- [交叉评估微调语言与安全测试语言](../conferences/icml-2026/cards/1401-1500.md#hawkins26a-evaluation) · The Heterogeneous Safety Impacts of Benign Multilingual Fine-Tuning
- [用结构操作诊断推理能力](../conferences/icml-2026/cards/1501-1600.md#he26x-evaluation) · Can LLMs Reason Structurally? Benchmarking via the lens of Data Structures
- [从真实补丁提取可复现的代码提速任务](../conferences/icml-2026/cards/1501-1600.md#he26y-evaluation) · SWE-Perf: Can Language Models Optimize Code Performance on Real-World Repositories?
- [分层测量剪枝造成的生成漂移](../conferences/icml-2026/cards/1501-1600.md#he26ag-evaluation) · Demystifying When Pruning Works via Representation Hierarchies
- [用跨会话任务检验记忆能否指导行动](../conferences/icml-2026/cards/1501-1600.md#he26am-evaluation) · Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks
- [用旧模型回答推断新模型基准分](../conferences/icml-2026/cards/1501-1600.md#helm26a-evaluation) · Query-efficient model evaluation using cached responses
- [按专家实际写入残差的贡献做解释](../conferences/icml-2026/cards/1501-1600.md#herbst26a-evaluation) · The Expert Strikes Back: Interpreting Mixture-of-Experts Language Models at Expert Level
- [将注入执行和原文保真分别评测](../conferences/icml-2026/cards/1501-1600.md#hermon26a-evaluation) · Security–Fidelity Tradeoffs: The Hidden Cost of Prompt Injection Defense
- [放大推理任务向量进行白盒审计](../conferences/icml-2026/cards/1501-1600.md#hopkins26a-evaluation) · Overthinking: Amplifying Reasoning Weights to Extract Learned Secrets
- [从因果激活轨迹识别拒答失稳](../conferences/icml-2026/cards/1601-1700.md#hu26ax-evaluation) · Tracing the Dynamics of Refusal: Exploiting Latent Refusal Trajectories for Robust Jailbreak Detection
- [把采样来源与训练损失交叉消融](../conferences/icml-2026/cards/1601-1700.md#huan26a-evaluation) · Does Math Reasoning Improve General LLM Capabilities? Understanding Transferability of LLM Reasoning
- [先精确反编译再按因果效应剪枝](../conferences/icml-2026/cards/1601-1700.md#huang26b-evaluation) · Discovering Interpretable Algorithms by Decompiling Transformers to RASP
- [审计安全数据自动增广的污染传播](../conferences/icml-2026/cards/1601-1700.md#huang26e-evaluation) · Rapid Poison: Practical Poisoning Attacks Against the Rapid Response Framework
- [在失败探测中划分探索和复查预算](../conferences/icml-2026/cards/1701-1800.md#huang26r-evaluation) · ProbeLLM: Automating Principled Diagnosis of LLM Failures
- [用滚动崩溃集与补丁双指标评估修复](../conferences/icml-2026/cards/1701-1800.md#huang26al-evaluation) · Outrunning LLM Cutoffs: A Live Kernel Crash Resolution Benchmark for All
- [用设备负载分布和 TTFT 共同审计 MoE 路由](../conferences/icml-2026/cards/1701-1800.md#huang26bc-evaluation) · RepetitionCurse: Measuring and Understanding Router Imbalance in Mixture-of-Experts LLMs under DoS Stress
- [按表格拓扑构建多轮用表轨迹](../conferences/icml-2026/cards/1701-1800.md#huang26cf-evaluation) · How Far Can LLM Agents Reason with Tables? Benchmarking Multi-Turn Agentic Table Question Answering in the Wild
- [用自适应重写压力测试语言水印](../conferences/icml-2026/cards/1701-1800.md#huang26ch-evaluation) · RLCracker: Evaluating the Worst-Case Vulnerability of LLM Watermarks with Adaptive RL Attacks
- [在任务可解时检验代理能否遵守素材许可](../conferences/icml-2026/cards/1701-1800.md#hui26a-evaluation) · Copyright-Bench: Agentic Evaluation of Copyright Law Compliance
- [用改写压力测试词元水印的概率裕量](../conferences/icml-2026/cards/1701-1800.md#hwang26e-evaluation) · LLM Watermark Evasion via Bias Inversion
- [把感知资源压力与实际上下文耗用区分开来](../conferences/icml-2026/cards/1801-1900.md#igbinedion26a-evaluation) · Lost in Context: Addressing Context Anxiety in Large Language Models
- [用随机记分标签设置污染检验上限](../conferences/icml-2026/cards/1801-1900.md#ishida26a-evaluation) · CapBencher: Give Your LLM Benchmark a Built-in Alarm for Test-Set Overfitting
- [用独立方式区分能力缺失和探索受抑](../conferences/icml-2026/cards/1801-1900.md#jang26b-evaluation) · Exploration Hacking: Can LLMs Learn to Resist RL Training?
- [以语义干扰下的预测稳定度校准置信](../conferences/icml-2026/cards/1801-1900.md#jawad26a-evaluation) · CaliDist: Calibrating Large Language Models via Behavioral Robustness to Distraction
- [用跨能力激活交集定位关键神经元](../conferences/icml-2026/cards/1801-1900.md#ji26a-evaluation) · Tiny Brains, Giant Impact: Uncovering the Keystone Neurons of LLM with Just a Few Prompts
- [分开检验表格预测的意图识别与模型构造](../conferences/icml-2026/cards/1801-1900.md#ji26c-evaluation) · TopBench: A Benchmark for Implicit Predictive Reasoning in Tabular Question Answering
- [把多模型分歧浓缩成可核验争点](../conferences/icml-2026/cards/1901-2000.md#jiang26d-evaluation) · Collaborative Disagreement Resolution for Scalable Oversight
- [按路由干预诊断 MoE 安全集中性](../conferences/icml-2026/cards/1901-2000.md#jiang26o-evaluation) · Sparse Models, Sparse Safety: Unsafe Routes in Mixture-of-Experts LLMs
- [用位移与曲率联合诊断推理轨迹](../conferences/icml-2026/cards/1901-2000.md#jiang26af-evaluation) · Beyond Scalars: Evaluating and Understanding LLM Reasoning via Geometric Progress and Stability
- [跨轮验证代理的安全目标是否被逐步改写](../conferences/icml-2026/cards/1901-2000.md#jiang26as-evaluation) · AgentLAB: Benchmarking LLM Agents against Long-Horizon Attacks
- [把裁判置信度训练为人类一致性排序](../conferences/icml-2026/cards/1901-2000.md#jin26h-evaluation) · Margin-Adaptive Confidence Ranking for Reliable LLM Judgement
- [分开评测代理的环境识别和拒绝](../conferences/icml-2026/cards/1901-2000.md#jones26a-evaluation) · A New Framework for Cybersecurity Refusals in AI Agents
- [用执行反馈搜寻良性指令下的意外风险](../conferences/icml-2026/cards/1901-2000.md#jones26b-evaluation) · When Benign Inputs Lead to Severe Harms: Eliciting Unsafe Unintended Behaviors of Computer-Use Agents
- [将数据影响沿循环计算的各步展开](../conferences/icml-2026/cards/2001-2100.md#kaissis26a-evaluation) · Step-Resolved Data Attribution for Looped Transformers
- [用临时中层读出测试特征可达性](../conferences/icml-2026/cards/2001-2100.md#kang26r-evaluation) · Capacity without Access: Reinterpreting the Mid-Depth Spectral Plateau in LLMs
- [把内层激活读出训练成可提问接口](../conferences/icml-2026/cards/2001-2100.md#karvonen26a-evaluation) · Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers
- [用序列概率波动做预训练成员诊断](../conferences/icml-2026/cards/2001-2100.md#ke26f-evaluation) · Rethinking Pretraining Data Detection for LLMs: From Local to Global
- [把题目差异纳入模型基准的区间估计](../conferences/icml-2026/cards/2001-2100.md#keller26a-evaluation) · Expanding the AI Evaluation Toolbox with Statistical Models
- [对偏好子群分布做鲁棒模型混合](../conferences/icml-2026/cards/2001-2100.md#khalaf26a-evaluation) · Robust AI Evaluation through Maximal Lotteries
- [生成能分辨候选程序的执行测试](../conferences/icml-2026/cards/2001-2100.md#kim26d-evaluation) · Rule2DRC: Benchmarking LLM Agents for DRC Script Synthesis with Execution-Guided Test Generation
- [以排序锚点校准语言模型表达的价值强度](../conferences/icml-2026/cards/2101-2200.md#kim26r-evaluation) · VALUEFLOW: Toward Pluralistic and Steerable Value-based Alignment in Large Language Models

<a id="by-computer-vision"></a>

### 计算机视觉

- [视觉推理评测](../conferences/icml-2026/cards/0001-0100.md#acuaviva26a-evaluation) · Rethinking Visual Intelligence: Insights from Video Pretraining
- [分割模型诊断](../conferences/icml-2026/cards/0001-0100.md#ahmed26a-evaluation) · Med-SegLens: Latent-Level Model Diffing for Interpretable Medical Image Segmentation
- [扩散模型域外检测](../conferences/icml-2026/cards/0001-0100.md#alexis26a-evaluation) · GEPC: Group-Equivariant Posterior Consistency for Out-of-Distribution Detection in Diffusion Models
- [深伪防御评测](../conferences/icml-2026/cards/0101-0200.md#baek26e-evaluation) · Proactive Defense Benchmark against Deepfake Generation
- [扩散模型概念遗忘](../conferences/icml-2026/cards/0301-0400.md#braun26b-evaluation) · Erased but Not Forgotten: How Backdoors Compromise Concept Erasure
- [生成模型后门评测](../conferences/icml-2026/cards/0501-0600.md#chen26az-evaluation) · Semantic-level Backdoor Attack against Text-to-Image Diffusion Models
- [人脸数据集内在质量估计](../conferences/icml-2026/cards/0601-0700.md#chen26gw-evaluation) · Efficient, Validation-Free Intrinsic Quality Estimation for Large-Scale Face Recognition Datasets
- [视觉表征的组合绑定诊断](../conferences/icml-2026/cards/0701-0800.md#chung26a-evaluation) · Global Geometry Is Not Enough for Vision Representations
- [类别遗忘的近邻输出泄漏](../conferences/icml-2026/cards/1001-1100.md#ebrahimpour-boroojeny26a-evaluation) · Unlearning Isn’t Forgetting: Revealing Hidden Leakage in Class Unlearning Evaluations
- [概念感知的显著性图](../conferences/icml-2026/cards/1001-1100.md#elisha26a-evaluation) · ConEx: Human-Interpretable Saliency Maps via Concept-Aware Attribution
- [交互世界模型的统一动作编码](../conferences/icml-2026/cards/1001-1100.md#fang26l-evaluation) · iWorld-Bench: A Benchmark for Interactive World Models with a Unified Action Generation Framework
- [高斯泼溅资产的变换溯源](../conferences/icml-2026/cards/1401-1500.md#han26t-evaluation) · GaussTrace: Provenance Analysis of 3D Gaussian Splatting Models with Evidence-based LLM Reasoning
- [用条件熵定位扩散的语义形成窗口](../conferences/icml-2026/cards/1401-1500.md#handke26a-evaluation) · The Entropic Signature of Class Speciation in Diffusion Models
- [插入抑制证据解释缺席概念](../conferences/icml-2026/cards/1501-1600.md#hesse26a-evaluation) · What is Missing? Explaining Neurons Activated by Absent Concepts
- [用人工定位上界区分小物体编辑和评审失败](../conferences/icml-2026/cards/1501-1600.md#hong26a-evaluation) · DLEBench: Evaluating Small-scale Object Editing Ability for Instruction-based Image Editing Model
- [跨训练阶段检验持续学习的后门持久性](../conferences/icml-2026/cards/1601-1700.md#huang26n-evaluation) · Persistent Backdoor Attacks in Class-Incremental Learning via Structural Invariant Anchoring
- [从特征存在性中扣除对象绑定信息](../conferences/icml-2026/cards/1701-1800.md#huang26y-evaluation) · Formalizing the Binding Problem
- [把扩散调度输入作为独立的安全审计面](../conferences/icml-2026/cards/1701-1800.md#huang26av-evaluation) · Watch Your Step: Information Injection in Diffusion Models via Shadow Timestep Embedding
- [按异常对象分配覆盖与误报代价](../conferences/icml-2026/cards/1801-1900.md#iqbal26a-evaluation) · Formally Exploring Visual Anomaly Detection Evaluation Metrics
- [从分布内几何挑选马氏检测的径向缩放](../conferences/icml-2026/cards/1801-1900.md#janiak26a-evaluation) · A Geometry-Based View of Mahalanobis OOD Detection
- [分别打乱概念频率与保留组合来定位生成失败](../conferences/icml-2026/cards/1801-1900.md#jeong26b-evaluation) · When Do Diffusion Models Learn to Generate Multiple Objects?
- [按观测锚点密度判断弱先验是否够用](../conferences/icml-2026/cards/1801-1900.md#jia26k-evaluation) · Weak Diffusion Priors Can Still Achieve Strong Inverse-Problem Performance
- [用多维因果干预检查视频物理表征](../conferences/icml-2026/cards/2001-2100.md#joseph26a-evaluation) · Interpreting Physics in Video World Models
- [固定下游容量和训练组合再比较对象槽](../conferences/icml-2026/cards/2001-2100.md#kapl26b-evaluation) · Are Object-Centric Representations Better at Compositional Generalization?
- [用混合真实和修补区域诊断检测通道](../conferences/icml-2026/cards/2001-2100.md#kim26k-evaluation) · Dissect and Prune: Enhancing Robustness in AI-Generated Image Detection
- [把噪声强度相对模型预处理的变化纳入评测](../conferences/icml-2026/cards/2101-2200.md#kim26w-evaluation) · Unlocking Noise-Resistant Vision: Key Architectural Secrets for Robust Models Against Gaussian Noise

<a id="by-nlp"></a>

### 自然语言处理

- [分词器评测](../conferences/icml-2026/cards/0001-0100.md#altintas26a-evaluation) · TokSuite: Measuring the Impact of Tokenizer Choice on Language Model Behavior
- [音频表征评测](../conferences/icml-2026/cards/0201-0300.md#basha26a-evaluation) · VocSim A Training-free Benchmark for Zero-shot Content Identity in Single-source Audio
- [检索增强生成安全评测](../conferences/icml-2026/cards/0501-0600.md#chen26av-evaluation) · Eyes-on-Me: Scalable RAG Poisoning through Transferable Attention-Steering Attractors
- [生成文本的惊异度转移检测](../conferences/icml-2026/cards/0501-0600.md#chen26bf-evaluation) · Black-Box Detection of LLM-Generated Text Using Generalized Jensen Shannon Divergence
- [音频深伪检测的多样性压力测试](../conferences/icml-2026/cards/0801-0900.md#dehdashtian26a-evaluation) · FoeGlass: Simple In-Context Learning Is Enough for Red Teaming Audio Deepfake Detectors
- [同行评审来源的声明级检测](../conferences/icml-2026/cards/0901-1000.md#duarte26a-evaluation) · Sem-Detect: Semantic Level Detection of AI Generated Peer-Reviews
- [重写式事后文本水印评测](../conferences/icml-2026/cards/1101-1200.md#fernandez26b-evaluation) · How Good is Post-Hoc Watermarking With Language Model Rephrasing?
- [机器翻译的无参考成对排序](../conferences/icml-2026/cards/1201-1300.md#gao26af-evaluation) · FiRE: Fine-grained Ranking Evaluation for Machine Translation
- [音频自监督表征的凸门控探测](../conferences/icml-2026/cards/1201-1300.md#ghaffari26a-evaluation) · BAT: Better Audio Transformer Guided by Convex Gated Probing
- [基于低概率词位的不确定性检测](../conferences/icml-2026/cards/1301-1400.md#guo26w-evaluation) · On the Salience of Low-Probability Tokens for AI-Generated Text Detection: A Multiscale Uncertainty Perspective
- [基于真实音乐密度的生成检测](../conferences/icml-2026/cards/1401-1500.md#han26u-evaluation) · MusicDET: Zero-Shot AI-Generated Music Detection
- [把模式归纳约束为可审计的类型图](../conferences/icml-2026/cards/1601-1700.md#hu26t-evaluation) · SCOPE and SCION: A Benchmark and an Auditable Reference Pipeline for Schema Induction and Fusion from Text
- [交换证据语言测引证相关性偏差](../conferences/icml-2026/cards/2001-2100.md#ki26a-evaluation) · Linguistic Nepotism: Trading-off Quality for Language Preference in Multilingual RAG

<a id="by-reinforcement-learning"></a>

### 强化学习

- [防御强化学习奖励](../conferences/icml-2026/cards/0201-0300.md#bates26a-evaluation) · Beyond Rewards in RL for Cyber Defence
- [像素策略的单因素泛化评测](../conferences/icml-2026/cards/0701-0800.md#cherepanov26a-evaluation) · KAGE-Bench: Fast Known-Axis Visual Generalization Evaluation for Reinforcement Learning
- [强化学习后门的逐步不确定性监测](../conferences/icml-2026/cards/1301-1400.md#guo26f-evaluation) · PolicyGuard: Towards Test-time and Step-level Adversary Defense for Reinforcement Learning Agent
- [持续记录新队友和新布局中的上下文适应](../conferences/icml-2026/cards/1901-2000.md#jing26d-evaluation) · Benchmarking the Limits of In-Context Reinforcement Learning for Ad-Hoc Teamwork

<a id="by-robotics"></a>

### 机器人学

- [机器人轨迹安全](../conferences/icml-2026/cards/0101-0200.md#bai26e-evaluation) · SafeLab: An Interactive High-Fidelity Benchmark for Embodied Safety in Scientific Robotics
- [柔性线状物体操作](../conferences/icml-2026/cards/0401-0500.md#cao26w-evaluation) · DLO-Lab: Benchmarking Deformable Linear Object Manipulations with Differentiable Physics
- [长程操作记忆的分项评测](../conferences/icml-2026/cards/0801-0900.md#dai26c-evaluation) · RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies
- [机器人生成视频的物理与任务评测](../conferences/icml-2026/cards/0801-0900.md#deng26r-evaluation) · Rethinking Video Generation Model for the Embodied World
- [动作块增量的基准姿态](../conferences/icml-2026/cards/1101-1200.md#feng26ab-evaluation) · Demystifying Action Space Design for Robotic Manipulation Policies
- [机器人代码策略的分层脚手架评测](../conferences/icml-2026/cards/1101-1200.md#fu26u-evaluation) · CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation
- [分开审计 VLA 的指令、推理与动作链路](../conferences/icml-2026/cards/1701-1800.md#huang26cm-evaluation) · TRAP: Hijacking VLA CoT-Reasoning via Adversarial Patches
- [协作增强时交换兼容伙伴轨迹并推演双人动作](../conferences/icml-2026/cards/2001-2100.md#kang26i-evaluation) · Moving Out: Physically-grounded Human-AI Collaboration

<a id="by-multimodal"></a>

### 多模态学习

- [视觉语言安全评测](../conferences/icml-2026/cards/0101-0200.md#azulay26a-evaluation) · Jailbreaking Vision-Language Models Through the Visual Modality
- [文档 Agent 评测](../conferences/icml-2026/cards/0301-0400.md#borchmann26a-evaluation) · Strategic Navigation or Stochastic Search? How Agents and Humans Reason Over Document Collections
- [视觉语言模型量化](../conferences/icml-2026/cards/0301-0400.md#bouguerra26a-evaluation) · Less Precise Can Be More Reliable: A Systematic Evaluation of Quantization’s Impact on VLMs Beyond Accuracy
- [图像感知评测](../conferences/icml-2026/cards/0301-0400.md#cao26i-evaluation) · UniPercept: Towards Unified Perceptual-Level Image Understanding across Aesthetics, Quality, Structure, and Texture
- [音视频生成评测](../conferences/icml-2026/cards/0401-0500.md#cao26v-evaluation) · T2AV-Compass: Towards Unified Evaluation for Text-to-Audio-Video Generation
- [音视频未来预测评测](../conferences/icml-2026/cards/0401-0500.md#chen26ad-evaluation) · FutureOmni: Evaluating Future Forecasting from Omni-Modal Context for Multimodal LLMs
- [误导视觉线索的配对评测](../conferences/icml-2026/cards/0501-0600.md#chen26dh-evaluation) · MVI-Bench: A Comprehensive Benchmark for Evaluating Robustness to Misleading Visual Inputs in LVLMs
- [基于物体提示的幻觉检测](../conferences/icml-2026/cards/0501-0600.md#chen26dl-evaluation) · DOUBT: Decoupled Object-level Understanding and Bridging via vMF-based Trustworthiness for Hallucination Detection in MLLMs
- [文生图工具链越狱评测](../conferences/icml-2026/cards/0601-0700.md#chen26en-evaluation) · OrchJail: Jailbreaking Tool-Calling Text-to-Image Agents by Orchestration-Guided Fuzzing
- [基础视觉推理诊断](../conferences/icml-2026/cards/0601-0700.md#chen26fj-evaluation) · BabyVision: Visual Reasoning Beyond Language
- [文生图人口属性多样性评测](../conferences/icml-2026/cards/0601-0700.md#chen26gz-evaluation) · HoloFair: Unified T2I Fairness Evaluation and Fair-GRPO Debiasing
- [视觉语言模型的选择偏好审计](../conferences/icml-2026/cards/0701-0800.md#cherep26a-evaluation) · Visual Persuasion: What Influences Decisions of Vision-Language Models?
- [游戏开发智能体的运行时反馈](../conferences/icml-2026/cards/0701-0800.md#chi26a-evaluation) · GameDevBench: Evaluating Agentic Capabilities Through Game Development
- [视觉实体追踪的感知与推理解耦](../conferences/icml-2026/cards/0701-0800.md#cohen26d-evaluation) · MET-Bench: Multimodal Entity Tracking for Evaluating the Limitations of Vision-Language and Reasoning Models
- [视觉历史中的跨图检索评测](../conferences/icml-2026/cards/0801-0900.md#deng26g-evaluation) · DeepImageSearch: Benchmarking Multimodal Agents for Context-Aware Image Retrieval in Visual Histories
- [科学视频推理的视觉依赖校验](../conferences/icml-2026/cards/0801-0900.md#deng26w-evaluation) · SciVideoBench: Benchmarking Scientific Video Reasoning in Large Multimodal Models
- [语义近邻校准标注判错](../conferences/icml-2026/cards/0801-0900.md#di26b-evaluation) · Detecting Errors in AI-Generated Annotations: When and Why Semantic Neighbors Help
- [由图像主动决定开放网页检索](../conferences/icml-2026/cards/1001-1100.md#fan26a-evaluation) · NAVIGATE: Evaluating Visual-Guided Search Decision-Making on the Open Web
- [用图像证据约束欺骗辩论](../conferences/icml-2026/cards/1001-1100.md#fang26f-evaluation) · Debate with Images: Detecting Deceptive Behaviors in Multimodal Large Language Models
- [音频安全评测的稀疏梯度诊断](../conferences/icml-2026/cards/1001-1100.md#fang26r-evaluation) · Sparse Tokens Suffice: Jailbreaking Audio Language Models via Token-Aware Gradient Optimization
- [文本条件下的音视频信息分解](../conferences/icml-2026/cards/1001-1100.md#fang26x-evaluation) · Towards Understanding Modality Interaction in Multimodal Language Models via Partial Information Decomposition
- [区分旧事实更新和未知事实学习](../conferences/icml-2026/cards/1101-1200.md#fu26c-evaluation) · MMKU-Bench: A Multimodal Update Benchmark for Diverse Visual Knowledge
- [多模态伪造的来源与事实双轴评测](../conferences/icml-2026/cards/1201-1300.md#gao26g-evaluation) · FakeWorld 1.0: An Omni-modal Benchmark for Fake Media and Content
- [文本知识编辑的图像迁移诊断](../conferences/icml-2026/cards/1201-1300.md#gao26ag-evaluation) · Do Text Edits Generalize to Visual Generation? Benchmarking Cross-Modal Knowledge Editing in UMMs
- [手机 GUI 代理的分能力诊断](../conferences/icml-2026/cards/1301-1400.md#gong26a-evaluation) · VenusBench-Mobile: A Challenging and User-Centric Benchmark for Mobile GUI Agents with Capability Diagnostics
- [图文一致的训练数据后门评测](../conferences/icml-2026/cards/1301-1400.md#guo26q-evaluation) · CBV: Clean-label Backdoor Attacks on Vision Language Models via Diffusion Models
- [网站开发的交互工作流验证](../conferences/icml-2026/cards/1501-1600.md#he26n-evaluation) · Vision2Web: A Hierarchical Benchmark for Visual Website Development with Agent Verification
- [对同一因果问题分别评估叙述和显式链](../conferences/icml-2026/cards/1501-1600.md#hoang26b-evaluation) · The Abstraction Gap in Vision-Language Causal Reasoning
- [在图像编辑评估中覆盖视觉指令](../conferences/icml-2026/cards/1601-1700.md#hou26h-evaluation) · When the Prompt Becomes Visual: Vision-Centric Jailbreak Attacks for Large Image Editing Models
- [从任务失败周期诊断隐藏视觉分块](../conferences/icml-2026/cards/1601-1700.md#hu26b-evaluation) · Steal the Patch Size: Adversarially Manipulate Vision Language Models
- [用逐模态数据复杂度和头部敲除诊断上下文迁移](../conferences/icml-2026/cards/1701-1800.md#huang26at-evaluation) · Dissecting Multimodal In-Context Learning: Modality Asymmetries and Circuit Dynamics in modern Transformers
- [用文字属性两端构造多模态排序轴](../conferences/icml-2026/cards/1801-1900.md#hyeon-woo26a-evaluation) · Zero-Shot Rankability: Revealing Latent Ordinal Structure in Multimodal Large Language Models via Language
- [拆开语音安全评审的模态贡献](../conferences/icml-2026/cards/1801-1900.md#ivry26a-evaluation) · LALM-as-a-Judge: Benchmarking Large Audio-Language Models for Safety Evaluation in Multi-Turn Spoken Dialogues
- [通过跨模态共享分区标识绑定证据](../conferences/icml-2026/cards/1801-1900.md#izadi26a-evaluation) · Uncovering Grounding IDs: How External Cues Shape Multi-Modal Binding
- [按视频评判熵筛动作渲染](../conferences/icml-2026/cards/1801-1900.md#ji26l-evaluation) · Zero-Shot Text-to-Motion Evaluation using Video Language Models
- [用逐模态移除辨别融合干扰](../conferences/icml-2026/cards/1801-1900.md#jia26a-evaluation) · VT-Bench: A Unified Benchmark for Visual-Tabular Multi-Modal Learning
- [用受控错误轨迹测视觉幻觉累积](../conferences/icml-2026/cards/1901-2000.md#jiang26t-evaluation) · MM-Snowball: Evaluating and Mitigating Hallucination Snowballing in Multimodal Multi-Turn Dialogue
- [先识别手写公式结构再转录符号](../conferences/icml-2026/cards/1901-2000.md#jiang26bg-evaluation) · Seeing Symbols, Missing Structure: A Real-World Handwritten Mathematical Expression Recognition Benchmark for Large Models
- [用独立条件拆解长提示文生图的失败](../conferences/icml-2026/cards/1901-2000.md#jiao26b-evaluation) · DetailMaster: Can Your Text-to-Image Model Handle Long Prompts?
- [先验证棋盘读数再测规则推理](../conferences/icml-2026/cards/1901-2000.md#jin26a-evaluation) · Seeing Without Understanding: Disentangling Perception, Reasoning, and Simulation in VLM Gameplay
- [在球面估计嵌入密度作不确定性代理](../conferences/icml-2026/cards/2001-2100.md#ju26b-evaluation) · Epistemic Uncertainty Quantification for Pre-trained VLMs via Riemannian Flow Matching
- [用因果补丁定位跨模态注意力汇点](../conferences/icml-2026/cards/2001-2100.md#jung26c-evaluation) · Probing Cross-modal Information Hubs in Audio-Visual LLMs
- [用注意力特征摊销推理中的区域消融归因](../conferences/icml-2026/cards/2001-2100.md#kang26d-evaluation) · Real-Time Visual Attribution Streaming in Thinking Model

<a id="by-ml-foundations"></a>

### 机器学习基础与统计

- [交互式评测](../conferences/icml-2026/cards/0001-0100.md#agrawal26b-evaluation) · A Benchmark and Framework for Evaluating Next Action Predictions in Spreadsheets
- [表征相似性](../conferences/icml-2026/cards/0001-0100.md#almudevar26a-evaluation) · Bridging Functional and Representational Similarity via Usable Information
- [机制可解释性](../conferences/icml-2026/cards/0001-0100.md#anani26a-evaluation) · Certified Circuits: Stability Guarantees for Mechanistic Circuits
- [参数扰动稳健性](../conferences/icml-2026/cards/0101-0200.md#arpit26a-evaluation) · TPV: Parameter Perturbations Through the Lens of Test Prediction Variance
- [模型拼接评测](../conferences/icml-2026/cards/0101-0200.md#athanasiadis26a-evaluation) · Grounding Functional Similarity by Invariance-Aware Model Stitching
- [影响函数](../conferences/icml-2026/cards/0101-0200.md#bado26a-evaluation) · Clustered Influence Functions
- [表格基础模型](../conferences/icml-2026/cards/0101-0200.md#balef26a-evaluation) · Is One Layer Enough? Understanding Inference Dynamics in Tabular Foundation Models
- [时序基础模型压缩](../conferences/icml-2026/cards/0201-0300.md#bao26c-evaluation) · Universal Redundancies in Time Series Foundation Models
- [可验证模型解释](../conferences/icml-2026/cards/0301-0400.md#boetius26a-evaluation) · Verified SHAP: Provable Bounds for Exact Shapley Values of Neural Networks
- [人评聚合](../conferences/icml-2026/cards/0301-0400.md#bonagiri26a-evaluation) · STABLEVAL: Disagreement-Aware and Stable Evaluation of AI Systems
- [共形覆盖诊断](../conferences/icml-2026/cards/0301-0400.md#braun26c-evaluation) · Conditional Coverage Diagnostics for Conformal Prediction
- [榜单评测前的统一微调](../conferences/icml-2026/cards/0601-0700.md#chen26gf-evaluation) · Leaderboard Incentives: Model Rankings under Strategic Post-Training
- [用合成记忆任务诊断可塑性](../conferences/icml-2026/cards/0601-0700.md#cheng26i-evaluation) · Local Redundancy: An Information-Theoretic Measure of Plasticity from Synthetic Memorization
- [元胞自动机可学习性的频谱诊断](../conferences/icml-2026/cards/0901-1000.md#disselhoff26a-evaluation) · Probing the Inductive Bias of Neural Networks through Learning Random Cellular Automata
- [按数据结构难度诊断聚类](../conferences/icml-2026/cards/0901-1000.md#durani26a-evaluation) · CHB: A Diagnostic Toolkit for Hardness-Aware Clustering Evaluation
- [序列状态跟踪的跨长度共享诊断](../conferences/icml-2026/cards/1001-1100.md#ebrahimi26a-evaluation) · On the "Induction Bias" in Sequence Models
- [沿 AdamW 训练路径联合归因](../conferences/icml-2026/cards/1001-1100.md#eichin26a-evaluation) · ExPLAIND: Unifying Model, Data, and Training Attribution to Study Model Behavior
- [时序预测的分频可预测性诊断](../conferences/icml-2026/cards/1101-1200.md#feng26u-evaluation) · Beyond Model Ranking: Predictability-Aligned Evaluation for Time Series Forecasting
- [评分模型的架构各向异性](../conferences/icml-2026/cards/1101-1200.md#floros26a-evaluation) · On the Anisotropy of Score-Based Generative Models
- [分布式数据归因的操纵鲁棒性](../conferences/icml-2026/cards/1201-1300.md#gao26k-evaluation) · On the Fragility of Data Attribution When Learning Is Distributed
- [条件生成的保形可靠性评分](../conferences/icml-2026/cards/1201-1300.md#gao26aa-evaluation) · Conformal Reliability: A New Evaluation Metric for Conditional Generation
- [扩散生成的训练样本邻近偏差](../conferences/icml-2026/cards/1201-1300.md#garnier-brun26a-evaluation) · Biased Generalization in Diffusion Models
- [程序化算法发现任务](../conferences/icml-2026/cards/1201-1300.md#goldie26a-evaluation) · Procedural Generation Of Algorithm Discovery Tasks in Machine Learning
- [表征相似度的置换零校准](../conferences/icml-2026/cards/1301-1400.md#groger26a-evaluation) · Revisiting the Platonic Representation Hypothesis: An Aristotelian View
- [按决策收益度量解释价值](../conferences/icml-2026/cards/1301-1400.md#guo26u-evaluation) · Explanations are a Means to an End: Decision Theoretic Explanation Evaluation
- [时间序列预测的频域稳健性评测](../conferences/icml-2026/cards/1401-1500.md#han26d-evaluation) · TSFAdv: Frequency-Guided Black-Box Adversarial Attacks on Time Series Forecasting
- [把图结构比较与免通道对齐的权重比较结合](../conferences/icml-2026/cards/1601-1700.md#hu26ap-evaluation) · An In-Depth Study on Deep Learning Model Cloning
- [按估分与找失败的目标分配测试](../conferences/icml-2026/cards/1701-1800.md#huang26bw-evaluation) · ProEval: Proactive Failure Discovery and Efficient Performance Estimation for Generative AI Evaluation
- [用全局兼容性筛查局部因果陈述](../conferences/icml-2026/cards/1801-1900.md#jahn26a-evaluation) · Evaluating Bivariate Causal Statements Based on Mutual Compatibility
- [把预文本假设拆成三种可测失效](../conferences/icml-2026/cards/1801-1900.md#jia26b-evaluation) · Quantitative Estimation of Target Task Performance from Unsupervised Pretext Task in Semi/Self-Supervised Learning
- [从预测分布到条件经验分布做非参数校准](../conferences/icml-2026/cards/2001-2100.md#jung26d-evaluation) · Nonparametric Distribution Regression Re-calibration
- [给每个分类错误赋予实例级损失权重](../conferences/icml-2026/cards/2001-2100.md#kang26m-evaluation) · Instance-Level Costs for Nuanced Classifier Evaluation
- [按不可约噪声分层评估表格模型](../conferences/icml-2026/cards/2001-2100.md#kartashev26a-evaluation) · Unveiling the Role of Data Uncertainty in Tabular Deep Learning
- [用统一搜索预算比较认证训练的整条前沿](../conferences/icml-2026/cards/2001-2100.md#kaulen26a-evaluation) · Rethinking Evaluation Paradigms in IBP-based Certified Training
- [在可逆频谱或趋势域内积分梯度](../conferences/icml-2026/cards/2001-2100.md#kechris26a-evaluation) · Time series saliency maps: Explaining models across multiple domains
- [借可信参考样本诊断异常输出机制](../conferences/icml-2026/cards/2001-2100.md#keenan26a-evaluation) · Mechanistic Anomaly Detection via Functional Attribution

<a id="by-graph-and-recommendation"></a>

### 图学习与推荐

- [图模型隐私评测](../conferences/icml-2026/cards/0001-0100.md#agbaje26a-evaluation) · Revisiting Asymmetries in Black-box Link Stealing against Graph Neural Networks
- [图模型迁移](../conferences/icml-2026/cards/0001-0100.md#akula26a-evaluation) · Same Graph Cross-Task Transfer in GNNs: Protocols and Predictors
- [缺失节点特征的压力测试](../conferences/icml-2026/cards/1101-1200.md#ferrini26a-evaluation) · Rethinking GNNs and Missing Features: Challenges, Evaluation and a Robust Solution
- [图 Mixup 插值质量诊断](../conferences/icml-2026/cards/1101-1200.md#forbat26a-evaluation) · Is Graph Mixup Beneficial? Investigating Interpolation And Empirical Performance of Graph Mixup Methods
- [多模态推荐的同步污染诊断](../conferences/icml-2026/cards/1301-1400.md#guan26b-evaluation) · VENOMREC: Cross-Modal Interactive Poisoning for Targeted Promotion in Multimodal LLM Recommender Systems
- [用图对齐替身摊薄重复归因开销](../conferences/icml-2026/cards/1501-1600.md#heidari26a-evaluation) · TN-SHAP-G: Graph-Structured Tensor Network Surrogates for Shapley Values and Interactions

<a id="by-scientific-ml"></a>

### 科学机器学习

- [时间序列预测评测](../conferences/icml-2026/cards/0001-0100.md#ahamed26a-evaluation) · TFRBench: A Reasoning Benchmark for Evaluating Forecasting Systems
- [格密码机器学习分析](../conferences/icml-2026/cards/0001-0100.md#alfarano26a-evaluation) · Improving ML Attacks on LWE with Data Repetition and Stepwise Regression
- [恶意软件谱系重建](../conferences/icml-2026/cards/0001-0100.md#amalan26a-evaluation) · MalTree: Tracing Malware Evolution from Embeddings at Scale
- [生存模型评测](../conferences/icml-2026/cards/0101-0200.md#bahrini26a-evaluation) · When Can We Trust Survival Model Evaluation ?
- [CAD 操作评测](../conferences/icml-2026/cards/0101-0200.md#bai26a-evaluation) · Op-CAD: Benchmarking and Investigating Operation-oriented CAD Generation
- [流体控制强化学习](../conferences/icml-2026/cards/0201-0300.md#becktepe26a-evaluation) · Plug-and-Play Benchmarking of Reinforcement Learning Algorithms for Large-Scale Flow Control
- [仿真 Agent 成本评测](../conferences/icml-2026/cards/0301-0400.md#cao26g-evaluation) · SimulCost: A Cost-Aware Benchmark and Toolkit for Automating Physics Simulations with LLMs
- [科学标注行为克隆](../conferences/icml-2026/cards/0401-0500.md#chandok26a-evaluation) · A Systematic Study of Behavioral Cloning for Scientific Data Annotation
- [自然感官数据的跨刺激神经预测](../conferences/icml-2026/cards/0601-0700.md#chen26fp-evaluation) · Real-World Unsupervised Models Generalize to Predict Brain Responses to Out-of-Distribution Stimuli
- [语言与语音层表征的脑响应对齐](../conferences/icml-2026/cards/0601-0700.md#cheng26l-evaluation) · Abstraction Induces the Brain Alignment of Language and Speech Models
- [长程脑电癫痫检测的泛化评测](../conferences/icml-2026/cards/0801-0900.md#dan26a-evaluation) · Quantifying the Generalization Gap in Seizure Detection: A Large-Scale Empirical Benchmark via the SzCORE Challenge
- [蛋白适应度的外推切分](../conferences/icml-2026/cards/0801-0900.md#didi26a-evaluation) · FLIP2: Expanding Protein Fitness Landscape Benchmarks for Real-World Machine Learning Applications
- [生物基础模型的双类扰动诊断](../conferences/icml-2026/cards/0901-1000.md#duan26f-evaluation) · (Be Cautious!) Bio-Foundation Models Are Not Yet Robust to Biologically Plausible Perturbations and ML Transformations
- [生物信息学智能体的流程稳健性评测](../conferences/icml-2026/cards/1001-1100.md#fa26a-evaluation) · BioAgent Bench: An AI Agent Evaluation Suite for Bioinformatics
- [按轮次回放蛋白工程候选筛选](../conferences/icml-2026/cards/1201-1300.md#gao26ao-evaluation) · TadA-Bench: A Million-Variant Benchmark for Future-Round Discovery Toward Agentic Protein Engineering
- [多语言医疗模型的分维度可信评测](../conferences/icml-2026/cards/1201-1300.md#ghosh26b-evaluation) · CLINIC : Evaluating Multilingual Trustworthiness in Language Models for Healthcare
- [视觉皮层映射的神经样本缩放](../conferences/icml-2026/cards/1201-1300.md#gokce26a-evaluation) · Multimodal Scaling Laws for Task & Data-Optimized Models of Visual Cortex
- [站点天气预报的物理与业务对照](../conferences/icml-2026/cards/1401-1500.md#han26v-evaluation) · Benchmarking Physics-Informed Time-Series Models for Operational Global Station Weather Forecasting
- [同时核对反演代理的物理耦合和速度](../conferences/icml-2026/cards/1501-1600.md#he26ay-evaluation) · MMPD-Bench: Bridging Multimodal Fission with Multi-Polarimetric Modalities Decomposition
<!-- classification:end -->
