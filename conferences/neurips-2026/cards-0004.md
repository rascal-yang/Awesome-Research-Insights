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
