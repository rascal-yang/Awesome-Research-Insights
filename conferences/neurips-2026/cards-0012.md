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

<a id="paper-149599"></a>

## Variational Consequence-Driven Offline Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149599) · [作者来源](https://openreview.net/forum?id=ou9IEnOfiY)

- **问题 / 瓶颈** · 直接正则难表示影响等价的动作。
- **核心创新 / 方法** · 用闭式潜散度近似难算的结构行为约束。
- **Baseline** · 既有离线强化学习。
- **Benchmark** · 多离线 RL 基准。
- **关键结果 / 消融** · 摘要称持续更强，幅度未核。
- **适用条件 / 局限** · 依赖潜表示充分性。

**可复用机制** · 区分动作表面相似与后果一致。

<a id="paper-152888"></a>

## Variational Inference via Entropic Transport Descent

[官方论文页](https://neurips.cc/virtual/2026/poster/152888) · [作者来源](https://openreview.net/forum?id=Pe1qlDnrcO)

- **问题 / 瓶颈** · 单粒子或局部更新会漏多峰。
- **核心创新 / 方法** · 熵正则 OT 将粒子配到附近高密度候选。
- **Baseline** · SVGD、AGF-SVGD、SGLD。
- **Benchmark** · 方差塌缩、贝叶斯逻辑和神经网络。
- **关键结果 / 消融** · 高维与多峰增益更突出。
- **适用条件 / 局限** · 需可评未归一密度，输运成本需测。

**可复用机制** · 先用多峰覆盖验证推断核再验平均误差。

<a id="paper-153361"></a>

## Variational Trajectory Optimization of Anisotropic Diffusion Schedules

[官方论文页](https://neurips.cc/virtual/2026/poster/153361) · [作者来源](https://openreview.net/forum?id=LwTBXZvDas)

- **问题 / 瓶颈** · 不同方向去噪难度不一。
- **核心创新 / 方法** · 对矩阵值路径做变分优化。
- **Baseline** · EDM。
- **Benchmark** · CIFAR-10、AFHQv2、FFHQ、ImageNet-64，各 NFE。
- **关键结果 / 消融** · 多预算一致改善。
- **适用条件 / 局限** · 矩阵噪声参数规模及泛化需复测。

**可复用机制** · 把噪声方案与表示几何共同设计。

<a id="paper-151186"></a>

## VAR-Q: Tuning-free KV Cache Quantization for Visual Autoregressive Image and Video Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/151186) · [作者来源](https://openreview.net/forum?id=cKR2ed5g34)

- **问题 / 瓶颈** · 照搬文本缓存压缩易错配。
- **核心创新 / 方法** · 根据缓存分析沿两轴构造无需调参分组。
- **Baseline** · 既有缓存量化。
- **Benchmark** · 视觉自回归图像与视频生成。
- **关键结果 / 消融** · 摘要给出定制分组，数值待核。
- **适用条件 / 局限** · 两轴特征依赖模型架构。

**可复用机制** · 量化前测各生成阶段和通道统计异质性。

<a id="paper-152719"></a>

## VASR: Variance-Aware Systematic Resampling for Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152719) · [作者来源](https://openreview.net/forum?id=QqtrK76QV1)

- **问题 / 瓶颈** · 多项式重采样会让粒子后代数过散。
- **核心创新 / 方法** · 用系统重采样和方差分解，噪声大奖励有高选择变体。
- **Baseline** · 多项式重采样。
- **Benchmark** · 奖励引导扩散 SMC。
- **关键结果 / 消融** · 分析多样性坍缩；高选择变体有意带偏。
- **适用条件 / 局限** · 偏差及延续噪声需分开验。

**可复用机制** · 先降低可控重采样方差再提高选择强度。

<a id="paper-155578"></a>

## V-CAST: Video Curvature-Aware Spatio-Temporal Pruning for Efficient Video Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155578) · [作者来源](https://openreview.net/forum?id=4ZHrSIJv8q)

- **问题 / 瓶颈** · 粗帧预算会漏连续事件，合并会扰坐标。
- **核心创新 / 方法** · 免训练按时空曲率决定保留。
- **Baseline** · 每帧配额、分段及合并。
- **Benchmark** · 多架构视频 LLM 长上下文 prefill。
- **关键结果 / 消融** · 摘要报告评估，幅度待核。
- **适用条件 / 局限** · 低曲率小目标可能仍关键。

**可复用机制** · 削预算前以坐标和事件召回验证。

<a id="paper-152275"></a>

## VC-OPD: Visual Counterfactual On-Policy Distillation for Grounded Vision-Language Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/152275) · [作者来源](https://openreview.net/forum?id=UIRHh7xJPJ)

- **问题 / 瓶颈** · 长推理中语言模式会压视觉。
- **核心创新 / 方法** · 先格式暖启，对每轨迹比较同教师的原图与破坏图像证据。
- **Baseline** · 普通在策略蒸馏。
- **Benchmark** · 视频或图像语言多模态推理基准。
- **关键结果 / 消融** · 摘要称视觉推理改善。
- **适用条件 / 局限** · 反事实图需保其他语义。

**可复用机制** · 构造同上下文视觉反事实为局部训练加权。

<a id="paper-155491"></a>

## VCR: Learning Valid Contextual Representation for Incomplete Wearable Signals

[官方论文页](https://neurips.cc/virtual/2026/poster/155491) · [作者来源](https://openreview.net/forum?id=5BWCy21RFh)

- **问题 / 瓶颈** · 固定融合对多缺模态不稳。
- **核心创新 / 方法** · 自监督学有效表示，缺失感知专家读 token。
- **Baseline** · 强监督和自监督。
- **Benchmark** · 可穿戴健康监测，完整及各缺失组合。
- **关键结果 / 消融** · 各缺失设置改善。
- **适用条件 / 局限** · 未见传感器和时间漂移需验。

**可复用机制** · 按实际传感组合而非均匀随机遮盖设计缺失训练。

<a id="paper-139354"></a>

## VecDBLens: A Modular Framework for Diagnosing Vector Databases  Retrieval Pipelines

[官方论文页](https://neurips.cc/virtual/2026/poster/139354) · [作者来源](https://openreview.net/forum?id=UtVlO4agwp)

- **问题 / 瓶颈** · 固定嵌入下容易误怪索引。
- **核心创新 / 方法** · 换一模块时匹配数据、参数及运行条件。
- **Baseline** · 只评索引。
- **Benchmark** · 向量库检索管线。
- **关键结果 / 消融** · 发现许多表面索引问题真正由嵌入限制。
- **适用条件 / 局限** · 需控制运行条件。

**可复用机制** · 端到端检索回归每次只动一个组件。

<a id="paper-156076"></a>

## VecUQ-OT: Aggregating Uncertainty Measures via Multivariate Ranks

[官方论文页](https://neurips.cc/virtual/2026/poster/156076) · [作者来源](https://openreview.net/forum?id=0ca8UlAbiR)

- **问题 / 瓶颈** · 直接相加对尺度和失效来源敏感。
- **核心创新 / 方法** · 熵正则 OT 汇总成单一排序。
- **Baseline** · 加性融合。
- **Benchmark** · 合成、图像、文本。
- **关键结果 / 消融** · 在个别指标失效时仍较稳。
- **适用条件 / 局限** · 也可能所有信号共同失准。

**可复用机制** · 用于弃权前核集成对相关错误的鲁棒。

<a id="paper-150521"></a>

## Velocity Ambiguity Profiles: Time-Resolved Bayes-Risk Diagnostics for Flow Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/150521) · [作者来源](https://openreview.net/forum?id=hU5qsz0CsX)

- **问题 / 瓶颈** · 固有速度歧义不会由加数据消除。
- **核心创新 / 方法** · 拆贝叶斯底线和有限样本余量。
- **Baseline** · 按原总损失重采样。
- **Benchmark** · 受控高斯混合、代理及抽样验证。
- **关键结果 / 消融** · 余量代理可降可降部分，跨格敏感限制强采样。
- **适用条件 / 局限** · 真实分布的底线难直接算。

**可复用机制** · 高损失时间步须先判断误差是否可学。

<a id="paper-148308"></a>

## Velocity-Space 3D Asset Editing

[官方论文页](https://neurips.cc/virtual/2026/poster/148308) · [作者来源](https://openreview.net/forum?id=yoa8hWDC5H)

- **问题 / 瓶颈** · 先反演和像素提升会带来误差。
- **核心创新 / 方法** · 无需反演、训练和掩码的采样内修改。
- **Baseline** · 原生 3D 及多视提升编辑。
- **Benchmark** · 多类 3D 资产。
- **关键结果 / 消融** · 摘要称领先，幅度未核。
- **适用条件 / 局限** · 复杂局部选择效果需单测。

**可复用机制** · 将生成编辑的误差来源按采样步骤消融。

<a id="paper-148885"></a>

## Vendi Anomaly Scores for Efficient and Accurate Anomaly Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/148885) · [作者来源](https://openreview.net/forum?id=uT5yKtgYS0)

- **问题 / 瓶颈** · 局部距离未衡量对整体集合影响。
- **核心创新 / 方法** · 用 Vendi Score 的 leave-one-out 差。
- **Baseline** · 现有异常方法。
- **Benchmark** · ImageNet 大规模和不同污染比例。
- **关键结果 / 消融** · 提高规模和污染仍稳。
- **适用条件 / 局限** · 依赖相似核和计算近似。

**可复用机制** · 集合异常度可用样本对全局多样的边际贡献。

<a id="paper-139699"></a>

## VeriContest: A Competitive-Programming Benchmark for Verifiable Code Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/139699) · [作者来源](https://openreview.net/forum?id=9vAOEu7dQE)

- **问题 / 瓶颈** · 普通测试通过夸大机器可证能力。
- **核心创新 / 方法** · 对规范、代码、证明单独及组合测试。
- **Baseline** · 十强模型自然语言到代码。
- **Benchmark** · VeriContest，分阶段成功率。
- **关键结果 / 消融** · 最好代码 92.18%，端到端 5.29%，证明 13.95%。
- **适用条件 / 局限** · 需证明语言能力和规范覆盖。

**可复用机制** · 工具代理代码验收设可核规格与证据两关。

<a id="paper-152908"></a>

## Verifiable Environments Are LEGO Bricks: Recursive Composition for Reasoning Generalization

[官方论文页](https://neurips.cc/virtual/2026/poster/152908) · [作者来源](https://openreview.net/forum?id=PUqSH8cFqy)

- **问题 / 瓶颈** · 手工创建线性扩张慢。
- **核心创新 / 方法** · 将验证环境作模块递归合并。
- **Baseline** · 单独环境手工构造。
- **Benchmark** · DeepSeek-R1-Distill-Qwen-14B、Qwen3-14B。
- **关键结果 / 消融** · 前者平均 48.2 到 51.3。
- **适用条件 / 局限** · 语义组合须保验证正确。

**可复用机制** · 扩大训练不只堆实例，还增可验规则组合。

<a id="paper-149396"></a>

## Verification-Aware Training for Speculative Decoding

[官方论文页](https://neurips.cc/virtual/2026/poster/149396) · [作者来源](https://openreview.net/forum?id=qMv8q5WApK)

- **问题 / 瓶颈** · 独立草稿训练不直接优化接受模式。
- **核心创新 / 方法** · 训练位置级接受预测头并使用验证反馈。
- **Baseline** · 普通推测草稿训练。
- **Benchmark** · Qwen3、LLaMA3.1 的数学、代码、聊天。
- **关键结果 / 消融** · 平均接受长度最多增 11.4%，墙钟提速最多增 8.7%。
- **适用条件 / 局限** · 依赖目标验证器。

**可复用机制** · 草稿模型训练应直接反映部署时的接受判据。

<a id="paper-155607"></a>

## Verification-Guided Abstraction Generation with Large Language Models for Generalized Planning

[官方论文页](https://neurips.cc/virtual/2026/poster/155607) · [作者来源](https://openreview.net/forum?id=4JHc9P6xNp)

- **问题 / 瓶颈** · 模型生成的抽象可能只适配少数训练实例。
- **核心创新 / 方法** · 生成候选 QNP 后用结构化错误修订。
- **Baseline** · 未经验证的抽象生成。
- **Benchmark** · PDDL 领域和实例泛化。
- **关键结果 / 消融** · 摘要报告可跨实例转移。
- **适用条件 / 局限** · 需具备符号规格。

**可复用机制** · 让模型提案，独立规划验证器提供可检查的修复依据。

<a id="paper-150614"></a>

## Verified-Source Authority Is Not Generic Sycophancy: Cue-Family Decomposition of LLM Compliance

[官方论文页](https://neurips.cc/virtual/2026/poster/150614) · [作者来源](https://openreview.net/forum?id=gpiTlXxy4C)

- **问题 / 瓶颈** · 表面上同一种服从可能对应不同机制。
- **核心创新 / 方法** · 固定答案并交换背书来源，另验证表征方向。
- **Baseline** · 权威、用户和中性条件。
- **Benchmark** · 事实题、PIQA、MMLU-Pro 与 GSM8K。
- **关键结果 / 消融** · 四个开放家族出现明显差异。
- **适用条件 / 局限** · 受所测提示和模型限制。

**可复用机制** · 评估引用信任时只改变来源标签，避免与答案难度混淆。

<a id="paper-148814"></a>

## Verifier-Backed Hard Problem Generation for Mathematical Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/148814) · [作者来源](https://openreview.net/forum?id=uuzIPLUUKL)

- **问题 / 瓶颈** · 题目生成者可通过无效题人为提高难度。
- **核心创新 / 方法** · 第三方验证器与解题者共同决定奖励。
- **Baseline** · 出题者和解题者的双边自博弈。
- **Benchmark** · 数学推理任务。
- **关键结果 / 消融** · 摘要报告明显优于基线。
- **适用条件 / 局限** · 依赖有效验证器。

**可复用机制** · 难度奖励只有在任务有效后才有意义。

<a id="paper-138925"></a>

## Verifier Choice is a Benchmark Design Variable: Auditing Structural Counting Evaluation in Text-to-Image Models

[官方论文页](https://neurips.cc/virtual/2026/poster/138925) · [作者来源](https://openreview.net/forum?id=wUGdrU38xm)

- **问题 / 瓶颈** · 总分可能掩盖拒评和偏差。
- **核心创新 / 方法** · 对七类结构逐图对比计数及人工判定。
- **Baseline** · 不同视觉计数验证器。
- **Benchmark** · 独立对象和依附子结构计数。
- **关键结果 / 消融** · 摘要提出六类配套诊断。
- **适用条件 / 局限** · 小范围类别。

**可复用机制** · 在同批生成结果上检查验证器的误报和拒评，再比较生成器。

<a id="paper-155211"></a>

## Verifiers in the Loop: Decoding Time Verification for Code Translation

[官方论文页](https://neurips.cc/virtual/2026/poster/155211) · [作者来源](https://openreview.net/forum?id=7RvjiiRX0n)

- **问题 / 瓶颈** · 早期错误会进入后续自回归上下文。
- **核心创新 / 方法** · 状态机交替调度生成和确定性验证。
- **Baseline** · 事后验证及采样扩展。
- **Benchmark** · 代码翻译成本与正确率。
- **关键结果 / 消融** · 摘要报告更好折中。
- **适用条件 / 局限** · 需要支持前缀的检查。

**可复用机制** · 对可执行生成可优先在便宜且有意义的边界检查。

<a id="paper-139856"></a>

## Verifying Agents in Rubric-Graded Environments

[官方论文页](https://neurips.cc/virtual/2026/poster/139856) · [作者来源](https://openreview.net/forum?id=08X5C49LWf)

- **问题 / 瓶颈** · 通用评判无法核实工作环境的实际状态。
- **核心创新 / 方法** · 从细则构造能力分类及环境对齐原则。
- **Baseline** · 其它自动评审。
- **Benchmark** · 21 项任务与 3204 条人工细则，并测试 OpenClaw。
- **关键结果 / 消融** · 跨环境 F1 为 0.951。
- **适用条件 / 局限** · 依赖人工细则和状态访问。

**可复用机制** · 设计代理评审器从必须核实的事实出发选择能力。

<a id="paper-152311"></a>

## Verifying Neural Networks with Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/152311) · [作者来源](https://openreview.net/forum?id=U2N3YhilwS)

- **问题 / 瓶颈** · 单步分数不衡量整棵树代价。
- **核心创新 / 方法** · actor-critic 学习在现有启发式上调整。
- **Baseline** · 先进固定启发式。
- **Benchmark** · 600 个神经网络验证实例。
- **关键结果 / 消融** · 多解决 11%，分支少 50%。
- **适用条件 / 局限** · 需验证训练数据。

**可复用机制** · 保持验证正确性算法不变，只学习决定计算顺序。

<a id="paper-149921"></a>

## VerifyMAS: Hypothesis Verification for Failure Attribution in LLM Multi-Agent Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/149921) · [作者来源](https://openreview.net/forum?id=mCxhih62ys)

- **问题 / 瓶颈** · 一次预测代理与步骤组合的搜索空间很大。
- **核心创新 / 方法** · 逐假设验证协调错误。
- **Baseline** · 直接预测错误代理与类型。
- **Benchmark** · 多代理长轨迹、Qwen 及 GPT。
- **关键结果 / 消融** · 摘要报告提高归因且未降低效率。
- **适用条件 / 局限** · 依赖提出的假设覆盖真错因。

**可复用机制** · 长流程排障应保留显式可反驳假设。

<a id="paper-139424"></a>

## VerifyThisBench: Joint Evaluation of Code, Specifications, and Proof

[官方论文页](https://neurips.cc/virtual/2026/poster/139424) · [作者来源](https://openreview.net/forum?id=RZTeyoxP6N)

- **问题 / 瓶颈** · 对错误规格的有效证明仍可能答错。
- **核心创新 / 方法** · 并列机器证明和独立任务测试。
- **Baseline** · 六个先进模型及七种验证工具。
- **Benchmark** · 1078 项任务。
- **关键结果 / 消融** · 通过证明的程序中只有部分符合真正意图。
- **适用条件 / 局限** · 测试无完备性保证。

**可复用机制** · 所有验证链应再检查规格是否对应用户需要。

<a id="paper-151870"></a>

## VeriGraph: Towards Verifiable Data-Analytic Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/151870) · [作者来源](https://openreview.net/forum?id=XHH1MUulfY)

- **问题 / 瓶颈** · 最终结论难回溯到输入和计算。
- **核心创新 / 方法** · 构造异构有向无环图连接状态。
- **Baseline** · 普通分析代理。
- **Benchmark** · 可验证的数据分析。
- **关键结果 / 消融** · 摘要报告显示证据图可支持检查。
- **适用条件 / 局限** · 图构建成本未报告。

**可复用机制** · 以结果出处为图边，便于逐条核查结论。

<a id="paper-148411"></a>

## VERITAS: Veracity-Enhanced Robust Identification of LLM-generated Text Against Style-shifts

[官方论文页](https://neurips.cc/virtual/2026/poster/148411) · [作者来源](https://openreview.net/forum?id=y30cLhgUpI)

- **问题 / 瓶颈** · 原始测试高精度可能来自写作风格。
- **核心创新 / 方法** · 比较风格变化前后的检测及专门检测模型。
- **Baseline** · 通用模型与较强专门检测器。
- **Benchmark** · 机器生成文本识别。
- **关键结果 / 消融** · 摘要报告准确度下降最高 11.43%。
- **适用条件 / 局限** · 限所测模型与文体。

**可复用机制** · 评价内容来源检测时，与写作形式无关的证据更值得投入。

<a id="paper-139095"></a>

## VeriWorld: A Verifiable Visual SWE-Bench for Spatial Reasoning in 3D Environments

[官方论文页](https://neurips.cc/virtual/2026/poster/139095) · [作者来源](https://openreview.net/forum?id=lLZbYegc4T)

- **问题 / 瓶颈** · 交互协议本身可混淆空间能力。
- **核心创新 / 方法** · 用确定性环境验证三组对照。
- **Baseline** · 不同表示和互动协议。
- **Benchmark** · 可执行三维空间推理。
- **关键结果 / 消融** · 摘要报告协议为实质混淆。
- **适用条件 / 局限** · 仿真环境限制外推。

**可复用机制** · 保持场景和目标不变，切换表示以定位感知还是决策问题。

<a id="paper-153885"></a>

## VersaCamVLA: Camera-Configurable VLA Policies for Robotic Manipulation

[官方论文页](https://neurips.cc/virtual/2026/poster/153885) · [作者来源](https://openreview.net/forum?id=I1cIuU8uQm)

- **问题 / 瓶颈** · 直接堆叠视角易受相机数和位姿变化干扰
- **核心创新 / 方法** · 把视图融合成紧凑场景 token 并接入已训练 VLA
- **Baseline** · 原 VLA 及直接多视图方法
- **Benchmark** · RoboTwin、LIBERO 和真实机器人
- **关键结果 / 消融** · 相机数变化及未见位姿下表现更稳，幅度未报告
- **适用条件 / 局限** · 依赖训练视角覆盖，摘要未给极端遮挡表现

**可复用机制** · 部署适配先匹配同样视觉 token 数再比较融合接口

<a id="paper-155242"></a>

## VESPO: Variational Sequence-level Soft Policy Optimization for Off-Policy LLM Training

[官方论文页](https://neurips.cc/virtual/2026/poster/155242) · [作者来源](https://openreview.net/forum?id=7CJdabpkqi)

- **问题 / 瓶颈** · 旧策略生成的长轨迹使重要性权重方差大
- **核心创新 / 方法** · 用序列级软优化核，区分长度归一化与近似方差
- **Baseline** · 近年权重重塑方法
- **Benchmark** · 计算及数学推理、稠密和 MoE；陈旧度压力
- **关键结果 / 消融** · 最高 64 倍陈旧设置仍稳定，分数未列
- **适用条件 / 局限** · 依赖权重核与生成调度，极端分布变化需检查

**可复用机制** · 为采样与训练解耦服务设置陈旧度—质量曲线

<a id="paper-155107"></a>

## VGB for Masked Diffusion Model: Efficient Test-time Scaling for Reward Satisfaction and Sample Editing

[官方论文页](https://neurips.cc/virtual/2026/poster/155107) · [作者来源](https://openreview.net/forum?id=8La5KkmM0T)

- **问题 / 瓶颈** · 前向单调揭示易承诺坏的局部决定
- **核心创新 / 方法** · 用带奖励倾斜叶分布的采样，同时允许揭示与重掩码
- **Baseline** · 参考采样、Best-of-N、仅前向价值引导
- **Benchmark** · 结构化约束与修复任务；质量及成本
- **关键结果 / 消融** · 摘要称改善质量成本前沿
- **适用条件 / 局限** · 理论及实测依赖部分状态评分，未覆盖任意自然语言任务

**可复用机制** · 可验证生成中同时比较回退预算与独立多抽样

<a id="paper-149423"></a>

## V-GIFT: Boosting Visual Instruction Tuning with Self-Supervised Guidance

[官方论文页](https://neurips.cc/virtual/2026/poster/149423) · [作者来源](https://openreview.net/forum?id=qA87deiifn)

- **问题 / 瓶颈** · 文字偏重训练可能削弱精细感知
- **核心创新 / 方法** · 把视觉自监督练习改写为可训练指令并控制比例
- **Baseline** · 常规视觉指令微调
- **Benchmark** · 多模型、多训练方式和视觉中心基准
- **关键结果 / 消融** · 仅加 3–10% 样本即持续改善
- **适用条件 / 局限** · 任务配比与训练模型影响收益

**可复用机制** · 数据策划保留少量像素或空间感知练习并独立验收

<a id="paper-154516"></a>

## ViCoR: Estimating Visual Necessity via Counterfactual Residuals for Multimodal Medical Data Selection

[官方论文页](https://neurips.cc/virtual/2026/poster/154516) · [作者来源](https://openreview.net/forum?id=D0DvVACDW0)

- **问题 / 瓶颈** · 高分可能来自文字捷径，边际样本多但无视觉监督
- **核心创新 / 方法** · 用反事实残差估计视觉必要性并筛样本
- **Baseline** · 全数据微调和其他选择器
- **Benchmark** · 多模态医学数据与多病种鲁棒性基准
- **关键结果 / 消融** · 20% 子集均分最强，扰动诊断显示图像依赖增强
- **适用条件 / 局限** · 医疗域结果需跨视觉任务核验

**可复用机制** · 设置去图、区域遮挡和完整图回归来检验选择器

<a id="paper-151290"></a>

## VICO: Visual Environments Co-Evolving for Vision-Language Model Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/151290) · [作者来源](https://openreview.net/forum?id=bWQSO81TTf)

- **问题 / 瓶颈** · 纯文本自博弈较少提供新的感知挑战
- **核心创新 / 方法** · 让视觉环境与模型共演化并比较文本编辑
- **Baseline** · 自演化、文字协同训练和图表 RLVR
- **Benchmark** · 图表与分布外视觉推理
- **关键结果 / 消融** · 对 OOD 最高增 5.0%，比文本共演化高 8.4%
- **适用条件 / 局限** · 摘要未列跨自然场景验证

**可复用机制** · 优先做视觉因素可控的难题生成及标注成本对照

<a id="paper-155230"></a>

## Video-FLAIR: Not Whether to Reason, But How

[官方论文页](https://neurips.cc/virtual/2026/poster/155230) · [作者来源](https://openreview.net/forum?id=7IM0JvagQT)

- **问题 / 瓶颈** · 总要求推理浪费 token，也可能生成无依据线索
- **核心创新 / 方法** · 按正确、依据与推理成本联合评分不同回答模式
- **Baseline** · 基座 Qwen2.5-VL 和始终推理
- **Benchmark** · MathVista、Video-Holmes、Video-MMMU；准确率和 token
- **关键结果 / 消融** · 分别高 5.4、4.8、4.8，平均 95 token 对 417
- **适用条件 / 局限** · 仍需校准没有依据或困难视频上的模式选择

**可复用机制** · 以同质量比较按题自适应和固定推理预算

<a id="paper-149484"></a>

## Video Forensic Self-Descriptions: Leveraging Temporally Distributed Forensic Microstructures for Zero-Shot Detection of AI-Generated Videos

[官方论文页](https://neurips.cc/virtual/2026/poster/149484) · [作者来源](https://openreview.net/forum?id=pnZvRHgjWk)

- **问题 / 瓶颈** · 单帧会漏运动近似的联合偏差。
- **核心创新 / 方法** · 用时序取证结构生成可审计诊断描述。
- **Baseline** · 现有零样本合成视频检测。
- **Benchmark** · 多集，35 生成器，检测及描述。
- **关键结果 / 消融** · 摘要报告领先，量未核。
- **适用条件 / 局限** · 新生成器和帧压缩需复测。

**可复用机制** · 对瞬时和跨帧证据分别验鲁棒性。

<a id="paper-148674"></a>

## VideoMaMa++: Temporally Consistent Video Matting via Preserve-and-Refine Tokens

[官方论文页](https://neurips.cc/virtual/2026/poster/148674) · [作者来源](https://openreview.net/forum?id=vxJjCRu1Km)

- **问题 / 瓶颈** · 长滑窗单纯传递上块误差会放大。
- **核心创新 / 方法** · 训练 preserve/refine token；推理跨块接已算 matte，并在每块加全局锚。
- **Baseline** · 现有分块抠像。
- **Benchmark** · 长时序一致性及细化。
- **关键结果 / 消融** · 无需额外训练可使用滑窗接口，量未核。
- **适用条件 / 局限** · 首参考错误以及外观突变需处理。

**可复用机制** · 局部传播旁加独立全局参照以减漂移。

<a id="paper-154317"></a>

## VideoMDM: Towards 3D Human Motion Generation From 2D Supervision

[官方论文页](https://neurips.cc/virtual/2026/poster/154317) · [作者来源](https://openreview.net/forum?id=EYB8rootIX)

- **问题 / 瓶颈** · 普通单目二维监督无法直接恢复深度。
- **核心创新 / 方法** · 用深度加权二维损失，并适配速度一致和表示对齐。
- **Baseline** · 3D 监督 MDM。
- **Benchmark** · HumanML3D、Fit3D、NBA。
- **关键结果 / 消融** · FID 0.88 对真值 0.54，真实视频人工偏好强。
- **适用条件 / 局限** · 深度尺度与姿态估计可靠性重要。

**可复用机制** · 辨认可由观测监督恢复的 3D 维，再引入结构先验。

<a id="paper-156098"></a>

## Video-Mirai: Autoregressive Video Diffusion Models Need Foresight

[官方论文页](https://neurips.cc/virtual/2026/poster/156098) · [作者来源](https://openreview.net/forum?id=0Oqbkn7POo)

- **问题 / 瓶颈** · 当前状态缺后续可见结构。
- **核心创新 / 方法** · 冻结前瞻编码器读全轨迹，停梯度目标蒸馏到因果状态。
- **Baseline** · Causal Forcing。
- **Benchmark** · VBench 5 秒和外推 30 秒。
- **关键结果 / 消融** · 5 秒总分 83.8 到 84.6，30 秒主体一致 84.9 到 88.5。
- **适用条件 / 局限** · 教师只可训练使用，未来预测不能看真实未来。

**可复用机制** · 上线不可见特权信息可做训练目标，不做运行输入。

<a id="paper-153411"></a>

## VideoMLA: Low-Rank Latent KV Cache for Minute-Scale Autoregressive Video Diffusion

[官方论文页](https://neurips.cc/virtual/2026/poster/153411) · [作者来源](https://openreview.net/forum?id=LWMSPE1KSY)

- **问题 / 瓶颈** · 低秩压缩可能从初始化已用满容量。
- **核心创新 / 方法** · 比较随机和谱初始化，做阶段适配。
- **Baseline** · 流式 AR 视频扩散。
- **Benchmark** · VBench 短长序列，B200。
- **关键结果 / 消融** · 短序列相近，长序列最好，吞吐 1.23 倍。
- **适用条件 / 局限** · 具体秩预算取决于段长和硬件。

**可复用机制** · 部署低秩监测占用再配置容量。

<a id="paper-153418"></a>

## Video Models Can Reason with Verifiable Rewards

[官方论文页](https://neurips.cc/virtual/2026/poster/153418) · [作者来源](https://openreview.net/forum?id=LTemJEibp6)

- **问题 / 瓶颈** · 成败稀疏使搜索起步难。
- **核心创新 / 方法** · 在视频扩散上用可判规则反馈并分解。
- **Baseline** · SFT 及开闭视频生成模型。
- **Benchmark** · Maze、FlowFree、Sokoban 及域外。
- **关键结果 / 消融** · 普遍改善，低成功时密集分解尤其关键。
- **适用条件 / 局限** · 需要可解析画面及可信规则。

**可复用机制** · 让视频世界模型在规则可验场景先学有效中间步骤。

<a id="paper-151423"></a>

## Video-Zero: Self-Evolution Video Understanding

[官方论文页](https://neurips.cc/virtual/2026/poster/151423) · [作者来源](https://openreview.net/forum?id=aoXXt7fcDl)

- **问题 / 瓶颈** · 标签自由训练可能循环放大语言猜测。
- **核心创新 / 方法** · 提问者和求解者围绕局部时段证据共演化。
- **Baseline** · 既有视频 VLM 及无定位的自训练。
- **Benchmark** · 13 时间 grounding、长视频与推理基准。
- **关键结果 / 消融** · 多个视频基座持续提高。
- **适用条件 / 局限** · 依赖定位准确和问题多样。

**可复用机制** · 给自训练增证据可见性验收。

<a id="paper-153093"></a>

## VidHalluDoctor: Learning Video Differences to Mitigate Hallucinations in Vision-Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153093) · [作者来源](https://openreview.net/forum?id=O19BzWLPGz)

- **问题 / 瓶颈** · 模型凭语言先验跳过微小视频区别。
- **核心创新 / 方法** · 用差异数据、反事实及理由答案一致奖励。
- **Baseline** · 现有视觉视频后训练。
- **Benchmark** · VidHalluEva，10000 视频。
- **关键结果 / 消融** · 摘要报告改善，幅度待核。
- **适用条件 / 局限** · 需控制反事实不改无关语义。

**可复用机制** · 同时验感知差异与推理是否真正用差异。

<a id="paper-138905"></a>

## VIGOR: Benchmarking Visual Rationale Correctness in Multimodal Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/138905) · [作者来源](https://openreview.net/forum?id=xlHEXHYvlZ)

- **问题 / 瓶颈** · 答对答案不等于逐项理由都由图像支持。
- **核心创新 / 方法** · 复用密集标注并验证补充的概念定位。
- **Baseline** · 不同多模态模型。
- **Benchmark** · VIGOR，多级概念和视觉定位。
- **关键结果 / 消融** · 摘要显示多级概念均存在证据错误。
- **适用条件 / 局限** · 自动标注可能有误差。

**可复用机制** · 评估理由时核验其中每个可定位声明，而不只看语言自然度。

<a id="paper-155830"></a>

## VIGOR: Visual Gain Ordering for Hallucination Mitigation in Multimodal Discrete Diffusion Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155830) · [作者来源](https://openreview.net/forum?id=2ZlTG9IUvR)

- **问题 / 瓶颈** · 语言先验给出的早期高置信会锁定幻觉。
- **核心创新 / 方法** · 用视觉增益排序迭代生成位置。
- **Baseline** · 普通掩码扩散解码。
- **Benchmark** · 多个幻觉和多模态推理基准。
- **关键结果 / 消融** · 摘要报告幻觉减少且推理改善。
- **适用条件 / 局限** · 摘要未给计算开销。

**可复用机制** · 优先提交有传感器增量证据的预测，避免只使用语言置信。

<a id="paper-153294"></a>

## VIGOR: Zero-Shot Visual Generalization via Latent-Space Consistency in Model-Based Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/153294) · [作者来源](https://openreview.net/forum?id=MKDlrS5Ftr)

- **问题 / 瓶颈** · 观测变化导致潜动力学错误跨步累积。
- **核心创新 / 方法** · 让不同外观的同状态潜表示一致。
- **Baseline** · 相同增强及无一致性的模型式 RL。
- **Benchmark** · 零样本未见视觉干扰。
- **关键结果 / 消融** · 摘要报告一致性而非增强选择解释鲁棒性。
- **适用条件 / 局限** · 外观变化必须不改变实际状态。

**可复用机制** · 验证背景变动是否改变同状态编码，再增加增强范围。

<a id="paper-152359"></a>

## Virtual Double Oracle: Faster Convergence by Leveraging Strategies That Were Watching All Along

[官方论文页](https://neurips.cc/virtual/2026/poster/152359) · [作者来源](https://openreview.net/forum?id=TfHtE1Ignc)

- **问题 / 瓶颈** · 晚加入策略从均匀状态起步会丢有用历史。
- **核心创新 / 方法** · 用双线性恒等式恢复新策略的乘法权重状态。
- **Baseline** · 普通 Double Oracle。
- **Benchmark** · 矩阵博弈、扑克、Goofspiel。
- **关键结果 / 消融** · 经验验证渐近率，折扣变体有限步表现更强。
- **适用条件 / 局限** · 依赖可折叠的双线性效用。

**可复用机制** · 可回算新候选历史时，将已花费的探索转化为初始化信息。

<a id="paper-155297"></a>

## Virtual Head Attention

[官方论文页](https://neurips.cc/virtual/2026/poster/155297) · [作者来源](https://openreview.net/forum?id=6chRc0Xfxr)

- **问题 / 瓶颈** · 减少物理头可能丢注意力多样性。
- **核心创新 / 方法** · 组内近恒等查询预混合并引入轻量线性算子。
- **Baseline** · MLA 与 GQA-4。
- **Benchmark** · 12 项基础模型基准。
- **关键结果 / 消融** · 摘要报告平均相对两基线加 0.70% 和 2.60%。
- **适用条件 / 局限** · 部署成本受注意力实现影响。

**可复用机制** · 减少缓存和真实头时可试解耦有效头多样性与物理头数。

<a id="paper-154323"></a>

## Virtual Task Prompting for Multi-Task Scene Understanding

[官方论文页](https://neurips.cc/virtual/2026/poster/154323) · [作者来源](https://openreview.net/forum?id=EXN4VTZJ8q)

- **问题 / 瓶颈** · 任务间依赖与交互通常隐含在共享主干。
- **核心创新 / 方法** · 由可训练路由从虚拟任务读出与图像交互，再写回。
- **Baseline** · 无任务提示及参数量对照。
- **Benchmark** · 多任务场景理解。
- **关键结果 / 消融** · 消融表明主要收益来自提示而非容量。
- **适用条件 / 局限** · 摘要未给任务明显冲突时边界。

**可复用机制** · 把任务关系写为可训练接口，有利于逐层测试共享和隔离。

<a id="paper-139809"></a>

## VisGym: Diverse, Customizable, Scalable Environments for Multimodal Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/139809) · [作者来源](https://openreview.net/forum?id=3F3t3dn3iI)

- **问题 / 瓶颈** · 最终成功率结合了多种交互设计。
- **核心创新 / 方法** · 提供可调的环境变量并做受控对照。
- **Baseline** · 不同前沿视觉语言模型。
- **Benchmark** · 多类交互式视觉环境。
- **关键结果 / 消融** · 摘要报告前沿模型仍面临挑战并支持控制变量诊断。
- **适用条件 / 局限** · 环境随机性与真实部署覆盖不同。

**可复用机制** · 测试视觉代理时用环境干预隔离感知、计划和反馈依赖。

<a id="paper-148995"></a>

## VisInteract: Towards Dynamic Interactive Text-to-Visualization under Imperfect Queries

[官方论文页](https://neurips.cc/virtual/2026/poster/148995) · [作者来源](https://openreview.net/forum?id=taklyDq3WJ)

- **问题 / 瓶颈** · 用户意图未必能从单轮文本恢复。
- **核心创新 / 方法** · 受控注入缺损，经无泄漏模拟用户补全，再按代码和图双验收。
- **Baseline** · 互动和非互动文本转图。
- **Benchmark** · VisInteract-Bench，端到端成功。
- **关键结果 / 消融** · 比最强互动基线提升 13.40% 至 16.27%。
- **适用条件 / 局限** · 模拟用户不一定代表实际沟通。

**可复用机制** · 多轮澄清系统应验证恢复的意图和最终制品，而非只测回答形式。

<a id="paper-152069"></a>

## Vision Correlators: Correlation-Driven Visual Understanding with Hypergraphs

[官方论文页](https://neurips.cc/virtual/2026/poster/152069) · [作者来源](https://openreview.net/forum?id=Vi8z1QsK4V)

- **问题 / 瓶颈** · 成对消息不能精确表达一些非线性群体关系。
- **核心创新 / 方法** · 用超图实现高阶视觉相关性。
- **Baseline** · Vision Transformer。
- **Benchmark** · ImageNet，参数、FLOPs 和准确率。
- **关键结果 / 消融** · 摘要报告最高少 76% 参数、93% FLOPs 且准确率提升 5.1%。
- **适用条件 / 局限** · 最高值未必同一设置，摘要未给所有任务。

**可复用机制** · 实体关系呈组合性时，应比较显式高阶边与单纯扩大成对连接。

<a id="paper-148251"></a>

## VisionCreator-R1: A Reflection-Enhanced Native Visual-Generation Agentic Model

[官方论文页](https://neurips.cc/virtual/2026/poster/148251) · [作者来源](https://openreview.net/forum?id=zGiLxdshrQ)

- **问题 / 瓶颈** · 行动计划信号清楚而反思信用分配更嘈杂。
- **核心创新 / 方法** · 通过先分后合分别优化两种能力。
- **Baseline** · 已有视觉代理及 Gemini2.5Pro。
- **Benchmark** · 单图和多图 VCR-Bench。
- **关键结果 / 消融** · 摘要报告整体优于所列模型。
- **适用条件 / 局限** · 摘要未给反思行为独立泛化结果。

**可复用机制** · 具有不同可验证性的能力可先用各自合适的监督，再测合并是否互相增益。

<a id="paper-155938"></a>

## Vision-Language Grounding as Bidirectional Concept Correspondence

[官方论文页](https://neurips.cc/virtual/2026/poster/155938) · [作者来源](https://openreview.net/forum?id=1fodx1B629)

- **问题 / 瓶颈** · 只看区域分割难区分未出现概念与位置错配
- **核心创新 / 方法** · 共同预测文本和图像掩码及有无对应
- **Baseline** · 常规定位和分割方法
- **Benchmark** · 长描述、零样本 LVIS；对应 F1
- **关键结果 / 消融** · 摘要报分别提升 59% 和 73%
- **适用条件 / 局限** · 统一任务格式对原数据标注的重解释需核对

**可复用机制** · 指代搜索在无匹配时可弃权并指出误解词组

<a id="paper-151295"></a>

## Vision-OPD: Learning to See Fine Details for Multimodal LLMs via On-Policy Self-Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/151295) · [作者来源](https://openreview.net/forum?id=bUVKljerUo)

- **问题 / 瓶颈** · 小图学生难观测文字纹理或小对象
- **核心创新 / 方法** · 在线自蒸馏让教师用视觉放大引导学生
- **Baseline** · 大模型和运行时看图工具智能体
- **Benchmark** · 多个细节视觉理解基准
- **关键结果 / 消融** · 与更大模型具有竞争力或更好，数值未报告
- **适用条件 / 局限** · 源输入过低分时蒸馏无法创造缺失像素

**可复用机制** · 给感知训练用额外观察并保持部署规格不变

<a id="paper-139833"></a>

## VistaQA: Benchmarking Joint Visual Question Answering and Pixel-Level Evidence

[官方论文页](https://neurips.cc/virtual/2026/poster/139833) · [作者来源](https://openreview.net/forum?id=26ADcnvSjf)

- **问题 / 瓶颈** · 总体准确无法判定模型是否看对区域
- **核心创新 / 方法** · 用几何均值同题评估回答与像素证据
- **Baseline** · 支持定位的模型及通用多模态流水线
- **Benchmark** · VistaQA；GROVE 联合指标
- **关键结果 / 消融** · 最强系统仍难兼顾两项，摘要未列数字
- **适用条件 / 局限** · 人工区域标注可能只覆盖一种充分证据

**可复用机制** · 设答案正确但证据错误的回归用例

<a id="paper-148918"></a>

## VISTA: Support-Anchored Value Targeting for Fast Flow-Based Vision-Language-Action Policies

[官方论文页](https://neurips.cc/virtual/2026/poster/148918) · [作者来源](https://openreview.net/forum?id=uDcXjAL4nU)

- **问题 / 瓶颈** · 无约束值优化可能去到未见状态动作
- **核心创新 / 方法** · 以行为支持锚定价值目标，从多步流教师学快策略
- **Baseline** · BC、优势条件 BC、IDQL、流 Q 学习及 20 步教师
- **Benchmark** · 五 BEHAVIOR-1K 模拟和五双臂实机任务
- **关键结果 / 消融** · 动作专家少 15 倍计算，整策略快 1.8 倍，平均成功率最高
- **适用条件 / 局限** · 保证及部署表现依赖价值估计和支持覆盖

**可复用机制** · 同时调值提升与示范锚定，观察危险的分布外动作

<a id="paper-150518"></a>

## Visual Instruction Tuning Aligns Modalities through Abstraction

[官方论文页](https://neurips.cc/virtual/2026/poster/150518) · [作者来源](https://openreview.net/forum?id=hWOJLeN1yx)

- **问题 / 瓶颈** · 全量更新耗时且视觉对齐未必全层发生
- **核心创新 / 方法** · 定位模态抽象对齐层，再限制微调到中间
- **Baseline** · 全量微调
- **Benchmark** · 视觉中心基准与训练耗时
- **关键结果 / 消融** · 性能接近完整微调且训练更快，幅度未报告
- **适用条件 / 局限** · 层位依赖骨干和训练配方

**可复用机制** · 用早中晚层同参数预算对照定位有效更新区域

<a id="paper-148225"></a>

## Visual-Redundancy-Controlled Parallel Decoding for Diffusion-Based Multimodal Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148225) · [作者来源](https://openreview.net/forum?id=zRTN5g11Av)

- **问题 / 瓶颈** · 按置信逐一选会重复注意同一图像证据
- **核心创新 / 方法** · 以 token 对图注意关系选择互补位置
- **Baseline** · 置信驱动解码
- **Benchmark** · M³CoT、MMBench 等任务；冗余、熵和准确率
- **关键结果 / 消融** · 较长解码分别高 18.8% 和 6.9%
- **适用条件 / 局限** · 位置注意代理需验证且有额外运行开销

**可复用机制** · 等采样次数下比较覆盖感知证据与选最高置信点

<a id="paper-139189"></a>

## Visual Robustness and Neural Alignment in a Shared Foraging Task: The Mouse vs. AI Benchmark

[官方论文页](https://neurips.cc/virtual/2026/poster/139189) · [作者来源](https://openreview.net/forum?id=fhaa8MaD9I)

- **问题 / 瓶颈** · 任务成功不显示退化适应。
- **核心创新 / 方法** · 同环境对照动物与 AI，并读神经预测。
- **Baseline** · 共享任务中的鼠与模型。
- **Benchmark** · Unity 搜寻及约 178 分钟多模态记录。
- **关键结果 / 消融** · 动物在退化输入下保持较稳。
- **适用条件 / 局限** · 脑对齐不等于控制鲁棒。

**可复用机制** · 分别测行为适应与表征.

<a id="paper-139562"></a>

## VisualWorldBench: A Fine-Grained Multi-Task Benchmark for Evaluating Visual World Knowledge in MLLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/139562) · [作者来源](https://openreview.net/forum?id=IQSAcPvs2W)

- **问题 / 瓶颈** · 单任务成绩不能代表可用世界知识。
- **核心创新 / 方法** · 按层次分类和任务交叉构造基准。
- **Baseline** · 传统视觉问答。
- **Benchmark** · 21K+ 叶类、32K+ 实例、八域。
- **关键结果 / 消融** · 最好均值 80.4%，同模型跨任务可差 40 点。
- **适用条件 / 局限** · 分类树及数据覆盖有限。

**可复用机制** · 按任务接口评知识类型。

<a id="paper-139184"></a>

## ViTeX-Bench: Benchmarking High-Fidelity Video Scene Text Editing

[官方论文页](https://neurips.cc/virtual/2026/poster/139184) · [作者来源](https://openreview.net/forum?id=fyPHDFABOs)

- **问题 / 瓶颈** · 单帧读对仍可能破坏运动。
- **核心创新 / 方法** · 真实视频配精确 mask 及指令，对齐字符和运动评估。
- **Baseline** · 现有文本编辑。
- **Benchmark** · ViTeX 387 视频，13 指标。
- **关键结果 / 消融** · 提供三轴诊断，数值未核。
- **适用条件 / 局限** · 训练配对半自动。

**可复用机制** · 内容编辑回归同时验证输出内容和非目标区。

<a id="paper-155764"></a>

## Viverra: Text-to-Code with Guarantees

[官方论文页](https://neurips.cc/virtual/2026/poster/155764) · [作者来源](https://openreview.net/forum?id=35jwwbZdxS)

- **问题 / 瓶颈** · 自然语言读起来合理不保证符合规格。
- **核心创新 / 方法** · 合成可验证断言并给用户解释。
- **Baseline** · 普通文本到代码。
- **Benchmark** · 18 任务、超 400 人用户研究。
- **关键结果 / 消融** · 断言提高代码理解。
- **适用条件 / 局限** · 断言覆盖度和形式化限制需检查。

**可复用机制** · 将保证写成可执行约束。

<a id="paper-149247"></a>

## VLA-Corrector: Lightweight Detect-and-Correct Inference for Adaptive Action Horizon

[官方论文页](https://neurips.cc/virtual/2026/poster/149247) · [作者来源](https://openreview.net/forum?id=ro5UbANNbJ)

- **问题 / 瓶颈** · 固定块长遇意外仍完整执行。
- **核心创新 / 方法** · 潜视觉监控比较预测实际状态，不改底座。
- **Baseline** · 固定分块 VLA。
- **Benchmark** · 视觉偏差及自适应动作。
- **关键结果 / 消融** · 摘要给轻量纠正，效果未核。
- **适用条件 / 局限** · 异常阈值依环境。

**可复用机制** · 用测量决策何时重规划。

<a id="paper-155119"></a>

## VLA-Pro: Cross-Task Procedural Memory Transfer for Vision-Language-Action Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155119) · [作者来源](https://openreview.net/forum?id=8GvqvSyg1S)

- **问题 / 瓶颈** · 场景和动作变化使端到端泛化弱。
- **核心创新 / 方法** · 训练存任务记忆，推理转到目标。
- **Baseline** · 共享 VLA 底座。
- **Benchmark** · RoboTwin、RLBench、实机。
- **关键结果 / 消融** · 仿真最高相对增 207%。
- **适用条件 / 局限** · 依赖记忆质量与参考可比性。

**可复用机制** · 按动作程序相似而非物体外观选迁移。

<a id="paper-139402"></a>

## VL-DocIR: A Benchmark for Vision-Based Long Document Retrieval

[官方论文页](https://neurips.cc/virtual/2026/poster/139402) · [作者来源](https://openreview.net/forum?id=SxsberZw0W)

- **问题 / 瓶颈** · 单相关页指标夸大复杂检索。
- **核心创新 / 方法** · 比较单多向量、文档评分、拆查询、集成。
- **Baseline** · leading 视觉检索器。
- **Benchmark** · VL-DocIR，nDCGAll@10 和 RecallAll@10。
- **关键结果 / 消融** · 最高 75.6 和 86.2，跨文档更难，文档上下文助同文档多页。
- **适用条件 / 局限** · 检索而非最终引用能力。

**可复用机制** · 按页内、页间和文档间分别选检索策略。

<a id="paper-152219"></a>

## VLM$^3$: Vision Language Models Are Native 3D Learners

[官方论文页](https://neurips.cc/virtual/2026/poster/152219) · [作者来源](https://openreview.net/forum?id=UfbiOahvgq)

- **问题 / 瓶颈** · 不同相机尺度混入坐标描述。
- **核心创新 / 方法** · 统一焦距、文本像素参照并混合训练。
- **Baseline** · 标准 VLM 的三维能力。
- **Benchmark** · 多 3D 任务。
- **关键结果 / 消融** · 摘要称简单设计足够，幅度待核。
- **适用条件 / 局限** · 仍需相机和标注质量。

**可复用机制** · 先修坐标约定和数据环境，再改网络。

<a id="paper-150642"></a>

## VLMs Trace Without Tracking: Diagnosing Failures in Visual Path Following

[官方论文页](https://neurips.cc/virtual/2026/poster/150642) · [作者来源](https://openreview.net/forum?id=gYPnYOVpLT)

- **问题 / 瓶颈** · 模型局部跟线时跳到相近路径。
- **核心创新 / 方法** · 构造受控路线和现实复杂图作为外推。
- **Baseline** · 不同视觉语言模型。
- **Benchmark** · 抽象路线、缠绕电线和地铁图。
- **关键结果 / 消融** · 跳线错误跨设置。
- **适用条件 / 局限** · 强视觉拥挤需要额外变量。

**可复用机制** · 将连续追踪与路线识别分开验。

<a id="paper-155339"></a>

## VLS: A Vision-Language-Shape Model for Open-Vocabulary Partonomic 3D Reconstruction

[官方论文页](https://neurips.cc/virtual/2026/poster/155339) · [作者来源](https://openreview.net/forum?id=6LlHvYynTV)

- **问题 / 瓶颈** · 3D 零件标注难收。
- **核心创新 / 方法** · 共享场和可变形隐式映射，混合不同标注级别的监督。
- **Baseline** · 常规三维重建。
- **Benchmark** · ShapeNetPart、PartNet、Objaverse。
- **关键结果 / 消融** · 摘要报告泛化，具体幅度待核。
- **适用条件 / 局限** · 语言先验可漏稀有部件。

**可复用机制** · 用不同模态可用的监督共同约束同一形状场。

<a id="paper-148647"></a>

## VLSplat: Vision-Language Guided Object-Centric 3D Gaussian Splatting via Scene Graph

[官方论文页](https://neurips.cc/virtual/2026/poster/148647) · [作者来源](https://openreview.net/forum?id=wB1qrn1Paj)

- **问题 / 瓶颈** · 局部点容易丢对象语义及关联。
- **核心创新 / 方法** · 用视觉语言和场景图约束高斯表示。
- **Baseline** · 普通 3DGS。
- **Benchmark** · 室内多场景。
- **关键结果 / 消融** · 语义一致和结构完整性改善。
- **适用条件 / 局限** · 关系预测偏差可能传递。

**可复用机制** · 3D 地图回归纳入对象级关系。

<a id="paper-154969"></a>

## V-LUMEN: Visual Lookup Memory for Embedding Scaling in Vision-Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154969) · [作者来源](https://openreview.net/forum?id=9ZQmXxQVG5)

- **问题 / 瓶颈** · 裸视觉缓存不随任务召回。
- **核心创新 / 方法** · 空间聚合成键，文本条件哈希检索。
- **Baseline** · Qwen3-VL-2B、等参 MoE/LoRA。
- **Benchmark** · 多个强推理的多模态基准。
- **关键结果 / 消融** · 冻结主干收益且匹配或超等参比较。
- **适用条件 / 局限** · 索引和额外内存需计入预算。

**可复用机制** · 外部记忆键同时保空间结构和任务相关性。

<a id="paper-139190"></a>

## VocalGrad: Evaluating Acoustic Perception in Audio Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139190) · [作者来源](https://openreview.net/forum?id=fagktzeTe2)

- **问题 / 瓶颈** · 语义题会掩盖低层听觉弱点。
- **核心创新 / 方法** · 二分类时间变化，并比较内部 probe 和输出。
- **Baseline** · 人类与主流音频语言模型。
- **Benchmark** · VocalGrad。
- **关键结果 / 消融** · 模型近机会水平，部分信号已编码但未被读出。
- **适用条件 / 局限** · 受声学刺激和接口影响。

**可复用机制** · 感知修复前确定编码还是读出问题。

<a id="paper-154938"></a>

## Voice "Cloning" Is Actually Style Transfer

[官方论文页](https://neurips.cc/virtual/2026/poster/154938) · [作者来源](https://openreview.net/forum?id=9oCb1fNV0g)

- **问题 / 瓶颈** · 同一说话人听感可能因生成而系统变化。
- **核心创新 / 方法** · 对源声音和克隆声音做人评。
- **Baseline** · 真实源声音。
- **Benchmark** · 权威、温暖、人性和信任等人评。
- **关键结果 / 消融** · 克隆语音被感知更权威温暖。
- **适用条件 / 局限** · 人评限所测情况。

**可复用机制** · 身份相似不能替代风格和信任的独立验证。

<a id="paper-155322"></a>

## Volatility-Whitened Probabilistic Residual Modeling for Long-Term Time Series Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/155322) · [作者来源](https://openreview.net/forum?id=6UKbpYP6hi)

- **问题 / 瓶颈** · 高波动维度主导原始尺度损失。
- **核心创新 / 方法** · 在分尺度残差空间建模再恢复原尺度。
- **Baseline** · 直接扩散未来变量。
- **Benchmark** · 八个真实时序集。
- **关键结果 / 消融** · 摘要报告长程预测改善。
- **适用条件 / 局限** · 依赖波动估计。

**可复用机制** · 把预测基线和条件波动分开可减轻异方差训练失衡。

<a id="paper-152277"></a>

## VolCo: Volumetric Contact for High-Fidelity Human Grasp Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/152277) · [作者来源](https://openreview.net/forum?id=UHbULsTmRA)

- **问题 / 瓶颈** · 表面接触不足以抑制穿透。
- **核心创新 / 方法** · 将接触编码成分层体素并扩散。
- **Baseline** · 现有手部抓取生成。
- **Benchmark** · 抓取穿透与稳定性。
- **关键结果 / 消融** · 摘要报告改善。
- **适用条件 / 局限** · 限手物几何。

**可复用机制** · 接触敏感生成应给局部物理关系独立表示。

<a id="paper-155942"></a>

## VoluCore: Spanning Teacher Representations with Volumetric Coresets for Data-Efficient LLM Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/155942) · [作者来源](https://openreview.net/forum?id=1ebC6IYOPL)

- **问题 / 瓶颈** · 单点质量可能导致重复覆盖。
- **核心创新 / 方法** · 最大化归一化特征 Gram 正则对数行列式。
- **Baseline** · 其他蒸馏数据选择。
- **Benchmark** · 紧凑蒸馏集。
- **关键结果 / 消融** · 目标在固定正则下为单调次模。
- **适用条件 / 局限** · 依赖教师特征。

**可复用机制** · 预算固定且需要多样信息时，按边际几何覆盖选样本。

<a id="paper-150973"></a>

## Vortex: Efficient and Programmable Sparse Attention Serving

[官方论文页](https://neurips.cc/virtual/2026/poster/150973) · [作者来源](https://openreview.net/forum?id=dsBz9htCtC)

- **问题 / 瓶颈** · 稀疏模式不易低成本接入。
- **核心创新 / 方法** · 以可编程前端和服务集成后端构造候选。
- **Baseline** · 全注意力。
- **Benchmark** · 吞吐与准确率。
- **关键结果 / 消融** · 最高 3.46 倍吞吐。
- **适用条件 / 局限** · 依赖服务栈。

**可复用机制** · 用实际部署吞吐验收稀疏算法，避免只比较计算量。

<a id="paper-148747"></a>

## Voxel as Token: A New Perspective for Zero-shot Cross-subject Vision Decoding

[官方论文页](https://neurips.cc/virtual/2026/poster/148747) · [作者来源](https://openreview.net/forum?id=vM4PorBFxC)

- **问题 / 瓶颈** · 过度池化会丢失可泛化激活关系。
- **核心创新 / 方法** · 用体素作为带学习表示的 token。
- **Baseline** · 既有视觉神经解码。
- **Benchmark** · 跨主体零样本视觉解码与 ROI 消融。
- **关键结果 / 消融** · 表现与 ROI 大小强相关。
- **适用条件 / 局限** · 限 fMRI 与所测区域。

**可复用机制** · 逐观测点建模时测试跨域收益来自局部信息还是较广联合模式。

<a id="paper-154454"></a>

## VSPO: Vector-Steered Policy Optimization for Controllable Model Behavior

[官方论文页](https://neurips.cc/virtual/2026/poster/154454) · [作者来源](https://openreview.net/forum?id=DSKSg1Kz1q)

- **问题 / 瓶颈** · 单奖励权重难同时维持多目标。
- **核心创新 / 方法** · 在 GRPO 中改变向量引导强度。
- **Baseline** · 奖励塑形、教师蒸馏和引导。
- **Benchmark** · 行为控制与任务准确率。
- **关键结果 / 消融** · 摘要报告两者均可保留或改善。
- **适用条件 / 局限** · 依赖可靠引导方向。

**可复用机制** · 控制学习可主动覆盖多个行为强度，而不只追求单个最优。

<a id="paper-152736"></a>

## VTV-FM: Flow Matching through Variational Terminal-Velocity Closure

[官方论文页](https://neurips.cc/virtual/2026/poster/152736) · [作者来源](https://openreview.net/forum?id=QkeTySGSs0)

- **问题 / 瓶颈** · 静态样本没有速度监督。
- **核心创新 / 方法** · 以变分闭合定义二阶桥。
- **Baseline** · 一阶和高阶流匹配。
- **Benchmark** · PDE 场与 CIFAR-10。
- **关键结果 / 消融** · 摘要报告几何与生成改善。
- **适用条件 / 局限** · 依赖闭合近似。

**可复用机制** · 需要曲线运动时可给路径增加速度状态，并验证边界估计。

<a id="paper-157020"></a>

## WAREX: Web Agent Reliability Evaluation on Existing Benchmarks

[官方论文页](https://neurips.cc/virtual/2026/poster/157020) · [作者来源](https://openreview.net/forum?id=o4pXVP8RCD)

- **问题 / 瓶颈** · 干净任务得分掩盖部署故障。
- **核心创新 / 方法** · 用带故障的既有环境比较恢复并训练。
- **Baseline** · 普通网页代理。
- **Benchmark** · 网页操作错误恢复。
- **关键结果 / 消融** · 摘要报告恢复率相对改善 88.9%。
- **适用条件 / 局限** · 限所测环境。

**可复用机制** · 验收代理时将恢复成功与正常任务成功分别报告。

<a id="paper-154228"></a>

## WASD: Wasserstein-based Knowledge Distillation for Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154228) · [作者来源](https://openreview.net/forum?id=FGlwR3s9v3)

- **问题 / 瓶颈** · 按索引差异不区分近义错位与无关预测。
- **核心创新 / 方法** · 用 Wasserstein 代价比较词表分布。
- **Baseline** · 逐词概率散度。
- **Benchmark** · 推理和代码等生成。
- **关键结果 / 消融** · 摘要指出语义信息有益。
- **适用条件 / 局限** · 依赖可靠的距离与求解成本。

**可复用机制** · 当多个词元可表达同义答案时，蒸馏可用软匹配传递教师偏好。

<a id="paper-140108"></a>

## Wasserstein Gradient Flows and Forward-Only Diffusion Are Not Enough for Multimodal Sampling

[官方论文页](https://neurips.cc/virtual/2026/poster/140108) · [作者来源](https://openreview.net/forum?id=7sdrh3QFdg)

- **问题 / 瓶颈** · 局部梯度流在模式间质量传输很慢
- **核心创新 / 方法** · 分析 Wasserstein 梯度流与前向扩散的混合时间
- **Baseline** · 标准局部采样以及同一族内变体
- **Benchmark** · 理论多模态分布，摘要未列实证名
- **关键结果 / 消融** · 部分多模态设置需不可接受长时间
- **适用条件 / 局限** · 结论针对论文覆盖的局部动态，未覆盖全部扩散方法

**可复用机制** · 对不连通解族记录模式访问频率并测非局部更新

<a id="paper-152190"></a>

## Watching Itself Watch: Self-Auditing Visual Reliance for Video Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/152190) · [作者来源](https://openreview.net/forum?id=UstDw3BBZv)

- **问题 / 瓶颈** · 训练可能用语言桥接而忽略视频
- **核心创新 / 方法** · 构建自身视觉依赖审计，按差距门控监督并增视觉对比
- **Baseline** · 原模型及现有视频推理方法
- **Benchmark** · 12 基准，含时间、空间、知识及长视频
- **关键结果 / 消融** · 摘要报告均有收益并减少逾九倍训练步
- **适用条件 / 局限** · 步数非全量成本，视觉替换需保持对照公平

**可复用机制** · 为视觉数据先定位语言捷径位置再加强监督

<a id="paper-150773"></a>

## Wavelet Flow Matching for Multi-Scale Physics Emulation

[官方论文页](https://neurips.cc/virtual/2026/poster/150773) · [作者来源](https://openreview.net/forum?id=fU3MXzvqwZ)

- **问题 / 瓶颈** · 单像素监督可能低估多尺度纹理漂移
- **核心创新 / 方法** · 固定小波表示后联合预测运输速度
- **Baseline** · 强混沌流模拟模型
- **Benchmark** · 三个混沌流系统；长期稳定、精度及频谱
- **关键结果 / 消融** · 三项改善，未报告幅度
- **适用条件 / 局限** · 适用范围主要为流体，边界效应需检查

**可复用机制** · 世界模型检查跨尺度能量是否随长程预测不合理衰退

<a id="paper-152557"></a>

## WaveletLoRA: Frequency-Aware Content-Style Decomposition for Personalized Image Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/152557) · [作者来源](https://openreview.net/forum?id=SEc7mCUDGI)

- **问题 / 瓶颈** · 只看属性相似会忽略一个通道污染另一个
- **核心创新 / 方法** · 以频率感知低秩适配区分内容和风格，并校验分离
- **Baseline** · 既有个性化生成方法
- **Benchmark** · 属性保真、分离和人偏好
- **关键结果 / 消融** · 摘要报告两类属性指标与人偏好改善
- **适用条件 / 局限** · 语义与频率映射未必适合所有概念

**可复用机制** · 控制输入按内容风格交叉配对，不用单一相似分

<a id="paper-148786"></a>

## Wayfinder: Adaptive Resource Routing from Agent Citations

[官方论文页](https://neurips.cc/virtual/2026/poster/148786) · [作者来源](https://openreview.net/forum?id=v4g06KBw8G)

- **问题 / 瓶颈** · 不同黑盒资源覆盖不同子查询。
- **核心创新 / 方法** · 从交互训练动态资源选择策略。
- **Baseline** · 监督和零样本路由。
- **Benchmark** · NFCorpus、FEVER 分区和 Tech Startup 异构语料。
- **关键结果 / 消融** · 摘要提供受控比较，量未核。
- **适用条件 / 局限** · 引用正确不一定覆盖用户问题。

**可复用机制** · 路由训练有机制地利用证据出处。

<a id="paper-154891"></a>

## WebNavigator: Global Web Navigation via Interaction Graph Retrieval

[官方论文页](https://neurips.cc/virtual/2026/poster/154891) · [作者来源](https://openreview.net/forum?id=A958ZPHMku)

- **问题 / 瓶颈** · 模型无全局拓扑导致盲走。
- **核心创新 / 方法** · 检索已有路径并用确定规划。
- **Baseline** · 逐步概率探索。
- **Benchmark** · 网页界面导航。
- **关键结果 / 消融** · 摘要指出结构信息是瓶颈，量未核。
- **适用条件 / 局限** · 页面更新使缓存图过时。

**可复用机制** · 工作内工具先用结构路径，失败再依受限观察探索。

<a id="paper-150203"></a>

## Weighted Conformal Clustering

[官方论文页](https://neurips.cc/virtual/2026/poster/150203) · [作者来源](https://openreview.net/forum?id=jxX0Xpi5Wc)

- **问题 / 瓶颈** · 普通共形在隐簇标签上无法直接适用。
- **核心创新 / 方法** · 按条件标签漂移设置共形权重。
- **Baseline** · 随机 split 共形。
- **Benchmark** · 非线性与高维聚类。
- **关键结果 / 消融** · 给权重误差引起覆盖下界，实验改善。
- **适用条件 / 局限** · 依赖可估权重。

**可复用机制** · 聚类输出带集合覆盖并报告标签估计误差。

<a id="paper-154050"></a>

## Weird Generalization from Narrow Finetuning: Persona Shifts and Inductive Backdoors

[官方论文页](https://neurips.cc/virtual/2026/poster/154050) · [作者来源](https://openreview.net/forum?id=GaxSVzlXpM)

- **问题 / 瓶颈** · 良性局部数据也可改变未见行为。
- **核心创新 / 方法** · 比较原模型及新模型的域内外行为测试。
- **Baseline** · 原未微调模型。
- **Benchmark** · 狭任务训练与域外角色及对齐。
- **关键结果 / 消融** · 观察到宽域意外变化。
- **适用条件 / 局限** · 不能凭窄任务数据估影响范围。

**可复用机制** · 微调验收覆盖从未训练的无关任务。

<a id="paper-152026"></a>

## Weisfeiler and Leman Follow the Arrow of Time: Expressive Power of Message Passing in Temporal Event Graphs

[官方论文页](https://neurips.cc/virtual/2026/poster/152026) · [作者来源](https://openreview.net/forum?id=W5jWeq8Ty5)

- **问题 / 瓶颈** · 节点聚合可能混入不合时序的连接。
- **核心创新 / 方法** · 在时间展开事件图做消息传递。
- **Baseline** · 常规 TGNN。
- **Benchmark** · 动态事件图分类。
- **关键结果 / 消融** · 给理论表达性及实验验证，幅度未核。
- **适用条件 / 局限** · 展开图成本随历史增长。

**可复用机制** · 信息边带时间约束，防未来泄漏和无效路径。

<a id="paper-150655"></a>

## Weisfeiler-Leman Is Incomplete on Simple Spectrum Graphs, so Canonicalize Them

[官方论文页](https://neurips.cc/virtual/2026/poster/150655) · [作者来源](https://openreview.net/forum?id=gQCHWXz2Fu)

- **问题 / 瓶颈** · 简单谱并不使固定 k-WL 完备。
- **核心创新 / 方法** · 用 PRiSM 规范化简谱特征分解。
- **Baseline** · k-WL。
- **Benchmark** · 简谱非同构图。
- **关键结果 / 消融** · 证明各 k 存在失效，PRiSM 完备。
- **适用条件 / 局限** · 简谱约束，不能外推任意图。

**可复用机制** · 图对齐方法在保证适用域之外加失败回归。

<a id="paper-138896"></a>

## Welfare, Improvability, and Variance: A Principal-Agent Approach to Optimal Benchmark Item Aggregation

[官方论文页](https://neurips.cc/virtual/2026/poster/138896) · [作者来源](https://openreview.net/forum?id=yF6rmSx7l7)

- **问题 / 瓶颈** · 平均分激励改善错误任务。
- **核心创新 / 方法** · 把分数设计写成多任务委托博弈。
- **Baseline** · 统一聚合。
- **Benchmark** · 理论基准福利分析。
- **关键结果 / 消融** · 三类原语共同决定损失。
- **适用条件 / 局限** · 福利优先级需独立设定。

**可复用机制** · 评估代理是否鼓励解决真正高价值瓶颈。

<a id="paper-155041"></a>

## What are Key Factors for Updates in RL for LLM Reasoning?

[官方论文页](https://neurips.cc/virtual/2026/poster/155041) · [作者来源](https://openreview.net/forum?id=8sh5hzkCxK)

- **问题 / 瓶颈** · 离策略程度改变比率分布和优势来源。
- **核心创新 / 方法** · 以经验重要性比方差估每组剪切边界。
- **Baseline** · DAPO、CISPO。
- **Benchmark** · 3B、7B，数学、表格问答、逻辑。
- **关键结果 / 消融** · 超过强基线，幅度未核。
- **适用条件 / 局限** · 组方差和细粒标签稳定性需测。

**可复用机制** · 同步调更新轮数和剪切阈值。

<a id="paper-148855"></a>

## What Arranges Features in Activation Space?  Non-Classical Predictive Geometry in Next-Token Predictors

[官方论文页](https://neurips.cc/virtual/2026/poster/148855) · [作者来源](https://openreview.net/forum?id=ufZDbHJ06x)

- **问题 / 瓶颈** · 仅列可解码概念不解释组织。
- **核心创新 / 方法** · 从不同生成过程分析预测者状态。
- **Baseline** · 不同数据生成或状态表示。
- **Benchmark** · 条件预测几何研究。
- **关键结果 / 消融** · 特征依数据、组织几何依生成器。
- **适用条件 / 局限** · 受可控潜过程分析限制。

**可复用机制** · 用等预测任务不同隐结构检验探针反映什么。

<a id="paper-155411"></a>

## What Can Labels Alone Audit and Edit in Frozen Representations?

[官方论文页](https://neurips.cc/virtual/2026/poster/155411) · [作者来源](https://openreview.net/forum?id=5rXQteakrg)

- **问题 / 瓶颈** · 标签不能唯一决定语义和背景分解。
- **核心创新 / 方法** · 拟合低维代理，保留其空间后再修改残余。
- **Baseline** · 未分离的整体编辑。
- **Benchmark** · 冻结表示的标签审计。
- **关键结果 / 消融** · 摘要支持在残差覆盖和划分稳定时采用。
- **适用条件 / 局限** · 标签不足以验证潜语义。

**可复用机制** · 做冻结编辑应先保护标签所需信息，再持出验证删改方向。

<a id="paper-150992"></a>

## What Claims Do LLM Benchmark Scores Support?

[官方论文页](https://neurips.cc/virtual/2026/poster/150992) · [作者来源](https://openreview.net/forum?id=dkKZh50w7W)

- **问题 / 瓶颈** · 从分数推到更强结论可能超出测量范围。
- **核心创新 / 方法** · 固定单位并检验声明所需的变化与不变量。
- **Baseline** · 原始基准单分数。
- **Benchmark** · 五个开源模型。
- **关键结果 / 消融** · 示范输出直接支持边界和下一步测量。
- **适用条件 / 局限** · 依赖声明集及对照可查性。

**可复用机制** · 在模型选型时将分数用于经过控制验证的具体能力。

<a id="paper-154524"></a>

## What Cohort INRs Encode, and Where to Freeze Them

[官方论文页](https://neurips.cc/virtual/2026/poster/154524) · [作者来源](https://openreview.net/forum?id=Cwk1nNVMQY)

- **问题 / 瓶颈** · 默认全量微调不是所有层都必要。
- **核心创新 / 方法** · 对比逐层冻结的表现与层稳定秩。
- **Baseline** · 标准微调。
- **Benchmark** · 多项隐式表示迁移。
- **关键结果 / 消融** · 最高稳定秩层与最佳冻结点吻合。
- **适用条件 / 局限** · 限所测 INR，不保证跨架构。

**可复用机制** · 对逐层迁移先用谱指标作筛选，再用少量任务确认。

<a id="paper-151749"></a>

## What Do Audio Models Really Hear? Layer Selection and Mechanistic Structure in Sound Representations

[官方论文页](https://neurips.cc/virtual/2026/poster/151749) · [作者来源](https://openreview.net/forum?id=YNzJ1MzFGS)

- **问题 / 瓶颈** · 仅比较全模型结果可能错过早层信息。
- **核心创新 / 方法** · 同一层任务上结合探针、消融和稳健性评估。
- **Baseline** · 全层与不同截断。
- **Benchmark** · 多种音频表示任务。
- **关键结果 / 消融** · 摘要提出分层审查机制。
- **适用条件 / 局限** · 具体层和指标随任务而变。

**可复用机制** · 选浅层读出要同时验证准确、稳定以及因果依赖。

<a id="paper-150770"></a>

## What do EEG Foundation Models Capture from Human Brain Signals?

[官方论文页](https://neurips.cc/virtual/2026/poster/150770) · [作者来源](https://openreview.net/forum?id=fUj6SZpI7V)

- **问题 / 瓶颈** · 线性可读出不能证明决策依赖。
- **核心创新 / 方法** · 对比岭探针、子空间消除及透明概念分类。
- **Baseline** · 随机特征和透明分类器。
- **Benchmark** · 不同 EEG 下游任务。
- **关键结果 / 消融** · 容易任务近乎由已有概念解释，难例有残余。
- **适用条件 / 局限** · 受概念词典覆盖限制。

**可复用机制** · 表示解释用探针提出候选，再用干预区分读到和使用。

<a id="paper-150120"></a>

## What Does an Observability Forecasting Foundation Model Know?

[官方论文页](https://neurips.cc/virtual/2026/poster/150120) · [作者来源](https://openreview.net/forum?id=kWi9pOSFy1)

- **问题 / 瓶颈** · 线性可读性和干预效果容易混淆。
- **核心创新 / 方法** · 在同样原始窗口上加入谱控制，并测层局部和干预。
- **Baseline** · 监督 FNO 及原始输入表征。
- **Benchmark** · TOTO 在 BOOM 上的遥测结构。
- **关键结果 / 消融** · 频率、指标和域可线性解码，但部分边界概念难以引导。
- **适用条件 / 局限** · 仅所测模型和任务。

**可复用机制** · 决定使用内部属性作为控制信号前，先检验具体操作对结果的影响。

<a id="paper-149772"></a>

## What Does a Sparse Autoencoder Feature Do? A Weight-Based Account

[官方论文页](https://neurips.cc/virtual/2026/poster/149772) · [作者来源](https://openreview.net/forum?id=nQXn6YRf2P)

- **问题 / 瓶颈** · 活动相关性不足以说明输出机制。
- **核心创新 / 方法** · 在不需激活数据的权重框架中识别输入或输出特征并检验。
- **Baseline** · 基于活动的解释。
- **Benchmark** · Gemma-2 与 Llama-3.1。
- **关键结果 / 消融** · 报告深度与角色的不同规律。
- **适用条件 / 局限** · 受具体字典和模型约束。

**可复用机制** · 判断稀疏特征作用时，保留写入和读出两条证据。

<a id="paper-149806"></a>

## What Drives Compositional Generalization? The Importance of Continuous Training Objectives in Visual Generative Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149806) · [作者来源](https://openreview.net/forum?id=nDJI3hkYsq)

- **问题 / 瓶颈** · 只测表示能力可能错过训练目标的影响。
- **核心创新 / 方法** · 跨任务干预损失连续性与条件覆盖。
- **Baseline** · 离散目标及辅助松弛。
- **Benchmark** · 多个组合生成，另含初步世界模型和语言模型。
- **关键结果 / 消融** · 摘要报告连续目标或辅助松弛有益。
- **适用条件 / 局限** · 条件信息也改变结果，其他模型证据初步。

**可复用机制** · 组合泛化变差时依次测试目标连续性和训练条件是否暴露了因素。

<a id="paper-149540"></a>

## What Fits (Into Few Tokens) Doesn't Overfit:  Compression and Generalization in ML Research Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/149540) · [作者来源](https://openreview.net/forum?id=pN8yAngM9e)

- **问题 / 瓶颈** · 同代理保留全部搜索上下文可能依赖验证集细节。
- **核心创新 / 方法** · 将参与搜索的策略压缩成短提示，再交给新代理。
- **Baseline** · 完整历史或不同压缩条件。
- **Benchmark** · 机器学习研究代理搜索。
- **关键结果 / 消融** · 摘要报告成功策略处于低复杂度区域。
- **适用条件 / 局限** · 压缩是验证手段，不保证无过拟合。

**可复用机制** · 审计自动研究时测试独立复现能否从简洁原则恢复结果。

<a id="paper-139717"></a>

## What Gets Measured Gets Managed: Sign-aware Recommendation Needs Sign-aware Evaluation

[官方论文页](https://neurips.cc/virtual/2026/poster/139717) · [作者来源](https://openreview.net/forum?id=8heSqfIF6F)

- **问题 / 瓶颈** · 相关性平均值容易掩盖不喜欢内容。
- **核心创新 / 方法** · 用线性探针与内积排序比较负向信息可读性。
- **Baseline** · 常规 top-K 与内积。
- **Benchmark** · 带正负反馈的推荐。
- **关键结果 / 消融** · 摘要报告表示含情感价但内积未能利用。
- **适用条件 / 局限** · 需有可靠的显式负反馈。

**可复用机制** · 对具有正负偏好的系统，将惩罚目标写进排序和独立验收指标。

<a id="paper-149925"></a>

## What Is Worth Representing? Representational Empowerment for Continual Model Construction

[官方论文页](https://neurips.cc/virtual/2026/poster/149925) · [作者来源](https://openreview.net/forum?id=m9oKQZGDlw)

- **问题 / 瓶颈** · 受资源限制不能保存所有经验。
- **核心创新 / 方法** · 以内部表示赋能评分衡量候选。
- **Baseline** · 控制外部状态的传统赋能。
- **Benchmark** · 持续模型构建。
- **关键结果 / 消融** · 摘要报告对选择与复用有潜力。
- **适用条件 / 局限** · 需要估计未来规划收益。

**可复用机制** · 决定留哪些经验时比较对未来决策的可测增益。

<a id="paper-154141"></a>

## What kills $v$-prediction? A Patch-wise PCA Perspective on Pixel-Space Flow Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/154141) · [作者来源](https://openreview.net/forum?id=FwWaPhPb2O)

- **问题 / 瓶颈** · 让骨干重建原始噪声输入容易淹没语义方向
- **核心创新 / 方法** · 将含原始噪声输入的项直接加到末层
- **Baseline** · 标准 v-prediction、x-prediction
- **Benchmark** · ImageNet 256×256；生成表现
- **关键结果 / 消融** · 改造 v 预测达到与 x 预测有竞争力，摘要未列数字
- **适用条件 / 局限** · 输入几何和预测参数化影响结论

**可复用机制** · 在去噪骨干对照显式旁路与增加容量

<a id="paper-152187"></a>

## What Makes Two States the Same? Value-Aware State Matching for Multi-Turn Agent Credit Assignment

[官方论文页](https://neurips.cc/virtual/2026/poster/152187) · [作者来源](https://openreview.net/forum?id=UutWRcG1RQ)

- **问题 / 瓶颈** · 硬阈值会把大量没有邻居的步骤扔掉
- **核心创新 / 方法** · 用价值感知核平滑替代阈值群组
- **Baseline** · GiGPO、HGPO
- **Benchmark** · ALFWorld、WebShop及多模型规模
- **关键结果 / 消融** · 两个基准改善，消除既有损失 30–36% 步信用的单例问题
- **适用条件 / 局限** · 缓存状态相似度必须反映可用价值

**可复用机制** · 把任务文本相似与状态行为相似分开建信号

<a id="paper-154858"></a>

## What MLLMs Learn about When they Learn about Multimodal Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/154858) · [作者来源](https://openreview.net/forum?id=AMC9hxPW4v)

- **问题 / 瓶颈** · 平均准确率无法看出弱点转向感知、推理或融合
- **核心创新 / 方法** · 对不同模型分解感知、通用推理及多模态特有失败
- **Baseline** · 不同学习阶段和模型质量
- **Benchmark** · 多模态推理错误分解，具体基准未报告
- **关键结果 / 消融** · 随着前两项改善，余错更多属于模态特有
- **适用条件 / 局限** · 诊断依赖类别可区分与标注可靠

**可复用机制** · 新增训练前先查剩余失败由何种能力支配

<a id="paper-153263"></a>

## What Probing Reveals about Autonomous Driving: Better Predictions Lead to Better Planning

[官方论文页](https://neurips.cc/virtual/2026/poster/153263) · [作者来源](https://openreview.net/forum?id=MYtWiWcp1j)

- **问题 / 瓶颈** · 良好总体闭环分可能掩盖临近碰撞预测退化
- **核心创新 / 方法** · 探测中间预测并以纠正预测做安全仿真干预
- **Baseline** · 原预测和纠正预测的策略结果
- **Benchmark** · 模拟近碰撞与闭环规划
- **关键结果 / 消融** · 修正预测能改变轨迹，摘要未给幅度
- **适用条件 / 局限** · 仿真不取代实机机制核验

**可复用机制** · 为控制系统加预警时点和缓解才算成功的回归

<a id="paper-148503"></a>

## What’s Holding Back Latent Visual Reasoning?

[官方论文页](https://neurips.cc/virtual/2026/poster/148503) · [作者来源](https://openreview.net/forum?id=xLMXsTUIOX)

- **问题 / 瓶颈** · 模型可使用正确潜态却在部署预测坍到狭小区域
- **核心创新 / 方法** · 对照 oracle 中间状态和自然解码潜态
- **Baseline** · 普通潜态推理、oracle 潜表示
- **Benchmark** · 视觉推理相关任务，摘要未列名称
- **关键结果 / 消融** · 预测潜态偏离 oracle，限制可利用收益
- **适用条件 / 局限** · oracle 的状态不能用于部署，且对数据构造敏感

**可复用机制** · 改善潜态生成前先用正确中间表示测上限

<a id="paper-149000"></a>

## What Should a Streaming Video Model Remember?

[官方论文页](https://neurips.cc/virtual/2026/poster/149000) · [作者来源](https://openreview.net/forum?id=tZME4ewq9U)

- **问题 / 瓶颈** · 不断增长输入或只用近窗都不理想
- **核心创新 / 方法** · 在线选择保留历史信息，不缓存重播所有帧
- **Baseline** · 近窗和其他流记忆方法
- **Benchmark** · StreamingBench、OVO-Bench 与离线视频
- **关键结果 / 消融** · 82.67%、67.03%，离线均值 74.4%
- **适用条件 / 局限** · 摘要未列硬件时延和极长序列条件

**可复用机制** · 分开测最近细节和跨长时段证据检索

<a id="paper-148165"></a>

## What Stops SGD on LLM Pre-Training: The Need for Large Learning Rate and How to Achieve it

[官方论文页](https://neurips.cc/virtual/2026/poster/148165) · [作者来源](https://openreview.net/forum?id=zorIfxhDUM)

- **问题 / 瓶颈** · 标准 SGD 小步时难追 Adam
- **核心创新 / 方法** · 用裁剪稳定高步长并实测差距
- **Baseline** · Adam 与未稳定 SGD
- **Benchmark** · 1B LLaMA、1M-token 批量；验证损失
- **关键结果 / 消融** · 差距从逾 50% 缩到约 3.5%
- **适用条件 / 局限** · 结果依赖大批、裁剪及具体模型

**可复用机制** · 优化器比较先独立扫保证稳定的最大步长

<a id="paper-154392"></a>

## What Time Is It? How Data Geometry Makes Time Conditioning Optional for Flow Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/154392) · [作者来源](https://openreview.net/forum?id=DvM39mOD5T)

- **问题 / 瓶颈** · 某些数据几何中状态已经包含时间信息
- **核心创新 / 方法** · 比较有无时间条件和不同耦合，对照损失和生成质量
- **Baseline** · 同一模型加或去时间，其他耦合
- **Benchmark** · CIFAR-10、CelebA-HQ、FFHQ
- **关键结果 / 消融** · 改变耦合影响大于移除时间输入
- **适用条件 / 局限** · 时间可辨识依赖数据与耦合，非普遍可去

**可复用机制** · 在统一预算中将耦合和条件作为独立因素消融

<a id="paper-154627"></a>

## What to Forget in Unlearning? Forget Set Curation for Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154627) · [作者来源](https://openreview.net/forum?id=CB3S2eQqCk)

- **问题 / 瓶颈** · 预设待忘样本忽略覆盖和附带损伤。
- **核心创新 / 方法** · 按模型提取表现和请求范围构造遗忘集合，测原文与内容。
- **Baseline** · 固定遗忘集。
- **Benchmark** · CleanSlate 歌曲、书、问答及保留。
- **关键结果 / 消融** · 请求续写几乎全压制，但未请求内容和能力会退化。
- **适用条件 / 局限** · 基准作品覆盖有限。

**可复用机制** · 分别报告需求覆盖、实测抑制和非目标损伤。

<a id="paper-156036"></a>

## What to Predict for Efficient Scheduling on Parallel Machines

[官方论文页](https://neurips.cc/virtual/2026/poster/156036) · [作者来源](https://openreview.net/forum?id=0wSvC9Zj1C)

- **问题 / 瓶颈** · 机器指派预测的小错可全局传播。
- **核心创新 / 方法** · 对照多种解编码的噪声和难度。
- **Baseline** · 直接预测任务分配。
- **Benchmark** · 并行机器调度，带错误预测。
- **关键结果 / 消融** · 顺序编码错误局部化，稳于直接编码。
- **适用条件 / 局限** · 受调度模型限制。

**可复用机制** · 选错误影响可局部化的预测目标。

<a id="paper-149905"></a>

## What to Remember, What to Reveal: Privacy-Aware Memory for Conversational Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/149905) · [作者来源](https://openreview.net/forum?id=mLdUy1WYEJ)

- **问题 / 瓶颈** · 个性化可能无意暴露隐私。
- **核心创新 / 方法** · 用消敏映射分开功能记忆和原值。
- **Baseline** · 普通记忆代理。
- **Benchmark** · 个性化、隐私和推理成本。
- **关键结果 / 消融** · 保个性化且减不必要曝光。
- **适用条件 / 局限** · 消敏标签需复验上下文推断。

**可复用机制** · 记忆读权限与生成输出权限分开控。

<a id="paper-153020"></a>

## What Transformer FFNs Never See: Theory, Diagnosis, and Lightweight Remediation

[官方论文页](https://neurips.cc/virtual/2026/poster/153020) · [作者来源](https://openreview.net/forum?id=Oa1iYsgkvE)

- **问题 / 瓶颈** · 聚合向量可能丢来源身份。
- **核心创新 / 方法** · 每块附四项紧凑路由量。
- **Baseline** · 标准 Transformer 与 oracle。
- **Benchmark** · Routing Reconstruction Task。
- **关键结果 / 消融** · 基线 31.4% 对 oracle 94.6%，补回逾 75% 差距，额外参低于 1.1%。
- **适用条件 / 局限** · 其他任务表征受益需测。

**可复用机制** · 聚合时保存足以追溯来源的旁信号。

<a id="paper-148192"></a>

## What Was That Again? Certified Robustness for Automatic Speech Recognition

[官方论文页](https://neurips.cc/virtual/2026/poster/148192) · [作者来源](https://openreview.net/forum?id=zdRy5kB5qm)

- **问题 / 瓶颈** · 固定样本二项检验成本高。
- **核心创新 / 方法** · 以 E-value martingale 保任意时刻有效。
- **Baseline** · 固定样本认证。
- **Benchmark** · 四 ASR 架构，WER、词和句证书。
- **关键结果 / 消融** · 平均 WER 相对降 25.5%。
- **适用条件 / 局限** · 依赖所用随机化条件。

**可复用机制** · 安全认证分局部和全序列，同时控制在线停止。

<a id="paper-155260"></a>

## When Actions Matter: Causal Affordances for Long-Horizon Credit Assignment in World Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155260) · [作者来源](https://openreview.net/forum?id=71oPZLHKsN)

- **问题 / 瓶颈** · 长时程终局反馈无法定位作用环节。
- **核心创新 / 方法** · 用因果 affordance 表示长程信用。
- **Baseline** · 常规世界模型。
- **Benchmark** · 长时任务。
- **关键结果 / 消融** · 摘要提出 WHAM，具体增益待核。
- **适用条件 / 局限** · 反事实模型误差影响归因。

**可复用机制** · 分开验动作预测与动作的可检验结果。

<a id="paper-152611"></a>

## When Alignment Fails: Stabilizing Cross-Dynamics RL with Prototype Trust Regions

[官方论文页](https://neurips.cc/virtual/2026/poster/152611) · [作者来源](https://openreview.net/forum?id=RpLLznYpDC)

- **问题 / 瓶颈** · 特征对齐可能两边同时坍缩。
- **核心创新 / 方法** · 每域用 EMA 原型设二阶信赖域。
- **Baseline** · 标准跨域对齐。
- **Benchmark** · 不同动力学的 RL 表示和 regret。
- **关键结果 / 消融** · 理论恢复非空覆盖及遗憾保证。
- **适用条件 / 局限** · 要求域内统计可稳定估。

**可复用机制** · 比较对齐之前先检测无用的共同塌缩。

<a id="paper-153226"></a>

## When All Paths Lead to Dead End: Deadlock-Depth-guided Monte Carlo Tree Search for Reentrant Blocking Hybrid Flow Shops

[官方论文页](https://neurips.cc/virtual/2026/poster/153226) · [作者来源](https://openreview.net/forum?id=Mq6HakMjhE)

- **问题 / 瓶颈** · 二元成功无法区分有希望分支。
- **核心创新 / 方法** · 给 MCTS rollout 的死锁深度独立评分。
- **Baseline** · 传统 MCTS。
- **Benchmark** · 可重入阻塞混合流水车间。
- **关键结果 / 消融** · 摘要表明失败深度有排序信息。
- **适用条件 / 局限** · 晚失败不等于最优，需按任务核验。

**可复用机制** · 稀疏成功环境给终止反馈附进度。

<a id="paper-155803"></a>

## When and How Much to Imagine: Adaptive Test-Time Scaling with World Models for Visual Spatial Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/155803) · [作者来源](https://openreview.net/forum?id=2lkBbc7J7q)

- **问题 / 瓶颈** · 统一生成未来耗费预算且可能误导。
- **核心创新 / 方法** · 按证据充足性门控及缩放视觉想象。
- **Baseline** · 全想象或不想象。
- **Benchmark** · 视觉空间推理。
- **关键结果 / 消融** · 研究发现不必要想象有代价，确数待核。
- **适用条件 / 局限** · 世界模型预测非真实观测。

**可复用机制** · 给模拟工具使用独立价值估计。

<a id="paper-151406"></a>

## When and How to Canonize: a Generalization Perspective

[官方论文页](https://neurips.cc/virtual/2026/poster/151406) · [作者来源](https://openreview.net/forum?id=auino4yMsg)

- **问题 / 瓶颈** · 选同一代表的不同规则泛化可差很大。
- **核心创新 / 方法** · 以覆盖数分析良好和劣质 canonization。
- **Baseline** · 非等变模型及其他规则。
- **Benchmark** · 点云置换。
- **关键结果 / 消融** · 规则可达到最优或非等变级误差。
- **适用条件 / 局限** · 取决于群和数据。

**可复用机制** · 规范化不是免费去变异，需验连续性及样本外。

<a id="paper-151346"></a>

## When and What to Prune?  Stage-Aware Visual Token Pruning for Efficient VLA

[官方论文页](https://neurips.cc/virtual/2026/poster/151346) · [作者来源](https://openreview.net/forum?id=bDNYAVS5VS)

- **问题 / 瓶颈** · 全阶段统一删 token 容易漏精控视觉。
- **核心创新 / 方法** · 训练免阶段感知视觉裁剪。
- **Baseline** · 原 VLA 和普通裁剪。
- **Benchmark** · LIBERO、SIMPLER、实机。
- **关键结果 / 消融** · 裁 87.5%，最高 1.718 倍，成功率有竞争力。
- **适用条件 / 局限** · 任务依赖局部线索，实机需压力测试。

**可复用机制** · 按阶段测视觉需求再设计算预算。

<a id="paper-153203"></a>

## When and Why Does Multi-Agent Debate Fail and Does It Really Underperform?

[官方论文页](https://neurips.cc/virtual/2026/poster/153203) · [作者来源](https://openreview.net/forum?id=N4agj1mm4n)

- **问题 / 瓶颈** · 竞争可能鼓励误导，共识选择可能过早删分支。
- **核心创新 / 方法** · 比较协作协议与竞争、共识。
- **Baseline** · CopMAD、CosMAD。
- **Benchmark** · 多代理推理。
- **关键结果 / 消融** · 两标准范式有不同失败模式。
- **适用条件 / 局限** · 协议设计和基础模型会影响现象。

**可复用机制** · 把协作结果及独立意见是否被采纳分开测。

<a id="paper-152200"></a>

## When and Why SignSGD Outperforms SGD: A Theoretical Study Based on $\ell_1$-norm Lower Bounds

[官方论文页](https://neurips.cc/virtual/2026/poster/152200) · [作者来源](https://openreview.net/forum?id=Up1I1hhYE6)

- **问题 / 瓶颈** · 用 L2 判停止可能看不到符号方法目标。
- **核心创新 / 方法** · 以 L1 下界建理论并做 GPT-2 对照。
- **Baseline** · SGD。
- **Benchmark** · 124M GPT-2 预训练。
- **关键结果 / 消融** · 分析预测该设置 SignSGD 收敛更快。
- **适用条件 / 局限** · 不能外推所有噪声与训练规模。

**可复用机制** · 量梯度方向有效性再选择符号优化。

<a id="paper-151059"></a>

## When Are Compositional Problems Learnable from Verifiable Rewards?

[官方论文页](https://neurips.cc/virtual/2026/poster/151059) · [作者来源](https://openreview.net/forum?id=dJ8kBICHqU)

- **问题 / 瓶颈** · 仅奖励最终答案可能收敛到次优组合。
- **核心创新 / 方法** · 以组成优势比例推可学性。
- **Baseline** · 有无先验优势的 RLVR。
- **Benchmark** · 若干结构化组合问题。
- **关键结果 / 消融** · 优势存在才有有效学习条件。
- **适用条件 / 局限** · 需可估子策略与验证奖励。

**可复用机制** · 为完全无优势部件补示范或课程。

<a id="paper-139798"></a>

## When Are Multimodal Predictions Biologically Supported? A Diagnostic Evaluation Framework

[官方论文页](https://neurips.cc/virtual/2026/poster/139798) · [作者来源](https://openreview.net/forum?id=3siPQWjkBS)

- **问题 / 瓶颈** · 有预测性能不能定位支持来源。
- **核心创新 / 方法** · 用五项对照指标将表征划四诊断型。
- **Baseline** · 只看预测准确。
- **Benchmark** · 肿瘤多模态表征评估。
- **关键结果 / 消融** · 框架区分各信号，摘要数值待核。
- **适用条件 / 局限** · 相关不等于因果，需可靠负对照。

**可复用机制** · 新模态应用前用共享与专有信息验收。

<a id="paper-139038"></a>

## When Are Predictions Enough? An Evaluation Protocol for Frozen Expert Composition

[官方论文页](https://neurips.cc/virtual/2026/poster/139038) · [作者来源](https://openreview.net/forum?id=oYmTqDKIF7)

- **问题 / 瓶颈** · 不匹配基线会混淆收益来源。
- **核心创新 / 方法** · 建预测层级、固定特征锚及高容量复核，按轴分组。
- **Baseline** · 预测空间与特征空间融合。
- **Benchmark** · 冻结专家组合。
- **关键结果 / 消融** · 评估结论依设计，幅度待核。
- **适用条件 / 局限** · 底座容量及数据预算要同配。

**可复用机制** · 专家是否互补要用容量匹配的分轴消融。

<a id="paper-155762"></a>

## When Are Semivalue-Based Decisions Identifiable? Robust Data Selection under Utility Ambiguity

[官方论文页](https://neurips.cc/virtual/2026/poster/155762) · [作者来源](https://openreview.net/forum?id=36n5iNZwMk)

- **问题 / 瓶颈** · 效用含糊时固定贡献分数无法保证选集唯一。
- **核心创新 / 方法** · 测试允许的效用变动下数据分组是否不变。
- **Baseline** · 固定效用下的半值分数。
- **Benchmark** · 数据选择的可识别性分析。
- **关键结果 / 消融** · 分组稳健性是保证成功的必要条件。
- **适用条件 / 局限** · 依赖效用范围定义。

**可复用机制** · 对任务价值尚不确定的数据，报告跨效用稳定子集。

<a id="paper-148618"></a>

## When Are Teacher Tokens Reliable? Position-Weighted On-Policy Self-Distillation for Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/148618) · [作者来源](https://openreview.net/forum?id=wPMiko3NFZ)

- **问题 / 瓶颈** · 高熵可以是无效分支，也可是真实解法多样性。
- **核心创新 / 方法** · 比较教师分支选择后的轨迹可行性并对位置加权。
- **Baseline** · 均匀自蒸馏。
- **Benchmark** · 推理蒸馏。
- **关键结果 / 消融** · 报告无需额外教师计算即可改进。
- **适用条件 / 局限** · 摘要未给数字。

**可复用机制** · 用后续解法可行性来决定是否加重当前软标签。

<a id="paper-151419"></a>

## When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction

[官方论文页](https://neurips.cc/virtual/2026/poster/151419) · [作者来源](https://openreview.net/forum?id=apVR4ALp2m)

- **问题 / 瓶颈** · 长互动目标可能从显式访问转为弱残差记忆。
- **核心创新 / 方法** · 组合目标可达比例、滑窗消融和残差探针。
- **Baseline** · 不同上下文窗。
- **Benchmark** · 多轮指令跟随。
- **关键结果 / 消融** · 给出失效的参数预测。
- **适用条件 / 局限** · 注意力比例需因果复核。

**可复用机制** · 诊断丢任务时直接切断访问路径作对照。

<a id="paper-150504"></a>

## When Attention Collapses: Residual Evidence Modeling for Compositional Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/150504) · [作者来源](https://openreview.net/forum?id=hbOb7WNLD6)

- **问题 / 瓶颈** · 多个槽反复解释同一强信号，弱成分丢失。
- **核心创新 / 方法** · 在注意力分配后更新剩余证据。
- **Baseline** · 无残差追踪的注意力。
- **Benchmark** · 加性叠加的多成分推断。
- **关键结果 / 消融** · 摘要报告避免槽塌缩。
- **适用条件 / 局限** · 假定可分离的证据。

**可复用机制** · 多槽推断可将已解释部分从后续槽的竞争中移出。

<a id="paper-154919"></a>

## When Attribution Patching Lies: Diagnosis and a Second-Order Correction

[官方论文页](https://neurips.cc/virtual/2026/poster/154919) · [作者来源](https://openreview.net/forum?id=9z06SMMtXu)

- **问题 / 瓶颈** · 一阶近似会遗漏下游非线性。
- **核心创新 / 方法** · 定位主要误差源，加入二阶校正。
- **Baseline** · 普通梯度归因替换。
- **Benchmark** · 标准电路归因基准。
- **关键结果 / 消融** · 摘要报告改善电路恢复。
- **适用条件 / 局限** · 高阶校正开销未报告。

**可复用机制** · 用便宜近似做筛选，再集中验证高风险结果。

<a id="paper-151914"></a>

## When Confidence Rises Too Early: Detecting Shortcut Reasoning via Premature Answer Commitment

[官方论文页](https://neurips.cc/virtual/2026/poster/151914) · [作者来源](https://openreview.net/forum?id=WxBav9I0Vd)

- **问题 / 瓶颈** · 最终正确会掩盖不忠实推理。
- **核心创新 / 方法** · 测量生成期间的过早承诺并据此识别。
- **Baseline** · 普通监测和验证器。
- **Benchmark** · 捷径推理和奖励偏好。
- **关键结果 / 消融** · F1 比强对照高超过 4.3%。
- **适用条件 / 局限** · 需要访问中间信号。

**可复用机制** · 对过程奖励检查置信的时间变化，不只看结局。

<a id="paper-153537"></a>

## When Copying Is Hard: Copy-Constrained Decoding for Exact Span Reproduction

[官方论文页](https://neurips.cc/virtual/2026/poster/153537) · [作者来源](https://openreview.net/forum?id=KcQ4wC6HLY)

- **问题 / 瓶颈** · 大模型仍会改写要求精确复现的字符。
- **核心创新 / 方法** · CopyGen 在解码阶段建模来源片段约束。
- **Baseline** · 普通语言模型生成。
- **Benchmark** · 合同、科技文献、代码与随机串。
- **关键结果 / 消融** · 摘要报告复制能力有系统缺口。
- **适用条件 / 局限** · 需要可定位正确来源。

**可复用机制** · 把逐字符复现作为硬约束独立执行。

<a id="paper-154779"></a>

## When Debate Helps: Proposal Supply and Verification-Aware Readout in Multi-Agent Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/154779) · [作者来源](https://openreview.net/forum?id=B2PDGRTWWu)

- **问题 / 瓶颈** · 更多争论不保证最终使用正确信息。
- **核心创新 / 方法** · 用可验证证据分析候选如何影响最终结果。
- **Baseline** · 不同专家供给与读出。
- **Benchmark** · 多代理推理。
- **关键结果 / 消融** · 摘要归因于供给与利用两部分。
- **适用条件 / 局限** · 未给普适团队规模。

**可复用机制** · 判定是否扩代理前先测已有候选是否被正确使用。

<a id="paper-139731"></a>

## When Do Cosine Prototypes Mislead? A Whitening-Aware Benchmark for Frozen-Feature Image Classification

[官方论文页](https://neurips.cc/virtual/2026/poster/139731) · [作者来源](https://openreview.net/forum?id=7nyfFNceM0)

- **问题 / 瓶颈** · 余弦可能丢弃低方差判别方向。
- **核心创新 / 方法** · 同一编码器对照各类分类器。
- **Baseline** · 余弦原型与 LDA。
- **Benchmark** · 九项图像分类，含 Aircraft。
- **关键结果 / 消融** · 余弦仅两项领先，DINOv2-B 某任务差距 37.63 点。
- **适用条件 / 局限** · 分类器选择受可用样本量影响。

**可复用机制** · 比较表征前交换读出模型，检查排名是否只是解码归纳偏置。

<a id="paper-151493"></a>

## When Does Fine-Tuning Extract Stored Knowledge? A Relation-Covering Theory for One-Layer Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/151493) · [作者来源](https://openreview.net/forum?id=aFLMTsDeTk)

- **问题 / 瓶颈** · 模型可能已存事实但不会通过问答格式提取。
- **核心创新 / 方法** · 分析训练关系如何触发已学表示。
- **Baseline** · 全量与低秩微调。
- **Benchmark** · 合成及 PopQA 的 GPT-2 和 Llama。
- **关键结果 / 消融** · 摘要支持关系覆盖预测趋势。
- **适用条件 / 局限** · 理论为单层模型。

**可复用机制** · 优先检查微调是否覆盖所需关系，不把未复述事实当成必须再训练。

<a id="paper-139414"></a>

## When Does Graph Retrieval Become Answer-Supporting Evidence? A Diagnostic Audit of GraphRAG

[官方论文页](https://neurips.cc/virtual/2026/poster/139414) · [作者来源](https://openreview.net/forum?id=S9CWPfaHOm)

- **问题 / 瓶颈** · 检索分数提高不保证生成质量。
- **核心创新 / 方法** · 对候选、排序、上下文、答案和代价逐段诊断。
- **Baseline** · 强重排、证据评分和图检索。
- **Benchmark** · GraphRAG-Benchmark Medical 和 Novel。
- **关键结果 / 消融** · 报告稳定的证据转化差距。
- **适用条件 / 局限** · 限所测检索生成组合。

**可复用机制** · 加入图检索前验证引入的证据确实改变答案。

<a id="paper-150132"></a>

## When Does Interaction Help? Representational Tradeoffs in Value-Based Imitation Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/150132) · [作者来源](https://openreview.net/forum?id=kRq9hKJYQU)

- **问题 / 瓶颈** · 跟随专家数据和在自身状态询问专家解决不同问题。
- **核心创新 / 方法** · 跨专家与学生容量对照价值式模仿和在线查询。
- **Baseline** · DAgger 与离线价值模仿。
- **Benchmark** · 价值式模仿学习。
- **关键结果 / 消融** · 学生明显弱于教师时增益最大。
- **适用条件 / 局限** · 需要交互访问专家。

**可复用机制** · 学生受限时可在实际遇到的状态获取指导。

<a id="paper-152959"></a>

## When Does Knowing the State Help? Diagnosing Process vs. Outcome Reward Design

[官方论文页](https://neurips.cc/virtual/2026/poster/152959) · [作者来源](https://openreview.net/forum?id=P61QuZf0Po)

- **问题 / 瓶颈** · 耗费步骤标注未必比结局奖更有效。
- **核心创新 / 方法** · 对照仅动作文字和完整轨迹状态下的质量预测。
- **Baseline** · 过程与结果奖励。
- **Benchmark** · 十域十一任务。
- **关键结果 / 消融** · 提出区分两类奖励适用的低成本诊断。
- **适用条件 / 局限** · 依赖可比较步骤标签。

**可复用机制** · 先测历史状态究竟增加多少判断力，再决定奖励粒度。

<a id="paper-152207"></a>

## When does LeJEPA learn a World Model?

[官方论文页](https://neurips.cc/virtual/2026/poster/152207) · [作者来源](https://openreview.net/forum?id=UmYyYHEj9P)

- **问题 / 瓶颈** · 预测自监督不自动保证潜坐标正确。
- **核心创新 / 方法** · 分析 LeJEPA 正对的频谱分解。
- **Baseline** · 不同潜分布假设。
- **Benchmark** · 线性可识别性理论。
- **关键结果 / 消融** · 高斯潜分布下证明线性可识别。
- **适用条件 / 局限** · 非高斯推广未报告。

**可复用机制** · 学习世界表征时显式验证坐标能否恢复真状态。

<a id="paper-153281"></a>

## When Does Non-Uniform Replay Matter in Reinforcement Learning?

[官方论文页](https://neurips.cc/virtual/2026/poster/153281) · [作者来源](https://openreview.net/forum?id=MQaqQTPeHp)

- **问题 / 瓶颈** · 低采样量下均匀回放可能浪费关键信号
- **核心创新 / 方法** · 对照访问量下的非均匀回放
- **Baseline** · 标准回放和三种 RL 算法
- **Benchmark** · 五基准套件，单任务、多任务和并行仿真
- **关键结果 / 消融** · 低样本量更高效，高样本量仍有竞争力
- **适用条件 / 局限** · 回放收益依数据吞吐和算法

**可复用机制** · 限制环境数据时分别测回放收益与额外计算

<a id="paper-154943"></a>

## When Does Subspace Direction Matter for LoRA? Regime Analysis of the Magnitude Principle in Few-Shot Adaptation

[官方论文页](https://neurips.cc/virtual/2026/poster/154943) · [作者来源](https://openreview.net/forum?id=9lfZA1MK8L)

- **问题 / 瓶颈** · 仅调幅度对部分任务表达不足
- **核心创新 / 方法** · 拆分子空间方向和幅度并做对齐度分层
- **Baseline** · vanilla LoRA、全数据与生成负对照
- **Benchmark** · 少量标注分类，含 LLaMA-2-7B、Llama-3.1-8B
- **关键结果 / 消融** · 高对齐任务收益最大，完整数据不维持同规律
- **适用条件 / 局限** · 结论主要在少样本分类

**可复用机制** · 按任务而不是统一秩配置决定适配方向

<a id="paper-153823"></a>

## When Do Multi-Agent Systems Help? An Information Bottleneck Perspective

[官方论文页](https://neurips.cc/virtual/2026/poster/153823) · [作者来源](https://openreview.net/forum?id=ISYF5z5nK8)

- **问题 / 瓶颈** · 压缩帮助弱模型但可能丢强模型能利用的冗余
- **核心创新 / 方法** · 用信息瓶颈分析任务信号与通信容量
- **Baseline** · 不同模型强度和通信量
- **Benchmark** · 多智能体任务，摘要未列名单
- **关键结果 / 消融** · 强模型获益较少，收益依通信限制
- **适用条件 / 局限** · 结论随信息密度和模型而变

**可复用机制** · 固定算力比较共享摘要和全文的任务完成率

<a id="paper-151259"></a>

## When Expert Disagreement Hurts: Auditing Prestige-Sensitive Revision in LLM Decision Pipelines

[官方论文页](https://neurips.cc/virtual/2026/poster/151259) · [作者来源](https://openreview.net/forum?id=bjKMAt08Ab)

- **问题 / 瓶颈** · 高声望可能诱导没有证据的答案反转
- **核心创新 / 方法** · 对照输出翻转和教师强制 Yes/No 偏好变化
- **Baseline** · 身份标签干预及基础修订
- **Benchmark** · 专家意见冲突、最终准确率和有害翻转
- **关键结果 / 消融** · 部分翻转没有相应偏好换向
- **适用条件 / 局限** · 外推依任务和身份线索

**可复用机制** · 让判断者先读依据，再测试身份标记是否改变决策

<a id="paper-139854"></a>

## When Guessing is Rewarded: Rethinking Language Model Evaluation with Distributional Uncertainty Scoring

[官方论文页](https://neurips.cc/virtual/2026/poster/139854) · [作者来源](https://openreview.net/forum?id=0R23YXfZQM)

- **问题 / 瓶颈** · 只奖励 top-1 会鼓励过度确定。
- **核心创新 / 方法** · 引入含备选概率质量的评分。
- **Baseline** · 只有答对得分。
- **Benchmark** · 理论和示例，多选不确定。
- **关键结果 / 消融** · 激励模型适当分配答案概率。
- **适用条件 / 局限** · 需要可读且校准的选项概率。

**可复用机制** · 评测区别答对和诚实表达不确定。

<a id="paper-148838"></a>

## When Is Rank-1 Steering Cheap? Geometry, Granularity, and Budgeted Search

[官方论文页](https://neurips.cc/virtual/2026/poster/148838) · [作者来源](https://openreview.net/forum?id=umOBxhQMmJ)

- **问题 / 瓶颈** · 无效搜索易被误认为低秩本身无表达。
- **核心创新 / 方法** · 用方向对齐导航候选，比较评估次数。
- **Baseline** · 无几何引导搜索。
- **Benchmark** · 三个模型家族及多概念。
- **关键结果 / 消融** · 达到 95% 最佳效用所需试验平均少 39.8%。
- **适用条件 / 局限** · 已找到效用并非全局最优。

**可复用机制** · 将编辑表达上限和定位难度拆开。

<a id="paper-152041"></a>

## When is Warmstarting Effective for Scaling Language Models?

[官方论文页](https://neurips.cc/virtual/2026/poster/152041) · [作者来源](https://openreview.net/forum?id=VyDwjNRtd2)

- **问题 / 瓶颈** · 初始函数完美保留未必提升最终收敛。
- **核心创新 / 方法** · 比较简单和复杂 warmstart 及不同增长因子。
- **Baseline** · 冻结大小及既有 warmstart。
- **Benchmark** · 稠密 MLP 和 LLM。
- **关键结果 / 消融** · 2 倍增长最常有收敛加速，简单策略可赢。
- **适用条件 / 局限** · 预训练算预算和模型结构影响结果。

**可复用机制** · 从收敛曲线而非首步损失选扩容方法。

<a id="paper-149375"></a>

## When Language Overrules: Revealing Text Dominance in Multimodal Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149375) · [作者来源](https://openreview.net/forum?id=qWyrRaeDAc)

- **问题 / 瓶颈** · 加非文本 token 数可能加大弱势。
- **核心创新 / 方法** · 不增信息只复制 token，比较图和视觉压缩。
- **Baseline** · 默认模态融合。
- **Benchmark** · 视觉及稠密图任务。
- **关键结果 / 消融** · 复制增不平衡，图紧凑信息可反转。
- **适用条件 / 局限** · 压缩只初步验证。

**可复用机制** · 选模态预算看有效信号而非 token 对等。

<a id="paper-153967"></a>

## When Less is More: The LLM Scaling Paradox in Context Compression

[官方论文页](https://neurips.cc/virtual/2026/poster/153967) · [作者来源](https://openreview.net/forum?id=H9lFJNJ2so)

- **问题 / 瓶颈** · 更大压缩器可降重构误差却使意义含混。
- **核心创新 / 方法** · 对嵌入跨度和重构确定性做诊断。
- **Baseline** · 不同规模压缩器。
- **Benchmark** · 有损 compressor–decoder。
- **关键结果 / 消融** · 观察到规模—忠实度反转。
- **适用条件 / 局限** · 依赖编码、解码及信息密度。

**可复用机制** · 压缩选型不能凭重构单一均值。

<a id="paper-148797"></a>

## When LLM Routers Overpay: Strong-Model Over-Selection under Loose Budgets

[官方论文页](https://neurips.cc/virtual/2026/poster/148797) · [作者来源](https://openreview.net/forum?id=v2DOrFK8Wp)

- **问题 / 瓶颈** · 松预算会把容易问题也送强模型。
- **核心创新 / 方法** · 以查询模型交互和成本感知排名。
- **Baseline** · 现有路由器。
- **Benchmark** · RouterBench、MMR-Bench、MixInstruct、RouterEval。
- **关键结果 / 消融** · 相对成本更低并达强模型级表现。
- **适用条件 / 局限** · 需要稳定的价格和备选模型对照。

**可复用机制** · 预算宽松时仍检查升级必要性。

<a id="paper-155608"></a>

## When LLMs Know but Fail to Reason: Injecting Memory for Reasoning Enhancement

[官方论文页](https://neurips.cc/virtual/2026/poster/155608) · [作者来源](https://openreview.net/forum?id=4I2mGv36HD)

- **问题 / 瓶颈** · 写入更多知识未必改善步骤。
- **核心创新 / 方法** · 量记忆到推理的对齐并做免训练激活补足。
- **Baseline** · 自然激活。
- **Benchmark** · 知识参与及推理表现。
- **关键结果 / 消融** · 摘要提出机制，量化待核。
- **适用条件 / 局限** · 注入信号需隔离表面相关。

**可复用机制** · 先诊断检索不通还是推理不足，再做训练。

<a id="paper-150747"></a>

## When Metropolis and Hastings Meet Bradley and Terry: Exact MCMC From Preference Voting

[官方论文页](https://neurips.cc/virtual/2026/poster/150747) · [作者来源](https://openreview.net/forum?id=fhEDVqcpV8)

- **问题 / 瓶颈** · 普通 MH 要可评密度。
- **核心创新 / 方法** · Pref-MH 用二元随机比较实现目标定义下的采样。
- **Baseline** · 显式密度 MH。
- **Benchmark** · 人或模型裁判的条件分布。
- **关键结果 / 消融** · 在相应偏好模型下精确。
- **适用条件 / 局限** · 依赖偏好概率与目标假设。

**可复用机制** · 将生成裁判与概率采样模型的对应关系显式验证。

<a id="paper-153640"></a>

## When Must AI Training Stage Checkpoints? A Distributional Model of Durability Boundaries at Scale

[官方论文页](https://neurips.cc/virtual/2026/poster/153640) · [作者来源](https://openreview.net/forum?id=JouNw5l7RN)

- **问题 / 瓶颈** · 直接并行文件系统不总最快。
- **核心创新 / 方法** · 计算规模负载阈值再启暂存。
- **Baseline** · 统一开启或关闭暂存。
- **Benchmark** · 大训练持久化时间分布。
- **关键结果 / 消融** · 找到争用阈值后的策略变化。
- **适用条件 / 局限** · 需量真实耐久和故障恢复。

**可复用机制** · 分别测写入响应和首次可恢复时间。

<a id="paper-156014"></a>

## When Noise Meets Long-Tail: Feature-Threshold Dual Calibration for Robust Pseudo-Labeling

[官方论文页](https://neurips.cc/virtual/2026/poster/156014) · [作者来源](https://openreview.net/forum?id=1A8tQcymU6)

- **问题 / 瓶颈** · 通用阈值抑制稀有类并放大噪声。
- **核心创新 / 方法** · 教师学生双校准。
- **Baseline** · 现有伪分割。
- **Benchmark** · 四公开集、三噪声。
- **关键结果 / 消融** · 尾类改善突出。
- **适用条件 / 局限** · 尾部标签极稀时阈值不稳。

**可复用机制** · 将表示偏移与接收率作为两项独立诊断。

<a id="paper-148594"></a>

## When Parallelism Pays Off: Cohesion-Aware Task Partitioning for Multi-Agent Coding

[官方论文页](https://neurips.cc/virtual/2026/poster/148594) · [作者来源](https://openreview.net/forum?id=wYda526jWp)

- **问题 / 瓶颈** · 跨代理沟通和合并会抵消并行节省。
- **核心创新 / 方法** · 让依赖紧密的模块留同一代理。
- **Baseline** · 普通并行与单代理。
- **Benchmark** · 多代理软件任务。
- **关键结果 / 消融** · 摘要报告运行更有效，幅度待核。
- **适用条件 / 局限** · 依赖图需真实反映修改冲突。

**可复用机制** · 并行前估分割边的沟通成本。

<a id="paper-152350"></a>

## When Poison Meets Structure: Topology-based Defense against Poisoning Attack on Graph-based Retrieval-Augmented Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/152350) · [作者来源](https://openreview.net/forum?id=TirVWlIdjG)

- **问题 / 瓶颈** · 相似条目可使检索结果失真。
- **核心创新 / 方法** · 以拓扑一致性作为轻量防御信号。
- **Baseline** · 普通 GraphRAG。
- **Benchmark** · 图证据的污染防御。
- **关键结果 / 消融** · 摘要给结构差异及保护，确数待核。
- **适用条件 / 局限** · 真实新事实也可能缺支持，须控制误杀。

**可复用机制** · 证据验证不只看是否与查询相近。

<a id="paper-152992"></a>

## When Policies Cannot Be Retrained: A Unified Closed-Form View of Post-Training Steering in Offline Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/152992) · [作者来源](https://openreview.net/forum?id=OnU82otbDI)

- **问题 / 瓶颈** · 差先验可使加法修正坍缩。
- **核心创新 / 方法** · 精度加权 PoE 并选 KL 预算。
- **Baseline** · 加法和仅先验适配。
- **Benchmark** · D4RL MuJoCo、AntMaze。
- **关键结果 / 消融** · 较差先验时退化更缓，不能越过原 actor 能力。
- **适用条件 / 局限** · 底座必须足够有能力。

**可复用机制** · 上线组合策略用原 actor 作坏先验回退。

<a id="paper-155843"></a>

## When Policy Entropy Constraint Fails: Preserving Diversity in Flow-based RLHF via Perceptual Entropy

[官方论文页](https://neurips.cc/virtual/2026/poster/155843) · [作者来源](https://openreview.net/forum?id=2TmlUKr7RZ)

- **问题 / 瓶颈** · 策略熵不变仍可能感知坍缩。
- **核心创新 / 方法** · 定义感知熵并用于奖励正则。
- **Baseline** · 标准策略熵约束。
- **Benchmark** · 流式生成对齐及多样性。
- **关键结果 / 消融** · 发现两种熵可解耦。
- **适用条件 / 局限** · 感知表示对人类差异的有效性需验。

**可复用机制** · 对齐训练同时监控实际输出形态覆盖。

<a id="paper-150889"></a>

## When Prompt Internalization Breaks: Continuous Experience Internalization in Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150889) · [作者来源](https://openreview.net/forum?id=eeMSJRJsKy)

- **问题 / 瓶颈** · 连续内化会遗忘早补丁并放大误差。
- **核心创新 / 方法** · 循环巩固时分离稳定监督。
- **Baseline** · 普通提示内化。
- **Benchmark** · CEI-Bench，保旧、吸新及误差。
- **关键结果 / 消融** · 摘要给失效诊断和缓解，幅度未核。
- **适用条件 / 局限** · 监督冲突定义需准确。

**可复用机制** · 将修订保持与写入效率分开。

<a id="paper-155439"></a>

## When Prompts Override Vision: Instruction-Induced Hallucinations in LVLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/155439) · [作者来源](https://openreview.net/forum?id=5bYMpSBSze)

- **问题 / 瓶颈** · 背景知识会覆盖真实视觉证据。
- **核心创新 / 方法** · 分因构造 HalluScope 并对图像 grounding 做 DPO。
- **Baseline** · 未增强视觉对齐的底座。
- **Benchmark** · HalluScope。
- **关键结果 / 消融** · 文本指令先验是显著来源，缓解确数待核。
- **适用条件 / 局限** · 诊断取决于提示及反事实控制。

**可复用机制** · 模型验收要求在文本与图像冲突时按视觉证据作答。

<a id="paper-152080"></a>

## When Riemann flows with Wasserstein: Generative Modeling of Probability Distributions on Manifolds

[官方论文页](https://neurips.cc/virtual/2026/poster/152080) · [作者来源](https://openreview.net/forum?id=VcYi3zSNpE)

- **问题 / 瓶颈** · 欧式直线可能移出流形。
- **核心创新 / 方法** · 回归至流形最优输运速度。
- **Baseline** · 常规流匹配。
- **Benchmark** · 流形上的生成分布。
- **关键结果 / 消融** · 摘要给理论性传输保证。
- **适用条件 / 局限** · 依赖可计算几何。

**可复用机制** · 对带硬几何约束的生成任务，从路径定义保留约束。

<a id="paper-151380"></a>

## When Safety Becomes An Outlier: Understanding the Retention of LLM Safety Behaviors

[官方论文页](https://neurips.cc/virtual/2026/poster/151380) · [作者来源](https://openreview.net/forum?id=b28qPD14np)

- **问题 / 瓶颈** · 模板可能被当成分布离群记忆。
- **核心创新 / 方法** · 控制模板和上下文相关拒答并持续微调。
- **Baseline** · 固定拒绝模板。
- **Benchmark** · 安全保留及帮助性。
- **关键结果 / 消融** · 报告自然句式改善保留。
- **适用条件 / 局限** · 需确保内容与场景匹配。

**可复用机制** · 安全行为的输出多样性可以作为抗遗忘变量。

<a id="paper-151343"></a>

## When Scores Conflict with Preferences: Calibrated Drift Control for Heterogeneous DPO

[官方论文页](https://neurips.cc/virtual/2026/poster/151343) · [作者来源](https://openreview.net/forum?id=bFc8A2Irjf)

- **问题 / 瓶颈** · 偏好和约束异质时某些更新增加违规。
- **核心创新 / 方法** · 按对齐和冲突样本的平衡估计漂移并约束。
- **Baseline** · 受约束和多目标对齐。
- **Benchmark** · 偏好性能与目标漂移。
- **关键结果 / 消融** · 摘要报告改善折中。
- **适用条件 / 局限** · 一阶诊断依赖局部近似。

**可复用机制** · 多目标对齐要测更新方向而不只看总体偏好正确率。

<a id="paper-154558"></a>

## When Should Agents Remember? Falsification-Gated Self-Evolution for LLM Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/154558) · [作者来源](https://openreview.net/forum?id=ChLHUJr0U1)

- **问题 / 瓶颈** · 失败的自我反思会污染后续任务。
- **核心创新 / 方法** · 把经验写成带适用条件和预测效果的可反驳假设。
- **Baseline** · 自动写入反思记忆。
- **Benchmark** · 目标迁移、反证和归档检查。
- **关键结果 / 消融** · 摘要报告门控式记忆有益。
- **适用条件 / 局限** · 依赖可核查迁移样本。

**可复用机制** · 把记忆更新当部署变更，用对照测试作为写入条件。

<a id="paper-154389"></a>

## When Should LLMs Be Less Specific? Selective Abstraction for Reliable Long-Form Text Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/154389) · [作者来源](https://openreview.net/forum?id=Dw4Z2wUSe3)

- **问题 / 瓶颈** · 少数错误细节会损害长文可靠性。
- **核心创新 / 方法** · 按原子论断选择抽象并以风险定阈值。
- **Baseline** · 普通生成与选择性保留。
- **Benchmark** · 选择风险及内容覆盖。
- **关键结果 / 消融** · 摘要报告介于细节与可靠性的可用折中。
- **适用条件 / 局限** · 依赖可靠置信度。

**可复用机制** · 分段控制描述分辨率，尽量保留有证据的信息。

<a id="paper-139169"></a>

## When Simulation Lies: A Sim-to-Real Benchmark and Domain-Randomized RL Recipe for Tool-Use Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/139169) · [作者来源](https://openreview.net/forum?id=gsyvQACB3x)

- **问题 / 瓶颈** · 仅干净仿真训练不覆盖运行故障。
- **核心创新 / 方法** · 分类构造可核验变化并进行鲁棒训练。
- **Baseline** · 无随机化工具代理。
- **Benchmark** · RobustBench-TC 的 22 种变化。
- **关键结果 / 消融** · 摘要报告可转移到未见故障。
- **适用条件 / 局限** · 限所覆盖的交互能力。

**可复用机制** · 工具模拟误差要分机制测试，按易失效环节采样。

<a id="paper-139510"></a>

## When Stored Evidence Stops Being Usable: Scale-Conditioned Evaluation of Agent Memory

[官方论文页](https://neurips.cc/virtual/2026/poster/139510) · [作者来源](https://openreview.net/forum?id=LXvDQgan2w)

- **问题 / 瓶颈** · 存入更多不等于可检索使用。
- **核心创新 / 方法** · 估可用边界、尾部调用和失效原因。
- **Baseline** · 不同平面及层级接口。
- **Benchmark** · LongMemEval、LoCoMo。
- **关键结果 / 消融** · 给出依赖规模和预算的可用边界。
- **适用条件 / 局限** · 随代理和接口改变。

**可复用机制** · 记忆验收同时记录规模、成功和最坏成本。

<a id="paper-151337"></a>

## When Symbol Names Should Not Matter: A Logistic Theory of Fresh-Symbol Classification

[官方论文页](https://neurips.cc/virtual/2026/poster/151337) · [作者来源](https://openreview.net/forum?id=bIdWoi4kWA)

- **问题 / 瓶颈** · 偶然符号重叠可给虚假结构能力。
- **核心创新 / 方法** · 拆出理想模板结果和有限样本词元误差。
- **Baseline** · 各正则及训练样本数量。
- **Benchmark** · 合成模板。
- **关键结果 / 消融** · 验证符号重叠带来的有限样本项。
- **适用条件 / 局限** · 适用分析的核及任务。

**可复用机制** · 结构泛化验证可重复随机改名并保持标签。

<a id="paper-151892"></a>

## When the Merge Coefficient Stops Mattering: Proximity Regularized Merging for Continual LoRA Adaptation

[官方论文页](https://neurips.cc/virtual/2026/poster/151892) · [作者来源](https://openreview.net/forum?id=XA9pSXrybR)

- **问题 / 瓶颈** · 推理时调合并系数不能修复不兼容更新。
- **核心创新 / 方法** · 添加接近正则配合多种写入规则。
- **Baseline** · 固定及系数优化方案。
- **Benchmark** · 持续 LoRA 和类增量。
- **关键结果 / 消融** · 摘要报告多设置 AAA 增益。
- **适用条件 / 局限** · 机制限所测适配器。

**可复用机制** · 需要后续合并时在训练阶段加入可合并目标。

<a id="paper-139243"></a>

## When the Most Disruptive Messages Are Safe to Prune in Aggregate: Functional Analysis of Communication Pruning in Two-Agent LLM Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/139243) · [作者来源](https://openreview.net/forum?id=cbbBD5fxYU)

- **问题 / 瓶颈** · 高干扰消息单独和一起删除可能影响不同。
- **核心创新 / 方法** · 按功能分类并跨模型回归验证。
- **Baseline** · 完整通信与各种裁剪。
- **Benchmark** · 21661 条消息、三底座四领域。
- **关键结果 / 消融** · 找到依赖底座的失效边界。
- **适用条件 / 局限** · 结论限双代理。

**可复用机制** · 剪枝策略要用真实批量删减测试，不能简单叠加逐条归因。

<a id="paper-153763"></a>

## When Think-with-Image Meets Safety: What Determines Multimodal Jailbreak Robustness?

[官方论文页](https://neurips.cc/virtual/2026/poster/153763) · [作者来源](https://openreview.net/forum?id=IrAuZcQJ25)

- **问题 / 瓶颈** · 只测输入输出忽略视觉处理方式。
- **核心创新 / 方法** · 在不同视觉工具设计下对照安全行为。
- **Baseline** · 较少显式图像交互的模型。
- **Benchmark** · 所测视觉语言模型和安全任务。
- **关键结果 / 消融** · 显式工具交互相对降低风险约 30%。
- **适用条件 / 局限** · 不保证每一工具或环境。

**可复用机制** · 部署前把工具接入作为防护系统的一部分验收。

<a id="paper-152014"></a>

## When to Adopt Model Updates

[官方论文页](https://neurips.cc/virtual/2026/poster/152014) · [作者来源](https://openreview.net/forum?id=W9csns6HGO)

- **问题 / 瓶颈** · 提前全量替换或拒绝无法区分各任务变化。
- **核心创新 / 方法** · 组合几何相似和信息充分性验证。
- **Baseline** · 统一选择更新。
- **Benchmark** · 上游更新与下游迁移的决策。
- **关键结果 / 消融** · 据摘要可选择性采纳。
- **适用条件 / 局限** · 需要可比较下游表征。

**可复用机制** · 为每项服务独立验证升级需要，避免统一强制切换。

<a id="paper-149570"></a>

## When to Align, When to Predict: A Phase Diagram for Multimodal Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149570) · [作者来源](https://openreview.net/forum?id=p90UBwHbhg)

- **问题 / 瓶颈** · 联合模型可能输给最佳单模态。
- **核心创新 / 方法** · 用线性信号噪声模型研究相关干扰。
- **Baseline** · 单模态、对齐和监督预测。
- **Benchmark** · 多模态线性理论。
- **关键结果 / 消融** · 给出可对比目标的信噪区间。
- **适用条件 / 局限** · 依赖线性和低秩假设。

**可复用机制** · 保留单模态强基线，并在共享噪声较强时测对齐的副作用。

<a id="paper-150327"></a>

## When to Trust a PFN: Detecting Harmful Shift in Tabular Foundation Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150327) · [作者来源](https://openreview.net/forum?id=ixQvsT5Hku)

- **问题 / 瓶颈** · 一般距离可能对良性偏移误报。
- **核心创新 / 方法** · 以无标签目标和锚数据的适配损失构造单侧检验。
- **Baseline** · 普通偏移检测。
- **Benchmark** · 14 数据集，TabPFN 与 TabICL。
- **关键结果 / 消融** · 匹配或改善有害检测，良性误报更少。
- **适用条件 / 局限** · 需合适锚数据及所给检验设定。

**可复用机制** · 阈值选择应针对预测风险而非任意分布差异。

<a id="paper-155733"></a>

## When Trackers Fail: VLM-Guided Verification and Recovery for Robust Video Object Segmentation

[官方论文页](https://neurips.cc/virtual/2026/poster/155733) · [作者来源](https://openreview.net/forum?id=3LeU4hTu4y)

- **问题 / 瓶颈** · 连续传播会积累分割漂移
- **核心创新 / 方法** · 以 VLM 判断何时选择性恢复，保留常规传播
- **Baseline** · SAM3
- **Benchmark** · LVOS-v2、SecVOS；J&F
- **关键结果 / 消融** · 分别提升 1.2 和 2.7
- **适用条件 / 局限** · 故障检测需额外时延，摘要未量化

**可复用机制** · 动态视觉系统将失败触发器与重建器分开验收

<a id="paper-151558"></a>

## Where Does Warm-Up Come From? Adaptive Scheduling for Norm-Constrained Optimizers

[官方论文页](https://neurips.cc/virtual/2026/poster/151558) · [作者来源](https://openreview.net/forum?id=ZhOdAQqrsd)

- **问题 / 瓶颈** · 固定预热依赖额外网格搜索
- **核心创新 / 方法** · 用自适应规则调整预热日程
- **Baseline** · 手工选优的 warm-up
- **Benchmark** · 不同 LLaMA 训练配置
- **关键结果 / 消融** · 匹配或超过最佳人调日程，不加超参搜索
- **适用条件 / 局限** · 摘要未展开选择信号，其他优化器需复核

**可复用机制** · 在训练初期测不同日程的稳定性及预算

<a id="paper-148457"></a>

## Where Do Long Captions Fail? Position-Aware Diagnosis and Reinforcement Learning for Detailed Image Captioning

[官方论文页](https://neurips.cc/virtual/2026/poster/148457) · [作者来源](https://openreview.net/forum?id=xguY8UCo1t)

- **问题 / 瓶颈** · 全局质量掩盖末段或某位置的幻觉
- **核心创新 / 方法** · 将描述拆成有位置的陈述，用有据性奖励训练
- **Baseline** · 长描述基线及全局评分
- **Benchmark** · 详细图像描述，分位置依据及偏好
- **关键结果 / 消融** · 两项改善且全局质量有竞争力
- **适用条件 / 局限** · 陈述抽取与依据标注需要独立检验

**可复用机制** · 高风险细节按主张分段验证再调描述长度

<a id="paper-139698"></a>

## Where Root Cause Analysis Fails: A Retrieval-Reranking Decomposition

[官方论文页](https://neurips.cc/virtual/2026/poster/139698) · [作者来源](https://openreview.net/forum?id=A2XdbroU25)

- **问题 / 瓶颈** · 最终诊断错可能由候选缺失或排序失效导致
- **核心创新 / 方法** · 多信号检索再 LLM 重排，依两级错误分解
- **Baseline** · 既有根因诊断法
- **Benchmark** · 简单及复杂故障；top-1
- **关键结果 / 消融** · 复杂增 2–26 点，简单增 9–13 点
- **适用条件 / 局限** · 结果不证明找到因果机制

**可复用机制** · 部署诊断助手先检索足够候选，再验证真实根因排名

<a id="paper-153022"></a>

## Where to Approximate in Neurosymbolic Inference?

[官方论文页](https://neurips.cc/virtual/2026/poster/153022) · [作者来源](https://openreview.net/forum?id=OZpQpBHvJk)

- **问题 / 瓶颈** · 训练可接受的近似未必能保留推理精度
- **核心创新 / 方法** · 对比不同近似编译对符号推理和模型学习效果
- **Baseline** · 精确和不同粗度近似
- **Benchmark** · 概率推理及神经符号学习
- **关键结果 / 消融** · 粗近似仍可保持下游精度，推理保真更敏感
- **适用条件 / 局限** · 证据依任务目标和近似部位

**可复用机制** · 分开验收高精确回答与大批训练的近似预算

<a id="paper-155128"></a>

## Where You Backpropagate Matters: Token Hypothesis for Memory-Efficient Fine-Tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/155128) · [作者来源](https://openreview.net/forum?id=8D8sa1Nuh0)

- **问题 / 瓶颈** · 全 token 激活占用限制长上下文训练
- **核心创新 / 方法** · 按 token 选择反传路径，并可叠加 LoRA/DoRA
- **Baseline** · 常规反传及 PEFT 组合
- **Benchmark** · 长上下文、GLUE、图像等任务，五种骨干
- **关键结果 / 消融** · 长上下文总显存最多少约 20%
- **适用条件 / 局限** · 需检查长尾 token 的梯度信息是否遗漏

**可复用机制** · 等内存比较丢反传位置和减上下文长度

<a id="paper-151199"></a>

## Which Tokens to Merge? Diffusion Dynamics for Efficient Image Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/151199) · [作者来源](https://openreview.net/forum?id=cDWOMIJrbJ)

- **问题 / 瓶颈** · 静态相似忽略各处去噪需求。
- **核心创新 / 方法** · 以动态分数指导免训练合并。
- **Baseline** · 常规 token 合并。
- **Benchmark** · PixArt-α、FLUX。
- **关键结果 / 消融** · 保持图像局部和全局保真。
- **适用条件 / 局限** · 速度及阈值依采样器。

**可复用机制** · 查看哪些位置后续还会改变，再裁冗余。

<a id="paper-153430"></a>

## Which Way Did It Move? Diagnosing and Overcoming Directional Motion Blindness in Video LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/153430) · [作者来源](https://openreview.net/forum?id=LOIQXC7mpg)

- **问题 / 瓶颈** · 内部可见方向但回答仍绑定错误。
- **核心创新 / 方法** · 分测编码器、投影及 LLM，调合成方向数据。
- **Baseline** · 未专项适配 VLM。
- **Benchmark** · MODIRECT 和不同视觉复杂度。
- **关键结果 / 消融** · 域内减错误，复杂画面仍难外推。
- **适用条件 / 局限** · 只用合成指令易过拟合。

**可复用机制** · 低层感知先验编码和输出读出分别修。

<a id="paper-150074"></a>

## Who caused $Y$? Local identifiability for learning causal parents

[官方论文页](https://neurips.cc/virtual/2026/poster/150074) · [作者来源](https://openreview.net/forum?id=kvVc2NQe9H)

- **问题 / 瓶颈** · 独立残差本身不能选真父集。
- **核心创新 / 方法** · 在满足假设的候选中最小化残差方差、再最小基数。
- **Baseline** · 只用残差独立。
- **Benchmark** · 加性噪声父集识别理论。
- **关键结果 / 消融** · 在无反向假设下可识别。
- **适用条件 / 局限** · 条件和独立性检验必须验证。

**可复用机制** · 对世界模型不必恢复整图，可先识别影响单个状态的父集。

<a id="paper-154032"></a>

## Whole-Body Compliant Control via Learned Force-Regulation Modules

[官方论文页](https://neurips.cc/virtual/2026/poster/154032) · [作者来源](https://openreview.net/forum?id=GlpxwFNGx2)

- **问题 / 瓶颈** · 位置跟随忽略接触下顺应性。
- **核心创新 / 方法** · 以学习的力调节组件实现全身遥操作。
- **Baseline** · 现有全身顺应控制。
- **Benchmark** · 模拟及 27 自由度 Sprout。
- **关键结果 / 消融** · 展示实机全身遥操作，幅度未核。
- **适用条件 / 局限** · 依赖力传感和硬件标定。

**可复用机制** · 把接触力调节与全局动作指令分离评估。

<a id="paper-150794"></a>

## Who Needs Labels? Adapting Vision Foundation Models With the Metadata You Already Have

[官方论文页](https://neurips.cc/virtual/2026/poster/150794) · [作者来源](https://openreview.net/forum?id=fLuDbpk8Ib)

- **问题 / 瓶颈** · 通用主干在专业域视觉先验不充分。
- **核心创新 / 方法** · 以可得元数据信号适配不需新标注。
- **Baseline** · 未适配视觉基础模型。
- **Benchmark** · 定域科学视觉。
- **关键结果 / 消融** · 摘要提出无标签适配，量化待核。
- **适用条件 / 局限** · 元数据可能变成泄漏捷径。

**可复用机制** · 集合切分按来源和设备，防元信息预测标签。

<a id="paper-153354"></a>

## Who Says What: Symbolic Trimodal Binding Mechanisms in Audio-Visual LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/153354) · [作者来源](https://openreview.net/forum?id=M0fBuZdipl)

- **问题 / 瓶颈** · 听得清且看得见仍可能把台词给错人。
- **核心创新 / 方法** · 以现成活动说话人检测供提示。
- **Baseline** · 原音视频语言模型。
- **Benchmark** · 三模态说话人台词关联。
- **关键结果 / 消融** · 观察错误主要出在音视连接。
- **适用条件 / 局限** · 依赖主动说话人模型在遮挡下质量。

**可复用机制** · 不同模态对错要测实体一致性。

<a id="paper-151857"></a>

## Who Should Evolve? Uncertainty-Aware Role Bottleneck Inference for Multi-Agent LLM Training

[官方论文页](https://neurips.cc/virtual/2026/poster/151857) · [作者来源](https://openreview.net/forum?id=XONEq9blMw)

- **问题 / 瓶颈** · 出现症状的角色可能是上游失误受害者。
- **核心创新 / 方法** · 对每轨迹推断瓶颈及不确定性。
- **Baseline** · 全角色或症状角色更新。
- **Benchmark** · HotpotQA、2WikiMultihopQA、MuSiQue。
- **关键结果 / 消融** · 摘要报告改进，幅度待核。
- **适用条件 / 局限** · 需要足够反事实归因证据。

**可复用机制** · 先核归因再分配角色训练预算。

<a id="paper-139035"></a>

## Who&When Pro: Can LLMs Really Attribute Failures in AI Agents?

[官方论文页](https://neurips.cc/virtual/2026/poster/139035) · [作者来源](https://openreview.net/forum?id=ot6saieu5V)

- **问题 / 瓶颈** · 成功率看不出责任源。
- **核心创新 / 方法** · 统一自动归因评估并跨协议分析。
- **Baseline** · 不同家族、协议及数据呈现。
- **Benchmark** · Who&When Pro。
- **关键结果 / 消融** · 观察失败归因系统性差异。
- **适用条件 / 局限** · 多角色互动可有多个真实促因。

**可复用机制** · 回放日志按角色和时间标故障，避免用末端角色替代源头。

<a id="paper-149850"></a>

## Who Wrote This Paper? Autonomous Scientific Discovery for 3DGS Research

[官方论文页](https://neurips.cc/virtual/2026/poster/149850) · [作者来源](https://openreview.net/forum?id=mptCBNtiEN)

- **问题 / 瓶颈** · 生成论文可能出现无法追溯的实验。
- **核心创新 / 方法** · 工作流执行复现、扩展、训练和消融，并维持记录绑定。
- **Baseline** · 常规手工 3DGS 迭代。
- **Benchmark** · Mip-NeRF 360、LLFF。
- **关键结果 / 消融** · 展示端到端与数字追踪。
- **适用条件 / 局限** · 一领域的趋势不能代表普适科学发现。

**可复用机制** · 验自动研究的证据链和复实际验。

<a id="paper-153112"></a>

## Why Are LLMs Confidently Wrong? Correcting Overconfident Errors via Causal Head Intervention

[官方论文页](https://neurips.cc/virtual/2026/poster/153112) · [作者来源](https://openreview.net/forum?id=Npk8kJ1fGH)

- **问题 / 瓶颈** · 单温度不区分不同过度自信机制。
- **核心创新 / 方法** · 定位因果贡献注意头并改置信。
- **Baseline** · 原模型或通用校准。
- **Benchmark** · 五多选问答，ECE、NLL、Brier。
- **关键结果 / 消融** · 改善校准并保准确。
- **适用条件 / 局限** · 干预和任务选项配置可能不通用。

**可复用机制** · 按错型校准，先验组件影响再改输出。

<a id="paper-154639"></a>

## Why Copy Others? Insights into Social Learning from Multi-Agent Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/154639) · [作者来源](https://openreview.net/forum?id=C75XbOudqL)

- **问题 / 瓶颈** · 盲从会复制错误且传播有成本。
- **核心创新 / 方法** · 比较单独试验与选择性社会学习。
- **Baseline** · 独立学习和普遍模仿。
- **Benchmark** · 多代理强化任务。
- **关键结果 / 消融** · 摘要报告何时模仿更有效，幅度待核。
- **适用条件 / 局限** · 取决于同伴技能和可观测性。

**可复用机制** · 只有同伴行为里的新信息价值超过获取成本时模仿。
