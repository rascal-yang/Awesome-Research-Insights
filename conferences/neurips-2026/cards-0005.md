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
