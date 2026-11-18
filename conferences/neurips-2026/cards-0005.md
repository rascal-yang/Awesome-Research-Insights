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
