# 评测与诊断

[首页](../README.md) · [English](../en/insights/evaluation.md)

基准、评测协议、消融与失效诊断。

<!-- classification:start -->
## 按研究领域浏览

[大语言模型](#by-llm) · [计算机视觉](#by-computer-vision) · [自然语言处理](#by-nlp) · [强化学习](#by-reinforcement-learning) · [机器人学](#by-robotics) · [多模态学习](#by-multimodal) · [机器学习基础与统计](#by-ml-foundations) · [图学习与推荐](#by-graph-and-recommendation) · [科学机器学习](#by-scientific-ml)

<a id="by-llm"></a>

### 大语言模型

- [一致性训练](../conferences/icml-2026/cards/0001-0100.md#africa26a-evaluation) · Consistency Training Can Entrench Misalignment
- [形式化证明评测](../conferences/icml-2026/cards/0001-0100.md#ammanamanchi26a-evaluation) · Faults in Our Formal Benchmarking: Dataset Defects and Evaluation Failures in Lean Theorem Proving
- [归纳头形成](../conferences/icml-2026/cards/0101-0200.md#aoyama26a-evaluation) · Predicting the Emergence of Induction Heads in Language Model Pretraining
- [隐性偏差审计](../conferences/icml-2026/cards/0101-0200.md#arcuschin26a-evaluation) · Biases in the Blind Spot: Detecting What LLMs Fail to Mention
- [推理忠实性](../conferences/icml-2026/cards/0101-0200.md#arcuschin26b-evaluation) · Chain-of-Thought Reasoning In The Wild Is Not Always Faithful
- [语言模型电路](../conferences/icml-2026/cards/0101-0200.md#arora26c-evaluation) · Language Model Circuits Are Sparse in the Neuron Basis
- [对齐行为诊断](../conferences/icml-2026/cards/0101-0200.md#baek26d-evaluation) · Sycophancy Towards Researchers Drives Performative Misalignment
- [机制可解释性](../conferences/icml-2026/cards/0101-0200.md#bair26a-evaluation) · Compressed Sensing for Capability Localization in Large Language Models
- [形式化证明评测](../conferences/icml-2026/cards/0101-0200.md#baksys26a-evaluation) · miniF2F-Dafny: LLM-Guided Mathematical Theorem Proving via Auto-Active Verification
- [相关裁判聚合](../conferences/icml-2026/cards/0101-0200.md#balasubramanian26a-evaluation) · Dependence-Aware Label Aggregation for LLM-as-a-Judge via Ising Models
- [推理忠实性](../conferences/icml-2026/cards/0301-0400.md#boppana26a-evaluation) · Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought
- [稀疏自编码器可解释性](../conferences/icml-2026/cards/0401-0500.md#chanin26a-evaluation) · Sparse but Wrong: Incorrect L0 Leads to Incorrect Features in Sparse Autoencoders
- [LLM API 变化检测](../conferences/icml-2026/cards/0401-0500.md#chauvin26a-evaluation) · Token-Efficient Change Detection in LLM APIs
- [幻觉逐步定位](../conferences/icml-2026/cards/0401-0500.md#chen26n-evaluation) · Mind the Gap: Catching Hallucinations via Evidence Drop on the Reasoning Manifold
- [RLVR 的难学样本](../conferences/icml-2026/cards/0501-0600.md#chen26aq-evaluation) · The Unlearnability Phenomenon in RLVR for Language Models
- [机制电路的非唯一性](../conferences/icml-2026/cards/0501-0600.md#chen26bb-evaluation) · All Circuits Lead to Rome: Rethinking Functional Anisotropy in Circuit and Sheaf Discovery for LLMs
- [对齐奖励的隐含目标诊断](../conferences/icml-2026/cards/0501-0600.md#chen26bg-evaluation) · Discovering Implicit Large Language Model Alignment Objectives
- [可解释注意力头的训练数据归因](../conferences/icml-2026/cards/0501-0600.md#chen26cv-evaluation) · Mechanistic Data Attribution: Tracing the Training Origins of Interpretable LLM Units
- [用逐层预测变化衡量推理投入](../conferences/icml-2026/cards/0501-0600.md#chen26di-evaluation) · Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens
- [代码生成的诈骗链接审计](../conferences/icml-2026/cards/0501-0600.md#chen26dp-evaluation) · Scam2Prompt: A Scalable Framework for Auditing Malicious Scam Endpoints in Production LLMs
- [分块低比特量化格式比较](../conferences/icml-2026/cards/0601-0700.md#chen26fa-evaluation) · INT vs. FP: A Comprehensive Study of Fine-Grained Low-bit Quantization Formats
- [语言模型强化学习的采样预算分配](../conferences/icml-2026/cards/0601-0700.md#cheng26n-evaluation) · IsoCompute Playbook: Optimally Scaling Sampling Compute for LLM RL
- [续写分布的语义与机制聚类](../conferences/icml-2026/cards/0701-0800.md#cho26g-evaluation) · Shared Semantics, Divergent Mechanisms: Unsupervised Feature Discovery by Aligning Semantics and Mechanisms
- [冻结演化轨迹的反馈归因](../conferences/icml-2026/cards/0701-0800.md#chong26b-evaluation) · Towards Feedback-to-Plan Decisions for Self-Evolving LLM Agents in CUDA Kernel Generation
- [图路径诊断推理幻觉](../conferences/icml-2026/cards/0801-0900.md#dai26k-evaluation) · When Do Hallucinations Arise? A Graph Perspective on the Evolution of Path Reuse and Path Compression
- [多模型投票的相关错误诊断](../conferences/icml-2026/cards/0801-0900.md#denisov-blanch26a-evaluation) · Truthfulness Does Not Scale Like Reasoning: Why Polling Fails as a Proxy Verifier
- [可切换适配器的模型自审计](../conferences/icml-2026/cards/0801-0900.md#dietz26a-evaluation) · Split Personality Training: Revealing Latent Knowledge Through Alternate Personalities
- [RLVR 训练目标劫持诊断](../conferences/icml-2026/cards/0901-1000.md#dong26b-evaluation) · Probing RLVR Training Instability through the Lens of Objective-Level Hacking
- [用成对推理比较降低评测方差](../conferences/icml-2026/cards/0901-1000.md#dong26o-evaluation) · Evaluating LLMs When They Do Not Know the Answer: Statistical Evaluation of Mathematical Reasoning via Comparative Signals
- [用超额描述长度区分能力诱发与学习](../conferences/icml-2026/cards/0901-1000.md#donoway26a-evaluation) · Bits That Count: Quantifying and Predicting Capabilities of Language Models
- [语言模型罕见事件的重要性估计](../conferences/icml-2026/cards/0901-1000.md#dorman26a-evaluation) · Rare Event Analysis of Large Language Models
- [奖励模型偏差的激活投影](../conferences/icml-2026/cards/1001-1100.md#fein26a-evaluation) · One Bias After Another: Mechanistic Reward Shaping and Persistent Biases in Language Reward Models
- [外部技能组合的后门评测](../conferences/icml-2026/cards/1001-1100.md#feng26c-evaluation) · SkillTrojan: Backdoor Attacks on Skill-Based Agent Systems
- [推理链的失败步骤比例](../conferences/icml-2026/cards/1101-1200.md#feng26e-evaluation) · What Characterizes Effective Reasoning? Revisiting Length, Review, and Structure of CoT
- [关系推理的元数控制评测](../conferences/icml-2026/cards/1101-1200.md#fesser26a-evaluation) · Evaluating Relational Reasoning in LLMs with REL
- [注意力奇异向量的特征对齐诊断](../conferences/icml-2026/cards/1101-1200.md#franco26a-evaluation) · Singular Vectors of Attention Heads Align with Features
- [幻灯片代理任务的分项评分](../conferences/icml-2026/cards/1201-1300.md#gandhi26a-evaluation) · PPT-Eval: A Benchmark for Computer-Use Agents on PowerPoint Tasks
- [长上下文中少量困难干扰的影响](../conferences/icml-2026/cards/1201-1300.md#gao26b-evaluation) · The First Drop of Ink: Nonlinear Impact of Distracting Information in Long-Context Reasoning
- [权重稀疏模型的电路提取](../conferences/icml-2026/cards/1201-1300.md#gao26w-evaluation) · Weight-sparse transformers have interpretable circuits
- [词元扰动的成分响应分析](../conferences/icml-2026/cards/1301-1400.md#gordon26a-evaluation) · Towards Spectroscopy: Susceptibility Clusters in Language Models
- [表格语言模型的任务级泄漏核查](../conferences/icml-2026/cards/1301-1400.md#gorla26a-evaluation) · The Illusion of Generalization in Tabular Language Models
- [智能体对训练接口的依赖诊断](../conferences/icml-2026/cards/1301-1400.md#gu26g-evaluation) · What Do Agents Learn from Trajectory-SFT: Semantics or Interfaces?
- [跨推理框架的静默错误定位](../conferences/icml-2026/cards/1301-1400.md#gu26q-evaluation) · Ekka: Automated Diagnosis of Silent Errors in LLM Inference
- [工具故障下的智能体失败披露评测](../conferences/icml-2026/cards/1301-1400.md#guo26k-evaluation) · Are Your Agents Upward Deceivers?
- [部署实例的伪随机指纹](../conferences/icml-2026/cards/1401-1500.md#gurvan26a-evaluation) · FLIPS: Instance-Fingerprinting for LLMs via Pseudo-random Sequences
- [多智能体安全的分阶段评测](../conferences/icml-2026/cards/1401-1500.md#hagag26a-evaluation) · Architecture Matters for Multi-Agent Security
- [异质偏好的局部稳定排行榜](../conferences/icml-2026/cards/1401-1500.md#haghtalab26a-evaluation) · Pluralistic Leaderboards
- [从旋转频率核识别长上下文注意力头](../conferences/icml-2026/cards/1401-1500.md#han26e-evaluation) · Revealing Long-context Potential of Attention Heads via Frequency Kernels
- [语言模型自述人格的行为验证](../conferences/icml-2026/cards/1401-1500.md#han26n-evaluation) · The Personality Illusion: Revealing Dissociation Between Self-Reports & Behavior in LLMs
- [内生和提示诱发价值的机制分解](../conferences/icml-2026/cards/1401-1500.md#han26q-evaluation) · Dual Mechanisms of Value Expression: Intrinsic vs. Prompted Values in Large Language Models
- [分层测量剪枝造成的生成漂移](../conferences/icml-2026/cards/1501-1600.md#he26ag-evaluation) · Demystifying When Pruning Works via Representation Hierarchies
- [将注入执行和原文保真分别评测](../conferences/icml-2026/cards/1501-1600.md#hermon26a-evaluation) · Security–Fidelity Tradeoffs: The Hidden Cost of Prompt Injection Defense
- [放大推理任务向量进行白盒审计](../conferences/icml-2026/cards/1501-1600.md#hopkins26a-evaluation) · Overthinking: Amplifying Reasoning Weights to Extract Learned Secrets
- [从因果激活轨迹识别拒答失稳](../conferences/icml-2026/cards/1601-1700.md#hu26ax-evaluation) · Tracing the Dynamics of Refusal: Exploiting Latent Refusal Trajectories for Robust Jailbreak Detection
- [把采样来源与训练损失交叉消融](../conferences/icml-2026/cards/1601-1700.md#huan26a-evaluation) · Does Math Reasoning Improve General LLM Capabilities? Understanding Transferability of LLM Reasoning
- [先精确反编译再按因果效应剪枝](../conferences/icml-2026/cards/1601-1700.md#huang26b-evaluation) · Discovering Interpretable Algorithms by Decompiling Transformers to RASP
- [用改写压力测试词元水印的概率裕量](../conferences/icml-2026/cards/1701-1800.md#hwang26e-evaluation) · LLM Watermark Evasion via Bias Inversion
- [用随机记分标签设置污染检验上限](../conferences/icml-2026/cards/1801-1900.md#ishida26a-evaluation) · CapBencher: Give Your LLM Benchmark a Built-in Alarm for Test-Set Overfitting
- [用独立方式区分能力缺失和探索受抑](../conferences/icml-2026/cards/1801-1900.md#jang26b-evaluation) · Exploration Hacking: Can LLMs Learn to Resist RL Training?
- [按路由干预诊断 MoE 安全集中性](../conferences/icml-2026/cards/1901-2000.md#jiang26o-evaluation) · Sparse Models, Sparse Safety: Unsafe Routes in Mixture-of-Experts LLMs
- [分开评测代理的环境识别和拒绝](../conferences/icml-2026/cards/1901-2000.md#jones26a-evaluation) · A New Framework for Cybersecurity Refusals in AI Agents
- [将数据影响沿循环计算的各步展开](../conferences/icml-2026/cards/2001-2100.md#kaissis26a-evaluation) · Step-Resolved Data Attribution for Looped Transformers
- [用临时中层读出测试特征可达性](../conferences/icml-2026/cards/2001-2100.md#kang26r-evaluation) · Capacity without Access: Reinterpreting the Mid-Depth Spectral Plateau in LLMs
- [把内层激活读出训练成可提问接口](../conferences/icml-2026/cards/2001-2100.md#karvonen26a-evaluation) · Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers
- [对偏好子群分布做鲁棒模型混合](../conferences/icml-2026/cards/2001-2100.md#khalaf26a-evaluation) · Robust AI Evaluation through Maximal Lotteries
- [固定迭代和成本再测多代理的贡献](../conferences/icml-2026/cards/2101-2200.md#kim26ba-evaluation) · Investigating Component Contributions in Multi-Agent ML Systems
- [沿词元轨迹子空间验证几何与熵的联系](../conferences/icml-2026/cards/2101-2200.md#king26a-evaluation) · Representational Curvature Modulates Behavioral Uncertainty in Large Language Models
- [在快检不明确的区间调用强检](../conferences/icml-2026/cards/2101-2200.md#kiyani26a-evaluation) · When to Trust the Cheap Check: Weak and Strong Verification for Reasoning
- [用控制训练变量检验谱指标的预测力](../conferences/icml-2026/cards/2201-2300.md#kulkarni26c-evaluation) · Disentangling Geometry, Performance, and Training in Language Models
- [用位置干预追踪口头置信度从哪里读出](../conferences/icml-2026/cards/2201-2300.md#kumaran26a-evaluation) · How do LLMs Compute Verbal Confidence?
- [先逐特征解释再汇总专家路由](../conferences/icml-2026/cards/2201-2300.md#lasy26a-evaluation) · RouterInterp: Understanding Superposed Specialisation in Mixture of Experts Routing
- [将特征触发路径与输出影响分开追踪](../conferences/icml-2026/cards/2301-2400.md#lee26a-evaluation) · Query Lens: Interpreting Sparse Key-Value Features with Indirect Effects
- [用成对协方差差分分解关系分数](../conferences/icml-2026/cards/2301-2400.md#lee26b-evaluation) · Decomposing Query-Key Feature Interactions Using Contrastive Covariances
- [用每字节损失比较不同分词的算力前沿](../conferences/icml-2026/cards/2301-2400.md#lee26bh-evaluation) · The Efficiency Gap in Byte Modeling
- [让目标模型和描述器持有冲突知识](../conferences/icml-2026/cards/2401-2500.md#li26k-evaluation) · Do Activation Verbalization Methods Convey Privileged Information?
- [可执行风险场景的逻辑与叙事分离](../conferences/icml-2026/cards/2501-2600.md#li26dy-evaluation) · AutoControl Arena: Synthesizing Executable Test Environments for Frontier AI Risk Evaluation
- [语义保持表示上的回答不确定性](../conferences/icml-2026/cards/2501-2600.md#li26eb-evaluation) · Gradients with Respect to Semantics Preserving Embeddings Tell the Uncertainty of Large Language Models
- [用信息剖面对照评测集体推理](../conferences/icml-2026/cards/2501-2600.md#li26ej-evaluation) · Systematic Failures in Collective Reasoning under Distributed Information in Multi-Agent LLMs
- [用滤过推理任务拆开图拓扑能力](../conferences/icml-2026/cards/2501-2600.md#li26gg-evaluation) · Large Language Models as Topological Thinkers: A Benchmark on Graph Persistent Homology
- [按环境状态测复杂工具任务](../conferences/icml-2026/cards/2601-2700.md#li26ij-evaluation) · ComplexMCP: Evaluation of LLM Agents in Dynamic, Interdependent, and Large-Scale Tool Sandbox
- [在工具接入时用模拟多轮测试生成安全经验](../conferences/icml-2026/cards/2601-2700.md#li26is-evaluation) · Unsafer in Many Turns: Benchmarking and Defending Multi-Turn Safety Risks in Tool-Using Agents
- [开放任务的证据依赖评分](../conferences/icml-2026/cards/2701-2800.md#lin26z-evaluation) · JADE: Expert-Grounded Dynamic Evaluation for Open-Ended Professional Tasks
- [用激活干预测试候选推理原语](../conferences/icml-2026/cards/2701-2800.md#lippl26a-evaluation) · AlgoTrace: Algorithmic Primitives and Compositional Geometry of Reasoning in Language Models
- [用多条正确轨迹的结构共识定位推理错误](../conferences/icml-2026/cards/2801-2900.md#liu26u-evaluation) · Diagnosing Multi-step Reasoning Failures in Black-box LLMs via Stepwise Confidence Attribution
- [真实 LoRA 回收的等数据对照](../conferences/icml-2026/cards/2801-2900.md#liu26bh-evaluation) · The Appeal and Reality of Recycling LoRAs with Adaptive Merging
- [将未知答案设为 Lean 元变量并附证明义务](../conferences/icml-2026/cards/2901-3000.md#liu26gl-evaluation) · Beyond Theorem Proving: Formulation, Framework and Benchmark for Formal Problem-Solving
- [可执行漏洞修复任务构建](../conferences/icml-2026/cards/3001-3100.md#luo26aj-evaluation) · CVE-Factory: Scaling Expert-Level Agentic Tasks for Code Security Vulnerability
- [配对评测降低最佳模型识别成本](../conferences/icml-2026/cards/3101-3200.md#lyu26h-evaluation) · Cutting LLM Evaluation Costs with SySRs: A Bandit Algorithm That Provably Exploits Model Similarity
- [用反例和语义保持改写检验稀疏特征是否真表征推理](../conferences/icml-2026/cards/3101-3200.md#ma26v-evaluation) · Do Sparse Autoencoders Identify Reasoning Features in Language Models?
- [激活异常检测与概念识别](../conferences/icml-2026/cards/3101-3200.md#macar26a-evaluation) · Mechanisms of Introspective Awareness
- [用反事实增量测自我解释的预测价值](../conferences/icml-2026/cards/3201-3300.md#mayne26a-evaluation) · A Positive Case for Faithfulness: LLM Self-Explanations Help Predict Model Behavior
- [持续激活干预下区分重试和有效纠正](../conferences/icml-2026/cards/3201-3300.md#mckenzie26a-evaluation) · Endogenous Resistance to Activation Steering in Language Models
- [因果电路稳定性](../conferences/icml-2026/cards/3201-3300.md#meloux26a-evaluation) · Mechanistic Interpretability as Statistical Estimation: A Variance Analysis
- [用已知复杂度检验动态深度分配](../conferences/icml-2026/cards/3301-3400.md#moosa26a-evaluation) · Understanding Dynamic Compute Allocation in Recurrent Transformers
- [以短题面和依赖图测试长推理](../conferences/icml-2026/cards/3301-3400.md#motwani26a-evaluation) · LongCoT: Benchmarking Long-Horizon Chain-of-Thought Reasoning
- [压低候选多样性的推理安全压力测试](../conferences/icml-2026/cards/3401-3500.md#nahin26a-evaluation) · Less Diverse, Less Safe: The Indirect But Pervasive Risk of Test-Time Scaling in Large Language Models
- [提示线索算法偏移](../conferences/icml-2026/cards/3401-3500.md#narula26a-evaluation) · The Invisible Lottery: How Subtle Cues Steer Algorithm Choice in LLM Code Generation
- [词元重复概率检测](../conferences/icml-2026/cards/3401-3500.md#nassif26a-evaluation) · Telescope: Improving Zero Shot Detection of LLM Generated Content By Measuring Token Repetition Probability
- [情景特定欺骗探针](../conferences/icml-2026/cards/3401-3500.md#natarajan26a-evaluation) · One Probe Won’t Catch Them All: Towards Targeted Deception Detection
- [定向指令选择拆解](../conferences/icml-2026/cards/3401-3500.md#nayak26a-evaluation) · A Critical Look at Targeted Instruction Selection: Disentangling What Matters (and What Doesn’t)
- [按模型输入信念测试解释充分性](../conferences/icml-2026/cards/3401-3500.md#nguyen26n-evaluation) · What LLMs Explain Is Not What They Believe: Evaluating Explanation Sufficiency Under Models’ Own Input Beliefs
- [用执行环境和数据依赖过滤评估数据科学 Agent](../conferences/icml-2026/cards/3401-3500.md#nie26b-evaluation) · DSGym: A Holistic Framework for Evaluating and Training Data Science Agents
- [辩论群体偏向](../conferences/icml-2026/cards/3501-3600.md#okawa26a-evaluation) · Emergence of Biased Consensus in Multi-Agent LLM Debates
- [从题内差异估计多项选择的长度偏差](../conferences/icml-2026/cards/3501-3600.md#oostermeijer26a-evaluation) · Accuracy and Normalized Accuracy under Length Bias: Analysis, Guidelines, and a Bayesian Alternative
- [推理片段递归归因](../conferences/icml-2026/cards/3501-3600.md#pan26g-evaluation) · Towards Long-Horizon Interpretability: Efficient and Faithful Multi-Token Attribution for Reasoning LLMs
- [以检查点反传校准省显存训练的对照](../conferences/icml-2026/cards/3501-3600.md#panchal26a-evaluation) · Memory Savings at What Cost? A Study of Alternatives to Backpropagation
- [用专家身份干预拆解团队协同损失](../conferences/icml-2026/cards/3501-3600.md#pappu26a-evaluation) · Multi-Agent Teams Hold Experts Back
- [真假数学命题成对评测](../conferences/icml-2026/cards/3601-3700.md#petrov26a-evaluation) · BrokenMath: A Benchmark for Sycophancy in Theorem Proving with LLMs
- [干预注意力头的时间重现方向](../conferences/icml-2026/cards/3601-3700.md#pink26a-evaluation) · Temporal Context Reinstatement Drives Episodic-Like Order Memory in Long-Context Language Models
- [用图任务分离低温推理循环机制](../conferences/icml-2026/cards/3601-3700.md#pipis26a-evaluation) · Wait, Wait, Wait... Why Do Reasoning Models Loop?
- [用等时长控制与细分能力探针审计 DPO](../conferences/icml-2026/cards/3601-3700.md#pollanen26a-evaluation) · Capability Traps in DPO
- [同时测记忆泄漏迎合和有用调用](../conferences/icml-2026/cards/3601-3700.md#pulipaka26a-evaluation) · PersistBench: When Should Long-Term Memories Be Forgotten by LLMs?
- [从词组交互测提示敏感性](../conferences/icml-2026/cards/3701-3800.md#qin26i-evaluation) · Evaluating and Explaining Prompt Sensitivity of LLMs Using Interactions
- [按曝光时机拆解选项线索](../conferences/icml-2026/cards/3801-3900.md#raman26a-evaluation) · Reasoning Models Are Test Exploiters: Rethinking Multiple Choice
- [按多次采样的最高泄漏评估遗忘](../conferences/icml-2026/cards/3801-3900.md#reisizadeh26a-evaluation) · Leak@$k$: Unlearning Does Not Make LLMs Forget Under Probabilistic Decoding
- [用同题偏好校验弱裁判的排名](../conferences/icml-2026/cards/3801-3900.md#remeli26a-evaluation) · Correct Looks Better: Pairwise Comparisons Reveal Accuracy Rankings
- [按连续编辑负载测权重编辑的推理退化](../conferences/icml-2026/cards/3801-3900.md#ren26p-evaluation) · Revisiting Parameter-Based Knowledge Editing in Large Language Models: Theoretical Limits and Empirical Evidence
- [用逐题同结果代理校准自偏好](../conferences/icml-2026/cards/3801-3900.md#roytburg26a-evaluation) · Are LLM Evaluators Really Narcissists? Sanity Checking Self-Preference Evaluations
- [同时比较扩散语言模型的似然扩展和生成效率](../conferences/icml-2026/cards/3901-4000.md#sahoo26a-evaluation) · Scaling Beyond Masked Diffusion Language Models
- [在攻击与受测模型分层校准裁判](../conferences/icml-2026/cards/3901-4000.md#schwinn26a-evaluation) · A Coin Flip for Safety: LLM Judges Fail to Reliably Measure Adversarial Robustness
- [把实验结果准确率与自报可预测性一起测](../conferences/icml-2026/cards/3901-4000.md#sehwag26a-evaluation) · SciPredict: Can LLMs Predict the Outcomes of Scientific Experiments in Natural Sciences?
- [用激活判别复核微调接口安全性](../conferences/icml-2026/cards/3901-4000.md#sel26a-evaluation) · Trojan-Speak: Bypassing Constitutional Classifiers with No Jailbreak Tax via Adversarial Finetuning
- [校准罕见动作频率以估计安全抽检的盲区](../conferences/icml-2026/cards/4001-4100.md#serrano26b-evaluation) · Frontier Models Can Take Actions at Low Probabilities
- [用评分衰减曲线定位细则缺口](../conferences/icml-2026/cards/4001-4100.md#sharma26b-evaluation) · RubricRobustness: Evaluating the Sensitivity of Rubrics-Based Benchmarks to Simple Perturbations
- [多轮旅行规划及逐轮奖励评测](../conferences/icml-2026/cards/4001-4100.md#shen26j-evaluation) · TRIP-Bench: A Benchmark for Long-Horizon Interactive Agents in Real-World Scenarios
- [用行为已知的模型群校准自我报告](../conferences/icml-2026/cards/4001-4100.md#shenoy26a-evaluation) · Introspection Adapters: Training LLMs to Report Their Learned Behaviors
- [剪层时监测决策转折消失](../conferences/icml-2026/cards/4101-4200.md#shi26k-evaluation) · Understanding Performance Collapse in Layer-Pruned Large Language Models via Decision Representation Transitions
- [分开验证修补与完整工作流](../conferences/icml-2026/cards/4101-4200.md#shi26r-evaluation) · CyberGym-E2E: Scalable Real-World Benchmark for AI Agents’ End-to-End Cybersecurity Capabilities
- [检索与知识执行分离评测](../conferences/icml-2026/cards/4101-4200.md#shi26ah-evaluation) · $τ$-Knowledge: Evaluating Conversational Agents over Unstructured Knowledge
- [逐声明风险与局部修复](../conferences/icml-2026/cards/4101-4200.md#shihab26a-evaluation) · CGRiC: Compositional Risk Certification for Structured LLM Outputs
- [把研究代理的平均奖励和上尾质量分开监控](../conferences/icml-2026/cards/4101-4200.md#si26b-evaluation) · Towards Execution-Grounded Automated AI Research
- [评测多轮惯性时控制话题结构与历史长度](../conferences/icml-2026/cards/4101-4200.md#simhi26a-evaluation) · Old Habits Die Hard: How Conversational History Geometrically Traps LLMs
- [扩散骨干与长度外推的受控边界](../conferences/icml-2026/cards/4101-4200.md#singh26d-evaluation) · DiffuMamba: High-Throughput Diffusion LMs with Mamba Backbone
- [steering副作用须跨维度测量](../conferences/icml-2026/cards/4101-4200.md#siu26a-evaluation) · SteeringSafety: Benchmarking Representation Steering in LLMs Across Safety Perspectives
- [以可迁移后果验证推理](../conferences/icml-2026/cards/4201-4300.md#son26a-evaluation) · Judging What We Cannot Solve: A Consequence-Based Approach for Oracle-Free Evaluation of Research-Level Math
- [文本智能体赋能估计及失败边界](../conferences/icml-2026/cards/4201-4300.md#song26g-evaluation) · Estimating the Empowerment of Language Model Agents
- [优化器与模拟器非对称校验](../conferences/icml-2026/cards/4201-4300.md#song26z-evaluation) · NEMO: Execution-Aware Optimization Modeling via Autonomous Coding Agents
- [合成监控优化饱和](../conferences/icml-2026/cards/4201-4300.md#storf26a-evaluation) · Constitutional Black-Box Monitoring for Scheming in LLM Agents
- [长对话评估的迁移失败](../conferences/icml-2026/cards/4201-4300.md#subasic26a-evaluation) · Evaluating Language Models in Realistic Conversational Contexts
- [风险条件化置信效用](../conferences/icml-2026/cards/4201-4300.md#subramani26a-evaluation) · The ACUTE Protocol: Operationalizing Language Model Activations for Better Calibration, Utility, and Trust
- [按组件审计智能体基准](../conferences/icml-2026/cards/4201-4300.md#suh26a-evaluation) · AgentSuite: Toward More Reliable Agent Evaluation with a Component-Based Benchmark Auditing Pipeline
- [激活尖峰与注意力汇解耦](../conferences/icml-2026/cards/4201-4300.md#sun26d-evaluation) · Anatomy of Massive Activations and Attention Sinks
- [editing-update-privacy-boundary](../conferences/icml-2026/cards/4201-4300.md#sun26z-evaluation) · Reverse-Engineering Model Editing on Language Models
- [依赖图质量流聚合](../conferences/icml-2026/cards/4301-4400.md#sun26av-evaluation) · Hallucination Detection from Structural Reasoning Model
- [外部状态变化归因诊断](../conferences/icml-2026/cards/4301-4400.md#sun26ba-evaluation) · AgentHijack: Benchmarking Computer Use Agent Robustness to Common Environment Corruptions
- [joint-fisher-sketch](../conferences/icml-2026/cards/4301-4400.md#sweeney26b-evaluation) · The Geometry of Updates: Fisher Alignment at Vocabulary Scale
- [steering-strength-laws](../conferences/icml-2026/cards/4301-4400.md#taimeskhanov26a-evaluation) · Towards Understanding Steering Strength
- [多轮工具安全的过滤盲点与推理预算](../conferences/icml-2026/cards/4301-4400.md#talokar26a-evaluation) · Helpful to a Fault: Measuring Illicit Assistance in Multi-Turn, Multilingual LLM Agents
- [威胁族间鲁棒迁移失败](../conferences/icml-2026/cards/4301-4400.md#tamber26a-evaluation) · Unifying Adversarial Robustness and Training Across Text Scoring Models
- [自奖励的耦合与过奖励偏差](../conferences/icml-2026/cards/4301-4400.md#tan26g-evaluation) · Breaking the Self-Confirming Loop: Diagnosing and Mitigating Systemic Reward Bias in Self-Rewarding RL
- [oracle-sampler-audit](../conferences/icml-2026/cards/4301-4400.md#tang26ad-evaluation) · Is Your Diffusion Sampler Actually Correct? A Sampler-Centric Evaluation of Discrete Diffusion Language Models
- [global-removal-failure](../conferences/icml-2026/cards/4301-4400.md#tang26ah-evaluation) · Do Language Models Track Entities Across State Changes?
- [reconstruction-is-not-semantic-compression](../conferences/icml-2026/cards/4401-4500.md#tarasov26a-evaluation) · Progressive Cramming: Reliable Token Compression and What It Reveals
- [separate-probe-drift-from-policy-change](../conferences/icml-2026/cards/4401-4500.md#taufeeque26a-evaluation) · The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes
- [tail-risk-agent-monitoring](../conferences/icml-2026/cards/4401-4500.md#tayebati26a-evaluation) · TRACER: Trajectory Risk Aggregation for Critical Episodes in Agentic Reasoning
- [cooperation-mechanisms-under-crossplay](../conferences/icml-2026/cards/4401-4500.md#tewolde26a-evaluation) · CoopEval: Benchmarking Cooperation-Sustaining Mechanisms and LLM Agents in Social Dilemmas
- [intent-versus-execution-refactoring](../conferences/icml-2026/cards/4401-4500.md#thillen26a-evaluation) · CodeTaste: Can LLMs Generate Human-Level Code Refactorings?
- [semantics-prior-conflict](../conferences/icml-2026/cards/4401-4500.md#thimmaiah26a-evaluation) · LLMs Lean on Priors, Not Programming Language Semantics
- [evaluation-factor-interactions](../conferences/icml-2026/cards/4401-4500.md#tian26d-evaluation) · Beyond Benchmarks: Toward Causally Faithful Evaluation of Large Language Models
- [过程奖励与正确率脱钩](../conferences/icml-2026/cards/4401-4500.md#tiwari26b-evaluation) · Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models
- [代码表示与执行机制的配对分离](../conferences/icml-2026/cards/4401-4500.md#tong26d-evaluation) · Is Code Better Than Language for Algorithmic Reasoning?
- [代码风格条件化安全失效](../conferences/icml-2026/cards/4401-4500.md#tran26b-evaluation) · Poison with Style: A Practical Poisoning Attack on Code Large Language Models
- [probability-irt-scaling](../conferences/icml-2026/cards/4401-4500.md#truong26b-evaluation) · Item Response Scaling Laws: A Measurement Theory Approach for Efficient and Generalizable Neural Scaling Estimation
- [选择局部依赖头递归传播不确定性](../conferences/icml-2026/cards/4501-4600.md#vazhentsev26a-evaluation) · Efficient Hallucination Detection for LLMs Using Uncertainty-Aware Attention Heads
- [构造式模型差分区分机制与调用时机](../conferences/icml-2026/cards/4501-4600.md#venhoff26a-evaluation) · Base Models Know How to Reason, Thinking Models Learn When
- [多智能体过程验证的迁移失败边界](../conferences/icml-2026/cards/4501-4600.md#venkataramani26a-evaluation) · MAS-ProVe: Understanding the Process Verification of Multi-Agent Systems
- [以可执行适配程序的码长比较任务复杂度](../conferences/icml-2026/cards/4501-4600.md#vergara-browne26a-evaluation) · Operationalising the Superficial Alignment Hypothesis via Task Complexity
- [reward-bias-search](../conferences/icml-2026/cards/4501-4600.md#wang26b-evaluation) · Automatically Finding Reward Model Biases
- [research-claim-rediscovery](../conferences/icml-2026/cards/4501-4600.md#wang26d-evaluation) · FIRE-Bench: Evaluating AI Agents on the Rediscovery of Scientific Insights
- [Automatic Layer Selection for Hallucination Detection](../conferences/icml-2026/cards/4501-4600.md#wang26r-evaluation) · Automatic Layer Selection for Hallucination Detection
- [AgentNoiseBench: Benchmarking Robustness of Tool-Using LLM Agents Under Noisy Condition](../conferences/icml-2026/cards/4601-4700.md#wang26ab-evaluation) · AgentNoiseBench: Benchmarking Robustness of Tool-Using LLM Agents Under Noisy Condition
- [有限专家池的合并收益预算](../conferences/icml-2026/cards/4601-4700.md#wang26bl-evaluation) · Model Merging Scaling Laws in Large Language Models
- [扩散语言模型SAE诊断边界](../conferences/icml-2026/cards/4601-4700.md#wang26cr-evaluation) · DLM-Scope: Mechanistic Interpretability of Diffusion Language Models via Sparse Autoencoders
- [注意力汇与巨激活的作用分离](../conferences/icml-2026/cards/4701-4800.md#wang26ed-evaluation) · Towards Understanding Massive Activations in Attention Sink Mechanism
- [隔离验证与污染采纳诊断](../conferences/icml-2026/cards/4701-4800.md#wang26gf-evaluation) · Persistent Semantic Entities in Tool-Augmented LLM Systems
- [图搜索复杂度与隐式推理容量](../conferences/icml-2026/cards/4701-4800.md#wang26hf-evaluation) · Finding the Minimal Parameter Budget for Implicit Reasoning: A Data Complexity Driven Scaling Law for Language Models
- [功能向量的路由与内容分解](../conferences/icml-2026/cards/4801-4900.md#wang26hp-evaluation) · How Few-Shot Examples Add Up: A Causal Decomposition of Function Vectors in In-Context Learning
- [用改写候选搜索单题电路](../conferences/icml-2026/cards/5001-5100.md#wu26a-evaluation) · Query Circuits: Explaining How Language Models Answer User Prompts
- [序贯探索产生新分配偏差](../conferences/icml-2026/cards/5001-5100.md#wu26ah-evaluation) · Large Language Models Develop Novel Social Biases Through Adaptive Exploration
- [推理打断与中途更正规则](../conferences/icml-2026/cards/5001-5100.md#wu26ao-evaluation) · Are Large Reasoning Models Interruptible?
- [代理难度泛化与接口迁移分离](../conferences/icml-2026/cards/5001-5100.md#xi26b-evaluation) · Does Reinforcement Fine-Tuning Improve Generalization of LLM Agents? An Empirical Study
- [跨模型正确性历史与跨数据校准](../conferences/icml-2026/cards/5101-5200.md#xiao26l-evaluation) · Generalized Correctness Models: Learning Calibrated and Cross-Model Correctness Predictors from Historical Patterns
- [RLVR可监测性的数据与熵边界](../conferences/icml-2026/cards/5101-5200.md#xiong26b-evaluation) · Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning
- [贡献路径与检索相关性的联合置信](../conferences/icml-2026/cards/5201-5300.md#xu26c-evaluation) · Information Flow Reveals When to Trust Language Models
- [双层并行与候选选择的成本边界](../conferences/icml-2026/cards/5201-5300.md#xu26bb-evaluation) · A Two-Tier Perspective on Inference-Time Parallelism in Multi-Agent LLM Systems
- [遗忘评估同时测恢复和保留能力](../conferences/icml-2026/cards/5201-5300.md#xu26cd-evaluation) · Unlearning Isn’t Deletion: Investigating Reversibility of Machine Unlearning in LLMs
- [自动化通信一侧区分协作失败](../conferences/icml-2026/cards/5301-5400.md#yadav26a-evaluation) · More Capable, Less Cooperative? When LLMs Fail at Zero-Cost Collaboration
- [伪奖励下污染捷径的分层审计](../conferences/icml-2026/cards/5301-5400.md#yan26f-evaluation) · Spurious Rewards Paradox: Mechanistically Understanding How RLVR Activates Memorization Shortcuts in LLMs
- [内部干预目标导出的查询指纹](../conferences/icml-2026/cards/5301-5400.md#yan26t-evaluation) · CircuitPrint: Mechanistic Circuit Fingerprints for Large Language Models
- [安全边界评估加入角色表征探测](../conferences/icml-2026/cards/5501-5600.md#ye26b-evaluation) · Prompt Injection as Role Confusion
- [拒绝行为与持续安全表征的分离](../conferences/icml-2026/cards/5501-5600.md#yin26b-evaluation) · Robust Harmful Features Under Jailbreak Attacks: Mechanistic Evidence from Attention Head Specialization in Large Language Models
- [RLVR下PEFT结构与初始化失效边界](../conferences/icml-2026/cards/5501-5600.md#yin26h-evaluation) · Evaluating Parameter Efficient Methods for RLVR
- [答案奖励外另测推理截断敏感性与独立可读性](../conferences/icml-2026/cards/5601-5700.md#yu26av-evaluation) · Outcome Rewards Do Not Guarantee Verifiable or Causally Important Reasoning
- [记忆匹配后的近远迁移剖面](../conferences/icml-2026/cards/5701-5800.md#zhang26u-evaluation) · The Generalization Spectrum: A Chromatographic Approach to Evaluating Learning Algorithms
- [从少量source模型隐状态构造benchmark小集](../conferences/icml-2026/cards/5701-5800.md#zhang26bj-evaluation) · Learning More from Less: Unlocking Internal Representations for Benchmark Compression
- [时间外验证的条件分位能力边界](../conferences/icml-2026/cards/5801-5900.md#zhang26by-evaluation) · Prescriptive Scaling Reveals the Evolution of Language Model Capabilities
- [按adapter驻留槽约束入口以控制LoRA尾延迟](../conferences/icml-2026/cards/5801-5900.md#zhang26dg-evaluation) · CLIMB: Taming the LoRA Residency Cliff in Multi-LoRA Serving
- [把语义cache命中与回答完整性分开审计](../conferences/icml-2026/cards/5801-5900.md#zhang26dt-evaluation) · From Similarity to Vulnerability: Key Collision Attack on LLM Semantic Caching
- [通信轮次下防御信号衰减](../conferences/icml-2026/cards/5901-6000.md#zhang26jb-evaluation) · When Embedding-Based Defenses Fail: Rethinking Safety in LLM-Based Multi-Agent Systems
- [跨seed双峰导致的表观能力跃迁](../conferences/icml-2026/cards/6001-6100.md#zhao26al-evaluation) · Random Scaling of Emergent Capabilities
- [在相关judge中选条件独立视图](../conferences/icml-2026/cards/6001-6100.md#zhao26aq-evaluation) · CARE: Confounder-Aware Aggregation for Reliable LLM Evaluation
- [分开审计原始轨迹和压缩经验](../conferences/icml-2026/cards/6001-6100.md#zhao26aw-evaluation) · Large Language Model Agents Are Not Always Faithful Self-Evolvers
- [区分形式验证通过和算法语义遵循](../conferences/icml-2026/cards/6001-6100.md#zhao26bm-evaluation) · AlgoVeri: An Aligned Benchmark for Verified Code Generation on Classical Algorithms
- [区分叙述变化与算法结构变化的代码测试](../conferences/icml-2026/cards/6101-6200.md#zheng26i-evaluation) · UniCode: Augmenting Evaluation for Code Reasoning
- [在捷径控制下比较ToM后训练](../conferences/icml-2026/cards/6101-6200.md#zhong26i-evaluation) · From Shortcuts to Reasoning: Robust Post-Training of Theory of Mind with Reinforcement Learning
- [多约束代码修改需同时测回归与遵循](../conferences/icml-2026/cards/6101-6200.md#zhong26t-evaluation) · SWE-IF: Aligning Code Evaluation with Human Preference
- [能力RL的代理奖励失败与有限迁移](../conferences/icml-2026/cards/6101-6200.md#zhou26p-evaluation) · Alignment Risks from Capability-Seeking RL Training
- [质量与重复饱和的经验配方缩放律](../conferences/icml-2026/cards/6101-6200.md#zhou26af-evaluation) · InfoLaw: Information Scaling Laws for Large Language Models with Quality-Weighted Mixture Data and Repetition
- [否定处理的晚层attention捷径诊断](../conferences/icml-2026/cards/6201-6300.md#zhou26bq-evaluation) · How Language Models Process Negation
- [调度熵的短程拟合与context扰动](../conferences/icml-2026/cards/6201-6300.md#zhu26g-evaluation) · Recognize Your Orchestrator: An Entropy Dynamics Perspective for LLM Multi-Agent Systems
- [拆开token碎片化与字符噪声的鲁棒评价](../conferences/icml-2026/cards/6201-6300.md#zhuo26b-evaluation) · Understanding the Ability of LLMs to Handle Character-Level Perturbation
- [对LLM评审同时测跨文同质性与改写敏感性](../conferences/icml-2026/cards/6301-6400.md#baumann26a-evaluation) · Position: Stop Automating Peer Review Without Rigorous Evaluation
- [实现与多次试验噪声的安全评价对照](../conferences/icml-2026/cards/6301-6400.md#beyer26b-evaluation) · Position: LLM-Safety Evaluations Lack Robustness
- [形式DSL评测分开接口可执行与证明成功](../conferences/icml-2026/cards/6301-6400.md#genevaux26a-evaluation) · Position: Mathematical DSL Benchmarks Need Executable Interface Contracts
- [保持假话表面线索而移除欺骗意图测试probe](../conferences/icml-2026/cards/6401-6500.md#gupta26e-evaluation) · Position: Anthropomorphic Misalignment Research Needs Stronger Evidence
- [压力类型与judge差异的同题sycophancy剖面](../conferences/icml-2026/cards/6401-6500.md#kasneci26a-evaluation) · Position: Sycophancy is an Educational Safety Risk: Why LLM Tutors Need Sycophancy Benchmarks
- [分别审计隐式防护的持久性与副作用](../conferences/icml-2026/cards/6401-6500.md#li26kc-evaluation) · Position: Retire the "Positive Backdoor" Label—Secret Alignment Requires Strict and Systematic Evaluation
- [用行为结果校准推理轨迹监控而非单看语义](../conferences/icml-2026/cards/6401-6500.md#riemer26a-evaluation) · Position: Collusion Risks Among AI Reasoning Agents Justify Certification Requirements for Making Market Decisions

<a id="by-computer-vision"></a>

### 计算机视觉

- [扩散模型域外检测](../conferences/icml-2026/cards/0001-0100.md#alexis26a-evaluation) · GEPC: Group-Equivariant Posterior Consistency for Out-of-Distribution Detection in Diffusion Models
- [深伪防御评测](../conferences/icml-2026/cards/0101-0200.md#baek26e-evaluation) · Proactive Defense Benchmark against Deepfake Generation
- [扩散模型概念遗忘](../conferences/icml-2026/cards/0301-0400.md#braun26b-evaluation) · Erased but Not Forgotten: How Backdoors Compromise Concept Erasure
- [视觉表征的组合绑定诊断](../conferences/icml-2026/cards/0701-0800.md#chung26a-evaluation) · Global Geometry Is Not Enough for Vision Representations
- [类别遗忘的近邻输出泄漏](../conferences/icml-2026/cards/1001-1100.md#ebrahimpour-boroojeny26a-evaluation) · Unlearning Isn’t Forgetting: Revealing Hidden Leakage in Class Unlearning Evaluations
- [用条件熵定位扩散的语义形成窗口](../conferences/icml-2026/cards/1401-1500.md#handke26a-evaluation) · The Entropic Signature of Class Speciation in Diffusion Models
- [插入抑制证据解释缺席概念](../conferences/icml-2026/cards/1501-1600.md#hesse26a-evaluation) · What is Missing? Explaining Neurons Activated by Absent Concepts
- [跨训练阶段检验持续学习的后门持久性](../conferences/icml-2026/cards/1601-1700.md#huang26n-evaluation) · Persistent Backdoor Attacks in Class-Incremental Learning via Structural Invariant Anchoring
- [从特征存在性中扣除对象绑定信息](../conferences/icml-2026/cards/1701-1800.md#huang26y-evaluation) · Formalizing the Binding Problem
- [把扩散调度输入作为独立的安全审计面](../conferences/icml-2026/cards/1701-1800.md#huang26av-evaluation) · Watch Your Step: Information Injection in Diffusion Models via Shadow Timestep Embedding
- [从分布内几何挑选马氏检测的径向缩放](../conferences/icml-2026/cards/1801-1900.md#janiak26a-evaluation) · A Geometry-Based View of Mahalanobis OOD Detection
- [分别打乱概念频率与保留组合来定位生成失败](../conferences/icml-2026/cards/1801-1900.md#jeong26b-evaluation) · When Do Diffusion Models Learn to Generate Multiple Objects?
- [按观测锚点密度判断弱先验是否够用](../conferences/icml-2026/cards/1801-1900.md#jia26k-evaluation) · Weak Diffusion Priors Can Still Achieve Strong Inverse-Problem Performance
- [固定下游容量和训练组合再比较对象槽](../conferences/icml-2026/cards/2001-2100.md#kapl26b-evaluation) · Are Object-Centric Representations Better at Compositional Generalization?
- [用混合真实和修补区域诊断检测通道](../conferences/icml-2026/cards/2001-2100.md#kim26k-evaluation) · Dissect and Prune: Enhancing Robustness in AI-Generated Image Detection
- [扣除欠拟合参照再定位扩散记忆](../conferences/icml-2026/cards/2101-2200.md#kim26aq-evaluation) · Localizing Memorized Regions in Diffusion Models via Coordinate-Wise Curvature Differences
- [用有限差分监督绕开 INR 拟合反传瓶颈](../conferences/icml-2026/cards/2101-2200.md#kim26as-evaluation) · Adversarial Robustness of Implicit Neural Representation-Based Classifiers
- [在生成潜空间规划归因路径](../conferences/icml-2026/cards/2101-2200.md#kim26aw-evaluation) · Manifold-Aligned Guided Integrated Gradients for Reliable Feature Attribution
- [用多个条件向量复测扩散去记忆](../conferences/icml-2026/cards/2201-2300.md#kowalczuk26a-evaluation) · Finding DoRI: Discovery of Retained Images in Diffusion Models
- [用角落位移区分显著性的中心先验](../conferences/icml-2026/cards/2201-2300.md#kuang26a-evaluation) · When Random Saliency Looks Trained: Architectural Center Bias in CNN Interpretability
- [水印通过后再检查反演潜变量的几何偏移](../conferences/icml-2026/cards/2301-2400.md#lee26bm-evaluation) · Rethinking Forgery Attacks on Semantic Watermarks in Black-Box Settings: A Geometric Distortion Perspective
- [用扩散特征污染率监测记忆](../conferences/icml-2026/cards/2401-2500.md#li26br-evaluation) · Evaluating the Representation Space of Diffusion Models via Self-Supervised Principles
- [用频率对照检验扩散模型的成员泄漏](../conferences/icml-2026/cards/2601-2700.md#lian26a-evaluation) · Enhancing Membership Inference Attacks on Diffusion Models from a Frequency-Domain Perspective
- [诊断潜空间曲率与可见细节失配](../conferences/icml-2026/cards/2601-2700.md#liang26d-evaluation) · Geometric Decoupling: Diagnosing the Structural Instability of Latent
- [扩散数据贡献者归因](../conferences/icml-2026/cards/3001-3100.md#lu26f-evaluation) · SurrogateSHAP: Training-Free Contributor Attribution for Text-to-Image (T2I) Models
- [用共享扩散模型反学习近似逐组反事实归因](../conferences/icml-2026/cards/3301-3400.md#murata26a-evaluation) · GUDA: Counterfactual Group-wise Training Data Attribution for Diffusion Models via Unlearning
- [用反演重建差异审计图像防仿制扰动](../conferences/icml-2026/cards/3701-3800.md#qiu26b-evaluation) · DDIM Inversion as a Perturbation Amplifier: Breaking Mimicry Protection via Reconstruction Error Minimization
- [用组合触发测试 ViT 检查点供应链防御](../conferences/icml-2026/cards/4001-4100.md#shen26a-evaluation) · DF-LoGiT: Data-Free Logic-Gated Backdoor Attacks in Vision Transformers
- [归因感知的物体表示评测](../conferences/icml-2026/cards/4101-4200.md#singh26f-evaluation) · Evaluating Object-Centric Models beyond Object Discovery
- [单观测噪声裂分模型检验](../conferences/icml-2026/cards/4201-4300.md#sprunck26a-evaluation) · Bayesian model selection and misspecification testing in imaging inverse problems only from noisy and partial measurements
- [在线自适应时间效用](../conferences/icml-2026/cards/4201-4300.md#sreeram26a-evaluation) · Tempora: Characterising the Time-Contingent Utility of Online Test-Time Adaptation
- [audit-low-level-shortcuts](../conferences/icml-2026/cards/4301-4400.md#svatko26a-evaluation) · Deep Learning for BioImaging: What Are We Really Learning?
- [基于定律的视频动力学评测](../conferences/icml-2026/cards/4401-4500.md#tragoudaras26a-evaluation) · Evaluating Newtonian Mechanics in Video Generative Models with Real Physical Systems
- [rarity-times-semantic-distinctiveness](../conferences/icml-2026/cards/4501-4600.md#vadakkeeveetil-sreelatha26a-evaluation) · RAIGen: Rare Attribute Identification in Text-to-Image Generative Models
- [在归因图层面做类别竞争](../conferences/icml-2026/cards/4501-4600.md#walter26a-evaluation) · Hidden in Plain Sight – Class Competition Focuses Attribution Maps
- [扰动响应而非静态伪影](../conferences/icml-2026/cards/4601-4700.md#wang26ad-evaluation) · RA-Det: Towards Universal Detection of AI-Generated Images via Robustness Asymmetry
- [硬标签法向估计的坐标信噪比](../conferences/icml-2026/cards/4701-4800.md#wang26gh-evaluation) · Bias in Zeroth-Order Normal Estimation for Decision-Based Attacks
- [扩散attention汇聚量与必要性分离](../conferences/icml-2026/cards/5001-5100.md#wu26ax-evaluation) · Attention Sinks in Diffusion Transformers: A Causal Analysis
- [拆分图像与软标签的数据压缩比较](../conferences/icml-2026/cards/5101-5200.md#xiao26k-evaluation) · Unifying Dataset Pruning and Distillation for Efficient Large-scale Compression
- [按下游任务分配像素预训练算力](../conferences/icml-2026/cards/5301-5400.md#yan26j-evaluation) · Rethinking Generative Image Pretraining: How Far Are We From Scaling Up Next-Pixel Prediction?
- [把连通碎裂显式接入分割评分](../conferences/icml-2026/cards/5801-5900.md#zhang26br-evaluation) · T-measure: A Topology-Consistent Metric for Binary Segmentation
- [用能量和结构匹配控制测边缘扰动的全局传播](../conferences/icml-2026/cards/5801-5900.md#zhang26ev-evaluation) · Geometric Collapse: When Vision Models Fail to Verify Physical Causality
- [码本利用率不等于表征维数](../conferences/icml-2026/cards/6001-6100.md#zhang26jl-evaluation) · Unveiling And Addressing Dimensional Collapse In Vector Quantization Models Via Codebook Regularization
- [无modelaccess时以patchscoreproxy定位训练对应](../conferences/icml-2026/cards/6001-6100.md#zhao26i-evaluation) · Nonparametric Data Attribution for Diffusion Models
- [架构稳定性必须条件于归因算子](../conferences/icml-2026/cards/6301-6400.md#elangovan26b-evaluation) · Position: Explanation Stability Is a Property of the Model–Method Pair, Not the Model
- [审美reward评测分开显式风格遵循与通用品质](../conferences/icml-2026/cards/6401-6500.md#guo26ao-evaluation) · Position: Universal Aesthetic Alignment Narrows Artistic Expression
- [用冲突与去线索联合检验shape改进](../conferences/icml-2026/cards/6401-6500.md#kayyam26b-evaluation) · Position: CNNs Don’t See Shape — And That Won’t Change Without New Architectures
- [区分年龄表征的直接验证与可学身份读出](../conferences/icml-2026/cards/6401-6500.md#marshalkin26a-evaluation) · Position: Age Estimation Models Do Not Process Biometric Data

<a id="by-nlp"></a>

### 自然语言处理

- [检索增强生成安全评测](../conferences/icml-2026/cards/0501-0600.md#chen26av-evaluation) · Eyes-on-Me: Scalable RAG Poisoning through Transferable Attention-Steering Attractors
- [交换证据语言测引证相关性偏差](../conferences/icml-2026/cards/2001-2100.md#ki26a-evaluation) · Linguistic Nepotism: Trading-off Quality for Language Preference in Multilingual RAG
- [按语料的语义分层覆盖检索评测](../conferences/icml-2026/cards/2101-2200.md#klearman26a-evaluation) · Coverage, Not Averages: Semantic Stratification for Trustworthy Retrieval Evaluation
- [分别破坏输出语言与源句内容寻找翻译头](../conferences/icml-2026/cards/2201-2300.md#lasnier26a-evaluation) · Translation Heads: Disentangling meaning from language in LLM-based machine translation
- [用未知查询下的文档改动压力测试召回](../conferences/icml-2026/cards/2301-2400.md#li26g-evaluation) · “Someone Hid It!”: Query-Agnostic Black-Box Attacks on LLM-Based Retrieval
- [按触发词语义审计蒸馏注意力标签的后门风险](../conferences/icml-2026/cards/3801-3900.md#ren26q-evaluation) · Attention Hijacking: Backdooring Text Dataset Distillation via Semantic Anchors
- [retrieval-blind-spot-audit](../conferences/icml-2026/cards/4301-4400.md#taghavi26a-evaluation) · With Argus Eyes: Assessing Retrieval Gaps via Uncertainty Scoring to Detect and Remedy Retrieval Blind Spots
- [语音生成中激活注入位置的诊断](../conferences/icml-2026/cards/4701-4800.md#wang26he-evaluation) · CoCoEmo: Composable and Controllable Human-Like Emotional TTS via Activation Steering
- [用词袋对照检验embedding的隐含语义读出](../conferences/icml-2026/cards/6501-6552.md#sun26bb-evaluation) · Position: Text Embeddings Should Capture Implicit Semantics, Not Just Surface Meaning

<a id="by-reinforcement-learning"></a>

### 强化学习

- [持续记录新队友和新布局中的上下文适应](../conferences/icml-2026/cards/1901-2000.md#jing26d-evaluation) · Benchmarking the Limits of In-Context Reinforcement Learning for Ad-Hoc Teamwork
- [用外部训练对手的交互路径检验强化学习后门](../conferences/icml-2026/cards/2801-2900.md#liu26w-evaluation) · Fox in the Henhouse: Supply-Chain Backdoor Attacks Against Reinforcement Learning
- [用可塑性干预与后门的交互诊断强化学习脆弱性](../conferences/icml-2026/cards/3101-3200.md#ma26w-evaluation) · Angel or Demon: Investigating the Plasticity Interventions’ Impact on Backdoor Threats in Deep Reinforcement Learning
- [把奖励塑形用作离策略控制变量](../conferences/icml-2026/cards/3101-3200.md#majumdar26a-evaluation) · Reward Shaping Control Variates for Off-Policy Evaluation Under Sparse Rewards
- [正常回报掩盖策略后门的压力测试](../conferences/icml-2026/cards/3701-3800.md#qian26n-evaluation) · Toward Subspace-Perturbed Trajectory-Aware Backdoor Attacks in Deep Reinforcement Learning
- [复核策略泛化时控制奖励和观察](../conferences/icml-2026/cards/3801-3900.md#rajabpour26a-evaluation) · Revisiting OOD Generalization in Programmatic RL
- [百任务序列暴露正则塑性失效](../conferences/icml-2026/cards/4401-4500.md#tomilin26a-evaluation) · MEAL: A Benchmark for Continual Multi-Agent Reinforcement Learning
- [跨输入可区分性诊断模板坍缩](../conferences/icml-2026/cards/4601-4700.md#wang26bn-evaluation) · RAGEN-2: Reasoning Collapse in Agentic RL
- [可观测孪生分离记忆收益](../conferences/icml-2026/cards/4601-4700.md#wang26bx-evaluation) · Investigating Memory in Model-Free RL with POPGym Arcade
- [把世界结构查询编码为派生交互任务](../conferences/icml-2026/cards/4901-5000.md#warrier26a-evaluation) · Benchmarking World-Model Learning with Environment-Level Queries
- [乘子漂移下混合critic的跟踪误差](../conferences/icml-2026/cards/5301-5400.md#yang26ab-evaluation) · Why Dedicated Critics: Eliminating Target Drift in Multi-Constraint RL
- [并行环境转单流时重配更新数据比](../conferences/icml-2026/cards/6501-6552.md#vandergrift26a-evaluation) · Position: RL Researchers Need to Distinguish Between Solving Simulators and Using Simulators as a Proxy

<a id="by-robotics"></a>

### 机器人学

- [动作块增量的基准姿态](../conferences/icml-2026/cards/1101-1200.md#feng26ab-evaluation) · Demystifying Action Space Design for Robotic Manipulation Policies
- [分开审计 VLA 的指令、推理与动作链路](../conferences/icml-2026/cards/1701-1800.md#huang26cm-evaluation) · TRAP: Hijacking VLA CoT-Reasoning via Adversarial Patches
- [用恢复测试区分机器人技能遗忘](../conferences/icml-2026/cards/2801-2900.md#liu26bu-evaluation) · Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning
- [按扰动修正扭矩分层评估动作模仿](../conferences/icml-2026/cards/3201-3300.md#meng26n-evaluation) · Distinguishing Imitation Error from Intrinsic Motion Learning Difficulty
- [空中操纵的视角依赖诊断](../conferences/icml-2026/cards/4301-4400.md#sun26an-evaluation) · AIR-VLA: Vision-Language-Action Systems for Aerial Manipulation
- [主动视角中的置信奖励失效](../conferences/icml-2026/cards/4301-4400.md#tang26a-evaluation) · See, Act, Adapt: Active Perception for Unsupervised Cross-Domain Visual Adaptation via Personalized VLM-Guided Agent
- [静态诊断与闭环修复的分离](../conferences/icml-2026/cards/5301-5400.md#yan26r-evaluation) · Can VLMs Diagnose and Recover from VLA Manipulation Faults?
- [跨视角保留与子空间adapter路由](../conferences/icml-2026/cards/5301-5400.md#yan26y-evaluation) · CE$^4$L: Continual Ego, Exo, and Ego-Exo Learning
- [按VLM与动作专家的不同瓶颈选部署优化](../conferences/icml-2026/cards/6101-6200.md#zhou26e-evaluation) · Characterizing Vision-Language-Action Models across XPUs: Constraints and Acceleration for On-Robot Deployment
- [按联合支持与边缘支持拆开VLA泛化评测](../conferences/icml-2026/cards/6201-6300.md#zhou26az-evaluation) · Dismantling the Illusion of Vision-Language-Action Models Competence via Explicit Distributional Shifts
- [真实失败视觉与偏好筛选dense负例的reward校准](../conferences/icml-2026/cards/6501-6552.md#tian26o-evaluation) · Position: Good Embodied Reward Models Need Bad Behavior Data

<a id="by-multimodal"></a>

### 多模态学习

- [视觉语言安全评测](../conferences/icml-2026/cards/0101-0200.md#azulay26a-evaluation) · Jailbreaking Vision-Language Models Through the Visual Modality
- [语义近邻校准标注判错](../conferences/icml-2026/cards/0801-0900.md#di26b-evaluation) · Detecting Errors in AI-Generated Annotations: When and Why Semantic Neighbors Help
- [用图像证据约束欺骗辩论](../conferences/icml-2026/cards/1001-1100.md#fang26f-evaluation) · Debate with Images: Detecting Deceptive Behaviors in Multimodal Large Language Models
- [文本条件下的音视频信息分解](../conferences/icml-2026/cards/1001-1100.md#fang26x-evaluation) · Towards Understanding Modality Interaction in Multimodal Language Models via Partial Information Decomposition
- [文本知识编辑的图像迁移诊断](../conferences/icml-2026/cards/1201-1300.md#gao26ag-evaluation) · Do Text Edits Generalize to Visual Generation? Benchmarking Cross-Modal Knowledge Editing in UMMs
- [从任务失败周期诊断隐藏视觉分块](../conferences/icml-2026/cards/1601-1700.md#hu26b-evaluation) · Steal the Patch Size: Adversarially Manipulate Vision Language Models
- [用逐模态数据复杂度和头部敲除诊断上下文迁移](../conferences/icml-2026/cards/1701-1800.md#huang26at-evaluation) · Dissecting Multimodal In-Context Learning: Modality Asymmetries and Circuit Dynamics in modern Transformers
- [拆开语音安全评审的模态贡献](../conferences/icml-2026/cards/1801-1900.md#ivry26a-evaluation) · LALM-as-a-Judge: Benchmarking Large Audio-Language Models for Safety Evaluation in Multi-Turn Spoken Dialogues
- [通过跨模态共享分区标识绑定证据](../conferences/icml-2026/cards/1801-1900.md#izadi26a-evaluation) · Uncovering Grounding IDs: How External Cues Shape Multi-Modal Binding
- [用受控错误轨迹测视觉幻觉累积](../conferences/icml-2026/cards/1901-2000.md#jiang26t-evaluation) · MM-Snowball: Evaluating and Mitigating Hallucination Snowballing in Multimodal Multi-Turn Dialogue
- [用独立条件拆解长提示文生图的失败](../conferences/icml-2026/cards/1901-2000.md#jiao26b-evaluation) · DetailMaster: Can Your Text-to-Image Model Handle Long Prompts?
- [先验证棋盘读数再测规则推理](../conferences/icml-2026/cards/1901-2000.md#jin26a-evaluation) · Seeing Without Understanding: Disentangling Perception, Reasoning, and Simulation in VLM Gameplay
- [用因果补丁定位跨模态注意力汇点](../conferences/icml-2026/cards/2001-2100.md#jung26c-evaluation) · Probing Cross-modal Information Hubs in Audio-Visual LLMs
- [用注意力特征摊销推理中的区域消融归因](../conferences/icml-2026/cards/2001-2100.md#kang26d-evaluation) · Real-Time Visual Attribution Streaming in Thinking Model
- [以同层文本近邻解释视觉隐藏表示](../conferences/icml-2026/cards/2201-2300.md#krojer26a-evaluation) · LatentLens: Revealing Highly Interpretable Visual Tokens in LLMs
- [用指令词元的内部状态判别模型是否虚构对象](../conferences/icml-2026/cards/2201-2300.md#lai26e-evaluation) · Instruction Lens Score: Your Instruction Contributes a Powerful Object Hallucination Detector for Multimodal Large Language Models
- [用输入和中间态两次干预检验视觉推理链](../conferences/icml-2026/cards/2401-2500.md#li26r-evaluation) · Imagination Helps Visual Reasoning, But Not Yet in Latent Space
- [单一扰动的语义依赖攻击评测](../conferences/icml-2026/cards/2401-2500.md#li26co-evaluation) · Semantic Router: On the Feasibility of Hijacking MLLMs via a Single Adversarial Perturbation
- [用事发时间与知识截止点检查时序预测泄露](../conferences/icml-2026/cards/2901-3000.md#liu26go-evaluation) · Rethinking Multimodal Time-Series Forecasting Evaluation
- [用成对守恒与非守恒条件剥离物理判断的文本先验](../conferences/icml-2026/cards/3001-3100.md#luo26n-evaluation) · Vision Language Models Cannot Reason About Physical Transformation
- [按样本的跨模态差异评估联邦成员推断暴露](../conferences/icml-2026/cards/3101-3200.md#ma26t-evaluation) · The Hidden Risk: Membership Inference Attacks on Multimodal Federated Learning via Modality Imbalance
- [视觉工具强化学习收益归因](../conferences/icml-2026/cards/3101-3200.md#ma26as-evaluation) · What Does Vision Tool-Use Reinforcement Learning Really Learn? Disentangling Tool-Induced and Intrinsic Effects for Crop-and-Zoom
- [让音频评估同时奖励语义相似和跨样本可辨识](../conferences/icml-2026/cards/3401-3500.md#niu26d-evaluation) · MECAT: A Multi-Experts Constructed Benchmark for Fine-Grained Audio Understanding Tasks
- [分阶段定位视觉计数的外推失效](../conferences/icml-2026/cards/3501-3600.md#pang26c-evaluation) · Unveiling the Visual Counting Bottleneck in Vision-Language Models
- [用最小视觉反例训练多模态裁判](../conferences/icml-2026/cards/3501-3600.md#park26c-evaluation) · Mitigating Perceptual Judgment Bias in Multimodal LLM-as-a-Judge via Perceptual Perturbation and Reward Modeling
- [以音频时钟复现全双工工具任务](../conferences/icml-2026/cards/3801-3900.md#ray26a-evaluation) · $τ$-Voice: Benchmarking Full-Duplex Voice Agents on Real-World Domains
- [视觉语言模型的概念几何干扰](../conferences/icml-2026/cards/3901-4000.md#savietto26a-evaluation) · The Geometry of Representational Failures in Vision Language Models
- [用无图对照校准视觉退化损失](../conferences/icml-2026/cards/3901-4000.md#saxena26b-evaluation) · VLM-RobustBench: A Comprehensive Benchmark for Robustness of Vision-Language Models
- [交叉测试物理能力与任务捷径](../conferences/icml-2026/cards/3901-4000.md#schulze-buschoff26a-evaluation) · Can Vision Language Models Learn Intuitive Physics from Interaction?
- [沿 Flow Matching 插值路径定位训练成员信号](../conferences/icml-2026/cards/4001-4100.md#sesmat26a-evaluation) · Where Flow Matching Leaks: Characterising the Membership Signals Along the Interpolation Path
- [换图检验视觉复查](../conferences/icml-2026/cards/4101-4200.md#shi26ad-evaluation) · Are VLMs Seeing or Just Saying? Uncovering the Illusion of Visual Re-examination
- [知识轻视觉推理与计算收益](../conferences/icml-2026/cards/4201-4300.md#song26s-evaluation) · VisualPuzzles: Decoupling Multimodal Reasoning Evaluation from Domain Knowledge
- [privacy-perception-reasoning-audit](../conferences/icml-2026/cards/4201-4300.md#sun26t-evaluation) · MultiPriv: Benchmarking Individual-Level Privacy Reasoning in Vision-Language Models
- [bidirectionality-late-interaction-synergy](../conferences/icml-2026/cards/4401-4500.md#teiletche26a-evaluation) · ModernVBERT: Towards Smaller Visual Document Retrievers
- [binding-vs-unimodal-recoverability](../conferences/icml-2026/cards/4501-4600.md#uselis26b-evaluation) · How can embedding models bind concepts?
- [atomic-multimodal-attribution](../conferences/icml-2026/cards/4501-4600.md#wan26m-evaluation) · Multimodal Fact-Level Attribution for Verifiable Reasoning
- [无害音频的跨模态安全干扰](../conferences/icml-2026/cards/4601-4700.md#wang26cf-evaluation) · Acoustic Interference: A New Paradigm Weaponizing Acoustic Latent Semantic for Universal Jailbreak against Large Audio Language Models
- [视觉压缩的安全与效用权衡](../conferences/icml-2026/cards/4701-4800.md#wang26fm-evaluation) · Understanding and Mitigating Token-Pruning-Induced Vulnerabilities in VLMs
- [环境到词汇的信息聚合定位](../conferences/icml-2026/cards/5001-5100.md#wu26am-evaluation) · The Mechanistic Emergence of Symbol Grounding in Language Models
- [固定任务下成对测试判据切换](../conferences/icml-2026/cards/5401-5500.md#yang26cx-evaluation) · Criterion-Conditional In-Context Learning: Evaluating Criterion-Shift Adaptation in Vision-Language Models
- [时间序列对齐应区分全局几何和局部邻域](../conferences/icml-2026/cards/5501-5600.md#yashwante26a-evaluation) · Time Series, Vision, and Language: Exploring the Limits of Alignment in Contrastive Representation Spaces
- [oracle视觉中间态分解生成与解读失败](../conferences/icml-2026/cards/5601-5700.md#zeller26a-evaluation) · MentisOculi: Revealing the Limits of Reasoning with Mental Imagery
- [让空间QA随实际frame预算重标](../conferences/icml-2026/cards/5701-5800.md#zhang26o-evaluation) · ReVSI: Rebuilding Visual Spatial Intelligence Evaluation for Accurate Assessment of VLM 3D Reasoning
- [CLIP测试时防御的指示量失配](../conferences/icml-2026/cards/5801-5900.md#zhang26cq-evaluation) · You Don’t Protect if You Don’t Expect: Breaking the Key Assumption behind CLIP’s Test-Time Defenses
- [按真实压缩路径评测视觉鲁棒性](../conferences/icml-2026/cards/5801-5900.md#zhang26dl-evaluation) · On the Adversarial Robustness of Large Vision-Language Models under Visual Token Compression
- [用单模态均可答的冲突题测模态依赖](../conferences/icml-2026/cards/5801-5900.md#zhang26ed-evaluation) · Evaluating and Steering Modality Preferences in Multi-modal LLMs
- [情绪头的中层选择性与深层共享性](../conferences/icml-2026/cards/5901-6000.md#zhang26fi-evaluation) · Interpreting and Enhancing Emotional Circuits in Large Vision-Language Models via Cross-Modal Information Flow
- [词汇相近时的关系完整性防御评测](../conferences/icml-2026/cards/5901-6000.md#zhang26fr-evaluation) · TokenSwap: Backdoor Attack on the Compositional Understanding of Large Vision-Language Models
- [准确率上升时的推理一致性漂移](../conferences/icml-2026/cards/6001-6100.md#zhao26am-evaluation) · On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs
- [位置与复述混杂后的幻觉校准](../conferences/icml-2026/cards/6301-6400.md#zohrabi26a-evaluation) · HaloProbe: Bayesian Detection and Mitigation of Object Hallucinations in Vision-Language Models
- [视觉细节任务先诊断信息访问再加文本推理](../conferences/icml-2026/cards/6301-6400.md#gao26ar-evaluation) · Position: Reasoning After Perception Means Reasoning Without Vision
- [分级提示注入区分视觉发现与计算失败](../conferences/icml-2026/cards/6401-6500.md#huang26cp-evaluation) · Position: The Systemic Lack of Agency in Visual Reasoning
- [先删中间图像再归因视觉CoT收益](../conferences/icml-2026/cards/6501-6552.md#yang26ed-evaluation) · Position: Your VLM May Not Be Thinking with Interleaved Images

<a id="by-ml-foundations"></a>

### 机器学习基础与统计

- [表征相似性](../conferences/icml-2026/cards/0001-0100.md#almudevar26a-evaluation) · Bridging Functional and Representational Similarity via Usable Information
- [机制可解释性](../conferences/icml-2026/cards/0001-0100.md#anani26a-evaluation) · Certified Circuits: Stability Guarantees for Mechanistic Circuits
- [参数扰动稳健性](../conferences/icml-2026/cards/0101-0200.md#arpit26a-evaluation) · TPV: Parameter Perturbations Through the Lens of Test Prediction Variance
- [模型拼接评测](../conferences/icml-2026/cards/0101-0200.md#athanasiadis26a-evaluation) · Grounding Functional Similarity by Invariance-Aware Model Stitching
- [影响函数](../conferences/icml-2026/cards/0101-0200.md#bado26a-evaluation) · Clustered Influence Functions
- [表格基础模型](../conferences/icml-2026/cards/0101-0200.md#balef26a-evaluation) · Is One Layer Enough? Understanding Inference Dynamics in Tabular Foundation Models
- [可验证模型解释](../conferences/icml-2026/cards/0301-0400.md#boetius26a-evaluation) · Verified SHAP: Provable Bounds for Exact Shapley Values of Neural Networks
- [人评聚合](../conferences/icml-2026/cards/0301-0400.md#bonagiri26a-evaluation) · STABLEVAL: Disagreement-Aware and Stable Evaluation of AI Systems
- [共形覆盖诊断](../conferences/icml-2026/cards/0301-0400.md#braun26c-evaluation) · Conditional Coverage Diagnostics for Conformal Prediction
- [榜单评测前的统一微调](../conferences/icml-2026/cards/0601-0700.md#chen26gf-evaluation) · Leaderboard Incentives: Model Rankings under Strategic Post-Training
- [用合成记忆任务诊断可塑性](../conferences/icml-2026/cards/0601-0700.md#cheng26i-evaluation) · Local Redundancy: An Information-Theoretic Measure of Plasticity from Synthetic Memorization
- [元胞自动机可学习性的频谱诊断](../conferences/icml-2026/cards/0901-1000.md#disselhoff26a-evaluation) · Probing the Inductive Bias of Neural Networks through Learning Random Cellular Automata
- [序列状态跟踪的跨长度共享诊断](../conferences/icml-2026/cards/1001-1100.md#ebrahimi26a-evaluation) · On the "Induction Bias" in Sequence Models
- [沿 AdamW 训练路径联合归因](../conferences/icml-2026/cards/1001-1100.md#eichin26a-evaluation) · ExPLAIND: Unifying Model, Data, and Training Attribution to Study Model Behavior
- [时序预测的分频可预测性诊断](../conferences/icml-2026/cards/1101-1200.md#feng26u-evaluation) · Beyond Model Ranking: Predictability-Aligned Evaluation for Time Series Forecasting
- [评分模型的架构各向异性](../conferences/icml-2026/cards/1101-1200.md#floros26a-evaluation) · On the Anisotropy of Score-Based Generative Models
- [分布式数据归因的操纵鲁棒性](../conferences/icml-2026/cards/1201-1300.md#gao26k-evaluation) · On the Fragility of Data Attribution When Learning Is Distributed
- [条件生成的保形可靠性评分](../conferences/icml-2026/cards/1201-1300.md#gao26aa-evaluation) · Conformal Reliability: A New Evaluation Metric for Conditional Generation
- [扩散生成的训练样本邻近偏差](../conferences/icml-2026/cards/1201-1300.md#garnier-brun26a-evaluation) · Biased Generalization in Diffusion Models
- [表征相似度的置换零校准](../conferences/icml-2026/cards/1301-1400.md#groger26a-evaluation) · Revisiting the Platonic Representation Hypothesis: An Aristotelian View
- [按决策收益度量解释价值](../conferences/icml-2026/cards/1301-1400.md#guo26u-evaluation) · Explanations are a Means to an End: Decision Theoretic Explanation Evaluation
- [用全局兼容性筛查局部因果陈述](../conferences/icml-2026/cards/1801-1900.md#jahn26a-evaluation) · Evaluating Bivariate Causal Statements Based on Mutual Compatibility
- [把预文本假设拆成三种可测失效](../conferences/icml-2026/cards/1801-1900.md#jia26b-evaluation) · Quantitative Estimation of Target Task Performance from Unsupervised Pretext Task in Semi/Self-Supervised Learning
- [从预测分布到条件经验分布做非参数校准](../conferences/icml-2026/cards/2001-2100.md#jung26d-evaluation) · Nonparametric Distribution Regression Re-calibration
- [用统一搜索预算比较认证训练的整条前沿](../conferences/icml-2026/cards/2001-2100.md#kaulen26a-evaluation) · Rethinking Evaluation Paradigms in IBP-based Certified Training
- [在可逆频谱或趋势域内积分梯度](../conferences/icml-2026/cards/2001-2100.md#kechris26a-evaluation) · Time series saliency maps: Explaining models across multiple domains
- [借可信参考样本诊断异常输出机制](../conferences/icml-2026/cards/2001-2100.md#keenan26a-evaluation) · Mechanistic Anomaly Detection via Functional Attribution
- [分别控制训练样本和任务重叠以测表征相似性](../conferences/icml-2026/cards/2501-2600.md#li26gf-evaluation) · Causes and Consequences of Representational Similarity in Machine Learning Models
- [共同检验共形预测集大小与下游群体结果](../conferences/icml-2026/cards/2901-3000.md#liu26fp-evaluation) · Beyond Procedure: Substantive Fairness in Conformal Prediction
- [把联邦后门检测的重点放到聚合后的持续性](../conferences/icml-2026/cards/3101-3200.md#ma26k-evaluation) · Coupled Trigger Optimization and Vulnerable Parameter Alignment for Persistent Backdoor Attacks on Federated Learning
- [先集成预测函数再估特征重要性](../conferences/icml-2026/cards/3501-3600.md#paillard26a-evaluation) · Aggregate Models, Not Explanations: Improving Feature Importance Estimation
- [用态密度测随机插值与梯度泛化](../conferences/icml-2026/cards/3501-3600.md#pakman26a-evaluation) · Revisiting the Volume Hypothesis
- [结构因果基准取样](../conferences/icml-2026/cards/3501-3600.md#panayiotou26a-evaluation) · CausalProfiler: Generating Synthetic Benchmarks for Rigorous and Transparent Evaluation of Causal Machine Learning
- [扩散模型优先复现常见局部特征](../conferences/icml-2026/cards/3801-3900.md#rodriguez26a-evaluation) · Diffusion Models Preferentially Memorize Prototypical Examples or: Why Does My Diffusion Model Love Slop?
- [用随机区域统计比较条件分布](../conferences/icml-2026/cards/4001-4100.md#sharief26a-evaluation) · MIRA: A Score for Conditional Distribution Accuracy and Model Comparison
- [按模型互信息和阈值验证抽取后的所有权](../conferences/icml-2026/cards/4001-4100.md#shen26b-evaluation) · CREDIT: Certified Ownership Verification of Deep Neural Networks Against Model Extraction Attacks
- [用集合覆盖率检查假遗忘](../conferences/icml-2026/cards/4101-4200.md#shi26j-evaluation) · Tackling Fake Forgetting through Uncertainty Quantification
- [序关系表征对齐](../conferences/icml-2026/cards/4101-4200.md#soares26a-evaluation) · Scalable and Interpretable Representation Alignment with Ordinal Similarity
- [表征压缩干扰与鲁棒性](../conferences/icml-2026/cards/4201-4300.md#stevinson26a-evaluation) · Adversarial Vulnerability from Interference Between Features in Superposition
- [unseen-class-privacy-auditing](../conferences/icml-2026/cards/4401-4500.md#thaker26a-evaluation) · Membership Inference Attacks for Unseen Classes
- [ranking-calibration-hierarchy](../conferences/icml-2026/cards/4401-4500.md#thies26a-evaluation) · Calibrated Preference Learning: The Case of Label Ranking
- [生成公平必须比较组内质量](../conferences/icml-2026/cards/4501-4600.md#verine26a-evaluation) · Equalized Generative Treatment: Matching f-divergences for Fairness in Generative Models
- [分离语义保持脆弱性和原始误差](../conferences/icml-2026/cards/4501-4600.md#vilucchio26a-evaluation) · On the Existence of Consistent Adversarial Attacks in High-Dimensional Linear Classification
- [自适应客户端优化器的隐私评测边界](../conferences/icml-2026/cards/4501-4600.md#wan26c-evaluation) · Gradient Inversion Attacks Beyond SGD
- [配对条件下的模块归因](../conferences/icml-2026/cards/4601-4700.md#wang26ay-evaluation) · CombinationTS: A Modular Framework for Understanding Time-Series Forecasting Models
- [解释稳定不能替代决策稳健性](../conferences/icml-2026/cards/4701-4800.md#wang26es-evaluation) · Exposing Vulnerabilities in Explanation for Time Series Classifiers via Dual-Target Attacks
- [速度场差估计函数分布相对熵](../conferences/icml-2026/cards/4701-4800.md#wang26fx-evaluation) · Relative Entropy Estimation in Function Space: Theory and Applications to Trajectory Inference
- [概念方向与TCAV分数的不同采样预算](../conferences/icml-2026/cards/4901-5000.md#wenkmann26a-evaluation) · On the Variability of Concept Activation Vectors
- [末层与全网线性化UQ的成本边界](../conferences/icml-2026/cards/4901-5000.md#wilson26a-evaluation) · Is the Last Layer Sufficient for Uncertainty Quantification?
- [按因果等价类分配归因查询](../conferences/icml-2026/cards/4901-5000.md#witter26a-evaluation) · Exactly Computing do-Shapley Values
- [预训练目标与适配方式的配对诊断](../conferences/icml-2026/cards/5101-5200.md#xiong26f-evaluation) · EEG-FM-Bench: A Comprehensive Benchmark for the Systematic Evaluation and Diagnostic Analyses of EEG Foundation Models
- [SSL局部GGN响应的landmark归因](../conferences/icml-2026/cards/5601-5700.md#zarvandi26a-evaluation) · Interpretable Self-Supervised Learning via Representer Landmarks and Nyström Approximation
- [Wasserstein参考切向场的双统计监测](../conferences/icml-2026/cards/5701-5800.md#zeng26f-evaluation) · Beyond Euclidean Summaries: Online Change Point Detection for Distribution-Valued Data
- [mergeability预测按merger与partner验证](../conferences/icml-2026/cards/6201-6300.md#zhou26bo-evaluation) · Demystifying Mergeability: Interpretable Properties to Predict Model Merging Success
- [固定组合decoder后的神经分数归因](../conferences/icml-2026/cards/6301-6400.md#chakraborty26d-evaluation) · Position: Neural Approximation Is Rarely Justified for Hard Combinatorial Problems
- [数据重采样与seed双层UQ参照](../conferences/icml-2026/cards/6401-6500.md#jimenez26a-evaluation) · Position: Epistemic Uncertainty Estimation Methods are Fundamentally Incomplete
- [先匹配forecasting局部参数与协变量再比层](../conferences/icml-2026/cards/6401-6500.md#moretti26a-evaluation) · Position: Current Benchmarking Hinders Real Progress in Deep Learning for Time Series Forecasting
- [模型平均领先之外检验任务分布与移除敏感性](../conferences/icml-2026/cards/6401-6500.md#oh26d-evaluation) · Position: State-of-the-Art Claims Require State-of-the-Art Evidence
- [拓扑表征先控制filtration再比较下游编码](../conferences/icml-2026/cards/6401-6500.md#rieso26a-evaluation) · Position: Topological Machine Learning Cannot Progress without Experimental Standards

<a id="by-graph-and-recommendation"></a>

### 图学习与推荐

- [图 Mixup 插值质量诊断](../conferences/icml-2026/cards/1101-1200.md#forbat26a-evaluation) · Is Graph Mixup Beneficial? Investigating Interpolation And Empirical Performance of Graph Mixup Methods
- [用图对齐替身摊薄重复归因开销](../conferences/icml-2026/cards/1501-1600.md#heidari26a-evaluation) · TN-SHAP-G: Graph-Structured Tensor Network Surrogates for Shapley Values and Interactions
- [回溯时序图节点记忆中的早期事件贡献](../conferences/icml-2026/cards/2901-3000.md#liu26gd-evaluation) · Towards the Explainability of Temporal Graph Networks via Memory Backtracking and Topological Attribution
- [众包事实核查桥接排序的抗操控审计](../conferences/icml-2026/cards/3901-4000.md#selvam26a-evaluation) · Gaming Consensus: Coordinated Manipulation in Crowdsourced Fact-Checking
- [图合成序列上的推荐CPT条件scaling](../conferences/icml-2026/cards/5901-6000.md#zhang26ih-evaluation) · Principled Synthetic Data Enables the First Scaling Laws for LLMs in Recommendation

<a id="by-scientific-ml"></a>

### 科学机器学习

- [分层诊断健康信号推理能力](../conferences/icml-2026/cards/2601-2700.md#li26hr-evaluation) · HEARTS: Benchmarking LLM Reasoning on Health Time Series
- [区分 RNA 表征复用与优化初始化](../conferences/icml-2026/cards/2601-2700.md#li26if-evaluation) · Understanding Transfer Learning of RNA Foundation Models on Downstream Tasks
- [用键长扫描的势能面平滑度指导原子势架构](../conferences/icml-2026/cards/2801-2900.md#liu26df-evaluation) · From Evaluation to Design: Using Potential Energy Surface Smoothness Metrics to Guide ML Interatomic Potential Architectures
- [晶体结构操作评测](../conferences/icml-2026/cards/3101-3200.md#lv26b-evaluation) · AtomWorld: A Benchmark for Evaluating Spatial Reasoning in Large Language Models on Material Structures
- [融合物理与约束证据解释控制动作](../conferences/icml-2026/cards/3301-3400.md#naagarajan26a-evaluation) · Hierarchical Causal Abduction: A Foundation Framework for Explainable Model Predictive Control
- [用概念重组测试分布外时序解释](../conferences/icml-2026/cards/3501-3600.md#oublal26a-evaluation) · TimeSAE: Causal Sparse Decoding for Faithful Explanations of Black-Box Time Series Models
- [rate-whitened-observable-alignment](../conferences/icml-2026/cards/4501-4600.md#ugalde26a-evaluation) · A Geometric Lens on Physics-Aligned Data Compression
- [按训练区间选择SciML优化器](../conferences/icml-2026/cards/4601-4700.md#wang26cc-evaluation) · Unveiling Multi-regime Patterns in SciML: Distinct Failure Modes and Regime-specific Optimization
- [几何探针指导算子重注入](../conferences/icml-2026/cards/5101-5200.md#xia26a-evaluation) · Do Neural Operators Forget Geometry? The Forgetting Hypothesis in Deep Operator Learning
- [极端物理regime的共享线性解码诊断](../conferences/icml-2026/cards/5401-5500.md#yao26k-evaluation) · The Perception–Physics Paradox: Probing Scientific Alignment with TC-Bench
- [用无上下文与错配对照验证预测context](../conferences/icml-2026/cards/6101-6200.md#zheng26n-evaluation) · Overcoming the Modality Gap in Context-Aided Forecasting
- [预训练表征要对照随机encoder并检查稀有标签影响](../conferences/icml-2026/cards/6301-6400.md#berger26a-evaluation) · Position: Evaluation of ECG Representations Must Be Fixed
- [同MAE下浮点精度的导数与谱序检查](../conferences/icml-2026/cards/6301-6400.md#cho26k-evaluation) · Position: Significant impact of numerical precision in scientific machine learning
- [域与horizon分层的TSFM选型](../conferences/icml-2026/cards/6501-6552.md#syed26a-evaluation) · Position: Time-Series Foundation Models Require Explicit Domain-Level Benchmarks
- [把预处理配置作为观测模型做跨数据稳定性审计](../conferences/icml-2026/cards/6501-6552.md#zhan26g-evaluation) · Position: AI for Science Should Treat Measurement-to-Dataset Pipelines as Inference Components
<!-- classification:end -->
