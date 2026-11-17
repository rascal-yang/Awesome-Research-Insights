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

<a id="by-modules"></a>

### 模块

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="berman26d-modules"></a>[Smoothness Errors in Dynamics Models and How to Avoid Them](https://proceedings.mlr.press/v306/berman26d.html) | 网格动力学平滑 | 热扩散等过程本身需要平滑，严格酉卷积会限制这种物理变化。放松酉性可在抑制图网络过平滑的同时允许合理的平滑演化。 |

<a id="by-loss-functions"></a>

### 损失函数

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="abijuru26b-loss-functions"></a>[Heavy-tailed Physics-Informed Neural Networks](https://proceedings.mlr.press/v306/abijuru26b.html) | 鲁棒损失 | 把物理残差建模为 Student-t，通过 EM 自适应调低极端残差在加权 MSE 中的影响。 |
| <a id="anwer26a-loss-functions"></a>[Certificates for Complex-Compatible Learned Cochain Laplacians](https://proceedings.mlr.press/v306/anwer26a.html) | 网格算子学习 | 给学习出的算子对测量其偏离链复形一致性的距离，并可闭式投影到最近的兼容算子，避免网格细化时条件数失控。 |

<a id="by-reinforcement-learning"></a>

### 强化学习方法

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="behzadifar26a-reinforcement-learning"></a>[DecAEvolve: Decompose, Adapt, and Evolve for Effective LLM-based Scientific Equation Discovery](https://proceedings.mlr.press/v306/behzadifar26a.html) | 科学方程发现 | 把候选方程拆成符号项提供细粒度反馈，再用测试时强化学习更新假设生成器，让后续搜索利用当前系统的观测与误差。 |

<a id="by-inference"></a>

### 推理策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="aich26a-inference"></a>[WIND: Weather Inverse Diffusion for Zero-Shot Atmospheric Modeling](https://proceedings.mlr.press/v306/aich26a.html) | 大气生成模型 | 用无条件大气视频扩散模型学习通用先验，将预报、降尺度和稀疏观测重建分别写成逆问题，在推理时做后验采样。 |
| <a id="andrae26a-inference"></a>[DAISI: Data Assimilation with Inverse Sampling using Stochastic Interpolants](https://proceedings.mlr.press/v306/andrae26a.html) | 数据同化 | 先用逆向采样把预报信息注入固定生成先验，再用观测引导条件采样。预报器可替换，生成先验无需逐轮重训。 |
| <a id="baker26a-inference"></a>[Supervised Guidance Training for Infinite-Dimensional Diffusion Models](https://proceedings.mlr.press/v306/baker26a.html) | 函数空间逆问题 | 用无限维 Doob h 变换把后验分数拆成无条件分数与观测引导项，只训练引导分量即可复用函数空间的扩散先验。 |

<a id="by-representation-learning"></a>

### 表征学习

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="abulikemu26a-representation-learning"></a>[Geometry-Guided Generative Representation for Functional Brain Graphs](https://proceedings.mlr.press/v306/abulikemu26a.html) | 图表征学习 | 用跨样本对齐的功能梯度作为图自编码器的几何先验，再在压缩的图级潜空间建模。 |
| <a id="antoniadis26a-representation-learning"></a>[Protein Language Model Embeddings Improve Generalization of Implicit Transfer Operators](https://proceedings.mlr.press/v306/antoniadis26a.html) | 分子动力学泛化 | 在粗粒化的隐式转移算子中加入蛋白语言模型嵌入作为条件，可改善对未见过蛋白的平衡态采样。 |
| <a id="ariguib26a-representation-learning"></a>[Learning the Neighborhood: Contrast-Free Multimodal Self-Supervised Molecular Graph Pretraining](https://proceedings.mlr.press/v306/ariguib26a.html) | 分子自监督 | 用固定半径子图作训练单元，从互补邻域预测其潜嵌入，把同一分子的多种 3D 构象引入免负样本训练。 |
| <a id="baloch26a-representation-learning"></a>[A Machine-Learned Comorbidity Index](https://proceedings.mlr.press/v306/baloch26a.html) | 多结局风险表征 | 用归一化 Hilbert–Schmidt 独立性准则将诊断编码压成一个非线性分数，使其共同反映多个结局的风险。 |

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

<a id="by-theory-statistics"></a>

### 理论与统计

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="antipov26a-theory-statistics"></a>[Flow-Based Density Ratio Estimation for Intractable Distributions with Applications in Genomics](https://proceedings.mlr.press/v306/antipov26a.html) | 密度比估计 | 用条件 flow matching 沿同一条生成轨迹追踪密度比，省去分别求两种分布似然再相除的流程。 |
| <a id="bao26a-theory-statistics"></a>[Learning Junta Distributions, Quantum Junta States, and QAC$^0$ Circuits](https://proceedings.mlr.press/v306/bao26a.html) | 量子稀疏依赖学习 | 只有 k 个相关位的经典分布可用约 2^k log(n) / ε² 个样本学习。量子态的相应结构只在 k 个量子位上偏离最大混合态，也可利用这种低维依赖。 |
| <a id="berman26a-theory-statistics"></a>[Leveraging Gauge Freedom for Learning Non-Gradient Population Dynamics of Stochastic Systems](https://proceedings.mlr.press/v306/berman26a.html) | 群体动力学反演 | 用连续性方程的弱形式约束总体分布演化，并允许非梯度速度场，可重建最小动能梯度流无法表达的输运。 |
<!-- classification:end -->
