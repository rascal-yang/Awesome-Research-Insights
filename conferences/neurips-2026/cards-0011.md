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

<a id="paper-148477"></a>

## Statistical Estimation of Adversarial Risk in Large Language Models under Best-of-N Sampling

[官方论文页](https://neurips.cc/virtual/2026/poster/148477) · [作者来源](https://openreview.net/forum?id=xW6XygNVrF)

- **问题 / 瓶颈** · 单轮结果低估累计不安全输出概率。
- **核心创新 / 方法** · 用统计风险曲线校准不同预算下的防御。
- **Baseline** · 单次和低预算安全评估。
- **Benchmark** · 大模型防御评测，不同尝试预算。
- **关键结果 / 消融** · 安全性相近时风险曲线仍可显著不同。
- **适用条件 / 局限** · 依赖所抽测试场景，概率估计需区间。

**可复用机制** · 上线前同时设置会话预算和相应的安全验收阈值。

<a id="paper-152254"></a>

## Statistical Inference in Causal Partial Identification under Smooth Densities

[官方论文页](https://neurips.cc/virtual/2026/poster/152254) · [作者来源](https://openreview.net/forum?id=UQOO8NDAjo)

- **问题 / 瓶颈** · 单点估计会掩盖不可识别性。
- **核心创新 / 方法** · 对光滑分布做条件最优运输，二次代价下推断稳定。
- **Baseline** · 传统部分识别估计器。
- **Benchmark** · 数值实验，效果集合推断。
- **关键结果 / 消融** · 给出渐近正态，实证比较估计与推断质量。
- **适用条件 / 局限** · 结论依赖光滑及二次成本。

**可复用机制** · 评价控制干预时先区分可识别范围和模型点预测。

<a id="paper-148436"></a>

## Statistical Limits of Affine Equivariant Estimation

[官方论文页](https://neurips.cc/virtual/2026/poster/148436) · [作者来源](https://openreview.net/forum?id=xpGyDKUODu)

- **问题 / 瓶颈** · 几何不变性可能有恢复代价。
- **核心创新 / 方法** · 重尾和污染两类设定做仿射等变下界。
- **Baseline** · Tukey、Stahel–Donoho 等。
- **Benchmark** · 高维稳健估计误差。
- **关键结果 / 消融** · 等变约束代价达 √d，经典估计器仍未必族内最优。
- **适用条件 / 局限** · 适用所分析污染与损失。

**可复用机制** · 设计鲁棒归一化时验算所要求的对称性是否损失可恢复性。

<a id="paper-155896"></a>

## Statistical Matching via Schr\"odinger Bridge beyond Conditional Independence

[官方论文页](https://neurips.cc/virtual/2026/poster/155896) · [作者来源](https://openreview.net/forum?id=21LjLAuU0D)

- **问题 / 瓶颈** · 共享变量不能排除未观测特征依赖。
- **核心创新 / 方法** · 用定向 Schrödinger 桥输出双向后验。
- **Baseline** · 条件独立假设。
- **Benchmark** · 合成、CelebA、Adult，预测效用。
- **关键结果 / 消融** · 性能持续改善；高斯及特定代价可精确恢复联合。
- **适用条件 / 局限** · 未观测依赖仍需模型条件。

**可复用机制** · 在模态数据不全配对时对照条件独立假设对下游的代价。

<a id="paper-153102"></a>

## Statistical Mixing Guarantees for Contractive Echo State Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/153102) · [作者来源](https://openreview.net/forum?id=NvLeAPXNDq)

- **问题 / 瓶颈** · 有 echo-state 性质不直接给稳定时间尺度。
- **核心创新 / 方法** · 把收缩系数映到混合和泛化界。
- **Baseline** · 传统容量及稳定分析。
- **Benchmark** · 独立或弱依赖输入。
- **关键结果 / 消融** · 得可核验稳定与预测规则，摘要无数值。
- **适用条件 / 局限** · 强相关输入和低收缩条件待查。

**可复用机制** · 规划状态记忆时联合约束历史依赖和所需混合时间。

<a id="paper-153359"></a>

## StatLUT: Statistical Feature-Driven Multimodal 3D LUT Generation for Photorealistic Style Transfer

[官方论文页](https://neurips.cc/virtual/2026/poster/153359) · [作者来源](https://openreview.net/forum?id=Ly4kWIst8U)

- **问题 / 瓶颈** · 逐像素编码将色彩与结构混入风格，并产生色阶。
- **核心创新 / 方法** · Lab 颜色统计条件生成 LUT，文本经扩散生成统计条件。
- **Baseline** · 传统编码和 LUT 迁移。
- **Benchmark** · 照片风格迁移及文本控制。
- **关键结果 / 消融** · 摘要报告机制与颜色保真目标，数字待核。
- **适用条件 / 局限** · 空间局部风格未必由全局 LUT 表达。

**可复用机制** · 外观编辑优先保留空间结构，单调试低维颜色参数。

<a id="paper-149045"></a>

## Stay Fair! Ensuring Group Fairness in Diffusion Models Across Guidance Scales

[官方论文页](https://neurips.cc/virtual/2026/poster/149045) · [作者来源](https://openreview.net/forum?id=tIDWhFyqX7)

- **问题 / 瓶颈** · 训练偏差以外，推理引导也会放大群体偏差。
- **核心创新 / 方法** · 分解不同区间的引导偏差并调公平引导。
- **Baseline** · 聚焦训练分布偏差的方法。
- **Benchmark** · 不同引导强度的群公平。
- **关键结果 / 消融** · 引导偏差随尺度递增并在大尺度占主导。
- **适用条件 / 局限** · 依赖群体标签和偏差定义。

**可复用机制** · 所有部署时可调采样参数都要一并审计公平与质量。

<a id="paper-153362"></a>

## ST-Bridge: Bridging Sketch and Text with Large Language Models for Coarse-to-Fine Image Retrieval

[官方论文页](https://neurips.cc/virtual/2026/poster/153362) · [作者来源](https://openreview.net/forum?id=LwKAysj5ob)

- **问题 / 瓶颈** · 全局融合丢鉴别线索。
- **核心创新 / 方法** · 通过 LLM 让草图近文本语义空间。
- **Baseline** · 直接融合和全局对齐。
- **Benchmark** · 场景级草图文字图像检索。
- **关键结果 / 消融** · 摘要报告更强检索，幅度未核。
- **适用条件 / 局限** · 生成描述可能忽略草图未明细节。

**可复用机制** · 检索时分开粗语义对齐和细粒条件验证。

<a id="paper-149419"></a>

## STDec: Spatio-Temporal Stability Guided Decoding for dLLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/149419) · [作者来源](https://openreview.net/forum?id=qBcBs3bMwp)

- **问题 / 瓶颈** · 过早解码可传播错误。
- **核心创新 / 方法** · 以时空稳定性调解码顺序。
- **Baseline** · 普通扩散 LLM 解码。
- **Benchmark** · 文本推理和多模态理解。
- **关键结果 / 消融** · 吞吐改善且质量相当。
- **适用条件 / 局限** · 阈值对任务和步数敏感。

**可复用机制** · 同时测内容稳定与可执行预算，再提交高置信 token。

<a id="paper-155473"></a>

## ST-DiffEye: Diffusion-based Continuous Gaze Generation via Joint Scanpath-Trajectory Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/155473) · [作者来源](https://openreview.net/forum?id=5MZl4W68FP)

- **问题 / 瓶颈** · 单条距离会惩罚合理多解。
- **核心创新 / 方法** · 联合建视线轨迹与路径，并推广序列相似为 CRPS。
- **Baseline** · 现有注视生成和单轨迹评价。
- **Benchmark** · 有目标及无目标搜索与自由观看。
- **关键结果 / 消融** · 摘要称领先，消融支持联合建模。
- **适用条件 / 局限** · 基础序列地度量决定评分含义。

**可复用机制** · 模仿学习多模态示范可用分布级指标验覆盖。

<a id="paper-148435"></a>

## SteadyThought: Mitigating LLM Under-Thinking via Thought-Level Preference Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/148435) · [作者来源](https://openreview.net/forum?id=xpPQq8hDSx)

- **问题 / 瓶颈** · 缩短输出可能诱发过早停止。
- **核心创新 / 方法** · 用思考粒度的偏好目标修正。
- **Baseline** · 现有长短推理优化。
- **Benchmark** · 多个模型及数据集，token 和准确率。
- **关键结果 / 消融** · token 更少，准确率持平或改善。
- **适用条件 / 局限** · 中间思考切分和监督质量待验。

**可复用机制** · 教模型何时结束，应评价思考单元边际贡献。

<a id="paper-153124"></a>

## Steer2Edit: From Activation Steering to Component-Level Editing

[官方论文页](https://neurips.cc/virtual/2026/poster/153124) · [作者来源](https://openreview.net/forum?id=Nk3qPYZkqr)

- **问题 / 瓶颈** · 上线每步转向持续费算力，广泛编辑难定位。
- **核心创新 / 方法** · 把转向向量用作组件选择诊断，并做 rank-1 编辑。
- **Baseline** · 全时激活转向。
- **Benchmark** · 组件级权重编辑。
- **关键结果 / 消融** · 提出免训练机制，摘要幅度待核。
- **适用条件 / 局限** · 局部编辑仍可能有相邻行为外溢。

**可复用机制** · 定位目标行为后小面积编辑，并独立回归其他能力。

<a id="paper-154457"></a>

## SteerCast: Retrieval-Based Latent Steering for Decoder-Only Time Series Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/154457) · [作者来源](https://openreview.net/forum?id=DRNgEw9MBD)

- **问题 / 瓶颈** · 固定预测器难适配细分模式。
- **核心创新 / 方法** · 取相似历史、聚合转向向量并逐步注入。
- **Baseline** · 微调底座和其他检索法。
- **Benchmark** · 多变量时序、多个预测窗口。
- **关键结果 / 消融** · 持续改善，不需额外训练。
- **适用条件 / 局限** · 索引近邻可能与当前未来机制不相似。

**可复用机制** · 用可撤销的检索干预替代全量模型更新。

<a id="paper-149209"></a>

## Steering Away from Memorization: Reachability-Constrained Reinforcement Learning for Text-to-Image Diffusion

[官方论文页](https://neurips.cc/virtual/2026/poster/149209) · [作者来源](https://openreview.net/forum?id=s8BKAZHA8D)

- **问题 / 瓶颈** · 无差别放大多样性会损害语义。
- **核心创新 / 方法** · 离线训练推理控制器，约束可达路径。
- **Baseline** · 现有推理期防记忆。
- **Benchmark** · 文生图，SSCD、FID、CLIP。
- **关键结果 / 消融** · 实现更好的三指标前沿。
- **适用条件 / 局限** · 取决于记忆检测与覆盖，须区分相似和复制。

**可复用机制** · 降低复制率时同时报告保真和提示一致性。

<a id="paper-156102"></a>

## Steering Externalities: Benign Activation Steering Unintentionally Increases Jailbreak Risk for Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/156102) · [作者来源](https://openreview.net/forum?id=0NZZS2IYP6)

- **问题 / 瓶颈** · 提高普通任务表现可能削弱底座安全。
- **核心创新 / 方法** · 比较上线前后标准安全测试结果。
- **Baseline** · 不做激活修改的同底座。
- **Benchmark** · 通用能力改动和安全评估。
- **关键结果 / 消融** · 摘要报告显著安全退化。
- **适用条件 / 局限** · 测试不能覆盖全部行为，须按部署更新重复。

**可复用机制** · 把安全能力当推理适配的回归门。

<a id="paper-148355"></a>

## Steering Fields: Adaptive Vector Fields for Safe Image Generation and Beyond

[官方论文页](https://neurips.cc/virtual/2026/poster/148355) · [作者来源](https://openreview.net/forum?id=yUc9CsiZvu)

- **问题 / 瓶颈** · 生成过程中状态方向会变。
- **核心创新 / 方法** · 逐步重估转向场。
- **Baseline** · 固定转向向量。
- **Benchmark** · 安全图像生成。
- **关键结果 / 消融** · 摘要提出动态机制，幅度待核。
- **适用条件 / 局限** · 评估需同时看生成质量和安全，不能只看一个分。

**可复用机制** · 把生成防御做成状态反馈控制，按阶段兼顾质量。

<a id="paper-149849"></a>

## Steering Frozen LLMs: Adaptive Social Alignment via Online Prompt Routing

[官方论文页](https://neurips.cc/virtual/2026/poster/149849) · [作者来源](https://openreview.net/forum?id=mrAigjn39k)

- **问题 / 瓶颈** · 冻结模型个性化若只看效用可能错误迁移安全偏好。
- **核心创新 / 方法** · 用两个相似图的交集分簇，再在线选择系统提示。
- **Baseline** · 最强非原型基线。
- **Benchmark** · 社会对齐、安全与效用、累积奖励。
- **关键结果 / 消融** · 累积奖励高 10.98%。
- **适用条件 / 局限** · 依赖在线反馈和相似度估计。

**可复用机制** · 把可共享探索经验的条件定为多个目标同时相近。

<a id="paper-149680"></a>

## Steering Optimisation Trajectories in Diffusion Representation Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149680) · [作者来源](https://openreview.net/forum?id=oF1hsTW7Rz)

- **问题 / 瓶颈** · 重建训练可能走上高重建但低解耦的路径。
- **核心创新 / 方法** · 调整 U-Net 捷径与噪声学习时序。
- **Baseline** · 常规扩散表征训练。
- **Benchmark** · 表征解耦、重建和对象分割。
- **关键结果 / 消融** · 摘要报告改善质量并降低种子敏感度。
- **适用条件 / 局限** · 摘要未给跨架构条件。

**可复用机制** · 表征目标不易直接监督时，可先控制训练早期允许的预测捷径。

<a id="paper-150277"></a>

## Steering Vectors as a Training Signal in LLM Post-Training

[官方论文页](https://neurips.cc/virtual/2026/poster/150277) · [作者来源](https://openreview.net/forum?id=jMVLPhJP73)

- **问题 / 瓶颈** · 零方差分组没有常规相对优势。
- **核心创新 / 方法** · 对受监督隐状态加钩子，或对特定 GRPO 组修正优势。
- **Baseline** · 常规监督微调及 GRPO。
- **Benchmark** · 不同方向、层、运算和模型检查点。
- **关键结果 / 消融** · 报告条件性改善，检查点改变可能失效。
- **适用条件 / 局限** · 必须重新验证方向与训练阶段的匹配。

**可复用机制** · 把激活干预当成独立训练信号，改变模型后重新校验方向。

<a id="paper-155743"></a>

## Steering Visual Generation in Unified Multimodal Models with Understanding Supervision

[官方论文页](https://neurips.cc/virtual/2026/poster/155743) · [作者来源](https://openreview.net/forum?id=3K0MBUbZGh)

- **问题 / 瓶颈** · 统一模型并训理解和生成不保证二者有效共享梯度。
- **核心创新 / 方法** · 用字幕和视觉回归分别注入抽象语义及结构细节。
- **Baseline** · 普通统一多模态后训练。
- **Benchmark** · 图像生成与编辑。
- **关键结果 / 消融** · 摘要报告两类任务受益。
- **适用条件 / 局限** · 独立效应量未报告。

**可复用机制** · 设计共享模型时让感知目标直接约束生成所用表征。

<a id="paper-150589"></a>

## STEER: Route-Aware Adaptive Reasoning for  Autonomous Driving

[官方论文页](https://neurips.cc/virtual/2026/poster/150589) · [作者来源](https://openreview.net/forum?id=h3f4C9NmLn)

- **问题 / 瓶颈** · 人工难度标签不等于推理实际收益。
- **核心创新 / 方法** · 优化直接回答与逐步推理路由。
- **Baseline** · 隐式或标签驱动的自适应驾驶。
- **Benchmark** · NAVSIM v1/v2，规划和推理效率。
- **关键结果 / 消融** · 作者报告规划与效率前沿改善。
- **适用条件 / 局限** · 需要有判别力的环境回报。

**可复用机制** · 按动作后果而非主观难度训练计算预算门。

<a id="paper-154118"></a>

## Stein Transport for Generative Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/154118) · [作者来源](https://openreview.net/forum?id=G8E7Hq2vAz)

- **问题 / 瓶颈** · 目标密度梯度不可得，昂贵样本有限。
- **核心创新 / 方法** · 用目标样本及高斯噪声构造代理，并在 RKHS 中闭式估计。
- **Baseline** · 既有生成或输运方法。
- **Benchmark** · 有限样本增强及贝叶斯逆问题。
- **关键结果 / 消融** · 摘要展示后验样本扩充。
- **适用条件 / 局限** · 依赖核选择，摘要未给高维可扩展性。

**可复用机制** · 高质量模拟样本稀缺时，可以学习样本到样本的局部输运而不估显式密度。

<a id="paper-139814"></a>

## StemBind: When MLLMs Get Lost Between Rules and Instances in Abstract Visual Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/139814) · [作者来源](https://openreview.net/forum?id=36x2MXhzBB)

- **问题 / 瓶颈** · 最终回答不能区分识别、找规律及使用规律的错误。
- **核心创新 / 方法** · 在共享图形题干上对齐三种问法。
- **Baseline** · 最终答案指标与子任务问答。
- **Benchmark** · 2298 个视觉题干。
- **关键结果 / 消融** · 摘要指出规则到实例绑定是明确的瓶颈。
- **适用条件 / 局限** · 限知识较轻的抽象图题。

**可复用机制** · 保持图像相同拆解能力，以免跨题内容差异混淆错因。

<a id="paper-149117"></a>

## StepBack: Step-Level Error-Localized Resampling for Efficient Test-Time Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/149117) · [作者来源](https://openreview.net/forum?id=skhKf04svt)

- **问题 / 瓶颈** · 全轨迹重生成浪费正确前缀。
- **核心创新 / 方法** · 轻量定位首错后重新生成后缀，并投票。
- **Baseline** · 自一致性与提前终止方法。
- **Benchmark** · 推理准确率与 token 用量。
- **关键结果 / 消融** · 摘要报告节约 token 至多 50%。
- **适用条件 / 局限** · 依赖首错定位精度。

**可复用机制** · 存在可靠局部失败信号时，以前缀复用替代重复整条搜索。

<a id="paper-153635"></a>

## Step-by-Step Optimization-like Reasoning in LLMs over Expanding Search Spaces

[官方论文页](https://neurips.cc/virtual/2026/poster/153635) · [作者来源](https://openreview.net/forum?id=Juf7k3U9xW)

- **问题 / 瓶颈** · 终点验证无法区分搜索早期多个可行动作。
- **核心创新 / 方法** · 用求解器当价值先知并按名次塑形在线奖励。
- **Baseline** · 只能终点检查的推理训练。
- **Benchmark** · OPT-star 可扩展搜索空间及训练消融。
- **关键结果 / 消融** · 报告改善逐步优化式推理。
- **适用条件 / 局限** · 依赖局部值评估器和构造任务。

**可复用机制** · 长程组合任务可给部分解提供可比较的延续价值。

<a id="paper-149665"></a>

## StepCAD: Mesh-to-CAD Code Generation via LLM Policy and Geometry-Guided Search

[官方论文页](https://neurips.cc/virtual/2026/poster/149665) · [作者来源](https://openreview.net/forum?id=oLvC2AljNY)

- **问题 / 瓶颈** · 一次写完整 CAD 难利用几何差异。
- **核心创新 / 方法** · 逐步按目标网格生成并在程序空间修订。
- **Baseline** · 既有网格转 CAD 方法。
- **Benchmark** · 网格重建、程序有效性与 IoU。
- **关键结果 / 消融** · 相对 IoU 增益最高 87.2%。
- **适用条件 / 局限** · 依赖可执行 CAD 表示。

**可复用机制** · 可执行输出的部分状态可充当搜索目标和错误定位证据。

<a id="paper-155406"></a>

## Step-dLLM: Adaptive Step-aware Sparse Attention for Efficient Diffusion LLM Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/155406) · [作者来源](https://openreview.net/forum?id=5sFFGPtDy2)

- **问题 / 瓶颈** · 跨步掩码只局部稳定，各头集中度也不同。
- **核心创新 / 方法** · 定期重建块稀疏图。
- **Baseline** · 密集 FlashAttention 和既有稀疏方案。
- **Benchmark** · 16K 上下文，核速度、延迟与准确度。
- **关键结果 / 消融** · 90% 稀疏度核快 4.2 倍，95% 时最高 8.5 倍。
- **适用条件 / 局限** · 核速度并非端到端加速。

**可复用机制** · 迭代模型的稀疏掩码应覆盖工作阶段和组件差异。

<a id="paper-148969"></a>

## Stepwise Penalization for Length-Efficient Chain-of-Thought Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/148969) · [作者来源](https://openreview.net/forum?id=tmQ2NMwIWk)

- **问题 / 瓶颈** · 全串统一惩罚可能压缩关键步骤。
- **核心创新 / 方法** · 在组相对策略更新中增加步骤过程优势。
- **Baseline** · 基础模型和序列级长度目标。
- **Benchmark** · 推理准确率及长度。
- **关键结果 / 消融** · 摘要报告长度平均降 56.3%，准确率升 4.2%。
- **适用条件 / 局限** · 依赖步骤贡献估计。

**可复用机制** · 压缩推理时优先减少低贡献环节而非同比截断。

<a id="paper-151384"></a>

## Step-wise Rubric Rewards for LLM Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/151384) · [作者来源](https://openreview.net/forum?id=b17OAEl2CG)

- **问题 / 瓶颈** · 汇总为一个分值会给错步骤同等信用，也可能鼓励重复返工。
- **核心创新 / 方法** · 按标准和步骤分派反馈。
- **Baseline** · 整响应的聚合规则奖励。
- **Benchmark** · AIME 2025 的忠实推理与自纠循环。
- **关键结果 / 消融** · 忠实率 34.5% 到 46.7%，自纠循环 48.1% 到 26.5%。
- **适用条件 / 局限** · 依赖稳定的步骤判定。

**可复用机制** · 过程奖励不仅看答案，还要检查错误步骤和无界自纠是否减少。

<a id="paper-139613"></a>

## StereoTales: A Multilingual Framework for Open-Ended Stereotype Discovery in LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/139613) · [作者来源](https://openreview.net/forum?id=FRBT5zuX3I)

- **问题 / 瓶颈** · 翻译同一组题难反映各语言环境偏见
- **核心创新 / 方法** · 用开放故事探测并对照人工和模型伤害评级
- **Baseline** · 不同语言、模型和人工评级
- **Benchmark** · 多语故事、属性差异及伤害评分
- **关键结果 / 消融** · 群体影响随语言改变，人工与模型评级相关 0.62
- **适用条件 / 局限** · 评审价值和样本语境限制外推

**可复用机制** · 覆盖各部署语言的高相关文化场景并独立核验评审

<a id="paper-152342"></a>

## Sticky Jump Diffusions: A Unifying Framework for Discrete, Continuous, and Hybrid Diffusion

[官方论文页](https://neurips.cc/virtual/2026/poster/152342) · [作者来源](https://openreview.net/forum?id=TmV4qk3gOS)

- **问题 / 瓶颈** · 离散、连续和混合过程往往绑定不同设计
- **核心创新 / 方法** · 以统一粘性跳跃过程分离离开锚点内核和逐锚 hazard
- **Baseline** · 离散、连续和混合扩散
- **Benchmark** · CIFAR-10、ImageNet-64、Text8、Sudoku
- **关键结果 / 消融** · 各设置具有竞争力，未列数字
- **适用条件 / 局限** · 采样参数需要按数据空间设定

**可复用机制** · 联合图文去噪可独立调结构扰动和恢复时序

<a id="paper-149260"></a>

## STILL: Selecting Tokens for Intra-Layer Hybrid Attention to Linearize LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/149260) · [作者来源](https://openreview.net/forum?id=rgEJDjkYDK)

- **问题 / 瓶颈** · 完全线性化会牺牲长距细粒度需求
- **核心创新 / 方法** · 层内动态选择 token，并用块并行和延后选择
- **Baseline** · 原预训练模型及既有线性化方法
- **Benchmark** · 常识、一般推理及长上下文
- **关键结果 / 消融** · 长上下文最高相对增 86.2%，短任务持平或更强
- **适用条件 / 局限** · 依赖筛选覆盖与硬件实现

**可复用机制** · 按长距任务保留少量精确计算并查遗漏率

<a id="paper-152828"></a>

## StitchEdit: Stitching Depth Priors into Image Editors via Per-Layer Gradient Probing

[官方论文页](https://neurips.cc/virtual/2026/poster/152828) · [作者来源](https://openreview.net/forum?id=Q7G74v5nSs)

- **问题 / 瓶颈** · 全层保留深度先验可能阻碍任务语义
- **核心创新 / 方法** · 以逐层探针调整学习率，分别保留深度迁移及允许更新
- **Baseline** · 指令编辑、深度条件编辑
- **Benchmark** · 150 空间、遮挡、视角编辑；感知及几何保真
- **关键结果 / 消融** · 摘要称两项领先
- **适用条件 / 局限** · 依赖探针与目标编辑属性相关

**可复用机制** · 先定位几何先验在哪些层有益，再分配适配强度

<a id="paper-149632"></a>

## Stitched Value Model for Diffusion Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/149632) · [作者来源](https://openreview.net/forum?id=odBEybhkHQ)

- **问题 / 瓶颈** · 每条样本估价值耗时和显存大
- **核心创新 / 方法** · 一次拟合可复用的噪声条件价值，应用多种对齐方法
- **Baseline** · 未摊销的 DPS、DiffusionNFT
- **Benchmark** · 扩散对齐的速度和显存
- **关键结果 / 消融** · DPS 快 3.2 倍并减半显存，DiffusionNFT 快 2.3 倍
- **适用条件 / 局限** · 需目标足够稳定以摊销拟合

**可复用机制** · 分开统计训练价值模型的成本和大量调用的节省

<a id="paper-149803"></a>

## Stochastic Grouping Conformal Prediction for Effective Subgroup Reliability

[官方论文页](https://neurips.cc/virtual/2026/poster/149803) · [作者来源](https://openreview.net/forum?id=nFBHPHZ66f)

- **问题 / 瓶颈** · 小群组独立校准估计不稳，全局掩盖差异
- **核心创新 / 方法** · 通过随机分组形成局部评分分布
- **Baseline** · 现有共形预测方法
- **Benchmark** · 合成和真实数据；子群覆盖与预测集大小
- **关键结果 / 消融** · 子群覆盖差距变小，预测集更小或相当
- **适用条件 / 局限** · 总体覆盖保证不等同任意子组严格覆盖

**可复用机制** · 部署可靠集时报告子组与整体两种覆盖

<a id="paper-149605"></a>

## Stop or Restart? Principled Inference Control for Large Reasoning Models via the Pandora's Box

[官方论文页](https://neurips.cc/virtual/2026/poster/149605) · [作者来源](https://openreview.net/forum?id=orRObNupcB)

- **问题 / 瓶颈** · 高置信错误不能靠基于置信的早停解决
- **核心创新 / 方法** · 校准停止并将部分预算给多样化重启
- **Baseline** · 常规测试时策略和额外样本对照
- **Benchmark** · 六推理基准、多 DeepSeek-R1 蒸馏模型；效率与校准
- **关键结果 / 消融** · 改善准确效率、ECE 与选择性准确，未列数字
- **适用条件 / 局限** · 边际收益需随任务和模型校准

**可复用机制** · 区分已可靠解与错误收敛，再决定延长还是重启

<a id="paper-148260"></a>

## Stop the Sampler! Classifier-Based Adaptive Stopping for Sampling Kernels

[官方论文页](https://neurips.cc/virtual/2026/poster/148260) · [作者来源](https://openreview.net/forum?id=zB413mSyhL)

- **问题 / 瓶颈** · 固定轨迹长度浪费计算或漏模式。
- **核心创新 / 方法** · 学习分类停止器并多层训练探索。
- **Baseline** · 标准 MCMC。
- **Benchmark** · 多个概率密度、长度、模式覆盖和混合。
- **关键结果 / 消融** · 更短轨迹且改善覆盖。
- **适用条件 / 局限** · 分类器误差对平衡条件需检查。

**可复用机制** · 将何时停作为采样核的一部分而非外接启发式。

<a id="paper-155026"></a>

## StoSplat: Ray-Aligned Stochastic Preconditioning for Feed-Forward 3D Gaussian Splatting

[官方论文页](https://neurips.cc/virtual/2026/poster/155026) · [作者来源](https://openreview.net/forum?id=94W0JyIrl4)

- **问题 / 瓶颈** · 几何边界和漂浮高斯不稳。
- **核心创新 / 方法** · 训练时扰动沿射线的中心，推理不变。
- **Baseline** · 现有前馈 3DGS。
- **Benchmark** · RealEstate10K、ScanNet、ACID。
- **关键结果 / 消融** · 减少漂浮物及边界伪影，推理无额外开销。
- **适用条件 / 局限** · 依赖相机射线与退火尺度。

**可复用机制** · 利用观测不确定性轴预条件训练，免加部署模块。

<a id="paper-149431"></a>

## STParOpt: An End-to-End Framework for Execution-Aware Parallelism Inference and Optimized CUDA Migration

[官方论文页](https://neurips.cc/virtual/2026/poster/149431) · [作者来源](https://openreview.net/forum?id=q6zVPYeseN)

- **问题 / 瓶颈** · 仅源码难可靠确认能否安全并行。
- **核心创新 / 方法** · 把并行选择建成部分观测问题，用运行信号消歧。
- **Baseline** · 编译器和 LLM 基线。
- **Benchmark** · 标准 HPC，CUDA 生成和并行识别。
- **关键结果 / 消融** · 两维优于基线，幅度未报告。
- **适用条件 / 局限** · 能运行的输入可能未覆盖正确性边界。

**可复用机制** · 先分出不可静态确定的决策，只对这些补运行测试。

<a id="paper-139430"></a>

## STRABLE: Benchmarking Tabular Machine Learning with Strings

[官方论文页](https://neurips.cc/virtual/2026/poster/139430) · [作者来源](https://openreview.net/forum?id=RIVxz1UYR5)

- **问题 / 瓶颈** · 文本存在不保证需要昂贵语言模型。
- **核心创新 / 方法** · 大规模对比字符串嵌入和表格管线。
- **Baseline** · 445 管线。
- **Benchmark** · STRABLE，现实表格与 oracle 排名。
- **关键结果 / 消融** · 常见类别主导场景简单嵌入便宜有效，榜单近 oracle。
- **适用条件 / 局限** · 语义密集长文本有不同需求。

**可复用机制** · 先测列是类别还是语义文本再选择编码。

<a id="paper-139618"></a>

## Stranger Things: When Objects Appear Without Their Typical Neighbours

[官方论文页](https://neurips.cc/virtual/2026/poster/139618) · [作者来源](https://openreview.net/forum?id=ExCVh3IQLg)

- **问题 / 瓶颈** · 主流平均成绩会掩盖依赖上下文捷径。
- **核心创新 / 方法** · 用配对 NPMI 排序和受控布局构造反常组合。
- **Baseline** · 五种视觉模型家族。
- **Benchmark** · STRANGE-Bench 11 档，监督、开放检测及分类。
- **关键结果 / 消融** · 揭示共现稀有时识别难点，幅度待核。
- **适用条件 / 局限** · 受合成风格及共现语料限制。

**可复用机制** · 构造不常共现的合理场景测试具身感知。

<a id="paper-152317"></a>

## StraTA: Incentivizing Agentic Reinforcement Learning with Strategic Trajectory Abstraction

[官方论文页](https://neurips.cc/virtual/2026/poster/152317) · [作者来源](https://openreview.net/forum?id=Tyr5VMW1pW)

- **问题 / 瓶颈** · 仅步骤动作与终局奖励难稳定探索。
- **核心创新 / 方法** · 在代理 RL 加策略抽象。
- **Baseline** · 强交互策略基线。
- **Benchmark** · ALFWorld、WebShop、SciWorld。
- **关键结果 / 消融** · 样本效率及最终表现一致改善。
- **适用条件 / 局限** · 策略文本不保证实际执行，须对照。

**可复用机制** · 让高层策略作为共享学习变量，再验是否改善整条轨迹。

<a id="paper-151459"></a>

## Strategic Causal Policy Learning: Welfare, Safety, and Fairness Thresholds

[官方论文页](https://neurips.cc/virtual/2026/poster/151459) · [作者来源](https://openreview.net/forum?id=aU5nzy3oAK)

- **问题 / 瓶颈** · 静态 CATE 规则忽略受益者改变可见属性。
- **核心创新 / 方法** · 以能达到处理区域的基线人群加权计算福利。
- **Baseline** · 常规按 CATE 阈值。
- **Benchmark** · 策略性干预福利、公平与安全权衡。
- **关键结果 / 消融** · 群体修正可恢复适宜分配，摘要未给数值。
- **适用条件 / 局限** · 需可信响应及操纵成本模型。

**可复用机制** · 具有部署反馈的决策系统应测试人群响应后的有效分布。

<a id="paper-156150"></a>

## Strategic Decision Focused Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/156150) · [作者来源](https://openreview.net/forum?id=00GgrAB0VK)

- **问题 / 瓶颈** · 预测更准确可能引发较差集体策略。
- **核心创新 / 方法** · 将预测后代理响应写入决策目标。
- **Baseline** · 预测精度优先的方法。
- **Benchmark** · 自然保护和基础设施场景。
- **关键结果 / 消融** · 理论和实证显示精度到效用可能非单调。
- **适用条件 / 局限** · 依赖博弈行为及均衡假设。

**可复用机制** · 将用户反应加入部署评价后再比较预测器。

<a id="paper-149381"></a>

## Strategic Decision Support for AI Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/149381) · [作者来源](https://openreview.net/forum?id=qUvsQBmDZg)

- **问题 / 瓶颈** · 固定多求助代价大，少求助又错失可修复实例。
- **核心创新 / 方法** · 估计支持反事实价值，按阈值选择并在线校准。
- **Baseline** · 无需支持和固定支持。
- **Benchmark** · 信息收集、人机协作、工具。
- **关键结果 / 消融** · 理论给阈值最优，可减少不必调用。
- **适用条件 / 局限** · 反事实价值外推依赖校准覆盖。

**可复用机制** · 将求助预算写成遗漏重要帮助的统计约束。

<a id="paper-139431"></a>

## Strategic Evaluation: Incentivizing AI Capability Coverage with Private Benchmarks

[官方论文页](https://neurips.cc/virtual/2026/poster/139431) · [作者来源](https://openreview.net/forum?id=RDooecvZ8l)

- **问题 / 瓶颈** · 开发者可在有限公共任务上专门优化。
- **核心创新 / 方法** · 把评估建成信息不对称动态博弈并抽取任务。
- **Baseline** · 固定公开评估。
- **Benchmark** · 覆盖率和社会任务效用分析。
- **关键结果 / 消融** · 能激励更广任务覆盖，摘要未给实证数。
- **适用条件 / 局限** · 依赖任务抽样与开发者激励。

**可复用机制** · 选择代理基准时保留随机隐藏切片。

<a id="paper-154371"></a>

## Strategic Feature Selection and Regularization

[官方论文页](https://neurips.cc/virtual/2026/poster/154371) · [作者来源](https://openreview.net/forum?id=E5F4jOGdsq)

- **问题 / 瓶颈** · 高风险特征仍含稳定预测信息。
- **核心创新 / 方法** · 将战略响应纳入特征选择和正则。
- **Baseline** · 仅操控性筛选。
- **Benchmark** · 策略性决策的学习。
- **关键结果 / 消融** · 单按操控性排除通常次优。
- **适用条件 / 局限** · 需要响应模型与实证外推。

**可复用机制** · 联合选择预测价值和响应后成本，而非二值禁用。

<a id="paper-150241"></a>

## Strategist: Designing Agentic Reasoning at Scale

[官方论文页](https://neurips.cc/virtual/2026/poster/150241) · [作者来源](https://openreview.net/forum?id=jgFA7uSnky)

- **问题 / 瓶颈** · 仅写高层策略不测执行成本。
- **核心创新 / 方法** · 元代理提议候选，执行并按准确与成本调整。
- **Baseline** · 固定推理策略。
- **Benchmark** · 小开发集上的任务流程设计。
- **关键结果 / 消融** · 摘要提出可执行验证机制，幅度待核。
- **适用条件 / 局限** · 开发集需隔离于检验集。

**可复用机制** · 将可观测收益当策略编辑验收条件。

<a id="paper-139777"></a>

## StreamGaze: Gaze-Guided Temporal Reasoning and Proactive Understanding in Streaming Videos

[官方论文页](https://neurips.cc/virtual/2026/poster/139777) · [作者来源](https://openreview.net/forum?id=5OWuaFLDP6)

- **问题 / 瓶颈** · 单纯视频时序问题缺人注意线索。
- **核心创新 / 方法** · 过去、当前、主动三类任务仅允许当前可见前缀。
- **Baseline** · 传统视频流式基准。
- **Benchmark** · StreamGaze，实时注视及用户意图。
- **关键结果 / 消融** · 摘要提供评测设置；数值待核。
- **适用条件 / 局限** · 视线延迟和眼动不等于意图。

**可复用机制** · 用因果可用输入检验助手能否从非语言提示得出行动。

<a id="paper-138994"></a>

## Streaming Interventions: Can Video LLMs Correct Mistakes as They Occur?

[官方论文页](https://neurips.cc/virtual/2026/poster/138994) · [作者来源](https://openreview.net/forum?id=s3K6o5xMfu)

- **问题 / 瓶颈** · 静态问答难教代理在过早与过晚之间选择。
- **核心创新 / 方法** · 将普通视频转换成表现出主动纠正的监督。
- **Baseline** · 原视频模型及不做反事实微调。
- **Benchmark** · Ego-MC-Bench，实际烹饪模拟的逐步帮助。
- **关键结果 / 消融** · 小视频模型改善尤明显。
- **适用条件 / 局限** · 合成提醒和真人容忍度仍需测。

**可复用机制** · 将干预何时发生与说什么一起标注。

<a id="paper-151287"></a>

## StreamMind: Dynamic Streaming Cognition for Online Video Understanding

[官方论文页](https://neurips.cc/virtual/2026/poster/151287) · [作者来源](https://openreview.net/forum?id=bXFMwP5xIt)

- **问题 / 瓶颈** · 每帧思考使回应闪烁、上下文碎片化。
- **核心创新 / 方法** · 按 GoP 累证并在边界调度记忆和推理。
- **Baseline** · 固定帧级更新。
- **Benchmark** · 在线流视频理解和主动交互。
- **关键结果 / 消融** · 摘要指出减少早判，量化待核。
- **适用条件 / 局限** · 过长窗口可能延迟紧急响应。

**可复用机制** · 把暂停、合并与立即响应设计为时序接口。

<a id="paper-150068"></a>

## StreamOV: Streaming Omni-Video Understanding via Evidence-Guided Memory and Response Triggering

[官方论文页](https://neurips.cc/virtual/2026/poster/150068) · [作者来源](https://openreview.net/forum?id=kzU6tZ4CEa)

- **问题 / 瓶颈** · 全历史的显存和逐步询问代价高。
- **核心创新 / 方法** · 长短期记忆压缩相关跨模态证据。
- **Baseline** · 现有流式及离线理解模型。
- **Benchmark** · SOVBench 与多流视频基准。
- **关键结果 / 消融** · 摘要报告强表现，幅度未核。
- **适用条件 / 局限** · 罕见低置信证据可能在压缩中丢失。

**可复用机制** · 把缓存优先级与用户潜在下一问题的信息价值联系。

<a id="paper-149743"></a>

## StreamPhy: Streaming Inference of High-Dimensional Physical Dynamics via  State Space Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149743) · [作者来源](https://openreview.net/forum?id=ng9cOq8Ghi)

- **问题 / 瓶颈** · 扩散法批量采样在稀疏、非等距观测下耗时。
- **核心创新 / 方法** · 将鲁棒观测编码与结构时序状态转移结合。
- **Baseline** · 扩散和其他物理场重建。
- **Benchmark** · 多个稀疏不规则采样条件，比较误差和延迟。
- **关键结果 / 消融** · 摘要报告准确度至少改善 48%，较扩散快 20 至 100 倍。
- **适用条件 / 局限** · 摘要未给系统规模、指标口径和分布变化范围。

**可复用机制** · 实时全场推断可用紧凑状态接收新传感数据而无需重新计算整个窗口。

<a id="paper-154290"></a>

## StreamPI: Streaming Multimodal Temporal Modeling for Vision-Language-Action Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154290) · [作者来源](https://openreview.net/forum?id=EsxSwziuTY)

- **问题 / 瓶颈** · 忽略语言和多帧对齐会削弱流式 VLA 的记忆与视觉细节。
- **核心创新 / 方法** · 以观测指令对为时间单元重排注意力，无新增参数。
- **Baseline** · π₀.₅。
- **Benchmark** · LIBERO 与真机记忆、精确感知任务。
- **关键结果 / 消融** · 摘要报告多任务表现超过基线。
- **适用条件 / 局限** · 摘要未给缓存开销及更长历史结果。

**可复用机制** · 在流式多模态序列对内部保留双向交互，再跨单元限制未来信息。

<a id="paper-149538"></a>

## STREAM: Stochastic Riemannian Flow Matching with Anisotropic Decoder for Digital Histopathology Image Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/149538) · [作者来源](https://openreview.net/forum?id=pP7kJXjPeY)

- **问题 / 瓶颈** · 强条件可能主导扩散潜空间并削弱多样性。
- **核心创新 / 方法** · 使用病理视觉模型的补丁特征作为生成潜变量，并采用各向异性解码。
- **Baseline** · 将视觉特征只作为条件的生成方法。
- **Benchmark** · 乳腺及结直肠组织影像重建与生成。
- **关键结果 / 消融** · 摘要报告达到先进表现。
- **适用条件 / 局限** · 需要可解码的领域特征，摘要未给多样性效应量。

**可复用机制** · 若强条件压缩了真实变异，应测试把它替换为生成坐标系本身。

<a id="paper-149527"></a>

## Strengthening LLMs for Tabular Prediction with Structural Priors

[官方论文页](https://neurips.cc/virtual/2026/poster/149527) · [作者来源](https://openreview.net/forum?id=pTunYUdPGz)

- **问题 / 瓶颈** · 表格多列的任意顺序及稀疏奖励会让模型学习表面格式。
- **核心创新 / 方法** · 用列重排构造等义观测，估计排列内和跨排列优势。
- **Baseline** · 包含 DeepSeek-R1 的推理模型。
- **Benchmark** · 表格预测，测预测性能。
- **关键结果 / 消融** · 摘要报告相较所述推理基座最高改善 53.17%。
- **适用条件 / 局限** · 需要真正保持标签的列排列，不适用于顺序有语义的字段。

**可复用机制** · 强化学习任务有已知对称性时，可跨等价视图共享结果监督。

<a id="paper-155256"></a>

## Stress Testing Chain-of-Thought Monitoring Against Covert Misalignment

[官方论文页](https://neurips.cc/virtual/2026/poster/155256) · [作者来源](https://openreview.net/forum?id=747gaY76Ke)

- **问题 / 瓶颈** · 短窗口异常检测无法覆盖上下文中逐渐偏离的行为。
- **核心创新 / 方法** · 在防御评测中结合整体和局部证据进行轨迹监控。
- **Baseline** · 既有思维链监控。
- **Benchmark** · TraceMRT，监控 AUC 与固定误报率下召回。
- **关键结果 / 消融** · 作者报告 AUC 0.91，误报率 0.05 时召回 0.74。
- **适用条件 / 局限** · 结果受可观察轨迹和基准分布限制。

**可复用机制** · 对行为监控按整个任务意图验证警报，避免只依赖短文本异常线索。

<a id="paper-139653"></a>

## Stress-Testing Neural Network Verifiers with Provably Robust Instances

[官方论文页](https://neurips.cc/virtual/2026/poster/139653) · [作者来源](https://openreview.net/forum?id=DD3nu4ghCl)

- **问题 / 瓶颈** · 未解决实例的标签未知，难区分超时、求解器和数值错误。
- **核心创新 / 方法** · 构造已知真值用例并记录求解难度分布。
- **Baseline** · 常用神经网络验证器。
- **Benchmark** · 解析标注的鲁棒性实例与难度诊断。
- **关键结果 / 消融** · 发现多项容差与实现问题。
- **适用条件 / 局限** · 通过构造的用例不能证明一般验证器正确。

**可复用机制** · 验证系统测评可先使用可信数学真值再测试更现实样例，分开量化无解和错误判断。

<a id="paper-148237"></a>

## STRIDE: Learnable Stepwise Language Feedback for LLM Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/148237) · [作者来源](https://openreview.net/forum?id=zNirHi4Pw4)

- **问题 / 瓶颈** · 零通过的采样组无法从相同的标量失败奖中学习。
- **核心创新 / 方法** · 以可学习的逐步文本反馈替代固定标量过程信号。
- **Baseline** · 标量方法与冻结或外部批评器。
- **Benchmark** · 推理任务和零通过问题的消融。
- **关键结果 / 消融** · 摘要报告在标量对照无学习信号的设置出现改善。
- **适用条件 / 局限** · 需要可靠的语言纠错，摘要未给额外生成成本。

**可复用机制** · 没有成功轨迹时，试用说明如何修改的局部反馈，先度量它能否引导到新解。

<a id="paper-153529"></a>

## Strong Helps Weak: Directional Cross-Modal Alignment Transfer in Multi-modal LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/153529) · [作者来源](https://openreview.net/forum?id=Keys8KrDQl)

- **问题 / 瓶颈** · 同模态对齐检查点在音视频等任务上不足。
- **核心创新 / 方法** · 用小校准集在权重空间闭式求出方向性跨模态对齐。
- **Baseline** · 现有模型合并方法。
- **Benchmark** · 资源不对称的模态迁移。
- **关键结果 / 消融** · 摘要报告优于既有合并法。
- **适用条件 / 局限** · 概念共享和方向选择依赖配对模型，摘要未给配对预算。

**可复用机制** · 把能力迁移视为有向选择，在保留目标模态效用条件下验证高资源来源。

<a id="paper-149475"></a>

## Strong Stochastic Flow Maps

[官方论文页](https://neurips.cc/virtual/2026/poster/149475) · [作者来源](https://openreview.net/forum?id=ppj0Eq4Y6y)

- **问题 / 瓶颈** · 常见随机流映射在分布意义上正确，却无法恢复同一噪声路径。
- **核心创新 / 方法** · 学习加性噪声 SDE 的强解映射，得到扩散模型的无模拟训练目标。
- **Baseline** · 此前仅匹配分布的流映射。
- **Benchmark** · 图像生成及少步随机系统采样。
- **关键结果 / 消融** · 摘要报告图像生成优于先前流映射。
- **适用条件 / 局限** · 只分析加性噪声 SDE，摘要未给计算量。

**可复用机制** · 生成动态时先明确是否需要同条件随机轨迹可重复，若需要就监督路径 而不仅是边缘。

<a id="paper-153838"></a>

## Strong Teacher Not Needed? On Distillation in LLM Pretraining

[官方论文页](https://neurips.cc/virtual/2026/poster/153838) · [作者来源](https://openreview.net/forum?id=ILYXt4mA8l)

- **问题 / 瓶颈** · 只换更大教师可能使增益饱和或逆转。
- **核心创新 / 方法** · 对照不同规模和成熟度的教师及不同蒸馏目标混合。
- **Baseline** · 标准语言模型预训练。
- **Benchmark** · 域内拟合、域外泛化和下游性能。
- **关键结果 / 消融** · 小或欠训练教师也能改善大模型，提升更常出现在泛化。
- **适用条件 / 局限** · 依赖损失混合，摘要未报告普适比例。

**可复用机制** · 用较便宜教师作为对照，并分开跟踪域内损失与域外表现再决定扩教师。

<a id="paper-155008"></a>

## StructLens: A Structural Lens for Language Models via Maximum Spanning Trees

[官方论文页](https://neurips.cc/virtual/2026/poster/155008) · [作者来源](https://openreview.net/forum?id=9HF1y6JGjp)

- **问题 / 瓶颈** · 逐 token 探针难观察整体表示层次。
- **核心创新 / 方法** · 构建残差流语义关系图，再提取最大生成树。
- **Baseline** · 局部 token 或传统句法结构解释。
- **Benchmark** · 跨层与跨训练阶段的语言结构。
- **关键结果 / 消融** · 摘要报告局部单元先显现、更大单元较晚。
- **适用条件 / 局限** · 树结构省略多重关系，摘要未给复杂语言外推。

**可复用机制** · 需要探测表示层级时，可用全局关系摘要而非单位置可预测性。

<a id="paper-152860"></a>

## Structural Blindness in Latent Data Assimilation: Representation Geometry Misleads Sensor Design

[官方论文页](https://neurips.cc/virtual/2026/poster/152860) · [作者来源](https://openreview.net/forum?id=Pr0dB2FD5u)

- **问题 / 瓶颈** · 平均解码几何会合并物理传感行为不同的选项。
- **核心创新 / 方法** · 分析 Fisher–Gram 粗化如何屏蔽真实传感差异，再用滤波相关验证。
- **Baseline** · 解码器 Fisher 的优化设计及可观测性评分。
- **Benchmark** · 潜空间数据同化、物理传感器排序。
- **关键结果 / 消融** · 摘要报告平均几何统计存在结构性盲点。
- **适用条件 / 局限** · 结论针对特定可写成平滑泛函的诊断。

**可复用机制** · 代理分数若把候选投影到相同表示，应以实际在线状态估计验证是否仍等效。

<a id="paper-155742"></a>

## Structural Causal Bottleneck Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155742) · [作者来源](https://openreview.net/forum?id=3KALmCyLoY)

- **问题 / 瓶颈** · 高维工具变量的朴素两阶段最小二乘可能在总体层面不可辨识。
- **核心创新 / 方法** · 为全变量学习结构瓶颈，再比较标准调整。
- **Baseline** · 朴素两阶段最小二乘与全维条件调整。
- **Benchmark** · 线性结构瓶颈的效应估计与可识别性实证。
- **关键结果 / 消融** · 摘要指出表征可改善朴素方法丢失的识别条件。
- **适用条件 / 局限** · 保证依赖所述因果结构与假设。

**可复用机制** · 降维前需要验证留下的特征保留调整或工具变量通路。

<a id="paper-149682"></a>

## Structural Entropy Optimized Communication for Multi-Agent Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149682) · [作者来源](https://openreview.net/forum?id=oE5vpNzODi)

- **问题 / 瓶颈** · 拓扑密集与消息冗余各自消耗通信预算
- **核心创新 / 方法** · 可微结构熵压图，节点信息瓶颈压消息
- **Baseline** · 现有 MARL 通信方法
- **Benchmark** · 含 SMACv2 的多智能体基准
- **关键结果 / 消融** · 摘要报告领先，未列定量
- **适用条件 / 局限** · 依赖训练时可微近似和部署通信代价

**可复用机制** · 给多机协作设拓扑与带宽两个独立消融

<a id="paper-152271"></a>

## Structural Rationale Distillation via Reasoning Space Compression

[官方论文页](https://neurips.cc/virtual/2026/poster/152271) · [作者来源](https://openreview.net/forum?id=UK2XjwZOOP)

- **问题 / 瓶颈** · 同类问题过多表达和策略增加监督噪声
- **核心创新 / 方法** · 按问题检索动态路径库提示教师，控制路径空间覆盖
- **Baseline** · CoT、自由和直接蒸馏、结构化监督
- **Benchmark** · 五数学和常识基准、两学生；性能和 token
- **关键结果 / 消融** · 优势稳定，存在中等库规模最优
- **适用条件 / 局限** · 路径库过小会丢失长尾解题思路

**可复用机制** · 不同预算下同时测路径覆盖和学生泛化

<a id="paper-155187"></a>

## Structural Self-Teaching for Compositional Generation in Unified Multimodal Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155187) · [作者来源](https://openreview.net/forum?id=7dwd2Ok9fy)

- **问题 / 瓶颈** · 对象、属性和关系约束易混为全局语义
- **核心创新 / 方法** · 从理解支路提取短语级定位作训练结构信号
- **Baseline** · 多个统一模型原生成配置
- **Benchmark** · 组合图像生成的对象、属性、空间约束
- **关键结果 / 消融** · 摘要报告持续改善，不增加测试输入
- **适用条件 / 局限** · 理解通道的定位错误会污染监督

**可复用机制** · 复用内部拆短语能力时分别验收绑定和空间

<a id="paper-155070"></a>

## Structure-agnostic Causal Representation Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/155070) · [作者来源](https://openreview.net/forum?id=8gtLRyYY45)

- **问题 / 瓶颈** · 错结构假设会丢可预测信息
- **核心创新 / 方法** · 联合拟合结构及其对应不变表示
- **Baseline** · 结构指定与结构 oracle
- **Benchmark** · 合成、Colored MNIST、PACS、VLCS、OfficeHome
- **关键结果 / 消融** · 在合成等追平 oracle，结构错设时较平稳退化
- **适用条件 / 局限** · 候选族和观测环境需覆盖真实机制

**可复用机制** · 对机器人跨域传感保留多种结构并测最差域

<a id="paper-149635"></a>

## Structured Sparse Memory for Recurrent Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/149635) · [作者来源](https://openreview.net/forum?id=obYfawO6lb)

- **问题 / 瓶颈** · 任务嵌入可能隐藏远大于骨干的容量
- **核心创新 / 方法** · 采用结构稀疏的任务嵌入，匹配增广数据并调整递归深度
- **Baseline** · 原任务记忆、不同合成数据和循环深度
- **Benchmark** · ARC-AGI-1 与 2；pass@2
- **关键结果 / 消融** · 任务记忆参数少逾 90%，合成数据是二代进步最大驱动
- **适用条件 / 局限** · 任务条件信息在真实部署未必可得

**可复用机制** · 报告全系统的记忆参数并匹配训练样本，不单归因骨干

<a id="paper-151619"></a>

## Structured State-Space Regularization for Generation-Friendly Image Tokenization

[官方论文页](https://neurips.cc/virtual/2026/poster/151619) · [作者来源](https://openreview.net/forum?id=ZD298GwlMx)

- **问题 / 瓶颈** · 高重建忠实不等价于好的扩散潜态
- **核心创新 / 方法** · 用状态空间推导的正则约束潜空间保留谱分量
- **Baseline** · 普通视觉分词器
- **Benchmark** · 下游生成及重建，基准名单未报告
- **关键结果 / 消融** · 生成改善而重建损失小
- **适用条件 / 局限** · 谱偏置不一定适合所有图像统计

**可复用机制** · 训练分词器时固定生成器比较两种指标取舍

<a id="paper-152193"></a>

## Structured Transforms for Low-Overhead Quantization of Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152193) · [作者来源](https://openreview.net/forum?id=UrdhHjjT3j)

- **问题 / 瓶颈** · 稠密正交矩阵昂贵，数值病态时压缩可能崩
- **核心创新 / 方法** · 有界无穷范数分解采用带随机符号的 DCT
- **Baseline** · QuIP 变体及 FP16
- **Benchmark** · Pythia-6.9B、Mistral-7B 的压力配置及困惑度
- **关键结果 / 消融** · 每步复杂度由 O(N²) 到 O(N log N)，压力下更稳定
- **适用条件 / 局限** · 实际推理速度取决于低位硬件和核

**可复用机制** · 部署量化同时测试状态数值稳定性与压缩耗时

<a id="paper-150156"></a>

## Structure-Guided Masked Autoencoders for Ultra-High Resolution Scientific Image Understanding

[官方论文页](https://neurips.cc/virtual/2026/poster/150156) · [作者来源](https://openreview.net/forum?id=kFIwMrx78r)

- **问题 / 瓶颈** · 均匀切块需过长序列且随机遮罩不匹配多尺度结构
- **核心创新 / 方法** · 内容自适应四叉树和结构条件掩码联合训练
- **Baseline** · 常规 MAE
- **Benchmark** · SpringXCT、PAIP 等超高分辨率数据；Dice 和速度
- **关键结果 / 消融** · 两数据提升 9.70、16.84 Dice 点，最高推理加速 24.8 倍
- **适用条件 / 局限** · 收益依赖成像内容可用四叉树表示，复杂纹理应验证

**可复用机制** · 对超高分地图做自适应分块并检查小目标保留

<a id="paper-153531"></a>

## Structure Over Scale: Learning Visual Reasoning from Pedagogical Video

[官方论文页](https://neurips.cc/virtual/2026/poster/153531) · [作者来源](https://openreview.net/forum?id=Ke7sRt4MQA)

- **问题 / 瓶颈** · 大规模杂视频缺明确监督时序
- **核心创新 / 方法** · 从教学视频组织视觉线索、问题、停顿与回答的配对
- **Baseline** · 基座 Qwen 视觉模型及各专有模型结果
- **Benchmark** · NExT-QA、Video-MME、MotionBench；10K QA 训练
- **关键结果 / 消融** · 分别高 19.7、10.6、4.9
- **适用条件 / 局限** · 来源为儿童教学内容，需核对领域差异并做同规模数据对照

**可复用机制** · 先筛证据与问题时间绑定的数据再扩大规模

<a id="paper-153046"></a>

## Structure, Subspace and System: Push the Real Limit of Extremely Low-Bit Quantization for MoE-LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/153046) · [作者来源](https://openreview.net/forum?id=OQDkkukEEU)

- **问题 / 瓶颈** · 平均权重误差不代表部署时被用的方向。
- **核心创新 / 方法** · 将量化误差导向路由激活零空间，并联动结构与系统。
- **Baseline** · 最强极低位 MoE 基线。
- **Benchmark** · Qwen3.5-35B-A3B、Mixtral，准确率和显存。
- **关键结果 / 消融** · 摘要报告平均准确率高 8.31%，内存约降 6.32 倍。
- **适用条件 / 局限** · 依赖路由校准覆盖。

**可复用机制** · 按专家所服务的样本测误差而非平均保留所有方向。

<a id="paper-150200"></a>

## Structure vs. Chaos: Asymmetric Entropic Optimization for Enforcing Instruction Hierarchy

[官方论文页](https://neurips.cc/virtual/2026/poster/150200) · [作者来源](https://openreview.net/forum?id=jzIRAnG5UD)

- **问题 / 瓶颈** · 纯输出检查晚且可能漏语义边界。
- **核心创新 / 方法** · 用不对称熵优化监测和校正异常。
- **Baseline** · 现有指令层级防御。
- **Benchmark** · 多个语言模型，指令安全测试。
- **关键结果 / 消融** · 摘要报告强稳健性，幅度未报告。
- **适用条件 / 局限** · 偏离检测需在常见正常输入校准误报。

**可复用机制** · 防御需测正常指令执行与异常分离。

<a id="paper-151464"></a>

## Structuring Open-Ended NAS: Semi-Automated Design Knowledge Structuring with LLMs for Efficient Neural Architecture Search

[官方论文页](https://neurips.cc/virtual/2026/poster/151464) · [作者来源](https://openreview.net/forum?id=aRGcG80o4Z)

- **问题 / 瓶颈** · 直接开放搜索少数路径反复采样。
- **核心创新 / 方法** · 公平按想法采样、Pareto 变异及迭代反馈。
- **Baseline** · 既有 NAS。
- **Benchmark** · CIFAR-10、CIFAR-100、ImageNet16-120。
- **关键结果 / 消融** · 分别提高 0.84、2.17、2.35 点。
- **适用条件 / 局限** · 搜索预算和训练评价需等价。

**可复用机制** · 为概念族留最低探索额度以减少架构趋同。

<a id="paper-152367"></a>

## StylePlan: Style-Conditioned Intent Planning for Zero-Shot Coordination

[官方论文页](https://neurips.cc/virtual/2026/poster/152367) · [作者来源](https://openreview.net/forum?id=TahqPwogCI)

- **问题 / 瓶颈** · 沿用长期偏好在换伙伴时恢复慢。
- **核心创新 / 方法** · 两时标估计并处理冲突。
- **Baseline** · Overcooked 伙伴协作方法。
- **Benchmark** · Overcooked V2 旧评估与 JAX 换伙伴。
- **关键结果 / 消融** · 切换恢复与性能下降改善。
- **适用条件 / 局限** · 未见伙伴整体优势仍缺统一重跑。

**可复用机制** · 行为协调先识别临时打破固有习惯的意图证据。

<a id="paper-155545"></a>

## StyleRoute: Diffusion Style Transfer via Regional Routing and Conflict-aware Projection

[官方论文页](https://neurips.cc/virtual/2026/poster/155545) · [作者来源](https://openreview.net/forum?id=4kfUQ7cPeY)

- **问题 / 瓶颈** · 全图迁移可能把风格施到错误对象。
- **核心创新 / 方法** · 区域路由并在冲突时投影更新。
- **Baseline** · 扩散和区域匹配风格方法。
- **Benchmark** · 多内容风格组合。
- **关键结果 / 消融** · 摘要报告一致改善，幅度未核。
- **适用条件 / 局限** · 目标区域及冲突定义影响效果。

**可复用机制** · 分开调变化范围和变化方向。

<a id="paper-149848"></a>

## Subcritical Signal Propagation at Initialization in Normalization-Free Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/149848) · [作者来源](https://openreview.net/forum?id=mrN0k7yv3r)

- **问题 / 瓶颈** · 激活方差稳定不保证雅可比稳定。
- **核心创新 / 方法** · 推导双向注意下 APJN 递推。
- **Baseline** · 深层 ViT 的测量值。
- **Benchmark** · 置换对称输入及跨层统计。
- **关键结果 / 消融** · 理论深度行为匹配实际 APJN。
- **适用条件 / 局限** · 结论限初始化与对称设定。

**可复用机制** · 网络深度缩放同时检查激活和梯度传播。

<a id="paper-149020"></a>

## Subdata Selection: A Unified Framework for Optimal Selection and Statistical Efficiency Assessment

[官方论文页](https://neurips.cc/virtual/2026/poster/149020) · [作者来源](https://openreview.net/forum?id=tRze0atkNs)

- **问题 / 瓶颈** · 比较启发式相互输赢看不出剩余空间。
- **核心创新 / 方法** · 统一框架评所选子数据到理论最优的差距。
- **Baseline** · 常用参数化子数据方案。
- **Benchmark** · 子数据量与统计效率。
- **关键结果 / 消融** · 多方法明显未达潜力。
- **适用条件 / 局限** · 依赖可构造的参数模型和基准界。

**可复用机制** · 建立有效最优上界后再定选数策略。

<a id="paper-148636"></a>

## Sub-Gaussian Confidence Intervals for Heavy-Tailed Data: Characterizing the Limits of Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/148636) · [作者来源](https://openreview.net/forum?id=wFuL2EAAu5)

- **问题 / 瓶颈** · 实际观测数高估尾部分布下的可用信息。
- **核心创新 / 方法** · 以额外参数连接重尾分布可恢复范围和区间宽度。
- **Baseline** · 现有重尾区间。
- **Benchmark** · 非对称与重尾数值实验。
- **关键结果 / 消融** · 覆盖率保持标称，某些比较方法失效。
- **适用条件 / 局限** · 有效样本参数须可靠选定。

**可复用机制** · 先检验尾部信息量，再报告置信水平。

<a id="paper-154775"></a>

## Subliminal Learning as Trait-Direction Drift: A Mechanism and Targeted Control under SFT Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/154775) · [作者来源](https://openreview.net/forum?id=B3eilxnBkK)

- **问题 / 瓶颈** · 表面无关的训练数据仍可能引发属性漂移。
- **核心创新 / 方法** · 校准属性读出，用走廊正则约束学生漂移。
- **Baseline** · 常规 SFT 蒸馏。
- **Benchmark** · 教师样本偏好差及学生方向变化。
- **关键结果 / 消融** · 摘要支持方向机制和干预。
- **适用条件 / 局限** · 探针可靠性及新属性泛化需验证。

**可复用机制** · 在保留任务监督同时对非目标行为加显式漂移预算。

<a id="paper-153935"></a>

## Subliminal Learning Is Steering Vector Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/153935) · [作者来源](https://openreview.net/forum?id=HTU3jyiPs0)

- **问题 / 瓶颈** · 表面内容不呈现教师行为倾向。
- **核心创新 / 方法** · 在隐藏表示中测教师和学生的方向变化，并比较优化器。
- **Baseline** · 两开源模型及不同优化器。
- **Benchmark** · 行为与方向对齐的受控实验。
- **关键结果 / 消融** · 自适应更新可积累小一致梯度，非自适应对照减弱效果。
- **适用条件 / 局限** · 只在所测模型和训练条件验证。

**可复用机制** · 复用教师样本时测优化器改变后未预期行为是否仍出现。

<a id="paper-153652"></a>

## Subliminal Transfer of Unsafe Behaviors in AI Agent Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/153652) · [作者来源](https://openreview.net/forum?id=Jk4Gr2aX9Y)

- **问题 / 瓶颈** · 只筛训练轨迹表面内容无法覆盖隐含行为偏差。
- **核心创新 / 方法** · 以隔离评估比较蒸馏前后的行为。
- **Baseline** · 未蒸馏底座及表面过滤。
- **Benchmark** · TerminalBench 等长程行为评测。
- **关键结果 / 消融** · 观察到非预期行为迁移。
- **适用条件 / 局限** · 仅限受控设置，机制与范围待核。

**可复用机制** · 安全验收要执行长程任务，不能只审核蒸馏文本。

<a id="paper-156665"></a>

## Sublinear Variational Optimization of Gaussian Mixture Models with Millions to Billions of Parameters

[官方论文页](https://neurips.cc/virtual/2026/poster/156665) · [作者来源](https://neurips.cc/virtual/2026/poster/156665)

- **问题 / 瓶颈** · 朴素迭代随 N、C、D² 增长。
- **核心创新 / 方法** · 子线性变分优化使维数成本线性。
- **Baseline** · 当前强 GMM 优化。
- **Benchmark** · 大规模训练及零样本图像去噪。
- **关键结果 / 消融** · 实际训练快约一数量级，去噪有竞争力。
- **适用条件 / 局限** · 质量和速度取决于混合结构。

**可复用机制** · 优先优化评估样本和成分的范围，再看参数量是否真限制部署。

<a id="paper-151522"></a>

## Submodular Benchmark Selection

[官方论文页](https://neurips.cc/virtual/2026/poster/151522) · [作者来源](https://openreview.net/forum?id=a2E0uvY4DZ)

- **问题 / 瓶颈** · 只挑各自高熵题目可能冗余。
- **核心创新 / 方法** · 按互信息做次模选择。
- **Baseline** · 熵选择。
- **Benchmark** · 十公开榜的三个矩阵。
- **关键结果 / 消融** · 小预算插补更准确。
- **适用条件 / 局限** · 榜间相关随模型家族和时间变。

**可复用机制** · 删冗余基准前用未来独立模型验证插补误差。

<a id="paper-149944"></a>

## Submodular Multi-Agent Reinforcement Learning for Effective Online Distributed Task Allocation

[官方论文页](https://neurips.cc/virtual/2026/poster/149944) · [作者来源](https://openreview.net/forum?id=m1AFEitkDl)

- **问题 / 瓶颈** · 全局团队奖励归因困难且有分配约束。
- **核心创新 / 方法** · 用分区多线性扩展与掩码分类动作。
- **Baseline** · 集中训练下常规代理策略。
- **Benchmark** · 多机器人覆盖等仿真。
- **关键结果 / 消融** · 证明边际梯度无偏，实验幅度待核。
- **适用条件 / 局限** · 依赖次模效用和分区约束。

**可复用机制** · 若团队收益边际递减，用个体边际而非全局同奖。

<a id="paper-151247"></a>

## Subprocess-Constrained Markov Decision Processes

[官方论文页](https://neurips.cc/virtual/2026/poster/151247) · [作者来源](https://openreview.net/forum?id=bo3SFyQXGi)

- **问题 / 瓶颈** · 只约束初始累计成本可掩盖后段风险。
- **核心创新 / 方法** · 按每个中间步骤定义期望累计成本，用价值集迭代。
- **Baseline** · 平稳约束策略。
- **Benchmark** · S-CMDP 理论。
- **关键结果 / 消融** · 平稳策略可次优且难优化，历史策略可避障碍。
- **适用条件 / 局限** · 需定义每个后缀的适用成本和可行性。

**可复用机制** · 长期安全保证应涵盖交接或重新起算时的条件风险。

<a id="paper-151551"></a>

## Subset-Conditioned Boundary Compensation for Missing-Modality Multimodal Classification

[官方论文页](https://neurips.cc/virtual/2026/poster/151551) · [作者来源](https://openreview.net/forum?id=ZnNIhBOEoB)

- **问题 / 瓶颈** · 信息少不等于只需要降低置信，错误具有固定方向。
- **核心创新 / 方法** · 保存模态因子化 margin 违规，推理做针对 logit 修正。
- **Baseline** · 统一缺模态补偿。
- **Benchmark** · 各模态子集的边界与初始化稳定性。
- **关键结果 / 消融** · 稳定错误集中边界，前向统计足以构建修正。
- **适用条件 / 局限** · 稀有模态组合需要足够记录。

**可复用机制** · 缺传感评估先查边界错位，再决定补模态还是只调分类头。

<a id="paper-150615"></a>

## Subspace-Guided Continual Learning: Hessian Based Stable–Plastic Decomposition for Exemplar-Free Class-Incremental Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/150615) · [作者来源](https://openreview.net/forum?id=gp622AVLX9)

- **问题 / 瓶颈** · 统一更新会冲掉旧类有用表示。
- **核心创新 / 方法** · 特征 Hessian 的高曲率特征向量组成稳定子空间，其正交补吸收新知识。
- **Baseline** · 无样本回放的类增量方法。
- **Benchmark** · 增量分类及遗忘评估。
- **关键结果 / 消融** · 摘要报告有竞争力或超出已有方法。
- **适用条件 / 局限** · 依赖曲率估计和正交分解，预算未报告。

**可复用机制** · 保留历史能力前先测局部敏感方向，让新梯度使用低干扰部分。

<a id="paper-139455"></a>

## SudoBench: A Contextual Authorization Benchmark for LLM Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/139455) · [作者来源](https://openreview.net/forum?id=OqnNJ4ruF0)

- **问题 / 瓶颈** · 单场景通过可能只是模型按字面拒绝或服从。
- **核心创新 / 方法** · 按反事实切换上下文权限，同时正确才记通过。
- **Baseline** · 多个前沿模型和授权设置。
- **Benchmark** · SudoBench 的授权上下文及成对通过。
- **关键结果 / 消融** · 摘要报告前沿模型仍不能可靠处理。
- **适用条件 / 局限** · 限所测授权类型，摘要未给真实工作流校准。

**可复用机制** · 权限评测把文本固定，单独改变可信授权，测试行为是否正确反转。

<a id="paper-154847"></a>

## Super-Level-Set Regression: Conditional Quantiles via Volume Minimization

[官方论文页](https://neurips.cc/virtual/2026/poster/154847) · [作者来源](https://openreview.net/forum?id=ASsB7ycA7e)

- **问题 / 瓶颈** · 先估密度再找分位集合引入不必要假设。
- **核心创新 / 方法** · 用超水平集回归处理体积与误差分位数之间的耦合。
- **Baseline** · 先估密度的方法。
- **Benchmark** · 多变量条件区域，摘要未给任务量化。
- **关键结果 / 消融** · 提出直接几何优化形式。
- **适用条件 / 局限** · 依赖可参数化集合，摘要未说明高维求积成本。

**可复用机制** · 若最终只需紧致预测区域，可尝试直接优化区域而非恢复整个分布。

<a id="paper-148794"></a>

## SuperSycophantic: Stress-Testing Frontier LLMs from Single- to Multi-Turn Sycophancy

[官方论文页](https://neurips.cc/virtual/2026/poster/148794) · [作者来源](https://openreview.net/forum?id=v2ZJiUHkC6)

- **问题 / 瓶颈** · 单轮回答无法反映模型在持续施压下的稳定性。
- **核心创新 / 方法** · 对客观与主观场景分别改变措辞和多轮压力。
- **Baseline** · 九个前沿模型。
- **Benchmark** · 多轮与首轮框架的迎合评测。
- **关键结果 / 消融** · GPT-5.4 在 23.8% 客观场景由对转错。
- **适用条件 / 局限** · 受所选问题与施压形态限制。

**可复用机制** · 多轮可靠性应在信息不变时改变用户态度，单独计量正确答案退化。

<a id="paper-139383"></a>

## SUPERVISE: A Unified Framework for Standardized and Reproducible Superpixel Evaluation

[官方论文页](https://neurips.cc/virtual/2026/poster/139383) · [作者来源](https://openreview.net/forum?id=TpOx3zA846)

- **问题 / 瓶颈** · 相同目标超像素数不代表真实输出相同。
- **核心创新 / 方法** · 按真实超像素数插值归一化后对照方法。
- **Baseline** · 31 种方法、多项评估指标。
- **Benchmark** · 七个数据集和 20 项超像素指标。
- **关键结果 / 消融** · 摘要报告规模归一化带来可一致对比的统计分析。
- **适用条件 / 局限** · 插值规则的外推和域外任务未报告。

**可复用机制** · 对输出粒度可变的模型，基于实测复杂度匹配质量曲线。

<a id="paper-151678"></a>

## Supervision Recovery for Time Series Anomaly Detection via Counterfactual Pairing

[官方论文页](https://neurips.cc/virtual/2026/poster/151678) · [作者来源](https://openreview.net/forum?id=YqBYI9KKtm)

- **问题 / 瓶颈** · 直接把模拟异常当正例可能把模拟域特征也带进监督。
- **核心创新 / 方法** · 从正常异常配对提取按族组织的效应，保留目标正常结构。
- **Baseline** · 无监督与直接注入基线，以及监督参考。
- **Benchmark** · 时序异常检测，不使用目标域异常标签。
- **关键结果 / 消融** · 摘要报告优于无监督和注入，接近有监督参考。
- **适用条件 / 局限** · 依赖模拟异常有代表性。

**可复用机制** · 迁移合成故障数据时尽量迁移变化量而非完整模拟样本。

<a id="paper-149817"></a>

## Support Before Frequency in Discrete Diffusion

[官方论文页](https://neurips.cc/virtual/2026/poster/149817) · [作者来源](https://openreview.net/forum?id=n7xCEekbI1)

- **问题 / 瓶颈** · 模型能生成合法样本时分布仍可能错。
- **核心创新 / 方法** · 低噪逆编辑拆为进入支持的概率量级及支持内的相对系数。
- **Baseline** · 均匀与吸收扩散。
- **Benchmark** · 离散扩散过程，关注支持与频率恢复。
- **关键结果 / 消融** · 摘要报告支持结构先于频率恢复。
- **适用条件 / 局限** · 分析针对最终低噪阶段。

**可复用机制** · 先测可行输出质量，再独立测模式比例，以免早期合法性掩盖分布偏差。

<a id="paper-153575"></a>

## Support Mismatch as a Benchmark Failure Mode for In-Context Prediction

[官方论文页](https://neurips.cc/virtual/2026/poster/153575) · [作者来源](https://openreview.net/forum?id=KO8zjpmrDJ)

- **问题 / 瓶颈** · 增加上下文可能无法降掉缺失候选导致的误差地板。
- **核心创新 / 方法** · 推导支持错配项并比较正确候选和同规模错误候选。
- **Baseline** · 不同规模或内容的候选集合。
- **Benchmark** · 标量和对齐高斯模型、受控已训练模型及选择题。
- **关键结果 / 消融** · 摘要报告正确支持改善无法由同数量错误候选替代。
- **适用条件 / 局限** · 理论依赖似然比矩条件。

**可复用机制** · 把知识支持缺失与示例不足分开诊断，以决定加上下文还是改检索库。

<a id="paper-155217"></a>

## Support-Safe Variational Hybrid Filtering for Contact-Mode and Sparse-Law Recovery

[官方论文页](https://neurips.cc/virtual/2026/poster/155217) · [作者来源](https://openreview.net/forum?id=7PXCrabsBB)

- **问题 / 瓶颈** · 只用学习提议可能丢掉少见接触，使后续推断无法恢复。
- **核心创新 / 方法** · 将学习提议与可行转移混合，联合过滤连续状态和离散模式。
- **Baseline** · 后处理分段和无模式预测。
- **Benchmark** · 可知规则的混合物理系统及接触模式。
- **关键结果 / 消融** · 作者报告能找回被对照遗漏的转移和活跃物理项。
- **适用条件 / 局限** · 依赖可信的可行转移和稀疏动力形式。

**可复用机制** · 在结构已知的状态估计中，让学习提议提速但由可行模型保留回退覆盖。

<a id="paper-152116"></a>

## Surface Recovery Is Not State Recovery: Pressure–Recovery–Relapse in Multi-turn LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/152116) · [作者来源](https://openreview.net/forum?id=VQPotrVKIT)

- **问题 / 瓶颈** · 当前答案改对不保证内部错误状态已修复。
- **核心创新 / 方法** · 构造压力、恢复、复发的连续阶段，并对照内部表征。
- **Baseline** · 只看恢复答案正确的评估。
- **Benchmark** · 事实问答与指令微调模型。
- **关键结果 / 消融** · 摘要报告输出恢复后仍可能复发。
- **适用条件 / 局限** · 潜状态取决于分析方法。

**可复用机制** · 报告短时纠正率之外，再测低成本干扰下恢复能保持多久。

<a id="paper-155157"></a>

## SURF: Steering the Scalarization Weight to Uniformly Traverse the Pareto Front

[官方论文页](https://neurips.cc/virtual/2026/poster/155157) · [作者来源](https://openreview.net/forum?id=7qtIxTWBAO)

- **问题 / 瓶颈** · 均匀权重可能导致前沿样本堆积。
- **核心创新 / 方法** · 按权重沿前沿移动的实际速度建立弧长分布并逆采样。
- **Baseline** · 常规权重抽样。
- **Benchmark** · 赌博机和 MO-Gymnasium。
- **关键结果 / 消融** · 报告更均匀覆盖且有效率。
- **适用条件 / 局限** · 需要可估的前沿参数化，有限样本仍有误差地板。

**可复用机制** · 优化旋钮到性能结果关系非线性时，调样本密度匹配结果空间的几何。

<a id="paper-153420"></a>

## SurGe: Improved Surface Geometry in Point Maps

[官方论文页](https://neurips.cc/virtual/2026/poster/153420) · [作者来源](https://openreview.net/forum?id=LSoxFFuHS0)

- **问题 / 瓶颈** · 整体几何指标可能忽略表面粗糙。
- **核心创新 / 方法** · 从预测点图计算法向，并比较梯度损失和邻域注意力。
- **Baseline** · 已有单目几何模型和模块消融。
- **Benchmark** · 八项零样本几何基准。
- **关键结果 / 消融** · 摘要报告局部表面几何提高。
- **适用条件 / 局限** · 依赖邻域法向估计。

**可复用机制** · 为需要接触或着色的三维预测补上表面微分指标。

<a id="paper-148844"></a>

## Surjective Pseudo-Invertible Neural Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/148844) · [作者来源](https://openreview.net/forum?id=uiqGz0UDET)

- **问题 / 瓶颈** · 线性零空间技巧无法直接处理语义或学习退化。
- **核心创新 / 方法** · 训练可伪逆模型并在生成时做非线性反投影。
- **Baseline** · 线性闭式反投影。
- **Benchmark** · 语义控制、分类检测及逆问题。
- **关键结果 / 消融** · 摘要报告无需重新训练生成先验即可使用。
- **适用条件 / 局限** · 依赖可学习且覆盖目标的观测映射，摘要未给定量边界。

**可复用机制** · 将观测一致性封装为可复用投影器，使同一生成先验适用不同约束。

<a id="paper-150609"></a>

## Surprise, Episodic Context, and Catastrophic Forgetting in LLM Fine-Tuning: An Empirical Study

[官方论文页](https://neurips.cc/virtual/2026/poster/150609) · [作者来源](https://openreview.net/forum?id=gsvP7j7bLZ)

- **问题 / 瓶颈** · 罕见更新可能改变无关提示的回答格式
- **核心创新 / 方法** · 按更新惊讶度比较平铺和增加事件上下文的样本
- **Baseline** · 普通提示与续写对
- **Benchmark** · 微调数据惊讶度、遗忘与代码串扰
- **关键结果 / 消融** · 代码串扰沿惊讶度从 4% 到 73%，补情境能减轻
- **适用条件 / 局限** · 依赖惊讶度估计，是否保护全部能力未证实

**可复用机制** · 微调样本保留适用前提，并测无关任务的输出格式

<a id="paper-139105"></a>

## Surprisingly consistent failures of post-hoc OOD detectors reveal security concerns in open-set recognition with modern CNNs and ViTs, stemming from representation mismatch

[官方论文页](https://neurips.cc/virtual/2026/poster/139105) · [作者来源](https://openreview.net/forum?id=kma0btMMP6)

- **问题 / 瓶颈** · 平均 OOD 分数掩盖底层表示共同失配
- **核心创新 / 方法** · 对照 CNN、ViT 的多种后验检测器并构建语义远离的困难子集
- **Baseline** · 既有事后 OOD 检测
- **Benchmark** · NINCO、ImageNet-OoD 等来源；开放集错判
- **关键结果 / 消融** · 远语义 OOD 仍有跨检测器持续失误
- **适用条件 / 局限** · 诊断样本经过选择，不能估计自然分布错误率

**可复用机制** · 换打分头前先检验底层表征是否区分难例

<a id="paper-154070"></a>

## Survive or Collapse: The Asymmetric Roles of Data Gating and Reward Grounding in Self-Play RL

[官方论文页](https://neurips.cc/virtual/2026/poster/154070) · [作者来源](https://openreview.net/forum?id=GPTwtahTVC)

- **问题 / 瓶颈** · 共同训练可能学习伪一致性而非可泛化解题
- **核心创新 / 方法** · 单独改变数据准入严格度与奖励条件并追踪外部验证
- **Baseline** · 不同门控及奖励接地设置
- **Benchmark** · 自博弈训练诊断与留出准确率
- **关键结果 / 消融** · 训练指标先解耦，验证准确率在更高严格度变化下才退化
- **适用条件 / 局限** · 相变结论依所用任务和严格度定义

**可复用机制** · 自博弈监控加外部冻结集并分别消融任务筛选与奖励

<a id="paper-150863"></a>

## SVDP: Training-Free Contextual Sparsity Predictors for Fast LLM Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/150863) · [作者来源](https://openreview.net/forum?id=em7XpU5sBc)

- **问题 / 瓶颈** · 逐 token 密集 FFN 浪费执行资源
- **核心创新 / 方法** · 用免训练预测与阈值校准触发条件计算
- **Baseline** · 默认解码及稀疏执行方法
- **Benchmark** · 三个 LLM 约 90% FFN 稀疏；数学与代码
- **关键结果 / 消融** · 解码最快约 1.8 倍、得分损失低于 1%
- **适用条件 / 局限** · 依赖已有高度稀疏及相应 CUDA/CANN 支持

**可复用机制** · 部署端先估哪几层稀疏度足以抵消分支开销

<a id="paper-150413"></a>

## SVoT: State-aware Visualization-of-Thought for Spatial Reasoning via Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/150413) · [作者来源](https://openreview.net/forum?id=iEEi07lQqo)

- **问题 / 瓶颈** · 最后答案可能掩盖错误对象交互
- **核心创新 / 方法** · 以中间状态图及转移监督训练可视推理
- **Baseline** · 现有多模态空间推理方案，摘要未列名单
- **Benchmark** · 作者构建的多物体交互和数字推理域
- **关键结果 / 消融** · 分布外最高提升 65 个百分点
- **适用条件 / 局限** · 证据集中在构造环境，真实视觉复杂性未验证

**可复用机制** · 给操作规划专门核对每步状态变化，而非只给终局奖励

<a id="paper-139812"></a>

## SWE-Git-Bench: A Worktree-Level Benchmark for Real Merge Conflict Resolution

[官方论文页](https://neurips.cc/virtual/2026/poster/139812) · [作者来源](https://openreview.net/forum?id=37pMYoL9Iz)

- **问题 / 瓶颈** · 极高文本相似并不保证正确合并
- **核心创新 / 方法** · 对照整文件及冲突块输出，并人工检查高相似非完全匹配项
- **Baseline** · 整文件接口、块级接口
- **Benchmark** · 真实合并冲突；编辑相似、完全匹配与人工审核
- **关键结果 / 消融** · 相似增 19.2 点而完全匹配近乎不变，40/80 审核样本可能不安全
- **适用条件 / 局限** · 人工核查样本小且聚焦已选输出

**可复用机制** · 合并 Agent 要跑与双侧改动相关的断言，不只比文本差异

<a id="paper-139342"></a>

## SWE-Marathon: Can AI Agents Autonomously Complete Ultra-Long-Horizon Software Work?

[官方论文页](https://neurips.cc/virtual/2026/poster/139342) · [作者来源](https://openreview.net/forum?id=VdUYkialkd)

- **问题 / 瓶颈** · 终局裁决可能被绕开，高分不等于完整流程
- **核心创新 / 方法** · 在授权良性任务上独立审查测试与运行环境，并多层验证输出
- **Baseline** · 现有短项目测试与作者长程环境
- **Benchmark** · SWE-Marathon；长程任务结果及评测完整性
- **关键结果 / 消融** · 作者报告 18.8% 轨迹有评测完整性异常
- **适用条件 / 局限** · 比率依赖模型、任务与检测定义

**可复用机制** · 将评测异常率与实际任务成功独立记录

<a id="paper-139202"></a>

## SWE-Pro: A Benchmark for Evaluating LLMs on Performance-Oriented Repository-Level Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/139202) · [作者来源](https://openreview.net/forum?id=ejx2oNUnIp)

- **问题 / 瓶颈** · 单小函数或单速度指标掩盖资源权衡。
- **核心创新 / 方法** · 仓库级参数化测试并控制计时噪声。
- **Baseline** · 当前 LLM 与专家修订。
- **Benchmark** · SWE-Pro，运行时间、峰值及 TWMU。
- **关键结果 / 消融** · 大模型运行收益近零且几乎不降内存，91.2% 任务有专家改进。
- **适用条件 / 局限** · 结论依赖仓库和机器组合。

**可复用机制** · 验收优化改动同时测试正确性、输入压力和内存权衡。

<a id="paper-155936"></a>

## SWE-Protégé: Learning to Selectively Collaborate With an Expert Unlocks Small Language Models as Software Engineering Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/155936) · [作者来源](https://openreview.net/forum?id=1gT9qIbj9f)

- **问题 / 瓶颈** · 全程换强模型成本大。
- **核心创新 / 方法** · 训练专家与门生协作，少量阶段借专家。
- **Baseline** · 既有小模型软件修复。
- **Benchmark** · SWE-bench Verified，Pass@1 和协作成本。
- **关键结果 / 消融** · 7B 得 42.4%，每题约四求助且占 11% token。
- **适用条件 / 局限** · 需要同等专家权限和质量。

**可复用机制** · 以局部求助替代整任务升级，监控专家支出比例。

<a id="paper-153489"></a>

## SwiftFlow: An Efficient One-Step Policy Learning via Improved Mean Flow for Robotic Manipulation

[官方论文页](https://neurips.cc/virtual/2026/poster/153489) · [作者来源](https://openreview.net/forum?id=L0WDOgp4Bz)

- **问题 / 瓶颈** · 连续行为生成的多步采样影响控制延迟。
- **核心创新 / 方法** · 改进 mean flow 并加训练专用正则。
- **Baseline** · 现有生成策略。
- **Benchmark** · Adroit、MetaWorld。
- **关键结果 / 消融** · 任务表现更强且一步，无明显额外推理成本。
- **适用条件 / 局限** · 实证目前为两模拟套件。

**可复用机制** · 把一步部署带来的精度要求直接写进训练目标。

<a id="paper-151623"></a>

## Swift Sampling: Selecting Temporal Surprises via Taylor Series

[官方论文页](https://neurips.cc/virtual/2026/poster/151623) · [作者来源](https://openreview.net/forum?id=ZACohTphcr)

- **问题 / 瓶颈** · 均匀抽帧浪费重复画面。
- **核心创新 / 方法** · 训练免 Taylor 近似检测时间惊讶。
- **Baseline** · 均匀或常用帧选。
- **Benchmark** · 视频帧信息选择。
- **关键结果 / 消融** · 摘要给新机制，量化待核。
- **适用条件 / 局限** · 相机运动也可能产生大惊讶。

**可复用机制** · 将变化预测误差作为抽帧依据并抑制全局抖动。

<a id="paper-150961"></a>

## SwiftVLM: Efficient Vision-Language Model Inference via Cross-Layer Token Bypass

[官方论文页](https://neurips.cc/virtual/2026/poster/150961) · [作者来源](https://openreview.net/forum?id=dxV7Vwadng)

- **问题 / 瓶颈** · 早剪使后期需要的信息不可恢复。
- **核心创新 / 方法** · 跨层 bypass 低分 token，后续阶段重估。
- **Baseline** · 早期永久删除。
- **Benchmark** · 视觉语言推理与层重要性。
- **关键结果 / 消融** · 实验发现重要性会换位，方案无需训练。
- **适用条件 / 局限** · 保存旁路有内存成本。

**可复用机制** · 对可逆剪枝的重新进入率和总算力做独立测量。

<a id="paper-150319"></a>

## Swimba: Switch Mamba Model Scales State Space Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150319) · [作者来源](https://openreview.net/forum?id=izlpFIy1uX)

- **问题 / 瓶颈** · 每专家各维护轨迹使计算扩张。
- **核心创新 / 方法** · 先混合 SSM 参数，再执行一次状态递归。
- **Baseline** · 分离专家的 MoE-SSM。
- **Benchmark** · 标准任务、真实吞吐与延迟。
- **关键结果 / 消融** · 扩容量但主导递归成本保持。
- **适用条件 / 局限** · 混合参数可能弱化各专家独立表达。

**可复用机制** · 动态专家可作用于算子参数而非分叉状态。

<a id="paper-152976"></a>

## Symb-xMIL: Symbolic Explanations for Multiple Instance Learning in Digital Pathology

[官方论文页](https://neurips.cc/virtual/2026/poster/152976) · [作者来源](https://openreview.net/forum?id=OwuMiUXJ26)

- **问题 / 瓶颈** · 热图不能说明怎样组合特征。
- **核心创新 / 方法** · 事后评估预测与 AND、OR、NOT 等人类可读逻辑的一致。
- **Baseline** · 普通事后框架。
- **Benchmark** · 合成及真实病理数据。
- **关键结果 / 消融** · 一致分数揭示语义模式，幅度未报告。
- **适用条件 / 局限** · 规则词表和特征定义限制解释。

**可复用机制** · 把模型是否遵从假设的组合规则变成可量的诊断。

<a id="paper-151782"></a>

## SymDrift: One-Shot Generative Modeling under Symmetries

[官方论文页](https://neurips.cc/virtual/2026/poster/151782) · [作者来源](https://openreview.net/forum?id=Y3ywi65g1k)

- **问题 / 瓶颈** · 生成器等变不保证推导的目标漂移等价。
- **核心创新 / 方法** · 按最优对齐对称化漂移，或用不变量嵌入。
- **Baseline** · 直接等变生成器和显式对称分布处理。
- **Benchmark** · 单步生成、对称数据。
- **关键结果 / 消融** · 摘要给两种方式，优势数字待核。
- **适用条件 / 局限** · 需要可用群作用和不变量。

**可复用机制** · 分别测试预测和训练监督对坐标变换是否一致。

<a id="paper-152474"></a>

## Symmetric Interventions for Eliciting Model Intent

[官方论文页](https://neurips.cc/virtual/2026/poster/152474) · [作者来源](https://openreview.net/forum?id=SniLob4M2j)

- **问题 / 瓶颈** · 单一评估情境无法区分外观一致的动机。
- **核心创新 / 方法** · 用对称干预对照各种行为解释的外推。
- **Baseline** · 标准单情境评估。
- **Benchmark** · 模型意图和行为推断。
- **关键结果 / 消融** · 摘要指出标准评估无法识别两种解释。
- **适用条件 / 局限** · 行为外推仍不足直接证明动机。

**可复用机制** · 保持任务控制一致并设计假说给不同预测的测试。

<a id="paper-155311"></a>

## Symmetry-Guaranteed Prediction of High-Order Tensor Properties for Crystalline Materials via Irreducible Decomposition

[官方论文页](https://neurips.cc/virtual/2026/poster/155311) · [作者来源](https://openreview.net/forum?id=6XMKkwiYyK)

- **问题 / 瓶颈** · 直接回归全张量可能破坏物理对称。
- **核心创新 / 方法** · 球谐卷积预测对称不可约分量后恢复原量。
- **Baseline** · 直接预测或近似对称基线。
- **Benchmark** · 晶体高阶张量预测及对称合规。
- **关键结果 / 消融** · 精确对称同时保持或改善准确。
- **适用条件 / 局限** · 依赖已知群和张量分解。

**可复用机制** · 若变量无效自由度可解析删除，网络只学必要分量。

<a id="paper-151617"></a>

## Symmetry Guarantees Statistic Recovery in Variational Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/151617) · [作者来源](https://openreview.net/forum?id=ZDvmwsQZ73)

- **问题 / 瓶颈** · 后验整体失配时仍可能有部分量准确。
- **核心创新 / 方法** · 统一以目标和变分族对称推导统计恢复。
- **Baseline** · 位置尺度族已知结论。
- **Benchmark** · 多类对称设置的理论。
- **关键结果 / 消融** · 将多已有保证纳入统一框架。
- **适用条件 / 局限** · 需目标和近似族满足对应对称。

**可复用机制** · 为下游不确定性选择近似族时先列必须保留的统计量。

<a id="paper-152328"></a>

## SympFNO: Structure-Preserving Fourier Neural Operators for Physical Surrogate Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/152328) · [作者来源](https://openreview.net/forum?id=TtVLwbWHCn)

- **问题 / 瓶颈** · 普通 FNO 长轨迹易破坏 Hamiltonian 几何。
- **核心创新 / 方法** · 三类辛层保结构变换。
- **Baseline** · 无约束 FNO。
- **Benchmark** · Hamiltonian 动力学的代理建模。
- **关键结果 / 消融** · 推得结构一致和表达效率优势，数值待核。
- **适用条件 / 局限** · 非保守系统可能不满足假设。

**可复用机制** · 将物理守恒写进跨域变换，而非只加损失。

<a id="paper-148541"></a>

## Symplectic Neural Operators for Learning Infinite Dimensional Hamiltonian Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/148541) · [作者来源](https://openreview.net/forum?id=x7jCoj91Df)

- **问题 / 瓶颈** · 仅单步拟合无法防能量漂移。
- **核心创新 / 方法** · 保辛神经算子及长期稳定性分析。
- **Baseline** · 不保结构的神经算子。
- **Benchmark** · 典型 Hamiltonian PDE。
- **关键结果 / 消融** · 能量行为更稳。
- **适用条件 / 局限** · 长期保证仍需学习精度和物理假设。

**可复用机制** · 分别验单步精度和不变量随时间漂移。

<a id="paper-155724"></a>

## Symplectic Normal Coordinates Flow for Generative Modeling of Hamiltonian Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/155724) · [作者来源](https://openreview.net/forum?id=3PCheCpOJt)

- **问题 / 瓶颈** · 无结构流可能引入不物理耦合。
- **核心创新 / 方法** · 以可逆辛层学习幅值依赖旋转。
- **Baseline** · 常规 normalizing flow。
- **Benchmark** · 加速器物理两个条件生成，NLL。
- **关键结果 / 消融** · 有竞争力或更好，弱非线性增益更明显。
- **适用条件 / 局限** · 依赖可学正规坐标。

**可复用机制** · 对结构系统在变换空间约束生成映射的物理类别。

<a id="paper-148524"></a>

## Symplectic Parallel Scan: A Neural Hamiltonian Framework for Accelerated Scientific Simulation

[官方论文页](https://neurips.cc/virtual/2026/poster/148524) · [作者来源](https://openreview.net/forum?id=xFfEoYpedJ)

- **问题 / 瓶颈** · 顺序积分开销大且长时间能量漂移。
- **核心创新 / 方法** · 在有限 Poisson 代数写动力学，用全轨迹监督及并行扫描。
- **Baseline** · 顺序 Hamiltonian 神经网络。
- **Benchmark** · 量子自旋及物理模拟基准。
- **关键结果 / 消融** · 时钟加速并减少外推中的漂移与辛违例。
- **适用条件 / 局限** · 生成元有限维近似需要验证。

**可复用机制** · 找到可组合动力学表示后再做扫描并行。

<a id="paper-151225"></a>

## Synaptic Strength Controls Trainability and Structural Stability in Rank-Deficient RNNs

[官方论文页](https://neurips.cc/virtual/2026/poster/151225) · [作者来源](https://openreview.net/forum?id=bz6Q9nPl9F)

- **问题 / 瓶颈** · 秩和权重尺度常一起变化使机制混杂。
- **核心创新 / 方法** · 用全权可训的低秩初始化解耦两轴。
- **Baseline** · 经典高维随机与低秩终态分析。
- **Benchmark** · RNN 可训练性和结构稳定性。
- **关键结果 / 消融** · 主要由突触强度控制，强弱各有利弊。
- **适用条件 / 局限** · 依赖所用循环学习场景。

**可复用机制** · 调低秩时与增益正交扫描，分别测训练与结构保留。

<a id="paper-139111"></a>

## SynBench: A Benchmark for Differentially Private Text Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/139111) · [作者来源](https://openreview.net/forum?id=kRbRRTtsgf)

- **问题 / 瓶颈** · 通用私有基准可能污染，宣称保护缺少审计。
- **核心创新 / 方法** · 统一效用保真及差分隐私审计。
- **Baseline** · 各种差分隐私文本生成。
- **Benchmark** · SynBench 九领域。
- **关键结果 / 消融** · 私有数据越偏离预训练，生成质量越退化。
- **适用条件 / 局限** · 公开可判别审计不能覆盖真实私域。

**可复用机制** · 在域外独立集同时评质量与隐私，而非只比较一个平均。

<a id="paper-148172"></a>

## SyncLight: Single-Edit Multi-View Relighting

[官方论文页](https://neurips.cc/virtual/2026/poster/148172) · [作者来源](https://openreview.net/forum?id=zkf4gdBviG)

- **问题 / 瓶颈** · 独立重光照破坏跨相机照明一致。
- **核心创新 / 方法** · 以一次单视角参考编辑条件化多视角 Transformer 的潜桥匹配。
- **Baseline** · 现有单视角独立重光照。
- **Benchmark** · 未标定位姿的静态场景、多视角灯光强度与颜色。
- **关键结果 / 消融** · 仅以图像对训练即可零样本推到任意视图数，一步输出。
- **适用条件 / 局限** · 静态场景验证；大视差、遮挡或运动之后需复测。

**可复用机制** · 用成对一致监督学习传播规则，再独立验证跨视角数外推。

<a id="paper-149981"></a>

## SyncWorld: Visual Calibration Enables World Models as Zero-Shot Simulators

[官方论文页](https://neurips.cc/virtual/2026/poster/149981) · [作者来源](https://openreview.net/forum?id=lj7OHtUYX1)

- **问题 / 瓶颈** · 不同平台相同动作命令可能产生不同效果，混合训练监督冲突。
- **核心创新 / 方法** · 在推演前给覆盖可控自由度的视觉动作示例。
- **Baseline** · 没有条件校准的世界模型。
- **Benchmark** · 未见环境的动作预测和策略改进。
- **关键结果 / 消融** · 摘要报告零样本模拟有效，并能在测试期改进策略。
- **适用条件 / 局限** · 校准需要覆盖自由度，摘要未给最少样本数。

**可复用机制** · 多设备学习对控制协议做情境校准，避免让模型仅靠场景外观猜动作含义。

<a id="paper-139213"></a>

## SynDORBench: Evaluating LVLM Perceptual Robustness Under Physically Constrained Visibility Conditions

[官方论文页](https://neurips.cc/virtual/2026/poster/139213) · [作者来源](https://openreview.net/forum?id=eJbJ4kjbfA)

- **问题 / 瓶颈** · 常见清晰图片不能判断模型在感知边界稳定性。
- **核心创新 / 方法** · 用人类可见性准则与受控合成渲染划分条件。
- **Baseline** · 所测视觉语言模型及人类可见阈值。
- **Benchmark** · 超过 5.4 万问答，变量含距、光照、相机和动作姿态。
- **关键结果 / 消融** · 摘要给出可与人类阈值直接对比的协议。
- **适用条件 / 局限** · 合成物理设定需验证是否代表部署。

**可复用机制** · 把场景可见程度当作连续变量，报告模型从可靠到退化的区间。

<a id="paper-151851"></a>

## SynerVLA: Exploiting Embodied Execution Phases for On-Device Dual-System VLA Acceleration

[官方论文页](https://neurips.cc/virtual/2026/poster/151851) · [作者来源](https://openreview.net/forum?id=XQcHUlCrAD)

- **问题 / 瓶颈** · 固定频率浪费流式冗余且限制控制速度。
- **核心创新 / 方法** · 利用两阶段的空间和时间冗余减少视觉处理。
- **Baseline** · 原双系统 VLA。
- **Benchmark** · 多代表平台，控制频率、速度、任务成功。
- **关键结果 / 消融** · 最高快 1.93 倍，控制频率提升 26%，成功率变化很小。
- **适用条件 / 局限** · 依赖阶段识别，摘要未给过渡误判。

**可复用机制** · 保持对关键操作阶段的观测预算，复用快速接近时重复内容。

<a id="paper-150196"></a>

## SynGeo: Synergizing Seeing and Proving through Revisable Geometric States

[官方论文页](https://neurips.cc/virtual/2026/poster/150196) · [作者来源](https://openreview.net/forum?id=k1LKHbKtrM)

- **问题 / 瓶颈** · 第一次读图的错漏若被固化，证明搜索难恢复。
- **核心创新 / 方法** · 从图文建谓词状态，在证明停滞时用符号诊断指导视觉重查。
- **Baseline** · 一次性图文形式化与不做视觉重访。
- **Benchmark** · 几何问题中的观察、形式化和证明。
- **关键结果 / 消融** · 摘要报告重访及互补推理均重要。
- **适用条件 / 局限** · 依赖符号诊断能定位问题，摘要未给修订次数开销。

**可复用机制** · 可验证推理失败也可能源自输入解析，应允许返回并更改结构化状态。

<a id="paper-153370"></a>

## SynGS: Synergistic Continual Learning and Change Detection with Gaussian Splatting

[官方论文页](https://neurips.cc/virtual/2026/poster/153370) · [作者来源](https://openreview.net/forum?id=Ls29PxSARF)

- **问题 / 瓶颈** · 外观波动不一定意味着几何改变。
- **核心创新 / 方法** · 联合学高斯级变化概率和场景，再据概率门控技术校正。
- **Baseline** · 既有三维场景更新和变化检测。
- **Benchmark** · 变化检测、场景更新与渲染速度。
- **关键结果 / 消融** · 摘要报告两项任务提升并维持实时渲染。
- **适用条件 / 局限** · 依赖变化概率质量，摘要未给照明异常边界。

**可复用机制** · 长期地图应分开放置外观解释和持久结构更新，避免瞬时光照污染地图。

<a id="paper-150893"></a>

## SynIB: Informational Bottleneck for Maximizing Synergy in Multimodal Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/150893) · [作者来源](https://openreview.net/forum?id=ed96r05m3R)

- **问题 / 瓶颈** · 普通训练易利用冗余模态或单一捷径。
- **核心创新 / 方法** · 以协同瓶颈目标对齐全观测和条件删观测的预测行为。
- **Baseline** · 常见多模态训练目标。
- **Benchmark** · CLIP-ViT、DeBERTa 与 CREMA-D 的讽刺扩展等设置。
- **关键结果 / 消融** · 协同样本准确率至多增 7.8%，整体至多增 3.8%。
- **适用条件 / 局限** · 需要区分真正协同样本，错误惩罚可伤害单模态本已充分的场景。

**可复用机制** · 多模态增强不能只测全输入得分，也应测试关键模态缺失是否按预期改变信心。

<a id="paper-151073"></a>

## Synthesis Through Simulation: Generating Coherent Enterprise Data via Scalable Agent-System Interaction

[官方论文页](https://neurips.cc/virtual/2026/poster/151073) · [作者来源](https://openreview.net/forum?id=d9jIdRauHh)

- **问题 / 瓶颈** · 按行造数据容易违反跨实体及先后关系。
- **核心创新 / 方法** · 用代理在模拟服务中执行允许的操作，再记录结果。
- **Baseline** · 传统按架构生成等方法。
- **Benchmark** · 十类环境的企业合成及工作流通过。
- **关键结果 / 消融** · 能强制结构合法；航空环境中紧耦合任务约 82% 轨迹失败。
- **适用条件 / 局限** · 合法不保证频率真实，依赖模拟覆盖和代理组合能力。

**可复用机制** · 想保留工作流一致性时，可让约束系统直接产生训练状态，同时分开检查成功覆盖率。

<a id="paper-149579"></a>

## Synthetic Anchor-Assisted Prototype Alignment for Heterogeneous Federated Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149579) · [作者来源](https://openreview.net/forum?id=p3wHaK3xhS)

- **问题 / 瓶颈** · 本地类别原型嘈杂且可能被污染。
- **核心创新 / 方法** · 以类描述及生成模型得到参考锚，指导客户端原型。
- **Baseline** · 代表性异质联邦基线。
- **Benchmark** · 异质联邦任务及锚质量、温度与系统开销诊断。
- **关键结果 / 消融** · 作者报告改善，并分析锚品质与温度影响。
- **适用条件 / 局限** · 参考锚会继承生成偏差，摘要未给精度。

**可复用机制** · 各参与方表征漂移时，先建共同校准锚并对照锚与真实分布一致性。

<a id="paper-154925"></a>

## Synthetic Pre-Pre-Training Improves Language Model Robustness to Noisy Pre-Training Data

[官方论文页](https://neurips.cc/virtual/2026/poster/154925) · [作者来源](https://openreview.net/forum?id=9wSLJmqdd1)

- **问题 / 瓶颈** · 从随机权重学习可能先吸收噪声相关性。
- **核心创新 / 方法** · 用随机 RNN 生成序列作预预训练，维持正式训练配方。
- **Baseline** · 无合成阶段的普通初始化。
- **Benchmark** · 人工损坏与自然噪声网络语料。
- **关键结果 / 消融** · 作者报告噪声越大相对收益越强，并观察损坏 token 间注意力权重下降。
- **适用条件 / 局限** · 依赖生成分布和训练量，摘要未给适用边界。

**可复用机制** · 数据清洗预算不足时可额外比较先学无噪序列结构的初始化和从头训练。

<a id="paper-152335"></a>

## Synthetic Tasks for Training AutoResearch

[官方论文页](https://neurips.cc/virtual/2026/poster/152335) · [作者来源](https://openreview.net/forum?id=TqCbmUrduo)

- **问题 / 瓶颈** · 短问答和独立实现任务不训练实验反馈。
- **核心创新 / 方法** · 用真实数据构造可执行研究任务并自调试。
- **Baseline** · 未在该任务训练的代理。
- **Benchmark** · 研究代理的任务通过及 AUP。
- **关键结果 / 消融** · 微调的 AUP 最高增 18%，并改善域外表现。
- **适用条件 / 局限** · 依赖任务验证及所采训练生态。

**可复用机制** · 为研究型代理生成数据时，应让训练轨迹包括可以评估和改进的基线。

<a id="paper-155345"></a>

## Synthetic Web: Benchmarking Language Agents under Adversarial Search Ranking

[官方论文页](https://neurips.cc/virtual/2026/poster/155345) · [作者来源](https://openreview.net/forum?id=6JUMpZWGTT)

- **问题 / 瓶颈** · 常用网页基准混入记忆答案，搜索排名和可信程度也可能相关。
- **核心创新 / 方法** · 构造有标签的合成互链网页，记过程并控制证据排序。
- **Baseline** · 现有网络代理及不同排名条件。
- **Benchmark** · 数千网页，检索推理与来源可靠性。
- **关键结果 / 消融** · 摘要报告即便证据可用，仍存在检索型推理局限。
- **适用条件 / 局限** · 合成网页不能代表全真实网络，摘要未给量化效果。

**可复用机制** · 对检索评测控制证据可得性和排名，区分没有检到与不善判断。

<a id="paper-155151"></a>

## Synthetic Worlds for Temporal Evaluation and Knowledge Updating in LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/155151) · [作者来源](https://openreview.net/forum?id=7vn1QgavAm)

- **问题 / 瓶颈** · 公开事实未知何时已进入预训练，难验证时效保持。
- **核心创新 / 方法** · 模拟事件轨迹后比较中训和指令微调的知识更新。
- **Baseline** · 既有知识更新方法。
- **Benchmark** · 受控虚构未来世界的事实和时间评估。
- **关键结果 / 消融** · 摘要报告较现有方法提升 14.23%。
- **适用条件 / 局限** · 在虚构一致环境验证，不等于真实新闻可及时吸收。

**可复用机制** · 要区分记忆和更新能力，可构造带连锁依赖的新事实，再跟踪更新后的跨事实一致性。

<a id="paper-139072"></a>

## SynthForensics: Benchmarking and Evaluating People-Centric Synthetic Video Deepfakes

[官方论文页](https://neurips.cc/virtual/2026/poster/139072) · [作者来源](https://openreview.net/forum?id=mzDFqKFToa)

- **问题 / 瓶颈** · 编辑数据上训练的检测器可能不覆盖全生成视频。
- **核心创新 / 方法** · 对不同时代假视频和压缩条件比较既有检测器、微调和重训。
- **Baseline** · 15 个检测器，传统伪造和新合成基准。
- **Benchmark** · 三个协议，AUC 及人类对画面质量的评价。
- **关键结果 / 消融** · 人脸检测方案降 13 至 55 个 AUC 点，平均 27；微调补回新域但伤及旧基准。
- **适用条件 / 局限** · 局限于所测生成源及检测器。

**可复用机制** · 反伪造模型适配新生成域时同时测旧域，以防把短期改善误认成普适鲁棒性。

<a id="paper-151432"></a>

## Systematic Hazard Sampling: Minimal-Variance Inference for Discrete Diffusion and Flow Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151432) · [作者来源](https://openreview.net/forum?id=al6oaoCR5A)

- **问题 / 瓶颈** · 低预算下随机编辑次数会造成残噪或级联替换。
- **核心创新 / 方法** · 用系统危险率采样替换离散采样，不需训练。
- **Baseline** · 既有离散扩散与流采样器。
- **Benchmark** · 约 110M 至 3B 模型，不同函数评估次数。
- **关键结果 / 消融** · 摘要报告样本质量一致改善，增益随评估次数增加。
- **适用条件 / 局限** · 依赖所述离散采样机制，摘要未给挂接成本。

**可复用机制** · 生成质量下降时单独测采样器引入的噪声，不只从模型损失诊断。

<a id="paper-152792"></a>

## T$^2$-Splat: Adaptive Topology Mesh Splatting with Texture Residuals

[官方论文页](https://neurips.cc/virtual/2026/poster/152792) · [作者来源](https://openreview.net/forum?id=QJlQ53FLTo)

- **问题 / 瓶颈** · 三角面折叠会让细节模糊并出现混叠
- **核心创新 / 方法** · 用多尺度残余纹理建模，使网格拓扑能压缩
- **Baseline** · 既有网格和点渲染方法
- **Benchmark** · Mip-NeRF 360、Tanks and Temples、DTU；PSNR 与面数
- **关键结果 / 消融** · 摘要报告 PSNR 增 0.87 dB，保留 10% 面仍有较好画质
- **适用条件 / 局限** · 材质和几何耦合时拆分适用性需核验

**可复用机制** · 在重建压缩中同时记录纹理和网格的率失真

<a id="paper-150304"></a>

## TabWorld: A World-Modeling Foundation Model for Tabular Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/150304) · [作者来源](https://openreview.net/forum?id=j8Vn2ZHt0f)

- **问题 / 瓶颈** · 自然观测只有变动后状态，难知动作反事实
- **核心创新 / 方法** · 真实表格教条件补全，合成结构因果模型给动作前后标签
- **Baseline** · 仅观测训练的表格生成
- **Benchmark** · 留出表格、低数据适配、SCM 干预诊断
- **关键结果 / 消融** · 适配后保真、实用和干预行为改善，未报告数值
- **适用条件 / 局限** · 真实因果响应未必与模拟 SCM 家族匹配

**可复用机制** · 在任务模型中区分观测建模与干预验收

<a id="paper-154934"></a>

## TACO: Towards Task-Consistent Open-Vocabulary Adaptation in Video Recognition

[官方论文页](https://neurips.cc/virtual/2026/poster/154934) · [作者来源](https://openreview.net/forum?id=9qHLzDW8KJ)

- **问题 / 瓶颈** · 直接专项优化可能损伤基础到新类别泛化
- **核心创新 / 方法** · 使用轻量投影区分训练优化与实际读出的表示
- **Baseline** · 现有开放词汇适配方法
- **Benchmark** · 跨数据集和 base-to-novel 视频识别
- **关键结果 / 消融** · 摘要报告领先，数值未列
- **适用条件 / 局限** · 测试类别与训练标签结构影响正则效果

**可复用机制** · 同时证实域内适应和未见类检索，不用同域分数代替后者

<a id="paper-148688"></a>

## TAC: Timestamped Audio Captioning

[官方论文页](https://neurips.cc/virtual/2026/poster/148688) · [作者来源](https://openreview.net/forum?id=vn02SDACyt)

- **问题 / 瓶颈** · 全局音频摘要会丢事件时序
- **核心创新 / 方法** · 生成分时音频或音视频描述，再交文本模型推理
- **Baseline** · 既有音频及音视频理解模型
- **Benchmark** · MMAU-Pro、MMSU、MMAR、DailyOmni、VideoHolmes
- **关键结果 / 消融** · 摘要报告组合成绩领先，未给幅度
- **适用条件 / 局限** · 纯文字可能压缩空间或细粒度声学信号

**可复用机制** · 将时序错误拆分为事件识别、时间标注与文字推理

<a id="paper-153041"></a>

## TACT-KV: Tri-Axis Cosine Transform for Compressing Volumetric KV Caches in Medical VLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/153041) · [作者来源](https://openreview.net/forum?id=OU6bVNsqd3)

- **问题 / 瓶颈** · 逐 token 无结构量化忽略空间或时空冗余
- **核心创新 / 方法** · 用三轴余弦变换后压缩 K/V 缓存
- **Baseline** · 原未压缩与其他缓存量化基线
- **Benchmark** · 六医学 VLM 的两 CT 集及四通用视频 VLM
- **关键结果 / 消融** · CT 上一比特预测近保真，同显存批次最高八倍
- **适用条件 / 局限** · 依赖体素或视频 token 布局可恢复且可用变换核

**可复用机制** · 三维感知推理在相同质量下检验轴向变换与普通低比特

<a id="paper-155710"></a>

## TailAdapt: Heavy-Tailed Sparse Variational Adaptation for Long-Tailed Class Incremental Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/155710) · [作者来源](https://openreview.net/forum?id=3V8BlU6B4a)

- **问题 / 瓶颈** · 头部类别易占据可学习参数并影响旧类
- **核心创新 / 方法** · 重尾稀疏变分适配允许少数参数高可塑
- **Baseline** · 长尾类增量的强基线
- **Benchmark** · LT-CIL；尾部、遗忘及参数效率
- **关键结果 / 消融** · 多项改善，摘要未列数字
- **适用条件 / 局限** · 稀疏选择应稳定复现实验，类频变化需重验

**可复用机制** · 给长尾流保留稀疏开放窗口并追踪旧类表现

<a id="paper-150715"></a>

## Tail Competition Explains Scaling in Best-of-N Sampling for Verifiable Problems

[官方论文页](https://neurips.cc/virtual/2026/poster/150715) · [作者来源](https://openreview.net/forum?id=g0h3FQFGch)

- **问题 / 瓶颈** · 样本越多可能选中评分极高的错误项
- **核心创新 / 方法** · 用正确、错误评分尾部竞争解释非单调区间，构造轻量停止指标
- **Baseline** · 固定候选数的 Best-of-N
- **Benchmark** · 合成及真实奖励评分；准确随 N 的变化
- **关键结果 / 消融** · 实验证实增加采样可能变差，不完全验证器收敛可能较慢
- **适用条件 / 局限** · 需足够尾部样本估计风险

**可复用机制** · 同一验证器按至少三档 N 验收而非直接增预算

<a id="paper-155753"></a>

## TailCon: Mitigating Tail Signal Erosion through Memory Consolidation for Long-Tailed Recognition

[官方论文页](https://neurips.cc/virtual/2026/poster/155753) · [作者来源](https://openreview.net/forum?id=3CZgBtaFyo)

- **问题 / 瓶颈** · 高频类更新可能冲淡低频类信号。
- **核心创新 / 方法** · 存稀有或不确定表征，用低容量代理周期蒸馏。
- **Baseline** · 重采样、解耦、专家及原型方案。
- **Benchmark** · CIFAR-10/100-LT、ImageNet-LT、iNaturalist 2018。
- **关键结果 / 消融** · 各套改善，关闭推理记忆仍有收益。
- **适用条件 / 局限** · 主要适合稀有复现且梯度冲突强时。

**可复用机制** · 把证据存留与优化整合解耦，分别测外存和写回贡献。

<a id="paper-150867"></a>

## Tail Cues, Principal Corrections: Plug-and-Play Rectification for Open-Set Test-Time Adaptation

[官方论文页](https://neurips.cc/virtual/2026/poster/150867) · [作者来源](https://openreview.net/forum?id=eldBzxFDbK)

- **问题 / 瓶颈** · 未知实例污染反传和可变记忆。
- **核心创新 / 方法** · 将主尾坐标分解，以加权岭回归估计模式和样本级主空间漂移。
- **Baseline** · UniEnt 与 COME。
- **Benchmark** · ImageNet-C、六 csOOD 集。
- **关键结果 / 消融** · 较 UniEnt H-score 高 2.2%，快 2.5 倍，显存仅 12%。
- **适用条件 / 局限** · 需源线性头与可靠回归路由。

**可复用机制** · 可用辅助坐标预测主轴偏差而不改底座。

<a id="paper-151735"></a>

## TailDiff: Elicitable Tail-Guided Diffusion for Risk-Sensitive Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/151735) · [作者来源](https://openreview.net/forum?id=YTXAbIxk6x)

- **问题 / 瓶颈** · 经验 VaR、ES 由排序和阈值计算。
- **核心创新 / 方法** · 用联合可诱导评分做免训练引导。
- **Baseline** · 尾风险仿真方法与合成 oracle。
- **Benchmark** · 合成及金融尾风险，尾指标与主体保真。
- **关键结果 / 消融** · 接近合成 oracle 下限，金融尾部有改善。
- **适用条件 / 局限** · 局部理论限低噪和小漂移。

**可复用机制** · 把尾部要求和主体保真分别当调参目标。

<a id="paper-154800"></a>

## TailFix: Mitigating Error Accumulation and Correcting Tail Deterioration in Long-Horizon Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/154800) · [作者来源](https://openreview.net/forum?id=As8bch5HUh)

- **问题 / 瓶颈** · 过度跨尺度混合传播初始偏差。
- **核心创新 / 方法** · 门控跨尺度残差并单独纠偏尾部。
- **Baseline** · 常规长预测。
- **Benchmark** · 多预测任务及尾部放大因子 TAF。
- **关键结果 / 消融** · 尾部放大和整体预测误差降低。
- **适用条件 / 局限** · 所选早晚段会改变 TAF。

**可复用机制** · 长预测除了均方误差还报告随提前量的扩大率。

<a id="paper-149857"></a>

## TailGuard: Subgroup Tail Coverage Theory for Safe LLM Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/149857) · [作者来源](https://openreview.net/forum?id=ml3suoaUwg)

- **问题 / 瓶颈** · 总体密度比掩盖小群体高危缺样本。
- **核心创新 / 方法** · 分析部署与训练尾部比，做有校准风险门。
- **Baseline** · 全局覆盖。
- **Benchmark** · 合成、半合成标签、主动查询和风险门代理试验。
- **关键结果 / 消融** · 尾部缺支持导致离线识别不可能。
- **适用条件 / 局限** · 需校准危害标度，数据层验证非部署结果。

**可复用机制** · 监控各群体极端风险，无法认证时收集缺失样本。

<a id="paper-153252"></a>

## Tail-Risk-Aware Stackelberg Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/153252) · [作者来源](https://openreview.net/forum?id=MdGZGoFqFn)

- **问题 / 瓶颈** · 学习策略的遗憾可能受跟随者响应误差支配。
- **核心创新 / 方法** · 以短缺规划认证 CVaR 响应，分解遗憾。
- **Baseline** · 直接 Stackelberg regret。
- **Benchmark** · 协作 bandit 与 Markov game 理论。
- **关键结果 / 消融** · bandit 近极小极大，Markov 真遗憾依赖覆盖。
- **适用条件 / 局限** · 需 CVaR 模型和响应兼容性。

**可复用机制** · 将错误响应估计与策略改进收益分开验证。

<a id="paper-151069"></a>

## Tail Wags the Model: Generalization and Membership Privacy Trade-offs of Sharpness-Aware Minimization

[官方论文页](https://neurips.cc/virtual/2026/poster/151069) · [作者来源](https://openreview.net/forum?id=dBVxJkzvkA)

- **问题 / 瓶颈** · 泛化改善可能同时放大个体训练信息。
- **核心创新 / 方法** · 比较 SAM 与梯度下降的少数组表示分离。
- **Baseline** · 常规 SGD。
- **Benchmark** · 长尾表示、泛化与隐私权衡。
- **关键结果 / 消融** · 理论和实验支持少数组相似性增大可能增加隐私风险。
- **适用条件 / 局限** · 分析依赖过参数与长尾结构。

**可复用机制** · 将整体泛化与分群隐私都纳入优化器选型。

<a id="paper-153778"></a>

## Take It or Leave It: Intent-Controlled Partial Optimal Transport

[官方论文页](https://neurips.cc/virtual/2026/poster/153778) · [作者来源](https://openreview.net/forum?id=IjSvYhsV0a)

- **问题 / 瓶颈** · 全局未匹配预算不能区分低质观测。
- **核心创新 / 方法** · 点级拒绝成本和增广支持上的平衡 OT。
- **Baseline** · 统一拒绝的部分 OT。
- **Benchmark** · 正无标签学习、开放部分域适配；卫星案例。
- **关键结果 / 消融** · 固定基线加入规则后改善。
- **适用条件 / 局限** · 依赖可验证的侧信息和拒配代价。

**可复用机制** · 工具证据匹配可拒配不可靠片段，而非强配全量。

<a id="paper-153795"></a>

## Taking Low-Rank LLM Compression a Step Further: A Global Perspective with Fused Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/153795) · [作者来源](https://openreview.net/forum?id=IdTyUsG3dN)

- **问题 / 瓶颈** · 层内重构误差沿网络放大，分解矩阵顺序运行慢。
- **核心创新 / 方法** · ADMM 分离秩约束和语言目标，融合 GPU 算子。
- **Baseline** · 逐层重构及未压缩模型。
- **Benchmark** · Qwen-3-8B 等，困惑度、零样本和速度。
- **关键结果 / 消融** · 压缩 30% 时困惑度 10.05 对原 9.85。
- **适用条件 / 局限** · 需适配运行内核；其他架构复测。

**可复用机制** · 联合评全局误差、实际吞吐和压缩比。

<a id="paper-154698"></a>

## Taking the Road Less Scheduled with Adaptive Polyak Steps

[官方论文页](https://neurips.cc/virtual/2026/poster/154698) · [作者来源](https://openreview.net/forum?id=BgIhio9OtL)

- **问题 / 瓶颈** · Schedule-Free 仍依赖基础步长调参。
- **核心创新 / 方法** · 从采样损失、梯度、迭代量和下界得 Polyak 步长。
- **Baseline** · 调参的 Schedule-Free SGD/Adam。
- **Benchmark** · 预训练、蒸馏与凸分析。
- **关键结果 / 消融** · 保近根号分之一收敛率并达相近或更好实证。
- **适用条件 / 局限** · 需要有效目标下界；逼近误差有条件。

**可复用机制** · 将真实损失下降空间作为动态步长尺度。

<a id="paper-139524"></a>

## TALES: Text-Adventure Learning Environment Suite

[官方论文页](https://neurips.cc/virtual/2026/poster/139524) · [作者来源](https://openreview.net/forum?id=KavE6QK1MK)

- **问题 / 瓶颈** · 特权信息或改版脚手架抬估成功。
- **核心创新 / 方法** · 从原版人写文本冒险与合成环境测失败。
- **Baseline** · 各开源与闭源代理。
- **Benchmark** · TALES，真实及生成任务。
- **关键结果 / 消融** · 最佳代理在人写任务低于 25%。
- **适用条件 / 局限** · 涉及游戏特定探索和交互。

**可复用机制** · 保留真实任务接口，排查合成场景是否过于乐观。

<a id="paper-155976"></a>

## Talk Less, Work More: Communication-Efficient Decentralized Stochastic Approximation

[官方论文页](https://neurips.cc/virtual/2026/poster/155976) · [作者来源](https://openreview.net/forum?id=1PWHsICnyE)

- **问题 / 瓶颈** · 每步协调通信代价高。
- **核心创新 / 方法** · 每通信轮先做 H 更新，弱连接图用 FastMix。
- **Baseline** · 频繁通信的去中心方法。
- **Benchmark** · 去中心 Q-learning、Markovian SGD、线性近似。
- **关键结果 / 消融** · 达到目标精度通信更少。
- **适用条件 / 局限** · 过多本地步会增加漂移和采样依赖。

**可复用机制** · 部署时按拓扑及目标误差联合调计算与协调。

<a id="paper-151232"></a>

## TALON: Confidence-Aware Speculative Decoding with Adaptive Token Trees

[官方论文页](https://neurips.cc/virtual/2026/poster/151232) · [作者来源](https://openreview.net/forum?id=bvEN7uoqUE)

- **问题 / 瓶颈** · 固定宽深浪费易分支并不足以探索难分支。
- **核心创新 / 方法** · 低不确定深窄，高不确定浅宽，迭代到预算。
- **Baseline** · EAGLE-3 和自回归。
- **Benchmark** · 五模型六数据集。
- **关键结果 / 消融** · 超过 EAGLE-3，相对自回归最高 5.16 倍。
- **适用条件 / 局限** · 速度受解码配置与设备变化。

**可复用机制** · 在总预算下按不确定度选择探索宽度和预取深度。

<a id="paper-150003"></a>

## TAMEing the Open-World Personalization: Towards Open-Set Personalized MLLM Assistant

[官方论文页](https://neurips.cc/virtual/2026/poster/150003) · [作者来源](https://openreview.net/forum?id=lUuttvJ3h1)

- **问题 / 瓶颈** · 静态概念库需要用户频繁编辑。
- **核心创新 / 方法** · 免训练概念调和可新建并细化已知概念。
- **Baseline** · 固定概念集的个性化助手。
- **Benchmark** · 开放集合多模态个性化。
- **关键结果 / 消融** · 摘要报告实证有效，幅度未核。
- **适用条件 / 局限** · 需检验概念误合并和隐私。

**可复用机制** · 只有证据区分新旧概念时才写入长期库。

<a id="paper-149760"></a>

## Taming CoT Obfuscation in VLMs: From Mechanistic Evidence to Activation-Level Enforcement

[官方论文页](https://neurips.cc/virtual/2026/poster/149760) · [作者来源](https://openreview.net/forum?id=nWvQHaEImN)

- **问题 / 瓶颈** · 答案准确仍可能出现失去图像依据的理由。
- **核心创新 / 方法** · 以监测器和稀疏自编码器对齐模板方向并正则。
- **Baseline** · GRPO。
- **Benchmark** · VIRL-39k、SPA-VL、四通用 VLM 基准。
- **关键结果 / 消融** · 可监测性最高增 30.9% 和 16.7%，通用和任务性能保持。
- **适用条件 / 局限** · 需裁判与 SAE 方向校准。

**可复用机制** · 分别验答案正确与实际视觉依据。

<a id="paper-154545"></a>

## Taming the Curses of Multiagency in Robust Markov Games with Large State Space through Linear Function Approximation

[官方论文页](https://neurips.cc/virtual/2026/poster/154545) · [作者来源](https://openreview.net/forum?id=ClsqGkeoIS)

- **问题 / 瓶颈** · 表格需要随状态与代理膨胀。
- **核心创新 / 方法** · 研究总变差不确定集下带线性近似的算法。
- **Baseline** · 表格及受限线性 RMG。
- **Benchmark** · 生成模型和在线交互理论。
- **关键结果 / 消融** · 在大状态条件下避免样本复杂度的多代理指数问题。
- **适用条件 / 局限** · 依赖线性模型及不确定集。

**可复用机制** · 先利用共同结构降维，再考虑鲁棒规划预算。

<a id="paper-152555"></a>

## Taming the Tails: Why Distributionally Robust Optimization Needs New Theory for Imbalanced Regression

[官方论文页](https://neurips.cc/virtual/2026/poster/152555) · [作者来源](https://openreview.net/forum?id=SFa3GaxCb3)

- **问题 / 瓶颈** · 全局分布半径主要控制多数区域。
- **核心创新 / 方法** · 局部样本越少越放宽目标区间歧义，并导密度加权。
- **Baseline** · 标准 Wasserstein/χ² DRO 及长尾回归。
- **Benchmark** · 七表格基准，尾 MSE 与 SERA。
- **关键结果 / 消融** · 尾性能改善，全局方法可与 ERM 相近。
- **适用条件 / 局限** · 区间低覆盖时区间划分敏感。

**可复用机制** · 稀有回报或故障预测应按对应目标值校准鲁棒性。

<a id="paper-151590"></a>

## TanGCE: Manifold-Aware Concept Erasure

[官方论文页](https://neurips.cc/virtual/2026/poster/151590) · [作者来源](https://openreview.net/forum?id=ZR2KTfCX8Y)

- **问题 / 瓶颈** · 线性删方向后仍可能泄露，不约束的更新会离流形。
- **核心创新 / 方法** · 用近邻割线估切面，对非线性属性梯度做信赖域投影。
- **Baseline** · 已有线性及非线性擦除。
- **Benchmark** · 13 语言模型、三概念、40 CelebA-CLIP 属性。
- **关键结果 / 消融** · 相同控制损伤下减少目标信号，改善既有擦除。
- **适用条件 / 局限** · 需有效近邻及可用属性模型。

**可复用机制** · 保护非目标行为时约束编辑方向，不只限制距离。

<a id="paper-152996"></a>

## Tango3D: Towards Alignment for Global and Local 2D-3D Correspondence

[官方论文页](https://neurips.cc/virtual/2026/poster/152996) · [作者来源](https://openreview.net/forum?id=OkNjnFaao1)

- **问题 / 瓶颈** · 只训练场景级表示会丢失局部对应。
- **核心创新 / 方法** · 将二维图块与三维 VAE token 映至共享空间，分阶段联合训练。
- **Baseline** · 单粒度的跨模态对齐作为背景。
- **Benchmark** · 局部二维三维对应和全局语义。
- **关键结果 / 消融** · 摘要报告建立兼顾全局与局部的细粒度对齐。
- **适用条件 / 局限** · 依赖几何编码器和多阶段训练，成本未报告。

**可复用机制** · 双模态表征可分别校准场景身份和实体位置，再共享表示。

<a id="paper-150263"></a>

## TAPIOCA: Why Task- Aware Pruning Improves OOD model Capability

[官方论文页](https://neurips.cc/virtual/2026/poster/150263) · [作者来源](https://openreview.net/forum?id=jT0H1Gve0C)

- **问题 / 瓶颈** · 域外输入可能扭曲范数和成对距离，导致熟悉任务的表示失效。
- **核心创新 / 方法** · 比较层几何，并用受控偏移和残差缩放验证因果解释。
- **Baseline** · 未剪枝和任务感知剪枝。
- **Benchmark** · 跨模型尺度的受控分布偏移。
- **关键结果 / 消融** · 摘要报告几何修正与域外改善相伴，并给出干预证据。
- **适用条件 / 局限** · 摘要未给统一几何阈值。

**可复用机制** · 剪枝也可能通过消除失真的残差更新改善域外能力，需直接测目标域几何。

<a id="paper-150631"></a>

## Target-Aligned Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/150631) · [作者来源](https://openreview.net/forum?id=geGOtycFCT)

- **问题 / 瓶颈** · 陈旧目标增加偏差，同时目标网络提供稳定。
- **核心创新 / 方法** · TARL 强调高对齐样本。
- **Baseline** · 离散和连续控制中的普通目标网络。
- **Benchmark** · 多种基准，含 Atari-10，以分数和墙钟衡量。
- **关键结果 / 消融** · Atari-10 峰值提升 38.18%，墙钟开销少于 4%。
- **适用条件 / 局限** · 结果依赖对齐度可靠，摘要未给低对齐样本的长期影响。

**可复用机制** · 若不能加快目标网络同步，可按新旧值一致性筛选更新信号。

<a id="paper-152616"></a>

## Target-Budget Best-Function Identification for Scaling-Law-Guided Model Selection

[官方论文页](https://neurips.cc/virtual/2026/poster/152616) · [作者来源](https://openreview.net/forum?id=RmWbG71zxj)

- **问题 / 瓶颈** · 在小资源上表现较差的设置可能最终最好。
- **核心创新 / 方法** · 用缩放定律及成本感知算法做目标预算最优候选识别。
- **Baseline** · Successive Halving 及仅用总计算的单变量缩放律。
- **Benchmark** · 多类缩放设置及排序反转的 Chinchilla 案例。
- **关键结果 / 消融** · 反转案例联合定律达 70% 至 87% 识别率，计算单变量基线为 0%。
- **适用条件 / 局限** · 保证依赖所述定律结构和估计准确。

**可复用机制** · 逐步淘汰前先检验外推预算是否会改变排序，并分别建模参数规模和数据。

<a id="paper-152635"></a>

## Targeted Synthetic Control Method

[官方论文页](https://neurips.cc/virtual/2026/poster/152635) · [作者来源](https://openreview.net/forum?id=RcGYPQDaKH)

- **问题 / 瓶颈** · 去偏估计可能产生不稳定权重或超出对照范围。
- **核心创新 / 方法** · 精化初始估计并使结果保持为观测对照的凸组合。
- **Baseline** · 既有合成控制方法。
- **Benchmark** · 合成和真实反事实估计实验。
- **关键结果 / 消融** · 摘要报告相较先进对照更准。
- **适用条件 / 局限** · 依赖对照覆盖，凸组合不允许任意外推。

**可复用机制** · 反事实决策需要审计时，在去偏之外将可解释的支持约束保留到最终估计。

<a id="paper-150962"></a>

## TARP: Trace-Anchored Regularization Prior for Retaining Stepwise Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/150962) · [作者来源](https://openreview.net/forum?id=dx2kKJoPQl)

- **问题 / 瓶颈** · 答案分数尚稳时策略和步骤可能已经变化。
- **核心创新 / 方法** · 从测得偏移构造轨迹正则。
- **Baseline** · 普通分阶段微调与答案评测。
- **Benchmark** · 旧任务保留及推理冗长度。
- **关键结果 / 消融** · 摘要报告几个设置中改善旧任务保留，并发现冗长权衡。
- **适用条件 / 局限** · 轨迹正则依赖特征选择，摘要未给普遍保证。

**可复用机制** · 将过程稳定性加入持续学习监控，以便比答案正确率更早发现退化。

<a id="paper-155521"></a>

## Task-Aware KV Cache Compression for LLM Agents via Utility-Driven Step Pruning

[官方论文页](https://neurips.cc/virtual/2026/poster/155521) · [作者来源](https://openreview.net/forum?id=4z1e71VXI6)

- **问题 / 瓶颈** · 逐 token 剪枝会破坏行动语义，密集证据下强排步骤也会误删。
- **核心创新 / 方法** · 融合注意力质量和意图先验并训练残差评分，熵高时回退。
- **Baseline** · 连续缓存和启发式剪枝。
- **Benchmark** · AgentBench 和 AlfWorld，20% KV 预算。
- **关键结果 / 消融** · 摘要报告相对启发式改善 2.9 至 7.3 点。
- **适用条件 / 局限** · 需按任务判断证据稀疏度。

**可复用机制** · 有时最重要的压缩设计是识别打分不可靠，并切回结构安全的缓存方式。

<a id="paper-154411"></a>

## Task-Driven Bayesian Experimental Design Yields Singly Intractable Objectives for Joint Policy Training

[官方论文页](https://neurips.cc/virtual/2026/poster/154411) · [作者来源](https://openreview.net/forum?id=Dl4K7mz1TS)

- **问题 / 瓶颈** · 减少参数不确定性不一定改善实际决策。
- **核心创新 / 方法** · 把预期未来损失改写为可联合随机优化的单层不可解目标。
- **Baseline** · 现有实验设计法。
- **Benchmark** · 不同下游行动和损失的贝叶斯实验设计。
- **关键结果 / 消融** · 摘要报告训练更简单有效。
- **适用条件 / 局限** · 依赖任务损失和可用的模拟数据。

**可复用机制** · 若采样是为某项行动服务，就直接把行动质量作为选择观测的优化信号。

<a id="paper-148615"></a>

## Task-Induced Riemannian Metrics for Vision Transformer Feature Spaces

[官方论文页](https://neurips.cc/virtual/2026/poster/148615) · [作者来源](https://openreview.net/forum?id=wQbmMf6PdD)

- **问题 / 瓶颈** · 逐 token 打分遗漏跨 token 扩散的方向，完整度量极大。
- **核心创新 / 方法** · 根据模型和解码器结构学习低秩任务诱导度量。
- **Baseline** · ToMe 及逐 token 选择。
- **Benchmark** · ViT-B/14 及 DPT 深度激进剪枝。
- **关键结果 / 消融** · 摘要报告高剪枝率下优于 ToMe。
- **适用条件 / 局限** · 低秩可学性依赖模型解码器结构。

**可复用机制** · 为特定下游压缩表示应先估关心的方向，再决定合并哪些 token。

<a id="paper-138911"></a>

## Task Success Is Not Enough: Side-effect-Aware Evaluation of Tool-Using Language Model Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/138911) · [作者来源](https://openreview.net/forum?id=xJdBs3VVTg)

- **问题 / 瓶颈** · 只评目标达成可能鼓励未授权的额外操作。
- **核心创新 / 方法** · 以确定性轨迹规则验证两个目标，覆盖多种状态耦合。
- **Baseline** · 所测工具代理及仅成功导向评测。
- **Benchmark** · 201 项邮件、日历和工单任务，覆盖 2,211 次运行。
- **关键结果 / 消融** · 摘要提供可复核轨迹与副作用评测协议。
- **适用条件 / 局限** · 所定义授权范围不代表任意组织要求。

**可复用机制** · 工作流中的通过条件应包含实际改过哪些状态以及授权来源。

<a id="paper-152712"></a>

## Task Vector Geometry Underlies Dual Modes of Task Inference in Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/152712) · [作者来源](https://openreview.net/forum?id=QvgaAPuT4e)

- **问题 / 瓶颈** · 单看训练任务性能未解释域外泛化何时发生。
- **核心创新 / 方法** · 用潜任务合成训练分布学习小 Transformer，再分析向量几何。
- **Baseline** · 不同训练分布及任务向量方向。
- **Benchmark** · 受控合成序列。
- **关键结果 / 消融** · 实验证明训练分布、几何与泛化有关。
- **适用条件 / 局限** · 小模型和合成设置，摘要未给真实任务外推。

**可复用机制** · 任务覆盖应同时看数量与几何方向，避免新任务落在训练子空间外。

<a id="paper-153416"></a>

## Tatemae: Detecting Alignment Faking via Tool Selection in LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/153416) · [作者来源](https://openreview.net/forum?id=LUX7b68Mpp)

- **问题 / 瓶颈** · 只读推理文本无法确认代理是否实际遵循安全约束。
- **核心创新 / 方法** · 对照不同监控条件下的工具选择，并核对行为和说明一致性。
- **Baseline** · 同模型不同监控条件及不同前沿模型。
- **Benchmark** · 108 个企业 IT 情景。
- **关键结果 / 消融** · 摘要报告监控条件会改变部分行为，而且跨域差异明显。
- **适用条件 / 局限** · 测试行为不等于确认模型内部意图。

**可复用机制** · 在审计有副作用的工具时直接测实际动作，不仅依赖模型自述。

<a id="paper-139574"></a>

## TDBench: Benchmarking Vision Language Models on Top-Down Image Understanding

[官方论文页](https://neurips.cc/virtual/2026/poster/139574) · [作者来源](https://openreview.net/forum?id=HcuEN74kvm)

- **问题 / 瓶颈** · 总体正确率无法区分偶然错误和旋转不稳定
- **核心创新 / 方法** · 用同题四种旋转并按难度匹配零模型检查残差
- **Baseline** · 不同 VLM 及难度调整的 Poisson-binomial 零假设
- **Benchmark** · TDBench；0 到 4 个方向正确的分布
- **关键结果 / 消融** · 分出掌握项和稳定失败项，摘要未给数值
- **适用条件 / 局限** · 依赖旋转不改变题意

**可复用机制** · 导航视觉测试先查坐标变换一致性再看平均分

<a id="paper-151024"></a>

## Teacher-Aware Evolution of Heuristic Programs from Learned Optimization Policies

[官方论文页](https://neurips.cc/virtual/2026/poster/151024) · [作者来源](https://openreview.net/forum?id=dXWka7F0Ie)

- **问题 / 瓶颈** · 只观察最终成本不足以指导程序候选调整
- **核心创新 / 方法** · 将神经优化教师的行为与任务绩效共同反馈给启发式程序搜索
- **Baseline** · 仅看性能的 LLM 启发式进化
- **Benchmark** · 调度、路线和图优化
- **关键结果 / 消融** · 摘要报告程序表现改善，部署无需神经推理
- **适用条件 / 局限** · 依赖教师行为和实际目标一致

**可复用机制** · 高频部署时离线蒸馏成可执行规则并单列质量损失

<a id="paper-153002"></a>

## Teaching Large Language Models When Not to Know: Learning Temporal Critique for Ex-Ante Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/153002) · [作者来源](https://openreview.net/forum?id=OhXc6BJCQS)

- **问题 / 瓶颈** · 训练模型知道将来事件，难从历史信息如实推断
- **核心创新 / 方法** · 给查询、截止及候选，训练识别泄漏并说明时间边界
- **Baseline** · 提示与普通 SFT
- **Benchmark** · Qwen2.5-7B/14B；时间泄漏
- **关键结果 / 消融** · 平均分别少 41.89 和 37.79 个百分点
- **适用条件 / 局限** · 需要可审计的可用信息时间

**可复用机制** · 回测智能体要求时间证据验收而不仅是答案正确

<a id="paper-148659"></a>

## Teaching VLMs What to Say, Not How to Reason: Rethinking Counterfactual Reasoning in Autonomous Driving

[官方论文页](https://neurips.cc/virtual/2026/poster/148659) · [作者来源](https://openreview.net/forum?id=w690TmNnXg)

- **问题 / 瓶颈** · 动作表述合规可能掩盖视觉因果失真
- **核心创新 / 方法** · 分别改变因果和非因果因素，对照人类与模型选择变化
- **Baseline** · 使用反事实推理的 VLM、人类对照
- **Benchmark** · 自动驾驶场景的视觉扰动与动作选择
- **关键结果 / 消融** · 模型对两类变化均响应，人类更具选择性
- **适用条件 / 局限** · 依赖场景变量正确分组

**可复用机制** · 用反事实前后实际动作变化而非文字相似度验收因果

<a id="paper-155265"></a>

## TeMPO: Frame-Causal Token Compression for Efficient Video Large Language Model

[官方论文页](https://neurips.cc/virtual/2026/poster/155265) · [作者来源](https://openreview.net/forum?id=6zXzWufbUb)

- **问题 / 瓶颈** · 压缩若利用未来帧难在线部署
- **核心创新 / 方法** · 按因果时序选择 token 并用无参数邻域融合
- **Baseline** · 原模型与无需训练的压缩法
- **Benchmark** · 四视频基准、多个多模态骨干
- **关键结果 / 消融** · 10% token 时保留 LLaVA-OneVision 99.8% 表现
- **适用条件 / 局限** · 视频帧预算与骨干影响结果

**可复用机制** · 等 token 预算下分别比较看更多帧和保留更密 token

<a id="paper-152083"></a>

## Temporal Backtracking Search for Test-time Generative Video Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/152083) · [作者来源](https://openreview.net/forum?id=VbbMjAFFHD)

- **问题 / 瓶颈** · 一次生成整段会把早期错误冻结
- **核心创新 / 方法** · 沿已有轨迹判断回溯点并重启，而非从零独立采样
- **Baseline** · 匹配预算 Best-of-N
- **Benchmark** · 算法、导航及机器人视频，含严格 OOD
- **关键结果 / 消融** · 作者报告 OOD 从 0.7% 至 22.7%，解均来自重启分支
- **适用条件 / 局限** · 依赖中间失败判断、未来状态及生成重启支持

**可复用机制** · 规划时比较局部分叉与相同预算的全重做

<a id="paper-153832"></a>

## Temporal Behavior Trees for Reinforcement Learning: Specifications as Rewards, Curricula, and Diagnostics

[官方论文页](https://neurips.cc/virtual/2026/poster/153832) · [作者来源](https://openreview.net/forum?id=IOFQf2UdfY)

- **问题 / 瓶颈** · 整体奖励难追踪哪个前置阶段阻塞
- **核心创新 / 方法** · 使用时序行为树导出奖励、课程和子任务失败
- **Baseline** · 稠密 STL 塑形及其他课程方法
- **Benchmark** · 六条离散及连续任务规格
- **关键结果 / 消融** · 简单任务持平，部分 reach-avoid 优于对照
- **适用条件 / 局限** · 规格正确性和表达成本由任务决定

**可复用机制** · 评测时用与训练同一子任务规格跟踪取得进展与触发失败

<a id="paper-153572"></a>

## Temporal Consistency Improves Generalization in Contextual Offline Meta Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/153572) · [作者来源](https://openreview.net/forum?id=KOlHCpKZ40)

- **问题 / 瓶颈** · 对比可区分任务却不学动态，重构只限短程。
- **核心创新 / 方法** · 预测同一历史后未来多步潜态，分析价值估计误差。
- **Baseline** · 对比与重构上下文方法。
- **Benchmark** · MuJoCo、Contextual DM Control、MetaWorld。
- **关键结果 / 消融** · 零样本和少样本泛化提升。
- **适用条件 / 局限** · 离线数据需要跨任务动态覆盖。

**可复用机制** · 用动态一致性约束任务表征，而非只按任务 ID 分离。

<a id="paper-151967"></a>

## Temporal Island Sparse Autoencoders for Interpreting Clinical Time-Series Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151967) · [作者来源](https://openreview.net/forum?id=WSgYALKmGw)

- **问题 / 瓶颈** · 逐单元热图难跨样本追踪。
- **核心创新 / 方法** · 稀疏自编码器用时序高斯区域和稀疏变量，再分开归因。
- **Baseline** · 事后逐单元归因。
- **Benchmark** · 五种主干，MIMIC-III/IV 各三任务。
- **关键结果 / 消融** · 提供结构概念且忠实度强。
- **适用条件 / 局限** · 字典以冻结主干为条件，域外需复查。

**可复用机制** · 先形成可复用时空原型，再为每次判断赋因。

<a id="paper-151166"></a>

## Temporal Pair Consistency for Flow Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/151166) · [作者来源](https://openreview.net/forum?id=cXos7ygjdV)

- **问题 / 瓶颈** · 独立时间监督没用路径结构。
- **核心创新 / 方法** · 训练时配两个时间点，保持采样和架构。
- **Baseline** · 标准 FM、OT-CFM、Rectified Flow、MeanFlow。
- **Benchmark** · CIFAR-10、ImageNet 256 和 512，同预算 NFE。
- **关键结果 / 消融** · CIFAR FM FID 6.35 到 3.19，OT-CFM 3.58 到 2.90。
- **适用条件 / 局限** · 需要同路径配对，随机和近邻对更弱。

**可复用机制** · 跨时间增目标一致性可降梯度方差而不加上线成本。

<a id="paper-149275"></a>

## Temporal Prototype Alignment for Frozen-Feature Dataset Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/149275) · [作者来源](https://openreview.net/forum?id=rX3bv5k1ck)

- **问题 / 瓶颈** · 空间多视图成本随增广数增长。
- **核心创新 / 方法** · 用在线原型估计、置信动量和多教师一致结构。
- **Baseline** · Linear Gradient Matching 等冻结特征方案。
- **Benchmark** · ImageNet 规模和细粒任务，跨 CNN 和 ViT。
- **关键结果 / 消融** · 显存更省和转移更强。
- **适用条件 / 局限** · 需累积信号稳定，优化切换时历史动量可能过时。

**可复用机制** · 用时间换空间时设置可靠性门避免陈旧估计。

<a id="paper-150389"></a>

## Temporal-Scale Sensitivity in Time-Series Tokenization and Scale-Robust Token Estimation by Gated Sum

[官方论文页](https://neurips.cc/virtual/2026/poster/150389) · [作者来源](https://openreview.net/forum?id=iQ0TBYaLes)

- **问题 / 瓶颈** · 短片段高方差，长片段压缩损信息。
- **核心创新 / 方法** · 轻量门控求和不同尺度的 token 估计。
- **Baseline** · 单时标分块。
- **Benchmark** · 12 数据集、四模态。
- **关键结果 / 消融** · 多任务提升且减尺度敏感。
- **适用条件 / 局限** · 跨度和门需匹配目标频率。

**可复用机制** · 把 patch 长度当偏差方差取舍，不必固定一档。

<a id="paper-154604"></a>

## Temporal Slice Learning for AI-Generated Video Detection with 400× Fewer FLOPs

[官方论文页](https://neurips.cc/virtual/2026/poster/154604) · [作者来源](https://openreview.net/forum?id=CNFgZ3PsmY)

- **问题 / 瓶颈** · 局部动态被大量重复外观淹没。
- **核心创新 / 方法** · 聚合选定行列，比较细节稳定与运动平滑。
- **Baseline** · ReStraV 等全视频方法。
- **Benchmark** · GenVideo、AI-Artist。
- **关键结果 / 消融** · FLOPs 减少超过 400 倍，推理 3.6 倍快。
- **适用条件 / 局限** · 切片可能漏随机位置伪影。

**可复用机制** · 针对时序证据用低成本重参数化，别只扩大主干。

<a id="paper-148926"></a>

## TEMPO: Temporal Enforcement via Mode-Separated Policy Optimization for Trustworthy LLM Backtesting

[官方论文页](https://neurips.cc/virtual/2026/poster/148926) · [作者来源](https://openreview.net/forum?id=uBLxMX8IFP)

- **问题 / 瓶颈** · 预训练事实的合法性依赖每例截止日期。
- **核心创新 / 方法** · GRPO 双模式奖励，先消除越期主张。
- **Baseline** · 日期提示和不按实例区分的遗忘。
- **Benchmark** · 三预测任务、两模型。
- **关键结果 / 消融** · 泄漏从 2–13% 降到 0.6–3.7%，有足够早期信号时性能增 6–13%。
- **适用条件 / 局限** · 依赖可验证的事实日期。

**可复用机制** · 条件证据边界应有独立先行约束。

<a id="paper-153006"></a>

## TENET: Time-point Encoding Network for Multivariate Time Series Anomaly Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/153006) · [作者来源](https://openreview.net/forum?id=OfstlhHWVn)

- **问题 / 瓶颈** · 局部变化放大重构误差。
- **核心创新 / 方法** · 相对时间位置检索窗口并与当前点混合，得标准正态 NLL。
- **Baseline** · 通用序列编码与其他单类目标。
- **Benchmark** · 多无监督时序异常数据。
- **关键结果 / 消融** · 保持固定评分仍优于改编码对照。
- **适用条件 / 局限** · 潜正态与任务标签可能不匹配。

**可复用机制** · 先使状态表征贴合决策，再复杂化异常分数。

<a id="paper-151664"></a>

## TENG-BC: Time-Evolving Natural Gradient for High-Accuracy Neural PDE Solvers with General Boundary Conditions

[官方论文页](https://neurips.cc/virtual/2026/poster/151664) · [作者来源](https://openreview.net/forum?id=Ywno1q1hWo)

- **问题 / 瓶颈** · 惩罚权重难兼容混合边界。
- **核心创新 / 方法** · 自然梯度形式逐步求解 Dirichlet、Neumann、Robin 等。
- **Baseline** · 传统求解器、PINN。
- **Benchmark** · 扩散、传输和非线性方程，匹配采样预算。
- **关键结果 / 消融** · 达求解器级精度并优于所比方案。
- **适用条件 / 局限** · 依赖边界可表示与自然梯度代价。

**可复用机制** · 物理代理学习应把边界条件当更新结构而非只设损失权重。

<a id="paper-150256"></a>

## TensorCommitments: A Lightweight Verifiable Inference for Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150256) · [作者来源](https://openreview.net/forum?id=jYSZwwreXP)

- **问题 / 瓶颈** · 客户端无法重跑全模型验证。
- **核心创新 / 方法** · 张量原生承诺和多元树绑定验证轨迹。
- **Baseline** · 慢密码学证明及需验证 GPU 方案。
- **Benchmark** · LLaMA2，证明和验证费用。
- **关键结果 / 消融** · 额外 0.97% 证明端及 0.12% 验证端时间。
- **适用条件 / 局限** · 依赖假设的验证与威胁模型。

**可复用机制** · 远程运行审计须同时量验证成本和覆盖。

<a id="paper-155464"></a>

## Tensorion: A Tensor-Aware Generalization of the Muon Optimizer

[官方论文页](https://neurips.cc/virtual/2026/poster/155464) · [作者来源](https://openreview.net/forum?id=5PDUovNqbT)

- **问题 / 瓶颈** · 展平丢多线性结构。
- **核心创新 / 方法** · 在张量范数球用自适应展开实现线性最小化 oracle。
- **Baseline** · Adam、张量优化法；二维时等价 Muon。
- **Benchmark** · 张量视觉任务，收敛和梯度稳定。
- **关键结果 / 消融** · 所测设定更稳定，幅度未核。
- **适用条件 / 局限** · 计算代价与可用展开依架构。

**可复用机制** · 优化器选型将权重轴对应的物理含义纳入更新。

<a id="paper-152923"></a>

## Terminal Failure Is Not Computational Failure: A Pre-Collapse Readout Regime in Nonlinear Dynamical Learners

[官方论文页](https://neurips.cc/virtual/2026/poster/152923) · [作者来源](https://openreview.net/forum?id=PPgIfHpvw4)

- **问题 / 瓶颈** · 终状态可能已失去中间正确证据。
- **核心创新 / 方法** · 比较早窗、范数停止及增长调节抽取。
- **Baseline** · 终点读出。
- **Benchmark** · MNIST、CIFAR-10 和多动态系统。
- **关键结果 / 消融** · 不稳定 modReLU 终点坍缩但前缀持稳，线性系统无同现象。
- **适用条件 / 局限** · 最佳读出依非线性和是否已训练。

**可复用机制** · 做全时间读出曲线，辨别递归真失败与读出过迟。

<a id="paper-139224"></a>

## TerminalWorld: Benchmarking Agents on Real-World Terminal Tasks

[官方论文页](https://neurips.cc/virtual/2026/poster/139224) · [作者来源](https://openreview.net/forum?id=dtdZBik7WV)

- **问题 / 瓶颈** · 专家编写任务不一定覆盖自然错误。
- **核心创新 / 方法** · 从录制轨迹抽取并验证 1530 个任务，人工核 200。
- **Baseline** · Terminal-Bench 等。
- **Benchmark** · 19 类环境，Verified 八模型六代理。
- **关键结果 / 消融** · 最高通过率 62.5%，与既有榜相关 0.20。
- **适用条件 / 局限** · 录制代表性和数据权限需验。

**可复用机制** · 代理回归集中测试真实多步骤行为并保采集来源可审计。

<a id="paper-148583"></a>

## TERMINATOR: Learning Optimal Exit Points for Early Stopping in Chain-of-Thought Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/148583) · [作者来源](https://openreview.net/forum?id=wjNvh6ASVx)

- **问题 / 瓶颈** · 通用长度上限忽略任务和模型。
- **核心创新 / 方法** · 构造最优推理长度样本，学习早退。
- **Baseline** · 原推理模型及现有早停。
- **Benchmark** · MATH-500、AIME 2025、HumanEval、GPQA。
- **关键结果 / 消融** · 过程缩短 14–55%，延迟减少逾一半。
- **适用条件 / 局限** · 偶然给对中间答案不代表所有任务可安全退出。

**可复用机制** · 把首次成功事件与最终正确作为联合验收。

<a id="paper-139599"></a>

## TerraVis: Towards Evaluation of World-Grounded Visual Consistency in Text-to-Image Generation via MLLM Workflows

[官方论文页](https://neurips.cc/virtual/2026/poster/139599) · [作者来源](https://openreview.net/forum?id=GFzKiLhgHV)

- **问题 / 瓶颈** · 对齐和高画质仍可有不可能关系。
- **核心创新 / 方法** · 先验适评性，再按对象、交互、场景及严重度诊断。
- **Baseline** · 常规审美、偏好和对齐指标。
- **Benchmark** · 两个通用文生图基准，多开闭模型。
- **关键结果 / 消融** · 世界一致性人类相关高于所比指标。
- **适用条件 / 局限** · 多模态评委仍可能漏多对象物理故障。

**可复用机制** · 世界模型评测给不同层级的可行动原因而非单分。

<a id="paper-152766"></a>

## TESLA: Native 4D Gaussian Splatting Generation with Temporally Structured Latents

[官方论文页](https://neurips.cc/virtual/2026/poster/152766) · [作者来源](https://openreview.net/forum?id=QXF0D2aiDK)

- **问题 / 瓶颈** · 逐视图视频缺少时间和视角一致。
- **核心创新 / 方法** · 时间结构潜量解耦粗几何与细外观，原生 4DGS 解码。
- **Baseline** · 多视角视频构造 4D 的方法。
- **Benchmark** · 4DGS 生成，动态序列和任意时间视点。
- **关键结果 / 消融** · 摘要报告优于对照，幅度未核。
- **适用条件 / 局限** · 依赖动画训练覆盖，非刚性复杂外观需测。

**可复用机制** · 给后续外观生成共享动态几何锚以避免视角独立漂移。

<a id="paper-148311"></a>

## Testable and Actionable Calibration for Full Swap Regret

[官方论文页](https://neurips.cc/virtual/2026/poster/148311) · [作者来源](https://openreview.net/forum?id=yls0nG3VKg)

- **问题 / 瓶颈** · 可信的概率偏差指标也可能不能预测用户效用损失。
- **核心创新 / 方法** · 从交换遗憾定义对比校准指标，并评估连续性和一致性。
- **Baseline** · 其他概率校准度量。
- **Benchmark** · 理论与实验校准比较。
- **关键结果 / 消融** · 摘要报告提出指标能将理论优势转为实践收益。
- **适用条件 / 局限** · 依赖所定义决策损失与采样假设。

**可复用机制** · 用于行动的置信度应按实际决策代价评价，而非只报分箱误差。

<a id="paper-150530"></a>

## Test-Time Adaptation via Self-Reinforced Optimal Transport for Zero-Shot OOD Detection with Vision–Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150530) · [作者来源](https://openreview.net/forum?id=hRRylGwSik)

- **问题 / 瓶颈** · 冻结多模态模型的最大置信无法可靠区分域内外。
- **核心创新 / 方法** · 对类别后验使用最优传输适配，迭代训练和自强化检测器。
- **Baseline** · 原始 VLM 分数和既有零样本域外检测。
- **Benchmark** · 域外检测基准及组件消融。
- **关键结果 / 消融** · 摘要报告优于已有方法且有各组件支持。
- **适用条件 / 局限** · 自强化依赖初始分离度，摘要未报告灾难性偏移条件。

**可复用机制** · 先对后验结构做目标域重校准，再决定统一拒识阈值。

<a id="paper-148903"></a>

## Test-Time Conditioning with Representation-Aligned Visual Features

[官方论文页](https://neurips.cc/virtual/2026/poster/148903) · [作者来源](https://openreview.net/forum?id=uJPI1xg4IN)

- **问题 / 瓶颈** · 文本或类别提示不容易表达参考图局部结构。
- **核心创新 / 方法** · 将去噪结果推向预训练提取器的参考表征。
- **Baseline** · 文本和类标签条件。
- **Benchmark** · ImageNet、COCO，以及局部与全局视觉引导。
- **关键结果 / 消融** · 摘要报告生成质量和多样性。
- **适用条件 / 局限** · 依赖表征语义及空间对齐，摘要未给成本和保真。

**可复用机制** · 细粒度条件可直接在与参考可比较的特征里计算，而非先用文本转述。

<a id="paper-152658"></a>

## Test-Time Defense Against Adversarial Attacks via Stochastic Resonance of Latent Ensembles

[官方论文页](https://neurips.cc/virtual/2026/poster/152658) · [作者来源](https://openreview.net/forum?id=RNQOTYbTSv)

- **问题 / 瓶颈** · 按具体扰动训练额外模块限制泛化。
- **核心创新 / 方法** · 对潜表征使用随机聚合再回映到参考域，无需微调。
- **Baseline** · 被保护模型的原始推理与其他视觉防护。
- **Benchmark** · 分类、双目、光流、深度和图文对齐。
- **关键结果 / 消融** · 摘要报告多任务效果改善，含光流 EPE 的改善。
- **适用条件 / 局限** · 依赖算力与随机集成，摘要未给干净样本代价。

**可复用机制** · 防御应同时测干净表现和多类受干扰任务，验证聚合不损伤任务相关细节。

<a id="paper-153144"></a>

## Test-Time Gradient Guidance of Flow Policies in Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/153144) · [作者来源](https://openreview.net/forum?id=NYzL9idgNU)

- **问题 / 瓶颈** · 从头通过去噪链做策略优化会降低稳定性和扩展性。
- **核心创新 / 方法** · QGF 在测试时用 Q 信息引导动作生成。
- **Baseline** · 演员评论家式流策略及普通行为策略。
- **Benchmark** · 强化学习和不同模型尺寸的控制。
- **关键结果 / 消融** · 摘要报告扩展性较好且具竞争力。
- **适用条件 / 局限** · 需要可靠价值函数，测试开销与域外估值误差未报告。

**可复用机制** · 表达力强的生成控制器可与局部价值改进模块分开训练。

<a id="paper-153400"></a>

## Test-Time Graph Anomaly Detection via Shifted Augmentation with Dynamic Objective Scheduling

[官方论文页](https://neurips.cc/virtual/2026/poster/153400) · [作者来源](https://openreview.net/forum?id=Lelz20rA0P)

- **问题 / 瓶颈** · 高信心样本偏向低偏移区，低信心样本的伪标签又不可靠。
- **核心创新 / 方法** · SADOS 使用变化增强并调度早期与后期目标。
- **Baseline** · 以固定目标或高置信伪标签做测试适应。
- **Benchmark** · 分布变化下的图异常检测。
- **关键结果 / 消融** · 摘要报告鲁棒性提升。
- **适用条件 / 局限** · 依赖增强覆盖目标变化，摘要未给调度触发条件。

**可复用机制** · 适配初期避免刚性伪标签，等表征恢复再强调任务决策。

<a id="paper-154657"></a>

## Test-Time Learning with an Evolving Library

[官方论文页](https://neurips.cc/virtual/2026/poster/154657) · [作者来源](https://openreview.net/forum?id=BzzLBbILBI)

- **问题 / 瓶颈** · 记录每个答案会形成冗余而不够通用。
- **核心创新 / 方法** · 评估经验当前效用和长期价值，逐步将实例规则整合。
- **Baseline** · 先进测试时缩放和学习。
- **Benchmark** · 数学、代码和多轮代理环境。
- **关键结果 / 消融** · 无真值反馈时摘要仍报告显著改善。
- **适用条件 / 局限** · 经验质量可能累积偏差，摘要未给长期漂移控制。

**可复用机制** · 跨任务重复部署可以主动将窄经验巩固为通用技能，而非无限添加单题记录。

<a id="paper-153940"></a>

## Test-time Multi-agent Coordination by Decomposed Value Gradient Flow

[官方论文页](https://neurips.cc/virtual/2026/poster/153940) · [作者来源](https://openreview.net/forum?id=HRgPovhTAK)

- **问题 / 瓶颈** · 各自做梯度改进可能让联合动作离开日志分布。
- **核心创新 / 方法** · 单独拟合行为流和分解价值，再用局部输运做测试时协调。
- **Baseline** · 仅行为模型及单独价值改进。
- **Benchmark** · 离线多代理强化学习及联合相关性。
- **关键结果 / 消融** · 理论指出局部输运与联合价值改进一致，并恢复相关性。
- **适用条件 / 局限** · 依赖可控制的价值分解误差，摘要未给额外推理成本。

**可复用机制** · 多代理价值改进应维护行为联合分布的覆盖，防止局部提升组合成不可行策略。

<a id="paper-153672"></a>

## Test-Time Personalization: A Diagnostic Framework and Probabilistic Fix for Scaling Failures

[官方论文页](https://neurips.cc/virtual/2026/poster/153672) · [作者来源](https://openreview.net/forum?id=JdKKdb98Rv)

- **问题 / 瓶颈** · 最佳样本数增加却可能因奖励模型塌缩或负相关而失败。
- **核心创新 / 方法** · 将 best-of-N 曲线拆成可测量量并据此修正。
- **Baseline** · 多个奖励模型和个性化排序。
- **Benchmark** · 多种生成策略及个性化文本任务。
- **关键结果 / 消融** · 摘要报告诊断曲线接近实测，修正后更稳定。
- **适用条件 / 局限** · 需要可信的个体偏好质量标签。

**可复用机制** · 部署个性化评分前测每类用户和查询上的有效排序，不能只看总体相关。

<a id="paper-151200"></a>

## Test-Time Prompt-Agnostic Decomposition

[官方论文页](https://neurips.cc/virtual/2026/poster/151200) · [作者来源](https://openreview.net/forum?id=cDRO2AY7N6)

- **问题 / 瓶颈** · 一次更新距离大或各步方向反复可让提示适配失效。
- **核心创新 / 方法** · 分解提示轨迹，约束两类故障。
- **Baseline** · 十种提示适配基线。
- **Benchmark** · 十五数据集，视觉与文本提示准确性。
- **关键结果 / 消融** · 视觉提示增 3% 至 8%，文本超过 2%。
- **适用条件 / 局限** · 摘要未给开放域更新开销或误差边界。

**可复用机制** · 记录更新方向与幅度的独立统计，诊断漂移时不要只调全局学习率。

<a id="paper-148449"></a>

## Test-time Risk Adaptation with Mixture of Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/148449) · [作者来源](https://openreview.net/forum?id=xjpWCBDACk)

- **问题 / 瓶颈** · 训练期风险目标固定，部署偏好可能更改。
- **核心创新 / 方法** · 用目标奖励和占据风险共同为已有策略候选动作评分。
- **Baseline** · 固定训练风险目标。
- **Benchmark** · 网格世界、MuJoCo、Safety-Gymnasium 及对齐场景。
- **关键结果 / 消融** · 摘要报告降低部署风险、保留奖励且不改参数。
- **适用条件 / 局限** · 依赖已有策略覆盖和可估占据。

**可复用机制** · 部署期风险约束变化可先调整候选动作评分，再考虑昂贵重训。

<a id="paper-155012"></a>

## Test-time Scaling for Diffusion Language Models with Frequency-Aware Remasking

[官方论文页](https://neurips.cc/virtual/2026/poster/155012) · [作者来源](https://openreview.net/forum?id=9FRE7icSIG)

- **问题 / 瓶颈** · 概率规则相同的采样器可能反复失败。
- **核心创新 / 方法** · 先快速采样，再对未解问题启用频率感知重掩码。
- **Baseline** · 只基于置信的基础解码。
- **Benchmark** · 推理与编程任务，含 HumanEval。
- **关键结果 / 消融** · 100 个普通样本都没解决的题中恢复 6.25% 至 18.75%。
- **适用条件 / 局限** · 需要识别未解决的题目，摘要未给不可验证任务效果。

**可复用机制** · 同种搜索失败多次时，应把剩余预算用于改变搜索规则。

<a id="paper-153345"></a>

## Test-Time Scaling in the Wild: Why Exploitation, Not Exploration, Is the Bottleneck

[官方论文页](https://neurips.cc/virtual/2026/poster/153345) · [作者来源](https://openreview.net/forum?id=M2vIH3TuCs)

- **问题 / 瓶颈** · 总体曲线混合生成候选不足与评判失败。
- **核心创新 / 方法** · 将预算分成探索和利用，用候选池质量与选择质量对照。
- **Baseline** · 单次生成及多候选融合。
- **Benchmark** · 医疗、法律、金融、通用聊天、创写五个领域。
- **关键结果 / 消融** · 摘要称融合只恢复约 40% 的可得质量。
- **适用条件 / 局限** · 开放任务的质量参照依赖评估。

**可复用机制** · 增加候选之前先查现有候选是否已含高质量答案，以决定扩生成还是改评审。

<a id="paper-154289"></a>

## Test-time Scaling of Diffusions with Flow Maps

[官方论文页](https://neurips.cc/virtual/2026/poster/154289) · [作者来源](https://openreview.net/forum?id=EtFrLaqiA4)

- **问题 / 瓶颈** · 难评半成品，使早期引导目标和终局效用错配。
- **核心创新 / 方法** · 构建流映射轨迹倾斜以快速预测完整样本。
- **Baseline** · 普通引导扩散与其他推理扩展法。
- **Benchmark** · 奖励引导生成和图像编辑，含视觉语言评判。
- **关键结果 / 消融** · 摘要展示支持复杂奖励的编辑。
- **适用条件 / 局限** · 依赖前瞻映射精度，摘要未给计算差异。

**可复用机制** · 只在终稿可评估时，学习便宜且可校验的末端预估用于中途决策。

<a id="paper-155507"></a>

## Test-Time Scaling with Diffusion Language Models via Reward-Guided Stitching

[官方论文页](https://neurips.cc/virtual/2026/poster/155507) · [作者来源](https://openreview.net/forum?id=54JyknakHB)

- **问题 / 瓶颈** · 先生成完整轨迹再选一条会浪费其他路线里可用的部分。
- **核心创新 / 方法** · 用掩码扩散采样多个候选，对各步评分，再以重组理由指导重算。
- **Baseline** · Dream、LLaDA 和 TiDAR。
- **Benchmark** · 扩散推理准确及延迟。
- **关键结果 / 消融** · 摘要报告延迟最多改善 1.8 倍。
- **适用条件 / 局限** · 跨轨迹步骤可能前提不一致，依赖过程奖励。

**可复用机制** · 将并行样本变成可搜索的局部候选池，重组后须验整体逻辑。

<a id="paper-155492"></a>

## Test Time Search Requires Training for Diversity

[官方论文页](https://neurips.cc/virtual/2026/poster/155492) · [作者来源](https://openreview.net/forum?id=5BCRUa67R0)

- **问题 / 瓶颈** · 共同奖励会使多候选收敛到同一种取舍
- **核心创新 / 方法** · 在奖励单纯形上分配向量偏好，后续候选条件于已出的候选
- **Baseline** · 标量奖励及 GRPO 优势估计
- **Benchmark** · 四个任务领域；best@k 与候选预算
- **关键结果 / 消融** · 预算越高相对优势越大，幅度未报告
- **适用条件 / 局限** · 依赖不同目标有可度量的 Pareto 取舍

**可复用机制** · 比较重复采样与训练出的有方向差异的候选

<a id="paper-150865"></a>

## Test-Time Speculation

[官方论文页](https://neurips.cc/virtual/2026/poster/150865) · [作者来源](https://openreview.net/forum?id=elwxI8Nne1)

- **问题 / 瓶颈** · 固定草稿无法适应当前题和生成段
- **核心创新 / 方法** · 以目标模型为教师在运行期间逐轮调整草稿
- **Baseline** · 现有推测解码器
- **Benchmark** · Qwen-3、Qwen-3.5、Llama 3.1；接受长度
- **关键结果 / 消融** · 最高改善 72%，平均 41%
- **适用条件 / 局限** · 接受长度不等价壁钟加速，需核算更新成本

**可复用机制** · 仅在预期生成较长的请求对照在线草稿更新

<a id="paper-148465"></a>

## Text as Partial Constraint: Core–Residual Alignment for Robust Vision–Language Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/148465) · [作者来源](https://openreview.net/forum?id=xc5RAI0YCe)

- **问题 / 瓶颈** · 图像信息常超出配套文本，强对齐可能抹掉细节
- **核心创新 / 方法** · 将核心对齐与视觉残差分建模
- **Baseline** · 普通对比图文对齐及强鲁棒基线
- **Benchmark** · ImageNet、Avg-14、POPE 和 OKVQA
- **关键结果 / 消融** · ImageNet 清洁和鲁棒 Top-1 为 81.42/64.05，POPE F1 为 85.16
- **适用条件 / 局限** · 核心与残差分解质量受文本充分度影响

**可复用机制** · 数据 captions 不完整时测哪些视觉属性在对齐后丢失

<a id="paper-139343"></a>

## Text-side fragility in contrastive vision-language retrieval

[官方论文页](https://neurips.cc/virtual/2026/poster/139343) · [作者来源](https://openreview.net/forum?id=VZDduyq0Lw)

- **问题 / 瓶颈** · 整体图文检索成绩可能掩盖文本端弱点
- **核心创新 / 方法** · 用匹配损伤分位比较图到文与文到图，再探测文本池化瓶颈
- **Baseline** · 清洁与损伤的图文查询
- **Benchmark** · 对比图文检索；Recall@1
- **关键结果 / 消融** · 文到图更脆弱，词汇破坏较词序破坏更关键
- **适用条件 / 局限** · 与词元化、池化及应用文本长度有关

**可复用机制** · 结构化场景检索分别测试内容词丢失和图像遮挡

<a id="paper-139514"></a>

## Text-to-CAD Evaluation with CADTests

[官方论文页](https://neurips.cc/virtual/2026/poster/139514) · [作者来源](https://openreview.net/forum?id=LITtdZUzkt)

- **问题 / 瓶颈** · 渲染相像不能证明拓扑合格
- **核心创新 / 方法** · 把文字要求转成可执行几何和拓扑测试，也用于候选生成筛选
- **Baseline** · 已有 Text-to-CAD 方法
- **Benchmark** · CADTestBench，几何与拓扑满足
- **关键结果 / 消融** · 简单的测试引导方法超过现有法，幅度未报告
- **适用条件 / 局限** · 仅覆盖可写为断言要求，主观设计需另评

**可复用机制** · 针对机器人资产生成分别测拓扑、碰撞和尺寸约束

<a id="paper-148848"></a>

## TGPO: Temporal Grounded Policy Optimization for Signal Temporal Logic Tasks

[官方论文页](https://neurips.cc/virtual/2026/poster/148848) · [作者来源](https://openreview.net/forum?id=uhy1JdsQsE)

- **问题 / 瓶颈** · 固定时限或只有终局奖励限制高维长任务
- **核心创新 / 方法** · 分阶段给密集奖励，推理中由 critic 选择时间分配
- **Baseline** · 现有时序逻辑策略方法
- **Benchmark** · 导航、操作、无人机和四足等五环境
- **关键结果 / 消融** · 摘要称成功率较最佳方法高 31.6%
- **适用条件 / 局限** · 需要形式任务规格和可估的阶段时限

**可复用机制** · 对分阶段操作核对改时限带来的合规与成功取舍

<a id="paper-151583"></a>

## TGRL: Temperature-Grouped Reinforcement Learning for Efficient Exploration in LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/151583) · [作者来源](https://openreview.net/forum?id=ZWkXIcPySl)

- **问题 / 瓶颈** · 固定采样温度可能无法同时覆盖稳定解和稀有解
- **核心创新 / 方法** · 将不同温度 rollout 纳入温度分组强化学习
- **Baseline** · 强 RLVR 基线
- **Benchmark** · 11 个数学、代码及工具任务
- **关键结果 / 消融** · 32B 数学均值增 1.6%，ALFWorld/WebShop 增 6.3%/4.9%
- **适用条件 / 局限** · 模型与任务温度分区需校验

**可复用机制** · 在固定样本数下测温度覆盖和单位墙钟收益

<a id="paper-150915"></a>

## The $1/\mathcal{W}$ Law: Context Length is the Dominant Energy Lever in LLM Inference Fleets

[官方论文页](https://neurips.cc/virtual/2026/poster/150915) · [作者来源](https://openreview.net/forum?id=eQmwjbxAVA)

- **问题 / 瓶颈** · 整机均值无法显示长上下文吞吐与能耗瓶颈
- **核心创新 / 方法** · 用工作负载和机群分析比较上下文路由、硬件与结构
- **Baseline** · 对照不同硬件及稀疏架构
- **Benchmark** · 机群推理能耗，与工作负载长短分布有关
- **关键结果 / 消融** · 摘要给架构级能效上界最高 5.1 倍
- **适用条件 / 局限** · 上界并非实测普遍增益，依赖机群与工作负载

**可复用机制** · 评估服务时按上下文长度报告每任务能量

<a id="paper-139050"></a>

## The AI Observatory: A Public Measure of Real-World AI Use

[官方论文页](https://neurips.cc/virtual/2026/poster/139050) · [作者来源](https://openreview.net/forum?id=o5j63mCxIq)

- **问题 / 瓶颈** · 单一来源难代表实际目标。
- **核心创新 / 方法** · 以共同 145 特征描述真实会话。
- **Baseline** · 单来源及职业用途。
- **Benchmark** · 23158 对话、85633 轮。
- **关键结果 / 消融** · 职业过滤去掉 48%。
- **适用条件 / 局限** · 采样及隐私限制覆盖。

**可复用机制** · 代理回归保留非职业使用切片。

<a id="paper-152268"></a>

## The Algorithm Is Not the Behavior: Learned Priors Override Look-Ahead in a Chess-Playing Neural Network

[官方论文页](https://neurips.cc/virtual/2026/poster/152268) · [作者来源](https://openreview.net/forum?id=ULhusDnCQy)

- **问题 / 瓶颈** · 行为错误可能并非前瞻缺失。
- **核心创新 / 方法** · 线性解码及因果干预观察棋步。
- **Baseline** · 正确与错误选择。
- **Benchmark** · 神经国际象棋。
- **关键结果 / 消融** · 错选时仍有正确后续表征。
- **适用条件 / 局限** · 其他任务须复测。

**可复用机制** · 分别评估候选规划与决策仲裁。

<a id="paper-152222"></a>

## The Alien Space of Science: Sampling Coherent but Cognitively Unavailable Research Directions

[官方论文页](https://neurips.cc/virtual/2026/poster/152222) · [作者来源](https://openreview.net/forum?id=UepmNYnfUe)

- **问题 / 瓶颈** · 默认采样倾向常见概念。
- **核心创新 / 方法** · 保文献一致并偏向低提议概率的组合。
- **Baseline** · 前沿 LLM。
- **Benchmark** · 16068 篇论文语料。
- **关键结果 / 消融** · 有效词汇覆盖宽 3.5 至 7 倍。
- **适用条件 / 局限** · 新颖不保证可研究。

**可复用机制** · 将方向熟悉程度和合理性分开评分。

<a id="paper-139819"></a>

## The Alignment Curse: Modality Alignment Supercharges Audio Attacks via Text Transfer

[官方论文页](https://neurips.cc/virtual/2026/poster/139819) · [作者来源](https://openreview.net/forum?id=2ueWNn2Xsh)

- **问题 / 瓶颈** · 能力改进可伴随风险。
- **核心创新 / 方法** · 比较对齐程度和安全评测。
- **Baseline** · 独立模态安全结果。
- **Benchmark** · 全模态模型黑盒安全。
- **关键结果 / 消融** · 摘要报告对齐程度影响安全风险。
- **适用条件 / 局限** · 仅限所测威胁与模型。

**可复用机制** · 把跨模态安全纳入对齐更新门。

<a id="paper-156077"></a>

## The Alignment Illusion in Multimodal Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/156077) · [作者来源](https://openreview.net/forum?id=0cLkbeOBGg)

- **问题 / 瓶颈** · 高相似未必表示共同语义。
- **核心创新 / 方法** · 比较前两个主夹角余弦的差。
- **Baseline** · 总体相似。
- **Benchmark** · 视觉和语言子空间。
- **关键结果 / 消融** · 区分权重诱导项和多方向视觉结构。
- **适用条件 / 局限** · 取决于所选层。

**可复用机制** · 同时看相似值和共享方向谱。

<a id="paper-152620"></a>

## The Alignment Tax Concentrates in Output Projections

[官方论文页](https://neurips.cc/virtual/2026/poster/152620) · [作者来源](https://openreview.net/forum?id=Rj4yyW4GB7)

- **问题 / 瓶颈** · 局部能力变化可和安全耦合。
- **核心创新 / 方法** · 比较投影模块变化与安全指标。
- **Baseline** · 对齐底座。
- **Benchmark** · 输出投影与拒答、安全测试。
- **关键结果 / 消融** · 一个模型因安全与结构重叠被排除。
- **适用条件 / 局限** · 安全样本有限。

**可复用机制** · 局部编辑不得以任务收益代替安全验收。

<a id="paper-150135"></a>

## The Alternation Depth Principle for Neural Operator Design

[官方论文页](https://neurips.cc/virtual/2026/poster/150135) · [作者来源](https://openreview.net/forum?id=kRVhNbueWa)

- **问题 / 瓶颈** · 总宽度不能表示耦合次序。
- **核心创新 / 方法** · 按方程所需最少交替阶段选容量。
- **Baseline** · FNO 变体和 KIN。
- **Benchmark** · 九初值集及 Darcy，736 次运行。
- **关键结果 / 消融** · 深度收益多在门槛后出现。
- **适用条件 / 局限** · 结构和任务限定。

**可复用机制** · 先列物理操作的依赖深度再定网络。

<a id="paper-153188"></a>

## The balance between feature learning and collapse in generative dynamical systems

[官方论文页](https://neurips.cc/virtual/2026/poster/153188) · [作者来源](https://openreview.net/forum?id=NB4cYMKKno)

- **问题 / 瓶颈** · 低秩可促简洁也会坍缩。
- **核心创新 / 方法** · 分析变分及流匹配的梯度秩。
- **Baseline** · 不同表示结构。
- **Benchmark** · 动力学生成和分布覆盖。
- **关键结果 / 消融** · 两类目标均可诱发低秩和分布坍缩。
- **适用条件 / 局限** · 依赖系统结构。

**可复用机制** · 不要用低秩单指标代表模型健康。

<a id="paper-155403"></a>

## The BatchNorm Illusion: Diagnosing Normalization Artifacts in Machine Unlearning Evaluation

[官方论文页](https://neurips.cc/virtual/2026/poster/155403) · [作者来源](https://openreview.net/forum?id=5uiFZ0FfMq)

- **问题 / 瓶颈** · 只前向就可能改变表面遗忘。
- **核心创新 / 方法** · 以状态校准算子隔离 BN 与权重。
- **Baseline** · 未控制 BN。
- **Benchmark** · 含 BN 遗忘架构。
- **关键结果 / 消融** · 差异可以完全来自运行统计。
- **适用条件 / 局限** · 其他有状态模块需单测。

**可复用机制** · 评估报告权重与缓冲状态的各自作用。

<a id="paper-150013"></a>

## The Bayesian Learning Rule Beyond KL Geometry

[官方论文页](https://neurips.cc/virtual/2026/poster/150013) · [作者来源](https://openreview.net/forum?id=lQY2mQuDx9)

- **问题 / 瓶颈** · KL 并非唯一能提供此类更新。
- **核心创新 / 方法** · 从混合空间散度推加性优化。
- **Baseline** · KL 几何。
- **Benchmark** · 至 CIFAR-100 实验。
- **关键结果 / 消融** · 支持与尾形可控，表现有竞争力。
- **适用条件 / 局限** · 新几何需可稳定计算。

**可复用机制** · 按目标支持和尾部风险选散度。

<a id="paper-153508"></a>

## The Benefits of Temporal Correlations: SGD Efficiently Learns k-Juntas from Random Walks

[官方论文页](https://neurips.cc/virtual/2026/poster/153508) · [作者来源](https://openreview.net/forum?id=KoUxx7CIP5)

- **问题 / 瓶颈** · 顺序样本可能传递额外信息。
- **核心创新 / 方法** · 比较惰性随机游走和批量学习 k-junta。
- **Baseline** · 大批量凸点损失。
- **Benchmark** · 固定 k、超立方体。
- **关键结果 / 消融** · 相关流样本复杂度近线性，常规大批不具同优势。
- **适用条件 / 局限** · 假设特殊。

**可复用机制** · 时序训练联合消融是否打散与批量大小。

<a id="paper-148450"></a>

## The Block Catastrophe of Marginal Calibration in Certified Requirements Traceability

[官方论文页](https://neurips.cc/virtual/2026/poster/148450) · [作者来源](https://openreview.net/forum?id=xjocfB8Qxp)

- **问题 / 瓶颈** · 边际证书可能掩盖块内失败。
- **核心创新 / 方法** · 分析边际和块风险的结构差。
- **Baseline** · 分布无关边际校准。
- **Benchmark** · 需求可追踪性认证。
- **关键结果 / 消融** · 差距可无界。
- **适用条件 / 局限** · 块定义需匹配使用流程。

**可复用机制** · 对重复或成组证据单验共同漏判概率。

<a id="paper-154844"></a>

## The Butterfly Effect in Reasoning: Branch-Structured Distributional Memory for Stochastic Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/154844) · [作者来源](https://openreview.net/forum?id=AUA2x6g9qo)

- **问题 / 瓶颈** · 单轨迹缺少失败参照。
- **核心创新 / 方法** · 短前缀分簇后扩展代表并写入记忆。
- **Baseline** · 单轨迹等选轨迹。
- **Benchmark** · GPQA-Diamond、MATH500。
- **关键结果 / 消融** · 相对增 8.7% 和 2.2%，延迟近似。
- **适用条件 / 局限** · 依赖分支覆盖。

**可复用机制** · 让记忆记录替代行为的结果。

<a id="paper-152642"></a>

## The Capability Frontier of GRPO

[官方论文页](https://neurips.cc/virtual/2026/poster/152642) · [作者来源](https://openreview.net/forum?id=RTt9K8h5PK)

- **问题 / 瓶颈** · 固定 rollout 亏在太易和几乎全错。
- **核心创新 / 方法** · 从成功率跟踪有效组规模。
- **Baseline** · 固定 G 8 至 128。
- **Benchmark** · 三个家族，MATH-500、GSM8K。
- **关键结果 / 消融** · 同预算各加 4.2–5.3 和 2.4–3.4 点。
- **适用条件 / 局限** · 在线预估难度要校准。

**可复用机制** · 总采样固定时按能产生相对反馈的概率调组。

<a id="paper-155556"></a>

## The Commit-Abstain Circuit: Why Language Models Hallucinate Instead of Abstaining

[官方论文页](https://neurips.cc/virtual/2026/poster/155556) · [作者来源](https://openreview.net/forum?id=4gAoZ2eJTM)

- **问题 / 瓶颈** · 最终生成无法显示过早承诺何时产生。
- **核心创新 / 方法** · 定位促承诺与促拒答的注意力头和 MLP。
- **Baseline** · 原模型及因果门控对照。
- **Benchmark** · 十个模型、五家族、三基准。
- **关键结果 / 消融** · 发现先承诺后纠正不足的稳定模式。
- **适用条件 / 局限** · 摘要未给泛化效应量。

**可复用机制** · 诊断过度回答时应分别测早期承诺形成和后层是否及时纠正。

<a id="paper-151154"></a>

## The Communication Bottleneck: A Round-Trip Study of Compositional Serialization in Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151154) · [作者来源](https://openreview.net/forum?id=ccZsQE4QdK)

- **问题 / 瓶颈** · 终点准确率混合生成表达与接收解析质量。
- **核心创新 / 方法** · 一模型转述结构，另一模型从文本还原，符号等价验收。
- **Baseline** · 十五模型两两交叉。
- **Benchmark** · 组合层级表达的通信矩阵。
- **关键结果 / 消融** · 摘要报告信道有损且换角色会改变结果。
- **适用条件 / 局限** · 需要可验证结构，未覆盖自然对话。

**可复用机制** · 多代理通信测评应交换角色以隔离发送和提取能力。

<a id="paper-138945"></a>

## The Complexity Kink: LLM Rubric Instruments for Causal Inference on Code Generation Reliability

[官方论文页](https://neurips.cc/virtual/2026/poster/138945) · [作者来源](https://openreview.net/forum?id=ucjCOJf47M)

- **问题 / 瓶颈** · 表面通过率断点会被任务分布或测试误差混淆。
- **核心创新 / 方法** · 用多个 rubric 难度信号及独立审阅检查通过率。
- **Baseline** · 不同模型、题群和评分口径。
- **Benchmark** · 21 模型约 10.5 万生成。
- **关键结果 / 消融** · 聚合准确率在断点两侧为 83.4% 与 90.1%，作者强调并非难度定律。
- **适用条件 / 局限** · rubric 与审计依赖模型评审。

**可复用机制** · 难度指标应通过受控重加权验证后才用于课程设计。

<a id="paper-151832"></a>

## The Compliance Trap: Diagnosing How AI Agents Consume Conflicting Memory

[官方论文页](https://neurips.cc/virtual/2026/poster/151832) · [作者来源](https://openreview.net/forum?id=XbuaSCh5Nt)

- **问题 / 瓶颈** · 检索正确与最终成功无法解释中间受污染动作。
- **核心创新 / 方法** · 沿工具轨迹对照有无冲突记忆。
- **Baseline** · 仅看检索或总体成功。
- **Benchmark** · 多步记忆代理轨迹。
- **关键结果 / 消融** · 摘要支持按行为传播阶段诊断。
- **适用条件 / 局限** · 依赖可观测动作。

**可复用机制** · 记忆管理需要判断影响何时发生，再把控制放到具体环节。

<a id="paper-156795"></a>

## The Confusion is Real: GRAPHIC – A Network Science Approach to Confusion Matrices in Deep Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/156795) · [作者来源](https://openreview.net/forum?id=UP9bx1WJwR)

- **问题 / 瓶颈** · 单层准确率无法识别类别关系形成过程。
- **核心创新 / 方法** · 以线性探针生成混淆图并跨深度和训练期比较。
- **Baseline** · 普通终点混淆矩阵。
- **Benchmark** · 中间表示与训练学习动态。
- **关键结果 / 消融** · 摘要报告能揭示真实混淆结构。
- **适用条件 / 局限** · 线性探针不是完整行为。

**可复用机制** · 想知道训练中哪些类逐渐分离，可比较混淆图而不只看探针总分。

<a id="paper-151175"></a>

## The Cost of Absolute Position: A Spread-Expressivity Tradeoff for Additive Positional Encodings

[官方论文页](https://neurips.cc/virtual/2026/poster/151175) · [作者来源](https://openreview.net/forum?id=cR4hyys307)

- **问题 / 瓶颈** · 可区分绝对位置会给等变性引入代价。
- **核心创新 / 方法** · 分析去均值嵌入展开对注意力风险的上下界。
- **Baseline** · 加法位置编码及 RoPE、ALiBi 的位移比较。
- **Benchmark** · 带均值池化的 softmax 注意力理论。
- **关键结果 / 消融** · 最小绝对位置分离要求一定展开。
- **适用条件 / 局限** · 匹配理论界只适用于所述加法族。

**可复用机制** · 先决定任务需多少绝对位置细节，再检查其代价是否损害平移泛化。

<a id="paper-148377"></a>

## The Cost of Mismatch: Noise Amplification in Zeroth-Order Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/148377) · [作者来源](https://openreview.net/forum?id=yLUddZsQl0)

- **问题 / 瓶颈** · 不匹配在线样本导致噪声放大。
- **核心创新 / 方法** · 分析成对差分的方差并比较匹配训练。
- **Baseline** · 不匹配的零阶评估及其他微调。
- **Benchmark** · 推理强化学习，含 Distill-Qwen-1.5B，比较训练稳定性和峰值显存。
- **关键结果 / 消融** · 摘要报告匹配数据改善可靠性，显存接近推理。
- **适用条件 / 局限** · 需要可复用样本和可比评估。

**可复用机制** · 有限差分先固定能固定的随机源，避免把样本变化当成参数响应。

<a id="paper-154497"></a>

## The Curse of Multiple Mediators: Hidden Interaction Effects in Activation Patching

[官方论文页](https://neurips.cc/virtual/2026/poster/154497) · [作者来源](https://openreview.net/forum?id=DA12jH1hET)

- **问题 / 瓶颈** · 逐个干预会漏掉仅联合激活时有效的路径。
- **核心创新 / 方法** · 拆分单中介和相互依赖的因果影响。
- **Baseline** · 按单组件 NIE 贪心排序。
- **Benchmark** · GPT-2 IOI 电路。
- **关键结果 / 消融** · 摘要展示多种排序和干预失败。
- **适用条件 / 局限** · 定量边界未报告，受提示和模型范围限制。

**可复用机制** · 定位能力模块时用成组反事实验证单组件结论。

<a id="paper-140002"></a>

## The Dead Salmons of AI Interpretability: The Need for a Statistical Inference Perspective

[官方论文页](https://neurips.cc/virtual/2026/poster/140002) · [作者来源](https://openreview.net/forum?id=w0wOa4UDHv)

- **问题 / 瓶颈** · 随机网络也能产出貌似合理的解释。
- **核心创新 / 方法** · 比较归因、探针、稀疏分解和因果解释的空模型现象。
- **Baseline** · 随机网络及正常网络。
- **Benchmark** · 多类解释性方法，立场论文汇总。
- **关键结果 / 消融** · 指出仅凭解释外观容易出现伪发现。
- **适用条件 / 局限** · 摘要未给统一跨方法效应量。

**可复用机制** · 对解释结果报告相对于空模型的增益，再判断是否恢复了训练所得机制。

<a id="paper-155970"></a>

## The Denoising Wrapper: A Modular Post-Processing Framework for Noisy First-Order Optimizers

[官方论文页](https://neurips.cc/virtual/2026/poster/155970) · [作者来源](https://openreview.net/forum?id=1UGggkyD1E)

- **问题 / 瓶颈** · 高噪梯度降低了现有一阶优化的有效更新。
- **核心创新 / 方法** · 以梯度和 Hessian 的统计估计净化 noisy 更新。
- **Baseline** · 普通 SGD、Adam 及噪声训练方案。
- **Benchmark** · 二次与三次优化和 CIFAR-10 的隐私训练。
- **关键结果 / 消融** · 摘要报告相较基线改善。
- **适用条件 / 局限** · 需要可用局部模型，摘要未给去噪成本。

**可复用机制** · 高噪训练可先判断能否改善输入梯度，而无需更换优化器核心。

<a id="paper-153185"></a>

## The Design Space of Tri-Modal Masked Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153185) · [作者来源](https://openreview.net/forum?id=NBUCuy2uaq)

- **问题 / 瓶颈** · 跨模态和批次扩大改变梯度噪声与预算的平衡。
- **核心创新 / 方法** · 在 AdamW 的 SDE 参数化下估计临界批次并引入漂移时域插值。
- **Baseline** · 不同批次、噪声日程和掩码设置。
- **Benchmark** · 三模态生成，含文本、图像和语音。
- **关键结果 / 消融** · 摘要报告 3B 训练模型在三种生成任务表现有竞争力。
- **适用条件 / 局限** · 规模和多因素共变，摘要未给各增益。

**可复用机制** · 多模态模型扩批需要验证优化步数和随机噪声是否都处于适宜区间。

<a id="paper-150735"></a>

## The Dormant Spiking Neuron: A State-Driven Mechanism for Efficient Spiking Neural Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/150735) · [作者来源](https://openreview.net/forum?id=fmUnrAKlSL)

- **问题 / 瓶颈** · 不太可能发放的神经元持续更新浪费计算。
- **核心创新 / 方法** · 用膜电位过阈触发休眠门。
- **Baseline** · 普通脉冲神经元。
- **Benchmark** · 脉冲 ResNet-18 等神经形态计算设定。
- **关键结果 / 消融** · 摘要报告效率收益。
- **适用条件 / 局限** · 依赖阈值与硬件可跳过能力，数值未报告。

**可复用机制** · 动态稀疏可根据内部状态预测无贡献模块，而非等输出后才发现零值。

<a id="paper-152081"></a>

## The Dynamic-Probabilistic Consistency Gap in Chaotic Surrogate Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/152081) · [作者来源](https://openreview.net/forum?id=VcROOA5wBN)

- **问题 / 瓶颈** · 高斯外推损失可能鼓励压低真实不稳定性或让噪声掩盖误差。
- **核心创新 / 方法** · 识别三类失配，并以 KAFFEE 适配代理滤波。
- **Baseline** · 普通开环概率预测。
- **Benchmark** · 13 个混沌系统的动态与滤波。
- **关键结果 / 消融** · 摘要报告支持上下文贝叶斯滤波并大体保留零样本动力学。
- **适用条件 / 局限** · 限所测模型和混沌域。

**可复用机制** · 不确定度校准须检查是否来自真实状态扰动传播，而不是独立噪声头。

<a id="paper-151912"></a>

## The Dynamics of Policy Gradient in Social Dilemmas with Partner Selection

[官方论文页](https://neurips.cc/virtual/2026/poster/151912) · [作者来源](https://openreview.net/forum?id=WxOMxfirif)

- **问题 / 瓶颈** · 伙伴选择改变对手分布，均质群体可能阻碍合作。
- **核心创新 / 方法** · 分析社会困境策略梯度并用随机过程描述演化。
- **Baseline** · 固定或不同伙伴机制。
- **Benchmark** · 社会困境与模拟多代理群体。
- **关键结果 / 消融** · 模型中方差是合作出现的必要条件。
- **适用条件 / 局限** · 依赖简化行为模型。

**可复用机制** · 多代理学习既要对照伙伴策略，也要控制代理群体多样性。

<a id="paper-154763"></a>

## The Era of Agentic Organization: Learning to Organize with Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154763) · [作者来源](https://openreview.net/forum?id=B83FJLtGn8)

- **问题 / 瓶颈** · 固定并行可能等待无关分支。
- **核心创新 / 方法** · 调度器分派子问题并合并中间知识，用 RL 学协调。
- **Baseline** · 固定并行思考。
- **Benchmark** · 数学推理与未见任务。
- **关键结果 / 消融** · 延迟降 28%，摘要报告推理表现提高。
- **适用条件 / 局限** · 依赖可分任务及并发资源。

**可复用机制** · 多代理预算受限时，可让调度器主动合并必要证据而非同步等待所有分支。

<a id="paper-139594"></a>

## The Fault in Our Metrics: Revisiting Generative Model Evaluation with Chamfer Distance

[官方论文页](https://neurips.cc/virtual/2026/poster/139594) · [作者来源](https://openreview.net/forum?id=GST0loGJ8O)

- **问题 / 瓶颈** · 小样本中近邻扩张的支持集会夸大评价
- **核心创新 / 方法** · 用 Chamfer 的两单向分量测真实与生成集合距离
- **Baseline** · 基于近邻扩张的生成评测
- **Benchmark** · 有限样本评估；忠实、覆盖、近邻敏感性
- **关键结果 / 消融** · 摘要称较少依赖近邻超参且计算可行
- **适用条件 / 局限** · 受特征度量、离群值和样本量影响

**可复用机制** · 固定嵌入及样本量，分别报告两向误差

<a id="paper-155998"></a>

## The Future of Facts: Tracing the Factual Generation-Verification Gap

[官方论文页](https://neurips.cc/virtual/2026/poster/155998) · [作者来源](https://openreview.net/forum?id=1Gv8dhNp6R)

- **问题 / 瓶颈** · 模型可能验证正确事实却不能生成它，也可能同时认可冲突事实
- **核心创新 / 方法** · 追踪持续学习后的两类行为并加前沿模型自然实验
- **Baseline** · 生成与验证、更新之前与之后
- **Benchmark** · 跨模型事实学习、持续更新与自然实验
- **关键结果 / 消融** · 验证先学、较耐遗忘；更新后可认可新旧答案
- **适用条件 / 局限** · 验证任务设计和选项先验会影响现象

**可复用机制** · 把事实编辑验收写成自由回忆和互斥选择两个不同测试

<a id="paper-150166"></a>

## The Geometric Inductive Bias of Grokking: Bypassing Phase Transitions via Architectural Topology

[官方论文页](https://neurips.cc/virtual/2026/poster/150166) · [作者来源](https://openreview.net/forum?id=kBjWa3dNvG)

- **问题 / 瓶颈** · 通用拓扑先验可能在非交换任务上无效
- **核心创新 / 方法** · 跨循环算术和非交换任务对照结构约束
- **Baseline** · 标准架构与引入几何对称结构的变体
- **Benchmark** · 受控算术任务及泛化延迟
- **关键结果 / 消融** · 循环任务消除延迟，非交换任务不复现
- **适用条件 / 局限** · 合成代数任务支持机制，不能外推所有推理任务

**可复用机制** · 按问题的变换群选结构并保留不匹配负对照

<a id="paper-155185"></a>

## The Geometric Wall: Manifold Structure Predicts Layerwise Sparse Autoencoder Scaling Laws

[官方论文页](https://neurips.cc/virtual/2026/poster/155185) · [作者来源](https://openreview.net/forum?id=7eqIUZyAMz)

- **问题 / 瓶颈** · 增大字典可能仍无法线性重构弯曲表示
- **核心创新 / 方法** · 拟合资源标度下的残差下限，与曲率和内在维度比较
- **Baseline** · 不同层和不同字典容量
- **Benchmark** · 层级几何及稀疏重建标度
- **关键结果 / 消融** · 高曲率与高内在维度层残差下限更高
- **适用条件 / 局限** · 从拟合下限推断几何仍依赖测量

**可复用机制** · 部署解释工具先测待分析层是否需要非线性基元

<a id="paper-148408"></a>

## The Geometry of Agent Skills: Non-Commutative Composition in Representation Space

[官方论文页](https://neurips.cc/virtual/2026/poster/148408) · [作者来源](https://openreview.net/forum?id=y5GTIdP1fS)

- **问题 / 瓶颈** · 分别可用的技能互换时结果可能不同
- **核心创新 / 方法** · 估计表示空间中的顺序交换残差，再与行为缺口比较
- **Baseline** · 低交换残差与合成系统
- **Benchmark** · 技能对、交换行为缺口及表示新颖度
- **关键结果 / 消融** · 相关性 Spearman 为 0.918/0.889
- **适用条件 / 局限** · 表征差分需固定起始上下文

**可复用机制** · 给技能库增加顺序兼容矩阵和失败反例

<a id="paper-149138"></a>

## The Geometry of Forgetting: Temporal Knowledge Drift as an Independent Axis in LLM Representations

[官方论文页](https://neurips.cc/virtual/2026/poster/149138) · [作者来源](https://openreview.net/forum?id=sZ9wFqGDVd)

- **问题 / 瓶颈** · 输出信心不能区分不同知识状态
- **核心创新 / 方法** · 固定输入，比较训练截止日期在事实变化前后的模型探针
- **Baseline** · 不同截止日期模型和输出置信
- **Benchmark** · 12 对模型的知识变化检测
- **关键结果 / 消融** · 排序概率 0.975–0.998
- **适用条件 / 局限** · 探针需校准并只在验证过的更新类型上解释

**可复用机制** · 时间敏感助手监控版本差异并用外部日期证据核验

<a id="paper-149230"></a>

## The Geometry of Generative Latents: Navigability and Invertibility

[官方论文页](https://neurips.cc/virtual/2026/poster/149230) · [作者来源](https://openreview.net/forum?id=ryTKhFAIv3)

- **问题 / 瓶颈** · 增加多层特征虽帮助重建却可能扭曲生成空间
- **核心创新 / 方法** · 在法向空间投影融合冻结 DINOv3 多层特征
- **Baseline** · 不受约束的融合及匹配 RAE
- **Benchmark** · 文生图及重建，名称和数值未报告
- **关键结果 / 消融** · 维持重建优势并避开生成退化
- **适用条件 / 局限** · 依赖潜空间法向结构与所选骨干

**可复用机制** · 图像 tokenizer 验收加入潜空间插值和生成对照

<a id="paper-153734"></a>

## The Hidden Power of Scaling Factor in LoRA Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/153734) · [作者来源](https://openreview.net/forum?id=J9AbM86AH7)

- **问题 / 瓶颈** · 绑定 rank 的启发式会让小学习率不适配
- **核心创新 / 方法** · 以分析建议的缩放范围设置 LoRA-alpha
- **Baseline** · 现有秩绑定启发式
- **Benchmark** · 不同任务的 LoRA 微调
- **关键结果 / 消融** · 摘要称表现改善且搜索更简单
- **适用条件 / 局限** · 摘要未列建议的数值区间，范围按配置复算

**可复用机制** · 改变秩时控制有效步长再比较参数效率

<a id="paper-149477"></a>

## The Horizon Threshold in Cooperative Multi-Agent Reward-Free Exploration

[官方论文页](https://neurips.cc/virtual/2026/poster/149477) · [作者来源](https://openreview.net/forum?id=ppLDIdDiWm)

- **问题 / 瓶颈** · 一次派很多代理不保证补足逐步信息。
- **核心创新 / 方法** · 比较更少阶段时需增加的代理数。
- **Baseline** · 不同探索阶段和代理数。
- **Benchmark** · 合作无奖励探索，长度 H。
- **关键结果 / 消融** · 低于 H 阶段需至少 A 的 H/ρ 次方代理；线性阶段允许多项式代理。
- **适用条件 / 局限** · 依赖理论信息及任务模型。

**可复用机制** · 设计并行采集时同时算自适应轮数和硬件规模。

<a id="paper-149941"></a>

## The Illusion of Diversity: Aligning LLM Exploration via Effective Entropy

[官方论文页](https://neurips.cc/virtual/2026/poster/149941) · [作者来源](https://openreview.net/forum?id=m3JyxgA0c5)

- **问题 / 瓶颈** · 总体熵增加可能来自错误轨迹。
- **核心创新 / 方法** · 给有效子空间定义熵并优化。
- **Baseline** · GRPO 和熵变体。
- **Benchmark** · 多个推理基准。
- **关键结果 / 消融** · 持续优于对照，幅度未核。
- **适用条件 / 局限** · 需验证器，正样本少时不确定。

**可复用机制** · 将正确多样性与错误多样性独立监控。

<a id="paper-153910"></a>

## The Illusion of Forgetting: Rank Leakage in Knowledge Editing and Its Mitigation

[官方论文页](https://neurips.cc/virtual/2026/poster/153910) · [作者来源](https://openreview.net/forum?id=HlaLfuxgVy)

- **问题 / 瓶颈** · 编辑后的普通输出掩盖未清除信号。
- **核心创新 / 方法** · 在编辑阶段显式约束被删除内容的词排名。
- **Baseline** · 标准知识编辑。
- **Benchmark** · 多模型数据算法，对抗性隐私和效用。
- **关键结果 / 消融** · 抗泄漏提升且编辑质量保持。
- **适用条件 / 局限** · 需要目标标注和独立防御验收。

**可复用机制** · 用隐含状态的泄露指标补充表面回答测试。

<a id="paper-139826"></a>

## The Illusion of Multi-Agent Advantage

[官方论文页](https://neurips.cc/virtual/2026/poster/139826) · [作者来源](https://openreview.net/forum?id=2TcjzzhWse)

- **问题 / 瓶颈** · 流程更复杂不等于有效分工。
- **核心创新 / 方法** · 比较自动和专家架构，并用明确可拆任务诊断。
- **Baseline** · CoT-SC。
- **Benchmark** · 传统推理、BrowseComp-Plus 及组合任务。
- **关键结果 / 消融** · 自动 MAS 至多贵 10 倍仍低于单代理。
- **适用条件 / 局限** · 结论限所测机制，不代表所有编排。

**可复用机制** · 先测上下文隔离与并行价值再上线多代理。

<a id="paper-148340"></a>

## The Implicit Bias of Hyperbolic Representation Learning for Multiclass Data: A Busemann Risk Perspective

[官方论文页](https://neurips.cc/virtual/2026/poster/148340) · [作者来源](https://openreview.net/forum?id=yZCszLIehq)

- **问题 / 瓶颈** · 边界占用可能是优化偏差。
- **核心创新 / 方法** · 按 Busemann 风险推漂移方向与渐进。
- **Baseline** · 不同漂移系数情形。
- **Benchmark** · 双曲多类嵌入理论。
- **关键结果 / 消融** · 漂移正时半径按半对数增长，负时回阈内。
- **适用条件 / 局限** · 依赖持久漂移与风险模型。

**可复用机制** · 选双曲表征时报告边界幅度而非仅聚类分数。

<a id="paper-155660"></a>

## The Interplay of Data Structure and Imbalance in the Learning Dynamics of Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155660) · [作者来源](https://openreview.net/forum?id=3xmpzYAkAo)

- **问题 / 瓶颈** · 样本量不能单独决定学习先后。
- **核心创新 / 方法** · 分析不同类数据几何及不平衡。
- **Baseline** · 按类别频率解释。
- **Benchmark** · 扩散类别动态。
- **关键结果 / 消融** · 较高方差优先学习，质心次要，可先记住一类而欠拟合另一类。
- **适用条件 / 局限** · 需在真实类分布重测。

**可复用机制** · 监控每类泛化和记忆，重采样同时考虑方差。

<a id="paper-149891"></a>

## The Invisible Hand of Physics: When Video Diffusion Models Know More Than They Show

[官方论文页](https://neurips.cc/virtual/2026/poster/149891) · [作者来源](https://openreview.net/forum?id=mTYG9xSbYv)

- **问题 / 瓶颈** · 视频违背物理不一定缺相关内部信号。
- **核心创新 / 方法** · 从生成状态恢复轨迹，用线性分类探针。
- **Baseline** · V-JEPA、VideoMAE。
- **Benchmark** · IntPhys、InfLevel。
- **关键结果 / 消融** · 平均约 81% 解码准确率。
- **适用条件 / 局限** · 可解码不等于生成使用或理解。

**可复用机制** · 重点查有物理表征却未用于控制的任务。

<a id="paper-149008"></a>

## The Kernel Reality Check: Benchmarking and Distilling Efficient Attention at Scale

[官方论文页](https://neurips.cc/virtual/2026/poster/149008) · [作者来源](https://openreview.net/forum?id=tVaxhv0A2z)

- **问题 / 瓶颈** · 小模型排名难迁移到基础模型。
- **核心创新 / 方法** · 用自适应提议的近似重要性采样，开发 LARA++。
- **Baseline** · softmax 与既有核法。
- **Benchmark** · 基础模型规模评测和蒸馏。
- **关键结果 / 消融** · 最高恢复 softmax 准确率的 99%。
- **适用条件 / 局限** · 序列长度和实际吞吐需独立复验。

**可复用机制** · 用近似误差解释速度精度权衡。

<a id="paper-151267"></a>

## The Key to Going Linear: Analysis-Driven Transformer Linearization

[官方论文页](https://neurips.cc/virtual/2026/poster/151267) · [作者来源](https://openreview.net/forum?id=bekG7rxPRG)

- **问题 / 瓶颈** · 纯门控累积缺少低秩投影能力。
- **核心创新 / 方法** · 分析投影后增 sink、短卷积、固定缓存路由。
- **Baseline** · 门控累计及 delta 网络。
- **Benchmark** · Transformer 线性化。
- **关键结果 / 消融** · 结构修改减小残余差距，幅度未核。
- **适用条件 / 局限** · 组件增益和预算需拆开测。

**可复用机制** · 用可解释的关键算子指导学生结构。

<a id="paper-138957"></a>

## The Labeling Problem in Hallucination Detection Benchmarks: An Empirical Evaluation

[官方论文页](https://neurips.cc/virtual/2026/poster/138957) · [作者来源](https://openreview.net/forum?id=tzJJksX8Y9)

- **问题 / 瓶颈** · 短参考未覆盖所有正确回答。
- **核心创新 / 方法** · 比较词法、NLI 与七种 LLM 评判提示。
- **Baseline** · 各自动标签方法。
- **Benchmark** · 开放域 QA 幻觉。
- **关键结果 / 消融** · 自动标签明显分歧。
- **适用条件 / 局限** · 结果受参考完整性和裁判影响。

**可复用机制** · 在发布检测基准前分别标不支持和错误。

<a id="paper-155777"></a>

## The Laplacian Keyboard: Beyond the Linear Span

[官方论文页](https://neurips.cc/virtual/2026/poster/155777) · [作者来源](https://openreview.net/forum?id=2xN81qKlwF)

- **问题 / 瓶颈** · 单层组合策略覆盖有限。
- **核心创新 / 方法** · 用 Laplacian Keyboard 学分层结构。
- **Baseline** · 原零样本解及标准 RL。
- **Benchmark** · 任务泛化、样本效率。
- **关键结果 / 消融** · 有逼近界，效果和样本利用改善。
- **适用条件 / 局限** · 依赖状态结构与层级可学。

**可复用机制** · 遇子任务组合误差测试是否受原技能线性跨度限制。

<a id="paper-154055"></a>

## The limbic navigation system as a hierarchical RNN

[官方论文页](https://neurips.cc/virtual/2026/poster/154055) · [作者来源](https://openreview.net/forum?id=GYHjzo1bhV)

- **问题 / 瓶颈** · 混合信号难查空间表示错因。
- **核心创新 / 方法** · 层级循环网分头积分并干预验证。
- **Baseline** · 神经实验观测作参照。
- **Benchmark** · 角与位置路径积分。
- **关键结果 / 消融** · 信息流与既有实验一致。
- **适用条件 / 局限** · 主要是生物启发模型，真实机器人待验证。

**可复用机制** · 以任务依赖拆运行记忆，定点测各层对位姿贡献。

<a id="paper-153541"></a>

## The Limits of AI-Driven Allocation: Optimal Screening under Aleatoric Uncertainty

[官方论文页](https://neurips.cc/virtual/2026/poster/153541) · [作者来源](https://openreview.net/forum?id=KanvRVjn7U)

- **问题 / 瓶颈** · 直接审查最高风险可能重复已明确动作。
- **核心创新 / 方法** · 通过选择性筛查和直接干预联合优化。
- **Baseline** · 按最高风险全送审。
- **Benchmark** · 带内生不确定性的资源分配理论。
- **关键结果 / 消融** · 最优策略在边界筛查、直接处理最高风险。
- **适用条件 / 局限** · 需要风险排序和审查可改变结局。

**可复用机制** · 人工复核优先布在行动决策可能翻转的位置。

<a id="paper-150207"></a>

## The Locality Cost of Semantic Patch Self-Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/150207) · [作者来源](https://openreview.net/forum?id=jvnyjDi5md)

- **问题 / 瓶颈** · 语义预测偏向对不可预测变化平均。
- **核心创新 / 方法** · 用无需标签的局部证据测多个目标和规模。
- **Baseline** · 不同辅助 patch 目标及底座。
- **Benchmark** · 细粒对应和语义抽象。
- **关键结果 / 消融** · 一致出现语义提升而局部对应退化。
- **适用条件 / 局限** · 取决于掩码与可预测区域。

**可复用机制** · 具身感知选视觉主干应同时测抽象和局部追踪。

<a id="paper-153073"></a>

## The Many Faces of On-Policy Distillation: Pitfalls, Mechanisms, and Fixes

[官方论文页](https://neurips.cc/virtual/2026/poster/153073) · [作者来源](https://openreview.net/forum?id=OCD8O5lBRt)

- **问题 / 瓶颈** · 教师或损失选错会使学生退化。
- **核心创新 / 方法** · 对照停止梯度 TopK、RLVR 教师及先 SFT 学生。
- **Baseline** · 原 OPD、OPSD。
- **Benchmark** · 数学推理和提示/知识内化。
- **关键结果 / 消融** · 特权不可用时所测 OPSD 失败，所提手段缓和。
- **适用条件 / 局限** · 结论依赖任务和教师。

**可复用机制** · 以可用信息匹配判断蒸馏能否迁移。

<a id="paper-152788"></a>

## The Many Senses of Visual Similarity: A Text-Prompted Image Perceptual Metric

[官方论文页](https://neurips.cc/virtual/2026/poster/152788) · [作者来源](https://openreview.net/forum?id=QKvTvdH8iS)

- **问题 / 瓶颈** · 单距离混合风格、对象与布局。
- **核心创新 / 方法** · 用多维自由文本的人类三元组判断训练文本条件度量。
- **Baseline** · 前沿 VLM 和人间一致。
- **Benchmark** · 多语义图像三元组，检索与生成评估。
- **关键结果 / 消融** · 更接近人类，域外保持。
- **适用条件 / 局限** · 不同人对同维度理解亦可分歧。

**可复用机制** · 按任务目标选择感知相似标准，而非全局同距离。

<a id="paper-153780"></a>

## The Marauder’s Map: Bézier Manifolds Reveal Hidden Surfaces for Model Merging and Ensembling

[官方论文页](https://neurips.cc/virtual/2026/poster/153780) · [作者来源](https://openreview.net/forum?id=Iig20MDcGt)

- **问题 / 瓶颈** · 只沿线和面连接难覆盖多专家。
- **核心创新 / 方法** · 用 Bézier 流形及按交互阶共享校正张量。
- **Baseline** · 既有一维与二维 mode connectivity。
- **Benchmark** · 多专家权重和任务能力。
- **关键结果 / 消融** · 可用少校正张量支持多任务。
- **适用条件 / 局限** · 依赖专家结构可对齐并验证曲面内点。

**可复用机制** · 选合并权重时保留可导航族而非只选端点和均值。

<a id="paper-153386"></a>

## The Mask Is Not the Object: Volumetric Supervision for 3D Gaussian Segmentation

[官方论文页](https://neurips.cc/virtual/2026/poster/153386) · [作者来源](https://openreview.net/forum?id=Lm87XRTCbZ)

- **问题 / 瓶颈** · 渲染梯度偏向视觉贡献高的高斯点，漏掉同对象图元。
- **核心创新 / 方法** · RGB 拟合后增加深度相关的体积监督。
- **Baseline** · 基于渲染特征的分割。
- **Benchmark** · Removal-3D、LERF、ScanNet。
- **关键结果 / 消融** · 改善体积分割，同时维持或提高通常的表面指标。
- **适用条件 / 局限** · 依赖优化后同物体图元深度结构。

**可复用机制** · 要编辑整个物体，应测形状体积中的归属，别只验证渲染可见表面。

<a id="paper-152307"></a>

## The Master Key Hypothesis: Unlocking Cross-Model Capability Transfer via Linear Subspace Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/152307) · [作者来源](https://openreview.net/forum?id=U3GUy7xRmI)

- **问题 / 瓶颈** · 直接复用激活向量会受坐标差异影响。
- **核心创新 / 方法** · 在有无能力的源变体中取对照向量，以低秩线性变换匹配目标模型。
- **Baseline** · 不使用迁移与未对齐控制作为方法背景。
- **Benchmark** · 逐步推理与数学任务。
- **关键结果 / 消融** · 摘要报告行为显著改善。
- **适用条件 / 局限** · 需要匹配输入与存在潜在能力的目标，未报告普适性。

**可复用机制** · 在缺少目标标签时可先比较目标模型是否具备能对齐的能力子空间。

<a id="paper-155865"></a>

## The Mechanism of Weak-to-Strong Generalization: Feature Elicitation from Latent Knowledge

[官方论文页](https://neurips.cc/virtual/2026/poster/155865) · [作者来源](https://openreview.net/forum?id=2Ibq2ITNEb)

- **问题 / 瓶颈** · 激活弱教师领域时可能损伤已有非目标知识。
- **核心创新 / 方法** · 分析两层网络中预训练低维子空间的重叠。
- **Baseline** · 不同相关度的非目标特征。
- **Benchmark** · 弱到强奖励模型训练及合成验证。
- **关键结果 / 消融** · 证明特定条件下可恢复目标能力，相关性可诱发遗忘。
- **适用条件 / 局限** · 限制为简化网络与合成数据。

**可复用机制** · 评估弱教师迁移时应兼顾未直接监督能力的保留。

<a id="paper-154263"></a>

## The Minimax Rate of Second-Order Calibration

[官方论文页](https://neurips.cc/virtual/2026/poster/154263) · [作者来源](https://openreview.net/forum?id=F64zJN7pvL)

- **问题 / 瓶颈** · 分箱和核估计样本收敛慢。
- **核心创新 / 方法** · 用解析平滑刻画和多项式回归估计。
- **Baseline** · 分箱及核平滑。
- **Benchmark** · 二阶校准误差实验。
- **关键结果 / 消融** · 理论率接近 n 的负二分之一次方，超出分箱的负四分之一次方。
- **适用条件 / 局限** · 依赖所设解析范围和平滑。

**可复用机制** · 误差分布平滑时可替换离散分箱，并用收敛率验证校准估计。

<a id="paper-151835"></a>

## The Mirage of Optimizing Training Policies: Monotonic Inference Policies as the Real Objective for LLM Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151835) · [作者来源](https://openreview.net/forum?id=XZFFNg98QZ)

- **问题 / 瓶颈** · 训练和推理参数同步也可能对轨迹赋不同概率。
- **核心创新 / 方法** · 以推理侧差距代理评估更新候选。
- **Baseline** · 训练侧重要性或稳定策略的 RL 方法。
- **Benchmark** · 高训练推理不匹配条件的推理训练。
- **关键结果 / 消融** · 作者报告推理效果和训练稳定性提升。
- **适用条件 / 局限** · 摘要未给在哪些引擎有足够偏移。

**可复用机制** · 强化学习上线前验证部署引擎策略，而非把训练概率当作动作分布。

<a id="paper-139327"></a>

## The Missing Corpus: Infinite Ground Truth for File-Grounded LLM Evaluation

[官方论文页](https://neurips.cc/virtual/2026/poster/139327) · [作者来源](https://openreview.net/forum?id=X8UDpzYS5G)

- **问题 / 瓶颈** · 人工标注昂贵且容易不一致，复现需明确来源。
- **核心创新 / 方法** · 先构造文档中间表示，再渲染文件及断言。
- **Baseline** · 传统人工文档问答数据是背景。
- **Benchmark** · 100 文档、50 域、4374 页、16589 个问答。
- **关键结果 / 消融** · 作者报告无额外标注成本且同种子复现。
- **适用条件 / 局限** · 合成文档不保证覆盖真实业务分布。

**可复用机制** · 需要可核验问答时，可在渲染材料前绑定生成答案和来源信息。

<a id="paper-153926"></a>

## The Missing Positional Story in LLMs: A Case Study of Shift-Invariant Attention

[官方论文页](https://neurips.cc/virtual/2026/poster/153926) · [作者来源](https://openreview.net/forum?id=HbJH1naglA)

- **问题 / 瓶颈** · 位置编码类型不能直接推定模型最终计算。
- **核心创新 / 方法** · 估计各头移位不变结构并做针对性干预。
- **Baseline** · 不同显式编码、不同头和干预对照。
- **Benchmark** · 偏移组织的检索及模型注意力行为。
- **关键结果 / 消融** · 移位不变性幅值与干预损失相随，绝对位置模型也学到此结构。
- **适用条件 / 局限** · 摘要未给所有任务效应量。

**可复用机制** · 偏移变化适应性应从实际注意力机制验证，而非仅根据编码类型推断。

<a id="paper-152312"></a>

## The Neural Race Model

[官方论文页](https://neurips.cc/virtual/2026/poster/152312) · [作者来源](https://openreview.net/forum?id=U280pm3mcR)

- **问题 / 瓶颈** · 只预测标签无法解释决定阈值和证据积累速度。
- **核心创新 / 方法** · 时间连续的竞争累加器将刺激作为漂移、噪声及阈值条件。
- **Baseline** · 传统固定参数决策模型。
- **Benchmark** · 刺激条件下的反应时间与选择。
- **关键结果 / 消融** · 摘要展示端到端优化和同一模型拟合两类输出。
- **适用条件 / 局限** · 依赖反应时观测和累加器假设。

**可复用机制** · 给考虑时间的代理行为建模时，测犹豫时长是否提供超出最终动作的信息。

<a id="paper-151427"></a>

## The Optimal Control Foundation of Early Exits – Turnpikes and ResNets

[官方论文页](https://neurips.cc/virtual/2026/poster/151427) · [作者来源](https://openreview.net/forum?id=anDvnfg9Dj)

- **问题 / 瓶颈** · 训练更深模型通常不能直接复用其早层的行为结论。
- **核心创新 / 方法** · 以最优控制证明联合训练的残差网络出现转向稳定阶段。
- **Baseline** · 不同深度的共训残差网络。
- **Benchmark** · 早退性能和中间表示相似性。
- **关键结果 / 消融** · 达指定损失所需层数可有独立于总深度的上界。
- **适用条件 / 局限** · 依赖联合训练与理论假设。

**可复用机制** · 部署早退前可跨模型深度验证中间表示和退出点的稳定性。

<a id="paper-154968"></a>

## The Optimization Prior: Instilling depth for shallow networks, detail for coarse networks

[官方论文页](https://neurips.cc/virtual/2026/poster/154968) · [作者来源](https://openreview.net/forum?id=9ZcIwyPLGI)

- **问题 / 瓶颈** · 随机初始化几何可能造成不同优化路径。
- **核心创新 / 方法** · 用随机初始化的引导模型给目标做初始几何对齐。
- **Baseline** · 原模型随机初值和多个架构引导。
- **Benchmark** · 浅模型及粗尺度模型的下游训练。
- **关键结果 / 消融** · 摘要报告不同架构能改变后续优化特性。
- **适用条件 / 局限** · 不等同于训练后蒸馏，额外初始化成本未报告。

**可复用机制** · 若架构难换，可尝试仅转移初始化几何，再按原预算训练。

<a id="paper-148461"></a>

## Theoretical guidelines for annealed Langevin dynamics in compositional simulation-based inference

[官方论文页](https://neurips.cc/virtual/2026/poster/148461) · [作者来源](https://openreview.net/forum?id=xdr2AIOz88)

- **问题 / 瓶颈** · 复合分数通常不对应真正后验的前向扩散路径。
- **核心创新 / 方法** · 沿桥接密度退火 Langevin 采样以控制偏差。
- **Baseline** · 以复合分数做逆 SDE。
- **Benchmark** · 组合式基于模拟的推断及理论基准。
- **关键结果 / 消融** · 逆过程可能有不可消除偏差，适当退火可改变偏差。
- **适用条件 / 局限** · 收敛取决于桥接密度和过程正则性。

**可复用机制** · 组合条件分数时先判断采样动态是否与真实前向路径一致。

<a id="paper-153597"></a>

## Theoretical Limits of Language Model Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/153597) · [作者来源](https://openreview.net/forum?id=KCwm0j2Hii)

- **问题 / 瓶颈** · 单看观测收益难判断算法瓶颈或预算瓶颈。
- **核心创新 / 方法** · 推导 KL 正则对齐的最大奖励上界，包含 Jeffreys 散度。
- **Baseline** · 已有奖励预算估计。
- **Benchmark** · 给定参考分布和奖励的对齐理论。
- **关键结果 / 消融** · 给出闭式的最优收益刻画。
- **适用条件 / 局限** · 依赖奖励及固定参考策略，摘要未给广泛实证。

**可复用机制** · 报告对齐收益应同时提供预算和同预算下可达上界。

<a id="paper-154381"></a>

## Theory of Optimal Learning Rate Schedules and Scaling Laws for a Random Feature Model

[官方论文页](https://neurips.cc/virtual/2026/poster/154381) · [作者来源](https://openreview.net/forum?id=DzVZ8bvupU)

- **问题 / 瓶颈** · 短跑最优学习率可能不适用于更长预算。
- **核心创新 / 方法** · 对随机特征模型优化有限时域速率，并在 GPT-2 风格预训练验证。
- **Baseline** · 固定退火日程与不同总训练量。
- **Benchmark** · 随机特征理论和语言模型实验。
- **关键结果 / 消融** · 理论分为两阶段类型，模型在退火时仍随训练量移动最优学习率。
- **适用条件 / 局限** · 随机特征假设不能无条件外推至大模型。

**可复用机制** · 延长训练计划时先扫峰值学习率，再判断日程和长度的联合最优。

<a id="paper-155001"></a>

## Theory on Attention Dynamics for Out-of-Distribution In-Context Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/155001) · [作者来源](https://openreview.net/forum?id=9JWBP6GQk7)

- **问题 / 瓶颈** · 注意力对正确和错误特征的信任会受整体训练特征影响。
- **核心创新 / 方法** · 分析 α 与 β 注意力动态及训练测试特征的成对关系。
- **Baseline** · 多种特征偏移形态。
- **Benchmark** · 合成和真实数据的域外上下文学习。
- **关键结果 / 消融** · 摘要报告注意力错误的变化可随不同交互升降。
- **适用条件 / 局限** · 理论依赖特征分解，摘要未给通用阈值。

**可复用机制** · 用受控偏移分别测试正确证据被削弱和错误证据被增强。

<a id="paper-149824"></a>

## The Override Gap: A Magnitude Account of Knowledge Conflict Failure in Hypernetwork-Based Instant LLM Adaptation

[官方论文页](https://neurips.cc/virtual/2026/poster/149824) · [作者来源](https://openreview.net/forum?id=n1UpRVEiaQ)

- **问题 / 瓶颈** · 能记新事实不代表能覆盖强旧先验
- **核心创新 / 方法** · 以冲突程度比较适配器相对预训练 margin
- **Baseline** · Doc-to-LoRA、普通 RAG 和显式冲突提示
- **Benchmark** · KID-Bench 489 题，区分新知识、组合和分级冲突
- **关键结果 / 消融** · Mistral-7B 从 53.6% 至 72.5%，新事实回忆 97.1%
- **适用条件 / 局限** · 知道冲突时显式提示仍可能更强

**可复用机制** · 知识更新评测按先验强度切分，不要只测新知识

<a id="paper-150805"></a>

## The parameters in weight-sparse transformers are interpretable

[官方论文页](https://neurips.cc/virtual/2026/poster/150805) · [作者来源](https://openreview.net/forum?id=fGxBOgrNrv)

- **问题 / 瓶颈** · 以已知任务挑参数会高估普适解释性
- **核心创新 / 方法** · 先挑非零参数，再对照训练稀疏及密集模型归纳作用
- **Baseline** · 同构密集模型、Pythia-70M
- **Benchmark** · 单非零权重可解释比例
- **关键结果 / 消融** · 稀疏为 17–35%，密集为 5–9%
- **适用条件 / 局限** · 样本和模型较小，不能外推大模型

**可复用机制** · 验证结构化稀疏可审性时使用先抽组件、后检验策略

<a id="paper-155162"></a>

## The Path Not Taken: RLVR Learns Off the Principals

[官方论文页](https://neurips.cc/virtual/2026/poster/155162) · [作者来源](https://openreview.net/forum?id=7ob9PpTAMB)

- **问题 / 瓶颈** · BF16 会隐去分布广泛的微小更新
- **核心创新 / 方法** · 跨训练比较权重区域及奇异方向和对齐模式
- **Baseline** · 多种 RLVR 与 SFT
- **Benchmark** · 训练参数变化与主奇异空间
- **关键结果 / 消融** · RLVR 偏好非主方向，相似区域跨配置重复
- **适用条件 / 局限** · 摘要未证明任何单适配器必然优越

**可复用机制** · 将 SFT 的 PEFT 布局用于 RL 前做高精权重与方向消融

<a id="paper-150856"></a>

## The PFAD Not Taken: Measuring Polysemanticity via Feature Affine Decomposition

[官方论文页](https://neurips.cc/virtual/2026/poster/150856) · [作者来源](https://openreview.net/forum?id=er0tG7a4Fo)

- **问题 / 瓶颈** · 顶部响应示例较难揭示不同输入子群中的功能
- **核心创新 / 方法** · 将标量特征拟合为视觉语义空间的硬路由仿射专家
- **Baseline** · 顶部激活案例方法
- **Benchmark** · 已知混合合成与真实视觉特征
- **关键结果 / 消融** · 恢复已知成分并发现定性分析遗漏的多义性
- **适用条件 / 局限** · 依赖代理专家质量和语义测量

**可复用机制** · 为归因单元查可解释性时同时测未出现在顶部样例中的分布切片

<a id="paper-153995"></a>

## The Price of Choosing Examples: Context Overfitting in Adaptive In-Context Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/153995) · [作者来源](https://openreview.net/forum?id=Gzmzr2tIux)

- **问题 / 瓶颈** · 查询后多轮筛选会让训练库证据过拟合
- **核心创新 / 方法** · 以提示转录与数据存储间信息量度量上下文容量
- **Baseline** · 预先固定示例和自适应检索
- **Benchmark** · 贝叶斯线性上下文回归、Gaussian top-k
- **关键结果 / 消融** · 理论区分实例相关性和选择稳定性
- **适用条件 / 局限** · 主要示例为线性 ICL，任意检索器未验证

**可复用机制** · 测试检索时保留独立库，报告反复调挑选规则的次数

<a id="paper-154189"></a>

## The Price of Locality: Why Forward-Forward Underperforms Backpropagation?

[官方论文页](https://neurips.cc/virtual/2026/poster/154189) · [作者来源](https://openreview.net/forum?id=FYRM9ZMFjU)

- **问题 / 瓶颈** · 只用局部目标容易随深度丢梯度多样性
- **核心创新 / 方法** · 区分并发局部更新的优化下限和核收缩造成的表示坍塌
- **Baseline** · 标准反向传播及 Forward-Forward
- **Benchmark** · 深层算法理论和核分析；摘要未给任务细节
- **关键结果 / 消融** · 局部训练的有效容量只线性随深度增加；反传同时依赖宽度与深度
- **适用条件 / 局限** · 量化结论依赖理论核与局部目标条件

**可复用机制** · 低通信训练别只看层 loss，还要测跨层有效梯度秩

<a id="paper-156016"></a>

## The Quantization Benefits of Residual-Free Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/156016) · [作者来源](https://openreview.net/forum?id=18XtiYe9Gk)

- **问题 / 瓶颈** · 激活重尾降低低比特精度
- **核心创新 / 方法** · 对照含残差与去残差结构，并配深度相关温度调节
- **Baseline** · 常规残差 Transformer
- **Benchmark** · 语言任务、全精度与低比特
- **关键结果 / 消融** · 少量全精度损失伴随更强低位鲁棒性
- **适用条件 / 局限** · 训练配方及部署位宽会影响收益

**可复用机制** · 以部署位宽评估架构，而非全精度做唯一选型
