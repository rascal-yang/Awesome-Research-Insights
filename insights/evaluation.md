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

### 计算机视觉

- [视觉推理评测](../papers/computer-vision.md#acuaviva26a-evaluation) · Rethinking Visual Intelligence: Insights from Video Pretraining
- [分割模型诊断](../papers/computer-vision.md#ahmed26a-evaluation) · Med-SegLens: Latent-Level Model Diffing for Interpretable Medical Image Segmentation
- [扩散模型域外检测](../papers/computer-vision.md#alexis26a-evaluation) · GEPC: Group-Equivariant Posterior Consistency for Out-of-Distribution Detection in Diffusion Models
- [深伪防御评测](../papers/computer-vision.md#baek26e-evaluation) · Proactive Defense Benchmark against Deepfake Generation
- [扩散模型概念遗忘](../papers/computer-vision.md#braun26b-evaluation) · Erased but Not Forgotten: How Backdoors Compromise Concept Erasure

### 自然语言处理

- [分词器评测](../papers/nlp.md#altintas26a-evaluation) · TokSuite: Measuring the Impact of Tokenizer Choice on Language Model Behavior
- [音频表征评测](../papers/nlp.md#basha26a-evaluation) · VocSim A Training-free Benchmark for Zero-shot Content Identity in Single-source Audio

### 强化学习

- [防御强化学习奖励](../papers/reinforcement-learning.md#bates26a-evaluation) · Beyond Rewards in RL for Cyber Defence

### 机器人学

- [机器人轨迹安全](../papers/robotics.md#bai26e-evaluation) · SafeLab: An Interactive High-Fidelity Benchmark for Embodied Safety in Scientific Robotics
- [柔性线状物体操作](../papers/robotics.md#cao26w-evaluation) · DLO-Lab: Benchmarking Deformable Linear Object Manipulations with Differentiable Physics

### 多模态学习

- [视觉语言安全评测](../papers/multimodal.md#azulay26a-evaluation) · Jailbreaking Vision-Language Models Through the Visual Modality
- [文档 Agent 评测](../papers/multimodal.md#borchmann26a-evaluation) · Strategic Navigation or Stochastic Search? How Agents and Humans Reason Over Document Collections
- [视觉语言模型量化](../papers/multimodal.md#bouguerra26a-evaluation) · Less Precise Can Be More Reliable: A Systematic Evaluation of Quantization’s Impact on VLMs Beyond Accuracy
- [图像感知评测](../papers/multimodal.md#cao26i-evaluation) · UniPercept: Towards Unified Perceptual-Level Image Understanding across Aesthetics, Quality, Structure, and Texture
- [音视频生成评测](../papers/multimodal.md#cao26v-evaluation) · T2AV-Compass: Towards Unified Evaluation for Text-to-Audio-Video Generation

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

### 图学习与推荐

- [图模型隐私评测](../papers/graph-and-recommendation.md#agbaje26a-evaluation) · Revisiting Asymmetries in Black-box Link Stealing against Graph Neural Networks
- [图模型迁移](../papers/graph-and-recommendation.md#akula26a-evaluation) · Same Graph Cross-Task Transfer in GNNs: Protocols and Predictors

### 科学机器学习

- [时间序列预测评测](../papers/scientific-ml.md#ahamed26a-evaluation) · TFRBench: A Reasoning Benchmark for Evaluating Forecasting Systems
- [格密码机器学习分析](../papers/scientific-ml.md#alfarano26a-evaluation) · Improving ML Attacks on LWE with Data Repetition and Stepwise Regression
- [恶意软件谱系重建](../papers/scientific-ml.md#amalan26a-evaluation) · MalTree: Tracing Malware Evolution from Embeddings at Scale
- [生存模型评测](../papers/scientific-ml.md#bahrini26a-evaluation) · When Can We Trust Survival Model Evaluation ?
- [CAD 操作评测](../papers/scientific-ml.md#bai26a-evaluation) · Op-CAD: Benchmarking and Investigating Operation-oriented CAD Generation
- [流体控制强化学习](../papers/scientific-ml.md#becktepe26a-evaluation) · Plug-and-Play Benchmarking of Reinforcement Learning Algorithms for Large-Scale Flow Control
- [仿真 Agent 成本评测](../papers/scientific-ml.md#cao26g-evaluation) · SimulCost: A Cost-Aware Benchmark and Toolkit for Automating Physics Simulations with LLMs
- [科学标注行为克隆](../papers/scientific-ml.md#chandok26a-evaluation) · A Systematic Study of Behavioral Cloning for Scientific Data Annotation
<!-- classification:end -->
