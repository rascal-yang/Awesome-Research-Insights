# 训练策略

[首页](../README.md) · [参与贡献](../CONTRIBUTING.md) · [English](../en/insights/training-strategies.md)

训练日程、课程学习与多阶段训练。

<!-- classification:start -->
## 按研究领域浏览

[大语言模型](#by-llm) · [计算机视觉](#by-computer-vision) · [自然语言处理](#by-nlp) · [强化学习](#by-reinforcement-learning) · [机器人学](#by-robotics) · [多模态学习](#by-multimodal) · [机器学习基础与统计](#by-ml-foundations) · [图学习与推荐](#by-graph-and-recommendation) · [科学机器学习](#by-scientific-ml)

<a id="by-llm"></a>

### 大语言模型

- [激活干预](../conferences/icml-2026/cards/0001-0100.md#adila26a-training-strategies) · Weight Updates as Activation Shifts: A Principled Framework for Steering
- [离散扩散加速](../conferences/icml-2026/cards/0001-0100.md#amin26a-training-strategies) · Consistent Diffusion Language Models
- [激活控制](../conferences/icml-2026/cards/0201-0300.md#bao26b-training-strategies) · Towards Steering without Sacrifice: Principled Training of Steering Vectors for Prompt-only Interventions
- [Transformer 到 SSM 蒸馏](../conferences/icml-2026/cards/0201-0300.md#bick26a-training-strategies) · Retrieval-Aware Distillation for Transformer-SSM Hybrids
- [推理后训练课程](../conferences/icml-2026/cards/0301-0400.md#bu26a-training-strategies) · Provable Sample Efficiency of Curriculum Post-Training for Transformer Reasoning
- [渐进式模型训练](../conferences/icml-2026/cards/0301-0400.md#bu26c-training-strategies) · Scaling depth capacity via zero/one-layer model expansion
- [微调泛化干预](../conferences/icml-2026/cards/0401-0500.md#casademunt26a-training-strategies) · Steering Out-of-Distribution Generalization with Concept Ablation Fine-Tuning
- [监督微调与强化学习协同](../conferences/icml-2026/cards/0501-0600.md#chen26an-training-strategies) · Beyond Two-Stage Training: Cooperative SFT and RL for LLM Reasoning
- [后训练的近似在策略数据](../conferences/icml-2026/cards/0501-0600.md#chen26do-training-strategies) · Retaining by Doing: The Role of On-Policy Data in Mitigating Forgetting
- [拒答引导的激活对抗训练](../conferences/icml-2026/cards/0601-0700.md#chen26em-training-strategies) · Steering Beyond the Support: Adversarial Training on Unsupervised Jailbroken Activation Simulation
- [按梯度冲突拆分指令微调](../conferences/icml-2026/cards/0701-0800.md#choi26g-training-strategies) · Decentralized Instruction Tuning: Conflict-Aware Splitting and Weight Merging
- [跨架构模型的激活对齐合并](../conferences/icml-2026/cards/0801-0900.md#cui26j-training-strategies) · Transport and Merge: Cross-Architecture Merging for Large Language Models
- [多题上下文诱导的短推理蒸馏](../conferences/icml-2026/cards/0801-0900.md#deng26m-training-strategies) · ConPress: Learning Efficient Reasoning from Multi-Question Contextual Pressure
- [FP8 注意力的谱范数缩放](../conferences/icml-2026/cards/1001-1100.md#emadi26a-training-strategies) · Rank-Aware Spectral Bounds on Attention Logits for Stable Low-Precision Training
- [长思维链蒸馏的梯度谱筛选](../conferences/icml-2026/cards/1001-1100.md#fan26e-training-strategies) · Uncovering the Gradient Geometry of Long CoT: A Spectral-guided Approach to Reasoning Distillation
- [异构联邦微调的 LoRA 子矩阵](../conferences/icml-2026/cards/1001-1100.md#fang26e-training-strategies) · Federated Sketching LoRA: A Flexible Framework for Heterogeneous Collaborative Fine-Tuning of LLMs
- [偏好对齐中的负例遗忘权重](../conferences/icml-2026/cards/1101-1200.md#feng26f-training-strategies) · Leveraging Machine Unlearning for Cost-Efficient Preference Alignment
- [上下文并行的按头显存复用](../conferences/icml-2026/cards/1201-1300.md#ghadia26a-training-strategies) · Untied Ulysses: Memory-Efficient Context Parallelism via Headwise Chunking
- [安全微调的缓冲与正交合并](../conferences/icml-2026/cards/1401-1500.md#ham26a-training-strategies) · Jailbreak to Protect: Buffering and Reinforcing via Temporary Jailbreaking for Safe Fine-Tuning in Large Language Models
- [预训练权重衰减与下游可塑性](../conferences/icml-2026/cards/1401-1500.md#han26b-training-strategies) · Weight Decay Improves Language Model Plasticity
- [用可微共形流程学习断言评分，再切回硬校准](../conferences/icml-2026/cards/1501-1600.md#hittesdorf26a-training-strategies) · Differentiable Conformal Training for LLM Reasoning Factuality
- [从自身 Jacobi 轨迹蒸馏保持因果的多词元预测](../conferences/icml-2026/cards/1601-1700.md#hu26aa-training-strategies) · Fast and Accurate Causal Parallel Decoding using Jacobi Forcing
- [用可辨识的掩码区间安排扩散语言模型训练预算](../conferences/icml-2026/cards/1701-1800.md#huang26an-training-strategies) · Tuning the Implicit Regularizer of Masked Diffusion Language Models: Enhancing Generalization via Insights from $k$-Parity
- [用词元扰动验证当前代码步骤真正依赖的计划线索](../conferences/icml-2026/cards/1701-1800.md#huang26ar-training-strategies) · PADA-Coder: Improving Plan-Following Code Generation via Perturbation-Verified Attention Distillation and Dynamic Alignment
- [用可恢复损失给任务向量加权](../conferences/icml-2026/cards/1801-1900.md#im26b-training-strategies) · Post-Hoc Merging is Not Enough: Many-Shot Model Merging with Loss-Gap Balancing
- [按 MoE 参数组缩放超参数再迁移](../conferences/icml-2026/cards/1901-2000.md#jiang26a-training-strategies) · Hyperparameter Transfer with Mixture-of-Experts Layers
- [让扩散预训练掩码随模型成熟度改变](../conferences/icml-2026/cards/1901-2000.md#jing26g-training-strategies) · InfoDLM: an Information-Adaptive Framework for Discrete Diffusion Language Model Pretraining
- [摊销预测分布的早期漂移](../conferences/icml-2026/cards/2101-2200.md#kim26ah-training-strategies) · From Drift to Coherence: Stabilizing Beliefs in LLMs
- [让教师从学生自己走到的状态接管](../conferences/icml-2026/cards/2201-2300.md#lauffer26a-training-strategies) · Imitation Learning for Multi-turn LM Agents via On-policy Expert Corrections
- [用可补算的数据分片抵消同步训练故障](../conferences/icml-2026/cards/2301-2400.md#lee26c-training-strategies) · SPARe: Stacked Parallelism with Adaptive Reordering for Fault-Tolerant LLM Pretraining Systems with 100k+ GPUs
- [在末块量化时直接校准词表分布](../conferences/icml-2026/cards/2301-2400.md#lee26bi-training-strategies) · LFQ: Logit-aware Final-block Quantization for Boosting the Generation Quality of Low-Bit Quantized LLMs
- [微调末几层改变贪婪解码的上下文排序](../conferences/icml-2026/cards/2401-2500.md#li26af-training-strategies) · Beyond Temperature: Hyperfitting as a Late-Stage Geometric Expansion
- [离散扩散语言模型的逆向蒸馏](../conferences/icml-2026/cards/2401-2500.md#li26az-training-strategies) · IDLM: Inverse-distilled Diffusion Language Models
- [自博弈题目的解法多样性](../conferences/icml-2026/cards/2401-2500.md#li26bh-training-strategies) · R-Diverse: Mitigating Diversity Illusion in Self-Play LLM Training
- [扰动 RoPE 位置索引并要求两次预测一致](../conferences/icml-2026/cards/2401-2500.md#li26cs-training-strategies) · Shuffle the Context: RoPE-Perturbed Self-Distillation for Long-Context Adaptation
- [为草稿训练拆开目标模型执行](../conferences/icml-2026/cards/2601-2700.md#li26hf-training-strategies) · SpecForge: A Flexible and Efficient Open-Source Training Framework for Speculative Decoding
- [先保持对话连续抽取激活再混合训练](../conferences/icml-2026/cards/2601-2700.md#li26ik-training-strategies) · Breaking the Block: Preserving Data Continuity to Train Superior SAEs for Instruct Models
- [先从符号任务学程序再用自然语言适配](../conferences/icml-2026/cards/2701-2800.md#lin26k-training-strategies) · Can Large Language Models Generalize Procedures Across Representations?
- [在零空间内重定向需要遗忘的事实](../conferences/icml-2026/cards/2701-2800.md#lin26ap-training-strategies) · ZeroUnlearn: Few-Shot Knowledge Unlearning in Large Language Models
- [以差分隐私处理提示再用潜变量条件生成代码](../conferences/icml-2026/cards/2801-2900.md#liu26ao-training-strategies) · PrivCode++: Latent-Conditioned Differentially Private Code Generation for Comprehensive Guarantees
- [在冷启动时限制专家令牌的概率跃升](../conferences/icml-2026/cards/2801-2900.md#liu26bm-training-strategies) · Clipping Low-Probability Tokens in SFT Yields a Generalizable Initialization for RL
- [按共同字符区间稀疏对齐跨词表蒸馏](../conferences/icml-2026/cards/2801-2900.md#liu26bw-training-strategies) · Entropy-aware Span-Constrained Optimal Transport for Robust Cross-Tokenizer Knowledge Distillation
- [融合预测与上下文的潜变量推理](../conferences/icml-2026/cards/2801-2900.md#liu26cv-training-strategies) · Latent Thoughts Tuning: Bridging Context and Reasoning with Fused Information in Latent Tokens
- [混合中训衔接通用预训练与专域后训练](../conferences/icml-2026/cards/2801-2900.md#liu26cz-training-strategies) · Midtraining Bridges Pretraining and Posttraining Distributions
- [用执行结果训练生成可组合的规划架构](../conferences/icml-2026/cards/2901-3000.md#liu26fz-training-strategies) · TodoEvolve: Learning to Architect Agent Planning Systems
- [推理轨迹几何水印](../conferences/icml-2026/cards/3001-3100.md#lu26q-training-strategies) · Echoes within the Reasoning: Stealthy and Effective Watermarking via Chain of Thought
- [从任务演示初始化可优化的上下文缓存](../conferences/icml-2026/cards/3001-3100.md#lu26ag-training-strategies) · Context Tuning for In-Context Optimization
- [按学生首个错误蒸馏工具推理](../conferences/icml-2026/cards/3101-3200.md#lyu26j-training-strategies) · Student-Centered Distillation Narrows the Agentic Gap Between Small and Large LLMs
- [通过撤销标记学习可回退的自回归生成](../conferences/icml-2026/cards/3101-3200.md#ma26ad-training-strategies) · Non-Monotonic Autoregressive Sequence Model
- [按任务相似度共享适配器子空间](../conferences/icml-2026/cards/3101-3200.md#magakyan26a-training-strategies) · Collaborative and Efficient Fine-tuning: Leveraging Task Similarity
- [专家推理自蒸馏](../conferences/icml-2026/cards/3201-3300.md#mendes26b-training-strategies) · Making Expert Reasoning Learnable with Self-Distillation
- [用交互稀疏度解释并改善深层 LLM 利用率](../conferences/icml-2026/cards/3301-3400.md#muhtar26a-training-strategies) · When Does Sparsity Mitigate the Curse of Depth in LLMs
- [从小模型微调更新生成大模型更新](../conferences/icml-2026/cards/3401-3500.md#nguyen26r-training-strategies) · Gradient Transformer: Learning to Generate Updates for LLMs
- [用同句的有无前缀蒸馏更新事实](../conferences/icml-2026/cards/3501-3600.md#padmanabhan26a-training-strategies) · Updating Parametric Knowledge with Context Distillation Retains Post-Training Capabilities
- [让掩码难度随可用上下文变化](../conferences/icml-2026/cards/3501-3600.md#parashar26a-training-strategies) · Learnability-Informed Fine-Tuning of Diffusion Language Models
- [按 Fisher 冲突筛选联邦 LoRA 上行层](../conferences/icml-2026/cards/3701-3800.md#qiu26w-training-strategies) · Less Is More in Federated Continual Learning: RieSelect for Conflict-Aware Layer Selection in LLMs
- [在并行扩散初稿后做最小编辑修复一致性](../conferences/icml-2026/cards/3801-3900.md#ren26t-training-strategies) · Edit-Based Refinement for Parallel Masked Diffusion Language Models
- [在预训练梯度路由中建立可组合权限](../conferences/icml-2026/cards/3801-3900.md#roland26a-training-strategies) · Modular Pretraining Enables Access Control
- [弱奖励训练前先恢复正确探索](../conferences/icml-2026/cards/3901-4000.md#ryd26a-training-strategies) · Removing Sandbagging in LLMs by Training with Weak Supervision
- [长上下文语言模型的训练推理分段一致性](../conferences/icml-2026/cards/4001-4100.md#shang26c-training-strategies) · Training–Inference Consistent Segmented Execution for Long-Context LLMs
- [从训练轨迹选择蒸馏词元](../conferences/icml-2026/cards/4001-4100.md#shen26i-training-strategies) · Training-Trajectory-Aware Token Selection
- [对齐稀疏与全注意的输出特征](../conferences/icml-2026/cards/4001-4100.md#shen26k-training-strategies) · SSA: Sparse Sparse Attention by Aligning Full and Sparse Attention Outputs in Feature Space
- [把各目标保留为共享主干上的独立头](../conferences/icml-2026/cards/4001-4100.md#shen26v-training-strategies) · Simultaneous Multi-objective Alignment Across Verifiable and Non-verifiable Rewards
- [让带示例的同一模型指导学生轨迹](../conferences/icml-2026/cards/4001-4100.md#shenfeld26a-training-strategies) · Self-Distillation Enables Continual Learning
- [同步增加数据难度与深度](../conferences/icml-2026/cards/4101-4200.md#singh26a-training-strategies) · Curriculum-Guided Layer Scaling for Language Model Pretraining
- [语义边缘锚定后训练](../conferences/icml-2026/cards/4201-4300.md#springer26a-training-strategies) · Annotations Mitigate Post-Training Mode Collapse
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
- [按序列拆分多token输出头以平衡流水](../conferences/icml-2026/cards/4701-4800.md#wang26gy-training-strategies) · AdaHC: Accelerating Multi-Token Prediction with Adaptive Head Chunking with Pipeline Parallelism
- [逐头长度温度与位置校准时机](../conferences/icml-2026/cards/4901-5000.md#wang26lk-training-strategies) · AdaRoPE: Not All Attention Heads Should Rotate and Scale Equally
- [预训练末期平坦化改善学习遗忘前沿](../conferences/icml-2026/cards/4901-5000.md#watts26a-training-strategies) · Sharpness-Aware Pretraining Mitigates Catastrophic Forgetting
- [摘要条件短程RL与回放](../conferences/icml-2026/cards/5001-5100.md#wu26as-training-strategies) · Reasoning Cache: Continual Improvement Over Long Horizons via Short-Horizon RL
- [高分歧软提示的定向遗忘修复](../conferences/icml-2026/cards/5101-5200.md#xia26j-training-strategies) · Adversarial Latent Embedding Repair for LLM Continual Learning
- [掩码生成与预测的对抗自监督RL](../conferences/icml-2026/cards/5101-5200.md#xing26c-training-strategies) · PretrainZero: Reinforcement Active Learning on Pretraining Data
- [路由器对所选专家的互补logit](../conferences/icml-2026/cards/5201-5300.md#xiong26p-training-strategies) · Token-Level LLM Collaboration via FusionRoute
- [预先蒸馏并缓存固定MoE路由](../conferences/icml-2026/cards/5201-5300.md#xu26t-training-strategies) · Grouter: Decoupling Routing from Representation for Accelerated MoE Training
- [先更新裁判再更新rubric的交替训练](../conferences/icml-2026/cards/5201-5300.md#xu26ai-training-strategies) · Alternating Reinforcement Learning for Rubric-Based Reward Modeling in Non-Verifiable LLM Post-Training
- [语义边效用代理驱动的廉价剪图](../conferences/icml-2026/cards/5401-5500.md#yang26bo-training-strategies) · AgentTailor: A Semantic-Aware LLM-Based Multi-Agent System with Actor-Critic Structure
- [用单共享浮点锚逐级派生二值残差路径](../conferences/icml-2026/cards/5501-5600.md#you26b-training-strategies) · RaBiT: Residual Aware Binarization Training for Accurate and Efficient LLMs
- [冻结或适配专家的双层mask选择](../conferences/icml-2026/cards/5601-5700.md#yu26bi-training-strategies) · Efficient Bilevel Optimization for CKA-Guided MoE Upcycling
- [逐token隐状态回馈的Jacobi预训练](../conferences/icml-2026/cards/5701-5800.md#zeng26l-training-strategies) · PonderLM-2: Pretraining LLM with Latent Thoughts in Continuous Space
- [联邦LoRA的正交规范对齐](../conferences/icml-2026/cards/5801-5900.md#zhang26cc-training-strategies) · FedRot-LoRA: Mitigating Rotational Misalignment in Federated LoRA
- [新解掩码token的偏好概率比](../conferences/icml-2026/cards/5901-6000.md#zhang26gt-training-strategies) · dTRPO : Trajectory Reduction in Policy Optimization of Diffusion Large Language Models
- [压缩视图训练与原始字节推理](../conferences/icml-2026/cards/6101-6200.md#zheng26e-training-strategies) · Proxy Compression for Language Modeling
- [先测扰动均值偏移再校正分类logit](../conferences/icml-2026/cards/6101-6200.md#zhou26a-training-strategies) · Harnessing Non-Adversarial Robustness in Large Language Models
- [用相反初始判决训练选择性反思](../conferences/icml-2026/cards/6201-6300.md#zhu26aw-training-strategies) · CAMEL: Confidence-Gated Reflection for Reward Modeling

<a id="by-computer-vision"></a>

### 计算机视觉

- [长视频生成](../conferences/icml-2026/cards/0301-0400.md#cai26h-training-strategies) · Mode Seeking meets Mean Seeking for Fast Long Video Generation
- [动态参数高效微调](../conferences/icml-2026/cards/0301-0400.md#cao26o-training-strategies) · Beyond Static Allocation: Dynamic Sensitivity-Aware Fine-Tuning for Vision Transformers
- [长上下文视频蒸馏](../conferences/icml-2026/cards/0601-0700.md#chen26eu-training-strategies) · Context Forcing: Consistent Autoregressive Video Generation with Long Context
- [图像词元化与生成联合训练](../conferences/icml-2026/cards/0701-0800.md#chu26b-training-strategies) · End-to-End Autoregressive Image Generation with 1D Semantic Tokenizer
- [稀疏软标签的硬标签校准](../conferences/icml-2026/cards/0701-0800.md#cui26g-training-strategies) · Hard Labels In! Rethinking the Role of Hard Labels in Mitigating Local Semantic Drift
- [视觉基础特征的压缩生成与细化](../conferences/icml-2026/cards/0901-1000.md#dong26l-training-strategies) · RePack then Refine: Efficient Diffusion Transformers with Vision Foundation Models
- [统一图像取证的受限低秩适配](../conferences/icml-2026/cards/0901-1000.md#du26g-training-strategies) · Can We Build a Monolithic Model for Fake Image Detection? SICA: Semantic-Induced Constrained Adaptation for Unified-Yet-Discriminative Artifact Feature Space Reconstruction
- [由图像功率谱确定扩散日程](../conferences/icml-2026/cards/1001-1100.md#esteves26a-training-strategies) · Spectrally-Guided Diffusion Noise Schedules
- [保留槽位的因素分区并在学习后回放解码器](../conferences/icml-2026/cards/2001-2100.md#kang26e-training-strategies) · Factor-Wise Homogeneity of Slot-Attention for Continual Object-Centric Learning
- [按学生不可学习区域选择教师熵](../conferences/icml-2026/cards/2301-2400.md#lee26g-training-strategies) · Toward Understanding Adversarial Distillation: Why Robust Teachers Fail
- [在图像球面方向上配对并学习流](../conferences/icml-2026/cards/2301-2400.md#lee26x-training-strategies) · Geometry-Aware Image Flow Matching
- [按实际输出漂移回收持续学习的秩](../conferences/icml-2026/cards/2501-2600.md#li26eq-training-strategies) · Energy-Structured Low-Rank Adaptation for Continual Learning
- [在测试时无标签更新中按样本裁剪并加噪](../conferences/icml-2026/cards/2501-2600.md#li26fy-training-strategies) · Private and Stable Test-time Adaptation with Differential Privacy
- [把正交投影丢掉的梯度送到任务分支](../conferences/icml-2026/cards/2701-2800.md#lin26aj-training-strategies) · GR-LoRA: Gradient-Recycling Low-Rank Adaptation for Class-Incremental Learning
- [稀疏相机控制的三维几何蒸馏](../conferences/icml-2026/cards/2801-2900.md#liu26bj-training-strategies) · CamGeo: Sparse Camera-Conditioned Image-to-Video Generation with 3D Geometry Priors
- [在偏好样本中保留优劣图像的真实初始噪声](../conferences/icml-2026/cards/3001-3100.md#lu26ai-training-strategies) · Offline Preference Optimization for Rectified Flow with Noise-Tracked Pairs
- [持续学习低秩知识合成](../conferences/icml-2026/cards/3001-3100.md#luo26ag-training-strategies) · SABER: Continual Learning with Representation Conflict Management
- [沿帧轴和去噪轴切换视频扩散粒度](../conferences/icml-2026/cards/3101-3200.md#ma26b-training-strategies) · Flex-Forcing: Towards a Unified Autoregressive and Bidirectional Video Diffusion Model
- [用对抗模仿降低流式生成器与示范轨迹分布差](../conferences/icml-2026/cards/3101-3200.md#ma26u-training-strategies) · FAIL: Flow Matching Adversarial Imitation Learning for Image Generation
- [视觉模块可塑性](../conferences/icml-2026/cards/3401-3500.md#odonnat26a-training-strategies) · Vision Transformer Finetuning Benefits from Non-Smooth Components
- [用梯度噪声和原型共同约束持续分割](../conferences/icml-2026/cards/3501-3600.md#pandey26b-training-strategies) · Continual Segmentation under Joint Nonstationarity
- [低比特校准随模型刷新注意力样本](../conferences/icml-2026/cards/3701-3800.md#qian26j-training-strategies) · Selective Coupling of Decoupled Informative Regions: Masked Attention Alignment for Data-Free Quantization of Vision Transformers
- [把扩散授权与具体样本绑定](../conferences/icml-2026/cards/3701-3800.md#qin26k-training-strategies) · GoodDiffusion: Proactive Copyright Protection for Diffusion Bridge Models via Learnable Sample-specific Signatures
- [按潜在结构簇拆分教师诱发的标签噪声](../conferences/icml-2026/cards/3801-3900.md#ren26i-training-strategies) · MIND: Decoupling Model-Induced Label Noise via Latent Manifold Disentanglement
- [按激活几何跨宽度迁移任务向量](../conferences/icml-2026/cards/3801-3900.md#rinaldi26a-training-strategies) · Transporting Task Vectors across Different Architectures without Training
- [跨域留出教师蒸馏](../conferences/icml-2026/cards/4201-4300.md#song26af-training-strategies) · DomED: Redesigning Ensemble Distillation for Domain Generalization
- [记忆条件对齐的蒸馏](../conferences/icml-2026/cards/4301-4400.md#sun26az-training-strategies) · WorldPlay: Towards Long-Term Geometric Consistency for Real-Time Interactive World Modeling
- [感知前置RL与任务梯度分配](../conferences/icml-2026/cards/4301-4400.md#tan26b-training-strategies) · VideoVeritas: AI-Generated Video Detection via Perception Pretext Reinforcement Learning
- [reuse-gradients-to-diagnose-fast-at-collapse](../conferences/icml-2026/cards/4401-4500.md#teymourian26a-training-strategies) · SORA: Free Second-Order Attacks in Fast Adversarial Training
- [视频模型的三帧视觉修正](../conferences/icml-2026/cards/4401-4500.md#tong26a-training-strategies) · CoF-T2I: Video Models as Pure Visual Reasoners for Text-to-Image Generation
- [uncertainty-modulated-bridge](../conferences/icml-2026/cards/4501-4600.md#tu26d-training-strategies) · Unifying Heterogeneous Degradations: Uncertainty-Aware Diffusion Bridge Model for All-in-One Image Restoration
- [点图x预测与纯噪声端点训练](../conferences/icml-2026/cards/5201-5300.md#xu26bm-training-strategies) · PointDiT: Pixel-Space Diffusion for Monocular Geometry Estimation
- [冻结扩散骨干的控制侧网络](../conferences/icml-2026/cards/5401-5500.md#yang26bk-training-strategies) · Diffusion Controller: Framework, Algorithms and Parameterization
- [干净扰动配对的路径选择与权重变换](../conferences/icml-2026/cards/5401-5500.md#yang26bn-training-strategies) · Suppress and Diversify: Refining Robust Pathways for Corruption Robustness
- [按QAT后敏感度分配激活位宽](../conferences/icml-2026/cards/5401-5500.md#yang26dm-training-strategies) · RobuQ: Pushing DiTs to W1.58A2 via Robust Activation Quantization
- [CLIP弱patch抑制与强patch增强](../conferences/icml-2026/cards/5501-5600.md#yi26f-training-strategies) · Improving CLIP Adaptation by Breaking Tail Alignment for Source-Free Cross-Domain Few-Shot Learning
- [用区间平均速度指导flow蒸馏](../conferences/icml-2026/cards/6001-6100.md#zhao26bx-training-strategies) · Mean Flow Distillation: Robust and Stable Distillation for Flow Matching Models
- [配对spike与surrogate原函数通路做SSL](../conferences/icml-2026/cards/6101-6200.md#zhou26g-training-strategies) · SpikeCLR: Self-Supervised Contrastive Learning for Visual Representations with Spiking Neural Networks
- [AR diffusion学生的ODE初始化匹配条件信息](../conferences/icml-2026/cards/6201-6300.md#zhu26bf-training-strategies) · Causal Forcing: Autoregressive Diffusion Distillation Done Right for High-Quality Real-Time Interactive Video Generation

<a id="by-nlp"></a>

### 自然语言处理

- [跨语种回答分布的一致性对齐](../conferences/icml-2026/cards/2801-2900.md#liu26dd-training-strategies) · Post-Training Language Models for Crosslingual Consistency
- [冻结与微调双视图的稳健分解](../conferences/icml-2026/cards/5601-5700.md#yu26bx-training-strategies) · Causal Fine-Tuning under Latent Confounded Shift

<a id="by-reinforcement-learning"></a>

### 强化学习

- [按宽度与深度缩放策略网络的参数和更新](../conferences/icml-2026/cards/2301-2400.md#lee26ai-training-strategies) · CompleteP for RL: Maintaining Feature Learning When Scaling Deep Reinforcement Learning
- [先覆盖有先修关系的课程图再训练前沿](../conferences/icml-2026/cards/2701-2800.md#liu26j-training-strategies) · Active Curriculum Refinement for Reinforcement Learning
- [用动作分布漂移动态调节在线 RL 批大小](../conferences/icml-2026/cards/3501-3600.md#park26w-training-strategies) · Scalable Reinforcement Learning via Adaptive Batch Scaling
- [用未来状态把多解动作拆成条件选择](../conferences/icml-2026/cards/3901-4000.md#schafer26a-training-strategies) · When Does Predictive Inverse Dynamics Outperform Behavior Cloning?
- [有置信门控的奖励补全](../conferences/icml-2026/cards/4101-4200.md#shihab26d-training-strategies) · What Reward Structure Enables Efficient Sparse-Reward RL? A Proof-of-Concept with Policy-Aware Matrix Completion
- [TD误差累计均值的平方根熵调度](../conferences/icml-2026/cards/4801-4900.md#wang26jc-training-strategies) · Tracking Drift: Variation-Aware Entropy Scheduling for Non-Stationary Reinforcement Learning
- [几何增长的目标网络冻结周期](../conferences/icml-2026/cards/4901-5000.md#weissmann26a-training-strategies) · The Role of Target Update Frequencies in Q-Learning
- [用BC对数概率预热AIL奖励](../conferences/icml-2026/cards/5201-5300.md#xu26j-training-strategies) · Provably Efficient Policy-Reward Co-Pretraining for Adversarial Imitation Learning
- [交替优化latent policy并把改进蒸馏到固定prior decoder](../conferences/icml-2026/cards/5901-6000.md#zhang26fu-training-strategies) · Generative Online Reinforcement Learning

<a id="by-robotics"></a>

### 机器人学

- [部件位姿的弱监督对称估计](../conferences/icml-2026/cards/0601-0700.md#chen26fw-training-strategies) · Generalizable and Actionable Parts Pose Estimation with Symmetry Annotation-Free Learning Strategy
- [视觉动作策略与世界模型的交替改进](../conferences/icml-2026/cards/1301-1400.md#guo26i-training-strategies) · VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model
- [用频域监督衔接连续动作块](../conferences/icml-2026/cards/1501-1600.md#he26aq-training-strategies) · FocalPolicy: Frequency-Optimized Chunking and Locally Anchored Flow Matching for Coherent Visuomotor Policy
- [训练控制端显式处理过期语义](../conferences/icml-2026/cards/1701-1800.md#huang26cd-training-strategies) · TIC-VLA: A Think-in-Control Vision-Language-Action Model for Robot Navigation in Dynamic Environments
- [仿真与真实数据联合训练](../conferences/icml-2026/cards/2301-2400.md#lei26d-training-strategies) · A Mechanistic Analysis of Sim-and-Real Co-Training in Generative Robot Policies
- [用视觉先验与语言后验分离动作信号](../conferences/icml-2026/cards/2601-2700.md#lian26d-training-strategies) · LangForce: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries
- [用后继观察降低少标注动作学习难度](../conferences/icml-2026/cards/3301-3400.md#morin26a-training-strategies) · On the Sample Efficiency of Inverse Dynamics Models for Semi-Supervised Imitation Learning
- [为RL保留动作后验覆盖](../conferences/icml-2026/cards/4501-4600.md#wagenmaker26a-training-strategies) · Posterior Behavioral Cloning: Pretraining BC Policies for Efficient RL Finetuning
- [dual-on-policy-distillation](../conferences/icml-2026/cards/4501-4600.md#wan26n-training-strategies) · Adversarial Dual On-Policy Distillation from Expressive Teacher
- [潜动作接口预热与联合训练坍塌](../conferences/icml-2026/cards/4801-4900.md#wang26kz-training-strategies) · Co-Evolving Latent Action World Models
- [VLA的本体感知路由与频域动作监督](../conferences/icml-2026/cards/5001-5100.md#wu26m-training-strategies) · VLANeXt: Recipes for Building Strong VLA Models
- [渐进约束教师的扩散策略后训练](../conferences/icml-2026/cards/5001-5100.md#wu26ck-training-strategies) · PACT: Self-Evolving Physical Safety Alignment for Diffusion Policies in Embodied Manipulation
- [在IL与RL组合中选择规划mask](../conferences/icml-2026/cards/6101-6200.md#zheng26z-training-strategies) · CoIRL-AD: Collaborative-Competitive Imitation-Reinforcement Learning in Latent World Models for Autonomous Driving

<a id="by-multimodal"></a>

### 多模态学习

- [多模态微调](../conferences/icml-2026/cards/0101-0200.md#asadollahzadeh26a-training-strategies) · TRACER: Persistent Regularization for Robust Multimodal Finetuning
- [视觉数据与符号绑定](../conferences/icml-2026/cards/0301-0400.md#buzeta26a-training-strategies) · Seeing to Generalize: How Visual Data Corrects Binding Shortcuts
- [多模态蒸馏的视觉与转移对齐](../conferences/icml-2026/cards/0601-0700.md#chen26gr-training-strategies) · Beyond Next-Token Alignment: Distilling Multimodal Large Language Models via Token Interactions
- [权重差迁移语音指令能力](../conferences/icml-2026/cards/0901-1000.md#du26t-training-strategies) · Unlocking Speech–Text Compositional Powers: Instruction-Following Speech Language Models without Instruction Tuning
- [多奖励条件的图像生成预训练](../conferences/icml-2026/cards/0901-1000.md#dufour26a-training-strategies) · MIRO: MultI-Reward cOnditioned pretraining improves T2I quality and efficiency
- [按实际梯度曝光量控制多模态尾部压力](../conferences/icml-2026/cards/1501-1600.md#hong26b-training-strategies) · Coverage $\not =$ Exposure: Auditable Control of Same-Support Tail Failures under Multimodal Missingness
- [用同类跨模态随机配对平滑监督](../conferences/icml-2026/cards/2301-2400.md#lee26bk-training-strategies) · Understanding Multimodal Learning: A Loss Landscape Smoothness Perspective
- [把语言多选题分布蒸馏为视觉类别概念签名](../conferences/icml-2026/cards/2701-2800.md#liang26ac-training-strategies) · Large Language Model Teaches Visual Students: Cross-Modality Transfer of Fine-Grained Conceptual Knowledge
- [在词义和声学冲突时学习用声学作答](../conferences/icml-2026/cards/3501-3600.md#pang26b-training-strategies) · Do Audio LLMs Listen or Read? Analyzing and Mitigating Paralinguistic Failures with VoxParadox
- [质量指称转成分割点提示](../conferences/icml-2026/cards/3601-3700.md#peng26j-training-strategies) · IQA-Spider: Unifying Multi-Granularity Image Quality Assessment with Reasoning, Grounding and Referring
- [持续个性化的参数覆盖选址](../conferences/icml-2026/cards/3601-3700.md#peng26n-training-strategies) · SCNS: Continual Personalization of Diffusion Models via Submodular Concept Neuron Selection
- [多内在表征生成辅助理解](../conferences/icml-2026/cards/4201-4300.md#su26n-training-strategies) · Generation Enhances Understanding in Unified Multimodal Models via Multi-Representation Generation
- [scale-conditioned-spatial-learning](../conferences/icml-2026/cards/4201-4300.md#sun26q-training-strategies) · SpaceVista: All-Scale Visual Spatial Reasoning from mm to km
- [统一多模态的数据与目标耦合](../conferences/icml-2026/cards/4401-4500.md#tong26c-training-strategies) · Beyond Language Modeling: An Exploration of Multimodal Pretraining
- [answer-coupled-video-localization](../conferences/icml-2026/cards/4501-4600.md#wang26e-training-strategies) · Video-in-the-Loop: Span-Grounded Long Video QA with Interleaved Reasoning
- [Text Before Vision: Staged Knowledge Injection Matters for Agentic RLVR in Ultra-High-Resolution Remote Sensing Understanding](../conferences/icml-2026/cards/4601-4700.md#wang26u-training-strategies) · Text Before Vision: Staged Knowledge Injection Matters for Agentic RLVR in Ultra-High-Resolution Remote Sensing Understanding
- [参考视觉视野对齐作为课程和奖励](../conferences/icml-2026/cards/4701-4800.md#wang26gt-training-strategies) · Seeing is Solving: Unlocking Efficient Multimodal RL via View Alignment
- [临时专家竞争决定扩容层](../conferences/icml-2026/cards/4801-4900.md#wang26le-training-strategies) · CoPE: Continual Probe-guided Expansion for Large Vision-Language Models
- [结构与语义目标的参数路由](../conferences/icml-2026/cards/5301-5400.md#yang26ae-training-strategies) · MUSE: Resolving Manifold Misalignment in Visual Tokenization via Topological Orthogonality
- [融合浅层特征时隔离skip梯度](../conferences/icml-2026/cards/5601-5700.md#yuan26n-training-strategies) · Detached Skip-Links and $R$-Probe: Decoupling Feature Aggregation from Gradient Propagation for MLLM OCR
- [按速度场消融选择REPA层](../conferences/icml-2026/cards/5901-6000.md#zhang26gw-training-strategies) · AG-REPA: Causal Layer Selection for Representation Alignment in Audio Flow Matching

<a id="by-ml-foundations"></a>

### 机器学习基础与统计

- [联邦 LoRA](../conferences/icml-2026/cards/0201-0300.md#bian26e-training-strategies) · FedTreeLoRA: Reconciling Statistical and Functional Heterogeneity in Federated LoRA Fine-Tuning
- [状态空间模型训练](../conferences/icml-2026/cards/0301-0400.md#brady26a-training-strategies) · Efficient Learning of Deep State Space Models via Importance Smoothing
- [递归去噪训练](../conferences/icml-2026/cards/0301-0400.md#cameron26a-training-strategies) · One Step Forward and K Steps Back: Better Reasoning with Denoising Recursion Models
- [离散扩散采样](../conferences/icml-2026/cards/0401-0500.md#carter26a-training-strategies) · Discrete Diffusion Samplers and Bridges: Off-Policy Algorithms and Applications in Latent Spaces
- [生成流的先验](../conferences/icml-2026/cards/0401-0500.md#chemseddine26a-training-strategies) · Adapting Noise to Data: Generative Flows from Learned 1D Processes
- [测试时因果结构学习](../conferences/icml-2026/cards/0401-0500.md#chen26t-training-strategies) · Test-Time Learning of Causal Structure from Interventional Data
- [离线 GFlowNet 的边奖励引导](../conferences/icml-2026/cards/0601-0700.md#chen26ej-training-strategies) · Beyond the Proxy: Trajectory-Distilled Guidance for Offline GFlowNet Training
- [面向后续适配的模型合并](../conferences/icml-2026/cards/0601-0700.md#chen26gq-training-strategies) · Learn to Merge: Meta-Learning for Adaptive Multi-Task Model Merging
- [逐步域适应的半对偶传输](../conferences/icml-2026/cards/0601-0700.md#chen26hd-training-strategies) · Rethinking the Flow-based Gradual Domain Adaptation: A Semi-Dual Optimal Transport Perspective
- [多目标扩散模型的半监督蒸馏](../conferences/icml-2026/cards/0601-0700.md#cheng26g-training-strategies) · Multi-Objective Learning for Diffusion Models: A Statistical Theory under Semi-Supervised Learning
- [二值贝叶斯网络的主动持续学习](../conferences/icml-2026/cards/0701-0800.md#cottart26a-training-strategies) · Active Continual Learning with Metaplastic Binary Bayesian Neural Networks
- [GFlowNet 互补探索](../conferences/icml-2026/cards/0801-0900.md#dall-antonia26a-training-strategies) · Avoid What You Know: Divergent Trajectory Balance for GFlowNets
- [扩散模型记忆的中等噪声区间](../conferences/icml-2026/cards/0901-1000.md#dodson26a-training-strategies) · Two Calm Ends and the Wild Middle: A Geometric Picture of Memorization in Diffusion Models
- [临界信号传播的分层 dropout](../conferences/icml-2026/cards/1101-1200.md#fernandez-sarmiento26a-training-strategies) · Dropout Universality: Scaling Laws and Optimal Scheduling at the Edge-of-Chaos
- [联合能量模型的边缘采样](../conferences/icml-2026/cards/1201-1300.md#geng26b-training-strategies) · Latent-Guided Cooperative Energy-Based Models
- [表格 MLP 超参数并行集成](../conferences/icml-2026/cards/1301-1400.md#gorishniy26a-training-strategies) · TabPack: Efficient Hyperparameter Ensembles for Tabular Deep Learning
- [在指数族中迁移微调因子](../conferences/icml-2026/cards/1301-1400.md#guo26y-training-strategies) · Fine-Tune Once, Reuse Across Models: Bayesian Task-Update Factors and Approximations
- [面向合并结果选择专家停止点](../conferences/icml-2026/cards/1501-1600.md#horoi26a-training-strategies) · From Memorization to Parameter Interference: How Overtraining Experts Harms Model Merging
- [沿约束流形法向扩展训练分布](../conferences/icml-2026/cards/2001-2100.md#keegan26a-training-strategies) · Manifold-Aware Perturbations for Constrained Generative Modeling
- [以随机补全做条件，仅用真实观测训练去噪](../conferences/icml-2026/cards/2101-2200.md#kim26bh-training-strategies) · AugMask: Training Diffusion Models on Incomplete Tabular Data via Stochastic Augmentation and Masking
- [轮流更新小权重切片保留累计方向](../conferences/icml-2026/cards/2201-2300.md#kowsher26b-training-strategies) · SliceFine: The Universal Winning-Slice Hypothesis for Pretrained Networks
- [用排队预测决定每轮联邦训练做多少本地工作](../conferences/icml-2026/cards/2401-2500.md#li26ae-training-strategies) · FedQueue: Queue-Aware Federated Learning for Cross-Facility HPC Training
- [合并模型时校准共享方向的幅值](../conferences/icml-2026/cards/2501-2600.md#li26ep-training-strategies) · When Shared Knowledge Hurts: Spectral Over-Accumulation in Model Merging
- [沿固定点轨迹蒸馏少步平衡求解器](../conferences/icml-2026/cards/2701-2800.md#lin26w-training-strategies) · Consistency Deep Equilibrium Models
- [跨数据孤岛组合生成因素](../conferences/icml-2026/cards/3301-3400.md#morshed26a-training-strategies) · Compositional Generative Modeling from Decentralized Data
- [在重尾坐标上做对数退火](../conferences/icml-2026/cards/3501-3600.md#pachebat26a-training-strategies) · Tail Annealing for Heavy-Tailed Flow Matching
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
- [失配稳健的序贯实验分配](../conferences/icml-2026/cards/4901-5000.md#wen26i-training-strategies) · Robust Sequential Experimental Design for A/B Testing
- [带任意类索引的噪声域对齐](../conferences/icml-2026/cards/5401-5500.md#yao26m-training-strategies) · Semi-Supervised Noise Adaptation: Transferring Knowledge from Noise Domain
- [在近参数量匹配下先扫天气模型宽深比](../conferences/icml-2026/cards/5501-5600.md#yu26r-training-strategies) · Scaling Laws of Global Weather Models
- [以permutation VI训练变长插入顺序](../conferences/icml-2026/cards/5901-6000.md#zhang26fx-training-strategies) · Variational Learning for Insertion-based Generation
- [以谱重建残差调每样本dropout](../conferences/icml-2026/cards/6101-6200.md#zhong26l-training-strategies) · DropoutTS: Sample-Adaptive Dropout for Robust Time Series Forecasting
- [用共同切空间定义流形平均速度](../conferences/icml-2026/cards/6101-6200.md#zhong26p-training-strategies) · Riemannian MeanFlow for One-Step Generation on Manifolds

<a id="by-graph-and-recommendation"></a>

### 图学习与推荐

- [图基础模型的消息微调](../conferences/icml-2026/cards/0501-0600.md#chen26cz-training-strategies) · Message Tuning Outshines Graph Prompt Tuning: A Prismatic Space Perspective
- [随机增删边后对齐推理消息期望](../conferences/icml-2026/cards/3901-4000.md#saber26a-training-strategies) · RADE: Random Add-Drop Edge as a Regularizer

<a id="by-scientific-ml"></a>

### 科学机器学习

- [层级仿真推断](../conferences/icml-2026/cards/0401-0500.md#charles26a-training-strategies) · Tokenised Flow Matching for Hierarchical Simulation Based Inference
- [确定性 PDE 模拟器的概率改造](../conferences/icml-2026/cards/0801-0900.md#diaconu26a-training-strategies) · Probabilistic Retrofitting of Learned Simulators
- [按原子数缩放分子扩散先验](../conferences/icml-2026/cards/1201-1300.md#gao26v-training-strategies) · Scaling the Prior: Size-Consistent Geometric Diffusion for 3D Molecular Generation
- [让神经信号预训练覆盖下游任务的时间尺度](../conferences/icml-2026/cards/1801-1900.md#jayalath26b-training-strategies) · MEG-XL: Data-Efficient Brain-to-Text via Long-Context Pre-Training
- [用回归、上下文去噪与局部性诱导不同轨道世界模型](../conferences/icml-2026/cards/2801-2900.md#liu26aj-training-strategies) · From Kepler to Newton: Inductive Biases Guide Learned World Models in Transformers
- [让分子结构与序列的生成时钟学习最优耦合](../conferences/icml-2026/cards/3701-3800.md#qiu26r-training-strategies) · Demystifying Multimodal Biomolecular Co-design With Intrinsic Geodesic Coupling
- [只用瞬时力学习大步长动力学](../conferences/icml-2026/cards/3801-3900.md#ripken26a-training-strategies) · Learning Hamiltonian Flow Maps: Mean Flow Consistency for Large-Timestep Molecular Dynamics
- [采样与梯度分开定精度](../conferences/icml-2026/cards/4101-4200.md#solinas26a-training-strategies) · Neural Quantum States in Mixed Precision
<!-- classification:end -->
