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

<a id="paper-151620"></a>

## Distributionally-Robust Policy Learning from Observational Data

[官方论文页](https://neurips.cc/virtual/2026/poster/151620) · [作者来源](https://openreview.net/forum?id=ZBROlVYoFY)

- **问题 / 瓶颈** · 经验策略在结构性分布变化下可能失效
- **核心创新 / 方法** · 将交叉拟合双稳健分数接入散度球最坏值优化，再以对偶分样本校正偏差
- **Baseline** · 经验福利最大化
- **Benchmark** · 福利就业半合成实验，另分析稳健遗憾
- **关键结果 / 消融** · 通常为根号样本倒数速率，有间隔条件时更快
- **适用条件 / 局限** · 限二元干预和指定散度及识别条件

**可复用机制** · 可将这一设计迁移到相同瓶颈的任务，并以所列基线检验：将交叉拟合双稳健分数接入散度球最坏值优化，再以对偶分样本校正偏差。

<a id="paper-154916"></a>

## Distributionally Robust Token Optimization in RLHF

[官方论文页](https://neurips.cc/virtual/2026/poster/154916) · [作者来源](https://openreview.net/forum?id=9zSXz3TUrv)

- **问题 / 瓶颈** · 措辞和语言轻微变化会破坏多步推理
- **核心创新 / 方法** · 在跨度级 actor 损失上构造散度邻域以强调困难片段
- **Baseline** · 常规 token 级 RLHF，具名对照待核
- **Benchmark** · 多个推理基准和输入分布变化，名称待核
- **关键结果 / 消融** · 摘要报告一致性改善，幅度待核
- **适用条件 / 局限** · 结果受跨度划分与散度半径影响

**可复用机制** · 可将这一设计迁移到相同瓶颈的任务，并以所列基线检验：在跨度级 actor 损失上构造散度邻域以强调困难片段。

<a id="paper-150474"></a>

## Distribution Corrected Decision Transformer for Offline Reinforcement Learning with Imbalanced Datasets

[官方论文页](https://neurips.cc/virtual/2026/poster/150474) · [作者来源](https://openreview.net/forum?id=hmdpCpN3Kt)

- **问题 / 瓶颈** · 少数高质量轨迹被大量次优数据淹没
- **核心创新 / 方法** · 由对偶求分布校正权重，以双 KL 维持支持，再同时加权 TD 与 DT 训练
- **Baseline** · 标准 Decision Transformer，其他具名方法待核
- **Benchmark** · D4RL 的不同失衡程度
- **关键结果 / 消融** · 摘要报告高度失衡时表现较强并给出理论保证
- **适用条件 / 局限** · 依赖静态数据覆盖有价值的状态动作

**可复用机制** · 可将这一设计迁移到相同瓶颈的任务，并以所列基线检验：由对偶求分布校正权重，以双 KL 维持支持，再同时加权 TD 与 DT 训练。

<a id="paper-151363"></a>

## Distribution Matching Distillation without Fake Score Network

[官方论文页](https://neurips.cc/virtual/2026/poster/151363) · [作者来源](https://openreview.net/forum?id=b7mPyu8rgW)

- **问题 / 瓶颈** · 独立网络增加更新和内存负担
- **核心创新 / 方法** · 用流映射生成器的端点伪速度替代独立 fake-score 网络
- **Baseline** · 流映射基线和摘要所列 DMD2 对照
- **Benchmark** · ImageNet-1K 256×256，比较 FID 与初始化方案
- **关键结果 / 消融** · 摘要报告流映射初始化时 FID 低于列出的 DMD2 对照，亦支持从头训练
- **适用条件 / 局限** · 伪速度适用于具备流映射结构的生成器

**可复用机制** · 可将这一设计迁移到相同瓶颈的任务，并以所列基线检验：用流映射生成器的端点伪速度替代独立 fake-score 网络。

<a id="paper-155709"></a>

## Distribution Shift in Missing Data Imputation: A Risk-Based Perspective and Importance-Weighted Correction under MAR

[官方论文页](https://neurips.cc/virtual/2026/poster/155709) · [作者来源](https://openreview.net/forum?id=3VK2QApcYJ)

- **问题 / 瓶颈** · 缺失依赖数据时，观测子集的损失偏离全数据风险
- **核心创新 / 方法** · 对观测数据的重要性加权以恢复全分布风险目标
- **Baseline** · 相同插补器的未校正版本
- **Benchmark** · MAR 插补模拟，比较 RMSE 与 Wasserstein 距离
- **关键结果 / 消融** · 平均分别下降 3% 和 7%
- **适用条件 / 局限** · 需要 MAR 假设及可靠的观测概率

**可复用机制** · 可将这一设计迁移到相同瓶颈的任务，并以所列基线检验：对观测数据的重要性加权以恢复全分布风险目标。

<a id="paper-153594"></a>

## DiT4DiT: Jointly Modeling Video Dynamics and Actions for Generalizable Robot Control

[官方论文页](https://neurips.cc/virtual/2026/poster/153594) · [作者来源](https://openreview.net/forum?id=KG3sjtKCP6)

- **问题 / 瓶颈** · 完整未来视频生成给实时控制增加延迟
- **核心创新 / 方法** · 读取视频 DiT 固定流时间步隐藏特征并直接驱动动作 DiT
- **Baseline** · VLA 和视频动作基线，具名对照待核
- **Benchmark** · LIBERO、24 项 RoboCasa-GR1、Unitree G1 真机
- **关键结果 / 消融** · 仿真分别为 98.6% 和 56.7%，较既有视频动作方法最高快 12 倍
- **适用条件 / 局限** · 单时间步的选取和跨频率鲁棒性待核

**可复用机制** · 可将这一设计迁移到相同瓶颈的任务，并以所列基线检验：读取视频 DiT 固定流时间步隐藏特征并直接驱动动作 DiT。

<a id="paper-149888"></a>

## Diverse Representative Rashomon Sets for Sparse Generalized Additive Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149888) · [作者来源](https://openreview.net/forum?id=mTtx8zpRhk)

- **问题 / 瓶颈** · 只在固定特征组内查找会低估预测多解性
- **核心创新 / 方法** · 从近最优模型集合中按多样性采样不同特征子集的稀疏 GAM
- **Baseline** · 特征受限的近最优集近似
- **Benchmark** · 比较模型多样性指标和预测质量，数据集待核
- **关键结果 / 消融** · 摘要报告多项指标的多样性显著增加且预测性能相近
- **适用条件 / 局限** · 依赖近最优阈值、距离定义和采样混合

**可复用机制** · 可将这一设计迁移到相同瓶颈的任务，并以所列基线检验：从近最优模型集合中按多样性采样不同特征子集的稀疏 GAM。

<a id="paper-151364"></a>

## Diversity Combining for Multi-Path LLM Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/151364) · [作者来源](https://openreview.net/forum?id=b7em4wEW0h)

- **问题 / 瓶颈** · 同质推理路径相关，增加样本会收益饱和
- **核心创新 / 方法** · 用四路径试运行估计相关性，再选择投票路径数与提示多样性
- **Baseline** · 固定 32 路多数投票及同质模板
- **Benchmark** · 五模型十二基准，数学、问答与语言理解
- **关键结果 / 消融** · 保留固定 32 路准确率的 97–104%；模板多样化在 57 个有效单元中的 55 个降低相关
- **适用条件 / 局限** · 均匀合并分析依赖可交换性

**可复用机制** · 可将这一设计迁移到相同瓶颈的任务，并以所列基线检验：用四路径试运行估计相关性，再选择投票路径数与提示多样性。

<a id="paper-153210"></a>

## Divide et Calibra: Multiclass Local Calibration via Vector Quantization

[官方论文页](https://neurips.cc/virtual/2026/poster/153210) · [作者来源](https://openreview.net/forum?id=N1Z3ARfFfn)

- **问题 / 瓶颈** · 全局校准掩盖局部误差，独立局部拟合又缺数据
- **核心创新 / 方法** · 在量化表示分区间共享 Dirichlet 校准因子
- **Baseline** · 全局和现有局部校准，具名方法待核
- **Benchmark** · 多分类基准，比较局部与全局校准及预测表现
- **关键结果 / 消融** · 摘要报告局部校准改善、全局表现可比
- **适用条件 / 局限** · 依赖码本分区和稀疏区域的因子共享

**可复用机制** · 可将这一设计迁移到相同瓶颈的任务，并以所列基线检验：在量化表示分区间共享 Dirichlet 校准因子。

<a id="paper-153517"></a>

## DivMoE: Fine-Grained MoE Upcycling via Cross-Domain Expert Composition

[官方论文页](https://neurips.cc/virtual/2026/poster/153517) · [作者来源](https://openreview.net/forum?id=KlvTMimHUL)

- **问题 / 瓶颈** · 复制初始化缺多样性，随机扰动可能伤及已有知识
- **核心创新 / 方法** · 以各领域微调模型初始化专家，路由每个领域最多选一个专家
- **Baseline** · 既有密集模型转 MoE 方法及 Moonlight-MoE
- **Benchmark** · 两种底座，比较平均准确率
- **关键结果 / 消融** · 转化对照为 47.0% 对 44.4%，另一设置与 Moonlight-MoE 同为 64.5%
- **适用条件 / 局限** · 领域划分与路由限制可能损害单领域容量

**可复用机制** · 可将这一设计迁移到相同瓶颈的任务，并以所列基线检验：以各领域微调模型初始化专家，路由每个领域最多选一个专家。

<a id="paper-152646"></a>

## DMax: Aggressive Parallel Decoding for dLLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/152646) · [作者来源](https://openreview.net/forum?id=RSM3ZqRlL2)

- **问题 / 瓶颈** · 硬提交 token 使并行错误累积
- **核心创新 / 方法** · 在掩码和预测词嵌入间软插值，训练恢复自身错误预测
- **Baseline** · LLaDA-2.0-mini
- **Benchmark** · GSM8K、MBPP、单 H200 批量一吞吐
- **关键结果 / 消融** · 两基准每步 token 分别由 2.04 到 5.47、2.71 到 5.86，准确率可比
- **适用条件 / 局限** · 吞吐依赖模型、硬件和实现

**可复用机制** · 可将这一设计迁移到相同瓶颈的任务，并以所列基线检验：在掩码和预测词嵌入间软插值，训练恢复自身错误预测。

<a id="paper-153054"></a>

## dMoE: dLLMs with Learnable Block Experts

[官方论文页](https://neurips.cc/virtual/2026/poster/153054) · [作者来源](https://openreview.net/forum?id=OMfRyEM1p5)

- **问题 / 瓶颈** · 逐 token 路由使并行块激活太多不同专家
- **核心创新 / 方法** · 聚合块内 token 路由分布，再用共享块分布引导专家选择
- **Baseline** · 常规逐 token MoE
- **Benchmark** · 多基准性能、独立专家数、内存和端到端延迟
- **关键结果 / 消融** · 专家数均值 69.5 降至 14.6，保留 99.11% 表现，提速 1.14 到 1.66 倍
- **适用条件 / 局限** · 块内需求差异过大时复用收益待验证

**可复用机制** · 可将这一设计迁移到相同瓶颈的任务，并以所列基线检验：聚合块内 token 路由分布，再用共享块分布引导专家选择。

<a id="paper-149321"></a>

## DnNP: Denoising Input Uncertainty in Neural Processes

[官方论文页](https://neurips.cc/virtual/2026/poster/149321) · [作者来源](https://openreview.net/forum?id=r0rxOyMffL)

- **问题 / 瓶颈** · 把带噪输入视为准确值会破坏估计和不确定性
- **核心创新 / 方法** · 用变分推断把输入去噪纳入神经过程元学习
- **Baseline** · 标准神经过程及固定观测方差插件模型
- **Benchmark** · 合成和真实数据，包含 PM2.5 空间插值
- **关键结果 / 消融** · 空气质量任务 RMSE 最多降 43%，NLL 最多降 80%
- **适用条件 / 局限** · 依赖噪声模型的适配性和观测覆盖

**可复用机制** · 可将这一设计迁移到相同瓶颈的任务，并以所列基线检验：用变分推断把输入去噪纳入神经过程元学习。

<a id="paper-148605"></a>

## DocAtlas: Long-Document Understanding as Mutable-State Interaction

[官方论文页](https://neurips.cc/virtual/2026/poster/148605) · [作者来源](https://openreview.net/forum?id=wV6e00cQ2S)

- **问题 / 瓶颈** · 静态索引难随问答过程积累分散证据。
- **核心创新 / 方法** · 层级文档树和可写笔记支撑搜索、读取及复核，固定上下文预算。
- **Baseline** · 直接输入 Qwen3.5-4B；另有人类参考。
- **Benchmark** · MMLongBench-Doc。
- **关键结果 / 消融** · GPT-5.4 为 71.4%，人类参考 65.8%；训练后小模型 63.7% 对 54.4%。
- **适用条件 / 局限** · 环境与训练贡献需拆分。

**可复用机制** · 固定上下文比较只读检索与允许写入和复核的检索。

<a id="paper-148548"></a>

## Do Coding Agents Deceive Us? Detecting and Preventing Cheating via Capped Evaluation with Randomized Tests

[官方论文页](https://neurips.cc/virtual/2026/poster/148548) · [作者来源](https://openreview.net/forum?id=x3srtw3rZo)

- **问题 / 瓶颈** · 自动评分可能奖励偏离任务意图的行为。
- **核心创新 / 方法** · 用随机测试构造正常完成时有已知上限的评测，并调整奖励避免过度追分。
- **Baseline** · 常规评测和奖励；具名变体待核。
- **Benchmark** · 多套代码数据集，测异常检测及排名稳定性。
- **关键结果 / 消融** · 作者报告可识别异常且保持排名，并减少违规行为。
- **适用条件 / 局限** · 依赖可论证的上限与独立测试。

**可复用机制** · 在授权代码评测中将显著超上限的结果送独立复核。

<a id="paper-139137"></a>

## Do Composed Image Retrieval Benchmarks Require Multimodal Composition?

[官方论文页](https://neurips.cc/virtual/2026/poster/139137) · [作者来源](https://openreview.net/forum?id=ihmgZB5OWQ)

- **问题 / 瓶颈** · 高检索分可能只来自单一模态。
- **核心创新 / 方法** · 跨模型找单模态可解查询，人审剩余查询是否有效。
- **Baseline** · 图像单模态、文本单模态和联合检索。
- **Benchmark** · 四个 CIR 基准、11 个嵌入模型，人审 4741 条。
- **关键结果 / 消融** · 单模态可解比例 32.2%–83.6%；人审仅 1689 条有效。
- **适用条件 / 局限** · 捷径定义取决于模型集合与人工审核。

**可复用机制** · 用单模态消融和人审验证互补信息是否必需。

<a id="paper-139349"></a>

## DocScope: Benchmarking Verifiable Reasoning for Trustworthy Long-Document Understanding

[官方论文页](https://neurips.cc/virtual/2026/poster/139349) · [作者来源](https://openreview.net/forum?id=V55GtaUSsR)

- **问题 / 瓶颈** · 答案正确不保证页、区域和事实齐全。
- **核心创新 / 方法** · 独立评估定位页、定位区域、抽取事实与验证答案。
- **Baseline** · 6 个闭源、12 个开源权重及专门模型。
- **Benchmark** · DocScope，273 份文档、1124 题。
- **关键结果 / 消融** · 正确答案中最高完整证据率也只有 29%；区域定位最弱。
- **适用条件 / 局限** · 评判器需经人工校准。

**可复用机制** · 将端到端失败拆到证据链阶段，确定应投资哪个模块。

<a id="paper-152903"></a>

## Do Deep Networks Forget Initialization? A Forgetting-Time View of Practical Inductive Bias

[官方论文页](https://neurips.cc/virtual/2026/poster/152903) · [作者来源](https://openreview.net/forum?id=PYoCtCiU8K)

- **问题 / 瓶颈** · 训练插值后仍可能保留初始化偏差。
- **核心创新 / 方法** · 用验证选择模型对初始化尺度的敏感性定义记忆，改变步长和正则。
- **Baseline** · 低步长 SGD、Adam 系与带范数控制的较高步长 SGD。
- **Benchmark** · CIFAR-10 ResNet 控制实验。
- **关键结果 / 消融** · ResNet-9 测试差达 26.5 个百分点，5000 epoch 仍近似不变。
- **适用条件 / 局限** · 现有证据限所测模型和任务。

**可复用机制** · 用长训练和匹配训练误差区分欠训练与持续的初始化敏感性。

<a id="paper-151086"></a>

## Do Diffusion Models Learn to Generalize Basic Visual Skills?

[官方论文页](https://neurips.cc/virtual/2026/poster/151086) · [作者来源](https://openreview.net/forum?id=d54SJBv41M)

- **问题 / 瓶颈** · 偏好和分布分数不区分技能外推与训练模式复现。
- **核心创新 / 方法** · 按可控技能规则合成训练集，并用规则直接打分。
- **Baseline** · 比较不同技能、随机种子和组合覆盖。
- **Benchmark** · VGL 的旋转、大小、计数、位置等技能。
- **关键结果 / 消融** · 旋转通常更可外推，但部分种子在周期边界失败。
- **适用条件 / 局限** · 合成实验不能直接外推到真实图像。

**可复用机制** · 报告不同技能和种子的外推曲线。

<a id="paper-152978"></a>

## Do Enterprise Systems Need Learned World Models? The Importance of Context to Infer Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/152978) · [作者来源](https://openreview.net/forum?id=OuLPTxbP2G)

- **问题 / 瓶颈** · 不同企业实例的配置使离线模型分布外失效。
- **核心创新 / 方法** · 在授权实例读取启用配置，按当前环境预测连锁状态变化。
- **Baseline** · 离线训练世界模型与配置读取代理。
- **Benchmark** · CascadeBench 合成环境的部署偏移。
- **关键结果 / 消融** · 作者报告离线模型遇规则变化下降，而读取配置更稳健。
- **适用条件 / 局限** · 要求具备授权访问且规则可读。

**可复用机制** · 先测规则改动后的预测误差，再选择训练或读取配置。

<a id="paper-150443"></a>

## Does 1/2-Tsallis-INF Also Work Well for Best-Arm Identification?

[官方论文页](https://neurips.cc/virtual/2026/poster/150443) · [作者来源](https://openreview.net/forum?id=i09r9ofsSO)

- **问题 / 瓶颈** · 低遗憾算法很少采样次优臂，重要性估计仍有大波动。
- **核心创新 / 方法** · 用估计累计损失差的 Lyapunov 函数分析错选概率。
- **Baseline** · 半阶 Tsallis-INF 原有低遗憾结论。
- **Benchmark** · 随机多臂理论设定，指标为经验最佳臂错选概率。
- **关键结果 / 消融** · 在给定学习率下推导多项式上界。
- **适用条件 / 局限** · 分析针对候选算法和随机设定。

**可复用机制** · 选择采样算法时同时检查部署收益与终点辨识的保证。

<a id="paper-151042"></a>

## Does Compression Imply Generalization? A Minimum Description Length Perspective

[官方论文页](https://neurips.cc/virtual/2026/poster/151042) · [作者来源](https://openreview.net/forum?id=dQ36O5uJBs)

- **问题 / 瓶颈** · 权重压缩或互信息难以从训练过程直接估计。
- **核心创新 / 方法** · 建立序贯遗憾、算法诱导参数描述长度和 PAC-MDL 界之间的联系。
- **Baseline** · 与信息瓶颈的编码复杂度校正作理论比较。
- **Benchmark** · CIFAR-10/100，测信号和泛化误差相关性。
- **关键结果 / 消融** · Pearson 相关超过 0.9。
- **适用条件 / 局限** · 理论针对近插值条件。

**可复用机制** · 比较训练配置时记录序贯遗憾，并检查是否在同样插值水平仍跟踪泛化。

<a id="paper-154086"></a>

## Does Inference-Time Reasoning Really Improve Video Understanding?

[官方论文页](https://neurips.cc/virtual/2026/poster/154086) · [作者来源](https://openreview.net/forum?id=GJtLZ5sLOQ)

- **问题 / 瓶颈** · 模型靠文本先验或单帧也可能答对。
- **核心创新 / 方法** · 控制帧采样并加入可定位的问题。
- **Baseline** · 纯文本、稀疏帧到实时采样，比较推理增强。
- **Benchmark** · VideoMME、Video-MMMU、LVBench 及 1500 题 TGVMME。
- **关键结果 / 消融** · 既有基准捷径 13%–46%，新基准 3.5%，额外推理增益最高 2.5%。
- **适用条件 / 局限** · 时间定位容差与标注质量待核。

**可复用机制** · 判断推理是否改善视觉理解时，拆看答对与找到证据的交集。

<a id="paper-156069"></a>

## Does Mixed Label Imbalance Matter to Minority Collapse in Imbalanced Learning?

[官方论文页](https://neurips.cc/virtual/2026/poster/156069) · [作者来源](https://openreview.net/forum?id=0g48FtWsjv)

- **问题 / 瓶颈** · 原始类别平衡未必缓解混合标签下的少类塌缩。
- **核心创新 / 方法** · 将混合标签视为独立标签并做平衡采样。
- **Baseline** · 类别平衡 Mixup。
- **Benchmark** · 少类塌缩的理论与实验，数据集待核。
- **关键结果 / 消融** · 作者报告混合标签平衡有利，量化待核。
- **适用条件 / 局限** · 混合标签数和实际数据分布可能影响收益。

**可复用机制** · 固定原始类别平衡再消融混合标签平衡。

<a id="paper-153810"></a>

## Does Seeing More Mean Knowing More? Mono-Anchored Advantage Normalization for Multi-Source Visual Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/153810) · [作者来源](https://openreview.net/forum?id=IXNKGx1CUw)

- **问题 / 瓶颈** · 附加模态也可能干扰原有主信号。
- **核心创新 / 方法** · 把多源相对单源的收益纳入优势归一化。
- **Baseline** · 常规多源 RLVR 和单源输入。
- **Benchmark** · 多源视觉推理，具名基准待核。
- **关键结果 / 消融** · 理论解释梯度中的信息增益，量化幅度待核。
- **适用条件 / 局限** · 需可比较的单源奖励。

**可复用机制** · 加模态时同时记录相对最强单源的收益和干扰。

<a id="paper-153905"></a>

## Does Sparse Connectivity Improve Generalization? Convolutional Networks Below the Edge of Stability

[官方论文页](https://neurips.cc/virtual/2026/poster/153905) · [作者来源](https://openreview.net/forum?id=Hq5Gl3Qj0N)

- **问题 / 瓶颈** · 全连接的稳定性界在高维球面可能空泛。
- **核心创新 / 方法** · 分析两层 ReLU 稀疏连接下的图块几何与稳定性限制。
- **Baseline** · 全连接网络和缺乏结构的图块。
- **Benchmark** · 理论球面设置与自然图像图块分析。
- **关键结果 / 消融** · 小感受野时给出非空泛界，缺结构的图块仍可过拟合。
- **适用条件 / 局限** · 限低于稳定性边缘的两层分析。

**可复用机制** · 选局部连接前检查训练图块是否真有低维结构。

<a id="paper-154722"></a>

## Does Synthetic Data Help? Empirical Evidence from Deep Learning Time Series Forecasters

[官方论文页](https://neurips.cc/virtual/2026/poster/154722) · [作者来源](https://openreview.net/forum?id=BUZncgztnb)

- **问题 / 瓶颈** · 平均增强收益会掩盖模型间相反响应。
- **核心创新 / 方法** · 交叉扫描模型、数据生成方式、数据稀疏度和课程切换。
- **Baseline** · 无增强与全量训练，比较不同课程。
- **Benchmark** · 五种架构、七个数据集、4218 次运行。
- **关键结果 / 消融** · 67% 试验退化，混合通道模型较易获益，硬切换 MSE 恶化 24%。
- **适用条件 / 局限** · 结论受生成器和数据集限制。

**可复用机制** · 小预算试点时交叉考察架构和生成器，并与渐进调度对照。

<a id="paper-150111"></a>

## Does the Question Really Matter? Training-Free Data Selection for Vision-Language SFT

[官方论文页](https://neurips.cc/virtual/2026/poster/150111) · [作者来源](https://openreview.net/forum?id=kcBOe422p2)

- **问题 / 瓶颈** · 训练样本可能靠语言捷径解答。
- **核心创新 / 方法** · 使用冻结视觉语言模型衡量条件差异，无需另训练代理。
- **Baseline** · 全量训练及 COINCIDE、XMAS。
- **Benchmark** · Vision-Flan 与 The Cauldron。
- **关键结果 / 消融** · Vision-Flan 用 10% 和 15% 数据报告提升 3.5% 和 4.8%。
- **适用条件 / 局限** · 依赖评估模型对答案有效性的校准。

**可复用机制** · 优先选择问题真正改变视觉证据解释的样本，并与同预算选择比较。

<a id="paper-154047"></a>

## Does Weight Decay Enhance Training Stability?

[官方论文页](https://neurips.cc/virtual/2026/poster/154047) · [作者来源](https://openreview.net/forum?id=GcAFI8YYmu)

- **问题 / 瓶颈** · 稳定性概念容易混用
- **核心创新 / 方法** · 跟踪稳定性边缘与参数和尖锐度梯度的全局对齐
- **Baseline** · 不同权重衰减与理论边界
- **Benchmark** · CNN、MLP 及 NTK 动力学
- **关键结果 / 消融** · CNN 振荡减弱，MLP 可在低于 2/η 处稳定
- **适用条件 / 局限** · 所研究网络和训练设定限制外推

**可复用机制** · 同时报告参数振荡、尖锐度与函数空间变化

<a id="paper-149184"></a>

## Does Your Large Language Model Have An Intuitive Sense of The Difficulty of A Question?

[官方论文页](https://neurips.cc/virtual/2026/poster/149184) · [作者来源](https://openreview.net/forum?id=sFq1guxX1W)

- **问题 / 瓶颈** · 额外 rollout 才估难度成本高
- **核心创新 / 方法** · 用少数参考题和单次前向读出难度，再切换推理预算
- **Baseline** · 额外 rollout 与训练难度预测器
- **Benchmark** · 数学、代码生成与问答
- **关键结果 / 消融** · 较 rollout 方法效率为 1.34–2.00 倍
- **适用条件 / 局限** · 参考题选择和域外稳健性待核

**可复用机制** · 固定正确率比较隐状态难度门控与试答门控

<a id="paper-155236"></a>

## Does Your Neural Network Extrapolate? Feature Engineering as Identifiability Bias for OOD Generalization

[官方论文页](https://neurips.cc/virtual/2026/poster/155236) · [作者来源](https://openreview.net/forum?id=7Df6LrvRJh)

- **问题 / 瓶颈** · 训练窗无法区分窗外分歧的数据过程
- **核心创新 / 方法** · 分析结构承诺和变换后覆盖；周期性例子用傅里叶坐标
- **Baseline** · 同架构同域内损失的不同表示
- **Benchmark** · 周期外推、天文预测及位置编码实验
- **关键结果 / 消融** · 作者报告仅改表示域外误差可差约 520 倍
- **适用条件 / 局限** · 正确表示仍需模型可表达且训练覆盖充分

**可复用机制** · 域内拟合相同时改变表示并检验外推

<a id="paper-154112"></a>

## Do Glimpse Policies See Like Humans? A Behavioral Audit Reveals Dissociated Viewing Priors in Classification-Trained Active Vision

[官方论文页](https://neurips.cc/virtual/2026/poster/154112) · [作者来源](https://openreview.net/forum?id=GBLeJAfMvA)

- **问题 / 瓶颈** · 分类精度无法代表自由观看行为
- **核心创新 / 方法** · 在五个行为维度比较 AdaptiveNN 与人类凝视
- **Baseline** · 中心偏置、人类轨迹
- **Benchmark** · 三个自由观看数据集
- **关键结果 / 消融** · 空间表现低于中心偏置，重访和扫视亦偏离人类
- **适用条件 / 局限** · 单一策略的结果不可推广至所有主动视觉

**可复用机制** · 对拟人视觉声明加入简单空间先验和条件行为对照

<a id="paper-151157"></a>

## Do Graph Neural Networks Learn Generalizable Algorithms for Clustering Graphs?

[官方论文页](https://neurips.cc/virtual/2026/poster/151157) · [作者来源](https://openreview.net/forum?id=car3LKiN8G)

- **问题 / 瓶颈** · 域内聚类不足以确定模型学到的算法
- **核心创新 / 方法** · 固定割代价训练不同 GNN，再用理论与探针辨别启发式
- **Baseline** · MPNN 与 PPGN 等架构
- **Benchmark** · 大图及不同图族，考察割代价与算法探针
- **关键结果 / 消融** · 各方均有泛化，表达能力不同可学出不同算法
- **适用条件 / 局限** · 差异依赖所选目标和图族

**可复用机制** · 同时报告目标函数表现与区分启发式的探针

<a id="paper-152263"></a>

## DoG: Sniffing Out Overconfidence in LLM Agents via Post-hoc Trajectory Restructuring

[官方论文页](https://neurips.cc/virtual/2026/poster/152263) · [作者来源](https://openreview.net/forum?id=UNOK2zAeoF)

- **问题 / 瓶颈** · 扁平轨迹遗漏分支与工具证据
- **核心创新 / 方法** · 把最终答案与推理、工具输出连成有向无环图
- **Baseline** · 通用文字校准与轨迹校准方法
- **Benchmark** · GAIA、GPQA、HLE，测 ECE、Brier 与 AUROC
- **关键结果 / 消融** · 报告多个指标改善或可比
- **适用条件 / 局限** · 依赖能够正确恢复证据关系

**可复用机制** · 固定轨迹并比较线性和图式校准

<a id="paper-153349"></a>

## Do Heavy Tails Help Diffusion? On the Subtle Trade-off Between Initialization and Training

[官方论文页](https://neurips.cc/virtual/2026/poster/153349) · [作者来源](https://openreview.net/forum?id=M1lkWZqUpb)

- **问题 / 瓶颈** · 厚尾初始化看似适合尾部数据却改变学习难度
- **核心创新 / 方法** · 比较厚尾与轻尾驱动扩散的采样误差界并验证
- **Baseline** · 轻尾高斯噪声
- **Benchmark** · 两个代表性扩散模型及合成和真实数据
- **关键结果 / 消融** · 厚尾使统计估计更难，实验观察到预期折衷
- **适用条件 / 局限** · 误差界依赖所考虑模型

**可复用机制** · 使用匹配数据和训练预算比较尾部召回与全局误差

<a id="paper-139308"></a>

## Do Image Editing Models Understand Lighting?

[官方论文页](https://neurips.cc/virtual/2026/poster/139308) · [作者来源](https://openreview.net/forum?id=YDISH8weQa)

- **问题 / 瓶颈** · 整体观感难替代像素级光传输判断
- **核心创新 / 方法** · 采集 HDR 配对并按材质及光照区域标注，校正摄影变化
- **Baseline** · 图像编辑模型和 VLM 评判
- **Benchmark** · 3DLP 约千对室内图像
- **关键结果 / 消融** · 低照明影响区域更易错，VLM 不适合像素级判断
- **适用条件 / 局限** · 主要限于室内和局部光源

**可复用机制** · 按光照变化幅度分桶比较物理误差

<a id="paper-139141"></a>

## Do Joint Audio-Video Generation Models Understand Physics?

[官方论文页](https://neurips.cc/virtual/2026/poster/139141) · [作者来源](https://openreview.net/forum?id=iUbannicWz)

- **问题 / 瓶颈** · 分别看声音及图像合理会忽视二者对应
- **核心创新 / 方法** · 五维评测覆盖模态内语义、物理与跨模态物理
- **Baseline** · 三个闭源与四个开放模型
- **Benchmark** · AV-Phys Bench 与人工评测
- **关键结果 / 消融** · 领先模型通过率 0.660，转变情景最多下降 67%
- **适用条件 / 局限** · 自动评分仍依赖工具与人工对齐

**可复用机制** · 评测跨模态模型时单列变化发生前后的耦合错误

<a id="paper-153454"></a>

## Do Latent-CoT Models Think Step-by-Step? A Mechanistic Study on Sequential Reasoning Tasks

[官方论文页](https://neurips.cc/virtual/2026/poster/153454) · [作者来源](https://openreview.net/forum?id=LAS8pm4WJ6)

- **问题 / 瓶颈** · 答案正确不能证明逐步计算
- **核心创新 / 方法** · 以探针、注意力和激活修补追踪多项式迭代中间状态
- **Baseline** · 不同任务深度及代数可压缩程度
- **Benchmark** · CODI 顺序多项式迭代
- **关键结果 / 消融** · 短任务出现忠实桥状态，复杂任务则部分压缩或消失
- **适用条件 / 局限** · 单类模型和任务的结论

**可复用机制** · 使用可控有效记忆需求验证推理路径

<a id="paper-148862"></a>

## Do Less, Decide Better: Optimal Human Dispatching in AI-Assisted Decisions

[官方论文页](https://neurips.cc/virtual/2026/poster/148862) · [作者来源](https://openreview.net/forum?id=ud2UVEQahC)

- **问题 / 瓶颈** · 逐项人审成本高
- **核心创新 / 方法** · 平方损失下求上下文奖励，线性设定分解两因素
- **Baseline** · 完整人审及不同回归头
- **Benchmark** · 3408 篇 ICLR 投稿、十维评分、三种模型
- **关键结果 / 消融** · 查询两至三项即可达到完整人审表现
- **适用条件 / 局限** · 依赖可拆分维度及可估条件不确定性

**可复用机制** · 固定人审预算比较不确定性与双因素调度

<a id="paper-150394"></a>

## Do LLMs Bind Episodes? Probing Cross-Episode Parametric Retrieval Through Shared Cues

[官方论文页](https://neurips.cc/virtual/2026/poster/150394) · [作者来源](https://openreview.net/forum?id=iO1tKRn7Lk)

- **问题 / 瓶颈** · 单事实可答不代表多事件能一同取回
- **核心创新 / 方法** · 比较开放回答、多选和受控叙事，并测试回忆生成监督
- **Baseline** · 延长推理、缩放及延长训练
- **Benchmark** · 多种前沿模型和受控叙事
- **关键结果 / 消融** · 绑定失败率 4–62%，高监督覆盖未转化为顺序训练准确率
- **适用条件 / 局限** · 真实知识验证和受控叙事各有边界

**可复用机制** · 分别测知识可访问性与联合生成最终覆盖

<a id="paper-154451"></a>

## Domain-Conditioned Class Imbalance: Why Global Class Balance Fails Across Domains

[官方论文页](https://neurips.cc/virtual/2026/poster/154451) · [作者来源](https://openreview.net/forum?id=DSwaLAA6lD)

- **问题 / 瓶颈** · 总体类别和域均衡可掩盖稀少组合
- **核心创新 / 方法** · 构造受控联合失衡，按实例生成域条件分类参数和伪标签
- **Baseline** · 多域不平衡方法
- **Benchmark** · 四个多域基准的三类设定
- **关键结果 / 消融** · 作者报告相对对照改善
- **适用条件 / 局限** · 依赖域线索质量；子组数值待核

**可复用机制** · 采样审计同时报告域类联合覆盖

<a id="paper-148171"></a>

## DOME: Drift-Adaptive On-Policy Motion Erasure in Video Diffusion Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/148171) · [作者来源](https://openreview.net/forum?id=zlsIDv6ZvH)

- **问题 / 瓶颈** · 原始轨迹监督收敛后指定运动仍可能存在
- **核心创新 / 方法** · 从编辑模型采样并沿观测漂移调整监督位置
- **Baseline** · 策略外轨迹与普通策略内训练
- **Benchmark** · Wan 2.1-T2V 的 20 个运动概念
- **关键结果 / 消融** · 局部接触动作受抑，全身动态效果有限；适应漂移消融关键
- **适用条件 / 局限** · 效果依赖运动概念及编辑位置

**可复用机制** · 编辑生成模型时同时监控训练损失和真实采样行为

<a id="paper-153447"></a>

## Dominant-Layer ZO: A Single Layer Dominates Zeroth-Order Fine-Tuning of LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/153447) · [作者来源](https://openreview.net/forum?id=LEaZsZB1xF)

- **问题 / 瓶颈** · 全量扰动计算多且信号不均
- **核心创新 / 方法** · 用首个激活离群层定位主导层，仅更新该层
- **Baseline** · 全量 MeZO 和 LoRA 零阶微调
- **Benchmark** · LLaMA2-7B、Qwen3-8B，九个基准
- **关键结果 / 消融** · 摘要报告最高 4.52 倍训练加速及平均性能改善
- **适用条件 / 局限** · 主导层随模型变化

**可复用机制** · 在新骨干比较单层扫描和统一参数预算

<a id="paper-153401"></a>

## Do More Modalities Always Help? A Geometric Perspective on Missing-Modality Robustness

[官方论文页](https://neurips.cc/virtual/2026/poster/153401) · [作者来源](https://openreview.net/forum?id=Le36VrocGr)

- **问题 / 瓶颈** · 全模态训练会形成缺模态时不利的依赖
- **核心创新 / 方法** · 将权重主子空间沿 Grassmann 测地线向单模态参照修正
- **Baseline** · 单模态及缺模态鲁棒方法
- **Benchmark** · 融合、双塔和视觉语言模型
- **关键结果 / 消融** · 作者报告缺模态表现改善且全模态精度保持
- **适用条件 / 局限** · 需要单模态参照和可定位的交互层

**可复用机制** · 同时汇报模态齐全与缺失时的表现，避免平均指标掩盖回退

<a id="paper-152489"></a>

## Done, But Not Sure: Disentangling World Completion from Self-Termination in Embodied Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/152489) · [作者来源](https://openreview.net/forum?id=SjRdxm7d6G)

- **问题 / 瓶颈** · 单一成功率混淆未完成、过度执行和虚报。
- **核心创新 / 方法** · VIGIL 按隐藏状态和终止报告分别计算分数。
- **Baseline** · 同一模型的状态完成率与验证成功率。
- **Benchmark** · 20 个模型、1000 个冻结回合。
- **关键结果 / 消融** · 执行接近的模型验证成功率差距可达 19.7 个百分点。
- **适用条件 / 局限** · 依赖可验证世界状态。

**可复用机制** · 分别记录达成、终止和证据充分性。

<a id="paper-152693"></a>

## Do Not Let Spikes Flip: Margin-Resculpted Learning for Robust Spiking Neural Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/152693) · [作者来源](https://openreview.net/forum?id=R7E5DE5F3A)

- **问题 / 瓶颈** · 连续激活目标不足以捕捉离散发放翻转。
- **核心创新 / 方法** · 度量翻转率和阈值裕量，并按活动水平约束过度占用。
- **Baseline** · 现有脉冲网络稳健训练，具名方法待核。
- **Benchmark** · 静态及事件数据、不同架构和替代梯度。
- **关键结果 / 消融** · 作者报告稳健性改善。
- **适用条件 / 局限** · 阈值窄区仍对梯度重要。

**可复用机制** · 稳健训练时同时记录决策翻转和可训练性。

<a id="paper-150011"></a>

## Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection

[官方论文页](https://neurips.cc/virtual/2026/poster/150011) · [作者来源](https://openreview.net/forum?id=lRXaR6ES4t)

- **问题 / 瓶颈** · 高分模型可能有高度相关的错误。
- **核心创新 / 方法** · 用标签与集成预测的互信息贪心选模型，并以高斯 copula 分析误差下限。
- **Baseline** · 相同查询预算的强集成基线。
- **Benchmark** · MEDMCQA、MMLU、AG News、IMDB。
- **关键结果 / 消融** · 作者报告四组均优于对照。
- **适用条件 / 局限** · 依赖有代表性的校准标签。

**可复用机制** · 以边际信息增益对照单模型排序。

<a id="paper-153136"></a>

## Don't Discard Your Rollouts: Reusing Teacher RL Traces for Student Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/153136) · [作者来源](https://openreview.net/forum?id=Nc74o46L3Z)

- **问题 / 瓶颈** · 直接复用混有早期低质量和离策略轨迹。
- **核心创新 / 方法** · 按通过率组织课程并区分监督与偏好数据，以教师似然筛选。
- **Baseline** · 收敛教师重新生成数据及朴素轨迹复用。
- **Benchmark** · 推理蒸馏设置，具名基准待核。
- **关键结果 / 消融** · 作者观察朴素复用弱于标准 SFT，筛选后可有效复用。
- **适用条件 / 局限** · 依赖已存奖励和教师概率。

**可复用机制** · 把归档复用当成数据选择，并与重新生成对照。

<a id="paper-153913"></a>

## Don’t Learn What You Can Compute: Arithmetic Residual Blocks for Exact Arithmetic in Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/153913) · [作者来源](https://openreview.net/forum?id=HkTpQ00UDJ)

- **问题 / 瓶颈** · 模型自行拟合算术不稳定。
- **核心创新 / 方法** · 冻结整数计算和原骨干，仅训练门控注入与低秩输出适配。
- **Baseline** · 原 SmolLM2-360M。
- **Benchmark** · 三位数以内四则运算严格匹配。
- **关键结果 / 消融** · 新增训练参数 170 万，准确率超过 99.9%。
- **适用条件 / 局限** · 更长输入和其他计算的路由能力待核。

**可复用机制** · 对具有确定解的子任务，比较训练接口与直接拟合。

<a id="paper-152022"></a>

## Don’t Let Gains FADE: Breaking Down Policy Gradient Weights in RL

[官方论文页](https://neurips.cc/virtual/2026/poster/152022) · [作者来源](https://openreview.net/forum?id=W67QEDh87x)

- **问题 / 瓶颈** · 替换优势函数常同时改变多个训练变量。
- **核心创新 / 方法** · 分解正负更新质量，据此构造熵自适应优势。
- **Baseline** · 对称与非对称优势算法。
- **Benchmark** · 7B、32B 可验证任务；具体数据集待核。
- **关键结果 / 消融** · 作者报告对称方法较慢，FADE 改善速度与多样性折衷。
- **适用条件 / 局限** · 增益受训练预算及模型影响。

**可复用机制** · 固定梯度规模分别对照正负权重和问题采样。

<a id="paper-153320"></a>

## Don't Match the Noise: Distribution Matching under Unknown Measurement Error with an Audit Sample

[官方论文页](https://neurips.cc/virtual/2026/poster/153320) · [作者来源](https://openreview.net/forum?id=MCFiU6DNGg)

- **问题 / 瓶颈** · 测量噪声可能使 MMD 匹配测量伪差。
- **核心创新 / 方法** · 利用审计样本校正核估计，无需指定噪声模型。
- **Baseline** · 标准 MMD 及其他校正方法。
- **Benchmark** · 参数估计和无监督分布匹配。
- **关键结果 / 消融** · 随机审计条件下对 oracle 无偏；作者报告实验优于对照。
- **适用条件 / 局限** · 根号收敛依赖审计规模随数据增长。

**可复用机制** · 对齐分布前，保留随机真值子集并测校正估计方差。

<a id="paper-139366"></a>

## Don't Pause! Every prediction matters in a streaming video

[官方论文页](https://neurips.cc/virtual/2026/poster/139366) · [作者来源](https://openreview.net/forum?id=UYNq6gYxzq)

- **问题 / 瓶颈** · 固定视频暂停点漏掉无请求输出。
- **核心创新 / 方法** · SPOT-Bench 以主动多轮请求和 Timeliness-F1 评估整个流。
- **Baseline** · 固定时间点 VideoQA 与不同流式模型。
- **Benchmark** · 流式视频事件响应，测时间精度与覆盖。
- **关键结果 / 消融** · 作者发现约半数时间无需回复，训练静默又可能降低响应。
- **适用条件 / 局限** · 事件时限受产品场景影响。

**可复用机制** · 设定连续响应窗口和空白窗口，在相同延迟下比较策略。

<a id="paper-155562"></a>

## Don't Waste Population: Post-Anneal Refinement for Combinatorial Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/155562) · [作者来源](https://openreview.net/forum?id=4ewSWxLXWS)

- **问题 / 瓶颈** · 只精修最优副本浪费并行群体信息。
- **核心创新 / 方法** · 对优质整数候选做局部精修，再沿优质解间的路径检查中间状态。
- **Baseline** · PQQA 的单解精修。
- **Benchmark** · QUBO 与图着色。
- **关键结果 / 消融** · 崎岖多盆地问题改善，单盆地退化为原精修。
- **适用条件 / 局限** · 收益取决于候选多样性及额外预算。

**可复用机制** · 用固定后处理预算比较精修单解和复用优质群体。

<a id="paper-153452"></a>

## Dooly: Configuration-Agnostic, Redundancy-Aware Profiling for LLM Inference Simulation

[官方论文页](https://neurips.cc/virtual/2026/poster/153452) · [作者来源](https://openreview.net/forum?id=LBbB4IGtB6)

- **问题 / 瓶颈** · 配置变化触发大量重复剖析。
- **核心创新 / 方法** · 追踪输入维度来源，只测延迟库未覆盖的操作。
- **Baseline** · 按配置重新剖析的模拟器。
- **Benchmark** · LLM 推理配置搜索；量化指标待核。
- **关键结果 / 消融** · 作者报告可跨配置复用性能测量。
- **适用条件 / 局限** · 依赖能隔离操作和服务状态。

**可复用机制** · 为性能样本建立结构化缓存键并报告配置覆盖。

<a id="paper-139569"></a>

## Doomed to Re-Annotate, Forever: The ImageNet Story

[官方论文页](https://neurips.cc/virtual/2026/poster/139569) · [作者来源](https://openreview.net/forum?id=HvYVosmFBa)

- **问题 / 瓶颈** · 单标签 ImageNet 可能错标或漏标。
- **核心创新 / 方法** · 重新标注并加定位与属性，审计衍生测试集。
- **Baseline** · 原 ImageNet-1k 验证集。
- **Benchmark** · ReImageNet，多标签、标注一致性与 top-1。
- **关键结果 / 消融** · 原标签约 13% 错误，32.7% 图像含多标签；改标后评分变化因模型而异。
- **适用条件 / 局限** · 新标注规则也影响可比性。

**可复用机制** · 同一模型保留新旧标签双评估，按漏标与错标拆解结果。

<a id="paper-153949"></a>

## D-OPSD: On-Policy Self-Distillation for Continuously Tuning Step-Distilled Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153949) · [作者来源](https://openreview.net/forum?id=HM5bMcRfJ3)

- **问题 / 瓶颈** · 常规微调容易损害少步扩散能力。
- **核心创新 / 方法** · 同一模型按纯文本和图文条件分成学生与教师，在学生轨迹上匹配分布。
- **Baseline** · 常规监督微调及原少步模型。
- **Benchmark** · 少步图像生成持续微调；具名基准待核。
- **关键结果 / 消融** · 作者提出维持少步能力的自蒸馏；数值待核。
- **适用条件 / 局限** · 依赖编码器的图文条件能力。

**可复用机制** · 固定采样步数，同时测新任务适配与原模型能力。

<a id="paper-154440"></a>

## DORA: A Scalable Asynchronous Reinforcement Learning System for Language Model Training

[官方论文页](https://neurips.cc/virtual/2026/poster/154440) · [作者来源](https://openreview.net/forum?id=DXbHLaGcFU)

- **问题 / 瓶颈** · 单版本 rollout 让长序列阻塞训练。
- **核心创新 / 方法** · 按版本动态分配资源，解除轨迹完成与批次边界绑定，并在同版本迁移缓存。
- **Baseline** · 单版本、部分 rollout 和副本方案。
- **Benchmark** · LLM 异步 RL，关注长尾和吞吐。
- **关键结果 / 消融** · 作者报告改善调度折衷，规模和幅度待核。
- **适用条件 / 局限** · 需要版本追踪及可迁移的状态。

**可复用机制** · 同时测吞吐、长轨迹保留和策略陈旧度。

<a id="paper-153848"></a>

## Do Robust LVLMs Hallucinate More? Uncovering Robustness-Induced Hallucination in Large Vision-Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153848) · [作者来源](https://openreview.net/forum?id=IINybdEu78)

- **问题 / 瓶颈** · 抗扰增强可能降低图像忠实度
- **核心创新 / 方法** · 测视觉 token 相似度并修正解码隐藏态
- **Baseline** · 鲁棒骨干及既有幻觉缓解法
- **Benchmark** · CHAIR、POPE、AMBER 等五套基准
- **关键结果 / 消融** · CHAIR_S 平均降 31.3 点，POPE 升 2.6 点
- **适用条件 / 局限** · 限于受测鲁棒骨干

**可复用机制** · 联合报告抗扰和图像事实性

<a id="paper-152493"></a>

## Do Sparse Autoencoders Learn Meaningful Concept Hierarchies?

[官方论文页](https://neurips.cc/virtual/2026/poster/152493) · [作者来源](https://openreview.net/forum?id=ShTEtBuHeA)

- **问题 / 瓶颈** · 定性示例难比较层级
- **核心创新 / 方法** · 从分类学提炼泛化和特化评价条件
- **Baseline** · 现有视觉 SAE
- **Benchmark** · 视觉特征层级
- **关键结果 / 消融** · 软硬吸收均降低质量
- **适用条件 / 局限** · 语言迁移待核

**可复用机制** · 兼测父子关系与特征吸收

<a id="paper-150945"></a>

## Do Thinking Tokens Help with Safety?

[官方论文页](https://neurips.cc/virtual/2026/poster/150945) · [作者来源](https://neurips.cc/virtual/2026/poster/150945)

- **问题 / 瓶颈** · 额外思考未必改变决策
- **核心创新 / 方法** · 比较思考进度与最终行为，同时测正常帮助性
- **Baseline** · GPT-OSS、Phi、OLMo、Qwen
- **Benchmark** · 拒答和正常提示帮助性
- **关键结果 / 消融** · 后段思考少改决定，部分干预损害正常帮助性
- **适用条件 / 局限** · 依赖模型和任务

**可复用机制** · 安全回归双测误合规和过拒

<a id="paper-155336"></a>

## Do We Need Asynchronous SGD? On the Near-Optimality of Synchronous Methods

[官方论文页](https://neurips.cc/virtual/2026/poster/155336) · [作者来源](https://openreview.net/forum?id=6NIyk8iU5e)

- **问题 / 瓶颈** · 异质环境可能无需异步开销
- **核心创新 / 方法** · 分析随机计算时间与部分参与下同步及备用工人变体
- **Baseline** · 异步优化、同步 SGD
- **Benchmark** · 理论时间复杂度和最优界
- **关键结果 / 消融** · 多个条件下同步仅差对数因子
- **适用条件 / 局限** · 部分设置仍需异步

**可复用机制** · 按达到目标精度的时间选更新方式

<a id="paper-153340"></a>

## Do We Really Need Diffusion for Generative Object Detection? A Minimal Prototype Perspective

[官方论文页](https://neurips.cc/virtual/2026/poster/153340) · [作者来源](https://openreview.net/forum?id=M42HRdwz6B)

- **问题 / 瓶颈** · 扩散组件收益混杂
- **核心创新 / 方法** · 逐组件干预 DiffusionDet，并构造线性加噪去噪基线
- **Baseline** · DiffusionDet
- **Benchmark** · COCO、零样本 CrowdHuman
- **关键结果 / 消融** · COCO 可比，稀疏候选和迁移更稳
- **适用条件 / 局限** · 限于所测结构

**可复用机制** · 用最小线性过程检查生成机制的必要性

<a id="paper-155908"></a>

## Do You CARE to Generalize? Extracting Robust Concept Directions from LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/155908) · [作者来源](https://neurips.cc/virtual/2026/poster/155908)

- **问题 / 瓶颈** · 环境差异既可能是伪相关也可能是概念信号
- **核心创新 / 方法** · 联合学习不变方向和正交环境残差
- **Baseline** · 现有方向提取方法
- **Benchmark** · 主谓一致等跨环境测量任务
- **关键结果 / 消融** · 未见环境测量更可靠
- **适用条件 / 局限** · 需环境标签并依赖线性表示

**可复用机制** · 用跨环境测试判断不变性是否丢失有效信号

<a id="paper-152718"></a>

## D-PACE: Dynamic Position-Aware Cross-Entropy for Parallel Speculative Drafting

[官方论文页](https://neurips.cc/virtual/2026/poster/152718) · [作者来源](https://openreview.net/forum?id=QrjZX92zUN)

- **问题 / 瓶颈** · 固定权重忽略瓶颈移动
- **核心创新 / 方法** · 从期望接受块长度导出位置交叉熵权重
- **Baseline** · 固定权重草稿器
- **Benchmark** · 多基准接收长度和实际加速
- **关键结果 / 消融** · 作者报告均提升，幅度待核
- **适用条件 / 局限** · 依赖验证配置

**可复用机制** · 把可接受位置的边际收益纳入草稿训练

<a id="paper-149051"></a>

## DP-EGGROLL: Centered Fitness-Vector Privatization for Backprop-Free Differentially Private Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/149051) · [作者来源](https://openreview.net/forum?id=tEkMApJftN)

- **问题 / 瓶颈** · 共模分量占用裁剪预算
- **核心创新 / 方法** · 先中心化后裁剪，聚合加噪
- **Baseline** · DP-AdamW、DP-ZO、不中心化版本
- **Benchmark** · 十个表格集、五种预算，测 AUROC 与 RMSE
- **关键结果 / 消融** · 分类 22/25 可比 DP-AdamW，中心化改善全部分类指标
- **适用条件 / 局限** · 单次隐私会计不覆盖多配置调参

**可复用机制** · 固定隐私预算测试去公共偏移的独立作用

<a id="paper-150092"></a>

## DPPE: Rethinking Camera-Based Positional Encoding for Scaling Multi-View Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/150092) · [作者来源](https://openreview.net/forum?id=kkycDUosSc)

- **问题 / 瓶颈** · 共用维度使位姿因素难独立辨识
- **核心创新 / 方法** · 解耦多视角注意力相机位姿编码
- **Baseline** · 现有相对相机编码
- **Benchmark** · 新视角合成与变焦、视角数外推
- **关键结果 / 消融** · 训练更稳定且外推更好
- **适用条件 / 局限** · 依赖相机和场景分布

**可复用机制** · 训练停滞时检查位姿因素可辨识性

<a id="paper-148680"></a>

## dRAE: Representation Autoencoder with Hyper-Spherical Codes

[官方论文页](https://neurips.cc/virtual/2026/poster/148680) · [作者来源](https://openreview.net/forum?id=vrjQMuRQQi)

- **问题 / 瓶颈** · 欧氏距离受各向异性尺度支配
- **核心创新 / 方法** · 超球面量化解耦幅值和方向
- **Baseline** · 现有欧氏码本方法
- **Benchmark** · 重建、视觉理解与生成
- **关键结果 / 消融** · 码本增至 131072 仍报告增益
- **适用条件 / 局限** · 依赖预训练特征的方向质量

**可复用机制** · 同时检查码字利用率和语义

<a id="paper-149812"></a>

## DRAMA: Dissecting Attention Redundancy for Accelerating Multimodal Diffusion Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149812) · [作者来源](https://openreview.net/forum?id=nAlvbSXW7z)

- **问题 / 瓶颈** · 长序列反复去噪计算昂贵
- **核心创新 / 方法** · 按空间注意力剪枝，按时序稳定性早停
- **Baseline** · 固定 token 和固定去噪步数
- **Benchmark** · 六个视觉语言基准
- **关键结果 / 消融** · 摘要报告平均加速 18.67 倍且精度有竞争力
- **适用条件 / 局限** · 稳定未必意味着难例已充分推理

**可复用机制** · 分别消融剪枝与早停并测长尾错误

<a id="paper-155776"></a>

## Drift Flow Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/155776) · [作者来源](https://openreview.net/forum?id=2yXRWyxBfG)

- **问题 / 瓶颈** · 一步漂移模型难用额外计算改善样本
- **核心创新 / 方法** · 结合直接漂移映射与可迭代流生成
- **Baseline** · 一步漂移和多步流匹配
- **Benchmark** · 多任务、多数据集；详细协议待核
- **关键结果 / 消融** · 作者报告一步有效且可以多步精修，曲线待核
- **适用条件 / 局限** · 各任务的额外步数收益待核

**可复用机制** · 按相同采样成本绘制单步和多步质量曲线。

<a id="paper-151871"></a>

## Drifting Field Policy: Wasserstein Gradient Flow on Policy Space for Offline-to-Online RL

[官方论文页](https://neurips.cc/virtual/2026/poster/151871) · [作者来源](https://openreview.net/forum?id=XGZrKnM8Qo)

- **问题 / 瓶颈** · 离线到在线适配需提升价值又保持已有行为先验
- **核心创新 / 方法** · 将更新写成反向 KL 的 Wasserstein 梯度流，使用评论家筛选动作形成可计算代理
- **Baseline** · 基于 ODE 的生成策略
- **Benchmark** · Robomimic、OGBench 操作任务
- **关键结果 / 消融** · 作者报告多任务上一步推理优于 ODE 策略
- **适用条件 / 局限** · 依赖评论家的排序准确性

**可复用机制** · 以固定推理预算比较不同锚定强度下的价值和行为保持。

<a id="paper-155051"></a>

## Drifting Fields are not Conservative

[官方论文页](https://neurips.cc/virtual/2026/poster/155051) · [作者来源](https://openreview.net/forum?id=8pC5fd3IzY)

- **问题 / 瓶颈** · 位置相关归一化一般使漂移场无法写成梯度
- **核心创新 / 方法** · 导出高斯径向核例外，构造尖锐核归一化获得标量势
- **Baseline** · 原始漂移目标和高斯归一化
- **Benchmark** · 理论均衡识别与生成性能对照，数据集待核
- **关键结果 / 消融** · 作者报告新归一化保持原目标性能
- **适用条件 / 局限** · 结论围绕径向核与指定归一化

**可复用机制** · 修改生成向量场时检查可积性与均衡点，而后决定是否直接优化标量势。

<a id="paper-152901"></a>

## Drift Q-Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/152901) · [作者来源](https://openreview.net/forum?id=PZBv14gx3M)

- **问题 / 瓶颈** · 分布外价值不可靠，迭代生成的动作推理昂贵
- **核心创新 / 方法** · 以漂移项维持行为支持及多模态，评论家推动价值改善
- **Baseline** · 扩散和流策略
- **Benchmark** · D4RL、OGBench，另测低质量数据
- **关键结果 / 消融** · 作者报告干净与退化数据下均表现稳健
- **适用条件 / 局限** · 依赖行为数据覆盖及价值估计

**可复用机制** · 同时测一步策略的动作覆盖、低质量数据鲁棒性及决策延迟。

<a id="paper-149468"></a>

## Drift-Resistant Navigation World Model with Anchored Epipolar Guidance

[官方论文页](https://neurips.cc/virtual/2026/poster/149468) · [作者来源](https://openreview.net/forum?id=psmFTmu8nE)

- **问题 / 瓶颈** · 逐帧递推易积累视觉与几何漂移
- **核心创新 / 方法** · 锚帧作为分段生成的未来条件，并以双向极线几何约束对应位置
- **Baseline** · 逐帧递推世界模型，具名对照待核
- **Benchmark** · 四个基准的长程画质、几何与规划表现
- **关键结果 / 消融** · 作者报告固定规划器下规划表现改善
- **适用条件 / 局限** · 依赖锚预测与相机几何

**可复用机制** · 保持规划器不变，比较锚引导补帧和自由递推。

<a id="paper-148289"></a>

## DRILL: Training World Models to Improve Policies, Not Predict Pixels

[官方论文页](https://neurips.cc/virtual/2026/poster/148289) · [作者来源](https://openreview.net/forum?id=yy2Wa09ZfU)

- **问题 / 瓶颈** · 像素预测更准未必产生更好的策略梯度
- **核心创新 / 方法** · 双层优化让内层 GRPO 使用想象数据，外层根据策略回报更新环境模型
- **Baseline** · WMPO、RLVR-World
- **Benchmark** · 五个操作模拟器和两个 VLA 骨干，测成功率
- **关键结果 / 消融** · 相较两种对照分别提高 13.1 和 7.9 个百分点，尽管像素误差可高 17%
- **适用条件 / 局限** · 实验证据限模拟，代理理论依赖局部假设

**可复用机制** · 同时记录预测误差和通过该模型训练的策略改善。

<a id="paper-151453"></a>

## DRIVE: Fine-tuning via Data Contribution- and Diversity-aware Weighting with Prior Regularization

[官方论文页](https://neurips.cc/virtual/2026/poster/151453) · [作者来源](https://openreview.net/forum?id=aZomMEAGSq)

- **问题 / 瓶颈** · 常见微调权重偏向单侧目标
- **核心创新 / 方法** · 以 Shapley 分解区分两项贡献，以协方差多样性和样本先验调整权重
- **Baseline** · 既有样本重加权方法，名称待核
- **Benchmark** · 微调表现、收敛和稳健性，任务待核
- **关键结果 / 消融** · 作者报告理论保证与整体改善，量化待核
- **适用条件 / 局限** · 对贡献代理和先验质量敏感

**可复用机制** · 在同预算下分别报告旧知识保持和新任务适配。

<a id="paper-149040"></a>

## DriveFuture: Future-Aware Latent World Models for Autonomous Driving

[官方论文页](https://neurips.cc/virtual/2026/poster/149040) · [作者来源](https://openreview.net/forum?id=tITD5xFjY8)

- **问题 / 瓶颈** · 仅以未来状态作辅助目标容易让规划忽略预测
- **核心创新 / 方法** · 训练以真值未来潜状态通过跨注意力细化，推理改用预测潜状态
- **Baseline** · 既有驾驶潜世界模型，具名对照待核
- **Benchmark** · NAVSIM v2 navhard、navtest 与 v1 navtest
- **关键结果 / 消融** · 报告 EPDMS 55.5、89.9 和 PDMS 90.7
- **适用条件 / 局限** · 训练和推理条件存在分布差异

**可复用机制** · 固定预测器，比较未来潜状态直接条件化与仅辅助监督。

<a id="paper-155869"></a>

## DriveMind: Mind-Evolving Belief Tracking for Closed-Loop Autonomous Driving

[官方论文页](https://neurips.cc/virtual/2026/poster/155869) · [作者来源](https://openreview.net/forum?id=2Hd1h7AQap)

- **问题 / 瓶颈** · 逐帧重新选择单一解释易在歧义场景锁定错误
- **核心创新 / 方法** · 传播、打分和重采样场景假设
- **Baseline** · 逐帧基线
- **Benchmark** · Bench2Drive，驾驶分与成功率
- **关键结果 / 消融** · 驾驶分 71.36 到 81.37，成功率 45.45% 到 54.09%
- **适用条件 / 局限** · 计算开销与假设质量待核

**可复用机制** · 固定推理预算比较单解释和多假设跟踪。

<a id="paper-139662"></a>

## DriveStreamBench: Evaluating User-Conditioned Watch-and-Notify in Streaming Driving Video

[官方论文页](https://neurips.cc/virtual/2026/poster/139662) · [作者来源](https://openreview.net/forum?id=CBbit0ejvP)

- **问题 / 瓶颈** · 离线识别表现无法反映因果流式告警能力
- **核心创新 / 方法** · 以同一批驾驶事件构建四层用户条件提醒评测
- **Baseline** · 多种 VLM 与 DriveStream-SFT
- **Benchmark** · DriveStreamBench，因果驾驶视频与用户条件
- **关键结果 / 消融** · 作者报告所有评估模型仍有明显不足，分项数值待核
- **适用条件 / 局限** · 场景局限于驾驶，误报时延协议待核

**可复用机制** · 为持续监控任务联合测漏报、误报和延迟。

<a id="paper-152058"></a>

## Drive vs. Decay: On the Training Dynamics of Joint-Embedding Predictive Architectures

[官方论文页](https://neurips.cc/virtual/2026/poster/152058) · [作者来源](https://openreview.net/forum?id=VofFK184SY)

- **问题 / 瓶颈** · JEPA 的防塌缩经验缺统一解释。
- **核心创新 / 方法** · 在线性化梯度流中比较逐模态驱动与衰减，并将预测器注意力初始化偏向恒等。
- **Baseline** · 常规 JEPA 预测器与不同掩码、缩放和 EMA 配置。
- **Benchmark** · 800 多种表格配置，以及 CIFAR-10、CIFAR-100 和 STL-10 上的 I-JEPA。
- **关键结果 / 消融** · 摘要报告验证了相边界，并改善有效秩和下游准确率。
- **适用条件 / 局限** · 理论针对训练早期及近似谱解耦。

**可复用机制** · 同时记录模态稳定比与有效秩，验证改动是否通过理论预期的方向起效。

<a id="paper-139692"></a>

## Driving on Memory

[官方论文页](https://neurips.cc/virtual/2026/poster/139692) · [作者来源](https://openreview.net/forum?id=AN8g1p8PlR)

- **问题 / 瓶颈** · 高分可能来自路况和地点先验。
- **核心创新 / 方法** · 保持历史地点信息而去掉当前交通参与者等动态观测。
- **Baseline** · 有实时相机输入的端到端规划方法。
- **Benchmark** · NAVSIM 和 Bench2Drive，比较基准规划分。
- **关键结果 / 消融** · 历史记忆在 NAVSIM 接近或超过领先方法，在 Bench2Drive 明显落后。
- **适用条件 / 局限** · 两基准的结果不能直接推广至真实驾驶。

**可复用机制** · 在声称模型理解动态场景前做保持静态结构的观测替换实验。

<a id="paper-151327"></a>

## Dr. MAS: Stable Reinforcement Learning for Multi-Agent LLM Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/151327) · [作者来源](https://openreview.net/forum?id=bLgNMclTCO)

- **问题 / 瓶颈** · GRPO 全局归一化会使角色间梯度尺度失衡。
- **核心创新 / 方法** · 用各智能体自己的奖励统计归一化，并共享调度训练资源。
- **Baseline** · 全局归一化的组相对优化；具名比较待核。
- **Benchmark** · Qwen2.5 与 Qwen3 的多智能体数学推理和多轮搜索。
- **关键结果 / 消融** · 作者报告训练稳定性改善，定量与独立消融待核。
- **适用条件 / 局限** · 每角色须有足量奖励样本。

**可复用机制** · 记录各角色梯度范数，用同预算比较共享与按角色优势归一化。

<a id="paper-154924"></a>

## DROGO: Default Representation Objective via Graph Optimization in Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/154924) · [作者来源](https://openreview.net/forum?id=9xEDvoOSsg)

- **问题 / 瓶颈** · 构造完整默认表示矩阵再分解成本高。
- **核心创新 / 方法** · 用神经网络以转移数据拟合默认表示主特征向量。
- **Baseline** · 先近似默认表示矩阵再做特征分解。
- **Benchmark** · 多个环境与奖励塑形用例；名称和指标待核。
- **关键结果 / 消融** · 作者报告近似有效并展示奖励塑形。
- **适用条件 / 局限** · 仅直接学习主向量，覆盖不足下的偏差待核。

**可复用机制** · 只需主谱方向时对照隐式优化和显式矩阵分解。

<a id="paper-152246"></a>

## DropKV: Decoupling Residual-Output Perturbation for Near-Optimal KV-Cache Eviction

[官方论文页](https://neurips.cc/virtual/2026/poster/152246) · [作者来源](https://openreview.net/forum?id=UVbaJoD3Qa)

- **问题 / 瓶颈** · 联合选择难优化，注意力分数不能充分反映输出影响。
- **核心创新 / 方法** · 将联合扰动问题拆成独立 token 评分，并用融合算子避免构建完整注意力矩阵。
- **Baseline** · 等缓存预算下的 KV 淘汰方法。
- **Benchmark** · RULER、LongBench 与三种长上下文模型。
- **关键结果 / 消融** · 评分算子提速 19.8 倍，匹配批量的预填充最多提速 9.9%。
- **适用条件 / 局限** · 近似保证依赖锥条件。

**可复用机制** · 同时测评分成本和端到端提速，并检查近似条件是否成立。

<a id="paper-151942"></a>

## DrPO: Drifting Preference Optimization for One-Step Generative Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151942) · [作者来源](https://openreview.net/forum?id=WfyzQahi56)

- **问题 / 瓶颈** · 单步生成同时兼顾效率、外部奖励兼容性与多样性较难。
- **核心创新 / 方法** · 以目标奖励判别正负在线样本，从潜特征构造偏好漂移场。
- **Baseline** · 单步生成偏好微调对照；名称待核。
- **Benchmark** · SD-Turbo、SDXL-Turbo，含 HPSv3、GenEval。
- **关键结果 / 消融** · 摘要报告有效在线微调，离线扩展属初步证据。
- **适用条件 / 局限** · 依赖正负样本的覆盖和奖励可靠性。

**可复用机制** · 固定奖励模型用样本估计更新，对照直接奖励梯度并单列多样性。

<a id="paper-150625"></a>

## DRScaffold: Boosting Dense-Scene Reasoning in Lightweight Vision Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150625) · [作者来源](https://openreview.net/forum?id=ghD19TF2Bx)

- **问题 / 瓶颈** · 密集场景中流畅的推理可能缺少实体关系支撑。
- **核心创新 / 方法** · 在监督微调中加入四阶段目标，无需改模型架构。
- **Baseline** · 冻结大模型与三种轻量 VLM 的原始配置。
- **Benchmark** · DRBench 含 2943 张图和 14573 道题，并测通用基准。
- **关键结果 / 消融** · 微调后的 Qwen2.5-VL-3B 在 DRBench 超过冻结的 32B。
- **适用条件 / 局限** · 结论限于评测所用任务，训练预算细节待核。

**可复用机制** · 在难场景把视觉定位与后续推理分别监督和评测。

<a id="paper-150894"></a>

## DSAQuant: Denoising-Stage-Aligned Quantization-Aware Training for Video Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/150894) · [作者来源](https://openreview.net/forum?id=ed33sAgUBp)

- **问题 / 瓶颈** · 跨步统一量化监督容易损失后期高频细节。
- **核心创新 / 方法** · 早期蒸馏保全局结构，后期转向目标驱动的细节重建，并按阶段门控。
- **Baseline** · 与不区分去噪步的量化训练比较。
- **Benchmark** · 文本到视频量化，比较整体结构、细节和计算开销。
- **关键结果 / 消融** · 摘要报告阶段对齐改善保真，数值待核。
- **适用条件 / 局限** · 阶段职责可能随采样器和模型变化。

**可复用机制** · 消融不同时间段的量化损失，分别测结构和纹理。

<a id="paper-154766"></a>

## DSBTR: A Diffusion Schrödinger Bridge Trajectory Refiner for Multi-Agent Trajectory Prediction

[官方论文页](https://neurips.cc/virtual/2026/poster/154766) · [作者来源](https://openreview.net/forum?id=B68WLZ0xU0)

- **问题 / 瓶颈** · 训练使用加噪起点而推理从无噪先验开始，精修可能反而退化。
- **核心创新 / 方法** · 用双端约束薛定谔桥对齐确定性先验，并推导高阶求解器。
- **Baseline** · 多种原始预测器及扩散精修路线。
- **Benchmark** · ETH/UCY 和 SDD 的多主体轨迹预测。
- **关键结果 / 消融** · 作者报告多种底座精度改善并避免负优化，幅度待核。
- **适用条件 / 局限** · 依赖粗预测优先覆盖正确模式。

**可复用机制** · 把训练终点和线上输入分布对齐，专门统计精修后变差的样本。

<a id="paper-151450"></a>

## DSSP: Diffusion State Space Policy  with Hierarchical Full-History Conditioning

[官方论文页](https://neurips.cc/virtual/2026/poster/151450) · [作者来源](https://openreview.net/forum?id=aaSIMuY19G)

- **问题 / 瓶颈** · 短历史窗口无法消解长期任务歧义。
- **核心创新 / 方法** · 用状态空间模型编码全历史，与近期状态分层融合，再做扩散动作生成。
- **Baseline** · 当前观测或短窗口条件扩散策略。
- **Benchmark** · 仿真及真机操作任务。
- **关键结果 / 消融** · 摘要报告较小模型获得较强表现，细项待核。
- **适用条件 / 局限** · 压缩状态可能丢失极早的罕见事件。

**可复用机制** · 比较等计算长短历史，并单独测依赖较早观测的任务。

<a id="paper-151540"></a>

## Dual Dimensionality for Local and Global Attention

[官方论文页](https://neurips.cc/virtual/2026/poster/151540) · [作者来源](https://openreview.net/forum?id=Zujn6IDCvy)

- **问题 / 瓶颈** · 统一维度忽略注意力距离差异
- **核心创新 / 方法** · 保留近期 token 完整维度，压缩远程表示
- **Baseline** · 全维和统一低维
- **Benchmark** · 70M 至 410M 预训练及 1B 级继续微调
- **关键结果 / 消融** · 远距可降至四分之一并接近全维，统一压缩较差
- **适用条件 / 局限** · 超长检索及实际缓存成本待核

**可复用机制** · 在同一缓存预算下比较距离感知分配与均匀压缩。

<a id="paper-154664"></a>

## DualDrift: Combining Forward and Reverse Drifts for One-Step Generative Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/154664) · [作者来源](https://openreview.net/forum?id=BxHttc1DET)

- **问题 / 瓶颈** · 仅从生成端估计漂移会漏用数据
- **核心创新 / 方法** · 结合正向和反向漂移，以批统计自动平衡
- **Baseline** · 标准 Drifting Models
- **Benchmark** · ImageNet 256，FID 和 Inception Score
- **关键结果 / 消融** · 报告收敛更快、两项指标改善
- **适用条件 / 局限** · 正向项单用可能偏向主模态

**可复用机制** · 对照双向修正及任一单向修正。

<a id="paper-153289"></a>

## Dual-Granularity Learning for Regression with Continuous Noisy Labels

[官方论文页](https://neurips.cc/virtual/2026/poster/153289) · [作者来源](https://openreview.net/forum?id=MNQLeuQSPM)

- **问题 / 瓶颈** · 离群标签不宜用于精确残差拟合
- **核心创新 / 方法** · 实例辅助残差、分箱对比约束与直方图桥接
- **Baseline** · 噪声回归对照待核
- **Benchmark** · 多种噪声条件下的回归
- **关键结果 / 消融** · 作者报告鲁棒性和泛化改善
- **适用条件 / 局限** · 分箱及噪声分布敏感性待核

**可复用机制** · 分别测试小误差纠正和大误差下的序结构保留。

<a id="paper-148859"></a>

## Duality Models: An Embarrassingly Simple One-step Generation Paradigm

[官方论文页](https://neurips.cc/virtual/2026/poster/148859) · [作者来源](https://openreview.net/forum?id=udpOHslgqs)

- **问题 / 瓶颈** · 将单步与多步训练目标分开会争夺预算
- **核心创新 / 方法** · 共享骨干的双头同时预测局部速度和全局流映射
- **Baseline** · MeanFlow、Shortcut 为方法对照
- **Benchmark** · ImageNet 256
- **关键结果 / 消融** · 679M DiT 双步 FID 1.79
- **适用条件 / 局限** · 需匹配模型与预算比较

**可复用机制** · 在固定训练样本下对照双头同时监督与分时监督。

<a id="paper-148696"></a>

## DualKV: Shared-Prompt Flash Attention for Efficient RL Training with Large Rollouts and Long Contexts

[官方论文页](https://neurips.cc/virtual/2026/poster/148696) · [作者来源](https://openreview.net/forum?id=viyAwqIA4H)

- **问题 / 瓶颈** · 同提示多次采样导致前缀计算和显存重复
- **核心创新 / 方法** · 融合共享区和响应区注意力，重排微批次，保持数学等价
- **Baseline** · FlashAttention
- **Benchmark** · Qwen3-8B GRPO/DAPO、30B MoE
- **关键结果 / 消融** · 8B GRPO 更新加速 1.63–2.10 倍，30B 端到端步耗时加速 3.38 倍
- **适用条件 / 局限** · 收益依赖公共前缀长度和采样数

**可复用机制** · 先测重复前缀占比，再选择共享内核。

<a id="paper-154151"></a>

## Dual-Pathway Circuits of Object Hallucination in Vision-Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154151) · [作者来源](https://openreview.net/forum?id=FrVqkZPNVv)

- **问题 / 瓶颈** · 相关性不足以解释错误对象输出
- **核心创新 / 方法** · 对五类模型做激活替换、条件路径分析和有针对性的抑制
- **Baseline** · 无干预模型和不同幻觉类型
- **Benchmark** · POPE-adversarial、AMBER
- **关键结果 / 消融** · 作者报告对象幻觉最多下降 76%，干预对关系幻觉有迁移
- **适用条件 / 局限** · 属性幻觉未显示相同迁移

**可复用机制** · 跨错误类型验证机制，而非把同一诊断泛化到所有幻觉。

<a id="paper-149934"></a>

## Dual-Rate Diffusion: Accelerating diffusion models with an interleaved heavy-light network

[官方论文页](https://neurips.cc/virtual/2026/poster/149934) · [作者来源](https://openreview.net/forum?id=m5HuTuCJy2)

- **问题 / 瓶颈** · 每步重复重网络计算导致采样昂贵
- **核心创新 / 方法** · 低频提取上下文，每步由轻网络复用它
- **Baseline** · 标准扩散及蒸馏组合
- **Benchmark** · ImageNet
- **关键结果 / 消融** · 质量可比，计算成本降至二分之一至四分之一
- **适用条件 / 局限** · 实际速度取决于硬件与缓存

**可复用机制** · 扫描上下文更新频率并监控质量退化点。

<a id="paper-150002"></a>

## Dual-Space Preconditioning for Variational Inequalities and Root-Finding Problems

[官方论文页](https://neurips.cc/virtual/2026/poster/150002) · [作者来源](https://openreview.net/forum?id=lVWwGH1DGX)

- **问题 / 瓶颈** · 经典余强单调和 Lipschitz 假设限制应用
- **核心创新 / 方法** · 建立放宽条件及确定性、随机收敛分析
- **Baseline** · 固定步长经典法及增长条件分析
- **Benchmark** · 变分不等式与根查找理论设定
- **关键结果 / 消融** · 等向预条件得到可变步长方法和更大允许范围
- **适用条件 / 局限** · 实际收敛依赖算子满足文中条件

**可复用机制** · 用算子条件指导步长和度量选择。

<a id="paper-151136"></a>

## DUDS: Dual-stage Data Selection for Efficient Reinforcement Learning with Verifiable Rewards

[官方论文页](https://neurips.cc/virtual/2026/poster/151136) · [作者来源](https://openreview.net/forum?id=cjuhKXBKYF)

- **问题 / 瓶颈** · 静态筛选不随训练变化，在线额外采样昂贵
- **核心创新 / 方法** · 离线联合质量和多样性，在线用后验成功率与新鲜度调整
- **Baseline** · 离线及在线数据筛选
- **Benchmark** · 四个推理基准
- **关键结果 / 消融** · 报告以较少数据和计算取得有竞争力表现
- **适用条件 / 局限** · 依赖可验证奖励，配置待核

**可复用机制** · 比较固定数据池与复用已有采样的动态筛选。

<a id="paper-153196"></a>

## DUET: Optimize Token-Budget Allocation for Reinforcement Learning with Verifiable Rewards

[官方论文页](https://neurips.cc/virtual/2026/poster/153196) · [作者来源](https://openreview.net/forum?id=N80WSnmidb)

- **问题 / 瓶颈** · 只调单一维度难提高单位 token 学习价值
- **核心创新 / 方法** · 先估计题目价值分配样本数，再按标记提前终止并重加权
- **Baseline** · 完整预算 GRPO 及三种预算对照
- **Benchmark** · Qwen3、Llama 的数学、代码与科学问答
- **关键结果 / 消融** · 报告加速 1.62 倍，半预算配置加速 2.51 倍
- **适用条件 / 局限** · 依赖停止标记和价值估计质量

**可复用机制** · 在共同预算下比较联合分配与单维度分配。

<a id="paper-151376"></a>

## DUST: Directional Uncertainty-aware and Scale-invariant Transfer Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151376) · [作者来源](https://openreview.net/forum?id=b3WKmq3X8i)

- **问题 / 瓶颈** · 源点估计无法传递方向不确定性
- **核心创新 / 方法** · 将源采样分布投影到单位球，以角锥先验收缩目标方向
- **Baseline** · 欧氏距离与角度点估计惩罚
- **Benchmark** · 模拟与 NHANES 高血压预测
- **关键结果 / 消融** · 源估计不确定且尺度失配时优势明显，幅度待核
- **适用条件 / 局限** · 假定源目标方向可共享

**可复用机制** · 固定目标样本量，扫描源估计方差和尺度比比较分布与点迁移。

<a id="paper-148139"></a>

## DyCoRM: Dynamic Criterion-Aware Reward Modeling for Text-to-Image Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/148139) · [作者来源](https://openreview.net/forum?id=zzottG3vbp)

- **问题 / 瓶颈** · 固定评分维度忽略用户的细粒度要求
- **核心创新 / 方法** · 显式定位任务标准，使用标准级注释训练偏好比较，并应用于候选选图
- **Baseline** · 通用静态奖励模型，具名对照待核
- **Benchmark** · DyCoDataset-20K 和 DyCoBench-1K
- **关键结果 / 消融** · 摘要给出动态标准评测与选图流程，量化结果待核
- **适用条件 / 局限** · 依赖标准注释和可靠的请求解析

**可复用机制** · 比较同批候选按统一量表与按请求量表排序，重点核查多约束请求。

<a id="paper-156115"></a>

## DyJR: Preserving Local Policy Plasticity in Reinforcement Learning with Verifiable Rewards via Dynamic Jensen-Shannon Replay

[官方论文页](https://neurips.cc/virtual/2026/poster/156115) · [作者来源](https://openreview.net/forum?id=0Go4KDhkDw)

- **问题 / 瓶颈** · 直接重用成功轨迹可能诱发模式坍塌
- **核心创新 / 方法** · 以先进先出和动态容量维护参考分布，用 JS 正则保留近期备选路径
- **Baseline** · GRPO、RLEP、Ex-GRPO
- **Benchmark** · 数学推理与 Text-to-SQL
- **关键结果 / 消融** · 作者报告效果提高、效率近似 GRPO，且头部 token 概率更少集中
- **适用条件 / 局限** · 参考分布随策略变化，缓存窗口敏感性待核

**可复用机制** · 固定采样预算对照直接回放和分布约束，观察备选路径概率。

<a id="paper-151075"></a>

## DynaFLIP: Rethinking Robotics Perception via Tri-Modal-Dynamics Guided Representation

[官方论文页](https://neurips.cc/virtual/2026/poster/151075) · [作者来源](https://openreview.net/forum?id=d8CUaJ56dY)

- **问题 / 瓶颈** · 静态图文编码难保留控制相关变化
- **核心创新 / 方法** · 用图像、语言与三维流三元组最小化共享球面单纯形体积，并加余弦及对比约束
- **Baseline** · 静态视觉及图文基线，名称待核
- **Benchmark** · 仿真和真机操作，含 VLA 与分布外设置
- **关键结果 / 消融** · 作者报告分布外增益最高 22.5%，口径待核
- **适用条件 / 局限** · 训练需三维流，推理只用图像

**可复用机制** · 在同一策略下切换编码器，测试运动监督能否改善对变化场景的适配。

<a id="paper-151637"></a>

## Dynamically Structured Diffusion Language Model Decoding via Bayesian Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/151637) · [作者来源](https://openreview.net/forum?id=Z6jLmoD11G)

- **问题 / 瓶颈** · 固定长度限制扩散语言模型，局部置信度缺乏结构
- **核心创新 / 方法** · 用贝叶斯后验调节扩张，以餐馆过程式分块并调度各块计算
- **Baseline** · 固定长度及可变长度解码
- **Benchmark** · 多个生成基准，名称与指标待核
- **关键结果 / 消融** · 作者报告质量与灵活性改善，幅度待核
- **适用条件 / 局限** · 结构先验与调度开销需验证

**可复用机制** · 以相同计算量分别消融长度选择、分块与排序。

<a id="paper-154443"></a>

## Dynamic Causal Structure Discovery for Autoregressive Visual Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/154443) · [作者来源](https://openreview.net/forum?id=DWFojJ4tLc)

- **问题 / 瓶颈** · 固定前缀同时引入冗余和遗漏依赖
- **核心创新 / 方法** · 用向量消融近似干预，由 Fisher 准则在推理时修正条件集合
- **Baseline** · 静态前缀自回归
- **Benchmark** · 视觉自回归生成，评测细节待核
- **关键结果 / 消融** · 作者报告质量和全局一致性改善
- **适用条件 / 局限** · 内部干预近似不等于真实因果识别

**可复用机制** · 比较固定和内容自适应条件，在等预算下分别测局部和全局质量。

<a id="paper-153747"></a>

## Dynamic Convolutions Improve Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/153747) · [作者来源](https://openreview.net/forum?id=J0j3wPpyop)

- **问题 / 瓶颈** · 静态短卷积表达能力有限
- **核心创新 / 方法** · 对查询、键和值应用动态短卷积，以专用内核减少开销
- **Baseline** · 标准 Transformer 和静态短卷积变体
- **Benchmark** · 联想回忆及 150M 至 2B 参数语言建模
- **关键结果 / 消融** · 缩放分析报告相对同参数标准架构约 1.33 倍算力优势
- **适用条件 / 局限** · 专用内核和规模区间影响效率

**可复用机制** · 对照静态与动态局部滤波，同时测回忆、建模损失和吞吐。

<a id="paper-155922"></a>

## Dynamic Delayed Tree Expansion For Improved Multi-Path Speculative Decoding

[官方论文页](https://neurips.cc/virtual/2026/poster/155922) · [作者来源](https://openreview.net/forum?id=1oCU9PKaoy)

- **问题 / 瓶颈** · 根部接受率提高不一定转化为吞吐改善
- **核心创新 / 方法** · 先草拟一段单路径，再分支并由神经选择器按上下文决定扩张
- **Baseline** · Traversal Verification、OT 验证及 SpecInfer
- **Benchmark** · 不同模型、任务和采样设置，测吞吐
- **关键结果 / 消融** · OT 方案平均比遍历高 5%，改进遍历平均提升 26%
- **适用条件 / 局限** · 依赖草稿和目标吻合度及选择器开销

**可复用机制** · 按树深记录接受率与耗时，以实测吞吐选择分支深度。

<a id="paper-155427"></a>

## Dynamic Expert Sharing: Decoupling Memory from Parallelism in Mixture-of-Experts Diffusion LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/155427) · [作者来源](https://openreview.net/forum?id=5jLBdUevsd)

- **问题 / 瓶颈** · 逐 token 路由使并行度增加时不同专家数膨胀
- **核心创新 / 方法** · 用区块级核心集选择满足整段 token 的专家集合
- **Baseline** · 原始 MoE 扩散模型及逐 token 跳过思路
- **Benchmark** · MoE 扩散模型的准确率、激活数、延迟
- **关键结果 / 消融** · 不同专家激活降低逾 55%，延迟最多降 38%，保留 99% 原准确率
- **适用条件 / 局限** · 收益取决于区块内需求共性和存储瓶颈

**可复用机制** · 固定准确率预算扫区块长度，对照逐 token 路由并测内存流量。

<a id="paper-153785"></a>

## Dynamic Latent Routing

[官方论文页](https://neurips.cc/virtual/2026/poster/153785) · [作者来源](https://openreview.net/forum?id=IgAxk6rEiw)

- **问题 / 瓶颈** · 预定义技能或独立训练代码可能难以组合
- **核心创新 / 方法** · 借子目标策略拼接的搜索原理，在一阶段内同时更新搜索路由与语言模型
- **Baseline** · 监督微调及其他离散潜变量方法
- **Benchmark** · 四个数据集、六种模型和六位整数运算机制分析
- **关键结果 / 消融** · 平均较监督微调高 6.6 个百分点，代码消融显示不同功能
- **适用条件 / 局限** · 低数据条件为主，代码可解释性未必跨任务

**可复用机制** · 用路由代码替换消融验证实际分工，并比较低数据适配效果。

<a id="paper-149280"></a>

## Dynamic Model Merging Made Slim

[官方论文页](https://neurips.cc/virtual/2026/poster/149280) · [作者来源](https://openreview.net/forum?id=rTNJl9wcz6)

- **问题 / 瓶颈** · 共享骨干与专家容量的固定比例浪费预算
- **核心创新 / 方法** · 用任务向量作为无数据监督进行可微秩优化，再短程精修
- **Baseline** · 已有动态合并方法
- **Benchmark** · 视觉、语言和多模态任务，比较表现与参数量
- **关键结果 / 消融** · 用单模型 1.24 倍参数达到既有基线，1.4 倍时超过
- **适用条件 / 局限** · 依赖可访问任务向量及分解质量

**可复用机制** · 在同一存储预算优化共享和私有秩，并记录任务间干扰。

<a id="paper-154422"></a>

## Dynamic Optimistic Constrained OCO with Memory via Delay Equivalence

[官方论文页](https://neurips.cc/virtual/2026/poster/154422) · [作者来源](https://openreview.net/forum?id=DhdcSBFGWf)

- **问题 / 瓶颈** · 带记忆和变化约束的在线优化难同时控制后悔和违规
- **核心创新 / 方法** · 用记忆到延迟的归约处理状态梯度，再纳入不可信预测做乐观更新
- **Baseline** · 既有带可分假设的方法及无记忆最优界
- **Benchmark** · 理论动态后悔和累计约束违规
- **关键结果 / 消融** · 界同时适应环境路径长度及预测准确度，完美预测下后悔常数级
- **适用条件 / 局限** · 违规界取决于路径长度是否已知；前提待核正文

**可复用机制** · 有状态在线决策可优先检查能否归约到延迟模型，再比较有无预测的保证。

<a id="paper-152814"></a>

## Dynamic Quadtree Tokenization for Autoregressive PDE Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/152814) · [作者来源](https://openreview.net/forum?id=QEBPUFXUHr)

- **问题 / 瓶颈** · 均匀网格浪费局部计算
- **核心创新 / 方法** · 小波启发的四叉树分块并在滚动时重网格
- **Baseline** · 均匀细网格骨干
- **Benchmark** · 均匀及自适应网格 PDE 滚动预测
- **关键结果 / 消融** · 匹配参数时自适应网格最细层误差降低
- **适用条件 / 局限** · 插值影响全域指标

**可复用机制** · 实验设计可对照按局部结构变化调整标记密度，并按均匀及自适应网格 PDE 滚动预测核查证据。

<a id="paper-154187"></a>

## Dynamic Query as Budgeting for Tiny Object Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/154187) · [作者来源](https://openreview.net/forum?id=FZOopPouyA)

- **问题 / 瓶颈** · 查询数量和选择逻辑的作用混杂
- **核心创新 / 方法** · 用编码器置信度估计预算并执行标准 Top-K
- **Baseline** · 动态查询检测器
- **Benchmark** · AI-TOD-v2、VisDrone、COCO
- **关键结果 / 消融** · AP 提升逾 0.5，查询约减半，推理约快四倍
- **适用条件 / 局限** · 依赖置信度反映密度

**可复用机制** · 实验设计可对照按密度调整查询数并固定选择规则，并按AI-TOD-v2、VisDrone、COCO核查证据。

<a id="paper-150727"></a>

## Dynamic Regret in Online Convex Optimization with Indicator Switching Costs

[官方论文页](https://neurips.cc/virtual/2026/poster/150727) · [作者来源](https://openreview.net/forum?id=frpCLd0FIr)

- **问题 / 瓶颈** · 静态对手保证无法直接推广
- **核心创新 / 方法** · 混合不同时间尺度的懒惰 FTRL，以最大耦合采样
- **Baseline** · 直接扩展静态技巧
- **Benchmark** · 在线凸优化理论，按对手切换数和路径长度衡量遗憾
- **关键结果 / 消融** · 分段常数对手下达到对数因子内最优
- **适用条件 / 局限** · 依赖理论设定，部署代价待核

**可复用机制** · 实验设计可对照有固定切换成本时联合设计决策与采样耦合，并按在线凸优化理论，按对手切换数和路径长度衡量遗憾核查证据。

<a id="paper-150374"></a>

## Dynamic Resolution Routing for Efficient Egocentric Grounding

[官方论文页](https://neurips.cc/virtual/2026/poster/150374) · [作者来源](https://openreview.net/forum?id=iYPoXQgQac)

- **问题 / 瓶颈** · 小物体易被 token 压缩漏掉
- **核心创新 / 方法** · 路由高分辨率图块并保持顺序，以间隔正则提升前景召回
- **Baseline** · 全分辨率及 token 缩减方法
- **Benchmark** · Ego4D、EgoIntention
- **关键结果 / 消融** · 最多减 67% token，保留原性能的 86.4%，最高快 1.66 倍
- **适用条件 / 局限** · 误路由会丢失小目标

**可复用机制** · 实验设计可对照以低分辨率全局视图引导局部高分辨率处理，并按Ego4D、EgoIntention核查证据。

<a id="paper-154629"></a>

## Dynamics-Aware Sparse Attention for Efficient Autoregressive Video Diffusion

[官方论文页](https://neurips.cc/virtual/2026/poster/154629) · [作者来源](https://openreview.net/forum?id=CAkj6hGR35)

- **问题 / 瓶颈** · 稠密视频生成重复处理静态区域
- **核心创新 / 方法** · 缓存偏向动态特征，按区域分配计算并进行动态引导蒸馏
- **Baseline** · 稠密自回归扩散
- **Benchmark** · VBench
- **关键结果 / 消融** · 作者报告 2.16 倍加速且保有视觉质量
- **适用条件 / 局限** · 镜头移动及大量运动时的收益待核

**可复用机制** · 实验设计可对照按运动区域分配历史缓存和计算，并按VBench核查证据。

<a id="paper-151856"></a>

## Dynamics-Informed Adaptive Offline RL for Real-Time Tokamak Plasma Control

[官方论文页](https://neurips.cc/virtual/2026/poster/151856) · [作者来源](https://openreview.net/forum?id=XPCEsmysv7)

- **问题 / 瓶颈** · 训练重建信号和在线传感不一致
- **核心创新 / 方法** · 以动力学模型提取潜在状态，并学习训练观测到部署观测的转换
- **Baseline** · 离线控制方案，具名基线待核
- **Benchmark** · 多次放电的离线测试与 DIII-D 实时部署
- **关键结果 / 消融** · 作者报告跟踪和鲁棒性改善
- **适用条件 / 局限** · 取决于转换误差与运行条件覆盖

**可复用机制** · 实验设计可对照用部署可用的观测训练离线控制策略，并按多次放电的离线测试与 DIII-D 实时部署核查证据。

<a id="paper-148692"></a>

## Dynamic Tokenization via Reinforcement Patching: End-to-end Training and Zero-shot Transfer

[官方论文页](https://neurips.cc/virtual/2026/poster/148692) · [作者来源](https://openreview.net/forum?id=vlSaF75Gmd)

- **问题 / 瓶颈** · 软离散化或启发式难兼顾可移植性
- **核心创新 / 方法** · 将边界作为强化学习动作，与预测骨干联合训练
- **Baseline** · 数据驱动分块方法
- **Benchmark** · 时间序列预测及独立分块器迁移
- **关键结果 / 消融** · 作者报告预测表现有竞争力
- **适用条件 / 局限** · 训练成本和跨骨干迁移幅度待核

**可复用机制** · 实验设计可对照用离散动作直接优化边界并固定压缩率，并按时间序列预测及独立分块器迁移核查证据。

<a id="paper-151874"></a>

## Dynamic Video Generation: Shaping Video Generation Across Time and Space

[官方论文页](https://neurips.cc/virtual/2026/poster/151874) · [作者来源](https://openreview.net/forum?id=XFSYmKLhpv)

- **问题 / 瓶颈** · 只压缩一维会限制加速或损害质量
- **核心创新 / 方法** · 根据内容自动调整时空采样与资源配置
- **Baseline** · 渐进分辨率路线，具名基线待核
- **Benchmark** · HunyuanVideo 与 HunyuanVideo-1.5
- **关键结果 / 消融** · 最高 7 倍加速，结合蒸馏最高 18 倍
- **适用条件 / 局限** · 峰值与质量度量的具体设置待核

**可复用机制** · 实验设计可对照联合调节时间和空间分辨率的计算预算，并按HunyuanVideo 与 HunyuanVideo-1.5核查证据。

<a id="paper-156061"></a>

## DynamicVLA: A Vision-Language-Action Model for Dynamic Object Manipulation

[官方论文页](https://neurips.cc/virtual/2026/poster/156061) · [作者来源](https://openreview.net/forum?id=0ltI4sHR1N)

- **问题 / 瓶颈** · 推理时目标继续移动，动作前缀会过期
- **核心创新 / 方法** · 重叠推理和执行，并丢弃时间失配的前缀
- **Baseline** · 已有动态操作模型，细项待核
- **Benchmark** · DOM 仿真和真机，覆盖未见运动样式
- **关键结果 / 消融** · 作者报告动态操作成功率改善
- **适用条件 / 局限** · 依赖延迟估计和后缀连续性

**可复用机制** · 实验设计可对照只执行预测动作块中仍然及时的后缀，并按DOM 仿真和真机，覆盖未见运动样式核查证据。

<a id="paper-148247"></a>

## DynaProto: Dynamic Prototypical Contrast for Temporally Consistent Object-Centric Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/148247) · [作者来源](https://openreview.net/forum?id=zJOsMj3Nby)

- **问题 / 瓶颈** · 固定槽位难处理物体进出画面
- **核心创新 / 方法** · 动态循环槽位注意力配合片段级原型对比
- **Baseline** · 固定槽位及既有对象中心学习
- **Benchmark** · YouTube-VIS 等对象发现和属性预测
- **关键结果 / 消融** · YouTube-VIS mBO 提升 11.0%
- **适用条件 / 局限** · 遮挡和长时再出现的边界待核

**可复用机制** · 实验设计可对照允许槽位随可见性变化并监督跨帧一致性，并按YouTube-VIS 等对象发现和属性预测核查证据。

<a id="paper-149611"></a>

## Dyna-Style Safety Augmented Reinforcement Learning: Staying Safe in the Face of Uncertainty

[官方论文页](https://neurips.cc/virtual/2026/poster/149611) · [作者来源](https://openreview.net/forum?id=oofzDJRuP8)

- **问题 / 瓶颈** · 未知动力学下固定规则过滤器难推广
- **核心创新 / 方法** · 以不确定性动力学模型学习过滤器，随安全数据积累更新
- **Baseline** · 已有安全强化学习方案
- **Benchmark** · 目标到达 CartPole 和 MuJoCo Walker
- **关键结果 / 消融** · 作者报告失败减少约两个数量级
- **适用条件 / 局限** · 实机迁移与不确定性失准影响待核

**可复用机制** · 实验设计可对照让安全过滤器同时约束预测失败和模型不确定性，并按目标到达 CartPole 和 MuJoCo Walker核查证据。

<a id="paper-149429"></a>

## DynaSub: Adaptive Subgrouping for Scalable Representation Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149429) · [作者来源](https://openreview.net/forum?id=q7e6qi0tQK)

- **问题 / 瓶颈** · 全局建模掩盖异常子群
- **核心创新 / 方法** · 在变分潜空间交替学习嵌入与非参数聚类
- **Baseline** · ResNet、ViT 骨干及现有 OOD 方法
- **Benchmark** · 近远 OOD、协变量漂移、类别 OOD，测 AUROC 和误报率
- **关键结果 / 消融** · 摘要报告误报率最多降低 10%
- **适用条件 / 局限** · 聚类稳定性和计算开销待核

**可复用机制** · 用随训练调整簇数的潜空间建模区分新子群与全局异常

<a id="paper-149930"></a>

## DynaTokens: Teaching Dynamics to Camera-Controlled Video Models at Test Time

[官方论文页](https://neurips.cc/virtual/2026/poster/149930) · [作者来源](https://openreview.net/forum?id=m6mxu2krgE)

- **问题 / 瓶颈** · 相机模型无法正确复现场景局部运动
- **核心创新 / 方法** · 冻结模型，经交叉注意力从少量轨迹优化场景专属 token
- **Baseline** · LoRA、块微调和专用可训练层
- **Benchmark** · VBench2、WorldScore，比较运动和相机控制
- **关键结果 / 消融** · 兼顾两类指标的折衷优于对照
- **适用条件 / 局限** · 依赖同场景示例，跨场景适配待核

**可复用机制** · 局部运动适合由可定位的条件 token 建模

<a id="paper-148952"></a>

## Dynin-Robotics: Omnimodal Unified Diffusion Vision-Language-Action Model

[官方论文页](https://neurips.cc/virtual/2026/poster/148952) · [作者来源](https://openreview.net/forum?id=tvmfTQg0WL)

- **问题 / 瓶颈** · 语义与动态分开训练造成互补失效
- **核心创新 / 方法** · 将动作、未来状态、语言和目标建模统一成同骨干的掩码去噪
- **Baseline** · 视觉语言及视频世界模型策略
- **Benchmark** · LIBERO、LIBERO-Plus、VLABench
- **关键结果 / 消融** · 标准任务可比，指令变化与扰动更稳健
- **适用条件 / 局限** · 联合训练代价和各目标贡献待核

**可复用机制** · 用共享掩码序列比较单独或联合解码动作与未来

<a id="paper-156053"></a>

## DyPSI: Dynamic Physics Sensing via Joint Field and Sensor-Trajectory Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/156053) · [作者来源](https://openreview.net/forum?id=0nkbZpHfRk)

- **问题 / 瓶颈** · 固定或逐帧选点难形成连续观测轨迹
- **核心创新 / 方法** · 联合扩散生成物理场和传感轨迹，用高斯过程时间核关联噪声
- **Baseline** · 静态布局和逐帧布局
- **Benchmark** · 湍流、GLORYS12 海温及三维车体气动
- **关键结果 / 消融** · 紧传感预算下重建误差改善
- **适用条件 / 局限** · 执行约束和轨迹平滑的权衡待核

**可复用机制** · 将待重建状态与观测位置共同建模，并以时间相关噪声约束轨迹

<a id="paper-156062"></a>

## DyRA: Dynamic Residual Approximation for Efficient Matrix Multiplication in DNNs

[官方论文页](https://neurips.cc/virtual/2026/poster/156062) · [作者来源](https://openreview.net/forum?id=0lCatrrRNf)

- **问题 / 瓶颈** · 小权重误差可能被激活放大
- **核心创新 / 方法** · 在结构化权重计算外动态近似低秩输出残差
- **Baseline** · 仅结构化权重近似
- **Benchmark** · 视觉、语音和语言模型，测准确性与速度
- **关键结果 / 消融** · DINOv3 GPU 提速 1.5 倍，精度损失降至不到对照三分之一
- **适用条件 / 局限** · 不同硬件和批大小的收益待核

**可复用机制** · 按激活空间误差而非权重误差分配近似预算

<a id="paper-150572"></a>

## DySurface: Consistent 4D Surface Reconstruction via Bridging Explicit Gaussians and Implicit Functions

[官方论文页](https://neurips.cc/virtual/2026/poster/150572) · [作者来源](https://openreview.net/forum?id=h9og8tDeEz)

- **问题 / 瓶颈** · 仅光度优化产生跨时刻几何歧义
- **核心创新 / 方法** · 将变形后的显式高斯转成动态稀疏体素，引导隐式符号距离场
- **Baseline** · 动态几何重建方法，具名待核
- **Benchmark** · 动态几何精度与渲染质量
- **关键结果 / 消融** · 几何精度改善同时保持竞争性渲染
- **适用条件 / 局限** · 依赖高斯对动态场景的覆盖

**可复用机制** · 以显式变形结果锚定隐式几何，避免正向与逆向变形失配

<a id="paper-154265"></a>

## E0: Expressive Fine-Grained Discrete Action Prediction for Vision-Language-Action Models via Tweedie Discrete Diffusion

[官方论文页](https://neurips.cc/virtual/2026/poster/154265) · [作者来源](https://openreview.net/forum?id=F4tL7wnb1n)

- **问题 / 瓶颈** · 连续或粗量化动作难同时适配多峰动作和符号骨干
- **核心创新 / 方法** · 对细粒度量化动作 token 用 Tweedie 离散扩散去噪
- **Baseline** · 强 VLA 对照，具名待核
- **Benchmark** · LIBERO、VLABench、ManiSkill、真机 Franka
- **关键结果 / 消融** · 摘要报告平均优于强基线 8.3%
- **适用条件 / 局限** · 量化精度、去噪预算和控制延迟待核

**可复用机制** · 按控制有效分辨率设动作词表，再与掩码生成和连续输出比较

<a id="paper-153750"></a>

## E4GEN: Event-level Explainable Extreme-Enhanced Time-series Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/153750) · [作者来源](https://openreview.net/forum?id=Iz17kYYauN)

- **问题 / 瓶颈** · 总体拟合好也可能漏掉极端事件
- **核心创新 / 方法** · 学习极端条件开始注入的去噪步，由样本自身预测信号并分层调制
- **Baseline** · 时间序列生成基线，具名待核
- **Benchmark** · 六个数据集、17 项指标
- **关键结果 / 消融** · 整体、极端与下游效用有改善
- **适用条件 / 局限** · 尾部罕见度和数据需求待核

**可复用机制** · 把尾事件条件的介入时机单独学习并评估

<a id="paper-155846"></a>

## Early Detection of Backbone Divergence via Neighborhood Structure in Learned Embeddings

[官方论文页](https://neurips.cc/virtual/2026/poster/155846) · [作者来源](https://openreview.net/forum?id=2T2Cs2OHk1)

- **问题 / 瓶颈** · 损失差距无法判定表征几何何时分化
- **核心创新 / 方法** · 把近邻夹角转换为球冠对数体积间距，做置换双样本检验
- **Baseline** · MMD、MMDAgg、Energy Distance、C2ST、近邻检验
- **Benchmark** · 14 个配置，维数 32–2048，比较首次稳定拒绝轮次
- **关键结果 / 消融** · 部分设置领先 25–60 轮；ResNet-50/CIFAR-100 第 61 对 121 轮
- **适用条件 / 局限** · 拒绝表明几何分化，不能单独判定成因

**可复用机制** · 同时监控 NLL 差距与骨干几何双样本检验

<a id="paper-151719"></a>

## Early Failure Detection and Intervention in Video Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151719) · [作者来源](https://openreview.net/forum?id=YbCJPGk7pI)

- **问题 / 瓶颈** · 生成结束后判失败造成重采样成本
- **核心创新 / 方法** · 早期潜变量转视频预览，用评分触发分层干预和早停
- **Baseline** · 完成后重生成
- **Benchmark** · CogVideoX-5B、Wan2.1-1.3B，VBench和时延
- **关键结果 / 消融** · 预览检查 39.2 毫秒，摘要报告额外耗时最高改善 2.64 倍
- **适用条件 / 局限** · 评分偏差与不同硬件开销待核

**可复用机制** · 先验证中间状态能否预测失败，再只对疑似失败启动修正

<a id="paper-152496"></a>

## Early Semantic Grounding in Image Editing Models for Zero-Shot Referring Image Segmentation

[官方论文页](https://neurips.cc/virtual/2026/poster/152496) · [作者来源](https://openreview.net/forum?id=ShIHKjhGRF)

- **问题 / 瓶颈** · 完整生成耗时且非分割所必需
- **核心创新 / 方法** · 提取首步去噪注意力定位与特征语义判别
- **Baseline** · 现有零样本指代分割
- **Benchmark** · RefCOCO、RefCOCO+、RefCOCOg
- **关键结果 / 消融** · 单步法优于所比零样本方法
- **适用条件 / 局限** · 依赖编辑骨干隐含定位能力

**可复用机制** · 先读取生成模型最早层的可分特征，再决定是否需要完整生成

<a id="paper-154126"></a>

## Early Signals, Strong Decisions: Prefix-Guided Sampling for Parallel Test-Time Scaling

[官方论文页](https://neurips.cc/virtual/2026/poster/154126) · [作者来源](https://openreview.net/forum?id=G5f8S6b2p6)

- **问题 / 瓶颈** · 完成低质量推理路径后再筛浪费计算
- **核心创新 / 方法** · 先采前缀、按内部置信度排序、续写高分路径
- **Baseline** · 标准并行测试时扩展
- **Benchmark** · 推理准确率、token 用量，具体基准待核
- **关键结果 / 消融** · 作者报告固定预算改善表现与效率
- **适用条件 / 局限** · 早期置信度失准可能误删有效路径

**可复用机制** · 按早期分数分配续写预算，对近决策边界单独评估

<a id="paper-155582"></a>

## EAT: Eviction-Aware Training for Long-Context LLM Inference on Edge Devices

[官方论文页](https://neurips.cc/virtual/2026/poster/155582) · [作者来源](https://openreview.net/forum?id=4YJpkRqrAO)

- **问题 / 瓶颈** · 量化改变注意力分数并干扰缓存淘汰
- **核心创新 / 方法** · 量化感知训练前向应用量化注意力诱导的遮罩，反向用掩码直通估计
- **Baseline** · 量化加淘汰串联、量化完整缓存
- **Benchmark** · 五任务平均分和天玑 9500 部署
- **关键结果 / 消融** · 半缓存时对照 29.04，EAT 39.44；较完整缓存吞吐增 64.1%
- **适用条件 / 局限** · 依赖量化规格与持有预算

**可复用机制** · 对依赖分数做离散选择的压缩流程联合训练和评测

<a id="paper-154040"></a>

## EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields

[官方论文页](https://neurips.cc/virtual/2026/poster/154040) · [作者来源](https://openreview.net/forum?id=GfwsJK6MIo)

- **问题 / 瓶颈** · 关节 token 难体现与画面的位置对应
- **核心创新 / 方法** · 将运动学状态和动作投影为相机视图内的场，用事件感知双向融合
- **Baseline** · 既有世界模型，具名待核
- **Benchmark** · WorldArena；具体指标待核
- **关键结果 / 消融** · 摘要报告优于对照，幅度待核
- **适用条件 / 局限** · 依赖相机和运动学对齐

**可复用机制** · 生成未来画面时比较空间对齐动作场与抽象动作 token

<a id="paper-149577"></a>

## ECHO: Continuous Hierarchical Memory for Vision-Language-Action Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149577) · [作者来源](https://openreview.net/forum?id=p56YFb1ACl)

- **问题 / 瓶颈** · 线性或扁平存储难以表达操作经验的类别组织。
- **核心创新 / 方法** · 双曲自编码器映射隐藏状态，按蕴含约束建树，后台以插值与分裂更新。
- **Baseline** · 以 π₀ 为底座并比较原版 π₀。
- **Benchmark** · LIBERO、跨套件长程操作及初步真机。
- **关键结果 / 消融** · LIBERO-Long 成功率绝对提高 12.8 个百分点。
- **适用条件 / 局限** · 真机证据初步，规模和检索开销待查。

**可复用机制** · 固定模型和存储量，比较层级检索与扁平近邻在未见任务组合上的表现。

<a id="paper-152212"></a>

## Echoes of Error: Residual-Directional Local Rollout Consistency for Timeseries Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/152212) · [作者来源](https://openreview.net/forum?id=UjSZdUySXj)

- **问题 / 瓶颈** · 单步小误差在闭环滚动中仍可能传播。
- **核心创新 / 方法** · 惩罚沿回馈扰动的雅可比向量积，给出近预测流形时的稳定管条件。
- **Baseline** · 教师强制与自由滚动的局部一致性对照，具体模型待核。
- **Benchmark** · 时间序列预测，比较滚动精度。
- **关键结果 / 消融** · 作者报告正则提升预测精度，具体数值待核。
- **适用条件 / 局限** · 一阶近似只描述局部扰动，远离流形时需另测。

**可复用机制** · 在自回归模型中针对实际可回馈残差做方向正则，并按预测跨度分析误差。

<a id="paper-152942"></a>

## EchoKV: Efficient KV Cache Compression via Similarity-Based Reconstruction

[官方论文页](https://neurips.cc/virtual/2026/poster/152942) · [作者来源](https://openreview.net/forum?id=PE7GYmhRfw)

- **问题 / 瓶颈** · 改投影的低秩压缩限制全缓存回退。
- **核心创新 / 方法** · 利用头间和层间相似度，由轻量网络用保留分量重建丢弃的 KV。
- **Baseline** · 对照现有压缩和完整缓存。
- **Benchmark** · LongBench、RULER，多骨干及压缩比。
- **关键结果 / 消融** · 摘要报告压缩效果优于对照，短上下文保持全缓存吞吐。
- **适用条件 / 局限** · 依赖缓存分量相似性，长文检索的边缘损失待核。

**可复用机制** · 评估压缩时保留原始执行路径，按上下文长度和显存预算测吞吐及质量。

<a id="paper-155692"></a>

## Echo learning enables biologically plausible temporal credit assignment

[官方论文页](https://neurips.cc/virtual/2026/poster/155692) · [作者来源](https://openreview.net/forum?id=3ew4yPTGyN)

- **问题 / 瓶颈** · 全 BPTT 需保存时间展开历史。
- **核心创新 / 方法** · 用哈密顿量可分性推导局部规则，并以稳态损失分别约束可逆性和自伴关系。
- **Baseline** · 全 BPTT、截断 BPTT、e-prop。
- **Benchmark** · 时间序列分类和回归，比较学习性能与梯度质量。
- **关键结果 / 消融** · 作者报告结构化回声模型可匹配 BPTT，放松版得到近似梯度。
- **适用条件 / 局限** · 精确性依赖动力学可逆和读出条件。

**可复用机制** · 先明确可逆性误差，再衡量常数内存更新和真实时序梯度的差异。

<a id="paper-153388"></a>

## EchoPrune: Interpreting Redundancy as Temporal Echoes for Efficient VideoLLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/153388) · [作者来源](https://openreview.net/forum?id=LlfSFn1ZXN)

- **问题 / 瓶颈** · 密采帧昂贵，稀采帧可能漏掉事件。
- **核心创新 / 方法** · 按连续帧对应计算新颖性，再结合文本查询相关性做免训练剪枝。
- **Baseline** · 对照免训练 token 削减；名称待查。
- **Benchmark** · LLaVA-OV、Qwen2.5VL、Qwen3VL，六个视频理解基准。
- **关键结果 / 消融** · 摘要报告同预算最多处理 20 倍帧，Qwen2.5VL-7B 预填充最高加速 5.6 倍。
- **适用条件 / 局限** · 对应误差可能把相机运动当事件，数值适用条件待查。

**可复用机制** · 固定模型 token 预算，比较密采剪枝和稀采全保留的时序证据召回。

<a id="paper-154932"></a>

## ECHO: Terminal Agents Learn World Models for Free

[官方论文页](https://neurips.cc/virtual/2026/poster/154932) · [作者来源](https://openreview.net/forum?id=9rkAbf5ICO)

- **问题 / 瓶颈** · 只有动作奖励会遗漏已经观测的环境反馈。
- **核心创新 / 方法** · 在策略梯度之外预测环境观测 token，复用前向计算与已有轨迹。
- **Baseline** · GRPO 和专家 SFT 后再做 GRPO。
- **Benchmark** · TerminalBench 2 和留出终端任务，以 pass@1 评估。
- **关键结果 / 消融** · Qwen3-8B 从 2.70% 到 5.17%，14B 从 5.17% 到 10.79%。
- **适用条件 / 局限** · 效果依赖合规训练环境及反馈质量，绝对成功率仍低。

**可复用机制** · 在普通软件维护模拟任务中，比较奖励单训与反馈预测辅助训练。

<a id="paper-139639"></a>

## ECLIPSE: A Spacecraft Rendezvous Trajectories Dataset with Controlled In-Orbit Lighting Conditions

[官方论文页](https://neurips.cc/virtual/2026/poster/139639) · [作者来源](https://openreview.net/forum?id=Dwc7cwaADG)

- **问题 / 瓶颈** · 传统仿真到真实对照混合了光照和轨迹因素。
- **核心创新 / 方法** · 配对合成训练集及硬件在环评估，对 14 条轨迹施加四种受控照明。
- **Baseline** · 比较匹配轨迹的照明条件。
- **Benchmark** · 航天器视觉位姿估计；误差指标待查。
- **关键结果 / 消融** · 作者报告在此设定下光照是迁移落差的主要因素。
- **适用条件 / 局限** · 硬件在环证据的真实在轨适用性仍待查。

**可复用机制** · 用同一轨迹的受控外观干预量化视觉迁移的主导因素。

<a id="paper-153610"></a>

## Edge of Stability Selectively Shapes Learning Across the Data Distribution

[官方论文页](https://neurips.cc/virtual/2026/poster/153610) · [作者来源](https://openreview.net/forum?id=K5wixs1lVP)

- **问题 / 瓶颈** · 整体稳定性指标可能隐藏组间学习速度差异。
- **核心创新 / 方法** · 从同一状态分支进入或离开稳定边缘，另用保距离扰动破坏方向对齐。
- **Baseline** · 对照同初态分支和方向随机化。
- **Benchmark** · 分组训练轨迹，分析 Hessian 顶方向与梯度幅值。
- **关键结果 / 消融** · 受益组需要方向对齐且梯度长期非零；交叉熵下高置信组可饱和。
- **适用条件 / 局限** · 结论依赖训练设定，跨损失验证待核。

**可复用机制** · 调大学习率时按群组测进度和方向对齐，识别总体收益掩盖的退化。

<a id="paper-150004"></a>

## Edge of Stochastic Stability: Revisiting the Edge of Stability for SGD

[官方论文页](https://neurips.cc/virtual/2026/poster/150004) · [作者来源](https://openreview.net/forum?id=lUoXQdMVoe)

- **问题 / 瓶颈** · 全批 Hessian 顶特征值稳定在 2/步长的规律不直接适用小批训练。
- **核心创新 / 方法** · 测量各批梯度沿相应 Hessian 的方向曲率，再取期望。
- **Baseline** · 对照全批梯度下降的谱锐度。
- **Benchmark** · 小批 SGD 训练轨迹，比较批锐度与全局最大特征值。
- **关键结果 / 消融** · 作者报告趋于 2/步长的是批锐度，全局最大特征值受到抑制。
- **适用条件 / 局限** · 结论受批大小与训练条件影响。

**可复用机制** · 比较小批训练的稳定性时同时记录批方向曲率和全局谱值。

<a id="paper-148560"></a>

## EDISCO: Equivariant Discrete Diffusion for Euclidean Combinatorial Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/148560) · [作者来源](https://openreview.net/forum?id=wzGLCsImQ1)

- **问题 / 瓶颈** · 增广和正则只近似旋转、反射及平移不变性。
- **核心创新 / 方法** · 用 E(2) 等变边评分配合边变量分类连续时间马尔可夫链。
- **Baseline** · 比较非等变及其他学习型求解器。
- **Benchmark** · TSP 100–10000 点、CVRP 50–2000 客户，并测两类分布偏移。
- **关键结果 / 消融** · 摘要报告用 33%–50% 训练实例仍优于所测基线。
- **适用条件 / 局限** · 已知几何群的假设对非欧式约束不一定成立。

**可复用机制** · 固定训练数据，比较精确等变模型和数据增广在坐标变换与分布偏移下的差异。

<a id="paper-154973"></a>

## EditBridge: Towards Faithful and Efficient Ultra-High-Resolution Image Editing

[官方论文页](https://neurips.cc/virtual/2026/poster/154973) · [作者来源](https://openreview.net/forum?id=9WPA6eQqZg)

- **问题 / 瓶颈** · 独立超分可能生成与源图不一致的细节。
- **核心创新 / 方法** · 用条件扩散桥从低清编辑直接细化，按首阶段语义对应引导分块交叉注意力。
- **Baseline** · 对照低分辨率编辑后独立超分及其他扩散方案。
- **Benchmark** · 最高 4K 的图像编辑，比较保真度和推理耗时。
- **关键结果 / 消融** · 作者报告 2K 加速 3.6–8.4 倍，4K 推理用时 61 秒。
- **适用条件 / 局限** · 依赖初次编辑的对应质量，设备与任务条件待查。

**可复用机制** · 将源图细节保持和编辑成功分开评估，再验证局部稀疏交互的加速损失。

<a id="paper-152491"></a>

## EditFlowSR: Revisable Expression Generation for Symbolic Regression

[官方论文页](https://neurips.cc/virtual/2026/poster/152491) · [作者来源](https://openreview.net/forum?id=SiqvujQlIz)

- **问题 / 瓶颈** · 序列生成难以修正已生成子结构
- **核心创新 / 方法** · 共享插入、删除与替换操作，分别以构造和化简轨迹监督
- **Baseline** · 自回归与搜索式符号回归，具名对照待核
- **Benchmark** · SRBench，准确率、树大小和时间
- **关键结果 / 消融** · 作者报告三项的 Pareto 排名领先
- **适用条件 / 局限** · 依赖训练轨迹覆盖和合法树操作

**可复用机制** · 同时以构造和化简监督树编辑，检查拟合与复杂度的权衡

<a id="paper-149507"></a>

## Editing Large Language Models with Geometry-Aware Regularization

[官方论文页](https://neurips.cc/virtual/2026/poster/149507) · [作者来源](https://openreview.net/forum?id=pci0NmsKVy)

- **问题 / 瓶颈** · 均匀约束既会损伤旧知识，也会妨碍困难更新
- **核心创新 / 方法** · 低秩加对角因子刻画 FFN 特征，保护核心低秩空间，困难编辑使用较弱约束
- **Baseline** · 现有知识编辑方法，具名对照待核
- **Benchmark** · GPT2-XL、GPT-J、LLaMA-3-8B，批次与最多一万次连续更新
- **关键结果 / 消融** · 作者报告编辑与旧知识保持均改善
- **适用条件 / 局限** · 核心子空间估计和难度代理的可靠性待核

**可复用机制** · 固定编辑数据，对照均匀约束与分空间、分难度正则

<a id="paper-139200"></a>

## EditJudge-Bench: Auditing VLM Image-Edit Judges with Synthetic Ground Truth

[官方论文页](https://neurips.cc/virtual/2026/poster/139200) · [作者来源](https://openreview.net/forum?id=eynW4BxY28)

- **问题 / 瓶颈** · 真实编辑把评分器错误和编辑器失误混在一起
- **核心创新 / 方法** · 用 Blender 受控修改场景，在九类编辑上将评分器视为二分类验证器
- **Baseline** · 18 种配置，含 GPT-4o 配 VIEScore 和微调评分器
- **Benchmark** · 1500 个前后样本，测 AUROC 并与真实人工偏好排名关联
- **关键结果 / 消融** · GPT-4o 配 VIEScore AUROC 67.1%，空间编辑近随机；两个真实集排名相关为 0.93、0.77
- **适用条件 / 局限** · 合成可控性与真实编辑复杂度之间仍有差异

**可复用机制** · 对自动评委先作受控干预测试，再检查失败类别和提示排序敏感性

<a id="paper-154496"></a>

## EDITORS Know Your Style! Editing LoRA Subspaces for Stylistic Attribution and Imitation

[官方论文页](https://neurips.cc/virtual/2026/poster/154496) · [作者来源](https://openreview.net/forum?id=DAEi6FPYeD)

- **问题 / 瓶颈** · 作者识别和风格生成容易借用训练语料的主题
- **核心创新 / 方法** · 用风格中性的语句训练诊断 LoRA，识别内容子空间后，对目标适配器做输入激活投影
- **Baseline** · 既有作者识别和风格生成系统
- **Benchmark** · 文学、社媒和新闻作者识别，以及风格与内容符合度
- **关键结果 / 消融** · 作者识别准确率相较最强对照最高提升 29%，风格生成也有改善
- **适用条件 / 局限** · 风格中性数据构造若偏置，会误去除有效风格

**可复用机制** · 在主题隔离划分下比较常规微调与内容方向投影

<a id="paper-151219"></a>

## Edit the Bits, Diff the Codes: Bitwise Residual Editing for Visual Autoregressive Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151219) · [作者来源](https://openreview.net/forum?id=c371hRPzMl)

- **问题 / 瓶颈** · 仅改 token 或 logits 无法保证局部之外保持不变
- **核心创新 / 方法** · 在 Bernoulli KL 信赖域内引导各位采样，将所采位变成按掩码写回的多尺度残差
- **Baseline** · 同 Infinity-2B 骨干的自回归编辑器
- **Benchmark** · PIE-Bench，文本对齐和背景保持
- **关键结果 / 消融** · 作者报告同骨干文本对齐领先；两个模块分别有助于对齐和保持
- **适用条件 / 局限** · 需要位残差接口与合适掩码；潜变量保持不保证解码像素逐点相同

**可复用机制** · 在可加残差生成器中把采样选择与空间写入拆开，并分别消融

<a id="paper-150520"></a>

## EDMA: Entropy-Driven Multimodal Answering

[官方论文页](https://neurips.cc/virtual/2026/poster/150520) · [作者来源](https://openreview.net/forum?id=hUf4I26zIr)

- **问题 / 瓶颈** · 逐步提示缺少对每种模态实际贡献的测量
- **核心创新 / 方法** · 用逻辑熵度量各模态划分的区分度，再组合模态并选择最终熵低的轨迹
- **Baseline** · 提示式基线及所评系统
- **Benchmark** · 多个多模态问答集，测 F1、误报和轨迹干预
- **关键结果 / 消融** · 相较最强提示基线和所比系统平均提升 12.8、19.8 个 F1 点
- **适用条件 / 局限** · 依赖候选集合及划分正确性，代表性待核

**可复用机制** · 先测单模态减熵，再保留有互补信息的证据，验证错误候选不在缩减中被固化

<a id="paper-148749"></a>

## Effect-Driven Skill Abstractions for Offline Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/148749) · [作者来源](https://openreview.net/forum?id=vLeZitFeKS)

- **问题 / 瓶颈** · 仅重建动作的技能码难区分可达目标
- **核心创新 / 方法** · 按当前状态与技能码预测下一状态，用预测训练动作量化，离散策略选码再由低层控制器执行
- **Baseline** · 连续 actor 和重建式技能量化
- **Benchmark** · 离线目标条件导航，指标待核
- **关键结果 / 消融** · 多数导航设置优于两类对照
- **适用条件 / 局限** · 需足够覆盖状态效果及可用低层控制器

**可复用机制** · 将技能码的训练目标从动作重建换为结果预测，固定码本容量比较目标到达

<a id="paper-153996"></a>

## Effective Context in Transformers: An Analysis of Fragmentation and Tokenization

[官方论文页](https://neurips.cc/virtual/2026/poster/153996) · [作者来源](https://openreview.net/forum?id=GzkBhDQNKM)

- **问题 / 瓶颈** · 无损重编码仍可能改变有限上下文的预测难度
- **核心创新 / 方法** · 在 Markov 源分析符号碎片化与贪心聚合，给出依赖历史覆盖概率与压缩率的界
- **Baseline** · 原始表示、碎片化表示和聚合表示
- **Benchmark** · Markov 源有限上下文对数损失
- **关键结果 / 消融** · 作者证明碎片化可严格提升最优损失，聚合在给定条件下能扩展有效历史
- **适用条件 / 局限** · 对自然语言的覆盖诊断不能直接替代理论前提

**可复用机制** · 按同样 token 预算比较源历史跨度分布，而非只看平均压缩率

<a id="paper-149088"></a>

## Effective Multi-sensor Conditioning for Street-view Novel-view Synthesis

[官方论文页](https://neurips.cc/virtual/2026/poster/149088) · [作者来源](https://openreview.net/forum?id=szHv2SyPlO)

- **问题 / 瓶颈** · 目标相机越偏离原路径，单一信号越难支撑合成
- **核心创新 / 方法** · 条件化视频扩散，联合 LiDAR、参考图和相机姿态，逐步减少训练中的 LiDAR 密度
- **Baseline** · 稀疏及更稠密 LiDAR 条件下的新视角方法
- **Benchmark** · Waymo Open Dataset，包含多种偏离轨迹
- **关键结果 / 消融** · 作者报告稀疏条件下领先，并可匹配使用 10–100 倍更密点云的方法
- **适用条件 / 局限** · 依赖标定、运动估计和参考覆盖

**可复用机制** · 将几何和外观分别作为条件，以射线几何对齐，扫描传感稀疏度验证稳健性

<a id="paper-149082"></a>

## Effectiveness of Curriculum Learning Depends on Reward Sparsity and Competing Optima

[官方论文页](https://neurips.cc/virtual/2026/poster/149082) · [作者来源](https://openreview.net/forum?id=t11t6OT9PS)

- **问题 / 瓶颈** · 课程对不同任务的收益差异很大
- **核心创新 / 方法** · 在目标拦截模型控制奖励范围，解析和数值研究 REINFORCE 学习动力学
- **Baseline** · 稀疏和密集奖励，以及是否使用课程的设置
- **Benchmark** · 开放环回合式合成任务
- **关键结果 / 消融** · 密集奖励下收益小；稀疏且努力成本与回报冲突时，课程可能是可学习的必要条件
- **适用条件 / 局限** · 证据来自最小模型，外部泛化需实证

**可复用机制** · 分别用课程增加有效反馈频率和绕开错误吸引域，消融两种作用

<a id="paper-139471"></a>

## Effect-Level Validation for Causal Discovery in Interactive Telemetry

[官方论文页](https://neurips.cc/virtual/2026/poster/139471) · [作者来源](https://openreview.net/forum?id=NqsvRZNvpb)

- **问题 / 瓶颈** · 图结构看似合理并不代表可用于决策
- **核心创新 / 方法** · 筛选能识别目标效应且存在重叠的图，再结合安慰剂、子采样、跨算法稳定性和 E-value 检验
- **Baseline** · 原始留存差异和未经过可识别筛选的发现运行
- **Benchmark** · 角色扮演游戏真实日志，目标为次日留存风险差
- **关键结果 / 消融** · 约三分之一的发现运行支持效应识别；部分图的调整后估计通过反证检验
- **适用条件 / 局限** · 单产品单查询且仍依赖未观测混杂假设

**可复用机制** · 将因果发现的验收单位设为具体效应查询，并报告识别失败比例

<a id="paper-155995"></a>

## Efficient, Accurate and Stable Gradients for Neural ODEs

[官方论文页](https://neurips.cc/virtual/2026/poster/155995) · [作者来源](https://openreview.net/forum?id=1IMnLHfJyl)

- **问题 / 瓶颈** · 递归检查点反传需要在重算和存储之间取舍
- **核心创新 / 方法** · 构造高阶、数值稳定的可逆积分步，以恢复前态方式计算精确离散梯度
- **Baseline** · 递归检查点法以及先前可逆架构
- **Benchmark** · 科学建模和时间序列分类，比较训练时间与显存
- **关键结果 / 消融** · 摘要报告训练加速超过两倍且平均内存至少降低十倍
- **适用条件 / 局限** · 精度和稳定性仍与具体方程和求解设置有关

**可复用机制** · 在相同误差容限下比较可逆积分和重算反传，分别报告稳定性、梯度误差与成本

<a id="paper-156141"></a>

## Efficient Adaptive Data Acquisition via Pretrained Belief Representations

[官方论文页](https://neurips.cc/virtual/2026/poster/156141) · [作者来源](https://openreview.net/forum?id=04exJhvdI5)

- **问题 / 瓶颈** · 直接读历史难复用预测先验
- **核心创新 / 方法** · 解耦预测表征和采集策略头
- **Baseline** · 已有摊销采集方法
- **Benchmark** · 实验设计、贝叶斯优化和主动学习
- **关键结果 / 消融** · 报告更少训练样本下改善采集表现
- **适用条件 / 局限** · 充分信念是理论依据，实际编码器未必保留全部信息

**可复用机制** · 固定预测器，比较信念编码与直接历史编码所需训练预算

<a id="paper-148733"></a>

## Efficient Adjoint Matching for Fine-tuning Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148733) · [作者来源](https://openreview.net/forum?id=vSHTrySbQc)

- **问题 / 瓶颈** · 原始伴随匹配需完整采样和反向积分
- **核心创新 / 方法** · 改用线性基漂移及匹配的终端代价
- **Baseline** · Adjoint Matching
- **Benchmark** · 文生图，PickScore、ImageReward、HPSv2.1、CLIPScore、美学
- **关键结果 / 消融** · 收敛最高快四倍，指标持平或改善
- **适用条件 / 局限** · 证据限所测文生图微调设置

**可复用机制** · 分别记录前向采样与反向积分开销，检验等预算奖励收益

<a id="paper-148269"></a>

## Efficient Agentic GPU Kernel Optimization with a Compact Domain-Specific Language and Speed-of-Light Guidance

[官方论文页](https://neurips.cc/virtual/2026/poster/148269) · [作者来源](https://openreview.net/forum?id=z71DjAr4OZ)

- **问题 / 瓶颈** · 每次候选都要编译验收，低层表示搜索成本高
- **核心创新 / 方法** · 以 μCUTLASS 暴露关键选项，配合理论吞吐指导和验收
- **Baseline** · 原始代码生成与 PyTorch
- **Benchmark** · H100 上 59 项 KernelBench
- **关键结果 / 消融** · GPT-5-mini 几何均值从 0.40 倍到 1.27 倍，加指导达 1.56 倍
- **适用条件 / 局限** · 硬件与算子覆盖有限

**可复用机制** · 在独立正确性和性能验收下比较 DSL 与原始代码

<a id="paper-153892"></a>

## Efficient Analytic Uncertainty Quantification for Multimodal Regression

[官方论文页](https://neurips.cc/virtual/2026/poster/153892) · [作者来源](https://openreview.net/forum?id=HwWUMaIRkr)

- **问题 / 瓶颈** · 单峰似然不能表示多个潜在结果
- **核心创新 / 方法** · 对分位回归与分类恢复推导解析 ELBO 和预测密度
- **Baseline** · 多峰回归方法及单峰参数模型
- **Benchmark** · 三项大规模多峰回归基准
- **关键结果 / 消融** · 报告改善所测多峰回归表现
- **适用条件 / 局限** · 解析性依赖所用变分形式，校准细节待核

**可复用机制** · 在多峰数据上同时比较密度拟合、区间覆盖和推理时间

<a id="paper-154977"></a>

## Efficient and Simple Data Mixing All The Time

[官方论文页](https://neurips.cc/virtual/2026/poster/154977) · [作者来源](https://openreview.net/forum?id=9UVUeqvO8L)

- **问题 / 瓶颈** · 固定代理模型可能无法跟踪训练阶段变化
- **核心创新 / 方法** · 插值当前模型上训练的适配器，在线选择数据配比
- **Baseline** · 不混合、重训与在线蒸馏
- **Benchmark** · 预训练、持续中训和持续指令微调
- **关键结果 / 消融** · 预训练平均困惑度改善 6.3%，持续学习匹配重训与蒸馏时节省算力
- **适用条件 / 局限** · 需要适配器插值能近似候选分布训练效果

**可复用机制** · 在不同训练阶段抽样验证配比排序的代理误差

<a id="paper-139637"></a>

## Efficient Benchmarking Is Just Feature Selection and Multiple Regression

[官方论文页](https://neurips.cc/virtual/2026/poster/139637) · [作者来源](https://openreview.net/forum?id=E0CrL9qFym)

- **问题 / 瓶颈** · 简单子集均分会遗漏题间冗余和区分度
- **核心创新 / 方法** · 用 mRMR 选题并拟合全分回归器
- **Baseline** · 既有子集预测与聚类选题
- **Benchmark** · 二值和连续基准，MAE、RMSE、秩相关
- **关键结果 / 消融** · 除数据极少情形外误差较低、排序较稳，选题更快
- **适用条件 / 局限** · 需一批模型的全量得分作为训练资料

**可复用机制** · 在留出模型上同时测绝对分和名次偏差

<a id="paper-155616"></a>

## Efficient Dataset Distillation for Pre-Trained Self-Supervised Models via Statistical Flow Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/155616) · [作者来源](https://openreview.net/forum?id=4DqCJdPblC)

- **问题 / 瓶颈** · 线性梯度匹配需反复加载大量真图和增强
- **核心创新 / 方法** · 由类别中心间相对关系构造全局统计流，匹配合成数据
- **Baseline** · Linear Gradient Matching
- **Benchmark** · 预训练自监督表征下的下游分类蒸馏
- **关键结果 / 消融** · 报告显存约减少十倍、蒸馏快四倍，效果持平或提升
- **适用条件 / 局限** · 依赖固定预训练表征，其他学习器待核

**可复用机制** · 在相同合成集大小下比较批级梯度与全局统计对齐

<a id="paper-148980"></a>

## Efficient Diffusion Policy Fine Tuning with Latent Noise Representation Bridging

[官方论文页](https://neurips.cc/virtual/2026/poster/148980) · [作者来源](https://openreview.net/forum?id=tjBAig6ZC4)

- **问题 / 瓶颈** · 潜噪声混叠导致反复拟合价值网络
- **核心创新 / 方法** · 建立线性潜噪声 MDP 理论，并用桥接方程学习潜表示
- **Baseline** · 现有潜噪声和生成策略微调
- **Benchmark** · 机器人运动和操作控制任务
- **关键结果 / 消融** · 报告困难任务表现约为对照二至三倍
- **适用条件 / 局限** · 理论依赖线性结构，实际环境适配须实测

**可复用机制** · 比较潜空间桥接和重复拟合价值网络的样本成本

<a id="paper-149796"></a>

## Efficient evaluation and error pattern discovery for blackbox AI systems

[官方论文页](https://neurips.cc/virtual/2026/poster/149796) · [作者来源](https://openreview.net/forum?id=nH1NodvfBz)

- **问题 / 瓶颈** · 完整评测和人工审核成本高
- **核心创新 / 方法** · 推导误差估计的重要性采样器并据此归纳错误模式
- **Baseline** · 依赖校准数据或固定基准的采样路线
- **Benchmark** · MMLU-Pro 与 TerminalBench 2.0
- **关键结果 / 消融** · 摘要报告两类任务均可用
- **适用条件 / 局限** · 代理质量与采样权重影响估计

**可复用机制** · 在固定成本下分别检验误差估计与长尾发现

<a id="paper-150090"></a>

## Efficient Evaluation of LLM Performance with Statistical Guarantees

[官方论文页](https://neurips.cc/virtual/2026/poster/150090) · [作者来源](https://openreview.net/forum?id=kmsvWSZXrM)

- **问题 / 瓶颈** · 多个模型和基准的穷举评测昂贵
- **核心创新 / 方法** · 结合历史贝叶斯因子模型、主动选题及有限总体校准
- **Baseline** · 均匀抽样及其他强基线
- **Benchmark** · 两个基准套件及不同历史缺失率
- **关键结果 / 消融** · 同等区间宽度最多约五倍查询节省
- **适用条件 / 局限** · 依赖历史信息价值和分配预算

**可复用机制** · 评测调度优化后仍需验证实际区间覆盖

<a id="paper-152541"></a>

## Efficient Fine-Tuning for Structured Sparsity Under Group Repartitioning

[官方论文页](https://neurips.cc/virtual/2026/poster/152541) · [作者来源](https://openreview.net/forum?id=SOamrNPF9T)

- **问题 / 瓶颈** · 换分组后从头学习浪费旧优化结果
- **核心创新 / 方法** · 将分组变更拆为基本操作并推导各步学习动态
- **Baseline** · 新分组下从头训练
- **Benchmark** · 组稀疏正则下的重分组实验
- **关键结果 / 消融** · 作者报告降低适配成本
- **适用条件 / 局限** · 依赖可分解操作及所用范数

**可复用机制** · 分别对比重分组后的目标值与耗时

<a id="paper-153950"></a>

## Efficient Generative Transformer Operators for Million-Point PDEs

[官方论文页](https://neurips.cc/virtual/2026/poster/153950) · [作者来源](https://openreview.net/forum?id=HLXxp5Wo4y)

- **问题 / 瓶颈** · 高分辨率网格昂贵且滚动预测会累积误差
- **核心创新 / 方法** · 分层编码解码结合分阶段训练及潜空间轨迹生成
- **Baseline** · 逐步预测算子及已有方法
- **Benchmark** · 大规模二维和三维 PDE
- **关键结果 / 消融** · 报告最高约百倍压缩和百万点扩展
- **适用条件 / 局限** · 解码保真度与分辨率相关

**可复用机制** · 在同预算下比较逐帧滚动与全轨迹生成的长时误差

<a id="paper-153904"></a>

## Efficient Hybrid Distillation: Synergizing Score and Adversarial Objectives for One-Step Diffusion

[官方论文页](https://neurips.cc/virtual/2026/poster/153904) · [作者来源](https://openreview.net/forum?id=Hq9vqR70JT)

- **问题 / 瓶颈** · 统一混合目标忽视高低噪声监督差异
- **核心创新 / 方法** · 分数蒸馏侧重高噪声，对抗蒸馏侧重低噪声
- **Baseline** · 单目标与直接混合目标
- **Benchmark** · 单步扩散和 DiT 流匹配
- **关键结果 / 消融** · 摘要报告两目标有效区间互补
- **适用条件 / 局限** · 切分边界需要按模型验证

**可复用机制** · 做分噪声段消融后再混合目标

<a id="paper-148809"></a>

## Efficient LLM Adaptation with Forward-Only Passes

[官方论文页](https://neurips.cc/virtual/2026/poster/148809) · [作者来源](https://openreview.net/forum?id=ux9eaZ3bxm)

- **问题 / 瓶颈** · 梯度适配成本大，穷举选择也慢
- **核心创新 / 方法** · 前向衡量各奇异分量诱发的激活角度集中度
- **Baseline** · 梯度适配和穷举搜索
- **Benchmark** · 多数据集任务适配
- **关键结果 / 消融** · 作者报告准确率具有竞争力且内存更低
- **适用条件 / 局限** · 依赖代表性输入和可读取权重

**可复用机制** · 用前向信号定位可压缩层再逐层验收

<a id="paper-150136"></a>

## Efficient Lookahead Encoding and Abstracted Width for Learning General Policies in Classical Planning

[官方论文页](https://neurips.cc/virtual/2026/poster/150136) · [作者来源](https://openreview.net/forum?id=kR1PKyczWe)

- **问题 / 瓶颈** · 逐状态评估昂贵且难建模状态关系
- **核心创新 / 方法** · 以相对当前状态的关系差异配置关系 GNN
- **Baseline** · 逐步评估的迭代宽度策略
- **Benchmark** · 经典规划与 IPC 2023 设置
- **关键结果 / 消融** · 作者报告更高效的前瞻编码
- **适用条件 / 局限** · 依赖关系式状态及搜索宽度

**可复用机制** · 用增量表示批量评分前瞻状态

<a id="paper-153042"></a>

## Efficiently Aligning Draft Models via Parameter- and Data-Efficient Adaptation

[官方论文页](https://neurips.cc/virtual/2026/poster/153042) · [作者来源](https://openreview.net/forum?id=OTKY3Ftw6B)

- **问题 / 瓶颈** · 目标分布漂移降低接受率
- **核心创新 / 方法** · 共享与私有组件分离，用目标模型重生成并筛数据
- **Baseline** · 逐目标重训草稿
- **Benchmark** · 微调目标上的平均接受长度和训练开销
- **关键结果 / 消融** · 作者报告恢复接受长度并降低训练成本
- **适用条件 / 局限** · 需要目标模型生成数据

**可复用机制** · 把草稿适配收益按参数更新量和再生成预算归因

<a id="paper-149800"></a>

## Efficient Memory Crystallization for Graph Learning under Non-Stationary Distribution Shifts

[官方论文页](https://neurips.cc/virtual/2026/poster/149800) · [作者来源](https://openreview.net/forum?id=nG6LsRFiOk)

- **问题 / 瓶颈** · 连续域漂移下重训记忆模块开销增长
- **核心创新 / 方法** · 把每个新域压缩成记忆并随域演化更新
- **Baseline** · 生成式记忆和直接适配
- **Benchmark** · 连续图协变量漂移
- **关键结果 / 消融** · 作者给出较直接适配更紧的泛化界
- **适用条件 / 局限** · 依赖摘要保留有效语义

**可复用机制** · 用固定记忆预算比较摘要与生成式回放

<a id="paper-151578"></a>

## Efficient Neural Field Learning via Adaptive Coverage and Focused Sampling

[官方论文页](https://neurips.cc/virtual/2026/poster/151578) · [作者来源](https://openreview.net/forum?id=ZYSGaMwCnb)

- **问题 / 瓶颈** · 逐点追逐高误差会重复采样局部
- **核心创新 / 方法** · 用自适应空间划分及区域级加权平衡覆盖与重点
- **Baseline** · 均匀和逐点自适应采样
- **Benchmark** · 科学场隐式表示学习
- **关键结果 / 消融** · 报告梯度方差和误差改善及更早收敛
- **适用条件 / 局限** · 分区质量和加权偏差影响适用性

**可复用机制** · 固定点数预算同时测空间覆盖和训练误差

<a id="paper-151908"></a>

## Efficient Off-Policy RL for Video Generation via Forward-Consistent Reward Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/151908) · [作者来源](https://openreview.net/forum?id=WyhaKI6IC1)

- **问题 / 瓶颈** · 少步模型不易沿用依赖在线轨迹的强化学习
- **核心创新 / 方法** · 把去噪损失变为正分数，做单步 GFlowNet 匹配，并双采样降低梯度偏差
- **Baseline** · 现有视频强化后训练
- **Benchmark** · 在线、回放、离线及少步视频生成
- **关键结果 / 消融** · 作者报告匹配残差界定到最优奖励倾斜分布的 KL，并在实验证明有效
- **适用条件 / 局限** · 摘要未给数据集及奖励细节

**可复用机制** · 离线生成后训练时比较点对点残差与依赖完整采样链的目标

<a id="paper-150018"></a>

## Efficient One-to-many Domain Translation via Diffusive Entropic Optimal Transport

[官方论文页](https://neurips.cc/virtual/2026/poster/150018) · [作者来源](https://openreview.net/forum?id=lMokHneWkz)

- **问题 / 瓶颈** · 高维生成分布的条件密度难直接估计
- **核心创新 / 方法** · 渐进加噪后以分数估计实现扩散熵，再联合分布匹配和传输成本
- **Baseline** · 多种一对多翻译方法
- **Benchmark** · 无配对域翻译，含一步及多步采样
- **关键结果 / 消融** · 报告同等多样性和成本下表现相当或更佳，并给出唯一性与零正则极限
- **适用条件 / 局限** · 理论条件及数据集待核

**可复用机制** · 高维一对多任务可在加噪分布上度量多样性并扫成本权重

<a id="paper-150130"></a>

## Efficient Prediction of Pass@k Scaling in Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150130) · [作者来源](https://openreview.net/forum?id=kSIarHMFfh)

- **问题 / 瓶颈** · 直接拟合在数据有限时外推不稳
- **核心创新 / 方法** · 采用 beta-binomial 估计并为更难的题目分配较多样本
- **Baseline** · 标准 pass@k 曲线拟合
- **Benchmark** · 重复采样能力估计，涉及数学及编程
- **关键结果 / 消融** · 作者报告更省计算且外推更可靠
- **适用条件 / 局限** · 实际使用应检查计算预算外推范围和置信区间，摘要未给数值

**可复用机制** · 预算有限时将逐题难度差异纳入重复采样能力审计

<a id="paper-155039"></a>

## Efficient Pre-Training with Token Superposition

[官方论文页](https://neurips.cc/virtual/2026/poster/155039) · [作者来源](https://openreview.net/forum?id=8td6EGze5A)

- **问题 / 瓶颈** · 逐 token 训练的单位算力数据吞吐受限
- **核心创新 / 方法** · 将相邻 token 合并、优化多热交叉熵，随后恢复标准目标
- **Baseline** · 常规预训练
- **Benchmark** · 270M、600M、3B 和 10B A1B MoE，比较损失和下游
- **关键结果 / 消融** · 10B A1B 等损失下预训练时间最多缩短 2.5 倍
- **适用条件 / 局限** · 袋化阶段损失顺序信息，恢复比例待核

**可复用机制** · 固定最终损失比较不同压缩训练与顺序恢复的预算分配

<a id="paper-149724"></a>

## Efficient Reasoning via Constrained Optimization in Latent Space

[官方论文页](https://neurips.cc/virtual/2026/poster/149724) · [作者来源](https://openreview.net/forum?id=nrBHRUPmWu)

- **问题 / 瓶颈** · 强制缩短推理可能删去必要步骤
- **核心创新 / 方法** · 找到高效推理的隐藏状态区域，用二次规划投影偏离状态，无需再训练
- **Baseline** · 关键词抑制及短推理策略，具名对照待核
- **Benchmark** · 4 个 1.5B 至 14B 模型，6 项数学、编程与科学问答
- **关键结果 / 消融** · 准确率最多提高 13.4%，生成 token 减少 11.8% 至 52.8%
- **适用条件 / 局限** · 依赖可访问隐藏状态；投影开销待核

**可复用机制** · 将生成长度与准确率联合评测，对照潜空间约束和长度上限

<a id="paper-152668"></a>

## Efficient Scaling of LLM Training with Flexible Context Parallelism

[官方论文页](https://neurips.cc/virtual/2026/poster/152668) · [作者来源](https://openreview.net/forum?id=RHltKicIIC)

- **问题 / 瓶颈** · 固定并行度在长度异质时造成负载不均与冗余通信
- **核心创新 / 方法** · 允许非二的幂的并行组，用多项式算法按批选择近似策略
- **Baseline** · Megatron-LM、DeepSpeed
- **Benchmark** · 长上下文 LLM 和多模态模型训练及极端不均衡批次
- **关键结果 / 消融** · 平均吞吐最多 1.47 倍，极端不均衡批次最多 2.24 倍
- **适用条件 / 局限** · 收益依赖集群拓扑及长度分布

**可复用机制** · 用每批序列长度做并行决策，并纳入毫秒级调度成本

<a id="paper-151165"></a>

## Efficient Serving for Dynamic Agent Workflows with Prediction-based KV-Cache Management

[官方论文页](https://neurips.cc/virtual/2026/poster/151165) · [作者来源](https://openreview.net/forum?id=cY4gQCRJvN)

- **问题 / 瓶颈** · 静态工作流假设不能处理动态分支和跨 Agent 复用
- **核心创新 / 方法** · 融合历史工作流及当前上下文预测调用，保守用于驱逐与预取
- **Baseline** · LRU 和 KVFlow
- **Benchmark** · 三个工作流基准，含动态和静态工作流
- **关键结果 / 消融** · 动态对 LRU 最多 1.85 倍，静态对 KVFlow 最多 1.26 倍
- **适用条件 / 局限** · 调用预测误差会浪费缓存或带宽

**可复用机制** · 把调用预测收益和误预测下的缓存损失一起评估

<a id="paper-155174"></a>

## Efficient Test-Time Adaptation For Robot Policies

[官方论文页](https://neurips.cc/virtual/2026/poster/155174) · [作者来源](https://openreview.net/forum?id=7k7qq6Pj9e)

- **问题 / 瓶颈** · 地形和载荷变化时价值外推可能过度自信
- **核心创新 / 方法** · 固定 critic，用熵正则缓解外推偏差，再优先回放低价值观测更新 actor
- **Baseline** · 不适配策略及只用冻结 critic 的轻量方案
- **Benchmark** · MuJoCo Playground 中 Go1、Go2、G1 四种偏移以及真实 Go2 负载
- **关键结果 / 消融** · 报告单设备最高改善 80%，真机优于不适配基线
- **适用条件 / 局限** · 仍依赖价值代理有效，真机证据限附加载荷

**可复用机制** · 用代理置信度和有限的难例记忆共同控制在线更新

<a id="paper-149626"></a>

## Efficient Test-time Adaptation through Candidate Verification and Divergence Shifts

[官方论文页](https://neurips.cc/virtual/2026/poster/149626) · [作者来源](https://openreview.net/forum?id=ofqsXmAtDS)

- **问题 / 瓶颈** · 迭代调整预测统计会带来额外开销
- **核心创新 / 方法** · 对 top-k 类别各自在记忆子空间重建特征，以假设插入后的最小聚合散度选类
- **Baseline** · 现有 VLM 测试时适配方法
- **Benchmark** · 15 个数据集上的五种设置
- **关键结果 / 消融** · 报告准确率改善，最多快 2 倍，内存开销降至三分之一以下
- **适用条件 / 局限** · 受候选召回和记忆覆盖限制

**可复用机制** · 固定候选池比较假设验证和参数更新的准确率及内存

<a id="paper-152500"></a>

## Efficient Tree Draft for Long-Context Speculative Decoding

[官方论文页](https://neurips.cc/virtual/2026/poster/152500) · [作者来源](https://openreview.net/forum?id=Sg8rYQS4Lz)

- **问题 / 瓶颈** · 长上下文中分支重复读前缀造成开销
- **核心创新 / 方法** · 使用利用受限树结构与共享前缀的专用算子，不改变采样逻辑
- **Baseline** · SGLang 原生树草稿
- **Benchmark** · 长上下文投机解码，测草稿阶段和总体吞吐
- **关键结果 / 消融** · 草稿最高快 2.66 倍，总吞吐最高 1.77 倍
- **适用条件 / 局限** · 依赖长上下文、树形草稿和底层算子支持

**可复用机制** · 测分支共享率与内存访问量，以确定是否进行前缀复用

<a id="paper-150778"></a>

## EgoForce: Robust Online Egocentric Motion Reconstruction via Diffusion Forcing

[官方论文页](https://neurips.cc/virtual/2026/poster/150778) · [作者来源](https://openreview.net/forum?id=fS4wDYJZpa)

- **问题 / 瓶颈** · 固定窗延迟，自回归易受噪声影响
- **核心创新 / 方法** · 非对称噪声调度结合稳健缺失补全随观测更新动作
- **Baseline** · 固定窗生成和自回归
- **Benchmark** · 在线第一视角全身重建
- **关键结果 / 消融** · 具体幅度待核
- **适用条件 / 局限** · 依赖可用头部与间歇手部证据

**可复用机制** · 流式估计中允许近期状态保留更高不确定性

<a id="paper-154591"></a>

## EgoMo3R: Joint Egocentric Motion and Scene Reconstruction

[官方论文页](https://neurips.cc/virtual/2026/poster/154591) · [作者来源](https://openreview.net/forum?id=CRnKeP6gZr)

- **问题 / 瓶颈** · 头戴图像模糊导致相机估计不稳
- **核心创新 / 方法** · 将深度、光流与点轨迹结合人运动扩散先验交替优化
- **Baseline** · 依赖外部度量相机轨迹的方案
- **Benchmark** · 单目第一视角人体和场景重建
- **关键结果 / 消融** · 数值待核
- **适用条件 / 局限** · 遮挡或几何特征失败会影响两项估计

**可复用机制** · 将两项重建共享证据并对照独立求解

<a id="paper-139373"></a>

## EgoStream: A Diagnostic Benchmark for Streaming Episodic Memory in Egocentric Vision

[官方论文页](https://neurips.cc/virtual/2026/poster/139373) · [作者来源](https://openreview.net/forum?id=UDecnw8V7B)

- **问题 / 瓶颈** · 时变世界中的错误答案未必意味着遗忘
- **核心创新 / 方法** · 标注答案有效时间并改变召回时刻
- **Baseline** · 统一流式框架中的多种记忆管理
- **Benchmark** · 2250 题、七类记忆共 8528 次评测
- **关键结果 / 消融** · 可比较不同延迟下的召回，量化待核
- **适用条件 / 局限** · 依赖时间窗标注质量

**可复用机制** · 为动态任务标注事实失效时刻再测试长期记忆

<a id="paper-151402"></a>

## EgoTac: In-the-wild Tactile Prediction from Egocentric Vision

[官方论文页](https://neurips.cc/virtual/2026/poster/151402) · [作者来源](https://openreview.net/forum?id=awVMKr9gzw)

- **问题 / 瓶颈** · 视频丰富但触觉标注难采
- **核心创新 / 方法** · 用连续力和二值接触两类监督训练推断
- **Baseline** · 已有接触估计器
- **Benchmark** · 域内力与域外接触
- **关键结果 / 消融** · 域内平均误差低于 0.06 N，作者报告域外接触改善
- **适用条件 / 局限** · 不可见受力歧义仍存在

**可复用机制** · 测试代理触觉时分开报告力精度和接触泛化

<a id="paper-153762"></a>

## EIHMR: Collaborative Human-Camera Estimation for Global Human Mesh Recovery

[官方论文页](https://neurips.cc/virtual/2026/poster/153762) · [作者来源](https://openreview.net/forum?id=IrOkEc6m95)

- **问题 / 瓶颈** · 运动相机与人体运动误差叠加
- **核心创新 / 方法** · 在冻结关键帧中细化局部人体并用重渲染辅助相机估计
- **Baseline** · 独立两阶段流程
- **Benchmark** · 单目全局人体网格恢复
- **关键结果 / 消融** · 幅度待核
- **适用条件 / 局限** · 依赖关键帧与度量深度

**可复用机制** · 比较静态参考视角反馈与两阶段估计的误差传播

<a id="paper-150112"></a>

## EIPO: Efficient Inter-Step Parallel Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/150112) · [作者来源](https://openreview.net/forum?id=kbZJJPpafP)

- **问题 / 瓶颈** · 顺序更新制约训练时延
- **核心创新 / 方法** · 建立恢复原轨迹的预条件非线性系统，用动量缓冲提取多割线信息
- **Baseline** · 顺序 SGD、Adam 和经典 Anderson 加速
- **Benchmark** · 理论轨迹收敛及训练运行时间
- **关键结果 / 消融** · 作者证明少于顺序步数的收敛，实测待核
- **适用条件 / 局限** · 并行资源和单轮成本决定实际收益

**可复用机制** · 对照迭代数量和实际墙钟时间并检查轨迹一致性

<a id="paper-152639"></a>

## Elastic Representations via Hyperbolic Geometry

[官方论文页](https://neurips.cc/virtual/2026/poster/152639) · [作者来源](https://openreview.net/forum?id=RVWViB6PQ7)

- **问题 / 瓶颈** · 固定嵌入维度难适应预算变化
- **核心创新 / 方法** · 用双曲几何学习非线性维度适配
- **Baseline** · Matryoshka Representation Learning、CSR
- **Benchmark** · 维度变化下的嵌入任务
- **关键结果 / 消融** · 量化细项待核
- **适用条件 / 局限** · 额外适配器与几何代价仍需测

**可复用机制** · 同时扫描缩减与扩展维度，报告质量和成本

<a id="paper-154798"></a>

## Elastic Spectral State Space Models for Train-Once Budgeted Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/154798) · [作者来源](https://openreview.net/forum?id=Asn9eGOVdP)

- **问题 / 瓶颈** · 固定序列模型需为不同设备重复训练
- **核心创新 / 方法** · 以 Hankel 谱通道逼近状态空间算子，并用门控及预算 dropout 训练不同前缀
- **Baseline** · 固定容量与宽度等裁剪；具名对照待核
- **Benchmark** · 多预算序列建模
- **关键结果 / 消融** · 量化待核
- **适用条件 / 局限** · 不同任务的谱集中度可能不同

**可复用机制** · 在训练时直接暴露部署所用的截断带宽

<a id="paper-150432"></a>

## ElegantVLA: Learning When to Think for Efficient Vision-Language-Action Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150432) · [作者来源](https://openreview.net/forum?id=i69xSliZFV)

- **问题 / 瓶颈** · 逐步固定算力忽略阶段难度
- **核心创新 / 方法** · 用轻量调度器做阶段自适应的模型内算力分配
- **Baseline** · 固定规则的 VLA 加速
- **Benchmark** · 实时机器人操作
- **关键结果 / 消融** · 延迟和成功率数值待核
- **适用条件 / 局限** · 调度误判可能影响关键阶段

**可复用机制** · 同时记录算力节省、失败发生阶段和操作成功

<a id="paper-148278"></a>

## ELF: Embedded Language Flows

[官方论文页](https://neurips.cc/virtual/2026/poster/148278) · [作者来源](https://openreview.net/forum?id=z3I6Aj563f)

- **问题 / 瓶颈** · 主流扩散语言模型依赖离散转移
- **核心创新 / 方法** · 在连续嵌入空间做时间连续的流匹配，末步共享权重解码
- **Baseline** · 离散扩散语言模型
- **Benchmark** · 语言生成，具名基准待核
- **关键结果 / 消融** · 作者报告优于所比离散模型，数值待核
- **适用条件 / 局限** · 依赖末步解码稳定性与采样预算

**可复用机制** · 固定采样预算比较连续空间与逐步离散化

<a id="paper-151632"></a>

## Elicited Adaptation: Auditable Localized Fairness via Pairwise Queries

[官方论文页](https://neurips.cc/virtual/2026/poster/151632) · [作者来源](https://openreview.net/forum?id=Z83ygLoc4N)

- **问题 / 瓶颈** · 全局公平标准难覆盖不同群体
- **核心创新 / 方法** · 以成对问询拟合局部距离和容差，在留出问询上验证
- **Baseline** · 平均及匹配准确率的全局个体公平
- **Benchmark** · Stress K=5、Adult-K3-human，十种子
- **关键结果 / 消融** · 作者报告局部模型在准确率和严格违规率上处于帕累托前沿
- **适用条件 / 局限** · 依赖群体反馈代表性与距离形式

**可复用机制** · 把公平目标征询与审计分开采样，分别报告分组违规率
