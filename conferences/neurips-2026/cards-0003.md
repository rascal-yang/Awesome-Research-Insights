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

<a id="paper-138913"></a>

## CausalSpatial: A Benchmark for Object-Centric Causal Spatial Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/138913) · [作者来源](https://openreview.net/forum?id=xHoB89Oc4p)

- **问题 / 瓶颈** · 文字推理易脱离场景
- **核心创新 / 方法** · 生成假设动作后的视频作为视觉证据
- **Baseline** · 人类与 GPT-5
- **Benchmark** · 碰撞、兼容性、遮挡、轨迹四类任务
- **关键结果 / 消融** · 人类 84%，GPT-5 54%；模拟模块单独增益待核
- **适用条件 / 局限** · 依赖生成视频的物理可信度

**可复用机制** · 分别评估初始画面和模拟画面条件下的答案及其视觉依据

<a id="paper-153856"></a>

## Causal Survival Forests with Negative Controls

[官方论文页](https://neurips.cc/virtual/2026/poster/153856) · [作者来源](https://openreview.net/forum?id=IDeaI3k5kC)

- **问题 / 瓶颈** · 删失与未测混杂会同时偏置异质效应
- **核心创新 / 方法** · 将代理变量与 Neyman 正交化写入森林损失
- **Baseline** · 现有生存效应估计器，名称待核
- **Benchmark** · 改变代理相关性、混杂及删失的模拟和临床数据
- **关键结果 / 消融** · 模拟中偏差与 RMSE 下降，临床结果包含已知模式
- **适用条件 / 局限** · 依赖负对照识别假设；观测效应须谨慎解释

**可复用机制** · 在同一删失模拟中单独改变代理质量，检验正交调整对效应误差的影响

<a id="paper-150884"></a>

## CausalTab: Pretraining Across Causal Environments for Tabular Causal Discovery

[官方论文页](https://neurips.cc/virtual/2026/poster/150884) · [作者来源](https://openreview.net/forum?id=eg7EMDLpBt)

- **问题 / 瓶颈** · 单一训练环境难迁移到陌生因果图
- **核心创新 / 方法** · 动态组合图先验、噪声及样本规模，训练直接输出因果图的模型
- **Baseline** · 经典及学习式因果发现方法，名称待核
- **Benchmark** · 合成与领域语义结构因果模型，考察分布外结构恢复
- **关键结果 / 消融** · 作者报告结构恢复较稳健，干预证据下尤其明显
- **适用条件 / 局限** · 受训练环境覆盖及可识别性约束

**可复用机制** · 固定骨干和样本数，比较环境多样性与单一先验的迁移收益

<a id="paper-139209"></a>

## Causal-VLM: Dense Causal Captioning in Videos

[官方论文页](https://neurips.cc/virtual/2026/poster/139209) · [作者来源](https://openreview.net/forum?id=eaK7y6VXZW)

- **问题 / 瓶颈** · 独立生成描述忽略事件依赖
- **核心创新 / 方法** · 在密集字幕上构造带因果边的训练数据并联合学习
- **Baseline** · 现有视频语言模型及独立预测方式，名称待核
- **Benchmark** · ActivityNet、YouCook2；因果 F1 与 CIDEr
- **关键结果 / 消融** · 因果 F1 为 0.73 和 0.64，CIDEr 分别增加 6.3 和 7.4
- **适用条件 / 局限** · 自动生成的边可能含误标，因果关系不等于真实干预效应

**可复用机制** · 给事件图增加边监督，检验其能否改善定位及描述

<a id="paper-153157"></a>

## CAVE: A Structured Credit Assignment Approach for Fragmented Visual Evidence Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/153157) · [作者来源](https://openreview.net/forum?id=NT1gZRQtc5)

- **问题 / 瓶颈** · 结果奖励难诊断跨区域推理哪一步有效
- **核心创新 / 方法** · 用 GRPO 在动作级结合信念变化、证据获取和焦点控制
- **Baseline** · 一般视觉推理微调与通用 VLM，具名对照待核
- **Benchmark** · TRACER-Bench 与公共多模态评测
- **关键结果 / 消融** · 摘要报告长距离与深层跨区域依赖下更稳健，幅度待核
- **适用条件 / 局限** · 过程质量依赖中间证据口径

**可复用机制** · 比较最终正确性奖励和动作级证据奖励，按证据跨度分桶

<a id="paper-148652"></a>

## CCDiff: Inverse Canonical Correlation Analysis for Discovering Visual Differences in Natural Language

[官方论文页](https://neurips.cc/virtual/2026/poster/148652) · [作者来源](https://openreview.net/forum?id=w8mxaFucap)

- **问题 / 瓶颈** · 逐图人工比较难扩展，语言模型依赖增加成本
- **核心创新 / 方法** · 先提候选词，再用逆 CCA 提取低相关方向并结合组内代表性排序
- **Baseline** · 依赖大语言模型的集合差异描述
- **Benchmark** · VisDiffBench、MetaShift、MIMIC-CXR
- **关键结果 / 消融** · 摘要报告至少约两倍加速，核心发现阶段无需 LLM token，效果可比或更优
- **适用条件 / 局限** · 依赖候选词表；未覆盖概念可能无法发现

**可复用机制** · 分开测候选概念覆盖率、统计排序精度与推理成本

<a id="paper-154162"></a>

## CC-GS: Low-Memory 3D Gaussian Splatting Training via CPU-GPU Block-Wise Context Compositing

[官方论文页](https://neurips.cc/virtual/2026/poster/154162) · [作者来源](https://openreview.net/forum?id=FoB1Zw7yGu)

- **问题 / 瓶颈** · 独立块训练丢失全图监督，上传全部可见点又占显存
- **核心创新 / 方法** · 先缓存非优化块的颜色和剩余透射，再逐块做可微渲染并异步传输
- **Baseline** · 标准 3DGS、独立块训练及可见点卸载
- **Benchmark** · 标准 3DGS 场景；峰值显存、质量及训练速度
- **关键结果 / 消融** · 测试中低于 2 GB，质量接近标准模型，训练最多慢 1.54 倍
- **适用条件 / 局限** · 增加主机存储和两遍计算开销

**可复用机制** · 有全局合成损失时，以缓存上下文支持局部梯度更新

<a id="paper-148611"></a>

## CCTimeBoost: Learning Time-Varying Relative Risk with Case-Control Boosted Trees

[官方论文页](https://neurips.cc/virtual/2026/poster/148611) · [作者来源](https://openreview.net/forum?id=wSn3dZhijP)

- **问题 / 瓶颈** · 固定风险分数难表示效应随时间交叉或反转
- **核心创新 / 方法** · 对采样风险集做分组排序，再用完整风险集估计基线风险
- **Baseline** · 树与神经生存模型；具名对照待核
- **Benchmark** · 八个右删失基准及模拟时变效应；区分度和校准
- **关键结果 / 消融** · 区分度报告领先，校准有竞争力；模拟可复原交叉风险
- **适用条件 / 局限** · 风险集采样与基线估计依赖删失设定

**可复用机制** · 当固定风险假设可能失效时，对照时变树与比例风险模型

<a id="paper-156085"></a>

## CD-RCM: Generalizable Continuous-Depth Novel View Synthesis for Reflectance Confocal Microscopy

[官方论文页](https://neurips.cc/virtual/2026/poster/156085) · [作者来源](https://openreview.net/forum?id=0WaapzByGt)

- **问题 / 瓶颈** · 面内与轴向分辨率不匹配，普通表面新视角方法不适用
- **核心创新 / 方法** · 按光学分层特点训练前馈模型预测未采集深度
- **Baseline** · 传统神经渲染路线，具体实验对照待核
- **Benchmark** · 稀疏反射式共聚焦皮肤图像栈；合成质量与时延
- **关键结果 / 消融** · 报告亚秒推理及高保真，定量细节待核
- **适用条件 / 局限** · 插值并非新增实测切片；诊断用途须独立验证

**可复用机制** · 对稀疏体成像单独验证轴向成像先验对插值与遮挡的贡献

<a id="paper-152287"></a>

## CECAR: Cache & Expert Co-Aware Routing Accelerates On-Device Inference of MoE LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/152287) · [作者来源](https://openreview.net/forum?id=UBnFBfqZgu)

- **问题 / 瓶颈** · 二元缓存状态会引起路由不稳定
- **核心创新 / 方法** · 联合缓存管理和专家路由，用学习式复用距离预测调整优先级
- **Baseline** · 传统 MoE 推理及整模型驻留主存方案
- **Benchmark** · Qwen3-30B-A3B，16 GB 显存，非驻留专家从 SSD 加载
- **关键结果 / 消融** · 12.5 token/s，较常规方案快 4.5 倍
- **适用条件 / 局限** · 依赖路由改动的质量代价与具体存储带宽

**可复用机制** · 在固定显存下联合测质量、命中率、加载延迟和吞吐

<a id="paper-148283"></a>

## CELEUS: Certifiable and Efficient LLM Evaluation via E-Processes

[官方论文页](https://neurips.cc/virtual/2026/poster/148283) · [作者来源](https://openreview.net/forum?id=z1gbJ1JWes)

- **问题 / 瓶颈** · 反复检查普通置信区间会使覆盖声明失效
- **核心创新 / 方法** · 用 e-process 配合不确定性采样及代理评分，构造条件无偏信号
- **Baseline** · 现有序贯评测基线；具名对照待核
- **Benchmark** · 达到固定精度的样本量及停止时覆盖率
- **关键结果 / 消融** · 作者报告少评 54–62% 样本并保持任意时点覆盖
- **适用条件 / 局限** · 需要采样和校正满足条件无偏

**可复用机制** · 预算敏感评测用有效序贯区间，同时记录停止规则和覆盖

<a id="paper-151414"></a>

## CellMSA: Context Modeling for Single-Cell Representation Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151414) · [作者来源](https://openreview.net/forum?id=aqtv1iusCF)

- **问题 / 瓶颈** · 独立编码会遗漏跨批次共享结构
- **核心创新 / 方法** · 跨批检索相关观测，将一致性与变化编码成成对上下文
- **Baseline** · 独立编码与同批上下文方法，具名待核
- **Benchmark** · 单细胞观测数据的表示评测
- **关键结果 / 消融** · 摘要报告多个评测改善，独立归因待核
- **适用条件 / 局限** · 依赖近邻检索与批次匹配质量

**可复用机制** · 跨环境表示训练时以固定参数预算比较同批与跨批上下文

<a id="paper-138931"></a>

## CellularS2-Bench: A Staged, Evidence-Grounded Benchmark for Cellular Network Security Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/138931) · [作者来源](https://openreview.net/forum?id=vniyGN0gce)

- **问题 / 瓶颈** · 标准文档的多条款依据易被单一问答分数掩盖
- **核心创新 / 方法** · 构造由专家核验的分阶段规范理解任务，要求依据可追踪
- **Baseline** · 对照既有问答数据及检索整合基线
- **Benchmark** · CellularS2-Bench；规范文字、表格及图示
- **关键结果 / 消融** · 报告评测规模，模型数值需全文核实
- **适用条件 / 局限** · 结果受规范版本和证据标注影响

**可复用机制** · 规范文档评测分别检查单条理解、多证据链接与结论依据

<a id="paper-150459"></a>

## CENDRe: Concept Extraction with Natural Domain Representations

[官方论文页](https://neurips.cc/virtual/2026/poster/150459) · [作者来源](https://openreview.net/forum?id=ht3dAp9x7G)

- **问题 / 瓶颈** · 仅时域归因会遗漏周期信号
- **核心创新 / 方法** · 从逐步潜变量自动聚类概念，沿可微域变换传播概念梯度
- **Baseline** · 已有时间序列概念提取方法
- **Benchmark** · 合成概念基准及轴承故障数据
- **关键结果 / 消融** · 摘要报告合成重要性更准确，并定位真实故障相关频带
- **适用条件 / 局限** · 对可逆域变换和潜概念质量有要求

**可复用机制** · 用同一概念打分比较时域与频域证据，并单独核验重要性

<a id="paper-139585"></a>

## CEO-Bench: Can Agents Play the Long Game?

[官方论文页](https://neurips.cc/virtual/2026/poster/139585) · [作者来源](https://openreview.net/forum?id=GtZU4mP4EI)

- **问题 / 瓶颈** · 短任务成功率不足以反映持续资源管理
- **核心创新 / 方法** · 模拟 500 天经营，叠加预算约束、市场变化和多工具依赖
- **Baseline** · 多个前沿模型，摘要指出 GPT-5.5
- **Benchmark** · CEO-Bench，考察经营余额及持续策略
- **关键结果 / 消融** · 作者报告只有 GPT-5.5 超过初始 100 万余额
- **适用条件 / 局限** · 单一模拟器结果受环境经济机制影响

**可复用机制** · 用共享初态和冲击事件比较长期目标保持而非只算单步正确

<a id="paper-139123"></a>

## Cephalonauts One: A deep fMRI dataset for decoding naturalistic speech in the human brain

[官方论文页](https://neurips.cc/virtual/2026/poster/139123) · [作者来源](https://openreview.net/forum?id=jqqDfxmqO5)

- **问题 / 瓶颈** · 跨参与者平均可掩盖个体深度记录的价值
- **核心创新 / 方法** · 在留出扫描会话上用音频片段检索评估解码
- **Baseline** · 数据发布包含标准基线解码器，名称待核
- **Benchmark** · 三名参与者分别 14、20、17 小时 fMRI，留出会话检索
- **关键结果 / 消融** · 摘要报告随个人训练数据增加持续改善
- **适用条件 / 局限** · 只有三人，跨人外推不足

**可复用机制** · 同时报告个体学习曲线和留出会话性能，区分数据深度与人群覆盖

<a id="paper-153331"></a>

## Certifiably Optimal Robust Angular Synchronization

[官方论文页](https://neurips.cc/virtual/2026/poster/153331) · [作者来源](https://openreview.net/forum?id=M7UwJ21cjC)

- **问题 / 瓶颈** · 逐边上界过松使全局验证昂贵
- **核心创新 / 方法** · 离散角度后做分支定界，结合标签剪枝和节点约束松弛
- **Baseline** · 标准逐边界及其他鲁棒估计方法
- **Benchmark** · 合成图、IMC、KITTI、NSS 等；角度误差和运行时间
- **关键结果 / 消融** · 测试均取得最优性证明，高异常比例仍亚度精度
- **适用条件 / 局限** · 最优性对应离散问题及最大一致性目标

**可复用机制** · 同一几何模型上对照逐边松弛和共享节点松弛的搜索规模

<a id="paper-150658"></a>

## Certification-Enhanced Generalization Bounds

[官方论文页](https://neurips.cc/virtual/2026/poster/150658) · [作者来源](https://openreview.net/forum?id=gPQCdRDGp8)

- **问题 / 瓶颈** · 纯解析证明依赖严格假设，样本稳定性本身不足以说明总体
- **核心创新 / 方法** · 验证训练过程的稳定性规范，再用集中不等式连接分布分析
- **Baseline** · 既有解析稳定性界及计算型泛化界
- **Benchmark** · 从玩具数据到语言模型微调，比对可证界宽度
- **关键结果 / 消融** · 作者报告比替代计算方法紧多个数量级
- **适用条件 / 局限** · 依赖可验证稳定性和验证成本

**可复用机制** · 选择泛化证书前分别检查样本级稳定性与总体概率界

<a id="paper-150529"></a>

## Certification from Examples is Hard for Circuits and Transformers under Minimal Overparametrization

[官方论文页](https://neurips.cc/virtual/2026/poster/150529) · [作者来源](https://openreview.net/forum?id=hRqL7vRChh)

- **问题 / 瓶颈** · 少量测试会遗漏罕见结构性错误
- **核心创新 / 方法** · 分析电路和 Transformer 的例证证书规模及近似认证门槛
- **Baseline** · 最小模型与轻微过参数模型的理论对照
- **Benchmark** · 阈值电路、对数精度 Transformer 与二进制加法
- **关键结果 / 消融** · 增加单门或常数规模结构可造成指数级认证困难
- **适用条件 / 局限** · 结论对应特定函数族、精度及证书定义

**可复用机制** · 在高准确率任务上额外检测边界错误并明确保证是平均还是精确

<a id="paper-151824"></a>

## Certified but Private: Scalable Zero-Knowledge Proofs for the Formal Verification of Neural Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/151824) · [作者来源](https://openreview.net/forum?id=XhTzs21IA3)

- **问题 / 瓶颈** · 审计要求可验证性质，但模型参数不能公开
- **核心创新 / 方法** · 将 CROWN 的非线性层线性松弛转为轻量证明
- **Baseline** · 先前零知识鲁棒性系统
- **Benchmark** · 超过 290 万参数模型的局部鲁棒证明时延
- **关键结果 / 消融** · 作者报告生成约 4 分钟，验证低于 7.5 秒
- **适用条件 / 局限** · 性质依赖前置松弛、扰动域与证明实现

**可复用机制** · 比较零知识证书的生证、验真开销和可覆盖扰动范围

<a id="paper-148390"></a>

## Certified Policy Optimisation for Nested Causal Bandits via PAC-Bayes Risk

[官方论文页](https://neurips.cc/virtual/2026/poster/148390) · [作者来源](https://openreview.net/forum?id=yCGQfWxC94)

- **问题 / 瓶颈** · 战略动作改变战术上下文，联合拟合容易失去机制可迁移性。
- **核心创新 / 方法** · 因果机制分解后每回合采样一次并递归决策，用历史数据给出离策略风险界。
- **Baseline** · 同函数类 RFF-GP 联合回归与联合决策。
- **Benchmark** · 层级结构因果模型、外生分布变化与证书随数据量变化。
- **关键结果 / 消融** · 报告零样本迁移更好且证书随数据增加收紧。
- **适用条件 / 局限** · 依赖层级因果结构和历史数据覆盖。

**可复用机制** · 先比较因果分解和联合拟合，再用风险上界决定各层何时切换。

<a id="paper-148991"></a>

## Certified Robust Interpretability via Concept-Space Stability under Interventional Proxies

[官方论文页](https://neurips.cc/virtual/2026/poster/148991) · [作者来源](https://openreview.net/forum?id=tbVIr983oG)

- **问题 / 瓶颈** · 像素空间预测稳定仍可能伴随概念漂移。
- **核心创新 / 方法** · 以 Lipschitz 界和间隔联合构造概念空间半径，并用干预代理学习。
- **Baseline** · 只看预测标签的认证。
- **Benchmark** · 概念瓶颈分类、合成真值与自然图像干预代理。
- **关键结果 / 消融** · 半径界对所考察结构紧至常数二倍；因果概念认证要求忠实性。
- **适用条件 / 局限** · 代理与真实干预存在误差。

**可复用机制** · 给解释审计单列概念漂移指标与证书。

<a id="paper-152235"></a>

## Certified Single-Level Reformulation for Tri-Level Cyber-Physical Grid Security

[官方论文页](https://neurips.cc/virtual/2026/poster/152235) · [作者来源](https://openreview.net/forum?id=UZCoLnaUiy)

- **问题 / 瓶颈** · 多层稳健优化难直接求解。
- **核心创新 / 方法** · 把多层防御评估转为单层约束优化，并认证最坏损失上界。
- **Baseline** · 原多层优化。
- **Benchmark** · 电网防御的 DC 和 AC 潮流模型。
- **关键结果 / 消融** · 获得保守风险证书。
- **适用条件 / 局限** · 松弛会影响上界紧度。

**可复用机制** · 部署稳健决策时用可计算上界并检查保守程度。

<a id="paper-139843"></a>

## CFC26: Building Evaluations for Deployment in Sonar-Based Fish Counting

[官方论文页](https://neurips.cc/virtual/2026/poster/139843) · [作者来源](https://openreview.net/forum?id=15IDKXrEp8)

- **问题 / 瓶颈** · 逐帧检测掩盖整段计数偏差。
- **核心创新 / 方法** · 扩充多流域声呐数据并引入两种作业流程对应的计数指标。
- **Baseline** · CFC22 与逐帧检测指标。
- **Benchmark** · 11 个地点、9 个河系，使用 nMNE 和 nMANE。
- **关键结果 / 消融** · 报告新指标揭示方向性偏差。
- **适用条件 / 局限** · 其他鱼种与传感条件需复核。

**可复用机制** · 以整段作业误差和新地点评估替代仅同域逐帧打分。

<a id="paper-152332"></a>

## C-GRPO: Conformal Group Relative Policy Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/152332) · [作者来源](https://openreview.net/forum?id=TrdqzzvFCs)

- **问题 / 瓶颈** · 固定组大小浪费简单题预算。
- **核心创新 / 方法** · 用任务非一致性分数校准停止并周期性重校准。
- **Baseline** · 固定预算 GRPO 和自适应基线。
- **Benchmark** · 数学、科学及代码六个基准，测 rollout 和 pass@1。
- **关键结果 / 消融** · 平均 rollout 较固定 GRPO 少 49–70%。
- **适用条件 / 局限** · 预算单调结论依赖策略单调改进。

**可复用机制** · 在同训练预算下并列报告停止覆盖和任务准确率。

<a id="paper-154069"></a>

## CHAIN: Complementary Signed Graph Propagation for Uncertainty Quantification in Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154069) · [作者来源](https://openreview.net/forum?id=GPcmXSBoHa)

- **问题 / 瓶颈** · 局部相似度可能忽略高阶语义关系。
- **核心创新 / 方法** · 建立有符号回应图，经随机传播聚合图级分数。
- **Baseline** · 成对相似度与聚类路线。
- **Benchmark** · 五个数据集，具名指标待核。
- **关键结果 / 消融** · 作者报告优于对照，幅度待核。
- **适用条件 / 局限** · 关系判定误差可能传播放大。

**可复用机制** · 固定采样预算消融支持边、矛盾边与高阶传播。

<a id="paper-155574"></a>

## CHAIN: Continual Heterogeneous Cooperation with Information Bottleneck for Multi-Agent Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/155574) · [作者来源](https://openreview.net/forum?id=4avjOdnj6s)

- **问题 / 瓶颈** · 环境变化时冗余表示和同质策略降低协作表现。
- **核心创新 / 方法** · 把异质策略瓶颈拆为拟合、压缩与异质化三部分。
- **Baseline** · 异质多智能体强化学习方法。
- **Benchmark** · 标准及滑移 MA-Mujoco、MEAL。
- **关键结果 / 消融** · 作者报告持续任务表现改善，幅度待核。
- **适用条件 / 局限** · 异质化可能伤害本就适合共享的任务。

**可复用机制** · 在非平稳协作任务分别消融压缩和专长目标。

<a id="paper-149929"></a>

## ChainFlow-VLA: Causal Flow Planning with Vision-Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149929) · [作者来源](https://openreview.net/forum?id=m7AO7a7zPZ)

- **问题 / 瓶颈** · 逐步生成积累误差，整体生成较难约束因果结构。
- **核心创新 / 方法** · 用自回归模型提出离散轨迹模式，以 VLM 条件流细化全局轨迹。
- **Baseline** · 自回归和整体生成路线。
- **Benchmark** · 驾驶轨迹规划，具名设置待核。
- **关键结果 / 消融** · 报告时序与整体一致性的改善，幅度待核。
- **适用条件 / 局限** · 候选模式漏检时残差修改范围有限。

**可复用机制** · 固定候选预算比较直接生成与模式内细化。

<a id="paper-151502"></a>

## Chaining 2-FWL GNNs for Combinatorial Graph Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/151502) · [作者来源](https://openreview.net/forum?id=aAfBJ8E8TU)

- **问题 / 瓶颈** · 纯结构对齐中消息传递表征可能退化。
- **核心创新 / 方法** · 串联 2-FWL 网络，每阶段解码并按匹配质量重排节点。
- **Baseline** · 经典 FAQ 与常量特征消息传递网络。
- **Benchmark** · 随机图、规则图及三个真实图基准。
- **关键结果 / 消融** · 稀疏随机图一项设置准确率 85% 对 13%，真实数据增益较小。
- **适用条件 / 局限** · 部分实验需数据集专用训练及 FAQ 后处理。

**可复用机制** · 区分离散反馈、初始化与后处理各自的增益。

<a id="paper-154354"></a>

## Chain-of-Correction: Progress-Aware Policy Steering via Anchor-Grounded Predictive Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/154354) · [作者来源](https://openreview.net/forum?id=EDXA8qb52B)

- **问题 / 瓶颈** · 局部合理修正可能无助于完成任务。
- **核心创新 / 方法** · 用锚定场景图表示关系，并进行历史验证和未来进度检查。
- **Baseline** · 像素或潜空间的推理时策略修正。
- **Benchmark** · COLOSSEUM、离线预测协议及真机。
- **关键结果 / 消融** · 作者报告改善，详细幅度待核。
- **适用条件 / 局限** · 依赖可恢复的三维关系与任务进度表征。

**可复用机制** · 给动作纠错器加整体进度验收，并单测局部修复成功率。

<a id="paper-149520"></a>

## Chain of Dual Structures in Transformer Attention

[官方论文页](https://neurips.cc/virtual/2026/poster/149520) · [作者来源](https://openreview.net/forum?id=pXT6GQVuw4)

- **问题 / 瓶颈** · 注意力三个阶段的结构约束通常分开讨论。
- **核心创新 / 方法** · 用凸势及 Legendre 对偶刻画打分、梯度归一化和对偶重心聚合。
- **Baseline** · 标准内积注意力。
- **Benchmark** · 按结构公理刻画可行计算形式。
- **关键结果 / 消融** · 得到归一化与聚合的必要形式。
- **适用条件 / 局限** · 必要性依赖给定公理。

**可复用机制** · 改变注意力算子时检查三阶段是否来自相容的势。

<a id="paper-154597"></a>

## Chain-of-Route: State-Aware LLM Routing for Multi-Turn Conversations

[官方论文页](https://neurips.cc/virtual/2026/poster/154597) · [作者来源](https://openreview.net/forum?id=CPCK7uqzh3)

- **问题 / 瓶颈** · 逐轮独立选择忽略历史和缓存复用。
- **核心创新 / 方法** · 递归传递对话状态，并单独跟踪每个模型的服务状态。
- **Baseline** · 逐请求路由。
- **Benchmark** · 多轮会话质量与服务成本，详细数据待核。
- **关键结果 / 消融** · 作者报告状态感知改善成本质量折衷，幅度待核。
- **适用条件 / 局限** · 缓存策略与模型池变化会影响成本估计。

**可复用机制** · 路由基准应固定对话并报告实际增量推理开销。

<a id="paper-140099"></a>

## Chain-of-Thought Oversight Should Not Treat Faithfulness as Monitorability

[官方论文页](https://neurips.cc/virtual/2026/poster/140099) · [作者来源](https://openreview.net/forum?id=DLek3EUyds)

- **问题 / 瓶颈** · 其中一项达标无法推出其他项达标。
- **核心创新 / 方法** · 用方向相反的案例对照内部证据与外部监测。
- **Baseline** · 仅用显式推理或内部探针作为验收的做法。
- **Benchmark** · 开放权重推理模型上的两种案例。
- **关键结果 / 消融** · 报告忠实性与外部可监测性可发生分离。
- **适用条件 / 局限** · 案例有限；监测结论依赖所选监测器。

**可复用机制** · 监督模型时为每种解释性质单设留出任务。

<a id="paper-150110"></a>

## ChainSpace: A Chained-Reasoning Paradigm for Spatial Intelligence

[官方论文页](https://neurips.cc/virtual/2026/poster/150110) · [作者来源](https://openreview.net/forum?id=kcBg1aX6Gx)

- **问题 / 瓶颈** · 独立问答可能绕开持续空间表征。
- **核心创新 / 方法** · 构造逻辑相关的多轮题链及链级指标，并模拟合成链式监督。
- **Baseline** · 孤立问答与开源多模态模型。
- **Benchmark** · ChainSpace-Bench 与外部空间基准。
- **关键结果 / 消融** · 链级指标揭示单题准确率掩盖的错误。
- **适用条件 / 局限** · 结果受问题链覆盖与模拟真实性影响。

**可复用机制** · 同时报告单轮正确率和跨轮一致性。

<a id="paper-150205"></a>

## Chance-constrained Flow Matching for High-Fidelity Constraint-aware Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/150205) · [作者来源](https://openreview.net/forum?id=jwaNz2c281)

- **问题 / 瓶颈** · 对带噪中间态使用干净样本可行域可能扭曲生成分布。
- **核心创新 / 方法** · 在采样过程中用机会约束处理可行性。
- **Baseline** · 逐步投影及先估计干净状态再投影。
- **Benchmark** · 物理场和偏微分方程约束生成。
- **关键结果 / 消融** · 作者报告保真与可行性改善，幅度待核。
- **适用条件 / 局限** · 保证依赖约束分布与优化前提。

**可复用机制** · 在模拟物理场上按同预算比较约束违例和分布误差。

<a id="paper-149306"></a>

## Change-Robust Online Topological Memory for Long-Term Relocalization and Semantic Navigation

[官方论文页](https://neurips.cc/virtual/2026/poster/149306) · [作者来源](https://openreview.net/forum?id=rADSBLErqY)

- **问题 / 瓶颈** · 环境变化下外观检索误配会污染地图。
- **核心创新 / 方法** · 将 RGB-D 候选变成位姿模式，用有界混合滤波和里程计筛选长期一致分支。
- **Baseline** · 检索后立即关联与事后拒绝思路。
- **Benchmark** · 长期重定位和真机四足物体导航。
- **关键结果 / 消融** · 作者报告多种场景变化下稀疏地图复用改善。
- **适用条件 / 局限** · 依赖深度、相对位姿与里程计质量。

**可复用机制** · 比较关联前几何确认与事后地图修正。

<a id="paper-151923"></a>

## Channel Mixer: A Pretrainable Tokenizer for Scalable Multi-Channel Vision Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/151923) · [作者来源](https://openreview.net/forum?id=Wrq9Wj3xln)

- **问题 / 瓶颈** · 逐通道展开会快速增加注意力开销。
- **核心创新 / 方法** · 用轻量自编码器预训通道无关 tokenizer，每空间块输出一个融合 token。
- **Baseline** · 逐通道展开的 ViT。
- **Benchmark** · 3–29 通道图像、ViT-S/16。
- **关键结果 / 消融** · 29 通道情形约少 20 倍 FLOPs 和 29 倍 token，精度可比或更好。
- **适用条件 / 局限** · 空间块内融合可能丢失独立通道细节。

**可复用机制** · 固定空间分辨率对照通道展开和局部融合。

<a id="paper-152137"></a>

## Channel-wise Vector Quantization

[官方论文页](https://neurips.cc/virtual/2026/poster/152137) · [作者来源](https://openreview.net/forum?id=VFeBuEITNa)

- **问题 / 瓶颈** · 空间块索引难直接组织由粗到细的信息
- **核心创新 / 方法** · 量化特征图的各通道并逐通道自回归
- **Baseline** · 普通 VQ 与自回归生成
- **Benchmark** · 重建 FID、GenEval、DPG
- **关键结果 / 消融** · 重建 FID 减半，GenEval 从 0.69 到 0.74
- **适用条件 / 局限** · 依赖编码器通道分工

**可复用机制** · 对照按块和按通道预测的码本利用与生成质量

<a id="paper-149597"></a>

## ChanSFormer: A Channel Agnostic Vision Transformer for Multi-Channel Cell Painting Images

[官方论文页](https://neurips.cc/virtual/2026/poster/149597) · [作者来源](https://openreview.net/forum?id=ov9pIIpqw4)

- **问题 / 瓶颈** · 固定通道嵌入限制未见通道
- **核心创新 / 方法** · 分离空间与通道注意力，为每通道配置 CLS
- **Baseline** · 通道自适应视觉 Transformer
- **Benchmark** · CHAMMI、JUMP-CP、So2Sat
- **关键结果 / 消融** · 报告可适应不同通道配置，分项数字待核
- **适用条件 / 局限** · 通道内容变化仍可能引入分布偏移

**可复用机制** · 按未见通道组合测试通道共享架构

<a id="paper-148219"></a>

## Characterizing Learning in Deep Neural Networks using a Tractable Algorithmic Complexity Estimator

[官方论文页](https://neurips.cc/virtual/2026/poster/148219) · [作者来源](https://openreview.net/forum?id=zT1uGkhHsM)

- **问题 / 瓶颈** · 二值化丢掉量化权重信息
- **核心创新 / 方法** · 将块分解扩展到多符号对象
- **Baseline** · 二值块分解
- **Benchmark** · 训练权重轨迹、泛化和压缩
- **关键结果 / 消融** · 报告训练中复杂度下降并与泛化相关
- **适用条件 / 局限** · 是复杂度估计而非精确值

**可复用机制** · 比较不同码宽下复杂度指标与压缩误差

<a id="paper-154072"></a>

## Characterizing Memorization in Diffusion Language Models: Generalized Extraction and Sampling Effects

[官方论文页](https://neurips.cc/virtual/2026/poster/154072) · [作者来源](https://openreview.net/forum?id=GOsBvzS6iy)

- **问题 / 瓶颈** · 只沿用自回归审计口径会遗漏生成机制差异
- **核心创新 / 方法** · 在统一的条件评估下比较训练文本复现风险
- **Baseline** · 自回归语言模型
- **Benchmark** · 不同规模和生成设定的隐私评估
- **关键结果 / 消融** · 作者报告对齐评测下扩散模型的个人信息泄漏较低
- **适用条件 / 局限** · 结论局限于所测模型及审计设定

**可复用机制** · 固定隐私评估预算比较不同生成模型的泄漏指标

<a id="paper-139666"></a>

## Characterizing the Aesthetic Defaults of Generative Image Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139666) · [作者来源](https://openreview.net/forum?id=C0BaTNbw0c)

- **问题 / 瓶颈** · 总体偏好分数不能说明风格来自何处
- **核心创新 / 方法** · 在图像嵌入上学习风格稀疏词汇，再用中性提示估计概念分布
- **Baseline** · 模型版本和真实图像分布
- **Benchmark** · 跨四年的 26 个生成器
- **关键结果 / 消融** · 报告跨模型风格范围收缩并偏向生活与编辑摄影
- **适用条件 / 局限** · 概念取决于嵌入和词汇训练

**可复用机制** · 用配对内容与可解释风格统计诊断版本漂移

<a id="paper-153245"></a>

## Characterizing the Edge of Stability in Variational Training Without Priors

[官方论文页](https://neurips.cc/virtual/2026/poster/153245) · [作者来源](https://openreview.net/forum?id=Mfhyva9QO7)

- **问题 / 瓶颈** · 无显式先验目标的隐式正则规律不明
- **核心创新 / 方法** · 用梯度估计信噪比和样本数描述稳定边界
- **Baseline** · 不同学习率与参数采样数
- **Benchmark** · 分布外任务和理论稳定边界
- **关键结果 / 消融** · 较大学习率与较少样本对应更平坦极小值
- **适用条件 / 局限** · 相关趋势受优化设定约束

**可复用机制** · 把采样方差与学习率作为联合消融变量

<a id="paper-153550"></a>

## Characterizing the Generalization Error of Random Feature Regression with Arbitrary Data-Augmentation

[官方论文页](https://neurips.cc/virtual/2026/poster/153550) · [作者来源](https://openreview.net/forum?id=KXzh31eKa0)

- **问题 / 瓶颈** · 增强的正则作用难量化
- **核心创新 / 方法** · 在样本和维度同比增长时推导随机特征读出误差
- **Baseline** · 不同增强统计和高斯设定
- **Benchmark** · 随机特征回归测试 MSE
- **关键结果 / 消融** · 高斯数据下刻画渐近紧致
- **适用条件 / 局限** · 只训练读出层的设定

**可复用机制** · 对冻结骨干优先检查增强二阶统计是否改变回归风险

<a id="paper-154648"></a>

## Characterizing Trainability of Instantaneous Quantum Polynomial Circuit Born Machine

[官方论文页](https://neurips.cc/virtual/2026/poster/154648) · [作者来源](https://openreview.net/forum?id=C2rWYFc9J6)

- **问题 / 瓶颈** · 量子生成模型梯度可能指数衰减
- **核心创新 / 方法** · 解析 MMD 梯度方差并给出上下界
- **Baseline** · 不同生成元拓扑和核权重
- **Benchmark** · 瞬时量子多项式线路 Born 模型
- **关键结果 / 消融** · 结构化拓扑中低权核可避免指数抑制
- **适用条件 / 局限** · 可训练性不直接证明量子优势

**可复用机制** · 选核时检查梯度方差随线路规模的变化

<a id="paper-153000"></a>

## Characterizing Underrepresentation in Generalizing Causal Survival Estimates

[官方论文页](https://neurips.cc/virtual/2026/poster/153000) · [作者来源](https://openreview.net/forum?id=OiKgzKcvqA)

- **问题 / 瓶颈** · 两种缺乏代表性会被混在一起
- **核心创新 / 方法** · 分解有效估计量渐近方差中的采样权重和删失权重
- **Baseline** · 只检查基线重叠的诊断
- **Benchmark** · 试验到目标人群的生存效应外推
- **关键结果 / 消融** · 理论标识哪些项在代表性减弱时发散
- **适用条件 / 局限** · 受删失和外推识别假设限制

**可复用机制** · 按子组和随访时点分开报告代表性缺口

<a id="paper-156019"></a>

## Characterizing Universal Object Representations Across Vision Models

[官方论文页](https://neurips.cc/virtual/2026/poster/156019) · [作者来源](https://openreview.net/forum?id=16SGONh3Vl)

- **问题 / 瓶颈** · 整体表示相似不解释共同编码了什么
- **核心创新 / 方法** · 分解物体相似性并统计非负概念维度出现频率
- **Baseline** · 通用与模型特异维度
- **Benchmark** · 162 个模型及人类相似判断和猕猴视觉活动
- **关键结果 / 消融** · 通用维度更可解释，与生物视觉相关
- **适用条件 / 局限** · 关联并非因果

**可复用机制** · 跨骨干比较时单独跟踪复现的语义维度

<a id="paper-148244"></a>

## Character Mixing for Video Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/148244) · [作者来源](https://openreview.net/forum?id=zKLIZIhkEs)

- **问题 / 瓶颈** · 外观匹配不能保证行为一致
- **核心创新 / 方法** · 分离角色身份与行为嵌入，并用保留外观的跨风格增强
- **Baseline** · 通用与个性化视频生成模型
- **Benchmark** · 跨角色组合基准
- **关键结果 / 消融** · 报告身份、交互和风格一致性改善
- **适用条件 / 局限** · 依赖角色注释及增强质量

**可复用机制** · 将熟悉实体和陌生搭档组合用于条件生成评测

<a id="paper-154071"></a>

## CHARM+: Cross-Hardware Attention with Re-Merge Multistream Mechanism

[官方论文页](https://neurips.cc/virtual/2026/poster/154071) · [作者来源](https://openreview.net/forum?id=GP3kYFlyJj)

- **问题 / 瓶颈** · 跨节点同步会受慢链路拖累
- **核心创新 / 方法** · 将注意力通信分层并用多流重叠计算，解耦跨硬件和内部通信
- **Baseline** · Ring-Attention
- **Benchmark** · 双 NUMA PCIe 与双节点 NVLink
- **关键结果 / 消融** · 双节点前向与反向平均快 2.8 和 3.9 倍
- **适用条件 / 局限** · 收益依赖拓扑及互联带宽

**可复用机制** · 对异构集群报告通信同步和计算覆盖率

<a id="paper-148773"></a>

## ChartArena: A Unified Benchmark with Atomic-Primitive Reasoning for Chart Parsing

[官方论文页](https://neurips.cc/virtual/2026/poster/148773) · [作者来源](https://openreview.net/forum?id=vAPXuhpYYw)

- **问题 / 瓶颈** · CSV 与 JSON 等输出难直接公平比较
- **核心创新 / 方法** · 将输出映射为规范三元组和有向图
- **Baseline** · 图表解析输出对照
- **Benchmark** · 双语八类图表及图示
- **关键结果 / 消融** · 摘要给出统一可比评测，量化细节待核
- **适用条件 / 局限** · 规范化可能忽略视觉属性

**可复用机制** · 先规范化语义结构，再比较不同序列化模型的解析能力

<a id="paper-150479"></a>

## Chasing Label Shifters: A Change-Aware Framework for Dynamic Graph Node Classification

[官方论文页](https://neurips.cc/virtual/2026/poster/150479) · [作者来源](https://openreview.net/forum?id=hkeWDm9UGm)

- **问题 / 瓶颈** · 稳定节点掩盖动态模型旧标签偏向
- **核心创新 / 方法** · 识别发生变化的节点并覆盖滞后邻居信号
- **Baseline** · 多种动态 GNN
- **Benchmark** · 变化节点与稳定节点分组
- **关键结果 / 消融** · 错误集中在旧标签，且旧类邻居更强时更严重
- **适用条件 / 局限** · 须识别状态转移，误触发可能影响稳定节点

**可复用机制** · 训练动态图时跟踪变化节点到旧类中心距离

<a id="paper-148306"></a>

## CHASM: Cross-frequency Harmonized Axis-Separable Mixing for Spectral Token Operators

[官方论文页](https://neurips.cc/virtual/2026/poster/148306) · [作者来源](https://openreview.net/forum?id=yp8Uvn0O2A)

- **问题 / 瓶颈** · 独立频率混合缺少同一通道方向
- **核心创新 / 方法** · 共享学习基底并用频率专属正增益，沿高宽分别混合
- **Baseline** · 同骨干谱混合模块
- **Benchmark** · MRI 重建分割与自然图像重建
- **关键结果 / 消融** · 报告同骨干改善
- **适用条件 / 局限** · 共享基底可能约束跨频异质信号

**可复用机制** · 固定骨干比较共享基底和独立算子

<a id="paper-148469"></a>

## Cheap Per-Component Testing for PLS, Stable Under Rotation

[官方论文页](https://neurips.cc/virtual/2026/poster/148469) · [作者来源](https://openreview.net/forum?id=xb6CB7d9LO)

- **问题 / 瓶颈** · PLS 的传统推断可能昂贵或有偏
- **核心创新 / 方法** · 用纠正后的渐近 t 检验，近奇异时用置换参照
- **Baseline** · 交叉验证置换及已有 PLS 检验
- **Benchmark** · 合成、Tecator 与跨语言词向量
- **关键结果 / 消融** · 证明正交重基不改变留出预测及检验统计量
- **适用条件 / 局限** · 对其他监督子空间的迁移尚未直接实测

**可复用机制** · 先保持子空间固定，再验证可解释旋转是否改变推断

<a id="paper-148921"></a>

## Cheap Talk, Real Stakes: Commitment and Exploitation in Human-LLM Strategic Interaction

[官方论文页](https://neurips.cc/virtual/2026/poster/148921) · [作者来源](https://openreview.net/forum?id=uDEUKmAbkA)

- **问题 / 瓶颈** · 只评最终行动会漏掉说做差距
- **核心创新 / 方法** · 随机化自由对话和身份遮蔽，记录承诺与实际行动
- **Baseline** · 人类、人机及模型配对
- **Benchmark** · 五种重复博弈共 3752 场
- **关键结果 / 消融** · 交流改善部分协调，但承诺不等同于一致执行
- **适用条件 / 局限** · 限制于受控博弈

**可复用机制** · 给代表用户协商的系统单独测承诺履行

<a id="paper-150678"></a>

## Chebyshev Differential Flows for Shape Matching and Interpolation with Endpoint Guidance

[官方论文页](https://neurips.cc/virtual/2026/poster/150678) · [作者来源](https://openreview.net/forum?id=gIxG2mgvoJ)

- **问题 / 瓶颈** · 逐顶点插值正则可能抑制必要的伸展剪切
- **核心创新 / 方法** · 以切比雪夫时间模式拆分端点可见和内部变形，泊松积分恢复形状
- **Baseline** · 逐顶点位移插值
- **Benchmark** · 三维形状匹配与插值
- **关键结果 / 消融** · 提出可在任意时间求值的紧凑路径，定量待核
- **适用条件 / 局限** · 端点无法唯一约束真实中间路径

**可复用机制** · 显式分开端点约束和中段自由度

<a id="paper-139263"></a>

## Chess-World-Model: A 10M-Game Benchmark for Exact State Tracking from Chess Move Sequences

[官方论文页](https://neurips.cc/virtual/2026/poster/139263) · [作者来源](https://openreview.net/forum?id=b8i6faPmkw)

- **问题 / 瓶颈** · 真实棋局中的位置分布可能掩盖状态更新错误。
- **核心创新 / 方法** · 比较真实留出棋局和均匀随机合法对局，要求从行动序列精确还原棋盘。
- **Baseline** · 因果 Transformer、SLiCE、Mamba-3 和含负特征值的 Gated DeltaNet。
- **Benchmark** · 一千万真实棋局及随机合法外推集，测棋盘状态精确预测。
- **关键结果 / 消融** · 循环模型在 3M 和 8M 参数时领先；真实集在 18M 以上饱和，随机集至 38M 仍能区分模型。
- **适用条件 / 局限** · 证据限于棋类离散转移。

**可复用机制** · 评估状态追踪时分别保留自然轨迹和按规则随机采样的轨迹。

<a id="paper-150424"></a>

## ChildPose: Foundation for Children Pose Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/150424) · [作者来源](https://openreview.net/forum?id=i8KQIvVtSo)

- **问题 / 瓶颈** · 成人中心的姿态模型面对儿童体型、遮挡和运动模糊容易失效。
- **核心创新 / 方法** · 在预训练姿态编码器上加邻帧记忆与时序注意力，辅以年龄预测。
- **Baseline** · 现成二维姿态模型及儿童数据微调变体。
- **Benchmark** · 儿童视频的未见受试者划分，测姿态表现和时序稳定性。
- **关键结果 / 消融** · 作者报告优于现成和仅微调方法，幅度待核。
- **适用条件 / 局限** · 依赖儿童数据及年龄监督，群体覆盖待核。

**可复用机制** · 固定数据预算，分别验证邻帧信息与形态属性监督。

<a id="paper-150942"></a>

## ChiP-STAR: Spatial-Topological Attention for Pre-trained Generative Chip Routing

[官方论文页](https://neurips.cc/virtual/2026/poster/150942) · [作者来源](https://openreview.net/forum?id=eAB0qsCFKl)

- **问题 / 瓶颈** · DFS 序列邻接不对应芯片布线路径的空间邻接。
- **核心创新 / 方法** · 在 T5Gemma 加双参考系旋转编码、傅里叶分解注意力先验与累计坐标扰动。
- **Baseline** · iPCL-Large。
- **Benchmark** · AiEDA 几何标注布线数据及商业 ECO 验证；测 Leaf IoU、连通性、线长和通孔。
- **关键结果 / 消融** · 作者报告 Leaf IoU 与连通性提高 5%，线长少 3%、通孔少 11%。
- **适用条件 / 局限** · 组件独立贡献及跨设计迁移待核。

**可复用机制** · 对空间结构序列化时分别验证序列距离、空间距离和闭环误差累积。

<a id="paper-152373"></a>

## Choosing Before Acting: Comparative Value Estimation for Long-Horizon Tool-Use Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/152373) · [作者来源](https://openreview.net/forum?id=TYXZvbmRax)

- **问题 / 瓶颈** · 终局奖励难分配到单步，日志只记录实际调用。
- **核心创新 / 方法** · 结合记录行为、贝叶斯工具图模拟与语义比较训练成对价值模型。
- **Baseline** · 原工具调用方法与多个语言模型骨干，具体名称待核。
- **Benchmark** · 三项工具调用基准，测 Tool F1 和任务成功。
- **关键结果 / 消融** · 作者报告各骨干表现改善，幅度待核。
- **适用条件 / 局限** · 反事实标签受模拟器与评判模型偏差影响。

**可复用机制** · 对同一决策点构造配对候选，比较执行前重排与仅按即时分数调用。

<a id="paper-153059"></a>

## CHoRD: Coordinating Scheduling and Data Placement for Efficient Deep Neural Network Inference on Chiplet-Based GPUs

[官方论文页](https://neurips.cc/virtual/2026/poster/153059) · [作者来源](https://openreview.net/forum?id=OK9jVw9YBS)

- **问题 / 瓶颈** · 独立优化调度或驻留会使跨芯粒流量持续增加。
- **核心创新 / 方法** · 从程序重建依赖，可选用一次画像运行，以访问模式联合分配存储与执行。
- **Baseline** · 轮转 RR、仅放置的 CLAP。
- **Benchmark** · 九个 CNN 和 Transformer 推理负载，4 与 8 芯粒 MGPUSim。
- **关键结果 / 消融** · 4 芯粒上画像模式较 RR 和 CLAP 分别快 2.94 倍和 1.66 倍。
- **适用条件 / 局限** · 为模拟证据，真机画像开销待核。

**可复用机制** · 按依赖核函数复用同一数据的频率比较联合和分离优化。

<a id="paper-153626"></a>

## CHORD: Cross-Model Hallucination Detection via Relational Graph Discrimination

[官方论文页](https://neurips.cc/virtual/2026/poster/153626) · [作者来源](https://openreview.net/forum?id=Jz5BMGep1M)

- **问题 / 瓶颈** · 不同模型的隐状态语义不一致。
- **核心创新 / 方法** · 把层、词元和特征的关系组织为图，用关系注意力和元学习提取共享检测信号。
- **Baseline** · 代表性隐状态检测器，具名方法待核。
- **Benchmark** · 在源模型训练并在未见模型评测，具体指标待核。
- **关键结果 / 消融** · 作者报告跨模型检测优于对照，幅度待核。
- **适用条件 / 局限** · 需访问隐状态，异构架构间可比关系待核。

**可复用机制** · 评估可移植探针时按整个模型留出，对照原始坐标和内部关系。

<a id="paper-148240"></a>

## Christoffel-DPS: Optimal sensor placement in diffusion posterior sampling for arbitrary distributions

[官方论文页](https://neurips.cc/virtual/2026/poster/148240) · [作者来源](https://openreview.net/forum?id=zMIv8bU50c)

- **问题 / 瓶颈** · 高斯布点假设与生成式恢复处理的复杂分布不符。
- **核心创新 / 方法** · 用 Christoffel 函数提出无分布形式的布点准则，衔接扩散及流模型后验恢复。
- **Baseline** · 高斯布点及已有生成模型布点方法。
- **Benchmark** · 结构性非高斯基准与低传感器预算恢复。
- **关键结果 / 消融** · 作者给出非渐近传感器数量界，并报告恢复优于对照，数值待核。
- **适用条件 / 局限** · 依赖候选观测与信号先验质量。

**可复用机制** · 固定传感预算，比较先验自适应布点与高斯近似布点。

<a id="paper-139317"></a>

## ChronosAlign: A Large-Scale, Updatable Benchmark for Decomposing Temporal Alignment in LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/139317) · [作者来源](https://openreview.net/forum?id=Xq8uri8T9Z)

- **问题 / 瓶颈** · 静态问题难区分事实召回、时间锚定与拒答。
- **核心创新 / 方法** · 用可更新的 Wikidata 和 Wikipedia 记录生成带来源题目，并配对三种提示。
- **Baseline** · 比较十六个模型及三种提示。
- **Benchmark** · ChronosAlign 约 50 万问答对和 2.7 万独立问题，覆盖 2000 至 2025 年。
- **关键结果 / 消融** · 作者报告显式召回在 2022 年后下降，显式相对提示结果分离，拒答有混杂。
- **适用条件 / 局限** · 依赖来源、生成模板和知识库覆盖。

**可复用机制** · 将拒答率与时间锚定错误分开报告，并用同一题目增量复测。

<a id="paper-155153"></a>

## ChunkFT: Byte-Streamed Optimization for Memory-Efficient Full Fine-Tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/155153) · [作者来源](https://openreview.net/forum?id=7uCEIbODMO)

- **问题 / 瓶颈** · 全量微调峰值显存限制设备选择。
- **核心创新 / 方法** · 按子张量计算梯度，逐步调度参数工作集，给出确定性收敛分析。
- **Baseline** · 显存高效微调与全量微调。
- **Benchmark** · Llama 3 8B 与 70B；测显存、耗时、理解、数学和 MT-Bench。
- **关键结果 / 消融** · 作者报告 7B 模型在 1K 输入时约需 13.72GB，并称质量与全量对照可比。
- **适用条件 / 局限** · 随机场景收敛与传输瓶颈待核。

**可复用机制** · 比较稠密更新与分块更新时同时测吞吐、显存和下游表现。

<a id="paper-155855"></a>

## CI4A: Semantic Component Interfaces for Agents Empowering Web Automation

[官方论文页](https://neurips.cc/virtual/2026/poster/155855) · [作者来源](https://openreview.net/forum?id=2OjpGbcs3u)

- **问题 / 瓶颈** · 高层计划正确仍会因细粒度界面动作失败。
- **核心创新 / 方法** · 将组件交互封装为统一工具原语，并随状态更新可用动作。
- **Baseline** · 在改造版 WebArena 中比较现有方法，配置待核。
- **Benchmark** · Ant Design 的 23 类组件及改造版 WebArena，测成功率和效率。
- **关键结果 / 消融** · 作者报告成功率 86.3%。
- **适用条件 / 局限** · 依赖可修改应用及同等接口下的公平比较。

**可复用机制** · 在自有应用比较语义工具与视觉点击，记录错误发生在计划还是执行。

<a id="paper-149190"></a>

## CIG: Exploration via Conditional Information Gain

[官方论文页](https://neurips.cc/virtual/2026/poster/149190) · [作者来源](https://openreview.net/forum?id=sDCGZbVL6d)

- **问题 / 瓶颈** · 终生新颖性忽略回合内冗余，回合奖励又不保留终生进展。
- **核心创新 / 方法** · 用集成分歧核的对数行列式近似信息增益，以 Cholesky 分解得到逐步奖励。
- **Baseline** · 既有终生、回合与混合探索方法。
- **Benchmark** · MiniGrid、OGBench 共十二任务，含随机干扰条件。
- **关键结果 / 消融** · 作者报告达到或超过对照，且对随机干扰稳健，幅度待核。
- **适用条件 / 局限** · 验证集中于短模型滚动，集成成本待核。

**可复用机制** · 用同等预算比较双条件增益与经验加权混合奖励。

<a id="paper-139332"></a>

## CineMME: Benchmarking Fine-Grained Perception and Plot Reasoning in Multimodal Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139332) · [作者来源](https://openreview.net/forum?id=WXj17YlNuM)

- **问题 / 瓶颈** · 剧情问答正确可能没有连贯证据链。
- **核心创新 / 方法** · 设计相互关联的对白定位与剧情推理评测，并消融视觉。
- **Baseline** · 二十个推理模型、十个定位模型。
- **Benchmark** · 975 段电影视频，报告时间与空间 IoU、WER 和推理正确率。
- **关键结果 / 消融** · Gemini-3 Pro 对白时间 IoU 68.33%，说话人空间 IoU 13.24%，推理 65.88%。
- **适用条件 / 局限** · 领域限于所选电影片段及评价配置。

**可复用机制** · 报告证据各环节表现，避免仅以最终回答衡量视频理解。

<a id="paper-149533"></a>

## CineOrchestra: Unified Entity-Centric Conditioning for Cinematic Video Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/149533) · [作者来源](https://openreview.net/forum?id=pQRtpMb2e7)

- **问题 / 瓶颈** · 单轴控制难联动多个电影元素。
- **核心创新 / 方法** · 用按区间采样的时间 RoPE 和实体时间交叉注意力 RoPE 路由条件。
- **Baseline** · 六种单轴控制方法。
- **Benchmark** · 两项新基准，测密集描述遵循与切镜时间，另有人类配对评价。
- **关键结果 / 消融** · 作者报告优于基线并有组件消融，幅度待核。
- **适用条件 / 局限** · 重叠实体与较长视频下的控制边界待核。

**可复用机制** · 对异构控制因素使用共享时间接口，并按实体和时序分别检验偏差。

<a id="paper-155825"></a>

## CipherFlow: Hardware-Aware Compiler Framework for Low-Latency Hybrid Secure Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/155825) · [作者来源](https://openreview.net/forum?id=2b0g4FkPGD)

- **问题 / 瓶颈** · 固定同态加密与安全多方计算的混合计划难适配环境变化。
- **核心创新 / 方法** · 画像原语成本，并随密码计算状态优化算子位置、跨域转换和维护动作。
- **Baseline** · 静态混合安全推理基线。
- **Benchmark** · BERT-base 和 ViT，真实后端及多种 CPU、GPU 和网络条件。
- **关键结果 / 消融** · 作者报告相较静态混合对照最高分别加速 16.5 倍及超过 22 倍。
- **适用条件 / 局限** · 依赖后端与威胁模型；画像变化影响计划。

**可复用机制** · 在相同隐私假设下跨设备和网络复测计划，记录优化是否来自减少转换。

<a id="paper-139313"></a>

## CIPHERGRID Benchmark: From Multimodal Rule Inference to Sequential Action

[官方论文页](https://neurips.cc/virtual/2026/poster/139313) · [作者来源](https://openreview.net/forum?id=Xw2kQScdD6)

- **问题 / 瓶颈** · 单项能力达标不保证能在未知规则下正确行动。
- **核心创新 / 方法** · 用配对图像、编码描述和解例定义陌生符号约定，再要求解新棋盘。
- **Baseline** · 前沿模型、人类规则判断与精确路径求解器。
- **Benchmark** · CIPHERGRID 路径寻找与规则推断，测准确率。
- **关键结果 / 消融** · 前沿模型准确率 18.74% 至 41.89%。
- **适用条件 / 局限** · 合成网格无法直接代表真实任务。

**可复用机制** · 组合能力测试使用可单独校验的子问题，辨别失败发生在哪一环。

<a id="paper-153589"></a>

## Circuit-Level Knowledge Distillation for Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153589) · [作者来源](https://openreview.net/forum?id=KIMFWIfv3W)

- **问题 / 瓶颈** · 学生可复现输出但使用不同内部机制。
- **核心创新 / 方法** · 用 transcoder 归因图表示计算，以最优传输对齐师生路径。
- **Baseline** · 六种蒸馏目标及各自不加路径匹配的版本。
- **Benchmark** · 两个模型家族、三个指令基准和数学迁移。
- **关键结果 / 消融** · 作者报告压缩越激进时收益更显著，并给出计算差异界；幅度待核。
- **适用条件 / 局限** · 依赖归因图质量，路径匹配代价待核。

**可复用机制** · 对照只拟合输出与加入内部路径监督，并扫描压缩比验证差异。

<a id="paper-152316"></a>

## CircuitSeer: Mining High-Quality Data by Probing Mathematical Reasoning Circuits in LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/152316) · [作者来源](https://openreview.net/forum?id=TzFuvVae5b)

- **问题 / 瓶颈** · 外部评判成本高，文本启发式难表达模型自身学习需求。
- **核心创新 / 方法** · 识别复杂推理激活的注意力头，以样本影响为排序信号。
- **Baseline** · 训练全量数据及既有筛选方法。
- **Benchmark** · 四个模型、九个数据集，以 Pass@1 为主要指标。
- **关键结果 / 消融** · Qwen2.5-Math-7B 在入选 10% 数据上较全量平均高 1.2 点。
- **适用条件 / 局限** · 回路定位和迁移依赖底座与任务。

**可复用机制** · 固定数据量对照内部回路排序和外部质量打分，并检查因果性。

<a id="paper-150250"></a>

## CITE: Anytime Valid Statistical Inference in LLM Self-Consistency

[官方论文页](https://neurips.cc/virtual/2026/poster/150250) · [作者来源](https://openreview.net/forum?id=jdhnUghROp)

- **问题 / 瓶颈** · 未知答案集合及数据依赖停止使固定样本置信结论失效。
- **核心创新 / 方法** · 用交并检验与 E-process 证实预先指定答案是唯一众数，并扩展到置信加权。
- **Baseline** · 理论极小极大下界及模拟对照，具体基线待核。
- **Benchmark** · 模拟与 LLM 自一致性实验，测错误认证率和停止样本数。
- **关键结果 / 消融** · 作者证明任意停止下控制错误认证率，主区间的上界与下界同阶。
- **适用条件 / 局限** · 认证的是众数，不保证事实正确；目标答案预先指定。

**可复用机制** · 动态分配采样预算时把统计停止保证与答案真值校验分开。

<a id="paper-153952"></a>

## Cite What You Explore: Budget-Aware LLM Reasoning over Medical KGs with Verifiable Evidence

[官方论文页](https://neurips.cc/virtual/2026/poster/153952) · [作者来源](https://openreview.net/forum?id=HKqJQcqfEb)

- **问题 / 瓶颈** · 病历中的信息不足，外部图搜索易耗尽预算或引用弱证据。
- **核心创新 / 方法** · 按支持分数和出处构图，在计划、导航、验证循环中以检索增益、成本和引用联合训练。
- **Baseline** · 最强风险预测对照，名称待核。
- **Benchmark** · MIMIC-III 和 IV，八类疾病、三个时域，评 AUPRC、引用精度和预算。
- **关键结果 / 消融** · 作者报告 AUPRC 增 3.4 点，引用精度 59.8% 到 77.9%，使用预算上限的 62% 至 65%。
- **适用条件 / 局限** · 仅回顾性研究，结果不等于临床部署有效。

**可复用机制** · 固定检索预算比较有无出处和复核步骤，分开统计引用精度及下游质量。

<a id="paper-154638"></a>

## City-RAG: Stepping Into a City via Spatially-Grounded Video Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/154638) · [作者来源](https://openreview.net/forum?id=C7T2iGG1Zy)

- **问题 / 瓶颈** · 文本或图像一致性难保证生成环境对应真实地点。
- **核心创新 / 方法** · 以地理配准数据作上下文，用时间不对齐训练拆分静态空间与瞬态因素。
- **Baseline** · 文本到视频与图像到视频方法，具名对照待核。
- **Benchmark** · 分钟级地理视频、复杂路线和闭环；指标待核。
- **关键结果 / 消融** · 作者报告天气与光照可跨长序列保持，并展示闭环与地理重建。
- **适用条件 / 局限** · 依赖地理数据覆盖与配准，缺少摘要量化。

**可复用机制** · 分别校验真实位置几何一致性与天气、光照等可控变化。

<a id="paper-151477"></a>

## CitySTAR: Agent-Driven Structured and Topology-Aware Reasoning for Open-Vocabulary Urban 3D Grounding

[官方论文页](https://neurips.cc/virtual/2026/poster/151477) · [作者来源](https://openreview.net/forum?id=aKAYRvEMRa)

- **问题 / 瓶颈** · 直接相似度难以指定空间关系。
- **核心创新 / 方法** · 从点云构建开放词汇场景图，用双向超图验证并补充二维证据。
- **Baseline** · 直接匹配类方法，具名待核。
- **Benchmark** · CitySTAR-3D，城市级开放词汇定位。
- **关键结果 / 消融** · 作者报告定位改善，幅度待核。
- **适用条件 / 局限** · 依赖实例图与关系证据。

**可复用机制** · 对同类别候选，分别检查与上下文的关系约束，再融合图片证据。

<a id="paper-139660"></a>

## CivBench: A Long-Horizon Benchmark for Tool-Mediated Agents in Civilization VI

[官方论文页](https://neurips.cc/virtual/2026/poster/139660) · [作者来源](https://openreview.net/forum?id=CL2vWOhnZJ)

- **问题 / 瓶颈** · 终局分数无法指出长程执行失败的环节。
- **核心创新 / 方法** · 记录主动查询潜在状态的频率与承诺十轮内的执行率。
- **Baseline** · 四个模型家族，共用操作指引。
- **Benchmark** · CivBench，300 多轮游戏与 76 个 MCP 工具。
- **关键结果 / 消融** · 承诺落实率为 48%–66%，查询间隔约 30–75 轮。
- **适用条件 / 局限** · 23 次运行是先导样本。

**可复用机制** · 为有工具的长程助理分别统计监控频率与计划兑现率。

<a id="paper-139311"></a>

## CLAMP: A Sim-to-Real Benchmark for Closed-Loop Kinematic Pose Estimation and Assembly Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/139311) · [作者来源](https://openreview.net/forum?id=Y7MzZuaIWr)

- **问题 / 瓶颈** · 树形关节模型和全装配评测无法覆盖闭环或缺件。
- **核心创新 / 方法** · 以带闭环约束的图描述机构，用约束流形采样并随缺件重构图。
- **Baseline** · RoboPEPP、HoRoPose、CRAVES。
- **Benchmark** · CLAMP 七类设备，逾两百万合成训练图与约 2.1 万真实测试图。
- **关键结果 / 消融** · 约束采样改善多数闭环设备，三基线平均均受缺件影响。
- **适用条件 / 局限** · 需要 CAD 与机构描述。

**可复用机制** · 构造合成诊断时保持物理约束，并单独评估拓扑改变后的性能。

<a id="paper-148239"></a>

## Clapping: Removing Per-sample Storage for Pipeline Parallel Learning with Communication Compression

[官方论文页](https://neurips.cc/virtual/2026/poster/148239) · [作者来源](https://openreview.net/forum?id=zMLxSjEos8)

- **问题 / 瓶颈** · 压缩可能需要逐样本存储或依赖无偏假设。
- **核心创新 / 方法** · 跨步复用样本，两种变体允许有偏压缩梯度并给出收敛保证。
- **Baseline** · 既有流水线压缩，具名对照待核。
- **Benchmark** · 不同任务的数值实验，指标待核。
- **关键结果 / 消融** · 作者报告支持少轮或在线训练，实测幅度待核。
- **适用条件 / 局限** · 样本复用频率与通信收益边界待核。

**可复用机制** · 比较复用样本与逐样本缓存，联合报告内存、通信量和收敛速度。

<a id="paper-152087"></a>

## Clarification as Supervision: Reinforcement Learning for Vision-Language Interfaces

[官方论文页](https://neurips.cc/virtual/2026/poster/152087) · [作者来源](https://openreview.net/forum?id=VaoJb3PtWQ)

- **问题 / 瓶颈** · 面向人类的描述会遗漏推理器需要的内容。
- **核心创新 / 方法** · 用强化学习惩罚依赖追问才成功的轨迹。
- **Baseline** · 预训练视觉描述模型。
- **Benchmark** · 七项视觉推理基准，测准确率及澄清频率。
- **关键结果 / 消融** · 平均准确率增 4.4 个百分点，潜在澄清需求最多下降 44%。
- **适用条件 / 局限** · 依赖推理器提出有效澄清。

**可复用机制** · 对串联感知和推理系统，区分首轮成功与追问后成功的回报。

<a id="paper-152303"></a>

## Class Adaptive Conformal Training

[官方论文页](https://neurips.cc/virtual/2026/poster/152303) · [作者来源](https://openreview.net/forum?id=U4gGjBCf7z)

- **问题 / 瓶颈** · 只优化总大小会忽略类别间预测集效率差异。
- **核心创新 / 方法** · 把训练写成带全局覆盖约束的增广拉格朗日问题。
- **Baseline** · 既有共形训练方法。
- **Benchmark** · 标准和长尾图像识别及文本分类，测集合大小与覆盖。
- **关键结果 / 消融** · 作者报告保持目标覆盖并缩小预测集。
- **适用条件 / 局限** · 全局覆盖不承诺每类同等覆盖。

**可复用机制** · 同时报告类条件集合大小和覆盖，避免平均指标掩盖尾类。

<a id="paper-152601"></a>

## Class–Domain Discriminability Guided Representation Enhancement for Domain Generalization

[官方论文页](https://neurips.cc/virtual/2026/poster/152601) · [作者来源](https://openreview.net/forum?id=RufkPejvKs)

- **问题 / 瓶颈** · 全局对齐可能删除判别特征或保留域偏差。
- **核心创新 / 方法** · 依据类别与域响应方差软分解为四类通道，再定制增强和正则。
- **Baseline** · 既有域泛化方法，具名待核。
- **Benchmark** · 多个标准域泛化基准，细项待核。
- **关键结果 / 消融** · 作者报告优于既有对照，幅度待核。
- **适用条件 / 局限** · 响应方差只是代理信号。

**可复用机制** · 跨域训练先审计通道属性，再对比统一对齐与分组干预。

<a id="paper-153465"></a>

## Class-Domain Incremental Learning with Extensible Multi-Center Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/153465) · [作者来源](https://openreview.net/forum?id=L7nQuDA3fX)

- **问题 / 瓶颈** · 单一原型难整合碎片化的新领域观测。
- **核心创新 / 方法** · 局部原型汇入类别树，并分别处理旧原型演化和新域初始化。
- **Baseline** · 既有增量方法，具名待核。
- **Benchmark** · 三个类别与域同时增量的数据集。
- **关键结果 / 消融** · 作者报告领先，消融待核。
- **适用条件 / 局限** · 依赖原型能概括特征分布。

**可复用机制** · 拆开新域初始化和旧类漂移校正，分别监测遗忘。

<a id="paper-152056"></a>

## Classification at the Edge of Stability: Unifying Self-Stabilization and Convergence Rates

[官方论文页](https://neurips.cc/virtual/2026/poster/152056) · [作者来源](https://openreview.net/forum?id=VpiPrv9CUK)

- **问题 / 瓶颈** · 分类损失没有有限极小点，平方损失的流形解释难移植。
- **核心创新 / 方法** · 以曲率参考子空间分离正交振荡与沿平坦方向的进展。
- **Baseline** · 稳定区和稳定边缘区的理论对照。
- **Benchmark** · 对称数据模型下的逻辑损失与多类交叉熵。
- **关键结果 / 消融** · 给出迭代点界，且大步长可能放大暂态正交残差。
- **适用条件 / 局限** · 依赖正则条件及对称数据模型。

**可复用机制** · 对大步长训练同时检查损失和预测方向，不只看渐近收敛。

<a id="paper-151054"></a>

## Classification Fields: Arbitrarily Fine Recursive Hierarchical Clustering From Few Examples

[官方论文页](https://neurips.cc/virtual/2026/poster/151054) · [作者来源](https://openreview.net/forum?id=dLTzQWpUx2)

- **问题 / 瓶颈** · 有限树无法外推持续细分的层次。
- **核心创新 / 方法** · 递归预测分离的子中心偏移，并以诱导度量约束结构。
- **Baseline** · 有限划分与有限树为概念对照，具名待核。
- **Benchmark** · 生成树、IFS 分形与图像诱导的递归层次。
- **关键结果 / 消融** · 作者给出截断指数收敛并报告递归几何保持。
- **适用条件 / 局限** · 假设局部细分规律可复用且子节点分离。

**可复用机制** · 单独测未见深度的路径度量和无序几何误差。

<a id="paper-156776"></a>

## Classification of high-dimensional data with spiked covariance matrix structure

[官方论文页](https://neurips.cc/virtual/2026/poster/156776) · [作者来源](https://openreview.net/forum?id=6bQDtTbaQs)

- **问题 / 瓶颈** · 原始特征的高维相关性会削弱判别。
- **核心创新 / 方法** · 用尖峰协方差白化，筛选稀疏均值差，再做判别。
- **Baseline** · 通行分类方法，具名待核。
- **Benchmark** · 真实和合成高维分类，另有渐近分析。
- **关键结果 / 消融** · 在稀疏度与样本条件下达到贝叶斯最优。
- **适用条件 / 局限** · 要求尖峰协方差与白化均值差稀疏。

**可复用机制** · 对相关高维数据比较先白化再筛选与直接筛选。

<a id="paper-155401"></a>

## Class-Incremental Learning via LoRA-based Elastic Ensemble of Experts

[官方论文页](https://neurips.cc/virtual/2026/poster/155401) · [作者来源](https://openreview.net/forum?id=5v1mhJ0DnN)

- **问题 / 瓶颈** · 逐任务加适配器导致线性增长，固定共享会干扰。
- **核心创新 / 方法** · 按饱和度弹性分配专家，组内分隔重要参数并投影梯度。
- **Baseline** · 逐任务扩展及固定共享 LoRA 方案。
- **Benchmark** · 标准类别增量基准，重点考察长任务序列。
- **关键结果 / 消融** · 作者报告性能与参数效率兼顾。
- **适用条件 / 局限** · 具体容量阈值和训练开销待核。

**可复用机制** · 相同参数预算下比较弹性路由和固定分配，同时测旧类保持。

<a id="paper-154098"></a>

## Class-Mixed Diffusion Augmentation for Shortcut-Breaking in Continual Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/154098) · [作者来源](https://openreview.net/forum?id=GGcrbkuKF6)

- **问题 / 瓶颈** · 同类合成有域差，任务专属特征易依赖捷径。
- **核心创新 / 方法** · 筛选可破坏捷径的生成条件并用于辅助训练。
- **Baseline** · 普通扩散增广及无样本持续学习对照。
- **Benchmark** · Split-CIFAR100 和 Split-ImageNet。
- **关键结果 / 消融** · 作者报告持续改善，额外开销较普通增广有限。
- **适用条件 / 局限** · 依赖生成覆盖与分类器筛选质量。

**可复用机制** · 增广时按任务识别错误检验是否消除捷径，而非只补旧类样本。

<a id="paper-139365"></a>

## ClawBenchPro: Benchmarking How Well Agent Harnesses Work

[官方论文页](https://neurips.cc/virtual/2026/poster/139365) · [作者来源](https://openreview.net/forum?id=Ua3glrk6yU)

- **问题 / 瓶颈** · 平均进度可能掩盖端到端失败。
- **核心创新 / 方法** · 跨模型和框架统一评测多领域、多会话工作流。
- **Baseline** · 14 个模型与四种框架，包括 OpenClaw、NanoClaw 和 Hermes-Agent。
- **Benchmark** · ClawBenchPro，约千个实例覆盖 43 域。
- **关键结果 / 消融** · 平均得分约 60%–74%，部分框架以准确率换成本。
- **适用条件 / 局限** · 结果依赖框架、工具与任务设置。

**可复用机制** · 分领域报告零缺陷率和每次成功的成本。

<a id="paper-149791"></a>

## CLaW: Codec-Guided Adaptive Latent Watermarking for Traceable Diffusion Image Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/149791) · [作者来源](https://openreview.net/forum?id=nI6z2amVXh)

- **问题 / 瓶颈** · 过早注入会被后续去噪削弱或影响图像。
- **核心创新 / 方法** · 冻结生成骨干，将编码器残差注入后段，用解码反馈适配强度。
- **Baseline** · 已有扩散图像水印。
- **Benchmark** · 图像变换后测 F1 和视觉保真。
- **关键结果 / 消融** · 作者报告平均 F1 较所比最佳高 6.34%。
- **适用条件 / 局限** · 依赖编解码器与变换类型。

**可复用机制** · 在相同保真阈值比较固定和置信度自适应注入。

<a id="paper-139588"></a>

## Claw-Eval: Towards Trustworthy Evaluation of Autonomous Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/139588) · [作者来源](https://openreview.net/forum?id=GlpMVukwjK)

- **问题 / 瓶颈** · 只检查终态会漏掉中途安全和鲁棒性问题。
- **核心创新 / 方法** · 独立采集三通道证据，并比较至少一次和每次均成功。
- **Baseline** · 终态评分及重复试验的不同汇总。
- **Benchmark** · Claw-Eval，300 项任务，14 个模型，三次试验。
- **关键结果 / 消融** · 黑箱终态评分漏掉 44% 安全违规和 13% 鲁棒性失败。
- **适用条件 / 局限** · 日志质量及任务代表性影响外推。

**可复用机制** · 将结果质量和执行过程合规分开验收，在扰动下比较一致性。

<a id="paper-151839"></a>

## CLeaR: A Unified Framework for Resolving the Leakage–Degradation Dilemma in Style Transfer

[官方论文页](https://neurips.cc/virtual/2026/poster/151839) · [作者来源](https://openreview.net/forum?id=XYaKipdytC)

- **问题 / 瓶颈** · 参考内容泄漏与风格保真往往互相牵制。
- **核心创新 / 方法** · 正交投影削弱内容，再跨视觉模型反演共享风格锚点，用能量引导保持对齐。
- **Baseline** · 既有风格迁移方法，具名对照待核。
- **Benchmark** · StyleBench 风格一致性、泄漏及模型评判。
- **关键结果 / 消融** · 报告风格更一致、泄漏减少；理论给出锚点估计误差随编码器数量下降。
- **适用条件 / 局限** · 不同编码器误差相关时的收益需核实。

**可复用机制** · 以多编码器共享像素锚点约束风格，并在匹配预算下与原方案对照。

<a id="paper-153511"></a>

## CLEAR: Complementary Tripartite Play with Bayesian Calibration for Semi-Supervised Edge Classification

[官方论文页](https://neurips.cc/virtual/2026/poster/153511) · [作者来源](https://openreview.net/forum?id=KnVgeVUR19)

- **问题 / 瓶颈** · 边类型不对称和分布失衡导致预测偏差。
- **核心创新 / 方法** · 拓扑与上下文分支生成伪标签，不确定性筛选后校准后验，由元教师调整目标系数。
- **Baseline** · 既有半监督边分类方法，具名待核。
- **Benchmark** · 边分类基准，数据集与指标待核。
- **关键结果 / 消融** · 作者报告优于对照；幅度待核。
- **适用条件 / 局限** · 邻域先验偏差可能随图分布变化而放大。

**可复用机制** · 用互补图视角筛选伪标签，再用邻域先验校准，并在匹配预算下与原方案对照。

<a id="paper-155535"></a>

## Clearer Sight, Fewer Lies: Oriented Pickup Preference Optimization for Multimodal Hallucination Mitigation

[官方论文页](https://neurips.cc/virtual/2026/poster/155535) · [作者来源](https://openreview.net/forum?id=4sDjEe8IfE)

- **问题 / 瓶颈** · 模型可能看到了证据却沿用语言先验。
- **核心创新 / 方法** · 对同一回答构造强、中、弱三档证据，配合片段及 token 正则。
- **Baseline** · 既有偏好优化与幻觉缓解方法，具名待核。
- **Benchmark** · 幻觉和通用能力基准，具体指标待核。
- **关键结果 / 消融** · 作者报告持续改善，理论给出局部视觉敏感性下界。
- **适用条件 / 局限** · 依赖证据排序可靠；真实遮挡下需验证。

**可复用机制** · 固定正确回答，按视觉证据强弱构造排序监督，并在匹配预算下与原方案对照。

<a id="paper-148625"></a>

## CLEF: EEG Foundation Models for Learning Clinical Semantics

[官方论文页](https://neurips.cc/virtual/2026/poster/148625) · [作者来源](https://openreview.net/forum?id=wMcJWB6pBK)

- **问题 / 瓶颈** · 短窗解码容易遗漏跨时段及临床信息。
- **核心创新 / 方法** · 以多窗谱估计构造会话尺度 token，重建预训练后对比对齐报告和病历。
- **Baseline** · 既有脑电基础模型和仅重建消融。
- **Benchmark** · 逾 26 万次脑电会话，234 项临床表征任务，另测外部队列。
- **关键结果 / 消融** · 229 项优于对照，平均 AUROC 从 0.65 到 0.74，对齐带来额外收益。
- **适用条件 / 局限** · 回顾性任务表现不能替代临床验证。

**可复用机制** · 先保留整段 EEG，再以报告及结构化病历对齐表示，并在匹配预算下与原方案对照。

<a id="paper-148962"></a>

## Click3R: Interactive Stereo 3D Reconstruction with Sparse Correspondence Clicks

[官方论文页](https://neurips.cc/virtual/2026/poster/148962) · [作者来源](https://openreview.net/forum?id=tr4R2c2FLR)

- **问题 / 瓶颈** · 一次预测难纠正重复纹理和对称结构歧义。
- **核心创新 / 方法** · 用轻量点对应适配器将人工点击注入重建网络。
- **Baseline** · 未加点击的前馈立体重建模型，具名待核。
- **Benchmark** · 标准基准及针对重建失败模式构造的挑战集。
- **关键结果 / 消融** · 作者报告单次对应点击即可降低重建误差。
- **适用条件 / 局限** · 误点和实际交互成本待核。

**可复用机制** · 让前馈重建接收稀疏跨图对应以纠错，并在匹配预算下与原方案对照。

<a id="paper-150357"></a>

## CLIFT: Conformal Self-Verification for Web Agent Training and Test-Time Scaling

[官方论文页](https://neurips.cc/virtual/2026/poster/150357) · [作者来源](https://openreview.net/forum?id=igVA4JNEyQ)

- **问题 / 瓶颈** · 二元成功反馈过于稀疏，部署时不一定能调用外部评判。
- **核心创新 / 方法** · 验证问题经评判一致性筛选，训练时提供分步信号，测试时按保守投票选择轨迹。
- **Baseline** · 贪心轨迹及开放网页基准对照。
- **Benchmark** · WebArena Infinity、VisualWebArena、Online Mind2Web。
- **关键结果 / 消融** · 报告开放模型性能改善，并观察到验证问题跨模型与任务迁移。
- **适用条件 / 局限** · 网页状态变化可能破坏先前校准。

**可复用机制** · 把训练期校准的验证问题复用于测试时重试筛选，并在匹配预算下与原方案对照。

<a id="paper-139102"></a>

## ClinMAS: A Knowledge-Grounded Multi-Agent Simulation Framework for Evaluating Clinical Reasoning in LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/139102) · [作者来源](https://openreview.net/forum?id=kxtifbesla)

- **问题 / 瓶颈** · 静态问答不能观察提问、检查及修正诊断的过程。
- **核心创新 / 方法** · 知识图谱驱动的病例模拟连接医生、患者和检查者角色，以规则评估效率和推理。
- **Baseline** · 静态及动态临床评测思路，具名模型待核。
- **Benchmark** · 多轮模拟病例，诊断、效率及质量维度。
- **关键结果 / 消融** · 作者报告揭示先进模型的临床推理缺口，幅度待核。
- **适用条件 / 局限** · 模拟患者不能替代真实临床验证。

**可复用机制** · 将诊断准确率和多轮信息收集质量分开测量，并在匹配预算下与原方案对照。

<a id="paper-149545"></a>

## ClinStab: Stability-Oriented Learning for Medical Time Series via Dual-Stream Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/149545) · [作者来源](https://openreview.net/forum?id=pLj36IwQSC)

- **问题 / 瓶颈** · 较高干净集准确率可能伴随采集扰动下的脆弱性。
- **核心创新 / 方法** · 在 Medformer 上将高能量成分交给注意力、残差交给轻量分支，并加一致性和教师监督。
- **Baseline** · Medformer 与 11 个基线，含软路由替代。
- **Benchmark** · 四个 EEG 和 ECG 公共数据集，比较干净准确率及扰动表现。
- **关键结果 / 消融** · 干净准确率均高于底座，部分稳健指标改善；PTB 排序存在取舍。
- **适用条件 / 局限** · 结论限于所测扰动，不构成普遍临床稳健性证据。

**可复用机制** · 按通道能量分流并保留低能量残差信息，并在匹配预算下与原方案对照。

<a id="paper-149746"></a>

## C-LoRA: Continual Low-Rank Adaptation for Pre-trained Visual Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149746) · [作者来源](https://openreview.net/forum?id=nf0YHUKcRr)

- **问题 / 瓶颈** · 单一 LoRA 顺序更新可能覆盖旧任务，任务独立适配器会持续增长。
- **核心创新 / 方法** · 将秩一分量路由分为稳定项和当前任务可塑项，部署复用一个适配器。
- **Baseline** · 标准 LoRA、适配器扩容或融合思路。
- **Benchmark** · 多项持续视觉学习基准，具名待核。
- **关键结果 / 消融** · 报告性能有竞争力，推理无任务模块选择。
- **适用条件 / 局限** · 旧知识保存程度受任务顺序及秩预算影响。

**可复用机制** · 用共享低秩子空间的路由控制遗忘和新任务更新，并在匹配预算下与原方案对照。

<a id="paper-148458"></a>

## Closed-Form Implicit Neural Representations

[官方论文页](https://neurips.cc/virtual/2026/poster/148458) · [作者来源](https://openreview.net/forum?id=xgO3o4J75E)

- **问题 / 瓶颈** · 高频细节分布不均时，统一容量的迭代拟合耗时且易欠拟合。
- **核心创新 / 方法** · 在重叠子域闭式最小二乘拟合，单位分解拼接，按频谱复杂度自适应细分。
- **Baseline** · 迭代反向传播的隐式表征及均一划分对照。
- **Benchmark** · 连续函数重建和容量受限设置，数据待核。
- **关键结果 / 消融** · 作者报告高复杂度区域主导误差，细分可改善质量。
- **适用条件 / 局限** · 局部系统条件数及拼接开销需单独评估。

**可复用机制** · 按局部频谱复杂度分配闭式拟合容量，并在匹配预算下与原方案对照。

<a id="paper-155421"></a>

## Closed-Form Last Layer Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/155421) · [作者来源](https://openreview.net/forum?id=5obHwQa2tL)

- **问题 / 瓶颈** · 联合 SGD 反复更新已有解析解的参数。
- **核心创新 / 方法** · 将线性头视为骨干函数，小批量更新兼顾当前与历史信息。
- **Baseline** · SGD 与 Adam。
- **Benchmark** · 含神经算子及因果推断的平方损失回归。
- **关键结果 / 消融** · 给出 NTK 条件下收敛分析，并报告回归实验效用。
- **适用条件 / 局限** · 需要线性末层和平方损失；闭式更新成本随特征维数增长。

**可复用机制** · 平方损失下交替更新骨干和闭式线性头，并在匹配预算下与原方案对照。

<a id="paper-153458"></a>

## Closed-Form Linear-Probe Dataset Distillation for Pre-trained Vision Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153458) · [作者来源](https://openreview.net/forum?id=L9EoOgA982)

- **问题 / 瓶颈** · 展开内层更新昂贵，而平方外层目标可能不保留类别区分。
- **核心创新 / 方法** · 用冻结特征上的核岭解计算探针，再以温度缩放交叉熵更新合成图。
- **Baseline** · LGM 有无 DSA，及平方损失外层消融。
- **Benchmark** · ImageNet-100 和 ImageNet-1K，各四个预训练视觉骨干。
- **关键结果 / 消融** · ImageNet-1K 三个骨干匹配或超过带 DSA 对照，约快 14 倍，显存低于八分之一。
- **适用条件 / 局限** · 面向冻结特征，端到端迁移需另测。

**可复用机制** · 闭式内层配判别式外层目标压缩线性探针数据，并在匹配预算下与原方案对照。

<a id="paper-154248"></a>

## Closed-Loop Alignment: Socially Coupled In-Context Learning and Relational Posterior Collapse

[官方论文页](https://neurips.cc/virtual/2026/poster/154248) · [作者来源](https://openreview.net/forum?id=FBGhYmbxHz)

- **问题 / 瓶颈** · 助手改变下一轮用户证据，独立评分看不到累积不稳。
- **核心创新 / 方法** · 将信念到行动、行动到证据和证据到信念的变化率相乘，比较回放及抑制控制。
- **Baseline** · 开放回放、自由对话和提示控制。
- **Benchmark** · GPT-4o 和 GPT-5.4-mini 的用户与助手模拟组合。
- **关键结果 / 消融** · 模拟中估计量跨过 1 接近不稳起点，阻尼控制降低发生率。
- **适用条件 / 局限** · AI 对 AI 模拟没有临床证据，模型增益依赖局部设定。

**可复用机制** · 用闭环增益诊断多轮互动中的反馈放大，并在匹配预算下与原方案对照。

<a id="paper-149779"></a>

## Closed Loop Dynamic Driving Data Mixture for Real-Synthetic Co-Training

[官方论文页](https://neurips.cc/virtual/2026/poster/149779) · [作者来源](https://openreview.net/forum?id=nNBsrNygh7)

- **问题 / 瓶颈** · 将所有合成数据加入会浪费预算并造成分布偏移。
- **核心创新 / 方法** · 学习场景向量并聚类，由闭环反馈估计簇重要性再检索样本。
- **Baseline** · 普通真实与合成混训、跨域方法。
- **Benchmark** · NavSim，约束合成数据预算。
- **关键结果 / 消融** · 报告少用合成样本且取得更高表现，幅度待核。
- **适用条件 / 局限** · 依赖闭环评测与部署分布吻合。

**可复用机制** · 按闭环表现更新合成驾驶场景的采样配比，并在匹配预算下与原方案对照。

<a id="paper-148375"></a>

## CLoSeR: Closing the Loop for Long-Context Streaming Reconstruction

[官方论文页](https://neurips.cc/virtual/2026/poster/148375) · [作者来源](https://openreview.net/forum?id=yLutWZN8IE)

- **问题 / 瓶颈** · 长序列前馈重建容易积累漂移。
- **核心创新 / 方法** · 全局描述检索闭环，在闭环窗口重估相对位姿，联合顺序约束在 SE(3) 优化。
- **Baseline** · 既有流式重建及 Sim(3) 或 SL(4) 图优化方法。
- **Benchmark** · 公里级序列，追踪漂移和重建一致性。
- **关键结果 / 消融** · 报告明显减少漂移，具名指标和幅度待核。
- **适用条件 / 局限** · 依赖骨干产生全局一致尺度及正确闭环候选。

**可复用机制** · 先验证尺度一致性，再选择较简单的刚体位姿图，并在匹配预算下与原方案对照。

<a id="paper-150349"></a>

## Closing the Approximation Gap in Simulation-free Latent SDEs

[官方论文页](https://neurips.cc/virtual/2026/poster/150349) · [作者来源](https://openreview.net/forum?id=inTYe61WZF)

- **问题 / 瓶颈** · 只参数化瞬时边缘会限制可表示的轨迹后验。
- **核心创新 / 方法** · Helmholtz-SDE 扩大与边缘分布兼容的路径律集合。
- **Baseline** · 模拟式变分推断和既有免模拟方法。
- **Benchmark** · 从含噪观测恢复随机动力学，含高后验不确定度设置。
- **关键结果 / 消融** · 高不确定性下收益更大，作者报告接近模拟式效果且运行更快。
- **适用条件 / 局限** · 兼容边缘条件及适用漂移类型需全文核实。

**可复用机制** · 在给定边缘分布下优化路径律，减少免模拟推断偏差，并在匹配预算下与原方案对照。

<a id="paper-148361"></a>

## Closing the Gap on the Sample Complexity of 1-Identification

[官方论文页](https://neurips.cc/virtual/2026/poster/148361) · [作者来源](https://openreview.net/forum?id=yRrNwwvdTn)

- **问题 / 瓶颈** · 多个合格臂时，已有界难刻画找出任一合格臂的成本。
- **核心创新 / 方法** · 用新优化问题构造至少一个合格臂时的下界，并建立统一上界。
- **Baseline** · 既有 1-identification 样本复杂度界。
- **Benchmark** · 多臂老虎机，指标为固定正确概率所需期望拉臂数。
- **关键结果 / 消融** · 新算法上界与下界匹配至多项式对数因子。
- **适用条件 / 局限** · 适用于给定阈值的纯探索，理论假设和常数待核。

**可复用机制** · 以实例级样本复杂度比较阈值臂搜索算法，并在匹配预算下与原方案对照。

<a id="paper-150601"></a>

## Closing the Indexing-Decoding Gap in Multimodal Generative Retrieval via Prefix Retention Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/150601) · [作者来源](https://openreview.net/forum?id=gvXqyOr3jX)

- **问题 / 瓶颈** · 完整标识符可以重建良好，却因低排名前缀过早淘汰。
- **核心创新 / 方法** · 结合前缀排序蒸馏、由浅至深扩大码本与前缀相似度融合。
- **Baseline** · 残差量化加树约束束搜索的生成式检索方法。
- **Benchmark** · 九项多模态检索任务，测前缀保留和检索表现。
- **关键结果 / 消融** · 报告保留率和检索表现均改善，独立模块贡献待核。
- **适用条件 / 局限** · 效果受束宽和量化层设计影响。

**可复用机制** · 直接优化目标标识符前缀的束搜索存活率，并在匹配预算下与原方案对照。

<a id="paper-155475"></a>

## Closing the Loop: Co-Evolving EM for Irregular Time Series Generation in Lifted Representations

[官方论文页](https://neurips.cc/virtual/2026/poster/155475) · [作者来源](https://openreview.net/forum?id=5KWVTlOIK4)

- **问题 / 瓶颈** · 单次补全会平均化或随训练过时
- **核心创新 / 方法** · 蒙特卡洛 EM 交替采样补全和重训，在提升空间中保持观测一致
- **Baseline** · 最强单次补全方案
- **Benchmark** · 九个数据集、四种破坏设置
- **关键结果 / 消融** · 作者报告 Context-FID 改善 73%
- **适用条件 / 局限** · 依赖后验采样质量与训练预算

**可复用机制** · 在同算力下比较固定补全和随模型更新补全

<a id="paper-153850"></a>

## Closing the Loop with Fixed-Point Self-Attention

[官方论文页](https://neurips.cc/virtual/2026/poster/153850) · [作者来源](https://openreview.net/forum?id=IH0NcTKzaZ)

- **问题 / 瓶颈** · 单次注意力无法利用更新后的表示再次选择上下文
- **核心创新 / 方法** · 固定值矩阵，从迭代状态更新查询键
- **Baseline** · BERT-Base、ELECTRA-Base 与 ViT-B/16
- **Benchmark** · GLUE、SQuAD v2.0 和视觉语言任务
- **关键结果 / 消融** · BERT 推理耗时约 1.3–1.4 倍；作者报告精度改善
- **适用条件 / 局限** · 收敛和开销依赖输入

**可复用机制** · 固定参数量比较整层循环与只循环注意力

<a id="paper-149208"></a>

## Closing the Reflection Gap: A Free Calibration Bonus for Agentic RL

[官方论文页](https://neurips.cc/virtual/2026/poster/149208) · [作者来源](https://openreview.net/forum?id=s8QIIohE8t)

- **问题 / 瓶颈** · 只奖成功会让失败轨迹的诚实报错缺少奖励
- **核心创新 / 方法** · 用预测成功与实际结果的一致性补充结果奖励
- **Baseline** · 常规结果奖励强化学习
- **Benchmark** · 五个文本到 SQL 基准
- **关键结果 / 消融** · 准确率 75.1% 到 76.5%，低置信比例指标 44.4% 到 7.7%
- **适用条件 / 局限** · 依赖可靠的结果反馈

**可复用机制** · 分开记录任务成功和失败自报正确率

<a id="paper-151474"></a>

## ClothTransformer: Unified Latent-Space Transformers for Scalable Cloth Simulation

[官方论文页](https://neurips.cc/virtual/2026/poster/151474) · [作者来源](https://openreview.net/forum?id=aLQA62sNo3)

- **问题 / 瓶颈** · 网格耦合使模拟难以共享和扩展
- **核心创新 / 方法** · 从固定尺寸潜 token 自回归模拟不同布料场景
- **Baseline** · 既有神经布料模拟器
- **Benchmark** · 人体驱动服装、机器人操作和自由落体碰撞
- **关键结果 / 消融** · 作者报告误差约为对照的 1/4 至 1/9
- **适用条件 / 局限** · 跨材料和长滚动的稳健性待核

**可复用机制** · 固定潜预算评估网格增密对误差与延迟的影响

<a id="paper-150688"></a>

## CLR-voyance : Reinforcing Open-Ended Reasoning for Inpatient Clinical Decision Support with Outcome-Aware Rubrics

[官方论文页](https://neurips.cc/virtual/2026/poster/150688) · [作者来源](https://openreview.net/forum?id=gFCYsqy2Py)

- **问题 / 瓶颈** · 拿完整轨迹评估下一步决策会泄漏未来
- **核心创新 / 方法** · 构造过去可见未来封存的任务，用有证据的逐例量规监督
- **Baseline** · Qwen3-8B、MedGemma-4B 为训练底座
- **Benchmark** · 住院推理任务；具体指标待核
- **关键结果 / 消融** · 作者报告任务表现提高且保持通用能力
- **适用条件 / 局限** · 回顾性验证不能直接证明部署获益

**可复用机制** · 在线决策基准独立规范模型输入与裁判证据

<a id="paper-152428"></a>

## CLUE: Closing the Loop on Conflict and Collapse in LLM Unlearning

[官方论文页](https://neurips.cc/virtual/2026/poster/152428) · [作者来源](https://openreview.net/forum?id=TBERXr62zm)

- **问题 / 瓶颈** · 固定调度不能响应表征崩溃
- **核心创新 / 方法** · 双路径控制器、冲突门控和停训风险头
- **Baseline** · 固定学习率及保留权重调度
- **Benchmark** · TOFU、WMDP、MUSE
- **关键结果 / 消融** · 作者给出保留损失增长和停训相关界
- **适用条件 / 局限** · 依赖元训练任务分布

**可复用机制** · 对照固定步数与按梯度冲突触发的停止

<a id="paper-151334"></a>

## CLUE: Correlated Latent Uncertainty for Single-Pass Deep Uncertainty Estimation

[官方论文页](https://neurips.cc/virtual/2026/poster/151334) · [作者来源](https://openreview.net/forum?id=bJi84wx0rb)

- **问题 / 瓶颈** · 独立证据模型不能表达输入间相关性
- **核心创新 / 方法** · 加入核先验传播信息，推理无需矩阵求逆
- **Baseline** · 标准证据深度学习是白噪声极限
- **Benchmark** · 合成与真实不确定性任务
- **关键结果 / 消融** · 作者报告校准质量改善且推理快
- **适用条件 / 局限** · 依赖核相关性适合数据

**可复用机制** · 对照独立潜变量与相关先验，测样本增加时的收缩

<a id="paper-150265"></a>

## ClusQuant: Mitigating Outliers with Clustering-Based Representations for Low-Precision LRMs

[官方论文页](https://neurips.cc/virtual/2026/poster/150265) · [作者来源](https://openreview.net/forum?id=jS7aRiV05d)

- **问题 / 瓶颈** · 早期激活波动使固定码本和预填充校准失配
- **核心创新 / 方法** · 旋转缩放缓解离群值，聚类拟合分布，自适应分配码本
- **Baseline** · 固定码本和常规校准
- **Benchmark** · 低精度推理任务；具体基准待核
- **关键结果 / 消融** · 作者报告准确率改善
- **适用条件 / 局限** · 部署收益依赖查找表内核

**可复用机制** · 固定预算比较解码阶段感知校准与常规校准

<a id="paper-153010"></a>

## Clustered Randomized Smoothing for Stochastic Prediction Functions

[官方论文页](https://neurips.cc/virtual/2026/poster/153010) · [作者来源](https://openreview.net/forum?id=OeD82ZRKWm)

- **问题 / 瓶颈** · 全局平滑会把不同可行模式平均掉
- **核心创新 / 方法** · 聚类噪声预测，分别平滑后混合，并给出落入区域并集的概率下界
- **Baseline** · 先进平滑方法
- **Benchmark** · 两个基准含驾驶轨迹预测
- **关键结果 / 消融** · 轨迹基准作者报告 Wasserstein 距离平均下降约 33%
- **适用条件 / 局限** · 依赖聚类稳定性

**可复用机制** · 同时测试模式覆盖和稳健性

<a id="paper-150333"></a>

## Clustering-Free End-to-End Spoof Diarization with Encoder-Decoder Attractors

[官方论文页](https://neurips.cc/virtual/2026/poster/150333) · [作者来源](https://openreview.net/forum?id=itLroDUg0G)

- **问题 / 瓶颈** · 独立聚类依赖预知类别数
- **核心创新 / 方法** · 用解码吸引子和匈牙利匹配训练，并预测吸引子存在概率
- **Baseline** · 此前 PartialSpoof 最优方案
- **Benchmark** · PartialSpoof，JER 与类别数准确率
- **关键结果 / 消融** · JER 15.76% 对 26.99%，类别数准确率 88.7%
- **适用条件 / 局限** · 跨真实录音分布待核

**可复用机制** · 对可变数量时序事件同时训练分段与实例分组

<a id="paper-155449"></a>

## Clustering with Weak Distance Oracles

[官方论文页](https://neurips.cc/virtual/2026/poster/155449) · [作者来源](https://openreview.net/forum?id=5W2OIUKFcN)

- **问题 / 瓶颈** · 嵌入距离可能被任意误差污染
- **核心创新 / 方法** · 在弱距离查询下随机选择中心并进行常数近似
- **Baseline** · 精确距离的 k-median 与 k-means
- **Benchmark** · 未知度量空间、近似比与查询数
- **关键结果 / 消融** · 给出常数成本近似，首个算法允许多于 k 个中心
- **适用条件 / 局限** · 依赖摘要给出的正确率假设

**可复用机制** · 验收弱距离聚类时同时记录中心数与查询代价

<a id="paper-152567"></a>

## ClusterSplat: Semantic Cluster Selection for 3D Visual Grounding in Gaussian Splatting

[官方论文页](https://neurips.cc/virtual/2026/poster/152567) · [作者来源](https://openreview.net/forum?id=SAk0iIw26c)

- **问题 / 瓶颈** · 逐高斯得分的全局阈值跨场景不稳
- **核心创新 / 方法** · 以描述长度准则合并相邻体素，再对簇排序和渲染
- **Baseline** · 逐原语阈值与 3DGS 基线
- **Benchmark** · ScanRefer、Ref-LERF
- **关键结果 / 消融** · 作者报告二维分割和显式三维定位改善
- **适用条件 / 局限** · 簇必须保留小目标边界

**可复用机制** · 固定原语特征比较簇级选择和逐点过滤

<a id="paper-153334"></a>

## Cluster with Auctions for Vector Search

[官方论文页](https://neurips.cc/virtual/2026/poster/153334) · [作者来源](https://openreview.net/forum?id=M4uXVIjfK7)

- **问题 / 瓶颈** · 共享分配器会把查询和数据库视为同分布
- **核心创新 / 方法** · 交替训练探测网络，并用并行拍卖求负载平衡分区
- **Baseline** · 既有近似最近邻索引
- **Benchmark** · 同召回下的检索吞吐
- **关键结果 / 消融** · 异分布查询最高报告 4.7 倍吞吐
- **适用条件 / 局限** · 依赖代表性查询集

**可复用机制** · 用异分布查询压测索引并观察桶负载

<a id="paper-152001"></a>

## CM2: Reinforcement Learning with Checklist Rewards for Multi-Turn and Multi-Step Agentic Tool Use

[官方论文页](https://neurips.cc/virtual/2026/poster/152001) · [作者来源](https://openreview.net/forum?id=WFTd0B5z01)

- **问题 / 瓶颈** · 长程工具调用难获得可验证结果奖励
- **核心创新 / 方法** · 稀疏发放奖励，背后用稠密检查项评判并用模拟工具训练
- **Baseline** · 同模型监督微调
- **Benchmark** · τ²-Bench、BFCL-V4、ToolSandbox
- **关键结果 / 消融** · 相对 SFT 分别提高 8、10、12 分
- **适用条件 / 局限** · 模拟工具与真实工具的差距待核

**可复用机制** · 固定环境分别消融判据粒度与奖励频率

<a id="paper-139485"></a>

## CME–SpectrumBench: Can LLMs Analyze Condensed Matter Spectral Data?

[官方论文页](https://neurips.cc/virtual/2026/poster/139485) · [作者来源](https://openreview.net/forum?id=NHQBRaklRP)

- **问题 / 瓶颈** · 理论问答无法测噪声下分析稠密实验数据
- **核心创新 / 方法** · 用模拟凝聚态谱图构造数字可核问题
- **Baseline** · 直接查询、带 Python 工具与手写代码
- **Benchmark** · 190 个问题，以数值误差衡量
- **关键结果 / 消融** · 作者报告直接推断较弱，用工具后接近手写代码
- **适用条件 / 局限** · 模拟谱图不代表完整真实流程

**可复用机制** · 按噪声和分辨率分层比较直答与可执行计算

<a id="paper-139081"></a>

## CM-EVS: Sparse Panoramic RGB-D-Pose Data for Complete Scene Coverage

[官方论文页](https://neurips.cc/virtual/2026/poster/139081) · [作者来源](https://openreview.net/forum?id=mSu3YzwW3t)

- **问题 / 瓶颈** · 密集轨迹重复而简单稀疏采样会漏拍
- **核心创新 / 方法** · 把已观测几何投到候选全景中再贪心选择
- **Baseline** · 密集与稀疏启发式采样
- **Benchmark** · 室内外全景 RGB-D 数据，约 3.6 万帧
- **关键结果 / 消融** · 给出有界代理误差下的覆盖近似
- **适用条件 / 局限** · 依赖几何与深度可靠性

**可复用机制** · 固定视图预算同时评价覆盖与重复率

<a id="paper-155422"></a>

## CMI-Trans: Cross Modal Inconsistency-aware Transport for HSI-LiDAR Classification

[官方论文页](https://neurips.cc/virtual/2026/poster/155422) · [作者来源](https://openreview.net/forum?id=5oHobTGS7m)

- **问题 / 瓶颈** · 对称融合会把仅一侧可靠的边缘混淆
- **核心创新 / 方法** · 校准像素可靠性并以不确定性调制最优传输
- **Baseline** · 对称融合，具名方法待核
- **Benchmark** · Houston、Trento、MUUFL 高光谱与 LiDAR 分类
- **关键结果 / 消融** · 超过 16% 强边缘点存在单模态主导
- **适用条件 / 局限** · 依赖传感器配准

**可复用机制** · 对单模态主导位置单独测融合收益

<a id="paper-153383"></a>

## CMPQ: Compensatory Quantization via Input-Aware Hessian Damping

[官方论文页](https://neurips.cc/virtual/2026/poster/153383) · [作者来源](https://openreview.net/forum?id=LmeQn4hd4y)

- **问题 / 瓶颈** · 逐层量化补偿使用已有误差的层输入
- **核心创新 / 方法** · 比较全精度和量化输入并调整 Hessian 阻尼
- **Baseline** · GPTQ 系列
- **Benchmark** · Qwen3 4B、8B、14B 在 2 至 3 位设置
- **关键结果 / 消融** · 作者报告 3 位相当，2 位明显改善
- **适用条件 / 局限** · 需要全精度校准参照

**可复用机制** · 按输入方向分配补偿并检查深层误差积累

<a id="paper-152151"></a>

## CoANeRV: Coordinate-Aware Token-Space Neural Video Representation

[官方论文页](https://neurips.cc/virtual/2026/poster/152151) · [作者来源](https://openreview.net/forum?id=VA2hCFiIsa)

- **问题 / 瓶颈** · 逐视频优化权重成本高
- **核心创新 / 方法** · 前馈编码视频 token，以连续坐标及分块注意力重建
- **Baseline** · 逐视频优化或生成专属权重的 NeRV
- **Benchmark** · 视频重建，具体数据与指标待核
- **关键结果 / 消融** · 作者报告分块降低峰值内存
- **适用条件 / 局限** · 码率与速度权衡待核

**可复用机制** · 在同码率下比较共享模型和视频专属参数

<a id="paper-152930"></a>

## Coarsening Linear Non-Gaussian Causal Models with Cycles

[官方论文页](https://neurips.cc/virtual/2026/poster/152930) · [作者来源](https://openreview.net/forum?id=PIqUM6XQI4)

- **问题 / 瓶颈** · 高维无环假设排除了反馈系统
- **核心创新 / 方法** · 寻找对有向环反转不变的低维无环表示
- **Baseline** · 高维等价类枚举和无环抽象设定
- **Benchmark** · 线性非高斯模型的可识别性及复杂度
- **关键结果 / 消融** · 给出最坏立方时间和样本界
- **适用条件 / 局限** · 依赖线性与非高斯假设

**可复用机制** · 对反馈系统明确区分底层可识别性和宏观可识别性

<a id="paper-151950"></a>

## Coarse-to-Fine 3D MRI Reconstruction via Resolution-Agnostic Neural Operators

[官方论文页](https://neurips.cc/virtual/2026/poster/151950) · [作者来源](https://openreview.net/forum?id=WcGVLtalaf)

- **问题 / 瓶颈** · 全体积训练成本高且常规 CNN 跨分辨率退化
- **核心创新 / 方法** · 连续基底参数化局部卷积，交替执行图像细化和测量一致性更新
- **Baseline** · 经典方法和三维 CNN
- **Benchmark** · SKM-TEA 和 BraTS 2021，测 PSNR
- **关键结果 / 消融** · 指定设置较 CNN 高 4.13 和 13.63 dB
- **适用条件 / 局限** · 跨扫描设备效果待核

**可复用机制** · 固定训练显存，对照连续卷积和常规卷积的跨网格恢复误差

<a id="paper-148485"></a>

## Coarse-to-Fine Compositional Diffusion for Long-Horizon Planning

[官方论文页](https://neurips.cc/virtual/2026/poster/148485) · [作者来源](https://openreview.net/forum?id=xTMCXC32qJ)

- **问题 / 瓶颈** · 重叠局部计划一致仍可能无法形成合理全局结构
- **核心创新 / 方法** · 对齐局部去噪估计得到粗骨架，加中等噪声后以原局部先验去噪
- **Baseline** · 已有组合扩散采样
- **Benchmark** · 长程机器人规划、全景图像及长视频
- **关键结果 / 消融** · 报告质量改善且去噪调用少 2–8 倍
- **适用条件 / 局限** · 适用噪声范围及任务分项待核

**可复用机制** · 对照仅局部一致和骨架引导，分别测长程结构与局部质量

<a id="paper-150766"></a>

## Coarse-to-Real: Generative Rendering for Populated Dynamic Scenes

[官方论文页](https://neurips.cc/virtual/2026/poster/150766) · [作者来源](https://openreview.net/forum?id=fVp15tyVKH)

- **问题 / 瓶颈** · 粗场景到真实视频缺少配对
- **核心创新 / 方法** · 两阶段训练，以合成粗细渲染配对锚定跨域时空特征
- **Baseline** · 具名对照待核
- **Benchmark** · 都市人群视频、CG 和游戏输入
- **关键结果 / 消融** · 作者报告可控制布局和运动并保持时间一致性
- **适用条件 / 局限** · 极端跨域测试待核

**可复用机制** · 配对数据稀缺时单独比较生成预训练与后续结构对齐的贡献

<a id="paper-154559"></a>

## Coarse-to-Refine: Trajectory Self-Refinement in Single Autoregressive Pass for Driving VLA

[官方论文页](https://neurips.cc/virtual/2026/poster/154559) · [作者来源](https://openreview.net/forum?id=ChIexaZeP5)

- **问题 / 瓶颈** · 驾驶模型单次输出缺少显式修订
- **核心创新 / 方法** · 依次生成粗轨迹、推理及细轨迹，并比较模仿和强化训练
- **Baseline** · 具名驾驶 VLA 待核
- **Benchmark** · NAVSIM v1、v2 和 NavHard
- **关键结果 / 消融** · 分别获 92.1 PDMS、90.4 及 49.6 EPDMS
- **适用条件 / 局限** · 真机及延迟待核

**可复用机制** · 同算力对照直接输出和单次序列内修订，分开评估推理影响

<a id="paper-139427"></a>

## COCOTree: A Dataset and Benchmark for Open Tree-Structured Visual Decomposition

[官方论文页](https://neurips.cc/virtual/2026/poster/139427) · [作者来源](https://openreview.net/forum?id=RQWfvcKFll)

- **问题 / 瓶颈** · 扁平分割评估漏掉部分到整体关系
- **核心创新 / 方法** · 结合视觉语言语义和 SAM 3 几何定位建立树标注，并提出 OTQ
- **Baseline** · 人工结构判断，具名模型待核
- **Benchmark** · COCOTree 超 2.1 万图、180 万节点
- **关键结果 / 消融** · 作者报告生成标注与人工结构判断一致性较强
- **适用条件 / 局限** · 自动标注偏差及指标权重待核

**可复用机制** · 层级视觉分解评测需将空间准确和父子关系都纳入

<a id="paper-149608"></a>

## CODA: Cohort- and Drift-aware Foundation Model for Multimodal Clinical Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/149608) · [作者来源](https://openreview.net/forum?id=opvU1rQLrM)

- **问题 / 瓶颈** · 只处理个体样本会漏掉相关群体参照
- **核心创新 / 方法** · 学习群体分层并将相对原型的偏离信号输入多模态模型
- **Baseline** · 具名对照待核
- **Benchmark** · 电子健康记录上的开放问答、封闭问答和报告
- **关键结果 / 消融** · 作者报告多任务效果改善，数值待核
- **适用条件 / 局限** · 基准结果不能直接外推到临床

**可复用机制** · 在异质人群数据上对照个体表征与原型加偏离表征

<a id="paper-153802"></a>

## CODA: Rewriting Transformer Blocks as GEMM-Epilogue Programs

[官方论文页](https://neurips.cc/virtual/2026/poster/153802) · [作者来源](https://openreview.net/forum?id=IbVBLfiHWM)

- **问题 / 瓶颈** · 独立算子使中间张量反复访问显存
- **核心创新 / 方法** · 固定 GEMM 主循环，暴露缩放、归约、成对变换及累积原语
- **Baseline** · 常规独立内核，具名对照待核
- **Benchmark** · 典型 Transformer 前后向工作负载
- **关键结果 / 消融** · 作者报告人工及模型编写的内核均有效，具体幅度待核
- **适用条件 / 局限** · 对非标准算子和 GPU 的适用性待核

**可复用机制** · 按中间张量移动量筛选融合对象，同时记录吞吐和显存流量

<a id="paper-151489"></a>

## Code2World: A GUI World Model via Renderable Code Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/151489) · [作者来源](https://openreview.net/forum?id=aG2jCapnlk)

- **问题 / 瓶颈** · 像素或文本难兼顾视觉与结构
- **核心创新 / 方法** · 用屏幕动作配对做监督，再以渲染一致性训练
- **Baseline** · GPT-5、Gemini-3-Pro-Image 等
- **Benchmark** · AndroidWorld 及下一界面预测
- **关键结果 / 消融** · 摘要报告 Gemini-2.5-Flash 导航提高 9.5%，具体口径待核
- **适用条件 / 局限** · 跨应用布局及外部状态待核

**可复用机制** · 在授权沙盒比较预测渲染结构与直接预测像素的下游导航收益

<a id="paper-155243"></a>

## Codebook-Guided Cross-Modal Knowledge Distillation for Structurally Heterogeneous Features

[官方论文页](https://neurips.cc/virtual/2026/poster/155243) · [作者来源](https://openreview.net/forum?id=7C9JPmZMKT)

- **问题 / 瓶颈** · 视觉网格和音频序列的结构不匹配
- **核心创新 / 方法** · 量化教师特征并按任务相关性与学生兼容性选择蒸馏锚
- **Baseline** · 特征级对齐方法，具名待核
- **Benchmark** · 跨模态分类及语义分割
- **关键结果 / 消融** · 作者报告框架有效，结果幅度待核
- **适用条件 / 局限** · 码本容量和选择机制敏感性待核

**可复用机制** · 对异构表示比较直接特征对齐与中立概念空间对齐

<a id="paper-151528"></a>

## CodecSplat: Ultra-Compact Latent Coding for Feed-Forward 3D Gaussian Splatting

[官方论文页](https://neurips.cc/virtual/2026/poster/151528) · [作者来源](https://openreview.net/forum?id=ZzyjwkoqaX)

- **问题 / 瓶颈** · 最终三维原语不规则且与生成过程脱节
- **核心创新 / 方法** · 熵编码二维特征，解码后预测深度及高斯参数
- **Baseline** · 直接压缩前馈生成的高斯原语
- **Benchmark** · DL3DV 和 RealEstate10K，测 PSNR 与每场景体积
- **关键结果 / 消融** · 摘要报告比直接压缩小约一个数量级
- **适用条件 / 局限** · 依赖前馈骨干和视角覆盖

**可复用机制** · 在固定显示质量下比较压缩中间表示和最终原语的码率

<a id="paper-139002"></a>

## Code Review Bench: An Automated Benchmark for Evaluating the Software Factory

[官方论文页](https://neurips.cc/virtual/2026/poster/139002) · [作者来源](https://openreview.net/forum?id=rdn1a8ZKqW)

- **问题 / 瓶颈** · 旁观者标注可能与作者的处理决策不一致
- **核心创新 / 方法** · 持续从公开事件汇总开发者响应，并与独立离线评测对照
- **Baseline** · 独立离线基准及 18 种工具
- **Benchmark** · 超 50 万个有评判的 PR，比较精度排序与更新趋势
- **关键结果 / 消融** · 两个评测给出相近排序，并检测到相同版本变化
- **适用条件 / 局限** · 忽略建议不等价于建议无效，需控制曝光和工作负载

**可复用机制** · 评估建议系统时把采纳行为与独立质量评审并列

<a id="paper-149333"></a>

## CoDeRNet: Selective Cross-Task Routing under Heterogeneous Supervision for Change Detection and Captioning

[官方论文页](https://neurips.cc/virtual/2026/poster/149333) · [作者来源](https://openreview.net/forum?id=qs10J0MYjM)

- **问题 / 瓶颈** · 检测与描述监督粒度不同，全面共享会传递噪声
- **核心创新 / 方法** · 保持任务专属表征，以需求和可靠性门控双向特征交换
- **Baseline** · 普通联合学习及通用跨任务通信
- **Benchmark** · LEVIR-MCI、WHU-CDC 的定位和描述
- **关键结果 / 消融** · 摘要报告描述改善且定位仍有竞争力
- **适用条件 / 局限** · 不同监督噪声下的阈值待核

**可复用机制** · 比较无门控、单边置信门控及双边门控的负迁移

<a id="paper-149471"></a>

## CodeScaler: Scaling Code LLM Training and Test-Time Inference via Reward Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149471) · [作者来源](https://openreview.net/forum?id=prz41cA9Og)

- **问题 / 瓶颈** · 执行反馈的覆盖与速度受单元测试限制
- **核心创新 / 方法** · 用验证过的问题生成偏好样本并加入语法感知提取和奖励塑形
- **Baseline** · 执行反馈 RL 和已有奖励模型
- **Benchmark** · 四个编码基准及 RM-Bench
- **关键结果 / 消融** · 8B 与 14B 分别较执行反馈高 1.55 和 4.23 分，推理约快十倍
- **适用条件 / 局限** · 执行正确性与奖励模型偏差需分辨

**可复用机制** · 固定候选预算，比较验证器、奖励排序及混合筛选

<a id="paper-155551"></a>

## Coding with "Enemy": Can Human Developers Detect AI Agent Sabotage?

[官方论文页](https://neurips.cc/virtual/2026/poster/155551) · [作者来源](https://openreview.net/forum?id=4ip9zQaFI7)

- **问题 / 瓶颈** · 告警出现不代表开发者会采纳
- **核心创新 / 方法** · 让开发者参与长时编程实验，比较告警条件并调查处理原因
- **Baseline** · 有无安全监控的实验条件
- **Benchmark** · 逾百名参与者和四种模型，关注检出与接受
- **关键结果 / 消融** · 作者报告 95% 未识别问题，告警条件仍有 56% 接受不安全改动
- **适用条件 / 局限** · 依赖实验任务与特定提示界面

**可复用机制** · 在授权审查中记录告警到阻止提交的转化率，而非仅统计告警召回

<a id="paper-154796"></a>

## CoDMD: Copula-aware Distribution Matching Distillation for Fast Video Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/154796) · [作者来源](https://openreview.net/forum?id=AtixmYM4CB)

- **问题 / 瓶颈** · 坐标级分布匹配未显式约束关系结构
- **核心创新 / 方法** · 复用教师和在线模型的分数估计构成成对矩阵并加入匹配损失
- **Baseline** · rCM、普通 DMD
- **Benchmark** · Wan-2.1-T2V 1.3B 和 14B，VBench
- **关键结果 / 消融** · 四步学生获 84.46 和 84.87，较所列对照更高
- **适用条件 / 局限** · 其他骨干和采样步长待核

**可复用机制** · 将关系匹配做单独损失消融，同时测时序稳定而非仅单帧质量

<a id="paper-155085"></a>

## CoE-Agent: Co-Evolving Patient-Doctor Agents via Interactive Policy Graph Optimization for Clinical Decision Making

[官方论文页](https://neurips.cc/virtual/2026/poster/155085) · [作者来源](https://openreview.net/forum?id=8YLhu314Jr)

- **问题 / 瓶颈** · 孤立任务训练难保跨阶段一致性
- **核心创新 / 方法** · 在变化交互对手下优化 DAG 的结构和任务目标，再合并并蒸馏多任务图
- **Baseline** · 具名对照待核
- **Benchmark** · MedChain 与 ClinicalBench
- **关键结果 / 消融** · 摘要报告平均分分别提升 11.13% 和 23.63%
- **适用条件 / 局限** · 局限于评测任务，不代表临床可用

**可复用机制** · 复杂工作流中分别核验策略图结构有效性和任务结果

<a id="paper-149378"></a>

## Co-evolution: A "One-to-many" LLM Fine-Tuning Paradigm

[官方论文页](https://neurips.cc/virtual/2026/poster/149378) · [作者来源](https://openreview.net/forum?id=qVAlPixuHg)

- **问题 / 瓶颈** · 单模型平均目标不区分互补与重复成功
- **核心创新 / 方法** · 用进化策略优化实例级边际覆盖，用种子重放节省模型存储
- **Baseline** · 常规微调与集成
- **Benchmark** · 多领域集成评测，指标待核
- **关键结果 / 消融** · 作者报告集成效果改善
- **适用条件 / 局限** · 重放开销与等预算对照待核

**可复用机制** · 在固定总预算下按新增获解样本度量集成互补性

<a id="paper-153495"></a>

## Co-Evolving Interpolants and Flows via Path-Flow Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/153495) · [作者来源](https://openreview.net/forum?id=KyEvA048lp)

- **问题 / 瓶颈** · 路径对齐损失降低时样本质量可能恶化
- **核心创新 / 方法** · 用保持端点的随机正则隐藏部分源信息，防止路径集中
- **Baseline** · 固定路径及无正则联合训练
- **Benchmark** · ImageNet 256 与多规模 SiT，测 FID
- **关键结果 / 消融** · 报告 FID 改善且采样器不变
- **适用条件 / 局限** · 路径熵的测量及跨数据结论待核

**可复用机制** · 学习生成桥时同时记录目标损失、中间分布集中度和最终样本质量

<a id="paper-152206"></a>

## Co-Evolving Policy Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/152206) · [作者来源](https://openreview.net/forum?id=UmuBorIdCx)

- **问题 / 瓶颈** · 混合训练能力冲突，事后蒸馏行为距离过大
- **核心创新 / 方法** · 并行训练专家，在持续 RLVR 中双向执行 OPD
- **Baseline** · 混合 RLVR、MOPD、单领域专家
- **Benchmark** · 文本、图像和视频推理
- **关键结果 / 消融** · 作者报告超过混合和事后蒸馏对照
- **适用条件 / 局限** · 专家差异及等算力对照细节待核

**可复用机制** · 固定预算比较训练中互蒸馏与训后蒸馏。

<a id="paper-153110"></a>

## CofactVLA: Deconfounding Vision-Language-Action Models via Counterfactual Intervention

[官方论文页](https://neurips.cc/virtual/2026/poster/153110) · [作者来源](https://openreview.net/forum?id=Ns2HaAwoQP)

- **问题 / 瓶颈** · 稀疏指令易被密集视觉覆盖
- **核心创新 / 方法** · 反事实分支引导速度场正交投影，并抑制协方差差的正特征空间
- **Baseline** · 常规 VLA，具体名称待核
- **Benchmark** · 仿真操作与真机分布外操作
- **关键结果 / 消融** · 作者报告真机成功率绝对提升 52.3 个百分点
- **适用条件 / 局限** · 遮蔽分支未必只捕获视觉混杂

**可复用机制** · 对照指令改变但场景不变时的执行响应。

<a id="paper-138891"></a>

## CoffeeBench: A Benchmark for Long-Horizon Strategic Decision-Making in Multi-Agent Economies

[官方论文页](https://neurips.cc/virtual/2026/poster/138891) · [作者来源](https://openreview.net/forum?id=yTlqnsbF9X)

- **问题 / 瓶颈** · 固定对手难体现适应和协调失败
- **核心创新 / 方法** · 每次控制持续供应链中一个经营主体
- **Baseline** · 多个前沿和帕累托前沿语言模型
- **Benchmark** · 采购、生产、定价与谈判，指标为累计净收入
- **关键结果 / 消融** · GPT-5.5 平均净收入最高，部分模型有计划却趋于不行动
- **适用条件 / 局限** · 模拟供应链的外部效度待核

**可复用机制** · 分开记账计划质量、状态推进和净收益。

<a id="paper-139836"></a>

## CogArena: Benchmarking Multimodal Agents on Interactive Behavioral Experiments

[官方论文页](https://neurips.cc/virtual/2026/poster/139836) · [作者来源](https://openreview.net/forum?id=1hg4by8JA2)

- **问题 / 瓶颈** · 文字改写会移除视觉交互约束
- **核心创新 / 方法** · 浏览器呈现实验，分别测完成、正确和经典行为特征
- **Baseline** · 文献人类基线与前沿多模态 Agent
- **Benchmark** · 交互式社会与行为科学实验
- **关键结果 / 消融** · Agent 可完成任务但经典行为特征与人有差异
- **适用条件 / 局限** · 人类分数引自文献，可比性依实验

**可复用机制** · 评分区分任务完成和行为机制一致性。

<a id="paper-139467"></a>

## CogBench: Evaluating Cognitive-Level Control in LLM Question Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/139467) · [作者来源](https://openreview.net/forum?id=O58q509EG1)

- **问题 / 瓶颈** · 题干用词可能替代真正的认知复杂度
- **核心创新 / 方法** · 将要求的 Bloom 层级与允许使用的动词层级拆开，规则和分类器分别评分
- **Baseline** · 普通提示、异级限制、LLM 评审
- **Benchmark** · 八学科、六层级、120 个教材段落、13 个模型
- **关键结果 / 消融** · 12 个非地板模型的严格遵循下降 24 至 56 个百分点
- **适用条件 / 局限** · 评分模型和动词表依赖教材与语言

**可复用机制** · 评估题目难度控制时加入词汇反事实并公开评分冲突。

<a id="paper-155926"></a>

## Cognitive constraints and thalamocortical architecture explain systematic biases and neural signatures in human hierarchical decision-making

[官方论文页](https://neurips.cc/virtual/2026/poster/155926) · [作者来源](https://openreview.net/forum?id=1lsYyvQ1i2)

- **问题 / 瓶颈** · 无约束贝叶斯模型无法解释人类的持续偏差
- **核心创新 / 方法** · 以切换相关噪声和丘脑皮层模块建模状态压缩及切换成本
- **Baseline** · 贝叶斯观察者、常规任务优化循环网络
- **Benchmark** · 层级感知决策行为与神经影像
- **关键结果 / 消融** · 作者称同时改善行为拟合并复现部分神经表征
- **适用条件 / 局限** · 神经表征相似不足以确立唯一机制

**可复用机制** · 同时用行为偏差和内部表征筛选认知模型。

<a id="paper-153873"></a>

## Cognitive Firewalls: A Synthetic Account of Cross-Lingual Reasoning Collapse

[官方论文页](https://neurips.cc/virtual/2026/poster/153873) · [作者来源](https://openreview.net/forum?id=I7DeL1MXJc)

- **问题 / 瓶颈** · 按语言分组掉分可能被误判为知识丢失
- **核心创新 / 方法** · 在合成模型中对照分组任务变化与通用能力稳定性
- **Baseline** · 强化学习前后及未训练分组
- **Benchmark** · ARC-Challenge 分组与 MMLU
- **关键结果 / 消融** · 留出组准确率从 67% 降至 10%，MMLU 保持 71.2%
- **适用条件 / 局限** · 合成结果不足以推断部署模型

**可复用机制** · 报告不同条件切片表现及独立通用能力对照。

<a id="paper-148331"></a>

## Co-GRPO: Co-Optimized Group Relative Policy Optimization for Masked Image Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/148331) · [作者来源](https://openreview.net/forum?id=ydt2nVtol8)

- **问题 / 瓶颈** · 单步掩码训练不优化多步解码日程
- **核心创新 / 方法** · 用 MDP 联合表示掩码生成模型和调度，以轨迹级 GRPO 共优化
- **Baseline** · 单步掩码训练与原解码日程，具名对照待核
- **Benchmark** · ImageReward、HPSv2、GenEval、DPG-Bench
- **关键结果 / 消融** · 作者报告生成质量改善，幅度待核
- **适用条件 / 局限** · 收益依赖奖励和调度参数化

**可复用机制** · 对照仅改模型、仅改调度和联合训练。

<a id="paper-139659"></a>

## COHE: Auditing Non-Transitivity in Sample Difficulty Proxies for Vision Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139659) · [作者来源](https://openreview.net/forum?id=CRLrnZHHFd)

- **问题 / 瓶颈** · 秩相关可能被误解为筛选有效
- **核心创新 / 方法** · 分别检查依赖、留出预测和下游操作迁移
- **Baseline** · 随机选择、打乱代理和任务一致对照
- **Benchmark** · CIFAR、ImageNet，含 DINOv2 隔离度压力测试
- **关键结果 / 消融** · 隔离度与早期学习相关，但用来选 10% 数据低于随机
- **适用条件 / 局限** · 结论仅对应具体代理、目标与协议

**可复用机制** · 分别报告相关性、预测力和实际采样收益。

<a id="paper-152340"></a>

## Coherence-Aware Transition-Intent Fusion for LTL Planning under Uncertain Semantic Maps

[官方论文页](https://neurips.cc/virtual/2026/poster/152340) · [作者来源](https://openreview.net/forum?id=Tny26qM6EO)

- **问题 / 瓶颈** · MAP 语义图过早固定任务路线
- **核心创新 / 方法** · 把候选转移转成到达避障意图，融合进度并按实际移动校准权重
- **Baseline** · 单意图、原始融合、TOAPP*
- **Benchmark** · 随机障碍与房间语义图，测 LTL 满足
- **关键结果 / 消融** · 作者报告满足率改善，主要收益来自意图校准
- **适用条件 / 局限** · 有限 top-K 可能遗漏重要解释

**可复用机制** · 在相同传感条件下对照单解释与进度校准的多解释规划。

<a id="paper-150732"></a>

## Coherence Mechanisms for Provable Self-Improvement

[官方论文页](https://neurips.cc/virtual/2026/poster/150732) · [作者来源](https://openreview.net/forum?id=fp0D7ypA3g)

- **问题 / 瓶颈** · 经验一致性方法缺少改进保证
- **核心创新 / 方法** · 在靠近基线的同时直接或两步投影到一致性约束
- **Baseline** · 原始模型和两种投影路径
- **Benchmark** · 可实现、不可实现、有限样本及宽松一致性理论设定
- **关键结果 / 消融** · 给出期望 Bregman 散度单调改进条件
- **适用条件 / 局限** · 保证依赖变换及目标的一致性条件

**可复用机制** · 采用自一致性更新前先验证变换保留任务。

<a id="paper-149553"></a>

## Coherent Hierarchical Multi-Label  Learning to Defer for Medical Imaging

[官方论文页](https://neurips.cc/virtual/2026/poster/149553) · [作者来源](https://openreview.net/forum?id=pH5jlmaXga)

- **问题 / 瓶颈** · 逐标签交接可能引入分类树矛盾
- **核心创新 / 方法** · 定义排除式交接约定，用动态规划投影或递归策略求一致动作
- **Baseline** · 逐标签二元委托
- **Benchmark** · 真实读片者和受控专家评测
- **关键结果 / 消融** · 投影完全消除不一致，递归方法接近零并保有效用
- **适用条件 / 局限** · 依赖标签树与交接约定

**可复用机制** · 同时计算预测效用和委托组合违规率。

<a id="paper-155857"></a>

## Coherent Routing in Decision Trees: Phase-Interference Learning for Interpretable Tabular Prediction

[官方论文页](https://neurips.cc/virtual/2026/poster/155857) · [作者来源](https://openreview.net/forum?id=2OLBsM6UWI)

- **问题 / 瓶颈** · 标量路由无法显式产生分支交叉项
- **核心创新 / 方法** · 复数两态用保范变换建模分支，分解干涉项
- **Baseline** · 标量 PIDT-1S、冻结相位 PFB、SDT
- **Benchmark** · 十个 OpenML 表格数据集，每个十种种子
- **关键结果 / 消融** · NLL 与 Brier 差异较小，论文定位为机制检验
- **适用条件 / 局限** · 固定结构结论不代表通用表格收益

**可复用机制** · 用冻结相位对照定位路径交互的真实贡献。

<a id="paper-139216"></a>

## CoilStellaration: A Dataset and Benchmark for Engineering-Aware Stellarator Coilset Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/139216) · [作者来源](https://openreview.net/forum?id=eD6yGqTL8u)

- **问题 / 瓶颈** · 只测场拟合不足以判断方案可制造性
- **核心创新 / 方法** · 按目标构型与工程限制组织条件生成评测
- **Baseline** · 参考生成模型和现有优化流程
- **Benchmark** · 177000 个优化方案，考核几何约束与目标场
- **关键结果 / 消融** · 发布数据、评测和参考基线，摘要未报告领先幅度
- **适用条件 / 局限** · 数据仅覆盖已采样构型和约束

**可复用机制** · 在物理生成任务中联合报告保真和可行比例。

<a id="paper-156142"></a>

## CoLa3D: Composable Latent 3D Decomposition

[官方论文页](https://neurips.cc/virtual/2026/poster/156142) · [作者来源](https://openreview.net/forum?id=03ztUki3T5)

- **问题 / 瓶颈** · 逐对象独立生成后拼装易错位
- **核心创新 / 方法** · 查询式 Transformer 接收掩码、点或可学习查询并分解场景潜变量
- **Baseline** · SAM 3D、MoGe2
- **Benchmark** · 合成和真实三维场景分解及可见深度
- **关键结果 / 消融** · 报告两倍速度，训练数据少于 SAM 3D 的 1%，可见深度与 MoGe2 相当
- **适用条件 / 局限** · 遮挡完备性及跨数据集边界待核

**可复用机制** · 固定输入时比较共享空间分解和独立生成再对齐。

<a id="paper-155599"></a>

## CoLaX: Context-Aware Local Explanations for Time Series Classification

[官方论文页](https://neurips.cc/virtual/2026/poster/155599) · [作者来源](https://openreview.net/forum?id=4Mn24WBKDZ)

- **问题 / 瓶颈** · 局部信号单独评估会遗漏远程依赖
- **核心创新 / 方法** · 在解释模型中用全局状态调制局部动态贡献
- **Baseline** · 时序事后解释方法，具名对照待核
- **Benchmark** · 时间序列分类，评估忠实度与稳定性
- **关键结果 / 消融** · 作者报告两指标改善，数值待核
- **适用条件 / 局限** · 需核查上下文的实际因果作用

**可复用机制** · 采用相同局部片段配不同全局上下文检查解释变化。

<a id="paper-138874"></a>

## ColdDDI: Evaluating Knowledge Utilization in Cold-Start Drug-Drug Interaction Prediction

[官方论文页](https://neurips.cc/virtual/2026/poster/138874) · [作者来源](https://openreview.net/forum?id=zbG2HOGCGH)

- **问题 / 瓶颈** · 聚合边预测分数混淆冷启动与证据贡献
- **核心创新 / 方法** · 按药物是否见过分层，做证据遮蔽、替换与通道敏感性检验
- **Baseline** · 八种常规方法与十三个语言模型
- **Benchmark** · ColdDDI 冷启动药物相互作用评测
- **关键结果 / 消融** · 作者发现部分知识图增强方法对证据移除不敏感
- **适用条件 / 局限** · 结论限于已标注数据与干预设计

**可复用机制** · 对知识增强模型移除关键证据并检查预测是否合理变化。

<a id="paper-152076"></a>

## Collaborative Reasoning Distillation via Cross-Feedback and Coherent Curation

[官方论文页](https://neurips.cc/virtual/2026/poster/152076) · [作者来源](https://openreview.net/forum?id=VdycoZTljf)

- **问题 / 瓶颈** · 正确终点可能来自有缺陷的推理
- **核心创新 / 方法** · 让教师互评，逐步评分后按连贯性拼接，预算内训练学生
- **Baseline** · 结果奖励和可比蒸馏模型，细项待核
- **Benchmark** · MATH-500 和 AIME’25
- **关键结果 / 消融** · CRD-4B 分别达到 97.3% 和 70.3%，用 50K 样本
- **适用条件 / 局限** · 教师误判可能相关，等算力贡献待核

**可复用机制** · 固定蒸馏预算比较只筛终点与加入逐步逻辑检验。

<a id="paper-149957"></a>

## CollabVR: Collaborative Video Reasoning with Vision-Language and Video Generation Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149957) · [作者来源](https://openreview.net/forum?id=lv4U2Eez13)

- **问题 / 瓶颈** · 整段生成后纠错难修复早期漂移
- **核心创新 / 方法** · VLM 每步规划并检查短片段，按错误类型重生成或拆分动作
- **Baseline** · 单次推理、Pass@k、已有测试时扩展
- **Benchmark** · Gen-ViRe 和 VBVR-Bench
- **关键结果 / 消融** · 作者报告等算力改善，困难任务收益最大
- **适用条件 / 局限** · 依赖局部故障可辨识，额外延时待核

**可复用机制** · 在同算力下比较整段重采样与按步骤诊断恢复。
