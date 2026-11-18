# NeurIPS 2026 论文卡 9

[会议索引](README.md)

<a id="paper-149376"></a>

## Neural Field Thermal Tomography: A Differentiable Physics Framework for Non-Destructive Evaluation

[官方论文页](https://neurips.cc/virtual/2026/poster/149376) · [作者来源](https://openreview.net/forum?id=qWyXszanTu)

- **问题 / 瓶颈** · 表面拟合好仍可能不能恢复内部。
- **核心创新 / 方法** · 坐标网络表达扩散率，经隐式热流求解，伴随回传边界误差。
- **Baseline** · 软约束 PINN、体素和经典信号处理。
- **Benchmark** · 合成 3D 与真实热成像，缺陷及深度。
- **关键结果 / 消融** · 摘要称两类恢复均更好。
- **适用条件 / 局限** · 限所测物理模型，精度依赖边界观测。

**可复用机制** · 评估内场而非只看边界误差，另报计算和内存。

<a id="paper-150228"></a>

## Neural Fractional Stochastic Differential Equations

[官方论文页](https://neurips.cc/virtual/2026/poster/150228) · [作者来源](https://openreview.net/forum?id=jqQXTnJOCO)

- **问题 / 瓶颈** · 无记忆 SDE 未必捕捉长期依赖，展开反传占内存。
- **核心创新 / 方法** · 使用可学阶数的 Caputo 模型及离散伴随。
- **Baseline** · 粗糙波动率模型和同架构 Neural SDE。
- **Benchmark** · S&P 500 指数期权，比较隐含波动误差。
- **关键结果 / 消融** · 摘要称在相同校准流程中误差最低。
- **适用条件 / 局限** · 时间网格及数据窗口依赖待核。

**可复用机制** · 在非生物时序上匹配架构、仅调整记忆阶，比较预测和内存。

<a id="paper-155213"></a>

## Neural Galerkin Normalizing Flows for Bayesian Inference of Diffusions with Inaccessible Boundaries

[官方论文页](https://neurips.cc/virtual/2026/poster/155213) · [作者来源](https://openreview.net/forum?id=7Qy5PJB1Db)

- **问题 / 瓶颈** · 逐 MCMC 提案重算前向方程昂贵。
- **核心创新 / 方法** · 用 Galerkin 流近似带点源初值的转移密度，再由观测路径拼接似然。
- **Baseline** · 在线 PDE 计算及反复桥模拟。
- **Benchmark** · 不可达边界的扩散与随机波动率设定。
- **关键结果 / 消融** · 摘要报告离线训练后推断更快。
- **适用条件 / 局限** · 依赖训练参数覆盖和边界正确性。

**可复用机制** · 在留出参数上检查近似似然和后验覆盖。

<a id="paper-151937"></a>

## Neural Garbage Collection: Learning to Forget while Learning to Reason

[官方论文页](https://neurips.cc/virtual/2026/poster/151937) · [作者来源](https://openreview.net/forum?id=WibVOPxZMf)

- **问题 / 瓶颈** · 手工保留规则不知未来推理需要。
- **核心创新 / 方法** · 把候选认知步骤与缓存动作共同用结果回报优化。
- **Baseline** · 完整缓存与既有裁剪规则。
- **Benchmark** · Countdown、AMC、AIME。
- **关键结果 / 消融** · 峰值缓存压 2–3 倍仍强于裁剪基线。
- **适用条件 / 局限** · 训练额外成本和域外鲁棒待核。

**可复用机制** · 对照同预算固定淘汰，测误删内容与最终正确。

<a id="paper-151113"></a>

## Neural Harmonic Measure Operator

[官方论文页](https://neurips.cc/virtual/2026/poster/151113) · [作者来源](https://openreview.net/forum?id=csUQ0IwX0R)

- **问题 / 瓶颈** · 常规算子改变边界后可能失配。
- **核心创新 / 方法** · 用游走退出样本监督谐和测度，Poisson 源项由另一网络处理。
- **Baseline** · 四种神经算子。
- **Benchmark** · MCB-B 三维变几何 Poisson 与二维测试。
- **关键结果 / 消融** · 三维五类均改善，二维有竞争力。
- **适用条件 / 局限** · 依赖椭圆问题分解和几何边界。

**可复用机制** · 固定几何跨边界值及源项测试无需重训的范围。

<a id="paper-149285"></a>

## Neural Modal Decomposition: Architectural Priors from Observables

[官方论文页](https://neurips.cc/virtual/2026/poster/149285) · [作者来源](https://openreview.net/forum?id=rRvz8kblVv)

- **问题 / 瓶颈** · 逐矩阵项回归成本随端口数平方增。
- **核心创新 / 方法** · 学习端口无关极点和成对端口的耦合，再组成响应。
- **Baseline** · 直接回归和 AAA 有理逼近的模态参考。
- **Benchmark** · 射频电磁器件，两端口训练向多端口迁移。
- **关键结果 / 消融** · 报告可预测未见端口数，估得极点与参考吻合。
- **适用条件 / 局限** · 需要适用线性时不变且模态稀疏。

**可复用机制** · 用留出端口验证响应与极点可辨识性。

<a id="paper-155584"></a>

## Neural networks are more modular than single neurons suggest

[官方论文页](https://neurips.cc/virtual/2026/poster/155584) · [作者来源](https://openreview.net/forum?id=4X3mMoAJwr)

- **问题 / 瓶颈** · 单神经元混合响应不意味着没有功能分工。
- **核心创新 / 方法** · 拟合各层级分解并做选择性消融。
- **Baseline** · 单元级模块与无分解。
- **Benchmark** · 视觉、文本和多任务 RNN。
- **关键结果 / 消融** · 子空间可分内容风格、语法语义或下游任务，即使单位重叠。
- **适用条件 / 局限** · 存在分解不等同训练自然边界，消融需同规模。

**可复用机制** · 用双重分离验证两个子空间分别作用不同任务。

<a id="paper-148632"></a>

## Neural Networks With Dense Weights Are Not Universal Approximators

[官方论文页](https://neurips.cc/virtual/2026/poster/148632) · [作者来源](https://openreview.net/forum?id=wIy5W0BG7A)

- **问题 / 瓶颈** · 无限维度或普通普适定理不能覆盖受限权重。
- **核心创新 / 方法** · 结合弱正则引理与消息传递解释构造不可逼近的 Lipschitz 函数。
- **Baseline** · 不约束权重的普适近似。
- **Benchmark** · 受特定权重及输入输出维数限制的 ReLU 理论。
- **关键结果 / 消融** · 存在受限致密网络不能逼近的函数。
- **适用条件 / 局限** · 不能概括为任意全连接网络失去普适性。

**可复用机制** · 在比较稀疏与致密架构时先检查理论约束与预算是否适用。

<a id="paper-154166"></a>

## Neural Neural Scaling Laws

[官方论文页](https://neurips.cc/virtual/2026/poster/154166) · [作者来源](https://openreview.net/forum?id=FmoL6zqWpY)

- **问题 / 瓶颈** · 验证均值掩盖任务特殊的非单调信号。
- **核心创新 / 方法** · 用时序网络外推任务准确率。
- **Baseline** · 逻辑缩放律。
- **Benchmark** · 公开模型检查点、66 个下游任务。
- **关键结果 / 消融** · 平均绝对误差 1.99%，较基线 3.56% 低约 44%。
- **适用条件 / 局限** · 依赖历史任务与检查点覆盖。

**可复用机制** · 按整模型家族和整个任务留出，做数据来源去重。

<a id="paper-151141"></a>

## Neural Operator-based Curriculum Learning for Physics-Informed Neural Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/151141) · [作者来源](https://openreview.net/forum?id=ciNWXOXC8v)

- **问题 / 瓶颈** · 手排难度和直接拷贝权重可能无法传递谱知识。
- **核心创新 / 方法** · 用切线核指导课程，由算子学习跨阶段初始化。
- **Baseline** · 普通 PINN 与手工课程。
- **Benchmark** · 复杂 PDE 测试套件，比较收敛和泛化。
- **关键结果 / 消融** · 摘要称提升明显，数值待核。
- **适用条件 / 局限** · 适用的 PDE 及算子开销待核。

**可复用机制** · 按频谱难度分别消融自动顺序和阶段初始化。

<a id="paper-150584"></a>

## Neural Optimal Transport in Hilbert Spaces

[官方论文页](https://neurips.cc/virtual/2026/poster/150584) · [作者来源](https://openreview.net/forum?id=h673LAeDNM)

- **问题 / 瓶颈** · 目标最优不必得到正确传输映射。
- **核心创新 / 方法** · 证明规则源可恢复 Monge 映射，并分析高斯平滑后的计划一致性。
- **Baseline** · 未平滑半对偶传输。
- **Benchmark** · 奇异的合成任务及无配对时序插补。
- **关键结果 / 消融** · 平滑极限的聚点可解原问题，若干实证表现最好。
- **适用条件 / 局限** · 依赖核及源条件，计划不等同逐点映射。

**可复用机制** · 对比目标和可观测映射误差，并检查平滑尺度。

<a id="paper-153194"></a>

## Neural population tuning statistics as priors for multitask generalization

[官方论文页](https://neurips.cc/virtual/2026/poster/153194) · [作者来源](https://openreview.net/forum?id=N8F8d2c171)

- **问题 / 瓶颈** · 编码精度不能说明对任务族的适配。
- **核心创新 / 方法** · 把大群体调谐统计映射到函数先验，以边际似然刻画适应。
- **Baseline** · 不适应群体。
- **Benchmark** · 函数族理论与海马奖励学习观察。
- **关键结果 / 消融** · 摘要报告适应降低泛化误差，并可解释奖励位置表征变化。
- **适用条件 / 局限** · 理论解释不证明生理因果。

**可复用机制** · 以任务族预测检验表征统计，而非只衡量单刺激编码。

<a id="paper-154120"></a>

## Neural Preconditioned Born Series: A Metric-Matched Framework for Learning-based Preconditioners

[官方论文页](https://neurips.cc/virtual/2026/poster/154120) · [作者来源](https://openreview.net/forum?id=G7pWWaC6g5)

- **问题 / 瓶颈** · 物理残差误差未必与迭代收敛一致。
- **核心创新 / 方法** · 在 Born 预条件坐标学习残差到修正的映射，以同度量定损失。
- **Baseline** · 直接残差学习、经典 CBS。
- **Benchmark** · 非均匀 Helmholtz、反应扩散型及 Newton 系统。
- **关键结果 / 消融** · 相比直接学习最高少 1.9 倍迭代，对 CBS 超过 20 倍。
- **适用条件 / 局限** · 依赖预条件的稳定性和系统范围。

**可复用机制** · 训练损失应匹配迭代器实际使用的几何。

<a id="paper-154337"></a>

## Neural Reconstruction of LiDAR Point Clouds under Jamming Attacks via Full-Waveform Representation and Simultaneous Laser Sensing

[官方论文页](https://neurips.cc/virtual/2026/poster/154337) · [作者来源](https://openreview.net/forum?id=EM3vywy1qY)

- **问题 / 瓶颈** · 下游点输出异常不代表整个传感通道失去信息。
- **核心创新 / 方法** · 用波形级防御模型区分可靠回波，并对照直接点处理。
- **Baseline** · 现有点输出及无恢复路线。
- **Benchmark** · 真实静态与行驶场景的传感恢复。
- **关键结果 / 消融** · 摘要报告车辆恢复率分别 92%、73%。
- **适用条件 / 局限** · 依赖原始波形访问，其他环境与设备需复测。

**可复用机制** · 将传感异常挑战设为分层审计，确认下游丢失的线索是否仍可从上游安全恢复。

<a id="paper-150170"></a>

## Neural Refraction Fields for Image Verification

[官方论文页](https://neurips.cc/virtual/2026/poster/150170) · [作者来源](https://openreview.net/forum?id=k9nUHL1sDu)

- **问题 / 瓶颈** · 只读元数据不一定能发现局部篡改，解析物理签名适用面窄。
- **核心创新 / 方法** · 以场景无关折射模型重建像素对齐参考，比较不一致。
- **Baseline** · 每场景辐射场优化与简化折射。
- **Benchmark** · 图像验证及局部篡改检测。
- **关键结果 / 消融** · 摘要报告训练后可快速高保真重建。
- **适用条件 / 局限** · 需要可信参考来源和校准，不能独立证明真伪。

**可复用机制** · 将内容验真绑定可重建的独立观测，而非只依赖分类器信心。

<a id="paper-149293"></a>

## Neural Scaling Laws in Particle Jets

[官方论文页](https://neurips.cc/virtual/2026/poster/149293) · [作者来源](https://openreview.net/forum?id=rMzU4uxIrE)

- **问题 / 瓶颈** · 仅扩大物理分类器的参数可能进入双下降或数据瓶颈。
- **核心创新 / 方法** · 在不同算力和数据量拟合尺度律，用大样本留出验证。
- **Baseline** · 较小喷注分类器与既有数据。
- **Benchmark** · 粒子喷注分类，另验证 77 亿喷注。
- **关键结果 / 消融** · 摘要报告放大数据后的表现跟随预测，并指出双下降区间。
- **适用条件 / 局限** · 经验规律限于所测任务和预算。

**可复用机制** · 扩规模前先以固定算力和样本两轴找到收益拐点。

<a id="paper-150516"></a>

## Neural Slack Variables for Shape Constraints

[官方论文页](https://neurips.cc/virtual/2026/poster/150516) · [作者来源](https://openreview.net/forum?id=hWUODLVAFM)

- **问题 / 瓶颈** · 只在违反处才有梯度容易造成边界不稳。
- **核心创新 / 方法** · 联训辅助网络表示可行约束量，引导主网络做双侧回归。
- **Baseline** · 单侧罚、互补松弛与硬约束架构。
- **Benchmark** · 单调、低维凸、障碍证书与无套利曲面。
- **关键结果 / 消融** · 摘要报告接近硬约束并适用部分非线性约束。
- **适用条件 / 局限** · 近似训练未必严格全域可行。

**可复用机制** · 先构造可验证的合法目标，再让主模型拟合约束量。

<a id="paper-155319"></a>

## Neural Spectral Capacity: An Architectural Quantity from Network Specification Alone

[官方论文页](https://neurips.cc/virtual/2026/poster/155319) · [作者来源](https://openreview.net/forum?id=6VtpAVw5S8)

- **问题 / 瓶颈** · 同参数或 FLOPs 无法辨别宽深等设计。
- **核心创新 / 方法** · 用随机矩阵谱构造逐层可加分数，以动态规划选结构。
- **Baseline** · 参数、FLOPs 和无训练代理。
- **Benchmark** · 七类模型、FlexiBERT、WikiText-103、LLaMA-7B 压缩。
- **关键结果 / 消融** · 摘要报告同预算排名更相关；动态规划秒级筛选。
- **适用条件 / 局限** · 初始化谱是代理，不能代替真实任务验证。

**可复用机制** · 让架构搜索使用可分解的结构性先验，再对少数候选训练验证。

<a id="paper-154480"></a>

## Neural Statistical Functions

[官方论文页](https://neurips.cc/virtual/2026/poster/154480) · [作者来源](https://openreview.net/forum?id=DHWVdjJrLt)

- **问题 / 瓶颈** · 逐点预测后反复采样估极值或分位耗时。
- **核心创新 / 方法** · 以区间条件统一积分、分位和最大值，用与单点回归的关系作监督。
- **Baseline** · 重复运行单例预测器。
- **Benchmark** · 能量积分、气动分位、碰撞应力极值。
- **关键结果 / 消融** · 摘要报告最多约百倍减少模型评估。
- **适用条件 / 局限** · 稀有区间的校准与统计一致性仍需检验。

**可复用机制** · 高频聚合需求可训练专用统计预测器，并独立验收尾部误差。

<a id="paper-149065"></a>

## Neural Structural Reasoner: A Brain-inspired Architecture for Reasoning over Structured Knowledge

[官方论文页](https://neurips.cc/virtual/2026/poster/149065) · [作者来源](https://openreview.net/forum?id=t8iDmsYS6X)

- **问题 / 瓶颈** · 平坦嵌入难显示拓扑组合。
- **核心创新 / 方法** · 耦合群体联接并维护候选关系路径，按置信并行评分。
- **Baseline** · 嵌入与规则挖掘基线。
- **Benchmark** · 知识图链路预测和隐含关系。
- **关键结果 / 消融** · 摘要报告匹配强基线且训练更高效。
- **适用条件 / 局限** · 路径可读取不保证因果忠实或完全覆盖。

**可复用机制** · 当需要解释规则组合时显式记录关系层级与中间推断。

<a id="paper-154463"></a>

## Neural‑Visual Decoding via Cognitive‑guided Adaptive Blurring and Information‑Constrained Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/154463) · [作者来源](https://openreview.net/forum?id=DP5UdHKCti)

- **问题 / 瓶颈** · 高细节图像特征和低信噪 EEG 难直接对齐。
- **核心创新 / 方法** · 用中心和显著性引导的软模糊、筛选振荡及边界校准。
- **Baseline** · 既有脑图零样本检索。
- **Benchmark** · 同被试和跨被试 Top-1、Top-5。
- **关键结果 / 消融** · 摘要报告两种设置均改善。
- **适用条件 / 局限** · 收集设定与刺激类别限制外推。

**可复用机制** · 让教师目标的空间粒度匹配可观测信号，而非要求弱传感器重建所有细节。

<a id="paper-139374"></a>

## NeuroAtlas: Benchmarking Foundation Models for Clinical EEG and Brain-Computer Interfaces

[官方论文页](https://neurips.cc/virtual/2026/poster/139374) · [作者来源](https://openreview.net/forum?id=U8tvjJbW9U)

- **问题 / 瓶颈** · 仅准确率和专用模型横向比较可能掩盖有限优势。
- **核心创新 / 方法** · 统一四十余个数据和多个任务，并用事件、睡眠分期衍生量等检查。
- **Baseline** · 监督及通用时序基础模型。
- **Benchmark** · NeuroAtlas 42 集、约 26 万小时。
- **关键结果 / 消融** · 专用模型不稳定优于通用骨干，排名随同域数据变化。
- **适用条件 / 局限** · 基准表现不代表临床部署验证。

**可复用机制** · 同时检查领域预训练收益与 downstream 真正关心的任务输出。

<a id="paper-156026"></a>

## NeuroFaith: Evaluating Mechanistic Faithfulness of LLM Free Text Self-Explanation at the Concept Level

[官方论文页](https://neurips.cc/virtual/2026/poster/156026) · [作者来源](https://openreview.net/forum?id=13UKdODUdP)

- **问题 / 瓶颈** · 理由中的概念可能没参与模型预测。
- **核心创新 / 方法** · 从解释提取关键概念，再检验内部概念信号是否影响答案。
- **Baseline** · 行为评估与模块级分析。
- **Benchmark** · 两跳推理和分类，自由文本解释。
- **关键结果 / 消融** · 摘要报告可探测不忠实解释，干预后忠实性改善。
- **适用条件 / 局限** · 依赖概念读出和扰动局部性。

**可复用机制** · 要求每个解释要点给出模型应改变预测的可证伪预期。

<a id="paper-154599"></a>

## NeuroHorizon: Long-Horizon Forward Prediction of Neural Population Activity via Autoregressive Decoding with Hierarchical Memory

[官方论文页](https://neurips.cc/virtual/2026/poster/154599) · [作者来源](https://openreview.net/forum?id=COuiDiirTQ)

- **问题 / 瓶颈** · 教师强制训练掩盖闭环累计漂移。
- **核心创新 / 方法** · 以尖峰事件分词、近期与分段双记忆及调度采样预测。
- **Baseline** · 既有神经活动预测。
- **Benchmark** · 多时域运动皮层、附加运动与视觉皮层迁移。
- **关键结果 / 消融** · 摘要报告多步滚动稳定，优于所比法。
- **适用条件 / 局限** · 跨种群和不同记录尺度需独立验证。

**可复用机制** · 把训练条件逐步换成部署会遇到的模型历史，实测远期偏差。

<a id="paper-148901"></a>

## NeuroInk: Retinomorphic Spiking Sequence Modeling for Handwritten Text Recognition

[官方论文页](https://neurips.cc/virtual/2026/poster/148901) · [作者来源](https://openreview.net/forum?id=uKMBVkBuxL)

- **问题 / 瓶颈** · 重复整帧没有有效时域变化。
- **核心创新 / 方法** · 把墨水粗细证据变成时变电流，用保细节层和列方向 CTC 读出。
- **Baseline** · 重复输入脉冲模型与其他识字路线。
- **Benchmark** · LAM，字符错误率和时步。
- **关键结果 / 消融** · 两步贪心解码下验证 2.4%、测试 2.6% CER。
- **适用条件 / 局限** · 外推受书写方向和字体退化影响。

**可复用机制** · 静态输入进入事件模型时，用时序承载互补证据而非复制帧。

<a id="paper-154231"></a>

## Neuro-Inspired Inverse Learning for Planning and Control

[官方论文页](https://neurips.cc/virtual/2026/poster/154231) · [作者来源](https://openreview.net/forum?id=FF1dzX9agi)

- **问题 / 瓶颈** · 逐步策略短视，反复优化整段轨迹昂贵。
- **核心创新 / 方法** · 训练逆模型生成多步命令，用覆盖更广的数据减少前向模型误导。
- **Baseline** · 离线 RL、扩散规划。
- **Benchmark** · D4RL 三个 Maze2D 和六个 AntMaze 变体。
- **关键结果 / 消融** · 平均约改善 24.2%，推理计算少一到两个数量级。
- **适用条件 / 局限** · 训练覆盖窄会诱发模型误用。

**可复用机制** · 同时评测整段控制的摊销效率和覆盖敏感性，必要时扩大训练状态范围。

<a id="paper-153319"></a>

## Neuro-KE: Knowledge-Guided Interfaces for Semantically Grounded EEG Foundation Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153319) · [作者来源](https://openreview.net/forum?id=MCJdyjyfDw)

- **问题 / 瓶颈** · 重建可保细节却忽略有意义的生理量。
- **核心创新 / 方法** · 以同类描述符形成数值、特征文本及指令标签。
- **Baseline** · 仅重建及仅类别文本。
- **Benchmark** · 三类接口，含 12 集与三骨干。
- **关键结果 / 消融** · 重建预训练对照增 2.60 点平衡准确，标签锚点对照增 2.23 点。
- **适用条件 / 局限** · 部分任务例外，生理描述符不是临床真值。

**可复用机制** · 用便宜可复看的领域指标贯穿表征、文本和问答三层验收。

<a id="paper-153760"></a>

## NeuroMem: A Neuroplastic Memory Framework for Lifelong Agents through Delayed Consolidation

[官方论文页](https://neurips.cc/virtual/2026/poster/153760) · [作者来源](https://openreview.net/forum?id=It0A0c7CHw)

- **问题 / 瓶颈** · 即时写入难区分一次性信息和可迁移经验。
- **核心创新 / 方法** · 从后续交互的延迟效用学保留、晋升、合并或删除。
- **Baseline** · 常规即时或长期记忆方案。
- **Benchmark** · EHRSQL、LoCoMo，成功率、F1 与记忆规模。
- **关键结果 / 消融** · EHRSQL 最多提高 8.7%，LoCoMo F1 至多加 5.2%。
- **适用条件 / 局限** · 延迟反馈必须覆盖候选重用机会。

**可复用机制** · 将记忆录取视为延迟评估，而非把所有短时记录视作长期知识。

<a id="paper-150082"></a>

## Neuromodulated Constrained Autoencoders for Context-Dependent Manifold Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/150082) · [作者来源](https://openreview.net/forum?id=krhi01CVlP)

- **问题 / 瓶颈** · 普通条件拼接和仿射调制会打破原约束。
- **核心创新 / 方法** · 用上下文超网络调节激活斜率与偏置以保持约束。
- **Baseline** · 条件拼接、仿射调制与普通自编码器。
- **Benchmark** · 上下文依赖流形及理论投影性质。
- **关键结果 / 消融** · 给出逐上下文的保证并报告经验验证。
- **适用条件 / 局限** · 输入上下文误差和流形维数变化需查。

**可复用机制** · 把条件适应与迭代不变性都作为验收项。

<a id="paper-149661"></a>

## NeuroRVQ: Multi-Scale Biosignal Tokenization for Generative Foundation Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149661) · [作者来源](https://openreview.net/forum?id=oOiBcvA4rm)

- **问题 / 瓶颈** · 共享时间尺度会丢失高频成分，线性相位误差不尊重周期。
- **核心创新 / 方法** · 用多尺度卷积生成分频表示，以分层残差量化编码并加入相位损失。
- **Baseline** · 通用或单尺度 biosignal tokenizer。
- **Benchmark** · EEG、ECG、EMG 重建和生成表示。
- **关键结果 / 消融** · 摘要提出可适配时序和频谱尺度的结构。
- **适用条件 / 局限** · 相位目标与下游收益的独立对照待查。

**可复用机制** · 分别检查窄频与高频重建，避免用全信号均方误差掩盖时序损失。

<a id="paper-151324"></a>

## Neurosymbolic Object-Centric Learning with Distant Supervision

[官方论文页](https://neurips.cc/virtual/2026/poster/151324) · [作者来源](https://openreview.net/forum?id=bMkCLL1wPH)

- **问题 / 瓶颈** · 既有规则监督常需要预先指定对象。
- **核心创新 / 方法** · 槽编码器给候选存在与类别概率，概率逻辑层对未观察分配边缘化。
- **Baseline** · 假设给出对象或槽不与逻辑层绑定的模型。
- **Benchmark** · 仅全局任务标签的物体关系推断。
- **关键结果 / 消融** · 摘要给出无对象标签的可微监督构造。
- **适用条件 / 局限** · 符号程序质量及枚举扩展成本待查。

**可复用机制** · 用任务级标签和对象级验证拆开监督成本与学习到的语义。

<a id="paper-150943"></a>

## NeuroSynTheos: Learning to accelerate counterexample-guided reactive synthesis modulo theories

[官方论文页](https://neurips.cc/virtual/2026/poster/150943) · [作者来源](https://openreview.net/forum?id=e9NgLNzzGp)

- **问题 / 瓶颈** · 逐条发现恒真式需要昂贵反例分析。
- **核心创新 / 方法** · 以公式抽象语法图预测候选批次，并共享代数模板。
- **Baseline** · CEGRES。
- **Benchmark** · 83 项标准理论反应综合规格。
- **关键结果 / 消融** · 报告求解约 60 项，而旧最佳为 19。
- **适用条件 / 局限** · 依赖训练轨迹及模板不变性，候选仍需形式核验。

**可复用机制** · 将学习用作候选生成，把正确性留给验证器。

<a id="paper-149810"></a>

## Never Go Full Batch: Stochastic TMLE for Large-Scale Debiased Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/149810) · [作者来源](https://openreview.net/forum?id=nBj3s8jbyk)

- **问题 / 瓶颈** · 每次全批波动拟合耗时和耗内存。
- **核心创新 / 方法** · 随机目标化迭代到解的邻域，再用全样本满足经验影响函数条件。
- **Baseline** · 标准全批 TMLE。
- **Benchmark** · 去偏推断的计算、收敛与统计有效性。
- **关键结果 / 消融** · 证明随机阶段进噪声球，少量全批迭代恢复所需根。
- **适用条件 / 局限** · 依赖末段全批可行与统计条件。

**可复用机制** · 将廉价近似阶段和保证有效性的末次校验分开。

<a id="paper-152649"></a>

## New Coresets for Fair Clustering

[官方论文页](https://neurips.cc/virtual/2026/poster/152649) · [作者来源](https://openreview.net/forum?id=RQT8lzmK8J)

- **问题 / 瓶颈** · 一般度量下现有摘要难同时保持公平约束和小空间。
- **核心创新 / 方法** · 将数据与带容量中心写成两个分布，利用运输距离和专门覆盖网分析均匀采样。
- **Baseline** · 标准合并压缩流式框架及此前较大核心集。
- **Benchmark** · 一般度量公平 k-median 的空间和摘要规模。
- **关键结果 / 消融** · 给出关于 k 近线性的核心集和流式空间。
- **适用条件 / 局限** · 保真要求依赖公平与容量定义，运行成本待核实。

**可复用机制** · 按受约束的最优赋值成本验证摘要，而非仅保留无约束距离。

<a id="paper-150055"></a>

## Next Forcing: Causal World Modeling with Multi-Chunk Prediction

[官方论文页](https://neurips.cc/virtual/2026/poster/150055) · [作者来源](https://openreview.net/forum?id=l6yzdsHdX0)

- **问题 / 瓶颈** · 单块目标不直接训练远期动力学。
- **核心创新 / 方法** · 以轻量辅助模块构成跨深度的因果链，近预测为更远的去噪提供特征。
- **Baseline** · 仅下一块监督的自回归视频模型。
- **Benchmark** · 视频动作世界模型的训练、准确性与推理速度。
- **关键结果 / 消融** · 摘要报告训练更快、精度提升且推理加速。
- **适用条件 / 局限** · 远程误差传播、硬件和动作类型差异待查。

**可复用机制** · 比较不同预测间隔的辅助损失，并检查长滚动而非只比单块质量。

<a id="paper-155772"></a>

## Next-Latent Prediction Transformers Learn Compact World Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155772) · [作者来源](https://openreview.net/forum?id=325YSKkc2n)

- **问题 / 瓶颈** · 只做下一词监督允许运行时临时检索而不总结状态。
- **核心创新 / 方法** · 在不改变主架构和推理流程下训练自监督隐态转移。
- **Baseline** · 下一词训练。
- **Benchmark** · 世界状态预测与泛化，理论分析信念状态。
- **关键结果 / 消融** · 理论中隐态收敛到足以预测未来的压缩信念。
- **适用条件 / 局限** · 理论条件和复杂任务实证待查。

**可复用机制** · 将历史压缩程度与长程泛化一起验收，区分状态学习与词预测收益。

<a id="paper-151625"></a>

## NEXUS: Neural Energy Fields for Physically Consistent Contact-Rich 3D Object Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/151625) · [作者来源](https://openreview.net/forum?id=Z9xwHfl47k)

- **问题 / 瓶颈** · 直接预测加速度难组合不同物理作用。
- **核心创新 / 方法** · 构建物体和动态接触图，累加保守标量能量并学习碰撞耗散。
- **Baseline** · 直接轨迹或加速度回归及只保守的 Hamiltonian 网络。
- **Benchmark** · 接触、变形与外力的三维对象动态。
- **关键结果 / 消融** · 摘要提出以同一结构组合多个效应。
- **适用条件 / 局限** · 接触不连续性及跨形态迁移需核实。

**可复用机制** · 分别验收能量守恒和碰撞后的能量损失，避免只看视频拟合。

<a id="paper-150691"></a>

## Nexus: Same Pretraining Loss, Better Downstream Generalization via Common Minima

[官方论文页](https://neurips.cc/virtual/2026/poster/150691) · [作者来源](https://openreview.net/forum?id=gEYdmlnR5G)

- **问题 / 瓶颈** · 平均损失相同可能掩盖不同源最优点相距甚远。
- **核心创新 / 方法** · Nexus 通过提高梯度相似性鼓励数据源间共同极小。
- **Baseline** · AdamW。
- **Benchmark** · 130M 至 3B，比较预训练与域外损失及下游推理。
- **关键结果 / 消融** · 3B 域外损失降 0.012，推理最高改善 15.0%。
- **适用条件 / 局限** · 优化开销和不同语料混合需核。

**可复用机制** · 匹配预训练损失和预算，再按数据源对比下游效果。

<a id="paper-154653"></a>

## NGDB-Zoo: Towards Efficient and Scalable Neural Graph Databases Training

[官方论文页](https://neurips.cc/virtual/2026/poster/154653) · [作者来源](https://openreview.net/forum?id=C1tuC3Hfob)

- **问题 / 瓶颈** · 多种查询形状导致吞吐低。
- **核心创新 / 方法** · 解耦算子和拓扑，动态调度多流并单独加载语义条件。
- **Baseline** · 传统查询级批处理。
- **Benchmark** · 六基准含 ogbl-wikikg2、ATLAS-Wiki，吞吐和 filtered MRR。
- **关键结果 / 消融** · 吞吐为参考的 1.8–6.8 倍，支持百万实体。
- **适用条件 / 局限** · 结构和 I/O 贡献及硬件依赖待核。

**可复用机制** · 分别测算子调度、文本读入和查询类型分布。

<a id="paper-153730"></a>

## NIKA: Efficient Neural Video Representation via Structured Latent Diversity

[官方论文页](https://neurips.cc/virtual/2026/poster/153730) · [作者来源](https://openreview.net/forum?id=JDRlh5OZZs)

- **问题 / 瓶颈** · 复杂解码使每帧恢复慢。
- **核心创新 / 方法** · 组合空间、频谱和时间基，使用轻卷积上采样。
- **Baseline** · NeRV 家族。
- **Benchmark** · UVG，PSNR、帧率和 MAC。
- **关键结果 / 消融** · 33.33 dB、462 FPS、4.5G MAC，MAC 少 39–51 倍。
- **适用条件 / 局限** · GPU 和潜状态储存需一并比较。

**可复用机制** · 固定总容量比较单类潜基扩宽和多类潜基组合。

<a id="paper-153070"></a>

## NINJA: A Navigator–Inspector Joint Architecture for Context-Efficient Issue Localization

[官方论文页](https://neurips.cc/virtual/2026/poster/153070) · [作者来源](https://openreview.net/forum?id=OCikE8Xieh)

- **问题 / 瓶颈** · 单一增长上下文易淹没局部证据。
- **核心创新 / 方法** · 在良性故障分析中分别维护全局材料及局部检查结果。
- **Baseline** · 单上下文问题定位。
- **Benchmark** · 多代码维护基准和多基础模型。
- **关键结果 / 消融** · 摘要称持续超过参考。
- **适用条件 / 局限** · 依赖标注质量，端到端修复未证明。

**可复用机制** · 用自有合成逻辑错误检查文件召回、证据准确与上下文耗时。

<a id="paper-148578"></a>

## NitroBox: Lightning-Fast Sandbox for Large-Scale RL Training

[官方论文页](https://neurips.cc/virtual/2026/poster/148578) · [作者来源](https://openreview.net/forum?id=wmjiv6thuV)

- **问题 / 瓶颈** · 推理提速可能被容器生命周期成本抵消。
- **核心创新 / 方法** · 比较独立隔离实例与复制写入等维护路径。
- **Baseline** · Docker。
- **Benchmark** · 32 并发训练及生命周期微基准。
- **关键结果 / 消融** · 端到端 40.6 到 28.4 小时，任务通过率相同。
- **适用条件 / 局限** · 不能仅凭性能推断隔离完整。

**可复用机制** · 在良性数学环境中同测吞吐和隔离回归，分别报各阶段时间。

<a id="paper-154266"></a>

## NIV: Neural Axis Variations for Variable Font Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/154266) · [作者来源](https://openreview.net/forum?id=F4kv6kdkQw)

- **问题 / 瓶颈** · 独立轴变化难保共同插值连贯。
- **核心创新 / 方法** · 以轴属性嵌入预测轮廓点位移并输出标准可变字体。
- **Baseline** · 手工变体及各轴独立路线，实证基线待核。
- **Benchmark** · 逾百万轴组合，未见字符、风格、CJK 和手写。
- **关键结果 / 消融** · 报告多类跨域泛化。
- **适用条件 / 局限** · 轮廓拓扑变化和多轴极端点需验。

**可复用机制** · 用字体引擎查插值合法，并在不同复杂度字形上评估。

<a id="paper-151699"></a>

## Njord: A Probabilistic Graph Neural Network for Ensemble Ocean Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/151699) · [作者来源](https://openreview.net/forum?id=YgZlTScsDW)

- **问题 / 瓶颈** · 确定性预报无法表示混沌不确定性。
- **核心创新 / 方法** · 潜变量图模型输出多个未来，并以聚类网格适配海岸形状。
- **Baseline** · 确定性海洋学习模型。
- **Benchmark** · OceanBench 全球 0.25 度及波罗的海 2 公里，实测上层变量。
- **关键结果 / 消融** · 全球平均误差最低，海表温度改善最大。
- **适用条件 / 局限** · 校准与极端天气需单报。

**可复用机制** · 同时比较集合覆盖、平均误差及不同网格下空间偏差。

<a id="paper-149843"></a>

## NLD4CO: Neural Langevin Dynamics  for Combinatorial Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/149843) · [作者来源](https://openreview.net/forum?id=mshiN8rReo)

- **问题 / 瓶颈** · 均匀初始化与局部建议在路线类任务慢。
- **核心创新 / 方法** · 有能量模型用热启动，其他任务用一致性表征给联合修正方向。
- **Baseline** · 普通 Langevin 和学习构造。
- **Benchmark** · MIS、MWIS、TSP、CVRP，解质量和速度。
- **关键结果 / 消融** · 摘要称质量改善且时间有竞争力。
- **适用条件 / 局限** · 实例分布及可行性保持待核。

**可复用机制** · 在同时间限下比较热启动贡献与联合修正贡献。

<a id="paper-154182"></a>

## NNCoxKL: Risk-Set Distillation from Probability-Free Prognostic Teachers for Deep Cox Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154182) · [作者来源](https://openreview.net/forum?id=FaX4fXye5X)

- **问题 / 瓶颈** · 直接用原评分依赖其校准与量纲。
- **核心创新 / 方法** · 在每个事件风险集中把顺序映成 Plackett–Luce 分布并做 KL 正则。
- **Baseline** · 内部 Deep Cox 和常规评分迁移。
- **Benchmark** · 临床跨域与受控生存评测，比较区分和校准。
- **关键结果 / 消融** · 摘要报告两类指标均改善。
- **适用条件 / 局限** · 外部顺序错误时有负迁移，未证明临床效用。

**可复用机制** · 单独扰动外部量纲和排序检查不同误差敏感性。

<a id="paper-154832"></a>

## nnTrace: Detecting and Localizing Silent Bugs in Distributed Training

[官方论文页](https://neurips.cc/virtual/2026/poster/154832) · [作者来源](https://openreview.net/forum?id=AcEBYF0OfF)

- **问题 / 瓶颈** · 损失与梯度范数不能及时定位。
- **核心创新 / 方法** · 对齐参考实现和分布式实现张量，并按精度计算容差。
- **Baseline** · 仅监测损失和梯度。
- **Benchmark** · Megatron-LM，多训练配置含 BF16 和 FP8。
- **关键结果 / 消融** · 检出 11 已知和 3 新代码缺陷。
- **适用条件 / 局限** · 需要可信对照以及计算开销。

**可复用机制** · 用自有实现构造数值近似与正常舍入对照，分层定位不匹配。

<a id="paper-154156"></a>

## NOCE-Net: Representation Learning for Battery Operational Context via Nested Sequence Modelling

[官方论文页](https://neurips.cc/virtual/2026/poster/154156) · [作者来源](https://openreview.net/forum?id=FpnVbelG5q)

- **问题 / 瓶颈** · 时长和早期窗口定义会混淆使用方式。
- **核心创新 / 方法** · 循环内 Transformer，循环间 GRU，以等效满循环统一单位。
- **Baseline** · 长序列基线。
- **Benchmark** · 约 700 电池、十集，未见化学与工况零样本。
- **关键结果 / 消融** · 电压 MAPE 13.7%，参数少约 40 倍。
- **适用条件 / 局限** · 依赖通量测量和衰退假设。

**可复用机制** · 跨工况独立比较分段标准，分报反应预测与容量诊断。

<a id="paper-156783"></a>

## No Detail Left Behind: Revisiting Self-Retrieval for Fine-Grained Image Captioning

[官方论文页](https://neurips.cc/virtual/2026/poster/156783) · [作者来源](https://neurips.cc/virtual/2026/poster/156783)

- **问题 / 瓶颈** · 自检索奖励可提高区分却产生幻觉。
- **核心创新 / 方法** · 在人工描述基础上补细节，以相似候选课程训练并测试。
- **Baseline** · 原自检索与多个多模态模型。
- **Benchmark** · RD100、ImageCoDe、TrueMatch。
- **关键结果 / 消融** · 前两者提高 8.9% 和 7.6%；新基准亦超过普通自检索。
- **适用条件 / 局限** · 事实评审误差和迁移待查。

**可复用机制** · 匹配候选难度，分报区分成功率和无图依据细节。

<a id="paper-149024"></a>

## NOFE – Neural Operator Function Embedding

[官方论文页](https://neurips.cc/virtual/2026/poster/149024) · [作者来源](https://openreview.net/forum?id=tQ6I4ZWHFJ)

- **问题 / 瓶颈** · 离散点嵌入可能受采样差异影响。
- **核心创新 / 方法** · 以图核算子学习函数到函数映射，可在任意坐标查询。
- **Baseline** · PCA、t-SNE、UMAP。
- **Benchmark** · 多数据含 ERA5，局部应力、全局结构及拼接误差。
- **关键结果 / 消融** · ERA5 局部应力 0.111，PCA 0.398，但 PCA 全局应力更低。
- **适用条件 / 局限** · 局部与全局权衡依任务。

**可复用机制** · 以交错网格和独立区域验尺度与接缝。

<a id="paper-153751"></a>

## No Free Alignment: Observability-Aware Alignment for Multimodal Heterogeneous Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/153751) · [作者来源](https://openreview.net/forum?id=IyPJb0blHd)

- **问题 / 瓶颈** · 文件或模态缺失时硬对齐会扩散噪声。
- **核心创新 / 方法** · 用跨模态桥接、侧向证据及原型不确定性估支持度，并对对齐调权。
- **Baseline** · 无差别对齐和常见异质训练。
- **Benchmark** · 图文、视听文本、动作和传感等异质数据。
- **关键结果 / 消融** · 报告整体改善，低可观测关系负迁移减少。
- **适用条件 / 局限** · 支持度代理在未知缺失模式下需核。

**可复用机制** · 对低支持关系单报收益和损失，消融各证据通道。

<a id="paper-155659"></a>

## No Free Best-of-Both-Worlds Learning  in Repeated Bilateral Trade

[官方论文页](https://neurips.cc/virtual/2026/poster/155659) · [作者来源](https://openreview.net/forum?id=3yiO50D45L)

- **问题 / 瓶颈** · 独立与一般相依情形的最优遗憾阶不同。
- **核心创新 / 方法** · 用两位反馈建立不可能性、最优折中及带侧信息例外。
- **Baseline** · 独立与依赖估值的极小极大率。
- **Benchmark** · 重复双边交易理论。
- **关键结果 / 消融** · 无侧信息不能同时最优；已知最优同价收益可恢复两种保证。
- **适用条件 / 局限** · 限所设反馈和估值模型。

**可复用机制** · 按可用侧信息分别评估，避免用独立模拟推出普遍结论。

<a id="paper-150634"></a>

## Noise-Level KL Rates for Multi-Marginal Schrödinger Bridge Surrogates

[官方论文页](https://neurips.cc/virtual/2026/poster/150634) · [作者来源](https://openreview.net/forum?id=gdWlrJdblF)

- **问题 / 瓶颈** · 每片边缘匹配不等于三维联合分布吻合。
- **核心创新 / 方法** · 将差异化为标量修正场，按噪声与后验集中量界定差距。
- **Baseline** · 精确多边缘 Schrödinger 桥。
- **Benchmark** · 三维先验和二维边缘的理论。
- **关键结果 / 消融** · 条件下 KL 为 O(Nσ²)，总变差为 O(√Nσ)。
- **适用条件 / 局限** · 限有界潜尺度和噪声对齐假设。

**可复用机制** · 在非生物合成体用独立切片和有耦合切片比较误差率。

<a id="paper-152186"></a>

## Noise-Regularized Training for Learned Image Compression

[官方论文页](https://neurips.cc/virtual/2026/poster/152186) · [作者来源](https://openreview.net/forum?id=UuyALisAVj)

- **问题 / 瓶颈** · 通常只在潜空间模拟量化噪声。
- **核心创新 / 方法** · 将输入噪声用作码率与重建 Jacobian 的正则。
- **Baseline** · 标准 ELIC、DMCI 与 VTM-22.0。
- **Benchmark** · 多码率比较 BD-Rate 和局部 Lipschitz。
- **关键结果 / 消融** · ELIC 降 2.60%；编码器与整链局部 Lipschitz 平均降约 12% 与 8%。
- **适用条件 / 局限** · 噪声大小和域外传输待核。

**可复用机制** · 固定量化与编解码部署，扫噪强并比较质量与码率。

<a id="paper-150670"></a>

## Noise-Started One-Step Image Super-Resolution via LR-Conditioned SplitMeanFlow and GAN Refinement

[官方论文页](https://neurips.cc/virtual/2026/poster/150670) · [作者来源](https://openreview.net/forum?id=gMYBb0YVMl)

- **问题 / 瓶颈** · 直接低清到高清回归容易平均细节。
- **核心创新 / 方法** · 以低分辨率条件和区间分割一致性蒸馏均速，再细化纹理。
- **Baseline** · 多步扩散和确定性一步超分。
- **Benchmark** · 真实超分，感知质量与速度。
- **关键结果 / 消融** · 摘要称一步保有效率且质量更优。
- **适用条件 / 局限** · 新增纹理未必忠于原图，需失真指标。

**可复用机制** · 同一次前向预算比较噪声与确定性起点，分列感知和像素真实性。

<a id="paper-148353"></a>

## Noisy2Latent: Nonparametric Deconvolution and Denoising via Maximum Mean Discrepancy

[官方论文页](https://neurips.cc/virtual/2026/poster/148353) · [作者来源](https://openreview.net/forum?id=yWIThDZBX3)

- **问题 / 瓶颈** · 直接拟合观测会学到噪声，显式似然对复杂密度难算。
- **核心创新 / 方法** · 模拟已知噪声后以 MMD 匹配观测，再用潜密度作经验贝叶斯先验。
- **Baseline** · 经典显式反卷积。
- **Benchmark** · 加性同方差或异方差噪声的理论与估计。
- **关键结果 / 消融** · 普通平滑噪声给多项式率，超平滑仅对数率。
- **适用条件 / 局限** · 依赖噪声模型与 Sobolev 条件。

**可复用机制** · 将模拟测量误差放进损失前向而非直接让生成器拟合原始观测。

<a id="paper-152238"></a>

## Noisy Data is Destructive to Reinforcement Learning with Verifiable Rewards

[官方论文页](https://neurips.cc/virtual/2026/poster/152238) · [作者来源](https://openreview.net/forum?id=UY4F6bcSSP)

- **问题 / 瓶颈** · 污染可把少量监督误判为强化算法有噪声鲁棒性。
- **核心创新 / 方法** · 重新逐项核验标注，固定干净和真正错误数据比较。
- **Baseline** · 基本 GRPO 和改进 RLVR。
- **Benchmark** · 数学推理和真实 Text2SQL 标注噪声。
- **关键结果 / 消融** · 数学低 8% 至 10%，Text2SQL 低 5% 至 12%。
- **适用条件 / 局限** · 不说明所有噪声率或算法均同程度受损。

**可复用机制** · 将噪声类型和真实错误率作为独立实测因素，不使用名义污染比例。

<a id="paper-148301"></a>

## Noisy isomorphism: Robust expressivity of GNNs under structural perturbation

[官方论文页](https://neurips.cc/virtual/2026/poster/148301) · [作者来源](https://openreview.net/forum?id=ysNuUmj7OA)

- **问题 / 瓶颈** · 无噪同构结果只给二元可分，不能预测稳定。
- **核心创新 / 方法** · 要求可识别的噪图比所有其他图更接近源嵌入。
- **Baseline** · 传统同构型判据。
- **Benchmark** · 结构扰动下的节点与图级鲁棒性。
- **关键结果 / 消融** · 可得到认证保证和图级半径，摘要报告能预测实证鲁棒性。
- **适用条件 / 局限** · 依赖噪声度量和可识别边界。

**可复用机制** · 从表征距离的来源间隔而非仅无扰是否可分选图骨干。

<a id="paper-155913"></a>

## No Model Required: Text Entropy Rate Filtering Prevents Iterative Fine-Tuning Collapse

[官方论文页](https://neurips.cc/virtual/2026/poster/155913) · [作者来源](https://openreview.net/forum?id=1rTomFsjg0)

- **问题 / 瓶颈** · 模型概率打分花费额外模型调用，也未必防止模式收缩。
- **核心创新 / 方法** · 以 Kontoyiannis 匹配长度估计文本熵率并筛选。
- **Baseline** · 模型 logprob 过滤和普通迭代。
- **Benchmark** · Llama-3.1-8B 六代 QLoRA 与跨域代理检验。
- **关键结果 / 消融** · 报告唯一三元组增 42%、词表增 30%、重复降 19%。
- **适用条件 / 局限** · 证据只限单谱系，任务真实性需另外评测。

**可复用机制** · 先用模型无关统计检查语料分布，再检验该过滤是否保留正确和困难内容。

<a id="paper-139104"></a>

## No More, No Less: Task Alignment in Terminal Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/139104) · [作者来源](https://openreview.net/forum?id=koHWZUTUlq)

- **问题 / 瓶颈** · 一律接受或拒绝均可在单维评估下显得正常。
- **核心创新 / 方法** · 配对环境任务成功与指令相关性两指标，比较防护前后。
- **Baseline** · 十个前沿代理及六项防护。
- **Benchmark** · TAB 89 个终端基准任务。
- **关键结果 / 消融** · 摘要报告一概抑制无关动作时常同步抑制必需线索。
- **适用条件 / 局限** · 真实部署多来源权限需独立复验。

**可复用机制** · 为防护的误拦和放过各设计对照，避免只提高拒绝率。

<a id="paper-155132"></a>

## Non-Asymptotic Best Policy Identification Guarantees in Online Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/155132) · [作者来源](https://openreview.net/forum?id=8AVpizcVK2)

- **问题 / 瓶颈** · 渐近特征时间忽略到达信息状态所需行动。
- **核心创新 / 方法** · 对 Navigate and Stop 给非渐近界并分解连通性、特征时间曲率等项。
- **Baseline** · NaS 的渐近分析。
- **Benchmark** · 表格 MDP、确定奖励下的固定置信。
- **关键结果 / 消融** · 摘要给出实例结构对样本代价的影响。
- **适用条件 / 局限** · 不覆盖连续状态和任意奖励噪声。

**可复用机制** · 同时预算导航到信息状态的成本与在那里取得的检定信息。

<a id="paper-156022"></a>

## Nonconvex Decentralized Stochastic Bilevel Optimization under Heavy-Tailed Noise

[官方论文页](https://neurips.cc/virtual/2026/poster/156022) · [作者来源](https://openreview.net/forum?id=15yIjsQCrh)

- **问题 / 瓶颈** · 常用有限方差和下层强凸条件限制适用面。
- **核心创新 / 方法** · 使用归一化随机方差缩减更新，直接分析相互依赖的梯度序列。
- **Baseline** · 既有去中心化双层优化。
- **Benchmark** · 重尾非凸的理论及实证。
- **关键结果 / 消融** · 摘要报告无需裁剪仍有收敛保证。
- **适用条件 / 局限** · 归一化及网络混合条件需核实。

**可复用机制** · 当裁剪阈值难选时将尺度分离到更新长度，并单独验证方差。

<a id="paper-151115"></a>

## Non-Expanding Gated Continued Fraction Architecture for Feedforward Layers in Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151115) · [作者来源](https://openreview.net/forum?id=csNiporPZm)

- **问题 / 瓶颈** · 深连分数骨干不稳定且曾需分段训练。
- **核心创新 / 方法** · 设计不扩张的门控层并改写除法计算。
- **Baseline** · 旧连分数、MLP 或 GLU。
- **Benchmark** · GPT-2、Llama-3、Mamba-2 及小型 MoE。
- **关键结果 / 消融** · 摘要报告不分段也可训练更深模型，吞吐更高。
- **适用条件 / 局限** · 数值保护与混合精度支持需核对。

**可复用机制** · 新非线性结构先解决数值运算再比较表达性。

<a id="paper-150395"></a>

## Nonlinear Direct Feedback Alignment for Scalable Backpropagation-Free Training

[官方论文页](https://neurips.cc/virtual/2026/poster/150395) · [作者来源](https://openreview.net/forum?id=iMEeZOdaUi)

- **问题 / 瓶颈** · 固定直接反馈难表达隐藏到输出的非线性。
- **核心创新 / 方法** · 给各层学习随训练更新的轻型反馈子网。
- **Baseline** · 反向传播及线性 DFA。
- **Benchmark** · 残差网络和 ViT；CIFAR、SVHN、ImageNet。
- **关键结果 / 消融** · 摘要报告缩小与反传的差距并保留并行。
- **适用条件 / 局限** · 需计入代理训练和通信。

**可复用机制** · 把反馈路径当作可学习近似，压缩但保留与当前网络对应的非线性。

<a id="paper-155203"></a>

## Non-Linear Pricing Restores Tractability for a Data Seller

[官方论文页](https://neurips.cc/virtual/2026/poster/155203) · [作者来源](https://openreview.net/forum?id=7WJ1EDR5yc)

- **问题 / 瓶颈** · 先验限制线性价格反而使优化难。
- **核心创新 / 方法** · 搜索单调下连续定价，并刻画有限折点的分段线性凸最优解。
- **Baseline** · 线性价格。
- **Benchmark** · 预算受限买方模型与实数模拟。
- **关键结果 / 消融** · 理论多项式求解，折点总数不超过买家数。
- **适用条件 / 局限** · 依赖特定买方效用和预算设定。

**可复用机制** · 先检查过强参数化约束是否排除了既低复杂度又可优化的解结构。

<a id="paper-153235"></a>

## Nonparametric Distribution Matching for Self-Supervised Whole-Slide Image Condensation

[官方论文页](https://neurips.cc/virtual/2026/poster/153235) · [作者来源](https://openreview.net/forum?id=Ml03ueObjM)

- **问题 / 瓶颈** · 固定原型可能丢学习相关的少数组织。
- **核心创新 / 方法** · 在冻结表征上以非参数先验和逐片容积分配实现分布匹配。
- **Baseline** · 已有病理切片压缩。
- **Benchmark** · 五个组织病理数据与临床评估。
- **关键结果 / 消融** · 平均准确提高 7.44%，效率精度折中改善。
- **适用条件 / 局限** · 属于选择的表征视角，标签意义需独立验。

**可复用机制** · 按样本内部多样性改保留规模，而非把每张图切成同数原型。

<a id="paper-156671"></a>

## Nonparametric Estimation of a Factorizable Density using Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/156671) · [作者来源](https://neurips.cc/virtual/2026/poster/156671)

- **问题 / 瓶颈** · 环境维数高时传统非参数估计样本需求大。
- **核心创新 / 方法** · 用稀疏共享权重构造生成估计，并分析全变差率。
- **Baseline** · 一般高维密度估计及理论下界。
- **Benchmark** · 可因子分解密度的理论。
- **关键结果 / 消融** · 适当假设下达到 minimax 率。
- **适用条件 / 局限** · 因子结构假设需独立验证。

**可复用机制** · 检测目标的交互阶数后再决定是否采用可共享的低维估计。

<a id="paper-156041"></a>

## Nonparametric In-Context Learning under Growing Geometric Complexity: Minimax Optimality and Local Geometry-Adaptivity of Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/156041) · [作者来源](https://openreview.net/forum?id=0re6u4E4X8)

- **问题 / 瓶颈** · 不同局部维度的任务难度不能由统一环境维数概括。
- **核心创新 / 方法** · 线性注意力先几何预处理，再实现各坐标图的局部多项式近似。
- **Baseline** · 切空间 oracle 与 minimax 下界。
- **Benchmark** · 几何复杂度递增的非参数回归。
- **关键结果 / 消融** · 在规定模型类上达到聚合 minimax 率。
- **适用条件 / 局限** · 理论架构不证明实际基础模型学到同一程序。

**可复用机制** · 按几何分区汇总误差，避免高样本量易区域掩盖稀少难区。

<a id="paper-140061"></a>

## No One Knows the State-of-the-Art in Geospatial Foundation Models

[官方论文页](https://neurips.cc/virtual/2026/poster/140061) · [作者来源](https://openreview.net/forum?id=U9fAHB63gc)

- **问题 / 瓶颈** · 相同论文标签并不意味着复现指标相同。
- **核心创新 / 方法** · 审计论文、基线来源、权重发布和训练配置。
- **Baseline** · 不同发表结果的交叉对照。
- **Benchmark** · 152 篇遥感研究。
- **关键结果 / 消融** · 46 处同模型基准协议差至少十点，39% 未发权重。
- **适用条件 / 局限** · 审计不产生新的统一排行榜。

**可复用机制** · 验收排名时注明复制还是实跑并测方差，分离算法和数据带来的影响。

<a id="paper-155864"></a>

## No Pose, No Problem in 4D: Feed-Forward Dynamic Gaussians from Unposed Multi-View Videos

[官方论文页](https://neurips.cc/virtual/2026/poster/155864) · [作者来源](https://openreview.net/forum?id=2KlxKfG6ly)

- **问题 / 瓶颈** · 联合学习完整三维运动缺可靠监督。
- **核心创新 / 方法** · 用伪光流监督像面分量，双向时空融合并以视角相关透明度缓解错位。
- **Baseline** · 前向静态或动态方法、逐场景优化。
- **Benchmark** · 四个动态多视图基准。
- **关键结果 / 消融** · 摘要报告优于先前前向法，追加优化后超过所比逐场景方法。
- **适用条件 / 局限** · 依赖光流在遮挡和移动背景中质量。

**可复用机制** · 选可直接从较便宜证据监督的分量，再间接恢复难观测坐标。

<a id="paper-139532"></a>

## NORA: Evaluating Grounded Reasonableness in Visual First-person Normative Action Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/139532) · [作者来源](https://openreview.net/forum?id=KOCSWLuBCV)

- **问题 / 瓶颈** · 从固定选项选对并不证明能自行提出并证成动作。
- **核心创新 / 方法** · 对开放候选要求事实、理由和动作组成支持图。
- **Baseline** · 12 个模型及直接、审议和结构提示。
- **Benchmark** · NoRA 1,420 个第一视角片段。
- **关键结果 / 消融** · 摘要报告模型常能找合理动作与事实，却较弱于将两者正确绑定。
- **适用条件 / 局限** · 合理标准依赖标注及文化情境。

**可复用机制** · 将行为许可和可见证据的绑定单列，防止评估偏爱高说服力措辞。

<a id="paper-154595"></a>

## No-Regret Caching with Delayed Hits

[官方论文页](https://neurips.cc/virtual/2026/poster/154595) · [作者来源](https://openreview.net/forum?id=CQ5tByxuD8)

- **问题 / 瓶颈** · 请求可能命中仍在下载条目，频次不反映阻塞时延。
- **核心创新 / 方法** · 对随机和对抗到达定义延迟影子成本，分别使用置信和扰动预测方法。
- **Baseline** · 经典确定策略与随机 Marker。
- **Benchmark** · 合成和真实请求轨迹，时延和遗憾。
- **关键结果 / 消融** · 现有方法可线性遗憾；摘要报告新策略次线性且时延改善。
- **适用条件 / 局限** · 结论依赖所设抓取和突发模型。

**可复用机制** · 缓存记录下载完成时间与并发等待，避免命中统计掩盖服务成本。

<a id="paper-151008"></a>

## Normalized Architectures are Natively 4-Bit

[官方论文页](https://neurips.cc/virtual/2026/poster/151008) · [作者来源](https://openreview.net/forum?id=dcb94zxXYq)

- **问题 / 瓶颈** · 低精度尾量化通常需额外干预。
- **核心创新 / 方法** · 用单位球约束权重和表示，分析点积信号相关与量化噪声。
- **Baseline** · 标准骨干及带额外量化校正。
- **Benchmark** · 1.2B 稠密和最高 30B 混合 MoE。
- **关键结果 / 消融** · 摘要报告稳定端到端 NVFP4 训练，无需部分常见干预。
- **适用条件 / 局限** · 依赖所测格式与归一化架构。

**可复用机制** · 把表征分布的数值稳定性作为架构设计变量，而非只当部署后处理。

<a id="paper-155654"></a>

## Normalized Friedkin–Johnsen Opinion Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/155654) · [作者来源](https://openreview.net/forum?id=416O82L9GQ)

- **问题 / 瓶颈** · 行随机传播会造成结构性影响偏差。
- **核心创新 / 方法** · 以规范化拉普拉斯替代传统邻居矩阵，分析平衡与均衡。
- **Baseline** · 经典 Friedkin–Johnsen。
- **Benchmark** · 大规模网络的收敛与影响度。
- **关键结果 / 消融** · 摘要报告结构平衡性质及可扩展计算。
- **适用条件 / 局限** · 社会含义受模型与观测假设限制。

**可复用机制** · 做群体传播分析时先对度数驱动的偏差作敏感性检验。

<a id="paper-150821"></a>

## Normalized SGD in the Convex Regime: First High-Probability Guarantees and Momentum Extension

[官方论文页](https://neurips.cc/virtual/2026/poster/150821) · [作者来源](https://openreview.net/forum?id=f322xYHDgN)

- **问题 / 瓶颈** · 归一化随机梯度会引入偏差，不能直接用普通 SGD 的证明。
- **核心创新 / 方法** · 证明 mini-batch 归一化更新的偏差界，并分析加动量时的高概率收敛。
- **Baseline** · 无动量归一化 SGD 及确定性归一化更新。
- **Benchmark** · 光滑凸优化及有界中心矩的重尾噪声；函数值与查询复杂度。
- **关键结果 / 消融** · 给出有无动量两种设定的高概率收敛界。
- **适用条件 / 局限** · 结论受凸性、矩条件、批量和步长要求限制。

**可复用机制** · 分别报告方向估计偏差和抗尺度收益。

<a id="paper-148856"></a>

## Normalizing Trajectory Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148856) · [作者来源](https://openreview.net/forum?id=ueBUOgdmxI)

- **问题 / 瓶颈** · 粗时间步不是简单高斯去噪，常见蒸馏失去似然。
- **核心创新 / 方法** · 每步使用浅可逆块，跨轨迹预测可并行，并由轨迹分数自蒸馏。
- **Baseline** · 现有少步文生图与流匹配初始化。
- **Benchmark** · 文生图质量与四步采样。
- **关键结果 / 消融** · 摘要报告四步匹配或优于基线，原模型保留精确轨迹似然。
- **适用条件 / 局限** · 精确似然是原轨迹模型性质，蒸馏后是否同时保留需查。

**可复用机制** · 将拟合粗步转移及推理蒸馏视为两个可分别验证的阶段。

<a id="paper-152750"></a>

## Norm Anchors Make Model Edits Last

[官方论文页](https://neurips.cc/virtual/2026/poster/152750) · [作者来源](https://openreview.net/forum?id=QbwOoMKB05)

- **问题 / 瓶颈** · 求解的值向量与已编辑 MLP 权重互相放大，可能积累到崩溃。
- **核心创新 / 方法** · 逐次更新前将值向量缩放到原模型的参考范数。
- **Baseline** · 常规定位编辑及仅限制单次更新的方案。
- **Benchmark** · 多主干、编辑器和编辑数据，测长期成功及单次效果。
- **关键结果 / 消融** · 编辑时域增长逾四倍，摘要报告长期效果平均改善 72.2%。
- **适用条件 / 局限** · 参考范数取法、严重邻域干扰和域外修改待查。

**可复用机制** · 画出编辑次数对参数和值的范数曲线，区分单次步幅和跨步正反馈。

<a id="paper-151918"></a>

## NormLift: From Lifted Features To Semantic Reliability In 3D Gaussian Splatting

[官方论文页](https://neurips.cc/virtual/2026/poster/151918) · [作者来源](https://openreview.net/forum?id=WvJHXxwn2e)

- **问题 / 瓶颈** · 传统渲染推导没有解释三维空间中的余弦检索。
- **核心创新 / 方法** · 最大化球面余弦对齐得到归一化加权特征，将范数分解为视图内与视图间一致性。
- **Baseline** · 通常反投影加权和及余弦匹配。
- **Benchmark** · 开放词表三维场景理解，考察语义及多视角支持。
- **关键结果 / 消融** · 摘要给出闭式解与视角支持校准。
- **适用条件 / 局限** · 支持不足时范数需校准，实证增益需核实。

**可复用机制** · 不要把归一化丢掉的尺度全当无关，先测试它是否预测多视图一致性。

<a id="paper-154390"></a>

## NorSA: Accelerating LLM Decoding via Normalized Sparse Activation

[官方论文页](https://neurips.cc/virtual/2026/poster/154390) · [作者来源](https://openreview.net/forum?id=DvzLG9N5Dx)

- **问题 / 瓶颈** · 固定独立同分布假设忽略上下文和相关特征。
- **核心创新 / 方法** · 结合去相关旋转与动态阈值，不需重训。
- **Baseline** · 已有免训练稀疏激活和稠密模型。
- **Benchmark** · LLaMA、Mistral、Qwen；困惑度、任务及解码时间。
- **关键结果 / 消融** · LLaMA3-8B 在 50% 稀疏下离稠密困惑度差 0.44，解码加速 1.32 倍。
- **适用条件 / 局限** · 速度依赖旋转和稀疏算子硬件成本。

**可复用机制** · 在同稀疏率下同时验收质量和真实延迟，检查相关性是否改变保留维度。

<a id="paper-148883"></a>

## Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148883) · [作者来源](https://openreview.net/forum?id=uTd0fqHftX)

- **问题 / 瓶颈** · 成功率不能区分根据场景重算还是重放熟悉轨迹。
- **核心创新 / 方法** · 在同场景和不同任务之间替换动作专家激活，并测试语言信号及特征池化。
- **Baseline** · 六类策略，含无语言 ACT。
- **Benchmark** · LIBERO、MetaWorld、SimplerEnv、ALOHA，逾 42 万滚动。
- **关键结果 / 消融** · π₀.₅、X-VLA 中供体运动复现率 99.6%、99.8%；部分信号绑定绝对工作区。
- **适用条件 / 局限** · 因果插入并不等同模型自然工作路径，其他构型需查。

**可复用机制** · 用姿态和目标位置微扰测试策略是以坐标模板还是视觉闭环完成动作。

<a id="paper-153476"></a>

## Not All Layers Are Equal in Image-to-Video Transfer

[官方论文页](https://neurips.cc/virtual/2026/poster/153476) · [作者来源](https://openreview.net/forum?id=L509wfhr0h)

- **问题 / 瓶颈** · 统一按层加时序模块忽略已有特征深度结构。
- **核心创新 / 方法** · 用同预训练范式视频模型估计从空间到时间敏感的转折点，前后选不同适配器。
- **Baseline** · 全层统一部署。
- **Benchmark** · 四个细动作基准、两种预训练范式，精度、参数和时间。
- **关键结果 / 消融** · 摘要报告精度最高改善 11.8%，参数少 29–48%，推理最多快约 10%。
- **适用条件 / 局限** · 选择边界需参照视频模型，迁移到其他范式待核实。

**可复用机制** · 选适配器前先扫描深度敏感性，而非只扩大适配参数。

<a id="paper-151931"></a>

## Not All Routing Drift Is Harmful: Trust-Region Projection for Class-Incremental Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151931) · [作者来源](https://openreview.net/forum?id=WklS219u5L)

- **问题 / 瓶颈** · 小漂移有时无害或有利，统一拉回会过度限制。
- **核心创新 / 方法** · 输入的路由以类级锚作 KL 信赖区，仅将过大偏差投影回去。
- **Baseline** · 无约束路由及完全稳定化。
- **Benchmark** · 预训练模型 MoE 类增量，按样本路由变化和遗忘。
- **关键结果 / 消融** · 样本分析显示大漂移解释多数退化，小漂移可稳定或改善。
- **适用条件 / 局限** · 锚构建和新类别的真实路由归属待查。

**可复用机制** · 先按漂移幅度统计性能，把修正预算集中在坏尾部。

<a id="paper-139654"></a>

## Not All Spines Are Created Equal: How CT Segmenters Fail on Lumbosacral Transitional Vertebrae

[官方论文页](https://neurips.cc/virtual/2026/poster/139654) · [作者来源](https://openreview.net/forum?id=D8yRWDAGQF)

- **问题 / 瓶颈** · 总体分割指标会掩盖一个椎体的整体标签错位。
- **核心创新 / 方法** · 按过渡脊椎分层，以交界窗口 DSC 和体素混淆查错位。
- **Baseline** · TotalSegmentator 及既有标注基准。
- **Benchmark** · 逾千份 CT，按变体分层，测交界和逐类 DSC。
- **关键结果 / 消融** · 所报任意过渡型病例的交界 DSC 低 29 点，特定变体缺 L6 时标签整体偏移。
- **适用条件 / 局限** · 异体变体样本有限，不能从数字确定临床风险。

**可复用机制** · 对罕见结构变化单独考核编号稳定性，不只抽取整体分割平均值。

<a id="paper-151378"></a>

## Not All Tasks Quantize Equally: Fisher-Guided Quantization for Visual Geometry Transformer

[官方论文页](https://neurips.cc/virtual/2026/poster/151378) · [作者来源](https://openreview.net/forum?id=b31hQvoPCd)

- **问题 / 瓶颈** · 同一视觉几何骨干的不同输出受误差影响不同。
- **核心创新 / 方法** · 以对角 Fisher 估敏感度，纳入可学仿射变换。
- **Baseline** · 现有 VGGT 后训练量化。
- **Benchmark** · 相机姿态、点图、深度及 4 位设置。
- **关键结果 / 消融** · 摘要报告最高相对改善 39%。
- **适用条件 / 局限** · 其他骨干和校准数据待核。

**可复用机制** · 逐任务报告相对浮点损失，不只取总均值。

<a id="paper-152065"></a>

## Not All Tokens Should Be Treated Equally: Context Credits Reassignment

[官方论文页](https://neurips.cc/virtual/2026/poster/152065) · [作者来源](https://openreview.net/forum?id=VjXxG2aN7k)

- **问题 / 瓶颈** · 统一优势可能强化文本先验。
- **核心创新 / 方法** · 按词元和轨迹的视觉接地估计做两级调权。
- **Baseline** · 标准统一信用和随机重权。
- **Benchmark** · 十种数学及通用多模态测试，另做视觉归因。
- **关键结果 / 消融** · 比对应算法更优，额外耗时小于 3%。
- **适用条件 / 局限** · 依赖视觉相关代理的有效性。

**可复用机制** · 同时测图像干预敏感性及准确率，跟等算力随机权重比较。

<a id="paper-152109"></a>

## Not all uncertainty is alike: volatility, stochasticity, and exploration

[官方论文页](https://neurips.cc/virtual/2026/poster/152109) · [作者来源](https://openreview.net/forum?id=VSnGy8znmQ)

- **问题 / 瓶颈** · 二者增加后验不确定性，但其信息价值不同。
- **核心创新 / 方法** · 用高斯状态空间老虎机推导噪声影响，并构造 CAUSE 奖励。
- **Baseline** · 常规探索和逐臂 Gittins。
- **Benchmark** · 异质噪声及变化环境控制实验。
- **关键结果 / 消融** · 波动提高探索，观测随机性抑制；方法超过参考。
- **适用条件 / 局限** · 模型假设与实际噪声可分性待核。

**可复用机制** · 分别改变过程噪声和观测噪声，检测探索率响应。

<a id="paper-152586"></a>

## NoTA: Normalized Tensor Adaptation for Parameter-Efficient Continual Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/152586) · [作者来源](https://openreview.net/forum?id=Rzivs8kzM2)

- **问题 / 瓶颈** · 逐任务更新稳定仍可能累计漂移。
- **核心创新 / 方法** · 以 MPO 压缩更新，对合并结果归一，另设分层调制。
- **Baseline** · 矩阵适配与逐任务归一。
- **Benchmark** · 无回放类增量训练。
- **关键结果 / 消融** · 摘要报告表现改善，理论遗忘界与任务数无关。
- **适用条件 / 局限** · 具体界和存储增长待核。

**可复用机制** · 按任务长度分组检查更新范数与旧类准确率。

<a id="paper-139439"></a>

## Not Another Text Benchmark: Putting the “Visual" Back in Visual Question Answering for Large Video Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139439) · [作者来源](https://openreview.net/forum?id=Pm7KDlF851)

- **问题 / 瓶颈** · 文字多选可能低估视觉推理缺口。
- **核心创新 / 方法** · 分别构造帧检索、未来预测和记忆变形的视觉测试。
- **Baseline** · 文字多选与若干视频模型。
- **Benchmark** · 三项视觉测试。
- **关键结果 / 消融** · 先进模型使用视觉查询时仍显弱。
- **适用条件 / 局限** · 不同模态难度需匹配。

**可复用机制** · 对同场景配视觉和文本选择，报告两者差距。

<a id="paper-149631"></a>

## Not Every Image Teaches Vision: Visual-Necessity-Gated Continual Learning for Multimodal Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149631) · [作者来源](https://openreview.net/forum?id=odMdim806d)

- **问题 / 瓶颈** · 图像存在不表明它提供监督。
- **核心创新 / 方法** · 对比真图和空图的目标似然，将梯度分流到语言、视觉和校准路径。
- **Baseline** · 普通持续微调。
- **Benchmark** · CoIN、MLLM-CL 和 UCIT 式序列。
- **关键结果 / 消融** · 报告平均、最终得分及视觉记忆保持改善。
- **适用条件 / 局限** · 空图选择和图文偏差需核。

**可复用机制** · 按视觉必要性分桶，并用真实图遮蔽做校准验证。

<a id="paper-155810"></a>

## Not Every Rubric Teaches Equally: Policy-Aware Rubric Rewards for RLVR

[官方论文页](https://neurips.cc/virtual/2026/poster/155810) · [作者来源](https://openreview.net/forum?id=2itEcLBhzr)

- **问题 / 瓶颈** · 部分指标已饱和或达不到，对当下学习没区分度。
- **核心创新 / 方法** · 保留人工权重和类别平衡，将组内训练压力分给可区分轨迹的项目。
- **Baseline** · 静态标准加权 GRPO。
- **Benchmark** · 两个图文或文本数据，各三个策略。
- **关键结果 / 消融** · 33 项中 27 项领先，到同平台少 3–4 倍步骤。
- **适用条件 / 局限** · 动态权重的长期目标偏差待核。

**可复用机制** · 记录训练与评测两组权重，并监控每条标准的通过率。

<a id="paper-153822"></a>

## Not Just Oversmoothing: Detecting Echo Chamber Effect in Graph Neural Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/153822) · [作者来源](https://openreview.net/forum?id=IT1grxElZr)

- **问题 / 瓶颈** · 全局指标会掩盖社区内先坍缩。
- **核心创新 / 方法** · 按成员关系分层距离，用独立社区内外聚合缓解。
- **Baseline** · 常规防过平滑与多种图骨干。
- **Benchmark** · 同配和异配图，按社区标签一致度测试。
- **关键结果 / 消融** · 社区与类别相合时坍缩有时有利，反之损害；CASP 改善表现。
- **适用条件 / 局限** · 依赖社区定义和标签结构。

**可复用机制** · 同时报告两种距离及分类，避免将一切平滑视作同一问题。

<a id="paper-150146"></a>

## Not Only Where, But When: Temporal Scheduling for RLVR

[官方论文页](https://neurips.cc/virtual/2026/poster/150146) · [作者来源](https://openreview.net/forum?id=kLm5BZHcSw)

- **问题 / 瓶颈** · 固定重权难兼顾异质行为。
- **核心创新 / 方法** · 先强化轨迹中目标词元，再向全面优化衰减，按轨迹百分位分组。
- **Baseline** · 固定词元加权及普通 RLVR。
- **Benchmark** · 数学和通用推理。
- **关键结果 / 消融** · 摘要报告持续增益与更稳定策略熵。
- **适用条件 / 局限** · 日程与数据难度跨域待核。

**可复用机制** · 等计算比较固定和递减日程，并同时看熵与正确。

<a id="paper-139061"></a>

## No Triangulation Without Representation: Generalization in Topological Deep Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/139061) · [作者来源](https://openreview.net/forum?id=nVgjwC8P84)

- **问题 / 瓶颈** · 原数据上的高分不证明对同一拓扑不同离散化可泛化。
- **核心创新 / 方法** · 扩充三角剖分表示及细化协议，控制模型输入特征。
- **Baseline** · GNN 和高阶消息传递。
- **Benchmark** · MANTRA 扩展及分辨率变化。
- **关键结果 / 消融** · 匹配表示后两类均可饱和原基准；对组合结构外未见泛化证据。
- **适用条件 / 局限** · 只覆盖特定流形和细化。

**可复用机制** · 将拓扑类别的保持与离散网格变化正交化。

<a id="paper-149430"></a>

## Not Suppressing or Purifying: Backdoor Containment via Expert Quarantine and Shutdown in LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/149430) · [作者来源](https://openreview.net/forum?id=q7PGR1UITf)

- **问题 / 瓶颈** · 整体权重修复未必能分离问题机制。
- **核心创新 / 方法** · 评估隔离和停用策略的部署效果，仅讨论防御验收。
- **Baseline** · 已有整体过滤与修复。
- **Benchmark** · 两类任务、四模型家族的受控测试。
- **关键结果 / 消融** · 摘要报告风险行为显著减少，多数常规能力保留。
- **适用条件 / 局限** · 隔离是否完整依赖所测环境。

**可复用机制** · 以自有模拟缺陷验证风险减少并测试对正常输入的影响。

<a id="paper-151837"></a>

## Not Too Generative, Not Too Discriminative: The Human Alignment Sweet Spot

[官方论文页](https://neurips.cc/virtual/2026/poster/151837) · [作者来源](https://openreview.net/forum?id=XYmvp2YQdC)

- **问题 / 瓶颈** · 架构与数据差异容易混淆目标影响。
- **核心创新 / 方法** · 用联合能量模型固定结构并连续调混合系数。
- **Baseline** · 纯生成和纯判别端点。
- **Benchmark** · 六个人类对齐测评，含相似、形纹冲突和属性。
- **关键结果 / 消融** · 中间区域更常达到最对齐结果。
- **适用条件 / 局限** · 可能不适用于不同架构预算。

**可复用机制** · 以同数据和模型扫混合系数，分别报告辨别与感知。

<a id="paper-151525"></a>

## NoTVLA: Semantics-Preserving Robot Adaptation via Narrative Action Interfaces

[官方论文页](https://neurips.cc/virtual/2026/poster/151525) · [作者来源](https://openreview.net/forum?id=a0zV7TNKuT)

- **问题 / 瓶颈** · 稠密监督可能削弱预训练语义。
- **核心创新 / 方法** · 从示范抽语义路点，配视觉锚和深度，再确定性解码轨迹。
- **Baseline** · 密集动作监督与匹配骨干。
- **Benchmark** · 语义留存、组合任务、相机和深度扰动。
- **关键结果 / 消融** · 摘要称在评任务之外应加入语义保真。
- **适用条件 / 局限** · 低级控制可行性与实体安全待核。

**可复用机制** · 在低风险模拟中分测成功、语言泛化和轨迹执行。

<a id="paper-139689"></a>

## NPCBench: A Clinical Apprenticeship Benchmark for Guideline-Constrained Care-Pathway Reasoning in Nasopharyngeal Carcinoma

[官方论文页](https://neurips.cc/virtual/2026/poster/139689) · [作者来源](https://openreview.net/forum?id=AVTJEREEah)

- **问题 / 瓶颈** · 静态问题难测状态更新和持续一致。
- **核心创新 / 方法** · 将组成任务与完整合成案例对照，按证据、状态及后续选择评分。
- **Baseline** · 30 个被测模型及组件题。
- **Benchmark** · 4,077 阶段问题、25 个完整案例。
- **关键结果 / 消融** · 局部强不必然迁移到案例级表现。
- **适用条件 / 局限** · 离线结果不能当临床有效性。

**可复用机制** · 保持证据条件同时比较分步评分与序列一致性。

<a id="paper-155156"></a>

## NP-LoRA: Null Space Projection for Subject-Style LoRA Fusion

[官方论文页](https://neurips.cc/virtual/2026/poster/155156) · [作者来源](https://openreview.net/forum?id=7ruWsRZRGX)

- **问题 / 瓶颈** · 简单加权可能令相互冲突方向强化。
- **核心创新 / 方法** · 用风格主方向定义内容低秩更新的软补空间投影。
- **Baseline** · 线性相加、硬投影和强融合基线。
- **Benchmark** · 多个预训练主题与风格 LoRA 对。
- **关键结果 / 消融** · 摘要称两种要求的平衡改善。
- **适用条件 / 局限** · 身份、风格强度与投影系数会交互。

**可复用机制** · 扫投影强度分别测两类保真。

<a id="paper-152954"></a>

## NPUsper: Eliminating Redundant Computation for Real-Time Whisper on Mobile NPUs

[官方论文页](https://neurips.cc/virtual/2026/poster/152954) · [作者来源](https://openreview.net/forum?id=P8hKTBfUd9)

- **问题 / 瓶颈** · 长填充重复计算，逐词图派发昂贵。
- **核心创新 / 方法** · 以跨注意时间特征判别无依据词元，并按固定步展开 NPU 图。
- **Baseline** · 现有流式 Whisper。
- **Benchmark** · 移动 NPU 的词延迟、首词、功耗和转录准确。
- **关键结果 / 消融** · 词延迟最多降 4.84 倍，首词 33.2 倍。
- **适用条件 / 局限** · 不同设备、噪声和语言需核。

**可复用机制** · 分别关闭重叠缩减与图展开，验时延及末尾漏词。

<a id="paper-153399"></a>

## NRF-GS: Neural Residual Fields for Expressive and Compact Gaussian Splatting

[官方论文页](https://neurips.cc/virtual/2026/poster/153399) · [作者来源](https://openreview.net/forum?id=LfX2iMIYnO)

- **问题 / 瓶颈** · 低阶球谐难表达镜面细节，常靠增点补偿。
- **核心创新 / 方法** · 每点保留漫反射和轻特征，全局 MLP 预测随视角变化的残差。
- **Baseline** · 标准 3DGS 球谐。
- **Benchmark** · 不同场景渲染，比较点数与质量。
- **关键结果 / 消融** · 点数最多减半且质量持平或更高。
- **适用条件 / 局限** · MLP 实时成本和外推新视图待核。

**可复用机制** · 同内存分开比较几何和反射误差。

<a id="paper-151078"></a>

## NTK Regression under dual power-law model: Deterministic Equivalents via SDE and PDE Methods

[官方论文页](https://neurips.cc/virtual/2026/poster/151078) · [作者来源](https://openreview.net/forum?id=d7UcR23Mnc)

- **问题 / 瓶颈** · 各向同性 NTK 理论不能代表双幂律数据。
- **核心创新 / 方法** · 结合随机矩阵及随机微积分推导信号加权预解式。
- **Baseline** · 各向同性与无限宽 NTK。
- **Benchmark** · 高维同比例增长的回归理论。
- **关键结果 / 消融** · 给出偏差方差分解及宽度数据联合风险率。
- **适用条件 / 局限** · 需要指定谱和目标条件。

**可复用机制** · 在等预算下改变目标和输入谱相对衰减，检验实际风险斜率。
