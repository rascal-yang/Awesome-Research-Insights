# NeurIPS 2026 论文卡 5

[会议索引](README.md)

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

<a id="paper-139147"></a>

## Evaluating Synthetic ECG Pretraining: When Can Patient-Free Simulators Substitute for Real ECG Data?

[官方论文页](https://neurips.cc/virtual/2026/poster/139147) · [作者来源](https://openreview.net/forum?id=iJc0X3nEby)

- **问题 / 瓶颈** · 迁移协议会改变模拟数据的比较结论
- **核心创新 / 方法** · 固定编码器与MAE目标，比较来源和匹配样本预算
- **Baseline** · 真实信号、模拟器、VAE、DCGAN及扩散
- **Benchmark** · PTB-XL、G12EC、CPSC2018的26项任务及F1
- **关键结果 / 消融** · 十万样本时SimECG-N在22项排首位，冻结探针仍受益于真实异常暴露
- **适用条件 / 局限** · 结论限于单导联和所测协议

**可复用机制** · 分别用冻结探针和全量微调判断合成数据是否可替代实测。在匹配预算下复查适用边界。

<a id="paper-139634"></a>

## Evaluating Test-Time Scaling of General LLM Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/139634) · [作者来源](https://openreview.net/forum?id=EDfvwinqmW)

- **问题 / 瓶颈** · 额外算力未必改善异质任务表现
- **核心创新 / 方法** · 控制预算扫描顺序交互和轨迹采样
- **Baseline** · 十种Agent与不同测试时预算
- **Benchmark** · 搜索、编码、推理和工具使用统一评测
- **关键结果 / 消融** · 两种扩展均未稳定获益，分别受平台期和验证不足限制
- **适用条件 / 局限** · 依赖任务分布和结果验证器

**可复用机制** · 分别测增加交互步数和并行轨迹的边际收益。在匹配预算下复查适用边界。

<a id="paper-138974"></a>

## Evaluating Uncertainty Calibration in Probabilistic Time Series Foundation Models

[官方论文页](https://neurips.cc/virtual/2026/poster/138974) · [作者来源](https://openreview.net/forum?id=t3VdYykgSV)

- **问题 / 瓶颈** · 汇总误差掩盖特定时距的失准
- **核心创新 / 方法** · 拆分总体、步长和条件校准，比较事后修正
- **Baseline** · 常用模型及重校准方法，具名待核
- **Benchmark** · 多数据集概率预测
- **关键结果 / 消融** · 不同模型呈系统失准，事后校准仅能改善部分口径
- **适用条件 / 局限** · 摘要未给定量幅度及数据集清单

**可复用机制** · 按预测步长和条件分别测不确定性校准。在匹配预算下复查适用边界。

<a id="paper-148437"></a>

## Evaluation Awareness in Language Models Has Limited Effect on Behaviour

[官方论文页](https://neurips.cc/virtual/2026/poster/148437) · [作者来源](https://openreview.net/forum?id=xp2oWSnMPf)

- **问题 / 瓶颈** · 推理中说正在被评测并不等于策略性改变
- **核心创新 / 方法** · 对照自然出现与受控文本变化下的答案分布
- **Baseline** · 有无明确评测意识的配对对照
- **Benchmark** · 开放权重模型的安全、对齐、道德与观点测试
- **关键结果 / 消融** · 自然出现时最大偏移3.7个百分点，受控比较效应较小
- **适用条件 / 局限** · 仅衡量表述与所测行为，不涵盖隐性意识

**可复用机制** · 用行为差异验证评测意识，避免只看自述频率。在匹配预算下复查适用边界。

<a id="paper-150183"></a>

## Event based Multi-Velocity-Scale Imaging

[官方论文页](https://neurips.cc/virtual/2026/poster/150183) · [作者来源](https://openreview.net/forum?id=k6FlyTwE3g)

- **问题 / 瓶颈** · 全局固定阈值在高速冗余与慢速细节丢失间取舍
- **核心创新 / 方法** · 多阈值成像并在现有事件相机实现采集
- **Baseline** · 统一对比阈值
- **Benchmark** · 合成与真实混合速度场景
- **关键结果 / 消融** · 保留结构及快速动态同时减少事件，数值待核
- **适用条件 / 局限** · 阈值如何随场景变化待查

**可复用机制** · 按运动尺度分配对比度阈值。在匹配预算下复查适用边界。

<a id="paper-151283"></a>

## Event-Grounded Sparse Autoencoders for Vision-Language-Action Policies

[官方论文页](https://neurips.cc/virtual/2026/poster/151283) · [作者来源](https://openreview.net/forum?id=bY6Sy7BOHn)

- **问题 / 瓶颈** · 机器人动作难像文字一样解释，滚动验证昂贵
- **核心创新 / 方法** · 按视觉状态及时间聚类末端关键帧对齐行为事件
- **Baseline** · 非事件排序与不同干预位置
- **Benchmark** · 两类仿真架构和真机试验
- **关键结果 / 消融** · OpenVLA效果最强并迁移至连续动作块
- **适用条件 / 局限** · 架构与干预位置影响结果，强干预不宜部署

**可复用机制** · 用闭环行为事件排序稀疏自编码器特征。在匹配预算下复查适用边界。

<a id="paper-153545"></a>

## EventLens: Event-Structure Reinforcement Learning for Video Understanding

[官方论文页](https://neurips.cc/virtual/2026/poster/153545) · [作者来源](https://openreview.net/forum?id=Ka48Llurl6)

- **问题 / 瓶颈** · 字幕训练可走语言捷径并漏掉事件关系
- **核心创新 / 方法** · 用切分、发展和事件关系任务分别训练再作多教师蒸馏
- **Baseline** · 直接混合强化学习
- **Benchmark** · Qwen3-VL上的时间定位、事件推理和视频问答
- **关键结果 / 消融** · 作者报告时序改善、通用问答保持且训练成本下降
- **适用条件 / 局限** · 依赖结构扰动任务和确定性奖励覆盖

**可复用机制** · 用可验证的事件结构任务替代单纯字幕监督。在匹配预算下复查适用边界。

<a id="paper-151793"></a>

## EventPrune: Cascaded Event-Assisted Token Pruning for Efficient First-Person Dynamic Spatial Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/151793) · [作者来源](https://openreview.net/forum?id=XyYCbuAP7m)

- **问题 / 瓶颈** · 静态剪枝易丢掉短时运动细节
- **核心创新 / 方法** · 先选运动关键帧再筛区域并融合事件和注意力信号
- **Baseline** · 完整视觉token
- **Benchmark** · 动态空间推理和ESR-Real
- **关键结果 / 消融** · 剪80%后37.62%对36.31%，推理快1.89倍
- **适用条件 / 局限** · 依赖事件传感器及RGB同步，静态信息可能被削弱

**可复用机制** · 用异步事件信号给视频token排序保留动态区域。在匹配预算下复查适用边界。

<a id="paper-153421"></a>

## Events as Triggers for Behavioral Diversity in Multi-Agent Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/153421) · [作者来源](https://openreview.net/forum?id=LSRtfZfGAE)

- **问题 / 瓶颈** · 固定身份绑定限制协作
- **核心创新 / 方法** · 以行为流形度量瞬态角色差异，按事件生成共享策略的 LoRA
- **Baseline** · 固定角色及已有多智能体方法
- **Benchmark** · 角色轮换与零样本泛化任务
- **关键结果 / 消融** · 作者报告只有该方法解出连续换角任务
- **适用条件 / 局限** · 依赖事件定义

**可复用机制** · 对照事件触发适配与固定身份或固定步长切换

<a id="paper-154368"></a>

## Every Bit, Everywhere, All At Once: A Binomial Multibit LLM Watermark

[官方论文页](https://neurips.cc/virtual/2026/poster/154368) · [作者来源](https://openreview.net/forum?id=E6Jp4SaVf6)

- **问题 / 瓶颈** · 整条消息准确率难定位不可靠位
- **核心创新 / 方法** · 作者对比逐位置信度和总体恢复指标
- **Baseline** · 八种水印基线
- **Benchmark** · 最多 64 位载荷，比较恢复和低失真区间
- **关键结果 / 消融** · 作者报告大载荷及低失真下优势更明显
- **适用条件 / 局限** · 具体编辑和文本条件待核

**可复用机制** · 在同等失真下报告各位恢复分布

<a id="paper-155361"></a>

## Every Sample Counts: Supervised Fine-Tuning of Language Models with Pointwise Constraints

[官方论文页](https://neurips.cc/virtual/2026/poster/155361) · [作者来源](https://openreview.net/forum?id=6BYu5yc6pZ)

- **问题 / 瓶颈** · 平均约束会隐去难例
- **核心创新 / 方法** · 增广拉格朗日约束各样本，并学习最小必要的松弛
- **Baseline** · 平均约束微调
- **Benchmark** · 小语言模型的指令安全、函数调用偏好及长度排序
- **关键结果 / 消融** · 作者报告尾部违反下降，下游性能大体保持
- **适用条件 / 局限** · 松弛与外点比例关系待核

**可复用机制** · 比较平均和逐样本约束时同时报告尾部和总体性能

<a id="paper-150103"></a>

## Everything at Every Scale: Scale-Invariant Diffusion with Continuous Super-Resolution

[官方论文页](https://neurips.cc/virtual/2026/poster/150103) · [作者来源](https://openreview.net/forum?id=kftOqseEy5)

- **问题 / 瓶颈** · 不同放大倍数通常需分别调节
- **核心创新 / 方法** · 前向按频带由细到粗衰减并加入匹配频谱噪声
- **Baseline** · 条件超分模型
- **Benchmark** · CIFAR-10 无条件生成、ImageNet 2–8 倍超分、Ising 重建
- **关键结果 / 消融** · CIFAR-10 FID 2.65，IS 9.63
- **适用条件 / 局限** · 尺度不变假设可能不适用于特殊成像链

**可复用机制** · 检验按频率退化的同一检查点能否覆盖多级逆问题

<a id="paper-152262"></a>

## EviAttr-OW: Evidential Attribute Reasoning for Open World Object Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/152262) · [作者来源](https://openreview.net/forum?id=UNSLchC9SB)

- **问题 / 瓶颈** · 已知类别偏置使未知目标难识别
- **核心创新 / 方法** · 用类无关属性及 Dirichlet 证据衡量已知类支持不足
- **Baseline** · 已有开放世界检测器
- **Benchmark** · RWD 五个现实应用数据集，未知类 mAP
- **关键结果 / 消融** · 未知类 mAP 增加 7.3
- **适用条件 / 局限** · 证据质量取决于属性覆盖

**可复用机制** · 单独测物体存在和分类确信度校准

<a id="paper-150393"></a>

## Evidence-RL: Towards Evidence-intensive Visual Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/150393) · [作者来源](https://openreview.net/forum?id=iOZY3TyfNU)

- **问题 / 瓶颈** · 全局图像扰动无法隔离证据
- **核心创新 / 方法** · 中和对象证据并和匹配非证据区比较，结合正确性做 GRPO
- **Baseline** · 既有强化后训练
- **Benchmark** · 九个公开基准、四个骨干
- **关键结果 / 消融** · 作者报告优于基线且无额外推理开销
- **适用条件 / 局限** · 依赖弱对象候选和匹配质量

**可复用机制** · 用反事实证据与对照区验证模型是否走视觉捷径

<a id="paper-154010"></a>

## Evidential Semantic Uncertainty Decomposition for Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154010) · [作者来源](https://openreview.net/forum?id=GsfbZh21T3)

- **问题 / 瓶颈** · 语义熵只度量采样分散
- **核心创新 / 方法** · 用轻量探针保留可靠证据，并设置未获支持类
- **Baseline** · 语义不确定性及扰动分解方法
- **Benchmark** · 四种骨干，分布外及歧义检测 AUROC 和 AUPR
- **关键结果 / 消融** · 摘要报告平均 AUROC 分别升 7.4% 和 4%
- **适用条件 / 局限** · 依赖聚类和采样质量

**可复用机制** · 分别校准语义冲突与证据缺失

<a id="paper-150339"></a>

## EVIDENT: Routing MLLM Adaptation through Entity-Grounded Visual Evidence for Cross-Domain Video Temporal Grounding

[官方论文页](https://neurips.cc/virtual/2026/poster/150339) · [作者来源](https://openreview.net/forum?id=irDPXJ2g3y)

- **问题 / 瓶颈** · 换视觉域后时间知识难与实体注意力结合
- **核心创新 / 方法** · 以实体瓶颈、绑定蒸馏与证据门控定位时间段
- **Baseline** · 普通多模态微调
- **Benchmark** · 跨域视频时间定位
- **关键结果 / 消融** · 作者报告域外改善且域内表现有竞争力
- **适用条件 / 局限** · 依赖实体可识别性

**可复用机制** · 固定参数预算比较实体证据瓶颈与密集-token 适配

<a id="paper-139527"></a>

## EvoCodeBench: Evaluating Coding Agents in Multi-Turn Iterative Interactions

[官方论文页](https://neurips.cc/virtual/2026/poster/139527) · [作者来源](https://openreview.net/forum?id=KUMjFWdsDg)

- **问题 / 瓶颈** · 单轮评测看不到持久代码状态的退化
- **核心创新 / 方法** · 保留工作区并同时验证新旧有效需求
- **Baseline** · 从参考完成状态起步的单轮评测
- **Benchmark** · 26 个常规编程任务、227 轮，MT@4 及 SR
- **关键结果 / 消融** · 多数模型单轮分高 22–40 分
- **适用条件 / 局限** · 结论依赖任务及累计测试覆盖

**可复用机制** · 迭代开发基准应保留工作区并重测旧约束

<a id="paper-153228"></a>

## EvoCUA: Evolving Computer Use Agents via Learning from Scalable Synthetic Experience

[官方论文页](https://neurips.cc/virtual/2026/poster/153228) · [作者来源](https://openreview.net/forum?id=MpUzZIp5jZ)

- **问题 / 瓶颈** · 静态示范缺少长程纠错
- **核心创新 / 方法** · 在封闭沙盒合成良性界面任务，以验证结果筛选并修正执行轨迹
- **Baseline** · OpenCUA-72B、UI-TARS-2
- **Benchmark** · OSWorld 桌面操作成功率
- **关键结果 / 消融** · 报告 56.7%，相对对照为 45.0% 和 53.1%
- **适用条件 / 局限** · 合成任务覆盖限制迁移

**可复用机制** · 评估获授权的桌面自动化时对照静态模仿与含纠错轨迹训练

<a id="paper-154131"></a>

## Evo-Depth: A Lightweight Depth-Enhanced Vision-Language-Action Model

[官方论文页](https://neurips.cc/virtual/2026/poster/154131) · [作者来源](https://openreview.net/forum?id=G2jacreNCB)

- **问题 / 瓶颈** · 显式深度或大几何模型增加部署成本
- **核心创新 / 方法** · 以轻量隐式深度模块调制视觉语言表示并逐步对齐动作
- **Baseline** · 显式及隐式三维 VLA 方法
- **Benchmark** · 四个仿真基准与真机成功率、显存和推理频率
- **关键结果 / 消融** · 作者报告 0.9B 模型在真机成功率及资源指标有优势
- **适用条件 / 局限** · 依赖多视角图像

**可复用机制** · 固定传感硬件对比轻量几何调制与 RGB 直接输入

<a id="paper-149312"></a>

## Evolutionary System Prompt Learning for Reinforcement Learning in LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/149312) · [作者来源](https://openreview.net/forum?id=r7HI4UDi9z)

- **问题 / 瓶颈** · 只更新一处可能限制泛化。
- **核心创新 / 方法** · 并行用多条系统提示采样，权重用强化学习更新，提示用模型反思迭代。
- **Baseline** · 仅 RL、仅提示演化。
- **Benchmark** · AIME、BeyondAIME、HMMT 和智能体搜索。
- **关键结果 / 消融** · AIME 到 BeyondAIME 成功率由 38.8% 到 45.1%。
- **适用条件 / 局限** · 收益可能受候选提示预算和训练奖励影响。

**可复用机制** · 固定采样预算分别消融语言上下文更新与参数更新。

<a id="paper-148564"></a>

## Evolution Fine-Tuning: Learning to Discover Across 371 Optimization Tasks

[官方论文页](https://neurips.cc/virtual/2026/poster/148564) · [作者来源](https://openreview.net/forum?id=www9RVeEpg)

- **问题 / 瓶颈** · 对单题执行搜索会丢弃演化经验。
- **核心创新 / 方法** · 收集跨领域搜索轨迹，并以其微调开放模型。
- **Baseline** · 同一底座未经该中训练；另与测试时 RL 组合。
- **Benchmark** · 371 种优化任务的轨迹库，22 项留出任务。
- **关键结果 / 消融** · 留出任务较底座平均提高 10.22%。
- **适用条件 / 局限** · 留出任务与训练族相似程度须复核。

**可复用机制** · 训练求解器时比较学习整个候选改进过程与学习最终解。

<a id="paper-155640"></a>

## EvoOptiGraph: Weakness-Driven Coevolution via Graph-Based Structural Generation for Optimization Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/155640) · [作者来源](https://openreview.net/forum?id=45RetuO3zX)

- **问题 / 瓶颈** · 静态自然语言转优化训练集缺结构多样性。
- **核心创新 / 方法** · 用二分图表示 MILP，经保有效性变换、编译及回译验证生成题目。
- **Baseline** · 较大通用模型、智能体和领域方法。
- **Benchmark** · 六个公开优化建模数据集。
- **关键结果 / 消融** · 作者报告准确性、可执行性及泛化改善，数值待核。
- **适用条件 / 局限** · 依赖图变换及求解器验证。

**可复用机制** · 对可形式化输出，用失败结构生成新的可验证实例。

<a id="paper-149899"></a>

## Exact Channel Decoupling via Joint Diagonalization and Uniform Splicing for Diffusion Transformer Quantization

[官方论文页](https://neurips.cc/virtual/2026/poster/149899) · [作者来源](https://openreview.net/forum?id=mO4pYQLElU)

- **问题 / 瓶颈** · 只平滑激活会遗留权重量化方差。
- **核心创新 / 方法** · 用广义特征问题联合对角化，并以 token 拼接替代时间平均。
- **Baseline** · 既有后训练量化基线。
- **Benchmark** · W3A4 的 DiT-XL/2 与 PixArt-Sigma。
- **关键结果 / 消融** · 摘要报告 FID 分别下降 16.06 和 6.49。
- **适用条件 / 局限** · 不同位宽或校准分布的稳健性待核。

**可复用机制** · 量化时同时诊断权重、激活和校准样本如何跨时间聚合。

<a id="paper-154073"></a>

## Exact Flow Linear Attention: Exact Solution from Continuous-Time Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/154073) · [作者来源](https://openreview.net/forum?id=GOjRwLmiSD)

- **问题 / 瓶颈** · 一阶离散在高能输入下引入误差。
- **核心创新 / 方法** · 用秩一结构化简连续动力学的指数和输入积分。
- **Baseline** · 欧拉型线性注意力与 SSM。
- **Benchmark** · 语言建模、MAD 与扰动测试。
- **关键结果 / 消融** · 作者报告稳定性和困惑度改善，维持线性复杂度与并行。
- **适用条件 / 局限** · 结果依赖秩一动力学结构。

**可复用机制** · 先辨别状态更新的离散误差，再比较精确积分和普通迭代。

<a id="paper-155943"></a>

## Exact Gaussian Moment Matching for Residual Networks: a Second-Order Method

[官方论文页](https://neurips.cc/virtual/2026/poster/155943) · [作者来源](https://openreview.net/forum?id=1dsxDeHdpR)

- **问题 / 瓶颈** · 残差网络中的近似矩误差逐层累积。
- **核心创新 / 方法** · 推导 probit、GeLU、ReLU 等激活的均值协方差匹配，包含残差连接。
- **Baseline** · 流行近似、确定性推理与蒙特卡洛参考。
- **Benchmark** · 随机网络及变分贝叶斯网络，用 KL 测误差。
- **关键结果 / 消融** · 随机网络最高报告百万倍 KL 误差改善，贝叶斯网络约百倍。
- **适用条件 / 局限** · 逐层正态化仍是近似。

**可复用机制** · 将局部激活矩误差与整网分布误差分开评估。

<a id="paper-153709"></a>

## Exact Instance Compression for Convex Empirical Risk Minimization via Color Refinement

[官方论文页](https://neurips.cc/virtual/2026/poster/153709) · [作者来源](https://openreview.net/forum?id=JM5piPXaA4)

- **问题 / 瓶颈** · 凸求解器在完整实例上也可能成本高。
- **核心创新 / 方法** · 以颜色细化识别可合并结构，再求解压缩目标。
- **Baseline** · 原始凸 ERM 及既有线性二次规划压缩。
- **Benchmark** · 回归、逻辑分类、弹性网和核模型。
- **关键结果 / 消融** · 提供无损框架，摘要报告数值有效性。
- **适用条件 / 局限** · 依赖可识别对称结构，压缩幅度因实例而异。

**可复用机制** · 先核验目标的等价分组，再比较原始和压缩求解。

<a id="paper-155154"></a>

## Exact Posterior Score Estimation for Solving Linear Inverse Problems

[官方论文页](https://neurips.cc/virtual/2026/poster/155154) · [作者来源](https://openreview.net/forum?id=7u8YcL4Z4P)

- **问题 / 瓶颈** · 直接用无条件分数需近似测量校正。
- **核心创新 / 方法** · 把线性高斯后验分数化成算子相关移位与各向异性噪声下的去噪。
- **Baseline** · 训练免调与训练式逆问题方法。
- **Benchmark** · FFHQ、ImageNet 五种线性逆问题。
- **关键结果 / 消融** · 摘要报告多种保真指标改善及约少一个数量级的调用。
- **适用条件 / 局限** · 依赖线性高斯观测条件。

**可复用机制** · 先推导观测可否化为去噪条件，再比较训练改造和推理梯度引导。

<a id="paper-155888"></a>

## Exact Regular-Constrained Sampling for Variable-Order Markov Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/155888) · [作者来源](https://openreview.net/forum?id=25TuIlUEUu)

- **问题 / 瓶颈** · 一阶状态合并了生成器要区分的历史。
- **核心创新 / 方法** · 在可达乘积边上运行精确动态规划。
- **Baseline** · 一阶约束信念传播及小规模枚举。
- **Benchmark** · 枚举校验和 Bach 前奏曲，最大历史阶 6。
- **关键结果 / 消融** · 获得精确配分函数，复杂度随时域和可达边线性增长。
- **适用条件 / 局限** · 仅适用于可有限自动机描述的约束。

**可复用机制** · 保留模型实际上下文状态，在其与规则的乘积图上采样。

<a id="paper-148463"></a>

## Exact Topological Compliance: Generating Persistence-Equivalent Graphs

[官方论文页](https://neurips.cc/virtual/2026/poster/148463) · [作者来源](https://openreview.net/forum?id=xcQkqD4abA)

- **问题 / 瓶颈** · 软约束只保证拓扑描述近似相似。
- **核心创新 / 方法** · 以局部构造和全局约束编码实现目标持久性图。
- **Baseline** · 软拓扑正则与局部全局构造对照。
- **Benchmark** · 四个图生成基准，检验目标描述匹配。
- **关键结果 / 消融** · 两种方法均精确匹配，局部法有多样性与不可行状态取舍。
- **适用条件 / 局限** · 全局开销受求解难度影响。

**可复用机制** · 若拓扑一致性是硬需求，单列匹配率和生成多样性。

<a id="paper-152457"></a>

## Exact Unlearning via Quantized Sufficient Statistics

[官方论文页](https://neurips.cc/virtual/2026/poster/152457) · [作者来源](https://openreview.net/forum?id=SyxiOl962F)

- **问题 / 瓶颈** · 分片重训仍随数据规模付出代价。
- **核心创新 / 方法** · 冻结小样本训练的索引结构，对其余样本维护可加累加量。
- **Baseline** · SISA。
- **Benchmark** · 15 个视觉文本表格数据集，测精度及预期删除时间。
- **关键结果 / 消融** · 作者报告预期删除速度提高 3–645 倍，但部分数据集准确率落后。
- **适用条件 / 局限** · 删除到索引训练样本需重建，精度受量化及类数影响。

**可复用机制** · 将高频数据更新与低频结构重建分开统计延迟和精度。

<a id="paper-154319"></a>

## ExComm: Exploration-Stage Communication for Error-Resilient Agentic Test-Time Scaling

[官方论文页](https://neurips.cc/virtual/2026/poster/154319) · [作者来源](https://openreview.net/forum?id=EXtXoqNLl3)

- **问题 / 瓶颈** · 早期错误污染后续推理
- **核心创新 / 方法** · 定期找分支事实冲突，经工具验证后追加软反馈并分散重复轨迹
- **Baseline** · 测试时扩展与通信方法
- **Benchmark** · AIME 2024、2025 和 GAIA
- **关键结果 / 消融** · 两骨干较最强对照平均提升 5.7% 与 5.0%
- **适用条件 / 局限** · 共同犯错时冲突信号不足

**可复用机制** · 固定预算对比早期核验和末端筛选

<a id="paper-150839"></a>

## Exemplar2VQA: A Scalable Exemplar-Driven Visual Question Answering Generation Framework via Multi-Agent Coding

[官方论文页](https://neurips.cc/virtual/2026/poster/150839) · [作者来源](https://openreview.net/forum?id=evkWoqTEUD)

- **问题 / 瓶颈** · 语言模型直接合成三维问题容易算错
- **核心创新 / 方法** · 多代理从模板扩写任务，以几何工具执行得到标签
- **Baseline** · Qwen2.5-VL 3B 和 7B 微调对照细节待核
- **Benchmark** · 室内、室外及混合空间问答
- **关键结果 / 消融** · 作者报告合成室内数据改善多种设置
- **适用条件 / 局限** · 依赖仿真场景和问题模板覆盖

**可复用机制** · 让确定性程序计算标签，模型负责扩写

<a id="paper-148905"></a>

## Existence Precedes Value: Joint Modeling of Observational Existence and Evolving States in Time Series Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/148905) · [作者来源](https://openreview.net/forum?id=uIvgvH7DE2)

- **问题 / 瓶颈** · 测试时未来有效时间戳未知
- **核心创新 / 方法** · 观测流和数值流通过可靠性嵌入、依赖建模与联合输出耦合
- **Baseline** · 先插补和连续时间预测；具名对照待核
- **Benchmark** · Glimpse 自然缺失及工业数据
- **关键结果 / 消融** · 作者报告一致改善，幅度待核
- **适用条件 / 局限** · 观测机制变化需要单独验证

**可复用机制** · 用未知观测时间戳的设置测试预测器

<a id="paper-155702"></a>

## Expanding Flow Maps

[官方论文页](https://neurips.cc/virtual/2026/poster/155702) · [作者来源](https://openreview.net/forum?id=3aX1lzdpqZ)

- **问题 / 瓶颈** · 固定维流映射不能直接改变序列长度
- **核心创新 / 方法** · 把流映射分成维度扩展和输运，可在离散单纯形插入 token
- **Baseline** · 固定画布流映射
- **Benchmark** · 连续与离散变长生成，数据集待核
- **关键结果 / 消融** · 固定画布是恒等扩展的特例
- **适用条件 / 局限** · 成本和质量随长度变化的实测待核

**可复用机制** · 将输出大小作为生成决策独立评估

<a id="paper-152089"></a>

## Expanding LLM Agent Boundaries with Strategy-Guided Exploration

[官方论文页](https://neurips.cc/virtual/2026/poster/152089) · [作者来源](https://openreview.net/forum?id=VaJZqNyAXo)

- **问题 / 瓶颈** · 稀疏奖励下逐动作试探效率低
- **核心创新 / 方法** · 以语言策略条件化环境动作，混合温度并从历史结果反思
- **Baseline** · 探索导向 RL 方法
- **Benchmark** · 普通 UI 操作和具身任务
- **关键结果 / 消融** · 作者报告效率和最终表现提升
- **适用条件 / 局限** · 依赖策略描述能落实为动作

**可复用机制** · 在同等任务交互预算比较策略级和动作级探索

<a id="paper-154399"></a>

## Expected Batch Optimal Transport Plans and Consequences for Flow Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/154399) · [作者来源](https://openreview.net/forum?id=Drh2loVsgL)

- **问题 / 瓶颈** · 随机批次输运不等于全局最优输运
- **核心创新 / 方法** · 用期望批次方案描述诱导耦合并推导半离散收敛率
- **Baseline** · 精确 OT 和不同批大小
- **Benchmark** · 两原子模型及合成和图像实验
- **关键结果 / 消融** · 证明大批一致性与半离散速率
- **适用条件 / 局限** · 速率依赖半离散假设

**可复用机制** · 同时测增大批量对耦合和积分误差的影响

<a id="paper-139760"></a>

## Expected Harm: Rethinking Safety Evaluation of (Mis)Aligned LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/139760) · [作者来源](https://openreview.net/forum?id=6SIPt7cfSm)

- **问题 / 瓶颈** · 只用严重性无法反映部署风险
- **核心创新 / 方法** · 以现实可执行性作为独立的防御评估维度，并检查阶段训练是否校准
- **Baseline** · 严重性单独评分
- **Benchmark** · 模型安全评估和 Olmo-3 阶段检查
- **关键结果 / 消融** · 作者观察到拒答与现实风险错位
- **适用条件 / 局限** · 可能性估计依赖使用环境

**可复用机制** · 部署审计可按两个维度分层检查遗漏

<a id="paper-149912"></a>

## ExperiGen: Agentic Hypothesis Discovery from Observational Data

[官方论文页](https://neurips.cc/virtual/2026/poster/149912) · [作者来源](https://openreview.net/forum?id=mHGzwFfdQI)

- **问题 / 瓶颈** · 预测增益可能出自伪相关
- **核心创新 / 方法** · 两个代理分别提出假设和操作化检验，用接受与拒绝记录引导后续
- **Baseline** · 已有假设生成方法
- **Benchmark** · 19 项跨领域任务及预注册和 A/B 验证
- **关键结果 / 消融** · 显著假设数为对照的 2–4 倍；预注册 11/16 方向显著
- **适用条件 / 局限** · 观察证据不能自动证成因果

**可复用机制** · 把探索与独立验证分开并保留失败记录

<a id="paper-149707"></a>

## ExpertNavigator: Functionally Coherent Expert Grouping and Pairwise-Ranked Routing for High-Fidelity Dense-to-MoE Conversion

[官方论文页](https://neurips.cc/virtual/2026/poster/149707) · [作者来源](https://openreview.net/forum?id=o3Q8xJvP0x)

- **问题 / 瓶颈** · 密集到 MoE 转换在预算约束下损失质量
- **核心创新 / 方法** · 联合功能聚类、成对排序和逐层稀疏预算
- **Baseline** · 其他 Dense-to-MoE 方法与密集模型
- **Benchmark** · 多基准的稀疏转换，名称待核
- **关键结果 / 消融** · 激活 60% FFN 参数时最高保留 97.8% 平均得分
- **适用条件 / 局限** · 实际加速依赖运行时和硬件

**可复用机制** · 固定全局激活预算比较分组及路由

<a id="paper-151817"></a>

## Explaining and Breaking the Safety-Helpfulness Ceiling via Preference Dimensional Expansion

[官方论文页](https://neurips.cc/virtual/2026/poster/151817) · [作者来源](https://openreview.net/forum?id=Xl0oQPYgSd)

- **问题 / 瓶颈** · 仅调权重可能受提示对可实现目标的限制
- **核心创新 / 方法** · 识别单奖励提示并改写为支持多维意图的提示
- **Baseline** · 顺序及同时对齐设置
- **Benchmark** · 有用、无害与真实三维奖励
- **关键结果 / 消融** · 作者报告顺序设置改善 5%–12.4%，同时设置总体奖励提高 4.6%
- **适用条件 / 局限** · 奖励改善需用独立评估确认

**可复用机制** · 先检查提示是否允许多个目标同时满足

<a id="paper-155701"></a>

## Explaining and Preventing Alignment Collapse in Iterative RLHF

[官方论文页](https://neurips.cc/virtual/2026/poster/155701) · [作者来源](https://openreview.net/forum?id=3azE5mTgC1)

- **问题 / 瓶颈** · 奖励模型从策略生成数据重新训练会造成反馈失真
- **核心创新 / 方法** · 把奖励模型演化纳入优化并用一阶近似正则
- **Baseline** · 标准迭代 RLHF
- **Benchmark** · 受控环境及 Llama-3.2-1B
- **关键结果 / 消融** · 作者报告缓解对齐崩溃，量化待核
- **适用条件 / 局限** · 依赖后续更新的近似

**可复用机制** · 同时监测当前奖励与下一轮真实偏好表现

<a id="paper-150190"></a>

## Explaining Cross-Modal Model Behavior with Gradient-Estimation-Based Feature Interaction

[官方论文页](https://neurips.cc/virtual/2026/poster/150190) · [作者来源](https://openreview.net/forum?id=k3fR86JLGj)

- **问题 / 瓶颈** · 一阶归因看不到跨模态协同
- **核心创新 / 方法** · 用代理梯度估计高阶 Shapley 交互，借助双编码器简化估计
- **Baseline** · 以固定图块为单位的跨模态解释
- **Benchmark** · CLIP 类模型的图文交互
- **关键结果 / 消融** · 作者报告可得到细粒度像素交互且保持效率
- **适用条件 / 局限** · 双编码器简化未必适用深度融合模型

**可复用机制** · 对齐任务中并列报告单特征和跨模态交互贡献

<a id="paper-156138"></a>

## Explanation Mechanism Influences Human Reliance on Reinforcement Learning Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/156138) · [作者来源](https://openreview.net/forum?id=099yUmkgyW)

- **问题 / 瓶颈** · 解释提高采纳率也可能放大过度依赖
- **核心创新 / 方法** · 在控制代理和任务时独立操纵建议最优性与解释真实性
- **Baseline** · Shapley、显著性和无解释等对照
- **Benchmark** · 100 人和 70 人的受控研究
- **关键结果 / 消融** · 奖励分解解释使恰当建议检测提高 89%，仍有过度依赖
- **适用条件 / 局限** · 研究结果可能依赖具体任务

**可复用机制** · 解释验收应分开测恰当采纳与错误采纳

<a id="paper-139691"></a>

## Explanation Multiplicity in SHAP: Characterization and Assessment

[官方论文页](https://neurips.cc/virtual/2026/poster/139691) · [作者来源](https://openreview.net/forum?id=ANaxIH1evO)

- **问题 / 瓶颈** · 同一预测的 SHAP 排名可能不稳定
- **核心创新 / 方法** · 双种子分离模型和解释器波动，再用随机空模型校准
- **Baseline** · 欧氏距离、排名指标、CTE 与确定性方法
- **Benchmark** · 多个数据集、模型及采样策略
- **关键结果 / 消融** · 小数据由模型波动主导，数据大时解释器波动主导
- **适用条件 / 局限** · 稳定替代方案可能改变估计目标

**可复用机制** · 报告排名和头部集合的分布而不只展示一次归因

<a id="paper-153929"></a>

## ExpLang: Improved Exploration and Exploitation in LLM Reasoning with On-Policy Thinking Language Selection

[官方论文页](https://neurips.cc/virtual/2026/poster/153929) · [作者来源](https://openreview.net/forum?id=HaJdg0gMxD)

- **问题 / 瓶颈** · 只用英语限制推理探索。
- **核心创新 / 方法** · 将推理语言选择纳入在线策略优化的动作空间。
- **Baseline** · 英语单语训练。
- **Benchmark** · 已见与未见语言的推理和语言遵循。
- **关键结果 / 消融** · 作者报告等预算下优于英语训练，语言遵循较高。
- **适用条件 / 局限** · 语种分布与任务明细待核。

**可复用机制** · 把语言当作可学习决策，同时报告答案和语言遵循。

<a id="paper-153676"></a>

## Exploiting Negative Multi-Cluster Structure in Class-Wise Embeddings for Weakly Supervised Multi-Label Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/153676) · [作者来源](https://openreview.net/forum?id=Jc0lO9zGdF)

- **问题 / 瓶颈** · 类级嵌入容易抹平负例内部结构。
- **核心创新 / 方法** · 跨嵌入汇总簇一致性挖正伪标签，以邻域排除找负标签，再做对比学习。
- **Baseline** · 弱监督多标签方法。
- **Benchmark** · 图像、文本及音频单标签监督。
- **关键结果 / 消融** · 作者报告平均改善 4.46%。
- **适用条件 / 局限** · 簇稳定性和指标口径待核。

**可复用机制** · 对照统一负类与保留语义子簇的弱监督。

<a id="paper-153038"></a>

## Exploration as Constrained Policy-Space Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/153038) · [作者来源](https://openreview.net/forum?id=OUryWodGWl)

- **问题 / 瓶颈** · 探索奖励后期可能与任务优势反向。
- **核心创新 / 方法** · 将探索约束写为最优传输，在经验批次上以 Sinkhorn 重加权。
- **Baseline** · 标准在线与离策略强化学习。
- **Benchmark** · 复杂连续控制任务。
- **关键结果 / 消融** · 作者报告避免所测任务性能退化。
- **适用条件 / 局限** · 度量、计算和批次敏感度待核。

**可复用机制** · 跟踪内在奖励和任务优势关联，比较固定奖励权重与动态权重。

<a id="paper-152906"></a>

## Exploration via Exploitation: The Blessing of Reward Diversity in Personalized Federated RL

[官方论文页](https://neurips.cc/virtual/2026/poster/152906) · [作者来源](https://openreview.net/forum?id=PWig4U4G3e)

- **问题 / 瓶颈** · 个性化目标被视为共享学习的障碍。
- **核心创新 / 方法** · 共享动力学与个性目标分开；利用跨代理奖励差异提供覆盖。
- **Baseline** · PF-UCBVI 与不加探索奖金的 PF-EFVI。
- **Benchmark** · 个性化联邦价值迭代理论，指标为遗憾。
- **关键结果 / 消融** · 作者证明充分奖励多样性下贪心方案可获对数遗憾。
- **适用条件 / 局限** · 依赖覆盖和共享动力学设定。

**可复用机制** · 量化合作方覆盖互补性后再决定探索预算。

<a id="paper-154772"></a>

## Exploring Lifelong Adaptation: In-Context Reinforcement Learning in Non-Stationary Environments

[官方论文页](https://neurips.cc/virtual/2026/poster/154772) · [作者来源](https://openreview.net/forum?id=B4sdRfOm1V)

- **问题 / 瓶颈** · 固定动力学掩盖终身适应失效。
- **核心创新 / 方法** · 交叉比较平稳与非平稳训练、序列骨干和交互规模。
- **Baseline** · 域随机化、平稳、非平稳及分阶段训练。
- **Benchmark** · 离散符号任务与连续控制。
- **关键结果 / 消融** · 作者报告三个因素共同影响适应，分项幅度待核。
- **适用条件 / 局限** · 外推依赖漂移类型。

**可复用机制** · 固定交互数分别评测突然切换和缓慢漂移。

<a id="paper-151074"></a>

## Exploring MLLM-Diffusion Information Transfer with MetaCanvas

[官方论文页](https://neurips.cc/virtual/2026/poster/151074) · [作者来源](https://openreview.net/forum?id=d8GC1xLs92)

- **问题 / 瓶颈** · 全局条件难传递布局和属性绑定。
- **核心创新 / 方法** · 把多模态表示组织为空间索引画布并逐块残差融合。
- **Baseline** · 匹配设置的全局条件及专用闭源系统。
- **Benchmark** · 三个扩散底座、六项生成和编辑任务。
- **关键结果 / 消融** · 作者报告一致改善，具体幅度待核。
- **适用条件 / 局限** · 依赖空间索引质量。

**可复用机制** · 在同一生成器比较逐块与全局条件的布局遵循。

<a id="paper-148417"></a>

## Exploring Starts Are Not Enough: Counterexamples and a Fix for Monte Carlo Exploring Starts

[官方论文页](https://neurips.cc/virtual/2026/poster/148417) · [作者来源](https://openreview.net/forum?id=xyHNYFTjvc)

- **问题 / 瓶颈** · 探索起点仍可能收敛到次优固定点。
- **核心创新 / 方法** · 构造两类更新反例，并在初始访问设置按状态反向缩放更新频率。
- **Baseline** · 样本均值初始访问和首次访问 MCES。
- **Benchmark** · 表格理论，以最优收敛为判据。
- **关键结果 / 消融** · 两版本均有反例；初始访问修正具收敛保证。
- **适用条件 / 局限** · 函数逼近不自动继承表格证明。

**可复用机制** · 同时监控更新频率与步长，而非仅检查探索覆盖。

<a id="paper-156760"></a>

## Exploring the Limitations of Layer Synchronization in Spiking Neural Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/156760) · [作者来源](https://neurips.cc/virtual/2026/poster/156760)

- **问题 / 瓶颈** · 同步训练模型直接异步执行会失配。
- **核心创新 / 方法** · 在反传中纳入异步调度，比较两种执行策略。
- **Baseline** · 同步训练和同步执行方案。
- **Benchmark** · 含时空信息的数据集，测脉冲数、延迟、精度。
- **关键结果 / 消融** · 作者报告最高少 50% 脉冲、推理快 2 倍、精度高 10%。
- **适用条件 / 局限** · 结果依赖调度、硬件和任务。

**可复用机制** · 对照训练与运行调度匹配和不匹配的效率与质量。

<a id="paper-139255"></a>

## Exploring the Limits of Compositional Generalization in Vision-Language-Action Manipulation

[官方论文页](https://neurips.cc/virtual/2026/poster/139255) · [作者来源](https://openreview.net/forum?id=bqpIkP9Yfq)

- **问题 / 瓶颈** · 孤立技能成功并不保证顺序执行。
- **核心创新 / 方法** · RoboCombine 用模块式执行拆开规划、触发和策略，扩展原子技能起始位姿。
- **Baseline** · 完整指令训练和未扩展起始状态的层级执行。
- **Benchmark** · RoboCombine，测顺序成功和转移成功。
- **关键结果 / 消融** · 在预知切换时机的层级执行下两指标分别从 2.11% 到 26.32%、2.63% 到 60.53%。
- **适用条件 / 局限** · 预知时机结果不能直接外推到自主切换。

**可复用机制** · 分离切换选择和下游策略在交接状态上的可执行性。

<a id="paper-149745"></a>

## Express Language Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/149745) · [作者来源](https://openreview.net/forum?id=nf2SQeKcr9)

- **问题 / 瓶颈** · 双向注意力的近似保证不能直接用于因果解码
- **核心创新 / 方法** · Express 将非因果注意力近似转为带保证的因果近似，并结合 Thinformer
- **Baseline** · Thinformer 与 FlashAttention 2
- **Benchmark** · 长上下文预填充、KV 压缩和长文本解码
- **关键结果 / 消融** · 长度 n 时误差为 log(n) 的 1.5 次方除以 s，内存 O(s)，报告实现加速
- **适用条件 / 局限** · 常数和硬件适用范围待核

**可复用机制** · 复用现有注意力近似时，分别验证因果保证和实际 I/O。

<a id="paper-154489"></a>

## ExpRFT: Exponential Reward-Weighted Fine-Tuning for Offline RL in Multi-Turn Dialogue

[官方论文页](https://neurips.cc/virtual/2026/poster/154489) · [作者来源](https://openreview.net/forum?id=DE0tMV3YZo)

- **问题 / 瓶颈** · 中心化仿射奖励加权可使损失无下界
- **核心创新 / 方法** · 对标准化优势做温度可调的指数加权
- **Baseline** · 仿射奖励加权 SFT 与 AWR 的设计比较
- **Benchmark** · 六项多轮对话基准
- **关键结果 / 消融** · 得到有良好定义的损失及噪声控制参数，量化待核
- **适用条件 / 局限** · 温度和优势标准化依赖奖励分布

**可复用机制** · 对离线轨迹加权方法同时扫描奖励噪声与温度。

<a id="paper-156110"></a>

## Extending 3D Reconstruction Models to Any Camera

[官方论文页](https://neurips.cc/virtual/2026/poster/156110) · [作者来源](https://openreview.net/forum?id=0K6xev69k8)

- **问题 / 瓶颈** · 透视预训练模型在鱼眼与全景图像上失效
- **核心创新 / 方法** · 以低秩适配接入非针孔相机
- **Baseline** · 原透视预训练模型
- **Benchmark** · 鱼眼、全景和原始透视重建
- **关键结果 / 消融** · 增加约 0.1% 参数，报告保留原透视表现
- **适用条件 / 局限** · 证据限所测模型与相机族

**可复用机制** · 适配传感器时，把旧传感器表现纳入回归测试。

<a id="paper-150218"></a>

## Extending ROC Analysis to Uncertainty-Aware Risk Prediction with an Interval-Based AUC (iAUC)

[官方论文页](https://neurips.cc/virtual/2026/poster/150218) · [作者来源](https://openreview.net/forum?id=jsG2UV3YqP)

- **问题 / 瓶颈** · 普通 AUC 无法反映区间重叠
- **核心创新 / 方法** · 以两条 ROC 式曲线分解正负样本排序
- **Baseline** · 点预测 ROC 与 AUC
- **Benchmark** · 区间风险预测的排序与类条件覆盖
- **关键结果 / 消融** · 在有效覆盖下给出最优 AUC 的界
- **适用条件 / 局限** · 理论依赖类条件覆盖

**可复用机制** · 联合报告区间覆盖和排序可信度。

<a id="paper-150273"></a>

## Externalized CPDAG Summaries Improve LLM Causal Deduction

[官方论文页](https://neurips.cc/virtual/2026/poster/150273) · [作者来源](https://openreview.net/forum?id=jNkJv4Cfma)

- **问题 / 瓶颈** · 自由推理容易用局部模式替代等价类判断
- **核心创新 / 方法** · 先生成带类型的 CPDAG 摘要，再依据结构回答
- **Baseline** · PC 指令基线及无结构双轮文本
- **Benchmark** · Corr2Cause、改写分布外测试
- **关键结果 / 消融** · Qwen3.5-27B 主实验 Yes F1 从 73.0 到 86.4
- **适用条件 / 局限** · 结构生成错误仍会传给第二轮

**可复用机制** · 比较结构中介和等轮次自由文本，并扰动结构验证依赖。

<a id="paper-155982"></a>

## Extracting Governing Equations from Latent Dynamics via Multi-View Contrastive Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/155982) · [作者来源](https://openreview.net/forum?id=1NoGYV3xUP)

- **问题 / 瓶颈** · 噪声和非线性观测使潜状态难辨识
- **核心创新 / 方法** · 时间对比学习联合恢复轨迹和动力学，以结构化基函数拟合方程
- **Baseline** · 既有潜动态辨识理论，实验对照待核
- **Benchmark** · 混沌、振荡和亚稳态及高斯和泊松噪声
- **关键结果 / 消融** · 理论辨识至仿射不定性，报告轨迹和流场恢复
- **适用条件 / 局限** · 需要共享过程的独立噪声视图

**可复用机制** · 结合多视图对齐与显式动力学基，并检查坐标不确定性。

<a id="paper-154324"></a>

## Extracting Search Trees from LLM Reasoning Traces Reveals Myopic Planning

[官方论文页](https://neurips.cc/virtual/2026/poster/154324) · [作者来源](https://openreview.net/forum?id=EWoL9QIbhS)

- **问题 / 瓶颈** · 长推理痕迹不直接证明深规划
- **核心创新 / 方法** · 从四连棋推理抽取搜索树、拟合认知模型并剪除部分文字做干预
- **Baseline** · 人类搜索与不同深度决策模型
- **Benchmark** · 四连棋，测树宽深和行动选择
- **关键结果 / 消融** · 宽度较能预测表现，动作更符合忽略深节点的模型
- **适用条件 / 局限** · 仅验证所测棋类与模型

**可复用机制** · 比较深层文字的存在和对选择的实际作用。

<a id="paper-150343"></a>

## Extraneous Cognitive Load in Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150343) · [作者来源](https://openreview.net/forum?id=iqBkP1UEL0)

- **问题 / 瓶颈** · 题目难度和表述开销通常混杂
- **核心创新 / 方法** · 控制五种呈现因素，以激活分数估计额外负荷
- **Baseline** · 同题不同呈现条件
- **Benchmark** · CogLoadBench 三类推理任务
- **关键结果 / 消融** · 额外负荷常降低准确率，报告激活分数可跨任务泛化
- **适用条件 / 局限** · 受所测模型与模板影响

**可复用机制** · 固定语义难度构造呈现对照，检查准确率下降来自何处。

<a id="paper-151744"></a>

## Extrapolative Weight Averaging Reveals Correctness–Efficiency Frontiers in Code RL

[官方论文页](https://neurips.cc/virtual/2026/poster/151744) · [作者来源](https://openreview.net/forum?id=YRDiKZgtA9)

- **问题 / 瓶颈** · 测试覆盖变化对代码性能有相反影响
- **核心创新 / 方法** · 在不同嵌套单测覆盖上训练共享初始化检查点，再沿权重方向插值或外推
- **Baseline** · 训练端点及插值
- **Benchmark** · 竞赛编程隐藏测试、时限及内存限制
- **关键结果 / 消融** · 报告外推扩展已训练端点间的前沿，高覆盖减少优化失败但增加正确性失败
- **适用条件 / 局限** · 依赖共享初始化及具体单测分布

**可复用机制** · 对不同奖励训练的模型分别统计失败类型，再检验权重外推。

<a id="paper-149109"></a>

## ExtraVAR: Stage-Aware RoPE Remapping for Resolution Extrapolation in Visual Autoregressive Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149109) · [作者来源](https://openreview.net/forum?id=spQoCaKIYY)

- **问题 / 瓶颈** · 视觉自回归跨分辨率时出现全局或局部重复与细节退化
- **核心创新 / 方法** · 将不同尺度阶段与主导频带匹配，分别调整映射
- **Baseline** · 直接迁移语言或扩散模型外推方式
- **Benchmark** · 视觉自回归高分辨率生成
- **关键结果 / 消融** · 作者报告抑制三类故障，量化待核
- **适用条件 / 局限** · 依赖粗到细尺度组织

**可复用机制** · 为每个阶段检查位置编码的敏感频带，分别测重复与细节误差。

<a id="paper-153894"></a>

## Extremely Sparse-View Computed Tomography from 2D Projections via Pose-Aware Diffusion Priors

[官方论文页](https://neurips.cc/virtual/2026/poster/153894) · [作者来源](https://openreview.net/forum?id=HvYYOiRYrE)

- **问题 / 瓶颈** · 训练与推理均稀疏时缺少高质量三维真值
- **核心创新 / 方法** · 从单幅二维投影学习位姿感知先验，采样时约束观测一致性和投影物理
- **Baseline** · 稀疏优化与学习式重建
- **Benchmark** · 两套公开 CT 数据的一、四、八视图设置
- **关键结果 / 消融** · 新视角质量最佳，重建相当或更好
- **适用条件 / 局限** · 不直接支持临床部署，依赖成像几何

**可复用机制** · 缺少三维训练标签时，在多个投影视图间施加共享潜体一致性。

<a id="paper-148617"></a>

## Factor Augmented High-Dimensional SGD

[官方论文页](https://neurips.cc/virtual/2026/poster/148617) · [作者来源](https://openreview.net/forum?id=wPsFSiDXLS)

- **问题 / 瓶颈** · 传统离线降维需保存全量数据
- **核心创新 / 方法** · 在线估计因子后迭代更新，分析递减步长与小批量下的矩收敛
- **Baseline** · 标准 SGD 与离线两阶段降维
- **Benchmark** · 高维流式理论设定，考察范数内的矩收敛
- **关键结果 / 消融** · 作者给出计入因子误差的收敛分析；经验幅度待核
- **适用条件 / 局限** · 需潜因子结构，具体假设待查正文

**可复用机制** · 在线降维和优化并行时，在收敛分析中为表征误差单独记账。

<a id="paper-149013"></a>

## Factorized Gradients for Scalable Highly-expressive Parametric Diffeomorphisms

[官方论文页](https://neurips.cc/virtual/2026/poster/149013) · [作者来源](https://openreview.net/forum?id=tTrgBMBN77)

- **问题 / 瓶颈** · 分片仿射速度下直接求参数梯度代价随点数和参数维数相乘增长
- **核心创新 / 方法** · 先积分轨迹，再投影至参数空间求因子化梯度
- **Baseline** · 传统 CPAB 梯度计算
- **Benchmark** · 分片仿射微分同胚，比较时间复杂度；实测细节待核
- **关键结果 / 消融** · 作者给出从 O(dTN) 到 O(TN+dC) 的复杂度
- **适用条件 / 局限** · 依赖分片网格结构；常数开销和适用规模待核

**可复用机制** · 求解同一轨迹的大量参数导数时，检查能否共享积分再批量投影。

<a id="paper-155234"></a>

## FactorizedHMR: A Hybrid Framework for Video Human Mesh Recovery

[官方论文页](https://neurips.cc/virtual/2026/poster/155234) · [作者来源](https://openreview.net/forum?id=7ERjBgSwbw)

- **问题 / 瓶颈** · 遮挡下肢体姿态多解，确定性平均会失真
- **核心创新 / 方法** · 先回归躯干与根，再用流匹配补全其余关节，加入几何监督
- **Baseline** · 强人体网格恢复基线；具名方法待核
- **Benchmark** · 相机和世界坐标下的视频人体网格基准
- **关键结果 / 消融** · 作者报告关节恢复和漂移改善，模糊场景更明显
- **适用条件 / 局限** · 稳定锚点若误估会向补全传播

**可复用机制** · 对不均匀不确定度的结构化目标，分开确定性锚定和概率补全。

<a id="paper-149364"></a>

## Factorized Spectral Representations for Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149364) · [作者来源](https://openreview.net/forum?id=qZTX18AAiX)

- **问题 / 瓶颈** · 将状态动作合并会限制复用，并扩大表征假设类
- **核心创新 / 方法** · 以噪声对比目标拟合 CP 分解，训练三个编码器
- **Baseline** · 矩阵式转移谱表示
- **Benchmark** · 连续控制及执行器变化迁移
- **关键结果 / 消融** · 作者给出样本复杂度改善并报告高维运动收益；迁移仅重训动作编码器
- **适用条件 / 局限** · 动态需近似可分解，否则低秩偏差可能增大

**可复用机制** · 执行器独立改变的任务可优先测试分离状态与动作的动力学编码。

<a id="paper-153530"></a>

## Facts Don't Speak Louder than Words: The Behavioral Essence of Long-CoT Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/153530) · [作者来源](https://openreview.net/forum?id=KeTJLE21Jz)

- **问题 / 瓶颈** · 拒绝采样默认正确轨迹和广覆盖不可或缺
- **核心创新 / 方法** · 比较错误轨迹、受限提示和仅已掌握问题的蒸馏
- **Baseline** · 标准长思维链蒸馏及不同损失
- **Benchmark** · 语言模型推理任务；具名基准待核
- **关键结果 / 消融** · 作者观察到错误轨迹或窄提示仍可带来接近收益，交叉熵支持复杂模式
- **适用条件 / 局限** · 不应外推为任意错误数据可用；分布条件待核

**可复用机制** · 用已掌握题目隔离行为迁移，再和新增知识数据做等预算比较。

<a id="paper-149903"></a>

## FADE: Fractional Anomalous Dynamics Extrapolation for Training-Free Diffusion Transformers Acceleration

[官方论文页](https://neurips.cc/virtual/2026/poster/149903) · [作者来源](https://openreview.net/forum?id=mM9yiKjZ8m)

- **问题 / 瓶颈** · 静态整数阶外推在弯曲非平稳轨迹上易积累误差
- **核心创新 / 方法** · 用 Mittag–Leffler 分数阶算子建模，并从跨样本统计构造查找表
- **Baseline** · 整数阶或复用型特征缓存
- **Benchmark** · 扩散 Transformer 推理延迟与生成质量；具名配置待核
- **关键结果 / 消融** · 作者提出免训练加速，量化幅度待核
- **适用条件 / 局限** · 依赖估计动态跨样本稳定；模型变化时需重新校准

**可复用机制** · 缓存策略应按步骤检验曲率及误差，比较同预算下的生成质量。

<a id="paper-149405"></a>

## Fail-Closed Alignment for Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149405) · [作者来源](https://openreview.net/forum?id=qJN2JFwGdt)

- **问题 / 瓶颈** · 单一路径失灵即可使拒绝不稳
- **核心创新 / 方法** · 渐进训练冗余安全表示，用防御验收确认路径独立性
- **Baseline** · 现有对齐；具名对照待核
- **Benchmark** · 六种安全压力评估与拒绝质量
- **关键结果 / 消融** · 作者报告平均不安全响应成功率 1.7%，质量大体保持
- **适用条件 / 局限** · 结果限所测模型及安全测试集

**可复用机制** · 用独立防御路径做容错验收，同时统计过度拒绝。

<a id="paper-155737"></a>

## Failing Forward: Adaptive Failure-Informed Learning for Vision-Language-Action Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155737) · [作者来源](https://openreview.net/forum?id=3Kqyrxf0U4)

- **问题 / 瓶颈** · 只克隆成功示范缺少纠错信号
- **核心创新 / 方法** · 共享视觉语言骨干，分开成功与失败动作生成器，按逐步分布距离调节引导
- **Baseline** · 仅成功行为克隆及既有 VLA
- **Benchmark** · 域内域外短程与长程操作；细项待核
- **关键结果 / 消融** · 作者报告失败感知训练收益，具体幅度待核
- **适用条件 / 局限** · 依赖失败样本代表部署偏移，负向引导过强或排斥有效动作

**可复用机制** · 训练动作生成时记录失败分布，核查自适应负引导是否比固定权重更稳。

<a id="paper-152161"></a>

## Failing to Falsify: Evaluating and Mitigating Confirmation Bias in Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152161) · [作者来源](https://openreview.net/forum?id=V3hfvlipsD)

- **问题 / 瓶颈** · 只证实不证伪导致探索效率低
- **核心创新 / 方法** · 让模型在三元组交互中提案、收反馈并猜规则，比较反例提示与行为蒸馏
- **Baseline** · 默认提示及鼓励反例的提示
- **Benchmark** · 11 个模型的隐藏规则与迁移 Blicket 任务
- **关键结果 / 消融** · 平均发现率从 42% 升到 56%，蒸馏展现迁移
- **适用条件 / 局限** · 任务简化了现实的证据结构

**可复用机制** · 将验证流程中的确认和反证查询分开统计，并检验迁移到新反馈机制。

<a id="paper-153631"></a>

## Failure-Band Authorization for Filtered Retrieval

[官方论文页](https://neurips.cc/virtual/2026/poster/153631) · [作者来源](https://openreview.net/forum?id=JxfZ6eyRMh)

- **问题 / 瓶颈** · 平均速度不能反映过滤向量搜索的尾延时
- **核心创新 / 方法** · 固定计划集，校准尾部区间并将召回下限纳入选择
- **Baseline** · 最强固定或动态对照；具名方法待核
- **Benchmark** · Medium+EntDoc，在 5–15% 失败区间比较尾延时及 Recall@20
- **关键结果 / 消融** · 作者报告匹配召回时 P95 和 P99 分别降 46% 和 45%
- **适用条件 / 局限** · 依赖数据、硬件和校准覆盖

**可复用机制** · 固定召回预算，在计划排序最不稳的区域单独测高分位延时。

<a id="paper-149263"></a>

## Failure Profiling and Reachable Trajectory Selection for Reasoning Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/149263) · [作者来源](https://openreview.net/forum?id=rbv0ZUxfLY)

- **问题 / 瓶颈** · 正解仍可能落在学生无法复现的轨迹分布
- **核心创新 / 方法** · 重复采样统计错误率和一致性，按失败类型生成并选择候选
- **Baseline** · 常规正确解蒸馏及错误增强方法
- **Benchmark** · 数学推理蒸馏，具名任务及指标待核
- **关键结果 / 消融** · 摘要提出按失败类型和可达性选择，量化收益待核
- **适用条件 / 局限** · 重复采样增加开销；学生变化后需重新估计

**可复用机制** · 蒸馏前分开估计错误率与错误一致性，避免给不同失败模式同样监督。

<a id="paper-155445"></a>

## Fair Bubble Sort: Provably Optimal Fair Ranking with Continuous Sensitive Attributes

[官方论文页](https://neurips.cc/virtual/2026/poster/155445) · [作者来源](https://openreview.net/forum?id=5YYHyRjX7r)

- **问题 / 瓶颈** · 离散分组丢失连续顺序及细粒度差异
- **核心创新 / 方法** · 用 Kendall 相关定义公平，以 Kemeny 距离度量失真，通过相邻交换优化
- **Baseline** · 离散分组式排名规则
- **Benchmark** · 合成与真实排序数据，比较公平与效用得失
- **关键结果 / 消融** · 作者证明无权 Kemeny 设定下最优并报告更优折衷
- **适用条件 / 局限** · 加权或其他公平定义不在该保证内

**可复用机制** · 敏感属性为连续变量时，以连续约束和离散分桶做公平效用对照。

<a id="paper-148409"></a>

## FairMT: Fairness for Heterogeneous Multi-Task Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/148409) · [作者来源](https://openreview.net/forum?id=y4pCWEetw2)

- **问题 / 瓶颈** · 多头敏感度和输出尺度不同
- **核心创新 / 方法** · 以分离梯度的有效最优组为参照，归一差距并以头部几何引导原始对偶优化
- **Baseline** · 效用导向多任务优化器
- **Benchmark** · 视觉与语言多任务公平评测
- **关键结果 / 消融** · 作者报告群体差距缩小且效用接近效用导向对照
- **适用条件 / 局限** · 依赖有效群体统计；量化幅度待核

**可复用机制** · 同预算比较直接聚合差距和经过各头灵敏度校正的聚合

<a id="paper-149831"></a>

## Fairness Failure Modes of Multimodal LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/149831) · [作者来源](https://openreview.net/forum?id=myI2BmrxeL)

- **问题 / 瓶颈** · 单一偏差分数掩盖两种方向相反的失误
- **核心创新 / 方法** · 控制图像可见证据和上下文歧义，分别报告公平与偏差分数
- **Baseline** · 闭源和开源模型、骨干语言模型、提示缓解方案
- **Benchmark** · MultiBBQ 视觉及图文设置
- **关键结果 / 消融** · 作者报告部分闭源模型过度拒答，部分开源模型在歧义下不善弃答
- **适用条件 / 局限** · 合成图和有限刻板情境限制外推

**可复用机制** · 用歧义与已消歧的成对样本分开统计拒答行为

<a id="paper-150604"></a>

## Faithful Embeddings of Irregular and Asynchronous Data for Online Log-NCDEs

[官方论文页](https://neurips.cc/virtual/2026/poster/150604) · [作者来源](https://openreview.net/forum?id=gtk5eOWBxM)

- **问题 / 瓶颈** · 人为重建路径可能改变连续模型的输入结构
- **核心创新 / 方法** · 用连续单射编码记录事件增量，组合任意区间的对数签名
- **Baseline** · 插值或插补驱动的连续时间模型
- **Benchmark** · 合成受控动力学及真实不规则序列
- **关键结果 / 消融** · 作者证明紧集上的通用性转移并报告精度和效率改善
- **适用条件 / 局限** · 依赖紧性等理论条件；具体基准及误差幅度待核

**可复用机制** · 固定模型比较事件编码与重建路径，在不同输出网格下测稳定性

<a id="paper-139844"></a>

## Faithfulness Metrics Don't Measure Faithfulness: A Meta-Evaluation with Ground Truth

[官方论文页](https://neurips.cc/virtual/2026/poster/139844) · [作者来源](https://openreview.net/forum?id=12Pl2wLcY7)

- **问题 / 瓶颈** · 合理性代理并不能测解释是否反映实际计算
- **核心创新 / 方法** · 构造可从输出推断中间计算的任务，在步骤和整链层面自动标记
- **Baseline** · 主流忠实度指标和随机基准
- **Benchmark** · BonaFide 含 13 任务、10 模型、3066 条链，测 AUROC
- **关键结果 / 消融** · 多数接近随机，整链最好 0.71，步骤最好 0.59 且难跨设置
- **适用条件 / 局限** · 可标真值任务与真实开放任务存在差距

**可复用机制** · 先以有已知机制的任务验收解释指标，再迁移到开放环境

<a id="paper-149124"></a>

## FaithSieve: Fine-Grained Evaluation of Math Proofs with Faithful Formal Evidence

[官方论文页](https://neurips.cc/virtual/2026/poster/149124) · [作者来源](https://openreview.net/forum?id=si7lviFpgb)

- **问题 / 瓶颈** · Lean 可能验证翻译漂移或跳过局部漏洞
- **核心创新 / 方法** · 细分证明、提取局部义务、检查上下文及对象是否忠实后采用形式证据
- **Baseline** · 直接自然语言判分
- **Benchmark** · ProofLoc-Olympiad 350 题及 University 200 题，首错精确匹配
- **关键结果 / 消融** · 两者分别达到 81.43% 和 84.5%，对照 72.29% 和 75.0%
- **适用条件 / 局限** · 依赖形式化质量和专业题域

**可复用机制** · 分开测自动形式化对齐与形式验证正确性

<a id="paper-138979"></a>

## FakeParts: a New Family of AI-Generated Video Forgeries

[官方论文页](https://neurips.cc/virtual/2026/poster/138979) · [作者来源](https://openreview.net/forum?id=suBjj8xrz2)

- **问题 / 瓶颈** · 只测完整生成容易高估检测覆盖
- **核心创新 / 方法** · 以局部篡改检测和定位为防御评测对象
- **Baseline** · 完整视频伪造基准、人类与超过 15 种检测模型
- **Benchmark** · FakePartsBench 的视频检测与像素及帧级标注
- **关键结果 / 消融** · 作者报告局部情形下人的检测准确率最多下降 26%，检测模型也退化
- **适用条件 / 局限** · 结果依赖数据分布及验证协议

**可复用机制** · 防御评测分层报告局部、全局条件下的识别率与定位

<a id="paper-150365"></a>

## FalconPerception-HD: High Density Perception via Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/150365) · [作者来源](https://openreview.net/forum?id=icSHR3O8rl)

- **问题 / 瓶颈** · 逐 token 交叉熵不对应集合精确率召回率
- **核心创新 / 方法** · 在 Falcon Perception 上用 GRPO 对集合输出优化并控制多头采样
- **Baseline** · 以最大似然训练的基础模型
- **Benchmark** · PBench、SACO-Gold 与高密度场景，包含 MCC
- **关键结果 / 消融** · 作者报告可到单场景 500 物体，并减少掩码重复及去重需求
- **适用条件 / 局限** · 奖励权衡依赖实例密度及匹配规则

**可复用机制** · 训练集合解码器时比较集合奖励和逐 token 损失，并看重复率

<a id="paper-150872"></a>

## Falcon-X: A Time Series Foundation Model for Heterogeneous Multivariate Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/150872) · [作者来源](https://openreview.net/forum?id=ekOExPyuZS)

- **问题 / 瓶颈** · 原变量尺度和物理意义不同，非负注意力限制交互
- **核心创新 / 方法** · 估计正负语义亲和，在潜实体空间做注意力，再路由重建各变量
- **Baseline** · 现有时间序列基础模型
- **Benchmark** · GIFT-Eval 和 fev-bench 的预测比较
- **关键结果 / 消融** · 作者报告领先，分项幅度待核
- **适用条件 / 局限** · 原型覆盖和负亲和解释性须验证

**可复用机制** · 按传感器组合留出任务比较共享原型与直接变量混合

<a id="paper-151229"></a>

## Fast 4D Mesh Generation by Spatio-Temporal Attention Chains

[官方论文页](https://neurips.cc/virtual/2026/poster/151229) · [作者来源](https://openreview.net/forum?id=bwPja6GtAE)

- **问题 / 瓶颈** · 长视频逐帧匹配慢且几何细节漂移
- **核心创新 / 方法** · 锚顶点映射到潜 token，沿时序注意力传播对应再回投顶点
- **Baseline** · 既有四维网格生成方法
- **Benchmark** · 动态网格几何、时序一致性、两类追踪和相机估计
- **关键结果 / 消融** · 作者报告 9 秒生成、13 倍提速，且可处理长至 16 倍的视频
- **适用条件 / 局限** · 早期潜对应须可靠，遮挡边界待测

**可复用机制** · 在生成模型中比较不同迭代层的对应质量，验证是否可替代外部匹配

<a id="paper-149973"></a>

## Fast Alignment of Embeddings: Computational Guarantees for Anisotropic Procrustes-Wasserstein

[官方论文页](https://neurips.cc/virtual/2026/poster/149973) · [作者来源](https://openreview.net/forum?id=loV2n73ZW3)

- **问题 / 瓶颈** · 未知旋转与排列相互耦合
- **核心创新 / 方法** · 先估计两边主特征空间再找匹配
- **Baseline** · 各向同性对齐理论
- **Benchmark** · 幂律协方差的带噪植入高斯模型
- **关键结果 / 消融** · 显式条件下多项式时间高概率精确恢复
- **适用条件 / 局限** · 依赖谱结构和噪声条件

**可复用机制** · 在尝试全局匹配前测共享谱结构

<a id="paper-151812"></a>

## Fast and Accurate Probing of In-Training LLMs' Downstream Performances

[官方论文页](https://neurips.cc/virtual/2026/poster/151812) · [作者来源](https://openreview.net/forum?id=XpnthdLoOn)

- **问题 / 瓶颈** · 生成评测慢且困惑度可偏离任务效果
- **核心创新 / 方法** · 从内部表征拟合下游 pass@1
- **Baseline** · 困惑度与生成评测
- **Benchmark** · 训练中检查点和下游成功概率
- **关键结果 / 消融** · 作者报告可快速预测任务表现
- **适用条件 / 局限** · 外推至新训练方案需校验

**可复用机制** · 用少量真实评测维护代理评分

<a id="paper-150772"></a>

## Fast and Stable Triangular Inversion for Delta-Rule Linear Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/150772) · [作者来源](https://openreview.net/forum?id=fU54rMdv6G)

- **问题 / 瓶颈** · Delta-rule 的三角求逆易成为瓶颈且误差会传播
- **核心创新 / 方法** · 系统比较以矩阵乘为主的直接与迭代方案
- **Baseline** · 多种直接和迭代三角求逆
- **Benchmark** · Delta-rule 线性 Transformer 的数值与硬件评测
- **关键结果 / 消融** · 提供复杂度、稳定性和实践对照
- **适用条件 / 局限** · 硬件和精度配置会改变取舍

**可复用机制** · 用端到端模型误差验证内核选择

<a id="paper-154725"></a>

## Fast-dLLM++: Fr\'{e}chet Profile Decoding for Faster Diffusion LLM Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/154725) · [作者来源](https://openreview.net/forum?id=BTfatNCwhE)

- **问题 / 瓶颈** · 最弱 token 置信度过度限制异质集合
- **核心创新 / 方法** · 保留模型和缓存的训练后解码，使用排序置信度轮廓
- **Baseline** · Fast-dLLM 的同置信选择规则
- **Benchmark** · 扩散语言模型并行生成，具体任务待核
- **关键结果 / 消融** · 同置信时退化为旧规则，异质时给出理论增益
- **适用条件 / 局限** · 依赖置信度的可靠性

**可复用机制** · 在同等任务准确率下比较最小置信与全轮廓提交

<a id="paper-151622"></a>

## FastDSAC: Unlocking the Potential of Maximum Entropy RL in High-Dimensional Humanoid Control

[官方论文页](https://neurips.cc/virtual/2026/poster/151622) · [作者来源](https://openreview.net/forum?id=ZBAe6ak1l6)

- **问题 / 瓶颈** · 高维探索低效且价值估计不稳
- **核心创新 / 方法** · 动态调节逐维熵并使用连续分布式 critic
- **Baseline** · 确定性策略梯度与随机策略
- **Benchmark** · HumanoidBench 和连续控制任务
- **关键结果 / 消融** · 作者报告随机策略表现改善并与确定性方法竞争
- **适用条件 / 局限** · 探索收益依赖动作维和吞吐配置

**可复用机制** · 独立消融熵调节和价值分布表示

<a id="paper-156001"></a>

## FASTER: Rethinking Real-Time Flow VLAs

[官方论文页](https://neurips.cc/virtual/2026/poster/156001) · [作者来源](https://openreview.net/forum?id=1G2AcEojJU)

- **问题 / 瓶颈** · 异步平滑不等同于快速反应
- **核心创新 / 方法** · 流采样中优先去噪近期动作并分析首动作时延
- **Baseline** · 固定流采样日程与异步推理
- **Benchmark** · VLA 反应时延和动作段执行
- **关键结果 / 消融** · 作者报告紧迫动作去噪显著加快
- **适用条件 / 局限** · 反应时分布取决于模型假设及执行时域

**可复用机制** · 把首动作延迟和执行时域分开监控

<a id="paper-149442"></a>

## FASTER: Value-Guided Sampling for Fast RL

[官方论文页](https://neurips.cc/virtual/2026/poster/149442) · [作者来源](https://openreview.net/forum?id=q3wZBBqRAC)

- **问题 / 瓶颈** · 完整采样多个动作代价高
- **核心创新 / 方法** · 将候选逐步淘汰表示为 MDP，并训练中间价值
- **Baseline** · 完整生成后再选候选
- **Benchmark** · 长时机器人操作与生成策略推理
- **关键结果 / 消融** · 作者报告降低候选计算成本并维持回报，具体值待核
- **适用条件 / 局限** · 早期价值误差可能错删候选

**可复用机制** · 对比计算节省与正确候选保留率

<a id="paper-153523"></a>

## Fast Gauss-Newton for Multiclass Cross-Entropy

[官方论文页](https://neurips.cc/virtual/2026/poster/153523) · [作者来源](https://openreview.net/forum?id=KiUlDWxNTi)

- **问题 / 瓶颈** · 全 GGN 耦合全部 logits
- **核心创新 / 方法** · 保留秩一项并用无矩阵共轭梯度求解
- **Baseline** · 完整 GGN
- **Benchmark** · 多类交叉熵的曲率与训练
- **关键结果 / 消融** · 正半定下近似，二分类精确且损失梯度保持
- **适用条件 / 局限** · 忽略竞争类别内协方差

**可复用机制** · 在多类任务比较曲率保真与求解预算

<a id="paper-152762"></a>

## Fast Learning Rates for Physics-Informed Kernel Methods

[官方论文页](https://neurips.cc/virtual/2026/poster/152762) · [作者来源](https://openreview.net/forum?id=QYqNJIQKwh)

- **问题 / 瓶颈** · 物理信息与函数观测的边际收益不明确
- **核心创新 / 方法** · 分析结合噪声值和线性微分观测的核估计量
- **Baseline** · 只给有限微分信息与完美约束的理论对照
- **Benchmark** · 有限样本误差界和数值模拟
- **关键结果 / 消融** · 超过问题相关阈值后达到完美约束的速率
- **适用条件 / 局限** · 依赖线性算子及核函数条件

**可复用机制** · 为差分和观测预算各画学习曲线

<a id="paper-152917"></a>

## Exactness Matters for Physical Rule Enforcement

[官方论文页](https://neurips.cc/virtual/2026/poster/152917) · [作者来源](https://openreview.net/forum?id=PR7Uan6tks)

- **问题 / 瓶颈** · 近似物理校正可能引起滚动分布偏移
- **核心创新 / 方法** · 比较目标流形上保持恒等的精确投影与近似清理
- **Baseline** · 原始 FNO、事后投影、循环内投影
- **Benchmark** · NS-128、非周期 CFDBench、层级预测
- **关键结果 / 消融** · NS-128 百步末步 MSE 从约 9.39e-5 降至循环内 5.37e-7；近似清理可降散度却增预测误差
- **适用条件 / 局限** · 精确性取决于边界与目标几何

**可复用机制** · 用真实目标失真和滚动误差共同选择校正强度

<a id="paper-148197"></a>

## Fast Reconstruction of Exact Maxwell Dynamics from Sparse Data

[官方论文页](https://neurips.cc/virtual/2026/poster/148197) · [作者来源](https://openreview.net/forum?id=zcI6E4WHeK)

- **问题 / 瓶颈** · 稀疏场观测下残差惩罚增加优化负担
- **核心创新 / 方法** · 浅层网络组合满足均匀介质 Maxwell 方程的精确解，证明模型类具有通用逼近性
- **Baseline** · 摘要未列具名模型
- **Benchmark** · 三维稀疏点观测，测相对验证误差和方程残差
- **关键结果 / 消融** · 约千点时误差低于 1%，方程残差为零
- **适用条件 / 局限** · 针对均匀介质设定

**可复用机制** · 线性控制方程可解析时，比较可行基网络与软约束训练

<a id="paper-149044"></a>

## Fast, Relaxation‑ and Hyperparameter‑Free Pairwise Worst-Case Class Separation

[官方论文页](https://neurips.cc/virtual/2026/poster/149044) · [作者来源](https://openreview.net/forum?id=tIGr4bvK5s)

- **问题 / 瓶颈** · 整体散布目标可掩盖局部类别混淆
- **核心创新 / 方法** · 最大化最小成对类间与类内散布比，外层分式变换、内层迭代求解二次规划
- **Baseline** · 判别降维方法，名称待核
- **Benchmark** · 分类误差评测
- **关键结果 / 消融** · 作者报告分类误差一致改善并给出收敛论证
- **适用条件 / 局限** · 非凸问题的收敛不等于全局最优

**可复用机制** · 在类对难度不均时报告最差类对和总体分类误差

<a id="paper-148369"></a>

## Fast-RL: Accelerating Reinforcement Learning for LongCoT Reasoning Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148369) · [作者来源](https://openreview.net/forum?id=yNcSbtT8cr)

- **问题 / 瓶颈** · 长思考采样主导强化学习成本
- **核心创新 / 方法** · 先以 LoRA 学模式切换并冻结，再用快思考采样更新推理参数
- **Baseline** · 常规慢思考强化学习
- **Benchmark** · 文本及多模态推理，含 Qwen3-1.7B 的 AIME24
- **关键结果 / 消融** · 作者报告约十倍训练加速，AIME24 慢快模式分别提升 10.0 和 13.7
- **适用条件 / 局限** · 前提是两模式共享技能且可可靠切换

**可复用机制** · 将采样模式控制与能力参数解耦，检验短轨迹更新能否转移

<a id="paper-149383"></a>

## Fast Sandwich Products in Clifford Algebra

[官方论文页](https://neurips.cc/virtual/2026/poster/149383) · [作者来源](https://openreview.net/forum?id=qRvZDh6s22)

- **问题 / 瓶颈** · 显式夹积或完整作用矩阵随代数维度膨胀
- **核心创新 / 方法** · 按阶将夹积分解成向量旋转的外幂，再把 Givens 旋转提升为稀疏基更新
- **Baseline** · 现有旋量夹积实现
- **Benchmark** · 墙钟耗时和内存
- **关键结果 / 消融** · 最高分别改善 64 倍和 35 倍
- **适用条件 / 局限** · 收益取决于维度与实现

**可复用机制** · 避免生成全维算子，直接组合低维作用在各子空间的提升

<a id="paper-149922"></a>

## Fast-WAM: Do World Action Models Need Test-time Future Imagination?

[官方论文页](https://neurips.cc/virtual/2026/poster/149922) · [作者来源](https://openreview.net/forum?id=mBYJRAFq7D)

- **问题 / 瓶颈** · 迭代生成未来帧增加动作延迟
- **核心创新 / 方法** · 通过对照变体分离视频共训练和测试时显式预测
- **Baseline** · 先想象再执行的 WAM 及移除视频共训练变体
- **Benchmark** · LIBERO、RoboTwin、真机任务、推理时延
- **关键结果 / 消融** · 110 ms，较想象后执行方法快逾六倍；移除视频共训练影响更大
- **适用条件 / 局限** · 现有任务未覆盖所有依赖未来预测的场景

**可复用机制** · 独立消融训练监督与推理路径，量化效果及响应延迟

<a id="paper-156637"></a>

## Fast Wasserstein rates for estimating probability distributions of probabilistic graphical models

[官方论文页](https://neurips.cc/virtual/2026/poster/156637) · [作者来源](https://neurips.cc/virtual/2026/poster/156637)

- **问题 / 瓶颈** · 高维 Wasserstein 估计存在维数灾难
- **核心创新 / 方法** · 对给定 DAG 的条件转移核施加可量化光滑条件
- **Baseline** · 弱 Wasserstein 与强双向 TV 光滑条件的理论对照
- **Benchmark** · 独立同分布样本下 Wasserstein 误差速率
- **关键结果 / 消融** · 速率由局部维度支配，强条件下证明尖锐性
- **适用条件 / 局限** · 需要已知图及对应光滑性

**可复用机制** · 先核实局部条件分布结构，再决定是否采用图分解估计

<a id="paper-148441"></a>

## Fault Tolerance in Transformers Favors Output Alignment over Hidden-State Consistency

[官方论文页](https://neurips.cc/virtual/2026/poster/148441) · [作者来源](https://openreview.net/forum?id=xm2tQzphI5)

- **问题 / 瓶颈** · 直接对齐故障位置隐藏状态可能约束过强
- **核心创新 / 方法** · 训练时模拟计算故障并比较输出 KL 与隐藏对齐目标
- **Baseline** · 隐藏对齐、SAM、R-Drop、SAF
- **Benchmark** · GPT-2 Small、8B 与留出语料，测困惑度退化
- **关键结果 / 消融** · 小模型退化从 12.9% 降至 0.21%；直接隐藏约束可恶化
- **适用条件 / 局限** · 受模拟故障分布限制

**可复用机制** · 用同预算对照不同对齐位置，并在未见语料测容错

<a id="paper-153584"></a>

## Fault Tolerant Coresets

[官方论文页](https://neurips.cc/virtual/2026/poster/153584) · [作者来源](https://openreview.net/forum?id=KKronbQMtE)

- **问题 / 瓶颈** · 普通带权核心集在摘要被损坏时无法保持代价
- **核心创新 / 方法** · 用敏感度采样构造可高效清理解码的冗余摘要
- **Baseline** · 普通敏感度核心集及容错大小下界
- **Benchmark** · k-means 代价近似与实验验证
- **关键结果 / 消融** · 额外规模项与 f·k/ε 同阶，并有相应必要下界
- **适用条件 / 局限** · 限于指定损坏预算和目标

**可复用机制** · 设计压缩摘要时同时度量原始逼近和损坏后的可恢复性

<a id="paper-151814"></a>

## FAUST: Federated Asynchronous Update with Staggered Timescales for Low-Communication Foundation Model Training

[官方论文页](https://neurips.cc/virtual/2026/poster/151814) · [作者来源](https://openreview.net/forum?id=Xos5UImld5)

- **问题 / 瓶颈** · 同步所有状态会增加通信，长期不同步可能破坏收敛
- **核心创新 / 方法** · 组合序列并行图重写和分层同步，将前向重分布与可延迟归约区分
- **Baseline** · DDP、Local Adam、DES-LOC
- **Benchmark** · 最高 1.3B 参数语言模型，比较通信开销、困惑度和总时间
- **关键结果 / 消融** · 作者报告困惑度距全同步不超过 4.6%，总耗时少 27%
- **适用条件 / 局限** · 结果取决于带宽及并行拓扑

**可复用机制** · 按状态漂移特征分配同步频率，监控全局质量而非只看通信

<a id="paper-156009"></a>

## FAVLA: A Force-Adaptive Multi-Rate VLA model for Contact-Rich Robotic Manipulation

[官方论文页](https://neurips.cc/virtual/2026/poster/156009) · [作者来源](https://openreview.net/forum?id=1BsG8wfOjt)

- **问题 / 瓶颈** · 统一低频融合丢失接触瞬间信息
- **核心创新 / 方法** · 低频视觉语言模型预测力统计，高频专家按力反馈修正动作块并动态融合
- **Baseline** · 力感知 VLA
- **Benchmark** · 真机精密接触操作，测成功率与峰值力
- **关键结果 / 消融** · 平均成功率 88.8%，同时降低峰值接触力
- **适用条件 / 局限** · 依赖力传感及力变化预测

**可复用机制** · 用事件不确定性触发快速闭环，分阶段检查延迟和接触峰值

<a id="paper-156133"></a>

## 𝑓-Differential Privacy Filters: Validity and Approximate Solutions

[官方论文页](https://neurips.cc/virtual/2026/poster/156133) · [作者来源](https://openreview.net/forum?id=0AH3Ph6OYP)

- **问题 / 瓶颈** · 静态张量积记账不一定能用于全自适应停止
- **核心创新 / 方法** · 刻画自然 f-DP 过滤器的有效条件，并以自适应中心极限定理导出近似过滤器
- **Baseline** · 自然张量积过滤器及 RDP 记账
- **Benchmark** · 子采样高斯机制的理论渐近比较
- **关键结果 / 消融** · 自然规则一般无效，近似方法在两端渐近区间优于 RDP
- **适用条件 / 局限** · 实际子采样率的近似可能乐观

**可复用机制** · 上线自适应预算前区分有限样本保证与渐近估计

<a id="paper-151552"></a>

## Feasible Policy Optimization for Safe Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151552) · [作者来源](https://openreview.net/forum?id=ZmudjL054f)

- **问题 / 瓶颈** · 每次更新同时严格约束可能保守
- **核心创新 / 方法** · 可行区内提升价值，区外降低可行性代价，利用约束衰减界分析共同解
- **Baseline** · 安全强化学习方法
- **Benchmark** · Safety-Gymnasium，检查约束满足和回报
- **关键结果 / 消融** · 作者报告约束表现好且任务回报有竞争力
- **适用条件 / 局限** · 训练期与部署保证需分别核实

**可复用机制** · 在受限任务中分别评估越界修复和可行区内收益

<a id="paper-152364"></a>

## FeatCal: Feature Calibration for Post-Merging Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152364) · [作者来源](https://openreview.net/forum?id=TbWDPX0nam)

- **问题 / 瓶颈** · 合并误差由局部失配和上游累积共同产生
- **核心创新 / 方法** · 按层以闭式解小幅更新权重，使其接近专家在同输入上的表征
- **Baseline** · Surgery、ProbSurgery
- **Benchmark** · CLIP 与 GLUE 模型融合任务
- **关键结果 / 消融** · CLIP 85.5% 对 77.0% 和 78.8%；GLUE 85.2% 对 83.7% 和 82.2%
- **适用条件 / 局限** · 需要代表性校准数据和可访问专家

**可复用机制** · 在融合完成后比较逐层校准与仅修正最后层

<a id="paper-148620"></a>

## Feature-Context Consistency: Unsupervised Adversarial Detection with Drift Stability on Attributed Graphs

[官方论文页](https://neurips.cc/virtual/2026/poster/148620) · [作者来源](https://openreview.net/forum?id=wOczaNixQw)

- **问题 / 瓶颈** · 标签迟到且自然漂移会导致误报
- **核心创新 / 方法** · 以无监督 Context Boost 度量节点与聚合邻域的一致性，分析检测和漂移稳定性
- **Baseline** · 监督 GNN、图异常检测和标准 RBM
- **Benchmark** · Ethereum 钓鱼与 Reddit 封禁数据等，测 AUROC 与 FPR
- **关键结果 / 消融** · 作者报告 AUROC 至少 0.96，漂移下 FPR 接近 5% 校准目标
- **适用条件 / 局限** · 依赖合法节点的邻域一致性

**可复用机制** · 单独测自然漂移下误报，避免把正常变化误当异常

<a id="paper-152004"></a>

## Feature Information Dynamics in Diffusion

[官方论文页](https://neurips.cc/virtual/2026/poster/152004) · [作者来源](https://openreview.net/forum?id=WDfD9WTJeJ)

- **问题 / 瓶颈** · 粗到细生成通常只靠定性判断
- **核心创新 / 方法** · 从无条件与特征条件去噪损失差估计信息密度，再分解层级特征的共享和独有信息
- **Baseline** · 像素扩散及 SDVAE、VAVAE、RAE 表示
- **Benchmark** · 频谱与类别、掩码、边缘层级的比较
- **关键结果 / 消融** · 定量验证像素域频谱顺序，并发现不同潜空间的时序不同
- **适用条件 / 局限** · 依赖去噪估计精度及特征定义

**可复用机制** · 做扩散控制设计前先测目标特征在各时间段的信息变化

<a id="paper-149864"></a>

## Feature learning  in high-dimensions under structured covariance: Scaling laws in quadratic networks

[官方论文页](https://neurips.cc/virtual/2026/poster/149864) · [作者来源](https://openreview.net/forum?id=mftAwZQsHo)

- **问题 / 瓶颈** · 各向同性理论难涵盖真实数据的方向差异。
- **核心创新 / 方法** · 在二次激活两层网络中解析各向异性高斯输入下的在线 SGD 和连续极限。
- **Baseline** · 各向同性理论与归一化前后的设置。
- **Benchmark** · 二次网络理论及一般激活的两层网络实验。
- **关键结果 / 消融** · 协方差谱影响尺度指数和样本复杂度；归一化提高样本效率的证据见作者摘要。
- **适用条件 / 局限** · 一般激活仅获实验支持，非高斯数据外推待核。

**可复用机制** · 比较样本效率前记录协方差谱，并用归一化对照区分输入谱与架构的影响。

<a id="paper-151094"></a>

## Feature Recovery for Object Understanding Under Physical Transformation

[官方论文页](https://neurips.cc/virtual/2026/poster/151094) · [作者来源](https://openreview.net/forum?id=d1FI4Z8ezj)

- **问题 / 瓶颈** · 结构性变换不同于一般图像噪声，外观变化会破坏原物体识别。
- **核心创新 / 方法** · 冻结视觉骨干，用 FRM 将退化特征映射到原始状态对齐的表示。
- **Baseline** · 无 FRM 的原模型，包括 RF-DETR、InternVL3.5 等。
- **Benchmark** · TRACE 含约 2.14 万个合成场景与 499 个物体身份，覆盖检测与原始属性恢复。
- **关键结果 / 消融** · 随变换加剧，RF-DETR mAP 相对降 71%；FRM 的检索平均提升 12.5%，具体增益口径待核。
- **适用条件 / 局限** · 需配对监督；真实火灾场景迁移尚待核查。

**可复用机制** · 测试结构性变换时按强度比较冻结骨干与特征恢复模块，分别测定位和语义恢复。

<a id="paper-152149"></a>

## FedCF: Fair Federated Conformal Prediction

[官方论文页](https://neurips.cc/virtual/2026/poster/152149) · [作者来源](https://openreview.net/forum?id=VAwYqelahI)

- **问题 / 瓶颈** · 总体覆盖可能掩盖不同人口组的覆盖缺口。
- **核心创新 / 方法** · 将 Conformal Fairness 扩展到联邦设置，分析人口组之间的公平差距。
- **Baseline** · 原 Conformal Fairness 框架和只考察总体覆盖的保形预测。
- **Benchmark** · 多领域数据集，检查不同组的覆盖与差距。
- **关键结果 / 消融** · 摘要报告经验验证；量化结论待核。
- **适用条件 / 局限** · 依赖所设交换性假设，跨客户端偏移下需复查。

**可复用机制** · 评估分布式不确定性系统时，同时报告总体、组别及跨客户端覆盖。

<a id="paper-153466"></a>

## Federated Concept-Based Models: Interpretable models with distributed supervision

[官方论文页](https://neurips.cc/virtual/2026/poster/153466) · [作者来源](https://openreview.net/forum?id=L7HwKQPq8i)

- **问题 / 瓶颈** · 单个机构往往无法标注所有概念，固定架构又难容纳新概念。
- **核心创新 / 方法** · 跨机构聚合概念信息，并随可用监督调整概念模型架构。
- **Baseline** · 全量概念监督与非自适应联邦模型。
- **Benchmark** · 预测准确率、概念干预效果及机构未标注概念上的推理。
- **关键结果 / 消融** · 作者报告准确率和干预效果接近全量监督，平均优于非自适应对照。
- **适用条件 / 局限** · 概念定义须能跨机构对应，隐私保护边界待全文确认。

**可复用机制** · 测试动态概念库时应单独留出本地无监督的概念，检验真正的跨机构迁移。

<a id="paper-155993"></a>

## Federated Distributionally Robust Neural Combinatorial Optimization with Convergence Guarantees

[官方论文页](https://neurips.cc/virtual/2026/poster/155993) · [作者来源](https://openreview.net/forum?id=1JoBgRVNAk)

- **问题 / 瓶颈** · REINFORCE 的方差受成本影响，难套用联邦 DRO 的损失假设。
- **核心创新 / 方法** · 在有界成本下推导联邦 Group DRO，加入 KL 正则稳定组权重。
- **Baseline** · 朴素 Group DRO 与 FedAvg。
- **Benchmark** · 容量约束车辆路径优化及最坏组表现。
- **关键结果 / 消融** · 作者给出 O(1/√T) 收敛保证；KL 对照避免权重塌缩。
- **适用条件 / 局限** · 有界成本与组定义对保证至关重要。

**可复用机制** · 最坏组优化时同时监控组权重和目标值，将稳定权重的正则单独消融。

<a id="paper-152765"></a>

## Federated Graph Learning with Local Message Compensation

[官方论文页](https://neurips.cc/virtual/2026/poster/152765) · [作者来源](https://openreview.net/forum?id=QXvATxXC7l)

- **问题 / 瓶颈** · 分割图使外部邻居的结构与语义消息丢失。
- **核心创新 / 方法** · 分别用语义代理补语义，用社区锚点约束补偿后的结构。
- **Baseline** · 联邦图学习基线，具名方法待核。
- **Benchmark** · 12 个同质和异质图数据集，含高度碎片化条件。
- **关键结果 / 消融** · 作者报告在所比方法中表现较优，碎片化条件更稳健。
- **适用条件 / 局限** · 代理与真实外邻居关系可能失配。

**可复用机制** · 按语义与拓扑两类缺失分别建立代理，并随切图比例测试。

<a id="paper-150671"></a>

## Federated Learning by Utility-Constrained Stochastic Aggregation for Improving Rational Participation

[官方论文页](https://neurips.cc/virtual/2026/poster/150671) · [作者来源](https://openreview.net/forum?id=gM2WzBs4Gb)

- **问题 / 瓶颈** · 跨机构参与方可能因本地收益不足退出。
- **核心创新 / 方法** · 以客户端效用可行性约束全局目标，并用随机聚合维持参与。
- **Baseline** · 默认客户端被动参与的联邦训练方法。
- **Benchmark** · 标准数据集，评估客户端留存与全局表现。
- **关键结果 / 消融** · 作者报告留存与全局模型表现同时提高，数值待核。
- **适用条件 / 局限** · 收益阈值需定义并估计，策略性行为边界待核。

**可复用机制** · 设计协作机制时应对照仅优化全局质量与加入本地退出阈值的效果。

<a id="paper-153323"></a>

## Federate the Router: Learning Language Model Routers with Sparse and Decentralized Evaluations

[官方论文页](https://neurips.cc/virtual/2026/poster/153323) · [作者来源](https://openreview.net/forum?id=MABQINnqfs)

- **问题 / 瓶颈** · 单个客户端只覆盖有限查询类型和模型。
- **核心创新 / 方法** · 针对 MLP 和 K-means 路由器，在客户端评估覆盖不一致时学习共享策略。
- **Baseline** · 仅用客户端本地评估训练的路由器。
- **Benchmark** · 两个基准，评估质量与推理成本前沿。
- **关键结果 / 消融** · 作者报告联邦协作改善准确率与成本折衷，并给出路由次优性分析。
- **适用条件 / 局限** · 适用于离线查询模型评分；评估口径及模型可用性需一致。

**可复用机制** · 训练路由器时同时测查询域外泛化和本地从未评估过的模型覆盖。

<a id="paper-156743"></a>

## FedIndex: Federated Domain Adaptation with Continuous Domain Indices

[官方论文页](https://neurips.cc/virtual/2026/poster/156743) · [作者来源](https://openreview.net/forum?id=fnbGFH0330)

- **问题 / 瓶颈** · 类别标签无法描述域间平滑变化。
- **核心创新 / 方法** · 利用全局判别器在不访问客户端原始数据的条件下对齐连续索引对应的分布。
- **Baseline** · 先前联邦域适配方法，具名基线待核。
- **Benchmark** · 合成及真实数据集的联邦域迁移。
- **关键结果 / 消融** · 作者报告理论支持域不变特征形成，并在所测数据上优于对照。
- **适用条件 / 局限** · 索引需能表达变化；外推到未覆盖索引的能力待核。

**可复用机制** · 用连续测量值描述数据偏移，并分开衡量索引区间内插值与区间外外推。

<a id="paper-148442"></a>

## FedLoVA: Value-Only Aggregation for Federated LoRA Fine-Tuning of Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148442) · [作者来源](https://openreview.net/forum?id=xlkHd6pwR7)

- **问题 / 瓶颈** · 不同投影更新速度不同，统一同步增加开销。
- **核心创新 / 方法** · 分别测 Q 和 V 的收敛后，只向服务器共享 V 的 LoRA 更新。
- **Baseline** · 既有联邦语言模型微调基线。
- **Benchmark** · 自然语言理解、多语种情感分析与生成任务。
- **关键结果 / 消融** · 作者报告通信成本最高减少至约 1/7.8，性能相近。
- **适用条件 / 局限** · 收益可能取决于骨干、任务和客户端异质性。

**可复用机制** · 在通信受限时按子模块测收敛，比较全部同步与只同步稳定活跃模块。

<a id="paper-151499"></a>

## FedPeel: Peeling Stabilized Layers for Robust Heterogeneous Federated Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151499) · [作者来源](https://openreview.net/forum?id=aD69yKg1Sj)

- **问题 / 瓶颈** · 不加区分地聚合代理模型可能导致震荡与负迁移。
- **核心创新 / 方法** · 选择稳定层，在频域分解共享与个体信息，并按样本教师置信度调节知识转移。
- **Baseline** · 异构联邦代理蒸馏方法，具体名称待核。
- **Benchmark** · 图像、文本与音频基准，衡量准确率、通信量和收敛。
- **关键结果 / 消融** · 作者给出 O(1/T) 收敛率并报告准确率和通信效率改善。
- **适用条件 / 局限** · 多种改变并用，各自独立增益和稳定判定待全文核查。

**可复用机制** · 用逐层稳定性决定通信时机，再用样本置信度控制哪些蒸馏信号可迁移。

<a id="paper-156778"></a>

## Fed-SB: A Silver Bullet for Extreme Communication Efficiency and Performance in (Private) Federated LoRA Fine-Tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/156778) · [作者来源](https://openreview.net/forum?id=87UyFEhzyP)

- **问题 / 瓶颈** · 独立平均低秩因子可能不能还原实际更新。
- **核心创新 / 方法** · 采用 LoRA-SB，固定左右因子，仅训练并平均夹在中间的方阵。
- **Baseline** · 传统适配器平均及高通信替代方法。
- **Benchmark** · 常识、算术和语言推断，比较通信成本与任务表现。
- **关键结果 / 消融** · 摘要报告通信成本最多降低 230 倍。
- **适用条件 / 局限** · 需要共享适配基；秩与隐私预算细节待核。

**可复用机制** · 对齐客户端基底后再聚合中间参数，测实际更新误差与传输量。

<a id="paper-153077"></a>

## FedVSSAM: Mitigating Flatness Incompatibility in Sharpness-Aware Federated Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/153077) · [作者来源](https://openreview.net/forum?id=OB02U98b9E)

- **问题 / 瓶颈** · 客户端各自偏好的平坦区域可能与全局目标不一致。
- **核心创新 / 方法** · 构造方差抑制方向并贯穿 SAM 搜索和更新。
- **Baseline** · 联邦 SAM 与其他联邦基线。
- **Benchmark** · 异质联邦学习设置，考虑局部更新与设备部分参与。
- **关键结果 / 消融** · 作者给出非凸收敛保证并报告优于基线。
- **适用条件 / 局限** · 额外估计成本和极端异质性下效果待核。

**可复用机制** · 不要只测客户端平坦度，另测方向偏离和全局表现。

<a id="paper-152267"></a>

## Feedback World Model Enables Precise Guidance of Diffusion Policy

[官方论文页](https://neurips.cc/virtual/2026/poster/152267) · [作者来源](https://openreview.net/forum?id=ULmPp5GXSX)

- **问题 / 瓶颈** · 分布外状态下静态动力学预测偏差会累积。
- **核心创新 / 方法** · 仅在线更新轻量潜空间反馈状态，并突出可由动作控制的预测成分。
- **Baseline** · 静态预测及普通引导，具名对照待核。
- **Benchmark** · LIBERO-Plus、Robomimic 和真机操作。
- **关键结果 / 消融** · 预测误差最多降低 76.4%，分布外成功率提高 30%。
- **适用条件 / 局限** · 需要执行后观测，收敛依赖潜空间观察器条件。

**可复用机制** · 分别消融反馈修正和动作引导以区分预测精度和控制收益。

<a id="paper-149287"></a>

## Feedforward Novel View Synthesis for Heterogeneous Cameras

[官方论文页](https://neurips.cc/virtual/2026/poster/149287) · [作者来源](https://openreview.net/forum?id=rQBdZ03odN)

- **问题 / 瓶颈** · 中心射线不能区分各相机中图块的投影覆盖。
- **核心创新 / 方法** · 引入局部射线图，并用角坐标替代像素网格做二维 RoPE。
- **Baseline** · 现有相机条件的新视角合成方法。
- **Benchmark** · ScanNet++ 混合相机与未见全景投影。
- **关键结果 / 消融** · 报告混合相机表现改善及全景零样本泛化。
- **适用条件 / 局限** · 要求相机标定且采用适用的中心相机模型。

**可复用机制** · 比较只编码图块中心和保留图块角覆盖的信息量。

<a id="paper-150142"></a>

## Feeling of Knowing in Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150142) · [作者来源](https://openreview.net/forum?id=kMAaCSiUd6)

- **问题 / 瓶颈** · 知识变化可能与自评信号不同步。
- **核心创新 / 方法** · 独立知识更新和自评通道，用中间知识状态训练校准器，再据判断优化回答行为。
- **Baseline** · 后训练前的自评和未显式对齐的模型。
- **Benchmark** · 三个知识更新评测集，名称及指标待核。
- **关键结果 / 消融** · 报告更新知识上的判断质量改善。
- **适用条件 / 局限** · 需追踪中间知识状态，跨主题稳健性待核。

**可复用机制** · 在每轮知识更新后以新旧知识分组检验检索触发与弃答。

<a id="paper-152029"></a>

## FerQ: Fermat Quotient Reformulation of High-Order Binary Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/152029) · [作者来源](https://openreview.net/forum?id=W4U6AMYhfN)

- **问题 / 瓶颈** · 高阶能量难直接交给二次优化器。
- **核心创新 / 方法** · 用标量聚合上的费马商组合表示单项式，另推导量子退火的二次嵌入。
- **Baseline** · 十二种已有能量变换。
- **Benchmark** · 四个来源的 k-SAT、Max-k-SAT 及随机玻璃和局域哈密顿量。
- **关键结果 / 消融** · 报告最高满足率与最低 CPU 时间。
- **适用条件 / 局限** · 重写不取消组合求解难度，嵌入开销仍随设定而异。

**可复用机制** · 对比变换规模、求解耗时及最终能量，避免只衡量辅助变量数。

<a id="paper-156119"></a>

## Few Channels Draw The Whole Picture: Revealing Massive Activations in Diffusion Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/156119) · [作者来源](https://openreview.net/forum?id=0GAdp0EnE3)

- **问题 / 瓶颈** · DiT 内部提示语义载体不清楚
- **核心创新 / 方法** · 以等规模通道干预、空间聚类和良性语义转移交叉验证
- **Baseline** · 同样数量的低统计量通道
- **Benchmark** · 文本到图像的质量、主体区域及语义插值，具名指标待核
- **关键结果 / 消融** · 高激活通道清零使质量明显下降，且聚类与显著区域一致
- **适用条件 / 局限** · 跨模型和提示的稳定性待核

**可复用机制** · 用匹配干预规模的负对照区分高激活通道与真正承担语义的通道。

<a id="paper-156779"></a>

## Few Contrastive Attention Heads Enable Visual Grounding in Large Vision-Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/156779) · [作者来源](https://openreview.net/forum?id=CnrAiXbw8a)

- **问题 / 瓶颈** · 视觉定位常需专门标签或结构改造
- **核心创新 / 方法** · 将双提示残差差异投影到各头输出空间，按重要性加权前十个头
- **Baseline** · 免训练非 LVLM 与 LVLM 基线
- **Benchmark** · RefCOCO、RefCOCO+、RefCOCOg，定位指标定义待核
- **关键结果 / 消融** · 对前类基线最高提升分别为 27.95%、21.93%、8.40%
- **适用条件 / 局限** · 依赖对照描述与头部排名的稳定性

**可复用机制** · 换骨干时先用目标和对照提示估计各头定位贡献，再测少头聚合。

<a id="paper-150752"></a>

## Few-shot Task Learning via Compositional Concept Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/150752) · [作者来源](https://openreview.net/forum?id=feUnReGdA8)

- **问题 / 瓶颈** · 行为克隆难分离目标、空间关系与约束
- **核心创新 / 方法** · COIN 先从示范推断概念组合，再调用策略实现
- **Baseline** · 行为克隆和 π₀ 等预训练策略
- **Benchmark** · 物体重排、导航、人动作生成及 LIBERO-90
- **关键结果 / 消融** · LIBERO-90 平均成功率 96.9%，参数约为 π₀ 的十分之一
- **适用条件 / 局限** · 依赖可重用概念及实现它们的策略

**可复用机制** · 分别测试见过概念的新组合和新概念，区分推断与执行失误。

<a id="paper-150793"></a>

## Few-Shot Visual Concept Extraction for Steering Diffusion Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/150793) · [作者来源](https://openreview.net/forum?id=fMSQSo0vsU)

- **问题 / 瓶颈** · 文本层调整难精准控制局部属性
- **核心创新 / 方法** · 由少量正负图像提示估计残差方向，场景级全局聚合、区域级掩码聚合
- **Baseline** · 文本编码器引导、免训练激活编辑及专用编辑模型
- **Benchmark** · 图像色彩、材质、光照及风格控制，具名基准待核
- **关键结果 / 消融** · 作者报告优于所比免训练对照，量化幅度待核
- **适用条件 / 局限** · 区域划分出错或属性共现可能产生串扰

**可复用机制** · 同预算对照全局和掩码均值差，分开测目标属性与背景保持。

<a id="paper-154720"></a>

## Few-Step Boltzmann Generators via Scalable Likelihood Flow Maps

[官方论文页](https://neurips.cc/virtual/2026/poster/154720) · [作者来源](https://openreview.net/forum?id=BW8H7viD5K)

- **问题 / 瓶颈** · 少步生成后，样本密度估计仍可能方差较大
- **核心创新 / 方法** · 用无需 Hutchinson 估计的可向量化目标蒸馏似然流映射
- **Baseline** · F2D2
- **Benchmark** · 图像数据上的训练成本与密度表现，具体指标待核
- **关键结果 / 消融** · 作者报告整体训练方差与耗时下降，图像分项数值待核
- **适用条件 / 局限** · 图像表现不能外推到其他专业科学任务

**可复用机制** · 对图像流模型同时报告生成质量、密度误差、训练方差和推理预算。

<a id="paper-151333"></a>

## Few-Step Diffusion Language Models via Trajectory Self-Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/151333) · [作者来源](https://openreview.net/forum?id=bJzsxLzKK7)

- **问题 / 瓶颈** · 减少去噪步数会放大 token 因子分解误差
- **核心创新 / 方法** · 轨迹自蒸馏配反向 KL 目标引导学生贴近教师模态
- **Baseline** · 完整步教师及少步解码对照
- **Benchmark** · 语言推理与常规代码生成基准，具名待核
- **关键结果 / 消融** · 作者报告少步与完整步差距缩小，数值和独立增益待核
- **适用条件 / 局限** · 依赖可获得教师轨迹，模式覆盖代价待核

**可复用机制** · 匹配解码步数，分别消融轨迹监督与末端目标。

<a id="paper-149510"></a>

## FFTSparse: Relative-Position Correlation Guided Sparse Attention for Long-Context Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149510) · [作者来源](https://openreview.net/forum?id=pbAu7eSrEE)

- **问题 / 瓶颈** · 动态稀疏掩码若逐对打分仍有二次成本
- **核心创新 / 方法** · 以 FFT 估计跨位置相关，按注意力头模式选择块稀疏掩码
- **Baseline** · 全注意力及动态稀疏方法
- **Benchmark** · 长上下文下游任务及 128K 预填充效率
- **关键结果 / 消融** · 掩码成本约全注意力的 0.02%，128K 最高加速 7.4 倍
- **适用条件 / 局限** · 依赖对角条带，离散关键证据召回须单测

**可复用机制** · 按头测量滞后结构，对照同预算邻域和频域掩码。

<a id="paper-155948"></a>

## FiedlerPrune: Connectivity-Preserving Cross-Layer Pruning for Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155948) · [作者来源](https://openreview.net/forum?id=1bEsw4hL3W)

- **问题 / 瓶颈** · 独立剪每层可能破坏跨层连接
- **核心创新 / 方法** · 将相邻线性层表示为加权多部图，用边对 Fiedler 值的贡献补充局部指标
- **Baseline** · 逐层及端到端剪枝
- **Benchmark** · 语言模型剪枝、推理加速、量化与微调兼容性
- **关键结果 / 消融** · 作者报告优于逐层对照，端到端剪枝成本低数个数量级，细节待核
- **适用条件 / 局限** · 图构造和层内指标会影响稀疏方案

**可复用机制** · 固定稀疏率检验图连通性分数是否改善精度和恢复成本。

<a id="paper-152438"></a>

## Fiedler-Regularized Causal Discovery for Sparse Connected DAGs

[官方论文页](https://neurips.cc/virtual/2026/poster/152438) · [作者来源](https://openreview.net/forum?id=T86xx1y8TJ)

- **问题 / 瓶颈** · 拟合、稀疏与无环约束仍可能产生碎片图
- **核心创新 / 方法** · 在光滑无向骨架的代数连通性上添加可微惩罚
- **Baseline** · GOLEM、图自编码器、DAG-GNN 的原版
- **Benchmark** · 最多 200 变量的稀疏连通合成图，测碎片和结构恢复
- **关键结果 / 消融** · 作者报告多个学习器均改善，幅度待核
- **适用条件 / 局限** · 真实过程如有独立子系统，约束可能引入伪边

**可复用机制** · 只在有连通先验时扫描惩罚，分别记录伪跨组边与结构误差。

<a id="paper-149180"></a>

## Fill the GAP: A Granular Alignment Paradigm for Visual Reasoning in Multimodal Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149180) · [作者来源](https://openreview.net/forum?id=sITfxatJtF)

- **问题 / 瓶颈** · 直接回灌可能遇到预归一化模型输入和输出的范数失配
- **核心创新 / 方法** · 以 PCA 对齐头映射视觉潜变量，用可检查视觉监督及按难度筛选样本
- **Baseline** · Qwen2.5-VL 7B 的不同监督变体
- **Benchmark** · 视觉感知与推理及潜变量干预，具名待核
- **关键结果 / 消融** · 作者报告监督变体中平均表现最好，潜变量提供任务相关信号
- **适用条件 / 局限** · 单骨干证据，三个模块独立效果待核

**可复用机制** · 比较范数兼容后的真实潜变量与等长占位 token，排除容量假象。

<a id="paper-155819"></a>

## FiLoRA: Focus-and-Ignore LoRA for Controllable Feature Reliance

[官方论文页](https://neurips.cc/virtual/2026/poster/155819) · [作者来源](https://openreview.net/forum?id=2eluv7sJYW)

- **问题 / 瓶颈** · 事后删除特征难验证模型对捷径依赖能否被主动调整
- **核心创新 / 方法** · 将 LoRA 对齐到各特征组，按指令选择激活
- **Baseline** · 固定预测目标下的特征干预，具名方法待核
- **Benchmark** · 图文和视听任务，测特征依赖变化和干预稳健性
- **关键结果 / 消融** · 作者报告门控可因果改变计算，且对伪相关干预更稳健
- **适用条件 / 局限** · 依赖可区分的特征组，跨模态稳定性待核

**可复用机制** · 固定标签与训练目标，比较核心及伪相关特征被调节时的预测。

<a id="paper-148574"></a>

## FILOsofer: A TEE-Shielded Model Partitioning Framework based on Fisher Information-Guided LoRA Obfuscation

[官方论文页](https://neurips.cc/virtual/2026/poster/148574) · [作者来源](https://openreview.net/forum?id=wrEeZDfTbu)

- **问题 / 瓶颈** · 全量可信执行昂贵，部分公开权重需要额外保护
- **核心创新 / 方法** · 以 Fisher 信息调节公开权重保护，将跨层低秩恢复参数置于 TEE
- **Baseline** · 既有 TEE 分区和整体可信执行方案
- **Benchmark** · 实际设置下的精度、安全与计算开销，具名待核
- **关键结果 / 消融** · 作者报告所测威胁设定下安全性接近黑盒，开销相较先前方法降低逾 50 倍
- **适用条件 / 局限** · 保证仅对应所测设置，硬件侧信道待核

**可复用机制** · 模型分区时记录保护参数量、端侧延迟和授权精度。

<a id="paper-152048"></a>

## Filter Banks: from Low-Rank Representations to Deep Models for Efficient Time Series Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/152048) · [作者来源](https://openreview.net/forum?id=VuOChaTi6n)

- **问题 / 瓶颈** · 复杂模型可能超过预测任务的内在秩
- **核心创新 / 方法** · 用降秩回归和核分析解释线性模型，再以滤波器组构造可调秩网络
- **Baseline** · 线性和近期轻量预测架构
- **Benchmark** · 长时序预测基准，具体数据及指标待核
- **关键结果 / 消融** · 作者报告多数基准表现有竞争力且计算成本较低
- **适用条件 / 局限** · 高秩时间变化可能不适合压缩

**可复用机制** · 先评估秩与误差曲线，再决定是否扩大网络深度。

<a id="paper-155800"></a>

## Filtered Conformal Ellipsoids for Graph-Native Time Series

[官方论文页](https://neurips.cc/virtual/2026/poster/155800) · [作者来源](https://openreview.net/forum?id=2mdgP5ws1o)

- **问题 / 瓶颈** · 分别校准各坐标难保证联合事件覆盖
- **核心创新 / 方法** · 在滤波均值和协方差的马氏分数上做分割保形，分析可观测预测分布的收缩
- **Baseline** · 静态协方差、无滤波、因子和 copula 方法
- **Benchmark** · METR-LA-20、PEMS-BAY-50 及扩展设置，测覆盖与体积
- **关键结果 / 消融** · 中等规模图任务中椭球较小，完整图和非图数据可由其他对照胜出
- **适用条件 / 局限** · 覆盖界依赖稳定性、协方差界和依赖性条件

**可复用机制** · 分开选择预测形状与覆盖校准，按图规模验证收益。

<a id="paper-153422"></a>

## Filtered-Trace Online Variational Training for Probabilistic Spiking Neural Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/153422) · [作者来源](https://openreview.net/forum?id=LRJMHwjMmy)

- **问题 / 瓶颈** · 全序列反传占用随序列长度增长的内存
- **核心创新 / 方法** · 用马尔可夫迹表示突触历史，并按预测范围调整未来信用估计
- **Baseline** · 全序列 BPTT
- **Benchmark** · 合成实验和 N-MNIST 分类，测偏差、准确率与内存
- **关键结果 / 消融** · 作者证明在核衰减条件下截断偏差指数下降，实验分类表现可比
- **适用条件 / 局限** · 长记忆核可能需要更大截断范围

**可复用机制** · 同时扫描训练内存、序列长度和估计偏差，避免仅根据分类准确率选截断长度。

<a id="paper-155504"></a>

## FIND: Frequency Invariance Disentanglement for Test-Time Adaptation in LiDAR 3D Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/155504) · [作者来源](https://openreview.net/forum?id=554xDogisf)

- **问题 / 瓶颈** · 空间自监督易混合语义与域风格
- **核心创新 / 方法** · B 样条自适应滤波分支分别生成伪标签和约束扰动一致性
- **Baseline** · 现有适配方法，名称待核
- **Benchmark** · 跨数据集与点云损坏测试
- **关键结果 / 消融** · 作者报告优于所比方法，幅度待核
- **适用条件 / 局限** · 依赖频率分解和伪标签质量

**可复用机制** · 用频域分支分离内容和传感器变化，在匹配预算下与原方法比较。

<a id="paper-154226"></a>

## Finding Interpretable Prompt-Specific Circuits in Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154226) · [作者来源](https://openreview.net/forum?id=FHfc57fnQe)

- **问题 / 瓶颈** · 聚合电路遮蔽提示相关机制
- **核心创新 / 方法** · ACC++ 单次前向提取影响注意力的低维信号
- **Baseline** · 原 ACC 及替换或干预类分析
- **Benchmark** · 多模型间接宾语识别及四语言案例
- **关键结果 / 消融** · 电路按提示聚类，跨语言可复用部件但信号常不同
- **适用条件 / 局限** · 主要证据来自特定语言任务

**可复用机制** · 按提示结构比较注意力通信线路，在匹配预算下与原方法比较。

<a id="paper-150950"></a>

## Finding Koopman Invariant Subspaces via Personalized PageRank

[官方论文页](https://neurips.cc/virtual/2026/poster/150950) · [作者来源](https://openreview.net/forum?id=e6Buij6ykm)

- **问题 / 瓶颈** · 有限字典难保证 Koopman 不变性
- **核心创新 / 方法** · 将 EDMD 零块关联到行归一化图的个性化 PageRank
- **Baseline** · 完整 EDMD 字典及普通 PageRank
- **Benchmark** · Duffing、Van der Pol 和 Lorenz 系统
- **关键结果 / 消融** · 给出样本量平方根倒数级界，实验显示紧凑字典可预测
- **适用条件 / 局限** · 更强结论要求种子在块内且能到达其余观测

**可复用机制** · 按算子泄漏选择小型观测字典，在匹配预算下与原方法比较。

<a id="paper-153132"></a>

## Finding Simple Proofs for First-Order Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/153132) · [作者来源](https://openreview.net/forum?id=NfXX7GR9t7)

- **问题 / 瓶颈** · 自动证书稠密难复用
- **核心创新 / 方法** · 最小化活跃假设并用加权稀疏搜索和半定规划提取中间引理
- **Baseline** · 原始拉格朗日对偶证书
- **Benchmark** · 梯度、近端和快速梯度方法
- **关键结果 / 消融** · 去除冗余不等式，近端示例恢复标准引理
- **适用条件 / 局限** · 依赖可得的证书，不能替代最终验证

**可复用机制** · 对优化收敛证书做稀疏化再人工验证，在匹配预算下与原方法比较。

<a id="paper-138954"></a>

## Fine-Grained Benchmark Generation for Comprehensive Evaluation of Foundation Models

[官方论文页](https://neurips.cc/virtual/2026/poster/138954) · [作者来源](https://openreview.net/forum?id=uAM1JfOl0D)

- **问题 / 瓶颈** · 总分掩盖能力分布与题目答案错误
- **核心创新 / 方法** · 以教材等材料生成题目，以解题图提高答案可靠性
- **Baseline** · MMLU、GSM8K 等既有基准
- **Benchmark** · 机器学习、企业和个人金融，12 个模型及专家审核
- **关键结果 / 消融** · 专家审核发现答案错误较少，并揭示模型间能力差异
- **适用条件 / 局限** · 仍依赖参考材料和专家复核

**可复用机制** · 用参考材料覆盖矩阵与解题图验收新题，在匹配预算下与原方法比较。

<a id="paper-156104"></a>

## FineRMoE: Dimension Expansion for Finer-Grained Expert with an Upcycling Approach

[官方论文页](https://neurips.cc/virtual/2026/poster/156104) · [作者来源](https://openreview.net/forum?id=0MqL9zkDSj)

- **问题 / 瓶颈** · 仅细分中间维度存在收益饱和
- **核心创新 / 方法** · 双维专家设计配合两级稀疏前向和旧模型升级初始化
- **Baseline** · 最强升级训练对照，名称待核
- **Benchmark** · 十项标准基准，比较参数和推理效率
- **关键结果 / 消融** · 作者报告效率与表现改善，幅度待核
- **适用条件 / 局限** · 证据基于升级训练，独立路由代价待核

**可复用机制** · 将专家细分扩展到输出维度，在匹配预算下与原方法比较。

<a id="paper-155221"></a>

## Fine-tuning Does Not Reach All: Uneven Safety and Knowledge Dynamics in Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155221) · [作者来源](https://openreview.net/forum?id=7MsNSkqKWp)

- **问题 / 瓶颈** · 平均安全得分掩盖局部退化
- **核心创新 / 方法** · 用配对样本分别测行为安全和困惑度反映的知识可访问性
- **Baseline** · 不同训练组成和微调阶段
- **Benchmark** · 概念分组的行为与知识评测
- **关键结果 / 消融** · 安全改善不均匀，知识熟悉度不能稳定预测外部行为
- **适用条件 / 局限** · 结论取决于概念覆盖和困惑度代理有效性

**可复用机制** · 安全微调后按知识概念做回归验收，在匹配预算下与原方法比较。

<a id="paper-152334"></a>

## Fine-Tuning Improves Information Conveyance in Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152334) · [作者来源](https://openreview.net/forum?id=TqEugPEDx7)

- **问题 / 瓶颈** · 固定 token 熵忽略不同长度的生成概率
- **核心创新 / 方法** · 用总序列与长度联合熵刻画生成树，并计算长度与熵率的相关性
- **Baseline** · 基础与微调模型
- **Benchmark** · 跨模型和任务的生成熵及语义多样性
- **关键结果 / 消融** · 作者报告控制混杂后熵率与语义多样性的关联接近三倍
- **适用条件 / 局限** · 关联不证明因果，依赖语义多样性测量

**可复用机制** · 把回答长度和内容不确定性一起分析，在匹配预算下与原方法比较。

<a id="paper-153546"></a>

## Fine-tuning language encoding models on slow fMRI improves prediction for fast ECoG

[官方论文页](https://neurips.cc/virtual/2026/poster/153546) · [作者来源](https://openreview.net/forum?id=KZUkyYypaw)

- **问题 / 瓶颈** · 高时间分辨率记录数据有限
- **核心创新 / 方法** · 从语言 fMRI 响应适配表示，再拟合 ECoG 编码模型并对照降采样
- **Baseline** · 原始语言表示及原始分辨率适配
- **Benchmark** · 语言刺激下 fMRI 与 ECoG 响应预测
- **关键结果 / 消融** · 较慢数据提升快信号预测，二倍降采样仍表现相当
- **适用条件 / 局限** · 观察性编码结果，跨人群和任务待核

**可复用机制** · 用低时间分辨率观测训练表示再评估高频数据，在匹配预算下与原方法比较。

<a id="paper-149889"></a>

## Fine-Tuning Language Models to Know What They Know

[官方论文页](https://neurips.cc/virtual/2026/poster/149889) · [作者来源](https://openreview.net/forum?id=mTpoDbfFvY)

- **问题 / 瓶颈** · 置信度可能受到作答偏置影响
- **核心创新 / 方法** · 系统化二类敏感度指标并用进化策略微调元认知
- **Baseline** · 现有度量和微调前模型，具名方法待核
- **Benchmark** · 留出数据、语言及新获得知识
- **关键结果 / 消融** · 作者报告可迁移，并观察到稀疏参数贡献
- **适用条件 / 局限** · 泛化范围和计算成本待核

**可复用机制** · 优先用区分正确与错误的元认知指标验收，在匹配预算下与原方法比较。

<a id="paper-150118"></a>

## Finetuning with Sampling: Make SFT Generalize, Not Forget

[官方论文页](https://neurips.cc/virtual/2026/poster/150118) · [作者来源](https://openreview.net/forum?id=kXgdaUrvBN)

- **问题 / 瓶颈** · 离策略示范信息丰富但可能和当前模型行为差异大
- **核心创新 / 方法** · 以 MCMC 将原轨迹变换到更接近参考模型的分布
- **Baseline** · 原专家数据与在策略对照
- **Benchmark** · 数学推理、事实学习与技能任务
- **关键结果 / 消融** · 作者报告泛化改善且遗忘减少
- **适用条件 / 局限** · 依赖参考模型质量与采样代价

**可复用机制** · 用参考模型重采样专家轨迹再监督微调，在匹配预算下与原方法比较。

<a id="paper-154540"></a>

## FineVLA: Fine-Grained Instruction Alignment for Steerable Vision-Language-Action Policies

[官方论文页](https://neurips.cc/virtual/2026/poster/154540) · [作者来源](https://openreview.net/forum?id=Cq60zqtx7v)

- **问题 / 瓶颈** · 粗目标描述无法表达接触、路径或最终构型
- **核心创新 / 方法** · 清理并时序对齐动作标注，用细粒度描述训练视觉语言动作策略
- **Baseline** · 粗目标描述的策略与理解对照
- **Benchmark** · RoboFine-Bench 问答与描述及 ALOHA 策略实验
- **关键结果 / 消融** · 作者报告细粒度指令控制改善
- **适用条件 / 局限** · 主要策略证据基于 ALOHA，标注误差影响待核

**可复用机制** · 为同一任务目标标注执行方式差异，在匹配预算下与原方法比较。

<a id="paper-153239"></a>

## Finite-Memory Control of POMDPs: Fundamental Limits and Efficient Design

[官方论文页](https://neurips.cc/virtual/2026/poster/153239) · [作者来源](https://openreview.net/forum?id=Mhm8xKoBkY)

- **问题 / 瓶颈** · 信念空间连续，有限控制器无法完整储存
- **核心创新 / 方法** · 用决策见证刻画不可合并的信念，并优化 RECAP 量化码本
- **Baseline** · 同记忆预算的有限表示方法
- **Benchmark** · 11 个 POMDP 基准
- **关键结果 / 消融** · 给出损失下界与码本误差上界，实测优于对照
- **适用条件 / 局限** · 依赖信念空间近似及任务模型

**可复用机制** · 按混淆后产生的决策损失分配记忆状态，在匹配预算下与原方法比较。

<a id="paper-152686"></a>

## FiRe: Fine-grained Multimodal Reasoning for Enhanced Image Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/152686) · [作者来源](https://openreview.net/forum?id=RBlcBaykle)

- **问题 / 瓶颈** · 全图判断与末端奖励难定位未满足属性
- **核心创新 / 方法** · 拆解提示、自评每个属性、局部修订，并用步级奖励和优势更新
- **Baseline** · 标准 GRPO 与基于推理的文生图方法
- **Benchmark** · 文生图及组合属性评测
- **关键结果 / 消融** · 作者报告组合任务提升显著；具体幅度待核
- **适用条件 / 局限** · 依赖可靠的属性判断与局部编辑

**可复用机制** · 对多步生成按中间可检查属性分配奖励

<a id="paper-155698"></a>

## Firefly: Illuminating Verified Real-world Tool Call Data Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/155698) · [作者来源](https://openreview.net/forum?id=3cQkNNBh1Q)

- **问题 / 瓶颈** · 先写任务再求解会产生不可达或难验证的样本
- **核心创新 / 方法** · 由授权工具环境的已知可达结果反向构造任务，并离线重放
- **Baseline** · 先生成任务再求解的合成管线
- **Benchmark** · tau2-Bench 与 BFCL
- **关键结果 / 消融** · 作者报告训练后评测改善，幅度待核
- **适用条件 / 局限** · 依赖受控工具和稳定可重放的响应

**可复用机制** · 从可验证终态反推训练任务，检查可达性与语义一致性

<a id="paper-150161"></a>

## First-Order Trajectory Matching: Fast Ensemble Predictions of Chaotic, Turbulent, Stochastic Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/150161) · [作者来源](https://openreview.net/forum?id=kCo39KbSIa)

- **问题 / 瓶颈** · 集合模型匹配边缘分布却容易漏掉通量
- **核心创新 / 方法** · 以对称局部轨迹位移匹配概率流速度并确定性演化
- **Baseline** · 显式估计漂移、扩散或 score 的建模思路
- **Benchmark** · 随机动力系统及 PDE，考察集合均值和流量
- **关键结果 / 消融** · 作者展示低成本轨迹感知集合预报；给出稳定性分析
- **适用条件 / 局限** · 时间分辨率与样本方差需平衡

**可复用机制** · 从轨迹直接估计概率流，并分开验证边缘分布与通量

<a id="paper-149171"></a>

## First-Token Attraction in Mamba Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/149171) · [作者来源](https://openreview.net/forum?id=sLpGI7l64r)

- **问题 / 瓶颈** · Mamba 的矩阵相互作用使注意力的正性论证难直接应用
- **核心创新 / 方法** · 用高维不变盒和离开时间分析还原有效符号条件
- **Baseline** · 因果注意力与传统时间序列作为机制比较
- **Benchmark** · 理论收敛及 Falcon-Mamba-7B 层间诊断
- **关键结果 / 消融** · 作者证明显式指数收敛，并观察深层向首 token 集中
- **适用条件 / 局限** · 理论适用的序列动力学条件待正文复核

**可复用机制** · 比较层间方向与首位置贡献，检测状态空间模型的汇聚

<a id="paper-151066"></a>

## Fisher Decorator: Refining Flow Policy via  A Local Transport Map

[官方论文页](https://neurips.cc/virtual/2026/poster/151066) · [作者来源](https://openreview.net/forum?id=dDvDTFE06y)

- **问题 / 瓶颈** · 各向同性动作惩罚忽略行为密度与流形方向
- **核心创新 / 方法** · 给初始流策略加局部残差映射，以 Fisher 矩阵近似 KL 约束
- **Baseline** · 基于 L2 或 Wasserstein 上界的流策略
- **Benchmark** · 多个离线强化学习基准及局部近似理论
- **关键结果 / 消融** · 作者报告表现改善，并刻画局部近似误差
- **适用条件 / 局限** · 保证限于局部邻域及估计可靠时

**可复用机制** · 离线策略精修按行为密度方向约束残差

<a id="paper-152494"></a>

## Fisher-R1: Training LLM Agents for Reliable Hypothesis Testing

[官方论文页](https://neurips.cc/virtual/2026/poster/152494) · [作者来源](https://openreview.net/forum?id=ShMNgympCf)

- **问题 / 瓶颈** · 代码正确执行仍可能产生无效统计结论
- **核心创新 / 方法** · 独立核对检验选择、假设与结论，用可验证奖励训练
- **Baseline** · 原骨干及 GPT-5.4、DeepSeek-V4-Pro
- **Benchmark** · P-Bench 425 道开放检验任务，以单次成功率评估
- **关键结果 / 消融** · 作者报告较 DeepSeek-V4-Pro 平均相对提高 21%
- **适用条件 / 局限** · 适用结论取决于数据生成假设和评分覆盖

**可复用机制** · 把统计有效性作为独立验收项，避免只检查执行

<a id="paper-155218"></a>

## Fixed-Point Masked Generative Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/155218) · [作者来源](https://openreview.net/forum?id=7Ox69QdIwT)

- **问题 / 瓶颈** · 每步固定深度的掩码生成成本高
- **核心创新 / 方法** · 共享层做不动点求解，跨步一致性配合三种 token 状态的热启动
- **Baseline** · MDLM 及固定深度掩码生成模型
- **Benchmark** · OpenWebText 困惑度、ImageNette FID 与资源成本
- **关键结果 / 消融** · 固定 96 次块前向算力下困惑度 830.8 降至 101.8
- **适用条件 / 局限** · 依赖不动点收敛及原解可迁移

**可复用机制** · 按变化状态复用上一步隐变量，与冷启动对照

<a id="paper-148540"></a>

## Fixed-Point Reasoning: Stable and Adaptive Deep Looped Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148540) · [作者来源](https://openreview.net/forum?id=x9VEF8HRwV)

- **问题 / 瓶颈** · 循环层延后停止时易出现信号传播问题
- **核心创新 / 方法** · 预归一化与残差缩放配合定点收敛停机
- **Baseline** · 具体对照待核查
- **Benchmark** · 数独、迷宫、状态跟踪
- **关键结果 / 消融** · 作者报告计算量可随难度调整
- **适用条件 / 局限** · 收敛阈值和最大深度仍需核查

**可复用机制** · 以状态收敛决定循环深度，采用同预算对照核验其收益。

<a id="paper-153159"></a>

## Fixed-Size Active Statistical Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/153159) · [作者来源](https://openreview.net/forum?id=NRmXsCr462)

- **问题 / 瓶颈** · 独立抽样使样本数随机并增加估计方差
- **核心创新 / 方法** · 将泊松抽样条件化到固定样本数，用于多元 Z 估计
- **Baseline** · 独立泊松抽样
- **Benchmark** · 理论渐近方差与模拟、真实数据
- **关键结果 / 消融** · 作者证明渐近方差不高于对照
- **适用条件 / 局限** · 有限样本收益需查实

**可复用机制** · 固定标注预算时比较条件泊松抽样，采用同预算对照核验其收益。

<a id="paper-149666"></a>

## Fixed Universal Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/149666) · [作者来源](https://openreview.net/forum?id=oLOTrZMfSu)

- **问题 / 瓶颈** · 模型权重固定后能模拟哪些模型仍不清楚
- **核心创新 / 方法** · 以输入嵌入编码目标 Transformer，并构造稀疏通用架构
- **Baseline** · 与既有随机 Transformer 经验结果比较
- **Benchmark** · 括号平衡与多跳推理
- **关键结果 / 消融** · 在所设类别和足够维度下可构造通用模型，随机初始化几乎处处具有通用性
- **适用条件 / 局限** · 要求特定编码和足够嵌入维度

**可复用机制** · 比较权重适配与输入编码的表达能力，采用同预算对照核验其收益。

<a id="paper-152205"></a>

## Fix the Structural Bottleneck: Context Compression via Explicit Information Transmission

[官方论文页](https://neurips.cc/virtual/2026/poster/152205) · [作者来源](https://openreview.net/forum?id=UmwQ35aBP0)

- **问题 / 瓶颈** · 压缩 token 协调有限且跨层信号稀释
- **核心创新 / 方法** · 从冻结骨干跨层选特征，再以运输计划分配信息至压缩槽位
- **Baseline** · 软压缩方法及完整上下文
- **Benchmark** · 12 个数据集的 F1 和压缩速度
- **关键结果 / 消融** · 摘要报告平均 F1 最多提高 18.5%，较最快对照快两倍以上
- **适用条件 / 局限** · 具体任务和资源口径待核查

**可复用机制** · 用全局槽位分配替代逐槽独立聚合，采用同预算对照核验其收益。

<a id="paper-151542"></a>

## FLAG: Flow Policy MaxEnt-RL by Latent Augmented Guidance

[官方论文页](https://neurips.cc/virtual/2026/poster/151542) · [作者来源](https://openreview.net/forum?id=ZuIBJ5uEay)

- **问题 / 瓶颈** · 全动作空间采样容易导致权重集中
- **核心创新 / 方法** · 以流潜变量扩展状态并优化一致的最大熵代理目标
- **Baseline** · 生成策略的全空间重要性采样方法
- **Benchmark** · 高维控制与受限采样设定
- **关键结果 / 消融** · 作者报告有限样本下仍能优化表达性策略
- **适用条件 / 局限** · 理论一致性假设与具体控制基准待查

**可复用机制** · 高维动作策略使用局部采样减缓重要性权重退化，采用同预算对照核验其收益。

<a id="paper-139338"></a>

## FLARE: Full-Modality Long-Video Audiovisual Retrieval Benchmark with User-Simulated Queries

[官方论文页](https://neurips.cc/virtual/2026/poster/139338) · [作者来源](https://openreview.net/forum?id=VwiAEEv0xh)

- **问题 / 瓶颈** · 短片描述匹配可能高估真实长视频检索
- **核心创新 / 方法** · 构造用户式查询并逐模态检验跨模态样例
- **Baseline** · 15 种检索器，含音频、视觉和双模态设定
- **Benchmark** · 399 个长视频，比较描述检索与查询检索
- **关键结果 / 消融** · 作者发现描述任务表现不一定迁移至用户查询
- **适用条件 / 局限** · 由何种模型定义单模态失败需查实

**可复用机制** · 以单模态失败、双模态成功筛选联合检索样例，采用同预算对照核验其收益。

<a id="paper-149137"></a>

## FLARE: Verifying MILP Reformulations with LLM-Based Formal Proof Synthesis

[官方论文页](https://neurips.cc/virtual/2026/poster/149137) · [作者来源](https://openreview.net/forum?id=sZLQvatATh)

- **问题 / 瓶颈** · 数值样例一致无法证明所有实例等价
- **核心创新 / 方法** · 将构造性重写形式化，由语言模型生成 Lean 可检查的证明
- **Baseline** · 现有比较法及非形式化 FLARE-NL
- **Benchmark** · FormulationBench 的 20 个问题和 116 个表述
- **关键结果 / 消融** · 摘要报告 FLARE 96.9%，非形式代理 99.3%
- **适用条件 / 局限** · 代理准确率与形式保证不同，证明覆盖边界待查

**可复用机制** · 给整数规划重写加入可核验的等价证明，采用同预算对照核验其收益。

<a id="paper-150295"></a>

## FlashBoB: I/O-Efficient Exact Backward-over-Backward for Softmax Attention

[官方论文页](https://neurips.cc/virtual/2026/poster/150295) · [作者来源](https://openreview.net/forum?id=jDTHY0c03X)

- **问题 / 瓶颈** · 显式注意力中间张量限制长序列高阶微分
- **核心创新 / 方法** · 利用二阶软最大反传仿射结构，以两个行标量组织两遍分块计算
- **Baseline** · 显式中间张量实现及标准重算模型
- **Benchmark** · 软最大注意力二阶反传的访存分析
- **关键结果 / 消融** · 无需物化平方规模张量，在指定重算模型匹配大缓存下界
- **适用条件 / 局限** · 结论依赖所用访存模型和硬件缓存

**可复用机制** · 以逐行充分量设计注意力二阶反传内核，采用同预算对照核验其收益。

<a id="paper-152191"></a>

## Flash-dLLM: IO-Aware KV Caching and Parallel Decoding for Fast, Memory-Efficient Diffusion LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/152191) · [作者来源](https://openreview.net/forum?id=UsksaoFwxx)

- **问题 / 瓶颈** · 独立优化缓存和并行验证会漏掉显存访存瓶颈
- **核心创新 / 方法** · 融合 KV 缓存内核，使用同一扩散模型提出并验证候选
- **Baseline** · 独立缓存或解码加速方法，具名对照待查
- **Benchmark** · 长序列扩散语言模型生成
- **关键结果 / 消融** · 作者报告推理加速并保持生成质量
- **适用条件 / 局限** · 实际收益依赖带宽与可复用缓存比例

**可复用机制** · 联合设计扩散解码缓存和候选验证，采用同预算对照核验其收益。

<a id="paper-153691"></a>

## FLASH: Efficient Visuomotor Policy via Sparse Sampling

[官方论文页](https://neurips.cc/virtual/2026/poster/153691) · [作者来源](https://openreview.net/forum?id=JViY8zwERh)

- **问题 / 瓶颈** · 离散动作逐步去噪难满足实时控制
- **核心创新 / 方法** · 稀疏拟合 Legendre 轨迹，从历史系数启动流，并解析求速度前馈
- **Baseline** · 扩散策略和既有流匹配策略
- **Benchmark** · 五项仿真与两项真实操作任务
- **关键结果 / 消融** · 摘要报告各任务成功率至少 92%，每回合推理 31.40 毫秒
- **适用条件 / 局限** · 高频动作及突变接触可能难用稀疏多项式表示

**可复用机制** · 用连续多项式表示动作并从历史系数启动生成，采用同预算对照核验其收益。

<a id="paper-150533"></a>

## FlashEvolve: Accelerating Agent Self-Evolution with Asynchronous Stage Orchestration

[官方论文页](https://neurips.cc/virtual/2026/poster/150533) · [作者来源](https://openreview.net/forum?id=hQqV68QK4q)

- **问题 / 瓶颈** · 同步生成和评估导致阶段间等待
- **核心创新 / 方法** · 用异步队列重叠工作，并按版本更新、丢弃或修补过期产物
- **Baseline** · 同步 GEPA
- **Benchmark** · 本地 vLLM 和 API 的 GEPA 任务
- **关键结果 / 消融** · 作者报告提案吞吐分别为 3.5 倍和 4.9 倍
- **适用条件 / 局限** · 提案吞吐不直接等于达到同等质量的总时长

**可复用机制** · 按版本处理过期的提示或工作流产物，采用同预算对照核验其收益。

<a id="paper-151360"></a>

## FlashFFN: Multi-Head Decomposition Enables I/O-Aware Feed-Forward Network

[官方论文页](https://neurips.cc/virtual/2026/poster/151360) · [作者来源](https://openreview.net/forum?id=b8w3ugs7jR)

- **问题 / 瓶颈** · 融合单遍 FFN 需存整宽输出累加器
- **核心创新 / 方法** · 分头降低累加宽度，并用子网络修正单头扩展比
- **Baseline** · 匹配参数量的 SwiGLU
- **Benchmark** · 片上空间可行性与模型比较
- **关键结果 / 消融** · 作者报告构造可在片上实现所设融合调度
- **适用条件 / 局限** · 可行性受硬件与分块设定影响

**可复用机制** · 以片上累加空间约束设计 FFN 的分头宽度，采用同预算对照核验其收益。

<a id="paper-151963"></a>

## Flash-KMeans: Fast and Memory-Efficient Exact K-Means

[官方论文页](https://neurips.cc/virtual/2026/poster/151963) · [作者来源](https://openreview.net/forum?id=WVswOFOoe5)

- **问题 / 瓶颈** · 显式距离矩阵耗带宽，原子散写压低质心更新效率
- **核心创新 / 方法** · 在线维护最近中心，排序建立逆映射后做聚合
- **Baseline** · 现有 GPU K-means 实现
- **Benchmark** · GPU 上的精确 K-means 聚类
- **关键结果 / 消融** · 设计节省距离矩阵存储与高争用更新开销
- **适用条件 / 局限** · 排序与融合收益依赖簇数及样本分布

**可复用机制** · 融合距离与在线最小值，并用逆映射消除更新争用，采用同预算对照核验其收益。

<a id="paper-148370"></a>

## FlashMask-3: Efficient and Expressive Mask-Aware Distributed Attention

[官方论文页](https://neurips.cc/virtual/2026/poster/148370) · [作者来源](https://openreview.net/forum?id=yNPYdsVguR)

- **问题 / 瓶颈** · 复杂长序列掩码在多节点训练中引入瓶颈
- **核心创新 / 方法** · 对列式掩码边界做裁剪、平移及取最大值，结合 Hopper 内核和稀疏负载均衡
- **Baseline** · FlashMask 及 FlashAttention-3
- **Benchmark** · 结构掩码下的多节点上下文并行
- **关键结果 / 消融** · 作者证明掩码本地化无需通信
- **适用条件 / 局限** · 适用范围受列式区间可表达性和硬件约束

**可复用机制** · 用键索引的边界向量在本地裁剪结构掩码，采用同预算对照核验其收益。

<a id="paper-153142"></a>

## Flash PD-SSM: Memory-Optimized Structured Sparse State-Space Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153142) · [作者来源](https://openreview.net/forum?id=NZX4ku8S86)

- **问题 / 瓶颈** · 稠密转移昂贵，固定结构则限制状态跟踪。
- **核心创新 / 方法** · 逐时间步从结构化稀疏矩阵库选一个转移，在保持稀疏运算时表达有限状态机。
- **Baseline** · 对角与其他状态空间模型。
- **Benchmark** · 合成与机制状态跟踪、长度超过 17,000 的时序任务和混合语言模型。
- **关键结果 / 消融** · 作者报告较强状态跟踪和长序列表现，吞吐提高、内存下降。
- **适用条件 / 局限** · 实际收益依赖内核、矩阵库及序列长度。

**可复用机制** · 固定训练预算对照单一转移、条件转移与稠密转移。

<a id="paper-151391"></a>

## FlashPlanner: Real-Time Goal-Conditioned Flow-Matching Planning for Autonomous Driving with Online RL Fine-Tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/151391) · [作者来源](https://openreview.net/forum?id=aztITR34On)

- **问题 / 瓶颈** · 模仿拟合与闭环表现不一致，多步生成占用延迟预算。
- **核心创新 / 方法** · 预训练目标点预测器，再用候选目标的闭环反馈进行 RL 微调，配合数据预测式流匹配规划器。
- **Baseline** · 先前生成式规划器，具体配置待核。
- **Benchmark** · nuPlan、interPlan 闭环和推理吞吐。
- **关键结果 / 消融** · 作者报告 166 FPS，对照 28 FPS，闭环规划表现改善。
- **适用条件 / 局限** · 硬件、采样次数及实际道路验证待核。

**可复用机制** · 把高层目标与轨迹采样分开测量，检验闭环收益来自哪一层。

<a id="paper-151863"></a>

## Flash-SD-KDE: Accelerating SD-KDE with Tensor Cores

[官方论文页](https://neurips.cc/virtual/2026/poster/151863) · [作者来源](https://openreview.net/forum?id=XKQaXj5Qol)

- **问题 / 瓶颈** · 得分去偏改善渐近速率但原实现开销较大。
- **核心创新 / 方法** · 重排算子以暴露矩阵乘结构并调用 Tensor Cores。
- **Baseline** · 已有 SD-KDE GPU 实现和 scikit-learn KDE。
- **Benchmark** · 16 维、32K 样本及 100 万样本两种规模的耗时。
- **关键结果 / 消融** · 小规模较 GPU 对照最高 47 倍；大规模处理 131K 查询用 2.3 秒。
- **适用条件 / 局限** · CPU 与 GPU 加速比不可等同，硬件和精度设置待核。

**可复用机制** · 对核方法分别测估计误差、同硬件加速和规模曲线。

<a id="paper-149335"></a>

## FlashSSM-3D: A Distilled State Space Model for Lightning-Fast Dense 3D Reconstruction

[官方论文页](https://neurips.cc/virtual/2026/poster/149335) · [作者来源](https://openreview.net/forum?id=qrND6erSwi)

- **问题 / 瓶颈** · 常规蒸馏难保多视角空间结构，从头训练开销高。
- **核心创新 / 方法** · 用 VGGT 教师训练无注意力 SSM，加入 Procrustes 对齐与相机重投影损失。
- **Baseline** · VGGT 教师和常规蒸馏思路。
- **Benchmark** · 多视角重建与相机姿态估计。
- **关键结果 / 消融** · 作者报告用约 25% 数据、不到 10% 训练计算，500 多视角低于 10 秒。
- **适用条件 / 局限** · 依赖教师几何正确性，速度测试硬件待核。

**可复用机制** · 对齐坐标自由度后比较特征蒸馏与结构监督。

<a id="paper-154501"></a>

## Flexformer: Flexible Linear Transformer with Learnable Attention Kernel

[官方论文页](https://neurips.cc/virtual/2026/poster/154501) · [作者来源](https://openreview.net/forum?id=D8frDvzgAf)

- **问题 / 瓶颈** · 固定核虽高效，但可能不适合不同数据的依赖结构。
- **核心创新 / 方法** · 将随机 Fourier 特征频率设为参数，并比较平稳和非平稳核。
- **Baseline** · 固定或弱可学习核及预训练 Transformer 教师。
- **Benchmark** · 语言建模、序列分类与长序列任务。
- **关键结果 / 消融** · 作者报告优于对照、可蒸馏近似 softmax，并显示核跨域迁移能力。
- **适用条件 / 局限** · 核特征数与计算质量取舍待核。

**可复用机制** · 在相同线性复杂度约束下，隔离固定频率和可训练频率的差异。

<a id="paper-139473"></a>

## Flexible Intensities Matter: A comprehensive re-evaluation of Classical and Neural Temporal Point Processes

[官方论文页](https://neurips.cc/virtual/2026/poster/139473) · [作者来源](https://openreview.net/forum?id=NoBHtWYMBB)

- **问题 / 瓶颈** · 弱形式的 Hawkes 对照可能夸大神经模型收益。
- **核心创新 / 方法** · 统一比较可学习 Hawkes 核、先前神经强度和 Transformer 样条强度头。
- **Baseline** · 经典与神经时序点过程。
- **Benchmark** · 既有事件数据、UK Biobank 疾病历史与 MIMIC-IV ICU 记录。
- **关键结果 / 消融** · 灵活 Hawkes 大体缩小差距；MIMIC-IV 中发现超出成对核解释的结构。
- **适用条件 / 局限** · 观察性数据证据不能直接识别因果机制。

**可复用机制** · 先升级经典基线的参数化，再判断新骨干是否必要。

<a id="paper-149927"></a>

## Flexible Routing via Uncertainty Decomposition

[官方论文页](https://neurips.cc/virtual/2026/poster/149927) · [作者来源](https://openreview.net/forum?id=m7fOVAfEEw)

- **问题 / 瓶颈** · 仅按总不确定性路由会浪费专家调用。
- **核心创新 / 方法** · 通过多标注观测估计可约与不可约不确定性，选择直接预测、升级或弃答。
- **Baseline** · 任务专用最优路由及实验对照，名称待核。
- **Benchmark** · 合成及真实分类，比较成本与性能并分析遗憾。
- **关键结果 / 消融** · 作者发现两类不确定性相关较弱时收益更明确。
- **适用条件 / 局限** · 需每个输入有多个独立标注。

**可复用机制** · 给专家升级与拒答分开设阈值并按成本比较。

<a id="paper-151034"></a>

## FlexMoE: One-for-All Nested Intra-Expert Pruning for MoE Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151034) · [作者来源](https://openreview.net/forum?id=dTCZtqedSq)

- **问题 / 瓶颈** · 稀疏激活仍需存储全部专家，单预算方案难复用。
- **核心创新 / 方法** · 专家通道排序后逐步提高剪枝成本压力，导出嵌套掩码并在中等预算恢复微调。
- **Baseline** · 近期 MoE 压缩方法及原模型。
- **Benchmark** · Qwen2-57B-A14B 等设置，模型表现、内存和在线吞吐。
- **关键结果 / 消融** · 作者报告不微调时剪掉 50% 路由专家参数仍保留约 99.8% 基线表现。
- **适用条件 / 局限** · 需共享通道排序与配套内核，跨底座待核。

**可复用机制** · 在同一模型中检验中预算恢复能否迁移到未见预算。

<a id="paper-149594"></a>

## FLINT: Coupling Proximal Initialization and Bounded Stochasticity for Flow-Matching Inverse Problems

[官方论文页](https://neurips.cc/virtual/2026/poster/149594) · [作者来源](https://openreview.net/forum?id=ovYQsp14kD)

- **问题 / 瓶颈** · 初始化改善可能被随后采样噪声抵消。
- **核心创新 / 方法** · 通过恢复误差上界连接两者，先近端优化源，再使用有界随机性做引导采样。
- **Baseline** · 随机初始化轨迹方法与源空间优化方法。
- **Benchmark** · 多类图像逆问题，感知质量、失真与耗时。
- **关键结果 / 消融** · 作者报告少量初始化迭代即可获得较佳感知表现，失真具竞争力。
- **适用条件 / 局限** · 依赖先验和测量算子，噪声预算迁移待核。

**可复用机制** · 初始化策略与后续噪声做正交消融，测收益何时被抹去。

<a id="paper-152411"></a>

## FLIP: Fast and Accurate Global Lipschitz Estimation for Large Feedforward Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/152411) · [作者来源](https://openreview.net/forum?id=TJXYYcODy8)

- **问题 / 瓶颈** · 大前馈网络的 Lipschitz 估计常耗时或偏松。
- **核心创新 / 方法** · 改写 SDP，逆向传播目标上下界，用割线迭代解局部子问题。
- **Baseline** · 既有全局 Lipschitz 估计方法。
- **Benchmark** · 随机与训练后的前馈网络，比较紧度和运行时间。
- **关键结果 / 消融** · 作者报告大规模网络上改进，1 亿参数网络约 3 秒。
- **适用条件 / 局限** · 适用网络结构、硬件与数值误差待核。

**可复用机制** · 评估稳健性证书时在同一硬件并报界的紧度与耗时。

<a id="paper-150844"></a>

## Flipping Bits, Not Gradients: Sharpness-Aware Minimization Directly on the Boolean Hypercube

[官方论文页](https://neurips.cc/virtual/2026/poster/150844) · [作者来源](https://openreview.net/forum?id=evBaB8ZWOV)

- **问题 / 瓶颈** · 潜连续权重扰动无法忠实探测二值损失邻域。
- **核心创新 / 方法** · 在有限位翻转邻域做贪心内层上升和锐度感知外层更新。
- **Baseline** · 标准二值训练与潜空间 SAM。
- **Benchmark** · 多个网络架构与数据集，测准确率和分布外鲁棒性。
- **关键结果 / 消融** · 作者给出以离散交互 Hessian 刻画的近似和收敛论证，报告实际增益。
- **适用条件 / 局限** · 预算与离散交互强度影响贪心效果。

**可复用机制** · 离散优化时把扰动定义在真实变量空间，并与连续代理对照。

<a id="paper-149413"></a>

## FLoRA-Chef: Making A Good LoRA Recipe in Federated Generalization

[官方论文页](https://neurips.cc/virtual/2026/poster/149413) · [作者来源](https://openreview.net/forum?id=qDbRHtLtST)

- **问题 / 瓶颈** · 异质客户端的因子更新不一致，直接聚合可能引入噪声。
- **核心创新 / 方法** · 追踪跨客户端更新离散度以选择聚合目标，并对矩阵分别重加权。
- **Baseline** · 直接聚合与既有联邦 LoRA 方法。
- **Benchmark** · 多种联邦异质设置下的全局泛化。
- **关键结果 / 消融** · 作者报告平均提升 6.94%，指标口径待核。
- **适用条件 / 局限** · 离散度依赖参与客户端和数据异质结构。

**可复用机制** · 比较因子对称和非对称聚合，单报聚合偏差。

<a id="paper-148653"></a>

## Flow Annealing Posterior Sampling for Function-Space Regression and Inverse Problems

[官方论文页](https://neurips.cc/virtual/2026/poster/148653) · [作者来源](https://openreview.net/forum?id=w8ebg6EwVu)

- **问题 / 瓶颈** · 固定网格方法难复用，先验密度计算可能不可行。
- **核心创新 / 方法** · 用预训函数空间流匹配和观测似然引导，借低秩协方差预条件做 Langevin 校正。
- **Baseline** · 函数回归和逆问题方法，具名对照待核。
- **Benchmark** · 高斯与非高斯过程回归及 PDE 逆问题。
- **关键结果 / 消融** · 作者报告后验连贯、校准与精度优于对照。
- **适用条件 / 局限** · 低秩近似对弱方差方向的影响待核。

**可复用机制** · 在不同观测与查询网格上共同测试后验校准和误差。

<a id="paper-153098"></a>

## FlowBank: Query-Adaptive Agentic Workflows Optimization through Precompute-and-Reuse

[官方论文页](https://neurips.cc/virtual/2026/poster/153098) · [作者来源](https://openreview.net/forum?id=Nx2TulAMl6)

- **问题 / 瓶颈** · 单流程覆盖有限，每个查询生成流程成本高。
- **核心创新 / 方法** · 搜索优先覆盖少见查询，去掉冗余流程，再估计查询与流程配对效用。
- **Baseline** · 自动搜索与手工工作流对照。
- **Benchmark** · 五项任务成功指标及推理开销，具名基准待核。
- **关键结果 / 消融** · 作者报告平均分较最强自动和手工对照分别相对增 4.26% 和 14.92%。
- **适用条件 / 局限** · 流程库覆盖有限，效用预测对分布偏移敏感。

**可复用机制** · 在固定在线预算下比较单流程、互补流程库和逐例生成。

<a id="paper-153168"></a>

## Flow-Based Conformal Predictive Distributions

[官方论文页](https://neurips.cc/virtual/2026/poster/153168) · [作者来源](https://openreview.net/forum?id=NLkjvjTgni)

- **问题 / 瓶颈** · 高维预测集合难表示。
- **核心创新 / 方法** · 以不符合度梯度流抵达集合边界，再混合多个置信水平。
- **Baseline** · 集合式共形预测。
- **Benchmark** · 偏微分方程反演、降水降尺度、气候去偏和飓风轨迹。
- **关键结果 / 消融** · 给出分解误差来源的界。
- **适用条件 / 局限** · 要求分数可微且足够正则。

**可复用机制** · 判断误差来自分数、基分布还是数值流。

<a id="paper-151466"></a>

## Flow-based Spectral Kernel Learning for Nonstationary Attention

[官方论文页](https://neurips.cc/virtual/2026/poster/151466) · [作者来源](https://openreview.net/forum?id=aP71hsUN95)

- **问题 / 瓶颈** · 平稳核难适应复杂 token 交互。
- **核心创新 / 方法** · 以归一化流学习双变量谱密度，去除查询键投影并固定正交值投影。
- **Baseline** · 既有注意力机制。
- **Benchmark** · 分类、消融和规模测试。
- **关键结果 / 消融** · 投影相关参数少约 40%–47%，保持线性内存伸缩。
- **适用条件 / 局限** · 整体参数与真实吞吐待核。

**可复用机制** · 固定计算预算比较适应性核与额外投影。

<a id="paper-148446"></a>

## Flow-Corrected Shape Optimization: Taming Manifold Drift in High-Dimensional 3D Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148446) · [作者来源](https://openreview.net/forum?id=xkGjQXY3TJ)

- **问题 / 瓶颈** · 高维潜空间中的梯度易离开有效形状区域。
- **核心创新 / 方法** · 交替做目标梯度更新与引导流匹配校正。
- **Baseline** · 潜空间正则及既有流匹配方法。
- **Benchmark** · 多种生成先验及形状优化任务。
- **关键结果 / 消融** · 作者报告兼顾形状有效性和目标可优化性。
- **适用条件 / 局限** · 量化收益与校正成本待核。

**可复用机制** · 分别追踪潜状态有效性和目标下降，检查校正频率取舍。

<a id="paper-152468"></a>

## Flow+Diff: Unifying Flow and Diffusion Representations for Multivariate Time Series Anomaly Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/152468) · [作者来源](https://openreview.net/forum?id=SsSjmffHDW)

- **问题 / 瓶颈** · 少数变量的微小异常易被均值掩盖。
- **核心创新 / 方法** · 比较可逆流编码和扩散模型去噪得到的正常潜表示。
- **Baseline** · 重建式异常检测及竞争方法。
- **Benchmark** · 六个多变量数据集。
- **关键结果 / 消融** · 四个数据集表现最佳。
- **适用条件 / 局限** · 基准名称和异常阈值待核。

**可复用机制** · 按异常涉及的变量比例对照潜空间分歧与重建误差。

<a id="paper-151143"></a>

## Flow-Direct: Feedback-Efficient and Reusable Guidance for Flow Models via Non-Parametric Guidance Field

[官方论文页](https://neurips.cc/virtual/2026/poster/151143) · [作者来源](https://openreview.net/forum?id=chIrbGRrfT)

- **问题 / 瓶颈** · 局部搜索会丢弃已付费的反馈。
- **核心创新 / 方法** · 从奖励加权分布密度比推导场，以历史样本做非参数估计。
- **Baseline** · 局部梯度近似及离散搜索。
- **Benchmark** · 具体应用基准待核。
- **关键结果 / 消融** · 作者提出可在复用时无需新增奖励评估，并可组合多个场。
- **适用条件 / 局限** · 估计精度依赖样本对目标区域的覆盖。

**可复用机制** · 预算固定时比较缓存全历史与仅用最新样本。

<a id="paper-150977"></a>

## Flow-DPPO: Divergence Proximal Policy Optimization for Flow Matching Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150977) · [作者来源](https://openreview.net/forum?id=drpFiVnG8v)

- **问题 / 瓶颈** · 比率估计噪声使约束强度不均。
- **核心创新 / 方法** · 精确计算步级 KL，仅屏蔽越阈且进一步偏离的更新。
- **Baseline** · Flow-GRPO、CPS 等 PPO 式方法。
- **Benchmark** · 图像和视频生成的在线后训练。
- **关键结果 / 消融** · 作者报告多轮更新更稳并缓解遗忘。
- **适用条件 / 局限** · 依赖高斯步级策略，具名评测待核。

**可复用机制** · 在相同步级 KL 预算下比较剪切与精确约束。

<a id="paper-149264"></a>

## Flow Equivariant State Space Model

[官方论文页](https://neurips.cc/virtual/2026/poster/149264) · [作者来源](https://openreview.net/forum?id=rbe5gNhR4J)

- **问题 / 瓶颈** · 固定坐标累积会混淆移动对象证据。
- **核心创新 / 方法** · 用候选流分支承载状态，构建粗细两层以上的记忆体系。
- **Baseline** · 固定坐标的选择性状态空间模型。
- **Benchmark** · Moving 和 Rotating MNIST、KTH、SEVIR。
- **关键结果 / 消融** · 报告变换跟踪及复杂天气预测中的多尺度收益。
- **适用条件 / 局限** · 复杂形变下的成本和误差待核。

**可复用机制** · 对有平移和局部形变的序列，分开消融记忆输送和尺度层级。

<a id="paper-155765"></a>

## FlowHOI: Flow-based Semantics-Grounded Generation of Hand-Object Interactions for Dexterous Robot Manipulation

[官方论文页](https://neurips.cc/virtual/2026/poster/155765) · [作者来源](https://openreview.net/forum?id=35aGAAx7tn)

- **问题 / 瓶颈** · 仅规划末端运动难保持连续接触。
- **核心创新 / 方法** · 分开生成几何抓握和语义操作，以场景 token 和动作文本监督约束。
- **Baseline** · 扩散式手物交互基线。
- **Benchmark** · GRAB、HOT3D 和四项实体机器人操作。
- **关键结果 / 消融** · GRAB 仿真成功率为最强扩散对照的 1.7 倍，推理快 40 倍。
- **适用条件 / 局限** · 性能依赖场景重建及重定向。

**可复用机制** · 以接触序列为动作接口，分别测物理可行性和语言一致性。

<a id="paper-154398"></a>

## Flow Map Denoisers: Traversing the Distortion-Perception Plane for Inverse Problems

[官方论文页](https://neurips.cc/virtual/2026/poster/154398) · [作者来源](https://openreview.net/forum?id=Ds12ClkyRZ)

- **问题 / 瓶颈** · 固定去噪器只覆盖一个折衷点。
- **核心创新 / 方法** · 将流映射的不同未来时间嵌入同一即插即用求解器。
- **Baseline** · 两端的专用复原模型。
- **Benchmark** · CelebA、AFHQ 上的线性和非线性逆问题。
- **关键结果 / 消融** · 高斯情况下精确恢复最优前沿，自然图像上近似成立。
- **适用条件 / 局限** · 自然图像结论为实证。

**可复用机制** · 扫展望时间并绘制完整失真与感知曲线。

<a id="paper-152052"></a>

## Flow Map Language Models: One-step Language Modeling via Continuous Denoising

[官方论文页](https://neurips.cc/virtual/2026/poster/152052) · [作者来源](https://openreview.net/forum?id=VqiKJfJ98m)

- **问题 / 瓶颈** · 离散扩散在少步生成时质量下降。
- **核心创新 / 方法** · 对 one-hot 单纯形建模，以交叉熵学习流和映射并对照三种蒸馏方式。
- **Baseline** · 离散扩散模型。
- **Benchmark** · LM1B、OpenWebText。
- **关键结果 / 消融** · 报告一步生成超过近期离散少步模型的八步质量。
- **适用条件 / 局限** · 长文本和规模外推待核。

**可复用机制** · 在固定数据下比较采样步数与质量曲线。

<a id="paper-153771"></a>

## Flow Matching for Offline Reinforcement Learning with Discrete Actions

[官方论文页](https://neurips.cc/virtual/2026/poster/153771) · [作者来源](https://openreview.net/forum?id=ImlV9V1zY1)

- **问题 / 瓶颈** · 连续速度场不能直接表达动作类别。
- **核心创新 / 方法** · 以连续时间马尔可夫链替代连续流，用 Q 加权目标及因子化联合动作路径。
- **Baseline** · 传统离线强化学习方法。
- **Benchmark** · 高维控制、多智能体游戏及动态偏好。
- **关键结果 / 消融** · 作者报告效果优于传统方法，理想条件下恢复最优策略。
- **适用条件 / 局限** · 联合动作依赖和量化误差需单测。

**可复用机制** · 比较离散生成和因子化对协同决策的影响。

<a id="paper-148142"></a>

## Flow Matching Policy Optimization with Mirror Descent and Entropy Constraints

[官方论文页](https://neurips.cc/virtual/2026/poster/148142) · [作者来源](https://openreview.net/forum?id=zxpb2T9sJT)

- **问题 / 瓶颈** · 随机去噪的熵难算，经求解器反传昂贵。
- **核心创新 / 方法** · 使用优势加权条件流匹配，按 tanh 修正熵并依据有效样本量调节温度。
- **Baseline** · 标准连续控制强化学习方法，具名实现待核。
- **Benchmark** · 稀疏奖励 FrankaKitchen 和稠密奖励 MuJoCo。
- **关键结果 / 消融** · 前者表现更好，后者保持竞争力。
- **适用条件 / 局限** · 有界动作变换和熵估计的适用条件待核。

**可复用机制** · 对照无需求解器反传的更新及其探索效率。

<a id="paper-153016"></a>

## Flow Matching Reinforcement Learning via SDE Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/153016) · [作者来源](https://openreview.net/forum?id=ObfkKSqYkf)

- **问题 / 瓶颈** · 确定性生成限制训练探索，随机训练的收益未必能迁移。
- **核心创新 / 方法** · 用扩散与流对偶构造训练 SDE 和部署 ODE，并分析性能转移。
- **Baseline** · 既有流强化学习可作为框架特例。
- **Benchmark** · 理论及实证验证，具名任务待核。
- **关键结果 / 消融** · 在预训练模型足够准确时给出接近性与改进转移保证。
- **适用条件 / 局限** · 保证依赖预训练质量和动态接近性。

**可复用机制** · 分别测试训练随机策略和部署确定策略的回报差距。

<a id="paper-148833"></a>

## Flow Mismatching: Unsupervised Anomaly Detection via Velocity Discrepancies in Flow Matching Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148833) · [作者来源](https://openreview.net/forum?id=uo8TtP3G5g)

- **问题 / 瓶颈** · 异常也可能被重建模型复原。
- **核心创新 / 方法** · 沿噪声到图像的路径比较模型速度和路径速度，并跨时间聚合差异。
- **Baseline** · 重建式检测，具名方法待核。
- **Benchmark** · 正常图像训练，输出像素热图和图像分数。
- **关键结果 / 消融** · 理论分解区分不可约项与得分分布偏差。
- **适用条件 / 局限** · 路径选择与正常样本覆盖影响检测。

**可复用机制** · 对照重建误差和场速度偏差，检查异常是否被过强生成器掩盖。

<a id="paper-152021"></a>

## Flow Perturbation++: Multi-Step Unbiased Jacobian Estimation for High-Dimensional Boltzmann Sampling

[官方论文页](https://neurips.cc/virtual/2026/poster/152021) · [作者来源](https://openreview.net/forum?id=W6FlrDtr71)

- **问题 / 瓶颈** · 单步随机 Jacobian 估计方差大。
- **核心创新 / 方法** · 沿概率流离散轨迹分步估计 Jacobian，降低无偏估计的波动。
- **Baseline** · Hutchinson 与单步 Flow Perturbation。
- **Benchmark** · 千维高斯混合上的平衡采样。
- **关键结果 / 消融** · 作者报告采样改善。
- **适用条件 / 局限** · 离散步数增加带来的计算成本需核。

**可复用机制** · 在同计算预算下比较单次估计和分步估计的方差及有效样本量。

<a id="paper-148780"></a>

## FlowR2A: Learning Reward-to-Action Distribution for Multimodal Driving Planning

[官方论文页](https://neurips.cc/virtual/2026/poster/148780) · [作者来源](https://openreview.net/forum?id=v7t2EKHHHj)

- **问题 / 瓶颈** · 固定轨迹库可用密集奖赏，但不能生成新的轨迹。
- **核心创新 / 方法** · 把模拟奖赏作为流匹配条件，以时间分辨奖赏区分安全、进度与舒适目标。
- **Baseline** · 固定词表打分式和锚点式规划。
- **Benchmark** · 多模态驾驶规划；测试设置待核。
- **关键结果 / 消融** · 作者提出可按奖赏控制测试时采样；幅度待核。
- **适用条件 / 局限** · 依赖模拟奖赏正确性，硬约束仍需独立验收。

**可复用机制** · 在固定候选数量下对照奖赏条件生成和生成后打分。

<a id="paper-152705"></a>

## FlowSteer: Towards Agents Designing Agentic Workflows via Reinforced Progressive Canvas Editing

[官方论文页](https://neurips.cc/virtual/2026/poster/152705) · [作者来源](https://openreview.net/forum?id=R0wivLiPfK)

- **问题 / 瓶颈** · 一次性设计多步工作流缺少逐步执行反馈。
- **核心创新 / 方法** · 在可执行图画布上每轮做一次原子编辑，接收检查与执行反馈并用强化学习训练。
- **Baseline** · 现有工作流构建基线，具名方法待核。
- **Benchmark** · 十二个数据集；本文仅考察正常授权流程。
- **关键结果 / 消融** · 作者报告优于对照。
- **适用条件 / 局限** · 依赖受控算子库及可核验反馈。

**可复用机制** · 在同执行预算下比较原子编辑与一次性生成，记录修复成功率。

<a id="paper-152250"></a>

## FlowTrack: Controlling Edit-Signal Execution in Inversion-Free Flow Video Editing

[官方论文页](https://neurips.cc/virtual/2026/poster/152250) · [作者来源](https://openreview.net/forum?id=USNrqsbBWX)

- **问题 / 瓶颈** · 逐步注入编辑速度可能累积时序抖动。
- **核心创新 / 方法** · 保留原生成器与速度信号，通过延续的位移方向和按响应衰减控制执行。
- **Baseline** · 直接注入速度差的免反演编辑器。
- **Benchmark** · 文本引导视频编辑，关注运动和未编辑区域稳定。
- **关键结果 / 消融** · 具体结果及消融待全文核。
- **适用条件 / 局限** · 强编辑时平滑可能削弱响应。

**可复用机制** · 以相同编辑信号比较直接注入与有记忆控制，分测语义和运动保持。

<a id="paper-154703"></a>

## Flux Attention: Context-Aware Hybrid Attention for Efficient LLMs Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/154703) · [作者来源](https://openreview.net/forum?id=BfLKfkqbAC)

- **问题 / 瓶颈** · 固定稀疏比例难适应检索需求，逐头动态还可能负载不均。
- **核心创新 / 方法** · 在冻结模型中用轻量路由按上下文逐层选全注意力或稀疏注意力。
- **Baseline** · 静态混合注意力与逐头动态稀疏。
- **Benchmark** · 长上下文自回归推理，兼顾检索与真实延时。
- **关键结果 / 消融** · 加速与检索量化待全文核对。
- **适用条件 / 局限** · 硬件、路由粒度及上下文偏移影响收益。

**可复用机制** · 同时测算量和墙钟时间，避免忽略不均衡的同步成本。

<a id="paper-152301"></a>

## FluxLite: Inference-Time Proposal Control for Discrete Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152301) · [作者来源](https://openreview.net/forum?id=U53acQOZ93)

- **问题 / 瓶颈** · 离散扩散倾斜采样中提议不匹配会导致粒子权重退化。
- **核心创新 / 方法** · 调整离散跃迁提议并以图散度补偿，保持目标路径且降低权重方差。
- **Baseline** · 基础 Feynman–Kac SMC。
- **Benchmark** · 离散扩散推理；具体基准待核。
- **关键结果 / 消融** · 证明目标保持及覆盖相关的稳定性条件。
- **适用条件 / 局限** · 覆盖不足仍限制有限粒子效果。

**可复用机制** · 同时报告权重方差和有效样本量，区分目标正确与有限预算下的效率。

<a id="paper-151170"></a>

## Flux: Online, Fine-Grained Data Scheduling for Training Machine Learning Interatomic Potentials

[官方论文页](https://neurips.cc/virtual/2026/poster/151170) · [作者来源](https://openreview.net/forum?id=cTBlOIoXV7)

- **问题 / 瓶颈** · 原子数相同的数据可能有不同图计算负载。
- **核心创新 / 方法** · 加载时估计几何和图负载，在线校准时间与内存并分配微批。
- **Baseline** · 按原子数分批及离线负载表。
- **Benchmark** · 大规模原子间势训练，考察各设备耗时和内存。
- **关键结果 / 消融** · 摘要给出在线负载调度机制，量化待核。
- **适用条件 / 局限** · 预测器需要随架构及数据变化校准。

**可复用机制** · 按真实计算负载而非样本数做分布式均衡。

<a id="paper-139220"></a>

## FML-bench: A Controlled Study of AI Research Agent Strategies from the Perspective of Search Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/139220) · [作者来源](https://openreview.net/forum?id=e4mtg1jObb)

- **问题 / 瓶颈** · 搜索策略与编辑执行基础设施混杂，使榜单难以归因。
- **核心创新 / 方法** · 统一执行环境，比较不同搜索拓扑并记录过程指标。
- **Baseline** · 贪心爬山、树搜索及其他代表性代理。
- **Benchmark** · 十个方向的 18 个基础机器学习任务，另设 12 项过程指标。
- **关键结果 / 消融** · 摘要称简单贪心接近最好的树搜索，复杂度未保证领先。
- **适用条件 / 局限** · 结果依赖任务、预算及模型。

**可复用机制** · 固定基础设施和等预算，对照策略时记录探索过程而非只看终分。

<a id="paper-154897"></a>

## fmxcoders: Factorized Masked Crosscoders for Cross-Layer Feature Discovery

[官方论文页](https://neurips.cc/virtual/2026/poster/154897) · [作者来源](https://openreview.net/forum?id=A71gEbBJUL)

- **问题 / 瓶颈** · 跨层权重分布无法证明激活依赖多层
- **核心创新 / 方法** · 共享低秩跨层基并随机遮蔽层
- **Baseline** · 标准 crosscoder、逐层 SAE
- **Benchmark** · GPT2-Small、Pythia、Gemma2，探针 F1、重建误差和功能一致性
- **关键结果 / 消融** · F1 提高 10–30 点，均方误差降 25–50%
- **适用条件 / 局限** · 语义连贯性还取决于评判标准

**可复用机制** · 在字典学习中遮蔽输入组检验功能依赖是否真的分散

<a id="paper-150481"></a>

## Focal Reward: Balanced Reinforcement Learning under Rubric-Based Rewards

[官方论文页](https://neurips.cc/virtual/2026/poster/150481) · [作者来源](https://openreview.net/forum?id=hkAx0LeHmi)

- **问题 / 瓶颈** · 静态汇总会掩盖单项缺陷
- **核心创新 / 方法** · 逆奖励投影估计饱和度，再自动重加权
- **Baseline** · 最强静态聚合对照
- **Benchmark** · 三种模型规模、六个生成任务基准
- **关键结果 / 消融** · 作者报告 18 组比较均改善
- **适用条件 / 局限** · 依赖评分准则的可信度

**可复用机制** · 优先强化还有提升余地的准则，按维度绘制训练曲线

<a id="paper-153419"></a>

## Focusable Monocular Depth Estimation

[官方论文页](https://neurips.cc/virtual/2026/poster/153419) · [作者来源](https://openreview.net/forum?id=LTHElHJrAh)

- **问题 / 瓶颈** · 全图统一损失忽略前景与边界
- **核心创新 / 方法** · 多尺度对齐分割特征与深度特征，门控注入框或文本提示
- **Baseline** · 全局微调 DA2、DA3
- **Benchmark** · FDE-Bench 五个数据源，区域误差与全图几何
- **关键结果 / 消融** · 破坏对齐使 AbsRel 最多增加 13.8%
- **适用条件 / 局限** · 依赖提示定位和相对深度的定义

**可复用机制** · 在固定全局精度下单独评价目标区和边界误差

<a id="paper-152059"></a>

## FocusBranch: Combinatorial Branch-and-Bound for $\ell_0$ Neural Network Robustness Verification

[官方论文页](https://neurips.cc/virtual/2026/poster/152059) · [作者来源](https://openreview.net/forum?id=VoRt2Q8ngL)

- **问题 / 瓶颈** · 稀疏扰动空间的组合数量巨大
- **核心创新 / 方法** · 用焦点集合与最少扰动数定义节点，结合覆盖设计和线性松弛
- **Baseline** · 现有鲁棒性验证器
- **Benchmark** · MNIST、Fashion-MNIST、CIFAR-10 图像分类模型
- **关键结果 / 消融** · 作者报告比现有验证器更高效
- **适用条件 / 局限** · 保证限于所设局部扰动模型

**可复用机制** · 根据子问题通过率和验证代价调整分支策略

<a id="paper-148676"></a>

## Focused Forcing: Content-Aware Per-Frame KV Selection for Efficient Autoregressive Video Diffusion

[官方论文页](https://neurips.cc/virtual/2026/poster/148676) · [作者来源](https://openreview.net/forum?id=vvkRFRkj8O)

- **问题 / 瓶颈** · 同一块内的不同帧依赖不同历史内容
- **核心创新 / 方法** · 逐帧结合注意力与历史多样性选帧，并依头部重要性分配预算
- **Baseline** · 块级共享历史及既有缓存方法
- **Benchmark** · 多种自回归视频生成范式，测运行时间和质量
- **关键结果 / 消融** · 端到端最高加速 1.48 倍
- **适用条件 / 局限** · 重要性估计的跨任务迁移待核

**可复用机制** · 检验共享缓存索引是否会忽略块内异质性

<a id="paper-155092"></a>

## Focus Matters: Attention-Value Dynamics for Hallucination Mitigation in Vision-Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155092) · [作者来源](https://openreview.net/forum?id=8VaNJuKNNk)

- **问题 / 瓶颈** · 权重小不代表输出影响小
- **核心创新 / 方法** · 识别视觉聚焦阶段并对低权重值进行诊断性替换
- **Baseline** · 无干预及其他推理时缓解技术
- **Benchmark** · 多个视觉语言骨干，物体幻觉和真实物体识别
- **关键结果 / 消融** · 作者报告幻觉下降而真实物体证据大体保留
- **适用条件 / 局限** · 视觉阶段及阈值可能随模型变化

**可复用机制** · 用权重与值的联合干预区分相关性与实际影响

<a id="paper-149699"></a>

## FocusNav: Learning Task-directed Perception via Action-Aware Future Reconstruction in Vision-and-Language Navigation

[官方论文页](https://neurips.cc/virtual/2026/poster/149699) · [作者来源](https://openreview.net/forum?id=o6XALDEi9V)

- **问题 / 瓶颈** · 不准确的子目标会误导低层执行
- **核心创新 / 方法** · 重建指令目标与可通行区域，约束预期视觉变化和动作实际效果对齐
- **Baseline** · 近期视觉语言导航方法
- **Benchmark** · R2R-CE、RxR-CE 和实机
- **关键结果 / 消融** · 作者报告表现及速度改善，具体幅度待核
- **适用条件 / 局限** · 依赖单目可见线索和动作效果测量

**可复用机制** · 检验预测变化是否真正反映动作执行，而非仅重建当前环境

<a id="paper-150522"></a>

## Focus on Where You Aggregate: Restricted SAM for Non-IID Federated Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/150522) · [作者来源](https://openreview.net/forum?id=hTzdtftVAe)

- **问题 / 瓶颈** · 逐客户端平坦化未必改善全局聚合点
- **核心创新 / 方法** · 按上一轮更新方向及客户端方差定义锥域，限制 SAM 的扰动方向
- **Baseline** · 常规联邦 SAM
- **Benchmark** · 视觉和语言骨干上的非独立同分布任务
- **关键结果 / 消融** · 作者报告收敛稳定性和性能改善
- **适用条件 / 局限** · 上一轮方向在分布变化时可能失效

**可复用机制** · 用聚合点误差检查优化邻域是否和部署位置匹配

<a id="paper-152816"></a>

## FOGO: Forgetting-aware Orthogonalization Optimizer

[官方论文页](https://neurips.cc/virtual/2026/poster/152816) · [作者来源](https://openreview.net/forum?id=QBkoiaQrV0)

- **问题 / 瓶颈** · 占优批次梯度容易覆盖弱但有用方向
- **核心创新 / 方法** · 正交化动量，低维码本记录代表方向，冲突时正交修正
- **Baseline** · Adam、Muon
- **Benchmark** · 类别失衡分类、持续学习、LLaVA-7B 微调和 GPT-2 预训练
- **关键结果 / 消融** · 作者报告收敛及保持能力改善
- **适用条件 / 局限** · 码本覆盖与计算开销待复核

**可复用机制** · 将历史方向作为优化状态并在等开销下测试遗忘程度

<a id="paper-139022"></a>

## Follow-Bench 2.0: An End-to-End 3D Benchmark for Socially-Aware Robot Person Following

[官方论文页](https://neurips.cc/virtual/2026/poster/139022) · [作者来源](https://openreview.net/forum?id=q4Gs05xKgs)

- **问题 / 瓶颈** · 各自独立的感知和规划指标遗漏闭环误差
- **核心创新 / 方法** · 在统一仿真设置中比较不同感知规划组合，设置背后与并行跟随
- **Baseline** · 模块化控制、端到端视觉策略与主动跟踪
- **Benchmark** · Follow-Bench 2.0，成功、可见度、恢复及社会距离
- **关键结果 / 消融** · 模块化方案在近距离舒适跟随上领先，侧向跟随仍困难
- **适用条件 / 局限** · 证据基于仿真

**可复用机制** · 评测人机协同行走时分别统计可见、失联后恢复和空间侵入

<a id="paper-150971"></a>

## Follow the Mean: Reference-Guided Flow Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/150971) · [作者来源](https://openreview.net/forum?id=dtoO1TcUb8)

- **问题 / 瓶颈** · 部分生成属性难以用文本控制
- **核心创新 / 方法** · 按条件终点均值修正流场，或学习锚定于参考均值的残差
- **Baseline** · 冻结 FLUX 模型、无条件 DiT-B/4
- **Benchmark** · 图像颜色、风格、结构控制与 AFHQv2 质量
- **关键结果 / 消融** · 作者报告固定提示和种子仍能控制属性，摊销方法质量与 DiT 接近
- **适用条件 / 局限** · 结论针对确定性插值和所测参考分布

**可复用机制** · 将示例选择设为独立变量，固定其他因素检查其对生成的影响

<a id="paper-150986"></a>

## Follow the Regularized Leader Does Not Converge in Constrained Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/150986) · [作者来源](https://openreview.net/forum?id=dmNapb9nHG)

- **问题 / 瓶颈** · 目标单调改善不保证约束问题达驻点
- **核心创新 / 方法** · 构造光滑函数与高维连续时间 FTRL 轨迹
- **Baseline** · 镜像下降及梯度下降的既有收敛结果
- **Benchmark** · 约束非凸优化的理论反例
- **关键结果 / 消融** · KKT 残差可以永久远离零
- **适用条件 / 局限** · 反例针对连续时间设置

**可复用机制** · 若考虑 FTRL 求解约束非凸问题，应检查驻点残差而非只看目标值

<a id="paper-148167"></a>

## Follow the Winners: Conservative Policy Improvement with the Cross-Entropy Method for Critic-Free RFT

[官方论文页](https://neurips.cc/virtual/2026/poster/148167) · [作者来源](https://openreview.net/forum?id=znxdUBOoQP)

- **问题 / 瓶颈** · 高方差轨迹会诱发过强更新
- **核心创新 / 方法** · 用交叉熵思想构建更保守的策略更新
- **Baseline** · GRPO、DPO
- **Benchmark** · 完整信息 Sokoban、不完整信息 Search-R1
- **关键结果 / 消融** · 作者报告前者匹配 GRPO、后者优于 GRPO
- **适用条件 / 局限** · 结论依赖奖励和不确定性设定

**可复用机制** · 按环境信息充分程度分组检查风险偏好是否帮助探索

<a id="paper-154247"></a>

## FoMEMO: Towards Foundation Models for Expensive Multi-objective Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/154247) · [作者来源](https://openreview.net/forum?id=FBTD1aJKiR)

- **问题 / 瓶颈** · 新任务反复拟合代理耗费评估
- **核心创新 / 方法** · 按偏好聚合目标预训练后验并在测试时从观测上下文预测
- **Baseline** · 从头拟合高斯过程和超体积策略
- **Benchmark** · 未见多目标任务
- **关键结果 / 消融** · 作者报告无需更新即可泛化，数值待核
- **适用条件 / 局限** · 依赖预训练任务覆盖和偏好表示

**可复用机制** · 按偏好拆解后验学习，并在相同任务条件下核对收益与适用边界。

<a id="paper-152890"></a>

## FoMo: Forking Moment in Generative Trajectory as a Perceptual Distance

[官方论文页](https://neurips.cc/virtual/2026/poster/152890) · [作者来源](https://openreview.net/forum?id=PdoitgUpJ7)

- **问题 / 瓶颈** · 人工绝对分数昂贵且有噪声
- **核心创新 / 方法** · 同轨迹在不同时刻分叉，以分叉先后作为监督
- **Baseline** · 人工绝对分数和成对选择数据
- **Benchmark** · 多骨干与多个质量评估基准
- **关键结果 / 消融** · 作者报告多个基准优于人工标注训练
- **适用条件 / 局限** · 分叉时刻的感知对应关系依赖生成模型

**可复用机制** · 用扩散分叉时刻生成感知距离标注，并在相同任务条件下核对收益与适用边界。

<a id="paper-138956"></a>

## ForceBody: Force-Paired Parametric Body Motion with Torque Uncertainty

[官方论文页](https://neurips.cc/virtual/2026/poster/138956) · [作者来源](https://openreview.net/forum?id=u95B9zb2bH)

- **问题 / 瓶颈** · 动作配准误差会传递到关节力矩标签
- **核心创新 / 方法** · 在逆动力学管线做蒙特卡洛并估计逐帧逐关节不确定度
- **Baseline** · MLP、Conv1D、LSTM、GRU、Mamba2、Transformer
- **Benchmark** · 140 人的 10389 条动作，预测地面反力与关节力矩
- **关键结果 / 消融** · Transformer 加权后力矩 MAE 降 12%
- **适用条件 / 局限** · 不确定度依赖误差模型

**可复用机制** · 用标签不确定度加权逆动力学监督，并在相同任务条件下核对收益与适用边界。

<a id="paper-139069"></a>

## Forced Orders: What LLM Leaderboards Hide About Model Comparisons

[官方论文页](https://neurips.cc/virtual/2026/poster/139069) · [作者来源](https://openreview.net/forum?id=n4qyXPVmSo)

- **问题 / 瓶颈** · 总分掩盖逐任务胜负及并列
- **核心创新 / 方法** · 逐任务统计模型间胜负平并以 SPA 聚合
- **Baseline** · 标量排行榜与 Elo
- **Benchmark** · AIME 2025、SWE-Bench Verified、Chatbot Arena 等
- **关键结果 / 消融** · 作者报告扰动下分层比 Elo 总序更稳定
- **适用条件 / 局限** · 同层表示证据不足，评估依赖任务构成

**可复用机制** · 用能力分层表达榜单无法支持的精细排序，并在相同任务条件下核对收益与适用边界。

<a id="paper-151896"></a>

## ForceFlow: Learning to Feel and Act via Contact-Driven Flow Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/151896) · [作者来源](https://openreview.net/forum?id=X8avpXmIqB)

- **问题 / 瓶颈** · 密集接触需要高精度即时力反馈
- **核心创新 / 方法** · 分阶段切换视觉和力觉，接触阶段联合预测力与动作
- **Baseline** · ForceVLA
- **Benchmark** · 六个真实接触操作任务
- **关键结果 / 消融** · 作者报告成功率较对照提高 37%，计算口径待核
- **适用条件 / 局限** · 依赖可靠的阶段转换与力传感

**可复用机制** · 分别建模视觉接近与力觉接触，并在相同任务条件下核对收益与适用边界。

<a id="paper-156065"></a>

## ForceLDM: A Force-aware Latent Dynamics Model for Contact-Rich Manipulation

[官方论文页](https://neurips.cc/virtual/2026/poster/156065) · [作者来源](https://openreview.net/forum?id=0j9L12vSKx)

- **问题 / 瓶颈** · 仅把力作为附加输入难学未来接触
- **核心创新 / 方法** · 教师读取未来力矩及光流，学生从当前观测蒸馏潜表示，训练渐进加噪
- **Baseline** · 现有接触操作策略，名称待核
- **Benchmark** · 五个真实接触任务、新物体与环境扰动
- **关键结果 / 消融** · 作者报告表现及泛化改善
- **适用条件 / 局限** · 训练需未来同步信号，改善幅度待核

**可复用机制** · 用未来力觉教当前观测策略预测接触，并在相同任务条件下核对收益与适用边界。

<a id="paper-152033"></a>

## Forecasting Downstream Performance of LLMs With Proxy Metrics

[官方论文页](https://neurips.cc/virtual/2026/poster/152033) · [作者来源](https://openreview.net/forum?id=W2xeiyOmWL)

- **问题 / 瓶颈** · 交叉熵与能力对齐差，直接评估贵
- **核心创新 / 方法** · 聚合专家解答 token 的熵、前 k 准确率和专家 token 名次
- **Baseline** · 损失与计算量代理及完整任务评估
- **Benchmark** · 跨家族选模、25 个语料排序、训练预测
- **关键结果 / 消融** · 跨家族 Spearman 0.81 对交叉熵 0.36，训练预测覆盖 18 倍计算范围
- **适用条件 / 局限** · 依赖可代表目标能力的专家轨迹

**可复用机制** · 用专家解答上的分布统计预测模型下游能力，并在相同任务条件下核对收益与适用边界。

<a id="paper-151608"></a>

## ForesightFlow: Self-Guided Flow Matching for Improving Vision-Language-Action Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151608) · [作者来源](https://openreview.net/forum?id=ZHqszixmfx)

- **问题 / 瓶颈** · 给评分一起降权会丢失失败监督
- **核心创新 / 方法** · 动作和成功潜势联合生成，仅对动作速度施加优势权重
- **Baseline** · 模仿学习与独立评论器
- **Benchmark** · 五个 BEHAVIOR-1K 仿真任务与五个双臂实物任务
- **关键结果 / 消融** · 作者报告训练计算降低 38%，解耦减轻价值虚高
- **适用条件 / 局限** · 依赖混合质量轨迹和评分校准

**可复用机制** · 把动作改进加权与成功评分校准分开，并在相同任务条件下核对收益与适用边界。

<a id="paper-153986"></a>

## Forgery Evidence Peaks Mid-Stack: Forensic Evidence Relay for Multimodal Forgery Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/153986) · [作者来源](https://openreview.net/forum?id=H3UPd6NZ4I)

- **问题 / 瓶颈** · 最终层可能弱化局部篡改证据
- **核心创新 / 方法** · 诊断中间层证据峰值，以门控残差传递到后层
- **Baseline** · 三种多模态伪造检测骨干
- **Benchmark** · 七个检测基准，测真实性、解释和定位
- **关键结果 / 消融** · 作者报告三类指标改善且最佳读取层对应峰值
- **适用条件 / 局限** · 层位置依赖骨干，掩码只用于诊断

**可复用机制** · 按逐层证据探针选择检测特征读出层，并在相同任务条件下核对收益与适用边界。

<a id="paper-152962"></a>

## Forgetting Has Neighbors: Localized Collateral Forgetting in Machine Unlearning

[官方论文页](https://neurips.cc/virtual/2026/poster/152962) · [作者来源](https://openreview.net/forum?id=P4bVkIi9y9)

- **问题 / 瓶颈** · 整体精度可能隐藏局部误差
- **核心创新 / 方法** · 按邻近程度比较重训练输出，用保留邻居训练局部软标签教师
- **Baseline** · 梯度上升、随机标签和完整重训
- **Benchmark** · CIFAR-100 部分类别删除
- **关键结果 / 消融** · 近邻预测更接近重训，整体指标保持竞争力
- **适用条件 / 局限** · 跨数据集和距离定义待核

**可复用机制** · 在删除集合邻域单独衡量遗忘副作用，并在相同任务条件下核对收益与适用边界。

<a id="paper-148637"></a>

## Forgetting to Improve: Principled Data Removal in Active Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/148637) · [作者来源](https://openreview.net/forum?id=wF1w6w0jmM)

- **问题 / 瓶颈** · 更多观测可能加剧任务相关的估计偏差
- **核心创新 / 方法** · 在高斯过程用影响函数估计样本对目标任务的贡献
- **Baseline** · 保留既有训练数据的方案
- **Benchmark** · 贝叶斯优化、基于模型的强化学习和转导
- **关键结果 / 消融** · 作者报告多任务改善，幅度待核
- **适用条件 / 局限** · 依赖高斯过程和影响估计准确性

**可复用机制** · 模型失配时检验删除有害样本能否改进目标任务，并在相同任务条件下核对收益与适用边界。

<a id="paper-149516"></a>

## Forward Shapley Scoring for Non-Myopic Active Feature Acquisition

[官方论文页](https://neurips.cc/virtual/2026/poster/149516) · [作者来源](https://openreview.net/forum?id=pY9eibVqPA)

- **问题 / 瓶颈** · 贪心策略难发现必须组合才有用的证据
- **核心创新 / 方法** · 在预算内未来查询集合上估计候选特征的 Shapley 贡献
- **Baseline** · 贪心、OL-MFRL 与 ODIN-MFRL
- **Benchmark** · AFABench CUBE-NM 和受控因果图
- **关键结果 / 消融** · 准确率 0.664±0.024，对照 0.235、0.160
- **适用条件 / 局限** · 需已知因果模型或生成模型

**可复用机制** · 用组合边际价值选择当前查询，并在相同任务条件下核对收益与适用边界。

<a id="paper-149122"></a>

## FOAM: Factored One-sided Adam-Moment for Practical and Scalable SOAP

[官方论文页](https://neurips.cc/virtual/2026/poster/149122) · [作者来源](https://openreview.net/forum?id=sjGaILUb1z)

- **问题 / 瓶颈** · SOAP 的状态缓存及特征分解昂贵。
- **核心创新 / 方法** · 舍弃输出侧 Kronecker 因子，以行列统计分解旋转后二阶矩。
- **Baseline** · SOAP、Muon、AdamW。
- **Benchmark** · 最高 760M 参数语言模型预训练，测验证损失、时间与状态内存。
- **关键结果 / 消融** · 损失与 SOAP 和 Muon 相近，时间接近 Muon。
- **适用条件 / 局限** · 等价性依赖 K-FAC Fisher 假设，单侧选择依赖输出曲率近各向同性。

**可复用机制** · 先检查输出曲率是否值得单独建模，再用等时预算验证单侧近似。

<a id="paper-150940"></a>

## Foundation Pareto Flow Policy for Multi-Objective Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/150940) · [作者来源](https://openreview.net/forum?id=eAjbjgXFPE)

- **问题 / 瓶颈** · 既有多目标策略常绑定特定任务或目标。
- **核心创新 / 方法** · 扩散 Transformer 用流匹配训练，经大规模预训练、精选中训和少样本后训。
- **Baseline** · D4MORL 上既有先进方法，具名待核。
- **Benchmark** · D4MORL，零样本偏好插值外推与少样本任务适配。
- **关键结果 / 消融** · 作者报告优于既有对照，幅度待核。
- **适用条件 / 局限** · 依赖历史数据的 Pareto 区域覆盖。

**可复用机制** · 把未见偏好与未见动力学分别留出，比较完整训练与去掉中训或后训。

<a id="paper-148841"></a>

## Found in Conversation: LLMs Teach Themselves to Close the Multi-Turn Gap

[官方论文页](https://neurips.cc/virtual/2026/poster/148841) · [作者来源](https://openreview.net/forum?id=ukPBQf8cPw)

- **问题 / 瓶颈** · 信息逐轮澄清时，模型表现低于一次性获得全部信息。
- **核心创新 / 方法** · 同一自蒸馏骨干以单轮全量视图监督多轮视图。
- **Baseline** · 自身单轮与多轮表现。
- **Benchmark** · Llama、Qwen、Phi、OLMo，3B–14B，多轮任务。
- **关键结果 / 消融** · 两个 Llama 恢复全部单轮表现，所有测试模型恢复超过 90%。
- **适用条件 / 局限** · 任务细节和分布外对话待核。

**可复用机制** · 保持信息一致，只变更教师与学生看到的信息组织方式，观察恢复幅度。

<a id="paper-149835"></a>

## FoundSurface: Feedforward Ray-Based 3D Scene Surface Reconstruction from Unposed Images

[官方论文页](https://neurips.cc/virtual/2026/poster/149835) · [作者来源](https://openreview.net/forum?id=mwnXqnBf8n)

- **问题 / 瓶颈** · 无位姿点图离散且稀疏。
- **核心创新 / 方法** · 预训练点图提供先验，surfel 投票筛视角，交叉注意力估计粗面，局部射线特征细化细节及法线。
- **Baseline** · 无位姿前馈方法，具名待核。
- **Benchmark** · 9 数据集训练、6 未见数据集零样本测试，测几何精度和细节。
- **关键结果 / 消融** · 作者报告超过所比先进模型，幅度待核。
- **适用条件 / 局限** · 依赖点图质量和多视角覆盖。

**可复用机制** · 分别验证参考视角筛选与连续射线细化，报告重建几何和法线。

<a id="paper-148775"></a>

## Foveal-Mamba: Inside-Out Ring Scanning with Recurrent Offset Prediction for Visual State Space Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148775) · [作者来源](https://openreview.net/forum?id=v9TJRTPJEp)

- **问题 / 瓶颈** · 仅凭局部响应选偏移，采样轨迹与递归状态脱节。
- **核心创新 / 方法** · 中心向外环扫，轻量 Mamba 用累计状态估计偏移。
- **Baseline** · DAMamba-Tiny 等。
- **Benchmark** · ImageNet-1K、ADE20K、COCO，测准确率、mIoU 和 AP。
- **关键结果 / 消融** · Tiny Top-1 84.3%，超过所比 DAMamba-Tiny 0.5 个百分点。
- **适用条件 / 局限** · 特殊长宽比及环扫先验的独立收益待核。

**可复用机制** · 检测视觉 SSM 的采样网络是否利用递归状态，并对照纯局部偏移。

<a id="paper-149976"></a>

## Foveated BagNet: Inherent Interpretability Does Not Exclude Global Context

[官方论文页](https://neurips.cc/virtual/2026/poster/149976) · [作者来源](https://openreview.net/forum?id=lnLU62lg9R)

- **问题 / 瓶颈** · 只看小块的可解释模型丢失全局上下文。
- **核心创新 / 方法** · 每个局部分类器读取同中心的多尺度图块，外围逐步降低分辨率。
- **Baseline** · BagNet-33 和 ResNet-50。
- **Benchmark** · ImageNet Top-1 与显著性图。
- **关键结果 / 消融** · 准确率 74%，两项对照分别为 65% 和 76%。
- **适用条件 / 局限** · 空间归因可追踪性不等于完整解释，跨任务待核。

**可复用机制** · 在固定局部归因接口下测试外围低频信息能否恢复分类能力。

<a id="paper-152899"></a>

## Fractional Power-of-Two Quantization for Efficient and Effective Multiplier-Free LLM Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/152899) · [作者来源](https://openreview.net/forum?id=PZZZiYPLst)

- **问题 / 瓶颈** · 整数二次幂量化格点过粗。
- **核心创新 / 方法** · 用平方根二网格、整型激活及近似网格校准，校准后的比例并入通道尺度。
- **Baseline** · 标准 PoT 与均匀整数。
- **Benchmark** · 七模型三位宽，含 Llama-3-8B 零样本常识。
- **关键结果 / 消融** · W4A4 比 PoT 相对提升 8.72%，比均匀整数低约 0.4 个百分点。
- **适用条件 / 局限** · 门电路优势不保证所有硬件实测吞吐改善。

**可复用机制** · 按实际算子实现校准权重，联合测任务精度和硬件开销。

<a id="paper-150427"></a>

## Fractional State Space Transition for Long Sequence Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/150427) · [作者来源](https://openreview.net/forum?id=i6ZEbxGeKu)

- **问题 / 瓶颈** · 普通 ODE 型 SSM 指数遗忘，难覆盖宽时间尺度。
- **核心创新 / 方法** · 以有限指数模态近似分数阶核，支持并行训练和固定状态解码。
- **Baseline** · 先进 SSM，具名待核。
- **Benchmark** · 最高 1.3B 参数语言建模的长短上下文对照。
- **关键结果 / 消融** · 作者报告长上下文改善且短上下文有竞争力。
- **适用条件 / 局限** · 模式数量决定可近似的时间范围。

**可复用机制** · 固定状态预算下比较指数和幂律核，扫描超出训练长度的序列。

<a id="paper-155391"></a>

## FrameRouter: Frame Budget Routing for Long-Video Understanding on Video-MME-v2 and Beyond

[官方论文页](https://neurips.cc/virtual/2026/poster/155391) · [作者来源](https://openreview.net/forum?id=61Yi6KS7Ek)

- **问题 / 瓶颈** · 统一预算对不同问题的证据覆盖不均。
- **核心创新 / 方法** · 用训练外的需求路由器和受预算约束的分配器，调用冻结采样策略。
- **Baseline** · 等平均帧预算的统一分配。
- **Benchmark** · Video-MME-v2 等长视频问答。
- **关键结果 / 消融** · 同平均预算下作者报告问答改善；幅度待核。
- **适用条件 / 局限** · 在线需求估计与问答证据可能失配。

**可复用机制** · 比较等预算的动态配额与均分，固定选帧策略以分离影响。

<a id="paper-154230"></a>

## FrameVGGT: Coherence-Preserving Memory for Bounded Streaming Geometry

[官方论文页](https://neurips.cc/virtual/2026/poster/154230) · [作者来源](https://openreview.net/forum?id=FFNTtlQxxZ)

- **问题 / 瓶颈** · 逐条缓存容易丢失多视图匹配的几何一致性。
- **核心创新 / 方法** · 组织固定容量的帧级 KV 段，使用紧凑键空间原型和稀疏锚点。
- **Baseline** · StreamVGGT 类流式几何及其他缓存对照，具体待核。
- **Benchmark** · 长序列三维重建、视频深度和相机位姿。
- **关键结果 / 消融** · 作者报告固定预算下几何更稳且精度内存折衷较好。
- **适用条件 / 局限** · 依赖跨视角匹配和锚点选择，闭环效果待核。

**可复用机制** · 在相同缓存大小下比较单 token 与完整观测组缓存，测长序列一致性。

<a id="paper-148622"></a>

## FreeAct: Demonstration-Free Robot Adaptation via Action-Grounded Generated Videos

[官方论文页](https://neurips.cc/virtual/2026/poster/148622) · [作者来源](https://openreview.net/forum?id=wNWxVVntG2)

- **问题 / 瓶颈** · 视频视觉合理不保证运动学一致
- **核心创新 / 方法** · 离散动作 token 对齐相机坐标末端 SE(3) 和夹爪变化，联合源域监督适配
- **Baseline** · 源域预训练策略与仅生成视频适配
- **Benchmark** · 目标环境偏移后的操作成功率
- **关键结果 / 消融** · 报告 2% 到 57%，再经自身轨迹适配到 74%
- **适用条件 / 局限** · 生成视频伪影和相机标定误差仍需监控

**可复用机制** · 验证动作码跨本体一致性后再扩大伪标注

<a id="paper-153859"></a>

## Free Draft-and-Verification: Toward Lossless Parallel Decoding for Diffusion Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153859) · [作者来源](https://openreview.net/forum?id=ICXpR98ax5)

- **问题 / 瓶颈** · 阈值并行可能改变生成质量
- **核心创新 / 方法** · 把未来 token 预测作为免费草案，在后续前向中自校验
- **Baseline** · 逐 token 静态解码与启发式并行
- **Benchmark** · 数学推理与代码生成，测每次前向 token 数和吞吐
- **关键结果 / 消融** · 最高分别 5.48 倍和 3.94 倍，保证复现静态结果
- **适用条件 / 局限** · 保证相对指定静态流程

**可复用机制** · 加速验收同时测逐序列等价与实际吞吐

<a id="paper-155600"></a>

## Free Heavy-Tailed Lunch for Muon: A Theoretical Justification of Empirical Success

[官方论文页](https://neurips.cc/virtual/2026/poster/155600) · [作者来源](https://openreview.net/forum?id=4Mid5GMDGS)

- **问题 / 瓶颈** · 欧氏方法在重尾梯度下可能付出维度代价
- **核心创新 / 方法** · 分析 Muon 等矩阵优化器的核范数驻点样本复杂度
- **Baseline** · 欧氏方法及其他 Schatten 几何
- **Benchmark** · 重尾非凸理论与语言模型训练
- **关键结果 / 消融** · 证明所设核范数驻点下 Muon 的维度项最优
- **适用条件 / 局限** · 依赖梯度中心矩与光滑性设定

**可复用机制** · 测重尾程度与几何后再做矩阵优化器消融

<a id="paper-148432"></a>

## Free Lunch for Pass@$k$? Low Cost Diverse Sampling for Diffusion Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148432) · [作者来源](https://openreview.net/forum?id=xpcBxYxoCo)

- **问题 / 瓶颈** · 独立样本容易重复同一种失败
- **核心创新 / 方法** · 依次修改一批扩散中间表示以减少候选重叠
- **Baseline** · 独立采样
- **Benchmark** · HumanEval、GSM8K，LLaDA 与 Dream，测多样性和 Pass@k
- **关键结果 / 消融** · 作者报告两类指标改善，幅度待核
- **适用条件 / 局限** · 批内顺序和排斥强度可能损害候选质量

**可复用机制** · 固定预算比较样本独立性与有效异质解数量

<a id="paper-149840"></a>

## FreeOcc: Decoupling Ego-Motion for Efficient 4D Occupancy Forecasting via Continuous Flow Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/149840) · [作者来源](https://openreview.net/forum?id=mu2BHamTXA)

- **问题 / 瓶颈** · 时序模块重复学习可由里程计给出的运动
- **核心创新 / 方法** · SE(2) 解耦加残差流，按不确定性路由到单步或 ODE
- **Baseline** · 重注意力或循环占据模型，具名基线待核
- **Benchmark** · nuScenes、零样本 SemanticKITTI 和传感扰动
- **关键结果 / 消融** · nuScenes 32.1% mIoU，集成模式 27 FPS
- **适用条件 / 局限** · 依赖里程计准确性和不确定性估计

**可复用机制** · 先补偿已知运动再学习场景残差

<a id="paper-149836"></a>

## FreeSpec: Training-Free Long Video Generation via Singular-Spectrum Reconstruction

[官方论文页](https://neurips.cc/virtual/2026/poster/149836) · [作者来源](https://openreview.net/forum?id=mwefOglxvK)

- **问题 / 瓶颈** · 延长窗口会压制细节及运动方向的谱能量
- **核心创新 / 方法** · 低秩全局引导与高秩局部基底融合
- **Baseline** · 固定划分全局和局部分支的免训练方法
- **Benchmark** · Wan2.1 与 LTX-Video 的长视频合成
- **关键结果 / 消融** · 报告时序动态改善且保持画面质量，量化待核
- **适用条件 / 局限** · SVD 成本和截断策略待核

**可复用机制** · 扩窗前后测奇异谱变化并比较不同融合秩

<a id="paper-148488"></a>

## FreqCa: Accelerating Image generation and editing via Frequency-Aware Caching

[官方论文页](https://neurips.cc/virtual/2026/poster/148488) · [作者来源](https://openreview.net/forum?id=xRAhPVJ1wk)

- **问题 / 瓶颈** · 全频假设相邻步相似会失效
- **核心创新 / 方法** · 分频缓存与二阶 Hermite 插值，以累计残差替代逐层缓存
- **Baseline** · 整特征缓存方法
- **Benchmark** · FLUX 与 Qwen-Image 生成编辑模型
- **关键结果 / 消融** · 作者报告缓存内存降低 99%，质量和速度详值待核
- **适用条件 / 局限** · 频带行为可能随采样器变化

**可复用机制** · 先测不同频带相似性与连续性再确定缓存策略

<a id="paper-154121"></a>

## Frequency‑Aware Flow Matching for Continuous and Consistent Robotic Action Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/154121) · [作者来源](https://openreview.net/forum?id=G7fOG13nTJ)

- **问题 / 瓶颈** · 混频率示范的离散动作块难统一
- **核心创新 / 方法** · DCT 系数上做流匹配，以一阶时间导数约束平滑
- **Baseline** · 离散动作块的流策略和视觉语言动作模型
- **Benchmark** · 玩具、避障、LapGym、LIBERO 和 Franka 真机
- **关键结果 / 消融** · 作者报告稳定性及成功率改善，幅度待核
- **适用条件 / 局限** · 平滑项可能压制真实突变接触

**可复用机制** · 异构频率采集时比较连续基动作与插值离散动作

<a id="paper-151162"></a>

## Frequency Domain Reservoir Computing

[官方论文页](https://neurips.cc/virtual/2026/poster/151162) · [作者来源](https://openreview.net/forum?id=cZ5lAACl8V)

- **问题 / 瓶颈** · 密集回声状态网络更新成本为平方量级
- **核心创新 / 方法** · 采用零填充输入、打包频域读出和原生频域非线性
- **Baseline** · 传统回声状态网络及序列模型
- **Benchmark** · 记忆、序列分类和长程多变量预测
- **关键结果 / 消融** · 密集更新线性复杂度，作者报告预测性能可比
- **适用条件 / 局限** · 依赖所用频域算子结构

**可复用机制** · 检查频域替代是否保留任务所需动态

<a id="paper-149155"></a>

## Frequency-Structured Hamiltonian Neural Network for Multi-Timescale Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/149155) · [作者来源](https://openreview.net/forum?id=sRJQgUFr36)

- **问题 / 瓶颈** · 单网络的频谱偏差妨碍刚性多时标系统学习
- **核心创新 / 方法** · 从滤波轨迹拟合多个 Hamiltonian 分量并合成单标量，PDE 时加入结构投影
- **Baseline** · 已有结构保持动力学模型
- **Benchmark** · FPU 链、浅水方程和 Taylor–Green 涡
- **关键结果 / 消融** · 作者报告长时滚动及能量行为改善
- **适用条件 / 局限** · 频带划分与守恒假设需符合实际系统

**可复用机制** · 在同预算下比较分频训练和直接拟合，联测滚动与能量误差

<a id="paper-154282"></a>

## FRESCO: A Novel Consistency Control for Asynchronous Pipeline Parallel Training

[官方论文页](https://neurips.cc/virtual/2026/poster/154282) · [作者来源](https://openreview.net/forum?id=Ez6jehFKyE)

- **问题 / 瓶颈** · 旧误差信号依赖旧特征，参数变化可能使反向梯度失配。
- **核心创新 / 方法** · 在激活子空间上约束更新作用为零，求最小修改的异步更新。
- **Baseline** · 代表性异步流水线方案。
- **Benchmark** · 大语言模型预训练，比较流水深度与不一致程度。
- **关键结果 / 消融** · 作者报告越深或失配越高时提升越明显。
- **适用条件 / 局限** · 约束和计算代价的具体权衡待核。

**可复用机制** · 使用前向等价性判定异步梯度是否可用，对照纯参数陈旧度约束。

<a id="paper-150248"></a>

## Freshness-Gated Imagination: Step-Level Trust for Latent World Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150248) · [作者来源](https://openreview.net/forum?id=jdqdKenIoy)

- **问题 / 瓶颈** · 同一想象轨迹里的不同步有不同预测偏差。
- **核心创新 / 方法** · 以优先回放改善熵信号校准，再用逐步熵软门控制梯度。
- **Baseline** · 单独启用任一模块与基础世界模型。
- **Benchmark** · Crafter 十种子几何分数和 DMC 连续控制。
- **关键结果 / 消融** · 单独逐步门控 −6.2%、单独轨迹适配 +0.6%、组合 +14.8%；DMC 基本持平。
- **适用条件 / 局限** · 依赖熵可反映模型可靠性，跨任务校准待测。

**可复用机制** · 用二乘二消融检验采样是否改善门控所用的置信信号。

<a id="paper-149612"></a>

## FRInGe: Distribution-Space Integrated Gradients with Fisher–Rao Geometry

[官方论文页](https://neurips.cc/virtual/2026/poster/149612) · [作者来源](https://openreview.net/forum?id=onv7aWVE1B)

- **问题 / 瓶颈** · 集成梯度对参考点与路径敏感。
- **核心创新 / 方法** · 从最大熵预测出发沿 Fisher–Rao 测地线插值，通过拉回度量与信赖域构造输入路径。
- **Baseline** · 常规集成梯度；其他对照待核。
- **Benchmark** · 六种 ImageNet 架构，测 MAS、扰动 AUC 和 infidelity。
- **关键结果 / 消融** · 校准类指标尤其 MAS 改善，其他指标具竞争力。
- **适用条件 / 局限** · 路径仍受模型与信赖域影响。

**可复用机制** · 比较预测空间路径与输入直线，分别测校准和删除忠实性。

<a id="paper-150468"></a>

## From Anti-Forgetting to Fast Adaptation: Continual Reinforcement Learning with World Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150468) · [作者来源](https://openreview.net/forum?id=hoG3Hx7DHo)

- **问题 / 瓶颈** · 奖励突变与固定规划长度拖慢新任务适应。
- **核心创新 / 方法** · 集合奖励预测指引探索，误差控制滚动长度，历史轨迹按质量重加权。
- **Baseline** · 已有持续强化学习策略，名称待核。
- **Benchmark** · Continual World、Continual Bench 和 DM Control。
- **关键结果 / 消融** · 作者报告适应和保持同时改善。
- **适用条件 / 局限** · 依赖奖励分歧及动力学误差估计，模块单独收益待核。

**可复用机制** · 把任务切换后的奖励校准速度和旧任务保持分开测量。

<a id="paper-155282"></a>

## From Baselines to Transport Geodesics: Axiomatic Attribution via Optimal Generative Flows

[官方论文页](https://neurips.cc/virtual/2026/poster/155282) · [作者来源](https://openreview.net/forum?id=6mst9gKX4f)

- **问题 / 瓶颈** · 相同预测仅因参考路径不同就可能得到不同解释。
- **核心创新 / 方法** · 固定路径用 Aumann–Shapley 积分；路径通过最小动能传输选取，以 Rectified Flow 近似。
- **Baseline** · 手工插值、其他流路径及常见归因对照。
- **Benchmark** · 归因稳定性、结构与删除忠实性；数据集待核。
- **关键结果 / 消融** · 作者报告低作用量路径更稳定，删除忠实性仍具竞争力。
- **适用条件 / 局限** · 传输逼近误差会传入归因，未保证路径在数据流形上。

**可复用机制** · 显式消融路径选择，在同归因积分规则下比较直线和流路径。

<a id="paper-152618"></a>

## From Click Imitation to Transition Equivalence: Rethinking Supervision for GUI Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/152618) · [作者来源](https://openreview.net/forum?id=Rlg9EOIVJF)

- **问题 / 瓶颈** · 同一目标可能有多种正确点击。
- **核心创新 / 方法** · 将示范转成状态转移描述，执行器选能实现转移的候选并检查结果。
- **Baseline** · 单动作模仿及既有界面代理。
- **Benchmark** · 网页预测、可执行导航、移动与桌面测试，测等价步骤、召回和完成率。
- **关键结果 / 消融** · 作者报告任务完成改善且无效操作减少。
- **适用条件 / 局限** · 依赖可靠的状态观察和目标判定。

**可复用机制** · 获准界面操作以状态达成为监督，评测替代操作和无效动作。

<a id="paper-155080"></a>

## From Clips to Streams: A Unified Framework for Streaming Sign Language Translation

[官方论文页](https://neurips.cc/virtual/2026/poster/155080) · [作者来源](https://openreview.net/forum?id=8cWsEeaaN5)

- **问题 / 瓶颈** · 预切分片段无法模拟连续手语的输入，串联误差会传播。
- **核心创新 / 方法** · 可变形 Transformer 并行解码边界和文本，以句感知滑窗采样及三模态预训练。
- **Baseline** · 先分割再翻译的串联流程。
- **Benchmark** · BOBSL、How2Sign 和两个合成流式数据集。
- **关键结果 / 消融** · 作者报告联合模型更好，所学边界在部分翻译对照中优于人工边界。
- **适用条件 / 局限** · 合成流结果不必然泛化至实时交互。

**可复用机制** · 将边界误差与语义质量分开衡量，并对照人工切分与联合学习。

<a id="paper-148326"></a>

## From Collapse to Improvement:  Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources

[官方论文页](https://neurips.cc/virtual/2026/poster/148326) · [作者来源](https://openreview.net/forum?id=yfGxUZj1zT)

- **问题 / 瓶颈** · 混入模型自生成数据可积累偏差。
- **核心创新 / 方法** · 分析下一词预测中真实与合成混合分布的多轮演化。
- **Baseline** · 不同真实混比和样本量设定。
- **Benchmark** · 理论下一词训练及其他模型的仿真。
- **关键结果 / 消融** · 在某些条件下真实信息比例即使下降，适当样本量仍可避免坍塌和恢复目标。
- **适用条件 / 局限** · 依赖新数据确实来自目标分布及分析条件。

**可复用机制** · 对迭代合成数据训练同时扫描混比和批量，不只看单轮损失。

<a id="paper-150917"></a>

## From Denoising to Refining: A Corrective Framework for Vision-Language Diffusion Model

[官方论文页](https://neurips.cc/virtual/2026/poster/150917) · [作者来源](https://openreview.net/forum?id=eOkoZ4QWa0)

- **问题 / 瓶颈** · 早期错误被后续并行解码当作条件并累积。
- **核心创新 / 方法** · 先训练改合成错误，再由专家纠正模型自身草稿训练。
- **Baseline** · 传统离散扩散去噪。
- **Benchmark** · 视觉语言生成的连贯性与事实准确性，具名基准待核。
- **关键结果 / 消融** · 作者报告改善，具体数值与效率开销待核。
- **适用条件 / 局限** · 依赖专家纠正质量。

**可复用机制** · 比较训练纠正人工扰动和纠正自身错误，测错误传播与总解码步数。

<a id="paper-153007"></a>

## From Expert Knowledge to Optimization Modeling: Prototype-Based Data Synthesis and Logical Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/153007) · [作者来源](https://openreview.net/forum?id=OfaHY0TIwp)

- **问题 / 瓶颈** · 从零生成数学模型无法利用已有结构。
- **核心创新 / 方法** · 基于 17 个原型合成保留瓶颈约束的数据，以轨迹排序训练逻辑奖励并用于测试时优化。
- **Baseline** · 同规模模型及大型多智能体方法。
- **Benchmark** · 七个基准及分布外建模任务，测准确率。
- **关键结果 / 消融** · 8B 模型平均 79.9%，作者报告两阶段皆有贡献。
- **适用条件 / 局限** · 未覆盖原型时的泛化边界待核。

**可复用机制** · 对结构化生成任务比较原型增量构造和直接完整生成。

<a id="paper-155254"></a>

## From Experts to Sub-experts: Fine-grained Parameter-Efficient Fine-Tuning for MoE LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/155254) · [作者来源](https://openreview.net/forum?id=760IPZeujm)

- **问题 / 瓶颈** · 整专家更新包含大量低响应通道。
- **核心创新 / 方法** · 联合路由重要性和通道激活选择子专家，缩放学习率和梯度。
- **Baseline** · LoRA 等 PEFT、专家级稀疏微调。
- **Benchmark** · OLMoE、Ling-mini-2.0，领域和通用任务。
- **关键结果 / 消融** · 作者报告更少训练参数下优于对照并保持通用能力。
- **适用条件 / 局限** · 稀疏选择与缩放的独立贡献待核。

**可复用机制** · 固定参数预算比较专家粒度和通道粒度。

<a id="paper-148946"></a>

## From Finding to Linking: Benchmarking and Advancing Cross-Long-Video Reasoning for Multimodal LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/148946) · [作者来源](https://openreview.net/forum?id=u03DysVjOF)

- **问题 / 瓶颈** · 单视频与短视频评测不足以揭示跨长视频检索难度。
- **核心创新 / 方法** · 用类型化绑定图填充证据槽，核验跨视频对应再输出答案。
- **Baseline** · 13 个 MLLM 与适配的长视频方法。
- **Benchmark** · CLoVR-Bench，400 个长视频、2000 对问答。
- **关键结果 / 消融** · 作者报告由局部比较到综合推理表现下降，证据图在跨视频绑定任务获益最大。
- **适用条件 / 局限** · 错误槽规划会漏掉关键证据。

**可复用机制** · 用相同底座对照证据定位误差与跨源绑定错误。
