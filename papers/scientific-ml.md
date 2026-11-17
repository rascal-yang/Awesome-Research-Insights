# 科学机器学习

[首页](../README.md) · [English](../en/papers/scientific-ml.md)

物理、医学、生物与工程中的机器学习。

<!-- classification:start -->
## 按技术类型浏览

<a id="by-architecture"></a>

### 模型架构

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="abijuru26a-architecture"></a>[Physics-Informed Residual Flows](https://proceedings.mlr.press/v306/abijuru26a.html) | 物理约束学习 | 把物理场预测拆成显式残差修正步骤，并检查中间预测是否沿合适的方向变化。 |
| <a id="ai26f-architecture"></a>[Nested Spatio-Temporal Time Series Forecasting](https://proceedings.mlr.press/v306/ai26f.html) | 时空预测 | 先对节点做谱聚类并预测区域级未来趋势，再将预测到的宏观变化注入节点级预测。 |
| <a id="andersson26a-architecture"></a>[scCBGM: Single-Cell Editing via Concept Bottlenecks](https://proceedings.mlr.press/v306/andersson26a.html) | 单细胞反事实编辑 | 在概念瓶颈加入解码器跳连，用交叉协方差惩罚减少概念与其他潜变量的相关性，再用合成反事实逐细胞验证编辑效果。 |
| <a id="bacarreza26a-architecture"></a>[Quantum latent distributions in deep generative models](https://proceedings.mlr.press/v306/bacarreza26a.html) | 量子生成先验 | 在理论设定中，量子潜分布能高效生成部分经典潜分布难以高效得到的目标分布。论文用光子实验和模拟比较了量子干涉带来的影响。 |
| <a id="balik26a-architecture"></a>[Modeling Temporal scRNA-seq Data with Latent Gaussian Process and Optimal Transport](https://proceedings.mlr.press/v306/balik26a.html) | 单细胞时间建模 | 用最优传输对齐观测和生成的群体快照，在没有逐细胞轨迹时仍可拟合潜高斯过程。用细胞类型及潜在时间建模异步发展。 |
| <a id="bao26d-architecture"></a>[Cheap2Rich: A Multi-Fidelity Framework for Data Assimilation and System Identification of Multiscale Physics - Rotating Detonation Engines](https://proceedings.mlr.press/v306/bao26d.html) | 多保真数据同化 | 将便宜的低保真模拟作为动态先验，由稀疏传感器历史估计可解释的误差修正，以恢复高保真状态中的局部物理效应。 |
| <a id="bazzi26a-architecture"></a>[Physics-Informed Coarsening for Multigrid Graph Neural Surrogates](https://proceedings.mlr.press/v306/bazzi26a.html) | 固体力学代理模型 | 用局部物理残差给网格节点评分，粗化时优先保留高应变和应力集中区域，改善多重网格 GNN 的长程 rollout 稳定性。 |
| <a id="berman26b-architecture"></a>[Stochastic Lifting for Generating Trajectories of Stochastic Physical Systems](https://proceedings.mlr.press/v306/berman26b.html) | 随机动力学生成 | 给每条训练转移附加独立随机坐标，让回归模型学到相近状态的多种后继。推理时重新采样坐标，每步一次前向生成随机轨迹。 |
| <a id="brandle26a-architecture"></a>[Continuous-Time Piecewise-Linear Recurrent Neural Networks](https://proceedings.mlr.press/v306/brandle26a.html) | 连续时间动力学 | 利用 ReLU 循环网络各区域内的分段线性结构推进连续动力学，减少数值积分开销，并能半解析地查找平衡点和极限环。 |
| <a id="brinke26a-architecture"></a>[STFlow: Data-Coupled Flow Matching for Geometric Trajectory Simulation](https://proceedings.mlr.press/v306/brinke26a.html) | 几何轨迹生成 | 以按观测条件构造的随机游走作为流匹配起点，替代独立高斯噪声。更接近真实轨迹的先验能降低传输成本。 |
| <a id="bu26d-architecture"></a>[Stochastic Neural Ray Tracing for Radio Frequency Channel Modeling](https://proceedings.mlr.press/v306/bu26d.html) | 无线传播建模 | 把射频传播写成随机输运过程，让材料衰减率成为可学习的传播参数，在神经射线追踪中保留互易性和可逆性。 |
| <a id="cao26ad-architecture"></a>[LabBuilder: Protocol-Grounded 3D Layout Generation for Interactable and Safe Laboratory](https://proceedings.mlr.press/v306/cao26ad.html) | 实验室布局生成 | 先把自然语言任务转成结构化实验协议，再在几何、导航及化学安全约束下迭代布局，使生成场景能按所建模的协议执行。 |
| <a id="chasmai26b-architecture"></a>[Bioacoustic Geolocation: Species Sounds as Geographic Signals](https://proceedings.mlr.press/v306/chasmai26b.html) | 生物声学定位 | 将声音里的物种线索与其地理分布结合，再融合检索定位；聚合附近多个样本可进一步利用物种组成线索。 |
| <a id="chen26aa-architecture"></a>[StormInsight: Hierarchical Environmental Forcing and Vertical Coupling for Convective Systems Evolution](https://proceedings.mlr.press/v306/chen26aa.html) | 对流风暴短时预报 | 分别编码风暴状态、垂直热力耦合和大尺度环境强迫，再按环境变化聚合不同高度的信息，支持三维结构的短时演化预测。 |
| <a id="chen26ai-architecture"></a>[From Holo Pockets to Electron Density: GPT-style Drug Design with Density](https://proceedings.mlr.press/v306/chen26ai.html) | 电子密度条件分子生成 | 用口袋内配体和溶剂的低分辨率电子密度代替刚性空口袋条件。密度可以来自计算或实验，并让自回归模型利用构象和占位信息。 |
| <a id="chen26cu-architecture"></a>[Co-Generative De Novo Functional Protein Design](https://proceedings.mlr.press/v306/chen26cu.html) | 功能条件蛋白质共生成 | 从功能提示检索已知结构基序，经交叉注意力引导氨基酸和结构 token 同步生成，再用局部结构的功能分类作为辅助监督。这样可把抽象功能条件落实到具体的结构线索。 |

<a id="by-modules"></a>

### 模块

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="berman26d-modules"></a>[Smoothness Errors in Dynamics Models and How to Avoid Them](https://proceedings.mlr.press/v306/berman26d.html) | 网格动力学平滑 | 热扩散等过程本身需要平滑，严格酉卷积会限制这种物理变化。放松酉性可在抑制图网络过平滑的同时允许合理的平滑演化。 |
| <a id="chang26b-modules"></a>[MedSIGHT: Towards Grounded Visual Comprehension in Medical Large Vision-Language Models](https://proceedings.mlr.press/v306/chang26b.html) | 医学视觉定位 | 在语言模型词表中引入区域代码，通过区域感知模块将代码解码成像素掩码，使语言输出能够对应到图像里的具体组织区域。 |
| <a id="chen26bw-modules"></a>[TSMGen: Target-Specific Molecule Generation via Higher-Order Structural Dependencies and Context-Aware Bidirectional Fusion](https://proceedings.mlr.press/v306/chen26bw.html) | 口袋与配体双向融合 | 将残基超图与原子级几何编码成口袋表征，让口袋与候选分子序列的特征分别作为查询做门控交叉注意力。把口袋查询得到的全局向量广播到各序列位置，再与逐位置融合结果相加以引导 SMILES 生成。 |

<a id="by-loss-functions"></a>

### 损失函数

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="abijuru26b-loss-functions"></a>[Heavy-tailed Physics-Informed Neural Networks](https://proceedings.mlr.press/v306/abijuru26b.html) | 鲁棒损失 | 把物理残差建模为 Student-t，通过 EM 自适应调低极端残差在加权 MSE 中的影响。 |
| <a id="anwer26a-loss-functions"></a>[Certificates for Complex-Compatible Learned Cochain Laplacians](https://proceedings.mlr.press/v306/anwer26a.html) | 网格算子学习 | 给学习出的算子对测量其偏离链复形一致性的距离，并可闭式投影到最近的兼容算子，避免网格细化时条件数失控。 |
| <a id="byeon26a-loss-functions"></a>[HEXST: Hexagonal Shifted-Window Transformer for Spatial Transcriptomics Gene Expression Prediction](https://proceedings.mlr.press/v306/byeon26a.html) | 空间转录组预测 | 针对组织切片上六角排列的采样点，用几何匹配的窗口和位置编码，再加局部差分损失，减轻逐点回归导致的基因表达过平滑。 |
| <a id="chasmai26a-loss-functions"></a>[MetaPerch: Learning from metadata for bioacoustics foundation models](https://proceedings.mlr.press/v306/chasmai26a.html) | 生物声学辅助监督 | 把录音已有的时间和位置元数据作为辅助学习目标，借物种与环境的相关性塑造表征，并分别测地理和声学域偏移。 |
| <a id="chen26y-loss-functions"></a>[SGERA: Stein-Guided ECG-Report Alignment for ECG Representation Learning](https://proceedings.mlr.press/v306/chen26y.html) | 心电与报告对齐 | 分别用 Stein 核约束单条心电与报告的匹配及跨样本的整体分布，再用难例匹配细化边界，弥补单一对比损失只监督样本对的不足。 |
| <a id="chen26at-loss-functions"></a>[FACT: Fuzzy Alignment with Comorbidity Topology for Reliable Multi-Label Medical Image Diagnosis](https://proceedings.mlr.press/v306/chen26at.html) | 共病多标签表征 | 让同一局部视觉证据以模糊隶属度支持多个疾病概念，再按共病关系组织概念锚点，避免硬分类边界抹掉可共享的病征。 |

<a id="by-optimization"></a>

### 优化

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="chen26ck-optimization"></a>[Learning-Guided Integration Contours Construction for Fast Large-Scale Generalized Eigensolvers](https://proceedings.mlr.press/v306/chen26ck.html) | 广义特征值积分轮廓 | 对厄米广义特征值问题，先用神经算子快速预测实谱，再用核密度估计找出谱簇间的低密度谷底，以此划分积分轮廓并预留边距。目标特征值由后续围道积分求解器计算。 |

<a id="by-reinforcement-learning"></a>

### 强化学习方法

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="behzadifar26a-reinforcement-learning"></a>[DecAEvolve: Decompose, Adapt, and Evolve for Effective LLM-based Scientific Equation Discovery](https://proceedings.mlr.press/v306/behzadifar26a.html) | 科学方程发现 | 把候选方程拆成符号项提供细粒度反馈，再用测试时强化学习更新假设生成器，让后续搜索利用当前系统的观测与误差。 |
| <a id="butbaia26a-reinforcement-learning"></a>[Hierarchical Reinforcement Learning for Sparse-Reward Search in Commutative Algebra](https://proceedings.mlr.press/v306/butbaia26a.html) | 数学反例搜索 | 把构造代数反例建成稀疏奖励的图搜索，使用受约束的多步选项与等变图策略，在长搜索中学习可复用的时间抽象。 |
| <a id="chang26g-reinforcement-learning"></a>[RetrOrchestrator: A Multi-Step Retrosynthesis Agent Dynamically Orchestrating Single-Step Transition Models](https://proceedings.mlr.press/v306/chang26g.html) | 逆合成搜索工具选择 | 搜索时同时决定展开哪个分子、调用哪个单步逆合成模型。用基于分子骨架的强化学习按局面路由，可利用各模型的互补能力。 |

<a id="by-training-strategies"></a>

### 训练策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="cao26r-training-strategies"></a>[TD3B: Transition-Directed Discrete Diffusion for Allosteric Binder Generation](https://proceedings.mlr.press/v306/cao26r.html) | 变构蛋白结合物生成 | 将预测激动或拮抗方向的信号与软亲和门控分开，用两者微调离散扩散，使生成目标能区分作用方向和静态结合强度。 |
| <a id="charles26a-training-strategies"></a>[Tokenised Flow Matching for Hierarchical Simulation Based Inference](https://proceedings.mlr.press/v306/charles26a.html) | 层级仿真推断 | 先从单站点仿真学习因子化似然，再拼出多站点合成观测训练完整层级后验，可减少每个训练样本需要调用仿真器的次数。 |
| <a id="chen26ao-training-strategies"></a>[EMFormer: Efficient Multi-Scale Transformer for Accumulative Context Weather Forecasting](https://proceedings.mlr.press/v306/chen26ao.html) | 长时天气预测 | 渐进增加模型可见的累积历史做微调，减轻长时预测误差累积，并用动态加权的组合损失平衡长短预测目标。 |

<a id="by-data-strategies"></a>

### 数据策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="brockschmidt26a-data-strategies"></a>[SurvDiff: A Diffusion Model for Generating Synthetic Data in Survival Analysis](https://proceedings.mlr.press/v306/brockschmidt26a.html) | 生存分析合成数据 | 联合生成协变量、事件时间和右删失标记，并把生存任务结构写进扩散损失，避免合成表格只拟合协变量却丢失删失机制。 |
| <a id="chan26a-data-strategies"></a>[DC-W2S: Dual-Consensus Weak-to-Strong Training for Reliable Process Reward Modeling in Biological Reasoning](https://proceedings.mlr.press/v306/chan26a.html) | 过程奖励数据筛选 | 同时用弱标注者之间的一致性与嵌入近邻的一致性评估逐步标签，再按可靠性采样例子并遮蔽可疑标签。 |

<a id="by-inference"></a>

### 推理策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="aich26a-inference"></a>[WIND: Weather Inverse Diffusion for Zero-Shot Atmospheric Modeling](https://proceedings.mlr.press/v306/aich26a.html) | 大气生成模型 | 用无条件大气视频扩散模型学习通用先验，将预报、降尺度和稀疏观测重建分别写成逆问题，在推理时做后验采样。 |
| <a id="andrae26a-inference"></a>[DAISI: Data Assimilation with Inverse Sampling using Stochastic Interpolants](https://proceedings.mlr.press/v306/andrae26a.html) | 数据同化 | 先用逆向采样把预报信息注入固定生成先验，再用观测引导条件采样。预报器可替换，生成先验无需逐轮重训。 |
| <a id="baker26a-inference"></a>[Supervised Guidance Training for Infinite-Dimensional Diffusion Models](https://proceedings.mlr.press/v306/baker26a.html) | 函数空间逆问题 | 用无限维 Doob h 变换把后验分数拆成无条件分数与观测引导项，只训练引导分量即可复用函数空间的扩散先验。 |
| <a id="bohde26a-inference"></a>[FRIGID: Scaling Diffusion-Based Molecular Generation from Mass Spectra at Training and Inference Time](https://proceedings.mlr.press/v306/bohde26a.html) | 质谱到分子生成 | 用正向碎裂模型找出候选分子中与观测质谱不符的局部片段，只重掩码并去噪这些片段，随推理预算逐步纠偏。 |
| <a id="cao26c-inference"></a>[Chamaileon: Cross-Context Binder Design with Contextualized Modeling and Mixed Sampling](https://proceedings.mlr.press/v306/cao26c.html) | 蛋白结合物设计 | 联合学习不同结合环境下的序列与结构，再在推理时混合多个环境的采样路径，以搜索同一条能适配多目标或多构象的序列。 |
| <a id="chen26bu-inference"></a>[Towards Docking-oriented De Novo Ligand Design via Gradient Inversion](https://proceedings.mlr.press/v306/chen26bu.html) | 对接预测梯度反演 | 把训练好的可微对接模型用作生成时的评分器，对候选配体的连续坐标和特征反传预测目标的梯度，每步投影回可行集合，最后按小分子或蛋白质配体的约束解码。 |

<a id="by-representation-learning"></a>

### 表征学习

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="abulikemu26a-representation-learning"></a>[Geometry-Guided Generative Representation for Functional Brain Graphs](https://proceedings.mlr.press/v306/abulikemu26a.html) | 图表征学习 | 用跨样本对齐的功能梯度作为图自编码器的几何先验，再在压缩的图级潜空间建模。 |
| <a id="antoniadis26a-representation-learning"></a>[Protein Language Model Embeddings Improve Generalization of Implicit Transfer Operators](https://proceedings.mlr.press/v306/antoniadis26a.html) | 分子动力学泛化 | 在粗粒化的隐式转移算子中加入蛋白语言模型嵌入作为条件，可改善对未见过蛋白的平衡态采样。 |
| <a id="ariguib26a-representation-learning"></a>[Learning the Neighborhood: Contrast-Free Multimodal Self-Supervised Molecular Graph Pretraining](https://proceedings.mlr.press/v306/ariguib26a.html) | 分子自监督 | 用固定半径子图作训练单元，从互补邻域预测其潜嵌入，把同一分子的多种 3D 构象引入免负样本训练。 |
| <a id="baloch26a-representation-learning"></a>[A Machine-Learned Comorbidity Index](https://proceedings.mlr.press/v306/baloch26a.html) | 多结局风险表征 | 用归一化 Hilbert–Schmidt 独立性准则将诊断编码压成一个非线性分数，使其共同反映多个结局的风险。 |
| <a id="chen26u-representation-learning"></a>[Foundation VAEs for CT Reconstruction, Augmentation, and Generation](https://proceedings.mlr.press/v306/chen26u.html) | 医学图像潜空间复用 | 自然图像和视频上预训练的 VAE 可以冻结后用于 CT 重建，再在同一潜空间训练条件扩散，复用编码器做重建、增强和生成。 |
| <a id="chen26ay-representation-learning"></a>[MolAlign3D: Enhancing Fixed-Dimensional E(3)-Equivariant Latent Space for High-Fidelity 3D Molecular Reconstruction and Editing](https://proceedings.mlr.press/v306/chen26ay.html) | 三维分子表征 | 在固定维的 E(3) 等变几何潜空间里加上预训练分子编码器的语义锚点，可保留重建精度，同时改善改变原子数等零样本编辑。 |
| <a id="chen26ct-representation-learning"></a>[SLAE: Strictly Local All-atom Environment for Protein Representation](https://proceedings.mlr.press/v306/chen26ct.html) | 蛋白质局部全原子表征 | 以残基附近的重原子类型和相对几何构建局部表征，同时监督全原子坐标重建、氨基酸识别和 Rosetta 相互作用能回归，让表征同时保留侧链几何和局部化学环境。 |
| <a id="chen26db-representation-learning"></a>[Protein Fold Classification at Scale: Benchmarking and Pretraining](https://proceedings.mlr.press/v306/chen26db.html) | 高掩码蛋白质结构预训练 | 随机掩去最高 90% 的残基，以 SE(3) 不变编码器处理可见结构，让轻量解码器重建骨架坐标。在去冗余的 TEDBench 上，这种自监督表征提升了折叠拓扑分类表现。 |

<a id="by-evaluation"></a>

### 评测与诊断

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="ahamed26a-evaluation"></a>[TFRBench: A Reasoning Benchmark for Evaluating Forecasting Systems](https://proceedings.mlr.press/v306/ahamed26a.html) | 时间序列预测评测 | 给预测器的解释也打分，检查跨变量依赖、趋势和外部事件，并用数值核验循环构造有数据依据的推理轨迹。 |
| <a id="alfarano26a-evaluation"></a>[Improving ML Attacks on LWE with Data Repetition and Stepwise Regression](https://proceedings.mlr.press/v306/alfarano26a.html) | 格密码机器学习分析 | 在论文测试的 LWE 参数内，重复训练样本与扩充数据都能帮助恢复更密集的秘密向量，逐步回归则用于更易识别的一部分分量。 |
| <a id="amalan26a-evaluation"></a>[MalTree: Tracing Malware Evolution from Embeddings at Scale](https://proceedings.mlr.press/v306/amalan26a.html) | 恶意软件谱系重建 | 从多种恶意软件特征构建进化树，并用样本时间戳验证推断的祖先后代关系，可以比较不同家族的演化速度。 |
| <a id="bahrini26a-evaluation"></a>[When Can We Trust Survival Model Evaluation ?](https://proceedings.mlr.press/v306/bahrini26a.html) | 生存模型评测 | 用未删失的完整事件时间作为基准，分别核对删失如何影响指标数值和模型排序。指标偏差适中也可能伴随排序失真。 |
| <a id="bai26a-evaluation"></a>[Op-CAD: Benchmarking and Investigating Operation-oriented CAD Generation](https://proceedings.mlr.press/v306/bai26a.html) | CAD 操作评测 | 用几何引导解析把建模序列切成单个操作，并用倒角和圆角专用的 CF-IoU 检查局部改动，避免整体形状相近掩盖操作错误。 |
| <a id="becktepe26a-evaluation"></a>[Plug-and-Play Benchmarking of Reinforcement Learning Algorithms for Large-Scale Flow Control](https://proceedings.mlr.press/v306/becktepe26a.html) | 流体控制强化学习 | 把可微 GPU 流体求解器和环境统一在 PyTorch 栈内，固定观测、执行和评测口径，让 PPO、SAC 与可微控制能直接对照。 |
| <a id="cao26g-evaluation"></a>[SimulCost: A Cost-Aware Benchmark and Toolkit for Automating Physics Simulations with LLMs](https://proceedings.mlr.press/v306/cao26g.html) | 仿真 Agent 成本评测 | 在测参成功率之外，把仿真器调用成本独立记账，并与固定扫描基线比较。论文中，多轮交互提高成功率的同时仍可能更耗时。 |
| <a id="chandok26a-evaluation"></a>[A Systematic Study of Behavioral Cloning for Scientific Data Annotation](https://proceedings.mlr.press/v306/chandok26a.html) | 科学标注行为克隆 | 用模拟的专家导航、纠错和验证轨迹研究标注策略，分开测界面操作与任务决策。多任务预训练可提升少样本新标注任务的微调效果。 |

<a id="by-theory-statistics"></a>

### 理论与统计

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="antipov26a-theory-statistics"></a>[Flow-Based Density Ratio Estimation for Intractable Distributions with Applications in Genomics](https://proceedings.mlr.press/v306/antipov26a.html) | 密度比估计 | 用条件 flow matching 沿同一条生成轨迹追踪密度比，省去分别求两种分布似然再相除的流程。 |
| <a id="bao26a-theory-statistics"></a>[Learning Junta Distributions, Quantum Junta States, and QAC$^0$ Circuits](https://proceedings.mlr.press/v306/bao26a.html) | 量子稀疏依赖学习 | 只有 k 个相关位的经典分布可用约 2^k log(n) / ε² 个样本学习。量子态的相应结构只在 k 个量子位上偏离最大混合态，也可利用这种低维依赖。 |
| <a id="berman26a-theory-statistics"></a>[Leveraging Gauge Freedom for Learning Non-Gradient Population Dynamics of Stochastic Systems](https://proceedings.mlr.press/v306/berman26a.html) | 群体动力学反演 | 用连续性方程的弱形式约束总体分布演化，并允许非梯度速度场，可重建最小动能梯度流无法表达的输运。 |
<!-- classification:end -->
