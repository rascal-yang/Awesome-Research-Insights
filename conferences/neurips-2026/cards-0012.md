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
