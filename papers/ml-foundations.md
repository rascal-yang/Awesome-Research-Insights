# 机器学习基础与统计

[首页](../README.md) · [English](../en/papers/ml-foundations.md)

通用学习方法、优化、学习理论与统计推断。

<!-- classification:start -->
## 按技术类型浏览

<a id="by-architecture"></a>

### 模型架构

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="agrawal26c-architecture"></a>[A Spiking Heterogeneous Harmonic Resonate-and-Fire State Space Model for Time Series](https://proceedings.mlr.press/v306/agrawal26c.html) | 脉冲状态空间模型 | 用有不同动态参数的二阶谐振脉冲单元建模长时序，核化回归版本可处理论文测试中最长 5 万步的序列。 |
| <a id="babbar26a-architecture"></a>[Falling Trees: A Model Class for Interpretable Risk Prioritization](https://proceedings.mlr.press/v306/babbar26a.html) | 可解释风险排序 | 把风险单调递减的规则列表扩展成可分叉的决策树，再用动态规划找近优解，可以增加表达力并保留优先级约束。 |
| <a id="baek26b-architecture"></a>[Learning to Theorize the World from Observation](https://proceedings.mlr.press/v306/baek26b.html) | 世界模型 | 从非文本观测中推断可以执行的潜程序，用共享转移模型运行它。重新组合学到的程序原语可以解释训练中没见过的现象。 |
| <a id="berman26c-architecture"></a>[Who Said Neural Networks Aren’t Linear?](https://proceedings.mlr.press/v306/berman26c.html) | 可线性化网络 | 用可逆网络把输入输出变到新坐标，中间只放线性算子；共享坐标变换的复合可直接合并线性算子，论文用它将多步扩散合成一步。 |
| <a id="bertholom26a-architecture"></a>[M-Star: Markovian Projection of Star-Shaped Diffusion for Exponential Family Distributions](https://proceedings.mlr.press/v306/bertholom26a.html) | 非高斯扩散 | 在星形扩散的非马尔可夫前向过程上学习马尔可夫投影，使指数族噪声模型也能保持连贯的反向轨迹并用于少步蒸馏。 |
| <a id="candogan26b-architecture"></a>[Deep Flow Networks](https://proceedings.mlr.press/v306/candogan26b.html) | 离散函数近似 | 把最小费用流的值函数扩展为可训练模型，可逼近具有凸延拓的离散函数。偏离 M 凸结构的程度决定最小化难度。 |
| <a id="chakraborty26a-architecture"></a>[Probabilistically-routed Bayesian Additive Spanning Trees for Learning on Constrained Domains](https://proceedings.mlr.press/v306/chakraborty26a.html) | 受约束域回归 | 把贝叶斯生成树的硬分割改成沿树概率路由，可拟合平滑函数；固定树下仍能利用稀疏精度矩阵做后验计算。 |
| <a id="chaussard26a-architecture"></a>[Independent Component Discovery in Temporal Count Data](https://proceedings.mlr.press/v306/chaussard26a.html) | 时序计数分解 | 按不同运行状态建模独立潜成分的贡献，以 Poisson 对数正态模型生成计数，可以区分持续共变成分与状态切换。 |

<a id="by-modules"></a>

### 模块

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="bae26d-modules"></a>[Affine-Scaled Attention: Towards Flexible and Stable Transformer Attention](https://proceedings.mlr.press/v306/bae26d.html) | 注意力参数化 | 在 softmax 权重上接一个由输入决定的仿射变换，允许修改注意力聚合的总幅度，保留按相关性加权值向量的结构。 |
| <a id="bai26l-modules"></a>[Diving into Kronecker Adapters: Component Design Matters](https://proceedings.mlr.press/v306/bai26l.html) | 克罗内克适配器 | 同样的参数预算可拆给不同数量和形状的克罗内克因子。配置会影响适配器对全量微调更新的拟合程度，因此选因子结构本身是重要超参。 |
| <a id="bamba26a-modules"></a>[DOT-MoE: Differentiable Optimal Transport for MoEfication](https://proceedings.mlr.press/v306/bamba26a.html) | 稠密模型转 MoE | 把 FFN 神经元分配建模为有容量约束的平衡最优传输，借可微 Sinkhorn 和直通估计器联合训练专家划分与 token 路由。 |
| <a id="banerjee26b-modules"></a>[Efficient Continuous-Depth Modeling with GRU Equivalents](https://proceedings.mlr.press/v306/banerjee26b.html) | 连续深度模型 | 用紧凑 GRU、一个低维线性 ODE 和稠密层替换多次非线性 ODE 求解，可以保留连续深度层的表达并减少训练推理开销。 |
| <a id="behrouz26a-modules"></a>[Memory Caching: RNNs with Growing Memory](https://proceedings.mlr.press/v306/behrouz26a.html) | 循环模型长程记忆 | 周期性缓存 RNN 隐状态，并允许门控聚合或稀疏选择历史检查点，可以按预算增长记忆容量并改善长上下文召回。 |
| <a id="behrouz26b-modules"></a>[ATLAS: Learning to Optimally Memorize the Context at Test Time](https://proceedings.mlr.press/v306/behrouz26b.html) | 测试时记忆更新 | 更新循环记忆时联合优化滑窗内近期多个 token 的加权键值拟合误差，使写入过程能结合历史上下文。 |
| <a id="brachet26a-modules"></a>[Time Series Forecasting Through the Lens of Dynamics](https://proceedings.mlr.press/v306/brachet26a.html) | 时间序列预测 | 在模型末端加入直接从历史数据点到未来数据点的动态模块，可以补足只在中间层表征中建模时序依赖的做法。 |
| <a id="brandoit26a-modules"></a>[Improving the Performance and Learning Stability of Parallelizable RNNs Designed for Ultra-Low Power Applications](https://proceedings.mlr.press/v306/brandoit26a.html) | 低功耗循环网络 | 将离散记忆状态改为累积更新，使梯度能沿时间跳连传播。在保持量化记忆和迟滞特性的同时，可减轻早期训练对初始化的敏感性。 |
| <a id="cao26af-modules"></a>[Enhanced Multi-Instance Partial Label Learning via Average Gradient Outer Product](https://proceedings.mlr.press/v306/cao26af.html) | 多实例部分标签 | 用包级预测的平均梯度外积找出对判别最敏感的特征方向，并据此重加权实例注意力，辅助识别被错误候选标签淹没的关键实例。 |
| <a id="chaudhry26a-modules"></a>[The Geometry of Projection Heads: Conditioning, Invariance, and Collapse](https://proceedings.mlr.press/v306/chaudhry26a.html) | 自监督投影头 | 线性投影头可做隐式白化，而平滑非线性头可在表征坍缩点引入负曲率。投影头的深度和激活函数因此会影响主干保留的信息。 |

<a id="by-loss-functions"></a>

### 损失函数

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="agirman26a-loss-functions"></a>[Iterative Robust Satisficing: Minimizing Performance Degradation Under Distribution Shift](https://proceedings.mlr.press/v306/agirman26a.html) | 分布偏移鲁棒性 | 把域内性能设为目标值，训练时直接降低性能随分布偏移下降的速率，每次更新可用一次前向和反向计算。 |
| <a id="applebaum26a-loss-functions"></a>[Optimal Learning from Label Proportions with General Loss Functions](https://proceedings.mlr.press/v306/applebaum26a.html) | 聚合标签学习 | 用组内标签比例构造低方差去偏损失估计，使只有聚合标签的二分类和多分类也能使用多种常见训练损失。 |
| <a id="berndt26a-loss-functions"></a>[Approximate Equivariance via Projection-Based Regularisation](https://proceedings.mlr.press/v306/berndt26a.html) | 近似等变正则 | 逐层正交投影得到等变分量，直接惩罚剩下的算子分量，可以覆盖整个群轨道，省掉大量抽样变换。 |
| <a id="cao26k-loss-functions"></a>[Negatives-Dominant Contrastive Learning for Generalization in Imbalanced Domains](https://proceedings.mlr.press/v306/cao26k.html) | 不平衡域泛化 | 在对比损失中放大负样本梯度以拉开类别边界，再用重加权交叉熵与跨域预测对齐来处理类内聚合、标签偏移和域偏移。 |
| <a id="chatterjee26a-loss-functions"></a>[One-shot Conditional Sampling: MMD meets Nearest Neighbors](https://proceedings.mlr.press/v306/chatterjee26a.html) | 单步条件采样 | 用近邻构造局部条件分布的训练估计，并用 MMD 直接优化生成器；测试时一次前向即可采样。 |

<a id="by-optimization"></a>

### 优化

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="abbas26a-optimization"></a>[QuantumBoost: A lazy, yet fast, quantum algorithm for learning with weak hypotheses](https://proceedings.mlr.press/v306/abbas26a.html) | 约束优化 | 在量子 boosting 中把昂贵的约束投影改成每隔 K 轮做一次，由两次投影之间的误差界确定可延迟多久。 |
| <a id="abe26a-optimization"></a>[Asymmetric Perturbation in Solving Bilinear Saddle-Point Optimization](https://proceedings.mlr.press/v306/abe26a.html) | 极小极大优化 | 用非对称收益扰动先改善梯度动力学，再在扰动足够小时恢复原博弈的均衡策略。 |
| <a id="ackermann26b-optimization"></a>[Bridging Spherical Black-Box Optimizers](https://proceedings.mlr.press/v306/ackermann26b.html) | 黑盒优化 | 在 ES 和 OVI 更新之间插值，可以调整优化器对平坦解和尖锐解的偏好。 |
| <a id="adnan26a-optimization"></a>[SparseOpt: Addressing Normalization-induced Gradient Skew in Sparse Training](https://proceedings.mlr.press/v306/adnan26a.html) | 动态稀疏训练 | 按每个神经元输入连接的非零比例开平方来缩放梯度，再用全层平均稀疏度归一化，以抵消批归一化在动态稀疏训练中引入的梯度偏移。 |
| <a id="afriat26a-optimization"></a>[A Robust Optimization Guided Pruning Framework for Vision and Large Language Models](https://proceedings.mlr.press/v306/afriat26a.html) | 一次性剪枝 | 把校准数据噪声和求解过程引起的二次目标不确定性写进鲁棒优化，可在现有一次性剪枝流程中替换目标。 |
| <a id="agarwal26d-optimization"></a>[An Efficient Joint Learning Approach for Item Response Theory](https://proceedings.mlr.press/v306/agarwal26d.html) | 项目反应理论 | 在 Rasch 模型的逻辑似然中引入 Pólya–Gamma 隐变量，使题目难度和用户能力可以在同一 EM 过程中估计。 |
| <a id="aguie26a-optimization"></a>[Improved Analysis of the Accelerated Noisy Power Method with Applications to Decentralized PCA](https://proceedings.mlr.press/v306/aguie26a.html) | 分布式主成分分析 | 把不精确矩阵向量积的容许误差界放宽，可以在去中心化 PCA 中保留加速幂迭代的收敛优势。 |
| <a id="alimisis26a-optimization"></a>[Why Do We Need Warm-up? A Theoretical Perspective](https://proceedings.mlr.press/v306/alimisis26a.html) | 学习率预热 | 若局部曲率上界随损失距最优值而增加，自适应步长在训练初期自然较小，并随损失下降变大，从而得到预热日程。 |
| <a id="amidzadeh26a-optimization"></a>[Non-Parametric Optimization for Scalable Learning in Stochastic Decision Problems](https://proceedings.mlr.press/v306/amidzadeh26a.html) | 时变随机优化 | 用 Malliavin 微积分推导随机决策路径的非参数最优条件，再训练路径跟踪器，可适应分布漂移且不直接受参数化维度限制。 |
| <a id="andersson26b-optimization"></a>[Diffusion Differentiable Resampling](https://proceedings.mlr.press/v306/andersson26b.html) | 可微粒子滤波 | 用免训练的扩散代理重参数化粒子重采样，使梯度可通过重采样步骤传播，同时保持重采样分布的一致性。 |
| <a id="andreyev26a-optimization"></a>[Momentum Further Constrains Sharpness at the Edge of Stochastic Stability](https://proceedings.mlr.press/v306/andreyev26a.html) | 随机优化稳定性 | 动量对稳定曲率的影响随 batch 大小翻转。小 batch 下动量放大随机波动并偏向较平坦区域，大 batch 下恢复经典的稳定作用。 |
| <a id="apidopoulos26a-optimization"></a>[Taming Stochastic Gradient Descent: Almost Sure Convergence and Saddle-Point Avoidance under $(L_0,L_1)$-Smoothness](https://proceedings.mlr.press/v306/apidopoulos26a.html) | 随机梯度收敛 | 对可超线性增长的随机梯度做步幅抑制，能在广义平滑与相应噪声假设下实现几乎必然收敛，并避开严格鞍点。 |
| <a id="armacki26a-optimization"></a>[High-Probability Convergence Guarantees of Decentralized SGD](https://proceedings.mlr.press/v306/armacki26a.html) | 去中心化优化 | 轻尾噪声下，去中心化 SGD 可在与均方误差分析相同的目标函数条件下获得高概率收敛，并随参与节点数线性加速。 |
| <a id="artemev26a-optimization"></a>[Exploiting weight-space symmetries for approximating curvature](https://proceedings.mlr.press/v306/artemev26a.html) | 曲率估计 | 对保持损失不变的权重变换做解析群平均，可以从单次梯度构造结构化 Hessian 近似，所选对称群决定成本与精度。 |
| <a id="attia26a-optimization"></a>[Learning Rate Annealing Improves Tuning Robustness in Stochastic Optimization](https://proceedings.mlr.press/v306/attia26a.html) | 学习率调参 | 在随机凸优化中，多项式退火到零会让收敛率对初始步长误设的依赖由线性降为次线性，支持以更粗的网格搜索初始学习率。 |
| <a id="avranas26a-optimization"></a>[Reducing Per-Sample Interference in Stochastic Optimization](https://proceedings.mlr.press/v306/avranas26a.html) | 样本间梯度冲突 | 在最后一个线性层估计批内样本的二阶干扰，用维数随 batch 大小增长的小优化问题来修正 SGD 或 AdamW 更新。 |
| <a id="bafna26a-optimization"></a>[Taking the GP Out of the Loop](https://proceedings.mlr.press/v306/bafna26a.html) | 贝叶斯优化 | 观察值较多时用近邻估算均值及不确定性，替换 TuRBO 的高斯过程代理和采集规则，可大幅压低每轮候选点的生成时间。 |
| <a id="bai26m-optimization"></a>[Towards Understanding Adam Convergence on Highly Degenerate Polynomials](https://proceedings.mlr.press/v306/bai26m.html) | Adam 收敛 | 在一类高度退化的多项式上，二阶矩与当前梯度平方脱钩可自动抬高有效步长，使 Adam 在稳定区间内获得局部线性收敛。 |
| <a id="bai26o-optimization"></a>[Adaptive Preconditioners Trigger Loss Spikes in Adam](https://proceedings.mlr.press/v306/bai26o.html) | 优化稳定性 | Adam 的二阶矩若在梯度开始变大时继续衰减，预条件曲率就可能越过稳定阈值。沿梯度方向测曲率可以预警损失尖峰。 |
| <a id="baldassari26a-optimization"></a>[Dimension-Free Multimodal Sampling via Preconditioned Annealed Langevin Dynamics](https://proceedings.mlr.press/v306/baldassari26a.html) | 高维多模态采样 | 高斯混合目标上，匹配平滑协方差与混合分量的谱结构，可让退火 Langevin 的精度控制不依赖离散维度。谱衰减预条件还能限制近似分数误差累积。 |
| <a id="banerjee26a-optimization"></a>[Local-Minima-Preserving Polynomial Relaxation of Ising Problems](https://proceedings.mlr.press/v306/banerjee26a.html) | 组合优化松弛 | 构造多项式松弛使连续局部极小点与 Ising 的单翻转局部极小点一一对应，可以直接用梯度优化寻找原问题的局部解。 |
| <a id="banihashem26c-optimization"></a>[Improved Dynamic Algorithm for Non-monotone Submodular Maximization under Cardinality Constraint](https://proceedings.mlr.press/v306/banihashem26c.html) | 动态次模优化 | 对有元素数上限的非单调次模最大化，可在集合持续增删时以接近二次于上限的单次更新时间，维持 0.262 的近似保证。 |
| <a id="bhatia26a-optimization"></a>[CLoVE: Personalized Federated Learning through Clustering of Loss Vector Embeddings](https://proceedings.mlr.press/v306/bhatia26a.html) | 个性化联邦学习 | 用多模型在客户端数据上的损失向量作为客户端嵌入，按损失模式聚类并分别聚合，可少依赖接近最优的模型初始化。 |
| <a id="bi26b-optimization"></a>[FedFit: Federated Dynamic Sparse Training via Fisher Information scoring](https://proceedings.mlr.press/v306/bi26b.html) | 联邦动态稀疏训练 | 用 Fisher 信息近似结构调整的二阶损失成本，代替只看参数幅值的剪枝准则，并省去显式 Hessian。 |
| <a id="blasingame26a-optimization"></a>[Rex: A Family of Reversible Exponential (Stochastic) Runge-Kutta Solvers](https://proceedings.mlr.press/v306/blasingame26a.html) | 可逆扩散求解 | 用 Lawson 变换把显式 Runge–Kutta 形式改为代数可逆的求解器，使扩散 ODE 和 SDE 都能以接近机器精度回放轨迹。 |
| <a id="blin26a-optimization"></a>[Batched First-Order Methods for Parallel LP Solving in MIP](https://proceedings.mlr.press/v306/blin26a.html) | 混合整数规划加速 | 批量处理强分支等步骤产生的相关线性规划，把重复的矩阵向量乘法改成 GPU 矩阵乘法，并以问题规模判断是否优于单纯形法。 |
| <a id="borghi26a-optimization"></a>[Variational inference via Gaussian interacting particles in the Bures-Wasserstein geometry](https://proceedings.mlr.press/v306/borghi26a.html) | 变分推断 | 在 Bures–Wasserstein 几何中用可高效计算的线性化参数表示高斯分布，多个粒子靠共识更新在分布空间做零阶搜索。 |
| <a id="bracher26a-optimization"></a>[JADAI: Jointly Amortizing Adaptive Design and Bayesian Inference](https://proceedings.mlr.press/v306/bracher26a.html) | 贝叶斯自适应实验 | 联合训练选实验的策略、历史编码器和扩散后验估计器，以整段实验中后验误差的逐步降低为目标，无需计算后验密度。 |
| <a id="braun26a-optimization"></a>[Spectral Gradient Descent Mitigates Anisotropy-Driven Misalignment: A Case Study in Phase Retrieval](https://proceedings.mlr.press/v306/braun26a.html) | 谱梯度优化 | 相位恢复中，高方差方向可能与真实信号正交，普通梯度更新会在早期放大这个方向。谱梯度归一化能抑制这种无关放大。 |
| <a id="bruno26a-optimization"></a>[Flatness-Aware Stochastic Gradient Langevin Dynamics](https://proceedings.mlr.press/v306/bruno26a.html) | Langevin 优化 | 把噪声尺度与逆温度联合设定，可让一阶 Langevin 更新采样偏向平坦的低损失盆地，同时保留较低的优化开销。 |
| <a id="cai26j-optimization"></a>[Fast Spectrally Sparse Signal Reconstruction via Jacobi-Preconditioned Gradient Descent](https://proceedings.mlr.press/v306/cai26j.html) | 谱稀疏信号重建 | 把信号重建写成低秩 Hankel 补全，在因子空间用 Jacobi 预条件更新；可保留一阶迭代成本，并在论文条件下让线性收敛率摆脱条件数。 |
| <a id="cao26ae-optimization"></a>[Diversity-Aware Recursive Feature Multiple Kernel Learning](https://proceedings.mlr.press/v306/cao26ae.html) | 多核学习 | 先从数据学习特征加权核，再联合优化核质量和多样性。线性松弛与 Nyström 草图可降低组合选核成本。 |
| <a id="cauvin26a-optimization"></a>[Bregman meets Lévy: Stochastic Mirror Descent with Heavy-Tailed Noise in Continuous and Discrete Time](https://proceedings.mlr.press/v306/cauvin26a.html) | 重尾随机镜像下降 | 用 Lévy 跳过程分析重尾随机梯度。即使方差无限，只要存在一阶以上的矩，仍可得到依赖矩阶数和目标曲率的收敛界。 |
| <a id="cayci26a-optimization"></a>[Geometric Convergence of Gauss–Newton for Neural Networks: Riemannian Geometry and Adaptive Damping](https://proceedings.mlr.press/v306/cayci26a.html) | Gauss–Newton 训练 | 把欠参数化的高斯–牛顿视作函数流形上的梯度下降，在过参数化时根据曲率调阻尼，可在特定条件下避免最小核特征值拖慢收敛。 |
| <a id="chagneux26a-optimization"></a>[Efficient Online Variational Estimation via Monte Carlo Sampling](https://proceedings.mlr.press/v306/chagneux26a.html) | 在线变分估计 | 用独立 Monte Carlo 样本估计流式证据下界及其梯度，使状态空间模型的参数和潜状态后验能在新观测到达时联合更新。 |
| <a id="chakraborty26c-optimization"></a>[Randomized Feasibility Methods for Constrained Optimization with Adaptive Step Sizes](https://proceedings.mlr.press/v306/chakraborty26c.html) | 随机约束优化 | 无需每步投影到整个可行交集，抽取随机数量的约束做 Polyak 式可行性更新，再与目标的梯度步交替。 |
| <a id="chao26a-optimization"></a>[Last-iterate Convergence of ADMM on Multi-affine Quadratic Equality Constrained Problem](https://proceedings.mlr.press/v306/chao26a.html) | 多仿射等式约束 | 即使全局问题非凸，固定其余变量后仍可利用单块结构。论文给出这类问题上 ADMM 的末次迭代收敛，约束非凸性受限时可线性收敛。 |
| <a id="chebykin26a-optimization"></a>[Iterated Population Based Training with Task-Agnostic Restarts](https://proceedings.mlr.press/v306/chebykin26a.html) | 种群超参优化 | 把超参更新间隔也纳入搜索。重启时复用模型权重，再用随训练阶段变化的贝叶斯优化初始化超参，从而在固定预算下调整搜索频率。 |
| <a id="chekalina26a-optimization"></a>[Scalable Kronecker-Factored Fisher Approximation for Neural Network Parameter Sensitivity](https://proceedings.mlr.press/v306/chekalina26a.html) | 低秩压缩的 Fisher 近似 | 用无需显式存储全矩阵的 Kronecker 分解保留参数间相关性，在论文的矩阵正态假设下可闭式求出让预期二阶损失增量最小的低秩层。 |
| <a id="chen26e-optimization"></a>[Bulk-Calibrated Credal Ambiguity Sets: Fast, Tractable Decision Making under Out-of-Sample Contamination](https://proceedings.mlr.press/v306/chen26e.html) | 污染下的分布鲁棒优化 | 从数据估计高概率区域，在区域内建模任意污染，区域外的尾部风险单独加界，可把原来可能无穷的最坏风险改写成可解的有限目标。 |
| <a id="chen26ah-optimization"></a>[Data-driven Mixed Integer Optimization through Probabilistic Multi-variable Branching](https://proceedings.mlr.press/v306/chen26ah.html) | 混合整数规划分支 | 用数据驱动的超平面同时对多个变量分支，不必改求解器的其他部分，可利用学习模型对变量间关系的预测缩小搜索。 |
| <a id="chen26ax-optimization"></a>[IO-Adam: Rethinking Memory-Efficient Adaptive Optimizers from Gradient Computation](https://proceedings.mlr.press/v306/chen26ax.html) | Adam 状态压缩 | 利用矩阵权重梯度由输入和输出梯度相乘形成的结构，分别跟踪这两侧的量以估计矩，从而减少直接存两份全尺寸矩状态的成本。 |

<a id="by-training-strategies"></a>

### 训练策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="abdollahpoorrostam26a-training-strategies"></a>[MODEL SOUPS NEED ONLY ONE INGREDIENT](https://proceedings.mlr.press/v306/abdollahpoorrostam26a.html) | 权重合并 | 对基座到微调模型的逐层权重差做 SVD，分别调整头部和尾部成分。 |
| <a id="almudevar26b-training-strategies"></a>[Representation Unlearning: Forgetting through Information Compression](https://proceedings.mlr.press/v306/almudevar26b.html) | 机器遗忘 | 固定模型参数，在表征空间学习信息瓶颈，保留与应保留数据有关的信息并压掉与欲遗忘数据有关的信息。 |
| <a id="bakr26a-training-strategies"></a>[Collaborative Threshold Watermarking](https://proceedings.mlr.press/v306/bakr26a.html) | 联邦模型水印 | 各客户端训练一个共享水印，对验证密钥做门限秘密分享，只有凑够指定数量的参与方才能共同确认模型来源。 |
| <a id="bell26a-training-strategies"></a>[Continual Model Routing in Evolving Model Hubs](https://proceedings.mlr.press/v306/bell26a.html) | 持续模型路由 | 模型库扩展时，用分领域的代表样本回放与旧检查点锚定训练路由嵌入，兼顾接入新模型和维持已有路由表现。 |
| <a id="bian26e-training-strategies"></a>[FedTreeLoRA: Reconciling Statistical and Functional Heterogeneity in Federated LoRA Fine-Tuning](https://proceedings.mlr.press/v306/bian26e.html) | 联邦 LoRA | 通过树形聚合让客户端共享较浅层的共同表征，并允许深层在不同客户端群中逐级专门化。 |
| <a id="brady26a-training-strategies"></a>[Efficient Learning of Deep State Space Models via Importance Smoothing](https://proceedings.mlr.press/v306/brady26a.html) | 状态空间模型训练 | 把变分训练与重要性平滑结合为可并行的 Monte Carlo 训练，避免沿时间轴串行运行传统粒子滤波，兼顾生成和判别任务。 |
| <a id="cameron26a-training-strategies"></a>[One Step Forward and K Steps Back: Better Reasoning with Denoising Recursion Models](https://proceedings.mlr.press/v306/cameron26a.html) | 递归去噪训练 | 按不同强度破坏目标解，再监督循环模型用多次共享块更新恢复，可让中间状态更接近推理过程，并训练非贪心细化路径。 |
| <a id="cao26a-training-strategies"></a>[Required Spine Optional Limbs: Heterogeneous Federated Learning via Backbone-sharing and Activation-guided Selection](https://proceedings.mlr.press/v306/cao26a.html) | 异构联邦学习 | 每层保留各设备共同训练的主干，剩余神经元按历史激活频率概率抽样，为不同设备生成子网并减少参数冲突。 |
| <a id="carter26a-training-strategies"></a>[Discrete Diffusion Samplers and Bridges: Off-Policy Algorithms and Applications in Latent Spaces](https://proceedings.mlr.press/v306/carter26a.html) | 离散扩散采样 | 用离策略样本训练离散扩散采样器，并将训练扩展为连接数据分布和未归一化能量目标的 Schrödinger 桥。 |
| <a id="che26a-training-strategies"></a>[Efficiently Training Time-to-First-Spike Spiking Neural Networks from Scratch](https://proceedings.mlr.press/v306/che26a.html) | 首脉冲时间编码 | 用适配稀疏放电的初始化和训练归一化维持梯度，再聚合输出脉冲时间鼓励提前放电。池化时用平均池化维持单次脉冲约束。 |
| <a id="chemseddine26a-training-strategies"></a>[Adapting Noise to Data: Generative Flows from Learned 1D Processes](https://proceedings.mlr.press/v306/chemseddine26a.html) | 生成流的先验 | 用一维分位数函数参数化噪声分布，再按 Wasserstein 距离拟合数据，让流匹配的起点适应重尾或紧支撑数据并缩短传输路径。 |
| <a id="chen26t-training-strategies"></a>[Test-Time Learning of Causal Structure from Interventional Data](https://proceedings.mlr.press/v306/chen26t.html) | 测试时因果结构学习 | 对每个新干预设定做实例级自增强，再依联合因果推断分阶段学习因果结构和干预目标，减少训练环境与实际干预不一致造成的偏移。 |

<a id="by-data-strategies"></a>

### 数据策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="afshani26a-data-strategies"></a>[The benefits of full data shuffle, now with optimal I/O cost: $k$-wise independence and matrix transposition to the rescue](https://proceedings.mlr.press/v306/afshani26a.html) | 数据洗牌 | 对无放回 SGD，用低阶独立的近随机排列代替均匀排列，在论文设定下保持期望收敛率并把 I/O 压到线性。 |
| <a id="bonilla26a-data-strategies"></a>[Causal Preference Elicitation](https://proceedings.mlr.press/v306/bonilla26a.html) | 主动因果发现 | 从观测数据得到的图后验出发，用带噪三类专家反馈更新边的存在和方向，并按期望信息增益优先选择要问的边。 |
| <a id="candes26a-data-strategies"></a>[Probably Approximately Correct Labels](https://proceedings.mlr.press/v306/candes26a.html) | 带保证的自动标注 | 按模型预测的不确定性分配人工核查，再用审计结果限制全数据集的标注错误率，保留自动标注节省的成本。 |
| <a id="chen26ac-data-strategies"></a>[Let the Prototype Guide You: Robust Aggregation of Sparse Multi-Class Annotations via Annotator Prototype Learning](https://proceedings.mlr.press/v306/chen26ac.html) | 稀疏多类标注聚合 | 先跨标注者共享每个类别的标注行为原型，再为个人估计原型权重，可在个人标注不足时共享统计强度，并允许复杂的混淆模式。 |

<a id="by-inference"></a>

### 推理策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="blessing26a-inference"></a>[Bridge Matching Sampler: Scalable Sampling via Generalized Fixed-Point Diffusion Matching](https://proceedings.mlr.press/v306/blessing26a.html) | 未归一化分布采样 | 把扩散匹配统一成由 Nelson 关系导出的不动点迭代，允许使用更一般的先验。阻尼正则可以缓和迭代中的模态坍缩。 |
| <a id="block26a-inference"></a>[Temper-Then-Tilt: Principled Unlearning for Generative Models through Tempering and Classifier Guidance](https://proceedings.mlr.press/v306/block26a.html) | 生成式模型遗忘 | 先对基座分布做温度缩放压平待遗忘样本的高概率峰，再用区分保留与遗忘数据的小分类器调整采样，以改善集中遗忘集的有限样本效果。 |
| <a id="castro-maci-as26a-inference"></a>[Conditional Diffusion Sampling](https://proceedings.mlr.press/v306/castro-maci-as26a.html) | 条件扩散采样 | 先用并行回火做全局探索，再沿有闭式形式的条件 SDE 做短时局部传输，结合两者能力而无需求助神经网络近似。 |
| <a id="chen26f-inference"></a>[Proximal-IMH: Proximal Posterior Proposals for Independent Metropolis–Hastings with Approximate Operators](https://proceedings.mlr.press/v306/chen26f.html) | 贝叶斯逆问题采样 | 先从便宜但有偏的近似后验采样，再解局部近端优化调整提议，最后由独立 Metropolis–Hastings 校正到目标后验。 |
| <a id="chen26g-inference"></a>[FlashBlock: Attention Caching for Efficient Long-Context Block Diffusion](https://proceedings.mlr.press/v306/chen26g.html) | 分块扩散注意力缓存 | 当前块外的注意力输出在多个去噪步骤间变化较小，可缓存并复用这一部分，每步继续重算变化大的块内注意力。 |

<a id="by-representation-learning"></a>

### 表征学习

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="achara26a-representation-learning"></a>[Multi-Way Representation Alignment](https://proceedings.mlr.press/v306/achara26a.html) | 多模型表征对齐 | 先用多路正交 Procrustes 建公共空间，再做方向校正，兼顾内部几何与跨模型检索。 |
| <a id="asefaw26a-representation-learning"></a>[WeightCLIP: Aligning Datasets and Models for Weight Space Learning](https://proceedings.mlr.press/v306/asefaw26a.html) | 权重空间学习 | 对齐数据集编码与训练出模型的权重潜变量，再解码可从目标数据的表示生成或细化模型参数。 |
| <a id="bamberger26a-representation-learning"></a>[Riemannian Metric Matching for Scalable Geometric Modeling of Distributions](https://proceedings.mlr.press/v306/bamberger26a.html) | 数据流形几何 | 把决定黎曼度量的 carré du champ 算子写成扰动的条件期望，用逐样本去噪训练神经估计器，无需在推理时重建核或近邻图。 |
| <a id="batra26a-representation-learning"></a>[Uncovering the Latent Potential of Deep Intermediate Representations](https://proceedings.mlr.press/v306/batra26a.html) | 中间层特征迁移 | 任务判别信息随深度非单调分布。先用谱方法挑中间层子空间，再用几何正则保持类别结构，可以改善迁移。 |
| <a id="berardini26a-representation-learning"></a>[Distribution Alignment for One-Shot Federated Learning via Optimal Transport](https://proceedings.mlr.press/v306/berardini26a.html) | 单轮联邦学习 | 用冻结编码器提取各方特征统计，以 Bures–Wasserstein 重心作共同参考，再通过闭式传输一次对齐本地表示。 |
| <a id="calvo-ordonez26a-representation-learning"></a>[Richer Bayesian Last Layers with Subsampled NTK Features](https://proceedings.mlr.press/v306/calvo-ordonez26a.html) | 贝叶斯不确定性 | 把全网络的神经切线核特征投影到末层特征空间，可让贝叶斯末层纳入前部网络的变化，同时保持低成本推断。 |
| <a id="cao26t-representation-learning"></a>[Causal Feature Learning via Generalized Rayleigh Quotients](https://proceedings.mlr.press/v306/cao26t.html) | 跨环境特征提取 | 用广义 Rayleigh 商在最大化时序预测相关性的同时惩罚环境之间的均值漂移，从而提取对工况变化更稳健的子空间。 |
| <a id="chawla26a-representation-learning"></a>[MetaOthello: A Controlled Study of Multiple World Models in Transformers](https://proceedings.mlr.press/v306/chawla26a.html) | 多世界模型表征 | 用共享语法但规则不同的黑白棋变体训练同一模型。跨游戏线性探针仍能干预棋盘表征，说明共性状态可共享，规则冲突则由局部机制处理。 |
| <a id="chen26h-representation-learning"></a>[Vector Linking via Cross-Model Local Isometric Consistency](https://proceedings.mlr.press/v306/chen26h.html) | 跨编码器向量匹配 | 不同编码器的局部距离经缩放后往往相容。用少量配对锚点构造距离签名，再把多视角都支持的匹配升为新锚点，可在黑盒编码器间对齐样本。 |

<a id="by-evaluation"></a>

### 评测与诊断

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="agrawal26b-evaluation"></a>[A Benchmark and Framework for Evaluating Next Action Predictions in Spreadsheets](https://proceedings.mlr.press/v306/agrawal26b.html) | 交互式评测 | 表格动作补全应在线计分。每次接受预测后更新剩余操作序列，才能量化真正节省的动作以及误报的成本。 |
| <a id="almudevar26a-evaluation"></a>[Bridging Functional and Representational Similarity via Usable Information](https://proceedings.mlr.press/v306/almudevar26a.html) | 表征相似性 | 模型拼接的可替代性有方向，且依赖连接器表达能力。比较两个表征时可做双向拼接，并报告使用的预测器类别。 |
| <a id="anani26a-evaluation"></a>[Certified Circuits: Stability Guarantees for Mechanistic Circuits](https://proceedings.mlr.press/v306/anani26a.html) | 机制可解释性 | 重复子采样概念数据来验证电路组件是否稳定，依赖个别样本的边或神经元可以留空，只保留对有限数据编辑不变的部分。 |
| <a id="arpit26a-evaluation"></a>[TPV: Parameter Perturbations Through the Lens of Test Prediction Variance](https://proceedings.mlr.press/v306/arpit26a.html) | 参数扰动稳健性 | 用预测方差把输出几何与扰动协方差拆开分析，使量化、剪枝与训练噪声可以共用局部敏感度框架，并导出无标签剪枝准则。 |
| <a id="athanasiadis26a-evaluation"></a>[Grounding Functional Similarity by Invariance-Aware Model Stitching](https://proceedings.mlr.press/v306/athanasiadis26a.html) | 模型拼接评测 | 拼接模型应同时检验前向任务兼容性和反向不变性。仅拼接成功的模型也可能依赖不同输入线索。 |
| <a id="bado26a-evaluation"></a>[Clustered Influence Functions](https://proceedings.mlr.press/v306/bado26a.html) | 影响函数 | 先聚类训练梯度并缓存每个簇均值的逆曲率结果，新子集查询按各簇的样本数线性组合，适合反复做数据删除或重采样分析。 |
| <a id="balef26a-evaluation"></a>[Is One Layer Enough? Understanding Inference Dynamics in Tabular Foundation Models](https://proceedings.mlr.press/v306/balef26a.html) | 表格基础模型 | 逐层跟踪预测形成过程可以发现跨层重复计算。用同一层循环细化的原型仅需原模型五分之一参数，在实验中达到相近表现。 |
| <a id="bao26c-evaluation"></a>[Universal Redundancies in Time Series Foundation Models](https://proceedings.mlr.press/v306/bao26c.html) | 时序基础模型压缩 | 多种时序 Transformer 可容忍移除整层。按投影矩阵的稳定秩挑头做消融，还能定位复读上下文模式和季节偏置的来源。 |
| <a id="boetius26a-evaluation"></a>[Verified SHAP: Provable Bounds for Exact Shapley Values of Neural Networks](https://proceedings.mlr.press/v306/boetius26a.html) | 可验证模型解释 | 用神经网络验证器给 SHAP 值逐步收紧上下界，可把精确求解推进到更大搜索空间，用来核对近似解释。 |
| <a id="bonagiri26a-evaluation"></a>[STABLEVAL: Disagreement-Aware and Stable Evaluation of AI Systems](https://proceedings.mlr.press/v306/bonagiri26a.html) | 人评聚合 | 联合推断潜在正确性和各标注者混淆模式，然后用题目后验期望计分。与硬多数票相比，这能减轻更换标注者子集造成的排名波动。 |
| <a id="braun26c-evaluation"></a>[Conditional Coverage Diagnostics for Conformal Prediction](https://proceedings.mlr.press/v306/braun26c.html) | 共形覆盖诊断 | 把各局部样本是否被预测集覆盖作为学习目标，比较分类器与固定目标覆盖率的风险，可识别边际覆盖指标漏掉的局部欠覆盖或过覆盖。 |

<a id="by-theory-statistics"></a>

### 理论与统计

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="aczel26a-theory-statistics"></a>[Efficient Bayesian Inference from Noisy Pairwise Comparisons](https://proceedings.mlr.press/v306/aczel26a.html) | 偏好标注 | 拟合成对偏好时同时估计标注者质量，使噪声较大的标注者贡献更小。 |
| <a id="adler26a-theory-statistics"></a>[A Capacity-Based Rationale for Multi-Head Attention](https://proceedings.mlr.press/v306/adler26a.html) | 注意力容量 | 总键维度相同时，多头可以减轻嵌入叠加造成的关系干扰，即使每个查询只需要找一个目标。 |
| <a id="agarwal26b-theory-statistics"></a>[Fast Reconstruction of Mixtures of Bernoulli Product Distributions](https://proceedings.mlr.press/v306/agarwal26b.html) | 潜变量模型 | 对 Bernoulli 乘积分布混合的生成多项式做低维限制，用低阶系数构造张量矩来恢复各分量和混合权重。 |
| <a id="agarwal26c-theory-statistics"></a>[Sinkhorn Treatment Effects: A Causal Optimal Transport Measure](https://proceedings.mlr.press/v306/agarwal26c.html) | 因果推断 | 用熵正则最优传输比较两个反事实结果分布，并把多个正则强度的检验合起来，降低检验功效对单一强度的依赖。 |
| <a id="aiyer26a-theory-statistics"></a>[A Theoretical Framework for Statistical Evaluability of Generative Models](https://proceedings.mlr.press/v306/aiyer26a.html) | 生成模型评测 | 有限样本下，基于有界测试函数的积分概率度量有近似估计保证，而罕见事件可使 KL 或 Rényi 散度无法可靠估计。 |
| <a id="alacaoglu26a-theory-statistics"></a>[Solving Stochastic Variational Inequalities without the Bounded Variance Assumption](https://proceedings.mlr.press/v306/alacaoglu26a.html) | 随机变分不等式 | 允许随机 oracle 的方差随变量范数平方增长，仍能在单调和满足弱 Minty 条件的部分非单调问题上保持约为 ε⁻⁴ 的复杂度。 |
| <a id="alami26a-theory-statistics"></a>[Set-Preserving Calibration from Conformal P-Values to E-Values](https://proceedings.mlr.press/v306/alami26a.html) | 共形预测 | 设计保留原预测集的 p 值到 e 值转换，再利用 e 值合并相依的划分或模型证据，可得到目标覆盖率。 |
| <a id="alcalde26a-theory-statistics"></a>[Attention’s forward pass and Frank-Wolfe](https://proceedings.mlr.press/v306/alcalde26a.html) | 注意力理论 | 零温度 hardmax 注意力可写成当前 token 凸包上的 Frank–Wolfe 步，键查询矩阵的符号决定动力学会向能量极值或凸包顶点演化。 |
| <a id="alhanouti26a-theory-statistics"></a>[Robust Strategic Classification under Decision-Dependent Cost Uncertainty](https://proceedings.mlr.press/v306/alhanouti26a.html) | 策略性分类 | 在两阶段鲁棒优化中让第二阶段的行为操纵成本取决于第一阶段决策，可建模用户对历史策略的长期适应。 |
| <a id="allain26a-theory-statistics"></a>[Asymmetric conformal prediction with penalized kernel sum-of-squares](https://proceedings.mlr.press/v306/allain26a.html) | 非对称共形预测 | 给预测带加入可调对称惩罚，让上下边界按残差偏度自动分配宽度，小样本和有偏预测中也能适配。 |
| <a id="alvarez-lopez26a-theory-statistics"></a>[Perceptrons and Localization of Attention’s Mean-Field Landscape](https://proceedings.mlr.press/v306/alvarez-lopez26a.html) | Transformer 均场理论 | 把 token 当作球面上的相互作用粒子，在论文研究的均场设定里，引入感知机后，临界分布通常由离散原子构成并局部集中。 |
| <a id="ambadi26a-theory-statistics"></a>[Likelihood over Estimation: Robust Quadratic Discriminant Analysis for Heavy-Tailed Distributions with Theory and Evidence](https://proceedings.mlr.press/v306/ambadi26a.html) | 重尾分类 | 在 QDA 中把高斯类条件似然换成对称 α 稳定似然。若类间方差差异本身有判别力，先修正似然可能比改用鲁棒参数估计更有效。 |
| <a id="ameli26a-theory-statistics"></a>[Learning-Augmented Online Covering Problems](https://proceedings.mlr.press/v306/ameli26a.html) | 带预测的在线算法 | 用预测请求包装现有的在线覆盖算法，把竞争比中对总请求数的依赖替换为对预测误差的依赖。 |
| <a id="anagnostides26a-theory-statistics"></a>[On the Computational Complexity of Performative Prediction](https://proceedings.mlr.press/v306/anagnostides26a.html) | 部署反馈下的预测 | 当模型对数据分布的反馈略强于收缩阈值时，即使用二次损失和线性分布偏移，找近似稳定点也会达到 PPAD 完全。 |
| <a id="anguita26a-theory-statistics"></a>[A Theory of How Pretraining Shapes Inductive Bias in Fine-Tuning](https://proceedings.mlr.press/v306/anguita26a.html) | 预训练与微调理论 | 当下游任务只依赖预训练特征的子集，较小的早层初始化尺度可让后续微调同时复用和调整这些特征。 |
| <a id="arno26a-theory-statistics"></a>[Rank-Learner: Orthogonal Ranking of Treatment Effects](https://proceedings.mlr.press/v306/arno26a.html) | 个体处理效应排序 | 如果决策只依赖排序，可直接优化两两处理效应顺序。Neyman 正交的目标降低了辅助模型估计误差对排序的影响。 |
| <a id="arvanitakis26a-theory-statistics"></a>[Provable Accuracy Collapse in Embedding-Based Representations under Dimensionality Mismatch](https://proceedings.mlr.press/v306/arvanitakis26a.html) | 嵌入维度下界 | 仅用距离三元组监督也可出现维度临界点。对构造出的三元组实例，当嵌入维度低于真实维度的固定比例，任何嵌入都将违反近半约束。 |
| <a id="ashiq26a-theory-statistics"></a>[Why DDIM Hallucinates More Than DDPM: A Theoretical Analysis of Reverse Dynamics](https://proceedings.mlr.press/v306/ashiq26a.html) | 扩散采样 | 在论文构造的高斯混合分布中，DDIM 的确定性轨迹可能滞留在模态之间，适时加入随机步有机会把轨迹带出该区域。 |
| <a id="ashouritaklimi26a-theory-statistics"></a>[Robust Bayes-Assisted Conformal Prediction](https://proceedings.mlr.press/v306/ashouritaklimi26a.html) | 鲁棒共形预测 | 让非一致性分数按先验可靠性做收缩。先验与观测不匹配时退回基于样本均值距离的分数，同时保留共形覆盖保证。 |
| <a id="asi26a-theory-statistics"></a>[Fast and Near-Optimal Algorithms for Private Hypothesis Selection](https://proceedings.mlr.press/v306/asi26a.html) | 差分隐私假设选择 | 用少量强假设构造替代损失，为多数候选高效打分，从而在假设总数近线性的时间内保持近最优统计速率。 |
| <a id="avital26a-theory-statistics"></a>[Learning Partial Concept Classes and Universal Rates Under Massart Noise](https://proceedings.mlr.press/v306/avital26a.html) | 带噪 PAC 学习 | 在 Massart 噪声下，用带偏移的 Rademacher 分析和局部度量熵收紧传导式经验风险最小化的超额误差界。 |
| <a id="aziz26a-theory-statistics"></a>[Fair Transit Stop Placement: A Clustering Perspective and Beyond](https://proceedings.mlr.press/v306/aziz26a.html) | 公平选址 | 公交站点的公平性可以通过比例聚类连接到联盟公平。独立选址算法能改进正当代表性的近似界，两者可以插值以调节取舍。 |
| <a id="baldo26a-theory-statistics"></a>[Regret-Based Federated Causal Discovery with Unknown Interventions](https://proceedings.mlr.press/v306/baldo26a.html) | 联邦因果发现 | 先识别客户端共有的部分定向无环图，再利用不同客户端的未知干预造成的结构差异，给更多因果边定向。 |
| <a id="banihashem26d-theory-statistics"></a>[Matroid Algorithms Under Size-Sensitive Independence Oracles](https://proceedings.mlr.press/v306/banihashem26d.html) | 拟阵算法成本 | 独立性查询按集合大小收费时，找基及相关估计的总代价近二次。最大回路大小有界时，最大权基可以用次二次查询成本求出。 |
| <a id="bansal26a-theory-statistics"></a>[Conformal C2ST: Turning weak classifiers into strong two-sample tests](https://proceedings.mlr.press/v306/bansal26a.html) | 两样本检验 | 把分类器分数转成共形 p 值，即使分类器较弱也能精确控制有限样本一类错误，检验功效随分类误差逐步下降。 |
| <a id="bardone26a-theory-statistics"></a>[A theory of learning data statistics in diffusion models, from easy to hard](https://proceedings.mlr.press/v306/bardone26a.html) | 扩散学习动力学 | 扩散模型通常先学成对统计，再学高阶相关。在受控累积量模型中，两者共享潜结构时，学习四阶统计的样本复杂度可从至少立方降到线性。 |
| <a id="barkeshli26a-theory-statistics"></a>[On the Origin of Neural Scaling Laws: from Random Graphs to Natural Language](https://proceedings.mlr.press/v306/barkeshli26a.html) | 神经缩放律 | 让 Transformer 预测不含幂律相关性的图随机游走也能观察到缩放律。改变训练序列生成器的复杂度，会系统改变测得的缩放指数。 |
| <a id="bashari26a-theory-statistics"></a>[General Synthetic-Powered Inference](https://proceedings.mlr.press/v306/bashari26a.html) | 合成数据辅助推断 | 用统计包装器把合成数据作为辅助证据。合成数据质量差时自适应退回真实数据基线，同时维持目标错误率。 |
| <a id="bateni26a-theory-statistics"></a>[Networked Information Aggregation for Binary Classification](https://proceedings.mlr.press/v306/bateni26a.html) | 分布式分类 | 每个节点可把父节点 logit 拼到本地特征训练分类器。若连续 M 个节点覆盖全部特征，沿路径加深可逐步降低信息聚合误差。 |
| <a id="bauer26a-theory-statistics"></a>[A unified theory of feature learning in RNNs and DNNs](https://proceedings.mlr.press/v306/bauer26a.html) | 循环网络特征学习 | 理论中学习信号超过初始化噪声后，跨步权重共享会让 RNN 学出相关的时间表征，并帮助推断没见过的时刻。 |
| <a id="bayle26a-theory-statistics"></a>[The Relative Instability of Model Comparison with Cross-validation](https://proceedings.mlr.press/v306/bayle26a.html) | 交叉验证比较 | 两个模型各自稳定，交叉验证估计的相对性能差也可能不稳定。检验或置信区间要核查性能差本身的稳定条件。 |
| <a id="bechavod26a-theory-statistics"></a>[Stronger Benchmarks for Prediction as a Service with Constraints](https://proceedings.mlr.press/v306/bechavod26a.html) | 约束在线决策 | 向目标和约束都不同的下游代理广播预测，仍可同时对多个相交子序列保证动态遗憾并让约束违规趋零，下游只需基于当前预测行动。 |
| <a id="beck26a-theory-statistics"></a>[Symmetries in PAC-Bayesian Learning](https://proceedings.mlr.press/v306/beck26a.html) | 对称性泛化 | 用 PAC-Bayes 分析把对称模型的泛化优势扩展到平移等非紧变换，并允许数据分布偏离严格不变假设。 |
| <a id="bell26b-theory-statistics"></a>[Efficient Public Verification of Private ML via Regularization](https://proceedings.mlr.press/v306/bell26b.html) | 差分隐私可验证训练 | 将随机凸训练拆成一串私有正则化子问题，利用标准隐私组合界保留接近最优的效用，同时使外部验证比重做训练便宜。 |
| <a id="benger26a-theory-statistics"></a>[Fair Decisions from Calibrated Scores: Achieving Optimal Classification While Satisfying Sufficiency](https://proceedings.mlr.press/v306/benger26a.html) | 分类公平性 | 即便分数逐群体完全校准，阈值化后也可能失去预测充分性。按群体和分数做随机后处理，可在满足充分性的解中优化准确率。 |
| <a id="bhagwat26a-theory-statistics"></a>[RSA-CP: Efficient Conformal Prediction in Small-Sample Regimes via Random Score Alignment](https://proceedings.mlr.press/v306/bhagwat26a.html) | 小样本共形校准 | 用最优传输直接把真实校准分数对齐到高分辨率参考分数分布，细化小样本的阶梯状分位数，同时保持有限样本覆盖。 |
| <a id="bhattacharya26a-theory-statistics"></a>[Dynamic High-Dimensional Facility Location with Low Recourse](https://proceedings.mlr.press/v306/bhattacharya26a.html) | 动态设施选址 | 非均匀选址成本且客户持续增删时，可通过放宽近似比换快速更新，同时把每次更新引起的设施调整控制到摊销对数级。 |
| <a id="bhattamishra26a-theory-statistics"></a>[Provably Learning Attention with Queries](https://proceedings.mlr.press/v306/bhattamishra26a.html) | 注意力黑盒可辨识性 | 任意向量查询下，低秩单头的参数可用压缩感知恢复，查询数随宽度与头维度的乘积增长。多头在没有额外假设时会失去这种可辨识性。 |
| <a id="bleistein26a-theory-statistics"></a>[Optimal Transport under Group Fairness Constraints](https://proceedings.mlr.press/v306/bleistein26a.html) | 群体公平最优传输 | 在传输矩阵中约束各群体配对的总概率。严格匹配目标会抬高成本时，可改成软惩罚或学习促成公平的地面代价。 |
| <a id="block26b-theory-statistics"></a>[On Contraction of Sequential and Offset Rademacher Complexities](https://proceedings.mlr.press/v306/block26b.html) | 统计复杂度收缩 | 在适当结构条件下，Lipschitz 复合的收缩可扩展到序贯和偏移 Rademacher 复杂度，但一般必须付出多对数因子。 |
| <a id="bogdanov26a-theory-statistics"></a>[Statistically Undetectable Backdoors in Deep Neural Networks](https://proceedings.mlr.press/v306/bogdanov26a.html) | 模型后门理论 | 即使可见全部模型权重，带后门与正常训练模型的分布仍可在总变差意义下接近。这个构造给白盒检测的可辨识性提供了反例。 |
| <a id="bohbot26a-theory-statistics"></a>[Token Sample Complexity of Attention](https://proceedings.mlr.press/v306/bohbot26a.html) | 注意力理论 | 有限 token 的注意力映射虽有根号样本数收敛率，常数却会随查询半径指数增长。改看输出分布的矩可得到半径依赖更温和的界。 |
| <a id="bollini26b-theory-statistics"></a>[Online Contract Design With Unknown Technology](https://proceedings.mlr.press/v306/bollini26b.html) | 在线机制设计 | 只要委托方掌握潜在动作集合，即使不知道哪些动作实际可用，也可避免原在线合同算法对问题规模的指数依赖。 |
| <a id="bon26a-theory-statistics"></a>[Persuasive Privacy](https://proceedings.mlr.press/v306/bon26a.html) | 隐私定义 | 把隐私写成贝叶斯博弈中的信息价值，可统一解释纯差分隐私和概率差分隐私，并为部分确定性算法定义有意义的隐私保证。 |
| <a id="boncoraglio26a-theory-statistics"></a>[Single-Head Attention in High Dimensions: A Theory of Generalization, Weights Spectra, and Scaling Laws](https://proceedings.mlr.press/v306/boncoraglio26a.html) | 注意力谱分析 | 在高维单头注意力的可分析设定中，模型会按谱成分逐步恢复目标；目标谱具有幂律时，这一过程可产生幂律学习曲线。 |
| <a id="boudou26a-theory-statistics"></a>[Tight Stability Bounds for Robust Distributed Learning: Byzantine Failures Hurt Generalization More than Data Poisoning](https://proceedings.mlr.press/v306/boudou26a.html) | 鲁棒分布式学习 | 本地数据投毒和任意篡改通信可以有相似的优化保证，但后者能造成更大的算法稳定性损失。比较算法时还需核对各威胁下的泛化界。 |
| <a id="boursier26a-theory-statistics"></a>[Softmax as Linear Attention in the Large-Prompt Regime: a Measure-based Perspective](https://proceedings.mlr.press/v306/boursier26a.html) | 长提示注意力 | 足够长的高斯提示下，softmax 注意力可逼近作用于输入测度的线性算子。这个近似可在受控训练轨迹上把线性注意力分析转用到 softmax。 |
| <a id="boushehrian26a-theory-statistics"></a>[Provable Bounds for the Learnability of Sample-Compressible Families from Noisy Samples](https://proceedings.mlr.press/v306/boushehrian26a.html) | 噪声下的分布学习 | 能用少量样本压缩表示的分布族，在独立加性噪声下仍可学习，但要满足可辨识条件；据此可对距离度量分别推导样本界。 |
| <a id="brosamle26a-theory-statistics"></a>[The Expressive Power of Low Precision Softmax Transformers with (Summarized) Chain-of-Thought](https://proceedings.mlr.press/v306/brosamle26a.html) | Transformer 表达力 | 有限精度的 softmax 解码器也可借思维链模拟图灵机。将思维链改成持续摘要后，构造中的模型宽深可按空间界的对数增长。 |
| <a id="burgin26a-theory-statistics"></a>[Beyond Structural Symmetries: Linear Mode Connectivity via Neuron Identifiability](https://proceedings.mlr.press/v306/burgin26a.html) | 权重空间对齐 | 可在数据支持集上识别功能相同的神经元，即使模型没有显式对称性。满足可辨识条件时，独立训练解之间可存在低损失直线路径。 |
| <a id="burla26a-theory-statistics"></a>[All ERMs Can Fail in Stochastic Convex Optimization Lower Bounds in Linear Dimension](https://proceedings.mlr.press/v306/burla26a.html) | 经验风险最小化 | 在一个可学习的随机凸问题中，样本数随维度线性增加时，唯一的经验风险最小解也可能过拟合。这个反例把问题定位到目标本身。 |
| <a id="byun26b-theory-statistics"></a>[Robust Human-AI Complementarity under Uncertainty](https://proceedings.mlr.press/v306/byun26b.html) | 人机预测互补 | 人和模型的错误负相关时，即使用户对双方信息质量了解有限，仍可构造保证期望效用改善的组合决策策略。 |
| <a id="cai26e-theory-statistics"></a>[Privacy-Aware Data Integration for Enhanced Quantile Inference under Heterogeneity](https://proceedings.mlr.press/v306/cai26e.html) | 隐私约束下的分位数估计 | 聚合多个站点的分位估计时，同时惩罚渐近方差和站点偏移。局部差分隐私约束下也能学习权重。 |
| <a id="cai26l-theory-statistics"></a>[Column Thresholding for Sparse Spiked Wigner Models: Improved Signal Strength Requirements](https://proceedings.mlr.press/v306/cai26l.html) | 稀疏尖峰恢复 | 稀疏尖峰含足够大的单个坐标时，列阈值化就能以约为稀疏度平方根的信号强度实现估计和支持集恢复，再用截断幂法精化。 |
| <a id="cao26b-theory-statistics"></a>[On the Robustness of Langevin Dynamics to Score Function Error](https://proceedings.mlr.press/v306/cao26b.html) | 分数误差与 Langevin 采样 | 对某些高维分布，即使估计分数的 Lp 误差任意小，多项式时间的 Langevin 采样仍可能在总变差意义下远离目标。 |
| <a id="cao26l-theory-statistics"></a>[A Control-Theoretic View of Mamba on Stability and Robustness](https://proceedings.mlr.press/v306/cao26l.html) | 选择性状态空间稳定性 | 单个状态矩阵稳定并不能推出任意切换后稳定。可用共同二次 Lyapunov 函数给选择性层建立证书，并从权重计算鲁棒界的常数。 |
| <a id="caucheteux26a-theory-statistics"></a>[A Unifying View of Variational Generative Wasserstein Flows](https://proceedings.mlr.press/v306/caucheteux26a.html) | Wasserstein 生成模型 | 将多个生成算法表示为参数化 JKO 更新，就能比较它们真正不同的目标散度和同一种运输正则；该形式还可扩展到核距离等目标。 |
| <a id="chan26b-theory-statistics"></a>[Continual Learning With Participation Privacy: An Auditable Buffering-Aggregation Recipe](https://proceedings.mlr.press/v306/chan26b.html) | 持续学习参与隐私 | 随机缓冲后按变长批次发布，可把单个用户加入或退出引起的全程位移转成批次邻接问题，从而复用前缀聚合的差分隐私机制。 |
| <a id="chang26f-theory-statistics"></a>[Dynamics Reveals Structure: Challenging the Linear Propagation Assumption](https://proceedings.mlr.press/v306/chang26f.html) | 关系推理的线性传播 | 否定与换序在特定张量分解下可由一阶更新传播，但关系复合需要双线性合取，与否定一般不兼容，限制了局部知识编辑的传播范围。 |
| <a id="chen26p-theory-statistics"></a>[High-Accuracy Sampling for Diffusion Models and Log-Concave Distributions](https://proceedings.mlr.press/v306/chen26p.html) | 扩散采样复杂度 | 若可获得与目标误差相应精度的分数估计，采样步骤对精度倒数可整体达到多对数依赖。复杂度的维度因子在低维流形条件下还可由内在维度替代。 |
| <a id="chen26af-theory-statistics"></a>[Split Group Knockoffs: Controlling False Discovery Rate in Transformational Group Sparsity](https://proceedings.mlr.press/v306/chen26af.html) | 组级变量发现 | 对线性变换后的成组效应构造 Split Knockoffs，可以在控组级假发现率的同时识别相关组，适合评估多个行为维度是否真有差异。 |
<!-- classification:end -->
