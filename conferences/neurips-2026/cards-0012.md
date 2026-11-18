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

<a id="paper-148495"></a>

## TriSearch: Learning to Optimize Triangulations via Bistellar Flips

[官方论文页](https://neurips.cc/virtual/2026/poster/148495) · [作者来源](https://openreview.net/forum?id=xNmLiO7Q7N)

- **问题 / 瓶颈** · 全空间枚举随规模爆炸。
- **核心创新 / 方法** · 用局部三角化支持和几何组合特征编码翻转。
- **Baseline** · 现有三角剖分采样。
- **Benchmark** · 3D、4D 多面体，固定预算。
- **关键结果 / 消融** · 小实例训练能零样本泛化，并在 4D 找更多不同有效剖分。
- **适用条件 / 局限** · 需可定义局部可行变换。

**可复用机制** · 将可行约束放入动作表示，策略只学习排序。

<a id="paper-152166"></a>

## TriSpec: Ternary Speculative Decoding via Lightweight Proxy Verification

[官方论文页](https://neurips.cc/virtual/2026/poster/152166) · [作者来源](https://openreview.net/forum?id=V2xJUmQ22n)

- **问题 / 瓶颈** · 全靶模型验证成本成为瓶颈。
- **核心创新 / 方法** · 三段式用精简验证器，只在不确定时调全模型。
- **Baseline** · 标准推测解码。
- **Benchmark** · Qwen3、多个 R1 蒸馏家族。
- **关键结果 / 消融** · 最高加速 35%，靶调用少 50%，准确率接近。
- **适用条件 / 局限** · 精确一致性需按目标独立验。

**可复用机制** · 扩草稿前测验证端的剩余开销。

<a id="paper-154734"></a>

## TriTD: Tri-Partite Trajectory–Distribution Distillation for Real-Time Autoregressive Video Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/154734) · [作者来源](https://openreview.net/forum?id=BQaVJhPUAg)

- **问题 / 瓶颈** · 同一个损失难覆盖三种误差源。
- **核心创新 / 方法** · 下一点轨迹蒸馏、按块加噪等分别约束。
- **Baseline** · 普通一致蒸馏。
- **Benchmark** · 实时 AR 视频质量和推理。
- **关键结果 / 消融** · 收紧初始化误差界并降低冗余 KV 更新。
- **适用条件 / 局限** · 依赖块式轨迹与顺序。

**可复用机制** · 先分解累计误差，再为不同来源设计训练信号。

<a id="paper-156111"></a>

## TritonTune: LLM-Guided Multi-Agent Optimization of GPU Kernel Configurations

[官方论文页](https://neurips.cc/virtual/2026/poster/156111) · [作者来源](https://openreview.net/forum?id=0JiQIE135s)

- **问题 / 瓶颈** · 生成候选可能在某输入尺寸退化。
- **核心创新 / 方法** · 多代理定向改参数，以原配置作 fallback。
- **Baseline** · 原配置和单纯 LLM 调参。
- **Benchmark** · TritonBench 19 内核、393 尺寸，V100。
- **关键结果 / 消融** · 几何平均 2.24 倍，80% 尺寸改善。
- **适用条件 / 局限** · 硬件和计时噪声影响验收。

**可复用机制** · 每个输入族独立保留经实测的原版本。

<a id="paper-152126"></a>

## Trivialized Generative Models on Lie Groups

[官方论文页](https://neurips.cc/virtual/2026/poster/152126) · [作者来源](https://openreview.net/forum?id=VLKcHOqgkz)

- **问题 / 瓶颈** · 直接群空间求解成本高。
- **核心创新 / 方法** · 学习端点约束的代数路径。
- **Baseline** · Riemannian 及群生成。
- **Benchmark** · SO(3) 及非紧 Sp(4,R) 物理基准。
- **关键结果 / 消融** · 改善质量和效率，幅度未核。
- **适用条件 / 局限** · 依赖可用群参数及提升。

**可复用机制** · 在共享线性坐标求解，再验证群约束。

<a id="paper-139385"></a>

## TRL-Bench: Standardizing Cross-Paradigm Representation-Level Evaluation of Tabular Encoders

[官方论文页](https://neurips.cc/virtual/2026/poster/139385) · [作者来源](https://openreview.net/forum?id=TkwRxfihFM)

- **问题 / 瓶颈** · 端到端专用流水线混入模型以外变化。
- **核心创新 / 方法** · 导出行、列、表表示，共享任务头。
- **Baseline** · 各训练范式原专用模型。
- **Benchmark** · TRL-Bench 20 模型 16 任务，含组合表增强。
- **关键结果 / 消融** · 形成跨范式可比测试，具体差异待核。
- **适用条件 / 局限** · 各包装器支持程度不同。

**可复用机制** · 比较基座表示前先固定下游读出能力。

<a id="paper-156044"></a>

## Tropical Boundary Complexity of Deep ReLU Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/156044) · [作者来源](https://openreview.net/forum?id=0pa5znZWZc)

- **问题 / 瓶颈** · 激活方差不能说明分类边界如何变化。
- **核心创新 / 方法** · 推随机高斯网络边界穿越与生成矩阵递推。
- **Baseline** · 不同初始化尺度。
- **Benchmark** · 二分类理论和 Monte Carlo。
- **关键结果 / 消融** · He 方差是保持该复杂度的唯一均匀尺度。
- **适用条件 / 局限** · 依赖初始化和高斯二类设定。

**可复用机制** · 分类初始化用任务相关边界指标补充方差传播。

<a id="paper-156769"></a>

## TropNNC: Structured Neural Network Compression Using Tropical Geometry

[官方论文页](https://neurips.cc/virtual/2026/poster/156769) · [作者来源](https://openreview.net/forum?id=u7DRq1icmY)

- **问题 / 瓶颈** · 常规筛选或需样本补偿。
- **核心创新 / 方法** · 把 ReLU 网络表示成热带有理函数，归并并适配保留神经元权重。
- **Baseline** · ThiNet、CUP。
- **Benchmark** · MNIST、CIFAR、ImageNet。
- **关键结果 / 消融** · 与强基线相近，理论界更紧。
- **适用条件 / 局限** · 依赖 ReLU 型架构。

**可复用机制** · 先找结构同类，再用权重补偿减剪枝误差。

<a id="paper-152325"></a>

## Truncate Bad, Upweight Good: BoN-Style Distillation via Rank-Based Classification

[官方论文页](https://neurips.cc/virtual/2026/poster/152325) · [作者来源](https://openreview.net/forum?id=TunY4IfXnt)

- **问题 / 瓶颈** · 全候选降权留下较差分布支持。
- **核心创新 / 方法** · 仅保排名上尾并调其内部权重。
- **Baseline** · 常规排名加权与强蒸馏。
- **Benchmark** · 奖励排序生成。
- **关键结果 / 消融** · 某些前提下截断可匹配最优单调重权。
- **适用条件 / 局限** · 极度依赖排名可信度。

**可复用机制** · 在相同训练预算对照硬去除坏样本和软降权。

<a id="paper-153518"></a>

## Truncated Riemannian (1+1)-ES for Black-Box Optimization with Intrinsic Dimension Guarantees

[官方论文页](https://neurips.cc/virtual/2026/poster/153518) · [作者来源](https://openreview.net/forum?id=KlMraKGdCH)

- **问题 / 瓶颈** · 环境维度大时浪费评估。
- **核心创新 / 方法** · 截断 Riemannian (1+1)-ES。
- **Baseline** · 无约束演化或不同截断。
- **Benchmark** · 球面稀疏 PCA 和黑盒优化。
- **关键结果 / 消融** · 证明近 ε⁻⁴ 非凸零阶率，实证支持。
- **适用条件 / 局限** · 需紧子流形及适当半径。

**可复用机制** · 把参数维度和搜索可达维度分开配置。

<a id="paper-148418"></a>

## TrunkFish: Making Model Width Incrementally Refinable

[官方论文页](https://neurips.cc/virtual/2026/poster/148418) · [作者来源](https://openreview.net/forum?id=xy4Di1S8IP)

- **问题 / 瓶颈** · 独立训练宽度层级贵。
- **核心创新 / 方法** · 隐藏维做因果依赖并保累积前缀读出。
- **Baseline** · 独立训练宽度集。
- **Benchmark** · 匹配 FLOPs 的验证损失与实际参数。
- **关键结果 / 消融** · 多宽度前沿改善，层级训练耗算减少。
- **适用条件 / 局限** · 前缀不访问后维可能影响表达。

**可复用机制** · 需在线伸缩的模型将依赖方向与资源档位共同设计。

<a id="paper-148510"></a>

## Trust, but Don’t Verify: Epistemic Blind Spots in LLM Source Evaluation

[官方论文页](https://neurips.cc/virtual/2026/poster/148510) · [作者来源](https://openreview.net/forum?id=xJwWlVv9wz)

- **问题 / 瓶颈** · 模型单测识假，但合成时可能不用判断。
- **核心创新 / 方法** · 对照独立有效性识别和联合估计。
- **Baseline** · 有效与伪造报告。
- **Benchmark** · 五模型、三家族及三专业域。
- **关键结果 / 消融** · 独立识别 0.76–1.00，进入合成后类似加权。
- **适用条件 / 局限** · 设置依赖来源格式。

**可复用机制** · 给证据核验独立关卡而非将其藏进生成。

<a id="paper-149919"></a>

## TrustFlow: Adaptive Trust Calibration for Language Model Guided Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149919) · [作者来源](https://openreview.net/forum?id=mDpGbO5PSA)

- **问题 / 瓶颈** · 固定调用可冗余甚至损害性能。
- **核心创新 / 方法** · 自适应可信度调价值对齐和偏好更新。
- **Baseline** · 不调整的 LLM 指导。
- **Benchmark** · 强化学习样本效率和上线依赖。
- **关键结果 / 消融** · 样本效率有提升且最终可独立运行。
- **适用条件 / 局限** · 需能估当前指导价值。

**可复用机制** · 把教师当可退出的训练辅助，验证撤掉后的效用。

<a id="paper-151852"></a>

## Trust Guided Decision Transformer

[官方论文页](https://neurips.cc/virtual/2026/poster/151852) · [作者来源](https://openreview.net/forum?id=XQWFbB5mIO)

- **问题 / 瓶颈** · 离线策略偏移会令长前缀持续误导。
- **核心创新 / 方法** · 对多个后缀做 conformal 校准并选择。
- **Baseline** · 状态预测、critic、硬重置。
- **Benchmark** · D4RL 导航和运动。
- **关键结果 / 消融** · 减少连续高误差，具体回报待核。
- **适用条件 / 局限** · 离线留出分布与部署漂移影响保证。

**可复用机制** · 检测上下文过期后先替换证据，再进行规划。

<a id="paper-139646"></a>

## TrustMod-SM: A Multi-Axis Benchmark for Evaluating Trustworthiness of LLMs in Social Media Content Moderation

[官方论文页](https://neurips.cc/virtual/2026/poster/139646) · [作者来源](https://openreview.net/forum?id=DYd5QgYXPw)

- **问题 / 瓶颈** · 准确率掩盖群体和情境错误。
- **核心创新 / 方法** · 统一五轴测试公信、公平、安全、鲁棒和上下文。
- **Baseline** · 十三个多模态和文本基座。
- **Benchmark** · TrustMod-SM 约 29000 项、八来源。
- **关键结果 / 消融** · 摘要指出存在系统性权衡，幅度待核。
- **适用条件 / 局限** · 真实规则和语言分布需重新验证。

**可复用机制** · 同时设公平和上下文最低阈值。

<a id="paper-148571"></a>

## Trust Region Continual Learning as an Implicit Meta-Learner

[官方论文页](https://neurips.cc/virtual/2026/poster/148571) · [作者来源](https://openreview.net/forum?id=wrirlNfjM9)

- **问题 / 瓶颈** · 两者合并时难判断在持续学习中的职责。
- **核心创新 / 方法** · 用单步隐式 MAML 近似解释信赖域更新。
- **Baseline** · 无重放或无曲率惩罚。
- **Benchmark** · 局部更新理论和持续学习。
- **关键结果 / 消融** · 得到元学习形式，实证幅度待核。
- **适用条件 / 局限** · 只在局部近似成立。

**可复用机制** · 调稳定性时分别消融旧样本和曲率估计。

<a id="paper-150346"></a>

## Trust Region Policy Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/150346) · [作者来源](https://openreview.net/forum?id=ioYRAhS4qE)

- **问题 / 瓶颈** · 原 OPD 梯度方差高。
- **核心创新 / 方法** · 动态构造近教师，设信赖域改进。
- **Baseline** · 常规 OPD。
- **Benchmark** · 数学推理和收敛分析。
- **关键结果 / 消融** · 提升稳定和样本效率，无额外计算。
- **适用条件 / 局限** · 近端构造需保真正教师能力。

**可复用机制** · 以教师学生差异配更新步幅。

<a id="paper-149711"></a>

## Trust Region Q Adjoint Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/149711) · [作者来源](https://openreview.net/forum?id=o0QcqHlW1x)

- **问题 / 瓶颈** · 病态 critic 放大小误差。
- **核心创新 / 方法** · 用投影对偶下降选控制系数与闭式 KL。
- **Baseline** · QAM。
- **Benchmark** · 预训练流策略的离策略微调。
- **关键结果 / 消融** · 摘要给精确偏离控制，具体实证幅度待核。
- **适用条件 / 局限** · 需随机控制公式及 critic 覆盖。

**可复用机制** · 控制完整动作路径偏离而非只限输出动作。

<a id="paper-151603"></a>

## Trust the Direction, Search the Step: Zero-and-First-Order Methods for LLM Fine-Tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/151603) · [作者来源](https://openreview.net/forum?id=ZKbACxi4Qb)

- **问题 / 瓶颈** · 固定学习率没有利用当前位置曲率。
- **核心创新 / 方法** · 用两次额外函数评估拟合局部方向模型并限域选步。
- **Baseline** · 标准一阶微调。
- **Benchmark** · 多语言模型及微调数据。
- **关键结果 / 消融** · 摘要报告精度和稳定性提高。
- **适用条件 / 局限** · 有额外前向成本，理论只保证到驻点邻域。

**可复用机制** · 方向可用但步长难调时，将昂贵多维搜索限制在当前梯度提出的一维线上。

<a id="paper-152130"></a>

## Trust What Matters: Language-Conditioned Evidence Routing for Video-IMU Action Question Answering

[官方论文页](https://neurips.cc/virtual/2026/poster/152130) · [作者来源](https://openreview.net/forum?id=VHtWvUUYvP)

- **问题 / 瓶颈** · 固定融合会混入未同步或有偏的物理观测。
- **核心创新 / 方法** · 结构化组织各模态证据再传入语言模型。
- **Baseline** · 固定传感器融合。
- **Benchmark** · 视频和 IMU 动作问答。
- **关键结果 / 消融** · 摘要报告支持面向问题的可信证据路由。
- **适用条件 / 局限** · 依赖可靠性估计，摘要未给消融数值。

**可复用机制** · 多读数冲突时先确定该问题需要哪些模态，再依据质量决定如何使用。

<a id="paper-151724"></a>

## Trustworthy and Efficient Map-free LiDAR Localization via Scan-Pose Alignment and Flow Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/151724) · [作者来源](https://openreview.net/forum?id=Ya8vDuIkP4)

- **问题 / 瓶颈** · 直接读出定位模型置信度可能漏报错误。
- **核心创新 / 方法** · 训练扫描与位姿的嵌入对齐并评估置信。
- **Baseline** · 各定位骨干及其原始输出。
- **Benchmark** · 无地图 LiDAR 重定位准确性、耗时和失败检测。
- **关键结果 / 消融** · 摘要报告跨系统有效。
- **适用条件 / 局限** · 依赖可取得原始扫描，摘要未给失效边界。

**可复用机制** · 姿态估计可另训一个观测一致性模型，分开验证猜测和置信度。

<a id="paper-151250"></a>

## Truth as a Compression Artifact in Language Model Training

[官方论文页](https://neurips.cc/virtual/2026/poster/151250) · [作者来源](https://openreview.net/forum?id=bmm89qsE0w)

- **问题 / 瓶颈** · 同样有错误数据时，模型偏好可能受简洁规则而非真实性驱动。
- **核心创新 / 方法** · 控制真假答案及错误规则数量，随模型规模比较。
- **Baseline** · 随机错误、单一替代规则和两种冲突替代。
- **Benchmark** · 受控冲突语料的正确答案偏好。
- **关键结果 / 消融** · 随机错误时偏好 65% 到 85%，单规则时约 45% 至 51%。
- **适用条件 / 局限** · 限合成环境，压缩解释是作者假说。

**可复用机制** · 数据质量审查要找成体系的错误，不能只测错标比例。

<a id="paper-149426"></a>

## Truthful Calibration Errors for Multi-Class Prediction

[官方论文页](https://neurips.cc/virtual/2026/poster/149426) · [作者来源](https://openreview.net/forum?id=q98y9pHu2F)

- **问题 / 瓶颈** · 普通经验校准分数可能因改概率或换分箱翻转排序。
- **核心创新 / 方法** · 构造真实报告最优的完整和逐类校准指标。
- **Baseline** · 基于置信的分箱误差。
- **Benchmark** · 多分类校准排序及分箱鲁棒性。
- **关键结果 / 消融** · 摘要报告逐类方法相对稳定。
- **适用条件 / 局限** · 摘要未给全部任务设定及样本复杂度。

**可复用机制** · 比较校准前验证评分规则不会以人为扭曲概率获得更高分。

<a id="paper-149079"></a>

## TSFM Meets LLM: Context as Covariate

[官方论文页](https://neurips.cc/virtual/2026/poster/149079) · [作者来源](https://openreview.net/forum?id=t2nNTWgHfq)

- **问题 / 瓶颈** · 直接让语言模型预测数值会丢掉专用预测先验。
- **核心创新 / 方法** · 用语言模型提取协变量，训练或调用时序基础模型。
- **Baseline** · Chronos 等预测模型和 GPT-4o。
- **Benchmark** · 交通及其他外部事件时序场景，以 MAE 衡量。
- **关键结果 / 消融** · Qwen3-4B 与 Chronos2 组合最多改善约 12% MAE。
- **适用条件 / 局限** · 依赖真实文本可在预测时获取，摘要未给泄漏对照。

**可复用机制** · 将语言模型用于信息提取，将数值建模交给有时序归纳偏置的网络。

<a id="paper-148825"></a>

## TS-ICL: A Flexible Time-Indexed Foundation Model for Time Series via In-Context Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/148825) · [作者来源](https://openreview.net/forum?id=urL7kBfWB5)

- **问题 / 瓶颈** · 固定位置序列接口不适合缺测和任意查询。
- **核心创新 / 方法** · 在合成因果依赖上训练概率上下文回归。
- **Baseline** · 单变量与协变量预测对照。
- **Benchmark** · 时序预测和补全，含缺失历史窗。
- **关键结果 / 消融** · 摘要报告历史缺测时优势尤其明显。
- **适用条件 / 局限** · 依赖合成结构覆盖，摘要未列模型与分布限制。

**可复用机制** · 将时间点作为独立查询输入，使一个模型处理未来预测和缺值恢复。

<a id="paper-138953"></a>

## TSNBench: Benchmarking LLM Proficiency in Time-Sensitive Networking

[官方论文页](https://neurips.cc/virtual/2026/poster/138953) · [作者来源](https://openreview.net/forum?id=uDgeZcptTR)

- **问题 / 瓶颈** · 选择题可通过识别正确候选，开放配置会暴露超预算。
- **核心创新 / 方法** · 对时间敏感网络做专家题与可计算延迟对照。
- **Baseline** · 不同语言模型和题型。
- **Benchmark** · 939 道选择题、100 道最坏延迟任务。
- **关键结果 / 消融** · 摘要指出选择题能力会高估实际配置可靠性。
- **适用条件 / 局限** · 限具体网络机制，摘要未给通用计算误差。

**可复用机制** · 安全关键任务应执行验证可用配置，避免只测概念识记。

<a id="paper-149443"></a>

## TStruct: Learning Shared Temporal Structures for Long-Term Time-Series Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/149443) · [作者来源](https://openreview.net/forum?id=q3fXT85cph)

- **问题 / 瓶颈** · 独立拟合时间关系浪费共享规律。
- **核心创新 / 方法** · 分析多个关系矩阵并提取反复出现的主结构。
- **Baseline** · 主流长程预测模型。
- **Benchmark** · 多长时序基准及计算效率。
- **关键结果 / 消融** · 摘要报告准确度和效率有优势。
- **适用条件 / 局限** · 摘要未给强非平稳时的失效量。

**可复用机制** · 固定预测结构前先跨变量和时段验证是否存在可共享的关系基底。

<a id="paper-154935"></a>

## TTB: Test-time MLP Baking for Efficient Rendering of Decoder-only View Synthesis Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154935) · [作者来源](https://openreview.net/forum?id=9pt0ng1IDx)

- **问题 / 瓶颈** · 完整注意力重复运行昂贵，直接替代又损质量。
- **核心创新 / 方法** · 在测试时以原注意力的输入输出对学习快速权重。
- **Baseline** · 常规 TTT 及现有新视图模型。
- **Benchmark** · 新视图渲染质量与速度。
- **关键结果 / 消融** · 渲染最多快 23 倍且质量相当。
- **适用条件 / 局限** · 需要一次拟合成本和足够复用次数。

**可复用机制** · 高代价模块反复在相近场景上运行时，可把计算蒸馏成场景专用快速映射。

<a id="paper-154339"></a>

## TTVidT: Decoupling the Temporal Axis for Efficient Motion-Centric Video Pretraining

[官方论文页](https://neurips.cc/virtual/2026/poster/154339) · [作者来源](https://openreview.net/forum?id=ELiMecKQps)

- **问题 / 瓶颈** · 大型联合编码器重算每帧静态结构。
- **核心创新 / 方法** · 以冻结初始化的逐帧空间路径配轻量时间层，学习重建帧差。
- **Baseline** · DisMo、VideoMAE、V-JEPA 2 等。
- **Benchmark** · HMDB51、IARD、EPIC-Kitchens。
- **关键结果 / 消融** · 比列出的重型对照少约 48% 至 55% 编码 FLOPs。
- **适用条件 / 局限** · 实证限所测尺度和动作数据。

**可复用机制** · 运动任务优先使用变化目标训练时间模块，保留已有空间编码。

<a id="paper-155978"></a>

## TUBE: Tangent Upper Bound on Evidence for Discrete Diffusion Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155978) · [作者来源](https://openreview.net/forum?id=1P9BKutXbt)

- **问题 / 瓶颈** · 下界差同时包含模型误差和界不紧。
- **核心创新 / 方法** · 通过切线上界构造无偏蒙特卡洛估计。
- **Baseline** · 精确自回归似然。
- **Benchmark** · 块掩码扩散及乱序自回归。
- **关键结果 / 消融** · 摘要报告所测模型似然仍低于基线。
- **适用条件 / 局限** · 依赖边界估计，不能外推到全部推理能力。

**可复用机制** · 比较潜变量生成时同时看上下界，避免误把估计偏差当模型能力差。

<a id="paper-154633"></a>

## Tuna-2: Pixel Embeddings Beat Vision Encoders for Multimodal Understanding and Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/154633) · [作者来源](https://openreview.net/forum?id=C9czc9fdwn)

- **问题 / 瓶颈** · 独立视觉编码器可能形成能力和适配瓶颈。
- **核心创新 / 方法** · 以简单图块嵌入训练端到端像素模型。
- **Baseline** · VAE 与表征编码器式多模态方案。
- **Benchmark** · 视觉生成和理解基准。
- **关键结果 / 消融** · 摘要报告多模态表现达到先进水平。
- **适用条件 / 局限** · 模型直训成本与尺度条件未报告。

**可复用机制** · 端到端多模态架构应保留轻视觉接口基线，以检验分模块设计真实收益。

<a id="paper-149979"></a>

## Tunable Latent Generative Priors for Compressed Sensing and Inverse Problems

[官方论文页](https://neurips.cc/virtual/2026/poster/149979) · [作者来源](https://openreview.net/forum?id=lkznuQI3gj)

- **问题 / 瓶颈** · 固定复杂度可能对稀观测过拟合或对丰富观测欠拟合。
- **核心创新 / 方法** · 用嵌套 dropout 训练可调潜表示。
- **Baseline** · 固定复杂度扩散、流和 VAE。
- **Benchmark** · 压缩感知、补全、去噪和相位恢复。
- **关键结果 / 消融** · 作者报告一致更低重建误差。
- **适用条件 / 局限** · 摘要未给自动选择规则的跨域准度。

**可复用机制** · 逆问题中的先验复杂度应随测量量和噪声变化，而不随模型总容量固定。

<a id="paper-153184"></a>

## Tuning the Tuner

[官方论文页](https://neurips.cc/virtual/2026/poster/153184) · [作者来源](https://openreview.net/forum?id=NBWT71jwtz)

- **问题 / 瓶颈** · 看单个最佳 PPO 分数忽略上层超参数和总体开销
- **核心创新 / 方法** · 改变 SMAC3 与 Hyperband 的外层配置并比较随机搜索
- **Baseline** · 随机搜索及直接 PPO 调参
- **Benchmark** · 多个环境的 PPO 调优；效果与额外算力
- **关键结果 / 消融** · 自动调参降低敏感度，逐环境收益没有超过随机搜索
- **适用条件 / 局限** · 仅验证具体调参器及 PPO

**可复用机制** · 先做同总计算预算的随机搜索，再决定是否加嵌套优化

<a id="paper-155650"></a>

## TwinFlux: One-Step Discrete-Continuous Flow for End-to-End Autonomous Driving

[官方论文页](https://neurips.cc/virtual/2026/poster/155650) · [作者来源](https://openreview.net/forum?id=41ua72BZf8)

- **问题 / 瓶颈** · 直接跳到终点可能遗漏子区间演化
- **核心创新 / 方法** · 让复原轨迹中直接位移与子区间累积相符
- **Baseline** · 近期端到端驾驶规划
- **Benchmark** · NAVSIMv1/v2，驾驶质量和推理实时性
- **关键结果 / 消融** · 摘要称性能领先且无额外推理开销
- **适用条件 / 局限** · 依赖轨迹重构空间和基准定义

**可复用机制** · 蒸馏快速规划器时检查每段合成是否等于一步输出

<a id="paper-151130"></a>

## TwinPrune: Density-Aware Two-Phase Token Pruning for Vision-Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151130) · [作者来源](https://openreview.net/forum?id=cmNvJykWg5)

- **问题 / 瓶颈** · 只测短简单任务可能掩盖解码损失
- **核心创新 / 方法** · 基于密度两阶段剪枝，并匹配保留率比较
- **Baseline** · H2O 等及未剪枝原模型
- **Benchmark** · TextVQA、MM-Vet、DocVQA 和 InternVL 模型族
- **关键结果 / 消融** · 12.5% 保留时 TextVQA 相对 H2O 高 9.6 个百分点
- **适用条件 / 局限** · 压缩曲线依赖生成长度和输入密度

**可复用机制** · 给解码压缩回归加入文档等全流程任务

<a id="paper-151270"></a>

## Two Drifts, One Principle: Conflict-Aware Spectral Consolidation for Multimodal Continual Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151270) · [作者来源](https://openreview.net/forum?id=bdROoNCzjt)

- **问题 / 瓶颈** · 固定秩下新旧技能会争用表示方向
- **核心创新 / 方法** · 用固定秩谱记忆保护既有主方向，吸收相容增量
- **Baseline** · 其他多模态持续学习方法
- **Benchmark** · 多模态持续学习，任务细目未报告
- **关键结果 / 消融** · 摘要报告无需回放或路由仍有效
- **适用条件 / 局限** · 依赖谱方向能刻画保留知识

**可复用机制** · 监控投影器与语言支路的漂移，并分别消融

<a id="paper-153140"></a>

## Two Layers of Attention Stability: A Koopman-Operator Analysis of Linear and Softmax Attention

[官方论文页](https://neurips.cc/virtual/2026/poster/153140) · [作者来源](https://openreview.net/forum?id=NakvgMzgsK)

- **问题 / 瓶颈** · 谱半径有界不足以保证轨迹各步不扩大
- **核心创新 / 方法** · 分析线性注意的算子稳定并以 softmax 行归一化为强约束对照
- **Baseline** · 原线性注意及 softmax
- **Benchmark** · ETT、Weather 等长期序列
- **关键结果 / 消融** · 填补至少 80% 差距，五项中三项长程超过 softmax
- **适用条件 / 局限** · 保证与评测任务的动态条件有关

**可复用机制** · 给世界模型检查误差最大范数而不只看整体谱

<a id="paper-149214"></a>

## Two-Level Softmax Sampling Done Right: Correcting Bias from Size Imbalance and Dispersion

[官方论文页](https://neurips.cc/virtual/2026/poster/149214) · [作者来源](https://openreview.net/forum?id=s3eaoMXlo8)

- **问题 / 瓶颈** · 先选组再选元素会偏向特定大小和离散程度
- **核心创新 / 方法** · 校正组权重以逼近原分布
- **Baseline** · 标准两级 softmax
- **Benchmark** · 五大数据集的采样性质
- **关键结果 / 消融** · 摘要称可忽略成本下分布近似更好
- **适用条件 / 局限** · 需要可估计组内统计

**可复用机制** · 量化采样选择前核对尾部 token 频率与组分布

<a id="paper-153791"></a>

## Two Speeds of Learning: A Representation-Readout Decomposition of Grokking and Double Descent

[官方论文页](https://neurips.cc/virtual/2026/poster/153791) · [作者来源](https://openreview.net/forum?id=Ie9GknsUHy)

- **问题 / 瓶颈** · 单看原预测头会误认迟发学习或过拟合
- **核心创新 / 方法** · 比较独立读出与原头随训练的对齐变化
- **Baseline** · 原模型读出及非标准训练配置
- **Benchmark** · MNIST grokking 和按轮双下降示例
- **关键结果 / 消融** · 表征退化与读出错配解释部分异常
- **适用条件 / 局限** · 现象来自受控例子

**可复用机制** · 冻结特征重训轻头并比较恢复幅度

<a id="paper-153347"></a>

## UECO: A Unified Encoder with Structure-Aware Attention Mixture via Iterative Edge Evolving for Neural Combinatorial Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/153347) · [作者来源](https://openreview.net/forum?id=M2lqt23VO7)

- **问题 / 瓶颈** · 各任务各骨干使方法比较混杂。
- **核心创新 / 方法** · 交错轻量局部图模块和全局节点注意，迭代更新边。
- **Baseline** · 特化神经组合骨架。
- **Benchmark** · 不同范式和组合任务。
- **关键结果 / 消融** · 摘要报告通用性证据，数值待核。
- **适用条件 / 局限** · 局部边构造决定泛化。

**可复用机制** · 将特有拓扑注入共享编码、保留公平骨架对照。

<a id="paper-155759"></a>

## UFO: A Unified Flow-Oriented Framework for Robust Continual Graph Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/155759) · [作者来源](https://openreview.net/forum?id=38kpqzHh0B)

- **问题 / 瓶颈** · 重放会强化历史错误。
- **核心创新 / 方法** · 条件流产生可重放表示，不存原样本。
- **Baseline** · 常规图持续学习。
- **Benchmark** · 四图基准及标签噪声比，正确率和遗忘。
- **关键结果 / 消融** · 两指标一致改善。
- **适用条件 / 局限** · 生成重放仍可能继承噪声，须筛。

**可复用机制** · 保留率上升时查保留的是正确还是错误记忆。

<a id="paper-154876"></a>

## UGGRH: Unsupervised Generative Completion and Graph-attention Refinement for Incomplete Cross-modal Hashing

[官方论文页](https://neurips.cc/virtual/2026/poster/154876) · [作者来源](https://openreview.net/forum?id=ADX5uP0Pe4)

- **问题 / 瓶颈** · 高缺失和不平衡让哈希相似变形。
- **核心创新 / 方法** · 无监督生成补全结合图注意力细化。
- **Baseline** · 常规不完整跨模态哈希。
- **Benchmark** · MIRFlickr25K、NUS-WIDE、MS COCO。
- **关键结果 / 消融** · 缺失及不平衡条件均提高检索。
- **适用条件 / 局限** · 补全错误可能随图传播。

**可复用机制** · 用跨样本邻域验虚拟模态，不直接信任补全。

<a id="paper-152769"></a>

## UGO: Unified Architecture for General Multi-Object Tracking by Segmentation

[官方论文页](https://neurips.cc/virtual/2026/poster/152769) · [作者来源](https://openreview.net/forum?id=QWQDuX9NHf)

- **问题 / 瓶颈** · 只靠检测召回不足以保持长期身份。
- **核心创新 / 方法** · 共享示例检测和实例传播，用层级管理记忆。
- **Baseline** · 现有多对象追踪。
- **Benchmark** · 实例掩码、跟踪召回。
- **关键结果 / 消融** · 摘要称两类指标提升，数值未核。
- **适用条件 / 局限** · 记忆容量与错误身份更新需验。

**可复用机制** · 分别存场景候选和对象历史，独立控制淘汰。

<a id="paper-150314"></a>

## UltraDiff:Transferring High-Fidelity Priors to Compressed Latent Spaces for High-resolution Image Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/150314) · [作者来源](https://openreview.net/forum?id=j164YLIssM)

- **问题 / 瓶颈** · 低码率生成存在多义性。
- **核心创新 / 方法** · 双分支 DiT 共享注意，蒸馏 f32 原生向量场。
- **Baseline** · f8 与直接 f32。
- **Benchmark** · 高分辨率图像生成。
- **关键结果 / 消融** · 摘要明确机制，幅度待核。
- **适用条件 / 局限** · 依赖老师同时覆盖两种编码。

**可复用机制** · 从高保真证据借训练信号但让学生在真实部署坐标学习。

<a id="paper-156029"></a>

## Ultra-DPO: Reimagining LLM Alignment as a Semi-Supervised Task

[官方论文页](https://neurips.cc/virtual/2026/poster/156029) · [作者来源](https://openreview.net/forum?id=11tDIVzbAR)

- **问题 / 瓶颈** · DPO 越出支持会退化，RLHF 奖励外推也会偏。
- **核心创新 / 方法** · 用半监督目标以人类偏好定锚，并用新采样扩展。
- **Baseline** · DPO、RLHF。
- **Benchmark** · 对齐分布和监督来源分析。
- **关键结果 / 消融** · 解释各自的结构失效，数值待核。
- **适用条件 / 局限** · 需确定何处离线支持足够。

**可复用机制** · 给外推伪标签单独验证风险。

<a id="paper-151853"></a>

## Ultra Fast PDE Solving via Physics Guided Few-step Diffusion

[官方论文页](https://neurips.cc/virtual/2026/poster/151853) · [作者来源](https://openreview.net/forum?id=XQGamZ3x8F)

- **问题 / 瓶颈** · 只匹配扩散分布不保物理条件。
- **核心创新 / 方法** · 将教师分布匹配及 PDE 引导联合。
- **Baseline** · 多步扩散及常规蒸馏。
- **Benchmark** · PDE 与下游条件推断。
- **关键结果 / 消融** · 少步保快速采样和一致性，幅度未核。
- **适用条件 / 局限** · 方程可微性和边界可用性重要。

**可复用机制** · 蒸馏物理模型应独立评精度和规律残差。

<a id="paper-154462"></a>

## UltraFlash: Accelerating Megapixel Visual Synthesis

[官方论文页](https://neurips.cc/virtual/2026/poster/154462) · [作者来源](https://openreview.net/forum?id=DPPXv0wQVk)

- **问题 / 瓶颈** · 提速去噪后阶段间仍重复 RGB 往返。
- **核心创新 / 方法** · 优化级联分辨率过渡和最终重叠解码。
- **Baseline** · 只减少扩散去噪。
- **Benchmark** · 级联图像分辨率、保真和速度。
- **关键结果 / 消融** · 过渡优化可改善两指标，确数待核。
- **适用条件 / 局限** · 实益依流水线和 VAE。

**可复用机制** · 分析生成瓶颈须计跨表示复制，不只计主干 FLOPs。

<a id="paper-153259"></a>

## Ultra Flash: Scaling Real-Time Streaming Video Generation to High Resolutions

[官方论文页](https://neurips.cc/virtual/2026/poster/153259) · [作者来源](https://openreview.net/forum?id=Mb3tl1Magj)

- **问题 / 瓶颈** · 直接全分辨推理缓慢。
- **核心创新 / 方法** · 保持生成架构，训练视频超分，接因果上采样和高分解码。
- **Baseline** · 低分辨生成与标准非流式超分。
- **Benchmark** · 单 B200 的 1K、2K 视频。
- **关键结果 / 消融** · 约 30 和 18 FPS。
- **适用条件 / 局限** · 端到端吞吐受基座与硬件限制。

**可复用机制** · 在级联系统分别测生成延迟及放大后的时序稳定。

<a id="paper-153643"></a>

## UltraVoxelGS: Voxel-First Feed-Forward Gaussian Splatting for 3D Ultrasound Reconstruction

[官方论文页](https://neurips.cc/virtual/2026/poster/153643) · [作者来源](https://openreview.net/forum?id=Jo1hZK6YQ8)

- **问题 / 瓶颈** · 按片堆高斯导致表示膨胀。
- **核心创新 / 方法** · 投影切片到固定体素，前馈预测高斯，并分解成像反射衰减。
- **Baseline** · 逐片生成和标准 GS。
- **Benchmark** · 3D 超声重建。
- **关键结果 / 消融** · 固定表示规模、适配外观，数值待核。
- **适用条件 / 局限** · 需已有切片位姿，成像模型领域特化。

**可复用机制** · 固定空间容量把数据量增长从表示规模中解耦。

<a id="paper-148275"></a>

## UMAS: System-Level Uncertainty Quantification for Multi-Agent LLM Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/148275) · [作者来源](https://openreview.net/forum?id=z4D5fgtmEo)

- **问题 / 瓶颈** · 平均置信忽略信息传递链。
- **核心创新 / 方法** · 内生生成置信估跨代理影响，无参数。
- **Baseline** · 其他多代理不确定性。
- **Benchmark** · Debate、DyLAN 及多基准。
- **关键结果 / 消融** · AUROC 平均加 10.49 点。
- **适用条件 / 局限** · 内生置信可能共同偏差。

**可复用机制** · 在拒答策略中区分成员可靠和传播可信。

<a id="paper-150927"></a>

## Umbilic Multinomial Logistic Regression

[官方论文页](https://neurips.cc/virtual/2026/poster/150927) · [作者来源](https://openreview.net/forum?id=eJ5eydjNyT)

- **问题 / 瓶颈** · 默认线性或零半径原型不能调边界形状。
- **核心创新 / 方法** · 以有符距离统一并学半径。
- **Baseline** · 多项逻辑回归和原型。
- **Benchmark** · 低样本视觉、原型和混合头。
- **关键结果 / 消融** · 实验支持按数据状态选边界。
- **适用条件 / 局限** · 需校准不同形状得分尺度。

**可复用机制** · 先决定类簇是否周围有外类，再选边界几何。

<a id="paper-150452"></a>

## U-MOF: Uncertainty-Guided Parameter-Efficient Multi-Objective Fine-Tuning for Long-Tailed Recognition

[官方论文页](https://neurips.cc/virtual/2026/poster/150452) · [作者来源](https://openreview.net/forum?id=hwDAQJu6Fl)

- **问题 / 瓶颈** · 固定混合权重难兼顾尾部与总体。
- **核心创新 / 方法** · 轻量残差头，按委员会熵调目标，正交投影协调。
- **Baseline** · 第二阶段训练及已发表强方法。
- **Benchmark** · CIFAR-100-LT、ImageNet-LT、iNat 2018。
- **关键结果 / 消融** · 稀有与整体表现均改善。
- **适用条件 / 局限** · 置信代理和冲突投影需消融。

**可复用机制** · 将进步需求与实际各损失更新方向共同考虑。

<a id="paper-155292"></a>

## U-MVP: Encode Locally, Decode Globally for Feed-Forward 3D Gaussian Splatting

[官方论文页](https://neurips.cc/virtual/2026/poster/155292) · [作者来源](https://openreview.net/forum?id=6exwb0yaJa)

- **问题 / 瓶颈** · 过早全局融合会丢单视外观。
- **核心创新 / 方法** · 视内注意编码、跨视解码及 U 形跳接。
- **Baseline** · 前馈和优化式 3DGS。
- **Benchmark** · 16 至 256 视图，含有位姿和无位姿。
- **关键结果 / 消融** · 域外重建和新视角具有竞争力。
- **适用条件 / 局限** · 视图密度及遮挡差异需测。

**可复用机制** · 分开维护局部图像信息和跨视任务匹配。

<a id="paper-148480"></a>

## Unaligned Image Guided Denoising via Cross-modal Conditional Flow Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/148480) · [作者来源](https://openreview.net/forum?id=xUc5mPpRrP)

- **问题 / 瓶颈** · 全步训练和小步部署错配。
- **核心创新 / 方法** · 任务阶段聚焦损失和自适应稀疏匹配。
- **Baseline** · 已有去噪与单图底座。
- **Benchmark** · 跨模态引导，一或两步。
- **关键结果 / 消融** · 摘要称少步领先。
- **适用条件 / 局限** · 误配风险需随几何偏移评估。

**可复用机制** · 控制少步的监督落在部署真正经历的阶段。

<a id="paper-150375"></a>

## Unbiased First-Order Randomized Smoothing for Differentiable Simulation

[官方论文页](https://neurips.cc/virtual/2026/poster/150375) · [作者来源](https://openreview.net/forum?id=iXltG66DNN)

- **问题 / 瓶颈** · 普通一阶平滑梯度漏跳跃贡献。
- **核心创新 / 方法** · 已知边界时校正，未知时融合经典梯度降方差。
- **Baseline** · 零阶及普通一阶。
- **Benchmark** · 碰撞和非光滑轨迹优化。
- **关键结果 / 消融** · 保持无偏且方差低数个数量级。
- **适用条件 / 局限** · 需验证跳跃边界及平滑选择。

**可复用机制** · 在接触控制中先查梯度偏差，再比较优化速度。

<a id="paper-149144"></a>

## Unbounded Streaming Text-To-Speech with Prefixed Sliding Window Attention

[官方论文页](https://neurips.cc/virtual/2026/poster/149144) · [作者来源](https://openreview.net/forum?id=sVwnrFCMYb)

- **问题 / 瓶颈** · 长训练上下文仍会积错且耗内存。
- **核心创新 / 方法** · 解码前缀滑窗及交叉注意滑窗。
- **Baseline** · 依赖小时级训练上下文的模型。
- **Benchmark** · 短篇和小时长连续合成。
- **关键结果 / 消融** · 仅训练不足 30 秒片段可长时合成，逐步成本线性。
- **适用条件 / 局限** · 不同语言和中途上下文变化需另测。

**可复用机制** · 在线序列以固定身份锚加可移局部窗口。

<a id="paper-156038"></a>

## Uncertainty as an Underconstrained Axis in Lossy Compression

[官方论文页](https://neurips.cc/virtual/2026/poster/156038) · [作者来源](https://openreview.net/forum?id=0tD46aY7z8)

- **问题 / 瓶颈** · 同样码率和总方差可能下游差距大。
- **核心创新 / 方法** · 定义条件重构方差并刻画码率失真不确定曲面。
- **Baseline** · 相同码率且标量不确定的重构。
- **Benchmark** · 同图下游分割，mIoU。
- **关键结果 / 消融** · 可差逾 40 点，88% 配对呈显著负斜率。
- **适用条件 / 局限** · 解析界依高斯线性设置。

**可复用机制** · 压缩应把误差预算让给决策不敏感区域。

<a id="paper-154574"></a>

## Uncertainty-Aware Listwise Reinforcement Fine-Tuning for Fine-Grained Visual Classification

[官方论文页](https://neurips.cc/virtual/2026/poster/154574) · [作者来源](https://openreview.net/forum?id=CYOjPaQTZA)

- **问题 / 瓶颈** · 单答案全对或全错会忽略同类近邻的有用信息。
- **核心创新 / 方法** · 用不确定感知的列表组相对更新训练候选。
- **Baseline** · 单答案的强化微调。
- **Benchmark** · 多个细粒度视觉基准，测 Top-1 和候选真值覆盖。
- **关键结果 / 消融** · 摘要报告 Top-1 提升并且平均约三候选就能维持高覆盖。
- **适用条件 / 局限** · 需要可信混淆邻域，摘要未给候选数敏感性。

**可复用机制** · 错误类别有自然邻近关系时，用有序候选反馈扩大训练信号，再保留严格单标签验收。

<a id="paper-154307"></a>

## Uncertainty-Aware Probabilistic Constrained Clustering from Entangled Pairwise Supervision

[官方论文页](https://neurips.cc/virtual/2026/poster/154307) · [作者来源](https://openreview.net/forum?id=EgwTOkzegp)

- **问题 / 瓶颈** · 几种观测机制的重叠会使强行划分错误。
- **核心创新 / 方法** · 在条件可辨识设定估计随机关系，并以角度目标及校正整合训练。
- **Baseline** · 已有深度约束聚类。
- **Benchmark** · 多个概率监督聚类数据及默认配置。
- **关键结果 / 消融** · 摘要报告优于基线且对配置稳健。
- **适用条件 / 局限** · 需要关系可辨识条件，摘要未给权重误差。

**可复用机制** · 将标签来源噪声与类别相似性分开，再决定用硬配对还是概率监督。

<a id="paper-149259"></a>

## Uncertainty Aware SURE Transfer Learning for Classification Problems

[官方论文页](https://neurips.cc/virtual/2026/poster/149259) · [作者来源](https://openreview.net/forum?id=rh6BZ4pWDJ)

- **问题 / 瓶颈** · 只看源模型分数可能让不相容来源负迁移。
- **核心创新 / 方法** · 用按坐标的稳健惩罚和研究级准则调迁移比重。
- **Baseline** · 普通迁移与单来源模型。
- **Benchmark** · 模拟及真实分类。
- **关键结果 / 消融** · 摘要报告相容源改善预测，不相容源权重下降。
- **适用条件 / 局限** · 依赖源系数与误差估计，摘要未给规模边界。

**可复用机制** · 融合多教师或数据域时，应按估计不确定性与相容性共同加权。

<a id="paper-148713"></a>

## Uncertainty Estimation for Pretrained Medical Image Registration Models via Transformation Equivariance

[官方论文页](https://neurips.cc/virtual/2026/poster/148713) · [作者来源](https://openreview.net/forum?id=vcFcWZeEEC)

- **问题 / 瓶颈** · 没有多个模型和标签时难以诊断失败。
- **核心创新 / 方法** · 利用坐标等变性带来的可核查关系，比较变换后对齐。
- **Baseline** · 已有配准模型和常规风险估计。
- **Benchmark** · 医学影像配准，摘要未给数据名。
- **关键结果 / 消融** · 摘要报告支持测试时风险估计。
- **适用条件 / 局限** · 依赖变换保留真实对应，摘要未给临床误报。

**可复用机制** · 当输出有已知变换规律时，可用等变误差给独立预测加可靠性检查。

<a id="paper-149046"></a>

## Uncertainty-Guided Reward Labeling for Reinforcement Learning under Limited Feedback

[官方论文页](https://neurips.cc/virtual/2026/poster/149046) · [作者来源](https://openreview.net/forum?id=tHUPLE3JIc)

- **问题 / 瓶颈** · 不保留已查询标签会浪费强化学习预算。
- **核心创新 / 方法** · 用不确定度引导下一项标注，拆开策略估计与奖励模型误差。
- **Baseline** · 完整反馈及其他低预算方法。
- **Benchmark** · 多个强化学习域与稀疏奖励反馈。
- **关键结果 / 消融** · 摘要报告少量标签接近全反馈。
- **适用条件 / 局限** · 依赖离线数据覆盖及不确定度质量。

**可复用机制** · 可重复使用的奖励标注应花在能最大幅度改善奖励估计的转移上。

<a id="paper-150791"></a>

## Uncertainty Quantification for Large Language Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150791) · [作者来源](https://openreview.net/forum?id=fNNb0OstQs)

- **问题 / 瓶颈** · 重复采样会抵消大语言扩散模型的推理效率。
- **核心创新 / 方法** · 以中间输出、重掩码频率和去噪复杂度构造免训练信号。
- **Baseline** · 重复采样的不确定度估计。
- **Benchmark** · 语言扩散模型和幻觉检测。
- **关键结果 / 消融** · 摘要报告开销最多低百倍且检测有竞争力。
- **适用条件 / 局限** · 需访问内部去噪，摘要未列绝对延迟。

**可复用机制** · 迭代生成模型可先用自然产生的中间步做置信估计，再考虑重复运行。

<a id="paper-152113"></a>

## Uncertainty Quantification for Multimodal Large Language Models with Incoherence-adjusted Semantic Volume

[官方论文页](https://neurips.cc/virtual/2026/poster/152113) · [作者来源](https://openreview.net/forum?id=VRTV8c5uuB)

- **问题 / 瓶颈** · 依赖外部评估器或只处理文本限制部署。
- **核心创新 / 方法** · 对模型内部多模态特征计算不相干性调整的语义体积。
- **Baseline** · 其他免训练不确定估计。
- **Benchmark** · 图像、音频、视频文本及非文本生成。
- **关键结果 / 消融** · 摘要报告跨输入输出模式可用。
- **适用条件 / 局限** · 需访问表征，摘要未给设备开销。

**可复用机制** · 多模态可靠性估计应跨输入输出类型验证，无需强制把所有内容先转文本。

<a id="paper-148612"></a>

## Uncovering and Shaping the Latent Representation of 3D Scene Topology in Vision-Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148612) · [作者来源](https://openreview.net/forum?id=wSSsA6iviw)

- **问题 / 瓶颈** · 颜色和外形显眼时可能淹没拓扑信号。
- **核心创新 / 方法** · 跨场景提取空间子空间，验证因果影响后以合成空间监督塑形。
- **Baseline** · 标准 SFT 和其他空间训练。
- **Benchmark** · 真实三维场景拓扑任务。
- **关键结果 / 消融** · 较对照最高改善 12.1%。
- **适用条件 / 局限** · 依赖空间可线性分离和合成数据覆盖。

**可复用机制** · 训练具身表征之前可检测空间内容是缺失还是被更强外观信号遮蔽。

<a id="paper-149167"></a>

## Uncovering Hidden Propensities in Language Models via Limited-Parameter Finetuning

[官方论文页](https://neurips.cc/virtual/2026/poster/149167) · [作者来源](https://openreview.net/forum?id=sMHHHiNe0M)

- **问题 / 瓶颈** · 静态行为等效可能掩盖不同的可激发倾向。
- **核心创新 / 方法** · 采用有限参数微调作行为敏感性测试并比较组别。
- **Baseline** · 初始行为测试。
- **Benchmark** · 8B 至 14B 已知倾向模型和 27B 至 32B 开放模型。
- **关键结果 / 消融** · 摘要报告可以区分表面行为类似的模型。
- **适用条件 / 局限** · 适配可能引入新行为，需独立控制因果解释。

**可复用机制** · 模型安全评估可将对小参数改动的稳定性作为额外指标，不只测固定权重行为。

<a id="paper-152608"></a>

## Uncovering the latent structure of interwoven population and temporal codes

[官方论文页](https://neurips.cc/virtual/2026/poster/152608) · [作者来源](https://openreview.net/forum?id=RqtKLn3TDs)

- **问题 / 瓶颈** · 仅使用频率可能遮盖潜在结构。
- **核心创新 / 方法** · 拟合能联合解释群体和爆发的潜变量。
- **Baseline** · 仅靠放电率的分析。
- **Benchmark** · 模拟和实验神经记录。
- **关键结果 / 消融** · 摘要报告恢复只看频率会遗漏的潜在因素。
- **适用条件 / 局限** · 限所测数据和神经信号模型。

**可复用机制** · 当点过程事件具有聚簇结构时，频率和时序应分别检验可预测信息。

<a id="paper-149596"></a>

## Understanding and Defending VLM Jailbreaks via Jailbreak-Related Representation Shift

[官方论文页](https://neurips.cc/virtual/2026/poster/149596) · [作者来源](https://openreview.net/forum?id=ovIB52cIlw)

- **问题 / 瓶颈** · 输入模态改变后，能识别风险的模型仍可能不做拒绝。
- **核心创新 / 方法** · 评估表征偏移与安全决策，并用防护干预核对。
- **Baseline** · 普通多模态安全策略。
- **Benchmark** · 不同安全场景及良性任务。
- **关键结果 / 消融** · 摘要报告安全改善且保留效用。
- **适用条件 / 局限** · 机制是所测模型中的解释，摘要未给部署外推。

**可复用机制** · 测试多模态防护时应同时测模型识别层和实际响应，减少只看一种输出的误判。

<a id="paper-148494"></a>

## Understanding and Mitigating Structural Forgetting in Fine-Tuned Time Series Foundation Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148494) · [作者来源](https://openreview.net/forum?id=xOIgmApw6e)

- **问题 / 瓶颈** · 预测分数改善仍可能破坏依赖结构的决策。
- **核心创新 / 方法** · 用时频诊断并配套结构保留的适配。
- **Baseline** · 普通微调和遗忘缓解。
- **Benchmark** · 三时序底座与九数据集。
- **关键结果 / 消融** · 平均恢复约 85% 结构意识，同时保留任务表现。
- **适用条件 / 局限** · 依赖结构指标和时序变化。

**可复用机制** · 迁移模型要保留下游实际读取的结构，不能仅用预测误差评估遗忘。

<a id="paper-148756"></a>

## Understanding and Mitigating Under-Confidence in GNNs from the Final Layer

[官方论文页](https://neurips.cc/virtual/2026/poster/148756) · [作者来源](https://openreview.net/forum?id=vGT1YmVaWI)

- **问题 / 瓶颈** · 只做全局温度会遗漏具体节点的几何偏移。
- **核心创新 / 方法** · 用最终层表征对照预测类质心，开展双层级校准。
- **Baseline** · 既有图网络校准。
- **Benchmark** · 图分类及节点置信，摘要未给数据名称。
- **关键结果 / 消融** · 摘要报告理论刻画及实证效果改善。
- **适用条件 / 局限** · 依赖最后一层类簇结构。

**可复用机制** · 区分不同类别的整体置信偏移与同类样本局部不同，避免只调全局常数。

<a id="paper-153180"></a>

## Understanding axial attention in TSFMs through single location regression

[官方论文页](https://neurips.cc/virtual/2026/poster/153180) · [作者来源](https://openreview.net/forum?id=NCYlMi9USZ)

- **问题 / 瓶颈** · 过早变尖会减少获得正确参数的信号。
- **核心创新 / 方法** · 用可解析的轴向注意力回归模型分析训练。
- **Baseline** · 固定逆温度等对照。
- **Benchmark** · 指定渐近条件及数值实验。
- **关键结果 / 消融** · 结果支持温度日程对经验收敛关键。
- **适用条件 / 局限** · 依赖简化回归和先验参数假设。

**可复用机制** · 注意力学习失败时先比较温度路径，而非只改变网络宽深。

<a id="paper-150898"></a>

## Understanding Goal Generalisation in Sequential Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/150898) · [作者来源](https://openreview.net/forum?id=ebbWZdCWlR)

- **问题 / 瓶颈** · 环境和策略训练共同决定分布外行为
- **核心创新 / 方法** · 拟合潜变量与行为的简单模型，测试留出流程
- **Baseline** · 单一训练管线下的归因
- **Benchmark** · 序贯 RL 的分布外表现与未见训练流程
- **关键结果 / 消融** · 摘要报告预测有效且可解释
- **适用条件 / 局限** · 因素分解依赖训练流水线的覆盖和可控性

**可复用机制** · 部署前设定场景变化，测试哪项训练条件实际改变目标选择

<a id="paper-152284"></a>

## Understanding Layer Patching in Model Size Interpolation

[官方论文页](https://neurips.cc/virtual/2026/poster/152284) · [作者来源](https://openreview.net/forum?id=UDT6ZDU0b3)

- **问题 / 瓶颈** · 参数接近不能保证替换对模型行为影响小
- **核心创新 / 方法** · 用贪心 KL 衡量层替换的边际影响并逐步构建
- **Baseline** · 从后向前的朴素层替换
- **Benchmark** · 模型大小插值与输出质量
- **关键结果 / 消融** · 摘要称经常优于后到前朴素基线
- **适用条件 / 局限** · 对照模型需能够配对替换层，选择依赖校准集

**可复用机制** · 缩减部署模型前先将固定顺序当强基线

<a id="paper-149297"></a>

## Understanding Multimodal Failure in Action-Chunking Behavioral Cloning

[官方论文页](https://neurips.cc/virtual/2026/poster/149297) · [作者来源](https://openreview.net/forum?id=rH2Cz9se1a)

- **问题 / 瓶颈** · 平滑潜态到动作映射难同时覆盖分离动作模式
- **核心创新 / 方法** · 分析转移平滑限制，并验证多模态与动作支持关系
- **Baseline** · 动作块行为克隆及生成策略对照
- **Benchmark** · 合成多模态任务与机器人仿真
- **关键结果 / 消融** · 实验支持过平滑会出现非数据支持区域
- **适用条件 / 局限** · 动作可行性需另有评估器

**可复用机制** · 用分离动作路线和不安全中间动作的反例验收生成策略

<a id="paper-152537"></a>

## Understanding Multi-View Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/152537) · [作者来源](https://openreview.net/forum?id=SPQmifceIS)

- **问题 / 瓶颈** · 注意力热图不能证明模型实际匹配
- **核心创新 / 方法** · 追踪对应随几何细化，并用解析对应替换部分头做干预
- **Baseline** · 原多视图模型中的不同头
- **Benchmark** · 多视重建、对应匹配及几何诊断
- **关键结果 / 消融** · 选定头可局部替换且仍支持重建
- **适用条件 / 局限** · 只适用于所测模型及少量头

**可复用机制** · 若几何算子已有可靠实现，先测能否代替脆弱重建模块

<a id="paper-152950"></a>

## Understanding Reasoning from Pretraining to Post-Training: Chess as a Controlled Testbed

[官方论文页](https://neurips.cc/virtual/2026/poster/152950) · [作者来源](https://openreview.net/forum?id=PALFTMGRb5)

- **问题 / 瓶颈** · 平均正确率难判断 RL 是否带来新行为
- **核心创新 / 方法** · 在可枚举走法任务比较预训、SFT 和 RL 的概率轨迹
- **Baseline** · 各训练阶段的策略
- **Benchmark** · 棋题和不同难度，正确动作概率
- **关键结果 / 消融** · 易例放大 SFT 已偏好动作，难例出现原来极少采样的动作
- **适用条件 / 局限** · 棋规则和动作可验证性使分析更清楚，其他任务未证实

**可复用机制** · 对推理 RL 同时监控罕见正确选项的覆盖和主解稳定性

<a id="paper-148898"></a>

## Understanding the Challenges in Iterative Generative Optimization with LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/148898) · [作者来源](https://openreview.net/forum?id=uMQtAycESf)

- **问题 / 瓶颈** · 单一通用循环无法覆盖不同优化信号
- **核心创新 / 方法** · 对照不同种子作品、轨迹截断与小批量
- **Baseline** · 同循环不同初始化和样本分配
- **Benchmark** · MLAgentBench、Atari、BBEH
- **关键结果 / 消融** · 初始化改变可达解，截断仍可帮助 Atari，大 batch 不单调提高 BBEH 泛化
- **适用条件 / 局限** · 具体划分和生成模型会影响规律

**可复用机制** · 开始多轮生成优化前为域内任务匹配预算做小型因子实验

<a id="paper-152782"></a>

## Understanding the Convergence of Direct Training of SNNs with Surrogate Gradients

[官方论文页](https://neurips.cc/virtual/2026/poster/152782) · [作者来源](https://openreview.net/forum?id=QNkfQ8wsii)

- **问题 / 瓶颈** · 平滑代理下降不保证离散目标下降
- **核心创新 / 方法** · 统计硬轨迹膜电位到发放阈值的尾部比例
- **Baseline** · 不同 SNN 架构及普通替代训练监控
- **Benchmark** · 代表性 SNN 任务，离散目标和阈值风险
- **关键结果 / 消融** · 摘要称该统计可诊断直接训练的误差
- **适用条件 / 局限** · 保证依赖正则性和替代函数设定

**可复用机制** · 部署低功耗传感前同时看脉冲目标与近阈值稳定

<a id="paper-149289"></a>

## Understanding the Curse of Unrolling

[官方论文页](https://neurips.cc/virtual/2026/poster/149289) · [作者来源](https://openreview.net/forum?id=rOtZp9OVts)

- **问题 / 瓶颈** · 更长展开可能放大梯度误差且占显存
- **核心创新 / 方法** · 截断早期导数计算，对照全展开和隐式微分
- **Baseline** · 隐式微分及完整展开
- **Benchmark** · 合成和少样本分类元学习
- **关键结果 / 消融** · 摘要称缓解梯度问题且降低内存
- **适用条件 / 局限** · 截断点依赖收敛轨迹与问题条件数

**可复用机制** · 验证不同展开长度是否改善外层目标，而非只拟合内循环

<a id="paper-151454"></a>

## Understanding the Effects of Hyper-Connections on Self-Attention Dynamics: A Bifurcation Analysis

[官方论文页](https://neurips.cc/virtual/2026/poster/151454) · [作者来源](https://openreview.net/forum?id=aY3DfjqhAX)

- **问题 / 瓶颈** · 标准残差不能独立控制动力分岔。
- **核心创新 / 方法** · 用额外参数调零不动点的 Jacobian 谱。
- **Baseline** · 标准残差。
- **Benchmark** · 预训练超连接语言模型。
- **关键结果 / 消融** · 实证不稳定制度表现更强。
- **适用条件 / 局限** · 结论局部且依赖结构。

**可复用机制** · 训练稳定和表达能力不应由同一代理判断。

<a id="paper-156752"></a>

## Understanding the Effects of Neuron Dominance in Deep Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/156752) · [作者来源](https://openreview.net/forum?id=VNV1h77UnH)

- **问题 / 瓶颈** · 峰值过大可能压制后层代表。
- **核心创新 / 方法** · 比较缓解激活支配的方案。
- **Baseline** · 原视觉控制策略。
- **Benchmark** · 视觉控制、峰值、功能容量和休眠率。
- **关键结果 / 消融** · 低峰值与更强容量和表现相关。
- **适用条件 / 局限** · 控制损失和激活影响需分实验。

**可复用机制** · 先定位休眠出在哪一层及上游主导源。

<a id="paper-139043"></a>

## Understanding the Interplay between Memorization and Learning in Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139043) · [作者来源](https://openreview.net/forum?id=oG5alWKa3Z)

- **问题 / 瓶颈** · 复述原串与学习语言规律不同。
- **核心创新 / 方法** · 定义条件记忆指标并让已记样本少见。
- **Baseline** · 标准均匀训练。
- **Benchmark** · 语言学习和记忆量。
- **关键结果 / 消融** · 摘要称减少记忆并改善覆盖。
- **适用条件 / 局限** · 评估必须分开可泛化结构与复述。

**可复用机制** · 让训练频率随新增信息而变。

<a id="paper-154527"></a>

## Understanding the Out-of-Distribution Generalization of Chain-of-Thought Reasoning in LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/154527) · [作者来源](https://openreview.net/forum?id=CwFstPZgCZ)

- **问题 / 瓶颈** · 任务答案泛化难定位来源。
- **核心创新 / 方法** · 用共享单步预测和显式状态组合。
- **Baseline** · 省状态追踪的推理。
- **Benchmark** · Atom-Task、GSM8K。
- **关键结果 / 消融** · 支持长短与组合外推，显式状态关键。
- **适用条件 / 局限** · 实证范围有限。

**可复用机制** · 用可复查状态减小链内分布移位。

<a id="paper-150354"></a>

## Understanding the Surprising Generalization Properties of Tabular Foundation Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150354) · [作者来源](https://openreview.net/forum?id=ikYK94iVvj)

- **问题 / 瓶颈** · 更大数据行数及整表清理未必收益。
- **核心创新 / 方法** · 比较单表 SSL 与列及表级预处理。
- **Baseline** · 多表预训练、整表过滤去重。
- **Benchmark** · 表格基础模型迁移。
- **关键结果 / 消融** · 单表可强迁移，列清理有增益、整表筛无增益。
- **适用条件 / 局限** · 结论依所测表与任务。

**可复用机制** · 按训练目标粒度筛训练数据。

<a id="paper-148284"></a>

## UnfoldArt: Zero-Shot Recovery of Full Articulated 3D Objects from Text or Image

[官方论文页](https://neurips.cc/virtual/2026/poster/148284) · [作者来源](https://openreview.net/forum?id=z1gCXDoGu2)

- **问题 / 瓶颈** · 静态图像看不到内表面。
- **核心创新 / 方法** · 高层估语义动作、低层估关节和交互点。
- **Baseline** · 静态铰接重建。
- **Benchmark** · 文字或图条件的 3D 铰接物体。
- **关键结果 / 消融** · 视频先验补可见外的结构，幅度待核。
- **适用条件 / 局限** · 合成隐藏几何需标不确定。

**可复用机制** · 主动生成不同姿态检验关节假设。

<a id="paper-148454"></a>

## Uni-Cheb: A Basis-Agnostic Learnable Chebyshev Filter for Multimodal Spectral Modulation

[官方论文页](https://neurips.cc/virtual/2026/poster/148454) · [作者来源](https://openreview.net/forum?id=xirTJtdHxQ)

- **问题 / 瓶颈** · 不同任务要全局周期或局部突变。
- **核心创新 / 方法** · 可学 Chebyshev 统一调 Fourier 或小波系数。
- **Baseline** · 各模态基础时序模型。
- **Benchmark** · 多基准及跨域。
- **关键结果 / 消融** · 摘要称普遍改善，数值未核。
- **适用条件 / 局限** · 周期先验随域变化。

**可复用机制** · 共享过滤参数机制时仍允许合理频域坐标变化。

<a id="paper-139060"></a>

## UniClawBench: A Universal Benchmark for Proactive Agents on Real-World Tasks

[官方论文页](https://neurips.cc/virtual/2026/poster/139060) · [作者来源](https://openreview.net/forum?id=nVoCk7Bf1E)

- **问题 / 瓶颈** · 单轮静态答案漏反馈处理。
- **核心创新 / 方法** · 分执行、评审和用户代理，评分项不进入被测上下文。
- **Baseline** · 预录静态评测。
- **Benchmark** · UniClawBench 动态任务、多轮。
- **关键结果 / 消融** · 提出过程验收，具体数字待核。
- **适用条件 / 局限** · 模拟用户非真实用户。

**可复用机制** · 把隐含评分和面向代理的反馈权限分开。

<a id="paper-156067"></a>

## UNICOM: Unified Multimodal Modeling via Compressed Continuous Semantic Representations

[官方论文页](https://neurips.cc/virtual/2026/poster/156067) · [作者来源](https://openreview.net/forum?id=0iUmETfbJj)

- **问题 / 瓶颈** · 高维语义生成慢且不稳。
- **核心创新 / 方法** · 为连续语义做通道压缩，保空间 token。
- **Baseline** · 空间 token 裁减。
- **Benchmark** · 多模态理解、VAE-free 重构和生成收敛。
- **关键结果 / 消融** · 通道压缩更有效且重构保持。
- **适用条件 / 局限** · 对不同编码器和分辨率需复测。

**可复用机制** · 空间结构重要时先压每位置宽度。

<a id="paper-154503"></a>

## UniCon3R: Unified Contact-aware 4D Human-Scene Reconstruction from Monocular Video

[官方论文页](https://neurips.cc/virtual/2026/poster/154503) · [作者来源](https://openreview.net/forum?id=D63wCULfGW)

- **问题 / 瓶颈** · 独立重建会产生穿透和轨迹不可信。
- **核心创新 / 方法** · 在线统一重建并利用人体场景接触作内部先验。
- **Baseline** · 既有 monocular 4D 方法。
- **Benchmark** · 人中心视频，物理和运动。
- **关键结果 / 消融** · 物理合理及全局运动改善并保持前馈速度。
- **适用条件 / 局限** · 接触预测错误会传播。

**可复用机制** · 场景动力协同约束应成为可验证推理信号。

<a id="paper-155407"></a>

## UniCustom: Unified Visual Conditioning for Multi-reference Image Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/155407) · [作者来源](https://openreview.net/forum?id=5sCkEfsOSE)

- **问题 / 瓶颈** · 仅语义特征易把细节给错参照。
- **核心创新 / 方法** · VLM 编码前融 ViT 与 VAE，并约束槽绑定。
- **Baseline** · 既有多参照生成。
- **Benchmark** · 两多参考基准。
- **关键结果 / 消融** · 身份、指令和组合忠实均改善。
- **适用条件 / 局限** · 复杂近义或同类参照需复测。

**可复用机制** · 建立分槽空间保留和跨槽串扰检查。

<a id="paper-149995"></a>

## UniDBO: A Unified Dual-Branch One-Step Denoising Framework for Autonomous Driving Scenario Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/149995) · [作者来源](https://openreview.net/forum?id=lcbL2baE12)

- **问题 / 瓶颈** · 开环拟合不保证滚动鲁棒。
- **核心创新 / 方法** · 共享编码，连续尺度拟合和高噪分支闭环。
- **Baseline** · AR 和多步扩散。
- **Benchmark** · 开闭环、跨域和系统仿真。
- **关键结果 / 消融** · 改善权衡且推理高效。
- **适用条件 / 局限** · 仿真不等于真实安全。

**可复用机制** · 保一步延迟时给闭环误差独立训练路径。

<a id="paper-154905"></a>

## UniDG: Universal Defect Generation via Defect-Context Editing

[官方论文页](https://neurips.cc/virtual/2026/poster/154905) · [作者来源](https://openreview.net/forum?id=A3soBL3Ciu)

- **问题 / 瓶颈** · 单配方难既多样又忠于正常背景。
- **核心创新 / 方法** · 编辑四元组做 SFT，再以位置、类别保真监督。
- **Baseline** · 领域特定缺陷生成。
- **Benchmark** · UDG 30 万正常/异常/掩码/描述。
- **关键结果 / 消融** · 摘要提出生成机制，收益细节待核。
- **适用条件 / 局限** · 合成异常不能代替真实质控。

**可复用机制** · 增强只变目标故障，将其他结构作验收约束。

<a id="paper-153710"></a>

## Unified Approach for Weakly Supervised Multicalibration

[官方论文页](https://neurips.cc/virtual/2026/poster/153710) · [作者来源](https://openreview.net/forum?id=JLxOg88ATs)

- **问题 / 瓶颈** · 比较预测和观察标签会误估亚群校准。
- **核心创新 / 方法** · 以污染矩阵重写风险并做 witness 约束。
- **Baseline** · 干净输入标签的多校准。
- **Benchmark** · 多弱监督设定。
- **关键结果 / 消融** · 有有限样本保证并提供后处理。
- **适用条件 / 局限** · 矩阵估计偏差会传递。

**可复用机制** · 以弱监督来源契约约束置信修正。

<a id="paper-150807"></a>

## Unified Forensic Preference Learning for Generalizable Synthetic Image Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/150807) · [作者来源](https://openreview.net/forum?id=fGUaeL5g1k)

- **问题 / 瓶颈** · 只给真伪标签易学生成器捷径。
- **核心创新 / 方法** · 把多模态取证知识转偏好监督。
- **Baseline** · 最强合成识别。
- **Benchmark** · 11 整理及野外基准。
- **关键结果 / 消融** · 平均平衡准确率 93.4%，最坏 81.4% 至 86.1%。
- **适用条件 / 局限** · 新生成器和新压缩需重验。

**可复用机制** · 按最坏组表现验知识监督。

<a id="paper-155625"></a>

## Unified Generative-Predictive Modeling for 4D Scene Understanding

[官方论文页](https://neurips.cc/virtual/2026/poster/155625) · [作者来源](https://openreview.net/forum?id=4Br2rbkC6J)

- **问题 / 瓶颈** · 分独立生成和几何预测难共用缺标数据。
- **核心创新 / 方法** · 联合 RGB、深度和位姿，保持任意子集条件，测试时搜补全。
- **Baseline** · 单任务前馈和生成模型。
- **Benchmark** · 跨模态、几何和未来场景。
- **关键结果 / 消融** · 稀观测候选搜索改善几何，幅度待核。
- **适用条件 / 局限** · 联合模型开销和一致性要验。

**可复用机制** · 把缺失标签建成条件组合而非丢样本。

<a id="paper-150948"></a>

## Unified Loss-Aware Density Control for 3D Gaussian Splatting

[官方论文页](https://neurips.cc/virtual/2026/poster/150948) · [作者来源](https://openreview.net/forum?id=e6aTB4t6ha)

- **问题 / 瓶颈** · 重复高斯会浪费原语。
- **核心创新 / 方法** · 以代理最小化选克隆并算子透明度。
- **Baseline** · 常规密度控制。
- **Benchmark** · 标准 3DGS，渲染及原语预算。
- **关键结果 / 消融** · 更少或类似原语下质量提高。
- **适用条件 / 局限** · 代理误差和预算需复测。

**可复用机制** · 显式量新增几何元素的边际贡献。

<a id="paper-152531"></a>

## Unified Noise Steering for Efficient Human-Guided VLA Adaptation

[官方论文页](https://neurips.cc/virtual/2026/poster/152531) · [作者来源](https://openreview.net/forum?id=SSqCNsA0YT)

- **问题 / 瓶颈** · 上机 RL 预算不足，外部纠正与策略动作不统一。
- **核心创新 / 方法** · 近似动作反演后学习噪声方向策略。
- **Baseline** · 强噪声 RL 及动作空间人机环。
- **Benchmark** · 四实机操作适配。
- **关键结果 / 消融** · 均值 66 分钟成功率 20% 到 90%。
- **适用条件 / 局限** · 依赖反演稳定、人类干预和设备。

**可复用机制** · 控制纠正应能以一致低维接口供策略学习。

<a id="paper-149348"></a>

## Unified Panoramic Geometry Estimation via Multi-View Foundation Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149348) · [作者来源](https://openreview.net/forum?id=qjgSaycXfb)

- **问题 / 瓶颈** · 全景域移与球面变形。
- **核心创新 / 方法** · 少改架构，混合透视和全景，单步预测深度、法线与天空。
- **Baseline** · 透视重建及一般全景方法。
- **Benchmark** · 室内外和零样本全景。
- **关键结果 / 消融** · 摘要称强效果，数值未核。
- **适用条件 / 局限** · 需要全景样本和适用范围验证。

**可复用机制** · 跨传感器改造先保原几何与联合监督，再改参数。

<a id="paper-148666"></a>

## Unified Resource-Grounded Coordination Protocol for Orchestrator-Free Heterogeneous Multi-Agent Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/148666) · [作者来源](https://openreview.net/forum?id=w2x7C7peAm)

- **问题 / 瓶颈** · 中心协调缺失时会出现未验证的交接。
- **核心创新 / 方法** · 按资源形成角色和任务图，再校验交接。
- **Baseline** · 同模型池的其他协调方法。
- **Benchmark** · 异构代理协同。
- **关键结果 / 消融** · 至少三角色的接受方案中 63.5% 插入批评或验证角色。
- **适用条件 / 局限** · 摘要未给总体性能数值。

**可复用机制** · 组织代理时让验证成为显式角色，避免只配置执行者。

<a id="paper-154811"></a>

## Unified Synthesis of Compositional Speech and Sound from Free-Form Text Prompts

[官方论文页](https://neurips.cc/virtual/2026/poster/154811) · [作者来源](https://openreview.net/forum?id=Am7V8MfDiN)

- **问题 / 瓶颈** · 自由文本含多个声源，独立模型难协调。
- **核心创新 / 方法** · PlanAudio 自回归规划，并渐进混合多场景。
- **Baseline** · 其他 CoT 机制。
- **Benchmark** · 文字生成声音、语音及其组合。
- **关键结果 / 消融** · 摘要报告语义潜计划与连续课程有益。
- **适用条件 / 局限** · 未给各项效应量。

**可复用机制** · 组合式音频应先规划共同事件，再生成各个声源。

<a id="paper-151328"></a>

## UniFlow-Audio: Unified Flow Matching for Audio Generation from Omni-Modalities

[官方论文页](https://neurips.cc/virtual/2026/poster/151328) · [作者来源](https://openreview.net/forum?id=bLR3wcXBSv)

- **问题 / 瓶颈** · 不同输入模态通常需不同生成器。
- **核心创新 / 方法** · 双融合对齐音频潜变量与条件特征。
- **Baseline** · 独立或自回归生成方案。
- **Benchmark** · 不同模态条件下音频生成。
- **关键结果 / 消融** · 摘要报告统一生成有竞争力。
- **适用条件 / 局限** · 架构开销及消融数值未报告。

**可复用机制** · 复用同一音频生成先验时，把输入模态差别隔离到条件融合。

<a id="paper-153715"></a>

## Uniform Diffusion Models revisited: Leave-One-Out Denoiser and Absorbing State Reformulation

[官方论文页](https://neurips.cc/virtual/2026/poster/153715) · [作者来源](https://openreview.net/forum?id=JJGRXH8cyk)

- **问题 / 瓶颈** · 最终训练目标可能不是通常的去噪后验。
- **核心创新 / 方法** · 推导留一后验及与其他参数化的转换。
- **Baseline** · 普通去噪参数化。
- **Benchmark** · 语言建模和离散扩散。
- **关键结果 / 消融** · 留一去噪器在所测任务更优。
- **适用条件 / 局限** · 限所分析参数化。

**可复用机制** · 修改生成后验的插入接口时先重新推导它对应的统计目标。

<a id="paper-151601"></a>

## Uniform Spectral Growth under Factor-wise Muon Orthogonalization in Matrix Factorization and LoRA

[官方论文页](https://neurips.cc/virtual/2026/poster/151601) · [作者来源](https://openreview.net/forum?id=ZKrEQSZqnM)

- **问题 / 瓶颈** · 小奇异值经常更晚被普通优化学习。
- **核心创新 / 方法** · 分别正交化因子步长，分析相近的谱增长速度。
- **Baseline** · 其他低秩优化。
- **Benchmark** · 矩阵分解理论及 LoRA 实证。
- **关键结果 / 消融** · 小奇异值较早达到目标，Muon 等给出近均匀增长。
- **适用条件 / 局限** · 理论为连续流，离散情形证据为实测。

**可复用机制** · 比较适配器优化时可记录每个秩方向的成长速度。

<a id="paper-155665"></a>

## UniFunc3D: Unified Active Spatial-Temporal Grounding for 3D Affordance Segmentation

[官方论文页](https://neurips.cc/virtual/2026/poster/155665) · [作者来源](https://openreview.net/forum?id=3vq4AkEW4K)

- **问题 / 瓶颈** · 被动投影容易让可动部件失去语义证据。
- **核心创新 / 方法** · 统一时空推理和粗到细观察。
- **Baseline** · 任务训练及其他免训练方案。
- **Benchmark** · 三维可供性分割与 mIoU。
- **关键结果 / 消融** · 摘要报告约 59.9% 相对增益。
- **适用条件 / 局限** · 依赖主动视角可用。

**可复用机制** · 若单视图证据不足，先用低成本预测缩小范围，再围绕任务所需信息重看。

<a id="paper-150380"></a>

## Unifying Contrastive and Generative Objectives for Visual Understanding and Text-to-Image Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/150380) · [作者来源](https://openreview.net/forum?id=iUP2tlq1du)

- **问题 / 瓶颈** · 分阶段或单一遮盖率会使对比和生成各自偏向不同条件。
- **核心创新 / 方法** · 训练时混合遮盖率，再以共同文本空间评价部分解码。
- **Baseline** · 单目标或其他联合训练。
- **Benchmark** · 视觉理解及图文生成。
- **关键结果 / 消融** · 摘要报告可改善结果同时维持 CLIP Score。
- **适用条件 / 局限** · 未给适用遮盖比例。

**可复用机制** · 联合目标要确保共享模块持续接触各目标需要的输入强度。

<a id="paper-153300"></a>

## Unifying Goal-Conditioned RL and Unsupervised Skill Learning via Control-Maximization

[官方论文页](https://neurips.cc/virtual/2026/poster/153300) · [作者来源](https://openreview.net/forum?id=MHeZHmPRnt)

- **问题 / 瓶颈** · 不同技能多样性目标未必覆盖关心的控制。
- **核心创新 / 方法** · 把目标到达和互信息技能统一为控制最大化。
- **Baseline** · 不同奖励目标和技能方法。
- **Benchmark** · 目标到达与技能学习的理论及应用。
- **关键结果 / 消融** · 摘要给出不同下游任务的预训练选择依据。
- **适用条件 / 局限** · 实施需符合控制度量的假设。

**可复用机制** · 评估技能库应看能控制哪些结果，而非只数有多少互异技能。

<a id="paper-151901"></a>

## Unifying Partner and Environment Diversity to Improve Human-AI Coordination

[官方论文页](https://neurips.cc/virtual/2026/poster/151901) · [作者来源](https://openreview.net/forum?id=X66IYOVa2D)

- **问题 / 瓶颈** · 固定场地下训练多伙伴难区分环境与社会泛化。
- **核心创新 / 方法** · 在角色和场景变化下训练可推断伙伴技能的潜表示。
- **Baseline** · 固定环境的伙伴多样化和跨环境自博弈。
- **Benchmark** · 未见用户和环境的协同。
- **关键结果 / 消融** · 作者报告表现提高且潜变量显示对技能的推断。
- **适用条件 / 局限** · 依赖训练覆盖并需要实人复核。

**可复用机制** · 当伙伴性能受环境影响时，对环境和伙伴做交叉外推。

<a id="paper-154954"></a>

## Unifying Reasoning and Planning through Energy Minimization

[官方论文页](https://neurips.cc/virtual/2026/poster/154954) · [作者来源](https://openreview.net/forum?id=9g7Kc9OMTB)

- **问题 / 瓶颈** · 动态扩散能量需要反复退火。
- **核心创新 / 方法** · 学习共享形式的时不变能量，并用梯度优化推理。
- **Baseline** · 扩散 EBM、专用求解器和规划器。
- **Benchmark** · 推理及迷宫等规划。
- **关键结果 / 消融** · 达到或超过对照且推理计算更少。
- **适用条件 / 局限** · 静态能量需可优化，摘要未给多峰难例。

**可复用机制** · 优先比较单能量的成本与解质，再决定是否引入逐步去噪。

<a id="paper-151050"></a>

## Unifying Sparsity and Discreteness: One-Shot Pruning for Quantized LLMs via Discrete Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/151050) · [作者来源](https://openreview.net/forum?id=dMShldodM4)

- **问题 / 瓶颈** · 连续优化的好解可能因后续取整而变差。
- **核心创新 / 方法** · QOP 在离散权重与稀疏约束下求解。
- **Baseline** · 分开剪枝和量化。
- **Benchmark** · 多模型与多位宽，平均准确率和困惑度。
- **关键结果 / 消融** · 摘要报告两项均持续优于基线。
- **适用条件 / 局限** · 量化格点和搜索成本限制适用性。

**可复用机制** · 最终部署状态离散时，压缩阶段应在真实可行值上评价误差。

<a id="paper-152723"></a>

## UniGS: Unified Geometry-Aware Gaussian Splatting for Multimodal Rendering

[官方论文页](https://neurips.cc/virtual/2026/poster/152723) · [作者来源](https://openreview.net/forum?id=QqB9JRnM29)

- **问题 / 瓶颈** · 直接使用中心深度不足以监督姿态和尺度。
- **核心创新 / 方法** · 通过可微射线椭球相交并推导深度和法向梯度。
- **Baseline** · 中心近似和其他高斯渲染。
- **Benchmark** · 多个多模态三维重建数据。
- **关键结果 / 消融** · 摘要报告先进准确度。
- **适用条件 / 局限** · 依赖椭球原语，求交成本未报告。

**可复用机制** · 若下游需要表面几何，训练时不要以中心近似替代真实渲染位置。

<a id="paper-152667"></a>

## UniMoE-World: A Unified Mixture-of-Experts Architecture for Scalable Multi-Control Video Generation World Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/152667) · [作者来源](https://openreview.net/forum?id=RHtNN9ZMbC)

- **问题 / 瓶颈** · 单一控制训练难共享多种监督。
- **核心创新 / 方法** · 在扩散 Transformer 加入 MoE 统一多控制。
- **Baseline** · 其他世界模型。
- **Benchmark** · WorldArena，运动及手部控制。
- **关键结果 / 消融** · 摘要报告达到先进结果。
- **适用条件 / 局限** · 需要跨接口共享表示，摘要未给专家开销。

**可复用机制** · 多种控制接口共存时，分开估计共享动态和控制特有信息。

<a id="paper-153352"></a>

## UniPath: Adaptive Coordination of Understanding and Generation for Unified Multimodal Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/153352) · [作者来源](https://openreview.net/forum?id=M1C4LYZjQz)

- **问题 / 瓶颈** · 固定工作流无法匹配不同输入。
- **核心创新 / 方法** · 按样本选择协作路径。
- **Baseline** · 固定协调路径。
- **Benchmark** · 统一多模态推理任务。
- **关键结果 / 消融** · 作者称提高表现并产生可检查的中间过程。
- **适用条件 / 局限** · 摘要未给路由标签和额外时延。

**可复用机制** · 含观察与生成的程序可让执行顺序由证据决定，而非硬设统一模板。

<a id="paper-152106"></a>

## UniPrefill: Universal Long-Context Prefill Acceleration via Block-wise Dynamic Sparsification

[官方论文页](https://neurips.cc/virtual/2026/poster/152106) · [作者来源](https://openreview.net/forum?id=VU9bHYAvdH)

- **问题 / 瓶颈** · 部分层采用线性或滑动窗口时，全注意力专用方法的收益下降。
- **核心创新 / 方法** · 用块级动态稀疏适配不同注意力结构。
- **Baseline** · 稀疏全注意力专用方案。
- **Benchmark** · 不同混合模型与并发规模，首 token 时间。
- **关键结果 / 消融** · 摘要报告首 token 最高快 2.1 倍。
- **适用条件 / 局限** · 收益依赖并发及架构。

**可复用机制** · 优化推理关键路径要以实际层结构占比而非理想全注意力为输入。

<a id="paper-148811"></a>

## UniT:  Toward a Unified Physical Language for Human-to-Humanoid Policy Learning and World Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/148811) · [作者来源](https://openreview.net/forum?id=uwdO3ESE0A)

- **问题 / 瓶颈** · 跨形态视觉和动作定义不同，直接模仿难迁移
- **核心创新 / 方法** · 建立联合动作与世界建模表示，检查人机特征和动作条件生成
- **Baseline** · 独立表征方式，具体模型未报告
- **Benchmark** · 人形操作及动作条件视频生成
- **关键结果 / 消融** · 摘要报告控制和表示对齐改善
- **适用条件 / 局限** · t-SNE 只作诊断，需统一实机任务验证

**可复用机制** · 跨形态预训练同时测动作可控性和策略成功

<a id="paper-155949"></a>

## UniVer: A Unified Perspective for Multi-step and Multi-draft Speculative Decoding

[官方论文页](https://neurips.cc/virtual/2026/poster/155949) · [作者来源](https://openreview.net/forum?id=1bA7Ig2sVb)

- **问题 / 瓶颈** · 分开拒绝采样难兼顾多个候选
- **核心创新 / 方法** · 按条件验证保持目标分布，对照无放回递归采样
- **Baseline** · 标准无放回递归拒绝采样
- **Benchmark** · 多模型和任务；接受长度、目标分布
- **关键结果 / 消融** · 接受长度提升 4.2–8.5%，分布精确对齐
- **适用条件 / 局限** · 接受长度不是墙钟，需计入验证成本

**可复用机制** · 推测验证应以解码质量同分布和实测时延双验收

<a id="paper-152902"></a>

## Universal Byte-Level Encoding: UTF-8/UTF-16 Routing to Reduce Cross-Script Token-Budget Disparities

[官方论文页](https://neurips.cc/virtual/2026/poster/152902) · [作者来源](https://openreview.net/forum?id=PYtjaNdYaM)

- **问题 / 瓶颈** · 固定 UTF-8 造成部分书写系统 token 成本高
- **核心创新 / 方法** · 在 UTF-8、UTF-16 编码间路由，按内容预算比较
- **Baseline** · 常规字节编码
- **Benchmark** · 多语语言模型；上下文长度、token 和质量
- **关键结果 / 消融** · 高成本书写系统降得最多，语言建模质量在种子差异内
- **适用条件 / 局限** · 混合书写系统路由及运行成本要核验

**可复用机制** · 多语产品按同等文本内容量而非单指 token 比较效率

<a id="paper-150341"></a>

## Universal Time Series Generation with Neural Controlled Differential Equations

[官方论文页](https://neurips.cc/virtual/2026/poster/150341) · [作者来源](https://openreview.net/forum?id=iqICKB71X4)

- **问题 / 瓶颈** · 固定网格需要插值并限制未知采样时点
- **核心创新 / 方法** · 用神经受控微分方程表达路径空间上的流匹配
- **Baseline** · 固定网格时序生成
- **Benchmark** · 概率预测与下游任务中的任意观测网格
- **关键结果 / 消融** · 不规则网格更受益，幅度未报告
- **适用条件 / 局限** · 实际收益受插值选择和求解成本影响

**可复用机制** · 异步多传感器分开测规则和不规则采样情况

<a id="paper-152503"></a>

## UNIVERSE: Unified Video Action Models for Autonomous Driving with Flexible Mask-Modulated Modality Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/152503) · [作者来源](https://openreview.net/forum?id=SfVDhDwIKG)

- **问题 / 瓶颈** · 每步都生成视频提高规划开销
- **核心创新 / 方法** · 单 DiT 以掩码耦合或解耦视频与轨迹输出
- **Baseline** · 独立建模、无视频共训练及无掩码消融
- **Benchmark** · NAVSIM、nuScenes、Bench2Drive
- **关键结果 / 消融** · NAVSIM 91.0 PDMS，支持零样本转移
- **适用条件 / 局限** · 单模型容量分配和未见场景校准影响结果

**可复用机制** · 规划部署默认仅出动作，按需触发视频辅助诊断

<a id="paper-154331"></a>

## UniVL: Unified Vision-Language Embedding for Spatially Grounded Contextual Image Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/154331) · [作者来源](https://openreview.net/forum?id=EPyIDzDBau)

- **问题 / 瓶颈** · 转成文本提示可能丢空间关联并增加编码开销
- **核心创新 / 方法** · 以联合表征直接条件生成，移除常规文字编码器
- **Baseline** · 标准文本提示方法
- **Benchmark** · 空间情境生成；FID、PSNR、TFLOPs 和时延
- **关键结果 / 消融** · FID 14 至 11，PSNR 16 至 20，时延最高少 44%
- **适用条件 / 局限** · 需要可映射到视觉条件空间的任务输入

**可复用机制** · 兼顾生成速度与空间约束时比较原生表征和经文字转换

<a id="paper-153227"></a>

## Unlearning Diffusion Policies via Relative Fisher Forgetting

[官方论文页](https://neurips.cc/virtual/2026/poster/153227) · [作者来源](https://openreview.net/forum?id=MpxEJi7gJL)

- **问题 / 瓶颈** · 直接移除示范需昂贵重训且会影响其他行为
- **核心创新 / 方法** · 相对 Fisher 度量配梯度裁剪及保留集正则
- **Baseline** · 其他遗忘方法和从头重训
- **Benchmark** · MuJoCo，遗忘集依赖、保留性能及计算
- **关键结果 / 消融** · 相对重训效率逾 12 倍，且摘要报告较低遗忘集依赖
- **适用条件 / 局限** · 目标行为若在保留集也有来源则难消除

**可复用机制** · 撤除不当示范时独立验收数据影响和实测行为

<a id="paper-150776"></a>

## UnlearningSoup: Is Repeated Tuning Necessary for Large Language Model Unlearning?

[官方论文页](https://neurips.cc/virtual/2026/poster/150776) · [作者来源](https://openreview.net/forum?id=fSWzkyhZrz)

- **问题 / 瓶颈** · 训练遗忘保留权衡敏感且候选间可能在同盆地。
- **核心创新 / 方法** · 用遗忘专用模型 soup，早期以二分搜索内插。
- **Baseline** · 分别重复训练遗忘。
- **Benchmark** · 多模型和任务的遗忘与保留。
- **关键结果 / 消融** · 发现共享盆地，有望节省重复调参，幅度未核。
- **适用条件 / 局限** · 插值不能保证个例忘却。

**可复用机制** · 在权重平均前验证端点和内部的完整遗忘审计。

<a id="paper-149440"></a>

## Unlearning That Lasts: Utility-Preserving, Robust, and Almost Irreversible Forgetting in LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/149440) · [作者来源](https://openreview.net/forum?id=q4iZrZtAjJ)

- **问题 / 瓶颈** · 方向性 KL 可能难兼顾稳忘与保留。
- **核心创新 / 方法** · 双集 JSD 优化，并独立测温和再学习。
- **Baseline** · KL 及已有遗忘。
- **Benchmark** · LPF 低知名事实，语义和效用。
- **关键结果 / 消融** · 更优权衡并耐温和再学习。
- **适用条件 / 局限** · 事实选择和语义判定有误差。

**可复用机制** · 不要只凭原问题答错判永久遗忘。

<a id="paper-150470"></a>

## Unleashing the Power of Intrinsic-Entropy-Driven Exploration for Off-Policy Generative RL

[官方论文页](https://neurips.cc/virtual/2026/poster/150470) · [作者来源](https://openreview.net/forum?id=hnh5y3DwoB)

- **问题 / 瓶颈** · 黑箱流采样常只能加启发噪声。
- **核心创新 / 方法** · 结构可逆双变量仿射流，变量替换给辅助动作熵。
- **Baseline** · 现有扩散 RL 与噪声探索。
- **Benchmark** · DMControl、HumanoidBench 共 14 任务。
- **关键结果 / 消融** · 摘要报告领先，幅度未核。
- **适用条件 / 局限** · 扩展熵不自动等于物理动作熵。

**可复用机制** · 显式处理探索统计量能否准确估计。

<a id="paper-149845"></a>

## Unlocking Accurate Geometry in 3DGS via Spatially Varying Affine Rectification

[官方论文页](https://neurips.cc/virtual/2026/poster/149845) · [作者来源](https://openreview.net/forum?id=mrz9qznPND)

- **问题 / 瓶颈** · 统一尺度不能纠正多区域视差偏差。
- **核心创新 / 方法** · 边缘感知平滑将视差变度量深度。
- **Baseline** · 几何优化类 3DGS。
- **Benchmark** · 无传感重建、几何精度和光度。
- **关键结果 / 消融** · 提高几何，保持图像质量。
- **适用条件 / 局限** · 区域估计需要足够多视观测。

**可复用机制** · 感知先验与单位噪声可按物体边界细化。

<a id="paper-152247"></a>

## Unlocking Any-Order Generation in Pretrained Autoregressive Image Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152247) · [作者来源](https://openreview.net/forum?id=UVG9WWadYE)

- **问题 / 瓶颈** · 目标位置不明，直接换顺序会甩离预训练。
- **核心创新 / 方法** · 前视位置嵌入及逐步改变生成顺序。
- **Baseline** · 原光栅 AR。
- **Benchmark** · 图像修补、扩展、编辑。
- **关键结果 / 消融** · 通用任意序能力可由适配得到，幅度未核。
- **适用条件 / 局限** · 新顺序覆盖和局部遮罩质量需测。

**可复用机制** · 改自回归因子分解时先让目标索引可辨，再扩训练分布。

<a id="paper-153657"></a>

## Unlocking Compositional Generalization in Continual Few-Shot Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/153657) · [作者来源](https://openreview.net/forum?id=JiDX823MQW)

- **问题 / 瓶颈** · 部件训练过拟合已有组合。
- **核心创新 / 方法** · 冻结 ViT，slot 对整类优化，推理组合。
- **Baseline** · 全局嵌入或显式部分匹配训练。
- **Benchmark** · 持续少样本和未见概念。
- **关键结果 / 消融** · 未见组合更好且遗忘少。
- **适用条件 / 局限** · 需要冻结特征已有局部语义。

**可复用机制** · 训练保持可组合部件，部署再按新对象关系组装。

<a id="paper-151938"></a>

## Unlocking Fine-Grained Perception in CLIP via Structurally-Aware Latent Masked Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/151938) · [作者来源](https://openreview.net/forum?id=WiG66zEVDd)

- **问题 / 瓶颈** · 全局对比不足以保持局部几何。
- **核心创新 / 方法** · 结构感知潜遮罩和双矩阵对齐。
- **Baseline** · 普通 CLIP。
- **Benchmark** · 密集预测和零样本。
- **关键结果 / 消融** · 两类改善，幅度待核。
- **适用条件 / 局限** · 局部强度度量随架构变化。

**可复用机制** · 密集适配要验局部关系且保语义零样本。

<a id="paper-151730"></a>

## Unlocking the Duality between Flow and Field Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/151730) · [作者来源](https://openreview.net/forum?id=YWRpiQXslM)

- **问题 / 瓶颈** · 名称不同会掩盖等价的前向路径。
- **核心创新 / 方法** · 建立 CFM 与 forward-only IFM 映射，并定位全 IFM 的额外表达。
- **Baseline** · 标准条件流匹配和一般 IFM。
- **Benchmark** · 理论生成动力学。
- **关键结果 / 消融** · 前向子类等价，完整 IFM 严格更广。
- **适用条件 / 局限** · 表达更广不保证训练可行。

**可复用机制** · 设计生成场时先用等价构造核对是否真需要更复杂场。

<a id="paper-139846"></a>

## Unpacking the Evaluators: How Configuration Shapes the Evaluation of Alignment in Explainable AI

[官方论文页](https://neurips.cc/virtual/2026/poster/139846) · [作者来源](https://openreview.net/forum?id=0x8H3vwcGg)

- **问题 / 瓶颈** · 指标变化可能来自配置而非模型。
- **核心创新 / 方法** · 将对齐评估写成配置轴。
- **Baseline** · 单一归因一致分数。
- **Benchmark** · 归因图、GT、软硬指标与阈值。
- **关键结果 / 消融** · 摘要指出配置会带来系统偏置，确数未核。
- **适用条件 / 局限** · 需要有代表性的专家参考。

**可复用机制** · 版本比较时呈现结果是否对配置选择稳定。

<a id="paper-149273"></a>

## Unpaired Canonical Correlation Analysis

[官方论文页](https://neurips.cc/virtual/2026/poster/149273) · [作者来源](https://openreview.net/forum?id=rYRi7zoSZK)

- **问题 / 瓶颈** · 传统 CCA 要成对观测。
- **核心创新 / 方法** · 用 QAP 与 CCA 关系推无配对估计。
- **Baseline** · 近期无配对对齐。
- **Benchmark** · 多真实多模态数据，真实相关恢复。
- **关键结果 / 消融** · 明显改善。
- **适用条件 / 局限** · 共享空间可识别依赖分布条件。

**可复用机制** · 在采集配对数据前量无配对投影能恢复多少匹配结构。

<a id="paper-154200"></a>

## Unrestrained Simplex Denoising for Discrete Data. A Generative Method Applied to Graphs.

[官方论文页](https://neurips.cc/virtual/2026/poster/154200) · [作者来源](https://openreview.net/forum?id=FSawnw2xXM)

- **问题 / 瓶颈** · 连续域路径对类别和未归一输出有失配。
- **核心创新 / 方法** · 以单纯形做生成去噪。
- **Baseline** · 现有离散图生成。
- **Benchmark** · 图数据生成。
- **关键结果 / 消融** · 摘要给新生成形式，结果数字待核。
- **适用条件 / 局限** · 需比较映射回离散图的有效性和代价。

**可复用机制** · 建模空间应约束采样始终能解释成有效类别概率。

<a id="paper-154498"></a>

## Unrolled gradients in disguise: bridging interpolation-based and Jacobian regularization for stable neural dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/154498) · [作者来源](https://openreview.net/forum?id=D9tcNsOthV)

- **问题 / 瓶颈** · 普通逐步误差只管局部拟合。
- **核心创新 / 方法** · 统一插值式与 Jacobian 正则为梯度近似。
- **Baseline** · 分别使用各启发正则。
- **Benchmark** · 学习动态的稳定性。
- **关键结果 / 消融** · 新正则改善稳定，幅度未核。
- **适用条件 / 局限** · 近似误差随时域和非线性变化。

**可复用机制** · 从目标长时梯度倒推便宜的局部约束。

<a id="paper-151439"></a>

## Unsupervised Concept Discovery with Dirichlet Concept Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151439) · [作者来源](https://openreview.net/forum?id=ahE8Fplb25)

- **问题 / 瓶颈** · 另训概念发现与生成过程不一致。
- **核心创新 / 方法** · Dirichlet 权重合成概念中心，调扩散均值及逆过程。
- **Baseline** · 普通扩散与事后解释。
- **Benchmark** · 多图像域、原型和干预。
- **关键结果 / 消融** · 产生可干预且重复的概念结构。
- **适用条件 / 局限** · 原型意义仍需人工或独立指标核验。

**可复用机制** · 将概念可辨信号写进路径而非只给隐变量标签。

<a id="paper-153211"></a>

## Unsupervised Domain Adaptation for Semantic Segmentation Based on Instance Spatial Geometry

[官方论文页](https://neurips.cc/virtual/2026/poster/153211) · [作者来源](https://openreview.net/forum?id=N19qO7k1Lr)

- **问题 / 瓶颈** · 绝对深度有传感差，关系结构可能更稳。
- **核心创新 / 方法** · 建模对象方向集中和主方向。
- **Baseline** · 常规 UDA。
- **Benchmark** · 标准域迁移分割基准。
- **关键结果 / 消融** · 优于摘要所比方法，幅度未核。
- **适用条件 / 局限** · 依赖实例检测和关系稳定。

**可复用机制** · 跨域感知用实例关系作不变量候选。

<a id="paper-154646"></a>

## Unsupervised Physics Informed Decomposition of Incomplete Time-Resolved Spectroscopy

[官方论文页](https://neurips.cc/virtual/2026/poster/154646) · [作者来源](https://openreview.net/forum?id=C4YjfEPhRx)

- **问题 / 瓶颈** · 仅静态记录混合背景和信号。
- **核心创新 / 方法** · 以物理时间变化分解谱和背景。
- **Baseline** · 现有谱分解。
- **Benchmark** · 模拟及新实测光谱时间序列，重构及峰。
- **关键结果 / 消融** · 短记录可回收目标，峰识别改善。
- **适用条件 / 局限** · 需有可区分衰减与目标动力学。

**可复用机制** · 时序观测的一部分可用来识别静态混合成分。

<a id="paper-150501"></a>

## Untrusted Content Masking for Web Agents with Security Guarantees

[官方论文页](https://neurips.cc/virtual/2026/poster/150501) · [作者来源](https://openreview.net/forum?id=hckd9UoUPT)

- **问题 / 瓶颈** · 显示内容可混入操作上下文。
- **核心创新 / 方法** · 以页面结构做防御性遮蔽，交互经最小权限沙箱接口。
- **Baseline** · 普通直接观察网页的代理。
- **Benchmark** · 网页代理安全规划与执行。
- **关键结果 / 消融** · 提出结构隔离防御，数值待核。
- **适用条件 / 局限** · 依赖结构标记可信和隔离接口正确。

**可复用机制** · 系统层限定代理可用信息及权限，不把策略安全只交给模型自行判断。

<a id="paper-150606"></a>

## Unveiling Entropy-Performance Decoupling in Agentic RL for Tool-Integrated Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/150606) · [作者来源](https://openreview.net/forum?id=gtJOVyrY09)

- **问题 / 瓶颈** · 采样多样可能只是失效循环。
- **核心创新 / 方法** · rollout 达无效交互上限时早停，保留必要恢复。
- **Baseline** · 普通工具推理 RL。
- **Benchmark** · 六公开基准、7B 至 32B。
- **关键结果 / 消融** · Qwen3-32B 宏平均增 13.6%。
- **适用条件 / 局限** · 阈值过严会阻断成功恢复。

**可复用机制** · 分别记录有信息探索和重复错误，按收益分采样预算。

<a id="paper-149067"></a>

## Unveiling Fine-Grained Visual Traces: Evaluating MultiModal Interleaved Reasoning Chains in Multimodal STEM Tasks

[官方论文页](https://neurips.cc/virtual/2026/poster/149067) · [作者来源](https://openreview.net/forum?id=t7FoUdbKB6)

- **问题 / 瓶颈** · 最终答对并不确认模型读取了必要的视觉证据。
- **核心创新 / 方法** · 约束题目无法单由文字或图像解决，然后标注跨模态过程。
- **Baseline** · 现有多模态模型和终点准确率。
- **Benchmark** · STEPSTEM，283 个高阶 STEM 问题。
- **关键结果 / 消融** · 摘要报告真实使用跨模态证据有提升空间。
- **适用条件 / 局限** · 限所设题目，摘要未给步骤评分误差。

**可复用机制** · 创建视觉问答时用去模态对照排除单模态捷径。

<a id="paper-153467"></a>

## Unveiling Implicit Advantage Symmetry: Why GRPO Struggles with Exploration and Difficulty Adaptation

[官方论文页](https://neurips.cc/virtual/2026/poster/153467) · [作者来源](https://openreview.net/forum?id=L7H48b3yB6)

- **问题 / 瓶颈** · 对称抵消可能不更新未采样动作，并偏向中等难度。
- **核心创新 / 方法** · 以 A-GRAE 改变探索激励和样本难度侧重。
- **Baseline** · GRPO 及变体。
- **Benchmark** · 七个语言和多模态推理基准。
- **关键结果 / 消融** · 摘要报告各模型类型均有一致改善。
- **适用条件 / 局限** · 依赖所述优势结构，摘要未给通用探索增益。

**可复用机制** · 训练时检查优势归一化是否在优化失败题和解法多样性时抵消必要信号。

<a id="paper-148534"></a>

## Unveiling Memorization–Generalization Coexistence: A Case Study on Arithmetic Tasks with Label Noise

[官方论文页](https://neurips.cc/virtual/2026/poster/148534) · [作者来源](https://openreview.net/forum?id=xBZ9SuztWE)

- **问题 / 瓶颈** · 模型输出受错误标签压制时，内部仍可保留泛化结构。
- **核心创新 / 方法** · 对两层网络和不同配置研究算术标签噪声。
- **Baseline** · 不同宽度及优化配置。
- **Benchmark** · 算术任务、错误与正确标签的记忆速度。
- **关键结果 / 消融** · 摘要报告噪声标签记得更快，宽模型可学内部泛化。
- **适用条件 / 局限** · 限两层合成实验，不能推广到所有模型。

**可复用机制** · 判断噪声训练失败前，探测是否已表征正确规则但读出被污染。

<a id="paper-154123"></a>

## Unveiling the Value of Motion for Cinematic Camera Trajectories

[官方论文页](https://neurips.cc/virtual/2026/poster/154123) · [作者来源](https://openreview.net/forum?id=G6OlxDRMK9)

- **问题 / 瓶颈** · 逐帧位置表示不显式提供镜头运动和导演意图。
- **核心创新 / 方法** · 在轨迹与文本双向任务比较分解表示。
- **Baseline** · 逐帧位姿编码。
- **Benchmark** · 轨迹到文本、文本到轨迹。
- **关键结果 / 消融** · 摘要报告两个方向均改善。
- **适用条件 / 局限** · 限电影轨迹，摘要未给其他硬件控制。

**可复用机制** · 运动语义主要取决于变化时，给方向和速度单独表征再处理绝对位姿。

<a id="paper-151223"></a>

## UpSafe℃: Upcycling for Controllable Safety in Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151223) · [作者来源](https://openreview.net/forum?id=c0mcgI6A3n)

- **问题 / 瓶颈** · 全模型静态修改可能影响正常任务。
- **核心创新 / 方法** · 将敏感层的前馈模块改为带安全专家和路由的稀疏层。
- **Baseline** · 静态安全对齐及原模型。
- **Benchmark** · 语言模型安全与普通效用。
- **关键结果 / 消融** · 摘要报告可控并支持动态安全干预。
- **适用条件 / 局限** · 依赖安全层识别和路由校准。

**可复用机制** · 在架构可能分离任务和安全能力时验证按需介入，单独测良性误阻。

<a id="paper-149965"></a>

## Urbex: Agentic Spatial Grounding for City-Scale 3D Scenes

[官方论文页](https://neurips.cc/virtual/2026/poster/149965) · [作者来源](https://openreview.net/forum?id=ls2ORqqsqZ)

- **问题 / 瓶颈** · 单视角或固定候选难消解同类对象。
- **核心创新 / 方法** · 代理使用局部地图及斜视观测，用平滑定位奖励习得工具顺序。
- **Baseline** · 城市尺度排序法及任务对照。
- **Benchmark** · CityRefer 与 STPLS3D-Refer，Hit@1 与 IoU。
- **关键结果 / 消融** · 摘要报告 CityRefer 表现最佳且具跨场景泛化。
- **适用条件 / 局限** · 依赖可调用的空间观察接口。

**可复用机制** · 定位系统应按不确定性主动判断哪些新视角有用，而非只重排旧候选。

<a id="paper-150077"></a>

## URDF-Anything+: End-to-End Generation for Simulation-Ready Articulated Assets

[官方论文页](https://neurips.cc/virtual/2026/poster/150077) · [作者来源](https://openreview.net/forum?id=kuegPlpgT1)

- **问题 / 瓶颈** · 分开几何重建和关节拟合可能失配。
- **核心创新 / 方法** · 用结构潜空间和自回归扩散共同建模二者。
- **Baseline** · 分阶段资产生成。
- **Benchmark** · 单图 URDF 构造和仿真到现实操作。
- **关键结果 / 消融** · 摘要报告改善并演示只在仿真训练的零样本部署。
- **适用条件 / 局限** · 依赖可用的资产表示，摘要未给物理参数可靠尺度。

**可复用机制** · 有交互需求时，应同时生成决定外观和可动性的结构，减少后置绑定。

<a id="paper-149641"></a>

## Urgency-Aware Autoregressive VLMs for Unanticipated Healthcare Occurrences

[官方论文页](https://neurips.cc/virtual/2026/poster/149641) · [作者来源](https://openreview.net/forum?id=oZu1lEHGvj)

- **问题 / 瓶颈** · 所有事件立即进入响应会反复中断，全部延期可能错过急事。
- **核心创新 / 方法** · 并发运行时间紧迫性评估后决定是否切换。
- **Baseline** · 立即与延后处理。
- **Benchmark** · 动态医疗场景及多种视觉语言模型。
- **关键结果 / 消融** · 报告多设置节省后续 token 且开销有限。
- **适用条件 / 局限** · 误判紧迫可能有严重后果，摘要未给校准阈值。

**可复用机制** · 设计可打断智能体时把事件优先级与当前任务生成分离。

<a id="paper-154348"></a>

## USAD: Uncertainty-aware Statistical Adversarial Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/154348) · [作者来源](https://openreview.net/forum?id=EGs2nZVWS3)

- **问题 / 瓶颈** · 单一分布距离可能漏检局部不稳定的样本。
- **核心创新 / 方法** · 将全局特征离散度与局部一致性结合成统计检测。
- **Baseline** · 最大均值差异等方法。
- **Benchmark** · 视觉防御测试的多种风险条件。
- **关键结果 / 消融** · 摘要报告结合两类不确定性改善检测。
- **适用条件 / 局限** · 依赖稳定性参照，摘要未给自然偏移误报。

**可复用机制** · 不要将群体统计和单样本行为稳定性互相替代，应分别监控。

<a id="paper-148715"></a>

## Useful Memories Become Faulty When Continuously Updated by LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/148715) · [作者来源](https://openreview.net/forum?id=vagovELSsT)

- **问题 / 瓶颈** · 每轮重写可让有用经验逐渐失真。
- **核心创新 / 方法** · 用持续更新和从真值抽象对照无记忆过程。
- **Baseline** · 无记忆与不同抽象方案。
- **Benchmark** · ARC-AGI 中先前答对的一组任务。
- **关键结果 / 消融** · 即便从真值抽象，GPT-5.4 的所测任务中 54% 再答时失败。
- **适用条件 / 局限** · 所测样本为特定子集，不能当全部准确率。

**可复用机制** · 代理新记忆先按证据保留并有门控地合并，再进行保留能力回归测试。

<a id="paper-155845"></a>

## User Embeddings are Superpositions of Interpretable Behavioral Modes

[官方论文页](https://neurips.cc/virtual/2026/poster/155845) · [作者来源](https://openreview.net/forum?id=2T4hO6DOUD)

- **问题 / 瓶颈** · 稠密向量难追溯由哪些行为组成。
- **核心创新 / 方法** · 对冻结用户表示做稀疏字典恢复，并命名模式。
- **Baseline** · 普通用户嵌入。
- **Benchmark** · 已知真值合成及真实用户表征。
- **关键结果 / 消融** · 摘要报告可解释模式及有竞争力的行为表征。
- **适用条件 / 局限** · 命名需人工校验，隐空间线性性是近似。

**可复用机制** · 审查个性化系统时比较模式组合和整体向量，而非只解读一个单一用户标签。

<a id="paper-151319"></a>

## Utility-Constrained Policy Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/151319) · [作者来源](https://openreview.net/forum?id=bNRLgYY6QD)

- **问题 / 瓶颈** · 风险中性约束会漏掉代价尾部。
- **核心创新 / 方法** · 扩展 CMDP 支持风险效用，并做策略优化。
- **Baseline** · 已有安全强化学习。
- **Benchmark** · Safety Gymnasium 的多任务。
- **关键结果 / 消融** · 摘要报告可匹配或超过现行方案。
- **适用条件 / 局限** · 需选接近部署风险偏好的效用。

**可复用机制** · 若平均安全代价掩盖事故风险，要同时验证尾部约束和普通任务表现。

<a id="paper-154062"></a>

## Utility-Driven Clustered Federated Learning via Class-wise Interaction Attribution

[官方论文页](https://neurips.cc/virtual/2026/poster/154062) · [作者来源](https://openreview.net/forum?id=GUPVvqCuHV)

- **问题 / 瓶颈** · 客户端表面相近不代表共享训练能改善泛化。
- **核心创新 / 方法** · FedCap 量化逐类更新贡献后分组。
- **Baseline** · 基于相似性的联邦聚类。
- **Benchmark** · 多种异质配置。
- **关键结果 / 消融** · 摘要报告准确度提升。
- **适用条件 / 局限** · 边际效用估计可能额外消耗验证资源。

**可复用机制** · 选择共享训练对象前先测试它们对不同类别具体有什么影响。

<a id="paper-153247"></a>

## UtoMe: Observation-Uncertainty-Guided Token Merging for Weather Foundation Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153247) · [作者来源](https://openreview.net/forum?id=MepgP6Rx39)

- **问题 / 瓶颈** · 相似度不区分任务敏感证据与观测噪声。
- **核心创新 / 方法** · 依据集合预测分散度，保留预测敏感的高可靠 patch 作锚。
- **Baseline** · 现有天气 token 合并。
- **Benchmark** · 天气基础模型的训练效率及预报。
- **关键结果 / 消融** · FLOPs 最多降低 45%。
- **适用条件 / 局限** · 需要集合观测离散度，摘要未给跨系统结果。

**可复用机制** · 压缩物理观测时用可信度帮助预算分配，而不只排序嵌入相似度。

<a id="paper-153858"></a>

## UTOPI: Efficient Egocentric Long-Video Understanding in AR via User-Guided Token Pre-Compression

[官方论文页](https://neurips.cc/virtual/2026/poster/153858) · [作者来源](https://openreview.net/forum?id=ICcMtlCHJL)

- **问题 / 瓶颈** · 静态裁剪可能重复视角背景而删任务相关前景。
- **核心创新 / 方法** · 运动线索先裁冗余，眼球追踪信号分配前景和背景预算。
- **Baseline** · 既有长视频压缩。
- **Benchmark** · 多基准和多视频模型，压缩与任务效果。
- **关键结果 / 消融** · 摘要报告最多少 95% token 且保持表现。
- **适用条件 / 局限** · 依赖眼动与运动传感器，注视不总代表任务重要性。

**可复用机制** · 多传感第一视角可用低开销人体行为线索动态调视频保留量。

<a id="paper-152475"></a>

## V2M-Zero: Zero-Pair Time-Aligned Video-to-Music Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/152475) · [作者来源](https://openreview.net/forum?id=SnU3xpuCox)

- **问题 / 瓶颈** · 视频和音乐内容难直接配对，但节奏可共享。
- **核心创新 / 方法** · 各模态分别以自身相似度建立事件变化曲线，再用于对齐。
- **Baseline** · 依赖配对视听监督的方案。
- **Benchmark** · 无配对视频到音乐，时间和风格控制。
- **关键结果 / 消融** · 摘要报告多个控制维度可独立设定。
- **适用条件 / 局限** · 同步不等于语义匹配，摘要未给量化质量。

**可复用机制** · 不同模态只共用时间结构时，可以单独建各自表征，再对齐变化时点。

<a id="paper-149449"></a>

## Validating Causal Abstraction Metrics on Simulated Complex Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/149449) · [作者来源](https://openreview.net/forum?id=q05m7XZ9Y9)

- **问题 / 瓶颈** · 拟合观测表示不保证抽象能保真描述干预
- **核心创新 / 方法** · 定义连续因果抽象误差与显式忠实检验
- **Baseline** · 现有因果抽象指标
- **Benchmark** · 多个受控复杂系统和抽样干预
- **关键结果 / 消融** · 在测试系统均通过区分实验，少至 30 次干预收敛
- **适用条件 / 局限** · 需能获得真实或可靠仿真干预

**可复用机制** · 为世界模型状态抽象单独验证行为扰动下的保持关系

<a id="paper-155274"></a>

## Valid Best-Model Identification for LLM Evaluation via Low-Rank Factorization

[官方论文页](https://neurips.cc/virtual/2026/poster/155274) · [作者来源](https://openreview.net/forum?id=6uU921FkRV)

- **问题 / 瓶颈** · 模型和样本自适应选取使普通置信区间失效
- **核心创新 / 方法** · 利用低秩结果结构，并对无放回样本构造有效区间
- **Baseline** · 全量评测及普通抽样
- **Benchmark** · 真实 LLM 基准；最佳模型识别、评估数及成本
- **关键结果 / 消融** · 摘要报告减少评估仍可识别最佳模型
- **适用条件 / 局限** · 任务或模型关系需可用低秩近似

**可复用机制** · 最强模型未知时为自动止测增加置信校准

<a id="paper-152707"></a>

## Value-Aware Stochastic KV Cache Eviction for Reasoning Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152707) · [作者来源](https://openreview.net/forum?id=R0GnMD9bkE)

- **问题 / 瓶颈** · 固定显存部署难支持逐题变化的缓存选择
- **核心创新 / 方法** · 用价值感知随机淘汰，持续保持容量上限
- **Baseline** · 相同稀疏率的强缓存选择及淘汰法
- **Benchmark** · Qwen3、六推理任务，四倍压缩
- **关键结果 / 消融** · 平均持平或更好；关键因子改善其他淘汰法约五点
- **适用条件 / 局限** · 依赖价值代理和任务，随机估计需种子复核

**可复用机制** · 给在线缓存同时设固定显存和关键上下文召回目标

<a id="paper-149802"></a>

## Value-Priced Uncertainty: A Family of PPO-Compatible Exploration Bonuses

[官方论文页](https://neurips.cc/virtual/2026/poster/149802) · [作者来源](https://openreview.net/forum?id=nFeALs705V)

- **问题 / 瓶颈** · 罕见状态估计不准不一定值得探索
- **核心创新 / 方法** · 用局部价值敏感度权衡不确定性并做实现消融
- **Baseline** · RND、ICM、RE3、VCSE、OPPO
- **Benchmark** · PPO 兼容多任务，摘要未列名称
- **关键结果 / 消融** · 多数任务更优，余下有竞争力，消融支持价值敏感度
- **适用条件 / 局限** · 早期 critic 可能不准，需要日程校准

**可复用机制** · 在机器人探索中优先验证对回报影响大的未知状态

<a id="paper-154788"></a>

## Variance-Averse n-Step Offline Reinforcement Learning for Sparse Long-Horizon Environments

[官方论文页](https://neurips.cc/virtual/2026/poster/154788) · [作者来源](https://openreview.net/forum?id=AytpRK1tDD)

- **问题 / 瓶颈** · 均值最优动作可能依赖很少数据或偶然回报
- **核心创新 / 方法** · 在类别分布上重新分配质量与 n 步回报结合
- **Baseline** · CVaR、均值方差及强离线控制基线
- **Benchmark** · D4RL 和 OGBench 超过 40 任务
- **关键结果 / 消融** · 最长程高方差任务收益最大，未列数字
- **适用条件 / 局限** · 过保守可能漏过难得但有效的高值动作

**可复用机制** · 给离线动作选择比较均值和风险调整回报的成功率

<a id="paper-151544"></a>

## Variance-Optimal State Resampling for Reinforcement Learning with Verifiable Rewards

[官方论文页](https://neurips.cc/virtual/2026/poster/151544) · [作者来源](https://openreview.net/forum?id=ZqLrUQLTaa)

- **问题 / 瓶颈** · 从头重复采样浪费已熟练策略前缀
- **核心创新 / 方法** · 复用回放前缀，用免额外模型调用的方差代理重采样
- **Baseline** · GRPO、GiGPO
- **Benchmark** · 数学推理、Sokoban 与 BabyAI
- **关键结果 / 消融** · 大部分任务性能提升且每更少生成 token
- **适用条件 / 局限** · 现有回放需要处理策略变化和分布偏差

**可复用机制** · 实测不同前缀的更新方差，再设采样率

<a id="paper-153246"></a>

## Variance Reduction for Expectations with Diffusion Teachers

[官方论文页](https://neurips.cc/virtual/2026/poster/153246) · [作者来源](https://openreview.net/forum?id=Mf2Qoh2jGX)

- **问题 / 瓶颈** · 独立样本估计期望成本高
- **核心创新 / 方法** · 摊销重复计算，并用重要性权重和逆 CDF 分层
- **Baseline** · 标准扩散教师抽样
- **Benchmark** · 多引导任务，含 DMD 对照
- **关键结果 / 消融** · 有效计算提升 2–3 倍，重要性和分层再加约 25%，DMD 无同等下游收益
- **适用条件 / 局限** · 降估计方差不保证下游提升

**可复用机制** · 分别验收估计效率、轨迹偏差和最终质量
