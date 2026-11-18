# NeurIPS 2026 论文卡 3

[会议索引](README.md)

<a id="paper-149967"></a>

## Causal Concept Explanations for Deep Neural Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149967) · [作者来源](https://openreview.net/forum?id=lrgD8sYBzf)

- **问题 / 瓶颈** · 相关概念可能无法驱动模型输出
- **核心创新 / 方法** · 用概念流生成反事实样本，以中介分析约束概念作用
- **Baseline** · 相关式概念解释，具名对照待核
- **Benchmark** · 控制、驾驶及细粒度分类
- **关键结果 / 消融** · 作者展示概念级因果归因，量化待核
- **适用条件 / 局限** · 依赖可用概念和反事实样本质量

**可复用机制** · 分别评估移除概念和，仅保留概念时的输出变化

<a id="paper-139553"></a>

## CausalConflictBench: Can Multimodal Models Follow Local Mechanisms That Conflict with Commonsense?

[官方论文页](https://neurips.cc/virtual/2026/poster/139553) · [作者来源](https://openreview.net/forum?id=IzbN000ZNL)

- **问题 / 瓶颈** · 规则与常识一致时无法区分答对原因
- **核心创新 / 方法** · 分别构造显式文本规则和视觉规则归纳并测成组严格准确率
- **Baseline** · 十四种开源和闭源多模态模型
- **Benchmark** · CausalConflictBench，测组准确率及常识回退
- **关键结果 / 消融** · 单题高分掩盖不稳定性，错误集中在常识答案
- **适用条件 / 局限** · 受规则构造与语言模板覆盖限制

**可复用机制** · 加入常识相反的配对病例并区分归纳与应用失败

<a id="paper-151347"></a>

## Causal Discovery from Unseen Environments

[官方论文页](https://neurips.cc/virtual/2026/poster/151347) · [作者来源](https://openreview.net/forum?id=bDH6pbl4W5)

- **问题 / 瓶颈** · 推断未知干预位置代价高
- **核心创新 / 方法** · 在线性高斯结构下分析合并数据如何诱发近独立非高斯噪声
- **Baseline** · 使用环境标签的方法
- **Benchmark** · 合成多干预环境与真实数据
- **关键结果 / 消融** · 合成表现可比或更好，真实数据可比
- **适用条件 / 局限** · 依赖线性结构和特定干预条件

**可复用机制** · 在复杂环境推断前保留经典 ICA 基线

<a id="paper-152473"></a>

## Causal Discovery over Clusters of Variables in Non-Markovian Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/152473) · [作者来源](https://openreview.net/forum?id=SoPlIu3TgX)

- **问题 / 瓶颈** · 现有聚簇发现常假设因果充分性
- **核心创新 / 方法** · 定义适用隐混杂的图等价类并给出可靠算法
- **Baseline** · 假设因果充分的簇级方法
- **Benchmark** · 理论比较可学习的簇间关系
- **关键结果 / 消融** · 给出算法可靠性，摘要未报告实证
- **适用条件 / 局限** · 需满足论文的图模型与背景知识假设

**可复用机制** · 先判断聚簇层的未观测混杂，再选择可识别的关系等级

<a id="paper-153240"></a>

## Causal Discovery Under Hard Selection Bias: A New Robust Score-Matching Approach

[官方论文页](https://neurips.cc/virtual/2026/poster/153240) · [作者来源](https://openreview.net/forum?id=Mhcp2GSL1c)

- **问题 / 瓶颈** · 非随机截断扭曲观测分布
- **核心创新 / 方法** · 利用确定性截断保留支持域内部联合分数及其雅可比的性质调整分数匹配
- **Baseline** · 既有分数匹配算法
- **Benchmark** · 有无截断的加性噪声模型；细项待核
- **关键结果 / 消融** · 作者报告截断下更稳健，无截断时与先进方法相近
- **适用条件 / 局限** · 依赖确定性截断与加性噪声假设

**可复用机制** · 筛选机制不可见时优先检验分数结构是否仍可用，并分别测截断边界内外

<a id="paper-152445"></a>

## Causal Discovery under Time-Varying Delays

[官方论文页](https://neurips.cc/virtual/2026/poster/152445) · [作者来源](https://openreview.net/forum?id=T4HWDl4y39)

- **问题 / 瓶颈** · 固定滞后可能把时延变化误当成机制变化
- **核心创新 / 方法** · 以算法因果模型定义变化时延，使用 STRETCH 恢复图
- **Baseline** · 固定时延或系数漂移建模路线；具名对照待核
- **Benchmark** · 合成数据因果图恢复及厄尔尼诺与印度季风案例
- **关键结果 / 消融** · 作者报告合成图恢复成功；案例仅说明适用性
- **适用条件 / 局限** · 可辨识条件和准确定时要求待核

**可复用机制** · 比较固定与变化时延模型时，独立扫描时延变化和因果强度变化

<a id="paper-149402"></a>

## Causal Discovery via Transformed Low-Rank Quantile Surfaces

[官方论文页](https://neurips.cc/virtual/2026/poster/149402) · [作者来源](https://openreview.net/forum?id=qKXBoHz41o)

- **问题 / 瓶颈** · 位置尺度模型难表达条件分布的形状变化
- **核心创新 / 方法** · 交替进行低秩拟合与单调变换估计，按方向比较曲面可表示性
- **Baseline** · 位置尺度与后非线性异方差方法
- **Benchmark** · 合成形状变化和非线性失真及标准双变量基准
- **关键结果 / 消融** · 作者证明一般可辨识，并报告复杂形状变化下表现更好
- **适用条件 / 局限** · 针对双变量及低秩假设，特殊边际可能不可辨识

**可复用机制** · 遇到方向间尺度拟合接近时，比较更一般的条件分位曲面残差

<a id="paper-151569"></a>

## Causal Discovery with False Positive Error Control

[官方论文页](https://neurips.cc/virtual/2026/poster/151569) · [作者来源](https://openreview.net/forum?id=ZbSa2GSJNV)

- **问题 / 瓶颈** · 常见因果发现保证偏渐近且要求较强忠实性
- **核心创新 / 方法** · 以保守 PC 结合 BY 型条件独立检验和保守定向，用参数 m 交换复杂度与假设强度
- **Baseline** · 传统 PC 与现有渐近保证；实验对照待核
- **Benchmark** · 线性高斯设定下有限样本 FDR
- **关键结果 / 消融** · 作者证明在弱忠实性条件下可控制有限样本错误发现率
- **适用条件 / 局限** · 受线性高斯、检验条件和 m 复杂度约束

**可复用机制** · 对高代价因果结论显式报告方向模糊项，以图蕴含的独立关系定义误报

<a id="paper-139161"></a>

## CausalDriveBench: Evaluating Causal Reasoning in Vision-Language-Action Models for Autonomous Driving

[官方论文页](https://neurips.cc/virtual/2026/poster/139161) · [作者来源](https://openreview.net/forum?id=hdSw2TGIXo)

- **问题 / 瓶颈** · 观察场景中轨迹准确或理由流畅不足以检验因果理解
- **核心创新 / 方法** · 用因果场景图标注实体相关性，并为场景变动提供问答及参考轨迹
- **Baseline** · 10 个驾驶 VLA 与 3 个通用 VLM，另有共享语言骨干对照
- **Benchmark** · nuScenes 衍生 7285 组问答与 1000 条反事实轨迹
- **关键结果 / 消融** · 最高问答准确率 70.6%，问答与轨迹表现跨模型无统计相关
- **适用条件 / 局限** · 依赖场景图和参考轨迹质量；为离线评测

**可复用机制** · 把同一反事实同时用于语言和动作输出，分别报告是否过度响应或忽视变化

<a id="paper-153668"></a>

## Causal Edit Serialization

[官方论文页](https://neurips.cc/virtual/2026/poster/153668) · [作者来源](https://openreview.net/forum?id=Jed6Feg5uv)

- **问题 / 瓶颈** · 编辑位置直接作为文本生成易无效
- **核心创新 / 方法** · 用编辑语言、定位头和双索引旋转位置编码保留因果掩码
- **Baseline** · 标准自回归与文本位置 DSL
- **Benchmark** · WikiAtomic 和 CoEdIT 式修订及算术
- **关键结果 / 消融** · 作者报告目标相似度和有效编辑率提高，最佳设置普通语言建模小幅下降
- **适用条件 / 局限** · 依赖可解析编辑监督，复杂文档扩展待核

**可复用机制** · 把操作预测和源位置定位拆成独立输出，分别测地址准确率和编辑有效性

<a id="paper-149771"></a>

## Causal Effect Identification with a Single Agnostic Proxy

[官方论文页](https://neurips.cc/virtual/2026/poster/149771) · [作者来源](https://openreview.net/forum?id=nQbOFhMDIB)

- **问题 / 瓶颈** · 代理与处理和结果的连边未知，简单校正公式不足
- **核心创新 / 方法** · 在线性非高斯无环模型中以累积量提出候选，再用独立关系筛解
- **Baseline** · 需要结构已知或多个代理的路线；具名对照待核
- **Benchmark** · 观测总体分布的识别定理及实证验证
- **关键结果 / 消融** · 作者证明可识别时找出真值，不可识别时报告失败
- **适用条件 / 局限** · 总体分布结论不直接保证有限样本性能

**可复用机制** · 代理结构未知时先做可识别性检查，再决定是否报告效应点估计

<a id="paper-149288"></a>

## Causal Effects with Unobserved Unit Types in Interacting Human–AI Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/149288) · [作者来源](https://openreview.net/forum?id=rPEiQxSWEc)

- **问题 / 瓶颈** · 交互平台无法逐个辨别人和代理，干预还会扩散
- **核心创新 / 方法** · 用人类类型概率构建分组，在因果消息传递框架下比较组均值
- **Baseline** · 整体混合效应作为问题参照；具名对照待核
- **Benchmark** · 行为差异化语言代理模拟平台及识别分析
- **关键结果 / 消融** · 作者给出一致恢复人类特异效应的条件，并报告模拟验证
- **适用条件 / 局限** · 依赖可信的人类类型先验和分组变化，真实平台效果待核

**可复用机制** · 设计混合用户平台实验时，用分组组成变化识别子群效应并检验先验偏差

<a id="paper-154373"></a>

## Causal Evaluation of Membership Inference Attacks

[官方论文页](https://neurips.cc/virtual/2026/poster/154373) · [作者来源](https://openreview.net/forum?id=E37QGIQj5A)

- **问题 / 瓶颈** · 低成本隐私评测可能把样本来源差异当成记忆
- **核心创新 / 方法** · 把记忆定义成纳入训练的因果效应，为不同重训预算设计评测估计量
- **Baseline** · 多次重训、单次随机纳入、事后评测协议
- **Benchmark** · 预训练和微调语言模型的隐私评测；具体数据待核
- **关键结果 / 消融** · 作者报告所提评测在分布偏移下仍能可靠衡量隐私风险
- **适用条件 / 局限** · 依赖估计条件；结论关于测量有效性

**可复用机制** · 比较隐私保护措施前，在受控数据上核验成员与非成员的分布和训练干扰

<a id="paper-155379"></a>

## Causal-Geo: Neuro-Symbolic Spatial Grounding for Situated Agent Planning

[官方论文页](https://neurips.cc/virtual/2026/poster/155379) · [作者来源](https://openreview.net/forum?id=642y9PfzJm)

- **问题 / 瓶颈** · 语义模型可能提出物理上不可达的计划
- **核心创新 / 方法** · 将语言意图转成势函数调节空间度量，再用图搜索求近似测地路线
- **Baseline** · 强化学习及分层语言规划器
- **Benchmark** · 湿地数字孪生与室内导航
- **关键结果 / 消融** · 作者报告稀疏奖励下优于 RL，并减少物理不可行计划
- **适用条件 / 局限** · 依赖可靠几何及约束建模；实际安全边界待核

**可复用机制** · 保留可行性检查器，在不同语义模型和矛盾提示上测路径有效率

<a id="paper-148981"></a>

## Causal Gradient Steering: Exposing Shortcut Gradients by Destroying Causal Signal

[官方论文页](https://neurips.cc/virtual/2026/poster/148981) · [作者来源](https://openreview.net/forum?id=tiohpJvNdL)

- **问题 / 瓶颈** · 域外泛化受标签无关线索干扰
- **核心创新 / 方法** · 在同样本移除任务语义、保留干扰结构，用其梯度约束原始更新方向
- **Baseline** · ERM 与 17 种领域泛化方法；另含 OSTrack 和 SCSD
- **Benchmark** · 五种领域泛化基准、视觉跟踪及分割
- **关键结果 / 消融** · 通用方法最多提高 15.8 个百分点；GTAV 至 ACDC 分割 mIoU 由 35.66 到 36.99
- **适用条件 / 局限** · 移除操作须保留干扰结构，失真检查必需

**可复用机制** · 用相同预算比较增强与语义移除梯度校正，并独立评估语义保留程度

<a id="paper-151770"></a>

## Causal heteroscedastic structure learning from incomplete temporal data

[官方论文页](https://neurips.cc/virtual/2026/poster/151770) · [作者来源](https://openreview.net/forum?id=YB8beKwrFO)

- **问题 / 瓶颈** · 先填补后建图可能制造伪连接，条件异方差加剧偏差
- **核心创新 / 方法** · 以条件流表征噪声，并用最优传输学习随机插补修正
- **Baseline** · 现有时序因果发现与插补路线；具名对照待核
- **Benchmark** · 合成与真实数据，多类缺失机制
- **关键结果 / 消融** · 作者报告跨缺失设置优于对照；幅度待核
- **适用条件 / 局限** · 依赖流模型和可用时序信息；缺失强度边界待核

**可复用机制** · 比较联合学习与两阶段方案时同时测图结构和插补质量

<a id="paper-149757"></a>

## Causal Inference for Sequential Settings under Interference and Latent Confounding

[官方论文页](https://neurips.cc/virtual/2026/poster/149757) · [作者来源](https://openreview.net/forum?id=nZvLqHKKp6)

- **问题 / 瓶颈** · 个体相互影响且存在随时间变化的不可见因素
- **核心创新 / 方法** · 以马尔可夫及 Ising 依赖表示二元结果，使用最大伪似然拟合后模拟效应
- **Baseline** · 具名实验对照待核
- **Benchmark** · 合成面板和美国县级观测案例
- **关键结果 / 消融** · 作者给出非渐近估计一致性结果并报告案例应用
- **适用条件 / 局限** · 要求二元序列及低秩因子结构；案例不替代识别假设

**可复用机制** · 比较有无网络干扰和低秩因素的估计，并对其假设敏感性做分解

<a id="paper-148923"></a>

## Causal learning with the invariance principle

[官方论文页](https://neurips.cc/virtual/2026/poster/148923) · [作者来源](https://openreview.net/forum?id=uC8JCLIwIA)

- **问题 / 瓶颈** · 单环境观测通常不能确定因果方向
- **核心创新 / 方法** · 对跨环境不变的无环结构模型分析双辅助环境的图及机制识别
- **Baseline** · 单环境观测识别作为理论参照
- **Benchmark** · 合成数据及非线性结构因果模型理论
- **关键结果 / 消融** · 作者给出两个辅助环境下图、机制及反事实可识别结论
- **适用条件 / 局限** · 需要论文所设环境变化及不变性条件，非任意环境组合

**可复用机制** · 收集多环境数据前核对变化是否满足识别条件，再检查反事实表现

<a id="paper-154762"></a>

## CausalMix: Data Mixture as Causal Inference for Language Model Training

[官方论文页](https://neurips.cc/virtual/2026/poster/154762) · [作者来源](https://openreview.net/forum?id=B9ShLVNHQD)

- **问题 / 瓶颈** · 固定池上的代理最优配比在新池上可能失效
- **核心创新 / 方法** · 用数据池统计作协变量、混合作处理，在小模型实验上估计条件处理效应
- **Baseline** · RegMix 及其他配比对照
- **Benchmark** · 512 次 Qwen2.5-0.5B 试验，验证 7B 放大与 Qwen3-4B 长推理数据
- **关键结果 / 消融** · 作者报告多项下游任务改善，具体分数待核
- **适用条件 / 局限** · 需要小模型实验覆盖池变化；估计外推依赖重叠条件

**可复用机制** · 在数据池变化时用已有试验估计条件配比，并和重训静态代理比较迁移开销

<a id="paper-153237"></a>

## Causal Multi-Task Demand Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/153237) · [作者来源](https://openreview.net/forum?id=Mk49ilMld8)

- **问题 / 瓶颈** · 跨市场迁移时价格和未观测需求相关
- **核心创新 / 方法** · 条件集包含所有价格但遮去两项需求结果，以外生价格点提供监督
- **Baseline** · 标准迁移学习方法
- **Benchmark** · 真实与合成需求数据，验证价格响应恢复
- **关键结果 / 消融** · 作者给出识别和条件集最大有效性结果，报告恢复改善
- **适用条件 / 局限** · 每任务需要至少两个不同的局部外生价格点

**可复用机制** · 跨任务监督可将混杂调整信息与识别留出的结果分开设计

<a id="paper-148689"></a>

## Causal pieces: analysing and improving spiking neural networks piece by piece

[官方论文页](https://neurips.cc/virtual/2026/poster/148689) · [作者来源](https://openreview.net/forum?id=vmQvISAYfP)

- **问题 / 瓶颈** · 传统线性区分析难处理脉冲时刻不连续
- **核心创新 / 方法** · 按输出脉冲的致因子网划分区域，分析区内连续性及区数与近似误差
- **Baseline** · 不同初始化与已有线性区概念
- **Benchmark** · Yin-Yang、Fashion-MNIST 和 EuroSAT
- **关键结果 / 消融** · 作者报告较多分区与成功训练明显相关，并给出近似误差下界
- **适用条件 / 局限** · 理论适用特定前馈单脉冲 LIF 条件，相关不等价因果

**可复用机制** · 在训练前用训练集估计分区覆盖，并与匹配尺度的初始化比较

<a id="paper-148867"></a>

## Causal Representation Learning for Generalisable Recommendation

[官方论文页](https://neurips.cc/virtual/2026/poster/148867) · [作者来源](https://openreview.net/forum?id=ub2HuIm8hN)

- **问题 / 瓶颈** · 日志由旧策略筛选，离线指标可能误导上线选择
- **核心创新 / 方法** · 用信息论准则及可优化变分下界训练表征，无额外推理开销
- **Baseline** · 同容量生产排序器及辅助对照
- **Benchmark** · 音乐服务数百万用户 A/B、KuaiRand、已知结构的合成基准
- **关键结果 / 消融** · 作者报告离线相近而在线参与度改善，偏移条件有更明显收益
- **适用条件 / 局限** · 目标是偏移泛化，潜在因子完整识别不在保证范围

**可复用机制** · 对日志训练的推荐器同时测试旧日志与反馈偏移环境，验证离线持平条件下的上线效果
