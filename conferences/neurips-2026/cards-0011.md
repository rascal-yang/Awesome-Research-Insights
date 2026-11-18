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
