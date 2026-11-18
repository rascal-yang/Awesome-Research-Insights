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

<a id="paper-154459"></a>

## Collapse Hunter: Tackling the Dimensional Degeneration in Generative Ranking

[官方论文页](https://neurips.cc/virtual/2026/poster/154459) · [作者来源](https://openreview.net/forum?id=DQIpp6LGTM)

- **问题 / 瓶颈** · 低基数行为 token 会拉低物品表示维度
- **核心创新 / 方法** · 分解注意力方向，仅在塌缩的行为查询物品通道对值施加非线性
- **Baseline** · 生成式排序基线
- **Benchmark** · 生成式推荐排序与有效秩评测，数据集待核
- **关键结果 / 消融** · 有效秩最高提升 12.58%，作者报告排序改善
- **适用条件 / 局限** · 其他通道与任务适用性待核

**可复用机制** · 按注意力通道测秩，比较全局和局部非线性。

<a id="paper-149747"></a>

## COLLAR: Cascaded Object-Level Latent Refinement for High-Fidelity Conditional Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/149747) · [作者来源](https://openreview.net/forum?id=neqB6nEQ0D)

- **问题 / 瓶颈** · 小区域对象控制容易产生伪影
- **核心创新 / 方法** · 在扩展视野分支对齐跨尺度语义，以频率自适应反馈更新全局特征
- **Baseline** · 已有对象级条件生成方法
- **Benchmark** · COCO-MIG、COCO-POS，测语义、画质、空间保真
- **关键结果 / 消融** · 作者报告三类指标改善，幅度待核
- **适用条件 / 局限** · 多对象冲突和计算代价待核

**可复用机制** · 比较直接贴回局部特征和经扩展上下文双向融合。

<a id="paper-139721"></a>

## ColorConceptBench: A Benchmark for Probabilistic Color-Concept Understanding in Text-to-Image Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139721) · [作者来源](https://openreview.net/forum?id=8XPtOZkQrP)

- **问题 / 瓶颈** · 显式颜色词测试掩盖情绪和状态等语义与颜色的关联
- **核心创新 / 方法** · 以专家标注建立隐式概念的概率色彩参考
- **Baseline** · 九种文生图模型及 CFG 调节
- **Benchmark** · 1,281 个概念和 6,584 条人工标注
- **关键结果 / 消融** · 抽象语义敏感度弱，调 CFG 后仍存在
- **适用条件 / 局限** · 标注群体和文化边界待核

**可复用机制** · 对可多解的生成语义以分布对照替代单标签。

<a id="paper-148997"></a>

## Colored Noise Diffusion Sampling

[官方论文页](https://neurips.cc/virtual/2026/poster/148997) · [作者来源](https://openreview.net/forum?id=ta2pzgldj0)

- **问题 / 瓶颈** · 白噪声忽略去噪过程中先低频后高频的差异
- **核心创新 / 方法** · 无须训练，在推理中把噪声能量集中到尚未解析的频带
- **Baseline** · 标准 ODE 和 SDE 求解器
- **Benchmark** · ImageNet-256，SiT、JiT、FLUX，测 FID
- **关键结果 / 消融** · SiT-XL/2 无引导 FID 从 8.26 降至 6.27，JiT-H/16 从 11.88 降至 8.31
- **适用条件 / 局限** · 其他模态和运行耗时待核

**可复用机制** · 固定模型与步数，对照白噪声和分频噪声。

<a id="paper-138980"></a>

## Colosseum: Auditing Collusion in Cooperative Multi-Agent Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/138980) · [作者来源](https://openreview.net/forum?id=spCefvRCT6)

- **问题 / 瓶颈** · 文本中的协作偏离意图未必落实到行为
- **核心创新 / 方法** · 以合作最优为参照计算动作遗憾，并和通信记录交叉核验
- **Baseline** · 正常合作与受控审计场景
- **Benchmark** · 多智能体合作任务上的行为和通信对照
- **关键结果 / 消融** · 作者观察到语言计划与实际动作不一致
- **适用条件 / 局限** · 结果依赖任务目标定义，外部有效性待核

**可复用机制** · 以真实目标达成率辅助判定系统风险，避免仅据文本告警。

<a id="paper-151062"></a>

## Colour me shocked: Exact Molecular Hessians from MLIPs in O(N) time using sparse differentiation!

[官方论文页](https://neurips.cc/virtual/2026/poster/151062) · [作者来源](https://openreview.net/forum?id=dIA3cMk8m7)

- **问题 / 瓶颈** · 局域势一阶计算可线性扩展，普通 Hessian 流程仍呈平方成本
- **核心创新 / 方法** · 利用局域相互作用导出稀疏结构，减少重复 Hessian 向量积
- **Baseline** · 逐方向稠密求导
- **Benchmark** · 烷烃和水团簇等原子系统，测运行时间与规模
- **关键结果 / 消融** · 作者报告总成本可为线性，所测系统约 2–15 倍加速
- **适用条件 / 局限** · 依赖局域性和稀疏度；长程耦合不直接满足

**可复用机制** · 求二阶信息前确认结构稀疏性，再对照稠密自动微分。

<a id="paper-154180"></a>

## CoLVR: Enhancing Exploratory Latent Visual Reasoning via Contrastive Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/154180) · [作者来源](https://openreview.net/forum?id=FdggkQpSHq)

- **问题 / 瓶颈** · 固定视觉目标压缩隐式推理的探索范围
- **核心创新 / 方法** · 用角度扰动构造潜表征对比监督，再以轨迹对比奖励做后训练
- **Baseline** · 硬对齐及已有潜推理模型
- **Benchmark** · VSP、Jigsaw、MMStar
- **关键结果 / 消融** · 作者报告分别提升 5.83%、8.00%、3.40%
- **适用条件 / 局限** · 具体比较口径与探索成本待核

**可复用机制** · 比较固定目标和相对约束下的潜推理与域外表现。

<a id="paper-152926"></a>

## Combating Camouflage and Forgetting: Spatio-Temporal Dual Denoising for Money Laundering Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/152926) · [作者来源](https://openreview.net/forum?id=PL6k93ECq7)

- **问题 / 瓶颈** · 异常信号在密集邻域中被稀释且跨时遗忘
- **核心创新 / 方法** · 防御检测以风险线索采样时序子图，结合重建和潜空间回放保留历史
- **Baseline** · 已有交易图检测方法
- **Benchmark** · 三个交易数据集的实体识别
- **关键结果 / 消融** · 作者报告优于对照，数值待核
- **适用条件 / 局限** · 标签分布和上线误报待核

**可复用机制** · 观察动态图异常时分别消融邻域选择与历史回放。

<a id="paper-148553"></a>

## Combating Catastrophic Forgetting in Continual Domain Adaptation via Knowledge Recasting

[官方论文页](https://neurips.cc/virtual/2026/poster/148553) · [作者来源](https://openreview.net/forum?id=x28eNvC5gp)

- **问题 / 瓶颈** · 直接顺序训练易损伤原有能力
- **核心创新 / 方法** · 以技能模式保留操作、依赖和验证步骤，抽去表面领域形式
- **Baseline** · 顺序后训练
- **Benchmark** · 两种 3B 指令模型的连续任务流与域外泛化
- **关键结果 / 消融** · 平均提高 2.53–5.75 分，Qwen-3B MATH 最大遗忘从 42.41 降为 7.10 分
- **适用条件 / 局限** · 依赖模式抽取有效及已有技能覆盖

**可复用机制** · 固定训练预算比较原始例子和按程序改写的例子。

<a id="paper-155652"></a>

## Combating Data Laundering in LLM Training

[官方论文页](https://neurips.cc/virtual/2026/poster/155652) · [作者来源](https://openreview.net/forum?id=41V90qR5dA)

- **问题 / 瓶颈** · 只查询原始文本可能漏掉变体训练暴露
- **核心创新 / 方法** · 使用面向检测的候选表达复核统计信号
- **Baseline** · 仅用原文查询的训练数据检测
- **Benchmark** · MIMIR，Pythia、Llama2、Falcon
- **关键结果 / 消融** · 作者报告防御审计信号恢复，幅度待核
- **适用条件 / 局限** · 依赖目标查询和独立参考语料，错误归因风险待核

**可复用机制** · 对审计方法单独测跨文本形式的召回和假阳性。

<a id="paper-150690"></a>

## COMET: Codebook-based Online-adaptive Multi-scale Embedding for Time-series Anomaly Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/150690) · [作者来源](https://openreview.net/forum?id=gEg9NAe7OM)

- **问题 / 瓶颈** · 多尺度异常和正常分布漂移难同时处理
- **核心创新 / 方法** · 多尺度编码后建立量化码本，以量化误差和密度感知距离双评分
- **Baseline** · 七个基线
- **Benchmark** · 五个数据集的 45 个评测项
- **关键结果 / 消融** · 作者报告 39 项领先
- **适用条件 / 局限** · 在线正常筛选失准可污染码本

**可复用机制** · 对照冻结原型和筛选后更新，测漂移及污染。

<a id="paper-151624"></a>

## CoMet: Context and Multiplicity Decomposition for Multimodal Uncertainty Estimation

[官方论文页](https://neurips.cc/virtual/2026/poster/151624) · [作者来源](https://openreview.net/forum?id=ZA1jp0eEhF)

- **问题 / 瓶颈** · 开放回答中多解与输入材料不足难区分
- **核心创新 / 方法** · 训练轻量后置模块估计二者，无需反复采样
- **Baseline** · 现有不确定性方法
- **Benchmark** · 开放多模态、幻觉检测与选择题视觉问答
- **关键结果 / 消融** · 作者报告估计改进且推理高效，幅度待核
- **适用条件 / 局限** · 拟合标注及跨任务校准待核

**可复用机制** · 对不同不确定性来源分别设置复核阈值。

<a id="paper-152607"></a>

## COMET: Decoupled Distillation, Routing, and Capacity Control for Task-Agnostic Continual Vision--Language Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/152607) · [作者来源](https://openreview.net/forum?id=RsE3HOXbTn)

- **问题 / 瓶颈** · 无旧数据和任务标签时，模态漂移与专家干扰耦合
- **核心创新 / 方法** · 蒸馏三类模态亲和关系，按客户端信号合并专家，部署以重建选路
- **Baseline** · 已有持续视觉语言学习和分模块消融
- **Benchmark** · X-TAIL
- **关键结果 / 消融** · 作者报告各模块均改善持续学习，幅度待核
- **适用条件 / 局限** · 需共享图文池，路由成本待核

**可复用机制** · 在相同容量下分开测试关系蒸馏和动态路由。

<a id="paper-153350"></a>

## CoMMa: Contribution-Aware Medical Multi-Agents for Decentralized Oncology Decision Support

[官方论文页](https://neurips.cc/virtual/2026/poster/153350) · [作者来源](https://openreview.net/forum?id=M1eBc5lFuT)

- **问题 / 瓶颈** · 分布式数据下，自由文本协商的贡献不稳定
- **核心创新 / 方法** · 专门代理使用本地数据，以确定性的嵌入投影近似边际贡献
- **Baseline** · 集中数据或提示分工的多代理方案
- **Benchmark** · 北美与东亚医院会议数据及公开肿瘤学评测
- **关键结果 / 消融** · 作者报告跨场景评测改善，幅度待核
- **适用条件 / 局限** · 不构成临床验证或正式隐私保证

**可复用机制** · 用可重复贡献估计诊断分区代理的汇总，并对照文本协调。

<a id="paper-151110"></a>

## Commit Then Explore: Reasoning Models Diversify, Not Converge

[官方论文页](https://neurips.cc/virtual/2026/poster/151110) · [作者来源](https://openreview.net/forum?id=cumW3H2I4l)

- **问题 / 瓶颈** · 长推理可能主要探索已形成答案附近的表达
- **核心创新 / 方法** · 用线性探针、稀疏自编码器和前后段消融量化形成与探索
- **Baseline** · 基础模型与四个自适应计算基线
- **Benchmark** · GSM8K、MATH、GPQA，三类推理模型
- **关键结果 / 消融** · 答案约在前 20% 可解码，监测节省 26–34% 计算且保留至少 92% 准确率
- **适用条件 / 局限** · 可解码不等于所有任务均可安全早停

**可复用机制** · 评估早停时同时检查初始答案的稳定性和剩余计算的因果收益。

<a id="paper-151353"></a>

## Communication-Efficient Federated Learning of Latent Patient Representations from Multi-Institutional EHRs

[官方论文页](https://neurips.cc/virtual/2026/poster/151353) · [作者来源](https://openreview.net/forum?id=bAy37JhHLo)

- **问题 / 瓶颈** · 跨医院直接汇集记录成本较高
- **核心创新 / 方法** · 本地仅上报边缘频率和低秩谱摘要，服务端恢复共同表示及标准化方向
- **Baseline** · 集中汇总、单站和已有联邦对照
- **Benchmark** · 模拟与真实多机构卒中电子病历
- **关键结果 / 消融** · 作者报告接近汇总估计，并给出逐行误差和方差下界相关结果
- **适用条件 / 局限** · 依赖谱结构和正则条件，分享摘要不等于差分隐私

**可复用机制** · 固定通信预算比较单次谱汇总和多轮训练。

<a id="paper-153942"></a>

## Communication-Efficient LLM Adaptation over Decentralized GPU Meshes

[官方论文页](https://neurips.cc/virtual/2026/poster/153942) · [作者来源](https://openreview.net/forum?id=HQjC0u4Aih)

- **问题 / 瓶颈** · 低带宽分布式适配中激活压缩会偏置梯度
- **核心创新 / 方法** · 异步快路压缩流水线和数据并行通信，慢路产生未压缩梯度供谱校正
- **Baseline** · 无压缩训练及单轴压缩
- **Benchmark** · 领域适配和持续预训练，含 200 Mbps 连接
- **关键结果 / 消融** · 作者报告流水线压缩最高 9 倍，双轴超过 40 倍且效果相当
- **适用条件 / 局限** · 锚点滞后和设备拓扑适用性待核

**可复用机制** · 测量快路吞吐与慢路校正频率对质量的共同影响。

<a id="paper-150059"></a>

## Communication-Efficient Personalized Adaptation via Federated-Local Model Merging

[官方论文页](https://neurips.cc/virtual/2026/poster/150059) · [作者来源](https://openreview.net/forum?id=l5U24ix94Z)

- **问题 / 瓶颈** · 任务异质时启发式混合难兼顾通用和个性知识
- **核心创新 / 方法** · 通过线性模式连通性导出方差迹上界及闭式权重
- **Baseline** · 本地和联邦模型及现有个性化方法
- **Benchmark** · 视觉与语言个性化适配和通信量
- **关键结果 / 消融** · 作者报告个性化和通信折衷改善
- **适用条件 / 局限** · 依赖可连通性，跨不兼容模型适用性待核

**可复用机制** · 用小型本地验证集比较闭式合并和固定权重。

<a id="paper-154739"></a>

## CommunityKV: Efficient Long-Context Decoding via Graph Partitioning

[官方论文页](https://neurips.cc/virtual/2026/poster/154739) · [作者来源](https://openreview.net/forum?id=BNHDGnaga1)

- **问题 / 瓶颈** · 逐 token 检索忽视关联，重聚类成本高。
- **核心创新 / 方法** · 复用 QK 分数构图，按社区取回 KV，新 token 局部归组。
- **Baseline** · 精确 FlashAttention-2。
- **Benchmark** · 开放权重模型长上下文任务，测解码吞吐与精度。
- **关键结果 / 消融** · 最高 1.86 倍吞吐，精度下降很小。
- **适用条件 / 局限** · 任务和模型细项待核。

**可复用机制** · 固定 KV 预算对照图分组和逐 token 选择。

<a id="paper-156037"></a>

## Commutator Memory: Sparse, Path-Local Reading and Steering in Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/156037) · [作者来源](https://openreview.net/forum?id=0vSuVjlB0R)

- **问题 / 瓶颈** · 总损失不能定位阶段顺序差异。
- **核心创新 / 方法** · 将两阶段梯度的 Lie 括号投影至 logits，形成 token 贡献。
- **Baseline** · 范数匹配随机方向及中性 dry-run 对照。
- **Benchmark** · Qwen SFT 留出 NLL、四个模型的配对终点。
- **关键结果 / 消融** · 支持重叠 82–99%，随机为 35–49%；Qwen-3-4B 干预弥合中位 32% 差距。
- **适用条件 / 局限** · 主要依据短步 SGD；AdamW 为试验。

**可复用机制** · 比较训练日程时除总损失外记录换序贡献集中在哪些 token。

<a id="paper-153373"></a>

## Comp$^2$VLM: A Hybrid Framework Combining Quantization and Lossless Compression for Efficient Vision-Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153373) · [作者来源](https://openreview.net/forum?id=Lr28LWsvm1)

- **问题 / 瓶颈** · 低精度伤害视觉语言对齐，无损解码可能串行。
- **核心创新 / 方法** · 按组降低量化熵，用共享 Huffman 表实现块并行。
- **Baseline** · W4A8 方案。
- **Benchmark** · LLaVA-onevision-7B 上的 TextVQA、OCRBench，测压缩率和延迟。
- **关键结果 / 消融** · 对应准确率提升 4.7% 和 7.7%；无损模块约 4% 端到端延迟开销。
- **适用条件 / 局限** · 收益取决于数据熵与 GPU 解码。

**可复用机制** · 量化校准同时记录重建误差、码长和真实延迟。

<a id="paper-153990"></a>

## CompactAttention: Accelerating Chunked Prefill with Block-Union KV Selection

[官方论文页](https://neurips.cc/virtual/2026/poster/153990) · [作者来源](https://openreview.net/forum?id=H2kz1bJFuL)

- **问题 / 瓶颈** · 分块预填充执行细粒度稀疏核或 KV 搬运成本高。
- **核心创新 / 方法** · 合并查询块和 GQA 组内掩码，原位读取最小覆盖块表。
- **Baseline** · 密集注意力及 QUOKA。
- **Benchmark** · LLaMA-3.1-8B-Instruct，RULER 和 128K 分块预填充。
- **关键结果 / 消融** · 接近密集准确率，注意力最高快 2.72 倍。
- **适用条件 / 局限** · 端到端加速和不同掩码的覆盖待核。

**可复用机制** · 若稀疏 kernel 不合适，保留选择信号并改用现有分页执行。

<a id="paper-152227"></a>

## Compact Representations of Impact-Based Fair-Ranking Policies

[官方论文页](https://neurips.cc/virtual/2026/poster/152227) · [作者来源](https://openreview.net/forum?id=Uc6X42DXPz)

- **问题 / 瓶颈** · 公平排序部署存储随用户规模增长。
- **核心创新 / 方法** · 证明每个最优解有至多物品数的保影响支撑，改用对偶表示并按权重子采样。
- **Baseline** · 用户绑定的混合排序。
- **Benchmark** · 真实推荐数据，测公平目标及部署存储。
- **关键结果 / 消融** · 报告保持目标且存储最多缩小 2596 倍。
- **适用条件 / 局限** · 适用所设 Nash 社会福利框架。

**可复用机制** · 先比较原策略与共享对偶表示，再在未见用户测公平目标。

<a id="paper-154865"></a>

## Compact SO(3) Equivariant Atomistic Foundation Models via Structural Pruning

[官方论文页](https://neurips.cc/virtual/2026/poster/154865) · [作者来源](https://openreview.net/forum?id=AJ8IWO0noE)

- **问题 / 瓶颈** · 原子图网络高阶张量计算昂贵。
- **核心创新 / 方法** · 沿通道和表示阶数移除整块以保留旋转等变。
- **Baseline** · 官方小型 MACE-MP 从头训练及任务专用从头训练。
- **Benchmark** · Matbench Discovery 和 8 个下游集；测能量、力和训练成本。
- **关键结果 / 消融** · Matbench 9 项中 7 项优于小模型；参数量少 1.5–4 倍。
- **适用条件 / 局限** · 裁剪收益依赖起始模型和任务。

**可复用机制** · 对有对称性约束的模型，比较按表示块剪枝与同大小从头训练。

<a id="paper-155667"></a>

## CompactSplat: Spatially Adaptive Gaussian Distribution for Feedforward Scene Reconstruction

[官方论文页](https://neurips.cc/virtual/2026/poster/155667) · [作者来源](https://openreview.net/forum?id=3sn6PeO6Ch)

- **问题 / 瓶颈** · 均匀原语分配浪费平坦区域存储。
- **核心创新 / 方法** · 纹理引导划分和层次采样，平面使用更大尺度原语。
- **Baseline** · 前馈三维高斯方案，具名对照待核。
- **Benchmark** · RealEstate10K、DL3DV、ScanNet，测渲染及原语数。
- **关键结果 / 消融** · 报告以更少原语取得较好质量并可推理时调节稀疏度。
- **适用条件 / 局限** · 超出所测视角和纹理情形待核。

**可复用机制** · 固定原语数量消融区域划分和尺度调节。

<a id="paper-153164"></a>

## Comparing Linear Regions in ReLU-Type Networks: Theory and Monte Carlo Methods

[官方论文页](https://neurips.cc/virtual/2026/poster/153164) · [作者来源](https://openreview.net/forum?id=NOrlEjE8dx)

- **问题 / 瓶颈** · 逐一区域计数难，参数量不直接反映分段复杂度。
- **核心创新 / 方法** · 刻画一般位置下激活模式与线性区关系，证明两层结果并做采样估计。
- **Baseline** · 两层均宽与前窄后宽配置。
- **Benchmark** · 随机全连接 ReLU 或 leaky ReLU，指标是线性区域数量。
- **关键结果 / 消融** · 报告靠输入层的神经元通常影响更大，并给出两层期望值。
- **适用条件 / 局限** · 区域数不直接等于泛化性能。

**可复用机制** · 选层宽时把几何复杂度与参数、任务精度分别报告。

<a id="paper-154270"></a>

## Comparing Transformers and Hybrid Models at the Token Level

[官方论文页](https://neurips.cc/virtual/2026/poster/154270) · [作者来源](https://openreview.net/forum?id=F41cmFncG0)

- **问题 / 瓶颈** · 总体损失无法分辨复制、句法和语义贡献。
- **核心创新 / 方法** · 按内容词、功能词、括号及重复 n-gram 切分 token 损失。
- **Baseline** · Olmo 3 与 Olmo Hybrid。
- **Benchmark** · 自然语言及代码，测逐 token 损失差。
- **关键结果 / 消融** · 优势集中内容词，在重复序列消失，闭括号上的差距缩小。
- **适用条件 / 局限** · 只测所给模型，状态优势属于解释假设。

**可复用机制** · 比较架构时用能力对应的 token 分桶代替单一困惑度。

<a id="paper-150292"></a>

## COMPASS: Composable Policy-Amortized Structured Search for LLM-Based Optimization Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/150292) · [作者来源](https://openreview.net/forum?id=jF68qSbugj)

- **问题 / 瓶颈** · 固定模板遍历无法吸收历史成败。
- **核心创新 / 方法** · 把模板 DAG 检索视为序贯决策，使用 DQN 学遍历，文本嵌入支持新增模板。
- **Baseline** · 启发式结构检索。
- **Benchmark** · 多个骨干及优化建模任务，测建模效果。
- **关键结果 / 消融** · 作者报告总体提升，复杂混合类别任务收益更大。
- **适用条件 / 局限** · 依赖执行反馈及模板覆盖。

**可复用机制** · 有可执行反馈的检索可对照可学习遍历与固定搜索。

<a id="paper-150283"></a>

## Compatible Likelihoods for Flow Matching on Manifolds

[官方论文页](https://neurips.cc/virtual/2026/poster/150283) · [作者来源](https://openreview.net/forum?id=jJsQucS0Fg)

- **问题 / 瓶颈** · 流形上的似然目标可能将样本推离数据。
- **核心创新 / 方法** · 构造兼容性判据，并用端点指数族把支持集限制在可实现速度。
- **Baseline** · 既有黎曼流匹配方法。
- **Benchmark** · 一维环面反例、高维积环面、四个球面地理数据集，测 NLL。
- **关键结果 / 消融** · 恢复反例正确速度，在四个球面集中的两个改善 NLL。
- **适用条件 / 局限** · 运行开销增加；速度方向分权形式取决于曲率。

**可复用机制** · 设计受限生成目标时同时验证支持集和人口极限下的优化方向。

<a id="paper-150873"></a>

## Competing Event Models: Next Event Prediction Under Interventions

[官方论文页](https://neurips.cc/virtual/2026/poster/150873) · [作者来源](https://openreview.net/forum?id=ekD79mlpR7)

- **问题 / 瓶颈** · 统一 next-token 分布难以单独修改未来事件时间。
- **核心创新 / 方法** · 以最早的独立潜在事件时间决定下一事件，考虑并发。
- **Baseline** · 标准 Transformer。
- **Benchmark** · 模拟时序干预与 MIMIC-IV 预测任务。
- **关键结果 / 消融** · 模拟可回收干预效应，真实数据 4 项中 3 项预测更好。
- **适用条件 / 局限** · 观察性预测不证明真实干预有效。

**可复用机制** · 需评估时间变更时，对照分类型时间模型和统一事件 token。

<a id="paper-153264"></a>

## CompilerKV: Risk-Adaptive KV Cache Compression via Offline Experience Compilation

[官方论文页](https://neurips.cc/virtual/2026/poster/153264) · [作者来源](https://openreview.net/forum?id=MYIR2frWUj)

- **问题 / 瓶颈** · 单条提示估计信噪比低，预填充后决策难撤回。
- **核心创新 / 方法** · 从校准语料编译保留表，在线查表并约束预算。
- **Baseline** · FullKV、SnapKV 和预填充压缩基线。
- **Benchmark** · 四个骨干的 LongBench、RULER、NIAH。
- **关键结果 / 消融** · 512 token 预算下较最强预填充对照平均高 1.67 分。
- **适用条件 / 局限** · 语料差异过大时迁移待核。

**可复用机制** · 对稳定的跨提示信号用离线估计，并在独立语料上测校准排序。

<a id="paper-148734"></a>

## CompJudge: Fine-Grained Comparative Evaluation using Multimodal LLM for Subject-Driven Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/148734) · [作者来源](https://openreview.net/forum?id=vRf7unujMa)

- **问题 / 瓶颈** · 逐图评分不能可靠区分身份细节错误。
- **核心创新 / 方法** · 比较保身份和失身份图像，再按比较结果调整打分。
- **Baseline** · 独立评分评估器和既有方法。
- **Benchmark** · CompILIAS 三元组及 DreamBench++。
- **关键结果 / 消融** · 报告分别改善 8.9 及 10.62–15.98 个百分点。
- **适用条件 / 局限** · 依赖三元组标签准确性，其他生成属性需另验。

**可复用机制** · 验证评审器时构造差异集中在目标属性的成对样本。

<a id="paper-151298"></a>

## Complementary Cache Guidance with Gradient Disentanglement for Continuous Test-Time Adaptation

[官方论文页](https://neurips.cc/virtual/2026/poster/151298) · [作者来源](https://openreview.net/forum?id=bU9thZFC6N)

- **问题 / 瓶颈** · 噪声伪标签和新旧目标冲突会积累。
- **核心创新 / 方法** · 投票改进伪标签，分别缓存近期可靠高熵和长期梯度一致样本，在短时信号零空间巩固历史。
- **Baseline** · 既有持续测试适配方法，具名待核。
- **Benchmark** · 多项视觉语言适配基准，具体指标待核。
- **关键结果 / 消融** · 作者报告优势，幅度与独立消融待核。
- **适用条件 / 局限** · 依赖伪标签质量和梯度低秩近似。

**可复用机制** · 遇到持续漂移时按时间尺度分开管理样本并消融梯度正交约束。

<a id="paper-151156"></a>

## Complementing DINO Features with Image Structure for Part Discovery

[官方论文页](https://neurips.cc/virtual/2026/poster/151156) · [作者来源](https://openreview.net/forum?id=cbLnr5GrNf)

- **问题 / 瓶颈** · 跨边界图块的混合特征降低部件分配置信度。
- **核心创新 / 方法** · 结合低层分割边界与 DINO 区域特征聚类。
- **Baseline** · 免训练方法及弱监督、无监督方法。
- **Benchmark** · CUB、CelebA、PartImageNet-OOD、PartImageNet-Seg。
- **关键结果 / 消融** · 超过 26K 图块分析发现边界图块更不确定；报告优于免训练对照。
- **适用条件 / 局限** · 依赖分割边界能刻画真实部件。

**可复用机制** · 评估发现模型时按是否跨边界分桶，并对照直接聚类和区域池化。

<a id="paper-155305"></a>

## Complete or Sparse: A Tale of Two Identifiabilities

[官方论文页](https://neurips.cc/virtual/2026/poster/155305) · [作者来源](https://openreview.net/forum?id=6Zf8KMxjD7)

- **问题 / 瓶颈** · 预测性能不保证恢复真实潜变量。
- **核心创新 / 方法** · 证明足够表征维数下线性恢复，并区分非负节能约束及具稀疏假设的恢复。
- **Baseline** · 完整和欠完整表示、生成与判别两类过程。
- **Benchmark** · 合成数据及视觉、语言模型和神经活动的数据分析。
- **关键结果 / 消融** · 维数不足时通常不可辨识，特定稀疏条件下仍可恢复单个潜变量。
- **适用条件 / 局限** · 理论取决于数据过程、稀疏性或非负条件。

**可复用机制** · 将线性混合与逐轴恢复分开验证，检查欠完整时是否满足恢复条件。

<a id="paper-138965"></a>

## CompleteRXN: Toward Completing Open Chemical Reaction Databases

[官方论文页](https://neurips.cc/virtual/2026/poster/138965) · [作者来源](https://openreview.net/forum?id=th8s60xMrD)

- **问题 / 瓶颈** · 高质量配对基准可能遗漏真实数据的缺失模式。
- **核心创新 / 方法** · 对不完整与完整记录配对，设置逐级困难划分并外测未策展样本。
- **Baseline** · 受约束编码解码器及 SynRBL。
- **Benchmark** · CompleteRXN 随机与分布外划分及未策展 USPTO。
- **关键结果 / 消融** · 随机和极端分布外等价准确率为 99.20% 和 91.12%，未策展记录进一步下降。
- **适用条件 / 局限** · 只评已有记录补全，数据规范会影响结果。

**可复用机制** · 补全基准同时报告按缺失程度分层的结果和未策展外测。

<a id="paper-155902"></a>

## Complexity Aware Continuous Level of Details for Gaussian Splatting

[官方论文页](https://neurips.cc/virtual/2026/poster/155902) · [作者来源](https://openreview.net/forum?id=1yzzKS5UI1)

- **问题 / 瓶颈** · 高斯集合截断后可能不均匀丢失细节。
- **核心创新 / 方法** · 复杂度引导训练期间重定位和推理保留，并限制全量与截断渲染的误差方差。
- **Baseline** · 基于 3DGS-MCMC；具名对照待核。
- **Benchmark** · 多预算渲染质量和退化曲线，具体数据待核。
- **关键结果 / 消融** · 报告退化更平滑，低预算收益更大。
- **适用条件 / 局限** · 复杂度代理不一定对应感知质量。

**可复用机制** · 对需要可截断部署的表示，直接监督多预算渲染并绘制质量曲线。

<a id="paper-151019"></a>

## Complexity-Aware LoRA Aggregation for Modality-Heterogeneous Federated Person Re-identification

[官方论文页](https://neurips.cc/virtual/2026/poster/151019) · [作者来源](https://openreview.net/forum?id=dZItc1V1aV)

- **问题 / 瓶颈** · 均匀聚合会淹没不同模态的检索模式
- **核心创新 / 方法** · 按模态保留共享秩和关键秩，并剪除冲突适配分量
- **Baseline** · 均匀聚合与全模型传输
- **Benchmark** · 可见光、红外和文本跨模态检索
- **关键结果 / 消融** · 报告优于已有方法，幅度待核
- **适用条件 / 局限** · 依赖复杂度估计

**可复用机制** · 异构联邦模型聚合时分别计量共享和私有适配方向。

<a id="paper-148201"></a>

## Complexity-guided Regularization for Generalizable Human Gaussian Splatting

[官方论文页](https://neurips.cc/virtual/2026/poster/148201) · [作者来源](https://openreview.net/forum?id=zbm9QnDqWY)

- **问题 / 瓶颈** · 复杂区域高斯过疏导致模糊
- **核心创新 / 方法** · 用局部几何和纹理熵约束密度并选择训练图块
- **Baseline** · 现有可泛化高斯泼溅方法
- **Benchmark** · 未见人物的新视图合成
- **关键结果 / 消融** · 报告细节改善并保持实时推理
- **适用条件 / 局限** · 基准名和速度待核

**可复用机制** · 把同一局部复杂度先验同时用于资源和监督分配。

<a id="paper-153053"></a>

## Complexity of Classical Acceleration for $\ell_1$-Regularized PageRank

[官方论文页](https://neurips.cc/virtual/2026/poster/153053) · [作者来源](https://openreview.net/forum?id=OO2ZfxkCzc)

- **问题 / 瓶颈** · FISTA 会临时激活最优解支持集之外的节点
- **核心创新 / 方法** · 在可检验边界约束下拆分加速核心项和边界开销
- **Baseline** · ISTA
- **Benchmark** · 真实和合成图的度数加权工作量
- **关键结果 / 消融** · 核心项可改善对传送参数的依赖，边界项可抵消收益
- **适用条件 / 局限** · 依赖约束条件与边界体积

**可复用机制** · 稀疏算法对照应计入中间迭代支持集扩张。

<a id="paper-153126"></a>

## Complexity of Differentially Private Selection via Federated APIs

[官方论文页](https://neurips.cc/virtual/2026/poster/153126) · [作者来源](https://openreview.net/forum?id=NjjTjmwMry)

- **问题 / 瓶颈** · 标准加噪聚合的选优有维度相关样本下界
- **核心创新 / 方法** · 加入稀疏向量技术接口并设计隐私选择算法
- **Baseline** · 标准聚合、洗牌与中央模型的理论界
- **Benchmark** · 私有选优和扩展估计任务
- **关键结果 / 消融** · 加性误差达到中央级对数维度数量级
- **适用条件 / 局限** · 需满足相应信任和隐私约束

**可复用机制** · 从接口表达能力定位分布式隐私任务瓶颈。

<a id="paper-155127"></a>

## Complex Optimization Modeling via Multiagent Fine-Tuning and Skill-Augmented Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/155127) · [作者来源](https://openreview.net/forum?id=8DDcXg3IK4)

- **问题 / 瓶颈** · 仅验收最终优化模型难定位中间角色的错误
- **核心创新 / 方法** · 拆分变量、约束等六步，用反事实分信用并在推理时提供角色技能
- **Baseline** · 已有方法及前沿语言模型
- **Benchmark** · 简单和复杂运筹建模任务
- **关键结果 / 消融** · 报告平均准确率改善，细项待核
- **适用条件 / 局限** · 需要可评判轨迹和领域技能

**可复用机制** · 固定终局验收后检查反事实过程信用是否改善复杂约束生成。

<a id="paper-153202"></a>

## Complex Schrödinger Bridges

[官方论文页](https://neurips.cc/virtual/2026/poster/153202) · [作者来源](https://openreview.net/forum?id=N4hE0Zplt1)

- **问题 / 瓶颈** · 无结构扩散桥的优化空间过大
- **核心创新 / 方法** · 复值 Schrödinger 桥加入哈密顿先验，图像变体有螺旋解析后验
- **Baseline** · 常规扩散桥，具名对照待核
- **Benchmark** · 物理及图像转换实验
- **关键结果 / 消融** · 作者验证理论和可用性，数值待核
- **适用条件 / 局限** · 几何先验与数据须适配

**可复用机制** · 在物理结构已知时比较结构化动力学和自由桥接。

<a id="paper-155547"></a>

## COMPLLLM: Fine-tuning LLMs to Discover Complementary Signals for Decision-making

[官方论文页](https://neurips.cc/virtual/2026/poster/155547) · [作者来源](https://openreview.net/forum?id=4kMncKrhE7)

- **问题 / 瓶颈** · 额外代理可能复述既有判断
- **核心创新 / 方法** · 用决策理论刻画相对于已有代理的互补信号并用作训练奖励
- **Baseline** · 单代理或未训练互补信号的流程
- **Benchmark** · 合成和专家参与的受控任务
- **关键结果 / 消融** · 报告找回已知互补信息且改善人和模型决策
- **适用条件 / 局限** · 依赖被辅助决策者及其信息

**可复用机制** · 在固定协作预算下分别比较信号正确性和相对已有决策的增量。

<a id="paper-148274"></a>

## Component-Based Out-of-Distribution Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/148274) · [作者来源](https://openreview.net/forum?id=z4SLzKzu0y)

- **问题 / 瓶颈** · 全图分数压低局部异常，图块分数易受噪声干扰
- **核心创新 / 方法** · 分成功能组件并分别给外观变化及跨组件关系打分
- **Baseline** · 全局和图块级检测方法
- **Benchmark** · 粗粒度与细粒度分布外检测
- **关键结果 / 消融** · 报告一致改善，幅度待核
- **适用条件 / 局限** · 依赖组件分解质量

**可复用机制** · 加入合法部件组合非法的单独评测。

<a id="paper-139605"></a>

## Composable Causality: A Toolkit for Systematic Time-Series Causal Discovery and Treatment-Effect Benchmarking

[官方论文页](https://neurips.cc/virtual/2026/poster/139605) · [作者来源](https://openreview.net/forum?id=FtoixLI4AT)

- **问题 / 瓶颈** · 固定数据集难分辨方法失败的主要因素
- **核心创新 / 方法** · 独立组合拓扑、噪声、缺失和干预，并复用随机实现生成成对反事实
- **Baseline** · 八种发现算法和四种效应估计器
- **Benchmark** · 81 种发现设置与18种效应估计设置
- **关键结果 / 消融** · 发现算法在多类缺失机制下均表现困难
- **适用条件 / 局限** · 证据来自构造分布

**可复用机制** · 用共享随机噪声生成干预对照，同时控制其他因素。

<a id="paper-151315"></a>

## COMPOSE: Composing Future Theorems from Citations and Formal Structure

[官方论文页](https://neurips.cc/virtual/2026/poster/151315) · [作者来源](https://openreview.net/forum?id=bOwtAJACqh)

- **问题 / 瓶颈** · 仅一种上下文无法兼顾研究动机和结构
- **核心创新 / 方法** · 用科学引用图及形式定理依赖图共同条件化
- **Baseline** · 已有检索和生成方法
- **Benchmark** · 108K 图配对与47K 后续论文，含检索和模型评判
- **关键结果 / 消融** · 报告双图表现更好
- **适用条件 / 局限** · 评判与检索不验证定理成立

**可复用机制** · 分别消融两种图，并将形式验证与相关性评分分开。

<a id="paper-150956"></a>

## COMPOSE: Hypergraph Cover Optimization for Multi-view 3D Human Pose Estimation

[官方论文页](https://neurips.cc/virtual/2026/poster/150956) · [作者来源](https://openreview.net/forum?id=e20UHiy3l3)

- **问题 / 瓶颈** · 遮挡导致局部合理的二元匹配无法全局兼容
- **核心创新 / 方法** · 把候选人体转为超图加权精确覆盖，以几何剪枝配整数规划或信念传播
- **Baseline** · 优化式及自监督方法
- **Benchmark** · 多视角三维人体姿态平均精度
- **关键结果 / 消融** · 最高分别提高31点和13点
- **适用条件 / 局限** · 依赖相机及二维检测质量

**可复用机制** · 跨多视角关联可直接优化全局一致的人体候选。

<a id="paper-151739"></a>

## ComPose: When to Trust Hands for Object Pose Tracking

[官方论文页](https://neurips.cc/virtual/2026/poster/151739) · [作者来源](https://openreview.net/forum?id=YSQd5SPRwo)

- **问题 / 瓶颈** · 只把手当成遮挡会浪费物体运动线索
- **核心创新 / 方法** · 筛选手关节并融合物体和手部旋转，再以可见几何校正平移
- **Baseline** · 依赖深度、模板或显式遮挡掩码的方案
- **Benchmark** · RGB 视频六自由度物体跟踪及下游操作
- **关键结果 / 消融** · 报告遮挡鲁棒性与动作迁移，数值待核
- **适用条件 / 局限** · 手物运动解耦时须抑制手部线索

**可复用机制** · 在遮挡分层评测中对照手部融合与仅用可见物体证据。

<a id="paper-149600"></a>

## Compose Your Oracles: Off Policy Improvement with Aggregated Guidance

[官方论文页](https://neurips.cc/virtual/2026/poster/149600) · [作者来源](https://openreview.net/forum?id=ou8C3NZhp9)

- **问题 / 瓶颈** · 在线多专家方法要频繁采新轨迹
- **核心创新 / 方法** · 将学习者并入专家池，用来源感知 critic 选动作并做离策略更新
- **Baseline** · 多专家引导及代表性离策略方法
- **Benchmark** · MetaWorld、DMC 和 Box2D
- **关键结果 / 消融** · 报告稀疏奖励和互补专家情形收益更强
- **适用条件 / 局限** · 专家同质或价值估计偏差会削弱效果

**可复用机制** · 先量化专家互补性，再决定是否训练来源专用价值。

<a id="paper-152144"></a>

## Composing Diffusion Priors with Explicit Physical Context via Generative Gibbs Sampling

[官方论文页](https://neurips.cc/virtual/2026/poster/152144) · [作者来源](https://openreview.net/forum?id=VBX4P5bFbr)

- **问题 / 瓶颈** · 训练先验可能没有覆盖任务条件下的耦合
- **核心创新 / 方法** · 构造扩展状态联合目标并用 Gibbs 更新，扩散时间副本交换改善混合
- **Baseline** · 预训练局部先验
- **Benchmark** · 双阱与 φ⁴ 格点等非生物物理系统
- **关键结果 / 消融** · 给出零扩散时间极限和二次相互作用的精确性结果
- **适用条件 / 局限** · 有限时间精确性条件有限

**可复用机制** · 物理任务改变时复用子系统先验并独立验证耦合目标。

<a id="paper-152239"></a>

## Compositional Generalization Certificates via the Van Kampen Theorem

[官方论文页](https://neurips.cc/virtual/2026/poster/152239) · [作者来源](https://openreview.net/forum?id=UXne8kTqvm)

- **问题 / 瓶颈** · 局部准确无法保证跨模块组合正确
- **核心创新 / 方法** · 以交叠表示空间的连通分支构建分层证书
- **Baseline** · 组内准确率及正确分支的理论对照
- **Benchmark** · 四元数群乘法及中央循环交叠
- **关键结果 / 消融** · 证明错误分支存在不可消除的预测间隙
- **适用条件 / 局限** · 结论依赖指定群和表示设定

**可复用机制** · 除单模块验收外，对交叠状态对齐及跨模块组合作单独压力测试。

<a id="paper-149110"></a>

## Compositional Policy Optimization with Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149110) · [作者来源](https://openreview.net/forum?id=so8irbBgTF)

- **问题 / 瓶颈** · 奖励和终止阈值难在单个子任务中预先定好
- **核心创新 / 方法** · 语言模型生成子任务定义，训练参数条件策略并在下游训练中选值
- **Baseline** · 固定预定义技能和阈值方法
- **Benchmark** · 机器人操作的任务组合与复用
- **关键结果 / 消融** · 报告能复用技能解决多类操作
- **适用条件 / 局限** · 依赖奖励可验证及技能覆盖

**可复用机制** · 推迟决定局部阈值，以后续技能可接续性作为选择标准。

<a id="paper-155613"></a>

## Compositional Reasoning in Language Models under Reinforcement Learning Post-Training

[官方论文页](https://neurips.cc/virtual/2026/poster/155613) · [作者来源](https://openreview.net/forum?id=4ElMzrtekX)

- **问题 / 瓶颈** · 单项技能高分可能掩盖组合失败
- **核心创新 / 方法** · 以依赖图定义三层组合并逐方向测迁移
- **Baseline** · 组件技能训练与完整组合训练
- **Benchmark** · 可验数据结构题及工具调用试点
- **关键结果 / 消融** · 组件到组合迁移较弱，反向更容易
- **适用条件 / 局限** · 真实工具证据仅试点

**可复用机制** · 按组合结构组织可验证任务并分开检查长度和结构外推。

<a id="paper-151682"></a>

## Compositional Training-Free Diffusion Planning for Long-Horizon Multiple Reach-Avoid Tasks

[官方论文页](https://neurips.cc/virtual/2026/poster/151682) · [作者来源](https://openreview.net/forum?id=YoWrqWunYY)

- **问题 / 瓶颈** · 长程计划的有序约束难用全局单目标表示
- **核心创新 / 方法** · 用因子图组合重叠轨迹段，在去噪时投影至局部要求
- **Baseline** · 引导式扩散规划
- **Benchmark** · 长程有序目标和约束规划
- **关键结果 / 消融** · 报告更快并给出拼接正确性保证
- **适用条件 / 局限** · 依赖局部约束与共享段一致性

**可复用机制** · 复用短程先验时将拼接边界也纳入可行性验收。

<a id="paper-148886"></a>

## Composition-RL: Compose Your Verifiable Prompts for Reinforcement Learning of Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148886) · [作者来源](https://openreview.net/forum?id=uSnERGG6v9)

- **问题 / 瓶颈** · 全通过的题随训练增加并减少有效反馈
- **核心创新 / 方法** · 将多个问题合成为可验提示，并递增组合深度
- **Baseline** · 用原数据训练的 RL
- **Benchmark** · 4B 至30B 模型的推理与跨域组合
- **关键结果 / 消融** · 报告持续改善，课程可进一步提升
- **适用条件 / 局限** · 依赖组合后仍可自动验收

**可复用机制** · 把已掌握样本转化为组合练习而不是直接丢弃。

<a id="paper-150918"></a>

## COMPOT: Calibration-Optimized Matrix Procrustes Orthogonalization for Transformers Compression

[官方论文页](https://neurips.cc/virtual/2026/poster/150918) · [作者来源](https://openreview.net/forum?id=eOWznbUyhS)

- **问题 / 瓶颈** · 单一低秩子空间可能过度损害中等压缩下的质量
- **核心创新 / 方法** · 校准稀疏权重分解，用闭式 Procrustes 更新并一次分配层间压缩率
- **Baseline** · 强低秩及稀疏压缩对照
- **Benchmark** · 多架构和任务的质量与压缩率
- **关键结果 / 消融** · 报告质量压缩折衷更优并可接量化
- **适用条件 / 局限** · 依赖校准数据和部署内核

**可复用机制** · 把多子空间表示与敏感度预算分配分别消融。

<a id="paper-154300"></a>

## Compressible Representations: Functional Spines in Deep Neural Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/154300) · [作者来源](https://openreview.net/forum?id=El13WPr9FG)

- **问题 / 瓶颈** · 方差不代表任务贡献
- **核心创新 / 方法** · 以隐藏表示的类 Fisher 矩阵排序并投影
- **Baseline** · 保方差、局部邻域及全局拓扑的投影
- **Benchmark** · 预训练视觉模型的维数与任务表现
- **关键结果 / 消融** · 作者报告较小子空间即可保留多数表现，常少于几何对照
- **适用条件 / 局限** · 任务与下游头改变后需重估

**可复用机制** · 固定维数比较功能投影和几何投影

<a id="paper-150720"></a>

## Compressing Collections of Trees with Decision Equivalence

[官方论文页](https://neurips.cc/virtual/2026/poster/150720) · [作者来源](https://openreview.net/forum?id=fwHieiqwl7)

- **问题 / 瓶颈** · 不同树可实现同一边界
- **核心创新 / 方法** · 寻找每个边界的稀疏等价树并保留代表
- **Baseline** · 原始树集合
- **Benchmark** · 二元叶决策树、集成和近最优模型集
- **关键结果 / 消融** · 给出等价去重及化简方法；摘要细节待核
- **适用条件 / 局限** · 适用二元叶；集成成员权重须另行处理

**可复用机制** · 统计模型多样性前按预测函数而非树形计数

<a id="paper-150194"></a>

## Computational Depth Predicts Quantization Sensitivity in Multimodal Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150194) · [作者来源](https://openreview.net/forum?id=k2VA2TJFFL)

- **问题 / 瓶颈** · 量化损失因任务而异
- **核心创新 / 方法** · 以逐步保真率的幂次建模随精度依赖步骤的退化
- **Baseline** · 不同任务深度与架构
- **Benchmark** · 四类 VLM 家族及图像和视频理解与生成
- **关键结果 / 消融** · 作者报告浅探针可预测留出架构的退化排序
- **适用条件 / 局限** · 深度度量与架构相关

**可复用机制** · 分别按推理步骤、去噪步数或时序链长度测量退化

<a id="paper-153891"></a>

## Computational Dynamic Mechanism Design

[官方论文页](https://neurips.cc/virtual/2026/poster/153891) · [作者来源](https://openreview.net/forum?id=HyFDGQQC6q)

- **问题 / 瓶颈** · 历史相关的偏离难解析
- **核心创新 / 方法** · 将单方偏离建模为参数化 POMDP，以随机自然策略梯度求解
- **Baseline** · 直接机制及单方偏离校验
- **Benchmark** · 参数化动态机制的有限样本与收敛分析
- **关键结果 / 消融** · 给出近似驻点优化保证
- **适用条件 / 局限** · 依赖模型和求解误差条件

**可复用机制** · 用最优偏离的近似 oracle 约束设计者更新

<a id="paper-150028"></a>

## Computationally Efficient Replicable Learning of Parities and Applications

[官方论文页](https://neurips.cc/virtual/2026/poster/150028) · [作者来源](https://openreview.net/forum?id=lJzvyZGkHM)

- **问题 / 瓶颈** · 以往高效可复现方法适用范围有限
- **核心创新 / 方法** · 构造任意分布下可实现奇偶函数的高效可复现 PAC 学习
- **Baseline** · 统计查询学习和差分隐私学习
- **Benchmark** · 理论奇偶学习，任意输入分布
- **关键结果 / 消融** · 作者给出首个高效可复现算法
- **适用条件 / 局限** · 可实现设定，非任意噪声模型

**可复用机制** · 比较稳定性定义时把运行时间和分布假设列入对照

<a id="paper-155651"></a>

## Computationally sufficient statistics for Ising models

[官方论文页](https://neurips.cc/virtual/2026/poster/155651) · [作者来源](https://openreview.net/forum?id=41qmmeIDx9)

- **问题 / 瓶颈** · 完整样本可能不可获取
- **核心创新 / 方法** · 分析有限阶联合统计与模型宽度的恢复关系
- **Baseline** · 完整配置学习与经典充分统计方法
- **Benchmark** · Ising 参数恢复的理论设定
- **关键结果 / 消融** · 摘要给出有限统计下可行的恢复结果
- **适用条件 / 局限** · 依赖模型宽度及足够精确的统计量

**可复用机制** · 采集不可完整观察的系统时先核对可辨识的统计阶数

<a id="paper-153933"></a>

## Compute Aligned Training: Optimizing for Test Time Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/153933) · [作者来源](https://openreview.net/forum?id=HUYwkuQIwd)

- **问题 / 瓶颈** · 单样本目标与测试时多样本筛选不一致
- **核心创新 / 方法** · 将推理策略写成基策略算子，为监督和强化学习推导目标
- **Baseline** · 标准 SFT 与 RL
- **Benchmark** · 不同测试时策略下的推理扩展
- **关键结果 / 消融** · 作者报告扩展效果改善；具体幅度待核
- **适用条件 / 局限** · 切换推理策略可能需要更换训练目标

**可复用机制** · 在相同采样预算下比较单样本训练和聚合感知训练

<a id="paper-152439"></a>

## Compute Allocation Under Model-Provider Competition

[官方论文页](https://neurips.cc/virtual/2026/poster/152439) · [作者来源](https://openreview.net/forum?id=T7wtHK2EEc)

- **问题 / 瓶颈** · 训练收益与服务容量受竞争反馈共同影响
- **核心创新 / 方法** · 两供应商在准确率和延迟间分配预算并分析均衡
- **Baseline** · 资源对称竞争
- **Benchmark** · 两供应商和按准确率延迟选择的用户群
- **关键结果 / 消融** · 模型中低预算方可借拥塞吸引用户
- **适用条件 / 局限** · 简化博弈，真实负载待验证

**可复用机制** · 比较算力策略时以内生需求代替固定流量假设

<a id="paper-148716"></a>

## Compute Efficiency and Serial Runtime Tradeoffs for Stochastic Momentum Methods

[官方论文页](https://neurips.cc/virtual/2026/poster/148716) · [作者来源](https://openreview.net/forum?id=vZu4zXa0PZ)

- **问题 / 瓶颈** · 大批量减少步数未必节省计算
- **核心创新 / 方法** · 在高斯协变量线性回归中推导动量的批量折衷下界
- **Baseline** · SGD、重球和加速 SGD
- **Benchmark** · 一致线性回归、离散有限维分析
- **关键结果 / 消融** · 重球可扩大高效批量窗口，但任意谱下未改善 SGD 计算前沿
- **适用条件 / 局限** · 结论限给定模型与谱设定

**可复用机制** · 在配平梯度查询次数后再比较动量速度

<a id="paper-151246"></a>

## Compute-optimal data scaling for neural surrogates via multi-fidelity training

[官方论文页](https://neurips.cc/virtual/2026/poster/151246) · [作者来源](https://openreview.net/forum?id=boIBg7GaQo)

- **问题 / 瓶颈** · 高精度仿真可能成为训练数据瓶颈
- **核心创新 / 方法** · 以固定数据生成算力优化连续层级的离散保真度配比
- **Baseline** · 单保真度数据配置
- **Benchmark** · PDE 神经代理的误差与仿真开销
- **关键结果 / 消融** · 作者报告多保真配置可达 Pareto 最优缩放
- **适用条件 / 局限** · 依赖数值误差与成本规律

**可复用机制** · 固定求解器预算扫描样本数、分辨率和混合比例

<a id="paper-152040"></a>

## Compute-Optimal Pretrain--Fine-tune in Ridge Gradient Flow

[官方论文页](https://neurips.cc/virtual/2026/poster/152040) · [作者来源](https://openreview.net/forum?id=VzaMH1nM2t)

- **问题 / 瓶颈** · 上游训练消耗适配时间
- **核心创新 / 方法** · 用岭最小二乘梯度流分析固定总时间的两阶段分配
- **Baseline** · 不同切换时刻
- **Benchmark** · 理论两阶段线性模型
- **关键结果 / 消融** · 最优分配取决于上游方向对下游预测的影响
- **适用条件 / 局限** · 结论限线性梯度流及相应假设

**可复用机制** · 用下游预测误差而非上游损失决定是否切换

<a id="paper-140060"></a>

## Computer Science Conferences Should Require Nonrepudiable Experimental Results

[官方论文页](https://neurips.cc/virtual/2026/poster/140060) · [作者来源](https://openreview.net/forum?id=UK7onMx1HA)

- **问题 / 瓶颈** · 作者控制日志不能独立证明数值来源
- **核心创新 / 方法** · 提出运行证明框架及 K-Veritas 参考实现
- **Baseline** · 自报清单、可选代码和普通日志
- **Benchmark** · 实验可追溯性及参考实现
- **关键结果 / 消融** · 作者报告构建了参考实现；开销细节待核
- **适用条件 / 局限** · 证明执行出处不等同证明实验有效

**可复用机制** · 独立验收执行来源和统计设计

<a id="paper-151946"></a>

## Computer Use at the Edge of the Statistical Precipice

[官方论文页](https://neurips.cc/virtual/2026/poster/151946) · [作者来源](https://openreview.net/forum?id=We2oXEmu4W)

- **问题 / 瓶颈** · 固定任务可能把动作记忆误计为观察能力
- **核心创新 / 方法** · 比较固定轨迹基线及确定性环境中的成功率估计，提出环境评测原则
- **Baseline** · 前沿 CUA 与不观测的基线
- **Benchmark** · 静态交互评测及确定性环境推导
- **关键结果 / 消融** · 作者发现无观察基线可超过部分模型
- **适用条件 / 局限** · 结论依赖环境确定性，避免泛化到所有界面

**可复用机制** · 将任务状态随机化并独立验证结果

<a id="paper-155133"></a>

## Computing All Optimal Partial $p$-Wasserstein Matchings on the Line

[官方论文页](https://neurips.cc/virtual/2026/poster/155133) · [作者来源](https://openreview.net/forum?id=88SUwJD17z)

- **问题 / 瓶颈** · 部分匹配比完整有序匹配复杂
- **核心创新 / 方法** · 用快速傅里叶变换组织平衡区间的转移计算
- **Baseline** · 一维完整匹配和已知 p=1 方法
- **Benchmark** · 均匀原子的一维部分 p-Wasserstein 匹配
- **关键结果 / 消融** · 给出面向 p>1 的算法结构；复杂度细节待核
- **适用条件 / 局限** · 限制一维及质量设定

**可复用机制** · 先检查是否可把部分匹配分解为重复区间子问题

<a id="paper-150647"></a>

## Computing Thiele Rules on Interval Elections and their Generalizations

[官方论文页](https://neurips.cc/virtual/2026/poster/150647) · [作者来源](https://openreview.net/forum?id=gUna8QDjeT)

- **问题 / 瓶颈** · 候选区间上的全幺模线性规划不能直接沿用
- **核心创新 / 方法** · 分析选民区间上的 Thiele 规则复杂度
- **Baseline** · 一般困难情形以及候选区间 LP
- **Benchmark** · 赞成票委员会选择的结构化偏好
- **关键结果 / 消融** · 作者解决选民区间的复杂度问题；精确定理待核
- **适用条件 / 局限** · 依赖区间结构

**可复用机制** · 实现规则前区分区间属性施加在哪一侧

<a id="paper-154350"></a>

## Concentrated Gradients Amplify Forgetting: Dominant-direction Projection for Continual Multimodal Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/154350) · [作者来源](https://openreview.net/forum?id=EF8TL6jlfw)

- **问题 / 瓶颈** · 集中更新会放大任务间干扰
- **核心创新 / 方法** · 分析 LoRA Fisher 敏感度与更新集中度，并投影近期梯度的主方向
- **Baseline** · 共享参数敏感度的分析和持续学习对照
- **Benchmark** · 多模态持续指令微调
- **关键结果 / 消融** · 作者将遗忘与共享高敏感参数上的更新集中联系起来
- **适用条件 / 局限** · 依赖 LoRA 设置和方向估计

**可复用机制** · 同时记录参数共享与更新集中度，比较等预算投影

<a id="paper-149192"></a>

## Concept-Aware Wasserstein Routing with Vision-Language Guidance for Few-Shot WSI Classification

[官方论文页](https://neurips.cc/virtual/2026/poster/149192) · [作者来源](https://openreview.net/forum?id=sClFLiex6B)

- **问题 / 瓶颈** · 单一类原型难覆盖切片内异质性
- **核心创新 / 方法** · 用非平衡最优传输对齐图块与概念，再用语义邻接和原型记忆聚合
- **Baseline** · 依赖单类锚点的视觉语言多实例分类
- **Benchmark** · 少样本全切片分类
- **关键结果 / 消融** · 作者提出联合框架；具体效果及分项待核
- **适用条件 / 局限** · 依赖冻结病理骨干与可用的概念描述

**可复用机制** · 固定图块编码，比较单原型与多概念路由

<a id="paper-149108"></a>

## Concept frustration: Aligning human concepts and machine representations

[官方论文页](https://neurips.cc/virtual/2026/poster/149108) · [作者来源](https://openreview.net/forum?id=sq7mf1Xca5)

- **问题 / 瓶颈** · 欧氏比较可能漏掉未知概念改变的关系
- **核心创新 / 方法** · 定义概念挫折，引入任务对齐相似度并在线性高斯模型中分解预测信号
- **Baseline** · 欧氏几何比较
- **Benchmark** · 监督人类概念与无监督模型表示的理论比较
- **关键结果 / 消融** · 理论显示任务对齐几何可识别该不一致
- **适用条件 / 局限** · 解析结论限具体生成模型

**可复用机制** · 以真实任务为参照判断本体是否漏掉潜变量

<a id="paper-150809"></a>

## Concept-Localized Generative Representations

[官方论文页](https://neurips.cc/virtual/2026/poster/150809) · [作者来源](https://openreview.net/forum?id=fDLPVya86p)

- **问题 / 瓶颈** · 重建准确不能保证概念局部化
- **核心创新 / 方法** · 用概念信息瓶颈上界促进集中编码并降低两潜变量依赖
- **Baseline** · 重建或预测目标，具名对照待核
- **Benchmark** · 合成与真实数据以及神经响应案例
- **关键结果 / 消融** · 摘要报告概念集中且生成保真，神经响应结构对齐更强
- **适用条件 / 局限** · 依赖概念监督的定义；指标待核

**可复用机制** · 将概念泄漏和重建误差作为独立指标

<a id="paper-153542"></a>

## Concept Modulation Models: A Unified Framework for Identifiability and Extrapolation

[官方论文页](https://neurips.cc/virtual/2026/poster/153542) · [作者来源](https://openreview.net/forum?id=KanpVVPIzD)

- **问题 / 瓶颈** · 条件生成的两种保证往往逐模型证明
- **核心创新 / 方法** · 用属性条件概念分布的对数密度比表达传输约束
- **Baseline** · 非线性 ICA 和因果表示中的既有分析
- **Benchmark** · 条件生成的理论设定
- **关键结果 / 消融** · 势函数恒等式延伸到新属性恰对应外推一致
- **适用条件 / 局限** · 仍需各模型自身的刚性论证

**可复用机制** · 先核对密度比恒等式能否延伸，再声称域外可识别

<a id="paper-151556"></a>

## Concepts in Motion: Temporal Concept Bottleneck Model for Interpretable Video Classification

[官方论文页](https://neurips.cc/virtual/2026/poster/151556) · [作者来源](https://openreview.net/forum?id=Zj6ihufW1x)

- **问题 / 瓶颈** · 全局概念无法描述动作先后和重复
- **核心创新 / 方法** · 按类从训练视频发现对象及动作概念，再对每个概念做时序注意力
- **Baseline** · 全局概念瓶颈及黑盒视频模型
- **Benchmark** · 多个视频分类基准，名称待核
- **关键结果 / 消融** · 摘要报告优于全局瓶颈并缩小和黑盒的差距
- **适用条件 / 局限** · 依赖视觉语言模型的逐时概念质量

**可复用机制** · 保持概念词表固定，对照平池化与逐概念时序建模

<a id="paper-151925"></a>

## Concepts Worth Having: Refining VLM-Guided Concept Bottleneck Models with Minimal Annotations

[官方论文页](https://neurips.cc/virtual/2026/poster/151925) · [作者来源](https://openreview.net/forum?id=WqZrNqsrTI)

- **问题 / 瓶颈** · 纯自动概念标签误差削弱解释性
- **核心创新 / 方法** · 在视觉语言嵌入中用高斯过程传播专家监督
- **Baseline** · 纯视觉语言引导的概念瓶颈
- **Benchmark** · 四个数据集，测概念准确率与校准
- **关键结果 / 消融** · 只标注 1% 时作者仍报告概念改善
- **适用条件 / 局限** · 依赖嵌入几何与标注覆盖

**可复用机制** · 固定标注预算，对照随机传播、嵌入传播和纯伪标签

<a id="paper-152103"></a>

## Concise and Logically Consistent Conformal Sets for Neuro-Symbolic Concept-Based Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152103) · [作者来源](https://openreview.net/forum?id=VUpjicJHf4)

- **问题 / 瓶颈** · 分开校准可能得到不一致或过大的集合
- **核心创新 / 方法** · 后处理联合共形集合，以一次演绎和溯因修订协调
- **Baseline** · 既有共形方法和自然基线，名称待核
- **Benchmark** · 八个数据集，测表现与集合大小
- **关键结果 / 消融** · 作者报告满足覆盖、一致和简洁三个要求
- **适用条件 / 局限** · 保证须按原文前提理解；知识错误类型的影响待核

**可复用机制** · 对结构化预测同时验收覆盖率、逻辑冲突率和集合大小

<a id="paper-151507"></a>

## Concise Reasoning Through the Lens of Lagrangian Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/151507) · [作者来源](https://openreview.net/forum?id=a8ifmvW6IK)

- **问题 / 瓶颈** · 固定标量权重需随任务和模型重调
- **核心创新 / 方法** · 以可计算替代更新实现长度约束的拉格朗日过程
- **Baseline** · GRPO 与标量化压缩思路
- **Benchmark** · 六项基准并跨数学、逻辑和 STEM
- **关键结果 / 消融** · 1.5B 模型长度降 64%，准确率由 44.2% 到 51.6%
- **适用条件 / 局限** · 适用性受可验证奖励及准确率估计制约

**可复用机制** · 把压缩视为满足目标准确率后的预算优化

<a id="paper-155212"></a>

## Conclusions from Circuit Extraction Depend on the Level of Description: A Controlled Comparison

[官方论文页](https://neurips.cc/virtual/2026/poster/155212) · [作者来源](https://openreview.net/forum?id=7RfZ1ThE5z)

- **问题 / 瓶颈** · 保留行为的消融图可能并不唯一
- **核心创新 / 方法** · 固定证明任务，改变稀疏度、查询键拆分和损失预算比较提取图
- **Baseline** · 随机 top-k 与三种电路描述
- **Benchmark** · Lean 风格规则生成的策略预测任务
- **关键结果 / 消融** · 头级重叠高于随机，精确边未稳定高于随机
- **适用条件 / 局限** · 限特定架构与合成证明设置

**可复用机制** · 复核机制结论时报告跨抽取协议和描述层级的重叠

<a id="paper-150148"></a>

## Concorde: Geometry-Aware Link Prediction via Decoupled Energy Minimization

[官方论文页](https://neurips.cc/virtual/2026/poster/150148) · [作者来源](https://openreview.net/forum?id=kKn1kj1a7N)

- **问题 / 瓶颈** · 稀疏图缺少通路，耦合表示和扩散可能谱不稳
- **核心创新 / 方法** · 融合谱锚、混合曲率残差和非局部向量场，用排序损失训练
- **Baseline** · 主流链路预测对照，名称待核
- **Benchmark** · 五个稀疏及稠密图基准，测早期检索精度
- **关键结果 / 消融** · 摘要报告稀疏场景 P@10% 近乎翻倍
- **适用条件 / 局限** · 各分支独立收益和谱计算成本待核

**可复用机制** · 固定检索评测，单独比较稳定谱锚是否有助于曲率表示

<a id="paper-154365"></a>

## Concord-SLAM: Cross-Render Concordance for Boundary-Native Semantic Gaussian SLAM

[官方论文页](https://neurips.cc/virtual/2026/poster/154365) · [作者来源](https://openreview.net/forum?id=E76LuXwjD6)

- **问题 / 瓶颈** · 独立监督易造成边界混合和语义泄漏
- **核心创新 / 方法** · 联合优化跨渲染结构差异，在语义和几何间断附近添加高斯
- **Baseline** · 语义高斯 SLAM 对照，具名方法待核
- **Benchmark** · Replica 和 ScanNet，测跟踪、重建与语义建图
- **关键结果 / 消融** · 作者摘要报告三方面改善
- **适用条件 / 局限** · 敏感于边界信号质量；组件增益待核

**可复用机制** · 先利用跨输出分歧寻找薄弱区域，再比对均匀和边界增密

<a id="paper-153436"></a>

## Concurrence of Symmetry Breaking and Nonlocality Phase Transitions in Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153436) · [作者来源](https://openreview.net/forum?id=LJu0XmevDe)

- **问题 / 瓶颈** · 局部去噪失效和语义分岔是否同步不明
- **核心创新 / 方法** · 在扩散 Transformer 中测生成轨迹与结果，比较两类临界时间
- **Baseline** · 局部去噪与全局过程的诊断对照
- **Benchmark** · 现代扩散 Transformer，模型和指标待核
- **关键结果 / 消融** · 摘要报告两类临界时间近乎同时出现
- **适用条件 / 局限** · 相关性不等于普遍因果；不同采样器需复核

**可复用机制** · 分时段测局部近似误差，再决定哪些步值得用全局计算

<a id="paper-154281"></a>

## Concurrent Image Understanding and Generation: Self-Correcting Coupled Markov Jump Process

[官方论文页](https://neurips.cc/virtual/2026/poster/154281) · [作者来源](https://openreview.net/forum?id=EzyXXt9tbh)

- **问题 / 瓶颈** · 顺序解码或只交换上一步历史难以修复矛盾
- **核心创新 / 方法** · 以跨模态注意力加权置信度调节跃迁率，必要时重新掩码
- **Baseline** · 顺序或并行掩码解码，具名方法待核
- **Benchmark** · JEdit、JMaze、JNono 的同分布与分布外评测
- **关键结果 / 消融** · 摘要报告联合表现最佳且随去噪步数改善
- **适用条件 / 局限** · 依赖已有掩码扩散模型及置信度质量

**可复用机制** · 固定采步预算，消融同一步耦合与重新掩码

<a id="paper-149245"></a>

## CondenseVLA: Learnable History Condensation for Efficient Multi-Frame VLA

[官方论文页](https://neurips.cc/virtual/2026/poster/149245) · [作者来源](https://openreview.net/forum?id=rpyJNSOs0e)

- **问题 / 瓶颈** · 直接延长视觉窗口带来冗余和开销
- **核心创新 / 方法** · 交叉注意力用可学习查询压缩缓存帧，并惩罚槽注意重合及嵌入相关
- **Baseline** · 原始 VLA 与直接加帧设置
- **Benchmark** · Simpler-WidowX、LIBERO、真机操作
- **关键结果 / 消融** · Simpler 从 58.4% 到 70.8%，LIBERO 97.2%，真机 52.0%
- **适用条件 / 局限** · 适用于短时视觉证据；更长记忆和槽容量边界待核

**可复用机制** · 在固定动作头 token 预算下比较学习压缩和均匀采帧

<a id="paper-152006"></a>

## Conditional Counterfactual Mean Embeddings: Doubly Robust Estimation and Learning Rates

[官方论文页](https://neurips.cc/virtual/2026/poster/152006) · [作者来源](https://openreview.net/forum?id=WBrsTgkHw7)

- **问题 / 瓶颈** · 只预测均值会漏掉多峰等结构
- **核心创新 / 方法** · 将条件反事实分布嵌入 RKHS，使用两阶段双稳健估计并给出三种实现
- **Baseline** · 岭回归、深度特征与神经核三类估计，外部基线待核
- **Benchmark** · 条件反事实分布恢复，指标待核
- **关键结果 / 消融** · 作者给出有限样本速率并报告恢复多峰结构
- **适用条件 / 局限** · 仍依赖反事实识别和核选择条件

**可复用机制** · 用分布恢复指标补充平均效应，对照两类干扰模型误差

<a id="paper-153992"></a>

## Conditional Evaluation of Language Models with Cheap Auxiliary Signals

[官方论文页](https://neurips.cc/virtual/2026/poster/153992) · [作者来源](https://openreview.net/forum?id=H1oCdymbyt)

- **问题 / 瓶颈** · 总体准确率遮蔽局部结构，模型裁判也可能有偏
- **核心创新 / 方法** · 将辅助信号按区域中心化并作为岭控制变量，保留小批金标残差
- **Baseline** · 仅金标评估及其他对照，具名方法待核
- **Benchmark** · MATH-500、ScienceQA、MMLU-Pro、GPQA
- **关键结果 / 消融** · 作者证明分组无偏并用局部 R² 诊断收益
- **适用条件 / 局限** · 区域样本太少可能使中心化估计不稳

**可复用机制** · 根据金标试点测局部 R² 后决定是否增用廉价裁判

<a id="paper-153084"></a>

## Conditional independence and graphical models for rankings

[官方论文页](https://neurips.cc/virtual/2026/poster/153084) · [作者来源](https://openreview.net/forum?id=O6AIP8gDLa)

- **问题 / 瓶颈** · 互斥约束使普通排名变量难直接分解
- **核心创新 / 方法** · 以保序的结构化粗化定义相对排名并套用贝叶斯网
- **Baseline** · 两个既有排名模型作为特例
- **Benchmark** · 理论建模与推断；摘要未列实证基准
- **关键结果 / 消融** · 作者报告统一两类模型并支持可处理推断
- **适用条件 / 局限** · 依赖粗化与图结构的选择

**可复用机制** · 先确定需要保留的相对次序，再对粗化变量建因子分解

<a id="paper-151278"></a>

## Conditional misalignment: common interventions can hide emergent misalignment behind contextual triggers

[官方论文页](https://neurips.cc/virtual/2026/poster/151278) · [作者来源](https://openreview.net/forum?id=bZlqpkQW7o)

- **问题 / 瓶颈** · 标准评估改善可能掩盖不同语境中的失效
- **核心创新 / 方法** · 比较三个干预在标准和语境变化评估中的一致性
- **Baseline** · 已有三种缓解路线
- **Benchmark** · 标准与语境变化的安全评估，具体对照待核
- **关键结果 / 消融** · 作者发现标准评估通过后仍可能在其他语境失效
- **适用条件 / 局限** · 结果依赖训练与评估分布，摘要不足以外推

**可复用机制** · 验收后训练策略时进行覆盖不同语境的防御性回归测试

<a id="paper-139151"></a>

## Conditional Multi-Event Temporal Grounding in Long-Form Video

[官方论文页](https://neurips.cc/virtual/2026/poster/139151) · [作者来源](https://openreview.net/forum?id=i6iM7B1Koa)

- **问题 / 瓶颈** · 单片段定位无法识别漏报及空答案捷径
- **核心创新 / 方法** · 构造时空组合查询，加入拒答 F1 和无训练搜索聚合
- **Baseline** · 多模态模型、代理、专用定位方法及 GPT-5
- **Benchmark** · 600 部长视频 2789 条查询，测 F1@0.5 等
- **关键结果 / 消融** · 搜索聚合对 GPT-5 的 F1@0.5 提高 6.1%，单位待核
- **适用条件 / 局限** · 受任务构造与长视频领域覆盖限制

**可复用机制** · 在多事件评测中加入无匹配查询，同时报告拒答与事件级召回

<a id="paper-153803"></a>

## Conditional Optimal Bridge for Riemannian Activation Steering

[官方论文页](https://neurips.cc/virtual/2026/poster/153803) · [作者来源](https://openreview.net/forum?id=Ia9hqQHC34)

- **问题 / 瓶颈** · 固定激活方向可能使域外任务受损
- **核心创新 / 方法** · 在残差流球面建条件随机桥，以输入相关势得到动态方向
- **Baseline** · 既有激活引导方法
- **Benchmark** · 四个模型的有用性、真实性和去毒化评测
- **关键结果 / 消融** · 摘要报告改进并减轻域外退化
- **适用条件 / 局限** · 依赖参考激活分布和计算预算

**可复用机制** · 用相同预算比较固定方向和按输入调整的质量引导

<a id="paper-155789"></a>

## Conditioning Gaussian Processes on Almost Anything

[官方论文页](https://neurips.cc/virtual/2026/poster/155789) · [作者来源](https://openreview.net/forum?id=2tEtU2vxsj)

- **问题 / 瓶颈** · 线性高斯之外常需重新推导推断
- **核心创新 / 方法** · 将高斯过程等价为线性扩散，白化后用点似然驱动的蒙特卡洛引导
- **Baseline** · 标准共轭高斯过程条件化
- **Benchmark** · 线性高斯、非线性物理及语言条件案例
- **关键结果 / 消融** · 线性高斯情形精确恢复标准条件分布，其他场景为近似
- **适用条件 / 局限** · 依赖可计算点似然，近似方差与预算有关

**可复用机制** · 用可解共轭情形验算，再对新似然独立测采样开销和误差

<a id="paper-151261"></a>

## ConfDet: Learning Reliable Confidence for MLLM-based Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/151261) · [作者来源](https://openreview.net/forum?id=biptQ5O8Vh)

- **问题 / 瓶颈** · 生成概率及自评不直接反映框质量
- **核心创新 / 方法** · 监督学习离散分数 token，以联合奖励提高区分度，再做条件校准
- **Baseline** · 提示自评、生成概率及外部代理分数
- **Benchmark** · 分布内外检测，测 AP 和校准误差
- **关键结果 / 消融** · 作者报告排序改善提高 AP 并减轻失准
- **适用条件 / 局限** · 依赖质量标签的定义；跨域重新校准需求待核

**可复用机制** · 固定检测结果，分别测排序与概率校准以确定改进来自哪层

<a id="paper-151802"></a>

## Confidence-Based Decoding is Provably Efficient for Diffusion Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151802) · [作者来源](https://openreview.net/forum?id=XuU9i7BWKK)

- **问题 / 瓶颈** · 固定并行步长不能适应序列难度
- **核心创新 / 方法** · 按置信度解掩码并用熵和设定停止阈值
- **Baseline** · 理论对照序列长度决定的迭代成本
- **Benchmark** · 评估目标分布的 KL 误差与期望迭代数
- **关键结果 / 消融** · 迭代上界随目标分布熵增大、随容忍误差增大而下降
- **适用条件 / 局限** · 理论条件和实际模型误差待核

**可复用机制** · 对固定误差预算按序列熵比较解码步数

<a id="paper-148424"></a>

## Confidence Estimation via Decoupled Smoothing for Dynamic LLM Routing and Aggregation

[官方论文页](https://neurips.cc/virtual/2026/poster/148424) · [作者来源](https://openreview.net/forum?id=xvl4oRu74P)

- **问题 / 瓶颈** · 固定单模型限制效果而统一集成浪费计算
- **核心创新 / 方法** · 解耦特征并平滑局部性能，用置信分布选推理动作
- **Baseline** · 单模型路由与多模型聚合基线
- **Benchmark** · 两种设定下测平均准确率和计算预算
- **关键结果 / 消融** · 分别比最强对照提高 1.02% 和 1.36%
- **适用条件 / 局限** · 依赖用于置信校准的性能数据

**可复用机制** · 用同预算对比固定集成和按查询分配

<a id="paper-152508"></a>

## Conflict-Aware Logit Adapters for Utility-Preserving Anti-Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/152508) · [作者来源](https://openreview.net/forum?id=Sc1RFFLbFC)

- **问题 / 瓶颈** · 推理端保护可能增加延迟并损害流畅性
- **核心创新 / 方法** · 冻结教师并学习轻量适配器，在防模仿与教师效用之间做权衡
- **Baseline** · 解码干预和原教师
- **Benchmark** · 推理任务上的教师质量、学生模仿效果和额外开销
- **关键结果 / 消融** · 摘要报告模仿减少且教师效用近似保留
- **适用条件 / 局限** · 防护外推与代理学生依赖待核

**可复用机制** · 验收防护时并列记录效用、延迟和保护效果

<a id="paper-148415"></a>

## Conflict-Suppressed RAG: A Simple Decoding-Time Framework for Faithful Retrieval-Augmented Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/148415) · [作者来源](https://openreview.net/forum?id=y0Ra4QaGgR)

- **问题 / 瓶颈** · 检索到的证据仍可能被参数知识盖过
- **核心创新 / 方法** · 两个互补的分数处理器抑制参数信号并增强上下文信号
- **Baseline** · 其他忠实生成对照，具名待核
- **Benchmark** · 六个忠实性基准和多个骨干
- **关键结果 / 消融** · 作者报告达到或接近最佳表现，且无需训练
- **适用条件 / 局限** · 依赖检索证据可信，错误召回需单测

**可复用机制** · 用冲突与无冲突分组检验干预收益和误伤

<a id="paper-150722"></a>

## Conformal Agent Error Attribution

[官方论文页](https://neurips.cc/virtual/2026/poster/150722) · [作者来源](https://openreview.net/forum?id=fvwWOlglCS)

- **问题 / 瓶颈** · 点归因难覆盖长交互中的关键失误
- **核心创新 / 方法** · 用过滤序列上的共形预测构造连续区间
- **Baseline** · 传统共形集合与非连续归因
- **Benchmark** · 多种智能体轨迹，测覆盖、定位和回滚修复
- **关键结果 / 消融** · 作者报告有限样本覆盖并验证回滚修复
- **适用条件 / 局限** · 覆盖假设与标注代价待核

**可复用机制** · 对照单点诊断与区间诊断的恢复开销

<a id="paper-150311"></a>

## Conformal Cache: Reliable Proxy-Discrepancy Caching for Fast Generative Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/150311) · [作者来源](https://openreview.net/forum?id=j4jK1X7X8M)

- **问题 / 瓶颈** · 代理低估误差会导致错误复用
- **核心创新 / 方法** · 用拆分共形按时间步校准代理与真实偏差之间的上侧修正
- **Baseline** · 未经校准的代理缓存
- **Benchmark** · 图像与视频生成中的缓存复用与质量
- **关键结果 / 消融** · 作者报告改进可靠性，幅度待核
- **适用条件 / 局限** · 依赖校准集和真实偏差可计算

**可复用机制** · 固定质量阈值比较代理缓存与校准后的加速

<a id="paper-150795"></a>

## Conformal Language Modeling via Posterior Sampling

[官方论文页](https://neurips.cc/virtual/2026/poster/150795) · [作者来源](https://openreview.net/forum?id=fLpIG7hvGw)

- **问题 / 瓶颈** · 事后剔除声明可能损伤连贯性
- **核心创新 / 方法** · 以校准高分区域为条件，从近似后验采样
- **Baseline** · 事后过滤的共形生成
- **Benchmark** · 人物传记生成和数学求解，比较风险与效用
- **关键结果 / 消融** · 相同统计保证下报告更高效用
- **适用条件 / 局限** · 近似后验的代价及其他任务表现待核

**可复用机制** · 用匹配风险预算对照生成内约束与事后过滤

<a id="paper-155524"></a>

## Conformal Prediction for Distribution-to-Distribution Regression

[官方论文页](https://neurips.cc/virtual/2026/poster/155524) · [作者来源](https://openreview.net/forum?id=4xA4yCPjL5)

- **问题 / 瓶颈** · 直接共形集合可能无法解释体积或采样
- **核心创新 / 方法** · 构造基空间分数并给出渐近条件覆盖的自适应方案
- **Baseline** · 朴素拆分共形
- **Benchmark** · 合成及真实分布回归数据
- **关键结果 / 消融** · 保留有限样本覆盖并报告可解释性改善
- **适用条件 / 局限** · 依赖基表示与自适应条件

**可复用机制** · 覆盖、集合体积和采样可行性应同时验收

<a id="paper-150920"></a>

## Conformal Prediction for Time-Dependent PDEs

[官方论文页](https://neurips.cc/virtual/2026/poster/150920) · [作者来源](https://openreview.net/forum?id=eOMQpbl25E)

- **问题 / 瓶颈** · 相近时刻的物理场分布仍可能不相容
- **核心创新 / 方法** · 分析函数空间奇异性与离散后的总变差，并在特定情形加权校准
- **Baseline** · 直接迁移共形校准
- **Benchmark** · 时间相关 PDE 代理模型的理论覆盖
- **关键结果 / 消融** · 证明精确覆盖可能不可得，并给出特定情形的有限样本保证
- **适用条件 / 局限** · 保证取决于离散化和设定

**可复用机制** · 改变网格前先扫描时域覆盖误差

<a id="paper-152533"></a>

## Conformal Prediction with Paraphrase-Aware Scoring for LLM Uncertainty Quantification

[官方论文页](https://neurips.cc/virtual/2026/poster/152533) · [作者来源](https://openreview.net/forum?id=SRr3j0cdl9)

- **问题 / 瓶颈** · 改写可能导致置信波动
- **核心创新 / 方法** · 用轻量代理产生可比输出并汇总多个改写分数
- **Baseline** · 单输入校准
- **Benchmark** · 多个模型族和不确定性基准的覆盖与集合大小
- **关键结果 / 消融** · 作者报告达到名义覆盖且集合更小更稳
- **适用条件 / 局限** · 改写须保持语义并增加推理开销

**可复用机制** · 同时报告覆盖和改写敏感性

<a id="paper-148731"></a>

## Conformal Selective Acting: Anytime-Valid Risk Control for RLVR-Trained LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/148731) · [作者来源](https://openreview.net/forum?id=vT3wPXlmSr)

- **问题 / 瓶颈** · 长时平均无法保证已执行动作的任意时刻错误率
- **核心创新 / 方法** · 对候选阈值维护 e-process 并选择通过认证的阈值
- **Baseline** · 边际风险和平均风险封装
- **Benchmark** · 在线 RLVR 流上的选择风险与认证复杂度
- **关键结果 / 消融** · 在可预测更新与单调风险下给出任意时刻路径保证
- **适用条件 / 局限** · 依赖等序校准和反馈可用

**可复用机制** · 把选择风险和边际风险分开设计验收

<a id="paper-149343"></a>

## Confounding-Aware Client Selection in Federated Learning via Causal Mediation Analysis

[官方论文页](https://neurips.cc/virtual/2026/poster/149343) · [作者来源](https://openreview.net/forum?id=qnyQCVffeL)

- **问题 / 瓶颈** · 激励可能把低报价当高价值
- **核心创新 / 方法** · 用客户端信息、报价与边际贡献的因果中介模型调整混杂
- **Baseline** · 现有激励与选择方法，名称待核
- **Benchmark** · 多个联邦学习数据集，测精度与社会福利
- **关键结果 / 消融** · 作者报告两项改善，幅度待核
- **适用条件 / 局限** · 依赖因果结构和可辨识条件

**可复用机制** · 对照按报价和按校正贡献分配预算

<a id="paper-139242"></a>

## ConnectomeBench2: A Unified Benchmark for Automated Connectomic Proofreading

[官方论文页](https://neurips.cc/virtual/2026/poster/139242) · [作者来源](https://openreview.net/forum?id=ceOs8fK1Ev)

- **问题 / 瓶颈** · 域内准确不能保证新物种和脑区可靠
- **核心创新 / 方法** · 在共享视觉与几何编码下评估分割纠错，比较距离与失准
- **Baseline** · 专家校对与数据规模及多样性对照
- **Benchmark** · 四种物种的连接组专家标注
- **关键结果 / 消融** · 报告域内校准，分布距离可预测域外准确率与校准下降
- **适用条件 / 局限** · 依赖专家标签与具体影像协议

**可复用机制** · 外推校对模型前以分布距离触发人工验证

<a id="paper-152592"></a>

## Conservation Laws for Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152592) · [作者来源](https://openreview.net/forum?id=RxdFtImvkv)

- **问题 / 瓶颈** · 去噪损失和整体似然的关系缺少统一刻画
- **核心创新 / 方法** · 将交叉熵写为沿噪声路径的局部信息导数积分
- **Baseline** · 离散和连续扩散及高斯 I-MMSE 特例
- **Benchmark** · Markov 源、text8、CIFAR-10
- **关键结果 / 消融** · 精确恒等式与有限容量下路径性能差异获实验支持
- **适用条件 / 局限** · 依赖所分析的无记忆噪声过程

**可复用机制** · 相同容量下比较不同路径的局部拟合误差

<a id="paper-149132"></a>

## Conservatism Controllable Compositional Guidance for Offline Safe Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149132) · [作者来源](https://openreview.net/forum?id=schnHNuzz8)

- **问题 / 瓶颈** · 固定训练折衷难覆盖多任务约束
- **核心创新 / 方法** · 分别训练奖励和安全引导，部署时组合并调节尺度
- **Baseline** · IQL 与优势加权回归等方法
- **Benchmark** · 离线安全强化学习的收益与约束代价
- **关键结果 / 消融** · 作者报告更好的折衷，幅度待核
- **适用条件 / 局限** · 离线覆盖与安全估值误差仍有限制

**可复用机制** · 固定训练数据绘制部署时的收益和风险曲线

<a id="paper-150543"></a>

## Conservative Continuous-Time Treatment Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/150543) · [作者来源](https://openreview.net/forum?id=hM2WDyPurD)

- **问题 / 瓶颈** · 优化器可能利用动力学代理误差
- **核心创新 / 方法** · 用路径签名核 MMD 约束预测轨迹与历史观测距离
- **Baseline** · 无保守正则的离线控制
- **Benchmark** · 模拟环境中的控制代价和鲁棒性
- **关键结果 / 消融** · 作者报告模拟下更稳健
- **适用条件 / 局限** · 仅模拟验证，本卡提取通用离线控制机制

**可复用机制** · 在验证模拟器中扫描支持惩罚并记录外推误差

<a id="paper-155960"></a>

## Conservative neural posterior estimation via distributionally robust training

[官方论文页](https://neurips.cc/virtual/2026/poster/155960) · [作者来源](https://openreview.net/forum?id=1XyUmZsyBA)

- **问题 / 瓶颈** · 神经后验易过度自信
- **核心创新 / 方法** · 在 Wasserstein 邻域最小化最坏训练损失
- **Baseline** · 标准神经后验估计
- **Benchmark** · 模拟推断任务的覆盖、校准和泛化差距
- **关键结果 / 消融** · 作者报告覆盖改善且训练与总体损失差距缩小
- **适用条件 / 局限** · 依赖邻域半径与仿真分布

**可复用机制** · 在固定仿真预算下比较覆盖而非只看拟合

<a id="paper-152985"></a>

## Conservative Pareto Set Amortization for Offline Multi-Objective Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/152985) · [作者来源](https://openreview.net/forum?id=Oqu7rV8HZm)

- **问题 / 瓶颈** · 引导生成需反复采样再筛选候选
- **核心创新 / 方法** · 训练偏好到设计的确定映射，由悲观逐目标代理及冻结支持先验监督
- **Baseline** · 引导扩散或流生成
- **Benchmark** · 离线多目标优化基准，比较解质量和推理开销
- **关键结果 / 消融** · 作者报告表现有竞争力且每方向只需一次查询
- **适用条件 / 局限** · 受离线支持和代理误差约束

**可复用机制** · 同等查询预算下比较直接映射与生成筛选

<a id="paper-153648"></a>

## Consilience for Verifier-Free Test-Time Scaling

[官方论文页](https://neurips.cc/virtual/2026/poster/153648) · [作者来源](https://openreview.net/forum?id=JlfjRX1l6T)

- **问题 / 瓶颈** · 高置信可能反映搜索不足
- **核心创新 / 方法** · 奖励先探索后收敛的置信度模式
- **Baseline** · 只按置信度排名
- **Benchmark** · 研究生数学与自由代码生成
- **关键结果 / 消融** · 作者报告优于基线
- **适用条件 / 局限** · 依赖置信度可比较

**可复用机制** · 分别消融初始置信惩罚与末端门槛

<a id="paper-155880"></a>

## Consistency as a Testable Property: Statistical Methods to Evaluate AI Agent Reliability

[官方论文页](https://neurips.cc/virtual/2026/poster/155880) · [作者来源](https://openreview.net/forum?id=28uXN3BzkF)

- **问题 / 瓶颈** · 通过率掩盖策略崩溃
- **核心创新 / 方法** · 用 U 统计量衡量输出一致性，用核度量衡量轨迹
- **Baseline** · pass@1
- **Benchmark** · 三个 Agent 基准
- **关键结果 / 消融** · 轨迹指标诊断更敏感
- **适用条件 / 局限** · 依赖扰动保义与轨迹度量

**可复用机制** · 固定语义重复运行并分开统计结果和过程

<a id="paper-151483"></a>

## Consistency-Preserving Concept Erasure via Unsafe–Safe Pairing and Directional Fisher-weighted Adaptation

[官方论文页](https://neurips.cc/virtual/2026/poster/151483) · [作者来源](https://openreview.net/forum?id=aHNQKnXHXJ)

- **问题 / 瓶颈** · 直接擦除可能破坏构图
- **核心创新 / 方法** · 配对语义重对齐与 Fisher 加权 DoRA 初始化
- **Baseline** · 已有概念擦除方法
- **Benchmark** · 擦除、保真与生成质量
- **关键结果 / 消融** · 作者报告均改善
- **适用条件 / 局限** · 依赖干净且保结构的替代样本

**可复用机制** · 同时检查改动区域与应保持区域

<a id="paper-154153"></a>

## Consistency Regularised Gradient Flows for Inverse Problems

[官方论文页](https://neurips.cc/virtual/2026/poster/154153) · [作者来源](https://openreview.net/forum?id=FrNVq0ydC9)

- **问题 / 瓶颈** · 许多评估步和自动编码器反传耗时
- **核心创新 / 方法** · 用统一欧氏–Wasserstein 梯度流配合少步模型
- **Baseline** · 已有潜扩散逆求解器
- **Benchmark** · 图像逆问题，以重建和网络评估次数比较
- **关键结果 / 消融** · 报告少步下精度与成本改善
- **适用条件 / 局限** · 依赖潜先验与观测匹配

**可复用机制** · 同预算比较联合流与顺序调提示

<a id="paper-152211"></a>

## Consistency-Verified Backdoor Defense for Federated Graph Learning via Cross-Layer Drift

[官方论文页](https://neurips.cc/virtual/2026/poster/152211) · [作者来源](https://openreview.net/forum?id=UjxaVYw25d)

- **问题 / 瓶颈** · 异质客户端容易误判
- **核心创新 / 方法** · 融合跨层漂移风险与服务器一致性核验
- **Baseline** · 已有联邦图后门防御
- **Benchmark** · 不同联邦图设置，测干净准确率与风险
- **关键结果 / 消融** · 作者报告保精度并降低风险
- **适用条件 / 局限** · 依赖可用的更新一致性信号

**可复用机制** · 按异质程度分别报告防御收益和干净精度

<a id="paper-148758"></a>

## Consistent 3D Surface Flow Model with Global State

[官方论文页](https://neurips.cc/virtual/2026/poster/148758) · [作者来源](https://openreview.net/forum?id=vGEOI5LZ5X)

- **问题 / 瓶颈** · 逐视图输出重复，固定解码粒度受限
- **核心创新 / 方法** · 未标定位姿的视图压成固定 token，再用流匹配解码定向点
- **Baseline** · 前馈及优化式重建
- **Benchmark** · 多视图表面指标与耗时
- **关键结果 / 消融** · 作者报告输出最高百万点，较优化式快约一个数量级
- **适用条件 / 局限** · 遮挡与光度一致性影响质量

**可复用机制** · 固定潜变量扫描输出点数验证精度成本

<a id="paper-156639"></a>

## Consistent Bayesian Spatial Domain Partitioning Using Predictive Spanning Tree Methods

[官方论文页](https://neurips.cc/virtual/2026/poster/156639) · [作者来源](https://neurips.cc/virtual/2026/poster/156639)

- **问题 / 瓶颈** · 有限空间单元聚类不便外推
- **核心创新 / 方法** · 先划分空间块，再用树切边诱导相连分区，推导后验集中条件
- **Baseline** · 生成树型空间聚类
- **Benchmark** · 仿真与大西洋数据
- **关键结果 / 消融** · 给出分区和簇数一致性及收敛率
- **适用条件 / 局限** · 依赖超参数与域内加密采样设定

**可复用机制** · 按理论条件比较切分和预测稳定性

<a id="paper-153249"></a>

## Consistent Geometric Deep Learning via Hilbert Bundles and Cellular Sheaves

[官方论文页](https://neurips.cc/virtual/2026/poster/153249) · [作者来源](https://openreview.net/forum?id=MdvTIPEaIr)

- **问题 / 瓶颈** · 普通图算子难处理不规则域的无限维信号
- **核心创新 / 方法** · 以 Hilbert 丛连接拉普拉斯定义卷积，再经两阶段采样离散
- **Baseline** · 经典图拉普拉斯收敛是理论参照
- **Benchmark** · 流形采样密度提高时的算子收敛
- **关键结果 / 消融** · 作者证明离散鞘算子依概率收敛
- **适用条件 / 局限** · 依赖几何连接与采样条件

**可复用机制** · 用分辨率扫描核对离散模型逼近误差

<a id="paper-150290"></a>

## Consistent One-vs-All Losses Robust to Misspecification of the Weak Label Transition Model

[官方论文页](https://neurips.cc/virtual/2026/poster/150290) · [作者来源](https://openreview.net/forum?id=jH8P1bT8U2)

- **问题 / 瓶颈** · 噪声机制错设破坏监督修正
- **核心创新 / 方法** · 转换一对其余损失并刻画保一致的转移空间
- **Baseline** · 反向修正与部分标签损失
- **Benchmark** · 弱标签模型错设条件下的分类比较
- **关键结果 / 消融** · 报告错设时优于既有方法
- **适用条件 / 局限** · 概率校准不是其优化目标

**可复用机制** · 区分排序需求与概率校准需求后选损失

<a id="paper-150965"></a>

## Consolidating Reasoning with Test-Time Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/150965) · [作者来源](https://openreview.net/forum?id=dwDo02oHXs)

- **问题 / 瓶颈** · 独立排名丢失互补步骤
- **核心创新 / 方法** · 元学习轻量 LoRA 内循环把并行轨迹写入参数
- **Baseline** · 最佳轨迹聚合基线
- **Benchmark** · 数学与 STEM，训练集含 12810 题
- **关键结果 / 消融** · 作者报告总体较最佳聚合提升 20%
- **适用条件 / 局限** · 额外更新预算与跨域迁移待核

**可复用机制** · 固定候选和成本比较参数整合与选择

<a id="paper-153456"></a>

## Consolidating Rewarded Perturbations for LLM Post-Training

[官方论文页](https://neurips.cc/virtual/2026/poster/153456) · [作者来源](https://openreview.net/forum?id=L9ncjOTwgM)

- **问题 / 瓶颈** · 扰动集成需多次前向
- **核心创新 / 方法** · 识别低秩更新结构并按奖励与兼容性加权，留出验证门控
- **Baseline** · RandOpt 与多次投票
- **Benchmark** · 五个模型与五项任务，涵盖数学代码写作
- **关键结果 / 消融** · 较底座平均提高 8.1 点
- **适用条件 / 局限** · 依赖奖励和验证代表性

**可复用机制** · 对照同扰动预算下单模型与集成

<a id="paper-152366"></a>

## Constant Term Shrinkage for Federated Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/152366) · [作者来源](https://openreview.net/forum?id=TawbVu1x6Q)

- **问题 / 瓶颈** · 直接平均会混进客户端漂移
- **核心创新 / 方法** · 分解常数与残差，由更新统计量闭式估计收缩量
- **Baseline** · 多种既有联邦训练方法
- **Benchmark** · 多数据集与异质性设置，比较稳健性及成本
- **关键结果 / 消融** · 作者报告无需额外通信仍改善稳健性
- **适用条件 / 局限** · 依赖分量分解能识别偏移

**可复用机制** · 保持残差不变，消融选择性与全量收缩

<a id="paper-154134"></a>

## Constrained Bombieri Point Processes

[官方论文页](https://neurips.cc/virtual/2026/poster/154134) · [作者来源](https://openreview.net/forum?id=Fyr9E68KbH)

- **问题 / 瓶颈** · 硬约束使多样子集采样难计算
- **核心创新 / 方法** · 用多项式 Bombieri 内积构造点过程与参数化采样算法
- **Baseline** · 受约束 k-DPP
- **Benchmark** · 匹配、路径、子图及预算约束理论
- **关键结果 / 消融** · 在样本数固定时给出固定参数可解保证
- **适用条件 / 局限** · 样本数大时复杂度仍可能高

**可复用机制** · 评估约束采样时同时报告样本大小与实例规模

<a id="paper-148166"></a>

## Constrained Code Generation with Discrete Diffusion

[官方论文页](https://neurips.cc/virtual/2026/poster/148166) · [作者来源](https://openreview.net/forum?id=zoVQ8aHNUH)

- **问题 / 瓶颈** · 事后完全重写成本高
- **核心创新 / 方法** · 中间程序分析定位需修正的区域并局部改变去噪轨迹
- **Baseline** · 离散扩散和自回归生成
- **Benchmark** · 代码生成的功能、语法和安全约束
- **关键结果 / 消融** · 作者报告约束达成改善且修正成本更低
- **适用条件 / 局限** · 依赖可判定约束与分析准确性

**可复用机制** · 对照中途局部检查和事后修复

<a id="paper-149103"></a>

## Constrained Decoding for Diffusion Language Models via Efficient Inference over Finite Automata

[官方论文页](https://neurips.cc/virtual/2026/poster/149103) · [作者来源](https://openreview.net/forum?id=ssAyzXEqoT)

- **问题 / 瓶颈** · 左到右掩码不适用于并行去噪
- **核心创新 / 方法** · 从约束化的均值场后验精确采样，并压缩推理深度
- **Baseline** · 无约束推理
- **Benchmark** · Dream-7B 和 LLaDA-8B，含 BFCL、xLAM、Spider
- **关键结果 / 消融** · BFCL-Live 随机准确率 22.3%→69.0%，额外耗时低于 5%
- **适用条件 / 局限** · 约束须可由有限自动机表达

**可复用机制** · 同时验证格式合规和任务质量

<a id="paper-152576"></a>

## Constrained Factorization with Diagonal Scaling: Rank-Revealing Training and Pruning

[官方论文页](https://neurips.cc/virtual/2026/poster/152576) · [作者来源](https://openreview.net/forum?id=S4MNR0ZcxB)

- **问题 / 瓶颈** · 普通因子分解仅近似低秩
- **核心创新 / 方法** · 约束外因子范数并用对角缩放显式分离秩，再用 SVD 剪枝
- **Baseline** · Burer–Monteiro 与原网络
- **Benchmark** · PSD 恢复、ViT、MLP-Mixer
- **关键结果 / 消融** · 作者报告显著降低参数和计算并保持竞争力
- **适用条件 / 局限** · 依赖可用的层内低秩结构

**可复用机制** · 固定精度比较训练中剪枝与事后低秩逼近

<a id="paper-154981"></a>

## Constrained Goal-directed Planar Graph Generation with Grammar-based Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/154981) · [作者来源](https://openreview.net/forum?id=9Sh3SI4EF1)

- **问题 / 瓶颈** · 生成中难兼顾无交叉等硬约束和任务目标
- **核心创新 / 方法** · 以参数图语法定义受约束 MDP，并在训练中投影动作
- **Baseline** · 经典图生成与深度生成基线
- **Benchmark** · 平面图结构可行性及目标得分
- **关键结果 / 消融** · 作者报告满足所设约束且目标优于对照
- **适用条件 / 局限** · 依赖可表达的语法和可计算投影

**可复用机制** · 将合法结构构造与任务评分拆开消融

<a id="paper-151463"></a>

## Constrained Graph Clustering: A Spectral Algorithm with Generalized Eigenvectors

[官方论文页](https://neurips.cc/virtual/2026/poster/151463) · [作者来源](https://openreview.net/forum?id=aSBc9QvaeR)

- **问题 / 瓶颈** · 单图拉普拉斯难同时反映两类约束
- **核心创新 / 方法** · 以最小广义特征向量嵌入，缺失约束时迭代生成
- **Baseline** · 已有约束聚类
- **Benchmark** · 合成与真实图上的聚类比较
- **关键结果 / 消融** · 在输入假设下给出常数近似，作者报告实证改善
- **适用条件 / 局限** · 依赖图满足理论条件及伪约束质量

**可复用机制** · 对比双图谱嵌入与仅使用必须链接

<a id="paper-151736"></a>

## Constrained Look-ahead Guidance for Interference-Aware Flow Editing

[官方论文页](https://neurips.cc/virtual/2026/poster/151736) · [作者来源](https://openreview.net/forum?id=YT8RaVa0pT)

- **问题 / 瓶颈** · 当前梯度可能让后续保真变差
- **核心创新 / 方法** · 免反演的一步前瞻评估去噪后奖励，并施加保真约束
- **Baseline** · 既有流式图像编辑方法
- **Benchmark** · 语义编辑达成与源内容保留
- **关键结果 / 消融** · 作者报告两者折衷改善
- **适用条件 / 局限** · 依赖奖励质量和近一步预测

**可复用机制** · 对照即时引导与前瞻引导的保真曲线

<a id="paper-154144"></a>

## Constrained MDPs with Trajectory Constraints

[官方论文页](https://neurips.cc/virtual/2026/poster/154144) · [作者来源](https://openreview.net/forum?id=FvA1nYXCFk)

- **问题 / 瓶颈** · 平均安全会掩盖个别轨迹的风险
- **核心创新 / 方法** · 递归计算可达奖励成本集合以刻画历史依赖策略
- **Baseline** · 马尔可夫策略与初始期望约束
- **Benchmark** · 理论计算复杂度与策略结构分析
- **关键结果 / 消融** · 一般情形马尔可夫策略次优，常数个约束下有多项式近似
- **适用条件 / 局限** · 约束数可变时近似求解 NP 难

**可复用机制** · 先确定是否要求每段历史下的条件安全，再选策略记忆

<a id="paper-152484"></a>

## Constrained Modulatory Reservoirs for Context-Dependent Computation

[官方论文页](https://neurips.cc/virtual/2026/poster/152484) · [作者来源](https://openreview.net/forum?id=SkTqNkpAlZ)

- **问题 / 瓶颈** · 多个可训练组件会掩盖适应路径
- **核心创新 / 方法** · 冻结动力学和低秩扰动基底，读出不直接接触线索
- **Baseline** · 可训练基底、活动与增益调制
- **Benchmark** · 瞬态线索通道选择
- **关键结果 / 消融** · 低损失取决于扰动容量、跨间隔保持和响应表达
- **适用条件 / 局限** · 合成任务，外推待核

**可复用机制** · 分别消融重配、记忆与读出

<a id="paper-149304"></a>

## Constrained Stochastic Spectral Preconditioning Converges for Nonconvex Objectives

[官方论文页](https://neurips.cc/virtual/2026/poster/149304) · [作者来源](https://openreview.net/forum?id=rCGJvUIOsM)

- **问题 / 瓶颈** · 理想矩阵符号与实际多项式更新不同
- **核心创新 / 方法** · 分析非线性谱预条件与近端步，并加入方差缩减
- **Baseline** · Muon、Scion及理想谱预条件
- **Benchmark** · 非凸目标下的收敛分析
- **关键结果 / 消融** · 给出重尾噪声收敛与标准噪声下加速
- **适用条件 / 局限** · 速率常数和假设待正文核查

**可复用机制** · 以真实更新算子替代理想化算子

<a id="paper-154276"></a>

## CONSTRAINER: Promptable Graph-Structured Optimization via Constraint Conditioning

[官方论文页](https://neurips.cc/virtual/2026/poster/154276) · [作者来源](https://openreview.net/forum?id=F2JqroViJ0)

- **问题 / 瓶颈** · 固定问题模型难迁移
- **核心创新 / 方法** · 把约束解析为算子图并编码为不变嵌入
- **Baseline** · 共享实例表示的方法
- **Benchmark** · 混合整数线性规划和电网优化
- **关键结果 / 消融** · 作者报告最优性与迁移改善
- **适用条件 / 局限** · 可行性保证与数值待核

**可复用机制** · 将问题约束与实例输入解耦

<a id="paper-155081"></a>

## Constraint-Aware Influence Estimation in Deep Constrained Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/155081) · [作者来源](https://openreview.net/forum?id=8au0CJzVts)

- **问题 / 瓶颈** · 经典影响函数只近似目标变化会偏
- **核心创新 / 方法** · 通过变分不等式刻画约束最优性并估计方向影响
- **Baseline** · 经典、罚项影响函数与重训练
- **Benchmark** · 约束回归、公平约束CNN
- **关键结果 / 消融** · 更符合留一重训练和测试损失变化
- **适用条件 / 局限** · 非光滑约束与规模边界待核

**可复用机制** · 用留一重训校验可行域敏感归因

<a id="paper-155108"></a>

## Constraint Retrieval Is Not Constraint Enforcement in Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155108) · [作者来源](https://openreview.net/forum?id=8LYdKabYW6)

- **问题 / 瓶颈** · 记住规则仍可能生成不合规内容
- **核心创新 / 方法** · 比较替代计划与表面形式约束，并分析执行时信号
- **Baseline** · 五个模型族及解码校验
- **Benchmark** · 提示约束合规测试
- **关键结果 / 消融** · 召回信号仍存在；表面校验不保证语义合规
- **适用条件 / 局限** · 语义规则需更高层验证

**可复用机制** · 把法规或格式校验纳入独立验收

<a id="paper-152789"></a>

## Constructive Neural Policies for the Quadratic Assignment Problem via Multi-Expert Imitation

[官方论文页](https://neurips.cc/virtual/2026/poster/152789) · [作者来源](https://openreview.net/forum?id=QK9X8K6gkZ)

- **问题 / 瓶颈** · 构造型策略难以处理成对成本
- **核心创新 / 方法** · 使用状态相关设施位置表示和启发式专家序列蒸馏
- **Baseline** · SAWT迭代改进
- **Benchmark** · 133个QAPLIB实例，五种子
- **关键结果 / 消融** · 平均差距11.02%，SAWT报告26.8%
- **适用条件 / 局限** · 协议和迭代预算不同

**可复用机制** · 固定推理预算比较构造与迭代求解

<a id="paper-154159"></a>

## Consumer Search and Social Learning in Agentic Markets

[官方论文页](https://neurips.cc/virtual/2026/poster/154159) · [作者来源](https://openreview.net/forum?id=Fogx1QxJIm)

- **问题 / 瓶颈** · 个体搜索改进不一定提高市场学习
- **核心创新 / 方法** · 建立成本搜索和跨消费者学习的动态模型
- **Baseline** · 可观察与不可观察搜索信号
- **Benchmark** · 稳态理论和数值模拟
- **关键结果 / 消融** · 隐藏搜索信号时技术改进也可能损害市场表现
- **适用条件 / 局限** · 模型结构和信息假设限制外推

**可复用机制** · 同时测个人效用与群体学习

<a id="paper-154366"></a>

## Contact Geometry for Generative Models: An Unbalanced Optimal Transport Formulation

[官方论文页](https://neurips.cc/virtual/2026/poster/154366) · [作者来源](https://openreview.net/forum?id=E75sBSUY4i)

- **问题 / 瓶颈** · 传统几何可能偏向高密度区
- **核心创新 / 方法** · 用接触几何解耦密度输运与质量增长
- **Baseline** · WFR方法
- **Benchmark** · 未配对图像翻译与视频生成
- **关键结果 / 消融** · 作者报告改进，幅度待核
- **适用条件 / 局限** · 步长敏感性待查

**可复用机制** · 评估高密度区过冲及少数模式覆盖

<a id="paper-149750"></a>

## Context as Low-Rank Weights: Bounded Parametric Dynamic Memory for Unbounded Context

[官方论文页](https://neurips.cc/virtual/2026/poster/149750) · [作者来源](https://openreview.net/forum?id=ndegfU6uMP)

- **问题 / 瓶颈** · KV缓存随历史线性增长
- **核心创新 / 方法** · 将历史压缩成有限权重基底并按查询路由
- **Baseline** · 完全注意力及高效基线
- **Benchmark** · 窗口内外长上下文任务
- **关键结果 / 消融** · 作者报告接近完全注意力并改善窗口外表现
- **适用条件 / 局限** · 记忆容量与延迟待核

**可复用机制** · 固定内存下测远距召回与覆盖

<a id="paper-151846"></a>

## Context-Aware Autoregressive Image Generation for Emerging Reasoning Properties

[官方论文页](https://neurips.cc/virtual/2026/poster/151846) · [作者来源](https://openreview.net/forum?id=XS3R795hKo)

- **问题 / 瓶颈** · 固定顺序可能遗漏图像结构依赖
- **核心创新 / 方法** · 联合全局上下文和局部信息决定位置
- **Baseline** · 固定或随机顺序
- **Benchmark** · 掩码自回归与多尺度自回归
- **关键结果 / 消融** · 作者报告结构稳健和复杂指令对齐改善
- **适用条件 / 局限** · 位置选择成本与指标待查

**可复用机制** · 在等预算下消融位置调度

<a id="paper-151257"></a>

## Context-Aware Generative Imputation for Robust Multimodal Learning in Missing Modality Scenarios

[官方论文页](https://neurips.cc/virtual/2026/poster/151257) · [作者来源](https://openreview.net/forum?id=bk4w1XMdSu)

- **问题 / 瓶颈** · 目标潜变量不唯一易坍塌
- **核心创新 / 方法** · 采用数据驱动遮蔽与条件分布对齐
- **Baseline** · 共享表示、专家路由及缺模态方法
- **Benchmark** · MIMIC三项预测、随机与自然缺失
- **关键结果 / 消融** · 作者报告效果较好并验证两组件
- **适用条件 / 局限** · 单一临床来源，部署效用待证

**可复用机制** · 区分随机缺失及系统性缺失

<a id="paper-153871"></a>

## Context Binding and Reusable Leakage in Threshold Decryption

[官方论文页](https://neurips.cc/virtual/2026/poster/153871) · [作者来源](https://openreview.net/forum?id=I8M8PZy2XG)

- **问题 / 瓶颈** · 单次损失低估跨上下文复用
- **核心创新 / 方法** · 以可达上下文刻画重复泄漏博弈的威慑条件
- **Baseline** · 可复用与上下文隔离方案
- **Benchmark** · 单调访问结构下的理论
- **关键结果 / 消融** · 单位损失下总威慑成本分别随轮次增长或保持常数
- **适用条件 / 局限** · 依赖折扣收益与问责模型

**可复用机制** · 将隔离作为防御评估维度

<a id="paper-139652"></a>

## ContextShift: A Controlled Benchmark for Context Dependence in Object Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/139652) · [作者来源](https://openreview.net/forum?id=DDUVPd74o7)

- **问题 / 瓶颈** · 总体AP会隐去上下文造成的召回损失
- **核心创新 / 方法** · 按背景置换及统计兼容性建立受控对照
- **Baseline** · 原图与背景替换，比较多类检测器
- **Benchmark** · COCO 2017，漏检、误检及候选量
- **关键结果 / 消融** · 漏检最多增加227%，候选量最多下降44%
- **适用条件 / 局限** · 替换质量及自然偏移外推待核

**可复用机制** · 分别报告召回与预测数量

<a id="paper-148315"></a>

## Contextual Flow Matching: Adaptive Step Selection in Flow Models for Efficient Visual Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/148315) · [作者来源](https://openreview.net/forum?id=yjB0PiXm3S)

- **问题 / 瓶颈** · 固定步数浪费易样本预算
- **核心创新 / 方法** · 训练轻量分配器以无监督奖励平衡保真与效率
- **Baseline** · 固定步数等加速方法
- **Benchmark** · 图像与视频生成
- **关键结果 / 消融** · 作者报告超过2.5倍加速且质量相近
- **适用条件 / 局限** · 需核对硬件、输入分布和奖励

**可复用机制** · 在等质量下报告逐输入时间

<a id="paper-156013"></a>

## Contextual Flow Matching for High-quality Visual Content Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/156013) · [作者来源](https://openreview.net/forum?id=1AXA4TdiEG)

- **问题 / 瓶颈** · 逐点监督忽略速度空间关联
- **核心创新 / 方法** · 加入微分和聚合算子分别约束高低频
- **Baseline** · 逐点流匹配
- **Benchmark** · ImageNet生成
- **关键结果 / 消融** · 作者报告收敛和生成保真度改善
- **适用条件 / 局限** · 指标和各项独立贡献待核

**可复用机制** · 固定模型消融局部差分和低频聚合

<a id="paper-138894"></a>

## Contextualized Evaluation of Vision Language Models through Dynamic Interviews

[官方论文页](https://neurips.cc/virtual/2026/poster/138894) · [作者来源](https://openreview.net/forum?id=yKrnpC8dOT)

- **问题 / 瓶颈** · 静态题目漏掉澄清与修正能力
- **核心创新 / 方法** · 将被测模型、考官和评分者分开并进行半结构访谈
- **Baseline** · 静态基准作为概念对照
- **Benchmark** · 图结构任务与多轮交互，指标待核
- **关键结果 / 消融** · 现有摘要未提供对照数字
- **适用条件 / 局限** · 考官与评分一致性待核

**可复用机制** · 跟踪状态转移证据而非只按结论评分

<a id="paper-149025"></a>

## Context Value Informed In-Context Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149025) · [作者来源](https://openreview.net/forum?id=tPPn7WBWDR)

- **问题 / 瓶颈** · 整轨迹回报可能造成高方差
- **核心创新 / 方法** · 训练价值头并将状态和上下文条件价值写为token
- **Baseline** · 依赖轨迹回报的上下文学习
- **Benchmark** · Dark Room、Minigrid、Procgen
- **关键结果 / 消融** · 作者报告适配更稳定且回报较高
- **适用条件 / 局限** · 价值估计误差及预算依赖待核

**可复用机制** · 同等交互预算比较回报和价值反馈

<a id="paper-139270"></a>

## Continual Learning Bench: Evaluating Frontier AI Systems in Real-World Stateful Environments

[官方论文页](https://neurips.cc/virtual/2026/poster/139270) · [作者来源](https://openreview.net/forum?id=ajW4TqUrCd)

- **问题 / 瓶颈** · 跨实例只测最终成绩会混淆先验
- **核心创新 / 方法** · 构造共享潜在结构的连续任务并测经验增益
- **Baseline** · 朴素上下文与专用记忆系统
- **Benchmark** · 六领域专家验证任务
- **关键结果 / 消融** · 作者报告朴素上下文优于专用记忆系统
- **适用条件 / 局限** · 结论依赖已测架构与任务顺序

**可复用机制** · 控制初始能力比较经验复用

<a id="paper-152180"></a>

## Continual Learning in Modern Hopfield Networks with an Application to Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152180) · [作者来源](https://openreview.net/forum?id=UyZlLEPgiU)

- **问题 / 瓶颈** · 平均遗忘掩盖少数孤立模式丢失
- **核心创新 / 方法** · 用Hopfield能量增加刻画遗忘并按能量选择回放
- **Baseline** · 聚簇与孤立样本、不同能量回放
- **Benchmark** · Hopfield网络、Stable Diffusion及像素DDPM
- **关键结果 / 消融** · 高能样本遗忘更大且从回放获益明显
- **适用条件 / 局限** · 可解析假设与实际能量估计待核

**可复用机制** · 等回放预算下按遗忘风险采样

<a id="paper-155372"></a>

## Continually Evolving Skill Knowledge in Vision Language Action Model

[官方论文页](https://neurips.cc/virtual/2026/poster/155372) · [作者来源](https://openreview.net/forum?id=67rz3TUfbb)

- **问题 / 瓶颈** · 持续模仿扩参不利于规模化
- **核心创新 / 方法** · 学习任务和技能知识表示并用语义近邻引导专家
- **Baseline** · VLA及持续模仿方法
- **Benchmark** · LIBERO与双臂真机迁移
- **关键结果 / 消融** · 作者报告1%回放仍有较强表现
- **适用条件 / 局限** · 长期容量和回放划分待核

**可复用机制** · 同时测新任务适配与旧技能保持

<a id="paper-156741"></a>

## Continual Robot Learning via Language-Guided Skill Acquisition

[官方论文页](https://neurips.cc/virtual/2026/poster/156741) · [作者来源](https://neurips.cc/virtual/2026/poster/156741)

- **问题 / 瓶颈** · 长程规划依赖预制技能，逐任务强化学习成本高。
- **核心创新 / 方法** · 语言模型分解任务并构造符号算子和稠密奖励，维护技能库并复用相关策略。
- **Baseline** · 模拟基线，具名方法待核。
- **Benchmark** · 两套基准的六个任务域及实体机器人展示。
- **关键结果 / 消融** · 作者报告相对基线改善，旧技能可加速新领域学习，幅度待核。
- **适用条件 / 局限** · 依赖有效的符号技能接口及奖励反馈。

**可复用机制** · 用固定新任务预算比较语义检索热启动与从头训练。

<a id="paper-149660"></a>

## Continuity Laws for Sequential Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149660) · [作者来源](https://openreview.net/forum?id=oQ3dzYdHDJ)

- **问题 / 瓶颈** · 连续时间推导不能保证离散模型在采样变化下稳定。
- **核心创新 / 方法** · 将连续性定义为时间离散细化下的轨迹收敛，并估计数据任务的时间连续性。
- **Baseline** · S4 与 S6。
- **Benchmark** · 连续时序基准及降采样效率与效果。
- **关键结果 / 消融** · S4 较稳定，S6 更受输入幅度和选择性动力学影响，作者报告降采样可改善效率与表现。
- **适用条件 / 局限** · 结论依赖离散化、幅度和任务。

**可复用机制** · 对时间采样率做扫描，测量输出收敛及下游任务误差。

<a id="paper-149317"></a>

## ContinuLoc: Continuous Pose Inference over Neural Fields for UAV Geo-Localization

[官方论文页](https://neurips.cc/virtual/2026/poster/149317) · [作者来源](https://openreview.net/forum?id=r4Nd67ZClj)

- **问题 / 瓶颈** · 离散检索的位姿精度受地图采样间距限制。
- **核心创新 / 方法** · 以神经场表示地理参考场景，在四自由度空间分层拟合观察和场景的语义相容性。
- **Baseline** · 离散检索及绝对位姿回归。
- **Benchmark** · ContinuScenes 多城图像，按四自由度精度阈值评估。
- **关键结果 / 消融** · 初步实验报告在更严阈值下仍优于对照，具体幅度待核。
- **适用条件 / 局限** · 需要地理参考与密集位姿监督，跨域泛化待核。

**可复用机制** · 固定语义特征与查询预算，比较离散检索和连续位姿优化。

<a id="paper-148651"></a>

## Continuous Audio Thinking for Large Audio Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148651) · [作者来源](https://openreview.net/forum?id=wA25uq7UK6)

- **问题 / 瓶颈** · 面向文本回答的训练可能丢失音调、情感及事件信息。
- **核心创新 / 方法** · 从音频专家蒸馏声学信息，以连续思考块组织后再解码回答。
- **Baseline** · 基于 Qwen2-Audio、Qwen2.5-Omni-7B、Audio Flamingo 3 对照。
- **Benchmark** · 音频推理、音乐分类、情感和转录等任务。
- **关键结果 / 消融** · 作者报告三模型均有收益，连续块在一次预填充处理，不增加自回归解码开销。
- **适用条件 / 局限** · 需要音频专家，预填充成本与数据条件待核。

**可复用机制** · 对比文本思考和连续听觉表征，对声学细节任务单独报告结果。

<a id="paper-150043"></a>

## Continuous-depth Deep Gaussian Processes

[官方论文页](https://neurips.cc/virtual/2026/poster/150043) · [作者来源](https://openreview.net/forum?id=lD5IXHqE11)

- **问题 / 瓶颈** · 离散层反复复合会使单样本目标变得病态。
- **核心创新 / 方法** · 用随机微分方程的深度依赖漂移建模，研究直接 GP 与流演化两类先验。
- **Baseline** · 普通和残差深层 GP。
- **Benchmark** · 合成、标准及大规模回归。
- **关键结果 / 消融** · 残差版本改善普通模型，作者报告连续版本总体更有利，数值待核。
- **适用条件 / 局限** · 依赖漂移先验与数值求解，训练成本随设定变化。

**可复用机制** · 把深度依赖作为先验设计变量，固定计算预算比较求解稳定性与回归误差。

<a id="paper-152067"></a>

## Continuous Diffusion Scales Competitively with Discrete Diffusion for Language

[官方论文页](https://neurips.cc/virtual/2026/poster/152067) · [作者来源](https://openreview.net/forum?id=ViiyKzhLpA)

- **问题 / 瓶颈** · 旧连续模型与现代离散模型的架构差异会混入扩展结论。
- **核心创新 / 方法** · 对齐 Plaid 架构得到 RePlaid，以似然训练，并分析最小化 ELBO 方差的噪声日程。
- **Baseline** · Plaid、Duo、MDLM 和自回归模型。
- **Benchmark** · OpenWebText 困惑度界、生成质量与计算扩展。
- **关键结果 / 消融** · 报告 PPL 界 22.6，与自回归约差 22 倍计算，并称嵌入优化贡献主要似然收益。
- **适用条件 / 局限** · 困惑度为界，比较依赖所试架构和训练区间。

**可复用机制** · 用匹配配置检查扩展，避免将目标函数优劣与模型代际混淆。

<a id="paper-149532"></a>

## Continuous Expert Assembly: Instance-Conditioned Low-Rank Residuals for All-in-One Image Restoration

[官方论文页](https://neurips.cc/virtual/2026/poster/149532) · [作者来源](https://openreview.net/forum?id=pQjphOzAGt)

- **问题 / 瓶颈** · 统一提示或静态专家不足以适应图像不同区域的组合退化。
- **核心创新 / 方法** · 交叉注意力读取空间特征，生成低秩分量，并按有符号相似度逐 token 密集组装。
- **Baseline** · 提示、描述符及专家型修复方法。
- **Benchmark** · AIO-3、AIO-5、CDD-11，比较修复质量、参数、计算和耗时。
- **关键结果 / 消融** · 作者报告空间变化和组合退化时改善更明显，详细幅度待核。
- **适用条件 / 局限** · 低秩分量容量及实际耗时依赖硬件和分辨率。

**可复用机制** · 固定参数预算，比较全局调制和逐位置低秩调整。

<a id="paper-154716"></a>

## Continuous Latent Diffusion Language Model

[官方论文页](https://neurips.cc/virtual/2026/poster/154716) · [作者来源](https://openreview.net/forum?id=BXGQBSGCtv)

- **问题 / 瓶颈** · 离散扩散需要兼顾全局组织、表示学习和高效输出。
- **核心创新 / 方法** · 以文本 VAE 连接块因果 DiT 的连续潜空间先验与条件解码器。
- **Baseline** · 严格匹配约 2B 参数的自回归与 LLaDA。
- **Benchmark** · 八个基准及最高约 2000 EFLOPs 的扩展曲线。
- **关键结果 / 消融** · 报告文本生成可随规模扩展，关键幅度待核。
- **适用条件 / 局限** · 依赖文本 VAE 稳定性，编码重建误差可能限制输出。

**可复用机制** · 在非自回归生成中单独评估潜语义先验和局部解码瓶颈。

<a id="paper-148351"></a>

## Continuously-Augmented Hybrid Masked Diffusion Model for Data Imputation

[官方论文页](https://neurips.cc/virtual/2026/poster/148351) · [作者来源](https://openreview.net/forum?id=yXHFO8GA82)

- **问题 / 瓶颈** · 全坐标高斯加噪后常需反复投影或重绘以恢复观测。
- **核心创新 / 方法** · 掩码扩散保持观测坐标不变，为缺失位置加连续辅助变量；仅用可见条目作伪缺失目标。
- **Baseline** · 反复 EM 式自补全及采样重绘。
- **Benchmark** · 表格、图像和图文任务，考察重建、感知和计算。
- **关键结果 / 消融** · 作者报告无需相关内循环即可取得较好折衷，数字待核。
- **适用条件 / 局限** · 对真实缺失机制的外推受可见条目代表性限制。

**可复用机制** · 对有明确硬约束的生成，在状态转移中保持约束，并和事后投影比耗时。

<a id="paper-149488"></a>

## Continuous Open-ended Discovery and Evolution of Skills as Hierarchical Reward Programs

[官方论文页](https://neurips.cc/virtual/2026/poster/149488) · [作者来源](https://openreview.net/forum?id=pmS0mCudyh)

- **问题 / 瓶颈** · 开放式技能训练常依赖人工编排长程子任务。
- **核心创新 / 方法** · 把成功条件和前置技能写成分层奖励程序，按状态切换，只训练新增行为。
- **Baseline** · 先前自动训练方案及真值奖励训练。
- **Benchmark** · Craftax-Classic、Craftax-Extended 和 XLand 模拟环境。
- **关键结果 / 消融** · 作者报告中位表现相对提升至约 6 倍和 2.6 倍，扩展实验发现逾 90 个技能程序。
- **适用条件 / 局限** · 要求模拟环境状态可验证；向真机迁移未由摘要确认。

**可复用机制** · 在模拟课程中比较分层成功谓词与直接稀疏目标，在同预算下测技能重用。

<a id="paper-149111"></a>

## Continuous p-adic Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/149111) · [作者来源](https://openreview.net/forum?id=smz6odwrZ6)

- **问题 / 瓶颈** · 直接在 p 进参数上求连续梯度会受到离散赋值限制。
- **核心创新 / 方法** · 提升到 Berkovich 仿射线，利用热带分片的分段线性损失和 max-plus 运算求梯度。
- **Baseline** · 实数参数对应模型。
- **Benchmark** · 合成任务和 p 进 Quillian 语义基准。
- **关键结果 / 消融** · 给出线性模型在热带胞腔内的局部收敛；实验表现相当或更高。
- **适用条件 / 局限** · 理论限于相应子树和局部胞腔，不能外推任意非线性模型。

**可复用机制** · 遇到不连通参数空间时，比较几何保持提升与普通欧式松弛。

<a id="paper-153749"></a>

## Continuous Personalized Diffusion Model via Spinor-Component Forward Geometry

[官方论文页](https://neurips.cc/virtual/2026/poster/153749) · [作者来源](https://openreview.net/forum?id=IzIr9M08Fo)

- **问题 / 瓶颈** · 紧凑标量只在反向阶段注入时，去噪器需同时重建与区分条件。
- **核心创新 / 方法** · 将有界旋量坐标与归一化图像漂移耦合，以条件化前向漂移塑造终端分布。
- **Baseline** · 标准及更高容量反向条件化。
- **Benchmark** · 图像生成的条件连续变化，指标与数据集待核。
- **关键结果 / 消融** · 作者报告单标量下表现有竞争力，并支持连续视觉变化。
- **适用条件 / 局限** · 需要条件有合适连续坐标，离散或高维偏好待验证。

**可复用机制** · 对同一连续控制信号比较前向几何和反向引导，检验中间值过渡。

<a id="paper-150079"></a>

## Continuous-Time Distribution Matching for Few-Step Diffusion Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/150079) · [作者来源](https://openreview.net/forum?id=ktYhgVjpqh)

- **问题 / 瓶颈** · 少量锚点容易遗漏轨迹误差，输出可能过平滑。
- **核心创新 / 方法** · 在随机长度连续日程上匹配分布，用学生速度外推潜变量并对齐。
- **Baseline** · 离散分布匹配蒸馏及一致性蒸馏。
- **Benchmark** · SD3-Medium 和 Longcat-Image 的少步图像生成。
- **关键结果 / 消融** · 报告无复杂辅助目标也能得到较好保真度，量化待核。
- **适用条件 / 局限** · 实际训练开销和两项设计的独立效应待核。

**可复用机制** · 固定推理步数测试连续日程和轨迹外匹配的各自贡献。

<a id="paper-155748"></a>

## Contour Monte Carlo: Sampling via Energy Level Sets

[官方论文页](https://neurips.cc/virtual/2026/poster/155748) · [作者来源](https://openreview.net/forum?id=3FGsou50eW)

- **问题 / 瓶颈** · 重尾或病态分布下 HMC 和 NUTS 混合可能慢。
- **核心创新 / 方法** · 径向目标可闭式抽样；一般目标估计一维能量边缘，并行运行约束层集链。
- **Baseline** · HMC、NUTS。
- **Benchmark** · posteriordb、合成目标和现实推断问题；固定计算预算比较收敛。
- **关键结果 / 消融** · 作者报告较强对照收敛更快；部分径向分布精确且无需链。
- **适用条件 / 局限** · 层集自身若难混合或能量边缘估计不准，收益会受限。

**可复用机制** · 分别诊断能量边缘覆盖与同能层混合，按瓶颈选择采样预算。

<a id="paper-139770"></a>

## ContractBench: Can LLM Agents Preserve Observation Contracts?

[官方论文页](https://neurips.cc/virtual/2026/poster/139770) · [作者来源](https://openreview.net/forum?id=5gUgBwrk8B)

- **问题 / 瓶颈** · 通用工具调用评分会遗漏过期引用及工件在传递中的变化。
- **核心创新 / 方法** · 用可控时钟与确定性完整性检查区分两类失败。
- **Baseline** · 38 个模型及多种模型规模。
- **Benchmark** · ContractBench 的 33 项双轴任务。
- **关键结果 / 消融** · 作者报告最佳 77.8%，表现随规模非单调；失败类型反馈在配对测试中提高 7.1 个百分点。
- **适用条件 / 局限** · 受所测接口和工作流覆盖限制。

**可复用机制** · 对自己维护的代理用模拟工件增加时效和完整性回归测试。

<a id="paper-150369"></a>

## Contractive Monoids: The Algebra Behind Stable Residual Propagation in Deep Graph Neural Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/150369) · [作者来源](https://openreview.net/forum?id=iaW7jdgiUn)

- **问题 / 瓶颈** · 深层图网络容易过平滑，双随机约束背后的必要性质不清。
- **核心创新 / 方法** · 以三条公理刻画收缩幺半群，实例化正交群、对角收缩集与谱范数球。
- **Baseline** · 标准 GNN 和双随机约束思路。
- **Benchmark** · 四种骨干、九个节点分类基准，考察深度增加后的精度和坍缩。
- **关键结果 / 消融** · 摘要报告多个约束在极深模型维持较稳精度和低坍缩。
- **适用条件 / 局限** · 依赖满足结构约束，梯度与表达能力折衷待核。

**可复用机制** · 在相同深度下比较不同收缩残差结构，同时测准确率与表示同质化。

<a id="paper-152740"></a>

## Contractive Restoring Flows: Robust Reasoning Distillation via Orbital Stability

[官方论文页](https://neurips.cc/virtual/2026/poster/152740) · [作者来源](https://openreview.net/forum?id=Qi4A0JHEhM)

- **问题 / 瓶颈** · 逐点匹配无法区分有害漂移和正常推理进展。
- **核心创新 / 方法** · 将残差流建模为动力系统，导出使横向误差收缩、切向不受约束的损失。
- **Baseline** · 其他蒸馏方法，具名对照待核。
- **Benchmark** · 长链推理及推理轨迹鲁棒性。
- **关键结果 / 消融** · 作者报告长链表现改善，在线性化范围内给出稳态误差分析。
- **适用条件 / 局限** · 理论依赖线性化及教师轨迹有效性。

**可复用机制** · 固定教师信号比较各向同性匹配与只压缩横向漂移。

<a id="paper-149353"></a>

## Contrast encodes inductive bias: separating slow noise from dynamics in predictive representation learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149353) · [作者来源](https://openreview.net/forum?id=qhXEAOv8zQ)

- **问题 / 瓶颈** · 跨轨迹负例能让模型靠近似恒定的噪声区分样本。
- **核心创新 / 方法** · 从同一轨迹采负例，并跨多个轨迹共享编码器训练。
- **Baseline** · 跨轨迹负样本的时序对比目标。
- **Benchmark** · 合成移动点的 SimCLR 式 JEPA 与物理摆视频的 DySIB。
- **关键结果 / 消融** · 报告同轨迹采样可恢复动态变量；强慢噪声下长轨迹仍有帮助。
- **适用条件 / 局限** · 当轨迹内状态几乎无变化或噪声本身快变时需复核。

**可复用机制** · 构造可控慢噪声扫描，比较两种负样本策略能否识别真实动力学。

<a id="paper-150131"></a>

## Contrastive Adversarial Training for Robust Graph Neural Networks under Label Poisoning

[官方论文页](https://neurips.cc/virtual/2026/poster/150131) · [作者来源](https://openreview.net/forum?id=kS90WnGV9B)

- **问题 / 瓶颈** · 错误标签的影响会沿邻接传播，单靠监督损失难区分难例和污染。
- **核心创新 / 方法** · 用对比式结构表征辨识异常标签，并将检测与鲁棒训练结合。
- **Baseline** · 既有图标签防御；具体名称待核。
- **Benchmark** · 多图节点分类基准及不同污染程度。
- **关键结果 / 消融** · 作者报告鲁棒性和效率改善，幅度待核。
- **适用条件 / 局限** · 真实异质图也可能标签与邻域不同，需注意误判。

**可复用机制** · 在防御评估中分开报告真实难例误报与污染检出。

<a id="paper-154298"></a>

## Contrastive Discovery: Open-Ended Scientific Discovery over Competing Explanations

[官方论文页](https://neurips.cc/virtual/2026/poster/154298) · [作者来源](https://openreview.net/forum?id=EloJA4f4FX)

- **问题 / 瓶颈** · 逐条否定假说不能说明其他解释是否得到支持。
- **核心创新 / 方法** · 组织相互排斥并覆盖候选空间的解释，用证据引起的相对信念变化评价发现。
- **Baseline** · 逐假说打分的发现方法。
- **Benchmark** · 六类科学任务，同等评估预算下比较已解决问题数。
- **关键结果 / 消融** · 作者报告解决问题更多，部分逐点否定可转化为对替代解释的支持。
- **适用条件 / 局限** · 结论依赖解释集合覆盖和证据质量。

**可复用机制** · 在非生物研究中比较逐假说与成组比较，用同预算测能否区分竞争机制。
