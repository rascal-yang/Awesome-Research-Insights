# 推理策略

[首页](../README.md) · [参与贡献](../CONTRIBUTING.md) · [English](../en/insights/inference.md)

解码、测试时适配与高效执行。

<!-- classification:start -->
## 按研究领域浏览

### 大语言模型

- [表征干预](../papers/llm.md#abdullaev26a-inference) · Concept Heterogeneity-aware Representation Steering
- [交互式研究 Agent](../papers/llm.md#ai26a-inference) · An Interactive Paradigm for Deep Research
- [多模型答案聚合](../papers/llm.md#ai26d-inference) · Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information
- [动态推理预算](../papers/llm.md#akhauri26a-inference) · Compute Where it Counts: Self Optimizing Language Models
- [小模型 Agent 路由](../papers/llm.md#alazraki26a-inference) · Scaling Small Agents Through Strategy Auctions
- [模型文本溯源](../papers/llm.md#ardoin26a-inference) · LLM Self-Recognition: Steering and Retrieving Activation Signatures
- [多 Agent 红队](../papers/llm.md#asad26a-inference) · RedDebate: Safer Responses Through Multi-Agent Red Teaming Debates
- [离散扩散搜索](../papers/llm.md#bai26f-inference) · PRISM: Efficient Test-Time Scaling via Hierarchical Search and Self-Verification for Discrete Diffusion Language Models
- [偏好对齐解码](../papers/llm.md#berdoz26a-inference) · Alignment-Aware Decoding
- [KV 缓存压缩](../papers/llm.md#bhatnagar26a-inference) · STAR-KV: Low-Rank KV Cache Compression via Soft Thresholding for Adaptive Rank Control
- [推理预算分配](../papers/llm.md#bilal26a-inference) · What If We Allocate Test-Time Compute Adaptively?
- [冷启动个性化](../papers/llm.md#bose26a-inference) · Cold-Start Personalization via Bayesian Adaptive Questioning
- [MoE 稀疏推理](../papers/llm.md#cai26i-inference) · Mining Tensor/Neuron-Level Sparsity to Maximize Mixture-of-Experts Potential in Post-Training and Inference
- [扩散语言模型解码](../papers/llm.md#cao26d-inference) · Search or Accelerate: Confidence-Switched Position Beam Search for Diffusion Language Models
- [LLM 推理隐私](../papers/llm.md#cao26q-inference) · OSNIP: Balancing the Privacy-Utility-Efficiency Trilemma in LLM Inference via Obfuscated Semantic Null Space
- [模型路由](../papers/llm.md#cao26ac-inference) · Models Under SCOPE: Scalable and Controllable Routing via Pre-hoc Reasoning
- [非结构化稀疏推理](../papers/llm.md#cetin26a-inference) · Sparser, Faster, Lighter Transformer Language Models
- [自投机解码](../papers/llm.md#cha26a-inference) · KnapSpec: Self-Speculative Decoding via Adaptive Layer Selection as a Knapsack Problem
- [跨层 KV 缓存压缩](../papers/llm.md#chang26d-inference) · xKV: Cross-Layer KV-Cache Compression via Aligned Singular Vector Extraction
- [GUI 流程复用](../papers/llm.md#chen26ar-inference) · AutoRPA: Efficient GUI Automation through LLM-Driven Code Synthesis from Interactions
- [分级披露文本水印](../papers/llm.md#chen26bs-inference) · Selective Disclosure Watermarking for Large Language Models
- [块扩散投机解码](../papers/llm.md#chen26bv-inference) · DFlash: Block Diffusion for Flash Speculative Decoding
- [树搜索 KV 缓存管理](../papers/llm.md#chen26cd-inference) · ArborKV: Structure-Aware KV Cache Management for Scaling Tree-based LLM Reasoning
- [扩散语言模型解码](../papers/llm.md#chen26ci-inference) · Beyond Confidence: Adaptive and Coherent Decoding for Diffusion Language Models
- [堆内存循环不变量生成](../papers/llm.md#chen26cm-inference) · MALICE: Memory-aware Loop Invariants Generation on Symbolic Execution Traces
- [动态检索抗投毒](../papers/llm.md#chen26cw-inference) · RADAR: Defending RAG Dynamically against Retrieval Corruption
- [指令与上下文示例联合选择](../papers/llm.md#chen26dt-inference) · SMILE: Extended Deep Submodular Function-Based Instruction and In-context Learning Demonstration Selection
- [神经元一致性解码](../papers/llm.md#chen26eo-inference) · Do LLMs Signal When They’re Right? Evidence from Neuron Agreement
- [细粒度 MoE 专家采样](../papers/llm.md#chen26er-inference) · Certain Head, Uncertain Tail: Expert-Sample for Test-Time Scaling in Fine-Grained MoE
- [检索证据净化与推导](../papers/llm.md#chen26et-inference) · From Extraction to Deduction: Resolving Functional Misalignment in RAG via a Collaborative Critic-Reasoner Framework
- [投机解码的动态草稿词表](../papers/llm.md#chen26fm-inference) · NanoSpec: Accelerating Speculative Decoding using Minimalist In-Context Vocabularies
- [智能体批推理的缓存拥塞控制](../papers/llm.md#chen26fs-inference) · CONCUR: High-Throughput Agentic Batch Inference of LLM via Congestion-Based Concurrency Control
- [批容量与缓存的影子价格路由](../papers/llm.md#chen26ft-inference) · Online Linear Programming for Multi-Objective Routing in LLM Serving
- [逐题技能路由与专家批处理](../papers/llm.md#chen26fy-inference) · Skill-Based Mixture-of-Experts: Adaptive Routing for Heterogeneous Reasoning via Inferred Skills
- [语言模型 SVD 压缩的分级秩分配](../papers/llm.md#chen26ge-inference) · CGSVD: Cascaded Granular Singular Value Decomposition for Large Language Model Compression
- [风险聚合引导的解码回滚](../papers/llm.md#chen26ha-inference) · RBCBF: Decoding Time Safety Alignment via Risk Guided Rollback and Barrier Control
- [代码文档的依赖感知搜索](../papers/llm.md#cheng26c-inference) · Escaping Whack-a-Mole: Optimizing Documentation as Repo-Specific Playbooks for Coding Agents
- [MXFP4 的溢出感知缩放](../papers/llm.md#chhugani26a-inference) · Unveiling the Potential of Quantization with MXFP4: Strategies for Quantization Error Reduction
- [证据排列混合的拒答门控](../papers/llm.md#chlon26a-inference) · Predictable Compression Failures: Order Sensitivity and Information Budgeting for Evidence-Grounded Binary Adjudication
- [主奇异子空间保留后再量化](../papers/llm.md#cho26e-inference) · Preserve-Then-Quantize: Balancing Rank Budgets for Quantization Error Reconstruction in LLMs
- [相关筛选与干预验证的 SAE 引导](../papers/llm.md#cho26h-inference) · CorrSteer: Generation-Time LLM Steering via Correlated Sparse Autoencoder Features
- [低延迟分词的绑核与轮询](../papers/llm.md#choi26b-inference) · PinTok: Tokenizers Deserve Dedicated Pinned CPU-Compute and Memory
- [同谱系模型的上下文忠实性门控](../papers/llm.md#choi26e-inference) · The Truth Stays in the Family: Enhancing Contextual Truthfulness via Inherited Heads in Model Lineages
- [RAG 段落注意力方差过滤](../papers/llm.md#choudhary26b-inference) · Through the Stealth Lens: Attention-Aware Defenses Against Poisoning in RAG
- [多层原型输入审核](../papers/llm.md#chrabaszcz26a-inference) · Efficient LLM Moderation with Multi-Layer Latent Prototypes
- [长上下文思维链示例排序](../papers/llm.md#chung26c-inference) · Many-Shot CoT-ICL: Making In-Context Learning Truly Learn
- [概率常识溯因推理](../papers/llm.md#cotnareanu26a-inference) · Abductive Reasoning with Probabilistic Commonsense
- [含平局偏好的分布校准聚合](../papers/llm.md#dadkhahi26a-inference) · Distribution-Calibrated Inference Time Compute for Thinking LLM-as-a-Judge
- [全局约束的序贯蒙特卡洛解码](../papers/llm.md#dang26c-inference) · Mitigating Bias in Locally Constrained Decoding via Tractable Proposals
- [KV 缓存的窗口离群保留](../papers/llm.md#datta26b-inference) · ManifoldKV: Training-Free KV Cache Compression via Euclidean Outlier Detection
- [推理生成中的动态弃答](../papers/llm.md#davidov26a-inference) · Knowing When to Quit: A Principled Framework for Dynamic Abstention in LLM Reasoning
- [词元几何感知的截断解码](../papers/llm.md#davoodi26a-inference) · Geometry-Aware Decoding with Wasserstein-Regularized Truncation and Mass Penalties for Large Language Models
- [用注意力温度缓解上下文分布偏移](../papers/llm.md#demir26a-inference) · Optimal Attention Temperature Improves the Robustness of In-Context Learning under Distribution Shift in High Dimensions
- [混合专家的全局渐进量化](../papers/llm.md#deng26t-inference) · GEMQ: Global Expert-Level Mixed-Precision Quantization for MoE LLMs
- [预算约束下的自适应群体提问](../papers/llm.md#ding26d-inference) · Whom to Query for What: Adaptive Group Elicitation via Multi-Turn LLM Interactions
- [端云推理的依赖感知子任务路由](../papers/llm.md#dong26g-inference) · HybridFlow: Resource-Adaptive Subtask Routing for Efficient Edge-Cloud LLM Inference
- [以未来注意力训练 KV 淘汰](../papers/llm.md#dong26h-inference) · ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution

### 计算机视觉

- [扩散模型逻辑控制](../papers/computer-vision.md#alesiani26a-inference) · Logical Guidance for the Exact Composition of Diffusion Models
- [图像隐写](../papers/computer-vision.md#bae26b-inference) · Training-Free Coverless Multi-Image Steganography with Access Control
- [扩散逆问题](../papers/computer-vision.md#bang26a-inference) · Triadic Dynamics Aware Diffusion Posterior Sampling for Inverse Problems: Optimizing Guidance and Stochasticity Schedules
- [潜空间流匹配](../papers/computer-vision.md#briq26a-inference) · Exploring and Exploiting Stability in Latent Flow Matching
- [无分类器引导](../papers/computer-vision.md#cai26g-inference) · Improving Classifier-Free Guidance of Flow Matching via Manifold Projection
- [多实例图像到三维](../papers/computer-vision.md#cai26n-inference) · TIMI: Training-Free Image-to-3D Multi-Instance Generation with Spatial Fidelity
- [低延迟图像压缩](../papers/computer-vision.md#cao26e-inference) · Efficient Learned Image Compression without Entropy Coding
- [扩散正负概念引导](../papers/computer-vision.md#chang26c-inference) · ContrastiveCFG: Guiding Diffusion Sampling by Contrasting Positive and Negative Concepts
- [免训练视频异常检测](../papers/computer-vision.md#chen26v-inference) · PRISM: Training-Free Video Anomaly Detection via Intrinsic Statistical Modeling
- [归一化流采样](../papers/computer-vision.md#chen26aj-inference) · Normalizing Flows with Iterative Denoising
- [流匹配的双锚点积分](../papers/computer-vision.md#chen26bp-inference) · Bi-Anchor Interpolation Solver for Accelerating Generative Modeling
- [网格词元的投机解码](../papers/computer-vision.md#chen26dn-inference) · XSpecMesh: Quality-Preserving Auto-Regressive Mesh Generation Acceleration via Multi-Head Speculative Decoding
- [新视角扩散的语义条件](../papers/computer-vision.md#chen26ey-inference) · SemanticNVS: Improving Semantic Scene Understanding in Generative Novel View Synthesis
- [自回归图像采样的轨迹剪枝](../papers/computer-vision.md#chen26fc-inference) · ScalingAR: Scaling Confidence for Autoregressive Image Generation
- [桥式生成模型的分频先验引导](../papers/computer-vision.md#chen26fq-inference) · GuidedBridge: Training-freely Improving Bridge Models with Prior Guidance
- [图像到点云配准的动态交互深度](../papers/computer-vision.md#cheng26b-inference) · FS-I2P: A Hierarchical Focus–Sweep Registration Network with Dynamically Allocated Depth
- [扩散采样的切向增量放大](../papers/computer-vision.md#cho26a-inference) · TAG: Tangential Amplifying Guidance for Hallucination-Resistant Sampling
- [扩散注意力的反对称分量调节](../papers/computer-vision.md#cho26d-inference) · Balancing Fidelity and Diversity in Diffusion Models via Symmetric Attention Decomposition: Hopfield Perspective
- [扩散负引导的阈值投影](../papers/computer-vision.md#choi26m-inference) · Concept Removal Guidance: Evidence-Calibrated Negative Guidance for Safe Diffusion Sampling
- [扩散 Transformer 激活稀疏推理](../papers/computer-vision.md#cong26a-inference) · RT-Lynx: Putting GEMM Sparsity in the Right Place for Diffusion Models
- [场景图粒子滤波定位](../papers/computer-vision.md#damblon26a-inference) · SG2Loc: Sequential Visual Localization on 3D Scene Graphs
- [六维位姿跟踪的漂移重定位](../papers/computer-vision.md#deng26a-inference) · STORM: Segment, Track, and Object Re-Localization from a Single Image
- [多概念遗忘的掩码合并](../papers/computer-vision.md#deng26i-inference) · Forget-It-All: Multi-Concept Machine Unlearning via Concept-Aware Neuron Masking

### 自然语言处理

- [排序与检索](../papers/nlp.md#agrawal26d-inference) · BlitzRank: Principled Zero-shot Ranking Agents with Tournament Graphs
- [文本水印](../papers/nlp.md#ai26b-inference) · PASA: A Principled Embedding-Space Watermarking Approach for LLM-Generated Text under Semantic-Invariant Attacks
- [句子级水印](../papers/nlp.md#an26a-inference) · IPMark: A Sentence-Level Watermark for LLMs with Hierarchical Personalization and Efficient Detection
- [全双工语音的异步检索](../papers/nlp.md#chien26b-inference) · MoshiRAG: Asynchronous Knowledge Retrieval for Full-Duplex Speech Language Models

### 强化学习

- [强化学习提前退出](../papers/reinforcement-learning.md#brosseit26a-inference) · Mind the Budget: Accelerating Deep Reinforcement Learning using Constrained Early Exit Neural Networks
- [模型强化学习搜索](../papers/reinforcement-learning.md#chang26a-inference) · The Surprising Difficulty of Search in Model-Based Reinforcement Learning
- [离线竞价的候选生成与价值筛选](../papers/reinforcement-learning.md#cui26h-inference) · DRIVE: Distributional and Retrieval-Augmented Bidding with Value Evaluation

### 机器人学

- [具身 Agent 感知](../papers/robotics.md#aissi26a-inference) · PRISM: Perception Reasoning Interleaved for Sequential Decision Making.
- [扩散预测控制](../papers/robotics.md#balim26a-inference) · Model-Based Diffusion Sampling for Predictive Control in Offline Decision Making
- [压缩空间运动规划](../papers/robotics.md#beyer26a-inference) · Motion Planning in Compressed Representation Spaces
- [移动操作站位](../papers/robotics.md#chai26a-inference) · N2M: Bridging Navigation and Manipulation by Learning Pose Preference from Rollout
- [概率场景图导航](../papers/robotics.md#chen26i-inference) · PSG-Nav: Probabilistic Scene Graph Navigation via Multiverse Decision Making
- [长程机器人轨迹采样](../papers/robotics.md#chen26co-inference) · Rethinking Instruction Drift as a Sampling Error: SNR-Aware Power Distributions for Long-Horizon Robotic Planning
- [多智能体协作的反事实规划](../papers/robotics.md#chi26b-inference) · EvoCF: Multi-Agent Collaboration via Agentic Memory-Driven Evolutionary Counterfactual Planning
- [VLA 不确定性调节感知与动作](../papers/robotics.md#choi26a-inference) · SCALE: Self-uncertainty Conditioned Adaptive Looking and Execution for Vision-Language-Action Models
- [机器人技能代码的局部重绑定](../papers/robotics.md#choi26c-inference) · Efficient Skill Grounding via Code Refactoring with Small Language Models
- [函数级 KV 缓存拼接与修补](../papers/robotics.md#chun26a-inference) · Functional Cache Grafting: Robust and Rapid Code-Policy Synthesis for Embodied Agents
- [导航中的熵驱动推理](../papers/robotics.md#ding26r-inference) · AdaNav: Adaptive Reasoning with Uncertainty for Vision-Language Navigation

### 多模态学习

- [视觉语言检索](../papers/multimodal.md#alshehri26a-inference) · Similarity Is Not Logic: Factored Inference for Dual-Encoder Vision-Language Models
- [流式语音工具调用](../papers/multimodal.md#arora26a-inference) · Stream RAG: Instant and Accurate Spoken Dialogue Systems with Streaming Tool Usage
- [视觉推理预算](../papers/multimodal.md#avogaro26a-inference) · SPARC: Separating Perception And Reasoning Circuits for Test-time Scaling of VLMs
- [文本到图像生成](../papers/multimodal.md#baek26c-inference) · Diagnosing and Correcting Concept Omission in Multimodal Diffusion Transformers
- [扩散对抗净化](../papers/multimodal.md#bai26b-inference) · Two Modalities Are Better Than One: Efficient Adversarial Purification via Multimodal Diffusion Models
- [三维生成引导](../papers/multimodal.md#bai26d-inference) · Let Language Constrain Geometry: Vision–Language Models as Semantic and Spatial Critics for 3D Generation
- [视觉语言推理控制](../papers/multimodal.md#bi26d-inference) · Does Reasoning Improve Seeing? Understanding When Vision-Language Models Benefit from Thinking
- [多模态上下文记忆](../papers/multimodal.md#chen26m-inference) · Task-Aware Structured Memory for Dynamic Multi-modal In-Context Learning
- [教学视频布局修正](../papers/multimodal.md#chen26bx-inference) · Code2Video: A Code-centric Paradigm for Educational Video Creation
- [注意力层对比解码](../papers/multimodal.md#chen26dx-inference) · Beyond Logits: Coherent Hallucination Mitigation via Attention Contrastive Decoding
- [双编码器视觉幻觉校正](../papers/multimodal.md#chen26dz-inference) · Beyond Blind Noising: Disentangled Visual Rectification for Hallucination Mitigation in MLLMs
- [图像生成的潜空间推理调度](../papers/multimodal.md#chen26fv-inference) · Show, Don’t Tell: Morphing Latent Reasoning into Image Generation
- [视觉语言模型注意力通路门控](../papers/multimodal.md#cheng26d-inference) · Mitigating Hallucinations in Large Vision-Language Models via Causal Route Gating
- [视觉词元删减后的注意力校准](../papers/multimodal.md#cho26b-inference) · Improving Visual Token Reduction via Rectifying Distortions for Efficient Multimodal LLM Inference
- [超高分遥感词元分区压缩](../papers/multimodal.md#dang26a-inference) · UHR-BAT: Budget-Aware Token Compression Vision-Language model for Ultra-High-Resolution Remote Sensing

### 机器学习基础与统计

- [未归一化分布采样](../papers/ml-foundations.md#blessing26a-inference) · Bridge Matching Sampler: Scalable Sampling via Generalized Fixed-Point Diffusion Matching
- [生成式模型遗忘](../papers/ml-foundations.md#block26a-inference) · Temper-Then-Tilt: Principled Unlearning for Generative Models through Tempering and Classifier Guidance
- [条件扩散采样](../papers/ml-foundations.md#castro-maci-as26a-inference) · Conditional Diffusion Sampling
- [贝叶斯逆问题采样](../papers/ml-foundations.md#chen26f-inference) · Proximal-IMH: Proximal Posterior Proposals for Independent Metropolis–Hastings with Approximate Operators
- [分块扩散注意力缓存](../papers/ml-foundations.md#chen26g-inference) · FlashBlock: Attention Caching for Efficient Long-Context Block Diffusion
- [摊销采样器与粒子采样互训](../papers/ml-foundations.md#choi26l-inference) · Reinforced Sequential Monte Carlo for Amortised Sampling
- [动态集成的路径聚合与早退](../papers/ml-foundations.md#colaco26a-inference) · Unifying Stacking and Cascading for Efficient Ensemble Inference
- [离散扩散的免训练 logit 引导](../papers/ml-foundations.md#dou26a-inference) · Plug-and-Play Guidance for Discrete Diffusion Models via Gradient-Informed Logit Correction

### 图学习与推荐

- [图模型测试时适应](../papers/graph-and-recommendation.md#ai26c-inference) · PromptDyG: Test-Time Prompt Adaptation on Dynamic Graphs
- [在线推荐校准](../papers/graph-and-recommendation.md#bisht26b-inference) · CARE: Adaptive Calibration for Reliable Recommendations

### 科学机器学习

- [大气生成模型](../papers/scientific-ml.md#aich26a-inference) · WIND: Weather Inverse Diffusion for Zero-Shot Atmospheric Modeling
- [数据同化](../papers/scientific-ml.md#andrae26a-inference) · DAISI: Data Assimilation with Inverse Sampling using Stochastic Interpolants
- [函数空间逆问题](../papers/scientific-ml.md#baker26a-inference) · Supervised Guidance Training for Infinite-Dimensional Diffusion Models
- [质谱到分子生成](../papers/scientific-ml.md#bohde26a-inference) · FRIGID: Scaling Diffusion-Based Molecular Generation from Mass Spectra at Training and Inference Time
- [蛋白结合物设计](../papers/scientific-ml.md#cao26c-inference) · Chamaileon: Cross-Context Binder Design with Contextualized Modeling and Mixed Sampling
- [对接预测梯度反演](../papers/scientific-ml.md#chen26bu-inference) · Towards Docking-oriented De Novo Ligand Design via Gradient Inversion
- [粗粒化玻尔兹曼重要性采样](../papers/scientific-ml.md#chen26gs-inference) · Coarse-Grained Boltzmann Generators
- [流行病模拟器的流图验证](../papers/scientific-ml.md#datta26a-inference) · Agentic Framework for Epidemiological Modeling
- [逆设计流的零锚定置信度](../papers/scientific-ml.md#de-campos26a-inference) · Generative Inverse Design with Abstention via Diagonal Flow Matching
- [重尾扩散桥的肠鸣音分离](../papers/scientific-ml.md#ding26a-inference) · Listening Through the Noise: Cauchy-Driven Diffusion Bridges for Robust Gastrointestinal Auscultation and Clinical Benchmarking
<!-- classification:end -->
