# 模块

[首页](../README.md) · [参与贡献](../CONTRIBUTING.md) · [English](../en/insights/modules.md)

可复用组件与局部连接方式。

<!-- classification:start -->
## 按研究领域浏览

[大语言模型](#by-llm) · [计算机视觉](#by-computer-vision) · [自然语言处理](#by-nlp) · [机器人学](#by-robotics) · [多模态学习](#by-multimodal) · [机器学习基础与统计](#by-ml-foundations) · [图学习与推荐](#by-graph-and-recommendation) · [科学机器学习](#by-scientific-ml)

<a id="by-llm"></a>

### 大语言模型

- [线性注意力记忆](../conferences/icml-2026/cards/0301-0400.md#bonnet26a-modules) · Learning to Remember, Learn, and Forget in Attention-Based Models
- [归一化替换](../conferences/icml-2026/cards/0301-0400.md#byun26a-modules) · Bounded Hyperbolic Tangent: A Stable and Efficient Alternative to Pre-Layer Normalization in Large Language Models
- [深层 Transformer 归一化](../conferences/icml-2026/cards/0401-0500.md#chao26b-modules) · SpanNorm: Reconciling Training Stability and Performance in Deep Transformers
- [上下文转 LoRA](../conferences/icml-2026/cards/0401-0500.md#charakorn26a-modules) · Doc-to-LoRA: Learning to Instantly Internalize Contexts
- [MoE 持续学习](../conferences/icml-2026/cards/0501-0600.md#chen26aw-modules) · Multi-Head Attention as a Source of Catastrophic Forgetting in MoE Transformers
- [线性投影后的局部归一化](../conferences/icml-2026/cards/0501-0600.md#chen26dj-modules) · SimpleGPT: Improving GPT via A Simple Normalization Strategy
- [独立价值空间的桥接词元](../conferences/icml-2026/cards/0501-0600.md#chen26dw-modules) · Toward Stable Value Alignment: Introducing Independent Modules for Consistent Value Guidance
- [逐词元全局注意力路由](../conferences/icml-2026/cards/0701-0800.md#choudhary26a-modules) · Learning When to Attend: Conditional Memory Access for Long-Context LLMs
- [连分式因果 token 混合](../conferences/icml-2026/cards/0801-0900.md#dhurandhar26a-modules) · CoFrGeNet: Continued Fraction Architectures for Language Generation
- [基于专家权重谱的免训练路由](../conferences/icml-2026/cards/0901-1000.md#do26a-modules) · Eigenvectors of Experts are Training-free Non-collapsing Routers
- [键相似度预调节注意力](../conferences/icml-2026/cards/1001-1100.md#duvvuri26a-modules) · LUCID: Attention with Preconditioned Representations
- [逐解码步的潜空间经验检索](../conferences/icml-2026/cards/1101-1200.md#feng26i-modules) · ExpWeaver: LLM Agents Learn from Experience via Latent RAG
- [MoE 专家输出的有向图聚合](../conferences/icml-2026/cards/1101-1200.md#feng26v-modules) · DAG-MoE: From Simple Mixture to Structural Aggregation in Mixture-of-Experts
- [Softplus 注意力的两阶段重加权](../conferences/icml-2026/cards/1201-1300.md#gao26y-modules) · Softplus Attention with Re-weighting Boosts Length Extrapolation in Large Language Models
- [稀疏 entmax 的直方图阈值初始化](../conferences/icml-2026/cards/1301-1400.md#goncalves26a-modules) · AdaSplash-2: Faster Differentiable Sparse Attention
- [把重遮盖位置的高熵表征留给下轮去噪](../conferences/icml-2026/cards/1601-1700.md#hu26as-modules) · Residual Context Diffusion Language Models
- [在自回归推理中保存耗散的连续隐状态](../conferences/icml-2026/cards/1601-1700.md#huang26m-modules) · Thinking in Flow: A Dissipative Stabilization Operator for Robust Autoregressive Reasoning
- [以分块偏置校准抑制压缩误差累积](../conferences/icml-2026/cards/1701-1800.md#huang26q-modules) · Representation Drift Compensation: A Near-Zero Inference Cost Enhancement for LLM Decomposition
- [让超网络按文本调节前馈门控斜率](../conferences/icml-2026/cards/1801-1900.md#ji26i-modules) · Learn-to-learn on Arbitrary Textual Conditioning: A Hypernetwork-Driven Meta-gated LLM
- [用反馈锁定 MoE 动态路由的平均预算](../conferences/icml-2026/cards/1901-2000.md#jin26f-modules) · DTop-p MoE: Sparsity-Controlled Dynamic Top-p MoE for Foundation Model Pre-training

<a id="by-computer-vision"></a>

### 计算机视觉

- [主动视觉分辨率](../conferences/icml-2026/cards/0201-0300.md#blauch26a-modules) · FOVI: A biologically-inspired foveated interface for deep vision models
- [小型视觉 Transformer](../conferences/icml-2026/cards/0301-0400.md#candogan26a-modules) · Spatial Priors via Space Filling Curves for Small and Limited Data Vision Transformers
- [分层三维语义分割](../conferences/icml-2026/cards/0301-0400.md#cao26j-modules) · Multi-Label Learning with Contrastive Cluster Self-Supervision for 3D Hierarchical Semantic Segmentation
- [轻量视频超分](../conferences/icml-2026/cards/0301-0400.md#cao26n-modules) · LiteVSR: Lightweight Adaptation of Frozen Diffusion Transformers for Video Super-Resolution
- [结构化图像生成](../conferences/icml-2026/cards/0401-0500.md#cao26ab-modules) · StructMAR: Structure-Aware Masked Autoregression for Explicit Layout Alignment in Text-to-Image Generation
- [视频超分的小波编码前端](../conferences/icml-2026/cards/0501-0600.md#chen26ce-modules) · WEVSR: Video Diffusion Generators for Real-World Video Super-Resolution with Wavelet-Enhanced VAE Encoder
- [ViT 多层注意力探针](../conferences/icml-2026/cards/0701-0800.md#ciernik26a-modules) · Attentive Multi-Layer Fusion for Vision Transformers
- [视觉概念瓶颈的原型证据](../conferences/icml-2026/cards/0701-0800.md#colamonaco26a-modules) · Prototype-Grounded Concept Models for Verifiable Concept Alignment
- [卷积权重与特征的双空间扰动](../conferences/icml-2026/cards/0801-0900.md#dhar26a-modules) · Does a Hybrid Space-Aware Randomized Defense Improve Empirical and Certified Adversarial Robustness?
- [偏振物理先验的透明物体深度](../conferences/icml-2026/cards/0901-1000.md#dong26i-modules) · PolarDepth: Monocular Transparent Object Depth from Polar-Physics Priors
- [红外可见光融合的卷积分支折叠](../conferences/icml-2026/cards/0901-1000.md#duan26a-modules) · MobileFusion: Mobile-Friendly Infrared and Visible Image Fusion via Structural Re-parameterization
- [人体视频的非对称身份注意力](../conferences/icml-2026/cards/1401-1500.md#guo26ad-modules) · WildActor: Unconstrained Identity-Preserving Video Generation
- [超分辨率的跨尺度词元前缀](../conferences/icml-2026/cards/1401-1500.md#hadji26a-modules) · Hierarchical Image Tokenization for Multi-Scale Image Super Resolution
- [用三维表面坐标连接跨姿态参考](../conferences/icml-2026/cards/1401-1500.md#han26ab-modules) · Pose-ICL: 3D-Aware In-Context Learning for Pose-Controllable Subject Customization
- [用局部退化控制分块采样与回写](../conferences/icml-2026/cards/1501-1600.md#he26an-modules) · Bend the Basics: Degradation-Aware Deformable Tokenization for All-in-One Image Restoration
- [把修正点击变成连通误差区](../conferences/icml-2026/cards/1601-1700.md#hu26au-modules) · Interactive Segmentation with Elaborate Focus Prior
- [用逐元素门控降低脉冲注意力通信](../conferences/icml-2026/cards/1901-2000.md#jiang26an-modules) · Efficient Transformer Attention for SNNs via Hadamard Simplification
- [从局部频谱提取风格并路由检测适配词元](../conferences/icml-2026/cards/1901-2000.md#jiang26ay-modules) · SCoA: Revisiting Domain Generalized Object Detection with Style-Conditioned Adaptation
- <a id="widen-the-student-distillation-interface"></a><a id="distillation-interface-design"></a>[只加宽学生模型的蒸馏接口](../conferences/icml-2026/cards/4401-4500.md#tian26k-modules) · From Per-Image Low-Rank to Encoding Mismatch: Rethinking Feature Distillation in Vision Transformers

<a id="by-nlp"></a>

### 自然语言处理

- [Agent 词表适配](../conferences/icml-2026/cards/0201-0300.md#bian26c-modules) · AgentVocab: Structure-Aware Vocabulary Adaptation for Efficient LLM Agents

<a id="by-robotics"></a>

### 机器人学

- [视觉动作策略的连续网格采样](../conferences/icml-2026/cards/1101-1200.md#feng26x-modules) · See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model
- [视觉动作模型的通道相关门控](../conferences/icml-2026/cards/1101-1200.md#fu26x-modules) · StableVLA: Towards Robust Vision-Language-Action Models without Extra Data
- [精密操作的点云傅里叶编码](../conferences/icml-2026/cards/1401-1500.md#gyenes26a-modules) · Fourier Features Let Agents Learn High Precision Policies with Imitation Learning
- [用行为检索和上下文间隔约束动作](../conferences/icml-2026/cards/1801-1900.md#jang26c-modules) · RA-VLA: Retrieval-Augmented VLA for Test-Time Adaptation
- [按多时域动作预测的共识决定执行长度](../conferences/icml-2026/cards/1901-2000.md#jing26f-modules) · Mixture of Horizons in Action Chunking
- <a id="instruction-prefixes-for-causal-visual-grounding"></a><a id="multimodal-token-layout"></a>[用指令前缀让视觉表征感知任务](../papers/reconvla.md#reconvla-modules) · ReconVLA

<a id="by-multimodal"></a>

### 多模态学习

- [细粒度视觉定位](../conferences/icml-2026/cards/0201-0300.md#barrios26a-modules) · MoDA: Modulation Adapter for Fine-Grained Visual Understanding in Instructional MLLMs
- [非对称 RGB-D 特征融合](../conferences/icml-2026/cards/0501-0600.md#chen26ch-modules) · Hamiltonian Asymmetric Fusion: One-Way Safe Directed Refinement under Modality Imbalance
- [缺失模态的结构化提示](../conferences/icml-2026/cards/0501-0600.md#chen26dv-modules) · SPR: A Structured Prompt Refinement Network for Modality Missing
- [音视频非对称 token 压缩](../conferences/icml-2026/cards/0901-1000.md#ding26e-modules) · OmniSIFT: Modality-Asymmetric Token Compression for Efficient Omni-modal Large Language Models
- [视听稀疏采样的 RoPE 抗混叠](../conferences/icml-2026/cards/1301-1400.md#gong26g-modules) · EchoingPixels: Aliasing-Resistant Joint Token Reduction for Audio-Visual LLMs
- [用位置编码绑定人物与音色](../conferences/icml-2026/cards/1401-1500.md#guo26af-modules) · DreamID-Omni: Unified Framework for Controllable Human-Centric Audio-Video Generation
- [放松传输边缘约束以减少不可靠视图的影响](../conferences/icml-2026/cards/1401-1500.md#han26aa-modules) · Robust Multi-View Fusion via Prototype-Anchored Unbalanced Optimal Transport
- [分开抽取实例和文本角色来推断假设编辑](../conferences/icml-2026/cards/1401-1500.md#he26b-modules) · Reasoning to Edit: Hypothetical Instruction-Based Image Editing with Visual Reasoning
- [将追踪专家与模态专家分工](../conferences/icml-2026/cards/1501-1600.md#hong26g-modules) · Unified Multimodal Visual Tracking with Dual Mixture-of-Experts
- [让推理过程主动发起稀疏查证](../conferences/icml-2026/cards/1601-1700.md#hu26ba-modules) · TVI-CoT: Text-Visual Interleaved Chain-of-Thought Reasoning for Multimodal Understanding

<a id="by-ml-foundations"></a>

### 机器学习基础与统计

- [注意力参数化](../conferences/icml-2026/cards/0101-0200.md#bae26d-modules) · Affine-Scaled Attention: Towards Flexible and Stable Transformer Attention
- [克罗内克适配器](../conferences/icml-2026/cards/0101-0200.md#bai26l-modules) · Diving into Kronecker Adapters: Component Design Matters
- [稠密模型转 MoE](../conferences/icml-2026/cards/0201-0300.md#bamba26a-modules) · DOT-MoE: Differentiable Optimal Transport for MoEfication
- [连续深度模型](../conferences/icml-2026/cards/0201-0300.md#banerjee26b-modules) · Efficient Continuous-Depth Modeling with GRU Equivalents
- [循环模型长程记忆](../conferences/icml-2026/cards/0201-0300.md#behrouz26a-modules) · Memory Caching: RNNs with Growing Memory
- [测试时记忆更新](../conferences/icml-2026/cards/0201-0300.md#behrouz26b-modules) · ATLAS: Learning to Optimally Memorize the Context at Test Time
- [时间序列预测](../conferences/icml-2026/cards/0301-0400.md#brachet26a-modules) · Time Series Forecasting Through the Lens of Dynamics
- [低功耗循环网络](../conferences/icml-2026/cards/0301-0400.md#brandoit26a-modules) · Improving the Performance and Learning Stability of Parallelizable RNNs Designed for Ultra-Low Power Applications
- [多实例部分标签](../conferences/icml-2026/cards/0401-0500.md#cao26af-modules) · Enhanced Multi-Instance Partial Label Learning via Average Gradient Outer Product
- [自监督投影头](../conferences/icml-2026/cards/0401-0500.md#chaudhry26a-modules) · The Geometry of Projection Heads: Conditioning, Invariance, and Collapse
- [相关矩阵流形全连接层](../conferences/icml-2026/cards/0601-0700.md#chen26fb-modules) · Riemannian Networks over Full-Rank Correlation Matrices
- [时间序列的后续轨迹检索](../conferences/icml-2026/cards/0701-0800.md#chong26c-modules) · Beyond Extrapolation: Knowledge Utilization Paradigm with Bidirectional Inspiration for Time Series Forecasting
- [无需旧样本的持续学习适配器](../conferences/icml-2026/cards/0701-0800.md#cosentino26a-modules) · PLATE: Plasticity-Tunable Efficient Adapters for Geometry-Aware Continual Learning
- [词元与专家的联合稀疏路由](../conferences/icml-2026/cards/0901-1000.md#do26b-modules) · Rethinking Sparse Mixture of Experts from a Unified Perspective
- [GPU 友好的块置换随机投影](../conferences/icml-2026/cards/1001-1100.md#dwaraknath26a-modules) · FlashSketch: Sketch-Kernel Co-Design for Fast Sparse Sketching on GPUs
- [可微的逐样本特征选择](../conferences/icml-2026/cards/1001-1100.md#ellinson26a-modules) · Hide&Seek: Learning to Explain in an End-to-End Differentiable Network
- [局部坐标对齐的向量丛注意力](../conferences/icml-2026/cards/1001-1100.md#fang26q-modules) · VBA: Vector Bundle Attention for Intrinsically Geometric Representation Learning
- [跨数据集时序谱结构对齐](../conferences/icml-2026/cards/1001-1100.md#fei26b-modules) · Olivia: Harmonizing Time Series Foundation Models with Power Spectral Density
- [时序分类的定长词元生成](../conferences/icml-2026/cards/1101-1200.md#feofanov26a-modules) · Mantis: Lightweight Foundation Model for Time Series Classification
- [显著性变速的多项式记忆](../conferences/icml-2026/cards/1201-1300.md#goffinet26a-modules) · HiPPO Zoo: Explicit Memory Mechanisms for Interpretable State Space Models
- [位置与内容分离的极坐标编码](../conferences/icml-2026/cards/1301-1400.md#gopalakrishnan26a-modules) · Decoupling The "What" and "Where" With Polar Coordinate Positional Embedding
- [时序预测的可变长模式词元](../conferences/icml-2026/cards/1301-1400.md#gotz26a-modules) · Byte Pair Encoding for Efficient Time Series Forecasting
- [ANN 到 SNN 的递推时序编码](../conferences/icml-2026/cards/1301-1400.md#gu26d-modules) · Temporal Weighted Encoding: Towards Maximal-Capacity Spike Coding for ANN–SNN Conversion
- [高维表格的相关特征分组压缩](../conferences/icml-2026/cards/1401-1500.md#habib26a-modules) · GOTabPFN: From Feature Ordering to Compact Tokenization for Tabular Foundation Models on High-Dimensional Data
- [用双曲几何实现层级记忆检索](../conferences/icml-2026/cards/1401-1500.md#hao26d-modules) · Hyperbolic Associative Memory Networks
- [用高阶随机草图补足线性原型注意力](../conferences/icml-2026/cards/1701-1800.md#huang26ao-modules) · PLASH: Provably Linear-Time Attention with Selective Higher-Order Feature Sketching
- [只在稀疏路由决策边界引入连续过渡](../conferences/icml-2026/cards/1701-1800.md#huu26a-modules) · Geometric and Stochastic Analysis of Discontinuities in Sparse Mixture-of-Experts
- [从输入块预估累加部分和的量化尺度](../conferences/icml-2026/cards/1701-1800.md#hwang26a-modules) · PsumQuant: In-line Post-training Partial Sum Quantizer for Energy Efficient NPU Inference
- [把目标偏好写进边注意力](../conferences/icml-2026/cards/1801-1900.md#jia26l-modules) · Preference-Modulated Structural Attention for Multi-Objective Combinatorial Optimization
- [在中间层用互斥正交子空间分离变因](../conferences/icml-2026/cards/2001-2100.md#jung26g-modules) · Layer-Centric Factors of Variation Disentanglement for Task- and Model-Agnostic Generalization

<a id="by-graph-and-recommendation"></a>

### 图学习与推荐

- [图卷积](../conferences/icml-2026/cards/0101-0200.md#bai26i-modules) · GI-GCN: Global Interacted Graph Convolutional Networks via Dominant Sets for Graph Classification
- [图神经网络表达力](../conferences/icml-2026/cards/0201-0300.md#barcelo26a-modules) · Message Passing on the Edge: Towards Scalable and Expressive GNNs
- [兼顾图拓扑与因果顺序的注意力](../conferences/icml-2026/cards/0601-0700.md#chen26gm-modules) · Weaving Graph over Tokens: Contextualizing Structured Sequences for LLMs
- [异配图消息的自成分消除](../conferences/icml-2026/cards/0701-0800.md#choi26d-modules) · Gauge-Equivariant Graph Networks via Self-Interference Cancellation
- [有向带属性图的酉卷积](../conferences/icml-2026/cards/1101-1200.md#fesser26b-modules) · Unitary Convolutions for Message-passing and Positional Encodings on Directed Graphs

<a id="by-scientific-ml"></a>

### 科学机器学习

- [网格动力学平滑](../conferences/icml-2026/cards/0201-0300.md#berman26d-modules) · Smoothness Errors in Dynamics Models and How to Avoid Them
- [医学视觉定位](../conferences/icml-2026/cards/0401-0500.md#chang26b-modules) · MedSIGHT: Towards Grounded Visual Comprehension in Medical Large Vision-Language Models
- [口袋与配体双向融合](../conferences/icml-2026/cards/0501-0600.md#chen26bw-modules) · TSMGen: Target-Specific Molecule Generation via Higher-Order Structural Dependencies and Context-Aware Bidirectional Fusion
- [脑电信号的复数频谱细化](../conferences/icml-2026/cards/0601-0700.md#chen26fr-modules) · PCRNet: Phase-aware Complex Refinement Network for EEG-based Auditory Attention Decoding
- [原子间势的自适应贝叶斯失活](../conferences/icml-2026/cards/0701-0800.md#coscia26a-modules) · BLIPs: Bayesian Learned Interatomic Potentials
- [用虚拟三跳路径编码蛋白交互先验](../conferences/icml-2026/cards/1201-1300.md#gao26ap-modules) · Learning the Interaction Prior for Protein-Protein Interaction Prediction: A Model-Agnostic Approach
<!-- classification:end -->
