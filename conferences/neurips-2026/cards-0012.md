# NeurIPS 2026 论文卡 12

[会议索引](README.md)

<a id="paper-139071"></a>

## TherapyGym: Evaluating and Aligning Clinical Fidelity and Safety in Therapy Chatbots

[官方论文页](https://neurips.cc/virtual/2026/poster/139071) · [作者来源](https://openreview.net/forum?id=mzFFA3ZcQd)

- **问题 / 瓶颈** · 流畅性和喜好不能代理专业要求。
- **核心创新 / 方法** · 专家校准多轮疗程评价。
- **Baseline** · 通用对话评分。
- **Benchmark** · TherapyGym，CTRS。
- **关键结果 / 消融** · 专家均分从 0.10 至 0.60，LLM 评委 0.16 至 0.59。
- **适用条件 / 局限** · 分数不是患者疗效，使用范围依专家审核。

**可复用机制** · 将垂直代理专业流程与安全设独立审计门。

<a id="paper-152613"></a>

## The Rate-Distortion-Polysemanticity Tradeoff in SAEs

[官方论文页](https://neurips.cc/virtual/2026/poster/152613) · [作者来源](https://openreview.net/forum?id=Rp9yurnWMc)

- **问题 / 瓶颈** · 追求单语义可能增加编码代价。
- **核心创新 / 方法** · 建玩具率失真模型并变更特征共现。
- **Baseline** · 不同约束的 SAE。
- **Benchmark** · 理论和受控数据。
- **关键结果 / 消融** · 强制单语义提高码率和误差，最优多义受共现影响。
- **适用条件 / 局限** · 受玩具生成假设约束。

**可复用机制** · 干预数据共现后再判断多义是否为架构问题。

<a id="paper-150680"></a>

## The Reasoning Boundary Paradox: How Reinforcement Learning Constrains Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150680) · [作者来源](https://openreview.net/forum?id=gIIcM35wXp)

- **问题 / 瓶颈** · 在策略采样会让解法变窄。
- **核心创新 / 方法** · 优先训练低似然且尚未过关的问题。
- **Baseline** · 标准 RLVR。
- **Benchmark** · 多数学基准 Pass@k。
- **关键结果 / 消融** · 曲线变窄可缓解，增益待核。
- **适用条件 / 局限** · 低似然可能是难题、错标或格式问题。

**可复用机制** · 评估 RL 数据课程应同看 Pass@1 和高 k。

<a id="paper-153284"></a>

## The Reciprocity Gradient

[官方论文页](https://neurips.cc/virtual/2026/poster/153284) · [作者来源](https://openreview.net/forum?id=MPZCNReQDd)

- **问题 / 瓶颈** · 只用固定对手反馈会忽略行动反过来影响对手。
- **核心创新 / 方法** · 从公开观测学对手策略，通过估计反传决策与评价信号。
- **Baseline** · 固定对手或用内在奖励。
- **Benchmark** · 参与者互动学习。
- **关键结果 / 消融** · 摘要提出联合优化，幅度待核。
- **适用条件 / 局限** · 依赖响应模型校准。

**可复用机制** · 学习协作决策时拟合反馈行为，再测误拟合的后果。

<a id="paper-153628"></a>

## The Reflexivity Threshold: A Phase Transition for Multi-Agent Performative Prediction

[官方论文页](https://neurips.cc/virtual/2026/poster/153628) · [作者来源](https://openreview.net/forum?id=JykL1GuF6G)

- **问题 / 瓶颈** · 单代理稳定不能推群体稳定。
- **核心创新 / 方法** · 由梯度敏感与曲率构反身矩阵并推阈值。
- **Baseline** · 单代理标量阈值。
- **Benchmark** · 多代理 performative prediction 的上界和下界。
- **关键结果 / 消融** · 矩阵统一刻画相变。
- **适用条件 / 局限** · 依赖局部敏感和曲率刻画。

**可复用机制** · 多个模型联动前审计交叉响应而非独立看误差。

<a id="paper-151614"></a>

## The Reward Was in Your Data All Along: Correcting Flow Matching with Discriminator-Guided RL.

[官方论文页](https://neurips.cc/virtual/2026/poster/151614) · [作者来源](https://openreview.net/forum?id=ZEUZR2yKyB)

- **问题 / 瓶颈** · 训练目标与真实采样分布有偏差。
- **核心创新 / 方法** · 以判别器作直接奖励强化学习。
- **Baseline** · 未经 DRL 的 SiT、JiT、REPA、RAE。
- **Benchmark** · 图像 FID、DINOv3 FD、人类偏好代理。
- **关键结果 / 消融** · SiT 无引导 FID 9.38 至 2.62，FD 88.2 至 19.3。
- **适用条件 / 局限** · 需检查判别过拟合和其他域覆盖。

**可复用机制** · 在生成分布上检验奖励是否纠正训练预测目标留下的误差。

<a id="paper-154852"></a>

## The Ringelmann Effect in Multi-Agent LLM Systems: A Scaling Law for Effective Team Size

[官方论文页](https://neurips.cc/virtual/2026/poster/154852) · [作者来源](https://openreview.net/forum?id=AQT3dCAg0a)

- **问题 / 瓶颈** · 观察提升可能来自重复评估。
- **核心创新 / 方法** · 比较有效团队规模及噪声安慰剂。
- **Baseline** · 真实讨论和单模型重看。
- **Benchmark** · 开放数学及扩大四倍设置。
- **关键结果 / 消融** · 同质团队中噪声对照追上重看效果。
- **适用条件 / 局限** · 异构团队和可工具验证任务不能直接套用。

**可复用机制** · 测协作增量需控制额外推理轮和 token。

<a id="paper-153754"></a>

## The risk of KV cache compression

[官方论文页](https://neurips.cc/virtual/2026/poster/153754) · [作者来源](https://openreview.net/forum?id=IxNf37GZip)

- **问题 / 瓶颈** · 最坏不可能性不足以指导可行输入。
- **核心创新 / 方法** · 按结构描述因果压缩极小极大风险。
- **Baseline** · 最坏例及现有经验压缩。
- **Benchmark** · prefill、自回归和因果掩码。
- **关键结果 / 消融** · 得到满足风险最优的设计原则。
- **适用条件 / 局限** · 取决于缓存模型和表示范围。

**可复用机制** · 压缩搜索从可压信号而非统一缓存比例出发。

<a id="paper-151317"></a>

## The road reaches every place, the short cut only one: Self-Adversarial Shortcut Mitigation for AI-Generated Image Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/151317) · [作者来源](https://openreview.net/forum?id=bO6CYKnaZo)

- **问题 / 瓶颈** · 单个强伪影易过拟合生成器。
- **核心创新 / 方法** · 对语义和伪影特征作自对抗学习，检查特征多样性。
- **Baseline** · 单线索检测。
- **Benchmark** · 跨图像生成器识别。
- **关键结果 / 消融** · 摘要报告广泛泛化改善，幅度待核。
- **适用条件 / 局限** · 依赖目标生成器多样性。

**可复用机制** · 检测器单测内容偏差及未见生成源灵敏度。

<a id="paper-139474"></a>

## The Ruler and the Judge: Benchmark-Conditional Evaluation of LLM-as-a-Judge

[官方论文页](https://neurips.cc/virtual/2026/poster/139474) · [作者来源](https://openreview.net/forum?id=NmRNfA31p3)

- **问题 / 瓶颈** · 与平均人工分相关不能保证正确判系统差距。
- **核心创新 / 方法** · 量表审核、裁判工具审核及样本外系统级校准。
- **Baseline** · 总体人机相关。
- **Benchmark** · 归一带符号边际、假分离、转移区间、EMD。
- **关键结果 / 消融** · 81 裁判维度中 57 个 EMD 改善。
- **适用条件 / 局限** · 依赖有效人工量表和样本。

**可复用机制** · 裁判上线前需核能否区分真实模型差和虚假差。

<a id="paper-152674"></a>

## The Sample Complexity of Multiple Change Point Identification under Bandit Feedback

[官方论文页](https://neurips.cc/virtual/2026/poster/152674) · [作者来源](https://openreview.net/forum?id=RG9xCWr9Oj)

- **问题 / 瓶颈** · 统一查询浪费平稳区域预算。
- **核心创新 / 方法** · 筛变化候选间隔再精到 η。
- **Baseline** · 仅跳幅的渐近刻画。
- **Benchmark** · 带噪分段常函数查询。
- **关键结果 / 消融** · 有限精度下位置和幅度共同决定成本。
- **适用条件 / 局限** · 依赖观测可查询和分段结构。

**可复用机制** · 检测时序变化时对近邻事件增单独预算。

<a id="paper-151146"></a>

## The Sampling Complexity of Condorcet Winner Identification in Dueling Bandits

[官方论文页](https://neurips.cc/virtual/2026/poster/151146) · [作者来源](https://openreview.net/forum?id=cgQkpwR4Mx)

- **问题 / 瓶颈** · 只查与最佳候选相连边会浪费有用关系。
- **核心创新 / 方法** · 按完整胜率差矩阵自适应分配。
- **Baseline** · 仅胜者差距的算法。
- **Benchmark** · Condorcet 胜者识别。
- **关键结果 / 消融** · 给匹配的依实例界和下界。
- **适用条件 / 局限** · 要求唯一 Condorcet 目标和可靠比对。

**可复用机制** · 模型偏好评估保留可间接排除候选的对比。

<a id="paper-150189"></a>

## The Scaling Laws of Skills in LLM Agent Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/150189) · [作者来源](https://openreview.net/forum?id=k4BUc62CYf)

- **问题 / 瓶颈** · 更多技能可能使前序选择乘法下降。
- **核心创新 / 方法** · 分析路由随库规模衰减和正确执行恢复后续决策。
- **Baseline** · 不同技能数量、粒度和可见策略。
- **Benchmark** · LLM 代理技能执行。
- **关键结果 / 消融** · 正确执行后困难下游改善约四倍。
- **适用条件 / 局限** · 依赖技能库和任务流程。

**可复用机制** · 技能上线前确定新增选项是否降低关键路由成功率。

<a id="paper-151564"></a>

## The Scaling Paradox of Tool-Calling LLM Agents Under Realistic MCP Faults

[官方论文页](https://neurips.cc/virtual/2026/poster/151564) · [作者来源](https://openreview.net/forum?id=ZfMdoPBhn0)

- **问题 / 瓶颈** · 更多推理步会放大依赖故障暴露。
- **核心创新 / 方法** · 在受控本地测试中按持久性和随机种子模拟接口故障。
- **Baseline** · 无故障环境和不同模型尺寸。
- **Benchmark** · 1350 条件，20B/120B 与三栈。
- **关键结果 / 消融** · 任务分降低 60%，大模型有错时完成率可更低。
- **适用条件 / 局限** · 真实环境故障分布需另测。

**可复用机制** · 以相同完整可靠性预算比较工具调用深度。

<a id="paper-149695"></a>

## The Score Kalman Filter

[官方论文页](https://neurips.cc/virtual/2026/poster/149695) · [作者来源](https://openreview.net/forum?id=o7YK39RTTY)

- **问题 / 瓶颈** · MaxEnt 配分函数高维积分贵。
- **核心创新 / 方法** · 用 Stein 恒等式闭合矩并更新后验。
- **Baseline** · 原 MaxEnt 矩滤波、经典 Kalman。
- **Benchmark** · 非高斯预测和更新。
- **关键结果 / 消融** · 线性代数实现，信息 Kalman 为特例。
- **适用条件 / 局限** · 依赖矩族与 score 近似。

**可复用机制** · 动态状态估计优先检查是否可避免显式归一化积分。

<a id="paper-149565"></a>

## The Shape of a Program: Path Signatures for Trace-to-Program Induction

[官方论文页](https://neurips.cc/virtual/2026/poster/149565) · [作者来源](https://openreview.net/forum?id=pAtl3nP8op)

- **问题 / 瓶颈** · 常规序列编码在少量轨迹下可能泛化不足。
- **核心创新 / 方法** · 以路径签名表示轨迹，再生成领域专用程序。
- **Baseline** · LSTM、Transformer、傅里叶编码。
- **Benchmark** · 两个经典 DSL 的轨迹到程序。
- **关键结果 / 消融** · 摘要报告优于对照且更省数据。
- **适用条件 / 局限** · 证据限两个 DSL，未给长轨迹计算。

**可复用机制** · 轨迹结构比绝对时间更重要时，可测路径签名能否替代通用序列编码。

<a id="paper-148705"></a>

## The Shape of Events: Edge-Based Inductive Biases via Cross-Domain Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/148705) · [作者来源](https://openreview.net/forum?id=vfKGFX4uRY)

- **问题 / 瓶颈** · 只看事件传感任务难以独立测量教师的归纳偏置。
- **核心创新 / 方法** · 将事件域知识转移到 RGB，再使用通用视觉诊断。
- **Baseline** · 普通 RGB 模型。
- **Benchmark** · 形状敏感任务与跨域蒸馏。
- **关键结果 / 消融** · 摘要指出事件数据带来边缘形状偏置。
- **适用条件 / 局限** · 依赖跨域蒸馏适配，未给独立数值。

**可复用机制** · 可通过跨域教师把传感器的局部归纳偏置迁移到易测量的模态。

<a id="paper-151909"></a>

## The Sharp Directions Are Against You: Curvature Analysis of Activation Steering

[官方论文页](https://neurips.cc/virtual/2026/poster/151909) · [作者来源](https://openreview.net/forum?id=WyedqmCk4O)

- **问题 / 瓶颈** · 高响应不一定意味着稳定有效的概念控制。
- **核心创新 / 方法** · 分析方向 Hessian 的高曲率谱。
- **Baseline** · 常见激活控制方向的对照。
- **Benchmark** · 多种行为控制条件。
- **关键结果 / 消融** · 摘要指出尖锐方向会损伤一致控制。
- **适用条件 / 局限** · 依赖行为损失和局部扰动区间。

**可复用机制** · 选激活方向时将鲁棒行为控制和高灵敏度分开评估。

<a id="paper-155585"></a>

## The Sign Code: The Hidden Binary Nature of Deep Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/155585) · [作者来源](https://openreview.net/forum?id=4WN4vV8RCR)

- **问题 / 瓶颈** · 连续表示可能掩盖由激活符号主导的特征。
- **核心创新 / 方法** · 用符号做近邻分类，再随机替换幅值。
- **Baseline** · 全精度分类与保留符号的幅值对照。
- **Benchmark** · 多种架构、激活与数据。
- **关键结果 / 消融** · 摘要报告符号近邻接近原模型，扰动幅值几乎不影响结果。
- **适用条件 / 局限** · 结论依赖所测架构和符号提取条件。

**可复用机制** · 做量化和解释时先按符号与幅值分别测判别信息。

<a id="paper-155935"></a>

## The Silent Hyperparameter: Quantifying the Impact of Inference Backends on LLM Reproducibility

[官方论文页](https://neurips.cc/virtual/2026/poster/155935) · [作者来源](https://openreview.net/forum?id=1gtJHlEFQQ)

- **问题 / 瓶颈** · 相同权重仍可因数值内核产生不同生成。
- **核心创新 / 方法** · 调查后端与论文记录并对照推理结果。
- **Baseline** · 多个推理引擎。
- **Benchmark** · 200 个引擎与 3.5 万论文的调查，以及推理比较。
- **关键结果 / 消融** · 报告后端对实验重复性具有后果。
- **适用条件 / 局限** · 摘要未给具体任务效应量。

**可复用机制** · 跨系统比较性能前，核对输出分布差异是否来自模型或执行栈。

<a id="paper-152487"></a>

## The Sparsity Whisperer

[官方论文页](https://neurips.cc/virtual/2026/poster/152487) · [作者来源](https://openreview.net/forum?id=SkASoryYLq)

- **问题 / 瓶颈** · 常用幅值分数可能不保护输入之间的区分。
- **核心创新 / 方法** · Wisp 用输入差异范数，Wisp+ 使用每个神经元最能区分的样本对。
- **Baseline** · 既有训练后剪枝。
- **Benchmark** · 不同模型族、任务及结构化稀疏。
- **关键结果 / 消融** · 摘要报告保留判别变化对多类剪枝有效。
- **适用条件 / 局限** · 依赖代表性的校准输入。

**可复用机制** · 压缩前明确哪些输入差异需要保留，用它替代单样本能量作为剪枝依据。

<a id="paper-149714"></a>

## The State-Prediction Separation Hypothesis

[官方论文页](https://neurips.cc/virtual/2026/poster/149714) · [作者来源](https://openreview.net/forum?id=nzCLgrnrNe)

- **问题 / 瓶颈** · 同表示承担两项职责可能增加梯度干扰。
- **核心创新 / 方法** · 以状态与预测分离替代常规共享结构。
- **Baseline** · 标准 Transformer。
- **Benchmark** · 验证损失、计算和数据效率及下游任务。
- **关键结果 / 消融** · 下游平均提高 2 至 3 个百分点。
- **适用条件 / 局限** · 摘要未给各任务架构限制。

**可复用机制** · 如果状态更新与预测相互牵制，可先分开两种表示职责再检验性能。

<a id="paper-148482"></a>

## The Structural Bias of $\ell_2$-Regularized Cross-Entropy Heads in Class-Incremental Learning: Characterization, Limits, and a Gauge-Anchoring Fix

[官方论文页](https://neurips.cc/virtual/2026/poster/148482) · [作者来源](https://openreview.net/forum?id=xULFTd3ead)

- **问题 / 瓶颈** · 任务独立 softmax 使不同任务头分数不可直接比较。
- **核心创新 / 方法** · 识别任务块共同偏移并在推理时去中心。
- **Baseline** · 联合训练和未校正顺序训练。
- **Benchmark** · CIFAR-100、ImageNet 各变体、DomainNet，五个冻结主干。
- **关键结果 / 消融** · 弥合联合与顺序差距的 82% 至 94%。
- **适用条件 / 局限** · 依赖所测正则分类头及分离条件。

**可复用机制** · 独立训练的输出头合并时，应先检测任务级常数偏移，不急于重训。

<a id="paper-152150"></a>

## The SuperActivator Mechanism: Transformers Concentrate Reliable Concept Signals in the Tail

[官方论文页](https://neurips.cc/virtual/2026/poster/152150) · [作者来源](https://openreview.net/forum?id=VAaP43gSBg)

- **问题 / 瓶颈** · 全局均值可能混合低强度的不同语义。
- **核心创新 / 方法** · 分析极端激活间差距的注意力放大。
- **Baseline** · 全局概念向量。
- **Benchmark** · 大模型概念证据定位。
- **关键结果 / 消融** · 检测通常在只用概念内 5% 至 10% 激活时达峰。
- **适用条件 / 局限** · 依赖概念和激活方向。

**可复用机制** · 估计语义方向时把局部高置信证据和平均行为分开验证。

<a id="paper-154971"></a>

## The Surprising Effectiveness of Deleting Weights in LLM Reasoning and Adaptation

[官方论文页](https://neurips.cc/virtual/2026/poster/154971) · [作者来源](https://openreview.net/forum?id=9Z9V0zY5As)

- **问题 / 瓶颈** · 普通适配更新更多状态且可能损伤原能力。
- **核心创新 / 方法** · 对 Transformer 门控投影学习二值掩码。
- **Baseline** · 全参数和其他轻量适配。
- **Benchmark** · 0.5B 至 8B 的 GRPO 与遗忘评估。
- **关键结果 / 消融** · 规模增加时与全量微调差距缩小，掩码存储小。
- **适用条件 / 局限** · 未给适用层和稀疏率通则。

**可复用机制** · 参数规模变化时重新比较离散掩码和连续适配的容量需求。

<a id="paper-149266"></a>

## The Surprising Effectiveness of Video Diffusion Models for Hand Motion Reconstruction

[官方论文页](https://neurips.cc/virtual/2026/poster/149266) · [作者来源](https://openreview.net/forum?id=rbIH0DXMsW)

- **问题 / 瓶颈** · 直接监督追踪在自然视频难获取三维真值。
- **核心创新 / 方法** · 通过叠加手部渲染目标适配预训练扩散模型。
- **Baseline** · 既有手部重建方法。
- **Benchmark** · 单视频的四维双手姿态。
- **关键结果 / 消融** · 摘要报告优于先前方法。
- **适用条件 / 局限** · 依赖视频先验和渲染监督，摘要未给标注成本。

**可复用机制** · 生成模型可作为运动重建先验，再用可渲染目标约束任务输出。

<a id="paper-139825"></a>

## The Text Uncanny Valley: Non-Monotonic Performance Degradation in LLM Information Retrieval

[官方论文页](https://neurips.cc/virtual/2026/poster/139825) · [作者来源](https://openreview.net/forum?id=2dLQDrT09Z)

- **问题 / 瓶颈** · 模型可能在中等破碎度失去词级线索又未切换到字符级。
- **核心创新 / 方法** · 比较不同碎裂水平及其机制。
- **Baseline** · 清洁与轻度或重度破碎输入。
- **Benchmark** · 文本检索准确度。
- **关键结果 / 消融** · 摘要报告中间区间出现非单调谷底。
- **适用条件 / 局限** · 作者解释为模式转换假说，摘要未给语言外推。

**可复用机制** · 部署到 OCR 或杂乱文本前，应覆盖中间噪声水平来发现最坏条件。

<a id="paper-155088"></a>

## The two clocks and the innovation window: When and how generative models learn rules

[官方论文页](https://neurips.cc/virtual/2026/poster/155088) · [作者来源](https://openreview.net/forum?id=8WJCdo8rks)

- **问题 / 瓶颈** · 单看训练拟合无法发现可创新的中间区间。
- **核心创新 / 方法** · 对比规则判定与记忆行为的时间尺度。
- **Baseline** · 不同规则复杂度与样本量。
- **Benchmark** · 奇偶、其他二元规则与组合谜题。
- **关键结果 / 消融** · 报告规则时间受复杂度影响，后期样本记忆盆地可占主导。
- **适用条件 / 局限** · 理论与实验限所述可控任务。

**可复用机制** · 想得到新样本时，应按有效规则泛化信号选检查点，而非只优化记忆精度。

<a id="paper-149581"></a>

## The Unembedding Bottleneck: A Mechanistic Analysis of Single Digit Counting in LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/149581) · [作者来源](https://openreview.net/forum?id=p2sbwRiO7X)

- **问题 / 瓶颈** · 输出错误不能区分缺知识与读出投影失配
- **核心创新 / 方法** · 用探针定位后只改输出矩阵，检查恢复及通用能力
- **Baseline** · 原模型和不改输出的计数效果
- **Benchmark** · 六模型单数字计数及通用能力保留
- **关键结果 / 消融** · 只更新约 0.001% 参数即可大幅恢复计数正确性
- **适用条件 / 局限** · 证据局限单数字计数，结论不自动推广

**可复用机制** · 适配前对比隐藏读出和原输出，判断是否需要微调骨干

<a id="paper-151028"></a>

## The Value of Being Wrong: Self-Mined Visual In-Context Learning from Errors

[官方论文页](https://neurips.cc/virtual/2026/poster/151028) · [作者来源](https://openreview.net/forum?id=dVu1u4QgAp)

- **问题 / 瓶颈** · 检索外观相似例可能重复已有偏误
- **核心创新 / 方法** · 挖掘模型自身错误并按当前预测筛可能复现的失败
- **Baseline** · 既有视觉 ICL 基线
- **Benchmark** · 四基准与四 VLM；分类、视觉问答、时延
- **关键结果 / 消融** · 平均高 2.72 分且时延约为对照的五分之一
- **适用条件 / 局限** · 需有可校验的错误样例，误诊可能引入偏差

**可复用机制** · 给检索器同时加相似例和针对当前假设的反例

<a id="paper-148184"></a>

## The Value of Covariance Matching in Gaussian DDPMs and the Lanczos Sampler

[官方论文页](https://neurips.cc/virtual/2026/poster/148184) · [作者来源](https://openreview.net/forum?id=zfgaE5LyWU)

- **问题 / 瓶颈** · 对角噪声无法表达像素间耦合
- **核心创新 / 方法** · 用少量 Lanczos 和雅可比向量积逼近后验采样
- **Baseline** · 对角协方差与 OCM-DDPM
- **Benchmark** · 标准图像生成，摘要未列名单
- **关键结果 / 消融** · 三步 Lanczos 已改善样本质量
- **适用条件 / 局限** · 依赖可计算的雅可比积及谱条件

**可复用机制** · 同推理预算检验协方差近似阶数和实际保真

<a id="paper-153414"></a>

## The VLM as Sensor: Bayesian Active Search for Long Video Understanding

[官方论文页](https://neurips.cc/virtual/2026/poster/153414) · [作者来源](https://openreview.net/forum?id=LVgNulVpKE)

- **问题 / 瓶颈** · 只按终局正确可能促使模型从预览猜
- **核心创新 / 方法** · 将 VLM 视作传感器，每轮按熵下降给分并门控终局奖励
- **Baseline** · 近年 RL 视频搜索
- **Benchmark** · 长视频任务准确率和使用帧数
- **关键结果 / 消融** · 摘要报最高加 8.8 分，同时少看 5–13 倍帧
- **适用条件 / 局限** · 熵下降依赖预测概率可校准

**可复用机制** · 在低帧预算下分别验收主动取证与正确作答

<a id="paper-155515"></a>

## The World is Not Mono: Enabling Spatial Understanding in Large Audio-Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155515) · [作者来源](https://openreview.net/forum?id=51hFveUNno)

- **问题 / 瓶颈** · 单声道或输出接口差异会混淆空间推理对照
- **核心创新 / 方法** · 以 FOA 和元数据监督训练，按听觉场景分析分层
- **Baseline** · 单声道系统作为诊断而非匹配对照
- **Benchmark** · 空间音频语言任务；STARSS23 真实记录诊断
- **关键结果 / 消融** · 摘要支持受控、可审计的空间问答
- **适用条件 / 局限** · 真实录音证据有限，输入输出接口不匹配

**可复用机制** · 多模态设备先固定传感器再比较模型空间能力

<a id="paper-150085"></a>

## Thinking with Images as Continuous Policy: Numerical Visual Chain-of-Thought

[官方论文页](https://neurips.cc/virtual/2026/poster/150085) · [作者来源](https://openreview.net/forum?id=kqCpiR360C)

- **问题 / 瓶颈** · 离散视觉推理接口会限制精细输出
- **核心创新 / 方法** · 用数值视觉思考表示空间动作，并用 GRPO 类型目标优化
- **Baseline** · 八种视觉推理基线
- **Benchmark** · 三个基准；定位精度、答案准确及收敛
- **关键结果 / 消融** · 三项改善，摘要未列数值
- **适用条件 / 局限** · 依赖连续坐标评测与参照物清晰

**可复用机制** · 规划和视觉定位分别比较坐标精度与终局答对率

<a id="paper-148599"></a>

## Thinking with Imagination: Agentic Visual Spatial Reasoning with World Simulators

[官方论文页](https://neurips.cc/virtual/2026/poster/148599) · [作者来源](https://openreview.net/forum?id=wYAS2pbniI)

- **问题 / 瓶颈** · 任意想象可能引入无用或不真实证据
- **核心创新 / 方法** · 用具行动的策略决定何时及何处生成新观察，和模拟器分别消融
- **Baseline** · Gemini-3-Flash、Qwen3-VL 原模型与加模拟器变体
- **Benchmark** · MMSI-Bench、MindCube
- **关键结果 / 消融** · Astra-VL 在两项分别 29.8 到 38.8、36.8 到 42.7
- **适用条件 / 局限** · 生成图像只是辅助，需验证真实几何

**可复用机制** · 为新视角想象独立验收模拟质量和查询策略

<a id="paper-148479"></a>

## Thinking with Imitation: Adaptive Reinforcement-Imitation Learning for Tool-Augmented Scientific Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/148479) · [作者来源](https://openreview.net/forum?id=xVDIXQnJEw)

- **问题 / 瓶颈** · 稀疏奖励让相对组更新归零。
- **核心创新 / 方法** · 按是否有成功动态交替在线强化和模仿。
- **Baseline** · 固定比例离线混合和直接加专家例。
- **Benchmark** · SciExplore-Bench 科学工具推理。
- **关键结果 / 消融** · 直接塞完整示范不升反降；切换效果幅度待核。
- **适用条件 / 局限** · 依赖专家和可验证结局。

**可复用机制** · 让模仿预算只覆盖策略尚不能探索到的能力。

<a id="paper-154630"></a>

## Thinking with Visual Primitives

[官方论文页](https://neurips.cc/virtual/2026/poster/154630) · [作者来源](https://openreview.net/forum?id=CA9dsXjWGT)

- **问题 / 瓶颈** · 文本空间描述可能繁琐且难复验。
- **核心创新 / 方法** · 以点和方框作为最小可定位推理步骤。
- **Baseline** · 普通文字链或复杂视觉操作。
- **Benchmark** · 多模态空间推理。
- **关键结果 / 消融** · 摘要提出高效路径，幅度未核。
- **适用条件 / 局限** · 精细几何和关系不一定可点框表达。

**可复用机制** · 记录能在原图复查的中间证据。

<a id="paper-150698"></a>

## ThinkJEPA: Empowering Latent World Models with Large Vision-Language Reasoning Model

[官方论文页](https://neurips.cc/virtual/2026/poster/150698) · [作者来源](https://openreview.net/forum?id=gBPgg0KWK7)

- **问题 / 瓶颈** · 单个采样步长难兼顾局部动态与长程推理。
- **核心创新 / 方法** · 稠密 JEPA 配低频 VLM，金字塔提取多层语义引导。
- **Baseline** · V-JEPA2 类型。
- **Benchmark** · 视频动态及语义引导。
- **关键结果 / 消融** · 摘要给机制，实证细节待核。
- **适用条件 / 局限** · 依赖教师信号和跨节奏对齐。

**可复用机制** · 不要为每帧重复高成本语义推理。

<a id="paper-149971"></a>

## Think, Plan, Paint: Layout-Aware Reasoning for Controllable Image Generation in Unified Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149971) · [作者来源](https://openreview.net/forum?id=lpI5QYN2jv)

- **问题 / 瓶颈** · 端到端像素没有明确空间约束。
- **核心创新 / 方法** · 统一模型产布局，以 RL 优化布局还原。
- **Baseline** · 现有布局感知 MLLM。
- **Benchmark** · 7B 与 80B，含 ATLAS-Reasoning。
- **关键结果 / 消融** · 摘要报告较现有布局模型平均提升 65.31%。
- **适用条件 / 局限** · 指标定义和规模效应需全文核。

**可复用机制** · 将规划正确率与生成忠实度分开验收。

<a id="paper-150302"></a>

## ThinkSafe: Self-Generated Safety Alignment for Reasoning Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150302) · [作者来源](https://openreview.net/forum?id=j99oLs1zyq)

- **问题 / 瓶颈** · 外部教师造成分布移位并损推理。
- **核心创新 / 方法** · 将安全调整视作 KL 投影，自生成后过滤学习。
- **Baseline** · 外部教师安全蒸馏。
- **Benchmark** · DeepSeek-R1-Distill、Qwen3。
- **关键结果 / 消融** · 摘要称安全提高且推理保持。
- **适用条件 / 局限** · 取决于过滤器与原分布安全样本覆盖。

**可复用机制** · 需要回补安全时优先保持部署模型原有推理分布。

<a id="paper-149446"></a>

## Think, then Score: Decoupled Reasoning and Scoring for Video Reward Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/149446) · [作者来源](https://openreview.net/forum?id=q1K2PuBRd7)

- **问题 / 瓶颈** · 同时强化两项可能互相干扰。
- **核心创新 / 方法** · 推理与评分组件分开优化。
- **Baseline** · 耦合视频奖励方法。
- **Benchmark** · 领域内、外视频奖励及生成后训练。
- **关键结果 / 消融** · 改善训练效率、稳定性和后训练画质。
- **适用条件 / 局限** · 评委偏差和新生成域仍需测。

**可复用机制** · 监督评分时单独验证解释质量是否真的贡献泛化。

<a id="paper-151335"></a>

## Think-with-Rubrics: From External Evaluator to Internal Reasoning Guidance

[官方论文页](https://neurips.cc/virtual/2026/poster/151335) · [作者来源](https://openreview.net/forum?id=bJbfVJRNJX)

- **问题 / 瓶颈** · 外部评分标准没有进入模型决策。
- **核心创新 / 方法** · 以自生成和参考量表核对量表及答案一致性。
- **Baseline** · 仅外部量表奖励。
- **Benchmark** · 多个指令遵循基准。
- **关键结果 / 消融** · 摘要报告持续优于比较对象，幅度未核。
- **适用条件 / 局限** · 自量表可能漏用户要求，需金标准复查。

**可复用机制** · 让可审计验收标准进入计划但不允许替换真实目标。

<a id="paper-150531"></a>

## Thompson Sampling using Prior-fitted Diffusion Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/150531) · [作者来源](https://openreview.net/forum?id=hRNiI7uR2f)

- **问题 / 瓶颈** · 高斯先验对非高斯函数族有限。
- **核心创新 / 方法** · 使用预训练 prior-fitted 扩散 Transformer 在线采样。
- **Baseline** · GP 等传统优化。
- **Benchmark** · 多全局优化基准及大小训练轮数。
- **关键结果 / 消融** · 部分非高斯设定有优势。
- **适用条件 / 局限** · 仿真先验错配和推理成本需控制。

**可复用机制** · 把目标先验假设视作可更换的后验近似组件。

<a id="paper-139538"></a>

## ThousandWorlds: A benchmark for emulating the climates of potentially habitable exoplanets

[官方论文页](https://neurips.cc/virtual/2026/poster/139538) · [作者来源](https://openreview.net/forum?id=KAFamWBzoo)

- **问题 / 瓶颈** · 单真值排名误把模拟器不一致当模型误差。
- **核心创新 / 方法** · 分设方法排名和相对模拟器差距。
- **Baseline** · 十统计、树、深度及 GP 基线。
- **Benchmark** · ThousandWorlds，低数据多模拟器参数到场。
- **关键结果 / 消融** · 提出可复用评估对照，量化待核。
- **适用条件 / 局限** · 模拟器一致不保证现实准确。

**可复用机制** · 在仿真驱动具身评测同时报告系统误差下限。

<a id="paper-148911"></a>

## TIB: Sample-wise Tempered Information Bottleneck for Multimodal Attribution beyond Alignment Assumption

[官方论文页](https://neurips.cc/virtual/2026/poster/148911) · [作者来源](https://openreview.net/forum?id=uG6aJZk6Im)

- **问题 / 瓶颈** · 各监督等权会让后验过度收缩。
- **核心创新 / 方法** · 由跨模态可靠性调温瓶颈。
- **Baseline** · 固定信息瓶颈。
- **Benchmark** · 受控错位和规模数据。
- **关键结果 / 消融** · 验证强迫解释问题并改善。
- **适用条件 / 局限** · 需要可靠跨模态相关估计。

**可复用机制** · 输出应允许部分输入无法形成一致解释。

<a id="paper-150989"></a>

## TIC-GRPO: Provable and Efficient Optimization for Reinforcement Learning from Human Feedback

[官方论文页](https://neurips.cc/virtual/2026/poster/150989) · [作者来源](https://openreview.net/forum?id=dlQ6zVz4Qq)

- **问题 / 瓶颈** · 单 token 概率不能消除全序列偏差。
- **核心创新 / 方法** · 先只剪比率上尾，再整轨迹统一权重。
- **Baseline** · token 级重要性比和常规 GRPO。
- **Benchmark** · 数学与代码。
- **关键结果 / 消融** · 更稳且最终成绩改善。
- **适用条件 / 局限** · 小概率长轨迹可能数值敏感。

**可复用机制** · 分别诊断重要性权重尾部和纠偏粒度。

<a id="paper-150963"></a>

## TIDE: Asymmetric Neural Circuits for Stabilized Temporal Inhibitory-Excitatory Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/150963) · [作者来源](https://openreview.net/forum?id=dwcrK8NHpm)

- **问题 / 瓶颈** · 自由递归可能在内部迭代中发散。
- **核心创新 / 方法** · 用 Wilson–Cowan 和侧抑制给非对称回路，能量解释目标。
- **Baseline** · CTM。
- **Benchmark** · 训练时间和 Top-1 分类。
- **关键结果 / 消融** · 低于 CTM 一半时间。
- **适用条件 / 局限** · 结构假设及不同迭代预算需验证。

**可复用机制** · 选重复计算机制时单测动态稳定而非看拟合速度。

<a id="paper-152874"></a>

## TIDE: Every Layer Knows the Token Beneath the Context

[官方论文页](https://neurips.cc/virtual/2026/poster/152874) · [作者来源](https://openreview.net/forum?id=PiL1EEzHt9)

- **问题 / 瓶颈** · 深层上下文化可能丢词标识。
- **核心创新 / 方法** · 预计算多个独立语义库，由深度路由，允许空库。
- **Baseline** · 单 token 身份注入和普通 Transformer。
- **Benchmark** · 语言建模与多下游。
- **关键结果 / 消融** · 摘要报告结构改进任务表现。
- **适用条件 / 局限** · 注入的额外内存与长程上下文交互需验。

**可复用机制** · 低层身份与上下文特征用可关闭的残差路径传递。

<a id="paper-150579"></a>

## TIDES: Implicit Time-Awareness in Selective State Space Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150579) · [作者来源](https://openreview.net/forum?id=h8MZDdLCLA)

- **问题 / 瓶颈** · 把内容选择写进步长破坏外推。
- **核心创新 / 方法** · 输入依赖移到对角状态矩阵。
- **Baseline** · 现有选择式与连续 SSM。
- **Benchmark** · Fading Flash，测试不同输入及未见 Δ。
- **关键结果 / 消融** · 避免两类模型的不同失效模式。
- **适用条件 / 局限** · 需物理时间戳可信，复杂现实数据待验。

**可复用机制** · 将采样时距与状态选择的两个自由度显式分开。

<a id="paper-155911"></a>

## TIDE: Trajectory-Aware Watermark Propagation for Text-to-Image Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155911) · [作者来源](https://openreview.net/forum?id=1tohGAfGuc)

- **问题 / 瓶颈** · 单阶段标记后续可能失真。
- **核心创新 / 方法** · 轨迹感知水印传播。
- **Baseline** · 扩散过程内已有水印。
- **Benchmark** · 图像验证、标准失真后的鲁棒及画质。
- **关键结果 / 消融** · 保持可靠验证和更好语义保真。
- **适用条件 / 局限** · 发布新采样器需回归验证。

**可复用机制** · 把来源认证与正常内容完整性当共同上线要求。

<a id="paper-154119"></a>

## TIER: Trajectory-Invariant Execution Rewards for Multi-Step Tool Composition

[官方论文页](https://neurips.cc/virtual/2026/poster/154119) · [作者来源](https://openreview.net/forum?id=G82YnmxBx8)

- **问题 / 瓶颈** · 参考过程限制同样正确的组合。
- **核心创新 / 方法** · 以函数 schema 和运行结果导不依赖单路径奖励。
- **Baseline** · 参考轨迹奖励。
- **Benchmark** · BFCL v3、NestFUL。
- **关键结果 / 消融** · 一致改善，幅度未核。
- **适用条件 / 局限** · 依赖工具检查覆盖，需避免行为副作用。

**可复用机制** · 对多步工具保接口合法与任务结果约束，放开操作顺序。

<a id="paper-152182"></a>

## TIGER: Bridging the Multimodal Reasoning-Access Gap via Modality Counterfactuals

[官方论文页](https://neurips.cc/virtual/2026/poster/152182) · [作者来源](https://openreview.net/forum?id=Ux4SAiuLgN)

- **问题 / 瓶颈** · 懂文字规则未必能经图像入口访问。
- **核心创新 / 方法** · 把文本算题变为图像条件，比较 GRPO/SFT/DPO。
- **Baseline** · 文字推理、常规 RLVR。
- **Benchmark** · MathVerse、EMMA 等。
- **关键结果 / 消融** · 多设置缩小模态差并泛化。
- **适用条件 / 局限** · 合成视觉表现可能有新捷径。

**可复用机制** · 同题不同入口评估是否需要感知连接而非重教推理。

<a id="paper-154023"></a>

## TIGER-FG: Text-Guided Implicit Fine-Grained Grounding for E-commerce Retrieval

[官方论文页](https://neurips.cc/virtual/2026/poster/154023) · [作者来源](https://openreview.net/forum?id=Gpkn9M7pZW)

- **问题 / 瓶颈** · 只蒸馏检索相似不能精确选区域。
- **核心创新 / 方法** · 双损失保区域空间一致及查询商品相似。
- **Baseline** · 最强电商检索基线。
- **Benchmark** · 两个标准和拥挤布局平台，R@1。
- **关键结果 / 消融** · 分别加 6.1 和 34.4 点；查询端 85.7M。
- **适用条件 / 局限** · 依赖领域文本区域信号。

**可复用机制** · 对代理视觉检索将商品身份和场景匹配证据分开蒸馏。

<a id="paper-149412"></a>

## Tight Gap-Dependent Regret Bounds and Problem-Independent Bounds for Cost-aware Cascading Bandits

[官方论文页](https://neurips.cc/virtual/2026/poster/149412) · [作者来源](https://openreview.net/forum?id=qE6UhWAHvg)

- **问题 / 瓶颈** · 需要预设正成本下界使零成本无法用。
- **核心创新 / 方法** · 修改 CC-UCB，单独维护经验零成本。
- **Baseline** · 原 CC-UCB。
- **Benchmark** · 成本感知级联 bandit 与模拟。
- **关键结果 / 消融** · 成本下界设错时修改可减少遗憾。
- **适用条件 / 局限** · 需要级联反馈及可比较成本。

**可复用机制** · 按真实调用代价和成功概率排序，特别校准免费探测。

<a id="paper-150040"></a>

## Tight PAC-Bayes Generalisation Guarantees for Large Language Model Safety Monitoring

[官方论文页](https://neurips.cc/virtual/2026/poster/150040) · [作者来源](https://openreview.net/forum?id=lDwefojK2s)

- **问题 / 瓶颈** · 验证集性能不直接提供小样本泛化证书。
- **核心创新 / 方法** · 压缩 PEFT 更新并以 PAC-Bayes 约束风险和不确定性。
- **Baseline** · 未压缩或常规 PEFT 作为方法背景。
- **Benchmark** · 大语言模型安全监控。
- **关键结果 / 消融** · 摘要报告压缩后可获得有信息量的泛化界。
- **适用条件 / 局限** · 依赖合适先验和数据假设，摘要未列任务数值。

**可复用机制** · 认证监控模型时，小而可编码的更新可能比只调参数量更有价值。

<a id="paper-155298"></a>

## Tikhonov-Stabilized Bezier Representation Forecasting for Training-free Diffusion Acceleration

[官方论文页](https://neurips.cc/virtual/2026/poster/155298) · [作者来源](https://openreview.net/forum?id=6cYL3DrquA)

- **问题 / 瓶颈** · 高阶外推不稳，逐模块误差会传过后续层。
- **核心创新 / 方法** · 以 Tikhonov 稳定的 Bezier 曲线预测表示。
- **Baseline** · 有限差分和其他训练免除的扩散加速。
- **Benchmark** · FLUX.1 与 HunyuanVideo。
- **关键结果 / 消融** · 最高加速分别 4.79 倍与 4.11 倍，摘要称质量更优。
- **适用条件 / 局限** · 适用长度和稳定参数需按模型验证。

**可复用机制** · 缓存可在漫长跳步前估计误差约束，并优先避免模块错误级联。

<a id="paper-155899"></a>

## TILT: Target-induced loss tilting under covariate shift

[官方论文页](https://neurips.cc/virtual/2026/poster/155899) · [作者来源](https://openreview.net/forum?id=20SLcD77Z4)

- **问题 / 瓶颈** · 支持错位时精确重要性权重易不稳定。
- **核心创新 / 方法** · 目标侧正则隐式定义随误差自局部化且有界的权重。
- **Baseline** · 源域训练、精确和相对重要性权重。
- **Benchmark** · 协变量偏移的理论与目标域表现。
- **关键结果 / 消融** · 摘要报告更好且正则参数变化下稳定。
- **适用条件 / 局限** · 依赖给定损失和无标签目标观测，摘要未给外推保证。

**可复用机制** · 对低支持目标区间优先测试有界适配，而非放大少数源样本。

<a id="paper-150957"></a>

## TIMA: Test-Time Internalization for Agentic Memory

[官方论文页](https://neurips.cc/virtual/2026/poster/150957) · [作者来源](https://openreview.net/forum?id=e1BjgiaD5E)

- **问题 / 瓶颈** · 外部日志难变成可复用的内部技能。
- **核心创新 / 方法** · 测试时内化执行经验并持续更新。
- **Baseline** · 已有代理记忆方式。
- **Benchmark** · 持续和域外任务以及内化模块的结构。
- **关键结果 / 消融** · 摘要报告记忆稳定且可见域外泛化。
- **适用条件 / 局限** · 更新具体依赖和代价未报告。

**可复用机制** · 验证内部经验学习需同时测长时间更新和域外复用，不能只看当题收益。

<a id="paper-152338"></a>

## Time–Frequency Non-Stationary Modeling for Multivariate Time Series Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/152338) · [作者来源](https://openreview.net/forum?id=ToQ5pSsGvK)

- **问题 / 瓶颈** · 全局周期可能产生虚假远距离依赖。
- **核心创新 / 方法** · 按片段估计频谱稳定性，融合时间和频率双路。
- **Baseline** · 现有多变量预测。
- **Benchmark** · 11 个基准，MSE 和 MAE。
- **关键结果 / 消融** · 在 55 项 MSE 比较中 44 项首位，MAE 43 项。
- **适用条件 / 局限** · 摘要未给可信度阈值和消融效果。

**可复用机制** · 长期依赖模型可对局部不稳定的频率降低权重，并保留时域证据。

<a id="paper-155398"></a>

## TimeOperator: A Function-to-Function Approach to Time Series Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/155398) · [作者来源](https://openreview.net/forum?id=5xJlZgQDqJ)

- **问题 / 瓶颈** · 跨频率常需换解码器或再采样。
- **核心创新 / 方法** · 从有限上下文构建样本条件算子，在指定查询时间求值。
- **Baseline** · 固定网格的时序预测。
- **Benchmark** · 跨频和跨时距预测。
- **关键结果 / 消融** · 摘要报告只改查询集合就能跨频预测。
- **适用条件 / 局限** · 依赖能被函数基表达的时间结构。

**可复用机制** · 预测接口若需多个采样分辨率，应把时间查询和内部状态建模分开。

<a id="paper-155395"></a>

## Time series analysis with Gumbel dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/155395) · [作者来源](https://openreview.net/forum?id=5yhfHMgZZG)

- **问题 / 瓶颈** · 标准切换模型可对噪声产生过多瞬时切换。
- **核心创新 / 方法** · 把离散状态松弛并在其上定义噪声。
- **Baseline** · 传统切换动力学。
- **Benchmark** · 两份真实随机时序数据。
- **关键结果 / 消融** · 摘要报告得到更可解释状态。
- **适用条件 / 局限** · 只给少数数据集，摘要未说明对真实突变效果。

**可复用机制** · 建模离散阶段切换时，验证观测噪声是否被错误解释成频繁状态跳跃。

<a id="paper-152955"></a>

## TimeTok: Granularity-Controllable Time-Series Generation via Hierarchical Tokenization

[官方论文页](https://neurips.cc/virtual/2026/poster/152955) · [作者来源](https://openreview.net/forum?id=P8dX5r550k)

- **问题 / 瓶颈** · 固定粒度生成无法消费草稿和多频预测请求。
- **核心创新 / 方法** · 从粗到细有序分词，供条件或无条件生成。
- **Baseline** · 固定分辨率生成法作为背景。
- **Benchmark** · 可控粒度时间序列生成。
- **关键结果 / 消融** · 摘要报告统一覆盖不同粒度设定。
- **适用条件 / 局限** · 未给每类任务数量与运行成本。

**可复用机制** · 多尺度生成可让粗 token 先表达主要变化，再按请求解码所需细节。

<a id="paper-150483"></a>

## Time to Pay Attention! Understanding High Complexity Corpus Reasoning Tasks

[官方论文页](https://neurips.cc/virtual/2026/poster/150483) · [作者来源](https://openreview.net/forum?id=hjbm3ZwK8d)

- **问题 / 瓶颈** · 相同语料大小可能对应完全不同的检索计算。
- **核心创新 / 方法** · 以语料任务复杂度刻画所需的小操作。
- **Baseline** · 简单语料推理与高复杂度条件。
- **Benchmark** · 长语料推理的效果与成本缩放。
- **关键结果 / 消融** · 摘要报告高复杂情景可呈二次成本。
- **适用条件 / 局限** · 前述复杂度依赖任务构造。

**可复用机制** · 评估长文预算应控制需组合的证据关系，而不是只控制词数。

<a id="paper-155785"></a>

## TimeTraveler: Temporal Strategy Planning with Time Dictionary for Streaming Video Understanding

[官方论文页](https://neurips.cc/virtual/2026/poster/155785) · [作者来源](https://openreview.net/forum?id=2vEb4EhU3O)

- **问题 / 瓶颈** · 全部请求使用统一回看策略会漏视频细节。
- **核心创新 / 方法** · 以时间字典保存观测，按问题时间意图指导检索。
- **Baseline** · 普通流式视频问答。
- **Benchmark** · 多个流式视频 QA 基准。
- **关键结果 / 消融** · 摘要报告改善流式回答并保留细粒度时间证据。
- **适用条件 / 局限** · 依赖时间标记和查询分析，摘要未给存储资源。

**可复用机制** · 连续感知系统将观测时间显式作为检索键，再按当前问题决定回看策略。

<a id="paper-139159"></a>

## TimeWarp: Evaluating Web Agents by Revisiting the Past

[官方论文页](https://neurips.cc/virtual/2026/poster/139159) · [作者来源](https://openreview.net/forum?id=hfun6NLTvi)

- **问题 / 瓶颈** · 在单版本上克隆动作会学到易变的视觉细节。
- **核心创新 / 方法** · 用历史网页版本对照并训练计划蒸馏。
- **Baseline** · 单版本的行为克隆。
- **Benchmark** · 网页代理和相关 Llama-3.1 8B 模型。
- **关键结果 / 消融** · 摘要指出视觉代理对界面更新敏感，并报告计划迁移有帮助。
- **适用条件 / 局限** · 页面快照差异可能伴随内容变化。

**可复用机制** · 如果界面经常迭代，可先复用目标和计划，再按当前界面求动作。

<a id="paper-151527"></a>

## Timing Is All You Need: SpikeCore, Learnable Delays, and Gain Control for Neuromorphic Classification

[官方论文页](https://neurips.cc/virtual/2026/poster/151527) · [作者来源](https://openreview.net/forum?id=a0D5EMqlKF)

- **问题 / 瓶颈** · 固定时序参数限制事件特征且需要更多仿真步。
- **核心创新 / 方法** · SpikeCore 保持可微训练并加入可学延迟与自适应阈值。
- **Baseline** · 常见神经形态分类架构。
- **Benchmark** · 神经形态分类的收敛、仿真步数和精度。
- **关键结果 / 消融** · 收敛快 5 至 6 倍，用约三分之一步数。
- **适用条件 / 局限** · 摘要未给硬件计量及迁移条件。

**可复用机制** · 时序稀疏计算应同时优化动态增益和实际所需步数。

<a id="paper-155663"></a>

## Tio: Language Models with Parallel Streams of Thoughts, Inputs and Outputs

[官方论文页](https://neurips.cc/virtual/2026/poster/155663) · [作者来源](https://openreview.net/forum?id=3w6cPaCQ2A)

- **问题 / 瓶颈** · 单一生成序列不能同时收新证据和完成输出。
- **核心创新 / 方法** · 并行建模思考、输入与输出流。
- **Baseline** · 标准单序列聊天模型。
- **Benchmark** · 实时并行交互，摘要未给基准细节。
- **关键结果 / 消融** · 作者报告可用性、效率及监控方面的优势。
- **适用条件 / 局限** · 摘要未给单流对照数值和部署成本。

**可复用机制** · 需要在线接收观察的代理应显式设计双向交互接口，而不是等待完整回合结束。

<a id="paper-151700"></a>

## TiRex-2: Generalizing TiRex to Multivariate Data and Streaming

[官方论文页](https://neurips.cc/virtual/2026/poster/151700) · [作者来源](https://openreview.net/forum?id=YgN3LimhOJ)

- **问题 / 瓶颈** · 长历史注意力会随上下文平方增长并反复计算。
- **核心创新 / 方法** · 结合时序混合与可更新记忆处理新补丁。
- **Baseline** · 依赖全历史注意力的预测模型。
- **Benchmark** · 流式多变量和单变量预测。
- **关键结果 / 消融** · 摘要报告每补丁推理保持常量，单变量活跃参数 38.4M。
- **适用条件 / 局限** · 多变量增加 44.1M 活跃参数，摘要未给端到端延迟。

**可复用机制** · 实时预测选型时比较追加一步的代价，而不只比较完整窗口吞吐。

<a id="paper-149496"></a>

## To Align or Not To Align: Check Your COMPASS Before You Train

[官方论文页](https://neurips.cc/virtual/2026/poster/149496) · [作者来源](https://openreview.net/forum?id=pi5rLDk0WR)

- **问题 / 瓶颈** · 强骨干组合和任务合并都可能破坏原技能
- **核心创新 / 方法** · 用训练前的配对兼容性评分预测对齐和任务算术
- **Baseline** · 候选编码器及不同合并对照
- **Benchmark** · 72 跨模态实验、392 合并；Flickr30k、COCO、八分类任务
- **关键结果 / 消融** · 图到文相关 0.90/0.91，技能保留相关 0.70
- **适用条件 / 局限** · 相关不证明因果且受候选分布影响

**可复用机制** · 按预估兼容性筛候选，再用统一小预算确认

<a id="paper-152547"></a>

## To Copy or Not to Copy: Controlling Speculative Decoding via Intrinsic Model Signals

[官方论文页](https://neurips.cc/virtual/2026/poster/152547) · [作者来源](https://openreview.net/forum?id=SLqBK6yQPm)

- **问题 / 瓶颈** · 上下文复制启发式容易在非复制片段浪费尝试
- **核心创新 / 方法** · 以内在表征判断切到复制或神经草稿
- **Baseline** · EAGLE3 及其他神经草稿
- **Benchmark** · Llama 与 Qwen；复制意图 AUC、吞吐
- **关键结果 / 消融** · AUC 超过 0.99，吞吐最高增 15%
- **适用条件 / 局限** · 依赖重复内容占比和可读取的内部信号

**可复用机制** · 按请求的可复制比例选择推测解码实现

<a id="paper-151823"></a>

## Token-Conditional Expert Dropout: Implicit Regularization for Stable MoE Pretraining

[官方论文页](https://neurips.cc/virtual/2026/poster/151823) · [作者来源](https://openreview.net/forum?id=XhZkbaD4Ft)

- **问题 / 瓶颈** · 辅助损失平衡需调系数且可能干扰专门化
- **核心创新 / 方法** · 用条件专家 dropout 做隐式负载正则
- **Baseline** · 原 MoE 和调优过的辅助损失
- **Benchmark** · 1.4B 激活/8B 总参数、480B tokens；MMLU-Pro、GPQA
- **关键结果 / 消融** · 利用方差少 67%，两基准各高 2.1 分
- **适用条件 / 局限** · 单随机种子，证据初步

**可复用机制** · 同训练预算测均衡与精度再做多种子核验

<a id="paper-154486"></a>

## Tokenization and Architecture Jointly Allocate Component Roles in Time Series Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/154486) · [作者来源](https://openreview.net/forum?id=DF6i5h0EXW)

- **问题 / 瓶颈** · 同一模块在点 token 和变量 token 上承担不同角色
- **核心创新 / 方法** · 审计跨特征信号经过哪个部件，比较分词和架构交互
- **Baseline** · DLinear、PatchTST、TSMixer、PatchMLP、iTransformer、CATS
- **Benchmark** · 时序预测架构的部件和表征诊断
- **关键结果 / 消融** · 单点分词弱化 FFN，变量分词可由注意主导
- **适用条件 / 局限** · 受各架构部件定义与信号传播测试影响

**可复用机制** · 比较时序骨干时同时匹配 token 语义与模块作用

<a id="paper-150812"></a>

## Tokenizer Choice Shapes Generalization in State-Centric Learning for Planning

[官方论文页](https://neurips.cc/virtual/2026/poster/150812) · [作者来源](https://openreview.net/forum?id=fBjXy542NQ)

- **问题 / 瓶颈** · 预测头更换可能掩盖表示丢掉状态不变量
- **核心创新 / 方法** · 对状态分词与其他管线因素做受控选择，分 IID 与 OOD
- **Baseline** · 不同状态分词和预测头配置
- **Benchmark** · 状态中心学习规划；同分布和分布外
- **关键结果 / 消融** · 分词影响最大且在 OOD 更强
- **适用条件 / 局限** · 结果限于所试规划任务和状态形态

**可复用机制** · 先找到状态编码失败，再优化预测网络

<a id="paper-148519"></a>

## Tokenizer-Generator Coupling in Medical Image Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/148519) · [作者来源](https://openreview.net/forum?id=xImy5OosQz)

- **问题 / 瓶颈** · 分词重建强不等于和给定采样器兼容
- **核心创新 / 方法** · 按 tokenizer、生成器和推理预算做交叉实验
- **Baseline** · 54 离散组合、16 连续参考
- **Benchmark** · 低分辨无条件医学图；重建和非临床 FID
- **关键结果 / 消融** · 同分词器结果随配对改变，支持联合选型
- **适用条件 / 局限** · 单种子、低分无条件，不能推断临床效用

**可复用机制** · 视觉生成采用固定预算矩阵比较压缩、重建与可建模性

<a id="paper-149648"></a>

## Tokens-per-Parameter Coverage Is Critical for Robust LLM Scaling Law Extrapolation

[官方论文页](https://neurips.cc/virtual/2026/poster/149648) · [作者来源](https://openreview.net/forum?id=oVM1ErNilo)

- **问题 / 瓶颈** · 参数和 token 固定比例的组合让参数估计病态
- **核心创新 / 方法** · 使用不共线的标度实验设计并分析雅可比
- **Baseline** · 共线训练设计
- **Benchmark** · 四标度律、五语料、多个精度模式和留出预测
- **关键结果 / 消融** · 不共线设计胜率 97.3%
- **适用条件 / 局限** · 结论仍依赖拟合律与有效样本范围

**可复用机制** · 预训练成本拟合时有意改变数据模型比例而非只扫总算力

<a id="paper-152684"></a>

## TokenSwap: Benchmarking and Reducing the Modality Gap in Multimodal LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/152684) · [作者来源](https://openreview.net/forum?id=RByqiSbFJf)

- **问题 / 瓶颈** · 模型规模或提示无法保证对等输入上的表现对齐
- **核心创新 / 方法** · 用 TokenSwap 测互换输入并加入训练
- **Baseline** · 推理与非推理模型、提示和规模变化
- **Benchmark** · 文本及视觉条件的输入等价测评
- **关键结果 / 消融** · 平均差距 10.1% 对 25.5%，训练可减差且保留两类能力
- **适用条件 / 局限** · 模态互换必须保持足够信息及难度一致

**可复用机制** · 把用户给同一信息的不同媒介做成成对回归

<a id="paper-156116"></a>

## ToLD: Efficient Time Series Forecasting via Tokenized Truncated Latent Diffusion

[官方论文页](https://neurips.cc/virtual/2026/poster/156116) · [作者来源](https://openreview.net/forum?id=0Gm2nx7nXH)

- **问题 / 瓶颈** · 训练时可见目标会让推理排名失配。
- **核心创新 / 方法** · 截断 token 潜扩散，并蒸馏无需目标的候选分数。
- **Baseline** · 现有预测。
- **Benchmark** · 八现实时间序列，MSE 和 CRPS。
- **关键结果 / 消融** · 最多 MSE 改善 4.3%，CRPS 降 19.3%。
- **适用条件 / 局限** · 依赖评分在新趋势下的可靠性。

**可复用机制** · 提高多样本质量时避免用部署不可见特征。

<a id="paper-150420"></a>

## ToMAToMP: Robust and Multi-Parameter Topological Clustering

[官方论文页](https://neurips.cc/virtual/2026/poster/150420) · [作者来源](https://openreview.net/forum?id=iAga8AJtXJ)

- **问题 / 瓶颈** · 单函数及图参数影响簇。
- **核心创新 / 方法** · 多参数持续同调分解构造稳健聚类。
- **Baseline** · 拓扑及非拓扑比较。
- **Benchmark** · 多数据集以及 outlier。
- **关键结果 / 消融** · 摘要称聚类质量和效率改善。
- **适用条件 / 局限** · 多参数分解成本及距离选择要核。

**可复用机制** · 有多尺度、多信号时用共同拓扑而非只调一张图。

<a id="paper-153219"></a>

## TOM-Pruning: Target-aware Output Manifold for LLM Pruning

[官方论文页](https://neurips.cc/virtual/2026/poster/153219) · [作者来源](https://openreview.net/forum?id=Mv31DAbjkw)

- **问题 / 瓶颈** · 欧式重构忽视对后级重要方向。
- **核心创新 / 方法** · 建局部输出流形与竞争通道相似度。
- **Baseline** · SparseGPT、Wanda。
- **Benchmark** · 多 LLM，多个稀疏率和 WikiText-2。
- **关键结果 / 消融** · 摘要报告一设定困惑度降低 26.8%。
- **适用条件 / 局限** · 局部统计和任务依赖需复验。

**可复用机制** · 剪枝损失与输出真正使用度量保持一致。

<a id="paper-150179"></a>

## Too Aligned to be Real: Detecting AI-Generated Images via Cross-modal Alignment Shift

[官方论文页](https://neurips.cc/virtual/2026/poster/150179) · [作者来源](https://openreview.net/forum?id=k72oka2LYR)

- **问题 / 瓶颈** · 内容差异常被误认为生成痕迹。
- **核心创新 / 方法** · 以语义匹配对量对齐漂移并训练检测器。
- **Baseline** · 已有图像生成检测。
- **Benchmark** · 扩散、GAN、自回归及商业体系。
- **关键结果 / 消融** · 商业生成器 ACC 和 AP 加 5.48% 与 6.13%。
- **适用条件 / 局限** · 新的对齐目标可能改变失配。

**可复用机制** · 先控制图文语义再量生成信号。

<a id="paper-154043"></a>

## ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/154043) · [作者来源](https://openreview.net/forum?id=Geiw1NtYWx)

- **问题 / 瓶颈** · 全程 RL 成本高且混合轨迹难收。
- **核心创新 / 方法** · 从已有 GUI 轨迹合成交错工具并 warmup，再练单轮切换。
- **Baseline** · OSWorld-MCP 现有基线。
- **Benchmark** · GUI 工具路由与任务准确率。
- **关键结果 / 消融** · 46.85% 准确率，相对基线逾 60%。
- **适用条件 / 局限** · 合成工具覆盖和权限需控制。

**可复用机制** · 训练混合代理先定位影响最大的接口切换再局部优化。

<a id="paper-148956"></a>

## Tool-Integrated Reasoning via Hierarchical Multi-Agent Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/148956) · [作者来源](https://openreview.net/forum?id=tu0xIum8Fk)

- **问题 / 瓶颈** · 代理分离后反馈难协同。
- **核心创新 / 方法** · 高层和低层分工，用层级 RL 对齐。
- **Baseline** · 单、多代理基线。
- **Benchmark** · 数学推理及 QA，多个底座。
- **关键结果 / 消融** · 一致改善，幅度未核。
- **适用条件 / 局限** · 执行反馈必须可验证。

**可复用机制** · 共享结局目标不意味着必须共用推理上下文。

<a id="paper-154321"></a>

## Tool-IQA: Augmenting Image Quality Assessment with Simple Tools

[官方论文页](https://neurips.cc/virtual/2026/poster/154321) · [作者来源](https://openreview.net/forum?id=EXsWjLfKTF)

- **问题 / 瓶颈** · 全局原亮度观察会漏局部伪影。
- **核心创新 / 方法** · 用局部查看等工具，比较批中调用贡献。
- **Baseline** · 单次全局评分。
- **Benchmark** · 多图像质量基准。
- **关键结果 / 消融** · 摘要报告有效工具增强，幅度未核。
- **适用条件 / 局限** · 额外工具调用需按成本复测。

**可复用机制** · 工具奖励按信息增益而非次数。

<a id="paper-155860"></a>

## Tools as Continuous Flow for Evolving Agentic Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/155860) · [作者来源](https://openreview.net/forum?id=2MsbN9cHvM)

- **问题 / 瓶颈** · 逐步离散选工具容易局部短视。
- **核心创新 / 方法** · 条件流匹配生成连续轨迹，再执行离散计划。
- **Baseline** · 常规工具编排。
- **Benchmark** · 动态环境计划级闭环基准。
- **关键结果 / 消融** · 给出效用收敛分析，数值待核。
- **适用条件 / 局限** · 潜动作和具体 API 的映射需验证。

**可复用机制** · 全局计划和执行离散化分开评估。

<a id="paper-154349"></a>

## ToolSearcher: Optimizing Tool Selection at Scale via Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/154349) · [作者来源](https://openreview.net/forum?id=EFnOrwjviv)

- **问题 / 瓶颈** · 同功能工具难区分，终局奖励不能定位检索失败。
- **核心创新 / 方法** · 按类别对比、多轮发现建模及分段奖励。
- **Baseline** · 强大型工具选择基线。
- **Benchmark** · 迭代搜索与工具组合。
- **关键结果 / 消融** · 多设置持续改善。
- **适用条件 / 局限** · 需要可靠类别及候选工具描述。

**可复用机制** · 找对工具和正确调用是可分别监督的目标。

<a id="paper-153674"></a>

## Tool Verification for Test-Time Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/153674) · [作者来源](https://openreview.net/forum?id=Jd7P3rhNnN)

- **问题 / 瓶颈** · 自一致信号对硬题反馈偏。
- **核心创新 / 方法** · 将工具验证接入测试时 RL。
- **Baseline** · TTRL。
- **Benchmark** · MATH-500、AMC、AIME 2024，多个模型。
- **关键结果 / 消融** · 难题改善尤明显，幅度未报告。
- **适用条件 / 局限** · 需可信执行器与预算。

**可复用机制** · 测试时适配前比较外部核验和内部投票。

<a id="paper-152134"></a>

## Too Smart to Teach: The Articulability Ceiling in Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152134) · [作者来源](https://openreview.net/forum?id=VGyVnplxNq)

- **问题 / 瓶颈** · 强解题器未必是强解释教师。
- **核心创新 / 方法** · 交叉配解释器和接收器，测试上下文迁移。
- **Baseline** · 360M 至 72B 教师，base 与 instruct。
- **Benchmark** · 40 教师、5 接收、13 来源。
- **关键结果 / 消融** · 中型教师可胜最大模型，教师正确性最关键。
- **适用条件 / 局限** · 实证为上下文解释，非参数蒸馏。

**可复用机制** · 按教学提升而非单题排名选教师。

<a id="paper-149592"></a>

## Top-$k$ Identification with Correlated Biased LLM Judges via Anchor Leverage

[官方论文页](https://neurips.cc/virtual/2026/poster/149592) · [作者来源](https://openreview.net/forum?id=owIAxN3QtB)

- **问题 / 瓶颈** · 多个相关裁判不消除同一系统偏差。
- **核心创新 / 方法** · 在因子偏差下用顺序分配并保守选锚。
- **Baseline** · 平均裁判和普通抽样。
- **Benchmark** · Arena-Hard v2.0 十裁判。
- **关键结果 / 消融** · 分析可识别性和代价最优，达到下界常数。
- **适用条件 / 局限** · 需要足够低维偏差假设。

**可复用机制** · 把人工核评价用于能改变榜单边界的方向。

<a id="paper-152095"></a>

## ToPA: Block-wise Toeplitz Adaptation for Expressive and Efficient Fine-Tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/152095) · [作者来源](https://openreview.net/forum?id=VYQLuuY0tY)

- **问题 / 瓶颈** · 长 Toeplitz 连乘难训，低秩容量有限。
- **核心创新 / 方法** · 块 Toeplitz 因子提高每因子表达。
- **Baseline** · 普通 Toeplitz、低秩及稀疏。
- **Benchmark** · 21 NLP/CV 数据和五架构。
- **关键结果 / 消融** · 证明更短链能逼近任意矩阵，实证支持。
- **适用条件 / 局限** · 实际内核成本需测。

**可复用机制** · 结构适配器选算子因子数和表达率双指标。

<a id="paper-153868"></a>

## Topic-Aware Contextual Cascading Bandits

[官方论文页](https://neurips.cc/virtual/2026/poster/153868) · [作者来源](https://openreview.net/forum?id=I9fcrY6tSo)

- **问题 / 瓶颈** · 独立点击假设忽略已展示项语义。
- **核心创新 / 方法** · 把已选主题表示为 MDP 状态，乐观优化。
- **Baseline** · 无主题上下文的级联。
- **Benchmark** · 点击 cascade 理论与遗憾。
- **关键结果 / 消融** · 给依条件改善的序列长度界及下界。
- **适用条件 / 局限** · 需要主题摘要有用且点击模型成立。

**可复用机制** · 排序器分别估单项质量和上文造成的边际变化。

<a id="paper-149504"></a>

## TopoCurve: Geometry-Aware Topology Reasoning via Bézier Curves in Autonomous Driving

[官方论文页](https://neurips.cc/virtual/2026/poster/149504) · [作者来源](https://openreview.net/forum?id=peNZjVneDd)

- **问题 / 瓶颈** · 离散曲线点不利于判断连接。
- **核心创新 / 方法** · 用 Bézier 参数化结构化车道。
- **Baseline** · 普通 3D 拓扑模型。
- **Benchmark** · 自动驾驶道路结构。
- **关键结果 / 消融** · 摘要明确几何方案，实验数值待核。
- **适用条件 / 局限** · 只保曲线不足处理分叉和不确定性。

**可复用机制** · 将空间连接推理绑定到可解析的形状参数。

<a id="paper-154783"></a>

## TopoFisher: Learning Topological Summary Statistics by Maximizing Fisher Information

[官方论文页](https://neurips.cc/virtual/2026/poster/154783) · [作者来源](https://openreview.net/forum?id=B1JksRv4SE)

- **问题 / 瓶颈** · 固定拓扑统计可能保形却丢最关键信息。
- **核心创新 / 方法** · 端到端最大化局部高斯 Fisher。
- **Baseline** · 固定拓扑 vectorization。
- **Benchmark** · 噪旋、随机场和弱引力透镜。
- **关键结果 / 消融** · 回收大量已知信息，优于比较对象。
- **适用条件 / 局限** · 局部高斯和模拟器条件影响。

**可复用机制** · 按下游估计目标挑拓扑特征而非全部保留。

<a id="paper-139025"></a>

## TopoGraphRAG-Bench: Evaluating Multimodal GraphRAG on Layout-Grounded Evidence Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/139025) · [作者来源](https://openreview.net/forum?id=pXhvOZB8Qw)

- **问题 / 瓶颈** · 纯检索命中不能代表恢复版面角色。
- **核心创新 / 方法** · 对照实体图和版面锚，包括多模态及文字系统。
- **Baseline** · 文本图、整页视觉检索、多模态图。
- **Benchmark** · TopoGraphRAG-Bench，检索生成和拓扑。
- **关键结果 / 消融** · 摘要指出版面、模态和证据功能都影响结果。
- **适用条件 / 局限** · 文档布局标注需有明确目标。

**可复用机制** · 以布局和证据角色共同定义文档查询验收。

<a id="paper-153082"></a>

## Topological Invariance and Breakdown in Learning Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/153082) · [作者来源](https://openreview.net/forum?id=O7QMMCGEnE)

- **问题 / 瓶颈** · 大步可能简化神经元流形。
- **核心创新 / 方法** · 以参数置换对称证明更新的拓扑阈值。
- **Baseline** · 低、高学习率。
- **Benchmark** · 神经元集合几何的理论。
- **关键结果 / 消融** · 阈值下保拓扑，上方可能破坏。
- **适用条件 / 局限** · 取决于更新和对称条件。

**可复用机制** · 选择学习率时检查隐结构是否应允许重组。

<a id="paper-151629"></a>

## Topological Out-of-Domain Generalization in Dynamical Systems Reconstruction

[官方论文页](https://neurips.cc/virtual/2026/poster/151629) · [作者来源](https://openreview.net/forum?id=Z8RyfGuta0)

- **问题 / 瓶颈** · 混合所有变量会在越过转折后失效。
- **核心创新 / 方法** · 做 feature splitting 并推可靠外推范围。
- **Baseline** · 分层和超网驱动重建。
- **Benchmark** · 跨动态制度与 tipping point。
- **关键结果 / 消融** · 零样本外推得到改善。
- **适用条件 / 局限** · 有界范围和新系统参数可识别性须检查。

**可复用机制** · 为世界模型给出外推范围并分开学各类潜参数。

<a id="paper-149943"></a>

## Topological Periodicity Test (TopPT) via Confidence Bound of Time-Delay Embeddings

[官方论文页](https://neurips.cc/virtual/2026/poster/149943) · [作者来源](https://openreview.net/forum?id=m2C92vyCO3)

- **问题 / 瓶颈** · 单值谱峰难以标记局部周期何时存在。
- **核心创新 / 方法** · 对持续图做子采样区间并校正插值误差。
- **Baseline** · 周期图。
- **Benchmark** · PhysioNet Fantasia 与 BIDMC 呼吸记录。
- **关键结果 / 消融** · 多数记录被检测，但只有部分局部窗通过。
- **适用条件 / 局限** · 依赖流形正则，可能偏保守。

**可复用机制** · 当全局周期掩盖局部变化时，记录周期证据随窗口的稳定区间。

<a id="paper-150154"></a>

## Topology-Aware Optimal Transport for Source-Free Test-Time Adaptation in Anomaly Segmentation

[官方论文页](https://neurips.cc/virtual/2026/poster/150154) · [作者来源](https://openreview.net/forum?id=kG41FPloKc)

- **问题 / 瓶颈** · 单阈值特征会随测试域变化。
- **核心创新 / 方法** · 串联最优传输对齐拓扑持久图。
- **Baseline** · 既有无源测试适配。
- **Benchmark** · 二维和三维异常分割。
- **关键结果 / 消融** · 平均 F1 最高分别比次优增 24.1% 与 10.2%。
- **适用条件 / 局限** · 摘要未给部署耗时。

**可复用机制** · 适配前用阈值敏感性检测伪结构。

<a id="paper-153660"></a>

## Topology-Aware Representation Alignment for Semi-Supervised Vision-Language Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/153660) · [作者来源](https://openreview.net/forum?id=JgmIV10Z6r)

- **问题 / 瓶颈** · 匹配持久图不保证配对几何对齐。
- **核心创新 / 方法** · 筛选拓扑显著边并用于图文嵌入对齐。
- **Baseline** · 其他拓扑目标与常规视觉语言对齐。
- **Benchmark** · 时尚检索等半监督任务。
- **关键结果 / 消融** · 报告更稳定，H1 出生边有用。
- **适用条件 / 局限** · 适用于可构造拓扑关系的配对资料。

**可复用机制** · 当配对稀缺时可用关键关系来约束两侧几何。

<a id="paper-154394"></a>

## TopoPrune: Robust Data Pruning via Unified Latent Space Topology

[官方论文页](https://neurips.cc/virtual/2026/poster/154394) · [作者来源](https://openreview.net/forum?id=DulZFWkYOG)

- **问题 / 瓶颈** · 只看单样本分数可能丢掉连接数据群的重要样本。
- **核心创新 / 方法** · 低维流形近似和可微持久同调联合排序。
- **Baseline** · 现有数据剪枝法。
- **Benchmark** · 跨架构数据保留与模型训练。
- **关键结果 / 消融** · 摘要称跨架构迁移更优。
- **适用条件 / 局限** · 依赖低维映射质量，摘要未给计算时间。

**可复用机制** · 筛选小训练集时对照结构覆盖与样本点质量。

<a id="paper-150854"></a>

## TopoScope: A Graph-Scoped LLM Agent for Printed Circuit Board Schematic Design

[官方论文页](https://neurips.cc/virtual/2026/poster/150854) · [作者来源](https://openreview.net/forum?id=et1Tk9D1jg)

- **问题 / 瓶颈** · 全量图上下文和自然语言规则容易产生引用错误。
- **核心创新 / 方法** · 按元件决策裁剪上下文，用结构模式验证规则。
- **Baseline** · 给予知识的电路专用基线。
- **Benchmark** · 中高难度多芯片原理图。
- **关键结果 / 消融** · 摘要报告有效性提高、非法图引用减少。
- **适用条件 / 局限** · 依赖可表示为图模式的约束，证据限电路。

**可复用机制** · 结构化代理可把输出图同时作为检索边界和验证空间。

<a id="paper-153864"></a>

## TOPPO: Rethinking PPO for Multi-Task Reinforcement Learning with Critic Balancing

[官方论文页](https://neurips.cc/virtual/2026/poster/153864) · [作者来源](https://openreview.net/forum?id=IB0sNv6vy7)

- **问题 / 瓶颈** · 只扩大网络可能无法解决多任务优化失衡。
- **核心创新 / 方法** · TOPPO 通过 critic 平衡改善梯度条件和任务学习动态。
- **Baseline** · 常规 PPO 及离策略 SAC。
- **Benchmark** · 多任务 RL。
- **关键结果 / 消融** · 摘要报告在所测任务赶上或超过离策略方案。
- **适用条件 / 局限** · 摘要未给各组件边界。

**可复用机制** · 多任务策略退化时可先校验价值误差在任务之间的权重。

<a id="paper-150449"></a>

## TORNADO: Adaptive Latent Stochastic Transport for Calibrated Probabilistic PDE Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/150449) · [作者来源](https://openreview.net/forum?id=hxP9I13XQ2)

- **问题 / 瓶颈** · 全局同噪声不能反映不同局部动态的不确定性。
- **核心创新 / 方法** · 对潜状态的后验转移学习状态相关 SDE。
- **Baseline** · 预设全局噪声。
- **Benchmark** · 概率 PDE 预测及校准。
- **关键结果 / 消融** · 作者报告状态相关噪声改善校准。
- **适用条件 / 局限** · 摘要未给跨系统收益。

**可复用机制** · 预测置信度应随当前状态变化，而不仅随外推时长变化。

<a id="paper-152940"></a>

## To See Far, Look Close: Evolutionary Forecasting for Long-term Time Series

[官方论文页](https://neurips.cc/virtual/2026/poster/152940) · [作者来源](https://openreview.net/forum?id=PFfOPbcZCE)

- **问题 / 瓶颈** · 直接远期梯度可能与局部动力学习冲突。
- **核心创新 / 方法** · 用演化式预测和短程动态外推。
- **Baseline** · 直接长跨度预测。
- **Benchmark** · 长程时序基准及更远外推。
- **关键结果 / 消融** · 摘要报告改善预测和稳定性。
- **适用条件 / 局限** · 需留意递推误差，摘要未给边界。

**可复用机制** · 直接预测退化时可按时距检查梯度冲突，再选择训练目标。

<a id="paper-151185"></a>

## ToS: Tree-of-Skill Reinforcement Learning driven by Behavior Tree for Long-Horizon Manipulation

[官方论文页](https://neurips.cc/virtual/2026/poster/151185) · [作者来源](https://openreview.net/forum?id=cKguVoE2ry)

- **问题 / 瓶颈** · 固定技能链难处理不同中间结果。
- **核心创新 / 方法** · 用行为模型在树执行时预测下一技能。
- **Baseline** · 预设技能顺序和去掉引导网络。
- **Benchmark** · 长程操作与未见任务、真机。
- **关键结果 / 消融** · 作者报告支持未见任务且可部署。
- **适用条件 / 局限** · 依赖可复用技能与状态估计。

**可复用机制** · 将任务结构和可变执行顺序分开，使局部技能能在不同分支复用。

<a id="paper-153131"></a>

## Total Variation Distance Estimation in Autoregressive Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153131) · [作者来源](https://openreview.net/forum?id=NfXgepjfRz)

- **问题 / 瓶颈** · 通过采样、浮点概率或完整 logits 获得的信息不同。
- **核心创新 / 方法** · 对应三种接口建立估算器并分析查询量。
- **Baseline** · KL 等替代指标。
- **Benchmark** · 自回归序列和 vLLM 等系统比较。
- **关键结果 / 消融** · logit 访问下查询量阶为 n/ε²，且为紧界。
- **适用条件 / 局限** · 概率误差大时效益下降。

**可复用机制** · 验证不同推理后端不应只对照最终文本，还可估计整序列分布差异。

<a id="paper-148558"></a>

## To Think or Not to Think: Pre-Decisional Reasoning Budgets for Referring Audio-Visual Segmentation

[官方论文页](https://neurips.cc/virtual/2026/poster/148558) · [作者来源](https://openreview.net/forum?id=x0E7dh4iw2)

- **问题 / 瓶颈** · 统一推理预算会在不适合的样本放大定位漂移。
- **核心创新 / 方法** · 用无泄漏的收益标注训练线性读出。
- **Baseline** · 固定和统一推理预算。
- **Benchmark** · 指代音视分割及定位质量。
- **关键结果 / 消融** · 摘要报告线性可解码的追加推理收益信号。
- **适用条件 / 局限** · 依赖具有代表性的预算比较标签。

**可复用机制** · 在生成前以实际增益作门控目标，而非只预测任务难度。

<a id="paper-149345"></a>

## Touch-R1: Reinforcing Touch Reasoning in MLLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/149345) · [作者来源](https://openreview.net/forum?id=qmrtrsIjCK)

- **问题 / 瓶颈** · 不同硬件的触觉特征变化会让模型学传感器相关捷径。
- **核心创新 / 方法** · 在多传感器同步触觉数据上训练基于动作观察的推理。
- **Baseline** · 原多模态推理基座。
- **Benchmark** · TouchReason-1M、TouchReason-Bench，含四种传感器。
- **关键结果 / 消融** · 摘要报告出现探查、比较和修订行为。
- **适用条件 / 局限** · 摘要未给去掉规模扩张的独立收益。

**可复用机制** · 评价接触推理应区分材料知识和对真实接触信号的依赖。

<a id="paper-148215"></a>

## Toward a theory of Evaluability

[官方论文页](https://neurips.cc/virtual/2026/poster/148215) · [作者来源](https://openreview.net/forum?id=zVxctUGl6p)

- **问题 / 瓶颈** · 黑盒评估不能默认测试与训练不相交。
- **核心创新 / 方法** · 比较不同信息下的可评估性，利用少量模型查询辅助。
- **Baseline** · 不允许或较少交互的评估。
- **Benchmark** · 自然分布与所分析的概念类。
- **关键结果 / 消融** · 摘要报告少量查询可增强某些设置中的可评估性。
- **适用条件 / 局限** · 理论受分布和概念类约束。

**可复用机制** · 评估协议应将污染状态写进假设，并检验查询能否提供独立证据。

<a id="paper-153758"></a>

## Toward Efficient Reasoning of Large Language Models via Latent Concept-Pyramid Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/153758) · [作者来源](https://openreview.net/forum?id=Iv6yJZqzWG)

- **问题 / 瓶颈** · 逐词生成的推理较贵而单级压缩可能失去关键信息
- **核心创新 / 方法** · 将链式推理组织为层级潜在概念并检查能否还原
- **Baseline** · 常规显式 CoT
- **Benchmark** · Qwen2.5 和 Qwen3；精度、token、时延及零样本
- **关键结果 / 消融** · 减少 token 和时延并保持竞争力，幅度未报告
- **适用条件 / 局限** · 可还原原推理不代表因果解释忠实

**可复用机制** · 效率评测同时记录推理可审阅性与答题成本

<a id="paper-139380"></a>

## Toward Interactive Understanding of Code APIs

[官方论文页](https://neurips.cc/virtual/2026/poster/139380) · [作者来源](https://openreview.net/forum?id=Tua6AP83Su)

- **问题 / 瓶颈** · 模型不清楚当前假设质量，过早停止探索
- **核心创新 / 方法** · 用非对称 actor-critic 改善可执行试探，运行仍按常规观察
- **Baseline** · 原模型，GPT-5-mini
- **Benchmark** · 交互式 API 理解和探索
- **关键结果 / 消融** · 调整后的 Qwen3-8B 追平 GPT-5-mini
- **适用条件 / 局限** · 训练需有能给 critic 的特权信息

**可复用机制** · 当工具助手过早结束时先给训练价值估计明确监督

<a id="paper-148466"></a>

## Towards Anytime-Valid Statistical Watermarking

[官方论文页](https://neurips.cc/virtual/2026/poster/148466) · [作者来源](https://openreview.net/forum?id=xbsjNKS4Iq)

- **问题 / 瓶颈** · 固定长度检测会给明显案例花过多样本
- **核心创新 / 方法** · 用 e-value 设计任意时点有效的顺序水印检测
- **Baseline** · 既有统计水印检测
- **Benchmark** · 模拟与基准；平均检测 token 预算
- **关键结果 / 消融** · 预算约低 13–15%
- **适用条件 / 局限** · 最优性依赖指定模型及最坏增长条件

**可复用机制** · 验收提前停规则时同时报告误报和所需文本长度

<a id="paper-139379"></a>

## Towards Characterizing Scientific Image Utility and Upgradability

[官方论文页](https://neurips.cc/virtual/2026/poster/139379) · [作者来源](https://openreview.net/forum?id=TudxFw3oZz)

- **问题 / 瓶颈** · 视觉观感提升可掩盖关键信息被改错
- **核心创新 / 方法** · 分开评价错误诊断和忠实修复，再比较两者瓶颈
- **Baseline** · 现有多模态恢复系统
- **Benchmark** · 科学图像错误评估与可修复性
- **关键结果 / 消融** · 诊断能力限制修复效果，数值未报告
- **适用条件 / 局限** · 需专家定义科学性错误，不能用感知分数替代

**可复用机制** · 采集图像修复的保真回归集，先对错误类型做分类

<a id="paper-151917"></a>

## Towards Closing the Autoregressive Gap in Language Modeling via Entropy-Gated Continuous Bitstream Diffusion

[官方论文页](https://neurips.cc/virtual/2026/poster/151917) · [作者来源](https://openreview.net/forum?id=WvVrxnsb7c)

- **问题 / 瓶颈** · 标准扩散头随词表线性增大
- **核心创新 / 方法** · 预测语义 bit patch 并以熵门控调采样
- **Baseline** · 既有语言扩散与 1024-NFE 设置
- **Benchmark** · 语言模型熵、推理步和显存效率
- **关键结果 / 消融** · 摘要报熵 5.26，以四分之一步数达到相应水平
- **适用条件 / 局限** · bit 编码结构和自然词元语义对齐待核

**可复用机制** · 在同质量目标比较词表增大时的吞吐及输出错误

<a id="paper-154279"></a>

## Towards Complementary Keypoint Detection via Mixture of Detectors

[官方论文页](https://neurips.cc/virtual/2026/poster/154279) · [作者来源](https://openreview.net/forum?id=F1HI02weX5)

- **问题 / 瓶颈** · 单一规则兼顾数量、位置均匀及匹配困难
- **核心创新 / 方法** · 用下游匹配质量给检测器路由训练奖励
- **Baseline** · 强几何关键点检测方法
- **Benchmark** · MegaDepth、ScanNet、HPatches 和多档点预算
- **关键结果 / 消融** · 多个预算优于对照，数字未报告
- **适用条件 / 局限** · 依赖检测器确有互补性

**可复用机制** · 按几何跟踪任务选择路由，而非只最大化候选数

<a id="paper-155526"></a>

## Towards Convergence of PPO: An Approximate Descent Approach

[官方论文页](https://neurips.cc/virtual/2026/poster/155526) · [作者来源](https://openreview.net/forum?id=4w3wfZ8itN)

- **问题 / 瓶颈** · 多轮 clipping 可能偏离原梯度但减少重采样
- **核心创新 / 方法** · 用近似下降分析多轮及重新洗牌的小批量更新
- **Baseline** · 单步策略优化和标准 PPO
- **Benchmark** · 光滑与有界 critic 偏差条件，摘要未列实验
- **关键结果 / 消融** · 获得收敛到驻点；额外轮引偏但有优化效率价值
- **适用条件 / 局限** · 理论依赖 critic 偏差界和稳定小步

**可复用机制** · 调整 PPO epoch 前分开记录样本重用和实际 KL 漂移

<a id="paper-151969"></a>

## Towards Direct Evaluation of Harness Optimizers via Priority Ranking

[官方论文页](https://neurips.cc/virtual/2026/poster/151969) · [作者来源](https://openreview.net/forum?id=WSQLJ0m6kS)

- **问题 / 瓶颈** · 仅验最终成绩掩盖中间选择错误且昂贵。
- **核心创新 / 方法** · 要求按更改组件对性能可能影响排名。
- **Baseline** · 整套 harness 实验。
- **Benchmark** · 代理工具和脚手架更改。
- **关键结果 / 消融** · 可低成本直接量步骤决策。
- **适用条件 / 局限** · 排名不能代替最终端到端验收。

**可复用机制** · 把先改哪一项与最后是否改善分开测。

<a id="paper-153005"></a>

## Towards Direct Latent-Space Synthesis for Parallel Branches in LLM-Agent Workflows

[官方论文页](https://neurips.cc/virtual/2026/poster/153005) · [作者来源](https://openreview.net/forum?id=Og5N7tTV6X)

- **问题 / 瓶颈** · 重复重编码传递文本增加代价。
- **核心创新 / 方法** · 综合分支直接读 KV。
- **Baseline** · 显式文本汇总。
- **Benchmark** · 并行代理工作流。
- **关键结果 / 消融** · 摘要给可插拔机制，量化待核。
- **适用条件 / 局限** · 需位置、模型和权限兼容。

**可复用机制** · 复用中间表示前测分支隔离和合并正确性。

<a id="paper-152751"></a>

## Toward Semantically-Consistent Tuning-Free Customization for Rectified Flow Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/152751) · [作者来源](https://openreview.net/forum?id=Qbw59DT7mb)

- **问题 / 瓶颈** · 保参照可能牺牲指令对齐。
- **核心创新 / 方法** · 在 rectified flow Transformer 中显式语义控制。
- **Baseline** · 已有免微调定制。
- **Benchmark** · 内容特定性和提示对齐。
- **关键结果 / 消融** · 两轴改善，数字待核。
- **适用条件 / 局限** · 摘要未给足模块细节。

**可复用机制** · 定制必须分别评参照保留和编辑实现。

<a id="paper-139021"></a>

## Towards Error-Free EHRs: Reasoning-Intensive Consistency Verification Between Clinical Notes and Structured Tables in Electronic Health Records

[官方论文页](https://neurips.cc/virtual/2026/poster/139021) · [作者来源](https://openreview.net/forum?id=q9O85I1Yqn)

- **问题 / 瓶颈** · 全文匹配会漏条件或时间冲突。
- **核心创新 / 方法** · 分段并按 anchor 动态调用表格工具。
- **Baseline** · 现有跨文档核对。
- **Benchmark** · EHR-ReasonCon，专家校准宽严标准。
- **关键结果 / 消融** · 多个底座表现领先，幅度未核。
- **适用条件 / 局限** · 临床数据的高门槛隐私与评估需另验。

**可复用机制** · 以实体和时间约束缩小工具查询范围。

<a id="paper-153706"></a>

## Towards Fair Graph Generation Without Sensitive Attribute

[官方论文页](https://neurips.cc/virtual/2026/poster/153706) · [作者来源](https://openreview.net/forum?id=JNw2R5LH1O)

- **问题 / 瓶颈** · 先固定错误敏感代理会把偏差带入生成。
- **核心创新 / 方法** · 让代理推断成为图生成内部组件。
- **Baseline** · 无群体标签常规公平生成。
- **Benchmark** · 图生成基准，公平和质量。
- **关键结果 / 消融** · 公平持续提高，质量具竞争力。
- **适用条件 / 局限** · 代理不能当真实群体身份；需审计错分。

**可复用机制** · 分别验证代理可靠性和它支持的公平边界。

<a id="paper-152666"></a>

## Towards Fairness under Label Bias in Image Segmentation: Impact, Measurement and Mitigation

[官方论文页](https://neurips.cc/virtual/2026/poster/152666) · [作者来源](https://openreview.net/forum?id=RIbRRjYome)

- **问题 / 瓶颈** · 盲去群体信息会删可用于纠偏的信号。
- **核心创新 / 方法** · 利用编码器的群体分离定位并缓解标签偏差。
- **Baseline** · 常规分割和不区分标注偏差。
- **Benchmark** · 三合成及现实偏差集。
- **关键结果 / 消融** · 无干净标签时仍检出并减缓差异。
- **适用条件 / 局限** · 依赖所验证偏差条件和群体数据权限。

**可复用机制** · 先识别标注机制，再决定去除或利用表示轴。

<a id="paper-153065"></a>

## Towards Financial World Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/153065) · [作者来源](https://openreview.net/forum?id=OEokq7iASc)

- **问题 / 瓶颈** · 潜结构可解释不保证改善核心预测。
- **核心创新 / 方法** · 比金融监督与 SSL 的任务指标和时间资产结构。
- **Baseline** · 监督量化模型。
- **Benchmark** · 价格变化、波动和交易成本。
- **关键结果 / 消融** · 监督预测仍领先，SSL 捕捉不同潜结构。
- **适用条件 / 局限** · 金融市场结果不等同于其他动力域。

**可复用机制** · 自监督预训练后同时验目标性能与潜因子覆盖。

<a id="paper-155195"></a>

## Towards Generalist Graph-Level Anomaly Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/155195) · [作者来源](https://openreview.net/forum?id=7ZuZgfPSG4)

- **问题 / 瓶颈** · 全局图表示携带数据集特有捷径。
- **核心创新 / 方法** · 以判别子图抽取和轻量选择器适配新域。
- **Baseline** · 现有图级异常方案。
- **Benchmark** · 多异质图异常基准。
- **关键结果 / 消融** · 摘要报告更好的泛化和样本效率。
- **适用条件 / 局限** · 依赖不同域共享局部异常模式。

**可复用机制** · 以结构可迁移性指导少样本图适配。

<a id="paper-152419"></a>

## Towards Generalizable 3D Anomaly Detection via Relational Inconsistency Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/152419) · [作者来源](https://openreview.net/forum?id=TGK0r4DOru)

- **问题 / 瓶颈** · 逐点外观误差受跨域偏移。
- **核心创新 / 方法** · 学习相邻结构的几何一致性。
- **Baseline** · 既有 3D 异常检测。
- **Benchmark** · Anomaly-ShapeNet、Real3D-AD，域内外。
- **关键结果 / 消融** · 两设置稳定改善。
- **适用条件 / 局限** · 正常邻域结构变化会使误报。

**可复用机制** · 将缺陷判断从单点移到可检查结构约束。

<a id="paper-155035"></a>

## Towards Generalizable Data Valuation: Learning an End-to-end Deep Model to Compute Shapley Values

[官方论文页](https://neurips.cc/virtual/2026/poster/155035) · [作者来源](https://openreview.net/forum?id=8vClXC5kYN)

- **问题 / 瓶颈** · 逐集全 Shapley 计算贵。
- **核心创新 / 方法** · 图结构预测，少量边际贡献补高保真。
- **Baseline** · 高预算排列 Shapley。
- **Benchmark** · 估值、删样本和加样本。
- **关键结果 / 消融** · 运行从小时降至秒且近真值。
- **适用条件 / 局限** · 迁移依赖任务和图近似。

**可复用机制** · 昂贵数据筛选先测代理在留出域是否能改善真实训练。

<a id="paper-151222"></a>

## Towards Generalizable Partially Relevant Video Retrieval

[官方论文页](https://neurips.cc/virtual/2026/poster/151222) · [作者来源](https://openreview.net/forum?id=c1UGpalx0Y)

- **问题 / 瓶颈** · 单集评估掩盖时段对齐过拟合。
- **核心创新 / 方法** · 保 CLIP 迁移的分支与目标片段匹配分支。
- **Baseline** · 现有 PRVR。
- **Benchmark** · 多源合训到未见目标的协议。
- **关键结果 / 消融** · 未见目标检索领先，幅度待核。
- **适用条件 / 局限** · 协议中的数据交叉与重复需审计。

**可复用机制** · 分开保通用对齐与任务特化，并用整库留出验。

<a id="paper-153552"></a>

## Towards High Semantic Fidelity: Hyperdimensional Symbolic Messages in Multi-Agent Communication

[官方论文页](https://neurips.cc/virtual/2026/poster/153552) · [作者来源](https://openreview.net/forum?id=KXTbANIGZW)

- **问题 / 瓶颈** · 黑盒向量或单通路会稀释关键信息。
- **核心创新 / 方法** · 超维符号消息配相似度双分支融合。
- **Baseline** · 常规模型通信。
- **Benchmark** · 多噪声情景，性能和结构可读性。
- **关键结果 / 消融** · 摘要称均保优势。
- **适用条件 / 局限** · 符号字典和噪声环境需要贴合。

**可复用机制** · 把消息解释性设独立验收，不以鲁棒平均替代。

<a id="paper-149609"></a>

## Towards Hyperparameter Transfer for Differentially Private Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/149609) · [作者来源](https://openreview.net/forum?id=opbIOcQ6tb)

- **问题 / 瓶颈** · 隐私噪声谱和低秩训练梯度不同，使标准 μP 失配。
- **核心创新 / 方法** · 给 DP-SGD、Adam、Muon 定谱缩放。
- **Baseline** · 标准 μP 和单模型调参。
- **Benchmark** · MLP、ViT、GPT-2，多宽度。
- **关键结果 / 消融** · 零样本传学习率可匹配或超过独调。
- **适用条件 / 局限** · 取决于噪声机制和裁剪。

**可复用机制** · 把隐私噪声作为独立缩放项。

<a id="paper-149628"></a>

## Towards Identifiable Latent Additive Noise Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149628) · [作者来源](https://openreview.net/forum?id=oeIa1kYSuD)

- **问题 / 瓶颈** · 严格全变化设定不现实。
- **核心创新 / 方法** · 约束函数族，允许机制变化子集。
- **Baseline** · 更严格因果表征模型。
- **Benchmark** · 合成、半合成与人类运动。
- **关键结果 / 消融** · 在弱条件证明可识别子结构。
- **适用条件 / 局限** · 部分识别不能推出完整图。

**可复用机制** · 用多任务变化识别能验证的机制，而非假设全部可识别。

<a id="paper-153509"></a>

## Towards Identifying Dominant Low-Rank Subspaces in Zeroth-Order Fine-Tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/153509) · [作者来源](https://openreview.net/forum?id=Ko8MeBmiba)

- **问题 / 瓶颈** · 全维或随机子空间方差大。
- **核心创新 / 方法** · 以平均历史梯度动态找主要低秩方向。
- **Baseline** · 随机子空间 ZO、全量一阶。
- **Benchmark** · 多 LLM 架构与下游。
- **关键结果 / 消融** · 优于所测零阶并接近一阶。
- **适用条件 / 局限** · 历史估计在任务突变时可能过时。

**可复用机制** · 内存受限时把扰动预算投向观察到的更新子空间。

<a id="paper-153285"></a>

## Towards instance-dependent regret optimality in Episodic MDPs with Posterior Sampling

[官方论文页](https://neurips.cc/virtual/2026/poster/153285) · [作者来源](https://openreview.net/forum?id=MPOsD4X94t)

- **问题 / 瓶颈** · 后验最优策略未必信息最优。
- **核心创新 / 方法** · 在探索回合使用固定参考策略，分开判是否需探。
- **Baseline** · 标准 PSRL。
- **Benchmark** · Episodic MDP 和实例依赖遗憾。
- **关键结果 / 消融** · 给参考策略所致对数探索成本。
- **适用条件 / 局限** · 依赖好参考与后验假设。

**可复用机制** · 策略部署用独立探索策略做信息采集可比对照。

<a id="paper-154109"></a>

## Toward Skill-Native LLMs: Skill Entropy for Benchmarking and Training Long-Horizon Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/154109) · [作者来源](https://openreview.net/forum?id=GC0mgKV3Ys)

- **问题 / 瓶颈** · 单技能评测不能推组合转移。
- **核心创新 / 方法** · Skill Entropy 量切换，构造跨技能任务。
- **Baseline** · 既有单技能榜和多前沿模型。
- **Benchmark** · Skill²-Bench，558 技能、九域，12 模型。
- **关键结果 / 消融** · 揭示跨技能结构困难，数值待核。
- **适用条件 / 局限** · 技能粒度影响难度刻画。

**可复用机制** · 训练课程按难转换边分配，而非只重复熟技能。

<a id="paper-152933"></a>

## Towards Matrix-Parallel and Feature-Scalable 3D Gaussian Splatting Rendering on GPUs

[官方论文页](https://neurips.cc/virtual/2026/poster/152933) · [作者来源](https://openreview.net/forum?id=PHnQZyfoZ1)

- **问题 / 瓶颈** · alpha 顺序依赖让 Tensor Core 利用差。
- **核心创新 / 方法** · tile 累积映射 warp 矩阵运算，打包压低可见不规则。
- **Baseline** · 标量 FMA 3DGS。
- **Benchmark** · 可扩展特征渲染及现代 GPU。
- **关键结果 / 消融** · 摘要给核心设计，增益数值待核。
- **适用条件 / 局限** · 依赖硬件形状、景物密度和通道规模。

**可复用机制** · 将不规则可见性通过打包转换为硬件可用矩阵块。

<a id="paper-155333"></a>

## Towards Mitigating Deceptive Safety Alignment in Large Reasoning Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155333) · [作者来源](https://openreview.net/forum?id=6PIauqxdE0)

- **问题 / 瓶颈** · 只测最终回答可能遗漏不一致。
- **核心创新 / 方法** · 用 DSAR 明确计量，并以 SARA 训练一致性。
- **Baseline** · 未使用一致性训练的大推理模型。
- **Benchmark** · 多个安全基准和提示条件，同时测效用。
- **关键结果 / 消融** · 摘要报告减少不一致并保留帮助性。
- **适用条件 / 局限** · 可见推理不是内部意图证明。

**可复用机制** · 把不同输出通道的安全表现分开验收，然后检查是否一致。

<a id="paper-149382"></a>

## Towards more general control of diffusion models using Jeffrey Guidance

[官方论文页](https://neurips.cc/virtual/2026/poster/149382) · [作者来源](https://openreview.net/forum?id=qUtuEEQhIU)

- **问题 / 瓶颈** · 传统引导往往只匹配一个属性目标，可能改动其他分布。
- **核心创新 / 方法** · 通过 Jeffrey 条件化更新指定嵌入分布。
- **Baseline** · 标准扩散引导。
- **Benchmark** · CIFAR-10、FFHQ、CelebA-HQ。
- **关键结果 / 消融** · 报告前两者 FID 大幅下降，也测试属性独立性。
- **适用条件 / 局限** · 依赖合适的目标表征与边缘分布。

**可复用机制** · 当需求是输出群体的比例或结构时，优先定义分布目标而非逐样本打分。

<a id="paper-151788"></a>

## Towards Multi-Human-Value Alignment via Value Localization in LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/151788) · [作者来源](https://openreview.net/forum?id=Y02g0k3yX4)

- **问题 / 瓶颈** · 把多个目标合并会隐藏不同价值共享或冲突。
- **核心创新 / 方法** · 用探针识别稀疏注意力头并做价值干预。
- **Baseline** · 整体对齐方法。
- **Benchmark** · 多模型的帮助、诚实、安全等表现。
- **关键结果 / 消融** · 报告价值头稀疏且灵活对齐改善。
- **适用条件 / 局限** · 探针发现需独立行为验证。

**可复用机制** · 分目标度量模型控制，不将某价值单项增益等同于整体变好。

<a id="paper-148687"></a>

## Towards On-Policy Data Evolution for Visual-Native Multimodal Deep Search Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/148687) · [作者来源](https://openreview.net/forum?id=vnIJBAvcbS)

- **问题 / 瓶颈** · 丢失中间视觉证据会重复检索或无法核对。
- **核心创新 / 方法** · 引入图像库引用协议，同时以代理反馈演化训练数据。
- **Baseline** · 静态生成训练资料与无中间复用。
- **Benchmark** · 多步视觉搜索和视觉局部细化。
- **关键结果 / 消融** · 摘要报告图像复用与动态数据均有收益。
- **适用条件 / 局限** · 依赖工具的地址与状态管理。

**可复用机制** · 持久化中间模态对象及其来源，让跨步骤视觉工具使用同一份证据。

<a id="paper-152676"></a>

## Towards Optimal Pre-training Data Mixtures for Empowering Reinforcement Learning in LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/152676) · [作者来源](https://openreview.net/forum?id=RFyOhPRUnL)

- **问题 / 瓶颈** · 基座普通指标未必预测强化学习后的表现。
- **核心创新 / 方法** · 通过小代理模型扫数据混合并以 k 条 RL 回答的困惑度引导优化。
- **Baseline** · 传统选择指标及其他混合。
- **Benchmark** · 1B、3B 模型及在线和离线 RL。
- **关键结果 / 消融** · 优化混合在所测算法中持续更优。
- **适用条件 / 局限** · 需要有代表性的 RL 轨迹，摘要未给规模外推。

**可复用机制** · 用与后训练分布对齐的代理评价匹配预训练数据，而不只测通用损失。

<a id="paper-154067"></a>

## Towards Optimism-Pessimism Trade-off in Model-based Offline-to-Online Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/154067) · [作者来源](https://openreview.net/forum?id=GPyvq8xYFz)

- **问题 / 瓶颈** · 单一离线策略无法同时稳住近分布和探索未见状态。
- **核心创新 / 方法** · 双目标训练策略池，部署按反馈选择。
- **Baseline** · 固定乐观或悲观策略。
- **Benchmark** · 离线到在线及变化任务的对照。
- **关键结果 / 消融** · 摘要报告域偏移明显时尤其受益。
- **适用条件 / 局限** · 需要线上反馈及有效候选覆盖。

**可复用机制** · 环境改变后先选可用策略，不必让所有风险偏好硬编码到一条策略。

<a id="paper-152071"></a>

## Towards Principled Efficient Rollout Allocation in Test-Time Training

[官方论文页](https://neurips.cc/virtual/2026/poster/152071) · [作者来源](https://openreview.net/forum?id=VhEkh5UxQR)

- **问题 / 瓶颈** · 固定采样将预算花在已很稳定的结论。
- **核心创新 / 方法** · 优势足够时从选举转确认，达到错误率门槛便停。
- **Baseline** · 固定预算多数。
- **Benchmark** · GPQA 等测试时训练。
- **关键结果 / 消融** · GPQA 节约超过 40% token，仍保持竞争性准确度。
- **适用条件 / 局限** · 后验误差依赖投票相关性和标定。

**可复用机制** · 在可量化重复结果的任务上，以停止时的不确定性决定是否再采样。

<a id="paper-155677"></a>

## Towards Principled Fine-Grained MoE Expert Pruning via Pseudo-Boolean Approximation

[官方论文页](https://neurips.cc/virtual/2026/poster/155677) · [作者来源](https://openreview.net/forum?id=3mjFgM0ciF)

- **问题 / 瓶颈** · 全组合搜索昂贵，独立排名无法看专家协同。
- **核心创新 / 方法** · 把专家保留写成伪布尔优化并对交互做近似。
- **Baseline** · 搜索和强分数基线。
- **Benchmark** · 7B 至 30B 的下游质量和效率。
- **关键结果 / 消融** · 摘要报告更好质量效率折中。
- **适用条件 / 局限** · 近似能否捕获高阶项和计算量未报告。

**可复用机制** · 压缩稀疏模型时先量化交互的重要性，再决定哪些专家应成组保留。

<a id="paper-149344"></a>

## Towards Realistic Conversational Multimodal Instruction Following

[官方论文页](https://neurips.cc/virtual/2026/poster/149344) · [作者来源](https://openreview.net/forum?id=qndRcwc5T4)

- **问题 / 瓶颈** · 最后回答准确不代表始终满足持久规则。
- **核心创新 / 方法** · 按跨模态上下文转移、持续指令等挑战测评并做细则训练。
- **Baseline** · 前沿模型及普通后训练。
- **Benchmark** · 多轮多模态指令遵循、六类挑战。
- **关键结果 / 消融** · 摘要报告前沿模型仍困难，细则训练改善约束且维持常规能力。
- **适用条件 / 局限** · 摘要未给每项约束的数据和结果口径。

**可复用机制** · 评测多轮工具助手时，记录每个约束何时建立、修改或应持续。

<a id="paper-152397"></a>

## Towards Real-Time Full-Waveform LiDAR Transformers via Intensity-Guided Token Reduction and Physics-Aware Augmentation

[官方论文页](https://neurips.cc/virtual/2026/poster/152397) · [作者来源](https://openreview.net/forum?id=TOfHGk54P0)

- **问题 / 瓶颈** · 低强度背景冗余造成实时计算过重。
- **核心创新 / 方法** · 用强度驱动裁剪，并单独设计与物理一致的增强。
- **Baseline** · 标准全波形 Transformer。
- **Benchmark** · 标准与分布外环境的全波形检测。
- **关键结果 / 消融** · 摘要报告减少冗余且改善精度，增强进一步提升泛化。
- **适用条件 / 局限** · 弱目标与背景可能重叠，摘要未给召回代价。

**可复用机制** · 传感器模型可在输入前按可信物理量做动态筛选，同时验证低信号目标。

<a id="paper-138935"></a>

## Towards Real-world Human Behavior Simulation: Benchmarking Large Language Models on Long-horizon, Cross-scenario, Heterogeneous Behavior Traces

[官方论文页](https://neurips.cc/virtual/2026/poster/138935) · [作者来源](https://openreview.net/forum?id=vRhFNoAPNv)

- **问题 / 瓶颈** · 单场景数据不能体现先前行为对后续选择的影响。
- **核心创新 / 方法** · 对齐长期异质行为轨迹，检查模型对个人差异的维持。
- **Baseline** · 孤立场景数据与先进 LLM。
- **Benchmark** · 跨情境、人类长期行为模拟。
- **关键结果 / 消融** · 观察到人物同质化与理想化偏差。
- **适用条件 / 局限** · 摘要未列数据覆盖差异。

**可复用机制** · 模拟长期角色时条件保持历史并与少见行为分布对照。

<a id="paper-149360"></a>

## Towards Reconstructing Geographically Diverse Architecture with 3D Foundation Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149360) · [作者来源](https://openreview.net/forum?id=qbpVyvprTf)

- **问题 / 瓶颈** · 地理表现差异可能被场景大小混淆。
- **核心创新 / 方法** · 量化地区与尺度的关系，并按诊断干预。
- **Baseline** · 原三维基础模型。
- **Benchmark** · 多地区建筑重建。
- **关键结果 / 消融** · 摘要报告尺度是主要混淆，干预改善总体与差距。
- **适用条件 / 局限** · 限建筑任务，摘要未给偏差分解量。

**可复用机制** · 报告分群差异时先平衡基础难度，再判断应适配哪个变量。

<a id="paper-149895"></a>

## Towards Reliable LLM Evaluation: Correcting the Winner’s Curse in Adaptive Benchmarking

[官方论文页](https://neurips.cc/virtual/2026/poster/149895) · [作者来源](https://openreview.net/forum?id=mQqvzWsweC)

- **问题 / 瓶颈** · 最大化测试分数会导致赢家乐观偏差。
- **核心创新 / 方法** · 用 SIREN 在拆分选择和评估后，对项目误差做 bootstrap。
- **Baseline** · 在同数据选择赢家直接报告。
- **Benchmark** · 受控模拟及 MMLU-Pro。
- **关键结果 / 消融** · 摘要报告赢家报告会改变部署判断，SIREN 接近有限样本目标。
- **适用条件 / 局限** · 理论限稳定选择与固定短名单。

**可复用机制** · 调参使用的基准可以筛选，但所选方案仍需留出数据来报告可比效果。

<a id="paper-139432"></a>

## Towards Reliable VLM Judges: State-Conditional Invariance and Presentation-Aware Diagnostics

[官方论文页](https://neurips.cc/virtual/2026/poster/139432) · [作者来源](https://openreview.net/forum?id=R0PFXXlrTV)

- **问题 / 瓶颈** · 一致性高可能源于无视真正相关证据。
- **核心创新 / 方法** · 以模拟器生成配对完整、证据删除、反事实和呈现变量。
- **Baseline** · 普通总体精度或一致性评价。
- **Benchmark** · GridWM-Judge、五类 MiniGrid 诊断。
- **关键结果 / 消融** · 摘要指出三个维度需联合报告。
- **适用条件 / 局限** · 确定性模拟评审限所测视觉证据。

**可复用机制** · 在评价模型上改变输入时明确哪些变化应改评分、哪些不应改。

<a id="paper-150922"></a>

## Towards Scalable Data Diversification for Language Model Pretraining via Leverage Score Sampling

[官方论文页](https://neurips.cc/virtual/2026/poster/150922) · [作者来源](https://openreview.net/forum?id=eNBJGhDB8u)

- **问题 / 瓶颈** · 覆盖启发式可能不保留特征谱，重复更新协方差昂贵。
- **核心创新 / 方法** · 用迭代杠杆分数采样。
- **Baseline** · 按覆盖或质量筛选。
- **Benchmark** · 语言模型预训练的下游任务，含代码。
- **关键结果 / 消融** · 摘要报告所选数据取得更好代码表现。
- **适用条件 / 局限** · 受所选特征和采样预算影响。

**可复用机制** · 训练集清洗同时测数据谱多样性和局部质量，避免把稀有有用样本全部清除。

<a id="paper-156087"></a>

## Towards Scalable Egocentric HOI for Humanoids: Benchmarking Whole-Body Dexterous Interaction with Tactile Prediction

[官方论文页](https://neurips.cc/virtual/2026/poster/156087) · [作者来源](https://openreview.net/forum?id=0UDyFy4rIa)

- **问题 / 瓶颈** · 视觉轨迹可能不符合真实物理接触。
- **核心创新 / 方法** · 以实测触觉约束人形交互重建。
- **Baseline** · 不使用接触优化的重建。
- **Benchmark** · 第一视角 RGB-D 的长程全身接触及恢复。
- **关键结果 / 消融** · 摘要展示接触感知基准和更物理的数据生成方法。
- **适用条件 / 局限** · 依赖触觉和视觉标定，摘要未给压力代价。

**可复用机制** · 合成或重定向全身示范时，应对接触部位额外施加真实信号约束。

<a id="paper-152627"></a>

## Towards Understanding Momentum Acceleration in River-Valley Loss Landscape

[官方论文页](https://neurips.cc/virtual/2026/poster/152627) · [作者来源](https://openreview.net/forum?id=RhiQnfDg2m)

- **问题 / 瓶颈** · 损失峡谷中的尖锐方向约束可用步长
- **核心创新 / 方法** · 区分沿低损失流形的进度和横向震荡，对照有无动量
- **Baseline** · 原始梯度下降
- **Benchmark** · 合成函数与语言模型训练
- **关键结果 / 消融** · 摘要称动量允许用较大学习率并抑制横向震荡
- **适用条件 / 局限** · 结论依赖峡谷结构以及步长范围

**可复用机制** · 记录模型的震荡和收敛速度后再增大动量

<a id="paper-151883"></a>

## Towards Understanding Self-Pretraining for Sequence Classification

[官方论文页](https://neurips.cc/virtual/2026/poster/151883) · [作者来源](https://openreview.net/forum?id=XC2lHn0w5A)

- **问题 / 瓶颈** · 类别标签可能无法学习部分注意力方向
- **核心创新 / 方法** · 用同一数据掩码重建促使绝对位置成为近邻偏置
- **Baseline** · 随机初始化后直接监督
- **Benchmark** · 序列分类、Long-Range Arena 相关设置
- **关键结果 / 消融** · 证据支持近邻交互的重要性，数字未报告
- **适用条件 / 局限** · 任务近邻模式强弱影响有效性

**可复用机制** · 有少量序列标注时验证预训练是否学会标签无法直接约束的关系

<a id="paper-155813"></a>

## Towards Understanding the Power and Limits of the Muon Optimizer: A River-Valley Perspective

[官方论文页](https://neurips.cc/virtual/2026/poster/155813) · [作者来源](https://openreview.net/forum?id=2hczCV54xy)

- **问题 / 瓶颈** · 增大更新有利初期找方向，却可能在近目标震荡
- **核心创新 / 方法** · 用混合尖峰感知模型分析优化轨迹，并尝试后期换梯度类方法
- **Baseline** · Adam/AdamW 与从头到尾的 Muon
- **Benchmark** · 矩阵感知和初步语言模型训练
- **关键结果 / 消融** · 摘要报告后段边界现象及两阶段初步证据
- **适用条件 / 局限** · 语言模型证据初步，切换时点未普遍验证

**可复用机制** · 比较尾段换优化器与单纯降学习率

<a id="paper-153958"></a>

## TPRL: Adaptive Visual Token Pruning in LVLMs via Language-Guided Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/153958) · [作者来源](https://openreview.net/forum?id=HGL8gQMjLg)

- **问题 / 瓶颈** · 各次剪枝相互影响，固定打分忽略终局
- **核心创新 / 方法** · 以语言条件及准确和计算奖励，用示范初始化后做 PPO
- **Baseline** · 手工打分及一次性剪枝
- **Benchmark** · 大视觉语言模型的准确率、token 和 FLOPs
- **关键结果 / 消融** · 最高去 66.7% token、少 54.2% FLOPs，平均精度降 0.7%
- **适用条件 / 局限** · FLOPs 与实际硬件延迟不同，剪枝可能损失稀有证据

**可复用机制** · 部署时同时验收多步预算、时延与失败样本

<a id="paper-139211"></a>

## TraceML: An Empirical Analysis of Human-Agent Planning in Machine Learning Development

[官方论文页](https://neurips.cc/virtual/2026/poster/139211) · [作者来源](https://openreview.net/forum?id=eL7smcZz4v)

- **问题 / 瓶颈** · 终局成绩看不出实验组织是否高效
- **核心创新 / 方法** · 对照专家和智能体逐步规划，并用诊断设计计划工作流
- **Baseline** · 人类专家、原编码智能体
- **Benchmark** · 134 MLE-bench 比赛、4672 个 Kaggle 轨迹
- **关键结果 / 消融** · 局部编辑较好，探索、实验排序和归因较弱；新流程改善表现
- **适用条件 / 局限** · 竞赛特性未必代表生产研究，摘要未列收益数字

**可复用机制** · 给研究助手单列实验顺序及保存和复用结果的回归

<a id="paper-153884"></a>

## TRACER: Verifiable Generative Provenance for Multimodal Tool-Using Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/153884) · [作者来源](https://openreview.net/forum?id=I2bqIi1pI6)

- **问题 / 瓶颈** · 工具调用多可能混入冗余或无依据推断
- **核心创新 / 方法** · 以可验证观测到主张依赖训练工具使用与摘要
- **Baseline** · 只优化工具的 SFT、最强闭源工具增强基线
- **Benchmark** · 多模态工具问答、摘要和总工具次数
- **关键结果 / 消融** · 答案 78.23%，摘要 95.72%，调用 4949 至 3486
- **适用条件 / 局限** · 观察与主张可归因性依赖任务规范

**可复用机制** · 用引用覆盖及实际工具预算同时验收 Agent

<a id="paper-139280"></a>

## TRACE: Tourism Recommendation with Accountable Citation Evidence

[官方论文页](https://neurips.cc/virtual/2026/poster/139280) · [作者来源](https://openreview.net/forum?id=ZmCqSnVZ8k)

- **问题 / 瓶颈** · 只测实体召回忽略可核理由和修正。
- **核心创新 / 方法** · 将旅游属性偏好与逐字评论证据和回退场景配对。
- **Baseline** · Recall@k。
- **Benchmark** · TRACE，多轮地点推荐。
- **关键结果 / 消融** · 提出可验证切片，分数未核。
- **适用条件 / 局限** · 证据质量与覆盖影响结果。

**可复用机制** · 以用户拒绝后实际改推荐验证对话适应。

<a id="paper-155184"></a>

## TRACE: Trajectory-Aware Conceps for Explainable Video Understanding

[官方论文页](https://neurips.cc/virtual/2026/poster/155184) · [作者来源](https://openreview.net/forum?id=7fOVVa6o6F)

- **问题 / 瓶颈** · 说运动重要仍未揭示来源。
- **核心创新 / 方法** · 加入轨迹级可解释监督与忠实评估。
- **Baseline** · 黑盒视频模型。
- **Benchmark** · 六基准，行为识别和 VQA。
- **关键结果 / 消融** · 仅平均落后 0.9 点和 0.1 点。
- **适用条件 / 局限** · 轨迹质量影响解释。

**可复用机制** · 要求解释可关联实际移动实体和时间。

<a id="paper-139848"></a>

## TraceTriage: A Benchmark for Cost-Aware Stop-or-Continue Decisions in Delayed-Outcome Workflows

[官方论文页](https://neurips.cc/virtual/2026/poster/139848) · [作者来源](https://openreview.net/forum?id=0nT73ZOEvC)

- **问题 / 瓶颈** · 终局成功率无法决定当前是否继续。
- **核心创新 / 方法** · 只用检查点证据，阈值在验证集定。
- **Baseline** · 普通终局预测比较。
- **Benchmark** · TraceTriage，长时间工作流。
- **关键结果 / 消融** · 提供成本感知验收，幅度未核。
- **适用条件 / 局限** · 成本口径须匹配部署。

**可复用机制** · 将提前停止纳入独立决策评估。

<a id="paper-152706"></a>

## Tracing Actual Causes with Counterfactual Witness Maps

[官方论文页](https://neurips.cc/virtual/2026/poster/152706) · [作者来源](https://openreview.net/forum?id=R0MXum0YPw)

- **问题 / 瓶颈** · 只找到一个原因不足以分责。
- **核心创新 / 方法** · 枚举反事实见证图以找带条件的原因。
- **Baseline** · 单原因查找。
- **Benchmark** · 随机布尔结构因果，至 15 节点。
- **关键结果 / 消融** · 证明完备且可执行于测试规模。
- **适用条件 / 局限** · 规模与因果模型准确性限制。

**可复用机制** · 分析小流程故障显式区分必要条件与候选共同原因。

<a id="paper-151046"></a>

## Tracing Agentic Failure from the Flow of Success

[官方论文页](https://neurips.cc/virtual/2026/poster/151046) · [作者来源](https://openreview.net/forum?id=dPFKov09YE)

- **问题 / 瓶颈** · LLM 逐步点评成本高。
- **核心创新 / 方法** · 以神经受控微分方程拟合成功潜轨迹。
- **Baseline** · 提示式检测。
- **Benchmark** · 100 成功轨迹，域内及域外。
- **关键结果 / 消融** · 快 200 至 5000 倍，F1 分别增 20% 和 7%。
- **适用条件 / 局限** · 少数成功模式未覆盖会误判。

**可复用机制** · 以廉价正常轨迹模型定位需人工复核步骤。

<a id="paper-152002"></a>

## TracingFlow: A Simulation-Free Trajectory Inference Framework Based on Second-Order Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/152002) · [作者来源](https://openreview.net/forum?id=WETDhvImnp)

- **问题 / 瓶颈** · 直接一阶迁移可能失真。
- **核心创新 / 方法** · 将免模拟匹配推广至二阶动力学。
- **Baseline** · 既有轨迹扩散或流方法。
- **Benchmark** · 复杂合成及单细胞轨迹。
- **关键结果 / 消融** · 摘要称分布和轨迹保真改善。
- **适用条件 / 局限** · 真实潜轨迹未直接观测。

**可复用机制** · 对速度随时间演化的系统比较一阶与二阶归纳偏置。

<a id="paper-155125"></a>

## Tracing Moral Foundations in Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155125) · [作者来源](https://openreview.net/forum?id=8EzndxNzWA)

- **问题 / 瓶颈** · 聚合判断会掩盖选择性改变。
- **核心创新 / 方法** · 比较预训练及后训练并查稠密和稀疏特征。
- **Baseline** · 人类判断与不同训练阶段。
- **Benchmark** · 道德维度的行为和表征。
- **关键结果 / 消融** · 表示在预训练出现，后训练选择性重排。
- **适用条件 / 局限** · 依赖采用的道德框架和人群。

**可复用机制** · 多价值对齐逐维验证而不是用一个总方向。

<a id="paper-149072"></a>

## Tracing Persona Vectors Through LLM Pretraining

[官方论文页](https://neurips.cc/virtual/2026/poster/149072) · [作者来源](https://openreview.net/forum?id=t52l7mvYeE)

- **问题 / 瓶颈** · 只看成品无法区分倾向何时出现。
- **核心创新 / 方法** · 用不同引导方式比较线性角色方向。
- **Baseline** · 不同 elicitation 和模型阶段。
- **Benchmark** · LLM 预训练轨迹。
- **关键结果 / 消融** · 早期存在稳定角色表示，不同方法显露不同面。
- **适用条件 / 局限** · 线性方向不等于角色完整表示。

**可复用机制** · 从训练轨迹找异常倾向开始形成的时期。

<a id="paper-148824"></a>

## Tracing Psychometric Inference in Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148824) · [作者来源](https://openreview.net/forum?id=urjQ6t9arH)

- **问题 / 瓶颈** · 表征变化和读出变化可能混同。
- **核心创新 / 方法** · 配对激活探针，扣除合成脊回归基线。
- **Baseline** · 行为指标及合成控制。
- **Benchmark** · 心理构念放大差异。
- **关键结果 / 消融** · 校正后对行为预测相关 r=0.88。
- **适用条件 / 局限** · 选构念和标注影响解释。

**可复用机制** · 诊断代理偏差时分离内部编码强度和输出读法。

<a id="paper-139645"></a>

## Tracing the Cascade: A Topology-Aware Evaluation Framework for Scientific Agent Hallucinations

[官方论文页](https://neurips.cc/virtual/2026/poster/139645) · [作者来源](https://openreview.net/forum?id=DZxHV6tNsz)

- **问题 / 瓶颈** · 最终正确可掩盖过程错误。
- **核心创新 / 方法** · 定位高连接知识节点及证据链校验。
- **Baseline** · 只看最终答案。
- **Benchmark** · 两生物医学子域、11 LLM 代理，含多跳和验证。
- **关键结果 / 消融** · 错误集中少数 hub，终局与过程分离。
- **适用条件 / 局限** · 迁移需新证据图，摘要未给通用界。

**可复用机制** · 优先验证供多个下游步骤依赖的证据。

<a id="paper-155695"></a>

## Track4D: Representing Dense 3D Tracking for Video Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155695) · [作者来源](https://openreview.net/forum?id=3d21Z6gJLQ)

- **问题 / 瓶颈** · 现有追踪难转移视频生成先验。
- **核心创新 / 方法** · 少量合成数据和 LoRA 将预训练视频模型条件化。
- **Baseline** · 现有 3D 跟踪。
- **Benchmark** · 五个零样本跟踪基准。
- **关键结果 / 消融** · 表现具竞争力。
- **适用条件 / 局限** · 坐标输出兼容性须验证，真实难例待测。

**可复用机制** · 先寻找能由生成主干表达的运动编码。

<a id="paper-155634"></a>

## TrackCraft3R: Repurposing Video Diffusion Transformers for Dense 3D Tracking

[官方论文页](https://neurips.cc/virtual/2026/poster/155634) · [作者来源](https://openreview.net/forum?id=46qtUc033H)

- **问题 / 瓶颈** · 现有 3D 跟踪在长时遮挡和大动作时更难。
- **核心创新 / 方法** · 复用视频扩散 Transformer 表征。
- **Baseline** · 既有密集 3D 跟踪。
- **Benchmark** · 长视频和大移动。
- **关键结果 / 消融** · 摘要报告稳健，确数待核。
- **适用条件 / 局限** · 预训练覆盖和输出成本影响可用性。

**可复用机制** · 用时间跨度分层验生成表征可否做跟踪代用。

<a id="paper-152726"></a>

## TrackFish3D: Self-Supervised 3D Tracking of Schooling Fish from Multi-view Videos

[官方论文页](https://neurips.cc/virtual/2026/poster/152726) · [作者来源](https://openreview.net/forum?id=QoMSgn3Pyt)

- **问题 / 瓶颈** · 相似外观难跨视角和遮挡保持身份。
- **核心创新 / 方法** · 自监督分离共可见对象，以运动预测过短遮挡。
- **Baseline** · 现有最强多对象跟踪。
- **Benchmark** · 多视角鱼与鸟轨迹，3D MOTA。
- **关键结果 / 消融** · 鱼 MOTA 83.7% 至 96.6%，可迁到鸟。
- **适用条件 / 局限** · 依赖足量多视角及可见轨迹。

**可复用机制** · 用共存排斥约束学身份，不依赖跨视角人工标签。

<a id="paper-150674"></a>

## TrackTok: Object-Centric Video Tokenization with Semantically Persistent Tokens

[官方论文页](https://neurips.cc/virtual/2026/poster/150674) · [作者来源](https://openreview.net/forum?id=gLXvwn6vSP)

- **问题 / 瓶颈** · 固定网格在时间上不断换语义。
- **核心创新 / 方法** · 用对象对齐 token 跨运动、形变、遮挡保身份。
- **Baseline** · 普通时空 tokenizer。
- **Benchmark** · 视频生成质量和样本吞吐。
- **关键结果 / 消融** · 最高约十倍吞吐。
- **适用条件 / 局限** · 漏小对象和深遮挡需测试。

**可复用机制** · 让 token 组织与交互对象一致而非固定像素坐标。

<a id="paper-154691"></a>

## TrAction: Action Recognition with Sparse Trajectories

[官方论文页](https://neurips.cc/virtual/2026/poster/154691) · [作者来源](https://openreview.net/forum?id=BiWI5m66G8)

- **问题 / 瓶颈** · 外观特征无法完整表达运动。
- **核心创新 / 方法** · 2.5D 轨迹 Transformer 做掩码预训练并和视觉特征融合。
- **Baseline** · DINOv2、V-JEPA 2。
- **Benchmark** · Something-Something V2，Top-1。
- **关键结果 / 消融** · 分别加 8.7 与 1.6 点。
- **适用条件 / 局限** · 受轨迹估计与任务运动显著性限制。

**可复用机制** · 先测试新增轨迹是否和强视频基座互补。

<a id="paper-155761"></a>

## Trading Sensing for Structure: Sparse IMU-EMG Fingertip Force Estimation via Neuro-inspired Structured Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/155761) · [作者来源](https://openreview.net/forum?id=37ByakECcQ)

- **问题 / 瓶颈** · 通用模型低数据且传感缺失时脆弱。
- **核心创新 / 方法** · 神经启发结构整合少量 IMU、EMG。
- **Baseline** · 密集传感和通用模型。
- **Benchmark** · 多用户多物体指尖力估计。
- **关键结果 / 消融** · 接近密集参考且参数更少。
- **适用条件 / 局限** · 人体个体变化和设备放置需校准。

**可复用机制** · 用可验证生理或动力关系补传感，而非盲增容量。

<a id="paper-139842"></a>

## Traffic STGNNs across Sensor, City, and Time Shifts: Routing Concentration Tracks Sensitivity to Sensor Dropout

[官方论文页](https://neurips.cc/virtual/2026/poster/139842) · [作者来源](https://openreview.net/forum?id=1DWmoUiM00)

- **问题 / 瓶颈** · 自适应图不一定比固定图更脆弱。
- **核心创新 / 方法** · 冻结比较地点、传感及时间转移。
- **Baseline** · 八 STGNN。
- **Benchmark** · 城市迁移、传感掉线、周内变化。
- **关键结果 / 消融** · 掉线跟随路由集中，跨城和时间排序不同。
- **适用条件 / 局限** · 目标图未提供的公平协议限定结论。

**可复用机制** · 不要用一种故障的排名代替所有域移。

<a id="paper-154615"></a>

## Trainable Sparse Attention via Hybrid Top-k+Top-p Masking and Distillation Fine-Tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/154615) · [作者来源](https://openreview.net/forum?id=CHKbRr1YwB)

- **问题 / 瓶颈** · 单 top-k 或 top-p 在不同分布不稳。
- **核心创新 / 方法** · 混合掩码并蒸馏微调。
- **Baseline** · 现有稀疏注意。
- **Benchmark** · 视频扩散的生成质量及稀疏速度。
- **关键结果 / 消融** · 95% 稀疏和 16.2 倍注意力加速。
- **适用条件 / 局限** · 注意力部件速度非整体吞吐。

**可复用机制** · 用预算和质量阈共同控制稀疏程度，再测实用耗时。

<a id="paper-150633"></a>

## Trainable Topology Supervision under Structurally Unreliable Pseudo Supervision

[官方论文页](https://neurips.cc/virtual/2026/poster/150633) · [作者来源](https://openreview.net/forum?id=ge0NKL4C5c)

- **问题 / 瓶颈** · 伪标签结构错误会干扰学习。
- **核心创新 / 方法** · 以软 Euler 轨迹和阈值变化替代条码，保守门控。
- **Baseline** · 同载体对照。
- **Benchmark** · 无监督伪装目标检测。
- **关键结果 / 消融** · 检测和结构可靠性一致改善。
- **适用条件 / 局限** · 简化拓扑代理可能漏高阶异常。

**可复用机制** · 按标签质量选择是否以及多强地加拓扑损失。

<a id="paper-149668"></a>

## Train at the Moving Edge: Rollout-Efficient RL for Large Reasoning Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149668) · [作者来源](https://openreview.net/forum?id=oLEiPvaZRf)

- **问题 / 瓶颈** · 有用样本随训练状态变化。
- **核心创新 / 方法** · 以历史排序加在线验证追踪学习边界。
- **Baseline** · 静态和统一 rollout。
- **Benchmark** · 推理 RL 的提示及训练效率。
- **关键结果 / 消融** · 观察到效用集中移动的难度熵交集。
- **适用条件 / 局限** · 熵高可能来自噪声，在线验证必需。

**可复用机制** · 课程同时追踪能力及输出多样性。

<a id="paper-154824"></a>

## Training Agent to Scale Inference-Time Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/154824) · [作者来源](https://openreview.net/forum?id=AgveNA7n1G)

- **问题 / 瓶颈** · 独立轨迹奖励无法训练相对排名与置信聚合。
- **核心创新 / 方法** · AutoPortfolio 在采样集合上优化排序。
- **Baseline** · 强代理强化学习。
- **Benchmark** · 12 项推理基准。
- **关键结果 / 消融** · 大候选池改善尤其明显。
- **适用条件 / 局限** · 摘要未给候选相关性边界。

**可复用机制** · 采样数扩大时，把候选集合质量和实际选择器质量分别优化。

<a id="paper-155056"></a>

## Training a Predictive Coding Network on ImageNet using Equilibrium Propagation

[官方论文页](https://neurips.cc/virtual/2026/poster/155056) · [作者来源](https://openreview.net/forum?id=8nLDF6mZEp)

- **问题 / 瓶颈** · 现有训练过程常难扩展至大图像任务。
- **核心创新 / 方法** · 结合中心式平衡传播和新的平衡方案。
- **Baseline** · 原预测编码与平衡传播。
- **Benchmark** · ImageNet。
- **关键结果 / 消融** · 报告可训练到 ImageNet 规模。
- **适用条件 / 局限** · 摘要未给同算力优势。

**可复用机制** · 规模限制可能来自状态求解而非模型类别，应分别验证。

<a id="paper-152100"></a>

## Training-Based Backdoors Are Not Cryptographic

[官方论文页](https://neurips.cc/virtual/2026/poster/152100) · [作者来源](https://openreview.net/forum?id=VX0VrTjuLs)

- **问题 / 瓶颈** · 有效后门未必构成理论上不可检测的行为。
- **核心创新 / 方法** · 在受限模型类分析训练产生的后门并检验可观测性。
- **Baseline** · 不同训练后门配置。
- **Benchmark** · 预训练大语言模型实证。
- **关键结果 / 消融** · 所测配置无同时有效且不可恢复者。
- **适用条件 / 局限** · 结论限理论模型类及实测配置。

**可复用机制** · 防御可以测识别性边界，无需黑盒宣称防护根本不可能。

<a id="paper-153796"></a>

## Training Data Attribution in Diffusion Models via Mirrored Unlearning and Noise-Consistent Skew

[官方论文页](https://neurips.cc/virtual/2026/poster/153796) · [作者来源](https://openreview.net/forum?id=Id0XHHT9w8)

- **问题 / 瓶颈** · 分别采样噪声可能干扰损失差值。
- **核心创新 / 方法** · 对镜像去学习后的模型和原模型计算归一化损失差。
- **Baseline** · 其他训练数据归因。
- **Benchmark** · 扩散生成归因与样本组合。
- **关键结果 / 消融** · 摘要报告一致优于其他方法。
- **适用条件 / 局限** · 第二模型训练成本未报告。

**可复用机制** · 在比较随机损失时控制噪声源，再解释样本贡献。

<a id="paper-155047"></a>

## Training Deliberative Monitors for Black-Box Scheming Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/155047) · [作者来源](https://openreview.net/forum?id=8r0rIgoH3E)

- **问题 / 瓶颈** · 部署中未必访问被监控模型内部推理。
- **核心创新 / 方法** · 用明确规则和教师的结构化标注训练监控器。
- **Baseline** · 提示式前沿模型监控。
- **Benchmark** · 行为轨迹检测，低误报和成本折中。
- **关键结果 / 消融** · 部分监控器位于经验 Pareto 前沿。
- **适用条件 / 局限** · 依赖教师标注及可观察行为。

**可复用机制** · 监控资源有限时比较固定低误报下的检测收益与运行成本。

<a id="paper-149653"></a>

## Training for the Model You Return: Improving Optimization for Iterate-Averaged Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149653) · [作者来源](https://openreview.net/forum?id=oTGwUj4oE3)

- **问题 / 瓶颈** · 普通 AdamW 优化瞬时参数而非最终使用的平均模型。
- **核心创新 / 方法** · 控制模型推导迭代更新的轻量包装 PACE。
- **Baseline** · AdamW、EMA、学习率衰减及 Schedule-Free。
- **Benchmark** · 1 至 2B 微调、FineWeb GPT-2 预训。
- **关键结果 / 消融** · 优于普通 AdamW 及 EMA 测试形式。
- **适用条件 / 局限** · 控制理论基于局部随机二次模型。

**可复用机制** · 当返回的是平均参数，应将平均应用写入更新优化目标。

<a id="paper-155326"></a>

## Training-Free 3D Editing via Feature-Divergence Localization and Trajectory Correction

[官方论文页](https://neurips.cc/virtual/2026/poster/155326) · [作者来源](https://openreview.net/forum?id=6StcC3knUL)

- **问题 / 瓶颈** · 全时段相同引导会漏编辑或污染周边。
- **核心创新 / 方法** · 按粗结构生成时机做轨迹局部校正。
- **Baseline** · 已有免训练三维编辑。
- **Benchmark** · 三维编辑局部性和目标效果。
- **关键结果 / 消融** · 摘要报告更稳定局部控制。
- **适用条件 / 局限** · 摘要未给通用阶段阈值。

**可复用机制** · 编辑任务可按生成时序分配约束，别全程用相同空间引导。

<a id="paper-153883"></a>

## Training-Free Active Test-Time Adaptation for Vision-Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153883) · [作者来源](https://openreview.net/forum?id=I3ciV94sTt)

- **问题 / 瓶颈** · 全无标签与先查当前答案之间缺少现实预算模型。
- **核心创新 / 方法** · 选择部分样本核对，并让模型在取得当前标签前先预测。
- **Baseline** · 强 VLM 测试适配。
- **Benchmark** · 十个跨域和 ImageNet 转移，含 ResNet 与 ViT。
- **关键结果 / 消融** · 报告稳定提升且附加开销小。
- **适用条件 / 局限** · 依赖人工预算和样本到达分布。

**可复用机制** · 适配评测应按时间区分可用的已有标签与当前预测后才得到的标签。

<a id="paper-151840"></a>

## Training-Free Cultural Alignment of Large Language Models via Persona Disagreement

[官方论文页](https://neurips.cc/virtual/2026/poster/151840) · [作者来源](https://openreview.net/forum?id=XXjm56G5Q3)

- **问题 / 瓶颈** · 冻结 API 难用参数训练补足文化差异。
- **核心创新 / 方法** · 多角色比较为生成提供文化条件信号。
- **Baseline** · 原始 70B 等模型。
- **Benchmark** · MultiTP，二元困境和开放场景。
- **关键结果 / 消融** · 不对齐下降分别 10% 至 24% 和 2% 至 7%。
- **适用条件 / 局限** · 依赖角色描述准确，不代表真实群体内部差异。

**可复用机制** · 跨文化助手可将分歧显式纳入决策，并按目标场景检验。

<a id="paper-154583"></a>

## Training-free Focus-Ambient Retention for Memory-Efficient Video Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154583) · [作者来源](https://openreview.net/forum?id=CVfZbrvMBG)

- **问题 / 瓶颈** · 固定逐帧裁剪可能删关键小目标并重复存背景。
- **核心创新 / 方法** · 融合注意力和频率等信号筛焦点，对背景按历史变化保留。
- **Baseline** · 逐帧或分块压缩。
- **Benchmark** · 视频语言评测及固定上下文预算。
- **关键结果 / 消融** · 摘要报告更好质量显存折中。
- **适用条件 / 局限** · 依赖缓存准确判断背景变化。

**可复用机制** · 处理长视频可给瞬时证据和慢变化场景分开分配记忆。

<a id="paper-149104"></a>

## Training-Free Generative Sampling via Moment-Matched Score Smoothing

[官方论文页](https://neurips.cc/virtual/2026/poster/149104) · [作者来源](https://openreview.net/forum?id=sro3uicxll)

- **问题 / 瓶颈** · 只靠基础分数可能不保持先验统计量。
- **核心创新 / 方法** · 以矩匹配平滑分数和 Langevin 粒子交互采样。
- **Baseline** · 神经扩散基线。
- **Benchmark** · 二维分布和图像潜空间，比较保真与多样性。
- **关键结果 / 消融** · 作者报告在 CPU 上免训练且有竞争力。
- **适用条件 / 局限** · 依赖所给矩代表目标。

**可复用机制** · 训练不可行且知道部分统计时，可先试样本级约束而非新增模型参数。

<a id="paper-153266"></a>

## Training-Free Open World Object Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/153266) · [作者来源](https://openreview.net/forum?id=MXj7wF9civ)

- **问题 / 瓶颈** · 开词表检测器的零样本能力不足以识别未知物体。
- **核心创新 / 方法** · 从前向结果收集类别外观与属性统计并聚类。
- **Baseline** · OW-OVD 和零样本 VLOD。
- **Benchmark** · M-OWODB 增量任务。
- **关键结果 / 消融** · 已知类 mAP 增 16.2，平均未知召回增 28.0。
- **适用条件 / 局限** · 依赖属性可用及类别聚类质量。

**可复用机制** · 开放集适配可使用额外属性结构刻画未知，而不改冻结编码器。

<a id="paper-154724"></a>

## Training-Free Task Vectors for LLM Behavioral Control

[官方论文页](https://neurips.cc/virtual/2026/poster/154724) · [作者来源](https://openreview.net/forum?id=BTg4Q4wn1V)

- **问题 / 瓶颈** · 任务向量通常要额外微调。
- **核心创新 / 方法** · 把目标激活映射为秩一权重改动。
- **Baseline** · 微调任务向量和行为控制方案。
- **Benchmark** · 特性控制和原有任务效用。
- **关键结果 / 消融** · 摘要报告保持效用且控制有竞争力。
- **适用条件 / 局限** · 依赖方向准确性与任务范围。

**可复用机制** · 需要小型可组合编辑时，测试把已知的激活效应转移到参数空间。

<a id="paper-151685"></a>

## Training Generalizable Collaborative Agents via Strategic Risk Aversion

[官方论文页](https://neurips.cc/virtual/2026/poster/151685) · [作者来源](https://openreview.net/forum?id=YmGCdpjNNh)

- **问题 / 瓶颈** · 只与固定伙伴训练可能形成脆弱共识。
- **核心创新 / 方法** · 用战略风险规避作为学习偏置。
- **Baseline** · 普通协作训练。
- **Benchmark** · 含 LLM 的多类合作任务，未见伙伴。
- **关键结果 / 消融** · 摘要报告异质与未见伙伴协作改善。
- **适用条件 / 局限** · 对手风险分布设定影响效果。

**可复用机制** · 先对同任务中的伙伴换样和偏离做压力测试，再决定是否优化最优配合或稳健配合。

<a id="paper-152967"></a>

## Training Language Models to Explain Their Own Computations

[官方论文页](https://neurips.cc/virtual/2026/poster/152967) · [作者来源](https://openreview.net/forum?id=P0tEbOYZ6N)

- **问题 / 瓶颈** · 流畅自解释可能只是复述输出。
- **核心创新 / 方法** · 以特征信息、激活因果结构和输入影响的解释训练独立模型。
- **Baseline** · 既有解释机制。
- **Benchmark** · 新解释查询及不同能力的目标模型。
- **关键结果 / 消融** · 摘要报告几万解释即可有一定泛化。
- **适用条件 / 局限** · 依赖可信机制标签，摘要未给错误解释率。

**可复用机制** · 训练自动解释器时保存可独立核对的因果依据，并测试未见查询。

<a id="paper-155671"></a>

## Training Language Models via Neural Cellular Automata

[官方论文页](https://neurips.cc/virtual/2026/poster/155671) · [作者来源](https://openreview.net/forum?id=3ryTlHkGEr)

- **问题 / 瓶颈** · 通用合成源可能欠缺目标域合适的结构
- **核心创新 / 方法** · 用神经元胞自动机生成合成数据并对照迁移层
- **Baseline** · 不同合成动力学和迁移模块
- **Benchmark** · 代码、数学与网页语言训练
- **关键结果 / 消融** · 注意层最易迁移，代码偏简单动力学，数学和网页偏复杂
- **适用条件 / 局限** · 数据生成成本与性能依赖域

**可复用机制** · 在相同 token 数下按目标任务扫合成结构复杂度

<a id="paper-152102"></a>

## Training Optimal Large Diffusion Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152102) · [作者来源](https://openreview.net/forum?id=VV80K0h5rJ)

- **问题 / 瓶颈** · 初期较优的损失可能最后不如另一目标
- **核心创新 / 方法** · 对照扩散 ELBO 和 MaskGIT、调整噪声课程与权重衰减
- **Baseline** · MaskGIT 损失、不同日程与 AR 超参法则
- **Benchmark** · 大规模扩散语言训练；学习速度和最终表现
- **关键结果 / 消融** · 易到难噪声加速早期，ELBO 后程超越，权重衰减在多轮更重要
- **适用条件 / 局限** · 最佳配置受训练轮数与预算限制

**可复用机制** · 在相同步数和目标质量分别比较训练方法

<a id="paper-150358"></a>

## Training Transformers for KV-Cache Compressibility

[官方论文页](https://neurips.cc/virtual/2026/poster/150358) · [作者来源](https://openreview.net/forum?id=igMG5UgMAj)

- **问题 / 瓶颈** · 无约束训练后压缩可能删掉不可替代上下文
- **核心创新 / 方法** · 训练中遮蔽部分 KV 槽，测试时应用已有后验压缩
- **Baseline** · 普通训练及多种后验压缩方法
- **Benchmark** · 检索、长上下文问答、压缩前缀续写困惑度
- **关键结果 / 消融** · 摘要称质量预算曲线改善
- **适用条件 / 局限** · 注意不同遮蔽分布对推理失效的影响

**可复用机制** · 可重训时做压缩感知训练和纯部署压缩的对照

<a id="paper-149380"></a>

## Training with Harnesses: On-Policy Harness Self-Distillation for Complex Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/149380) · [作者来源](https://openreview.net/forum?id=qUygKjKWMJ)

- **问题 / 瓶颈** · 部署同时运行脚手架增加成本且可能干扰已学模型
- **核心创新 / 方法** · 用在线自蒸馏将脚手架行为吸收到基础模型
- **Baseline** · 基础模型、训练后加回脚手架
- **Benchmark** · 复杂推理任务，具体数值未报告
- **关键结果 / 消融** · 训练后重新加脚手架可能无益或变差
- **适用条件 / 局限** · 取决于脚手架能力是否可从现有输入复现

**可复用机制** · 拆开验收训练脚手架与测试脚手架的边际效果

<a id="paper-152046"></a>

## Trajectory-Consistent Dropout for Uncertainty Decomposition in Hamiltonian Neural Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/152046) · [作者来源](https://openreview.net/forum?id=Vuh3ZNdgF6)

- **问题 / 瓶颈** · 逐步重采样混淆参数不确定与时序噪声
- **核心创新 / 方法** · 蒙特卡洛 dropout 对整轨迹固定掩码，保留轴分解
- **Baseline** · 每步重采样或常规估计
- **Benchmark** · 弹簧链与横场 Ising；轨迹不确定、点预测与似然
- **关键结果 / 消融** · 分解可迁移，点预测和似然提升依系统而不同
- **适用条件 / 局限** · 物理结构与后验代理影响解释

**可复用机制** · 评估世界模型置信区间时记录整轨迹的模型一致性

<a id="paper-148661"></a>

## Trajectory-Matching Meta Pseudo-Labeling for Semi-Supervised Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/148661) · [作者来源](https://openreview.net/forum?id=w4z8ShoMu5)

- **问题 / 瓶颈** · 直接二阶元梯度显存需求高
- **核心创新 / 方法** · 以学生更新的方向匹配近似元伪标签更新
- **Baseline** · MPL、原始可微元梯度及强 SSL
- **Benchmark** · CIFAR100 2500 标签等；效果、显存和梯度对齐
- **关键结果 / 消融** · 显存少 39.7% 对 MPL，少 54% 对原始实现
- **适用条件 / 局限** · 方向匹配可能需短热身，依任务梯度噪声

**可复用机制** · 预算受限时测近似更新方向和伪标签错误传播

<a id="paper-151355"></a>

## TrajEvolve: Trajectory Evolution for Reinforcement Learning with Hindsight Credit Assignment

[官方论文页](https://neurips.cc/virtual/2026/poster/151355) · [作者来源](https://openreview.net/forum?id=bARCcbV2Jj)

- **问题 / 瓶颈** · 连续分数难标且精度不足
- **核心创新 / 方法** · 反事实验证删除或修改步骤后能否完成，以二元监督学必要性
- **Baseline** · 原轨迹级信用，摘要未列名单
- **Benchmark** · 两个数据集，具体名称未报告
- **关键结果 / 消融** · 摘要报告效果优于对照
- **适用条件 / 局限** · 依赖删除后仍能有效验证以及环境可重放

**可复用机制** · 在可回放任务用必要性标签训练或校准过程奖励

<a id="paper-154461"></a>

## TrajLift: Encoding Verbal Memory Dynamics via Heat Diffusion on Semantic Hierarchies

[官方论文页](https://neurips.cc/virtual/2026/poster/154461) · [作者来源](https://openreview.net/forum?id=DPkTPrRA03)

- **问题 / 瓶颈** · 仅词序列丢概念层级。
- **核心创新 / 方法** · 在语义图做热扩散并用谱选择表达层级。
- **Baseline** · 不联合结构与时间的方法。
- **Benchmark** · 合成与临床语料。
- **关键结果 / 消融** · 证明可分结构和时间，实证持续改善。
- **适用条件 / 局限** · 依赖层级构造。

**可复用机制** · 为有知识层级的轨迹用扩散度量而非平面相似。

<a id="paper-154385"></a>

## TrajLoc: Trajectory-Attention Localization for Multi-Object Motion Control

[官方论文页](https://neurips.cc/virtual/2026/poster/154385) · [作者来源](https://openreview.net/forum?id=DyRKHZlevm)

- **问题 / 瓶颈** · 多实体互相抢运动指令。
- **核心创新 / 方法** · 按目标轨迹定位注意区域。
- **Baseline** · 普通运动控制。
- **Benchmark** · 六数据集，最多 20 目标及域外场景。
- **关键结果 / 消融** · 保真与轨迹一致提高。
- **适用条件 / 局限** · 拥挤遮挡和轨迹标注质量需测。

**可复用机制** · 拆每个对象的约束并测角色和路径串扰。

<a id="paper-155885"></a>

## TrajWiki: Source-Grounded Memory Trajectories for Long-Horizon Dialogue Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/155885) · [作者来源](https://openreview.net/forum?id=26nRwIZFcb)

- **问题 / 瓶颈** · 检索散碎会重复且难更新冲突。
- **核心创新 / 方法** · 逐步汇编实体、事件、数量和冲突，保轨迹来源。
- **Baseline** · 普通长记忆。
- **Benchmark** · LoCoMo、MedMT，开闭模型。
- **关键结果 / 消融** · 多模型对话改善，量未核。
- **适用条件 / 局限** · 总结可能丢例外或重新引入错误。

**可复用机制** · 要求后续回答可追溯到条目和原轮次。

<a id="paper-155049"></a>

## Transcoda: End-to-End Zero-Shot Optical Music Recognition via Data-Centric Synthetic Training

[官方论文页](https://neurips.cc/virtual/2026/poster/155049) · [作者来源](https://openreview.net/forum?id=8pzICTUGAk)

- **问题 / 瓶颈** · 多种等价音乐文本分散学习信号。
- **核心创新 / 方法** · 合成训练，编码归一并以语法解码。
- **Baseline** · 既有光学音乐识别。
- **Benchmark** · 零样本谱面转录。
- **关键结果 / 消融** · 摘要给规范和合法性控制，量未报。
- **适用条件 / 局限** · 符号正规形应保语义和时间。

**可复用机制** · 结构 OCR 先统一可等价编码，再追求序列准确。

<a id="paper-155046"></a>

## Transcoder Adapters for Reasoning-Model Diffing

[官方论文页](https://neurips.cc/virtual/2026/poster/155046) · [作者来源](https://openreview.net/forum?id=8r7iV7T03x)

- **问题 / 瓶颈** · 重建不变主干浪费可解释容量。
- **核心创新 / 方法** · 训练 transcoder adapter 重建微调前后差。
- **Baseline** · 典型全 MLP transcoder。
- **Benchmark** · 多推理基准和 7B 案例。
- **关键结果 / 消融** · 少一数量级活跃特征，保大量能力。
- **适用条件 / 局限** · 适用能配对的层结构。

**可复用机制** · 把受训行为变化单独建模后再做介入。

<a id="paper-149773"></a>

## Transductive Generalization for GNNs via Optimal Transport

[官方论文页](https://neurips.cc/virtual/2026/poster/149773) · [作者来源](https://openreview.net/forum?id=nPn4mFZwlJ)

- **问题 / 瓶颈** · 消息传播可能引入有害几何。
- **核心创新 / 方法** · 从最优传输泛化界做可训练正则。
- **Baseline** · 常规 GNN。
- **Benchmark** · 传导式泛化。
- **关键结果 / 消融** · 较原模型一致改善。
- **适用条件 / 局限** · 依赖标注或类估计质量。

**可复用机制** · 检查传播改变特征几何后再选正则。

<a id="paper-153605"></a>

## Transferability for General Reasoning: An Automated Curriculum for Multi-Domain LLM RL

[官方论文页](https://neurips.cc/virtual/2026/poster/153605) · [作者来源](https://openreview.net/forum?id=K8uod6RgUG)

- **问题 / 瓶颈** · 只追当下可学习会偏主域。
- **核心创新 / 方法** · 用在线 bandit 估跨域迁移收益。
- **Baseline** · 仅可学习性的课程。
- **Benchmark** · 多域与不平衡训练混合。
- **关键结果 / 消融** · 移除迁移项明显下降。
- **适用条件 / 局限** · 跨域分数估计需节省 rollout。

**可复用机制** · 监控每字段梯度收益对其他域的外部性。

<a id="paper-151820"></a>

## Transferable SCF-Acceleration through Solver-Aligned Initialization Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151820) · [作者来源](https://openreview.net/forum?id=Xjaap3pzlS)

- **问题 / 瓶颈** · 准确预测收敛态不保证快速收敛。
- **核心创新 / 方法** · 用求解器对齐训练和含构建成本的 ERIC。
- **Baseline** · 基态监督及普通 RIC。
- **Benchmark** · SCF 求解和域外初始猜测。
- **关键结果 / 消融** · 原监督能预测目标却拖慢求解。
- **适用条件 / 局限** · 求解器和近似需重新对齐。

**可复用机制** · 模型辅助求解按最终执行成本而非静态预测误差验。

<a id="paper-149253"></a>

## Transferable, Time-Parallel Graph Dynamics via Space-Time Factorization

[官方论文页](https://neurips.cc/virtual/2026/poster/149253) · [作者来源](https://openreview.net/forum?id=rjusfdj0um)

- **问题 / 瓶颈** · 每拓扑重训难积累数据。
- **核心创新 / 方法** · 时空因子化，局部时间可并行。
- **Baseline** · 仅本地训练 oracle。
- **Benchmark** · 跨几何 Navier–Stokes，15 训练几何。
- **关键结果 / 消融** · 相对 L2 接近 oracle 约 10% 内。
- **适用条件 / 局限** · 图间共动力假设需验证。

**可复用机制** · 共享过程规律而把拓扑适配留给确定混合器。

<a id="paper-151650"></a>

## Transfer Entropy as a Measure of Information Flow in VLMs and LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/151650) · [作者来源](https://openreview.net/forum?id=Z3QSYA86Ix)

- **问题 / 瓶颈** · 注意力强弱不能单独诊断冗余。
- **核心创新 / 方法** · 估层、token 和头的转移熵。
- **Baseline** · 不同塔与模型深度。
- **Benchmark** · CLIP、RoBERTa、解码器模型和 T5。
- **关键结果 / 消融** · CLIP 视觉晚层冗余，架构具有不同流峰。
- **适用条件 / 局限** · 转移熵不直接证明因果。

**可复用机制** · 先定位信息传递再做干预验证。

<a id="paper-149647"></a>

## Transfer Learning of Linear Regression with Multiple Pretrained Models: Benefiting from More Pretrained Models via Overparameterization Debiasing

[官方论文页](https://neurips.cc/virtual/2026/poster/149647) · [作者来源](https://openreview.net/forum?id=oVpl7LvQtc)

- **问题 / 瓶颈** · 来源多可能新增高维估计偏差。
- **核心创新 / 方法** · 推测试误差和乘法校正。
- **Baseline** · 不校正的多模型迁移。
- **Benchmark** · 线性回归理论与实证。
- **关键结果 / 消融** · 在条件下多来源可帮，校正降低偏差。
- **适用条件 / 局限** · 未证明直接用于一般深网络。

**可复用机制** · 多源迁移的高维增益需和校正成本一起测。

<a id="paper-152993"></a>

## Transfer Learning Through Conditional Quantile Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/152993) · [作者来源](https://openreview.net/forum?id=OmEzTubNlR)

- **问题 / 瓶颈** · 直接源标签混合导致分布失配。
- **核心创新 / 方法** · 按目标条件分位变换源数据再训练。
- **Baseline** · 目标单训、其他跨域。
- **Benchmark** · 仿真和真实回归。
- **关键结果 / 消融** · 有效条件下超额风险更紧，精度改善。
- **适用条件 / 局限** · 需要分位估计质量。

**可复用机制** · 适配不只平移均值，应保护不同输入条件下的形状。

<a id="paper-153562"></a>

## Transferring Visual Explainability from Self-Explaining to Prediction-Only Vision Transformers via Task Arithmetic

[官方论文页](https://neurips.cc/virtual/2026/poster/153562) · [作者来源](https://openreview.net/forum?id=KSFfnJEsF3)

- **问题 / 瓶颈** · 新领域缺解释标签。
- **核心创新 / 方法** · 从源解释监督取算术向量，加到预测 ViT。
- **Baseline** · 仅预测基线。
- **Benchmark** · ImageNet-1k 解释训练、十目标集。
- **关键结果 / 消融** · 解释变好且分类基本保持。
- **适用条件 / 局限** · 架构和来源兼容必须验证。

**可复用机制** · 把解释训练增量当适配器，与任务精度独立验。

<a id="paper-150527"></a>

## Transformers Can Learn Multiclass Classification In-Context: Isotropy Governs Generalization

[官方论文页](https://neurips.cc/virtual/2026/poster/150527) · [作者来源](https://openreview.net/forum?id=hSlGiiuHL6)

- **问题 / 瓶颈** · 平均分类掩盖少数类提示退化。
- **核心创新 / 方法** · 用稳定秩分析上下文多类与标签偏。
- **Baseline** · 既有二类分析。
- **Benchmark** · 线性 Transformer 和预训练实证。
- **关键结果 / 消融** · 高稳定秩提升泛化与少数类稳健。
- **适用条件 / 局限** · 受类中心模型与提示设计限制。

**可复用机制** · 挑演示时兼顾频率和表示方向覆盖。

<a id="paper-151845"></a>

## Transformers Converge to Invariant Algorithmic Cores

[官方论文页](https://neurips.cc/virtual/2026/poster/151845) · [作者来源](https://openreview.net/forum?id=XSpP1DqsdD)

- **问题 / 瓶颈** · 参数逐元素难识别共享算法。
- **核心创新 / 方法** · 提取核心子空间并因果验证。
- **Baseline** · 比较不同 Transformer 参数化。
- **Benchmark** · 合成及预训练模型。
- **关键结果 / 消融** · 能恢复共享算法结构，幅度待核。
- **适用条件 / 局限** · 机制验证依赖所测任务。

**可复用机制** · 做跨模型解释时对齐计算功能，而非索引。

<a id="paper-156799"></a>

## Transformers in the Dark: Navigating Unknown Search Spaces via Bandit Feedback

[官方论文页](https://neurips.cc/virtual/2026/poster/156799) · [作者来源](https://openreview.net/forum?id=Jij7zCjVfc)

- **问题 / 瓶颈** · 可写搜索程序不代表可从反馈学。
- **核心创新 / 方法** · 固定扩树反馈机制，训练不同搜索轨迹。
- **Baseline** · 训练前后和不同搜索策略。
- **Benchmark** · 受控 bandit 树及预训练模型。
- **关键结果 / 消融** · 理论可表达，轨迹训练改善。
- **适用条件 / 局限** · 受控反馈与真实环境差异大。

**可复用机制** · 先在可复验环境测搜索和观察反馈角色。

<a id="paper-155096"></a>

## Transformers Linearly Represent Highly Structured World Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155096) · [作者来源](https://openreview.net/forum?id=8RPfEpnyrk)

- **问题 / 瓶颈** · 表面文本不同会掩盖共享计算。
- **核心创新 / 方法** · 提取线性世界状态及稀疏决策回路。
- **Baseline** · 不同任务呈现。
- **Benchmark** · 组合推理受控模型。
- **关键结果 / 消融** · 几何由约束而非表面变化决定。
- **适用条件 / 局限** · 任务特化，真实世界状态不可直接推断。

**可复用机制** · 用等价呈现验证机制是否真正对应任务约束。

<a id="paper-154590"></a>

## Transformers Provably Implement In-Context Reinforcement Learning with Policy Improvement

[官方论文页](https://neurips.cc/virtual/2026/poster/154590) · [作者来源](https://openreview.net/forum?id=CRstYxsyfj)

- **问题 / 瓶颈** · 模型行为好不表明执行何种机制。
- **核心创新 / 方法** · 构造线性注意实现 SARSA 和 actor–critic。
- **Baseline** · 只能做价值估计的上下文设置。
- **Benchmark** · 理论参数构造。
- **关键结果 / 消融** · 单块可执行所述改进。
- **适用条件 / 局限** · 存在性不保证训练实际获得。

**可复用机制** · 将策略改进及价值估计分别作为上下文探针。

<a id="paper-155595"></a>

## Transformers Provably Learn Graph Search: Training Dynamics and the Exponential Power of Depth

[官方论文页](https://neurips.cc/virtual/2026/poster/155595) · [作者来源](https://openreview.net/forum?id=4QZv5tGC5T)

- **问题 / 瓶颈** · 模型可表达 DFS 不一定能梯度学到。
- **核心创新 / 方法** · 引导搜索训练样例配两层 Transformer。
- **Baseline** · 不同深度与训练数据。
- **Benchmark** · 有向图寻路和未见图。
- **关键结果 / 消融** · 给两层梯度流学习和泛化保证。
- **适用条件 / 局限** · 依赖刻意训练分布。

**可复用机制** · 测试搜索归纳前分开控制深度和示范覆盖。

<a id="paper-149320"></a>

## Transforming Image Editors into Video Editors

[官方论文页](https://neurips.cc/virtual/2026/poster/149320) · [作者来源](https://openreview.net/forum?id=r1K6p0Djsg)

- **问题 / 瓶颈** · 逐帧编辑易时序闪烁。
- **核心创新 / 方法** · 关键帧固定为锚点，再运动引导生成。
- **Baseline** · 现有视频编辑。
- **Benchmark** · IVEBench、VIE-Bench。
- **关键结果 / 消融** · 一致性与遵循较强，消融表明效果关联图像编辑器质量。
- **适用条件 / 局限** · 复杂遮挡或大运动限制锚传播。

**可复用机制** · 升级视频质量先优化空间编辑，再查时间传播。

<a id="paper-154776"></a>

## Transition-Aware Credit Assignment in Agentic Learning for LLM Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/154776) · [作者来源](https://openreview.net/forum?id=B3PxtA5k1K)

- **问题 / 瓶颈** · 失败轨迹内有用工具步骤可能被整体奖励惩罚。
- **核心创新 / 方法** · TACA 建模工具转移有效性并稳定稀疏工具使用分组。
- **Baseline** · 代理与非代理推理强化学习。
- **Benchmark** · 多模型多个推理任务。
- **关键结果 / 消融** · 摘要报告一致优于对照。
- **适用条件 / 局限** · 依赖可度量转移质量，摘要未给额外标注和计算。

**可复用机制** · 同一失败轨迹中保留有信息的局部行动，降低所有工具动作共享同一优势的偏差。

<a id="paper-149447"></a>

## TransMem: Transition-Aware Retrieval for Evolving Personal Memory

[官方论文页](https://neurips.cc/virtual/2026/poster/149447) · [作者来源](https://openreview.net/forum?id=q1I1T0tsdw)

- **问题 / 瓶颈** · 只记孤立事实可能把过期偏好当成当前条件。
- **核心创新 / 方法** · 构建主题记忆图并加入表示偏好改变的事件。
- **Baseline** · 事实锚、时间扩展、扁平变化检索与固定跳数。
- **Benchmark** · 长期个性化及带更新的用户记忆。
- **关键结果 / 消融** · 摘要报告显式变化记录及检索具有优势。
- **适用条件 / 局限** · 依赖可靠的偏好改变检测。

**可复用机制** · 对会变化的用户状态，记录旧值到新值的过渡及来源。

<a id="paper-155288"></a>

## Transolver-GMsFEM: A Hybrid Framework for High-Contrast Multiscale PDEs on Irregular Grids

[官方论文页](https://neurips.cc/virtual/2026/poster/155288) · [作者来源](https://openreview.net/forum?id=6fXwM7ttG5)

- **问题 / 瓶颈** · 直接神经解在参数偏移下脆弱，数值法的局部特征问题昂贵。
- **核心创新 / 方法** · 以 Transolver 代替多尺度有限元中的基函数求解。
- **Baseline** · 纯神经 PDE 求解。
- **Benchmark** · 不规则网格和高对比多尺度 PDE，含分布外变化。
- **关键结果 / 消融** · 摘要报告准确和鲁棒性更佳，尤其在纯神经方法失败时。
- **适用条件 / 局限** · 依赖合适的传统分解和基函数验收。

**可复用机制** · 混合求解先找出廉价可近似的组件，将核心数值约束留在组装步骤。

<a id="paper-151282"></a>

## Transporting Quantiles to Codebook: Scalable Vector Quantization without Codebook Collapse

[官方论文页](https://neurips.cc/virtual/2026/poster/151282) · [作者来源](https://openreview.net/forum?id=bYAJ4GjECY)

- **问题 / 瓶颈** · 直接学码本可能使少数 token 独占使用。
- **核心创新 / 方法** · 轻量流匹配从规则源分布输运等分位码字。
- **Baseline** · 常规可学向量量化码本。
- **Benchmark** · 图像及两个高精度分词任务。
- **关键结果 / 消融** · 摘要报告码字充分利用并改善表达。
- **适用条件 / 局限** · 流近似、码本大小与开销边界未报告。

**可复用机制** · 避免依靠均衡惩罚修补塌缩时，可用保质量的映射定义有结构的离散化。

<a id="paper-153288"></a>

## Transporting the Past: An Optimal Transport View of Backtracking Counterfactuals

[官方论文页](https://neurips.cc/virtual/2026/poster/153288) · [作者来源](https://openreview.net/forum?id=MNVvTXlGGM)

- **问题 / 瓶颈** · 直接最近投影可能满足反事实却打破噪声解释结构。
- **核心创新 / 方法** · 比较最优传输的逐点评估和加外生独立约束版本。
- **Baseline** · 不约束外生独立的投影。
- **Benchmark** · 非双射结构因果模型合成实验。
- **关键结果 / 消融** · 摘要报告传输代价、满足度与独立性的权衡。
- **适用条件 / 局限** · 合成结构和因果假设限制外推。

**可复用机制** · 做反事实先声明哪些机制固定，别只验证反事实约束是否达成。

<a id="paper-155149"></a>

## Trapping Attacker in Dilemma: Examining Internal Correlations and External Influences of Trigger for Defending GNN Backdoors

[官方论文页](https://neurips.cc/virtual/2026/poster/155149) · [作者来源](https://openreview.net/forum?id=7xWSWpsU5J)

- **问题 / 瓶颈** · 单一异常指标可能漏检或误删正常结构。
- **核心创新 / 方法** · 防御框架结合内部结构和预测影响两类信号。
- **Baseline** · 既有图模型防护。
- **Benchmark** · 图神经网络后门防护，比较干净准确度及风险。
- **关键结果 / 消融** · 摘要表明组合防护能限制所测后门效果。
- **适用条件 / 局限** · 证据限所测图和防护设定，摘要未给自然分布误报。

**可复用机制** · 图防护验收按异常结构和影响分别诊断，避免单看防御成功率。

<a id="paper-150855"></a>

## Traversal-Invariant Positional Encoding for Serialized Graphs

[官方论文页](https://neurips.cc/virtual/2026/poster/150855) · [作者来源](https://openreview.net/forum?id=erlgJjFpeV)

- **问题 / 瓶颈** · 序列位置变化不应改变底层图关系。
- **核心创新 / 方法** · 分析无环情形中的结构位置编码，并提出遍历稳健方法。
- **Baseline** · 参数匹配 Graphormer 与正弦位置编码。
- **Benchmark** · BACE、BBBP 和片段级解释。
- **关键结果 / 消融** · 摘要报告可与图原生模型竞争，警示结构对齐增 5 点。
- **适用条件 / 局限** · 严格不变依赖分析的结构条件。

**可复用机制** · 图的可读序列接口可保持结构等价，不必为每条遍历单独学习同一关系。

<a id="paper-152716"></a>

## TraXion: Rethinking Pre-training Frameworks for Mobility and Beyond

[官方论文页](https://neurips.cc/virtual/2026/poster/152716) · [作者来源](https://openreview.net/forum?id=QtFyIbY3oe)

- **问题 / 瓶颈** · 将访问序列直接当自然语言忽略事件主体和时空属性。
- **核心创新 / 方法** · 以多实体时空事件流统一不同序列领域。
- **Baseline** · 从语言模型直接继承的预训练目标。
- **Benchmark** · 移动记录、访问日志及临床时序。
- **关键结果 / 消融** · 摘要报告拓展领域匹配或超过旧方法。
- **适用条件 / 局限** · 摘要未给独立目标拆解和预处理预算。

**可复用机制** · 跨领域迁移损失前先比对事件时间、主体和地点是否真的像文本序列。

<a id="paper-150271"></a>

## Treat Bias as Noise: Training Bias-Robust LLM Reasoning via Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/150271) · [作者来源](https://openreview.net/forum?id=jPnZFyHo4X)

- **问题 / 瓶颈** · 只教模型反对某类线索会学到相反捷径。
- **核心创新 / 方法** · 用平衡训练条件和强化学习形成不依赖线索的推理。
- **Baseline** · 普通训练与更大 Qwen3。
- **Benchmark** · 偏置信号下的推理。
- **关键结果 / 消融** · 摘要称偏置抵抗可超过 8B 与 14B 对照。
- **适用条件 / 局限** · 依赖线索与正确结论的受控生成。

**可复用机制** · 验证模型对捷径的独立性，要同时测试线索正确、错误和缺失。

<a id="paper-155538"></a>

## Treating Hyperparameters as Interventions: Task-Invariant Representation Learning for Transferable HPO

[官方论文页](https://neurips.cc/virtual/2026/poster/155538) · [作者来源](https://openreview.net/forum?id=4qFz5DLdjS)

- **问题 / 瓶颈** · 训练得到的嵌入可能把超参数选择误当任务身份。
- **核心创新 / 方法** · 约束表示跨超参数干预不变且能预测表现。
- **Baseline** · 常规任务表示与不同超参数空间。
- **Benchmark** · 学习率变化百倍及跨域 HPO。
- **关键结果 / 消融** · 摘要报告条件独立检验通过且可跨超参数空间迁移。
- **适用条件 / 局限** · 依赖可获得覆盖的超参数干预。

**可复用机制** · 构建调参元学习输入前，切断历史参数选择与任务特征的泄漏。

<a id="paper-155240"></a>

## TReDS: Trajectory-Grounded Requirement-Capability Modeling for Training Distribution Shaping in Tool-Interactive Tasks

[官方论文页](https://neurips.cc/virtual/2026/poster/155240) · [作者来源](https://openreview.net/forum?id=7CVEj1Jjzi)

- **问题 / 瓶颈** · 单一任务成功率不能指出应补哪一技能。
- **核心创新 / 方法** · 从受控工具轨迹估需求，在同一空间跟踪能力，按可靠性在线修正。
- **Baseline** · 静态训练抽样。
- **Benchmark** · 工具交互任务及不同能力需求。
- **关键结果 / 消融** · 摘要报告调整训练分布有益。
- **适用条件 / 局限** · 需有可信探查轨迹，摘要未给测量成本。

**可复用机制** · 设计任务采样时直接匹配诊断出的技能差距，不只改善奖励配方。

<a id="paper-153244"></a>

## Tree-Ensemble Repair through Constrained Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/153244) · [作者来源](https://openreview.net/forum?id=MgEUWFldkw)

- **问题 / 瓶颈** · 重新训练难确保目标属性修复。
- **核心创新 / 方法** · MILP 联合调整树集成以满足要求，并尽量保留效用。
- **Baseline** · 普通验证及修复流程。
- **Benchmark** · 树集成与 MDP 安全策略。
- **关键结果 / 消融** · 摘要报告常可改善属性并避免性能退化。
- **适用条件 / 局限** · 计算可行性随树与约束大小变化。

**可复用机制** · 结构化策略的局部修理可以同时优化规则符合和原任务表现。

<a id="paper-151038"></a>

## TreeGraft: Adaptive Multi-Drafter Grafting for Tree-Based Speculative Decoding

[官方论文页](https://neurips.cc/virtual/2026/poster/151038) · [作者来源](https://openreview.net/forum?id=dRhBDs50Cm)

- **问题 / 瓶颈** · 小草稿快速但错误多，大草稿慢。
- **核心创新 / 方法** · 不同草稿模型共享一棵树，并按需更新评分。
- **Baseline** · 两个固定单草稿方案。
- **Benchmark** · 树式推测解码的吞吐与速度。
- **关键结果 / 消融** · 相较较强单方案平均提升 15.1%，最高 26.6%。
- **适用条件 / 局限** · 增加模型需要内存，摘要未说明分支调度成本。

**可复用机制** · 搜索系统可将广泛扩展与昂贵重排分配给不同预算模型。

<a id="paper-148753"></a>

## TreemapMix: Dirichlet-Controlled Multi-Image Augmentation for Probability and Ordinal Supervision

[官方论文页](https://neurips.cc/virtual/2026/poster/148753) · [作者来源](https://openreview.net/forum?id=vHPQM0CONK)

- **问题 / 瓶颈** · 自由混图无法明确各类占比和可验证排序。
- **核心创新 / 方法** · Dirichlet 采样权重并分配面积比例区域，提供两类训练目标。
- **Baseline** · 常规混合增强与监督目标。
- **Benchmark** · 图像分类和表征迁移。
- **关键结果 / 消融** · 摘要报告两种监督均可利用区域配置，表征可迁移。
- **适用条件 / 局限** · 像素面积不总等于语义信息，摘要未给物体遮挡条件。

**可复用机制** · 合成训练样本可从相同可测属性导出不同监督，先检查模型需要校准概率还是相对顺序。

<a id="paper-153976"></a>

## TreePII: Efficient Computation of Higher-Order Probabilistic Interaction Indices in Tree Ensembles

[官方论文页](https://neurips.cc/virtual/2026/poster/153976) · [作者来源](https://openreview.net/forum?id=H6uLXEZRGE)

- **问题 / 瓶颈** · 逐项枚举高阶特征组合开销大。
- **核心创新 / 方法** · 在多线性扩展的偏导积分上用插值求积求精确指标。
- **Baseline** · 既有树交互计算。
- **Benchmark** · 树集成高阶概率交互，比较理论与实践。
- **关键结果 / 消融** · 摘要报告超越现有计算。
- **适用条件 / 局限** · 依赖树结构，摘要未给量级。

**可复用机制** · 结构模型先寻找可复用的积分表示，再决定是否用抽样近似解释。

<a id="paper-155984"></a>

## Tree Rotary Positional Encoding for Extreme Length Extrapolation from Scratch

[官方论文页](https://neurips.cc/virtual/2026/poster/155984) · [作者来源](https://openreview.net/forum?id=1NNDe1C284)

- **问题 / 瓶颈** · 单索引把训练位置变化和未见长距离耦合。
- **核心创新 / 方法** · 按结构层次组织旋转位置维度。
- **Baseline** · RoPE。
- **Benchmark** · 1.2B 训练长度 512，外推 32K。
- **关键结果 / 消融** · 32K 困惑度 149.96 对 4532.21，推理效率相近。
- **适用条件 / 局限** · 需要从头训练，摘要未给多样下游生成正确率。

**可复用机制** · 向新长度迁移时，可在多个尺度分别编码偏移，避免所有位置维度同时进入陌生范围。

<a id="paper-153291"></a>

## Tree Training: Efficient LLM Training on Tree-Structured Trajectories

[官方论文页](https://neurips.cc/virtual/2026/poster/153291) · [作者来源](https://openreview.net/forum?id=MMS2MVw0et)

- **问题 / 瓶颈** · 把树摊平后每条路径重复计算前缀
- **核心创新 / 方法** · 以等价 token 加权损失算每个节点一次，必要时将树无冗余拆分
- **Baseline** · 每分支分别计算的 SFT 和 RL
- **Benchmark** · 稠密及 MoE；端到端训练速度与显存
- **关键结果 / 消融** · 最快 6.2 倍，分区峰值可由单路径限定
- **适用条件 / 局限** · 复用收益依赖分支重合和激活内存

**可复用机制** · 多 rollout 改树型训练前用原逐轨迹损失逐项核对数值

<a id="paper-139448"></a>

## TRIAD: Benchmarking Omni-Modal Ambiguity in Multimodal Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139448) · [作者来源](https://openreview.net/forum?id=PFj07C6mVV)

- **问题 / 瓶颈** · 简单识别任务允许忽略音频
- **核心创新 / 方法** · 构建文图音三元组，并用去模态或描述替代做反事实
- **Baseline** · 不同多模态模型及人类
- **Benchmark** · TRIAD；按组准确率与模态贡献
- **关键结果 / 消融** · 部分设置模型低至个位数，人类较稳，模型常低用音频
- **适用条件 / 局限** · 需要证明缺少任一路时确实不唯一

**可复用机制** · 为音视频 Agent 加只有正确融合证据才可区分的最小对照

<a id="paper-139419"></a>

## TRIAGE: Evaluating Prospective Metacognitive Control in LLMs under Resource Constraints

[官方论文页](https://neurips.cc/virtual/2026/poster/139419) · [作者来源](https://openreview.net/forum?id=Rsyi3nwmf6)

- **问题 / 瓶颈** · 逐题准确率不测排队、择题和分配成本
- **核心创新 / 方法** · 用模型自己的基础成本定预算，预先承诺有序计划
- **Baseline** · 推理启用与关闭、多个前沿和开源模型
- **Benchmark** · 竞赛数学、研究生科学、代码和专家综合
- **关键结果 / 消融** · 摘要显示前瞻控制存在明显缺口
- **适用条件 / 局限** · 规则和计费结果随工具环境变化

**可复用机制** · 把有限作答预算做成整批任务测评

<a id="paper-156097"></a>

## TriAxialKV: Toward Extreme Low-Precision KV-Cache Quantization for Agentic Inference Tasks

[官方论文页](https://neurips.cc/virtual/2026/poster/156097) · [作者来源](https://openreview.net/forum?id=0PStm4OPPJ)

- **问题 / 瓶颈** · 工具结果与普通历史 token 的压缩敏感性不同
- **核心创新 / 方法** · 按三轴做混合精度及配套解码内核
- **Baseline** · SGLang 的 BF16 KV
- **Benchmark** · Qwen3-VL-32B-Thinking、OSWorld；成功与吞吐
- **关键结果 / 消融** · 匹配准确，支持 4.5 倍缓存并增 30% 吞吐
- **适用条件 / 局限** · 依赖特定硬件及角色标注，其他工作负载需重验

**可复用机制** · 在相同内存下先找关键角色再给其保留较高精度

<a id="paper-155841"></a>

## TRIDENT: Post-Selection Evidence Accountability for Token-Efficient RAG

[官方论文页](https://neurips.cc/virtual/2026/poster/155841) · [作者来源](https://openreview.net/forum?id=2UTqijjMAy)

- **问题 / 瓶颈** · 随机配对校准遇到短名单时可能偏乐观
- **核心创新 / 方法** · 按日志规约检验支持，控制查询级错误或弃权
- **Baseline** · 随机配对校准与等预算选证
- **Benchmark** · HotpotQA、2Wiki、MuSiQue；假证书和问答表现
- **关键结果 / 消融** · 摘要称控制假证书且改善同预算选择
- **适用条件 / 局限** · 保证限日志选择规约，换策略需再校准

**可复用机制** · 把证据校准集设成实际候选策略形成的分布

<a id="paper-148902"></a>

## Triggering Generalist Reasoning via Predictive Uncertainty for Dual-System VLA

[官方论文页](https://neurips.cc/virtual/2026/poster/148902) · [作者来源](https://openreview.net/forum?id=uJi8ZIMP1U)

- **问题 / 瓶颈** · 固定调用浪费易阶段算力且可能错过突发
- **核心创新 / 方法** · 复用现有前向估不确定性，阈值化决定是否调用通用模型
- **Baseline** · 固定频率等非自适应方式
- **Benchmark** · VLA-Arena 的成功率、调用成本
- **关键结果 / 消融** · 匹配成功时通用模型调用显著减少
- **适用条件 / 局限** · 不确定性的校准受任务变化及分布移位影响

**可复用机制** · 部署前用易例和突发恢复分别测成本成功率曲线

<a id="paper-139435"></a>

## Trimming the Long-Tail of Visual World Modeling Evaluation

[官方论文页](https://neurips.cc/virtual/2026/poster/139435) · [作者来源](https://openreview.net/forum?id=QXhOfEEBll)

- **问题 / 瓶颈** · 常见场景真实感掩盖约束及因果交互弱点
- **核心创新 / 方法** · 以物体属性、动力学及约束任务建立分项，并校验自动评审
- **Baseline** · 通用视觉世界模型及人类评审
- **Benchmark** · Tailor-Bench；长尾工具交互
- **关键结果 / 消融** · 多类长尾失败，8B 自动评审与人类相关 0.88
- **适用条件 / 局限** · 自动评审不能替代外部物理验证

**可复用机制** · 按交互稀有度和违反的物理约束记录错误
