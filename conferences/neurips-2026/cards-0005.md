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
