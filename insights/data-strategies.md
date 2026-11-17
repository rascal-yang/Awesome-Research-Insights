# 数据策略

[首页](../README.md) · [参与贡献](../CONTRIBUTING.md) · [English](../en/insights/data-strategies.md)

数据筛选、标注、增强与采样。

<!-- classification:start -->
## 按研究领域浏览

[大语言模型](#by-llm) · [计算机视觉](#by-computer-vision) · [自然语言处理](#by-nlp) · [强化学习](#by-reinforcement-learning) · [机器人学](#by-robotics) · [多模态学习](#by-multimodal) · [机器学习基础与统计](#by-ml-foundations) · [图学习与推荐](#by-graph-and-recommendation) · [科学机器学习](#by-scientific-ml)

<a id="by-llm"></a>

### 大语言模型

- [数据选择](../conferences/icml-2026/cards/0001-0100.md#aden-ali26a-data-strategies) · Subliminal Effects in Your Data: A General Mechanism via Log-Linearity
- [训练数据选择](../conferences/icml-2026/cards/0001-0100.md#agrawal26a-data-strategies) · Minibatch selection for Language Models via Partition Matroid Constrained Gradient Matching
- [改写稳定性](../conferences/icml-2026/cards/0101-0200.md#arraf26a-data-strategies) · Learning Rewrite-Invariant Reasoning with Targeted Alternation Training
- [代码安全评测](../conferences/icml-2026/cards/0101-0200.md#arx26a-data-strategies) · AutoBaxBuilder: Bootstrapping Code Security Benchmarking
- [奖励投机](../conferences/icml-2026/cards/0101-0200.md#azarbal26a-data-strategies) · Recontextualization Mitigates Specification Gaming Without Modifying the Specification
- [事实预训练](../conferences/icml-2026/cards/0201-0300.md#behnia26a-data-strategies) · Facts in Stats: Impacts of Pretraining Diversity on Language Model Generalization
- [GUI Agent 错误恢复](../conferences/icml-2026/cards/0301-0400.md#bu26b-data-strategies) · Recovering Policy-Induced Errors: Benchmarking and Trajectory Synthesis for Robust GUI Agents
- [网页 Agent 训练环境](../conferences/icml-2026/cards/0401-0500.md#chae26a-data-strategies) · Safe and Scalable Web Agent Learning via Recreated Websites
- [开放预测训练数据](../conferences/icml-2026/cards/0401-0500.md#chandak26a-data-strategies) · Curating the Future: A Scalable Recipe for Training Open-Ended Forecasters
- [威胁情报驱动的流量数据构造](../conferences/icml-2026/cards/0501-0600.md#chen26cb-data-strategies) · Threat2Traffic: Multi-Agent Environment Synthesis for Malware Traffic Generation from Threat Intelligence
- [语料域变动后的混合比例复用](../conferences/icml-2026/cards/0501-0600.md#chen26dd-data-strategies) · Olmix: A Framework for Data Mixing Throughout LM Development
- [任务敏感注意力头筛样](../conferences/icml-2026/cards/0601-0700.md#chen26gi-data-strategies) · From Parameters to Data: A Task-Parameter-Guided Fine-Tuning Pipeline for Efficient LLM Alignment
- [从工具执行轨迹反推训练任务](../conferences/icml-2026/cards/0601-0700.md#chen26gj-data-strategies) · DIVE: Scaling Diversity in Agentic Task Synthesis for Generalizable Tool Use
- [棋类后训练数据的推理忠实度](../conferences/icml-2026/cards/0901-1000.md#dionisopoulos26a-data-strategies) · How Reasoning Evolves from Post-Training Data: An Empirical Study Using Chess
- [语言模型预训练语料的时间排序](../conferences/icml-2026/cards/1001-1100.md#fabre26a-data-strategies) · Understanding Data Temporality Impact on Large Language Models Pre-training
- [指令数据的缺陷分诊](../conferences/icml-2026/cards/1101-1200.md#fu26f-data-strategies) · Cure-SFT: Diagnostic-Guided Data Curation for Instruction Tuning
- [差分隐私偏好对合成](../conferences/icml-2026/cards/1201-1300.md#gao26ae-data-strategies) · Differentially Private Preference Data Synthesis for Large Language Model Alignment
- [复用可验证的软件环境](../conferences/icml-2026/cards/1301-1400.md#guo26aa-data-strategies) · MEnvAgent: Scalable Polyglot Environment Construction for Verifiable Software Engineering
- [用多步代理更新估计样本的后续价值](../conferences/icml-2026/cards/1401-1500.md#hao26b-data-strategies) · BLISS: A Lightweight Bilevel Influence Scoring Method for Data Selection in Language Model Pretraining
- [交替由学生写风格和教师补解法](../conferences/icml-2026/cards/1701-1800.md#huang26bq-data-strategies) · How to Fine-Tune a Reasoning Model? A Teacher–Student Cooperation Framework to Synthesize Student-Consistent SFT Data
- [把短题答案串成可验收的长链](../conferences/icml-2026/cards/1801-1900.md#ivanova26a-data-strategies) · h1: Bootstrapping LLMs to Reason over Longer Horizons via Reinforcement Learning
- [用同一教师对齐前后差异筛选监督](../conferences/icml-2026/cards/1901-2000.md#jiang26j-data-strategies) · Contrastive Weak-to-Strong Generalization
- [先验证可解性再奖励合成题难度](../conferences/icml-2026/cards/1901-2000.md#jiao26f-data-strategies) · Agentic Proposing: Enhancing Large language Model Reasoning via Compositional Skill Synthesis
- [用扰动模型的前缀损失挑长推理样本](../conferences/icml-2026/cards/1901-2000.md#jin26o-data-strategies) · Reasoning Quality Emerges Early: Data Curation for Reasoning Models
- [按短前缀给每步推理单独打分](../conferences/icml-2026/cards/2001-2100.md#just26a-data-strategies) · The Signal is in the Steps: Local Scoring for Reasoning Data Selection
- [按边际安全收益选择最小增强集](../conferences/icml-2026/cards/2001-2100.md#kao26a-data-strategies) · Submodular Optimization for Minimal Augmentation in Robust Language Model Alignment
- [用模型自己的解掩顺序生成训练掩码](../conferences/icml-2026/cards/2101-2200.md#kim26o-data-strategies) · Stop Training for the Worst: Progressive Unmasking Accelerates Masked Diffusion Training
- [将端侧偏好记忆压缩为可检索指令](../conferences/icml-2026/cards/2301-2400.md#lee26u-data-strategies) · From Volume to Value: Preference-Aligned Memory Construction for On-Device RAG
- [先定义专家推理步骤再用证据改写监督](../conferences/icml-2026/cards/2301-2400.md#levi26a-data-strategies) · Toward Cybersecurity-Expert Small Language Models
- [容量感知的数据配比定律](../conferences/icml-2026/cards/2401-2500.md#li26av-data-strategies) · Capacity-Aware Mixture Law Enables Efficient LLM Data Optimization
- [瞄准稀疏字典中的数据空缺](../conferences/icml-2026/cards/2601-2700.md#li26hl-data-strategies) · Less is Enough: Synthesizing Diverse Data in LLM Feature Space with Sparse Autoencoders
- [用合并成分模型评估预训练数据配比](../conferences/icml-2026/cards/2601-2700.md#li26jt-data-strategies) · Decouple Searching from Training: Scaling Data Mixing via Model Merging for Large Language Model Pre-training
- [用实体与约束子树合成知识密集建模任务](../conferences/icml-2026/cards/2701-2800.md#liu26d-data-strategies) · Opt-Miner: Empowering Information-Seeking Agent with Tree-Guided Data Synthesis for Optimization Modeling
- [联合调节微调数据预算与推理难度](../conferences/icml-2026/cards/2701-2800.md#liu26m-data-strategies) · Data Difficulty and the Generalization–Extrapolation Tradeoff in LLM Fine-Tuning
- [由检索头干预识别高价值推理步骤](../conferences/icml-2026/cards/2801-2900.md#liu26bd-data-strategies) · AIR: Post-training Data Selection for Reasoning via Attention Head Influence
- [把题内均匀抽样当作代码数据筛选对照](../conferences/icml-2026/cards/2801-2900.md#liu26bz-data-strategies) · Random Selection Reveals Implicit Knowledge Consensus in Code Generation
- [可执行推理题族合成](../conferences/icml-2026/cards/2901-3000.md#liu26ew-data-strategies) · Scaling the Scaling Logic: Agentic Meta-Synthesis of Logic Reasoning
- [Lean 缺失经验引理挖掘](../conferences/icml-2026/cards/2901-3000.md#liu26ez-data-strategies) · MathlibLemma: Folklore Lemma Generation and Benchmark for Formal Mathematics
- [从开放文本构造可核验强化学习题](../conferences/icml-2026/cards/3001-3100.md#lu26a-data-strategies) · Golden Goose: A Simple Trick to Synthesize Unlimited RLVR Tasks from Unverifiable Internet Text
- [从可运行全栈仓库反推训练任务与测试](../conferences/icml-2026/cards/3001-3100.md#lu26ab-data-strategies) · FullStack-Agent: Enhancing Agentic Full-Stack Web Coding via Development-Oriented Testing and Repository Back-Translation
- [用目标条件的 token 保留率给微调样本排序](../conferences/icml-2026/cards/3001-3100.md#luo26m-data-strategies) · TarGATE: Target-Aware Data Selection via Token-Attenuation Gates
- [用 Actor–Critic 动态选择预训练域权重](../conferences/icml-2026/cards/3101-3200.md#ma26i-data-strategies) · AC-ODM: Actor–Critic Online Data Mixing for Sample-Efficient LLM Pretraining
- [补少量实体恒等句让自回归模型学反向关联](../conferences/icml-2026/cards/3101-3200.md#ma26o-data-strategies) · Breaking the Reversal Curse in Autoregressive Language Models via Identity Bridge
- [用非对称辩论验证定制守卫训练样本](../conferences/icml-2026/cards/3201-3300.md#mazza26a-data-strategies) · BARRED: Synthetic Training of Custom Policy Guardrails via Asymmetric Debate
- [主动偏好对选择](../conferences/icml-2026/cards/3201-3300.md#melikidze26a-data-strategies) · ActiveUltraFeedback: Efficient Preference Data Generation using Active Learning
- [智能体轨迹水印](../conferences/icml-2026/cards/3201-3300.md#meng26b-data-strategies) · Watermarking LLM Agent Trajectories
- [在 LoRA 验证梯度子空间筛选指令数据](../conferences/icml-2026/cards/3301-3400.md#min26a-data-strategies) · GIST: Targeted Data Selection for Instruction Tuning via Coupled Optimization Geometry
- [用均衡语义域支持预训练数据配比](../conferences/icml-2026/cards/3301-3400.md#min26e-data-strategies) · GEM: Geometric Entropy Mixing for Optimal LLM Data Curation
- [用效用相同的偏好对压制伪特征](../conferences/icml-2026/cards/3301-3400.md#moya26a-data-strategies) · Spurious Correlation Learning in Preference Optimization: Mechanisms, Consequences, and Mitigation via Tie Training
- [按注意力指纹筛指令数据](../conferences/icml-2026/cards/3301-3400.md#nagaraj26a-data-strategies) · TRIM: Token-wise Attention-Derived Saliency for Data-Efficient Instruction Tuning
- [区分预训练过滤收益与高质量分布匹配](../conferences/icml-2026/cards/3401-3500.md#nait-saada26a-data-strategies) · Removing Noise, not Finding Gold: Quality Filtering for Large-Scale Pretraining
- [提示响应互信息](../conferences/icml-2026/cards/3401-3500.md#nam26b-data-strategies) · Maximizing Mutual Information Between Prompt and Response Improves LLM Performance With No Additional Data
- [安全数据白化归因](../conferences/icml-2026/cards/3501-3600.md#pan26l-data-strategies) · Detecting and Filtering Unsafe Training Data via Data Attribution with Denoised Representation
- [用当前模型的估计熵重排领域课程](../conferences/icml-2026/cards/3501-3600.md#pang26e-data-strategies) · EDCO: Dynamic Curriculum Orchestration for Domain-specific Large Language Model Fine-tuning
- [反向推理骨架](../conferences/icml-2026/cards/3601-3700.md#peng26b-data-strategies) · Measuring and Mitigating Post-Hoc Rationalization in Reverse Chain-of-Thought Generation
- [用验证器筛选有效又加速的循环不变量](../conferences/icml-2026/cards/3601-3700.md#pinto26a-data-strategies) · Not All Invariants Are Equal: Curating Training Data to Accelerate Program Verification with SLMs
- [小模型蒸馏保留本机推理表达](../conferences/icml-2026/cards/3701-3800.md#qian26l-data-strategies) · The Quality-Utility Paradox: Why High-Reward Data Impairs Small Model Mathematical Reasoning
- [基于共享历史的推理提示选样](../conferences/icml-2026/cards/3701-3800.md#qu26f-data-strategies) · Small Generalizable Prompt Predictive Models Can Steer Efficient RL Post-Training of Large Reasoning Models
- [按用户保护完整纵向序列](../conferences/icml-2026/cards/3801-3900.md#rosenblatt26a-data-strategies) · Privately Fine-Tuned LLMs Preserve Temporal Dynamics in Tabular Data
- [用补丁行召回构造仓库专用代理数据](../conferences/icml-2026/cards/4001-4100.md#shen26o-data-strategies) · SERA: Soft-Verified Efficient Repository Agents

<a id="by-computer-vision"></a>

### 计算机视觉

- [图像训练数据保护](../conferences/icml-2026/cards/0301-0400.md#cai26m-data-strategies) · FUSE: Full-spectrum Unlearnable Examples via Spectral Equalization
- [合成图检测](../conferences/icml-2026/cards/0401-0500.md#cao26s-data-strategies) · Where Detectors Fail: Probing Generative Space for Generalizable AI-Generated Image Detection
- [生成偏好数据](../conferences/icml-2026/cards/0401-0500.md#chen26s-data-strategies) · When Preference Labels Fall Short: Aligning Diffusion Models from Real Data
- [跨域遮挡分割数据](../conferences/icml-2026/cards/0501-0600.md#chen26bj-data-strategies) · Amodal Instance Segmentation with IRAIS Dataset for Sim-to-Real Transfer
- [扩散训练子集的单边部分传输](../conferences/icml-2026/cards/0701-0800.md#cui26f-data-strategies) · Geometry-Aware Dataset Condensation for Diffusion Model Training
- [生成视频检测的质量分布配对](../conferences/icml-2026/cards/1001-1100.md#fang26s-data-strategies) · Real Data Lies: Unveiling and Closing the Quality Shortcut in Generalizable AI-Generated Video Detection
- [扩散数据蒸馏的集合耦合引导](../conferences/icml-2026/cards/1101-1200.md#gan26d-data-strategies) · Set-Coupled Guidance: Set-Level Coordination in Diffusion-Based Dataset Distillation
- [分别约束插入物的布局、照明和边界纹理](../conferences/icml-2026/cards/1601-1700.md#hou26a-data-strategies) · Plan, Decouple, Assimilate: Physics-Aware Object Insertion in Remote Sensing Imagery
- [以细粒度隐私标注驱动频带适配](../conferences/icml-2026/cards/1601-1700.md#hu26bk-data-strategies) · VPD-100K: Towards Generalizable and Fine-grained Visual Privacy Protection
- [沿正常特征低方差方向造难负例](../conferences/icml-2026/cards/2001-2100.md#karzanov26a-data-strategies) · Geometrically Constrained Outlier Synthesis
- [乘积流形上的数据集蒸馏](../conferences/icml-2026/cards/2501-2600.md#li26ea-data-strategies) · GeoDM: Geometry-aware Distribution Matching for Dataset Distillation
- [按最差分类间隔蒸馏数据](../conferences/icml-2026/cards/2501-2600.md#li26ec-data-strategies) · Mind Your Margin and Boundary: Are Your Distilled Datasets Truly Robust?
- [用带符号熵轨迹识别错误图像标签](../conferences/icml-2026/cards/2601-2700.md#li26ju-data-strategies) · On Revisiting Entropy for Identifying Mislabeled Images
- [单目数据立体反遮挡](../conferences/icml-2026/cards/3001-3100.md#lu26k-data-strategies) · Geometric Reciprocity: Unlocking Self-Supervision for Stereoscopic Video Generation
- [语义校准局部扩散增强](../conferences/icml-2026/cards/3101-3200.md#lv26c-data-strategies) · SCalDA: Semantics-Calibrated and Diffusion-Enhanced Data Augmentation
- [重识别类别核心集](../conferences/icml-2026/cards/3401-3500.md#oh26b-data-strategies) · CSOR: Coreset Selection for Object Re-identification via Class Pruning
- [按识别特征距离选择扩散混合类别](../conferences/icml-2026/cards/3801-3900.md#rahimi26a-data-strategies) · ScoreMix: Synthetic Data Generation by Score Composition in Diffusion Models Improves Recognition
- [用细粒度对象簇训练属性编辑](../conferences/icml-2026/cards/3801-3900.md#reiss26a-data-strategies) · Alterbute: Editing Intrinsic Attributes of Objects in Images

<a id="by-nlp"></a>

### 自然语言处理

- [差分隐私合成数据](../conferences/icml-2026/cards/0201-0300.md#banayeeanzade26a-data-strategies) · EPSVec: Efficient and Private Synthetic Data Generation via Dataset Vectors
- [对比学习的困难负例组批](../conferences/icml-2026/cards/0901-1000.md#dutta26a-data-strategies) · HOBIT: Hardness Optimized Batch Sampling for InfoNCE Training
- [用结构化属性生成可审计的隐私文书](../conferences/icml-2026/cards/2101-2200.md#kim26az-data-strategies) · Privasis: Synthesizing the Largest "Public" Private Dataset from Scratch

<a id="by-reinforcement-learning"></a>

### 强化学习

- [零样本离线强化学习](../conferences/icml-2026/cards/0201-0300.md#bendib26a-data-strategies) · Improving Zero-Shot Offline RL via Behavioral Task Sampling
- [跨域离线强化学习的软筛选](../conferences/icml-2026/cards/0601-0700.md#chen26gd-data-strategies) · Transport or Discard: Robust Unbalanced Optimal Transport for Cross-Domain Policy Adaptation
- [数学搜索课程的中间难度实例](../conferences/icml-2026/cards/1001-1100.md#fagan26a-data-strategies) · The Two-Hump Problem: Bridging the Difficulty Gap in Mathematical Reinforcement Learning
- [世界模型的主动探测数据](../conferences/icml-2026/cards/1101-1200.md#feng26aa-data-strategies) · Learning Task-Sufficient World Models by Synergizing Agentic Exploration and Structured Modeling
- [用情景记忆的时差误差选择合成强化学习经验](../conferences/icml-2026/cards/3101-3200.md#ma26p-data-strategies) · Episodic Memory-Guided Controllable Experience Synthesis for Reinforcement Learning
- [按动力学模式赋值的跨域离线强化学习](../conferences/icml-2026/cards/3701-3800.md#qiao26e-data-strategies) · Unifying Value Alignment and Assignment in Cross-Domain Offline Reinforcement Learning with Heterogeneous Datasets
- [以同一状态拼接来路和去路](../conferences/icml-2026/cards/3701-3800.md#qing26a-data-strategies) · BiTrajDiff: Bidirectional Trajectory Generation with Diffusion Models for Offline Reinforcement Learning
- [用可核验轨迹捷径增加离线转移](../conferences/icml-2026/cards/3901-4000.md#schmahling26a-data-strategies) · Trajectory-Level Data Augmentation for Offline Reinforcement Learning

<a id="by-robotics"></a>

### 机器人学

- [双臂仿真数据生成](../conferences/icml-2026/cards/0401-0500.md#chen26j-data-strategies) · RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation
- [物理可用的桌面场景](../conferences/icml-2026/cards/0401-0500.md#chen26ab-data-strategies) · PhyScene3D: Physically Consistent Interactive 3D Tabletop Scene Generation
- [固定预算下的机器人示范分配](../conferences/icml-2026/cards/0501-0600.md#chen26cy-data-strategies) · Escaping the Diversity Trap in Robotic Manipulation via Anchor-Centric Adaptation
- [具身动作风险的组合数据构造](../conferences/icml-2026/cards/0701-0800.md#choi26i-data-strategies) · EMBGuard: Constructing Hazard-Aware Guardrails for Safe Planning in Embodied Agents
- [跨来源点云的 VLA 训练](../conferences/icml-2026/cards/1001-1100.md#fan26b-data-strategies) · Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds
- [人类视频的潜动作监督](../conferences/icml-2026/cards/1201-1300.md#gao26q-data-strategies) · DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos
- [人形运动跟踪的可行性与难度选样](../conferences/icml-2026/cards/1301-1400.md#guan26f-data-strategies) · LIMMT: Less Is More for Motion Tracking
- [固定动作几何并按覆盖选择模拟视频改写](../conferences/icml-2026/cards/1701-1800.md#hui26b-data-strategies) · Seeing Realism from Simulation: Efficient Video Transfer for Vision-Language-Action Data Augmentation
- [以仿真重放跨机器人改写同一示范](../conferences/icml-2026/cards/1801-1900.md#ji26g-data-strategies) · OXE-AugE: A Large-Scale Robot Augmentation of OXE for Scaling Cross-Embodiment Policy Learning
- [分别模拟深度像素失效和值误差](../conferences/icml-2026/cards/2601-2700.md#liang26n-data-strategies) · PRISM: Learning Realistic Depth via Physics-Grounded Noise Disentanglement with Semantic-Geometric Collaboration

<a id="by-multimodal"></a>

### 多模态学习

- [数据与后训练](../conferences/icml-2026/cards/0001-0100.md#acuna26a-data-strategies) · Long Grounded Thoughts: Synthesizing Visual Problems and Reasoning Chains at Scale
- [视觉定位监督](../conferences/icml-2026/cards/0101-0200.md#assouel26a-data-strategies) · PGT: Procedurally Generated Tasks for improving visual grounding in MLLMs
- [多模态数据蒸馏](../conferences/icml-2026/cards/0301-0400.md#bo26b-data-strategies) · Efficient Multi-modal Dataset Distillation via Analytic Parameter Matching
- [弱监督指代分割](../conferences/icml-2026/cards/0401-0500.md#cao26aa-data-strategies) · Learning to Label: A Reinforced Self-Evolving Framework for Semi-supervised Referring Expression Segmentation
- [GUI 智能体的失败轨迹纠错数据](../conferences/icml-2026/cards/0601-0700.md#chen26gb-data-strategies) · CAPTCHA Solving for Native GUI Agents: Automated Reasoning-Action Data Generation and Self-Corrective Training
- [用近域异常文本约束开放集识别](../conferences/icml-2026/cards/1001-1100.md#fang26b-data-strategies) · Immuno-VLM: Immunizing Large Vision-Language Models via Generative Semantic Antibodies for Open-World Trustworthiness
- [电信观测序列保留绝对量纲](../conferences/icml-2026/cards/1101-1200.md#feng26s-data-strategies) · TelecomTS: A Multi-Modal Observability Dataset for Time Series and Language Analysis
- [知识密集视频的分技能数据构造](../conferences/icml-2026/cards/1101-1200.md#fu26s-data-strategies) · VideoKR: Towards Knowledge- and Reasoning-Intensive Video Understanding
- [视频到三维空间监督数据](../conferences/icml-2026/cards/1201-1300.md#gao26o-data-strategies) · Holi-Spatial: Evolving Video Streams into Holistic 3D Spatial Intelligence
- [图像到 CAD 的几何反馈扩增](../conferences/icml-2026/cards/1201-1300.md#giannone26a-data-strategies) · GIFT: Bootstrapping Image-to-CAD Program Synthesis via Geometric Feedback
- [界面全量解析监督](../conferences/icml-2026/cards/1401-1500.md#gurbuz26a-data-strategies) · ScreenParse: Moving Beyond Sparse Grounding with Complete Screen Parsing Supervision
- [从参考模型置信度自动构建视觉偏好对](../conferences/icml-2026/cards/1501-1600.md#he26ap-data-strategies) · RLSF-V: Mitigating Hallucinations in MLLMs via Fuzzy Semantic Self-Feedback
- [用遮罩模型生成无掩膜配音训练对](../conferences/icml-2026/cards/1501-1600.md#he26au-data-strategies) · From Inpainting to Editing: Unlocking Robust Mask-Free Visual Dubbing via Generative Bootstrapping
- [把可回放 GUI 探索组织成可复用前缀树](../conferences/icml-2026/cards/1901-2000.md#jiang26p-data-strategies) · TreeCUA: Efficiently Scaling GUI Automation with Tree-Structured Verifiable Evolution
- [用身体部位定位为无障碍理解建立监督](../conferences/icml-2026/cards/2001-2100.md#ke26e-data-strategies) · IVQA-LD: Inclusive Multimodal Understanding for Population with Limb Deficiency
- [用视觉交叉熵收益分配训练预算](../conferences/icml-2026/cards/2301-2400.md#lee26m-data-strategies) · Focusing Where Vision Matters: Selective Training for Large Vision Language Models via Visual Information Gain
- [先采高纯单事件再约束音频混合](../conferences/icml-2026/cards/2401-2500.md#li26y-data-strategies) · A Semantically Consistent Dataset for Data-Efficient Query-Based Universal Sound Separation
- [过程奖励训练的轨迹筛选](../conferences/icml-2026/cards/2401-2500.md#li26bm-data-strategies) · Training Data Efficiency in Multimodal Process Reward Models
- [用可执行绘图代码连接几何题结构和图像](../conferences/icml-2026/cards/2701-2800.md#lin26c-data-strategies) · Synthesizing Multimodal Geometry Datasets from Scratch and Enabling Visual Alignment via Plotting Code
- [按系统、图像与用户输入分解注意力识别投毒](../conferences/icml-2026/cards/2801-2900.md#liu26ag-data-strategies) · TCAP: Tri-Component Attention Profiling for Unsupervised Backdoor Detection in MLLM Fine-Tuning
- [用跨模态对齐轨迹选择指令样本](../conferences/icml-2026/cards/3401-3500.md#naharas26a-data-strategies) · Data Selection for Fine-tuning Vision Language Models via Cross Modal Alignment Trajectories
- [用自生成图注增加可利用的跨模态冗余](../conferences/icml-2026/cards/3901-4000.md#ryan26a-data-strategies) · Self-Captioning Multimodal Interaction Tuning: Amplifying Exploitable Redundancies for Robust Vision Language Models

<a id="by-ml-foundations"></a>

### 机器学习基础与统计

- [数据洗牌](../conferences/icml-2026/cards/0001-0100.md#afshani26a-data-strategies) · The benefits of full data shuffle, now with optimal I/O cost: $k$-wise independence and matrix transposition to the rescue
- [主动因果发现](../conferences/icml-2026/cards/0301-0400.md#bonilla26a-data-strategies) · Causal Preference Elicitation
- [带保证的自动标注](../conferences/icml-2026/cards/0301-0400.md#candes26a-data-strategies) · Probably Approximately Correct Labels
- [稀疏多类标注聚合](../conferences/icml-2026/cards/0401-0500.md#chen26ac-data-strategies) · Let the Prototype Guide You: Robust Aggregation of Sparse Multi-Class Annotations via Annotator Prototype Learning
- [训练样本选择的二部图覆盖](../conferences/icml-2026/cards/0701-0800.md#chi26d-data-strategies) · Unifying and Optimizing Data Values for Selection via Sequential Decision-Making
- [低秩数据子集的残差采样](../conferences/icml-2026/cards/0701-0800.md#cohen-addad26a-data-strategies) · Active Learning with Low-Rank Structure for Data Selection
- [元学习选样的低信噪比](../conferences/icml-2026/cards/0901-1000.md#du26u-data-strategies) · On the Difficulty of Learning a Meta-network for Training Data Selection
- [合成递归训练的多偏好筛选](../conferences/icml-2026/cards/1001-1100.md#falahati26a-data-strategies) · Curated Synthetic Data Doesn’t Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferences
- [治疗效应估计的主动随机试验](../conferences/icml-2026/cards/1201-1300.md#gao26z-data-strategies) · Budgeted Active Experimentation for Treatment Effect Estimation from Observational and Randomized Data
- [用全局模型的相对信心在客户端重分配标签](../conferences/icml-2026/cards/1601-1700.md#hu26ao-data-strategies) · FedReLa: Imbalanced Federated Learning via Re-Labeling
- [用参考模型权重方向估计样本效用](../conferences/icml-2026/cards/1601-1700.md#huang26c-data-strategies) · Evaluating Sample Utility for Efficient Data Selection by Mimicking Model Weights
- [用梯度投影贡献分配联邦客户端预算](../conferences/icml-2026/cards/1801-1900.md#ji26b-data-strategies) · ShapCCS: Shapley-Driven Client Coreset Selection in Federated Learning
- [在上下文中按条件互信息决定补测哪个特征](../conferences/icml-2026/cards/2101-2200.md#kobayashi26a-data-strategies) · Learning-To-Measure: In-Context Active Feature Acquisition
- [先复用加密边缘统计再发布私有合成数据](../conferences/icml-2026/cards/2201-2300.md#kumar26e-data-strategies) · $\textttFHAIM$: Fully Homomorphic AIM for Private Tabular Synthetic Data Generation
- [用单调学习曲线和预期缺口决定采集量](../conferences/icml-2026/cards/2301-2400.md#lee26af-data-strategies) · Monotonic Variational Gaussian Process for Efficient Data Collection
- [梯度筛查与特征校正的噪声标签净化](../conferences/icml-2026/cards/2401-2500.md#li26cr-data-strategies) · GFD-EMVC: Evolutionary Multi-View Classification with Label Noise via Gradient and Feature Dual-Perception
- [用预测相关性奖励训练少样本表格生成器](../conferences/icml-2026/cards/2701-2800.md#lin26p-data-strategies) · ReTabSyn: Realistic Tabular Data Synthesis via Reinforcement Learning
- [用小波最优输运边际影响给时序片段估值](../conferences/icml-2026/cards/2801-2900.md#liu26dh-data-strategies) · TimeLAVA: Learning-Agnostic Valuation for Time Series Data
- [回归残差复用](../conferences/icml-2026/cards/3301-3400.md#mohebbi26a-data-strategies) · Counterfactual Residual Data Augmentation for Regression
- [用等权群体重心蒸馏数据](../conferences/icml-2026/cards/3301-3400.md#moslemi26a-data-strategies) · Fair Dataset Distillation via Cross-Group Barycenter Alignment
- [解耦类别与域上下文来合成时间序列](../conferences/icml-2026/cards/3601-3700.md#pei26c-data-strategies) · CURE: Context-driven Diffusion with Progressive Expansion for Single Domain Generalization in Time Series Classification
- [在多种表征上挑回放样本](../conferences/icml-2026/cards/3701-3800.md#qi26n-data-strategies) · Cross-View Lewis Weight Fusion Empowering Exemplar Replay for Federated Class-Incremental Learning
- [递归生成中的局部筛选偏差](../conferences/icml-2026/cards/3701-3800.md#qiao26c-data-strategies) · When Sample Selection Bias Precipitates Model Collapse
- [保留残余噪声标签的训练数据迭代](../conferences/icml-2026/cards/3801-3900.md#rodriguez-munoz26a-data-strategies) · Ambient Dataloops: Generative Models for Dataset Refinement
- [凝缩时保留时序频谱和变量依赖](../conferences/icml-2026/cards/4001-4100.md#shao26b-data-strategies) · One Batch Is Enough: A Unified Dataset Condensation Framework for General Time Series Analysis

<a id="by-graph-and-recommendation"></a>

### 图学习与推荐

- [图数据增强](../conferences/icml-2026/cards/0101-0200.md#azizpour26a-data-strategies) · From Moments to Models: Graphon-Mixture Learning for Mixup and Contrastive Learning
- [联邦文本图证据凝缩](../conferences/icml-2026/cards/0501-0600.md#chen26cr-data-strategies) · DANCE: Dynamic, Available, Neighbor-gated Condensation for Federated Text-Attributed Graphs
- [图基础模型的合成预训练先验](../conferences/icml-2026/cards/1001-1100.md#eremeev26a-data-strategies) · GraphPFN: A Prior-Data Fitted Graph Foundation Model
- [选取同时覆盖特征与超图传播的标注节点](../conferences/icml-2026/cards/1601-1700.md#hou26c-data-strategies) · HIAL: Towards Semantics-Aware Hypergraph Active Learning via Dual-Perspective Information Maximization
- [以扩散邻域影响冲突诊断标签](../conferences/icml-2026/cards/2001-2100.md#ju26c-data-strategies) · Identifying and Correcting Label Noise for Robust GNNs via Influence Contradiction
- [先合成表间连接再生成列分布](../conferences/icml-2026/cards/2201-2300.md#kothapalli26a-data-strategies) · PluRel: Synthetic Data unlocks Scaling Laws for Relational Foundation Models
- [锚定超图凝缩并对齐两级分布](../conferences/icml-2026/cards/2501-2600.md#li26gi-data-strategies) · Anchor-guided Hypergraph Condensation with Dual-level Discrimination
- [潜空间单步合成图异常](../conferences/icml-2026/cards/2601-2700.md#li26hb-data-strategies) · GOCM: Single-Step Graph Outlier Synthesis via Origin Consistency Model

<a id="by-scientific-ml"></a>

### 科学机器学习

- [生存分析合成数据](../conferences/icml-2026/cards/0301-0400.md#brockschmidt26a-data-strategies) · SurvDiff: A Diffusion Model for Generating Synthetic Data in Survival Analysis
- [过程奖励数据筛选](../conferences/icml-2026/cards/0401-0500.md#chan26a-data-strategies) · DC-W2S: Dual-Consensus Weak-to-Strong Training for Reliable Process Reward Modeling in Biological Reasoning
- [物理仿真的流式快照压缩](../conferences/icml-2026/cards/0701-0800.md#cranganore26a-data-strategies) · ANTiC: Adaptive Neural Temporal In Situ Compressor
- [单细胞训练的块采样与批量预取](../conferences/icml-2026/cards/0801-0900.md#d-ascenzo26a-data-strategies) · scDataset: Scalable Data Loading for Deep Learning on Large-Scale Single-Cell Omics
- [用同步心电和呼吸筛选 PPG 对比样本](../conferences/icml-2026/cards/1201-1300.md#geenjaar26a-data-strategies) · A robust PPG foundation model using multimodal physiological supervision
- [在分布变化更快的内在时间上选择采样点](../conferences/icml-2026/cards/1701-1800.md#huynh26a-data-strategies) · Active Timepoint Selection for Learning Measure-Valued Trajectories
- [用几何投影约束血管造影的狭窄编辑](../conferences/icml-2026/cards/2601-2700.md#li26jn-data-strategies) · Geometrically Constrained Stenosis Editing in Coronary Angiography via Entropic Optimal Transport
- [离线预计算短式改写以去重训练](../conferences/icml-2026/cards/3901-4000.md#saegert26a-data-strategies) · Breaking the Simplification Bottleneck in Amortized Neural Symbolic Regression
<!-- classification:end -->
