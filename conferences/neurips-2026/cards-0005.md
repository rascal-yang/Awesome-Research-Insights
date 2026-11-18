# NeurIPS 2026 论文卡 5

[会议索引](README.md)

<a id="paper-149767"></a>

## Eliciting Zero-Shot Named Entity Recognition in Large Language Models via Instruction Semantic Elaboration

[官方论文页](https://neurips.cc/virtual/2026/poster/149767) · [作者来源](https://openreview.net/forum?id=nTbfA3r6QL)

- **问题 / 瓶颈** · 直接给类别名难以消除近义类型混淆。
- **核心创新 / 方法** · 用相邻概念对照、构成要素拆分与具体示例扩展指令。
- **Baseline** · 原始指令及强基线，名称待核。
- **Benchmark** · 四个领域的零样本 NER，比较 F1。
- **关键结果 / 消融** · 作者报告相对初始指令提高 10.99%，相对强基线提高 6.89%。
- **适用条件 / 局限** · 实体定义和示例质量仍可能影响迁移。

**可复用机制** · 固定模型和评测集，分别消融类别对照、定义拆分与示例。

<a id="paper-139367"></a>

## ELMA: Benchmarking Anaphoric Compositions for Long-Term Text-to-Motion Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/139367) · [作者来源](https://openreview.net/forum?id=UWLadjotaK)

- **问题 / 瓶颈** · 上一片段定义的约束容易被后续生成遗忘。
- **核心创新 / 方法** · 从自然视频提取连续 30 秒动作并标注片段间依赖，用于微调。
- **Baseline** · 现有动作生成器及微调版本。
- **Benchmark** · ELMA，测整体物理合理性与文本语义对齐。
- **关键结果 / 消融** · 发现上下文依赖指令是明显弱点，微调改善两类指标；幅度待核。
- **适用条件 / 局限** · 依赖自动标注质量，超出已测片段时长待验证。

**可复用机制** · 对照含指代与独立描述，分开报告动作质量和跨段约束保持。

<a id="paper-154929"></a>

## ELPAC: Endpoint-Anchored Latent Progression with Stage-Varying Multimodal Coordination

[官方论文页](https://neurips.cc/virtual/2026/poster/154929) · [作者来源](https://openreview.net/forum?id=9u0n8IU711)

- **问题 / 瓶颈** · 部分观测的横截面队列难区分阶段、亚型和残差关联。
- **核心创新 / 方法** · 用端点和单调趋势约束贝叶斯轨迹，以稀疏残差因子表达分阶段的关联。
- **Baseline** · 群体轨迹、协方差回归及融合路线；具名对照待核。
- **Benchmark** · 合成数据与 ADNI、NACC/SCAN 队列，检验恢复与区间校准。
- **关键结果 / 消融** · 作者报告结构恢复准确、区间校准良好，且发现亚型间关联差异。
- **适用条件 / 局限** · 依赖端点可靠性及可辨识假设；横截面关联无法直接证明因果。

**可复用机制** · 对部分观测队列把阶段趋势与残差因子分开建模，先用已知真值仿真检查误归因。

<a id="paper-149339"></a>

## ELSA3D: Elastic Semantic Anchoring for Unified 3D Understanding and Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/149339) · [作者来源](https://openreview.net/forum?id=qoh4UZPjM8)

- **问题 / 瓶颈** · 平铺两类 token 容易混杂全局结构和局部细节。
- **核心创新 / 方法** · 动态锚 token 在选定尺度融合语言和几何，每个块路由激活的锚。
- **Baseline** · 比较最强统一模型及同架构非弹性版本。
- **Benchmark** · 图像到三维、文本到三维、三维描述。
- **关键结果 / 消融** · 作者报告所列指标领先，较非弹性版 FLOPs 和时延约减半。
- **适用条件 / 局限** · 需可靠的多尺度几何特征，路由选择可能漏掉细节。

**可复用机制** · 在固定骨干下对照平铺融合与尺度条件路由，并报告实际时延。

<a id="paper-153273"></a>

## EMA-Nesterov: Stabilizing Nesterov's Lookahead for Accelerated Deep Learning Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/153273) · [作者来源](https://openreview.net/forum?id=MTYA6Kc3Bb)

- **问题 / 瓶颈** · 一步参数差在随机非凸训练中噪声较大。
- **核心创新 / 方法** · 用指数滑动平均替换 Nesterov 瞬时前瞻，仍为单循环。
- **Baseline** · 标准 Nesterov、短期及多步前瞻。
- **Benchmark** · 凸收敛分析与 Adam、SOAP、Muon 上的深度训练。
- **关键结果 / 消融** · 保留凸加速率；摘要报告语言预训练等任务改善。
- **适用条件 / 局限** · 凸理论不直接保证非凸训练加速，EMA 时标待调。

**可复用机制** · 固定步数和算力，对照一步前瞻与更新 EMA 并扫描梯度噪声。

<a id="paper-149789"></a>

## Embedded-Arena: Building Hardware-in-the-Loop Coding Agents to Run AI on Microcontrollers

[官方论文页](https://neurips.cc/virtual/2026/poster/149789) · [作者来源](https://openreview.net/forum?id=nJ0AEgMZGZ)

- **问题 / 瓶颈** · 静态推断难同时满足精度、内存和功耗。
- **核心创新 / 方法** · 在授权设备上迭代编译部署，回传测量并调整模型与固件。
- **Baseline** · 无硬件反馈的前沿模型与人类专家。
- **Benchmark** · 商用 MCU，视觉、音频压缩，以及相机与穿戴案例。
- **关键结果 / 消融** · 无反馈成功率为 0%；闭环三轮内首次部署，七轮内可超专家。
- **适用条件 / 局限** · 依赖可重复的目标硬件测量，跨设备结果待核。

**可复用机制** · 优化端侧部署时，以实际测得的资源约束为反馈并设无反馈对照。

<a id="paper-153155"></a>

## Embedding Foundation Model Predictions in Discrete-Choice Models with Structural Guarantees

[官方论文页](https://neurips.cc/virtual/2026/poster/153155) · [作者来源](https://openreview.net/forum?id=NTGgX4PiPf)

- **问题 / 瓶颈** · 端到端预测可能违反价格单调性或给出异常支付意愿。
- **核心创新 / 方法** · 先用带符号约束的多项 logit 拟合结构系数，再冻结并加入基于预计算预测的小型修正。
- **Baseline** · 多项 logit 及两个表格基础模型。
- **Benchmark** · 三个离散选择数据集，测准确率、成本单调与时间价值。
- **关键结果 / 消融** · 平均提升 6.4 个百分点，保持 100% 成本单调；作者证明保留边际替代率。
- **适用条件 / 局限** · 保证依赖修正项的结构，其他约束需额外证明。

**可复用机制** · 在有经济结构限制的预测中，将可解释系数与残差校正分开训练。

<a id="paper-154694"></a>

## Embedding Security Properties into AI-Enabled Cyber-Physical Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/154694) · [作者来源](https://openreview.net/forum?id=BhPABKjORM)

- **问题 / 瓶颈** · 只重建输入不能确保时间序列预测满足系统约束。
- **核心创新 / 方法** · 在预测防护框架中用信号时序逻辑约束修复和输出精修。
- **Baseline** · 规则过滤及仅重建路线，具体对照待核。
- **Benchmark** · 真实多变量控制系统预测，比较干扰下的稳健性和规范符合率。
- **关键结果 / 消融** · 作者报告规范符合率和稳健性提升，单独重建无法达到同样效果。
- **适用条件 / 局限** · 依赖正确规范，未见场景的保证范围待核。

**可复用机制** · 防御评测时同时记录输入恢复误差和输出违反规范的比例。

<a id="paper-155251"></a>

## Embeddings for Preferences, Not Semantics

[官方论文页](https://neurips.cc/virtual/2026/poster/155251) · [作者来源](https://openreview.net/forum?id=76xjwLMwhW)

- **问题 / 瓶颈** · 语义相似度可能错误代理同意程度。
- **核心创新 / 方法** · 构造打破语义干扰和偏好关联的合成训练数据，改变最优打分器所依赖的信号。
- **Baseline** · 通用文本嵌入及其余弦相似度。
- **Benchmark** · 11 个在线协商数据集，测偏好预测。
- **关键结果 / 消融** · 证明解相关能减少对干扰信号的依赖，实验报告偏好预测改善。
- **适用条件 / 局限** · 依赖合成配对确实保留所需立场，跨文化迁移待核。

**可复用机制** · 用同立场不同措辞及同措辞不同立场的配对，分别测试嵌入距离。

<a id="paper-153742"></a>

## Embodied Neurocomputation: A Framework for Interfacing Biological Neural Cultures with Scaled Task-Driven Validation

[官方论文页](https://neurips.cc/virtual/2026/poster/153742) · [作者来源](https://openreview.net/forum?id=J4K89pUUjW)

- **问题 / 瓶颈** · 单次任务成功不足以区分偶然表现与持续学习。
- **核心创新 / 方法** · 以简单模拟导航做统一任务，比较配置在多回合中的学习一致性。
- **Baseline** · 匹配交互预算的优化 DQN。
- **Benchmark** · 模拟网格导航，观察多回合表现。
- **关键结果 / 消融** · 作者报告少数配置稳定学习且优于所比 DQN。
- **适用条件 / 局限** · 任务简单，计算和能量成本并未由交互预算自动匹配。

**可复用机制** · 比较不同计算系统时，同时报告重复回合学习和资源口径。

<a id="paper-148643"></a>

## EmbodiedObject: All-in-One Object Understanding with SLAT

[官方论文页](https://neurips.cc/virtual/2026/poster/148643) · [作者来源](https://openreview.net/forum?id=wBnYpq6K32)

- **问题 / 瓶颈** · 视觉真实的资产仍可能缺少部件与操作属性。
- **核心创新 / 方法** · 分析二维到三维生成潜空间，用统一解码器输出可供性、部件分割与关节信息。
- **Baseline** · 现有统一点云编码器。
- **Benchmark** · 真实图像输入的三维物体属性预测；具名数据集待核。
- **关键结果 / 消融** · 报告生成潜变量富含局部结构语义；量化待核。
- **适用条件 / 局限** · 依赖生成结果及遮挡敏感性，任务泛化待验证。

**可复用机制** · 固定解码器，对比生成模型潜变量和专用点编码器的局部属性可预测性。

<a id="paper-148357"></a>

## Embodied-R1.5: Evolving Physical Intelligence via Embodied Foundation Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148357) · [作者来源](https://openreview.net/forum?id=yUKiJaJzFl)

- **问题 / 瓶颈** · 感知定位、计划与纠错联合训练会产生异质任务冲突。
- **核心创新 / 方法** · 平衡多任务强化学习，并以计划、定位、纠错交替构成闭环。
- **Baseline** · Gemini-Robotics-ER-1.5、GPT-5.4 以及动作模型对照。
- **Benchmark** · 24 项具身 VLM 基准、四套操作基准及真机测试。
- **关键结果 / 消融** · 作者报告 8B 模型在 16 项 VLM 基准领先，并展示低数据动作适配。
- **适用条件 / 局限** · 数据扩量与训练设计的独立贡献待全文核实。

**可复用机制** · 在相同数据下比较均衡训练和混合采样，同时消融在线纠错。

<a id="paper-139530"></a>

## EMERGE: A Benchmark for Updating Knowledge Graphs with Emerging Textual Knowledge

[官方论文页](https://neurips.cc/virtual/2026/poster/139530) · [作者来源](https://openreview.net/forum?id=KQZ7c8k0kf)

- **问题 / 瓶颈** · 独立抽取关系无法决定现有图需要怎样更新。
- **核心创新 / 方法** · 将文本与时间对应的已有知识图配对，监督具体图编辑。
- **Baseline** · 独立文本抽取路线；具名实验基线待核。
- **Benchmark** · EMERGE 使用 2019–2025 七个 Wikidata 快照、23.3 万段文本和 119 万编辑。
- **关键结果 / 消融** · 报告困难集中在文本新知识与现有结构的结合，细项待核。
- **适用条件 / 局限** · 维基编辑时间不一定等同于事实变化时间。

**可复用机制** · 将图更新评测拆成事实理解和结合当前状态执行合法编辑。

<a id="paper-149226"></a>

## Emergence of a Shared Canonical Object Frame from In-the-Wild Videos

[官方论文页](https://neurips.cc/virtual/2026/poster/149226) · [作者来源](https://openreview.net/forum?id=rzUWi6tqwc)

- **问题 / 瓶颈** · 手工定义类别姿态坐标不易扩展。
- **核心创新 / 方法** · 学习像素到共享网格的稠密对应，用带噪 SfM 估计逐序列对齐，并施加多视图一致性。
- **Baseline** · 有规范姿态标签的类别位姿方法。
- **Benchmark** · 16 万野外物体视频训练，类别级姿态评测。
- **关键结果 / 消融** · 作者报告无需姿态标签即可获得有竞争力的姿态精度。
- **适用条件 / 局限** · 依赖足够的视角和特征先验；对称物体存在歧义。

**可复用机制** · 缺标准坐标标签时，先试共享几何瓶颈并显式测对称实例误差。

<a id="paper-152320"></a>

## Emergence of Distortions in High-Dimensional Guided Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152320) · [作者来源](https://openreview.net/forum?id=TxAk7QpMRk)

- **问题 / 瓶颈** · 标准 CFG 可能使采样偏离真实条件分布，降低多样性。
- **核心创新 / 方法** · 用精确分数的混合模型分析类别数与维度的相变，并测试含负引导窗口的调度。
- **Baseline** · 标准 CFG 时间表。
- **Benchmark** · 高维高斯混合理论及真实潜扩散实验。
- **关键结果 / 消融** · 指数类别数下出现扭曲，次指数区间可能消失；新调度报告改善区分与多样性。
- **适用条件 / 局限** · 相变结论受理论分布假设限制。

**可复用机制** · 扫描类别密度和引导时段，同时报告多样性、类别一致性与估计方差。

<a id="paper-152582"></a>

## Emergence of Physical Intelligence via Controllable Information Production

[官方论文页](https://neurips.cc/virtual/2026/poster/152582) · [作者来源](https://openreview.net/forum?id=S15gujrcKN)

- **问题 / 瓶颈** · 预先挑选统计变量的内在动机受设计者偏差影响。
- **核心创新 / 方法** · 从动力系统和最优控制定义信息产生指标，并关联值函数与熵率。
- **Baseline** · 既有内在动机方法，具名对照待核。
- **Benchmark** · 机器人学习基准及人形自主起身。
- **关键结果 / 消融** · 作者报告优于所比方法并解决部分此前未通过任务。
- **适用条件 / 局限** · 信息量估计仍受状态表示及采样影响。

**可复用机制** · 比较探索奖励时，区分可控动力学变化与外生随机变化。

<a id="paper-150542"></a>

## Emergence, Retention and Mitigation of Ill-conditioning due to Basis Lifting in KANs

[官方论文页](https://neurips.cc/virtual/2026/poster/150542) · [作者来源](https://openreview.net/forum?id=hNlDDHSyD6)

- **问题 / 瓶颈** · 固定基提升可压缩特征能量到少量方向，使 SGD 病态。
- **核心创新 / 方法** · 分析提升后经验 Gram 的特征值漂移，引入线性映射前的可学习基坐标变换 T-KAN。
- **Baseline** · B 样条、Chebyshev 和 RBF KAN。
- **Benchmark** · 受控中小规模比较条件数和优化。
- **关键结果 / 消融** · 作者报告常能改善条件与训练，参数开销很小。
- **适用条件 / 局限** · 尚不能从中小模型外推到大规模。

**可复用机制** · 基展开模型训练不稳时扫描 Gram 谱和种子敏感性，再对照基坐标变换。

<a id="paper-151342"></a>

## Emergent Low-Rank Training Dynamics in MLPs with Smooth Activations

[官方论文页](https://neurips.cc/virtual/2026/poster/151342) · [作者来源](https://openreview.net/forum?id=bFu308g2iB)

- **问题 / 瓶颈** · 非线性网络低秩更新缺少理论解释
- **核心创新 / 方法** · 刻画平滑两层 MLP 的梯度下降不变子空间
- **Baseline** · 全参数 MLP
- **Benchmark** · 分类任务及扩展结构验证
- **关键结果 / 消融** · 恰当初始化后性能接近全参数
- **适用条件 / 局限** · 严格理论限于所设两层模型

**可复用机制** · 固定参数预算消融子空间初始化

<a id="paper-150105"></a>

## Emergent Misalignment as Data-Mediated Transfer

[官方论文页](https://neurips.cc/virtual/2026/poster/150105) · [作者来源](https://openreview.net/forum?id=kez5eKP7QS)

- **问题 / 瓶颈** · 局部微调风险可能跨任务传播
- **核心创新 / 方法** · 分别审计数据、预训练来源和训练渠道的安全影响
- **Baseline** · 监督微调与不同蒸馏渠道
- **Benchmark** · 跨任务安全行为诊断
- **关键结果 / 消融** · 作者报告安全变化并非均匀传播
- **适用条件 / 局限** · 证据限所测模型和数据

**可复用机制** · 上线前按数据来源和训练阶段分层测安全回归

<a id="paper-152452"></a>

## Emergent representations of graphical structure in mechanistic neural models of causal judgment

[官方论文页](https://neurips.cc/virtual/2026/poster/152452) · [作者来源](https://openreview.net/forum?id=T1VpyAm5Or)

- **问题 / 瓶颈** · 规范模型难解释实现机制
- **核心创新 / 方法** · 训练循环网络回答关系查询，再用动力学分析内部状态
- **Baseline** · 查询变量和非查询变量对照
- **Benchmark** · 随机观测下的因果关系判断
- **关键结果 / 消融** · 模型利用非查询变量并隐式编码全图
- **适用条件 / 局限** · 网络机制不是脑实验证据

**可复用机制** · 用局部任务监督并探查内部是否学习全局结构

<a id="paper-152210"></a>

## Emergent Semantic Role Understanding in Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152210) · [作者来源](https://openreview.net/forum?id=UlPkTaWvWX)

- **问题 / 瓶颈** · 角色能力究竟来自预训练还是适配未明
- **核心创新 / 方法** · 用线性探针提取冻结解码器表征中的语义角色
- **Baseline** · 任务微调模型
- **Benchmark** · 跨模型规模的语义角色预测
- **关键结果 / 消融** · 冻结表征含大量信息但弱于微调，表示随规模更分散
- **适用条件 / 局限** · 线性可解码不等于因果使用

**可复用机制** · 并报探针和微调性能，区分表示存在与任务可用性

<a id="paper-153218"></a>

## Emergent Visual Thinking in Text-Only Reasoning through Multimodal Training

[官方论文页](https://neurips.cc/virtual/2026/poster/153218) · [作者来源](https://openreview.net/forum?id=Mvqk8cd5uy)

- **问题 / 瓶颈** · 文本推理中的空间表征未必实际参与决策
- **核心创新 / 方法** · 对匹配骨干做隐藏空间方向消融并对比空间与符号任务
- **Baseline** · 匹配文本骨干及跨家族控制
- **Benchmark** · 六家族十配置，BBH navigate 和 boolean expressions
- **关键结果 / 消融** · Chameleon-7B 对应变化为下降27.6和提高5.2个百分点
- **适用条件 / 局限** · 效果依赖模型架构、层与任务

**可复用机制** · 在目标能力及反向对照任务同时测干预效果

<a id="paper-149935"></a>

## EM-NeSy: Expectation Maximization for Neurosymbolic Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149935) · [作者来源](https://openreview.net/forum?id=m5H4yh6pI7)

- **问题 / 瓶颈** · 端到端梯度限制近似符号推断
- **核心创新 / 方法** · E步求标签条件下符号后验，M步仅更新神经参数
- **Baseline** · 精确推断时恢复标准端到端设定
- **Benchmark** · 可扩展性和计算开销实验，任务名称待核
- **关键结果 / 消融** · 作者报告更易扩展和有效率
- **适用条件 / 局限** · 需要可用的后验推断器

**可复用机制** · 拆开符号推理与可微训练，比较精确和近似后验的成本

<a id="paper-139785"></a>

## EmoPhone: A Multi-Wave Dataset for In-the-Wild Mobile and Wearable Affect Sensing

[官方论文页](https://neurips.cc/virtual/2026/poster/139785) · [作者来源](https://openreview.net/forum?id=4xXw8qgOwz)

- **问题 / 瓶颈** · 单一划分难识别具体泛化瓶颈
- **核心创新 / 方法** · 统一核心标签下构造三种数据划分
- **Baseline** · 监督学习、无监督域适配和域泛化
- **Benchmark** · EmoPhone 三波手机与穿戴数据
- **关键结果 / 消融** · 三种划分分别由三类方法领先，域泛化优势较小
- **适用条件 / 局限** · 波次变化和人群差异难完全分离

**可复用机制** · 为部署情境分别设计时间、用户和波次隔离

<a id="paper-151720"></a>

## EMO: Pretraining Mixture of Experts for Emergent Modularity

[官方论文页](https://neurips.cc/virtual/2026/poster/151720) · [作者来源](https://openreview.net/forum?id=YavQQZ3cUM)

- **问题 / 瓶颈** · 常规MoE裁掉多数专家时性能崩溃
- **核心创新 / 方法** · 同一文档的 token 从共享子池选择专家，文档间可选不同池
- **Baseline** · 标准MoE与完整模型
- **Benchmark** · 一万亿 token 预训练及专家保留率对照
- **关键结果 / 消融** · 保留25%和12.5%专家时分别仅降约1和3个百分点
- **适用条件 / 局限** · 依赖文档内领域一致性

**可复用机制** · 面向可裁剪部署时从训练起约束路由，并扫保留比例

<a id="paper-150276"></a>

## Emotion-Trained Vision Models Do Not Necessarily Learn EEG-Aligned Facial Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/150276) · [作者来源](https://openreview.net/forum?id=jMlzffZ5UW)

- **问题 / 瓶颈** · 任务准确率不保证模拟动态脑表征
- **核心创新 / 方法** · 比较训练与随机模型特征几何和时间分辨 EEG
- **Baseline** · 六种视觉模型及同架构随机初始化
- **Benchmark** · 25人观看一秒动态表情视频
- **关键结果 / 消融** · 部分视频模型训练后恐惧相关对齐反而更弱
- **适用条件 / 局限** · 观察性证据，样本和刺激范围有限

**可复用机制** · 脑对齐评测需匹配结构并检验像素与身份混杂

<a id="paper-152590"></a>

## EmoTrack: Robust Depression Tracking from Counseling Transcripts across Session Regimes

[官方论文页](https://neurips.cc/virtual/2026/poster/152590) · [作者来源](https://openreview.net/forum?id=RxhWFgA7GC)

- **问题 / 瓶颈** · 全局提示难区分跨会话连续性与当前披露
- **核心创新 / 方法** · 组合提取信号与冻结轮级嵌入，可加入紧凑会话记忆
- **Baseline** · 单轮及纵向预测基线
- **Benchmark** · LongCounsel-8、DAIC-WOZ 的 PHQ-8 预测
- **关键结果 / 消融** · 单轮最强基线之上 MAE 相对降低13.5%，纵向表现可比
- **适用条件 / 局限** · 属于数据集预测实验，临床外推待验证

**可复用机制** · 将当前内容与历史信息分开，并对照仅当前轮输入

<a id="paper-155140"></a>

## EmpathyChat: Structured Cognitive Reasoning in Empathetic Spoken Dialogue

[官方论文页](https://neurips.cc/virtual/2026/poster/155140) · [作者来源](https://openreview.net/forum?id=83C9MlXWbY)

- **问题 / 瓶颈** · 感知错误会传到推断与回复
- **核心创新 / 方法** · 用声学锚定注意力加强输入对齐，并分阶段分配奖励信用
- **Baseline** · 既有语音对话模型，具名对照待核
- **Benchmark** · EmpathySet-400K与专家标注 EmpathyEval
- **关键结果 / 消融** · 作者报告感知、推断和应答均改善
- **适用条件 / 局限** · 各组件独立贡献待核

**可复用机制** · 多阶段对话分别测输入理解、推断与最终输出

<a id="paper-151539"></a>

## Empirical Bayes Flow Matching for Continuous Cryo-EM Heterogeneity

[官方论文页](https://neurips.cc/virtual/2026/poster/151539) · [作者来源](https://openreview.net/forum?id=Zuq1PmOuVS)

- **问题 / 瓶颈** · 干净潜变量训练样本不可得
- **核心创新 / 方法** · 在经验贝叶斯 EM 中近似后验采样，再用稳定化隐状态更新流模型
- **Baseline** · 需要干净预训练数据的方案为背景，具名对照待核
- **Benchmark** · 双月与 MNIST 受控逆问题
- **关键结果 / 消融** · 作者报告从间接观测学习先验可行
- **适用条件 / 局限** · 依赖已知前向算子与后验近似质量

**可复用机制** · 用持续的隐状态估计减少迭代学习先验的抖动

<a id="paper-152794"></a>

## Empirical Bayes Rebiasing

[官方论文页](https://neurips.cc/virtual/2026/poster/152794) · [作者来源](https://openreview.net/forum?id=QIqata1493)

- **问题 / 瓶颈** · 全量去偏会放大方差
- **核心创新 / 方法** · 非参数极大似然估计偏差分布，再据此回引部分偏差
- **Baseline** · 直接扣除偏差估计
- **Benchmark** · 预测驱动推断及语言模型成对胜率评估
- **关键结果 / 消融** · 作者给出覆盖收敛率并报告精度改善
- **适用条件 / 局限** · 需要大量可联合分析的估计, 具体覆盖条件待核

**可复用机制** · 比较去偏与部分校正，联合报告覆盖和区间长度

<a id="paper-150340"></a>

## Empirical regularities in subjective decision-making by LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/150340) · [作者来源](https://openreview.net/forum?id=ir6D0E35hW)

- **问题 / 瓶颈** · 主观排序混合了多种偏差
- **核心创新 / 方法** · 在受控任务中改变提示与生成、筛选组合
- **Baseline** · 不同提示与阶段设置
- **Benchmark** · 创意生成和主观剪枝实验
- **关键结果 / 消融** · 表面相似提示也会改变偏差显著性，阶段间有交互
- **适用条件 / 局限** · 任务是风格化设置，通用幅度待核

**可复用机制** · 固定候选列表先测筛选偏好，再交叉交换候选来源

<a id="paper-150367"></a>

## Empowering Masked Diffusion Models to Self-Correct with Leave-One-Out Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/150367) · [作者来源](https://openreview.net/forum?id=ic1GS1Kl0Z)

- **问题 / 瓶颈** · 仅遮盖位置学习使监督稀疏且难改已生成 token
- **核心创新 / 方法** · 一次前向为每个位置预测给定其余序列的替代分布
- **Baseline** · 同参数掩码扩散模型及已有重遮盖方案
- **Benchmark** · LM1B困惑度、OpenWebText质量和多样性
- **关键结果 / 消融** · 作者报告困惑度改善，质量多样性曲线在多种预算下更优
- **适用条件 / 局限** · 推理细化依赖额外迭代预算

**可复用机制** · 用无当前位置泄漏的密集监督训练可修订的生成器

<a id="paper-152727"></a>

## Empowering Time Series Analysis with Large-Scale Multimodal Pretraining

[官方论文页](https://neurips.cc/virtual/2026/poster/152727) · [作者来源](https://openreview.net/forum?id=QoM8XcqNiY)

- **问题 / 瓶颈** · 单模态模型缺少互补信息
- **核心创新 / 方法** · 以频域增强编码器融合派生图文、原始序列与新闻，时频解码
- **Baseline** · 单模态时序模型为背景，具名对照待核
- **Benchmark** · MM-TS六领域，零样本预测和异常检测
- **关键结果 / 消融** · 作者报告两个任务均有较强零样本表现
- **适用条件 / 局限** · 新增数据规模与模块增益尚待分离

**可复用机制** · 以同数据量消融派生模态与外部信息

<a id="paper-149410"></a>

## Enabling approximate joint sampling in diffusion LMs

[官方论文页](https://neurips.cc/virtual/2026/poster/149410) · [作者来源](https://openreview.net/forum?id=qFl5qT3qAP)

- **问题 / 瓶颈** · 并行边缘采样损失 token 联合依赖
- **核心创新 / 方法** · 冻结扩散骨干，训练单层采样器模仿逐 token 的联合采样
- **Baseline** · 独立边缘采样、逐 token 联合作参照
- **Benchmark** · Dream与Llada，数学、代码和无条件文本
- **关键结果 / 消融** · 每步解遮八个 token 时相对真实联合分布的 MAUVE 为0.84，边缘基线0.19
- **适用条件 / 局限** · 近似联合误差随解遮数量和任务变化

**可复用机制** · 固定骨干前向次数，比较采样头内迭代与独立并行

<a id="paper-152504"></a>

## Enabling Denoising Score Matching Type Training for Manifold Diffusion Model via Momentum and Splitting

[官方论文页](https://neurips.cc/virtual/2026/poster/152504) · [作者来源](https://openreview.net/forum?id=SebY0YimhJ)

- **问题 / 瓶颈** · 弯曲流形的布朗转移难直接求
- **核心创新 / 方法** · 交替切空间 OU 速度更新和确定性测地传输
- **Baseline** · 隐式得分、热核近似和流匹配路线
- **Benchmark** · 复杂黎曼流形与高维数据，具名任务待核
- **关键结果 / 消融** · 作者报告可进行类似 DSM 的训练并验证有效性
- **适用条件 / 局限** · 需要指数映射接口，局部转移不等于全局闭式

**可复用机制** · 若转移核不可算，可将随机速度与几何传输分离构造监督

<a id="paper-154856"></a>

## Enabling Preference-driven Unlearning in Few-step Distilled Text-to-Image Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154856) · [作者来源](https://openreview.net/forum?id=AMoAi3Al48)

- **问题 / 瓶颈** · 多步噪声预测损失直接迁移到少步模型效果差
- **核心创新 / 方法** · 为少步生成调整偏好优化，使概念移除直接发生在蒸馏模型
- **Baseline** · 标准扩散 DPO 及其遗忘衍生方案
- **Benchmark** · 身份、敏感生成及物体概念移除，检查保留质量
- **关键结果 / 消融** · 作者报告遗忘改善并保留非目标能力
- **适用条件 / 局限** · 具体阈值、具名模型与完整消融待核

**可复用机制** · 遗忘目标应与实际部署的去噪步数匹配，并同时测保留质量

<a id="paper-155216"></a>

## Enabling VLA Action Self-Verification via VLM Token Probability Bucketing

[官方论文页](https://neurips.cc/virtual/2026/poster/155216) · [作者来源](https://openreview.net/forum?id=7Pyltnw11B)

- **问题 / 瓶颈** · 外置验证器增加成本
- **核心创新 / 方法** · 将动作块离散成桶，用流匹配和桶概率联合训练；推理批量评分并复用前缀缓存
- **Baseline** · 同检查点单样本及等预算外部验证器
- **Benchmark** · 多骨干、多套仿真和真机任务，测成功率
- **关键结果 / 消融** · 较单样本仿真、真机、分布外成功率分别提高 2.7、17.1、16.4 个百分点
- **适用条件 / 局限** · 依赖离散粒度与桶得分校准

**可复用机制** · 在固定候选集下比较内置概率与外置评分器，单独测校准和延迟

<a id="paper-150626"></a>

## ENACT: Single-Image Human-Scene Interaction Motion from Language via Foundation-Model Orchestration

[官方论文页](https://neurips.cc/virtual/2026/poster/150626) · [作者来源](https://openreview.net/forum?id=ggS7kWFKgX)

- **问题 / 瓶颈** · 单张图像无法直接提供完整三维场景或连续人体动作
- **核心创新 / 方法** · 以结构化关键帧组织冻结模块，先优化接触姿态再按约束连接关键帧
- **Baseline** · 场景条件、零样本和图像基线，具体名称待核
- **Benchmark** · 标准人体场景交互基准及手机图像，测穿透和足滑
- **关键结果 / 消融** · 作者报告平均和最大穿透及足滑均最低
- **适用条件 / 局限** · 依赖单视角几何与人体姿态恢复精度

**可复用机制** · 将长序列生成拆为接触关键帧推断与约束插值，并分开测两阶段失败

<a id="paper-138889"></a>

## EndoSCOP-V: A Multi-Turn Video Understanding Evaluation Framework for Multimodal Models in Endoscopy Reporting and Clinical Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/138889) · [作者来源](https://openreview.net/forum?id=yeEUbJaub1)

- **问题 / 瓶颈** · 单帧或单任务评测难分辨长视频多轮推理失败来源
- **核心创新 / 方法** · 将结构化报告变为多轮问答，逐轮注入金答案，以医生标注关键帧隔离时间定位
- **Baseline** · 15 位专科医生及 14 个开放权重模型
- **Benchmark** · 1307 段视频、20275 轮；严格准确率
- **关键结果 / 消融** · 医生审计为 78%，最佳开放模型 59.8%，去掉格式简单项后为 53.4%
- **适用条件 / 局限** · 金答案协议衡量单轮能力，临床部署价值需独立验证

**可复用机制** · 同时报告逐轮金答案与自然滚动表现，再用关键帧条件定位瓶颈

<a id="paper-155390"></a>

## Endowing Your Vision-Language-Action Model with a Predictive Mind

[官方论文页](https://neurips.cc/virtual/2026/poster/155390) · [作者来源](https://openreview.net/forum?id=61rEbqQcpq)

- **问题 / 瓶颈** · 像素重建可能把容量花在与动作无关的外观
- **核心创新 / 方法** · 以执行动作作条件对齐当前与未来中间表示，部署去掉辅助预测组件
- **Baseline** · 原 VLA、像素预测及与骨干弱耦合的预测方案
- **Benchmark** · LIBERO、多骨干和真实操作，考察训练效率与任务表现
- **关键结果 / 消融** · 摘要称 LIBERO 用 1/60 迭代数达到或超过完整训练底座
- **适用条件 / 局限** · 依赖训练中配对未来观察；迭代数不直接等于训练成本

**可复用机制** · 评估未来监督时固定部署结构，比较预测目标是否直接塑造控制所用表示

<a id="paper-153367"></a>

## End-to-End Differentiable Diffusion Conditioning for Physics-Informed Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/153367) · [作者来源](https://openreview.net/forum?id=LtzApP65N7)

- **问题 / 瓶颈** · 固定生成采样难按代理目标继续改进
- **核心创新 / 方法** · 通过确定性去噪链对条件求导，用冻结代理和约束损失更新条件
- **Baseline** · 离线模型优化方法，具名对照待核
- **Benchmark** · 数据中心工作负载调度与四项 Design-Bench 任务
- **关键结果 / 消融** · 作者报告调度结果领先，四任务平均排名最优
- **适用条件 / 局限** · 依赖代理可信度和反传开销，离线优化仍可能利用代理误差

**可复用机制** · 固定生成器与代理，对照静态条件和优化后条件，并检查约束违反

<a id="paper-148468"></a>

## End-to-End Identifiable and Consistent Recurrent Switching Dynamical Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/148468) · [作者来源](https://openreview.net/forum?id=xbOBrgiqzA)

- **问题 / 瓶颈** · 变分近似可能削弱切换状态恢复
- **核心创新 / 方法** · 证明一类递归非线性系统的可辨识性，用流模型和 EM 优化精确似然
- **Baseline** · 基于 VAE 的切换状态估计器
- **Benchmark** · 合成及真实时间序列，评估解耦和预测
- **关键结果 / 消融** · 作者报告潜结构分离与预测更好，数值待核
- **适用条件 / 局限** · 保证依赖定理假设；EM 的规模成本待核

**可复用机制** · 在带真值切换状态的合成任务上分开测状态恢复和预测误差

<a id="paper-155932"></a>

## End-to-End Neural Modeling of EM Response and Design Performance for Free-Form RFIC Passives

[官方论文页](https://neurips.cc/virtual/2026/poster/155932) · [作者来源](https://openreview.net/forum?id=1jB1kt5Wfx)

- **问题 / 瓶颈** · 只传显式电磁量可能丢失电路性能所需信息
- **核心创新 / 方法** · 联训频率条件模拟器与电路条件求解器，用依赖正则分离显式和互补响应
- **Baseline** · 传统电磁仿真
- **Benchmark** · 自由形状无源器件，跨频率和电路条件测 R² 和评估时间
- **关键结果 / 消融** · 21M 参数，几乎所有目标 R² 超过 0.98
- **适用条件 / 局限** · 依赖几何与频率覆盖，跨工艺泛化待核

**可复用机制** · 串联代理模型中比较只传物理量与同时传互补表示的下游误差

<a id="paper-155881"></a>

## End-to-End Training for Unified Tokenization and Latent Denoising

[官方论文页](https://neurips.cc/virtual/2026/poster/155881) · [作者来源](https://openreview.net/forum?id=28rLEQtSjg)

- **问题 / 瓶颈** · 冻结潜空间限制生成目标对分词表示的反馈
- **核心创新 / 方法** · 将完整图像编码和带条件的噪声去噪视为两种潜变量推断，双次前传联合训练
- **Baseline** · 分阶段的潜扩散模型
- **Benchmark** · ImageNet 256×256 图像生成，测 FID
- **关键结果 / 消融** · Base 与 Large 的 FID 为 2.12 和 1.75
- **适用条件 / 局限** · 共享参数的梯度干扰及预算公平性待核

**可复用机制** · 对照共享编码和冻结编码，联合测重建及生成质量

<a id="paper-152552"></a>

## End-to-End Verification of Neuro-symbolic Automata via Contrastive Logit-Gaps

[官方论文页](https://neurips.cc/virtual/2026/poster/152552) · [作者来源](https://openreview.net/forum?id=SHNolnMBUT)

- **问题 / 瓶颈** · 逐层界在递归中爆炸，重叠坐标的 log-sum-exp 差值难收紧
- **核心创新 / 方法** · 拆成不相交坐标的对比 logit 差，并以融合时序算子线性化
- **Baseline** · 递归松弛验证方案
- **Benchmark** · 神经符号自动机序列任务，测证书紧度及耗时
- **关键结果 / 消融** · 长序列仍能保持较紧证书，验证提速最高约 6 倍
- **适用条件 / 局限** · 限范数有界扰动及所测自动机形式

**可复用机制** · 验证复合系统时设计便于做界的表示，再拆分测单步松弛和递归放大

<a id="paper-148678"></a>

## EnerGNN: Learning Optimization-Compatible Energy Functions for Exact Constrained Combinatorial Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/148678) · [作者来源](https://openreview.net/forum?id=vtsBNxxhyQ)

- **问题 / 瓶颈** · 神经预测不能保证部署时新增限制可满足
- **核心创新 / 方法** · 最优性感知对比学习塑造离散能量，推理用 MIP 全量求解或只搜索复杂变量
- **Baseline** · 直接优化及战略分解设置；具名对照待核
- **Benchmark** · 二次背包、组合拍卖和供应链，测原始间隙
- **关键结果 / 消融** · 多数实例间隙低于 1%，可外推至更大实例并注入新约束
- **适用条件 / 局限** · 约束须可表达为 MIP，运行时间受求解难度影响

**可复用机制** · 固定能量权重，将新约束的满足率和解质量分开验证

<a id="paper-153867"></a>

## Energy-Based Operator Learning in Function Space

[官方论文页](https://neurips.cc/virtual/2026/poster/153867) · [作者来源](https://openreview.net/forum?id=I9qAqBoxNx)

- **问题 / 瓶颈** · 确定性算子难表示条件分布
- **核心创新 / 方法** · 定义函数空间能量并以高斯为参考，通过能量梯度迭代生成
- **Baseline** · 预测算子及去噪算子
- **Benchmark** · 一维函数与 Navier–Stokes、Darcy、Burgers，涵盖超分辨与预测
- **关键结果 / 消融** · 作者报告生成效果较强，异常函数呈高能量
- **适用条件 / 局限** · 迭代算力及跨分辨率能量校准待核

**可复用机制** · 把生成能量用作异常分数前，在正常分布偏移上测误报

<a id="paper-154978"></a>

## Energy-Guided Transport for Projection-Free Physics-Informed Flow Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/154978) · [作者来源](https://openreview.net/forum?id=9UPtcUT0hz)

- **问题 / 瓶颈** · 覆盖整个区域的 PDE 投影成本高，且可能打断生成路径
- **核心创新 / 方法** · 将物理残差写成平滑势能，沿积分过程施加耗散引导
- **Baseline** · 精确投影及其他物理约束生成方法
- **Benchmark** · 一维与二维物理系统，含混沌 Navier–Stokes
- **关键结果 / 消融** · 作者报告稳定性与精度权衡改善，较精确投影加速
- **适用条件 / 局限** · 软能量不自动保证严格满足约束

**可复用机制** · 固定求解预算比较连续引导和投影的残差、稳定性与速度

<a id="paper-151795"></a>

## Energy Is All We Need: Beyond FLOPs in Model-Heterogeneous Federated Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151795) · [作者来源](https://openreview.net/forum?id=XyElCGNMrd)

- **问题 / 瓶颈** · FLOPs 无法可靠预测不同客户架构的实际能耗
- **核心创新 / 方法** · 以原型对齐梯度做结构化剪枝，按实测能耗曲线的拐点截断本地训练
- **Baseline** · 分别比较剪枝、调度与联合设置
- **Benchmark** · 异构 GPU 联邦学习，比较真实能耗与准确率
- **关键结果 / 消融** · 摘要报告通过 GPU 功耗监测验证两机制，量化值待核
- **适用条件 / 局限** · 依赖设备实测及原型可比较性

**可复用机制** · 异构系统节能时逐设备测能量，并按实际训练收益而非算量代理调度

<a id="paper-150007"></a>

## Energy-Tweedie: Score meets Score, Energy meets Energy

[官方论文页](https://neurips.cc/virtual/2026/poster/150007) · [作者来源](https://openreview.net/forum?id=lTLzpUqJPJ)

- **问题 / 瓶颈** · 经典 Tweedie 公式局限于高斯扰动的后验均值关系
- **核心创新 / 方法** · 对广义椭圆噪声推导能量评分路径导数与边缘 Stein 分数关系
- **Baseline** · 高斯扰动的经典 Tweedie 关系
- **Benchmark** · 理论覆盖椭圆能量噪声与广义高斯；实证待核
- **关键结果 / 消融** · 给出后验采样估计和噪声参数校准依据
- **适用条件 / 局限** · 需要匹配评分规则和理论所设噪声条件

**可复用机制** · 替换去噪噪声族时重新验证评分目标是否匹配边缘分数

<a id="paper-151095"></a>

## ENGINE: Endogenous Variational MultiScale Optimization for Zeroth-Order LLM Fine-Tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/151095) · [作者来源](https://openreview.net/forum?id=d0rAtRO4pl)

- **问题 / 瓶颈** · 全空间估计方差大，子空间更新遗漏重要方向
- **核心创新 / 方法** · 用多重网格式 V 循环在粗细空间轮换并回注细尺度信息
- **Baseline** · 现有零阶微调方案
- **Benchmark** · 标准语言模型基准，比较准确率、前向次数及峰值内存
- **关键结果 / 消融** · 前向次数最高提速 2.61 倍且不增加峰值内存
- **适用条件 / 局限** · 墙钟时间和高维探针频率的普适性待核

**可复用机制** · 固定前向预算消融高维修正频率，并同时追踪效果和峰值内存

<a id="paper-150845"></a>

## EngramState: Loadable Tool Priors for Efficient Function Calling

[官方论文页](https://neurips.cc/virtual/2026/poster/150845) · [作者来源](https://openreview.net/forum?id=ev5gqvsLa0)

- **问题 / 瓶颈** · 每次推理重复编码工具说明耗费端侧计算
- **核心创新 / 方法** · 离线构造压缩状态，在线用同骨干检索并按反馈路由
- **Baseline** · 文本工具描述检索后重新编码
- **Benchmark** · DroidCall、RWKV-7 1.5B 与 Galaxy S25 Ultra，测准确率及首 token 时延
- **关键结果 / 消融** · Top-4 提示由 985 token 降至 22，检索存储 8.24 MiB
- **适用条件 / 局限** · 依赖支持外部状态的骨干和离线缓存可更新性

**可复用机制** · 对说明重复的工具缓存模型状态，单独测调用正确率与缓存维护开销

<a id="paper-148518"></a>

## Enhanced convergence guarantees of score-based generative models in $\mathcal{W}_2$-distance beyond log-concavity

[官方论文页](https://neurips.cc/virtual/2026/poster/148518) · [作者来源](https://openreview.net/forum?id=xIp1jU9Y4y)

- **问题 / 瓶颈** · 既有采样复杂度随维数和误差目标增长较快
- **核心创新 / 方法** · 建立 Euler–Maruyama 和 Poisson midpoint 的误差分析框架
- **Baseline** · 已有 Euler–Maruyama 迭代复杂度界
- **Benchmark** · 理论以 W₂ 距离刻画目标误差
- **关键结果 / 消融** · 上界分别为忽略对数因子的 √d/ε 和 √d/ε^(2/3)
- **适用条件 / 局限** · 保证依赖文中非对数凹条件，迭代数并非墙钟时间

**可复用机制** · 择取采样离散格式前核对理论假设，并对齐每步代价比较误差

<a id="paper-152178"></a>

## Enhancing Agentic Code Localization with Traceability Recovered from Repository Evolution

[官方论文页](https://neurips.cc/virtual/2026/poster/152178) · [作者来源](https://openreview.net/forum?id=UyyXZoIZmv)

- **问题 / 瓶颈** · 静态快照可能丢失历史修改原因
- **核心创新 / 方法** · 离线从历史 PR 提取提示与架构理由，在线双路检索并校验版本
- **Baseline** · 五种代码定位智能体
- **Benchmark** · SWE-bench Lite 与 Verified，文件、模块及函数 Acc@1 与成本
- **关键结果 / 消融** · 作者报告各层级平均提高约 11% 至 13%，token 用量下降 29.2%
- **适用条件 / 局限** · 依赖有代表性的复审记录与版本匹配

**可复用机制** · 在授权维护任务中比较仅检索当前源码和加历史 PR 的定位准确率

<a id="paper-155158"></a>

## Enhancing Gaze Reasoning in Vision Foundation Models for Gaze Following

[官方论文页](https://neurips.cc/virtual/2026/poster/155158) · [作者来源](https://openreview.net/forum?id=7qK9e9Gt6l)

- **问题 / 瓶颈** · 显著物体可能替代真实视线推断
- **核心创新 / 方法** · 头部条件局部 LoRA 与视锥外惩罚保留场景表征并强化头部线索
- **Baseline** · 视觉基础模型视线跟随方法
- **Benchmark** · GazeFollow、VAT，含低显著性目标
- **关键结果 / 消融** · 摘要报告低显著性条件改善尤大
- **适用条件 / 局限** · 增益幅度待核

**可复用机制** · 把显著物体与视线方向分开控制，检查适配是否利用真正线索

<a id="paper-154613"></a>

## Enhancing LLMs with Cognitive-Affective Personality Inference for Simulating Human Social-Psychological Behavior

[官方论文页](https://neurips.cc/virtual/2026/poster/154613) · [作者来源](https://openreview.net/forum?id=CHeF30DtLG)

- **问题 / 瓶颈** · 静态角色提示混合人格和情境解释
- **核心创新 / 方法** · 三次零样本调用分别构建任务盲人格、情境状态及决策
- **Baseline** · 空白、人口属性、叙事及思维链提示
- **Benchmark** · 两类重建社会心理研究、四个骨干
- **关键结果 / 消融** · 整体对齐较强，消融支持前两阶段
- **适用条件 / 局限** · 重建研究的拟合无法证明心理机制

**可复用机制** · 用独立消融检验共享角色与逐场景状态各自收益

<a id="paper-152331"></a>

## Enhancing Novel View Synthesis via Geometry Grounded Set Diffusion

[官方论文页](https://neurips.cc/virtual/2026/poster/152331) · [作者来源](https://openreview.net/forum?id=Tsa68eSMjP)

- **问题 / 瓶颈** · 单视图细化容易产生视图不一致
- **核心创新 / 方法** · 对高斯泼溅渲染用坐标图、相机射线与集合注意力联合去噪
- **Baseline** · 扩散新视图合成对照，名称待核
- **Benchmark** · EUVS、Para-Lane、nuScenes、DL3DV
- **关键结果 / 消融** · 摘要报告感知质量、结构相似度和外推鲁棒性提升
- **适用条件 / 局限** · 依赖相机位姿与初始几何

**可复用机制** · 对视图集合同时做几何条件化，按外推幅度分层测试

<a id="paper-154532"></a>

## Enhancing Speech Large Language Models through Reinforced Behavior Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/154532) · [作者来源](https://openreview.net/forum?id=CtJ6YRQRlm)

- **问题 / 瓶颈** · 同义指令因口音、噪声和口吃产生不同响应
- **核心创新 / 方法** · 对同义多声学视图用语义、正确性、一致性和推理奖励做组相对更新
- **Baseline** · 近期语音语言模型
- **Benchmark** · 语音问答、翻译、推理及不流畅鲁棒性
- **关键结果 / 消融** · 推理密集和声学扰动提示获益最大，幅度待核
- **适用条件 / 局限** · 等义分组的可靠性影响监督

**可复用机制** · 将声学变化与语义变化分开，比较奖励前后的行为一致性

<a id="paper-149526"></a>

## Enhancing Tabular Learners with Context-Aware Semantic Embeddings

[官方论文页](https://neurips.cc/virtual/2026/poster/149526) · [作者来源](https://openreview.net/forum?id=pV2wVDrTqK)

- **问题 / 瓶颈** · 孤立编码忽略列名与条目的数据集含义
- **核心创新 / 方法** · 以代表行预填表格语言模型的 KV 缓存，再生成逐行语境嵌入
- **Baseline** · 孤立行嵌入及近期表格上下文学习器
- **Benchmark** · CARTE、TextTab、TabArena
- **关键结果 / 消融** · 语义丰富和低数据场景改善明显
- **适用条件 / 局限** · 代表行选择与训练测试隔离须核实

**可复用机制** · 固定表格预测器，分别测试无语境与训练集代表行语境

<a id="paper-149322"></a>

## Ensemble Distributionally Robust Bayesian Optimisation

[官方论文页](https://neurips.cc/virtual/2026/poster/149322) · [作者来源](https://openreview.net/forum?id=qzmJlrajPM)

- **问题 / 瓶颈** · 单一代理易受模型错设影响
- **核心创新 / 方法** · 以集成代理处理上下文分布鲁棒的零阶贝叶斯优化
- **Baseline** · 已有分布鲁棒贝叶斯优化，具体名称待核
- **Benchmark** · 理论遗憾界与实证，基准待核
- **关键结果 / 消融** · 给出次线性遗憾界，报告实证符合理论
- **适用条件 / 局限** · 适用假设和复杂度待正文核实

**可复用机制** · 选代理时同时评估一般遗憾与上下文偏移下表现

<a id="paper-149487"></a>

## Ensemble Modeling for Time Series Forecasting: an Adaptive Robust Optimization Approach

[官方论文页](https://neurips.cc/virtual/2026/poster/149487) · [作者来源](https://openreview.net/forum?id=pnLT9fn4nN)

- **问题 / 瓶颈** · 静态组合难适应环境变化
- **核心创新 / 方法** · 用自适应鲁棒优化构造时变线性集成
- **Baseline** · 事后最佳成员及竞争性集成方法
- **Benchmark** · 合成实验、空气污染、能耗和气旋强度
- **关键结果 / 消融** · 较事后最佳成员 RMSE 降16–26%，CVaR 降14–28%
- **适用条件 / 局限** · 权重可用信息及切分细节待核

**可复用机制** · 在同一滚动评测中比较时变权重、静态权重和尾部风险

<a id="paper-152721"></a>

## Ensemble Selective Classification

[官方论文页](https://neurips.cc/virtual/2026/poster/152721) · [作者来源](https://openreview.net/forum?id=Qqq3JkX68b)

- **问题 / 瓶颈** · 固定模型下单一分数难跨域稳定
- **核心创新 / 方法** · 用可微软排序近似 AURC 训练正确性选择器
- **Baseline** · 单一分数、hinge 和 SELE
- **Benchmark** · 15 项视觉与 NLP 分类另含 LLM 选择题
- **关键结果 / 消融** · 组合在分布偏移下常优于最佳单分数
- **适用条件 / 局限** · 需要部署分布少量真标签

**可复用机制** · 模型冻结时，在部署校准集直接优化风险覆盖排序

<a id="paper-148212"></a>

## Ensembling Language Models with Sequential Monte Carlo

[官方论文页](https://neurips.cc/virtual/2026/poster/148212) · [作者来源](https://openreview.net/forum?id=zWigIoVsHo)

- **问题 / 瓶颈** · 逐 token 平均难定义跨词表序列分布
- **核心创新 / 方法** · 将字符串级集成写为推断，用字符空间序列蒙特卡洛采样
- **Baseline** · 概率平均和乘积等聚合策略
- **Benchmark** · 多模型多提示文本生成
- **关键结果 / 消融** · 乘积等共识策略优于概率平均
- **适用条件 / 局限** · 有限粒子时仍有近似偏差和开销

**可复用机制** · 比较集成方式时固定推断预算并报告样本近似质量

<a id="paper-150792"></a>

## Ensuring Deployment-Time Safety of Neural Network Controlled Systems via Localized Certificate Repair

[官方论文页](https://neurips.cc/virtual/2026/poster/150792) · [作者来源](https://openreview.net/forum?id=fMUyPAggFz)

- **问题 / 瓶颈** · 新增障碍使原证书失效
- **核心创新 / 方法** · 保留未变区域，逐级从局部证书修复切换至策略联合更新与局部重训
- **Baseline** · 从头重训
- **Benchmark** · 四个基准、五个新增障碍
- **关键结果 / 消融** · 双方成功实例平均快17.3倍，策略性能下降16.2%
- **适用条件 / 局限** · 保证依赖系统模型和证书验证

**可复用机制** · 对变化区域做局部修复，再按验证失败决定升级范围

<a id="paper-139577"></a>

## EnterpriseBench: Evaluating LLM Agents on End-to-End Spreadsheet Tasks in Finance

[官方论文页](https://neurips.cc/virtual/2026/poster/139577) · [作者来源](https://openreview.net/forum?id=HI4PcfnlXQ)

- **问题 / 瓶颈** · 单格问答忽略整表修改与审阅质量
- **核心创新 / 方法** · 以专业标准构造准确性、公式、格式三轴评估
- **Baseline** · 前沿表格 Agent 家族，Claude 表现领先
- **Benchmark** · 金融建模与情景分析的完整表格任务
- **关键结果 / 消融** · 计算链变深时，强模型也明显退化
- **适用条件 / 局限** · 行业标准和模型版本影响排序

**可复用机制** · 评测产物代理时分开测可编辑结构和计算正确性

<a id="paper-151144"></a>

## EntiRE: Invariant Learning for Robust Concept Erasure in Text-to-Image Generative Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151144) · [作者来源](https://openreview.net/forum?id=ch8Vn8e6ZM)

- **问题 / 瓶颈** · 平均遗忘效果掩盖局部残留
- **核心创新 / 方法** · 以不变学习和总变差约束使提示空间的遗忘更均匀
- **Baseline** · 概念擦除基线
- **Benchmark** · 风格、对象及敏感概念擦除的防御比较
- **关键结果 / 消融** · 摘要报告鲁棒性与通用能力保留改善
- **适用条件 / 局限** · 需要同时校验正常概念误删

**可复用机制** · 将擦除验收拆为残留分布和无关能力回归测试

<a id="paper-153267"></a>

## EntityBench: Towards Entity-Consistent Long-Range Multi-Shot Video Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/153267) · [作者来源](https://openreview.net/forum?id=MXMtuuTopS)

- **问题 / 瓶颈** · 单镜头质量无法解释跨镜头身份漂移
- **核心创新 / 方法** · 标注角色、对象和地点调度，分开衡量画质、指令与一致性
- **Baseline** · 现有多镜头方法和显式实体记忆
- **Benchmark** · 140段2491镜头，最多相隔48镜头
- **关键结果 / 消融** · 一致性随间隔下降，实体记忆角色保真效应量2.33
- **适用条件 / 局限** · 评判器和叙事素材范围影响稳定性

**可复用机制** · 按重现间隔分桶，检验实体记忆是否减少漂移

<a id="paper-152767"></a>

## EntropyCache: Decoded Token Entropy Guided KV Caching for Diffusion Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152767) · [作者来源](https://openreview.net/forum?id=QX9lXOB8FY)

- **问题 / 瓶颈** · 扩散模型双向注意力使缓存迅速过期
- **核心创新 / 方法** · 以最大熵代理缓存漂移，同时刷新近期解码 token
- **Baseline** · 无缓存基础解码及近似缓存
- **Benchmark** · LLaDA-8B-Instruct、Dream-7B-Instruct
- **关键结果 / 消融** · 标准基准15.2–26.4倍加速，判断开销约0.5%
- **适用条件 / 局限** · 相对于原始基线的倍率不等于所有缓存方案

**可复用机制** · 固定精度下测刷新代理与真实缓存漂移相关性

<a id="paper-148328"></a>

## Entropy Distribution as a Fingerprint for Hallucinations in Generative Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148328) · [作者来源](https://openreview.net/forum?id=yeXKhJ9iy3)

- **问题 / 瓶颈** · 平均熵会丢掉少数高不确定 token
- **核心创新 / 方法** · 参考分布校准均值与最大熵，单次前向评分
- **Baseline** · 单次黑箱检测与多样本检测
- **Benchmark** · 八个问答基准、十个模型
- **关键结果 / 消融** · 摘要报告领先单次黑箱方法，且与多样本方法统计上相近
- **适用条件 / 局限** · 需要 token logits 和可迁移参考分布

**可复用机制** · 按生成长度校准熵尾部，再测误报与检出率

<a id="paper-149956"></a>

## Entropy Dynamics of Agent Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149956) · [作者来源](https://openreview.net/forum?id=lvlmhvccQi)

- **问题 / 瓶颈** · 单轮训练经验难解释轨迹熵周期
- **核心创新 / 方法** · 分解熵周期，以表示分离损失区分正确与错误轨迹
- **Baseline** · 不同骨干与强化学习算法，具名待核
- **Benchmark** · 多项工具任务，测熵及下游表现
- **关键结果 / 消融** · 重复和幻觉可跨周期积累，辅助损失报告改善
- **适用条件 / 局限** · 轨迹标签质量和因果解释待核

**可复用机制** · 把诊断粒度从单 token 扩至回合，记录熵趋势和可验证错误

<a id="paper-152175"></a>

## Entropy-Gated Latent Recursion

[官方论文页](https://neurips.cc/virtual/2026/poster/152175) · [作者来源](https://openreview.net/forum?id=UznQDehNbu)

- **问题 / 瓶颈** · 只靠 token 采样会限制候选多样性
- **核心创新 / 方法** · 高熵位置重用顶部不同层跨度至分布收敛或限步
- **Baseline** · 仅温度、仅层跨度与联合方案
- **Benchmark** · 八个模型、六个数学基准
- **关键结果 / 消融** · MATH-500联合候选 oracle 91.6%，仅温度83.4%
- **适用条件 / 局限** · oracle 不等于可部署选择器表现

**可复用机制** · 固定推断预算下比较采样温度和递归跨度的候选互补性

<a id="paper-152779"></a>

## Entropy Guided Dynamic Patch Segmentation for Time Series Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/152779) · [作者来源](https://openreview.net/forum?id=QPKvNhibb1)

- **问题 / 瓶颈** · 固定窗口会把自然转折分到不同块
- **核心创新 / 方法** · 按条件熵检测边界，再池化与交叉注意力编码为定长表示
- **Baseline** · 固定长度时间序列分块
- **Benchmark** · 长时预测、分类及异常检测
- **关键结果 / 消融** · 摘要报告准确度和效率同时改善
- **适用条件 / 局限** · 熵估计、噪声及运行开销细项待核

**可复用机制** · 保持编码器相同，比较规则分块与转折感知分块

<a id="paper-149828"></a>

## Entropy Minimization without Model Collapse: Mitigating Prediction Bias in Medical Imaging

[官方论文页](https://neurips.cc/virtual/2026/poster/149828) · [作者来源](https://openreview.net/forum?id=n0LfI4MJNe)

- **问题 / 瓶颈** · 分布偏移合并类簇，熵最小化会强化预测偏置
- **核心创新 / 方法** · 在测试时均衡各预测类对无监督熵目标的贡献
- **Baseline** · 常规熵最小化等测试时适配方法
- **Benchmark** · 四个医学影像数据集及 ImageNet-C
- **关键结果 / 消融** · 作者报告防止塌缩且表现可比或更好
- **适用条件 / 局限** · 真实标签比例偏斜时需单测

**可复用机制** · 同时监测类别覆盖和预测准确度

<a id="paper-152571"></a>

## Entropy Polarity in Reinforcement Fine-Tuning:  Direction, Asymmetry, and Control

[官方论文页](https://neurips.cc/virtual/2026/poster/152571) · [作者来源](https://openreview.net/forum?id=S8HaL0jX6J)

- **问题 / 瓶颈** · 全局熵指标掩盖单次更新方向
- **核心创新 / 方法** · 一阶近似预测扩熵或缩熵，并按熵轨迹调节两类更新
- **Baseline** · 竞争性 RLVR 方法
- **Benchmark** · 数学推理和 agent 基准
- **关键结果 / 消融** · 作者报告奖励及训练效率改善
- **适用条件 / 局限** · 一阶近似在大更新下待核

**可复用机制** · 分别消融扩熵和缩熵分支

<a id="paper-139835"></a>

## EnvFaultBench: Benchmarking LLM Agents on Software Environment-Fault Troubleshooting

[官方论文页](https://neurips.cc/virtual/2026/poster/139835) · [作者来源](https://openreview.net/forum?id=1tS0rcwXBg)

- **问题 / 瓶颈** · 源码修复基准遗漏依赖及配置故障
- **核心创新 / 方法** · 容器内复现环境问题，以隐含功能测试验收任意有效修复
- **Baseline** · 统一框架的十个模型及零样本对照
- **Benchmark** · 75 个项目、348 个实例，覆盖三种生态
- **关键结果 / 消融** · 最优解决率 65.8%，零样本为 10.9%
- **适用条件 / 局限** · 容器任务与实际运维有差别

**可复用机制** · 在授权维修评测中同时记录验收成功率和首次修复步数

<a id="paper-151010"></a>

## Environment-Robust Representation Learning with Empirical Bayes

[官方论文页](https://neurips.cc/virtual/2026/poster/151010) · [作者来源](https://openreview.net/forum?id=dcFIgr2nN2)

- **问题 / 瓶颈** · 潜变量分布变化使观测预测失稳
- **核心创新 / 方法** · 经验贝叶斯设先验，变分目标含分环境项和平衡项
- **Baseline** · 已有跨域预测方法
- **Benchmark** · 模拟与天体源识别等
- **关键结果 / 消融** · 作者报告未见环境预测改善
- **适用条件 / 局限** · 假设条件生成机制跨环境稳定

**可复用机制** · 在环境划分中单测机制稳定假设

<a id="paper-153039"></a>

## EO-WM: A Physically Informed World Model for Probabilistic Earth Observation Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/153039) · [作者来源](https://openreview.net/forum?id=OUSDMTfzLA)

- **问题 / 瓶颈** · 天气变量合并输入难评估变化响应
- **核心创新 / 方法** · 以不同条件路径为视频扩散提供基线、异常和累计作用
- **Baseline** · 确定性模型和常规条件扩散
- **Benchmark** · 极端夏季及季节配对诊断，测 NDVI
- **关键结果 / 消融** · 降幅预测误差相对减 5.63%，方向命中相对增 7.80%
- **适用条件 / 局限** · 依赖天气条件及遥感覆盖

**可复用机制** · 除像素指标外做匹配条件下响应测试

<a id="paper-148198"></a>

## EP-Flow: Disordered Crystal Structure Prediction without Site-level Annotation

[官方论文页](https://neurips.cc/virtual/2026/poster/148198) · [作者来源](https://openreview.net/forum?id=zc9Yuz8txr)

- **问题 / 瓶颈** · 化学式给定但无位点标注
- **核心创新 / 方法** · 在共享中心化空间学习保边缘量流，并映射回可行占据
- **Baseline** · 适配的有序晶体生成器
- **Benchmark** · 基于 COD、MPDS 的无序晶体预测
- **关键结果 / 消融** · 作者报告整体表现和局部无序结构改善
- **适用条件 / 局限** · 依赖配方与位点约束

**可复用机制** · 用可行域参数化代替事后检查边缘约束

<a id="paper-152068"></a>

## EPIC: Efficient Predicate-Guided Inference-Time Control for Compositional Text-to-Image Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/152068) · [作者来源](https://openreview.net/forum?id=ViGYqNSZKu)

- **问题 / 瓶颈** · 组合描述中不同失败类型需要不同修复
- **核心创新 / 方法** · 预先生成固定视觉谓词程序，再逐轮验证并路由
- **Baseline** · 单次生成与已有精修方法
- **Benchmark** · GenEval2，提示级准确率和成本
- **关键结果 / 消融** · 34.16% 至 71.46%，同预算较强对照高 19.23 点
- **适用条件 / 局限** · 依赖视觉验证的可靠性

**可复用机制** · 固定预算比较局部修复与全局重采样

<a id="paper-150907"></a>

## EpicWorldModel: Exploration-driven Planning with Latent World Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150907) · [作者来源](https://openreview.net/forum?id=eX8xQG15Hs)

- **问题 / 瓶颈** · 遮挡产生多种可能未来，确定性预测会混合它们
- **核心创新 / 方法** · 联合学习表示与流预测，以方差指导 CEM
- **Baseline** · LeWorldModel 等
- **Benchmark** · 部分可观测环境中的潜空间规划
- **关键结果 / 消融** · 报告成功率最多提升 22%
- **适用条件 / 局限** · 方差只是信息增益代理

**可复用机制** · 按遮挡程度比较确定预测与不确定性探索

<a id="paper-155163"></a>

## Epigenomics-Guided Flow Matching for 3D Genome Super-Resolution

[官方论文页](https://neurips.cc/virtual/2026/poster/155163) · [作者来源](https://openreview.net/forum?id=7oTMtNxW5H)

- **问题 / 瓶颈** · 纯局部切片可能破坏距离结构
- **核心创新 / 方法** · 用位置相关条件及结构先验约束观测矩阵重建
- **Baseline** · 原始观测与超分方法
- **Benchmark** · 留出条件下的观测结构恢复
- **关键结果 / 消融** · 作者报告留出条件表现改善
- **适用条件 / 局限** · 仅观测数据重建

**可复用机制** · 矩阵超分时对照局部误差与全局结构的保留

<a id="paper-153200"></a>

## EpiPivot: Learning to Control the Simplex Method under Epistemic Uncertainty

[官方论文页](https://neurips.cc/virtual/2026/poster/153200) · [作者来源](https://openreview.net/forum?id=N65zIjBufL)

- **问题 / 瓶颈** · 规则耗时依赖优化轨迹
- **核心创新 / 方法** · 用时序注意力和共享潜样本估计不确定性，再作 Thompson 选择
- **Baseline** · 经典与学习式规则
- **Benchmark** · 大规模线性规划，测枢轴成本
- **关键结果 / 消融** · 较最佳经典规则最多降 79%
- **适用条件 / 局限** · 估计器开销和分布变化待核

**可复用机制** · 同时记录收敛率和规则选择开销

<a id="paper-153698"></a>

## Epiplexity Guided Data Selection and Generation for Out-of-Distribution Generalization

[官方论文页](https://neurips.cc/virtual/2026/poster/153698) · [作者来源](https://openreview.net/forum?id=JRQ16ZxTmz)

- **问题 / 瓶颈** · 数据质量静态排序未考虑训练阶段
- **核心创新 / 方法** · 用损失曲线拟合边际结构增益，据此分配采样
- **Baseline** · 静态采样对照待核
- **Benchmark** · 零样本和微调迁移任务
- **关键结果 / 消融** · 作者报告结构增益与迁移表现正相关
- **适用条件 / 局限** · 依赖计算预算和损失拟合

**可复用机制** · 在同算力下比较静态配比和边际增益配比

<a id="paper-155281"></a>

## Epistemic Pairwise Maximin Share

[官方论文页](https://neurips.cc/virtual/2026/poster/155281) · [作者来源](https://openreview.net/forum?id=6pVA0fm67W)

- **问题 / 瓶颈** · 已有认识论公平放松方法无法直接迁移
- **核心创新 / 方法** · 定义 EPMMS 并区分可加与双值估值推导保证
- **Baseline** · EFX、PMMS 与 MMS
- **Benchmark** · 不可分物品公平分配的理论设定
- **关键结果 / 消融** · 可加情况下有可计算的 4/5 保证，双值下有更强保证
- **适用条件 / 局限** · 依赖估值结构

**可复用机制** · 在选公平目标前查估值结构能支持的存在与算法保证

<a id="paper-150541"></a>

## Epistemic Social Learning: Latent Behavioral Structure under Endogenous Multi-Agent Interaction

[官方论文页](https://neurips.cc/virtual/2026/poster/150541) · [作者来源](https://openreview.net/forum?id=hNvgA94KTi)

- **问题 / 瓶颈** · 行动改变数据分布，静态聚类无法保证适应
- **核心创新 / 方法** · 快速贝叶斯信念与慢速加权原型更新耦合
- **Baseline** · 重复博弈学习基线，具名待核
- **Benchmark** · 行为切换后测累计遗憾
- **关键结果 / 消融** · 作者报告切换后遗憾降 26%
- **适用条件 / 局限** · 理论对应受控随机过程条件

**可复用机制** · 用切换后遗憾检验交互表征是否指导行动

<a id="paper-153023"></a>

## EpiStream: Utility-Aware Temporal Abstraction for Dense-Action Streams

[官方论文页](https://neurips.cc/virtual/2026/poster/153023) · [作者来源](https://openreview.net/forum?id=OZd2dd0dZ6)

- **问题 / 瓶颈** · 密集动作缺少清晰边界
- **核心创新 / 方法** · 用教师构建提交优势，训练只看前缀的因果策略
- **Baseline** · 分割式流处理
- **Benchmark** · 游戏和运动，含实时建议与意图预测
- **关键结果 / 消融** · 作者报告片段连贯性及下游表现改善
- **适用条件 / 局限** · 依赖效用和记忆预算

**可复用机制** · 固定容量比较边界分割与效用触发提交

<a id="paper-149913"></a>

## Equilibrium Forcing: Adaptive Video Generation Without Noise Conditioning

[官方论文页](https://neurips.cc/virtual/2026/poster/149913) · [作者来源](https://openreview.net/forum?id=mH42nbVley)

- **问题 / 瓶颈** · 静态采样日程难适应视频内容
- **核心创新 / 方法** · 去除噪声等级条件，把采样写成梯度优化
- **Baseline** · 噪声等级条件的自回归视频生成
- **Benchmark** · 视频质量和时序一致性
- **关键结果 / 消融** · 作者报告画质与一致性改善
- **适用条件 / 局限** · 步长稳定性和计算成本待核

**可复用机制** · 按固定算力比较静态与自适应采样

<a id="paper-148529"></a>

## Equilibrium Matching: Generative Modeling with Implicit Energy-Based Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148529) · [作者来源](https://openreview.net/forum?id=xD7V6hlH9d)

- **问题 / 瓶颈** · 时间条件流绑定采样过程
- **核心创新 / 方法** · 学习隐式能量梯度，采样时以可调优化器下降
- **Baseline** · 扩散及流模型
- **Benchmark** · ImageNet 256×256 生成，另有去噪与分布外检测
- **关键结果 / 消融** · FID 1.90
- **适用条件 / 局限** · 计算预算和优化终止条件需核

**可复用机制** · 在同时间预算下比较固定求解器和自适应能量优化

<a id="paper-150437"></a>

## Equivariant Reinforcement Learning for Clifford Quantum Circuit Synthesis

[官方论文页](https://neurips.cc/virtual/2026/poster/150437) · [作者来源](https://openreview.net/forum?id=i2rdzOU15l)

- **问题 / 瓶颈** · 不同电路规模常要分别训练
- **核心创新 / 方法** · 把辛矩阵化为恒等阵的门搜索建模为强化学习，用等变网络与随机游走课程
- **Baseline** · 最优参考、Qiskit Aaronson–Gottesman 和贪心合成
- **Benchmark** · 全连通 Clifford 电路，比较双比特门数和运行时间
- **关键结果 / 消融** · 六比特在秒级预算下有 99.2% 最优，继续训练后泛化至 30 比特
- **适用条件 / 局限** · 限 Clifford 与全连通设定

**可复用机制** · 在小规模精确验证后测试同一等变策略跨规模迁移

<a id="paper-155430"></a>

## Equivariant Spherical Transformer for Efficient Molecular Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/155430) · [作者来源](https://openreview.net/forum?id=5i7KqZASE3)

- **问题 / 瓶颈** · 严格等变算子限制非线性表达
- **核心创新 / 方法** · 在球面傅里叶表示的采样空间应用 Transformer，以均匀采样维持等变归纳偏置
- **Baseline** · 常规等变图网络及更大模型
- **Benchmark** · OC20、MPtrj、QM9，指标待核
- **关键结果 / 消融** · 作者报告三个基准有改善，OC20 上部分小模型超过较大模型
- **适用条件 / 局限** · 采样预算及模块独立开销待核

**可复用机制** · 在几何预测中比较同预算的等变局部算子与球面采样注意力

<a id="paper-152958"></a>

## Ergodic Risk Measures: Towards a Risk-Aware Foundation for Continual Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/152958) · [作者来源](https://openreview.net/forum?id=P7WboKVZGN)

- **问题 / 瓶颈** · 经典风险度量不能直接刻画持续学习中的长期表现
- **核心创新 / 方法** · 提出遍历风险度量并证明其对持续设定的兼容性
- **Baseline** · 经典风险度量及风险中性目标
- **Benchmark** · 持续学习理论与风险感知案例，细节待核
- **关键结果 / 消融** · 作者给出不兼容性结果及兼容扩展
- **适用条件 / 局限** · 结论依赖所定义的持续过程和风险性质

**可复用机制** · 为非静态学习过程选风险指标时检验其与长期性能定义的一致性

<a id="paper-148507"></a>

## Ergodic Trajectory Design by Learned Pushforward Maps: Provable Coverage via Conditional Flow Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/148507) · [作者来源](https://openreview.net/forum?id=xKCytZZNNd)

- **问题 / 瓶颈** · 逐轨迹重优化难以复用
- **核心创新 / 方法** · 以解析环域轨迹提供遍历性，用离线学习的推前映射转到目标密度
- **Baseline** · 时间扭曲、优化和同步流匹配
- **Benchmark** · 合成密度及真实覆盖数据，考察覆盖、能量与约束
- **关键结果 / 消融** · 给出周期数平方根倒数收敛率与误差界，报告较强权衡
- **适用条件 / 局限** · 严格认证需 Lipschitz 界，软惩罚无法保证硬约束

**可复用机制** · 对固定目标密度的环境比较复用映射和逐次重规划的成本

<a id="paper-151365"></a>

## ERIS: Enhancing Privacy and Scalability in Federated Learning via Federated Shard Aggregation

[官方论文页](https://neurips.cc/virtual/2026/poster/151365) · [作者来源](https://openreview.net/forum?id=b7CsCWQwlK)

- **问题 / 瓶颈** · 中心聚合看到完整客户端更新且可能成为瓶颈
- **核心创新 / 方法** · 将互不重叠的更新片段分给多个聚合方，重组结果保留集中式更新
- **Baseline** · FedAvg，另比较有无压缩
- **Benchmark** · 视觉与文本任务，包括大语言模型
- **关键结果 / 消融** · 作者报告相近效用及较低通信瓶颈，并给出信息泄露上界
- **适用条件 / 局限** · 依赖可见范围和聚合方威胁假设

**可复用机制** · 比较分片协作和中心汇聚时同时核对更新等价性与观察者可见比例

<a id="paper-138971"></a>

## ER-Reason: A Benchmark Dataset for LLM Clinical Reasoning in the Emergency Room

[官方论文页](https://neurips.cc/virtual/2026/poster/138971) · [作者来源](https://openreview.net/forum?id=tI6dUEC7KR)

- **问题 / 瓶颈** · 静态考试题难测流程中判断的演进
- **核心创新 / 方法** · 以匿名真实病例构造阶段任务和逐步一致性问题，考查更新方向和幅度
- **Baseline** · 推理型与非推理型模型，传统基准作背景
- **Benchmark** · 25,174 份记录、3,437 名患者、2,555 条专家标注
- **关键结果 / 消融** · 作者报告可发现静态基准难体现的错误
- **适用条件 / 局限** · 为回顾评测，无法代替临床验证

**可复用机制** · 对多阶段专业任务同时测最终判断和证据加入后的变化

<a id="paper-149993"></a>

## Error-Guided Bellman Calibration for Semi-Offline Value Estimation

[官方论文页](https://neurips.cc/virtual/2026/poster/149993) · [作者来源](https://openreview.net/forum?id=lcrYylOS2v)

- **问题 / 瓶颈** · 沿原预测值校准可能漏掉结构化偏差
- **核心创新 / 方法** · 以在策略样本拟合误差模型，然后沿误差轴做 Bellman 校准
- **Baseline** · 经典 Bellman 校准
- **Benchmark** · 合成、CRM、D4RL
- **关键结果 / 消融** · 作者报告改进，并给出细化保证及有限样本界
- **适用条件 / 局限** · 需要少量可信在策略样本，误差模型错设影响收益

**可复用机制** · 与沿预测值校准做同预算比较并分层测偏差

<a id="paper-153788"></a>

## eSAM: Editing SAM3 Attention for Training-Free Referring Segmentation

[官方论文页](https://neurips.cc/virtual/2026/poster/153788) · [作者来源](https://openreview.net/forum?id=If1BheAYFE)

- **问题 / 瓶颈** · SAM 3 起始 token 吸收大量视觉交叉注意力
- **核心创新 / 方法** · 用 CLIPSeg 空间先验将注意力转向相关内容词，并重标定值张量
- **Baseline** · 原始 SAM 3、仅去汇点变体与免训练方法
- **Benchmark** · RefCOCO 系列、Ref-DAVIS17、Ref-YouTube-VOS、MeViS
- **关键结果 / 消融** · 起始 token 平均吸收 54.8%，完整方案在免训练方法中领先
- **适用条件 / 局限** · 依赖空间先验质量及内部注意力访问

**可复用机制** · 用有无重分配的消融检验去汇点是否真正改善局部对齐

<a id="paper-156139"></a>

## Escape the Context Manifold: Preventing DiT In-Context Editing via Conditional Flow Hijacking

[官方论文页](https://neurips.cc/virtual/2026/poster/156139) · [作者来源](https://openreview.net/forum?id=06nMkjyRaB)

- **问题 / 瓶颈** · 只测简单属性编辑难代表复杂提示下的防护效果
- **核心创新 / 方法** · 从条件生成过程设计防护并同时评估身份、质量与提示匹配
- **Baseline** · DeContext 及既有参考图像保护方法
- **Benchmark** · FLUX.1-Kontext，属性和复杂场景编辑
- **关键结果 / 消融** · 作者报告复杂场景防护改善且保留提示匹配
- **适用条件 / 局限** · 模型迁移和编辑分布的具体边界待核

**可复用机制** · 回归测试参考图像保护时覆盖多种编辑复杂度和模型

<a id="paper-154899"></a>

## Escaping Parameter Space: Tight Generalization Bounds via Representation Quality

[官方论文页](https://neurips.cc/virtual/2026/poster/154899) · [作者来源](https://openreview.net/forum?id=A66lKoZWY8)

- **问题 / 瓶颈** · 参数空间复杂度证书可能松弛
- **核心创新 / 方法** · 用末层表示的近邻分类器分解泛化证书
- **Baseline** · 参数空间证书及破坏类几何的诊断对照
- **Benchmark** · CIFAR-10/100 和 ImageNet，使用 ResNet-18 或 DINOv2
- **关键结果 / 消融** · 从头训练的 CIFAR-10 误差界间隙为 8 个百分点，冻结表示也提供非平凡证书
- **适用条件 / 局限** · 依赖可测稳定性及局部类几何

**可复用机制** · 区分训练集记忆与几何泛化，用几何干预和独立测试核对

<a id="paper-151359"></a>

## Escaping Path Mirages in Offline Goal-Conditioned Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151359) · [作者来源](https://openreview.net/forum?id=b9QDpSzHr4)

- **问题 / 瓶颈** · 偶然成功轨迹会让价值估计过度乐观
- **核心创新 / 方法** · 提取高变异节点，以分段学习构建目标条件边
- **Baseline** · 已有离线目标条件强化学习方法
- **Benchmark** · OGBench，长时高随机目标到达
- **关键结果 / 消融** · 作者报告优于先前方法，具体幅度待核
- **适用条件 / 局限** · 依赖离线数据覆盖与分叉识别

**可复用机制** · 评估长时路径时检查高随机转移的分段成功率

<a id="paper-148924"></a>

## Escaping Reasoning Basins: Basin-Aware Search for  Inference-Time  LLM Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/148924) · [作者来源](https://openreview.net/forum?id=uBdT7X4KmA)

- **问题 / 瓶颈** · 相似轨迹反复消耗固定预算
- **核心创新 / 方法** · 按符号或语义聚类识别推理簇并惩罚重复访问
- **Baseline** · 同预算 Tree of Thoughts
- **Benchmark** · Game of 24，测成功与正确错误轨迹的冗余差
- **关键结果 / 消融** · 最高提高 22 个百分点，并观察到正冗余差
- **适用条件 / 局限** · 效果受聚类质量和任务类型影响

**可复用机制** · 在固定预算下比较多样性调度与单纯提高生成数

<a id="paper-150429"></a>

## Escaping the Cognitive Well: Efficient Competition Math with Off-the-Shelf Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150429) · [作者来源](https://openreview.net/forum?id=i6Ojls5BRt)

- **问题 / 瓶颈** · 反复修订与评分可能共同认可错误证明
- **核心创新 / 方法** · 从长解答抽取引理，在新上下文做独立校验
- **Baseline** · 公开数学推理流水线及 DeepThink 对照
- **Benchmark** · IMO-ProofBench Advanced，比较表现与平均费用
- **关键结果 / 消融** · Gemini 3.0 Pro 得 67.1%，约每题 31 美元
- **适用条件 / 局限** · 抽取及验证模型仍可能共享遗漏，费用受服务定价影响

**可复用机制** · 将局部引理验证与整份解答评分分离

<a id="paper-151654"></a>

## Escaping the Curse of Dimensionality in One‑Step Flow-Based Generative Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151654) · [作者来源](https://openreview.net/forum?id=Z20kWigIHe)

- **问题 / 瓶颈** · 多次采样昂贵，单步流的统计保证有限
- **核心创新 / 方法** · 分析高斯噪声扰动低维曲面的分布并导出近似与泛化界
- **Baseline** · 受环境维度或非实用损失限制的既有理论
- **Benchmark** · 低维曲面加高斯噪声的理论设定
- **关键结果 / 消融** · 作者给出规避维数灾难的误差界
- **适用条件 / 局限** · 不直接外推至无低维结构的任意分布

**可复用机制** · 在验证单步生成的缩放规律时控制内在维度和噪声

<a id="paper-154335"></a>

## ESENSC: A Polynomial-Time Axiomatic Alternative to SHAP

[官方论文页](https://neurips.cc/virtual/2026/poster/154335) · [作者来源](https://openreview.net/forum?id=EOUyLpw8l7)

- **问题 / 瓶颈** · 精确 SHAP 对特征数呈指数增长
- **核心创新 / 方法** · 用计算约束和受限边际差异刻画确定性闭式归因规则
- **Baseline** · 精确 SHAP 与抽样近似
- **Benchmark** · 神经网络和 XGBoost，比较偏差、排名一致性和开销
- **关键结果 / 消融** · 作者报告线性伸缩，较抽样近似更贴近精确归因
- **适用条件 / 局限** · 受限公理与完整 SHAP 不等价，交互分布变化需复核

**可复用机制** · 在可精确计算的小规模对照上选择高维归因替代

<a id="paper-151206"></a>

## ES-Merging: Biological MLLM Merging via Embedding Space Signals

[官方论文页](https://neurips.cc/virtual/2026/poster/151206) · [作者来源](https://openreview.net/forum?id=cB1cxze69T)

- **问题 / 瓶颈** · 只看参数难保留模型对各输入模态的专门能力
- **核心创新 / 方法** · 从不同粒度的嵌入响应分别估计层级与元素级系数
- **Baseline** · 参数空间启发式合并
- **Benchmark** · 跨模态推理和单模态能力保留评测，细节待核
- **关键结果 / 消融** · 作者报告两方面均改善
- **适用条件 / 局限** · 依赖校准输入能覆盖部署模态，此卡只提取通用合并思路

**可复用机制** · 固定合并预算，以分模态验证比较参数驱动和输入响应驱动的系数

<a id="paper-139789"></a>

## EsoLang-Bench: Evaluating Large Language Models via Esoteric Programming Languages

[官方论文页](https://neurips.cc/virtual/2026/poster/139789) · [作者来源](https://openreview.net/forum?id=4eE8q4LYIm)

- **问题 / 瓶颈** · 常见语言评测可能受预训练覆盖影响
- **核心创新 / 方法** · 将相同问题移植到五种低频图灵完备语言
- **Baseline** · Python、JavaScript 版本，另对比不同提示策略
- **Benchmark** · 80 个问题、五种低频语言与五个前沿模型
- **关键结果 / 消融** · 常用语言顶尖模型达 100%，低频版本约 0–11%
- **适用条件 / 局限** · 低频语法本身的困难和语料稀缺未完全隔离

**可复用机制** · 以相同任务逻辑更换接口语法，检测工具使用的分布依赖

<a id="paper-154196"></a>

## ESSAM: A Novel Competitive Evolution Strategies Approach to Reinforcement Learning for Memory Efficient LLMs Fine-Tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/154196) · [作者来源](https://openreview.net/forum?id=FU76df5Sqr)

- **问题 / 瓶颈** · 数学后训练显存消耗高
- **核心创新 / 方法** · 将参数空间演化搜索结合尖锐度目标，另设计加速变体
- **Baseline** · PPO、GRPO
- **Benchmark** · GSM8K 与六个泛化集，测准确率、显存和耗时
- **关键结果 / 消融** · GSM8K 平均 78.27%，摘要报告相较 PPO 与 GRPO 显存分别降至约 1/18 与 1/10
- **适用条件 / 局限** · 完整公平比较需匹配训练总算力

**可复用机制** · 同时记录显存、模型调用数和端到端时间，避免只以单步资源选算法

<a id="paper-149338"></a>

## ESS-Flow: training-free guidance as Bayesian inference in source space

[官方论文页](https://neurips.cc/virtual/2026/poster/149338) · [作者来源](https://openreview.net/forum?id=qokTHEVYpp)

- **问题 / 瓶颈** · 常规条件引导要求梯度或配对训练
- **核心创新 / 方法** · 利用高斯源先验进行椭圆切片采样，只调用前向生成与观测
- **Baseline** · 摘要未列具名方法
- **Benchmark** · 材料目标约束等设置，保留非生物模型证据
- **关键结果 / 消融** · 作者展示无需反向传播的条件生成，幅度待核
- **适用条件 / 局限** · 依赖高斯先验与可计算的观测似然

**可复用机制** · 在离散观测下比较源空间贝叶斯采样和样本拒绝的调用量

<a id="paper-152597"></a>

## Estimating and Orthogonalizing Unknown Pre-training Gradients for Continual Fine-tuning of Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152597) · [作者来源](https://openreview.net/forum?id=RvsI4JyU2Q)

- **问题 / 瓶颈** · 持续微调会损失通识且原预训练数据不可得。
- **核心创新 / 方法** · 学习软提示寻找易遗忘样本，并以一阶 Pareto 更新约束梯度正交。
- **Baseline** · 正交投影类持续微调方法。
- **Benchmark** · 多个语言模型的旧任务、通识与新任务评测，名称待核。
- **关键结果 / 消融** · 作者报告两类旧能力保存改善，幅度待核。
- **适用条件 / 局限** · 代理梯度能否覆盖真实能力取决于伪样本。

**可复用机制** · 用易遗忘伪样本估计未知预训练梯度，再约束新任务更新方向。

<a id="paper-149123"></a>

## Estimating Continuous Treatment Effects with Recourse Data

[官方论文页](https://neurips.cc/virtual/2026/poster/149123) · [作者来源](https://openreview.net/forum?id=sipan8Hqx1)

- **问题 / 瓶颈** · 观测仅记录实际施加的连续处理。
- **核心创新 / 方法** · 将改变结果所需的处理量视为边界样本，对只见负例的左截断用 Lynden–Bell 校正，再构造辅助损失。
- **Baseline** · 标准连续处理估计器，名称待核。
- **Benchmark** · 合成与半合成剂量响应估计。
- **关键结果 / 消融** · 作者报告一致改善，幅度待核。
- **适用条件 / 局限** · 依赖可识别边界和相应正性条件。

**可复用机制** · 用结果翻转边界为日志覆盖稀疏区间补充监督。

<a id="paper-155112"></a>

## Estimating Implicit Regularization in Deep Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/155112) · [作者来源](https://openreview.net/forum?id=8J2wYjpdE2)

- **问题 / 瓶颈** · 训练技巧的隐式偏置不易解析。
- **核心创新 / 方法** · 拟合能解释更新偏差的惩罚项。
- **Baseline** · 已知 L1、L2 和早停效应作为校验。
- **Benchmark** · 显式正则对照及深网 dropout 分析。
- **关键结果 / 消融** · 恢复已知惩罚，并在 dropout 中观察到隐式 L2 效应。
- **适用条件 / 局限** · 拟合依赖轨迹及候选惩罚族，等效近似未必唯一。

**可复用机制** · 从实际权重更新与损失梯度之差估计等效正则。

<a id="paper-151197"></a>

## Estimating Model-Level Membership Inference Vulnerability Without Reference Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151197) · [作者来源](https://openreview.net/forum?id=cEP6vewR7h)

- **问题 / 瓶颈** · 大量参考模型使例行隐私审计昂贵。
- **核心创新 / 方法** · 用训练和测试损失的总体分布估计模型级风险，按分布形态校准估计量。
- **Baseline** · 参考模型审计以及低成本参考对照。
- **Benchmark** · 九个图像分类架构、四个数据集和五种 GPT-2 尺寸。
- **关键结果 / 消融** · 两类设定中代理估计误差约为 0.03 和 0.01。
- **适用条件 / 局限** · 用于模型级风险估计，部署须重新校准。

**可复用机制** · 将授权模型隐私筛查与逐样本判定分离。

<a id="paper-152169"></a>

## Estimating the expected output of wide random MLPs more efficiently than sampling

[官方论文页](https://neurips.cc/virtual/2026/poster/152169) · [作者来源](https://openreview.net/forum?id=V2CWyf8875)

- **问题 / 瓶颈** · 直接采样估计需要多次前向。
- **核心创新 / 方法** · 以累积量和 Hermite 展开近似逐层激活分布。
- **Baseline** · Monte Carlo。
- **Benchmark** · 初始化宽 MLP、高斯输入，比较均方误差、计算量与稀有事件概率。
- **关键结果 / 消融** · 充分宽时达到同误差所需 FLOPs 较少；稀有事件估计亦受益。
- **适用条件 / 局限** · 需验证有限宽、非高斯和训练后网络。

**可复用机制** · 宽随机网络估计均值时比较逐层分布近似与 Monte Carlo。

<a id="paper-153468"></a>

## Estimation of the Label-Noise Transition Matrix with Performance Guarantees via Selective Classification

[官方论文页](https://neurips.cc/virtual/2026/poster/153468) · [作者来源](https://openreview.net/forum?id=L7DQ7FTnLR)

- **问题 / 瓶颈** · 类别后验不准会污染转移率。
- **核心创新 / 方法** · 以二分类和单侧选择性决策构造估计，并推导有限样本界。
- **Baseline** · 基于类别后验的估计。
- **Benchmark** · 有限样本理论，摘要未列实证数据。
- **关键结果 / 消融** · 提供估计保证及算法细化误差界。
- **适用条件 / 局限** · 保证依赖选择性分类器及相应分布条件。

**可复用机制** · 估计标签转移矩阵时用单侧选择性分类替代类别后验拟合。

<a id="paper-149601"></a>

## Euclidean Embedding of Data Using Local Distances

[官方论文页](https://neurips.cc/virtual/2026/poster/149601) · [作者来源](https://openreview.net/forum?id=otyFLS0MyX)

- **问题 / 瓶颈** · 原始向量缺失，直接计算全局距离不可行。
- **核心创新 / 方法** · 最小化局部度量失配，从图计算变分方程并迭代解稀疏线性系统。
- **Baseline** · 摘要未列具名对照。
- **Benchmark** · 合成流形和真实数据，检查邻域及度量保留。
- **关键结果 / 消融** · 作者报告局部关系保留且近似全局等距。
- **适用条件 / 局限** · 邻接图质量制约恢复，非等距对象不保证精确。

**可复用机制** · 仅有邻域距离时仍可估计欧氏坐标。

<a id="paper-154221"></a>

## Euclidean Score-Based Generative Modeling with Permutation Semantics

[官方论文页](https://neurips.cc/virtual/2026/poster/154221) · [作者来源](https://openreview.net/forum?id=FJgavPHMxU)

- **问题 / 瓶颈** · 离散排列与连续扩散的状态空间不兼容。
- **核心创新 / 方法** · 用中心化坐标的排序区编码排列，共享边界对应相邻交换。
- **Baseline** · 连续松弛与离散扩散方法。
- **Benchmark** · 拼图、MNIST 四位排序、旅行商及偏好排序。
- **关键结果 / 消融** · 作者报告准确性与计算效率改善，具体指标待核。
- **适用条件 / 局限** · 排序边界的质量及大排列规模表现待核。

**可复用机制** · 在连续坐标排序区域中建模排列，末端仅排序一次。

<a id="paper-150332"></a>

## Euler-Mamba: Learning Resolution-Invariant State Evolution on Polar Manifolds for Asymmetric Pansharpening

[官方论文页](https://neurips.cc/virtual/2026/poster/150332) · [作者来源](https://openreview.net/forum?id=itSOxQyCrl)

- **问题 / 瓶颈** · 笛卡尔扫描不便区分频域几何与光谱信息。
- **核心创新 / 方法** · 在极域做径向状态演化，显式旋转相位并独立缩放幅度。
- **Baseline** · 笛卡尔选择性扫描及全色锐化对照。
- **Benchmark** · 非对称全色锐化和零样本跨分辨率。
- **关键结果 / 消融** · 作者报告质量、复杂度与跨尺度表现改善，幅度待核。
- **适用条件 / 局限** · 依赖频域构造与传感数据对齐。

**可复用机制** · 将相位对齐与幅度校准分开建模。

<a id="paper-148681"></a>

## EVA-0: Test-Time Model Evolution with Only Two Forward Passes per Sample

[官方论文页](https://neurips.cc/virtual/2026/poster/148681) · [作者来源](https://openreview.net/forum?id=vrZyjNTvp5)

- **问题 / 瓶颈** · 反传开销高，零阶更新可能漂移或走捷径。
- **核心创新 / 方法** · 尺度不变损失、锚引导及逐样本双侧扰动共用推理预算。
- **Baseline** · DeYO 和 FOA。
- **Benchmark** · ImageNet-C 上的 ViT-Base。
- **关键结果 / 消融** · 作者报告优于二者且较 FOA 加速 14 倍。
- **适用条件 / 局限** · 设备、扰动分布和长期稳定性待核。

**可复用机制** · 预算仅两次前向时用锚约束缓解更新漂移。

<a id="paper-155915"></a>

## EVA-Cap: Optimizing Audiovisual Video Captioning via Event-Centric Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/155915) · [作者来源](https://openreview.net/forum?id=1q1CvwCzHA)

- **问题 / 瓶颈** · 无结构文本损失掩盖细粒度音画错误。
- **核心创新 / 方法** · 构造原子事件监督，先 SFT 再用三项事件目标做 GRPO。
- **Baseline** · 现有音画描述方法，名称待核。
- **Benchmark** · ChronusAV 和 WorldSense。
- **关键结果 / 消融** · 摘要报告平均增益分别为 5.3% 和 3.3%。
- **适用条件 / 局限** · 依赖事件切分及质量控制。

**可复用机制** · 视频描述按事件分别监督完整性、归因和同步。

<a id="paper-148728"></a>

## EVA: Evidence-seeking Visual Agent for Hallucination-Resistant Multimodal Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/148728) · [作者来源](https://openreview.net/forum?id=vUqsQ4aoDb)

- **问题 / 瓶颈** · 工具调用可能失败，答案也可能忽略正确证据。
- **核心创新 / 方法** · 以中间观察重规划工具参数，由快慢路由决定取证，并独立核对证据。
- **Baseline** · 直接视觉模型及多智能体推理。
- **Benchmark** · 视觉推理可靠性与工具成本，名称待核。
- **关键结果 / 消融** · 作者报告可靠性改善且选择性调用控制成本。
- **适用条件 / 局限** · 外部工具错误和路由漏判仍可能传播。

**可复用机制** · 复杂视觉问题走外部工具路径并独立检查答案与证据一致。

<a id="paper-139131"></a>

## EvalAwareBench: A Benchmark for Measuring Evaluation Awareness in Frontier Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139131) · [作者来源](https://openreview.net/forum?id=j7WYZpyj9J)

- **问题 / 瓶颈** · 转录来源和探针跨模型失配可能改变排名。
- **核心创新 / 方法** · 用统一的验证流水线记录评估意识，按转录生成器控制混杂。
- **Baseline** · 未分层及复用单一探针的做法。
- **Benchmark** · 系统卡评估与多种部署转录。
- **关键结果 / 消融** · 转录生成器解释 11.25% 测量变异，并可改变排名。
- **适用条件 / 局限** · 可识别评测不等于实际行为改变。

**可复用机制** · 比较评测有效性时按生成器分层并逐模型校准。

<a id="paper-139724"></a>

## Evaluating AI-based Scientific Knowledge Synthesis with Epidemiological Systematic Reviews

[官方论文页](https://neurips.cc/virtual/2026/poster/139724) · [作者来源](https://openreview.net/forum?id=8HqJ3tXDtH)

- **问题 / 瓶颈** · 汇总分数容易掩盖阶段瓶颈。
- **核心创新 / 方法** · 建立专家标注的综述评估集，并给各阶段独立指标。
- **Baseline** · 五个前沿推理模型。
- **Benchmark** · 16,248 篇文章的综述流程，含字段 F1 和成本。
- **关键结果 / 消融** · 抽取平均字段 F1 均未超过 0.67，成本相差可达 96 倍。
- **适用条件 / 局限** · 结果针对所测文献语料，不能直接推广到自主部署。

**可复用机制** · 文献综述代理按筛选、抽取等阶段分别验收。

<a id="paper-153547"></a>

## Evaluating and Understanding Scheming Propensity in LLM Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/153547) · [作者来源](https://openreview.net/forum?id=KZEBAGDrLx)

- **问题 / 瓶颈** · 在人为极端设置观察到风险不等于实际发生概率。
- **核心创新 / 方法** · 分别比较主体和环境因素，检查受控评估与实际配置间差异。
- **Baseline** · 不同设置下的隔离行为评估。
- **Benchmark** · 面向具备工具接口的语言代理的受控安全评估。
- **关键结果 / 消融** · 作者报告常规配置下观察较少，结果对环境和监督设置敏感。
- **适用条件 / 局限** · 低观察频率不能排除低概率或未覆盖行为。

**可复用机制** · 用真实部署配置验证安全结论对环境变化的敏感性。

<a id="paper-139219"></a>

## Evaluating an Evaluation: Membership Inference Attacks as Machine Unlearning Diagnostics

[官方论文页](https://neurips.cc/virtual/2026/poster/139219) · [作者来源](https://openreview.net/forum?id=eA1BsaVVh5)

- **问题 / 瓶颈** · 单一聚合隐私分数可能混淆训练质量和真正遗忘。
- **核心创新 / 方法** · 以原模型、重训和遗忘模型的差距闭合作为归一化诊断。
- **Baseline** · 原模型与数据删除后重训模型。
- **Benchmark** · 八组数据架构、四种方法与 500 余次实验。
- **关键结果 / 消融** · 约 42% 实验任务对难区分原与重训，八组有五组出现单调性违规。
- **适用条件 / 局限** · 高记忆状态下的诊断价值较强。

**可复用机制** · 遗忘验收同时检查指标可分性和随遗忘量变化的单调性。

<a id="paper-139422"></a>

## Evaluating Compositional Generalization in Transformers: The Role of Composition Equivalence and Module Coverage

[官方论文页](https://neurips.cc/virtual/2026/poster/139422) · [作者来源](https://openreview.net/forum?id=RdGxXfd2x2)

- **问题 / 瓶颈** · 不同组合可能是同一函数，使换序看起来像外推。
- **核心创新 / 方法** · 系统改变训练测试的函数等价性和模块上下文覆盖，对照直接及逐步监督。
- **Baseline** · 只监督末端以及带中间监督的模型。
- **Benchmark** · 合成函数组合及 LiveCodeBench 上的 Llama3-8B。
- **关键结果 / 消融** · 去掉等价后直接模型明显退化，覆盖偏移增大使两类模型均退化。
- **适用条件 / 局限** · 真实复杂任务的等价判定可能难以完成。

**可复用机制** · 组合泛化评测同时控制端到端函数等价与模块覆盖。

<a id="paper-139655"></a>

## Evaluating Deployable Inference-Time Error Prediction in Vision MoEs

[官方论文页](https://neurips.cc/virtual/2026/poster/139655) · [作者来源](https://openreview.net/forum?id=Crc1w3K3Ig)

- **问题 / 瓶颈** · 备用专家含信号并不代表可可靠纠正主预测。
- **核心创新 / 方法** · 将非选中专家特征与路由信号融合做后验校准。
- **Baseline** · 校准过的仅路由信号基线。
- **Benchmark** · 五个 RGB 和多光谱分类数据集，测 top-1、错误排序及 ECE。
- **关键结果 / 消融** · 路由错误 ECE 平均改善约 10–13%，准确率收益不稳定。
- **适用条件 / 局限** · 额外前向成本与校准集迁移需评估。

**可复用机制** · 额外专家的预算优先用于判别路由错误，再评估能否提升准确率。

<a id="paper-139290"></a>

## Evaluating Depth and Breadth in Test-Time Scaling for Compositional Visual Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/139290) · [作者来源](https://openreview.net/forum?id=ZA59XMPrcN)

- **问题 / 瓶颈** · 单一规模指标忽略准确率、延迟和吞吐的不同约束。
- **核心创新 / 方法** · 同预算比较深采样、并行、分步、修正及混合路由。
- **Baseline** · 各固定深度与广度策略。
- **Benchmark** · 组合文生图，比较对象、数量、空间关系绑定与成本。
- **关键结果 / 消融** · 简单提示并行有竞争力，复杂提示修正更有用，混合方案常有更好权衡。
- **适用条件 / 局限** · 受验证器与编辑器质量制约。

**可复用机制** · 按提示复杂度在并行探索与串行修正间调预算。

<a id="paper-139438"></a>

## Evaluating Epistemic Uncertainty: Beyond OOD Detection and Active Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/139438) · [作者来源](https://openreview.net/forum?id=PscPjahZWf)

- **问题 / 瓶颈** · 域外检测或相关性指标和真实拒判目的可能不一致。
- **核心创新 / 方法** · 将选择性预测写作带覆盖约束的风险与遗憾优化，求最优混合阈值。
- **Baseline** · 以域外检测、主动学习等代理任务排名。
- **Benchmark** · 稠密人工标注数据与选择性预测理论。
- **关键结果 / 消融** · 作者报告决策排名与代理排名可逆转。
- **适用条件 / 局限** · 依赖有足够标注估计不可约与可约减误差。

**可复用机制** · 用风险、可约减误差和覆盖率曲面判断不确定性是否有决策用处。

<a id="paper-139677"></a>

## Evaluating Multimodal Narrative Understanding of Popular Hollywood Films

[官方论文页](https://neurips.cc/virtual/2026/poster/139677) · [作者来源](https://openreview.net/forum?id=Awura1yDmq)

- **问题 / 瓶颈** · 静态视觉难覆盖影片叙事线索
- **核心创新 / 方法** · 用流行且可能属公版的影片构造叙事选择题
- **Baseline** · 视觉语言、视听模型和人类
- **Benchmark** · 好莱坞影片叙事选择题准确率
- **关键结果 / 消融** · 视听模型最高61.1%，多种视觉模型接近随机
- **适用条件 / 局限** · 历史影片的文化与年代覆盖有限

**可复用机制** · 区分视听与纯视觉叙事理解。在匹配预算下复查适用边界。

<a id="paper-139125"></a>

## Evaluating Neural Data Tokenizers: A Framework for Assessing Learned Representations of Spiking Activity

[官方论文页](https://neurips.cc/virtual/2026/poster/139125) · [作者来源](https://openreview.net/forum?id=jYb8X9iFPY)

- **问题 / 瓶颈** · 重建精度可能误导模型选型
- **核心创新 / 方法** · 用七维指标评估离散、连续、单神经元及群体分词
- **Baseline** · 不同分词策略
- **Benchmark** · 十个跨物种、脑区和记录技术的数据集
- **关键结果 / 消融** · 仅重建训练可支持下游，但两种质量可明显分离
- **适用条件 / 局限** · 限于所测记录和任务

**可复用机制** · 选择神经分词器时分别测重建和下游效用。在匹配预算下复查适用边界。

<a id="paper-140116"></a>

## Evaluating Physical Reasoning in LLM Agents Requires Construction Benchmarks

[官方论文页](https://neurips.cc/virtual/2026/poster/140116) · [作者来源](https://openreview.net/forum?id=42PVaAYxLX)

- **问题 / 瓶颈** · 匹配目标外观无法证明制品能工作
- **核心创新 / 方法** · 按真实物理及功能验证审计现有基准，并列出五种能力
- **Baseline** · 现有物理基准
- **Benchmark** · 十一项基准审计
- **关键结果 / 消融** · 仅两项同时满足两条件，均为建造任务
- **适用条件 / 局限** · 五维能力框架尚无全覆盖实证

**可复用机制** · 用物理功能验证检验建造任务。在匹配预算下复查适用边界。

<a id="paper-139638"></a>

## Evaluating Spatiotemporal Reasoning of Vision-Language Models in Atari Gameplay

[官方论文页](https://neurips.cc/virtual/2026/poster/139638) · [作者来源](https://openreview.net/forum?id=DxBsMki9Zo)

- **问题 / 瓶颈** · 实际延迟会混淆视觉时序推理和响应速度
- **核心创新 / 方法** · 控制游戏观测时序，并用分数可分性分析诊断任务
- **Baseline** · 不同视觉模型、提示及记忆设计
- **Benchmark** · AtariBench二十款游戏的顺序动作决策
- **关键结果 / 消融** · 模型常误判运动且过度依赖文本历史
- **适用条件 / 局限** · 电子游戏结果不能直接外推实景

**可复用机制** · 将模型推理耗时与游戏状态推进解耦。在匹配预算下复查适用边界。

<a id="paper-139147"></a>

## Evaluating Synthetic ECG Pretraining: When Can Patient-Free Simulators Substitute for Real ECG Data?

[官方论文页](https://neurips.cc/virtual/2026/poster/139147) · [作者来源](https://openreview.net/forum?id=iJc0X3nEby)

- **问题 / 瓶颈** · 迁移协议会改变模拟数据的比较结论
- **核心创新 / 方法** · 固定编码器与MAE目标，比较来源和匹配样本预算
- **Baseline** · 真实信号、模拟器、VAE、DCGAN及扩散
- **Benchmark** · PTB-XL、G12EC、CPSC2018的26项任务及F1
- **关键结果 / 消融** · 十万样本时SimECG-N在22项排首位，冻结探针仍受益于真实异常暴露
- **适用条件 / 局限** · 结论限于单导联和所测协议

**可复用机制** · 分别用冻结探针和全量微调判断合成数据是否可替代实测。在匹配预算下复查适用边界。

<a id="paper-139634"></a>

## Evaluating Test-Time Scaling of General LLM Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/139634) · [作者来源](https://openreview.net/forum?id=EDfvwinqmW)

- **问题 / 瓶颈** · 额外算力未必改善异质任务表现
- **核心创新 / 方法** · 控制预算扫描顺序交互和轨迹采样
- **Baseline** · 十种Agent与不同测试时预算
- **Benchmark** · 搜索、编码、推理和工具使用统一评测
- **关键结果 / 消融** · 两种扩展均未稳定获益，分别受平台期和验证不足限制
- **适用条件 / 局限** · 依赖任务分布和结果验证器

**可复用机制** · 分别测增加交互步数和并行轨迹的边际收益。在匹配预算下复查适用边界。

<a id="paper-157023"></a>

## Evaluating the evidence trace of NeurIPS 2025 contributions with agentic code auditing

[官方论文页](https://neurips.cc/virtual/2026/poster/157023) · [作者来源](https://openreview.net/forum?id=xjCJY8Xxcm)

- **问题 / 瓶颈** · 自报清单难覆盖实现与论文的偏差
- **核心创新 / 方法** · 先生成证据定位，再独立核验发现并交人工抽查
- **Baseline** · 自报可复现性清单及人工核验
- **Benchmark** · 抽查100篇NeurIPS 2025实证论文
- **关键结果 / 消融** · 87篇可取代码中发现609项差异；抽检中1.7%有误
- **适用条件 / 局限** · 无法检验未公开代码，审计也不能替代复跑

**可复用机制** · 将论文结果追溯到产生结果的代码位置。在匹配预算下复查适用边界。

<a id="paper-138974"></a>

## Evaluating Uncertainty Calibration in Probabilistic Time Series Foundation Models

[官方论文页](https://neurips.cc/virtual/2026/poster/138974) · [作者来源](https://openreview.net/forum?id=t3VdYykgSV)

- **问题 / 瓶颈** · 汇总误差掩盖特定时距的失准
- **核心创新 / 方法** · 拆分总体、步长和条件校准，比较事后修正
- **Baseline** · 常用模型及重校准方法，具名待核
- **Benchmark** · 多数据集概率预测
- **关键结果 / 消融** · 不同模型呈系统失准，事后校准仅能改善部分口径
- **适用条件 / 局限** · 摘要未给定量幅度及数据集清单

**可复用机制** · 按预测步长和条件分别测不确定性校准。在匹配预算下复查适用边界。

<a id="paper-139404"></a>

## Evaluating Whether LLMs Can Reliably Connect the DOTs?

[官方论文页](https://neurips.cc/virtual/2026/poster/139404) · [作者来源](https://openreview.net/forum?id=St4No81OAc)

- **问题 / 瓶颈** · 参数量和缺口位置不可靠地解释补全质量
- **核心创新 / 方法** · 遮蔽一至三句，以自动指标及五维质量标准评测
- **Baseline** · 二十种开源LLM及不同提示
- **Benchmark** · 约9200个跨四类叙事样本
- **关键结果 / 消融** · Gemma-2-2B质评4.02/5，显式推理增益仅0.6%
- **适用条件 / 局限** · 难度规律限所测任务，质评协议待核

**可复用机制** · 按领域和叙事长度评测文本补全。在匹配预算下复查适用边界。

<a id="paper-148437"></a>

## Evaluation Awareness in Language Models Has Limited Effect on Behaviour

[官方论文页](https://neurips.cc/virtual/2026/poster/148437) · [作者来源](https://openreview.net/forum?id=xp2oWSnMPf)

- **问题 / 瓶颈** · 推理中说正在被评测并不等于策略性改变
- **核心创新 / 方法** · 对照自然出现与受控文本变化下的答案分布
- **Baseline** · 有无明确评测意识的配对对照
- **Benchmark** · 开放权重模型的安全、对齐、道德与观点测试
- **关键结果 / 消融** · 自然出现时最大偏移3.7个百分点，受控比较效应较小
- **适用条件 / 局限** · 仅衡量表述与所测行为，不涵盖隐性意识

**可复用机制** · 用行为差异验证评测意识，避免只看自述频率。在匹配预算下复查适用边界。

<a id="paper-139130"></a>

## EVALUATION CARDS: An Interpretive Layer for AI Evaluation Reporting

[官方论文页](https://neurips.cc/virtual/2026/poster/139130) · [作者来源](https://openreview.net/forum?id=jGvGY7wh7Q)

- **问题 / 瓶颈** · 排行榜分数难比较且证据来源不明
- **核心创新 / 方法** · 从文献和访谈定 schema 并部署监测工具，给四类解释信号
- **Baseline** · 分散的模型卡、榜单和报告方式
- **Benchmark** · 52篇文献、10次访谈及101843项结果
- **关键结果 / 消融** · 发现报告系统性缺口，摘要未给信号的独立验证
- **适用条件 / 局限** · 数据覆盖和抽取精度影响解释

**可复用机制** · 统一将基准、实验运行与模型元数据链接到结果。在匹配预算下复查适用边界。

<a id="paper-152346"></a>

## Even More Guarantees for Variational Inference in the Presence of Symmetries

[官方论文页](https://neurips.cc/virtual/2026/poster/152346) · [作者来源](https://openreview.net/forum?id=TjhnPIXaBU)

- **问题 / 瓶颈** · 近似族错设时难知哪些统计量仍可准确恢复
- **核心创新 / 方法** · 为前向KL和α散度推导均值与相关矩阵精确恢复充分条件
- **Baseline** · 先前依赖对数凹的保证
- **Benchmark** · 对称错设目标，含多峰示例
- **关键结果 / 消融** · 在所给条件下无需目标对数凹，反例展示优化失败
- **适用条件 / 局限** · 充分条件不等于一般保证

**可复用机制** · 按目标对称性选择散度与位置尺度族。在匹配预算下复查适用边界。

<a id="paper-150866"></a>

## Even Sailors Need Calm Seas: Taming the Geometry of VLMs for Fast Adversarial Fine-Tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/150866) · [作者来源](https://openreview.net/forum?id=elpJhhSIEj)

- **问题 / 瓶颈** · 单步训练可能在训练半径表现好而在更弱扰动失效
- **核心创新 / 方法** · 训练时约束局部梯度几何以维持近似稳定
- **Baseline** · 已有单步鲁棒微调
- **Benchmark** · 多种视觉语言架构和数据，名称待核
- **关键结果 / 消融** · 作者报告鲁棒性和效率改善，发现半径过拟合
- **适用条件 / 局限** · 未验证所有输入扰动与架构

**可复用机制** · 鲁棒微调时独立测多个扰动强度。在匹配预算下复查适用边界。

<a id="paper-154551"></a>

## Even Sharper Bounds for Transductive Learning and Its Applications

[官方论文页](https://neurips.cc/virtual/2026/poster/154551) · [作者来源](https://openreview.net/forum?id=CiwuIEyV2o)

- **问题 / 瓶颈** · 既有转导界相比归纳界多一项对数差距
- **核心创新 / 方法** · 用交换游走的集中不等式和分层局部分析控制损失差
- **Baseline** · 经典归纳与既有转导局部界
- **Benchmark** · 有限VC二分类与转导核学习理论
- **关键结果 / 消融** · 达到相应归纳界并改进核学习上界
- **适用条件 / 局限** · 依赖无放回抽样和所列假设

**可复用机制** · 在无放回划分中用局部复杂度分析转导风险。在匹配预算下复查适用边界。

<a id="paper-150183"></a>

## Event based Multi-Velocity-Scale Imaging

[官方论文页](https://neurips.cc/virtual/2026/poster/150183) · [作者来源](https://openreview.net/forum?id=k6FlyTwE3g)

- **问题 / 瓶颈** · 全局固定阈值在高速冗余与慢速细节丢失间取舍
- **核心创新 / 方法** · 多阈值成像并在现有事件相机实现采集
- **Baseline** · 统一对比阈值
- **Benchmark** · 合成与真实混合速度场景
- **关键结果 / 消融** · 保留结构及快速动态同时减少事件，数值待核
- **适用条件 / 局限** · 阈值如何随场景变化待查

**可复用机制** · 按运动尺度分配对比度阈值。在匹配预算下复查适用边界。

<a id="paper-153700"></a>

## Event-Centric Perception in Weak-Signal Physical Streams with Multimodal LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/153700) · [作者来源](https://openreview.net/forum?id=JQhrfSnBxh)

- **问题 / 瓶颈** · 直接提示容易漏掉弱且跨时间分布的线索
- **核心创新 / 方法** · 局部事件推理和轻量事件对齐适配
- **Baseline** · 直接提示前沿多模态模型
- **Benchmark** · 声呐事件基准及热成像
- **关键结果 / 消融** · 声呐召回0.041到0.914，归一化误差0.982到0.334
- **适用条件 / 局限** · 仅在所测传感器与事件定义下验证

**可复用机制** · 将弱信号流输出定义为结构化事件。在匹配预算下复查适用边界。

<a id="paper-151283"></a>

## Event-Grounded Sparse Autoencoders for Vision-Language-Action Policies

[官方论文页](https://neurips.cc/virtual/2026/poster/151283) · [作者来源](https://openreview.net/forum?id=bY6Sy7BOHn)

- **问题 / 瓶颈** · 机器人动作难像文字一样解释，滚动验证昂贵
- **核心创新 / 方法** · 按视觉状态及时间聚类末端关键帧对齐行为事件
- **Baseline** · 非事件排序与不同干预位置
- **Benchmark** · 两类仿真架构和真机试验
- **关键结果 / 消融** · OpenVLA效果最强并迁移至连续动作块
- **适用条件 / 局限** · 架构与干预位置影响结果，强干预不宜部署

**可复用机制** · 用闭环行为事件排序稀疏自编码器特征。在匹配预算下复查适用边界。

<a id="paper-153545"></a>

## EventLens: Event-Structure Reinforcement Learning for Video Understanding

[官方论文页](https://neurips.cc/virtual/2026/poster/153545) · [作者来源](https://openreview.net/forum?id=Ka48Llurl6)

- **问题 / 瓶颈** · 字幕训练可走语言捷径并漏掉事件关系
- **核心创新 / 方法** · 用切分、发展和事件关系任务分别训练再作多教师蒸馏
- **Baseline** · 直接混合强化学习
- **Benchmark** · Qwen3-VL上的时间定位、事件推理和视频问答
- **关键结果 / 消融** · 作者报告时序改善、通用问答保持且训练成本下降
- **适用条件 / 局限** · 依赖结构扰动任务和确定性奖励覆盖

**可复用机制** · 用可验证的事件结构任务替代单纯字幕监督。在匹配预算下复查适用边界。

<a id="paper-151793"></a>

## EventPrune: Cascaded Event-Assisted Token Pruning for Efficient First-Person Dynamic Spatial Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/151793) · [作者来源](https://openreview.net/forum?id=XyYCbuAP7m)

- **问题 / 瓶颈** · 静态剪枝易丢掉短时运动细节
- **核心创新 / 方法** · 先选运动关键帧再筛区域并融合事件和注意力信号
- **Baseline** · 完整视觉token
- **Benchmark** · 动态空间推理和ESR-Real
- **关键结果 / 消融** · 剪80%后37.62%对36.31%，推理快1.89倍
- **适用条件 / 局限** · 依赖事件传感器及RGB同步，静态信息可能被削弱

**可复用机制** · 用异步事件信号给视频token排序保留动态区域。在匹配预算下复查适用边界。

<a id="paper-153421"></a>

## Events as Triggers for Behavioral Diversity in Multi-Agent Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/153421) · [作者来源](https://openreview.net/forum?id=LSRtfZfGAE)

- **问题 / 瓶颈** · 固定身份绑定限制协作
- **核心创新 / 方法** · 以行为流形度量瞬态角色差异，按事件生成共享策略的 LoRA
- **Baseline** · 固定角色及已有多智能体方法
- **Benchmark** · 角色轮换与零样本泛化任务
- **关键结果 / 消融** · 作者报告只有该方法解出连续换角任务
- **适用条件 / 局限** · 依赖事件定义

**可复用机制** · 对照事件触发适配与固定身份或固定步长切换

<a id="paper-153487"></a>

## EverAnimate: Minute-Scale Human Animation via Latent Flow Restoration

[官方论文页](https://neurips.cc/virtual/2026/poster/153487) · [作者来源](https://openreview.net/forum?id=L0ik0L4kA9)

- **问题 / 瓶颈** · 背景质量和人物身份随时间漂移
- **核心创新 / 方法** · 跨块传播潜状态并在流匹配采样时校正速度
- **Baseline** · 长动画生成方法
- **Benchmark** · 10 秒与 90 秒动画的 PSNR、SSIM、LPIPS、FID
- **关键结果 / 消融** · 90 秒 PSNR 和 SSIM 各升 15%，LPIPS 与 FID 分别降 32% 和 27%
- **适用条件 / 局限** · 超过评测时长的稳定性待核

**可复用机制** · 分别比较跨块记忆与块内恢复的作用

<a id="paper-154368"></a>

## Every Bit, Everywhere, All At Once: A Binomial Multibit LLM Watermark

[官方论文页](https://neurips.cc/virtual/2026/poster/154368) · [作者来源](https://openreview.net/forum?id=E6Jp4SaVf6)

- **问题 / 瓶颈** · 整条消息准确率难定位不可靠位
- **核心创新 / 方法** · 作者对比逐位置信度和总体恢复指标
- **Baseline** · 八种水印基线
- **Benchmark** · 最多 64 位载荷，比较恢复和低失真区间
- **关键结果 / 消融** · 作者报告大载荷及低失真下优势更明显
- **适用条件 / 局限** · 具体编辑和文本条件待核

**可复用机制** · 在同等失真下报告各位恢复分布

<a id="paper-155361"></a>

## Every Sample Counts: Supervised Fine-Tuning of Language Models with Pointwise Constraints

[官方论文页](https://neurips.cc/virtual/2026/poster/155361) · [作者来源](https://openreview.net/forum?id=6BYu5yc6pZ)

- **问题 / 瓶颈** · 平均约束会隐去难例
- **核心创新 / 方法** · 增广拉格朗日约束各样本，并学习最小必要的松弛
- **Baseline** · 平均约束微调
- **Benchmark** · 小语言模型的指令安全、函数调用偏好及长度排序
- **关键结果 / 消融** · 作者报告尾部违反下降，下游性能大体保持
- **适用条件 / 局限** · 松弛与外点比例关系待核

**可复用机制** · 比较平均和逐样本约束时同时报告尾部和总体性能

<a id="paper-150103"></a>

## Everything at Every Scale: Scale-Invariant Diffusion with Continuous Super-Resolution

[官方论文页](https://neurips.cc/virtual/2026/poster/150103) · [作者来源](https://openreview.net/forum?id=kftOqseEy5)

- **问题 / 瓶颈** · 不同放大倍数通常需分别调节
- **核心创新 / 方法** · 前向按频带由细到粗衰减并加入匹配频谱噪声
- **Baseline** · 条件超分模型
- **Benchmark** · CIFAR-10 无条件生成、ImageNet 2–8 倍超分、Ising 重建
- **关键结果 / 消融** · CIFAR-10 FID 2.65，IS 9.63
- **适用条件 / 局限** · 尺度不变假设可能不适用于特殊成像链

**可复用机制** · 检验按频率退化的同一检查点能否覆盖多级逆问题

<a id="paper-152262"></a>

## EviAttr-OW: Evidential Attribute Reasoning for Open World Object Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/152262) · [作者来源](https://openreview.net/forum?id=UNSLchC9SB)

- **问题 / 瓶颈** · 已知类别偏置使未知目标难识别
- **核心创新 / 方法** · 用类无关属性及 Dirichlet 证据衡量已知类支持不足
- **Baseline** · 已有开放世界检测器
- **Benchmark** · RWD 五个现实应用数据集，未知类 mAP
- **关键结果 / 消融** · 未知类 mAP 增加 7.3
- **适用条件 / 局限** · 证据质量取决于属性覆盖

**可复用机制** · 单独测物体存在和分类确信度校准

<a id="paper-154066"></a>

## Evidence Guided Dual Expert Memory with Joint Routing for VLLMs Online Correction

[官方论文页](https://neurips.cc/virtual/2026/poster/154066) · [作者来源](https://openreview.net/forum?id=GQbI4onTUV)

- **问题 / 瓶颈** · 整样本残差会吸收无关背景
- **核心创新 / 方法** · 细掩码提取证据，结合图文上下文和可靠性选专家
- **Baseline** · 线上视觉语言模型编辑器
- **Benchmark** · 编辑可靠性、泛化及可解释性，具名数据待核
- **关键结果 / 消融** · 作者报告三类结果改善
- **适用条件 / 局限** · 证据掩码质量影响重用

**可复用机制** · 比较局部与全图专家的跨场景复用及非目标副作用

<a id="paper-150393"></a>

## Evidence-RL: Towards Evidence-intensive Visual Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/150393) · [作者来源](https://openreview.net/forum?id=iOZY3TyfNU)

- **问题 / 瓶颈** · 全局图像扰动无法隔离证据
- **核心创新 / 方法** · 中和对象证据并和匹配非证据区比较，结合正确性做 GRPO
- **Baseline** · 既有强化后训练
- **Benchmark** · 九个公开基准、四个骨干
- **关键结果 / 消融** · 作者报告优于基线且无额外推理开销
- **适用条件 / 局限** · 依赖弱对象候选和匹配质量

**可复用机制** · 用反事实证据与对照区验证模型是否走视觉捷径

<a id="paper-154010"></a>

## Evidential Semantic Uncertainty Decomposition for Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154010) · [作者来源](https://openreview.net/forum?id=GsfbZh21T3)

- **问题 / 瓶颈** · 语义熵只度量采样分散
- **核心创新 / 方法** · 用轻量探针保留可靠证据，并设置未获支持类
- **Baseline** · 语义不确定性及扰动分解方法
- **Benchmark** · 四种骨干，分布外及歧义检测 AUROC 和 AUPR
- **关键结果 / 消融** · 摘要报告平均 AUROC 分别升 7.4% 和 4%
- **适用条件 / 局限** · 依赖聚类和采样质量

**可复用机制** · 分别校准语义冲突与证据缺失

<a id="paper-150339"></a>

## EVIDENT: Routing MLLM Adaptation through Entity-Grounded Visual Evidence for Cross-Domain Video Temporal Grounding

[官方论文页](https://neurips.cc/virtual/2026/poster/150339) · [作者来源](https://openreview.net/forum?id=irDPXJ2g3y)

- **问题 / 瓶颈** · 换视觉域后时间知识难与实体注意力结合
- **核心创新 / 方法** · 以实体瓶颈、绑定蒸馏与证据门控定位时间段
- **Baseline** · 普通多模态微调
- **Benchmark** · 跨域视频时间定位
- **关键结果 / 消融** · 作者报告域外改善且域内表现有竞争力
- **适用条件 / 局限** · 依赖实体可识别性

**可复用机制** · 固定参数预算比较实体证据瓶颈与密集-token 适配

<a id="paper-150827"></a>

## EviSAM3: Evidence-Driven SAM3 for Referring Remote Sensing Image Segmentation

[官方论文页](https://neurips.cc/virtual/2026/poster/150827) · [作者来源](https://openreview.net/forum?id=f1JHxI12WT)

- **问题 / 瓶颈** · 遥感目标尺度和歧义使单次定位困难
- **核心创新 / 方法** · 为 SAM3 增加动量证据记忆并按信息价值重加权
- **Baseline** · SAM3 适配和现有指代分割方法
- **Benchmark** · 遥感指代分割与高歧义场景
- **关键结果 / 消融** · 作者报告多种情形改善，幅度待核
- **适用条件 / 局限** · 迭代额外成本待核

**可复用机制** · 对照单次融合与多轮记忆修正

<a id="paper-150274"></a>

## EVOCHAMBER:  Test-Time Co-evolution of Multi-Agent System at Individual, Team, and Population Scales

[官方论文页](https://neurips.cc/virtual/2026/poster/150274) · [作者来源](https://openreview.net/forum?id=jNJFL5PPGJ)

- **问题 / 瓶颈** · 全量广播可能抹平专长
- **核心创新 / 方法** · 按任务分组，并用非对称经验提炼与共享更新小组
- **Baseline** · 已有测试时适配方法
- **Benchmark** · 数学、常规代码及跨域推理任务流
- **关键结果 / 消融** · Qwen3-8B 的三类得分为 63.9%、75.7%、87.1%
- **适用条件 / 局限** · 不同任务流迁移与计算预算待核

**可复用机制** · 比较全员广播与按失败类型定向共享

<a id="paper-139527"></a>

## EvoCodeBench: Evaluating Coding Agents in Multi-Turn Iterative Interactions

[官方论文页](https://neurips.cc/virtual/2026/poster/139527) · [作者来源](https://openreview.net/forum?id=KUMjFWdsDg)

- **问题 / 瓶颈** · 单轮评测看不到持久代码状态的退化
- **核心创新 / 方法** · 保留工作区并同时验证新旧有效需求
- **Baseline** · 从参考完成状态起步的单轮评测
- **Benchmark** · 26 个常规编程任务、227 轮，MT@4 及 SR
- **关键结果 / 消融** · 多数模型单轮分高 22–40 分
- **适用条件 / 局限** · 结论依赖任务及累计测试覆盖

**可复用机制** · 迭代开发基准应保留工作区并重测旧约束

<a id="paper-153228"></a>

## EvoCUA: Evolving Computer Use Agents via Learning from Scalable Synthetic Experience

[官方论文页](https://neurips.cc/virtual/2026/poster/153228) · [作者来源](https://openreview.net/forum?id=MpUzZIp5jZ)

- **问题 / 瓶颈** · 静态示范缺少长程纠错
- **核心创新 / 方法** · 在封闭沙盒合成良性界面任务，以验证结果筛选并修正执行轨迹
- **Baseline** · OpenCUA-72B、UI-TARS-2
- **Benchmark** · OSWorld 桌面操作成功率
- **关键结果 / 消融** · 报告 56.7%，相对对照为 45.0% 和 53.1%
- **适用条件 / 局限** · 合成任务覆盖限制迁移

**可复用机制** · 评估获授权的桌面自动化时对照静态模仿与含纠错轨迹训练

<a id="paper-154131"></a>

## Evo-Depth: A Lightweight Depth-Enhanced Vision-Language-Action Model

[官方论文页](https://neurips.cc/virtual/2026/poster/154131) · [作者来源](https://openreview.net/forum?id=G2jacreNCB)

- **问题 / 瓶颈** · 显式深度或大几何模型增加部署成本
- **核心创新 / 方法** · 以轻量隐式深度模块调制视觉语言表示并逐步对齐动作
- **Baseline** · 显式及隐式三维 VLA 方法
- **Benchmark** · 四个仿真基准与真机成功率、显存和推理频率
- **关键结果 / 消融** · 作者报告 0.9B 模型在真机成功率及资源指标有优势
- **适用条件 / 局限** · 依赖多视角图像

**可复用机制** · 固定传感硬件对比轻量几何调制与 RGB 直接输入

<a id="paper-153727"></a>

## EvoGround: Self-Evolving Video Agents for Video Temporal Grounding

[官方论文页](https://neurips.cc/virtual/2026/poster/153727) · [作者来源](https://openreview.net/forum?id=JDoWHmhvEd)

- **问题 / 瓶颈** · 人工时间定位标签昂贵
- **核心创新 / 方法** · 提议器生成查询和时间段，定位器学习并反馈质量
- **Baseline** · 全监督时间定位方法
- **Benchmark** · 2500 段无标注视频与多项时间定位基准
- **关键结果 / 消融** · 作者报告达到或超过全监督模型
- **适用条件 / 局限** · 反馈错误可能自我强化

**可复用机制** · 固定无标签数据比较固定伪标注与反馈驱动的标注改进

<a id="paper-148609"></a>

## EvoInspect: A Unified Self-Evolving Multi-Agent Framework for Industrial Hardware Inspection

[官方论文页](https://neurips.cc/virtual/2026/poster/148609) · [作者来源](https://openreview.net/forum?id=wTp6LCV27h)

- **问题 / 瓶颈** · 静态预处理不能应对复合缺陷
- **核心创新 / 方法** · 粗到细定位并把恢复与检测经验分别蒸馏入记忆
- **Baseline** · 端到端及静态恢复流水线
- **Benchmark** · 轴承、PCB、太阳能电致发光及磁瓦，测召回与精度
- **关键结果 / 消融** · 作者报告定位召回与精度提高
- **适用条件 / 局限** · 不同恢复模块的独立价值待核

**可复用机制** · 按缺陷类型测试动态预处理与固定配置

<a id="paper-150446"></a>

## Evolutionary Feature Engineering for Structured Data

[官方论文页](https://neurips.cc/virtual/2026/poster/150446) · [作者来源](https://openreview.net/forum?id=hz6wl9NrRG)

- **问题 / 瓶颈** · 固定预处理难匹配数据分布
- **核心创新 / 方法** · 以标准 fit/transform 封装，利用验证集反馈迭代变换
- **Baseline** · 现成时序模型及既有表格特征工程
- **Benchmark** · 时序 MASE、WQL、MAE 和表格预测
- **关键结果 / 消融** · 作者报告时序平均误差至少下降 3%
- **适用条件 / 局限** · 反复访问验证集有过拟合风险

**可复用机制** · 保留独立测试集，比较自动变换与固定标准化

<a id="paper-148561"></a>

## Evolutionary foraging in grids: Intermittent search emerges as an optimal strategy

[官方论文页](https://neurips.cc/virtual/2026/poster/148561) · [作者来源](https://openreview.net/forum?id=wy6k0zCeMv)

- **问题 / 瓶颈** · 位移长尾不能区分行为机制。
- **核心创新 / 方法** · 让运动参数在可耗尽网格中演化，用二阶和四阶矩比较搜索模型。
- **Baseline** · Lévy 游走和间歇搜索。
- **Benchmark** · 有限环面格网，均匀或 Lévy dust 资源。
- **关键结果 / 消融** · 间歇模型 R² 超过 0.99，Lévy 模型超过 0.9。
- **适用条件 / 局限** · 结论依赖有限格网和设定的能量与覆盖适应度。

**可复用机制** · 对轨迹同时拟合不同阶位移矩，检验短程利用和长程换区是否构成独立阶段。

<a id="paper-149312"></a>

## Evolutionary System Prompt Learning for Reinforcement Learning in LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/149312) · [作者来源](https://openreview.net/forum?id=r7HI4UDi9z)

- **问题 / 瓶颈** · 只更新一处可能限制泛化。
- **核心创新 / 方法** · 并行用多条系统提示采样，权重用强化学习更新，提示用模型反思迭代。
- **Baseline** · 仅 RL、仅提示演化。
- **Benchmark** · AIME、BeyondAIME、HMMT 和智能体搜索。
- **关键结果 / 消融** · AIME 到 BeyondAIME 成功率由 38.8% 到 45.1%。
- **适用条件 / 局限** · 收益可能受候选提示预算和训练奖励影响。

**可复用机制** · 固定采样预算分别消融语言上下文更新与参数更新。

<a id="paper-148564"></a>

## Evolution Fine-Tuning: Learning to Discover Across 371 Optimization Tasks

[官方论文页](https://neurips.cc/virtual/2026/poster/148564) · [作者来源](https://openreview.net/forum?id=www9RVeEpg)

- **问题 / 瓶颈** · 对单题执行搜索会丢弃演化经验。
- **核心创新 / 方法** · 收集跨领域搜索轨迹，并以其微调开放模型。
- **Baseline** · 同一底座未经该中训练；另与测试时 RL 组合。
- **Benchmark** · 371 种优化任务的轨迹库，22 项留出任务。
- **关键结果 / 消融** · 留出任务较底座平均提高 10.22%。
- **适用条件 / 局限** · 留出任务与训练族相似程度须复核。

**可复用机制** · 训练求解器时比较学习整个候选改进过程与学习最终解。

<a id="paper-153181"></a>

## Evolving Agent Teams

[官方论文页](https://neurips.cc/virtual/2026/poster/153181) · [作者来源](https://openreview.net/forum?id=NCRt7BmX5a)

- **问题 / 瓶颈** · 固定分工会陷入局部最优。
- **核心创新 / 方法** · 监督者诊断停滞并调整分工，用共享策略树和日志传承经验。
- **Baseline** · 同 token 预算的编程智能体。
- **Benchmark** · FlashInfer 内核及生产工作负载。
- **关键结果 / 消融** · 扩展预算下内核平均加速 1.2 倍，47 负载中 36 个更快。
- **适用条件 / 局限** · 证据来自授权内核性能优化，算力预算影响可比性。

**可复用机制** · 为性能优化保留可追溯的尝试树，对照固定分工与按停滞信号调整。

<a id="paper-139805"></a>

## EvoMemBench: Benchmarking Agent Memory from a Self-Evolving Perspective

[官方论文页](https://neurips.cc/virtual/2026/poster/139805) · [作者来源](https://openreview.net/forum?id=3adOYrlRz9)

- **问题 / 瓶颈** · 统一指标掩盖记忆收益与任务结构的关系。
- **核心创新 / 方法** · 以回合内外和知识或执行两轴组织任务。
- **Baseline** · 15 种记忆方法与长上下文模型。
- **Benchmark** · EvoMemBench 统一协议。
- **关键结果 / 消融** · 长上下文仍有竞争力，检索对知识任务强，流程匹配时程序记忆更有效。
- **适用条件 / 局限** · 相关性依赖经验是否匹配任务。

**可复用机制** · 同预算按上下文是否充足和任务类型分层报告记忆收益。

<a id="paper-148706"></a>

## EvoMM: Reinforced Self-Evolving Multimodal Agentic Memory

[官方论文页](https://neurips.cc/virtual/2026/poster/148706) · [作者来源](https://openreview.net/forum?id=vfFhl0Fozp)

- **问题 / 瓶颈** · 静态摘要或纯文本转写会损失视觉线索。
- **核心创新 / 方法** · 以异构图连接回合和会话记忆，过程奖励对记忆操作做密集归因。
- **Baseline** · 纯文本、多模态及智能体记忆基线。
- **Benchmark** · Mem-Gallery、MMLongBench、LoCoMo。
- **关键结果 / 消融** · 摘要报告一致改善，幅度待核。
- **适用条件 / 局限** · 需要可判定过程反馈，图维护成本待核。

**可复用机制** · 比较静态检索与允许修订记忆的策略，分别测证据保留和时序一致性。

<a id="paper-155640"></a>

## EvoOptiGraph: Weakness-Driven Coevolution via Graph-Based Structural Generation for Optimization Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/155640) · [作者来源](https://openreview.net/forum?id=45RetuO3zX)

- **问题 / 瓶颈** · 静态自然语言转优化训练集缺结构多样性。
- **核心创新 / 方法** · 用二分图表示 MILP，经保有效性变换、编译及回译验证生成题目。
- **Baseline** · 较大通用模型、智能体和领域方法。
- **Benchmark** · 六个公开优化建模数据集。
- **关键结果 / 消融** · 作者报告准确性、可执行性及泛化改善，数值待核。
- **适用条件 / 局限** · 依赖图变换及求解器验证。

**可复用机制** · 对可形式化输出，用失败结构生成新的可验证实例。

<a id="paper-149899"></a>

## Exact Channel Decoupling via Joint Diagonalization and Uniform Splicing for Diffusion Transformer Quantization

[官方论文页](https://neurips.cc/virtual/2026/poster/149899) · [作者来源](https://openreview.net/forum?id=mO4pYQLElU)

- **问题 / 瓶颈** · 只平滑激活会遗留权重量化方差。
- **核心创新 / 方法** · 用广义特征问题联合对角化，并以 token 拼接替代时间平均。
- **Baseline** · 既有后训练量化基线。
- **Benchmark** · W3A4 的 DiT-XL/2 与 PixArt-Sigma。
- **关键结果 / 消融** · 摘要报告 FID 分别下降 16.06 和 6.49。
- **适用条件 / 局限** · 不同位宽或校准分布的稳健性待核。

**可复用机制** · 量化时同时诊断权重、激活和校准样本如何跨时间聚合。

<a id="paper-153163"></a>

## Exact Combinatorial Optimization for Partial Permutation Synchronization

[官方论文页](https://neurips.cc/virtual/2026/poster/153163) · [作者来源](https://openreview.net/forum?id=NPIijWupQs)

- **问题 / 瓶颈** · 谱松弛舍入可能破坏循环一致性。
- **核心创新 / 方法** · 平移亲和谱后用逐次线性指派，利用全幺模保持整数解。
- **Baseline** · 谱松弛匹配。
- **Benchmark** · 图像匹配，测准确性、一致性和耗时。
- **关键结果 / 消融** · 证明单调上升至 KKT 条件，摘要报告实证改善。
- **适用条件 / 局限** · 精确性针对子问题，不保证全局最优。

**可复用机制** · 当子问题有整数多面体，优先比较直接指派与连续舍入。

<a id="paper-154073"></a>

## Exact Flow Linear Attention: Exact Solution from Continuous-Time Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/154073) · [作者来源](https://openreview.net/forum?id=GOjRwLmiSD)

- **问题 / 瓶颈** · 一阶离散在高能输入下引入误差。
- **核心创新 / 方法** · 用秩一结构化简连续动力学的指数和输入积分。
- **Baseline** · 欧拉型线性注意力与 SSM。
- **Benchmark** · 语言建模、MAD 与扰动测试。
- **关键结果 / 消融** · 作者报告稳定性和困惑度改善，维持线性复杂度与并行。
- **适用条件 / 局限** · 结果依赖秩一动力学结构。

**可复用机制** · 先辨别状态更新的离散误差，再比较精确积分和普通迭代。

<a id="paper-153876"></a>

## Exact-Form Regret and Conservative Correlated Equilibria

[官方论文页](https://neurips.cc/virtual/2026/poster/153876) · [作者来源](https://openreview.net/forum?id=I6C1jbK29Z)

- **问题 / 瓶颈** · 外部遗憾不足以描述有限策略变换。
- **核心创新 / 方法** · 以位移场恰当性使势函数望远镜求和，镜像下降采用相应几何。
- **Baseline** · 半粗仿射和近端偏离。
- **Benchmark** · 理论设定，检查有限偏离遗憾和循环反例。
- **关键结果 / 消融** · 可行且有势的偏离获平方根遗憾，非零环流可导致线性遗憾。
- **适用条件 / 局限** · 尖锐性依赖光滑及单连通条件。

**可复用机制** · 分析在线算法时先检查偏离的一阶形式是否有势。

<a id="paper-155943"></a>

## Exact Gaussian Moment Matching for Residual Networks: a Second-Order Method

[官方论文页](https://neurips.cc/virtual/2026/poster/155943) · [作者来源](https://openreview.net/forum?id=1dsxDeHdpR)

- **问题 / 瓶颈** · 残差网络中的近似矩误差逐层累积。
- **核心创新 / 方法** · 推导 probit、GeLU、ReLU 等激活的均值协方差匹配，包含残差连接。
- **Baseline** · 流行近似、确定性推理与蒙特卡洛参考。
- **Benchmark** · 随机网络及变分贝叶斯网络，用 KL 测误差。
- **关键结果 / 消融** · 随机网络最高报告百万倍 KL 误差改善，贝叶斯网络约百倍。
- **适用条件 / 局限** · 逐层正态化仍是近似。

**可复用机制** · 将局部激活矩误差与整网分布误差分开评估。

<a id="paper-153709"></a>

## Exact Instance Compression for Convex Empirical Risk Minimization via Color Refinement

[官方论文页](https://neurips.cc/virtual/2026/poster/153709) · [作者来源](https://openreview.net/forum?id=JM5piPXaA4)

- **问题 / 瓶颈** · 凸求解器在完整实例上也可能成本高。
- **核心创新 / 方法** · 以颜色细化识别可合并结构，再求解压缩目标。
- **Baseline** · 原始凸 ERM 及既有线性二次规划压缩。
- **Benchmark** · 回归、逻辑分类、弹性网和核模型。
- **关键结果 / 消融** · 提供无损框架，摘要报告数值有效性。
- **适用条件 / 局限** · 依赖可识别对称结构，压缩幅度因实例而异。

**可复用机制** · 先核验目标的等价分组，再比较原始和压缩求解。

<a id="paper-155154"></a>

## Exact Posterior Score Estimation for Solving Linear Inverse Problems

[官方论文页](https://neurips.cc/virtual/2026/poster/155154) · [作者来源](https://openreview.net/forum?id=7u8YcL4Z4P)

- **问题 / 瓶颈** · 直接用无条件分数需近似测量校正。
- **核心创新 / 方法** · 把线性高斯后验分数化成算子相关移位与各向异性噪声下的去噪。
- **Baseline** · 训练免调与训练式逆问题方法。
- **Benchmark** · FFHQ、ImageNet 五种线性逆问题。
- **关键结果 / 消融** · 摘要报告多种保真指标改善及约少一个数量级的调用。
- **适用条件 / 局限** · 依赖线性高斯观测条件。

**可复用机制** · 先推导观测可否化为去噪条件，再比较训练改造和推理梯度引导。

<a id="paper-153108"></a>

## Exact power indices for plurality-voting ensembles

[官方论文页](https://neurips.cc/virtual/2026/poster/153108) · [作者来源](https://openreview.net/forum?id=Nsz4JjAs2B)

- **问题 / 瓶颈** · 单模型准确率不能反映平票及协作。
- **核心创新 / 方法** · 以组合公式和生成函数精确计算 Shapley、Banzhaf 权重。
- **Baseline** · 现有近似归因方法。
- **Benchmark** · 二分类、多分类投票及视觉语言提示集成。
- **关键结果 / 消融** · 二分类线性时间，多分类低阶多项式时间。
- **适用条件 / 局限** · 依赖相对多数投票和随机平票规则。

**可复用机制** · 按实际集成规则归因，再以剪枝后性能检验指标。

<a id="paper-156088"></a>

## Exact Recovery of Lipschitz Orthogonal Coordinate Transformations via Constrained Normalizing Flows

[官方论文页](https://neurips.cc/virtual/2026/poster/156088) · [作者来源](https://openreview.net/forum?id=0StQFVtzOM)

- **问题 / 瓶颈** · 保持分布的变换可交换潜在解释。
- **核心创新 / 方法** · 以 Lipschitz 正交坐标约束推导可辨识性，并构造受约束的流。
- **Baseline** · 既有非线性 ICA。
- **Benchmark** · 分量恢复及模型错设实验。
- **关键结果 / 消融** · 理论给出置换、缩放等价下恢复，摘要报告较强实证。
- **适用条件 / 局限** · 依赖有界非高斯源和正则假设。

**可复用机制** · 选可辨识流模型时把结构限制和等价类明确写入恢复评测。

<a id="paper-155888"></a>

## Exact Regular-Constrained Sampling for Variable-Order Markov Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/155888) · [作者来源](https://openreview.net/forum?id=25TuIlUEUu)

- **问题 / 瓶颈** · 一阶状态合并了生成器要区分的历史。
- **核心创新 / 方法** · 在可达乘积边上运行精确动态规划。
- **Baseline** · 一阶约束信念传播及小规模枚举。
- **Benchmark** · 枚举校验和 Bach 前奏曲，最大历史阶 6。
- **关键结果 / 消融** · 获得精确配分函数，复杂度随时域和可达边线性增长。
- **适用条件 / 局限** · 仅适用于可有限自动机描述的约束。

**可复用机制** · 保留模型实际上下文状态，在其与规则的乘积图上采样。

<a id="paper-148463"></a>

## Exact Topological Compliance: Generating Persistence-Equivalent Graphs

[官方论文页](https://neurips.cc/virtual/2026/poster/148463) · [作者来源](https://openreview.net/forum?id=xcQkqD4abA)

- **问题 / 瓶颈** · 软约束只保证拓扑描述近似相似。
- **核心创新 / 方法** · 以局部构造和全局约束编码实现目标持久性图。
- **Baseline** · 软拓扑正则与局部全局构造对照。
- **Benchmark** · 四个图生成基准，检验目标描述匹配。
- **关键结果 / 消融** · 两种方法均精确匹配，局部法有多样性与不可行状态取舍。
- **适用条件 / 局限** · 全局开销受求解难度影响。

**可复用机制** · 若拓扑一致性是硬需求，单列匹配率和生成多样性。

<a id="paper-152457"></a>

## Exact Unlearning via Quantized Sufficient Statistics

[官方论文页](https://neurips.cc/virtual/2026/poster/152457) · [作者来源](https://openreview.net/forum?id=SyxiOl962F)

- **问题 / 瓶颈** · 分片重训仍随数据规模付出代价。
- **核心创新 / 方法** · 冻结小样本训练的索引结构，对其余样本维护可加累加量。
- **Baseline** · SISA。
- **Benchmark** · 15 个视觉文本表格数据集，测精度及预期删除时间。
- **关键结果 / 消融** · 作者报告预期删除速度提高 3–645 倍，但部分数据集准确率落后。
- **适用条件 / 局限** · 删除到索引训练样本需重建，精度受量化及类数影响。

**可复用机制** · 将高频数据更新与低频结构重建分开统计延迟和精度。

<a id="paper-150163"></a>

## Example-Based Spatial Guidance for Training-Free Concept Erasure in Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150163) · [作者来源](https://openreview.net/forum?id=kCWbL63oQy)

- **问题 / 瓶颈** · 粗粒度安全二分类可能误判整体输出质量下降为成功。
- **核心创新 / 方法** · 用示例分解目标概念并进行局部抑制，同时细分评测。
- **Baseline** · 全局概念抑制和粗粒度二元评价。
- **Benchmark** · 作者所用多个安全数据集及 SD3 迁移。
- **关键结果 / 消融** · 摘要报告多概念抑制有效，幅度待核。
- **适用条件 / 局限** · 依赖示例覆盖及评判模型可靠度。

**可复用机制** · 对生成安全防护同时测子概念移除和无关内容保留。

<a id="paper-154319"></a>

## ExComm: Exploration-Stage Communication for Error-Resilient Agentic Test-Time Scaling

[官方论文页](https://neurips.cc/virtual/2026/poster/154319) · [作者来源](https://openreview.net/forum?id=EXtXoqNLl3)

- **问题 / 瓶颈** · 早期错误污染后续推理
- **核心创新 / 方法** · 定期找分支事实冲突，经工具验证后追加软反馈并分散重复轨迹
- **Baseline** · 测试时扩展与通信方法
- **Benchmark** · AIME 2024、2025 和 GAIA
- **关键结果 / 消融** · 两骨干较最强对照平均提升 5.7% 与 5.0%
- **适用条件 / 局限** · 共同犯错时冲突信号不足

**可复用机制** · 固定预算对比早期核验和末端筛选

<a id="paper-150839"></a>

## Exemplar2VQA: A Scalable Exemplar-Driven Visual Question Answering Generation Framework via Multi-Agent Coding

[官方论文页](https://neurips.cc/virtual/2026/poster/150839) · [作者来源](https://openreview.net/forum?id=evkWoqTEUD)

- **问题 / 瓶颈** · 语言模型直接合成三维问题容易算错
- **核心创新 / 方法** · 多代理从模板扩写任务，以几何工具执行得到标签
- **Baseline** · Qwen2.5-VL 3B 和 7B 微调对照细节待核
- **Benchmark** · 室内、室外及混合空间问答
- **关键结果 / 消融** · 作者报告合成室内数据改善多种设置
- **适用条件 / 局限** · 依赖仿真场景和问题模板覆盖

**可复用机制** · 让确定性程序计算标签，模型负责扩写

<a id="paper-148905"></a>

## Existence Precedes Value: Joint Modeling of Observational Existence and Evolving States in Time Series Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/148905) · [作者来源](https://openreview.net/forum?id=uIvgvH7DE2)

- **问题 / 瓶颈** · 测试时未来有效时间戳未知
- **核心创新 / 方法** · 观测流和数值流通过可靠性嵌入、依赖建模与联合输出耦合
- **Baseline** · 先插补和连续时间预测；具名对照待核
- **Benchmark** · Glimpse 自然缺失及工业数据
- **关键结果 / 消融** · 作者报告一致改善，幅度待核
- **适用条件 / 局限** · 观测机制变化需要单独验证

**可复用机制** · 用未知观测时间戳的设置测试预测器

<a id="paper-153717"></a>

## ExoC2T: An exogenous-driven spatio-temporal learning framework for cross-city transfer

[官方论文页](https://neurips.cc/virtual/2026/poster/153717) · [作者来源](https://openreview.net/forum?id=JHbypQ7cMg)

- **问题 / 瓶颈** · 目标城市缺历史流量输入
- **核心创新 / 方法** · 用外部线索建立共享机制原型，以少量证据更新城市偏差后验
- **Baseline** · 时空预测和跨城市迁移方法
- **Benchmark** · 多城市人流预测
- **关键结果 / 消融** · 作者报告稳定改善，幅度待核
- **适用条件 / 局限** · 所需目标支持数据依摘要尚不明确

**可复用机制** · 显式区分无目标序列与零目标数据

<a id="paper-155702"></a>

## Expanding Flow Maps

[官方论文页](https://neurips.cc/virtual/2026/poster/155702) · [作者来源](https://openreview.net/forum?id=3aX1lzdpqZ)

- **问题 / 瓶颈** · 固定维流映射不能直接改变序列长度
- **核心创新 / 方法** · 把流映射分成维度扩展和输运，可在离散单纯形插入 token
- **Baseline** · 固定画布流映射
- **Benchmark** · 连续与离散变长生成，数据集待核
- **关键结果 / 消融** · 固定画布是恒等扩展的特例
- **适用条件 / 局限** · 成本和质量随长度变化的实测待核

**可复用机制** · 将输出大小作为生成决策独立评估

<a id="paper-152089"></a>

## Expanding LLM Agent Boundaries with Strategy-Guided Exploration

[官方论文页](https://neurips.cc/virtual/2026/poster/152089) · [作者来源](https://openreview.net/forum?id=VaJZqNyAXo)

- **问题 / 瓶颈** · 稀疏奖励下逐动作试探效率低
- **核心创新 / 方法** · 以语言策略条件化环境动作，混合温度并从历史结果反思
- **Baseline** · 探索导向 RL 方法
- **Benchmark** · 普通 UI 操作和具身任务
- **关键结果 / 消融** · 作者报告效率和最终表现提升
- **适用条件 / 局限** · 依赖策略描述能落实为动作

**可复用机制** · 在同等任务交互预算比较策略级和动作级探索

<a id="paper-149656"></a>

## Expanding the Role of Diffusion Models for Robust Classifier Training

[官方论文页](https://neurips.cc/virtual/2026/poster/149656) · [作者来源](https://openreview.net/forum?id=oRtG25ar63)

- **问题 / 瓶颈** · 合成样本训练未利用生成器内部特征
- **核心创新 / 方法** · 对抗训练中同时使用扩散表示与生成样本，比较互补性
- **Baseline** · 仅使用合成数据的对照
- **Benchmark** · CIFAR-10、CIFAR-100 和 ImageNet
- **关键结果 / 消融** · 作者报告鲁棒性改善及表征更解耦
- **适用条件 / 局限** · 依赖扩散骨干的表示鲁棒性

**可复用机制** · 独立切换辅助特征和生成样本做消融

<a id="paper-154399"></a>

## Expected Batch Optimal Transport Plans and Consequences for Flow Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/154399) · [作者来源](https://openreview.net/forum?id=Drh2loVsgL)

- **问题 / 瓶颈** · 随机批次输运不等于全局最优输运
- **核心创新 / 方法** · 用期望批次方案描述诱导耦合并推导半离散收敛率
- **Baseline** · 精确 OT 和不同批大小
- **Benchmark** · 两原子模型及合成和图像实验
- **关键结果 / 消融** · 证明大批一致性与半离散速率
- **适用条件 / 局限** · 速率依赖半离散假设

**可复用机制** · 同时测增大批量对耦合和积分误差的影响

<a id="paper-139760"></a>

## Expected Harm: Rethinking Safety Evaluation of (Mis)Aligned LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/139760) · [作者来源](https://openreview.net/forum?id=6SIPt7cfSm)

- **问题 / 瓶颈** · 只用严重性无法反映部署风险
- **核心创新 / 方法** · 以现实可执行性作为独立的防御评估维度，并检查阶段训练是否校准
- **Baseline** · 严重性单独评分
- **Benchmark** · 模型安全评估和 Olmo-3 阶段检查
- **关键结果 / 消融** · 作者观察到拒答与现实风险错位
- **适用条件 / 局限** · 可能性估计依赖使用环境

**可复用机制** · 部署审计可按两个维度分层检查遗漏

<a id="paper-150444"></a>

## Experience Makes Skillful: Enabling Generalizable Medical Agent Reasoning via Self-Evolving Skill Memory

[官方论文页](https://neurips.cc/virtual/2026/poster/150444) · [作者来源](https://openreview.net/forum?id=i09nlt9B6r)

- **问题 / 瓶颈** · 原始轨迹冗余且可用性难估计
- **核心创新 / 方法** · 将经验结构化，按反馈更新检索价值和保留规则
- **Baseline** · 其他记忆型代理
- **Benchmark** · 临床任务的离线及在线研究评测
- **关键结果 / 消融** · 作者报告超过对照并可跨骨干迁移
- **适用条件 / 局限** · 基准表现不足以确证临床适用性

**可复用机制** · 固定模型比较原始轨迹与结构化技能库

<a id="paper-149912"></a>

## ExperiGen: Agentic Hypothesis Discovery from Observational Data

[官方论文页](https://neurips.cc/virtual/2026/poster/149912) · [作者来源](https://openreview.net/forum?id=mHGzwFfdQI)

- **问题 / 瓶颈** · 预测增益可能出自伪相关
- **核心创新 / 方法** · 两个代理分别提出假设和操作化检验，用接受与拒绝记录引导后续
- **Baseline** · 已有假设生成方法
- **Benchmark** · 19 项跨领域任务及预注册和 A/B 验证
- **关键结果 / 消融** · 显著假设数为对照的 2–4 倍；预注册 11/16 方向显著
- **适用条件 / 局限** · 观察证据不能自动证成因果

**可复用机制** · 把探索与独立验证分开并保留失败记录

<a id="paper-152852"></a>

## Expert-guided Bayesian optimization for sustainable protein formulation

[官方论文页](https://neurips.cc/virtual/2026/poster/152852) · [作者来源](https://openreview.net/forum?id=PtKZzOYrLi)

- **问题 / 瓶颈** · 高维搜索预算不足
- **核心创新 / 方法** · 专家选并扩展低维子空间，分解选择误差和优化误差
- **Baseline** · 普通与专家引导搜索
- **Benchmark** · FormulateBench 24 项植物性食品配方及两项实测
- **关键结果 / 消融** · 十轮实测效用提升 29% 和 26%
- **适用条件 / 局限** · 依赖专家能保留关键变量

**可复用机制** · 先测遗漏因素风险再分配子空间搜索预算

<a id="paper-149707"></a>

## ExpertNavigator: Functionally Coherent Expert Grouping and Pairwise-Ranked Routing for High-Fidelity Dense-to-MoE Conversion

[官方论文页](https://neurips.cc/virtual/2026/poster/149707) · [作者来源](https://openreview.net/forum?id=o3Q8xJvP0x)

- **问题 / 瓶颈** · 密集到 MoE 转换在预算约束下损失质量
- **核心创新 / 方法** · 联合功能聚类、成对排序和逐层稀疏预算
- **Baseline** · 其他 Dense-to-MoE 方法与密集模型
- **Benchmark** · 多基准的稀疏转换，名称待核
- **关键结果 / 消融** · 激活 60% FFN 参数时最高保留 97.8% 平均得分
- **适用条件 / 局限** · 实际加速依赖运行时和硬件

**可复用机制** · 固定全局激活预算比较分组及路由

<a id="paper-151817"></a>

## Explaining and Breaking the Safety-Helpfulness Ceiling via Preference Dimensional Expansion

[官方论文页](https://neurips.cc/virtual/2026/poster/151817) · [作者来源](https://openreview.net/forum?id=Xl0oQPYgSd)

- **问题 / 瓶颈** · 仅调权重可能受提示对可实现目标的限制
- **核心创新 / 方法** · 识别单奖励提示并改写为支持多维意图的提示
- **Baseline** · 顺序及同时对齐设置
- **Benchmark** · 有用、无害与真实三维奖励
- **关键结果 / 消融** · 作者报告顺序设置改善 5%–12.4%，同时设置总体奖励提高 4.6%
- **适用条件 / 局限** · 奖励改善需用独立评估确认

**可复用机制** · 先检查提示是否允许多个目标同时满足

<a id="paper-155701"></a>

## Explaining and Preventing Alignment Collapse in Iterative RLHF

[官方论文页](https://neurips.cc/virtual/2026/poster/155701) · [作者来源](https://openreview.net/forum?id=3azE5mTgC1)

- **问题 / 瓶颈** · 奖励模型从策略生成数据重新训练会造成反馈失真
- **核心创新 / 方法** · 把奖励模型演化纳入优化并用一阶近似正则
- **Baseline** · 标准迭代 RLHF
- **Benchmark** · 受控环境及 Llama-3.2-1B
- **关键结果 / 消融** · 作者报告缓解对齐崩溃，量化待核
- **适用条件 / 局限** · 依赖后续更新的近似

**可复用机制** · 同时监测当前奖励与下一轮真实偏好表现

<a id="paper-150190"></a>

## Explaining Cross-Modal Model Behavior with Gradient-Estimation-Based Feature Interaction

[官方论文页](https://neurips.cc/virtual/2026/poster/150190) · [作者来源](https://openreview.net/forum?id=k3fR86JLGj)

- **问题 / 瓶颈** · 一阶归因看不到跨模态协同
- **核心创新 / 方法** · 用代理梯度估计高阶 Shapley 交互，借助双编码器简化估计
- **Baseline** · 以固定图块为单位的跨模态解释
- **Benchmark** · CLIP 类模型的图文交互
- **关键结果 / 消融** · 作者报告可得到细粒度像素交互且保持效率
- **适用条件 / 局限** · 双编码器简化未必适用深度融合模型

**可复用机制** · 对齐任务中并列报告单特征和跨模态交互贡献

<a id="paper-156138"></a>

## Explanation Mechanism Influences Human Reliance on Reinforcement Learning Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/156138) · [作者来源](https://openreview.net/forum?id=099yUmkgyW)

- **问题 / 瓶颈** · 解释提高采纳率也可能放大过度依赖
- **核心创新 / 方法** · 在控制代理和任务时独立操纵建议最优性与解释真实性
- **Baseline** · Shapley、显著性和无解释等对照
- **Benchmark** · 100 人和 70 人的受控研究
- **关键结果 / 消融** · 奖励分解解释使恰当建议检测提高 89%，仍有过度依赖
- **适用条件 / 局限** · 研究结果可能依赖具体任务

**可复用机制** · 解释验收应分开测恰当采纳与错误采纳

<a id="paper-139691"></a>

## Explanation Multiplicity in SHAP: Characterization and Assessment

[官方论文页](https://neurips.cc/virtual/2026/poster/139691) · [作者来源](https://openreview.net/forum?id=ANaxIH1evO)

- **问题 / 瓶颈** · 同一预测的 SHAP 排名可能不稳定
- **核心创新 / 方法** · 双种子分离模型和解释器波动，再用随机空模型校准
- **Baseline** · 欧氏距离、排名指标、CTE 与确定性方法
- **Benchmark** · 多个数据集、模型及采样策略
- **关键结果 / 消融** · 小数据由模型波动主导，数据大时解释器波动主导
- **适用条件 / 局限** · 稳定替代方案可能改变估计目标

**可复用机制** · 报告排名和头部集合的分布而不只展示一次归因

<a id="paper-151711"></a>

## Explanations over Graphs: An Agent Architecture for IT Enterprise Diagnostic Tasks

[官方论文页](https://neurips.cc/virtual/2026/poster/151711) · [作者来源](https://openreview.net/forum?id=YcWFCquBYo)

- **问题 / 瓶颈** · 长证据链摘要会丢证据，诊断结果随探索顺序变化
- **核心创新 / 方法** · 模型做局部证据标注，确定性控制器管理依赖图和信念更新
- **Baseline** · ReAct 诊断代理
- **Benchmark** · ITBench 的授权运维诊断任务
- **关键结果 / 消融** · 作者报告 Majority-at-k F1 平均提高七倍
- **适用条件 / 局限** · 依赖资源图质量；不宜据单次输出自动执行修复

**可复用机制** · 以多次运行的一致正确性审核运维诊断

<a id="paper-153929"></a>

## ExpLang: Improved Exploration and Exploitation in LLM Reasoning with On-Policy Thinking Language Selection

[官方论文页](https://neurips.cc/virtual/2026/poster/153929) · [作者来源](https://openreview.net/forum?id=HaJdg0gMxD)

- **问题 / 瓶颈** · 只用英语限制推理探索。
- **核心创新 / 方法** · 将推理语言选择纳入在线策略优化的动作空间。
- **Baseline** · 英语单语训练。
- **Benchmark** · 已见与未见语言的推理和语言遵循。
- **关键结果 / 消融** · 作者报告等预算下优于英语训练，语言遵循较高。
- **适用条件 / 局限** · 语种分布与任务明细待核。

**可复用机制** · 把语言当作可学习决策，同时报告答案和语言遵循。

<a id="paper-155833"></a>

## Explicit Geometric Chain-of-Thought for Vision-Language-Action in Autonomous Driving

[官方论文页](https://neurips.cc/virtual/2026/poster/155833) · [作者来源](https://openreview.net/forum?id=2Y9nM4dnX8)

- **问题 / 瓶颈** · 二维语义缺乏驾驶所需的局部几何。
- **核心创新 / 方法** · 先定位二维决策区域，再采样几何模型的局部特征并加入生成上下文。
- **Baseline** · 端到端驾驶方案，具名对照待核。
- **Benchmark** · PlanningGrounding 与多个驾驶基准。
- **关键结果 / 消融** · 作者报告安全相关规划指标改善。
- **适用条件 / 局限** · 依赖区域定位，长尾复核待核。

**可复用机制** · 对照全图与区域几何输入并检查候选区域漏检。

<a id="paper-153676"></a>

## Exploiting Negative Multi-Cluster Structure in Class-Wise Embeddings for Weakly Supervised Multi-Label Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/153676) · [作者来源](https://openreview.net/forum?id=Jc0lO9zGdF)

- **问题 / 瓶颈** · 类级嵌入容易抹平负例内部结构。
- **核心创新 / 方法** · 跨嵌入汇总簇一致性挖正伪标签，以邻域排除找负标签，再做对比学习。
- **Baseline** · 弱监督多标签方法。
- **Benchmark** · 图像、文本及音频单标签监督。
- **关键结果 / 消融** · 作者报告平均改善 4.46%。
- **适用条件 / 局限** · 簇稳定性和指标口径待核。

**可复用机制** · 对照统一负类与保留语义子簇的弱监督。

<a id="paper-149501"></a>

## Exploiting Textual Semantics for Robust Cross-View Object Correspondence

[官方论文页](https://neurips.cc/virtual/2026/poster/149501) · [作者来源](https://openreview.net/forum?id=pfGJDSU6oL)

- **问题 / 瓶颈** · 视角变化破坏外观一致性。
- **核心创新 / 方法** · 从查询视图生成描述，并用搜索视图反复更新文本特征后融合。
- **Baseline** · 视觉对应方案，具名模型待核。
- **Benchmark** · Ego-Exo4D 与 HANDAL-X。
- **关键结果 / 消融** · 作者报告优于所比模型。
- **适用条件 / 局限** · 依赖描述事实性；遮挡影响待核。

**可复用机制** · 比较固定文本与搜索视图适配文本的对应效果。

<a id="paper-153038"></a>

## Exploration as Constrained Policy-Space Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/153038) · [作者来源](https://openreview.net/forum?id=OUryWodGWl)

- **问题 / 瓶颈** · 探索奖励后期可能与任务优势反向。
- **核心创新 / 方法** · 将探索约束写为最优传输，在经验批次上以 Sinkhorn 重加权。
- **Baseline** · 标准在线与离策略强化学习。
- **Benchmark** · 复杂连续控制任务。
- **关键结果 / 消融** · 作者报告避免所测任务性能退化。
- **适用条件 / 局限** · 度量、计算和批次敏感度待核。

**可复用机制** · 跟踪内在奖励和任务优势关联，比较固定奖励权重与动态权重。

<a id="paper-152906"></a>

## Exploration via Exploitation: The Blessing of Reward Diversity in Personalized Federated RL

[官方论文页](https://neurips.cc/virtual/2026/poster/152906) · [作者来源](https://openreview.net/forum?id=PWig4U4G3e)

- **问题 / 瓶颈** · 个性化目标被视为共享学习的障碍。
- **核心创新 / 方法** · 共享动力学与个性目标分开；利用跨代理奖励差异提供覆盖。
- **Baseline** · PF-UCBVI 与不加探索奖金的 PF-EFVI。
- **Benchmark** · 个性化联邦价值迭代理论，指标为遗憾。
- **关键结果 / 消融** · 作者证明充分奖励多样性下贪心方案可获对数遗憾。
- **适用条件 / 局限** · 依赖覆盖和共享动力学设定。

**可复用机制** · 量化合作方覆盖互补性后再决定探索预算。

<a id="paper-154772"></a>

## Exploring Lifelong Adaptation: In-Context Reinforcement Learning in Non-Stationary Environments

[官方论文页](https://neurips.cc/virtual/2026/poster/154772) · [作者来源](https://openreview.net/forum?id=B4sdRfOm1V)

- **问题 / 瓶颈** · 固定动力学掩盖终身适应失效。
- **核心创新 / 方法** · 交叉比较平稳与非平稳训练、序列骨干和交互规模。
- **Baseline** · 域随机化、平稳、非平稳及分阶段训练。
- **Benchmark** · 离散符号任务与连续控制。
- **关键结果 / 消融** · 作者报告三个因素共同影响适应，分项幅度待核。
- **适用条件 / 局限** · 外推依赖漂移类型。

**可复用机制** · 固定交互数分别评测突然切换和缓慢漂移。

<a id="paper-151074"></a>

## Exploring MLLM-Diffusion Information Transfer with MetaCanvas

[官方论文页](https://neurips.cc/virtual/2026/poster/151074) · [作者来源](https://openreview.net/forum?id=d8GC1xLs92)

- **问题 / 瓶颈** · 全局条件难传递布局和属性绑定。
- **核心创新 / 方法** · 把多模态表示组织为空间索引画布并逐块残差融合。
- **Baseline** · 匹配设置的全局条件及专用闭源系统。
- **Benchmark** · 三个扩散底座、六项生成和编辑任务。
- **关键结果 / 消融** · 作者报告一致改善，具体幅度待核。
- **适用条件 / 局限** · 依赖空间索引质量。

**可复用机制** · 在同一生成器比较逐块与全局条件的布局遵循。

<a id="paper-153018"></a>

## Exploring Multi-Order Self-Similarity for Motion Understanding

[官方论文页](https://neurips.cc/virtual/2026/poster/153018) · [作者来源](https://openreview.net/forum?id=ObEzynFfiu)

- **问题 / 瓶颈** · 单一阶对应难表达多层次动态。
- **核心创新 / 方法** · 用轻量模块学习并整合多阶时空自相似特征。
- **Baseline** · 所比视频模型，具名对照待核。
- **Benchmark** · 动作识别、运动问答和机器人任务。
- **关键结果 / 消融** · 作者报告多类任务改善且额外开销较小。
- **适用条件 / 局限** · 边际开销和逐阶贡献待核。

**可复用机制** · 对不同运动任务在同预算下消融自相似阶数。

<a id="paper-148417"></a>

## Exploring Starts Are Not Enough: Counterexamples and a Fix for Monte Carlo Exploring Starts

[官方论文页](https://neurips.cc/virtual/2026/poster/148417) · [作者来源](https://openreview.net/forum?id=xyHNYFTjvc)

- **问题 / 瓶颈** · 探索起点仍可能收敛到次优固定点。
- **核心创新 / 方法** · 构造两类更新反例，并在初始访问设置按状态反向缩放更新频率。
- **Baseline** · 样本均值初始访问和首次访问 MCES。
- **Benchmark** · 表格理论，以最优收敛为判据。
- **关键结果 / 消融** · 两版本均有反例；初始访问修正具收敛保证。
- **适用条件 / 局限** · 函数逼近不自动继承表格证明。

**可复用机制** · 同时监控更新频率与步长，而非仅检查探索覆盖。

<a id="paper-155882"></a>

## Exploring the Epipolar Consistency for Light Field Deraining

[官方论文页](https://neurips.cc/virtual/2026/poster/155882) · [作者来源](https://openreview.net/forum?id=28qDxfgwC0)

- **问题 / 瓶颈** · 雨丝导致深度估计和视角对齐误差。
- **核心创新 / 方法** · 沿极线汇总一致性图，按图采样干净背景区域的冗余特征。
- **Baseline** · 依赖预测深度与直接映射的方法。
- **Benchmark** · 光场去雨数据和真实场景。
- **关键结果 / 消融** · 作者报告恢复改善，具体幅度待核。
- **适用条件 / 局限** · 依赖多视角冗余和极线几何。

**可复用机制** · 比较基于深度的对齐与直接按极线一致性选择证据。

<a id="paper-156760"></a>

## Exploring the Limitations of Layer Synchronization in Spiking Neural Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/156760) · [作者来源](https://neurips.cc/virtual/2026/poster/156760)

- **问题 / 瓶颈** · 同步训练模型直接异步执行会失配。
- **核心创新 / 方法** · 在反传中纳入异步调度，比较两种执行策略。
- **Baseline** · 同步训练和同步执行方案。
- **Benchmark** · 含时空信息的数据集，测脉冲数、延迟、精度。
- **关键结果 / 消融** · 作者报告最高少 50% 脉冲、推理快 2 倍、精度高 10%。
- **适用条件 / 局限** · 结果依赖调度、硬件和任务。

**可复用机制** · 对照训练与运行调度匹配和不匹配的效率与质量。

<a id="paper-139255"></a>

## Exploring the Limits of Compositional Generalization in Vision-Language-Action Manipulation

[官方论文页](https://neurips.cc/virtual/2026/poster/139255) · [作者来源](https://openreview.net/forum?id=bqpIkP9Yfq)

- **问题 / 瓶颈** · 孤立技能成功并不保证顺序执行。
- **核心创新 / 方法** · RoboCombine 用模块式执行拆开规划、触发和策略，扩展原子技能起始位姿。
- **Baseline** · 完整指令训练和未扩展起始状态的层级执行。
- **Benchmark** · RoboCombine，测顺序成功和转移成功。
- **关键结果 / 消融** · 在预知切换时机的层级执行下两指标分别从 2.11% 到 26.32%、2.63% 到 60.53%。
- **适用条件 / 局限** · 预知时机结果不能直接外推到自主切换。

**可复用机制** · 分离切换选择和下游策略在交接状态上的可执行性。

<a id="paper-155704"></a>

## Exponential Map Models as an Interpretable Framework for Generating Neural Spatial Representations

[官方论文页](https://neurips.cc/virtual/2026/poster/155704) · [作者来源](https://openreview.net/forum?id=3ZO4NGunEr)

- **问题 / 瓶颈** · 训练出的空间表征难解释路径不变性的来源。
- **核心创新 / 方法** · 以指数映射连接位置和表征，分析生成元交换和反对称性。
- **Baseline** · 经验优化与显式正则化空间表征。
- **Benchmark** · 路径积分、平移相似性及空间度量的理论推导。
- **关键结果 / 消融** · 作者给出交换性和反对称性对应的几何性质。
- **适用条件 / 局限** · 具体神经数据验证待核。

**可复用机制** · 先定义表征随空间变换应满足的代数性质，再决定训练约束。

<a id="paper-152775"></a>

## Exposing and Mitigating Temporal Attack in Deepfake Video Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/152775) · [作者来源](https://openreview.net/forum?id=QSc3qGboAK)

- **问题 / 瓶颈** · 常规高 AUC 可掩盖脆弱的时序捷径。
- **核心创新 / 方法** · 训练时压制不稳定统计并保留可靠运动特征。
- **Baseline** · 常用深伪检测模型。
- **Benchmark** · 公开视频基准与鲁棒评测。
- **关键结果 / 消融** · 作者报告所测扰动下较最强对照 AUC 高 21.30%，单位待核。
- **适用条件 / 局限** · 真实部署中的鲁棒边界待核。

**可复用机制** · 把干净性能和跨分布稳定性作为两个验收项。

<a id="paper-149220"></a>

## Exposing the Illusion of Erasure in Knowledge Editing for LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/149220) · [作者来源](https://openreview.net/forum?id=s0R5gl7GcP)

- **问题 / 瓶颈** · 编辑后常规测试通过不能证明旧知识消失。
- **核心创新 / 方法** · 对低秩编辑做表征和损失几何分析。
- **Baseline** · 主流知识编辑方法及不同架构。
- **Benchmark** · 模型知识编辑与保留诊断，数据集指标待核。
- **关键结果 / 消融** · 作者报告旧知识可持续存在，低秩改变更接近抑制而非删除。
- **适用条件 / 局限** · 只覆盖所测编辑器，不能普遍推断其他方法。

**可复用机制** · 对有遗忘要求的系统增加独立残留审计，分别报告表达与表征证据。

<a id="paper-152909"></a>

## Expressive Power of Deep Homomorphism Networks over Relational Databases

[官方论文页](https://neurips.cc/virtual/2026/poster/152909) · [作者来源](https://openreview.net/forum?id=PUkMW1q30n)

- **问题 / 瓶颈** · 消息传递难表达部分关系查询
- **核心创新 / 方法** · 将同态网络的 max、sum、mean 聚合与一阶逻辑片段对应
- **Baseline** · 消息传递 GNN 与不同聚合
- **Benchmark** · 关系数据库和 SQL 合取查询的理论设定
- **关键结果 / 消融** · 给出计数、比例量词等表达关系，并研究静态分析
- **适用条件 / 局限** · 结论对应特定逻辑片段

**可复用机制** · 用需要表达的查询性质检查聚合器能否区分目标实例。

<a id="paper-149745"></a>

## Express Language Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/149745) · [作者来源](https://openreview.net/forum?id=nf2SQeKcr9)

- **问题 / 瓶颈** · 双向注意力的近似保证不能直接用于因果解码
- **核心创新 / 方法** · Express 将非因果注意力近似转为带保证的因果近似，并结合 Thinformer
- **Baseline** · Thinformer 与 FlashAttention 2
- **Benchmark** · 长上下文预填充、KV 压缩和长文本解码
- **关键结果 / 消融** · 长度 n 时误差为 log(n) 的 1.5 次方除以 s，内存 O(s)，报告实现加速
- **适用条件 / 局限** · 常数和硬件适用范围待核

**可复用机制** · 复用现有注意力近似时，分别验证因果保证和实际 I/O。

<a id="paper-154489"></a>

## ExpRFT: Exponential Reward-Weighted Fine-Tuning for Offline RL in Multi-Turn Dialogue

[官方论文页](https://neurips.cc/virtual/2026/poster/154489) · [作者来源](https://openreview.net/forum?id=DE0tMV3YZo)

- **问题 / 瓶颈** · 中心化仿射奖励加权可使损失无下界
- **核心创新 / 方法** · 对标准化优势做温度可调的指数加权
- **Baseline** · 仿射奖励加权 SFT 与 AWR 的设计比较
- **Benchmark** · 六项多轮对话基准
- **关键结果 / 消融** · 得到有良好定义的损失及噪声控制参数，量化待核
- **适用条件 / 局限** · 温度和优势标准化依赖奖励分布

**可复用机制** · 对离线轨迹加权方法同时扫描奖励噪声与温度。

<a id="paper-149316"></a>

## Extended Wasserstein-GAN Approach to Causal Distribution Learning: Density-Free Estimation and Minimax Optimality

[官方论文页](https://neurips.cc/virtual/2026/poster/149316) · [作者来源](https://openreview.net/forum?id=r59bGWg9jN)

- **问题 / 瓶颈** · 密度比估计不稳定，目标可能偏离可识别因果量
- **核心创新 / 方法** · 定义条件干预分布并训练 GAN 最小化平均 Wasserstein 风险
- **Baseline** · 依赖密度估计的反事实生成方法
- **Benchmark** · 条件干预分布估计及极小极大分析
- **关键结果 / 消融** · 建立极小极大最优性，具体速率待核
- **适用条件 / 局限** · 依赖识别条件，不能仅凭生成质量推出因果有效性

**可复用机制** · 在建模尾部风险时将训练风险与可识别分布目标对齐。

<a id="paper-156110"></a>

## Extending 3D Reconstruction Models to Any Camera

[官方论文页](https://neurips.cc/virtual/2026/poster/156110) · [作者来源](https://openreview.net/forum?id=0K6xev69k8)

- **问题 / 瓶颈** · 透视预训练模型在鱼眼与全景图像上失效
- **核心创新 / 方法** · 以低秩适配接入非针孔相机
- **Baseline** · 原透视预训练模型
- **Benchmark** · 鱼眼、全景和原始透视重建
- **关键结果 / 消融** · 增加约 0.1% 参数，报告保留原透视表现
- **适用条件 / 局限** · 证据限所测模型与相机族

**可复用机制** · 适配传感器时，把旧传感器表现纳入回归测试。

<a id="paper-151268"></a>

## Extending Myerson's Optimal Auctions to Correlated Bidders via Neural Network Interpolation

[官方论文页](https://neurips.cc/virtual/2026/poster/151268) · [作者来源](https://openreview.net/forum?id=beJTn29hNA)

- **问题 / 瓶颈** · 相关竞标者下贪心分配可能不单调
- **核心创新 / 方法** · 神经插值生成分配，再验证并修复以保证策略真实
- **Baseline** · Myerson 贪心分配及收入参考
- **Benchmark** · 单物品拍卖，多类估值分布，测收入与真实性
- **关键结果 / 消融** · 作者报告近最优收入并验证真实性
- **适用条件 / 局限** · 不等同于一般近似最优保证

**可复用机制** · 在硬约束的学习决策中将收益优化与可验证可行性分开检查。

<a id="paper-150095"></a>

## Extending Pretrained 10-Second ECG Foundation Models to Longer Horizons

[官方论文页](https://neurips.cc/virtual/2026/poster/150095) · [作者来源](https://openreview.net/forum?id=kk9jN1duEy)

- **问题 / 瓶颈** · 固定 10 秒心电模型缺少长窗聚合
- **核心创新 / 方法** · 用轻量插件接收变长输入并进行语义时序建模
- **Baseline** · 冻结短窗 ECG 基础模型
- **Benchmark** · 多种长程 ECG 任务、数据与骨干
- **关键结果 / 消融** · 报告长窗适配有效，幅度待核
- **适用条件 / 局限** · 限回顾性信号建模，临床外推待验证

**可复用机制** · 延长短窗时序模型时，对比简单聚合和跨窗语义模块。

<a id="paper-150218"></a>

## Extending ROC Analysis to Uncertainty-Aware Risk Prediction with an Interval-Based AUC (iAUC)

[官方论文页](https://neurips.cc/virtual/2026/poster/150218) · [作者来源](https://openreview.net/forum?id=jsG2UV3YqP)

- **问题 / 瓶颈** · 普通 AUC 无法反映区间重叠
- **核心创新 / 方法** · 以两条 ROC 式曲线分解正负样本排序
- **Baseline** · 点预测 ROC 与 AUC
- **Benchmark** · 区间风险预测的排序与类条件覆盖
- **关键结果 / 消融** · 在有效覆盖下给出最优 AUC 的界
- **适用条件 / 局限** · 理论依赖类条件覆盖

**可复用机制** · 联合报告区间覆盖和排序可信度。

<a id="paper-150273"></a>

## Externalized CPDAG Summaries Improve LLM Causal Deduction

[官方论文页](https://neurips.cc/virtual/2026/poster/150273) · [作者来源](https://openreview.net/forum?id=jNkJv4Cfma)

- **问题 / 瓶颈** · 自由推理容易用局部模式替代等价类判断
- **核心创新 / 方法** · 先生成带类型的 CPDAG 摘要，再依据结构回答
- **Baseline** · PC 指令基线及无结构双轮文本
- **Benchmark** · Corr2Cause、改写分布外测试
- **关键结果 / 消融** · Qwen3.5-27B 主实验 Yes F1 从 73.0 到 86.4
- **适用条件 / 局限** · 结构生成错误仍会传给第二轮

**可复用机制** · 比较结构中介和等轮次自由文本，并扰动结构验证依赖。

<a id="paper-155982"></a>

## Extracting Governing Equations from Latent Dynamics via Multi-View Contrastive Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/155982) · [作者来源](https://openreview.net/forum?id=1NoGYV3xUP)

- **问题 / 瓶颈** · 噪声和非线性观测使潜状态难辨识
- **核心创新 / 方法** · 时间对比学习联合恢复轨迹和动力学，以结构化基函数拟合方程
- **Baseline** · 既有潜动态辨识理论，实验对照待核
- **Benchmark** · 混沌、振荡和亚稳态及高斯和泊松噪声
- **关键结果 / 消融** · 理论辨识至仿射不定性，报告轨迹和流场恢复
- **适用条件 / 局限** · 需要共享过程的独立噪声视图

**可复用机制** · 结合多视图对齐与显式动力学基，并检查坐标不确定性。

<a id="paper-154324"></a>

## Extracting Search Trees from LLM Reasoning Traces Reveals Myopic Planning

[官方论文页](https://neurips.cc/virtual/2026/poster/154324) · [作者来源](https://openreview.net/forum?id=EWoL9QIbhS)

- **问题 / 瓶颈** · 长推理痕迹不直接证明深规划
- **核心创新 / 方法** · 从四连棋推理抽取搜索树、拟合认知模型并剪除部分文字做干预
- **Baseline** · 人类搜索与不同深度决策模型
- **Benchmark** · 四连棋，测树宽深和行动选择
- **关键结果 / 消融** · 宽度较能预测表现，动作更符合忽略深节点的模型
- **适用条件 / 局限** · 仅验证所测棋类与模型

**可复用机制** · 比较深层文字的存在和对选择的实际作用。

<a id="paper-150343"></a>

## Extraneous Cognitive Load in Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150343) · [作者来源](https://openreview.net/forum?id=iqBkP1UEL0)

- **问题 / 瓶颈** · 题目难度和表述开销通常混杂
- **核心创新 / 方法** · 控制五种呈现因素，以激活分数估计额外负荷
- **Baseline** · 同题不同呈现条件
- **Benchmark** · CogLoadBench 三类推理任务
- **关键结果 / 消融** · 额外负荷常降低准确率，报告激活分数可跨任务泛化
- **适用条件 / 局限** · 受所测模型与模板影响

**可复用机制** · 固定语义难度构造呈现对照，检查准确率下降来自何处。

<a id="paper-154246"></a>

## ExtrapAir: Air Quality Inference at Unmonitored Locations via Weather-Bridged Spatial Attention

[官方论文页](https://neurips.cc/virtual/2026/poster/154246) · [作者来源](https://openreview.net/forum?id=FBdLg0pxh3)

- **问题 / 瓶颈** · 常规模型依赖待预测站点的历史记录
- **核心创新 / 方法** · 逐变量编码天气，以地理和语义先验引导非竞争空间聚合
- **Baseline** · 32 个对照
- **Benchmark** · 五套真实空气质量数据，测 MAE
- **关键结果 / 消融** · 作者报告总体 MAE 最多降低 15.24%
- **适用条件 / 局限** · 新地区的天气观测质量影响迁移

**可复用机制** · 用整站留出验证无历史预测，并与只利用近邻空间的模型对照。

<a id="paper-151744"></a>

## Extrapolative Weight Averaging Reveals Correctness–Efficiency Frontiers in Code RL

[官方论文页](https://neurips.cc/virtual/2026/poster/151744) · [作者来源](https://openreview.net/forum?id=YRDiKZgtA9)

- **问题 / 瓶颈** · 测试覆盖变化对代码性能有相反影响
- **核心创新 / 方法** · 在不同嵌套单测覆盖上训练共享初始化检查点，再沿权重方向插值或外推
- **Baseline** · 训练端点及插值
- **Benchmark** · 竞赛编程隐藏测试、时限及内存限制
- **关键结果 / 消融** · 报告外推扩展已训练端点间的前沿，高覆盖减少优化失败但增加正确性失败
- **适用条件 / 局限** · 依赖共享初始化及具体单测分布

**可复用机制** · 对不同奖励训练的模型分别统计失败类型，再检验权重外推。

<a id="paper-149109"></a>

## ExtraVAR: Stage-Aware RoPE Remapping for Resolution Extrapolation in Visual Autoregressive Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149109) · [作者来源](https://openreview.net/forum?id=spQoCaKIYY)

- **问题 / 瓶颈** · 视觉自回归跨分辨率时出现全局或局部重复与细节退化
- **核心创新 / 方法** · 将不同尺度阶段与主导频带匹配，分别调整映射
- **Baseline** · 直接迁移语言或扩散模型外推方式
- **Benchmark** · 视觉自回归高分辨率生成
- **关键结果 / 消融** · 作者报告抑制三类故障，量化待核
- **适用条件 / 局限** · 依赖粗到细尺度组织

**可复用机制** · 为每个阶段检查位置编码的敏感频带，分别测重复与细节误差。

<a id="paper-153894"></a>

## Extremely Sparse-View Computed Tomography from 2D Projections via Pose-Aware Diffusion Priors

[官方论文页](https://neurips.cc/virtual/2026/poster/153894) · [作者来源](https://openreview.net/forum?id=HvYYOiRYrE)

- **问题 / 瓶颈** · 训练与推理均稀疏时缺少高质量三维真值
- **核心创新 / 方法** · 从单幅二维投影学习位姿感知先验，采样时约束观测一致性和投影物理
- **Baseline** · 稀疏优化与学习式重建
- **Benchmark** · 两套公开 CT 数据的一、四、八视图设置
- **关键结果 / 消融** · 新视角质量最佳，重建相当或更好
- **适用条件 / 局限** · 不直接支持临床部署，依赖成像几何

**可复用机制** · 缺少三维训练标签时，在多个投影视图间施加共享潜体一致性。

<a id="paper-139675"></a>

## Eyes on VLM: Benchmarking Gaze Following and Social Gaze Prediction in Vision Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139675) · [作者来源](https://openreview.net/forum?id=BAw8E27N8g)

- **问题 / 瓶颈** · 单一注视任务混淆空间定位与社会关系推理
- **核心创新 / 方法** · 构建两类任务并跨视觉语言模型比较
- **Baseline** · 多种 VLM，名称待核
- **Benchmark** · EyeVLM 的注视跟随和社会注视预测
- **关键结果 / 消融** · 摘要提出系统评测，两类任务量化差异待全文核
- **适用条件 / 局限** · 场景人群和视线标注限制外推

**可复用机制** · 在复杂感知评测中先区分局部几何与关系推理。

<a id="paper-150550"></a>

## F2G-Pose: Geometry-Aware Foundation Feature Lifting for Direct RGB-D Category-Level Object Pose Estimation

[官方论文页](https://neurips.cc/virtual/2026/poster/150550) · [作者来源](https://openreview.net/forum?id=hJJz7BT9Hr)

- **问题 / 瓶颈** · 类别内部差异和遮挡增加位姿歧义
- **核心创新 / 方法** · 将视觉特征提升至点云，以局部编码和专家模型联合预测姿态尺寸和形状
- **Baseline** · 确定式和扩散式方法
- **Benchmark** · 只用合成 SOPE 训练，评估类别级 RGB-D 位姿
- **关键结果 / 消融** · 作者报告单次前向得到实时输出，量化对比待核
- **适用条件 / 局限** · 需要深度数据，合成至真实差异待核

**可复用机制** · 比较直接回归与有辅助形状约束的回归，并分开测遮挡与延时。

<a id="paper-139472"></a>

## FACBench: A Benchmark for Formal-Anchor Collisions in Multilingual Mathematical Grounding

[官方论文页](https://neurips.cc/virtual/2026/poster/139472) · [作者来源](https://openreview.net/forum?id=NpetAmYjE2)

- **问题 / 瓶颈** · 多语言别名提高召回但可能让错误概念排第一
- **核心创新 / 方法** · 构造五语言概念冲突查询及 Mathlib 图压力测试，并使用来源与上下文规则
- **Baseline** · 朴素多语言别名合并
- **Benchmark** · FACBench 的冲突查询、图挖掘留出及类定理探针
- **关键结果 / 消融** · 规则使两个受控设置 top-1 提高约 11 和 28 个百分点
- **适用条件 / 局限** · 受控收益不能直接外推到完整证明

**可复用机制** · 将正确候选是否出现与其是否排首分别计量。

<a id="paper-152471"></a>

## Face Deepfake-aware Recovery via Semantic-driven Facial Representation-based Watermarking

[官方论文页](https://neurips.cc/virtual/2026/poster/152471) · [作者来源](https://openreview.net/forum?id=SqHbIQuLi6)

- **问题 / 瓶颈** · 空间对齐误差影响水印恢复
- **核心创新 / 方法** · 分组件编码语义潜变量，解码后重建身份一致内容
- **Baseline** · 已有图像水印
- **Benchmark** · CelebA-HQ、FFHQ 的恢复和提取
- **关键结果 / 消融** · 作者报告在光度及几何扰动下改善身份保持与提取
- **适用条件 / 局限** · 验证限所测人脸及扰动

**可复用机制** · 把需恢复的内容编码在独立语义通道中，再定义几何扰动恢复测试。

<a id="paper-152285"></a>

## FacEDiT: Talking Head Video Editing via Facial Motion Infilling

[官方论文页](https://neurips.cc/virtual/2026/poster/152285) · [作者来源](https://openreview.net/forum?id=UDOhx8aiSo)

- **问题 / 瓶颈** · 同人同场景局部台词变化的配对视频难获得
- **核心创新 / 方法** · 掩蔽局部脸部运动，结合语音与边界上下文重建，并加局部时间偏置和连续性正则
- **Baseline** · 语音驱动生成和唇同步路线；具名对照待核
- **Benchmark** · 局部插入删除与替换，评估同步、身份和边界
- **关键结果 / 消融** · 摘要提出局部运动补全验证；量化数值待核
- **适用条件 / 局限** · 训练遮挡与实际编辑的时长和运动分布可能不同

**可复用机制** · 对难收集编辑配对的时序任务，从普通序列模拟局部缺失并保留边界作为条件。

<a id="paper-150724"></a>

## FacePhys: State of the Heart Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/150724) · [作者来源](https://openreview.net/forum?id=ftGKpah4gM)

- **问题 / 瓶颈** · 压缩与端侧计算预算限制相机心率测量
- **核心创新 / 方法** · 采用时空状态空间对偶，跨帧传递心动状态
- **Baseline** · 既有远程光电容积脉搏波估计
- **Benchmark** · 跨数据集误差、内存和逐帧时延；具名数据待核
- **关键结果 / 消融** · 作者报告误差降低 49%，内存 3.6 MB，逐帧 9.46 ms
- **适用条件 / 局限** · 摘要未证明临床用途或跨设备统一时延

**可复用机制** · 在端侧测周期信号时对照历史状态和滑窗，分别测压缩鲁棒性与资源成本。

<a id="paper-155525"></a>

## FaceProbe: Recovering HDR Environment Map via Masked Diffusion and Physical Preference

[官方论文页](https://neurips.cc/virtual/2026/poster/155525) · [作者来源](https://openreview.net/forum?id=4wUS85pd1H)

- **问题 / 瓶颈** · 单张肖像推断全方向光照多解
- **核心创新 / 方法** · 扩散补全结合肖像结构及外围线索，以渲染一致性反馈对齐光照
- **Baseline** · 传统人脸反射和生成式全景方法
- **Benchmark** · 360 度 HDR 环境恢复；数据与指标待核
- **关键结果 / 消融** · 作者报告改善清晰度和光照一致性，量化对照待核
- **适用条件 / 局限** · 依赖可见背景与反射线索，遮挡光源仍有歧义

**可复用机制** · 对不完整逆问题将已观测区域固定，并用物理后果评价补全。

<a id="paper-154063"></a>

## FACETS: Cross-Granularity Vision--Language Modeling for 3D Anomaly Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/154063) · [作者来源](https://openreview.net/forum?id=GU2KPq4O7s)

- **问题 / 瓶颈** · 粗几何或纯视觉分数难定位细小缺陷
- **核心创新 / 方法** · 联合语言语义与几何显著性，在点和块两种粒度推理
- **Baseline** · 重建误差和正常样本记忆库路线
- **Benchmark** · 三维多类别质量检测；具名数据与指标待核
- **关键结果 / 消融** · 作者报告统一多类别检测，数值待核
- **适用条件 / 局限** · 依赖点质量与缺陷描述；遮挡条件的独立消融待核

**可复用机制** · 选三维异常模型时对照是否保留点级证据，分开测对象检出与点级定位。

<a id="paper-148617"></a>

## Factor Augmented High-Dimensional SGD

[官方论文页](https://neurips.cc/virtual/2026/poster/148617) · [作者来源](https://openreview.net/forum?id=wPsFSiDXLS)

- **问题 / 瓶颈** · 传统离线降维需保存全量数据
- **核心创新 / 方法** · 在线估计因子后迭代更新，分析递减步长与小批量下的矩收敛
- **Baseline** · 标准 SGD 与离线两阶段降维
- **Benchmark** · 高维流式理论设定，考察范数内的矩收敛
- **关键结果 / 消融** · 作者给出计入因子误差的收敛分析；经验幅度待核
- **适用条件 / 局限** · 需潜因子结构，具体假设待查正文

**可复用机制** · 在线降维和优化并行时，在收敛分析中为表征误差单独记账。

<a id="paper-156135"></a>

## Factored Generative Models through Mechanism Diversity

[官方论文页](https://neurips.cc/virtual/2026/poster/156135) · [作者来源](https://openreview.net/forum?id=09pkPpF5MG)

- **问题 / 瓶颈** · 只约束潜分布可能不适合先验固定的条件生成器
- **核心创新 / 方法** · 证明足够的机制多样性可带来可辨识性，提出生成器雅可比对比目标
- **Baseline** · 潜分布约束及稀疏等正则路线
- **Benchmark** · 潜在扩散模型上的三项概念解耦基准
- **关键结果 / 消融** · 作者报告概念解耦改善；各项幅度待核
- **适用条件 / 局限** · 理论依赖条件对机制有充分变化，雅可比成本需评估

**可复用机制** · 当条件改变映射而不改变先验时，以机制干预检查潜因素是否独立。

<a id="paper-149013"></a>

## Factorized Gradients for Scalable Highly-expressive Parametric Diffeomorphisms

[官方论文页](https://neurips.cc/virtual/2026/poster/149013) · [作者来源](https://openreview.net/forum?id=tTrgBMBN77)

- **问题 / 瓶颈** · 分片仿射速度下直接求参数梯度代价随点数和参数维数相乘增长
- **核心创新 / 方法** · 先积分轨迹，再投影至参数空间求因子化梯度
- **Baseline** · 传统 CPAB 梯度计算
- **Benchmark** · 分片仿射微分同胚，比较时间复杂度；实测细节待核
- **关键结果 / 消融** · 作者给出从 O(dTN) 到 O(TN+dC) 的复杂度
- **适用条件 / 局限** · 依赖分片网格结构；常数开销和适用规模待核

**可复用机制** · 求解同一轨迹的大量参数导数时，检查能否共享积分再批量投影。

<a id="paper-155234"></a>

## FactorizedHMR: A Hybrid Framework for Video Human Mesh Recovery

[官方论文页](https://neurips.cc/virtual/2026/poster/155234) · [作者来源](https://openreview.net/forum?id=7ERjBgSwbw)

- **问题 / 瓶颈** · 遮挡下肢体姿态多解，确定性平均会失真
- **核心创新 / 方法** · 先回归躯干与根，再用流匹配补全其余关节，加入几何监督
- **Baseline** · 强人体网格恢复基线；具名方法待核
- **Benchmark** · 相机和世界坐标下的视频人体网格基准
- **关键结果 / 消融** · 作者报告关节恢复和漂移改善，模糊场景更明显
- **适用条件 / 局限** · 稳定锚点若误估会向补全传播

**可复用机制** · 对不均匀不确定度的结构化目标，分开确定性锚定和概率补全。

<a id="paper-149827"></a>

## Factorized Self-Supervised Speech Tokenization

[官方论文页](https://neurips.cc/virtual/2026/poster/149827) · [作者来源](https://openreview.net/forum?id=n0PEFDbLxC)

- **问题 / 瓶颈** · 离散单元容易把静态因素混入随时间变化的内容
- **核心创新 / 方法** · 扩展线性因子分解以覆盖未见说话者，再对动态分量聚类并解码重建
- **Baseline** · 已有语音分词与未分解特征；具体方法待核
- **Benchmark** · 噪声下 token 稳定性、语音合成、转换和建模
- **关键结果 / 消融** · 作者报告稳定性及合成改善，其他任务有竞争力
- **适用条件 / 局限** · 依赖静态动态因素可分；说话人数量影响估计

**可复用机制** · 要稳定编码时变信号，先分出片段级不变量并分别测试重建和噪声稳定度。

<a id="paper-149364"></a>

## Factorized Spectral Representations for Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149364) · [作者来源](https://openreview.net/forum?id=qZTX18AAiX)

- **问题 / 瓶颈** · 将状态动作合并会限制复用，并扩大表征假设类
- **核心创新 / 方法** · 以噪声对比目标拟合 CP 分解，训练三个编码器
- **Baseline** · 矩阵式转移谱表示
- **Benchmark** · 连续控制及执行器变化迁移
- **关键结果 / 消融** · 作者给出样本复杂度改善并报告高维运动收益；迁移仅重训动作编码器
- **适用条件 / 局限** · 动态需近似可分解，否则低秩偏差可能增大

**可复用机制** · 执行器独立改变的任务可优先测试分离状态与动作的动力学编码。

<a id="paper-153530"></a>

## Facts Don't Speak Louder than Words: The Behavioral Essence of Long-CoT Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/153530) · [作者来源](https://openreview.net/forum?id=KeTJLE21Jz)

- **问题 / 瓶颈** · 拒绝采样默认正确轨迹和广覆盖不可或缺
- **核心创新 / 方法** · 比较错误轨迹、受限提示和仅已掌握问题的蒸馏
- **Baseline** · 标准长思维链蒸馏及不同损失
- **Benchmark** · 语言模型推理任务；具名基准待核
- **关键结果 / 消融** · 作者观察到错误轨迹或窄提示仍可带来接近收益，交叉熵支持复杂模式
- **适用条件 / 局限** · 不应外推为任意错误数据可用；分布条件待核

**可复用机制** · 用已掌握题目隔离行为迁移，再和新增知识数据做等预算比较。

<a id="paper-152324"></a>

## Factual recall in linear associative memories: sharp asymptotics and mechanistic insights

[官方论文页](https://neurips.cc/virtual/2026/poster/152324) · [作者来源](https://openreview.net/forum?id=Tv6Zf9bZKi)

- **问题 / 瓶颈** · 关联检索约束彼此耦合，不能直接套分类容量
- **核心创新 / 方法** · 分析独立竞争目标的解耦线性模型，并对照原模型
- **Baseline** · 单层原始线性关联记忆与解耦模型
- **Benchmark** · 理论容量、权重谱与数值验证
- **关键结果 / 消融** · 临界容量满足 p log p / d² = 1/2；另分析线性两层
- **适用条件 / 局限** · 结果属于理想化线性模型，不能直接外推实际语言模型

**可复用机制** · 衡量记忆容量时用全部候选竞争，并报告维度和关联量的关系。

<a id="paper-149903"></a>

## FADE: Fractional Anomalous Dynamics Extrapolation for Training-Free Diffusion Transformers Acceleration

[官方论文页](https://neurips.cc/virtual/2026/poster/149903) · [作者来源](https://openreview.net/forum?id=mM9yiKjZ8m)

- **问题 / 瓶颈** · 静态整数阶外推在弯曲非平稳轨迹上易积累误差
- **核心创新 / 方法** · 用 Mittag–Leffler 分数阶算子建模，并从跨样本统计构造查找表
- **Baseline** · 整数阶或复用型特征缓存
- **Benchmark** · 扩散 Transformer 推理延迟与生成质量；具名配置待核
- **关键结果 / 消融** · 作者提出免训练加速，量化幅度待核
- **适用条件 / 局限** · 依赖估计动态跨样本稳定；模型变化时需重新校准

**可复用机制** · 缓存策略应按步骤检验曲率及误差，比较同预算下的生成质量。

<a id="paper-149405"></a>

## Fail-Closed Alignment for Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149405) · [作者来源](https://openreview.net/forum?id=qJN2JFwGdt)

- **问题 / 瓶颈** · 单一路径失灵即可使拒绝不稳
- **核心创新 / 方法** · 渐进训练冗余安全表示，用防御验收确认路径独立性
- **Baseline** · 现有对齐；具名对照待核
- **Benchmark** · 六种安全压力评估与拒绝质量
- **关键结果 / 消融** · 作者报告平均不安全响应成功率 1.7%，质量大体保持
- **适用条件 / 局限** · 结果限所测模型及安全测试集

**可复用机制** · 用独立防御路径做容错验收，同时统计过度拒绝。

<a id="paper-155737"></a>

## Failing Forward: Adaptive Failure-Informed Learning for Vision-Language-Action Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155737) · [作者来源](https://openreview.net/forum?id=3Kqyrxf0U4)

- **问题 / 瓶颈** · 只克隆成功示范缺少纠错信号
- **核心创新 / 方法** · 共享视觉语言骨干，分开成功与失败动作生成器，按逐步分布距离调节引导
- **Baseline** · 仅成功行为克隆及既有 VLA
- **Benchmark** · 域内域外短程与长程操作；细项待核
- **关键结果 / 消融** · 作者报告失败感知训练收益，具体幅度待核
- **适用条件 / 局限** · 依赖失败样本代表部署偏移，负向引导过强或排斥有效动作

**可复用机制** · 训练动作生成时记录失败分布，核查自适应负引导是否比固定权重更稳。

<a id="paper-152161"></a>

## Failing to Falsify: Evaluating and Mitigating Confirmation Bias in Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152161) · [作者来源](https://openreview.net/forum?id=V3hfvlipsD)

- **问题 / 瓶颈** · 只证实不证伪导致探索效率低
- **核心创新 / 方法** · 让模型在三元组交互中提案、收反馈并猜规则，比较反例提示与行为蒸馏
- **Baseline** · 默认提示及鼓励反例的提示
- **Benchmark** · 11 个模型的隐藏规则与迁移 Blicket 任务
- **关键结果 / 消融** · 平均发现率从 42% 升到 56%，蒸馏展现迁移
- **适用条件 / 局限** · 任务简化了现实的证据结构

**可复用机制** · 将验证流程中的确认和反证查询分开统计，并检验迁移到新反馈机制。

<a id="paper-153631"></a>

## Failure-Band Authorization for Filtered Retrieval

[官方论文页](https://neurips.cc/virtual/2026/poster/153631) · [作者来源](https://openreview.net/forum?id=JxfZ6eyRMh)

- **问题 / 瓶颈** · 平均速度不能反映过滤向量搜索的尾延时
- **核心创新 / 方法** · 固定计划集，校准尾部区间并将召回下限纳入选择
- **Baseline** · 最强固定或动态对照；具名方法待核
- **Benchmark** · Medium+EntDoc，在 5–15% 失败区间比较尾延时及 Recall@20
- **关键结果 / 消融** · 作者报告匹配召回时 P95 和 P99 分别降 46% 和 45%
- **适用条件 / 局限** · 依赖数据、硬件和校准覆盖

**可复用机制** · 固定召回预算，在计划排序最不稳的区域单独测高分位延时。

<a id="paper-149263"></a>

## Failure Profiling and Reachable Trajectory Selection for Reasoning Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/149263) · [作者来源](https://openreview.net/forum?id=rbv0ZUxfLY)

- **问题 / 瓶颈** · 正解仍可能落在学生无法复现的轨迹分布
- **核心创新 / 方法** · 重复采样统计错误率和一致性，按失败类型生成并选择候选
- **Baseline** · 常规正确解蒸馏及错误增强方法
- **Benchmark** · 数学推理蒸馏，具名任务及指标待核
- **关键结果 / 消融** · 摘要提出按失败类型和可达性选择，量化收益待核
- **适用条件 / 局限** · 重复采样增加开销；学生变化后需重新估计

**可复用机制** · 蒸馏前分开估计错误率与错误一致性，避免给不同失败模式同样监督。

<a id="paper-155445"></a>

## Fair Bubble Sort: Provably Optimal Fair Ranking with Continuous Sensitive Attributes

[官方论文页](https://neurips.cc/virtual/2026/poster/155445) · [作者来源](https://openreview.net/forum?id=5YYHyRjX7r)

- **问题 / 瓶颈** · 离散分组丢失连续顺序及细粒度差异
- **核心创新 / 方法** · 用 Kendall 相关定义公平，以 Kemeny 距离度量失真，通过相邻交换优化
- **Baseline** · 离散分组式排名规则
- **Benchmark** · 合成与真实排序数据，比较公平与效用得失
- **关键结果 / 消融** · 作者证明无权 Kemeny 设定下最优并报告更优折衷
- **适用条件 / 局限** · 加权或其他公平定义不在该保证内

**可复用机制** · 敏感属性为连续变量时，以连续约束和离散分桶做公平效用对照。

<a id="paper-154171"></a>

## Fair Division of Work in Collaborative Mean Estimation via Bargaining

[官方论文页](https://neurips.cc/virtual/2026/poster/154171) · [作者来源](https://openreview.net/forum?id=Fil0EoNr7j)

- **问题 / 瓶颈** · 平均分工忽视成本与数据质量差异
- **核心创新 / 方法** · 将满足 PAC 精度的样本分配写成议价问题，用一参数福利族覆盖数种公平定义
- **Baseline** · 功利、平等和 Nash 议价准则
- **Benchmark** · 共享均值的标量估计理论
- **关键结果 / 消融** · 给出已知方差时的公平分工刻画
- **适用条件 / 局限** · 共享均值和成本假设限制外推

**可复用机制** · 先算联合精度可行域，再按约定福利设置各方配额

<a id="paper-148409"></a>

## FairMT: Fairness for Heterogeneous Multi-Task Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/148409) · [作者来源](https://openreview.net/forum?id=y4pCWEetw2)

- **问题 / 瓶颈** · 多头敏感度和输出尺度不同
- **核心创新 / 方法** · 以分离梯度的有效最优组为参照，归一差距并以头部几何引导原始对偶优化
- **Baseline** · 效用导向多任务优化器
- **Benchmark** · 视觉与语言多任务公平评测
- **关键结果 / 消融** · 作者报告群体差距缩小且效用接近效用导向对照
- **适用条件 / 局限** · 依赖有效群体统计；量化幅度待核

**可复用机制** · 同预算比较直接聚合差距和经过各头灵敏度校正的聚合

<a id="paper-149831"></a>

## Fairness Failure Modes of Multimodal LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/149831) · [作者来源](https://openreview.net/forum?id=myI2BmrxeL)

- **问题 / 瓶颈** · 单一偏差分数掩盖两种方向相反的失误
- **核心创新 / 方法** · 控制图像可见证据和上下文歧义，分别报告公平与偏差分数
- **Baseline** · 闭源和开源模型、骨干语言模型、提示缓解方案
- **Benchmark** · MultiBBQ 视觉及图文设置
- **关键结果 / 消融** · 作者报告部分闭源模型过度拒答，部分开源模型在歧义下不善弃答
- **适用条件 / 局限** · 合成图和有限刻板情境限制外推

**可复用机制** · 用歧义与已消歧的成对样本分开统计拒答行为

<a id="paper-150117"></a>

## Fairness in limited resource prediction-driven decisions

[官方论文页](https://neurips.cc/virtual/2026/poster/150117) · [作者来源](https://openreview.net/forum?id=kXu9l8Thvx)

- **问题 / 瓶颈** · 有限资源时某些公平定义可能导致极端效用损失
- **核心创新 / 方法** · 把比例公平改造成可调正则并构造有界代价的机会均等变体
- **Baseline** · 最大最小公平与传统机会均等
- **Benchmark** · 容量受限的预测驱动资源分配理论
- **关键结果 / 消融** · 证明极端条件下传统准则代价可无界，并给出替代准则的界
- **适用条件 / 局限** · 结论依赖效用定义及理论条件

**可复用机制** · 部署前比较公平约束的最坏效用代价曲线

<a id="paper-153829"></a>

## Fair Range k-Supplier Clustering in Offline and Streaming Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153829) · [作者来源](https://openreview.net/forum?id=IQsFwmNekG)

- **问题 / 瓶颈** · 公平要求施加在供应中心而非客户
- **核心创新 / 方法** · 为群体上下限下的 k-supplier 设计离线、流式和重叠组近似算法
- **Baseline** · 现有公平聚类求解器
- **Benchmark** · 理论近似比及合成与真实数据的质量和耗时
- **关键结果 / 消融** · 互斥组离线 3 近似、流式 3+ε；重叠组 3 近似对簇数指数
- **适用条件 / 局限** · 重叠组算法受簇数限制

**可复用机制** · 在设施选址前检查配额交叠，再选择流式或参数化算法

<a id="paper-148629"></a>

## FairSplit: Decomposing the Embedding Space for Fair Classification

[官方论文页](https://neurips.cc/virtual/2026/poster/148629) · [作者来源](https://openreview.net/forum?id=wKZHeFrUHc)

- **问题 / 瓶颈** · 分类效用与减少敏感属性依赖冲突
- **核心创新 / 方法** · 学习维度掩码，以 HSIC 提约束并将预测限制在公平子空间
- **Baseline** · 既有公平分类方法，具名对照待核
- **Benchmark** · 多类及非二元敏感属性的公平基准
- **关键结果 / 消融** · 证明人口统计均等差距受维度与 HSIC 限制，并报告实证权衡有竞争力
- **适用条件 / 局限** · 依赖训练时敏感属性，其他公平定义待核

**可复用机制** · 监控预测子空间维度和泄漏，并对照只惩罚泄漏的训练

<a id="paper-151993"></a>

## FairTune Market: A Fair and Trustworthy Marketplace for Fine-Tuned LLMs via Posted-Price & Proper-Scoring Mechanisms

[官方论文页](https://neurips.cc/virtual/2026/poster/151993) · [作者来源](https://openreview.net/forum?id=WIuScfyKmS)

- **问题 / 瓶颈** · 买方购前无法确认模型与需求是否匹配
- **核心创新 / 方法** · 固定标价并以截断的适当评分规则按生成验证结果结算
- **Baseline** · 常规市场及拥有完整风格信息的 Oracle
- **Benchmark** · 模拟市场和 10 个文本领域的嵌入匹配
- **关键结果 / 消融** · 摘要报告微调成本下降 72.4%，恢复 Oracle 福利的 96.3%
- **适用条件 / 局限** · 依赖评估可验证及市场行为假设

**可复用机制** · 将初始匹配与事后质量支付分开，按验证噪声测误报和成本

<a id="paper-150604"></a>

## Faithful Embeddings of Irregular and Asynchronous Data for Online Log-NCDEs

[官方论文页](https://neurips.cc/virtual/2026/poster/150604) · [作者来源](https://openreview.net/forum?id=gtk5eOWBxM)

- **问题 / 瓶颈** · 人为重建路径可能改变连续模型的输入结构
- **核心创新 / 方法** · 用连续单射编码记录事件增量，组合任意区间的对数签名
- **Baseline** · 插值或插补驱动的连续时间模型
- **Benchmark** · 合成受控动力学及真实不规则序列
- **关键结果 / 消融** · 作者证明紧集上的通用性转移并报告精度和效率改善
- **适用条件 / 局限** · 依赖紧性等理论条件；具体基准及误差幅度待核

**可复用机制** · 固定模型比较事件编码与重建路径，在不同输出网格下测稳定性

<a id="paper-154238"></a>

## FaithfulFaces: Pose-Faithful Facial Identity Preservation for Text-to-Video Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/154238) · [作者来源](https://openreview.net/forum?id=FD6ARt6oA9)

- **问题 / 瓶颈** · 大姿态变化和遮挡会造成跨帧身份飘移
- **核心创新 / 方法** · 以显式角度和姿态共享字典对齐跨视角身份条件
- **Baseline** · 现有人物一致性文本到视频方法，名称待核
- **Benchmark** · 大转角与遮挡的视频一致性评测
- **关键结果 / 消融** · 作者报告身份一致性和结构清晰度改善
- **适用条件 / 局限** · 数据偏差和未见姿态极值待核

**可复用机制** · 在合规授权数据上分开检查姿态响应与外观连续性

<a id="paper-139844"></a>

## Faithfulness Metrics Don't Measure Faithfulness: A Meta-Evaluation with Ground Truth

[官方论文页](https://neurips.cc/virtual/2026/poster/139844) · [作者来源](https://openreview.net/forum?id=12Pl2wLcY7)

- **问题 / 瓶颈** · 合理性代理并不能测解释是否反映实际计算
- **核心创新 / 方法** · 构造可从输出推断中间计算的任务，在步骤和整链层面自动标记
- **Baseline** · 主流忠实度指标和随机基准
- **Benchmark** · BonaFide 含 13 任务、10 模型、3066 条链，测 AUROC
- **关键结果 / 消融** · 多数接近随机，整链最好 0.71，步骤最好 0.59 且难跨设置
- **适用条件 / 局限** · 可标真值任务与真实开放任务存在差距

**可复用机制** · 先以有已知机制的任务验收解释指标，再迁移到开放环境

<a id="paper-149124"></a>

## FaithSieve: Fine-Grained Evaluation of Math Proofs with Faithful Formal Evidence

[官方论文页](https://neurips.cc/virtual/2026/poster/149124) · [作者来源](https://openreview.net/forum?id=si7lviFpgb)

- **问题 / 瓶颈** · Lean 可能验证翻译漂移或跳过局部漏洞
- **核心创新 / 方法** · 细分证明、提取局部义务、检查上下文及对象是否忠实后采用形式证据
- **Baseline** · 直接自然语言判分
- **Benchmark** · ProofLoc-Olympiad 350 题及 University 200 题，首错精确匹配
- **关键结果 / 消融** · 两者分别达到 81.43% 和 84.5%，对照 72.29% 和 75.0%
- **适用条件 / 局限** · 依赖形式化质量和专业题域

**可复用机制** · 分开测自动形式化对齐与形式验证正确性

<a id="paper-138979"></a>

## FakeParts: a New Family of AI-Generated Video Forgeries

[官方论文页](https://neurips.cc/virtual/2026/poster/138979) · [作者来源](https://openreview.net/forum?id=suBjj8xrz2)

- **问题 / 瓶颈** · 只测完整生成容易高估检测覆盖
- **核心创新 / 方法** · 以局部篡改检测和定位为防御评测对象
- **Baseline** · 完整视频伪造基准、人类与超过 15 种检测模型
- **Benchmark** · FakePartsBench 的视频检测与像素及帧级标注
- **关键结果 / 消融** · 作者报告局部情形下人的检测准确率最多下降 26%，检测模型也退化
- **适用条件 / 局限** · 结果依赖数据分布及验证协议

**可复用机制** · 防御评测分层报告局部、全局条件下的识别率与定位

<a id="paper-149554"></a>

## FA-LAM: Focus-Aware Large Avatar Model for One-Shot 4D Animatable Gaussian Head

[官方论文页](https://neurips.cc/virtual/2026/poster/149554) · [作者来源](https://openreview.net/forum?id=pGrWSHPZN0)

- **问题 / 瓶颈** · 重建与动画共享训练时存在任务冲突
- **核心创新 / 方法** · 以对称语义注意力约束加双阶段训练，并为流式输入融合可见 token
- **Baseline** · 现有可动画头部重建方法
- **Benchmark** · 大视角和局部细节的静态及动态头部重建
- **关键结果 / 消融** · 作者报告质量改善，数值和具名对照待核
- **适用条件 / 局限** · 依赖头部结构先验及授权数据

**可复用机制** · 固定参数预算比较联合与分阶段学习补全和动画

<a id="paper-150365"></a>

## FalconPerception-HD: High Density Perception via Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/150365) · [作者来源](https://openreview.net/forum?id=icSHR3O8rl)

- **问题 / 瓶颈** · 逐 token 交叉熵不对应集合精确率召回率
- **核心创新 / 方法** · 在 Falcon Perception 上用 GRPO 对集合输出优化并控制多头采样
- **Baseline** · 以最大似然训练的基础模型
- **Benchmark** · PBench、SACO-Gold 与高密度场景，包含 MCC
- **关键结果 / 消融** · 作者报告可到单场景 500 物体，并减少掩码重复及去重需求
- **适用条件 / 局限** · 奖励权衡依赖实例密度及匹配规则

**可复用机制** · 训练集合解码器时比较集合奖励和逐 token 损失，并看重复率

<a id="paper-150872"></a>

## Falcon-X: A Time Series Foundation Model for Heterogeneous Multivariate Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/150872) · [作者来源](https://openreview.net/forum?id=ekOExPyuZS)

- **问题 / 瓶颈** · 原变量尺度和物理意义不同，非负注意力限制交互
- **核心创新 / 方法** · 估计正负语义亲和，在潜实体空间做注意力，再路由重建各变量
- **Baseline** · 现有时间序列基础模型
- **Benchmark** · GIFT-Eval 和 fev-bench 的预测比较
- **关键结果 / 消融** · 作者报告领先，分项幅度待核
- **适用条件 / 局限** · 原型覆盖和负亲和解释性须验证

**可复用机制** · 按传感器组合留出任务比较共享原型与直接变量混合

<a id="paper-151030"></a>

## FAME: Forecasting Academic Impact via Continuous-Time Manifold Evolution

[官方论文页](https://neurips.cc/virtual/2026/poster/151030) · [作者来源](https://openreview.net/forum?id=dUYwNu0iG4)

- **问题 / 瓶颈** · 即时文本评分难代理延迟结果
- **核心创新 / 方法** · 用文本和知识流关系建动态主题空间，并把几何信号加给语言评估器
- **Baseline** · 前沿语言模型评估器及其加动态信号版本
- **Benchmark** · 3200 篇三子领域 arXiv 论文的前瞻多维预测
- **关键结果 / 消融** · 作者报告动态模型优于语言评估器，且附加信号有益
- **适用条件 / 局限** · 影响力是代理指标，不能直接等同学术价值

**可复用机制** · 严格按时间切分，比较纯文本评估与引入历史演化证据

<a id="paper-151260"></a>

## FARE: Forensic Acceptance Region Estimation for Catching Bait-and-Switch Image Generators

[官方论文页](https://neurips.cc/virtual/2026/poster/151260) · [作者来源](https://openreview.net/forum?id=biz1Z9lOtc)

- **问题 / 瓶颈** · 黑盒接口在认证后可能替换模型
- **核心创新 / 方法** · 以认证样本建立输出一致性判定，用难例收紧接受区域
- **Baseline** · 既有生成器验证基线
- **Benchmark** · 相近模型版本和变体的替换检测，关注严格误报阈值
- **关键结果 / 消融** · 作者报告严格运行点优于对照，幅度待核
- **适用条件 / 局限** · 需要可信登记样本；正常更新可能导致漂移

**可复用机制** · 将样本登记和上线抽检分离，按预设误报率衡量检测能力

<a id="paper-148285"></a>

## FASD: Hardware Acceleration for Multi-AI-Agent Discussion

[官方论文页](https://neurips.cc/virtual/2026/poster/148285) · [作者来源](https://openreview.net/forum?id=z1Bfiyossy)

- **问题 / 瓶颈** · 多代理轮数、会话和节点增加会抬高讨论延迟
- **核心创新 / 方法** · 用图耦合动态建模代表工作流，并把适合的优化放入 FPGA
- **Baseline** · 常规软件级多代理执行优化
- **Benchmark** · 不同大小和复杂度的多代理工作负载，比较速度与质量
- **关键结果 / 消融** · 作者报告图越大收益越明显且任务性能保持
- **适用条件 / 局限** · 特定硬件映射与工作流结构限制泛化

**可复用机制** · 先按轮次和拓扑分析时延，再决定图级调度是否值得硬件化

<a id="paper-149237"></a>

## FashionChameleon: Towards Real-Time and Interactive Human-Garment Video Customization

[官方论文页](https://neurips.cc/virtual/2026/poster/149237) · [作者来源](https://openreview.net/forum?id=ru7qDMOTdU)

- **问题 / 瓶颈** · 交互换装需低延迟又不能中断运动
- **核心创新 / 方法** · 单服装教师训练与流式蒸馏后，推理时分别更新条件缓存和管理历史缓存
- **Baseline** · 既有服装视频定制系统
- **Benchmark** · 交互切换、长视频外推及单卡吞吐
- **关键结果 / 消融** · 作者报告单卡 23.8 FPS，约快 30–180 倍
- **适用条件 / 局限** · 依赖训练服装和缓存分离质量；具名硬件及一致性指标待核

**可复用机制** · 流式编辑先定义哪些历史应失效，再测切换和运动连续性

<a id="paper-151229"></a>

## Fast 4D Mesh Generation by Spatio-Temporal Attention Chains

[官方论文页](https://neurips.cc/virtual/2026/poster/151229) · [作者来源](https://openreview.net/forum?id=bwPja6GtAE)

- **问题 / 瓶颈** · 长视频逐帧匹配慢且几何细节漂移
- **核心创新 / 方法** · 锚顶点映射到潜 token，沿时序注意力传播对应再回投顶点
- **Baseline** · 既有四维网格生成方法
- **Benchmark** · 动态网格几何、时序一致性、两类追踪和相机估计
- **关键结果 / 消融** · 作者报告 9 秒生成、13 倍提速，且可处理长至 16 倍的视频
- **适用条件 / 局限** · 早期潜对应须可靠，遮挡边界待测

**可复用机制** · 在生成模型中比较不同迭代层的对应质量，验证是否可替代外部匹配

<a id="paper-155794"></a>

## Fast Accurate Quantum Monte Carlo without Metropolis Adjustment

[官方论文页](https://neurips.cc/virtual/2026/poster/155794) · [作者来源](https://openreview.net/forum?id=2qZHSkdQpV)

- **问题 / 瓶颈** · 接受拒绝增加计算且可能限制混合
- **核心创新 / 方法** · 将无修正 HMC 用于量子期望估计
- **Baseline** · MH 修正 HMC
- **Benchmark** · 量子观测量与有限预算误差
- **关键结果 / 消融** · 论文分析离散偏差和采样方差的权衡
- **适用条件 / 局限** · 需验证步长偏差不掩盖目标信号

**可复用机制** · 固定总算力拆解偏差和方差

<a id="paper-149617"></a>

## Fast Algorithms for the Label Propagation Operator on Signed Graphs

[官方论文页](https://neurips.cc/virtual/2026/poster/149617) · [作者来源](https://openreview.net/forum?id=ol8v70zjm8)

- **问题 / 瓶颈** · 吸收随机游走近似方差高
- **核心创新 / 方法** · 多根生成树结合 Rao–Blackwell 化
- **Baseline** · 吸收随机游走近似
- **Benchmark** · 真实网络含千万节点规模
- **关键结果 / 消融** · 报告精度和可扩展性改善
- **适用条件 / 局限** · 依赖带符号图的边界求解设定

**可复用机制** · 在同等抽样预算下比较单路径与条件平均

<a id="paper-149973"></a>

## Fast Alignment of Embeddings: Computational Guarantees for Anisotropic Procrustes-Wasserstein

[官方论文页](https://neurips.cc/virtual/2026/poster/149973) · [作者来源](https://openreview.net/forum?id=loV2n73ZW3)

- **问题 / 瓶颈** · 未知旋转与排列相互耦合
- **核心创新 / 方法** · 先估计两边主特征空间再找匹配
- **Baseline** · 各向同性对齐理论
- **Benchmark** · 幂律协方差的带噪植入高斯模型
- **关键结果 / 消融** · 显式条件下多项式时间高概率精确恢复
- **适用条件 / 局限** · 依赖谱结构和噪声条件

**可复用机制** · 在尝试全局匹配前测共享谱结构

<a id="paper-151812"></a>

## Fast and Accurate Probing of In-Training LLMs' Downstream Performances

[官方论文页](https://neurips.cc/virtual/2026/poster/151812) · [作者来源](https://openreview.net/forum?id=XpnthdLoOn)

- **问题 / 瓶颈** · 生成评测慢且困惑度可偏离任务效果
- **核心创新 / 方法** · 从内部表征拟合下游 pass@1
- **Baseline** · 困惑度与生成评测
- **Benchmark** · 训练中检查点和下游成功概率
- **关键结果 / 消融** · 作者报告可快速预测任务表现
- **适用条件 / 局限** · 外推至新训练方案需校验

**可复用机制** · 用少量真实评测维护代理评分

<a id="paper-154587"></a>

## Fast and Consistent Structure Learning in Graphical Models via Approximate Cross-Validation

[官方论文页](https://neurips.cc/virtual/2026/poster/154587) · [作者来源](https://openreview.net/forum?id=CTPhY8k8EQ)

- **问题 / 瓶颈** · 普通交叉验证成本高且可能选择不一致
- **核心创新 / 方法** · 以近似交叉验证构建可扩展图恢复流程
- **Baseline** · 交叉验证与 BIC 类准则
- **Benchmark** · 高维稀疏图的理论与实验
- **关键结果 / 消融** · 在信号强度条件下证明选择一致
- **适用条件 / 局限** · 依赖结构和信号假设

**可复用机制** · 同时检验选边稳定性和预测误差

<a id="paper-152237"></a>

## Fast and slow gradient descent dynamics of logistic regression through weak alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/152237) · [作者来源](https://openreview.net/forum?id=UYEfZQ9sax)

- **问题 / 瓶颈** · 训练损失下降快于最大间隔方向收敛
- **核心创新 / 方法** · 用弱对齐刻画梯度下降分阶段演化
- **Baseline** · 仅采用渐近最大间隔描述
- **Benchmark** · 逻辑回归分离数据上的方向与优化动态
- **关键结果 / 消融** · 区分优化与方向收敛时间尺度
- **适用条件 / 局限** · 非线性模型的适用性待核

**可复用机制** · 记录间隔与方向随时间变化

<a id="paper-156051"></a>

## Fast and Stable Gradient Approximation for Bilinear Forms of Hermitian Matrix Functions

[官方论文页](https://neurips.cc/virtual/2026/poster/156051) · [作者来源](https://openreview.net/forum?id=0o7Q9IWQK0)

- **问题 / 瓶颈** · 反传递推或增广矩阵带来正交化负担
- **核心创新 / 方法** · 用前向 Lanczos 计算近似双线性矩阵函数梯度
- **Baseline** · 重正交化反传和增广 Arnoldi
- **Benchmark** · 大规模 Hermitian 矩阵函数
- **关键结果 / 消融** · 梯度误差受 Lanczos 残差控制，作者测试中稳定且较快
- **适用条件 / 局限** · 依赖 Hermitian 结构及误差界假设

**可复用机制** · 同步监控前向和梯度近似误差

<a id="paper-150772"></a>

## Fast and Stable Triangular Inversion for Delta-Rule Linear Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/150772) · [作者来源](https://openreview.net/forum?id=fU54rMdv6G)

- **问题 / 瓶颈** · Delta-rule 的三角求逆易成为瓶颈且误差会传播
- **核心创新 / 方法** · 系统比较以矩阵乘为主的直接与迭代方案
- **Baseline** · 多种直接和迭代三角求逆
- **Benchmark** · Delta-rule 线性 Transformer 的数值与硬件评测
- **关键结果 / 消融** · 提供复杂度、稳定性和实践对照
- **适用条件 / 局限** · 硬件和精度配置会改变取舍

**可复用机制** · 用端到端模型误差验证内核选择

<a id="paper-152691"></a>

## Fast Approximate $\ell_p$ Chamfer Distance via Lopsided Embeddings and Structured JL

[官方论文页](https://neurips.cc/virtual/2026/poster/152691) · [作者来源](https://openreview.net/forum?id=R8o3ICPCsm)

- **问题 / 瓶颈** · 逐对距离比较在高维昂贵
- **核心创新 / 方法** · 一般 p 用单边嵌入，欧氏情形用结构化 JL
- **Baseline** · 既有 Chamfer 算法
- **Benchmark** · 理论运行时间与近似误差
- **关键结果 / 消融** · 给出近输入线性的运行时间界，含对数与误差因子
- **适用条件 / 局限** · 适用于 1<p≤2 的单向 Chamfer

**可复用机制** · 先确定范数再判断降维误差能否支撑最近邻聚合

<a id="paper-149330"></a>

## FAST-Brain: A Flow-Aligned Spatio-Temporal Surrogate Brain Model

[官方论文页](https://neurips.cc/virtual/2026/poster/149330) · [作者来源](https://openreview.net/forum?id=qu1GlOKsSN)

- **问题 / 瓶颈** · 长时脑影像同时具有空间约束和低维结构
- **核心创新 / 方法** · 以图卷积和 Transformer 建模流对齐的 BOLD 信号
- **Baseline** · 传统时空代理建模，具名方法待核
- **Benchmark** · 静息态 fMRI 和合成时空数据
- **关键结果 / 消融** · 低维子空间假设下给出本征维度误差分析
- **适用条件 / 局限** · 仅涉及观测信号建模

**可复用机制** · 区分环境维度和本征维度对时空代理的影响

<a id="paper-156099"></a>

## Fast Diverse Nearest Neighbor Search

[官方论文页](https://neurips.cc/virtual/2026/poster/156099) · [作者来源](https://openreview.net/forum?id=0NrAOwOmiN)

- **问题 / 瓶颈** · 多样图检索的开销随返回条目数二次增长
- **核心创新 / 方法** · 借鉴群测随机划分类别并为桶建立近邻索引
- **Baseline** · Anand 等 ICML 2025 的多样图方法
- **Benchmark** · 不同类别近邻检索的查询复杂度
- **关键结果 / 消融** · 作者给出次线性于 k 的额外因子
- **适用条件 / 局限** · 依赖近似容许度及建桶参数

**可复用机制** · 把类别覆盖与距离精度同时纳入检索比较

<a id="paper-154725"></a>

## Fast-dLLM++: Fr\'{e}chet Profile Decoding for Faster Diffusion LLM Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/154725) · [作者来源](https://openreview.net/forum?id=BTfatNCwhE)

- **问题 / 瓶颈** · 最弱 token 置信度过度限制异质集合
- **核心创新 / 方法** · 保留模型和缓存的训练后解码，使用排序置信度轮廓
- **Baseline** · Fast-dLLM 的同置信选择规则
- **Benchmark** · 扩散语言模型并行生成，具体任务待核
- **关键结果 / 消融** · 同置信时退化为旧规则，异质时给出理论增益
- **适用条件 / 局限** · 依赖置信度的可靠性

**可复用机制** · 在同等任务准确率下比较最小置信与全轮廓提交

<a id="paper-151622"></a>

## FastDSAC: Unlocking the Potential of Maximum Entropy RL in High-Dimensional Humanoid Control

[官方论文页](https://neurips.cc/virtual/2026/poster/151622) · [作者来源](https://openreview.net/forum?id=ZBAe6ak1l6)

- **问题 / 瓶颈** · 高维探索低效且价值估计不稳
- **核心创新 / 方法** · 动态调节逐维熵并使用连续分布式 critic
- **Baseline** · 确定性策略梯度与随机策略
- **Benchmark** · HumanoidBench 和连续控制任务
- **关键结果 / 消融** · 作者报告随机策略表现改善并与确定性方法竞争
- **适用条件 / 局限** · 探索收益依赖动作维和吞吐配置

**可复用机制** · 独立消融熵调节和价值分布表示

<a id="paper-153729"></a>

## Faster Dynamic Graph Clustering with Hierarchical Graph Contraction

[官方论文页](https://neurips.cc/virtual/2026/poster/153729) · [作者来源](https://openreview.net/forum?id=JDWJEQwXiU)

- **问题 / 瓶颈** · 动态图聚类查询可能成为主要瓶颈
- **核心创新 / 方法** · 以层次收缩维护持续加边的图族
- **Baseline** · Laenen 和 Sun ICML 2024
- **Benchmark** · 理论复杂度和合成、真实动态图
- **关键结果 / 消融** · 给出摊销 O(d) 更新与软 O(n^(1/d)) 查询
- **适用条件 / 局限** · 边插入设定，删除边未覆盖

**可复用机制** · 通过调节层数权衡更新和查询

<a id="paper-152615"></a>

## Faster Rates For  Federated Variational Inequalities

[官方论文页](https://neurips.cc/virtual/2026/poster/152615) · [作者来源](https://openreview.net/forum?id=RmzepfWb3R)

- **问题 / 瓶颈** · 联邦变分不等式的速率受客户端漂移制约
- **核心创新 / 方法** · 改进 Local Extra SGD 分析并提出带额外步的局部不精确近端方法
- **Baseline** · Local Extra SGD
- **Benchmark** · 光滑单调随机和复合变分不等式
- **关键结果 / 消融** · 在有界 Hessian 等条件下给出更快保证
- **适用条件 / 局限** · 各速率依赖具体有界性假设

**可复用机制** · 按异质性和条件选择局部更新器

<a id="paper-156001"></a>

## FASTER: Rethinking Real-Time Flow VLAs

[官方论文页](https://neurips.cc/virtual/2026/poster/156001) · [作者来源](https://openreview.net/forum?id=1G2AcEojJU)

- **问题 / 瓶颈** · 异步平滑不等同于快速反应
- **核心创新 / 方法** · 流采样中优先去噪近期动作并分析首动作时延
- **Baseline** · 固定流采样日程与异步推理
- **Benchmark** · VLA 反应时延和动作段执行
- **关键结果 / 消融** · 作者报告紧迫动作去噪显著加快
- **适用条件 / 局限** · 反应时分布取决于模型假设及执行时域

**可复用机制** · 把首动作延迟和执行时域分开监控

<a id="paper-149442"></a>

## FASTER: Value-Guided Sampling for Fast RL

[官方论文页](https://neurips.cc/virtual/2026/poster/149442) · [作者来源](https://openreview.net/forum?id=q3wZBBqRAC)

- **问题 / 瓶颈** · 完整采样多个动作代价高
- **核心创新 / 方法** · 将候选逐步淘汰表示为 MDP，并训练中间价值
- **Baseline** · 完整生成后再选候选
- **Benchmark** · 长时机器人操作与生成策略推理
- **关键结果 / 消融** · 作者报告降低候选计算成本并维持回报，具体值待核
- **适用条件 / 局限** · 早期价值误差可能错删候选

**可复用机制** · 对比计算节省与正确候选保留率

<a id="paper-153523"></a>

## Fast Gauss-Newton for Multiclass Cross-Entropy

[官方论文页](https://neurips.cc/virtual/2026/poster/153523) · [作者来源](https://openreview.net/forum?id=KiUlDWxNTi)

- **问题 / 瓶颈** · 全 GGN 耦合全部 logits
- **核心创新 / 方法** · 保留秩一项并用无矩阵共轭梯度求解
- **Baseline** · 完整 GGN
- **Benchmark** · 多类交叉熵的曲率与训练
- **关键结果 / 消融** · 正半定下近似，二分类精确且损失梯度保持
- **适用条件 / 局限** · 忽略竞争类别内协方差

**可复用机制** · 在多类任务比较曲率保真与求解预算

<a id="paper-150502"></a>

## Fast KVzip: Efficient and Accurate LLM Inference with Gated KV Eviction

[官方论文页](https://neurips.cc/virtual/2026/poster/150502) · [作者来源](https://openreview.net/forum?id=hbemMJsy3u)

- **问题 / 瓶颈** · 压缩可能损害质量或增加推理开销
- **核心创新 / 方法** · 冻结骨干，用前向表示和重建目标训练门控
- **Baseline** · 既有缓存压缩与完整缓存
- **Benchmark** · Qwen2.5-1M、Qwen3、Gemma3 的长上下文等任务
- **关键结果 / 消融** · 作者报告最高移除约 70% KV 且性能接近完整缓存
- **适用条件 / 局限** · 保真程度依任务与预算变化

**可复用机制** · 同时评估预填充、解码延迟与长程召回

<a id="paper-152762"></a>

## Fast Learning Rates for Physics-Informed Kernel Methods

[官方论文页](https://neurips.cc/virtual/2026/poster/152762) · [作者来源](https://openreview.net/forum?id=QYqNJIQKwh)

- **问题 / 瓶颈** · 物理信息与函数观测的边际收益不明确
- **核心创新 / 方法** · 分析结合噪声值和线性微分观测的核估计量
- **Baseline** · 只给有限微分信息与完美约束的理论对照
- **Benchmark** · 有限样本误差界和数值模拟
- **关键结果 / 消融** · 超过问题相关阈值后达到完美约束的速率
- **适用条件 / 局限** · 依赖线性算子及核函数条件

**可复用机制** · 为差分和观测预算各画学习曲线

<a id="paper-152917"></a>

## Exactness Matters for Physical Rule Enforcement

[官方论文页](https://neurips.cc/virtual/2026/poster/152917) · [作者来源](https://openreview.net/forum?id=PR7Uan6tks)

- **问题 / 瓶颈** · 近似物理校正可能引起滚动分布偏移
- **核心创新 / 方法** · 比较目标流形上保持恒等的精确投影与近似清理
- **Baseline** · 原始 FNO、事后投影、循环内投影
- **Benchmark** · NS-128、非周期 CFDBench、层级预测
- **关键结果 / 消融** · NS-128 百步末步 MSE 从约 9.39e-5 降至循环内 5.37e-7；近似清理可降散度却增预测误差
- **适用条件 / 局限** · 精确性取决于边界与目标几何

**可复用机制** · 用真实目标失真和滚动误差共同选择校正强度

<a id="paper-153596"></a>

## Fast Organic Crystal Structure Prediction with Unit Cell Flow Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/153596) · [作者来源](https://openreview.net/forum?id=KD4i8hE0Rc)

- **问题 / 瓶颈** · 重复结构裁剪和三角层计算开销大
- **核心创新 / 方法** · 流匹配生成去冗余晶胞，以成对偏置注意力替换三角层
- **Baseline** · OXtal
- **Benchmark** · OXtal 汇总结构预测测试集
- **关键结果 / 消融** · 作者报告求解率更高且快 5–8 倍
- **适用条件 / 局限** · 结果依赖能量排序和候选预算

**可复用机制** · 周期材料生成优先测试基本重复单元，从而降低表示冗余

<a id="paper-148197"></a>

## Fast Reconstruction of Exact Maxwell Dynamics from Sparse Data

[官方论文页](https://neurips.cc/virtual/2026/poster/148197) · [作者来源](https://openreview.net/forum?id=zcI6E4WHeK)

- **问题 / 瓶颈** · 稀疏场观测下残差惩罚增加优化负担
- **核心创新 / 方法** · 浅层网络组合满足均匀介质 Maxwell 方程的精确解，证明模型类具有通用逼近性
- **Baseline** · 摘要未列具名模型
- **Benchmark** · 三维稀疏点观测，测相对验证误差和方程残差
- **关键结果 / 消融** · 约千点时误差低于 1%，方程残差为零
- **适用条件 / 局限** · 针对均匀介质设定

**可复用机制** · 线性控制方程可解析时，比较可行基网络与软约束训练

<a id="paper-149044"></a>

## Fast, Relaxation‑ and Hyperparameter‑Free Pairwise Worst-Case Class Separation

[官方论文页](https://neurips.cc/virtual/2026/poster/149044) · [作者来源](https://openreview.net/forum?id=tIGr4bvK5s)

- **问题 / 瓶颈** · 整体散布目标可掩盖局部类别混淆
- **核心创新 / 方法** · 最大化最小成对类间与类内散布比，外层分式变换、内层迭代求解二次规划
- **Baseline** · 判别降维方法，名称待核
- **Benchmark** · 分类误差评测
- **关键结果 / 消融** · 作者报告分类误差一致改善并给出收敛论证
- **适用条件 / 局限** · 非凸问题的收敛不等于全局最优

**可复用机制** · 在类对难度不均时报告最差类对和总体分类误差

<a id="paper-148369"></a>

## Fast-RL: Accelerating Reinforcement Learning for LongCoT Reasoning Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148369) · [作者来源](https://openreview.net/forum?id=yNcSbtT8cr)

- **问题 / 瓶颈** · 长思考采样主导强化学习成本
- **核心创新 / 方法** · 先以 LoRA 学模式切换并冻结，再用快思考采样更新推理参数
- **Baseline** · 常规慢思考强化学习
- **Benchmark** · 文本及多模态推理，含 Qwen3-1.7B 的 AIME24
- **关键结果 / 消融** · 作者报告约十倍训练加速，AIME24 慢快模式分别提升 10.0 和 13.7
- **适用条件 / 局限** · 前提是两模式共享技能且可可靠切换

**可复用机制** · 将采样模式控制与能力参数解耦，检验短轨迹更新能否转移

<a id="paper-149383"></a>

## Fast Sandwich Products in Clifford Algebra

[官方论文页](https://neurips.cc/virtual/2026/poster/149383) · [作者来源](https://openreview.net/forum?id=qRvZDh6s22)

- **问题 / 瓶颈** · 显式夹积或完整作用矩阵随代数维度膨胀
- **核心创新 / 方法** · 按阶将夹积分解成向量旋转的外幂，再把 Givens 旋转提升为稀疏基更新
- **Baseline** · 现有旋量夹积实现
- **Benchmark** · 墙钟耗时和内存
- **关键结果 / 消融** · 最高分别改善 64 倍和 35 倍
- **适用条件 / 局限** · 收益取决于维度与实现

**可复用机制** · 避免生成全维算子，直接组合低维作用在各子空间的提升

<a id="paper-156095"></a>

## Fast-Slow Evolutionary Occupancy Prediction via Controlled Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/156095) · [作者来源](https://openreview.net/forum?id=0PrltFkr6P)

- **问题 / 瓶颈** · 准确与低延迟模型到达时间不同
- **核心创新 / 方法** · 分开演化确定性的自车坐标位移和真正的场景变化
- **Baseline** · 快速系统与慢速系统
- **Benchmark** · 三组快慢模型及不规则到达
- **关键结果 / 消融** · 报告精度优于快速基线，时延低于慢速系统
- **适用条件 / 局限** · 依赖配对模型输出及自车位姿

**可复用机制** · 异步融合时分别处理坐标变换和语义状态更新

<a id="paper-149922"></a>

## Fast-WAM: Do World Action Models Need Test-time Future Imagination?

[官方论文页](https://neurips.cc/virtual/2026/poster/149922) · [作者来源](https://openreview.net/forum?id=mBYJRAFq7D)

- **问题 / 瓶颈** · 迭代生成未来帧增加动作延迟
- **核心创新 / 方法** · 通过对照变体分离视频共训练和测试时显式预测
- **Baseline** · 先想象再执行的 WAM 及移除视频共训练变体
- **Benchmark** · LIBERO、RoboTwin、真机任务、推理时延
- **关键结果 / 消融** · 110 ms，较想象后执行方法快逾六倍；移除视频共训练影响更大
- **适用条件 / 局限** · 现有任务未覆盖所有依赖未来预测的场景

**可复用机制** · 独立消融训练监督与推理路径，量化效果及响应延迟

<a id="paper-156637"></a>

## Fast Wasserstein rates for estimating probability distributions of probabilistic graphical models

[官方论文页](https://neurips.cc/virtual/2026/poster/156637) · [作者来源](https://neurips.cc/virtual/2026/poster/156637)

- **问题 / 瓶颈** · 高维 Wasserstein 估计存在维数灾难
- **核心创新 / 方法** · 对给定 DAG 的条件转移核施加可量化光滑条件
- **Baseline** · 弱 Wasserstein 与强双向 TV 光滑条件的理论对照
- **Benchmark** · 独立同分布样本下 Wasserstein 误差速率
- **关键结果 / 消融** · 速率由局部维度支配，强条件下证明尖锐性
- **适用条件 / 局限** · 需要已知图及对应光滑性

**可复用机制** · 先核实局部条件分布结构，再决定是否采用图分解估计

<a id="paper-148441"></a>

## Fault Tolerance in Transformers Favors Output Alignment over Hidden-State Consistency

[官方论文页](https://neurips.cc/virtual/2026/poster/148441) · [作者来源](https://openreview.net/forum?id=xm2tQzphI5)

- **问题 / 瓶颈** · 直接对齐故障位置隐藏状态可能约束过强
- **核心创新 / 方法** · 训练时模拟计算故障并比较输出 KL 与隐藏对齐目标
- **Baseline** · 隐藏对齐、SAM、R-Drop、SAF
- **Benchmark** · GPT-2 Small、8B 与留出语料，测困惑度退化
- **关键结果 / 消融** · 小模型退化从 12.9% 降至 0.21%；直接隐藏约束可恶化
- **适用条件 / 局限** · 受模拟故障分布限制

**可复用机制** · 用同预算对照不同对齐位置，并在未见语料测容错

<a id="paper-153584"></a>

## Fault Tolerant Coresets

[官方论文页](https://neurips.cc/virtual/2026/poster/153584) · [作者来源](https://openreview.net/forum?id=KKronbQMtE)

- **问题 / 瓶颈** · 普通带权核心集在摘要被损坏时无法保持代价
- **核心创新 / 方法** · 用敏感度采样构造可高效清理解码的冗余摘要
- **Baseline** · 普通敏感度核心集及容错大小下界
- **Benchmark** · k-means 代价近似与实验验证
- **关键结果 / 消融** · 额外规模项与 f·k/ε 同阶，并有相应必要下界
- **适用条件 / 局限** · 限于指定损坏预算和目标

**可复用机制** · 设计压缩摘要时同时度量原始逼近和损坏后的可恢复性

<a id="paper-151814"></a>

## FAUST: Federated Asynchronous Update with Staggered Timescales for Low-Communication Foundation Model Training

[官方论文页](https://neurips.cc/virtual/2026/poster/151814) · [作者来源](https://openreview.net/forum?id=Xos5UImld5)

- **问题 / 瓶颈** · 同步所有状态会增加通信，长期不同步可能破坏收敛
- **核心创新 / 方法** · 组合序列并行图重写和分层同步，将前向重分布与可延迟归约区分
- **Baseline** · DDP、Local Adam、DES-LOC
- **Benchmark** · 最高 1.3B 参数语言模型，比较通信开销、困惑度和总时间
- **关键结果 / 消融** · 作者报告困惑度距全同步不超过 4.6%，总耗时少 27%
- **适用条件 / 局限** · 结果取决于带宽及并行拓扑

**可复用机制** · 按状态漂移特征分配同步频率，监控全局质量而非只看通信

<a id="paper-156009"></a>

## FAVLA: A Force-Adaptive Multi-Rate VLA model for Contact-Rich Robotic Manipulation

[官方论文页](https://neurips.cc/virtual/2026/poster/156009) · [作者来源](https://openreview.net/forum?id=1BsG8wfOjt)

- **问题 / 瓶颈** · 统一低频融合丢失接触瞬间信息
- **核心创新 / 方法** · 低频视觉语言模型预测力统计，高频专家按力反馈修正动作块并动态融合
- **Baseline** · 力感知 VLA
- **Benchmark** · 真机精密接触操作，测成功率与峰值力
- **关键结果 / 消融** · 平均成功率 88.8%，同时降低峰值接触力
- **适用条件 / 局限** · 依赖力传感及力变化预测

**可复用机制** · 用事件不确定性触发快速闭环，分阶段检查延迟和接触峰值

<a id="paper-155019"></a>

## FC-DGCN: Deep Graph Convolutional Network for Face Clustering and Recognition

[官方论文页](https://neurips.cc/virtual/2026/poster/155019) · [作者来源](https://openreview.net/forum?id=99QeLhDZQG)

- **问题 / 瓶颈** · 全图局部连接评分难兼顾质量与规模
- **核心创新 / 方法** · 全图预测节点置信度，局部子图预测边，将节点连至高置信可靠邻居
- **Baseline** · 图聚类基线
- **Benchmark** · MS-Celeb-1M 的成对和 BCubed F 分数，另测伪标注下游效果
- **关键结果 / 消融** · 作者报告聚类与低标注下游效果改善
- **适用条件 / 局限** · 依赖亲和图质量，偏差与跨数据适用性待核

**可复用机制** · 可在通用图聚类中拆分原型可信度和局部边判定

<a id="paper-156133"></a>

## 𝑓-Differential Privacy Filters: Validity and Approximate Solutions

[官方论文页](https://neurips.cc/virtual/2026/poster/156133) · [作者来源](https://openreview.net/forum?id=0AH3Ph6OYP)

- **问题 / 瓶颈** · 静态张量积记账不一定能用于全自适应停止
- **核心创新 / 方法** · 刻画自然 f-DP 过滤器的有效条件，并以自适应中心极限定理导出近似过滤器
- **Baseline** · 自然张量积过滤器及 RDP 记账
- **Benchmark** · 子采样高斯机制的理论渐近比较
- **关键结果 / 消融** · 自然规则一般无效，近似方法在两端渐近区间优于 RDP
- **适用条件 / 局限** · 实际子采样率的近似可能乐观

**可复用机制** · 上线自适应预算前区分有限样本保证与渐近估计

<a id="paper-152855"></a>

## FEAD: Fine-Grained Epipolar Attention Diffusion for Large-Disparity Light Field Spatial Super-Resolution

[官方论文页](https://neurips.cc/virtual/2026/poster/152855) · [作者来源](https://openreview.net/forum?id=PszcGoxSmL)

- **问题 / 瓶颈** · 粗视差在大视差区域不足以对齐高频信息
- **核心创新 / 方法** · 扩散细化极线注意力，用细化结果引导跨视图扭曲与融合
- **Baseline** · 光场超分辨率基线，名称待核
- **Benchmark** · 光场空域超分辨率，重点为大视差场景
- **关键结果 / 消融** · 作者报告大视差场景收益尤其明显
- **适用条件 / 局限** · 依赖可靠极线几何，开销待核

**可复用机制** · 多视图融合中按几何缩小匹配空间，再用学习细化检查困难区

<a id="paper-151552"></a>

## Feasible Policy Optimization for Safe Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151552) · [作者来源](https://openreview.net/forum?id=ZmudjL054f)

- **问题 / 瓶颈** · 每次更新同时严格约束可能保守
- **核心创新 / 方法** · 可行区内提升价值，区外降低可行性代价，利用约束衰减界分析共同解
- **Baseline** · 安全强化学习方法
- **Benchmark** · Safety-Gymnasium，检查约束满足和回报
- **关键结果 / 消融** · 作者报告约束表现好且任务回报有竞争力
- **适用条件 / 局限** · 训练期与部署保证需分别核实

**可复用机制** · 在受限任务中分别评估越界修复和可行区内收益

<a id="paper-152364"></a>

## FeatCal: Feature Calibration for Post-Merging Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152364) · [作者来源](https://openreview.net/forum?id=TbWDPX0nam)

- **问题 / 瓶颈** · 合并误差由局部失配和上游累积共同产生
- **核心创新 / 方法** · 按层以闭式解小幅更新权重，使其接近专家在同输入上的表征
- **Baseline** · Surgery、ProbSurgery
- **Benchmark** · CLIP 与 GLUE 模型融合任务
- **关键结果 / 消融** · CLIP 85.5% 对 77.0% 和 78.8%；GLUE 85.2% 对 83.7% 和 82.2%
- **适用条件 / 局限** · 需要代表性校准数据和可访问专家

**可复用机制** · 在融合完成后比较逐层校准与仅修正最后层

<a id="paper-148620"></a>

## Feature-Context Consistency: Unsupervised Adversarial Detection with Drift Stability on Attributed Graphs

[官方论文页](https://neurips.cc/virtual/2026/poster/148620) · [作者来源](https://openreview.net/forum?id=wOczaNixQw)

- **问题 / 瓶颈** · 标签迟到且自然漂移会导致误报
- **核心创新 / 方法** · 以无监督 Context Boost 度量节点与聚合邻域的一致性，分析检测和漂移稳定性
- **Baseline** · 监督 GNN、图异常检测和标准 RBM
- **Benchmark** · Ethereum 钓鱼与 Reddit 封禁数据等，测 AUROC 与 FPR
- **关键结果 / 消融** · 作者报告 AUROC 至少 0.96，漂移下 FPR 接近 5% 校准目标
- **适用条件 / 局限** · 依赖合法节点的邻域一致性

**可复用机制** · 单独测自然漂移下误报，避免把正常变化误当异常

<a id="paper-152004"></a>

## Feature Information Dynamics in Diffusion

[官方论文页](https://neurips.cc/virtual/2026/poster/152004) · [作者来源](https://openreview.net/forum?id=WDfD9WTJeJ)

- **问题 / 瓶颈** · 粗到细生成通常只靠定性判断
- **核心创新 / 方法** · 从无条件与特征条件去噪损失差估计信息密度，再分解层级特征的共享和独有信息
- **Baseline** · 像素扩散及 SDVAE、VAVAE、RAE 表示
- **Benchmark** · 频谱与类别、掩码、边缘层级的比较
- **关键结果 / 消融** · 定量验证像素域频谱顺序，并发现不同潜空间的时序不同
- **适用条件 / 局限** · 依赖去噪估计精度及特征定义

**可复用机制** · 做扩散控制设计前先测目标特征在各时间段的信息变化

<a id="paper-150047"></a>

## Feature Learning Dynamics in Infinite-Depth Neural Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/150047) · [作者来源](https://openreview.net/forum?id=lBVOJogILX)

- **问题 / 瓶颈** · 反传复用权重导致前后向相关性，不能直接按独立噪声处理。
- **核心创新 / 方法** · 用条件高斯表示拆解复用项与独立波动，并构造保留协方差的 NFD。
- **Baseline** · 有限深度 SGD 动力学及既有连续深度视角。
- **Benchmark** · depth-μP 下的一层 ResNet，解析比较有限深度与极限。
- **关键结果 / 消融** · 非退化条件下，深度离散误差为 O(L⁻¹)，复用耦合项衰减为 O(L⁻²)；初始化宽度项为 O(n⁻¹)。
- **适用条件 / 局限** · 结论依赖架构、缩放和非退化条件。

**可复用机制** · 分析深网络时分别量化有限宽度、有限深度及前后向耦合误差。

<a id="paper-149864"></a>

## Feature learning  in high-dimensions under structured covariance: Scaling laws in quadratic networks

[官方论文页](https://neurips.cc/virtual/2026/poster/149864) · [作者来源](https://openreview.net/forum?id=mftAwZQsHo)

- **问题 / 瓶颈** · 各向同性理论难涵盖真实数据的方向差异。
- **核心创新 / 方法** · 在二次激活两层网络中解析各向异性高斯输入下的在线 SGD 和连续极限。
- **Baseline** · 各向同性理论与归一化前后的设置。
- **Benchmark** · 二次网络理论及一般激活的两层网络实验。
- **关键结果 / 消融** · 协方差谱影响尺度指数和样本复杂度；归一化提高样本效率的证据见作者摘要。
- **适用条件 / 局限** · 一般激活仅获实验支持，非高斯数据外推待核。

**可复用机制** · 比较样本效率前记录协方差谱，并用归一化对照区分输入谱与架构的影响。

<a id="paper-151094"></a>

## Feature Recovery for Object Understanding Under Physical Transformation

[官方论文页](https://neurips.cc/virtual/2026/poster/151094) · [作者来源](https://openreview.net/forum?id=d1FI4Z8ezj)

- **问题 / 瓶颈** · 结构性变换不同于一般图像噪声，外观变化会破坏原物体识别。
- **核心创新 / 方法** · 冻结视觉骨干，用 FRM 将退化特征映射到原始状态对齐的表示。
- **Baseline** · 无 FRM 的原模型，包括 RF-DETR、InternVL3.5 等。
- **Benchmark** · TRACE 含约 2.14 万个合成场景与 499 个物体身份，覆盖检测与原始属性恢复。
- **关键结果 / 消融** · 随变换加剧，RF-DETR mAP 相对降 71%；FRM 的检索平均提升 12.5%，具体增益口径待核。
- **适用条件 / 局限** · 需配对监督；真实火灾场景迁移尚待核查。

**可复用机制** · 测试结构性变换时按强度比较冻结骨干与特征恢复模块，分别测定位和语义恢复。

<a id="paper-153987"></a>

## FedAdaVR: Adaptive Variance Reduction for Robust Federated Learning under Limited Client Participation

[官方论文页](https://neurips.cc/virtual/2026/poster/153987) · [作者来源](https://openreview.net/forum?id=H3RLFv3n4M)

- **问题 / 瓶颈** · 部分参与会增大服务器聚合误差。
- **核心创新 / 方法** · 将最近客户端更新与自适应优化及方差缩减结合，另提供量化存储变体。
- **Baseline** · 先进联邦基线及未量化 FedAdaVR，具名方法待核。
- **Benchmark** · 多个数据集的 IID 与非 IID 联邦训练。
- **关键结果 / 消融** · 作者给出非凸分析中消除部分参与误差的结论；量化存储降低 50%、75% 或 87.5%。
- **适用条件 / 局限** · 旧更新的时效和量化效应随参与模式变化。

**可复用机制** · 在固定参与率下对照只聚合在线更新与复用历史更新，并同时跟踪内存。

<a id="paper-155141"></a>

## Fed-AGA: An Anchor Graph Alignment Framework for Federated Unaligned Multi-view Clustering

[官方论文页](https://neurips.cc/virtual/2026/poster/155141) · [作者来源](https://openreview.net/forum?id=82yEbCFK30)

- **问题 / 瓶颈** · 分布式多视图样本缺乏一一对应。
- **核心创新 / 方法** · 各端上传轻量锚点图，服务器用拓扑签名粗对齐，再以注意力细匹配并对比融合。
- **Baseline** · 相关联邦多视图聚类方法，具名对照待核。
- **Benchmark** · 多数据集跨视图聚类，指标与错配协议待全文核查。
- **关键结果 / 消融** · 作者报告聚类表现优于所比方法。
- **适用条件 / 局限** · 锚点需保留类别结构；不共享原始数据并不自动给出形式隐私保证。

**可复用机制** · 先用稳定的组级结构约束匹配空间，再在组内用局部相似性做细对齐。

<a id="paper-153757"></a>

## FedCAG: Federated Causality-Aware Graph Learning for Multi-Cloud Workload Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/153757) · [作者来源](https://openreview.net/forum?id=IvCj0BCLBL)

- **问题 / 瓶颈** · 跨云预测受数据隔离与负载异质性影响。
- **核心创新 / 方法** · 各站点构建定向指标、空间与时间关系图，联合联邦预测模型和图先验，再做个体化调整。
- **Baseline** · 常用联邦预测方法及若干集中训练模型，具名对照待核。
- **Benchmark** · 真实多云工作负载预测，数据集及指标待核。
- **关键结果 / 消融** · 作者报告优于联邦基线及若干集中式方法。
- **适用条件 / 局限** · 由遥测估计的方向关系不等同于已验证的因果效应。

**可复用机制** · 跨站点预测时，将只聚合参数和增设结构先验分别做对照。

<a id="paper-152149"></a>

## FedCF: Fair Federated Conformal Prediction

[官方论文页](https://neurips.cc/virtual/2026/poster/152149) · [作者来源](https://openreview.net/forum?id=VAwYqelahI)

- **问题 / 瓶颈** · 总体覆盖可能掩盖不同人口组的覆盖缺口。
- **核心创新 / 方法** · 将 Conformal Fairness 扩展到联邦设置，分析人口组之间的公平差距。
- **Baseline** · 原 Conformal Fairness 框架和只考察总体覆盖的保形预测。
- **Benchmark** · 多领域数据集，检查不同组的覆盖与差距。
- **关键结果 / 消融** · 摘要报告经验验证；量化结论待核。
- **适用条件 / 局限** · 依赖所设交换性假设，跨客户端偏移下需复查。

**可复用机制** · 评估分布式不确定性系统时，同时报告总体、组别及跨客户端覆盖。

<a id="paper-153466"></a>

## Federated Concept-Based Models: Interpretable models with distributed supervision

[官方论文页](https://neurips.cc/virtual/2026/poster/153466) · [作者来源](https://openreview.net/forum?id=L7HwKQPq8i)

- **问题 / 瓶颈** · 单个机构往往无法标注所有概念，固定架构又难容纳新概念。
- **核心创新 / 方法** · 跨机构聚合概念信息，并随可用监督调整概念模型架构。
- **Baseline** · 全量概念监督与非自适应联邦模型。
- **Benchmark** · 预测准确率、概念干预效果及机构未标注概念上的推理。
- **关键结果 / 消融** · 作者报告准确率和干预效果接近全量监督，平均优于非自适应对照。
- **适用条件 / 局限** · 概念定义须能跨机构对应，隐私保护边界待全文确认。

**可复用机制** · 测试动态概念库时应单独留出本地无监督的概念，检验真正的跨机构迁移。

<a id="paper-139042"></a>

## Federated Dataset Simulation: Inducing Label-Free Heterogeneity Across Tasks

[官方论文页](https://neurips.cc/virtual/2026/poster/139042) · [作者来源](https://openreview.net/forum?id=oIgrH55uFj)

- **问题 / 瓶颈** · 标签偏斜划分难覆盖分割和检测中的异质性。
- **核心创新 / 方法** · 用预训练嵌入做几何划分，或按视觉语言模型提取的语义准则分配数据。
- **Baseline** · Dirichlet 标签偏斜划分。
- **Benchmark** · 四个数据集，覆盖分类、分割和检测；衡量异质性及训练表现。
- **关键结果 / 消融** · 两种方案造成的异质性不低于标签偏斜，并改变下游表现。
- **适用条件 / 局限** · 模拟划分的异质性不一定代表真实组织或设备分布。

**可复用机制** · 对联邦算法增加与标签无关的划分轴，并报告划分结构而非只报准确率。

<a id="paper-155993"></a>

## Federated Distributionally Robust Neural Combinatorial Optimization with Convergence Guarantees

[官方论文页](https://neurips.cc/virtual/2026/poster/155993) · [作者来源](https://openreview.net/forum?id=1JoBgRVNAk)

- **问题 / 瓶颈** · REINFORCE 的方差受成本影响，难套用联邦 DRO 的损失假设。
- **核心创新 / 方法** · 在有界成本下推导联邦 Group DRO，加入 KL 正则稳定组权重。
- **Baseline** · 朴素 Group DRO 与 FedAvg。
- **Benchmark** · 容量约束车辆路径优化及最坏组表现。
- **关键结果 / 消融** · 作者给出 O(1/√T) 收敛保证；KL 对照避免权重塌缩。
- **适用条件 / 局限** · 有界成本与组定义对保证至关重要。

**可复用机制** · 最坏组优化时同时监控组权重和目标值，将稳定权重的正则单独消融。

<a id="paper-152765"></a>

## Federated Graph Learning with Local Message Compensation

[官方论文页](https://neurips.cc/virtual/2026/poster/152765) · [作者来源](https://openreview.net/forum?id=QXvATxXC7l)

- **问题 / 瓶颈** · 分割图使外部邻居的结构与语义消息丢失。
- **核心创新 / 方法** · 分别用语义代理补语义，用社区锚点约束补偿后的结构。
- **Baseline** · 联邦图学习基线，具名方法待核。
- **Benchmark** · 12 个同质和异质图数据集，含高度碎片化条件。
- **关键结果 / 消融** · 作者报告在所比方法中表现较优，碎片化条件更稳健。
- **适用条件 / 局限** · 代理与真实外邻居关系可能失配。

**可复用机制** · 按语义与拓扑两类缺失分别建立代理，并随切图比例测试。

<a id="paper-150671"></a>

## Federated Learning by Utility-Constrained Stochastic Aggregation for Improving Rational Participation

[官方论文页](https://neurips.cc/virtual/2026/poster/150671) · [作者来源](https://openreview.net/forum?id=gM2WzBs4Gb)

- **问题 / 瓶颈** · 跨机构参与方可能因本地收益不足退出。
- **核心创新 / 方法** · 以客户端效用可行性约束全局目标，并用随机聚合维持参与。
- **Baseline** · 默认客户端被动参与的联邦训练方法。
- **Benchmark** · 标准数据集，评估客户端留存与全局表现。
- **关键结果 / 消融** · 作者报告留存与全局模型表现同时提高，数值待核。
- **适用条件 / 局限** · 收益阈值需定义并估计，策略性行为边界待核。

**可复用机制** · 设计协作机制时应对照仅优化全局质量与加入本地退出阈值的效果。

<a id="paper-151627"></a>

## Federated Logic Gate Networks via Boolean Feature Selection

[官方论文页](https://neurips.cc/virtual/2026/poster/151627) · [作者来源](https://openreview.net/forum?id=Z9KHpOrNHS)

- **问题 / 瓶颈** · 参数平均可能改变离散门函数，并在异质数据下失效。
- **核心创新 / 方法** · 聚合各类别与门的触发统计，筛选硬化的布尔特征，可加入多样性约束。
- **Baseline** · 参数空间合并、其他无数据方案及集中式 BFS。
- **Benchmark** · 非 IID 布尔网络合并，测准确率及逻辑综合后单元数。
- **关键结果 / 消融** · 所提聚合与集中式 BFS 等价；作者报告极端非 IID 下更稳且部署单元较少。
- **适用条件 / 局限** · 依赖共享门定义、留出统计与可比较类别。

**可复用机制** · 合并离散网络时优先在共有的功能坐标系选择组件，并检验综合后是否等价。

<a id="paper-154090"></a>

## Federated Unlearning with Gradient Adaptive Shaping

[官方论文页](https://neurips.cc/virtual/2026/poster/154090) · [作者来源](https://openreview.net/forum?id=GJ1Wmjsdsm)

- **问题 / 瓶颈** · 本地遗忘过强、全局更新冲突都会损害保留端。
- **核心创新 / 方法** · 将原预测作为有界偏好目标的负参考，再向兼容保留客户端的方向投影。
- **Baseline** · 重新训练及联邦遗忘基线，具体名称待核。
- **Benchmark** · 比较遗忘有效性与保留数据准确率。
- **关键结果 / 消融** · 作者给出保留域经验风险不增及相对重训的超额风险分析，并报告实证收益。
- **适用条件 / 局限** · 风险保证依赖理论假设；不能用保留精度替代遗忘实测。

**可复用机制** · 分别消融本地更新约束和聚合投影，联合报告遗忘与保留效用。

<a id="paper-153323"></a>

## Federate the Router: Learning Language Model Routers with Sparse and Decentralized Evaluations

[官方论文页](https://neurips.cc/virtual/2026/poster/153323) · [作者来源](https://openreview.net/forum?id=MABQINnqfs)

- **问题 / 瓶颈** · 单个客户端只覆盖有限查询类型和模型。
- **核心创新 / 方法** · 针对 MLP 和 K-means 路由器，在客户端评估覆盖不一致时学习共享策略。
- **Baseline** · 仅用客户端本地评估训练的路由器。
- **Benchmark** · 两个基准，评估质量与推理成本前沿。
- **关键结果 / 消融** · 作者报告联邦协作改善准确率与成本折衷，并给出路由次优性分析。
- **适用条件 / 局限** · 适用于离线查询模型评分；评估口径及模型可用性需一致。

**可复用机制** · 训练路由器时同时测查询域外泛化和本地从未评估过的模型覆盖。

<a id="paper-153075"></a>

## FedIBS: Federated Vision-Language Adaptation via Intrinsic Bias Selection

[官方论文页](https://neurips.cc/virtual/2026/poster/153075) · [作者来源](https://openreview.net/forum?id=OBeuu8d4RS)

- **问题 / 瓶颈** · 添加外部适配模块会增加推理开销，异质客户端仍需个体化。
- **核心创新 / 方法** · 只微调前馈投影偏置，以 Fisher 引导的逐步掩码区分共享与私有坐标。
- **Baseline** · 联邦提示微调与联邦 adapter。
- **Benchmark** · 多数据集、多异质程度的 VLM 个体化和泛化。
- **关键结果 / 消融** · 作者报告更低通信开销及更好表现，推理无额外模块。
- **适用条件 / 局限** · 偏置适配容量有限；掩码随域变化的稳定性待查。

**可复用机制** · 固定通信预算时，把增设适配模块和筛选骨干内生参数分别评估。

<a id="paper-156743"></a>

## FedIndex: Federated Domain Adaptation with Continuous Domain Indices

[官方论文页](https://neurips.cc/virtual/2026/poster/156743) · [作者来源](https://openreview.net/forum?id=fnbGFH0330)

- **问题 / 瓶颈** · 类别标签无法描述域间平滑变化。
- **核心创新 / 方法** · 利用全局判别器在不访问客户端原始数据的条件下对齐连续索引对应的分布。
- **Baseline** · 先前联邦域适配方法，具名基线待核。
- **Benchmark** · 合成及真实数据集的联邦域迁移。
- **关键结果 / 消融** · 作者报告理论支持域不变特征形成，并在所测数据上优于对照。
- **适用条件 / 局限** · 索引需能表达变化；外推到未覆盖索引的能力待核。

**可复用机制** · 用连续测量值描述数据偏移，并分开衡量索引区间内插值与区间外外推。

<a id="paper-148442"></a>

## FedLoVA: Value-Only Aggregation for Federated LoRA Fine-Tuning of Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148442) · [作者来源](https://openreview.net/forum?id=xlkHd6pwR7)

- **问题 / 瓶颈** · 不同投影更新速度不同，统一同步增加开销。
- **核心创新 / 方法** · 分别测 Q 和 V 的收敛后，只向服务器共享 V 的 LoRA 更新。
- **Baseline** · 既有联邦语言模型微调基线。
- **Benchmark** · 自然语言理解、多语种情感分析与生成任务。
- **关键结果 / 消融** · 作者报告通信成本最高减少至约 1/7.8，性能相近。
- **适用条件 / 局限** · 收益可能取决于骨干、任务和客户端异质性。

**可复用机制** · 在通信受限时按子模块测收敛，比较全部同步与只同步稳定活跃模块。

<a id="paper-151499"></a>

## FedPeel: Peeling Stabilized Layers for Robust Heterogeneous Federated Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151499) · [作者来源](https://openreview.net/forum?id=aD69yKg1Sj)

- **问题 / 瓶颈** · 不加区分地聚合代理模型可能导致震荡与负迁移。
- **核心创新 / 方法** · 选择稳定层，在频域分解共享与个体信息，并按样本教师置信度调节知识转移。
- **Baseline** · 异构联邦代理蒸馏方法，具体名称待核。
- **Benchmark** · 图像、文本与音频基准，衡量准确率、通信量和收敛。
- **关键结果 / 消融** · 作者给出 O(1/T) 收敛率并报告准确率和通信效率改善。
- **适用条件 / 局限** · 多种改变并用，各自独立增益和稳定判定待全文核查。

**可复用机制** · 用逐层稳定性决定通信时机，再用样本置信度控制哪些蒸馏信号可迁移。

<a id="paper-155040"></a>

## FedProG: Federated Graph Learning via Server-Side LLM Semantic Bridging and Uncertainty-Aware Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/155040) · [作者来源](https://openreview.net/forum?id=8tUxcQWc2X)

- **问题 / 瓶颈** · 跨客户端的邻域缺失限制图消息传递。
- **核心创新 / 方法** · 冻结服务端语言模型，根据软提示生成虚拟邻居，以多路径采样过滤不确定结果，并在客户端做语义一致性投影。
- **Baseline** · 图补全基线，名称待核。
- **Benchmark** · 跨域非独立同分布的文本属性图，数据集与度量待核。
- **关键结果 / 消融** · 作者报告泛化改善且客户端开销下降。
- **适用条件 / 局限** · 依赖服务端模型与提示隐私预算，实测成本待核。

**可复用机制** · 将补全质量和客户端开销分开测量，并按置信度筛除生成邻居。

<a id="paper-149139"></a>

## FedReCall: Recalling Client-Specific Directions in Federated LoRA Fine-tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/149139) · [作者来源](https://openreview.net/forum?id=sY42gw5mw5)

- **问题 / 瓶颈** · 分别平均 LoRA 因子可能削弱客户端独有方向。
- **核心创新 / 方法** · 比较本地与聚合更新的奇异方向，在私有缓存保存可信方向，用单批损失探测控制旁路启用。
- **Baseline** · 现有 FedLoRA 聚合器及无旁路对照。
- **Benchmark** · 联邦语言模型适配，比较个性化与全局表现。
- **关键结果 / 消融** · 作者报告个性化改善，多数聚合器全局指标改善。
- **适用条件 / 局限** · 依赖客户端能保存历史缓存，单批探测误差待核。

**可复用机制** · 比较找回本地方向与直接扩大适配器秩的个性化效果。

<a id="paper-148199"></a>

## FedRSPO+: A Heterogeneity-aware Algorithm for Decision-focused Federated Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/148199) · [作者来源](https://openreview.net/forum?id=zbsbqMhkWi)

- **问题 / 瓶颈** · 细小预测误差可导致多面体问题最优解跳变。
- **核心创新 / 方法** · 用投影正则平滑决策映射，再按退火训练并兼容联邦聚合。
- **Baseline** · 纯预测联邦学习与决策导向框架。
- **Benchmark** · 合成背包、最短路径及 PJM 电价案例，改变异质性和通信预算。
- **关键结果 / 消融** · 给出决策误差与遗憾上界，异质性界在同质时消失，无需强凸。
- **适用条件 / 局限** · 论文证据集中于所设结构化决策问题。

**可复用机制** · 分别改变目标函数和可行域，比较代理平滑前后的决策损失及更新稳定性。

<a id="paper-156778"></a>

## Fed-SB: A Silver Bullet for Extreme Communication Efficiency and Performance in (Private) Federated LoRA Fine-Tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/156778) · [作者来源](https://openreview.net/forum?id=87UyFEhzyP)

- **问题 / 瓶颈** · 独立平均低秩因子可能不能还原实际更新。
- **核心创新 / 方法** · 采用 LoRA-SB，固定左右因子，仅训练并平均夹在中间的方阵。
- **Baseline** · 传统适配器平均及高通信替代方法。
- **Benchmark** · 常识、算术和语言推断，比较通信成本与任务表现。
- **关键结果 / 消融** · 摘要报告通信成本最多降低 230 倍。
- **适用条件 / 局限** · 需要共享适配基；秩与隐私预算细节待核。

**可复用机制** · 对齐客户端基底后再聚合中间参数，测实际更新误差与传输量。

<a id="paper-151822"></a>

## FedSEM: Mitigating Cross-Client Evidence Drift in Federated Multiple Instance Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151822) · [作者来源](https://openreview.net/forum?id=XhoxhpfjPV)

- **问题 / 瓶颈** · 包级标签下不同客户端可能学到不一致的实例证据。
- **核心创新 / 方法** · 由本地注意力挑出高置信实例，压缩并在服务端去重、保多样性和校准分数。
- **Baseline** · 联邦多实例学习基线。
- **Benchmark** · 异质联邦多实例任务，数据和指标待核。
- **关键结果 / 消融** · 作者报告性能与泛化改善，额外传输有限。
- **适用条件 / 局限** · 原型仍可能携带隐私信息，隐私保证待核。

**可复用机制** · 固定通信预算对照只聚合参数和额外共享实例原型。

<a id="paper-153586"></a>

## FedSOUL: Federated Continual Unlearning via Spectral Orthogonality

[官方论文页](https://neurips.cc/virtual/2026/poster/153586) · [作者来源](https://openreview.net/forum?id=KKJDo7EkPM)

- **问题 / 瓶颈** · 连续请求会因参数方向重叠损害此前遗忘。
- **核心创新 / 方法** · 在共享正交频谱基中分配子空间，并传输稀疏更新系数。
- **Baseline** · 常规联邦遗忘方法。
- **Benchmark** · 最多十次连续遗忘请求下的遗忘与效用。
- **关键结果 / 消融** · 作者报告权衡更稳定，系数空间更新正交。
- **适用条件 / 局限** · 函数层面的保持依赖投影梯度泄漏受限。

**可复用机制** · 同时测试更新正交性与此前遗忘样本的函数表现。

<a id="paper-148309"></a>

## FedTrace: Generated-Content-Based Watermark Verification for Traitor Tracing in Federated Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/148309) · [作者来源](https://openreview.net/forum?id=ynVmgUSGjZ)

- **问题 / 瓶颈** · 传统验证往往需要权重或可查询服务。
- **核心创新 / 方法** · 以生成内容的稳定标识作为归因证据，比较单客户端和联合泄漏的验证结果。
- **Baseline** · 需要权重或在线查询的追踪方案，具名对照待核。
- **Benchmark** · 定制扩散数据、底座与联邦设置。
- **关键结果 / 消融** · 报告局部适配后仍能检测标识，联合来源区分改善。
- **适用条件 / 局限** · 来源归因需考虑误报和适配强度，数值待核。

**可复用机制** · 用独立验证区分追踪成功、误归因和正常生成质量。

<a id="paper-152313"></a>

## FedVaccine: Knowledge Recall after Spatial-Temporal Catastrophic Forgetting in Federated Continual Learning via Gradient-Based Vaccine

[官方论文页](https://neurips.cc/virtual/2026/poster/152313) · [作者来源](https://openreview.net/forum?id=U1jzG8noWv)

- **问题 / 瓶颈** · 持续强保留可能压制新任务适应，而生成式回放开销大。
- **核心创新 / 方法** · 从本地任务梯度压缩合成小样本集，按任务回放并聚合。
- **Baseline** · 持续学习对照，具名方法待核。
- **Benchmark** · 三个持续联邦基准，名称待核。
- **关键结果 / 消融** · 报告无需训练回放生成器即可快速恢复。
- **适用条件 / 局限** · 梯度压缩的覆盖及隐私边界待核。

**可复用机制** · 在同等训练预算下分开测新任务塑性和旧任务恢复速度。

<a id="paper-153077"></a>

## FedVSSAM: Mitigating Flatness Incompatibility in Sharpness-Aware Federated Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/153077) · [作者来源](https://openreview.net/forum?id=OB02U98b9E)

- **问题 / 瓶颈** · 客户端各自偏好的平坦区域可能与全局目标不一致。
- **核心创新 / 方法** · 构造方差抑制方向并贯穿 SAM 搜索和更新。
- **Baseline** · 联邦 SAM 与其他联邦基线。
- **Benchmark** · 异质联邦学习设置，考虑局部更新与设备部分参与。
- **关键结果 / 消融** · 作者给出非凸收敛保证并报告优于基线。
- **适用条件 / 局限** · 额外估计成本和极端异质性下效果待核。

**可复用机制** · 不要只测客户端平坦度，另测方向偏离和全局表现。

<a id="paper-139671"></a>

## Feedback Forensics: A Toolkit to Measure AI Personality

[官方论文页](https://neurips.cc/virtual/2026/poster/139671) · [作者来源](https://openreview.net/forum?id=BefK8Kp2pO)

- **问题 / 瓶颈** · 综合排序会掩盖谄媚或语气偏移。
- **核心创新 / 方法** · 自适应发现行为特征，并跟踪反馈数据及模型输出。
- **Baseline** · 相对偏好排名；没有具名量化对照。
- **Benchmark** · Chatbot Arena、MultiPref、PRISM 与常见语言模型。
- **关键结果 / 消融** · 展示特征可在反馈与输出两侧追踪，摘要未量化。
- **适用条件 / 局限** · 特征定义和标注一致性待核。

**可复用机制** · 发布模型时把行为特征回归测试加入总偏好分以外的监测。

<a id="paper-152267"></a>

## Feedback World Model Enables Precise Guidance of Diffusion Policy

[官方论文页](https://neurips.cc/virtual/2026/poster/152267) · [作者来源](https://openreview.net/forum?id=ULmPp5GXSX)

- **问题 / 瓶颈** · 分布外状态下静态动力学预测偏差会累积。
- **核心创新 / 方法** · 仅在线更新轻量潜空间反馈状态，并突出可由动作控制的预测成分。
- **Baseline** · 静态预测及普通引导，具名对照待核。
- **Benchmark** · LIBERO-Plus、Robomimic 和真机操作。
- **关键结果 / 消融** · 预测误差最多降低 76.4%，分布外成功率提高 30%。
- **适用条件 / 局限** · 需要执行后观测，收敛依赖潜空间观察器条件。

**可复用机制** · 分别消融反馈修正和动作引导以区分预测精度和控制收益。

<a id="paper-150475"></a>

## Feed-Forward 3D Gaussian Splatting for High-Fidelity Animatable Hand Avatar Reconstruction from a Single Image

[官方论文页](https://neurips.cc/virtual/2026/poster/150475) · [作者来源](https://openreview.net/forum?id=hlvxGsP8zJ)

- **问题 / 瓶颈** · 单视角下未观测区域易被错误外观更新污染。
- **核心创新 / 方法** · 先建立规范手部几何，再按渲染贡献选择性更新高斯。
- **Baseline** · 多视图、逐主体优化和单图方法，具名结果待核。
- **Benchmark** · 单目可动画手部重建与渲染。
- **关键结果 / 消融** · 作者报告画质和量化表现较强。
- **适用条件 / 局限** · 遮挡区域缺少直接证据，未见姿态泛化待核。

**可复用机制** · 将表面外观更新受可见性和渲染贡献约束，与全局外观回归对照。

<a id="paper-149287"></a>

## Feedforward Novel View Synthesis for Heterogeneous Cameras

[官方论文页](https://neurips.cc/virtual/2026/poster/149287) · [作者来源](https://openreview.net/forum?id=rQBdZ03odN)

- **问题 / 瓶颈** · 中心射线不能区分各相机中图块的投影覆盖。
- **核心创新 / 方法** · 引入局部射线图，并用角坐标替代像素网格做二维 RoPE。
- **Baseline** · 现有相机条件的新视角合成方法。
- **Benchmark** · ScanNet++ 混合相机与未见全景投影。
- **关键结果 / 消融** · 报告混合相机表现改善及全景零样本泛化。
- **适用条件 / 局限** · 要求相机标定且采用适用的中心相机模型。

**可复用机制** · 比较只编码图块中心和保留图块角覆盖的信息量。

<a id="paper-150142"></a>

## Feeling of Knowing in Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150142) · [作者来源](https://openreview.net/forum?id=kMAaCSiUd6)

- **问题 / 瓶颈** · 知识变化可能与自评信号不同步。
- **核心创新 / 方法** · 独立知识更新和自评通道，用中间知识状态训练校准器，再据判断优化回答行为。
- **Baseline** · 后训练前的自评和未显式对齐的模型。
- **Benchmark** · 三个知识更新评测集，名称及指标待核。
- **关键结果 / 消融** · 报告更新知识上的判断质量改善。
- **适用条件 / 局限** · 需追踪中间知识状态，跨主题稳健性待核。

**可复用机制** · 在每轮知识更新后以新旧知识分组检验检索触发与弃答。

<a id="paper-148321"></a>

## Felid: A Flexible and Efficient Design for Transformer Fine-Tuning over Encrypted Data

[官方论文页](https://neurips.cc/virtual/2026/poster/148321) · [作者来源](https://openreview.net/forum?id=yglphSefi0)

- **问题 / 瓶颈** · 加密矩阵运算和刷新开销主导训练。
- **核心创新 / 方法** · 采用可变批打包，减少旋转和重线性化，并在函数自举中合并逐元素激活。
- **Baseline** · 近期同态加密微调系统。
- **Benchmark** · 两层 BERT 风格模型，批大小 16，测密文原语和时间。
- **关键结果 / 消融** · 旋转及重线性化减少约 30 倍，自举减少约 2.5 倍，训练 650 秒约快 8 倍。
- **适用条件 / 局限** · 扩展到深层模型的通信和内存待核。

**可复用机制** · 先按原语计数剖析加密训练，再比较打包和融合优化。

<a id="paper-149434"></a>

## FELPS: Fair and Efficient Scheduling for Multi-LoRA Serving System

[官方论文页](https://neurips.cc/virtual/2026/poster/149434) · [作者来源](https://openreview.net/forum?id=q6S0veB7O2)

- **问题 / 瓶颈** · 频繁切换适配器有利于公平但增加搬运成本。
- **核心创新 / 方法** · 把比例公平得分和加载状态优先级分离，由权重调节。
- **Baseline** · 多 LoRA 服务调度基线。
- **Benchmark** · 真实服务负载下公平性和效率权衡。
- **关键结果 / 消融** · 报告优于各对照，量化幅度待核。
- **适用条件 / 局限** · 需要监测适配器负载和驻留状态。

**可复用机制** · 扫描公平权重并绘制公平效率曲线，避免用单点吞吐替代公平性。

<a id="paper-155313"></a>

## FENet: Functional Embedding Neural Network for Change-Point Detection in Functional Time Series

[官方论文页](https://neurips.cc/virtual/2026/poster/155313) · [作者来源](https://openreview.net/forum?id=6WmRBxSI5l)

- **问题 / 瓶颈** · 服务器曲线是高维异构函数型时间序列。
- **核心创新 / 方法** · 基于函数型 CUSUM 和神经表示的联系学习变化点规则。
- **Baseline** · 传统变化点方法，名称待核。
- **Benchmark** · 模拟及真实服务器运行指标，含训练与测试分布不一致。
- **关键结果 / 消融** · 报告有限数据下稳健，可定位运行指标异常。
- **适用条件 / 局限** · 真实变化标注与误报情况待核。

**可复用机制** · 分别测告警误报和定位误差，并加入跨环境的运维曲线检验。

<a id="paper-151723"></a>

## FEP-Agent: Grounding LLM Agent Self-Evolution in Active Inference with Semantic Memory

[官方论文页](https://neurips.cc/virtual/2026/poster/151723) · [作者来源](https://openreview.net/forum?id=YaCXhGOZpn)

- **问题 / 瓶颈** · 执行与知识构建各自独立时可能积累未验证记忆。
- **核心创新 / 方法** · 执行者兼顾目标和探索，构建者用反事实验证约束记忆复杂度，以关联社区组织索引。
- **Baseline** · 记忆型 Agent 基线，具名对照待核。
- **Benchmark** · 多个 Agent 基准，数据与度量待核。
- **关键结果 / 消融** · 报告总体性能改善；消融待核。
- **适用条件 / 局限** · 依赖知识验证质量和可检索组织。

**可复用机制** · 在良性任务内独立比较主动探索和记忆写入验证的贡献。

<a id="paper-152029"></a>

## FerQ: Fermat Quotient Reformulation of High-Order Binary Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/152029) · [作者来源](https://openreview.net/forum?id=W4U6AMYhfN)

- **问题 / 瓶颈** · 高阶能量难直接交给二次优化器。
- **核心创新 / 方法** · 用标量聚合上的费马商组合表示单项式，另推导量子退火的二次嵌入。
- **Baseline** · 十二种已有能量变换。
- **Benchmark** · 四个来源的 k-SAT、Max-k-SAT 及随机玻璃和局域哈密顿量。
- **关键结果 / 消融** · 报告最高满足率与最低 CPU 时间。
- **适用条件 / 局限** · 重写不取消组合求解难度，嵌入开销仍随设定而异。

**可复用机制** · 对比变换规模、求解耗时及最终能量，避免只衡量辅助变量数。

<a id="paper-154544"></a>

## Ferrogen: Generative Pipeline for Guided Search of Novel Ferroelectric Material for Logic and Memory

[官方论文页](https://neurips.cc/virtual/2026/poster/154544) · [作者来源](https://openreview.net/forum?id=CnO0wbQ24u)

- **问题 / 瓶颈** · 穷举与反复高精度计算筛选昂贵。
- **核心创新 / 方法** · 用带属性条件的晶体生成模型提议候选，代理筛选后以 DFT 验证。
- **Baseline** · 穷举数据库搜索与基础晶体生成模型。
- **Benchmark** · 铁电存储材料的极化、开关能量与绝缘性质。
- **关键结果 / 消融** · 按代理筛选口径约提高 80 倍搜索效率，另用 DFT 验证候选。
- **适用条件 / 局限** · 效率数字来自代理筛选，理论候选不等于器件实验验证。

**可复用机制** · 将生成器筛选效率与独立物理验证通过率分开汇报。
