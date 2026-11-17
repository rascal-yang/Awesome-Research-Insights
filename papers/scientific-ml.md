# 科学机器学习

[首页](../README.md) · [English](../en/papers/scientific-ml.md)

物理、医学、生物与工程中的机器学习。

<!-- classification:start -->
## 按技术类型浏览

<a id="by-architecture"></a>

### 模型架构

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="abijuru26a-architecture"></a>[Physics-Informed Residual Flows](https://proceedings.mlr.press/v306/abijuru26a.html) · [论文卡](../conferences/icml-2026/cards/0001-0100.md#paper-abijuru26a) | 物理约束学习 | 把物理场预测拆成显式残差修正步骤，并检查中间预测是否沿合适的方向变化。 |
| <a id="ai26f-architecture"></a>[Nested Spatio-Temporal Time Series Forecasting](https://proceedings.mlr.press/v306/ai26f.html) · [论文卡](../conferences/icml-2026/cards/0001-0100.md#paper-ai26f) | 时空预测 | 先对节点做谱聚类并预测区域级未来趋势，再将预测到的宏观变化注入节点级预测。 |
| <a id="andersson26a-architecture"></a>[scCBGM: Single-Cell Editing via Concept Bottlenecks](https://proceedings.mlr.press/v306/andersson26a.html) · [论文卡](../conferences/icml-2026/cards/0001-0100.md#paper-andersson26a) | 单细胞反事实编辑 | 在概念瓶颈加入解码器跳连，用交叉协方差惩罚减少概念与其他潜变量的相关性，再用合成反事实逐细胞验证编辑效果。 |
| <a id="bacarreza26a-architecture"></a>[Quantum latent distributions in deep generative models](https://proceedings.mlr.press/v306/bacarreza26a.html) · [论文卡](../conferences/icml-2026/cards/0101-0200.md#paper-bacarreza26a) | 量子生成先验 | 在理论设定中，量子潜分布能高效生成部分经典潜分布难以高效得到的目标分布。论文用光子实验和模拟比较了量子干涉带来的影响。 |
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
| <a id="collart26a-architecture"></a>[Constrained hybrid modelling to predict microbial dynamics and organic matter turnover in soil systems](https://proceedings.mlr.press/v306/collart26a.html) | 基因组性状到土壤碳动力学 | 用神经网络从宏基因组性状预测动力学参数，再经可微土壤过程模型生成碳库和 CO₂ 时间序列。以可测 CO₂ 拟合并对未观测状态和参数施加生态约束，可限制在相同排放曲线下可能出现的不合理动力学。 |
| <a id="cretu26a-architecture"></a>[SynLaD: Latent Diffusion for Generating Synthesizable Molecules Conditioned on 3D Pharmacophore Profiles](https://proceedings.mlr.press/v306/cretu26a.html) | 分子构象与合成路线的联合潜空间 | 用同一分子潜变量分别解码原子类型和三维坐标，以及序列化的反应合成路径。再以三维药效团为条件在该空间中做扩散采样，使生成结果同时附带候选结构和合成方案。 |
| <a id="dagli26a-architecture"></a>[Adaptive Volumetric Mechanical Property Fields Invariant to Resolution](https://proceedings.mlr.press/v306/dagli26a.html) | 机械属性场的自适应稀疏体素 | 由共享 Transformer 自粗到细处理待细分体素，让每个候选预测空置、保留或继续细分，并让子体素继承父级隐状态。保留的非空体素携带材料潜变量，可在不同分辨率下恢复杨氏模量、泊松比与密度。 |
| <a id="dai26a-architecture"></a>[TINNs: Time-Induced Neural Networks for Solving Time-Dependent PDEs](https://proceedings.mlr.press/v306/dai26a.html) | 时间驱动空间网络参数 | 用小网络给空间网络各层的权重组和偏置组分别生成时间坐标，同组参数共享该坐标但各有仿射系数。由此可随时间改变整个空间映射，又省去大超网络逐项生成全部参数的成本。 |
| <a id="deng26c-architecture"></a>[Condition-Aware Graph Flow Matching for Modeling the Distributions of Complex Fluid Systems](https://proceedings.mlr.press/v306/deng26c.html) | 工况条件下的分层图流匹配 | 将流体网格及其物理工况作为条件，用多层图上的消息传递预测流匹配向量场。构建粗图时兼顾邻接关系与局部点密度，使模型能在不规则网格上同时处理局部梯度和远距离作用。 |
| <a id="elsborg26a-architecture"></a>[Global Plane Waves from Local Gaussians: Periodic Charge Densities in a Blink](https://proceedings.mlr.press/v306/elsborg26a.html) | 周期晶体电荷密度的傅里叶重建 | 在实空间拟合局部各向异性高斯，从闭式傅里叶变换直接得到倒空间平面波系数，再以一次逆 FFT 重建整胞周期电荷密度，省去逐点累加周期镜像。 |
| <a id="fang26u-architecture"></a>[BIOARC: Discovering Optimal Neural Architectures for Biological Foundation Models](https://proceedings.mlr.press/v306/fang26u.html) | 生物序列模型的异构架构搜索 | 将卷积、循环、注意力和状态空间等块放入可共享权重的超网，每条候选路径独立选择深度、块类型和隐藏宽度。由数据筛选混合架构，以匹配基因组、蛋白等不同序列的归纳偏置。 |
| <a id="feng26b-architecture"></a>[LERD: Latent Event-Relational Dynamics for Neurodegenerative Classification](https://proceedings.mlr.press/v306/feng26b.html) | 脑电潜事件的电生理先验 | 将各脑电通道的潜事件时间建模为更新过程，用可微泄漏积分发放模型导出随时间变化的瞬时发放率作为先验。模型用该先验从未标注脑电推断事件与跨通道关系，并汇总组别的事件速率和时序差异。 |
| <a id="friedl26a-architecture"></a>[Learning Hamiltonian Dynamics at Scale: A Differential-Geometric Approach](https://proceedings.mlr.press/v306/friedl26a.html) | 辛降维的 Hamilton 动力学 | 用受几何约束的辛自编码器把高维状态压到低维结构保持子流形，在该空间内学习 Hamilton 动力学。通过保持潜空间的辛结构，降维后的模型仍可进行物理一致的长时预测。 |
| <a id="ghiglino26a-architecture"></a>["Do Diffusion Models Dream of Electric Planes?" Discrete and Continuous Simulation-Based Inference for Aircraft Design](https://proceedings.mlr.press/v306/ghiglino26a.html) | 飞行器拓扑与连续参数的层级扩散 | 先生成电动垂直起降飞行器的离散构型，再让掩码扩散模型在该构型下推断连续设计参数。按构型确定参与推断的变量，可处理不同部件数量和排列带来的可变参数维度。 |
| <a id="hagnberger26a-architecture"></a>[SMART: Scalable Mesh-free Aerodynamic Simulations from Raw Geometries using a Transformer-based Surrogate Model](https://proceedings.mlr.press/v306/hagnberger26a.html) | 点云到气动场的跨层解码 | 从原始几何点云和仿真参数提取不同深度的潜表征，让解码器每层查询对应编码层的几何特征，可在任意空间点估计物理量而无须输入仿真网格。 |

<a id="by-modules"></a>

### 模块

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="berman26d-modules"></a>[Smoothness Errors in Dynamics Models and How to Avoid Them](https://proceedings.mlr.press/v306/berman26d.html) | 网格动力学平滑 | 热扩散等过程本身需要平滑，严格酉卷积会限制这种物理变化。放松酉性可在抑制图网络过平滑的同时允许合理的平滑演化。 |
| <a id="chang26b-modules"></a>[MedSIGHT: Towards Grounded Visual Comprehension in Medical Large Vision-Language Models](https://proceedings.mlr.press/v306/chang26b.html) | 医学视觉定位 | 在语言模型词表中引入区域代码，通过区域感知模块将代码解码成像素掩码，使语言输出能够对应到图像里的具体组织区域。 |
| <a id="chen26bw-modules"></a>[TSMGen: Target-Specific Molecule Generation via Higher-Order Structural Dependencies and Context-Aware Bidirectional Fusion](https://proceedings.mlr.press/v306/chen26bw.html) | 口袋与配体双向融合 | 将残基超图与原子级几何编码成口袋表征，让口袋与候选分子序列的特征分别作为查询做门控交叉注意力。把口袋查询得到的全局向量广播到各序列位置，再与逐位置融合结果相加以引导 SMILES 生成。 |
| <a id="chen26fr-modules"></a>[PCRNet: Phase-aware Complex Refinement Network for EEG-based Auditory Attention Decoding](https://proceedings.mlr.press/v306/chen26fr.html) | 脑电信号的复数频谱细化 | 对脑电特征做二维傅里叶变换，用独立卷积分支处理实部和虚部，以幅值谱生成的门控同时筛选两个分支，再逆变换并与时域卷积特征融合。该设计在文中的 0.1 秒听觉注意解码实验中仍有改善。 |
| <a id="coscia26a-modules"></a>[BLIPs: Bayesian Learned Interatomic Potentials](https://proceedings.mlr.press/v306/coscia26a.html) | 原子间势的自适应贝叶斯失活 | 在消息传递层用高斯变分后验表示权重，由边特征决定消息网络的方差尺度，由节点特征决定更新网络的方差尺度。借助局部重参数化采样，可同时估计原子体系能量、力及其不确定性。 |
| <a id="gao26ap-modules"></a>[Learning the Interaction Prior for Protein-Protein Interaction Prediction: A Model-Agnostic Approach](https://proceedings.mlr.press/v306/gao26ap.html) | 用虚拟三跳路径编码蛋白交互先验 | 由两个蛋白的表征生成带受控数量三跳路径的提示图，把交互预测转为图级分类。该分类头可接到现有蛋白编码器上，显式利用多条三跳路径与相互作用相关的先验。 |

<a id="by-loss-functions"></a>

### 损失函数

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="abijuru26b-loss-functions"></a>[Heavy-tailed Physics-Informed Neural Networks](https://proceedings.mlr.press/v306/abijuru26b.html) · [论文卡](../conferences/icml-2026/cards/0001-0100.md#paper-abijuru26b) | 鲁棒损失 | 把物理残差建模为 Student-t，通过 EM 自适应调低极端残差在加权 MSE 中的影响。 |
| <a id="anwer26a-loss-functions"></a>[Certificates for Complex-Compatible Learned Cochain Laplacians](https://proceedings.mlr.press/v306/anwer26a.html) · [论文卡](../conferences/icml-2026/cards/0101-0200.md#paper-anwer26a) | 网格算子学习 | 给学习出的算子对测量其偏离链复形一致性的距离，并可闭式投影到最近的兼容算子，避免网格细化时条件数失控。 |
| <a id="byeon26a-loss-functions"></a>[HEXST: Hexagonal Shifted-Window Transformer for Spatial Transcriptomics Gene Expression Prediction](https://proceedings.mlr.press/v306/byeon26a.html) | 空间转录组预测 | 针对组织切片上六角排列的采样点，用几何匹配的窗口和位置编码，再加局部差分损失，减轻逐点回归导致的基因表达过平滑。 |
| <a id="chasmai26a-loss-functions"></a>[MetaPerch: Learning from metadata for bioacoustics foundation models](https://proceedings.mlr.press/v306/chasmai26a.html) | 生物声学辅助监督 | 把录音已有的时间和位置元数据作为辅助学习目标，借物种与环境的相关性塑造表征，并分别测地理和声学域偏移。 |
| <a id="chen26y-loss-functions"></a>[SGERA: Stein-Guided ECG-Report Alignment for ECG Representation Learning](https://proceedings.mlr.press/v306/chen26y.html) | 心电与报告对齐 | 分别用 Stein 核约束单条心电与报告的匹配及跨样本的整体分布，再用难例匹配细化边界，弥补单一对比损失只监督样本对的不足。 |
| <a id="chen26at-loss-functions"></a>[FACT: Fuzzy Alignment with Comorbidity Topology for Reliable Multi-Label Medical Image Diagnosis](https://proceedings.mlr.press/v306/chen26at.html) | 共病多标签表征 | 让同一局部视觉证据以模糊隶属度支持多个疾病概念，再按共病关系组织概念锚点，避免硬分类边界抹掉可共享的病征。 |
| <a id="chen26fk-loss-functions"></a>[Self-Supervised Dynamical System Representations for Physiological Time-Series](https://proceedings.mlr.press/v306/chen26fk.html) | 生理时序的跨窗重建监督 | 用同一动力过程的一个窗口估计系统表征，再让该表征参与重建另一个窗口。跨窗共享的生成规律可以帮助重建，各窗口独有的初值和过程噪声难以迁移，从而促使编码器保留可迁移信息。 |
| <a id="chowdhury26b-loss-functions"></a>[S2M-Net: Spectral-Spatial Mixing with Morphology-Aware Adaptive Loss for Medical Image Segmentation](https://proceedings.mlr.press/v306/chowdhury26b.html) | 医学分割的形态自适应损失 | 从真值掩码计算管状程度、紧致度、边界不规则性和相对面积，用这些量逐样本调节区域、边界等损失的权重，并与数据集层面学习的权重结合。 |
| <a id="ding26w-loss-functions"></a>[Physics-informed Neural Operator Learning for Nonlinear Grad-Shafranov Equation](https://proceedings.mlr.press/v306/ding26w.html) | 固定边界等离子体平衡监督 | 求解非线性 Grad–Shafranov 方程时，将少量求解器平衡场作为监督锚点，与离散方程残差共同训练神经算子。实验中，锚点有助于避开错误解支，联合训练则减轻跨形状与多参数偏移的尾部误差。 |
| <a id="eberhard26a-loss-functions"></a>[Derivative Informed Learning of Exchange-Correlation Functionals](https://proceedings.mlr.press/v306/eberhard26a.html) | 交换关联泛函的导数监督 | 在能量、电子密度监督之外，对可容许密度矩阵的 Grassmann 流形切方向匹配参考泛函的梯度及 Hessian。前两阶响应匹配训练泛函在自洽解附近的变化，且论文观察到 Hessian 监督改善 TDDFT 激发能预测。 |
| <a id="estevez26b-loss-functions"></a>[CellBRIDGE: Learning Cellular Trajectories via Interaction-Aware Alignment](https://proceedings.mlr.press/v306/estevez26b.html) | 保留配体受体关系的细胞传输 | 用发送细胞的配体活性与接收细胞的受体活性构成有向多类型交互张量，在融合 Gromov–Wasserstein 对齐中同时比较表达特征和这些交互结构，以连接不同时间的单细胞快照。 |

<a id="by-optimization"></a>

### 优化

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="chen26ck-optimization"></a>[Learning-Guided Integration Contours Construction for Fast Large-Scale Generalized Eigensolvers](https://proceedings.mlr.press/v306/chen26ck.html) | 广义特征值积分轮廓 | 对厄米广义特征值问题，先用神经算子快速预测实谱，再用核密度估计找出谱簇间的低密度谷底，以此划分积分轮廓并预留边距。目标特征值由后续围道积分求解器计算。 |
| <a id="chen26fx-optimization"></a>[LABO: LLM-Accelerated Bayesian Optimization through Broad Exploration and Selective Experimentation](https://proceedings.mlr.press/v306/chen26fx.html) | 语言模型预测与真实实验的门控 | 用高斯过程分别建模语言模型的低成本预测以及它与真实实验的偏差。贝叶斯优化选点后，只有偏差项占预测方差的比例超过阈值才调用昂贵实验，其余位置用低成本预测更新代理。 |
| <a id="du26n-optimization"></a>[Plug-and-Play Diffusion Meets ADMM: Dual-Variable Coupling for Robust Medical Image Reconstruction](https://proceedings.mlr.press/v306/du26n.html) | 扩散重建的对偶反馈与频谱均衡 | 用 ADMM 的对偶变量累积测量一致性与去噪先验的失配。送入预训练去噪器前，估计残差功率谱并在能量不足的频段补噪，使输入残差更接近去噪器预期的白噪声。 |
| <a id="estevez26a-optimization"></a>[Automatic Construction of Clinical Scoring Systems with LLM Agents](https://proceedings.mlr.press/v306/estevez26a.html) | 临床二元规则的等权清单搜索 | 用语言模型按预定义语法提议可执行的二元规则，再用数据检验区分度和规则冗余并筛成有长度上限的等权清单，最后选择总分阈值。 |
| <a id="fink26a-optimization"></a>[RAPNet: Accelerating Algebraic Multigrid with Learned Sparse Corrections](https://proceedings.mlr.press/v306/fink26a.html) | 代数多重网格的稀疏粗层修正 | 用若干标准多重网格循环生成高频成分已衰减的残差，以此学习稀疏粗层算子修正。神经网络只在求解器初始化时运行，迭代阶段仍用稀疏算子计算。 |
| <a id="gao26j-optimization"></a>[Excited Pfaffians: Generalized Neural Wave Functions Across Structure and State](https://proceedings.mlr.press/v306/gao26j.html) | 量子激发态的多态重要性采样 | 将同一分子结构下各态的采样密度混合作为共同提议，用混合密度重加权估计任意两态波函数的重叠。这样每对重叠都能复用所有态的样本，通过共享神经网络降低跨态求值开销。 |
| <a id="goffinet26b-optimization"></a>[Torus Graphs for Large Scale Neural Phase Analysis](https://proceedings.mlr.press/v306/goffinet26b.html) | 大规模神经振荡相位图的随机分数匹配 | 将环面图分数匹配的二次型改写为充分统计量雅可比与参数向量乘积的平方范数，利用局部相位导数的稀疏性按小批更新。每步成本降为相位变量数的平方，使上千维相位耦合和动态扩展可算。 |
| <a id="guoze26a-optimization"></a>[Geometry-Aware Neural Optimizer for Shape Optimization and Inversion](https://proceedings.mlr.press/v306/guoze26a.html) | 几何潜变量到 PDE 场的可微优化 | 在预测物理场的代理模型中，把形状潜向量经门控残差注入切片 token，使场目标可以直接反传到几何表示。优化时对白名单以外的部位用零空间约束控制形变，支持局部形状调整。 |
| <a id="gutjahr26a-optimization"></a>[Constrained Flow Optimization via Sequential Fine-Tuning for Molecular Design](https://proceedings.mlr.press/v306/gutjahr26a.html) | 约束分子生成的顺序微调 | 将奖励与约束超额的增广拉格朗日惩罚合成当轮微调目标，采样估计平均违约后再调乘子和惩罚强度，让通用生成微调器逐轮兼顾分子效用与可合成性。 |
| <a id="haddadnia26a-optimization"></a>[Target-Aware Bandit Allocation for Scalable Surrogate Optimization in Chemical Space](https://proceedings.mlr.press/v306/haddadnia26a.html) | 分区赌博机分配化学筛选预算 | 把分子库按特征分簇并将簇视为臂，每轮只在选中的簇上运行全局代理模型的获取函数，再用实际评估的批均值更新臂选择，可省去逐轮全库打分。 |

<a id="by-reinforcement-learning"></a>

### 强化学习方法

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="behzadifar26a-reinforcement-learning"></a>[DecAEvolve: Decompose, Adapt, and Evolve for Effective LLM-based Scientific Equation Discovery](https://proceedings.mlr.press/v306/behzadifar26a.html) | 科学方程发现 | 把候选方程拆成符号项提供细粒度反馈，再用测试时强化学习更新假设生成器，让后续搜索利用当前系统的观测与误差。 |
| <a id="butbaia26a-reinforcement-learning"></a>[Hierarchical Reinforcement Learning for Sparse-Reward Search in Commutative Algebra](https://proceedings.mlr.press/v306/butbaia26a.html) | 数学反例搜索 | 把构造代数反例建成稀疏奖励的图搜索，使用受约束的多步选项与等变图策略，在长搜索中学习可复用的时间抽象。 |
| <a id="chang26g-reinforcement-learning"></a>[RetrOrchestrator: A Multi-Step Retrosynthesis Agent Dynamically Orchestrating Single-Step Transition Models](https://proceedings.mlr.press/v306/chang26g.html) | 逆合成搜索工具选择 | 搜索时同时决定展开哪个分子、调用哪个单步逆合成模型。用基于分子骨架的强化学习按局面路由，可利用各模型的互补能力。 |
| <a id="chen26gv-reinforcement-learning"></a>[Token-Sparse Medical Multimodal Reasoning via Dual-Stream Reinforcement Learning](https://proceedings.mlr.press/v306/chen26gv.html) | 医学视觉定位与稀疏推理 | 让同一策略先在医学图像上定位相关区域，再用裁剪后的视觉词元回答问题。顺序优化两分支并互用答题正确性奖励，使定位步骤得到所保留证据能否支撑答案的反馈。 |
| <a id="deng26y-reinforcement-learning"></a>[LASER: Learning Active Sensing for Continuum Field Reconstruction](https://proceedings.mlr.press/v306/deng26y.html) | 连续物理场重建的主动传感 | 从稀疏在线观测编码场的潜状态，再用扩散动力学预测未来场状态。策略基于潜空间前瞻估计候选传感器位置对重建精度的影响，学习把传感器移向当前尚未充分观测的区域。 |
| <a id="flynn26a-reinforcement-learning"></a>[GenCircuit-RL: Reinforcement Learning from Hierarchical Verification for Genetic Circuit Design](https://proceedings.mlr.press/v306/flynn26a.html) | 遗传电路代码的分层验证奖励 | 把代码执行、结构约束和功能表现拆成分层评分，高层奖励受低层检查结果门控。训练课程逐阶段从基础格式移到功能正确性，以缓解一次性成败反馈稀疏的问题。 |
| <a id="gao26c-reinforcement-learning"></a>[Salus: Strategic Diagnostic Testing for Complex Diagnosis via Multi-Agent Reinforcement Learning](https://proceedings.mlr.press/v306/gao26c.html) | 序贯诊断的分角色奖励 | 在模拟诊断环境里分开生成鉴别诊断、决定何时停止和提出下一项检查。对早期鉴别诊断按正确疾病在前三位的排名给分，并单独惩罚控制器过早停止，为终局诊断前的动作提供更密集的训练反馈。 |
| <a id="gu26b-reinforcement-learning"></a>[CSG: Cognitive Structure Generation for Intelligent Education](https://proceedings.mlr.press/v306/gu26b.html) | 学生认知图的分层去噪奖励 | 把学生概念关系图的反向去噪视作策略，按照 SOLO 层级评价去噪后图中与下一道实际作答有关的概念和关系。分层奖励使生成图可独立于具体下游预测器学习。 |

<a id="by-training-strategies"></a>

### 训练策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="cao26r-training-strategies"></a>[TD3B: Transition-Directed Discrete Diffusion for Allosteric Binder Generation](https://proceedings.mlr.press/v306/cao26r.html) | 变构蛋白结合物生成 | 将预测激动或拮抗方向的信号与软亲和门控分开，用两者微调离散扩散，使生成目标能区分作用方向和静态结合强度。 |
| <a id="charles26a-training-strategies"></a>[Tokenised Flow Matching for Hierarchical Simulation Based Inference](https://proceedings.mlr.press/v306/charles26a.html) | 层级仿真推断 | 先从单站点仿真学习因子化似然，再拼出多站点合成观测训练完整层级后验，可减少每个训练样本需要调用仿真器的次数。 |
| <a id="chen26ao-training-strategies"></a>[EMFormer: Efficient Multi-Scale Transformer for Accumulative Context Weather Forecasting](https://proceedings.mlr.press/v306/chen26ao.html) | 长时天气预测 | 渐进增加模型可见的累积历史做微调，减轻长时预测误差累积，并用动态加权的组合损失平衡长短预测目标。 |
| <a id="consens26a-training-strategies"></a>[Predicting evolutionary rate as a pretraining task improves genome language model representations](https://proceedings.mlr.press/v306/consens26a.html) | 基因组模型的进化速率监督 | 将单碱基 PhyloP 分数用作进化速率预训练目标，与序列重建联合优化。对调控基因组和变异效应基准，这种监督为序列重建提供了额外的保守性信号。 |
| <a id="deng26o-training-strategies"></a>[Discrete Survival Knowledge Distillation for Competing Risks Analysis](https://proceedings.mlr.press/v306/deng26o.html) | 竞争风险的离散危险率蒸馏 | 将每个时间区间内各事件发生及无事件的概率组成多项分布，只在个体仍处于风险集的区间计算师生 KL 散度，并把它加入本地生存似然。可用教师预测作监督，保留删失观测下的风险集结构。 |
| <a id="deng26p-training-strategies"></a>[Component-Wise Composite Likelihood Distillation for Censored Time-to-Event Data](https://proceedings.mlr.press/v306/deng26p.html) | 删失数据的分量似然蒸馏 | 在复合似然的每个可比较样本集合内，对教师风险分数指数化并归一化，再用该分量上的 KL 散度对齐学生分布。教师只需给出样本风险分数，即可用于 Cox 等仅有部分似然的情形。 |
| <a id="diaconu26a-training-strategies"></a>[Probabilistic Retrofitting of Learned Simulators](https://proceedings.mlr.press/v306/diaconu26a.html) | 确定性 PDE 模拟器的概率改造 | 把每个集合成员的低维高斯噪声映射为跨空间共享的条件归一化调制量，再用公平版 CRPS 微调预测集合。预训练主干用较小学习率，新增噪声支路用较大学习率，以利用原有动力学表征。 |
| <a id="gao26s-training-strategies"></a>[MedCRP-CL: Continual Medical Image Segmentation via Bayesian Nonparametric Semantic Modality Discovery](https://proceedings.mlr.press/v306/gao26s.html) | 医学分割任务的在线分簇适配 | 用中国餐馆过程从新增任务的临床提示推断它应加入已有语义簇还是新建一簇。簇间独立保存低秩适配器，簇内共享参数并用弹性权重巩固减轻遗忘。 |
| <a id="gao26v-training-strategies"></a>[Scaling the Prior: Size-Consistent Geometric Diffusion for 3D Molecular Generation](https://proceedings.mlr.press/v306/gao26v.html) | 按原子数缩放分子扩散先验 | 让坐标的高斯噪声方差随原子数调整，同时维持原子类别通道的噪声规则，以校准不同大小分子的坐标尺度与噪声之比，使粗结构在更一致的去噪阶段形成。 |
| <a id="garnier26a-training-strategies"></a>[Mesh Based Simulations with Spatial and Temporal awareness](https://proceedings.mlr.press/v306/garnier26a.html) | 网格模拟的模板监督与时序校正 | 用节点邻接模板内的一组场值做联合监督，约束局部空间差分，再以跨时间注意力执行预测与校正。把这两项加入不同网格代理后，论文观察到长程滚动误差累积变慢。 |
| <a id="guan26j-training-strategies"></a>[Federated Multi-view Clustering for Remote Sensing Data](https://proceedings.mlr.press/v306/guan26j.html) | 遥感多视图聚类的原型对齐 | 各客户端从配准样本的软分配中找簇的共现模式，用这些模式校正独立建模造成的簇编号错位。客户端交换加噪原型，并用分布间 Wasserstein 距离对齐异构视图中的簇。 |
| <a id="guo26c-training-strategies"></a>[MutAtlas: A PDB-Wide Energy-Guided Atlas of Protein Mutation Effects](https://proceedings.mlr.press/v306/guo26c.html) | 蛋白突变的多源相对偏好蒸馏 | 枚举结构上同一残基的替换候选，先在各来源内归一化两种替换的得分差，再按支持同一排序方向的来源数加权。可同时利用能量模型、蛋白语言模型和逆折叠模型的相对判断。 |
| <a id="han26j-training-strategies"></a>[Expert-level Leaf Cell Layout Generation via Preference-Optimized LLM](https://proceedings.mlr.press/v306/han26j.html) | 用性能偏好训练单元版图脚本生成 | 以贝叶斯优化弥补人工版图缺少对应脚本的问题，构造可运行的脚本和版图配对。再用性能感知嵌入衡量生成结果与参考版图的接近程度，为监督微调后的偏好训练提供信号。 |

<a id="by-data-strategies"></a>

### 数据策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="brockschmidt26a-data-strategies"></a>[SurvDiff: A Diffusion Model for Generating Synthetic Data in Survival Analysis](https://proceedings.mlr.press/v306/brockschmidt26a.html) | 生存分析合成数据 | 联合生成协变量、事件时间和右删失标记，并把生存任务结构写进扩散损失，避免合成表格只拟合协变量却丢失删失机制。 |
| <a id="chan26a-data-strategies"></a>[DC-W2S: Dual-Consensus Weak-to-Strong Training for Reliable Process Reward Modeling in Biological Reasoning](https://proceedings.mlr.press/v306/chan26a.html) | 过程奖励数据筛选 | 同时用弱标注者之间的一致性与嵌入近邻的一致性评估逐步标签，再按可靠性采样例子并遮蔽可疑标签。 |
| <a id="cranganore26a-data-strategies"></a>[ANTiC: Adaptive Neural Temporal In Situ Compressor](https://proceedings.mlr.press/v306/cranganore26a.html) | 物理仿真的流式快照压缩 | 仿真运行时用涡量平方积分等物理指标监测变化，以滑窗中的自适应阈值选择快照。对选中快照沿用上一帧的神经场，通过低秩参数更新编码变化，避免先落盘整段轨迹。 |
| <a id="d-ascenzo26a-data-strategies"></a>[scDataset: Scalable Data Loading for Deep Learning on Large-Scale Single-Cell Omics](https://proceedings.mlr.press/v306/d-ascenzo26a.html) | 单细胞训练的块采样与批量预取 | 随机抽取连续磁盘块并一次预取多个小批次的细胞，再在内存打乱和分批。块读取减少随机 I/O，跨块打乱则让单个训练批次能混合更远的磁盘位置，缓解连续读取引入的相关性。 |
| <a id="geenjaar26a-data-strategies"></a>[A robust PPG foundation model using multimodal physiological supervision](https://proceedings.mlr.press/v306/geenjaar26a.html) | 用同步心电和呼吸筛选 PPG 对比样本 | 从与 PPG 同步记录的心电和呼吸窗口提取生理指标，按这些指标的相似性选取对比样本。预训练可保留含噪的 PPG 窗口，部署时只需 PPG 输入，论文在未见的可穿戴数据上验证了迁移能力。 |

<a id="by-inference"></a>

### 推理策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="aich26a-inference"></a>[WIND: Weather Inverse Diffusion for Zero-Shot Atmospheric Modeling](https://proceedings.mlr.press/v306/aich26a.html) · [论文卡](../conferences/icml-2026/cards/0001-0100.md#paper-aich26a) | 大气生成模型 | 用无条件大气视频扩散模型学习通用先验，将预报、降尺度和稀疏观测重建分别写成逆问题，在推理时做后验采样。 |
| <a id="andrae26a-inference"></a>[DAISI: Data Assimilation with Inverse Sampling using Stochastic Interpolants](https://proceedings.mlr.press/v306/andrae26a.html) · [论文卡](../conferences/icml-2026/cards/0001-0100.md#paper-andrae26a) | 数据同化 | 先用逆向采样把预报信息注入固定生成先验，再用观测引导条件采样。预报器可替换，生成先验无需逐轮重训。 |
| <a id="baker26a-inference"></a>[Supervised Guidance Training for Infinite-Dimensional Diffusion Models](https://proceedings.mlr.press/v306/baker26a.html) | 函数空间逆问题 | 用无限维 Doob h 变换把后验分数拆成无条件分数与观测引导项，只训练引导分量即可复用函数空间的扩散先验。 |
| <a id="bohde26a-inference"></a>[FRIGID: Scaling Diffusion-Based Molecular Generation from Mass Spectra at Training and Inference Time](https://proceedings.mlr.press/v306/bohde26a.html) | 质谱到分子生成 | 用正向碎裂模型找出候选分子中与观测质谱不符的局部片段，只重掩码并去噪这些片段，随推理预算逐步纠偏。 |
| <a id="cao26c-inference"></a>[Chamaileon: Cross-Context Binder Design with Contextualized Modeling and Mixed Sampling](https://proceedings.mlr.press/v306/cao26c.html) | 蛋白结合物设计 | 联合学习不同结合环境下的序列与结构，再在推理时混合多个环境的采样路径，以搜索同一条能适配多目标或多构象的序列。 |
| <a id="chen26bu-inference"></a>[Towards Docking-oriented De Novo Ligand Design via Gradient Inversion](https://proceedings.mlr.press/v306/chen26bu.html) | 对接预测梯度反演 | 把训练好的可微对接模型用作生成时的评分器，对候选配体的连续坐标和特征反传预测目标的梯度，每步投影回可行集合，最后按小分子或蛋白质配体的约束解码。 |
| <a id="chen26gs-inference"></a>[Coarse-Grained Boltzmann Generators](https://proceedings.mlr.press/v306/chen26gs.html) | 粗粒化玻尔兹曼重要性采样 | 增强采样偏置只依赖粗粒化坐标时，给定该坐标的原子构型条件分布保持不变，因此可用重新计算的无偏投影力拟合平均力势。随后用其玻尔兹曼权重与流模型密度的比值重加权，平衡统计的准确性取决于势的拟合质量。 |
| <a id="datta26a-inference"></a>[Agentic Framework for Epidemiological Modeling](https://proceedings.mlr.press/v306/datta26a.html) | 流行病模拟器的流图验证 | 先从场景描述生成包含舱室与转移的流图，检查转移合法性以及与免疫衰减、疫苗接种等假设的一致性，再将通过验证的图编译成待校准的动力系统。 |
| <a id="de-campos26a-inference"></a>[Generative Inverse Design with Abstention via Diagonal Flow Matching](https://proceedings.mlr.press/v306/de-campos26a.html) | 逆设计流的零锚定置信度 | 流匹配训练时让设计坐标和噪声成对，让性能标签连到零。反向生成候选时可直接用应归零的坐标残差衡量不确定性，再用正向重建目标的误差复核候选。 |
| <a id="ding26a-inference"></a>[Listening Through the Noise: Cauchy-Driven Diffusion Bridges for Robust Gastrointestinal Auscultation and Clinical Benchmarking](https://proceedings.mlr.press/v306/ding26a.html) | 重尾扩散桥的肠鸣音分离 | 用 Cauchy 驱动的扩散桥建模受干扰音频到干净肠鸣音的恢复。采样时把重尾项实现为随机尺度的高斯噪声，使条件尺度固定时能沿用高斯桥的闭式反向更新。 |
| <a id="gallon26a-inference"></a>[Physics-Informed Diffusion Models in Spectral Space](https://proceedings.mlr.press/v306/gallon26a.html) | 谱空间扩散的 PDE 后验引导 | 用截断并缩放的 Fourier 系数联合表示 PDE 参数和解，在谱系数上学习扩散先验。推理时对去噪估计做逆变换，把稀疏观测误差和 PDE 残差的梯度反馈到采样中，以同一先验处理正问题和逆问题。 |
| <a id="gan26b-inference"></a>[SKETCH: Semantic Key-Point Conditioning for Long-Horizon Vessel Trajectory Prediction](https://proceedings.mlr.press/v306/gan26b.html) | 港口和航路节点条件下的航迹外推 | 从历史航迹检索和核验参考航迹，先估计船只接下来可能经过的港区、海峡或航路节点，再以该关键点约束局部运动预测。把远期导航意图与短期运动分开，可减小长时外推的方向漂移。 |
| <a id="gao26p-inference"></a>[Residual-Guided Multi-Resolution Refinement of Foundation Models: A Case Study in Drought Forecasting](https://proceedings.mlr.press/v306/gao26p.html) | 干旱预测的多分辨率残差校正 | 在多个时间分辨率上调用冻结的时序模型，以粗尺度预测为起点，用历史回测训练的残差估计来调节粗预测与细尺度结果的融合，逐级修正干旱指数预测。 |
| <a id="ge26b-inference"></a>[Thinking in Scales: Accelerating Gigapixel Pathology Image Analysis via Adaptive Continuous Reasoning](https://proceedings.mlr.press/v306/ge26b.html) | 超大病理切片的动态倍率推理 | 先在低倍率定位候选区域，再用注意力剪枝选择需要高倍率查看的局部，并在预测熵足够低时提前停止。论文在所测切片数据上维持相近 AUC，同时显著减少需要编码的图块。 |
| <a id="giral26a-inference"></a>[GenDA: Generative Data Assimilation on Complex Urban Areas via Classifier-Free Diffusion Guidance](https://proceedings.mlr.press/v306/giral26a.html) | 稀疏传感条件下的城市风场扩散 | 在粗细两层网格传播观测信息，细网格保留建筑附近梯度，粗网格连接远处区域。生成时组合学习几何先验的无传感分支与传感条件分支，用同一采样流程同化固定点或沿轨迹获取的观测。 |
| <a id="han26g-inference"></a>[Smooth Dynamic Cutoffs for Machine Learning Interatomic Potentials](https://proceedings.mlr.press/v306/han26g.html) | 原子势的平滑动态截断 | 按局部邻居密度调整作用半径，并将边贡献平滑衰减到零，近似维持固定邻居预算。这样可减少稠密构型中的图边数和显存，在所测分子动力学系统中仍能长时稳定滚动。 |

<a id="by-representation-learning"></a>

### 表征学习

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="abulikemu26a-representation-learning"></a>[Geometry-Guided Generative Representation for Functional Brain Graphs](https://proceedings.mlr.press/v306/abulikemu26a.html) · [论文卡](../conferences/icml-2026/cards/0001-0100.md#paper-abulikemu26a) | 图表征学习 | 用跨样本对齐的功能梯度作为图自编码器的几何先验，再在压缩的图级潜空间建模。 |
| <a id="antoniadis26a-representation-learning"></a>[Protein Language Model Embeddings Improve Generalization of Implicit Transfer Operators](https://proceedings.mlr.press/v306/antoniadis26a.html) · [论文卡](../conferences/icml-2026/cards/0101-0200.md#paper-antoniadis26a) | 分子动力学泛化 | 在粗粒化的隐式转移算子中加入蛋白语言模型嵌入作为条件，可改善对未见过蛋白的平衡态采样。 |
| <a id="ariguib26a-representation-learning"></a>[Learning the Neighborhood: Contrast-Free Multimodal Self-Supervised Molecular Graph Pretraining](https://proceedings.mlr.press/v306/ariguib26a.html) · [论文卡](../conferences/icml-2026/cards/0101-0200.md#paper-ariguib26a) | 分子自监督 | 用固定半径子图作训练单元，从互补邻域预测其潜嵌入，把同一分子的多种 3D 构象引入免负样本训练。 |
| <a id="baloch26a-representation-learning"></a>[A Machine-Learned Comorbidity Index](https://proceedings.mlr.press/v306/baloch26a.html) | 多结局风险表征 | 用归一化 Hilbert–Schmidt 独立性准则将诊断编码压成一个非线性分数，使其共同反映多个结局的风险。 |
| <a id="chen26u-representation-learning"></a>[Foundation VAEs for CT Reconstruction, Augmentation, and Generation](https://proceedings.mlr.press/v306/chen26u.html) | 医学图像潜空间复用 | 自然图像和视频上预训练的 VAE 可以冻结后用于 CT 重建，再在同一潜空间训练条件扩散，复用编码器做重建、增强和生成。 |
| <a id="chen26ay-representation-learning"></a>[MolAlign3D: Enhancing Fixed-Dimensional E(3)-Equivariant Latent Space for High-Fidelity 3D Molecular Reconstruction and Editing](https://proceedings.mlr.press/v306/chen26ay.html) | 三维分子表征 | 在固定维的 E(3) 等变几何潜空间里加上预训练分子编码器的语义锚点，可保留重建精度，同时改善改变原子数等零样本编辑。 |
| <a id="chen26ct-representation-learning"></a>[SLAE: Strictly Local All-atom Environment for Protein Representation](https://proceedings.mlr.press/v306/chen26ct.html) | 蛋白质局部全原子表征 | 以残基附近的重原子类型和相对几何构建局部表征，同时监督全原子坐标重建、氨基酸识别和 Rosetta 相互作用能回归，让表征同时保留侧链几何和局部化学环境。 |
| <a id="chen26db-representation-learning"></a>[Protein Fold Classification at Scale: Benchmarking and Pretraining](https://proceedings.mlr.press/v306/chen26db.html) | 高掩码蛋白质结构预训练 | 随机掩去最高 90% 的残基，以 SE(3) 不变编码器处理可见结构，让轻量解码器重建骨架坐标。在去冗余的 TEDBench 上，这种自监督表征提升了折叠拓扑分类表现。 |
| <a id="cheng26m-representation-learning"></a>[Physics-Informed Pre-training on Efficient Electron-Density Images for Organic Material Property Prediction](https://proceedings.mlr.press/v306/cheng26m.html) | 多视角电子密度图表征 | 把三维电子密度转为多视角图像，共享视觉编码器提取各视角特征后池化，并用跨尺度物理任务预训练。论文在有机光伏和发色团数据上验证了这种输入在降低电子密度建模成本的同时仍能预测材料属性。 |
| <a id="dilip26a-representation-learning"></a>[Adaptive Protein Tokenization](https://proceedings.mlr.press/v306/dilip26a.html) | 蛋白结构的可截断全局分词 | 训练时随机截断蛋白结构量化 token 序列的后缀，并用保留的前缀调节流匹配解码器。这样早期 token 优先承载大小和整体结构等信息，追加 token 可逐步恢复更多几何细节。 |
| <a id="du26f-representation-learning"></a>[BioFormer: Rethinking Cross-Subject Generalization via Spectral Structural Alignment in Biomedical Time-Series](https://proceedings.mlr.press/v306/du26f.html) | 生理时序的分频幅相对齐 | 对生理时间序列特征做傅里叶变换，从样本频谱生成各频带的调制量，分别调整振幅和相位。以频带而非单个频点为单位对齐，减轻受试者间幅相差异对分类的影响。 |
| <a id="gelard26a-representation-learning"></a>[Bimodal masked language modeling for bulk RNA-seq and DNA methylation representation learning](https://proceedings.mlr.press/v306/gelard26a.html) | 转录组与甲基化的双模态掩码学习 | 将配对样本的基因表达量和甲基化量离散化，两种模态用各自的输出头预测被扰动的数值词元，以联合自监督学习肿瘤样本的表征。论文以癌种分类和生存预测验证表征的迁移效果。 |
| <a id="guo26a-representation-learning"></a>[SIGMA-PPG: Statistical-prior Informed Generative Masking Architecture for PPG Foundation Model](https://proceedings.mlr.press/v306/guo26a.html) | 脉搏波词元的语义一致量化 | 对脉搏波片段加入缩放和高斯扰动，在量化前约束增强片段的编码接近原片段编码。该约束和频谱重建一起训练词元器，使轻微采集变化更少产生重复的码本项。 |
| <a id="han26f-representation-learning"></a>[Learning Permutation-invariant Macroscopic Dynamics](https://proceedings.mlr.press/v306/han26f.html) | 无序微观系统的宏观状态表征 | 用置换不变编码器压缩粒子集合，并让解码器重建观测点周围的质量分布，取消逐点对应的要求。再与宏观可观测量的动力学联合学习，可跟踪粒子次序任意变化时的群体演化。 |

<a id="by-evaluation"></a>

### 评测与诊断

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="ahamed26a-evaluation"></a>[TFRBench: A Reasoning Benchmark for Evaluating Forecasting Systems](https://proceedings.mlr.press/v306/ahamed26a.html) · [论文卡](../conferences/icml-2026/cards/0001-0100.md#paper-ahamed26a) | 时间序列预测评测 | 给预测器的解释也打分，检查跨变量依赖、趋势和外部事件，并用数值核验循环构造有数据依据的推理轨迹。 |
| <a id="alfarano26a-evaluation"></a>[Improving ML Attacks on LWE with Data Repetition and Stepwise Regression](https://proceedings.mlr.press/v306/alfarano26a.html) · [论文卡](../conferences/icml-2026/cards/0001-0100.md#paper-alfarano26a) | 格密码机器学习分析 | 在论文测试的 LWE 参数内，重复训练样本与扩充数据都能帮助恢复更密集的秘密向量，逐步回归则用于更易识别的一部分分量。 |
| <a id="amalan26a-evaluation"></a>[MalTree: Tracing Malware Evolution from Embeddings at Scale](https://proceedings.mlr.press/v306/amalan26a.html) · [论文卡](../conferences/icml-2026/cards/0001-0100.md#paper-amalan26a) | 恶意软件谱系重建 | 从多种恶意软件特征构建进化树，并用样本时间戳验证推断的祖先后代关系，可以比较不同家族的演化速度。 |
| <a id="bahrini26a-evaluation"></a>[When Can We Trust Survival Model Evaluation ?](https://proceedings.mlr.press/v306/bahrini26a.html) · [论文卡](../conferences/icml-2026/cards/0101-0200.md#paper-bahrini26a) | 生存模型评测 | 用未删失的完整事件时间作为基准，分别核对删失如何影响指标数值和模型排序。指标偏差适中也可能伴随排序失真。 |
| <a id="bai26a-evaluation"></a>[Op-CAD: Benchmarking and Investigating Operation-oriented CAD Generation](https://proceedings.mlr.press/v306/bai26a.html) · [论文卡](../conferences/icml-2026/cards/0101-0200.md#paper-bai26a) | CAD 操作评测 | 用几何引导解析把建模序列切成单个操作，并用倒角和圆角专用的 CF-IoU 检查局部改动，避免整体形状相近掩盖操作错误。 |
| <a id="becktepe26a-evaluation"></a>[Plug-and-Play Benchmarking of Reinforcement Learning Algorithms for Large-Scale Flow Control](https://proceedings.mlr.press/v306/becktepe26a.html) | 流体控制强化学习 | 把可微 GPU 流体求解器和环境统一在 PyTorch 栈内，固定观测、执行和评测口径，让 PPO、SAC 与可微控制能直接对照。 |
| <a id="cao26g-evaluation"></a>[SimulCost: A Cost-Aware Benchmark and Toolkit for Automating Physics Simulations with LLMs](https://proceedings.mlr.press/v306/cao26g.html) | 仿真 Agent 成本评测 | 在测参成功率之外，把仿真器调用成本独立记账，并与固定扫描基线比较。论文中，多轮交互提高成功率的同时仍可能更耗时。 |
| <a id="chandok26a-evaluation"></a>[A Systematic Study of Behavioral Cloning for Scientific Data Annotation](https://proceedings.mlr.press/v306/chandok26a.html) | 科学标注行为克隆 | 用模拟的专家导航、纠错和验证轨迹研究标注策略，分开测界面操作与任务决策。多任务预训练可提升少样本新标注任务的微调效果。 |
| <a id="chen26fp-evaluation"></a>[Real-World Unsupervised Models Generalize to Predict Brain Responses to Out-of-Distribution Stimuli](https://proceedings.mlr.press/v306/chen26fp.html) | 自然感官数据的跨刺激神经预测 | 用真实环境采样训练无监督模型，再用学得的特征预测刺激诱发的皮层响应。仅用普通话训练的模型可预测英语刺激下的听觉响应，用婴儿头戴相机视频训练的模型可预测成年人观看物体图像时的视觉响应。 |
| <a id="cheng26l-evaluation"></a>[Abstraction Induces the Brain Alignment of Language and Speech Models](https://proceedings.mlr.press/v306/cheng26l.html) | 语言与语音层表征的脑响应对齐 | 逐层测量表征内在维度并预测 fMRI 和 ECoG 信号，发现高维度的中间层通常更贴合脑响应。以脑响应为目标微调时，内在维度和可解码的语义信息也随之增加。 |
| <a id="dan26a-evaluation"></a>[Quantifying the Generalization Gap in Seizure Detection: A Large-Scale Empirical Benchmark via the SzCORE Challenge](https://proceedings.mlr.press/v306/dan26a.html) | 长程脑电癫痫检测的泛化评测 | 用独立留出的连续脑电记录做容器化盲测，按发作事件及每日误报计分，并单看每名受试者的排名。该测试中最高事件 F1 为 32%，总体领先的算法在受试者之间仍有较大波动。 |
| <a id="didi26a-evaluation"></a>[FLIP2: Expanding Protein Fitness Landscape Benchmarks for Real-World Machine Learning Applications](https://proceedings.mlr.press/v306/didi26a.html) | 蛋白适应度的外推切分 | 分别按突变数、突变位置、具体替换、适应度和野生型骨架构造训练与测试切分。例如按适应度用低分变体训练、高分变体测试，可衡量模型能否外推到后续优化所需的高适应度区间。 |
| <a id="duan26f-evaluation"></a>[(Be Cautious!) Bio-Foundation Models Are Not Yet Robust to Biologically Plausible Perturbations and ML Transformations](https://proceedings.mlr.press/v306/duan26f.html) | 生物基础模型的双类扰动诊断 | 分别对蛋白结构加入未解析环缺失等生物数据扰动，并在原数据固定时改动建图的邻居数或截断半径。用边集合 Jaccard 相似度等指标量化建图变化，再与输出波动对照，可区分数据采集误差和处理流程敏感性。 |
| <a id="fa26a-evaluation"></a>[BioAgent Bench: An AI Agent Evaluation Suite for Bioinformatics](https://proceedings.mlr.press/v306/fa26a.html) | 生物信息学智能体的流程稳健性评测 | 为端到端任务指定可检查的产物，并记录运行轨迹。在损坏输入、误导文件和冗长提示下分别重测，可发现智能体虽能搭对高层流程，仍可能在具体输入取舍或错误恢复上出错。 |
| <a id="gao26ao-evaluation"></a>[TadA-Bench: A Million-Variant Benchmark for Future-Round Discovery Toward Agentic Protein Engineering](https://proceedings.mlr.press/v306/gao26ao.html) | 按轮次回放蛋白工程候选筛选 | 对齐各轮测量标签并保留真实实验时间顺序，用早期轮次的数据对后续才出现的候选排序。随机切分中表现良好的模型在未来轮次的有限预算筛选中仍明显退化，显示插值指标会高估前瞻能力。 |
| <a id="ghosh26b-evaluation"></a>[CLINIC : Evaluating Multilingual Trustworthiness in Language Models for Healthcare](https://proceedings.mlr.press/v306/ghosh26b.html) | 多语言医疗模型的分维度可信评测 | 把医疗语言模型的真实性、公平性、安全性、鲁棒性与隐私拆为 18 项任务，在 15 种语言中分层比较。论文测试显示，低资源语言在诚实性、公平性及隐私上的退化尤其明显。 |
| <a id="gokce26a-evaluation"></a>[Multimodal Scaling Laws for Task & Data-Optimized Models of Visual Cortex](https://proceedings.mlr.press/v306/gokce26a.html) | 视觉皮层映射的神经样本缩放 | 分别改变预训练规模与拟合模型到脑响应映射所用的刺激和记录配对数。所测多种记录模态中，增加配对数在考察范围内带来近似对数线性的对齐增益，而扩大预训练的收益逐渐饱和。 |
| <a id="han26v-evaluation"></a>[Benchmarking Physics-Informed Time-Series Models for Operational Global Station Weather Forecasting](https://proceedings.mlr.press/v306/han26v.html) | 站点天气预报的物理与业务对照 | 先用图动态核心生成物理引导的基线，再由 Transformer 预测残差，并约束气压风场配合和能量平滑性。对照业务数值预报时同时报告常规变量与极端事件误差，可看出学术模型在真实站点上的差距。 |

<a id="by-theory-statistics"></a>

### 理论与统计

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="antipov26a-theory-statistics"></a>[Flow-Based Density Ratio Estimation for Intractable Distributions with Applications in Genomics](https://proceedings.mlr.press/v306/antipov26a.html) · [论文卡](../conferences/icml-2026/cards/0101-0200.md#paper-antipov26a) | 密度比估计 | 用条件 flow matching 沿同一条生成轨迹追踪密度比，省去分别求两种分布似然再相除的流程。 |
| <a id="bao26a-theory-statistics"></a>[Learning Junta Distributions, Quantum Junta States, and QAC$^0$ Circuits](https://proceedings.mlr.press/v306/bao26a.html) | 量子稀疏依赖学习 | 只有 k 个相关位的经典分布可用约 2^k log(n) / ε² 个样本学习。量子态的相应结构只在 k 个量子位上偏离最大混合态，也可利用这种低维依赖。 |
| <a id="berman26a-theory-statistics"></a>[Leveraging Gauge Freedom for Learning Non-Gradient Population Dynamics of Stochastic Systems](https://proceedings.mlr.press/v306/berman26a.html) | 群体动力学反演 | 用连续性方程的弱形式约束总体分布演化，并允许非梯度速度场，可重建最小动能梯度流无法表达的输运。 |
| <a id="ding26c-theory-statistics"></a>[Disentangling Latent Risk Pathways via Bayesian Hypergraph Inference](https://proceedings.mlr.press/v306/ding26c.html) | 多病风险的贝叶斯超图 | 以潜在疾病组为超边，使某个风险因子可在多条超边上有不同效应，再汇总疾病所属超边的贡献。用分层先验分别表示超边是否存在、疾病是否属于超边及因子是否作用于超边，便于报告各项后验不确定性。 |
| <a id="ek26a-theory-statistics"></a>[Learning Treatment Allocations with Risk Control Under Partial Identifiability](https://proceedings.mlr.press/v306/ek26a.html) | 部分可识别的治疗分配风险 | 按给定的倾向赔率偏差范围为未获益治疗比例计算风险上界。先用一部分数据训练候选分配策略，再用独立样本的上置信界筛选满足风险容忍度的候选。 |
| <a id="fu26i-theory-statistics"></a>[Learning General Causal Structures with Hidden Dynamic Process for Climate Analysis](https://proceedings.mlr.press/v306/fu26i.html) | 隐藏动态过程的因果可识别性 | 把含隐藏动态驱动的非线性结构方程写成等价的非线性独立成分模型，再用雅可比的非零结构表征观测变量间因果边。在文中给定的条件变异与结构约束下，可同时识别隐藏过程的表示和观测因果图。 |
| <a id="gatzner26a-theory-statistics"></a>[Principled Confidence Estimation for Deep Computed Tomography](https://proceedings.mlr.press/v306/gatzner26a.html) | 基于物理似然的 CT 重建置信区域 | 用 Beer–Lambert 前向过程和 Poisson 观测模型计算似然，再以序贯似然混合为重建结果构造置信区域。论文在模型条件下提供覆盖保证，同一方法可比较传统重建器和深度重建器给出的区域宽度。 |
| <a id="gloeckler26a-theory-statistics"></a>[Scalable Simulation-Based Model Inference with Test-Time Complexity Control](https://proceedings.mlr.press/v306/gloeckler26a.html) | 推理时可调的模型复杂度先验 | 先从观测解码离散模型结构，再在选定结构下推断连续参数。训练时将复杂度先验强度输入两个解码器，部署时只改变该条件就能比较不同简约程度下的后验，无需重新训练。 |
| <a id="guan26a-theory-statistics"></a>[A Call to Lagrangian Action: Learning Population Mechanics from Temporal Snapshots](https://proceedings.mlr.press/v306/guan26a.html) | 从时间快照学习群体 Hamilton 动力学 | 把群体演化建模为 Wasserstein 空间中的作用量极值问题，再从多个时刻的边际分布反推 Hamilton 动力学。只需群体快照即可插值和预测分布，并能表示梯度流难以描述的周期运动。 |
<!-- classification:end -->
