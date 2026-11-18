# NeurIPS 2026 论文卡 4

[会议索引](README.md)

<a id="paper-150523"></a>

## Decentralized Aggregation of LLM Predictions via Wagering Mechanisms

[官方论文页](https://neurips.cc/virtual/2026/poster/150523) · [作者来源](https://openreview.net/forum?id=hTh1EZEUym)

- **问题 / 瓶颈** · 集中式权重不便独立学习
- **核心创新 / 方法** · 各模型提交概率和优势赌注，以留一得分确定激励
- **Baseline** · 集中式集成基线
- **Benchmark** · 问答与预测基准
- **关键结果 / 消融** · 作者报告与集中式可比，并给出占优策略激励保证
- **适用条件 / 局限** · 两机制在归一性和无套利间取舍

**可复用机制** · 比较集中权重和可独立学习的优势加权，同时测校准。

<a id="paper-151009"></a>

## Decentralized Coupled Representation Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151009) · [作者来源](https://openreview.net/forum?id=dcWLsSqiXL)

- **问题 / 瓶颈** · 采样和表征共同演化可能使子空间退化
- **核心创新 / 方法** · 推导Langevin极限与含正交Lyapunov函数的平均流
- **Baseline** · 离散过程和平均连续极限的理论对照
- **Benchmark** · 随机几何图与连续流形
- **关键结果 / 消融** · 谱隙下平均轨迹行空间收敛至主特征空间
- **适用条件 / 局限** · 依赖图缩放、时标分离及谱隙

**可复用机制** · 在耦合估计中单独核查正交性与时标。

<a id="paper-151866"></a>

## Decentralized Multi-Goal Multi-Agent Pathfinding with Spatial Prior and Neighbor Intent Prediction

[官方论文页](https://neurips.cc/virtual/2026/poster/151866) · [作者来源](https://openreview.net/forum?id=XIPf6xYobP)

- **问题 / 瓶颈** · 目标次序冲突会在相同区域堆积拥堵
- **核心创新 / 方法** · 高层均衡目标和路径，低层预测邻居意图并用协作PPO执行
- **Baseline** · 最佳分散式路径基线
- **Benchmark** · 多目标多智能体路径任务，聚合路径成本SoC
- **关键结果 / 消融** · 较最佳分散基线平均降低19.77%
- **适用条件 / 局限** · 要求已分配目标且模型能观测局部意图线索

**可复用机制** · 分别消融全局疏导和局部意图，按密度报告拥堵。

<a id="paper-155245"></a>

## Decentralized Q-Learning in Markov Potential Games

[官方论文页](https://neurips.cc/virtual/2026/poster/155245) · [作者来源](https://openreview.net/forum?id=7AKNXrGEF8)

- **问题 / 瓶颈** · 固定探索对罕见和常见状态配置相同预算
- **核心创新 / 方法** · 各智能体独立更新Q，并用在线访问率调整响应平滑度
- **Baseline** · 持续θ-greedy独立学习
- **Benchmark** · 无限时域折扣马尔可夫势博弈与路由实验
- **关键结果 / 消融** · 证明几乎必然收敛到近似纳什集合
- **适用条件 / 局限** · 需全局状态和势博弈结构

**可复用机制** · 对稀有状态提高探索并核对访问估计误差。

<a id="paper-151288"></a>

## Decentralized Ranking Aggregation via Gossip: Convergence and Robustness

[官方论文页](https://neurips.cc/virtual/2026/poster/151288) · [作者来源](https://openreview.net/forum?id=bX0ELaA3QT)

- **问题 / 瓶颈** · 偏好记录分散且可能污染
- **核心创新 / 方法** · 用 gossip 聚合分散的偏好排序
- **Baseline** · 集中式中位排序及传统 gossip
- **Benchmark** · 通信网络上的排序共识
- **关键结果 / 消融** · 分析收敛与对污染的稳健性
- **适用条件 / 局限** · 具体图条件待核

**可复用机制** · 在节点间传递排序信息求共识；以卡片中的对照设置验证。

<a id="paper-152927"></a>

## Deceptive Grounding: Entity Attribution Failure in Clinical Retrieval-Augmented Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/152927) · [作者来源](https://openreview.net/forum?id=PL3EWYRq36)

- **问题 / 瓶颈** · 引用正确仍可能归错实体
- **核心创新 / 方法** · 用因子评测和移除实体证据的消融区分错误归因与编造
- **Baseline** · 普通忠实度和引用检查
- **Benchmark** · 13 个模型的临床 RAG 因子评测
- **关键结果 / 消融** · 峰值归因错误率为 8% 至 87%，移除实体证据后转为编造
- **适用条件 / 局限** · 受控场景的峰值不能外推部署频率

**可复用机制** · 独立检查证据与被查询实体是否一致；以卡片中的对照设置验证。

<a id="paper-149170"></a>

## Decide Before You Record: Heterogeneity-Guided Pre-Acquisition Stimulus Selection for Cross-Day Neuroprostheses

[官方论文页](https://neurips.cc/virtual/2026/poster/149170) · [作者来源](https://openreview.net/forum?id=sM47HO1iDP)

- **问题 / 瓶颈** · 被动记录导致跨日校准成本高
- **核心创新 / 方法** · 用句子对齐路径熵量化异质性指导校准采集
- **Baseline** · 被动采集后适配
- **Benchmark** · 日间颅内脑电语言解码
- **关键结果 / 消融** · 摘要报告可用较针对性的校准数据
- **适用条件 / 局限** · 适用范围和数据量待核

**可复用机制** · 采集校准信号前按跨日异质性选择刺激；以卡片中的对照设置验证。

<a id="paper-155924"></a>

## Decision-Aware Proximal Bridge Learning for Optimal Treatment Selection

[官方论文页](https://neurips.cc/virtual/2026/poster/155924) · [作者来源](https://openreview.net/forum?id=1mkWNVA6c7)

- **问题 / 瓶颈** · 全局准确率可能掩盖最优动作附近的误差
- **核心创新 / 方法** · 加权拟合近端因果桥函数并保留全局稳定项
- **Baseline** · 全局桥函数估计后优化
- **Benchmark** · 有潜在混杂和代理变量的连续动作决策
- **关键结果 / 消融** · 目标是改善策略决策，详细结果待核
- **适用条件 / 局限** · 需要代理识别假设

**可复用机制** · 按决策相关动作区域分配因果拟合权重；以卡片中的对照设置验证。

<a id="paper-149225"></a>

## Decision-Focused Learning in MDPs: An Occupancy Measure Approach

[官方论文页](https://neurips.cc/virtual/2026/poster/149225) · [作者来源](https://openreview.net/forum?id=rzZPOKJV34)

- **问题 / 瓶颈** · 对全部状态动作的 Bellman 条件求导成本高
- **核心创新 / 方法** · 用活动约束求导，并用随机约束草图与软状态聚合改善连续性和规模
- **Baseline** · Bellman KKT 求导
- **Benchmark** · 有限及连续状态 MDP
- **关键结果 / 消融** · 摘要给出梯度构造和可扩展近似
- **适用条件 / 局限** · 活动约束改变会造成梯度跳跃

**可复用机制** · 在预测动力学时通过占用测度规划反传；以卡片中的对照设置验证。

<a id="paper-151045"></a>

## Decision Focused Scenario Learning for Contextual Stochastic Programming

[官方论文页](https://neurips.cc/virtual/2026/poster/151045) · [作者来源](https://openreview.net/forum?id=dPKq7jP43J)

- **问题 / 瓶颈** · 两阶段随机规划的情景生成存在可表示性和不可微问题
- **核心创新 / 方法** · 证明单个支持集外情景分量可能足够，并分析对数障碍平滑
- **Baseline** · 对随机二阶段分量有限制的方法
- **Benchmark** · 上下文两阶段随机规划
- **关键结果 / 消融** · 得到情景分量的等价性及平滑优化结果
- **适用条件 / 局限** · 充分条件需对照具体问题

**可复用机制** · 按决策质量而非仅按分布拟合选择情景；以卡片中的对照设置验证。

<a id="paper-153801"></a>

## Decision Path Tracing for Causal Analysis in Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/153801) · [作者来源](https://openreview.net/forum?id=IbpdnkjhTP)

- **问题 / 瓶颈** · 枚举所有 Transformer 路径成本高
- **核心创新 / 方法** · 自动跟踪决策路径并干预验证
- **Baseline** · 非路径组件
- **Benchmark** · Transformer 类别处理和稀疏干预
- **关键结果 / 消融** · 路径受干预后自修复较少，观察到跨类别共享模块
- **适用条件 / 局限** · 可迁移性需跨模型核查

**可复用机制** · 用干预后自修复差异检查路径是否承载决策；以卡片中的对照设置验证。

<a id="paper-154405"></a>

## Decoding the Critique Mechanism in Large Reasoning Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154405) · [作者来源](https://openreview.net/forum?id=Dpd5naao28)

- **问题 / 瓶颈** · 显式自我纠错不能覆盖隐式恢复
- **核心创新 / 方法** · 插入算术错误后比较中间状态和最终答案，分析内部特征方向
- **Baseline** · 未显式纠错与显式纠错案例
- **Benchmark** · 多个规模推理模型的算术过程
- **关键结果 / 消融** · 观察到未口头修正仍得出正确答案
- **适用条件 / 局限** · 不能直接外推到开放任务

**可复用机制** · 同时测错误中间步骤与最终恢复；以卡片中的对照设置验证。

<a id="paper-156777"></a>

## DecompDreamer: A Composition-Aware Curriculum for Structured 3D Asset Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/156777) · [作者来源](https://neurips.cc/virtual/2026/poster/156777)

- **问题 / 瓶颈** · 联合优化导致组件梯度冲突
- **核心创新 / 方法** · 分阶段建立空间骨架与细化对象
- **Baseline** · 同时优化及迭代启发式
- **Benchmark** · 组合提示的文本到三维
- **关键结果 / 消融** · 摘要报告保真、解耦及空间一致性提升
- **适用条件 / 局限** · 依赖初始关系骨架质量

**可复用机制** · 先定对象关系再细化部件；以卡片中的对照设置验证。

<a id="paper-152463"></a>

## Decomposed Graded Verifier for Generative World Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/152463) · [作者来源](https://openreview.net/forum?id=SvcdFlTvuz)

- **问题 / 瓶颈** · 二元验证给出的训练反馈太粗
- **核心创新 / 方法** · 按子目标分级评分，有真值图像时比较成对验证
- **Baseline** · 二元与逐点评分
- **Benchmark** · 文生图与生成式世界建模
- **关键结果 / 消融** · 作者报告逐项评分优于二元对照，分析了成对验证条件
- **适用条件 / 局限** · 成对验证需要可取参考图

**可复用机制** · 把复杂目标拆成可评分子项；以卡片中的对照设置验证。

<a id="paper-149003"></a>

## Decomposed Representations Mitigate the Alignment–Specificity Trade-off in Multi-Omics

[官方论文页](https://neurips.cc/virtual/2026/poster/149003) · [作者来源](https://openreview.net/forum?id=tY6lfTLggZ)

- **问题 / 瓶颈** · 对齐目标与分类目标可能竞争
- **核心创新 / 方法** · 将输入分成分别承载互补角色的表示
- **Baseline** · 只优化模态对齐或融合的方法
- **Benchmark** · 共测多模态观测数据的检索、补全和分类
- **关键结果 / 消融** · 摘要提出按任务测各表示的作用
- **适用条件 / 局限** · 限观察数据表示，不外推干预

**可复用机制** · 独立保留共享、私有及融合信息；以卡片中的对照设置验证。

<a id="paper-152875"></a>

## Decompose the Distillation: Interpretable Single-Pass Guidance for Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152875) · [作者来源](https://openreview.net/forum?id=PiKPINkvGh)

- **问题 / 瓶颈** · 单步近似常混合基础预测与引导
- **核心创新 / 方法** · 在冻结骨干共享特征上用两个低秩适配器预测基础流和引导方向
- **Baseline** · 双前向 CFG 与单前向替代
- **Benchmark** · 条件图像生成及推理引导尺度调节
- **关键结果 / 消融** · 适配器各增约 2.5% 参数，一次前向后可动态调尺度
- **适用条件 / 局限** · 具体画质和速度权衡待核

**可复用机制** · 单次前向保留可独立调节的引导方向；以卡片中的对照设置验证。

<a id="paper-152417"></a>

## Decomposing and Reshaping Scaling Laws through Token Learning Times

[官方论文页](https://neurips.cc/virtual/2026/poster/152417) · [作者来源](https://openreview.net/forum?id=THZDVZArRH)

- **问题 / 瓶颈** · 总体幂律无法说明各样本何时被学到
- **核心创新 / 方法** · 用 sigmoid 拟合逐 token 损失轨迹并汇总学习时谱
- **Baseline** · 基于难度分布的聚合解释
- **Benchmark** · 百余次预训练，最高 6B 参数及 300B token
- **关键结果 / 消融** · 可重建验证损失对训练步、数据量及模型规模的导数
- **适用条件 / 局限** · 依赖拟合形状和训练分布

**可复用机制** · 追踪单 token 学习时间解释总体损失变化；以卡片中的对照设置验证。

<a id="paper-149998"></a>

## Decomposing Conformal Uncertainty: Calibration- and Instance-Driven Feature Attribution

[官方论文页](https://neurips.cc/virtual/2026/poster/149998) · [作者来源](https://openreview.net/forum?id=lZavBaxJ68)

- **问题 / 瓶颈** · 直接解释区间宽度会混合两种不确定性
- **核心创新 / 方法** · 为校准集和测试点分别构造特征归因游戏
- **Baseline** · 直接对总区间做局部归因
- **Benchmark** · 合成及实际数据的分割共形预测
- **关键结果 / 消融** · 两分量常呈反向作用
- **适用条件 / 局限** · 要求区间大小可分成校准项和实例项

**可复用机制** · 分别归因校准样本与测试实例的区间宽度；以卡片中的对照设置验证。

<a id="paper-150168"></a>

## Decomposing Earth Embeddings with Sparse Autoencoders

[官方论文页](https://neurips.cc/virtual/2026/poster/150168) · [作者来源](https://openreview.net/forum?id=kB29xkjNQK)

- **问题 / 瓶颈** · 原始嵌入混合多个物理概念
- **核心创新 / 方法** · 用稀疏自编码器提取字典并按参考产品评估
- **Baseline** · 原始嵌入及三类稀疏自编码器
- **Benchmark** · AlphaEarth 与 Tessera 的空间特征
- **关键结果 / 消融** · 三类方案均优于原始嵌入，Matryoshka 表现最好
- **适用条件 / 局限** · 空间自相关及参考标签可能影响解释

**可复用机制** · 用地理一致性和标签恢复评估地球表示分解；以卡片中的对照设置验证。

<a id="paper-151693"></a>

## Decomposing Effects in Neural Causal Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151693) · [作者来源](https://openreview.net/forum?id=Yjey5dh4Et)

- **问题 / 瓶颈** · 相同图并不保证网络干预语义相同
- **核心创新 / 方法** · 以图网络构造不同的子机制分解并比较干预
- **Baseline** · 每条结构方程单独拟合
- **Benchmark** · 神经结构因果模型理论
- **关键结果 / 消融** · 给出经典模型之外两类参数化
- **适用条件 / 局限** · 需要核查各参数共享机制的假设

**可复用机制** · 把因果图固定后比较子机制的参数共享；以卡片中的对照设置验证。

<a id="paper-153074"></a>

## Decomposing how prompting steers behavior

[官方论文页](https://neurips.cc/virtual/2026/poster/153074) · [作者来源](https://openreview.net/forum?id=OBmtKw49N3)

- **问题 / 瓶颈** · 提示改变行为但表示机制难定位
- **核心创新 / 方法** · 拟合逐级表达能力的映射，在留出输入上替换隐藏态验证
- **Baseline** · 平移、刚体、缩放、仿射与非线性映射
- **Benchmark** · 三种语言模型、三种视觉语言模型和六个数据集
- **关键结果 / 消融** · 同时以表示及行为恢复验证解释
- **适用条件 / 局限** · 覆盖的提示族有限

**可复用机制** · 比较哪种低复杂度映射解释提示变化；以卡片中的对照设置验证。

<a id="paper-149560"></a>

## Decomposing SGD Dynamics in Neural Networks: Teacher-Induced Spikes and Variance Inflation

[官方论文页](https://neurips.cc/virtual/2026/poster/149560) · [作者来源](https://openreview.net/forum?id=pCMDLPWcuw)

- **问题 / 瓶颈** · 相同训练误差仍可能对应不同泛化
- **核心创新 / 方法** · 将首层分成教师信号与正交项，分析协方差谱和替代动力学
- **Baseline** · 训练或冻结正交分量
- **Benchmark** · 两层网络、多指数教师的比例极限
- **关键结果 / 消融** · 发现教师相关谱尖峰及冻结改善泛化的区间
- **适用条件 / 局限** · 依赖已知教师分解及极限条件

**可复用机制** · 检查无关子空间方差再决定是否冻结；以卡片中的对照设置验证。

<a id="paper-152921"></a>

## Decomposing Temporal and Job-Induced Dynamics for Probabilistic Computing Workload Forecasting via Graph-Conditioned Dual-Branch Diffusion

[官方论文页](https://neurips.cc/virtual/2026/poster/152921) · [作者来源](https://openreview.net/forum?id=PQGRbKCkdM)

- **问题 / 瓶颈** · 仅使用利用率历史会忽略共同作业引起的波动
- **核心创新 / 方法** · 从调度日志构图并以时间和作业两支路预测扩散噪声
- **Baseline** · 只建模时间相关的方法
- **Benchmark** · 数据中心概率负载预测
- **关键结果 / 消融** · 作者报告波动结构随作业共现而变
- **适用条件 / 局限** · 依赖调度日志，具体增益待核

**可复用机制** · 引入随调度变化的机器依赖预测负载；以卡片中的对照设置验证。

<a id="paper-152282"></a>

## Decomposing the modulation of interactions between neuronal populations

[官方论文页](https://neurips.cc/virtual/2026/poster/152282) · [作者来源](https://openreview.net/forum?id=UFTQ6XUIb3)

- **问题 / 瓶颈** · 加性子空间无法解释第三变量的调节
- **核心创新 / 方法** · 将低秩张量作为降秩回归的双线性扰动
- **Baseline** · 加性通信子空间
- **Benchmark** · 模拟与同时钙成像
- **关键结果 / 消融** · 模拟恢复调节结构，实测显示调节不对称
- **适用条件 / 局限** · 观测关联不能识别因果

**可复用机制** · 分别诊断已有通道变化与新通道出现

<a id="paper-153116"></a>

## Deconstructing Multi-Task Active Learning: The Paradox of Gradient Conflict and Orthogonal Decomposition

[官方论文页](https://neurips.cc/virtual/2026/poster/153116) · [作者来源](https://openreview.net/forum?id=NnPRFtAI1U)

- **问题 / 瓶颈** · 线性合并信息性和多样性可能选中离群样本
- **核心创新 / 方法** · 先投影筛信息性，再做流形覆盖，另估计跨任务依赖
- **Baseline** · 多任务主动学习方法
- **Benchmark** · COCO、Cityscapes、NYUv2
- **关键结果 / 消融** · 作者报告稳定改善
- **适用条件 / 局限** · 依赖梯度度量与任务组成

**可复用机制** · 独立消融冲突采样和梯度手术

<a id="paper-148478"></a>

## DeCoRL: Decomposed Consistency Reinforcement Learning for Multi-Image Composition

[官方论文页](https://neurips.cc/virtual/2026/poster/148478) · [作者来源](https://openreview.net/forum?id=xVnuPOotSj)

- **问题 / 瓶颈** · 整体监督难定位参考对象失配
- **核心创新 / 方法** · 定位参考与生成对象，再聚合单对象一致性评分做强化后训练
- **Baseline** · 监督微调与现有方法
- **Benchmark** · DeCo-Bench、MICo-Bench，含二至六参考图
- **关键结果 / 消融** · 摘要报告一致性有提升
- **适用条件 / 局限** · 依赖对应定位与奖励可靠性

**可复用机制** · 将全局图像偏好拆成可定位的检查项

<a id="paper-149572"></a>

## Decoupled Complementary Fields on 3D Gaussian Maps for Embodied Navigation and Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/149572) · [作者来源](https://openreview.net/forum?id=p8mGm9kb7M)

- **问题 / 瓶颈** · 混合证据缺口和环境可靠性会干扰目标选择
- **核心创新 / 方法** · 在线高斯地图保留证据，分开建模查询歧义与环境就绪性
- **Baseline** · 语义地图及导航方案
- **Benchmark** · A-EQA、GOAT-Bench
- **关键结果 / 消融** · 作者报告证据采集和终局决策改善
- **适用条件 / 局限** · 依赖在线重建质量

**可复用机制** · 对照单一探索分数与双场决策

<a id="paper-152459"></a>

## Decoupled Descent: Exact Test Error Tracking Via Approximate Message Passing

[官方论文页](https://neurips.cc/virtual/2026/poster/152459) · [作者来源](https://openreview.net/forum?id=Sycq4iSaqb)

- **问题 / 瓶颈** · 训练误差可能逐轮偏离测试误差
- **核心创新 / 方法** · 通过近似消息传递思想抵消数据复用引入的偏差
- **Baseline** · 普通梯度下降
- **Benchmark** · XOR、带噪 MNIST、CIFAR-10 非线性探测
- **关键结果 / 消融** · 特定高斯混合中渐近一致，扩展实验报告差距缩小
- **适用条件 / 局限** · 理论条件专门化，不能取消常规验证

**可复用机制** · 在模拟已知分布下检查训练误差能否跟踪独立测试

<a id="paper-150180"></a>

## Decoupled Mode Connectivity for Base-to-Novel Generalization in Vision-Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150180) · [作者来源](https://openreview.net/forum?id=k6ybSN5XjO)

- **问题 / 瓶颈** · 两个目标共用提示时梯度相悖
- **核心创新 / 方法** · 双提示用低损失插值走廊连接，锚定预训练类别相似性
- **Baseline** · CoOp、KgCoOp、MMA
- **Benchmark** · 十一数据集，比较基础和未见类准确率
- **关键结果 / 消融** · 多数配置两类准确率均改善
- **适用条件 / 局限** · 迁移依赖正则的类别置换性质

**可复用机制** · 用双端点插值检查是否改善原有权衡

<a id="paper-149914"></a>

## Decoupled Optimization for Teacher-Student Semi-Supervised Learning via a Pioneer Student

[官方论文页](https://neurips.cc/virtual/2026/poster/149914) · [作者来源](https://openreview.net/forum?id=mFnnOgbOQs)

- **问题 / 瓶颈** · 师生同步及有标签梯度主导限制学习
- **核心创新 / 方法** · 独立参数训练先导学生并周期回传知识
- **Baseline** · 主流师生半监督方法
- **Benchmark** · 多种半监督设置，数据集待核
- **关键结果 / 消融** · 摘要报告普遍提升
- **适用条件 / 局限** · 回传频率和新增训练开销待核

**可复用机制** · 对照同预算的独立支路和共享参数

<a id="paper-151599"></a>

## Decoupled Prototype Contrastive Alignment Hashing for Cross-Modal Retrieval

[官方论文页](https://neurips.cc/virtual/2026/poster/151599) · [作者来源](https://openreview.net/forum?id=ZMcdN863jM)

- **问题 / 瓶颈** · 单层对齐难兼顾语义与离散码
- **核心创新 / 方法** · Transformer 抽取图文交互，双层对比目标加解耦原型一致性
- **Baseline** · 无监督跨模态哈希方法
- **Benchmark** · 三个图文检索基准，名称待核
- **关键结果 / 消融** · 摘要报告优于对照
- **适用条件 / 局限** · 独立原型项的贡献待核

**可复用机制** · 分开测连续表示质量与码检索精度

<a id="paper-151316"></a>

## Decoupled Safety Control: A Safety-Control Algorithm for Training-Free Safety Guidance

[官方论文页](https://neurips.cc/virtual/2026/poster/151316) · [作者来源](https://openreview.net/forum?id=bOS8epZNuS)

- **问题 / 瓶颈** · 同一条件同时定义风险和干预，容易殃及正常语义
- **核心创新 / 方法** · 以当前生成状态决定推理期间的安全干预
- **Baseline** · 潜空间与文本空间防护
- **Benchmark** · 图像生成安全评测
- **关键结果 / 消融** · 作者报告抑制增强且正常质量保持
- **适用条件 / 局限** · 基准覆盖与误判边界待核

**可复用机制** · 同时报告正常提示保真和安全违规率

<a id="paper-152818"></a>

## Decoupling Action from Egocentric Observation for World Simulation

[官方论文页](https://neurips.cc/virtual/2026/poster/152818) · [作者来源](https://openreview.net/forum?id=QAYW75ayLF)

- **问题 / 瓶颈** · 显式几何估计会有误差，运动表征又可能丢失接触
- **核心创新 / 方法** · 早期锚定手物结构，中后期校准稀疏对应
- **Baseline** · 显式几何控制与运动迁移方法
- **Benchmark** · EgoActionBench，含动作保留与交互可信度
- **关键结果 / 消融** · 摘要报告交互更合理且更连贯
- **适用条件 / 局限** · 生成视频不能直接保证物理接触正确

**可复用机制** · 在跨场景动作迁移中分别消融早期结构约束和后期校准

<a id="paper-151800"></a>

## Decoupling Conversational Dynamics in Full-Duplex Spoken Models through Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151800) · [作者来源](https://openreview.net/forum?id=Xv1Cz6907L)

- **问题 / 瓶颈** · 对话时序训练可能削弱指令及推理能力
- **核心创新 / 方法** · 在高影响对话窗口分解发起、反馈、让话等奖励
- **Baseline** · 原指令模型及全双工模型
- **Benchmark** · 全双工对话、推理与指令跟随
- **关键结果 / 消融** · 作者报告时序改善并保持语义能力
- **适用条件 / 局限** · 评测人群和延迟条件待核

**可复用机制** · 独立度量语义质量及插话恢复

<a id="paper-149168"></a>

## Decoupling Direction and Magnitude: Language-Steered Flow Matching for Super-Resolution in the Dark

[官方论文页](https://neurips.cc/virtual/2026/poster/149168) · [作者来源](https://openreview.net/forum?id=sMFrrQ0Yyf)

- **问题 / 瓶颈** · 全局统一强度会过度修改可靠区域
- **核心创新 / 方法** · 条件语言及图像 token 定方向，空间步长场定更新幅度
- **Baseline** · 全局步长的扩散或流匹配
- **Benchmark** · 成对与真实暗光图像，含消融
- **关键结果 / 消融** · 摘要报告一步恢复有效
- **适用条件 / 局限** · 真实严重退化的幻觉风险待核

**可复用机制** · 同一速度场对照固定和局部步长

<a id="paper-154428"></a>

## Decoupling Exploration and Policy Optimization: Uncertainty Guided Tree Search for Hard Exploration

[官方论文页](https://neurips.cc/virtual/2026/poster/154428) · [作者来源](https://openreview.net/forum?id=DfrwtUhLEr)

- **问题 / 瓶颈** · 仅为扩大状态覆盖运行策略优化开销高
- **核心创新 / 方法** · 用不确定性驱动树搜索收集轨迹，再做监督反向学习
- **Baseline** · 内在动机强化学习
- **Benchmark** · Montezuma、Pitfall、Venture、Adroit、AntMaze
- **关键结果 / 消融** · 作者报告探索效率约高一个数量级
- **适用条件 / 局限** · 搜索保存和回访状态的成本待核

**可复用机制** · 分别计算探索和策略部署成本

<a id="paper-149216"></a>

## Decoupling is the Key: Scaling Deep Value Networks in Reinforcement Leanring

[官方论文页](https://neurips.cc/virtual/2026/poster/149216) · [作者来源](https://openreview.net/forum?id=s2GEGdj4Dh)

- **问题 / 瓶颈** · 深层价值网络易谱塌缩且拟合目标噪声
- **核心创新 / 方法** · 解耦谱成分和分布边界目标，离线时分离策略价值学习
- **Baseline** · 耦合式价值更新及浅层网络
- **Benchmark** · 在线和离线强化学习，三至三十二层价值网络
- **关键结果 / 消融** · 报告随深度增加表现改善
- **适用条件 / 局限** · 任务依赖与计算预算待核

**可复用机制** · 扫描深度并同时观测有效秩和回报

<a id="paper-154393"></a>

## Decoupling Label Shift and Surrogate Gradient Errors for Robust Federated Spiking Neural Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/154393) · [作者来源](https://openreview.net/forum?id=DuuJjNysv1)

- **问题 / 瓶颈** · 标签偏移使膜电位离开替代梯度敏感区
- **核心创新 / 方法** · 自适应时空发放阈值与两层级蒸馏
- **Baseline** · 联邦脉冲网络方法
- **Benchmark** · 三个数据集，含严重标签偏移
- **关键结果 / 消融** · 作者报告全局和客户端表现改善
- **适用条件 / 局限** · 通信与训练成本待核

**可复用机制** · 同时追踪局部梯度有效性与全局分类

<a id="paper-150052"></a>

## Decoupling Time and Risk: Risk-Sensitive Reinforcement Learning with General Discounting

[官方论文页](https://neurips.cc/virtual/2026/poster/150052) · [作者来源](https://openreview.net/forum?id=l7UJw4SS0u)

- **问题 / 瓶颈** · 指数折扣难覆盖复杂跨期偏好
- **核心创新 / 方法** · 以广义折扣建模多时域回报，再优化分布风险度量
- **Baseline** · 现有单时域方法
- **Benchmark** · 理论最优性与数值实验，具体任务待核
- **关键结果 / 消融** · 报告多时域版本修正既有缺陷
- **适用条件 / 局限** · 非指数折扣的适用条件待核

**可复用机制** · 分别扫描折扣函数与风险度量的政策影响

<a id="paper-152326"></a>

## DecQ: Detail-Condensing Queries for Enhanced Reconstruction and Generation in Representation Autoencoders

[官方论文页](https://neurips.cc/virtual/2026/poster/152326) · [作者来源](https://openreview.net/forum?id=TujfWq01JT)

- **问题 / 瓶颈** · 直接微调可能破坏语义空间
- **核心创新 / 方法** · 查询聚合中间层细节，与图块 token 共同生成并供解码
- **Baseline** · 冻结 DINOv2 的 RAE
- **Benchmark** · 重建 PSNR 与生成 FID
- **关键结果 / 消融** · 八个查询使 PSNR 19.13 到 22.76 dB，新增计算 3.9%
- **适用条件 / 局限** · 不同骨干及图像编辑的泛化待核

**可复用机制** · 固定骨干比较细节查询和全量微调

<a id="paper-151979"></a>

## DEDCA: Test-Time Adaptation for Generalized AI-Generated Image Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/151979) · [作者来源](https://openreview.net/forum?id=WP9ROPHHjk)

- **问题 / 瓶颈** · 单一证据遇未知生成器容易偏移
- **核心创新 / 方法** · 融合语义与生成痕迹，由可靠性门控调权
- **Baseline** · 现有图像检测和测试时适配方法
- **Benchmark** · GenImage，平均准确率
- **关键结果 / 消融** · 摘要报告 92.0%
- **适用条件 / 局限** · 证据共同失效及流式变化待核

**可复用机制** · 在未知来源验证双证据适配与单分支的表现

<a id="paper-150425"></a>

## DeepArrhythmia: Segment-Contextualized ECG Arrhythmia Classification via Selective Evidence Acquisition

[官方论文页](https://neurips.cc/virtual/2026/poster/150425) · [作者来源](https://openreview.net/forum?id=i8JkJYOjY6)

- **问题 / 瓶颈** · 孤立心搏分析忽视节律和邻近形态
- **核心创新 / 方法** · 组合信号及渲染波形，使用专用测量工具提取节律形态，按置信度路由
- **Baseline** · 孤立心搏与固定证据方法，具体待核
- **Benchmark** · 多心搏 ECG 分类，具体数据集待核
- **关键结果 / 消融** · 摘要未提供性能数值
- **适用条件 / 局限** · 需验证跨设备和人群校准，不能据此临床部署

**可复用机制** · 在固定计算预算比较选择性与全量证据

<a id="paper-151777"></a>

## Deep Barycentric Regression for Optimal Transport Map Estimation and its Statistical Optimality

[官方论文页](https://neurips.cc/virtual/2026/poster/151777) · [作者来源](https://openreview.net/forum?id=Y6gjRpnLxO)

- **问题 / 瓶颈** · 参数化极小极大估计可能不稳定
- **核心创新 / 方法** · 先算无正则传输计划，再以重心目标做神经网络最小二乘
- **Baseline** · 非参数和参数化传输估计方法
- **Benchmark** · 合成、图像及无监督域适配
- **关键结果 / 消融** · 在 Lipschitz 映射和正则条件下达极小极大速率，实验报告有竞争力
- **适用条件 / 局限** · 先求传输计划的规模成本待核

**可复用机制** · 将样本匹配和映射拟合分开评估

<a id="paper-153820"></a>

## Deep Double Q-learning

[官方论文页](https://neurips.cc/virtual/2026/poster/153820) · [作者来源](https://openreview.net/forum?id=IT8wbomtEn)

- **问题 / 瓶颈** · 目标与在线估计相关，仍会高估
- **核心创新 / 方法** · 显式训练两个 Q 函数，结合较低回放比和较慢目标更新
- **Baseline** · Double DQN
- **Benchmark** · 57 个 Atari 游戏
- **关键结果 / 消融** · 47 个游戏优于基线且高估降低
- **适用条件 / 局限** · 共享层可能仍引入相关性

**可复用机制** · 用同预算比较两个显式估计器与单估计器目标解耦。

<a id="paper-155011"></a>

## Deep Ensembles for Epistemic Uncertainty: A Frequentist Perspective

[官方论文页](https://neurips.cc/virtual/2026/poster/155011) · [作者来源](https://openreview.net/forum?id=9FW7gD5kYf)

- **问题 / 瓶颈** · 深集成的认知不确定性缺乏频率学解释
- **核心创新 / 方法** · 证明 bootstrap 估计渐近正确，再将其拆成两部分
- **Baseline** · 深集成与 bootstrap
- **Benchmark** · 经验不确定性分解，数据集待核
- **关键结果 / 消融** · 训练随机性在所测设定占多数
- **适用条件 / 局限** · 占比可能随数据及训练设置而变

**可复用机制** · 用重复采样和重复初始化分别测量两类方差。

<a id="paper-139410"></a>

## DeepfakeGenome: Toward Next-Generation Deepfake Attribution

[官方论文页](https://neurips.cc/virtual/2026/poster/139410) · [作者来源](https://openreview.net/forum?id=SLFrtKUAas)

- **问题 / 瓶颈** · 二分类分数饱和，难反映实际归因
- **核心创新 / 方法** · 为伪造检测与归因构建四种协议，含检索式归因
- **Baseline** · 已有开放集归因指标
- **Benchmark** · DeepfakeGenome，100 种算法、约 200 万图像
- **关键结果 / 消融** · 作者报告逾两千次评测，细项待核
- **适用条件 / 局限** · 只覆盖数据集所含的人脸生成来源

**可复用机制** · 将真假识别、已知来源归因和未知来源检索拆开评估。

<a id="paper-155757"></a>

## Deep Gaussian Processes on Directed Acyclic Graphs

[官方论文页](https://neurips.cc/virtual/2026/poster/155757) · [作者来源](https://openreview.net/forum?id=39DTnj1MzT)

- **问题 / 瓶颈** · 串行深核叠加可能丢失输入差异
- **核心创新 / 方法** · 构建 DAG 深高斯过程与保留图依赖的结构化变分推断
- **Baseline** · 核类、连接拓扑及中间观测的理论对照
- **Benchmark** · 潜变量碰撞结构及多保真重离子模拟等
- **关键结果 / 消融** · 给出保留输入可区分深度频率的下界，并报告多保真贡献可恢复
- **适用条件 / 局限** · 依赖图结构与所设核类

**可复用机制** · 比较独立近似和保留依赖的近似是否能复现碰撞点条件化效应。

<a id="paper-151547"></a>

## Deep Generative Models for Phylogenetic Inference with Complex Evolutionary Processes

[官方论文页](https://neurips.cc/virtual/2026/poster/151547) · [作者来源](https://openreview.net/forum?id=ZpGlbpubQi)

- **问题 / 瓶颈** · 复杂演化模型下基于似然的树后验难算
- **核心创新 / 方法** · 仿真训练按自顶向下、中部向外或自底向上生成树的离散扩散模型
- **Baseline** · Phyloformer 2 和错设的传统推断
- **Benchmark** · 仿真及真实系统发育数据
- **关键结果 / 消融** · 三种方案均改善拟合，作者报告真实数据后验更准
- **适用条件 / 局限** · 仿真过程错设仍可能影响校准

**可复用机制** · 对树结构模拟推断固定训练数据，比较不同树构造顺序的后验拟合表现。

<a id="paper-151494"></a>

## Deep Heteroskedastic Regression: Post-Hoc Variance Estimation from Latent Representations

[官方论文页](https://neurips.cc/virtual/2026/poster/151494) · [作者来源](https://openreview.net/forum?id=aFEmSFmQld)

- **问题 / 瓶颈** · 联合训练易出现方差过拟合及表示退化
- **核心创新 / 方法** · 用留出集在预训练网络中间表示上训练方差头
- **Baseline** · 端到端均值方差网络
- **Benchmark** · 多模态异方差回归
- **关键结果 / 消融** · 摘要报告不确定性表现有竞争力且保留均值精度
- **适用条件 / 局限** · 需可靠留出数据，偏移下的校准待核

**可复用机制** · 在同预算下比较后置方差头与联合训练，分别测均值和校准。

<a id="paper-152578"></a>

## Deep-Koopman-KANDy: Dictionary Discovery for Deep-Koopman Operators with Kolmogorov-Arnold Networks for Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/152578) · [作者来源](https://openreview.net/forum?id=S1pUNll4Zb)

- **问题 / 瓶颈** · 固定候选库限制发现，无结构潜变量难解释
- **核心创新 / 方法** · 用 KAN 编解码和水平集及链式梯度关系读出 Koopman 字典
- **Baseline** · EDMD、SINDy、KANDy 与普通深 Koopman 为方法比较背景
- **Benchmark** · Lorenz、Chirikov、Ikeda 和 Arnold 猫映射
- **关键结果 / 消融** · Lorenz 字典召回完整，Jaccard 0.79±0.06；负对照未找到稀疏闭包
- **适用条件 / 局限** · 读出仍受候选基约束，不能保证闭包存在

**可复用机制** · 将训练和字典选择分离，并加入不存在有限闭包的负对照。

<a id="paper-151589"></a>

## Deep Learning as Neural Low-Degree Filtering: A Spectral Theory of Hierarchical Feature Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151589) · [作者来源](https://openreview.net/forum?id=ZRp3Qmrbhu)

- **问题 / 瓶颈** · 随机特征近似看不到梯度学习如何产生特征
- **核心创新 / 方法** · 用 Neural LoFi 将逐层更新近似为选择和标签有最大可及低阶相关的方向
- **Baseline** · 随机特征基线
- **Benchmark** · 全连接和卷积架构的机制实验
- **关键结果 / 消融** · 报告优于随机特征并能预测早期梯度学习表示
- **适用条件 / 局限** · 属于特定训练极限的代理

**可复用机制** · 对照低阶谱相关与实际梯度学习到的早期表示。

<a id="paper-151498"></a>

## Deep Learning-based Algebraic Reynolds Stress Closures for RANS simulations of Turbulent Flows

[官方论文页](https://neurips.cc/virtual/2026/poster/151498) · [作者来源](https://openreview.net/forum?id=aDNQ6nqqKm)

- **问题 / 瓶颈** · 离线闭合部署时遇到分布偏移
- **核心创新 / 方法** · 网络调节隐式雷诺应力方程参数，以结构化伴随穿过耦合求解
- **Baseline** · 基础 RANS、张量基网络、DeepONet、PINN 等
- **Benchmark** · 方形管道和周期丘陵
- **关键结果 / 消融** · 跨条件速度误差较 RANS 降至约二分之一至四分之一
- **适用条件 / 局限** · 依赖弱平衡假设和求解器结构

**可复用机制** · 单独对照离线与求解内训练，并用未见流态测闭合误差。

<a id="paper-152977"></a>

## Deep Minds and Shallow Probes

[官方论文页](https://neurips.cc/virtual/2026/poster/152977) · [作者来源](https://openreview.net/forum?id=OwCwpsL5eB)

- **问题 / 瓶颈** · 等价网络的隐藏坐标可因重参数化而不同
- **核心创新 / 方法** · 从仿射群作用推导浅层探针层级，以可见商空间支持跨模型迁移
- **Baseline** · 线性探针和二阶探针
- **Benchmark** · 合成及真实任务，具名基准待核
- **关键结果 / 消融** · 作者报告二阶探针的补充价值和跨族覆盖感知迁移
- **适用条件 / 局限** · 精确理论限于最终读出层

**可复用机制** · 比较探针迁移前后覆盖，并验证隐藏坐标改变不影响结果。

<a id="paper-148229"></a>

## Deep Probabilistic Supervision for Image Classification

[官方论文页](https://neurips.cc/virtual/2026/poster/148229) · [作者来源](https://openreview.net/forum?id=zQY7TOySRe)

- **问题 / 瓶颈** · 硬标签易诱导过度自信
- **核心创新 / 方法** · 用贝叶斯推断形成概率目标，初始化后摆脱硬目标
- **Baseline** · 既有自蒸馏方法
- **Benchmark** · ImageNet、CIFAR-100 与标签噪声对照
- **关键结果 / 消融** · 摘要报告示例精度提高 2.0%，ECE 下降 40%
- **适用条件 / 局限** · 初始化和目标推断假设的敏感性待核

**可复用机制** · 同一骨干分别对照硬目标和样本级概率目标，测准确率与校准。

<a id="paper-153616"></a>

## Deep Reasoning in General Purpose Agents via Structured Meta-Cognition

[官方论文页](https://neurips.cc/virtual/2026/poster/153616) · [作者来源](https://openreview.net/forum?id=K4JhviyO5S)

- **问题 / 瓶颈** · 固定脚手架遇到任务结构变化会失效
- **核心创新 / 方法** · 以形式语言组织关联推断、计算和递归求解并保留依赖
- **Baseline** · 既有通用和任务特化脚手架
- **Benchmark** · 多跳推理、长链问答、长上下文聚合和研究任务
- **关键结果 / 消融** · 作者报告比最强对照平均提高 24.8%
- **适用条件 / 局限** · 复杂分解可能增加调度成本

**可复用机制** · 按结构和调用负载比较动态分解与固定脚手架。

<a id="paper-153645"></a>

## Deep Research as Rubric

[官方论文页](https://neurips.cc/virtual/2026/poster/153645) · [作者来源](https://openreview.net/forum?id=JmP1iLzzlJ)

- **问题 / 瓶颈** · 静态量规可能漏掉任务特异正确性
- **核心创新 / 方法** · 先检索事实和失败模式，再蒸馏成独立约束供 GRPO
- **Baseline** · 外部强模型量规及自举量规版本
- **Benchmark** · 六个研究与专家推理基准
- **关键结果 / 消融** · 约 1K–3K 训练样本即可取得有竞争力表现，自举第三轮最佳
- **适用条件 / 局限** · 检索质量会传递到奖励

**可复用机制** · 固定样本量对照静态与证据生成量规，检查量规是否覆盖真实失败。

<a id="paper-155301"></a>

## DeepVoting: Learning and Improving Voting Rules with Fine-Tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/155301) · [作者来源](https://openreview.net/forum?id=6biK4w9ftC)

- **问题 / 瓶颈** · 公理不兼容时无法要求零违规
- **核心创新 / 方法** · 用社会选择特征拟合原规则，微调时同时控制行为漂移和新增公理违规
- **Baseline** · 原投票规则及已有学习规则
- **Benchmark** · 规则拟合准确率与公理满足度
- **关键结果 / 消融** · 作者报告减少参数且逼近不可兼得边界
- **适用条件 / 局限** · 不能消除公理冲突，结果取决于偏好分布

**可复用机制** · 用保真度与公理违规的双指标选择聚合规则。

<a id="paper-154918"></a>

## Default Feature Representations of the Cognitive Map

[官方论文页](https://neurips.cc/virtual/2026/poster/154918) · [作者来源](https://openreview.net/forum?id=9zIIpQP6FM)

- **问题 / 瓶颈** · 环境变化后重学完整预测地图成本高
- **核心创新 / 方法** · 固定特征基和环境算子分解，已知变化可闭式求解，未知时用 TD 更新
- **Baseline** · 后继表征与基于模型的版本
- **Benchmark** · 重规划任务和局部变化下的网格细胞现象
- **关键结果 / 消融** · 无模型版本接近有模型并超后继表征基线
- **适用条件 / 局限** · 依赖固定特征覆盖新环境

**可复用机制** · 局部环境变化时对照只更新算子和重学完整地图。

<a id="paper-152017"></a>

## Defense-as-Skill: Evolving Runtime Guard Skill for Skill-Augmented Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/152017) · [作者来源](https://neurips.cc/virtual/2026/poster/152017)

- **问题 / 瓶颈** · 仅安装时审查难反映具体任务中的风险
- **核心创新 / 方法** · 以独立守护模块将动作分流到放行、重规划或确认
- **Baseline** · 具名防御对照待核
- **Benchmark** · SCOPE-R，Claude Code 及 OpenClaw，测防护和正常任务可用性
- **关键结果 / 消融** · 作者报告降低攻击成功并保持正常功能
- **适用条件 / 局限** · 守护策略需覆盖任务语境且仍会误判

**可复用机制** · 独立验收敏感动作权限门，并同时测误拒绝和正常任务完成。

<a id="paper-151160"></a>

## Defining Operational Conditions for Safety-Critical AI-Based Systems from Data

[官方论文页](https://neurips.cc/virtual/2026/poster/151160) · [作者来源](https://openreview.net/forum?id=caIKT2YrhB)

- **问题 / 瓶颈** · 依赖专家枚举可能漏掉复杂的条件组合
- **核心创新 / 方法** · 用多维核定义条件亲和度，以有界且顺序无关的算法构建运行域
- **Baseline** · 原隐藏运行域及替代样本的相似性对照
- **Benchmark** · 蒙特卡洛及航空防碰撞用例
- **关键结果 / 消融** · 报告可以从估计运行域生成与原域相近的数据
- **适用条件 / 局限** · 历史数据缺口不会自动消失

**可复用机制** · 用采样覆盖及分布相似性验收数据驱动运行域。

<a id="paper-154436"></a>

## DeFlowCritic: Dense Latent Reward Alignment for Text-to-Image Flow Matching Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154436) · [作者来源](https://openreview.net/forum?id=DYlByUybv0)

- **问题 / 瓶颈** · 末端稀疏奖励延迟信用分配
- **核心创新 / 方法** · 训练读取去噪器特征的内部 critic，联合评估构图和审美
- **Baseline** · 终图奖励及联合奖励方案
- **Benchmark** · GenEval2、T2I-CompBench
- **关键结果 / 消融** · 作者报告提示遵循和视觉质量较平衡，幅度待核
- **适用条件 / 局限** · 中间分数可能偏离最终图像质量

**可复用机制** · 固定生成预算对照潜空间密集奖励和终点奖励。

<a id="paper-155920"></a>

## DeFlow: Decoupling Behavior-Prior Modeling and Value Maximization for Offline Policy Extraction

[官方论文页](https://neurips.cc/virtual/2026/poster/155920) · [作者来源](https://openreview.net/forum?id=1oqxe0EmlH)

- **问题 / 瓶颈** · 直接优化迭代流需对求解器反传
- **核心创新 / 方法** · 保留多步流先验，以轻量残差和自适应信赖域改进价值
- **Baseline** · 生成式离线强化学习方法
- **Benchmark** · 多模态操作与离线到在线设置
- **关键结果 / 消融** · 作者报告总体有竞争力并在部分场景收益明显
- **适用条件 / 局限** · 信赖域不能保证严格的数据支持

**可复用机制** · 分别比较动作覆盖、价值改进和在线推理成本。

<a id="paper-153737"></a>

## Deformable 2D Gaussian Splatting

[官方论文页](https://neurips.cc/virtual/2026/poster/153737) · [作者来源](https://openreview.net/forum?id=J74MJSTvZk)

- **问题 / 瓶颈** · 对称高斯平滑高频细节
- **核心创新 / 方法** · 对切平面两轴做可学习单调重映射，各加一个控制点
- **Baseline** · 标准2DGS及替代核
- **Benchmark** · MipNeRF 360、Tanks&Temples，新视图与几何重建
- **关键结果 / 消融** · 报告改善锐边的表达
- **适用条件 / 局限** · 极复杂形状的收益待核

**可复用机制** · 先保留栅格化管线，再比较局部坐标变形和替换核。

<a id="paper-149334"></a>

## DeformGen: Dynamics-Based Topology Augmentation for Deformable Manipulation Policy Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149334) · [作者来源](https://openreview.net/forum?id=qrVOx2oqXj)

- **问题 / 瓶颈** · 刚体位姿增强无法产生可信形变
- **核心创新 / 方法** · 局部扰动经动力学模拟至稳定，再将粒子位移连续化以变换末端轨迹
- **Baseline** · 原始示范及刚体增强
- **Benchmark** · 高保真可形变操控基准
- **关键结果 / 消融** · 报告策略学习持续改善
- **适用条件 / 局限** · 依赖仿真和位移估计

**可复用机制** · 成对扩充状态及动作，检查二者的几何一致性。

<a id="paper-152675"></a>

## DeformMaster: An Interactive Physics-Neural World Model for Deformable Objects from Videos

[官方论文页](https://neurips.cc/virtual/2026/poster/152675) · [作者来源](https://openreview.net/forum?id=RFz2SWN1Gj)

- **问题 / 瓶颈** · 视频难以确定材料动力学及新交互结果
- **核心创新 / 方法** · 连续体滚动叠加神经残差，以分布式柔顺驱动表达手部运动，用局部本构专家表达材料
- **Baseline** · 已有先进方法，名称待核
- **Benchmark** · 真实形变视频上的新动作、动态视角和预测
- **关键结果 / 消融** · 报告滚动与渲染更好
- **适用条件 / 局限** · 材料与交互范围待核

**可复用机制** · 把误差校正留给残差，用结构化动力学维持可干预接口。

<a id="paper-149268"></a>

## DEFT: Disentanglement-Enhanced Fine-Tuning for EEG Foundation Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149268) · [作者来源](https://openreview.net/forum?id=raum5BFSpu)

- **问题 / 瓶颈** · 跨人脑电中的个体风格混入分类
- **核心创新 / 方法** · 微调适配器拆分任务与个体风格，通过对比和重建等目标约束
- **Baseline** · 同骨干匹配微调
- **Benchmark** · 多个脑电数据集和四种骨干
- **关键结果 / 消融** · 报告超越匹配对照，消融支持分支分工
- **适用条件 / 局限** · 跨设备收益待核

**可复用机制** · 固定骨干后测任务分支预测与个体身份泄漏。

<a id="paper-150704"></a>

## DegBins: Degradation-Driven Binning for Depth Super-Resolution

[官方论文页](https://neurips.cc/virtual/2026/poster/150704) · [作者来源](https://openreview.net/forum?id=g8MvEzqyXx)

- **问题 / 瓶颈** · 单一加性残差对空间变化退化不够灵活
- **核心创新 / 方法** · 预测每个残差区间概率并求加权和，结合局部退化分阶段细分
- **Baseline** · 传统残差回归，具名对照待核
- **Benchmark** · 深度超分辨率实验
- **关键结果 / 消融** · 报告改善重建
- **适用条件 / 局限** · 区间校准与计算成本待核

**可复用机制** · 对非均匀误差用条件区间代替点回归，并评价困难区域。

<a id="paper-153930"></a>

## DeGlare: Self-Supervised Specular Removal for Industrial Metallic Surfaces via Multi-Illumination Priors

[官方论文页](https://neurips.cc/virtual/2026/poster/153930) · [作者来源](https://openreview.net/forum?id=HZaT8wSiXs)

- **问题 / 瓶颈** · 工业金属高光难收集无高光标注
- **核心创新 / 方法** · 在固定视角多光照观测上交换潜表示，促使分解漫反射和镜面成分
- **Baseline** · 有监督高光去除及零样本基线
- **Benchmark** · 实物工业机器人采集数据
- **关键结果 / 消融** · 作者报告低数据条件下有效
- **适用条件 / 局限** · 新材料及光照范围待核

**可复用机制** · 当照明可控而真值昂贵时，以同视角跨照明一致性作监督。

<a id="paper-154303"></a>

## Déjà View: Looping Transformers for Multi-View 3D Reconstruction

[官方论文页](https://neurips.cc/virtual/2026/poster/154303) · [作者来源](https://openreview.net/forum?id=Eidz3t6qmk)

- **问题 / 瓶颈** · 深层三维重建模型重复做逐步细化
- **核心创新 / 方法** · 循环应用同一 Transformer 块，以迭代次数控制推理计算
- **Baseline** · 大型前馈模型及等训练预算不共享变体
- **Benchmark** · 五个室内外、物体和驾驶重建基准
- **关键结果 / 消融** · 报告更少参数下可比或更高精度，共享优于非共享变体
- **适用条件 / 局限** · 较长循环的稳定性待核

**可复用机制** · 比较等算力下的共享迭代与增加独立层。

<a id="paper-155078"></a>

## Delayed homomorphic reinforcement learning for environments with delayed feedback

[官方论文页](https://neurips.cc/virtual/2026/poster/155078) · [作者来源](https://openreview.net/forum?id=8eYgphdWiq)

- **问题 / 瓶颈** · 保留完整延迟历史导致状态爆炸
- **核心创新 / 方法** · 按信念等价抽象扩增状态，同时供策略和值函数使用
- **Baseline** · 状态扩增类方法
- **Benchmark** · 有限域理论及 MuJoCo 连续控制
- **关键结果 / 消融** · 确定性情形保最优并恢复无延迟样本量级，随机近似有价值损失界
- **适用条件 / 局限** · 依赖可构造信念等价关系

**可复用机制** · 延迟控制中先估计哪些不同历史在控制上等价。

<a id="paper-150466"></a>

## Delay-Embedded Representations for Robust Saccade Classification in Noisy Oculographic Signals

[官方论文页](https://neurips.cc/virtual/2026/poster/150466) · [作者来源](https://openreview.net/forum?id=hpVPOORw3w)

- **问题 / 瓶颈** · 阈值和深度检测器对强噪声或噪声迁移敏感
- **核心创新 / 方法** · 时延嵌入的滑窗双簇分解筛候选，以参数波形验证
- **Baseline** · U'n'Eye、REMoDNaV、I2MC 等九项
- **Benchmark** · 多噪声水平眼动事件检测，测 F1
- **关键结果 / 消融** · 报告中高噪声下持续提高 F1
- **适用条件 / 局限** · 依赖合理的事件波形假设

**可复用机制** · 把抗噪候选提取和事件参数估计拆开评测。

<a id="paper-155678"></a>

## Delightful Distributed Policy Gradient

[官方论文页](https://neurips.cc/virtual/2026/poster/155678) · [作者来源](https://openreview.net/forum?id=3mTHnPoUXG)

- **问题 / 瓶颈** · 低概率失败会主导批次，而低概率成功有探索价值
- **核心创新 / 方法** · 以优势乘惊讶度门控更新，无需行为策略概率
- **Baseline** · 精确行为概率的重要性加权策略梯度
- **Benchmark** · 模拟陈旧数据的 MNIST 及 Transformer 序列任务
- **关键结果 / 消融** · 报告多种干扰下误差或样本效率有数量级改善
- **适用条件 / 局限** · 依赖优势符号可靠

**可复用机制** · 同时报告稀有成功保留率与异常失败梯度贡献。

<a id="paper-153315"></a>

## Delta-Adapter: Scalable Exemplar-Based Image Editing with Single-Pair Supervision

[官方论文页](https://neurips.cc/virtual/2026/poster/153315) · [作者来源](https://openreview.net/forum?id=MDWlBA1fMo)

- **问题 / 瓶颈** · 难收集共享编辑意图的两个图像对
- **核心创新 / 方法** · 从冻结视觉编码器提取源目标语义差，以适配器注入编辑骨干，另约束输出变化一致性
- **Baseline** · 四种强编辑基线
- **Benchmark** · 见过的编辑任务中的编辑精度及内容一致性
- **关键结果 / 消融** · 报告两项指标均改善
- **适用条件 / 局限** · 变化表示能否分离背景与编辑待核

**可复用机制** · 以冻结特征差表示跨实例迁移的变换。

<a id="paper-151284"></a>

## DeltaMomentum: A Key-Value based Anisotropic Momentum Update via Delta Rule

[官方论文页](https://neurips.cc/virtual/2026/poster/151284) · [作者来源](https://openreview.net/forum?id=bXrZIgeNoe)

- **问题 / 瓶颈** · EMA 丢弃线性层梯度的外积结构
- **核心创新 / 方法** · 以输入为键、输出误差为值用 delta rule 更新一阶缓冲
- **Baseline** · 标准 EMA 动量及基准优化器
- **Benchmark** · 线性回归理论与优化实验
- **关键结果 / 消融** · 证明固定点对应正则化 Wiener 预测并改善跟踪收缩
- **适用条件 / 局限** · 理论条件及实际开销待核

**可复用机制** · 非平稳训练中按输入方向监测动量过时程度。

<a id="paper-153494"></a>

## DeltaPrompts: Escaping the Zero-Delta Trap in Multimodal Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/153494) · [作者来源](https://openreview.net/forum?id=KyGX4aOkhc)

- **问题 / 瓶颈** · 两者已给相同分布的样本几乎无学习信号
- **核心创新 / 方法** · 以答案散度定位能力差，对已有题种子定向合成
- **Baseline** · 常规题集与筛选方式
- **Benchmark** · 图表和文档推理，同模型对与跨模型迁移
- **关键结果 / 消融** · 标准数据最高约 69% 近零差异，作者报告高差异数据有益
- **适用条件 / 局限** · 散度不代表教师正确

**可复用机制** · 分离教师质量与师生差异，做等预算数据筛选。

<a id="paper-155940"></a>

## DELTA: Robustly Training Label-Conditional Diffusion Models with Weak Annotations

[官方论文页](https://neurips.cc/virtual/2026/poster/155940) · [作者来源](https://openreview.net/forum?id=1fJGfUpQRC)

- **问题 / 瓶颈** · 噪声、歧义或缺失标签会污染条件扩散
- **核心创新 / 方法** · 以变分目标联合推断真标签后验和干净分布，用中位数附近采样时间步
- **Baseline** · 各类专用弱监督扩散对照
- **Benchmark** · 三类弱标签下的类别一致性与样本质量
- **关键结果 / 消融** · 报告较对照更优且少用外部先验
- **适用条件 / 局限** · 极高噪声下的可识别性待核

**可复用机制** · 统一处理多种不可靠标签并分开测分类一致性和保真。

<a id="paper-151215"></a>

## DELTA-TTS: Adapting Autoregressive Model into a Diffusion Language Model for Text-to-Speech

[官方论文页](https://neurips.cc/virtual/2026/poster/151215) · [作者来源](https://openreview.net/forum?id=c4cM3P84zM)

- **问题 / 瓶颈** · 逐 token 解码延迟随长度增长
- **核心创新 / 方法** · LoRA 配块内短程对流连续性建模的卷积，适配双向去掩码
- **Baseline** · CosyVoice3 自回归底座
- **Benchmark** · 585 小时 LibriTTS 适配、Seed-TTS test-en
- **关键结果 / 消融** · 词错率 1.75%，token 生成快 3.3 倍
- **适用条件 / 局限** · 加速仅为 token 阶段

**可复用机制** · 比较整链端到端耗时及声学连续性。

<a id="paper-152418"></a>

## DELTAVID: Enhancing Fine-Grained Spatiotemporal Perception with Cross-Video Differences

[官方论文页](https://neurips.cc/virtual/2026/poster/152418) · [作者来源](https://openreview.net/forum?id=TGch9ifZ6l)

- **问题 / 瓶颈** · 全局语义相近时模型难定位局部变化
- **核心创新 / 方法** · 在真实视频构造局部可控变化，监督差异、时间边界和空间证据
- **Baseline** · 基础视频语言模型
- **Benchmark** · DeltaVid-Bench、Video-MME、MLVU 等
- **关键结果 / 消融** · 报告差异检测改善并迁移至通用评测
- **适用条件 / 局限** · 需验证合成改动是否有非语义捷径

**可复用机制** · 先控制全局语义再评估模型能否定位改变区域。

<a id="paper-149197"></a>

## Delve into the Applicability of Advanced Optimizers for Multi-Task Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149197) · [作者来源](https://openreview.net/forum?id=sBSgNPZhSj)

- **问题 / 瓶颈** · 瞬时修正经动量累积及高曲率传播会被稀释
- **核心创新 / 方法** · APT 自适应调节动量，另对 Muon 正交化约束方向保存
- **Baseline** · 既有多任务梯度法与 Adam、Muon
- **Benchmark** · 四种标准多任务基准
- **关键结果 / 消融** · 报告兼容性及效果改善
- **适用条件 / 局限** · 跨骨干与曲率条件待核

**可复用机制** · 分别测瞬时梯度冲突和实际更新冲突。

<a id="paper-153684"></a>

## Democratizing Tool Learning with Environments Fully Simulated by a Free 8B Language Model

[官方论文页](https://neurips.cc/virtual/2026/poster/153684) · [作者来源](https://openreview.net/forum?id=JZaFq20B2u)

- **问题 / 瓶颈** · 交互环境和动态难度构造成本高
- **核心创新 / 方法** · 用本地模型模拟任务、用户、工具及结果验证，并适配课程难度
- **Baseline** · 使用额外标注或外部模型的工具训练方案
- **Benchmark** · 工具调用任务，指标细节待核
- **关键结果 / 消融** · 作者报告多数设置超过额外资源对照
- **适用条件 / 局限** · 模拟到真实工具的差距待核

**可复用机制** · 固定环境预算比较静态和动态生成任务，并在独立真实任务验证。

<a id="paper-156660"></a>

## Demographic parity in regression and classification within the unawareness framework

[官方论文页](https://neurips.cc/virtual/2026/poster/156660) · [作者来源](https://neurips.cc/virtual/2026/poster/156660)

- **问题 / 瓶颈** · 不可直接使用敏感属性时，分类和回归的等价条件不明确
- **核心创新 / 方法** · 以最优传输重心刻画平方损失下的公平回归，证明分类决策集嵌套条件
- **Baseline** · 与允许差别对待的已有理论对照
- **Benchmark** · 人口统计均等与代价敏感分类理论设定
- **关键结果 / 消融** · 在嵌套时证明双向刻画
- **适用条件 / 局限** · 限所述公平准则和损失

**可复用机制** · 以嵌套性判断能否用同一连续评分和阈值构造多项分类决策。

<a id="paper-152530"></a>

## Demystifying Classifier-Free Guidance for Auto-Regressive Image Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/152530) · [作者来源](https://openreview.net/forum?id=SSyBnCPk9V)

- **问题 / 瓶颈** · 条件 logits 的重复偏向掩盖纹理。
- **核心创新 / 方法** · 分析条件与无条件输出，复用条件前向的中间注意力。
- **Baseline** · 条件贪婪解码与标准 CFG。
- **Benchmark** · 多个自回归图像模型，检查纹理和注意力计算量。
- **关键结果 / 消融** · 约减少 25% 注意力计算，质量变化小。
- **适用条件 / 局限** · 理论使用浅层 Transformer。

**可复用机制** · 按分支比较注意力可复用性与纹理损失。

<a id="paper-155629"></a>

## Demystifying Numerical Errors in LLM Inference: Achieving Reproducible Inference for Mission-Critical Tasks with HEAL

[官方论文页](https://neurips.cc/virtual/2026/poster/155629) · [作者来源](https://openreview.net/forum?id=49aQ53Ipde)

- **问题 / 瓶颈** · 贪婪解码仍可能因转换误差跨 GPU 发散。
- **核心创新 / 方法** · 用 INT16 存储 QKV 并在低精度张量核上补偿乘法误差。
- **Baseline** · 常规 16 位推理与全 FP32。
- **Benchmark** · MCR-Bench 的重复运行一致性与性能。
- **关键结果 / 消融** · 一致性接近 FP32，开销最高减少 6.7 倍。
- **适用条件 / 局限** · 迁移到新内核和硬件需重测。

**可复用机制** · 用跨硬件逐层对照定位首次舍入分歧。

<a id="paper-155576"></a>

## Denoise First, Orthogonalize Later: Understanding Momentum in Muon via Spectral Filtering

[官方论文页](https://neurips.cc/virtual/2026/poster/155576) · [作者来源](https://openreview.net/forum?id=4ZeLyC7o3w)

- **问题 / 瓶颈** · 正交化可能放大噪声导致的奇异空间偏移。
- **核心创新 / 方法** · 在信号加扰动模型中分析动量扩大谱隙的效果。
- **Baseline** · 先正交再动量以及无动量。
- **Benchmark** · 理论对齐与含语言模型训练的实验。
- **关键结果 / 消融** · 前置动量有更强的信号对齐保证。
- **适用条件 / 局限** · 依赖结构化梯度假设。

**可复用机制** · 比较动量顺序时同时测谱隙和更新方向。

<a id="paper-151878"></a>

## Denoising Distances in Metric Measure Spaces

[官方论文页](https://neurips.cc/virtual/2026/poster/151878) · [作者来源](https://openreview.net/forum?id=XDVLprycQY)

- **问题 / 瓶颈** · 流形条件之外的距离去噪复杂度不清楚。
- **核心创新 / 方法** · 在度量测度空间构造固定半径聚类与不同精度算法。
- **Baseline** · 对照流形设定及高成本算法。
- **Benchmark** · 理论比较精度和计算。
- **关键结果 / 消融** · 固定精度可高效实现，更高精度由非高效算法实现。
- **适用条件 / 局限** · 摘要仅提示计算统计缺口，未证明普遍下界。

**可复用机制** · 在一般度量空间分别报告精度门槛与计算代价。

<a id="paper-154041"></a>

## Denoising Implicit Variational Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/154041) · [作者来源](https://openreview.net/forum?id=GfgvZIgKUs)

- **问题 / 瓶颈** · 半隐式分布的边缘分数难算。
- **核心创新 / 方法** · 以去噪分数匹配训练网络，代入路径式 ELBO 梯度。
- **Baseline** · UIVI 及反向条件采样方法。
- **Benchmark** · 合成分布与真实数据贝叶斯任务。
- **关键结果 / 消融** · 作者报告梯度估计成本降低，驻点误差受分数误差控制。
- **适用条件 / 局限** · 依赖分析假设及分数拟合精度。

**可复用机制** · 显式测代理分数误差及其对下游优化的影响。

<a id="paper-151512"></a>

## Denoising-Time Heterogeneity in VLA Action Generation: A Controlled Study via Step-Wise Expert

[官方论文页](https://neurips.cc/virtual/2026/poster/151512) · [作者来源](https://openreview.net/forum?id=a64w6jVtnu)

- **问题 / 瓶颈** · 共享去噪器可能掩盖阶段差异。
- **核心创新 / 方法** · 混合两套速度场，保持容量和总混合量，改变专家时序。
- **Baseline** · 时间反转日程与同构专家控制。
- **Benchmark** · LIBERO、CALVIN 策略评测。
- **关键结果 / 消融** · 对齐日程在两基准均优于反转。
- **适用条件 / 局限** · 结果限于所测专家与任务。

**可复用机制** · 固定专家与预算，仅改变去噪阶段分配。

<a id="paper-154837"></a>

## Denoising Time Matters: Diverse Generation in Diffusion Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154837) · [作者来源](https://openreview.net/forum?id=AZvYD2Qmwj)

- **问题 / 瓶颈** · 全程扰动可能损害词汇细化。
- **核心创新 / 方法** · 在流形约束下扰动条件轨迹，再按时间缩小扰动。
- **Baseline** · 常规扩散解码，具名对照待核。
- **Benchmark** · 开放生成、指令任务及可验证推理。
- **关键结果 / 消融** · 多种骨干上多样性提高，推理能力基本保持。
- **适用条件 / 局限** · 采样参数和模型范围仍需核查。

**可复用机制** · 分别消融早期和后期扰动，分开测语义差异与质量。

<a id="paper-153427"></a>

## Dense Cross-Tokenizer Distillation via Semantic Optimal Local Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/153427) · [作者来源](https://openreview.net/forum?id=LQF7JsKagA)

- **问题 / 瓶颈** · 词表不共享坐标，字面映射或文本块压缩会丢信息。
- **核心创新 / 方法** · 按解码文本划块，用校准语料估计代价，在双向检索的局部支持上做熵正则传输。
- **Baseline** · 同训练和解码设置下的跨词表蒸馏方法。
- **Benchmark** · Dolly、UltraChat 和代码数学迁移。
- **关键结果 / 消融** · 作者报告优于直接对照，支持覆盖与得分相关。
- **适用条件 / 局限** · 依赖校准语料和检索覆盖。

**可复用机制** · 跨词表蒸馏时把支持召回率与训练结果一起测。

<a id="paper-153814"></a>

## Dense Flow from Adaptive Correspondence

[官方论文页](https://neurips.cc/virtual/2026/poster/153814) · [作者来源](https://openreview.net/forum?id=IWagPCbpdp)

- **问题 / 瓶颈** · 固定像素网格难平衡内部区域与边界细节。
- **核心创新 / 方法** · 学习像素到 token 的软分配，在 token 空间匹配后投回像素。
- **Baseline** · 固定网格光流模型。
- **Benchmark** · KITTI 与 Sintel 的零样本跨数据集测试。
- **关键结果 / 消融** · 作者报告 KITTI EPE 最优、KITTI Fl 和 Sintel Final EPE 第二。
- **适用条件 / 局限** · 遮挡和细小结构仍可能导致分组错误。

**可复用机制** · 评测自适应匹配时分别报告边界与区域内误差。

<a id="paper-149337"></a>

## Dense Structural Compression of Transformers via Gauge-Correct Channel Removal

[官方论文页](https://neurips.cc/virtual/2026/poster/149337) · [作者来源](https://openreview.net/forum?id=qq8R6cSNpW)

- **问题 / 瓶颈** · 可互相缩放的因子使单边范数不可靠。
- **核心创新 / 方法** · 用对称组稀疏惩罚平衡因子，并物理移除全零通道。
- **Baseline** · 手工架构与采用同效用指标的后剪枝。
- **Benchmark** · 多项式长除、字符语言模型和掩码自编码。
- **关键结果 / 消融** · 长除任务在正确率不变时实现 190 倍压缩。
- **适用条件 / 局限** · 最高压缩率来自受控任务。

**可复用机制** · 对可重参数化结构比较训练中压缩与事后剪枝。

<a id="paper-154375"></a>

## Density-Ratio Losses for Post-Hoc Learning to Defer

[官方论文页](https://neurips.cc/virtual/2026/poster/154375) · [作者来源](https://openreview.net/forum?id=E25jB11LFP)

- **问题 / 瓶颈** · 固定委派规则难适应不同人工预算。
- **核心创新 / 方法** · 以散度正则重加权定义两种理想分布，转成类别概率估计。
- **Baseline** · 常用后处理基线及 Chow 规则。
- **Benchmark** · 多数据设置的后处理委派，指标细节待核。
- **关键结果 / 消融** · 作者报告表现可比且跨数据更稳健。
- **适用条件 / 局限** · 依赖专家表现和密度比估计。

**可复用机制** · 固定两个预测者，仅扫描委派评分阈值比较预算前沿。

<a id="paper-151486"></a>

## Dependency-Guided Parallel Decoding in Discrete Diffusion Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151486) · [作者来源](https://openreview.net/forum?id=aGLo39lNPa)

- **问题 / 瓶颈** · 逐 token 边缘相乘会忽略强依赖。
- **核心创新 / 方法** · 用末层状态估计成对影响，并贪心约束累计依赖。
- **Baseline** · 置信度及 KL 选择，另接入 dParallel。
- **Benchmark** · Dream-7B 以及数学和代码任务。
- **关键结果 / 消融** · 作者报告 1.7–2.2 倍加速，准确率可比或改善。
- **适用条件 / 局限** · 误差界依赖次可加假设。

**可复用机制** · 并行生成时显式控制候选间依赖，而非只按置信度排序。

<a id="paper-140012"></a>

## Deployment-Memory LLM Test-Time Training Should Require Behavioral Evidence Beyond Perplexity

[官方论文页](https://neurips.cc/virtual/2026/poster/140012) · [作者来源](https://openreview.net/forum?id=ra80Jaw38j)

- **问题 / 瓶颈** · 困惑度改善可能与真实回忆无关。
- **核心创新 / 方法** · 构造代理损失改善而行为回忆失败的诊断反例。
- **Baseline** · 局部困惑度或未来 token 损失等代理。
- **Benchmark** · 论文审计及反例，评价回忆、保持和下游使用。
- **关键结果 / 消融** · 反例显示代理损失改善不足以支持记忆结论。
- **适用条件 / 局限** · 证据主要是诊断反例与观点分析。

**可复用机制** · 把代理优化和脱离原始上下文后的记忆使用分开测。

<a id="paper-154654"></a>

## Deployment-Time Online Imitation Learning from Corrective Demonstrations

[官方论文页](https://neurips.cc/virtual/2026/poster/154654) · [作者来源](https://openreview.net/forum?id=C1sXJuHXuz)

- **问题 / 瓶颈** · 反复全量重训代价随数据增大。
- **核心创新 / 方法** · 用随机投影和在线岭回归更新部署策略。
- **Baseline** · 行为克隆及依赖累积数据重训的交互路线。
- **Benchmark** · 机器人操作任务上的持续部署更新。
- **关键结果 / 消融** · 作者报告稳定改善并优于所比行为克隆。
- **适用条件 / 局限** · 需要实时专家纠正，适应幅度待核。

**可复用机制** · 固定纠正预算比较在线充分统计与重训的遗忘和耗时。

<a id="paper-139479"></a>

## Depth2Pose: A Pose-Based Benchmark for Monocular Depth Estimation without Ground-Truth Depth

[官方论文页](https://neurips.cc/virtual/2026/poster/139479) · [作者来源](https://openreview.net/forum?id=NVZSWCjNVK)

- **问题 / 瓶颈** · 全局深度误差未必反映几何求解质量。
- **核心创新 / 方法** · 以预测深度和特征对应求解相对位姿，无需稠密真值。
- **Baseline** · 传统逐像素深度指标。
- **Benchmark** · D2P 挑战场景和常用深度基准。
- **关键结果 / 消融** · 常用数据上两类指标趋于一致，但优秀方法未必泛化到 D2P。
- **适用条件 / 局限** · 受参考位姿与特征匹配质量影响。

**可复用机制** · 深度用于定位前用同一几何求解器验证下游误差。

<a id="paper-152407"></a>

## Depth Exploration for LLM Decoding

[官方论文页](https://neurips.cc/virtual/2026/poster/152407) · [作者来源](https://openreview.net/forum?id=TKWIMojtwx)

- **问题 / 瓶颈** · 单一早退层选择存在计算浪费和回退损失。
- **核心创新 / 方法** · 扩展深度候选，提交全深度参考 token，再收缩至可复用分支。
- **Baseline** · 单深度选择、投机和分布式解码。
- **Benchmark** · 早退训练模型及标准语言模型的吞吐测试。
- **关键结果 / 消融** · 作者报告优于深度选择对照且保持输出等价。
- **适用条件 / 局限** · 分支成本和收益取决于运行时。

**可复用机制** · 扫描候选深度间隔并测每次提交的计算与回退开销。

<a id="paper-152636"></a>

## DepthGraft: Structural Regularization through Hierarchical Cross-Layer KV Reconstruction

[官方论文页](https://neurips.cc/virtual/2026/poster/152636) · [作者来源](https://openreview.net/forum?id=RaqeCKA8Ch)

- **问题 / 瓶颈** · 深层信息稀释，邻层共享或全局锚点难均匀传梯度。
- **核心创新 / 方法** · 按跨步对应选择浅层和中层分层重建 KV。
- **Baseline** · 相邻共享及全局锚点共享。
- **Benchmark** · 0.5B 到 65B 的稠密和 MoE，含 MMLU-Pro。
- **关键结果 / 消融** · 缓存约减少三分之一，16B MoE 在 MMLU-Pro 增 7 个百分点。
- **适用条件 / 局限** · 具体预算与拓扑敏感性待核。

**可复用机制** · 在同缓存预算下对照不同共享边，并测表示几何。

<a id="paper-149698"></a>

## DepthMaster: Unified Monocular Depth Estimation for Perspective and Panoramic Images

[官方论文页](https://neurips.cc/virtual/2026/poster/149698) · [作者来源](https://openreview.net/forum?id=o6YcOXGpEx)

- **问题 / 瓶颈** · 全景畸变与米制标签稀缺阻碍共用骨干。
- **核心创新 / 方法** · 用虚拟相机分解全景并对齐重叠区域预测。
- **Baseline** · 全景专用与通用深度方案。
- **Benchmark** · 13 个零样本深度数据集。
- **关键结果 / 消融** · 作者报告优于所比较通用及专用方法。
- **适用条件 / 局限** · 依赖足够重叠与投影几何准确性。

**可复用机制** · 优先在重叠对应处施加约束，再测拼接误差。

<a id="paper-150663"></a>

## Depth-Recurrent Attention Mixtures: Giving Latent Reasoning the Attention it Deserves

[官方论文页](https://neurips.cc/virtual/2026/poster/150663) · [作者来源](https://openreview.net/forum?id=gO5QiZbYME)

- **问题 / 瓶颈** · 深度递归的固定隐维成为容量瓶颈。
- **核心创新 / 方法** · 在共享循环层混合三类注意力以解耦缩放维度。
- **Baseline** · 匹配 FLOPs、参数和显存的 Transformer。
- **Benchmark** · 最高约 2B 参数的语言推理实验。
- **关键结果 / 消融** · 同准确率平均约需三分之一训练 token。
- **适用条件 / 局限** · 更大尺度的训练稳定性待核。

**可复用机制** · 比较递归和固定深度时三种资源同时匹配。

<a id="paper-149074"></a>

## Depth through Recurrence: Towards Ultra-Efficient On-Device ASR

[官方论文页](https://neurips.cc/virtual/2026/poster/149074) · [作者来源](https://openreview.net/forum?id=t4zfR92Bzz)

- **问题 / 瓶颈** · 边缘 ASR 受参数和计算预算限制。
- **核心创新 / 方法** · 按表征对层分组并蒸馏至共享循环块。
- **Baseline** · 较大的语音识别参考模型。
- **Benchmark** · Open ASR Leaderboard。
- **关键结果 / 消融** · 两块模型平均恢复参考准确率的 97.4%。
- **适用条件 / 局限** · 循环节省参数未必同比减少延迟。

**可复用机制** · 用层相似性指导共享，并分别测大小、延迟与准确率。

<a id="paper-152655"></a>

## Derivative-Informed Training of Neural Operators On-the-Fly via Sketched Tangent Consistency

[官方论文页](https://neurips.cc/virtual/2026/poster/152655) · [作者来源](https://openreview.net/forum?id=RO1LZT9pc2)

- **问题 / 瓶颈** · 离线切线求解和存储昂贵
- **核心创新 / 方法** · 抽样输入方向，用自动微分求方向导数并约束切线方程，按算子条件预处理
- **Baseline** · 离线 DIFNO
- **Benchmark** · 四类 PDE 含 Burgers 和二维 Navier–Stokes
- **关键结果 / 消融** · 正确预处理时精度可比，省去离线导数生成
- **适用条件 / 局限** · 刚性或不定算子上直接施加残差可能失败

**可复用机制** · 固定训练预算对比原始和预条件切线残差

<a id="paper-152570"></a>

## Derived Fields Preserve Fine-Scale Detail in Budgeted Neural Simulators

[官方论文页](https://neurips.cc/virtual/2026/poster/152570) · [作者来源](https://openreview.net/forum?id=S8JSn3ujCO)

- **问题 / 瓶颈** · 细节在量化重建前已可能丢失
- **核心创新 / 方法** · 按校准的压缩通道联合选择原始和派生场及预算
- **Baseline** · 多种同预算基线，具名待核
- **Benchmark** · PDEBench 时变正问题，滚动 nRMSE 与细尺度保真
- **关键结果 / 消融** · 细尺度和平均误差均改善，输入端已有增益
- **适用条件 / 局限** · 依赖压缩通道校准

**可复用机制** · 把输入保真和滚动误差分开测

<a id="paper-154887"></a>

## Deriving Hyperparameter Scaling Laws via Modern Optimization Theory

[官方论文页](https://neurips.cc/virtual/2026/poster/154887) · [作者来源](https://openreview.net/forum?id=A9u0AReK7q)

- **问题 / 瓶颈** · 跨训练长度的缩放常依赖经验
- **核心创新 / 方法** · 最小化 LMO 优化器收敛上界以求幂律
- **Baseline** · 经验缩放与已有理论观察
- **Benchmark** · 固定模型大小，比较迭代或 token 预算
- **关键结果 / 消融** · 恢复多类经验规律并指出动量与批量耦合
- **适用条件 / 局限** · 收敛界只是代理且不覆盖模型大小变化

**可复用机制** · 为同一预算比较多种动量和批量组合

<a id="paper-153178"></a>

## Designing Effective Monitor-Based Interventions for Mitigating Reward Hacking During RL

[官方论文页](https://neurips.cc/virtual/2026/poster/153178) · [作者来源](https://openreview.net/forum?id=NERzW49Ahm)

- **问题 / 瓶颈** · 离线监控准确率未必预测闭环训练安全
- **核心创新 / 方法** · 比较监控配置和任务难度组成，并转移防御结论
- **Baseline** · 朴素监控器
- **Benchmark** · 代码、医疗对话和传记任务的奖励偏差率
- **关键结果 / 消融** · 两个迁移环境中报告从 70–100% 降至 0%
- **适用条件 / 局限** · 限定所测模型与环境

**可复用机制** · 用独立回归测试验收监控方案

<a id="paper-154581"></a>

## Designing Kernel Surrogate Models for Multimodal Attribution

[官方论文页](https://neurips.cc/virtual/2026/poster/154581) · [作者来源](https://openreview.net/forum?id=CWGFOa2GfB)

- **问题 / 瓶颈** · 加性归因漏掉跨样本模态协同
- **核心创新 / 方法** · 结构核分开建模样本是否入选和模态组成，并拟合终点损失
- **Baseline** · 加性或线性数据归因，具名待核
- **Benchmark** · 代理拟合、数据选择及交通事故预测
- **关键结果 / 消融** · 摘要报告归因分数提高 60.3%，数据选择平均准确率提高 2.24%
- **适用条件 / 局限** · 代理依赖训练重采样及核选择

**可复用机制** · 比较同预算加性和非加性归因的选择表现

<a id="paper-155438"></a>

## Designing Reinforcement Learning for Diffusion Models: A Unified Path-Space View

[官方论文页](https://neurips.cc/virtual/2026/poster/155438) · [作者来源](https://openreview.net/forum?id=5e4jcilj33)

- **问题 / 瓶颈** · 扩散强化学习方法表面形式分散
- **核心创新 / 方法** · 从路径空间目标推出等价降方差价值梯度，并以组内样本核估计梯度
- **Baseline** · Flow-GRPO、AWM、DiffusionNFT
- **Benchmark** · SD3.5-M 与 Qwen-Image 对齐训练
- **关键结果 / 消融** · 作者报告可匹配或超过已有方法
- **适用条件 / 局限** · 有限样本估值和权重边界影响稳定性

**可复用机制** · 固定奖励和轨迹预算再比较估计器

<a id="paper-155220"></a>

## Despa: Resolving Spatial Collapse in VLMs via Depth-Grounded Geometry

[官方论文页](https://neurips.cc/virtual/2026/poster/155220) · [作者来源](https://openreview.net/forum?id=7OtFTKPxC5)

- **问题 / 瓶颈** · 二维语义相似不足以推断度量空间
- **核心创新 / 方法** · 注入几何位置及深度旋转编码
- **Baseline** · Qwen3-VL-235B-A22B、GPT-5.2 及多个开源骨干
- **Benchmark** · SpaBench、MSMU、RefSpatial-U、VSI-Bench
- **关键结果 / 消融** · 摘要报告 SpaBench 比两具名模型高 27.9% 与 31.1%
- **适用条件 / 局限** · 受深度质量与任务分布影响

**可复用机制** · 固定骨干分别消融两种深度编码

<a id="paper-151134"></a>

## DetailAnywhere: Fashion Detail Generation via Cross-Modal Feature Alignment Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/151134) · [作者来源](https://openreview.net/forum?id=ckGG0WagkI)

- **问题 / 瓶颈** · 位置标记与近景外观语义不直接对齐
- **核心创新 / 方法** · DINOv3 教师对齐两个扩散分支，配对奖励约束一致性
- **Baseline** · 开放源代码图像生成方法
- **Benchmark** · FDBench，四万余对人工核验样本及人评
- **关键结果 / 消融** · 作者报告一致性和生成质量改善
- **适用条件 / 局限** · 证据限服装品类，独立增益待核

**可复用机制** · 分别衡量区域对应、身份一致及生成质量

<a id="paper-150451"></a>

## Detect Anything in Graphic Design: Element-Level Rewards for Autoregressive Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/150451) · [作者来源](https://openreview.net/forum?id=hwvqsWfZFI)

- **问题 / 瓶颈** · 无序检测忽略遮挡的图层关系
- **核心创新 / 方法** · 按合成顺序预测完整框，用元素级相对策略优化
- **Baseline** · GRPO 及检测基线
- **Benchmark** · 九个检测基准和图形设计遮挡检测
- **关键结果 / 消融** · 作者报告元素级优化持续优于 GRPO
- **适用条件 / 局限** · 依赖可定义构图顺序

**可复用机制** · 对结构化输出在同奖励定义下比较元素与序列粒度

<a id="paper-139119"></a>

## Detect, Explain, Interpret: An End-to-End Benchmark for Time Series Anomaly Detection, Explainability and Interpretability.

[官方论文页](https://neurips.cc/virtual/2026/poster/139119) · [作者来源](https://openreview.net/forum?id=jxfd3833me)

- **问题 / 瓶颈** · 检测准确率不足以说明定位和理解异常的能力
- **核心创新 / 方法** · 结合异常标注、各维度分数和冻结模型解释建立评测
- **Baseline** · 现有异常检测器与冻结语言模型
- **Benchmark** · SHAD 的 144 条多变量存储遥测序列
- **关键结果 / 消融** · 提供三阶段对照，具体结果待核
- **适用条件 / 局限** · 单来源存储系统的外推待验证

**可复用机制** · 分别验收发现、定位和解释

<a id="paper-155937"></a>

## Detecting Hidden ML Training With Zero-Overhead Telemetry

[官方论文页](https://neurips.cc/virtual/2026/poster/155937) · [作者来源](https://openreview.net/forum?id=1fv2pVeapQ)

- **问题 / 瓶颈** · 平均准确率会掩盖没见过的任务分布失效
- **核心创新 / 方法** · 用不读取数据或权重的遥测做分类并按负载难度分层评估
- **Baseline** · 不同迭代轮次与负载组
- **Benchmark** · 九种 GPU、四代硬件
- **关键结果 / 消融** · 总体 98.6%，最难未知组 43–87%
- **适用条件 / 局限** · 不能据总体表现保证跨设备部署

**可复用机制** · 独立保留陌生负载做监测上线验收

<a id="paper-155181"></a>

## Detecting RLVR Training Data via Structural Convergence of Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/155181) · [作者来源](https://openreview.net/forum?id=7iHajwYLxA)

- **问题 / 瓶颈** · 似然指标未必反映可验证奖励训练的污染
- **核心创新 / 方法** · 以生成之间的结构差异作审计信号
- **Baseline** · 似然和已有污染检测基线
- **Benchmark** · 多个可验证奖励训练模型，区分已知入训与留出题
- **关键结果 / 消融** · 摘要报告结构差异优于对照，数值待核
- **适用条件 / 局限** · 需要排除题目难度、解码及少解问题影响

**可复用机制** · 用已知来源的基准题做受控污染审计

<a id="paper-150861"></a>

## Detection and Classification in Latent Spaces: High-Dimensional Analysis and Validation

[官方论文页](https://neurips.cc/virtual/2026/poster/150861) · [作者来源](https://openreview.net/forum?id=eoEglhtYkx)

- **问题 / 瓶颈** · 潜空间检测随维度不总单调改善
- **核心创新 / 方法** · 推导线性和二次统计量的大偏差表现并扩展到多类
- **Baseline** · 线性与二次判别规则
- **Benchmark** · 视觉、文本和音频基础表征
- **关键结果 / 消融** · 误差随维样比可出现多重下降；报告理论和实测相符
- **适用条件 / 局限** · 依赖高维比例极限与模型假设

**可复用机制** · 在固定误报预算下扫描表示维度

<a id="paper-151934"></a>

## DetectViT: Test-time Backdoor Detection for Vision Transformers via Inter-Head Attention Discrepancy

[官方论文页](https://neurips.cc/virtual/2026/poster/151934) · [作者来源](https://openreview.net/forum?id=WjAq71jgrz)

- **问题 / 瓶颈** · 输出标签或嵌入的检测不易跨任务使用
- **核心创新 / 方法** · 用头间一致与注意力熵波动作监测量，以少量外部分布样本校准
- **Baseline** · 已有运行时检测器
- **Benchmark** · DeiT、CLIP 和 LLaVA，分类与描述
- **关键结果 / 消融** · 作者报告小校准集有效；单设定误报 0.17%
- **适用条件 / 局限** · 不可将单设定率外推到新检查点

**可复用机制** · 用独立正常样本验收误报和监测延迟

<a id="paper-153726"></a>

## Detect What You Need: Chain-of-Causal Reasoning for 3D Intent Grounding

[官方论文页](https://neurips.cc/virtual/2026/poster/153726) · [作者来源](https://openreview.net/forum?id=JF39l5WGlk)

- **问题 / 瓶颈** · 意图通常缺少可直接匹配的外观词
- **核心创新 / 方法** · 以需求属性图对齐功能表征和点云几何语义
- **Baseline** · 隐式意图匹配方法
- **Benchmark** · 三维意图和视觉定位
- **关键结果 / 消融** · 作者报告改善，数值待核
- **适用条件 / 局限** · 功能图覆盖和点云质量影响判断

**可复用机制** · 分别检查功能需求推断和候选匹配

<a id="paper-148978"></a>

## DETS: An Interval-Censored Evidential Sampling Framework for Cross-Domain Scientific Discovery

[官方论文页](https://neurips.cc/virtual/2026/poster/148978) · [作者来源](https://openreview.net/forum?id=tjw3hiE7Tt)

- **问题 / 瓶颈** · 点监督容易拟合测量噪声
- **核心创新 / 方法** · 最大化容差区间内的概率质量，并区分两类不确定性作数据选择依据
- **Baseline** · 点回归及跨域基线
- **Benchmark** · 仅提取热力学和带隙预测的证据
- **关键结果 / 消融** · 作者报告高噪低数据时更稳健，组件贡献待核
- **适用条件 / 局限** · 容差需经测量标定

**可复用机制** · 在已知仪器误差下对照区间与点监督

<a id="paper-148931"></a>

## Developmental Visual Experience Scaffolds Grounded Concept Acquisition in Vision-Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148931) · [作者来源](https://openreview.net/forum?id=uA7IWRdKRA)

- **问题 / 瓶颈** · 图文对齐分数可能掩盖概念层级差异
- **核心创新 / 方法** · 对比渐进清晰与全程清晰的视觉语言对比训练
- **Baseline** · 全程清晰输入
- **Benchmark** · 标题对齐、基本及上位类别、行为相似性
- **关键结果 / 消融** · 标题水平相当，阶段课程的层级对齐更强
- **适用条件 / 局限** · 训练预算和模糊轨迹的边界待核

**可复用机制** · 在同数据预算比较课程并测层级概念而非只测标题

<a id="paper-153302"></a>

## DexMirror: Real-to-Sim Scene Mirroring for Sim-to-Real Dexterous Manipulation

[官方论文页](https://neurips.cc/virtual/2026/poster/153302) · [作者来源](https://openreview.net/forum?id=MH1pV5BGQ8)

- **问题 / 瓶颈** · 漂亮渲染仍可能几何错位
- **核心创新 / 方法** · 组合高斯重建和以手为中心的校准，将特权策略蒸馏给视觉策略
- **Baseline** · 具名仿真到真机对照待核
- **Benchmark** · 六项灵巧操作及重建 F1
- **关键结果 / 消融** · 作者报告重建 F1 为 0.981 并完成真机验证
- **适用条件 / 局限** · 依赖可重建场景及机器人校准

**可复用机制** · 单独控制校准误差再比较渲染质量与迁移收益

<a id="paper-151955"></a>

## DexOPE: 6D Object Pose Estimation in Dexterous Manipulation

[官方论文页](https://neurips.cc/virtual/2026/poster/151955) · [作者来源](https://openreview.net/forum?id=WYYNxzcyv2)

- **问题 / 瓶颈** · 确定性回归易在重遮挡下给出平均无效解
- **核心创新 / 方法** · 采样位姿后验时以非穿透和触觉接触引导
- **Baseline** · 已有六维位姿方法，具名待核
- **Benchmark** · DexOPE 含约 1500 个物品及模拟和实景
- **关键结果 / 消融** · 作者报告遮挡鲁棒性及未见物体泛化改善
- **适用条件 / 局限** · 依赖可靠接触和物体几何

**可复用机制** · 按遮挡强度比较点估计与物理约束后验

<a id="paper-154902"></a>

## Dexterous Skill Discovery via Topology-Aware Wasserstein Dependency

[官方论文页](https://neurips.cc/virtual/2026/poster/154902) · [作者来源](https://openreview.net/forum?id=A5ERuovz5k)

- **问题 / 瓶颈** · 显式奖励难覆盖灵巧操作
- **核心创新 / 方法** · 在 se(3) 李代数中构造技能与物体运动的 Wasserstein 依赖
- **Baseline** · 现有度量感知技能发现
- **Benchmark** · 多指操控及跨本体任务
- **关键结果 / 消融** · 作者报告无需人工监督即可发现多轴平移及转动
- **适用条件 / 局限** · 依赖物体位姿估计

**可复用机制** · 以物体运动为技能信号，对照欧氏距离和位姿拓扑度量

<a id="paper-153375"></a>

## D-GAP: Improving Out-of-Domain Robustness via Dataset-Agnostic and Gradient-Guided Augmentation in Amplitude and Pixel Spaces

[官方论文页](https://neurips.cc/virtual/2026/poster/153375) · [作者来源](https://openreview.net/forum?id=Lqa5ffpkXU)

- **问题 / 瓶颈** · 通用增强可能漏掉域特有频率偏差
- **核心创新 / 方法** · 用任务梯度生成频域敏感度，引导幅度与像素空间增强
- **Baseline** · 手工或单频域增强
- **Benchmark** · 无监督域适应视觉任务
- **关键结果 / 消融** · 作者报告跨域鲁棒性改善，幅度待核
- **适用条件 / 局限** · 梯度依赖当前模型与训练信号

**可复用机制** · 固定增强预算比较梯度引导与均匀扰动

<a id="paper-155974"></a>

## DGRAF: Observation-Quality-Aware Reinforcement Learning for Dynamic Reconfigurable Batteries

[官方论文页](https://neurips.cc/virtual/2026/poster/155974) · [作者来源](https://openreview.net/forum?id=1QZxzf78Bp)

- **问题 / 瓶颈** · 固定风险边界无法兼顾传感丢失和效率
- **核心创新 / 方法** · 联合扩散补全并量化质量，将质量接入分布式风险决策
- **Baseline** · 全观测或固定保守策略
- **Benchmark** · 动态可重构电池传感故障设置
- **关键结果 / 消融** · 作者报告改善安全与性能折衷，细节待核
- **适用条件 / 局限** · 质量失准时风险调节可能失效

**可复用机制** · 在缺失观测控制中按补全可信度选风险预算

<a id="paper-148763"></a>

## DiA: Directional Adapter

[官方论文页](https://neurips.cc/virtual/2026/poster/148763) · [作者来源](https://openreview.net/forum?id=vF2lXB0cGj)

- **问题 / 瓶颈** · 双向平均容易丢失动作阶段差异
- **核心创新 / 方法** · 冻结 CLIP 上用紧凑瓶颈深度卷积实现正向与反向时序分支，再学习融合
- **Baseline** · CLIP 与视频适配方法
- **Benchmark** · 细粒度视频动作识别
- **关键结果 / 消融** · 作者报告精度和算力折衷改善
- **适用条件 / 局限** · 反向分支需访问未来帧

**可复用机制** · 固定参数量比较对称聚合和方向分解

<a id="paper-151898"></a>

## DiagEval: Trajectory-Conditioned Diagnosis for Reliable Software Evaluation with GUI Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/151898) · [作者来源](https://openreview.net/forum?id=X7W0twHPBw)

- **问题 / 瓶颈** · 一次 GUI 执行不能覆盖所有有效路径
- **核心创新 / 方法** · 利用失败轨迹选择针对性功能核对，汇集结果辅助归因
- **Baseline** · 原始单轨迹评估与重新执行
- **Benchmark** · WebDevJudge-Unit 和 RealDevBench，多种 GUI 评测器与骨干
- **关键结果 / 消融** · 作者报告改善假阴性案例的诊断
- **适用条件 / 局限** · 不重建完整状态图，输出也不是校准概率

**可复用机制** · 在授权功能测试中保留失败轨迹并优先检查有区分力的状态

<a id="paper-154008"></a>

## DIAGNO: Diagonal Spherical Neural Operators for Heterogeneous Earth Dynamics Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/154008) · [作者来源](https://openreview.net/forum?id=GtXyIhzAqI)

- **问题 / 瓶颈** · 严格旋转等变会隔离频谱演化
- **核心创新 / 方法** · 从球面谱分解显式参数化跨模态相互作用核
- **Baseline** · 旋转等变球面算子与平面算子
- **Benchmark** · 地球动力学预测
- **关键结果 / 消融** · 作者报告建模改善，精度和开销待核
- **适用条件 / 局限** · 更宽松的对称假设需验证数据及计算成本

**可复用机制** · 检查物理对称性是否过强，再对照谱模态独立与混合

<a id="paper-154288"></a>

## Diagnosing and Correcting Bias in MLLM for Long Video Understanding

[官方论文页](https://neurips.cc/virtual/2026/poster/154288) · [作者来源](https://openreview.net/forum?id=EtgXlsMo0V)

- **问题 / 瓶颈** · 错误可能来自语言或显著但无关的视频线索
- **核心创新 / 方法** · S-MME 诊断捷径，CLEAR 用反事实视图估计偏差并干预隐藏状态
- **Baseline** · 原多模态模型等，具名对照待核
- **Benchmark** · S-MME 长视频问答
- **关键结果 / 消融** · 作者报告缓解捷径，幅度待核
- **适用条件 / 局限** · 反事实视图也可能包含真实证据

**可复用机制** · 在固定帧预算下测移除证据与保留干扰时的答案稳定性

<a id="paper-153711"></a>

## Diagnosing and Mitigating Modality Interference in Multimodal Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153711) · [作者来源](https://openreview.net/forum?id=JLVUKlvQ8q)

- **问题 / 瓶颈** · 模态无关信号可能压过应当优先的证据
- **核心创新 / 方法** · 在偏视觉与偏文本任务中，控制性修改无关模态并比较输出
- **Baseline** · 无扰动与多类模型
- **Benchmark** · 跨模型家族和规模的图像及文本主导任务
- **关键结果 / 消融** · 多种尺度均观察到退化
- **适用条件 / 局限** · 需确认被扰模态确实对任务无关

**可复用机制** · 把跨模态整合能力与抗无关输入干扰能力分开测

<a id="paper-149438"></a>

## Diagnosing and Repairing Visual Collapse in Compact Medical Multimodal LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/149438) · [作者来源](https://openreview.net/forum?id=q5FAFDMeZq)

- **问题 / 瓶颈** · 视觉问答得分能掩盖文本捷径
- **核心创新 / 方法** · 测视觉空间多样性、更新幅度与注意力，给三种失效各设轻量训练损失
- **Baseline** · 原始模型与不同残差干预
- **Benchmark** · 五种紧凑医疗多模态骨干和六个医疗问答基准
- **关键结果 / 消融** · 视觉残差更新约小一个数量级，移除视觉残差影响很小
- **适用条件 / 局限** · 诊断不等同于临床可用性

**可复用机制** · 在不改推理的前提下，将视觉依赖作为辅助训练和评估目标

<a id="paper-139853"></a>

## DiagnosticIQ: A Benchmark for LLM-Based Industrial Maintenance Action Recommendation from Symbolic Rules

[官方论文页](https://neurips.cc/virtual/2026/poster/139853) · [作者来源](https://openreview.net/forum?id=0S9Uw8cJOR)

- **问题 / 瓶颈** · 判断正确可能只靠题面线索
- **核心创新 / 方法** · 把规则改写成析取范式，配合相似干扰项及五类变体
- **Baseline** · 29 种语言模型、四种嵌入对照及九位从业者
- **Benchmark** · DiagnosticIQ，16 种资产与 6690 道专家核验题
- **关键结果 / 消融** · 从业者均值 45%，模型结果分项待核
- **适用条件 / 局限** · 选择题与现场安全决策有差距

**可复用机制** · 验收规则推理时用保持语义的改写和针对性干扰项

<a id="paper-152327"></a>

## Diagonalizing the Softmax: Hadamard Initialization for Tractable Cross-Entropy Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/152327) · [作者来源](https://openreview.net/forum?id=TtyvY0C2eo)

- **问题 / 瓶颈** · 平方损失理论无法解释全部交叉熵动态
- **核心创新 / 方法** · 对正交输入的两层线性网络，以 Hadamard 初始化对角化 softmax 并构造 Lyapunov 函数
- **Baseline** · 平方损失谱初始化框架
- **Benchmark** · 多类交叉熵理论设定，度量有限时间收敛和神经坍缩
- **关键结果 / 消融** · 证明收敛并发现非单调动态与类别数效应
- **适用条件 / 局限** · 依赖正交输入及特定初始化

**可复用机制** · 在简化设定比较不同损失的真实训练动态，不直接套用平方损失推导

<a id="paper-155455"></a>

## DiagSQL: A Diagnostic Validator for Text-to-SQL with Reward Allocation and Co-occurrence Shaping

[官方论文页](https://neurips.cc/virtual/2026/poster/155455) · [作者来源](https://openreview.net/forum?id=5TcCMJta3q)

- **问题 / 瓶颈** · 序列统一奖励会同时强化正确标签和错误解释
- **核心创新 / 方法** · 拆分诊断奖励，并将错误类型共现用于优化训练信号
- **Baseline** · 标准 GRPO 的序列奖励
- **Benchmark** · Text-to-SQL 验证与错误诊断，数据集待核
- **关键结果 / 消融** · 作者报告改善信用分配与诊断，数值待核
- **适用条件 / 局限** · 错误共现依赖数据域

**可复用机制** · 多字段验证器对齐分项奖励，检查正确子项是否掩盖错误子项

<a id="paper-149867"></a>

## DialBandit: Adaptive Sequential Search with Tunable Evaluation Fidelity

[官方论文页](https://neurips.cc/virtual/2026/poster/149867) · [作者来源](https://openreview.net/forum?id=mcHs6YbNzO)

- **问题 / 瓶颈** · 固定评估强度忽略其成本与噪声
- **核心创新 / 方法** · 重复评估估计各模型的精度–噪声曲线，再按不确定性规划
- **Baseline** · 固定评估的级联及 oracle 索引策略
- **Benchmark** · 在线顺序搜索与语言模型级联
- **关键结果 / 消融** · 作者给出联合停止与精度选择的索引策略
- **适用条件 / 局限** · 需重复评估和可比较的成本量纲

**可复用机制** · 用相同预算比较固定检查与按模型适配检查精度

<a id="paper-155164"></a>

## Dialect ASR based on Multi-View Pseudo-Parallel Augmentation and Noise-Robust Contrastive Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/155164) · [作者来源](https://openreview.net/forum?id=7oIszAz46V)

- **问题 / 瓶颈** · 方言标注稀缺且语料往往不平行
- **核心创新 / 方法** · 生成伪平行视图，联合语义和方言层级的抗噪对比学习
- **Baseline** · Whisper-large 适配及已有方法
- **Benchmark** · 瑞士德语、中文和阿拉伯语方言识别
- **关键结果 / 消融** · 作者报告可推广到非平行数据，数值待核
- **适用条件 / 局限** · 伪配对质量及方言覆盖限制迁移

**可复用机制** · 将共享内容与方言信息分开设计对比关系

<a id="paper-153135"></a>

## DialectLLM: A Dialect-Aware Dialog[ue] Generation Framework Beyond Standard American English

[官方论文页](https://neurips.cc/virtual/2026/poster/153135) · [作者来源](https://openreview.net/forum?id=NcciyroKQl)

- **问题 / 瓶颈** · 一套转换规则用于双方可能产生不自然的拟态
- **核心创新 / 方法** · 由母语语言学家核验词汇、拼写与句法规则，构建九种方言平行对话
- **Baseline** · 既有方言文本生成方法
- **Benchmark** · 人工偏好及方言自然度评估
- **关键结果 / 消融** · 摘要报告成对自然度偏好为 98.8%
- **适用条件 / 局限** · 英语九种方言，人工偏好不代表所有社群

**可复用机制** · 将识别方言和生成恰当回应拆成不同任务

<a id="paper-139390"></a>

## DIBench: Benchmarking Decision Integrity of GUI-based Mobile Agents Under Deceptive Injections

[官方论文页](https://neurips.cc/virtual/2026/poster/139390) · [作者来源](https://openreview.net/forum?id=TLLDufyhSM)

- **问题 / 瓶颈** · 流程执行成功仍可能选错对象
- **核心创新 / 方法** · 在授权测试中比较目标约束与最终选择，使用统一的决策完整性指标
- **Baseline** · 任务成功等执行层指标
- **Benchmark** · 七款商业及三款模拟应用、五类任务
- **关键结果 / 消融** · 作者发现执行成功不能覆盖隐藏决策偏离
- **适用条件 / 局限** · 覆盖限于所测应用与任务

**可复用机制** · 部署审核同时记录流程完成与候选对象选择的约束一致性

<a id="paper-151451"></a>

## DICE: Decoupling Capability from Intervention Necessity in LLM Tutoring

[官方论文页](https://neurips.cc/virtual/2026/poster/151451) · [作者来源](https://openreview.net/forum?id=aa9Or06597)

- **问题 / 瓶颈** · 下一句教师话语训练隐含每轮都需回应
- **核心创新 / 方法** · 先选教学动作，用含无干预对照的滚动价值加权学习
- **Baseline** · 总是生成回应等教学策略
- **Benchmark** · DICE-Bench 多变体数学辅导及模拟会话
- **关键结果 / 消融** · 作者报告减少不必要干预并维持辅导效果
- **适用条件 / 局限** · 模拟学习者不能代替真实学生验证

**可复用机制** · 在对话代理中单独学习是否介入，并使用不介入作为反事实对照

<a id="paper-148173"></a>

## DICEQuant: Distortion-Compensated Rounding with Dual-Ended Shrinkage for LLM Quantization

[官方论文页](https://neurips.cc/virtual/2026/poster/148173) · [作者来源](https://openreview.net/forum?id=zk0THf3od5)

- **问题 / 瓶颈** · 局部重构忽视上游失真
- **核心创新 / 方法** · CURE 平稳求导，DCR 调整舍入中心并用 Hessian 加权
- **Baseline** · 旋转式后训练量化
- **Benchmark** · 语言模型后训练量化
- **关键结果 / 消融** · 摘要报告统一误差建模；量化幅度待核
- **适用条件 / 局限** · 依赖失真与曲率近似

**可复用机制** · 将上游噪声纳入舍入目标

<a id="paper-151096"></a>

## DictLLM: Post-training Compression of Large Language Model with Dictionary Kernels

[官方论文页](https://neurips.cc/virtual/2026/poster/151096) · [作者来源](https://openreview.net/forum?id=d0p33Top6I)

- **问题 / 瓶颈** · 逐层压缩重复存储
- **核心创新 / 方法** · 以 SVD 初始化，对稀疏系数和字典分别做曲率感知量化
- **Baseline** · 逐层压缩
- **Benchmark** · 移动端语言模型压缩；具体任务待核
- **关键结果 / 消融** · 共享字典与稀疏系数减少存储；幅度待核
- **适用条件 / 局限** · 依赖层间共享结构

**可复用机制** · 比较共用字典与独立分解的内存和误差

<a id="paper-152453"></a>

## DiDE: Direct Injection with Color-Texture DEcoupling for 3D Stylization

[官方论文页](https://neurips.cc/virtual/2026/poster/152453) · [作者来源](https://openreview.net/forum?id=T0OsmO746x)

- **问题 / 瓶颈** · 联合风格迁移使二者干扰
- **核心创新 / 方法** · 分配潜空间通道，并在自注意力中组合两类参考
- **Baseline** · 二维及三维风格迁移
- **Benchmark** · Disen3D-Bench
- **关键结果 / 消融** · 作者报告风格控制优于对照
- **适用条件 / 局限** · 依赖潜空间存在可分通道

**可复用机制** · 在固定内容下分别交换颜色与纹理参考

<a id="paper-155720"></a>

## Diff3R: Feed-forward 3D Gaussian Splatting with Uncertainty Aware Differentiable Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/155720) · [作者来源](https://openreview.net/forum?id=3QXU3rF61y)

- **问题 / 瓶颈** · 快速预测质量和逐场景优化成本存在权衡
- **核心创新 / 方法** · 用隐式微分和无矩阵 PCG 将求解嵌入训练，以不确定性约束更新
- **Baseline** · 前馈与逐场景优化 3DGS
- **Benchmark** · 稀疏视图重建
- **关键结果 / 消融** · 作者报告更能抵御异常输入和欠约束过拟合
- **适用条件 / 局限** · 额外求解增加延迟

**可复用机制** · 用相同优化预算比较普通预测和端到端学得的初始化

<a id="paper-149887"></a>

## Diff-Aid: Inference-time Adaptive Interaction Denoising for Rectified Text-to-Image Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/149887) · [作者来源](https://openreview.net/forum?id=mUAzPnYiWX)

- **问题 / 瓶颈** · 固定条件权重忽略去噪阶段差异
- **核心创新 / 方法** · 推理时自适应调节图文交互
- **Baseline** · SD 3.5 和 FLUX
- **Benchmark** · 提示遵循、视觉质量、人偏好及下游编辑
- **关键结果 / 消融** · 作者报告多指标改善
- **适用条件 / 局限** · 跨模型与提示的额外成本待核

**可复用机制** · 对照固定和动态条件调制

<a id="paper-150268"></a>

## DiffATS: Diffusion in Aligned Tensor Space

[官方论文页](https://neurips.cc/virtual/2026/poster/150268) · [作者来源](https://openreview.net/forum?id=jQzUVefSI5)

- **问题 / 瓶颈** · 同一张量可有多种旋转表示
- **核心创新 / 方法** · 以中心样本为锚做正交 Procrustes，再在对齐张量原语上扩散
- **Baseline** · 直接扩散与学习式压缩路线
- **Benchmark** · 高分辨率时空场；细节待核
- **关键结果 / 消融** · 作者给出原语与低秩张量间的同胚证明
- **适用条件 / 局限** · 依赖所用低秩表示和空间设定

**可复用机制** · 先对齐等价表示再做生成建模

<a id="paper-152243"></a>

## DiffCap-RL: Differential QA Rewards for Dense Image and Video Captioning

[官方论文页](https://neurips.cc/virtual/2026/poster/152243) · [作者来源](https://openreview.net/forum?id=UWkuOadUR9)

- **问题 / 瓶颈** · 静态 QA 奖励会饱和
- **核心创新 / 方法** · 以离线评分为锚，分离冲突问题和补充细节问题
- **Baseline** · 静态 QA 与粗粒度评判
- **Benchmark** · 图像视频描述、人评、在线 RL 与多样本选择
- **关键结果 / 消融** · 作者报告可维持判别信号；幅度待核
- **适用条件 / 局限** · 依赖问题和视觉回答可靠性

**可复用机制** · 按候选分歧动态测试事实与新增细节

<a id="paper-152753"></a>

## Diff-CA: Separating Common and Salient Factors with Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152753) · [作者来源](https://openreview.net/forum?id=QbYbgrobWj)

- **问题 / 瓶颈** · 传统对比分析重建质量受限
- **核心创新 / 方法** · 先训图像条件扩散，再弱监督学习加性条件分解
- **Baseline** · VAE 和 GAN 对比分析路线
- **Benchmark** · 图像重建与定向编辑
- **关键结果 / 消融** · 在给定条件下证明加性分解可识别
- **适用条件 / 局限** · 依赖加性假设和弱监督

**可复用机制** · 通过交换特异因素检查共享因素是否保留

<a id="paper-152390"></a>

## DiffCool: Label-Free Synthesis of Chip-Tailored Heat Sinks via Thermal-Aware Diffusion

[官方论文页](https://neurips.cc/virtual/2026/poster/152390) · [作者来源](https://openreview.net/forum?id=TSSdr3DP9M)

- **问题 / 瓶颈** · 缺少最优散热器布局标注
- **核心创新 / 方法** · 以可制造的离散转移和可微热损失驱动生成
- **Baseline** · 传统散热器
- **Benchmark** · 开源处理器、峰温和温度梯度
- **关键结果 / 消融** · 峰温降 28.3%，温度梯度降 56.9%
- **适用条件 / 局限** · 单一处理器证据，依赖热代理

**可复用机制** · 无标签逆设计可结合约束采样和仿真损失

<a id="paper-151447"></a>

## Diffeomoprhism-Informed 3D Gaussian Splattings via Screen-Space Optimal Transport (OT)

[官方论文页](https://neurips.cc/virtual/2026/poster/151447) · [作者来源](https://openreview.net/forum?id=ac9rdVDTOU)

- **问题 / 瓶颈** · 均匀降采样丢掉细边
- **核心创新 / 方法** · 用屏幕空间最优传输重参数化图像
- **Baseline** · 原始 3DGS
- **Benchmark** · 新视角合成与感知指标
- **关键结果 / 消融** · BRISQUE 等改善，PSNR 和 SSIM 可能下降
- **适用条件 / 局限** · 指标依赖参考图像分辨率

**可复用机制** · 用固定像素预算比较均匀和非均匀监督

<a id="paper-155314"></a>

## DiffeoMorph: Learning to Morph 3D Shapes Using Differentiable Agent-Based Simulations

[官方论文页](https://neurips.cc/virtual/2026/poster/155314) · [作者来源](https://openreview.net/forum?id=6WbQEdAa2e)

- **问题 / 瓶颈** · 逐点匹配对数量和排序敏感
- **核心创新 / 方法** · 在仿真中用旋转对齐的三维 Zernike 损失比较形状
- **Baseline** · 形状损失对照；具名待核
- **Benchmark** · 分布式形状形成仿真
- **关键结果 / 消融** · 作者报告形状损失有优势；幅度待核
- **适用条件 / 局限** · 仅据非生物仿真抽象

**可复用机制** · 对机器人群任务比较分布级与逐点监督

<a id="paper-148506"></a>

## Difference of Convex Programming in the Wasserstein Space with Applications to MMD Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/148506) · [作者来源](https://openreview.net/forum?id=xKLfU6Cqa2)

- **问题 / 瓶颈** · Wasserstein 一阶方法在非测地凸目标上难分析
- **核心创新 / 方法** · 将 CCCP 扩展到 Wasserstein 空间并为 MMD 和能量距离构造凸差分解
- **Baseline** · Wasserstein 梯度下降
- **Benchmark** · MMD 和能量距离优化
- **关键结果 / 消融** · 证明所设条件下近驻点性质并报告部分分解收敛更快
- **适用条件 / 局限** · 依赖分解及曲率假设

**可复用机制** · 比较不同凸差分解的稳定性

<a id="paper-154330"></a>

## Differencing the Diffusion Trajectory toward Uncertain Components for Time Series Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/154330) · [作者来源](https://openreview.net/forum?id=EQ3rr1gzcl)

- **问题 / 瓶颈** · 历史对慢趋势和高频残差约束不同
- **核心创新 / 方法** · 令前向过程逐步向二阶差分结构移动，用阶段门控结合两类历史
- **Baseline** · 直接扩散与外部预分解
- **Benchmark** · 概率时序预测；指标待核
- **关键结果 / 消融** · 作者提出端到端吸收可预测性差异；幅度待核
- **适用条件 / 局限** · 依赖差分能分离趋势与不确定性

**可复用机制** · 对照固定预处理与时变扩散算子

<a id="paper-154944"></a>

## Differentiable Belief-based Opponent Shaping

[官方论文页](https://neurips.cc/virtual/2026/poster/154944) · [作者来源](https://openreview.net/forum?id=9kOlSk4Zqs)

- **问题 / 瓶颈** · 参数空间更新无法显式描述观察者信念
- **核心创新 / 方法** · 在隐藏角色仿真中建模多观察者的信念更新
- **Baseline** · PPO 与 BBM
- **Benchmark** · 隐藏角色博弈
- **关键结果 / 消融** · 作者报告混合动机设置收益最大
- **适用条件 / 局限** · 依赖信念模型与封闭规则

**可复用机制** · 在仿真中比较显式信念和无信念策略

<a id="paper-148406"></a>

## Differentiable Bit-Widths: Co-optimizing Pruning and Quantization via SVD for Ultra-Efficient LLM Compression

[官方论文页](https://neurips.cc/virtual/2026/poster/148406) · [作者来源](https://openreview.net/forum?id=y5tDLoawiV)

- **问题 / 瓶颈** · 先剪枝再量化无法联动预算
- **核心创新 / 方法** · 学习 SVD 成分的可微位宽
- **Baseline** · 两阶段压缩
- **Benchmark** · 极低位宽语言模型压缩
- **关键结果 / 消融** · 作者报告在 1.61 位时仍有竞争力
- **适用条件 / 局限** · 部署收益依赖混合精度实现

**可复用机制** · 固定总位预算比较联合和顺序分配

<a id="paper-156759"></a>

## Differentiable Cluster Discovery in Temporal Graphs

[官方论文页](https://neurips.cc/virtual/2026/poster/156759) · [作者来源](https://openreview.net/forum?id=1caZVb6zL7)

- **问题 / 瓶颈** · 静态目标分布与动态图编码冲突
- **核心创新 / 方法** · 用 Gumbel–Softmax 采样、期望聚类与时序一致性损失
- **Baseline** · 时序图聚类方法
- **Benchmark** · 六个真实时序图数据集
- **关键结果 / 消融** · 作者报告聚类精度和稳健性改善
- **适用条件 / 局限** · 依赖时序一致性符合任务

**可复用机制** · 测联合软离散分组能否减少梯度振荡

<a id="paper-148538"></a>

## Differentiable Exact Learning of Algorithms

[官方论文页](https://neurips.cc/virtual/2026/poster/148538) · [作者来源](https://openreview.net/forum?id=x9jhyvsLzO)

- **问题 / 瓶颈** · 单靠输入输出难保证递归算法可学
- **核心创新 / 方法** · 用可微有限状态转导器和策略轨迹学习，并抽取离散转导器
- **Baseline** · RNN 控制器及输入输出学习路线
- **Benchmark** · 二进制和十进制加法乘法
- **关键结果 / 消融** · 报告泛化到数千倍长度，并在聚类假设下证明加法抽取正确性
- **适用条件 / 局限** · 证明并未覆盖所有实验任务

**可复用机制** · 将外部轨迹用于中间监督并单独验证离散规则

<a id="paper-153641"></a>

## Differentiable Knapsack and Top-k Operators via Dynamic Programming

[官方论文页](https://neurips.cc/virtual/2026/poster/153641) · [作者来源](https://openreview.net/forum?id=Joe3lARuyi)

- **问题 / 瓶颈** · 离散选择几乎处处无梯度
- **核心创新 / 方法** · 统一背包和 Top-k 的平滑递推及并行反向计算
- **Baseline** · 离散原算子；具体实证对照待核
- **Benchmark** · 背包预测、离散 VAE、受约束推荐 RL
- **关键结果 / 消融** · 证明特定置换等变条件下 Shannon 正则唯一
- **适用条件 / 局限** · 受 DP 状态空间及平滑影响

**可复用机制** · 比较递推平滑与对输出直接连续松弛

<a id="paper-153043"></a>

## Differentiable Learning of Lifted Action Schemas for Classical Planning

[官方论文页](https://neurips.cc/virtual/2026/poster/153043) · [作者来源](https://openreview.net/forum?id=OSDbmV3Glw)

- **问题 / 瓶颈** · 轨迹可见但动作参数缺失
- **核心创新 / 方法** · 根据状态差异学习共享 lifted 动作模式
- **Baseline** · 已有规划模式学习路线
- **Benchmark** · 多个经典规划域
- **关键结果 / 消融** · 作者报告良好学习表现；幅度待核
- **适用条件 / 局限** · 假设状态完全可观测

**可复用机制** · 先在结构化状态轨迹验证再扩展到感知输入

<a id="paper-153003"></a>

## Differentiable Nonlinear Model Predictive Control

[官方论文页](https://neurips.cc/virtual/2026/poster/153003) · [作者来源](https://openreview.net/forum?id=OgtCRU5ApQ)

- **问题 / 瓶颈** · 一般非线性 MPC 缺少高效梯度实现
- **核心创新 / 方法** · 对内点平滑条件做隐式微分，在 SQP 中实现正向与伴随灵敏度
- **Baseline** · mpc.pytorch 与 cvxpygen
- **Benchmark** · 一般最优控制问题的灵敏度求值
- **关键结果 / 消融** · 作者报告加速超过三倍
- **适用条件 / 局限** · 依赖求解收敛和局部灵敏度条件

**可复用机制** · 复用求解器结构评估梯度而不展开迭代

<a id="paper-149856"></a>

## Differentiable Range-Partition Entropy for Entropy-Sensitive Geometric Algorithms

[官方论文页](https://neurips.cc/virtual/2026/poster/149856) · [作者来源](https://openreview.net/forum?id=ml7qF9daTZ)

- **问题 / 瓶颈** · 硬分区熵不可直接求梯度
- **核心创新 / 方法** · 构造软半空间单元并区分归一化熵与规模加权工作量
- **Baseline** · SciPy/Qhull 管线
- **Benchmark** · 二维凸包与 Delaunay
- **关键结果 / 消融** · 求解器最高加速约 4–5 倍，凸包面积误差低于 0.2%
- **适用条件 / 局限** · 依赖间隔分离，端到端收益较小

**可复用机制** · 同时报告预处理成本和求解加速，避免把归一化熵直接当运行时间

<a id="paper-156105"></a>

## Differentiable Systematic Resampling for Variational Sequential Monte Carlo

[官方论文页](https://neurips.cc/virtual/2026/poster/156105) · [作者来源](https://openreview.net/forum?id=0Mo3B5JStu)

- **问题 / 瓶颈** · 离散重采样阻断反传
- **核心创新 / 方法** · 引入温度控制的系统重采样松弛
- **Baseline** · 最优传输式可微重采样
- **Benchmark** · 随机动态系统和手写数据
- **关键结果 / 消融** · 偏差随退火指数收敛，实验性能可比且开销更低
- **适用条件 / 局限** · 有限温度存在偏差

**可复用机制** · 联合扫描温度、估计误差与计算开销

<a id="paper-139203"></a>

## Differential Item Functioning as an Item-Level Diagnostic for LLM Benchmarks

[官方论文页](https://neurips.cc/virtual/2026/poster/139203) · [作者来源](https://openreview.net/forum?id=ejdzLQqAqP)

- **问题 / 瓶颈** · 聚合分数隐藏题型差异
- **核心创新 / 方法** · 条件化整体得分后用 Mantel–Haenszel 诊断差异题项
- **Baseline** · 聚合分数与两家族对比
- **Benchmark** · 六个基准，Llama 和 Qwen
- **关键结果 / 消融** · 按偏向选择题目可改变甚至反转排名
- **适用条件 / 局限** · 受模型家族和题目分层影响

**可复用机制** · 报告题项偏差及移除偏题后的排名敏感性

<a id="paper-149241"></a>

## Differentially Private Model Merging

[官方论文页](https://neurips.cc/virtual/2026/poster/149241) · [作者来源](https://openreview.net/forum?id=rtA6xeWV0d)

- **问题 / 瓶颈** · 部署要求变化时重新训练成本高
- **核心创新 / 方法** · 比较随机选择与线性组合，并直接做隐私会计
- **Baseline** · 随机模型选择
- **Benchmark** · 均值估计理论与真实及合成数据
- **关键结果 / 消融** · 均值估计中线性组合隐私效用更优
- **适用条件 / 局限** · 需对同数据集上的联合机制做会计

**可复用机制** · 生成部署模型前对组合机制重新验证目标预算

<a id="paper-148832"></a>

## Differentially Private Sparse Reward Estimation with Preference Feedback

[官方论文页](https://neurips.cc/virtual/2026/poster/148832) · [作者来源](https://openreview.net/forum?id=up1oAQCUCJ)

- **问题 / 瓶颈** · 稠密模型误差随环境维数放大
- **核心创新 / 方法** · 对成对偏好分别建立样本级和标签级差分隐私估计
- **Baseline** · 稠密私有奖励估计
- **Benchmark** · 情感生成及安全对齐
- **关键结果 / 消融** · 稀疏误差界主要依赖有效维度，实证权衡改善
- **适用条件 / 局限** · 依赖稀疏性和 Bradley–Terry–Luce 假设

**可复用机制** · 按保护对象和特征有效维数选择估计目标

<a id="paper-155037"></a>

## Differential Vector Erasure: Unified Training-Free Concept Erasure for Flow Matching Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155037) · [作者来源](https://openreview.net/forum?id=8tyFYkKJGC)

- **问题 / 瓶颈** · 微调成本高且 DDPM 方案不直接适用
- **核心创新 / 方法** · 用目标和锚概念的速度场差异定义抑制方向
- **Baseline** · 现有概念擦除方法
- **Benchmark** · FLUX 概念抑制、画质与多样性
- **关键结果 / 消融** · 报告抑制改善且质量保持
- **适用条件 / 局限** · 依赖合适锚及概念可分离性

**可复用机制** · 同时测删除目标与保留语义，避免只报告抑制成功

<a id="paper-151671"></a>

## Differentiating Network Design Objectives for Balancing Cost and Distance

[官方论文页](https://neurips.cc/virtual/2026/poster/151671) · [作者来源](https://openreview.net/forum?id=YuYZQCQoQp)

- **问题 / 瓶颈** · 建设成本和路程相互耦合
- **核心创新 / 方法** · 用动态无环删边稳定路由，截断值求解后拓扑舍入
- **Baseline** · 专用算法、可微方案和商业求解器
- **Benchmark** · 1487 个运输及合成图实例
- **关键结果 / 消融** · 报告时间质量折衷改善，在规定条件下固定精度计算量为 O(m log n)
- **适用条件 / 局限** · 理论依赖论文限定条件

**可复用机制** · 将离散网络选择改写为无环局部策略，并单独检验舍入损失

<a id="paper-153078"></a>

## Diff-Instruct with Diffused Reward: Towards Principled One-step Generator RL

[官方论文页](https://neurips.cc/virtual/2026/poster/153078) · [作者来源](https://openreview.net/forum?id=OAfN5ujM04)

- **问题 / 瓶颈** · 仅优化终点奖励会损害保真度
- **核心创新 / 方法** · 将奖励倾斜分布传播到各噪声级，用短步去噪估计分数修正
- **Baseline** · 既有一步 SDXL 方法及多步教师
- **Benchmark** · SDXL 与 Z-Image 上的偏好和画质
- **关键结果 / 消融** · 报告 Pareto 表现改善，Z-Image 一步偏好超过 50 步教师
- **适用条件 / 局限** · 代理误差与奖励覆盖待核

**可复用机制** · 在相同生成步数下同时比较偏好与保真

<a id="paper-150096"></a>

## Diff-Kalman: Difference-Driven Learning for Structure-Preserving Kalman Filtering

[官方论文页](https://neurips.cc/virtual/2026/poster/150096) · [作者来源](https://openreview.net/forum?id=kk5tmlhwi6)

- **问题 / 瓶颈** · 直接预测高维滤波参数容易不稳定
- **核心创新 / 方法** · 用历史状态差预测增量，用差分残差调节协方差和增益
- **Baseline** · 代表性滤波方法
- **Benchmark** · MOT 轨迹和 Lorenz 动力学
- **关键结果 / 消融** · 报告估计精度改善
- **适用条件 / 局限** · 两模块独立收益待核

**可复用机制** · 保留经典滤波结构，只学习低维差分修正

<a id="paper-148542"></a>

## DiffPTS: Rethinking Diffusion ELBO for Probabilistic Time Series Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/148542) · [作者来源](https://openreview.net/forum?id=x7OutBc7Vk)

- **问题 / 瓶颈** · 分开预训练均值和方差会割裂变分目标
- **核心创新 / 方法** · 从位置尺度噪声模型重新推导 ELBO 并联合优化
- **Baseline** · 扩散式概率预测方法
- **Benchmark** · 多个预测基准，CRPS 和 MSE
- **关键结果 / 消融** · 平均分别降低超过 14.53% 和 16.55%
- **适用条件 / 局限** · 依赖位置尺度噪声设定

**可复用机制** · 在同骨干比较联合 ELBO 和预训练统计量

<a id="paper-150450"></a>

## DifFRACT: Diffusion Feature Reconstruction and Attribution for Circuit Tracing

[官方论文页](https://neurips.cc/virtual/2026/poster/150450) · [作者来源](https://openreview.net/forum?id=hwwQnLpJt5)

- **问题 / 瓶颈** · 注意力图难解释 MLP 中的语义组合
- **核心创新 / 方法** · 训练时间条件 transcoder 并在线性化计算中归因特征
- **Baseline** · 稀疏自编码器与注意力分析
- **Benchmark** · FLUX.1[schnell] 上的属性绑定及稀疏保真
- **关键结果 / 消融** · 报告稀疏保真折衷可比或更佳并定位系统性错误
- **适用条件 / 局限** · 依赖替代层的保真及线性化

**可复用机制** · 以时刻分层验证归因，并用良性属性干预检验因果作用

<a id="paper-155104"></a>

## DiffRatio: Training One-Step Diffusion Models Without Teacher Supervision

[官方论文页](https://neurips.cc/virtual/2026/poster/155104) · [作者来源](https://openreview.net/forum?id=8PGxK47BQD)

- **问题 / 瓶颈** · 蒸馏梯度叠加教师及学生分数误差
- **核心创新 / 方法** · 按扩散时刻学习学生与数据的对数密度比，预训练分数模型只初始化
- **Baseline** · 教师监督蒸馏
- **Benchmark** · CIFAR-10 和两种分辨率 ImageNet
- **关键结果 / 消融** · 报告优于多数蒸馏对照
- **适用条件 / 局限** · 初始化仍依赖预训练，候选并行有计算成本

**可复用机制** · 在等总推理开销下比较密度比筛选与增加串行步数

<a id="paper-151677"></a>

## DiffRisk: Diffusion Representation Learning with Informative Missingness for Health Risk Prediction

[官方论文页](https://neurips.cc/virtual/2026/poster/151677) · [作者来源](https://openreview.net/forum?id=Ys3sg1XgsA)

- **问题 / 瓶颈** · 插补可能抹掉有信息量的缺测模式
- **核心创新 / 方法** · 用条件分数目标学习观测子集对应的潜在条件分布
- **Baseline** · 健康风险预测基线
- **Benchmark** · 五项基于电子病历的风险预测任务
- **关键结果 / 消融** · 报告均优于所比基线
- **适用条件 / 局限** · 缺失模式可能随机构政策变化

**可复用机制** · 按缺失模式及机构分层评估，不用随机缺失替代真实机制

<a id="paper-149202"></a>

## DiffScore: Text Evaluation Beyond Autoregressive Likelihood

[官方论文页](https://neurips.cc/virtual/2026/poster/149202) · [作者来源](https://openreview.net/forum?id=sAJrqWRuQf)

- **问题 / 瓶颈** · 自回归分数受单向位置影响
- **核心创新 / 方法** · 双向评分并用 PMI 分解流畅性和忠实度
- **Baseline** · 自回归评价器
- **Benchmark** · 十项基准，零样本及微调
- **关键结果 / 消融** · 报告两种设置均改善
- **适用条件 / 局限** · 双向掩码只能消除单向因式分解偏差

**可复用机制** · 记录跨掩码率质量曲线，而非一个总分

<a id="paper-150318"></a>

## Diffusion-DRF: Free, Rich, and Differentiable Reward for Video Diffusion Fine-Tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/150318) · [作者来源](https://openreview.net/forum?id=izqmMvuObQ)

- **问题 / 瓶颈** · 全局奖励难定位提示与视频的局部错配
- **核心创新 / 方法** · 让冻结视觉语言评价器回答多维开放问题并用可微信号优化
- **Baseline** · Flow-GRPO
- **Benchmark** · 未见的 VBench-2.0
- **关键结果 / 消融** · 总体表现提高 4.74 分
- **适用条件 / 局限** · 评价器偏差和问题覆盖待核

**可复用机制** · 用分项反馈识别具体错配，保留独立画质评估

<a id="paper-155420"></a>

## Diffusion-Enhanced GFlowNet for Solving Vehicle Routing Problems

[官方论文页](https://neurips.cc/virtual/2026/poster/155420) · [作者来源](https://openreview.net/forum?id=5pGVh6PbGd)

- **问题 / 瓶颈** · 高奖励区域内生成流扩展不足
- **核心创新 / 方法** · 对边级反向信号加噪去噪，配规模适配解码
- **Baseline** · 车辆路径求解基线
- **Benchmark** · 合成和真实数据，最多一万节点
- **关键结果 / 消融** · 报告性能改善，具体幅度待核
- **适用条件 / 局限** · 复杂规模时算力及多样性需同时量化

**可复用机制** · 比较等预算下高质量解覆盖而非仅比较最优值

<a id="paper-154060"></a>

## Diffusion Fine-Tuning: Iterative Refinement for Advanced Grounding with Diffusion Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154060) · [作者来源](https://openreview.net/forum?id=GUkwzvouGc)

- **问题 / 瓶颈** · 早期定位错误不可回改且难预算顶点
- **核心创新 / 方法** · 离散扩散共同去噪坐标，以数位粗到细训练
- **Baseline** · 匹配微调的自回归视觉语言模型
- **Benchmark** · 二维框、16 点多边形和单目三维框
- **关键结果 / 消融** · 二维框相当，多边形改善，采用 12 步联合去噪
- **适用条件 / 局限** · 仍有去噪串行成本，较多顶点有质量与时延取舍

**可复用机制** · 固定顶点预算比较联合修正与逐点生成

<a id="paper-150176"></a>

## Diffusion fine-tuning with Rewarded Moment Matching Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/150176) · [作者来源](https://openreview.net/forum?id=k7jVv4PA8D)

- **问题 / 瓶颈** · 单独奖励微调可能降低蒸馏保真
- **核心创新 / 方法** · 在线采样训练并用矩匹配蒸馏损失近似积分 KL
- **Baseline** · DI++、DRaFT、HyperNoise 和 GenCast 教师
- **Benchmark** · ImageNet FID–奖励及天气 CRPS
- **关键结果 / 消融** · GenCast 加速 7.5 倍，93% 目标变量优于教师且校准改善
- **适用条件 / 局限** · 天气结论限目标变量和协议

**可复用机制** · 画奖励与质量的 Pareto 曲线，并对概率模型检查校准

<a id="paper-151465"></a>

## Diffusion Guidance Is a Controllable Policy Improvement Operator

[官方论文页](https://neurips.cc/virtual/2026/poster/151465) · [作者来源](https://openreview.net/forum?id=aQYvs5JZpu)

- **问题 / 瓶颈** · 价值建模限制生成式策略扩展
- **核心创新 / 方法** · 将扩散引导推导为策略改进算子并允许不显式学习价值函数
- **Baseline** · 监督式目标条件行为克隆
- **Benchmark** · 离线强化学习任务
- **关键结果 / 消融** · 作者观察引导权重增加时表现提高，范围待核
- **适用条件 / 局限** · 不能保证超出实测范围仍单调

**可复用机制** · 在固定训练下扫描引导权重，同时检查分布偏移

<a id="paper-154873"></a>

## Diffusion Language Models Can Approximate Optimal Infilling Lengths Implicitly

[官方论文页](https://neurips.cc/virtual/2026/poster/154873) · [作者来源](https://openreview.net/forum?id=AFvSuWgvYZ)

- **问题 / 瓶颈** · 固定长度约束双向补全。
- **核心创新 / 方法** · 利用真实长度附近的首步置信峰，扣除系统性长度偏差后搜索。
- **Baseline** · 固定长度与聊天式自适应。
- **Benchmark** · 代码补全 Pass@1，文本补全 BLEU-2 和 ROUGE-L。
- **关键结果 / 消融** · 对两类代码基线最高分别改善 47.7% 和 40.5%；文本指标最高改善 8.5% 和 9.9%。
- **适用条件 / 局限** · 依赖候选范围内仍有可辨认的置信峰。

**可复用机制** · 把长度搜索放在正式去噪前，比较校准前后的搜索开销与补全质量。

<a id="paper-148526"></a>

## Diffusion Masked Pretraining for Dynamic Point Cloud

[官方论文页](https://neurips.cc/virtual/2026/poster/148526) · [作者来源](https://openreview.net/forum?id=xFR59J1lic)

- **问题 / 瓶颈** · 真实掩码中心泄漏，位移点估计会平均多个可能轨迹。
- **核心创新 / 方法** · 只对被掩码管中心加噪并预测其位置；以条件扩散噪声预测监督位移。
- **Baseline** · 未加 DiMP 的骨干。
- **Benchmark** · 离线动作分割及因果约束在线推理，评估准确率。
- **关键结果 / 消融** · 绝对改善分别为 11.21% 和 13.65%。
- **适用条件 / 局限** · 两分支各自收益与跨传感器泛化待核。

**可复用机制** · 掩码预训练同时排查位置旁路和多解目标被均值抹平的问题。

<a id="paper-154312"></a>

## Diffusion Meta-Prompting and Steering for Generalizable Foundation Model Adaptation

[官方论文页](https://neurips.cc/virtual/2026/poster/154312) · [作者来源](https://openreview.net/forum?id=EbyKAh8h40)

- **问题 / 瓶颈** · 逐任务学提示难迁移到新类别、领域和组合。
- **核心创新 / 方法** · 以任务描述条件化提示扩散，用训练阶段选出的提示作推理采样锚点。
- **Baseline** · 提示检索与元学习方法。
- **Benchmark** · 分类、检索与文生图，含 55 对数据集组合分类。
- **关键结果 / 消融** · 组合分类平均最多提高 2.0%，个别组合达 8.5%；相对提示检索存储与推理成本降低逾 90%。
- **适用条件 / 局限** · 依赖历史提示库覆盖与可比较的参数空间。

**可复用机制** · 无法访问新任务数据时，对照提示检索和任务描述条件合成，再测锚点消融。

<a id="paper-150031"></a>

## Diffusion Model's Generalization Can Be Characterized by Inductive Biases toward a Data-Dependent Ridge Manifold

[官方论文页](https://neurips.cc/virtual/2026/poster/150031) · [作者来源](https://openreview.net/forum?id=lIze4Hj7sl)

- **问题 / 瓶颈** · 只判断有没有记住训练数据，无法解释新样本落到哪里。
- **核心创新 / 方法** · 以平滑经验分布构建时变对数密度脊，分析反向过程的接近、对齐与沿脊运动。
- **Baseline** · 随机特征模型中比较架构偏置与优化误差。
- **Benchmark** · 合成多峰数据与 MNIST 潜扩散的几何轨迹。
- **关键结果 / 消融** · 理论区分法向偏差与切向运动，实验支持预测。
- **适用条件 / 局限** · 脊结构与误差分解的可估计性依赖条件。

**可复用机制** · 生成诊断分别测离数据结构的法向误差和沿结构的覆盖差异。

<a id="paper-151563"></a>

## Diffusion Models Observe Only Gradients: A Geometric Perspective on Score Matching Errors

[官方论文页](https://neurips.cc/virtual/2026/poster/151563) · [作者来源](https://openreview.net/forum?id=ZfRxNzTSSZ)

- **问题 / 瓶颈** · 全量 L2 分数误差大时边缘分布仍可正确。
- **核心创新 / 方法** · 将误差分成梯度与无散分量，以对偶 Sobolev 恒等式估计影响边缘动力学的部分。
- **Baseline** · 全量 L2 分数误差与路径空间 Girsanov 界。
- **Benchmark** · 理论 KL 界与采样质量相关性实验；具体基准待核。
- **关键结果 / 消融** · 作者给出全量误差无法统一下界散度的结果，梯度误差估计在实验中相关性更强。
- **适用条件 / 局限** · 对应特定边缘动力学几何；对轨迹质量的含义需另验。

**可复用机制** · 验证生成模型时比较损失、梯度误差和边缘样本质量，避免把路径误差直接当边缘误差。

<a id="paper-150145"></a>

## Diffusion Models without Classifier-free Guidance

[官方论文页](https://neurips.cc/virtual/2026/poster/150145) · [作者来源](https://openreview.net/forum?id=kLqGIEnVoC)

- **问题 / 瓶颈** · CFG 采样用到的倾斜分数与训练目标不一致。
- **核心创新 / 方法** · Model-guidance 将后验倾斜并入训练并在线自举，采样省掉额外引导前向。
- **Baseline** · CFG 及蒸馏类思路。
- **Benchmark** · ImageNet 256，评估 FID 与推理速度。
- **关键结果 / 消融** · 摘要报告 FID 1.34，推理约提速两倍。
- **适用条件 / 局限** · 换训练骨干或引导强度时的覆盖边界待核。

**可复用机制** · 比较显式推理引导与训练内引导，在固定采样成本下同时报告保真与覆盖。

<a id="paper-152139"></a>

## Diffusion Path Samplers via Sequential Monte Carlo

[官方论文页](https://neurips.cc/virtual/2026/poster/152139) · [作者来源](https://openreview.net/forum?id=VEHUg2tjj5)

- **问题 / 瓶颈** · 沿连续扩散路径求中间分数常缺少可用解析式。
- **核心创新 / 方法** · 传播条件辅助变量以估计时变密度与分数，并用控制变量降低方差。
- **Baseline** · OU 时间反演、随机插值及扩散退火 Langevin 路径比较。
- **Benchmark** · 合成和真实数据采样，具体误差指标待核。
- **关键结果 / 消融** · 作者提供理论保证和实证，量化结果待核。
- **适用条件 / 局限** · 依赖可评估未归一化目标，并承担粒子传播开销。

**可复用机制** · 为扩散采样器固定粒子预算，对照路径与控制变量日程的方差。

<a id="paper-153673"></a>

## Diffusion-State Policy Optimization for Masked Diffusion Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153673) · [作者来源](https://openreview.net/forum?id=Jd9XMjrCiK)

- **问题 / 瓶颈** · 只看最终奖励会模糊中间填充决策贡献。
- **核心创新 / 方法** · 从缓存 logits 重采样当前掩码并评分，用固定状态的分支目标估计梯度。
- **Baseline** · 终局反馈 diffu-GRPO 和 SPG。
- **Benchmark** · LLaDA-8B-Instruct 的数学与规划，匹配滚动成本和优化步数。
- **关键结果 / 消融** · 作者报告优于终局反馈对照，幅度待核。
- **适用条件 / 局限** · 依赖缓存分布与分支完成评分质量。

**可复用机制** · 在冻结相同 rollout 预算下比较终局信用与局部分支信用。

<a id="paper-150829"></a>

## Diffusion Subgoal Planning for Long-Horizon Offline Goal-Conditioned Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/150829) · [作者来源](https://openreview.net/forum?id=ezp2TvIFGP)

- **问题 / 瓶颈** · 长时域稀疏奖励和折扣使高层价值不稳。
- **核心创新 / 方法** · 学习条件和无条件流，用生成引导偏向最终目标，保留底层层级执行。
- **Baseline** · 离线目标条件强化学习方法，具名方法待核。
- **Benchmark** · 离线导航、操作与多步迷宫。
- **关键结果 / 消融** · 摘要报告多个任务超过对照，迷宫收益突出。
- **适用条件 / 局限** · 可达性受离线数据和执行层覆盖约束。

**可复用机制** · 高层价值噪声大时，在共同底层比较生成子目标和价值引导的规划成功率。

<a id="paper-150048"></a>

## Diffusion Thinking for Fast Long-Form Spatial Reasoning in Vision--Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150048) · [作者来源](https://openreview.net/forum?id=lBRcoVJDrO)

- **问题 / 瓶颈** · 逐 token 生成空间长推理延迟高，过度并行又损精度。
- **核心创新 / 方法** · 块内离散去噪、块间因果并复用 KV 缓存，以缓存复思重新分配推理预算。
- **Baseline** · 自回归长推理，Qwen2.5-VL 和 InternVL3 骨干。
- **Benchmark** · 56.1 万实例训练数据覆盖六种空间任务；比较端到端推理速度和准确率。
- **关键结果 / 消融** · 块尺寸 32 时报告 38.18–41.81 倍提速；八轮复思仍有 4.20–4.60 倍，在最大骨干精度持平或更优。
- **适用条件 / 局限** · 依赖长推理训练分布，速度受硬件与缓存影响。

**可复用机制** · 在固定墙钟预算下扫并行块尺寸与纠错轮数，联合画速度和正确率。

<a id="paper-154152"></a>

## Diffusion-Time Concept Manifolds: Sparse Autoencoder Groups for Interpreting Denoising Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154152) · [作者来源](https://openreview.net/forum?id=FrP1gSPL04)

- **问题 / 瓶颈** · 静态单特征分析无法解释揭开 token 的顺序。
- **核心创新 / 方法** · 在多个掩码率构造 SAE 特征组，测试时间持续性、几何一致性与干预。
- **Baseline** · 单特征、PCA、随机分组及图结构分组。
- **Benchmark** · BERT、LLaDA、控制模板和自然 SST-2，测情感几何与揭开置信。
- **关键结果 / 消融** · 组结构跨种子及数据设置较稳，干预效果超过匹配对照。
- **适用条件 / 局限** · 摘要主要验证情感概念。

**可复用机制** · 比较单特征和特征组的跨去噪阶段预测，再用匹配对照测试干预。

<a id="paper-151083"></a>

## Diffusion Transformers with Residual Adaptive Layer Normalization

[官方论文页](https://neurips.cc/virtual/2026/poster/151083) · [作者来源](https://openreview.net/forum?id=d682nArxGB)

- **问题 / 瓶颈** · PreNorm 深层块可能重复加工相似表征。
- **核心创新 / 方法** · 利用早层表示调节后层缩放、偏移与门控，并保持原有时间和类别条件。
- **Baseline** · SiT-XL/2 加 REG 或 REPA。
- **Benchmark** · ImageNet 256，测收敛与下游生成表现。
- **关键结果 / 消融** · 相对两对照报告最高约 2 倍和 36 倍的训练加速。
- **适用条件 / 局限** · 效果依赖骨干的条件归一化接口，比较的收敛门槛待核。

**可复用机制** · 需要提高深层区分度时，对照直接残差传输和经条件调制传输。

<a id="paper-151930"></a>

## Diffusion Tree Search for Inference Time Adaptation of Material Foundation Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151930) · [作者来源](https://openreview.net/forum?id=WlhX6hq6Jo)

- **问题 / 瓶颈** · 微调成本高且很多材料奖励不可微。
- **核心创新 / 方法** · 在去噪轨迹树搜索内使用重要性校正提案，并共享多目标搜索以覆盖不同偏好。
- **Baseline** · 预训练晶体扩散模型与条件引导版本。
- **Benchmark** · 晶体稳定性、稀有空间群和多目标 Pareto 质量。
- **关键结果 / 消融** · 作者报告不改底座即可改善稳定率和 Pareto 前沿。
- **适用条件 / 局限** · 依赖可计算的材料评价和足够搜索预算。

**可复用机制** · 在非生物材料设计中固定底座，对照逐目标采样和共享树搜索。

<a id="paper-155666"></a>

## Diffusion-warm sampling of the XY model enables fast thermalization at scale

[官方论文页](https://neurips.cc/virtual/2026/poster/155666) · [作者来源](https://openreview.net/forum?id=3vCVCEk7Px)

- **问题 / 瓶颈** · 随机初始化热化慢，系统扩大后代价上升。
- **核心创新 / 方法** · 训练温度条件扩散模型，再用少量 MCMC 步修正生成状态。
- **Baseline** · 随机初态标准 MCMC。
- **Benchmark** · 凝聚态 XY 模型，跨格点规模追踪自旋相关与热化时间。
- **关键结果 / 消融** · 作者报告热化时间降低约一个数量级。
- **适用条件 / 局限** · 主要验证连续对称 XY 模型，关键相区与跨模型边界待核。

**可复用机制** · 模拟中对照生成热启动与随机热启动，并以物理观测量而非外观定义热化。

<a id="paper-155419"></a>

## DIGS: Distribution-Informed Gaussian Splatting for Training-Free Open-Vocabulary 3D Segmentation

[官方论文页](https://neurips.cc/virtual/2026/poster/155419) · [作者来源](https://openreview.net/forum?id=5pWANdn0Cl)

- **问题 / 瓶颈** · 单特征赋值会抹掉跨多个实例的边界歧义。
- **核心创新 / 方法** · 每个高斯维护 top-M 标签分布，再聚合成类无关实例并融合视觉和文本编码。
- **Baseline** · 免训练 SFS 与训练型 LaGa。
- **Benchmark** · LERF-OVS、LERF-Mask、3D-OVS，另测建图及检索耗时。
- **关键结果 / 消融** · LERF-OVS 为 71.95% mIoU；单 A100 建图 1–3 分钟，检索 5.4 毫秒。
- **适用条件 / 局限** · 依赖多视角分割质量和 top-M 截断容量。

**可复用机制** · 推迟边界标签硬化，在相同压缩预算下比较单标签和多峰表示的边界误差。

<a id="paper-150062"></a>

## DiLaDiff: Distilled Latent-augmented Diffusion for Language Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/150062) · [作者来源](https://openreview.net/forum?id=l1EueDpKBW)

- **问题 / 瓶颈** · 逐位置扩散解码难捕捉输出 token 之间的关联。
- **核心创新 / 方法** · 先学连续语义潜空间及扩散先验，再蒸馏为少步一致性模型。
- **Baseline** · 标准掩码扩散和不蒸馏版本。
- **Benchmark** · 语言生成质量、推理吞吐和潜变量生成开销；任务待核。
- **关键结果 / 消融** · 作者报告未蒸馏即优于掩码对照，蒸馏进一步降低额外开销。
- **适用条件 / 局限** · 依赖潜变量语义质量及蒸馏后先验保真。

**可复用机制** · 在固定吞吐下比较共享潜变量与独立离散采样，再单独消融先验蒸馏。

<a id="paper-154617"></a>

## DiM$^3$: Bridging Multilingual and Multimodal Models via Direction- and Magnitude-Aware Merging

[官方论文页](https://neurips.cc/virtual/2026/poster/154617) · [作者来源](https://openreview.net/forum?id=CF3jmTcKdp)

- **问题 / 瓶颈** · 不同任务的残差作用不同，直接相加可能相互覆盖。
- **核心创新 / 方法** · 在共享语言骨干逐维组合残差，保留原视觉编码器和投影器。
- **Baseline** · 原多模态模型、现有合并方法及专门多语言多模态微调。
- **Benchmark** · LLaVA 和 Qwen 系列，57 种语言的文本和视觉语言基准。
- **关键结果 / 消融** · 摘要报告优于既有合并方法并基本保持通用多模态能力。
- **适用条件 / 局限** · 要求共享骨干与参数对齐；数值及低资源语言边界待核。

**可复用机制** · 评估模型合并时分开测新增能力和已有能力保持，并对照无筛选的直接叠加。

<a id="paper-155874"></a>

## Dimension Bounds for Contractive Reservoir Computing from Input Entropy

[官方论文页](https://neurips.cc/virtual/2026/poster/155874) · [作者来源](https://openreview.net/forum?id=2C39UZjQf8)

- **问题 / 瓶颈** · 回声状态唯一性不回答状态空间有多丰富。
- **核心创新 / 方法** · 把量化输入的收缩储备池写成迭代函数系统，对平稳测度推导熵与 Lyapunov 维数界。
- **Baseline** · 比较不同收缩强度及相似映射下的精确维数。
- **Benchmark** · 理论设定为独立同分布量化输入的收缩储备池。
- **关键结果 / 消融** · 在符合分离条件时维数由输入熵与收缩比例决定，给出全维表示的临界判据。
- **适用条件 / 局限** · 精确等式需要共形或相似条件；一般网络为界。

**可复用机制** · 调漏率或谱半径时同时测表示维数和稳定性，检验是否过度收缩。

<a id="paper-153363"></a>

## Dimension-Uniform Discretization Analysis of Preconditioned Annealed Langevin Dynamics for Multimodal Gaussian Mixtures

[官方论文页](https://neurips.cc/virtual/2026/poster/153363) · [作者来源](https://openreview.net/forum?id=LvzRfDwh4K)

- **问题 / 瓶颈** · Euler–Maruyama 稳定约束可能逼初始平滑分布接近目标。
- **核心创新 / 方法** · 用指数积分器处理刚性部分，按预条件和谱可和条件推导维度一致 KL 界。
- **Baseline** · Euler–Maruyama 离散。
- **Benchmark** · 多峰高斯混合的理论分析，以随维数增长的 KL 误差为准。
- **关键结果 / 消融** · 在指定谱条件下，即使初始 KL 随维数发散也可取得维度一致的小误差。
- **适用条件 / 局限** · 结论针对高斯混合及规定谱条件。

**可复用机制** · 高维扩展时先区分连续动力学与积分器的稳定限制，再比较隐式或精确处理刚性部分。

<a id="paper-155664"></a>

## DinoComplete: 3D Shape Completion with Distilled Semantic Priors and State Space Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155664) · [作者来源](https://openreview.net/forum?id=3w5XrsVWsn)

- **问题 / 瓶颈** · 未知类别和噪声扫描中纯几何难以补全
- **核心创新 / 方法** · 蒸馏多视角 DINO 体素特征，再用全局与分块状态空间层融合
- **Baseline** · 确定性与生成式形状补全
- **Benchmark** · ShapeNet 未见类别和 ScanNet 对象，比较补全质量与成本
- **关键结果 / 消融** · 作者报告质量、内存和速度均改善
- **适用条件 / 局限** · 依赖视觉语义与几何配准

**可复用机制** · 固定补全头，比较有无对齐语义蒸馏的跨类别表现

<a id="paper-156661"></a>

## DINOv3

[官方论文页](https://neurips.cc/virtual/2026/poster/156661) · [作者来源](https://neurips.cc/virtual/2026/poster/156661)

- **问题 / 瓶颈** · 长训练可能使空间特征质量退化
- **核心创新 / 方法** · 引入 Gram 锚定以约束密集表示，并另做分辨率和文本适配
- **Baseline** · 先前自监督与弱监督视觉骨干
- **Benchmark** · 冻结特征下的多种视觉任务，摘要未列具体指标
- **关键结果 / 消融** · 作者报告密集特征与下游表现改善
- **适用条件 / 局限** · 摘要无法分离锚定、数据和模型规模收益

**可复用机制** · 固定数据和步数，监控局部关系在长期训练中的变化

<a id="paper-148916"></a>

## DiPhon: Diffusion on Graphons for Scalable Graph Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/148916) · [作者来源](https://openreview.net/forum?id=uDmhLyLIAy)

- **问题 / 瓶颈** · 训练和生成图规模改变时图统计可能漂移
- **核心创新 / 方法** · 在图核空间用 Jacobi 扩散并离散到有限图，去噪估计反向分数
- **Baseline** · 常规固定尺度图扩散作为问题背景，具名基线待核
- **Benchmark** · 小图训练和更大稠密图生成
- **关键结果 / 消融** · 证明一阶矩精确匹配、二阶矩差异有闭式，作者报告可扩图生成
- **适用条件 / 局限** · 稠密图假设限制外推

**可复用机制** · 在纯图结构任务上先测尺度间矩再评估生成质量

<a id="paper-156633"></a>

## DiPMInd: Distance profile based mutual independence testing for random objects

[官方论文页](https://neurips.cc/virtual/2026/poster/156633) · [作者来源](https://neurips.cc/virtual/2026/poster/156633)

- **问题 / 瓶颈** · 随机对象可能不存在共享向量坐标
- **核心创新 / 方法** · 比较联合距离剖面和边缘乘积分布剖面，结合自适应权重与置换检验
- **Baseline** · 已有独立性检验，具名对照待核
- **Benchmark** · 理论极限、局部备择及实证功效
- **关键结果 / 消融** · 作者报告最小极大率最优性，部分权重下渐近无分布
- **适用条件 / 局限** · 需要可识别条件，部分结论要求边缘距离剖面连续

**可复用机制** · 为异构对象先确认度量和可识别性，再比较加权检验功效

<a id="paper-148861"></a>

## DiPO: Disentangled Perplexity Policy Optimization for Fine-grained Exploration-Exploitation Trade-Off

[官方论文页](https://neurips.cc/virtual/2026/poster/148861) · [作者来源](https://openreview.net/forum?id=udWtfeFJ7W)

- **问题 / 瓶颈** · 统一更新难兼顾过易和过难的样本
- **核心创新 / 方法** · 分离高低困惑度子空间并双向分配奖励，尽量少改验证奖励
- **Baseline** · 一般 RLVR，具名基线待核
- **Benchmark** · 数学推理和函数调用
- **关键结果 / 消融** · 作者报告两类任务均改善，幅度待核
- **适用条件 / 局限** · 困惑度未必等于学习难度或样本价值

**可复用机制** · 分别追踪两类样本的验证通过率，对照仅用验证奖励

<a id="paper-148348"></a>

## DiReCL: Learning Differentiable Reward Code with Inverse Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/148348) · [作者来源](https://openreview.net/forum?id=yXtaGQVE33)

- **问题 / 瓶颈** · 神经奖励不易检查，手写代码难校准
- **核心创新 / 方法** · 把代码模板数值转为可微参数做逆强化学习，再用诊断修订模板
- **Baseline** · 标准逆强化学习和语言模型辅助奖励设计
- **Benchmark** · MuJoCo 运动和自动驾驶任务
- **关键结果 / 消融** · 作者报告性能超过所比基线的 1.25 倍
- **适用条件 / 局限** · 依赖示范和可微模板，摘要未拆分两类更新增益

**可复用机制** · 先固定可审查结构做参数校准，仅在残差持续时再调整结构

<a id="paper-153100"></a>

## Direct Acceleration of Stochastic Root-Finding Without Variance Reduction and Regularization

[官方论文页](https://neurips.cc/virtual/2026/poster/153100) · [作者来源](https://openreview.net/forum?id=NwFLuTS4h3)

- **问题 / 瓶颈** · 常规锚点加速可能积累随机误差
- **核心创新 / 方法** · 采用双锚点机制，无需方差缩减或双循环正则化
- **Baseline** · Halpern 型方法与已知复杂度界
- **Benchmark** · 随机求根与不动点的理论分析
- **关键结果 / 消融** · 一般适用设定复杂度为误差的负三次方，强单调时接近负二次方
- **适用条件 / 局限** · 依赖期望余强单调或平方非扩张等条件

**可复用机制** · 先确认算子条件，再按固定批量预算比较随机加速策略

<a id="paper-155500"></a>

## Direct Conditional Parameterization for N-Dimensional Splatting

[官方论文页](https://neurips.cc/virtual/2026/poster/155500) · [作者来源](https://openreview.net/forum?id=57CdXoL0gj)

- **问题 / 瓶颈** · 逐图元条件切片重复求逆和矩阵乘法
- **核心创新 / 方法** · 分别参数化透明度精度因子及位置位移，应用于高斯和 Beta 核
- **Baseline** · N-DGS 和 UBS
- **Benchmark** · 五个静态与动态基准，测质量和切片速度
- **关键结果 / 消融** · 切片加速 6.9–7.7 倍，主 MCMC 设置质量最多提高 1.26 dB
- **适用条件 / 局限** · 不同条件维度或场景的端到端收益待核

**可复用机制** · 将推理反复从联合参数推导的属性改为直接学习，并分别测质量与阶段耗时

<a id="paper-152995"></a>

## Direct Conditioning of Audio Diffusion Transformers on fMRI Reveals Cortical Contributions to Sound Reconstruction

[官方论文页](https://neurips.cc/virtual/2026/poster/152995) · [作者来源](https://openreview.net/forum?id=OlCa72ym7P)

- **问题 / 瓶颈** · 音频扩散常以文本为条件，中间预测可能丢失信息
- **核心创新 / 方法** · 用适配器将连续观测输入扩散 Transformer 的交叉注意力
- **Baseline** · 两阶段 fMRI 到潜变量方案
- **Benchmark** · 音频重建，含声学、语义和听觉模型保真指标
- **关键结果 / 消融** · 作者报告多项指标较基线改善
- **适用条件 / 局限** · 仅验证所测脑信号条件，任意连续输入的有效性未证实

**可复用机制** · 固定生成骨干，对比直接连续条件和先预测中间特征

<a id="paper-155581"></a>

## Direct Estimation of Schrödinger Bridge Time-Series Drifts: Finite-Sample, Asymptotic, and Adaptive Guarantees

[官方论文页](https://neurips.cc/virtual/2026/poster/155581) · [作者来源](https://openreview.net/forum?id=4Z2NRZV5nH)

- **问题 / 瓶颈** · 迭代桥求解会混入优化、逼近和离散化误差
- **核心创新 / 方法** · 对条件比率的分子分母做核回归，选择自适应带宽
- **Baseline** · 势函数与迭代桥求解为分析背景
- **Benchmark** · 理论界与合成数据，测有限样本尺度和高斯近似
- **关键结果 / 消融** · 给出有限样本界、点态中心极限定理和近最小极大自适应率
- **适用条件 / 局限** · 要求 Hölder 正则、密度下界与有界支持等条件

**可复用机制** · 单独评估漂移估计的方差和偏差，再引入桥求解器

<a id="paper-152629"></a>

## Directional Confusions Reveal Divergent Inductive Biases Through Rate-Distortion Geometry in Human and Machine Vision

[官方论文页](https://neurips.cc/virtual/2026/poster/152629) · [作者来源](https://openreview.net/forum?id=Rg5nL1oYDA)

- **问题 / 瓶颈** · 相同准确率可能掩盖模型和人不同的混淆模式
- **核心创新 / 方法** · 从混淆矩阵测方向不对称，结合率失真前沿的斜率、曲率与面积
- **Baseline** · 人类、深度视觉模型以及稳健训练变体
- **Benchmark** · 自然图像分类的十二类扰动和匹配表现的仿真
- **关键结果 / 消融** · 人类混淆广而弱，模型稀疏而强；稳健训练未复现人类模式
- **适用条件 / 局限** · 结果来自所测类别及扰动

**可复用机制** · 报告成对混淆方向并控制准确率，检查稳健性是否改变错误结构

<a id="paper-150199"></a>

## Directional Noise Conditioning for Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150199) · [作者来源](https://openreview.net/forum?id=jzTnuYTSXT)

- **问题 / 瓶颈** · 逐步去噪可能削弱指定属性的条件控制
- **核心创新 / 方法** · 对不同属性学习潜空间噪声偏移并联合优化偏移精度和去噪
- **Baseline** · 时间步嵌入与交叉注意力条件方案
- **Benchmark** · 图像离散及连续属性控制与反事实生成
- **关键结果 / 消融** · 作者报告属性控制更精确，定量幅度待核
- **适用条件 / 局限** · 方向可分性和无标签潜变量语义需要验证

**可复用机制** · 不改生成主干时可比较输入噪声偏移和层内条件化的属性保持

<a id="paper-148256"></a>

## Direction-Aware Offline-to-Online Learning in Linear Contextual Bandits

[官方论文页](https://neurips.cc/virtual/2026/poster/148256) · [作者来源](https://openreview.net/forum?id=zCquLHIOxw)

- **问题 / 瓶颈** · 欧氏偏差界无法区分方向性分布偏移
- **核心创新 / 方法** · 用椭球偏差证书控制历史数据分支，证书未知时在线估计
- **Baseline** · 标准 SupLinUCB
- **Benchmark** · 线性上下文赌博机理论与数值实验，测遗憾
- **关键结果 / 消融** · 最坏情形可匹配基线，覆盖与低偏差方向重合时改善
- **适用条件 / 局限** · 理论依赖线性模型与证书估计条件

**可复用机制** · 将历史覆盖和偏差按特征方向联合审计

<a id="paper-149331"></a>

## Direct Product Flow Matching: Decoupling Radial and Angular Dynamics for Few-Shot Adaptation

[官方论文页](https://neurips.cc/virtual/2026/poster/149331) · [作者来源](https://openreview.net/forum?id=qtVzcDdIqD)

- **问题 / 瓶颈** · 归一化丢失范数信号，径向角向耦合影响拟合
- **核心创新 / 方法** · 将跨模态流写成乘积流形并用常数度量解耦半径与角度
- **Baseline** · 以既有流匹配少样本适配为对照
- **Benchmark** · 预训练视觉语言模型的少样本适配
- **关键结果 / 消融** · 作者提出并验证几何解耦，具体幅度待核
- **适用条件 / 局限** · 范数含有可靠信号的前提须检验

**可复用机制** · 比较全归一化与保留范数的对齐，并分别报告分布内外结果

<a id="paper-155798"></a>

## DiRecT: Safe Diffusion-Based Planning via Receding-Horizon Denoising

[官方论文页](https://neurips.cc/virtual/2026/poster/155798) · [作者来源](https://openreview.net/forum?id=2nsFEzrTEf)

- **问题 / 瓶颈** · 每步投影噪声中间态会过度约束并破坏采样
- **核心创新 / 方法** · 以滚动时域近似分开随机去噪与最终约束求解
- **Baseline** · 每步可行集投影
- **Benchmark** · 约束轨迹采样，比较可行性与采样质量
- **关键结果 / 消融** · 作者报告可在保留扩散质量下引导终态，幅度待核
- **适用条件 / 局限** · 依赖可用约束优化器与可达的终态

**可复用机制** · 约束定义于最终样本时，对照中间投影和终态约束

<a id="paper-153147"></a>

## DirectUV: Image-Conditioned UV Texture Generation with Surface-Aware Positional Encoding

[官方论文页](https://neurips.cc/virtual/2026/poster/153147) · [作者来源](https://openreview.net/forum?id=NWZOrQHECk)

- **问题 / 瓶颈** · UV 岛和接缝会把相邻表面点分隔
- **核心创新 / 方法** · 把潜空间图块映射到三维坐标，按注意力头分配不同表面细分粒度
- **Baseline** · 多视图投影和现有直接 UV 生成
- **Benchmark** · 单图条件的三维网格纹理，考察清晰度和全局一致性
- **关键结果 / 消融** · 作者报告接缝一致性和纹理质量提高，数值待核
- **适用条件 / 局限** · 需可用的 UV 与表面对应

**可复用机制** · 固定纹理主干比较 UV 格点位置与物理表面位置

<a id="paper-154424"></a>

## Dirichlet-Guided Group Forecasting for Alleviating Over-smoothing in Time Series Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/154424) · [作者来源](https://openreview.net/forum?id=DgOd19LuBJ)

- **问题 / 瓶颈** · 单次实现监督容易平均多种未来，削弱尖峰和转折
- **核心创新 / 方法** · 用 Dirichlet 层级采样和奖励优化区分多个预测分布
- **Baseline** · 常规时序预测，具名基线待核
- **Benchmark** · 真实时序数据，评估准确性、多样性和动力学一致性
- **关键结果 / 消融** · 作者报告过度平滑降低且多项指标改善
- **适用条件 / 局限** · 模式数和分布选择可能影响校准

**可复用机制** · 在多解序列上测尖峰与转折，与点预测误差分开汇报

<a id="paper-155781"></a>

## DiRotQ: Rotation-Aware Quantization for 4-bit Diffusion Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/155781) · [作者来源](https://openreview.net/forum?id=2vvKmRgMuy)

- **问题 / 瓶颈** · DiT 激活全量四比特会损伤生成质量
- **核心创新 / 方法** · PCA 旋转激活，保留主子空间精度，将逆旋转并入权重并配合 GPTQ
- **Baseline** · SVDQuant，与半精度为参考
- **Benchmark** · PixArt 在 MJHQ-30K 的 FID 和 PSNR
- **关键结果 / 消融** · FID 15.9 对 18.9，PSNR 19.1 对 17.6 dB
- **适用条件 / 局限** · 校准分布和额外高精度成本需对齐

**可复用机制** · 固定有效算力，比较按方差保留与均匀低精度

<a id="paper-152518"></a>

## Disambiguating 2D-3D Correspondences in Gaussian Splatting-based Feature Fields for Visual Localization

[官方论文页](https://neurips.cc/virtual/2026/poster/152518) · [作者来源](https://openreview.net/forum?id=SWuCpRLccL)

- **问题 / 瓶颈** · 大高斯的多对一投影会使 PnP 不稳定
- **核心创新 / 方法** · 用混合高斯细分图元，再根据多视角渲染贡献筛选并聚合特征
- **Baseline** · 光度训练的高斯场定位
- **Benchmark** · 视觉定位基准，检查位姿与 PnP 收敛
- **关键结果 / 消融** · 作者报告定位改善，无需逐场景训练或迭代精修
- **适用条件 / 局限** · 依赖视角覆盖和稳定的跨视角渲染权重

**可复用机制** · 将定位用图元筛选与渲染质量分开优化，测匹配歧义

<a id="paper-138947"></a>

## DIS-Bench: Evaluating LLMs on System Testing via Directed Input Synthesis

[官方论文页](https://neurips.cc/virtual/2026/poster/138947) · [作者来源](https://openreview.net/forum?id=uZfKjYti0g)

- **问题 / 瓶颈** · 单测生成不足以覆盖仓库级系统行为
- **核心创新 / 方法** · 从程序执行选择具有挑战的可达分支，构建系统测试任务
- **Baseline** · BM25 检索和 OpenHands 等编码代理
- **Benchmark** · 37 个仓库 8267 项任务，DIS-Bench-Lite 报 pass@1
- **关键结果 / 消融** · 最佳开权配置 28.1%，最佳前沿配置 57.8%
- **适用条件 / 局限** · 衡量覆盖指定分支，不等于发现或修复缺陷

**可复用机制** · 对授权项目的正常系统测试，将分支覆盖和行为断言分别评估

<a id="paper-155886"></a>

## DiscoLoop: Looping Discrete Embeddings and Continuous Hidden States for Multi-hop Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/155886) · [作者来源](https://openreview.net/forum?id=26R1JkrIyI)

- **问题 / 瓶颈** · 连续状态和干净词嵌入几何失配
- **核心创新 / 方法** · 递归同时传递离散嵌入与连续状态
- **Baseline** · 循环 Transformer
- **Benchmark** · 符号与合成语言多跳、实际预训练
- **关键结果 / 消融** · 无训练对齐近乎消除 OOD 差距；混合通道提高两跳学习效率
- **适用条件 / 局限** · 多跳深度外推待核

**可复用机制** · 先做中间状态对齐干预，再决定是否增加离散通道

<a id="paper-153999"></a>

## DisCoMBO: Steering Expert-in-the-Loop Black Box Optimization via Distributional Conformance

[官方论文页](https://neurips.cc/virtual/2026/poster/153999) · [作者来源](https://openreview.net/forum?id=Gy6WP1zaMc)

- **问题 / 瓶颈** · 采集权重难透明表达专家知识
- **核心创新 / 方法** · 用概率电路和归一化惊讶分数度量一致性
- **Baseline** · 传统采集重加权及核不确定性
- **Benchmark** · AutoML、材料和风场优化
- **关键结果 / 消融** · 作者给出无遗憾保证并报告跨任务有效
- **适用条件 / 局限** · 理论条件及对照幅度待核

**可复用机制** · 把先验可信度和探索奖励分开测量

<a id="paper-149717"></a>

## Discovering Mechanistic Models of Neural Activity: System Identification in an in Silico Zebrafish

[官方论文页](https://neurips.cc/virtual/2026/poster/149717) · [作者来源](https://openreview.net/forum?id=nwvvEjN12N)

- **问题 / 瓶颈** · 域内准确率可能奖励捷径
- **核心创新 / 方法** · 用已知模拟真值比较预测和结构恢复，并加入结构先验
- **Baseline** · 既有预测方法及无结构先验对照
- **Benchmark** · 仿真神经活动的域内和域外验证
- **关键结果 / 消融** · 作者报告预测改善，但结构约束对恢复关键
- **适用条件 / 局限** · 证据来自模拟真值

**可复用机制** · 机制发现应独立验收结构和预测误差

<a id="paper-148569"></a>

## Discovering Phase Space Structure in Learned Hamiltonian Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/148569) · [作者来源](https://openreview.net/forum?id=wstD80hIpm)

- **问题 / 瓶颈** · 已知构型假设限制原始观测建模
- **核心创新 / 方法** · 端口哈密顿骨干结合条件生成及循环坐标损失
- **Baseline** · 监督动力学及生成基线
- **Benchmark** · 仿真和真实轨迹及视频
- **关键结果 / 消融** · 作者报告轨迹与视频改善并恢复机械坐标
- **适用条件 / 局限** · 可辨识条件待核

**可复用机制** · 把坐标恢复作为独立评测

<a id="paper-148335"></a>

## Discovering Programmatic Policies from Reinforcement Learning-Based Traffic Signal Controllers

[官方论文页](https://neurips.cc/virtual/2026/poster/148335) · [作者来源](https://openreview.net/forum?id=ybRA9BTKJ8)

- **问题 / 瓶颈** · 深度交通控制器复杂且难迁移
- **核心创新 / 方法** · 语言模型提出函数，经合法性审查、教师行为校准和任务打分
- **Baseline** · 交通深度强化学习教师
- **Benchmark** · 多种交通场景和教师
- **关键结果 / 消融** · 作者报告匹配教师表现并改善迁移与计算成本
- **适用条件 / 局限** · 跨城市和实际部署待核

**可复用机制** · 蒸馏时同时检查程序合法性、行为保真和任务结果

<a id="paper-150060"></a>

## Discovering Structurally Plausible and Interpretable Cognitive Models with Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150060) · [作者来源](https://openreview.net/forum?id=l2Zr7y18C6)

- **问题 / 瓶颈** · 预测拟合可掩盖结构无效
- **核心创新 / 方法** · 演化搜索加入结构验证和冗余参数清理
- **Baseline** · 任务专用模型及去除验证器对照
- **Benchmark** · 三项人类行为任务
- **关键结果 / 消融** · 无验证器更易违反行为约束
- **适用条件 / 局限** · 约束质量依赖领域知识

**可复用机制** · 分别审核预测、结构有效性和参数冗余

<a id="paper-156742"></a>

## Discovering Symbolic Differential Equations with Symmetry Invariants

[官方论文页](https://neurips.cc/virtual/2026/poster/156742) · [作者来源](https://openreview.net/forum?id=9t1dEyYfPc)

- **问题 / 瓶颈** · 通用搜索会产生违反物理的方程
- **核心创新 / 方法** · 用微分不变量作原子项供稀疏回归或遗传搜索
- **Baseline** · 原有回归与遗传搜索
- **Benchmark** · Darcy 流及反应扩散
- **关键结果 / 消融** · 作者报告恢复简洁且满足对称性的方程
- **适用条件 / 局限** · 需要正确指定对称群

**可复用机制** · 已知不变量时先限制候选字典再搜索

<a id="paper-148895"></a>

## Discovering Unseen Degradations to Adapt Open-World Image Restoration

[官方论文页](https://neurips.cc/virtual/2026/poster/148895) · [作者来源](https://openreview.net/forum?id=uOrhK38Kpk)

- **问题 / 瓶颈** · 固定评分难适应未知混合退化
- **核心创新 / 方法** · 持续发现退化，用类别与实例条件描述，并以特征距离筛伪目标
- **Baseline** · 现有恢复方法
- **Benchmark** · 开放世界协议及真实恶劣天气
- **关键结果 / 消融** · 作者报告多项画质指标和组合稳健性改善
- **适用条件 / 局限** · 类别发现错误可能传递

**可复用机制** · 分开测试未知退化发现和伪目标可靠性

<a id="paper-154140"></a>

## Discovering What You Can Control: Interventional Boundary Discovery for Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/154140) · [作者来源](https://openreview.net/forum?id=Fwbd26L5dC)

- **问题 / 瓶颈** · 观测相关性无法识别可控维度
- **核心创新 / 方法** · 逐维做两样本干预比较并校正错误发现率
- **Baseline** · 互信息、前向模型、敏感性及全观测 SAC
- **Benchmark** · 12 个连续控制设置，至多 100 个干扰量
- **关键结果 / 消融** · 11 个设置匹配 oracle 回报
- **适用条件 / 局限** · 需要可安全随机化的动作

**可复用机制** · 对观察筛选增加动作干预对照

<a id="paper-155862"></a>

## DISCOVER: Online Variance-Guided Data Discovery for Budgeted Multimodal GRPO

[官方论文页](https://neurips.cc/virtual/2026/poster/155862) · [作者来源](https://openreview.net/forum?id=2MTnzpkl7i)

- **问题 / 瓶颈** · 均匀 rollout 浪费在低学习价值提示上
- **核心创新 / 方法** · 语义代表样本向未标注样本传递奖励证据，并按时间更新
- **Baseline** · 预算匹配随机、难样本、全池及在线选择
- **Benchmark** · ViRL39K、VLAA-Thinking 与 Qwen3-VL-2B
- **关键结果 / 消融** · 作者报告 10% 独特样本预算下胜过对照
- **适用条件 / 局限** · 依赖可验证奖励与语义近邻

**可复用机制** · 固定预算评估在线更新比静态难度筛选的收益

<a id="paper-139006"></a>

## DiscoverPhysics: Benchmarking LLMs for out-of-the-box scientific thinking

[官方论文页](https://neurips.cc/virtual/2026/poster/139006) · [作者来源](https://openreview.net/forum?id=r7QnwP79SC)

- **问题 / 瓶颈** · 熟悉的科学题可能只测记忆
- **核心创新 / 方法** · 在不同规律的模拟世界中让模型设计实验并提交解释和实现
- **Baseline** · 十种前沿模型
- **Benchmark** · 11 个模拟世界，留出轨迹 MSE 及解释评分
- **关键结果 / 消融** · 最强模型仅通过约半数；预测好不保证解释好
- **适用条件 / 局限** · 解释有模型评判环节

**可复用机制** · 把可证伪实验与最终预测分开验收

<a id="paper-151112"></a>

## Discrete Diffusion Models Exploit Asymmetry to Solve Lookahead Planning Tasks

[官方论文页](https://neurips.cc/virtual/2026/poster/151112) · [作者来源](https://openreview.net/forum?id=ctX2gxgiSE)

- **问题 / 瓶颈** · 扩散可能利用反向路径容易这一捷径
- **核心创新 / 方法** · 用图遍历对照自回归与非自回归的学习及解码
- **Baseline** · 自回归与非自回归模型
- **Benchmark** · 有分叉的前瞻图规划与潜表示分析
- **关键结果 / 消融** · 作者发现逆向确定路径将高阶前瞻化成一步转移
- **适用条件 / 局限** · 是否适用于对称难度图待核

**可复用机制** · 构造正反均难的对照再判断规划优势

<a id="paper-139528"></a>

## Discrete Diffusion Playground: A 2D Benchmark for Discrete Generative Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139528) · [作者来源](https://openreview.net/forum?id=KUMYilHjV5)

- **问题 / 瓶颈** · 代理指标可能漏掉真实几何错配
- **核心创新 / 方法** · 把二维已知分布双射编码为二进制序列再反解
- **Baseline** · 自回归与掩码扩散；反向和交错顺序
- **Benchmark** · 高斯混合、倾斜棋盘格、网格散度和 Wasserstein 距离
- **关键结果 / 消融** · 扩散在倾斜棋盘格大多失败；自回归保留几何
- **适用条件 / 局限** · 二维诊断无法替代高维测试

**可复用机制** · 在已知真分布上检查边界和支撑覆盖

<a id="paper-154408"></a>

## Discrete Flow Matching: Convergence Guarantees Under Minimal Assumptions

[官方论文页](https://neurips.cc/virtual/2026/poster/154408) · [作者来源](https://openreview.net/forum?id=DnD9EjVFG3)

- **问题 / 瓶颈** · 离散流匹配的有限步误差保证不足
- **核心创新 / 方法** · 在生成器近似误差假设下分析两种时间离散模型
- **Baseline** · 依赖较强分数假设的早期理论
- **Benchmark** · 有限离散网格上的 KL 和总变差
- **关键结果 / 消融** · 得到早停目标 KL 界与完整目标 TV 界
- **适用条件 / 局限** · 适用范围限所分析模型与误差假设

**可复用机制** · 报告界时明确目标分布和离散预算

<a id="paper-154362"></a>

## Discrete Langevin-Inspired Posterior Sampling

[官方论文页](https://neurips.cc/virtual/2026/poster/154362) · [作者来源](https://openreview.net/forum?id=E9UMLvG2aa)

- **问题 / 瓶颈** · 连续松弛和逐坐标更新限制通用性
- **核心创新 / 方法** · 在离散扩散先验下并行选择梯度引导的 token 更新
- **Baseline** · 离散后验采样器与连续扩散求解器
- **Benchmark** · MNIST、CIFAR、FFHQ 及空间映射
- **关键结果 / 消融** · 作者报告比离散对照好并与连续对照有竞争力
- **适用条件 / 局限** · 依赖任务可用的梯度线索

**可复用机制** · 比较直接离散更新与连续松弛的质量和成本

<a id="paper-151383"></a>

## Discrete Neural Interlingua for Ontology-Agnostic EHR Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/151383) · [作者来源](https://openreview.net/forum?id=b1dCEA7ccn)

- **问题 / 瓶颈** · 不同编码和同义词会形成不相关符号
- **核心创新 / 方法** · 以同义配对及共现关系训练向量量化词表
- **Baseline** · 固定本体词表及现有事件表示
- **Benchmark** · MIMIC-III 20 项任务和 eICU 14 项零样本任务，平均 AUPRC
- **关键结果 / 消融** · 作者报告分别提高 4.0% 和 8.8%
- **适用条件 / 局限** · 编码歧义与临床外推待核

**可复用机制** · 跨库迁移时独立评估概念对齐和预测性能

<a id="paper-153666"></a>

## Discrete Stochastic Localization for Non-autoregressive Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/153666) · [作者来源](https://openreview.net/forum?id=Jf5a5Sqnz8)

- **问题 / 瓶颈** · 依赖时间步的去噪器限制推理路径切换
- **核心创新 / 方法** · 以单位球嵌入构造名义 SNR 不变的去噪器
- **Baseline** · 掩码离散扩散及预训练 MDLM
- **Benchmark** · OpenWebText 的 MAUVE 和 Text8 的 NLL
- **关键结果 / 消融** · 作者报告多步预算提升，同检查点支持低至 48 步混合采样
- **适用条件 / 局限** · 其他离散任务上的表现待核

**可复用机制** · 固定模型权重比较不同采样路径

<a id="paper-149547"></a>

## Discretizing Continuous Time Series for Imputation with Masked Diffusion Training

[官方论文页](https://neurips.cc/virtual/2026/poster/149547) · [作者来源](https://openreview.net/forum?id=pKTszDf7fn)

- **问题 / 瓶颈** · 连续扩散的噪声目标与补全目标不一致
- **核心创新 / 方法** · 为有效值随机序数量化，掩码独立，训练直接补全原信号
- **Baseline** · 确定性和生成式补全方法
- **Benchmark** · 多种时间序列基准与缺失模式
- **关键结果 / 消融** · 作者报告稳健性和扩展性改善
- **适用条件 / 局限** · 数据集细节及离散化误差待核

**可复用机制** · 将缺失编码和预测目标分别做消融

<a id="paper-148214"></a>

## Discriminative Score Function: Turning Pretrained Models into Functional Generative Priors

[官方论文页](https://neurips.cc/virtual/2026/poster/148214) · [作者来源](https://openreview.net/forum?id=zWDlC6eCkN)

- **问题 / 瓶颈** · 缺少真实校准图像时难保留特征几何
- **核心创新 / 方法** · 从预训练判别模型损失梯度提取图像更新方向
- **Baseline** · 无数据量化校准方法
- **Benchmark** · ResNet、DETR、DINOv2 上的图像生成与量化
- **关键结果 / 消融** · 作者报告校准更好保留特征几何
- **适用条件 / 局限** · 生成质量与骨干的关系待核

**可复用机制** · 把校准样本的特征保真与视觉质量分开评估

<a id="paper-148543"></a>

## Disen-Forcing: Disentangling Semantic Anchoring from Motion for Autoregressive Video Diffusion

[官方论文页](https://neurips.cc/virtual/2026/poster/148543) · [作者来源](https://openreview.net/forum?id=x6iaZeSlAJ)

- **问题 / 瓶颈** · 全头共享首帧缓存会导致蒸馏后的长视频运动塌缩。
- **核心创新 / 方法** · 蒸馏中分离首帧语义与局部动态的上下文路由，并加入运动解耦正则。
- **Baseline** · 基础自回归视频扩散及全头首帧缓存。
- **Benchmark** · 长时视频生成，考察语义和运动；具名指标待核。
- **关键结果 / 消融** · 作者报告一致性与运动同时改善，幅度待核。
- **适用条件 / 局限** · 依赖注意力头分工及可用的蒸馏过程。

**可复用机制** · 对照每头接入首帧和选择性接入，分开报告语义漂移与运动幅度。

<a id="paper-153847"></a>

## Disentangled Multimodal Learning for Scalable Dynamic IR-Drop Analysis

[官方论文页](https://neurips.cc/virtual/2026/poster/153847) · [作者来源](https://openreview.net/forum?id=IImqhmEtiG)

- **问题 / 瓶颈** · 芯片瞬态压降仿真受空间复杂度和长时间测试共同制约。
- **核心创新 / 方法** · LWFusor 用物理对齐学习将活动序列投影到空间电势域。
- **Baseline** · 物理仿真与学习代理，具名设置待核。
- **Benchmark** · 工业规模芯片，考察热点捕获和推理耗时。
- **关键结果 / 消融** · 作者报告数量级加速并保持热点保真。
- **适用条件 / 局限** · 未见工艺和负载下的签核误差待核。

**可复用机制** · 面对静态结构和动态输入，预编码静态结构并与逐时步求解比较。

<a id="paper-151286"></a>

## Disentangled Representation Learning via Flow Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/151286) · [作者来源](https://openreview.net/forum?id=bXNMPTOJ05)

- **问题 / 瓶颈** · 仅依赖扩散结构的独立性偏好难确保因子语义对齐。
- **核心创新 / 方法** · 在紧凑潜空间建立因子条件流，用非重叠正则抑制串扰。
- **Baseline** · 代表性解耦方法，具名基线待核。
- **Benchmark** · 多数据集评测解耦分数、可控性和生成保真。
- **关键结果 / 消融** · 作者报告三方面改善，具体数值待核。
- **适用条件 / 局限** · 依赖因子条件的定义与可用性。

**可复用机制** · 干预单个因子时同时测目标效果及其他属性变化。

<a id="paper-155474"></a>

## Disentangled Sparse Representations for Concept-Separated Diffusion Unlearning

[官方论文页](https://neurips.cc/virtual/2026/poster/155474) · [作者来源](https://openreview.net/forum?id=5Ls4MY5nvC)

- **问题 / 瓶颈** · 只优化稀疏重建可能让多个概念共享原子。
- **核心创新 / 方法** · SAEParate 用概念对比损失聚类潜特征，编码器引入 GeLU 变换。
- **Baseline** · 稀疏自编码器概念遗忘及其他对照，细节待核。
- **Benchmark** · UnlearnCanvas，含风格与物体联合遗忘。
- **关键结果 / 消融** · 作者报告联合遗忘提升尤为明显。
- **适用条件 / 局限** · 依赖足以区分目标的概念样本。

**可复用机制** · 以目标抑制和邻近概念保持指标联合选择遗忘表示。

<a id="paper-155738"></a>

## Disentanglement as Identifiable Pushforward Factorisation

[官方论文页](https://neurips.cc/virtual/2026/poster/155738) · [作者来源](https://openreview.net/forum?id=3Kq1axaXfK)

- **问题 / 瓶颈** · 独立潜先验无法单独保证生成流形的可分解性。
- **核心创新 / 方法** · 用生成雅可比 SVD 刻画推前密度的一维分解，给出可识别条件。
- **Baseline** · 一般光滑生成模型与对角后验高斯 β-VAE 的理论比较。
- **Benchmark** · 高斯数据、dSprites、CelebA 的机制验证。
- **关键结果 / 消融** · 在给定条件下可识别到置换和符号，作者解释 β 如何调节解耦。
- **适用条件 / 局限** · 结论依赖光滑性和论文列出的生成器条件。

**可复用机制** · 比较潜变量独立性的同时检查生成空间中的局部几何。

<a id="paper-155723"></a>

## Disentangling Continuous-Time Latent Dynamics: Identifiability of Latent SDEs via Diffusion Shifts

[官方论文页](https://neurips.cc/virtual/2026/poster/155723) · [作者来源](https://openreview.net/forum?id=3PMnq8eP55)

- **问题 / 瓶颈** · 未知非线性观测下，单一扩散环境难区分潜动态坐标。
- **核心创新 / 方法** · 用漂移共享、扩散协方差不同的两个环境导出识别，并构造两阶段估计器。
- **Baseline** · 线性 OU 与一般加性噪声 SDE 理论对照。
- **Benchmark** · 合成系统及 Hardanger Bridge 传感监测数据。
- **关键结果 / 消融** · 方差比逐坐标互异时识别到置换和缩放；瞬时漂移图在平滑条件下亦可识别。
- **适用条件 / 局限** · 需要加性噪声、对角扩散和共享漂移。

**可复用机制** · 设计多环境采集时分别测噪声变化和漂移稳定性，检验识别前提。

<a id="paper-150058"></a>

## Disentangling Dual Image References in Frequency Aware Diffusion Models for Personalized Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/150058) · [作者来源](https://openreview.net/forum?id=l5xRQDiYkv)

- **问题 / 瓶颈** · 直接混合参考会使早期强频带压制文本或误传结构。
- **核心创新 / 方法** · Dual-FDM 在频域替换中低频段，以频带信息熵比调节去噪阶段。
- **Baseline** · 个性化扩散生成方法，具体具名模型待核。
- **Benchmark** · 双参考个性化生成与色彩风格迁移。
- **关键结果 / 消融** · 作者报告优于对照，量化与独立消融待核。
- **适用条件 / 局限** · 依赖频带和视觉属性之间的近似对应。

**可复用机制** · 以固定提示对照全频段融合与分频融合，并分开测颜色、结构与提示对齐。

<a id="paper-153573"></a>

## Disentangling generalization and memorization in large language models using chess

[官方论文页](https://neurips.cc/virtual/2026/poster/153573) · [作者来源](https://openreview.net/forum?id=KOZDunh4vu)

- **问题 / 瓶颈** · 总体得分难区分熟悉案例召回和新状态推理。
- **核心创新 / 方法** · 构造国际象棋局面先验密度分层，用棋引擎评价。
- **Baseline** · GPT 系列、Claude Opus、Gemini 及随机走棋。
- **Benchmark** · 从常见到罕见棋局，比较棋力和推理每 token 收益。
- **关键结果 / 消融** · 稀疏先验时基础模型退回随机基线附近，推理边际收益也下降。
- **适用条件 / 局限** · 国际象棋局面先验是代理，无法直接确定训练集暴露。

**可复用机制** · 按可得先验分层报告性能与推理预算收益。

<a id="paper-155780"></a>

## Disentangling Homophilic and Heterophilic Patterns for Multi-Domain Graph Foundation Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155780) · [作者来源](https://openreview.net/forum?id=2w0Bbk6akp)

- **问题 / 瓶颈** · 统一表征可能混合不同连接模式；硬切图损失边。
- **核心创新 / 方法** · 为每个邻居估计两类软边权，并用低通与高通双骨干分别对齐。
- **Baseline** · 共享单域不变表示及硬划分路线；具名对照待核。
- **Benchmark** · 多域图数据集与下游泛化。
- **关键结果 / 消融** · 作者报告实验支持方法，幅度待核。
- **适用条件 / 局限** · 软边权误差及额外双路成本待核。

**可复用机制** · 图移植时比较软边分工和硬分区对跨群边与下游准确度的影响。

<a id="paper-154249"></a>

## Disentangling Optimization Geometry via Hierarchical Polar Adapters for Class-Incremental Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/154249) · [作者来源](https://openreview.net/forum?id=FBAriogGVS)

- **问题 / 瓶颈** · 单组笛卡尔权重同时改动旧特征强度和方向，容易遗忘。
- **核心创新 / 方法** · HiPo 在傅里叶表示中构造极坐标适配器，用 Fisher 快照筛选并转存长期记忆。
- **Baseline** · 持续学习基线，具名方法待核。
- **Benchmark** · 标准类别增量基准及分布外偏移。
- **关键结果 / 消融** · 作者报告几何稳定和任务表现改善，组件增益待核。
- **适用条件 / 局限** · 依赖分层存储及 Fisher 估计；实际维护成本需核。

**可复用机制** · 固定增量预算对照普通适配器与幅值、方向分离更新。

<a id="paper-151104"></a>

## Disentangling the Good From the Bad: Quantization-Induced Flips Are Not Random

[官方论文页](https://neurips.cc/virtual/2026/poster/151104) · [作者来源](https://openreview.net/forum?id=cxWrTgqwLx)

- **问题 / 瓶颈** · 总准确率掩盖互相抵消的样本级变化。
- **核心创新 / 方法** · 用 SVD 分析高低秩表示分歧，以区分翻转并做选择性后处理。
- **Baseline** · 全精度模型与 PTQ、QAT 量化流程。
- **Benchmark** · 视觉、语言与多模态模型，评估翻转和准确率。
- **关键结果 / 消融** · 作者报告翻转呈频谱结构；选择性修正能保留有益翻转。
- **适用条件 / 局限** · 不同架构和精度下的阈值需核实。

**可复用机制** · 在压缩验收中加入样本级转移矩阵，并按可接受错误类型选择校正。

<a id="paper-150252"></a>

## Disentangling Where and When: Factored Spatio-Temporal Explanations for Video Action Recognition

[官方论文页](https://neurips.cc/virtual/2026/poster/150252) · [作者来源](https://openreview.net/forum?id=jaIWjThmrT)

- **问题 / 瓶颈** · 单一显著图混合空间外观和时序运动。
- **核心创新 / 方法** · 冻结识别器，联合优化空间和运动掩码，用最近帧替换和分离损失约束。
- **Baseline** · 领先视频解释方法，具名对照待核。
- **Benchmark** · EPIC-Kitchens-55、EGTEA Gaze+、Something-Something V2，含删除 AUC。
- **关键结果 / 消融** · 作者报告最低删除 AUC，掩码约稀疏五倍，并指出常规插入指标偏差。
- **适用条件 / 局限** · 扰动结果依赖替换方式和冻结识别器。

**可复用机制** · 对视频解释单独扫描空间和时间预算，避免用单一像素指标评判。

<a id="paper-151294"></a>

## Dispatchable Coordination Envelopes for Embodied Collaboration Under Sequential Uncertainty

[官方论文页](https://neurips.cc/virtual/2026/poster/151294) · [作者来源](https://openreview.net/forum?id=bVJu7TwSXf)

- **问题 / 瓶颈** · 小延迟或资源冲突会让原本可行的计划无法执行。
- **核心创新 / 方法** · FLECAR 离线合成可派发执行窗口，在线仅修复影响区域。
- **Baseline** · 传统点调度修复及带类似局部修复的点基线。
- **Benchmark** · 相同事件流的合成协作任务，测事件后可行性、成功和修复负担。
- **关键结果 / 消融** · 可行性从 0.388 到 0.840，成功率从 0.580 到 0.840；单步存活指标近似持平。
- **适用条件 / 局限** · 证据来自生成实例，依赖事件与约束建模。

**可复用机制** · 以同事件预算对照窗口与点计划，并分别测局部恢复和长期成功。

<a id="paper-152623"></a>

## Displacement Geometry Captures Platonic Shared Reality Across Models and Modalities

[官方论文页](https://neurips.cc/virtual/2026/poster/152623) · [作者来源](https://openreview.net/forum?id=RhzOixWu51)

- **问题 / 瓶颈** · 点对齐较弱并不意味着模型不共享关系几何。
- **核心创新 / 方法** · 用单一正交变换测位移匹配，分解共享语义和私有能力。
- **Baseline** · 点式相似、微调与关系蒸馏；ShadowCLIP 对照微调方法。
- **Benchmark** · 44 个独立训练的视觉和语言编码器。
- **关键结果 / 消融** · 作者报告位移较绝对位置更一致，微调与关系蒸馏对两个指标影响相反。
- **适用条件 / 局限** · 正交对齐、概念构造及模型族决定可外推范围。

**可复用机制** · 跨模态对齐时同时报告点相似与成对位移保持。

<a id="paper-149863"></a>

## DisRFM: Polar Riemannian Flow Matching for Structure-Preserving Graph Domain Adaptation

[官方论文页](https://neurips.cc/virtual/2026/poster/149863) · [作者来源](https://openreview.net/forum?id=mhAWnLhyoC)

- **问题 / 瓶颈** · 无条件域混淆可能压低标签相关图拓扑并导致不稳。
- **核心创新 / 方法** · 在常曲率空间中以极坐标建模，用拓扑条件流匹配连接类兼容样本。
- **Baseline** · 欧式对抗适配及图域迁移方法，具名基线待核。
- **Benchmark** · 不同结构和语义偏移下的图分类。
- **关键结果 / 消融** · 作者报告优于对照，另分析失配和流误差与目标风险的关系。
- **适用条件 / 局限** · 依赖伪标签质量和几何模型适配。

**可复用机制** · 按语义与结构偏移强度分别测试域适配，核对类别保持。

<a id="paper-148193"></a>

## DisSparse: Pipelined Top-$p$ Sparse Attention for  Long-Context LLM Serving

[官方论文页](https://neurips.cc/virtual/2026/poster/148193) · [作者来源](https://openreview.net/forum?id=zcxTKrFsxv)

- **问题 / 瓶颈** · 固定 top-k 在注意力集中与分散时会分别浪费带宽或遗漏上下文。
- **核心创新 / 方法** · DisSparse 将 top-p 块筛选移出调度关键路径，并用预填充分数重排 token。
- **Baseline** · 稠密 vLLM 和现有 top-p 选择。
- **Benchmark** · 多模型的中长上下文，评测选择速度、批量和准确率。
- **关键结果 / 消融** · 作者报告选择快至 1.45 倍，同内存下最大批量达稠密方案 8 倍。
- **适用条件 / 局限** · 依赖运行时调度和设备；选择速率不等于端到端加速。

**可复用机制** · 在固定召回或精度下测动态块预算与固定预算的总延迟。

<a id="paper-150595"></a>

## Distance-Dependent Connectivity Shapes Continual Learning by Synaptic-Resource-Delimited Separation of Neural Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/150595) · [作者来源](https://openreview.net/forum?id=gyvtSJyA7P)

- **问题 / 瓶颈** · 全随机和过度局部连接可能分别造成广泛竞争或资源瓶颈。
- **核心创新 / 方法** · 在仿真三维循环脉冲网络中按距离赋连接概率，与移除距离依赖比较。
- **Baseline** · 不同连接范围和随机连接。
- **Benchmark** · 十类增量 MNIST，比较准确率、突触竞争及动态分离。
- **关键结果 / 消融** · 中间连接范围最佳，准确率 71.4%，曲线非单调。
- **适用条件 / 局限** · 结论来自仿真及单类任务，不能直接外推皮层。

**可复用机制** · 检验持续学习结构时扫描连接尺度并记录任务间参数竞争。

<a id="paper-152924"></a>

## Distance Marching for Generative Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/152924) · [作者来源](https://openreview.net/forum?id=PPRUA4hujO)

- **问题 / 瓶颈** · 高维样本无法直接给出可靠的最近点投影。
- **核心创新 / 方法** · 按样本到查询位置的邻近性加权损失，学习距离场并构造确定性采样。
- **Baseline** · 不输时间和输入时间的生成模型。
- **Benchmark** · 多数据集及架构，观察生成性能、收敛与分布外检测。
- **关键结果 / 消融** · 作者报告无时间输入仍具竞争力，距离可用于早停；数值待核。
- **适用条件 / 局限** · 高维稀疏流形的距离估计质量需核。

**可复用机制** · 为生成器增加可测的几何停止条件，对照固定步数的成本和质量。

<a id="paper-139444"></a>

## DistDebug-Bench: Can LLM Agents Diagnose Bugs in Distributed Systems?

[官方论文页](https://neurips.cc/virtual/2026/poster/139444) · [作者来源](https://openreview.net/forum?id=Pbjabxdt5U)

- **问题 / 瓶颈** · 单文件编程题无法暴露分布式排障中的视野狭窄。
- **核心创新 / 方法** · 以跨系统真实缺陷构造基准，区分推理结构不足与工具范围不一致。
- **Baseline** · 代表性语言模型与 agent，具名对照待核。
- **Benchmark** · 11 个系统、5 种语言、10 类模式，共 120 个错误。
- **关键结果 / 消融** · 作者报告生产型诊断存在明显差距，常见问题为局部证据偏重。
- **适用条件 / 局限** · 基准诊断结论需与实际维护环境区分。

**可复用机制** · 给维护 agent 测可复现的工具范围、证据覆盖及归因正确度。

<a id="paper-155669"></a>

## Distillation of Foundation Models for Time-dependent PDEs

[官方论文页](https://neurips.cc/virtual/2026/poster/155669) · [作者来源](https://openreview.net/forum?id=3sM5zMNFJn)

- **问题 / 瓶颈** · 少量目标域轨迹容易使学生只见短期真值状态，部署滚动会累积误差。
- **核心创新 / 方法** · TREX 从已微调教师生成长期轨迹并周期注入噪声，学生可加入任务等变先验。
- **Baseline** · 已微调基础模型教师，其他蒸馏对照待核。
- **Benchmark** · 多个含时间演化的 PDE 基准，比较精度、参数量和推理速度。
- **关键结果 / 消融** · 作者报告学生达到或超过教师精度，推理加速逾一个数量级。
- **适用条件 / 局限** · 依赖教师在目标域滚动可信，噪声强度对长期误差的影响待核。

**可复用机制** · 蒸馏序列模型时在相同训练预算比较短真值片段和含恢复状态的教师滚动。

<a id="paper-148655"></a>

## Distilling Conditional Image Generators into Spatial Effect Maps

[官方论文页](https://neurips.cc/virtual/2026/poster/148655) · [作者来源](https://openreview.net/forum?id=w8QGr2Cjci)

- **问题 / 瓶颈** · 生成图像虽能反映协变量，却难量化空间效应。
- **核心创新 / 方法** · 以目标设计下的统计泛函定义效应，并蒸馏均值、梯度或结构化分数。
- **Baseline** · 比较三类蒸馏目标；外部对照待核。
- **Benchmark** · 合成、半真实等十一组实验。
- **关键结果 / 消融** · 给出分离教师偏差、查询和近似误差的界及匹配部分阶数的下界。
- **适用条件 / 局限** · 地图是目标设计下的统计投影，因果解释还需识别假设。

**可复用机制** · 先定义要解释的条件效应，再按目标分布查询教师。

<a id="paper-150714"></a>

## Distilling Graph Geometry: Knowledge Gap from GNNs to MLPs

[官方论文页](https://neurips.cc/virtual/2026/poster/150714) · [作者来源](https://openreview.net/forum?id=g12F7YzATu)

- **问题 / 瓶颈** · 稀疏图学生漏学高能方向，稠密图学生保留教师已压缩的方向。
- **核心创新 / 方法** · 用 Ollivier–Ricci 曲率识别两类误差，以能量加权的对齐规则训练。
- **Baseline** · 其他无需推理时访问图的蒸馏方法。
- **Benchmark** · 节点分类及师生特征秩差。
- **关键结果 / 消融** · 摘要报告分类改善且秩差减少。
- **适用条件 / 局限** · 依赖训练图及曲率估计；详细消融待核。

**可复用机制** · 将蒸馏误差按局部图几何分组，决定哪里蒸馏表征。

<a id="paper-154163"></a>

## Distilling LLM Feedback for Lean Theorem Proving

[官方论文页](https://neurips.cc/virtual/2026/poster/154163) · [作者来源](https://openreview.net/forum?id=FnkxYxDDDG)

- **问题 / 瓶颈** · GRPO 的稀疏奖励可诱发探索不足。
- **核心创新 / 方法** · 用模型在看到外部语言反馈时的 token 分布监督未看到反馈的策略。
- **Baseline** · 单独 GRPO、单独反馈蒸馏及两阶段训练。
- **Benchmark** · Lean 4 定理证明，测策略熵及 pass@k。
- **关键结果 / 消融** · 摘要报告多样性和 pass@k 扩展改善，两阶段更强。
- **适用条件 / 局限** · 依赖有效语言反馈；计算成本与跨任务迁移待核。

**可复用机制** · 在有验证器的推理任务比较反馈蒸馏初始化与直接奖励训练。

<a id="paper-151289"></a>

## Distilling Multi-Teacher Scoring Principles for Unsupervised Time Series Anomaly Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/151289) · [作者来源](https://openreview.net/forum?id=bWTT2NfbCw)

- **问题 / 瓶颈** · 静态集成需同时维护多个推理模型且异常无标签。
- **核心创新 / 方法** · 归一化各教师分数，以分差构造由教师共识决定的成对监督。
- **Baseline** · 单个检测器、静态分数集成及预训练模型。
- **Benchmark** · 七个异常检测数据集及零样本迁移。
- **关键结果 / 消融** · 摘要报告优于单教师和静态集成，学生少于八万参数。
- **适用条件 / 局限** · 教师共同漏检会污染伪监督。

**可复用机制** · 无法对齐不同检测器的分数时先对齐排序，再做教师分歧消融。

<a id="paper-150342"></a>

## Distilling Sequential Computation in Transformer Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150342) · [作者来源](https://openreview.net/forum?id=iqGrRkvjJU)

- **问题 / 瓶颈** · 逐 token 计算和缓存会随上下文增长。
- **核心创新 / 方法** · 轻量合并器将静态嵌入映射为代理，并回退替换既有缓存段。
- **Baseline** · 原预训练自回归模型；具名对照待核。
- **Benchmark** · 问答、摘要、常识和长程数学推理。
- **关键结果 / 消融** · 作者报告有效长度最多减少 40%，准确率退化轻微。
- **适用条件 / 局限** · 是否加速取决于合并及回退的实际成本。

**可复用机制** · 在固定模型上同时测压缩比、真实时延及长程检索损失。

<a id="paper-149862"></a>

## Distilling What Matters: Confidence-Aware Selective Distillation for Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149862) · [作者来源](https://openreview.net/forum?id=mhRs8gO4jl)

- **问题 / 瓶颈** · 静态蒸馏会让不可靠的教师压过学生已有先验。
- **核心创新 / 方法** · 按置信度在 token 层切换 KL 方向，并在批层抑制教师更不确定时的更新。
- **Baseline** · Skewed-KL 和 α–β 散度。
- **Benchmark** · 八组师生、十一项指令、代码及推理等评测。
- **关键结果 / 消融** · 摘要报告跨设置改善；组件独立增量待核。
- **适用条件 / 局限** · 置信度失准可能导致跳过有用教师。

**可复用机制** · 按师生置信差分桶比较各散度，单测教师出错时的学生保持率。

<a id="paper-153115"></a>

## Distill to Think, Foresee to Act: Cognitive-Physical Reinforcement Learning for Autonomous Driving

[官方论文页](https://neurips.cc/virtual/2026/poster/153115) · [作者来源](https://openreview.net/forum?id=Nnj4imYoT2)

- **问题 / 瓶颈** · 模仿学习对少见场景覆盖有限。
- **核心创新 / 方法** · 将视觉语言语义蒸馏入 BEV 编码器，动作条件世界模型预测未来语义，使用物理与意图双奖励。
- **Baseline** · 行为克隆；具名对照待核。
- **Benchmark** · 自动驾驶策略的安全和意图执行；具体设置待核。
- **关键结果 / 消融** · 摘要报告策略评估改善，细项待核。
- **适用条件 / 局限** · 世界模型误差会影响奖励；不能把模拟结果当道路安全保证。

**可复用机制** · 固定行为策略监督，分开消融语义蒸馏、预测奖励和意图奖励。

<a id="paper-139362"></a>

## Distinguishing Performance From Competence in Evaluations of Humanlike Abstract Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/139362) · [作者来源](https://openreview.net/forum?id=Uc9b3QYaQN)

- **问题 / 瓶颈** · 输出准确率可能同时混入抽象能力和实现能力。
- **核心创新 / 方法** · 在不同输入模态、工具和推理预算下评估解答与自然语言规则。
- **Baseline** · 人类及高性能 AI 推理模型。
- **Benchmark** · ConceptARC，以输出准确率和目标规则识别率衡量。
- **关键结果 / 消融** · 文本模式仅看准确率会高估能力，视觉模式可能低估识别能力。
- **适用条件 / 局限** · 依赖规则标注标准；口头规则不证明实际内部过程。

**可复用机制** · 跨模态比较时并报规则识别与规则执行结果。

<a id="paper-151983"></a>

## DISTMOE: Rehearsal-free Routing in Mixture-of-Experts for Distributed Instruction Tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/151983) · [作者来源](https://openreview.net/forum?id=WN0djCTue9)

- **问题 / 瓶颈** · 各客户端专家独训产生特征尺度漂移。
- **核心创新 / 方法** · 新增私有 FFN，整合时只更新路由与轻量投影，并用各向同性约束稳定组合。
- **Baseline** · 集中或分布式视觉指令微调；具名对照待核。
- **Benchmark** · 多种视觉语言基准与分散域设置。
- **关键结果 / 消融** · 摘要报告无需显式域标签的 token 级组合可行。
- **适用条件 / 局限** · 需要有可共享的公共数据；不构成形式隐私保证。

**可复用机制** · 评估分布式专家时对照直接合并与公共锚定，单测混域输入。

<a id="paper-151072"></a>

## Distributed Online Convex Optimization with Compressed Communication: Optimal Regret and Applications

[官方论文页](https://neurips.cc/virtual/2026/poster/151072) · [作者来源](https://openreview.net/forum?id=dA7fbAenM6)

- **问题 / 瓶颈** · 分布式在线凸优化的压缩误差与投影误差耦合。
- **核心创新 / 方法** · 把误差反馈加入 FTRL，再用在线压缩处理双向误差。
- **Baseline** · 未压缩在线优化及理论下界。
- **Benchmark** · 凸及强凸在线损失，以压缩率和轮次数刻画遗憾。
- **关键结果 / 消融** · 取得与下界同阶的遗憾；分别随轮数平方根及对数增长。
- **适用条件 / 局限** · 依赖论文的压缩器与凸性设定。

**可复用机制** · 估通信预算时同时考虑损失曲率和压缩率对遗憾的影响。

<a id="paper-152561"></a>

## Distributed-Order Fractional Spiking Neural Network

[官方论文页](https://neurips.cc/virtual/2026/poster/152561) · [作者来源](https://openreview.net/forum?id=SDhAA8uvvX)

- **问题 / 瓶颈** · 单阶膜电位动力学难表达不同时间尺度。
- **核心创新 / 方法** · 用 Grünwald–Letnikov 离散化实现分布阶动力学。
- **Baseline** · 一阶与单分数阶 SNN。
- **Benchmark** · 脉冲时序建模；具体数据和指标待核。
- **关键结果 / 消融** · 作者说明混合阶数提供更丰富的时间记忆。
- **适用条件 / 局限** · 离散历史状态可能增加时间和内存。

**可复用机制** · 对跨时间尺度的序列在同预算下比较单阶与学习混合阶。

<a id="paper-155766"></a>

## Distribution-Adaptive Policy Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/155766) · [作者来源](https://openreview.net/forum?id=35C6J7b2RQ)

- **问题 / 瓶颈** · 行为和目标策略差距扩大时固定域难兼顾偏差与方差。
- **核心创新 / 方法** · 利用重要性比率统计量自适应控制更新范围。
- **Baseline** · 在策略及传统离策略 RLVR。
- **Benchmark** · 语言模型可验证奖励推理的极端离策略设置。
- **关键结果 / 消融** · 摘要报告稳定并可匹配或超过在策略对照。
- **适用条件 / 局限** · 还需验证极端比率下统计可靠性与跨任务边界。

**可复用机制** · 按样本陈旧程度分组比较固定和分布自适应信赖域。

<a id="paper-152916"></a>

## Distributional Alignment as a Criterion for Designing Task Vectors in In-Context Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/152916) · [作者来源](https://openreview.net/forum?id=PRjQ0E5e0e)

- **问题 / 瓶颈** · 仅看任务准确率难指导如何抽取向量。
- **核心创新 / 方法** · 定义任务向量与完整上下文预测差，再用线性回归估示范效应。
- **Baseline** · 现有任务向量和完整上下文学习。
- **Benchmark** · 八个分类基准、五个语言模型。
- **关键结果 / 消融** · 摘要报告分布差与准确率负相关，平均准确率改善 9.2%。
- **适用条件 / 局限** · 实证集中在分类，生成任务待验证。

**可复用机制** · 在同推理预算下先检验分布对齐，再比较任务准确率。

<a id="paper-153324"></a>

## Distributional Estimation of 3D Object Orientation

[官方论文页](https://neurips.cc/virtual/2026/poster/153324) · [作者来源](https://openreview.net/forum?id=M9VJONoD46)

- **问题 / 瓶颈** · 单姿态或固定对称群难表达连续对称。
- **核心创新 / 方法** · 以截断 Wigner-D 展开表示 SO(3) 上的等变多峰密度。
- **Baseline** · 等变回归器和固定商空间分类器。
- **Benchmark** · ShapeNet 朝向估计，含连续对称类。
- **关键结果 / 消融** · 摘要报告连续对称类优势明显，离散训练标签可泛化到连续带。
- **适用条件 / 局限** · 展开阶数限制可表达的峰宽。

**可复用机制** · 在多解视觉任务中比较分布预测和点估计，并按对称类型拆分。

<a id="paper-150289"></a>

## Distributionally Robust Algorithmic Recourse for Tree Ensembles

[官方论文页](https://neurips.cc/virtual/2026/poster/150289) · [作者来源](https://openreview.net/forum?id=jHEZML7XAa)

- **问题 / 瓶颈** · 更新离散树结构时，连续参数扰动模型不合用。
- **核心创新 / 方法** · 在树预测分布上定义不确定集合，并优化保持有效的挽回建议。
- **Baseline** · 常规挽回与连续参数扰动的稳健路线。
- **Benchmark** · 树集成更新时的建议有效性；详细基准待核。
- **关键结果 / 消融** · 摘要提出可用分布稳健优化表达，量化待核。
- **适用条件 / 局限** · 预测分布偏移集合需覆盖实际更新。

**可复用机制** · 用历史模型版本校验所设不确定集合，然后比较建议成本和稳定性。

<a id="paper-153169"></a>

## Distributionally Robust Black Box Optimization-based Bidding Strategy in Auction-based Federated Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/153169) · [作者来源](https://openreview.net/forum?id=NLbcRxbOBP)

- **问题 / 瓶颈** · 把不可分解的招募与训练收益硬拆成逐步奖励会引入不稳定。
- **核心创新 / 方法** · 将整个流程作为黑盒，使用 Wasserstein 集合处理分布偏移及动态预算投影。
- **Baseline** · 逐步强化学习竞价策略。
- **Benchmark** · 基于拍卖的联邦学习流程；具体实验待核。
- **关键结果 / 消融** · 摘要给出不连续竞价目标的平滑代理分析。
- **适用条件 / 局限** · 完整评估昂贵，分布集合覆盖质量待核。

**可复用机制** · 比较端到端黑盒目标与塑形奖励，在相同调用预算下测结果和违规率。

<a id="paper-150440"></a>

## Distributionally Robust Domain Randomization with Learned Risk-Sensitive Dynamics Samplers

[官方论文页](https://neurips.cc/virtual/2026/poster/150440) · [作者来源](https://openreview.net/forum?id=i1x7979VN8)

- **问题 / 瓶颈** · 固定采样下的平均性能会遗漏罕见失败域。
- **核心创新 / 方法** · 在参考采样器的 KL 邻域取最坏分布，以指数倾斜和反向 KL 拟合采样器。
- **Baseline** · 均匀及自适应域随机化、EPOpt。
- **Benchmark** · 六项 MuJoCo Playground，测 CVaR 和最低回报。
- **关键结果 / 消融** · 摘要报告尾部指标优于对照。
- **适用条件 / 局限** · 要有可参数化动力学和可用策略滚动样本。

**可复用机制** · 固定采样预算比较平均导向与低回报导向，两者均报告均值与尾部。

<a id="paper-154214"></a>

## Distributionally Robust Listwise Preference Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/154214) · [作者来源](https://openreview.net/forum?id=FL7ACXQ5Rb)

- **问题 / 瓶颈** · 近似并列或标注不一致会改变整张排名。
- **核心创新 / 方法** · 对条件排名加总变差不确定集合，最坏排序可按隐式分数排序求出。
- **Baseline** · 名义 Plackett–Luce 及成对稳健优化路线。
- **Benchmark** · 离线固定列表及在线策略生成列表的理论设定。
- **关键结果 / 消融** · 最坏排序计算由阶乘枚举降至排序，并给出优化保证。
- **适用条件 / 局限** · 需验证不确定集合是否代表真实标注偏差。

**可复用机制** · 列表监督中按排名冲突强度比较名义目标和稳健目标。

<a id="paper-150482"></a>

## Distributionally Robust Mixture-of-Experts Training

[官方论文页](https://neurips.cc/virtual/2026/poster/150482) · [作者来源](https://openreview.net/forum?id=hk7uVfp5W3)

- **问题 / 瓶颈** · 负载均衡不能保证非首选专家对误路由输入有足够能力。
- **核心创新 / 方法** · 按专家激活加权的指数滑动损失，通过带熵正则的分层分布加权。
- **Baseline** · FLAME-MoE 和无辅助损失的均衡方案。
- **Benchmark** · 746M 与 10.3B MoE、下游任务和强制误路由。
- **关键结果 / 消融** · 摘要报告专家损失方差下降，误路由下退化降低 4.3%。
- **适用条件 / 局限** · 机制仍需在其他路由规则下核验。

**可复用机制** · 在负载指标外，单测合理的次选专家接收 token 时的损失。

<a id="paper-152819"></a>

## Distributionally Robust Multi-Task Reinforcement Learning via Adaptive Task Sampling

[官方论文页](https://neurips.cc/virtual/2026/poster/152819) · [作者来源](https://openreview.net/forum?id=QAK203jC3u)

- **问题 / 瓶颈** · 等量采样会在简单任务浪费交互。
- **核心创新 / 方法** · 把多任务学习写成可行性问题，用最大回报差定义极小极大采样目标。
- **Baseline** · 等交互预算的多任务训练及其他方法；具名对照待核。
- **Benchmark** · MetaWorld MT10、MT50，数据效率和最差任务结果。
- **关键结果 / 消融** · 作者报告交互效率及较弱任务表现改善。
- **适用条件 / 局限** · 依赖可比较的任务回报目标。

**可复用机制** · 把资源分配和梯度冲突分开消融，固定交互预算比较最差任务表现。
