# NeurIPS 2026 论文卡 11

[会议索引](README.md)

<a id="paper-148157"></a>

## Selective Safety Steering via Value-Filtered Decoding

[官方论文页](https://neurips.cc/virtual/2026/poster/148157) · [作者来源](https://openreview.net/forum?id=zsrEQJOOeK)

- **问题 / 瓶颈** · 常开控制会影响正常帮助度。
- **核心创新 / 方法** · 值估计过滤解码期的安全转向。
- **Baseline** · 现有推理转向。
- **Benchmark** · 多安全数据集，安全、帮助度和与底座相似。
- **关键结果 / 消融** · 权衡优于比较对象，幅度未报告。
- **适用条件 / 局限** · 需防御价值估计的独立校准。

**可复用机制** · 安全过滤同时管漏干预和无必要干预。

<a id="paper-148701"></a>

## Selectivity and Shape in the Design of Forward-Forward Goodness Functions

[官方论文页](https://neurips.cc/virtual/2026/poster/148701) · [作者来源](https://openreview.net/forum?id=vh5aoPi2ke)

- **问题 / 瓶颈** · 总能量可能掩盖少量判别激活。
- **核心创新 / 方法** · 对比 top-k、entmax、峰度及高阶矩，并配标签分离。
- **Baseline** · 平方和 goodness。
- **Benchmark** · 13 函数、5 激活、6 数据集。
- **关键结果 / 消融** · Fashion-MNIST 89%，MNIST 98.2±0.1%。
- **适用条件 / 局限** · 组合改变多个因素，适用规模待验。

**可复用机制** · 局部训练指标分别控制活跃单元选择和分布形状。

<a id="paper-150042"></a>

## Selectivity Makes State-Space Models Universal Sequence Approximators

[官方论文页](https://neurips.cc/virtual/2026/poster/150042) · [作者来源](https://openreview.net/forum?id=lD881YL8Tk)

- **问题 / 瓶颈** · 固定更新的表达能力受限。
- **核心创新 / 方法** · 证明简单选择式写入足以普遍逼近。
- **Baseline** · 固定状态更新。
- **Benchmark** · 固定时域的因果序列规则。
- **关键结果 / 消融** · 给出选择状态空间通用性。
- **适用条件 / 局限** · 定长逼近不保证训练可达或无限长外推。

**可复用机制** · 选择性更新可承担表达能力，不必由全量注意力承担。

<a id="paper-150022"></a>

## Select Smarter, Not More? Prompt-Aware Evaluation Scheduling with Submodular Guarantees

[官方论文页](https://neurips.cc/virtual/2026/poster/150022) · [作者来源](https://openreview.net/forum?id=lL7J1xH02I)

- **问题 / 瓶颈** · 静态样本不区分后期候选，启发更新会抖动。
- **核心创新 / 方法** · 用兼顾区分、覆盖和有限更新的单调次模目标。
- **Baseline** · 预固定子集、启发更新。
- **Benchmark** · 提示优化多任务。
- **关键结果 / 消融** · 给约 1−1/e 冷启保证，收益集中在未饱和任务。
- **适用条件 / 局限** · 依赖轮间漂移有界。

**可复用机制** · 将评测样本用于区分当前假设而保持覆盖。

<a id="paper-153170"></a>

## Select-then-differentiate: Solving Bilevel Optimization with Manifold Lower-level Solution Sets

[官方论文页](https://neurips.cc/virtual/2026/poster/153170) · [作者来源](https://openreview.net/forum?id=NLXLf4kGZu)

- **问题 / 瓶颈** · 标准双层公式要求唯一内层解。
- **核心创新 / 方法** · 局部 PL 下以唯一选择和伪逆算超梯度。
- **Baseline** · 内层单解的经典公式。
- **Benchmark** · 内层解流形及外层驻点分析。
- **关键结果 / 消融** · 复杂度由解流形内在维度控制。
- **适用条件 / 局限** · 选择唯一与局部正则条件关键。

**可复用机制** · 模型选择和 hypergradient 可分别诊断，不强迫低层全局唯一。

<a id="paper-152160"></a>

## Self-Adjoint Flow Policy Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/152160) · [作者来源](https://openreview.net/forum?id=V4bnZAJAx7)

- **问题 / 瓶颈** · 数值逆映射和前向采样可能不一致。
- **核心创新 / 方法** · 同一对称规则反向步长即给逆映射。
- **Baseline** · 现有在策略生成控制。
- **Benchmark** · 八项 IsaacLab 连续控制。
- **关键结果 / 消融** · 可计算似然并与采样规则一致，实证数值待核。
- **适用条件 / 局限** · 依赖数值规则和控制实现。

**可复用机制** · 架构与积分器共同保证概率更新所需一致性。

<a id="paper-153048"></a>

## Self-Calibrated GUI Reward Model via Inverse Dynamic Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/153048) · [作者来源](https://openreview.net/forum?id=OPejG5R0IO)

- **问题 / 瓶颈** · 只看到动后界面可能误判成功。
- **核心创新 / 方法** · 逆动力从状态变化检查执行动作，为奖励做运行期校准。
- **Baseline** · 普通 GUI 评委。
- **Benchmark** · OSWorld、ScienceBoard、AndroidWorld。
- **关键结果 / 消融** · RL 收敛加快，最终表现和域外泛化改善。
- **适用条件 / 局限** · 依赖动作可逆识别，等效动作需单测。

**可复用机制** · 给奖励模型加独立的操作因果一致性检查。

<a id="paper-155247"></a>

## Self-Cleaning Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155247) · [作者来源](https://openreview.net/forum?id=79S41XUgZr)

- **问题 / 瓶颈** · 生成器可能继承低质量样本。
- **核心创新 / 方法** · 基于输运的自清理，并比较源外样本到目标分布距离。
- **Baseline** · 常规扩散。
- **Benchmark** · 合成污染、多样性和数据质量。
- **关键结果 / 消融** · 理论给距离改善条件，实证有优势。
- **适用条件 / 局限** · 代理净化质量与潜在偏差需验证。

**可复用机制** · 清理闭环先测投影后是否损失罕见真实结构。

<a id="paper-155897"></a>

## Self-Compacting Language Model Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/155897) · [作者来源](https://openreview.net/forum?id=21IUMTFqTe)

- **问题 / 瓶颈** · 固定 token 截断会抹掉尚未完成推导。
- **核心创新 / 方法** · 代理自己调用压缩工具，以收敛和中断状态定义量表。
- **Baseline** · 固定间隔和 token 门限。
- **Benchmark** · 长期代理轨迹。
- **关键结果 / 消融** · 提出无需改权重的压缩决策；摘要数值待核。
- **适用条件 / 局限** · 模型判断进度失准时需兜底。

**可复用机制** · 用语义边界管理压缩，而非用长度近似边界。

<a id="paper-148960"></a>

## Self-Consuming Generative Models with Co-Evolving Human Preferences

[官方论文页](https://neurips.cc/virtual/2026/poster/148960) · [作者来源](https://openreview.net/forum?id=tsXMIKjzrO)

- **问题 / 瓶颈** · 用户偏好与模型共演化放大初始优势。
- **核心创新 / 方法** · 联合选参照分布和混合权重控制平衡与采集成本。
- **Baseline** · 纯用户筛选合成训练。
- **Benchmark** · 迭代混合动力学与平衡。
- **关键结果 / 消融** · 纯合成可收敛到单一主导实例。
- **适用条件 / 局限** · 结论依赖偏好和更新模型。

**可复用机制** · 长期合成训练监测属性占用，并保留独立数据锚。

<a id="paper-151765"></a>

## Self-Correction as Transition Geometry: Internalizing Reasoning via Lifted State Policy Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/151765) · [作者来源](https://openreview.net/forum?id=YDIiUo61NU)

- **问题 / 瓶颈** · 显式反复修订提高延迟。
- **核心创新 / 方法** · 文字答案附连续细化状态，以能量下降和编辑步惩罚训练。
- **Baseline** · 显式修订及部件消融。
- **Benchmark** · Qwen3.5 多数学、科学、代码、逻辑任务。
- **关键结果 / 消融** · 聚合准确率更高且跳过上线修订轮。
- **适用条件 / 局限** · 能量排序和后训练迁移需单独评测。

**可复用机制** · 将纠错当局部转换策略学，再蒸馏为单次生成。

<a id="paper-152280"></a>

## SelfCritic-VLA: Language as Intrinsic Critic for Vision Language Action Models in Autonomous Driving

[官方论文页](https://neurips.cc/virtual/2026/poster/152280) · [作者来源](https://openreview.net/forum?id=UGQKMlMM5j)

- **问题 / 瓶颈** · 只产轨迹无显式后果评估。
- **核心创新 / 方法** · 训练对照候选轨迹和语义反馈，再 GRPO 学批评条件下细化。
- **Baseline** · 普通驾驶 VLA。
- **Benchmark** · 长尾闭环驾驶。
- **关键结果 / 消融** · 摘要说明方法，具体数字待核。
- **适用条件 / 局限** · 反事实候选及人类验收决定语义质量。

**可复用机制** · 单测动作批评能否引发实际轨迹修正。

<a id="paper-150397"></a>

## Self-Distillation of Hidden Layers for Masked Self-Supervised Representation Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/150397) · [作者来源](https://openreview.net/forum?id=iLR53jV2Bg)

- **问题 / 瓶颈** · 单层蒸馏可能偏向某一抽象尺度。
- **核心创新 / 方法** · 学生预测各深度教师隐表示。
- **Baseline** · 可比潜预测基线。
- **Benchmark** · 掩码自监督表示学习。
- **关键结果 / 消融** · 摘要报告显著增益，具体完整数字待核。
- **适用条件 / 局限** · 教师层选取及训练成本影响结果。

**可复用机制** · 对多尺度迁移任务用多层监督保留不同抽象维度。

<a id="paper-152431"></a>

## Self-Distilled RLVR

[官方论文页](https://neurips.cc/virtual/2026/poster/152431) · [作者来源](https://openreview.net/forum?id=TAt6jrbMb8)

- **问题 / 瓶颈** · 只模仿见过答案的教师可能泄漏信息且长期训练不稳定。
- **核心创新 / 方法** · RLSD 将特权教师信号与环境验证分工。
- **Baseline** · 普通 RLVR 和仅靠在线自蒸馏。
- **Benchmark** · 可验证推理训练及收敛稳定性，摘要未列基准。
- **关键结果 / 消融** · 作者报告更高收敛上限和更好稳定性。
- **适用条件 / 局限** · 依赖可验证结果和特权教师，摘要未给数值。

**可复用机制** · 让稀疏但可靠的外部奖励决定学习正负号，再用密集教师信息调节更新幅度。

<a id="paper-148772"></a>

## Self-Evolution Reasoner: Continuous Optimization via Policy-Intrinsic Exploration and Exploitation

[官方论文页](https://neurips.cc/virtual/2026/poster/148772) · [作者来源](https://openreview.net/forum?id=vAhTbJQW5J)

- **问题 / 瓶颈** · 随机探索易卡在局部最优，外部示范又存在策略分布差。
- **核心创新 / 方法** · SEPO 以标签引导探索，并利用当前策略生成的可行解继续优化。
- **Baseline** · 标准探索和借用外部演示的训练方式。
- **Benchmark** · 多个推理领域，在相同训练时间或步数下比较。
- **关键结果 / 消融** · 作者报告困难任务和小模型上仍能持续改进。
- **适用条件 / 局限** · 依赖标签与可检查结果，摘要未给逐任务得分。

**可复用机制** · 先给少量结果信息帮助策略生成自己的可行轨迹，再把训练放回其能执行的推理分布。

<a id="paper-150784"></a>

## SelfGuard: Self-Supervised Deviation Modeling for Multi-Modal Jailbreak Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/150784) · [作者来源](https://openreview.net/forum?id=fQrMmdCmbG)

- **问题 / 瓶颈** · 只记历史恶意模式的检测器易随输入变化退化。
- **核心创新 / 方法** · 自监督建模良性规律，部署时聚合多个语义、格式和一致性偏差信号。
- **Baseline** · 针对已知样例训练的检测器。
- **Benchmark** · 多个多模态基准，摘要未列名称。
- **关键结果 / 消融** · 作者报告方法有效。
- **适用条件 / 局限** · 需要足够代表实际环境的良性数据，摘要未给误报率。

**可复用机制** · 对难以提前枚举的异常，可先估计正常的跨模态关系，同时校验良性变体的误报。

<a id="paper-155539"></a>

## Self-Improving World Modelling with Latent Actions

[官方论文页](https://neurips.cc/virtual/2026/poster/155539) · [作者来源](https://openreview.net/forum?id=4ow6O2MFtV)

- **问题 / 瓶颈** · 只用状态序列难区分何种动作引起变化。
- **核心创新 / 方法** · SWIRL 交替最大化生成状态与潜动作的条件互信息，以及逆模型解释观测转移的证据下界。
- **Baseline** · 现有世界建模方法，摘要未列名称。
- **Benchmark** · Aurora-Bench、ByteMorph、WorldPredictionBench、StableToolBench，以及单轮多轮视觉动态。
- **关键结果 / 消融** · 摘要分别报告 16%、28%、16%、14% 增益。
- **适用条件 / 局限** · 潜动作的一致性不等同真实控制变量，摘要未给可辨识边界。

**可复用机制** · 没有配对控制日志时，让前向可控性与逆向可解释性互相提供监督。

<a id="paper-151252"></a>

## Self-Organized Conformal Prediction: Reducing Regional Coverage Gaps with Unsupervised Group Discovery

[官方论文页](https://neurips.cc/virtual/2026/poster/151252) · [作者来源](https://openreview.net/forum?id=bl6vZeiL9I)

- **问题 / 瓶颈** · 全局保序校准可能盖住房间子群覆盖率不足。
- **核心创新 / 方法** · 用自组织映射做无监督分组，再从匹配单元或固定邻域抽校准样本。
- **Baseline** · 全局校准及局部共形分位数方法。
- **Benchmark** · 回归与分类，表格和图像嵌入，考察区域覆盖缺口。
- **关键结果 / 消融** · 单元检索有精确有效性，邻域中心单元保证包含 KS 偏差项。
- **适用条件 / 局限** · 依赖组内校准数据与交换性条件，邻域保证较弱。

**可复用机制** · 校准可独立于预测模型按表征几何分组，用局部覆盖检查整体平均掩盖的误差。

<a id="paper-155496"></a>

## Self-Recognition Finetuning can Reverse and Prevent Emergent Misalignment

[官方论文页](https://neurips.cc/virtual/2026/poster/155496) · [作者来源](https://openreview.net/forum?id=59CXcl41Fa)

- **问题 / 瓶颈** · 微调可能破坏先前对齐行为，普通良性训练的作用难区分。
- **核心创新 / 方法** · 比较自生成文本识别和多种良性训练，测预防及逆转。
- **Baseline** · 正确领域数据、常识和计数任务的良性微调。
- **Benchmark** · GPT-4.1、Qwen2.5-32B-Instruct、Seed-OSS-36B-Instruct 与多种误对齐数据。
- **关键结果 / 消融** · 摘要报告识别训练对预防和逆转有效，逆转并非该方法独有。
- **适用条件 / 局限** · 摘要未给跨任务效应量或预防适用范围。

**可复用机制** · 行为保护应分开测试损伤前后的干预效果，避免用逆转结论代替预防证据。

<a id="paper-149029"></a>

## Self-Rewarded Multimodal Coherent Reasoning Across Diverse Visual Domains

[官方论文页](https://neurips.cc/virtual/2026/poster/149029) · [作者来源](https://openreview.net/forum?id=tMbUp1FMia)

- **问题 / 瓶颈** · 单一过程分数易奖励重复或自信但不看图的输出。
- **核心创新 / 方法** · 聚合语义、词汇、非冗余、视觉依据及步骤一致性，用置信降温稳定 GRPO。
- **Baseline** · 同规模开源模型及去掉单项奖励和降温的消融。
- **Benchmark** · 广泛视觉基准，考察平均正确率与连贯性。
- **关键结果 / 消融** · 7B 模型平均 81.4%，作者报告消融支持各项贡献。
- **适用条件 / 局限** · 依赖自评对证据的识别能力，摘要未给独立外部验证。

**可复用机制** · 没有人工轨迹时可分列答案依据、步骤一致性及重复惩罚，再控制过度自信。

<a id="paper-150689"></a>

## Self-Rewarding Sequential Monte Carlo for Masked Diffusion Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150689) · [作者来源](https://openreview.net/forum?id=gFBldFk335)

- **问题 / 瓶颈** · 局部高置信揭掩码过于贪心且对噪声敏感。
- **核心创新 / 方法** · 运行多个扩散粒子，以轨迹级置信度迭代加权和重采样。
- **Baseline** · 常规局部置信度的单轨迹扩散解码。
- **Benchmark** · 多种掩码语言模型和任务，摘要未列名称。
- **关键结果 / 消融** · 摘要报告无训练与外部奖励也可改善生成。
- **适用条件 / 局限** · 需要多并行采样，摘要未给等算力或置信误校准影响。

**可复用机制** · 长序列候选可用分批竞争的轨迹提高多样性，不必只提交每步最可信预测。

<a id="paper-153105"></a>

## Self-Supervised Doppler-Guided RF Odometry

[官方论文页](https://neurips.cc/virtual/2026/poster/153105) · [作者来源](https://openreview.net/forum?id=Nurtj1O5Ei)

- **问题 / 瓶颈** · 无纹理环境下纯几何匹配退化。
- **核心创新 / 方法** · 用周期一致的对比随机游走匹配时空单元，再用多普勒一致性约束位移。
- **Baseline** · 既有射频里程计方法。
- **Benchmark** · 静态与动态环境，考察里程计精度。
- **关键结果 / 消融** · 静态有竞争力，动态明显优于对照。
- **适用条件 / 局限** · 要求多普勒观测及一致的传感模型，摘要未给绝对误差。

**可复用机制** · 如果传感器直接测到运动投影，可用其作为匹配监督，不必只靠难区分的空间相似性。

<a id="paper-148922"></a>

## Self-Supervised Goal-Reaching Results in Multi-Agent Cooperation and Exploration

[官方论文页](https://neurips.cc/virtual/2026/poster/148922) · [作者来源](https://openreview.net/forum?id=uCJyXkPw75)

- **问题 / 瓶颈** · 外部奖励太稀疏时代理还无法形成中间协调技能。
- **核心创新 / 方法** · 以达到目标状态的概率作为自监督学习目标。
- **Baseline** · 相同稀疏奖励下的其他方法和单代理方案。
- **Benchmark** · 多代理强化学习基准及稀疏中间协调。
- **关键结果 / 消融** · 作者报告可找到其他方法从未成功的非平凡协调行为。
- **适用条件 / 局限** · 依赖可指定的目标状态，摘要未给复杂环境成功率。

**可复用机制** · 任务奖励出现前，可先用共享可达状态信号形成协作行为。

<a id="paper-154148"></a>

## Self-Supervised Keyframe Discovery for Horizon-Invariant Behavior Cloning

[官方论文页](https://neurips.cc/virtual/2026/poster/154148) · [作者来源](https://openreview.net/forum?id=FttcVlwwrf)

- **问题 / 瓶颈** · 递归或有限上下文处理长历史容易遗忘、训练不稳。
- **核心创新 / 方法** · 用随机历史观测学习选择目标，再条件化行为克隆。
- **Baseline** · 强记忆增强策略。
- **Benchmark** · 23 个记忆密集操作任务以及训练时长外推。
- **关键结果 / 消融** · 绝对成功率提升 15 至 30 个百分点。
- **适用条件 / 局限** · 依赖关键观测足够覆盖所需记忆，摘要未给动态漂移结果。

**可复用机制** · 让记忆选择学习保留影响未来动作的观测，再把动作策略与历史窗口解耦。

<a id="paper-154892"></a>

## Self-Supervised On-Policy Reinforcement Learning via Contrastive Proximal Policy Optimisation

[官方论文页](https://neurips.cc/virtual/2026/poster/154892) · [作者来源](https://openreview.net/forum?id=A91croHbNN)

- **问题 / 瓶颈** · 已有无奖励对比学习多为离线策略且连续动作居多。
- **核心创新 / 方法** · CPPO 从对比 Q 直接构造策略优势。
- **Baseline** · 以往 CRL 和有奖励 PPO。
- **Benchmark** · 18 项单代理及多代理任务，含离散与连续设置。
- **关键结果 / 消融** · 14/18 优于以往 CRL，12/18 至少匹配有奖励 PPO。
- **适用条件 / 局限** · 需能训练目标可达性比较，摘要未给设置敏感性。

**可复用机制** · 要保留在线更新框架时，先测试以自监督可达性估算替代显式奖励优势。

<a id="paper-155235"></a>

## Self-Supervised Reconstruction Knockoffs for Calibrated Unsupervised Feature Selection

[官方论文页](https://neurips.cc/virtual/2026/poster/155235) · [作者来源](https://openreview.net/forum?id=7DwhldqTP6)

- **问题 / 瓶颈** · 仅能自我重建或边缘方差大不代表对其他特征有用。
- **核心创新 / 方法** · 用对称门控自编码器做遮盖重建并产生带符号 knockoff 统计量。
- **Baseline** · 边缘重要性和自复制对照。
- **Benchmark** · 合成与实际数据上的无标签特征筛选。
- **关键结果 / 消融** · 在交换性和耦合条件下给出控制，近似替代时提供探索性排名。
- **适用条件 / 局限** · 近似 knockoff 时不能沿用精确错误发现保证。

**可复用机制** · 评测无监督特征时比较有意义和匹配空特征的贡献，分开记录探索排名与统计结论。

<a id="paper-153533"></a>

## Self-Trained Verification for Training- and Test-Time Self-Improvement

[官方论文页](https://neurips.cc/virtual/2026/poster/153533) · [作者来源](https://openreview.net/forum?id=KdMT1obOmV)

- **问题 / 瓶颈** · 普通自评可能分数越来越高而正确率不涨。
- **核心创新 / 方法** · 用参考答案帮助模型产生自身原先漏掉的可操作错因，再训练验证器。
- **Baseline** · 继续强化学习及常规自验证修订。
- **Benchmark** · 生成器收敛后的推理，评估 pass@1。
- **关键结果 / 消融** · 摘要报告测试时加入验证器相对增 33%，独立生成器相较继续 RL 的边界增 30%。
- **适用条件 / 局限** · 训练阶段仍需要参考解，摘要未给错误标注成本。

**可复用机制** · 把参考解用于生成训练期错误反馈，部署时保持验证器无需答案。

<a id="paper-153395"></a>

## Self-Tuning Graph Filters via State-Dependent Operator Composition

[官方论文页](https://neurips.cc/virtual/2026/poster/153395) · [作者来源](https://openreview.net/forum?id=LfgU9MTrxj)

- **问题 / 瓶颈** · 固定全图滤波无法兼顾低通、反差和恒等响应。
- **核心创新 / 方法** · Castor 按节点组合不同运算，并可调传播动态。
- **Baseline** · 十四种对照图方法及一阶传播。
- **Benchmark** · 14 个覆盖不同同配性的节点分类基准。
- **关键结果 / 消融** · 每个数据集居前三，平均名次 2.07。
- **适用条件 / 局限** · 摘要未给计算成本或动态图实验。

**可复用机制** · 图中不同位置的邻居作用不同时，优先调局部传播模式而不是只改变全局跳数。

<a id="paper-154149"></a>

## Semantic Consistency of Vision Tokens: A Vision-Centric Perspective on Multimodal Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154149) · [作者来源](https://openreview.net/forum?id=FtLpZ57wIU)

- **问题 / 瓶颈** · 视觉与语言各自优化时可能牺牲词元表达稳定性
- **核心创新 / 方法** · 在 MLLM 诊断下共同使用一致性和语言对齐设计
- **Baseline** · 专用视觉编码器及其他 MLLM
- **Benchmark** · 视觉与文本中心评测组
- **关键结果 / 消融** · 摘要称视觉任务领先且文本任务保持较强
- **适用条件 / 局限** · 具体效益依赖模型和训练设置，摘要未给幅度

**可复用机制** · 适配视觉编码器时用两类任务防止单项指标掩盖退化

<a id="paper-149281"></a>

## SemanticDLM+: Improving Diffusion LLMs through Bias-variance Trade-off in Transition Kernel Design

[官方论文页](https://neurips.cc/virtual/2026/poster/149281) · [作者来源](https://openreview.net/forum?id=rSybF4j1zL)

- **问题 / 瓶颈** · 语义邻域转移易把生成困在单一话题或表达区域
- **核心创新 / 方法** · 加入全局转移并在采样中惩罚语义过度重复
- **Baseline** · SemDLM 和均匀转移
- **Benchmark** · LM1B、OpenWebText；文本质量和多样性
- **关键结果 / 消融** · 训练动态改善且保留竞争力，摘要未列数值
- **适用条件 / 局限** · 全局转移过多可能重现均匀扩散的学习难度

**可复用机制** · 对生成转移分别消融局部可修复性和跨簇探索

<a id="paper-152298"></a>

## Semantic-level Exploration for Multi-Agent Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/152298) · [作者来源](https://openreview.net/forum?id=U6KA6jtstP)

- **问题 / 瓶颈** · 原始观察和动作难积累可重用的访问统计
- **核心创新 / 方法** · 用向量量化形成观察动作原型，按滑窗访问计数给奖励
- **Baseline** · 现有多智能体探索方法
- **Benchmark** · 多智能体基准，具体名称未报告
- **关键结果 / 消融** · 摘要报告更好效果和训练效率
- **适用条件 / 局限** · 原型合并不同任务语义时会低估新颖性

**可复用机制** · 在协作探索中分开调原型分辨率和窗口长度

<a id="paper-148919"></a>

## Semantic Optimal Transport for Sparse Autoencoder Feature Matching and Circuit Compression

[官方论文页](https://neurips.cc/virtual/2026/poster/148919) · [作者来源](https://openreview.net/forum?id=uDcMEMaREB)

- **问题 / 瓶颈** · 字典向量角度无法统一不同层的表征空间
- **核心创新 / 方法** · 用语义描述构造分布并以 Wasserstein 比较
- **Baseline** · 解码向量及基于 LLM 的匹配
- **Benchmark** · 跨层 SAE 特征匹配与电路压缩
- **关键结果 / 消融** · 摘要称匹配更优并可自动聚合为易解释组
- **适用条件 / 局限** · 依赖样本覆盖和分布表示选择

**可复用机制** · 对同功能特征检查激活重缩放是否改变匹配结论

<a id="paper-151306"></a>

## Semantic Routing: Exploring Multi-Layer LLM Feature Weighting for Diffusion Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/151306) · [作者来源](https://openreview.net/forum?id=bRpXPKp716)

- **问题 / 瓶颈** · 固定倒数第二层可能限制细粒度指令条件
- **核心创新 / 方法** · 对文字层做深度路由并对比按时间步路由
- **Baseline** · 倒数第二层及仅时间路由
- **Benchmark** · GenAI-Bench 等指令遵循及视觉保真
- **关键结果 / 消融** · 计数高 9.97，纯时间路由可能损害视觉保真
- **适用条件 / 局限** · 名义时间与有效采样时间错位是解释而非普遍结论

**可复用机制** · 先做去噪骨干深度的条件消融，再引入随时间调度

<a id="paper-150648"></a>

## Semantics-to-Contact: A Stagewise Framework for Robust Contact-Rich Manipulation

[官方论文页](https://neurips.cc/virtual/2026/poster/150648) · [作者来源](https://openreview.net/forum?id=gUco1fy8uO)

- **问题 / 瓶颈** · 单次语义定位难处理实际接触的不确定性
- **核心创新 / 方法** · 把语义聚焦与接触阶段细化分成两个环节
- **Baseline** · 接触操作强基线，摘要未列名称
- **Benchmark** · 六项实机接触任务，视觉与位置变化
- **关键结果 / 消融** · 成功率持续提升且变动下稳定，未报告幅度
- **适用条件 / 局限** · 依赖任务可拆成粗定位和接触阶段

**可复用机制** · 分开验收物体选对和局部插入、抓取等接触动作

<a id="paper-148299"></a>

## SemGeo-Gen: Unsupervised Generation of Approximate Cross-Instance Semantic-Geometric Correspondences

[官方论文页](https://neurips.cc/virtual/2026/poster/148299) · [作者来源](https://openreview.net/forum?id=ytcyAkt461)

- **问题 / 瓶颈** · 人工跨实例稠密对应代价高
- **核心创新 / 方法** · 从三维资产生成近似语义几何对应并作预训练
- **Baseline** · 同类对应模型的真实训练配置
- **Benchmark** · SPair-71k；PCK@0.10
- **关键结果 / 消融** · 最多提升 5 点
- **适用条件 / 局限** · 资产几何覆盖和合成对应偏差限制迁移

**可复用机制** · 稀缺几何标签时同时测合成初始化和真实微调成本

<a id="paper-150512"></a>

## Semiparametric Efficient Tests for Interpretable Distributional Treatment Effects

[官方论文页](https://neurips.cc/virtual/2026/poster/150512) · [作者来源](https://openreview.net/forum?id=hXlL2JXxiW)

- **问题 / 瓶颈** · 全局统计量只报告拒绝。
- **核心创新 / 方法** · 在学习的结果位置估干预核证据。
- **Baseline** · 全局双重稳健核检验。
- **Benchmark** · 半合成医学成像，I 类错误和功效。
- **关键结果 / 消融** · I 类错误接近标称，功效有竞争力。
- **适用条件 / 局限** · 依赖因果识别及位置选择的误差控制。

**可复用机制** · 比较策略时报告哪些状态或结果分布受干预影响。

<a id="paper-150067"></a>

## SemISP: Semantic-Consistent Diffusion for Cross-Camera RAW-to-sRGB Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/150067) · [作者来源](https://openreview.net/forum?id=kzbguNhHJG)

- **问题 / 瓶颈** · RAW 到 sRGB 受传感器域偏移。
- **核心创新 / 方法** · 以场景语义引导扩散。
- **Baseline** · 现有跨相机 ISP。
- **Benchmark** · 两个跨相机基准，保真和感知。
- **关键结果 / 消融** · 两类指标一致改善。
- **适用条件 / 局限** · 语义在低照等退化下须复测。

**可复用机制** · 分开传感器外观变换与场景内容约束。

<a id="paper-149928"></a>

## SemMSA: Latent Semantic-Aided Robust Multimodal Sentiment Analysis with Incomplete Data

[官方论文页](https://neurips.cc/virtual/2026/poster/149928) · [作者来源](https://openreview.net/forum?id=m7bhzxLZxE)

- **问题 / 瓶颈** · 不完整观测损害跨模态一致性。
- **核心创新 / 方法** · 语言模型补情感相关语义，谱对齐各模态。
- **Baseline** · 现有多模态情感模型。
- **Benchmark** · SIMS、MOSI、MOSEI。
- **关键结果 / 消融** · 摘要报告领先，幅度未核。
- **适用条件 / 局限** · 生成语义可能引入偏差。

**可复用机制** · 让先验语义参与所有可见模态的一致性约束。

<a id="paper-139610"></a>

## SenseBench: A Benchmark for Remote Sensing Low-Level Visual Perception and Description in Large Vision-Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139610) · [作者来源](https://openreview.net/forum?id=FZRAoMbDvR)

- **问题 / 瓶颈** · 语言流畅掩盖基础辨别失败。
- **核心创新 / 方法** · 客观退化识别与主观诊断描述并行。
- **Baseline** · 23 个视觉语言模型。
- **Benchmark** · SenseBench 遥感低层评测。
- **关键结果 / 消融** · 多失真会崩溃，感知和描述表现可反转。
- **适用条件 / 局限** · 遥感排序不能自动外推。

**可复用机制** · 视觉评估构造多失真组合并要求独立非语言判断。

<a id="paper-150351"></a>

## Senses Wide Shut: A Representation-Action Gap in Omnimodal LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/150351) · [作者来源](https://openreview.net/forum?id=imx0XlBXqI)

- **问题 / 瓶颈** · 模型可能感到矛盾却仍回答。
- **核心创新 / 方法** · 交叉模态与真假前提，再以探针引导解码。
- **Baseline** · 普通解码与标准前提。
- **Benchmark** · IMAVB，500 个长视频片段。
- **关键结果 / 消融** · 重注冲突信号后拒绝更稳。
- **适用条件 / 局限** · 干预初步，探针不一定可迁移。

**可复用机制** · 感知审计区分未获得证据和获得证据却未改变行动。

<a id="paper-139690"></a>

## SENTINEL: A Multi-Level Formal Framework for Safety Evaluation of Foundation Model-based Embodied Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/139690) · [作者来源](https://openreview.net/forum?id=APzonK9omC)

- **问题 / 瓶颈** · 终局违规难追根。
- **核心创新 / 方法** · 用时序逻辑将要求连接逐层形式验证。
- **Baseline** · 多种基座具身代理。
- **Benchmark** · VirtualHome、Ai2Thor。
- **关键结果 / 消融** · 发现三层不同违规。
- **适用条件 / 局限** · 依赖仿真和规约覆盖。

**可复用机制** · 以同一安全意图验证各中间接口的输出有效性。

<a id="paper-139708"></a>

## SeoulMMOD: A Large-Scale Multimodal Origin-Destination Flow Benchmark

[官方论文页](https://neurips.cc/virtual/2026/poster/139708) · [作者来源](https://openreview.net/forum?id=9Odwt5ID8o)

- **问题 / 瓶颈** · 区尺度性能无法外推到小区。
- **核心创新 / 方法** · 同设置比较多粒度和单多方式预测。
- **Baseline** · 多种时空模型，单方式和多方式。
- **Benchmark** · SeoulMMOD，城内分区 OD 流。
- **关键结果 / 消融** · 多种区级方法不能下探，直接联合无稳定益处。
- **适用条件 / 局限** · 一城市及固定出行覆盖。

**可复用机制** · 把提高空间分辨率和增加模态视作独立压力轴。

<a id="paper-149235"></a>

## Separating Common and Unique Directions for Model Merging

[官方论文页](https://neurips.cc/virtual/2026/poster/149235) · [作者来源](https://openreview.net/forum?id=rvKcBnoRlt)

- **问题 / 瓶颈** · 直接合并稀释有用残差。
- **核心创新 / 方法** · 在共享方向基按离散程度拆分，合公共部分，留独有残差。
- **Baseline** · 四种参数算术合并。
- **Benchmark** · 11 基座、四家族、44 组合。
- **关键结果 / 消融** · 42 组合改善，最高 22.5%。
- **适用条件 / 局限** · 独有残差上线选取需另验。

**可复用机制** · 无数据合并前按方向检查任务冲突和能量占用。

<a id="paper-151189"></a>

## SePO: Self-Evolving Prompt Agent for System Prompt Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/151189) · [作者来源](https://openreview.net/forum?id=cJX1IpMwgF)

- **问题 / 瓶颈** · 固定元提示可能限制检索路径。
- **核心创新 / 方法** · 进化档案同时保任务代理提示和优化代理提示。
- **Baseline** · 只优化任务提示。
- **Benchmark** · 系统提示优化。
- **关键结果 / 消融** · 摘要提出共同演化，幅度待核。
- **适用条件 / 局限** · 必须独立评估以免过拟合反馈。

**可复用机制** · 将元搜索规则视作可追踪参数，对照固定元提示。

<a id="paper-149604"></a>

## SeqDiCO: Sequence-oriented Diffusion for Scale-Generalizable Neural Combinatorial Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/149604) · [作者来源](https://openreview.net/forum?id=osLraeFVlW)

- **问题 / 瓶颈** · 固定输入规模表述可能限制泛化。
- **核心创新 / 方法** · 以序列域生成路由。
- **Baseline** · 代表性扩散和自回归神经求解器。
- **Benchmark** · TSP、CVRP 跨规模。
- **关键结果 / 消融** · 摘要报告持续优于对照。
- **适用条件 / 局限** · 实证是两类组合问题。

**可复用机制** · 候选表示选择能随问题规模自然变化的结构。

<a id="paper-153872"></a>

## Seq-LoRA: Sequential Bayesian Low-Rank Adaptation for Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153872) · [作者来源](https://openreview.net/forum?id=I7N01JSe99)

- **问题 / 瓶颈** · 无权合并忽略各切片曲率。
- **核心创新 / 方法** · 共享 MAP 锚、Kronecker 曲率与高斯伪观测，Kalman 聚合。
- **Baseline** · 独立 LoRA 或普通后验组合。
- **Benchmark** · 顺序切片证据聚合。
- **关键结果 / 消融** · 给出诱导线性高斯的精确推断，摘要无量化结果。
- **适用条件 / 局限** · 依赖局部二次及低维投影近似。

**可复用机制** · 对连续域适配累计可解释曲率证据，显式维护旧域不确定性。

<a id="paper-152093"></a>

## Sequence-to-Sequence Modeling with Camera-Induced Priors for Multi-View Stereo

[官方论文页](https://neurips.cc/virtual/2026/poster/152093) · [作者来源](https://openreview.net/forum?id=VYsvm6wbZr)

- **问题 / 瓶颈** · 普通 token 序列不反映视线约束。
- **核心创新 / 方法** · 在全局 Transformer 注入相机诱导几何。
- **Baseline** · 多视图立体与前馈重建。
- **Benchmark** · 多个公开多视图基准。
- **关键结果 / 消融** · 优于两类方法，幅度未核。
- **适用条件 / 局限** · 有噪相机标定位姿需单测。

**可复用机制** · 明确先验几何与数据驱动匹配的接口。

<a id="paper-150882"></a>

## Sequential Behavioral Watermarking for LLM Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/150882) · [作者来源](https://openreview.net/forum?id=ehO9ULukTj)

- **问题 / 瓶颈** · 绝对轮编号在位置错乱时失效。
- **核心创新 / 方法** · 把来源信号放入转移统计并与随机钥对照。
- **Baseline** · 轮编号行为水印。
- **Benchmark** · 多代理任务、多个模型及受损轨迹。
- **关键结果 / 消融** · 检测稳且任务效用保持，幅度未核。
- **适用条件 / 局限** · 需授权验证与足量观察。

**可复用机制** · 对变长轨迹选不依赖绝对位置的来源统计。

<a id="paper-153160"></a>

## Sequential Probabilistic Uncertainty Estimation for Parallel Multi-Agent Reasoning Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/153160) · [作者来源](https://openreview.net/forum?id=NRg4W8EzfT)

- **问题 / 瓶颈** · 单次投票不足以表达关联不确定性。
- **核心创新 / 方法** · 免训练对潜在信念序贯推断。
- **Baseline** · 对数似然及多代理专用估计器。
- **Benchmark** · 五主干、六基准、两协议。
- **关键结果 / 消融** · 错分识别、弃权和校准均改善。
- **适用条件 / 局限** · 依赖协议及代理相关性。

**可复用机制** · 让置信融合同步反映信息加入和冲突累积。

<a id="paper-148577"></a>

## Serialization Tax in Shared-Latent Exchangeable Decisions

[官方论文页](https://neurips.cc/virtual/2026/poster/148577) · [作者来源](https://openreview.net/forum?id=wnpLcHUs9t)

- **问题 / 瓶颈** · 逐项打分忽略共同潜状态。
- **核心创新 / 方法** · 用不依赖隐藏标签的 TaxScore 标出需共享潜变量的组。
- **Baseline** · Transformer 计数头。
- **Benchmark** · MovieLens 1M 和 10M，NLL 与效用。
- **关键结果 / 消融** · 高分子集 NLL 0.673 到 0.629、0.670 到 0.639；按需路由效用加 0.006 至 0.012。
- **适用条件 / 局限** · 实证为推荐候选，效用需预定义。

**可复用机制** · 动作取决于组内达标计数时测试预测相关性。

<a id="paper-151553"></a>

## SetAD: Semi-Supervised Anomaly Learning in Contextual Sets

[官方论文页](https://neurips.cc/virtual/2026/poster/151553) · [作者来源](https://openreview.net/forum?id=ZlslgF7R5B)

- **问题 / 瓶颈** · 固定点分数不考虑上下文。
- **核心创新 / 方法** · 训练集合评分并平均对多个随机背景的标准化偏差。
- **Baseline** · 现有半监督异常检测。
- **Benchmark** · 十真实数据集。
- **关键结果 / 消融** · 摘要报告显著优于对照。
- **适用条件 / 局限** · 参考背景可能受污染，须确认多样性。

**可复用机制** · 把分数的参考分布与异常模型一并验证。

<a id="paper-150414"></a>

## SetCon: Towards Open-Ended Referring Segmentation via Set-Level Concept Prediction

[官方论文页](https://neurips.cc/virtual/2026/poster/150414) · [作者来源](https://openreview.net/forum?id=iDe99buVDR)

- **问题 / 瓶颈** · 逐个目标输出容易遗漏，也难保证集合互斥。
- **核心创新 / 方法** · 将视觉语言模型生成的自然语言概念用于层次语义分解和联合掩码。
- **Baseline** · 既有逐对象或分割专用 token 方法。
- **Benchmark** · gRefCOCO、MUSE 和七个指代视频基准，指标含 gIoU 和 J&F。
- **关键结果 / 消融** · MUSE 增加 12.1 gIoU，MeViS 增加 10.9 J&F，多目标时优势扩大。
- **适用条件 / 局限** · 依赖概念生成质量和联合解码，摘要未给概念错误影响。

**可复用机制** · 任务目标是完整对象集合时，可先形成可共享的概念计划，再一次生成结构化输出。

<a id="paper-148292"></a>

## Severity-Controlled Prediction Sets for Medication Recommendation

[官方论文页](https://neurips.cc/virtual/2026/poster/148292) · [作者来源](https://openreview.net/forum?id=ywQz91vA0C)

- **问题 / 瓶颈** · 分类覆盖率等权处理不同程度的预测错误。
- **核心创新 / 方法** · 为候选定义层级感知的严重性损失，用共形方式校准限额，无需重训练。
- **Baseline** · 主要控制覆盖率的普通预测集方法。
- **Benchmark** · MIMIC-IV 的用药集合，按 ATC 层级度量偏离严重性。
- **关键结果 / 消融** · 摘要报告达到设定的严重性容差，并将远距错配转为相近或精确匹配。
- **适用条件 / 局限** · 需要可信的严重性定义和代表性校准资料，临床效用未报告。

**可复用机制** · 高代价决策系统应单独校准错误的严重程度，覆盖率只能回答其中一项问题。

<a id="paper-139026"></a>

## SFT-then-RL Outperforms Mixed-Policy Methods for LLM Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/139026) · [作者来源](https://openreview.net/forum?id=pWkCETOQnA)

- **问题 / 瓶颈** · 监督训练的实现错误可人为压低基线。
- **核心创新 / 方法** · 查出微批次遗漏与小批损失权重错误，纠正后重新比较。
- **Baseline** · 已有混合策略方法。
- **Benchmark** · Qwen2.5-Math-7B 和 Llama-3.1-8B 的数学任务及 FLOPs。
- **关键结果 / 消融** · 修复后的分阶段训练相较对照加 3.8 和 22.2 点，50 步 RL 变体仍领先。
- **适用条件 / 局限** · 依赖所测试框架版本和数学任务。

**可复用机制** · 看到复杂训练替代方案大幅领先时，先用不同累积配置重现简单基线的相同更新。

<a id="paper-150405"></a>

## SGD at the Edge of Stability: The Stochastic Sharpness Gap

[官方论文页](https://neurips.cc/virtual/2026/poster/150405) · [作者来源](https://openreview.net/forum?id=iHSnUlPAyy)

- **问题 / 瓶颈** · 全批 GD 的 2/η 锐度门槛不能解释小批稳定点。
- **核心创新 / 方法** · 用随机自稳定分析耦合 SGD 和投影梯度动态，推导平衡锐度差。
- **Baseline** · 全批 GD 与不同批大小的 SGD。
- **Benchmark** · 理论锐度和噪声方向，摘要未列任务。
- **关键结果 / 消融** · 批越小通常越平坦，满批时恢复 GD。
- **适用条件 / 局限** · 定量预测依赖文中动力学假设。

**可复用机制** · 批量对曲率的影响取决于噪声是否投影到尖锐方向，单看总噪声可能不够。

<a id="paper-153017"></a>

## SGD Provably Prioritizes a Shortcut Spurious Feature in the XOR Model

[官方论文页](https://neurips.cc/virtual/2026/poster/153017) · [作者来源](https://openreview.net/forum?id=ObLhQCyrtH)

- **问题 / 瓶颈** · 更强的简单相关性可能先学到，并长期压制复杂信号。
- **核心创新 / 方法** · 分析两层 ReLU 在 XOR 真信号与线性伪相关共存时的 SGD。
- **Baseline** · 去除伪相关的 XOR 学习、不同伪相关强度。
- **Benchmark** · 高维布尔超立方体，考察特征学习时间与样本门槛。
- **关键结果 / 消融** · 理论表明模型先迅速学习捷径，强度足够时在原信号单独可学的样本量仍被压制。
- **适用条件 / 局限** · 定理限于所述模型，常数相关下的延迟恢复属初步实证。

**可复用机制** · 排查捷径时不仅看最终准确率，也看干预伪特征后真信号是否学到。

<a id="paper-153601"></a>

## SGEvolve: Semantic Gradient Guidance for LLM-Driven Evolutionary Search

[官方论文页](https://neurips.cc/virtual/2026/poster/153601) · [作者来源](https://openreview.net/forum?id=KAggF6KCUl)

- **问题 / 瓶颈** · 仅让语言模型随机改写容易丢失已有改进。
- **核心创新 / 方法** · 把代际差值视为零阶证据，让模型推断可能的上升方向并指导生成。
- **Baseline** · 已有开源 LLM 演化框架。
- **Benchmark** · 数学优化、算法设计和工业问题，衡量解质量与搜索效率。
- **关键结果 / 消融** · 作者报告所有任务类型中更优。
- **适用条件 / 局限** · 需要可比较的评估反馈，摘要未给模型调用成本。

**可复用机制** · 让生成代理解释哪些具体变动带来分数改变，再以这些证据指导下一批变动。

<a id="paper-139734"></a>

## SH$^2$: A Mathematician-Curated benchmark for Assessing Research-level Math Capabilities of LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/139734) · [作者来源](https://openreview.net/forum?id=7Okh54hj8U)

- **问题 / 瓶颈** · 竞赛分数可能高估研究式数学迁移。
- **核心创新 / 方法** · 数学专家原创题目，分难度检验，并以人类限时研究核对。
- **Baseline** · 小型到前沿模型、开放权重模型和人类参与者。
- **Benchmark** · 1,141 题和另行的 99 道拒答题，考察数学解题与识别病题。
- **关键结果 / 消融** · 开放模型到研究相邻题的优势减弱，25 名参与者的合并解覆盖 79 题子集的 50.6%。
- **适用条件 / 局限** · 数字来自有限限时子集，不能代表数学研究的整体能力。

**可复用机制** · 基准若要衡量迁移，应拿明显不同的任务构造来检验优化过的解题策略。

<a id="paper-139563"></a>

## ShadowBench: Exposing Lexical Anchoring and the Illusion of Forgetting in Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139563) · [作者来源](https://openreview.net/forum?id=IO7C0IFyvW)

- **问题 / 瓶颈** · 名称缺失可使模型无法调用记忆，形成已经遗忘的假象。
- **核心创新 / 方法** · 对同一实体构造双特征关联并对照有无显式名称。
- **Baseline** · 使用显式名称的评测及不同规模模型。
- **Benchmark** · ShadowBench 的潜在实体关联和遗忘测试。
- **关键结果 / 消融** · 去掉名称后表现下降超过 20%，部分遗忘案例仍可见相关知识被使用。
- **适用条件 / 局限** · 行为测量不能直接证明参数擦除，摘要未给全部实体分布。

**可复用机制** · 验证模型遗忘时应改变访问线索并检测关联知识，不能只看直接询问。

<a id="paper-139054"></a>

## ShadowTransfer: A Geographic Transfer Benchmark for Overhead Shadow Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/139054) · [作者来源](https://openreview.net/forum?id=nsoesUF2ic)

- **问题 / 瓶颈** · 普通同城划分掩盖跨城市失败，整体分数又混合像素偏差。
- **核心创新 / 方法** · 留一城市评估，多探针区分输入外观、特征和掩码置信度。
- **Baseline** · 三类架构、七种适配方法及同城上限。
- **Benchmark** · 三城两分辨率、4500 个人工验证掩码，以 mIoU 与迁移缺口衡量。
- **关键结果 / 消融** · 各适配方法均退化，分析发现阴影内置信度主要下降；插件平均 mIoU 为 70.92。
- **适用条件 / 局限** · 只有三个美国城市的遥感任务，摘要未给跨国家验证。

**可复用机制** · 遇到跨环境分割下降可先按类别分解置信度，并比较输入差异和内部表征差异。

<a id="paper-153569"></a>

## Shaping Useful Noise: Energy Distributions Predict Visual Pretraining Quality

[官方论文页](https://neurips.cc/virtual/2026/poster/153569) · [作者来源](https://openreview.net/forum?id=KQRZdjU6Q1)

- **问题 / 瓶颈** · 只选高似然合成图会漏掉真实数据中的纹理和变化。
- **核心创新 / 方法** · 用能级分布距离 Eld 诊断再重采样或混合合成来源。
- **Baseline** · FID、LPIPS 变化量与特征空间召回。
- **Benchmark** · 多种合成数据，CNN 与 ViT 自监督预训练及下游迁移。
- **关键结果 / 消融** · 摘要报告 Eld 对预训练效果有额外预测力，重采样改善迁移。
- **适用条件 / 局限** · 依赖能量度量和代表性的真实参考，摘要未给跨任务增量。

**可复用机制** · 合成训练数据质量不等同平均逼真度，应匹配参考分布中较少见但重要的区域。

<a id="paper-154044"></a>

## Shared Modular Recurrence in Contextual MDPs for Universal Morphology Control

[官方论文页](https://neurips.cc/virtual/2026/poster/154044) · [作者来源](https://openreview.net/forum?id=Gegwgu6VmY)

- **问题 / 瓶颈** · 运动学、动力学、拓扑变化使专用策略难零样本部署。
- **核心创新 / 方法** · 以 Transformer 式共享模块迭代交换上下文再控制。
- **Baseline** · 既有多机器人控制方法，摘要未列名称。
- **Benchmark** · MuJoCo 四个环境，含训练未见形态属性。
- **关键结果 / 消融** · 作者报告未见运动学、动力学和拓扑的零样本表现明显提高。
- **适用条件 / 局限** · 证据限 MuJoCo，摘要未报告硬件或模块代价。

**可复用机制** · 控制器缺少完整形态标签时，可先让局部模块经多轮交互对齐内部状态。

<a id="paper-155266"></a>

## Shared Truth: Emergent Truth Properties in Large Language Models via Heterogeneous Injection-based Transfer

[官方论文页](https://neurips.cc/virtual/2026/poster/155266) · [作者来源](https://openreview.net/forum?id=6yzSqbvNaN)

- **问题 / 瓶颈** · 注入增益可能来自源探针校准不足
- **核心创新 / 方法** · 对照不同对齐方法、部分与全量替换，并分解增益来源
- **Baseline** · 原生探针、刚性及学习式对齐
- **Benchmark** · 跨模型真值轨迹和校准拟合
- **关键结果 / 消融** · 21 条轨迹均有小的实际可分增益，全部替换失败
- **适用条件 / 局限** · 语义兼容只在部分注入下验证

**可复用机制** · 跨家族迁移诊断前先用留出样本重校准并设全替换负对照

<a id="paper-149663"></a>

## Sharp Capacity Scaling of Spectral Optimizers in Learning Associative Memory

[官方论文页](https://neurips.cc/virtual/2026/poster/149663) · [作者来源](https://openreview.net/forum?id=oNlQTzdbf5)

- **问题 / 瓶颈** · 早期快不直接代表最终最优
- **核心创新 / 方法** · 分析阈值化梯度下的关联记忆容量并做合成验证
- **Baseline** · SGD 和 Muon
- **Benchmark** · 合成联想记忆任务；恢复速率及信息极限
- **关键结果 / 消融** · Muon 初期更快，两者后期收敛速度相近
- **适用条件 / 局限** · 理论依赖关联记忆模型与梯度近似

**可复用机制** · 资源受限情况下分开报告达标时间与较长训练后的差距

<a id="paper-152105"></a>

## Shattered Compositionality: Counterintuitive Learning Dynamics of Transformers for Arithmetic

[官方论文页](https://neurips.cc/virtual/2026/poster/152105) · [作者来源](https://openreview.net/forum?id=VUD0RWdAEz)

- **问题 / 瓶颈** · 能分别完成子技能不保证新组合正确
- **核心创新 / 方法** · 受控改变步骤组合，排查混合错误并与扩容、草稿训练对照
- **Baseline** · 不同规模及有无草稿监督的 Transformer
- **Benchmark** · 合成算术及现代 LLM 的受控分布漂移
- **关键结果 / 消融** · 组合错误持续，扩容和草稿监督未消除
- **适用条件 / 局限** · 证据以算术为主

**可复用机制** · 构造留出技能组合测试，确认模型能按任务结构重组

<a id="paper-153027"></a>

## Shepherd: A Runtime Substrate Empowering Meta-Agents with a Formalized Execution Trace

[官方论文页](https://neurips.cc/virtual/2026/poster/153027) · [作者来源](https://openreview.net/forum?id=OZ3EtBIrwP)

- **问题 / 瓶颈** · 完整重跑代价高且不可控中间状态
- **核心创新 / 方法** · 形式化执行轨迹，使元控制器从选定时点分叉
- **Baseline** · MetaHarness、GEPA，及原工具 Agent RL
- **Benchmark** · CooperBench、TerminalBench-2 及元优化基准
- **关键结果 / 消融** · 元优化最多高 11 点且耗时低 58%，训练示例 34.2% 至 39.4%
- **适用条件 / 局限** · 需隔离和复现工具环境状态

**可复用机制** · 对授权的良性任务用相同前缀做干预因果对照

<a id="paper-150524"></a>

## ShiftRAG: Bypassing the Textual Bottleneck via Decoupled Learning and Continuous Soft Tokens

[官方论文页](https://neurips.cc/virtual/2026/poster/150524) · [作者来源](https://openreview.net/forum?id=hTSuoFjBpl)

- **问题 / 瓶颈** · 将证据全部还原成纯文本可能损失高区分特征
- **核心创新 / 方法** · 把检索结果编为连续软 token，以解耦目标缓解表征秩退化
- **Baseline** · 既有检索增强方法
- **Benchmark** · 检索、问答及通用编码生成评测
- **关键结果 / 消融** · 摘要报告检索及问答均改善并保持基础能力
- **适用条件 / 局限** · 需要取用兼容生成器的隐态，摘要未量化收益

**可复用机制** · 测等预算的连续证据编码和文本证据，并核对可审计性

<a id="paper-139398"></a>

## ShopGym: An Integrated Framework for Realistic Simulation and Scalable Benchmarking of E-Commerce Web Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/139398) · [作者来源](https://openreview.net/forum?id=T78ZNu4RMq)

- **问题 / 瓶颈** · 真实站状态动态变化，合成环境可能失真
- **核心创新 / 方法** · 构建沙盒并比较链接结构及代理任务表现相关性
- **Baseline** · 真实数据店与合成数据店
- **Benchmark** · 六店 224 任务
- **关键结果 / 消融** · 合成店保留若干结构，表现与现实店正相关
- **适用条件 / 局限** · 相关不保证具体站点或个体会复现

**可复用机制** · 用一小组真实站任务作为模拟环境的校准锚

<a id="paper-155271"></a>

## Short-Context Dominance: How Much Local Context Natural Language Actually Needs?

[官方论文页](https://neurips.cc/virtual/2026/poster/155271) · [作者来源](https://openreview.net/forum?id=6waI39kcJc)

- **问题 / 瓶颈** · 训练让模型偏重局部文本，压低依赖远距离信息的词
- **核心创新 / 方法** · 估计距离敏感度并在解码时提升长距离相关词
- **Baseline** · 标准解码及多种非贪心配置
- **Benchmark** · 问答任务和多架构；长短上下文检测
- **关键结果 / 消融** · 检测表现较强并改善问答，未列数值
- **适用条件 / 局限** · 相似度或重要性代理可能误报，应验证不同距离

**可复用机制** · 部署时交叉置换近邻和远距证据来查真正依赖

<a id="paper-153528"></a>

## Should We Pay This Much for Robustness? Efficient Proxy Certificates with Marginal Guarantees

[官方论文页](https://neurips.cc/virtual/2026/poster/153528) · [作者来源](https://openreview.net/forum?id=KfO6qMzPTr)

- **问题 / 瓶颈** · 逐样本强证书开销大。
- **核心创新 / 方法** · 统计控制代理偏离原可靠证书的程度。
- **Baseline** · 原始昂贵认证。
- **Benchmark** · 稳健认证的边际风险及费用。
- **关键结果 / 消融** · 可作为边际证书或回退前置，摘要未报告幅度。
- **适用条件 / 局限** · 边际保证不等价于逐例保证。

**可复用机制** · 按可接受证书粒度安排分层计算。

<a id="paper-149469"></a>

## Show Me What You Don’t Know: Efficient Sampling from Invariant Sets for Model Validation

[官方论文页](https://neurips.cc/virtual/2026/poster/149469) · [作者来源](https://openreview.net/forum?id=pslue396DW)

- **问题 / 瓶颈** · 小扰动测试看不到表示丢失的因素。
- **核心创新 / 方法** · 从近似不变集合采样和可视化。
- **Baseline** · 普通局部解释。
- **Benchmark** · 常见数据和特征提取器。
- **关键结果 / 消融** · 揭示有益及值得警惕的不变性。
- **适用条件 / 局限** · 采样覆盖不代表穷尽全集。

**可复用机制** · 主动寻找表征相同的反例，测丢掉的任务信息。

<a id="paper-151972"></a>

## SHRED: Retain-Set-Free Unlearning via Self-Distillation with Logit Demotion

[官方论文页](https://neurips.cc/virtual/2026/poster/151972) · [作者来源](https://openreview.net/forum?id=WRwsWAq0SG)

- **问题 / 瓶颈** · 忘却序列内不同词承载的记忆量不同。
- **核心创新 / 方法** · 自蒸馏并降高惊讶记忆 token 的 logit。
- **Baseline** · 依赖保留集的遗忘。
- **Benchmark** · 四遗忘基准，遗忘与效用和连续运行。
- **关键结果 / 消融** · 摘要报告更优权衡及多轮效用稳定。
- **适用条件 / 局限** · 高惊讶不一定都是目标记忆，需外部审计。

**可复用机制** · 先按 token 估目标信息再做局部编辑。

<a id="paper-152542"></a>

## SICAF: Time-Varying Focus Bottleneck for Self-Supervised Event-Based Optical Flow with Spiking Neural Network

[官方论文页](https://neurips.cc/virtual/2026/poster/152542) · [作者来源](https://openreview.net/forum?id=SNh0Hj5bcG)

- **问题 / 瓶颈** · 固定压缩会抹掉短暂运动。
- **核心创新 / 方法** · 自监督 SNN 以紧凑瓶颈和时变关注训练。
- **Baseline** · 自监督 SNN 光流。
- **Benchmark** · 多事件集，MVSEC 的 AEE。
- **关键结果 / 消融** · AEE 改善 8.14%。
- **适用条件 / 局限** · 实证依赖事件传感与训练代理。

**可复用机制** · 压缩事件流时以时间变化而非持续平均决定带宽。

<a id="paper-148899"></a>

## SierpinskiCam: Camera-Controlled Video Retaking with Sierpinski Triangle Pattern Cues

[官方论文页](https://neurips.cc/virtual/2026/poster/148899) · [作者来源](https://openreview.net/forum?id=uLAOZJkWvq)

- **问题 / 瓶颈** · 远离源路径时几何引导稀疏。
- **核心创新 / 方法** · Sierpinski 纹理补几何，负 RoPE 区分参考和目标 token。
- **Baseline** · 无纹理的几何指导。
- **Benchmark** · 视频重拍，可控性和保真。
- **关键结果 / 消融** · 摘要报告改善，幅度未核。
- **适用条件 / 局限** · 新暴露区域仍可能无真实外观。

**可复用机制** · 用稳定虚拟锚检验视点变化，外观证据分流传入。

<a id="paper-150328"></a>

## SIEVE: Overcoming Topological Obstruction in Equivariant Self-Supervised Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/150328) · [作者来源](https://openreview.net/forum?id=iw5WbeKHOu)

- **问题 / 瓶颈** · 常量和噪声掩码要求模型猜朝向而坍缩。
- **核心创新 / 方法** · SE(3) 等变编码压到不变几何标量。
- **Baseline** · 坐标、手工几何、常量和噪声掩码。
- **Benchmark** · 点云任务与未见形状类别。
- **关键结果 / 消融** · 避免坍缩，未见类别收益更强。
- **适用条件 / 局限** · 不变输出无法承担需绝对朝向的任务。

**可复用机制** · 让预训练目标的对称性与可观察信息一致。

<a id="paper-150306"></a>

## SIEVES: Selective Prediction Generalizes through Visual Evidence Scoring

[官方论文页](https://neurips.cc/virtual/2026/poster/150306) · [作者来源](https://openreview.net/forum?id=j7Y9kxJJPM)

- **问题 / 瓶颈** · 语言置信无法预测外域证据缺失。
- **核心创新 / 方法** · 以视觉证据分数选择满足风险要求的答题集合。
- **Baseline** · 不做 grounding 的选择预测。
- **Benchmark** · V*、HR-Bench-8k、MME-RealWorld-Lite、VizWiz、AdVQA。
- **关键结果 / 消融** · 外域覆盖最高增至三倍。
- **适用条件 / 局限** · 风险控制随分布和分数校准变化。

**可复用机制** · 选答何时可靠先测证据可见性。

<a id="paper-152143"></a>

## SIGA: Scientific Simulation Coding Agent Adapter- A Geophysics Case Study

[官方论文页](https://neurips.cc/virtual/2026/poster/152143) · [作者来源](https://openreview.net/forum?id=VBiAc0ibjz)

- **问题 / 瓶颈** · 分数波动大且坏案例没有可运行输入。
- **核心创新 / 方法** · 用仿真适配流程监控复合任务的输出结构和成败。
- **Baseline** · 无适配流程及初步人类对照。
- **Benchmark** · GEOS 多物理难任务。
- **关键结果 / 消融** · 跨种子方差约降 40 倍，结构相似加约 7 点。
- **适用条件 / 局限** · 案例域专用，适配组件贡献需另验。

**可复用机制** · 结构化工具评测先将解析失败与有效内容误差分开。

<a id="paper-152746"></a>

## SIGMA: A Sigmoid-Gated Sampler for Test-Time Scaling in Diffusion Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152746) · [作者来源](https://openreview.net/forum?id=QeHRu4aPnt)

- **问题 / 瓶颈** · 同策略难平衡步数、多样和承诺不确定性。
- **核心创新 / 方法** · 联合熵拆 token 与轨迹项，求 sigmoid 门控和位置温度。
- **Baseline** · 既有扩散语言推理扩展。
- **Benchmark** · LLaDA、Dream，数学与代码。
- **关键结果 / 消融** · 改善成本准确 Pareto 前沿。
- **适用条件 / 局限** · 不确定性代理与具体解码器有关。

**可复用机制** · 分配扩散计算时区分选择哪个位置和填什么。

<a id="paper-151764"></a>

## SIGMA: Semantic-Difference Instruction-Grounding Mask Annotator for Text-Driven Image Manipulation Localization

[官方论文页](https://neurips.cc/virtual/2026/poster/151764) · [作者来源](https://openreview.net/forum?id=YE3wLDLd1p)

- **问题 / 瓶颈** · 仅像素差会混入无意变化。
- **核心创新 / 方法** · 基础视觉特征差分，按指令空间先验双向融合。
- **Baseline** · 独立领域标注与现有定位检测器。
- **Benchmark** · 约 110 万训练样本，六检测器五数据集。
- **关键结果 / 消融** · 摘要报告 F1 提升 18.34%。
- **适用条件 / 局限** · 指令执行偏离时可能产生软错标。

**可复用机制** · 重用生成数据时要用意图约束特征差分。

<a id="paper-150835"></a>

## Signal-Adaptive Trust Regions for Gradient-Free Optimization of Recurrent Spiking Neural Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/150835) · [作者来源](https://openreview.net/forum?id=ewv4YcAxRj)

- **问题 / 瓶颈** · 采样种群小时更新方差和步长难稳。
- **核心创新 / 方法** · 对 Bernoulli 连接约束相对 KL，按信号能量归一。
- **Baseline** · PPO-LSTM 等强控制法。
- **Benchmark** · 循环脉冲网高维连续控制。
- **关键结果 / 消融** · 小种群更稳，回报有竞争力。
- **适用条件 / 局限** · 针对分布参数化，能量估计可能噪声大。

**可复用机制** · 无梯度搜索使用可比的信号归一变化量。

<a id="paper-139286"></a>

## SignalBench: Comparing Dense Feedback Methods for Long-Horizon Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/139286) · [作者来源](https://openreview.net/forum?id=ZMC8Gwiail)

- **问题 / 瓶颈** · 最终训练分数混入优化工程差异。
- **核心创新 / 方法** · 无需训练地量反馈与参考中间价值的相关性。
- **Baseline** · 简单提示和 21 种密集方法。
- **Benchmark** · 四环境、六底座，1200 余评估。
- **关键结果 / 消融** · 简单提示持续领先复杂对照。
- **适用条件 / 局限** · 参考价值可能不等于真实最优，相关不等于提升。

**可复用机制** · 先离线检验奖励能否区分有用策略再训练。

<a id="paper-154702"></a>

## Signature Approach for Contextual Bandits with Nonlinear and Path-dependent Rewards

[官方论文页](https://neurips.cc/virtual/2026/poster/154702) · [作者来源](https://openreview.net/forum?id=BfjQPRAfuN)

- **问题 / 瓶颈** · 当前观测向量遗漏历史顺序。
- **核心创新 / 方法** · 签名特征配 disjoint UCB。
- **Baseline** · 线性、核 contextual bandit。
- **Benchmark** · 传感监测、睡眠分类、护理排班。
- **关键结果 / 消融** · 持续优于基线并有次线性遗憾界。
- **适用条件 / 局限** · 依赖有界与非退化条件。

**可复用机制** · 在部分可观测决策中检验历史特征是否胜过静态上下文。

<a id="paper-139252"></a>

## Signature-Kernel Evaluation Metrics for Robust Probabilistic and Tail-Event Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/139252) · [作者来源](https://openreview.net/forum?id=c4U3xzPCvL)

- **问题 / 瓶颈** · 整体 CRPS 可能遮蔽有决策价值的轨迹尾部。
- **核心创新 / 方法** · 截尾签名核折叠主体到一个点，保留尾区分布比较。
- **Baseline** · CRPS、quantile loss。
- **Benchmark** · 时序基础模型及尾事件。
- **关键结果 / 消融** · 分布捕获可排序，任务最优不总一致。
- **适用条件 / 局限** · 尾区需按真实效用指定。

**可复用机制** · 单独评故障或极端条件，并用匹配分布的评分目标。

<a id="paper-149007"></a>

## Sign-Based Optimizers Are Effective Under Heavy-Tailed Noise

[官方论文页](https://neurips.cc/virtual/2026/poster/149007) · [作者来源](https://openreview.net/forum?id=tVpWLU3dKH)

- **问题 / 瓶颈** · 有限方差假设不足以描述大模型训练。
- **核心创新 / 方法** · 以广义重尾噪声解释符号优化器。
- **Baseline** · AdamW、Lion、Muon。
- **Benchmark** · LLM 预训练与噪声理论。
- **关键结果 / 消融** · 摘要报告理论对实证有支持。
- **适用条件 / 局限** · 需先验证当前模型噪声形状。

**可复用机制** · 调整优化器前检查梯度幅值是否主要携带离群噪声。

<a id="paper-154588"></a>

## Signed-Permutation Coordinate Transport for RMSNorm Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/154588) · [作者来源](https://openreview.net/forum?id=CSyPlMeiph)

- **问题 / 瓶颈** · 按带符号相关对齐会错失等价坐标。
- **核心创新 / 方法** · 符号边缘化 Hungarian，比较 LayerNorm 与 RMSNorm 对称。
- **Baseline** · 原始有号相关匹配。
- **Benchmark** · 坐标保真合并与人口分析。
- **关键结果 / 消融** · 有号误差受正号比例上限，边缘化解除。
- **适用条件 / 局限** · 结论依赖所述残差和增益结构。

**可复用机制** · 合并前识别不改变功能的坐标对称性。

<a id="paper-150261"></a>

## Signed Rectified Flow: Negativity Controlled Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/150261) · [作者来源](https://openreview.net/forum?id=jUXmcQ9uAr)

- **问题 / 瓶颈** · 只拟合正样本难压重复或不期望属性。
- **核心创新 / 方法** · 用负测度推广 rectified flow。
- **Baseline** · 标准 rectified flow。
- **Benchmark** · ImageNet 保真多样性与反记忆测试。
- **关键结果 / 消融** · 改善保真与多样性权衡并减少近邻相似。
- **适用条件 / 局限** · 负测度条件及下游生成有效性需检查。

**可复用机制** · 为可检验的反目标单独建建模分量。

<a id="paper-152299"></a>

## SignRot: LLM Quantization with Massive Outlier-Aware Sign-Adjusted Rotation

[官方论文页](https://neurips.cc/virtual/2026/poster/152299) · [作者来源](https://openreview.net/forum?id=U5hyumUfdC)

- **问题 / 瓶颈** · Hadamard 不能消除巨大离群造成的双峰。
- **核心创新 / 方法** · 以一次校准估通道和符号，预合入旋转。
- **Baseline** · 普通 Hadamard 量化。
- **Benchmark** · LLM 校准与量化。
- **关键结果 / 消融** · 分布收为单峰，无额外推理开销。
- **适用条件 / 局限** · 优势只适用于巨大离群结构。

**可复用机制** · 压缩前看旋转后分布形状，不仅看最大值。

<a id="paper-139658"></a>

## SiliconBench: Speed, Memory, and Fidelity for LLM Inference on Apple Silicon

[官方论文页](https://neurips.cc/virtual/2026/poster/139658) · [作者来源](https://openreview.net/forum?id=CYtU8IXAgH)

- **问题 / 瓶颈** · 只比较 token 速度可能看不到运行栈的内存和数值问题。
- **核心创新 / 方法** · 对不同并发度和两类工作负载重复测试，使用同权重 NVIDIA 输出作为保真参照。
- **Baseline** · 十个 Apple Silicon 推理栈和同权重 NVIDIA 参照。
- **Benchmark** · 三个模型版本、短对话与多轮代理，下游加权 F1。
- **关键结果 / 消融** · 双节点一种解码实现快 1.3 倍，TCP 流水线反慢 16% 至 19%。
- **适用条件 / 局限** · 限所测设备、模型和任务，保真仅用一项分类任务。

**可复用机制** · 比较推理引擎时固定模型权重并同时记录任务保真和实际并发资源消耗。

<a id="paper-149726"></a>

## SILSA: Sliding-Window Slice Latents for Topology-Preserving High-Resolution 3D Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/149726) · [作者来源](https://openreview.net/forum?id=noPCtvLWl3)

- **问题 / 瓶颈** · 密集体素昂贵，过度压缩又容易破坏薄结构与连通性。
- **核心创新 / 方法** · 沿三个轴取重叠深度窗口，以切片 VAE 编码后做单阶段流生成。
- **Baseline** · 更密集、多层级和较紧凑的三维分词器。
- **Benchmark** · 三维形状生成，比较 token 数、质量、显存、推理时间。
- **关键结果 / 消融** · 较次紧凑对照少 70% token，训练显存少 40.4%、推理时间少 58.5%。
- **适用条件 / 局限** · 拓扑优势部分来自定性样例，摘要未给更复杂场景结果。

**可复用机制** · 结构跨局部区域延伸时，用重叠切片保留邻域连续性，再在紧凑序列上生成。

<a id="paper-153233"></a>

## SimCT: Recovering Lost Supervision for Cross-Tokenizer On-Policy Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/153233) · [作者来源](https://openreview.net/forum?id=MnkwYa1NsV)

- **问题 / 瓶颈** · 只匹配同名 token 会系统性丢弃异词表位置的教师信号。
- **核心创新 / 方法** · 在共享单 token 之外比较短的多 token 字符串，不换蒸馏损失。
- **Baseline** · 共享词表 OPD 和代表性跨分词器方法。
- **Benchmark** · 在线蒸馏比较及恢复监督消融，摘要未列任务。
- **关键结果 / 消融** · 作者报告一致增益，消融支持恢复丢弃监督。
- **适用条件 / 局限** · 需要两种分词器可对齐的续写，摘要未给构建算力。

**可复用机制** · 词表边界不一致时可对齐短文本片段，监督到两边分别切出的序列。

<a id="paper-154316"></a>

## Simmer: A Scalable Pretraining Recipe for Video-Text Encoders

[官方论文页](https://neurips.cc/virtual/2026/poster/154316) · [作者来源](https://openreview.net/forum?id=EYFTk3vtZR)

- **问题 / 瓶颈** · 单全局向量难吸收不同语域及内容方面的描述。
- **核心创新 / 方法** · 合成多语域字幕，使多个视频向量分别与不同字幕方面对齐。
- **Baseline** · 既有视频文字预训练方案。
- **Benchmark** · 五项视频文本编码任务与三种模型规模。
- **关键结果 / 消融** · 作者报告性能领先并只使用此前方法约 1/2 至 1/60 的视频量。
- **适用条件 / 局限** · 摘要未给字幕合成成本和噪声边界。

**可复用机制** · 增加每条样本配对视角时，让结构有空间保留各方面语义。

<a id="paper-149355"></a>

## Simple Baselines are Competitive with Code Evolution

[官方论文页](https://neurips.cc/virtual/2026/poster/149355) · [作者来源](https://openreview.net/forum?id=qgUDr2vspa)

- **问题 / 瓶颈** · 复杂流程容易把任务设置和有效搜索空间的收益误归给算法。
- **核心创新 / 方法** · 在三个领域对照两种简单流程和主流管线并诊断影响因素。
- **Baseline** · 流行代码演化管线。
- **Benchmark** · 数学界、代理脚手架和机器学习竞赛。
- **关键结果 / 消融** · 简单方法在三域均匹配或超过对照，数学域搜索空间影响大于算法。
- **适用条件 / 局限** · 各领域的主要限制可能不同，摘要未给全量数值。

**可复用机制** · 比较生成式探索方法应使用共享可编辑参数空间和同样的验证代价。

<a id="paper-151368"></a>

## Simple Extensions of Single-Objective Acquisition Functions and Hedge Strategies for Multi-Objective Bayesian Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/151368) · [作者来源](https://openreview.net/forum?id=b5xkf7NyNR)

- **问题 / 瓶颈** · 多目标贝叶斯优化经常需要重新设计采集函数。
- **核心创新 / 方法** · 以超体积转化重用采集分数并推广 hedge 策略。
- **Baseline** · 现有专门设计的多目标贝叶斯优化。
- **Benchmark** · 多目标优化精度与样本效率，摘要未列函数。
- **关键结果 / 消融** · 摘要称有竞争力。
- **适用条件 / 局限** · 需要可计算的超体积，摘要未给大量目标时的代价。

**可复用机制** · 先换采集的比较空间，评估能否原样重用成熟单目标搜索策略。

<a id="paper-149298"></a>

## Simple KNN-Based Outlier Detection Achieves Robust Clustering

[官方论文页](https://neurips.cc/virtual/2026/poster/149298) · [作者来源](https://openreview.net/forum?id=rGWj7JwpMU)

- **问题 / 瓶颈** · 复杂联合鲁棒优化成本高，但简单异常打分的保证不明确。
- **核心创新 / 方法** · 在簇大小条件下证明近邻筛选提供常数因子归约。
- **Baseline** · 更复杂鲁棒聚类方法。
- **Benchmark** · 理论和真实数据，比较聚类代价及耗时。
- **关键结果 / 消融** · 作者报告匹配或超过多种基线。
- **适用条件 / 局限** · 依赖最优簇的规模条件，小的真实簇可能误删。

**可复用机制** · 采用异常点预过滤前，先确认低密度小类并非任务要保留的信号。

<a id="paper-149228"></a>

## Simple Test-Time Refinement for Plot-to-Code Generation via Visual-Code Diagnostics

[官方论文页](https://neurips.cc/virtual/2026/poster/149228) · [作者来源](https://openreview.net/forum?id=rywd4Tm9jn)

- **问题 / 瓶颈** · 整体图像相似度无法告诉生成模型改哪个部分。
- **核心创新 / 方法** · 按粗错误类别训练定位器，根据渲染反馈迭代修订生成代码。
- **Baseline** · 现有推理时扩展方法及多种生成器。
- **Benchmark** · 绘图到代码的质量与诊断表现，摘要未给指标或数据集。
- **关键结果 / 消融** · 作者报告多生成器上一致提高。
- **适用条件 / 局限** · 依赖可重复渲染并有定位训练样本，摘要未给测试时预算。

**可复用机制** · 若输出可转换为目标模态，可把执行差异转成局部可操作反馈而非整段评分。

<a id="paper-139458"></a>

## SimplexUQ: An Evaluation Framework and Benchmark for Conformal Uncertainty on Simplex-Valued Predictions

[官方论文页](https://neurips.cc/virtual/2026/poster/139458) · [作者来源](https://openreview.net/forum?id=OVTO18J0dv)

- **问题 / 瓶颈** · 固定总体阈值的覆盖差异可能部分来自校准而非预测器偏差。
- **核心创新 / 方法** · 冻结基座、分数和不依赖响应的分层，只改变包装器并做受控偏差扫掠。
- **Baseline** · 不同共形包装器。
- **Benchmark** · 六合成及六真实任务，包括类别概率、主题或其他构成比例。
- **关键结果 / 消融** · 去除预测器偏差只部分减少全局阈值的覆盖差异。
- **适用条件 / 局限** · 基准是诊断性比较，摘要未给通用排名。

**可复用机制** · 对概率向量做分层诊断时，冻结预测系统以隔离校准决策自身的影响。

<a id="paper-151357"></a>

## Simple yet Effective Semi-supervised Knowledge Distillation from Vision-Language Models via Dual-Head Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/151357) · [作者来源](https://openreview.net/forum?id=bA0Jhhnk8K)

- **问题 / 瓶颈** · 两个目标梯度冲突可能削弱监督和教师泛化。
- **核心创新 / 方法** · DHO 为监督和蒸馏分别使用预测头，共享表征。
- **Baseline** · 已有半监督训练及视觉语言教师蒸馏。
- **Benchmark** · ImageNet 半监督及多个域外变体。
- **关键结果 / 消融** · 摘要报告超越对照，有些小学生优于教师。
- **适用条件 / 局限** · 摘要未报告共享主干中的残余冲突或单头部署代价。

**可复用机制** · 不同来源的标签可能对应不同决策边界，先分离输出映射再共用特征。

<a id="paper-150401"></a>

## Simplicity is Enough: ReAct Agents for Prompt Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/150401) · [作者来源](https://openreview.net/forum?id=iJGXuLyRh7)

- **问题 / 瓶颈** · 小集上的随机差异会误报复杂优化器的收益。
- **核心创新 / 方法** · 允许代理以工具评估、定位错误并迭代验证提示。
- **Baseline** · 既有提示优化方法。
- **Benchmark** · 多跳问答、数学、事实验证、指令与结构分类。
- **关键结果 / 消融** · 作者报告简单循环有竞争力，并观察小基准会给出不稳定相对差异。
- **适用条件 / 局限** · 效果依赖评价质量，摘要未给总体置信区间。

**可复用机制** · 固定模型采样预算并增加统计覆盖后，再判断专用优化功能是否需要。

<a id="paper-148514"></a>

## Simplified Reversible Residual Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/148514) · [作者来源](https://openreview.net/forum?id=xJJVBYKgl8)

- **问题 / 瓶颈** · 常规反传存储所有激活，旧 RevNet 需要用两个不同变换取代原残差。
- **核心创新 / 方法** · 将 RevNet 两支路之一置为恒等函数，反传时重算激活。
- **Baseline** · 非可逆 ResNet 与 Transformer 及原 RevNet。
- **Benchmark** · ImageNet 分类和 OpenWebText 语言建模。
- **关键结果 / 消融** · 摘要报告性能接近非可逆对照。
- **适用条件 / 局限** · 重算的墙钟和数值精度未报告。

**可复用机制** · 将激活重算引入旧模型时，可试用较小结构改动的可逆残差。

<a id="paper-156008"></a>

## SimReg: Achieving Higher Performance in the Pretraining via Embedding Similarity Regularization

[官方论文页](https://neurips.cc/virtual/2026/poster/156008) · [作者来源](https://openreview.net/forum?id=1BwcSDQLHJ)

- **问题 / 瓶颈** · 传统目标只在输出预测层给匹配信号，未直接约束表征。
- **核心创新 / 方法** · 以同标签拉近、异标签分离的序列内对比损失正则化嵌入。
- **Baseline** · 标准语言模型预训练目标。
- **Benchmark** · 稠密与 MoE 架构，比较收敛和零样本任务。
- **关键结果 / 消融** · 摘要报告快超 30% 收敛，平均零样本增益超 1%。
- **适用条件 / 局限** · 依赖辅助权重和批内标签分布，摘要未给计算开销。

**可复用机制** · 现有 token 标签可额外提供表示层关系信号，无需增加标注任务。

<a id="paper-153145"></a>

## SimSD: Simple Speculative Decoding in Diffusion Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153145) · [作者来源](https://openreview.net/forum?id=NYqEuoKbxZ)

- **问题 / 瓶颈** · 直接借用自回归验证会丢掉并行优势
- **核心创新 / 方法** · 在扩散解码中保留并行验证并兼容缓存和块解码
- **Baseline** · 标准 SDAR 解码及其他加速组合
- **Benchmark** · 四个基准；吞吐及生成质量
- **关键结果 / 消融** · 吞吐最高 7.46 倍，平均质量保持或改善
- **适用条件 / 局限** · 证据来自 SDAR，依赖硬件与块长

**可复用机制** · 先用相同任务质量和实际吞吐衡量推测接受机制

<a id="paper-148668"></a>

## Simulating Human Memory with Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148668) · [作者来源](https://openreview.net/forum?id=w1TBHVhUbg)

- **问题 / 瓶颈** · 仅提示表现像人不能产生相同记忆曲线
- **核心创新 / 方法** · 组合提示与记忆压缩器，用人类参考作验证
- **Baseline** · 只做行为模仿提示
- **Benchmark** · 人类遗忘数据及教育用户模拟
- **关键结果 / 消融** · 压缩能让遗忘更接近人类，下游证据初步
- **适用条件 / 局限** · 只验证有限任务，不能当真实用户替代

**可复用机制** · 用人类记忆基准验收历史截断与压缩策略

<a id="paper-152094"></a>

## Simulation-aided Reinforcement Learning with Control Variates

[官方论文页](https://neurips.cc/virtual/2026/poster/152094) · [作者来源](https://openreview.net/forum?id=VYeUnrk9Ch)

- **问题 / 瓶颈** · 直接混合会把模拟器偏差带入目标
- **核心创新 / 方法** · 以控制变量帮助策略评价，再扩展到 actor-critic 和离线 RL
- **Baseline** · 标准仿真混合
- **Benchmark** · 多项 MuJoCo 控制任务
- **关键结果 / 消融** · 实验优于常规混合，幅度未报告
- **适用条件 / 局限** · 控制变量有效性依赖关联度及估计

**可复用机制** · sim-to-real 时分开量化估计方差与模型偏差

<a id="paper-150165"></a>

## Simulation-Informed Diffusion for Decentralized Multi-robot Motion Planning

[官方论文页](https://neurips.cc/virtual/2026/poster/150165) · [作者来源](https://openreview.net/forum?id=kBwVVfWwux)

- **问题 / 瓶颈** · 固定频率共享过贵而纯独立规划易冲突
- **核心创新 / 方法** · 扩散模型预测邻居轨迹，用安全约束规划自身；拥塞才触发协调
- **Baseline** · 既有分布式控制规划
- **Benchmark** · 多环境，最多 100 机器人和 160 障碍
- **关键结果 / 消融** · 效果与约束满足改进，摘要未列数字
- **适用条件 / 局限** · 依赖可校准邻居预测，预测不准需安全回退

**可复用机制** · 以冲突不确定度决定共享频率，而非均匀广播

<a id="paper-152120"></a>

## SimVLA: Attributing Gains in VLA Models Through Controlled Ablation

[官方论文页](https://neurips.cc/virtual/2026/poster/152120) · [作者来源](https://openreview.net/forum?id=VMuUVQecnd)

- **问题 / 瓶颈** · 额外机器人预训练和网络规模会混淆归因
- **核心创新 / 方法** · 控制同设置下的组件对照，从小视觉语言骨干接轻量头出发
- **Baseline** · 既有 VLA 与同设置组件变体
- **Benchmark** · LIBERO、其他基准和留出实机场景
- **关键结果 / 消融** · LIBERO 平均成功率 98.6%，无需额外大机器人预训练
- **适用条件 / 局限** · 结论限该骨干和训练配置家族

**可复用机制** · 拿新增模块前先建立同预算的简单基线并做单因素验证

<a id="paper-153806"></a>

## Single Shot HDR Recovery via a Video Diffusion Prior

[官方论文页](https://neurips.cc/virtual/2026/poster/153806) · [作者来源](https://openreview.net/forum?id=IZP0ggyeR6)

- **问题 / 瓶颈** · 单帧过曝或失焦区域无法直接恢复
- **核心创新 / 方法** · 用输入条件生成多帧并融合，处理 HDR 后还试全焦恢复
- **Baseline** · 同容量生成方法
- **Benchmark** · HDR 重建及单幅失焦全焦恢复；人评
- **关键结果 / 消融** · 72% 人类偏好，数值重建改善
- **适用条件 / 局限** · 生成帧可能臆造信息，保真须独立评估

**可复用机制** · 将缺失信息恢复变成有一致性约束的多次采样再融合

<a id="paper-153161"></a>

## Sink vs. diagonal patterns as mechanisms for attention switch and oversmoothing prevention

[官方论文页](https://neurips.cc/virtual/2026/poster/153161) · [作者来源](https://openreview.net/forum?id=NPpBWkJvNA)

- **问题 / 瓶颈** · token 间持续混合可能导致过平滑
- **核心创新 / 方法** · 理论比较两种注意力模式的表示代价及关闭混合能力
- **Baseline** · sink、对角注意及无关闭机制
- **Benchmark** · 理论与注意力模式；摘要未报告具体数据
- **关键结果 / 消融** · 解释了 sink 更低表示代价及注意层可退化为逐 token 行为
- **适用条件 / 局限** · 机制依赖具体网络和注意力条件

**可复用机制** · 压缩注意力时保留无需传播层的自路径对照

<a id="paper-151147"></a>

## SIRAS: Sibling-Relative Advantage Shaping for Reinforcement Learning from Verifiable Rewards

[官方论文页](https://neurips.cc/virtual/2026/poster/151147) · [作者来源](https://openreview.net/forum?id=cgLXIEtoqC)

- **问题 / 瓶颈** · 同组归一化在结果全同的组中失去区分
- **核心创新 / 方法** · 用兄弟轨迹相对优势与校准残差，保持组平均 GRPO 优势
- **Baseline** · GRPO 及既有推理 RL
- **Benchmark** · 六推理基准；AIME25 和 26
- **关键结果 / 消融** · 摘要报告 Qwen3-8B AIME25 高 12.2，扩展实验 AIME26 高 23.3
- **适用条件 / 局限** · 依赖可校验任务和兄弟结构估计

**可复用机制** · 检查训练集端部难度是否被组归一化清零

<a id="paper-155992"></a>

## SitCom: Scaling Egocentric Multi-Party Spoken Dialogue for Situated Communication Assistance

[官方论文页](https://neurips.cc/virtual/2026/poster/155992) · [作者来源](https://openreview.net/forum?id=1KuO44r5uN)

- **问题 / 瓶颈** · 离线必要信息已齐，在线要应对尚未结束的互动
- **核心创新 / 方法** · 结合真实与方向仿真语音，分型设计经过人工核验问题
- **Baseline** · 合成数据、真实数据及前沿模型
- **Benchmark** · SitCom-Bench 4300 题，两类时序任务
- **关键结果 / 消融** · 关闭仿真实际差距需混合训练，现场查询仍难
- **适用条件 / 局限** · 场景和扬声人覆盖限制外推

**可复用机制** · 实时助手按首个可答时机评估质量和延迟

<a id="paper-155890"></a>

## Sketch Then Paint: Hierarchical Reinforcement Learning for Diffusion Multi-Modal Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155890) · [作者来源](https://openreview.net/forum?id=24mJNRxaLs)

- **问题 / 瓶颈** · 平坦奖励难保护全图布局。
- **核心创新 / 方法** · 层级 Token GRPO 加结构优先信用。
- **Baseline** · 标准策略优化。
- **Benchmark** · MMaDA、Lumina-DiMOO，GenEval、DPG 及六附加指标。
- **关键结果 / 消融** · 布局、画质和偏好等改善。
- **适用条件 / 局限** · 结构粒度的选择需复测。

**可复用机制** · 将生成布局和局部渲染分开安排奖励。

<a id="paper-150596"></a>

## Skill-Adaptive Noise Scheduling for Diffusion Policies

[官方论文页](https://neurips.cc/virtual/2026/poster/150596) · [作者来源](https://openreview.net/forum?id=gy1X23GoMB)

- **问题 / 瓶颈** · 统一日程低效处理动作复杂度差异。
- **核心创新 / 方法** · 学习技能条件逐动作维度的日程。
- **Baseline** · 现有扩散技能和规划。
- **Benchmark** · 接触密集及灵巧操作，成功率和步数。
- **关键结果 / 消融** · 成功率提高且去噪步数减少。
- **适用条件 / 局限** · 依赖技能识别与控制维耦合。

**可复用机制** · 将生成步数和扰动强度集中到较难的技能自由度。

<a id="paper-149869"></a>

## SkillCIR: Intent-Guided Skill Composition for Training-Free Composed Image Retrieval

[官方论文页](https://neurips.cc/virtual/2026/poster/149869) · [作者来源](https://openreview.net/forum?id=mabFRBx8a2)

- **问题 / 瓶颈** · 理解编辑意图不代表执行检索正确。
- **核心创新 / 方法** · 免训练路由不同约束给检索组件。
- **Baseline** · 训练免组合检索。
- **Benchmark** · 三基准、三 CLIP 底座，recall/mAP 与时延。
- **关键结果 / 消融** · 增加 2.8 至 7.9 点，较最新对照约 23 倍快。
- **适用条件 / 局限** · 依赖意图分解和技能覆盖。

**可复用机制** · 分别核验检索意图解析和条件实际执行。

<a id="paper-149473"></a>

## Skill-Coupled Policy Optimization with Calibrated Group-Wise Advantage Estimation

[官方论文页](https://neurips.cc/virtual/2026/poster/149473) · [作者来源](https://openreview.net/forum?id=pqt0gteKQs)

- **问题 / 瓶颈** · 独立估计方差高，全局收缩忽略题间结构。
- **核心创新 / 方法** · 分组相关性构造结构收缩先验。
- **Baseline** · 逐提示、全局收缩。
- **Benchmark** · 多模型、多任务。
- **关键结果 / 消融** · 训练更稳且表现改善。
- **适用条件 / 局限** · 技能相似性错误可能造成负迁移。

**可复用机制** · 采样不足时只跨相关任务共享基线统计。

<a id="paper-151649"></a>

## SkillForge: Co-Evolving Skills and Agents via Dynamic Skill Lifecycles

[官方论文页](https://neurips.cc/virtual/2026/poster/151649) · [作者来源](https://openreview.net/forum?id=Z3a0qCfhFi)

- **问题 / 瓶颈** · 旧技能堆积会误导已进步的模型。
- **核心创新 / 方法** · 试用、活跃、稳定、退役，先用底座 rollout 淘汰低适合。
- **Baseline** · 强交互技能代理。
- **Benchmark** · 多个交互基准，成功率。
- **关键结果 / 消融** · 最强基线之上相对提升最高 7.8%。
- **适用条件 / 局限** · 需适合度评估和防止技能短期过早淘汰。

**可复用机制** · 技能保留应随策略能力重新评估。

<a id="paper-148850"></a>

## SkillGen: Verified Inference-Time Agent Skill Synthesis

[官方论文页](https://neurips.cc/virtual/2026/poster/148850) · [作者来源](https://openreview.net/forum?id=uhXX7721wa)

- **问题 / 瓶颈** · 技能归纳可能过拟合演示。
- **核心创新 / 方法** · 多代理从基础代理轨迹合成技能。
- **Baseline** · 现有技能生成。
- **Benchmark** · 不同代理、数据集和跨模型迁移。
- **关键结果 / 消融** · 留出任务持续改善，技能可迁移。
- **适用条件 / 局限** · 验收质量依赖任务覆盖。

**可复用机制** · 把技能开发和留出执行检验分开。

<a id="paper-151198"></a>

## Skill-Level Effects in Behavioral Cloning: When Low-Skill Data Improves Performance

[官方论文页](https://neurips.cc/virtual/2026/poster/151198) · [作者来源](https://openreview.net/forum?id=cELixXL3SO)

- **问题 / 瓶颈** · 专家轨迹可能在复制误差后迅速崩落。
- **核心创新 / 方法** · 用动作出错后的回报下降定义 fragility。
- **Baseline** · 高技能与低技能演示。
- **Benchmark** · BC 的演示质量受控对照。
- **关键结果 / 消融** · 某些条件下低技能训练更强，脆弱性可解释。
- **适用条件 / 局限** · 不意味着应普遍用低质量数据。

**可复用机制** · 在人力有限时测示范动作容错性而非只按最高回报选。

<a id="paper-150167"></a>

## SkillMaster: Toward Autonomous Skill Mastery in LLM Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/150167) · [作者来源](https://openreview.net/forum?id=kB6WL1V53t)

- **问题 / 瓶颈** · 固定技能存储不能教代理何时创建或更新。
- **核心创新 / 方法** · 从轨迹评审提出新增、修改或保留，再在相近任务验。
- **Baseline** · 外置固定技能。
- **Benchmark** · 长程代理技能选择和编辑。
- **关键结果 / 消融** · 摘要提出可检验机制，增益未核。
- **适用条件 / 局限** · 探针要隔离一次编辑实际贡献。

**可复用机制** · 对长期记忆更新施测旧技能保持和新技能增益。

<a id="paper-151264"></a>

## SkillOpt: Executive Strategy for Self-Evolving Agent Skills

[官方论文页](https://neurips.cc/virtual/2026/poster/151264) · [作者来源](https://openreview.net/forum?id=bgUar0JP5t)

- **问题 / 瓶颈** · 对训练回放的反思容易过拟合。
- **核心创新 / 方法** · 优化器汇总成败，出结构增删改，以文本更新预算排名。
- **Baseline** · 无技能及现有编辑。
- **Benchmark** · 六直接聊天基准，含具身决策。
- **关键结果 / 消融** · GPT-5.5 对无技能平均增加 21.5 点。
- **适用条件 / 局限** · 有留出开销，定期复验评判漂移。

**可复用机制** · 把文本指南迭代当小步优化，并保留回滚条件。

<a id="paper-155493"></a>

## SkillOrchestra: Learning to Route Agents via Skill Transfer

[官方论文页](https://neurips.cc/virtual/2026/poster/155493) · [作者来源](https://openreview.net/forum?id=5B5fOqwuhG)

- **问题 / 瓶颈** · 端到端 RL 路由训练贵且难解释。
- **核心创新 / 方法** · 以可复用能力描述指导分配。
- **Baseline** · Router-R1、ToolOrchestra。
- **Benchmark** · 十基准。
- **关键结果 / 消融** · 最高改善 27.5%，相对两者学习成本降 700 倍和 300 倍。
- **适用条件 / 局限** · 技能统计及成本比较口径需验证。

**可复用机制** · 按任务需求与成员能力匹配，独立验失败路由。

<a id="paper-151446"></a>

## SkillOS: Learning Skill Curation for Self-Evolving Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/151446) · [作者来源](https://openreview.net/forum?id=ace71RDhko)

- **问题 / 瓶颈** · 即时奖励抓不到长期技能价值。
- **核心创新 / 方法** · 依赖任务成组，早回合写入，晚回合用复合奖励评估。
- **Baseline** · 固定或启发式技能整理。
- **Benchmark** · 依赖式交互任务流。
- **关键结果 / 消融** · 使用更有针对性，技能出现高层归纳。
- **适用条件 / 局限** · 需要可组装依赖序列和留出评估。

**可复用机制** · 使用更新后的真实后续回合成效训练记忆策略。

<a id="paper-156011"></a>

## SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/156011) · [作者来源](https://openreview.net/forum?id=1BZdDrOyJH)

- **问题 / 瓶颈** · 轨迹重复但经验未传承。
- **核心创新 / 方法** · 构建 SkillBank、按需检索并在 RL 中递归更新。
- **Baseline** · 不带递归技能的策略。
- **Benchmark** · ALFWorld、WebShop、七搜索任务。
- **关键结果 / 消融** · 摘要报告实验验证，幅度未核。
- **适用条件 / 局限** · 技能库与策略不断变化，需要防止旧技能劣化。

**可复用机制** · 将行为改进和可检索案例归纳一起优化但分别跟踪。

<a id="paper-139353"></a>

## SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks

[官方论文页](https://neurips.cc/virtual/2026/poster/139353) · [作者来源](https://openreview.net/forum?id=Utmr8dZbrt)

- **问题 / 瓶颈** · 跨任务或不同配置对照掩盖真实技能价值。
- **核心创新 / 方法** · 固定任务和代理，改变技能条件。
- **Baseline** · 无技能对照。
- **Benchmark** · SkillsBench 跨领域代理任务。
- **关键结果 / 消融** · 摘要确立配对比较，幅度未核。
- **适用条件 / 局限** · 同预算与任务定义需保持一致。

**可复用机制** · 隔离技能注入本身的效果并按任务类型分层。

<a id="paper-151567"></a>

## Skill-SD: Skill-Conditioned Self-Distillation for Multi-turn LLM Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/151567) · [作者来源](https://openreview.net/forum?id=ZeThM3k7x0)

- **问题 / 瓶颈** · 把技能永久注入推理上下文有成本。
- **核心创新 / 方法** · 从当前策略轨迹生成动态训练监督。
- **Baseline** · 普通 GRPO、OPD。
- **Benchmark** · AppWorld、Sokoban。
- **关键结果 / 消融** · 对 GRPO 提 14.0% 和 10.9%，对 OPD 提 42.1% 和 40.6%。
- **适用条件 / 局限** · 技能和奖励质量依赖轨迹多样性。

**可复用机制** · 对训练时状态加丰富脚手架，部署可用原接口。

<a id="paper-152785"></a>

## SKIM: Pruning Large Language Model Agents via Selective Knowledge Informed Masking

[官方论文页](https://neurips.cc/virtual/2026/poster/152785) · [作者来源](https://openreview.net/forum?id=QLGlAPvyfZ)

- **问题 / 瓶颈** · 普通平均重要性忽略参数与语法槽。
- **核心创新 / 方法** · 结构化生成中按角色指导剪枝及蒸馏。
- **Baseline** · 常规非结构剪枝。
- **Benchmark** · 工具调用与多步交互，多个稀疏率。
- **关键结果 / 消融** · 精度更高，极高稀疏时优势明显。
- **适用条件 / 局限** · 依赖语法角色可解析。

**可复用机制** · 压缩约束解码模型应按决策价值区分结构和参数 token。

<a id="paper-150768"></a>

## SkipSR: Faster Super-Resolution with Token Skipping

[官方论文页](https://neurips.cc/virtual/2026/poster/150768) · [作者来源](https://openreview.net/forum?id=fVcbQE6MZo)

- **问题 / 瓶颈** · 全帧同成本处理平坦块。
- **核心创新 / 方法** · 只对需细化的区域运行超分。
- **Baseline** · 致密视频超分。
- **Benchmark** · 视频重建质量和效率。
- **关键结果 / 消融** · 摘要报告加速机制，具体幅度待核。
- **适用条件 / 局限** · 低清图可能漏小字和细线。

**可复用机制** · 在稀疏执行前验跳过的误报成本，尤其小目标。

<a id="paper-149332"></a>

## Skip the Hessian, Keep the Rates: Globalized Semismooth Newton with Lazy Hessian Updates

[官方论文页](https://neurips.cc/virtual/2026/poster/149332) · [作者来源](https://openreview.net/forum?id=qs8DDaqFC9)

- **问题 / 瓶颈** · 逐轮高阶评估昂贵，不易扩。
- **核心创新 / 方法** · 重用旧广义 Hessian，定期刷新保全局和超线性。
- **Baseline** · 标准频繁 Hessian 更新。
- **Benchmark** · 矩阵分解和 Lipschitz 约束神经网。
- **关键结果 / 消融** · 给出全局及局部速率，并展示速度收益。
- **适用条件 / 局限** · 依赖半光滑条件和刷新间隔。

**可复用机制** · 二阶训练把曲率刷新预算与方向更新分开。

<a id="paper-151503"></a>

## SkiP: When to Skip and When to Refine for Efficient Robot Manipulation

[官方论文页](https://neurips.cc/virtual/2026/poster/151503) · [作者来源](https://openreview.net/forum?id=aAOUWKZVnm)

- **问题 / 瓶颈** · 等频逐步克隆在冗余段慢。
- **核心创新 / 方法** · 动作频谱自动分段，跳过段学习下一关键段入口动作。
- **Baseline** · 标准 BC 和分层跳过。
- **Benchmark** · 操作任务速度、关键操作成功。
- **关键结果 / 消融** · 同一网络可跳过与细调，摘要幅度待核。
- **适用条件 / 局限** · 频谱代理可能遗漏慢而关键的接触段。

**可复用机制** · 用演示预先区分可跨越的平稳运动与需精控的状态变化。

<a id="paper-139475"></a>

## SlackBench: Benchmarking Agents on Collaborative Projects Grounded in Real Code Repositories

[官方论文页](https://neurips.cc/virtual/2026/poster/139475) · [作者来源](https://openreview.net/forum?id=Nc9EWtWWx4)

- **问题 / 瓶颈** · 单文档问答无法检验证据是否已过时或相互冲突。
- **核心创新 / 方法** · 以真实代码仓库为根基设计会议和沟通证据与代码状态的联合查证任务。
- **Baseline** · 20 个前沿模型和代理框架。
- **Benchmark** · SlackBench 协作开发与研究任务，给出整体分数。
- **关键结果 / 消融** · 最佳系统不足 60%。
- **适用条件 / 局限** · 摘要未给各类误差和更广组织环境表现。

**可复用机制** · 测工作流智能体时，将过时记录与当前状态并置，考察其证据校验能力。

<a id="paper-150237"></a>

## SLDR: Defending Against Malicious Fine-tuning via Selective Layers Recovery and Dynamic Routing

[官方论文页](https://neurips.cc/virtual/2026/poster/150237) · [作者来源](https://openreview.net/forum?id=jjuXPhJpD0)

- **问题 / 瓶颈** · 下游微调可能损害模型安全，所有层统一恢复可能影响任务性能。
- **核心创新 / 方法** · 用带符号敏感性挑选两端的层训练恢复适配器，运行时按风险分类启用。
- **Baseline** · 有风险的微调模型和既有安全恢复方法。
- **Benchmark** · 四架构、五项下游任务和四项风险基准。
- **关键结果 / 消融** · Llama3.1/SST2 平均有害分由 11.54 降至 0.08，同时维持任务准确率。
- **适用条件 / 局限** · 依赖风险路由可靠性，摘要未报告漏判、良性误触发或开销。

**可复用机制** · 局部恢复用于回滚受损行为时，将恢复能力与运行时激活条件分开评估。

<a id="paper-150301"></a>

## Sliced Inner Product Gromov–Wasserstein Distances

[官方论文页](https://neurips.cc/virtual/2026/poster/150301) · [作者来源](https://openreview.net/forum?id=j9kxvPRZEw)

- **问题 / 瓶颈** · 一般 GW 即使一维也未必有闭式求解，切片效率受限。
- **核心创新 / 方法** · 在内积代价下得到一维结果并构造切片 IGW。
- **Baseline** · 标准 GW 和一般切片距离是方法背景。
- **Benchmark** · 数值理论验证、异质文本聚类与语言模型表示比较。
- **关键结果 / 消融** · 摘要报告旋转不变性并展示两类应用。
- **适用条件 / 局限** · 依赖内积代价，摘要未列运算规模和误差。

**可复用机制** · 跨编码器比表示时，可先确定要忽略哪些坐标变换，再选择结构距离。

<a id="paper-153403"></a>

## SLIDERS: Systematic Reviews via Automated Evidence Synthesis and Reconciliation

[官方论文页](https://neurips.cc/virtual/2026/poster/153403) · [作者来源](https://openreview.net/forum?id=LbmCSLInX7)

- **问题 / 瓶颈** · 仅依赖关键词或向量召回难满足跨文档覆盖。
- **核心创新 / 方法** · 按问题抽取字段和全文片段，由证据核对代理聚合多文献数据。
- **Baseline** · 既有检索与综述代理。
- **Benchmark** · 三任务、约 600 万至 1100 万 token 文献集及两类追问。
- **关键结果 / 消融** · 主要任务准确率接近 90%，两类追问为 77.9% 和 58.3%。
- **适用条件 / 局限** · 摘要未给医学综述审查一致性及成本。

**可复用机制** · 需要核查可追溯性时，汇总表中的字段应能回到供独立验证的原文片段。

<a id="paper-155791"></a>

## SLiDE: Structured Linear Dynamics for Forecasting with Exogenous Inputs

[官方论文页](https://neurips.cc/virtual/2026/poster/155791) · [作者来源](https://openreview.net/forum?id=2rJCMiMakf)

- **问题 / 瓶颈** · 编码器与 rollout 不一致会增加自由度并产生虚假相关。
- **核心创新 / 方法** · 在潜空间用共同线性递归编码历史，以及用未来外生输入驱动预测。
- **Baseline** · 面向外生时间序列的既有预测方案。
- **Benchmark** · 真实和合成的外生预测，含未见外生驱动的系统。
- **关键结果 / 消融** · 摘要报告消融支持历史编码与线性 rollout，未见外生条件仍有收益。
- **适用条件 / 局限** · 依赖可用的未来外生变量和可学习的近似线性空间。

**可复用机制** · 预测模型面对驱动分布变化时，单独建模持久动力学与外部输入。

<a id="paper-153520"></a>

## SliMOO: Interpretable Multi-Objective Evolutionary Search for LLM Depth Pruning

[官方论文页](https://neurips.cc/virtual/2026/poster/153520) · [作者来源](https://openreview.net/forum?id=KkPVejhpML)

- **问题 / 瓶颈** · 一个领域不敏感的层可能是另一个领域所需。
- **核心创新 / 方法** · 以逐层移除评估构建任务层地图，再做多目标进化搜索剪枝集合。
- **Baseline** · 规则、贪心与标量优化剪枝。
- **Benchmark** · Llama-3.1 和 Qwen3，比较跨数学与编程的多任务保留。
- **关键结果 / 消融** · Llama-3.1-70B 在 25% 稀疏下数学从 24.33% 到 34.40%，编程从 35.03% 到 39.14%。
- **适用条件 / 局限** · 逐层分数不能充分描述层联合作用，摘要未给总体搜索预算。

**可复用机制** · 多用途模型压缩时让各任务参与可解释的多目标取舍。

<a id="paper-138903"></a>

## SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks

[官方论文页](https://neurips.cc/virtual/2026/poster/138903) · [作者来源](https://openreview.net/forum?id=xxD8UZjGl8)

- **问题 / 瓶颈** · 单次任务成功掩盖架构在迭代中逐步恶化。
- **核心创新 / 方法** · 用不断扩展的需求和分阶段检查，比较有无质量指引。
- **Baseline** · 15 个代码代理及显式质量指引。
- **Benchmark** · 36 个问题、196 个检查点，测正确性、复杂度和冗长。
- **关键结果 / 消融** · 无代理完整解决问题，最好通过率 14.8%；质量指引改善起点但未改变退化速率。
- **适用条件 / 局限** · 限于测试仓库周期与结构度量。

**可复用机制** · 评估长期工程质量应测退化斜率，避免初版更整洁遮盖后续累积。

<a id="paper-154636"></a>

## SLOPE: Optimistic Potential Landscape Shaping for Model-based Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/154636) · [作者来源](https://openreview.net/forum?id=C7a3d9iUcu)

- **问题 / 瓶颈** · 稀疏标量奖励难提供计划更新方向。
- **核心创新 / 方法** · 用分布回归估计乐观上界，放大罕见成功产生的潜势。
- **Baseline** · 先进奖励建模或模型式强化学习基线。
- **Benchmark** · 五基准与真机、30 多项任务，含稀疏和稠密奖励。
- **关键结果 / 消融** · 摘要报告在三种奖励稀疏度下均领先。
- **适用条件 / 局限** · 摘要未给乐观程度过高时的结果或逐任务指标。

**可复用机制** · 规划时给成功证据稀少但可能有用的区域足够探索权重。

<a id="paper-154236"></a>

## Slower Generalization, Faster Memorization: A Sweet Spot in Algorithmic Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/154236) · [作者来源](https://openreview.net/forum?id=FDIVnGvUBM)

- **问题 / 瓶颈** · 泛化是否可达和泛化多快可能有不同的数据量最优点。
- **核心创新 / 方法** · 在动态规划输出任务改变数据规模，比较训练和验证精确匹配。
- **Baseline** · 乘法任务作对照。
- **Benchmark** · Needleman–Wunsch 矩阵生成，小型 Transformer，训练及验证匹配。
- **关键结果 / 消融** · 中等数据最早达到高验证精度，更大数据仍泛化但需要更多更新；乘法未同样减慢。
- **适用条件 / 局限** · 仅是受控任务，摘要未给更大模型外推。

**可复用机制** · 数据消融同时报告固定更新表现和达到阈值时间，避免把两类标度结论混为一谈。

<a id="paper-139283"></a>

## SLVMBench: Skill Learning from Video Memory

[官方论文页](https://neurips.cc/virtual/2026/poster/139283) · [作者来源](https://openreview.net/forum?id=ZRdrfTmC6h)

- **问题 / 瓶颈** · 答对视频内容不足以说明学到可用程序。
- **核心创新 / 方法** · 把教程嵌入两到三小时视频流，并在持续视频中提出需应用技能的问题。
- **Baseline** · 已有视频语言模型。
- **Benchmark** · SLVMBench，分别测试记忆提取和实时程序应用。
- **关键结果 / 消融** · 摘要报告隐藏在长历史中时应用效果明显退化。
- **适用条件 / 局限** · 限于所测教程和问答，摘要未报告动作执行结果。

**可复用机制** · 技能理解评测把找到示范和把示范迁移到新任务分成两步。

<a id="paper-154074"></a>

## SLVR: Structured Latent Visual Reasoning via Human-like Reasoning Flows

[官方论文页](https://neurips.cc/virtual/2026/poster/154074) · [作者来源](https://openreview.net/forum?id=GOIf9kmCHv)

- **问题 / 瓶颈** · 显式逐词推理慢，单一潜状态无法独立监督中间职责。
- **核心创新 / 方法** · 按规划、定位和证据选择组织潜在阶段，配专门监督。
- **Baseline** · 显式文本推理与通用潜推理。
- **Benchmark** · MMVP、BLINK Relation、V*、MathVista 和 ChartQA。
- **关键结果 / 消融** · 摘要报告 BLINK Relation 提高 14.2，并改善多项视觉推理。
- **适用条件 / 局限** · 需要阶段监督质量，摘要未给完整时延和泛化边界。

**可复用机制** · 在隐式推理中按职责指定中间表示及其训练信号，有助于摆脱长文本推理轨迹。

<a id="paper-155994"></a>

## Small Model Portfolios for Many Deployment Profiles: Submodular Coverage under Bundled Constraints

[官方论文页](https://neurips.cc/virtual/2026/poster/155994) · [作者来源](https://openreview.net/forum?id=1JWwZf78Km)

- **问题 / 瓶颈** · 模型的质量、内存与速度若分属不同候选，仍可能没有任何一个可部署。
- **核心创新 / 方法** · 在已测模型档案上做加权最大覆盖，以贪心挑选模型。
- **Baseline** · 标量及 Pareto 选择。
- **Benchmark** · 多类部署需求与预算，考察覆盖率及重测噪声。
- **关键结果 / 消融** · 贪心有 1−1/e 保证，经验增益集中于难覆盖档且 K=3 最稳定。
- **适用条件 / 局限** · 需要可靠的预测量档案，未覆盖的目标无法由选择补足。

**可复用机制** · 部署候选筛选应以一套可同时满足的需求为覆盖单位。

<a id="paper-150817"></a>

## Smart Picks in the Dark: Towards Efficient RLVR for Reasoning via Tracing Metacognitive Pivots

[官方论文页](https://neurips.cc/virtual/2026/poster/150817) · [作者来源](https://openreview.net/forum?id=f6NxXBLsMW)

- **问题 / 瓶颈** · 均匀标签覆盖消耗预算且许多样本不需要人工
- **核心创新 / 方法** · 用注意力变化定位推理转折并做三路数据分流
- **Baseline** · 充分监督推理模型
- **Benchmark** · 训练标注率、收敛和推理表现
- **关键结果 / 消融** · 仅用 29.3% 标注样本仍超过充分监督，收敛快 2.75 倍
- **适用条件 / 局限** · 内部转折只是代理，需核对其跨骨干稳定性

**可复用机制** · 当标注受限时用学习不确定性作分流对照

<a id="paper-149874"></a>

## SMART: Scalable Multi-Agent Role-conditioned  Teaming via LLM-free Tree Search

[官方论文页](https://neurips.cc/virtual/2026/poster/149874) · [作者来源](https://openreview.net/forum?id=mYzIBNy0LN)

- **问题 / 瓶颈** · 让 LLM 给每个协作编组评分成本高
- **核心创新 / 方法** · 先确定拓扑与候选集，再用轻量元数据 rollout 指派
- **Baseline** · 既有多智能体组织方式，摘要未列清单
- **Benchmark** · GPT-4o-mini 在 GSM8K、MATH、HumanEval、MBPP
- **关键结果 / 消融** · 摘要列 93.64%、61.73%、93.89%、87.68%
- **适用条件 / 局限** · 元数据不足时难代表当前任务相容性

**可复用机制** · 预算受限时分开测角色搜索和实际工作器的生成费用

<a id="paper-139761"></a>

## SMMBench: A Benchmark for Source-Distributed Multimodal Agent Memory

[官方论文页](https://neurips.cc/virtual/2026/poster/139761) · [作者来源](https://openreview.net/forum?id=6FddqZ3fYX)

- **问题 / 瓶颈** · 单文档检索可能高估整合多处记录的能力
- **核心创新 / 方法** · 在多个来源上分设记忆检索、偏好和动作推断任务
- **Baseline** · 记忆型和检索型方法
- **Benchmark** · 1877 样本、264 来源
- **关键结果 / 消融** · 摘要称当前系统仍难，未列对照幅度
- **适用条件 / 局限** · 题目对跨源依赖的强度需进一步审计

**可复用机制** · 对照片、对话与历史事件跨源的必要证据覆盖分开评分

<a id="paper-153896"></a>

## SMoA: Spectrum Modulation Adapter for Parameter-Efficient Fine-Tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/153896) · [作者来源](https://openreview.net/forum?id=HtLt3XukFH)

- **问题 / 瓶颈** · 常规单低秩分支可能覆盖谱方向有限
- **核心创新 / 方法** · 拆成对齐谱块，每块加 Hadamard 调制低秩分支
- **Baseline** · LoRA 和其他 LoRA 变体
- **Benchmark** · 多个任务的低预算适配，任务名未报告
- **关键结果 / 消融** · 摘要报告平均优势，未给数字
- **适用条件 / 局限** · 额外块划分与变换成本要纳入预算

**可复用机制** · 相同参数数下比较谱覆盖广度与下游性能

<a id="paper-148194"></a>

## Smooth Partial Lotteries for Stable Randomized Selection

[官方论文页](https://neurips.cc/virtual/2026/poster/148194) · [作者来源](https://openreview.net/forum?id=zciTC98AYH)

- **问题 / 瓶颈** · 硬排序或现有部分抽签高度敏感
- **核心创新 / 方法** · 用平滑随机选择，并比较稳定性与遗憾折衷
- **Baseline** · 现有部分抽签、公平和隐私稳定性定义
- **Benchmark** · ICLR 2025、NeurIPS 2024、瑞士 NSF 评审分
- **关键结果 / 消融** · 理论和实际数据均发现原规则可被单分改动大幅改变
- **适用条件 / 局限** · 适用于有预算和评分的选择，价值函数需贴合用途

**可复用机制** · 给主动采样标注或选择预算加入分数扰动回归

<a id="paper-152423"></a>

## Smooth Piecewise Cutting for Neural Operator to Handle Discontinuities and Sharp Transitions

[官方论文页](https://neurips.cc/virtual/2026/poster/152423) · [作者来源](https://openreview.net/forum?id=TDrTy1h1EQ)

- **问题 / 瓶颈** · 单一全域平滑表示模糊锋面
- **核心创新 / 方法** · 学习分区，对每片用神经算子生成较平滑分量
- **Baseline** · DeepONet 及已有神经算子
- **Benchmark** · 多个有不连续与跃变的 PDE；低分辨率训练
- **关键结果 / 消融** · 摘要称更准且参数更少
- **适用条件 / 局限** · 分区误差可能移动真实锋面，迁移尚需核对

**可复用机制** · 有接触边界的场预测可对照分片和单域表示

<a id="paper-148985"></a>

## SO(3)-Equivariant Learning on CAD Boundary Representations

[官方论文页](https://neurips.cc/virtual/2026/poster/148985) · [作者来源](https://openreview.net/forum?id=tf8Fu4Bubx)

- **问题 / 瓶颈** · 仅用不变量会丢失面之间的相对方向
- **核心创新 / 方法** · 在边界表示图上传递旋转等变向量信息
- **Baseline** · 既有 B-rep 法及等变点云法
- **Benchmark** · 五种 CAD 形状识别和表面分割基准
- **关键结果 / 消融** · 摘要报告全面领先且样本效率更好
- **适用条件 / 局限** · 依赖 B-rep 结构和拓扑质量

**可复用机制** · 机器人形状分析保留方向关系，再按任务消除全局姿态

<a id="paper-151769"></a>

## SOAP-Bubbles: Effective and Scalable Variational Learning with Structured Covariances

[官方论文页](https://neurips.cc/virtual/2026/poster/151769) · [作者来源](https://openreview.net/forum?id=YBJkwSJVbo)

- **问题 / 瓶颈** · 对角后验难表示模型参数耦合
- **核心创新 / 方法** · 用结构协方差近似并从学习到的后验采样集成
- **Baseline** · IVON
- **Benchmark** · 语言预训练验证损失及后验集成测试损失
- **关键结果 / 消融** · 摘要称等开销下降低损失，且集成优于 IVON 后验
- **适用条件 / 局限** · 全高斯最优只在指定条件成立

**可复用机制** · 评估不确定性时同时测单模型验证和后验集成收益

<a id="paper-151153"></a>

## SOAR: Regression-based LiDAR Relocalization for UAVs

[官方论文页](https://neurips.cc/virtual/2026/poster/151153) · [作者来源](https://openreview.net/forum?id=cdxdVJjpkZ)

- **问题 / 瓶颈** · 视点变化下几何匹配不稳。
- **核心创新 / 方法** · 滑窗注意力维持局部性并使用局部不变相对编码。
- **Baseline** · 现有 LiDAR 重定位。
- **Benchmark** · 有同步点云、6DoF 及多次遍历的 UAVLoc。
- **关键结果 / 消融** · 定位成功率提高 40%，均误差降逾 10 m。
- **适用条件 / 局限** · 实证涵盖数据集中的视角，跨平台须重测。

**可复用机制** · 重定位可将局部匹配不变性与全局位姿解码分开。

<a id="paper-148421"></a>

## SOAR: Semantic Organ-Aware Pretraining for 3D CT Image Understanding

[官方论文页](https://neurips.cc/virtual/2026/poster/148421) · [作者来源](https://openreview.net/forum?id=xwakWJUI55)

- **问题 / 瓶颈** · 全局配对只覆盖少量诊断发现。
- **核心创新 / 方法** · 训练语义器官感知 CT 表征并接现有 LLM。
- **Baseline** · 基于报告的全局对齐。
- **Benchmark** · 五项公共及内部基准，VQA 准确和 AUC。
- **关键结果 / 消融** · VQA 平均加 3.53%，筛查和异常 AUC 加 4.25 点。
- **适用条件 / 局限** · 需可靠局部器官信号，其他传感器待验。

**可复用机制** · 发现文本只描述少数区域时分开监督全局和未描述局部。

<a id="paper-152622"></a>

## Sobolev Regularized MMD Gradient Flow

[官方论文页](https://neurips.cc/virtual/2026/poster/152622) · [作者来源](https://openreview.net/forum?id=RiNRfwPQ7Z)

- **问题 / 瓶颈** · 直接 MMD 梯度流有非凸障碍。
- **核心创新 / 方法** · 对见证函数加 Sobolev 正则；用 Stein 核适配采样。
- **Baseline** · 只适合采样或生成的一般梯度流。
- **Benchmark** · 采样及生成的连续与离散收敛。
- **关键结果 / 消融** · 得到 MMD 全局收敛，实验有支持。
- **适用条件 / 局限** · 依赖核和正则条件。

**可复用机制** · 在分布匹配任务中同时测试差异量和其引导梯度。

<a id="paper-152951"></a>

## SoccerNarrate: Event-Grounded Streaming Soccer Commentary with Macro-Window Preference Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/152951) · [作者来源](https://openreview.net/forum?id=P9oiEDJVAl)

- **问题 / 瓶颈** · 逐词评估忽略实时事件覆盖。
- **核心创新 / 方法** · 宏窗口偏好对齐，以带时间约束的事件蕴含评估。
- **Baseline** · 强离线与流式方法。
- **Benchmark** · 完整足球比赛，事件精度和覆盖。
- **关键结果 / 消融** · 两轴改善，摘要未核幅度。
- **适用条件 / 局限** · 事件定义及转述延迟依场景。

**可复用机制** · 实时视频代理按事件窗口而非单句时间切片给予反馈。

<a id="paper-148453"></a>

## Social Choice Foundations for Simulation-Augmented Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/148453) · [作者来源](https://openreview.net/forum?id=xjWS1jZydQ)

- **问题 / 瓶颈** · 缩小群体代理会损害比例代表性。
- **核心创新 / 方法** · 以比例聚类分两层动态选代表。
- **Baseline** · 全部个体和全部模拟查询。
- **Benchmark** · 比例代表性理论，m 个体、n 模拟、k 查询。
- **关键结果 / 消融** · n 与 k 可远小于上一层而近似保代表性。
- **适用条件 / 局限** · 依赖比例和近似条件，真实行为可信度仍须测。

**可复用机制** · 角色过多时先保群体覆盖，再按任务上取样。

<a id="paper-155006"></a>

## SocialDirector: Training-Free Social Interaction Control for Multi-Person Video Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/155006) · [作者来源](https://openreview.net/forum?id=9HlJW88mEe)

- **问题 / 瓶颈** · 整体视频文本引导可将动作分错人。
- **核心创新 / 方法** · 免训练社会交互控制并自动分项评估。
- **Baseline** · 原视频生成模型及真实视频上界。
- **Benchmark** · 多模型互动生成和现有数据增强标注。
- **关键结果 / 消融** · 交互保真改善且接近真实上界。
- **适用条件 / 局限** · 自动 VLM 裁判可能漏掉细小行为。

**可复用机制** · 多人指令将关系三元组作约束与评估单位。

<a id="paper-148789"></a>

## Social Interaction Breaks Replicate Independence in Controlled-Clone LLM Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/148789) · [作者来源](https://openreview.net/forum?id=v48Q9Nsxcw)

- **问题 / 瓶颈** · 复制同底座不保证交互后独立。
- **核心创新 / 方法** · 控制克隆并测社会认知转移。
- **Baseline** · 不交互克隆。
- **Benchmark** · 主任务外十个设置。
- **关键结果 / 消融** · 五格在 0.05 下显著为正，未见显著反转。
- **适用条件 / 局限** · 统计功效和多比条件需核。

**可复用机制** · 聚合模拟结果时以独立交互组为重复单位。

<a id="paper-150828"></a>

## SOC-ICNN: From Polyhedral to Conic Geometry for Learning Convex Surrogate Functions

[官方论文页](https://neurips.cc/virtual/2026/poster/150828) · [作者来源](https://openreview.net/forum?id=f1AOGYk9aS)

- **问题 / 瓶颈** · ReLU ICNN 主要给多面体结构。
- **核心创新 / 方法** · 加入 PSD 曲率和欧氏范数锥表示。
- **Baseline** · ReLU 输入凸网和 LP 结构。
- **Benchmark** · 凸函数逼近与下游决策。
- **关键结果 / 消融** · 表示严格扩展且前向渐近阶不变，逼近改善。
- **适用条件 / 局限** · SOCP 运行成本和规模需实地比较。

**可复用机制** · 训练代理要保凸时可利用可求解的锥结构表达曲率。

<a id="paper-150571"></a>

## SODA: Selective Optimization with Deferred BN Alignment for Efficient Dataset Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/150571) · [作者来源](https://openreview.net/forum?id=hAi08GriqP)

- **问题 / 瓶颈** · 每次全层对齐计算冗余。
- **核心创新 / 方法** · 分阶段选择和延迟 BN 统计约束。
- **Baseline** · 全层 BN 对齐。
- **Benchmark** · CIFAR-100、Tiny 数据等。
- **关键结果 / 消融** · 分析指出可同时降成本和提泛化，确数待核。
- **适用条件 / 局限** · 依赖带 BN 的蒸馏管线。

**可复用机制** · 蒸馏监督应先定位边际收益高的层与训练阶段。

<a id="paper-152288"></a>

## Soft Contamination Means Benchmarks Test Shallow Generalization

[官方论文页](https://neurips.cc/virtual/2026/poster/152288) · [作者来源](https://openreview.net/forum?id=UBmysDOEQQ)

- **问题 / 瓶颈** · 逐字去重仍会高估泛化。
- **核心创新 / 方法** · 嵌入检索 Olmo 3 语料，受控加入副本并比较划分和邻近基准。
- **Baseline** · 同榜真留出及相关基准。
- **Benchmark** · CodeForces、MBPP 等。
- **关键结果 / 消融** · 近副本比例 76% 与 100%，同榜收益明显而通常不跨榜。
- **适用条件 / 局限** · 受语义判定及污染训练制度影响。

**可复用机制** · 用任务家族留出而非只在同题库真实留出。

<a id="paper-151016"></a>

## Soft Forward-Backward Representations for Zero-shot Reinforcement Learning with General Utilities

[官方论文页](https://neurips.cc/virtual/2026/poster/151016) · [作者来源](https://openreview.net/forum?id=da88i4IpCj)

- **问题 / 瓶颈** · 单个确定零样本策略不足表示多解。
- **核心创新 / 方法** · 最大熵 FB 从离线数据学随机策略族。
- **Baseline** · 经典 FB。
- **Benchmark** · 教学及高维通用效用任务。
- **关键结果 / 消融** · 保有原 FB 特性并支持更广效用。
- **适用条件 / 局限** · 需要离线覆盖和可表示效用。

**可复用机制** · 任务未定时保留可变策略分布，不提前压成单个最优动作。

<a id="paper-155147"></a>

## Soft geometric inductive bias for object centric dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/155147) · [作者来源](https://openreview.net/forum?id=7yVfU7Zd4x)

- **问题 / 瓶颈** · 硬等变可能不符真实交互。
- **核心创新 / 方法** · 将几何结构纳入对象中心动力学而不强制全部对称。
- **Baseline** · 常规世界模型和严格几何约束。
- **Benchmark** · 2D 刚体、3D 带电粒子和真实驾驶轨迹。
- **关键结果 / 消融** · 摘要报告样本效率，数字未核。
- **适用条件 / 局限** · 先验必须与对象关系匹配。

**可复用机制** · 将近似对称当可学习偏置而非硬约束。

<a id="paper-150736"></a>

## Soft-Radial Projection for Constrained End-to-End Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/150736) · [作者来源](https://openreview.net/forum?id=flhcgCEqDM)

- **问题 / 瓶颈** · 硬投影到同一面导致雅可比降秩。
- **核心创新 / 方法** · 从严格可行锚沿射线缩放到相对内域。
- **Baseline** · 硬径向、正交投影。
- **Benchmark** · 凸可行集及梯度饱和分析。
- **关键结果 / 消融** · 映射一对一且雅可比满秩。
- **适用条件 / 局限** · 需要可行锚，不能直接取边界最优点。

**可复用机制** · 按可行性和反传秩共同选约束层。

<a id="paper-149550"></a>

## Soft Token Alignment for Cross-Lingual Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/149550) · [作者来源](https://openreview.net/forum?id=pJ0iIOHK6H)

- **问题 / 瓶颈** · 低资源语言难从英文推理迁移。
- **核心创新 / 方法** · SFT 增英文枢纽软表示对齐。
- **Baseline** · 底座及标准 SFT。
- **Benchmark** · 四项多语推理基准。
- **关键结果 / 消融** · 最高加 17.7 点，超 SFT 3.8 点。
- **适用条件 / 局限** · 英文枢纽可能带来语言和文化偏差。

**可复用机制** · 跨表面形式迁移优先对齐解题表征。

<a id="paper-149135"></a>

## SOLA: A Structured Operator Library for Attention in Pretrained Vision Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/149135) · [作者来源](https://openreview.net/forum?id=satkentfHg)

- **问题 / 瓶颈** · 全部头使用同一轻量近似可能损失关键结构。
- **核心创新 / 方法** · 三类结构算子替代，并用每头诊断限定误差。
- **Baseline** · 原始预训练注意力。
- **Benchmark** · 十 ViT、七种预训练。
- **关键结果 / 消融** · 多训练来源可找到适用头。
- **适用条件 / 局限** · 误差保证依赖诊断条件与输入范围。

**可复用机制** · 为低成本算子选择设置局部误差证据。

<a id="paper-155686"></a>

## SOLAR: AI-Powered Speed-of-Light Performance Analysis

[官方论文页](https://neurips.cc/virtual/2026/poster/155686) · [作者来源](https://openreview.net/forum?id=3gVc9ylFKl)

- **问题 / 瓶颈** · 相对旧实现快慢不能说明剩余空间。
- **核心创新 / 方法** · 从 PyTorch 或 JAX 程序自动派生并验证 SOL。
- **Baseline** · 相对软件实现比较。
- **Benchmark** · KernelBench、JAX/Flax、机器人工作负载。
- **关键结果 / 消融** · 支持优化定位和硬件配置推演。
- **适用条件 / 局限** · 取决于硬件模型与运行参数。

**可复用机制** · 区分已接近上限与仍值得优化的目标。

<a id="paper-148491"></a>

## Solaris: Building a Multiplayer Video World Model in Minecraft

[官方论文页](https://neurips.cc/virtual/2026/poster/148491) · [作者来源](https://openreview.net/forum?id=xP408u4Mho)

- **问题 / 瓶颈** · 逐视角模拟长时会漂移。
- **核心创新 / 方法** · 多视角联合生成，检查点 Self Forcing 支持长视域教师。
- **Baseline** · 既有模型和训练实现。
- **Benchmark** · 多玩家移动、grounding、构建和视角一致；1264 万帧。
- **关键结果 / 消融** · 方法优于对照，展示三玩家训练验证。
- **适用条件 / 局限** · 目前环境狭窄，扩玩家与真实世界需复验。

**可复用机制** · 教师的长期校验可分块降低训练内存。

<a id="paper-153893"></a>

## SOLE-R1: Video-Language Reasoning as the Sole Reward for On-Robot Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/153893) · [作者来源](https://openreview.net/forum?id=HvikTXllja)

- **问题 / 瓶颈** · 有遮挡时策略可能只优化判断器错误。
- **核心创新 / 方法** · 以视频语言时序推理作唯一在线奖励。
- **Baseline** · 现有通用 VLM 评判及真值奖励参照。
- **Benchmark** · 四种模拟与实机操作，随机初始化。
- **关键结果 / 消融** · 摘要称可零样本学未见操作。
- **适用条件 / 局限** · 若关键状态不可见仍需独立验收和安全约束。

**可复用机制** · 把跨视角与过程证据用于测奖励能否区分真完成。

<a id="paper-139395"></a>

## SOL-ExecBench: Speed-of-Light Benchmarking for Real-World GPU Kernels Against Hardware Limits

[官方论文页](https://neurips.cc/virtual/2026/poster/139395) · [作者来源](https://openreview.net/forum?id=TE8B0CjNsw)

- **问题 / 瓶颈** · 软件基线可浮动，计时与结果可能被误优化。
- **核心创新 / 方法** · 分析 SOL、沙箱编译、输入正确检查及活动计时。
- **Baseline** · 单代理优化 PyTorch 等。
- **Benchmark** · 真实内核与 SOL 分数。
- **关键结果 / 消融** · 第三方报告 1.38 倍几何平均加速，SOL 0.56。
- **适用条件 / 局限** · 口径依硬件和执行环境。

**可复用机制** · 自动优化至少同时测功能正确、实测延迟和理论上限比例。

<a id="paper-151443"></a>

## Solver-as-Teacher: Solver-Guided On-Policy Post-Training Framework for PDE Foundation Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151443) · [作者来源](https://openreview.net/forum?id=afU6OolFcZ)

- **问题 / 瓶颈** · 混沌系统长程逐点模仿会超过可预测范围，逐步误差同时累积。
- **核心创新 / 方法** · 模型在线 rollout，在自身状态附近获取数值解监督。
- **Baseline** · 标准 SFT。
- **Benchmark** · PDE 模型的 50 步 RMSE，24 个域内组合和七个参数偏移基准。
- **关键结果 / 消融** · 23/24 域内组合和全部七个偏移基准得最低 RMSE，最佳相对降幅 90%。
- **适用条件 / 局限** · 依赖可从模型状态求解的数值教师，摘要未给总计算。

**可复用机制** · 长期预测模型可在当前错误附近学习纠偏，无需精确匹配不可预测的单条未来。

<a id="paper-152502"></a>

## Solver-Aware Decompositions for Programming-by-Example: When Dividing Requires Knowing how to Conquer

[官方论文页](https://neurips.cc/virtual/2026/poster/152502) · [作者来源](https://openreview.net/forum?id=SffA3K1Xus)

- **问题 / 瓶颈** · 逻辑正确的分解可能超出有限求解器搜索能力。
- **核心创新 / 方法** · 使用求解器反馈评价和优化分解。
- **Baseline** · 人工真值分解及其先知对照。
- **Benchmark** · 若干示例驱动程序合成领域。
- **关键结果 / 消融** · 解决部分真值分解先知失败的任务。
- **适用条件 / 局限** · 换求解器可能需重校，摘要未给搜索成本。

**可复用机制** · 中间任务应匹配实际执行器而非唯一参考分解。

<a id="paper-139575"></a>

## Solving Every Step Is Not Enough: Milestone Oracles Reveal a Composition Gap in LLM Math Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/139575) · [作者来源](https://openreview.net/forum?id=HMBgtHSMNi)

- **问题 / 瓶颈** · 子题都能解仍可能无法拼成全局方案。
- **核心创新 / 方法** · 阶梯式给予路线图、子目标答案，并独立考子目标，用符号验证分类。
- **Baseline** · 无帮助和独立第二教师。
- **Benchmark** · 354 个 NuminaMath 样本，六个模型，也测试代码生成。
- **关键结果 / 消融** · 不同教师的逐题恢复判定一致率为 83% 至 87%。
- **适用条件 / 局限** · 依赖可验证的路线图，摘要未给其他领域覆盖。

**可复用机制** · 通过有控制的援助定位是分解、局部求解还是组合环节导致失败。

<a id="paper-154770"></a>

## Solving Max-Cut to Global Optimality via Feasibility-Preserving Graph Neural Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/154770) · [作者来源](https://openreview.net/forum?id=B5QAybMEKM)

- **问题 / 瓶颈** · 无约束预测不能安全剪枝，传统 SDP 代价高。
- **核心创新 / 方法** · GNN 预测原始和对偶可行的松弛解，接入分支定界。
- **Baseline** · Mosek SDP。
- **Benchmark** · Max-Cut 精确求解和运行耗时。
- **关键结果 / 消融** · 相较 Mosek 加速至多 10.6 倍。
- **适用条件 / 局限** · 依赖可构造可行预测的松弛，验证限 Max-Cut。

**可复用机制** · 用学习代理提速时，将输出限制为可作界的对象，保留原求解器的最优证书。

<a id="paper-148806"></a>

## Solving Stochastic Control under Multiplicative and Internal Noise via Constrained Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/148806) · [作者来源](https://openreview.net/forum?id=uzMEs1gPQ6)

- **问题 / 瓶颈** · 乘性噪声使部分可观察控制与滤波不再简单分离。
- **核心创新 / 方法** · 坐标下降求互相最优的线性控制和滤波。
- **Baseline** · 已有数值求解器。
- **Benchmark** · 随机线性二次控制及冗余手臂任务。
- **关键结果 / 消融** · 报告数量级加速，并发现内部噪声相关控制策略。
- **适用条件 / 局限** · 线性控制及二次代价设定，摘要未给实物迁移。

**可复用机制** · 遇到动作改变传感噪声时先检验估计控制分离假设，再设计联动更新。

<a id="paper-153057"></a>

## Sophon: A Procedural Diagnostic for Spatial Reasoning in Vision-Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153057) · [作者来源](https://openreview.net/forum?id=OL7Mvsjyzg)

- **问题 / 瓶颈** · 低准确率可能来自没有空间表示或不会将表示转成答案。
- **核心创新 / 方法** · 用程序控场景与不同坐标问法，并分析词表方向和表示。
- **Baseline** · 开放 VLM、前沿闭源模型及人工。
- **Benchmark** · 四类题型及多坐标体系，使用正确率。
- **关键结果 / 消融** · 开放模型 47% 至 52%，前沿 77% 至 83%，人类 84% 至 94%。
- **适用条件 / 局限** · 程序化几何未必代表自然场景。

**可复用机制** · 当表征探针有信号但答案仍错时，单独测试从表征到选项的读出瓶颈。

<a id="paper-154927"></a>

## Soteria: Formally Verified Planning with Runtime Enforcement for Safe LLM Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/154927) · [作者来源](https://openreview.net/forum?id=9url1EFMaU)

- **问题 / 瓶颈** · 只验证计划不足以约束实际工具调用。
- **核心创新 / 方法** · 在首次工具调用前验证结构化计划，再据已验证计划控制运行。
- **Baseline** · 既有代理护栏。
- **Benchmark** · 多类工具任务，比较规范符合和任务效用。
- **关键结果 / 消融** · 作者报告规范全部满足且效用最高为对照五倍。
- **适用条件 / 局限** · 需要可形式化规格和可信执行层。

**可复用机制** · 把计划和实际副作用联接到同一规则，防止途中偏离已审核步骤。

<a id="paper-149794"></a>

## Sound Verification of Deployed Neural Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/149794) · [作者来源](https://openreview.net/forum?id=nHbkxmdykn)

- **问题 / 瓶颈** · 验证器和部署算子顺序不同时，实数级证明可能不覆盖浮点执行。
- **核心创新 / 方法** · 核对操作树差异并在证明中涵盖数值误差。
- **Baseline** · 既有验证和部署运行。
- **Benchmark** · 神经网络部署验证的数值一致性与性能。
- **关键结果 / 消融** · 摘要报告有限开销，并检测到所测已知失效。
- **适用条件 / 局限** · 依赖已覆盖的部署数值和操作模型。

**可复用机制** · 验证通过后仍应比较目标设备上的算子语义，尤其当编译与融合会改变计算顺序。

<a id="paper-154092"></a>

## Source-Causal Control of Historical Context in Longitudinal Radiology Report Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/154092) · [作者来源](https://openreview.net/forum?id=GHvYdC6tmg)

- **问题 / 瓶颈** · 历史可补漏也可能诱导模型陈述当前证据没有支持的发现。
- **核心创新 / 方法** · 对同一当前输入分别给真历史、匹配错误历史等条件，量化错误方向。
- **Baseline** · 真实、错误与不提供历史等条件。
- **Benchmark** · MIMIC-CXR 18,716 对，五种条件及代理假阳性假阴性。
- **关键结果 / 消融** · 错误历史每报告代理假阳性加 0.366、假阴性少 0.129。
- **适用条件 / 局限** · 指标为代理，证据来自胸片。

**可复用机制** · 可以测试模型是不是真的核验当前观测，还是机械复述相关的历史资料。

<a id="paper-150441"></a>

## SP$^2$ec: Adaptive Self-Speculative Decoding for Vision-Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150441) · [作者来源](https://openreview.net/forum?id=i1ipNcYYoM)

- **问题 / 瓶颈** · 统一草稿结构可能无法平衡不同请求的吞吐与验证率。
- **核心创新 / 方法** · 用吞吐相对层数的单峰性来最小化每请求的墙钟遗憾。
- **Baseline** · 静态草稿和其他自推测方法。
- **Benchmark** · Qwen3-VL、LLaVA-1.5 的视觉与文本任务。
- **关键结果 / 消融** · 摘要报告有效，并有适应单峰的遗憾分析。
- **适用条件 / 局限** · 依赖单峰近似，摘要未列加速数值。

**可复用机制** · 推测解码应按负载选择草稿复杂度，以墙钟收益而非接受率单独驱动。

<a id="paper-154253"></a>

## SP$^3$: Spherical Priors for Plug-and-Play Restoration

[官方论文页](https://neurips.cc/virtual/2026/poster/154253) · [作者来源](https://openreview.net/forum?id=F9SLbhP7uz)

- **问题 / 瓶颈** · 无训练生成先验常需推理梯度与多次迭代。
- **核心创新 / 方法** · 在半二次分裂中执行投影与测量校正。
- **Baseline** · 零样本扩散和流恢复。
- **Benchmark** · 多种图像恢复场景，比较感知质量和速度。
- **关键结果 / 消融** · 摘要报告质量相当，速度为对照 3 至 630 倍。
- **适用条件 / 局限** · 依赖有闭式数据一致性或可简化的观测模型。

**可复用机制** · 逆问题中把先验和测量分成各自低成本的一步，尽早给出可用结果。

<a id="paper-153437"></a>

## Space-Aware World Models: Spatial Persistence Through Factored Scene Representations

[官方论文页](https://neurips.cc/virtual/2026/poster/153437) · [作者来源](https://openreview.net/forum?id=LIkrG4Xb53)

- **问题 / 瓶颈** · 每步重新生成场景会逐渐破坏空间布局。
- **核心创新 / 方法** · 分解场景潜变量与可演化运动状态。
- **Baseline** · 普通潜空间世界模型。
- **Benchmark** · 静态布局、地图观测的导航式问题。
- **关键结果 / 消融** · 作者报告减少场景生成误差并改善表现。
- **适用条件 / 局限** · 依赖布局在整局不变，且需地图式观察。

**可复用机制** · 可明确冻结的环境结构应和会变化的行动状态分开建模。

<a id="paper-152663"></a>

## Space Group Conditional Flow Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/152663) · [作者来源](https://openreview.net/forum?id=RKIPnVN3E0)

- **问题 / 瓶颈** · 自由生成坐标时高对称合法样本不足。
- **核心创新 / 方法** · 训练空间群条件流匹配，并使用群平均维持对称。
- **Baseline** · 常规晶体生成器。
- **Benchmark** · MP-20 晶体从头生成。
- **关键结果 / 消融** · 作者报告先进结果且对称化成本很小。
- **适用条件 / 局限** · 依赖已知对称群，摘要未给其他领域结果。

**可复用机制** · 可信的群结构可嵌入生成步骤，减少事后修复约束的负担。

<a id="paper-155167"></a>

## SPACE: Unifying Symmetric and Asymmetric Routing Problems for Generalist Neural Solver

[官方论文页](https://neurips.cc/virtual/2026/poster/155167) · [作者来源](https://openreview.net/forum?id=7ncFxVZuOq)

- **问题 / 瓶颈** · 对称与非对称路径成本不一定共享欧氏几何。
- **核心创新 / 方法** · 选择参考枢轴形成统一的坐标无关表示。
- **Baseline** · 对称路线的坐标模型或分任务求解器。
- **Benchmark** · 55 类对称和对应非对称，共 110 种路线设置。
- **关键结果 / 消融** · 报告两种几何设定下均有可用的零样本泛化。
- **适用条件 / 局限** · 依赖选定枢轴代表底层距离，摘要未给成本和差值。

**可复用机制** · 缺少可信全局坐标时，使用与若干稳定参考点的双向位置关系描述对象。

<a id="paper-155840"></a>

## SpanFormer: Multi-Level Adaptive Sparsity for Object Detection in High-Resolution Wide Shots

[官方论文页](https://neurips.cc/virtual/2026/poster/155840) · [作者来源](https://openreview.net/forum?id=2VF28peAaM)

- **问题 / 瓶颈** · 孤立局部窗会缺远处相关信息
- **核心创新 / 方法** · 按视觉相似与空间半径聚类保留窗口，并共享投影拼接 K/V
- **Baseline** · SparseFormer
- **Benchmark** · PANDA 千兆像素检测；AP50 与骨干 FLOPs
- **关键结果 / 消融** · AP50 从 78.0% 至 80.3%，FLOPs 少超 75%
- **适用条件 / 局限** · 相似窗口可能漏掉远距非相似依赖

**可复用机制** · 给高分视觉助手同时测 token 预算、远距离理解和小目标召回

<a id="paper-150088"></a>

## SPANUQ: Span-Level Uncertainty Quantification for Large Language Model Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/150088) · [作者来源](https://openreview.net/forum?id=kn5hr1973d)

- **问题 / 瓶颈** · 整体置信不能说明哪项主张要复核
- **核心创新 / 方法** · 估每个文本片段不确定性，再学习重要性加权聚合
- **Baseline** · 片段启发式及序列级方法
- **Benchmark** · 五 LLM 两模型族，片段 AUROC 与序列相关
- **关键结果 / 消融** · AUROC 0.908–0.944，组合与序列指标相关 0.839
- **适用条件 / 局限** · 需要稳定划分片段及局部标签

**可复用机制** · 把审核算力安排到低可信片段，并核对聚合误差

<a id="paper-153049"></a>

## Sparse All-Layer Connector for Domain Generalised Semantic Segmentation

[官方论文页](https://neurips.cc/virtual/2026/poster/153049) · [作者来源](https://openreview.net/forum?id=OPMdo1lyMp)

- **问题 / 瓶颈** · 不同骨干相同深度不代表相同域迁移价值
- **核心创新 / 方法** · 稀疏选择候选层并以候选 dropout 鼓励更稳选择
- **Baseline** · 常规深度对齐融合
- **Benchmark** · 四基础模型组合、三域泛化分割设置
- **关键结果 / 消融** · 摘要报告泛化优于对照，未给数字
- **适用条件 / 局限** · 效果依赖候选层覆盖和域设置

**可复用机制** · 给多模态连接器加跨域固定层与动态选层对照

<a id="paper-150458"></a>

## Sparse Attention as a Range Searching Problem: Towards an Inference-Efficient Index for KV Cache

[官方论文页](https://neurips.cc/virtual/2026/poster/150458) · [作者来源](https://openreview.net/forum?id=htJoIGk2K0)

- **问题 / 瓶颈** · 只测速度会遗漏原本高权重的键
- **核心创新 / 方法** · 把高权重键定位转化为范围搜索，做 CPU/GPU 索引优化
- **Baseline** · 既有稀疏注意力及 FlashAttention
- **Benchmark** · 准确率与推理时延，摘要未给任务细目
- **关键结果 / 消融** · 摘要报告相对于稀疏法两项俱优，并快于稠密实现
- **适用条件 / 局限** · 实际收益受索引复用和硬件影响

**可复用机制** · 长上下文索引同时测高权重键召回、墙钟及整任务质量

<a id="paper-155048"></a>

## Sparse Delta Memory: Scaling the State of Linear RNNs through Sparsity

[官方论文页](https://neurips.cc/virtual/2026/poster/155048) · [作者来源](https://openreview.net/forum?id=8qEsjLzluv)

- **问题 / 瓶颈** · 等参数量不代表一样的长程记忆容量
- **核心创新 / 方法** · 扩大显式状态而只访问少量单元，并可学习初始状态
- **Baseline** · 等 FLOPs 与等参数的线性记忆
- **Benchmark** · 上下文学习、长程检索、常识及推理
- **关键结果 / 消融** · 较大状态改善检索，学习初态进一步提升
- **适用条件 / 局限** · 需高效稀疏读写并处理寻址冲突

**可复用机制** · 比较内存容量和每步访存，避免只按参数选线性骨干

<a id="paper-154235"></a>

## Sparse Expansion Utility: Identifying and Routing to Pivotal Steps in LLM Reasoning Chains

[官方论文页](https://neurips.cc/virtual/2026/poster/154235) · [作者来源](https://openreview.net/forum?id=FDeJvVyqif)

- **问题 / 瓶颈** · 分类 AUC 高仍可能挑到有负收益的步骤
- **核心创新 / 方法** · 用样本内列表相对顺序消除模型与基准的效用尺度差异
- **Baseline** · 逐步 top-k BCE
- **Benchmark** · 跨模型与基准的扩展步骤，AUC@10 和实际收益
- **关键结果 / 消融** · AUC 为 0.70 的逐点方法收益为负，列表损失纠正反转
- **适用条件 / 局限** · 未完成等 token 的自一致或 best-of-N 对比

**可复用机制** · 把路由决策收益当主要验收，单列分类指标

<a id="paper-149627"></a>

## Sparse Koopman Autoencoders Identify Local Dynamical Regimes in Multibasin Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/149627) · [作者来源](https://openreview.net/forum?id=oenYjKFj4D)

- **问题 / 瓶颈** · 密集全局潜态会混合多个运动规律
- **核心创新 / 方法** · 学习稀疏潜表示，并以激活支持编码区域
- **Baseline** · 密集潜态 Koopman 自编码器
- **Benchmark** · 多势阱非线性系统、留出盆地内部状态
- **关键结果 / 消融** · 稀疏支持能区分区域，密集版本坍为单族
- **适用条件 / 局限** · 未验证真实接触系统，需明确状态覆盖

**可复用机制** · 在摩擦或接触切换模型中检查潜支持是否随区间改变

<a id="paper-148156"></a>

## Sparse Layers are Critical to Scaling Looped Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148156) · [作者来源](https://openreview.net/forum?id=zt77AglOvq)

- **问题 / 瓶颈** · 任意层退出不能借助输出层的一致性
- **核心创新 / 方法** · 以稀疏专家扩展循环模型，并比较不同停止点输出收敛
- **Baseline** · 标准 Transformer、不同早退点
- **Benchmark** · 循环模型扩展、质量和效率
- **关键结果 / 消融** · 摘要称边界收敛更快且稀疏循环扩展改善权衡
- **适用条件 / 局限** · 依赖各循环共享末端结构

**可复用机制** · 动态算力策略用完整迭代作为首个对照

<a id="paper-155610"></a>

## Sparsely Supervised Diffusion

[官方论文页](https://neurips.cc/virtual/2026/poster/155610) · [作者来源](https://openreview.net/forum?id=4HalTYbzQG)

- **问题 / 瓶颈** · 密集重建可能记忆训练样本并不稳定
- **核心创新 / 方法** · 随机屏蔽绝大部分像素监督，大部分上下文仍用于估分
- **Baseline** · 常规扩散监督
- **Benchmark** · 多图像集，FID、记忆和训练稳定性
- **关键结果 / 消融** · 最高掩码 98% 仍具竞争力
- **适用条件 / 局限** · 真实特征密度与采样掩码的关系待查

**可复用机制** · 小样本生成同时核对去重召回和 FID

<a id="paper-151057"></a>

## Sparse Multimodal Switching State-Space Models for Regime-Dependent Neural Connectivity under Partial Observations

[官方论文页](https://neurips.cc/virtual/2026/poster/151057) · [作者来源](https://openreview.net/forum?id=dJy3Ipz0tx)

- **问题 / 瓶颈** · 固定连接不能表示时变共变。
- **核心创新 / 方法** · 联合建模 EEG 与 iEEG 观测、切换潜过程及稀疏边。
- **Baseline** · 最强平稳方案和两阶段连接推断。
- **Benchmark** · 合成恢复，Edge F1。
- **关键结果 / 消融** · 相对提升约 25% 和 64%。
- **适用条件 / 局限** · 真实潜连接不可直接验证，结构假设需检。

**可复用机制** · 多传感图推断时区分读出缺失与系统机制切换。

<a id="paper-153731"></a>

## Sparse Planning in Visual World Models via Cost Gradients

[官方论文页](https://neurips.cc/virtual/2026/poster/153731) · [作者来源](https://openreview.net/forum?id=JDEHvMtOmX)

- **问题 / 瓶颈** · 均匀或显著性筛选会保留不相关物体。
- **核心创新 / 方法** · 免训练按输入空间 token 的目标代价梯度范数排序。
- **Baseline** · 目标无关稀疏选择。
- **Benchmark** · 视觉世界模型规划及计算。
- **关键结果 / 消融** · 摘要给出目标条件选择器，量化待核。
- **适用条件 / 局限** · 局部梯度对远期事件可能不稳。

**可复用机制** · 按行动目标的敏感性裁剪感知上下文。

<a id="paper-155383"></a>

## Sparse Repair in Reasoning Traces: A Structural View of Test-Time Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/155383) · [作者来源](https://openreview.net/forum?id=63LOfNSXwb)

- **问题 / 瓶颈** · 全轨迹反复采样浪费预算。
- **核心创新 / 方法** · 分开离线反事实发现和可部署位置分配。
- **Baseline** · 基础解码和完整轨迹采样。
- **Benchmark** · 三模型、四任务族。
- **关键结果 / 消融** · 约 1.31 倍生成 token 成本时平均加 4.2 点，11/12 对最优。
- **适用条件 / 局限** · 依赖关键点发现能迁移，预算需实测。

**可复用机制** · 确认瓶颈位置后再保留少量重采样。

<a id="paper-155694"></a>

## Sparse Reward Subsystem in Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155694) · [作者来源](https://openreview.net/forum?id=3dZL4FURuU)

- **问题 / 瓶颈** · 隐藏状态可预测不等于特征具有实际作用。
- **核心创新 / 方法** · 定位稀疏价值神经元并做迁移和因果检验。
- **Baseline** · 分散的隐藏状态信号。
- **Benchmark** · 多数据集和模型，置信度与过程搜索。
- **关键结果 / 消融** · 价值信号跨数据和模型，支持内部过程引导。
- **适用条件 / 局限** · 神经元功能可能依语境重叠。

**可复用机制** · 用稀疏探针和介入共同验证内部奖励来源。

<a id="paper-150790"></a>

## Sparse Sum-of-Squares Layers for Certified Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/150790) · [作者来源](https://openreview.net/forum?id=fO3zFhG0ES)

- **问题 / 瓶颈** · 只在前向稀疏导致训练成本和证书结构丢失。
- **核心创新 / 方法** · SOS 反传复用局部块、重叠及稀疏约束。
- **Baseline** · 普通 SDP/SOS 层。
- **Benchmark** · 有认证学习任务。
- **关键结果 / 消融** · 摘要报告可扩反传及保结构，数值待核。
- **适用条件 / 局限** · 需要原问题有可用稀疏分解。

**可复用机制** · 端到端约束学习同时审计前向和隐式梯度复杂度。

<a id="paper-148588"></a>

## Sparse Updates Generalize Better Than Optimization: Stability Analysis for Randomized Subspace Descent

[官方论文页](https://neurips.cc/virtual/2026/poster/148588) · [作者来源](https://openreview.net/forum?id=weRx6oFuWD)

- **问题 / 瓶颈** · 下降更快未必泛化更好。
- **核心创新 / 方法** · 用稳定性分析比较随机子空间优化与全量方向。
- **Baseline** · 不同子空间大小的下降。
- **Benchmark** · 凸与非凸实证。
- **关键结果 / 消融** · 支持泛化和优化权衡。
- **适用条件 / 局限** · 结论受样本和各步随机抽取假设制约。

**可复用机制** · 选稀疏预算时分别记录训练收敛和稳定性。

<a id="paper-155269"></a>

## Sparse Video Generation Propels Real-World Beyond-the-View Vision-Language Navigation

[官方论文页](https://neurips.cc/virtual/2026/poster/155269) · [作者来源](https://openreview.net/forum?id=6xFifx1LaW)

- **问题 / 瓶颈** · 逐帧视频推理达不到闭环时限。
- **核心创新 / 方法** · 以稀疏 20 秒未来指导亚秒动作预测。
- **Baseline** · 强 LLM 导航。
- **Benchmark** · 真实零样本 BVN，含夜间。
- **关键结果 / 消融** · 成功率为基线 2.5 倍。
- **适用条件 / 局限** · 生成预测仍需安全感知纠偏。

**可复用机制** · 在导航中用低时域采样换可在线的远期视觉前瞻。

<a id="paper-148319"></a>

## Sparsity for Free: A Budget-Induced Equilibrium in Joint Topology–Parameter Search

[官方论文页](https://neurips.cc/virtual/2026/poster/148319) · [作者来源](https://openreview.net/forum?id=yhAndGxKFn)

- **问题 / 瓶颈** · 高维参数来不及优化会让稀疏候选看起来更优。
- **核心创新 / 方法** · 结合 CMA-ES 有限预算与有噪排名推拓扑平衡。
- **Baseline** · 稠密拓扑及双层搜参。
- **Benchmark** · EvoluCMAES 的联合拓扑和参数搜索。
- **关键结果 / 消融** · 理论预测固定预算下稳态偏稀疏。
- **适用条件 / 局限** · 搜索排名可能反映优化难度而非拓扑固有质量。

**可复用机制** · 给稠密对照同等有效收敛预算，再判断剪枝价值。

<a id="paper-139780"></a>

## SpatialBench: Is Your Spatial Foundation Model an All-Round Player

[官方论文页](https://neurips.cc/virtual/2026/poster/139780) · [作者来源](https://openreview.net/forum?id=5Fvw97JTqm)

- **问题 / 瓶颈** · 狭窄单任务基准难测综合泛化。
- **核心创新 / 方法** · 跨任务与采样条件诊断。
- **Baseline** · 多种空间基础模型。
- **Benchmark** · SpatialBench 的多域、输入密度及硬件。
- **关键结果 / 消融** · 摘要提供广覆盖评估，具体规律待核。
- **适用条件 / 局限** · 对于目标硬件仍要独立测延迟。

**可复用机制** · 单独比较采样策略与模型能力，减少选型混杂。

<a id="paper-149047"></a>

## SpatialClaw: Rethinking Action Interface for Agentic Spatial Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/149047) · [作者来源](https://openreview.net/forum?id=tHCYfFr3sR)

- **问题 / 瓶颈** · 一次性脚本早承诺，固定工具接口不够组合。
- **核心创新 / 方法** · 有状态 Python 内核中逐单元调用感知与几何原语。
- **Baseline** · 一次执行和结构化工具调用。
- **Benchmark** · 空间推理代理。
- **关键结果 / 消融** · 支持运行时调整，摘要效果数字待核。
- **适用条件 / 局限** · 需隔离执行和可审计数据权限。

**可复用机制** · 把行动定义成带反馈的原语组合，分开程序有效与空间正确。

<a id="paper-139727"></a>

## SPATIALEPIBENCH: Benchmarking Spatial Information and Epidemic Priors in Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/139727) · [作者来源](https://openreview.net/forum?id=857OhlxF9J)

- **问题 / 瓶颈** · 简单一次时间切分会夸大复杂先验。
- **核心创新 / 方法** · 统一时间推进评估，同时对照持久性预测。
- **Baseline** · 最后值与邻接增强模型。
- **Benchmark** · 11 现实时间序列评测集。
- **关键结果 / 消融** · 多个提前量下多种复杂方法仍低于简基线。
- **适用条件 / 局限** · 不同数据和评测切分不能直接外推排序。

**可复用机制** · 部署时序模型前先确认结构先验超出最近观测的真实增益。

<a id="paper-148740"></a>

## SpatialFlow-GRPO: Where Spatial Credit Drives Image Editing

[官方论文页](https://neurips.cc/virtual/2026/poster/148740) · [作者来源](https://openreview.net/forum?id=vOr0WAaBeN)

- **问题 / 瓶颈** · 全局奖励抹掉哪处编辑成功。
- **核心创新 / 方法** · 训练区域评审并使空间奖励指导 GRPO。
- **Baseline** · 全图奖励编辑。
- **Benchmark** · SFReward-14K 和 MultiEditBench。
- **关键结果 / 消融** · 局部反馈提高编辑质量，摘要无准确幅度。
- **适用条件 / 局限** · 需要空间标注和不相关区保持对照。

**可复用机制** · 不同编辑区分别计功，防止强势区域替弱区域得分。

<a id="paper-139304"></a>

## Spatial-IQ: Deconstructing Spatial Intelligence via Hierarchical Capability Tests

[官方论文页](https://neurips.cc/virtual/2026/poster/139304) · [作者来源](https://openreview.net/forum?id=YQbS1ro7SL)

- **问题 / 瓶颈** · 边界识别与遮挡推理瓶颈混杂。
- **核心创新 / 方法** · 九项分层子任务并另查心理旋转，比较三种输出格式。
- **Baseline** · 只看总体正确的基准。
- **Benchmark** · Spatial-IQ，文本、图选和图编辑。
- **关键结果 / 消融** · 摘要提出分项定位，具体失败差异待核。
- **适用条件 / 局限** · 层级锚定一种人类发展结构。

**可复用机制** · 复杂空间任务按必要子能力设计测试，改变输出格式排除接口混杂。

<a id="paper-151858"></a>

## Spatially Feasible 3D Indoor Scene Generation via Interaction-Oriented Human Proxy

[官方论文页](https://neurips.cc/virtual/2026/poster/151858) · [作者来源](https://openreview.net/forum?id=XOBgPRg5Vn)

- **问题 / 瓶颈** · 几何像真可能无法通行或操作。
- **核心创新 / 方法** · 以人形代理约束交互空间。
- **Baseline** · 普通室内生成。
- **Benchmark** · 布局质量与空间合理性。
- **关键结果 / 消融** · 摘要报告改善，幅度未核。
- **适用条件 / 局限** · 代理行为覆盖和不同实施体需重测。

**可复用机制** · 为机器人场景将可达交互纳入生成验收。

<a id="paper-154561"></a>

## Spatially-Grounded Long Video Generation with Self Geometry Forcing

[官方论文页](https://neurips.cc/virtual/2026/poster/154561) · [作者来源](https://openreview.net/forum?id=CfeJnlX4X0)

- **问题 / 瓶颈** · 只传外观会累积空间漂移。
- **核心创新 / 方法** · 联合外观与几何扩散，自强制训练并对中间预测做几何验证。
- **Baseline** · 因果视频扩散和普通蒸馏。
- **Benchmark** · 长视频的外观、空间一致和可控。
- **关键结果 / 消融** · 摘要称恒定逐帧计算且三轴改善。
- **适用条件 / 局限** · 依赖初期几何预测质量。

**可复用机制** · 长期记忆学习要模拟自身估计误差并检测几何一致性。

<a id="paper-154721"></a>

## Spatial Representation Distillation and Knowledge Routing for Vision-Language-Action Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154721) · [作者来源](https://openreview.net/forum?id=BUe7sbiSLH)

- **问题 / 瓶颈** · 大语言底座成本不一定是动作能力关键。
- **核心创新 / 方法** · 通过空间结构蒸馏和知识路由给轻量主干。
- **Baseline** · 较大 VLA。
- **Benchmark** · 模拟和实机操作。
- **关键结果 / 消融** · 0.5B 主干及 50M 可训参数达到或超过部分较大模型。
- **适用条件 / 局限** · 需可用空间监督，任务覆盖决定迁移。

**可复用机制** · 按控制所需知识选择蒸馏目标，而非统一放大主干。

<a id="paper-153697"></a>

## Spatial-temporal Attributes Enhanced Prompt Weighting and Fusion for Video Recognition

[官方论文页](https://neurips.cc/virtual/2026/poster/153697) · [作者来源](https://openreview.net/forum?id=JSGGhTC9BN)

- **问题 / 瓶颈** · LLM 生成提示会有不相关或错误属性。
- **核心创新 / 方法** · 以视频特征相似度动态加权属性嵌入。
- **Baseline** · 固定模板和一律扩展文本提示。
- **Benchmark** · 多视频识别任务。
- **关键结果 / 消融** · 摘要给出适配方案，效果幅度待核。
- **适用条件 / 局限** · 相似度本身可偏向主导背景。

**可复用机制** · 文本先验应为当前观测提供可衰减证据。

<a id="paper-151702"></a>

## SpatialVAM: Spatial-Aware Multi-View Video Diffusion as a Data-Efficient Robot Policy

[官方论文页](https://neurips.cc/virtual/2026/poster/151702) · [作者来源](https://openreview.net/forum?id=Yg9wmxxbDb)

- **问题 / 瓶颈** · 外观视频未明确编码三维动作。
- **核心创新 / 方法** · 联合未来空间动作热图与多相机 RGB。
- **Baseline** · 视频动作模型、VLA、3D 策略。
- **Benchmark** · Meta-World、RoboCasa 和实机，只十条示范。
- **关键结果 / 消融** · 摘要分别报告提高 22%、10%、16%。
- **适用条件 / 局限** · 多相机标定和真实接触预估限制迁移。

**可复用机制** · 共享未来生成可解耦可解释控制线索和外观。

<a id="paper-152385"></a>

## SP-CACW: Convergence-Aware Client Weighting for Selfish Personalized Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/152385) · [作者来源](https://openreview.net/forum?id=TUVCMnWa8i)

- **问题 / 瓶颈** · 启发式客户端绩效代理缺理论。
- **核心创新 / 方法** · 构建收敛感知客户端混合权重。
- **Baseline** · 启发加权和分群。
- **Benchmark** · MNIST、CIFAR、LEAF Shakespeare。
- **关键结果 / 消融** · 给出收敛保证并实证，幅度未核。
- **适用条件 / 局限** · 客户端目标及异质条件须重新核对。

**可复用机制** · 共享训练中先估哪些外部客户端更新能具体改善本地收敛。

<a id="paper-139762"></a>

## SPDEBench: An Extensive Benchmark for Learning Stochastic PDEs

[官方论文页](https://neurips.cc/virtual/2026/poster/139762) · [作者来源](https://openreview.net/forum?id=6ARrY9kPwQ)

- **问题 / 瓶颈** · 不同数值处理会让基准的轨迹来自不同学习问题。
- **核心创新 / 方法** · 用受控数值方案建立含奇异方程的基准并比较模型。
- **Baseline** · 通用算子学习基线。
- **Benchmark** · 随机 PDE 的多条件长时空预测任务。
- **关键结果 / 消融** · 摘要指出部分针对性模型优于通用算子学习。
- **适用条件 / 局限** · 依赖参考求解器，摘要未给各生成变量的独立效应量。

**可复用机制** · 比较随机系统预测前固定参考数据生成语义，将数值变化单独作为外推条件。

<a id="paper-152241"></a>

## Speak Early: Speculative Speech Generation for Low-Latency SpeechLLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/152241) · [作者来源](https://openreview.net/forum?id=UXN4JDGgR2)

- **问题 / 瓶颈** · 只加速语言解码会留下同量级的语音等待。
- **核心创新 / 方法** · 以可推测的早期语言内容触发合成并在不重启时校正。
- **Baseline** · 分阶段语音语言模型推理。
- **Benchmark** · 语音语言模型的首个语音延迟、正确性与语音质量。
- **关键结果 / 消融** · 首个语音延迟减少 18% 至 30%，维持质量与正确性。
- **适用条件 / 局限** · 依赖可增量纠正的合成，摘要未给严重推测错误代价。

**可复用机制** · 流式模型要量整个关键路径，考虑可撤销或可纠正的下游预处理。

<a id="paper-150056"></a>

## SpecBlock: Block-Iterative Speculative Decoding with Dynamic Tree Drafting

[官方论文页](https://neurips.cc/virtual/2026/poster/150056) · [作者来源](https://openreview.net/forum?id=l6JgXCnnMq)

- **问题 / 瓶颈** · 独立多 token 草稿便宜但接受率受限。
- **核心创新 / 方法** · 块迭代生成相依候选，并在预计吞吐收益高于成本时调整树。
- **Baseline** · EAGLE-3。
- **Benchmark** · 推测解码速度和起草计算对照。
- **关键结果 / 消融** · 平均速度增 8% 至 13%，起草开销为对照 44% 至 52%；自适应后速度增 11% 至 19%。
- **适用条件 / 局限** · 摘要未列硬件、批量和模型适用范围。

**可复用机制** · 并行草稿时保留块内条件依赖，并以真实运行成本决定树调整。

<a id="paper-148847"></a>

## SpecBridge: Learning Natural-Language Formalization Plans for the Formal Specification Synthesis Task

[官方论文页](https://neurips.cc/virtual/2026/poster/148847) · [作者来源](https://openreview.net/forum?id=ui1AYUwFTN)

- **问题 / 瓶颈** · 非正式意图到证明语法存在表示间隙，语法通过不代表语义满足。
- **核心创新 / 方法** · 用自然语言规划桥接，并逐层执行可计算及证明验证。
- **Baseline** · 直接形式规格合成。
- **Benchmark** · 自然语言程序需求到证明助手规格，含执行与证明通过率。
- **关键结果 / 消融** · 摘要报告可计算验证增加 15.2%，证明验证增加 28.4%。
- **适用条件 / 局限** · 依赖形式签名和验证器，摘要未给形式语义指标范围。

**可复用机制** · 对要求严谨的生成任务，可用可核查的中间语义结构，再编译为目标语言。

<a id="paper-148346"></a>

## SpecDrop: Parameter-Free Category-Conditioned Routing for Modular Specialization

[官方论文页](https://neurips.cc/virtual/2026/poster/148346) · [作者来源](https://openreview.net/forum?id=yYWJotX1BO)

- **问题 / 瓶颈** · 路由效果可能来自分类与专业能力恰好对齐。
- **核心创新 / 方法** · 以粗标签提供固定分支权重，并改变跨任务的对齐程度。
- **Baseline** · 参数预算匹配的学习路由和多分支无路由。
- **Benchmark** · ImageNet-1K、CIFAR-100、SlimPajama 与 SuperNI LoRA。
- **关键结果 / 消融** · 粒度吻合时匹配或超过学习路由，失配时只匹配无路由。
- **适用条件 / 局限** · 需要可用类别标签，不能假定类别越细越好。

**可复用机制** · 判断是否训练新路由器前先验证监督类别和希望出现的专家分工是否在同一尺度。

<a id="paper-150381"></a>

## SpecHop: Continuous Speculation for Accelerating Multi-Hop Retrieval Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/150381) · [作者来源](https://openreview.net/forum?id=iS6Bu6eqWc)

- **问题 / 瓶颈** · 链式工具调用延迟叠加，直接替换工具可能改决策。
- **核心创新 / 方法** · 连续维护多个推测线程，并用原始观测验证。
- **Baseline** · 原始非推测工具调用。
- **Benchmark** · 多跳检索增强任务，以墙钟和原代理输出一致性衡量。
- **关键结果 / 消融** · 部分设置降低延迟至多 40%，接近理论预测。
- **适用条件 / 局限** · 依赖快而有预测性的工具和并行资源。

**可复用机制** · 能可靠验证时，以未确认推测做可撤销准备，保持正式执行路径不变。

<a id="paper-148508"></a>

## Specialist Mediators: Causal Localization of Dense Fine-Tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/148508) · [作者来源](https://openreview.net/forum?id=xK0zRemqmT)

- **问题 / 瓶颈** · 激活内可定位的能力不一定能由稀疏参数更新复制。
- **核心创新 / 方法** · 对密集微调做激活替换，分别衡量域内恢复和域外影响，再测试稀疏更新。
- **Baseline** · 密集微调、激活替换及局部稀疏适配。
- **Benchmark** · 多个专门任务含 GSM8K。
- **关键结果 / 消融** · 摘要报告部分设置注意力解释收益，但在 GSM8K 中 MLP 贡献显著。
- **适用条件 / 局限** · 激活替换与真实部署更新不同。

**可复用机制** · 分别测试机制可定位、行为可恢复及参数可实现三个条件，再决定剪去哪个适配模块。

<a id="paper-149673"></a>

## Specificity-Aware Diffusion Steering via Variance-Reduced Sequential Monte Carlo

[官方论文页](https://neurips.cc/virtual/2026/poster/149673) · [作者来源](https://openreview.net/forum?id=oIBOJ76wYl)

- **问题 / 瓶颈** · 笼统排斥负条件容易引起目标模式移动和粒子权重塌缩。
- **核心创新 / 方法** · 用重叠目标定义似然比门槛，并以低方差序贯蒙特卡洛采样。
- **Baseline** · 负引导扩散基线。
- **Benchmark** · 含文生图的采样和特异性评估。
- **关键结果 / 消融** · 摘要报告少模态漂移、权重更稳定且更能抑制不期望区域。
- **适用条件 / 局限** · 依赖可比较的参考分布，摘要未给采样额外时间。

**可复用机制** · 需要排除不想要的属性时，先检查功能性目标的重叠边界，避免误删正目标独有区域。

<a id="paper-152867"></a>

## SpecLoR: Spectral Lookahead Rectification for Motion-Coherent Text-to-Video Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/152867) · [作者来源](https://openreview.net/forum?id=PoLjtyYc3T)

- **问题 / 瓶颈** · 原始中间状态含噪，直接在空间修正会破坏局部外观。
- **核心创新 / 方法** · 用前瞻预测获取结构信号后在频域校正。
- **Baseline** · Wan2.2 默认去噪及已有视频修正方法。
- **Benchmark** · 多个运动生成基准、物理伪影和运动连贯性。
- **关键结果 / 消融** · 摘要报告改善，40 步设置只额外 4 次函数评估。
- **适用条件 / 局限** · 依赖预测及频带选择，摘要未给各视频类型作用边界。

**可复用机制** · 需要保留局部细节时可把运动一致性干预限制到结构相关频率。

<a id="paper-155889"></a>

## SPECS: Faster Test-Time Scaling through Speculative Drafts and Dynamic Switching

[官方论文页](https://neurips.cc/virtual/2026/poster/155889) · [作者来源](https://openreview.net/forum?id=24r1YmB7zX)

- **问题 / 瓶颈** · 每一个推理分支都用大模型串行生成开销高。
- **核心创新 / 方法** · 以软验证策略选择续写并按需切换。
- **Baseline** · 既有推理时扩展比较。
- **Benchmark** · 推理基准和延迟，摘要片段未列具体条件。
- **关键结果 / 消融** · 报告减少延迟约 26%，理论大并行极限对应 KL 正则目标。
- **适用条件 / 局限** · 依赖额外并行算力、可用的评分器和两模型协作。

**可复用机制** · 推理流程能有效评估候选时，把探索与验证分配给不同开销模型。

<a id="paper-151780"></a>

## Spectral-Aligned Pruning for Universal Error-Correcting Code Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/151780) · [作者来源](https://openreview.net/forum?id=Y5hbfFtOH1)

- **问题 / 瓶颈** · 逐任务剪枝开销高且专门掩码难复用。
- **核心创新 / 方法** · 依据纠错码对应二部图的谱筛选可共享的稀疏配置。
- **Baseline** · 逐码单独剪枝。
- **Benchmark** · 多种纠错码，按解码效果、计算及模型内存比较。
- **关键结果 / 消融** · 摘要报告效果接近专用剪枝并节省计算及内存。
- **适用条件 / 局限** · 图谱依据针对特定纠错结构，其他架构未经验证。

**可复用机制** · 若任务的稀疏依赖可由图描述，可以先匹配谱相似性再检验剪枝配置复用。

<a id="paper-149102"></a>

## Spectral Alignment in Forward–Backward Representations via Temporal Abstraction

[官方论文页](https://neurips.cc/virtual/2026/poster/149102) · [作者来源](https://openreview.net/forum?id=sslTJpHwTo)

- **问题 / 瓶颈** · 逐步转移下的动态有高频谱分量，低容量表示难捕捉长程结构。
- **核心创新 / 方法** · 分析时间抽象对转移谱的低通作用，控制后继表示有效秩。
- **Baseline** · 单步向前向后表征。
- **Benchmark** · 连续控制下的长程训练及谱分析。
- **关键结果 / 消融** · 摘要报告有效秩下降并有利于长程表示。
- **适用条件 / 局限** · 自举可能受误差限制，摘要未给最优抽象时距。

**可复用机制** · 压缩价值动态前先测试更长的转移单元是否把容量集中到持久行为模式。

<a id="paper-151524"></a>

## Spectral Annealing: Normalization-Path Exploration for Large-Scale Ising Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/151524) · [作者来源](https://openreview.net/forum?id=a138H6V09U)

- **问题 / 瓶颈** · 单一特征问题的离散解质量受选定归一化制约。
- **核心创新 / 方法** · 将参数从原邻接连续移至有符号归一化拉普拉斯。
- **Baseline** · GPU 优化和传统元启发式。
- **Benchmark** · 大规模 Ising 优化，含 840 万变量实例。
- **关键结果 / 消融** · 摘要报告高达 83 倍提速并保持更优解质。
- **适用条件 / 局限** · 依赖结构可谱化，摘要未给跨应用路径设计。

**可复用机制** · 谱松弛结果不稳时，沿有解释的归一化族找候选，评估离散目标而不拘泥一个谱解。

<a id="paper-154061"></a>

## Spectral Degeneration of Softmax Attention under Isotropic Score Geometry

[官方论文页](https://neurips.cc/virtual/2026/poster/154061) · [作者来源](https://openreview.net/forum?id=GUj06j9XU5)

- **问题 / 瓶颈** · 对注意力何以表现为低秩缺少能跨视觉与语言解释的机制。
- **核心创新 / 方法** · 假设分数各向同性并有尖峰与谱体分离，分析逐行 softmax。
- **Baseline** · 视觉和语言预训练注意力矩阵的经验谱。
- **Benchmark** · 统计假设和真实模型诊断。
- **关键结果 / 消融** · 理论显示强方向保留且多数模态压到接近零。
- **适用条件 / 局限** · 依赖所述分数几何，不代表所有位置和任务。

**可复用机制** · 做低秩注意力近似先检查主方向是否支配且谱体在 softmax 后确实被压缩。

<a id="paper-154914"></a>

## Spectral Energy Allocation Enables Source-Free Domain Adaptation in Time Series Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/154914) · [作者来源](https://openreview.net/forum?id=9zd8FaFWpx)

- **问题 / 瓶颈** · 短预测容易得到伪标签，但频域分配与长时距需求不同。
- **核心创新 / 方法** · 从目标域时序内切分学习短预测，调整不同跨度的能量分配。
- **Baseline** · 既有无源域预测适配方法。
- **Benchmark** · 多预测骨干上的无源适配，摘要未列数据。
- **关键结果 / 消融** · 作者报告跨多个骨干显著改善。
- **适用条件 / 局限** · 需要目标序列足够长，摘要未给伪标签误差界。

**可复用机制** · 不能访问源数据时，可用目标时间连续性生成训练信号，再独立修正预测跨度偏差。

<a id="paper-152378"></a>

## Spectral Geometry of Attention: From Information Routing to Uncertainty

[官方论文页](https://neurips.cc/virtual/2026/poster/152378) · [作者来源](https://openreview.net/forum?id=TXNoJp3DRA)

- **问题 / 瓶颈** · 常规欧氏谱把无效吸收与跨 token 信息流相混
- **核心创新 / 方法** · 采用注意分布诱导的概率几何并分析 token 差分算子
- **Baseline** · 概率式置信估计及注意力谱启发式
- **Benchmark** · LLM 不确定性任务，收益尤其见于长摘要
- **关键结果 / 消融** · 摘要报告长摘要受益较多，未给数字
- **适用条件 / 局限** · 机制代理依赖隐藏注意图

**可复用机制** · 判断注意力干预前单独测有效信息传递

<a id="paper-149561"></a>

## Spectral Identifiability for World Models: Polynomial Projectors, Resolvent Stability, and a Krylov Bottleneck

[官方论文页](https://neurips.cc/virtual/2026/poster/149561) · [作者来源](https://openreview.net/forum?id=pByZKc2Y2m)

- **问题 / 瓶颈** · 像素级预测不足以排序控制可靠性
- **核心创新 / 方法** · 分析多时间步预测瓶颈并做谱扰动与生成系统验证
- **Baseline** · 像素预测误差选型及若干生成系统
- **Benchmark** · 线性模拟、组合 OOD 和控制排名
- **关键结果 / 消融** · 生成实验支持谱预测，控制与像素排名可能分离
- **适用条件 / 局限** · 主要保证来自线性或对角结构

**可复用机制** · 给世界模型在同预测误差下做动作扰动和闭环验收

<a id="paper-154057"></a>

## Spectral Insights from the Unconstrained Feature Model for Neural Multi-Output Regression

[官方论文页](https://neurips.cc/virtual/2026/poster/154057) · [作者来源](https://openreview.net/forum?id=GWo2PCEWu8)

- **问题 / 瓶颈** · 统一目标标准化可能改变原单位误差
- **核心创新 / 方法** · 用无约束特征模型解析目标谱，实测带衰减的神经回归
- **Baseline** · 联合输出与分量输出，标准化和不标准化
- **Benchmark** · 机器人模仿和自动驾驶；原尺度 MSE
- **关键结果 / 消融** · 白化作用取决于平均目标方差，实验复现定性趋势
- **适用条件 / 局限** · 简化模型不能替代目标任务测量

**可复用机制** · 动作有不同单位时保留原系统尺度的每轴和总体回归

<a id="paper-148958"></a>

## SpectralKV: Redundancy-Aware KV Cache Compression via Spectral Coreset Selection

[官方论文页](https://neurips.cc/virtual/2026/poster/148958) · [作者来源](https://openreview.net/forum?id=ttixAKQvFd)

- **问题 / 瓶颈** · 均匀层预算加 top-k 保留近重复项
- **核心创新 / 方法** · 跨层分配并以谱核集保留不同几何方向
- **Baseline** · 七个缓存压缩方法
- **Benchmark** · LongBench 15 任务及 PG-19，16K/32K
- **关键结果 / 消融** · 保留 6.25% 时优势最大，静态配置峰值显存最高少 44%
- **适用条件 / 局限** · 收益取决于输入方向可压缩性和核集构造成本

**可复用机制** · 缓存验收同时看去重复和低频证据保留

<a id="paper-153177"></a>

## Spectral Measures of Mamba Conductances Predict and Shape Effective Receptive Fields

[官方论文页](https://neurips.cc/virtual/2026/poster/153177) · [作者来源](https://openreview.net/forum?id=NEc94pojGg)

- **问题 / 瓶颈** · 仅看模型尺寸不能解释长距记忆
- **核心创新 / 方法** · 从 Mamba 离散化构造谱，按距离选择慢快模式
- **Baseline** · 快速模式及其他导通设定
- **Benchmark** · 选择复制，最高 1500 token；单种子延至 4000
- **关键结果 / 消融** · 较慢条件总体 0.68±0.13，快速为 0.34±0.15
- **适用条件 / 局限** · 冻结参数预测与真训练泛化不同，4000 单种子

**可复用机制** · 确定目标记忆距离后消融模式时间常数

<a id="paper-151007"></a>

## Spectral Progressive Diffusion for Efficient Image and Video Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/151007) · [作者来源](https://openreview.net/forum?id=ddRju4BSEw)

- **问题 / 瓶颈** · 早期高频多为噪声，满分辨率浪费算力
- **核心创新 / 方法** · 按功率谱设计分辨率日程，并用谱噪声扩展作阶段衔接
- **Baseline** · 固定分辨率扩散；有无微调
- **Benchmark** · 预训练图像和视频扩散；速度及质量
- **关键结果 / 消融** · 摘要报告显著提速并保持质量，未给幅度
- **适用条件 / 局限** · 频率时序依赖模型与目标内容

**可复用机制** · 生成加速时对照频谱阶段和实际像素质量

<a id="paper-148147"></a>

## Spectral Representations for Provably Robust Offline Meta-Reinforcement Learning from Bagged Rewards

[官方论文页](https://neurips.cc/virtual/2026/poster/148147) · [作者来源](https://openreview.net/forum?id=zvAriUgbiU)

- **问题 / 瓶颈** · 逐步估计目标信息随包长增加而崩塌
- **核心创新 / 方法** · 在无奖励转移上学谱表征，再以包奖励做闭式贝叶斯回归
- **Baseline** · 逐转移上下文离线元 RL
- **Benchmark** · 连续控制元 RL 与单 episode 标量反馈
- **关键结果 / 消融** · 仅 episode 奖励仍能推断任务并取得竞争回报
- **适用条件 / 局限** · 需共享动力学和能重构任务价值的谱表示

**可复用机制** · 长程反馈不应机械摊派每步，同预算比较包级建模

<a id="paper-154946"></a>

## Spectral Stratification of Semantic Abstraction in Vision-Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154946) · [作者来源](https://openreview.net/forum?id=9k4pNHw5Wo)

- **问题 / 瓶颈** · 总嵌入相似同时混合宽分类和细区分
- **核心创新 / 方法** · 截取主成分子空间并比较人类抽象行为
- **Baseline** · 全秩表示及不同谱秩
- **Benchmark** · 多个视觉语言模型和分类层级数据
- **关键结果 / 消融** · 低秩对应广义概念，高阶承载细分，紧凑子空间更贴近人类
- **适用条件 / 局限** · 结论依赖嵌入模型、分类树和评估样本

**可复用机制** · 物体类别定位与近邻实例识别分别试不同谱分解尺度

<a id="paper-154075"></a>

## Spectral Transformer Neural Processes

[官方论文页](https://neurips.cc/virtual/2026/poster/154075) · [作者来源](https://openreview.net/forum?id=GNyLIJGdwZ)

- **问题 / 瓶颈** · 仅按时间接近度匹配会漏远距离同相位样本
- **核心创新 / 方法** · 估上下文频谱并采任务自适应频率特征
- **Baseline** · Transformer Neural Processes 及其他基线
- **Benchmark** · 合成、真实时序和图像预测
- **关键结果 / 消融** · 摘要报告多个任务持续改进，未列幅度
- **适用条件 / 局限** · 短上下文与非平稳序列会降低频谱估计可信度

**可复用机制** · 周期机器人信号测试跨周期同相位和不规则扰动

<a id="paper-152699"></a>

## Spectral Unlearning: Transformer Structure-Preserving Updates for Language Model

[官方论文页](https://neurips.cc/virtual/2026/poster/152699) · [作者来源](https://openreview.net/forum?id=R3Qn4N72Rg)

- **问题 / 瓶颈** · 逐参数更新忽略线性层几何。
- **核心创新 / 方法** · 标准遗忘目标上替换为谱矩阵优化。
- **Baseline** · 既有遗忘目标的默认优化器。
- **Benchmark** · 记忆、隐私和任务效用的调和平均。
- **关键结果 / 消融** · 在线性层输入和输出归一的设定推得精确最陡方向。
- **适用条件 / 局限** · 实际非线性与非归一模块需测。

**可复用机制** · 模型编辑应对比优化几何而非只比遗忘损失。

<a id="paper-150210"></a>

## Speculative Decoding Is Per-Token, Not Path

[官方论文页](https://neurips.cc/virtual/2026/poster/150210) · [作者来源](https://openreview.net/forum?id=jumLplfWH0)

- **问题 / 瓶颈** · 整路径前缀重合可能严重低估收益。
- **核心创新 / 方法** · 推导精确推测接受的逐 token 率与路径重合界。
- **Baseline** · 路径级前缀重合估计。
- **Benchmark** · 理论含独立同分布情形。
- **关键结果 / 消融** · 两者可严格分离且差距无界。
- **适用条件 / 局限** · 墙钟速度另受草稿成本和内核制约。

**可复用机制** · 草稿选型应测逐位置接受行为并换算真实吞吐。

<a id="paper-155356"></a>

## Speculative Self-Distillation enables Efficient Knowledge Internalization

[官方论文页](https://neurips.cc/virtual/2026/poster/155356) · [作者来源](https://openreview.net/forum?id=6DlaA6eBt7)

- **问题 / 瓶颈** · 全交给单教师或单学生成本或分布偏移更大。
- **核心创新 / 方法** · 采用推测式逐 token 混合策略做自蒸馏。
- **Baseline** · 常规自蒸馏策略。
- **Benchmark** · 知识内化，摘要未报告基准细表。
- **关键结果 / 消融** · 摘要提出高效机制，驱动收益待全文核。
- **适用条件 / 局限** · 线上混合规则及额外计算需校验。

**可复用机制** · 让高成本监督集中于最需要教师纠偏的 token。

<a id="paper-149645"></a>

## Speech Tokenizers are Vulnerable:  Transferable Semantic Attack and Robust Tokenizer

[官方论文页](https://neurips.cc/virtual/2026/poster/149645) · [作者来源](https://openreview.net/forum?id=oVx8Urehhw)

- **问题 / 瓶颈** · 编码器的小退化会向 ASR 和语言模型放大。
- **核心创新 / 方法** · 噪声训练结合稳健语义蒸馏。
- **Baseline** · 普通语音 tokenizer。
- **Benchmark** · 语义重构、ASR、音频语言模型。
- **关键结果 / 消融** · 防御改善重构与下游，确数待核。
- **适用条件 / 局限** · 依赖所测噪声和语音域。

**可复用机制** · 语音鲁棒测试应测表征和任务两个接口，及其误差放大。

<a id="paper-151791"></a>

## Speeding up Log-Sum-Exp: Kernel Fusion at the Memory Wall, Integer Arithmetic at the Compute Wall

[官方论文页](https://neurips.cc/virtual/2026/poster/151791) · [作者来源](https://openreview.net/forum?id=Xz4CvAU4eg)

- **问题 / 瓶颈** · 实现瓶颈随硬件不同。
- **核心创新 / 方法** · GPU 单通路融合复用特殊函数单元，CPU 用近似整数算。
- **Baseline** · PyTorch LSE。
- **Benchmark** · 多个硬件和负载规模。
- **关键结果 / 消融** · GPU 小负载 10 至 11 倍，大约 6 倍。
- **适用条件 / 局限** · 近似误差和实际融合需按精度预算核验。

**可复用机制** · 先定位访存还是算术限速再选核优化。

<a id="paper-148614"></a>

## Speed Predictions for Online Energy-Efficient Scheduling

[官方论文页](https://neurips.cc/virtual/2026/poster/148614) · [作者来源](https://openreview.net/forum?id=wSAlwori4a)

- **问题 / 瓶颈** · 预测任务输入未必适合机器速度调节。
- **核心创新 / 方法** · 改为直接预测机器速度。
- **Baseline** · 预测待处理任务的方案。
- **Benchmark** · 在线速度缩放，能耗情况。
- **关键结果 / 消融** · 摘要给新预测模型，量化待核。
- **适用条件 / 局限** · 依赖速度预测误差与代价关系。

**可复用机制** · 资源控制可直接预测动作，而非先预测工作负载再折算。

<a id="paper-151467"></a>

## Spend Only What You Need: Defect-Aware Residual Coverage for Efficient Multi-Agent Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/151467) · [作者来源](https://openreview.net/forum?id=aP2jpM9pME)

- **问题 / 瓶颈** · 固定人数无法根据当前进展控制成本。
- **核心创新 / 方法** · 跟踪不确定、矛盾、验证失败和方面覆盖来做免训练控制。
- **Baseline** · 固定式多代理编排。
- **Benchmark** · 五个推理及多模态套件。
- **关键结果 / 消融** · 摘要报告有评测，幅度待核。
- **适用条件 / 局限** · 缺陷检测需独立校准。

**可复用机制** · 每次代理调用针对一项未解决缺陷，避免重复讨论。

<a id="paper-155259"></a>

## SPERA: Spherical Prior EEG Foundation Model with Geometry- and Frequency-Aware Latent Prediction

[官方论文页](https://neurips.cc/virtual/2026/poster/155259) · [作者来源](https://openreview.net/forum?id=71zbNNbFKV)

- **问题 / 瓶颈** · 同样掩码忽略传感几何。
- **核心创新 / 方法** · 引球面先验并做潜空间预测。
- **Baseline** · 普通 EEG 基础模型。
- **Benchmark** · EEG 几何与频率表征。
- **关键结果 / 消融** · 摘要未报告可概括的结果数值。
- **适用条件 / 局限** · 依赖合理电极位置，别的传感器需验证。

**可复用机制** · 有球面布局的传感器应使用坐标结构做潜预测。

<a id="paper-153724"></a>

## SPEXT: A Decoupled Multi-Spectral Foundation Model for Earth Observation and Vision-Language Grounding

[官方论文页](https://neurips.cc/virtual/2026/poster/153724) · [作者来源](https://openreview.net/forum?id=JFOmDUpPJq)

- **问题 / 瓶颈** · 全局对比监督侵蚀稠密光谱保真。
- **核心创新 / 方法** · 解耦稠密光谱流和语言定位目标。
- **Baseline** · 耦合对比监督的视觉基础模形。
- **Benchmark** · 遥感光谱和语言定位。
- **关键结果 / 消融** · 摘要归因于目标耦合，量化待核。
- **适用条件 / 局限** · 多光谱实证，其他密集任务需复查。

**可复用机制** · 追踪全局对齐是否牺牲低层传感信息。

<a id="paper-151633"></a>

## SphereFlow: Missing Modality Imputation via Geometric Transport on Hypersphere

[官方论文页](https://neurips.cc/virtual/2026/poster/151633) · [作者来源](https://openreview.net/forum?id=Z7Y3gTo3NR)

- **问题 / 瓶颈** · 高维跨模态轨迹可能偏离流形。
- **核心创新 / 方法** · 在单位球上以现有模态为源做输运。
- **Baseline** · 既有缺失补全与满模态 oracle。
- **Benchmark** · BraTS 补全、CT–MRI 转换和下游肿瘤分割。
- **关键结果 / 消融** · 补全逼近满模态分割差距约 80%。
- **适用条件 / 局限** · 偏离界依赖模态相似度。

**可复用机制** · 相近传感器间以真实观测作生成初态稳住路径。

<a id="paper-148342"></a>

## SPHERE-JEPA: Spherical Prediction with Homogeneous Embeddings

[官方论文页](https://neurips.cc/virtual/2026/poster/148342) · [作者来源](https://openreview.net/forum?id=yZ1VgiAJie)

- **问题 / 瓶颈** · 非均匀密度制造各向异性近邻。
- **核心创新 / 方法** · 由流形最坏情形推 kNN 和核岭适宜分布。
- **Baseline** · 高斯表示。
- **Benchmark** · 流形 kNN、球面核岭及 JEPA。
- **关键结果 / 消融** · 相应条件下球均匀最优。
- **适用条件 / 局限** · 最坏情形与现实目标分布可能不同。

**可复用机制** · 嵌入训练先验证所用下游估计器的几何需要。

<a id="paper-152043"></a>

## SphereVAD: Training-Free Video Anomaly Detection via Geodesic Inference on the Unit Hypersphere

[官方论文页](https://neurips.cc/virtual/2026/poster/152043) · [作者来源](https://openreview.net/forum?id=Vx5NOUBXIF)

- **问题 / 瓶颈** · 普通距离不利用单位归一表示的曲率。
- **核心创新 / 方法** · 以 vMF 测地似然比做零样本检测。
- **Baseline** · 免训练及全监督 VAD。
- **Benchmark** · 三个公开视频异常基准。
- **关键结果 / 消融** · 高于既有免训练方法，接近部分监督方案。
- **适用条件 / 局限** · 类别和正常中心分布须重新校准。

**可复用机制** · 冻结表示先测试匹配其几何的统计头。

<a id="paper-150195"></a>

## Spherical Bayesian Experimental Design for Active View Selection in 3D Gaussian Splatting

[官方论文页](https://neurips.cc/virtual/2026/poster/150195) · [作者来源](https://openreview.net/forum?id=k2OeOyeBRk)

- **问题 / 瓶颈** · 选择学全部参数需近似后验且不对应观测。
- **核心创新 / 方法** · 对逐高斯球面外观定义贝叶斯实验设计，闭式后验。
- **Baseline** · 使用全参和 Laplace 近似的方法。
- **Benchmark** · 主动 3DGS、重建与不确定性。
- **关键结果 / 消融** · 多基准重建更好，不确定性更可靠。
- **适用条件 / 局限** · 依赖外观模型和几何估计。

**可复用机制** · 传感器的实际可观察变量应定义信息收益。

<a id="paper-148878"></a>

## Spherical Flows for Sampling Categorical Data

[官方论文页](https://neurips.cc/virtual/2026/poster/148878) · [作者来源](https://openreview.net/forum?id=uVMZotQcJ7)

- **问题 / 瓶颈** · 欧式输运对类别曲率约束处理粗。
- **核心创新 / 方法** · 用 vMF 路径和预测校正采样。
- **Baseline** · 测地及欧式路径。
- **Benchmark** · Sudoku、语言建模。
- **关键结果 / 消融** · 组合显著提高生成结果。
- **适用条件 / 局限** · 依赖类别到球面编码。

**可复用机制** · 对于离散结构对照路径几何和采样积分器的独立效应。

<a id="paper-148719"></a>

## Spherical Interpolation for Backward-Compatible Multimodal Representations

[官方论文页](https://neurips.cc/virtual/2026/poster/148719) · [作者来源](https://openreview.net/forum?id=vYCMLEpje4)

- **问题 / 瓶颈** · 单用对齐新查询可能仍离最优方向远。
- **核心创新 / 方法** · 用球面线性插值，并用局部 margin 认证。
- **Baseline** · 正交对齐单独使用。
- **Benchmark** · 多检索基准和模型，Recall@K。
- **关键结果 / 消融** · 插值持续改善，幅度待核。
- **适用条件 / 局限** · 只在特定几何与局部间隔条件成立。

**可复用机制** · 跨版本上线可先在查询侧混合并保护旧索引。

<a id="paper-155138"></a>

## SphMind: Towards Robust, Training-Free VLM-based Spatial Reasoning with a 360 Camera

[官方论文页](https://neurips.cc/virtual/2026/poster/155138) · [作者来源](https://openreview.net/forum?id=85idnnCtik)

- **问题 / 瓶颈** · 平面模型不能直接理解扭曲和环绕。
- **核心创新 / 方法** · 用球谐结构图及球面等变量表征关系。
- **Baseline** · 普通多模态模型。
- **Benchmark** · 三项全景空间评估。
- **关键结果 / 消融** · 免训练平均改善逾 21.4%。
- **适用条件 / 局限** · 需相机球面模型，真实部署需抗遮挡验证。

**可复用机制** · 保持传感几何后再交给普通语言推理。

<a id="paper-150740"></a>

## SPHQuant: Efficient extreme low bit weight quantization for Vision-Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150740) · [作者来源](https://openreview.net/forum?id=fkP34GiYc2)

- **问题 / 瓶颈** · 旋转改善精度却带来解码成本。
- **核心创新 / 方法** · 以球面编码做仅权重 PTQ。
- **Baseline** · 旋转式与免旋转 2–3 bit 量化。
- **Benchmark** · 视觉语言任务和解码吞吐。
- **关键结果 / 消融** · 性能匹配强方法，吞吐加 30.3%。
- **适用条件 / 局限** · 特定硬件和权重布局需复测。

**可复用机制** · 部署量化按精度和真实解码成本联合选择。

<a id="paper-152294"></a>

## Spikes as Detectors: Phase-Conditioned Spiking Dynamics for Time-Series Anomaly Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/152294) · [作者来源](https://openreview.net/forum?id=U8hMwVUl0r)

- **问题 / 瓶颈** · 仅重构误差漏掉相位不合时的异常。
- **核心创新 / 方法** · 用 LIF 状态及相位条件测异常，亦可与误差融合。
- **Baseline** · 重构误差及匹配 ANN。
- **Benchmark** · 周期和准周期数据，相位可靠性分层。
- **关键结果 / 消融** · 融合稳定超纯误差，强复现段增益最大。
- **适用条件 / 局限** · 弱周期或漂移时相位可能失效。

**可复用机制** · 显式记录相位可信度再决定何时依赖动态状态分数。

<a id="paper-153966"></a>

## SpikeSSL: A Universal Spike Inference Framework with Dynamics-Informed State-Space Layers

[官方论文页](https://neurips.cc/virtual/2026/poster/153966) · [作者来源](https://openreview.net/forum?id=H9vWJVIOyQ)

- **问题 / 瓶颈** · 通用时序回归难适应指示剂和采样率差异。
- **核心创新 / 方法** · 双向 IIR 状态层配合指示剂、采样率及轨迹统计，并以模拟轨迹扩充。
- **Baseline** · 通用时序回归。
- **Benchmark** · 跨指示剂尖峰推断与约 1.1 万条合成轨迹。
- **关键结果 / 消融** · 模拟增强缩小跨条件差距并改善零样本。
- **适用条件 / 局限** · 需要合理的信号仿真，摘要未给各组件增益。

**可复用机制** · 估计隐事件时可用传感器动力学初始化时序结构，再对采样性质显式条件化。

<a id="paper-148673"></a>

## Spike-to-Field Mechanisms of Turbulence-Like Dynamics in Spatial Spiking Neural Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/148673) · [作者来源](https://openreview.net/forum?id=vxPwfztRhd)

- **问题 / 瓶颈** · 放电率、涡旋数或尾部分布单项可能误证动力机制。
- **核心创新 / 方法** · 分别破坏传播延迟、树突滤波或尖峰时序，并比较多个时空症状。
- **Baseline** · 各类破坏对照。
- **Benchmark** · 空间脉冲网络的连续场、相位缺陷和事件尾部。
- **关键结果 / 消融** · 破坏不同动力学环节时主要场特征受到抑制。
- **适用条件 / 局限** · 仅为模型实验，向真实神经或其他系统的迁移未报告。

**可复用机制** · 通过单因素机制破坏检验复杂统计现象，避免把统计拟合当作动力学解释。

<a id="paper-150590"></a>

## SpikingGamma: Temporally Precise Online SNN Training Through Smoothed Temporal Delays

[官方论文页](https://neurips.cc/virtual/2026/poster/150590) · [作者来源](https://openreview.net/forum?id=h3Q9HOiJJg)

- **问题 / 瓶颈** · 细时步对反向穿时昂贵，在线近似在长时序中不稳。
- **核心创新 / 方法** · 维护紧凑平滑延迟组，配合在线训练。
- **Baseline** · BPTT 和 RTRL 类脉冲方法。
- **Benchmark** · 时序脉冲网络任务及不同时间分辨率。
- **关键结果 / 消融** · 摘要报告对时间分辨率稳健。
- **适用条件 / 局限** · 摘要未给硬件实测与泛化边界。

**可复用机制** · 在线学习对快时基敏感时，可把不同延迟写成显式状态，提高局部更新可用性。

<a id="paper-154218"></a>

## Spiking neural network initialization for scale-invariant maximization of entropy

[官方论文页](https://neurips.cc/virtual/2026/poster/154218) · [作者来源](https://openreview.net/forum?id=FKAzoZp21M)

- **问题 / 瓶颈** · 只保持单层激活方差难保证更深层不失活。
- **核心创新 / 方法** · 推导联合时空传播性质的权重和偏置分布。
- **Baseline** · 既有脉冲初始化。
- **Benchmark** · UEA 多变量时序、神经形态分类与连续控制。
- **关键结果 / 消融** · 作者报告各范式均排名第一，未需独立调参。
- **适用条件 / 局限** · 依赖所设神经元动力学。

**可复用机制** · 有阈值和重置的网络应按自身激活动力学初始化，避免直接套用平滑网络规则。

<a id="paper-156130"></a>

## Spin-Weighted Spherical Harmonics Enable Complete and Scalable E(3)-Equivariant Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/156130) · [作者来源](https://openreview.net/forum?id=0AtjGLdzZg)

- **问题 / 瓶颈** · 标量球谐的高效张量运算可能漏掉此类相互作用。
- **核心创新 / 方法** · 以自旋加权球谐恢复反对称通道，保持渐近效率。
- **Baseline** · 原 GTP 等变架构。
- **Benchmark** · 三维原子系统、材料与非中心对称几何。
- **关键结果 / 消融** · 摘要报告高阶等变覆盖更完整。
- **适用条件 / 局限** · 适用边界来自所述代数构造，摘要未给墙钟数值。

**可复用机制** · 做三维等变建模时先审查对称基遗漏的宇称，再决定是否扩大通道数量。

<a id="paper-155523"></a>

## SPIRIT: Speed-Driven Online Adaptation for Self-Speculative Decoding

[官方论文页](https://neurips.cc/virtual/2026/poster/155523) · [作者来源](https://openreview.net/forum?id=4y9wxYdbsM)

- **问题 / 瓶颈** · 接受率类似的配置可能存在不同草稿和验证成本。
- **核心创新 / 方法** · 用窗口运行反馈选择当前配置并保持目标分布。
- **Baseline** · 免训练自推测基线。
- **Benchmark** · 解码吞吐和输出分布一致性。
- **关键结果 / 消融** · 加速最高 1.74 倍。
- **适用条件 / 局限** · 依赖可测稳定吞吐，摘要未给切换成本。

**可复用机制** · 不要用接受率替代整体加速，调节前直接观测草稿与验证的合计成本。

<a id="paper-149531"></a>

## Splatting the Invisible: Geometry and Appearance Scene Completion from Sparse Views

[官方论文页](https://neurips.cc/virtual/2026/poster/149531) · [作者来源](https://openreview.net/forum?id=pSNAnXldPD)

- **问题 / 瓶颈** · 逐视图补全容易失去三维一致性，只补几何又缺少外观。
- **核心创新 / 方法** · 用高斯场 VAE 建稀疏点潜空间，并以双阶段条件流补全。
- **Baseline** · 既有图像补全或几何补全方法。
- **Benchmark** · 多个三维场景数据，衡量几何和外观。
- **关键结果 / 消融** · 报告几何保真改善 33% 至 82%，外观有竞争力。
- **适用条件 / 局限** · 依赖稀疏观测与训练先验，摘要未给域外表现。

**可复用机制** · 必须跨视图一致的缺失部分宜先补在三维公共表征中，再解码各视图。

<a id="paper-155679"></a>

## SPLICE: Structured Prompt Local Iterative Combinatorial Evolution

[官方论文页](https://neurips.cc/virtual/2026/poster/155679) · [作者来源](https://openreview.net/forum?id=3m6Zh7DSNb)

- **问题 / 瓶颈** · 单字符串改写可能误改已经验证的约束和格式。
- **核心创新 / 方法** · 在显式区段上做局部组合式迭代搜索。
- **Baseline** · 单步采样与整体提示重写。
- **Benchmark** · 分类到模型评审细则等任务。
- **关键结果 / 消融** · 原样保留冻结段，跨模型方差小于单步采样。
- **适用条件 / 局限** · 依赖人为或自动正确划分区段。

**可复用机制** · 优化系统提示可将硬约束和可实验变量作为结构化接口处理。

<a id="paper-152305"></a>

## SplineFlow: Flow Matching for Dynamical Systems with B-Spline Interpolants

[官方论文页](https://neurips.cc/virtual/2026/poster/152305) · [作者来源](https://openreview.net/forum?id=U3shszcCi7)

- **问题 / 瓶颈** · 不规则观测下高阶插值可能振荡。
- **核心创新 / 方法** · 流匹配用 B 样条构建跨观测条件路径。
- **Baseline** · 既有流匹配与插值方案。
- **Benchmark** · 动态系统和非均匀采样条件。
- **关键结果 / 消融** · 作者报告高阶动态及不规则采样优势尤其明显。
- **适用条件 / 局限** · 依赖路径平滑性，摘要未给节点布局敏感度。

**可复用机制** · 多时间点监督优先用局部可控的光滑插值，避免修改一个观测扰动全段。

<a id="paper-151356"></a>

## Split and Bridge: Multimodal Generation via Diffusion Bridging

[官方论文页](https://neurips.cc/virtual/2026/poster/151356) · [作者来源](https://openreview.net/forum?id=bABzi3Dcax)

- **问题 / 瓶颈** · 统一潜空间通常需联合重训。
- **核心创新 / 方法** · 在分流点后用桥模块引导各预训练扩散过程。
- **Baseline** · 统一多模态生成方法。
- **Benchmark** · 交错共生成、图像编辑与风格迁移。
- **关键结果 / 消融** · 摘要报告可复用预训练模型且任务可行。
- **适用条件 / 局限** · 桥接训练要求及精确对照未报告。

**可复用机制** · 多模态组合可只共享决定公共结构的阶段，保留模态专用细节处理。

<a id="paper-152641"></a>

## Split-RL: Local Conflict Resolution in Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/152641) · [作者来源](https://openreview.net/forum?id=RUIN0YgMdQ)

- **问题 / 瓶颈** · 全局平均专家和策略梯度会在冲突状态抵消。
- **核心创新 / 方法** · 用指导标签参与树的空间划分，再在叶内进行更新。
- **Baseline** · 普通树拟合及其他离线策略。
- **Benchmark** · 不同规模离线数据的模仿和改进。
- **关键结果 / 消融** · 摘要报告达到近专家表现并优于其他方法。
- **适用条件 / 局限** · 需有可靠的冲突或指导标签，摘要未给更高维对照。

**可复用机制** · 混合监督时在冲突状态内再决定取舍，避免对所有样本施加相同全局权重。

<a id="paper-152147"></a>

## Split the Differences, Pool the Rest: Provably Efficient Multi-Objective Imitation

[官方论文页](https://neurips.cc/virtual/2026/poster/152147) · [作者来源](https://openreview.net/forum?id=VBFoBmDCQY)

- **问题 / 瓶颈** · 独立克隆会浪费可共享的示范。
- **核心创新 / 方法** · 共享一致的状态动作数据，对分歧部分用多输出克隆。
- **Baseline** · 每位专家分开训练。
- **Benchmark** · 多离散环境与连续 LQR。
- **关键结果 / 消融** · 证明更快统计收敛并进行实证。
- **适用条件 / 局限** · 依赖检测一致与冲突样本，连续扩展证据有限。

**可复用机制** · 共享无冲突数据，使每个目标的专门容量只解释真实行为分歧。

<a id="paper-155773"></a>

## Split Then Select: Moment-Preserving Density Control for Generalized Primitive Splatting

[官方论文页](https://neurips.cc/virtual/2026/poster/155773) · [作者来源](https://openreview.net/forum?id=31sxeY9QjS)

- **问题 / 瓶颈** · 先挑原语再强拆可能扰动渲染和损失。
- **核心创新 / 方法** · 匹配局部矩，将原语分成子候选并后续筛选。
- **Baseline** · 传统先选后拆及其他点元渲染。
- **Benchmark** · 多种 splatting，比较图元数、质量和渲染效率。
- **关键结果 / 消融** · 摘要报告更少原语且质量不降。
- **适用条件 / 局限** · 保持至高阶误差，并非任意条件下完全相等。

**可复用机制** · 扩张表示容量前可构造近似函数不变的候选，再交给选择规则。

<a id="paper-148973"></a>

## SplitZip: Ultra Fast Lossless KV Compression for Disaggregated LLM Serving

[官方论文页](https://neurips.cc/virtual/2026/poster/148973) · [作者来源](https://openreview.net/forum?id=tksnxsc1Fc)

- **问题 / 瓶颈** · CPU 或慢编码方法跟不上 KV 生产。
- **核心创新 / 方法** · 用面向 GPU 的无损路径匹配传输实时性。
- **Baseline** · 已有无损权重或 KV 编码。
- **Benchmark** · BF16 和 FP8 KV 及首 token 延迟和请求吞吐。
- **关键结果 / 消融** · 首 token 约快 1.30 倍，吞吐约高 1.23 倍。
- **适用条件 / 局限** · 依赖网络与硬件瓶颈，摘要未给通用开销。

**可复用机制** · 压缩在线状态前同时测编码、传输和解码关键路径。

<a id="paper-139155"></a>

## SpreadsheetBench 2: Evaluating Agents on End-to-End Business Spreadsheet Workflows

[官方论文页](https://neurips.cc/virtual/2026/poster/139155) · [作者来源](https://openreview.net/forum?id=hpl1s8KD4Z)

- **问题 / 瓶颈** · 最终文件错不能区分目标选错与公式写错
- **核心创新 / 方法** · 审计操作轨迹并给阶段失败分类
- **Baseline** · 不同表格智能体，摘要未列名单
- **Benchmark** · SpreadsheetBench 2；总体和调试正确率
- **关键结果 / 消融** · 最强总体 34.89%，调试低至 12.00%，常见失败在检查及目标单元格
- **适用条件 / 局限** · 结论基于商务表格任务

**可复用机制** · 要求智能体验证选定范围再写入，独立记录误改

<a id="paper-154280"></a>

## SpRePE: A Spherical Geometry-Aware Position Embedding scheme for Vision Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/154280) · [作者来源](https://openreview.net/forum?id=F06aHos38r)

- **问题 / 瓶颈** · 平面位置近邻不适合球面拓扑
- **核心创新 / 方法** · 引入球面位置编码并维持 RoPE 同阶开销
- **Baseline** · 既有位置嵌入
- **Benchmark** · 球面图像分类、全景深度、全球天气预测
- **关键结果 / 消融** · 球面几何关键时收益明显，未列幅度
- **适用条件 / 局限** · 取决于输入几何与采样布局

**可复用机制** · 对 360 度传感在缝两侧、极区做单独验证

<a id="paper-150262"></a>

## SPRING: Solver-guided Process Rewards for Novel Logical Reasoning Steps Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/150262) · [作者来源](https://openreview.net/forum?id=jUAayjmSnv)

- **问题 / 瓶颈** · 仅终局奖励不给中间推导反馈
- **核心创新 / 方法** · 以求解器构建过程级奖励
- **Baseline** · 基础 LLM、终局奖励 RL
- **Benchmark** · ZebraLogic、AR-LSAT；谜题正确率和总体分
- **关键结果 / 消融** · ZebraLogic 较终局奖励最高高 15.43 点，AR-LSAT 高 12.14 点
- **适用条件 / 局限** · 要求任务能可靠形式化，过程检查不代表任意任务泛化

**可复用机制** · 可执行推理先对照正确中间命题和仅最终解的奖励

<a id="paper-149697"></a>

## SPRM: From Cooperative Games to Marginal-Contribution Process Reward Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/149697) · [作者来源](https://openreview.net/forum?id=o6rESNXJwW)

- **问题 / 瓶颈** · 把整轨迹结果广播给每步会错归因
- **核心创新 / 方法** · 合作博弈视角估步骤边际贡献并训练过程奖励
- **Baseline** · 人工、rollout、策展和结果广播监督的开放 PRM
- **Benchmark** · ProcessBench、PRMBench、AceMath-RewardBench；首错与 rerank
- **关键结果 / 消融** · 三类评价均改善，未列数值
- **适用条件 / 局限** · 步骤相互依赖且边际效用的估计成本要核实

**可复用机制** · 优先验证高奖励步骤对最终表现的独立贡献

<a id="paper-153943"></a>

## SRA: Spatial Reasoning Adapter via Evolving Social Interaction Graphs for Trajectory Prediction

[官方论文页](https://neurips.cc/virtual/2026/poster/153943) · [作者来源](https://openreview.net/forum?id=HQ4n16Lma3)

- **问题 / 瓶颈** · 在预测前固定邻接会遗漏未来近邻
- **核心创新 / 方法** · 随预测状态更新关系并按不确定性传播消息
- **Baseline** · LED、MID、MoFlow 的不加 SRA 版本
- **Benchmark** · SDD、NBA、Soccer、Football
- **关键结果 / 消融** · 各骨干数据组合都提高，平均 6–7%
- **适用条件 / 局限** · 高置信锚状态仍会出错

**可复用机制** · 多机器人轨迹任务比较固定图与随未来状态更新的图

<a id="paper-139596"></a>

## SR-Prominence: A Crowdsourced Protocol and Dataset Suite for Perceptually-Weighted Super-Resolution Artifact Evaluation

[官方论文页](https://neurips.cc/virtual/2026/poster/139596) · [作者来源](https://openreview.net/forum?id=GJzL4oNx1s)

- **问题 / 瓶颈** · 二值瑕疵指标不能代表明显程度
- **核心创新 / 方法** · 以众包显著性校验局部指标并构造可重用协议
- **Baseline** · DISTS、无参考 IQA 及专项伪影检测
- **Benchmark** · 超分瑕疵数据集，局部显著性，跨参考设置
- **关键结果 / 消融** · DISTS 等标准分较强，若干专用方法迁移差
- **适用条件 / 局限** · 人类评价依赖观看条件和任务

**可复用机制** · 给视觉去噪保留局部感知显著性与像素误差双验收

<a id="paper-154011"></a>

## Stability and Generalization in Looped Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/154011) · [作者来源](https://openreview.net/forum?id=Gs9Aw1utOC)

- **问题 / 瓶颈** · 不稳定动力学会削弱多轮推理泛化
- **核心创新 / 方法** · 对照召回位置，含保留恒等路径的内部召回
- **Baseline** · 不同循环召回结构
- **Benchmark** · 棋、数独、前缀和；单层循环 Transformer
- **关键结果 / 消融** · 性能随理论预测变化，摘要未列量化
- **适用条件 / 局限** · 目前证据主要为单层和受控任务

**可复用机制** · 对重复细化模型监控收敛与跨步梯度，再增加循环次数

<a id="paper-149173"></a>

## Stability-Aware Self-Training for CLIP under Cross-Modal Anchoring Mismatch

[官方论文页](https://neurips.cc/virtual/2026/poster/149173) · [作者来源](https://openreview.net/forum?id=sKdtoMZXRC)

- **问题 / 瓶颈** · 文本类别锚与视觉聚类中心错位。
- **核心创新 / 方法** · 用稳定权重生成图片原型。
- **Baseline** · 一般 CLIP 自训练。
- **Benchmark** · 存在跨模态锚错位的适配。
- **关键结果 / 消融** · 摘要报告稳定性建模提高鲁棒性，幅度未核。
- **适用条件 / 局限** · 稳定错误需另有验证信号。

**可复用机制** · 伪标注应观察多个时间点，不只看单次置信度。

<a id="paper-153846"></a>

## Stability-Constrained Regime-Aware Forecasting for Heterogeneous Panel Time Series

[官方论文页](https://neurips.cc/virtual/2026/poster/153846) · [作者来源](https://openreview.net/forum?id=IJ0jP4TvfO)

- **问题 / 瓶颈** · 池化抵消异号信号，单专家谱归一无法保证系统收缩。
- **核心创新 / 方法** · 诊断模式反向效应并惩罚门控分歧。
- **Baseline** · 池化加法和局部谱归一。
- **Benchmark** · 151 国面板与合成压力测试。
- **关键结果 / 消融** · 尾部恢复信号，DM p=0.016；强模式反差下需分歧罚。
- **适用条件 / 局限** · 实证面板非目标任务，收缩界依赖门系数。

**可复用机制** · 混合动态应单测路由贡献的全局稳定性。

<a id="paper-152554"></a>

## Stability-Enhanced Federated Learning with Accelerated Gradient

[官方论文页](https://neurips.cc/virtual/2026/poster/152554) · [作者来源](https://openreview.net/forum?id=SFp0bLpWTb)

- **问题 / 瓶颈** · 普通动量提速未提高稳定。
- **核心创新 / 方法** · 结合全局动量和梯度差校正 NAG 与混合近端项。
- **Baseline** · 多种动量联邦方案。
- **Benchmark** · 非 IID 理论及多个真实集。
- **关键结果 / 消融** · 稳定界改善，收敛更快。
- **适用条件 / 局限** · 收益受异质性和本地步数影响。

**可复用机制** · 以稳定性而非仅训练损失评估加速更新。

<a id="paper-151921"></a>

## Stability in Multi-Step Reasoning via Jacobian-based Error Accumulation Analysis

[官方论文页](https://neurips.cc/virtual/2026/poster/151921) · [作者来源](https://openreview.net/forum?id=WtBpkiw90s)

- **问题 / 瓶颈** · 每步的输入敏感性使错误复合。
- **核心创新 / 方法** · 压缩 CoT，量化感知训练正则输入雅可比。
- **Baseline** · 普通推理训练。
- **Benchmark** · 七任务、长度外推。
- **关键结果 / 消融** · 平均加 3.5%，长度泛化加 8.2%。
- **适用条件 / 局限** · 量化感知效应依赖训练设置。

**可复用机制** · 分别控制轨迹长度和每步扰动放大。

<a id="paper-149842"></a>

## Stability Regimes for Framing-Sensitive Fine-Tuning in Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149842) · [作者来源](https://openreview.net/forum?id=mt2diEh4OH)

- **问题 / 瓶颈** · 微小表述偏差经反馈会积累。
- **核心创新 / 方法** · 用五类受控呈现和人评构造配对主张。
- **Baseline** · 不同呈现及反馈对照。
- **Benchmark** · FrameRef 和序列暴露任务。
- **关键结果 / 消融** · 单步小偏移在反馈下累积成较大差异。
- **适用条件 / 局限** · 人评及呈现类型有文化依赖。

**可复用机制** · 代理研究应同时测单次和反馈环中的敏感性。

<a id="paper-155837"></a>

## Stability-Weighted Direction Regularization Disentangles Generator Shortcuts from Detection Signal

[官方论文页](https://neurips.cc/virtual/2026/poster/155837) · [作者来源](https://openreview.net/forum?id=2VpqRkpXM9)

- **问题 / 瓶颈** · 删除模型源可分方向会一并删真伪证据。
- **核心创新 / 方法** · LDA 方向按跨源稳定性打分，只罚不稳者。
- **Baseline** · ERM、EFFORT 和硬投影去方向。
- **Benchmark** · 四分布外生成器的 AUC 和方差。
- **关键结果 / 消融** · ResNet-50 平均 AUC 方差尺度显著收紧，CLIP 相比 ERM 加 1.7 点。
- **适用条件 / 局限** · 依赖训练生成器覆盖真实变化。

**可复用机制** · 不要按域可识别性一刀切删特征，先测跨域符号稳定。

<a id="paper-152714"></a>

## Stabilizing Extrapolation in Looped Transformers via Learned Stochastic Stopping

[官方论文页](https://neurips.cc/virtual/2026/poster/152714) · [作者来源](https://openreview.net/forum?id=Qv0Lwp7s5A)

- **问题 / 瓶颈** · 确定迭代次数易在外推中震荡。
- **核心创新 / 方法** · 用 RL 学随机停止，并对照启发采样。
- **Baseline** · 固定和启发迭代。
- **Benchmark** · 二进制加法、Dyck-1、Unique Set、Copy。
- **关键结果 / 消融** · 常改善正确率稳定权衡，也能稳定次优计算。
- **适用条件 / 局限** · 停止稳定不保证算对。

**可复用机制** · 同时评价答案、停止分布和新长度泛化。

<a id="paper-149495"></a>

## Stabilizing Few-Shot Object Detection with Language-Conditioned Probabilistic Prototypes

[官方论文页](https://neurips.cc/virtual/2026/poster/149495) · [作者来源](https://openreview.net/forum?id=pi6vqZBaUT)

- **问题 / 瓶颈** · 一两张异常支持图会主导类别。
- **核心创新 / 方法** · 语言查询作锚，异方差高斯降权，部件级对齐。
- **Baseline** · FPD。
- **Benchmark** · PASCAL VOC、MS-COCO。
- **关键结果 / 消融** · VOC Split 2 一样本 nAP50 加 3.9 点。
- **适用条件 / 局限** · 语言及部件知识受类别覆盖影响。

**可复用机制** · 少样本适配时传播支持样本可靠性而非平均。

<a id="paper-151790"></a>

## Stabilizing Knowledge, Promoting Reasoning: Dual-Token Constraints for RLVR

[官方论文页](https://neurips.cc/virtual/2026/poster/151790) · [作者来源](https://openreview.net/forum?id=XzRoRbdbXp)

- **问题 / 瓶颈** · 硬冻结或异步训练隔断联合更新。
- **核心创新 / 方法** · 响应级熵归一化，按类型独立 clipping 和 KL。
- **Baseline** · 隔离更新和常规 RLVR。
- **Benchmark** · 数学与代码。
- **关键结果 / 消融** · 摘要报告实验改善，幅度待核。
- **适用条件 / 局限** · 熵只是角色代理，校准错误会影响知识。

**可复用机制** · 共享一个策略但为不同 token 分配不同偏移预算。

<a id="paper-149900"></a>

## Stabilizing Off-policy LLM Optimization with Prefix Importance Ratio

[官方论文页](https://neurips.cc/virtual/2026/poster/149900) · [作者来源](https://openreview.net/forum?id=mN7OOSKVlg)

- **问题 / 瓶颈** · 单词比值不含前文采样偏移。
- **核心创新 / 方法** · 用最小前缀比构造稳健目标。
- **Baseline** · token 级重要性比。
- **Benchmark** · 离策略 LLM 后训练。
- **关键结果 / 消融** · 理论指出前缀为严格校正项，实证幅度待核。
- **适用条件 / 局限** · 乘积比例易失稳，需数值检查。

**可复用机制** · 在更新前明确轨迹何处发生分布失配。

<a id="paper-148304"></a>

## Stabilizing Policy Optimization via Logits Convexity

[官方论文页](https://neurips.cc/virtual/2026/poster/148304) · [作者来源](https://openreview.net/forum?id=yppWn8zxqm)

- **问题 / 瓶颈** · RL 梯度可能不具 SFT 的有利方向。
- **核心创新 / 方法** · 从原 RL 目标导最佳目标策略，再拟合模拟 logits 凸性。
- **Baseline** · 常规策略优化。
- **Benchmark** · 多个语言模型家族。
- **关键结果 / 消融** · 摘要称训练更稳和表现更强。
- **适用条件 / 局限** · 最优目标近似决定实现。

**可复用机制** · 若可先计算策略目标，宜单测凸拟合的稳定收益。

<a id="paper-153095"></a>

## Stabilizing RL+Search for Imperfect-Information Extensive-Form Games

[官方论文页](https://neurips.cc/virtual/2026/poster/153095) · [作者来源](https://openreview.net/forum?id=NzsjoeFQ45)

- **问题 / 瓶颈** · 固定步数使递归目标方差按深度平方增长。
- **核心创新 / 方法** · 在期望预算附近高斯随机 CFR 总步数。
- **Baseline** · 固定步数 ReBeL。
- **Benchmark** · 不完全信息扩展式游戏。
- **关键结果 / 消融** · 保线性 CFR 收敛阶，递归方差从二次到线性。
- **适用条件 / 局限** · 依赖变差界及 CFR 设定。

**可复用机制** · 递归规划用随机深度打散系统误差，再测预算分布。

<a id="paper-148261"></a>

## Stabilizing the Dynamic Low-Rank Training

[官方论文页](https://neurips.cc/virtual/2026/poster/148261) · [作者来源](https://openreview.net/forum?id=zAGUzDSLhh)

- **问题 / 瓶颈** · 强压缩下未来梯度需要已删方向。
- **核心创新 / 方法** · 回注主要被忽略奇异方向，并对截断阈值负反馈。
- **Baseline** · DLRT 和 LoRA。
- **Benchmark** · 训练压缩及 DeBERTa-v3 SuperGLUE。
- **关键结果 / 消融** · 高压缩下可训，PEFT 参数对 LoRA 多 2.8%。
- **适用条件 / 局限** · 缓冲计算成本与秩动态须实测。

**可复用机制** · 低秩容量不只调目标秩，也保留短期可恢复方向。

<a id="paper-154907"></a>

## Stable3R: Streaming 3D Reconstruction with Stable Geometric References

[官方论文页](https://neurips.cc/virtual/2026/poster/154907) · [作者来源](https://openreview.net/forum?id=A2C5edhRjI)

- **问题 / 瓶颈** · 早期缓存不充分，首帧偏差持续积累。
- **核心创新 / 方法** · 刷新历史缓存并用前缀几何约束姿态。
- **Baseline** · 首帧锚的因果 KV 重建。
- **Benchmark** · 多个流式重建基准。
- **关键结果 / 消融** · 摘要报告改善，幅度未核。
- **适用条件 / 局限** · 上线可允许的缓存延迟需核。

**可复用机制** · 关键参照采用可修订的证据窗口，避免固定错误。

<a id="paper-154677"></a>

## STABLE: A Continual Learning Optimizer with Adaptive Drift Control

[官方论文页](https://neurips.cc/virtual/2026/poster/154677) · [作者来源](https://openreview.net/forum?id=Br2ANAj8hi)

- **问题 / 瓶颈** · 固定正则难兼顾可塑和稳定。
- **核心创新 / 方法** · 原始对偶漂移控制，并分析局部得分稳定时的边界侵蚀。
- **Baseline** · 普通 PEFT 及专用持续学习。
- **Benchmark** · 长期单模态与 CLIP 多模态流。
- **关键结果 / 消融** · 简单 PEFT 加优化器持平或超过专法。
- **适用条件 / 局限** · 理论依赖距离分类及局部稳定条件。

**可复用机制** · 基于可测间隔动态控制更新预算。

<a id="paper-153504"></a>

## Stable and Granular Policy Optimization for Generative Recommendation

[官方论文页](https://neurips.cc/virtual/2026/poster/153504) · [作者来源](https://openreview.net/forum?id=KqTAFaifPA)

- **问题 / 瓶颈** · 序列指标无法说明哪个生成决策改善排序。
- **核心创新 / 方法** · 组策略优化同时处理稳定性与粒度。
- **Baseline** · 六种 RL 推荐基线。
- **Benchmark** · 两个公开基准及商业在线 A/B。
- **关键结果 / 消融** · CTR 加 2.36%，广告收入加 1.95%。
- **适用条件 / 局限** · 推荐评价和部署回报未必可转目标排序。

**可复用机制** · 对序列目标比较细粒更新和全序列奖励的各自效果。

<a id="paper-150122"></a>

## Stable and Scalable Probabilistic Numerical Solvers for Stiff and High-Dimensional ODEs

[官方论文页](https://neurips.cc/virtual/2026/poster/150122) · [作者来源](https://openreview.net/forum?id=kWEGM5zPCL)

- **问题 / 瓶颈** · 既有近似在高维刚系统失稳。
- **核心创新 / 方法** · 迭代重线性化使求解器全隐式。
- **Baseline** · 现有概率求解器。
- **Benchmark** · 刚性和高维数值问题。
- **关键结果 / 消融** · 稳定性与规模性改善。
- **适用条件 / 局限** · 需比较迭代停止及梯度代价。

**可复用机制** · 生成动力学出现刚性时应评估重线性化，而非只减步长。

<a id="paper-154759"></a>

## StableAvatar: Ultra-Long Audio-Driven Avatar Video Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/154759) · [作者来源](https://openreview.net/forum?id=BAov2t06Vm)

- **问题 / 瓶颈** · 固定外部编码误差会累积。
- **核心创新 / 方法** · 时间步适配、模型原生音频引导及滑窗融合。
- **Baseline** · 常规外部音频交叉注意。
- **Benchmark** · 长音频头像视频，同步和连续性。
- **关键结果 / 消融** · 摘要报告改善，幅度未核。
- **适用条件 / 局限** · 实证集中在头像，窗口边缘和语音域需验。

**可复用机制** · 长片段多模态生成把条件校准与滑窗一致性分开。

<a id="paper-157019"></a>

## Stable Continuous-Time Consistency Distillation: An Empirical Study with a Multistep Extension

[官方论文页](https://neurips.cc/virtual/2026/poster/157019) · [作者来源](https://openreview.net/forum?id=di6ofoWEU8)

- **问题 / 瓶颈** · 单步目标扩展多步可能难稳。
- **核心创新 / 方法** · 在 sCD 上加段条件的多步推广。
- **Baseline** · TrigFlow/sCM 框架及单步 sCD。
- **Benchmark** · 连续时间一致性稳定与多步生成。
- **关键结果 / 消融** · 摘要提出并考察多步，幅度待核。
- **适用条件 / 局限** · 需验证各段误差积累及统一预算。

**可复用机制** · 多步蒸馏按段约束误差传播，单测步数与质量。

<a id="paper-150233"></a>

## Stable GFlowNets with Probabilistic Guarantees

[官方论文页](https://neurips.cc/virtual/2026/poster/150233) · [作者来源](https://openreview.net/forum?id=jnP3JrG3BL)

- **问题 / 瓶颈** · 高分布质量不保证训练损失足够受控，有限优化难判断。
- **核心创新 / 方法** · 用损失到总变差的界分析保真度，并以自适应参考流稳定训练。
- **Baseline** · 普通轨迹平衡训练。
- **Benchmark** · 模式覆盖、鲁棒性及可认证性。
- **关键结果 / 消融** · 作者报告折中改善，并在有界轨迹损失条件下给出保证。
- **适用条件 / 局限** · 界依赖损失受控，摘要未给任务与数值。

**可复用机制** · 采样模型在追求覆盖多模态时，可以将训练量转化为明确的分布偏差证书。

<a id="paper-155198"></a>

## StableHand: Quality-Aware Flow Matching for World-Space Dual-Hand Motion Estimation from Egocentric Video

[官方论文页](https://neurips.cc/virtual/2026/poster/155198) · [作者来源](https://openreview.net/forum?id=7Yxqeh6UZi)

- **问题 / 瓶颈** · 统一使用噪声帧会把遮挡证据当作同样可信。
- **核心创新 / 方法** · 把每帧手观测质量分解并接入流匹配。
- **Baseline** · 统一处理时序条件的最强对照。
- **Benchmark** · 第一视角手运动含 ARCTIC 高遮挡序列，W-MPJPE。
- **关键结果 / 消融** · W-MPJPE 下降约 20% 至 25%。
- **适用条件 / 局限** · 依赖对观测质量的估计，摘要未给跨传感器验证。

**可复用机制** · 长序列生成补全应保存观测质量，让低可信段更多依赖时序先验。

<a id="paper-154652"></a>

## Stable Long-Horizon PDE Forecasting via Latent Structured Spectral Propagators

[官方论文页](https://neurips.cc/virtual/2026/poster/154652) · [作者来源](https://openreview.net/forum?id=C20RzfkyzY)

- **问题 / 瓶颈** · 直接滚动物理场会累积不稳定细尺度误差。
- **核心创新 / 方法** · 将 PDE 场放入时间一致空间，再用结构化谱算子传播紧凑状态。
- **Baseline** · 先进时序场预测。
- **Benchmark** · PDE 长程预测及超训练时间外推，使用相对 L2。
- **关键结果 / 消融** · 相对 L2 最多下降 48.9%，外推更稳定。
- **适用条件 / 局限** · 依赖谱传播适配性，摘要未给异常动力系统范围。

**可复用机制** · 预测器可拆为稳定的递归动态核心与高保真细节恢复模块。

<a id="paper-156002"></a>

## Stable Max Coverage Under a Cardinality Constraint

[官方论文页](https://neurips.cc/virtual/2026/poster/156002) · [作者来源](https://openreview.net/forum?id=1FegBT41mH)

- **问题 / 瓶颈** · 只优化期望覆盖可能得出极脆弱的选集。
- **核心创新 / 方法** · 以正则化目标加相关采样平衡敏感性和覆盖。
- **Baseline** · 标准最大覆盖。
- **Benchmark** · 合成与真实覆盖实例，比较效用与敏感度。
- **关键结果 / 消融** · 近似因子 1−1/e，另有大小随正则变化的加性项。
- **适用条件 / 局限** · 保证限给定基数和目标，摘要未给经验参数。

**可复用机制** · 当部署更重视选集稳定性时，将覆盖损失与允许的离散方案变化共同管理。

<a id="paper-148586"></a>

## Stable Partial Order Constraints for Temporal Causal Structure Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/148586) · [作者来源](https://openreview.net/forum?id=wgAOX8Wvbf)

- **问题 / 瓶颈** · 不同滞后造成变量级循环，静态约束会让循环游走累积。
- **核心创新 / 方法** · 用时间结构与归一化摘要表达高阶可达性。
- **Baseline** · 静态可微偏序约束。
- **Benchmark** · 时序结构学习及非平稳设置。
- **关键结果 / 消融** · 摘要报告非平稳条件下有效。
- **适用条件 / 局限** · 依赖预设可用偏序，摘要未给量化恢复增益。

**可复用机制** · 约束因果顺序前应区分瞬时边与跨时边，避免将合法反馈当作违规。

<a id="paper-152770"></a>

## Stable Resolution-Invariant Emulation in Entropically Controlled Kinetic Methods

[官方论文页](https://neurips.cc/virtual/2026/poster/152770) · [作者来源](https://openreview.net/forum?id=QVYzAlckz5)

- **问题 / 瓶颈** · 粗化会丢失耗散通道并引入混叠噪声。
- **核心创新 / 方法** · 对动力学神经求解器控制熵动态。
- **Baseline** · 生成数据用的稳定数值求解方法。
- **Benchmark** · 粗分辨率的动力模拟稳定性。
- **关键结果 / 消融** · 摘要称粗网格的稳定性超过参考数值求解器。
- **适用条件 / 局限** · 需要可定义耗散量，摘要未给非动力学问题范围。

**可复用机制** · 低分辨率学代理最好补回被分辨率截断的物理机制，而不是仅拟合短期误差。

<a id="paper-151809"></a>

## StableVQ: Practical Guidelines for Stable Vector-Quantized Tokenizer Training

[官方论文页](https://neurips.cc/virtual/2026/poster/151809) · [作者来源](https://openreview.net/forum?id=XrO6sGUEHB)

- **问题 / 瓶颈** · 两模块相互补救时对初始化和码本规模敏感。
- **核心创新 / 方法** · StableVQ 对各模块学习目标单独改造。
- **Baseline** · 普通 VQ 分词训练。
- **Benchmark** · ImageNet，不同码本大小和初始化，考察利用率与重建。
- **关键结果 / 消融** · 摘要报告训练更稳定，码本利用和重建改善。
- **适用条件 / 局限** · 摘要未给跨图像外模态或下游生成增益。

**可复用机制** · 分模块量化训练时，单独测试编码质量与码本健康度，避免二者指标互相掩盖。

<a id="paper-148748"></a>

## STAC-R: Subspace-Tracked Activation Compression with Residuals

[官方论文页](https://neurips.cc/virtual/2026/poster/148748) · [作者来源](https://openreview.net/forum?id=vM3HWhzSRT)

- **问题 / 瓶颈** · 只压缩单个张量的尺寸无法保证整体峰值显存降低。
- **核心创新 / 方法** · 跟踪子空间，直接收缩因子对应的权重梯度，并以统计量预测可减内存。
- **Baseline** · 全量保存及停留在重建的压缩路径。
- **Benchmark** · 含 Qwen-2.5 和 Llama-3.2 的训练内存配置。
- **关键结果 / 消融** · 摘要指出部分 SwiGLU 配置会增加显存。
- **适用条件 / 局限** · 层结构影响峰值，摘要未给大规模吞吐。

**可复用机制** · 先估计压缩在哪些张量生命周期能减少峰值，再判断是否启用。

<a id="paper-149420"></a>

## StaDy: Factorizing the World into Static and Dynamic via Likelihood Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/149420) · [作者来源](https://openreview.net/forum?id=qBH3DcGnNL)

- **问题 / 瓶颈** · 强压缩同时破坏真正复杂的动态；弱压缩可能允许静态信息泄漏。
- **核心创新 / 方法** · 匹配仅给潜变量的预测与无条件预测。
- **Baseline** · 以窄瓶颈分离静态和动态的方案。
- **Benchmark** · 世界建模及不同动态潜空间维度。
- **关键结果 / 消融** · 摘要报告维数增加仍减少静态泄漏并改善复杂动力表示。
- **适用条件 / 局限** · 依赖训练可评估条件与无条件输出，摘要未给重建开销。

**可复用机制** · 要解耦表示，可限制变量独自可解释的信息，而非简单限制变量总容量。

<a id="paper-149801"></a>

## Stage-Aware Dual Alignment for Covariate Shift in Graph Domain Adaptation

[官方论文页](https://neurips.cc/virtual/2026/poster/149801) · [作者来源](https://openreview.net/forum?id=nFn17qZZSS)

- **问题 / 瓶颈** · 特征分布和依特征条件的边结构不同，单阶段对齐遗漏其一。
- **核心创新 / 方法** · 输入用对抗对齐，消息传递逐层重加权。
- **Baseline** · 既有图域适配及单阶段对齐。
- **Benchmark** · 合成和真实图基准，含耦合偏移。
- **关键结果 / 消融** · 摘要报告跨设置优于旧方法，耦合时尤其明显。
- **适用条件 / 局限** · 需稳健估计结构偏移，摘要未给动态更新成本。

**可复用机制** · 先定位偏移进入图模型的阶段，再对该阶段修正，不只对齐最终嵌入。

<a id="paper-139841"></a>

## StaminaBench: Stress-Testing Coding Agents over 100 Interaction Turns

[官方论文页](https://neurips.cc/virtual/2026/poster/139841) · [作者来源](https://openreview.net/forum?id=1IMrtjWVBs)

- **问题 / 瓶颈** · 短任务无法判断错误随迭代或因框架而增。
- **核心创新 / 方法** · 通过程序生成测试和结构化修改，隔离运行并测长期完成。
- **Baseline** · 不同模型和代理框架。
- **Benchmark** · 100 轮交互与最长约 6000 行的累积代码。
- **关键结果 / 消融** · 摘要报告强模型随框架表现变动，弱模型各框架失败。
- **适用条件 / 局限** · 修改空间人工约束，未覆盖任意真实需求。

**可复用机制** · 同一长程任务用多个代理执行环境跑对照，区分模型不足与框架造成的积累失败。

<a id="paper-150310"></a>

## Standing on the Shoulders of Giants: Rethinking EEG Foundation Model Pretraining via Multi-Teacher Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/150310) · [作者来源](https://openreview.net/forum?id=j4s4yXToW0)

- **问题 / 瓶颈** · 单模态重建可能低效利用已有通用表征。
- **核心创新 / 方法** · 用多位成熟基础模型给 EEG 学生提供表征监督。
- **Baseline** · 独立的脑电自监督预训练。
- **Benchmark** · EEG 下游与缩减预训练数据。
- **关键结果 / 消融** · 摘要报告一致超过自监督，只有 25% 数据仍有竞争力。
- **适用条件 / 局限** · 摘要未给各教师独立贡献与其他低资源传感迁移。

**可复用机制** · 低资源信号可先验证时间或空间结构相似的其他模态教师，再决定是否训练单模态底座。

<a id="paper-148439"></a>

## STAPO: Stabilizing Reinforcement Learning for LLMs by Silencing Rare Spurious Tokens

[官方论文页](https://neurips.cc/virtual/2026/poster/148439) · [作者来源](https://openreview.net/forum?id=xnL7HqJSHm)

- **问题 / 瓶颈** · 少数与推理结果关联低的位置继承全序列奖励，引发熵不稳定。
- **核心创新 / 方法** · 联合分析伪相关风险、梯度范数和熵，对可疑位置抑制更新。
- **Baseline** · GRPO、20-Entropy、JustRL。
- **Benchmark** · 两种标准设置，考察推理准确率和训练熵。
- **关键结果 / 消融** · 摘要称异常 token 约 0.01%，抑制后稳定性和平均准确率更好。
- **适用条件 / 局限** · 需正确识别无价值 token，摘要未给假阳性影响。

**可复用机制** · 强化训练的异常可集中在极少更新位置，应该检查 token 级贡献而非只调序列剪切。

<a id="paper-153469"></a>

## STARFlow2: Bridging Language Models and Normalizing Flows for Unified Multimodal Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/153469) · [作者来源](https://openreview.net/forum?id=L7AuyR68b3)

- **问题 / 瓶颈** · 非因果迭代去噪与左到右缓存衔接困难
- **核心创新 / 方法** · 结合自回归流和语言骨干，图文输出无需重新编码即可入 KV
- **Baseline** · 常见语言加扩散的多模态架构
- **Benchmark** · 图像生成和多模态理解，细目未列
- **关键结果 / 消融** · 摘要报告较强表现及原生缓存复用
- **适用条件 / 局限** · 架构和视觉 latent 必须匹配，实测缓存收益未列

**可复用机制** · 统一生成选型同时测跨模态交接开销

<a id="paper-148796"></a>

## StarWM:  Self-Supervised Trained Attention Routing for Robust World Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148796) · [作者来源](https://openreview.net/forum?id=v2NzTOEOfM)

- **问题 / 瓶颈** · 按像素面积分配表征会为大块干扰耗容量
- **核心创新 / 方法** · 以自监督门控跨注意路由，使相关状态进入想象
- **Baseline** · 重建型及同期无重建方法
- **Benchmark** · DeepMind Control，清洁、连续视频及随机视频背景
- **关键结果 / 消融** · 三场景稳定，并在长时想象保留关键属性
- **适用条件 / 局限** · 证据来自受控背景，真实遮挡须重估

**可复用机制** · 分别核验拟合背景和保留任务变量的程度

<a id="paper-149218"></a>

## State Augmented Flows

[官方论文页](https://neurips.cc/virtual/2026/poster/149218) · [作者来源](https://openreview.net/forum?id=s0ZcT4SvLA)

- **问题 / 瓶颈** · 数据空间投影相同时不同轨迹可能有相反速度
- **核心创新 / 方法** · 给速度网络扩展状态但不改最终样本空间
- **Baseline** · rectified flow 基线
- **Benchmark** · MNIST、CIFAR-10、ImageNet-32；不同 NFE
- **关键结果 / 消融** · 各项改善，低 NFE 收益最大
- **适用条件 / 局限** · 高维增量的计算与走势要匹配网络

**可复用机制** · 同预算比较附加状态和多步采样

<a id="paper-153030"></a>

## State Copying Crowds Out Reasoning: Mechanistic Evidence for Delta Planning in Autoregressive Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153030) · [作者来源](https://openreview.net/forum?id=OXm9qcC6FZ)

- **问题 / 瓶颈** · 逐步复制高熵全状态会干扰推理
- **核心创新 / 方法** · 对比全状态生成、等长控制及复杂复制，再以残差式草稿更新状态
- **Baseline** · Full-State Generation 及等长控制
- **Benchmark** · Formal Math 2000 token、SWE-bench Lite
- **关键结果 / 消融** · 数学 41.2–68.5% 到 97.1–99.4%，SWE 也提升
- **适用条件 / 局限** · 长依赖距离仍降准确，需可靠状态管理

**可复用机制** · 对持久任务让程序保留状态，要求模型写更新和下一动作

<a id="paper-151469"></a>

## StateLedger: Path-Addressed External Memory for Persistent Multi-Agent Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/151469) · [作者来源](https://openreview.net/forum?id=aNVVPOAxzx)

- **问题 / 瓶颈** · 可检索片段无法直接表达谁覆盖了谁
- **核心创新 / 方法** · 用路径更新存状态，变更日志和检查点存历史并去重证据
- **Baseline** · 其他长程 Agent 记忆
- **Benchmark** · LongMemEval、LoCoMo、Evo-Memory；准确率与存储
- **关键结果 / 消融** · LongMemEval-S 98.8%，LongMemEval-M 82.6% 且持久存储为参考的 14.7%
- **适用条件 / 局限** · 保证依赖覆盖与读取一致性

**可复用机制** · 承载偏好或环境变量的记忆应显式保留版本和来源

<a id="paper-148318"></a>

## State-Resolving Attention for Length-Extrapolating Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/148318) · [作者来源](https://openreview.net/forum?id=yhRk81TgYO)

- **问题 / 瓶颈** · 相关性检索不区分已被更新的历史
- **核心创新 / 方法** · 状态解析注意先筛内容，再按时序找有效记录
- **Baseline** · 普通 Transformer
- **Benchmark** · 重复关联回忆、复制、长上下文及预训练
- **关键结果 / 消融** · 外推明显优于训练长度，摘要未给数值
- **适用条件 / 局限** · 更新顺序或版本规则可能比简单时间复杂

**可复用机制** · 为记忆评测加入重复赋值及撤销旧偏好

<a id="paper-151920"></a>

## StateTree: Enhancing Long-term Dialogue Reasoning via Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151920) · [作者来源](https://openreview.net/forum?id=Wtmbj6bI9C)

- **问题 / 瓶颈** · 真实长会话稀缺且全长 RL 贵
- **核心创新 / 方法** · 用多会话构造路径追踪、自带真值的 RL 代理任务
- **Baseline** · SFT、RL 方法与 QwenLong-L1-32B
- **Benchmark** · 128K LongMemEval、短上下文与跨会话能力
- **关键结果 / 消融** · 14B 为 59.0%，32B 对照 45.2%
- **适用条件 / 局限** · 代理树结构与实际对话演变可能不同

**可复用机制** · 比较从短历史训练中学出的更新、检索和跨会话规划

<a id="paper-149986"></a>

## Static-Dynamic Disentanglement for Efficient Multi-Frame Vision-Language-Action Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149986) · [作者来源](https://openreview.net/forum?id=lhhOfpsgc5)

- **问题 / 瓶颈** · 重复固定背景花算力又缩短动态上下文
- **核心创新 / 方法** · 按多层静态与动态表示拆分视频帧，再进行条件控制
- **Baseline** · 原 VLA 和多帧基线，名称未报告
- **Benchmark** · 多帧融合、仿真、实机常规及依赖记忆任务
- **关键结果 / 消融** · 实机依赖记忆成功率高 23.3 个百分点，实机一般快 2.2 倍
- **适用条件 / 局限** · 静止物体的小变化可能对动作关键

**可复用机制** · 同时验收加速、稀有运动识别和依赖历史的任务
