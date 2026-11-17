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

### 自然语言处理

- [排序与检索](../papers/nlp.md#agrawal26d-inference) · BlitzRank: Principled Zero-shot Ranking Agents with Tournament Graphs
- [文本水印](../papers/nlp.md#ai26b-inference) · PASA: A Principled Embedding-Space Watermarking Approach for LLM-Generated Text under Semantic-Invariant Attacks
- [句子级水印](../papers/nlp.md#an26a-inference) · IPMark: A Sentence-Level Watermark for LLMs with Hierarchical Personalization and Efficient Detection

### 强化学习

- [强化学习提前退出](../papers/reinforcement-learning.md#brosseit26a-inference) · Mind the Budget: Accelerating Deep Reinforcement Learning using Constrained Early Exit Neural Networks
- [模型强化学习搜索](../papers/reinforcement-learning.md#chang26a-inference) · The Surprising Difficulty of Search in Model-Based Reinforcement Learning

### 机器人学

- [具身 Agent 感知](../papers/robotics.md#aissi26a-inference) · PRISM: Perception Reasoning Interleaved for Sequential Decision Making.
- [扩散预测控制](../papers/robotics.md#balim26a-inference) · Model-Based Diffusion Sampling for Predictive Control in Offline Decision Making
- [压缩空间运动规划](../papers/robotics.md#beyer26a-inference) · Motion Planning in Compressed Representation Spaces
- [移动操作站位](../papers/robotics.md#chai26a-inference) · N2M: Bridging Navigation and Manipulation by Learning Pose Preference from Rollout
- [概率场景图导航](../papers/robotics.md#chen26i-inference) · PSG-Nav: Probabilistic Scene Graph Navigation via Multiverse Decision Making
- [长程机器人轨迹采样](../papers/robotics.md#chen26co-inference) · Rethinking Instruction Drift as a Sampling Error: SNR-Aware Power Distributions for Long-Horizon Robotic Planning

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

### 机器学习基础与统计

- [未归一化分布采样](../papers/ml-foundations.md#blessing26a-inference) · Bridge Matching Sampler: Scalable Sampling via Generalized Fixed-Point Diffusion Matching
- [生成式模型遗忘](../papers/ml-foundations.md#block26a-inference) · Temper-Then-Tilt: Principled Unlearning for Generative Models through Tempering and Classifier Guidance
- [条件扩散采样](../papers/ml-foundations.md#castro-maci-as26a-inference) · Conditional Diffusion Sampling
- [贝叶斯逆问题采样](../papers/ml-foundations.md#chen26f-inference) · Proximal-IMH: Proximal Posterior Proposals for Independent Metropolis–Hastings with Approximate Operators
- [分块扩散注意力缓存](../papers/ml-foundations.md#chen26g-inference) · FlashBlock: Attention Caching for Efficient Long-Context Block Diffusion

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
<!-- classification:end -->
