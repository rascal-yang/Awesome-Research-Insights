# 训练策略

[首页](../README.md) · [参与贡献](../CONTRIBUTING.md) · [English](../en/insights/training-strategies.md)

训练日程、课程学习与多阶段训练。

<!-- classification:start -->
## 按研究领域浏览

[大语言模型](#by-llm) · [计算机视觉](#by-computer-vision) · [自然语言处理](#by-nlp) · [强化学习](#by-reinforcement-learning) · [机器人学](#by-robotics) · [多模态学习](#by-multimodal) · [机器学习基础与统计](#by-ml-foundations) · [图学习与推荐](#by-graph-and-recommendation) · [科学机器学习](#by-scientific-ml)

<a id="by-llm"></a>

### 大语言模型

- [参数高效微调](../conferences/icml-2026/cards/0001-0100.md#adepu26a-training-strategies) · Fine-Tuning of Transformer models with Frames
- [激活干预](../conferences/icml-2026/cards/0001-0100.md#adila26a-training-strategies) · Weight Updates as Activation Shifts: A Principled Framework for Steering
- [离散扩散加速](../conferences/icml-2026/cards/0001-0100.md#amin26a-training-strategies) · Consistent Diffusion Language Models
- [递归潜空间推理](../conferences/icml-2026/cards/0101-0200.md#asadulaev26a-training-strategies) · Latent Reasoning in TRMs is Secretly a Policy Improvement Operator
- [黑盒模型适配](../conferences/icml-2026/cards/0101-0200.md#asawa26a-training-strategies) · How to Train Your Advisor: Steering Black-Box LLMs with Advisor Models
- [激活控制](../conferences/icml-2026/cards/0201-0300.md#bao26b-training-strategies) · Towards Steering without Sacrifice: Principled Training of Steering Vectors for Prompt-only Interventions
- [技能持续学习](../conferences/icml-2026/cards/0201-0300.md#berthon26a-training-strategies) · Skill Neologisms: Towards Skill-based Continual Learning
- [测试时语言模型学习](../conferences/icml-2026/cards/0201-0300.md#bian26b-training-strategies) · Future-Gain Guided Test-Time Learning for Large Language Models
- [Transformer 到 SSM 蒸馏](../conferences/icml-2026/cards/0201-0300.md#bick26a-training-strategies) · Retrieval-Aware Distillation for Transformer-SSM Hybrids
- [持续预训练](../conferences/icml-2026/cards/0301-0400.md#borodin26a-training-strategies) · Diffract: Spectral View of LLM Domain Adaptation
- [推理后训练课程](../conferences/icml-2026/cards/0301-0400.md#bu26a-training-strategies) · Provable Sample Efficiency of Curriculum Post-Training for Transformer Reasoning
- [渐进式模型训练](../conferences/icml-2026/cards/0301-0400.md#bu26c-training-strategies) · Scaling depth capacity via zero/one-layer model expansion
- [微调泛化干预](../conferences/icml-2026/cards/0401-0500.md#casademunt26a-training-strategies) · Steering Out-of-Distribution Generalization with Concept Ablation Fine-Tuning
- [监督微调与强化学习协同](../conferences/icml-2026/cards/0501-0600.md#chen26an-training-strategies) · Beyond Two-Stage Training: Cooperative SFT and RL for LLM Reasoning
- [知识纠错与置信校准](../conferences/icml-2026/cards/0501-0600.md#chen26ap-training-strategies) · Know More, Know Clearer: A Meta-Cognitive Framework for Knowledge Augmentation in Large Language Models
- [4 位训练权重振荡](../conferences/icml-2026/cards/0501-0600.md#chen26cl-training-strategies) · TetraJet-v2: Accurate NVFP4 Training for Large Language Models with Oscillation Suppression and Outlier Control
- [后训练的近似在策略数据](../conferences/icml-2026/cards/0501-0600.md#chen26do-training-strategies) · Retaining by Doing: The Role of On-Policy Data in Mitigating Forgetting
- [拒答引导的激活对抗训练](../conferences/icml-2026/cards/0601-0700.md#chen26em-training-strategies) · Steering Beyond the Support: Adversarial Training on Unsupervised Jailbroken Activation Simulation
- [代码风险节点的树式自对弈](../conferences/icml-2026/cards/0601-0700.md#chen26gc-training-strategies) · Learn from Your Mistakes: Tree-like Self-Play for Secure Code LLMs
- [多智能体的隐私偏好构造](../conferences/icml-2026/cards/0601-0700.md#cheng26o-training-strategies) · PrivAct: Internalizing Contextual Privacy Preservation via Multi-Agent Preference Training
- [按梯度冲突拆分指令微调](../conferences/icml-2026/cards/0701-0800.md#choi26g-training-strategies) · Decentralized Instruction Tuning: Conflict-Aware Splitting and Weight Merging
- [跨架构模型的激活对齐合并](../conferences/icml-2026/cards/0801-0900.md#cui26j-training-strategies) · Transport and Merge: Cross-Architecture Merging for Large Language Models
- [多题上下文诱导的短推理蒸馏](../conferences/icml-2026/cards/0801-0900.md#deng26m-training-strategies) · ConPress: Learning Efficient Reasoning from Multi-Question Contextual Pressure
- [置信度加权的 LoRA 秩规划](../conferences/icml-2026/cards/0901-1000.md#ding26h-training-strategies) · CSPLoRA: Confidence-Guided Structural Planning for Low-Rank Adaptation
- [LoRA 的双因素层间秩分配](../conferences/icml-2026/cards/0901-1000.md#ding26y-training-strategies) · COBRA: Contribution-Based Bayesian Rank Allocation for Parameter-Efficient Fine-Tuning
- [联邦微调的索引重叠后门筛查](../conferences/icml-2026/cards/0901-1000.md#dogani26a-training-strategies) · INDEXGUARD: Index-only Backdoor Vetting for Secure Federated PEFT of Large Language Models
- [逐层和逐时调度随机深度](../conferences/icml-2026/cards/1001-1100.md#elhoushi26a-training-strategies) · Don’t Drop Dropout: Optimizing Layer Sparsity for Efficient LLM Training and Inference
- [保留用户决策权的建议训练](../conferences/icml-2026/cards/1001-1100.md#ellis26a-training-strategies) · Training LLM Agents to Empower Humans
- [FP8 注意力的谱范数缩放](../conferences/icml-2026/cards/1001-1100.md#emadi26a-training-strategies) · Rank-Aware Spectral Bounds on Attention Logits for Stable Low-Precision Training
- [长思维链蒸馏的梯度谱筛选](../conferences/icml-2026/cards/1001-1100.md#fan26e-training-strategies) · Uncovering the Gradient Geometry of Long CoT: A Spectral-guided Approach to Reasoning Distillation
- [异构联邦微调的 LoRA 子矩阵](../conferences/icml-2026/cards/1001-1100.md#fang26e-training-strategies) · Federated Sketching LoRA: A Flexible Framework for Heterogeneous Collaborative Fine-Tuning of LLMs
- [偏好对齐中的负例遗忘权重](../conferences/icml-2026/cards/1101-1200.md#feng26f-training-strategies) · Leveraging Machine Unlearning for Cost-Efficient Preference Alignment
- [自回归转扩散的位置相关掩码](../conferences/icml-2026/cards/1101-1200.md#fu26q-training-strategies) · Efficient-DLM: From Autoregressive to Diffusion Language Models, and Beyond in Speed
- [单样本自生成熵最小化](../conferences/icml-2026/cards/1201-1300.md#gao26d-training-strategies) · One-shot Entropy Minimization for Language Model Reasoning
- [上下文并行的按头显存复用](../conferences/icml-2026/cards/1201-1300.md#ghadia26a-training-strategies) · Untied Ulysses: Memory-Efficient Context Parallelism via Headwise Chunking
- [推理链的分段合并与补全](../conferences/icml-2026/cards/1301-1400.md#gui26a-training-strategies) · Short Chains, Deep Thoughts: Balancing Reasoning Efficiency and Intra-Segment Capability via Split-Merge Optimization
- [安全微调的缓冲与正交合并](../conferences/icml-2026/cards/1401-1500.md#ham26a-training-strategies) · Jailbreak to Protect: Buffering and Reinforcing via Temporary Jailbreaking for Safe Fine-Tuning in Large Language Models
- [预训练权重衰减与下游可塑性](../conferences/icml-2026/cards/1401-1500.md#han26b-training-strategies) · Weight Decay Improves Language Model Plasticity
- [对话中的反对意见建模](../conferences/icml-2026/cards/1401-1500.md#han26s-training-strategies) · ToMAP: Training Opponent-Aware LLM Persuaders with Theory of Mind
- [先对齐混合学生隐状态，再蒸馏并合并专家](../conferences/icml-2026/cards/1401-1500.md#hauzenberger26a-training-strategies) · Effective Distillation to Hybrid xLSTM Architectures
- [蒸馏投影的激活感知初始化](../conferences/icml-2026/cards/1501-1600.md#he26aj-training-strategies) · Reasoning-preserved Efficient Distillation of Large Language Models via Activation-aware Initialization
- [用可微共形流程学习断言评分，再切回硬校准](../conferences/icml-2026/cards/1501-1600.md#hittesdorf26a-training-strategies) · Differentiable Conformal Training for LLM Reasoning Factuality
- [从自身 Jacobi 轨迹蒸馏保持因果的多词元预测](../conferences/icml-2026/cards/1601-1700.md#hu26aa-training-strategies) · Fast and Accurate Causal Parallel Decoding using Jacobi Forcing
- [用可辨识的掩码区间安排扩散语言模型训练预算](../conferences/icml-2026/cards/1701-1800.md#huang26an-training-strategies) · Tuning the Implicit Regularizer of Masked Diffusion Language Models: Enhancing Generalization via Insights from $k$-Parity
- [用词元扰动验证当前代码步骤真正依赖的计划线索](../conferences/icml-2026/cards/1701-1800.md#huang26ar-training-strategies) · PADA-Coder: Improving Plan-Following Code Generation via Perturbation-Verified Attention Distillation and Dynamic Alignment
- [用标注者可靠性加权语言模型偏好学习](../conferences/icml-2026/cards/1701-1800.md#huang26co-training-strategies) · Reliability-Aware LLM Alignment from Inconsistent Human Feedback
- [用可恢复损失给任务向量加权](../conferences/icml-2026/cards/1801-1900.md#im26b-training-strategies) · Post-Hoc Merging is Not Enough: Many-Shot Model Merging with Loss-Gap Balancing
- [用事后复盘监督时点受限预测](../conferences/icml-2026/cards/1801-1900.md#jajal26a-training-strategies) · Global Merger-Arbitrage Forecasting with Language Models
- [分开监督推理与证据定位置信度](../conferences/icml-2026/cards/1801-1900.md#jang26a-training-strategies) · Confidence is Not Universal: Task-Dependent Calibration and Emergent Behavior in LLMs
- [按 MoE 参数组缩放超参数再迁移](../conferences/icml-2026/cards/1901-2000.md#jiang26a-training-strategies) · Hyperparameter Transfer with Mixture-of-Experts Layers
- [按安全配置改变标签并维护严重度排序](../conferences/icml-2026/cards/1901-2000.md#jiang26v-training-strategies) · Configurable Reward Model for Balanced Safety Alignment
- [把少量可程序生成的结构任务放到预训练开头](../conferences/icml-2026/cards/1901-2000.md#jiang26ap-training-strategies) · Procedural Pretraining: Warming Up Language Models with Abstract Data
- [让扩散预训练掩码随模型成熟度改变](../conferences/icml-2026/cards/1901-2000.md#jing26g-training-strategies) · InfoDLM: an Information-Adaptive Framework for Discrete Diffusion Language Model Pretraining
- [按安全与失准模型的似然差挑交错样本](../conferences/icml-2026/cards/2001-2100.md#kaczer26a-training-strategies) · In-Training Defenses Against Emergent Misalignment in Language Models
- [将批评当训练条件来教模型改答案](../conferences/icml-2026/cards/2001-2100.md#kapusuzoglu26a-training-strategies) · Critique-Guided Distillation for Robust Reasoning via Refinement
- [用宏动作缩短有效决策长度](../conferences/icml-2026/cards/2001-2100.md#kim26h-training-strategies) · On Training Large Language Models for Long-Horizon Tasks: An Empirical Study of Horizon Length
- [按词表双射重编码并通过 API 适配模型](../conferences/icml-2026/cards/2101-2200.md#kim26v-training-strategies) · AlienLM: Alienization of Language for API-Boundary Privacy in Black-Box LLMs
- [摊销预测分布的早期漂移](../conferences/icml-2026/cards/2101-2200.md#kim26ah-training-strategies) · From Drift to Coherence: Stabilizing Beliefs in LLMs
- [让用户通过看样例逐步形成意图](../conferences/icml-2026/cards/2101-2200.md#kim26av-training-strategies) · DiscoverLLM: From Executing Intents to Discovering Them
- [联邦偏好对齐的个性化混合先验](../conferences/icml-2026/cards/2201-2300.md#koo26a-training-strategies) · Federated Variational Preference Alignment with Gumbel-Softmax Prior for Personalized User Preferences
- [让教师从学生自己走到的状态接管](../conferences/icml-2026/cards/2201-2300.md#lauffer26a-training-strategies) · Imitation Learning for Multi-turn LM Agents via On-policy Expert Corrections
- [用可补算的数据分片抵消同步训练故障](../conferences/icml-2026/cards/2301-2400.md#lee26c-training-strategies) · SPARe: Stacked Parallelism with Adaptive Reordering for Fault-Tolerant LLM Pretraining Systems with 100k+ GPUs
- [在相同推理轨迹上稳住 FP4 的低熵决策](../conferences/icml-2026/cards/2301-2400.md#lee26an-training-strategies) · ReQAT: Achieving Full-Precision Reasoning Accuracy with 4-bit Floating-Point Quantization-Aware Training
- [在末块量化时直接校准词表分布](../conferences/icml-2026/cards/2301-2400.md#lee26bi-training-strategies) · LFQ: Logit-aware Final-block Quantization for Boosting the Generation Quality of Low-Bit Quantized LLMs
- [让低秩适配器在多解续写中分工](../conferences/icml-2026/cards/2301-2400.md#letzelter26a-training-strategies) · Multiple Choice Learning of Low-Rank Adapters for Language Modeling
- [微调末几层改变贪婪解码的上下文排序](../conferences/icml-2026/cards/2401-2500.md#li26af-training-strategies) · Beyond Temperature: Hyperfitting as a Late-Stage Geometric Expansion
- [离散扩散语言模型的逆向蒸馏](../conferences/icml-2026/cards/2401-2500.md#li26az-training-strategies) · IDLM: Inverse-distilled Diffusion Language Models
- [自博弈题目的解法多样性](../conferences/icml-2026/cards/2401-2500.md#li26bh-training-strategies) · R-Diverse: Mitigating Diversity Illusion in Self-Play LLM Training
- [扰动 RoPE 位置索引并要求两次预测一致](../conferences/icml-2026/cards/2401-2500.md#li26cs-training-strategies) · Shuffle the Context: RoPE-Perturbed Self-Distillation for Long-Context Adaptation
- [语义与偏好双轴课程的层间监控](../conferences/icml-2026/cards/2501-2600.md#li26ds-training-strategies) · Layer-wise Gradient Disentanglement: Decoupling Semantics and Preferences in Direct Preference Optimization
- [按证明闭合反馈区分有效战术](../conferences/icml-2026/cards/2501-2600.md#li26ek-training-strategies) · OptProver: Bridging Olympiad and Optimization through Continual Training in Formal Theorem Proving
- [为草稿训练拆开目标模型执行](../conferences/icml-2026/cards/2601-2700.md#li26hf-training-strategies) · SpecForge: A Flexible and Efficient Open-Source Training Framework for Speculative Decoding
- [用无角色预测稳定安全决策](../conferences/icml-2026/cards/2601-2700.md#li26hh-training-strategies) · Disentangling Intent from Role: Adversarial Self-Play for Persona-Invariant Safety Alignment
- [先保持对话连续抽取激活再混合训练](../conferences/icml-2026/cards/2601-2700.md#li26ik-training-strategies) · Breaking the Block: Preserving Data Continuity to Train Superior SAEs for Instruct Models
- [先从符号任务学程序再用自然语言适配](../conferences/icml-2026/cards/2701-2800.md#lin26k-training-strategies) · Can Large Language Models Generalize Procedures Across Representations?
- [在零空间内重定向需要遗忘的事实](../conferences/icml-2026/cards/2701-2800.md#lin26ap-training-strategies) · ZeroUnlearn: Few-Shot Knowledge Unlearning in Large Language Models
- [以差分隐私处理提示再用潜变量条件生成代码](../conferences/icml-2026/cards/2801-2900.md#liu26ao-training-strategies) · PrivCode++: Latent-Conditioned Differentially Private Code Generation for Comprehensive Guarantees
- [让规划和执行一致度参与代理训练样本加权](../conferences/icml-2026/cards/2801-2900.md#liu26az-training-strategies) · CoPE: A Framework for Optimizing Coordination between Planning and Execution in LLM-based Agents
- [在冷启动时限制专家令牌的概率跃升](../conferences/icml-2026/cards/2801-2900.md#liu26bm-training-strategies) · Clipping Low-Probability Tokens in SFT Yields a Generalizable Initialization for RL
- [按共同字符区间稀疏对齐跨词表蒸馏](../conferences/icml-2026/cards/2801-2900.md#liu26bw-training-strategies) · Entropy-aware Span-Constrained Optimal Transport for Robust Cross-Tokenizer Knowledge Distillation
- [融合预测与上下文的潜变量推理](../conferences/icml-2026/cards/2801-2900.md#liu26cv-training-strategies) · Latent Thoughts Tuning: Bridging Context and Reasoning with Fused Information in Latent Tokens
- [混合中训衔接通用预训练与专域后训练](../conferences/icml-2026/cards/2801-2900.md#liu26cz-training-strategies) · Midtraining Bridges Pretraining and Posttraining Distributions
- [复用跨域频繁激活的 MoE 专家初始化目标模型](../conferences/icml-2026/cards/2901-3000.md#liu26dr-training-strategies) · XPERT: Expert Knowledge Transfer for Effective Training of Language Models
- [用执行结果训练生成可组合的规划架构](../conferences/icml-2026/cards/2901-3000.md#liu26fz-training-strategies) · TodoEvolve: Learning to Architect Agent Planning Systems
- [推理轨迹几何水印](../conferences/icml-2026/cards/3001-3100.md#lu26q-training-strategies) · Echoes within the Reasoning: Stealthy and Effective Watermarking via Chain of Thought
- [从任务演示初始化可优化的上下文缓存](../conferences/icml-2026/cards/3001-3100.md#lu26ag-training-strategies) · Context Tuning for In-Context Optimization
- [按学生首个错误蒸馏工具推理](../conferences/icml-2026/cards/3101-3200.md#lyu26j-training-strategies) · Student-Centered Distillation Narrows the Agentic Gap Between Small and Large LLMs
- [通过撤销标记学习可回退的自回归生成](../conferences/icml-2026/cards/3101-3200.md#ma26ad-training-strategies) · Non-Monotonic Autoregressive Sequence Model
- [按任务相似度共享适配器子空间](../conferences/icml-2026/cards/3101-3200.md#magakyan26a-training-strategies) · Collaborative and Efficient Fine-tuning: Leveraging Task Similarity
- [用非均匀质心做极低位宽量化训练](../conferences/icml-2026/cards/3201-3300.md#maskey26a-training-strategies) · 1-Bit Wonder: Improving QAT Performance in the Low-Bit Regime through K-Means Quantization
- [专家推理自蒸馏](../conferences/icml-2026/cards/3201-3300.md#mendes26b-training-strategies) · Making Expert Reasoning Learnable with Self-Distillation
- [同伴成功轨迹的交叉教学](../conferences/icml-2026/cards/3301-3400.md#mishra26a-training-strategies) · CoRe: Collaborative Reasoning via Cross Teaching
- [用回报重要性权重把多轮 RL 转为离线微调](../conferences/icml-2026/cards/3301-3400.md#mu26b-training-strategies) · DRIFT: Decoupled Rollouts and Importance-Weighted Fine-Tuning for Efficient Multi-Turn Optimization
- [用交互稀疏度解释并改善深层 LLM 利用率](../conferences/icml-2026/cards/3301-3400.md#muhtar26a-training-strategies) · When Does Sparsity Mitigate the Curse of Depth in LLMs
- [从小模型微调更新生成大模型更新](../conferences/icml-2026/cards/3401-3500.md#nguyen26r-training-strategies) · Gradient Transformer: Learning to Generate Updates for LLMs
- [为量化跳层保留训练路径多样性](../conferences/icml-2026/cards/3401-3500.md#noh26a-training-strategies) · QTALE: Quantization-Robust Token-Adaptive Layer Execution for LLMs
- [用同句的有无前缀蒸馏更新事实](../conferences/icml-2026/cards/3501-3600.md#padmanabhan26a-training-strategies) · Updating Parametric Knowledge with Context Distillation Retains Post-Training Capabilities
- [让掩码难度随可用上下文变化](../conferences/icml-2026/cards/3501-3600.md#parashar26a-training-strategies) · Learnability-Informed Fine-Tuning of Diffusion Language Models
- [迭代蒸馏每个场景内的低遗憾轨迹](../conferences/icml-2026/cards/3501-3600.md#park26b-training-strategies) · Post-Training LLMs as Better Decision-Making Agents: A Regret-Minimization Approach
- [工具轨迹特权蒸馏](../conferences/icml-2026/cards/3601-3700.md#penaloza26a-training-strategies) · Privileged Information Distillation for Language Models
- [由教师激活初始化稀疏专家路由](../conferences/icml-2026/cards/3601-3700.md#peng26l-training-strategies) · PADD: Path-Aligned Decompression Distillation for Non-Router Teacher to Guide MoE Student Learning
- [按 Fisher 冲突筛选联邦 LoRA 上行层](../conferences/icml-2026/cards/3701-3800.md#qiu26w-training-strategies) · Less Is More in Federated Continual Learning: RieSelect for Conflict-Aware Layer Selection in LLMs
- [本地蒸馏平滑数据差异，全局原始数据校正事实](../conferences/icml-2026/cards/3801-3900.md#ren26n-training-strategies) · FedSDR: Federated Self-Distillation with Rectification
- [在并行扩散初稿后做最小编辑修复一致性](../conferences/icml-2026/cards/3801-3900.md#ren26t-training-strategies) · Edit-Based Refinement for Parallel Masked Diffusion Language Models
- [在预训练梯度路由中建立可组合权限](../conferences/icml-2026/cards/3801-3900.md#roland26a-training-strategies) · Modular Pretraining Enables Access Control
- [兼顾通用和长上下文的中期训练](../conferences/icml-2026/cards/3901-4000.md#runwal26a-training-strategies) · PRISM: Demystifying Retention and Interaction in Mid-Training
- [弱奖励训练前先恢复正确探索](../conferences/icml-2026/cards/3901-4000.md#ryd26a-training-strategies) · Removing Sandbagging in LLMs by Training with Weak Supervision
- [用预训练与专业续训的联合扩展律选拆分点](../conferences/icml-2026/cards/4001-4100.md#seto26a-training-strategies) · Optimal Splitting of Language Models from Mixtures to Specialized Domains
- [用历史检查点的自生成轨迹缓解静态监督错配](../conferences/icml-2026/cards/4001-4100.md#shahroz26a-training-strategies) · TMS: Trajectory-Mixed Supervision for On-Policy Self Distillation
- [长上下文语言模型的训练推理分段一致性](../conferences/icml-2026/cards/4001-4100.md#shang26c-training-strategies) · Training–Inference Consistent Segmented Execution for Long-Context LLMs
- [按旧偏好冲突类型重用已有对齐数据](../conferences/icml-2026/cards/4001-4100.md#sharma26c-training-strategies) · The Realignment Problem: When Right becomes Wrong in LLMs
- [从训练轨迹选择蒸馏词元](../conferences/icml-2026/cards/4001-4100.md#shen26i-training-strategies) · Training-Trajectory-Aware Token Selection
- [对齐稀疏与全注意的输出特征](../conferences/icml-2026/cards/4001-4100.md#shen26k-training-strategies) · SSA: Sparse Sparse Attention by Aligning Full and Sparse Attention Outputs in Feature Space
- [把各目标保留为共享主干上的独立头](../conferences/icml-2026/cards/4001-4100.md#shen26v-training-strategies) · Simultaneous Multi-objective Alignment Across Verifiable and Non-verifiable Rewards
- [让带示例的同一模型指导学生轨迹](../conferences/icml-2026/cards/4001-4100.md#shenfeld26a-training-strategies) · Self-Distillation Enables Continual Learning
- [在每个新任务开始前重选训练提示](../conferences/icml-2026/cards/4101-4200.md#shi26c-training-strategies) · Training Prompt Matters: State-Adaptive Optimization for Robust Fine-Tuning
- [同步增加数据难度与深度](../conferences/icml-2026/cards/4101-4200.md#singh26a-training-strategies) · Curriculum-Guided Layer Scaling for Language Model Pretraining
- [语义边缘锚定后训练](../conferences/icml-2026/cards/4201-4300.md#springer26a-training-strategies) · Annotations Mitigate Post-Training Mode Collapse
- [MoE对齐的专家容量分配](../conferences/icml-2026/cards/4201-4300.md#sun26m-training-strategies) · MESA: Improving MoE Safety Alignment via Decentralized Expertise
- [trajectory-aware-gui-judge](../conferences/icml-2026/cards/4201-4300.md#sun26w-training-strategies) · SEAgent: Self-Evolving Computer Use Agent with Autonomous Learning from Experience
- [lie-bracket-curriculum](../conferences/icml-2026/cards/4301-4400.md#sweeney26a-training-strategies) · The Geometry of Sequential Learning: Lie-Bracket Prediction of Transfer Order
- [选择性反向prompt更新](../conferences/icml-2026/cards/4401-4500.md#tiwari26a-training-strategies) · Turning Back Without Forgetting: Selective Backward Refinement for Parameter-Efficient Continual Learning
- [单调部分上下文流式训练](../conferences/icml-2026/cards/4401-4500.md#tong26n-training-strategies) · ProactiveLLM: Learning Active Interaction for Streaming Large Language Models
- [random-clipping-with-matched-accounting](../conferences/icml-2026/cards/4501-4600.md#ullah26a-training-strategies) · Efficient DP-SGD for LLMs with Randomized Clipping
- [上下文长短构造无奖励偏好](../conferences/icml-2026/cards/4501-4600.md#wan26a-training-strategies) · Mitigating Conversational Inertia in Multi-Turn Agents
- [When RL Meets Adaptive Speculative Training: A Unified Training-Serving System](../conferences/icml-2026/cards/4501-4600.md#wang26j-training-strategies) · When RL Meets Adaptive Speculative Training: A Unified Training-Serving System
- [按收敛状态选择扩深方式](../conferences/icml-2026/cards/4601-4700.md#wang26aq-training-strategies) · Beyond Sunk Costs: Boosting LLM Pre-training Efficiency via Orthogonal Growth of Mixture-of-Experts
- [蒸馏按局部不确定性分配硬软监督](../conferences/icml-2026/cards/4601-4700.md#wang26cw-training-strategies) · The Bridge-Garden Dilemma in LLM Distillation: Why Mixing Hard and Soft Labels Works
- [gradient-component-regrouping](../conferences/icml-2026/cards/4701-4800.md#wang26ds-training-strategies) · Decomposing the Basic Abilities of Large Language Models: Mitigating Cross-Task Interference in Multi-Task Instruct-Tuning
- [答案充分性指导推理压缩](../conferences/icml-2026/cards/4701-4800.md#wang26dz-training-strategies) · SuCo: Sufficiency-guided Continuous Adaptive Reasoning
- [随机演员屏蔽促工作流探索](../conferences/icml-2026/cards/4701-4800.md#wang26eg-training-strategies) · Beyond Static Pipelines: Learning Dynamic Workflows for Text-to-SQL
- [按序列拆分多token输出头以平衡流水](../conferences/icml-2026/cards/4701-4800.md#wang26gy-training-strategies) · AdaHC: Accelerating Multi-Token Prediction with Adaptive Head Chunking with Pipeline Parallelism
- [逐头长度温度与位置校准时机](../conferences/icml-2026/cards/4901-5000.md#wang26lk-training-strategies) · AdaRoPE: Not All Attention Heads Should Rotate and Scale Equally

<a id="by-computer-vision"></a>

### 计算机视觉

- [少步生成蒸馏](../conferences/icml-2026/cards/0101-0200.md#bai26n-training-strategies) · Optimizing Few-Step Generation with Adaptive Matching Distillation
- [长视频生成](../conferences/icml-2026/cards/0301-0400.md#cai26h-training-strategies) · Mode Seeking meets Mean Seeking for Fast Long Video Generation
- [动态参数高效微调](../conferences/icml-2026/cards/0301-0400.md#cao26o-training-strategies) · Beyond Static Allocation: Dynamic Sensitivity-Aware Fine-Tuning for Vision Transformers
- [端侧文生图蒸馏](../conferences/icml-2026/cards/0401-0500.md#chavhan26a-training-strategies) · NanoFLUX: Distillation-Driven Compression of Large Text-to-Image Generation Models for Mobile Devices
- [视图一致的三维 VAE 稀疏训练](../conferences/icml-2026/cards/0501-0600.md#chen26cn-training-strategies) · Focusing: View-Consistent Sparse Voxels for Efficient 3D VAE Training
- [高斯泼溅的瞬态区域筛除](../conferences/icml-2026/cards/0501-0600.md#chen26dm-training-strategies) · 3DGS-HPC: Distractor-free 3D Gaussian Splatting with Hybrid Patch-wise Classification
- [长上下文视频蒸馏](../conferences/icml-2026/cards/0601-0700.md#chen26eu-training-strategies) · Context Forcing: Consistent Autoregressive Video Generation with Long Context
- [图像词元化与生成联合训练](../conferences/icml-2026/cards/0701-0800.md#chu26b-training-strategies) · End-to-End Autoregressive Image Generation with 1D Semantic Tokenizer
- [稀疏软标签的硬标签校准](../conferences/icml-2026/cards/0701-0800.md#cui26g-training-strategies) · Hard Labels In! Rethinking the Role of Hard Labels in Mitigating Local Semantic Drift
- [多帧插值扩散的一步蒸馏](../conferences/icml-2026/cards/0901-1000.md#ding26t-training-strategies) · SpeedVFI: One-step Diffusion for Efficient Video Frame Interpolation
- [高斯泼溅的误差引导像素采样](../conferences/icml-2026/cards/0901-1000.md#dong26k-training-strategies) · TurboGS: Accelerating 3D Gaussian Splatting via Error-Guided Sparse Pixel Sampling and Optimization
- [视觉基础特征的压缩生成与细化](../conferences/icml-2026/cards/0901-1000.md#dong26l-training-strategies) · RePack then Refine: Efficient Diffusion Transformers with Vision Foundation Models
- [统一图像取证的受限低秩适配](../conferences/icml-2026/cards/0901-1000.md#du26g-training-strategies) · Can We Build a Monolithic Model for Fake Image Detection? SICA: Semantic-Induced Constrained Adaptation for Unified-Yet-Discriminative Artifact Feature Space Reconstruction
- [视频扩散的三维一致性偏好](../conferences/icml-2026/cards/0901-1000.md#du26q-training-strategies) · VideoGPA: Distilling Geometry Priors for 3D-Consistent Video Generation
- [由图像功率谱确定扩散日程](../conferences/icml-2026/cards/1001-1100.md#esteves26a-training-strategies) · Spectrally-Guided Diffusion Noise Schedules
- [物理平面光照监督的补光条件](../conferences/icml-2026/cards/1301-1400.md#gong26j-training-strategies) · Light Up Your Face: A Physically Consistent Dataset and Diffusion Model for Face Fill-Light Enhancement
- [用配对视频差分监督遮挡先验](../conferences/icml-2026/cards/1501-1600.md#he26al-training-strategies) · CLEAR: Context-Aware Learning with End-to-End Mask-Free Inference for Adaptive Video Subtitle Removal
- [先筛稳定样本再削弱纹理捷径](../conferences/icml-2026/cards/1501-1600.md#he26aw-training-strategies) · Refining Context-Entangled Content Segmentation via Curriculum Selection and Anti-Curriculum Promotion
- [直接预测标签以积累跨轮不一致性](../conferences/icml-2026/cards/1601-1700.md#hou26b-training-strategies) · Just Y-Prediction: Enabling Historical Cumulative Inconsistency in Label Diffusion for Learning with Noisy Labels
- [用分级加噪监督激活生成器早层](../conferences/icml-2026/cards/1801-1900.md#hyun26a-training-strategies) · Scalable GANs with Transformers
- [保留槽位的因素分区并在学习后回放解码器](../conferences/icml-2026/cards/2001-2100.md#kang26e-training-strategies) · Factor-Wise Homogeneity of Slot-Attention for Continual Object-Centric Learning
- [用熵导向扰动训练失真恢复](../conferences/icml-2026/cards/2201-2300.md#kumar26a-training-strategies) · Feature Collapse Under Corruption: An Entropy Perspective on Robust Neural Networks
- [按学生不可学习区域选择教师熵](../conferences/icml-2026/cards/2301-2400.md#lee26g-training-strategies) · Toward Understanding Adversarial Distillation: Why Robust Teachers Fail
- [在图像球面方向上配对并学习流](../conferences/icml-2026/cards/2301-2400.md#lee26x-training-strategies) · Geometry-Aware Image Flow Matching
- [用部件可供性图约束从文本生成的人物交互](../conferences/icml-2026/cards/2401-2500.md#li26ac-training-strategies) · HOI-PAGE: Zero-Shot Human-Object Interaction Generation with Part Affordance Guidance
- [持续红外复原的通道扩展与复用](../conferences/icml-2026/cards/2401-2500.md#li26cp-training-strategies) · Expandable, Compressible, Mineable: Open-World Thermal Image Restoration
- [按类别频率调三个去噪专家的共识门槛](../conferences/icml-2026/cards/2401-2500.md#li26cy-training-strategies) · CARE: Class-Adaptive Expert Consensus for Reliable Learning with Long-Tailed Noisy Labels
- [转换后按初始失真给 SNN 局部特征蒸馏加权](../conferences/icml-2026/cards/2401-2500.md#li26db-training-strategies) · High-Fidelity ANN-to-SNN Conversion via Closed-Loop CKA Distillation
- [按渲染块残差加密高斯基元](../conferences/icml-2026/cards/2501-2600.md#li26em-training-strategies) · PCGS: Deblurring 3D Gaussian Splatting with Patch Comparison
- [按实际输出漂移回收持续学习的秩](../conferences/icml-2026/cards/2501-2600.md#li26eq-training-strategies) · Energy-Structured Low-Rank Adaptation for Continual Learning
- [在测试时无标签更新中按样本裁剪并加噪](../conferences/icml-2026/cards/2501-2600.md#li26fy-training-strategies) · Private and Stable Test-time Adaptation with Differential Privacy
- [从原图提取字形与风格做场景文字编辑](../conferences/icml-2026/cards/2501-2600.md#li26gj-training-strategies) · Self-Prompting Diffusion Transformer for Open-Vocabulary Scene Text Editing via In-Context Learning
- [分开蒸馏开放词汇检测的语义和边界](../conferences/icml-2026/cards/2601-2700.md#li26hp-training-strategies) · Object-level Semantic and Spatial Distillation for Open Vocabulary Detection
- [用双向视频判别器约束单步因果生成](../conferences/icml-2026/cards/2601-2700.md#li26iw-training-strategies) · AAD-1: Asymmetric Adversarial Distillation for One-Step Autoregressive Video Generation
- [图像光效迁移的内容—光效拆分](../conferences/icml-2026/cards/2601-2700.md#li26ka-training-strategies) · TransLight: Image-Guided Customized Lighting Control with Generative Decoupling
- [按纬度监督全景编辑的形状](../conferences/icml-2026/cards/2601-2700.md#liang26m-training-strategies) · World-Shaper: A Unified Framework for 360\textdegree Panoramic Editing
- [长视频的语义记忆与运动监督](../conferences/icml-2026/cards/2701-2800.md#lin26ah-training-strategies) · DynaMem: Consistent Long Video Generation via Hierarchical Memory and Motion Priors
- [把正交投影丢掉的梯度送到任务分支](../conferences/icml-2026/cards/2701-2800.md#lin26aj-training-strategies) · GR-LoRA: Gradient-Recycling Low-Rank Adaptation for Class-Incremental Learning
- [以分层 Wasserstein 聚合联邦原型并解耦蒸馏](../conferences/icml-2026/cards/2801-2900.md#liu26af-training-strategies) · FedCDWA: Decoupled Federated Prototype Distillation with Hierarchical Wasserstein Aggregation
- [用图拉普拉斯双特征向量构造伪装物体伪掩码](../conferences/icml-2026/cards/2801-2900.md#liu26au-training-strategies) · Unsupervised Camouflaged Object Detection with Dual-Eigenvector Spectral Pseudo-Labeling and Contrastive Refinement
- [稀疏相机控制的三维几何蒸馏](../conferences/icml-2026/cards/2801-2900.md#liu26bj-training-strategies) · CamGeo: Sparse Camera-Conditioned Image-to-Video Generation with 3D Geometry Priors
- [以热扩散伪掩码和样本权重双层更新检测器](../conferences/icml-2026/cards/2901-3000.md#liu26fj-training-strategies) · Diffuse to Detect: Bi-Level Sample Rebalancing with Pseudo-Label Diffusion for Point-Supervised Infrared Small-Target Detection
- [在偏好样本中保留优劣图像的真实初始噪声](../conferences/icml-2026/cards/3001-3100.md#lu26ai-training-strategies) · Offline Preference Optimization for Rectified Flow with Noise-Tracked Pairs
- [随训练演化的分割低秩专家](../conferences/icml-2026/cards/3001-3100.md#luo26y-training-strategies) · ACO-MoE-LoRA: Evolving-while-Training for Adapting Segment Anything Model 2 to Specialized Domains
- [持续学习低秩知识合成](../conferences/icml-2026/cards/3001-3100.md#luo26ag-training-strategies) · SABER: Continual Learning with Representation Conflict Management
- [沿帧轴和去噪轴切换视频扩散粒度](../conferences/icml-2026/cards/3101-3200.md#ma26b-training-strategies) · Flex-Forcing: Towards a Unified Autoregressive and Bidirectional Video Diffusion Model
- [以预测不一致驱动频谱扰动抑制跨域检测捷径](../conferences/icml-2026/cards/3101-3200.md#ma26n-training-strategies) · Domain Adaptive Object Detection via Dynamic Causal Refinement
- [用对抗模仿降低流式生成器与示范轨迹分布差](../conferences/icml-2026/cards/3101-3200.md#ma26u-training-strategies) · FAIL: Flow Matching Adversarial Imitation Learning for Image Generation
- [弹性追踪 token 预算](../conferences/icml-2026/cards/3101-3200.md#ma26aq-training-strategies) · Learning Generalized Trackers with Elastic Token Budgets
- [在联邦训练中交换类流形而非单点原型](../conferences/icml-2026/cards/3301-3400.md#mu26c-training-strategies) · Federated Manifold Learning (FML): Tackling Domain Heterogeneity with Structural Knowledge Transfer
- [视觉模块可塑性](../conferences/icml-2026/cards/3401-3500.md#odonnat26a-training-strategies) · Vision Transformer Finetuning Benefits from Non-Smooth Components
- [用梯度噪声和原型共同约束持续分割](../conferences/icml-2026/cards/3501-3600.md#pandey26b-training-strategies) · Continual Segmentation under Joint Nonstationarity
- [低比特校准随模型刷新注意力样本](../conferences/icml-2026/cards/3701-3800.md#qian26j-training-strategies) · Selective Coupling of Decoupled Informative Regions: Masked Attention Alignment for Data-Free Quantization of Vision Transformers
- [把扩散授权与具体样本绑定](../conferences/icml-2026/cards/3701-3800.md#qin26k-training-strategies) · GoodDiffusion: Proactive Copyright Protection for Diffusion Bridge Models via Learnable Sample-specific Signatures
- [将潜空间水印教师蒸馏进解码器](../conferences/icml-2026/cards/3801-3900.md#rebuffi26a-training-strategies) · Learning to Watermark in the Latent Space of Generative Models
- [按潜在结构簇拆分教师诱发的标签噪声](../conferences/icml-2026/cards/3801-3900.md#ren26i-training-strategies) · MIND: Decoupling Model-Induced Label Noise via Latent Manifold Disentanglement
- [按激活几何跨宽度迁移任务向量](../conferences/icml-2026/cards/3801-3900.md#rinaldi26a-training-strategies) · Transporting Task Vectors across Different Architectures without Training
- [用稀疏记忆打分再渐进筛污染](../conferences/icml-2026/cards/3901-4000.md#safarov26a-training-strategies) · Memory-Distilled Selection for Noise-Robust Anomaly Detection
- [残差移位扩散的单步超分蒸馏](../conferences/icml-2026/cards/3901-4000.md#selikhanovych26a-training-strategies) · One-Step Residual Shifting Diffusion for Image Super-Resolution via Distillation
- [球面噪声渐变与立方体时序校正](../conferences/icml-2026/cards/4201-4300.md#song26u-training-strategies) · PVDepth: Panoramic Video Depth Estimation via Geometry-Aware Spatiotemporal Adaptation
- [跨域留出教师蒸馏](../conferences/icml-2026/cards/4201-4300.md#song26af-training-strategies) · DomED: Redesigning Ensemble Distillation for Domain Generalization
- [梯度证据挖掘未知目标](../conferences/icml-2026/cards/4201-4300.md#su26h-training-strategies) · OOVDet: Low-Density Prior Learning for Zero-Shot Out-of-Vocabulary Object Detection
- [记忆条件对齐的蒸馏](../conferences/icml-2026/cards/4301-4400.md#sun26az-training-strategies) · WorldPlay: Towards Long-Term Geometric Consistency for Real-Time Interactive World Modeling
- [感知前置RL与任务梯度分配](../conferences/icml-2026/cards/4301-4400.md#tan26b-training-strategies) · VideoVeritas: AI-Generated Video Detection via Perception Pretext Reinforcement Learning
- [reuse-gradients-to-diagnose-fast-at-collapse](../conferences/icml-2026/cards/4401-4500.md#teymourian26a-training-strategies) · SORA: Free Second-Order Attacks in Fast Adversarial Training
- [视频模型的三帧视觉修正](../conferences/icml-2026/cards/4401-4500.md#tong26a-training-strategies) · CoF-T2I: Video Models as Pure Visual Reasoners for Text-to-Image Generation
- [uncertainty-modulated-bridge](../conferences/icml-2026/cards/4501-4600.md#tu26d-training-strategies) · Unifying Heterogeneous Degradations: Uncertainty-Aware Diffusion Bridge Model for All-in-One Image Restoration

<a id="by-nlp"></a>

### 自然语言处理

- [低资源语音的多温度自对齐](../conferences/icml-2026/cards/1201-1300.md#geng26c-training-strategies) · Bridging the Stability-Expressivity Gap: Synthetic Data Scaling and Preference Alignment for Low-Resource Spoken Language Models
- [以合成数据监督锚抑制属性奖励投机](../conferences/icml-2026/cards/1601-1700.md#hu26an-training-strategies) · ACTG-ARL: Differentially Private Conditional Text Generation with RL-Boosted Control
- [用对话答复构造改写偏好](../conferences/icml-2026/cards/2101-2200.md#kim26ak-training-strategies) · Breaking the Reference Bottleneck via Learning to Rewrite Conversational Queries without Gold Reference Passages
- [用同语义跨时间的文档构造检索偏好](../conferences/icml-2026/cards/2101-2200.md#kim26bm-training-strategies) · Temporal Preference Optimization for Unsupervised Retrieval
- [跨语种回答分布的一致性对齐](../conferences/icml-2026/cards/2801-2900.md#liu26dd-training-strategies) · Post-Training Language Models for Crosslingual Consistency
- [在学习率衰减期引入稀有语种以减轻重复](../conferences/icml-2026/cards/3201-3300.md#marone26a-training-strategies) · mmBERT: A Modern Multilingual Encoder with Annealed Language Learning

<a id="by-reinforcement-learning"></a>

### 强化学习

- [按宽度与深度缩放策略网络的参数和更新](../conferences/icml-2026/cards/2301-2400.md#lee26ai-training-strategies) · CompleteP for RL: Maintaining Feature Learning When Scaling Deep Reinforcement Learning
- [先覆盖有先修关系的课程图再训练前沿](../conferences/icml-2026/cards/2701-2800.md#liu26j-training-strategies) · Active Curriculum Refinement for Reinforcement Learning
- [可执行环境变体的闭环课程](../conferences/icml-2026/cards/3301-3400.md#mitsides26a-training-strategies) · Dreaming in Code for Curriculum Learning in Open-Ended Worlds
- [只适配共享策略骨干两端的线性映射](../conferences/icml-2026/cards/3501-3600.md#park26i-training-strategies) · Adaptive Policy Backbone via Shared Network
- [用动作分布漂移动态调节在线 RL 批大小](../conferences/icml-2026/cards/3501-3600.md#park26w-training-strategies) · Scalable Reinforcement Learning via Adaptive Batch Scaling
- [用未来状态把多解动作拆成条件选择](../conferences/icml-2026/cards/3901-4000.md#schafer26a-training-strategies) · When Does Predictive Inverse Dynamics Outperform Behavior Cloning?
- [有置信门控的奖励补全](../conferences/icml-2026/cards/4101-4200.md#shihab26d-training-strategies) · What Reward Structure Enables Efficient Sparse-Reward RL? A Proof-of-Concept with Policy-Aware Matrix Completion
- [TD误差累计均值的平方根熵调度](../conferences/icml-2026/cards/4801-4900.md#wang26jc-training-strategies) · Tracking Drift: Variation-Aware Entropy Scheduling for Non-Stationary Reinforcement Learning

<a id="by-robotics"></a>

### 机器人学

- [终身轨迹规划](../conferences/icml-2026/cards/0401-0500.md#chen26d-training-strategies) · NOMAD: Lifelong Trajectory Planning via Non-Parametric Bayesian Memory-Adaptive Diffusion Experts
- [部件位姿的弱监督对称估计](../conferences/icml-2026/cards/0601-0700.md#chen26fw-training-strategies) · Generalizable and Actionable Parts Pose Estimation with Symmetry Annotation-Free Learning Strategy
- [跨构型控制的奇异分量门控](../conferences/icml-2026/cards/1101-1200.md#feng26n-training-strategies) · Knowledge Diversion for Efficient Morphology Control and Policy Transfer
- [视觉动作策略与世界模型的交替改进](../conferences/icml-2026/cards/1301-1400.md#guo26i-training-strategies) · VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model
- [用频域监督衔接连续动作块](../conferences/icml-2026/cards/1501-1600.md#he26aq-training-strategies) · FocalPolicy: Frequency-Optimized Chunking and Locally Anchored Flow Matching for Coherent Visuomotor Policy
- [让同一符号域提供规划示范与逐步反馈](../conferences/icml-2026/cards/1701-1800.md#huang26v-training-strategies) · Self-CriTeach: LLM Self-Teaching and Self-Critiquing for Improving Robotic Planning via Automated Domain Generation
- [训练控制端显式处理过期语义](../conferences/icml-2026/cards/1701-1800.md#huang26cd-training-strategies) · TIC-VLA: A Think-in-Control Vision-Language-Action Model for Robot Navigation in Dynamic Environments
- [仿真与真实数据联合训练](../conferences/icml-2026/cards/2301-2400.md#lei26d-training-strategies) · A Mechanistic Analysis of Sim-and-Real Co-Training in Generative Robot Policies
- [用视觉先验与语言后验分离动作信号](../conferences/icml-2026/cards/2601-2700.md#lian26d-training-strategies) · LangForce: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries
- [把符号级失败修复蒸馏成 VLA 的执行策略](../conferences/icml-2026/cards/2801-2900.md#liu26am-training-strategies) · NeurVLA: Unleashing Failure-Handling Capability of Vision-Language-Action Models via Neural-Symbolic Reasoning
- [先让动作符合骨干接口再学连续执行](../conferences/icml-2026/cards/2801-2900.md#liu26bx-training-strategies) · RDT2: Exploring the Scaling Limit of UMI Data Towards Zero-Shot Cross-Embodiment Generalization
- [用大规模人手视频预训练可转移的动作指令模型](../conferences/icml-2026/cards/3001-3100.md#luo26e-training-strategies) · Vision-Language-Action Pretraining from Large-Scale Human Videos
- [用后继观察降低少标注动作学习难度](../conferences/icml-2026/cards/3301-3400.md#morin26a-training-strategies) · On the Sample Efficiency of Inverse Dynamics Models for Semi-Supervised Imitation Learning
- [用未来交互表示微调少示范策略](../conferences/icml-2026/cards/3401-3500.md#nguyen26b-training-strategies) · FOCA: Future-Oriented Conditioning for Data-Efficient Vision-Language-Action Adaptation
- [为RL保留动作后验覆盖](../conferences/icml-2026/cards/4501-4600.md#wagenmaker26a-training-strategies) · Posterior Behavioral Cloning: Pretraining BC Policies for Efficient RL Finetuning
- [dual-on-policy-distillation](../conferences/icml-2026/cards/4501-4600.md#wan26n-training-strategies) · Adversarial Dual On-Policy Distillation from Expressive Teacher
- [动作梯度筛选意图状态](../conferences/icml-2026/cards/4801-4900.md#wang26hw-training-strategies) · Scaling by Diversified Experience for Vision-Language-Action Models
- [潜动作接口预热与联合训练坍塌](../conferences/icml-2026/cards/4801-4900.md#wang26kz-training-strategies) · Co-Evolving Latent Action World Models

<a id="by-multimodal"></a>

### 多模态学习

- [多模态上下文学习](../conferences/icml-2026/cards/0001-0100.md#alipour-talemi26a-training-strategies) · Hyper-ICL: Attention Calibration with Hyperbolic Anchor Distillation for Multimodal In-Context Learning
- [多模态微调](../conferences/icml-2026/cards/0101-0200.md#asadollahzadeh26a-training-strategies) · TRACER: Persistent Regularization for Robust Multimodal Finetuning
- [视觉数据与符号绑定](../conferences/icml-2026/cards/0301-0400.md#buzeta26a-training-strategies) · Seeing to Generalize: How Visual Data Corrects Binding Shortcuts
- [视觉语言蒸馏与量化](../conferences/icml-2026/cards/0501-0600.md#chen26am-training-strategies) · Gated Relational Alignment via Confidence-based Distillation for Efficient VLMs
- [多模态蒸馏的视觉与转移对齐](../conferences/icml-2026/cards/0601-0700.md#chen26gr-training-strategies) · Beyond Next-Token Alignment: Distilling Multimodal Large Language Models via Token Interactions
- [双曲空间中的 CLIP 持续适配](../conferences/icml-2026/cards/0601-0700.md#cheng26p-training-strategies) · HypCL: Adapting CLIP in Hyperbolic Space for Continual Learning
- [权重差迁移语音指令能力](../conferences/icml-2026/cards/0901-1000.md#du26t-training-strategies) · Unlocking Speech–Text Compositional Powers: Instruction-Following Speech Language Models without Instruction Tuning
- [多奖励条件的图像生成预训练](../conferences/icml-2026/cards/0901-1000.md#dufour26a-training-strategies) · MIRO: MultI-Reward cOnditioned pretraining improves T2I quality and efficiency
- [多模态编码与融合的嵌套优化](../conferences/icml-2026/cards/1101-1200.md#feng26m-training-strategies) · Multimodal Nested Learning for Decoupled and Coordinated Optimization
- [长视频内容的一次性参数蒸馏](../conferences/icml-2026/cards/1301-1400.md#guan26c-training-strategies) · From Content to Knowledge: Lightning Fast Long-Video Understanding with Neural Knowledge Representations
- [隐蔽文字识别的能力边界训练](../conferences/icml-2026/cards/1401-1500.md#guo26aj-training-strategies) · ImpText: A Benchmark and Tool-Augmented Framework for Implicit Text Reasoning
- [按实际梯度曝光量控制多模态尾部压力](../conferences/icml-2026/cards/1501-1600.md#hong26b-training-strategies) · Coverage $\not =$ Exposure: Auditable Control of Same-Support Tail Failures under Multimodal Missingness
- [训练多轮多尺度视觉检索轨迹](../conferences/icml-2026/cards/1701-1800.md#huang26bx-training-strategies) · Vision-DeepResearch: Incentivizing DeepResearch Capability in Multimodal Large Language Models
- [把分步装配指令与可见中间状态配对](../conferences/icml-2026/cards/1701-1800.md#huo26a-training-strategies) · Shape of Thought: Progressive Object Assembly via Visual Chain-of-Thought
- [用合成探针找出微调时应保护的权重](../conferences/icml-2026/cards/1701-1800.md#hwang26g-training-strategies) · Model-Dowser: Data-Free Importance Probing to Mitigate Catastrophic Forgetting in Multimodal Large Language Models
- [区分冻结模块和多模态 token 的并行开销](../conferences/icml-2026/cards/1801-1900.md#jang26g-training-strategies) · Efficient Distributed MLLM Training with Cornstarch
- [用新模型的错误重配下一轮训练样本](../conferences/icml-2026/cards/1801-1900.md#jia26c-training-strategies) · From Blind Spots to Gains: Diagnostic-Driven Iterative Training for Large Multimodal Models
- [分阶段监督文档结构和细粒度内容](../conferences/icml-2026/cards/1901-2000.md#jiang26q-training-strategies) · Dissecting Post-Training: Uncovering the Complementary Roles of SFT and RL for Document Parsing
- [用旧知识激活的零空间初始化新适配器](../conferences/icml-2026/cards/1901-2000.md#jiang26s-training-strategies) · KORE: Enhancing Knowledge Injection for Large Multimodal Models via Knowledge-Oriented Controls
- [按任务相似度降权检查基础能力遗忘](../conferences/icml-2026/cards/2001-2100.md#kang26c-training-strategies) · Don’t Forget Why You Started: Tackling Dual Forgetting in Vision-Language Continual Learning
- [先校正视觉注意再用 IoU 细化定位](../conferences/icml-2026/cards/2001-2100.md#karim26a-training-strategies) · FOCUS: Forcing In-Context Object Localization through Visual Support Constraints and Policy Optimization
- [图文生成的持续跨模态对齐](../conferences/icml-2026/cards/2101-2200.md#kong26h-training-strategies) · ECA: Efficient Continual Alignment for Open-Ended Image-to-Text Generation
- [缺失模态的上下文提示](../conferences/icml-2026/cards/2201-2300.md#lang26a-training-strategies) · AOEPT: Breaking the Implicit Modality-Reduction Bottleneck in Modality-Missing Prompt Tuning
- [蒸馏物体词组层级及跨模态关系](../conferences/icml-2026/cards/2201-2300.md#le26b-training-strategies) · HieRD: Hierarchical Relational Distillation for Vision-Language Embedding Models
- [用同类跨模态随机配对平滑监督](../conferences/icml-2026/cards/2301-2400.md#lee26bk-training-strategies) · Understanding Multimodal Learning: A Loss Landscape Smoothness Perspective
- [用共享语言概念预对齐不同遥感传感器](../conferences/icml-2026/cards/2401-2500.md#li26q-training-strategies) · Unifying Heterogeneous Multi-Modal Remote Sensing Detection Via Language-Pivoted Pretraining
- [把退化表征拉回干净特征分布](../conferences/icml-2026/cards/2601-2700.md#li26hs-training-strategies) · Robust Vision-Language Models via Manifold-Adversarial Adapters
- [用有图无图的奖励差筛查幻觉](../conferences/icml-2026/cards/2601-2700.md#li26ic-training-strategies) · IRIS: Implicit Reward-Guided Internal Sifting for Mitigating Multimodal Hallucination
- [按难度逐步学习最小图文对照](../conferences/icml-2026/cards/2601-2700.md#li26ie-training-strategies) · Mitigating Visual Hallucinations via Semantic Curriculum Preference Optimization in MLLMs
- [优先蒸馏教师可靠且师生分歧大的在线轨迹](../conferences/icml-2026/cards/2601-2700.md#li26im-training-strategies) · Video-OPD: Efficient Post-Training of Multimodal Large Language Models for Temporal Video Grounding via On-Policy Distillation
- [把语言多选题分布蒸馏为视觉类别概念签名](../conferences/icml-2026/cards/2701-2800.md#liang26ac-training-strategies) · Large Language Model Teaches Visual Students: Cross-Modality Transfer of Fine-Grained Conceptual Knowledge
- [持续学习中用共享双曲等距约束保护图文层级](../conferences/icml-2026/cards/2901-3000.md#liu26dq-training-strategies) · Hyperbolic Multimodal Continual Learning
- [客户端和服务器分别训练图像与文本编码器](../conferences/icml-2026/cards/3101-3200.md#ma26h-training-strategies) · Decoupled Training with Local Reinforcement Fine-Tuning in Federated Learning
- [按输入与输出 token 动态缓解视觉语言微调的长尾偏差](../conferences/icml-2026/cards/3201-3300.md#miao26c-training-strategies) · Adaptive Token Refinement in Long-Tailed Large Vision-Language Models Fine-Tuning
- [三维关系推理蒸馏](../conferences/icml-2026/cards/3301-3400.md#mo26c-training-strategies) · Distilling Neuro-Symbolic Programs into 3D Multi-modal LLMs
- [用预期问答效用路由并汇总持续 VQA 专家](../conferences/icml-2026/cards/3301-3400.md#mozaffari26a-training-strategies) · Calibrated Knowledge Aggregation in Bayesian Mixture-of-Experts for Continual VQA
- [文档定位推理验证](../conferences/icml-2026/cards/3401-3500.md#neogi26a-training-strategies) · DocVAL: Validated Chain-of-Thought Distillation for Grounded Document VQA
- [多图视角动作推理](../conferences/icml-2026/cards/3401-3500.md#oi26a-training-strategies) · From Correspondence to Actions: Human-Like Multi-Image Spatial Reasoning in Multi-modal Large Language Models
- [在词义和声学冲突时学习用声学作答](../conferences/icml-2026/cards/3501-3600.md#pang26b-training-strategies) · Do Audio LLMs Listen or Read? Analyzing and Mitigating Paralinguistic Failures with VoxParadox
- [解耦语音动作和肖像视角训练](../conferences/icml-2026/cards/3501-3600.md#paraperas-papantoniou26a-training-strategies) · STARCaster: Spatio-Temporal AutoRegressive Video Diffusion for Identity- and View-Aware Talking Portraits
- [对齐冻结视频模型的 token 接口接入新模态](../conferences/icml-2026/cards/3501-3600.md#park26m-training-strategies) · V-LynX: Token Interface Alignment for Video+X LLMs
- [质量指称转成分割点提示](../conferences/icml-2026/cards/3601-3700.md#peng26j-training-strategies) · IQA-Spider: Unifying Multi-Granularity Image Quality Assessment with Reasoning, Grounding and Referring
- [持续个性化的参数覆盖选址](../conferences/icml-2026/cards/3601-3700.md#peng26n-training-strategies) · SCNS: Continual Personalization of Diffusion Models via Submodular Concept Neuron Selection
- [预测客户端选择的反事实效果再调联邦参与预算](../conferences/icml-2026/cards/3801-3900.md#ren26r-training-strategies) · FedSSM: State Space Model-based Proactive Inference for Heterogeneous Multimodal Federated Learning
- [重写语义不相容的指令响应](../conferences/icml-2026/cards/3901-4000.md#sabolic26a-training-strategies) · BYORn: Bootstrap Your Own Responses to Defend Large Vision-Language Models Against Backdoor Attacks
- [用显式跨模态冲突训练操纵检测](../conferences/icml-2026/cards/4001-4100.md#shen26r-training-strategies) · CORE: Conflict-Oriented Reasoning for General Multimodal Manipulation Detection
- [以阶段化隐词元压缩多模态推理](../conferences/icml-2026/cards/4001-4100.md#shen26s-training-strategies) · Efficient Reasoning with Hidden Thinking
- [多内在表征生成辅助理解](../conferences/icml-2026/cards/4201-4300.md#su26n-training-strategies) · Generation Enhances Understanding in Unified Multimodal Models via Multi-Representation Generation
- [scale-conditioned-spatial-learning](../conferences/icml-2026/cards/4201-4300.md#sun26q-training-strategies) · SpaceVista: All-Scale Visual Spatial Reasoning from mm to km
- [统一多模态的数据与目标耦合](../conferences/icml-2026/cards/4401-4500.md#tong26c-training-strategies) · Beyond Language Modeling: An Exploration of Multimodal Pretraining
- [无配对跨模态分阶段适配](../conferences/icml-2026/cards/4401-4500.md#tran26e-training-strategies) · Cross-Modal Knowledge Distillation without Paired Data: Theoretical Foundation and Algorithm
- [answer-coupled-video-localization](../conferences/icml-2026/cards/4501-4600.md#wang26e-training-strategies) · Video-in-the-Loop: Span-Grounded Long Video QA with Interleaved Reasoning
- [Text Before Vision: Staged Knowledge Injection Matters for Agentic RLVR in Ultra-High-Resolution Remote Sensing Understanding](../conferences/icml-2026/cards/4601-4700.md#wang26u-training-strategies) · Text Before Vision: Staged Knowledge Injection Matters for Agentic RLVR in Ultra-High-Resolution Remote Sensing Understanding
- [参考视觉视野对齐作为课程和奖励](../conferences/icml-2026/cards/4701-4800.md#wang26gt-training-strategies) · Seeing is Solving: Unlocking Efficient Multimodal RL via View Alignment
- [共享前缀的局部视频候选排名](../conferences/icml-2026/cards/4801-4900.md#wang26iu-training-strategies) · WorldCompass: Reinforcement Learning for Long-Horizon World Models
- [联合提示训练保留原提示对照](../conferences/icml-2026/cards/4801-4900.md#wang26kl-training-strategies) · PromptRL: Prompt Matters in RL for Flow-Based Image Generation
- [临时专家竞争决定扩容层](../conferences/icml-2026/cards/4801-4900.md#wang26le-training-strategies) · CoPE: Continual Probe-guided Expansion for Large Vision-Language Models

<a id="by-ml-foundations"></a>

### 机器学习基础与统计

- [权重合并](../conferences/icml-2026/cards/0001-0100.md#abdollahpoorrostam26a-training-strategies) · MODEL SOUPS NEED ONLY ONE INGREDIENT
- [机器遗忘](../conferences/icml-2026/cards/0001-0100.md#almudevar26b-training-strategies) · Representation Unlearning: Forgetting through Information Compression
- [联邦模型水印](../conferences/icml-2026/cards/0101-0200.md#bakr26a-training-strategies) · Collaborative Threshold Watermarking
- [持续模型路由](../conferences/icml-2026/cards/0201-0300.md#bell26a-training-strategies) · Continual Model Routing in Evolving Model Hubs
- [联邦 LoRA](../conferences/icml-2026/cards/0201-0300.md#bian26e-training-strategies) · FedTreeLoRA: Reconciling Statistical and Functional Heterogeneity in Federated LoRA Fine-Tuning
- [状态空间模型训练](../conferences/icml-2026/cards/0301-0400.md#brady26a-training-strategies) · Efficient Learning of Deep State Space Models via Importance Smoothing
- [递归去噪训练](../conferences/icml-2026/cards/0301-0400.md#cameron26a-training-strategies) · One Step Forward and K Steps Back: Better Reasoning with Denoising Recursion Models
- [异构联邦学习](../conferences/icml-2026/cards/0301-0400.md#cao26a-training-strategies) · Required Spine Optional Limbs: Heterogeneous Federated Learning via Backbone-sharing and Activation-guided Selection
- [离散扩散采样](../conferences/icml-2026/cards/0401-0500.md#carter26a-training-strategies) · Discrete Diffusion Samplers and Bridges: Off-Policy Algorithms and Applications in Latent Spaces
- [首脉冲时间编码](../conferences/icml-2026/cards/0401-0500.md#che26a-training-strategies) · Efficiently Training Time-to-First-Spike Spiking Neural Networks from Scratch
- [生成流的先验](../conferences/icml-2026/cards/0401-0500.md#chemseddine26a-training-strategies) · Adapting Noise to Data: Generative Flows from Learned 1D Processes
- [测试时因果结构学习](../conferences/icml-2026/cards/0401-0500.md#chen26t-training-strategies) · Test-Time Learning of Causal Structure from Interventional Data
- [存内计算权重抗扰训练](../conferences/icml-2026/cards/0501-0600.md#chen26bq-training-strategies) · Diversity-aware Weight Perturbation Promotes Robust Adaptation
- [多层联邦个性化建模](../conferences/icml-2026/cards/0501-0600.md#chen26cp-training-strategies) · Personalized Additive Modeling for Multi-level Federated Learning
- [离线 GFlowNet 的边奖励引导](../conferences/icml-2026/cards/0601-0700.md#chen26ej-training-strategies) · Beyond the Proxy: Trajectory-Distilled Guidance for Offline GFlowNet Training
- [多方向异步流水线训练](../conferences/icml-2026/cards/0601-0700.md#chen26ff-training-strategies) · AMDP: Asynchronous Multi-Directional Pipeline Parallelism for Large-Scale Models Training
- [面向后续适配的模型合并](../conferences/icml-2026/cards/0601-0700.md#chen26gq-training-strategies) · Learn to Merge: Meta-Learning for Adaptive Multi-Task Model Merging
- [逐步域适应的半对偶传输](../conferences/icml-2026/cards/0601-0700.md#chen26hd-training-strategies) · Rethinking the Flow-based Gradual Domain Adaptation: A Semi-Dual Optimal Transport Perspective
- [多目标扩散模型的半监督蒸馏](../conferences/icml-2026/cards/0601-0700.md#cheng26g-training-strategies) · Multi-Objective Learning for Diffusion Models: A Statistical Theory under Semi-Supervised Learning
- [二值贝叶斯网络的主动持续学习](../conferences/icml-2026/cards/0701-0800.md#cottart26a-training-strategies) · Active Continual Learning with Metaplastic Binary Bayesian Neural Networks
- [选择式解释的双路蒸馏](../conferences/icml-2026/cards/0801-0900.md#dai26e-training-strategies) · Learn from A Rationalist: Distilling Intermediate Interpretable Rationales
- [GFlowNet 互补探索](../conferences/icml-2026/cards/0801-0900.md#dall-antonia26a-training-strategies) · Avoid What You Know: Divergent Trajectory Balance for GFlowNets
- [矩阵与卷积的低秩微调](../conferences/icml-2026/cards/0901-1000.md#ding26o-training-strategies) · LAVA: A Unified Framework for Finetuning Language and Vision Models
- [表格离群检测的合成课程](../conferences/icml-2026/cards/0901-1000.md#ding26s-training-strategies) · From Zero to Hero: Advancing Zero-Shot Foundation Models for Tabular Outlier Detection
- [扩散模型记忆的中等噪声区间](../conferences/icml-2026/cards/0901-1000.md#dodson26a-training-strategies) · Two Calm Ends and the Wild Middle: A Geometric Picture of Memorization in Diffusion Models
- [噪声联邦微调的双分支 LoRA](../conferences/icml-2026/cards/1001-1100.md#fang26v-training-strategies) · Decoupled Low-Rank Adaptation for Robust Federated Fine-Tuning
- [临界信号传播的分层 dropout](../conferences/icml-2026/cards/1101-1200.md#fernandez-sarmiento26a-training-strategies) · Dropout Universality: Scaling Laws and Optimal Scheduling at the Edge-of-Chaos
- [时间序列的多目标掩码预训练](../conferences/icml-2026/cards/1101-1200.md#fu26n-training-strategies) · Zeus: Towards Tuning-Free Foundation Model for Time Series Analysis
- [无标签自监督模型的参数合并](../conferences/icml-2026/cards/1101-1200.md#fuller26a-training-strategies) · Self-Soupervision: Cooking Model Soups without Labels
- [预训练权重邻域的随机专家集成](../conferences/icml-2026/cards/1101-1200.md#gan26a-training-strategies) · Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights
- [不规则时序图流的辅助轨迹监督](../conferences/icml-2026/cards/1201-1300.md#gao26ac-training-strategies) · One-Step Graph-Structured Neural Flows for Irregular Multivariate Time Series Classification
- [联合能量模型的边缘采样](../conferences/icml-2026/cards/1201-1300.md#geng26b-training-strategies) · Latent-Guided Cooperative Energy-Based Models
- [表格 MLP 超参数并行集成](../conferences/icml-2026/cards/1301-1400.md#gorishniy26a-training-strategies) · TabPack: Efficient Hyperparameter Ensembles for Tabular Deep Learning
- [在指数族中迁移微调因子](../conferences/icml-2026/cards/1301-1400.md#guo26y-training-strategies) · Fine-Tune Once, Reuse Across Models: Bayesian Task-Update Factors and Approximations
- [蒸馏专家搜索的候选分布](../conferences/icml-2026/cards/1401-1500.md#han26x-training-strategies) · $\textttMetaDistill$: Unlocking the Performance Ceiling for Pretrained Optimizers
- [按投影能量拆分持续学习的共享与专用更新](../conferences/icml-2026/cards/1401-1500.md#he26f-training-strategies) · Task-Driven Subspace Decomposition for Knowledge Sharing and Isolation in LoRA-based Continual Learning
- [联邦低秩更新的选择聚合与尾部投影](../conferences/icml-2026/cards/1501-1600.md#he26p-training-strategies) · FedPissa: Towards Federated Personalized Adaptation of Foundation Models via LoRA Subspace Mapping
- [面向合并结果选择专家停止点](../conferences/icml-2026/cards/1501-1600.md#horoi26a-training-strategies) · From Memorization to Parameter Interference: How Overtraining Experts Harms Model Merging
- [用回放统计锚定跨域不变表示](../conferences/icml-2026/cards/1801-1900.md#janetzky26a-training-strategies) · Continual Learning of Domain-Invariant Representations
- [给每个私有专家选相关且多样的公开代理](../conferences/icml-2026/cards/1901-2000.md#jiang26c-training-strategies) · MetaMoE: Diversity-Aware Proxy Selection for Privacy-Preserving Mixture-of-Experts Unification
- [合并时只适配任务接口和权重系数](../conferences/icml-2026/cards/2001-2100.md#jung26f-training-strategies) · SyMerge: From Non-Interference to Synergistic Merging via Single-Layer Adaptation
- [沿约束流形法向扩展训练分布](../conferences/icml-2026/cards/2001-2100.md#keegan26a-training-strategies) · Manifold-Aware Perturbations for Constrained Generative Modeling
- [以随机补全做条件，仅用真实观测训练去噪](../conferences/icml-2026/cards/2101-2200.md#kim26bh-training-strategies) · AugMask: Training Diffusion Models on Incomplete Tabular Data via Stochastic Augmentation and Masking
- [轮流更新小权重切片保留累计方向](../conferences/icml-2026/cards/2201-2300.md#kowsher26b-training-strategies) · SliceFine: The Universal Winning-Slice Hypothesis for Pretrained Networks
- [基于上下文差异的零样本时序检测](../conferences/icml-2026/cards/2201-2300.md#lan26b-training-strategies) · Towards Foundation Models for Zero-Shot Time Series Anomaly Detection: Leveraging Synthetic Data and Relative Context Discrepancy
- [异构联邦模型的模块聚合](../conferences/icml-2026/cards/2301-2400.md#leng26b-training-strategies) · LEGO-FL: Learning Heterogeneous Federated Models as a LEGO Assembly Games
- [用排队预测决定每轮联邦训练做多少本地工作](../conferences/icml-2026/cards/2401-2500.md#li26ae-training-strategies) · FedQueue: Queue-Aware Federated Learning for Cross-Facility HPC Training
- [合并模型时校准共享方向的幅值](../conferences/icml-2026/cards/2501-2600.md#li26ep-training-strategies) · When Shared Knowledge Hurts: Spectral Over-Accumulation in Model Merging
- [用教师估计源重混合训练生成式分离器](../conferences/icml-2026/cards/2501-2600.md#li26fa-training-strategies) · SURF: Separation via Unsupervised Remixing Flow
- [沿固定点轨迹蒸馏少步平衡求解器](../conferences/icml-2026/cards/2701-2800.md#lin26w-training-strategies) · Consistency Deep Equilibrium Models
- [用共享语义锚点校准异质客户端的残差](../conferences/icml-2026/cards/3001-3100.md#lu26aa-training-strategies) · FedARC: Anchor-Guided Residual Compensation for Data and Model Heterogeneous Federated Learning
- [联邦子模型按平台期逐步恢复容量](../conferences/icml-2026/cards/3101-3200.md#ma26ab-training-strategies) · Breaking the Capacity Bottleneck in Model-Heterogeneous Federated Learning via Gradual Model Restoration
- [一次联邦训练支持多预算量化](../conferences/icml-2026/cards/3101-3200.md#ma26ae-training-strategies) · No Retraining at Edge: Efficient Resource-Aware Mixed-Precision Quantization via Federated Supernet Learning
- [跨数据孤岛组合生成因素](../conferences/icml-2026/cards/3301-3400.md#morshed26a-training-strategies) · Compositional Generative Modeling from Decentralized Data
- [按谱熵与跨通道依赖适配时间序列模型](../conferences/icml-2026/cards/3301-3400.md#na26b-training-strategies) · Time-PEFT: Temporal and Multichannel Complexity-Based Fine-Tuning for Time-Series Foundation Models
- [在重尾坐标上做对数退火](../conferences/icml-2026/cards/3501-3600.md#pachebat26a-training-strategies) · Tail Annealing for Heavy-Tailed Flow Matching
- [结合跨层连通性与专家一致性合并任务向量](../conferences/icml-2026/cards/3501-3600.md#park26l-training-strategies) · Saliency-Aware Model Merging
- [让异构客户端共享类判别规则](../conferences/icml-2026/cards/3701-3800.md#qin26g-training-strategies) · Towards Rule-Based Knowledge Sharing in Federated Learning
- [训练前固定低秩符号模板以突破亚比特存储下限](../conferences/icml-2026/cards/3901-4000.md#sakai26a-training-strategies) · Sign Lock-In: Randomly Initialized Weight Signs Persist and Bottleneck Sub-Bit Model Compression
- [在训练中学适于事后公平阈值控制的表征](../conferences/icml-2026/cards/3901-4000.md#sakata26a-training-strategies) · Fair Classification with Efficient and Post-hoc Controllable Fairness-Accuracy Trade-off
- [用权重低频 DCT 分量一次初始化不同尺寸网络](../conferences/icml-2026/cards/4001-4100.md#shen26f-training-strategies) · Breaking the Scale Barrier: One-Shot Knowledge Transfer via Frequency Transform
- [让部署模型反向校准伪标签教师](../conferences/icml-2026/cards/4101-4200.md#shi26d-training-strategies) · Coupled Training with Privileged Information and Unlabeled Data
- [先学数据到能量的生成耦合](../conferences/icml-2026/cards/4101-4200.md#shin26d-training-strategies) · Efficient Generative Modeling beyond Memoryless Diffusion via Adjoint Schrödinger Bridge Matching
- [有限维泊松场蒸馏](../conferences/icml-2026/cards/4101-4200.md#shlenskii26a-training-strategies) · Overclocking Electrostatic Generative Models
- [按均值偏移与有效秩诊断SAE特征死亡](../conferences/icml-2026/cards/4101-4200.md#simon26a-training-strategies) · On the Relationship Between Activation Outliers and Feature Death in Sparse Autoencoders
- [路径蒸馏任务算术](../conferences/icml-2026/cards/4101-4200.md#sommariva26a-training-strategies) · Distilling Linearized Behavior into Non-linear Fine-Tuning for Effective Task Arithmetic
- [子图消息复用](../conferences/icml-2026/cards/4201-4300.md#song26m-training-strategies) · MIMO-LP: A Multi-Input Multi-Output Framework for Subgraph-based Link Prediction
- [静默梯度错误与副本重同步](../conferences/icml-2026/cards/4301-4400.md#tang26g-training-strategies) · Identifying and Mitigating Errors in Gradient Aggregation of Distributed Data Parallel Training
- [联邦全局教师修正噪声标签](../conferences/icml-2026/cards/4401-4500.md#tian26l-training-strategies) · Learning Locally, Revising Globally: Global Reviser for Federated Learning with Noisy Labels
- [按DRO强度分散集成](../conferences/icml-2026/cards/4601-4700.md#wang26bc-training-strategies) · Learning Credal Ensembles via Distributionally Robust Optimization

<a id="by-graph-and-recommendation"></a>

### 图学习与推荐

- [超图鲁棒训练](../conferences/icml-2026/cards/0101-0200.md#arafat26a-training-strategies) · Adversarial Attacks and Robust Training for Hypergraph Neural Networks
- [图组合优化迁移](../conferences/icml-2026/cards/0301-0400.md#canturk26a-training-strategies) · Can Computational Reducibility Lead to Transferable Models for Graph Combinatorial Optimization?
- [图基础模型的消息微调](../conferences/icml-2026/cards/0501-0600.md#chen26cz-training-strategies) · Message Tuning Outshines Graph Prompt Tuning: A Prismatic Space Perspective
- [图分区投毒认证的半监督增强](../conferences/icml-2026/cards/1301-1400.md#gosch26a-training-strategies) · Certifying Graph Neural Networks Against Label and Structure Poisoning
- [图自监督任务的反馈式预算调度](../conferences/icml-2026/cards/1301-1400.md#grover26a-training-strategies) · Feedback Control for Multi-Objective Graph Self-Supervision
- [从全局模型和本地图邻居两侧找噪声标签](../conferences/icml-2026/cards/2501-2600.md#li26fv-training-strategies) · FedRGL: Robust Federated Graph Learning under Label Noise
- [以对比聚类进行路段到车道迁移](../conferences/icml-2026/cards/2601-2700.md#li26ih-training-strategies) · Being More Lightweight and Practical: Mini-sized Contrastive Learning Pre-trained Models for Fine-grained Traffic Task
- [各客户端保留曲率并共享类空更新](../conferences/icml-2026/cards/2701-2800.md#liu26b-training-strategies) · FlatLand: Personalized Graph Federated Learning via Tailored Lorentz Space
- [图节点特征置换剪枝](../conferences/icml-2026/cards/3401-3500.md#navarro26a-training-strategies) · Adaptive Node Feature Selection for Graph Neural Networks
- [组合问题分布元学习](../conferences/icml-2026/cards/3501-3600.md#pan26h-training-strategies) · Problem Distributions as Tasks: Repurposing Meta Learning for Generative Combinatorial Optimization towards Multi-task Pretraining and Adaptation
- [用低秩局部遗忘和排序校准删除推荐交互](../conferences/icml-2026/cards/3601-3700.md#prakash26c-training-strategies) · Obliviate: Efficient Unlearning in Recommender Systems
- [随机增删边后对齐推理消息期望](../conferences/icml-2026/cards/3901-4000.md#saber26a-training-strategies) · RADE: Random Add-Drop Edge as a Regularizer

<a id="by-scientific-ml"></a>

### 科学机器学习

- [变构蛋白结合物生成](../conferences/icml-2026/cards/0301-0400.md#cao26r-training-strategies) · TD3B: Transition-Directed Discrete Diffusion for Allosteric Binder Generation
- [层级仿真推断](../conferences/icml-2026/cards/0401-0500.md#charles26a-training-strategies) · Tokenised Flow Matching for Hierarchical Simulation Based Inference
- [长时天气预测](../conferences/icml-2026/cards/0501-0600.md#chen26ao-training-strategies) · EMFormer: Efficient Multi-Scale Transformer for Accumulative Context Weather Forecasting
- [基因组模型的进化速率监督](../conferences/icml-2026/cards/0701-0800.md#consens26a-training-strategies) · Predicting evolutionary rate as a pretraining task improves genome language model representations
- [竞争风险的离散危险率蒸馏](../conferences/icml-2026/cards/0801-0900.md#deng26o-training-strategies) · Discrete Survival Knowledge Distillation for Competing Risks Analysis
- [删失数据的分量似然蒸馏](../conferences/icml-2026/cards/0801-0900.md#deng26p-training-strategies) · Component-Wise Composite Likelihood Distillation for Censored Time-to-Event Data
- [确定性 PDE 模拟器的概率改造](../conferences/icml-2026/cards/0801-0900.md#diaconu26a-training-strategies) · Probabilistic Retrofitting of Learned Simulators
- [医学分割任务的在线分簇适配](../conferences/icml-2026/cards/1201-1300.md#gao26s-training-strategies) · MedCRP-CL: Continual Medical Image Segmentation via Bayesian Nonparametric Semantic Modality Discovery
- [按原子数缩放分子扩散先验](../conferences/icml-2026/cards/1201-1300.md#gao26v-training-strategies) · Scaling the Prior: Size-Consistent Geometric Diffusion for 3D Molecular Generation
- [网格模拟的模板监督与时序校正](../conferences/icml-2026/cards/1201-1300.md#garnier26a-training-strategies) · Mesh Based Simulations with Spatial and Temporal awareness
- [遥感多视图聚类的原型对齐](../conferences/icml-2026/cards/1301-1400.md#guan26j-training-strategies) · Federated Multi-view Clustering for Remote Sensing Data
- [蛋白突变的多源相对偏好蒸馏](../conferences/icml-2026/cards/1301-1400.md#guo26c-training-strategies) · MutAtlas: A PDB-Wide Energy-Guided Atlas of Protein Mutation Effects
- [用性能偏好训练单元版图脚本生成](../conferences/icml-2026/cards/1401-1500.md#han26j-training-strategies) · Expert-level Leaf Cell Layout Generation via Preference-Optimized LLM
- [按分子去噪表现选择化学振动扰动](../conferences/icml-2026/cards/1601-1700.md#hou26f-training-strategies) · MOES-Pred: Molecular Structural Representation Learning by Adaptive Energy-Sentinel Vibration for Generalized Property Prediction
- [让神经信号预训练覆盖下游任务的时间尺度](../conferences/icml-2026/cards/1801-1900.md#jayalath26b-training-strategies) · MEG-XL: Data-Efficient Brain-to-Text via Long-Context Pre-Training
- [训练模型在医学图像上选区域并核查工具所得证据](../conferences/icml-2026/cards/1901-2000.md#jiang26bd-training-strategies) · Ophiuchus: Incentivizing Tool-augmented ”Think with Images” for Joint Medical Segmentation, Understanding and Reasoning
- [把诊断规程拆成可奖励的导联证据](../conferences/icml-2026/cards/1901-2000.md#jin26l-training-strategies) · ECG-R1: Protocol-Guided and Modality-Agnostic MLLM for Reliable ECG Interpretation
- [蒸馏逐切片特征以跨架构联合训练](../conferences/icml-2026/cards/1901-2000.md#jing26b-training-strategies) · Federated Distillation for Whole Slide Image via Gaussian-Mixture Feature Alignment and Curriculum Integration
- [用解之间的物理差值为粗网格数据补监督](../conferences/icml-2026/cards/2101-2200.md#kim26q-training-strategies) · Semi-Supervised Neural Super-Resolution for Mesh-Based Simulations
- [只在训练时用原子轨迹教静态预测器](../conferences/icml-2026/cards/2101-2200.md#kim26au-training-strategies) · Teaching Molecular Dynamics to a Non-Autoregressive Ionic Transport Predictor
- [按置信与分歧共同筛选分割伪标](../conferences/icml-2026/cards/2501-2600.md#li26et-training-strategies) · Are We Overconfident in Models and Results for Semi-Supervised 3D Medical Image Segmentation?
- [用回归、上下文去噪与局部性诱导不同轨道世界模型](../conferences/icml-2026/cards/2801-2900.md#liu26aj-training-strategies) · From Kepler to Newton: Inductive Biases Guide Learned World Models in Transformers
- [为多任务健康模型组合共享和条件适配](../conferences/icml-2026/cards/2801-2900.md#liu26br-training-strategies) · DIYHealth Suite: Dataset, Model, and Benchmark for Health Management at Home
- [无线信号扩散中的可学习物理信道](../conferences/icml-2026/cards/2901-3000.md#liu26em-training-strategies) · From Denoising to De-Channeling: Integrating Physical Channel Priors into Diffusion Models for Radio Signal Understanding
- [用亚群原型路由联邦专家](../conferences/icml-2026/cards/3201-3300.md#meng26c-training-strategies) · Fair-FedMOE: Group-Fair One-Shot Federated Learning via Prototype-Guided Experts for Medical Imaging Analysis
- [按通道构建时序后门防御的可信池](../conferences/icml-2026/cards/3401-3500.md#nguyen26g-training-strategies) · TimeGuard: Channel-wise Pool Training for Backdoor Defense in Time Series Forecasting
- [让分子结构与序列的生成时钟学习最优耦合](../conferences/icml-2026/cards/3701-3800.md#qiu26r-training-strategies) · Demystifying Multimodal Biomolecular Co-design With Intrinsic Geodesic Coupling
- [只用瞬时力学习大步长动力学](../conferences/icml-2026/cards/3801-3900.md#ripken26a-training-strategies) · Learning Hamiltonian Flow Maps: Mean Flow Consistency for Large-Timestep Molecular Dynamics
- [两阶段训练的概率天气预报](../conferences/icml-2026/cards/3901-4000.md#ruhling-cachay26a-training-strategies) · U-Cast: A Surprisingly Simple and Efficient Frontier Probabilistic AI Weather Forecaster
- [用阴性对照稳定生物图像批归一化适配](../conferences/icml-2026/cards/3901-4000.md#sanchez-fernandez26a-training-strategies) · Stabilizing In-Context Multi-Source Domain Adaptation for Biomedical Images Through Controls
- [采样与梯度分开定精度](../conferences/icml-2026/cards/4101-4200.md#solinas26a-training-strategies) · Neural Quantum States in Mixed Precision
<!-- classification:end -->
