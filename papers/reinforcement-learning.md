# 强化学习

[首页](../README.md) · [参与贡献](../CONTRIBUTING.md) · [English](../en/papers/reinforcement-learning.md)

从交互、反馈和离线经验中学习。

<a id="group-relative-policy-optimization"></a>

## 组相对策略优化

| 论文 | 首次公开 / 发表 | 可借鉴的技术 | 资源 |
| :--- | :--- | :--- | :--- |
| [**GDPO**](https://proceedings.mlr.press/v306/liu26aa.html)<br><sub>Shih-Yang Liu 等, GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization</sub> | [2026-01-08](https://arxiv.org/abs/2601.05242)<br><sub>[ICML 2026](https://proceedings.mlr.press/v306/liu26aa.html)</sub> | [多奖励先分别归一化再聚合](../insights/reinforcement-learning.md#normalize-each-reward-before-aggregation) | [PMLR](https://proceedings.mlr.press/v306/liu26aa.html) · [arXiv](https://arxiv.org/abs/2601.05242) · [代码](https://github.com/NVlabs/GDPO) |

<!-- classification:start -->
## 按技术类型浏览

<a id="by-architecture"></a>

### 模型架构

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="bian26a-architecture"></a>[RN-D: Discretized Categorical Actors for On-Policy Reinforcement Learning](https://proceedings.mlr.press/v306/bian26a.html) | 连续控制动作表示 | 将每个连续动作维度分箱，用分类分布代替高斯策略，并搭配正则化网络，可改善论文所测的 on-policy 控制任务。 |

<a id="by-reinforcement-learning"></a>

### 强化学习方法

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="agrawalla26a-reinforcement-learning"></a>[What Does Flow-Matching Bring to TD-Learning?](https://proceedings.mlr.press/v306/agrawalla26a.html) | 价值函数学习 | 让 flow-matching critic 在训练和读出时都沿速度场积分。后续步可修正中间估计，论文把这个收益与拟合回报分布区分开。 |
| <a id="akgul26a-reinforcement-learning"></a>[Distributional Active Inference](https://proceedings.mlr.press/v306/akgul26a.html) | 分布强化学习 | 把组织感知状态和远期规划的主动推断目标写进分布强化学习框架，使其可以通过无显式转移动力学模型的算法求解。 |
| <a id="anand26a-reinforcement-learning"></a>[Data-Source Adaptive Online Learning under Heteroscedastic Noise](https://proceedings.mlr.press/v306/anand26a.html) | 多来源在线学习 | 在同一轮同时对臂回报建立上置信界、对数据源方差建立下置信界，可逐渐挑出低噪声来源并逼近已知最佳来源的遗憾表现。 |
| <a id="aouali26a-reinforcement-learning"></a>[Off-Policy Learning in Large Action Spaces: Optimization Matters More Than Estimation](https://proceedings.mlr.press/v306/aouali26a.html) | 离策略学习 | 动作空间变大时，统计性质更好的估计器可能带来更难的优化目标。加权对数似然可改善优化，并在实验中学到同等或更好的策略。 |
| <a id="asadulaev26b-reinforcement-learning"></a>[Zero-Shot Off-Policy Learning](https://proceedings.mlr.press/v306/asadulaev26b.html) | 零样本离策略学习 | 通过后继测度计算稳态密度比，在测试遇到新奖励时即时修正离线数据与目标策略的分布差异。 |
| <a id="auzina26a-reinforcement-learning"></a>[Intrinsic Credit Assignment for Long Horizon Interaction](https://proceedings.mlr.press/v306/auzina26a.html) | 长任务信用分配 | 量化中间行动让模型对正确解的信念增加了多少，以此奖励有效提问，并为多步交互提供比最终成败更密集的训练信号。 |
| <a id="bae26a-reinforcement-learning"></a>[Neural Logistic Bandits](https://proceedings.mlr.press/v306/bae26a.html) | 神经逻辑老虎机 | 用避免直接依赖环境维度的自归一化 Bernstein 不等式构造 UCB，使遗憾界随神经特征的有效维度增长。 |
| <a id="bae26c-reinforcement-learning"></a>[LLM-Guided Communication for Cooperative Multi-Agent Reinforcement Learning](https://proceedings.mlr.press/v306/bae26c.html) | 多智能体通信 | 让 LLM 迭代设计通信规则，同时用各智能体的全局状态重建误差及彼此差异来评估规则，避免只有少数成员获得完整信息。 |
| <a id="bagatella26a-reinforcement-learning"></a>[Test-time Offline Reinforcement Learning on Goal-related Experience](https://proceedings.mlr.press/v306/bagatella26a.html) | 目标条件测试时 RL | 根据当前状态选离线数据，再按测试目标评估转移质量，用少量更新在滚动时域内持续微调策略，适配当前这条轨迹。 |
| <a id="basu26a-reinforcement-learning"></a>[Performative Policy Gradient: Optimality in Performative Reinforcement Learning](https://proceedings.mlr.press/v306/basu26a.html) | 部署反馈下的强化学习 | 策略会改变环境动力学时，将这种影响纳入策略梯度。在论文的 softmax 参数化设定里，可收敛到考虑自身引发分布变化的最优策略。 |
| <a id="baur26a-reinforcement-learning"></a>[MAVRL: Learning Reward Functions from Multiple Feedback Types with Amortized Variational Inference](https://proceedings.mlr.press/v306/baur26a.html) | 多反馈奖励学习 | 为示范、比较、评分和停止信号等各自建似然，用共享潜奖励和一个变分目标联合推断，可避免手调不同反馈的损失权重。 |
| <a id="belouadah26a-reinforcement-learning"></a>[CSPO: Constraint-Sensitive Policy Optimization for Safe Reinforcement Learning](https://proceedings.mlr.press/v306/belouadah26a.html) | 安全策略优化 | 用局部一阶近似计算策略到安全边界的有符号距离，把它加入原始策略目标，缓解拉格朗日乘子更新滞后造成的违规与振荡。 |
| <a id="blonde26a-reinforcement-learning"></a>[Noise-Guided Transport: Imitation Learning from Random Priors](https://proceedings.mlr.press/v306/blonde26a.html) | 低数据模仿学习 | 将模仿学习写成从随机先验出发的最优传输问题，用离策略对抗训练求解，可在少量专家转移下学习高维控制，并把不确定性纳入方法。 |
| <a id="liu26aa-reinforcement-learning"></a>[GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization](https://proceedings.mlr.press/v306/liu26aa.html) | 多奖励策略优化 | 先在同一轨迹组内分别归一化各项奖励，再合并优势，避免量级大的奖励淹没其余维度。 [详细解读](../insights/reinforcement-learning.md#normalize-each-reward-before-aggregation) |

<a id="by-data-strategies"></a>

### 数据策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="bendib26a-data-strategies"></a>[Improving Zero-Shot Offline RL via Behavioral Task Sampling](https://proceedings.mlr.press/v306/bendib26a.html) | 零样本离线强化学习 | 从离线数据中的真实行为提取任务向量作为训练任务分布，替换任意随机向量，有助于策略泛化到未见奖励。 |

<a id="by-representation-learning"></a>

### 表征学习

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="bastankhah26a-representation-learning"></a>[Learning to Perceive the World Through Control: Empowerment-Based Representation Learning](https://proceedings.mlr.press/v306/bastankhah26a.html) | 控制相关表征 | 最大化智能体可以对环境施加的影响，会产生描述不同状态信息的前向和后向表征，两者都可对与控制无关的因素保持不变。 |

<a id="by-evaluation"></a>

### 评测与诊断

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="bates26a-evaluation"></a>[Beyond Rewards in RL for Cyber Defence](https://proceedings.mlr.press/v306/bates26a.html) | 防御强化学习奖励 | 用独立于训练奖励的目标评估比较策略。若稀疏成功信号在探索中出现得够频繁，策略可更可靠并减少代价高的动作。 |

<a id="by-theory-statistics"></a>

### 理论与统计

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="abbadi26a-theory-statistics"></a>[What Preferences Can—and Cannot—Predict in Multi-Agent Online Learning](https://proceedings.mlr.press/v306/abbadi26a.html) | 多智能体学习 | 仅比较策略偏好顺序会丢掉收益幅度，同一偏好图允许出现不同的 FTRL 动态。 |
| <a id="anagnostides26b-theory-statistics"></a>[(Doubly) Exponential Lower Bounds for Follow the Regularized Leader in Potential Games](https://proceedings.mlr.press/v306/anagnostides26b.html) | 在线博弈动力学 | 势博弈的结构仍允许 FTRL 收敛至纳什均衡需要指数时间，极端的虚拟对弈在多人博弈中甚至有双指数下界。 |
| <a id="anderson26a-theory-statistics"></a>[The Value Function Semi-Algebraic Set in Partially Observable Markov Decision Processes](https://proceedings.mlr.press/v306/anderson26a.html) | 部分可观测决策 | 无记忆随机策略的可达价值由多项式不等式表示。部分可观测性可引入独立局部极大值，其表现依赖初始状态分布。 |
| <a id="ann26a-theory-statistics"></a>[Generalized Linear Bandits with Memory](https://proceedings.mlr.press/v306/ann26a.html) | 带动作记忆的老虎机 | 当历史动作通过有限记忆影响当前回报时，用分块决策与收缩置信界可把广义线性设定的遗憾控制到平方根量级。 |
| <a id="arora26b-theory-statistics"></a>[Minimax-Optimal Policy Regret in Partially Observable Markov Games](https://proceedings.mlr.press/v306/arora26b.html) | 部分可观测博弈 | 对有记忆的适应性对手，以几何增长的轮次固定候选策略，用累积历史更新乐观似然置信集，可将跨策略切换次数控制在对数量级。 |
| <a id="balagopalan26a-theory-statistics"></a>[Fixed Budget is No Harder Than Fixed Confidence in Best-Arm Identification up to Logarithmic Factors](https://proceedings.mlr.press/v306/balagopalan26a.html) | 最优臂识别 | 用通用转换器包装任意固定置信度算法，可在仅增加对数级样本开销的条件下，把它用于固定预算的最优臂识别。 |
| <a id="balcan26a-theory-statistics"></a>[Learning in Structured Stackelberg Games](https://proceedings.mlr.press/v306/balcan26a.html) | 结构化 Stackelberg 博弈 | 当上下文可以预测追随者类型时，更合适的在线难度度量是 Stackelberg–Littlestone 维数。它能紧致刻画领导者的实例最优遗憾。 |
| <a id="banihashem26a-theory-statistics"></a>[Bandit Social Learning with Exploration Episodes](https://proceedings.mlr.press/v306/banihashem26a.html) | 社会学习探索 | 个体在自己的短回合里有探索动机，整体系统的贝叶斯遗憾仍可能线性增长，设计平台时要单独考虑跨回合的探索。 |
| <a id="barbara26a-theory-statistics"></a>[Optimal Rates for Feasible Payoff Set Estimation in Games](https://proceedings.mlr.press/v306/barbara26a.html) | 逆博弈估计 | 只观察到近似纳什行为时，可用 Hausdorff 距离估计所有与行为相容的收益函数集合，为后续反事实分析保留不可辨识性。 |
| <a id="benyamine26a-theory-statistics"></a>[Dynamic Programming for Epistemic Uncertainty in Markov Decision Processes](https://proceedings.mlr.press/v306/benyamine26a.html) | 不确定 MDP | 把未知转移看作随机分布，对策略回报施加风险度量，并据此判断哪类风险偏好还能沿用 Bellman 递推。 |
<!-- classification:end -->
