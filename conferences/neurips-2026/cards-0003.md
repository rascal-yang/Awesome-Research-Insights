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

<a id="paper-152434"></a>

## Contrastive Hypergraph Source-free Domain Adaptive Object Detection in Adverse Weathers

[官方论文页](https://neurips.cc/virtual/2026/poster/152434) · [作者来源](https://openreview.net/forum?id=TAXQQlBzoz)

- **问题 / 瓶颈** · 低置信候选易丢失，成对对比难表达高阶关系。
- **核心创新 / 方法** · 按上下文、原型和不确定性构图，以超边级 InfoNCE 对比。
- **Baseline** · 成对对比的无源域适应；具名方法待核。
- **Benchmark** · 恶劣天气目标检测；基准和指标待核。
- **关键结果 / 消融** · 作者报告域偏移下检测改善，幅度待核。
- **适用条件 / 局限** · 依赖提案及分组质量。

**可复用机制** · 对照成对和组级损失，分天气与置信度测召回。

<a id="paper-150695"></a>

## Contrastive Identification and Generation in the Limit

[官方论文页](https://neurips.cc/virtual/2026/poster/150695) · [作者来源](https://openreview.net/forum?id=gCUDMFRrpy)

- **问题 / 瓶颈** · 异类成对信息无法直接揭示哪项为正例。
- **核心创新 / 方法** · 用共同交叉图刻画极限识别和一致生成，并定义对比闭包维数。
- **Baseline** · 仅正例的极限识别及生成。
- **Benchmark** · 无噪和有限污染的理论设定。
- **关键结果 / 消融** · 给出精确刻画及紧样本复杂度；某些类对有限污染的成对监督更稳健。
- **适用条件 / 局限** · 二元假设与特定污染模型。

**可复用机制** · 收集成对标签前分别检查识别唯一性和生成要求。

<a id="paper-148964"></a>

## Contrastive Nonmyopic Objective Cost-Tradeoff Acquisition for Longitudinal Data

[官方论文页](https://neurips.cc/virtual/2026/poster/148964) · [作者来源](https://openreview.net/forum?id=tqkenMK3QV)

- **问题 / 瓶颈** · 早期测量一旦跳过可能无法补做。
- **核心创新 / 方法** · 按未来预测损失和测量成本学对比嵌入，按时间聚类缓存计划。
- **Baseline** · 非参数、贪心与强化学习方案。
- **Benchmark** · 合成及医疗纵向数据，比较准确率和采集成本。
- **关键结果 / 消融** · 作者报告准确率更高且成本更低，幅度待核。
- **适用条件 / 局限** · 依赖训练轨迹对未来收益的估计。

**可复用机制** · 对不可补采数据比较逐步贪心和带预算的计划检索。

<a id="paper-149777"></a>

## Contrastive Pretraining Scales Agentic Exploration

[官方论文页](https://neurips.cc/virtual/2026/poster/149777) · [作者来源](https://openreview.net/forum?id=nO7QFPhYra)

- **问题 / 瓶颈** · 表示各向异性可能把不同动作压成相近特征。
- **核心创新 / 方法** · 通过对比预训练及谱分析解释在线奖励迁移。
- **Baseline** · 非对比预训练。
- **Benchmark** · 语言数据谱分析、多模态个性化及在线推理模拟。
- **关键结果 / 消融** · 理论与模拟支持探索收益；实际规模待核。
- **适用条件 / 局限** · 证据依赖所用动作空间和仿真。

**可复用机制** · 比较预训练目标时在等在线预算下测动作可分性和新奖励迁移。

<a id="paper-151743"></a>

## Contrastive Representation Shaping for LLM Unlearning

[官方论文页](https://neurips.cc/virtual/2026/poster/151743) · [作者来源](https://openreview.net/forum?id=YRlb8TydTR)

- **问题 / 瓶颈** · 输出抑制可能仍保留内部概念表示。
- **核心创新 / 方法** · 对比正则分离待遗忘和保留特征，保持保留特征几何。
- **Baseline** · 主流遗忘方法及其加正则版本；具名待核。
- **Benchmark** · 不同规模语言模型的遗忘基准。
- **关键结果 / 消融** · 报告表示纠缠下降及遗忘改善，数值待核。
- **适用条件 / 局限** · 表示代理不足以单独证明删除。

**可复用机制** · 同时评测遗忘、保留与重新提取风险。

<a id="paper-150870"></a>

## Contrastive Retrieval Heads for Improved Attention-Based Reranking

[官方论文页](https://neurips.cc/virtual/2026/poster/150870) · [作者来源](https://openreview.net/forum?id=el3L9KxeOE)

- **问题 / 瓶颈** · 大量注意力头可能引入排序噪声。
- **核心创新 / 方法** · 用对比注意力得分筛头并裁剪后层。
- **Baseline** · 常规注意力重排序及未裁剪版本。
- **Benchmark** · 多模型和数据集的列表重排。
- **关键结果 / 消融** · 低于 1% 的头承担主要效果；裁后半层排序精度近似。
- **适用条件 / 局限** · 头的定位可能随模型和任务改变。

**可复用机制** · 在固定候选列表上验证头和层裁剪的准确率、延迟及显存。

<a id="paper-153432"></a>

## Contrastive Thinking Decoding: Steering Answer Generation in Reasoning Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153432) · [作者来源](https://openreview.net/forum?id=LNzV4tfoSx)

- **问题 / 瓶颈** · 正确推理记录与最终答案可能分离。
- **核心创新 / 方法** · 对比原轨迹与加噪轨迹下的答案 logits。
- **Baseline** · 标准解码与直接复制轨迹答案。
- **Benchmark** · 数学、科学、代码、MMLU 及迎合测试。
- **关键结果 / 消融** · 正确轨迹与答案分离率达 6%–48%；作者报告不一致下降。
- **适用条件 / 局限** · 需要显式轨迹，额外计算取舍待核。

**可复用机制** · 分别统计推理正确和回答正确，检验纠错与一致性。

<a id="paper-154890"></a>

## Contribution-Aware Structured Sparsity for Model Merging

[官方论文页](https://neurips.cc/virtual/2026/poster/154890) · [作者来源](https://openreview.net/forum?id=A9dM7Hk3BV)

- **问题 / 瓶颈** · 幅值剪裁难区分各任务的重要组件。
- **核心创新 / 方法** · 为注意力头与前馈神经元构造任务结构掩码，可用于合并或调节梯度。
- **Baseline** · 幅值、随机裁剪及代表性合并算子。
- **Benchmark** · ViT 20 项、RoBERTa 8 项及 Qwen2.5 4 项任务。
- **关键结果 / 消融** · 作者报告多种算子表现改善，幅度待核。
- **适用条件 / 局限** · 组件的重要性与任务组合相关。

**可复用机制** · 在同稀疏率下对照无结构裁剪与贡献掩码。

<a id="paper-152028"></a>

## Control-Augmented Autoregressive Diffusion for Data Assimilation

[官方论文页](https://neurips.cc/virtual/2026/poster/152028) · [作者来源](https://openreview.net/forum?id=W4x1rXfdP2)

- **问题 / 瓶颈** · 稀疏观测下自回归预报漂移，在线扩散引导昂贵。
- **核心创新 / 方法** · 预览未来滚动，以终端代价训练控制器修正每次去噪。
- **Baseline** · 强扩散同化方法，具体名称待核。
- **Benchmark** · 两类 PDE、ERA5 六种观测设置和 GenCast 扩展。
- **关键结果 / 消融** · 作者报告约一个数量级加速并改善稳定性。
- **适用条件 / 局限** · 观测机制变化可能需要新控制器。

**可复用机制** · 比较离线控制器与在线校正的精度、漂移及运行时间。

<a id="paper-156073"></a>

## Control Charts for Multi-Agent Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/156073) · [作者来源](https://openreview.net/forum?id=0ef8FCdBWk)

- **问题 / 瓶颈** · 定性监测难量化系统随平台学习产生的漂移。
- **核心创新 / 方法** · 用自适应控制图分析群体过程。
- **Baseline** · 固定参考监测与动态参考。
- **Benchmark** · 模拟与理论分析。
- **关键结果 / 消融** · 作者报告自适应监测有必要，但仅靠动态参考会漏掉部分行为异常。
- **适用条件 / 局限** · 模拟结论能否迁移待核。

**可复用机制** · 用长期基准和动态参考共同检验健康监测的漏报。

<a id="paper-155463"></a>

## Control First, Robustness Next: Decoupled Representation Learning for Visual RL Generalization

[官方论文页](https://neurips.cc/virtual/2026/poster/155463) · [作者来源](https://openreview.net/forum?id=5QHgjQxxKM)

- **问题 / 瓶颈** · 控制与鲁棒目标联合训练可能相互干扰。
- **核心创新 / 方法** · 用弱增强在线训练参考策略，后续将强增强表示映射到参考空间。
- **Baseline** · 联合学习方法；具名对照待核。
- **Benchmark** · RL-ViGen 上的 DMControl 与 Robosuite。
- **关键结果 / 消融** · 作者报告视觉迁移改善且原环境表现保持较好。
- **适用条件 / 局限** · 依赖参考表征质量。

**可复用机制** · 同测原环境和变化环境，对照联合与分阶段训练。

<a id="paper-151092"></a>

## ControlFlow3D: Distilling Multi-View Knowledge into Latent Flow Matching for Point Cloud Upsampling

[官方论文页](https://neurips.cc/virtual/2026/poster/151092) · [作者来源](https://openreview.net/forum?id=d1VrPTpLIA)

- **问题 / 瓶颈** · 稀疏点云难消除几何歧义。
- **核心创新 / 方法** · 在冻结三维表示空间内聚类图像与点 token，用共享原型引导流匹配及一致性蒸馏。
- **Baseline** · 点云上采样基线；具名待核。
- **Benchmark** · ShapeNetPU 的 3.5 万对象及其他上采样基准。
- **关键结果 / 消融** · 作者报告泛化改善，具体指标待核。
- **适用条件 / 局限** · 训练期需配对多视图。

**可复用机制** · 对照共享原型蒸馏和仅点云监督，固定测试输入。

<a id="paper-149461"></a>

## ControlJEPA: Principled Trajectory Regularization via Lyapunov Tube Loss

[官方论文页](https://neurips.cc/virtual/2026/poster/149461) · [作者来源](https://openreview.net/forum?id=pw4nMbt6SR)

- **问题 / 瓶颈** · 角度惩罚不约束离参考轨迹的距离。
- **核心创新 / 方法** · 用离散输入到状态稳定性推导收缩损失和管宽界。
- **Baseline** · 标准微调及已有轨迹正则。
- **Benchmark** · 六个基准、七个模型家族。
- **关键结果 / 消融** · 报告准确率和数据效率改善，推理时几何仍存在。
- **适用条件 / 局限** · 保证依赖收缩假设，管宽选择待核。

**可复用机制** · 用同数据预算比较角度和距离约束，分别测多样性与偏离。

<a id="paper-152374"></a>

## Controllable and Content Based Recommendations

[官方论文页](https://neurips.cc/virtual/2026/poster/152374) · [作者来源](https://openreview.net/forum?id=TYSDot6Dmj)

- **问题 / 瓶颈** · 隐向量难理解和调整。
- **核心创新 / 方法** · 从物品多媒体内容提取文字并接入协同过滤。
- **Baseline** · 潜表示推荐器和 TEARS。
- **Benchmark** · 图像、音频及视频推荐场景。
- **关键结果 / 消融** · 报告排序有竞争力且文本干预可改变推荐。
- **适用条件 / 局限** · 文字摘要可能遗漏关键偏好。

**可复用机制** · 分开评估排序与编辑后的方向一致性。

<a id="paper-154139"></a>

## Controllable Dynamic 3D Shape Generation via 3D Trajectories and Text

[官方论文页](https://neurips.cc/virtual/2026/poster/154139) · [作者来源](https://openreview.net/forum?id=FxPg1mJLqX)

- **问题 / 瓶颈** · 语言很难精确描述部位运动路径。
- **核心创新 / 方法** · 将轨迹编码成与物体形状对齐的条件 token。
- **Baseline** · 文本生成与以轨迹指导的视频方法。
- **Benchmark** · 动态三维形状定量评估和用户研究。
- **关键结果 / 消融** · 报告跟踪和表达改善，幅度待核。
- **适用条件 / 局限** · 受输入轨迹质量与形状对应影响。

**可复用机制** · 固定提示，对照文字与对齐轨迹条件的运动误差。

<a id="paper-155513"></a>

## Controllable Generative Sandbox for Causal Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/155513) · [作者来源](https://openreview.net/forum?id=52BMkNkLA7)

- **问题 / 瓶颈** · 模拟真实分布和控制混杂等因素常有冲突。
- **核心创新 / 方法** · 混合高斯先验与按数据类型设计解码器，并显式调节重叠、混杂和效应异质性。
- **Baseline** · 既有因果模拟器，具名待核。
- **Benchmark** · 混合表格数据及观察研究的估计器验证。
- **关键结果 / 消融** · 报告分布拟合和独立调参能力较强。
- **适用条件 / 局限** · 模拟控制不证明真实混杂已识别。

**可复用机制** · 评估因果估计器时按因子实验独立改变重叠和混杂。

<a id="paper-155376"></a>

## Controllable Multi-label Video Safety Detection via Adaptive Tversky Policy Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/155376) · [作者来源](https://openreview.net/forum?id=66AVx7heNO)

- **问题 / 瓶颈** · 静态二分类目标难适应类别误报与漏报成本。
- **核心创新 / 方法** · 用自适应 Tversky 奖励改变两类错误权重。
- **Baseline** · 静态训练目标和现有视频安全检测。
- **Benchmark** · SafeWatch-Bench 与 XD-Violence。
- **关键结果 / 消融** · SafeWatch-Bench-Real 的 Jaccard 从 40.66 提至 75.44。
- **适用条件 / 局限** · 新类别和阈值迁移待核。

**可复用机制** · 按类别测可控查准查全曲线，明确各工作点的成本。

<a id="paper-155875"></a>

## Controllable Road Marking Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/155875) · [作者来源](https://openreview.net/forum?id=2BbIJHhfqI)

- **问题 / 瓶颈** · 直接预测稀疏路面标线时易断裂。
- **核心创新 / 方法** · 以鸟瞰条件扩散生成软图，再结构化渲染恢复细线。
- **Baseline** · DDIM 掩码细化。
- **Benchmark** · Argoverse 2 测试集上的标线结构保真。
- **关键结果 / 消融** · 作者报告结构指标改善并支持文本编辑。
- **适用条件 / 局限** · 证据限所用地图及提示类别。

**可复用机制** · 对细线生成比较硬标签与软目标，并同时测拓扑连通性。

<a id="paper-148816"></a>

## Controllable User Simulation

[官方论文页](https://neurips.cc/virtual/2026/poster/148816) · [作者来源](https://openreview.net/forum?id=uus8MMsekx)

- **问题 / 瓶颈** · 事后标签耦合行为策略
- **核心创新 / 方法** · 预先控制、逐步控制或直接按策略训练
- **Baseline** · 事后全局标签微调
- **Benchmark** · 对话分布及新策略泛化
- **关键结果 / 消融** · 作者报告保留行为多样性
- **适用条件 / 局限** · 因果条件需核正文

**可复用机制** · 在同一新策略下对照事前条件和事后标签

<a id="paper-153604"></a>

## Controlling for Omitted Variable Bias in Deep Neural Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/153604) · [作者来源](https://openreview.net/forum?id=K9sgYlq0Bi)

- **问题 / 瓶颈** · 去相关不足以校正遗漏变量偏差
- **核心创新 / 方法** · 交叉拟合加岭惩罚重估可加末层
- **Baseline** · 去相关及无混杂训练
- **Benchmark** · 模拟图像和诱导混杂的神经影像
- **关键结果 / 消融** · 恢复模拟真实效应且预测接近无混杂训练
- **适用条件 / 局限** · 依赖测得协变量及可加形式

**可复用机制** · 分别检查协变量效应估计与边际化预测

<a id="paper-151349"></a>

## Controlling Temporal Pseudo-Label Marginals for Stable Online Test-Time Adaptation

[官方论文页](https://neurips.cc/virtual/2026/poster/151349) · [作者来源](https://openreview.net/forum?id=bC8ezX1M1D)

- **问题 / 瓶颈** · 早期偏差会被循环强化
- **核心创新 / 方法** · 用短缓冲与 Sinkhorn 平衡生成软监督
- **Baseline** · 熵或多样性稳定化
- **Benchmark** · 偏斜和非平稳在线数据流
- **关键结果 / 消融** · 作者报告缓解崩塌且开销低于 1%
- **适用条件 / 局限** · 真实类别比例偏移时目标分布需校准

**可复用机制** · 同时跟踪类别边际和在线误差

<a id="paper-149068"></a>

## Controlling Transient Amplification Improves Long-horizon Rollouts

[官方论文页](https://neurips.cc/virtual/2026/poster/149068) · [作者来源](https://openreview.net/forum?id=t6SrxcxWcq)

- **问题 / 瓶颈** · 渐近稳定仍可能出现暂态放大
- **核心创新 / 方法** · 通过雅可比向量积估计两类惩罚
- **Baseline** · 无正则的 UNet、FNO 及 FourCastNet
- **Benchmark** · 一维二维时空数据与 ERA5
- **关键结果 / 消融** · 多步滚动稳定性提高，适用实例达数千步
- **适用条件 / 局限** · 依赖局部线性分析；额外训练成本待核

**可复用机制** · 把暂态误差放大和渐近稳定分开测

<a id="paper-151630"></a>

## Control Reinforcement Learning: Token-Level Mechanistic Analysis via Learned SAE Feature Steering

[官方论文页](https://neurips.cc/virtual/2026/poster/151630) · [作者来源](https://openreview.net/forum?id=Z8Ogf2OPQp)

- **问题 / 瓶颈** · 静态归因可能漏掉时变特征贡献
- **核心创新 / 方法** · 记录逐 token 特征干预的分支变化
- **Baseline** · 静态方向及激活归因
- **Benchmark** · Gemma 与 LLaMA 的通用推理任务
- **关键结果 / 消融** · 观察到跨任务迁移不对称
- **适用条件 / 局限** · 干预解释依赖 SAE 字典

**可复用机制** · 对通用能力分别报告任务内贡献和迁移

<a id="paper-151441"></a>

## ControlSVG: Exploring Controllable SVG Generation with Autoregressive Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151441) · [作者来源](https://openreview.net/forum?id=afzeP5GBOh)

- **问题 / 瓶颈** · 只输入空间条件容易随序列变长漂移
- **核心创新 / 方法** · 反馈已绘结果并将离散 token 与绝对坐标联合监督
- **Baseline** · 条件预填充和条件解码
- **Benchmark** · 边缘图转 SVG，并初步验证手绘
- **关键结果 / 消融** · 作者报告对齐质量改善
- **适用条件 / 局限** · 手绘泛化证据初步

**可复用机制** · 对照只给初始条件与循环观察中间输出

<a id="paper-149917"></a>

## Control Under the Wrong Model Is Better Than Under the Correct One

[官方论文页](https://neurips.cc/virtual/2026/poster/149917) · [作者来源](https://openreview.net/forum?id=mErAv9CVnq)

- **问题 / 瓶颈** · 推断和控制分离可能失效
- **核心创新 / 方法** · 分析线性乘性噪声模型下联合最优控制器
- **Baseline** · 先滤波后控制与外部真实动力学
- **Benchmark** · 带内部噪声的线性控制设定
- **关键结果 / 消融** · 最优内部动力学偏离真实模型，随内部噪声增强
- **适用条件 / 局限** · 结论限于所分析设定

**可复用机制** · 同时按估计误差和闭环成本选内部模型

<a id="paper-149087"></a>

## Convergence Analysis of Newton's Method for Neural Networks in the Overparameterized Limit

[官方论文页](https://neurips.cc/virtual/2026/poster/149087) · [作者来源](https://openreview.net/forum?id=szSde6PDAI)

- **问题 / 瓶颈** · 梯度下降对高频目标拟合慢
- **核心创新 / 方法** · 用 Newton 切核表征无限宽极限
- **Baseline** · 梯度下降 NTK
- **Benchmark** · 过参数化训练理论
- **关键结果 / 消融** · 适当正则下极限收敛指数快且跨频一致
- **适用条件 / 局限** · 有限模型成本与效果待验证

**可复用机制** · 比较优化器时按目标频带分解收敛速度

<a id="paper-155534"></a>

## Convergence Guarantees for Federated SARSA with Local Training and Heterogeneous Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/155534) · [作者来源](https://openreview.net/forum?id=4sFTcukOxE)

- **问题 / 瓶颈** · 本地转移和奖励不同
- **核心创新 / 方法** · 用精确多步误差展开分析 FedSARSA
- **Baseline** · 单智能体 SARSA 与理论对照
- **Benchmark** · 线性近似、异质 Markov 采样和数值实验
- **关键结果 / 消融** · 除高阶项外随智能体数线性加速
- **适用条件 / 局限** · 结论限于线性近似等假设

**可复用机制** · 在固定通信预算下改变本地步数和异质性

<a id="paper-149591"></a>

## Convergence of Near-Linear Width ReLU Networks with Unbalanced Initialization

[官方论文页](https://neurips.cc/virtual/2026/poster/149591) · [作者来源](https://openreview.net/forum?id=owJpOXaqDm)

- **问题 / 瓶颈** · ReLU 激活翻转引起经验核漂移
- **核心创新 / 方法** · 不平衡高斯初始化控制 NTK 漂移，低秩响应可加 sketch
- **Baseline** · 随机特征和共轭核设定及普通梯度下降
- **Benchmark** · 共享首层的双层多输出 ReLU 理论
- **关键结果 / 消融** · 得到近线性宽度保证和 Nesterov 加速
- **适用条件 / 局限** · 依赖极限核谱和输出结构

**可复用机制** · 比较初始化时跟踪核漂移及所需训练宽度

<a id="paper-152956"></a>

## Convex Compositional Reasoning Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152956) · [作者来源](https://openreview.net/forum?id=P8NrHa7X4l)

- **问题 / 瓶颈** · 非凸能量让局部因子组合后难求解
- **核心创新 / 方法** · 用输入凸网络和可行集凸松弛，先对比学习再展开求解器训练
- **Baseline** · 非凸组合能量及小规模训练
- **Benchmark** · 组合推理跨规模泛化
- **关键结果 / 消融** · 作者报告向更大实例免重训迁移
- **适用条件 / 局限** · 松弛紧致性限制实际可行性

**可复用机制** · 分开测因子预测质量与组合后的求解误差

<a id="paper-155590"></a>

## Conveyance: A Versatile Framework for Learning in Structured Class Spaces

[官方论文页](https://neurips.cc/virtual/2026/poster/155590) · [作者来源](https://openreview.net/forum?id=4SAFhHJb63)

- **问题 / 瓶颈** · 交叉熵对类别结构不敏感
- **核心创新 / 方法** · 对不同类别划分优化两个间隔并保持部分凸性
- **Baseline** · 各任务专用方法
- **Benchmark** · 层级分类、序数回归、多实例学习
- **关键结果 / 消融** · 作者报告达到或超过专用对照
- **适用条件 / 局限** · 需可编码的类别关系

**可复用机制** · 固定骨干对照结构损失和标准交叉熵

<a id="paper-152915"></a>

## Cool Graphs: Active Property Search Towards Quantum Nano-Refrigerators

[官方论文页](https://neurips.cc/virtual/2026/poster/152915) · [作者来源](https://openreview.net/forum?id=PRkY0xcxEL)

- **问题 / 瓶颈** · 随机配置很少达到吸热目标
- **核心创新 / 方法** · 图变分编码先分离参数区域，再用 dropout 不确定性选择仿真
- **Baseline** · 随机采样
- **Benchmark** · 电子结吸热预测及跨拓扑验证
- **关键结果 / 消融** · 留出与外推拓扑 ROC-AUC 为 0.89 和 0.80，32 轮优于随机
- **适用条件 / 局限** · 依赖模拟器及不确定性校准

**可复用机制** · 比较边界采样与随机采样每轮发现率

<a id="paper-139333"></a>

## COOP$^2$: Defining, Observing, and Repairing Cooperation in LLM Multi-Agent Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/139333) · [作者来源](https://openreview.net/forum?id=WWrTVADZAi)

- **问题 / 瓶颈** · 最终成功率掩盖协作破裂的位置
- **核心创新 / 方法** · 用环境进度定义可验证协作条件并打开针对性修复通道
- **Baseline** · 无针对性修复的协作流程
- **Benchmark** · 两个环境及三种通信结构
- **关键结果 / 消融** · 作者报告成功率和约束满足改善并产生额外通信
- **适用条件 / 局限** · 需可验证要求及可信预测

**可复用机制** · 同时记录约束通过率、决策开销和消息量

<a id="paper-153701"></a>

## Cooperative Multi-Agent Reinforcement Learning via Epigraph-Form Guided Exploration

[官方论文页](https://neurips.cc/virtual/2026/poster/153701) · [作者来源](https://openreview.net/forum?id=JQUxXMC9Es)

- **问题 / 瓶颈** · 线性混合内外奖励可能破坏任务表现
- **核心创新 / 方法** · 以 epigraph 改写回报约束并自适应探索预算，使用后继距离奖励
- **Baseline** · 常见多智能体探索方法
- **Benchmark** · SMAX、VMAS、MPE
- **关键结果 / 消融** · 作者报告优于强对照且出现新协作策略
- **适用条件 / 局限** · 依赖可靠估计当前回报水平

**可复用机制** · 对照固定加权和以回报底线调节探索

<a id="paper-150402"></a>

## Co-optimization for Adaptive Conformal Prediction

[官方论文页](https://neurips.cc/virtual/2026/poster/150402) · [作者来源](https://openreview.net/forum?id=iIkqszzLay)

- **问题 / 瓶颈** · 固定中心在偏态异方差下区间不经济
- **核心创新 / 方法** · 交替优化折叠残差分位数及中心区间损失，再分割校准
- **Baseline** · 固定中心及其他共形回归方法
- **Benchmark** · 回归区间长度与覆盖可靠性
- **关键结果 / 消融** · 作者证明边际保证及一致估计下渐近条件覆盖
- **适用条件 / 局限** · 有限样本条件覆盖无普遍保证

**可复用机制** · 在匹配覆盖下比较固定与自适应中心区间

<a id="paper-149906"></a>

## Coordinating Hundreds of RL Agents through Scalable Inference-Time Search

[官方论文页](https://neurips.cc/virtual/2026/poster/149906) · [作者来源](https://openreview.net/forum?id=mLNxExQR4f)

- **问题 / 瓶颈** · 统一潜变量限制联合策略空间
- **核心创新 / 方法** · 复用 COMPASS 底座，将潜变量从团队级拆至个体级
- **Baseline** · 共享潜变量的 COMPASS
- **Benchmark** · 三环境十四场景，最多 200 个智能体
- **关键结果 / 消融** · 作者报告大规模场景最高提高 45%
- **适用条件 / 局限** · 要求可仿真评估候选与共享目标

**可复用机制** · 用固定搜索预算扫描团队规模并比较变量共享度

<a id="paper-154512"></a>

## Coordination Connectivity: Shared Initialization Shapes the Joint-Policy Landscape in MARL

[官方论文页](https://neurips.cc/virtual/2026/poster/154512) · [作者来源](https://openreview.net/forum?id=D2HpZYZ8aI)

- **问题 / 瓶颈** · 两支成功团队未必能安全混合
- **核心创新 / 方法** · 测联合插值回报障碍，结合换人和角色交换验证
- **Baseline** · 共享 MAPPO 初始化与独立 HAPPO 团队
- **Benchmark** · 三张 SMAC 地图、四个种子
- **关键结果 / 消融** · 共享初始化的障碍接近零，独立训练团队较高
- **适用条件 / 局限** · 证据限所用训练历史与任务

**可复用机制** · 部署替换单个智能体前测团队回报而非只测单体

<a id="paper-152600"></a>

## CoPE-VideoLM: Leveraging Codec Primitives For Efficient Video Language Modelling

[官方论文页](https://neurips.cc/virtual/2026/poster/152600) · [作者来源](https://openreview.net/forum?id=RvGMXiyXQI)

- **问题 / 瓶颈** · 完整帧编码昂贵，稀疏采样会漏掉事件
- **核心创新 / 方法** · 轻量编码器汇总编解码器原语并预训练对齐图像特征
- **Baseline** · 标准关键帧视频语言模型
- **Benchmark** · 14 项问答、时间、运动和空间理解基准
- **关键结果 / 消融** · 首 token 延时最多降 86%，token 最多降 93%
- **适用条件 / 局限** · 依赖视频编码和原语可用性

**可复用机制** · 在固定 token 预算下扫描关键帧与原语比例

<a id="paper-150787"></a>

## Co-PiLOT: Constrained Physics-Informed Latent Optimization for Target-Driven Inverse Design

[官方论文页](https://neurips.cc/virtual/2026/poster/150787) · [作者来源](https://openreview.net/forum?id=fPIgwuSCOy)

- **问题 / 瓶颈** · 高维微结构直接搜索难保证可行
- **核心创新 / 方法** · 生成解码器作为有效性先验，以不确定性和信赖域选模拟候选
- **Baseline** · 同一解码器下的 DANTE、TuRBO、BAxUS
- **Benchmark** · 镁合金微结构，比较目标相对误差
- **关键结果 / 消融** · 作者报告最佳组合较对照相对误差改善约 6%
- **适用条件 / 局限** · 证据限材料仿真与解码器覆盖

**可复用机制** · 固定模拟预算和解码器比较潜空间搜索策略

<a id="paper-151176"></a>

## COPRA: Conditional Parameter Adaptation with Reinforcement Learning for Video Anomaly Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/151176) · [作者来源](https://openreview.net/forum?id=cQfyDaizQX)

- **问题 / 瓶颈** · 静态视频异常检测难应对域移位及抽帧差异。
- **核心创新 / 方法** · 轻量生成器对冻结视觉语言模型逐片段输出参数更新。
- **Baseline** · 固定提示或静态共享更新。
- **Benchmark** · 视频异常检测、视频问答和密集字幕。
- **关键结果 / 消融** · 摘要报告同域及跨域均优于静态对照。
- **适用条件 / 局限** · 适配延迟和异常类别覆盖待核。

**可复用机制** · 固定骨干比较共享与逐片段更新。

<a id="paper-154658"></a>

## CoQuant: Covariance-Aware Rotation for 2-bit KV Cache Quantization

[官方论文页](https://neurips.cc/virtual/2026/poster/154658) · [作者来源](https://openreview.net/forum?id=ByTqCb7VnS)

- **问题 / 瓶颈** · 通用旋转在两位量化下易丢失注意力信息。
- **核心创新 / 方法** · 离线估计协方差，求固定旋转和裁剪阈值，并配套 INT2 内核。
- **Baseline** · BF16、朴素旋转 INT2。
- **Benchmark** · 五项推理任务及最长 128K 的 RULER-NIAH。
- **关键结果 / 消融** · 两款 Qwen 的 BF16 差距为 3.78 和 1.42 点；缓存约缩小八倍。
- **适用条件 / 局限** · 吞吐收益依硬件、批大小和服务内核而变。

**可复用机制** · 在同内存预算同时测长上下文准确率与吞吐。

<a id="paper-139515"></a>

## CORAL: A Benchmark for Structure-aware and Brain-wide Neuron Reconstruction in Light Microscopy

[官方论文页](https://neurips.cc/virtual/2026/poster/139515) · [作者来源](https://openreview.net/forum?id=LFD4mDTd1s)

- **问题 / 瓶颈** · 局部图块成绩难预测全脑重建质量。
- **核心创新 / 方法** · 基于纤维预测评估结构，并以迭代局部到全局流程扩展重建。
- **Baseline** · 主流局部重建方法，具名对照待核。
- **Benchmark** · fMOST 局部图块与全脑神经元重建。
- **关键结果 / 消融** · 摘要指出结构评测和整脑任务暴露额外缺陷。
- **适用条件 / 局限** · 跨显微模态的泛化待验证。

**可复用机制** · 对长程结构重建同时检查几何、连接及尺度迁移。

<a id="paper-152402"></a>

## CORA: Per-Slice Coherent Orthogonal Rotation for SVD-based Low-Rank Adaptation

[官方论文页](https://neurips.cc/virtual/2026/poster/152402) · [作者来源](https://openreview.net/forum?id=TMmhacwh3s)

- **问题 / 瓶颈** · 普通低秩更新未显式保留左右基的耦合。
- **核心创新 / 方法** · 对权重行切片做截断 SVD，共用正交旋转并调整谱尺度。
- **Baseline** · LoRA、DoRA、PiSSA、MiLoRA。
- **Benchmark** · 常识推理和代码生成。
- **关键结果 / 消融** · 摘要报告用约八分之一参数超过所比方法。
- **适用条件 / 局限** · 切片和秩的选择边界待核。

**可复用机制** · 固定参数预算比较相干旋转与独立低秩更新。

<a id="paper-153844"></a>

## CoRDS: Coreset-Based Representative and Diverse Selection for Streaming Video Understanding

[官方论文页](https://neurips.cc/virtual/2026/poster/153844) · [作者来源](https://openreview.net/forum?id=IJR2muDUYS)

- **问题 / 瓶颈** · 按 token 局部打分可能保留重复帧。
- **核心创新 / 方法** · 在键值联合表示做核心集选择，加入正交多样性。
- **Baseline** · 启发式流式缓存压缩。
- **Benchmark** · 四款视觉语言模型、五项长视频及流式视频基准。
- **关键结果 / 消融** · 固定缓存下摘要报告优于对照。
- **适用条件 / 局限** · 子集选择开销及不同视频分布的影响待核。

**可复用机制** · 同预算分别检验键覆盖、值覆盖及二者联合。

<a id="paper-155856"></a>

## CoreQ: Learning-Free Mismatch Correction and Successive Rounding for Quantization

[官方论文页](https://neurips.cc/virtual/2026/poster/155856) · [作者来源](https://openreview.net/forum?id=2OSsvaeOHi)

- **问题 / 瓶颈** · 前层离散误差改变后层输入，全量补偿可能过拟合小校准集。
- **核心创新 / 方法** · 几何分解推得闭式校正系数，再用逐次舍入或有界束搜索求解。
- **Baseline** · 现有训练后量化方法，具体名称待核。
- **Benchmark** · 多模型族、位宽和量化设定，测困惑度与下游准确率。
- **关键结果 / 消融** · 摘要报告两类指标改善。
- **适用条件 / 局限** · 依赖校准集代表性，束搜索增加计算。

**可复用机制** · 对照全量、固定和逐层自适应校正。

<a id="paper-151276"></a>

## CoRE-RL: Co-evolving Reasoning Trajectories and Evidence Subgraphs with Learned Evidence Projection

[官方论文页](https://neurips.cc/virtual/2026/poster/151276) · [作者来源](https://openreview.net/forum?id=baoEzZg5LH)

- **问题 / 瓶颈** · 一次检索难覆盖多跳桥接事实，扩张又引入干扰。
- **核心创新 / 方法** · 抽取关键主张，利用未支撑主张检索，再按反馈学习保留证据子图。
- **Baseline** · 原始 CoRE 与学习投影版本；其他具名对照待核。
- **Benchmark** · WebQuestionsSP、Complex WebQuestions。
- **关键结果 / 消融** · 摘要报告准确率、证据充分性及预算稳健性改善。
- **适用条件 / 局限** · 依赖主张抽取与知识图谱覆盖。

**可复用机制** · 固定上下文预算比较一次检索和按缺证主张补检。

<a id="paper-154272"></a>

## Coreset-Induced Conditional Velocity Flow Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/154272) · [作者来源](https://openreview.net/forum?id=F3OUp4tpG4)

- **问题 / 瓶颈** · 从各向同性噪声学习多模态条件速度成本高。
- **核心创新 / 方法** · 以带权核心集构成高斯混合，校正流只拟合近似源到目标的残差。
- **Baseline** · 噪声源层级流匹配。
- **Benchmark** · MNIST、CIFAR-10、ImageNet-32、CelebA-HQ。
- **关键结果 / 消融** · 摘要报告匹配架构下少步生成有竞争力，并给出压缩假设下的输运界。
- **适用条件 / 局限** · 依赖核心集近似质量与条件矩。

**可复用机制** · 在同架构比较噪声源与近似源的运输代价和少步质量。

<a id="paper-149987"></a>

## Coresets for Clustering Using Noisy Comparisons and Few Distance Queries

[官方论文页](https://neurips.cc/virtual/2026/poster/149987) · [作者来源](https://openreview.net/forum?id=lhTqQ3cQIZ)

- **问题 / 瓶颈** · 经典算法通常假设能访问全部距离。
- **核心创新 / 方法** · 用有噪比较实现几何环分组与均匀采样，再做标准核心集压缩。
- **Baseline** · 全距离访问核心集及此前常数因子预言机方法。
- **Benchmark** · 欧氏空间的 $(k,z)$ 聚类与查询开销。
- **关键结果 / 消融** · 核心集大小匹配经典界，所需距离查询随输入大小仅多对数增长。
- **适用条件 / 局限** · 需要四元比较与少量距离查询，噪声条件待核。

**可复用机制** · 分别计比较次数和直接距离次数，选择采样协议。

<a id="paper-152055"></a>

## Cornerstones or Stumbling Blocks? Deciphering the Rock Tokens in On-Policy Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/152055) · [作者来源](https://openreview.net/forum?id=VqAeYOsISa)

- **问题 / 瓶颈** · 高 KL 与高梯度不一定对应推理贡献。
- **核心创新 / 方法** · 追踪持久高损失 token，并用因果干预估计功能贡献。
- **Baseline** · 标准等权的在线策略蒸馏。
- **Benchmark** · 蒸馏过程中生成序列、梯度份额及推理任务。
- **关键结果 / 消融** · 摘要报告此类 token 最多约占一半，因果干预下推理贡献小。
- **适用条件 / 局限** · 规律依赖所测学生和教师，阈值待核。

**可复用机制** · 按损失和干预收益共同选择 token 权重。

<a id="paper-150895"></a>

## CORP: Closed-Form One-shot Representation-Preserving Structured Pruning for Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/150895) · [作者来源](https://openreview.net/forum?id=echydG0ikq)

- **问题 / 瓶颈** · 一次结构剪枝若不复原表示会明显掉点。
- **核心创新 / 方法** · 无标签校准集上用闭式岭回归拟合仿射补偿并折入权重。
- **Baseline** · 无补偿一次剪枝。
- **Benchmark** · ImageNet、DeiT 分类，测 Top-1。
- **关键结果 / 消融** · DeiT-Huge 同时剪去 50% 两类结构后达 83.27%。
- **适用条件 / 局限** · 补偿依赖校准分布。

**可复用机制** · 固定稀疏度检验是否需要对剪去通道做回归补偿。

<a id="paper-153790"></a>

## Correctable Fork Tokens: Verifier-Anchored Selective Credit Assignment for Tool-Integrated RLVR

[官方论文页](https://neurips.cc/virtual/2026/poster/153790) · [作者来源](https://openreview.net/forum?id=IeA9ZyY6JF)

- **问题 / 瓶颈** · 序列奖励均摊到每个 token 会稀释关键决策。
- **核心创新 / 方法** · 训练时共享参数的答案条件分支定位分岔，仅缩放验证器给出的优势。
- **Baseline** · GRPO、较大教师的在线策略蒸馏。
- **Benchmark** · BFCL v3/v4、Tau3。
- **关键结果 / 消融** · 多轮准确率较 GRPO 增 4.2/6.5 个百分点；Tau3 增 8.3 点。
- **适用条件 / 局限** · 需要可靠答案及可验证反馈。

**可复用机制** · 分别消融关键位置定位和验证器反馈粒度。

<a id="paper-152214"></a>

## Correct but Unselectable: The Hidden Interface Tax in Multi-Candidate Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/152214) · [作者来源](https://openreview.net/forum?id=Uj1fB00bWb)

- **问题 / 瓶颈** · 候选正确但不可解析时，扩候选数未必有效。
- **核心创新 / 方法** · 将覆盖拆解为原始覆盖和可选覆盖，构造兼容的候选接口。
- **Baseline** · 固定选择器的生成再重排。
- **Benchmark** · GSM8K、competition_math、GPQA Diamond、MMLU-Pro。
- **关键结果 / 消融** · GPQA 从 5.6% 到 19.2%，联合加强生成达到 25.8%。
- **适用条件 / 局限** · 候选格式修复本身未必让选择器选对。

**可复用机制** · 分开记录正确候选出现率、可解析率与最终选中率。

<a id="paper-154255"></a>

## Corrected Integrated Laplace Approximation for Bayesian Inference in Latent Gaussian Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154255) · [作者来源](https://openreview.net/forum?id=F8uu9a7S7t)

- **问题 / 瓶颈** · 非高斯似然下近似后验可能明显偏离。
- **核心创新 / 方法** · 对 ILA 引入重要性校正，支持准蒙特卡洛及梯度采样。
- **Baseline** · 未校正 ILA。
- **Benchmark** · 潜高斯模型的应用示例及超参数 HMC。
- **关键结果 / 消融** · 摘要证明样本数增加时趋于目标后验，并报告误差降低。
- **适用条件 / 局限** · 方差与开销取决于提议分布。

**可复用机制** · 比较校正前后后验误差及每单位计算的有效样本数。

<a id="paper-150994"></a>

## Correction Space Steering for Hallucination Mitigation in Large Vision-Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150994) · [作者来源](https://openreview.net/forum?id=diwoFVUWNi)

- **问题 / 瓶颈** · 一个固定向量太粗，全维预测易在未见幻觉上不稳。
- **核心创新 / 方法** · 从激活差分学习修正子空间，在线回归低维坐标。
- **Baseline** · 固定向量及其他推理时幻觉缓解法。
- **Benchmark** · 标准视觉语言幻觉基准，具名待核。
- **关键结果 / 消融** · 摘要报告无需重训骨干即可降低幻觉。
- **适用条件 / 局限** · 受差分数据覆盖及秩选择制约。

**可复用机制** · 在固定骨干上对照全维、固定向量和低秩条件校正。

<a id="paper-154007"></a>

## Corrective Diffusion Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154007) · [作者来源](https://openreview.net/forum?id=Gteb9OmhzF)

- **问题 / 瓶颈** · 只学解掩码难识别已显示内容中的错误。
- **核心创新 / 方法** · 训练错误识别置信度，引导局部修订并保留正确内容。
- **Baseline** · 原模型及标准掩码扩散微调。
- **Benchmark** · Code Revision Benchmark、数学推理和 ParallelBench。
- **关键结果 / 消融** · 匹配算力数据时摘要报告修订与生成均改善。
- **适用条件 / 局限** · 依赖训练错误分布覆盖真实生成错误。

**可复用机制** · 同时测错误定位、正确内容保留及生成质量。

<a id="paper-152258"></a>

## Correct, Route, Calibrate: Efficient Preference Optimization from Noisy, Heterogeneous Human Feedback

[官方论文页](https://neurips.cc/virtual/2026/poster/152258) · [作者来源](https://openreview.net/forum?id=UOoH4aqCJg)

- **问题 / 瓶颈** · 异质可靠性造成偏好估计偏差，非随机路由又影响标注员评价。
- **核心创新 / 方法** · 后验校正标签，按信息量分配任务，以双稳健估计纠正选择偏差。
- **Baseline** · 常规 DPO 及可靠性估计对照。
- **Benchmark** · UltraFeedback 半合成标注和 AlpacaEval 2。
- **关键结果 / 消融** · 摘要报告偏好恢复及下游表现改善，可靠性估计误差下降。
- **适用条件 / 局限** · 半合成噪声未必代表真实标注。

**可复用机制** · 固定人评预算比较随机与信息路由，并校正选择偏差。

<a id="paper-151628"></a>

## Correlating Cross-Iteration Noise for DP-SGD using Model Curvature

[官方论文页](https://neurips.cc/virtual/2026/poster/151628) · [作者来源](https://openreview.net/forum?id=Z96zEg7guN)

- **问题 / 瓶颈** · 噪声既改梯度估计，也会改变下一步求梯度的位置。
- **核心创新 / 方法** · 把位置移动影响加入相关噪声优化，用公共数据估 Hessian 上界。
- **Baseline** · DP-BandMF。
- **Benchmark** · 视觉和自然语言任务的差分隐私训练。
- **关键结果 / 消融** · 摘要报告在多个任务提升准确率。
- **适用条件 / 局限** · 依赖曲率估计，具体隐私预算和增益待核。

**可复用机制** · 固定隐私预算比较只校正梯度与同时计入轨迹偏移。

<a id="paper-149327"></a>

## Correlation-Aware Contextual Bandits with Surrogate Rewards for LLM Routing

[官方论文页](https://neurips.cc/virtual/2026/poster/149327) · [作者来源](https://openreview.net/forum?id=qwKrlELWvB)

- **问题 / 瓶颈** · 直接混合代理奖励可能引入系统偏差。
- **核心创新 / 方法** · 独立估计两类反馈并适应性混合预测，另给出奖励直接混合版本。
- **Baseline** · 标准上下文赌博机和静态路由。
- **Benchmark** · 模型路由准确率与成本权衡评测及遗憾分析。
- **关键结果 / 消融** · 摘要报告代理错设时仍可接近只用真实奖励的保证。
- **适用条件 / 局限** · 依赖臂相关结构和代理信号质量。

**可复用机制** · 扫代理偏差并比较分离预测与直接奖励混合。

<a id="paper-151032"></a>

## Correpondence Alignment For Improved Virtual Try-On

[官方论文页](https://neurips.cc/virtual/2026/poster/151032) · [作者来源](https://openreview.net/forum?id=dTXhiKHb4G)

- **问题 / 瓶颈** · 生成器隐式学到的对应可能丢失衣服细节。
- **核心创新 / 方法** · 蒸馏外部可靠匹配，并以熵最小化集中跨图注意力。
- **Baseline** · 未经显式对齐的 DiT 基线。
- **Benchmark** · 虚拟试衣形状与局部保真，含视觉语言评判协议。
- **关键结果 / 消融** · 作者报告形状和细节改善，具体数值待核。
- **适用条件 / 局限** · 依赖外部匹配质量与自动评判校准。

**可复用机制** · 固定生成器，对照可靠对应监督和注意力熵约束。

<a id="paper-155477"></a>

## Correspondence Pruning by Iterative Structural Rectification

[官方论文页](https://neurips.cc/virtual/2026/poster/155477) · [作者来源](https://openreview.net/forum?id=5J1rwV6KnM)

- **问题 / 瓶颈** · 特征改变后早期邻域与分组会过时。
- **核心创新 / 方法** · 每层按特征重建近邻图与原型软分组。
- **Baseline** · 冻结分配及强注意力匹配器。
- **Benchmark** · YFCC100M、SUN3D 与 HPatches，测几何估计精度和耗时。
- **关键结果 / 消融** · 冻结分配损失超过 30% mAP，完整模型较最强注意力对照提高 8.2% mAP@5°且快 35%。
- **适用条件 / 局限** · 结果依赖特征、邻域预算和所用几何任务。

**可复用机制** · 先比较重建结构的频率，再决定是否换更复杂算子。

<a id="paper-155914"></a>

## CorridorLight: Cooperation as Task Negotiation with Causal Gating for Traffic Signal Control

[官方论文页](https://neurips.cc/virtual/2026/poster/155914) · [作者来源](https://openreview.net/forum?id=1rJLK6fsvX)

- **问题 / 瓶颈** · 路网联合动作空间随路口数量迅速扩大。
- **核心创新 / 方法** · 高层周期生成互不重叠的走廊任务，路口以反事实净收益门控协作。
- **Baseline** · 协作交通信号控制基线。
- **Benchmark** · 合成网格与真实路网拓扑下的交通控制实验。
- **关键结果 / 消融** · 作者报告多种需求下系统表现改善，幅度待核。
- **适用条件 / 局限** · 真实路网不等于真实部署，依赖车道图及任务周期。

**可复用机制** · 在相同调度频率下比较固定协作与按净收益协作。

<a id="paper-152688"></a>

## Corrupted Plans, Clean Traces: What Planning-Execution Decoupling Reveals About CoT Monitoring

[官方论文页](https://neurips.cc/virtual/2026/poster/152688) · [作者来源](https://neurips.cc/virtual/2026/poster/152688)

- **问题 / 瓶颈** · 表面正常的解释和实际任务行为可能不一致。
- **核心创新 / 方法** · 比较不同推理配置的监察器，检查解释判断能否预测异常行为。
- **Baseline** · 有推理与无推理监察器。
- **Benchmark** · 语言模型监控实验，评估异常检测及预算变化。
- **关键结果 / 消融** · 推理监察器总体较好，但增加预算的效果不单调，且仍有漏报。
- **适用条件 / 局限** · 限于作者测试的设置，部署中的误报与延迟仍需测。

**可复用机制** · 监察系统应同时验收行为结果，并对监察预算单独扫描漏报率。

<a id="paper-156659"></a>

## Corruptions of Supervised Learning Problems: Typology and Mitigations

[官方论文页](https://neurips.cc/virtual/2026/poster/156659) · [作者来源](https://neurips.cc/virtual/2026/poster/156659)

- **问题 / 瓶颈** · 分散的数据损坏模型难解释不同校正方法何时适用。
- **核心创新 / 方法** · 以 Markov 核刻画分布变动，比较干净和损坏下的 Bayes 风险并推导校正。
- **Baseline** · 经典标签损失修正。
- **Benchmark** · 理论设定覆盖标签、属性和联合扰动。
- **关键结果 / 消融** · 标签扰动仅改变损失，而属性扰动还改变有效假设族。
- **适用条件 / 局限** · 依赖监督学习与扰动模型假设。

**可复用机制** · 分布变化后检查可用假设族是否同时改变，再选校正方法。

<a id="paper-154557"></a>

## CORTEG: Foundation Models Enable Cross-Modality Representation Transfer from Scalp to Intracranial Brain Recordings

[官方论文页](https://neurips.cc/virtual/2026/poster/154557) · [作者来源](https://openreview.net/forum?id=ChfliH0uB0)

- **问题 / 瓶颈** · 颅内记录的个体数据少，传感器布局与头皮脑电不同。
- **核心创新 / 方法** · 预训练脑电骨干结合电极位置适配器、双频词元及留一受试者微调。
- **Baseline** · 任务专用解码器。
- **Benchmark** · 公开手指轨迹回归与私有音频包络回归，受试者数为 9 和 16。
- **关键结果 / 消融** · 音频任务增益显著，手指任务领先但差异不显著；校准用单卡 10–30 分钟。
- **适用条件 / 局限** · 样本少，私有数据结果的外部复验受限。

**可复用机制** · 传感器迁移中分开比较空间对齐和频带建模，在未见受试者上测试。

<a id="paper-152414"></a>

## Cortically-Resolved Recurrent Architecture for fMRI

[官方论文页](https://neurips.cc/virtual/2026/poster/152414) · [作者来源](https://openreview.net/forum?id=TIdiRMJ2QV)

- **问题 / 瓶颈** · 统一时序算子掩盖不同区域的时间尺度。
- **核心创新 / 方法** · 各区域有独立循环参数和可微软记忆窗口，跨区交互经身份感知注意力。
- **Baseline** · 区域级脑影像解码模型。
- **Benchmark** · NSD 刺激分类、ABIDE 和 COBRE 诊断。
- **关键结果 / 消融** · 作者报告成绩可比，所学尺度具有可解释的空间组织。
- **适用条件 / 局限** · 尺度解释仍需独立生理验证。

**可复用机制** · 固定空间建模，比较共享和区域独立时序核并验证解释稳定性。

<a id="paper-149092"></a>

## CORVUS: Context Optimization and Reduction Via Underlying Synchronization for LLM Coding Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/149092) · [作者来源](https://openreview.net/forum?id=sxZjrxwU2k)

- **问题 / 瓶颈** · 追加式轨迹保存过期文件快照并重复占用上下文。
- **核心创新 / 方法** · 保留相关文件注册表，每轮只注入文件现有内容。
- **Baseline** · 保留历史读文件结果的常规追加式轨迹。
- **Benchmark** · SWE-POLYBENCH_VERIFIED、SWE-BENCH PRO，四种语言模型。
- **关键结果 / 消融** · 平均输入 token 降 9–50%，最终提示缩短 15–32%，通过率可比。
- **适用条件 / 局限** · 需可靠感知文件修改，调试历史状态另需保留。

**可复用机制** · 将可变工作状态与事件序列分离，分别测过期读取和 token 开销。

<a id="paper-150611"></a>

## COSAC: Counterfactual Credit Assignment in Sequential Cooperative Teams

[官方论文页](https://neurips.cc/virtual/2026/poster/150611) · [作者来源](https://openreview.net/forum?id=gs2iunr5fs)

- **问题 / 瓶颈** · 联合评估器或重要性采样在长团队中成本或方差较高。
- **核心创新 / 方法** · 对每个成员的贡献做岭回归分解，通过当前策略前向生成反事实后续。
- **Baseline** · 共享奖励及其他无评估器方法。
- **Benchmark** · 最多 16 个成员的顺序赌博机与四智能体 ARC。
- **关键结果 / 消融** · 赌博机优势 MSE 最低，ARC 收敛更快；量化幅度待核。
- **适用条件 / 局限** · 依赖固定动作顺序，强非加性交互仍应检查偏差。

**可复用机制** · 固定环境调用预算，对照个体信用信号与共享团队奖励。

<a id="paper-151869"></a>

## CoScan: Multi-Scale Content-Adaptive Space-Filling Scans for Causal State-Space Image Restoration

[官方论文页](https://neurips.cc/virtual/2026/poster/151869) · [作者来源](https://openreview.net/forum?id=XHd7CqQtoF)

- **问题 / 瓶颈** · 固定二维转一维的顺序可能打断相邻语义信息。
- **核心创新 / 方法** · 用可微代理监督局部连贯和因果可预测性，通过树粗化构造跨尺度扫描。
- **Baseline** · 固定扫描的 Mamba 图像恢复骨干。
- **Benchmark** · 多种图像恢复基准和高层视觉任务，名称待核。
- **关键结果 / 消融** · 作者报告多种恢复任务有增益且新增开销小。
- **适用条件 / 局限** · 依赖扫描代理与任务相关，跨设备耗时待核。

**可复用机制** · 对固定骨干切换扫描路径，测退化强度变化下的恢复质量及延迟。

<a id="paper-139285"></a>

## Cosine is Human: The Reproducibility Ceiling of Perceptual Similarity

[官方论文页](https://neurips.cc/virtual/2026/poster/139285) · [作者来源](https://openreview.net/forum?id=ZQ6YtLisva)

- **问题 / 瓶颈** · 只报告一致案例准确率会高估对人类新判断的泛化。
- **核心创新 / 方法** · 在全量三元组按票差分层，做投票拆半重测并比较相似和同异协议。
- **Baseline** · 十一种方法，含冻结余弦、LoRA 与 DreamSim。
- **Benchmark** · NIGHTS 的 64,420 个非平票三元组及共享刺激。
- **关键结果 / 消融** · 冻结余弦 74.1%，DreamSim 80.7%；总体投票重现率仅 70.1%。
- **适用条件 / 局限** · 拆半是重测估计，受所用投票数与人群限制。

**可复用机制** · 声明对齐人类前加独立人评重测，区分拟合既有票与预测新票。

<a id="paper-139351"></a>

## COSMIO: A Benchmark for Cross-Survey Modality Imputation

[官方论文页](https://neurips.cc/virtual/2026/poster/139351) · [作者来源](https://openreview.net/forum?id=UwoE2LI1HF)

- **问题 / 瓶颈** · 普通样本补全精度不能反映稀有科学对象是否保留。
- **核心创新 / 方法** · 对同一天体场景模拟不同巡天仪器观测，测试跨巡天缺失模式和罕见强引力透镜。
- **Baseline** · 多种已有模态补全方法。
- **Benchmark** · LSST、Euclid、Roman 的对齐模拟观测与透镜检测。
- **关键结果 / 消融** · 模型迁移不佳，罕见样本补全退化传导至下游检测。
- **适用条件 / 局限** · 模拟仪器与实际巡天之间仍有差异。

**可复用机制** · 给跨传感补全加入低频事件专门留出集，并在最终科学任务上验收。

<a id="paper-151916"></a>

## Cost-Aware Best-LLM Identification using Dueling Feedback

[官方论文页](https://neurips.cc/virtual/2026/poster/151916) · [作者来源](https://openreview.net/forum?id=WwFT9uaTpj)

- **问题 / 瓶颈** · 固定评估轮数忽略模型调用的成本差异。
- **核心创新 / 方法** · 把模型选型写成异成本对决赌博机，用 Track-and-Stop 分配查询。
- **Baseline** · 经典不考虑成本算法及其成本敏感变体。
- **Benchmark** · 合成与真实模型偏好样本，测给定错误率的查询成本。
- **关键结果 / 消融** · 在存在 Condorcet 胜者时取得渐近最优成本，作者报告实证改善。
- **适用条件 / 局限** · 偏好循环或调用费用波动时，理论需重新验证。

**可复用机制** · 先查是否有普遍胜者，再用固定置信度比较总成本。

<a id="paper-151093"></a>

## Cost-Aware Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151093) · [作者来源](https://openreview.net/forum?id=d1T390yy1T)

- **问题 / 瓶颈** · 等量抽样可能把多数计算花在高成本低贡献样本。
- **核心创新 / 方法** · 以梯度范数和成本构造采样，大模型强化学习中用优势幅值作梯度代理。
- **Baseline** · 常规 SGD 采样及 GRPO。
- **Benchmark** · 有限和目标理论及 1.5B、4B、8B 模型策略优化。
- **关键结果 / 消融** · 作者报告减少优化 token 同时保持或改善准确率，幅度待核。
- **适用条件 / 局限** · 代理贡献随任务和训练阶段变化。

**可复用机制** · 度量达到同质量的实际成本，单独核对样本价值代理的排序。

<a id="paper-153329"></a>

## Cost Efficient Fairness Audit Under Partial Feedback

[官方论文页](https://neurips.cc/virtual/2026/poster/153329) · [作者来源](https://openreview.net/forum?id=M86rt803hI)

- **问题 / 瓶颈** · 部分反馈造成公平估计缺失，而补取真实标签成本不一。
- **核心创新 / 方法** · 分别设计黑箱近最优审计和利用指数族混合假设的审计。
- **Baseline** · 随机探索及自然补采方法。
- **Benchmark** · Adult Income、Law School，比较审计成本，覆盖常用公平指标。
- **关键结果 / 消融** · 作者报告审计成本约低 50%。
- **适用条件 / 局限** · 混合模型需分布假设，补采成本应重新估计。

**可复用机制** · 把标签缺失机制与获取成本写进公平审计方案并做敏感性分析。

<a id="paper-149885"></a>

## CoT-Guard: Small Models for Strong Monitoring

[官方论文页](https://neurips.cc/virtual/2026/poster/149885) · [作者来源](https://neurips.cc/virtual/2026/poster/149885)

- **问题 / 瓶颈** · 长轨迹让高容量监察器部署成本偏高。
- **核心创新 / 方法** · 通过强监察器蒸馏与困难场景后训练提升小模型的异常识别。
- **Baseline** · GPT-5.4、GPT-5-mini、Qwen3-32B、Gemini-3-Flash。
- **Benchmark** · 代码生成监察，以真负率乘真阳性率评估。
- **关键结果 / 消融** · 4B 模型报告 75%，Gemini-3-Flash 为 83%。
- **适用条件 / 局限** · 测试协议和真实环境的误报与成本边界待核。

**可复用机制** · 在相同监察预算下比较大模型和专用小模型，同时测漏报和误报。

<a id="paper-154397"></a>

## CoTrek: Toward Scalable On-Policy Distillation for Long Chain-of-Thought Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/154397) · [作者来源](https://openreview.net/forum?id=DsDVXNgrHK)

- **问题 / 瓶颈** · 完整后缀模仿把修复错误路径与继续解题混在一起。
- **核心创新 / 方法** · 从学生已偏离的深前缀采样教师恢复，提取共享修复段，配合深度课程。
- **Baseline** · 强在策略蒸馏基线。
- **Benchmark** · 长推理基准及更深前缀设置，测精度、恢复与 pass@k。
- **关键结果 / 消融** · 作者报告最终精度与恢复最高分别改善 6.84% 和 9.27%。
- **适用条件 / 局限** · 需可由教师恢复的前缀及可靠的修复提取。

**可复用机制** · 控制教师采样预算，对照完整后缀和短纠错目标。

<a id="paper-151761"></a>

## CoTs as Probabilistic Programs: A Programmatic View of Thinking Step-by-Step in Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151761) · [作者来源](https://openreview.net/forum?id=YEVrT8IA3J)

- **问题 / 瓶颈** · 高似然轨迹不一定支持正确推理。
- **核心创新 / 方法** · 将步骤建模为随机选择、分支建模依赖，再用可微算子组合反馈与轨迹得分。
- **Baseline** · 仅以轨迹似然打分的分析。
- **Benchmark** · 小型离散程序语义及多项案例，具体量化设置待核。
- **关键结果 / 消融** · 案例展示似然打分的局限与逐步敏感度分析。
- **适用条件 / 局限** · 简化程序语义与真实模型长轨迹之间有差距。

**可复用机制** · 解释推理时分别测执行概率、答案贡献和关键步骤敏感性。

<a id="paper-155458"></a>

## Counterfactual Debugging the World Model Transfer Gap

[官方论文页](https://neurips.cc/virtual/2026/poster/155458) · [作者来源](https://openreview.net/forum?id=5SUeNVcFWj)

- **问题 / 瓶颈** · 最大的视觉误差不一定解释部署性能差。
- **核心创新 / 方法** · 用分治式反事实归因在真实轨迹中寻找关键转移或奖励误差。
- **Baseline** · 统计或视觉误差排序；具名对照待核。
- **Benchmark** · 合成注入观测偏差、奖励偏差及物理偏差的多个环境。
- **关键结果 / 消融** · 作者报告定位关键错误且利用稀疏性显著降低计算。
- **适用条件 / 局限** · 需要有效对照轨迹，密集相互作用错误的开销待核。

**可复用机制** · 按纠正误差后是否改善策略排序来决定下一步模型修复。

<a id="paper-154297"></a>

## Counterfactual Distillation: Internalizing Reflective Experience into LLM Agent

[官方论文页](https://neurips.cc/virtual/2026/poster/154297) · [作者来源](https://openreview.net/forum?id=Eme3GC4jGU)

- **问题 / 瓶颈** · 仅凭最终奖励会集中强化少数已有成功行为。
- **核心创新 / 方法** · 树形探索中重新审视过去决策，以修改动作监督原状态，测试时无需额外反馈。
- **Baseline** · GRPO、Early Experience。
- **Benchmark** · 交互编码和通用智能体任务，测 pass@128 与 pass@1。
- **关键结果 / 消融** · 作者报告 pass@128 改善最高 14%，和强化学习交替时 pass@1 改善超过 10%。
- **适用条件 / 局限** · 依赖可靠反思与充分分支覆盖。

**可复用机制** · 固定环境调用预算，对照结果奖励与显式修正监督对解法覆盖的影响。

<a id="paper-151311"></a>

## Counterfactual Estimation under Composite Treatments via Progressive Distribution Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/151311) · [作者来源](https://openreview.net/forum?id=bQvJDLN27X)

- **问题 / 瓶颈** · 组合稀疏且混杂相互交织。
- **核心创新 / 方法** · 逆拓扑次序按父节点条件做增广，逐步最小化 KL。
- **Baseline** · 七种对照及最近方法消融。
- **Benchmark** · IHDP、Twins、Hillstrom 半合成和受控模拟。
- **关键结果 / 消融** · 摘要报告稀有组合收益最大。
- **适用条件 / 局限** · 依赖因果图及覆盖条件。

**可复用机制** · 按组合稀有度检验图分解的增广收益。

<a id="paper-155627"></a>

## Counterfactual Explanations for Time-Series Classification via Constrained Flow Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/155627) · [作者来源](https://openreview.net/forum?id=4BQToRUDBl)

- **问题 / 瓶颈** · 分类梯度不可用且单类任务难处理。
- **核心创新 / 方法** · 学习随流时间变化的目标区间，推理用局部编辑和投影纠偏。
- **Baseline** · 梯度式方案，具体对照待核。
- **Benchmark** · UCR 分类任务与个案。
- **关键结果 / 消融** · 报告定量和定性效果；证明理想边缘匹配时风险等价。
- **适用条件 / 局限** · 依赖生成器和目标区间质量。

**可复用机制** · 比较仅标签接口下的反事实有效性与编辑范围。

<a id="paper-152584"></a>

## Counterfactual Instruction Grounding for Vision-Language-Action Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152584) · [作者来源](https://openreview.net/forum?id=S0PONpfMze)

- **问题 / 瓶颈** · 窄域模仿可能使后段动作摆脱语言约束。
- **核心创新 / 方法** · 用反事实指令做对比目标，自回归用动作似然，流模型用能量近似。
- **Baseline** · 已微调 VLA；具名对照待核。
- **Benchmark** · RoboCasa、LIBERO-Plus 和真实厨房。
- **关键结果 / 消融** · 两基准成功率 71.3% 和 86.3%。
- **适用条件 / 局限** · 依赖反事实指令质量。

**可复用机制** · 以相同场景替换指令，测轨迹是否仍能区分指令。

<a id="paper-153015"></a>

## Counterfactual Maps: What They Are and How to Find Them

[官方论文页](https://neurips.cc/virtual/2026/poster/153015) · [作者来源](https://openreview.net/forum?id=Oc0x3mRg64)

- **问题 / 瓶颈** · 冷启动优化延迟高，启发式不保证最优。
- **核心创新 / 方法** · 将分区压缩成带标签超矩形，用体积 KD 树分支定界。
- **Baseline** · 启发式和混合整数优化。
- **Benchmark** · 多个真实数据集，测最优性和查询延迟。
- **关键结果 / 消融** · 作者报告毫秒级精确查询。
- **适用条件 / 局限** · 需要预处理；最坏情况和存储成本待核。

**可复用机制** · 多次查询同一模型时用预处理换在线延迟，并保留最优证书。

<a id="paper-150109"></a>

## Counterfactual Online Conformal Prediction Under Adaptive Logging

[官方论文页](https://neurips.cc/virtual/2026/poster/150109) · [作者来源](https://openreview.net/forum?id=kcz4dJYi4k)

- **问题 / 瓶颈** · 罕选动作的覆盖可能被总体覆盖掩盖。
- **核心创新 / 方法** · 逆倾向递推校准，双稳健版本将偏差变为两种误差乘积。
- **Baseline** · 标准自适应共形预测。
- **Benchmark** · 合成决策、开放赌博机数据、金融再平衡。
- **关键结果 / 消融** · 覆盖速率在对数因子内匹配下界，作者报告覆盖和遗憾改善。
- **适用条件 / 局限** · 需要正性，极稀有行动权重不稳。

**可复用机制** · 部署后按行动分别审计覆盖并检查日志倾向。

<a id="paper-148259"></a>

## Counterfactual Predictive State Representations: The Intrinsic Dimension of Partial-Information Games

[官方论文页](https://neurips.cc/virtual/2026/poster/148259) · [作者来源](https://openreview.net/forum?id=zBs8IFbJ3b)

- **问题 / 瓶颈** · 可观测轨迹复杂度可高估决策所需状态。
- **核心创新 / 方法** · 将可行信念按查询不可区分性取商，得到最小实现和更新算子。
- **Baseline** · 有限秩预测状态等为特例。
- **Benchmark** · 有限时域双人零和完美记忆博弈，理论验证。
- **关键结果 / 消融** · 给出维数等价、滚动样本界及指数分离例子。
- **适用条件 / 局限** · 要求指定博弈与局部设计条件。

**可复用机制** · 压缩状态时以行动相关查询的有效秩替代完整轨迹数量。

<a id="paper-151386"></a>

## Counterfactual Rollout Replay: Forkable Environments as Free Process Rewards for Software Engineering Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/151386) · [作者来源](https://openreview.net/forum?id=b0yS7nonHU)

- **问题 / 瓶颈** · 长程代码维护的终局奖励难区分中间决策。
- **核心创新 / 方法** · 从选定决策点重放备选动作，以回报差标记该步优势。
- **Baseline** · 仅终局奖励的 GRPO。
- **Benchmark** · SWE-Gym 训练，SWE-bench Verified 和 SWE-rebench 评测。
- **关键结果 / 消融** · 摘要报告用更少轨迹提高问题解决率。
- **适用条件 / 局限** · 需要可复现环境并支付额外重放计算。

**可复用机制** · 在常规软件维护训练中以匹配执行成本比较终局和局部分支信用。

<a id="paper-148627"></a>

## CounterFlowNet: From Minimal Changes to Meaningful Counterfactual Explanations

[官方论文页](https://neurips.cc/virtual/2026/poster/148627) · [作者来源](https://openreview.net/forum?id=wL6SWD7afK)

- **问题 / 瓶颈** · 混合表格数据难同时实现稀疏、有效及可行。
- **核心创新 / 方法** · 将反事实写成 GFlowNet 的逐特征编辑，推理用动作掩码。
- **Baseline** · 表格反事实生成基线，名称待核。
- **Benchmark** · 八个数据集，两种协议。
- **关键结果 / 消融** · 摘要报告质量折衷改善且满足指定约束。
- **适用条件 / 局限** · 奖励定义决定样本分布。

**可复用机制** · 将不可修改和单调约束留在解码接口，可在固定模型上更换。

<a id="paper-139606"></a>

## CounterStrike-1K: A Multi-Perspective Dataset of Professional Gameplay for World Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/139606) · [作者来源](https://openreview.net/forum?id=FsEoZwUHsR)

- **问题 / 瓶颈** · 单视角画面合理不代表跨视角状态一致。
- **核心创新 / 方法** · 对游戏回放同步所有参与者观测并对齐动作和场景状态。
- **Baseline** · 互联网视频与模拟 rollout 为数据来源对照。
- **Benchmark** · 七张游戏地图、1490 小时视图，评测检索和共享状态恢复。
- **关键结果 / 消融** · 提供固定划分；摘要未报对照分数。
- **适用条件 / 局限** · 仅限游戏环境。

**可复用机制** · 跨智能体预测需单独评估共享状态恢复。

<a id="paper-150435"></a>

## Counting without Scale: Scale-Consistent Error Correction for Crowd Counting

[官方论文页](https://neurips.cc/virtual/2026/poster/150435) · [作者来源](https://openreview.net/forum?id=i4EGsPX5qd)

- **问题 / 瓶颈** · 尺度变化与标签噪声会导致计数不稳。
- **核心创新 / 方法** · 约束同场景不同尺度密度图并以概率模型估计标注不确定性。
- **Baseline** · CrowdDiff、Steerer、CrowdFormer。
- **Benchmark** · 五个计数数据集，测 MAE 与跨集泛化。
- **关键结果 / 消融** · 报告 MAE 降 5–7%，多尺度项最多降 15%。
- **适用条件 / 局限** · 收益依赖噪声假设。

**可复用机制** · 分别消融监督一致性和噪声校正。

<a id="paper-155294"></a>

## CoupledFlow: One-Step Neural Operators for Coupled Multi-Physics PDEs

[官方论文页](https://neurips.cc/virtual/2026/poster/155294) · [作者来源](https://openreview.net/forum?id=6eIWOGXqT1)

- **问题 / 瓶颈** · 独立算子遗漏双向耦合。
- **核心创新 / 方法** · 以一步生成算子拟合各过程的平均速度并共享完整条件。
- **Baseline** · 耦合算子与生成 PDE 基线。
- **Benchmark** · 多个多物理基准，指标待核。
- **关键结果 / 消融** · 给出 Wasserstein-2 界并报告实验改善。
- **适用条件 / 局限** · 依赖流的正则性和联合状态可见。

**可复用机制** · 同预算比较独立更新与全状态条件化。

<a id="paper-153836"></a>

## Coupled Guidance for Flow Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/153836) · [作者来源](https://openreview.net/forum?id=IMU91e91Zo)

- **问题 / 瓶颈** · 照搬扩散引导可能破坏训练耦合。
- **核心创新 / 方法** · 从几何角度利用流匹配固有耦合设计引导。
- **Baseline** · 移植扩散引导的流匹配方法。
- **Benchmark** · ManiSkill3、Adroit、ImageNet-128、CelebA-HQ-256。
- **关键结果 / 消融** · 摘要报告质量与稳定性改善，无额外开销。
- **适用条件 / 局限** · 依赖耦合结构；数值待核。

**可复用机制** · 更换生成参数化后先检查引导是否保持训练分布。

<a id="paper-153205"></a>

## Coupled Integral PINN for Discontinuity

[官方论文页](https://neurips.cc/virtual/2026/poster/153205) · [作者来源](https://openreview.net/forum?id=N3iBY93EZ6)

- **问题 / 瓶颈** · 点态 PDE 残差对不连续解不稳。
- **核心创新 / 方法** · 加辅助积分势网络和耦合积分约束。
- **Baseline** · 标准 PINN；有限体积为方法动机。
- **Benchmark** · Burgers、Buckley–Leverett、Euler、浅水方程。
- **关键结果 / 消融** · 报告激波附近更稳，幅度待核。
- **适用条件 / 局限** · 依赖守恒形式及辅助势拟合。

**可复用机制** · 用积分弱约束对照逐点损失，单独检查间断区域。

<a id="paper-154400"></a>

## Coupling-Aware Reinforcement Learning for Co-Evolving Graph Games

[官方论文页](https://neurips.cc/virtual/2026/poster/154400) · [作者来源](https://openreview.net/forum?id=DrGKhgoPSC)

- **问题 / 瓶颈** · 大规模不规则图中无掩码交互与 PPO 难稳定协同。
- **核心创新 / 方法** · 跨图注意力掩码配策略镜像下降。
- **Baseline** · 仅自身、无掩码及 PPO 变体。
- **Benchmark** · 三类奖励域及多种网络规模。
- **关键结果 / 消融** · 作者报告难规模下仍有效，并给出累计漂移上界。
- **适用条件 / 局限** · 需要已知跨图结构。

**可复用机制** · 单独消融结构掩码和更新规则，按网络规模验收。

<a id="paper-154013"></a>

## Coupling Models for One-Step Discrete Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/154013) · [作者来源](https://openreview.net/forum?id=GrxkmHsKwU)

- **问题 / 瓶颈** · 迭代生成较慢且一步蒸馏依赖教师。
- **核心创新 / 方法** · 为离散样本学习高斯潜量耦合，并训练直接解码器。
- **Baseline** · 最强一步生成基线。
- **Benchmark** · LM1B 文本和 MNIST-Binary。
- **关键结果 / 消融** · 报告困惑度降 33%，二值图像 FID 降 46%。
- **适用条件 / 局限** · 结果依赖选择的操作点。

**可复用机制** · 固定一次前向预算比较学习耦合与手设耦合。

<a id="paper-153186"></a>

## Covariate-Adjusted Deep Causal Learning for Heterogeneous Panel Data Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153186) · [作者来源](https://openreview.net/forum?id=NBIkiyBee2)

- **问题 / 瓶颈** · 单元差异与时间依赖会破坏简单插补。
- **核心创新 / 方法** · 用前馈网络与多输出自编码器建模，再进行结构化矩阵补全。
- **Baseline** · 摘要未列具名对照。
- **Benchmark** · 模拟及真实面板应用。
- **关键结果 / 消融** · 给出收敛保证并报告插补改善。
- **适用条件 / 局限** · 依赖潜结构和识别条件。

**可复用机制** · 分别消融协变量非线性与共享时序因子。

<a id="paper-155540"></a>

## COVD: Continual Open-Vocabulary Object Detection with Novel Concept Injection

[官方论文页](https://neurips.cc/virtual/2026/poster/155540) · [作者来源](https://openreview.net/forum?id=4of16OWJXb)

- **问题 / 瓶颈** · 新类不断出现且全量重训贵。
- **核心创新 / 方法** · 用旧类文本保持文本空间，再选择性更新文本分支。
- **Baseline** · 视觉语言持续学习方法。
- **Benchmark** · Novel-114，评估新类注入、旧类保持和开放词汇。
- **关键结果 / 消融** · 报告新旧类表现改善且无需新增参数。
- **适用条件 / 局限** · 要求视觉底座已表征新概念。

**可复用机制** · 先测视觉可分性，再判断是否只需修改语义接口。

<a id="paper-154675"></a>

## Coverage-Based Calibration for Post-Training Quantization via Weighted Maximum Coverage over Outlier Channels

[官方论文页](https://neurips.cc/virtual/2026/poster/154675) · [作者来源](https://openreview.net/forum?id=BsTRAPk0F8)

- **问题 / 瓶颈** · 随机采样易遗漏稀有高幅激活通道。
- **核心创新 / 方法** · 缓存模块级激活掩码，按重构敏感度加权后贪心最大覆盖。
- **Baseline** · AWQ 和 GPTQ，固定池及随机校准。
- **Benchmark** · LLaMA-2、LLaMA-3、Mistral，五项下游评测。
- **关键结果 / 消融** · AWQ 128 样本下 MMLU 提升 1.2–1.5 点。
- **适用条件 / 局限** · 阈值和加权近似需随模型核对。

**可复用机制** · 固定校准预算扫描稀有通道覆盖率与下游质量。

<a id="paper-155083"></a>

## Coverage-Verified Sparse Attention: Closed-Loop Quality Control for Long-Context LLM Decoding

[官方论文页](https://neurips.cc/virtual/2026/poster/155083) · [作者来源](https://openreview.net/forum?id=8Z6u3YSO1c)

- **问题 / 瓶颈** · 固定 KV 子集没有质量反馈。
- **核心创新 / 方法** · 用保留 softmax 质量同时作为验收条件和恢复插值权重。
- **Baseline** · 开环稀疏注意力及密集注意力。
- **Benchmark** · LongBench、RULER，7B 和 70B。
- **关键结果 / 消融** · 作者报告质量接近密集对照，128K 吞吐最高 6.21 倍。
- **适用条件 / 局限** · 实际收益依赖触发频次和核实现。

**可复用机制** · 同预算比较带验证恢复和固定稀疏度推理。

<a id="paper-152458"></a>

## CoVisIT: Cross-modal Prior Guided Diffusion Model for Visible-to-Infrared Image Translation

[官方论文页](https://neurips.cc/virtual/2026/poster/152458) · [作者来源](https://openreview.net/forum?id=Syljya6tdQ)

- **问题 / 瓶颈** · 单靠可见光无法可靠推断热分布，红外低分辨率且未对齐。
- **核心创新 / 方法** · 潜扩散使用高分辨率可见结构和低分辨率红外约束，动态卷积适配局部错位。
- **Baseline** · 红外超分与可见到红外转换。
- **Benchmark** · 可见和红外图像重建与下游任务，具名基准待核。
- **关键结果 / 消融** · 摘要报告质量提升及下游改善。
- **适用条件 / 局限** · 需要真实低分辨率红外作为锚。

**可复用机制** · 有互补传感器时分别消融结构和测量约束。

<a id="paper-156015"></a>

## CoWorld-VLA: Thinking in a Multi-Expert World Model for Autonomous Driving

[官方论文页](https://neurips.cc/virtual/2026/poster/156015) · [作者来源](https://openreview.net/forum?id=19TafUAsz0)

- **问题 / 瓶颈** · 文本推理难保留连续空间和时间
- **核心创新 / 方法** · 用语义交互、几何、动态和自车轨迹四类专家 token 条件化分层扩散
- **Baseline** · 文本及潜变量推理是讨论对象，具名实验对照待核
- **Benchmark** · NAVSIM v1 的场景生成、轨迹精度和碰撞
- **关键结果 / 消融** · 作者报告有竞争力，消融支持专家互补
- **适用条件 / 局限** · 摘要未给闭环真机证据

**可复用机制** · 逐类移除规划条件以区分几何和交互信息贡献

<a id="paper-150296"></a>

## CPA: Efficient and Stable FP4 RL Training via Cross-Precision Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/150296) · [作者来源](https://openreview.net/forum?id=jCqn6PPPpi)

- **问题 / 瓶颈** · FP4 将训练推理栈数值差异放大为重要性权重偏差
- **核心创新 / 方法** · 保留 BF16 主策略并实际用 FP4 rollout，对采样 token 加跨精度 KL
- **Baseline** · 全 BF16 RL
- **Benchmark** · 端到端训练耗时和性能，任务待核
- **关键结果 / 消融** · BF16 检查点匹配全精度对照并快 8–19%
- **适用条件 / 局限** · 依赖量化栈，误差与硬件边界待核

**可复用机制** · 比较实际 rollout 与训练分布差，而非只验证模拟量化

<a id="paper-151658"></a>

## CP-MLPs: A Tensor-Rank Theory of Tied and Untied MLP Blocks

[官方论文页](https://neurips.cc/virtual/2026/poster/151658) · [作者来源](https://openreview.net/forum?id=Z0avyF5HD7)

- **问题 / 瓶颈** · 共享检测与取值方向的表达代价不清楚
- **核心创新 / 方法** · 将检测、取值、写入建模为秩一张量交互，推导分阶宽度差异
- **Baseline** · ReLU 平方、ReGLU 与 SwiGLU 所代表的结构
- **Benchmark** · 合成交互与同参数门控 MLP
- **关键结果 / 消融** · 非共享对不定二次及角色不对称目标更省宽度，纯幂适合共享
- **适用条件 / 局限** · 精确结论依赖目标阶次与表示设定

**可复用机制** · 增加训练预算前先检查宽度造成的近似下限

<a id="paper-139052"></a>

## Cracks in the Foundation: A Civil Infrastructure Dataset to Challenge Vision Foundation Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139052) · [作者来源](https://openreview.net/forum?id=nxteZPGIxC)

- **问题 / 瓶颈** · 常规图像基准难反映几何缺陷识别
- **核心创新 / 方法** · 用专家标注的基础设施实例分割数据测试视觉模型
- **Baseline** · 零样本视觉基础模型及监督专用分割器
- **Benchmark** · CiF 约十五万高分辨率图像，测 mAP
- **关键结果 / 消融** · 专用模型约在 25% mAP 停滞
- **适用条件 / 局限** · 采集分布和缺陷类别决定迁移边界

**可复用机制** · 对低纹理任务单设几何缺陷切片，比较领域监督能否消除差距

<a id="paper-149960"></a>

## CRAFT: Causal Responsibility and Failure Tracing in Medical Vision Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149960) · [作者来源](https://openreview.net/forum?id=ltg40TysQ2)

- **问题 / 瓶颈** · 同一准确率会混合两类不同故障
- **核心创新 / 方法** · 用因果头干预和时间轨迹验证两类机制能否分离
- **Baseline** · 干预前后和无冲突输入
- **Benchmark** · 多个医学 VQA 基准和视觉语言架构
- **关键结果 / 消融** · 作者报告两类头集合不同且干预效果可分
- **适用条件 / 局限** · 模型内发现不足以证明临床有效性

**可复用机制** · 在固定任务上分别改变证据冲突和视觉质量

<a id="paper-152651"></a>

## CRAFT: Conflict-Resolved Aggregation for Federated Training

[官方论文页](https://neurips.cc/virtual/2026/poster/152651) · [作者来源](https://openreview.net/forum?id=ROxD67Qddn)

- **问题 / 瓶颈** · 均匀平均可能掩盖个别性能下滑
- **核心创新 / 方法** · 把参考方向投影到非负对齐约束，采用闭式和逐层处理
- **Baseline** · FedAvg 及其他联邦对照
- **Benchmark** · 非 IID 与不平衡设置，比较全局精度和差距
- **关键结果 / 消融** · 作者报告差距下降且全局精度有竞争力
- **适用条件 / 局限** · 近零可行更新与抽样影响待核

**可复用机制** · 记录均值和客户端尾部指标，并检查逐层冲突

<a id="paper-150208"></a>

## CRAFT: Counterfactual-to-Interactive Reinforcement Fine-Tuning for Driving Policies

[官方论文页](https://neurips.cc/virtual/2026/poster/150208) · [作者来源](https://openreview.net/forum?id=jvYypWtfPg)

- **问题 / 瓶颈** · 闭环反馈稀疏而反事实监督有偏
- **核心创新 / 方法** · 将同一访问分布下的梯度拆成代理及残差，并向 EMA 教师正则化
- **Baseline** · 闭环和反事实微调，具体设置待核
- **Benchmark** · Bench2Drive 的三类策略架构
- **关键结果 / 消融** · 作者报告闭环增益且消融支持两项互补
- **适用条件 / 局限** · 依赖代理质量和关键交互样本

**可复用机制** · 等交互预算比较单独代理、真实反馈和残差组合

<a id="paper-139437"></a>

## CrafterDojo: A Suite of Foundation Models for Building Open-Ended Embodied Agents in Crafter

[官方论文页](https://neurips.cc/virtual/2026/poster/139437) · [作者来源](https://openreview.net/forum?id=Q7Y8eh12e2)

- **问题 / 瓶颈** · 大型沙箱提高迭代成本
- **核心创新 / 方法** · 自动生成演示及视频语言对，训练可组合基础组件
- **Baseline** · 非层级智能体
- **Benchmark** · Crafter 长程任务，精确指标待核
- **关键结果 / 消融** · 作者报告层级智能体有优势
- **适用条件 / 局限** · 环境较简化，不能直接外推

**可复用机制** · 以同一资产和训练预算验证分层结构的增益

<a id="paper-151168"></a>

## Crafter: Towards Automated Reproducible Machine Learning via Agentic Code Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/151168) · [作者来源](https://openreview.net/forum?id=cWMcK8uzFF)

- **问题 / 瓶颈** · 论文关键细节分散导致一次生成遗漏
- **核心创新 / 方法** · 构建证据规格并在规划前定位缺项，最后用运行反馈修复
- **Baseline** · Paper2Code 与 DeepCode
- **Benchmark** · 23 篇 PaperBench Code-Dev，另测三个仓库运行
- **关键结果 / 消融** · 平均 0.84，执行里程碑三个全达，平均五次修复
- **适用条件 / 局限** · 执行子样本小且仅报告一类底座

**可复用机制** · 分开验证实现忠实度和可运行性

<a id="paper-155462"></a>

## CRANE: Constrained Reasoning Injection for Code Agents via Nullspace Editing

[官方论文页](https://neurips.cc/virtual/2026/poster/155462) · [作者来源](https://openreview.net/forum?id=5QIRV0FZpg)

- **问题 / 瓶颈** · 合并推理能力时可能牺牲工具格式和效率
- **核心创新 / 方法** · 选择有益权重增量并抑制影响协议的分量
- **Baseline** · 原指令、推理检查点及其他合并方法
- **Benchmark** · Roo-Eval、SWE-bench-Verified 和 Terminal-Bench v2
- **关键结果 / 消融** · 作者报告 SWE-bench 最多多解决 14 项
- **适用条件 / 局限** · 依赖成对底座，未知工具协议待检验

**可复用机制** · 对合并模型分别测完成率、协议违例和推理成本

<a id="paper-151001"></a>

## Credit Assignment with Resets in Language Model Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/151001) · [作者来源](https://openreview.net/forum?id=dffvGIN6Hu)

- **问题 / 瓶颈** · 单一结果奖励难识别出错步骤
- **核心创新 / 方法** · 对比随机重置和模型自行定位重置，使用后缀结果更新
- **Baseline** · GRPO 与随机重置
- **Benchmark** · 多模型推理基准，具名任务待核
- **关键结果 / 消融** · 作者报告自定位重置持续优于对照
- **适用条件 / 局限** · 依赖结果可验证且错误定位可靠

**可复用机制** · 固定 rollout 预算比较随机截断、错误定位和完整采样

<a id="paper-139433"></a>

## CREF: Forecasting Benchmarks for the Age of Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/139433) · [作者来源](https://openreview.net/forum?id=QrrgR9gtNJ)

- **问题 / 瓶颈** · 历史评测易受记忆、相关信号和工具取数污染
- **核心创新 / 方法** · 从公开 API 持续构造未来预测任务
- **Baseline** · 静态历史评测与回溯评测
- **Benchmark** · 32 个 API 的 50 个任务
- **关键结果 / 消融** · 回溯排序与静态较一致，实时发现语言模型表现差距
- **适用条件 / 局限** · 数据延迟与评测频度需管理

**可复用机制** · 部署前增加时间锁定评测，并按数据频率对照

<a id="paper-149844"></a>

## CRePE: Curved Ray Expectation Positional Encoding for Unified-Camera-Controlled Video Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/149844) · [作者来源](https://openreview.net/forum?id=msKXlv69Pt)

- **问题 / 瓶颈** · 针孔或仅射线编码难覆盖鱼眼和场景深度
- **核心创新 / 方法** · 沿源射线构造深度相关编码，以几何注意力适配器接入冻结 DiT
- **Baseline** · 现有多视图位置编码
- **Benchmark** · 统一相机模型下的镜头控制、质量及编码消融
- **关键结果 / 消融** · 作者报告控制更稳定且视频质量改善
- **适用条件 / 局限** · 依赖几何伪监督，标定误差待核

**可复用机制** · 固定生成骨干比较针孔、纯射线与深度感知编码

<a id="paper-149613"></a>

## CRESiST: Self-Enhancing Exploritive Policy Learning for Simultaneous Speech Translation

[官方论文页](https://neurips.cc/virtual/2026/poster/149613) · [作者来源](https://openreview.net/forum?id=omv2djtEFF)

- **问题 / 瓶颈** · 前缀翻译反复计算缓存且依赖切分
- **核心创新 / 方法** · 交替输入语音块和生成文本，以语义和时延反馈蒸馏读写策略
- **Baseline** · 级联系统及静态对齐
- **Benchmark** · FLEURS、CoVoST2、MuST-C、ACL 60/60
- **关键结果 / 消融** · 作者报告质量时延前沿改善
- **适用条件 / 局限** · 真实长流内存和噪声边界待核

**可复用机制** · 在同一质量目标下比较时延、缓存重算和切分依赖

<a id="paper-139787"></a>

## CRISP: Compositional Reasoning over Images via Stackable Programs for VLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/139787) · [作者来源](https://openreview.net/forum?id=4tXzMne4ZB)

- **问题 / 瓶颈** · 最终正确可能来自中间视觉依据错误
- **核心创新 / 方法** · 用可组合操作生成链，并自动导出每步对象框真值
- **Baseline** · 最终答案评测和不同模型深度表现
- **Benchmark** · 二维精灵、三维人物及室内场景
- **关键结果 / 消融** · 模型随推理深度退化，部分正确答案过程不正确
- **适用条件 / 局限** · 需结构化场景描述

**可复用机制** · 固定操作类型扫描深度并记录各步定位和答案正确率

<a id="paper-153441"></a>

## CRISP: Fixing Flying Pixels in Latent LiDAR Generation via Diffusion Decoding

[官方论文页](https://neurips.cc/virtual/2026/poster/153441) · [作者来源](https://openreview.net/forum?id=LIADRHg7uI)

- **问题 / 瓶颈** · 卷积解码模糊轮廓导致悬空点
- **核心创新 / 方法** · 用像素空间扩散解码和支持掩码替代卷积解码
- **Baseline** · 原卷积解码及 LiDM
- **Benchmark** · KITTI-360、SemanticKITTI、nuScenes，测 FSVD、FPVD、FRID
- **关键结果 / 消融** · 固定骨干两项距离平均下降 50.5%，世界模型替换 FSVD 降 15.5%
- **适用条件 / 局限** · 额外扩散开销待核

**可复用机制** · 对输出端伪影先做单模块替换，按边缘和非边缘分层评分

<a id="paper-139027"></a>

## Croissant Baker: Metadata Generation for Discoverable, Governable, and Reusable ML Datasets

[官方论文页](https://neurips.cc/virtual/2026/poster/139027) · [作者来源](https://openreview.net/forum?id=pVO3A5soQi)

- **问题 / 瓶颈** · 受治理和大型数据无法先上传公共平台
- **核心创新 / 方法** · 用模块化处理器从本地目录提取并验证 Croissant 元数据
- **Baseline** · 生产者元数据或标准导出真值
- **Benchmark** · 超 140 数据集，含大规模 Parquet 案例
- **关键结果 / 消融** · 作者报告与真值一致率 97–100%
- **适用条件 / 局限** · 复杂语义和治理字段覆盖待核

**可复用机制** · 将可从文件确定的字段与需文档确认的字段独立验证

<a id="paper-139073"></a>

## CroissantMiner: Automated Extraction and Validation of Croissant Metadata for ML Datasets

[官方论文页](https://neurips.cc/virtual/2026/poster/139073) · [作者来源](https://openreview.net/forum?id=mrHeRim4QM)

- **问题 / 瓶颈** · 拆分可能丢失长字段所需证据
- **核心创新 / 方法** · 全模式评测结合规则与人工审计的模型判分
- **Baseline** · 20 个系统含单次抽取及四类 Agent
- **Benchmark** · 602 篇，102 篇人工金标，其余银标
- **关键结果 / 消融** · 最佳规范提示单次抽取综合 0.704，分解普遍更差
- **适用条件 / 局限** · 模型判断及银标质量影响排序

**可复用机制** · 按字段证据跨度报告分解相对单次的收益

<a id="paper-151354"></a>

## Cross-Architecture Transferability is Width-Confounded:Diagnosis and Subspace Correction

[官方论文页](https://neurips.cc/virtual/2026/poster/151354) · [作者来源](https://openreview.net/forum?id=bAYaurZBBI)

- **问题 / 瓶颈** · 无标签秩分数混入特征维数
- **核心创新 / 方法** · 与固定参考编码器对齐后计算子空间校正分数
- **Baseline** · RankMe与随机选择
- **Benchmark** · 三个架构池、23个任务单元，测选择遗憾
- **关键结果 / 消融** · 平均遗憾从0.165降至0.071
- **适用条件 / 局限** · 依赖参考模型，架构内效果应分开看

**可复用机制** · 先分开报告族内和族间选择误差

<a id="paper-149084"></a>

## Cross-Attentive Bayesian Low-Rank Adaptation for Multimodal Uncertainty Estimation

[官方论文页](https://neurips.cc/virtual/2026/poster/149084) · [作者来源](https://openreview.net/forum?id=szn6IUxvw6)

- **问题 / 瓶颈** · 确定性单模态适配遗漏声学条件
- **核心创新 / 方法** · 文本低秩特征查询音频帧，预测适配器潜变量的后验参数
- **Baseline** · 确定性PEFT；具名对照待核
- **Benchmark** · 低资源音文任务，评测及数值待核
- **关键结果 / 消融** · 蒙特卡洛预测可拆解观测和适配不确定性
- **适用条件 / 局限** · 依赖帧级对齐并增加采样开销

**可复用机制** · 将随机性限制在低秩适配器，比较校准与成本

<a id="paper-139089"></a>

## Cross-Cell-Line Perturbation Prediction Needs Controls

[官方论文页](https://neurips.cc/virtual/2026/poster/139089) · [作者来源](https://openreview.net/forum?id=lnpzb1HvwX)

- **问题 / 瓶颈** · 总体分布指标易被目标群体背景变化主导
- **核心创新 / 方法** · 在留出群体上将总体分布与条件效应分别评估
- **Baseline** · 复制背景对照与平均差值对照
- **Benchmark** · 公开单细胞数据的留出群体评估，Energy及条件效应相关性
- **关键结果 / 消融** · 简单对照可在总体指标上竞争，方法排序随指标变化
- **适用条件 / 局限** · 限所测数据和群体

**可复用机制** · 预测干预响应前先检查基线是否已利用群体背景取得高分

<a id="paper-151708"></a>

## Cross-Channel Agreement Beats Consensus: Compositional Verification for Geometry Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/151708) · [作者来源](https://openreview.net/forum?id=Ye0G2Uemjp)

- **问题 / 瓶颈** · 同一图像偏差引起多数票相关错误
- **核心创新 / 方法** · 将自然语言答案与可执行符号路径配对，仅接受一致候选
- **Baseline** · 多数投票及非组合对照
- **Benchmark** · 四个几何任务，准确率
- **关键结果 / 消融** · 81.0%，较多数投票高10.4个百分点
- **适用条件 / 局限** · 依赖可执行表示与路径误差的互补性

**可复用机制** · 在共享感知证据的任务上比较跨通道确认和单通道投票

<a id="paper-151653"></a>

## Crosscoding Through Time: Sparse Feature Discovery Across Sequence Positions

[官方论文页](https://neurips.cc/virtual/2026/poster/151653) · [作者来源](https://openreview.net/forum?id=Z27xj38Fta)

- **问题 / 瓶颈** · 逐位置字典难识别回溯等时间行为
- **核心创新 / 方法** · 通过时序crosscoder提取分布在不同位置的特征
- **Baseline** · 传统SAE及其他时序模型
- **Benchmark** · TempBench的合成及真实任务
- **关键结果 / 消融** · 回溯检出率比SAE高40%，诱发效果高15%
- **适用条件 / 局限** · 仅两项真实任务优于比较方法

**可复用机制** · 在诊断顺序行为时比较位置联合字典与单位置探针

<a id="paper-138884"></a>

## Cross-Dialect Generalization Without Retraining: Benchmarks and Evaluation of Schema-Derived Constrained Decoding for MLIR

[官方论文页](https://neurips.cc/virtual/2026/poster/138884) · [作者来源](https://openreview.net/forum?id=yrIzLZp02Q)

- **问题 / 瓶颈** · 为每个新方言微调难扩展
- **核心创新 / 方法** · 从操作定义抽取语法和类型约束，推理时使用
- **Baseline** · 梯度式适配及约束变体；具名待核
- **Benchmark** · 435条MLIR样例，含30条功能对照
- **关键结果 / 消融** · 摘要提供跨方言及可执行性评测，数值待核
- **适用条件 / 局限** · 合法文本未必语义正确

**可复用机制** · 把编译通过与实际输出正确分开计分

<a id="paper-150347"></a>

## Cross-Distribution Generalization in Longitudinal Behavioral Data Through Frozen Coherence Constraints

[官方论文页](https://neurips.cc/virtual/2026/poster/150347) · [作者来源](https://openreview.net/forum?id=ioWVlKwBW2)

- **问题 / 瓶颈** · 跨群体行为数据的语义容易漂移
- **核心创新 / 方法** · 分别编码时序、频域和语义，用定向注意力融合并联合判别与一致性训练
- **Baseline** · 特征对齐与容量扩张路线
- **Benchmark** · GLOBEM跨群体评测及其他行为数据
- **关键结果 / 消融** · GLOBEM分布外准确率79.93%，提升27.13个百分点
- **适用条件 / 局限** · 群体和任务差异限制外推

**可复用机制** · 对照冻结与可更新的一致性参照

<a id="paper-152725"></a>

## Cross-Domain Knowledge Separation and Positive Transmission for Noisy Domain Incremental Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/152725) · [作者来源](https://openreview.net/forum?id=QpRuEc6Iem)

- **问题 / 瓶颈** · 标签噪声加剧领域冲突和遗忘
- **核心创新 / 方法** · 对比隔离领域提示并选择可靠旧知识辅助新域学习
- **Baseline** · 领域增量学习对照，具名待核
- **Benchmark** · 噪声领域增量学习，数据和数值待核
- **关键结果 / 消融** · 作者报告经验验证，独立增益待核
- **适用条件 / 局限** · 可靠性估计可能受噪声率影响

**可复用机制** · 分别对照提示隔离及选择性知识迁移

<a id="paper-153625"></a>

## Cross-Family Universality of Behavioral Axes via Anchor-Projected Representations

[官方论文页](https://neurips.cc/virtual/2026/poster/153625) · [作者来源](https://openreview.net/forum?id=JzUapd8EXW)

- **问题 / 瓶颈** · 隐藏维度及分词不同阻碍对照
- **核心创新 / 方法** · 将不同模型激活投影至公共锚坐标，评估跨家族方向一致性
- **Baseline** · 目标家族留出对照
- **Benchmark** · 五个模型家族及十个行为维度
- **关键结果 / 消融** · 留出检测准确率0.83，平均二元AUROC 0.95
- **适用条件 / 局限** · 结果依赖锚样本与模型簇

**可复用机制** · 建立跨模型探针时独立留出架构及锚样本

<a id="paper-153646"></a>

## Cross-Fitting for Neural Posterior Estimation

[官方论文页](https://neurips.cc/virtual/2026/poster/153646) · [作者来源](https://openreview.net/forum?id=JmM3HShlbu)

- **问题 / 瓶颈** · 灵活后验模型可能向零方差过拟合
- **核心创新 / 方法** · 交叉拟合条件均值后再估计折外残差密度
- **Baseline** · 标准神经后验估计
- **Benchmark** · 八项合成任务及宇宙学数据，留出对数似然
- **关键结果 / 消融** · 作者报告似然改善且高维收益更明显
- **适用条件 / 局限** · 折外残差方差可能受均值误差抬升

**可复用机制** · 分离均值和高阶矩拟合，单独检查校准

<a id="paper-151273"></a>

## Cross Flow: One-Step Generation Across Latent and Pixel Spaces

[官方论文页](https://neurips.cc/virtual/2026/poster/151273) · [作者来源](https://openreview.net/forum?id=bbx1xRuNl6)

- **问题 / 瓶颈** · 固定潜空间解码器难补偿潜变量偏差
- **核心创新 / 方法** · 以跨空间目标联合潜变量生成和像素解码
- **Baseline** · 传统潜扩散及生成比较，具名待核
- **Benchmark** · ImageNet-1k 256×256，FID和网络评估次数
- **关键结果 / 消融** · 一次网络评估FID为1.62
- **适用条件 / 局限** · 结果限已测试分辨率和数据

**可复用机制** · 在同推理预算下对比跨空间流与显式解码

<a id="paper-148739"></a>

## Cross-Foundation Complementary Learning Systems for Continual Test-Time Adaptation in Open-Vocabulary Semantic Segmentation

[官方论文页](https://neurips.cc/virtual/2026/poster/148739) · [作者来源](https://openreview.net/forum?id=vP6mCzbls0)

- **问题 / 瓶颈** · 持续适配会破坏开放词汇语义接口
- **核心创新 / 方法** · 只快速更新少量视觉归一化参数，并用慢记忆与冻结结构观察器稳定
- **Baseline** · NACLIP未适配
- **Benchmark** · Cityscapes至ACDC和OnDA流，mIoU
- **关键结果 / 消融** · 两种流分别达32.92及30.75 mIoU
- **适用条件 / 局限** · 需额外冻结观察器，成本待核

**可复用机制** · 用同义词一致性监测适配是否破坏语义接口

<a id="paper-150764"></a>

## CrossID: Cross-Supervised Spatio-Temporal Gated Fusion for Personalized Portrait Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/150764) · [作者来源](https://openreview.net/forum?id=fYVQT7T0IU)

- **问题 / 瓶颈** · 自重建有复制参考特征的捷径
- **核心创新 / 方法** · 以时空门控适配器和交叉监督双重约束
- **Baseline** · 既有参考肖像生成方法，具名待核
- **Benchmark** · CrossID-Bench及视觉语言评估
- **关键结果 / 消融** · 作者报告兼顾参考保真和文本可控性
- **适用条件 / 局限** · 数据规模与训练策略的分别贡献待核

**可复用机制** · 应在授权数据上固定骨干，隔离交叉监督对两个目标的影响

<a id="paper-139193"></a>

## Crossing the Validation crisis: Cross-validation reduces benchmarking variance surprisingly well

[官方论文页](https://neurips.cc/virtual/2026/poster/139193) · [作者来源](https://openreview.net/forum?id=fOqEGBqN5y)

- **问题 / 瓶颈** · 单次划分难区分真实性能和验证波动
- **核心创新 / 方法** · 用虚拟样本增益量化多折对估计方差的帮助，并以早期折预测边际收益
- **Baseline** · 单次划分与不同折数
- **Benchmark** · 合成数据、组织病理扫描及NLP微调
- **关键结果 / 消融** · 多折可显著改善稳定性，收益饱和有时比预期晚
- **适用条件 / 局限** · 取决于折间相关性和训练预算

**可复用机制** · 依据测得的方差改善决定是否增加折数

<a id="paper-150184"></a>

## Cross-Layer Evolution Graph Learning for Fine-grained VLM Hallucination Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/150184) · [作者来源](https://openreview.net/forum?id=k5PB3UmZfp)

- **问题 / 瓶颈** · 静态特征探针受到粗粒度监督限制
- **核心创新 / 方法** · 把内部状态建成跨层异质图，用多实例学习读出token风险
- **Baseline** · 静态特征探针；具名待核
- **Benchmark** · M-HalDetect、ViGoR、HalLoc
- **关键结果 / 消融** · 检测优于所比方法，定位表现有竞争力
- **适用条件 / 局限** · 需访问内部状态，层选取影响未知

**可复用机制** · 同时量化句级检出与token定位

<a id="paper-155262"></a>

## Cross-Modal Prior-Guided Training with Visual Foundation Models for Unsupervised LiDAR Point Cloud Registration

[官方论文页](https://neurips.cc/virtual/2026/poster/155262) · [作者来源](https://openreview.net/forum?id=715pTqJc6O)

- **问题 / 瓶颈** · 稀疏点云和有限视觉重合使伪标签不稳定
- **核心创新 / 方法** · 视觉教师整合几何先验并生成伪标签，学生按可匹配性学习
- **Baseline** · 无监督配准对照，具名待核
- **Benchmark** · KITTI、nuScenes的点云配准
- **关键结果 / 消融** · 作者报告多种骨干改善，部署不增参数
- **适用条件 / 局限** · 依赖训练阶段视觉覆盖和标定

**可复用机制** · 按重合率分组测跨模态教师对配准收益

<a id="paper-148536"></a>

## Cross-Model Circuit Discovery

[官方论文页](https://neurips.cc/virtual/2026/poster/148536) · [作者来源](https://openreview.net/forum?id=xAgPnoOF5V)

- **问题 / 瓶颈** · 单层表征比对难解释跨模型计算
- **核心创新 / 方法** · 扩展跨层转码器，联合稀疏性和输出保真目标
- **Baseline** · 完整类别电路及各模型保留特征
- **Benchmark** · 配对视觉分类模型，比较剪枝后准确率
- **关键结果 / 消融** · 共享交集保留完整电路89%至98%准确率
- **适用条件 / 局限** · 限论文所测视觉模型与类别

**可复用机制** · 用共享特征剪枝和输出保持检验跨模型电路共性

<a id="paper-153772"></a>

## Cross-Model KV Cache Transfer in LLM Families: A Closed-Form Linear Mapping for Prefill Reuse

[官方论文页](https://neurips.cc/virtual/2026/poster/153772) · [作者来源](https://openreview.net/forum?id=ImLkPKhbKo)

- **问题 / 瓶颈** · 换模型通常必须重复预填充
- **核心创新 / 方法** · 去除位置旋转后，以逐头岭回归将多个源层映射至目标层
- **Baseline** · 目标独立预填充与非线性映射
- **Benchmark** · 三族六个模型对，比较准确率保留
- **关键结果 / 消融** · 四对保留71%至98%准确率，两对明显下降
- **适用条件 / 局限** · 匹配KV头数与维度仍不足以保证成功

**可复用机制** · 按路由对校准缓存映射，在低保留率时重算

<a id="paper-153663"></a>

## Cross-order Consensus Graph Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/153663) · [作者来源](https://openreview.net/forum?id=JfYnVbWGRN)

- **问题 / 瓶颈** · 过早汇总边信息会削弱结构区分
- **核心创新 / 方法** · 以线图学习边匹配，与节点匹配联合优化，并加跨阶对齐正则
- **Baseline** · 深度图匹配基线，具名待核
- **Benchmark** · 标准视觉图匹配，比较准确率
- **关键结果 / 消融** · 作者报告比对照准确率更高，数值待核
- **适用条件 / 局限** · 边构造和线图规模可能限制扩展

**可复用机制** · 比较仅节点匹配与节点边联合推断，并分开消融求解和正则

<a id="paper-155202"></a>

## Cross-Question Reliable Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/155202) · [作者来源](https://openreview.net/forum?id=7WpdfgWglP)

- **问题 / 瓶颈** · 逐题二值奖励会挤压置信排序
- **核心创新 / 方法** · 从题组在多个容忍风险下的拒答阈值构造相对奖励
- **Baseline** · 逐题正确性匹配奖励
- **Benchmark** · MATH-500、GSM8K、Big-Math-Digits 与跨域问答，测 C@5
- **关键结果 / 消融** · 数学 C@5 从 0.8% 到 42.4%，跨域从 9.9% 到 23.6%
- **适用条件 / 局限** · 依赖组内排序和训练覆盖

**可复用机制** · 用相同错误预算比较逐题校准和组间排序训练。

<a id="paper-148830"></a>

## CrossSteer:Cross-Modal Safety Steering for Audio-Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148830) · [作者来源](https://neurips.cc/virtual/2026/poster/148830)

- **问题 / 瓶颈** · 语音变化使安全方向估计不稳定
- **核心创新 / 方法** · 把文本来源的安全信号迁移到共享表示，用于增强防护
- **Baseline** · 直接语音侧调整及已有防护
- **Benchmark** · 三个音频语言骨干，测防护表现与正常效用
- **关键结果 / 消融** · 作者报告防护改善，正常效用大体保留
- **适用条件 / 局限** · 依赖跨模态共享表示，具体幅度待查

**可复用机制** · 验证跨模态防护时分开报告安全指标和正常语音任务表现。

<a id="paper-148398"></a>

## Cross-User Poisoning: User-Task Boundary Failures in Multi-User Collaborative Language Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/148398) · [作者来源](https://neurips.cc/virtual/2026/poster/148398)

- **问题 / 瓶颈** · 共享上下文会混淆授权主体
- **核心创新 / 方法** · 对照上下文压缩及显式来源和任务边界防护
- **Baseline** · 仅做摘要的防护
- **Benchmark** · 多用户任务环境，评估边界隔离
- **关键结果 / 消融** · 作者观察到摘要不足，任务聚类与来源提示有益
- **适用条件 / 局限** · 对自适应风险的防护未确认

**可复用机制** · 共享助手应分别验证用户身份、任务范围和工具权限。

<a id="paper-152755"></a>

## CrossWeave: Emergent Cross-Modal Scene and Instance Retrieval from Sparse 2D-3D Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/152755) · [作者来源](https://openreview.net/forum?id=Qakxj8c6lU)

- **问题 / 瓶颈** · 整图向量丢掉场景细节
- **核心创新 / 方法** · 学习图块与点匹配，用最优传输聚合冗余区域
- **Baseline** · 全局编码及不同任务独立模型
- **Benchmark** · ScanNet、3RScan 场景及实例检索
- **关键结果 / 消融** · 单模型在两类检索表现领先，幅度待核
- **适用条件 / 局限** · 依赖可靠局部对应

**可复用机制** · 比较局部监督与全局标签的标注预算和检索性能。

<a id="paper-152853"></a>

## Crowded in B-Space: Calibrating Shared Directions for LoRA Merging

[官方论文页](https://neurips.cc/virtual/2026/poster/152853) · [作者来源](https://openreview.net/forum?id=PtEkosDXWk)

- **问题 / 瓶颈** · 多个 B 矩阵反复强化少量共同方向
- **核心创新 / 方法** · 压低 B 中过度共享方向，再缩放合并更新
- **Baseline** · Task Arithmetic、TIES、TSV-M
- **Benchmark** · 数学、代码、金融、医学共八基准
- **关键结果 / 消融** · 较原合并方法平均提高 3.4–8.3 点
- **适用条件 / 局限** · 跨骨干约束待核

**可复用机制** · 分别诊断 A、B 的重叠度，再比较合并性能。

<a id="paper-148277"></a>

## CRUMB: Efficient Prior Fitted Network Inference via Distributionally Matched Context Batching

[官方论文页](https://neurips.cc/virtual/2026/poster/148277) · [作者来源](https://openreview.net/forum?id=z3XMLStVPC)

- **问题 / 瓶颈** · 全量训练样本上下文导致二次开销
- **核心创新 / 方法** · 聚类查询，贪心最小化 MMD 选择上下文，再执行模型
- **Baseline** · 现有上下文选择策略
- **Benchmark** · TabArena 51 个数据集，三个 PFN
- **关键结果 / 消融** · 作者报告优于对照，对协变量漂移更稳健
- **适用条件 / 局限** · 聚类和检索成本需单测

**可复用机制** · 按查询簇匹配小样本上下文并比较召回与成本。

<a id="paper-139175"></a>

## CruxBench: A Benchmark of Information Discovery

[官方论文页](https://neurips.cc/virtual/2026/poster/139175) · [作者来源](https://openreview.net/forum?id=gR5rYsslQS)

- **问题 / 瓶颈** · 答案准确率难反映信息发现能力
- **核心创新 / 方法** · 用未来市场变化衡量开放问题的信息价值
- **Baseline** · 八个前沿及开放权重模型
- **Benchmark** · 336 个预测市场目标
- **关键结果 / 消融** · 与独立模型质量相关系数 0.87，可预测下游有效性
- **适用条件 / 局限** · 市场价格不能代表所有领域的信念

**可复用机制** · 用后续可观测结果评估提问，另测真实下游帮助。

<a id="paper-139015"></a>

## CryoAtlas: A Large Curated Dataset and Unified Benchmark for Cryo-EM Atomic Model Building

[官方论文页](https://neurips.cc/virtual/2026/poster/139015) · [作者来源](https://openreview.net/forum?id=qHJrv65ncA)

- **问题 / 瓶颈** · 单一指标难区分重建质量
- **核心创新 / 方法** · 统一证据与多维评估协议，按观测质量和相似性切片
- **Baseline** · Phenix、AlphaFold 3 与学习方法
- **Benchmark** · 冷冻电镜重建评测，618 个目标
- **关键结果 / 消融** · 作者报告重训改善，幅度待核
- **适用条件 / 局限** · 仅反映观测结构重建

**可复用机制** · 重建任务应同时报告输入拟合和物理有效性。

<a id="paper-149543"></a>

## CryoGeo: Latent Pose Equivariance for Amortized Ab Initio Cryo-EM Reconstruction

[官方论文页](https://neurips.cc/virtual/2026/poster/149543) · [作者来源](https://openreview.net/forum?id=pMplnGXe2b)

- **问题 / 瓶颈** · 仅靠重建目标容易出现位姿塌缩
- **核心创新 / 方法** · 在输出位姿上施加与图像平面变换一致的等变约束
- **Baseline** · 无约束变体及神经基线
- **Benchmark** · 模拟和真实冷冻电镜重建
- **关键结果 / 消融** · 作者报告位姿一致性和重建稳定性改善
- **适用条件 / 局限** · 依赖已知成像变换规则

**可复用机制** · 对逆问题同时检验输出等变性和原观测重建质量。

<a id="paper-154603"></a>

## CrystalREPA: Transferring Physical Priors from Universal MLIPs to Crystal Generative Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154603) · [作者来源](https://openreview.net/forum?id=CNnIIFw6WS)

- **问题 / 瓶颈** · 通用势能排行榜未必预测教师迁移效果
- **核心创新 / 方法** · 冻结势能模型，通过按元素的对比目标对齐生成模型内部表示
- **Baseline** · 不同教师及未对齐生成模型
- **Benchmark** · 三个生成框架、十个教师和两个晶体基准
- **关键结果 / 消融** · 作者报告稳定性及有效性改善，迁移强弱与表征可分性相关
- **适用条件 / 局限** · 限所测框架与晶体数据

**可复用机制** · 蒸馏前用表征探针选择教师，并对照只按排行榜选择。

<a id="paper-139195"></a>

## CSBench: A Comprehensive Benchmark for Evaluating Project-Level System Construction in Computer Science

[官方论文页](https://neurips.cc/virtual/2026/poster/139195) · [作者来源](https://openreview.net/forum?id=fHaQSToCTh)

- **问题 / 瓶颈** · 算法成绩掩盖系统构建短板
- **核心创新 / 方法** · 以隔离环境中的规格到代码任务评估构建和执行反馈利用
- **Baseline** · 12 种语言模型
- **Benchmark** · 100 项操作系统、编译器或数据库等课程任务
- **关键结果 / 消融** · GPT-5.2 算法题超过 90%，系统类低于 35%
- **适用条件 / 局限** · 课程任务与生产项目有差别

**可复用机制** · 评估代码助手时按系统层次区分维护与从零实现。

<a id="paper-149718"></a>

## CSCN: The Crossed Subtree Convolutional Network

[官方论文页](https://neurips.cc/virtual/2026/poster/149718) · [作者来源](https://openreview.net/forum?id=nwrZPCZZ92)

- **问题 / 瓶颈** · 图远距关系难跨多跳传递且易过平滑
- **核心创新 / 方法** · 按序对齐子树并以滑动窗口聚合树内和跨树特征
- **Baseline** · 传统消息传递网络
- **Benchmark** · 多个图分类基准，具体数据集待核
- **关键结果 / 消融** · 作者报告结果具竞争力
- **适用条件 / 局限** · 排序和大图成本待核

**可复用机制** · 用子结构表示而非全局深层传播，比较图分类表现。

<a id="paper-153299"></a>

## CS-DICE: Offline Reinforcement Learning with Coherent Occupancy Regularization

[官方论文页](https://neurips.cc/virtual/2026/poster/153299) · [作者来源](https://openreview.net/forum?id=MI1dfW9mTi)

- **问题 / 瓶颈** · 混合隐藏模式的占用分布可能要求执行器无法实现的动作关系
- **核心创新 / 方法** · 以硬或软选择器决定 DICE 正则参考切片，保留执行接口
- **Baseline** · 对照池化参考的标准 DICE
- **Benchmark** · 受控实验与 MaMuJoCo 合作设置
- **关键结果 / 消融** · 一致参考能恢复高回报，冲突前信号可见时池化可正常工作
- **适用条件 / 局限** · 依赖识别与执行条件一致的切片

**可复用机制** · 对离线数据做隐藏模式压力测试，再选正则参考。

<a id="paper-154473"></a>

## CSFlow: Aligning Flow Matching with Human Contrast Sensitivity

[官方论文页](https://neurips.cc/virtual/2026/poster/154473) · [作者来源](https://openreview.net/forum?id=DKVqS2hVS1)

- **问题 / 瓶颈** · 各空间频率形成时间和可感知程度不同
- **核心创新 / 方法** · 估计逆流各区间生成的频率，并据对比敏感度重设时间权重
- **Baseline** · 未调整的流匹配
- **Benchmark** · 生成图像的 FID、Inception Score、GenEval
- **关键结果 / 消融** · 作者报告分别改善 4.7%、2.2%、2.5%
- **适用条件 / 局限** · 不同视觉数据和感知条件下须重校

**可复用机制** · 先测频率形成时序，再对照均匀调度。

<a id="paper-139630"></a>

## CSI-TextBench: A Dataset and Benchmark for Language-Grounded Ambient Sensing Perception

[官方论文页](https://neurips.cc/virtual/2026/poster/139630) · [作者来源](https://openreview.net/forum?id=EO00lY9oOt)

- **问题 / 瓶颈** · 无线感知样本缺少自然语言配对
- **核心创新 / 方法** · 按标注层级生成描述并做多对多配对和对比对齐
- **Baseline** · 五种对齐方法及任务分类器集成
- **Benchmark** · 七种感知任务和 140 个组合场景
- **关键结果 / 消融** · 组合场景 top-1 86.9%，作者报告开放查询和少样本适配表现
- **适用条件 / 局限** · 受标签词表和传感域偏移影响

**可复用机制** · 对弱标注传感输入同时测试单属性和组合查询。

<a id="paper-149892"></a>

## CSLA: Sparse-Linear Attention with Learnable Routing and Quantization-aware Training

[官方论文页](https://neurips.cc/virtual/2026/poster/149892) · [作者来源](https://openreview.net/forum?id=mTASL9d9xh)

- **问题 / 瓶颈** · 启发式门控可能误分配稀疏与线性计算
- **核心创新 / 方法** · 用学习路由和混合比例校正分解，配合量化感知微调
- **Baseline** · 稀疏线性注意力
- **Benchmark** · 视频扩散生成，比较注意力加速和生成质量
- **关键结果 / 消融** · 作者报告 97% 稀疏度及 18.6 倍注意力加速
- **适用条件 / 局限** · 单算子加速不等于端到端加速

**可复用机制** · 同预算下分别消融路由、混合和量化。

<a id="paper-153774"></a>

## CSO-LLM: Class Subspace Orthogonalization for Post-Training Backdoor Detection and Trigger Inversion in LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/153774) · [作者来源](https://neurips.cc/virtual/2026/poster/153774)

- **问题 / 瓶颈** · 分类器的正常语义信号可能抬高安全检测误报
- **核心创新 / 方法** · 在防御审计中控制普通类别信号对检测分数的干扰
- **Baseline** · 基础检测器
- **Benchmark** · 多个文本分类域及语言模型骨干
- **关键结果 / 消融** · 作者报告敏感性和特异性改善，幅度待核
- **适用条件 / 局限** · 证据来自分类设置

**可复用机制** · 以正常类别词和跨域样本验证防御检测误报。

<a id="paper-153130"></a>

## CSO: Refining Robotic Policies via Skill Distribution Alignment and Skill-Grained Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/153130) · [作者来源](https://openreview.net/forum?id=NgYZ9EHKT6)

- **问题 / 瓶颈** · 动作量化导致先验分布偏差，整段重要性更新不稳
- **核心创新 / 方法** · 成功轨迹拒绝采样微调，更新时为各技能独立算裁剪比率
- **Baseline** · 量化动作技能先验与强化学习变体
- **Benchmark** · LIBERO、RoboTwin 及真机
- **关键结果 / 消融** · 作者报告具有竞争力，具体幅度待核
- **适用条件 / 局限** · 需可判定成功及可靠技能编码

**可复用机制** · 分别测先验校正与更新粒度对技能成功率的贡献。

<a id="paper-139020"></a>

## CTE-Bench: Audited Counterfactual Trace Evaluation for Stateful Software Simulators

[官方论文页](https://neurips.cc/virtual/2026/poster/139020) · [作者来源](https://openreview.net/forum?id=q9lApBA60Y)

- **问题 / 瓶颈** · 全局分数会掩盖干预生效处的错误。
- **核心创新 / 方法** · 用可执行服务为固定查询序列生成反事实对照。
- **Baseline** · 教师强制、隐藏后续轨迹、自回归滚动。
- **Benchmark** · 六个 Python 服务、255 个条目，按受影响位置计算精确匹配。
- **关键结果 / 消融** · Kimi 从教师强制的 61.5% 降至无后续提示的 28.9%。
- **适用条件 / 局限** · 确定性小型服务。

**可复用机制** · 只在干预确实改变响应的位置比较模拟保真度。

<a id="paper-139728"></a>

## CT-Lesion: A Multi-Region CT Dataset for Co-existing Lesion Segmentation and Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/139728) · [作者来源](https://openreview.net/forum?id=7utEDwCdTe)

- **问题 / 瓶颈** · 局部数据常把共存病灶标作背景。
- **核心创新 / 方法** · 脑胸腹 CT 对共存病灶做非预设类别的标注。
- **Baseline** · 与单区域和单病种数据思路比较，具名对照待核。
- **Benchmark** · 500 份 CT，检测与分割。
- **关键结果 / 消融** · 七位放射科医生完成标注，模型收益幅度待核。
- **适用条件 / 局限** · 私有队列，跨机构泛化待核。

**可复用机制** · 挑选跨域训练数据时同时审计漏标和稀有类别互补性。

<a id="paper-148258"></a>

## CTM-AI: A Blueprint for General AI Inspired by a Model of Consciousness

[官方论文页](https://neurips.cc/virtual/2026/poster/148258) · [作者来源](https://openreview.net/forum?id=zC3DNpexKf)

- **问题 / 瓶颈** · 多个专业组件难以整合互补信息。
- **核心创新 / 方法** · 用 CTM 启发的处理器架构选择、整合与交换信息。
- **Baseline** · 多模态和多智能体框架，具名配置待核。
- **Benchmark** · MUStARD、UR-FUNNY、StableToolBench、WebArena-Lite。
- **关键结果 / 消融** · 作者报告前两项准确率 72.28 和 72.13。
- **适用条件 / 局限** · 选择过程的独立消融待核。

**可复用机制** · 固定专家集，比较动态选择与固定协作。

<a id="paper-153321"></a>

## CTRL: Continual Test-Time Reinforcement Learning for Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153321) · [作者来源](https://openreview.net/forum?id=MBS7pBUFkB)

- **问题 / 瓶颈** · 错误共识和遗忘会互相强化。
- **核心创新 / 方法** · 用过程奖励筛选轨迹，以历史锚点梯度软校正更新。
- **Baseline** · 结果多数投票及单任务测试时强化学习。
- **Benchmark** · 连续任务流，测适应与保持，名称待核。
- **关键结果 / 消融** · 摘要指出两类误差可耦合，独立增益待核。
- **适用条件 / 局限** · 依赖过程评分可靠性及锚点覆盖。

**可复用机制** · 将伪标签筛选和遗忘防护分别消融。

<a id="paper-149614"></a>

## CuBic: Curvature-Driven Dynamic Inference Caching for Fast, High-Fidelity Flow Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/149614) · [作者来源](https://openreview.net/forum?id=ome95BvF3y)

- **问题 / 瓶颈** · 固定缓存间隔忽略局部速度场变化。
- **核心创新 / 方法** · 以代理曲率驱动空间分块和预算内更新，使用稀疏前向执行。
- **Baseline** · 经验规则或固定粒度缓存。
- **Benchmark** · 图像和视频流匹配，测成本与保真。
- **关键结果 / 消融** · 报告理论陈旧误差界和运行收益，数值待核。
- **适用条件 / 局限** · 代理与真实轨迹曲率的关系需验证。

**可复用机制** · 在相同预算比较曲率调度和固定间隔。

<a id="paper-139244"></a>

## CUDABeaver: Benchmarking LLM-Based Automated CUDA Debugging

[官方论文页](https://neurips.cc/virtual/2026/poster/139244) · [作者来源](https://openreview.net/forum?id=cZEC5u5oMz)

- **问题 / 瓶颈** · 测试通过可能来自退化到慢实现。
- **核心创新 / 方法** · 从真实失败工作区抽取任务，分开记录修复结果、调试轨迹和速度。
- **Baseline** · 比较多种模型和协议。
- **Benchmark** · 213 项 CUDA 调试任务，以协议条件化 pass@k 衡量。
- **关键结果 / 消融** · 作者报告仅计测试通过会遗漏性能退化，细项待核。
- **适用条件 / 局限** · 任务限制单文件，依赖测试与硬件。

**可复用机制** · 将修复前后性能与功能测试分别设门槛。

<a id="paper-148268"></a>

## CUDABench: Benchmarking LLMs for Text-to-CUDA Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/148268) · [作者来源](https://openreview.net/forum?id=z77rvLkVc6)

- **问题 / 瓶颈** · 编译成功不足以证明生成内核正确或高效。
- **核心创新 / 方法** · 用执行验证检查一致性并以 roofline 评估性能。
- **Baseline** · 已有高级语言到 CUDA 任务及多种 LLM。
- **Benchmark** · 多应用领域的文本到 CUDA 生成。
- **关键结果 / 消融** · 摘要报告编译成功与功能正确之间有显著落差。
- **适用条件 / 局限** · 效率依赖输入形状及硬件。

**可复用机制** · 为生成内核建立分层质量漏斗。

<a id="paper-139752"></a>

## CultureRed: Benchmarking Culture-Specific AI Safety Based on Global Statutes

[官方论文页](https://neurips.cc/virtual/2026/poster/139752) · [作者来源](https://openreview.net/forum?id=6hX4bhydM1)

- **问题 / 瓶颈** · 只测禁止项无法发现忽略例外导致的过度拒绝。
- **核心创新 / 方法** · 用法规主题及明确例外构造配对评测，并请专家抽查。
- **Baseline** · 通用安全评测与多种生成模型及守卫模型。
- **Benchmark** · 15 国 252 份法规、54,470 个规则与提示配对。
- **关键结果 / 消融** · 共测试 14 个生成模型及 16 个守卫，分项结果待核。
- **适用条件 / 局限** · 法规并非文化全貌，且随地区与时点变化。

**可复用机制** · 把规则适用和例外分别编码，按地区报告错误。

<a id="paper-155375"></a>

## CURe: Conservative Unlearning with Soft-Gating Regularization for Offline Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/155375) · [作者来源](https://openreview.net/forum?id=66b4l76IM4)

- **问题 / 瓶颈** · 均匀压低价值可能破坏应保留行为。
- **核心创新 / 方法** · 用遗忘轨迹和保留参考的 TD 梯度相似度门控评论器与策略更新。
- **Baseline** · 均匀遗忘及离线强化学习底座。
- **Benchmark** · MuJoCo，审计可检测影响与保留效用。
- **关键结果 / 消融** · 作者报告遗忘与效用折中改善，数值待核。
- **适用条件 / 局限** · 参考梯度须能代表保留数据。

**可复用机制** · 按重叠程度分层检查遗忘后策略漂移。

<a id="paper-151876"></a>

## CURE: Counterfactual Unsafe-token Re-masking for Diffusion Large Language Model Test-time Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/151876) · [作者来源](https://openreview.net/forum?id=XF2UgJwAIj)

- **问题 / 瓶颈** · 中间状态可能引导最终输出偏离安全要求。
- **核心创新 / 方法** · 用阶段条件化安全值定位需要重遮盖的位置，冻结基础模型。
- **Baseline** · 模型级对齐、轨迹检测和整块修正。
- **Benchmark** · 扩散语言模型安全评测，指标细项待核。
- **关键结果 / 消融** · 作者提出选择性修正以控制计算成本，比较幅度待核。
- **适用条件 / 局限** · 依赖安全值校准，与去噪阶段相关。

**可复用机制** · 在防御评测中对照局部修正与整块再生成。

<a id="paper-151750"></a>

## CURE: Coupled User-Grouped Reinforcement Learning for Cross-Domain Recommendation with Non-Overlapping Users

[官方论文页](https://neurips.cc/virtual/2026/poster/151750) · [作者来源](https://openreview.net/forum?id=YNBa2nmHd0)

- **问题 / 瓶颈** · 用户无交集时难获得目标域监督。
- **核心创新 / 方法** · 生成目标域伪推荐，以同用户联合归一化耦合域内外更新。
- **Baseline** · 跨域推荐方法，具名对照待核。
- **Benchmark** · Amazon Reviews、MovieLens 和在线 A/B。
- **关键结果 / 消融** · 摘要报告跨域与域内性能均改善。
- **适用条件 / 局限** · 伪监督质量和平台数据条件影响结果。

**可复用机制** · 固定伪数据对比独立归一化和用户分组归一化。

<a id="paper-155870"></a>

## CURE: Visual Reprogramming of Vision-Language Models under Limited Supervision

[官方论文页](https://neurips.cc/virtual/2026/poster/155870) · [作者来源](https://openreview.net/forum?id=2H603JxvpD)

- **问题 / 瓶颈** · 直接套用半监督会放大偏差且使输入重编程不稳。
- **核心创新 / 方法** · 结合高斯置信边际软权重和双属性提示一致性。
- **Baseline** · 已有视觉重编程与直接半监督扩展。
- **Benchmark** · 12 个少标签分类基准，测准确率。
- **关键结果 / 消融** · 摘要报告两组对照平均改善 5.06 和 6.67 个百分点。
- **适用条件 / 局限** · 边际校准受未标注分布影响。

**可复用机制** · 冻结骨干，对比硬阈值与软权重，单独消融一致性。

<a id="paper-154369"></a>

## Curriculum Learning for Safety Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/154369) · [作者来源](https://openreview.net/forum?id=E5y9WQdBbu)

- **问题 / 瓶颈** · 固定训练方案在分布外安全任务中可能脆弱。
- **核心创新 / 方法** · 按样本难度组织课程，按能力采样并逐步更新参考。
- **Baseline** · 常规 DPO 安全对齐。
- **Benchmark** · 三个模型家族，测分布外有害响应、一般能力和误拒。
- **关键结果 / 消融** · 作者报告分布外有害响应减少 16%，用 75% 数据达到基线安全性。
- **适用条件 / 局限** · 难度分级和参考更新效应待分别核验。

**可复用机制** · 固定数据预算，比较课程采样和随机采样的安全泛化。

<a id="paper-153849"></a>

## Curriculum Multiple Shooting for Robust Training of Neural and Universal Differential Equations

[官方论文页](https://neurips.cc/virtual/2026/poster/153849) · [作者来源](https://openreview.net/forum?id=IHtSSNfqdx)

- **问题 / 瓶颈** · 长序列、噪声和部分观测使轨迹拟合困难。
- **核心创新 / 方法** · 把多重射击与课程训练结合以稳定优化。
- **Baseline** · 既有微分方程拟合策略，具名方法待核。
- **Benchmark** · 12 组真实和仿真时序，覆盖 NODE、UDE 和机理 ODE。
- **关键结果 / 消融** · 作者报告收敛更快更稳，且泛化有竞争力。
- **适用条件 / 局限** · 课程与分段细节及各自收益待核。

**可复用机制** · 对照整轨迹训练与分段课程，并用留出轨迹测外推。

<a id="paper-156100"></a>

## Curriculum proof repair with learned counterexamples

[官方论文页](https://neurips.cc/virtual/2026/poster/156100) · [作者来源](https://openreview.net/forum?id=0Np4tgb57w)

- **问题 / 瓶颈** · 验证器错误粒度粗，裸通过反馈难分配信用。
- **核心创新 / 方法** · 生成诊断证据、修复理由和证明，由 Verus 反馈并按不变量依赖奖励。
- **Baseline** · 提示、检索或稀疏反馈的证明修复。
- **Benchmark** · Verus 证明修复，数据规模及通过率待核。
- **关键结果 / 消融** · 作者介绍拓扑奖励，分项量化待核。
- **适用条件 / 局限** · 依赖可测归纳性和可信验证环境。

**可复用机制** · 检验诊断中间步骤是否提高验证通过率，同时检查证明约束未被削弱。

<a id="paper-150081"></a>

## Curvature Beyond Positivity: Greedy Guarantees for Arbitrary Submodular Functions

[官方论文页](https://neurips.cc/virtual/2026/poster/150081) · [作者来源](https://openreview.net/forum?id=krtOWKxcTH)

- **问题 / 瓶颈** · 传统乘法近似通常需要非负或单调。
- **核心创新 / 方法** · 推广曲率概念并分析带剪枝的贪心。
- **Baseline** · 经典单调贪心及非单调统一比率。
- **Benchmark** · 任意次模函数的理论设定。
- **关键结果 / 消融** · 给出曲率依赖保证，在指定曲率范围优于 0.401 的非负统一比率。
- **适用条件 / 局限** · 需核实约束和曲率范围，不能直接泛化。

**可复用机制** · 选贪心前估算目标曲率，检查剪枝保证。

<a id="paper-154986"></a>

## Curvature-Dependent Lower Bounds for Frank-Wolfe

[官方论文页](https://neurips.cc/virtual/2026/poster/154986) · [作者来源](https://openreview.net/forum?id=9QiqOqCKsr)

- **问题 / 瓶颈** · 已知上界未说明能否在低维进一步加速。
- **核心创新 / 方法** · 分析简单实例上的 Frank–Wolfe 迭代动力学。
- **Baseline** · 均匀凸域已知上界。
- **Benchmark** · 精确线搜索或短步长，p≥3。
- **关键结果 / 消融** · 给出与 T 的负 p/(p−1) 次幂匹配的下界。
- **适用条件 / 局限** · 针对特定步长及几何条件。

**可复用机制** · 用对应下界判断是调整步长还是改算法族。

<a id="paper-153902"></a>

## Curvature-Dependent Lower Bounds for Riemannian Online Convex Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/153902) · [作者来源](https://openreview.net/forum?id=HrajZWdRvk)

- **问题 / 瓶颈** · 欧氏线性化在流形上不保测地凸性。
- **核心创新 / 方法** · 在双曲空间构造难实例，分析曲率和可行域直径对遗憾的影响。
- **Baseline** · 欧氏一阶与完整反馈及流形完整反馈。
- **Benchmark** · Hadamard 流形在线凸优化。
- **关键结果 / 消融** · 给出依赖曲率直径因子的一阶遗憾下界。
- **适用条件 / 局限** · 随机算法需几何跨度条件；无此限制的证明要求确定性和足够直径。

**可复用机制** · 在流形选反馈接口时核对曲率、直径和信息强度。

<a id="paper-152159"></a>

## Curvature-Guided Parameter Initialization for Multi-Task Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/152159) · [作者来源](https://openreview.net/forum?id=V4iWMobrjM)

- **问题 / 瓶颈** · 初值差异会混淆多任务算法的经验比较。
- **核心创新 / 方法** · 短预热探测局部曲率，选择经验上更有利的初始化。
- **Baseline** · 原始多任务优化算法及标准初始化。
- **Benchmark** · 标准多任务评测，具名数据与指标待核。
- **关键结果 / 消融** · 作者报告现有方法对初值敏感，具体收益待核。
- **适用条件 / 局限** · 有额外预热开销，局部曲率未必预测全程。

**可复用机制** · 固定优化器和预算，跨种子评估初始化与训练算法交互。

<a id="paper-138987"></a>

## CurveBench: A Benchmark for Exact Topological Reasoning over Nested Jordan Curves

[官方论文页](https://neurips.cc/virtual/2026/poster/138987) · [作者来源](https://openreview.net/forum?id=sHNd7dsC1m)

- **问题 / 瓶颈** · 关系问答难暴露全局层级错误
- **核心创新 / 方法** · 从嵌套曲线恢复有根树并以可验证奖励训练
- **Baseline** · Gemini-3.1-Pro-Preview、Qwen3-VL-8B-Thinking
- **Benchmark** · 756 图，按难度测树生成准确率
- **关键结果 / 消融** · 最强模型简单 71.1%、困难 19.1%；训练后 Qwen 简单档由 2.8% 到 33.3%
- **适用条件 / 局限** · 限于不相交平面曲线

**可复用机制** · 用完整包含树验收视觉推理，在固定评测预算下复核适用条件。

<a id="paper-149893"></a>

## CurveRL: Principled Distribution-Aware Context Reweighting for LLM Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/149893) · [作者来源](https://openreview.net/forum?id=mSNQ3ZeCPi)

- **问题 / 瓶颈** · 固定规则忽略训练中难度分布变化
- **核心创新 / 方法** · 用效用泛函的导数解释加权，再按分位数与密度设计权重
- **Baseline** · GRPO 等 RLVR 方法
- **Benchmark** · 多项推理基准，名称待核
- **关键结果 / 消融** · 作者报告持续优于基线，幅度待核
- **适用条件 / 局限** · 依赖可靠估计通过率分布

**可复用机制** · 按通过率分布而非绝对值调整提示权重，在固定评测预算下复核适用条件。

<a id="paper-148257"></a>

## CutAttn: Discovering Cognitive Transition Layers for Efficient Long-Context Prefilling

[官方论文页](https://neurips.cc/virtual/2026/poster/148257) · [作者来源](https://openreview.net/forum?id=zCmAsPM9EI)

- **问题 / 瓶颈** · 仅稀疏注意力未节省前馈计算
- **核心创新 / 方法** · 以层间 JS 散度定位过渡层，以归一化熵动态控制块裁剪
- **Baseline** · 完整及稀疏注意力
- **Benchmark** · RULER、InfiniteBench、LongBench
- **关键结果 / 消融** · 128K 预填充最高加速 2.02 倍，叠加稀疏注意力 2.81 倍
- **适用条件 / 局限** · 层位置和门槛可能随架构变化

**可复用机制** · 在注意力转为集中的层裁剪隐藏状态，在固定评测预算下复核适用条件。

<a id="paper-148338"></a>

## CUVET: A Partitioning Approach for Continuous Treatment Assignment At Scale

[官方论文页](https://neurips.cc/virtual/2026/poster/148338) · [作者来源](https://openreview.net/forum?id=yaAz2Trarn)

- **问题 / 瓶颈** · 不同用户对处理强度反应不同
- **核心创新 / 方法** · 树分群，在幂律边际递减假设下求闭式分配
- **Baseline** · 多种决策方法，具名待核
- **Benchmark** · MT-LIFT 和 CUVET-policy，测预算可行的收益
- **关键结果 / 消融** · MT-LIFT 报告增益 11.1%，对照最高 1.3%
- **适用条件 / 局限** · 依赖幂律及分群充分性

**可复用机制** · 分群后按边际投入产出分配连续预算，在固定评测预算下复核适用条件。

<a id="paper-152025"></a>

## CVTA: Cross-Variable Temporal Attention for Multivariate Irregular Time Series Prediction

[官方论文页](https://neurips.cc/virtual/2026/poster/152025) · [作者来源](https://openreview.net/forum?id=W5zQOIkTwd)

- **问题 / 瓶颈** · 异步观测和量纲异质性难统一处理
- **核心创新 / 方法** · 变量条件嵌入配合近期动态状态上的跨变量注意力
- **Baseline** · 既有预测器及加装模块的版本
- **Benchmark** · 多项真实短期预测，具名待核
- **关键结果 / 消融** · 报告在线预测与辅助模块均有效，幅度待核
- **适用条件 / 局限** · 长程效果待核

**可复用机制** · 用紧凑跨变量状态预测异步序列，在固定评测预算下复核适用条件。

<a id="paper-149212"></a>

## CWAGraph: Retrieving What Was Never Explicitly Identified in Graph-Based RAG

[官方论文页](https://neurips.cc/virtual/2026/poster/149212) · [作者来源](https://openreview.net/forum?id=s6xGR3aduA)

- **问题 / 瓶颈** · 缺边默认未知会遗漏规则覆盖的实体
- **核心创新 / 方法** · 在图检索中加入局部闭世界层，将规则证据关联到其管辖实体
- **Baseline** · 分块和图式 RAG
- **Benchmark** · SetQA 493 题，两领域三难度
- **关键结果 / 消融** · 报告持续改善，幅度待核
- **适用条件 / 局限** · 仅对可识别范围的规则适用

**可复用机制** · 检索有界规则时显式表示适用范围与例外，在固定评测预算下复核适用条件。

<a id="paper-138885"></a>

## CyberDualEval: Measuring Dual-Use Cyber Risks in Frontier Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/138885) · [作者来源](https://neurips.cc/virtual/2026/poster/138885)

- **问题 / 瓶颈** · 总体拒绝率无法区分过拒和过度协助
- **核心创新 / 方法** · 将防御分析准确性与边界判断分开评估
- **Baseline** · 不同前沿模型和助手配置
- **Benchmark** · 真实安全问题的防御性评估，聚焦分析和拒绝信号
- **关键结果 / 消融** · 同时观察到过度协助和过拒
- **适用条件 / 局限** · 摘要未给定量细节；结果依赖配置

**可复用机制** · 分别验证防御回答质量和拒绝校准，在固定评测预算下复核适用条件。

<a id="paper-153270"></a>

## CyCLeGen: Cycle-Consistent Layout Prediction and Image Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/153270) · [作者来源](https://openreview.net/forum?id=MUrqtx2pBo)

- **问题 / 瓶颈** · 单向训练不足以约束空间忠实性
- **核心创新 / 方法** · 双向强化学习结合几何与感知奖励
- **Baseline** · 具名对照待核
- **Benchmark** · 图像理解、生成和描述任务
- **关键结果 / 消融** · 8K 强化学习样本下报告多项改善
- **适用条件 / 局限** · 依赖逆向布局识别准确性

**可复用机制** · 用布局到图像再到布局的一致性作训练信号，在固定评测预算下复核适用条件。

<a id="paper-152695"></a>

## CycleSpectra: Cyclic Motion Spectra for Phase-Queryable 4D Cardiac Reconstruction

[官方论文页](https://neurips.cc/virtual/2026/poster/152695) · [作者来源](https://openreview.net/forum?id=R6WdWujy5S)

- **问题 / 瓶颈** · 离散帧拼接难保证周期闭合
- **核心创新 / 方法** · 从稀疏相位学习低维频谱并用解析层读出位移
- **Baseline** · 配准及时间条件重建等近期方法
- **Benchmark** · 心脏 CT 与跨模态 MR，测射血分数和容积曲线相关
- **关键结果 / 消融** · 两帧时报告最小射血分数误差与最高曲线相关
- **适用条件 / 局限** · 针对近似闭合周期

**可复用机制** · 用固定周期合成层查询任意相位，在固定评测预算下复核适用条件。

<a id="paper-155503"></a>

## Cyclic Discrete Diffusion: A Novel Multi-Class Segmentation Refinement Technique

[官方论文页](https://neurips.cc/virtual/2026/poster/155503) · [作者来源](https://openreview.net/forum?id=55XffjPoPJ)

- **问题 / 瓶颈** · 逐类二值处理削弱类别间一致性
- **核心创新 / 方法** · 用循环标签跳转构成有限状态扩散并分析谱隙
- **Baseline** · 二值精修和不同骨干
- **Benchmark** · 语义、实例及二值分割，比较区域与边界
- **关键结果 / 消融** · 报告多数据和骨干均改善
- **适用条件 / 局限** · 标签顺序敏感性待核

**可复用机制** · 在统一多类别标签空间精修分割，在固定评测预算下复核适用条件。

<a id="paper-155983"></a>

## Cylindrical Geodesic Flow Matching for Quasiperiodic Physiological Signal Transformation

[官方论文页](https://neurips.cc/virtual/2026/poster/155983) · [作者来源](https://openreview.net/forum?id=1NmpaqEwkP)

- **问题 / 瓶颈** · 仿射桥可能扭曲中间振幅和频率
- **核心创新 / 方法** · 用相位振幅圆柱测地线提供中间速度监督
- **Baseline** · 插值和直接监督预测
- **Benchmark** · 可穿戴心血管波形转换，测 Hilbert、L2 和 DTW 距离
- **关键结果 / 消融** · 相对最强对照最多约降 15%
- **适用条件 / 局限** · 依赖准周期与可用配对

**可复用机制** · 为周期信号选择尊重相位环绕的插值，在固定评测预算下复核适用条件。

<a id="paper-151535"></a>

## D$^2$Quant: Accurate Low-bit Post-Training Weight Quantization for LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/151535) · [作者来源](https://openreview.net/forum?id=Zx81NVkpZ2)

- **问题 / 瓶颈** · 低于四比特时降维层与激活偏移易导致退化
- **核心创新 / 方法** · 双尺度量化保持位宽，在 LayerNorm 中校正均值漂移
- **Baseline** · 低比特权重后训练量化
- **Benchmark** · 多项低于四比特模型评测，具名待核
- **关键结果 / 消融** · 作者报告优于对照，幅度待核
- **适用条件 / 局限** · 依赖校准数据与归一化结构

**可复用机制** · 分别处理降维投影保真和激活均值漂移，在固定评测预算下复核适用条件。

<a id="paper-153310"></a>

## D2D: Detector-to-Differentiable Critic for Improved Numeracy in Text-to-Image Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/153310) · [作者来源](https://openreview.net/forum?id=MFUdIySxW3)

- **问题 / 瓶颈** · 依赖枚举的计数不能直接提供梯度
- **核心创新 / 方法** · 将检测 logits 映射为软计数，推理时优化噪声先验
- **Baseline** · 回归计数评价器与原生成器
- **Benchmark** · 三种生成器和四项计数基准
- **关键结果 / 消融** · D2D-Small 计数准确率最高增 13.7%
- **适用条件 / 局限** · 依赖检测质量，遮挡可能误导梯度

**可复用机制** · 将检测器的计数信号改造为可微指导，在固定评测预算下复核适用条件。

<a id="paper-148695"></a>

## DACA-GRPO: Denoising-Aware Credit Assignment for Reinforcement Learning in Diffusion Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148695) · [作者来源](https://openreview.net/forum?id=vjbVsKvLXq)

- **问题 / 瓶颈** · 同等加权忽略步骤贡献，均值场估计偏差大
- **核心创新 / 方法** · 从中间预测提取进展分数，分层遮盖保留多数上下文
- **Baseline** · 三种 GRPO 底座
- **Benchmark** · 七项数学、代码和约束生成基准
- **关键结果 / 消融** · 数学最高增 5.6 个百分点，约束满足最高增 36.3 个百分点
- **适用条件 / 局限** · 依赖扩散预测轨迹，跨架构待核

**可复用机制** · 按去噪进展分配 token 权重并改进似然估计，在固定评测预算下复核适用条件。

<a id="paper-154329"></a>

## DACE: Diversity-Driven Adversarial Co-Evolution for Robust LLM Safety Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/154329) · [作者来源](https://neurips.cc/virtual/2026/poster/154329)

- **问题 / 瓶颈** · 只随新压力样本更新会丢掉旧有稳健性
- **核心创新 / 方法** · 对已验证的历史防御样本进行不确定性加权回放
- **Baseline** · 近期共训练与回放方法，具名待核
- **Benchmark** · 安全与通用能力评估
- **关键结果 / 消融** · 报告分布外稳健性改善并保持通用能力；独立贡献待核
- **适用条件 / 局限** · 整套实验不能单独证明回放效果

**可复用机制** · 用带不确定度的历史防御反馈降低遗忘，在固定评测预算下复核适用条件。

<a id="paper-156146"></a>

## DaCe-DT: Data-Centric Offline Multi-Task Reinforcement Learning via Adaptive Prompts and Trajectory Correction for Heterogeneous Tasks

[官方论文页](https://neurips.cc/virtual/2026/poster/156146) · [作者来源](https://openreview.net/forum?id=01tycO9CPF)

- **问题 / 瓶颈** · 随机提示与碎片轨迹削弱策略监督
- **核心创新 / 方法** · 联合长度门控、相关片段检索与价值自适应校正
- **Baseline** · 离线多任务强化学习方法
- **Benchmark** · Meta-World 的最优和次优数据
- **关键结果 / 消融** · 报告平均改善 11.73% 和 13.34%
- **适用条件 / 局限** · 依赖检索和价值估计质量

**可复用机制** · 按任务复杂度和轨迹质量调整提示和回报，在固定评测预算下复核适用条件。

<a id="paper-151411"></a>

## DACE RL for Compute Efficient Reinforcement Learning in Small Model Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/151411) · [作者来源](https://openreview.net/forum?id=asPNY0YBKr)

- **问题 / 瓶颈** · 固定超参难应对难度和训练状态变化
- **核心创新 / 方法** · 用平滑后的熵、多样性、优势饱和与一致性驱动预算和采样更新
- **Baseline** · 均匀预算 GRPO
- **Benchmark** · 三个小型底座和六项数学推理基准
- **关键结果 / 消融** · rollout GPU 小时降 38–52%，Pass@32 平均增 4.7 个百分点
- **适用条件 / 局限** · 域外及大模型适用性待核

**可复用机制** · 以训练诊断动态调整 rollout 预算，在固定评测预算下复核适用条件。

<a id="paper-153686"></a>

## DAGA: Dynamic Attention-Guided Adaptation for Self-Supervised Vision Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/153686) · [作者来源](https://openreview.net/forum?id=JYsS0zrDlk)

- **问题 / 瓶颈** · 静态适配忽略冻结骨干的图像特定语义。
- **核心创新 / 方法** · 将注意图转为空间和通道门，调节瓶颈适配器。
- **Baseline** · 近期 PEFT 方法。
- **Benchmark** · ImageNet-1K、ADE20K、CUB-200 和 FGVC-Aircraft。
- **关键结果 / 消融** · 增加 1.4% 参数，DINOv3-ViT-B 在 ImageNet-1K 达 85.9%。
- **适用条件 / 局限** · 在 MAE、CLIP 和 DeiT 上增益较小。

**可复用机制** · 固定适配预算，按骨干注意力质量比较条件门控和静态适配。

<a id="paper-155436"></a>

## DAG-Biased Graph Learning for Multimodal Survival on EHR

[官方论文页](https://neurips.cc/virtual/2026/poster/155436) · [作者来源](https://openreview.net/forum?id=5e6HZ4aFfT)

- **问题 / 瓶颈** · 自由学习邻接会形成密集双向边并过拟合。
- **核心创新 / 方法** · 逐模态学习邻接并加无环与稀疏约束，模态间用元邻接，再以软结构偏置多头注意。
- **Baseline** · 硬路由图及其他生存预测方法，具体名称待核。
- **Benchmark** · 五项 EHR 生存预测任务。
- **关键结果 / 消融** · 摘要报告错误或稀疏结构下传播退化较缓，定量结果待核。
- **适用条件 / 局限** · 学习到的图不可直接解释为因果关系。

**可复用机制** · 把图先验作为注意偏置，针对删边与错边测试稳健性。

<a id="paper-150664"></a>

## DAGent: Evaluate-then-Grow Planning for Deep Research Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/150664) · [作者来源](https://openreview.net/forum?id=gNnU6UhVDm)

- **问题 / 瓶颈** · 一次规划会在证据最少时承诺最多分支。
- **核心创新 / 方法** · 按批扩展 DAG，用已完成节点的不确定度驱动后续规划，并维护分层上下文。
- **Baseline** · 先规划再修补的 DAG 方案。
- **Benchmark** · 多来源深度研究任务，具体指标待核。
- **关键结果 / 消融** · 摘要提出增量扩张机制，定量预算收益待核。
- **适用条件 / 局限** · 依赖可靠的不确定度和中间证据评估。

**可复用机制** · 固定调用预算，比较提前建图与按证据逐轮扩张的无用分支数量。

<a id="paper-151308"></a>

## Dancing in Fetters: Pareto-Optimal On-Device LLMs under Hardware Constraints

[官方论文页](https://neurips.cc/virtual/2026/poster/151308) · [作者来源](https://openreview.net/forum?id=bR5Ck67tHh)

- **问题 / 瓶颈** · 每个模型都训练并实测会使端侧搜索成本过高。
- **核心创新 / 方法** · 以 170 个模型拟合架构到训练损失的关系，以 roofline 估计推理时延，搜索双目标前沿。
- **Baseline** · 与常规模型及候选实测对照，详细名称待核。
- **Benchmark** · Jetson Orin 上评估 1942 个候选架构。
- **关键结果 / 消融** · 作者报告可定位端侧性能与时延前沿；具体对照效应待核。
- **适用条件 / 局限** · 损失代理及硬件估计需要跨预算与设备校准。

**可复用机制** · 先对代理预测前沿抽样实测，再投入训练候选。

<a id="paper-155531"></a>

## Dandelions: A Spherical Flower for Neural Simulation of Planetary Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/155531) · [作者来源](https://openreview.net/forum?id=4sWdU0DnBl)

- **问题 / 瓶颈** · 欧氏算子在高纬和周期边界扭曲邻域。
- **核心创新 / 方法** · 预测切平面位移并沿大圆变形，使用球谐空间实现多尺度池化。
- **Baseline** · DeepSphere、DISCO、SFNO 等球面方案，实验对照待核。
- **Benchmark** · 原生球面 PDE，包含改造的 Galewsky 射流。
- **关键结果 / 消融** · 摘要给出球面无卷积架构与基准，逐任务效应待核。
- **适用条件 / 局限** · 球谐计算成本与分辨率边界需核实。

**可复用机制** · 对球面任务比较原生变形与重网格欧氏模型的高纬误差。

<a id="paper-148819"></a>

## DAPS: Dependency-Aware Premise Selection for LLM Theorem Proving

[官方论文页](https://neurips.cc/virtual/2026/poster/148819) · [作者来源](https://openreview.net/forum?id=uudLzL0d8u)

- **问题 / 瓶颈** · 逐对语义打分偏向高频引理。
- **核心创新 / 方法** · 结合 Mathlib 分型依赖和 53 个 Lean Blueprint 项目，通过邻域编码、组对比以及分阶段适配训练。
- **Baseline** · 语义相似度的神经前提选择。
- **Benchmark** · Lean 4 前提检索，Blueprint 有 3805 个正式或非正式节点。
- **关键结果 / 消融** · 具体检索及证明成功比例待核。
- **适用条件 / 局限** · 依赖可抽取的证明结构，跨库与新定理推广需复核。

**可复用机制** · 用未见项目和低频前提测试结构检索，避免仅报告总体召回。

<a id="paper-154306"></a>

## DARE: Dual-Level Adversarial Learning with Domain-Aware Regularization for Whole Slide Image Classification

[官方论文页](https://neurips.cc/virtual/2026/poster/154306) · [作者来源](https://openreview.net/forum?id=Eh2LNe24lx)

- **问题 / 瓶颈** · 制片和扫描差异跨尺度出现，单一对齐会负迁移。
- **核心创新 / 方法** · 教师学生产生目标域伪标签，对块和切片特征双层对齐，并加域感知正则。
- **Baseline** · 现有无监督域适配；具名方法待核。
- **Benchmark** · 跨机构全切片图像分类。
- **关键结果 / 消融** · 摘要报告方法旨在缓解负迁移，具体结果待核。
- **适用条件 / 局限** · 依赖目标域伪标签可靠性。

**可复用机制** · 若局部和整图的域差异不一致，分别消融两级对齐。

<a id="paper-148595"></a>

## DarkVGGT: Seeing Through Darkness Using Thermal Geometry without Daylight Tax

[官方论文页](https://neurips.cc/virtual/2026/poster/148595) · [作者来源](https://openreview.net/forum?id=wYQCa1v7gQ)

- **问题 / 瓶颈** · 颜色与反射变化使弱光重建证据不可靠。
- **核心创新 / 方法** · 分离热辐射几何线索与反射残差，再经共享几何路由把高可信线索注入可见流。
- **Baseline** · 可见光及现有多模态重建方法，名称待核。
- **Benchmark** · 低可见 RGB-T 重建和光照充足条件对照。
- **关键结果 / 消融** · 作者报告低光估计改善并大体保留明亮场景表现。
- **适用条件 / 局限** · 需双模态标定；热反射分解的环境边界待核。

**可复用机制** · 融合时按几何可信度注入辅助模态，并检验主模态已足够时的性能回退。

<a id="paper-151097"></a>

## DARLING: Detection Augmented Reinforcement Learning with Non-Stationary Guarantees

[官方论文页](https://neurips.cc/virtual/2026/poster/151097) · [作者来源](https://openreview.net/forum?id=d0ltzL90Cg)

- **问题 / 瓶颈** · 分段平稳 MDP 的奖励和转移会在未知时间改变。
- **核心创新 / 方法** · 用模块化变化检测增强无模型策略，并推导表格及线性设定的动态遗憾下界。
- **Baseline** · 已有非平稳强化学习算法和极小极大下界。
- **Benchmark** · 分段平稳表格及线性 MDP；动态遗憾。
- **关键结果 / 消融** · 满足分离及可达条件的表格设定可达下界，线性情形另需已知相关参数。
- **适用条件 / 局限** · 难分辨变化或未知线性可达参数可能破坏保证。

**可复用机制** · 报告重训练前明确变化可分辨性和采样可达性。

<a id="paper-152813"></a>

## DARPAN: Controllability-Aware Residual Filtering for Pretrained Physical Control

[官方论文页](https://neurips.cc/virtual/2026/poster/152813) · [作者来源](https://openreview.net/forum?id=QENhKkAMiO)

- **问题 / 瓶颈** · 原始预测误差混合了可控偏差和外生漂移。
- **核心创新 / 方法** · 在预训练物理控制策略之上过滤历史残差，重点更新动作敏感部分。
- **Baseline** · 预训练序列控制或原始误差适配，具体对照待核。
- **Benchmark** · 含延迟的物理控制场景。
- **关键结果 / 消融** · 隔离外生漂移与可控误差的定量结果待核。
- **适用条件 / 局限** · 动作敏感性估计需可信，并考虑迟滞。

**可复用机制** · 测试适配时分别施加执行器偏移和外生扰动，比较过滤前后。

<a id="paper-152532"></a>

## DART: Domain-Agnostic Residual Transfer for Generalist Anomaly Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/152532) · [作者来源](https://openreview.net/forum?id=SSOyQ68YQj)

- **问题 / 瓶颈** · 纹理和成像条件会污染可迁移异常特征。
- **核心创新 / 方法** · 在残差与检测头之间加入解耦模块，用跨域元训练保持异常判别并压制域信息。
- **Baseline** · 多种基础异常检测方法。
- **Benchmark** · MVTec AD、VisA 和 BraTS 的跨域异常检测。
- **关键结果 / 消融** · 作者报告各基础方法均有改善，更强域移下增益更大。
- **适用条件 / 局限** · 依赖参考异常及源域覆盖。

**可复用机制** · 按偏移强度测残差模块，并对照仅改变元训练。

<a id="paper-151821"></a>

## DARTS: Targeting Prognostic Covariates in Budget-Constrained Sequential Experiments

[官方论文页](https://neurips.cc/virtual/2026/poster/151821) · [作者来源](https://openreview.net/forum?id=Xj4Qs8GucY)

- **问题 / 瓶颈** · 高维测量成本与协变量调整精度相冲突。
- **核心创新 / 方法** · 预算约束 Thompson 采样选变量，随后重随机化和回归调整。
- **Baseline** · 已知协变量与预算约束实验方案，详待核。
- **Benchmark** · 分批随机实验，评估处理效应估计方差与覆盖。
- **关键结果 / 消融** · 作者给出批内随机化有效性和渐近覆盖，并给出近极小极大采集风险。
- **适用条件 / 局限** · 依赖以过去批次做选择，而非当前批次结果。

**可复用机制** · 将测量预算选择与批内分配分离来维持设计推断。

<a id="paper-155299"></a>

## DART: Zero-Shot Dual-Side Alignment Routing for LLM Performance-Cost Tradeoffs

[官方论文页](https://neurips.cc/virtual/2026/poster/155299) · [作者来源](https://openreview.net/forum?id=6cPZndmGS6)

- **问题 / 瓶颈** · 表面语义及离散模型标识不利于未见模型路由。
- **核心创新 / 方法** · 用需求编码器表示查询所需能力，用元数据和模型家族图初始化供应侧模型嵌入。
- **Baseline** · 语义匹配及离散模型标识路由。
- **Benchmark** · 语言模型效果与费用折衷，具体模型及指标待核。
- **关键结果 / 消融** · 摘要给出零样本接入机制，定量结果待核。
- **适用条件 / 局限** · 依赖家族和元数据能预测新模型能力。

**可复用机制** · 以留出模型家族评估路由器，单独列接入成本。

<a id="paper-151399"></a>

## DashAttention: Differentiable and Adaptive Sparse Hierarchical Attention

[官方论文页](https://neurips.cc/virtual/2026/poster/151399) · [作者来源](https://openreview.net/forum?id=axGCEGSg4a)

- **问题 / 瓶颈** · 固定 top-k 忽略查询密度差异且切断跨层梯度。
- **核心创新 / 方法** · 粗层用 α-entmax 自适应选块并为细粒度 softmax 提供先验。
- **Baseline** · 全注意力、NSA 和 InfLLMv2。
- **Benchmark** · 语言模型长上下文与高稀疏率比较。
- **关键结果 / 消融** · 摘要报告 75% 稀疏度时准确度可比全注意力。
- **适用条件 / 局限** · 实际吞吐依赖不规则块访问和 GPU 实现。

**可复用机制** · 用同等稀疏预算比较固定 top-k 与可微动态支持集。

<a id="paper-155623"></a>

## DASM: Dynamic Autoregressive Subgraph Mining via Two-Stage Policy Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/155623) · [作者来源](https://openreview.net/forum?id=4CA3Tomjpr)

- **问题 / 瓶颈** · 静态扩张难适应不同结构，逐步监督也面临暴露偏差。
- **核心创新 / 方法** · 先以多标签和非对称 F1 做候选节点监督，再以 GRPO 优化端到端质量和停止决策。
- **Baseline** · 静态子图抽取及逐步监督，具体方法待核。
- **Benchmark** · 种子节点出发的子图挖掘。
- **关键结果 / 消融** · 停止与质量的具体定量对照待核。
- **适用条件 / 局限** · 终止奖励须与下游子图目标一致。

**可复用机制** · 对图扩张分别评估下一步节点与整体停止质量。

<a id="paper-149310"></a>

## DASS: A Solver-Agnostic Dynamic Auxiliary Search Strategy for Symbolic Regression

[官方论文页](https://neurips.cc/virtual/2026/poster/149310) · [作者来源](https://openreview.net/forum?id=r8CiyuxeA4)

- **问题 / 瓶颈** · 表达式组合数使符号回归搜索低效。
- **核心创新 / 方法** · 跨环境评估基函数项，过滤不稳定候选，以 Gibbs 后验和已获优解更新潜力。
- **Baseline** · 不使用辅助子空间的符号回归求解器。
- **Benchmark** · 符号回归精度和搜索效率，基准详待核。
- **关键结果 / 消融** · 作者提出求解器无关的指导方法，收益量级待核。
- **适用条件 / 局限** · 需可构造基函数并取得可信的多环境评估。

**可复用机制** · 把候选项指导与求解器解耦并在相同计算预算下比较。

<a id="paper-151478"></a>

## Data-Adaptive Mahalanobis Metric Learning for Cross-Head Attention in Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/151478) · [作者来源](https://openreview.net/forum?id=aK0LiJE4IQ)

- **问题 / 瓶颈** · 多头注意的分块度量忽略头间关系。
- **核心创新 / 方法** · 学习完整跨头 Mahalanobis 型度量，使其随输入变化并用跨层共享约束开销。
- **Baseline** · 标准多头注意及变体。
- **Benchmark** · Transformer 表达能力及学习效果，具体指标待核。
- **关键结果 / 消融** · 摘要报告表达与学习优势，计算及消融细节待核。
- **适用条件 / 局限** · 完整度量可能增加计算并诱发过拟合。

**可复用机制** · 用相同容量对照块对角、静态全矩阵和动态全矩阵。

<a id="paper-154287"></a>

## Data Auctions for Retrieval Augmented Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/154287) · [作者来源](https://openreview.net/forum?id=EtzYBT7sG8)

- **问题 / 瓶颈** · 数据只能给一个购买者时，福利最大化困难，直接近似分配不能保证诚实。
- **核心创新 / 方法** · 用覆盖估值建模，以分配后处理调整分配来恢复激励相容。
- **Baseline** · 常用组合拍卖基线。
- **Benchmark** · 合成及真实图像和文本数据；福利与激励相容性。
- **关键结果 / 消融** · 作者给出 1−1/e 近似与激励相容性结果，报告实验有效。
- **适用条件 / 局限** · 依赖该覆盖估值与专属分配假设。

**可复用机制** · 将求解效率与激励条件分别验证，避免把福利近似视为机制可用。

<a id="paper-138991"></a>

## DataComp-VLM: Improved open datasets for Vision-Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/138991) · [作者来源](https://openreview.net/forum?id=s8J0YiyTuN)

- **问题 / 瓶颈** · 不同语料、模型和训练预算使数据选择收益难以归因。
- **核心创新 / 方法** · 统一四类数据格式，让筛选、混合与采样在多个模型和预算下比较。
- **Baseline** · 标题或指令主导混合及不同过滤策略。
- **Benchmark** · 160 个数据集，1B–8B 模型、6.25B–200B token 预算，最多 52 个评测。
- **关键结果 / 消融** · 摘要报告指令占比较高的混合扩展更好，8B 模型在 33 项核心评测达 63.6%。
- **适用条件 / 局限** · 结论依赖所测试模型族、配比及评测任务。

**可复用机制** · 先固定过滤再扫描数据配比，检验收益排序是否随训练规模变化。

<a id="paper-149999"></a>

## Data-Constrained Language Model Pretraining: Improved Regularization and Scaling Laws

[官方论文页](https://neurips.cc/virtual/2026/poster/149999) · [作者来源](https://openreview.net/forum?id=lYgfGE5Vvq)

- **问题 / 瓶颈** · 数据重复使单轮训练缩放规律失准。
- **核心创新 / 方法** · 加入随机掩码输入的辅助下词预测；SoftQ 显式耦合数据与规模。
- **Baseline** · 强权重衰减及经典加性缩放律。
- **Benchmark** · 72M 至 1.4B 模型多轮预训练。
- **关键结果 / 消融** · 摘要报告验证损失降低，1.4B 有下游增益。
- **适用条件 / 局限** · 辅助目标与缩放律的外推范围待核。

**可复用机制** · 有限语料下独立比较掩码辅助监督与单纯增强权重衰减。

<a id="paper-150410"></a>

## Data Density Scaling Laws for Image Self-Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/150410) · [作者来源](https://openreview.net/forum?id=iFfvOd4ve5)

- **问题 / 瓶颈** · 样本重复的效用随数据域变化。
- **核心创新 / 方法** · 把唯一图像数与每图重复次数拆入缩放模型。
- **Baseline** · 传统 Chinchilla 式拟合。
- **Benchmark** · Maxar、Waymo 与 ImageNet 图像自蒸馏。
- **关键结果 / 消融** · 作者发现部分设置下重复小子集优于更多唯一数据。
- **适用条件 / 局限** · 收益取决于子集多样性与训练域。

**可复用机制** · 固定训练步数扫描唯一图像和重复次数，按域拟合响应。

<a id="paper-155264"></a>

## Data Diversity Drives the Emergence of Symbolic Mechanisms Supporting Abstract Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/155264) · [作者来源](https://openreview.net/forum?id=6zzLcq5wNY)

- **问题 / 瓶颈** · 抽象推理的符号机制来源不清。
- **核心创新 / 方法** · 改变抽象序列词表大小与架构，测表示、注意和因果中介。
- **Baseline** · 不同词表规模及 Transformer 变体和 MLP。
- **Benchmark** · 抽象序列及系统性分布外泛化。
- **关键结果 / 消融** · 符号迹象随多样性增强，也出现于 MLP。
- **适用条件 / 局限** · 证据来自受控任务，不能直接外推大型预训练。

**可复用机制** · 验证新推理机制时控制训练多样性再比较架构。

<a id="paper-155410"></a>

## Data-Driven Covariate Selection for Nonparametric and Cycle-Agnostic Causal Effect Estimation

[官方论文页](https://neurips.cc/virtual/2026/poster/155410) · [作者来源](https://openreview.net/forum?id=5rgmG7fjJh)

- **问题 / 瓶颈** · 反馈环与潜在混杂使调整集难定。
- **核心创新 / 方法** · 利用条件独立在 sigma 去环化下不变，将局部筛选保证扩展到有环图。
- **Baseline** · 无环模型的同一筛选方法及全局结构学习。
- **Benchmark** · 有环合成因果模型。
- **关键结果 / 消融** · 工作给出有环情况下的理论保证与合成验证。
- **适用条件 / 局限** · 依赖可用的条件独立信息及论文模型假设。

**可复用机制** · 存在反馈时，先验证局部调整条件再决定是否需要估计全图。

<a id="paper-150257"></a>

## Data-Driven Soft Labeling Scales DNA Read Classification to Whole-Body Cell-Type Deconvolution

[官方论文页](https://neurips.cc/virtual/2026/poster/150257) · [作者来源](https://openreview.net/forum?id=jY2nvX28FP)

- **问题 / 瓶颈** · 异质观测可对应多个类别，硬标签引入矛盾。
- **核心创新 / 方法** · 用条件类别分布代替单一类别监督。
- **Baseline** · 现有混合比例估计方法。
- **Benchmark** · 公开人体组织观测的类别比例估计。
- **关键结果 / 消融** · 作者报告误差下降且可跨组织验证。
- **适用条件 / 局限** · 仅覆盖论文所测观测分布。

**可复用机制** · 多类弱监督中比较软标签与硬标签对校准和聚合误差的影响。

<a id="paper-150335"></a>

## Data-Efficient Learning for Constraint Satisfaction Problems via  Relational Biases and Hard Axiom Clamping

[官方论文页](https://neurips.cc/virtual/2026/poster/150335) · [作者来源](https://openreview.net/forum?id=ism9H7dCPG)

- **问题 / 瓶颈** · 循环求解时已知线索会漂移。
- **核心创新 / 方法** · 以关系偏置编码约束拓扑，每轮恢复固定线索。
- **Baseline** · Trial & Error 2025。
- **Benchmark** · 数独 RRN 和 Kaggle、图着色、二值谜题。
- **关键结果 / 消融** · RRN 数独整盘准确率 99.94%。
- **适用条件 / 局限** · 需显式约束图与可靠固定约束。

**可复用机制** · 将不可改变量从自由预测中分离，并检验每轮钳制的收益。

<a id="paper-139364"></a>

## DataFlex: A Unified Benchmark and Evaluation Platform for Data-Centric Training of Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139364) · [作者来源](https://openreview.net/forum?id=Uaf41CPesH)

- **问题 / 瓶颈** · 数据选择代码与训练设置混杂对比。
- **核心创新 / 方法** · 固定种子、数据划分与训练设施比较十个数据策略。
- **Baseline** · 静态全量训练、DoReMi 与 ODM 等。
- **Benchmark** · Mistral-7B 和 Llama-3.2-3B，包含 MMLU。
- **关键结果 / 消融** · 摘要报告动态选择有收益，小模型增益最多 13.3 分。
- **适用条件 / 局限** · 结论受模型和语料限制。

**可复用机制** · 评测数据算法时统一训练协议并按模型尺寸及资源域分别报告。

<a id="paper-152919"></a>

## Data-Free Metrics Are Not Invariant Under Functionality-Preserving Reparametrisations

[官方论文页](https://neurips.cc/virtual/2026/poster/152919) · [作者来源](https://openreview.net/forum?id=PQie2dx3oX)

- **问题 / 瓶颈** · 数据无关的层指标可能受参数表示影响。
- **核心创新 / 方法** · 构造功能不变的重参数化，检验随机矩阵指标稳定性。
- **Baseline** · 原模型与稳健层重初始化变体。
- **Benchmark** · 多个架构与规模；具体清单待核。
- **关键结果 / 消融** · 作者发现模型功能相同时，部分指标可任意变化。
- **适用条件 / 局限** · 结论针对所考察指标与变换。

**可复用机制** · 用函数等价模型做指标不变性测试，再将指标用于压缩选层。

<a id="paper-154499"></a>

## Data-Free Reservoir Features for Efficient Long-Horizon Cold-Start Continual Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/154499) · [作者来源](https://openreview.net/forum?id=D9TG2PKiJD)

- **问题 / 瓶颈** · 冷启动增量训练容易遗忘或形成首任务偏置。
- **核心创新 / 方法** · 冻结随机二维储备池特征，以流式线性判别头更新并做预测集成。
- **Baseline** · 持续更新骨干及首任务后冻结骨干。
- **Benchmark** · 无回放冷启动类别增量图像分类。
- **关键结果 / 消融** · 作者给出逐样本闭式更新方案；数值待核。
- **适用条件 / 局限** · 固定随机特征能力与集成预算需评估。

**可复用机制** · 在极少初始数据时加入随机固定特征加在线头作为低成本对照。

<a id="paper-139023"></a>

## Dataset Collections: Challenges of Large-Scale Data Aggregation in 3D Medical Image Datasets

[官方论文页](https://neurips.cc/virtual/2026/poster/139023) · [作者来源](https://openreview.net/forum?id=pv8FxEsBFY)

- **问题 / 瓶颈** · 聚合公开影像容易掩盖来源与重复。
- **核心创新 / 方法** · 从数据来源、复用、泄漏和分布多个维度审计集合。
- **Baseline** · 单数据集管理与聚合版本；具名对照待核。
- **Benchmark** · 大规模三维放射影像集合。
- **关键结果 / 消融** · 摘要讨论复用传播和泄漏等失效风险，量化待核。
- **适用条件 / 局限** · 证据来自所研究的影像集合。

**可复用机制** · 合并公共数据时保留来源图，并按原始来源核查训练测试交叉。

<a id="paper-155633"></a>

## Dataset Distillation via Drifting

[官方论文页](https://neurips.cc/virtual/2026/poster/155633) · [作者来源](https://openreview.net/forum?id=477JMtoDLS)

- **问题 / 瓶颈** · 像素级逼近不保证小数据能训练好分类器。
- **核心创新 / 方法** · 用合成样本诱导与真实数据相似的线性头训练信号。
- **Baseline** · 真实图像子集及不同预训练骨干。
- **Benchmark** · 线性探针，含 DINO 蒸馏数据迁移至 CLIP。
- **关键结果 / 消融** · 作者报告优于所测真实子集并能跨骨干迁移。
- **适用条件 / 局限** · 跨骨干结果限所测模型及任务。

**可复用机制** · 用冻结骨干的训练贡献筛小数据，并检查换骨干后的收益。

<a id="paper-151119"></a>

## Dataset Mismatch Matters in Group Relative Policy Optimization for Reinforcement Learning from Verifiable Rewards

[官方论文页](https://neurips.cc/virtual/2026/poster/151119) · [作者来源](https://openreview.net/forum?id=cqgCrzAcDZ)

- **问题 / 瓶颈** · 仅按源提示筛选无法修正目标分布偏移。
- **核心创新 / 方法** · 用目标验证准确率驱动双层源提示重加权，并惩罚增量信息低的 rollout。
- **Baseline** · 源侧选择式 GRPO。
- **Benchmark** · 六个数学推理基准、三种模型规模。
- **关键结果 / 消融** · 作者报告评测重加权效果，具体幅度待核。
- **适用条件 / 局限** · 依赖可共享的目标验证反馈。

**可复用机制** · 目标数据不可共享时，可用汇总验证信号更新源任务分配。

<a id="paper-153138"></a>

## DAWN: Dependency-Aware Fast Inference for Diffusion LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/153138) · [作者来源](https://openreview.net/forum?id=NbRKV16cev)

- **问题 / 瓶颈** · 并行解掩码忽略待预测 token 间依赖。
- **核心创新 / 方法** · 用依赖图挑选受已知位置支持且相互干扰较小的并行位置。
- **Baseline** · 扩散模型并行解码基线。
- **Benchmark** · 多个模型和数据集的速度与生成质量。
- **关键结果 / 消融** · 作者报告 1.80 至 8.06 倍加速。
- **适用条件 / 局限** · 调度收益依赖依赖估计及成本。

**可复用机制** · 在同质量预算下对照按置信度和按依赖结构批量解码。

<a id="paper-154080"></a>

## DBPS: Doob-Bridge Posterior Sampler with Balanced Endpoint-Population Control for Unpaired Neurodegenerative Pathology Transport

[官方论文页](https://neurips.cc/virtual/2026/poster/154080) · [作者来源](https://openreview.net/forum?id=GLIYSpGCJP)

- **问题 / 瓶颈** · 独立端点快照不足以确定个体演变。
- **核心创新 / 方法** · 以可调权重组合端点和总体引导构造随机桥。
- **Baseline** · 纯端点桥、纯总体及其他无配对传输。
- **Benchmark** · 公开观察影像队列的终点分布拟合。
- **关键结果 / 消融** · 作者报告混合设置改善终点拟合。
- **适用条件 / 局限** · 观察拟合不能验证个体纵向轨迹。

**可复用机制** · 无配对传输中扫描个体与总体引导权重并保留两个边界基线。

<a id="paper-148857"></a>

## DC-DiT: Adaptive Compute and Elastic Inference for Visual Generation via Dynamic Chunking

[官方论文页](https://neurips.cc/virtual/2026/poster/148857) · [作者来源](https://openreview.net/forum?id=ue644x6zvR)

- **问题 / 瓶颈** · 固定图块对平滑和细节区域分配相同预算。
- **核心创新 / 方法** · 训练路由器动态聚合图块，并保留 token 优先级供弹性推理。
- **Baseline** · 固定切块 DiT。
- **Benchmark** · ImageNet 条件生成，测 FLOPs 和 FID。
- **关键结果 / 消融** · 最多减 36.8% FLOPs，FID 最多改善 37.8%。
- **适用条件 / 局限** · 收益依赖图像和去噪阶段。

**可复用机制** · 比较按内容及时间步压缩与固定 token 预算的质量计算曲线。

<a id="paper-152997"></a>

## DC-Ocean: Deep Latent Compression for Global High-Resolution Ocean Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/152997) · [作者来源](https://openreview.net/forum?id=Ok9b0N26E1)

- **问题 / 瓶颈** · 陆海边界和多深度变量使普通降采样失真。
- **核心创新 / 方法** · 以边界门控卷积与球面插值保护海岸，结合全局注意力编码。
- **Baseline** · 图像域自编码器移植基线，匹配下采样率。
- **Benchmark** · 多变量多深度全球海洋重建及潜空间预报。
- **关键结果 / 消融** · 作者报告重建保真度改善；长时指标待核。
- **适用条件 / 局限** · 边界和变量分布改变时需重测。

**可复用机制** · 分别报告近边界和远场误差，并测压缩对滚动预报的影响。

<a id="paper-152595"></a>

## DC-SAE: Deep Compression Semantic Autoencoder for Faster Diffusion Convergence

[官方论文页](https://neurips.cc/virtual/2026/poster/152595) · [作者来源](https://openreview.net/forum?id=Rx1xVinvFW)

- **问题 / 瓶颈** · 高压缩难兼顾像素重建和扩散收敛。
- **核心创新 / 方法** · 将语义编码和低层像素细节编码分开。
- **Baseline** · VAE 和预训练语义表征自编码器。
- **Benchmark** · 图像生成与重建评估。
- **关键结果 / 消融** · 作者报告高压缩下训练和重建表现改善，详值待核。
- **适用条件 / 局限** · 两路编码的预算及单独贡献待核。

**可复用机制** · 在固定潜空间大小下对照单语义编码与保留像素支路。

<a id="paper-152806"></a>

## DCVD: Dual-Channel Cross-Modal Fusion for Joint Vulnerability Detection and Localization

[官方论文页](https://neurips.cc/virtual/2026/poster/152806) · [作者来源](https://openreview.net/forum?id=QFBbFDJdtz)

- **问题 / 瓶颈** · 函数告警不足以支持维护者定位修复。
- **核心创新 / 方法** · 结合结构和语义表示，并监督函数级与语句级检测。
- **Baseline** · 既有检测与定位方法。
- **Benchmark** · 公开软件漏洞防御审计基准。
- **关键结果 / 消融** · 作者报告检测与定位均改善，幅度待核。
- **适用条件 / 局限** · 应评估跨项目误报与维护者复核成本。

**可复用机制** · 为授权代码审计分别测全局检出与定位质量，保留人工确认。

<a id="paper-150507"></a>

## DC-ViT: Modulating Spatial and Channel Interactions for Multi-Channel Images

[官方论文页](https://neurips.cc/virtual/2026/poster/150507) · [作者来源](https://openreview.net/forum?id=hZtke2JkSA)

- **问题 / 瓶颈** · 无约束混合稀释多通道图像的各通道语义。
- **核心创新 / 方法** · 将空间内更新与跨通道更新分开，并以任务适配通道聚合。
- **Baseline** · 联合注意力的多通道 ViT。
- **Benchmark** · 异构多通道影像；具体数据和指标待核。
- **关键结果 / 消融** · 摘要报告通道语义保持和表现改善。
- **适用条件 / 局限** · 通道缺失和传感变化仍需测试。

**可复用机制** · 对照共享注意力和解耦交互，按通道组合报告稳健性。

<a id="paper-154024"></a>

## DDACOM: Dual-Decoupled Adaptive Communication for Multi-Agent Reinforcement Learning under Dynamic Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/154024) · [作者来源](https://openreview.net/forum?id=Gp5eu43iRL)

- **问题 / 瓶颈** · 固定网络训练不能应对部署带宽变化。
- **核心创新 / 方法** · 分离消息生成、发送与控制，用反馈估计发送预算。
- **Baseline** · 固定带宽与重要性筛选方法。
- **Benchmark** · SMAC、MPE 协作任务。
- **关键结果 / 消融** · 作者报告协作表现提升，数值待核。
- **适用条件 / 局限** · 带宽估计与反馈延迟会影响调度。

**可复用机制** · 在波动带宽下分别评估消息价值和发送策略，以同字节预算比较。
