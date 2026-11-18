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
