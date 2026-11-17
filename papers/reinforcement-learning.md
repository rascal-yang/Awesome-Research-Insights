# 强化学习

[首页](../README.md) · [参与贡献](../CONTRIBUTING.md) · [English](../en/papers/reinforcement-learning.md)

从交互、反馈和离线经验中学习。

<a id="group-relative-policy-optimization"></a>

## 组相对策略优化

| 论文 | 首次公开 / 发表 | 可借鉴的技术 | 资源 |
| :--- | :--- | :--- | :--- |
| [**GDPO**](https://proceedings.mlr.press/v306/liu26aa.html) · [论文卡](../conferences/icml-2026/cards/2801-2900.md#paper-liu26aa)<br><sub>Shih-Yang Liu 等, GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization</sub> | [2026-01-08](https://arxiv.org/abs/2601.05242)<br><sub>[ICML 2026](https://proceedings.mlr.press/v306/liu26aa.html)</sub> | [多奖励先分别归一化再聚合](../insights/reinforcement-learning.md#normalize-each-reward-before-aggregation) | [PMLR](https://proceedings.mlr.press/v306/liu26aa.html) · [arXiv](https://arxiv.org/abs/2601.05242) · [代码](https://github.com/NVlabs/GDPO) |

<!-- classification:start -->
## 按技术类型浏览

<a id="by-architecture"></a>

### 模型架构

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="bian26a-architecture"></a>[RN-D: Discretized Categorical Actors for On-Policy Reinforcement Learning](https://proceedings.mlr.press/v306/bian26a.html) · [论文卡](../conferences/icml-2026/cards/0201-0300.md#paper-bian26a) | 连续控制动作表示 | 将每个连续动作维度分箱，用分类分布代替高斯策略，并搭配正则化网络，可改善论文所测的 on-policy 控制任务。 |

<a id="by-loss-functions"></a>

### 损失函数

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="chen26ep-loss-functions"></a>[Continuity-Regularized Flow Matching for Offline Reinforcement Learning](https://proceedings.mlr.press/v306/chen26ep.html) | 离线强化学习流策略正则 | 从连续性方程导出对动作速度场雅可比矩阵的正则项，用随机雅可比向量积估计范数，再用 Beta 分布加密中间流时刻的采样，约束从噪声到动作的生成路径。 |

<a id="by-optimization"></a>

### 优化

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="corso26a-optimization"></a>[Fast Mixing Steady-State Control in Markov Decision Processes](https://proceedings.mlr.press/v306/corso26a.html) | 目标稳态分布约束下的快速混合 | 在遍历 MDP 中对策略诱导的马尔可夫链施加目标稳态分布约束，以次大奇异值构造混合速度的凸替代目标。对表格 MDP，还可从离线数据估计转移，并分析估计误差对所得策略的影响。 |
| <a id="dam26a-optimization"></a>[Second-Order Smooth Planning with Optimal-Transport Bellman Smoothing](https://proceedings.mlr.press/v306/dam26a.html) | 二阶平滑 Bellman 规划 | 用动作分布上的最优传输平滑构造具有 Lipschitz Hessian 的 Bellman 更新，再以独立估计的交叉乘积无偏估计二阶修正。在固定平滑参数下，误差 ε 的模拟器调用复杂度降至 ε⁻³ 量级，忽略对数因子。 |

<a id="by-reinforcement-learning"></a>

### 强化学习方法

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="agrawalla26a-reinforcement-learning"></a>[What Does Flow-Matching Bring to TD-Learning?](https://proceedings.mlr.press/v306/agrawalla26a.html) · [论文卡](../conferences/icml-2026/cards/0001-0100.md#paper-agrawalla26a) | 价值函数学习 | 让 flow-matching critic 在训练和读出时都沿速度场积分。后续步可修正中间估计，论文把这个收益与拟合回报分布区分开。 |
| <a id="akgul26a-reinforcement-learning"></a>[Distributional Active Inference](https://proceedings.mlr.press/v306/akgul26a.html) · [论文卡](../conferences/icml-2026/cards/0001-0100.md#paper-akgul26a) | 分布强化学习 | 把组织感知状态和远期规划的主动推断目标写进分布强化学习框架，使其可以通过无显式转移动力学模型的算法求解。 |
| <a id="anand26a-reinforcement-learning"></a>[Data-Source Adaptive Online Learning under Heteroscedastic Noise](https://proceedings.mlr.press/v306/anand26a.html) · [论文卡](../conferences/icml-2026/cards/0001-0100.md#paper-anand26a) | 多来源在线学习 | 在同一轮同时对臂回报建立上置信界、对数据源方差建立下置信界，可逐渐挑出低噪声来源并逼近已知最佳来源的遗憾表现。 |
| <a id="aouali26a-reinforcement-learning"></a>[Off-Policy Learning in Large Action Spaces: Optimization Matters More Than Estimation](https://proceedings.mlr.press/v306/aouali26a.html) · [论文卡](../conferences/icml-2026/cards/0101-0200.md#paper-aouali26a) | 离策略学习 | 动作空间变大时，统计性质更好的估计器可能带来更难的优化目标。加权对数似然可改善优化，并在实验中学到同等或更好的策略。 |
| <a id="asadulaev26b-reinforcement-learning"></a>[Zero-Shot Off-Policy Learning](https://proceedings.mlr.press/v306/asadulaev26b.html) · [论文卡](../conferences/icml-2026/cards/0101-0200.md#paper-asadulaev26b) | 零样本离策略学习 | 通过后继测度计算稳态密度比，在测试遇到新奖励时即时修正离线数据与目标策略的分布差异。 |
| <a id="auzina26a-reinforcement-learning"></a>[Intrinsic Credit Assignment for Long Horizon Interaction](https://proceedings.mlr.press/v306/auzina26a.html) · [论文卡](../conferences/icml-2026/cards/0101-0200.md#paper-auzina26a) | 长任务信用分配 | 量化中间行动让模型对正确解的信念增加了多少，以此奖励有效提问，并为多步交互提供比最终成败更密集的训练信号。 |
| <a id="bae26a-reinforcement-learning"></a>[Neural Logistic Bandits](https://proceedings.mlr.press/v306/bae26a.html) · [论文卡](../conferences/icml-2026/cards/0101-0200.md#paper-bae26a) | 神经逻辑老虎机 | 用避免直接依赖环境维度的自归一化 Bernstein 不等式构造 UCB，使遗憾界随神经特征的有效维度增长。 |
| <a id="bae26c-reinforcement-learning"></a>[LLM-Guided Communication for Cooperative Multi-Agent Reinforcement Learning](https://proceedings.mlr.press/v306/bae26c.html) · [论文卡](../conferences/icml-2026/cards/0101-0200.md#paper-bae26c) | 多智能体通信 | 让 LLM 迭代设计通信规则，同时用各智能体的全局状态重建误差及彼此差异来评估规则，避免只有少数成员获得完整信息。 |
| <a id="bagatella26a-reinforcement-learning"></a>[Test-time Offline Reinforcement Learning on Goal-related Experience](https://proceedings.mlr.press/v306/bagatella26a.html) · [论文卡](../conferences/icml-2026/cards/0101-0200.md#paper-bagatella26a) | 目标条件测试时 RL | 根据当前状态选离线数据，再按测试目标评估转移质量，用少量更新在滚动时域内持续微调策略，适配当前这条轨迹。 |
| <a id="basu26a-reinforcement-learning"></a>[Performative Policy Gradient: Optimality in Performative Reinforcement Learning](https://proceedings.mlr.press/v306/basu26a.html) · [论文卡](../conferences/icml-2026/cards/0201-0300.md#paper-basu26a) | 部署反馈下的强化学习 | 策略会改变环境动力学时，将这种影响纳入策略梯度。在论文的 softmax 参数化设定里，可收敛到考虑自身引发分布变化的最优策略。 |
| <a id="baur26a-reinforcement-learning"></a>[MAVRL: Learning Reward Functions from Multiple Feedback Types with Amortized Variational Inference](https://proceedings.mlr.press/v306/baur26a.html) · [论文卡](../conferences/icml-2026/cards/0201-0300.md#paper-baur26a) | 多反馈奖励学习 | 为示范、比较、评分和停止信号等各自建似然，用共享潜奖励和一个变分目标联合推断，可避免手调不同反馈的损失权重。 |
| <a id="belouadah26a-reinforcement-learning"></a>[CSPO: Constraint-Sensitive Policy Optimization for Safe Reinforcement Learning](https://proceedings.mlr.press/v306/belouadah26a.html) · [论文卡](../conferences/icml-2026/cards/0201-0300.md#paper-belouadah26a) | 安全策略优化 | 用局部一阶近似计算策略到安全边界的有符号距离，把它加入原始策略目标，缓解拉格朗日乘子更新滞后造成的违规与振荡。 |
| <a id="blonde26a-reinforcement-learning"></a>[Noise-Guided Transport: Imitation Learning from Random Priors](https://proceedings.mlr.press/v306/blonde26a.html) · [论文卡](../conferences/icml-2026/cards/0201-0300.md#paper-blonde26a) | 低数据模仿学习 | 将模仿学习写成从随机先验出发的最优传输问题，用离策略对抗训练求解，可在少量专家转移下学习高维控制，并把不确定性纳入方法。 |
| <a id="bo26c-reinforcement-learning"></a>[Counterfactual Bootstrap for Robust Meta-Reinforcement Learning](https://proceedings.mlr.press/v306/bo26c.html) · [论文卡](../conferences/icml-2026/cards/0301-0400.md#paper-bo26c) | 因果元强化学习 | 从与混杂观测相容的候选环境中采样反事实轨迹，再用它们训练策略初始化，显式覆盖多个可能的环境机制。 |
| <a id="bui26a-reinforcement-learning"></a>[Efficient and Uncertainty-Aware Diffusion Framework for Offline-to-Online Reinforcement Learning](https://proceedings.mlr.press/v306/bui26a.html) · [论文卡](../conferences/icml-2026/cards/0301-0400.md#paper-bui26a) | 离线到在线强化学习 | 离线从扩散模型蒸馏快采样 actor 和转移模型，在线以 Laplace 近似和状态偏移判断不确定性，帮助在分布变动时调节探索。 |
| <a id="cao26f-reinforcement-learning"></a>[Direct Flow Q-Learning](https://proceedings.mlr.press/v306/cao26f.html) · [论文卡](../conferences/icml-2026/cards/0301-0400.md#paper-cao26f) | 流匹配策略优化 | 用最终动作的 Q 值梯度构造每一步速度场的引导项，直接训练多步流策略，避免通过全部采样步骤反传或蒸馏成单步。 |
| <a id="chen26cc-reinforcement-learning"></a>[Best-of-Both-Worlds for Heavy-Tailed Markov Decision Processes](https://proceedings.mlr.press/v306/chen26cc.html) | 重尾损失下的占用度量更新 | 已知转移时，用随状态动作占用概率变化的阈值跳过极端损失，再用跳过补偿项修正估计并更新 FTRL 策略。在论文的有限 α 阶矩假设下，该估计支持对抗情形的次线性遗憾及满足自约束条件的随机情形的对数遗憾。 |
| <a id="chen26dk-reinforcement-learning"></a>[Multi-Agent Reinforcement Learning with Submodular Reward](https://proceedings.mlr.press/v306/chen26dk.html) | 次模团队奖励的贪心策略 | 固定前面智能体的局部策略，把新智能体带来的团队奖励增量作为它的奖励，再求解单智能体策略。在独立转移、单调次模奖励且动力学已知的设定下，所得策略达到最优价值的一半减去有限采样误差。 |
| <a id="chen26fl-reinforcement-learning"></a>[Policy-Driven World Model Adaptation for Robust Offline Model-based Reinforcement Learning](https://proceedings.mlr.press/v306/chen26fl.html) | 离线强化学习的对抗动力学适配 | 在受离线转移数据约束的范围内，把世界模型更新为降低当前策略回报的响应，并用 Stackelberg 学习让策略更新考虑这一模型响应。在加噪的 MuJoCo 和随机托卡马克控制任务中，所得策略更稳健。 |
| <a id="chen26fn-reinforcement-learning"></a>[VIPO: Value Function Inconsistency Penalized Offline Reinforcement Learning](https://proceedings.mlr.press/v306/chen26fn.html) | 价值一致性约束的离线世界模型 | 在转移拟合之外，再惩罚模型内估计的价值与离线数据直接估计的价值之间的差异，使世界模型的训练兼顾对决策回报有影响的误差。 |
| <a id="cheng26q-reinforcement-learning"></a>[How Does the Lagrangian Guide Safe Reinforcement Learning through Diffusion Models?](https://proceedings.mlr.press/v306/cheng26q.html) | 增广拉格朗日引导安全动作去噪 | 把奖励与安全代价组成的拉格朗日量作为动作去噪的能量，并加入约束违背惩罚来改善能量的局部曲率。在论文分析的条件下，这能稳定采样与训练，并保留最优策略分布。 |
| <a id="cheng26s-reinforcement-learning"></a>[Hybrid Reinforcement Learning in Adversarial Markov Decision Processes](https://proceedings.mlr.press/v306/cheng26s.html) | 对抗 MDP 的混合反馈遗憾控制 | 并行运行使用在线反馈的基学习器和多个离策略基学习器，为后者配置覆盖不同失配程度的学习率，再用元算法组合策略。这样在行为策略覆盖较好时可利用离策略反馈收紧遗憾界，覆盖较差时仍有在线保证。 |
| <a id="cho26f-reinforcement-learning"></a>[Bilinear Bandits with Partially Observable Features](https://proceedings.mlr.press/v306/cho26f.html) | 部分可观测双线性老虎机 | 在用户和物品两侧增添可见特征的正交补基，并以奖励预测和逆倾向校正构造未选组合的伪奖励。直接用双线性 Lasso 拟合，利用诱导出的块对角 Gram 结构精确分块更新。 |
| <a id="choi26k-reinforcement-learning"></a>[Chain-of-Goals Hierarchical Policy for Long-Horizon Offline Goal-Conditioned RL](https://proceedings.mlr.press/v306/choi26k.html) | 离线策略的潜子目标链 | 给定状态和终点，由同一 MLP-Mixer 自回归地从远到近生成潜子目标，再根据整条子目标链预测底层动作。训练以离线轨迹中固定步长采样的状态监督子目标，并用共享价值函数为子目标和动作计算优势权重。 |
| <a id="chu26a-reinforcement-learning"></a>[Value Aggregation with Uncertainty in Online Decentralized MARL](https://proceedings.mlr.press/v306/chu26a.html) | 去中心化 Q 值的不确定性聚合 | 按各智能体两次同步之间对每个状态动作对的访问次数决定聚合权重。访问更充分的估计可获得超过 1 的系数，较不确定的邻居项允许取负，以补偿普通凸平均引起的学习回退。 |
| <a id="chua26a-reinforcement-learning"></a>[Balancing Plasticity and Stability with Fast and Slow Successor Features](https://proceedings.mlr.press/v306/chua26a.html) | 持续漂移下的多时间尺度巩固 | 将巩固机制施加在后继特征上，使快速分量通过新经验更新，较慢分量通过多个时间尺度保留历史。在持续漂移的 MiniWorld 和 MuJoCo 实验里，这比直接巩固 Q 值更有效。 |
| <a id="chung26b-reinforcement-learning"></a>[Offline Reinforcement Learning with Universal Horizon Models](https://proceedings.mlr.press/v306/chung26b.html) | 任意步长的离线强化学习模型 | 以期望预见步数为条件直接预测未来状态，避免逐步在模型自产生的状态上反复推演。训练时按几何分布抽取步数后将超长值压到分位点上，以限制不可靠的远期自举目标。 |
| <a id="croissant26a-reinforcement-learning"></a>[Linear Bandits beyond Inner Product Spaces, the case of Bandit Optimal Transport](https://proceedings.mlr.press/v306/croissant26a.html) | 最优传输老虎机的熵正则探索 | 在希尔伯特空间中用最小二乘构造传输成本的置信集，再选择乐观的运输计划并加入熵惩罚。随着轮数增加减小熵系数，以控制相对未正则化 Kantorovich 最优传输的累积近似误差。 |
| <a id="de-lara26a-reinforcement-learning"></a>[SMAC: Score-Matched Actor-Critics for Robust Offline-to-Online Transfer](https://proceedings.mlr.press/v306/de-lara26a.html) | 离线到在线的动作梯度匹配 | 离线训练时约束 Q 函数对动作的梯度与策略对数密度的动作梯度相匹配，减小切到在线 Actor–Critic 目标时的局部更新冲突。在六个 D4RL 任务上，论文报告了转入 SAC 和 TD3 时的平滑过渡。 |
| <a id="debes26a-reinforcement-learning"></a>[Multivariate Distributional Reinforcement Learning Using Sliced Divergences](https://proceedings.mlr.press/v306/debes26a.html) | 多元回报分布的切片差异 | 沿一维方向投影多元回报，再用 Wasserstein 等一维差异比较分布。共享标量折扣时可对方向均匀平均，面对一般稠密折扣矩阵时，论文以最大投影差异获得相应的 Bellman 收缩结果。 |
| <a id="deng26b-reinforcement-learning"></a>[BFTS: Thompson Sampling with Bayesian Additive Regression Trees](https://proceedings.mlr.press/v306/deng26b.html) | 贝叶斯回归树的 Thompson 采样 | 每个动作独立拟合一个贝叶斯加性回归树模型，从后验抽取各动作的奖励函数并选择当前上下文中预测奖励最高的动作。实验用 MCMC 近似采样，论文的贝叶斯遗憾界针对设定正确且精确采样的情形。 |
| <a id="deng26n-reinforcement-learning"></a>[Sparse Topology-Aware Pairwise Scoring for Large-Scale Multi-Agent Reinforcement Learning](https://proceedings.mlr.press/v306/deng26n.html) | 多智能体通信的稀疏选边 | 先只保留编号相距二的幂次的有向候选边，把每个智能体的候选数限制在对数级。再按智能体状态和边类型评分，用 Gumbel–Sigmoid 学习选择对任务回报有帮助的通信边。 |
| <a id="ding26z-reinforcement-learning"></a>[Sample-Efficient Diffusion-based Reinforcement Learning with Critic Guidance](https://proceedings.mlr.press/v306/ding26z.html) | 评论家引导的扩散策略回归 | 在反向扩散中通过正在估计的干净动作回传 Q 值梯度，将引导方向限制在典型噪声尺度上并保留随机扰动，再用生成的高价值动作作策略回归目标。 |
| <a id="diwan26a-reinforcement-learning"></a>[Trust Region Inverse Reinforcement Learning: Explicit Dual Ascent using Local Policy Updates](https://proceedings.mlr.press/v306/diwan26a.html) | 信赖域逆强化学习的对偶更新 | 沿给定方向大步更新奖励后，在旧策略附近求出信赖域最优策略。在论文的最大因果熵设定下，该策略等价于同方向较小奖励更新的全局最优策略，可用局部搜索推进显式对偶上升。 |
| <a id="dong26d-reinforcement-learning"></a>[TQL: Scaling Q-Functions with Transformers by Preventing Attention Collapse](https://proceedings.mlr.press/v306/dong26d.html) | 大规模 Q 网络的注意力熵控制 | 按层将 Transformer Q 网络的注意力熵拉向目标水平，减轻模型加宽时注意力权重过度集中引发的训练不稳。在所测任务上，这使更大价值网络能带来性能增益。 |
| <a id="dong26m-reinforcement-learning"></a>[Mean Flow Policy Optimization](https://proceedings.mlr.press/v306/dong26m.html) | 少步 MeanFlow 策略优化 | 将动作策略参数化为预测区间平均流速的 MeanFlow 模型，并在软策略迭代中处理动作似然和熵正则策略改进。少步生成保留了动作分布的表达能力，同时在所测控制任务中降低了训练与推理时间。 |
| <a id="doo26a-reinforcement-learning"></a>[Q-Flow: Stable and Expressive Reinforcement Learning with Flow-based Policy](https://proceedings.mlr.press/v306/doo26a.html) | 流策略的中间状态价值优化 | 沿确定性动作流把终端动作价值传给中间潜状态，学习中间价值函数并以其梯度更新速度场。这样可在策略优化时省去对完整数值积分路径反传。 |
| <a id="du26b-reinforcement-learning"></a>[Stabilizing PPO via Latent-Space Regularization and KDE-Driven Exploration](https://proceedings.mlr.press/v306/du26b.html) | PPO 的潜空间新颖性奖励 | 用 critic 隐表示做高斯核密度估计，以负对数密度衡量新颖性。只在转移到的状态超过当批分位阈值时增加该动作的优势，使探索奖励集中于低密度区域。 |
| <a id="du26p-reinforcement-learning"></a>[IEC: When Information-Driven Exploration Meets Spectral Consensus via Primal–Dual Reward Regularization in Decentralized MARL](https://proceedings.mlr.press/v306/du26p.html) | 去中心化探索与共识的原始对偶调节 | 在信息增益和状态新颖性奖励之外，用通信图上邻居策略的分歧约束协作。若本批分歧超过预算就提高惩罚乘子，将探索强度与协调压力的平衡交给原始对偶更新。 |
| <a id="eberhard26b-reinforcement-learning"></a>[Commit to the Bit: Reactive Reinforcement Learning Done Right](https://proceedings.mlr.press/v306/eberhard26b.html) | 状态聚合下的动作承诺 Q 学习 | 进入某个观测特征时选定一个动作，只要观测特征未变就继续执行，直到跨到新特征才重新采样。在有限环境、确定观测映射及论文的重连鲁棒性等条件下，学习得到的贪心策略几乎必然是最优反应式策略。 |
| <a id="edgar26a-reinforcement-learning"></a>[Moment Matching Q-Learning](https://proceedings.mlr.press/v306/edgar26a.html) | 基于矩匹配的少步动作采样 | 用 DDIM 插值从两个噪声时刻生成同一目标时刻的动作样本，以最大均值差异让两条采样路径的分布对齐。策略训练用该分布一致性作行为克隆约束，同时用 Q 值提高动作质量。 |
| <a id="ezer26a-reinforcement-learning"></a>[Stochastic Linear Bandits with Parameter Noise](https://proceedings.mlr.press/v306/ezer26a.html) | 参数噪声下的方差自适应探索 | 对包含标准基向量的动作集，先逐坐标用分组均值的中位数估计期望奖励参数，再按参数估计精度与奖励方差决定何时转为利用。在协方差已知的论文设定中达到相应单位球遗憾界，只差对数因子。 |
| <a id="farebrother26a-reinforcement-learning"></a>[Compositional Planning with Jumpy World Models](https://proceedings.mlr.press/v306/farebrother26a.html) | 跨尺度状态占用的策略组合 | 以策略标识和折扣率条件化状态占用预测模型，用短时域预测自举长时域预测，再组合各预训练策略的多步转移以估计切换序列价值。这样可用策略片段作为长程规划的动作。 |
| <a id="fei26a-reinforcement-learning"></a>[Learning Interpretable Options by Identifying Reward Diffusion Bottlenecks in Reinforcement Learning](https://proceedings.mlr.press/v306/fei26a.html) | 用随机奖励定位探索瓶颈 | 对当前状态估计策略转移前后价值差的平方期望，并在随机奖励函数下汇总该量。高值指向奖励扩散受阻的区域，可据此构造趋近或离开瓶颈的时序扩展动作，无需显式构建状态转移图。 |
| <a id="feng26q-reinforcement-learning"></a>[Offline Reinforcement Learning with Generative Trajectory Policies](https://proceedings.mlr.press/v306/feng26q.html) | 离线策略的生成 ODE 解映射 | 用生成 ODE 的解映射在不同时间点间直接搬运动作样本。训练时以离线动作构造闭式向量场近似，代替不断调用尚在学习的得分模型做多步积分，从而降低算量并稳定监督目标。 |
| <a id="fu26b-reinforcement-learning"></a>[FlowMAP: Flow Matching for Generalizable Agent Planning](https://proceedings.mlr.press/v306/fu26b.html) | 价值引导的规划分布传输 | 学习连续时间速度场，把初始元状态分布推向任务条件下的高价值区域。规划流与执行策略共同训练，再用流传输约束交互诱导的分布变化，减轻环境偏移时的规划误差积累。 |
| <a id="fu26k-reinforcement-learning"></a>[HPS: Hyperspherical Parameter Sharing for Efficient Multi-Agent Reinforcement Learning](https://proceedings.mlr.press/v306/fu26k.html) | 多智能体共享权重的尺度分离 | 将共享主干的权重向量归一化到单位球面，令反传梯度只保留切向分量。用各智能体的尺度生成器单独调节输出幅度，保留共享方向的同时减少尺度梯度冲突。 |
| <a id="fukazawa26a-reinforcement-learning"></a>[RAMAC: Multimodal Risk-Aware Offline Reinforcement Learning and the Role of Behavior Regularization](https://proceedings.mlr.press/v306/fukazawa26a.html) | 生成式离线策略的下尾风险约束 | 用价值模型估计动作回报的分布，对扩散策略优化下尾条件风险价值，同时加入行为克隆正则。这样保留了多峰动作的表达能力，并抑制偏离离线数据的高风险动作。 |
| <a id="gao26ak-reinforcement-learning"></a>[Decentralized Bandits without Global Clock for Dynamic Matching Market](https://proceedings.mlr.press/v306/gao26ak.html) | 无全局时钟的匹配探索 | 动态匹配中，各参与者用本地成功匹配记录更新置信区间，并用本地指针和等待机制调整探索，避免把因竞争被拒的申请计为偏好样本。论文给出任意进出下双边学习的次线性遗憾界。 |
| <a id="genalti26a-reinforcement-learning"></a>[Online Packet Scheduling with Deadlines and Learning](https://proceedings.mlr.press/v306/genalti26a.html) | 未知价值包的限期调度 | 将包类型视为仅在对应包未过期时可选的臂。对截止期最多晚一拍的情形，分别找出即将到期与可等待包中置信上界最高者，再用随调度状态变化的阈值比较，兼顾即刻发送和后续学习。 |
| <a id="gerogiannis26a-reinforcement-learning"></a>[DAL: A Practical Prior-Free Black-Box Framework for Piecewise Stationary Bandits](https://proceedings.mlr.press/v306/gerogiannis26a.html) | 分段平稳老虎机的检测式重启 | 用少量强制探索为变点检测器持续收集反馈，检测到奖励机制变化时重置内部的平稳老虎机算法。将探测与正常选臂解耦，可在不知道变点个数和位置时复用现有平稳算法。 |
| <a id="ghosh26a-reinforcement-learning"></a>[Online Robust Reinforcement Learning with General Function Approximation](https://proceedings.mlr.press/v306/ghosh26a.html) | 在线稳健 Bellman 的对偶拟合 | 用对偶函数统一表示各状态动作处、散度不确定集下的最坏转移备份。在线采样后联合拟合对偶备份和值函数，使一般函数逼近下的分布稳健学习能直接依赖交互数据。 |
| <a id="goyal26a-reinforcement-learning"></a>[Contextual Slate GLM Bandits with Limited Adaptivity](https://proceedings.mlr.press/v306/goyal26a.html) | 有限更新的组合 GLM 赌博机 | 每轮每个槽位选一件商品但只观察整组回报时，用整组的参考组合估计链接函数的导数来缩放特征，避免逐件缩放累积非线性误差。论文在上下文多样性条件下给出了有限策略更新次数的遗憾保证。 |
| <a id="han26i-reinforcement-learning"></a>[Transferable Reinforcement Learning via Probabilistic Latent Embeddings and Dynamic Policy Adaptation for Sim-to-Real Deployment](https://proceedings.mlr.press/v306/han26i.html) | 由环境后验控制仿真到现实的策略风险 | 从现场交互推断环境条件的潜变量分布，再按后验估计精度调节分布式强化学习策略的风险水平。部署初期可更保守，随着环境辨识改善再降低保守程度。 |
| <a id="liu26aa-reinforcement-learning"></a>[GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization](https://proceedings.mlr.press/v306/liu26aa.html) · [论文卡](../conferences/icml-2026/cards/2801-2900.md#paper-liu26aa) | 多奖励策略优化 | 先在同一轨迹组内分别归一化各项奖励，再合并优势，避免量级大的奖励淹没其余维度。 [详细解读](../insights/reinforcement-learning.md#normalize-each-reward-before-aggregation) |

<a id="by-data-strategies"></a>

### 数据策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="bendib26a-data-strategies"></a>[Improving Zero-Shot Offline RL via Behavioral Task Sampling](https://proceedings.mlr.press/v306/bendib26a.html) · [论文卡](../conferences/icml-2026/cards/0201-0300.md#paper-bendib26a) | 零样本离线强化学习 | 从离线数据中的真实行为提取任务向量作为训练任务分布，替换任意随机向量，有助于策略泛化到未见奖励。 |
| <a id="chen26gd-data-strategies"></a>[Transport or Discard: Robust Unbalanced Optimal Transport for Cross-Domain Policy Adaptation](https://proceedings.mlr.press/v306/chen26gd.html) | 跨域离线强化学习的软筛选 | 用非平衡最优传输匹配源域与目标域的转移样本，以广义 KL 惩罚替代固定总运输量约束。按每条源转移的传输边际给离线训练加权，该权重随到目标域的最小匹配代价指数衰减。 |
| <a id="fagan26a-data-strategies"></a>[The Two-Hump Problem: Bridging the Difficulty Gap in Mathematical Reinforcement Learning](https://proceedings.mlr.press/v306/fagan26a.html) | 数学搜索课程的中间难度实例 | 在 Andrews–Curtis 搜索中构造可解但需要多步操作的实例，填补简单例与几乎无法解决例之间的数据缺口。将一组基本变换合成替换动作，可在稀疏成功反馈下缩短策略需要搜索的决策链。 |
| <a id="feng26aa-data-strategies"></a>[Learning Task-Sufficient World Models by Synergizing Agentic Exploration and Structured Modeling](https://proceedings.mlr.press/v306/feng26aa.html) | 世界模型的主动探测数据 | 构建可区分的探测技能库，在新环境中按对世界模型参数的信息增益挑选技能，并兼顾状态覆盖，让后续表征学习获得能区分控制相关潜在因素的轨迹。 |

<a id="by-inference"></a>

### 推理策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="brosseit26a-inference"></a>[Mind the Budget: Accelerating Deep Reinforcement Learning using Constrained Early Exit Neural Networks](https://proceedings.mlr.press/v306/brosseit26a.html) · [论文卡](../conferences/icml-2026/cards/0301-0400.md#paper-brosseit26a) | 强化学习提前退出 | 在 actor 的不同深度挂接出口，训练时用约束线性规划决定性能和计算预算之间的退出规则，部署时用学好的规则直接选择出口。 |
| <a id="chang26a-inference"></a>[The Surprising Difficulty of Search in Model-Based Reinforcement Learning](https://proceedings.mlr.press/v306/chang26a.html) · [论文卡](../conferences/icml-2026/cards/0401-0500.md#paper-chang26a) | 模型强化学习搜索 | 搜索可能放大候选轨迹的价值高估，即使动力学模型准确也会选错。对多个价值估计取最小值，可在搜索时降低这种偏差。 |
| <a id="cui26h-inference"></a>[DRIVE: Distributional and Retrieval-Augmented Bidding with Value Evaluation](https://proceedings.mlr.press/v306/cui26h.html) | 离线竞价的候选生成与价值筛选 | 用高斯混合头采样多个可能的出价，同时检索相近状态下的优质历史出价。推理时把两类候选交给用日志和隐式 Q 学习训练的价值评估器排序，选择估计价值最高的出价。 |
| <a id="gu26a-inference"></a>[SARL: Structure-Aligned Reinforcement Learning for Bridging the Perception-Action Gap in Airspace](https://proceedings.mlr.press/v306/gu26a.html) | 空域避碰策略的运动学约束 | 将安全间隔和航空让行规则写成信号时序逻辑，在推理时依据本机及邻机观测检查并修正策略动作。论文在不同飞机数量的仿真中验证了该约束模块。 |
| <a id="guo26r-inference"></a>[RAD: Retrieval High-quality Demonstrations to Enhance Decision-making](https://proceedings.mlr.press/v306/guo26r.html) | 为离线控制检索可达高回报子目标 | 先查找与当前状态相似的专家轨迹位置，再从其随后的短窗口中挑选回报接近最优的可续接状态。生成模型以所选状态为目标规划到达它的子轨迹，到达后可接续专家轨迹的高回报动作。 |

<a id="by-representation-learning"></a>

### 表征学习

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="bastankhah26a-representation-learning"></a>[Learning to Perceive the World Through Control: Empowerment-Based Representation Learning](https://proceedings.mlr.press/v306/bastankhah26a.html) · [论文卡](../conferences/icml-2026/cards/0201-0300.md#paper-bastankhah26a) | 控制相关表征 | 最大化智能体可以对环境施加的影响，会产生描述不同状态信息的前向和后向表征，两者都可对与控制无关的因素保持不变。 |

<a id="by-evaluation"></a>

### 评测与诊断

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="bates26a-evaluation"></a>[Beyond Rewards in RL for Cyber Defence](https://proceedings.mlr.press/v306/bates26a.html) · [论文卡](../conferences/icml-2026/cards/0201-0300.md#paper-bates26a) | 防御强化学习奖励 | 用独立于训练奖励的目标评估比较策略。若稀疏成功信号在探索中出现得够频繁，策略可更可靠并减少代价高的动作。 |
| <a id="cherepanov26a-evaluation"></a>[KAGE-Bench: Fast Known-Axis Visual Generalization Evaluation for Reinforcement Learning](https://proceedings.mlr.press/v306/cherepanov26a.html) | 像素策略的单因素泛化评测 | 保持转移和奖励不变，每个训练与评测配置对只改变一个渲染参数。论文中的 PPO-CNN 有时在背景或图像滤镜变化后仍能向前移动，却无法通关，评测时可同时记录任务完成率和推进程度。 |
| <a id="guo26f-evaluation"></a>[PolicyGuard: Towards Test-time and Step-level Adversary Defense for Reinforcement Learning Agent](https://proceedings.mlr.press/v306/guo26f.html) | 强化学习后门的逐步不确定性监测 | 给当前状态动作历史拼接多条参考轨迹的未来片段，分别用时序高斯过程估计当前步的后验方差，再汇总为异常分数。由此可在完整轨迹尚不可见时逐步监测策略的后门行为。 |

<a id="by-theory-statistics"></a>

### 理论与统计

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="abbadi26a-theory-statistics"></a>[What Preferences Can—and Cannot—Predict in Multi-Agent Online Learning](https://proceedings.mlr.press/v306/abbadi26a.html) · [论文卡](../conferences/icml-2026/cards/0001-0100.md#paper-abbadi26a) | 多智能体学习 | 仅比较策略偏好顺序会丢掉收益幅度，同一偏好图允许出现不同的 FTRL 动态。 |
| <a id="anagnostides26b-theory-statistics"></a>[(Doubly) Exponential Lower Bounds for Follow the Regularized Leader in Potential Games](https://proceedings.mlr.press/v306/anagnostides26b.html) · [论文卡](../conferences/icml-2026/cards/0001-0100.md#paper-anagnostides26b) | 在线博弈动力学 | 势博弈的结构仍允许 FTRL 收敛至纳什均衡需要指数时间，极端的虚拟对弈在多人博弈中甚至有双指数下界。 |
| <a id="anderson26a-theory-statistics"></a>[The Value Function Semi-Algebraic Set in Partially Observable Markov Decision Processes](https://proceedings.mlr.press/v306/anderson26a.html) · [论文卡](../conferences/icml-2026/cards/0001-0100.md#paper-anderson26a) | 部分可观测决策 | 无记忆随机策略的可达价值由多项式不等式表示。部分可观测性可引入独立局部极大值，其表现依赖初始状态分布。 |
| <a id="ann26a-theory-statistics"></a>[Generalized Linear Bandits with Memory](https://proceedings.mlr.press/v306/ann26a.html) · [论文卡](../conferences/icml-2026/cards/0001-0100.md#paper-ann26a) | 带动作记忆的老虎机 | 当历史动作通过有限记忆影响当前回报时，用分块决策与收缩置信界可把广义线性设定的遗憾控制到平方根量级。 |
| <a id="arora26b-theory-statistics"></a>[Minimax-Optimal Policy Regret in Partially Observable Markov Games](https://proceedings.mlr.press/v306/arora26b.html) · [论文卡](../conferences/icml-2026/cards/0101-0200.md#paper-arora26b) | 部分可观测博弈 | 对有记忆的适应性对手，以几何增长的轮次固定候选策略，用累积历史更新乐观似然置信集，可将跨策略切换次数控制在对数量级。 |
| <a id="balagopalan26a-theory-statistics"></a>[Fixed Budget is No Harder Than Fixed Confidence in Best-Arm Identification up to Logarithmic Factors](https://proceedings.mlr.press/v306/balagopalan26a.html) · [论文卡](../conferences/icml-2026/cards/0101-0200.md#paper-balagopalan26a) | 最优臂识别 | 用通用转换器包装任意固定置信度算法，可在仅增加对数级样本开销的条件下，把它用于固定预算的最优臂识别。 |
| <a id="balcan26a-theory-statistics"></a>[Learning in Structured Stackelberg Games](https://proceedings.mlr.press/v306/balcan26a.html) · [论文卡](../conferences/icml-2026/cards/0101-0200.md#paper-balcan26a) | 结构化 Stackelberg 博弈 | 当上下文可以预测追随者类型时，更合适的在线难度度量是 Stackelberg–Littlestone 维数。它能紧致刻画领导者的实例最优遗憾。 |
| <a id="banihashem26a-theory-statistics"></a>[Bandit Social Learning with Exploration Episodes](https://proceedings.mlr.press/v306/banihashem26a.html) · [论文卡](../conferences/icml-2026/cards/0201-0300.md#paper-banihashem26a) | 社会学习探索 | 个体在自己的短回合里有探索动机，整体系统的贝叶斯遗憾仍可能线性增长，设计平台时要单独考虑跨回合的探索。 |
| <a id="barbara26a-theory-statistics"></a>[Optimal Rates for Feasible Payoff Set Estimation in Games](https://proceedings.mlr.press/v306/barbara26a.html) · [论文卡](../conferences/icml-2026/cards/0201-0300.md#paper-barbara26a) | 逆博弈估计 | 只观察到近似纳什行为时，可用 Hausdorff 距离估计所有与行为相容的收益函数集合，为后续反事实分析保留不可辨识性。 |
| <a id="benyamine26a-theory-statistics"></a>[Dynamic Programming for Epistemic Uncertainty in Markov Decision Processes](https://proceedings.mlr.press/v306/benyamine26a.html) · [论文卡](../conferences/icml-2026/cards/0201-0300.md#paper-benyamine26a) | 不确定 MDP | 把未知转移看作随机分布，对策略回报施加风险度量，并据此判断哪类风险偏好还能沿用 Bellman 递推。 |
| <a id="bollini26a-theory-statistics"></a>[Learning in Bayesian Stackelberg Games With Unknown Follower’s Types](https://proceedings.mlr.press/v306/bollini26a.html) · [论文卡](../conferences/icml-2026/cards/0301-0400.md#paper-bollini26a) | 在线 Stackelberg 博弈 | 领头方不知道对手类型的收益时，只观测最佳响应不足以保证次线性遗憾；如果每轮还能看到类型，则可达到根号轮数量级。 |
| <a id="braverman26a-theory-statistics"></a>[Online Learning with Recency: Algorithms for Sliding-window Streaming Multi-armed Bandits](https://proceedings.mlr.press/v306/braverman26a.html) · [论文卡](../conferences/icml-2026/cards/0301-0400.md#paper-braverman26a) | 流式多臂老虎机 | 只允许在最近到达的臂里选择时，有限存储使精确找最佳臂困难，近似最佳臂则可用更少内存；可用这一区别决定要保证哪种精度。 |
| <a id="cao26x-theory-statistics"></a>[Understanding Behavior Cloning with Action Quantization](https://proceedings.mlr.press/v306/cao26x.html) · [论文卡](../conferences/icml-2026/cards/0401-0500.md#paper-cao26x) | 行为克隆动作量化 | 当动力学稳定且策略满足概率平滑条件时，离散动作上的对数损失可保持最优样本复杂度；量化误差随时域至多多项式放大。 |
| <a id="carr26a-theory-statistics"></a>[Reinforcement Learning with Pairwise Preferences in Long-Term Decision Problems](https://proceedings.mlr.press/v306/carr26a.html) · [论文卡](../conferences/icml-2026/cards/0401-0500.md#paper-carr26a) | 长期偏好强化学习 | 将轨迹成对偏好建成马尔可夫竞赛，在该设定下可用定常马尔可夫策略达到依赖完整历史的策略所能达到的表现。 |
| <a id="chen26dy-theory-statistics"></a>[Noise as a Natural Regularizer in Markov Decision Processes: Connecting Environmental Stochasticity and Policy Simplicity](https://proceedings.mlr.press/v306/chen26dy.html) | 重置噪声与有效折扣 | 若每步以概率 1−α 从固定分布重置，且重置概率和分布均与当前状态及动作无关，则折扣为 γ 的含噪 MDP 与折扣为 αγ 的原 MDP 共享最优策略。有效规划范围因此可由保留原转移的概率刻画。 |
| <a id="chen26ef-theory-statistics"></a>[A Causal Decomposition Approach for Fair Contextual Multi-Armed Bandits](https://proceedings.mlr.press/v306/chen26ef.html) | 因果公平约束下的上下文老虎机 | 分别约束受保护属性的反事实直接、间接及伪关联效应，用在线估计和探索补偿项近似可行域，再把镜像下降得到的策略投影进去。在论文的因果识别和约束可行条件下，累积遗憾和约束违反均可次线性增长。 |
| <a id="chen26gk-theory-statistics"></a>[Offline Two-Player Zero-Sum Markov Games with KL Regularization](https://proceedings.mlr.press/v306/chen26gk.html) | 离线零和博弈的 KL 正则估计 | 从末阶段逆推，用最小二乘估计价值，每阶段对双方策略加入相对参考策略的 KL 正则后求鞍点。在数据满足单方偏离覆盖、函数类条件且正则强度与参考策略满足联合约束时，正则博弈的对偶间隙随样本数按约 1/n 衰减。 |
| <a id="drago26a-theory-statistics"></a>[Online Compatible Reward Identification from Preference Feedback](https://proceedings.mlr.press/v306/drago26a.html) | 偏好查询基的方差瓶颈 | 在 Bradley–Terry 比较下，用一组线性独立的轨迹差来识别兼容奖励。以集合中最小的伯努利反馈方差衡量其可估计性，优先选择能覆盖奖励方向且比较结果未过度饱和的查询基。 |
| <a id="ebi26a-theory-statistics"></a>[Informed Asymmetric Actor-Critic: Leveraging Privileged Signals Beyond Full-State Access](https://proceedings.mlr.press/v306/ebi26a.html) | 部分可观测强化学习的特权评论家 | 让 actor 仅使用观测历史，critic 在训练时另接收任意依赖环境状态的特权信号。给定历史时，对额外信号求条件平均即可回到原动作价值，因此在论文的信息结构下，所得策略梯度等于标准梯度。 |
| <a id="escamilla26a-theory-statistics"></a>[When Can You Poison Rewards? A Tight Characterization of Reward Poisoning in Linear MDPs](https://proceedings.mlr.press/v306/escamilla26a.html) | 线性 MDP 的奖励投毒可行性 | 将有限步线性 MDP 的可攻击性化为凸二次规划，最大化目标动作对竞争动作的最小价值间隔，同时保留目标策略所访问动作上的奖励。按论文的预算条件，最优间隔为正恰好对应可攻击。 |
| <a id="faizal26a-theory-statistics"></a>[Local Policies for Graph-Structured Markov Decision Processes](https://proceedings.mlr.press/v306/faizal26a.html) | 图结构 MDP 的局部策略近似 | 用 Dobrushin 型矩阵控制节点状态和动作扰动向远处传播的幅度。满足论文的稳定性条件时，每个智能体仅读取 m 跳邻域就可近似全局最优，性能差距随 m 指数下降。 |
| <a id="flynn26b-theory-statistics"></a>[Posterior Sampling Reinforcement Learning with Gaussian Processes for Continuous Control: Sublinear Regret Bounds for Unbounded State Spaces](https://proceedings.mlr.press/v306/flynn26b.html) | 无界状态空间的高斯过程后验采样 | 递归应用高斯过程的极值集中界，对实际访问的状态建立高概率有界区域，再在该区域内用链式界控制后验采样误差。在论文的弱光滑条件下，Bayes 遗憾随有效信息增益和交互时长的乘积平方根增长，另有时域长度因子。 |
| <a id="gauthier26a-theory-statistics"></a>[Anytime Detection of Strategic Deviations in Multi-Agent Systems](https://proceedings.mlr.press/v306/gauthier26a.html) | 重复博弈中的任意时偏离检测 | 按收益违背均衡条件的程度递推 e 值，使零假设下的证据过程成为超鞅。在线监视何时越过阈值，可在适时停止的同时控制误报，并用同一框架检测多种均衡假设。 |
| <a id="ghugare26a-theory-statistics"></a>[On the Role of Computation in Reinforcement Learning](https://proceedings.mlr.press/v306/ghugare26a.html) | 策略计算预算与长程泛化 | 按执行计算上限将策略分层，可以构造低预算策略在训练任务上达到最优、却在更长测试任务上明显落后的情形。论文以参数共享的循环策略检验这一差异，通过增加循环次数扩大计算预算。 |
| <a id="giorgi26a-theory-statistics"></a>[Impact of Connectivity on Laplacian Representations in Reinforcement Learning](https://proceedings.mlr.press/v306/giorgi26a.html) | 状态图谱特征的价值误差分解 | 用状态图拉普拉斯的低频特征线性拟合价值函数时，误差界包含截断项和特征估计项。前者受图的代数连通度及首个被舍弃的特征值控制，后者取决于保留边界处的谱间隙及特征优化误差。 |
| <a id="gong26i-theory-statistics"></a>[The Cost of Information: Phase Transitions in Contextual Bandits with Paid Observations](https://proceedings.mlr.press/v306/gong26i.html) | 付费观测的免费预算相变 | 把观察动作的费用纳入上下文老虎机的累计遗憾，免费预算低于临界量时主要抵扣费用，高于临界量时可改善遗憾的渐近阶。按预算相对阈值切换策略，可在两个区间都接近下界。 |
<!-- classification:end -->
