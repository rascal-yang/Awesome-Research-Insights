# 数据策略

[首页](../README.md) · [参与贡献](../CONTRIBUTING.md) · [English](../en/insights/data-strategies.md)

数据筛选、标注、增强与采样。

<!-- classification:start -->
## 按研究领域浏览

[大语言模型](#by-llm) · [计算机视觉](#by-computer-vision) · [自然语言处理](#by-nlp) · [强化学习](#by-reinforcement-learning) · [机器人学](#by-robotics) · [多模态学习](#by-multimodal) · [机器学习基础与统计](#by-ml-foundations) · [图学习与推荐](#by-graph-and-recommendation) · [科学机器学习](#by-scientific-ml)

<a id="by-llm"></a>

### 大语言模型

- [数据选择](../conferences/icml-2026/cards/0001-0100.md#aden-ali26a-data-strategies) · Subliminal Effects in Your Data: A General Mechanism via Log-Linearity
- [改写稳定性](../conferences/icml-2026/cards/0101-0200.md#arraf26a-data-strategies) · Learning Rewrite-Invariant Reasoning with Targeted Alternation Training
- [奖励投机](../conferences/icml-2026/cards/0101-0200.md#azarbal26a-data-strategies) · Recontextualization Mitigates Specification Gaming Without Modifying the Specification
- [事实预训练](../conferences/icml-2026/cards/0201-0300.md#behnia26a-data-strategies) · Facts in Stats: Impacts of Pretraining Diversity on Language Model Generalization
- [交替由学生写风格和教师补解法](../conferences/icml-2026/cards/1701-1800.md#huang26bq-data-strategies) · How to Fine-Tune a Reasoning Model? A Teacher–Student Cooperation Framework to Synthesize Student-Consistent SFT Data
- [用同一教师对齐前后差异筛选监督](../conferences/icml-2026/cards/1901-2000.md#jiang26j-data-strategies) · Contrastive Weak-to-Strong Generalization
- [用扰动模型的前缀损失挑长推理样本](../conferences/icml-2026/cards/1901-2000.md#jin26o-data-strategies) · Reasoning Quality Emerges Early: Data Curation for Reasoning Models
- [按边际安全收益选择最小增强集](../conferences/icml-2026/cards/2001-2100.md#kao26a-data-strategies) · Submodular Optimization for Minimal Augmentation in Robust Language Model Alignment
- [用模型自己的解掩顺序生成训练掩码](../conferences/icml-2026/cards/2101-2200.md#kim26o-data-strategies) · Stop Training for the Worst: Progressive Unmasking Accelerates Masked Diffusion Training
- [容量感知的数据配比定律](../conferences/icml-2026/cards/2401-2500.md#li26av-data-strategies) · Capacity-Aware Mixture Law Enables Efficient LLM Data Optimization
- [瞄准稀疏字典中的数据空缺](../conferences/icml-2026/cards/2601-2700.md#li26hl-data-strategies) · Less is Enough: Synthesizing Diverse Data in LLM Feature Space with Sparse Autoencoders
- [用合并成分模型评估预训练数据配比](../conferences/icml-2026/cards/2601-2700.md#li26jt-data-strategies) · Decouple Searching from Training: Scaling Data Mixing via Model Merging for Large Language Model Pre-training
- [联合调节微调数据预算与推理难度](../conferences/icml-2026/cards/2701-2800.md#liu26m-data-strategies) · Data Difficulty and the Generalization–Extrapolation Tradeoff in LLM Fine-Tuning
- [由检索头干预识别高价值推理步骤](../conferences/icml-2026/cards/2801-2900.md#liu26bd-data-strategies) · AIR: Post-training Data Selection for Reasoning via Attention Head Influence
- [把题内均匀抽样当作代码数据筛选对照](../conferences/icml-2026/cards/2801-2900.md#liu26bz-data-strategies) · Random Selection Reveals Implicit Knowledge Consensus in Code Generation
- [可执行推理题族合成](../conferences/icml-2026/cards/2901-3000.md#liu26ew-data-strategies) · Scaling the Scaling Logic: Agentic Meta-Synthesis of Logic Reasoning
- [从开放文本构造可核验强化学习题](../conferences/icml-2026/cards/3001-3100.md#lu26a-data-strategies) · Golden Goose: A Simple Trick to Synthesize Unlimited RLVR Tasks from Unverifiable Internet Text
- [用目标条件的 token 保留率给微调样本排序](../conferences/icml-2026/cards/3001-3100.md#luo26m-data-strategies) · TarGATE: Target-Aware Data Selection via Token-Attenuation Gates
- [用 Actor–Critic 动态选择预训练域权重](../conferences/icml-2026/cards/3101-3200.md#ma26i-data-strategies) · AC-ODM: Actor–Critic Online Data Mixing for Sample-Efficient LLM Pretraining
- [补少量实体恒等句让自回归模型学反向关联](../conferences/icml-2026/cards/3101-3200.md#ma26o-data-strategies) · Breaking the Reversal Curse in Autoregressive Language Models via Identity Bridge
- [主动偏好对选择](../conferences/icml-2026/cards/3201-3300.md#melikidze26a-data-strategies) · ActiveUltraFeedback: Efficient Preference Data Generation using Active Learning
- [在 LoRA 验证梯度子空间筛选指令数据](../conferences/icml-2026/cards/3301-3400.md#min26a-data-strategies) · GIST: Targeted Data Selection for Instruction Tuning via Coupled Optimization Geometry
- [用均衡语义域支持预训练数据配比](../conferences/icml-2026/cards/3301-3400.md#min26e-data-strategies) · GEM: Geometric Entropy Mixing for Optimal LLM Data Curation
- [用效用相同的偏好对压制伪特征](../conferences/icml-2026/cards/3301-3400.md#moya26a-data-strategies) · Spurious Correlation Learning in Preference Optimization: Mechanisms, Consequences, and Mitigation via Tie Training
- [区分预训练过滤收益与高质量分布匹配](../conferences/icml-2026/cards/3401-3500.md#nait-saada26a-data-strategies) · Removing Noise, not Finding Gold: Quality Filtering for Large-Scale Pretraining
- [提示响应互信息](../conferences/icml-2026/cards/3401-3500.md#nam26b-data-strategies) · Maximizing Mutual Information Between Prompt and Response Improves LLM Performance With No Additional Data
- [小模型蒸馏保留本机推理表达](../conferences/icml-2026/cards/3701-3800.md#qian26l-data-strategies) · The Quality-Utility Paradox: Why High-Reward Data Impairs Small Model Mathematical Reasoning
- [参考动作引导拒绝采样](../conferences/icml-2026/cards/4201-4300.md#sun26h-data-strategies) · KBQA-R1: Reinforcing Large Language Models for Knowledge Base Question Answering
- [boundary-aware-evidence-curriculum](../conferences/icml-2026/cards/4201-4300.md#sun26p-data-strategies) · Rethinking the Reranker: Boundary-Aware Evidence Selection for Robust Retrieval-Augmented Generation
- [以学生真进步奖励课程生成](../conferences/icml-2026/cards/4301-4400.md#sundaram26a-data-strategies) · Teaching Models to Teach Themselves: Reasoning at the Edge of Learnability
- [sae-ood-selection](../conferences/icml-2026/cards/4301-4400.md#suresh26a-data-strategies) · At the Edge of Understanding: Sparse Autoencoders Trace The Limits of Transformer Generalization
- [knowledge-injection-scaling](../conferences/icml-2026/cards/4301-4400.md#tang26y-data-strategies) · SPA: A Simple but Tough-to-Beat Baseline for Knowledge Injection
- [first-error-local-repair](../conferences/icml-2026/cards/4301-4400.md#tang26aa-data-strategies) · CALM Before the STORM: Unlocking Native Reasoning for Optimization Modeling
- [surprisal-boundary-knowledge-editing](../conferences/icml-2026/cards/4401-4500.md#tian26e-data-strategies) · AnyEdit++: Adaptive Long-Form Knowledge Editing via Bayesian Surprise
- [预训练AI叙事改变行为先验](../conferences/icml-2026/cards/4401-4500.md#tice26a-data-strategies) · Alignment Pretraining: AI Discourse Causes Self-Fulfilling (Mis)alignment
- [hidden-state-trust-filtering](../conferences/icml-2026/cards/4501-4600.md#uzunoglu26a-data-strategies) · Trust Functions: Near-Lossless Weak-to-Strong Generalization by Learning When to Trust the Weak Teacher
- [DARTS: Distribution-Aware Active Rollout Trajectory Shaping for Accelerating LLM Reinforcement Learning](../conferences/icml-2026/cards/4601-4700.md#wang26w-data-strategies) · DARTS: Distribution-Aware Active Rollout Trajectory Shaping for Accelerating LLM Reinforcement Learning
- [非均匀原子技能采样](../conferences/icml-2026/cards/4601-4700.md#wang26ak-data-strategies) · The Power of Power Law: Asymmetry Enables Compositional Reasoning
- [输出梯度核选择辅助数据](../conferences/icml-2026/cards/4701-4800.md#wang26eq-data-strategies) · Mining Useful General Data for Low-Resource Domain Adaptation
- [注意力片段引导生成回放](../conferences/icml-2026/cards/4701-4800.md#wang26go-data-strategies) · Towards Understanding Continual Factual Knowledge Acquisition of Language Models: From Theory to Algorithm
- [模型合并代理数据混合比例](../conferences/icml-2026/cards/4701-4800.md#wang26hi-data-strategies) · MergeMix: Optimizing Mid-Training Data Mixtures via Learnable Model Merging
- [目标神经元激活集合筛选数据](../conferences/icml-2026/cards/4801-4900.md#wang26hk-data-strategies) · Target-Oriented Pretraining Data Selection via Neuron-Activated Graph
- [前缀支持的交错披露](../conferences/icml-2026/cards/4901-5000.md#wei26i-data-strategies) · When to Think, When to Speak: Learning Disclosure Policies for LLM Reasoning
- [错误反馈与不可解状态的轨迹增强](../conferences/icml-2026/cards/5001-5100.md#wu26al-data-strategies) · Can Agents Generalize to the Open World? Unveiling the Fragility of Static Training in Tool Use
- [按非对称loss影响排batch顺序](../conferences/icml-2026/cards/5201-5300.md#xu26p-data-strategies) · D$^3$: Dynamic Directional Graph-Constrained Data Scheduling for LLM Training
- [按基础能力边缘而非饱和任务分配RL数据](../conferences/icml-2026/cards/5801-5900.md#zhang26en-data-strategies) · On the Interplay of Pre-Training, Mid-Training, and RL on Reasoning Language Models
- [用reward波动和entropy门控UCB集中group rollouts](../conferences/icml-2026/cards/5901-6000.md#zhang26gc-data-strategies) · Resource-Efficient Reinforcement for Reasoning Large Language Models via Dynamic One-Shot Policy Refinement
- [按奖励偏好方向共识筛rollout](../conferences/icml-2026/cards/6101-6200.md#zhou26ad-data-strategies) · GeoAlign: Geometric Rollout Curation for Robust LLM Reinforcement Learning
- [在偏好聚合前检查同标注者的一致性与测量有效性](../conferences/icml-2026/cards/6301-6400.md#ghafouri26a-data-strategies) · Position: RLHF May Not Reflect Genuine Preferences

<a id="by-computer-vision"></a>

### 计算机视觉

- [图像训练数据保护](../conferences/icml-2026/cards/0301-0400.md#cai26m-data-strategies) · FUSE: Full-spectrum Unlearnable Examples via Spectral Equalization
- [扩散数据蒸馏的集合耦合引导](../conferences/icml-2026/cards/1101-1200.md#gan26d-data-strategies) · Set-Coupled Guidance: Set-Level Coordination in Diffusion-Based Dataset Distillation
- [沿正常特征低方差方向造难负例](../conferences/icml-2026/cards/2001-2100.md#karzanov26a-data-strategies) · Geometrically Constrained Outlier Synthesis
- [用带符号熵轨迹识别错误图像标签](../conferences/icml-2026/cards/2601-2700.md#li26ju-data-strategies) · On Revisiting Entropy for Identifying Mislabeled Images
- [单目数据立体反遮挡](../conferences/icml-2026/cards/3001-3100.md#lu26k-data-strategies) · Geometric Reciprocity: Unlocking Self-Supervision for Stereoscopic Video Generation
- [object-conditioned-foveation](../conferences/icml-2026/cards/4401-4500.md#traub26a-data-strategies) · Looking Locally: Object-Centric Vision Transformers as Foundation Models for Efficient Segmentation
- [按频谱和扩散时刻学习选patch](../conferences/icml-2026/cards/4601-4700.md#wang26bq-data-strategies) · FaPS: A General and Fast Training Method for Diffusion Models
- [按尺度原型修正VAR logits](../conferences/icml-2026/cards/4601-4700.md#wang26co-data-strategies) · ProtoVAR: Efficient Dataset Distillation via Prototype-Guided Visual Autoregressive Modeling
- [按本地与全局预测缺口补数据](../conferences/icml-2026/cards/4701-4800.md#wang26ga-data-strategies) · FedPDG: Prediction Discrepancy–Guided Data Generation for Heterogeneous Federated Learning
- [片间一致性约束的拼图回放](../conferences/icml-2026/cards/4701-4800.md#wang26hc-data-strategies) · Beyond Buffer Limits: Energy-Based Data Reassembly for Continual Learning
- [运动加权梯度的数据归因](../conferences/icml-2026/cards/5001-5100.md#wu26aq-data-strategies) · Motion Attribution for Video Generation
- [蒸馏图像的扩散后恢复](../conferences/icml-2026/cards/5101-5200.md#xia26g-data-strategies) · DIVER: Diving Deeper into Distilled Data via Expressive Semantic Recovery
- [分开控制合成场景密度与边界细节](../conferences/icml-2026/cards/5701-5800.md#zhang26be-data-strategies) · What Makes Synthetic Data Effective in Image Segmentation
- [混合点云预训练中的编码与缺失模态控制](../conferences/icml-2026/cards/5901-6000.md#zhang26gs-data-strategies) · Utonia: Toward One Encoder for All Point Clouds
- [低置信伪标签的预测位移筛选](../conferences/icml-2026/cards/6001-6100.md#zhao26w-data-strategies) · Rethinking Low-Confidence Pseudo Labels: Influence-Aware Semi-Supervised Fine-Tuning for Hyperspectral Change Detection
- [按评测先验审计3D pruning信号](../conferences/icml-2026/cards/6001-6100.md#zhao26ao-data-strategies) · Exploring 3D Dataset Pruning
- [累计不确定性筛防御训练子集](../conferences/icml-2026/cards/6001-6100.md#zhao26ba-data-strategies) · Anti-Backdoor Coreset Selection via Cumulative Entropy

<a id="by-nlp"></a>

### 自然语言处理

- [差分隐私合成数据](../conferences/icml-2026/cards/0201-0300.md#banayeeanzade26a-data-strategies) · EPSVec: Efficient and Private Synthetic Data Generation via Dataset Vectors
- [对比学习的困难负例组批](../conferences/icml-2026/cards/0901-1000.md#dutta26a-data-strategies) · HOBIT: Hardness Optimized Batch Sampling for InfoNCE Training
- [固定生成机制再干预任务频次](../conferences/icml-2026/cards/4101-4200.md#snaebjarnarson26a-data-strategies) · Causally Evaluating the Learnability of Formal Language Tasks
- [保持句法的预训练语义消融](../conferences/icml-2026/cards/4901-5000.md#winston26a-data-strategies) · Learning syntax without semantics: Disentangled tiny language models

<a id="by-reinforcement-learning"></a>

### 强化学习

- [零样本离线强化学习](../conferences/icml-2026/cards/0201-0300.md#bendib26a-data-strategies) · Improving Zero-Shot Offline RL via Behavioral Task Sampling
- [跨域离线强化学习的软筛选](../conferences/icml-2026/cards/0601-0700.md#chen26gd-data-strategies) · Transport or Discard: Robust Unbalanced Optimal Transport for Cross-Domain Policy Adaptation
- [数学搜索课程的中间难度实例](../conferences/icml-2026/cards/1001-1100.md#fagan26a-data-strategies) · The Two-Hump Problem: Bridging the Difficulty Gap in Mathematical Reinforcement Learning
- [世界模型的主动探测数据](../conferences/icml-2026/cards/1101-1200.md#feng26aa-data-strategies) · Learning Task-Sufficient World Models by Synergizing Agentic Exploration and Structured Modeling
- [以同一状态拼接来路和去路](../conferences/icml-2026/cards/3701-3800.md#qing26a-data-strategies) · BiTrajDiff: Bidirectional Trajectory Generation with Diffusion Models for Offline Reinforcement Learning
- [用可核验轨迹捷径增加离线转移](../conferences/icml-2026/cards/3901-4000.md#schmahling26a-data-strategies) · Trajectory-Level Data Augmentation for Offline Reinforcement Learning
- [Reward-Preserving Counterfactual State Editing for Offline Reinforcement Learning](../conferences/icml-2026/cards/4601-4700.md#wang26s-data-strategies) · Reward-Preserving Counterfactual State Editing for Offline Reinforcement Learning
- [按扩展后的populationexploitability选择新policy](../conferences/icml-2026/cards/5901-6000.md#zhang26ho-data-strategies) · Global Policy-Space Response Oracles for Two-Player Zero-Sum Games

<a id="by-robotics"></a>

### 机器人学

- [固定预算下的机器人示范分配](../conferences/icml-2026/cards/0501-0600.md#chen26cy-data-strategies) · Escaping the Diversity Trap in Robotic Manipulation via Anchor-Centric Adaptation
- [以仿真重放跨机器人改写同一示范](../conferences/icml-2026/cards/1801-1900.md#ji26g-data-strategies) · OXE-AugE: A Large-Scale Robot Augmentation of OXE for Scaling Cross-Embodiment Policy Learning
- [分别模拟深度像素失效和值误差](../conferences/icml-2026/cards/2601-2700.md#liang26n-data-strategies) · PRISM: Learning Realistic Depth via Physics-Grounded Noise Disentanglement with Semantic-Geometric Collaboration
- [geometry-confidence-next-view](../conferences/icml-2026/cards/4401-4500.md#tsai26a-data-strategies) · Creat3r: Confidence Reaggregation for Exploration-aware Active 3D Reconstruction
- [优化整个序列的前缀差异度](../conferences/icml-2026/cards/4501-4600.md#van-huffel26a-data-strategies) · Neural Low-Discrepancy Sequences
- [按被动移动轨迹评估传感器部署](../conferences/icml-2026/cards/5701-5800.md#zhang26b-data-strategies) · BALLAST: Bayesian Active Learning with Look-ahead Amendment for Sea-drifter Trajectories under Spatio-Temporal Vector Fields
- [示范锚定区域的困难与非冗余选样](../conferences/icml-2026/cards/6201-6300.md#zhu26s-data-strategies) · Making Learner Weakness Actionable for Learning from Demonstration with Novice Teachers

<a id="by-multimodal"></a>

### 多模态学习

- [多模态数据蒸馏](../conferences/icml-2026/cards/0301-0400.md#bo26b-data-strategies) · Efficient Multi-modal Dataset Distillation via Analytic Parameter Matching
- [图像到 CAD 的几何反馈扩增](../conferences/icml-2026/cards/1201-1300.md#giannone26a-data-strategies) · GIFT: Bootstrapping Image-to-CAD Program Synthesis via Geometric Feedback
- [用视觉交叉熵收益分配训练预算](../conferences/icml-2026/cards/2301-2400.md#lee26m-data-strategies) · Focusing Where Vision Matters: Selective Training for Large Vision Language Models via Visual Information Gain
- [过程奖励训练的轨迹筛选](../conferences/icml-2026/cards/2401-2500.md#li26bm-data-strategies) · Training Data Efficiency in Multimodal Process Reward Models
- [按系统、图像与用户输入分解注意力识别投毒](../conferences/icml-2026/cards/2801-2900.md#liu26ag-data-strategies) · TCAP: Tri-Component Attention Profiling for Unsupervised Backdoor Detection in MLLM Fine-Tuning
- [任务分布一致性与相关性联合剪枝](../conferences/icml-2026/cards/4601-4700.md#wang26cz-data-strategies) · ConsMSA: Semantic Distribution Consistency Learning for Multimodal Sentiment Analysis
- [局部教师全图学生](../conferences/icml-2026/cards/4901-5000.md#wei26j-data-strategies) · Zooming without Zooming: Region-to-Image Distillation for Fine-Grained Multimodal Perception
- [用相关与无关遮挡区分证据依赖](../conferences/icml-2026/cards/5201-5300.md#xu26x-data-strategies) · DeFacto: Counterfactual Thinking with Images for Enforcing Evidence-Grounded and Faithful Reasoning
- [标签多样性驱动空间关系泛化](../conferences/icml-2026/cards/5301-5400.md#yamamoto26a-data-strategies) · Left–Right Symmetry Breaking in CLIP-Style Vision-Language Models Trained on Synthetic Spatial-Relation Data
- [按相对不确定性的平衡点选模态对齐样本](../conferences/icml-2026/cards/5901-6000.md#zhang26fw-data-strategies) · Beyond Fixed Biases: Decoding the Role of Reasoning Uncertainty in MLLM Modality Conflicts

<a id="by-ml-foundations"></a>

### 机器学习基础与统计

- [数据洗牌](../conferences/icml-2026/cards/0001-0100.md#afshani26a-data-strategies) · The benefits of full data shuffle, now with optimal I/O cost: $k$-wise independence and matrix transposition to the rescue
- [主动因果发现](../conferences/icml-2026/cards/0301-0400.md#bonilla26a-data-strategies) · Causal Preference Elicitation
- [稀疏多类标注聚合](../conferences/icml-2026/cards/0401-0500.md#chen26ac-data-strategies) · Let the Prototype Guide You: Robust Aggregation of Sparse Multi-Class Annotations via Annotator Prototype Learning
- [训练样本选择的二部图覆盖](../conferences/icml-2026/cards/0701-0800.md#chi26d-data-strategies) · Unifying and Optimizing Data Values for Selection via Sequential Decision-Making
- [低秩数据子集的残差采样](../conferences/icml-2026/cards/0701-0800.md#cohen-addad26a-data-strategies) · Active Learning with Low-Rank Structure for Data Selection
- [元学习选样的低信噪比](../conferences/icml-2026/cards/0901-1000.md#du26u-data-strategies) · On the Difficulty of Learning a Meta-network for Training Data Selection
- [合成递归训练的多偏好筛选](../conferences/icml-2026/cards/1001-1100.md#falahati26a-data-strategies) · Curated Synthetic Data Doesn’t Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferences
- [治疗效应估计的主动随机试验](../conferences/icml-2026/cards/1201-1300.md#gao26z-data-strategies) · Budgeted Active Experimentation for Treatment Effect Estimation from Observational and Randomized Data
- [用全局模型的相对信心在客户端重分配标签](../conferences/icml-2026/cards/1601-1700.md#hu26ao-data-strategies) · FedReLa: Imbalanced Federated Learning via Re-Labeling
- [在上下文中按条件互信息决定补测哪个特征](../conferences/icml-2026/cards/2101-2200.md#kobayashi26a-data-strategies) · Learning-To-Measure: In-Context Active Feature Acquisition
- [先复用加密边缘统计再发布私有合成数据](../conferences/icml-2026/cards/2201-2300.md#kumar26e-data-strategies) · $\textttFHAIM$: Fully Homomorphic AIM for Private Tabular Synthetic Data Generation
- [用单调学习曲线和预期缺口决定采集量](../conferences/icml-2026/cards/2301-2400.md#lee26af-data-strategies) · Monotonic Variational Gaussian Process for Efficient Data Collection
- [用小波最优输运边际影响给时序片段估值](../conferences/icml-2026/cards/2801-2900.md#liu26dh-data-strategies) · TimeLAVA: Learning-Agnostic Valuation for Time Series Data
- [用等权群体重心蒸馏数据](../conferences/icml-2026/cards/3301-3400.md#moslemi26a-data-strategies) · Fair Dataset Distillation via Cross-Group Barycenter Alignment
- [递归生成中的局部筛选偏差](../conferences/icml-2026/cards/3701-3800.md#qiao26c-data-strategies) · When Sample Selection Bias Precipitates Model Collapse
- [保留残余噪声标签的训练数据迭代](../conferences/icml-2026/cards/3801-3900.md#rodriguez-munoz26a-data-strategies) · Ambient Dataloops: Generative Models for Dataset Refinement
- [联邦列主元与局部样本选择](../conferences/icml-2026/cards/4301-4400.md#tang26r-data-strategies) · Federated Data and Feature Selection by Generalized CUR Decomposition
- [nonlinear-component-data-valuation](../conferences/icml-2026/cards/4401-4500.md#tian26c-data-strategies) · Is Data Shapley Not Better than Random in Data Selection? Ask NASH
- [按公开分布定向混合的隐私采样](../conferences/icml-2026/cards/4501-4600.md#vithana26a-data-strategies) · Optimal Domain-Aware Privacy Mechanisms for Synthetic Data Generation
- [按来源方向几何筛选共享表示数据](../conferences/icml-2026/cards/4701-4800.md#wang26ft-data-strategies) · On the Power of Source Screening for Learning Shared Feature Extractors
- [反演结构响应以调整训练权重](../conferences/icml-2026/cards/4701-4800.md#wang26fw-data-strategies) · Patterning: The Dual of Interpretability
- [连续函数参数化的轨迹蒸馏](../conferences/icml-2026/cards/5001-5100.md#wu26ca-data-strategies) · CHESS: Chebyshev Spectral Synthesis for Trajectory Condensation
- [loss与entropy方差配权的在线选样](../conferences/icml-2026/cards/5401-5500.md#yang26bq-data-strategies) · Data Agent: Learning to Select Data via End-to-End Dynamic Optimization
- [用票数margin后验分配重复标注预算](../conferences/icml-2026/cards/5801-5900.md#zhang26bv-data-strategies) · MA$^3$S: Model-Agnostic Active Annotation Strategy for Crowdsourcing
- [用在线utility而非合成保真度决定注入](../conferences/icml-2026/cards/5901-6000.md#zhang26hn-data-strategies) · Active Tabular Augmentation via Policy-Guided Diffusion Inpainting

<a id="by-graph-and-recommendation"></a>

### 图学习与推荐

- [图基础模型的合成预训练先验](../conferences/icml-2026/cards/1001-1100.md#eremeev26a-data-strategies) · GraphPFN: A Prior-Data Fitted Graph Foundation Model
- [按重建支持分层遮蔽](../conferences/icml-2026/cards/4301-4400.md#tang26l-data-strategies) · Reconstruction Outcomes Look Similar but Processes Differ: Improving Context Consistency and Coverage in Graph Masked Auto-Encoder
- [由目标梯度反推负采样](../conferences/icml-2026/cards/4601-4700.md#wang26db-data-strategies) · Negative Sampling From the Ground Up: A Redesign for Recommendations
- [节点超边异质度共同控制mask与传播](../conferences/icml-2026/cards/5401-5500.md#yao26e-data-strategies) · H$^2$CL: Heterogeneity-Aware Hypergraph Contrastive Learning for Robust Representation Learning
- [结构签名约束的少数类合成](../conferences/icml-2026/cards/5501-5600.md#yin26d-data-strategies) · Rel-MOSS: Towards Imbalanced Relational Deep Learning on Relational Databases

<a id="by-scientific-ml"></a>

### 科学机器学习

- [离线预计算短式改写以去重训练](../conferences/icml-2026/cards/3901-4000.md#saegert26a-data-strategies) · Breaking the Simplification Bottleneck in Amortized Neural Symbolic Regression
<!-- classification:end -->

<!-- conference-classification:start -->
## CoRL 2026

- [Diagnosing Compositional Generalization in Sequential Robot Tasks](../conferences/corl-2026/cards.md#paper-gqfyim5djy)
- [FAKTUAL](../conferences/corl-2026/cards.md#paper-tscng5wcwn)
- [π0.7](../conferences/corl-2026/cards.md#paper-5xkfwwrw0v)
- [RoboPocket](../conferences/corl-2026/cards.md#paper-thg2jwuii6)
- [PAKT](../conferences/corl-2026/cards.md#paper-2vdrocnuih)
- [AIDA-OWMM](../conferences/corl-2026/cards.md#paper-4m7c3psa78)
- [SimHum](../conferences/corl-2026/cards.md#paper-cvpjguuatq)
- [SIDO](../conferences/corl-2026/cards.md#paper-mqly5j6pnd)
- [SuperSuit: An Isomorphic Bimodal Interface for Scalable Mobile Manipulation](../conferences/corl-2026/cards.md#paper-penaq22jh1)
- [AmodalBox: Automated 3D Bounding Box Annotation under Partial Visibility](../conferences/corl-2026/cards.md#paper-0o1c1xxn1m)
- [Worlds in One Demo: A Synthetic Data Engine for Learning Open-World Mobile Manipulation](../conferences/corl-2026/cards.md#paper-w1x9mho93e)
- [Generative Flow on Symbolic Abstractions for Embodiment Capability Discovery](../conferences/corl-2026/cards.md#paper-weyfps89nj)
- [EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data](../conferences/corl-2026/cards.md#paper-wf4x17al2r)
- [FACTR 2: Learning External Force Sensing for Commodity Robot Arms Improves Policy Learning](../conferences/corl-2026/cards.md#paper-03zmmfktxk)
- [Scale Up Strategically: Learning Compositional Generalization via Bias-Aware Evaluation and Data Collection for Robotic Manipulation](../conferences/corl-2026/cards.md#paper-quvj7qbql6)
- [Counterfactual Video Generation Enables Scalable Humanoid Loco-Manipulation](../conferences/corl-2026/cards.md#paper-uzalccyrvl)
- [τ0-WM: A Unified Video-Action World Model for Robotic Manipulation](../conferences/corl-2026/cards.md#paper-qvol1xoutn)
- [Enhancing Robotic Control Robustness through Generative Visual Model](../conferences/corl-2026/cards.md#paper-e5lvpa2glx)
- [PlayWorld: Learning Robot World Models from Autonomous Play Data](../conferences/corl-2026/cards.md#paper-hatezfmdn5)
- [Training Controllable World Models via Action Influence Maximization](../conferences/corl-2026/cards.md#paper-oocwc3dn5d)
- [VISTA: Vision-Grounded and Physics-Validated Adaptation of UMI data for VLA Training](../conferences/corl-2026/cards.md#paper-xagvjptxtr)
- [Human-like autonomy emerges from self-play and a pinch of human data](../conferences/corl-2026/cards.md#paper-lovzujpkxn)
- [SPARC: Reliable Spatial Annotations from Robot Demonstrations at Scale](../conferences/corl-2026/cards.md#paper-gx5xey9ade)
- [GUILD: Guided Iterative Data Collection for Imitation Learning](../conferences/corl-2026/cards.md#paper-6txmwx1wih)
- [ATHENA: Accelerated Multi-Task Heterogeneous Influence Functions for Robot Data Curation](../conferences/corl-2026/cards.md#paper-dpgz9kssgo)
- [What is the Better Curriculum: Controller-Shaped Grasping Behavior for Contact Force-Sensitive Manipulation](../conferences/corl-2026/cards.md#paper-f3dic5djnz)
- [SSR: Scaling Surefooted and Symmetric Humanoid Traversal Toward the Open World](../conferences/corl-2026/cards.md#paper-4it3fcnny2)

## NeurIPS 2026

- [3D-VITAL: Visibility-aware Identity Training from Artificial Liftings of 3D Reconstruction model for Cross-View Object Re-Identification](../conferences/neurips-2026/cards.md#paper-150244)
- [A Bitter Lesson for Data Filtering](../conferences/neurips-2026/cards.md#paper-155947)
- [AffordSim: A Scalable Data Generator and Benchmark for Affordance-Aware Robotic Manipulation](../conferences/neurips-2026/cards.md#paper-139222)
- [Are Easier or Harder Examples Better? Rethinking Data Selection for Reward Models and Preference Optimization](../conferences/neurips-2026/cards.md#paper-151585)
- [Beyond Isolation: Neighbor-Consistent Data Pruning for Multivariate Time Series Forecasting](../conferences/neurips-2026/cards-0002.md#paper-154771)
- [Bilevel Optimization of Synthetic Trajectories for Multi-Turn LLM Fine-Tuning](../conferences/neurips-2026/cards-0002.md#paper-155173)
- [BLADE: Scalable Bi-level Adaptive Data Selection for LLM Training](../conferences/neurips-2026/cards-0002.md#paper-152234)
- [Blocked Gibbs meets Diffusion Transformers: Unsupervised Learning for Constraint Optimization](../conferences/neurips-2026/cards-0002.md#paper-148271)
- [Boundary Mass in Feature Space as a Label-Budget Diagnostic for Representations](../conferences/neurips-2026/cards-0002.md#paper-149689)
- [Breaking Noise Shortcuts in Self-Supervised Learning via Noise-Aligned View Generation](../conferences/neurips-2026/cards-0002.md#paper-153415)
- [CausalMix: Data Mixture as Causal Inference for Language Model Training](../conferences/neurips-2026/cards-0003.md#paper-154762)
- [Characterizing the Generalization Error of Random Feature Regression with Arbitrary Data-Augmentation](../conferences/neurips-2026/cards-0003.md#paper-153550)
- [CircuitSeer: Mining High-Quality Data by Probing Mathematical Reasoning Circuits in LLMs](../conferences/neurips-2026/cards-0003.md#paper-152316)
- [Class-Mixed Diffusion Augmentation for Shortcut-Breaking in Continual Learning](../conferences/neurips-2026/cards-0003.md#paper-154098)
- [Closed-Form Linear-Probe Dataset Distillation for Pre-trained Vision Models](../conferences/neurips-2026/cards-0003.md#paper-153458)
- [Compute-optimal data scaling for neural surrogates via multi-fidelity training](../conferences/neurips-2026/cards-0003.md#paper-151246)
- [Consilience for Verifier-Free Test-Time Scaling](../conferences/neurips-2026/cards-0003.md#paper-153648)
- [Control-Augmented Autoregressive Diffusion for Data Assimilation](../conferences/neurips-2026/cards-0003.md#paper-152028)
- [CWAGraph: Retrieving What Was Never Explicitly Identified in Graph-Based RAG](../conferences/neurips-2026/cards-0003.md#paper-149212)
- [Data Density Scaling Laws for Image Self-Distillation](../conferences/neurips-2026/cards-0003.md#paper-150410)
- [DeformGen: Dynamics-Based Topology Augmentation for Deformable Manipulation Policy Learning](../conferences/neurips-2026/cards-0004.md#paper-149334)
- [DeltaPrompts: Escaping the Zero-Delta Trap in Multimodal Distillation](../conferences/neurips-2026/cards-0004.md#paper-153494)
- [DISCOVER: Online Variance-Guided Data Discovery for Budgeted Multimodal GRPO](../conferences/neurips-2026/cards-0004.md#paper-155862)
- [Distribution Shift in Missing Data Imputation: A Risk-Based Perspective and Importance-Weighted Correction under MAR](../conferences/neurips-2026/cards-0004.md#paper-155709)
- [Does Mixed Label Imbalance Matter to Minority Collapse in Imbalanced Learning?](../conferences/neurips-2026/cards-0004.md#paper-156069)
- [Does the Question Really Matter? Training-Free Data Selection for Vision-Language SFT](../conferences/neurips-2026/cards-0004.md#paper-150111)
- [DUDS: Dual-stage Data Selection for Efficient Reinforcement Learning with Verifiable Rewards](../conferences/neurips-2026/cards-0004.md#paper-151136)
- [Efficient and Simple Data Mixing All The Time](../conferences/neurips-2026/cards-0004.md#paper-154977)
- [Efficient Dataset Distillation for Pre-Trained Self-Supervised Models via Statistical Flow Matching](../conferences/neurips-2026/cards-0004.md#paper-155616)
- [Epiplexity Guided Data Selection and Generation for Out-of-Distribution Generalization](../conferences/neurips-2026/cards-0005.md#paper-153698)
- [EvoOptiGraph: Weakness-Driven Coevolution via Graph-Based Structural Generation for Optimization Modeling](../conferences/neurips-2026/cards-0005.md#paper-155640)
- [FASTER: Value-Guided Sampling for Fast RL](../conferences/neurips-2026/cards-0005.md#paper-149442)
- [Fault Tolerant Coresets](../conferences/neurips-2026/cards-0005.md#paper-153584)
- [Finetuning with Sampling: Make SFT Generalize, Not Forget](../conferences/neurips-2026/cards-0005.md#paper-150118)
- [Firefly: Illuminating Verified Real-world Tool Call Data Generation](../conferences/neurips-2026/cards-0005.md#paper-155698)
- [Flux: Online, Fine-Grained Data Scheduling for Training Machine Learning Interatomic Potentials](../conferences/neurips-2026/cards-0005.md#paper-151170)
- [Forgetting to Improve: Principled Data Removal in Active Learning](../conferences/neurips-2026/cards-0005.md#paper-148637)
- [FreeAct: Demonstration-Free Robot Adaptation via Action-Grounded Generated Videos](../conferences/neurips-2026/cards-0005.md#paper-148622)
- [From Collapse to Improvement:  Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources](../conferences/neurips-2026/cards-0005.md#paper-148326)
- [From Persistence to Survival: Hypothesis Testing, Effect Sizes and Vectorisation for Topological Features](../conferences/neurips-2026/cards-0006.md#paper-153632)
- [From Sample to Subset Construction: Coverage-Aware Curation of Robot Demonstrations](../conferences/neurips-2026/cards-0006.md#paper-150964)
- [From Weeks to Hours: Fast and Principled SFT Curation for LLM](../conferences/neurips-2026/cards-0006.md#paper-155549)
- [Generative Active Learning via Bayesian Acquisition for Improving the Efficiency of Synthetic Data](../conferences/neurips-2026/cards-0006.md#paper-149816)
- [Geometric Gain Graph: Zero-Token Graph Construction for Multi-Hop RAG](../conferences/neurips-2026/cards-0006.md#paper-151572)
- [Gradient Boosted Trees for Retrieval-Augmented Generation](../conferences/neurips-2026/cards-0006.md#paper-153272)
- [GradTrack: Detecting Noisy Labels via Temporal Trajectories of Class-wise Gradient Misalignment](../conferences/neurips-2026/cards-0006.md#paper-148547)
- [Guiding Data Allocation for Robust Subpopulation Generalization](../conferences/neurips-2026/cards-0006.md#paper-153167)
- [Hallucination in World Models is Predictable and Preventable](../conferences/neurips-2026/cards-0006.md#paper-155605)
- [High Performance Differentially Private Fine-Tuning using Dataset Distillation](../conferences/neurips-2026/cards-0006.md#paper-153009)
- [HomeFlow: A Data Flywheel for Smart Home Agent Training with Verifiable Simulation](../conferences/neurips-2026/cards-0006.md#paper-153647)
- [HopChain: Multi-Hop Data Synthesis for Generalizable Vision-Language Reasoning](../conferences/neurips-2026/cards-0006.md#paper-149865)
- [How Data Scales in Agentic Reinforcement Learning: Laws and Synthesis Strategies](../conferences/neurips-2026/cards-0006.md#paper-155951)
- [How to Instruct Your Robot: Dense Language Annotations Power Robot Policy Learning](../conferences/neurips-2026/cards-0006.md#paper-150612)
- [I Have a Stream: Making Self-Supervised Learning Work on Continuous Video](../conferences/neurips-2026/cards-0007.md#paper-151662)
- [Improved Leverage Score Sampling for Constrained Active Linear Regression](../conferences/neurips-2026/cards-0007.md#paper-155618)
- [In-context learning to predict critical transitions in dynamical systems](../conferences/neurips-2026/cards-0007.md#paper-155891)
- [InfCLIP: Unified Data Valuation for CLIP Pretraining via Influence-Inspired Scoring](../conferences/neurips-2026/cards-0007.md#paper-150869)
- [Intent2CAD: How Semantic-Parametric Supervision Shapes Text-to-CAD Generation](../conferences/neurips-2026/cards-0007.md#paper-155244)
- [Irreducible Supervision Enables Compositional Generalization in Post-Training](../conferences/neurips-2026/cards-0007.md#paper-149659)
- [LARK: Learnability-Grounded Trajectory Selection for Efficient Reasoning Distillation](../conferences/neurips-2026/cards-0007.md#paper-149142)
- [LCD$^3$: Layout-Conditioned Diffusion for Dataset Distillation in Object Detection](../conferences/neurips-2026/cards-0007.md#paper-150456)
- [Learning to Correct Geometry in Generated Videos](../conferences/neurips-2026/cards-0007.md#paper-154269)
- [Learning under Localized Minority Imbalance](../conferences/neurips-2026/cards-0007.md#paper-148554)
- [Learning Where to Simulate: Generative Active Sampling for Online PDE Surrogate Training](../conferences/neurips-2026/cards-0007.md#paper-151676)
- [Less Language, More Latents: Annotation-Efficient VLAs for Driving](../conferences/neurips-2026/cards-0007.md#paper-149160)
- [Leveraging Data Symmetries to Select an Optimal Subset of Training Data under Label Noise](../conferences/neurips-2026/cards-0007.md#paper-151105)
- [LITE: A Lightweight Lazy Sampler for Efficient SGD](../conferences/neurips-2026/cards-0008.md#paper-154582)
- [LittleLearner: Language Models Under Pedagogically-Controlled Knowledge Exposure](../conferences/neurips-2026/cards-0008.md#paper-148220)
- [LLM-ACES: Closed-Loop Discovery of Dynamic Systems with LLM-Guided Adaptive Search](../conferences/neurips-2026/cards-0008.md#paper-155346)
- [Localized Dynamics-Aware Domain Adaption for Off-Dynamics Offline Reinforcement Learning](../conferences/neurips-2026/cards-0008.md#paper-151978)
- [LoMo: Local Modality Substitution for Deeper Vision-Language Fusion](../conferences/neurips-2026/cards-0008.md#paper-154345)
- [Lumberjack: Better Differentially Private Random Forests through Heavy Hitter Detection in Trees](../conferences/neurips-2026/cards-0008.md#paper-148332)
- [M$^3$: Reframing Training Measures for Discretized Physical Simulations](../conferences/neurips-2026/cards-0008.md#paper-149542)
- [META-PAP: Meta-learning for Prompt-aware Preference Pairing in LLM Alignment](../conferences/neurips-2026/cards-0008.md#paper-148316)
- [MGMem: An Efficient, Deterministic, and Provenance-Preserving Framework for Long-Horizon Agent Memory](../conferences/neurips-2026/cards-0008.md#paper-151505)
- [MindLoom: Composing Thought Modes for Frontier-Level Reasoning Data Synthesis](../conferences/neurips-2026/cards-0008.md#paper-155952)
- [MIRAGE: Duality-Inspired MILP Augmentation for Representation Learning](../conferences/neurips-2026/cards-0008.md#paper-150478)
- [Model Distribution-Aware Multimodal Dataset Distillation](../conferences/neurips-2026/cards-0008.md#paper-148787)
- [NADS: Navigator-Guided Data Selection for Mitigating Catastrophic Forgetting in Fine-Tuning](../conferences/neurips-2026/cards-0008.md#paper-148869)
- [Negation Neglect: When models fail to learn negations in training](../conferences/neurips-2026/cards-0008.md#paper-149048)
- [New Coresets for Fair Clustering](../conferences/neurips-2026/cards-0009.md#paper-152649)
- [OFBD: Object-Focused Background Debiasing for Long-Tailed Learning](../conferences/neurips-2026/cards-0009.md#paper-152979)
- [OmniEgoCap: Camera-Agnostic Sequence-Level Egocentric Motion Reconstruction](../conferences/neurips-2026/cards-0009.md#paper-151885)
- [Online Data Selection for Instruction Tuning via Gaussian Processes](../conferences/neurips-2026/cards-0009.md#paper-155444)
- [OpenSearcher: Democratizing Deep Search through a Fully Offline Pipeline with Programmatic Verification](../conferences/neurips-2026/cards-0009.md#paper-152128)
- [Opt-Arena: Evaluating, Selecting, and Generating Optimization Modeling Data via Tripartite Graphs](../conferences/neurips-2026/cards-0009.md#paper-153953)
- [Optimal Real-Data Allocation for Synthetic-Data-Augmented Inference](../conferences/neurips-2026/cards-0009.md#paper-148327)
- [Optimal Transport Reweighting for Robust Learning under Spurious Correlations and Label Noise](../conferences/neurips-2026/cards-0009.md#paper-149217)
- [Pixels to Tokens: Token Space Efficient Active Learning for Low-Budget Semantic Segmentation](../conferences/neurips-2026/cards-0009.md#paper-148535)
- [Provable Selective Auto-labeling with Reliability Guarantees](../conferences/neurips-2026/cards-0010.md#paper-154352)
- [Quantile Benchmarking Heterogeneous Web Corpora in Open LLM Pretraining](../conferences/neurips-2026/cards-0010.md#paper-149953)
- [Readiness-Aware Sample Selection for Noisy Labels with Class Imbalance](../conferences/neurips-2026/cards-0010.md#paper-153563)
- [REGATE: Confidence-Calibrated Integration of Temporally-Aligned Exogenous Texts for Dynamic Graphs](../conferences/neurips-2026/cards-0010.md#paper-150490)
- [Rethinking Dataset Distillation for Classification: Do Distilled Sets Outperform Coresets?](../conferences/neurips-2026/cards-0010.md#paper-139495)
- [ReToken: One Token to Improve Vision–Language Models for Visual Retrieval](../conferences/neurips-2026/cards-0010.md#paper-155661)
- [Retrieval-Centric Deep Learning in Growing Nonparametric Neural Networks](../conferences/neurips-2026/cards-0010.md#paper-150000)
- [Retrieval from Within: An Intrinsic Capability of Attention-Based Models](../conferences/neurips-2026/cards-0010.md#paper-154257)
- [Reverse to Advance: Teleoperation-Cost Effective Hard Policy Learning from Reversed Easy Tasks](../conferences/neurips-2026/cards-0010.md#paper-152349)
- [Ripple in Still Water: Zero-Shot Clustering in Heterogeneous Federated Learning with Wavelet Scattering Transform](../conferences/neurips-2026/cards-0010.md#paper-150906)
- [Robust Approximate Nearest Neighbor Search for Any Dataset](../conferences/neurips-2026/cards-0010.md#paper-150072)
- [SAGE: Semantic Ambiguity Guided Capacity Expansion for Retrieval-Augmented Generation](../conferences/neurips-2026/cards-0010.md#paper-150303)
- [Scaling Laws for Multimodal Data Mixtures](../conferences/neurips-2026/cards-0010.md#paper-148475)
- [Scaling Laws for SAE Training Data](../conferences/neurips-2026/cards-0010.md#paper-148634)
- [Scaling Whole-Body Loco-Manipulation through Compositional Data Synthesis](../conferences/neurips-2026/cards-0010.md#paper-149896)
- [SIGMA: Semantic-Difference Instruction-Grounding Mask Annotator for Text-Driven Image Manipulation Localization](../conferences/neurips-2026/cards-0011.md#paper-151764)
- [Social Choice Foundations for Simulation-Augmented Generation](../conferences/neurips-2026/cards-0011.md#paper-148453)
- [SODA: Selective Optimization with Deferred BN Alignment for Efficient Dataset Distillation](../conferences/neurips-2026/cards-0011.md#paper-150571)
- [Spherical Interpolation for Backward-Compatible Multimodal Representations](../conferences/neurips-2026/cards-0011.md#paper-148719)
- [SteerCast: Retrieval-Based Latent Steering for Decoder-Only Time Series Forecasting](../conferences/neurips-2026/cards-0011.md#paper-154457)
- [Subdata Selection: A Unified Framework for Optimal Selection and Statistical Efficiency Assessment](../conferences/neurips-2026/cards-0011.md#paper-149020)
- [Swift Sampling: Selecting Temporal Surprises via Taylor Series](../conferences/neurips-2026/cards-0011.md#paper-151623)
- [Synthesis Through Simulation: Generating Coherent Enterprise Data via Scalable Agent-System Interaction](../conferences/neurips-2026/cards-0011.md#paper-151073)
- [Synthetic Tasks for Training AutoResearch](../conferences/neurips-2026/cards-0011.md#paper-152335)
- [Synthetic Worlds for Temporal Evaluation and Knowledge Updating in LLMs](../conferences/neurips-2026/cards-0011.md#paper-155151)
- [Temporal Prototype Alignment for Frozen-Feature Dataset Distillation](../conferences/neurips-2026/cards-0011.md#paper-149275)
- [The Horizon Threshold in Cooperative Multi-Agent Reward-Free Exploration](../conferences/neurips-2026/cards-0011.md#paper-149477)
- [The Missing Corpus: Infinite Ground Truth for File-Grounded LLM Evaluation](../conferences/neurips-2026/cards-0011.md#paper-139327)
- [The Sample Complexity of Multiple Change Point Identification under Bandit Feedback](../conferences/neurips-2026/cards-0012.md#paper-152674)
- [The Sampling Complexity of Condorcet Winner Identification in Dueling Bandits](../conferences/neurips-2026/cards-0012.md#paper-151146)
- [TIGER: Bridging the Multimodal Reasoning-Access Gap via Modality Counterfactuals](../conferences/neurips-2026/cards-0012.md#paper-152182)
- [TimeWarp: Evaluating Web Agents by Revisiting the Past](../conferences/neurips-2026/cards-0012.md#paper-139159)
- [TopoPrune: Robust Data Pruning via Unified Latent Space Topology](../conferences/neurips-2026/cards-0012.md#paper-154394)
- [Towards Generalizable Data Valuation: Learning an End-to-end Deep Model to Compute Shapley Values](../conferences/neurips-2026/cards-0012.md#paper-155035)
- [Towards Generalizable Partially Relevant Video Retrieval](../conferences/neurips-2026/cards-0012.md#paper-151222)
- [Towards instance-dependent regret optimality in Episodic MDPs with Posterior Sampling](../conferences/neurips-2026/cards-0012.md#paper-153285)
- [Towards On-Policy Data Evolution for Visual-Native Multimodal Deep Search Agents](../conferences/neurips-2026/cards-0012.md#paper-148687)
- [Towards Optimal Pre-training Data Mixtures for Empowering Reinforcement Learning in LLMs](../conferences/neurips-2026/cards-0012.md#paper-152676)
- [Towards Scalable Data Diversification for Language Model Pretraining via Leverage Score Sampling](../conferences/neurips-2026/cards-0012.md#paper-150922)
- [Train at the Moving Edge: Rollout-Efficient RL for Large Reasoning Models](../conferences/neurips-2026/cards-0012.md#paper-149668)
- [Transfer Learning Through Conditional Quantile Matching](../conferences/neurips-2026/cards-0012.md#paper-152993)
- [TReDS: Trajectory-Grounded Requirement-Capability Modeling for Training Distribution Shaping in Tool-Interactive Tasks](../conferences/neurips-2026/cards-0012.md#paper-155240)
- [Uncertainty-Guided Reward Labeling for Reinforcement Learning under Limited Feedback](../conferences/neurips-2026/cards-0012.md#paper-149046)
- [Unifying Partner and Environment Diversity to Improve Human-AI Coordination](../conferences/neurips-2026/cards-0012.md#paper-151901)
- [Utility-Driven Clustered Federated Learning via Class-wise Interaction Attribution](../conferences/neurips-2026/cards-0012.md#paper-154062)
- [VidHalluDoctor: Learning Video Differences to Mitigate Hallucinations in Vision-Language Models](../conferences/neurips-2026/cards-0012.md#paper-153093)
- [VL-DocIR: A Benchmark for Vision-Based Long Document Retrieval](../conferences/neurips-2026/cards-0012.md#paper-139402)
- [VoluCore: Spanning Teacher Representations with Volumetric Coresets for Data-Efficient LLM Distillation](../conferences/neurips-2026/cards-0012.md#paper-155942)
- [Wayfinder: Adaptive Resource Routing from Agent Citations](../conferences/neurips-2026/cards-0012.md#paper-148786)
- [When Are Semivalue-Based Decisions Identifiable? Robust Data Selection under Utility Ambiguity](../conferences/neurips-2026/cards-0012.md#paper-155762)
- [When Simulation Lies: A Sim-to-Real Benchmark and Domain-Randomized RL Recipe for Tool-Use Agents](../conferences/neurips-2026/cards-0012.md#paper-139169)
- [X-AVDD: Cross-Attentive Audio-Visual Dataset Distillation](../conferences/neurips-2026/cards-0013.md#paper-153215)
- [XMNoise2Clean: Cross-Modal Denoising Under Sparse Data](../conferences/neurips-2026/cards-0013.md#paper-151207)

## CVPR 2026（暂收录）

- [Unique Lives, Shared World: Learning from Single-Life Videos](../conferences/cvpr-2026/cards.md#paper-single-life-geometry)
- [Federated Active Learning Under Extreme Non-IID and Global Class Imbalance](../conferences/cvpr-2026/cards.md#paper-fairfal-local-global-querying)
- [Shoe Style-Invariant and Ground-Aware Learning for Dense Foot Contact Estimation](../conferences/cvpr-2026/cards.md#paper-feco-contact-style-randomization)
- [HoneyBee: Data Recipes for Vision-Language Reasoners](../conferences/cvpr-2026/cards.md#paper-honeybee-data-interventions)
- [Delving Aleatoric Uncertainty in Medical Image Segmentation via Vision Foundation Models](../conferences/cvpr-2026/cards.md#paper-aleatoric-uncertainty-spectrum)
- [Does YOLO Really Need to See Every Training Image in Every Epoch?](../conferences/cvpr-2026/cards.md#paper-afss-anti-forgetting-sampling)
- [DiT360: High-Fidelity Panoramic Image Generation via Hybrid Training](../conferences/cvpr-2026/cards.md#paper-dit360)
- [JRM: Joint Reconstruction Model for Multiple Objects without Alignment](../conferences/cvpr-2026/cards.md#paper-jrm-negative-support-reconstruction)
- [UniLS: End-to-End Audio-Driven Avatars for Unified Listening and Speaking](../conferences/cvpr-2026/cards.md#paper-unils)
- [A Unified Framework for Knowledge Transfer in Bidirectional Model Scaling](../conferences/cvpr-2026/cards.md#paper-bidirectional-wavelet-model-scaling)
- [Revisiting Unknowns: Towards Effective and Efficient Open-Set Active Learning](../conferences/cvpr-2026/cards.md#paper-e2oal)
- [PLACID: Identity-Preserving Multi-Object Compositing via Video Diffusion with Synthetic Trajectories](../conferences/cvpr-2026/cards.md#paper-placid-synthetic-trajectories)
- [Portable Active Learning for Object Detection](../conferences/cvpr-2026/cards.md#paper-portable-active-learning-detection)
- [Concept-Aware Batch Sampling Improves Language-Image Pretraining](../conferences/cvpr-2026/cards.md#paper-concept-aware-batch-sampling)
- [StaR-KVQA: Structured Reasoning Traces for Implicit-Knowledge Visual Question Answering](../conferences/cvpr-2026/cards.md#paper-star-kvqa)
- [Revisiting the Necessity of Lengthy Chain-of-Thought in Vision-centric Reasoning Generalization](../conferences/cvpr-2026/cards.md#paper-minimal-grounding-cot-generalization)
- [AE2VID: Event-based Video Reconstruction via Aperture Modulation](../conferences/cvpr-2026/cards.md#paper-ae2vid-active-event-acquisition)
- [Mitigating The Distribution Shift of Diffusion-based Dataset Distillation](../conferences/cvpr-2026/cards.md#paper-diffusion-dataset-distribution-shift)
- [Long-Tail Internet Photo Reconstruction](../conferences/cvpr-2026/cards.md#paper-megadepth-x-sparse-view-sampling)
- [MotionEdit: Benchmarking and Learning Motion-Centric Image Editing](../conferences/cvpr-2026/cards.md#paper-motionnft)
- [FBTA: Enabling Single-GPU End-to-End Gigapixel WSI Classification with Feature Bridging and Translation Alignment](../conferences/cvpr-2026/cards.md#paper-fbta-feature-bridging)
- [Beyond the Golden Data: Resolving the Motion-Vision Quality Dilemma via Timestep Selective Training](../conferences/cvpr-2026/cards.md#paper-tqd-video-diffusion)
- [Agile Deliberation: Concept Deliberation for Subjective Visual Classification](../conferences/cvpr-2026/cards.md#paper-agile-deliberation)
- [Generalizable Video Quality Assessment via Weak-to-Strong Learning](../conferences/cvpr-2026/cards.md#paper-weak-to-strong-video-quality)
- [DiG: Differential Grounding for Enhancing Fine-Grained Perception in Multimodal Large Language Models](../conferences/cvpr-2026/cards.md#paper-dig-differential-grounding)
- [MDS-VQA: Model-Informed Data Selection for Video Quality Assessment](../conferences/cvpr-2026/cards.md#paper-mds-vqa)
- [OpenVision 2: A Family of Generative Pretrained Visual Encoders for Multimodal Learning](../conferences/cvpr-2026/cards.md#paper-openvision-2-generative-pretraining)
- [Cleaning the Pool: Progressive Filtering of Unlabeled Pools in Deep Active Learning](../conferences/cvpr-2026/cards.md#paper-refine-active-learning)
- [Dataset Distillation by Influence Matching](../conferences/cvpr-2026/cards.md#paper-infmatch-terminal-data-influence)
- [R4: Retrieval-Augmented Reasoning for Vision-Language Models in 4D Spatio-Temporal Space](../conferences/cvpr-2026/cards.md#paper-r4-semantic-spatiotemporal-memory-retrieval)
- [Less is More: Data-Efficient Adaptation for Controllable Text-to-Video Generation](../conferences/cvpr-2026/cards.md#paper-simple-synthetic-video-controls)
- [Socratic-Geo: Synthetic Data Generation and Cross-Modal Geometric Reasoning via Multi-Agent Interaction](../conferences/cvpr-2026/cards.md#paper-socratic-geo-failure-directed-synthesis)
- [SRA 2: Variational Autoencoder Self-Representation Alignment  for Efficient Diffusion Training](../conferences/cvpr-2026/cards.md#paper-sra2-vae-feature-alignment)
- [AffordGen: Generating Diverse Demonstrations for Generalizable Object Manipulation with Affordance Correspondence](../conferences/cvpr-2026/cards.md#paper-affordgen-geometry-demonstration-budget)
- [Beyond Semantic Search: Towards Referential Anchoring in Composed Image Retrieval](../conferences/cvpr-2026/cards.md#paper-oacir-instance-anchor-retrieval)
- [What Makes Good Synthetic Training Data for Zero-Shot Stereo Matching?](../conferences/cvpr-2026/cards.md#paper-synthetic-stereo-camera-baseline-distribution)
- [Retrieve-to-Restore: Efficient All-in-One Image Restoration with a Retrieval-Based Degradation Bank](../conferences/cvpr-2026/cards.md#paper-r2r-retrieved-degradation-prior-bank)
- [MR-RAG: Multimodal Relevance-Aware Retrieval-Augmented Generation for Medical Visual Question Answering](../conferences/cvpr-2026/cards.md#paper-mr-rag)
- [EvoGraph-R1: Self-Evolving Multimodal Knowledge Hypergraphs for Agentic Retrieval](../conferences/cvpr-2026/cards.md#paper-evograph-online-multimodal-graph-refinement)
- [GThinker: Towards General Multimodal Reasoning via Cue-Guided Rethinking](../conferences/cvpr-2026/cards.md#paper-gthinker-cue-rethinking)
- [OS-Fed: One Snapshot Is All You Need](../conferences/cvpr-2026/cards.md#paper-osfed-compact-learned-update-snapshot)
- [Real2Edit2Real: Generating Robotic Demonstrations via a 3D Control Interface](../conferences/cvpr-2026/cards.md#paper-real2edit2real)
- [IntroSVG: Learning from Rendering Feedback for Text-to-SVG Generation via an Introspective Generator-Critic Framework](../conferences/cvpr-2026/cards.md#paper-introsvg-render-feedback)
- [Stitch-a-Demo: Creating Video Demonstrations from Multistep Descriptions](../conferences/cvpr-2026/cards.md#paper-stitch-a-demo-coherence-hard-negatives)
- [From Panel to Pixel: Zoom-In Vision-Language Pretraining from Biomedical Scientific Literature](../conferences/cvpr-2026/cards.md#paper-panel2patch-hierarchical-figure-supervision)
- [VideoNet: A Large-Scale Dataset for Domain-Specific Action Recognition](../conferences/cvpr-2026/cards.md#paper-videonet-single-action-filtering)
- [Synthetic Object Compositions for Scalable and Accurate Learning in Detection, Segmentation, and Grounding](../conferences/cvpr-2026/cards.md#paper-soc-label-preserving-object-composition)
- [Towards Generalized Multimodal Homography Estimation](../conferences/cvpr-2026/cards.md#paper-multimodal-homography-synthesis)
- [ReMatch: Boosting Representation through Matching for Multimodal Retrieval](../conferences/cvpr-2026/cards.md#paper-rematch-generative-retrieval-supervision)
- [MuCo: Multi-turn Contrastive Learning for Multimodal Embedding Model](../conferences/cvpr-2026/cards.md#paper-muco-multi-turn-contrastive)
- [FedRG: Unleashing the Representation Geometry for Federated Learning with Noisy Clients](../conferences/cvpr-2026/cards.md#paper-fedrg-geometry-first-noisy-labels)
- [ViLoMem: Agentic Learner with Grow-and-Refine Multimodal Semantic Memory](../conferences/cvpr-2026/cards.md#paper-vilomem-visual-and-logical-memory-streams)
- [Diffusion-Based Native Adversarial Synthesis for Enhanced Medical Segmentation Generalization](../conferences/cvpr-2026/cards.md#paper-synthetic-hard-example-utility)
- [PropFly: Learning to Propagate via On-the-Fly Supervision from Pre-trained Video Diffusion Models](../conferences/cvpr-2026/cards.md#paper-propfly-online-paired-supervision)
- [Image-based Outlier Synthesis With Training Data](../conferences/cvpr-2026/cards.md#paper-ascood-inlier-derived-outliers)
- [RAG-TP: A General Framework for Vehicle Trajectory Prediction via Retrieval-Augmented Generation](../conferences/cvpr-2026/cards.md#paper-rag-tp-retrieved-trajectory-experts)
- [No Need For Real Anomaly: MLLM Empowered Zero-Shot Video Anomaly Detection](../conferences/cvpr-2026/cards.md#paper-lavida-pseudo-anomalies)
- [BriMA: Bridged Modality Adaptation for Multi-Modal Continual Action Quality Assessment](../conferences/cvpr-2026/cards.md#paper-brima-modality-aware-replay)
- [Multi-Scale Gaussian-Language Map for Zero-shot Embodied Navigation and Reasoning](../conferences/cvpr-2026/cards.md#paper-glmap-instance-region-memory-navigation)
- [HAD: Hallucination-Aware Diffusion Priors for 3D Reconstruction](../conferences/cvpr-2026/cards.md#paper-had-multiview-hallucination-masks)
- [FreeScale: Scaling 3D Scenes via Certainty-Aware Free-View Generation](../conferences/cvpr-2026/cards.md#paper-freescale-certainty-views)
- [M^3KG-RAG: Multi-hop Multimodal Knowledge Graph-enhanced Retrieval-Augmented Generation](../conferences/cvpr-2026/cards.md#paper-m3kg-rag-modality-retrieval-graph-filtering)
- [EventHub: Data Factory for Generalizable Event-Based Stereo Networks without Active Sensors](../conferences/cvpr-2026/cards.md#paper-eventhub)
- [Guardians of the Hair: Rescuing Soft Boundaries in Depth, Stereo, and Novel Views](../conferences/cvpr-2026/cards.md#paper-hairguard-soft-boundary-correction)
- [FoundIR-v2: Optimizing Pre-Training Data Mixtures for Image Restoration Foundation Model](../conferences/cvpr-2026/cards.md#paper-foundir-v2-data-equilibrium)
- [MatchMask: Mask-Centric Generative Data Augmentation for Label-Scarce Semantic Segmentation](../conferences/cvpr-2026/cards.md#paper-matchmask-gradient-probe)
- [CLIP-like Model as a Foundational Density Ratio Estimator](../conferences/cvpr-2026/cards.md#paper-clip-foundational-density-ratio)
- [Unlocking Strong Supervision: A Data-Centric Study of General-Purpose Audio Pre-Training Methods](../conferences/cvpr-2026/cards.md#paper-audio-strong-supervision-objective-tradeoffs)

<!-- conference-classification:end -->
