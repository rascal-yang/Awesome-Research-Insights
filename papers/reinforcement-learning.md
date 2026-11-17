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
| <a id="bo26c-reinforcement-learning"></a>[Counterfactual Bootstrap for Robust Meta-Reinforcement Learning](https://proceedings.mlr.press/v306/bo26c.html) | 因果元强化学习 | 从与混杂观测相容的候选环境中采样反事实轨迹，再用它们训练策略初始化，显式覆盖多个可能的环境机制。 |
| <a id="bui26a-reinforcement-learning"></a>[Efficient and Uncertainty-Aware Diffusion Framework for Offline-to-Online Reinforcement Learning](https://proceedings.mlr.press/v306/bui26a.html) | 离线到在线强化学习 | 离线从扩散模型蒸馏快采样 actor 和转移模型，在线以 Laplace 近似和状态偏移判断不确定性，帮助在分布变动时调节探索。 |
| <a id="cao26f-reinforcement-learning"></a>[Direct Flow Q-Learning](https://proceedings.mlr.press/v306/cao26f.html) | 流匹配策略优化 | 用最终动作的 Q 值梯度构造每一步速度场的引导项，直接训练多步流策略，避免通过全部采样步骤反传或蒸馏成单步。 |
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
| <a id="liu26aa-reinforcement-learning"></a>[GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization](https://proceedings.mlr.press/v306/liu26aa.html) | 多奖励策略优化 | 先在同一轨迹组内分别归一化各项奖励，再合并优势，避免量级大的奖励淹没其余维度。 [详细解读](../insights/reinforcement-learning.md#normalize-each-reward-before-aggregation) |

<a id="by-data-strategies"></a>

### 数据策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="bendib26a-data-strategies"></a>[Improving Zero-Shot Offline RL via Behavioral Task Sampling](https://proceedings.mlr.press/v306/bendib26a.html) | 零样本离线强化学习 | 从离线数据中的真实行为提取任务向量作为训练任务分布，替换任意随机向量，有助于策略泛化到未见奖励。 |
| <a id="chen26gd-data-strategies"></a>[Transport or Discard: Robust Unbalanced Optimal Transport for Cross-Domain Policy Adaptation](https://proceedings.mlr.press/v306/chen26gd.html) | 跨域离线强化学习的软筛选 | 用非平衡最优传输匹配源域与目标域的转移样本，以广义 KL 惩罚替代固定总运输量约束。按每条源转移的传输边际给离线训练加权，该权重随到目标域的最小匹配代价指数衰减。 |

<a id="by-inference"></a>

### 推理策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="brosseit26a-inference"></a>[Mind the Budget: Accelerating Deep Reinforcement Learning using Constrained Early Exit Neural Networks](https://proceedings.mlr.press/v306/brosseit26a.html) | 强化学习提前退出 | 在 actor 的不同深度挂接出口，训练时用约束线性规划决定性能和计算预算之间的退出规则，部署时用学好的规则直接选择出口。 |
| <a id="chang26a-inference"></a>[The Surprising Difficulty of Search in Model-Based Reinforcement Learning](https://proceedings.mlr.press/v306/chang26a.html) | 模型强化学习搜索 | 搜索可能放大候选轨迹的价值高估，即使动力学模型准确也会选错。对多个价值估计取最小值，可在搜索时降低这种偏差。 |

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
| <a id="cherepanov26a-evaluation"></a>[KAGE-Bench: Fast Known-Axis Visual Generalization Evaluation for Reinforcement Learning](https://proceedings.mlr.press/v306/cherepanov26a.html) | 像素策略的单因素泛化评测 | 保持转移和奖励不变，每个训练与评测配置对只改变一个渲染参数。论文中的 PPO-CNN 有时在背景或图像滤镜变化后仍能向前移动，却无法通关，评测时可同时记录任务完成率和推进程度。 |

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
| <a id="bollini26a-theory-statistics"></a>[Learning in Bayesian Stackelberg Games With Unknown Follower’s Types](https://proceedings.mlr.press/v306/bollini26a.html) | 在线 Stackelberg 博弈 | 领头方不知道对手类型的收益时，只观测最佳响应不足以保证次线性遗憾；如果每轮还能看到类型，则可达到根号轮数量级。 |
| <a id="braverman26a-theory-statistics"></a>[Online Learning with Recency: Algorithms for Sliding-window Streaming Multi-armed Bandits](https://proceedings.mlr.press/v306/braverman26a.html) | 流式多臂老虎机 | 只允许在最近到达的臂里选择时，有限存储使精确找最佳臂困难，近似最佳臂则可用更少内存；可用这一区别决定要保证哪种精度。 |
| <a id="cao26x-theory-statistics"></a>[Understanding Behavior Cloning with Action Quantization](https://proceedings.mlr.press/v306/cao26x.html) | 行为克隆动作量化 | 当动力学稳定且策略满足概率平滑条件时，离散动作上的对数损失可保持最优样本复杂度；量化误差随时域至多多项式放大。 |
| <a id="carr26a-theory-statistics"></a>[Reinforcement Learning with Pairwise Preferences in Long-Term Decision Problems](https://proceedings.mlr.press/v306/carr26a.html) | 长期偏好强化学习 | 将轨迹成对偏好建成马尔可夫竞赛，在该设定下可用定常马尔可夫策略达到依赖完整历史的策略所能达到的表现。 |
| <a id="chen26dy-theory-statistics"></a>[Noise as a Natural Regularizer in Markov Decision Processes: Connecting Environmental Stochasticity and Policy Simplicity](https://proceedings.mlr.press/v306/chen26dy.html) | 重置噪声与有效折扣 | 若每步以概率 1−α 从固定分布重置，且重置概率和分布均与当前状态及动作无关，则折扣为 γ 的含噪 MDP 与折扣为 αγ 的原 MDP 共享最优策略。有效规划范围因此可由保留原转移的概率刻画。 |
| <a id="chen26ef-theory-statistics"></a>[A Causal Decomposition Approach for Fair Contextual Multi-Armed Bandits](https://proceedings.mlr.press/v306/chen26ef.html) | 因果公平约束下的上下文老虎机 | 分别约束受保护属性的反事实直接、间接及伪关联效应，用在线估计和探索补偿项近似可行域，再把镜像下降得到的策略投影进去。在论文的因果识别和约束可行条件下，累积遗憾和约束违反均可次线性增长。 |
| <a id="chen26gk-theory-statistics"></a>[Offline Two-Player Zero-Sum Markov Games with KL Regularization](https://proceedings.mlr.press/v306/chen26gk.html) | 离线零和博弈的 KL 正则估计 | 从末阶段逆推，用最小二乘估计价值，每阶段对双方策略加入相对参考策略的 KL 正则后求鞍点。在数据满足单方偏离覆盖、函数类条件且正则强度与参考策略满足联合约束时，正则博弈的对偶间隙随样本数按约 1/n 衰减。 |
<!-- classification:end -->
