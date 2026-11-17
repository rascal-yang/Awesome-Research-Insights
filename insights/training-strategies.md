# 训练策略

[首页](../README.md) · [参与贡献](../CONTRIBUTING.md) · [English](../en/insights/training-strategies.md)

训练日程、课程学习与多阶段训练。

<!-- classification:start -->
## 按研究领域浏览

### 大语言模型

- [参数高效微调](../papers/llm.md#adepu26a-training-strategies) · Fine-Tuning of Transformer models with Frames
- [激活干预](../papers/llm.md#adila26a-training-strategies) · Weight Updates as Activation Shifts: A Principled Framework for Steering
- [离散扩散加速](../papers/llm.md#amin26a-training-strategies) · Consistent Diffusion Language Models
- [递归潜空间推理](../papers/llm.md#asadulaev26a-training-strategies) · Latent Reasoning in TRMs is Secretly a Policy Improvement Operator
- [黑盒模型适配](../papers/llm.md#asawa26a-training-strategies) · How to Train Your Advisor: Steering Black-Box LLMs with Advisor Models
- [激活控制](../papers/llm.md#bao26b-training-strategies) · Towards Steering without Sacrifice: Principled Training of Steering Vectors for Prompt-only Interventions
- [技能持续学习](../papers/llm.md#berthon26a-training-strategies) · Skill Neologisms: Towards Skill-based Continual Learning
- [测试时语言模型学习](../papers/llm.md#bian26b-training-strategies) · Future-Gain Guided Test-Time Learning for Large Language Models
- [Transformer 到 SSM 蒸馏](../papers/llm.md#bick26a-training-strategies) · Retrieval-Aware Distillation for Transformer-SSM Hybrids
- [持续预训练](../papers/llm.md#borodin26a-training-strategies) · Diffract: Spectral View of LLM Domain Adaptation
- [推理后训练课程](../papers/llm.md#bu26a-training-strategies) · Provable Sample Efficiency of Curriculum Post-Training for Transformer Reasoning
- [渐进式模型训练](../papers/llm.md#bu26c-training-strategies) · Scaling depth capacity via zero/one-layer model expansion
- [微调泛化干预](../papers/llm.md#casademunt26a-training-strategies) · Steering Out-of-Distribution Generalization with Concept Ablation Fine-Tuning
- [监督微调与强化学习协同](../papers/llm.md#chen26an-training-strategies) · Beyond Two-Stage Training: Cooperative SFT and RL for LLM Reasoning
- [知识纠错与置信校准](../papers/llm.md#chen26ap-training-strategies) · Know More, Know Clearer: A Meta-Cognitive Framework for Knowledge Augmentation in Large Language Models
- [4 位训练权重振荡](../papers/llm.md#chen26cl-training-strategies) · TetraJet-v2: Accurate NVFP4 Training for Large Language Models with Oscillation Suppression and Outlier Control
- [后训练的近似在策略数据](../papers/llm.md#chen26do-training-strategies) · Retaining by Doing: The Role of On-Policy Data in Mitigating Forgetting
- [拒答引导的激活对抗训练](../papers/llm.md#chen26em-training-strategies) · Steering Beyond the Support: Adversarial Training on Unsupervised Jailbroken Activation Simulation

### 计算机视觉

- [少步生成蒸馏](../papers/computer-vision.md#bai26n-training-strategies) · Optimizing Few-Step Generation with Adaptive Matching Distillation
- [长视频生成](../papers/computer-vision.md#cai26h-training-strategies) · Mode Seeking meets Mean Seeking for Fast Long Video Generation
- [动态参数高效微调](../papers/computer-vision.md#cao26o-training-strategies) · Beyond Static Allocation: Dynamic Sensitivity-Aware Fine-Tuning for Vision Transformers
- [端侧文生图蒸馏](../papers/computer-vision.md#chavhan26a-training-strategies) · NanoFLUX: Distillation-Driven Compression of Large Text-to-Image Generation Models for Mobile Devices
- [视图一致的三维 VAE 稀疏训练](../papers/computer-vision.md#chen26cn-training-strategies) · Focusing: View-Consistent Sparse Voxels for Efficient 3D VAE Training
- [高斯泼溅的瞬态区域筛除](../papers/computer-vision.md#chen26dm-training-strategies) · 3DGS-HPC: Distractor-free 3D Gaussian Splatting with Hybrid Patch-wise Classification
- [长上下文视频蒸馏](../papers/computer-vision.md#chen26eu-training-strategies) · Context Forcing: Consistent Autoregressive Video Generation with Long Context

### 机器人学

- [终身轨迹规划](../papers/robotics.md#chen26d-training-strategies) · NOMAD: Lifelong Trajectory Planning via Non-Parametric Bayesian Memory-Adaptive Diffusion Experts

### 多模态学习

- [多模态上下文学习](../papers/multimodal.md#alipour-talemi26a-training-strategies) · Hyper-ICL: Attention Calibration with Hyperbolic Anchor Distillation for Multimodal In-Context Learning
- [多模态微调](../papers/multimodal.md#asadollahzadeh26a-training-strategies) · TRACER: Persistent Regularization for Robust Multimodal Finetuning
- [视觉数据与符号绑定](../papers/multimodal.md#buzeta26a-training-strategies) · Seeing to Generalize: How Visual Data Corrects Binding Shortcuts
- [视觉语言蒸馏与量化](../papers/multimodal.md#chen26am-training-strategies) · Gated Relational Alignment via Confidence-based Distillation for Efficient VLMs

### 机器学习基础与统计

- [权重合并](../papers/ml-foundations.md#abdollahpoorrostam26a-training-strategies) · MODEL SOUPS NEED ONLY ONE INGREDIENT
- [机器遗忘](../papers/ml-foundations.md#almudevar26b-training-strategies) · Representation Unlearning: Forgetting through Information Compression
- [联邦模型水印](../papers/ml-foundations.md#bakr26a-training-strategies) · Collaborative Threshold Watermarking
- [持续模型路由](../papers/ml-foundations.md#bell26a-training-strategies) · Continual Model Routing in Evolving Model Hubs
- [联邦 LoRA](../papers/ml-foundations.md#bian26e-training-strategies) · FedTreeLoRA: Reconciling Statistical and Functional Heterogeneity in Federated LoRA Fine-Tuning
- [状态空间模型训练](../papers/ml-foundations.md#brady26a-training-strategies) · Efficient Learning of Deep State Space Models via Importance Smoothing
- [递归去噪训练](../papers/ml-foundations.md#cameron26a-training-strategies) · One Step Forward and K Steps Back: Better Reasoning with Denoising Recursion Models
- [异构联邦学习](../papers/ml-foundations.md#cao26a-training-strategies) · Required Spine Optional Limbs: Heterogeneous Federated Learning via Backbone-sharing and Activation-guided Selection
- [离散扩散采样](../papers/ml-foundations.md#carter26a-training-strategies) · Discrete Diffusion Samplers and Bridges: Off-Policy Algorithms and Applications in Latent Spaces
- [首脉冲时间编码](../papers/ml-foundations.md#che26a-training-strategies) · Efficiently Training Time-to-First-Spike Spiking Neural Networks from Scratch
- [生成流的先验](../papers/ml-foundations.md#chemseddine26a-training-strategies) · Adapting Noise to Data: Generative Flows from Learned 1D Processes
- [测试时因果结构学习](../papers/ml-foundations.md#chen26t-training-strategies) · Test-Time Learning of Causal Structure from Interventional Data
- [存内计算权重抗扰训练](../papers/ml-foundations.md#chen26bq-training-strategies) · Diversity-aware Weight Perturbation Promotes Robust Adaptation
- [多层联邦个性化建模](../papers/ml-foundations.md#chen26cp-training-strategies) · Personalized Additive Modeling for Multi-level Federated Learning
- [离线 GFlowNet 的边奖励引导](../papers/ml-foundations.md#chen26ej-training-strategies) · Beyond the Proxy: Trajectory-Distilled Guidance for Offline GFlowNet Training
- [多方向异步流水线训练](../papers/ml-foundations.md#chen26ff-training-strategies) · AMDP: Asynchronous Multi-Directional Pipeline Parallelism for Large-Scale Models Training

### 图学习与推荐

- [超图鲁棒训练](../papers/graph-and-recommendation.md#arafat26a-training-strategies) · Adversarial Attacks and Robust Training for Hypergraph Neural Networks
- [图组合优化迁移](../papers/graph-and-recommendation.md#canturk26a-training-strategies) · Can Computational Reducibility Lead to Transferable Models for Graph Combinatorial Optimization?
- [图基础模型的消息微调](../papers/graph-and-recommendation.md#chen26cz-training-strategies) · Message Tuning Outshines Graph Prompt Tuning: A Prismatic Space Perspective

### 科学机器学习

- [变构蛋白结合物生成](../papers/scientific-ml.md#cao26r-training-strategies) · TD3B: Transition-Directed Discrete Diffusion for Allosteric Binder Generation
- [层级仿真推断](../papers/scientific-ml.md#charles26a-training-strategies) · Tokenised Flow Matching for Hierarchical Simulation Based Inference
- [长时天气预测](../papers/scientific-ml.md#chen26ao-training-strategies) · EMFormer: Efficient Multi-Scale Transformer for Accumulative Context Weather Forecasting
<!-- classification:end -->
