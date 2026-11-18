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

<a id="paper-155075"></a>

## NuMuon: Nuclear-Norm-Constrained Muon for Compressible LLM Training

[官方论文页](https://neurips.cc/virtual/2026/poster/155075) · [作者来源](https://openreview.net/forum?id=8fDXAcnATc)

- **问题 / 瓶颈** · 全秩更新的 Muon 权重结构未明。
- **核心创新 / 方法** · 对更新方向加核范数约束。
- **Baseline** · 原 Muon 与常见压缩。
- **Benchmark** · 十亿参数级语言模型。
- **关键结果 / 消融** · 摘要报告压缩后质量改善并保留收敛。
- **适用条件 / 局限** · 依赖矩阵谱和后续压缩方法。

**可复用机制** · 即使更新满秩，也应直接测权重有效秩，再决定训练正则。

<a id="paper-139335"></a>

## nuReasoning: A Reasoning-Centric Dataset and Benchmark for Long-Tail Autonomous Driving

[官方论文页](https://neurips.cc/virtual/2026/poster/139335) · [作者来源](https://openreview.net/forum?id=WDTaPI01Fw)

- **问题 / 瓶颈** · 会回答驾驶问题不等于规划更好。
- **核心创新 / 方法** · 用空间、决策、反事实标注同时评估问答和规划。
- **Baseline** · 无推理监督的 VLA。
- **Benchmark** · 多城市两万个二十秒片段。
- **关键结果 / 消融** · 摘要报告关闭推理输出后仍有规划收益。
- **适用条件 / 局限** · 基准收益不能直接外推道路安全。

**可复用机制** · 禁用显式输出做对照，隔离推理监督对内部策略的贡献。

<a id="paper-153330"></a>

## Nuwa: Evaluation-Grounded Agentic Construction of Time Series Forecasting Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/153330) · [作者来源](https://openreview.net/forum?id=M7a9vo8Nj6)

- **问题 / 瓶颈** · 自动搜索难归因是模块、外生量还是参数起作用。
- **核心创新 / 方法** · 以预算限制选择局部候选和对照，将增益及数据条件写入记忆。
- **Baseline** · 对应参考配置。
- **Benchmark** · 约 15,000 次时序实验。
- **关键结果 / 消融** · 摘要报告平均 MSE 降 8%。
- **适用条件 / 局限** · 局部因子变化不必代表全局最好。

**可复用机制** · 把调参日志设计成可回查的局部干预证据。

<a id="paper-154834"></a>

## N-vium: Mixture-of-Exits Transformer for Accelerated Exact Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/154834) · [作者来源](https://openreview.net/forum?id=AbwLJoCyB5)

- **问题 / 瓶颈** · 近似早退出可能损精度。
- **核心创新 / 方法** · 学习多深度分布混合，将未计算深层状态延后并与后续词元合批。
- **Baseline** · 参数和数据匹配 Transformer。
- **Benchmark** · 最高 1.5B 的困惑度与时延。
- **关键结果 / 消融** · 摘要报告最大模型墙钟加速 57.9%，无困惑度损失。
- **适用条件 / 局限** · 精确是对所学混合分布，依赖调度效率。

**可复用机制** · 同训练目标定义可变深度计算，再通过跨词元批处理兑现延迟收益。

<a id="paper-153072"></a>

## NyoomFloat12: Accelerating LLM Inference via Lossless 12-bit Weight Compression

[官方论文页](https://neurips.cc/virtual/2026/poster/153072) · [作者来源](https://openreview.net/forum?id=OCT6Zc4IU0)

- **问题 / 瓶颈** · 变长熵码并行解码过慢。
- **核心创新 / 方法** · 逐矩阵标度后对主群省去共有指数位，异常组引用原值缓冲。
- **Baseline** · BF16、cuBLAS 与先前无损解码。
- **Benchmark** · GEMV 及 Qwen3-32B 容量受限服务。
- **关键结果 / 消融** · 带宽设置较匹配 BF16 最多快 1.21 倍，服务吞吐最多 2.67 倍。
- **适用条件 / 局限** · 依赖指数分布和带宽瓶颈。

**可复用机制** · 先确定常见值可定宽编码，再单独保留稀少异常的精确性。

<a id="paper-148732"></a>

## OASES: Outcome-Aligned Search-Evaluation Co-Training for Agentic Search

[官方论文页](https://neurips.cc/virtual/2026/poster/148732) · [作者来源](https://openreview.net/forum?id=vSRBcZC2wQ)

- **问题 / 瓶颈** · 固定代理奖励可能偏离终局且随策略变陈旧。
- **核心创新 / 方法** · 以中间状态能否支持原问作过程分，在线更新状态评估器与策略。
- **Baseline** · 仅结局奖励、强强化搜索。
- **Benchmark** · 五个多跳 QA。
- **关键结果 / 消融** · 摘要报告一致改善，并有两部分诊断。
- **适用条件 / 局限** · 依赖终局真值与过程评分质量。

**可复用机制** · 训练过程裁判时用当前策略新状态反复校验其与终局的一致性。

<a id="paper-152937"></a>

## OASIS: Observation-Action Space Alignment via SE(3) Trajectory Prediction for Robotic Manipulation

[官方论文页](https://neurips.cc/virtual/2026/poster/152937) · [作者来源](https://openreview.net/forum?id=PGq5jFALJa)

- **问题 / 瓶颈** · 预测未来外观不能直接给控制的刚体几何。
- **核心创新 / 方法** · 融合视觉语言与深度，监督相机系 SE(3) 并据预测隐状态输出动作块。
- **Baseline** · VLA 与世界动作模型。
- **Benchmark** · 仿真和实机的成功与分布外设置。
- **关键结果 / 消融** · 摘要报告两类表现改善。
- **适用条件 / 局限** · 依赖深度、坐标及端位姿监督。

**可复用机制** · 让控制接口以动作空间同构几何提供可测的中间状态。

<a id="paper-155429"></a>

## OASIS: Online Adaptive Steering for In-Training Safety of LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/155429) · [作者来源](https://openreview.net/forum?id=5idvmMr6r1)

- **问题 / 瓶颈** · 固定激活干预可能随参数变化变陈旧。
- **核心创新 / 方法** · 在线跟踪对齐偏移，用样本自适应激活防护保持训练。
- **Baseline** · 固定安全机制与正规化。
- **Benchmark** · 三种对齐问题、三种微调数据情形。
- **关键结果 / 消融** · 摘要报告防护改善并保持任务表现。
- **适用条件 / 局限** · 需要在部署前再次评估未知更新。

**可复用机制** · 将防护校准频率与实际分布漂移关联，而不是只在训练前校准。

<a id="paper-139282"></a>

## Object Detection Benchmarks are Incomplete: The Role of Label Errors and Annotation Uncertainty

[官方论文页](https://neurips.cc/virtual/2026/poster/139282) · [作者来源](https://openreview.net/forum?id=ZS2MA5cnQ0)

- **问题 / 瓶颈** · 小、遮挡、密集目标常被漏标，人工歧义被硬标签折叠。
- **核心创新 / 方法** · 重标并汇集至少十一人意见作为软标签。
- **Baseline** · 原标注和合成噪声检查。
- **Benchmark** · COCO、VOC、Cityscapes、KITTI。
- **关键结果 / 消融** · 重标对象数在 KITTI 最多增 60%、COCO 40%；真实错误检测更难。
- **适用条件 / 局限** · 标注规则改变也可影响对象数。

**可复用机制** · 同时量化真漏标与多元合理判断，再比较性能和排名。

<a id="paper-150191"></a>

## Object Hallucination Mitigation in Large Vision-Language Models via Self-Vision Dual Masking and Uncertainty-Triggered Assembly

[官方论文页](https://neurips.cc/virtual/2026/poster/150191) · [作者来源](https://openreview.net/forum?id=k3bNFdhhNj)

- **问题 / 瓶颈** · 全图读出可能凭背景或类别先验幻觉。
- **核心创新 / 方法** · 用自身视觉编码器生成互补遮罩，按熵触发支持优先的 logit 组合。
- **Baseline** · 原 VLM、额外训练与外部视觉专家。
- **Benchmark** · 多个骨干的对象幻觉和感知。
- **关键结果 / 消融** · 摘要报告幻觉减且感知保持竞争力。
- **适用条件 / 局限** · 遮罩漏真证据时纠正会出错。

**可复用机制** · 将辅助推理预算集中于高不确定事件，并用互补视图做反事实检查。

<a id="paper-151331"></a>

## Objective-Aligned Amortized Inference for Offline Bayes-Adaptive MDP Model Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151331) · [作者来源](https://openreview.net/forum?id=bKLjQijakE)

- **问题 / 瓶颈** · 目标对采样流程不变，编码器仍可从访问频次读出流程。
- **核心创新 / 方法** · 让编码器因子化于目标诱导的数据签名。
- **Baseline** · 不加限制的摊销编码器。
- **Benchmark** · 多协议的后验一致和规划。
- **关键结果 / 消融** · 摘要报告结构匹配减小差异。
- **适用条件 / 局限** · 依赖签名保留实际识别信息。

**可复用机制** · 不变损失不自动带来不变表示，需用结构或对照显式保证。

<a id="paper-155962"></a>

## Objective Shaping with Hard Negatives: Windowed Partial AUC Optimization for   RL-based LLM Recommenders

[官方论文页](https://neurips.cc/virtual/2026/poster/155962) · [作者来源](https://openreview.net/forum?id=1WfjtTf5CM)

- **问题 / 瓶颈** · 优化整体 AUC 不等于改善 Top-K。
- **核心创新 / 方法** · 分析二元 GRPO 与 AUC 等价，针对 FPR 窗做局部重加权。
- **Baseline** · 随机负例、束搜索难负例。
- **Benchmark** · 四个真实推荐集。
- **关键结果 / 消融** · 摘要报告更契合 Top-K，数据集上改善。
- **适用条件 / 局限** · 窗口依赖候选分布及目标 K。

**可复用机制** · 把负例难度选择解读为对优化目标的改变，按真实排序口径设窗口。

<a id="paper-154103"></a>

## OBJECT-UNI: A Unified Model for Object-Centric Spatial Understanding and Controllable Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/154103) · [作者来源](https://openreview.net/forum?id=GDwGbEZvpN)

- **问题 / 瓶颈** · 描述姿态的文字难支撑精确视角操纵。
- **核心创新 / 方法** · 将方向抽象为结构化视点，同时保留连续几何监督和实例锚点。
- **Baseline** · 通用统一视觉模型。
- **Benchmark** · UniSpatial-80K，物姿理解及视点生成。
- **关键结果 / 消融** · 摘要报告两项能力改善。
- **适用条件 / 局限** · 连续状态的估计与目标视角覆盖限制可控性。

**可复用机制** · 用单位和坐标清楚的状态变量连接推断与控制，验收其双向一致性。

<a id="paper-139674"></a>

## ObjView-Bench: Rethinking Difficulty and Deployment for Object-Centric View Planning

[官方论文页](https://neurips.cc/virtual/2026/poster/139674) · [作者来源](https://openreview.net/forum?id=BOgzWFvn2S)

- **问题 / 瓶颈** · 理想视点预算可能颠倒部署排序。
- **核心创新 / 方法** · 用集合覆盖描述协议难度，分别扫描预算和物理可达。
- **Baseline** · 经典、学习与混合视点规划。
- **Benchmark** · ObjView-Bench 主动重建。
- **关键结果 / 消融** · 摘要报告预算与可达改变排名，难度采样有益。
- **适用条件 / 局限** · 集合覆盖近似未涵盖所有物理代价。

**可复用机制** · 把物体难度与部署限制拆开，否则训练和验收容易选错样本。

<a id="paper-139628"></a>

## OBLIQ-Bench: Exposing Overlooked Bottlenecks in Modern Retrievers with Latent and Implicit Queries

[官方论文页](https://neurips.cc/virtual/2026/poster/139628) · [作者来源](https://openreview.net/forum?id=ERE2Puzaqv)

- **问题 / 瓶颈** · 验证器准确但从未收到正确文档时，末端评分无法定位原因。
- **核心创新 / 方法** · 用潜在模式定义长尾查询，分别给已有候选和搜索测试。
- **Baseline** · 现代检索及直接推理判相关。
- **Benchmark** · OBLIQ-Bench 五项真实长尾检索。
- **关键结果 / 消融** · 摘要报告看到候选时判断较准，实际召回仍弱。
- **适用条件 / 局限** · 发现限所测隐式模式和语料。

**可复用机制** · 先给判别器真候选测上限，再归因索引与召回欠缺。

<a id="paper-152077"></a>

## ObsConDA: Observability-Constrained Data Assimilation with Control-Space Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/152077) · [作者来源](https://openreview.net/forum?id=Vdp2Hgele9)

- **问题 / 瓶颈** · 稀疏观测位置变化时固定潜空间可能修正不可辨状态。
- **核心创新 / 方法** · 从背景与观测几何确定支持方向，只估对应控制系数。
- **Baseline** · 经典同化和学习校正器。
- **Benchmark** · 真实地面站、模拟匹配及几何偏移。
- **关键结果 / 消融** · 摘要报告留出站与全场表现最佳，消融支持方向自适应。
- **适用条件 / 局限** · 依赖背景状态与传感结构可用。

**可复用机制** · 每轮只更新当下观测真正约束的方向。

<a id="paper-153828"></a>

## Observable Neural ODEs for Identifiable Causal Forecasting in Continuous Time

[官方论文页](https://neurips.cc/virtual/2026/poster/153828) · [作者来源](https://openreview.net/forum?id=IQwsfl9G8s)

- **问题 / 瓶颈** · 拟合能预测历史并不保证能辨识干预效应。
- **核心创新 / 方法** · 以可观测正常形建 Neural ODE，结合潜状态滤波与连续时间调整。
- **Baseline** · 现有序列模型。
- **Benchmark** · 合成、半合成和观测医疗数据下的方法学评估。
- **关键结果 / 消融** · 摘要给出可观测性必要性与较好预测。
- **适用条件 / 局限** · 观测效果不是临床因果验证，识别依赖模型条件。

**可复用机制** · 明确区分预测能力和反事实可识别性，先验收测量是否约束状态。

<a id="paper-151775"></a>

## Observations Drift, Structures Remain: Structural Pretraining with Time Alignment for Electromagnetic Signals

[官方论文页](https://neurips.cc/virtual/2026/poster/151775) · [作者来源](https://openreview.net/forum?id=Y7NJqTgjv8)

- **问题 / 瓶颈** · 重建波形易学传播和设备捷径。
- **核心创新 / 方法** · 用采样率归一的 RoPE 和层级离散结构遮罩目标。
- **Baseline** · 混合波形重建。
- **Benchmark** · 多种电磁任务，全监督和少样本。
- **关键结果 / 消融** · 摘要报告跨观测变化更稳。
- **适用条件 / 局限** · 依赖采样率可靠和离散单元构造。

**可复用机制** · 将时间坐标和语义目标从硬件采样外观解耦。

<a id="paper-139118"></a>

## OccStress: Stress-Testing the 4D Occupancy Forecasting Chain

[官方论文页](https://neurips.cc/virtual/2026/poster/139118) · [作者来源](https://openreview.net/forum?id=k1vpGWtKyd)

- **问题 / 瓶颈** · 干净序列不显示误差进入、持续和传播位置。
- **核心创新 / 方法** · 构造感知及未来预测两套压力测试，对当前、近期和更早状态分别施加扰动。
- **Baseline** · 干净预测及不同注入时点。
- **Benchmark** · 61 类损坏、八万余锚点；3D 和 4D 占据。
- **关键结果 / 消融** · 作者报告上游误差和预测自身敏感性都明显。
- **适用条件 / 局限** · 合成损坏与真实传感故障的对应待查。

**可复用机制** · 用相同预测器替换输入来源和扰动时点，测误差是否会在闭环积累。

<a id="paper-149393"></a>

## Occupancy-based Quantile Risk Control

[官方论文页](https://neurips.cc/virtual/2026/poster/149393) · [作者来源](https://openreview.net/forum?id=qOeSSrQgQq)

- **问题 / 瓶颈** · 保守区间与只渐近有效的办法难支撑阈值选择。
- **核心创新 / 方法** · 按有序损失划桶，以每桶最大损失上界化，再选合规参数。
- **Baseline** · 既有共形分位风险控制。
- **Benchmark** · 风险阈值和置信水平下的有限样本分析。
- **关键结果 / 消融** · 证明上界有限样本有效并向最优界收敛。
- **适用条件 / 局限** · 依赖校准可交换性等条件，边缘与分布变化需查。

**可复用机制** · 分开校验桶频率误差和桶内最坏损失，不以平均风险替代分位控制。

<a id="paper-150573"></a>

## OceanCBM: A Concept Bottleneck Model for Mechanistic Interpretability in Ocean Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/150573) · [作者来源](https://openreview.net/forum?id=h9jfL4NIg5)

- **问题 / 瓶颈** · 只测预报可出现多种互不一致的解释。
- **核心创新 / 方法** · 用指定海洋概念和自由概念共同预测混合层热含量，混合监督。
- **Baseline** · 只做预测、只做物理概念监督。
- **Benchmark** · 海洋时空热含量预测，比较不同初始化的机制一致性。
- **关键结果 / 消融** · 综合监督的机制表示较一致，对照即使预测接近也可学不同结构。
- **适用条件 / 局限** · 自由概念未必对应单一物理量，外推需查。

**可复用机制** · 在等预测精度下同时衡量概念跨初始化稳定性。

<a id="paper-152912"></a>

## OCTOPUS: Optimized KV Cache for Transformers via Octahedral Parametrization Under optimal Squared error quantization

[官方论文页](https://neurips.cc/virtual/2026/poster/152912) · [作者来源](https://openreview.net/forum?id=PTfy7K7w8o)

- **问题 / 瓶颈** · 坐标独立处理未利用方向与模长结构。
- **核心创新 / 方法** · 将三元组方向八面体映到二维，配合模长 Lloyd–Max 量化，按平方误差分比特。
- **Baseline** · TurboQuant、PolarQuant。
- **Benchmark** · 文本、视频及音频，比较位宽和保真。
- **关键结果 / 消融** · 摘要报告各已测位宽持平或更好，低位时优势增大。
- **适用条件 / 局限** · 运行时速度和硬件打包成本待查。

**可复用机制** · 固定缓存占用下比较几何码本是否比增加标量精度有利。

<a id="paper-152979"></a>

## OFBD: Object-Focused Background Debiasing for Long-Tailed Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/152979) · [作者来源](https://openreview.net/forum?id=OuD9gP9e2o)

- **问题 / 瓶颈** · 尾类背景变化大且梯度可能受背景主导。
- **核心创新 / 方法** · 前景保留 CutMix 改换背景，同时按背景特征进行无参数校正。
- **Baseline** · 重平衡及常规增强。
- **Benchmark** · 长尾视觉识别，检查背景偏差和尾部表现。
- **关键结果 / 消融** · 摘要发现尾类对背景偏差更敏感。
- **适用条件 / 局限** · 前景估计错误和真实物体背景依赖的边界待核实。

**可复用机制** · 用前景固定、背景变化的对照评估是否真的减少伪相关。

<a id="paper-151729"></a>

## Offline Constrained Reinforcement Learning under Partial Data Coverage

[官方论文页](https://neurips.cc/virtual/2026/poster/151729) · [作者来源](https://openreview.net/forum?id=YXF70sZQPU)

- **问题 / 瓶颈** · 只让最优解可表示，仍可能引入伪鞍点。
- **核心创新 / 方法** · 分解线性规划，以原始对偶求解显式策略，避免从未知采集分布抽取策略。
- **Baseline** · 需要完整覆盖或额外正则的已有离线约束方法。
- **Benchmark** · 折扣约束 MDP，一般函数近似；可行性与近似最优。
- **关键结果 / 消融** · 更强可实现性下限制鞍点都是最优，算法可返回近可行近最优解。
- **适用条件 / 局限** · 需核验可实现性和覆盖条件。

**可复用机制** · 学习约束表示时检查所有经验鞍点的可达性，不能只检查目标策略可表达。

<a id="paper-139500"></a>

## Offline Preference-Based Trajectory Evaluation

[官方论文页](https://neurips.cc/virtual/2026/poster/139500) · [作者来源](https://openreview.net/forum?id=M1eNDOOTeU)

- **问题 / 瓶颈** · 相同最终结果掩盖不同过程并损失有效样本。
- **核心创新 / 方法** · 比较完整轨迹的部分完成与时间分布。
- **Baseline** · 仅终点成功。
- **Benchmark** · 多代理与交互基准，测配对平局和排名稳定。
- **关键结果 / 消融** · 轨迹比较将平局从约 75% 降到约 30%。
- **适用条件 / 局限** · 中间偏好依赖任务及价值，无意义快进可能虚增优势。

**可复用机制** · 在相同终局成功率下显式比较部分进度，避免把中途失败都当等价。

<a id="paper-153404"></a>

## Off-Policy Evaluation of Large Language Models via Learned Semantic Bottleneck Embeddings

[官方论文页](https://neurips.cc/virtual/2026/poster/153404) · [作者来源](https://openreview.net/forum?id=LbaPgj9LAg)

- **问题 / 瓶颈** · 倾向比方差大，而普通压缩可能丢掉奖励相关区别。
- **核心创新 / 方法** · 以条件信息瓶颈最小化边缘重要加权估计的均方误差上界。
- **Baseline** · IPS、通用嵌入 MIPS。
- **Benchmark** · HelpSteer2、UltraFeedback，Qwen、Gemma、Llama 策略，指标 MSE。
- **关键结果 / 消融** · 摘要报告相较既有方法降低 MSE。
- **适用条件 / 局限** · 仍受记录策略覆盖和奖励模型误差限制。

**可复用机制** · 对同一日志控制不同瓶颈的偏差与方差，并测少数高奖励模式是否被压掉。

<a id="paper-152279"></a>

## OGPO: Offline Goal-conditioned Policy Optimization for Recoverable Vision-Language-Action Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152279) · [作者来源](https://openreview.net/forum?id=UHGjizDGoH)

- **问题 / 瓶颈** · 逐步模仿易绑定单条示范路径。
- **核心创新 / 方法** · 重标任务进度关键态，构造以达到这些状态为目标的离线过程奖励。
- **Baseline** · 轨迹级行为模仿。
- **Benchmark** · 机器人操作与偏离示范的恢复；具名待核实。
- **关键结果 / 消融** · 摘要提出关键状态目标可支持可行的新路径。
- **适用条件 / 局限** · 关键状态标注、数据支持与恢复条件待查。

**可复用机制** · 在偏离点重新初始化评测，分开比较重现演示和到达同一任务进度。

<a id="paper-155542"></a>

## OHATP: Graph Anomaly Detection with Orthogonal-Hyperspherical Augmentation and Topology Perception

[官方论文页](https://neurips.cc/virtual/2026/poster/155542) · [作者来源](https://openreview.net/forum?id=4mRMtwcvXD)

- **问题 / 瓶颈** · 随机屏蔽和结构变化可能消除异常证据。
- **核心创新 / 方法** · 限制投影与噪声几何并按消息影响调节，再筛异常子结构。
- **Baseline** · 随机增强和既有图异常模型。
- **Benchmark** · 图异常评测，AUROC 和 AUPRC。
- **关键结果 / 消融** · 摘要报告改善逾 6% 和 29%。
- **适用条件 / 局限** · 需拆开两部分贡献，也需检查稀疏异常。

**可复用机制** · 用已知异常结构比较增强前后可检测性。

<a id="paper-148515"></a>

## OLA-Place: Cross-Modal Place Recognition without Global Descriptors

[官方论文页](https://neurips.cc/virtual/2026/poster/148515) · [作者来源](https://openreview.net/forum?id=xJJLGIE6Sb)

- **问题 / 瓶颈** · 整体嵌入会丢细粒度对应。
- **核心创新 / 方法** · 保留对象粒度，以掩码最大值计算集合相似性。
- **Baseline** · 单一全局描述符。
- **Benchmark** · 文本识别三维地点，具体基准待核。
- **关键结果 / 消融** · 摘要称对象对齐结果提升。
- **适用条件 / 局限** · 依赖对象检测与提及解析。

**可复用机制** · 在重复对象和无效候选上复核匹配。

<a id="paper-150464"></a>

## OliO: ODE-based Linear Transition Operator for Self-Supervised Time Series Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/150464) · [作者来源](https://openreview.net/forum?id=hpwkIMU05L)

- **问题 / 瓶颈** · 把时间偏移当噪声会破坏预测信息。
- **核心创新 / 方法** · 用严格上三角线性 ODE 对齐不同偏移的潜变量。
- **Baseline** · 遮盖、对比与调参强基线。
- **Benchmark** · 多骨干和时序集，MSE。
- **关键结果 / 消融** · 最优改善 5.75%。
- **适用条件 / 局限** · 依赖线性变换假设。

**可复用机制** · 按时间间隔测试稳定性和准确率。

<a id="paper-139331"></a>

## OmniCapBench: A Deep-Structured Evaluation Framework for Fine-Grained Audio-Visual Captioning

[官方论文页](https://neurips.cc/virtual/2026/poster/139331) · [作者来源](https://openreview.net/forum?id=WgEmdr50mC)

- **问题 / 瓶颈** · 整段评分不能定位问题。
- **核心创新 / 方法** · 提取可验收原子单元并结合规则与局部语义比较。
- **Baseline** · 整段分数、局部探针、普通模型评审。
- **Benchmark** · 786 个高密度标注视频。
- **关键结果 / 消融** · 局部感知较强，长程身份和视听对齐薄弱。
- **适用条件 / 局限** · 依赖标注与评审一致性。

**可复用机制** · 分报身份延续、时间定位和跨模态绑定。

<a id="paper-151885"></a>

## OmniEgoCap: Camera-Agnostic Sequence-Level Egocentric Motion Reconstruction

[官方论文页](https://neurips.cc/virtual/2026/poster/151885) · [作者来源](https://openreview.net/forum?id=XBhKJqEr4E)

- **问题 / 瓶颈** · 固定视野或通用缺失掩码难以迁移。
- **核心创新 / 方法** · 依据相机几何增强，扩散利用全序列稀疏姿态证据。
- **Baseline** · 固定可见性及事后优化。
- **Benchmark** · OmniEgoDB、合成与真实设备。
- **关键结果 / 消融** · 报告跨设备重建改善。
- **适用条件 / 局限** · 未见安装角度和遮挡待核。

**可复用机制** · 按视野、安装方式和运动独立分组验收。

<a id="paper-155919"></a>

## OmniGF: A Dual-Branch Vision-Language Framework for Unified Gaze Following

[官方论文页](https://neurips.cc/virtual/2026/poster/155919) · [作者来源](https://openreview.net/forum?id=1pPCCHeICG)

- **问题 / 瓶颈** · 文本坐标不易精确，同图多人重复编码。
- **核心创新 / 方法** · 共享场景编码，附各人头部向量并读稠密状态。
- **Baseline** · 单人模型和纯文本坐标。
- **Benchmark** · 多个视线与语义任务。
- **关键结果 / 消融** · 摘要称超过标准参考。
- **适用条件 / 局限** · 拥挤场景人头捕获及标注适用范围待核。

**可复用机制** · 在合成多人互动中同时测像素定位和目标语义。

<a id="paper-155508"></a>

## Omni-Interactive Universal Embedder

[官方论文页](https://neurips.cc/virtual/2026/poster/155508) · [作者来源](https://openreview.net/forum?id=54DQalLSzW)

- **问题 / 瓶颈** · 只用文本交互无法准确引用视听局部。
- **核心创新 / 方法** · 通过视觉和音频分割将选择输入通用向量模型。
- **Baseline** · 标准多模态嵌入与文本交互。
- **Benchmark** · MMEB-v2-video、MAEB、SCaR、OmniCHOIR。
- **关键结果 / 消融** · OmniCHOIR 摘要报告改善 24.1%。
- **适用条件 / 局限** · 依赖前置分割和跨模态表示。

**可复用机制** · 固定语义目标比较文本、区域与组合表达。

<a id="paper-151826"></a>

## OmniJigsaw: Enhancing Omni-Modal Reasoning via Modality-Orchestrated Reordering

[官方论文页](https://neurips.cc/virtual/2026/poster/151826) · [作者来源](https://openreview.net/forum?id=XftlRnCnyu)

- **问题 / 瓶颈** · 完整视听流里模型可能只用简单一路。
- **核心创新 / 方法** · 比较联合输入、样本级选择和片段级遮盖。
- **Baseline** · 联合模态及样本级选择。
- **Benchmark** · 15 个视频、音频和组合任务。
- **关键结果 / 消融** · 细粒度遮盖效果最好。
- **适用条件 / 局限** · 代理任务的覆盖需验。

**可复用机制** · 固定样本和奖励，比较遮盖粒度和跨模态依赖。

<a id="paper-154211"></a>

## OmniMechanism Design for Human-AI Collaboration with Impressionable Minds

[官方论文页](https://neurips.cc/virtual/2026/poster/154211) · [作者来源](https://openreview.net/forum?id=FLnfOfsR2X)

- **问题 / 瓶颈** · 人工建议并非固定不变。
- **核心创新 / 方法** · 以条件老虎机和校准框架优化逐条件协作。
- **Baseline** · 固定披露或人工判断不变的设计。
- **Benchmark** · 合作理论和多条件实验。
- **关键结果 / 消融** · 摘要报告可适应变化的询问成本和目标。
- **适用条件 / 局限** · 高风险真实应用仍需独立验收。

**可复用机制** · 对自有良性评估独立操纵显示预测与成本。

<a id="paper-138886"></a>

## OmniMemBench: Towards Scalable Evaluation of Long-Term Omni-Modal Agent Memory

[官方论文页](https://neurips.cc/virtual/2026/poster/138886) · [作者来源](https://openreview.net/forum?id=yl7Kom0j0v)

- **问题 / 瓶颈** · 总答题分会混淆检索与压缩损失。
- **核心创新 / 方法** · 分测线索覆盖、记忆条目相关和问答表现。
- **Baseline** · 长上下文、RAG 与结构化记忆。
- **Benchmark** · 6,655 问、8 类、128K 至 1M。
- **关键结果 / 消融** · 线索覆盖相近时记忆仍更弱，字幕会丢感知细节。
- **适用条件 / 局限** · 评审一致性及人物对话覆盖限制。

**可复用机制** · 固定证据和题目分别验压缩前后线索及答案。

<a id="paper-150029"></a>

## OmniMem: Scalable and Adaptive Memory Retrieval for Long Video Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/150029) · [作者来源](https://openreview.net/forum?id=lJpXhbi9az)

- **问题 / 瓶颈** · 局部信息会占满稀疏缓存，并集取数也昂贵。
- **核心创新 / 方法** · 长历史时排除本地候选，结合共享选择和各头独立读取。
- **Baseline** · 截断、隐式压缩以及长视频基线。
- **Benchmark** · 长视频动态度、一致性和内存。
- **关键结果 / 消融** · 动态度提高 52.3%，内存相近。
- **适用条件 / 局限** · 依赖硬件随机读取与局部短程保障。

**可复用机制** · 分别报告近期连续和远程重访一致性。

<a id="paper-153308"></a>

## Omni-Safety under Cross-Modality Conflict: Vulnerabilities, Dynamic Mechanisms and Efficient Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/153308) · [作者来源](https://openreview.net/forum?id=MG5vjzQiWq)

- **问题 / 瓶颈** · 单流测试不能保证组合场景可靠。
- **核心创新 / 方法** · 报告受控安全干预前后风险识别和普通任务准确率。
- **Baseline** · 未额外适配的模型。
- **Benchmark** · 多模态受控安全及能力对照。
- **关键结果 / 消融** · 摘要中拒绝有害请求的成功率由 69.9% 到 91.2%。
- **适用条件 / 局限** · 不能外推未知模态和模糊请求。

**可复用机制** · 分模态审计漏报、正常请求误拒和效用。

<a id="paper-153551"></a>

## OmniSelect: Dynamic Modality-Aware Token Compression for Efficient Omni-modal Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153551) · [作者来源](https://openreview.net/forum?id=KXeTOhQPAP)

- **问题 / 瓶颈** · 固定比例不适应问题。
- **核心创新 / 方法** · 用轻量关联评分决定声音、视频或均衡模式，并在各时间组剪裁。
- **Baseline** · 固定模态裁剪。
- **Benchmark** · 多模态理解，测表现及词元减少。
- **关键结果 / 消融** · 摘要称压缩下保持强表现。
- **适用条件 / 局限** · 依赖相关估计，跨时段罕见证据会丢。

**可复用机制** · 相同预算比较三种主导情形及动态分配。

<a id="paper-149329"></a>

## OmniSE: Support-Faithful Optimization for Evidence-Centric Audio-Video Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/149329) · [作者来源](https://openreview.net/forum?id=quMnHuIS85)

- **问题 / 瓶颈** · 答对可能基于错时段或单模态。
- **核心创新 / 方法** · 用含时间线索和模态的证据记录，对比替代支持，再比较答案轨迹。
- **Baseline** · 答案级训练和同规模开放模型。
- **Benchmark** · 若干视听问答集。
- **关键结果 / 消融** · 报告持续优于参考。
- **适用条件 / 局限** · 证据标签可靠性及额外计算待核。

**可复用机制** · 用视听错配样例验证答案和证据分数。

<a id="paper-151867"></a>

## OmniSpace: Efficient Geometry Awareness for Autonomous Vehicles MLLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/151867) · [作者来源](https://openreview.net/forum?id=XICFVurCWx)

- **问题 / 瓶颈** · 依赖在线三维模型会增加复杂度和传递误差。
- **核心创新 / 方法** · 显式注入位姿及极线关联，并用三维教师蒸馏。
- **Baseline** · 依赖在线三维模型的路线。
- **Benchmark** · nuScenes、Bench2Drive、nuInstruct、Omnidrive、DriveBench。
- **关键结果 / 消融** · 摘要称多类任务改善。
- **适用条件 / 局限** · 闭环安全与不同摄像头仍需核对。

**可复用机制** · 以低风险模拟分别消融位姿、匹配和监督。

<a id="paper-152619"></a>

## Omni-SpikeDet: A Spiking Open-World Detector with Dynamic Text–Image Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/152619) · [作者来源](https://openreview.net/forum?id=Rkd6BFx0pt)

- **问题 / 瓶颈** · 开放词表多依赖稠密神经，脉冲接口存在训练失配。
- **核心创新 / 方法** · 以整数脉冲训练和脉冲推理，使用跨尺度语言调制。
- **Baseline** · 稠密和已有脉冲检测。
- **Benchmark** · COCO 和 LVIS，AP、参数与理论能耗。
- **关键结果 / 消融** · AP 47.2 与 27.9，参数 4.2M。
- **适用条件 / 局限** · 理论能耗 19.8 mJ 不代表实机。

**可复用机制** · 以同实际设备预算测稠密和脉冲的准确、耗时及能耗。

<a id="paper-138921"></a>

## OmniToM: Benchmarking Theory of Mind in LLMs via Explicit Belief Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/138921) · [作者来源](https://openreview.net/forum?id=wm4vgQFJmq)

- **问题 / 瓶颈** · 终点答案可能正确却不跟踪知识访问。
- **核心创新 / 方法** · 提取原子信念，再按嵌套级别、真假与角色知识等评分。
- **Baseline** · 终点社会推理题。
- **Benchmark** · 895 故事，22,343 信念条目。
- **关键结果 / 消融** · 摘要称角色知识访问和归属仍是瓶颈。
- **适用条件 / 局限** · 依赖标注模式和故事构造。

**可复用机制** · 分别审计主体、认知状态与最终推论。

<a id="paper-139772"></a>

## OmniTraffic: A Controllable Generation Pipeline and Benchmark for Spatio-Temporal Traffic Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/139772) · [作者来源](https://openreview.net/forum?id=5fv0JAYAwL)

- **问题 / 瓶颈** · 被动识别对真实决策的结构能力区分不足。
- **核心创新 / 方法** · 重建可编辑路口并同步生成带结构真值的问题，用实录对照迁移。
- **Baseline** · 十一种模型及人工。
- **Benchmark** · 12 个路口与 3K 人工核验样本。
- **关键结果 / 消融** · 摘要报告拓扑和时空差距最明显，模拟训练改善实录问答。
- **适用条件 / 局限** · 实录及路口范式有限，不等于安全验证。

**可复用机制** · 用可控环境逐项操纵交通因素，避免总体识别分数掩盖关系推理失败。

<a id="paper-148151"></a>

## On approximation and estimation of Schrödinger potentials without the curse of dimensionality

[官方论文页](https://neurips.cc/virtual/2026/poster/148151) · [作者来源](https://openreview.net/forum?id=zuVAp9q3Lp)

- **问题 / 瓶颈** · 有限样本恢复 Schrödinger 势的保证不清楚。
- **核心创新 / 方法** · 分析高斯到目标的桥和 Doob 变换的神经近似误差。
- **Baseline** · 以环境维数衡量估计难度的通用分析。
- **Benchmark** · 近似与估计的理论上界。
- **关键结果 / 消融** · 界由目标有效维数决定。
- **适用条件 / 局限** · 依赖论文的目标几何和正则条件，实际估计代价待核实。

**可复用机制** · 低维结构存在时优先检查适配性，不以原始坐标数直接推断数据量。

<a id="paper-154421"></a>

## On Computing Diverse Solutions in the Earth Movers Distance

[官方论文页](https://neurips.cc/virtual/2026/poster/154421) · [作者来源](https://openreview.net/forum?id=Di32FbHcJU)

- **问题 / 瓶颈** · 计算一个子集对的距离不解决组合搜索的难度。
- **核心创新 / 方法** · 针对欧氏和一般度量分别推导有参近似，考察最远子集。
- **Baseline** · 两两 EMD 计算和复杂度下界。
- **Benchmark** · 指定 r 个 k 子集的最小两两运输距离。
- **关键结果 / 消融** · 欧氏给接近最优的有参算法；两个子集的一般度量给二近似。
- **适用条件 / 局限** · 依赖维数和 k、r，非度量代价更受限。

**可复用机制** · 不要把距离可计算误当多样候选可高效选，先选适合的数据几何。

<a id="paper-151830"></a>

## On Differentially Private Mechanisms for Linear Regression

[官方论文页](https://neurips.cc/virtual/2026/poster/151830) · [作者来源](https://openreview.net/forum?id=Xd1wBiiFWf)

- **问题 / 瓶颈** · 每个时点重跑批算法成本高，隐私也需统一核算。
- **核心创新 / 方法** · 采用连续更新的无约束线性估计机制，分析误差及空间。
- **Baseline** · 受约束连续方法与反复批处理。
- **Benchmark** · 真实数据、逐步参数输出及最坏界。
- **关键结果 / 消融** · 误差差距随根号维数与对数因子增长，实证优于所比私有方法。
- **适用条件 / 局限** · 给定 DP 定义及数据约束。

**可复用机制** · 流数据频繁发布时用事件级预算统一设计估计器，而非将每次结果独立加噪。

<a id="paper-151936"></a>

## On Differential Private $\ell_1$, $\ell_2$ and $\ell_p^p$ Distance Queries

[官方论文页](https://neurips.cc/virtual/2026/poster/151936) · [作者来源](https://openreview.net/forum?id=WifaN44w16)

- **问题 / 瓶颈** · 旧方案每个查询需组合多个树级计数。
- **核心创新 / 方法** · 以距离和计数的组合构造查询树，缩减项数。
- **Baseline** · ICLR 2024 结点扰动树等。
- **Benchmark** · L1、L2 和 Lp 距离查询；时延和隐私误差。
- **关键结果 / 消融** · 摘要报告相同预处理空间下加快查询并改善误差。
- **适用条件 / 局限** · 要按核、范围和 DP 预算复核常数。

**可复用机制** · 将隐私作用于可重复查询的中间表示，并将实际需要发布的归约项最小化。

<a id="paper-149544"></a>

## One Adapter For All: Towards Generalizable Many-To-One Domain Adaptation In Heterogeneous Collaborative Perception

[官方论文页](https://neurips.cc/virtual/2026/poster/149544) · [作者来源](https://openreview.net/forum?id=pM1uwdYGp1)

- **问题 / 瓶颈** · 每个来源训练专用适配器不适合新车辆或端侧。
- **核心创新 / 方法** · 分离域不变内容和域模式，以专家混合做来源到目标重组。
- **Baseline** · 一对一适配。
- **Benchmark** · V2V4Real、V2X-Real 和零样本新源。
- **关键结果 / 消融** · 摘要报告共享固定适配器对所比基线有优势。
- **适用条件 / 局限** · 极端传感结构与通信噪声仍需评估。

**可复用机制** · 共享内容表示，条件调节域样式，而不是为每个伙伴固定接口。

<a id="paper-149252"></a>

## One Algorithm, Two Goals: Dual Scoring for Parameter and Data Selection in LLM Fine-Tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/149252) · [作者来源](https://openreview.net/forum?id=rkcG6vtYfa)

- **问题 / 瓶颈** · 独立评分重复成本且难协调两类约束。
- **核心创新 / 方法** · 用统一局部响应代理从梯度交互矩阵行列得到数据和参数效用。
- **Baseline** · 单轴选择和串行组合。
- **Benchmark** · 3B 至 9B 微调，匹配预算。
- **关键结果 / 消融** · 摘要报告完整方法折中优于串行混合。
- **适用条件 / 局限** · 依赖验证集代表性和局部近似。

**可复用机制** · 用共同验证目标同步预算，不分别选择后再假定两个结果兼容。

<a id="paper-150139"></a>

## One Avatar, Any Budget: Robust LoD for Dynamic Gaussian Avatars

[官方论文页](https://neurips.cc/virtual/2026/poster/150139) · [作者来源](https://openreview.net/forum?id=kO5gQ83XI5)

- **问题 / 瓶颈** · 删原始图元会破坏少数面部区域，预算间重新训练昂贵。
- **核心创新 / 方法** · 用语义分布约束选高斯，根据预算比在规范空间预测属性残差。
- **Baseline** · 动态头像已有层级细节适配。
- **Benchmark** · NeRSemble 多压缩比。
- **关键结果 / 消融** · 摘要报告预算下降时质量退化更慢。
- **适用条件 / 局限** · 限头像及所测动态，其他对象需验证覆盖方式。

**可复用机制** · 将图元选择和生成补偿拆开，使同一模型支持多档部署。

<a id="paper-154018"></a>

## One-Bit Clustering for Two Component Sub-Gaussian Mixture Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154018) · [作者来源](https://openreview.net/forum?id=Gqah1tHXsO)

- **问题 / 瓶颈** · 强尖峰会使极低位量化只保留少数坐标。
- **核心创新 / 方法** · 用抖动量化和 Lloyd 变体，必要时先做 Haar 随机旋转。
- **Baseline** · 未量化聚类与理论最小错误。
- **Benchmark** · 两成分次高斯混合，误分类及精确恢复。
- **关键结果 / 消融** · 非尖峰条件下误差随信噪比指数降，分离阈值仅有对数损失。
- **适用条件 / 局限** · 限两成分和指定浓缩条件。

**可复用机制** · 量化前检测能量集中，用正交变换减少坐标饱和。

<a id="paper-148266"></a>

## OneCanvas: 3D Scene Understanding via Panoramic Reprojection

[官方论文页](https://neurips.cc/virtual/2026/poster/148266) · [作者来源](https://openreview.net/forum?id=z9GVQGjnKg)

- **问题 / 瓶颈** · 逐帧输入不含共同坐标，专用结构昂贵。
- **核心创新 / 方法** · 以深度位姿反投世界坐标，将角位置放入全景并加连续三维编码。
- **Baseline** · 复杂几何编码与更高算力方法。
- **Benchmark** · SQA3D、VSI-Bench、SPBench。
- **关键结果 / 消融** · 摘要报告前两项领先，训练成本少一个数量级。
- **适用条件 / 局限** · 依赖深度位姿及场景覆盖。

**可复用机制** · 保持角向关系与度量位置信号并存，以支持换视点的推理。

<a id="paper-151574"></a>

## One for All: A Non-Linear Transformer can enable Cross-Domain Generalization for In-Context Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151574) · [作者来源](https://openreview.net/forum?id=ZZh6M076fq)

- **问题 / 瓶颈** · 仅训练在多任务上并不保证新域可表达。
- **核心创新 / 方法** · 把非线性 Transformer 联系到 RKHS 中的时序差分回归。
- **Baseline** · 传统多任务和元强化路线。
- **Benchmark** · 多个 MetaWorld 域及 TD 目标。
- **关键结果 / 消融** · 分析显示共享核条件下同权重可表示不同域价值，实测目标收敛。
- **适用条件 / 局限** · 收敛不代表所有新域回报稳健。

**可复用机制** · 选择上下文共享模型时检查价值函数的共同表示，而非只统计任务数。

<a id="paper-149035"></a>

## One Language-Free Foundation Model Is Enough for Universal Vision Anomaly Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/149035) · [作者来源](https://openreview.net/forum?id=tLTO6bWhaB)

- **问题 / 瓶颈** · 语言提示昂贵，图像级和像素级任务的特征几何不同。
- **核心创新 / 方法** · 移除语言侧推导，以分类、分割和特征层各自小权重适配。
- **Baseline** · 视觉语言的零少样本异常与全样本方法。
- **Benchmark** · 14 个工业和医学基准。
- **关键结果 / 消融** · 仅约 0.02M 可训练参数，摘要报告优于所比零少样本。
- **适用条件 / 局限** · 结果依赖骨干及目标域，医学场景未证明临床效度。

**可复用机制** · 若提示的主要职责只是构造线性决策，直接拟合权重并分开验证任务梯度。

<a id="paper-153564"></a>

## One-Layer Transformers Provably Learn In-Context K-Nearest Neighbor Prediction with Chain-of-Thought

[官方论文页](https://neurips.cc/virtual/2026/poster/153564) · [作者来源](https://openreview.net/forum?id=KRMF9RmzSJ)

- **问题 / 瓶颈** · 直接软最大容易只偏向最邻近样本。
- **核心创新 / 方法** · 构造一层模型经中间推理实现 K 近邻，并分析梯度学习。
- **Baseline** · 无推理一层 1-NN 与 K-NN。
- **Benchmark** · 特定可分二分类上下文任务。
- **关键结果 / 消融** · 无推理的 K 大于一设定有下界，带推理可训练至相应构造。
- **适用条件 / 局限** · 证明限理想数据设置。

**可复用机制** · 比较多证据汇聚的计算需求，不能从单最佳示例的成功外推。

<a id="paper-150016"></a>

## One Loss to Rule Them All: Marked Time-to-Event for Structured EHR Foundation Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150016) · [作者来源](https://openreview.net/forum?id=lNy0GEHZYE)

- **问题 / 瓶颈** · 只学习下一离散事件会忽略何时与观测强度。
- **核心创新 / 方法** · 用带标记的事件时间似然同时监督出现时刻和关联数值。
- **Baseline** · 下一词元及忽略连续测量的损失。
- **Benchmark** · 多 EHR 数据、架构、分类、回归和时间预测。
- **关键结果 / 消融** · 摘要报告泛化改善，尤其扩展到回归与发生时间。
- **适用条件 / 局限** · 采样频率或医疗记录流程可能是混淆。

**可复用机制** · 将观测时间和类型依赖写入目标，避免静态离散化丢时间机制。

<a id="paper-155435"></a>

## One Model, Two Roles: Emergent Specialization in a Shared Recurrent Transformer

[官方论文页](https://neurips.cc/virtual/2026/poster/155435) · [作者来源](https://openreview.net/forum?id=5g3g2p3Zwl)

- **问题 / 瓶颈** · 同一权重很难从形式上解释如何同时探索和维持方案。
- **核心创新 / 方法** · 在一个状态更新注入输入，另一更新遮掉；另对照身份词。
- **Baseline** · 无区分信号及状态冻结。
- **Benchmark** · Sudoku-Extreme、Maze 的轨迹探针和冻结。
- **关键结果 / 消融** · 摘要报告局部不确定和全局提案的分工，前者注意更局部。
- **适用条件 / 局限** · 两个任务的机制差异明显，不能假定普适固定分工。

**可复用机制** · 以轻量身份信号控制共享模块执行模式，并用动态消融验证角色。

<a id="paper-154314"></a>

## One More Time: Revisiting Neural Quantum States from a Reinforcement Learning Perspective

[官方论文页](https://neurips.cc/virtual/2026/poster/154314) · [作者来源](https://openreview.net/forum?id=EaMqs3Vxzg)

- **问题 / 瓶颈** · 直接一阶法忽略几何，随机重配置大模型求逆不稳。
- **核心创新 / 方法** · 将能量建为 Born 分布上的优势优化，限制概率比和环绕相位变化。
- **Baseline** · Adam、minSR、SPRING。
- **Benchmark** · Ising、Heisenberg、J1–J2 与 1.5B 模型示范。
- **关键结果 / 消融** · 摘要报告收敛时延和稳定性改善。
- **适用条件 / 局限** · 依赖自回归可采样表征及任务物理性质。

**可复用机制** · 复数概率模型的相位和幅值需要不同的距离，分别限制训练变化。

<a id="paper-155831"></a>

## One Scan is Enough: Demonstration-Free Adaptation for Language-Guided Navigation

[官方论文页](https://neurips.cc/virtual/2026/poster/155831) · [作者来源](https://openreview.net/forum?id=2YW1bwmi4r)

- **问题 / 瓶颈** · 每场景遥操数据贵，公开策略受布局外观变化。
- **核心创新 / 方法** · 从手机扫描生成指令及可执行轨迹，再用基于重建的可计算效用适配。
- **Baseline** · 最强 VLA 与常规演示适配路线。
- **Benchmark** · 五个真实环境和同楼未扫描区。
- **关键结果 / 消融** · 机器人成功率 89% 对 48%，未扫描区 87%。
- **适用条件 / 局限** · 同楼未扫描不代表跨新楼直接泛化，依赖扫描一致性。

**可复用机制** · 把地图变成可验证的任务生成根，而非仅在推理作为描述性提示。

<a id="paper-155557"></a>

## One-Shot Generative Flows: Existence and Obstructions

[官方论文页](https://neurips.cc/virtual/2026/poster/155557) · [作者来源](https://openreview.net/forum?id=4fhoYxsUYq)

- **问题 / 瓶颈** · 流匹配训练目标允许多峰，但速度场未必能一步积分。
- **核心创新 / 方法** · 由条件统计的 PDE 刻画零加速度，对高斯构造可行过程并证明分离多峰的障碍。
- **Baseline** · 独立端点的常见生成流设置。
- **Benchmark** · 高斯端点及充分分开的目标模式；理论可实现性。
- **关键结果 / 消融** · 任意高斯端点可构造，而某些多峰目标不存在直线流。
- **适用条件 / 局限** · 结论依赖独立端点和模式分离条件。

**可复用机制** · 将单步误差区分为估计误差和速度族自身限制。

<a id="paper-151541"></a>

## One-Shot Private Confidence Regions via Resampling

[官方论文页](https://neurips.cc/virtual/2026/poster/151541) · [作者来源](https://openreview.net/forum?id=ZueKmUuWjT)

- **问题 / 瓶颈** · 为每次重采样引入独立隐私损失会随次数增长。
- **核心创新 / 方法** · 对有放回和无放回分情况界定最终分位数的敏感性。
- **Baseline** · 逐重样本私有化。
- **Benchmark** · 均值类、分位数和退化 U 统计；非渐近隐私和效用。
- **关键结果 / 消融** · 重采样次数的隐私代价分别为对数级和无关，而非平方根级。
- **适用条件 / 局限** · 依赖全局或可算平滑敏感度及发布范围。

**可复用机制** · 仅保护需要公开的统计量，并防止中间样本被当作无害调试输出。

<a id="paper-155832"></a>

## One Temperature to Rule Them All?

[官方论文页](https://neurips.cc/virtual/2026/poster/155832) · [作者来源](https://openreview.net/forum?id=2YBreEieXy)

- **问题 / 瓶颈** · 固定温度在多预算比较中会低估简单基线。
- **核心创新 / 方法** · 逐题估计不同温度的成功概率，并计算最优的预算分配。
- **Baseline** · 按 K 调优的单温度。
- **Benchmark** · 多模型多数据，逐题成功与 pass@K。
- **关键结果 / 消融** · 多温度有收益但通常不大；难题最佳温度差别随难度缓慢增大。
- **适用条件 / 局限** · 选定的模型域和候选预算影响差值。

**可复用机制** · 报告温度选择的附加试验成本，并在相同预算下比较。

<a id="paper-154791"></a>

## One-Time Soft Alignment Enables Resilient Learning without Weight Transport

[官方论文页](https://neurips.cc/virtual/2026/poster/154791) · [作者来源](https://openreview.net/forum?id=AvMF6ujTNu)

- **问题 / 瓶颈** · 固定随机反馈深层学习不稳，逐步权重共享增加同步。
- **核心创新 / 方法** · 在起点软对齐前向和反馈矩阵，之后保持局部反馈训练。
- **Baseline** · 随机反馈及标准反传。
- **Benchmark** · 深层训练精度、谱、泛化与鲁棒性；具名基准待查。
- **关键结果 / 消融** · 摘要报告接近反传，适度不对称的方案可改善所测鲁棒性。
- **适用条件 / 局限** · 依赖初始化比例和体系，分布变化待核实。

**可复用机制** · 控制初始角度，测是否可在无持续同步下维持有效梯度。

<a id="paper-151767"></a>

## One View Is Enough: In-the-Wild Monocular Pretraining for Novel View Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/151767) · [作者来源](https://openreview.net/forum?id=YC0au39jWi)

- **问题 / 瓶颈** · 专用多视图数据限制场景覆盖，推理深度预估又增时延。
- **核心创新 / 方法** · 冻结深度网络生成目标位姿视图，用掩码监督可见区，并对新显露区另加生成目标。
- **Baseline** · 多视图监督及推理需深度的替代方案。
- **Benchmark** · RealEstate10K、DL3DV，三千万单图预训与短多视角微调。
- **关键结果 / 消融** · 未用多视监督在 DL3DV 优于所测方法，报告 116 FPS。
- **适用条件 / 局限** · 伪深度可靠性、标定和难遮挡待查。

**可复用机制** · 控制训练期几何教师与部署消耗，并在显露区单独评估重建。

<a id="paper-153304"></a>

## One World, Dual Timeline: Decoupled Spatio-Temporal Gaussian Scene Graph for 4D Cooperative Driving Reconstruction

[官方论文页](https://neurips.cc/virtual/2026/poster/153304) · [作者来源](https://openreview.net/forum?id=MGgkFy8IUf)

- **问题 / 瓶颈** · 单一位姿解释异时观测会产生动态鬼影。
- **核心创新 / 方法** · 各物体共享规范高斯表示，按源捕获时间维护不同姿态。
- **Baseline** · 单一时间线的高斯场景图。
- **Benchmark** · 车路协同四维重建，评估动态目标外观和位置。
- **关键结果 / 消融** · 理论上单轨时间损失随速度与时间差乘积的平方增长。
- **适用条件 / 局限** · 需要可靠时间戳和本体对应，实证幅度待查。

**可复用机制** · 按速度和同步偏移分层检验，先排除表征问题再调优化。

<a id="paper-155423"></a>

## On JEPA Isotropy

[官方论文页](https://neurips.cc/virtual/2026/poster/155423) · [作者来源](https://openreview.net/forum?id=5mi1bkx1o8)

- **问题 / 瓶颈** · 瓶颈压缩与较差谱条件会造成不同风险。
- **核心创新 / 方法** · 将线性 JEPA 改写为降秩回归，分解不可约误差与超额风险。
- **Baseline** · 通用各向同性嵌入设计。
- **Benchmark** · 线性理论及数值实验，测秩、风险和谱条件。
- **关键结果 / 消融** · 预测秩随目标异质度增长到瓶颈，白化谱决定优化界。
- **适用条件 / 局限** · 线性 ERM 条件限制深层外推。

**可复用机制** · 先测试低维瓶颈是否太窄，再决定谱正则能解决多少误差。

<a id="paper-149964"></a>

## On Length Bias in EEG-to-Text Decoding

[官方论文页](https://neurips.cc/virtual/2026/poster/149964) · [作者来源](https://openreview.net/forum?id=lsTNd5Lyoe)

- **问题 / 瓶颈** · 模型可能靠持续时长识别句子而非读取神经内容。
- **核心创新 / 方法** · 跨被试持出，配对真实和长度匹配噪声，再做架构分解。
- **Baseline** · 十个分类器、三个生成器，与仅保留长度结构的输入。
- **Benchmark** · 三套英语听读 EEG 数据，测句子解码。
- **关键结果 / 消融** · 摘要报告长度显著抬高成绩且架构差异大，分类器中 BIOT 不受该对照影响。
- **适用条件 / 局限** · 不代表残余效果必为神经语义，其他非内容混杂仍需检查。

**可复用机制** · 刻意保留非目标协变量并替换真实信号，估计捷径独自能解释多少表现。

<a id="paper-154789"></a>

## Online Active Testing: Adaptive Importance Sampling for Unbiased Risk Estimation in Data Streams

[官方论文页](https://neurips.cc/virtual/2026/poster/154789) · [作者来源](https://openreview.net/forum?id=AyJOqDpoNN)

- **问题 / 瓶颈** · 固定抽样漏掉少数影响风险精度的大损失。
- **核心创新 / 方法** · 自适应决定标注，并按入样概率进行逆加权。
- **Baseline** · 均匀标注及可回看样本池的主动测试。
- **Benchmark** · 流式回归及分类，含均方、绝对、零一和对数损失。
- **关键结果 / 消融** · 给出无偏、偏离界及一致性的理论保证，并导出最小方差策略。
- **适用条件 / 局限** · 需记录真实查询概率且非零采样支持；未知二阶矩估计需核实。

**可复用机制** · 将标签预算集中到高风险区域，但保留概率日志以恢复总体风险。

<a id="paper-150540"></a>

## Online Allocation with Differential Privacy

[官方论文页](https://neurips.cc/virtual/2026/poster/150540) · [作者来源](https://openreview.net/forum?id=hO8NU92Rtb)

- **问题 / 瓶颈** · 隐私概念不同导致优化边界变化。
- **核心创新 / 方法** · 构造近优隐私分配框架，并用镜像下降及 FTRL 实现。
- **Baseline** · 非隐私与不同隐私定义。
- **Benchmark** · 对抗、随机理论及电池边缘路由实验。
- **关键结果 / 消融** · 摘要报告满足相应隐私条件并接近最优。
- **适用条件 / 局限** · 具体隐私预算及持续组合需核。

**可复用机制** · 按相同预算比较效用损失，注明保护对象。

<a id="paper-151416"></a>

## Online Allocation with Unknown Shared Supply

[官方论文页](https://neurips.cc/virtual/2026/poster/151416) · [作者来源](https://openreview.net/forum?id=apuN36lY0N)

- **问题 / 瓶颈** · 未见未来需求，跨站点提前分配会导致缺货。
- **核心创新 / 方法** · GPA 用确定阈值，增设可抵御坏预测的学习扩展。
- **Baseline** · 离线最优及自然在线基线。
- **Benchmark** · 合成及现实数据、稀缺供应。
- **关键结果 / 消融** · 证明紧 4/3 比率加误差项；摘要称实证改善。
- **适用条件 / 局限** · 依赖运输费和不可回补假设。

**可复用机制** · 扫描预测误差、供应规模及不可服务量。

<a id="paper-151573"></a>

## Online Bayesian Calibration under Gradual and Abrupt System Changes

[官方论文页](https://neurips.cc/virtual/2026/poster/151573) · [作者来源](https://openreview.net/forum?id=Zabh2YskEn)

- **问题 / 瓶颈** · 将偏差误当参数会破坏可辨识，平滑更新又难跟随突变。
- **核心创新 / 方法** · 参数用粒子更新，差异用条件 GP，变点时重置。
- **Baseline** · 滑窗贝叶斯和数据同化。
- **Benchmark** · 合成与工厂模拟，校准与预测。
- **关键结果 / 消融** · 渐变时更准，重启改善突变稳定。
- **适用条件 / 局限** · 依赖突变检出和仿真可靠性。

**可复用机制** · 分别报平稳误报、渐变追踪和突变延迟。

<a id="paper-151000"></a>

## Online Bayesian Recalibration of Brain–Computer Interfaces with Language Model Potentials

[官方论文页](https://neurips.cc/virtual/2026/poster/151000) · [作者来源](https://openreview.net/forum?id=dg1ZRMGStk)

- **问题 / 瓶颈** · 错误硬标签会积累解码偏差。
- **核心创新 / 方法** · 按贝叶斯滤波近似用 top-k 软标签及参数漂移先验。
- **Baseline** · 硬标签持续校准与既有脑机解码。
- **Benchmark** · 合成漂移、手写及语音脑机数据。
- **关键结果 / 消融** · 手写 WER 持续低于 3%，比先前参考近 30% 改善。
- **适用条件 / 局限** · 非临床有效性，语言先验偏差需核。

**可复用机制** · 分别比较候选质量、漂移强度和累积误差。

<a id="paper-156664"></a>

## Online Bernstein-von Mises theorem

[官方论文页](https://neurips.cc/virtual/2026/poster/156664) · [作者来源](https://neurips.cc/virtual/2026/poster/156664)

- **问题 / 瓶颈** · 逐批投影误差可能传到最终后验。
- **核心创新 / 方法** · 每轮做变分近似并分析终点的 Bernstein–von Mises 性质。
- **Baseline** · 全批后验。
- **Benchmark** · 正规模型下的小批次理论。
- **关键结果 / 消融** · 批次超过维度相关阈值时误差渐近可忽略。
- **适用条件 / 局限** · 依赖模型正规性与阈值；有限样本待核。

**可复用机制** · 在同数据下比较批尺寸导致的覆盖和均值偏差。

<a id="paper-151323"></a>

## Online Budget Allocation with Censored Semi-Bandit Feedback

[官方论文页](https://neurips.cc/virtual/2026/poster/151323) · [作者来源](https://openreview.net/forum?id=bMskKiSDl8)

- **问题 / 瓶颈** · 预算少的任务反馈被删失。
- **核心创新 / 方法** · 用乐观分配，在收益递减下获得更快实例界。
- **Baseline** · 全反馈算法的理论下界与普通老虎机。
- **Benchmark** · 删失半反馈预算分配。
- **关键结果 / 消融** · 收益递减时多对数，通用时近 K√T 且有匹配下界。
- **适用条件 / 局限** · 要求任务成功概率单调。

**可复用机制** · 按费用和成功概率仿真，分报观测偏差与遗憾。

<a id="paper-149162"></a>

## Online Causal Configuration for Networked Systems via Doubly Robust Steady-State Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149162) · [作者来源](https://openreview.net/forum?id=sO7mOWC5TC)

- **问题 / 瓶颈** · 即时反馈与独立单元模型不适用。
- **核心创新 / 方法** · 用暴露表示、重叠采样和双稳健稳态估计组织配置选择。
- **Baseline** · 即时分配和普通独立估计路线。
- **Benchmark** · METR-LA 与 FlockLab 的受控回放。
- **关键结果 / 消融** · 摘要报告识别质量与部署成本权衡。
- **适用条件 / 局限** · 干扰近似及残留依赖限制解释。

**可复用机制** · 在良性仿真分开验稳态误差和探测导致的服务变化。

<a id="paper-148517"></a>

## Online Change-point Detection using Foundation Probabilistic Forecasting Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148517) · [作者来源](https://openreview.net/forum?id=xIyD2dHHEW)

- **问题 / 瓶颈** · 时序的趋势、季节性和异方差影响固定阈值。
- **核心创新 / 方法** · 以概率基座预测形成近标准高斯统计，缓冲以免模型过快适应，并 bootstrap 边界。
- **Baseline** · 经典 CUSUM、MOSUM 与现有检测。
- **Benchmark** · 含多种趋势、季节及自相关的仿真。
- **关键结果 / 消融** · 摘要报告检测有竞争力且无需显式设变化前模型。
- **适用条件 / 局限** · 相关统计和分位校准误差需检查。

**可复用机制** · 同误报率比较检测延迟，缓冲长度做敏感性分析。

<a id="paper-153343"></a>

## Online Conformal Abstention for Factuality Control Under Adversarial Bandit Feedback

[官方论文页](https://neurips.cc/virtual/2026/poster/153343) · [作者来源](https://openreview.net/forum?id=M3UtnMEDaL)

- **问题 / 瓶颈** · 只观察已选回应反馈会使调阈偏差。
- **核心创新 / 方法** · 将老虎机遗憾换成风险界，提取拒答结构允许的额外反馈。
- **Baseline** · 全信息和现有保形拒答参考。
- **Benchmark** · 非平稳、对抗性问答反馈。
- **关键结果 / 消融** · 理论给平方根级控制，报告覆盖有竞争力。
- **适用条件 / 局限** · 用户赞踩不必等于事实真值。

**可复用机制** · 用独立标注估误反馈及风险，同时报告实际覆盖。

<a id="paper-153920"></a>

## Online Control with Multiple Sensors

[官方论文页](https://neurips.cc/virtual/2026/poster/153920) · [作者来源](https://openreview.net/forum?id=HeDwP6bLo0)

- **问题 / 瓶颈** · 全拼接会使理论代价随传感器数放大。
- **核心创新 / 方法** · 用 FTRL 和策略类 L1 结构分析遗憾。
- **Baseline** · 直接套用部分观测控制。
- **Benchmark** · 随机二次及对抗凸代价的线性模型。
- **关键结果 / 消融** · 依传感器数为多对数，时间为平方根量级。
- **适用条件 / 局限** · 仅和受限最优单传感器比较。

**可复用机制** · 依传感器数和噪声分组，报告相对单传感器成本。

<a id="paper-155444"></a>

## Online Data Selection for Instruction Tuning via Gaussian Processes

[官方论文页](https://neurips.cc/virtual/2026/poster/155444) · [作者来源](https://openreview.net/forum?id=5Z8GeMizku)

- **问题 / 瓶颈** · 随机小批只做局部筛选，忽略训练中价值变化。
- **核心创新 / 方法** · GP 建模连续效用，固定共享 Hedge 思路更新策略。
- **Baseline** · GREATS 及批内选择。
- **Benchmark** · 三个微调数据集，考察最终表现。
- **关键结果 / 消融** · 摘要报告超过基线，有动态遗憾保证。
- **适用条件 / 局限** · 代理训练成本及语义漂移待核。

**可复用机制** · 匹配训练和筛选总耗时，再对比跨批次收益。

<a id="paper-151530"></a>

## Online Differentially Private Consistent Clustering

[官方论文页](https://neurips.cc/virtual/2026/poster/151530) · [作者来源](https://openreview.net/forum?id=ZzXRQVvFXC)

- **问题 / 瓶颈** · 专用私有算法可能随时间大幅改中心。
- **核心创新 / 方法** · 把输入变为私有半核集流，用后处理复用非私有聚类。
- **Baseline** · 既有私有流式 k-means 和 k-median。
- **Benchmark** · 近似、空间、运行时间及一致性理论。
- **关键结果 / 消融** · 匹配或改善已知界并继承所选算法一致性。
- **适用条件 / 局限** · 隐私及长期近似条件待核。

**可复用机制** · 在等预算核查中心漂移和目标并报资源。

<a id="paper-148149"></a>

## Online Directional Regression for Streaming Sufficient Dimension Reduction

[官方论文页](https://neurips.cc/virtual/2026/poster/148149) · [作者来源](https://openreview.net/forum?id=zuuQ9Axt80)

- **问题 / 瓶颈** · 只靠一阶矩会漏对称和交互结构。
- **核心创新 / 方法** · 递推估标准化、跟踪广义子空间并以加权重采样选维数。
- **Baseline** · 一阶方法及反复批量方向回归。
- **Benchmark** · 合成与真实流式数据。
- **关键结果 / 消融** · 报告适应多种依赖并节约计算，有一致性保证。
- **适用条件 / 局限** · 需要正则条件及数据分片。

**可复用机制** · 在均值不变但方差相关的模拟中比较恢复。

<a id="paper-139644"></a>

## Online Evaluation of LLMs via Dyadic Designs

[官方论文页](https://neurips.cc/virtual/2026/poster/139644) · [作者来源](https://openreview.net/forum?id=DjieumWYZe)

- **问题 / 瓶颈** · 完全随机会增加两组难度差异。
- **核心创新 / 方法** · 以二进层次近邻在线平衡，无需选分层超参数。
- **Baseline** · 完全随机及最优调参的在线分层。
- **Benchmark** · AlpacaEval 805 提示的顺序模拟。
- **关键结果 / 消融** · 与随机相比失配约低 6 倍。
- **适用条件 / 局限** · 依赖到达设定及预测信号，真实延迟待验。

**可复用机制** · 预注册协变量并同时记录组间平衡和效果区间。

<a id="paper-153060"></a>

## Online Fair Division Meets Reordering Buffers

[官方论文页](https://neurips.cc/virtual/2026/poster/153060) · [作者来源](https://openreview.net/forum?id=OJg3z0LXM4)

- **问题 / 瓶颈** · 直接分配在混合正负估值时难保证无羡慕。
- **核心创新 / 方法** · 在缓冲里构造匹配，逐步分配大多数项。
- **Baseline** · 无缓冲和全离线路线。
- **Benchmark** · 加性个人 k 值模型的理论。
- **关键结果 / 消融** · 线性容量可每步达 EF1，多数时达无羡慕。
- **适用条件 / 局限** · 依赖个人取值数，通用模型界不同。

**可复用机制** · 对比等待预算与公平质量，同时报最坏等待。

<a id="paper-150024"></a>

## Online Finetuning Decision Transformers with Pure RL Gradients

[官方论文页](https://neurips.cc/virtual/2026/poster/150024) · [作者来源](https://openreview.net/forum?id=lKf0a3wiQx)

- **问题 / 瓶颈** · 事后重标有利监督却改变重要性比的含义。
- **核心创新 / 方法** · 用子轨迹更新、序列似然和主动采样适配 GRPO。
- **Baseline** · 现有在线决策 Transformer。
- **Benchmark** · 多个在线决策基准，具体待核。
- **关键结果 / 消融** · 报告优于基线。
- **适用条件 / 局限** · 离线到在线条件匹配及更新成本待核。

**可复用机制** · 分别消融是否重标和优化粒度，记录比值偏差。

<a id="paper-155670"></a>

## Online Imitation Learning for Stabilizing Vlasov--Poisson Plasmas

[官方论文页](https://neurips.cc/virtual/2026/poster/155670) · [作者来源](https://openreview.net/forum?id=3sKugTZ9Le)

- **问题 / 瓶颈** · 小克隆误差可能沿滚动迅速放大。
- **核心创新 / 方法** · 对比离线行为克隆与使用在线纠正状态的模仿。
- **Baseline** · 行为克隆。
- **Benchmark** · 文中一维受控动力学仿真及稳定理论。
- **关键结果 / 消融** · 在线方案可维持更长时域稳定。
- **适用条件 / 局限** · 不能外推实际安全关键控制。

**可复用机制** · 在良性合成不稳定系统报告误差随时域增长。

<a id="paper-150975"></a>

## Online Learning in Stabilized Linear Dynamical Games with Adversarial Disturbances

[官方论文页](https://neurips.cc/virtual/2026/poster/150975) · [作者来源](https://openreview.net/forum?id=ds0HbzOzSs)

- **问题 / 瓶颈** · 多方动作共同改变后续状态及损失。
- **核心创新 / 方法** · 比较不同反馈下的带记忆梯度更新，并对共同目标建立势博弈。
- **Baseline** · 单代理非随机控制或线性二次博弈。
- **Benchmark** · 线性系统中的对抗扰动理论。
- **关键结果 / 消融** · 给次线性近优遗憾和共同目标下均衡追踪。
- **适用条件 / 局限** · 需稳定基线和完整状态观测。

**可复用机制** · 固定相同扰动，比较反馈范围与个体遗憾。

<a id="paper-153773"></a>

## Online Learning of Group-Stable Coalition Structures

[官方论文页](https://neurips.cc/virtual/2026/poster/153773) · [作者来源](https://openreview.net/forum?id=Ilrh0L7gOZ)

- **问题 / 瓶颈** · 偏好未知且反馈噪声使临时稳定可能误判。
- **核心创新 / 方法** · 结合乐观与悲观估计探索、认证。
- **Baseline** · 常见群体稳定性条件及已知偏好参照。
- **Benchmark** · 合成联盟实例与理论。
- **关键结果 / 消融** · 存在稳定划分时误差和遗憾次线性；不存在时错误次数常数级。
- **适用条件 / 局限** · 依赖偏好和反馈设定。

**可复用机制** · 分别评价存在性判断与实际长期违例。

<a id="paper-149131"></a>

## Online Learning on Hidden-Convex Losses via Algorithmic Equivalence: Optimal Regret, Geometric Barrier, and Bandit Feedback

[官方论文页](https://neurips.cc/virtual/2026/poster/149131) · [作者来源](https://openreview.net/forum?id=sdtnLayEs7)

- **问题 / 瓶颈** · 存在凸坐标并不足以使原坐标优化等价。
- **核心创新 / 方法** · 将原梯度步与镜像步对齐，刻画相容的充要条件。
- **Baseline** · 先前隐凸 OGD 及标准凸在线梯度。
- **Benchmark** · 全反馈和单点反馈理论，含反例。
- **关键结果 / 消融** · 相容时平方根遗憾，不相容可线性；单点为 T^(3/4)。
- **适用条件 / 局限** · 限光滑和几何条件。

**可复用机制** · 先审计坐标度量，再选原梯度或显式镜像更新。

<a id="paper-155730"></a>

## Online Learning via Learned Latent Bayesian Tracking

[官方论文页](https://neurips.cc/virtual/2026/poster/155730) · [作者来源](https://openreview.net/forum?id=3NNBL5KQ3u)

- **问题 / 瓶颈** · 全参数滤波不可扩展，手选子空间又不适配漂移。
- **核心创新 / 方法** · 离线元学状态演化与升维映射，在线用扩展 Kalman 滤波再复原权重。
- **Baseline** · 现有在线学习和贝叶斯滤波。
- **Benchmark** · 时变无线信道与非平稳图像分类。
- **关键结果 / 消融** · 摘要报告适应速度、准确及成本改善。
- **适用条件 / 局限** · 依赖离线漂移覆盖。

**可复用机制** · 将在线更新维度而非模型容量压小，用可执行滤波处理不确定性。

<a id="paper-151773"></a>

## Online Learning with Certified Unlearning over Graphs

[官方论文页](https://neurips.cc/virtual/2026/poster/151773) · [作者来源](https://openreview.net/forum?id=Y9ZVSXcXaD)

- **问题 / 瓶颈** · 删点或边影响可经邻接扩大，完整重训成本高。
- **核心创新 / 方法** · 按近期批量信息做二阶回溯校正。
- **Baseline** · 从头训练及事后遗忘。
- **Benchmark** · 多个图集；结点、边及特征删除。
- **关键结果 / 消融** · 摘要报告低成本达到相近效用；偶尔删除仅增加加性遗憾。
- **适用条件 / 局限** · 高频删除、传播深度和认证条件需单验。

**可复用机制** · 保留局部演化所需统计，以便把删除纳入正常增量更新。

<a id="paper-148737"></a>

## Online Localized Conformal Prediction

[官方论文页](https://neurips.cc/virtual/2026/poster/148737) · [作者来源](https://openreview.net/forum?id=vPeDJdLEKg)

- **问题 / 瓶颈** · 全局校准在异质输入上产生过宽区间。
- **核心创新 / 方法** · 结合局部校准及在线适应，用约束凸优化选带宽。
- **Baseline** · 自适应共形推断。
- **Benchmark** · 模拟和真实序列的长期覆盖与区间宽度。
- **关键结果 / 消融** · 摘要报告覆盖有效且区间较窄。
- **适用条件 / 局限** · 长期覆盖不保证任时点条件覆盖。

**可复用机制** · 样本流有异质性时保留局部校准，在线监控各局部规则的宽度收益。

<a id="paper-153821"></a>

## Online Maximization of Non-Decomposable Test and Population Utilities

[官方论文页](https://neurips.cc/virtual/2026/poster/153821) · [作者来源](https://openreview.net/forum?id=IT4rHivVsd)

- **问题 / 瓶颈** · 混淆矩阵效用不能按单例独立相加。
- **核心创新 / 方法** · 以随机 Dinkelbach 更新按流数据估分式参数，并将在线预测转换为批模型。
- **Baseline** · 直接逐样本风险优化以及总体效用比较。
- **Benchmark** · Jaccard、F 指标及相关基准。
- **关键结果 / 消融** · 相关分式指标可达约 n^-0.5 遗憾，略去对数。
- **适用条件 / 局限** · 依赖条件概率误差及指标形式。

**可复用机制** · 使用全局效用诱导的阈值更新，而非直接用局部替代损失。

<a id="paper-155249"></a>

## Online Minimum Description Length Passive-Aggressive Algorithms

[官方论文页](https://neurips.cc/virtual/2026/poster/155249) · [作者来源](https://openreview.net/forum?id=77tofmsGFn)

- **问题 / 瓶颈** · 概率分布和压缩器缺少普通向量间隔。
- **核心创新 / 方法** · 每类一压缩器，违反码长间隔时以信息投影改真类概率。
- **Baseline** · 被动攻击式在线分类及压缩近似。
- **Benchmark** · 文本等序列分类。
- **关键结果 / 消融** · 摘要展示自适应词典可近似实现。
- **适用条件 / 局限** · 压缩分数需对序列长度和初始化可比。

**可复用机制** · 在无固定特征空间时使用压缩长度衡量样本属于各群体的证据。

<a id="paper-151634"></a>

## Online Min-Max Optimization: From Individual Regrets to Cumulative Saddle Points

[官方论文页](https://neurips.cc/virtual/2026/poster/151634) · [作者来源](https://openreview.net/forum?id=Z7Fzxtf74w)

- **问题 / 瓶颈** · 静态 Nash 遗憾可能与个体遗憾相冲。
- **核心创新 / 方法** · 以累计对偶差替代，并分析动态鞍点。
- **Baseline** · 静态均衡遗憾及各方个体遗憾。
- **Benchmark** · 强凸凹、指数凹及部分 PL 的理论。
- **关键结果 / 消融** · 摘要给出兼容指标的次线性界。
- **适用条件 / 局限** · 保证依赖函数类。

**可复用机制** · 先验证两层目标是否兼容，再联合报告算法均衡与个体后悔。

<a id="paper-154670"></a>

## Online Resource Allocation With General Constraints

[官方论文页](https://neurips.cc/virtual/2026/poster/154670) · [作者来源](https://openreview.net/forum?id=BtOcFcAUxb)

- **问题 / 瓶颈** · 一般约束不总有零消耗安全动作。
- **核心创新 / 方法** · 以弱适应分析控制拉格朗日乘子，分别处理硬预算和其他违反量。
- **Baseline** · 只含预算的在线分配。
- **Benchmark** · 随机与对抗序列的动态比较。
- **关键结果 / 消融** · 严格满足预算，同时一般约束累计违反约根号 T 量级。
- **适用条件 / 局限** · 依赖离线可行裕度；对抗保证有对应系数。

**可复用机制** · 不要把软约束都当有安全动作的资源账，分别验证可行性。

<a id="paper-155110"></a>

## Online Set Learning from Precision and Recall Feedback

[官方论文页](https://neurips.cc/virtual/2026/poster/155110) · [作者来源](https://openreview.net/forum?id=8KsPIzpp5i)

- **问题 / 瓶颈** · 精度和召回抽样分别依赖提交集合或目标集合。
- **核心创新 / 方法** · 以 VC 维定可学性，并处理两类反馈诱导的依赖。
- **Baseline** · 全监督 ERM 和适当学习规则。
- **Benchmark** · 集合在线学习的可实现及不可实现条件。
- **关键结果 / 消融** · 有限 VC 等价于可学，但 ERM 乃至所有适当规则可失效。
- **适用条件 / 局限** · 不是最佳遗憾率的完整刻画。

**可复用机制** · 验收学习规则前写明谁决定被观察元素，防止错误的独立性假定。

<a id="paper-151236"></a>

## On Lipschitz Explosion in Deep Neural Networks with Normalization: Consequences for Optimization and Robustness

[官方论文页](https://neurips.cc/virtual/2026/poster/151236) · [作者来源](https://openreview.net/forum?id=btvnW0Xn5i)

- **问题 / 瓶颈** · 逐层范数小不能保证全网稳定。
- **核心创新 / 方法** · 分析归一化下两个 Lipschitz 常数，并做鲁棒性对照。
- **Baseline** · 逐层谱范数控制。
- **Benchmark** · 线性归一化网络理论与 MNIST、Fashion-MNIST、CIFAR-10。
- **关键结果 / 消融** · 两种敏感度可随深度指数增大。
- **适用条件 / 局限** · 最坏结果不能代替经验稳定性结论。

**可复用机制** · 需要证书时独立测整个归一化计算图，不仅检查单层权重。

<a id="paper-155688"></a>

## On Making $SE(2)$-Invariant Networks Optimal

[官方论文页](https://neurips.cc/virtual/2026/poster/155688) · [作者来源](https://openreview.net/forum?id=3gDFvmTZXb)

- **问题 / 瓶颈** · 直接改所有非线性层会提高工程成本。
- **核心创新 / 方法** · 从不变量理论建 SE(2) 最小特征映射，接入常规 CNN。
- **Baseline** · 既有等变骨干。
- **Benchmark** · 旋转平移分类与成本。
- **关键结果 / 消融** · 摘要报告精度相近或改善且计算更省。
- **适用条件 / 局限** · 不适用需要输出位置姿态的任务。

**可复用机制** · 先根据输出定义选择不变还是等变，再决定要保留结构的层。

<a id="paper-155630"></a>

## On Minimizing Regret in Fixed-Confidence $\varepsilon$-Best Arm Identification

[官方论文页](https://neurips.cc/virtual/2026/poster/155630) · [作者来源](https://openreview.net/forum?id=48e13H6fg5)

- **问题 / 瓶颈** · 采样最省的算法可能在识别期损失较高。
- **核心创新 / 方法** · 以遗憾感知信息下界分析 KL-UCB 加贪心。
- **Baseline** · 固定置信最佳臂识别与信息论下界。
- **Benchmark** · 错误概率趋零的渐近理论。
- **关键结果 / 消融** · 若分布为高斯等可达到最优遗憾常数。
- **适用条件 / 局限** · 限相关分布及渐近区。

**可复用机制** · 实际部署把识别过程中的收益损失与样本数分别作为设计目标。

<a id="paper-148933"></a>

## On Neural Scaling Laws for Weather Emulation through Continual Training

[官方论文页](https://neurips.cc/virtual/2026/poster/148933) · [作者来源](https://openreview.net/forum?id=u9jpPYohUA)

- **问题 / 瓶颈** · 只测单个预算无法看出模型数据和算力最优配置。
- **核心创新 / 方法** · 训练可扩展 Swin，扫 IsoFLOP，并在降温阶段调多步或频谱目标。
- **Baseline** · 常规余弦学习率。
- **Benchmark** · 天气模拟，多模型数据和算力规模。
- **关键结果 / 消融** · 摘要报告优于余弦且后段可改善滚动与频谱。
- **适用条件 / 局限** · 外推受模型和气象数据范围限制。

**可复用机制** · 从可比较训练阶段获得尺度曲线，再在低学习率段适配实际预测口径。

<a id="paper-151639"></a>

## On objective mismatch in molecular retrieval from tandem mass spectrometry

[官方论文页](https://neurips.cc/virtual/2026/poster/151639) · [作者来源](https://openreview.net/forum?id=Z655zMeBt6)

- **问题 / 瓶颈** · 高指纹相似目标不总能找到真实候选。
- **核心创新 / 方法** · 用决策遗憾分析候选集合结构，并比较多种监督损失。
- **Baseline** · 传统指纹相似损失。
- **Benchmark** · MassSpecGym 结构识别。
- **关键结果 / 消融** · 摘要报告指纹与检索间 Pareto 折中。
- **适用条件 / 局限** · 取决于候选库及相似性结构。

**可复用机制** · 中间预测和最终选择要分别验收，必要时直接对齐候选集决策目标。

<a id="paper-148999"></a>

## On Observation Time for Recovering Latent Hawkes Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/148999) · [作者来源](https://openreview.net/forum?id=tZwHSbbaof)

- **问题 / 瓶颈** · 时间不足会使少量真实关联无证据。
- **核心创新 / 方法** · 先对截断分箱事件做筛选，再最小二乘精化。
- **Baseline** · 信息下界及既有点过程估计。
- **Benchmark** · 稀疏弱相互作用平稳 Hawkes。
- **关键结果 / 消融** · 对 d 个实体，在所设类中 log d 量级必要且充分。
- **适用条件 / 局限** · 需满足平稳、弱耦合和稀疏条件。

**可复用机制** · 用理论支持的观测窗口做边恢复试验，再评价延长观测与加密采样的作用。

<a id="paper-148938"></a>

## On-Policy Consistency Training Improves LLM Safety with Minimal Capability Degradation

[官方论文页](https://neurips.cc/virtual/2026/poster/148938) · [作者来源](https://openreview.net/forum?id=u3h9PXcNHZ)

- **问题 / 瓶颈** · 离线 SFT 容易记表面形式并损害通用能力。
- **核心创新 / 方法** · 由当前策略出响应，再让同模型在对应的对比条件提供监督。
- **Baseline** · 离线一致性 SFT 和基座。
- **Benchmark** · 三模型族的迎合、抗不安全请求及安全意识。
- **关键结果 / 消融** · 摘要报告迎合 8.1% 对基座 15.4%，通用能力退化较少。
- **适用条件 / 局限** · 安全评估不覆盖所有部署条件。

**可复用机制** · 让监督数据分布跟随训练中的策略，并以未见场景确认对齐泛化。

<a id="paper-148864"></a>

## On-Policy Counterfactual Influence

[官方论文页](https://neurips.cc/virtual/2026/poster/148864) · [作者来源](https://openreview.net/forum?id=uca0HSKmnM)

- **问题 / 瓶颈** · 普通影响函数只追单次权重偏移。
- **核心创新 / 方法** · 将策略、后续采样与再更新的耦合纳入反事实影响。
- **Baseline** · 监督式或离线影响函数与实测删事件。
- **Benchmark** · 语言模型强化，AdamW 等。
- **关键结果 / 消融** · 摘要报告更准确预测删事件效果，归因加权重训有增益。
- **适用条件 / 局限** · 依赖反事实估计与训练噪声。

**可复用机制** · 用删去事件后的真实训练对照校准影响值，不只验单步梯度。

<a id="paper-149770"></a>

## On-Policy Distillation with Open Property-Equivalence Reward for LLM-Based NL-to-SVA Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/149770) · [作者来源](https://openreview.net/forum?id=nRVe5pE6sQ)

- **问题 / 瓶颈** · 总准确掩盖时序算子模板化。
- **核心创新 / 方法** · 在线采样学生断言，以形式等价验证加权教师前向 KL。
- **Baseline** · SFT、专用与通用模型。
- **Benchmark** · NL2SVA-Human / Machine，多候选通过率。
- **关键结果 / 消融** · 摘要报告 pass@1、5、10 领先。
- **适用条件 / 局限** · 依赖可验证性质覆盖，形式规范仍需审核。

**可复用机制** · 让教师密集监督建立在已核验的功能正确性上，而不只匹配文本。

<a id="paper-153484"></a>

## On-Policy Hindsight Distillation for Early Risk Prediction

[官方论文页](https://neurips.cc/virtual/2026/poster/153484) · [作者来源](https://openreview.net/forum?id=L26pEowauj)

- **问题 / 瓶颈** · 弱早期信号往往只有随访后才清楚。
- **核心创新 / 方法** · 先从早期记录生成理由，再在多个扰动随访视图下蒸馏稳定信号。
- **Baseline** · 只用早期记录或终局标签。
- **Benchmark** · 多神经退行队列的远期风险。
- **关键结果 / 消融** · 摘要报告优于所比基线。
- **适用条件 / 局限** · 须严格时间隔离，回顾验证不等于临床效用。

**可复用机制** · 把未来信息仅留在训练教师，并用扰动一致性抑制事后偶然线索。

<a id="paper-151999"></a>

## On Reparameterizing the Score Function

[官方论文页](https://neurips.cc/virtual/2026/poster/151999) · [作者来源](https://openreview.net/forum?id=WGc94WFesu)

- **问题 / 瓶颈** · 冻结历史的得分函数没有利用下游分布对早先选择的依赖。
- **核心创新 / 方法** · 放松前缀以传播下游梯度，再以中心化和闭式系数控制方差。
- **Baseline** · 普通策略梯度和不同离散放松。
- **Benchmark** · 自回归序列、弱和强时序结构，测梯度方差。
- **关键结果 / 消融** · 含已学时序依赖的策略收益较大，嵌入放松提供明显降方差。
- **适用条件 / 局限** · 直接加路径项有偏，条件与计算成本待核实。

**可复用机制** · 先测轨迹相关性及方差，再决定控制变量的复杂度。

<a id="paper-150399"></a>

## On the Burden of Achieving Fairness in Conformal Prediction

[官方论文页](https://neurips.cc/virtual/2026/poster/150399) · [作者来源](https://openreview.net/forum?id=iJfigzq6s5)

- **问题 / 瓶颈** · 全局覆盖会藏住组条件分数的分位异质性。
- **核心创新 / 方法** · 推导混合阈值的失真界，比较组别独立和汇总校准。
- **Baseline** · 汇总校准与分组策略。
- **Benchmark** · 模拟和真实数据，覆盖公平与集合大小公平。
- **关键结果 / 消融** · 两类公平目标存在实证和理论权衡。
- **适用条件 / 局限** · 结论针对指定方法族，样本少的组还受估计噪声制约。

**可复用机制** · 把公平误差在哪个指标上出现作为政策选择，而非只优化整体覆盖。

<a id="paper-149090"></a>

## On the Complexity of Offline Reinforcement Learning with Q*-Approximation and Partial Coverage

[官方论文页](https://neurips.cc/virtual/2026/poster/149090) · [作者来源](https://openreview.net/forum?id=syfyAxAGkx)

- **问题 / 瓶颈** · 即使最优 Q 可实现且 Bellman 完备，也不确保样本有效。
- **核心创新 / 方法** · 以信息论下界给反例，并用决策估计框架分解两种复杂度。
- **Baseline** · 仅假设最优值可实现及完备的理论情形。
- **Benchmark** · 部分覆盖的离线学习，考察样本复杂度。
- **关键结果 / 消融** · 证明两个常见假设单独结合仍不够，并统一部分既有结果。
- **适用条件 / 局限** · 关于更充分条件和算法常数应查完整理论。

**可复用机制** · 把训练集覆盖缺口和模型误差分开验证，避免用表示能力代替覆盖论证。

<a id="paper-156746"></a>

## On the Convergence Analysis of Muon

[官方论文页](https://neurips.cc/virtual/2026/poster/156746) · [作者来源](https://openreview.net/forum?id=4nH4CulGaP)

- **问题 / 瓶颈** · 矩阵参数展平会忽略结构，但经验优势缺解释。
- **核心创新 / 方法** · 分析 Muon 与梯度下降的收敛及低秩 Hessian 条件。
- **Baseline** · 标准梯度下降。
- **Benchmark** · 理论速率和验证实验；具名设置待核实。
- **关键结果 / 消融** · 作者指出低秩曲率可给 Muon 好处。
- **适用条件 / 局限** · 低秩形态和定量条件需查，实践不必然比所有自适应方法好。

**可复用机制** · 把曲率结构作为优化器消融轴，而不是只凭参数形状选型。

<a id="paper-152272"></a>

## On the Divergence of Differential Temporal Difference Learning without Local Clocks

[官方论文页](https://neurips.cc/virtual/2026/poster/152272) · [作者来源](https://openreview.net/forum?id=UJzniNLXaL)

- **问题 / 瓶颈** · 折扣问题中两者常可换，平均回报并非如此。
- **核心创新 / 方法** · 构造局部时钟收敛而全局时钟发散的反例。
- **Baseline** · 全局与每状态步长。
- **Benchmark** · 平均回报的理论反例。
- **关键结果 / 消融** · 证明两种时钟不等效。
- **适用条件 / 局限** · 反例不意味着所有全局时钟都会发散。

**可复用机制** · 在低频状态上单列更新次数和估值偏差，对比以访问频次分配训练。

<a id="paper-155543"></a>

## On the Effect of Token Correlations on Semantic Transfer in Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/155543) · [作者来源](https://openreview.net/forum?id=4kvpzWhoqH)

- **问题 / 瓶颈** · 早期模型可能把任务特有 token 和标签绑定。
- **核心创新 / 方法** · 受控配对表述测零样本迁移，再调整标签引入阶段。
- **Baseline** · 从开头引入标签与无专属 token。
- **Benchmark** · 命题逻辑的语义等价任务。
- **关键结果 / 消融** · 摘要报告延后引入显著改善迁移。
- **适用条件 / 局限** · 结果在受控逻辑任务成立，其他语料和时机需验证。

**可复用机制** · 用相同样本总量改变标签课程，检验是否影响语义与词面相关。

<a id="paper-154468"></a>

## On the Efficiency of Structured Pruning in Small Language Model Pretraining

[官方论文页](https://neurips.cc/virtual/2026/poster/154468) · [作者来源](https://openreview.net/forum?id=DMQt7OrYIm)

- **问题 / 瓶颈** · 仅计剪枝恢复低估大模型预训练代价。
- **核心创新 / 方法** · 让大模型训练、迭代结构剪枝与恢复共享一个余弦日程。
- **Baseline** · 从零训练及分阶段放大剪枝。
- **Benchmark** · 2.8B 到 1.3B、最多 2T token，控制数据和预算。
- **关键结果 / 消融** · 分阶段方法未稳定超过从头训，联合方法有适度净改善。
- **适用条件 / 局限** · 同 token 不必等于同 FLOPs，硬件与目标任务需查。

**可复用机制** · 同时记账大模型期计算及部署体积，不仅报恢复段成绩。

<a id="paper-154726"></a>

## On the Error Correcting Effects of Stochasticity in Discrete Diffusion

[官方论文页](https://neurips.cc/virtual/2026/poster/154726) · [作者来源](https://openreview.net/forum?id=BTRvd3ITHB)

- **问题 / 瓶颈** · 快速确定收敛可能在错误模式锁定。
- **核心创新 / 方法** · 分析可交换概率质量的冗余转移，以交替正反扩散恢复随机性。
- **Baseline** · 确定和更随机的既有离散采样。
- **Benchmark** · 大规模图像与语言，尤其少网络评估区间。
- **关键结果 / 消融** · 理论给出特定误差收缩，实验证明速度质量权衡改善。
- **适用条件 / 局限** · 随机性过强也延缓收敛，数值增益按任务验证。

**可复用机制** · 将纠错随机性和额外采样开销分开测。

<a id="paper-156766"></a>

## On the Expressive Power and Limitations of Multi-Layer SSMs

[官方论文页](https://neurips.cc/virtual/2026/poster/156766) · [作者来源](https://openreview.net/forum?id=NQ8IcsIti8)

- **问题 / 瓶颈** · 单看隐藏维度不足以解释串行组合能力。
- **核心创新 / 方法** · 用函数复合证明层深和状态精度的界，比较读入后推理与边读边推理。
- **Baseline** · 不同深度的 SSM 和一遍流式算法。
- **Benchmark** · 显式表多函数组合；状态维度、每标量精度及层数。
- **关键结果 / 消融** · 证明最坏情形深度层级，插入推理时机改变可模拟类别。
- **适用条件 / 局限** · 取决于正式的函数复合模型和有限精度假设。

**可复用机制** · 对长程任务以相同持久信息预算比较加层、加精度和交错计算。

<a id="paper-152360"></a>

## On the Faithfulness of Visual Thinking: Measurement and Enhancement

[官方论文页](https://neurips.cc/virtual/2026/poster/152360) · [作者来源](https://openreview.net/forum?id=TfDaCyVusi)

- **问题 / 瓶颈** · 正确答案可与错误视觉中间步骤并存。
- **核心创新 / 方法** · 分别干预图与文本推理，并训练生成最少且足够的证据。
- **Baseline** · 只奖输出格式的强化微调。
- **Benchmark** · 细粒度感知与推理。
- **关键结果 / 消融** · 图像干预不及文本影响明显，新目标改善忠实度。
- **适用条件 / 局限** · 依赖证据评估的有效性。

**可复用机制** · 同时报答案准确与图像替换后的变化。

<a id="paper-155587"></a>

## On the Fragility of Latent Knowledge: Layer-wise Influence under Unlearning in Large Language Model

[官方论文页](https://neurips.cc/virtual/2026/poster/155587) · [作者来源](https://openreview.net/forum?id=4UOY7tvEhc)

- **问题 / 瓶颈** · 遗忘可能波及其他能力。
- **核心创新 / 方法** · 逐组件替换定位脆弱位置，再比较局部恢复。
- **Baseline** · 原遗忘与原始模型。
- **Benchmark** · 多组遗忘及保留评测。
- **关键结果 / 消融** · 报告恢复改善折中。
- **适用条件 / 局限** · 恢复也可能带回目标内容。

**可复用机制** · 分别验收保留能力及删除质量，再决定是否恢复。

<a id="paper-154606"></a>

## On the fundamentals of gradient-based SAT solvers

[官方论文页](https://neurips.cc/virtual/2026/poster/154606) · [作者来源](https://openreview.net/forum?id=CMd4XXXt1U)

- **问题 / 瓶颈** · 梯度可能困于公式不变子空间。
- **核心创新 / 方法** · 理论统一边际和神经参数化目标，并用等价预处理改变几何。
- **Baseline** · 变量边际梯度与神经参数化。
- **Benchmark** · 多类 SAT 基准及无监督训练。
- **关键结果 / 消融** · 预处理改善多类任务，神经参数化可领先。
- **适用条件 / 局限** · 不同结构作用待核。

**可复用机制** · 对逻辑等价公式同时测对称性与求解速度。

<a id="paper-148858"></a>

## On the Geometry and Latent-Space Composition of Hypernetwork-Generated LoRAs

[官方论文页](https://neurips.cc/virtual/2026/poster/148858) · [作者来源](https://openreview.net/forum?id=udwqYC27uV)

- **问题 / 瓶颈** · 权重合并忽视结构化适配器几何。
- **核心创新 / 方法** · 合并中间隐量再解码固定秩。
- **Baseline** · 因子与权重融合。
- **Benchmark** · Doc-to-LoRA 与 SHINE 的多文档设置。
- **关键结果 / 消融** · 合并效果更好且保持固定秩。
- **适用条件 / 局限** · 直接微调适配器的几何未必相同。

**可复用机制** · 同容量比较两种合并表示，记录跨文档谱对齐。

<a id="paper-152581"></a>

## On the Impact of Side-Information in Bandit Learning: More is Not Always Merrier

[官方论文页](https://neurips.cc/virtual/2026/poster/152581) · [作者来源](https://openreview.net/forum?id=S19nBzjygT)

- **问题 / 瓶颈** · 采样时序可使普通 UCB 退化。
- **核心创新 / 方法** · 形式化非退化，给出反例和通用修正。
- **Baseline** · UCB、Thompson、探索后承诺。
- **Benchmark** · 理论及推荐群组实验。
- **关键结果 / 消融** · 同一信息可损害 UCB 而帮助其他算法。
- **适用条件 / 局限** · 取决于到达安排。

**可复用机制** · 按群体报告共享后的遗憾变化。

<a id="paper-151807"></a>

## On the Importance of Gating: Memorization vs. In-Context Learning in State Space Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151807) · [作者来源](https://openreview.net/forum?id=XsNfjnUeWl)

- **问题 / 瓶颈** · 门控会优先促成权重内记忆。
- **核心创新 / 方法** · 对比有无门的训练动力与理论。
- **Baseline** · 无门状态空间。
- **Benchmark** · 上下文学习与长度外推。
- **关键结果 / 消融** · 门会延缓上下文解，却常有利长序列。
- **适用条件 / 局限** · 依任务和门形式。

**可复用机制** · 同时保留两项验收并横向比较训练曲线。

<a id="paper-148174"></a>

## On the Information Loss of Multi-Token Prediction: Origin and Solution

[官方论文页](https://neurips.cc/virtual/2026/poster/148174) · [作者来源](https://openreview.net/forum?id=zjAVLNtSaV)

- **问题 / 瓶颈** · 块间信息丢失导致累计错误。
- **核心创新 / 方法** · 加入随机遮盖和双向块级目标。
- **Baseline** · 标准 MTP、逐词解码。
- **Benchmark** · 五骨干六任务含数学与 GLUE。
- **关键结果 / 消融** · 准确多 0.3–3.0 点，快 1.4–1.9 倍。
- **适用条件 / 局限** · 长程解码差错待核。

**可复用机制** · 按块深度比较同运行成本的质量变化。

<a id="paper-154965"></a>

## On the Instability and Stabilization of Blockwise Muon

[官方论文页](https://neurips.cc/virtual/2026/poster/154965) · [作者来源](https://openreview.net/forum?id=9a90UHToab)

- **问题 / 瓶颈** · 分别正交可放大组合更新。
- **核心创新 / 方法** · 旋转修正关键方向的跨块放大。
- **Baseline** · 全量和分块 Muon。
- **Benchmark** · 语言模型预训练。
- **关键结果 / 消融** · 报告接近完整收敛且保留分块效率。
- **适用条件 / 局限** · 通信开销待核。

**可复用机制** · 比较方向范数、大步长稳定和实际耗时。

<a id="paper-152053"></a>

## On the Invariance and Generality of Neural Scaling Laws

[官方论文页](https://neurips.cc/virtual/2026/poster/152053) · [作者来源](https://openreview.net/forum?id=VqUBACubep)

- **问题 / 瓶颈** · 新域拟合昂贵，直接重用可能失真。
- **核心创新 / 方法** · 分别分析可逆变换和降低信息分辨率的变换。
- **Baseline** · 域内重新拟合和直接迁移。
- **Benchmark** · 语言、视觉、语音及噪声时序。
- **关键结果 / 消融** · 数据指数误差可在 3% 内。
- **适用条件 / 局限** · 真实任务的信息分辨率难估。

**可复用机制** · 用已知可逆操作和已知损失作对照。

<a id="paper-148182"></a>

## On the Last-Iterate Convergence of Clipped Gradient Methods

[官方论文页](https://neurips.cc/virtual/2026/poster/148182) · [作者来源](https://openreview.net/forum?id=zgEpuLdwBv)

- **问题 / 瓶颈** · 普通最终点理论常依赖轻尾。
- **核心创新 / 方法** · 推导高概率最优最终迭代率。
- **Baseline** · 普通 SGD 及此前结果。
- **Benchmark** · 随机凸和强凸。
- **关键结果 / 消融** · 得到最优高概率最终点收敛。
- **适用条件 / 局限** · 不保证任意非凸模型。

**可复用机制** · 同时报告平均点及末点误差。

<a id="paper-154956"></a>

## On the Limits of Latent Reuse in Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154956) · [作者来源](https://openreview.net/forum?id=9eRD2Dppl5)

- **问题 / 瓶颈** · 冻结源潜空间可能破坏目标得分统计。
- **核心创新 / 方法** · 分别推导子空间主角和随扩散尺度放大的噪声项。
- **Baseline** · 冻结源潜表征及共享训练。
- **Benchmark** · 近低秩源与目标理论。
- **关键结果 / 消融** · 刻画误差及所需共享维数。
- **适用条件 / 局限** · 限近低秩假设。

**可复用机制** · 先测子空间投影残差，再决定重训。

<a id="paper-152743"></a>

## On the Memorization of Consistency Distillation for Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152743) · [作者来源](https://openreview.net/forum?id=QhEYPYxSzC)

- **问题 / 瓶颈** · 教师的训练样本复现不一定全部转给学生。
- **核心创新 / 方法** · 对照蒸馏前后，并用随机特征分析方向稳定性。
- **Baseline** · 带记忆的扩散教师。
- **Benchmark** · 生成质量及记忆复现。
- **关键结果 / 消融** · 记忆下降，生成质量保持或改善。
- **适用条件 / 局限** · 没有形式隐私保证。

**可复用机制** · 用自有合成标识同时测精确复现和一般质量。

<a id="paper-148724"></a>

## On the Nature of Attention Sink that Shapes Decoding Strategy in Omni-LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/148724) · [作者来源](https://openreview.net/forum?id=vX3qb5LCF9)

- **问题 / 瓶颈** · 高注意并不等于头冗余。
- **核心创新 / 方法** · 分析汇聚值共同偏置并改变早期层协调。
- **Baseline** · 原始全模态解码。
- **Benchmark** · 七项视频问答。
- **关键结果 / 消融** · 报告持续改善，约 1.1 倍解码开销。
- **适用条件 / 局限** · 跨结构及内部访问约束待核。

**可复用机制** · 对照直接删除汇聚词与保留其值的变化。

<a id="paper-151326"></a>

## On the Necessity of Guidance Decay:  From Three-Phase Analysis in Gaussian Mixture Models to Dynamic Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/151326) · [作者来源](https://openreview.net/forum?id=bLqrqUf9K9)

- **问题 / 瓶颈** · 固定尺度可能导致过曝。
- **核心创新 / 方法** · 由高斯混合分三阶段推导稳定边界，比较 VP 与 VE。
- **Baseline** · 固定引导与截断。
- **Benchmark** · 理论与生成质量。
- **关键结果 / 消融** · VP 稳定限制更严格，报告过曝下降。
- **适用条件 / 局限** · 混合模型未必适用全部自然图。

**可复用机制** · 同语义准确率下独立测过曝和视觉保真。

<a id="paper-155689"></a>

## On the Nonlinearity of Learning Rate Scaling for LLM Training

[官方论文页](https://neurips.cc/virtual/2026/poster/155689) · [作者来源](https://openreview.net/forum?id=3fy5G5iNJf)

- **问题 / 瓶颈** · 最优标称步长在大规模时偏离线性缩放。
- **核心创新 / 方法** · 比较数据和参数外推，分析权重范数瞬态并验证 AdamH。
- **Baseline** · 普通对数线性规律。
- **Benchmark** · 22–407M，5–100B 词元。
- **关键结果 / 消融** · 用有效学习率和数据外推可大体去除曲率。
- **适用条件 / 局限** · 超出规模仍待核。

**可复用机制** · 记录权重范数达到平衡的时长。

<a id="paper-155456"></a>

## On the Optimal Sample Complexity of Offline Multi-Armed Bandits with KL Regularization

[官方论文页](https://neurips.cc/virtual/2026/poster/155456) · [作者来源](https://openreview.net/forum?id=5SbBySWwEj)

- **问题 / 瓶颈** · 不同正则区间的精度依赖不同。
- **核心创新 / 方法** · 细化 KL-PCB 样本界并给匹配下界。
- **Baseline** · 既有 KL-PCB 分析。
- **Benchmark** · 上下文老虎机理论。
- **关键结果 / 消融** · 强正则相对弱正则可降低精度指数。
- **适用条件 / 局限** · 参数是逆正则强度，边界需细读。

**可复用机制** · 分别标注覆盖和正则量后再比较方法。

<a id="paper-153579"></a>

## On the Origin of Algorithmic Progress in AI: Evidence from Language Model Pre-Training

[官方论文页](https://neurips.cc/virtual/2026/poster/153579) · [作者来源](https://openreview.net/forum?id=KM1WIINeDC)

- **问题 / 瓶颈** · 小规模消融不能解释大规模硬件效率。
- **核心创新 / 方法** · 结合历史创新消融与跨规模 LSTM、Transformer 实验。
- **Baseline** · 此前汇总效率估计。
- **Benchmark** · 预训练等质量 FLOP 与缩放规律。
- **关键结果 / 消融** · 小规模消融不到十倍；估计大部分对数收益来自规模相关改进。
- **适用条件 / 局限** · 历史推断受外推影响。

**可复用机制** · 固定数据口径给多个预算而非一项倍数。

<a id="paper-148376"></a>

## On the Overscaling Curse of Parallel Thinking: System Efficacy Contradicts Sample Efficiency

[官方论文页](https://neurips.cc/virtual/2026/poster/148376) · [作者来源](https://openreview.net/forum?id=yLcpYgtJ0Z)

- **问题 / 瓶颈** · 统一预算浪费已能解好的样例。
- **核心创新 / 方法** · 从隐表示预测适合的候选数，再并行生成。
- **Baseline** · 固定全局预算。
- **Benchmark** · 并行推理精度、延迟与内存。
- **关键结果 / 消融** · 摘要称相近质量时利用率更高。
- **适用条件 / 局限** · 难题预算低估成本待查。

**可复用机制** · 分开报尾部延迟、题级预算和正确率。

<a id="paper-152281"></a>

## On the Parallel Optimality of Exponentiated Gradient Descent

[官方论文页](https://neurips.cc/virtual/2026/poster/152281) · [作者来源](https://openreview.net/forum?id=UFum06hNky)

- **问题 / 瓶颈** · 一阶查询总量和串行轮数不同。
- **核心创新 / 方法** · 对 L1 Lipschitz 目标给各轮并行多项式查询下界。
- **Baseline** · 指数梯度经典串行率。
- **Benchmark** · 概率单纯形和 L1 球的理论。
- **关键结果 / 消融** · 所涉精度下轮数约仍需 ε^-2，省略对数。
- **适用条件 / 局限** · 结论限该预言模型和精度范围。

**可复用机制** · 先检查并发能否减少依赖链，再决定扩机器或利用目标额外结构。

<a id="paper-153313"></a>

## On the Pitfalls of Instance-Based Dynamic Curricula

[官方论文页](https://neurips.cc/virtual/2026/poster/153313) · [作者来源](https://openreview.net/forum?id=MF2F6p7JOi)

- **问题 / 瓶颈** · 子采样可改变日程，伪装成选样收益。
- **核心创新 / 方法** · 在重配日程对照下分离挑选具体样本和训练步变化。
- **Baseline** · 静态、动态及采样对照。
- **Benchmark** · CIFAR-10、CIFAR-100、ImageNet。
- **关键结果 / 消融** · 部分领先课程的收益可由有效学习率解释。
- **适用条件 / 局限** · 证据针对所测图像分类与方法。

**可复用机制** · 先匹配优化过程才验证课程排序是否提供额外信息。

<a id="paper-148955"></a>

## On the Price of Privacy for Language Identification and Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/148955) · [作者来源](https://openreview.net/forum?id=tuVOBgviZm)

- **问题 / 瓶颈** · 单一隐私预算概念掩盖机制类别差异。
- **核心创新 / 方法** · 推导不可实现统计设置中的识别与生成上下界。
- **Baseline** · 非私有、近似 DP 和纯 DP。
- **Benchmark** · 理论错误指数。
- **关键结果 / 消融** · 常数 ε 近似 DP 可恢复所测非私有率；纯 DP 按 min(1, ε) 放缓。
- **适用条件 / 局限** · 理论语言族不直接代表现实大模型训练。

**可复用机制** · 把隐私定义与模型假设作为可行性输入，而不是从单个 ε 推断代价。

<a id="paper-150372"></a>

## On the Primacy Bias in RLVR Training

[官方论文页](https://neurips.cc/virtual/2026/poster/150372) · [作者来源](https://openreview.net/forum?id=iYqWuTaHph)

- **问题 / 瓶颈** · 整体分数可能主要反映熟题精度。
- **核心创新 / 方法** · 区分易难题并比较混训和难题强化时的表示和性能。
- **Baseline** · 混合采样与初始基座。
- **Benchmark** · 多个可验证推理域及受控数据。
- **关键结果 / 消融** · 混训更多改善易题；难题推动能力但久训可伤易题。
- **适用条件 / 局限** · 影响随初始熟悉性及数据变化。

**可复用机制** · 同时保存旧能力留出与新能力留出，以避免平均分掩盖真实变化。

<a id="paper-153853"></a>

## On the Provable Emergence of Hierarchical Concept Structure in CLIP Embeddings

[官方论文页](https://neurips.cc/virtual/2026/poster/153853) · [作者来源](https://openreview.net/forum?id=IFmLNK0lpW)

- **问题 / 瓶颈** · 对比目标本身未标记概念树。
- **核心创新 / 方法** · 度量父类与子孙相对其他分支的角分离，并分析固定图像表示的对比学习。
- **Baseline** · 随机初始化、训练前后和不同对比损失。
- **Benchmark** · CLIP 几何、多层合成任务。
- **关键结果 / 消融** · 图像侧有弱先验，文本层级在训练后出现。
- **适用条件 / 局限** · 证明依赖图像分离裕度及简化设定。

**可复用机制** · 若希望文本继承特定概念结构，先核验配对图像已具该结构。

<a id="paper-154768"></a>

## On the Rademacher Complexity of Graph Neural Networks: Unifying Expressivity and Geometry

[官方论文页](https://neurips.cc/virtual/2026/poster/154768) · [作者来源](https://openreview.net/forum?id=B5sX9YQyxl)

- **问题 / 瓶颈** · WL 等可分能力不能单独给真实泛化代价。
- **核心创新 / 方法** · 以等价类分布及 Lipschitz 覆盖刻画经验 Rademacher 复杂度。
- **Baseline** · 仅用 VC 或图不变量计数。
- **Benchmark** · 不同图不变量及经验测度的理论。
- **关键结果 / 消融** · 复杂度受等价类频率与几何平滑控制，且随 Wasserstein 扰动稳定。
- **适用条件 / 局限** · 依赖输入度量及假设类正则。

**可复用机制** · 选更有表达力的骨干时先测增加的区分类是否在数据中实质出现。

<a id="paper-155580"></a>

## On the Recall Scaling Laws in Mamba: A Theoretical and Mechanistic Study via Hashing

[官方论文页](https://neurips.cc/virtual/2026/poster/155580) · [作者来源](https://openreview.net/forum?id=4ZDfHcccsn)

- **问题 / 瓶颈** · 总体语言损失无法定位容量界。
- **核心创新 / 方法** · 解释 Mamba 的低层关联为可学习线性哈希，推导容量尺度。
- **Baseline** · 实测回忆容量与理论下界。
- **Benchmark** · 不同词表、状态和嵌入的关联回忆。
- **关键结果 / 消融** · 摘要报告下界对所测容量预测较紧。
- **适用条件 / 局限** · 限该回忆任务与状态模型。

**可复用机制** · 同时扫状态维数和词表，不只改变上下文长度。

<a id="paper-149548"></a>

## On the Recoverability of Causal Relations from Bulk Gene Expression Data

[官方论文页](https://neurips.cc/virtual/2026/poster/149548) · [作者来源](https://openreview.net/forum?id=pKBv1h4LAZ)

- **问题 / 瓶颈** · 平均测量无法恢复单细胞结构。
- **核心创新 / 方法** · 区分函数形式与条件独立一致性，分析线性聚合和结构条件。
- **Baseline** · 将聚合等同原数据的因果推断。
- **Benchmark** · 四套整体及四套单细胞数据。
- **关键结果 / 消融** · 线性聚合与仿射方程下可保存，实测支持有限。
- **适用条件 / 局限** · 一般情况下不可由聚合数据识别。

**可复用机制** · 聚合前先列出必须保留的统计关系，缺相容条件时避免解释观察图为因果。

<a id="paper-154387"></a>

## On the Relaxation of Conditional Independence Assumption for Image Segmentation

[官方论文页](https://neurips.cc/virtual/2026/poster/154387) · [作者来源](https://openreview.net/forum?id=DwqwJHYbqV)

- **问题 / 瓶颈** · 全独立假设漏边缘信号，全依赖计算又贵。
- **核心创新 / 方法** · 用空间局部依赖、倒数矩近似与固定点替代穷举。
- **Baseline** · argmax 和独立 RankSEG。
- **Benchmark** · 多分割数据，Dice 或 IoU。
- **关键结果 / 消融** · 摘要报告 O(d log d)，小目标和低对比改善明显。
- **适用条件 / 局限** · 依赖局部依赖可表达主要结构。

**可复用机制** · 用有限邻域依赖增加可信度，避免为弱长程边支付全局成本。

<a id="paper-154750"></a>

## On the Runway Cascade of Transformers for Language Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/154750) · [作者来源](https://openreview.net/forum?id=BG7L2BEqkO)

- **问题 / 瓶颈** · 单一直接边无法反映早先信息如何重复进入残差。
- **核心创新 / 方法** · 从间接路径的汇总重连部分直接注意边。
- **Baseline** · 标准 Transformer。
- **Benchmark** · 语言建模、检索与长度外推。
- **关键结果 / 消融** · 摘要报告三者有改善且不加参数。
- **适用条件 / 局限** · 路径摘要成本与长上下文扩展待核实。

**可复用机制** · 诊断信息拥堵时同时查看直接和累积的间接流。

<a id="paper-151061"></a>

## On the Sparsity of Direct Preference Optimization: Weight Disentanglement in the NTK Regime

[官方论文页](https://neurips.cc/virtual/2026/poster/151061) · [作者来源](https://openreview.net/forum?id=dIhTYcLqCB)

- **问题 / 瓶颈** · 只看参数数不说明偏好任务相互干扰。
- **核心创新 / 方法** · 在 NTK 线性化中连接支持向量和正负梯度抵消。
- **Baseline** · 监督微调。
- **Benchmark** · GPT-2、HH-RLHF、UltraFeedback。
- **关键结果 / 消融** · 摘要报告两级稀疏且交叉任务干扰最多降 35 倍。
- **适用条件 / 局限** · 依赖局部线性及模型规模。

**可复用机制** · 分别排查是少数对比样本决定更新，还是参数空间出现可分离方向。

<a id="paper-154548"></a>

## On the Sparsity-Storage-Accuracy Tradeoff in Parsimoniously Activated Dictionary Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/154548) · [作者来源](https://openreview.net/forum?id=Ck8F9vHTAH)

- **问题 / 瓶颈** · 全局激活惩罚缺可解释的尺度选择。
- **核心创新 / 方法** · 以共享激活潜变量的最大后验重写算法并分析折中。
- **Baseline** · 手调全局惩罚及元素级 L1。
- **Benchmark** · 视觉重建及视觉语言推理。
- **关键结果 / 消融** · 摘要报告同稀疏水平重建改善。
- **适用条件 / 局限** · 需验证所假定生成模型与硬件收益。

**可复用机制** · 设定存储和误差预算后估激活惩罚，避免只扫重建分数。

<a id="paper-154185"></a>

## On the Tightness and Computational Tractability of Higher-Dimensional Confidence Sequences

[官方论文页](https://neurips.cc/virtual/2026/poster/154185) · [作者来源](https://openreview.net/forum?id=FZkTNX1Pl4)

- **问题 / 瓶颈** · 逐指标区间保守，联合紧区域难求。
- **核心创新 / 方法** · 用盒、Lp 椭球或交集近似赌注组合，同时保留覆盖。
- **Baseline** · Bonferroni 与组合区域。
- **Benchmark** · 多指标 A/B 和模型比较。
- **关键结果 / 消融** · 摘要报告接近不可解的紧区域并优于常用快速方案。
- **适用条件 / 局限** · 依赖有界向量均值及所设监控条件。

**可复用机制** · 用外包络优化计算量，不能用无保证数值近似替换有效区域。

<a id="paper-150461"></a>

## On the Token Value Inequality in Efficient Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/150461) · [作者来源](https://openreview.net/forum?id=hrWCDkWrpQ)

- **问题 / 瓶颈** · 整段长度惩罚不区分关键推理与探索冗余。
- **核心创新 / 方法** · 以归一化词元概率构造价值代理，结合选择性 GRPO 压缩。
- **Baseline** · 常规推理与匹配长度的强模型。
- **Benchmark** · 准确率及词元预算。
- **关键结果 / 消融** · 摘要报告质量保留时词元消耗减少 76%。
- **适用条件 / 局限** · 低置信不必然无用，需对稀有关键步骤做干预。

**可复用机制** · 剪缩之前验证词元是否承担不可替代的结构角色。

<a id="paper-154939"></a>

## On Time, Within Budget: Constraint-Driven Online Resource Allocation for Agentic Workflows

[官方论文页](https://neurips.cc/virtual/2026/poster/154939) · [作者来源](https://openreview.net/forum?id=9n93yn1m1m)

- **问题 / 瓶颈** · 平均时延与成本不能衡量硬截止成功。
- **核心创新 / 方法** · 对依赖图模拟未来执行，按剩余资源完成度分配模型和并发。
- **Baseline** · 强资源编排基线。
- **Benchmark** · CodeFlow、ProofFlow，不同工期和预算。
- **关键结果 / 消融** · 摘要报告约束下成功概率普遍改善。
- **适用条件 / 局限** · 依赖运行时长度及成功率估计。

**可复用机制** · 执行中随已观察结果重算剩余计划，而非只制定固定预算表。

<a id="paper-155199"></a>

## OntoPlan: An Ontology-Grounded Scene Representation and Agentic Framework for Scalable Robot Task Planning

[官方论文页](https://neurips.cc/virtual/2026/poster/155199) · [作者来源](https://openreview.net/forum?id=7YcnWpfSWA)

- **问题 / 瓶颈** · 线性文本使空间关系丢失且随场景增长。
- **核心创新 / 方法** · 以对象、空间、状态和关系形式化目标，取相关子图再生成可执行计划。
- **Baseline** · 文本场景及直接动作生成的规划器。
- **Benchmark** · 五室内环境、三规模、150 任务。
- **关键结果 / 消融** · 成功率 0.83 对 0.30，词元较最佳效率基线少约 5.8 倍。
- **适用条件 / 局限** · 依赖本体质量与状态更新，真实身体执行需复验。

**可复用机制** · 让语言模型解释目标，形式状态验证动作前置；信息不够时保留澄清路径。

<a id="paper-152352"></a>

## On Worst-Case Guarantees for Graph-Based Nearest-Neighbor Search

[官方论文页](https://neurips.cc/virtual/2026/poster/152352) · [作者来源](https://openreview.net/forum?id=ThkUq9PUA7)

- **问题 / 瓶颈** · 标准图式贪心在坏例中可线性查询。
- **核心创新 / 方法** · 分析纯数据点图下界，引入额外 Steiner 节点给次线性界。
- **Baseline** · HNSW、DiskANN 等及 LSH 理论。
- **Benchmark** · 欧氏近似近邻与初步召回时延。
- **关键结果 / 消融** · 理论上允许辅助节点可达与 LSH 可比的界，实证改进温和。
- **适用条件 / 局限** · 附加节点的构建与存储需要计入。

**可复用机制** · 将索引可引入的导航空间与原始数据点集合分开考虑。

<a id="paper-152375"></a>

## OopsWorld! Operation-Grounded Seamless World Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/152375) · [作者来源](https://openreview.net/forum?id=TYAayuMqM6)

- **问题 / 瓶颈** · 下一幕描述不能保证旧对象锚点持续。
- **核心创新 / 方法** · 以类型化操作定义边界，用全景状态条件教师监督只见操作和历史的学生。
- **Baseline** · 现有长视频和场景条件生成。
- **Benchmark** · SeamlessWorld 八类操作，VBench 动态与长质量。
- **关键结果 / 消融** · 摘要报告两项分数 91.67 与 80.42，仍有锚点保留差距。
- **适用条件 / 局限** · 合成任务与现实互动迁移待核查。

**可复用机制** · 训练和验收同时测操作引发的改变及不应改变的旧证据。

<a id="paper-139232"></a>

## OpenBrain: An Auditable Generated-Label Release for Whole-Brain MRI Parcellation

[官方论文页](https://neurips.cc/virtual/2026/poster/139232) · [作者来源](https://openreview.net/forum?id=dR9OMtUEEC)

- **问题 / 瓶颈** · 只发布标签难以核实其是否可靠。
- **核心创新 / 方法** · 保留主模型与委员会预测、来源、几何/影像一致和相对风险供独立分层。
- **Baseline** · 随机固定预算选择。
- **Benchmark** · 35,838 例 OpenNeuro T1w、外部队列及固定训练预算；宏平均 Dice。
- **关键结果 / 消融** · 低风险选择较随机高 3.2–3.7 点。
- **适用条件 / 局限** · 不同来源阈值及低风险群体代表性待查。

**可复用机制** · 给伪标签保留可审计证据，避免只提供单一未经外部校验的置信分。

<a id="paper-148587"></a>

## Opening the Black Box of Classifier-Free Guidance via Information Bottleneck

[官方论文页](https://neurips.cc/virtual/2026/poster/148587) · [作者来源](https://openreview.net/forum?id=wfY4Srt4qX)

- **问题 / 瓶颈** · 相同引导在不同去噪阶段不一定同样有效。
- **核心创新 / 方法** · 将轨迹视为时间变化信息瓶颈，依据 Fisher 信息平衡推断关键阶段。
- **Baseline** · 固定或人工动态 CFG。
- **Benchmark** · 条件扩散，考察采样质量和引导时点。
- **关键结果 / 消融** · 理论指出临界阶段后条件信号更强。
- **适用条件 / 局限** · 具体阈值估计及不同模型的经验收益待核实。

**可复用机制** · 做逐段引导消融，用相同网络评估次数比较高价值阶段和全程引导。

<a id="paper-152128"></a>

## OpenSearcher: Democratizing Deep Search through a Fully Offline Pipeline with Programmatic Verification

[官方论文页](https://neurips.cc/virtual/2026/poster/152128) · [作者来源](https://openreview.net/forum?id=VKegdQ1pF8)

- **问题 / 瓶颈** · 自由写题难证明答案唯一，在线检索合成不易复现。
- **核心创新 / 方法** · 从 Wikidata 计算最小区分集，展开为推理 DAG，再用 SPARQL 合取查询核验答案。
- **Baseline** · 依赖在线 API 或缺少程序核验的数据管线。
- **Benchmark** · 离线深搜索训练与答案唯一性；具体基准待核实。
- **关键结果 / 消融** · 摘要给出无需在线合成的确定性唯一检查。
- **适用条件 / 局限** · 唯一性只在知识库快照和查询约束中成立。

**可复用机制** · 先确定唯一答案和必需证据，再做自然语言改写并重新验证。

<a id="paper-155432"></a>

## Open-Vocabulary 3D Part Segmentation with  Semantic Propagation Hawkes Process

[官方论文页](https://neurips.cc/virtual/2026/poster/155432) · [作者来源](https://openreview.net/forum?id=5hcg8T2gV0)

- **问题 / 瓶颈** · 只做点文本匹配无法显式修正弱证据。
- **核心创新 / 方法** · 把点表示约束到文本条件低秩空间，用有限步 Hawkes 传播高置信种子并反馈到后续整形。
- **Baseline** · 普通点文本匹配。
- **Benchmark** · 多个开放词表三维部件基准。
- **关键结果 / 消融** · 摘要给出单前向内完成整形和传播的设计。
- **适用条件 / 局限** · 种子错判可能扩散，跨物体和粒度应查。

**可复用机制** · 对难部件同时测形状限制和传播单项效果，检查错误是否被放大。

<a id="paper-150532"></a>

## Open Vocabulary Domain Unlearning

[官方论文页](https://neurips.cc/virtual/2026/poster/150532) · [作者来源](https://openreview.net/forum?id=hR9v42DbaF)

- **问题 / 瓶颈** · 只测编辑所用类会把记住类域配对误判为整域遗忘。
- **核心创新 / 方法** · 用 held-out 类构建开放词表遗忘测试，并给域敏感权重编辑作参照。
- **Baseline** · 封闭类遗忘评估。
- **Benchmark** · 视觉语言域遗忘，评估已见和未见类别及保留域。
- **关键结果 / 消融** · 摘要指出传统测试会漏掉未见类中的残余域识别。
- **适用条件 / 局限** · 分类器识别下降不等于知识完全删除，领域定义需查。

**可复用机制** · 将遗忘的样本划分按正交语义维度持出，核查遗忘是否泛化。

<a id="paper-139156"></a>

## OpenVTON-Bench: A Large-Scale High-Resolution Benchmark for Controllable Virtual Try-On Evaluation

[官方论文页](https://neurips.cc/virtual/2026/poster/139156) · [作者来源](https://openreview.net/forum?id=hkbyKxmccF)

- **问题 / 瓶颈** · 整体视觉分数不能指出接缝错误来自形状还是纹理。
- **核心创新 / 方法** · 基于分割及形态侵蚀构造多尺度区域，并结合语义评判。
- **Baseline** · 传统整体质量度量。
- **Benchmark** · 约十万高分辨率换装图对，考察背景、身份、纹理、形态和真实度。
- **关键结果 / 消融** · 摘要描述局部度量可以单列边界和内部错误。
- **适用条件 / 局限** · 电商换装之外的评测有效性及与人评一致性待查。

**可复用机制** · 保留区域级误差归因，并检验分割失败是否影响纹理得分。

<a id="paper-149311"></a>

## OPERA: An Agent for Image Restoration with End-to-End Joint Planning–Execution Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/149311) · [作者来源](https://openreview.net/forum?id=r7MoK2h7x4)

- **问题 / 瓶颈** · 独立训成的工具在多重退化下可能不适合串联。
- **核心创新 / 方法** · 用最终复原质量学习工具组合，并按选出的序列联合优化各工具。
- **Baseline** · 全能复原与现有代理组装模型。
- **Benchmark** · 多退化及现实复原数据，复原质量。
- **关键结果 / 消融** · 摘要报告多个场景的整体表现优于对照。
- **适用条件 / 局限** · 联合优化和更大搜索空间各自效应及资源待查。

**可复用机制** · 将工具级质量与跨工具相容性分别验收，按退化组合分层。

<a id="paper-150153"></a>

## Operads for compositional reasoning in LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/150153) · [作者来源](https://openreview.net/forum?id=kGXWfWoQFU)

- **问题 / 瓶颈** · 仅在同一问题采多个答案无法测试组合一致性。
- **核心创新 / 方法** · 用显式分解结果与直接答案的一致性作为逐题信号。
- **Baseline** · 自一致、语义熵和自评概率。
- **Benchmark** · 四个多跳问答基准、十二个 4B–671B 模型。
- **关键结果 / 消融** · 跨模型 Pearson 相关 0.86–0.94，推理成本约为最强采样基线的三分之一。
- **适用条件 / 局限** · 跨模型相关不同于逐题可靠性，分解错误可能误报。

**可复用机制** · 同时观察分解有效性和答案一致性，防止两条错误途径一致而获得高置信。

<a id="paper-154322"></a>

## OperatorSHAP: Fast and Accurate Shapley Value Estimation for Neural Operators

[官方论文页](https://neurips.cc/virtual/2026/poster/154322) · [作者来源](https://openreview.net/forum?id=EXq2TaPGfM)

- **问题 / 瓶颈** · 普通摊销 SHAP 预设同形输入，难覆非规则网格。
- **核心创新 / 方法** · 连接函数空间归因与 Aumann–Shapley，训练网格无关的摊销解释器。
- **Baseline** · FastSHAP 和离散 Shapley 对照。
- **Benchmark** · 多分辨率及不同网格大小的神经算子。
- **关键结果 / 消融** · 摘要报告与离散估计一致并无需重训迁移。
- **适用条件 / 局限** · 连续路径与背景分布选择的敏感性待查。

**可复用机制** · 检查解释的跨分辨率一致性，而非只验证某一种点划分的归因图。

<a id="paper-151932"></a>

## OPPO: Bayesian Value Recursion for Token-Level Credit Assignment in Policy Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/151932) · [作者来源](https://openreview.net/forum?id=WkadvgDPwb)

- **问题 / 瓶颈** · 统一优势忽略决定性步骤，单独评分不结合历史。
- **核心创新 / 方法** · 用答案条件似然比递推后验成功率，推导局部优势。
- **Baseline** · GRPO、DAPO、SDPO。
- **Benchmark** · 两模型七个数学科学和代码基准。
- **关键结果 / 消融** · 摘要报告持续提升，竞赛长题收获最大。
- **适用条件 / 局限** · 依赖答案及模型校准。

**可复用机制** · 同额外前向预算比较累积和独立词元信用。

<a id="paper-153312"></a>

## Opponent Modeling in Incomplete-Information Continuous Colonel Blotto

[官方论文页](https://neurips.cc/virtual/2026/poster/153312) · [作者来源](https://openreview.net/forum?id=MFTBJfrkL4)

- **问题 / 瓶颈** · 边缘信息可能丢相关性，不能由更多样本弥补。
- **核心创新 / 方法** · 把最坏收益不确定性写成到可观察函数跨度的距离。
- **Baseline** · 完整后验、不同阶边缘。
- **Benchmark** · 连续 Blotto 及预算分配理论。
- **关键结果 / 消融** · 一阶边缘仅对可加类精确，三及更多维可需更高阶。
- **适用条件 / 局限** · 依赖给定函数类。

**可复用机制** · 在无害分配游戏改相关性、保留边缘检查策略变化。

<a id="paper-149166"></a>

## OPSRL-SSP: Optimistic Posterior Sampling for Stochastic Shortest Path with Minimax-Optimal Regret

[官方论文页](https://neurips.cc/virtual/2026/poster/149166) · [作者来源](https://openreview.net/forum?id=sMu4oJ1wW2)

- **问题 / 瓶颈** · 普通后验采样缺统一保证。
- **核心创新 / 方法** · 以随时间的采样日程及乐观伪状态扩充模型。
- **Baseline** · 标准后验采样及最优遗憾下界。
- **Benchmark** · 未知转移 SSP，含零成本条件。
- **关键结果 / 消融** · 主项匹配极小极大遗憾。
- **适用条件 / 局限** · 假设和低阶项需全文确认。

**可复用机制** · 按长尾终止时长分别记录探索和规划表现。

<a id="paper-153953"></a>

## Opt-Arena: Evaluating, Selecting, and Generating Optimization Modeling Data via Tripartite Graphs

[官方论文页](https://neurips.cc/virtual/2026/poster/153953) · [作者来源](https://openreview.net/forum?id=HKMOHcifiP)

- **问题 / 瓶颈** · 向量去重未必去掉同约束结构。
- **核心创新 / 方法** · 以原子规则构建三部图，用覆盖与重叠选核集及补欠样本。
- **Baseline** · 距离和不确定性筛样。
- **Benchmark** · 运筹建模；比较 5K 与 20K 预算。
- **关键结果 / 消融** · 5K 精选超过一般方法 20K 平台。
- **适用条件 / 局限** · 需核验规则抽取准确。

**可复用机制** · 按未见约束组合测试，匹配训练词元避免规模混淆。

<a id="paper-152209"></a>

## OpticalRAG: Pixel-Space Compression for Token-Efficient Retrieval-Augmented Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/152209) · [作者来源](https://openreview.net/forum?id=UloVevL5nW)

- **问题 / 瓶颈** · 纯文本截断会抛弃布局与细节。
- **核心创新 / 方法** · 页面渲染，借冻结图文空间检索并用交叉注意压为查询前缀。
- **Baseline** · 闭卷语言模型和常见文本压缩 RAG。
- **Benchmark** · LongBench-v2、BAMBOO、LooGLE-v2，16 注入词元。
- **关键结果 / 消融** · LongBench-v2 对闭卷高 5.17 点；压缩感知指标领先三集。
- **适用条件 / 局限** · 渲染、OCR 难度和实际计算成本需核。

**可复用机制** · 同输入成本比较细节查找与通用语义问题。

<a id="paper-151049"></a>

## Optimal algorithmic complexity of inference in quantum kernel methods

[官方论文页](https://neurips.cc/virtual/2026/poster/151049) · [作者来源](https://openreview.net/forum?id=dMzQUanLcb)

- **问题 / 瓶颈** · 逐项估计核成本大，查询最优未必门最优。
- **核心创新 / 方法** · 将加权核和归入单可观测量并用振幅估计，另比较重要采样。
- **Baseline** · 逐项采样。
- **Benchmark** · 理论查询和门级分析。
- **关键结果 / 消融** · 查询阶为 L1 系数范数除精度，有匹配下界。
- **适用条件 / 局限** · 依赖硬件和准备成本。

**可复用机制** · 在同误差下分别报告总门数与查询数。

<a id="paper-150041"></a>

## Optimal Algorithms for Fixed-Graph  Multi-Attribution Privacy

[官方论文页](https://neurips.cc/virtual/2026/poster/150041) · [作者来源](https://openreview.net/forum?id=lDbcs5uokk)

- **问题 / 瓶颈** · 单样本单人的隐私假设低估共享归属敏感度。
- **核心创新 / 方法** · 近似贡献界并用图密度给上下界，结合 DP-SGD。
- **Baseline** · 常规单归属与 LP、贪心裁剪。
- **Benchmark** · 固定公开归属图理论，含一般和独立抽样。
- **关键结果 / 消融** · 学习误差受图集中度控制，刻画筛样偏差。
- **适用条件 / 局限** · 归属结构公开、内容私有。

**可复用机制** · 同隐私预算分别验高密度组效用与裁剪偏差。

<a id="paper-155961"></a>

## Optimal and Efficient Contextual Combinatorial Semi-bandits with General Function Approximation

[官方论文页](https://neurips.cc/virtual/2026/poster/155961) · [作者来源](https://openreview.net/forum?id=1XBZJBTBc2)

- **问题 / 瓶颈** · 仅有限基数的动作集合未必支持特定策略搜索。
- **核心创新 / 方法** · 以凸优化分布抽样组合，使用一般回报函数近似。
- **Baseline** · 策略搜索和限制更强的推荐组合。
- **Benchmark** · 理论分析含一般组合动作。
- **关键结果 / 消融** · 在可实现条件下达近最优平方根遗憾。
- **适用条件 / 局限** · 已知函数类和逐臂反馈。

**可复用机制** · 独立报告求解开销与实际遗憾。

<a id="paper-151579"></a>

## Optimal Ansatz-free Hamiltonian Learning In Situ

[官方论文页](https://neurips.cc/virtual/2026/poster/151579) · [作者来源](https://openreview.net/forum?id=ZYCtg2pJYn)

- **问题 / 瓶颈** · 高精度最优协议可能需深电路与过高时分辨率。
- **核心创新 / 方法** · 在无额外控制设定用随机时间探测与乘积态测量学习。
- **Baseline** · 依赖深控制的方案和无控制下界。
- **Benchmark** · 有范数界的哈密顿量理论。
- **关键结果 / 消融** · 总演化时间匹配该设定下界，时间分辨率不随目标精度变化。
- **适用条件 / 局限** · 理论不等同复杂系统硬件实测。

**可复用机制** · 按演化时间和最短采样间隔验收低风险量子校准实验。

<a id="paper-152344"></a>

## Optimal Byzantine-resilient Federated Learning with User-level Differential Privacy

[官方论文页](https://neurips.cc/virtual/2026/poster/152344) · [作者来源](https://openreview.net/forum?id=TlQd1co4f2)

- **问题 / 瓶颈** · 直接加噪可能不能保证收敛。
- **核心创新 / 方法** · 比较双层动量带来的客户端方差缓解和服务端稳定性。
- **Baseline** · 非线性鲁棒聚合与 DP 的直接拼接。
- **Benchmark** · 强凸、非凸理论及公开数据数值实验。
- **关键结果 / 消融** · 强凸达阶最优，衰减项分别为 1/T 和 1/√T。
- **适用条件 / 局限** · 依故障比例和隐私假设。

**可复用机制** · 在自有模拟分别扫隐私、异常比例与客户端异质度。

<a id="paper-150624"></a>

## Optimal Contextual Pricing under Agnostic Non-Lipschitz Demand

[官方论文页](https://neurips.cc/virtual/2026/poster/150624) · [作者来源](https://openreview.net/forum?id=giaq1R0M4q)

- **问题 / 瓶颈** · 原平滑理论依赖不存在的 Lipschitz 性。
- **核心创新 / 方法** · 估参数后保守网格探测，并按置信度改决策。
- **Baseline** · 此前 T^(3/4) 方法。
- **Benchmark** · 线性估值、非平滑需求的在线理论。
- **关键结果 / 消融** · 得到近 T^(2/3) 最优遗憾。
- **适用条件 / 局限** · 要有条件良好的随机情境。

**可复用机制** · 先分层测试具突变和连续需求的模型误差。

<a id="paper-155799"></a>

## Optimal Convergence Analysis of DDPM for General Distributions

[官方论文页](https://neurips.cc/virtual/2026/poster/155799) · [作者来源](https://openreview.net/forum?id=2nT2NsEr3J)

- **问题 / 瓶颈** · 一般维数界会高估一定分布族的迭代量。
- **核心创新 / 方法** · 放松平滑并分析 TV 和 KL，构造匹配下界。
- **Baseline** · 既有 d 除精度界与 DDIM。
- **Benchmark** · 准确得分下的理论。
- **关键结果 / 消融** · 界含 √d min(√d,L) 项。
- **适用条件 / 局限** · 实际得分误差和常数未计。

**可复用机制** · 在同得分估计质量下扫步数，分开测统计误差与速度。

<a id="paper-154002"></a>

## Optimal Dimension-Free Sampling for Regularized Classification

[官方论文页](https://neurips.cc/virtual/2026/poster/154002) · [作者来源](https://openreview.net/forum?id=Gv4HMpqs8v)

- **问题 / 瓶颈** · 传统维数依赖或灵敏度界偏松。
- **核心创新 / 方法** · 以均匀或按范数抽样推导界及匹配下界。
- **Baseline** · 早期三次级灵敏度界。
- **Benchmark** · Logistic、hinge、ReLU 及多个正则。
- **关键结果 / 消融** · L1 与 L2 正则出现不同阶；部分零起始损失无维数无关界。
- **适用条件 / 局限** · 不同 k 定义及正则需全文确认。

**可复用机制** · 给每种目标独立控制相对误差，避免通用样本量。

<a id="paper-154125"></a>

## Optimal Experiments for Partial Causal Effect Identification

[官方论文页](https://neurips.cc/virtual/2026/poster/154125) · [作者来源](https://openreview.net/forum?id=G61y8qp0of)

- **问题 / 瓶颈** · 成本高时遍历候选昂贵，部分实验不会缩界。
- **核心创新 / 方法** · 用因果图区分零潜力路径并先做可辨识性筛选。
- **Baseline** · 多项式规划和未筛子集搜索。
- **Benchmark** · 随机图及 11 个 bnlearn 网络。
- **关键结果 / 消融** · 无需解规划即裁掉平均 50%–88% 候选。
- **适用条件 / 局限** · 依赖因果图正确，场景效果不构成临床证据。

**可复用机制** · 在良性模拟固定预算比较区间最坏缩减和图错误敏感度。

<a id="paper-148709"></a>

## Optimal Hidden-Target Learning for Online Inventory Optimization on General Convex Sets

[官方论文页](https://neurips.cc/virtual/2026/poster/148709) · [作者来源](https://openreview.net/forum?id=veDCFlujwu)

- **问题 / 瓶颈** · 已购库存不能立即撤回，普通在线凸优化忽略记忆。
- **核心创新 / 方法** · 对隐藏目标做梯度学习，将落差化成一维队列分析。
- **Baseline** · 一般凸容量下此前算法。
- **Benchmark** · 任意有界凸容量集合理论。
- **关键结果 / 消融** · 改进共同需求概率依赖并匹配下界，含动态和强凸界。
- **适用条件 / 局限** · 共同需求假设及延迟受任务限制。

**可复用机制** · 同时监控目标变化速率和投影积压。

<a id="paper-155446"></a>

## Optimal In-context Adaptivity and Distributional Robustness of Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/155446) · [作者来源](https://openreview.net/forum?id=5YXJKkV5dy)

- **问题 / 瓶颈** · 单难度训练可能不会随新任务复杂度改变估计。
- **核心创新 / 方法** · 对随机平滑度及有效维数的先验混合证明适应性。
- **Baseline** · 已知测试分布估计器的最优率。
- **Benchmark** · 非参数回归及多指标模型理论。
- **关键结果 / 消融** · 在卡方散度邻域中一致达难度相关最优率。
- **适用条件 / 局限** · 邻域和难度必须覆盖，非一般推理结果。

**可复用机制** · 留出结合低复杂度和分布偏移的任务，分别测预测斜率。

<a id="paper-153067"></a>

## Optimal In-Context Learning of Autoregressive Processes under Heterogeneous Second-Order Moments of the Prompts

[官方论文页](https://neurips.cc/virtual/2026/poster/153067) · [作者来源](https://openreview.net/forum?id=OEIZ6QQAsu)

- **问题 / 瓶颈** · 仅一阶均值不能区分过程。
- **核心创新 / 方法** · 分析线性注意和非线性头，给近最优二阶 AR(1) 估计的收敛。
- **Baseline** · 一阶上下文估计及最优二阶估计器。
- **Benchmark** · 异质提示二阶矩下的 AR(1) 理论和实验。
- **关键结果 / 消融** · 摘要称训练逼近目标函数且实证支持。
- **适用条件 / 局限** · 结构、训练参数化与过程受限。

**可复用机制** · 保持一阶矩、改变协方差验证机制。

<a id="paper-150063"></a>

## Optimal Learning-Augmented Algorithm for Online Bidding

[官方论文页](https://neurips.cc/virtual/2026/poster/150063) · [作者来源](https://openreview.net/forum?id=l10hVCrw4N)

- **问题 / 瓶颈** · 确定性最优折中不覆盖随机情况。
- **核心创新 / 方法** · 用阈值序列分布及延迟方程刻画 Pareto 边界。
- **Baseline** · 先前确定性及随机在线方法。
- **Benchmark** · 在线出价理论和线性搜索扩展。
- **关键结果 / 消融** · 闭合随机折中差距并改善线性搜索。
- **适用条件 / 局限** · 理论依赖损失和预测模型。

**可复用机制** · 在无害阈值搜索中从准确信号到坏信号扫两类指标。

<a id="paper-149470"></a>

## Optimal Linear Regression Without a Variance

[官方论文页](https://neurips.cc/virtual/2026/poster/149470) · [作者来源](https://openreview.net/forum?id=psDmvTWpNt)

- **问题 / 瓶颈** · 噪声不具方差时常规置信区间失效。
- **核心创新 / 方法** · 从经验残差作削减，无需知道噪声矩率或尺度。
- **Baseline** · 有限方差回归及极小极大下界。
- **Benchmark** · 协变量有限四阶矩下重尾回归理论。
- **关键结果 / 消融** · 高概率速率指数为 (α−1)/α，匹配下界。
- **适用条件 / 局限** · 需样本超过阈值及协变量条件。

**可复用机制** · 在尾部加重时比较修剪获得的预测误差与覆盖率。

<a id="paper-152628"></a>

## Optimal Rates for Adaptive Private $k$-PCA

[官方论文页](https://neurips.cc/virtual/2026/poster/152628) · [作者来源](https://openreview.net/forum?id=Rgs7JZ6dSS)

- **问题 / 瓶颈** · 逐向量消去使秩和谱隙成本增加。
- **核心创新 / 方法** · 对 d×k 基块做非消去式更新，并自适应隐私噪声。
- **Baseline** · k-DP-PCA 的逐向量消去。
- **Benchmark** · 次高斯及尖峰协方差模型。
- **关键结果 / 消融** · 摘要报告维数与秩样本复杂度最优，改善谱隙依赖。
- **适用条件 / 局限** · 保证受分布和谱条件限制。

**可复用机制** · 私有子空间估计也应做块算法对照，避免重复估计同一谱结构。

<a id="paper-152811"></a>

## Optimal Rates for Differentially Private Hypothesis Testing with E-values

[官方论文页](https://neurips.cc/virtual/2026/poster/152811) · [作者来源](https://openreview.net/forum?id=QEVhuw3jUX)

- **问题 / 瓶颈** · 有自适应停止要求的隐私分析不能依赖单一最终时点。
- **核心创新 / 方法** · 刻画最优隐私 e-power，并给私有 e-process 的停时匹配界。
- **Baseline** · DP-SPRT。
- **Benchmark** · 多个序贯二元检验及隐私等级。
- **关键结果 / 消融** · 摘要报告所提算法用更少数据。
- **适用条件 / 局限** · 依赖已知的两分布与 ε 隐私假设。

**可复用机制** · 将隐私预算与随时有效性共同设计，用达到同等证据所需样本比较。

<a id="paper-148362"></a>

## Optimal Rates for Pure $\varepsilon$-Differentially Private Stochastic Convex Optimization with Heavy Tails

[官方论文页](https://neurips.cc/virtual/2026/poster/148362) · [作者来源](https://openreview.net/forum?id=yRKg6vh4uv)

- **问题 / 瓶颈** · 最坏梯度上界可能不存在，纯隐私限值仍需保证。
- **核心创新 / 方法** · 在有界矩条件下私有优化扩展损失。
- **Baseline** · 既有零集中隐私及理论下界。
- **Benchmark** · 重尾随机凸优化及铰链、绝对值等结构类。
- **关键结果 / 消融** · 摘要给纯 ε 隐私近 minimax 率，一些结构类可确定多项式求解。
- **适用条件 / 局限** · 确定运行条件与损失结构相关。

**可复用机制** · 在强隐私约束下区分单例梯度异常和整个目标可估的平滑包络。

<a id="paper-148327"></a>

## Optimal Real-Data Allocation for Synthetic-Data-Augmented Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/148327) · [作者来源](https://openreview.net/forum?id=yemcYUgNFt)

- **问题 / 瓶颈** · 固定份额忽略合成方差和偏差下降速度。
- **核心创新 / 方法** · 用校准规模的偏差率与真实估计方差写最优条件。
- **Baseline** · 固定比例规则。
- **Benchmark** · 不同统计尺度下的真实与合成分配理论。
- **关键结果 / 消融** · 在主要条件下，最佳校准样本量次线性，固定比例会过量。
- **适用条件 / 局限** · 摘要末句截断，算法安全检查不作记录；理论依赖偏差模型。

**可复用机制** · 同时测校准后的残余偏差与真实样本估计方差，动态改变预算比例。

<a id="paper-153807"></a>

## Optimal Recalibration of an Online Predictor

[官方论文页](https://neurips.cc/virtual/2026/poster/153807) · [作者来源](https://openreview.net/forum?id=IZBCEtLXFZ)

- **问题 / 瓶颈** · 牺牲现有预测质量换校准可能降低效用。
- **核心创新 / 方法** · 以不平衡 Blackwell 可达性归约联合控制两项指标。
- **Baseline** · 已有在线校准与平方损失下界。
- **Benchmark** · Lipschitz 合适损失的在线理论。
- **关键结果 / 消融** · 约 ε^-3 轮实现 ε 校准及 ε² 额外损失，平方损失匹配。
- **适用条件 / 局限** · 依赖所测损失类和渐近。

**可复用机制** · 预设允许偏离的效用代价，同时监测校准误差，避免只优化其中一端。

<a id="paper-152669"></a>

## Optimal Representation Size: High-Dimensional Analysis of Pretraining and Linear Probing

[官方论文页](https://neurips.cc/virtual/2026/poster/152669) · [作者来源](https://openreview.net/forum?id=RHhBaG1Vop)

- **问题 / 瓶颈** · 表示小不总能在稀标签下更好泛化。
- **核心创新 / 方法** · 将无标注 PCA 与有标签线性探针分开并解析误差。
- **Baseline** · 不同表示维数的探针。
- **Benchmark** · 高维理论，另观察自动编码器和预训练 LLM。
- **关键结果 / 消融** · 预训练充分且标签少时强压缩有利，前者不足时大表示更优。
- **适用条件 / 局限** · 解析结论限简化两阶段模型。

**可复用机制** · 对少样本任务不要固定探针维度，要在不同预训练规模下重扫。

<a id="paper-151070"></a>

## Optimal Risk Bounds of Stochastic Gradient Descent for Shallow ReLU Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/151070) · [作者来源](https://openreview.net/forum?id=dBGhQx4fCF)

- **问题 / 瓶颈** · 已有风险结果常使用二次量级梯度计算。
- **核心创新 / 方法** · 控制随机轨迹波动并在 NTK 可分下分析 SGD。
- **Baseline** · 全量 GD。
- **Benchmark** · 对数宽浅网和间隔条件。
- **关键结果 / 消融** · 约线性计算达到此前近最优风险量级。
- **适用条件 / 局限** · 依赖近初始化与核间隔，不代表深网通用。

**可复用机制** · 固定风险目标比较所需梯度调用数，而非只对齐优化步数。

<a id="paper-149630"></a>

## Optimal scaling laws in learning hierarchical multi-index models

[官方论文页](https://neurips.cc/virtual/2026/poster/149630) · [作者来源](https://openreview.net/forum?id=odXDV3exT8)

- **问题 / 瓶颈** · 单一整体尺度不能解释层级恢复停滞。
- **核心创新 / 方法** · 分析多指标目标，使用目标无关谱估计恢复子空间再学读出。
- **Baseline** · 浅网梯度训练与信息下界。
- **Benchmark** · 表示受限的两层网络理论。
- **关键结果 / 消融** · 最优率由顺序恢复控制，出现相变和停滞。
- **适用条件 / 局限** · 依赖层级目标及理论数据。

**可复用机制** · 分别评估哪一层级刚获得可学信号，再投训练样本。

<a id="paper-148381"></a>

## Optimal sequential tests yield log-optimal e-processes

[官方论文页](https://neurips.cc/virtual/2026/poster/148381) · [作者来源](https://openreview.net/forum?id=yJdPgH8377)

- **问题 / 瓶颈** · 每个拒绝时刻可用不等于证据过程增长最优。
- **核心创新 / 方法** · 用加权停时指示构造单调 WAIT e-process。
- **Baseline** · 最优测试与最优 e-process 的已知单向结果。
- **Benchmark** · 渐近停时与长期对数证据理论。
- **关键结果 / 消融** · 摘要证明反向构造可达对数最优。
- **适用条件 / 局限** · 需明确所采用渐近最优定义。

**可复用机制** · 若有可信停时规则，先验证其组合能支持所需证据报告。

<a id="paper-149258"></a>

## Optimal Subgroup Discovery at Every Support Threshold

[官方论文页](https://neurips.cc/virtual/2026/poster/149258) · [作者来源](https://openreview.net/forum?id=rheTYmImAU)

- **问题 / 瓶颈** · 极小群组偏离大却不稳定，单标量掩盖折中。
- **核心创新 / 方法** · 先学同质划分，再贪心选整原子，边界最多需部分一个原子。
- **Baseline** · 既有子群发现及后处理。
- **Benchmark** · 19 数据集的 KL 偏离与覆盖。
- **关键结果 / 消融** · 摘要报告多支持下找到更偏离群组。
- **适用条件 / 局限** · 依赖划分逼近真实同质区域。

**可复用机制** · 让最小覆盖作为显式决策，并报告整个偏离支持前沿。

<a id="paper-149217"></a>

## Optimal Transport Reweighting for Robust Learning under Spurious Correlations and Label Noise

[官方论文页](https://neurips.cc/virtual/2026/poster/149217) · [作者来源](https://openreview.net/forum?id=s2EZiHa9PF)

- **问题 / 瓶颈** · 错标同样有大损失，可能被误作有效难例。
- **核心创新 / 方法** · 从有限有组别的验证集建参考分布，以传输对齐定权后单次 ERM。
- **Baseline** · 基于损失的重训加权。
- **Benchmark** · 多个有噪声的子群偏移基准。
- **关键结果 / 消融** · 摘要报告包括少数群体错标时最差群体准确改善。
- **适用条件 / 局限** · 依赖参考样本代表性与匹配特征。

**可复用机制** · 将组对齐和训练损失大小分离，防止错标样本消耗难例预算。

<a id="paper-150725"></a>

## Optimistic Dual Averaging Unifies Modern Optimizers

[官方论文页](https://neurips.cc/virtual/2026/poster/150725) · [作者来源](https://openreview.net/forum?id=fsvzA0o8vh)

- **问题 / 瓶颈** · 不同优化器的经验规则使权重衰减调参代价高。
- **核心创新 / 方法** · 用 SODA 统一乐观对偶平均，给任意基座加 1/k 衰减。
- **Baseline** · Muon、Lion、AdEMAMix、NAdam。
- **Benchmark** · 不同规模与训练周期。
- **关键结果 / 消融** · 摘要报告无需额外调参仍有改善。
- **适用条件 / 局限** · 机制不保证所有任务的最好衰减。

**可复用机制** · 先用有理论依据的日程作各基座共同对照，再投入逐模型搜索。

<a id="paper-155898"></a>

## Optimistic Q-value Adaptation for Offline-to-Online Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/155898) · [作者来源](https://openreview.net/forum?id=20yOoplUQb)

- **问题 / 瓶颈** · 策略受限和价值正则两种离线法都可能低估。
- **核心创新 / 方法** · 离线另预训一对 actor critic，与原对组成受控乐观备份。
- **Baseline** · TD3+BC、CQL 与现有离线到在线方法。
- **Benchmark** · D4RL MuJoCo、Maze2D、AntMaze、Adroit。
- **关键结果 / 消融** · 摘要报告跨两类骨干改善。
- **适用条件 / 局限** · 需控制额外估计偏差和离线算力。

**可复用机制** · 不要只调策略约束，应检查价值偏差会不会在新数据自举中累积。

<a id="paper-150875"></a>

## Optimization Dynamics Imprint Semantic Specificity in Contrastive Embedding Norms

[官方论文页](https://neurips.cc/virtual/2026/poster/150875) · [作者来源](https://openreview.net/forum?id=ejpcbuLKfg)

- **问题 / 瓶颈** · 训练损失对缩放不敏感不代表实际范数无信息。
- **核心创新 / 方法** · 分析优化动力，解释长度与语义具体度等量的联系。
- **Baseline** · 只用方向的余弦读出。
- **Benchmark** · 若干嵌入及检索校准任务。
- **关键结果 / 消融** · 摘要报告推导可支撑特定模型的免费校准信号。
- **适用条件 / 局限** · 范数关联可能随训练及域变化。

**可复用机制** · 对比方向和长度各自带来的可校准信息，不默认归一化无损。

<a id="paper-150439"></a>

## Optimized Forward-Backward Rematerialization for Memory-Efficient Pipeline Parallel Training

[官方论文页](https://neurips.cc/virtual/2026/poster/150439) · [作者来源](https://openreview.net/forum?id=i1zm1UWbH2)

- **问题 / 瓶颈** · 固定重算配置难覆盖显存和调度差异。
- **核心创新 / 方法** · 允许解耦梯度时在反传内重算，用 ILP 分配设备与微批。
- **Baseline** · 既有重算和一波、多波调度。
- **Benchmark** · 不同设备内存和大模型训练。
- **关键结果 / 消融** · 摘要报告最优调度随显存改变，重算开销下降。
- **适用条件 / 局限** · 依赖算子耗时和内存测量。

**可复用机制** · 将调度和重算作为同预算问题求解，而非先选最快调度再被动修内存。

<a id="paper-156024"></a>

## Optimizer-Induced Mode Connectivity: From AdamW to Muon

[官方论文页](https://neurips.cc/virtual/2026/poster/156024) · [作者来源](https://openreview.net/forum?id=15PMEzUEgp)

- **问题 / 瓶颈** · 零损解的连通性可能依赖隐式正则。
- **核心创新 / 方法** · 按优化器划定解集合，分析宽度和交集，再检查路径谱。
- **Baseline** · 同优化器和跨 AdamW、Muon 路径。
- **Benchmark** · 两层 ReLU 理论与 GPT-2。
- **关键结果 / 消融** · 宽时同优化器集合连通，窄例跨优化器间有损失屏障。
- **适用条件 / 局限** · 理论限简化模型，不能预测所有合并。

**可复用机制** · 跨优化器融合独立检查路径损失和谱变化，不用同骨干作充分条件。

<a id="paper-151696"></a>

## Optimizing Agent Tool-Use via Trajectory-based Insight Evolution

[官方论文页](https://neurips.cc/virtual/2026/poster/151696) · [作者来源](https://openreview.net/forum?id=YhqhX9eS3E)

- **问题 / 瓶颈** · 说明歧义和缺例可使代理无法正确调用。
- **核心创新 / 方法** · 生成有差异的轨迹，回看哪些说明变化与成功相关，迭代改文档。
- **Baseline** · 参数微调、强化及原工具说明。
- **Benchmark** · 若干工具任务域的调用正确和成功率。
- **关键结果 / 消融** · 摘要报告两方面改善。
- **适用条件 / 局限** · 轨迹归因会受其他因素混淆；需版本化验证。

**可复用机制** · 将文档作为可优化的外部接口，每次改动后重放成功与失败对照。

<a id="paper-155093"></a>

## Optimizing Analytic Constants via AI-Guided Lean Proof Refinement

[官方论文页](https://neurips.cc/virtual/2026/poster/155093) · [作者来源](https://openreview.net/forum?id=8UcFFcJ2fm)

- **问题 / 瓶颈** · 无结构提示下代理难以定位改参数对最终界的影响。
- **核心创新 / 方法** · 以 Lean 部分形式化蓝图分解证明，让局部改写自动传到结果。
- **Baseline** · 既有文献中的常数界。
- **Benchmark** · Grothendieck 和 Korenblum 常数。
- **关键结果 / 消融** · 摘要报告两个常数的严格改善。
- **适用条件 / 局限** · 蓝图由相关文献搭建，未证明自主选择全部策略。

**可复用机制** · 先将需要保持的论证用内核验收，再开放小范围搜索可改部分。

<a id="paper-155480"></a>

## Optimizing Computational-Statistical Runtime for Wasserstein Distance Estimation

[官方论文页](https://neurips.cc/virtual/2026/poster/155480) · [作者来源](https://openreview.net/forum?id=5GGreyp28W)

- **问题 / 瓶颈** · 直接解经验分布精度可能超过样本本身支持的能力。
- **核心创新 / 方法** · 抽样后把经验分布压成规则笛卡尔网格，再用规则结构求解。
- **Baseline** · 直接按样本求精确或近似 Wasserstein。
- **Benchmark** · 低维欧氏分布，测加性误差与运行时间。
- **关键结果 / 消融** · Hölder 平滑等条件下可压缩而不增渐近误差。
- **适用条件 / 局限** · 高维网格灾难和稀疏分布条件待查。

**可复用机制** · 把数值误差预算绑定统计下界，避免在错误精度目标上烧算力。

<a id="paper-154395"></a>

## Optimizing Retraining Schedules via Learning Curves

[官方论文页](https://neurips.cc/virtual/2026/poster/154395) · [作者来源](https://openreview.net/forum?id=DtRZYbRdO0)

- **问题 / 瓶颈** · 每步重训成本高，固定周期忽略收益递减。
- **核心创新 / 方法** · 按风险与曲线间距构造日程，并在线适应未知幂指数。
- **Baseline** · 每步重训。
- **Benchmark** · 独立同分布可实现学习，及漂移扩展。
- **关键结果 / 消融** · 单调曲线下对数次更新够用，缓慢幂律情形降至双对数。
- **适用条件 / 局限** · 有漂移时不能直接使用静态次数界。

**可复用机制** · 先测增量样本能减少多少风险，再据该幅度决定是否重训。

<a id="paper-150636"></a>

## Oracle-Robust Online Alignment for Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150636) · [作者来源](https://openreview.net/forum?id=gd1SmOZK7y)

- **问题 / 瓶颈** · 在线更新与偏好数据采集相互耦合。
- **核心创新 / 方法** · 在单层对齐目标加入逐点 oracle 不确定集；对数线性策略可拆成经验损失与敏感性罚项。
- **Baseline** · SAIL 原目标。
- **Benchmark** · 理论近似驻点及查询复杂度。
- **关键结果 / 消融** · 给出闭式分解，查询复杂度约为精度倒数平方。
- **适用条件 / 局限** · 依赖对数线性形式及不确定集是否覆盖真评委。

**可复用机制** · 把评委不确定性显式当成量化假设，与仅换评委和调损失权重作对照。

<a id="paper-149392"></a>

## OrbitLoRA: Learning Rotation-Aware Low-Data Adaptation of Vision Foundation Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149392) · [作者来源](https://openreview.net/forum?id=qP2piMgcsC)

- **问题 / 瓶颈** · 普通 token 不保证对旋转作可预测变换。
- **核心创新 / 方法** · LoRA 配合具有标量与向量类型的残差分支，用可转向特征和谐波坐标初始化。
- **Baseline** · 帧平均、规范化和标准低秩适配。
- **Benchmark** · 科学成像的低数据跨方向适配。
- **关键结果 / 消融** · 摘要强调无需整体重训的旋转感知构造。
- **适用条件 / 局限** · 真实旋转下的效果、插入深度与等变程度待查。

**可复用机制** · 把旋转一致性和下游精度分别验收，避免只在合成旋转上选用模型。

<a id="paper-154803"></a>

## ORCA: Hunting Compositional Failures in Text-to-Image Diffusion

[官方论文页](https://neurips.cc/virtual/2026/poster/154803) · [作者来源](https://openreview.net/forum?id=Ar6frZW38L)

- **问题 / 瓶颈** · 已有语言组合线索不一定被去噪目标使用。
- **核心创新 / 方法** · 在自监督视觉特征的低秩分量上加入跨模态组合对齐辅助损失。
- **Baseline** · 现有 CLIP 与 T5 联合扩散。
- **Benchmark** · 属性、相对位置和计数等组合生成。
- **关键结果 / 消融** · 作者报告低秩视觉结构可作为组合监督。
- **适用条件 / 局限** · 低秩选择、独立对照与具体提升待查。

**可复用机制** · 以相同文字编码器比较去噪损失和组合对齐，避免把问题归因给词语表示不足。

<a id="paper-155849"></a>

## OrchestraRL: Learning to Orchestrate LLM Agent Swarms with Entropy-Aware Communication Control

[官方论文页](https://neurips.cc/virtual/2026/poster/155849) · [作者来源](https://openreview.net/forum?id=2R3giVsHQ5)

- **问题 / 瓶颈** · 群体变大并不必然提高结果。
- **核心创新 / 方法** · 用输出嵌入分散度估计群体状态，由宏层选通信方式与拓扑，微层选发言对象及时机。
- **Baseline** · 随机广播与单代理。
- **Benchmark** · SWE-bench Verified，八代理、每题 64 调用、Claude Opus 4.5。
- **关键结果 / 消融** · 固定预算下由 80.4% 提到 85.5%，单代理为 80.9%。
- **适用条件 / 局限** · 所报差值限当前预算与模型，其他任务及控制器训练成本待查。

**可复用机制** · 对照相同调用数和角色，检查性能收益来自消息组织还是多用计算。

<a id="paper-154353"></a>

## Order-Marginalized Scoring for Masked Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154353) · [作者来源](https://openreview.net/forum?id=EE2N89jedk)

- **问题 / 瓶颈** · 虽然训练对顺序对称，单个顺序的候选排名可能大变。
- **核心创新 / 方法** · 抽多个解码排列作 Monte Carlo 估计，用于重排或 best-of-N。
- **Baseline** · 单固定顺序计分。
- **Benchmark** · PCFG 与 OpenWebText 扩散模型，固定候选池。
- **关键结果 / 消融** · 作者观察多数输入的单序排名有分歧。
- **适用条件 / 局限** · 顺序抽样数与额外推理的最佳折中待查。

**可复用机制** · 先测排序方差，再选择是否值得为候选分数跨路径取平均。

<a id="paper-152754"></a>

## Ordinal Geometry Complements Reconstruction: Diagnosing Planning with Compressed Value Functions

[官方论文页](https://neurips.cc/virtual/2026/poster/152754) · [作者来源](https://openreview.net/forum?id=QbTBLTxehl)

- **问题 / 瓶颈** · 拓扑造成大量很小的价值差时，均方可与局部选动作质量脱钩。
- **核心创新 / 方法** · 测邻域排序保真，在固定环境效应和单调重标后比较预测力。
- **Baseline** · 仅 L2 重建评分。
- **Benchmark** · 网格、八个连续导航环境及三种 Maze2D 布局。
- **关键结果 / 消融** · 邻域排序在控制环境后新增解释度 0.106，单调改变可大幅改变 L2。
- **适用条件 / 局限** · 结果依赖局部邻居和规划器，复杂奖励需查。

**可复用机制** · 将价值标定和局部择优分开验收，用排序保真解释规划性能。

<a id="paper-153277"></a>

## Ordinary Least Squares as an Attention Mechanism

[官方论文页](https://neurips.cc/virtual/2026/poster/153277) · [作者来源](https://openreview.net/forum?id=MRyrIW18CW)

- **问题 / 瓶颈** · 注意层未必需要全参数训练。
- **核心创新 / 方法** · 将 OLS 写成嵌入内积匹配，扩展到多项式回归替代层。
- **Baseline** · 标准表格 Transformer 和常用回归。
- **Benchmark** · UCI、OpenML 与 Monte Carlo。
- **关键结果 / 消融** · 摘要称相近或更高精度且参数更少。
- **适用条件 / 局限** · 高维特征展开成本待核。

**可复用机制** · 固定输入与预算比较注意权重和回归权重。

<a id="paper-153614"></a>

## Orlicz–Sobolev with Musielak: An Efficient Regularization Approach for Graph-based IPM

[官方论文页](https://neurips.cc/virtual/2026/poster/153614) · [作者来源](https://openreview.net/forum?id=K4gYi2bonY)

- **问题 / 瓶颈** · Sobolev IPM 固定了几何。
- **核心创新 / 方法** · 借 Orlicz 和 Musielak 范数关系正则化，将计算化作一元优化。
- **Baseline** · 普通 Sobolev IPM 和 Orlicz–Wasserstein。
- **Benchmark** · 图文档分类与拓扑数据分析。
- **关键结果 / 消融** · 摘要称对后者快多个数量级，任务表现有竞争力。
- **适用条件 / 局限** · 依赖图度量与特定凸函数。

**可复用机制** · 在相同距离质量下比较先验几何与求解时间。

<a id="paper-139041"></a>

## OroPrecipBench: a km-scale benchmark for spatial precipitation downscaling over complex terrain

[官方论文页](https://neurips.cc/virtual/2026/poster/139041) · [作者来源](https://openreview.net/forum?id=oIt8ejKQlL)

- **问题 / 瓶颈** · 像素误差低仍可破坏降水海拔剖面。
- **核心创新 / 方法** · 采用同地理双轨验证，另测地形条件分布。
- **Baseline** · 十种统计、确定性或生成方法。
- **Benchmark** · 五个美国地形区，HRRR 与 ERA5 到 PRISM。
- **关键结果 / 消融** · 理想超分提升未稳定迁移，剖面及极端量尤脆弱。
- **适用条件 / 局限** · 区域和数据源局限待核。

**可复用机制** · 同时报告像素、地形剖面与尾降雨误差。

<a id="paper-150309"></a>

## Orthogonal Origin Parking: Decoupling Lorentz Manifolds for Robust OOD Generalization

[官方论文页](https://neurips.cc/virtual/2026/poster/150309) · [作者来源](https://openreview.net/forum?id=j5DnkgPGKb)

- **问题 / 瓶颈** · 宽大支系占用同一双曲空间的角度容量。
- **核心创新 / 方法** · 将根支路分配到独立 Lorentz 因子，并将无关因子约束到原点。
- **Baseline** · 欧式及单一双曲流形。
- **Benchmark** · 四种生物影像类分布外分类。
- **关键结果 / 消融** · 摘要称低维子空间能保留细粒度与税目层级。
- **适用条件 / 局限** · 依赖可信层级及根分类。

**可复用机制** · 对照不分层和多空间，按小支系单独计错。

<a id="paper-155965"></a>

## Orthogonal Sparse Subgraph Alignment for Structure-Function Coupling in Brain Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/155965) · [作者来源](https://openreview.net/forum?id=1VRjEYWcHX)

- **问题 / 瓶颈** · 全局配准可能掩盖局部一致结构。
- **核心创新 / 方法** · 按功能社区做正交对齐和稀疏节点选择。
- **Baseline** · 相同节点数基线。
- **Benchmark** · 合成与 ABCD 脑结构记录。
- **关键结果 / 消融** · 报告可恢复旋转下的子图且样本外相关更强。
- **适用条件 / 局限** · 统计一致性限所设生成条件。

**可复用机制** · 在非生物双网络构造已知稀疏对应，验坐标与节点恢复。

<a id="paper-155673"></a>

## Orthogonal Updates for the Win: Towards Accelerated Adaptive Minimax Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/155673) · [作者来源](https://openreview.net/forum?id=3qFdSTZko6)

- **问题 / 瓶颈** · 正交处理改几何，固定步长易振荡。
- **核心创新 / 方法** · 由累计梯度范数调步，并加方差降低变体。
- **Baseline** · 现有单循环随机极小极大方法。
- **Benchmark** · 非凸强凹理论及实验。
- **关键结果 / 消融** · 普通版 T^−1/4，方差降低 T^−1/3。
- **适用条件 / 局限** · 依赖强凹平滑设定。

**可复用机制** · 比较两侧更新规模和驻点误差。

<a id="paper-154343"></a>

## Orthogonal Uplift Learning with Permutation-Invariant Representations for Combinatorial Treatments

[官方论文页](https://neurips.cc/virtual/2026/poster/154343) · [作者来源](https://openreview.net/forum?id=EIVfHEXb1P)

- **问题 / 瓶颈** · 把新政策当离散标签不能泛化。
- **核心创新 / 方法** · 以置换不变聚合编码条件动作混合，并做正交低秩 uplift。
- **Baseline** · 类别编码及一般表示。
- **Benchmark** · 平台随机试验与长尾政策。
- **关键结果 / 消融** · 摘要称准确和稳定提升。
- **适用条件 / 局限** · 依赖随机化、支持及政策表示。

**可复用机制** · 在无害合成策略上区别新组合和新频率带来的偏差。

<a id="paper-154438"></a>

## OrthoReg: Orthogonal Regularization for Hybrid Symbolic-Neural Dynamical Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/154438) · [作者来源](https://openreview.net/forum?id=DXi8r1Jvin)

- **问题 / 瓶颈** · 只做 L2 正则无法防止残差复制符号部分。
- **核心创新 / 方法** · 以正交项隔离符号库可表达成分和补充项。
- **Baseline** · 标准 L2 正则。
- **Benchmark** · 部分符号库失配的动力学基准。
- **关键结果 / 消融** · 恢复与域外预测改善。
- **适用条件 / 局限** · 符号库严重错误时仍不能解释残差。

**可复用机制** · 分别验符号恢复、外推和总预测。

<a id="paper-154037"></a>

## Orthros: Phase-Aware Heterogeneous Attention for Efficient Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/154037) · [作者来源](https://openreview.net/forum?id=Ggocm0VXS9)

- **问题 / 瓶颈** · 固定全注意夹杂会保留预填充平方瓶颈。
- **核心创新 / 方法** · 同一模块在线性预填充与全注意解码之间切换。
- **Baseline** · 普通 Transformer 和线性、滑窗注意。
- **Benchmark** · 多规模语言及 128K 检索。
- **关键结果 / 消融** · 最高预填充快 21.9 倍，原地转换后实证有竞争力。
- **适用条件 / 局限** · 短上下文或重解码未必受益。

**可复用机制** · 按输入输出长度网格比较首词和整体时延。

<a id="paper-150719"></a>

## Orthrus: Memory-Efficient Parallel Token Generation via Dual-View Diffusion

[官方论文页](https://neurips.cc/virtual/2026/poster/150719) · [作者来源](https://openreview.net/forum?id=fwaVRSuVPd)

- **问题 / 瓶颈** · 独立并行模型容易损精度并重复缓存。
- **核心创新 / 方法** · 冻结底座，加入扩散视图作并行候选，通过共识验证保持精确。
- **Baseline** · 逐词自回归与纯扩散。
- **Benchmark** · 并行生成质量、缓存与速度。
- **关键结果 / 消融** · 摘要称无损且最高 7.8 倍，附加缓存 O(1)。
- **适用条件 / 局限** · 需核对硬件、采样匹配和接受率。

**可复用机制** · 以相同随机种子与基准分布确认并行版本保真。

<a id="paper-139359"></a>

## OS-Omni: A Cross-Platform Benchmark for Generalist Computer-Using Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/139359) · [作者来源](https://openreview.net/forum?id=UlijzWpwGW)

- **问题 / 瓶颈** · 不同系统可做同一步却无法完整跟踪状态。
- **核心创新 / 方法** · 统一可复现初始条件、轨迹记录和可执行终态验收。
- **Baseline** · 人工与多个计算机助手。
- **Benchmark** · 六类平台 1,200 任务。
- **关键结果 / 消融** · 最强代理 47.1% 对人工 88.1%，困难任务跌至 16.4%。
- **适用条件 / 局限** · 特定任务及平台覆盖。

**可复用机制** · 用无害测试日历等验证最终状态，按复杂度分层。

<a id="paper-151204"></a>

## OS-Pruner: Pruning Chains-of-Thought of Reasoning Models via Optimal Stopping

[官方论文页](https://neurips.cc/virtual/2026/poster/151204) · [作者来源](https://openreview.net/forum?id=cB7emUeNVr)

- **问题 / 瓶颈** · 静态预算过短或过长。
- **核心创新 / 方法** · 从前缀训练轻停止器优化预设效用。
- **Baseline** · 固定预算、启发式与其他提前退出。
- **Benchmark** · 多推理模型和基准。
- **关键结果 / 消融** · 摘要报缩短 20%–60%，准确损失较少。
- **适用条件 / 局限** · 需检查训练外难题。

**可复用机制** · 改变代价权重绘制准确、长度与实际时延曲线。

<a id="paper-152476"></a>

## OTEdit: Entropic Transport Corrected Trajectory for Inversion-Free Flow-Based Image Editing

[官方论文页](https://neurips.cc/virtual/2026/poster/152476) · [作者来源](https://openreview.net/forum?id=SnQJpsC6YB)

- **问题 / 瓶颈** · 单 ODE 轨迹易受随机漂移。
- **核心创新 / 方法** · 以潜粒子间熵正则传输构造时变修正，并按累计偏差调强度。
- **Baseline** · 无反演的单轨迹编辑。
- **Benchmark** · 多图像编辑实验和人偏好。
- **关键结果 / 消融** · 报告结构保真与语义对齐改善。
- **适用条件 / 局限** · 每步传输和粒子数增加成本。

**可复用机制** · 同耗时比较多个轨迹提供的稳定性和细节保留。

<a id="paper-148743"></a>

## OTformer: Non-Stationarity-Aware Adaptive Optimal Transport Attention for Time Series Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/148743) · [作者来源](https://openreview.net/forum?id=vNR0rYjfuq)

- **问题 / 瓶颈** · 固定 softmax 硬度不适合各种漂移。
- **核心创新 / 方法** · 从未归一统计估非平稳性并调 Sinkhorn 熵，另加入周期位置。
- **Baseline** · iTransformer。
- **Benchmark** · 八集 32 设置，ECL 和 Solar 等。
- **关键结果 / 消融** · ECL、Solar 跨时长平均 MSE 降 4.4%、12.5%。
- **适用条件 / 局限** · 需拆分周期和熵作用。

**可复用机制** · 对已知漂移强度的控制序列观察路由变化。

<a id="paper-156785"></a>

## OTIS: Learning High-Quality Time Series Features With Tiny Encoders

[官方论文页](https://neurips.cc/virtual/2026/poster/156785) · [作者来源](https://neurips.cc/virtual/2026/poster/156785)

- **问题 / 瓶颈** · 盲目扩模型导致传感设备难部署。
- **核心创新 / 方法** · 域感知分词和双遮盖协同，将噪声预测从结构特征中分离。
- **Baseline** · 大规模通用编码器。
- **Benchmark** · 162 任务及资源测评。
- **关键结果 / 消融** · 7.1M 匹配大 54 倍的对照，报告更省内存、时延和能源。
- **适用条件 / 局限** · 资源口径及三部件消融待核。

**可复用机制** · 固定参数测跨域以及纯去噪和结构任务。

<a id="paper-150253"></a>

## OT-Robust3DVLA: A Wasserstein Barycenter is the Right Inductive Bias for Robust Multi-View 3D Vision-Language-Action Policies

[官方论文页](https://neurips.cc/virtual/2026/poster/150253) · [作者来源](https://openreview.net/forum?id=jZB1x1CTzW)

- **问题 / 瓶颈** · 小标定变化会重新排列拼接标记。
- **核心创新 / 方法** · 用 Wasserstein 重心融合视图测度成固定数量标记。
- **Baseline** · 拼接注意与其他融合。
- **Benchmark** · 合成、LIBERO、RLBench 和 CALVIN ABC→D。
- **关键结果 / 消融** · 合成闭环拼接由 85% 到 0%，重心最坏条件 92%。
- **适用条件 / 局限** · 界依扰动集和求解残差，实机安全需检。

**可复用机制** · 固定后续策略，以多种 benign 传感扰动审计动作稳定。

<a id="paper-149690"></a>

## OTROPE: Optimal Transport-based Robust Off-policy Evaluation for Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149690) · [作者来源](https://openreview.net/forum?id=oA3cCf5Xta)

- **问题 / 瓶颈** · 旧模型标签分布不能直接评价新模型。
- **核心创新 / 方法** · 运输重配样本，结合评审代理与人工残差。
- **Baseline** · 普通评审及密度比路线。
- **Benchmark** · 合成和真实语言模型评测。
- **关键结果 / 消融** · 报告稳定优于参考，并给两类收敛条件。
- **适用条件 / 局限** · 语义嵌入不一定保留质量因素。

**可复用机制** · 以随机抽取的新模型人工标注验均值和误差。

<a id="paper-151111"></a>

## Outcome-Based RL Provably Leads Transformers to Reason, but Only With the Right Data

[官方论文页](https://neurips.cc/virtual/2026/poster/151111) · [作者来源](https://openreview.net/forum?id=ctcKsexBkZ)

- **问题 / 瓶颈** · 全长难链的稀疏反馈不足以引出分步算法。
- **核心创新 / 方法** · 分析单层 Transformer 在图遍历上如何经短样本学逐顶点移动。
- **Baseline** · 不同短实例占比及更长测试链。
- **Benchmark** · 合成遍历及语言数学推理。
- **关键结果 / 消融** · 短例达到一定质量比例时可学可外推策略，比例消失时学习受阻。
- **适用条件 / 局限** · 严格条件限受控模型，迁移实验不能证明普遍。

**可复用机制** · 用能提供早期学习信号的最小子问题作课程，并验证是否习得可递归操作。

<a id="paper-149012"></a>

## Out-of-Distribution Detection in Continual Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149012) · [作者来源](https://openreview.net/forum?id=tUbhxJCUrN)

- **问题 / 瓶颈** · 只验已知分类会忽略旧任务的开放集误报。
- **核心创新 / 方法** · 按任务控制 KAN 激活局部范围，并以几何打分补置信。
- **Baseline** · 回放式和置信拒识。
- **Benchmark** · 持续学习的已知分类和未知检测。
- **关键结果 / 消融** · 摘要报告维持分类并提升未知拒识。
- **适用条件 / 局限** · 几何评分如何跨任务校准需核实。

**可复用机制** · 避免依赖全局置信，在每次任务更新后独立校验旧类与陌生输入的可分性。

<a id="paper-150982"></a>

## Overcoming Attention Distraction: Training-Free Latent Communication for Multi-Agent Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/150982) · [作者来源](https://openreview.net/forum?id=dndnlqP2vp)

- **问题 / 瓶颈** · 拼接后 softmax 可能放大角色不一致产生的无关状态。
- **核心创新 / 方法** · 抽取上游主语义方向，按信噪动态缩放其投影后加到下游。
- **Baseline** · 拼接跨注意。
- **Benchmark** · 54 个多代理组合和长上下文推理。
- **关键结果 / 消融** · 摘要报告 46 项优于对照。
- **适用条件 / 局限** · 依赖角色间有共享子空间，维数与成本待核实。

**可复用机制** · 先对齐传递的语义分量再叠加，避免把各代理的完整隐藏状态混入竞争。

<a id="paper-151854"></a>

## Overcoming Catastrophic Forgetting in Visual Continual Learning with Reinforcement Fine-Tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/151854) · [作者来源](https://openreview.net/forum?id=XQ0Bir2SLj)

- **问题 / 瓶颈** · 相同任务奖励可掩盖引发遗忘的轨迹差异。
- **核心创新 / 方法** · 将旧策略轨迹 KL 变成保留奖励，以跨任务 EMA 规范优势。
- **Baseline** · 常规 RFT 与 SFT。
- **Benchmark** · 五种分类、视频和检测的类增量域增量设置。
- **关键结果 / 消融** · 摘要报告减少遗忘且保持可塑性。
- **适用条件 / 局限** · 需要旧策略或其评估信号，稳定权重需任务校验。

**可复用机制** · 同解题质量时优先保留对已有能力改变较温和的轨迹。

<a id="paper-149563"></a>

## Overcoming Kernel Redundancy for Scaling Logic Gate Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/149563) · [作者来源](https://openreview.net/forum?id=pBQwXLxijA)

- **问题 / 瓶颈** · 加宽常只复制相似逻辑模式。
- **核心创新 / 方法** · 在首门层用输入依赖动态逻辑核选路，保持布尔执行。
- **Baseline** · 朴素加宽的逻辑门网络。
- **Benchmark** · 核多样性、参数效率及分类表现。
- **关键结果 / 消融** · 摘要报告最早层重复最多，动态选择提升利用率及精度。
- **适用条件 / 局限** · 对更复杂布尔部署仍需检验成本。

**可复用机制** · 把稀疏容量投给重复最严重层，并直接测增加宽度带来的有效功能。

<a id="paper-152172"></a>

## Overcoming Rank Collapse in Feedback Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/152172) · [作者来源](https://openreview.net/forum?id=V0LvPorUoL)

- **问题 / 瓶颈** · 固定反馈方向可能只探索低维子空间。
- **核心创新 / 方法** · 以 Muon 正交更新和激活归一化扩展反馈维度。
- **Baseline** · 反向传播与普通反馈对齐。
- **Benchmark** · CIFAR-10、CIFAR-100 和更深架构。
- **关键结果 / 消融** · ResNet-18 的 CIFAR-100 准确高九个百分点。
- **适用条件 / 局限** · 证据集中在视觉网络，泛化与原因需验证。

**可复用机制** · 不给反馈信号无目标加噪，先针对低秩限制做正交化对照。

<a id="paper-152208"></a>

## Overcoming State Inertia in Full-Duplex Spoken Language Models via Activation Steering

[官方论文页](https://neurips.cc/virtual/2026/poster/152208) · [作者来源](https://openreview.net/forum?id=Uly2PDh7XI)

- **问题 / 瓶颈** · 生成偏置持续会丢掉用户起始词。
- **核心创新 / 方法** · 探查两路预测状态，用感知方向对中断做免训校正。
- **Baseline** · 原模型，无感知引导。
- **Benchmark** · 零缓冲中断评估，正确率和初始词出现率。
- **关键结果 / 消融** · PersonaPlex 正确率从 28% 到 45%，初词出现从 40% 到 72%。
- **适用条件 / 局限** · 提前切换过强可能抑制合理继续说话。

**可复用机制** · 分别测中断检测和起始内容理解，避免只测最后是否停说。

<a id="paper-151945"></a>

## Overcoming the Resolution Limit: Significance-Aware Regularization for Intersectional Fairness

[官方论文页](https://neurips.cc/virtual/2026/poster/151945) · [作者来源](https://openreview.net/forum?id=WeKiJiGv0V)

- **问题 / 瓶颈** · 稀组随机偏差容易被当真差异过拟合。
- **核心创新 / 方法** · 用显著超额与软计数似然比，仅强调可认证的差异。
- **Baseline** · 不区分显著性的公平正则。
- **Benchmark** · 三个基准和稀组压力测试。
- **关键结果 / 消融** · 摘要报告公平效用折中改善，无认证差异时梯度极小。
- **适用条件 / 局限** · 强依赖组样本量和显著性设定。

**可复用机制** · 先估统计支持再惩罚群体差异，避免浪费模型容量拟合噪声。

<a id="paper-152216"></a>

## Oversmoothing as Representation Degeneracy in Neural Sheaf Diffusion

[官方论文页](https://neurips.cc/virtual/2026/poster/152216) · [作者来源](https://openreview.net/forum?id=UhbffncO5W)

- **问题 / 瓶颈** · 把过平滑只当谱衰减无法说明学到的几何退化。
- **核心创新 / 方法** · 用关联箭图表示分解谐空间，考察矩映射正则与不等维设置。
- **Baseline** · 等 stalk 维数和其他图扩散约束。
- **Benchmark** · 异配图数据及谱和表示分析。
- **关键结果 / 消融** · 摘要称不等维去除已证结构障碍，部分数据验证稳定性改善。
- **适用条件 / 局限** · 提升具数据依赖，不保证通用。

**可复用机制** · 检查限制表示分解的结构约束，再决定是否调正则强度。

<a id="paper-150716"></a>

## Overthinking as a Symptom of Knowledge Conflict: Understanding and Detecting LLM's Hallucinations in Retrieval-Augmented Question Answering

[官方论文页](https://neurips.cc/virtual/2026/poster/150716) · [作者来源](https://openreview.net/forum?id=fzpG3voiei)

- **问题 / 瓶颈** · 长度增加也可能来自证据与先验难协调。
- **核心创新 / 方法** · 按冲突模式分类及打分，对不同程度使用区分的诊断。
- **Baseline** · 只凭长度或普通检测。
- **Benchmark** · 三个 QA 数据及三个模型。
- **关键结果 / 消融** · 摘要报告单次输出可改善幻觉检测。
- **适用条件 / 局限** · 关联不等因果，且需在新模型重新标定。

**可复用机制** · 验收要同时核对推理冗余与冲突证据，不以长度阈值取代证据。

<a id="paper-139810"></a>

## OWCE: Revealing Language Model Complementarity via Online Weakness-Conditioned Evaluation

[官方论文页](https://neurips.cc/virtual/2026/poster/139810) · [作者来源](https://openreview.net/forum?id=3A8dgOgJRK)

- **问题 / 瓶颈** · 整体排行榜不能指出谁能覆盖某模型偏错。
- **核心创新 / 方法** · 按各模型弱点生成难度递进题，并交叉评所有模型。
- **Baseline** · 静态总体分数。
- **Benchmark** · 七基准、七模型。
- **关键结果 / 消融** · 最佳伙伴使失败率最多降 25 个百分点，并不总是全局首名。
- **适用条件 / 局限** · 生成题质量及初始弱点覆盖影响结果。

**可复用机制** · 构建错误重叠矩阵辅助路由，而非只按单模型平均得分组队。

<a id="paper-149556"></a>

## OxyGen: Unified KV Cache Management for VLA Inference under Multi-Task Parallelism

[官方论文页](https://neurips.cc/virtual/2026/poster/149556) · [作者来源](https://openreview.net/forum?id=pGA2narTk6)

- **问题 / 瓶颈** · 独立解码重复视觉预填充，语言变长拖慢固定频率动作。
- **核心创新 / 方法** · 共享跨任务 KV，跨帧持续批处理语言与动作。
- **Baseline** · 隔离执行的 pi0.5。
- **Benchmark** · RTX 4090、Jetson AGX Thor 及实机人形。
- **关键结果 / 消融** · 最多加速 3.7 倍，同时 200+ 词元每秒及 70Hz 动作。
- **适用条件 / 局限** · 依赖骨干前缀共享与硬件调度。

**可复用机制** · 在统一缓存层保护动作时限，不把慢任务与动作步强同步。

<a id="paper-150553"></a>

## P$^{3}$: Joint Program-and-Proof Planning\\ for Verified Code Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/150553) · [作者来源](https://openreview.net/forum?id=hIC9ua4c4q)

- **问题 / 瓶颈** · 实现结束后发现证明困难会反复交替返工。
- **核心创新 / 方法** · 由规范生成统一程序证明计划，再展开两部分交给形式检验。
- **Baseline** · 先代码后证明的强基线。
- **Benchmark** · Verina、AlgoVeri、Lean4Commit0，四骨干。
- **关键结果 / 消融** · 摘要报告成功率高 4.6 至 11.2 点，难题时长最多减约 37%。
- **适用条件 / 局限** · 需要规格可形式化且验证环境可执行。

**可复用机制** · 在规划阶段明确不变量和接口证明义务，避免最后补证明时改主体。

<a id="paper-151816"></a>

## P$^3$-VLM: A Point-based Alternative for Grounded 3D Vision-Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151816) · [作者来源](https://openreview.net/forum?id=XlVqVpPeMI)

- **问题 / 瓶颈** · 尺寸和形状坐标本身能猜类别。
- **核心创新 / 方法** · 将单点替代包围盒，并为点条件设计任务、位置和上下文路径。
- **Baseline** · 盲 LLM、其他 3D VLM 与框提示。
- **Benchmark** · ScanNet Nr3D、位置字幕和三维 QA。
- **关键结果 / 消融** · 盲模型从 36.4% 至 18.0%；点方案位置字幕报告 52.1%。
- **适用条件 / 局限** · 单点会增加多对象消歧需求。

**可复用机制** · 评测提示只提供任务必要定位信号，以盲对照验证视觉证据确有增量。

<a id="paper-149491"></a>

## PAAC: Privacy-Aware Agentic Device-Cloud Collaboration

[官方论文页](https://neurips.cc/virtual/2026/poster/149491) · [作者来源](https://openreview.net/forum?id=pkgQ4KB4Se)

- **问题 / 瓶颈** · 算力分割不能自动保护用户数据。
- **核心创新 / 方法** · 云端只操作有类型占位符，设备端用确定性登记复原及执行。
- **Baseline** · 设备级与云级的私有代理。
- **Benchmark** · 三项严格隐私任务及 17 额外任务。
- **关键结果 / 消融** · 摘要报告准确改善 15% 至 36%，泄漏降约 2 至 6 倍。
- **适用条件 / 局限** · 占位符仍可能透露类型，敏感检测误差需审计。

**可复用机制** · 将隐私边界明确到数据字段与可执行动作，验证云端不能直接读取原值。

<a id="paper-154157"></a>

## PAC-Bayesian Bounds for Learning Partially Observed Stochastic Linear Time-Invariant State-Space Systems with Inputs and Sub-Gaussian Noise

[官方论文页](https://neurips.cc/virtual/2026/poster/154157) · [作者来源](https://openreview.net/forum?id=FpjDuXISKf)

- **问题 / 瓶颈** · 训练误差小不代表有限数据下两类误差都小。
- **核心创新 / 方法** · 以 PAC-Bayes 从经验误差推导预测风险，进一步联系参数估计。
- **Baseline** · 经验训练误差和不同辨识方法。
- **Benchmark** · 输入驱动的随机线性时不变状态空间；次高斯噪声。
- **关键结果 / 消融** · 摘要给出适用于多辨识算法的有限样本界。
- **适用条件 / 局限** · 依赖线性时不变和噪声假设。

**可复用机制** · 将对部署的预测质量和参数可恢复程度拆成两项测试。

<a id="paper-148975"></a>

## PACE: A Proxy for Agentic Capability Evaluation

[官方论文页](https://neurips.cc/virtual/2026/poster/148975) · [作者来源](https://openreview.net/forum?id=tkOFdQaXLa)

- **问题 / 瓶颈** · 全流程耗资，简单单技能总分又难预测。
- **核心创新 / 方法** · 结合目标局部与全局有效题目，拟合代理总体得分。
- **Baseline** · 完整代理任务及一般非代理基准分。
- **Benchmark** · 14 模型、四代理基准、19 原子集合。
- **关键结果 / 消融** · 摘要报告留一 MAE 低于 4%、排序相关超过 0.80，而花费远低于 1%。
- **适用条件 / 局限** · 新模型家族与新工作流仍需完整评测。

**可复用机制** · 用低价评分筛候选并为最终模型补全真实执行测试。

<a id="paper-149141"></a>

## PACE-dLLM: Elastic Block Decoding via Confidence Cliff Estimation for Diffusion Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149141) · [作者来源](https://openreview.net/forum?id=sWWqM0EZOQ)

- **问题 / 瓶颈** · 固定块长同时控制可见距离和提交粒度。
- **核心创新 / 方法** · 拟合当前窗口置信曲线的陡降区，由饱和点推下一步窗口，另用阈值提交。
- **Baseline** · 固定块解码及间接加速启发式。
- **Benchmark** · LLaDA、Dream 系列的扩散解码；时延与质量。
- **关键结果 / 消融** · 摘要将置信曲线作为可随上下文变化的窗口证据。
- **适用条件 / 局限** · 曲线非单峰或无明显陡降时需额外验证。

**可复用机制** · 对相同提交量扫描可见窗口，分开管理预测算力和出错代价。

<a id="paper-149179"></a>

## PACE: Partial-state Amortized Constraint Editing for Neural Combinatorial Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/149179) · [作者来源](https://openreview.net/forum?id=sJ8pDLLENR)

- **问题 / 瓶颈** · 热图及部分预测未必是可继续的解。
- **核心创新 / 方法** · 从当前可行状态排序编辑，只应用保持可扩展的操作，并提供可行补全。
- **Baseline** · 逐步构造与全量解修订。
- **Benchmark** · 路由及图组合优化，含测试时预算扩展。
- **关键结果 / 消融** · 摘要提出统一可行状态、编辑及闭合机制。
- **适用条件 / 局限** · 有效性依赖能够核验可扩展性，任务级闭合成本需查。

**可复用机制** · 训练和搜索沿用同一状态和约束，避免后处理修复不合规候选。

<a id="paper-149859"></a>

## PACE: Phase-Aware Chunk Execution for Robot Policies with Action Chunking

[官方论文页](https://neurips.cc/virtual/2026/poster/149859) · [作者来源](https://openreview.net/forum?id=mjYg599A94)

- **问题 / 瓶颈** · 固定执行长度跨任务不可靠，频繁重规划也破坏连续。
- **核心创新 / 方法** · 在预测动作块的速度序列找低速相位作为候选刷新点。
- **Baseline** · 固定长度执行。
- **Benchmark** · RoboTwin2.0 的 50 个任务。
- **关键结果 / 消融** · 最强固定长度平均 57.8%，相位法 64.2%。
- **适用条件 / 局限** · 低速未必代表相位边界，真实机器人及高速接触需核实。

**可复用机制** · 用同一策略比较调度规则，按重规划频率和路径连续性验收。

<a id="paper-149213"></a>

## Pacing Branch Parallelism in LLM Serving

[官方论文页](https://neurips.cc/virtual/2026/poster/149213) · [作者来源](https://openreview.net/forum?id=s3hkn23fkN)

- **问题 / 瓶颈** · 过早开分支会拖慢同批串行工作，固定上限可能浪费空闲吞吐。
- **核心创新 / 方法** · 逐步估计分支额外开销，对照当前批的剩余预算决定进入。
- **Baseline** · 贪心分支接纳和固定宽度。
- **Benchmark** · Qwen3-32B 服务，变动批组成和上下文。
- **关键结果 / 消融** · 摘要给出按步调宽的可行机制，分支共享前缀。
- **适用条件 / 局限** · 时延估计随硬件和负载变动，尾时延待查。

**可复用机制** · 测分支对同批任务的外部开销，再决定并行度而非套固定上限。

<a id="paper-155276"></a>

## PACO: Partial-order-Augmented Continuous Optimization for Differentiable Causal Discovery

[官方论文页](https://neurips.cc/virtual/2026/poster/155276) · [作者来源](https://openreview.net/forum?id=6snQ8zlSKn)

- **问题 / 瓶颈** · 逐链枚举导致代价随最大路径数量增长。
- **核心创新 / 方法** · 用偏序严格传递闭包掩码覆盖矩阵指数，在同一块指数计算约束和伴随梯度。
- **Baseline** · 逐路径检测的连续结构学习。
- **Benchmark** · 多链先验的 DAG 学习，约束与运行成本。
- **关键结果 / 消融** · 方法的主要矩阵计算不依赖最大路径枚举。
- **适用条件 / 局限** · 错误偏序和大维矩阵指数下的权衡待查。

**可复用机制** · 把结构先验集中编译成可微可达运算，避免重复逐链求导。

<a id="paper-155512"></a>

## PAC Reasoning: Controlling the Performance Loss for Efficient Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/155512) · [作者来源](https://openreview.net/forum?id=52BT1Jih6O)

- **问题 / 瓶颈** · 常见门控只报告速度和事后错误，缺少事前风险界。
- **核心创新 / 方法** · 校准从思考切换到非思考的损失上置信限。
- **Baseline** · 总思考及无统计保证的动态切换。
- **Benchmark** · 推理基准，测试计算节省和目标容忍。
- **关键结果 / 消融** · 理论给出分布无关的性能损失控制，摘要报告实测节省。
- **适用条件 / 局限** · 覆盖范围依赖校准样本与线上任务分布。

**可复用机制** · 把误降级成本设成独立控制量，再在该约束内追求效率。

<a id="paper-155370"></a>

## PAIR-CI: Calibrated Conditional Independence Testing for Causal Discovery with Incomplete Data

[官方论文页](https://neurips.cc/virtual/2026/poster/155370) · [作者来源](https://openreview.net/forum?id=699aXIZ0uv)

- **问题 / 瓶颈** · 即便一致检验也可能因填补引入伪关联而失去校准。
- **核心创新 / 方法** · 配对置换比较交叉验证损失，并估计多重补全和交叉验证的联合方差。
- **Baseline** · 先补再测的常规 CI。
- **Benchmark** · 非随机缺失模拟，假阳性和检验校准。
- **关键结果 / 消融** · 常规假阳性约 28–45%，摘要报告配对法低于名义水平。
- **适用条件 / 局限** · 共享误差能否抵消依赖设定，实际数据和缺失机制待查。

**可复用机制** · 按配对构造让两组模型面对同一观测误差，再测功效是否受影响。

<a id="paper-154087"></a>

## Paloma: Phase-Conditioned Residual Modulation for Time Series Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/154087) · [作者来源](https://openreview.net/forum?id=GJqifj1exB)

- **问题 / 瓶颈** · 去周期后的残差未必无结构。
- **核心创新 / 方法** · 按相位旋转特征方向并缩放幅度。
- **Baseline** · 未调制残差的预测骨干。
- **Benchmark** · 十二个预测数据集及多个骨干。
- **关键结果 / 消融** · 摘要称模块对多骨干有效。
- **适用条件 / 局限** · 需可靠相位，节律变化时待验。

**可复用机制** · 对照无相位、仅幅值和同时调制。

<a id="paper-150774"></a>

## PaLoRA: Paced Low-Rank Adaptation for Continual Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/150774) · [作者来源](https://openreview.net/forum?id=fU1XY23snF)

- **问题 / 瓶颈** · 定向投影在有限精度有泄漏，固定小步仍可积累遗忘。
- **核心创新 / 方法** · 截断 SVD 压缩历史、做零空间投影并按秩调步。
- **Baseline** · 固定低学习率和既有持续学习。
- **Benchmark** · 50 任务 ImageNet-A 和 ImageNet-R。
- **关键结果 / 消融** · 两类长序列评测约多 4% 准确。
- **适用条件 / 局限** · 有效秩估计和有限精度条件待核。

**可复用机制** · 在长任务流记录泄漏、有效秩与新旧任务折中。

<a id="paper-155815"></a>

## PAMod: Modeling Cyclical Shifts via Phase-Amplitude Modulation for Non-stationary Time Series Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/155815) · [作者来源](https://openreview.net/forum?id=2h1BtfsPus)

- **问题 / 瓶颈** · RevIN 假定观测窗和未来分布一致。
- **核心创新 / 方法** · 周期特征分别调均值和尺度，在归一空间实现动态反变换。
- **Baseline** · 标准 RevIN 和各预测骨干。
- **Benchmark** · 十二真实时序，含插件迁移。
- **关键结果 / 消融** · 摘要报告性能提高且成本较少。
- **适用条件 / 局限** · 与 Paloma 残差相位机制相近，实证区别需全文核。

**可复用机制** · 单测均值漂移与方差漂移，避免只看综合 MSE。

<a id="paper-153505"></a>

## PANDA: Prior-guided Attentional Dual-path Architecture

[官方论文页](https://neurips.cc/virtual/2026/poster/153505) · [作者来源](https://openreview.net/forum?id=Kq4o9psxtB)

- **问题 / 瓶颈** · 归一化使多个有效节点必须竞争。
- **核心创新 / 方法** · 主路径混合结构先验和注意，辅助路径以不归一权重发送。
- **Baseline** · 四个空间或谱超图模型。
- **Benchmark** · 八个真实基准，含有向无向。
- **关键结果 / 消融** · 平均提升 5.18 个百分点。
- **适用条件 / 局限** · 非归一支路可能受节点数影响。

**可复用机制** · 按超边度数分组消融辅助支路。

<a id="paper-148290"></a>

## Pandora's AI Model Routing Box: Efficient Allocation with Costly Value Estimation

[官方论文页](https://neurips.cc/virtual/2026/poster/148290) · [作者来源](https://openreview.net/forum?id=yxwL9oTlWU)

- **问题 / 瓶颈** · 昂贵估计无须服务所有查询。
- **核心创新 / 方法** · 用高斯值信号下的检查价值决定是否升级评审。
- **Baseline** · 仅廉价路由与穷尽昂贵估计。
- **Benchmark** · 多模型、检索与可变推理预算三领域。
- **关键结果 / 消融** · 匹配全估计的质量，明显减少昂贵查询。
- **适用条件 / 局限** · 高斯假设与方差校准依赖。

**可复用机制** · 在同预算画评审调用频率和最终质量前沿。

<a id="paper-154817"></a>

## Pan-FM: A Pan-Organ Foundation Model with Saliency-Guided Masking for Missing Robustness

[官方论文页](https://neurips.cc/virtual/2026/poster/154817) · [作者来源](https://openreview.net/forum?id=AjS1p0GxuG)

- **问题 / 瓶颈** · 随机遮盖未必消除始终依赖某一器官。
- **核心创新 / 方法** · 按注意显著性遮盖支配输入并做自蒸馏。
- **Baseline** · 单器官与普通多器官方法。
- **Benchmark** · UK Biobank、七器官以及常见缺失。
- **关键结果 / 消融** · 摘要称分类与缺失健壮性提高。
- **适用条件 / 局限** · 不能外推临床；注意不一定量化重要性。

**可复用机制** · 按不同缺失模式与实测必要性检查结果。

<a id="paper-152142"></a>

## Panoptic Saliency Ranking

[官方论文页](https://neurips.cc/virtual/2026/poster/152142) · [作者来源](https://openreview.net/forum?id=VCP5mqmgK9)

- **问题 / 瓶颈** · 只排序主显著物漏掉其他实体关系。
- **核心创新 / 方法** · 将隐式注意矩阵转为显式关系，由关系做全场景排序。
- **Baseline** · 既有显著对象排序。
- **Benchmark** · PSR18K 及三套普通排序基准。
- **关键结果 / 消融** · 摘要称更快更准，参数更少。
- **适用条件 / 局限** · 需确认注意边的关系保真。

**可复用机制** · 同输入预算分别测排序与边准确。

<a id="paper-150762"></a>

## Panoptic Scene Program Diffusion Transformer

[官方论文页](https://neurips.cc/virtual/2026/poster/150762) · [作者来源](https://openreview.net/forum?id=fagdsZ9hps)

- **问题 / 瓶颈** · 平铺提示难保持实例、属性所属及角色关系。
- **核心创新 / 方法** · 双流联合去噪图像和全景程序，并用视觉定位与循环一致监督。
- **Baseline** · 匹配设置的平铺文本模型。
- **Benchmark** · GenEval 2、SANEval-Simple、PSG-Score、DetailMaster。
- **关键结果 / 消融** · 计数、属性绑定和对象角色更明显改善。
- **适用条件 / 局限** · 依赖程序及视觉对齐质量。

**可复用机制** · 同时对照外部固定程序与共同生成，并按程序错误率分层。

<a id="paper-148684"></a>

## PanoWorld: Geometry-Consistent Panoramic Video World Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/148684) · [作者来源](https://openreview.net/forum?id=vq6RcMt70J)

- **问题 / 瓶颈** · 球面观感自然仍可能几何断裂。
- **核心创新 / 方法** · 在透视底座上加全景深度与三维跟踪位置的损失，并调整球面编码。
- **Baseline** · 普通全景视频生成。
- **Benchmark** · PanoGeo 的真实和合成全景，深度、轨迹与观感。
- **关键结果 / 消融** · 摘要报几何改善，观感具竞争力。
- **适用条件 / 局限** · 伪深度及跟踪偏差限制。

**可复用机制** · 在接缝、近深度变化和快速相机运动分组测三维一致。

<a id="paper-150495"></a>

## PanoWorld: Towards Spatial Supersensing in 360◦ Panorama World

[官方论文页](https://neurips.cc/virtual/2026/poster/150495) · [作者来源](https://openreview.net/forum?id=hgAZq94Mbr)

- **问题 / 瓶颈** · 分割透视图会使参考系转换和接缝隐式化。
- **核心创新 / 方法** · 以球面注意和几何语言配对训练加入原生空间信息。
- **Baseline** · 多透视切片与开闭源模型。
- **Benchmark** · PanoSpace-Bench、H*Bench、R2R-CE。
- **关键结果 / 消融** · 摘要报告一致改善。
- **适用条件 / 局限** · 数据和注意的独立效果待核。

**可复用机制** · 在接缝及偏航变化分别对照球面与多视角切片。

<a id="paper-154867"></a>

## PaperLens: How Predictable Is Paper Acceptance?

[官方论文页](https://neurips.cc/virtual/2026/poster/154867) · [作者来源](https://openreview.net/forum?id=AJ2gyvFOF9)

- **问题 / 瓶颈** · 二分类可能利用匿名破坏和先验分布。
- **核心创新 / 方法** · 平衡数据并删除泄漏线索，比较视觉文档和纯 Markdown。
- **Baseline** · 前沿提示、评审训练及不同模型规模。
- **Benchmark** · OpenReview 与 arXiv 材料的分类排序。
- **关键结果 / 消融** · 视觉更强，3B 到 14B 增益较小。
- **适用条件 / 局限** · 录用只代表流程结果，不能作为科研质量。

**可复用机制** · 测试排版与正文各自增益并保持作者身份不泄漏。

<a id="paper-149215"></a>

## PAPO-VLA: Planning-Aware Policy Optimization for Vision-Language-Action Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149215) · [作者来源](https://openreview.net/forum?id=s3ZEtW3nVE)

- **问题 / 瓶颈** · 整条轨迹同权难找决策点。
- **核心创新 / 方法** · 由动作变化和结果筛规划点，再以充分与必要的对照调优势。
- **Baseline** · 模仿及轨迹级强化学习。
- **Benchmark** · 多个操作基准，名称待核。
- **关键结果 / 消融** · 摘要报告任务表现提升。
- **适用条件 / 局限** · 反事实动作估计和额外交互待核。

**可复用机制** · 仅在低风险仿真同预算对比决策加权和均匀更新。

<a id="paper-151484"></a>

## Parabolic Position Encoding: Vision-Centric, Principled, Extrapolatable, General

[官方论文页](https://neurips.cc/virtual/2026/poster/151484) · [作者来源](https://openreview.net/forum?id=aHGX6FOsYg)

- **问题 / 瓶颈** · 一维编码推广未处理多维方向。
- **核心创新 / 方法** · 以抛物项刻画几何并提供旋转不变变体。
- **Baseline** · 现有视觉位置编码。
- **Benchmark** · ImageNet-1K 外推，另八集四模态。
- **关键结果 / 消融** · 外推最多比次优高 10.5%，七集匹配或超过。
- **适用条件 / 局限** · 旋转不变会否丢方向信息需按任务测。

**可复用机制** · 固定骨干在视角、尺度及长度外推分别验收。

<a id="paper-150825"></a>

## Paradoxes of Game Theoretic Equilibria and Price of Anarchy

[官方论文页](https://neurips.cc/virtual/2026/poster/150825) · [作者来源](https://openreview.net/forum?id=f1cGnSFoPg)

- **问题 / 瓶颈** · 理论最坏均衡可在自然动态中为排斥点。
- **核心创新 / 方法** · 构造势博弈、低遗憾及拥塞反例，比较向量场与平均。
- **Baseline** · Nash、CE、CCE 和无政府代价。
- **Benchmark** · 静态与动态理论。
- **关键结果 / 消融** · 低交换遗憾也可出现混沌，静态边界无法描述轨迹。
- **适用条件 / 局限** · 依赖选定游戏与动态。

**可复用机制** · 在仿真分别记录盆地、周期和时均效用。

<a id="paper-156748"></a>

## Paradoxical noise preference in RNNs

[官方论文页](https://neurips.cc/virtual/2026/poster/156748) · [作者来源](https://neurips.cc/virtual/2026/poster/156748)

- **问题 / 瓶颈** · 内部噪声可改变学到的随机固定点。
- **核心创新 / 方法** · 对照同方差两种注入和不同测试噪声，分析非线性附近偏置。
- **Baseline** · 训练后无噪声、外部注入。
- **Benchmark** · 函数逼近、迷宫、路径积分和多任务。
- **关键结果 / 消融** · 内部注入时常在非零噪声效果最好，外部趋势相反。
- **适用条件 / 局限** · 依赖训练噪强和激活。

**可复用机制** · 同时验无噪推理与训练噪，不假定关闭随机项必有利。

<a id="paper-155812"></a>

## ParaLin: Accelerating Parallel Diffusion Integrator via Intrinsic Partially Linear Structure

[官方论文页](https://neurips.cc/virtual/2026/poster/155812) · [作者来源](https://openreview.net/forum?id=2iMSq9oirM)

- **问题 / 瓶颈** · 时序积分限制并行。
- **核心创新 / 方法** · 重写为部分线性方程组并即时更新，根对应原积分轨迹。
- **Baseline** · 顺序 DDPM 及 ParaSolver。
- **Benchmark** · Flux、Stable Diffusion 与多种流模型，25–50 步及长步。
- **关键结果 / 消融** · 实用步数快 2.7–3.9 倍，单 GPU 比并行参考约 2.5 倍。
- **适用条件 / 局限** · 硬件、步数和显存依赖。

**可复用机制** · 在相同轨迹残差下测速度，分开短步和长期步数收益。

<a id="paper-150574"></a>

## Parallel Broyden methods for efficiently evaluating nonlinear state space models

[官方论文页](https://neurips.cc/virtual/2026/poster/150574) · [作者来源](https://openreview.net/forum?id=h9gPX15hwW)

- **问题 / 瓶颈** · 对角近似漏耦合，完整 Jacobian 昂贵。
- **核心创新 / 方法** · 由割线构建对角加低秩 Broyden 块，并压秩以并行扫描。
- **Baseline** · 精确 Newton 和对角准 Newton。
- **Benchmark** · 低秩 RNN、并行 MCMC 与扩散。
- **关键结果 / 消融** · 摘要报告迭代减少、速度更快。
- **适用条件 / 局限** · 耦合非低秩时误差与成本需查。

**可复用机制** · 先诊断耦合谱，比较适应秩与逐步评估。

<a id="paper-153482"></a>

## Parallel Computation Algorithms and Convergence Guarantees for Mean-Field Langevin Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/153482) · [作者来源](https://openreview.net/forum?id=L2cmR58g9Y)

- **问题 / 瓶颈** · 仅看总更新不能说明延迟下界。
- **核心创新 / 方法** · 在 log-Sobolev 条件下分析有限粒子与极限的并行收敛。
- **Baseline** · 顺序平均场动力。
- **Benchmark** · 熵正则优化的理论。
- **关键结果 / 消融** · 给两种设置的多对数顺序轮保证。
- **适用条件 / 局限** · 依赖函数不等式，经验及总并行量待核。

**可复用机制** · 在同误差记录并发数与顺序轮，避免只报墙钟。

<a id="paper-151458"></a>

## Parallel Fixed-Point Spiking Neurons for Efficient Training of Spiking Neural Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/151458) · [作者来源](https://openreview.net/forum?id=aUNVuXFPLe)

- **问题 / 瓶颈** · 漏积分逐点循环限制设备并行。
- **核心创新 / 方法** · 以迭代固定点解耦时步，并学习传播算子。
- **Baseline** · 顺序展开与其他并行方法。
- **Benchmark** · 事件识别、图像序列、语音和时序。
- **关键结果 / 消融** · 摘要报告效率改善且精度维持或更好。
- **适用条件 / 局限** · 需验证固定点步数及收敛。

**可复用机制** · 用跨时步的并行信息传播代替显式逐次依赖。

<a id="paper-148849"></a>

## Parallel-in-Time Training of Recurrent Neural Networks for Dynamical Systems Reconstruction

[官方论文页](https://neurips.cc/virtual/2026/poster/148849) · [作者来源](https://openreview.net/forum?id=uhe6KW6jyO)

- **问题 / 瓶颈** · 线性状态扫描有效但未必表示非线性演化。
- **核心创新 / 方法** · 将广义教师强制加入 DEER 训练。
- **Baseline** · 线性状态空间与一般 DEER。
- **Benchmark** · 动力系统重建，最长测试超过万步。
- **关键结果 / 消融** · 长轨迹在含慢过程时有明显收益。
- **适用条件 / 局限** · 时间范围只对所需慢尺度有用。

**可复用机制** · 先估数据的动力时间尺度，再选可表达的并行扫描，不能仅按序列长度选模型。

<a id="paper-151152"></a>

## Parallel-in-Time Variational Inference for Latent Stochastic Differential Equations

[官方论文页](https://neurips.cc/virtual/2026/poster/151152) · [作者来源](https://openreview.net/forum?id=ceFLsj8po8)

- **问题 / 瓶颈** · 顺序仿真误差累乘且训练慢。
- **核心创新 / 方法** · 用非马尔可夫序列网络并行预测各步状态增量。
- **Baseline** · 序贯变分采样。
- **Benchmark** · 复杂度测试、长期非线性预测及高维序列。
- **关键结果 / 消融** · 摘要报告并行跨度从线性到对数，误差传播变加性。
- **适用条件 / 局限** · 模型后验及分数噪声的适配条件需核对。

**可复用机制** · 对需累计的结果学习可并行的增量接口，再用并行扫描求轨迹。

<a id="paper-139064"></a>

## ParallelKernelBench: Can LLMs Write Fast Multi-GPU Kernels?

[官方论文页](https://neurips.cc/virtual/2026/poster/139064) · [作者来源](https://openreview.net/forum?id=nQ2uJYyc4s)

- **问题 / 瓶颈** · 单卡 roofline 掩盖通信是否限制吞吐。
- **核心创新 / 方法** · 按并行类型组织任务，并对正确结果做通信感知 roofline。
- **Baseline** · 不重叠的 PyTorch 加 NCCL。
- **Benchmark** · PKB 87 任务。
- **关键结果 / 消融** · 首次正确至 32%，仅 25% 可超不重叠基线。
- **适用条件 / 局限** · 所测平台和实现有限。

**可复用机制** · 先核对通信是否真并行，再比较内核算术性能。

<a id="paper-154505"></a>

## Parallel Rollout Approximation for Pixel-Space Autoregressive Image Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/154505) · [作者来源](https://openreview.net/forum?id=D55NaBnwtO)

- **问题 / 瓶颈** · 训练看真值，生成读自身误差，逐步采样训练昂贵。
- **核心创新 / 方法** · 用共享一步去噪与可学习小中间态并行构造训练输入。
- **Baseline** · 既有像素自回归和潜空间模型。
- **Benchmark** · ImageNet-1K 256²，FID 与分类探针。
- **关键结果 / 消融** · 135M 模型 FID 2.58，对前法 3.60。
- **适用条件 / 局限** · 草案是否覆盖长程复合错误需另验。

**可复用机制** · 训练时近似部署输入分布，而不把昂贵真实逐步生成放进每个批次。

<a id="paper-149580"></a>

## Parameter Exploration for RLVR via Variational Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149580) · [作者来源](https://openreview.net/forum?id=p3hX7ae4x4)

- **问题 / 瓶颈** · 单个扰动模型容易造成组内同质样本。
- **核心创新 / 方法** · 用近似后验采多个参数，对全部 rollout 共同计算组优势。
- **Baseline** · 单参数样本与标准组优化。
- **Benchmark** · 多个 LLM 和数学推理，含 AIME。
- **关键结果 / 消融** · 摘要报告多样本和跨组优势较优。
- **适用条件 / 局限** · 要核对采样尺度与额外算力。

**可复用机制** · 在固定展开数下将多样性同时分配给动作噪声和参数采样。

<a id="paper-155237"></a>

## Parameterized Complexity of Stationarity Testing for Piecewise-Affine Functions and Shallow CNN Losses

[官方论文页](https://neurips.cc/virtual/2026/poster/155237) · [作者来源](https://openreview.net/forum?id=7CznRls7QK)

- **问题 / 瓶颈** · 连续分段仿射不能保证高效检验。
- **核心创新 / 方法** · 区分固定维的可解面和参数复杂性硬面，并延伸至浅 CNN。
- **Baseline** · 已有最坏情况不可解结果。
- **Benchmark** · 近似驻点与局部极小的理论。
- **关键结果 / 消融** · 部分有 XP 算法；更广类别仍有硬度界。
- **适用条件 / 局限** · 依赖编码、维数及采用的驻点定义。

**可复用机制** · 优化验收别把各驻点概念视为相同成本，先选可验证的近似目标。

<a id="paper-149296"></a>

## Parameterized Stripe Attention for Efficient Video Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/149296) · [作者来源](https://openreview.net/forum?id=rJkErQ4C6o)

- **问题 / 瓶颈** · 固定模式不够灵活，运行时搜索影响内核。
- **核心创新 / 方法** · 统一参数化周期斜带，离线在误差阈值下最大化稀疏。
- **Baseline** · FlashAttention-3。
- **Benchmark** · HunyuanVideo、Wan 2.1。
- **关键结果 / 消融** · 端到端快 1.57 倍和 1.37 倍。
- **适用条件 / 局限** · 质量妥协及跨分辨率稳定性需验收。

**可复用机制** · 将可解释稀疏模式压成同一内核支持的参数，而非运行时生成任意掩码。

<a id="paper-150568"></a>

## Parameter symmetries determine representational geometry in overparameterized nonlinear networks

[官方论文页](https://neurips.cc/virtual/2026/poster/150568) · [作者来源](https://openreview.net/forum?id=hBTMHDGZsj)

- **问题 / 瓶颈** · 完全相同计算可对应截然不同几何。
- **核心创新 / 方法** · 将标准对称分成加法、复制与缩放，按计算重要度重权特征。
- **Baseline** · 模型函数与未经校正的表示比较。
- **Benchmark** · 过参数非线性网的理论分析。
- **关键结果 / 消融** · 摘要说明函数等价模型可几何极不相似。
- **适用条件 / 局限** · 依赖所分析对称族；重要度选择需验证。

**可复用机制** · 设计解释指标尽量对不改变行为的参数重排不变。

<a id="paper-152318"></a>

## Parametric Meets Non-parametric: Bridging Dual Prediction Spaces for Semi-supervised Medical Image Segmentation

[官方论文页](https://neurips.cc/virtual/2026/poster/152318) · [作者来源](https://openreview.net/forum?id=Txi4PjNfS3)

- **问题 / 瓶颈** · 网络定位细但噪声敏感，类原型稳但边界粗。
- **核心创新 / 方法** · 用体素置信选择网络和原型输出，并以原型熵与跨空间对齐联训。
- **Baseline** · 单路伪标签的半监督方法。
- **Benchmark** · 多医学分割及少标签。
- **关键结果 / 消融** · 摘要报告一致改善。
- **适用条件 / 局限** · 两路共同误判仍可能强化错误。

**可复用机制** · 让共享训练信号来自互补高可信分支，并将双低置信样本留作待审。

<a id="paper-150049"></a>

## ParaPC-FM: Accelerating Parallel Sampling via Principled Initialization

[官方论文页](https://neurips.cc/virtual/2026/poster/150049) · [作者来源](https://openreview.net/forum?id=l8sEnyVlRf)

- **问题 / 瓶颈** · 差初值使并行修正重复调用模型。
- **核心创新 / 方法** · 将截断预测器与高阶校正共同写成固定点。
- **Baseline** · ParaDiGMS 风格及 ParaTAA。
- **Benchmark** · FLUX.1-dev、SD3、SD3.5 的时延及质量。
- **关键结果 / 消融** · FLUX 百步最高快 1.49 倍，质量近乎不变。
- **适用条件 / 局限** · 收益依赖步数与并发硬件。

**可复用机制** · 先提高可免费复用的初值精度，而非增加并行修正次数。

<a id="paper-149518"></a>

## Parasite Features: Causal Abstraction Through Spurious Pathways

[官方论文页](https://neurips.cc/virtual/2026/poster/149518) · [作者来源](https://openreview.net/forum?id=pXYWXZE3QV)

- **问题 / 瓶颈** · 替换特征能改变结果也可能是把两个独立方向人工连起来。
- **核心创新 / 方法** · 构造可判输入和可操纵输出但不相连的控制，测试分布式对齐。
- **Baseline** · 传统因果抽象检验。
- **Benchmark** · 句法一致与两位数加法。
- **关键结果 / 消融** · 摘要报告线性对齐可发现寄生特征。
- **适用条件 / 局限** · 不否定所有因果抽象，适用范围需具体。

**可复用机制** · 对任何机制解释检查干预是否只在验证时创造了未自然使用的通路。

<a id="paper-151385"></a>

## ParaVT: Taming the Tool Prior Paradox for Parallel Tool Use in Agentic Video Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151385) · [作者来源](https://openreview.net/forum?id=b10WlhqFMr)

- **问题 / 瓶颈** · 引导先验既帮助探索，又可能造成格式崩溃及不调用捷径。
- **核心创新 / 方法** · 在易崩的结构词元奖励正确格式，通过每问帧预算变化区分调用价值。
- **Baseline** · 串行工具、普通 GRPO、弱先验模型。
- **Benchmark** · 六项长视频理解。
- **关键结果 / 消融** · 平均提升 7.9%，训练格式合规从 0.13 至 0.64。
- **适用条件 / 局限** · 受工具协议、视觉覆盖及基础先验约束。

**可复用机制** · 工具奖励在局部语法和任务信息收益分开验收，不用一个结局分统管。

<a id="paper-151968"></a>

## PARE: Pruning and Adaptive Routing for Efficient Video Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/151968) · [作者来源](https://openreview.net/forum?id=WSWLqEZjZV)

- **问题 / 瓶颈** · 统一剪枝易先去掉时间头，固定块深度浪费计算。
- **核心创新 / 方法** · 按时空注意职责裁宽，以时间和内容条件的轻路由裁深。
- **Baseline** · 固定宽深压缩及步数蒸馏。
- **Benchmark** · Wan2.1-14B 图转视频和文本转视频，VBench。
- **关键结果 / 消融** · 摘要报告每步开销下降且质量保持。
- **适用条件 / 局限** · 需要恢复蒸馏与测试调度支持。

**可复用机制** · 容量预算按阶段和输入变动，剪除前验证部件承担的是空间还是时间职责。

<a id="paper-151618"></a>

## Pareto DNN Verification: Fast for Most Queries

[官方论文页](https://neurips.cc/virtual/2026/poster/151618) · [作者来源](https://openreview.net/forum?id=ZDDAP6WLxi)

- **问题 / 瓶颈** · 每次完整求解深网容易超时。
- **核心创新 / 方法** · 先验证浅层出口，在稳定执行轨迹下用完备验证证明。
- **Baseline** · 全深度验证。
- **Benchmark** · MNIST、CIFAR，至 33M 网络。
- **关键结果 / 消融** · 约八成查询低时延，部分安全例至十倍加速。
- **适用条件 / 局限** · 出口须纳入保证，附加网络不等于原模型。

**可复用机制** · 把绝大多数简单状态与困难状态分成有明确验证边界的子问题。

<a id="paper-155972"></a>

## ParetoM$^3$: Learning on the Pareto Set under Preference Guidance via Min-Max-Min Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/155972) · [作者来源](https://openreview.net/forum?id=1ROin5KHsq)

- **问题 / 瓶颈** · 先固定加权和可能遗漏可用解。
- **核心创新 / 方法** · 用在弱 Pareto 集为零的优值构建罚问题，单循环求近驻点。
- **Baseline** · 已有偏好优化及 KKT 判据。
- **Benchmark** · 合成、分类、回归和数学推理。
- **关键结果 / 消融** · 局部条件下给非渐近近驻点和近弱 Pareto，摘要报告实证有效。
- **适用条件 / 局限** · 需罚参数、局部几何和指定偏好。

**可复用机制** · 先定义允许折中解的证书，再在其中优化个性化目标。

<a id="paper-154172"></a>

## ParetoSlider: Diffusion Models Post-Training for Continuous Reward Control

[官方论文页](https://neurips.cc/virtual/2026/poster/154172) · [作者来源](https://openreview.net/forum?id=FikEkhzT3F)

- **问题 / 瓶颈** · 固定加权使每个取舍需要一套模型。
- **核心创新 / 方法** · 以连续偏好权重条件化强化后训练的去噪过程。
- **Baseline** · 固定各权重分别训练的扩散模型。
- **Benchmark** · SD3.5、FluxKontext、LTX-2。
- **关键结果 / 消融** · 单模型匹配或超过各固定偏好模型。
- **适用条件 / 局限** · 训练权重范围之外可能失控。

**可复用机制** · 以同一服务模型验收可调前沿，而不只评价一个平均权重。

<a id="paper-155621"></a>

## PARI: Policy-Driven Active Residual Intervention for Weakly Supervised Point Cloud Segmentation

[官方论文页](https://neurips.cc/virtual/2026/poster/155621) · [作者来源](https://openreview.net/forum?id=4COCLKO8xE)

- **问题 / 瓶颈** · 被动伪标签错误不断传播，对所有点修改会伤可靠预测。
- **核心创新 / 方法** · 强化代理根据不确定度选点，抑制高可信修改并以空间语义上下文精修。
- **Baseline** · 常规弱监督、同骨干全监督。
- **Benchmark** · S3DIS、ScanNetV2。
- **关键结果 / 消融** · 摘要报告跨骨干改善，某 1% 设置超同骨干全监督。
- **适用条件 / 局限** · 依赖不确定分数和分布，不能据个别设定否定全监督。

**可复用机制** · 把何时干预和怎么修复做成两个分别验收的决定。

<a id="paper-153061"></a>

## Partially Performative Prediction

[官方论文页](https://neurips.cc/virtual/2026/poster/153061) · [作者来源](https://openreview.net/forum?id=OJ3tHPcSRq)

- **问题 / 瓶颈** · 两种变化混在一起，追踪固定均衡可能不合适。
- **核心创新 / 方法** · 将数据分布设为模型依赖及外生时变的共同响应，并定义在线稳定最优。
- **Baseline** · 只含 endogenous 变化的执行式预测。
- **Benchmark** · 理论下的重训跟踪条件。
- **关键结果 / 消融** · 摘要报告可刻画何时追踪有效。
- **适用条件 / 局限** · 实际难识别两种变化各占多少。

**可复用机制** · 在上线监控中加入与模型决策无关的漂移对照，再判断重训是否改善反馈闭环。

<a id="paper-151064"></a>

## Past as State, Present as Attention: Persistent-State Blockwise Flow Matching for Long-Horizon Co-Speech Motion Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/151064) · [作者来源](https://openreview.net/forum?id=dGHAQR4OKs)

- **问题 / 瓶颈** · 短历史易漂移，长历史开销大。
- **核心创新 / 方法** · 跨块持久状态保存风格，块内双向注意处理当前动作。
- **Baseline** · 短帧和长历史条件。
- **Benchmark** · 长时语音驱动手势生成。
- **关键结果 / 消融** · 摘要提出多块训练来保持连贯。
- **适用条件 / 局限** · 分离机制的收益待核实。

**可复用机制** · 分开测跨块风格与块内运动质量。

<a id="paper-151428"></a>

## Past, Future, All at Once: Breaking Stability-Plasticity Dilemma via Post-hoc JANUS Rectification

[官方论文页](https://neurips.cc/virtual/2026/poster/151428) · [作者来源](https://openreview.net/forum?id=amfBq5fDzv)

- **问题 / 瓶颈** · 一般参数正交不保证输出保持。
- **核心创新 / 方法** · 用 JANUS 投影和分步信赖区修正。
- **Baseline** · 常规高效微调与子空间正交。
- **Benchmark** · 旧任务保持及修正成本。
- **关键结果 / 消融** · 给出一阶保持依据。
- **适用条件 / 局限** · 依赖雅可比代表性，远距离一阶近似失效。

**可复用机制** · 同时检查修复后旧能力和新任务效果。

<a id="paper-154566"></a>

## Patch4Patch: Restoring Structural Connectivity in Patch-based Vision Encoders

[官方论文页](https://neurips.cc/virtual/2026/poster/154566) · [作者来源](https://openreview.net/forum?id=CenzhX8Go9)

- **问题 / 瓶颈** · 表格的行及坐标轴在分区处断开。
- **核心创新 / 方法** · 稀疏选锚，在分区间用双向注意并门控融合。
- **Baseline** · 常规分区和全局注意。
- **Benchmark** · 三种视觉语言骨干的表格和图表理解。
- **关键结果 / 消融** · 摘要报告性能改善。
- **适用条件 / 局限** · 锚的选择可靠性需要核实。

**可复用机制** · 固定算力后用保持语义的布局改变检验稳定。

<a id="paper-139148"></a>

## PatchBench: Measuring Collateral Damage in Activation Patching

[官方论文页](https://neurips.cc/virtual/2026/poster/139148) · [作者来源](https://openreview.net/forum?id=iGhJMl38AQ)

- **问题 / 瓶颈** · 总体通过率会掩盖连带损伤。
- **核心创新 / 方法** · 为每种已知失败布置关联良性和持出的安全测试。
- **Baseline** · 总体拒绝率与平均能力。
- **Benchmark** · 多模型修复测试，测覆盖和误拒。
- **关键结果 / 消融** · 摘要说明现有指标不足以判断选择性。
- **适用条件 / 局限** · 保护范围应按部署定义。

**可复用机制** · 用相邻良性例排除无差别抑制。

<a id="paper-152498"></a>

## Patching Up Circuit Learning on Images

[官方论文页](https://neurips.cc/virtual/2026/poster/152498) · [作者来源](https://openreview.net/forum?id=SgOj0VYeoD)

- **问题 / 瓶颈** · 联合依赖模型大且可能较难学习。
- **核心创新 / 方法** · 递归共享概率电路参数。
- **Baseline** · 独立块电路。
- **Benchmark** · 图像似然、时间和存储。
- **关键结果 / 消融** · 摘要报告竞技似然及显著节省。
- **适用条件 / 局限** · 大尺度依赖能否保留待核实。

**可复用机制** · 同时测每个表示的可训练性、依赖及资源。

<a id="paper-150775"></a>

## PatchKV: Weight Space Compensation of KV Cache

[官方论文页](https://neurips.cc/virtual/2026/poster/150775) · [作者来源](https://openreview.net/forum?id=fTgwQmKmJx)

- **问题 / 瓶颈** · 激进 KV 压缩丢失部分证据。
- **核心创新 / 方法** · 在加载时用参照查询激活做闭式岭回归，再合并上下文补丁。
- **Baseline** · 原 KV 压缩方法。
- **Benchmark** · SCBench、SQuAD、NIAH、GSM8K。
- **关键结果 / 消融** · 摘要报告改善压缩缓存性能，合并后单上下文前向成本不变。
- **适用条件 / 局限** · 多上下文并发的切换成本待核实。

**可复用机制** · 按查询次数估算一次性补偿的盈亏平衡。

<a id="paper-154882"></a>

## PATCH: Learnable Tile-Level Hybrid Sparsity for LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/154882) · [作者来源](https://openreview.net/forum?id=ABuaxVr804)

- **问题 / 瓶颈** · 任意稀疏难加速，统一 2:4 易伤效果。
- **核心创新 / 方法** · 学掩码选择每瓦片的模式。
- **Baseline** · 稠密、无结构稀疏及均匀 2:4。
- **Benchmark** · 0.5B–13B，含 A6000 上 LLaMA-2 7B。
- **关键结果 / 消融** · 实例实测加速 1.18–1.38 倍。
- **适用条件 / 局限** · 收益依赖硬件与内核。

**可复用机制** · 端到端扫稀疏率，避免只报理论乘加量。

<a id="paper-154920"></a>

## Path-independent Flow Matching for Multi-parameter Generative Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/154920) · [作者来源](https://openreview.net/forum?id=9yq2JAPSPm)

- **问题 / 瓶颈** · 独立学习各坐标轴不能保证组合一致。
- **核心创新 / 方法** · 用多参数条件概率路径做免模拟训练。
- **Baseline** · 单参数流匹配。
- **Benchmark** · 多参数输运、重心及一致性。
- **关键结果 / 消融** · 在适当条件下证明路径一致和重心近似。
- **适用条件 / 局限** · 可满足性及大维实证需查。

**可复用机制** · 用不同编辑顺序到相同端点，直接测生成差异。

<a id="paper-153514"></a>

## Pathways of Visual Information Flow in Vision-Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153514) · [作者来源](https://openreview.net/forum?id=KmqJXqbsh6)

- **问题 / 瓶颈** · 消融后仍答对可能由备用通路补偿。
- **核心创新 / 方法** · 用因果补丁、注意清除与损坏输入比较两通路。
- **Baseline** · 原前向、局部抑制和不同提示。
- **Benchmark** · 合成和自然数据，三类视觉任务。
- **关键结果 / 消融** · 通路依任务、数据和提示，消融会激活备用路径。
- **适用条件 / 局限** · 干预下可工作不等于平常使用。

**可复用机制** · 测正常前向及多路径共同干预，以免把补偿当主机制。

<a id="paper-148683"></a>

## Pattern-Based Matrix Analysis Under Permutations

[官方论文页](https://neurips.cc/virtual/2026/poster/148683) · [作者来源](https://openreview.net/forum?id=vqLCMxTvrv)

- **问题 / 瓶颈** · 带状或块对角信息可能不体现在线性秩。
- **核心创新 / 方法** · 以交替线性指派寻找行列重排，再拟合低秩残差。
- **Baseline** · 纯低秩、无重排及固定掩码。
- **Benchmark** · 合成、相关矩阵、图矩阵和语言模型注意。
- **关键结果 / 消融** · 具有严格秩分离例，实证可识别不同几何。
- **适用条件 / 局限** · 全局最优一般 NP 难，等价排列难区分。

**可复用机制** · 先匹配已知形状再查残差奇异值，避免仅报低秩拟合。

<a id="paper-152560"></a>

## PatternBloom: Empowering Agentic RAG with Externalized RL-Distilled Graph Patterns

[官方论文页](https://neurips.cc/virtual/2026/poster/152560) · [作者来源](https://openreview.net/forum?id=SDljMGVCMp)

- **问题 / 瓶颈** · 相同逻辑在不同问题中反复推导。
- **核心创新 / 方法** · 将高信息密度证据图抽象为类型化骨架，以外部索引复用。
- **Baseline** · 仅检索文段、关系或事实图。
- **Benchmark** · 域外精确匹配与不同推理深度。
- **关键结果 / 消融** · 7B 模型平均域外精确匹配高 15.0。
- **适用条件 / 局限** · 受图提取、来源可靠性与奖励选择影响。

**可复用机制** · 在公有百科题上对照内容检索与结构检索的边际收益。

<a id="paper-155647"></a>

## Pause and Reflect: Conformal Aggregation for Chain-of-Thought Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/155647) · [作者来源](https://openreview.net/forum?id=434OhnsWUQ)

- **问题 / 瓶颈** · 简单投票未量化高置信错误。
- **核心创新 / 方法** · 用加权路径分数做保形拒答，分析可分性与选择性准确。
- **Baseline** · 多数投票。
- **Benchmark** · 四任务及四个开源模型，含 GSM8K。
- **关键结果 / 消融** · GSM8K 选择性准确 90.1%，拒答少于 5%，投票 82%。
- **适用条件 / 局限** · 校准与部署分布变化影响保证。

**可复用机制** · 同时报覆盖、错误作答及条件准确。

<a id="paper-150489"></a>

## PAVE: Prefill-Conditioned Activation Editing for Hallucination Mitigation in LVLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/150489) · [作者来源](https://openreview.net/forum?id=hiYMBdcGSJ)

- **问题 / 瓶颈** · 固定干预可能抑制真实视觉证据。
- **核心创新 / 方法** · 预填充时取图像相关基底，结合离线视觉与错误子空间。
- **Baseline** · 输出端改分布及固定激活编辑。
- **Benchmark** · LLaVA-1.5-7B、Qwen-VL，CHAIR、POPE、MME。
- **关键结果 / 消融** · 摘要称幻觉下降且视觉效用保留。
- **适用条件 / 局限** · 依赖白盒访问与选定校准集。

**可复用机制** · 对同一物体改变背景检查误伤与有效抑制。

<a id="paper-151122"></a>

## Payoff-Aware Prediction of Population Game Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/151122) · [作者来源](https://openreview.net/forum?id=cphFgh3BN0)

- **问题 / 瓶颈** · 只拟合旧激励下的轨迹会把二者混为一体。
- **核心创新 / 方法** · 通过 Riemannian 动态建模，固定收益输入而学习响应结构。
- **Baseline** · 直接从轨迹拟合动态。
- **Benchmark** · 合成零和、势博弈及 YouTube Trending 多国数据。
- **关键结果 / 消融** · 保留固定收益 Nash 均衡，变化收益预测有效。
- **适用条件 / 局限** · 依赖响应共享与收益覆盖。

**可复用机制** · 按留出激励规则验多步误差及均衡位置。

<a id="paper-156012"></a>

## Payoff-Only Learning in Games via Best-Response Differential Inclusions

[官方论文页](https://neurips.cc/virtual/2026/poster/156012) · [作者来源](https://openreview.net/forum?id=1BVKDnc5HH)

- **问题 / 瓶颈** · 未知对手使最佳响应难直接估计。
- **核心创新 / 方法** · 分周期估自己的动作回报，将随机更新映射为最佳响应包含。
- **Baseline** · 全观察策略或经典无遗憾动力作为背景。
- **Benchmark** · 有限零和、势博弈和一般位置 2×2 理论。
- **关键结果 / 消融** · 指定类别末迭代收敛，减小障碍可去偏。
- **适用条件 / 局限** · 要求长期运行及特定博弈结构。

**可复用机制** · 对比末步和平均策略，分报回报估计误差。

<a id="paper-138920"></a>

## PBT-Bench: Benchmarking AI Agents on Property-Based Testing

[官方论文页](https://neurips.cc/virtual/2026/poster/138920) · [作者来源](https://openreview.net/forum?id=wota1ZN4By)

- **问题 / 瓶颈** · 通用随机测试可能漏普通逻辑错误。
- **核心创新 / 方法** · 对照通用提示与结构化属性测试框架的发现率。
- **Baseline** · 通用与结构化提示，八个模型。
- **Benchmark** · 40 个 Python 库的 100 个受控问题。
- **关键结果 / 消融** · 中等模型常提升逾 20 点，最强模型不总获益。
- **适用条件 / 局限** · 人工注入错误不代表真实分布。

**可复用机制** · 在授权合成代码检查不变量清晰度与边界覆盖，不以报错次数代替验收。

<a id="paper-139034"></a>

## PCBInnoBench: Benchmarking LLM Agents on Real-World PCB Design

[官方论文页](https://neurips.cc/virtual/2026/poster/139034) · [作者来源](https://openreview.net/forum?id=owSXOGoqx5)

- **问题 / 瓶颈** · 直接给轨迹可掩盖定位和跨工件一致性缺陷。
- **核心创新 / 方法** · 同任务有无专家引导，使用隐式验证包。
- **Baseline** · 任务目标提示与专家过程提示。
- **Benchmark** · 372 项 KiCad 任务。
- **关键结果 / 消融** · 最强引导 22.0%，无引导 7.3%。
- **适用条件 / 局限** · 限所选元件及任务，真实可靠性待验。

**可复用机制** · 在普通合成电路分别校验设计约束和跨文件一致。

<a id="paper-149018"></a>

## PCBSchemaGen: Reward-Guided LLM Code Synthesis for Printed Circuit Boards (PCB) Schematic Design with Structured Verification

[官方论文页](https://neurips.cc/virtual/2026/poster/149018) · [作者来源](https://openreview.net/forum?id=tSDSSdj4mC)

- **问题 / 瓶颈** · 一般单元测试不能确认物理接口约束。
- **核心创新 / 方法** · 以器件文档给约束，独立结构验证器反馈候选。
- **Baseline** · 相同模型的普通电路提示。
- **Benchmark** · 两套 PCB 基准，227 任务、22 域。
- **关键结果 / 消融** · 31B 在 PCBBench 平均通过 81.3%。
- **适用条件 / 局限** · 结构通过不证明真实电气性能。

**可复用机制** · 在普通低压教学电路加入外部规则与人工检查。

<a id="paper-152664"></a>

## PCDFusion: Proposal-Context-Detail Bayesian Rendering for Infrared-Visible Image Fusion

[官方论文页](https://neurips.cc/virtual/2026/poster/152664) · [作者来源](https://openreview.net/forum?id=RJBEmXTRsP)

- **问题 / 瓶颈** · 二者在低照度和热目标处失真不同。
- **核心创新 / 方法** · 以可见光锚定外观，依据可靠性分阶段融温度响应和频带细节。
- **Baseline** · 普通特征融合。
- **Benchmark** · 多个公开红外与可见融合基准。
- **关键结果 / 消融** · 摘要报告观感、目标保留与下游改善。
- **适用条件 / 局限** · 依赖可靠性估计和传感器配准。

**可复用机制** · 分照度和场景测试贡献，不用同一全局权重。

<a id="paper-138916"></a>

## PCEval: A Benchmark for Evaluating Physical Computing Capabilities of Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/138916) · [作者来源](https://openreview.net/forum?id=x2Gkudl2S5)

- **问题 / 瓶颈** · 逻辑正确不保证接线实现。
- **核心创新 / 方法** · 在模拟中自动验证程序、逻辑及物理工件。
- **Baseline** · 14 个模型和不同复杂度。
- **Benchmark** · PCEval 教育用模拟电路。
- **关键结果 / 消融** · 电路概念和编码表现好，物理布局明显较弱。
- **适用条件 / 局限** · 不能外推实体电安全。

**可复用机制** · 在教学用低风险仿真单列布局连通率及程序结果。

<a id="paper-139614"></a>

## PCFBench: How Far Can Large Vision-Language Models Go in Physics-aware Photonic Inverse Design?

[官方论文页](https://neurips.cc/virtual/2026/poster/139614) · [作者来源](https://openreview.net/forum?id=FQXg2OPgnz)

- **问题 / 瓶颈** · 能认出几何并不意味着能推断物理行为。
- **核心创新 / 方法** · 用单步属性和整流程分别度量，追踪串联误差。
- **Baseline** · 独立 VLM 和多助手流程。
- **Benchmark** · 26 项、18 种结构族及受控模拟。
- **关键结果 / 消融** · 摘要称单步感知好于整体设计，误差会级联。
- **适用条件 / 局限** · 领域与模拟误差限制。

**可复用机制** · 用普通波导仿真替换上游输入为真值，定位流程瓶颈。

<a id="paper-155714"></a>

## PDE-PFN: Prior-Data Fitted Neural PDE Solver

[官方论文页](https://neurips.cc/virtual/2026/poster/155714) · [作者来源](https://openreview.net/forum?id=3SCmcBS34S)

- **问题 / 瓶颈** · 每个新方程重训代价高，先验不必完全正确。
- **核心创新 / 方法** · 以近似 PINN 解预训练 PFN，并通过注意力做后验均值近似。
- **Baseline** · 任务专属求解器与参考基线。
- **Benchmark** · 多种二维方程和带噪先验。
- **关键结果 / 消融** · 摘要称跨式泛化、耐噪且零梯度推断。
- **适用条件 / 局限** · 先验覆盖不足的边界待核。

**可复用机制** · 按先验误差分桶，匹配预算测试是否真正减少新任务求解。

<a id="paper-149720"></a>

## PDE-SSM: A Spectral State Space Approach to Spatial Mixing in Diffusion Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/149720) · [作者来源](https://openreview.net/forum?id=nunyVp7239)

- **问题 / 瓶颈** · 全注意平方开销且缺局部偏置。
- **核心创新 / 方法** · 用可学习对流扩散反应块，在 Fourier 域计算。
- **Baseline** · 常规 DiT。
- **Benchmark** · 流匹配图像生成，质量与算力。
- **关键结果 / 消融** · 摘要称相近或更优且计算更少。
- **适用条件 / 局限** · 频域边界和细节精度需验。

**可复用机制** · 在多分辨率下比较质量和混合计算，留出非周期边界条件。

<a id="paper-149876"></a>

## PDF-HR: Pose Distance Fields for Humanoid Robots

[官方论文页](https://neurips.cc/virtual/2026/poster/149876) · [作者来源](https://openreview.net/forum?id=mYvVwJ57SZ)

- **问题 / 瓶颈** · 离散数据难直接评价一条新姿态。
- **核心创新 / 方法** · 拟合到重定向姿态集的可微距离，用于正则与评分。
- **Baseline** · 无先验和强控制基线。
- **Benchmark** · 单轨迹、一般跟踪、风格模仿及重定向。
- **关键结果 / 消融** · 摘要称各应用有改善。
- **适用条件 / 局限** · 近数据姿态不保证动力学可行或真机安全。

**可复用机制** · 以低风险仿真分测先验距离、关节限制和实际稳定性。

<a id="paper-155287"></a>

## PDHFormer: Progressive Dual-Head Transformer for Behavioral Choice Prediction

[官方论文页](https://neurips.cc/virtual/2026/poster/155287) · [作者来源](https://openreview.net/forum?id=6gQNL51pmW)

- **问题 / 瓶颈** · 并行头忽略选择间依赖。
- **核心创新 / 方法** · 共享编码器，经显式头间连接输入上游预测并配残差门。
- **Baseline** · 并行多头和深度表格模型。
- **Benchmark** · 城市移动、制造、外送等选择预测。
- **关键结果 / 消融** · 摘要称分域改善，消融支持两部件。
- **适用条件 / 局限** · 错误的上游预测可扩大偏差。

**可复用机制** · 分别用真值和预测条件估误差传播，并查逆因果次序。

<a id="paper-152869"></a>

## P-EAGLE: Parallel-Drafting EAGLE with Scalable Training

[官方论文页](https://neurips.cc/virtual/2026/poster/152869) · [作者来源](https://openreview.net/forum?id=PlnpZsdFsg)

- **问题 / 瓶颈** · 并行位置与长上下文组合使草案训练开销大。
- **核心创新 / 方法** · 把 EAGLE 改为共享隐状态的并行预测，以掩码预计算和序列分块训练。
- **Baseline** · 自回归 EAGLE-3。
- **Benchmark** · vLLM 的 GPT-OSS 120B、20B 及 Qwen3-Coder 30B。
- **关键结果 / 消融** · 相对 EAGLE-3 加速 1.10 至 1.36 倍。
- **适用条件 / 局限** · 收益依赖输出长度和多头草案命中。

**可复用机制** · 同一骨干状态支持多个草案位置，训练负担则按单条序列内部切分。

<a id="paper-152032"></a>

## PEARL: Solver-in-the-Loop Interactive Optimization Modeling from Natural Language

[官方论文页](https://neurips.cc/virtual/2026/poster/152032) · [作者来源](https://openreview.net/forum?id=W3LmdJrHns)

- **问题 / 瓶颈** · 一次生成不利用求解器发现歧义与不可行约束。
- **核心创新 / 方法** · 训练代理择时执行局部程序，读取诊断后重写并决定停止。
- **Baseline** · 单轮和工具增强的强模型。
- **Benchmark** · 多个数学优化建模基准。
- **关键结果 / 消融** · 摘要报告 4B 版本胜过所比 685B 模型。
- **适用条件 / 局限** · 可行解不保证目标语义完整。

**可复用机制** · 把求解器当中间证据源，同时用任务要求验收最终规范忠实度。

<a id="paper-154336"></a>

## PEEK: Context Map as an Orientation Cache for Long-Context LLM Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/154336) · [作者来源](https://openreview.net/forum?id=ENGBo0bbcF)

- **问题 / 瓶颈** · 每次重读昂贵，旧任务执行记录又不一定能引导新任务。
- **核心创新 / 方法** · 提炼跨问实体、组织和模式，让结构编辑与优先清理保持恒定词元预算。
- **Baseline** · ACE 等长期上下文代理。
- **Benchmark** · 文档和代码的长时推理、汇总和学习。
- **关键结果 / 消融** · 摘要报告指标改善 6.3% 至 34.0%，相较 ACE 成本低 1.7 至 5.8 倍。
- **适用条件 / 局限** · 仅有共用上下文时容易复用；内容更新要使地图失效。

**可复用机制** · 把可迁移的语料组织知识与任务记录分开存储，优先保留可帮助定位的索引。

<a id="paper-150622"></a>

## PEEK: One-Step Look-Ahead Exposure Bias Correction for Diffusion Sampling

[官方论文页](https://neurips.cc/virtual/2026/poster/150622) · [作者来源](https://openreview.net/forum?id=glLK6ZrE3S)

- **问题 / 瓶颈** · 生成噪声状态脱离训练时的真值加噪。
- **核心创新 / 方法** · 先试前进一步再评估去噪器，按离线计划选择更后面的干净预测。
- **Baseline** · 等函数调用数的 DPM-Solver++ 与 DEIS。
- **Benchmark** · CIFAR-10、CelebA-HQ、LSUN、ImageNet、MS-COCO。
- **关键结果 / 消融** · 五次均值最高降 39.3% FID；缓存减探索日程的重复计算。
- **适用条件 / 局限** · 位置搜索需对目标模型和指标验证。

**可复用机制** · 为数值更新保留一小部分预览预算，先在同计算量下验证质量增益。

<a id="paper-153191"></a>

## PEIRA: Learning Predictive Encoders through Inter-View Regressor Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/153191) · [作者来源](https://openreview.net/forum?id=NASMgUDs9w)

- **问题 / 瓶颈** · 隐含自蒸馏目标可能存在稳定塌缩。
- **核心创新 / 方法** · 以最优带正则线性回归器的迹定义显式目标。
- **Baseline** · VICReg、LeJEPA 和常见预测式自监督。
- **Benchmark** · ImageNet-1K 与 CIFAR-10。
- **关键结果 / 消融** · 理论中稳定点为非平凡最优且恢复主典型相关结构，实证有竞争力。
- **适用条件 / 局限** · 理论限所用回归和稳定性假设。

**可复用机制** · 用可分析的跨视图目标区分表示压缩、有效维度和真塌缩。

<a id="paper-139171"></a>

## Penalize to Verify: A Multi-Domain Benchmark for Trustworthy LLM Evaluation

[官方论文页](https://neurips.cc/virtual/2026/poster/139171) · [作者来源](https://openreview.net/forum?id=gaAl3PizQP)

- **问题 / 瓶颈** · 人机一致率忽略貌似正确推理的误导及过度自信。
- **核心创新 / 方法** · 由独立模型实际错误构造合理错解配对，以分层惩罚检查置信校准。
- **Baseline** · 普通准确率及不同模型作为裁判。
- **Benchmark** · PVBench，数学、代码和知识。
- **关键结果 / 消融** · 摘要报告遇误导轨迹性能显著下降，并有自评偏差。
- **适用条件 / 局限** · 弃权分与错误罚应按部署风险校验。

**可复用机制** · 把可审慎退出与能力同时评估，避免单靠猜测获得平均正确。

<a id="paper-153613"></a>

## Penalty-Based First-Order Methods for Bilevel Optimization with Minimax and Constrained Lower-Level Problems

[官方论文页](https://neurips.cc/virtual/2026/poster/153613) · [作者来源](https://openreview.net/forum?id=K4vQ9YKOxc)

- **问题 / 瓶颈** · 常用双层方法假设下层只是最小化。
- **核心创新 / 方法** · 用罚式一阶方法处理上下两层极小极大，在 Slater 条件下对偶化。
- **Baseline** · 既有受约束双层方法。
- **Benchmark** · 确定和随机情形的 KKT 复杂度。
- **关键结果 / 消融** · 确定情形近 ε^-4，较既有近 ε^-7 有改善。
- **适用条件 / 局限** · 依赖对偶条件与停机的近似要求。

**可复用机制** · 先检查对偶可行性，再用共同实现处理带约束和对抗的下层。

<a id="paper-149347"></a>

## PENEX: AdaBoost-Inspired Neural Network Regularization

[官方论文页](https://neurips.cc/virtual/2026/poster/149347) · [作者来源](https://openreview.net/forum?id=qkj6i3bJhc)

- **问题 / 瓶颈** · 直接指数目标优化不便，高错误样本也可能不稳定。
- **核心创新 / 方法** · 设计对普通一阶法可用的正则化指数目标并分析间隔。
- **Baseline** · 交叉熵及现有正则。
- **Benchmark** · 低数据视觉和语言任务。
- **关键结果 / 消融** · 摘要报告间隔增大、性能持平或更好。
- **适用条件 / 局限** · 对错标和大规模数据的效果待核实。

**可复用机制** · 选择不同损失时报告样本间隔分布，而非只比较终点准确。

<a id="paper-139229"></a>

## PepSpecBench: A Unified Evaluation Benchmark for Peptide Tandem Mass Spectrometry Prediction

[官方论文页](https://neurips.cc/virtual/2026/poster/139229) · [作者来源](https://openreview.net/forum?id=dePVHdM1Gw)

- **问题 / 瓶颈** · 随机划分可能让相近序列在两集合泄漏。
- **核心创新 / 方法** · 统一片段输出空间与处理，做物种留出及元数据变化敏感性。
- **Baseline** · 六类质谱预测模型。
- **Benchmark** · PepSpecBench 的跨物种、跨条件评估。
- **关键结果 / 消融** · 摘要报告统一协议暴露模型差异与鲁棒限制。
- **适用条件 / 局限** · 只衡量分析任务的表征与预测，不证明实际鉴定性能。

**可复用机制** · 划分按可近似记忆的骨架分组，避免把重叠模板复用当新序列泛化。

<a id="paper-154683"></a>

## Perceive, Interact, Reason: Building Tool-Augmented Visual Agents for Spatial Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/154683) · [作者来源](https://openreview.net/forum?id=BlPie2QVxk)

- **问题 / 瓶颈** · 隐式视觉表征难保细空间证据，仅问答不便验证。
- **核心创新 / 方法** · 分别提供感知及交互操作，以合成工具轨迹和组内组间策略训练。
- **Baseline** · Qwen3-8B 与相近参数方法。
- **Benchmark** · 八数据集 13 基准的地图、探测与重建。
- **关键结果 / 消融** · 摘要报告域内加 10.0%，域外加 4.4%。
- **适用条件 / 局限** · 各工具质量及收益分解待核实。

**可复用机制** · 允许模型主动核验空间假设，并单独检查它调用的是读证据还是改表示。

<a id="paper-150178"></a>

## Perceive-then-Plan: Layout-as-Policy for Monocular 3D Scene Layout Estimation

[官方论文页](https://neurips.cc/virtual/2026/poster/150178) · [作者来源](https://openreview.net/forum?id=k75EREQHoh)

- **问题 / 瓶颈** · 独立预测难处理物理相互作用和全局布局。
- **核心创新 / 方法** · 初始化场景，规划器逐步平移、旋转或缩放，以轨迹监督及偏好训练。
- **Baseline** · 端到端直接布局。
- **Benchmark** · 单图室内布局及下游编辑。
- **关键结果 / 消融** · 摘要报告物理一致和图像一致均改善。
- **适用条件 / 局限** · 场景初始化误差较大时调整动作可能不足。

**可复用机制** · 把复杂约束修正作为可回放序列，每步检验是否破坏观察一致性。

<a id="paper-150126"></a>

## PercepCap: Video Captioner with Structured Spatio-Temporal Perception

[官方论文页](https://neurips.cc/virtual/2026/poster/150126) · [作者来源](https://openreview.net/forum?id=kU5dBalt2j)

- **问题 / 瓶颈** · 只输出语言不易定位物体识别或事件时间错误。
- **核心创新 / 方法** · 将标题常见对象反向找框与时间段，联合监督轨迹及最终文本。
- **Baseline** · 标准 Qwen3-VL 字幕。
- **Benchmark** · DREAM-1K、CaReBench、VidCapBench、ShortVidBench、MotionBench。
- **关键结果 / 消融** · 摘要报告字幕及转问答评估改善。
- **适用条件 / 局限** · 从标题反向构造的数据会漏无文本提及的事件。

**可复用机制** · 让中间证据共享最终描述的对象和事件身份，便于发现文字和观察的偏差。

<a id="paper-153770"></a>

## Perception for Action in Latent World Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153770) · [作者来源](https://openreview.net/forum?id=InDOasTozM)

- **问题 / 瓶颈** · 只预测未来潜量可能淡化控制相关信息。
- **核心创新 / 方法** · 从相邻潜状态预测导致转移的动作，配合原预测训练。
- **Baseline** · 冻结编码、EMA 或复杂潜正则路线。
- **Benchmark** · 无奖励离线轨迹的二维、三维控制。
- **关键结果 / 消融** · 摘要报告可稳定端到端学习并做有竞争力的规划。
- **适用条件 / 局限** · 依赖动作在观察中可辨识，环境简单。

**可复用机制** · 用动作可解码性保护可控制维度，避免专为视觉重建保留不可控干扰。

<a id="paper-138922"></a>

## Perception, Not Reasoning, Limits Visual Theory of Mind

[官方论文页](https://neurips.cc/virtual/2026/poster/138922) · [作者来源](https://openreview.net/forum?id=wcIvtqkhgL)

- **问题 / 瓶颈** · 视觉比文本差可能因未看清谁当时在场。
- **核心创新 / 方法** · 用五档感知真实度验证视觉、场景描述与文本上界。
- **Baseline** · 仅视觉、仅文本及自动场景描述。
- **Benchmark** · 二维抽象和自然三维的七个 VLM。
- **关键结果 / 消融** · 真值感知支架可弥补差距，自动描述不足；错误中现实偏差占约六成。
- **适用条件 / 局限** · 仅所测虚假信念任务，感知内容可能与推理耦合。

**可复用机制** · 加真值中间表示定位短板，再决定增加感知还是逻辑组件。

<a id="paper-154291"></a>

## Perception Without Engagement: Dissecting the Causal Discovery Deficit in LMMs

[官方论文页](https://neurips.cc/virtual/2026/poster/154291) · [作者来源](https://openreview.net/forum?id=EsnHyvhAN4)

- **问题 / 瓶颈** · 模型可准确讲视频，却在因果判断时沿用文本先验。
- **核心创新 / 方法** · 控制双模态证据以做诊断，再训练原视频策略远离缺视觉选择分布。
- **Baseline** · 普通 GRPO 与只文本先验的参照。
- **Benchmark** · ProCauEval，17 个模型及训练实验。
- **关键结果 / 消融** · 摘要报告视觉参与改善并保留基本理解。
- **适用条件 / 局限** · 遮坏视觉不保证仅去掉先验，须独立测鲁棒性。

**可复用机制** · 弱化替代通道时检验决策确有变化，以免训练只学会描述证据。

<a id="paper-155684"></a>

## Perfect Parallelization in Mini-Batch SGD with Classical Momentum Acceleration

[官方论文页](https://neurips.cc/virtual/2026/poster/155684) · [作者来源](https://openreview.net/forum?id=3iXnCafw0q)

- **问题 / 瓶颈** · 既有随机动量理论需大批尺寸或强噪声假设。
- **核心创新 / 方法** · 分析插值二次目标下 heavy ball 与 Nesterov 的任意小批。
- **Baseline** · 普通 SGD 与经典动量。
- **Benchmark** · 二次插值问题的理论及动量实证。
- **关键结果 / 消融** · 加速与批大小成正比直至饱和。
- **适用条件 / 局限** · 不能推广到一般非插值和非二次模型。

**可复用机制** · 批量和动量应同时扫，结合饱和点决定硬件并行开销。

<a id="paper-150209"></a>

## Performance-Driven Policy Optimization for Speculative Decoding with Adaptive Windowing

[官方论文页](https://neurips.cc/virtual/2026/poster/150209) · [作者来源](https://openreview.net/forum?id=jv3dCrUrFw)

- **问题 / 瓶颈** · 窗口早期不一致会令后部正确草案失去价值。
- **核心创新 / 方法** · 用成本和分布奖励，加自适应选择高偏差窗口训练草案。
- **Baseline** · 逐词元监督草案。
- **Benchmark** · 多模型家族共享协议，接受长度及加速。
- **关键结果 / 消融** · 平均前缀 6.29 至 6.52，速度 3.39 至 4.36 倍。
- **适用条件 / 局限** · 实际收益依赖验证并行和目标模型分布。

**可复用机制** · 将草案损失对齐部署的窗口成功，优先修复截断最常发生的位置。

<a id="paper-155604"></a>

## Performative Prediction with Selective Labels

[官方论文页](https://neurips.cc/virtual/2026/poster/155604) · [作者来源](https://openreview.net/forum?id=4KuDZUSGv3)

- **问题 / 瓶颈** · 选择性标签破坏完全观测下的稳定迭代保证。
- **核心创新 / 方法** · 用标签正例率的区间建立最坏情况目标，再重复最小化风险。
- **Baseline** · 仅使用可观测数据的重复风险最小化。
- **Benchmark** · 选择性反馈的表现性预测，考察距稳定点的偏差。
- **关键结果 / 消融** · 摘要给出在一定距离内的保证。
- **适用条件 / 局限** · 依赖正例率区间及反馈敏感性。

**可复用机制** · 独立跟踪观测机制与预测误差，核查部署造成的选择性偏差。

<a id="paper-150682"></a>

## Per-Loss Adapters for Gradient Conflict in Physics-Informed Neural Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/150682) · [作者来源](https://openreview.net/forum?id=gI9SOvgxbz)

- **问题 / 瓶颈** · 统一改梯度会对不同原因过度干预。
- **核心创新 / 方法** · 先观测 1000 步原训练，再按现象选择重权或为每个损失加独立低秩适配器。
- **Baseline** · 原 PINN、标量均衡、全参数梯度干预。
- **Benchmark** · 逾 60 个含正逆问题的 PDE 配置。
- **关键结果 / 消融** · 摘要报告多个明显不同的梯度冲突类型。
- **适用条件 / 局限** · 早期剖面未必预测后期，门槛待核实。

**可复用机制** · 梯度余弦和相对范数都记录，先验证成因再选干预。

<a id="paper-151313"></a>

## PermuQuant: Lowering Per-Group Quantization Error by Reordering Channels for Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151313) · [作者来源](https://openreview.net/forum?id=bQr7RtVC2C)

- **问题 / 瓶颈** · 共享尺度会被组内异质通道的异常值主导。
- **核心创新 / 方法** · 按联合二阶矩分组，并用校准误差决定是否采用排序。
- **Baseline** · 原顺序分组 PTQ。
- **Benchmark** · 扩散模型极低比特设置，考察量化误差及生成保真。
- **关键结果 / 消融** · 摘要指出按组重排可减少误差。
- **适用条件 / 局限** · 依赖校准代表性及索引与融合开销。

**可复用机制** · 控制同一组宽和位宽，仅变化通道次序检验量化质量。

<a id="paper-154178"></a>

## Permutation Sensitivity in t-SVD-based Multi-view Clustering

[官方论文页](https://neurips.cc/virtual/2026/poster/154178) · [作者来源](https://openreview.net/forum?id=FfHdqICXbw)

- **问题 / 瓶颈** · FFT 基隐含依赖输入次序，而聚类结果原则上不应跟随。
- **核心创新 / 方法** · 分别定义结果和表示不变性，用恢复平滑顺序或数据等变变换纠偏。
- **Baseline** · 固定 Fourier 的 t-SVD。
- **Benchmark** · 多视图及不完全多视图聚类。
- **关键结果 / 消融** · 原方法在换序时幅度明显波动。
- **适用条件 / 局限** · 对照需对齐输出置换，新增变换成本待查。

**可复用机制** · 为无序任务加入置换压力测试，避免单个预排序基准夸大能力。

<a id="paper-150368"></a>

## Permute-then-Adapt: Weak-to-Strong Contrastive Image--Text Adaptation

[官方论文页](https://neurips.cc/virtual/2026/poster/150368) · [作者来源](https://openreview.net/forum?id=ibeDXGKMar)

- **问题 / 瓶颈** · 固定相似阈值不随数据集噪声变。
- **核心创新 / 方法** · 离线随机置换估计偶然配对分数，仅纳入统计可区分样本，优化多正例对比目标。
- **Baseline** · 任意阈值、严格单正例与普通蒸馏。
- **Benchmark** · 图文匹配适配，测质量及额外开销。
- **关键结果 / 消融** · 摘要报告可离线预计算且训练开销很低。
- **适用条件 / 局限** · 统计显著不等于语义真值，需控制域漂移和多重比较。

**可复用机制** · 以随机关联为基线验收挖出的正对，再做阈值消融。

<a id="paper-149271"></a>

## PerQ: Inverse Generative Modeling for Neural Image Compression via Quantization Error Compensation

[官方论文页](https://neurips.cc/virtual/2026/poster/149271) · [作者来源](https://openreview.net/forum?id=rZtNsw4WVh)

- **问题 / 瓶颈** · 无约束生成可损像素保真及码率响应。
- **核心创新 / 方法** · 冻结多码率编解码器，再用有界支持的条件流补偿。
- **Baseline** · 多码率失真优化与生成式 MS-ILLM。
- **Benchmark** · Kodak、CLIC2020-test，LPIPS、FID 和编码表现。
- **关键结果 / 消融** · 摘要报告感知相近且编码质量具竞争力。
- **适用条件 / 局限** · 误差单元依赖主编码结构，延迟和更极端码率待查。

**可复用机制** · 同时查像素保真与感知质量，避免只用生成真实感评估编码。

<a id="paper-150672"></a>

## Persistent Planar Memory for Video World Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150672) · [作者来源](https://openreview.net/forum?id=gLnVSxwQF6)

- **问题 / 瓶颈** · 逐像素点云占用大。
- **核心创新 / 方法** · 随生成块一起预测 RGB 和平面，持续合并并以渲染深度回馈模型。
- **Baseline** · 逐像素点云与其他三维世界模型。
- **Benchmark** · DL3DV、RealEstate10K，视频、尺度深度、法线及空间成本。
- **关键结果 / 消融** · 约每场景 5MB、比点云轻约千倍，摘要报告生成质量更优。
- **适用条件 / 局限** · 复杂曲面和非平面物体可能表示不足。

**可复用机制** · 对结构背景与活跃对象采用不同存储单位，并测信息损失。

<a id="paper-148512"></a>

## Persistent-Transient Policy Evaluation for Markov Chains via Minimal Peripheral Quotients

[官方论文页](https://neurips.cc/virtual/2026/poster/148512) · [作者来源](https://openreview.net/forum?id=xJcl52dxxi)

- **问题 / 瓶颈** · 经典回报均值和偏差会把周期模式与真正暂态混在一起。
- **核心创新 / 方法** · 按外围特征子空间取商，将所有不衰减模式隔离到持续部分。
- **Baseline** · 经典增益和偏差分解。
- **Benchmark** · 有限链固定策略，含周期和可约状态。
- **关键结果 / 消融** · 给出最小精确商和固定规约下唯一分解。
- **适用条件 / 局限** · 依赖已知或可估转移矩阵，谱间隙小的数值表现待查。

**可复用机制** · 单独汇报相位持久性，避免将长期周期波动当作初始化噪声。

<a id="paper-153612"></a>

## Persona-Model Collapse in Emergent Misalignment

[官方论文页](https://neurips.cc/virtual/2026/poster/153612) · [作者来源](https://openreview.net/forum?id=K5bBnxdnZ5)

- **问题 / 瓶颈** · 单一总体评分会掩盖角色一致性退化。
- **核心创新 / 方法** · 比较基础模型与受控微调后的人设问卷方差。
- **Baseline** · 基础模型及匹配的安全训练对照。
- **Benchmark** · 四模型的问卷与角色一致分析。
- **关键结果 / 消融** · 风险条件下角色间敏感与角色内波动同时上升。
- **适用条件 / 局限** · 量表变化仅为行为证据。

**可复用机制** · 用无害角色及授权系统测跨版本差异，确保人格一致性与正常能力。

<a id="paper-152713"></a>

## Persona Vectors: Monitoring and Controlling Character Traits in Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152713) · [作者来源](https://openreview.net/forum?id=QvUJ3iQrY6)

- **问题 / 瓶颈** · 微调可使模型产生跨任务性格漂移。
- **核心创新 / 方法** · 对照部署响应、训练数据和防护干预的一致性，只记录检测与预防。
- **Baseline** · 未加预防干预的普通微调。
- **Benchmark** · 奉承、幻觉等行为与模型变化。
- **关键结果 / 消融** · 摘要称监测可预测部分行为漂移并排查影响数据。
- **适用条件 / 局限** · 检测是代理，未覆盖所有表面行为。

**可复用机制** · 用批准的良性数据做多轮回归，并以行为实测确认探针。

<a id="paper-154674"></a>

## Per-Starting-Point Plausibility and Diversity Bounds for Score-Based Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154674) · [作者来源](https://openreview.net/forum?id=Bspdourakl)

- **问题 / 瓶颈** · 平均过起点的结论不能解释单输入。
- **核心创新 / 方法** · 给单起点合理性和两起点可分性的配套界。
- **Baseline** · 已有先验平均分析。
- **Benchmark** · 二维合成、MNIST、CIFAR-10 的定性验证。
- **关键结果 / 消融** · 同一收缩率控制两项，超过一阶段后起点信息消退。
- **适用条件 / 局限** · 边界与得分质量相关。

**可复用机制** · 编辑时同时报告主体保留和目标分布偏差。

<a id="paper-152558"></a>

## Persuasive Prediction via Decision Calibration

[官方论文页](https://neurips.cc/virtual/2026/poster/152558) · [作者来源](https://openreview.net/forum?id=SEBdVdqbdq)

- **问题 / 瓶颈** · 全局校准不保证每种响应的误差平衡。
- **核心创新 / 方法** · 以决策条件无偏性分析替代精确共同先验。
- **Baseline** · 理想已知先验与普通预测。
- **Benchmark** · 抽象博弈中的单接收和随机响应理论。
- **关键结果 / 消融** · 证明条件下可无交换遗憾，单接收可匹配已知先验参照。
- **适用条件 / 局限** · 依赖最佳响应假设，不可外推到现实个体。

**可复用机制** · 在非个人的库存分配模拟中评全局与决策条件误差。

<a id="paper-148703"></a>

## Perturb and Correct: Post-Hoc Ensembles using Affine Redundancy

[官方论文页](https://neurips.cc/virtual/2026/poster/148703) · [作者来源](https://openreview.net/forum?id=vfloLQFqoN)

- **问题 / 瓶颈** · 训练域相同的模型在外部可表现不同。
- **核心创新 / 方法** · 随机变换一层后以相邻仿射层最小二乘恢复校准集预测。
- **Baseline** · 普通事后集成。
- **Benchmark** · MuJoCo 动力学和 CIFAR-10 域外检测。
- **关键结果 / 消融** · 报告在一个预训练模型上取得较强域内外折中。
- **适用条件 / 局限** · 依赖校准支持覆盖。

**可复用机制** · 对照用不同数据训练的集合，区分分歧和真正可靠告警。

<a id="paper-150547"></a>

## Perturb, Repair, Verify: Self-Play Vision-Language Verifiers for Compositional Understanding

[官方论文页](https://neurips.cc/virtual/2026/poster/150547) · [作者来源](https://openreview.net/forum?id=hK4oymHJs3)

- **问题 / 瓶颈** · 固定难负例昂贵，且不随模型错误更新。
- **核心创新 / 方法** · 用已知正确的图文配对，对局部描述做受控变换，重新核验修订结果。
- **Baseline** · 静态教师和固定负例。
- **Benchmark** · 组合核验及视觉细节鲁棒性。
- **关键结果 / 消融** · 摘要报告细节判断增强且总体多模态能力保持。
- **适用条件 / 局限** · 自生成数据和评估可能共享错误。

**可复用机制** · 按普通物体、计数和关系错误分层，用独立标签验收。

<a id="paper-155303"></a>

## PE-SHAP: Causally Interpretable Path-Wise Shapley Explanations

[官方论文页](https://neurips.cc/virtual/2026/poster/155303) · [作者来源](https://openreview.net/forum?id=6afj7vl5xr)

- **问题 / 瓶颈** · 一般 Shapley 可能漏链中介。
- **核心创新 / 方法** · 以去除部分通路的效果构造逐中介归因。
- **Baseline** · 关联归因及已有因果路径 Shapley。
- **Benchmark** · 已知作用的合成 SCM、German Credit、COMPAS。
- **关键结果 / 消融** · 逐样本量加总到总中介，群体聚合为 NIE。
- **适用条件 / 局限** · 依赖因果图和可辨识假定。

**可复用机制** · 在有已知链路的合成图验证加总和信号分配。

<a id="paper-151379"></a>

## Pessimistic Latent Task-aware Optimization for Robust Offline Meta-Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151379) · [作者来源](https://openreview.net/forum?id=b2o4Aci1XF)

- **问题 / 瓶颈** · 干净表征不能解决策略从未见过区域。
- **核心创新 / 方法** · 从任务簇中心向外扰动潜量，由模型集合生成短轨迹并评可信度。
- **Baseline** · 强离线上下文元强化学习。
- **Benchmark** · 八个 MuJoCo 连续控制任务。
- **关键结果 / 消融** · 摘要称域外回报改善且域内有竞争力。
- **适用条件 / 局限** · 中心距离与任务罕见程度并非普遍对应。

**可复用机制** · 将潜量距离、模型分歧和策略效果分别报告。

<a id="paper-152045"></a>

## PF-SGS: Pose-Free Streaming 3D Gaussian Splatting for Large-Scale Scene Reconstruction

[官方论文页](https://neurips.cc/virtual/2026/poster/152045) · [作者来源](https://openreview.net/forum?id=VvTOafbWm6)

- **问题 / 瓶颈** · 逐帧单向状态易忘记旧场景并缺局部约束。
- **核心创新 / 方法** · 门控持久记忆的更新，以有限未来观测补局部几何。
- **Baseline** · 依赖位姿先验的大尺度方法。
- **Benchmark** · 可变长序列，重建质量与用时。
- **关键结果 / 消融** · 摘要称线性成本且接近位姿先验方案。
- **适用条件 / 局限** · 缓冲引入延迟，新摄像头条件待核。

**可复用机制** · 在相同延迟及内存下比较是否使用有限前视。

<a id="paper-152738"></a>

## PGGT-Loc: Primitive-Grounded Geometry Transformer for Feed-Forward Camera Localization

[官方论文页](https://neurips.cc/virtual/2026/poster/152738) · [作者来源](https://openreview.net/forum?id=Qj1kSEf9Rs)

- **问题 / 瓶颈** · 复杂地图长期维护昂贵。
- **核心创新 / 方法** · 将单图与平面图元做对应，联合预测位姿相关目标。
- **Baseline** · 多阶段和稠密地图定位。
- **Benchmark** · 详细平面地图与简化建筑布局。
- **关键结果 / 消融** · 摘要称两种地图设置均领先。
- **适用条件 / 局限** · 依赖能见结构与地图时效。

**可复用机制** · 在图元有缺失且光照变化时测定位退化。

<a id="paper-153527"></a>

## PGID: Progressive Guided Inversion and Denoising for Robust Watermark Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/153527) · [作者来源](https://openreview.net/forum?id=KfdFXxbNSJ)

- **问题 / 瓶颈** · 仅测正常样本无法发现检测符号不稳。
- **核心创新 / 方法** · 用受控测试比较防御性反演去噪和普通检测。
- **Baseline** · 常见语义水印检测。
- **Benchmark** · 多种水印方案，受控来源检测。
- **关键结果 / 消融** · 摘要报告恢复被干扰来源检测并减少错误判定。
- **适用条件 / 局限** · 模型和水印范围有限。

**可复用机制** · 在自有正常图与合成退化上分报误报及漏报。

<a id="paper-150392"></a>

## PG-LRF: Physiology-Guided Latent Rectified Flow for Electro-Hemodynamic PPG-to-ECG Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/150392) · [作者来源](https://openreview.net/forum?id=iOvXn5DzBr)

- **问题 / 瓶颈** · 统计相关可重建外观却不满足信号生成关系。
- **核心创新 / 方法** · 用共享相位模拟辅助构造潜空间，并联合检验 ECG 和 PPG 一致。
- **Baseline** · 纯数据驱动生成。
- **Benchmark** · MC-MED，测信号和下游分类。
- **关键结果 / 消融** · 摘要报告两方面提升。
- **适用条件 / 局限** · 生成信号不能当临床真实测量。

**可复用机制** · 匹配相关性指标，独立检查高频形态和正向测量一致。

<a id="paper-148213"></a>

## PGMS: Pyramidal Gaussian Mixture Splatting for 3DGS Compression

[官方论文页](https://neurips.cc/virtual/2026/poster/148213) · [作者来源](https://openreview.net/forum?id=zWaptyAtZO)

- **问题 / 瓶颈** · 单点量化忽略几何和外观联合冗余。
- **核心创新 / 方法** · 递归聚类成金字塔，按目标码率分配容量，并按成像贡献更新。
- **Baseline** · 固定高斯结构及其他压缩。
- **Benchmark** · 常见 3DGS 码率和渲染基准。
- **关键结果 / 消融** · 摘要称高压缩同时保持画质。
- **适用条件 / 局限** · 编码开销和不同纹理场景待核。

**可复用机制** · 在相同文件量下按尺度比较外观共享和几何简化。

<a id="paper-152671"></a>

## PGSB: Pretrained-Guided Shared Basis for LoRA Model Merging

[官方论文页](https://neurips.cc/virtual/2026/poster/152671) · [作者来源](https://openreview.net/forum?id=RH9XxRniDK)

- **问题 / 瓶颈** · 各任务低秩坐标未必可直接互加。
- **核心创新 / 方法** · 共同子空间重表达与基底权重交互后再融合。
- **Baseline** · 权重或低秩空间直接合并。
- **Benchmark** · 多个任务基准，明细待核。
- **关键结果 / 消融** · 摘要称稳健超过强参考。
- **适用条件 / 局限** · 预训练底座一致及独特技能保留需验。

**可复用机制** · 同参数量分别测试共享与冲突任务的收益。

<a id="paper-151387"></a>

## Phaedra: Learning High-Fidelity Discrete Tokenization for the Physical Sciences

[官方论文页](https://neurips.cc/virtual/2026/poster/151387) · [作者来源](https://openreview.net/forum?id=b0sJcf0mWu)

- **问题 / 瓶颈** · 自然图像词元通常忽视强度和频谱的精确性。
- **核心创新 / 方法** · 以形状和增益分量分别表达物理场压缩。
- **Baseline** · 既有视觉离散编码器。
- **Benchmark** · 各 PDE、未见方程和遥感观测。
- **关键结果 / 消融** · 摘要称恢复、泛化与下游预测改善。
- **适用条件 / 局限** · 适用动态范围和码率待核。

**可复用机制** · 同时测幅值、频谱和局部几何，而非只验感知相似。

<a id="paper-155415"></a>

## Phase-Adaptive Fusion: Spatio-Temporal Modulation for VLA Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155415) · [作者来源](https://openreview.net/forum?id=5qxJ8cZwVt)

- **问题 / 瓶颈** · 本体输入可形成捷径，令接触时忽略空间线索。
- **核心创新 / 方法** · 从动作和状态历史估阶段，以空间对齐和时间分支门控。
- **Baseline** · 标准图像与本体融合。
- **Benchmark** · LIBERO、Meta-World、Robomimic 及长程实机。
- **关键结果 / 消融** · 摘要称降低对位漂移并改善鲁棒。
- **适用条件 / 局限** · 阶段标签和真实安全需复核。

**可复用机制** · 仅在低风险环境按阶段遮挡视觉或扰动本体，比较精度。

<a id="paper-153947"></a>

## PhaseDance: Capturing Rhythm and Expressivity in Dance Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/153947) · [作者来源](https://openreview.net/forum?id=HN7bfQQd3M)

- **问题 / 瓶颈** · 逐拍匹配不保证形成连续节奏单元。
- **核心创新 / 方法** · 以周期相位表征舞蹈，将表达性用结构指标监督。
- **Baseline** · 逐拍生成及传统舞种标签。
- **Benchmark** · 多个动作或舞蹈任务，节奏与表现指标。
- **关键结果 / 消融** · 摘要称整体节奏更一致且表现增强。
- **适用条件 / 局限** · 复杂节奏和人工评价待核。

**可复用机制** · 分别改变节拍速度和小节相位，测模型是否混淆。

<a id="paper-154774"></a>

## Phase-DGS: Phase-Guided Dynamic Gaussian Splatting from Unsynchronized Multi-view Video

[官方论文页](https://neurips.cc/virtual/2026/poster/154774) · [作者来源](https://openreview.net/forum?id=B3qu4p01hU)

- **问题 / 瓶颈** · 错时、丢帧和冻结破坏传统动态重建。
- **核心创新 / 方法** · 用语义相位统一不同相机观测，并接入已有动态高斯。
- **Baseline** · RealTime-4DGS、FreeTimeGS 等。
- **Benchmark** · 偏移、丢帧和冻结的多视图评测。
- **关键结果 / 消融** · 摘要报告最高增加 8.5 dB PSNR。
- **适用条件 / 局限** · 非周期动作或相位歧义待核。

**可复用机制** · 分周期及非周期两组验帧匹配与重建稳定。

<a id="paper-150371"></a>

## Phase Kernel Lifts Capacity of Dense Associative Memory

[官方论文页](https://neurips.cc/virtual/2026/poster/150371) · [作者来源](https://openreview.net/forum?id=iZSMEnlggu)

- **问题 / 瓶颈** · 线性核使吸引域重叠，产生虚假状态。
- **核心创新 / 方法** · 使用非线性相位核分离吸引域并保持单调能量下降。
- **Baseline** · 线性现代 Hopfield 网络。
- **Benchmark** · MNIST、CIFAR-10、TinyImageNet。
- **关键结果 / 消融** · 摘要报告临界容量最多升约 50 倍，检索抗噪改善。
- **适用条件 / 局限** · 理论限定所构造核族。

**可复用机制** · 用过载与噪声扫查吸引域质量，而非只测低负载正确率。

<a id="paper-151017"></a>

## PhaseLoRA: Control-Regime-Conditioned Low-Rank Adaptation for Continuous-Action Vision-Language-Action Policies

[官方论文页](https://neurips.cc/virtual/2026/poster/151017) · [作者来源](https://openreview.net/forum?id=dZhUeQa53U)

- **问题 / 瓶颈** · 接近、接触和运输需求不同，静态更新不适用全部阶段。
- **核心创新 / 方法** · 以细控制倾向和边界强度调动作专家 LoRA 左因子。
- **Baseline** · 同参数高秩 LoRA，标量门控等。
- **Benchmark** · LIBERO 平均成功。
- **关键结果 / 消融** · 相对同参数对照高 12.2 点；消融支持方向变化。
- **适用条件 / 局限** · 依赖可靠阶段代理，实机待核查。

**可复用机制** · 适配少量参数时先对照相位级方向更新，再考虑增秩。

<a id="paper-150376"></a>

## Phases of Muon: When Muon  Eclipses SignSGD

[官方论文页](https://neurips.cc/virtual/2026/poster/150376) · [作者来源](https://openreview.net/forum?id=iXZjCLrCHW)

- **问题 / 瓶颈** · 大批有效的谱预条件在小批不必成立。
- **核心创新 / 方法** · 从矩阵最小二乘提取 SignSVD 与 SignSGD 的确定动态。
- **Baseline** · 两种符号或谱规则及等方差情况。
- **Benchmark** · 幂律协方差、目标频谱与批尺寸。
- **关键结果 / 消融** · 大批 SignSVD 有平方根预条件，小批弱特征接近 SGD；两者优势分区。
- **适用条件 / 局限** · 结论限理想高维模型。

**可复用机制** · 不要用单批结果决定优化器，校验低特征模态是否仍有加速。

<a id="paper-149119"></a>

## Phase Space Attention: A Hairer Lift Resolves the Single-Layer Induction Obstruction

[官方论文页](https://neurips.cc/virtual/2026/poster/149119) · [作者来源](https://openreview.net/forum?id=sk3TDpwOR9)

- **问题 / 瓶颈** · 标准一层双线性注意缺所需滤波阶。
- **核心创新 / 方法** · 对旋转位置编码后的流应用辛剪切。
- **Baseline** · 原单层注意与双层归纳电路。
- **Benchmark** · 4M 至 92M 模型及受控归纳任务。
- **关键结果 / 消融** · 摘要报告一设置单层 74.2% 并有明确相变。
- **适用条件 / 局限** · 唯一性限定义的设计类，相变依赖假设。

**可复用机制** · 补显式时序状态前先检查缺失的滤波阶，避免盲目扩骨干。

<a id="paper-148770"></a>

## Phase Transitions in Attention: A Bayesian Theory of Copy Head Emergence

[官方论文页](https://neurips.cc/virtual/2026/poster/148770) · [作者来源](https://openreview.net/forum?id=vB716nAsNr)

- **问题 / 瓶颈** · 不同学习曲线可能掩盖不同归纳机制。
- **核心创新 / 方法** · 将复制任务后验降到低维序参量，核验优化动态。
- **Baseline** · softmax 和线性注意力。
- **Benchmark** · 单层复制任务、后验采样与 Adam。
- **关键结果 / 消融** · softmax 一阶跳变，线性先二阶再平滑过渡。
- **适用条件 / 局限** · 简化复制任务不直接等同真实模型。

**可复用机制** · 比较网络宽度时控制数据量，并查看电路形成是否突变。

<a id="paper-152536"></a>

## Phase Transitions in Heavy-Tailed Mean Estimation under $\ell_p$ Norms

[官方论文页](https://neurips.cc/virtual/2026/poster/152536) · [作者来源](https://openreview.net/forum?id=SQPGUFQdc1)

- **问题 / 瓶颈** · 欧氏样本均值的期望优势不能外推高阶范数。
- **核心创新 / 方法** · 采用按坐标中位均值，按 n、d、p 的关系调分组。
- **Baseline** · 普通样本均值与投影中位均值。
- **Benchmark** · 只假定存在协方差的 Lp 风险。
- **关键结果 / 消融** · p 大于二时某区间需稳健化才能达到最优期望。
- **适用条件 / 局限** · 具体阈值需依理论分布类。

**可复用机制** · 按最终误差度量选稳健估计，而非沿用为置信度调出的分组。

<a id="paper-148777"></a>

## Phase-wise MLLM Tuning for Multi-framework WebUI Code Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/148777) · [作者来源](https://openreview.net/forum?id=v877QpbW7u)

- **问题 / 瓶颈** · 软件框架交叉训练可能混语法，造成编译失败。
- **核心创新 / 方法** · 固定框架语法并归一无关命名，在异质度和兼容度下分组与排序。
- **Baseline** · 共同微调及其他基线。
- **Benchmark** · 截图到 React、Vue、Angular 等生成。
- **关键结果 / 消融** · 摘要报告编译和生成均改善。
- **适用条件 / 局限** · 归一处理需保留各框架的真实约束。

**可复用机制** · 对结构不同的目标先测负迁移，用阶段适配而非全批无差别混合。

<a id="paper-150700"></a>

## Phase-wise Velocity Distillation: Towards Effective Image Generation with A Single NFE

[官方论文页](https://neurips.cc/virtual/2026/poster/150700) · [作者来源](https://openreview.net/forum?id=g9V4RTYjMF)

- **问题 / 瓶颈** · 单次学生同时处理两阶段易过平滑。
- **核心创新 / 方法** · 将时间轴拆相位学习平均速度，复杂文本任务另分别判别。
- **Baseline** · 已有蒸馏学生与多步教师。
- **Benchmark** · ImageNet 256、SD3.5-Medium、FLUX.1-dev。
- **关键结果 / 消融** · 单次教师等效计算下 ImageNet FID 1.48。
- **适用条件 / 局限** · 两次半模型的具体墙钟需核实。

**可复用机制** · 用相同总计算但不同阶段专长，分开验收全局结构及细节。

<a id="paper-149200"></a>

## PhGPO: Pheromone-Guided Policy Optimization for Long-Horizon Tool Planning

[官方论文页](https://neurips.cc/virtual/2026/poster/149200) · [作者来源](https://openreview.net/forum?id=sAUmVeY7RI)

- **问题 / 瓶颈** · 只奖励当前成功没有显式复用跨步骤结构。
- **核心创新 / 方法** · 从以往轨迹估成功工具转移并引导策略。
- **Baseline** · 标准长程工具强化。
- **Benchmark** · 多步工具规划；具体基准待核实。
- **关键结果 / 消融** · 摘要报告规划改善。
- **适用条件 / 局限** · 依赖转移可跨任务，需留探索预算。

**可复用机制** · 将成功重用粒度设为局部转移，避免记住整条计划。

<a id="paper-155933"></a>

## PHIONet: Port Hamiltonian Inertial Odometry Network

[官方论文页](https://neurips.cc/virtual/2026/poster/155933) · [作者来源](https://openreview.net/forum?id=1hm3CeFT8G)

- **问题 / 瓶颈** · 局部速度拟合准确也可能累计漂移。
- **核心创新 / 方法** · 在有限 IMU 窗用耗散能量残差联结校正和速度。
- **Baseline** · 学习式惯导对照。
- **Benchmark** · Blackbird、EuRoC，ATE 与 RTE。
- **关键结果 / 消融** · 摘要报告两类误差降低。
- **适用条件 / 局限** · 依赖所设耗散与惯性观测。

**可复用机制** · 给轨迹模型加窗口级物理一致性，验收累计而非单帧误差。

<a id="paper-139250"></a>

## PHMForge: Evaluating LLM Agents on Industrial Prognostics through MCP-Native, Algorithm-Grounded Tools

[官方论文页](https://neurips.cc/virtual/2026/poster/139250) · [作者来源](https://openreview.net/forum?id=cCEnSuNLxJ)

- **问题 / 瓶颈** · 工具能调用不等于知道何时调用，静态检索不一定能代替计算。
- **核心创新 / 方法** · 对照算法工具与同信息静态检索，按轨迹分解错误。
- **Baseline** · 三框架及六模型、静态 RAG。
- **Benchmark** · 99 场景、八类资产。
- **关键结果 / 消融** · 最佳 pass@1 80.8%，部分寿命场景静态替代使 5/5 降 1/5。
- **适用条件 / 局限** · 子集很小，安全使用需明确人审。

**可复用机制** · 对有算法计算的任务做等信息对照，别把工具优势笼统归给检索。

<a id="paper-139754"></a>

## PHOEBI: An Open-World Benchmark for Multi-Label Bacterial Identification in Phase-Contrast Microscopy

[官方论文页](https://neurips.cc/virtual/2026/poster/139754) · [作者来源](https://openreview.net/forum?id=6cpui5CQW9)

- **问题 / 瓶颈** · 随机划分会把已见组合作为泛化，端到端错误难归因。
- **核心创新 / 方法** · 冻结视觉表征，对照池化及未知类别输出。
- **Baseline** · 普通分类骨干、预训练和解码器。
- **Benchmark** · PHOEBI 的未见混合组合。
- **关键结果 / 消融** · 摘要报告普通分类掉点，改变池化更有效。
- **适用条件 / 局限** · 是非侵入图像识别结果，跨采集条件需验证。

**可复用机制** · 先验收局部证据是否可读，再检查组合汇总是否掩盖少数组分。

<a id="paper-149703"></a>

## PhotoFlow: Agentic 3D Virtual Photography Missions

[官方论文页](https://neurips.cc/virtual/2026/poster/149703) · [作者来源](https://openreview.net/forum?id=o5fDea7QFO)

- **问题 / 瓶颈** · 一次机位预测难兼顾几何和构图，重复渲染浪费。
- **核心创新 / 方法** · 先提多样候选，比较当前最优，再将失败位置转为区域记忆。
- **Baseline** · 单轮预测、单链反思、锚点与随机。
- **Benchmark** · 47 个 Blender 场景、141 个摄影任务。
- **关键结果 / 消融** · 六轮预算下摘要报告质量和成功率最高。
- **适用条件 / 局限** · 美学评分依赖评审，几何遮挡随场景变。

**可复用机制** · 在有昂贵模拟反馈的搜索中记住失败区域，而不只存最佳样本。

<a id="paper-139124"></a>

## PhyMetric: Diagnosing Physical Plausibility in Text-to-Video Generation via Scene-Level QA

[官方论文页](https://neurips.cc/virtual/2026/poster/139124) · [作者来源](https://openreview.net/forum?id=jfYWGg0AKD)

- **问题 / 瓶颈** · 泛问是否符合物理可能退化到随机判断。
- **核心创新 / 方法** · 结合具体物理前提、事件序列和证据帧做二元校验。
- **Baseline** · 单一泛化评分。
- **Benchmark** · 1,115 场景、8,920 平衡题及三裁判。
- **关键结果 / 消融** · 泛问准确降至机会水平，物理先验改善与人类对齐。
- **适用条件 / 局限** · 裁判能力不同，先验需正确。

**可复用机制** · 把综合质量分解为可证伪的事件观测和时序约束。

<a id="paper-154704"></a>

## PhyMo: Learning Physical Dynamics with Accurate and Continuous Motion from Multi-View Videos

[官方论文页](https://neurips.cc/virtual/2026/poster/154704) · [作者来源](https://openreview.net/forum?id=BfBnHowvB9)

- **问题 / 瓶颈** · 只渲染监督可用外观变化遮掩错轨。
- **核心创新 / 方法** · 显式轨迹表示区分变形与外观，双向约束运动连续。
- **Baseline** · 当前动态场景重建方法。
- **Benchmark** · 四个动态场景数据。
- **关键结果 / 消融** · 摘要报告插值与未来运动表现领先。
- **适用条件 / 局限** · 快速遮挡或非刚性运动仍需针对验收。

**可复用机制** · 把几何预测和图像质量分开评分，避免用外观补偿错误动力。

<a id="paper-149085"></a>

## PhyMotion: Structured 3D Motion Reward for Physics-Grounded Human Video Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/149085) · [作者来源](https://openreview.net/forum?id=szjzOlLpZL)

- **问题 / 瓶颈** · 二维质量可能给悬空或违背动力的动作高分。
- **核心创新 / 方法** · 将估计三维人体动作重定向到仿真，分项给连续反馈。
- **Baseline** · 二维感知型及既有奖励。
- **Benchmark** · 自回归和双向视频生成，自动及盲评。
- **关键结果 / 消融** · 摘要报告动作真实性提升，三个分项互补。
- **适用条件 / 局限** · 依赖人体恢复误差及仿真近似。

**可复用机制** · 用可解释分量定位运动失败，不让整体视觉分掩盖接触或动态异常。

<a id="paper-149508"></a>

## PhyProbe: Rethinking Physical Consistency Evaluation in Generated Videos

[官方论文页](https://neurips.cc/virtual/2026/poster/149508) · [作者来源](https://openreview.net/forum?id=pcRAi8J0Ss)

- **问题 / 瓶颈** · 不同标注源只给偏序或含噪绝对分。
- **核心创新 / 方法** · 冻结时空编码器，训练轻评分头融合排序、回归与校准。
- **Baseline** · 通用视觉语言裁判及专用物理评估器。
- **Benchmark** · 真实生成、全生成配对和人类偏好。
- **关键结果 / 消融** · 摘要报告排序与线性相关均较强。
- **适用条件 / 局限** · 只在所测视频领域评价，分数须复校。

**可复用机制** · 用跨来源共享锚点维持合同尺度，同时保留可靠局部的比较信号。

<a id="paper-153149"></a>

## PhysAgentGym: Free Physical-Law Verifiers for Training Small Code-Reasoning Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/153149) · [作者来源](https://openreview.net/forum?id=NV5qjfDXZB)

- **问题 / 瓶颈** · 手写答案或仅看终点不利于规模化也难识别错误机理。
- **核心创新 / 方法** · 将物理约束编为多时点谓词，以稠密和稀疏评分筛训练轨迹。
- **Baseline** · 仅末端筛选和大型参照模型。
- **Benchmark** · 四物理子域、1,320 个模拟任务。
- **关键结果 / 消融** · 7B 报告均分 0.942、接近所比前沿模型；双评分筛选有 1.4 至 8.7 点改善。
- **适用条件 / 局限** · 闭式规律需可信，弱谓词可能漏错。

**可复用机制** · 只在可执行规范通过时将代理输出作监督，并记录轨迹中每类误差。

<a id="paper-152574"></a>

## PhysDNet: Physics-Driven Gradient Amplification for Real-Time Image Dehazing

[官方论文页](https://neurips.cc/virtual/2026/poster/152574) · [作者来源](https://openreview.net/forum?id=S57Q0ZigdC)

- **问题 / 瓶颈** · 轻型模型容量有限，重雾细节更难学。
- **核心创新 / 方法** · 融合近红外和稀疏深度，经固定物理反演的双输出损失调梯度。
- **Baseline** · 已有去雾方法。
- **Benchmark** · Seeing Through Fog，PSNR、检测恢复与边缘算耗。
- **关键结果 / 消融** · 高 1.67 dB 且少 5.2 倍算力，恢复约 54.9% 检测损失。
- **适用条件 / 局限** · 物理近似不总成立，异质雾仍需验证。

**可复用机制** · 仅在训练阶段使用物理梯度聚焦难区域，部署时不增加模型。

<a id="paper-139832"></a>

## PhysEval: Quantifying the Gap Between Video Generation and World Physical Laws

[官方论文页](https://neurips.cc/virtual/2026/poster/139832) · [作者来源](https://openreview.net/forum?id=26VREDvTyr)

- **问题 / 瓶颈** · 自然运动外观可掩盖错误的加速度或守恒量。
- **核心创新 / 方法** · 为题目记录目标值、单位、可量测条件和预期物体数，按条件提取物理量。
- **Baseline** · 感知与文字对齐以及定性物理评估。
- **Benchmark** · 十项运动学、材料与守恒指标。
- **关键结果 / 消融** · 摘要提出自动区分可量测和不满足前提的样本。
- **适用条件 / 局限** · 标定、遮挡及自动提取误差需验证。

**可复用机制** · 先检查视频是否满足量测条件，再分开统计真实性与数值偏差。

<a id="paper-155354"></a>

## PhysFormer: Learning to Simulate Mechanics in World Space

[官方论文页](https://neurips.cc/virtual/2026/poster/155354) · [作者来源](https://openreview.net/forum?id=6G9JMnjcL7)

- **问题 / 瓶颈** · 像素生成缺少可直接评估的机械变量，逐步递推积累误差。
- **核心创新 / 方法** · 在节点位置、速度、材料条件下扩散整段网格，分别做时间、顶点和物体注意力。
- **Baseline** · 自回归机械动力学。
- **Benchmark** · 十万余碰撞轨迹，刚体、可变形体、未见几何及更多物体。
- **关键结果 / 消融** · 报告轨迹误差、刚性及动量上的改善。
- **适用条件 / 局限** · 训练以仿真为主，全轨迹内存及分布外碰撞仍需查。

**可复用机制** · 同一动力学数据对照整段输出与逐步积分，直接验证守恒和轨迹误差。

<a id="paper-148671"></a>

## PhysGraphNet: Physical-State Scene Graphs via Latent Graph Reasoning and Counterfactual Supervision

[官方论文页](https://neurips.cc/virtual/2026/poster/148671) · [作者来源](https://openreview.net/forum?id=vxrLfNSsBQ)

- **问题 / 瓶颈** · 语义视觉编码难识别遮挡、开闭和阻挡等谓词。
- **核心创新 / 方法** · 将物体、关系和记忆 token 送入图推理层，加状态反事实及校准。
- **Baseline** · 无图监督、视觉对比模型及少样本 GPT-4o。
- **Benchmark** · PACBench 的物理状态 F1、选择题和反事实方向。
- **关键结果 / 消融** · 微 F1 0.651，相比最强无图对照高 0.170；反事实方向一致率 99.6%。
- **适用条件 / 局限** · 单图的不可观察状态无法只靠学习消除。

**可复用机制** · 将静态谓词正确和改变物理条件时的响应方向分开测。

<a id="paper-148249"></a>

## PhysGuard: Fisher-Guided Gradient Projection for Sim-to-Real Neural PDE Surrogates

[官方论文页](https://neurips.cc/virtual/2026/poster/148249) · [作者来源](https://openreview.net/forum?id=zHUiR3DWyZ)

- **问题 / 瓶颈** · 适配实测误差可能破坏预训练获得的物理结构。
- **核心创新 / 方法** · 在仿真数据上用经验 Fisher 识别关键参数方向，逐层 Gram 形式执行更新投影。
- **Baseline** · 普通 sim-to-real 微调。
- **Benchmark** · 神经算子仿真到实测适配。
- **关键结果 / 消融** · 摘要给出适用于数百万参数的高效投影。
- **适用条件 / 局限** · 若仿真物理先验本身有错，保护方向会妨碍适配；净增益待查。

**可复用机制** · 同时测旧物理结构保持和实测改善，不能只看新域误差。

<a id="paper-150035"></a>

## Physics-Constrained Generative World Model for Off-Road Terrain via Post-hoc Projection

[官方论文页](https://neurips.cc/virtual/2026/poster/150035) · [作者来源](https://openreview.net/forum?id=lG1tx6cbVl)

- **问题 / 瓶颈** · 惩罚项可能同时损失地形逼真度且无法保证可行。
- **核心创新 / 方法** · 对生成输出用闭式投影处理坡度稳定、承载及连续性。
- **Baseline** · 无约束生成和匹配的 PhysLoss。
- **Benchmark** · 四类生成器及 TartanDrive，物理通过率、FID 和额外开销。
- **关键结果 / 消融** · 扩散通过率从 53% 到 100%，FID 仍为 13.72；四类方法额外开销小于 4.3%。
- **适用条件 / 局限** · 只保证所定义的约束，投影外的物理风险和边界需测。

**可复用机制** · 固定生成器分别记录约束通过与分布偏移，检查后处理能否兼顾。

<a id="paper-154719"></a>

## Physics-Informed Optimal Control by Control-Only Supervision with Error Guarantees on Value and Policy

[官方论文页](https://neurips.cc/virtual/2026/poster/154719) · [作者来源](https://openreview.net/forum?id=BWHQemN2Xs)

- **问题 / 瓶颈** · 没有值标签常难直接学可执行控制。
- **核心创新 / 方法** · 由值函数梯度派生策略，用 Riccati 参考产生控制标签。
- **Baseline** · SDRE 求解器。
- **Benchmark** · 高维控制数值实验，测代价、稳定和推理速度。
- **关键结果 / 消融** · 理论给值及梯度误差界，实测与 SDRE 代价接近。
- **适用条件 / 局限** · 依赖动力学和控制求解结构，真实系统验证待查。

**可复用机制** · 检查预测控制和价值梯度的一致性，不只对照控制动作误差。

<a id="paper-150133"></a>

## PhySPRING: Structure-Preserving Reduction of Physics-Informed  Digital Twins via Graph Neural Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/150133) · [作者来源](https://openreview.net/forum?id=kRm7mfbn8W)

- **问题 / 瓶颈** · 细网格继承不必要拓扑，拖慢循环模拟。
- **核心创新 / 方法** · 学习机械参数和多个粗化层，所有层保留显式弹簧质量系统。
- **Baseline** · 未粗化数字孪生。
- **Benchmark** · PhysTwin 的重建和动态预报。
- **关键结果 / 消融** · 摘要报告响应引导粗化可改善与压缩并行的预测。
- **适用条件 / 局限** · 接触拓扑和少见碰撞的保真需独立验证。

**可复用机制** · 逐层报告速度与任务相关机械响应，避免只测几何压缩。

<a id="paper-155622"></a>

## PiCA: Pivot-Based Credit Assignment For Search Agentic Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/155622) · [作者来源](https://openreview.net/forum?id=4CNCefRkpK)

- **问题 / 瓶颈** · 结果反馈稀疏且逐步独立评分忽略依赖
- **核心创新 / 方法** · 以历史条件下的成功概率衡量信息增益并突出关键转折，基于势函数奖励塑形
- **Baseline** · 现有过程奖励方法，名称未报告
- **Benchmark** · 七个知识密集 QA 基准
- **关键结果 / 消融** · 3B 和 7B 提升 15.2% 和 2.2%，摘要未给出统计口径
- **适用条件 / 局限** · 依赖对状态成功率的估计

**可复用机制** · 给搜索智能体分配信用时，估计动作改变最终成功概率的幅度

<a id="paper-153056"></a>

## PickMoment: Continuous-Time Single-Image-to-Video via Learning Deblurring and Blur-to-Video

[官方论文页](https://neurips.cc/virtual/2026/poster/153056) · [作者来源](https://openreview.net/forum?id=OLVcmhgg5O)

- **问题 / 瓶颈** · 中心帧或固定数量帧遗漏任意曝光时刻
- **核心创新 / 方法** · 拟合曝光子区间的均值，训练同时约束重建、区间可加性和零区间清晰帧
- **Baseline** · 去模糊生成法及复原法，名称未报告
- **Benchmark** · GoPro、HIDE、RealBlur 和 GoPro-7
- **关键结果 / 消融** · 摘要称在 GoPro-7 单次前向逐帧保真度最高
- **适用条件 / 局限** · 依赖曝光积分模型与可用子帧监督

**可复用机制** · 对时间积分传感恢复，利用子区间组成规律做自一致监督

<a id="paper-148976"></a>

## PiD: Fast and High-Resolution Latent Decoding with Pixel Diffusion

[官方论文页](https://neurips.cc/virtual/2026/poster/148976) · [作者来源](https://openreview.net/forum?id=tkGw4mDy71)

- **问题 / 瓶颈** · 逆编码解码器难合成高分辨细节
- **核心创新 / 方法** · 用噪声级适配器接收未完全去噪 latent，并用 DMD2 蒸馏为四步
- **Baseline** · 先解码再超分的级联
- **Benchmark** · 多个 VAE 和语义潜空间，比较视觉保真度、内存及延迟
- **关键结果 / 消融** · RTX 5090 上 512 到 2048 的案例低于 1 秒，峰值 13 GB
- **适用条件 / 局限** · 性能数字依赖硬件和分辨率

**可复用机制** · 把生成与解码交接提前，但应把交接噪声级作为解码条件

<a id="paper-138985"></a>

## PieArena: Ranking and Profiling Language Agents in Realistic Negotiation Scenarios

[官方论文页](https://neurips.cc/virtual/2026/poster/138985) · [作者来源](https://openreview.net/forum?id=sODMs3VRWj)

- **问题 / 瓶颈** · 单次结果混合对手能力和环境偏差
- **核心创新 / 方法** · 用连续收益、互换及交叉配对构造带不确定性的排名并校正不对称
- **Baseline** · 人际与人机对照及不同语言模型
- **Benchmark** · MBA 课程改编谈判任务，连续收益与行为指标
- **关键结果 / 消融** · 联合意图脚手架对中低档收益大，前沿档收益递减
- **适用条件 / 局限** · 受场景和人类样本限制

**可复用机制** · 对交互式 Agent 同时报校正后排名、不确定性与回合内行为

<a id="paper-138968"></a>

## PINNBench: A Benchmark and Evaluation Study of Training Policy Selection in Hybrid PINN-Operator Solvers

[官方论文页](https://neurips.cc/virtual/2026/poster/138968) · [作者来源](https://openreview.net/forum?id=tV0S5T2Cz8)

- **问题 / 瓶颈** · 选错不同训练策略的代价差异大
- **核心创新 / 方法** · 在标准化训练政策对照中比较路由后悔并跨方程族留出
- **Baseline** · 五种路由方法，包括物理损失启发法和随机森林
- **Benchmark** · 13 个 PDE 配置、八个方程族，主要对照使用相对 L2
- **关键结果 / 消融** · 两路由命中均为 62%，平均后悔 0.0850 对 0.0011
- **适用条件 / 局限** · 证据来自特定 PDE 和有限政策候选

**可复用机制** · 模型路由以选错后损失校准，不用准确率单独排序

<a id="paper-148525"></a>

## Pion: A Spectrum-Preserving Optimizer via Orthogonal Equivalence Transformation

[官方论文页](https://neurips.cc/virtual/2026/poster/148525) · [作者来源](https://openreview.net/forum?id=xFbqlwBtwM)

- **问题 / 瓶颈** · 常见加法更新同时改变尺度和几何
- **核心创新 / 方法** · 通过左右正交变换更新矩阵，保持奇异值
- **Baseline** · Adam、Muon 为摘要点名的加法优化器
- **Benchmark** · LLM 预训练和微调，指标未报告
- **关键结果 / 消融** · 摘要报告稳定且有竞争力
- **适用条件 / 局限** · 固定谱限制谱值适应且摘要未列消融数值

**可复用机制** · 把旋转与谱变化拆成独立因素，检验优化收益来自何处

<a id="paper-150938"></a>

## PISA: Piecewise Sparse Attention Is Wiser for Efficient Diffusion Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/150938) · [作者来源](https://openreview.net/forum?id=eBE11Hq3CA)

- **问题 / 瓶颈** · 高稀疏率下删块破坏上下文
- **核心创新 / 方法** · 关键块精确算，其余利用分布稳定性做块级 Taylor 近似
- **Baseline** · 块稀疏注意力方法
- **Benchmark** · Wan2.1、Hunyuan-Video 和 FLUX 的生成质量与加速
- **关键结果 / 消融** · 两个视频模型加速 1.91 倍和 2.57 倍
- **适用条件 / 局限** · 依赖弱块稳定性，泛化需复核

**可复用机制** · 用精确或近似的二级计算替代仅保留或删除

<a id="paper-155482"></a>

## PISG: Constraint-Aligned Signal Amplification for Diffusion-Based Combinatorial Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/155482) · [作者来源](https://openreview.net/forum?id=5G4RbpOCB8)

- **问题 / 瓶颈** · 预测排名与可行性错位使贪心回退
- **核心创新 / 方法** · 外推原预测与结构降质预测的差，强化约束相关变量
- **Baseline** · DIFUSCO、T2T、FastT2T、StruDiCO 等求解器无增强版本
- **Benchmark** · TSP 和 MIS-ER，贪心解码且无后处理
- **关键结果 / 消融** · 16 个 TSP 求解器规模组合和四个 MIS-ER 求解器均改善，最高 8.4%
- **适用条件 / 局限** · 须构造有意义的结构扰动且依赖已有去噪器信号

**可复用机制** · 先检验变量评分是否识别约束，再决定是否增配搜索预算

<a id="paper-139226"></a>

## PitchBench: Measuring Pitch Hearing in Audio-Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139226) · [作者来源](https://openreview.net/forum?id=dlSvqHjTE4)

- **问题 / 瓶颈** · 高层任务和选择题可能掩盖音高感知不足
- **核心创新 / 方法** · 分别测绝对与相对音高，系统变化音源、时长、噪声和记谱
- **Baseline** · 被测前沿音频语言模型，完整名单未报告
- **Benchmark** · 28 项实验，覆盖序列、和弦及复调
- **关键结果 / 消融** · 多个设置下表现不稳定并随音源、时长和格式变化
- **适用条件 / 局限** · 受控音乐感知证据，未覆盖所有音频任务

**可复用机制** · 多模态评测从高层任务拆出基本感知因子，检查困难来自输入还是作答形式

<a id="paper-152042"></a>

## PIVOT: A Unified Agentic Framework for Streaming Long-Video Understanding

[官方论文页](https://neurips.cc/virtual/2026/poster/152042) · [作者来源](https://openreview.net/forum?id=VxtrscFTfw)

- **问题 / 瓶颈** · 固定响应时机难覆盖未来证据
- **核心创新 / 方法** · 在严格顺序访问和有界共享记忆下，由规划器检索、观察并决策回答或延后
- **Baseline** · 固定检索或响应策略的流式系统和离线视频智能体
- **Benchmark** · 由 LVBench 转换的 LVBench-Ref2Stream，准确率及延迟
- **关键结果 / 消融** · 摘要未报告具体数字
- **适用条件 / 局限** · 依赖证据时间锚标注，评测需联合看延迟

**可复用机制** · 用过去、现在和未来混合提问验证缓存与延答策略

<a id="paper-151098"></a>

## PixelART: Image-to-Layer Decomposition without Latents or Text-to-Image Pretraining

[官方论文页](https://neurips.cc/virtual/2026/poster/151098) · [作者来源](https://openreview.net/forum?id=d0YFvkRclJ)

- **问题 / 瓶颈** · 低噪细节表现不能代表正确分配到可编辑图层。
- **核心创新 / 方法** · 以像素流直接建模 RGBA，增加高噪时点覆盖。
- **Baseline** · VAE 潜扩散和文本到图像初始化。
- **Benchmark** · 多层模板最高 1024²，层及合成重建。
- **关键结果 / 消融** · 摘要报告参数少逾十倍；数据充足时文本生成初始化未增最终质量。
- **适用条件 / 局限** · 强结论依赖训练规模；小数据迁移待验。

**可复用机制** · 按错误是否影响分配或纹理区分时间步，给真正决定可编辑性的阶段更多监督。

<a id="paper-153886"></a>

## PixelDense: Dense Prediction as Representation Alignment for Pixel Diffusion

[官方论文页](https://neurips.cc/virtual/2026/poster/153886) · [作者来源](https://openreview.net/forum?id=I1UN3yU3WX)

- **问题 / 瓶颈** · 平加多个教师压入同投影会相互抵消。
- **核心创新 / 方法** · 按语义及几何拆投影，用参数正交惩罚隔离。
- **Baseline** · DINOv2、单密集教师及不分组多教师。
- **Benchmark** · PixelGen、DeCo，GenEval、DPG-Bench、HPS；另测深度与全景。
- **关键结果 / 消融** · GenEval 总体 0.7927 到 0.8093，摘要报告超过各单教师。
- **适用条件 / 局限** · 投影分离效果依赖教师任务分工。

**可复用机制** · 梯度目标存在不变性冲突时，先隔离教师所需空间，再比较同教师数量的共享对照。

<a id="paper-155465"></a>

## PixelDiT2: Representation-Grounded Pixel Diffusion Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/155465) · [作者来源](https://openreview.net/forum?id=5P4vAdvfAy)

- **问题 / 瓶颈** · 从原 RGB 同时学表示和去噪会拖慢收敛。
- **核心创新 / 方法** · 给去噪 Transformer 注入明确的逐块视觉表征指导。
- **Baseline** · JiT-G。
- **Benchmark** · ImageNet 256²，FID、训练轮数。
- **关键结果 / 消融** · 320 轮 FID 1.50，对照 600 轮 1.82。
- **适用条件 / 局限** · 推理期教师成本及独立消融待核实。

**可复用机制** · 训练原空间生成器时用冻结视觉表征减轻学习结构的负担。

<a id="paper-153024"></a>

## PixelPonder: Dynamic Patch Adaptation for Enhanced Multi-Conditional Text-to-Image Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/153024) · [作者来源](https://openreview.net/forum?id=OZZyhPmeOO)

- **问题 / 瓶颈** · 独立条件分支全局叠加会产生冗余和失真。
- **核心创新 / 方法** · 在图块选择有效控制，在时间轴从结构到纹理改变注入。
- **Baseline** · 独立的 ControlNet 类机制。
- **Benchmark** · 多种空间控制与文本一致性。
- **关键结果 / 消融** · 摘要报告对齐改善且保持语义。
- **适用条件 / 局限** · 依赖条件质量和局部判定，冲突条件需单验。

**可复用机制** · 让不同条件在擅长的空间与阶段参与，而不是整图同权投票。

<a id="paper-153571"></a>

## Pixels over Symbols: Sensory Realism Improves Behavioral Alignment in Models of Cognition

[官方论文页](https://neurips.cc/virtual/2026/poster/153571) · [作者来源](https://openreview.net/forum?id=KPqWTVFc4d)

- **问题 / 瓶颈** · 符号输入可能让模型解题，却掩盖表示如何形成人类样的动态。
- **核心创新 / 方法** · 对同类任务用写实和抽象输入训练，另做冻结权重换输入。
- **Baseline** · 抽象符号网络及人类。
- **Benchmark** · 一组依赖记忆的决策任务。
- **关键结果 / 消融** · 写实模型更像人类但仍差；冻结抽象骨干可解任务却改变原来动态。
- **适用条件 / 局限** · 仅支持所测任务，行为相似不等于机制同一。

**可复用机制** · 在抽象结果外验证真实感官接口，避免从任务准确推出人类样推理。

<a id="paper-149181"></a>

## Pixel-space Autoregressive Image Synthesis via Spectrum Serialization and Flow-based Refinement

[官方论文页](https://neurips.cc/virtual/2026/poster/149181) · [作者来源](https://openreview.net/forum?id=sHRb3N6tLL)

- **问题 / 瓶颈** · VQ 重建损失可沿解码传播。
- **核心创新 / 方法** · 比较表示内在维数，直接序列化离散像素块并做流精修。
- **Baseline** · VQ 自回归和现有图像生成。
- **Benchmark** · 类条件及文本条件生成。
- **关键结果 / 消融** · 摘要报告有竞争力；原始 patch 的估计内在维数较低。
- **适用条件 / 局限** · 估计维数不证明所有数据均适合像素序列。

**可复用机制** · 先测编码损失是否主导，再选择不依赖单独预训练编码器的粗细分工。

<a id="paper-148535"></a>

## Pixels to Tokens: Token Space Efficient Active Learning for Low-Budget Semantic Segmentation

[官方论文页](https://neurips.cc/virtual/2026/poster/148535) · [作者来源](https://openreview.net/forum?id=xBIIoVBT4V)

- **问题 / 瓶颈** · 将词元插值至高分辨率可能制造选择几何伪迹。
- **核心创新 / 方法** · 冻结 DINOv3，在多层原词元格用两级 MaxHerding，最后以解码间隔细化。
- **Baseline** · 已有低标注主动分割。
- **Benchmark** · CamVid、Cityscapes、ADE20K、Pascal Context。
- **关键结果 / 消融** · 十轮每图一点时最高分别加 14.65 与 23.34 mIoU。
- **适用条件 / 局限** · 依赖视觉表示覆盖，弱类别标签有偏时需复验。

**可复用机制** · 用可靠低分辨分组选择初候选，再付高分辨人工标注成本。

<a id="paper-139117"></a>

## PixFoundation 2.0: Do Video Multi-Modal LLMs Use Motion in Visual Grounding?

[官方论文页](https://neurips.cc/virtual/2026/poster/139117) · [作者来源](https://openreview.net/forum?id=k9wJGm2f4P)

- **问题 / 瓶颈** · 动作描述可被静态特征捷径解答。
- **核心创新 / 方法** · 构造错序及真假运动对照，单独验按描述定位目标。
- **Baseline** · 强单图定位及已有视频方法。
- **Benchmark** · MoCentric-Bench 的运动指代。
- **关键结果 / 消融** · 摘要报告单帧常持平或更强，专门动作适配改善所测新基准。
- **适用条件 / 局限** · 限受控动作及分割任务。

**可复用机制** · 改变时间信息但保留同样对象，确认系统的优势来自真正读时序。

<a id="paper-155100"></a>

## PLACE: Patch-Level Agnostic Concept Extraction

[官方论文页](https://neurips.cc/virtual/2026/poster/155100) · [作者来源](https://openreview.net/forum?id=8QlhKxCYSB)

- **问题 / 瓶颈** · 局部裁剪破坏全局几何，梯度监督又贵。
- **核心创新 / 方法** · 在原激活上以 Gram 对齐监督无标签概念。
- **Baseline** · 梯度 KL 提取及 SAE。
- **Benchmark** · ImageNet、COCO 与 DINOv2、ViT-MAE、ViT-B/16。
- **关键结果 / 消融** · 报告比 KL 方案约快 20 倍、比 SAE 约 11 倍。
- **适用条件 / 局限** · 对齐相似不是完全因果，跨下游需验证。

**可复用机制** · 解释视觉骨干优先保留原输入产生的关系几何，再评估代理忠实性。

<a id="paper-150699"></a>

## Plan2Sense: Open-World Task Planning in Epistemic States via Interleaved Ontic and Sensing Actions

[官方论文页](https://neurips.cc/virtual/2026/poster/150699) · [作者来源](https://openreview.net/forum?id=g9ZhljQuww)

- **问题 / 瓶颈** · 无差别搜集昂贵，猜测初态则可能不可执行。
- **核心创新 / 方法** · 用真、假、未知的知识状态和目标回归生成条件策略，含对象绑定。
- **Baseline** · 全探索与假设式重规划。
- **Benchmark** · 三个第一视角开放世界探测基准。
- **关键结果 / 消融** · 摘要报告成功率及效率更高，避免所测不良状态。
- **适用条件 / 局限** · 依赖能表达任务的知识谓词，实机误感知待查。

**可复用机制** · 把未知状态设为显式待获取条件，感知计划只为可行性服务。

<a id="paper-150984"></a>

## PLANING: A Loosely Coupled Triangle-Gaussian Framework for Streaming 3D Reconstruction

[官方论文页](https://neurips.cc/virtual/2026/poster/150984) · [作者来源](https://openreview.net/forum?id=dmRkqf6pOG)

- **问题 / 瓶颈** · 仅追渲染或仅追几何难同时稳定。
- **核心创新 / 方法** · 以三角形及高斯松耦合，在线用独立几何、外观优化。
- **Baseline** · PGSR、ARTDECO 及离线 2D Gaussian Splatting。
- **Benchmark** · ScanNetV2，Chamfer、PSNR 和时间。
- **关键结果 / 消融** · 相较 PGSR Chamfer 改善 18.52%，较 ARTDECO 高 1.31 dB。
- **适用条件 / 局限** · 依赖两表示持续对齐。

**可复用机制** · 将长期几何维护和高频纹理校正拆成不同更新路径，分别验收。

<a id="paper-150211"></a>

## Planning as Dynamics Relaxation: Hippocampal Recurrent Network Realizes Optimal Goal-Directed Navigation

[官方论文页](https://neurips.cc/virtual/2026/poster/150211) · [作者来源](https://openreview.net/forum?id=juTALxlaPs)

- **问题 / 瓶颈** · 重新搜索全图忽略已有可复用导航动力。
- **核心创新 / 方法** · 让递归网权重表示空间转移，目标驱动松弛求线性可解 MDP 的场。
- **Baseline** · 经典线性可解 MDP 解。
- **Benchmark** · 复杂障碍导航模拟和解析同等性。
- **关键结果 / 消融** · 摘要报告松弛实现最优目标引导，局部变化仅需低秩更新。
- **适用条件 / 局限** · 限定给定转移及代价，生理实现未证实。

**可复用机制** · 对环境变化频繁的任务保留可局部编辑的转移图，并用同一场生成行动方向。

<a id="paper-153963"></a>

## Planning Persuasion, Not Utterances: Profile-Conditioned Open-Loop Search for Dialogue Strategy

[官方论文页](https://neurips.cc/virtual/2026/poster/153963) · [作者来源](https://openreview.net/forum?id=HCOhbXzn7c)

- **问题 / 瓶颈** · 逐句树分支高，生成偏好与表述混在一起。
- **核心创新 / 方法** · 按抽象对话动作扩展，并在多个历史实例上评估节点再转写。
- **Baseline** · 直接生成与文字级规划。
- **Benchmark** · PersuasionForGood 的受控对话研究。
- **关键结果 / 消融** · 摘要报告策略搜索与任务指标改善。
- **适用条件 / 局限** · 域内结果不证明跨用户效度，需明确同意边界。

**可复用机制** · 将高层交互策略与表面表达分离，使流程能审计目标与实际语言。

<a id="paper-148860"></a>

## Platonic Representations in the Human Brain: Unsupervised Recovery of Universal Geometry

[官方论文页](https://neurips.cc/virtual/2026/poster/148860) · [作者来源](https://openreview.net/forum?id=udfnSh2EHl)

- **问题 / 瓶颈** · 没有跨受试者配对时难比较神经表示。
- **核心创新 / 方法** · 用刺激重复自监督，各自建空间，再同步两两正交旋转。
- **Baseline** · 未同步的成对旋转。
- **Benchmark** · Natural Scenes Dataset 的跨受试者检索。
- **关键结果 / 消融** · 摘要报告同步到共同空间继续改善检索。
- **适用条件 / 局限** · 依赖视觉任务重叠，不能外推到所有脑表征。

**可复用机制** · 先用保持距离的变换检验共享几何，必要时才引入自由度更大的对齐。

<a id="paper-155058"></a>

## Platonic Task Arithmetic

[官方论文页](https://neurips.cc/virtual/2026/poster/155058) · [作者来源](https://openreview.net/forum?id=8mxuyjOsQd)

- **问题 / 瓶颈** · 异构权重不存在一一坐标对应。
- **核心创新 / 方法** · 提取架构无关矩阵，先做任务代数，再轻量实现在目标模型。
- **Baseline** · 单同架构任务向量。
- **Benchmark** · 多个模型任务的组合和转移。
- **关键结果 / 消融** · 摘要报告能跨异构模型传递。
- **适用条件 / 局限** · 描述构造与保真分解待核实。

**可复用机制** · 让可比较对象是行为变化而非权重差，分别测组合和实现误差。

<a id="paper-150534"></a>

## PLATO: Pointer Learner for Agent and Task Openness

[官方论文页](https://neurips.cc/virtual/2026/poster/150534) · [作者来源](https://openreview.net/forum?id=hQ5UdY6Jie)

- **问题 / 瓶颈** · 填充掩码暗中固定任务和代理上限。
- **核心创新 / 方法** · 以指针策略和形状动态的图 critic 编码实体关系。
- **Baseline** · 有限规模和只支持单一开放因素的代理。
- **Benchmark** · MOASEI 野火响应模拟。
- **关键结果 / 消融** · 摘要报告零样本结果更一致，策略支持变化集合。
- **适用条件 / 局限** · 需控制实体增长成本，模拟不能代替现场验证。

**可复用机制** · 让动作索引由实时对象集合定义，而非预划固定类别。

<a id="paper-152410"></a>

## Plausibility Is Not Prediction: Contrastive Evidence for LLM-Based Cellular Perturbation Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/152410) · [作者来源](https://openreview.net/forum?id=TK0wNbf8IH)

- **问题 / 瓶颈** · 合理叙述可能完全不读具体观察。
- **核心创新 / 方法** · 比较模型、简单频率及预定义基因分层的预测效果。
- **Baseline** · 频率基线及接近随机对照。
- **Benchmark** · 受控细胞观测预测；仅提取评测证据。
- **关键结果 / 消融** · 摘要报告部分模型回退到近随机的逐基因辨别。
- **适用条件 / 局限** · 不提供生物设计或干预建议；机制归因待实验。

**可复用机制** · 基准若存在边缘频次信号，应当控制实体身份后再验证模型是否真的使用条件。

<a id="paper-154712"></a>

## Playing ZendoWorld: Challenging AI Agents on Active Visual Concept Induction

[官方论文页](https://neurips.cc/virtual/2026/poster/154712) · [作者来源](https://openreview.net/forum?id=BZmvSJeoow)

- **问题 / 瓶颈** · 对训练例分类正确也可能用错规则。
- **核心创新 / 方法** · 让 Agent 主动构造场景获取反馈，比较视觉、贝叶斯和符号方法。
- **Baseline** · 纯视觉语言推理、粒子过滤、动态概念发现及人类。
- **Benchmark** · ZendoWorld 视觉概念游戏，测反馈实验与规则。
- **关键结果 / 消融** · 摘要报告视觉语言代理选择的试验接近无信息。
- **适用条件 / 局限** · 结论依赖规则空间、可提议动作和感知质量。

**可复用机制** · 对同一首批观察比较随机试验与信息导向试验，直接测能排除多少假设。

<a id="paper-151476"></a>

## PLLS-CP: Unsupervised Hallucination Detection with Layer Selection and Cross-Domain Conformal Guarantees

[官方论文页](https://neurips.cc/virtual/2026/poster/151476) · [作者来源](https://openreview.net/forum?id=aKIJQBf4JP)

- **问题 / 瓶颈** · 固定阈值缺覆盖保证，完全重训练昂贵。
- **核心创新 / 方法** · 用伪标签选层学检测器，外接 Mondrian 共形校准。
- **Baseline** · 不迁移阈值及仅内部信号检测。
- **Benchmark** · 领域移位检测，考察边际覆盖和重新校准。
- **关键结果 / 消融** · 目标域重新校准后给出边际覆盖及偏差集中界。
- **适用条件 / 局限** · 要求可取得目标校准数据，不能把边际覆盖视为任意子组保证。

**可复用机制** · 让表示迁移和阈值校准成为两项成本独立的决策。

<a id="paper-154423"></a>

## PoEM: Predicting New RL Outcomes from Existing Policies

[官方论文页](https://neurips.cc/virtual/2026/poster/154423) · [作者来源](https://openreview.net/forum?id=Dh60W6N12a)

- **问题 / 瓶颈** · 每次奖励修改都重训昂贵，逐参数平均不一定符合奖励关系。
- **核心创新 / 方法** · 线性奖励组合对应对数策略组合；更一般情形用近似低秩。
- **Baseline** · 每次按新奖励重新训练。
- **Benchmark** · 跨奖励后训练结果及策略预测。
- **关键结果 / 消融** · 摘要给出线性情形的关系，非线性情形常见近似低秩。
- **适用条件 / 局限** · 关系的正则化和共享参考策略条件待查。

**可复用机制** · 先验证新奖励及策略投影视角的留出误差，再决定是否需要训练。

<a id="paper-155736"></a>

## Point4D: Long-range 4D Motion Reconstruction

[官方论文页](https://neurips.cc/virtual/2026/poster/155736) · [作者来源](https://openreview.net/forum?id=3L4DUaI1nh)

- **问题 / 瓶颈** · 基于最初图像补丁或重投影，在遮挡及视角变化后失效。
- **核心创新 / 方法** · 采用可灵活查询的三维点运动解码器，将上块端点直接用于下一块。
- **Baseline** · 短上下文前馈四维方法和起点补丁。
- **Benchmark** · 超过两百帧的多种跟踪评测。
- **关键结果 / 消融** · 摘要报告超过原前馈模型并能跟踪更长序列。
- **适用条件 / 局限** · 端点误差仍可积累，极端回环是否能重新对齐待查。

**可复用机制** · 在固定起始点对照跨块三维记忆和逐块二维匹配。

<a id="paper-153208"></a>

## Point Cloud Sequence Encoding for Material-conditioned Graph Network Simulators

[官方论文页](https://neurips.cc/virtual/2026/poster/153208) · [作者来源](https://openreview.net/forum?id=N1j3W5Bm2y)

- **问题 / 瓶颈** · 真实观测难获得刚度等物性与网格。
- **核心创新 / 方法** · 以时空点云序列编码器为图模拟器提供上下文，并加入辅助监督。
- **Baseline** · 给定物性或以网格轨迹适配。
- **Benchmark** · 仿真新物性及动态场景的零样本 sim-to-real。
- **关键结果 / 消融** · 摘要报告零样本案例精度较高。
- **适用条件 / 局限** · 依赖时序观测能区分物性，欠观测及规模需查。

**可复用机制** · 将隐参数推断和后续动力学预测分开验收。

<a id="paper-149146"></a>

## Point Tracking Improves World Action Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149146) · [作者来源](https://openreview.net/forum?id=sVFAjZ4nrj)

- **问题 / 瓶颈** · 像素变化混合动作、光照与纹理。
- **核心创新 / 方法** · 同一扩散 Transformer 联合预测视觉潜态、二维轨迹、可见性与动作。
- **Baseline** · 像素世界动作模型。
- **Benchmark** · LIBERO、真实 LeRobot，含长程遮挡、交互、出画。
- **关键结果 / 消融** · 摘要报告遮挡等困难长程任务收益最大。
- **适用条件 / 局限** · 追踪伪标偏差与动作收益的因果隔离待核实。

**可复用机制** · 分开测观感和任务相关运动，验证长程可见性变化时的控制。

<a id="paper-149391"></a>

## PointZero: 3D Point Track Completion for Learning Transferable 3D Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/149391) · [作者来源](https://openreview.net/forum?id=qPN2noamDW)

- **问题 / 瓶颈** · 依赖动作标注限制可用视频范围。
- **核心创新 / 方法** · 单 RGB-D 及少量已知三维轨迹预测可见点未来轨迹。
- **Baseline** · 相同数据上的既有动态预测方法。
- **Benchmark** · 290 万合成帧，含刚体、关节和形变，另做下游迁移。
- **关键结果 / 消融** · 摘要报告在同数据下改善。
- **适用条件 / 局限** · 深度及轨迹来源、真实视频域迁移需查。

**可复用机制** · 把稀疏局部运动当作条件，比较同数据下纯 RGB 预训练和三维运动补全。

<a id="paper-154048"></a>

## POISE: Instance-Specific Prompt Tuning under Latent Mixture Target Distributions

[官方论文页](https://neurips.cc/virtual/2026/poster/154048) · [作者来源](https://openreview.net/forum?id=GbrExqa8nQ)

- **问题 / 瓶颈** · 单共享提示可能保留不可消除的近似差距
- **核心创新 / 方法** · 按输入路由可训练提示专家，用共享低秩残差补公共结构
- **Baseline** · 静态共享提示；具体实验模型未报告
- **Benchmark** · 多个基准，名称和指标未报告
- **关键结果 / 消融** · 摘要称分流提示参数效率较高，理想分配下后悔可逼近零
- **适用条件 / 局限** · 理论依赖潜在有限混合与理想分配条件

**可复用机制** · 先测共享提示在不同样本簇是否冲突，再选择单提示或路由专家

<a id="paper-154663"></a>

## Poisoning Attacks on LLMs Require a Near-constant Number of Poison Samples

[官方论文页](https://neurips.cc/virtual/2026/poster/154663) · [作者来源](https://openreview.net/forum?id=BxdDYMEfcZ)

- **问题 / 瓶颈** · 容易把数据规模误作异常影响的替代指标
- **核心创新 / 方法** · 对照不同训练规模的安全回归表现
- **Baseline** · 不同规模的训练条件
- **Benchmark** · 模型预训练和微调的受控安全评测
- **关键结果 / 消融** · 摘要提示规模增加本身无法保证异常影响下降
- **适用条件 / 局限** · 受控实验，外推到任意训练流程未验证

**可复用机制** · 以数据来源审计和授权安全回归判断整体防护效果

<a id="paper-156031"></a>

## Polar Transformers: $SO(2)^K$-Equivariant Angular Attention for Cryo-EM Image-Set Processing

[官方论文页](https://neurips.cc/virtual/2026/poster/156031) · [作者来源](https://openreview.net/forum?id=10lTNbAX7p)

- **问题 / 瓶颈** · 各图独立旋转且低信噪时对齐困难
- **核心创新 / 方法** · 用极坐标特征和 FFT 相关计算相对角度注意力，并对置换保持不变
- **Baseline** · 单图及图像组基线，名称未报告
- **Benchmark** · 模拟冷冻电镜图像，去噪相对 MSE 和下游分辨率
- **关键结果 / 消融** · SNR 为 0.02 时相对 MSE 最大降 40%，下游重建分辨率改善 20%
- **适用条件 / 局限** · 摘要证据来自模拟数据和面内旋转

**可复用机制** · 为多视图融合按已知变换群设计相对位置注意力

<a id="paper-154799"></a>

## Polestar: Drift-Aware Cache Calibration and Token Commitment for Efficient Inference of Diffusion LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/154799) · [作者来源](https://openreview.net/forum?id=AsdJ0sPsgT)

- **问题 / 瓶颈** · 双向注意让缓存失效，也使固定提交阈值不稳
- **核心创新 / 方法** · 稀疏刷新漂移位置，并用显著漂移事件判断 token 是否提交
- **Baseline** · 现有效率基线，名称未报告
- **Benchmark** · 多种扩散语言模型的数学和代码生成，测准确率、吞吐与并行度
- **关键结果 / 消融** · 摘要报告最高 10.73% 准确率提升及 3.7 倍吞吐
- **适用条件 / 局限** · 依赖双向解码结构及漂移信号

**可复用机制** · 迭代推理中直接测内部状态变化，联合决定何时复用与停止

<a id="paper-154425"></a>

## Policy-DRIFT: Dynamic Reward-Informed Flow Trajectory Steering

[官方论文页](https://neurips.cc/virtual/2026/poster/154425) · [作者来源](https://openreview.net/forum?id=Dg4j2E3Vtz)

- **问题 / 瓶颈** · 策略直接优化任务奖励可能需要较高执行能耗
- **核心创新 / 方法** · 条件流匹配学习可实现状态，推理时终端奖励引导目标，跟踪策略优化场误差
- **Baseline** · 直接 DRL 控制基线
- **Benchmark** · DNS 湍流通道，摩擦雷诺数 180；减阻与致动能耗
- **关键结果 / 消融** · 减阻 49%，致动能耗约为 DRL 的 1/37
- **适用条件 / 局限** · 仅验证单一模拟工况，依赖可实现状态建模

**可复用机制** · 可复用控制器按统一跟踪目标训练，任务偏好放在目标采样器

<a id="paper-154020"></a>

## Policy-Level Exploration for Coordinated Multi-Agent Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/154020) · [作者来源](https://openreview.net/forum?id=GqILfCgsZe)

- **问题 / 瓶颈** · 逐步动作噪声会破坏跨步协调
- **核心创新 / 方法** · 选项策略从共享子策略集合选择，条件于所选策略确定性执行
- **Baseline** · 主流多智能体 RL 方法，具体名单未报告
- **Benchmark** · Predator Prey、SMAC、SMACv2、Google Research Football、MACO
- **关键结果 / 消融** · 摘要报告样本效率和最终性能均改善
- **适用条件 / 局限** · 依赖可学习的共享子策略及任务中的跨步结构

**可复用机制** · 把协作探索的随机性放到策略级而非逐步动作级

<a id="paper-151120"></a>

## Policy Optimization in Hybrid Discrete-Continuous Action Spaces via Mixed Gradients

[官方论文页](https://neurips.cc/virtual/2026/poster/151120) · [作者来源](https://openreview.net/forum?id=cqg3IKxaHY)

- **问题 / 瓶颈** · 直接微分离散决策或非光滑动力学会产生偏差或弱信号
- **核心创新 / 方法** · 可微连续段走路径梯度，其余使用得分函数，组合保持无偏
- **Baseline** · PPO
- **Benchmark** · 库存控制和切换线性二次调节
- **关键结果 / 消融** · 连续动作维度越高，相对 PPO 差距越大；离散最优响应附近交叉项变弱
- **适用条件 / 局限** · 需能对平滑模拟器部分反向传播

**可复用机制** · 对混合机器人控制器按可微性选择梯度估计器

<a id="paper-153141"></a>

## PolyMind: Exploring Width Scaling for Reflective Reasoning in Language Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/153141) · [作者来源](https://openreview.net/forum?id=NaTtE318r2)

- **问题 / 瓶颈** · 增加同质反思容易产生重复上下文
- **核心创新 / 方法** · 规划互补审查范围，隔离执行，再汇总成结构化简报；用角色平衡目标训练
- **Baseline** · 最强串行深度反思对照及宽度参考
- **Benchmark** · 代码生成、数学推理与多跳问答，同反思预算
- **关键结果 / 消融** · 平均领先 6.1%，弥合约 80% 的参考差距
- **适用条件 / 局限** · 依赖可验证反馈及有效汇总

**可复用机制** · 按排查角度分配并行反思工位，并定额比较重试预算

<a id="paper-151361"></a>

## PolyVision: Conditional Visual Scaling Via Dynamic Expert Routing For Vision-Centric MLLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/151361) · [作者来源](https://openreview.net/forum?id=b8tcacoAkU)

- **问题 / 瓶颈** · 固定专家池的均匀执行把成本花在所有 patch 上
- **核心创新 / 方法** · 注意力路由器按 patch 分配编码器，VisPack 打包执行且保留样本独立性
- **Baseline** · 基于 Qwen3，摘要未列对照名单
- **Benchmark** · 多模态基准，具体名称和指标未报告
- **关键结果 / 消融** · 摘要报告视觉理解和效率权衡有改善
- **适用条件 / 局限** · 需要多个预对齐的视觉专家及路由执行支持

**可复用机制** · 让局部视觉证据决定算力分配，检查专家调用分布与质量

<a id="paper-148262"></a>

## POME: Post Optimization Model Edit via Muon-Style Projection

[官方论文页](https://neurips.cc/virtual/2026/poster/148262) · [作者来源](https://openreview.net/forum?id=zA8hNLdmm6)

- **问题 / 瓶颈** · 微调更新谱中可能夹杂幅度很小的噪声方向
- **核心创新 / 方法** · 对权重增量做截断 SVD，剪掉小奇异值并均衡保留方向
- **Baseline** · 原始微调检查点
- **Benchmark** · GSM8K 与代码生成，涵盖 7B 至 72B 模型
- **关键结果 / 消融** · 摘要报告平均提升 2.5% 与 1.0%
- **适用条件 / 局限** · 需配对兼容检查点，截断可能去掉小但有用的更新

**可复用机制** · 保留微调前后模型，用谱编辑对照检验增量哪些方向在起作用

<a id="paper-154987"></a>

## Pooling Versus Ensembling for Ridge Regression Under Covariate Shift

[官方论文页](https://neurips.cc/virtual/2026/poster/154987) · [作者来源](https://openreview.net/forum?id=9QYohrmHKg)

- **问题 / 瓶颈** · 子群输入不同是否值得分别训练。
- **核心创新 / 方法** · 分析固定和随机效应下岭回归风险。
- **Baseline** · 逐群最优调参后集成。
- **Benchmark** · 线性结果模型，含无岭极限。
- **关键结果 / 消融** · 随机效应下最优合并优于逐群集成。
- **适用条件 / 局限** · 结论依赖效应和线性模型假设。

**可复用机制** · 分组训练前先拆分输入漂移与条件机制漂移。

<a id="paper-151838"></a>

## PO-PDDL: Learning Symbolic POMDPs from Visual Demonstrations for Robot Planning Under Uncertainty

[官方论文页](https://neurips.cc/virtual/2026/poster/151838) · [作者来源](https://openreview.net/forum?id=XYgtVaASQv)

- **问题 / 瓶颈** · 视频观测与潜在状态不一致。
- **核心创新 / 方法** · 恢复符号状态轨迹，再学习转移和观测模型。
- **Baseline** · PDDL 与 POMDP 模型学习。
- **Benchmark** · 真实长时程操作，规划表现和成本。
- **关键结果 / 消融** · 规划更稳且成本较低，幅度未报告。
- **适用条件 / 局限** · 要求视频可用于重建符号状态。

**可复用机制** · 用潜状态和观测的分歧定位部分可观测性。

<a id="paper-154370"></a>

## POP: Online Structural Pruning Enables Efficient Inference of Large Foundation Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154370) · [作者来源](https://openreview.net/forum?id=E5kkSzO2hf)

- **问题 / 瓶颈** · 固定剪枝忽略生成上下文。
- **核心创新 / 方法** · 通道分为保留、候选和剪除，随 token 仅更新候选。
- **Baseline** · 既有剪枝方案。
- **Benchmark** · LLM、MoE、视觉语言模型，含生成任务。
- **关键结果 / 消融** · 精度有竞争力，摘要未量化额外开销。
- **适用条件 / 局限** · 依赖预填充分区能保留重要通道。

**可复用机制** · 先固定稳定结构，在线仅对不确定子集自适应。

<a id="paper-149049"></a>

## Population-Aligned Persona Generation for LLM-based Social Simulation

[官方论文页](https://neurips.cc/virtual/2026/poster/149049) · [作者来源](https://openreview.net/forum?id=tFyJ7qpZTB)

- **问题 / 瓶颈** · 角色生成结果不代表目标群体。
- **核心创新 / 方法** · 筛选低保真画像，再重要性采样匹配测量分布并适配子群。
- **Baseline** · 摘要未报告具名基线。
- **Benchmark** · 社会模拟，对齐如大五人格。
- **关键结果 / 消融** · 人口层偏差下降，幅度未报告。
- **适用条件 / 局限** · 依赖可用参考分布及人格代理的有效性。

**可复用机制** · 把角色质量筛选与集合级对齐做成两个可独立检验的环节。

<a id="paper-155506"></a>

## PORTool: Importance-Aware Policy Optimization with Rewarded Tree for Multi-Tool-Integrated Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/155506) · [作者来源](https://openreview.net/forum?id=54keqZlySs)

- **问题 / 瓶颈** · 结果奖励难定位哪个中间决策有贡献。
- **核心创新 / 方法** · 根据分支后代正确性及工具调用有效性赋分，结合局部和全局信号更新。
- **Baseline** · 策略优化基线，名称未报告。
- **Benchmark** · 多工具推理，正确率与调用步数。
- **关键结果 / 消融** · 正确率提高且步数减少，消融支持步级信号。
- **适用条件 / 局限** · 要求终局可判定并能采样多个分支。

**可复用机制** · 在匹配上下文内对比候选决策，把终局信号细化到步骤。

<a id="paper-151657"></a>

## PORT: Preference Optimization via Robust Token-Level Reweighting

[官方论文页](https://neurips.cc/virtual/2026/poster/151657) · [作者来源](https://openreview.net/forum?id=Z0gcomg5dI)

- **问题 / 瓶颈** · 序列级偏好无法区分内部好坏片段。
- **核心创新 / 方法** · 用 token logit 的经验 CDF 作梯度范数惩罚的前向代理。
- **Baseline** · 序列级鲁棒偏好优化。
- **Benchmark** · 不同偏好噪声设置。
- **关键结果 / 消融** · 降低梯度偏差上界，摘要称鲁棒性更高。
- **适用条件 / 局限** · 代理有效性依赖 token 表征区分噪声。

**可复用机制** · 标注污染发生在局部时，把鲁棒权重的粒度下沉到局部。

<a id="paper-155227"></a>

## PoSafeNet: Structured Safety Learning via Compositional Projection

[官方论文页](https://neurips.cc/virtual/2026/poster/155227) · [作者来源](https://openreview.net/forum?id=7K93T7me9y)

- **问题 / 瓶颈** · 固定层级和松弛把冲突语义藏进求解器。
- **核心创新 / 方法** · 用偏序描述允许的覆盖，组合控制屏障函数诱导的半空间投影。
- **Baseline** · dQP、松弛及层级安全层。
- **Benchmark** · 避障、约束操作、视觉驾驶。
- **关键结果 / 消融** · 可行性、效率和任务表现均提升，幅度未报告。
- **适用条件 / 局限** · 依赖可表达为投影的约束及事先定义的关系。

**可复用机制** · 把安全条款能否互相让步写成可审查的偏序。

<a id="paper-155020"></a>

## Pose6DAug: Physically Plausible Multi-View Object Swapping for Robot Data Augmentation

[官方论文页](https://neurips.cc/virtual/2026/poster/155020) · [作者来源](https://openreview.net/forum?id=97Qo8sjV7p)

- **问题 / 瓶颈** · 新物体依赖遥操作重采集。
- **核心创新 / 方法** · 保留成功动作，用显式网格沿 6D 位姿跨视角渲染替换物。
- **Baseline** · 现有最强基线未具名。
- **Benchmark** · 新对象和分布内操作成功率。
- **关键结果 / 消融** · 新对象相对提升 16.5%，分布内表现保持。
- **适用条件 / 局限** · 依赖标定、网格、跟踪及动作与新几何的兼容性。

**可复用机制** · 保留成功轨迹的几何锚点，只替换待泛化的因素。

<a id="paper-154017"></a>

## PoseBridge: Bridging the Skeletonization Gap for Zero-Shot Skeleton-Based Action Recognition

[官方论文页](https://neurips.cc/virtual/2026/poster/154017) · [作者来源](https://openreview.net/forum?id=GqheFyyPQn)

- **问题 / 瓶颈** · 仅用关节点丢失物体交互及视觉语义。
- **核心创新 / 方法** · 以骨架为条件连接估计器中间表示，适配类别原型。
- **Baseline** · 比较方法摘要未具名。
- **Benchmark** · NTU、PKU-MMD、Kinetics 零样本识别。
- **关键结果 / 消融** · Kinetics PURLS 八拆分提升 13.3 至 17.4 点。
- **适用条件 / 局限** · 需可接入姿态估计中间特征。

**可复用机制** · 压缩表征丢掉的语义可在上游取回，再以结构表征约束其注入。

<a id="paper-154608"></a>

## Pose-Free Feed-Forward 3D Inpainting via Learnable Mask Attention and Support Token Refinement

[官方论文页](https://neurips.cc/virtual/2026/poster/154608) · [作者来源](https://openreview.net/forum?id=CJyr8Dldh1)

- **问题 / 瓶颈** · 掩码破坏跨视角匹配且遮挡处证据不足。
- **核心创新 / 方法** · 可学掩码注意保持可靠观测，按置信度加入扩散支持 token。
- **Baseline** · 依赖预计算位姿的补全方法，未具名。
- **Benchmark** · 无位姿多视图 3D 补全。
- **关键结果 / 消融** · 摘要称质量更高且推理较快，数值未报告。
- **适用条件 / 局限** · 需参考视图及 3D 基础模型，扩散证据可能不准确。

**可复用机制** · 让观测保持空间主导，只让低证据区域吸收带置信度的生成提示。

<a id="paper-148270"></a>

## PosePlaner: Denoising Any Feedforward Pose Predictor from Pairwise Planar Geometry

[官方论文页](https://neurips.cc/virtual/2026/poster/148270) · [作者来源](https://openreview.net/forum?id=z6VEPNL9Hx)

- **问题 / 瓶颈** · 端到端位姿难在测试时从匹配证据纠偏。
- **核心创新 / 方法** · 以粗平面匹配和初始位姿为条件学习流，再融合位姿假设。
- **Baseline** · 前馈预测器与匹配求解器。
- **Benchmark** · 双视图训练、多视图流式位姿精化。
- **关键结果 / 消融** · 改善位姿和长序列漂移，幅度未报告。
- **适用条件 / 局限** · 依赖可获取粗几何匹配。

**可复用机制** · 双视图训练的几何残差模块可周期性校正多视图主网络。

<a id="paper-151605"></a>

## Positional Encoding and Prompt-Order Sensitivity in In-Context Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151605) · [作者来源](https://openreview.net/forum?id=ZJxEzyLoXN)

- **问题 / 瓶颈** · 难解释位置编码对上下文示例顺序的影响。
- **核心创新 / 方法** · 在线性注意力中分析 one-hot 与 RoPE 下排列改变引起的输出变化。
- **Baseline** · 比较两种位置编码。
- **Benchmark** · 线性回归和动力系统。
- **关键结果 / 消融** · 首阶依赖为 k/N，常数随编码、权重和任务变。
- **适用条件 / 局限** · 结论依赖线性注意力及分析任务。

**可复用机制** · 用统一扰动比例做两类顺序诊断，区分任务本身的顺序要求。

<a id="paper-151164"></a>

## Positional Encoding Is All You Need For Scalable Equivariance Constraint Relaxation

[官方论文页](https://neurips.cc/virtual/2026/poster/151164) · [作者来源](https://openreview.net/forum?id=cYC8wdYHgB)

- **问题 / 瓶颈** · 严格约束可能导致难优化，密集松弛开销大。
- **核心创新 / 方法** · 加入带可学尺度的位置编码，将位置注入退火到零。
- **Baseline** · 非等变密集层的训练松弛。
- **Benchmark** · 平移、旋转等变模型。
- **关键结果 / 消融** · 表现显著改善且算存开销较小，数值未报告。
- **适用条件 / 局限** · 验证范围限于摘要中两类对称性。

**可复用机制** · 用可撤除的位置信号替代额外密集层来探索约束外路径。

<a id="paper-148423"></a>

## Positional LSH: Binary Block Matrix Approximation for Attention with Linear Biases

[官方论文页](https://neurips.cc/virtual/2026/poster/148423) · [作者来源](https://openreview.net/forum?id=xvvSJ2zQyy)

- **问题 / 瓶颈** · 位置偏置注意力难高效分块。
- **核心创新 / 方法** · 从位置 LSH 采样分块掩码，用样本均值近似偏置。
- **Baseline** · 原始 ALiBi 注意力。
- **Benchmark** · 大语言模型长上下文及理论误差。
- **关键结果 / 消融** · 近线性复杂度，给出高概率统一输出近似。
- **适用条件 / 局限** · 摘要不支持直接外推到其他位置偏置。

**可复用机制** · 可将特定位置衰减拆为若干普通块注意力。

<a id="paper-152427"></a>

## Positional versus Symbolic Attention Heads: Learning Dynamics, RoPE Geometry, and Length Generalization

[官方论文页](https://neurips.cc/virtual/2026/poster/152427) · [作者来源](https://openreview.net/forum?id=TCB4gWgKff)

- **问题 / 瓶颈** · 结构等价的推理任务可依赖不同机制。
- **核心创新 / 方法** · 跟踪头部类型，并用 RoPE 几何与 discrepancy 分析。
- **Baseline** · 对照数字与字母多跳任务。
- **Benchmark** · GPT-J 受控实验及现实模型的长度外推。
- **关键结果 / 消融** · 符号头外推更可靠，位置头限制更强。
- **适用条件 / 局限** · 依赖受控机制定义，长文本任务迁移待验证。

**可复用机制** · 长度压力测试应检查模型依赖的是符号还是位置路径。

<a id="paper-155520"></a>

## Position-aware eXplanation: A Model-Agnostic Framework for Positional Attributions

[官方论文页](https://neurips.cc/virtual/2026/poster/155520) · [作者来源](https://openreview.net/forum?id=4zYGP89YC6)

- **问题 / 瓶颈** · 标准归因混合位置与语义。
- **核心创新 / 方法** · 将梯度、扰动及边界法扩成联合归因，并定位反事实移动效果。
- **Baseline** · 原归因方法。
- **Benchmark** · 视觉、语言及临床时序。
- **关键结果 / 消融** · 作者报告分离后两类归因都有改善。
- **适用条件 / 局限** · 移动可能改变语义，因果解释需核实。

**可复用机制** · 以保持内容的配对移位来测位置偏差，再比较特征归因。

<a id="paper-140068"></a>

## Position: Telic Errors Make VLMs Unreliable Annotators in Sensitive Contexts

[官方论文页](https://neurips.cc/virtual/2026/poster/140068) · [作者来源](https://openreview.net/forum?id=RLRpTy0ryW)

- **问题 / 瓶颈** · 准确识别画面元素并不保证理解其社会含义。
- **核心创新 / 方法** · 对照正常标注、添加自写描述及提供标签后解释。
- **Baseline** · 普通前向标注。
- **Benchmark** · 六个开权重视觉语言模型。
- **关键结果 / 消融** · 加描述下降约两点，给标签后相关含义识别达 95–100%。
- **适用条件 / 局限** · 标签可能简化推理，不同文化情境需复核。

**可复用机制** · 以分阶段到达相同任务的对照区别视觉读取和语义判断。

<a id="paper-152488"></a>

## Position Without Positional Embeddings: A Directional Mechanism in NoPE Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/152488) · [作者来源](https://openreview.net/forum?id=Sje2qgTHl2)

- **问题 / 瓶颈** · LayerNorm 可去掉方差信号所依赖的尺度。
- **核心创新 / 方法** · 解释前缀平均、句首信号及第二层输出值投影如何形成方向插值。
- **Baseline** · 基于因果注意和方差的解释。
- **Benchmark** · 两层 NoPE Transformer 的位置恢复。
- **关键结果 / 消融** · 位置可在线性方向轨迹中解码。
- **适用条件 / 局限** · 浅层机理不保证自然语料及深层一致。

**可复用机制** · 对位置探针做尺度归一和方向消融，验证信息是否独立保留。

<a id="paper-154826"></a>

## Positive-Unlabeled Preference Optimization For Chest X-ray Report Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/154826) · [作者来源](https://openreview.net/forum?id=Aecnz8LJjt)

- **问题 / 瓶颈** · 旧报告会因检查目标而省略影像异常。
- **核心创新 / 方法** · 构造提及与省略的对照响应，用正例—未标注方法更新偏好目标。
- **Baseline** · 按普通报告做偏好学习。
- **Benchmark** · 胸部 X 光报告生成；具体对照和指标待核实。
- **关键结果 / 消融** · 摘要提出降低已有发现被省略导致的训练偏差。
- **适用条件 / 局限** · 需要区分省略和真正明确否定，临床验证待查。

**可复用机制** · 对可正向验证但未明确否定的标签，避免自动构造负偏好。

<a id="paper-151721"></a>

## Post-ADC Inference: Valid Inference After Active Data Collection

[官方论文页](https://neurips.cc/virtual/2026/poster/151721) · [作者来源](https://openreview.net/forum?id=YauynQOvHf)

- **问题 / 瓶颈** · 黑盒优化主动把观测集中于有希望的区域
- **核心创新 / 方法** · 用选择性推断同时校正主动采集和数据驱动目标设计
- **Baseline** · 常规事后推断概念对照
- **Benchmark** · GP-UCB 与 TPE 采集的数据；p 值和置信区间有效性
- **关键结果 / 消融** · 两种采集方法上均报告有效推断
- **适用条件 / 局限** · 对观测噪声有假设

**可复用机制** · 不要把主动搜索记录直接当独立验证样本

<a id="paper-154341"></a>

## Posterior Alternative Calibration in Ambiguous Inverse Problems

[官方论文页](https://neurips.cc/virtual/2026/poster/154341) · [作者来源](https://openreview.net/forum?id=EKatBiU7g8)

- **问题 / 瓶颈** · 样本覆盖了所有解仍可能分配错误的频率
- **核心创新 / 方法** · 将参考后验和采样分布映射到同一预指定标签空间，比较分支概率
- **Baseline** · DDIM、DPS、DDNM、RePaint、聚类采样
- **Benchmark** · 合成歧义诊断与语义标签补全；MCE
- **关键结果 / 消融** · 部分方法找全替代解但分配概率不同
- **适用条件 / 局限** · 需要可定义的有限标签分支和后验参考

**可复用机制** · 补全、候选轨迹等任务同时测出现频率和覆盖率

<a id="paper-155188"></a>

## Posterior-First Neural PDE Simulation: Inferring Hidden Problem State from a Single Field

[官方论文页](https://neurips.cc/virtual/2026/poster/155188) · [作者来源](https://openreview.net/forum?id=7byePZP7Lo)

- **问题 / 瓶颈** · 一帧观测不足以识别模拟条件，点预测混淆多个未来
- **核心创新 / 方法** · 先以适当评分规则学习隐藏状态后验，再给下游 rollout 条件化
- **Baseline** · 直接场到未来与 oracle 标签条件
- **Benchmark** · 合成精确歧义与隐藏元数据的 PDEBench；rollout nRMSE
- **关键结果 / 消融** · 汇总 0.175 降至 0.132，弥合 59.4% 直推到 oracle 的差距
- **适用条件 / 局限** · 依赖可定义的隐藏态和训练精化标签

**可复用机制** · 单观测世界模型可把不可辨识参数显式传成概率条件

<a id="paper-151954"></a>

## Post-hoc Selective Classification for Reliable Synthetic Image Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/151954) · [作者来源](https://openreview.net/forum?id=WYncw2up3x)

- **问题 / 瓶颈** · 输出 logit 置信在合成图像检测迁移中可能失效
- **核心创新 / 方法** · 将中层表征的质心匹配转为置信分，并按风险覆盖目标组合
- **Baseline** · 常见 logit 置信评分函数
- **Benchmark** · 合成图像检测的协变量漂移；AURC
- **关键结果 / 消融** · 最高降低 69.55% AURC
- **适用条件 / 局限** · 需要取得检测器中层表征，数字属特定漂移设置

**可复用机制** · 用中间层独立证据校准固定感知器的拒答阈值

<a id="paper-153877"></a>

## POST: Progressive Object-Slot Tokenization for Multimodal Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153877) · [作者来源](https://openreview.net/forum?id=I5n7HcjMSv)

- **问题 / 瓶颈** · 平坦 patch 裁减可能丢失物体级结构
- **核心创新 / 方法** · 逐步提炼对象槽，以槽权重合并 patch，并剪去支持弱的槽
- **Baseline** · LLaVA-1.5，patch 与对象级压缩
- **Benchmark** · VOC、COCO、RefCOCO 系列及多模态基准
- **关键结果 / 消融** · 8.3% 视觉 token 预算下大多数基准相当或更优
- **适用条件 / 局限** · 依赖槽捕获对象且小物体低支持风险待验证

**可复用机制** · 按实例结构压缩 token，再测指代定位而非只测通用问答

<a id="paper-154748"></a>

## Post-Selection Distributional Model Evaluation

[官方论文页](https://neurips.cc/virtual/2026/poster/154748) · [作者来源](https://openreview.net/forum?id=BHw0wT9T0q)

- **问题 / 瓶颈** · 数据驱动预选导致常规区间失去覆盖
- **核心创新 / 方法** · 用 e-values 控制选择后错误覆盖率
- **Baseline** · 样本拆分
- **Benchmark** · 合成、LLM text-to-SQL 与电信性能；分布 KPI 区间
- **关键结果 / 消融** · 理论给出比样本拆分更省样本的条件
- **适用条件 / 局限** · 效率优势依赖论文所列条件

**可复用机制** · 对可靠性分位数或尾部指标的配置比较纳入选择后覆盖

<a id="paper-151584"></a>

## Post-Training Quantization with Gradient-Projected Fisher Approximation for Vision Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/151584) · [作者来源](https://openreview.net/forum?id=ZWDJy4JaBH)

- **问题 / 瓶颈** · 显式曲率矩阵昂贵，独立处理维度损失耦合
- **核心创新 / 方法** · 重建损失用梯度投影逼近跨维作用，并软舍入缩小离散差距
- **Baseline** · 其他 PTQ 方法，摘要未列名称
- **Benchmark** · 多种视觉任务的低比特量化
- **关键结果 / 消融** · 摘要报告领先，指标未列
- **适用条件 / 局限** · 块重建仍需校准，适用比特细节未报告

**可复用机制** · 量化重建指标可用梯度投影保留跨维信息

<a id="paper-139746"></a>

## PotARCin: Multi-Dimensional Evaluation of Skill Acquisition in Abstract Reasoning Tasks

[官方论文页](https://neurips.cc/virtual/2026/poster/139746) · [作者来源](https://openreview.net/forum?id=73Y8WKXOCP)

- **问题 / 瓶颈** · 完成标准样例未必学会可复用规则
- **核心创新 / 方法** · 同一抽象规则实现可执行生成器和验证器，拆成五种操作
- **Baseline** · 四个前沿模型的标准 ARC 评估
- **Benchmark** · ARC-AGI-1 训练任务和 P-ARC，准确率
- **关键结果 / 消融** · 标准 ARC 与拆项差 30–50 个百分点，P-ARC 各项约 0–8%
- **适用条件 / 局限** · 取决于规则生成器质量和覆盖

**可复用机制** · 验收学会技能时用同规则不同接口区分记题与可迁移求解

<a id="paper-154816"></a>

## Power Distribution Bridges Sampling, Self-Reward RL, and Self-Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/154816) · [作者来源](https://openreview.net/forum?id=AjW8i6kx9F)

- **问题 / 瓶颈** · 提升模型自信可能无助于真实表现
- **核心创新 / 方法** · 建立序列幂分布与 KL 自奖励 RL、蒸馏的联系，用教师样本做离线蒸馏
- **Baseline** · 幂采样、自奖励训练
- **Benchmark** · 推理任务及自奖励、真实奖励
- **关键结果 / 消融** · 真实收益受两种奖励对齐影响，蒸馏可匹配或超过采样
- **适用条件 / 局限** · 推断依赖序列后缀，局部幂近似不足

**可复用机制** · 先验证代理相关性，再决定以训练还是推理摊销采样成本

<a id="paper-153339"></a>

## Powering Up Zeroth-Order Training via Subspace Gradient Orthogonalization

[官方论文页](https://neurips.cc/virtual/2026/poster/153339) · [作者来源](https://openreview.net/forum?id=M4Dr8w1xjd)

- **问题 / 瓶颈** · 查询估计噪声大，弱谱向放大
- **核心创新 / 方法** · 结合低秩子空间与梯度正交化实现 ZO-Muon
- **Baseline** · MeZO
- **Benchmark** · LLM 的 SST-2 与 ViT-B 的 CIFAR-100 微调；查询量和准确率
- **关键结果 / 消融** · 达到相同 SST-2 表现只用 24.7% 查询，CIFAR-100 提升 25.1%
- **适用条件 / 局限** · 依赖低秩方向含有效任务信号

**可复用机制** · 为查询受限适配测子空间几何和达到同指标的查询预算

<a id="paper-150128"></a>

## Practical Estimation of the Bayes Optimal Fairness-Accuracy Tradeoff with Soft Labels

[官方论文页](https://neurips.cc/virtual/2026/poster/150128) · [作者来源](https://openreview.net/forum?id=kTv8UGGoPJ)

- **问题 / 瓶颈** · 难判断准确率损失是否来自任务本身。
- **核心创新 / 方法** · 用软标签和组别估计带等真阳性率约束的贝叶斯误差。
- **Baseline** · 以普通贝叶斯误差估计为出发点。
- **Benchmark** · 二分类公平性与准确率前沿；含带噪软标签。
- **关键结果 / 消融** · 证明一致性及样本界，经验估计方差较低。
- **适用条件 / 局限** · 依赖软标签和组别信息；验证集中于二分类。

**可复用机制** · 训练前用标签概率估计约束代价和剩余改进空间。

<a id="paper-150089"></a>

## Practical Non-Stationary Graph Gaussian Processes

[官方论文页](https://neurips.cc/virtual/2026/poster/150089) · [作者来源](https://openreview.net/forum?id=kmyCsFfuCm)

- **问题 / 瓶颈** · 逐节点非平稳参数容易过拟合。
- **核心创新 / 方法** · 由辅助信号和单一可学参数控制相对扩散，允许正负关系。
- **Baseline** · 平稳及高参数非平稳 GP。
- **Benchmark** · 五个真实图数据集。
- **关键结果 / 消融** · 达到或超过比较方法，证明参数 1 是唯一的平稳缩放点。
- **适用条件 / 局限** · 需要与传播相关的辅助信号，具体指标摘要未报告。

**可复用机制** · 用共享参数把历史可靠性映射到局部扩散强度。

<a id="paper-152264"></a>

## Precise but Uncoupled: Reviewer Precision Does Not Guarantee Critique Uptake in Multi-Agent Math Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/152264) · [作者来源](https://openreview.net/forum?id=UN7juOFtSR)

- **问题 / 瓶颈** · 发现错误未必改变后续候选。
- **核心创新 / 方法** · 用执行轨迹区分告警精度、采纳和修复，干预评语所在上下文。
- **Baseline** · 匹配单智能体、广播同伴、规划执行评审。
- **Benchmark** · 4181 道 Omni-MATH，分层准确率及告警精度。
- **关键结果 / 消融** · 评审精度 0.861 对 0.644 却采纳更低，强制确认反而降准确率。
- **适用条件 / 局限** · 主要为匹配的数学代理，位置干预证据为方向性。

**可复用机制** · 把评语送入求解工作上下文，并测实际改动和修复。

<a id="paper-139017"></a>

## Precise Debugging Benchmark: Is Your Model Debugging or Regenerating?

[官方论文页](https://neurips.cc/virtual/2026/poster/139017) · [作者来源](https://openreview.net/forum?id=qBuOrD12Mv)

- **问题 / 瓶颈** · 测试通过掩盖整体重写。
- **核心创新 / 方法** · 组合经验证的原子缺陷，分别计算编辑级精度和缺陷级召回。
- **Baseline** · GPT-5.1-Codex、DeepSeek-V3.2-Thinking 及迭代代理策略。
- **Benchmark** · PDB-Single 单行和 PDB-Wild 多行或仓库级修复。
- **关键结果 / 消融** · 单行修复通过率逾 76% 时精度仍低于 45%。
- **适用条件 / 局限** · 需已知合理编辑，合成缺陷未覆盖全部真实改法。

**可复用机制** · 把目标完成和无关改动拆开评估，可用于约束式编辑任务。

<a id="paper-154105"></a>

## PRECISE: SDE-Consistent Stochastic Sampling for RL Post-Training of Flow-Matching Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154105) · [作者来源](https://openreview.net/forum?id=GDousLQnYE)

- **问题 / 瓶颈** · 少步采样的额外噪声破坏去噪。
- **核心创新 / 方法** · 推导探索调度，离散化时冻结干净潜变量后验均值。
- **Baseline** · 既有随机采样器。
- **Benchmark** · 生成对齐，以 PickScore 和 HPSv2.1 等计量。
- **关键结果 / 消融** · 达到旧采样器最佳域内表现快 13.1% 至 53.2%。
- **适用条件 / 局限** · 依赖流匹配 RL 和后验近似，其他生成域待验。

**可复用机制** · 把与随机策略无关的离散化误差从探索噪声中分离。

<a id="paper-155380"></a>

## Precision As You Need: Stochastic Computing Is a Dense Adaptive Quantizer

[官方论文页](https://neurips.cc/virtual/2026/poster/155380) · [作者来源](https://openreview.net/forum?id=63tLNzOrMq)

- **问题 / 瓶颈** · 固定低位格式精度粒度有限。
- **核心创新 / 方法** · 以随机位流长度表示精度，动态为 token 或组分配长度。
- **Baseline** · 匹配位预算的固定 INT 量化。
- **Benchmark** · 分类、检测分割、生成和世界模型规划。
- **关键结果 / 消融** · 精度具竞争力，动态配置降低平均长度时更稳。
- **适用条件 / 局限** · 论文给出 GPU 软件模拟，实际专用硬件收益需测。

**可复用机制** · 将局部精度变成连续预算变量并保持运算基元一致。

<a id="paper-149371"></a>

## Precision-Aware Hopfield Retrieval: Unifying Population Codes and Memory Retrieval with Information Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/149371) · [作者来源](https://openreview.net/forum?id=qYhHysIvHY)

- **问题 / 瓶颈** · 固定读取无法利用编码位置间的不均匀信息。
- **核心创新 / 方法** · 用编码 Fisher 信息共同优化检索器，推导依赖刺激的逆温度。
- **Baseline** · 不使用编码信息的贝叶斯检索器。
- **Benchmark** · 离散联想记忆，检索损失、编码资源及回忆偏差。
- **关键结果 / 消融** · 作者推导资源和损失优势并复现中间趋势及负载效应。
- **适用条件 / 局限** · 依赖明确概率模型及编码精度可估。

**可复用机制** · 在记忆候选融合前按写入表示的局部精度调整读取锐度。

<a id="paper-155454"></a>

## Precision-Pyramid: Towards real-time neural decoding for fault-tolerant quantum computing

[官方论文页](https://neurips.cc/virtual/2026/poster/155454) · [作者来源](https://openreview.net/forum?id=5TiPghU8Xg)

- **问题 / 瓶颈** · 均匀极低位量化可能损坏判决。
- **核心创新 / 方法** · 统一二值权重，前段 INT2 激活并逐级升精度。
- **Baseline** · MWPM、Relay-BP 等。
- **Benchmark** · 表面码和 BB 码的模拟及硬件校准噪声，逻辑错误与延迟。
- **关键结果 / 消融** · 亚微秒且较经典基线逻辑错误更低。
- **适用条件 / 局限** · 实证为 FPGA 量子解码，其他模型需重测。

**可复用机制** · 资源开销集中在早期特征阶段时分段升精度，保护低成本决策层。

<a id="paper-149030"></a>

## PreCoMem: Predictive Cognitive Memory for Self-Evolving Long-Term Dialogue Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/149030) · [作者来源](https://openreview.net/forum?id=tM4m7NFSe4)

- **问题 / 瓶颈** · 覆盖或追加难区分噪声与真实变化。
- **核心创新 / 方法** · 合并语义偏差和矛盾证据，以检索置信下调，再按双阈值维护、暂存或纠正。
- **Baseline** · 常见追加及启发式覆盖。
- **Benchmark** · LoCoMo、LongMemEval、PersonaMem-v2、DiMoBench。
- **关键结果 / 消融** · 摘要称准确率及漂移适应有优势，未报告数字。
- **适用条件 / 局限** · 依赖检索可靠性和阈值校准。

**可复用机制** · 用低置信待确认状态阻止单次矛盾立即重写长期记忆。

<a id="paper-153969"></a>

## Preconditioned Flow Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/153969) · [作者来源](https://openreview.net/forum?id=H9J2nlJCjx)

- **问题 / 瓶颈** · 高方差方向先拟合，小特征值方向慢。
- **核心创新 / 方法** · 先做近各向同性可逆变换，在变换空间学流再映回。
- **Baseline** · 计算匹配基线及预条件器消融。
- **Benchmark** · 高斯、混合高斯、latent MNIST、最高 512² 图像，FID、MMD、精确率与召回。
- **关键结果 / 消融** · 改善低特征值方向恢复和图像指标，幅度未报告。
- **适用条件 / 局限** · 预条件器质量与逆变换开销会影响收益。

**可复用机制** · 把模型难训与路径病态分开，先修几何再增加容量。

<a id="paper-155272"></a>

## Preconditioned Implicit Midpoint Langevin Sampling for Non-Smooth Bayesian Imaging

[官方论文页](https://neurips.cc/virtual/2026/poster/155272) · [作者来源](https://openreview.net/forum?id=6vWdtoSoVB)

- **问题 / 瓶颈** · Euler 大步导致平稳方差膨胀。
- **核心创新 / 方法** · 隐式中点配合预条件；非光滑项用矩阵范数 Moreau 包络。
- **Baseline** · 预条件 Euler 和无预条件 IMLA。
- **Benchmark** · 高斯与全变分正则贝叶斯成像。
- **关键结果 / 消融** · 高斯任意步长方差精确，混合受有效条件数控制。
- **适用条件 / 局限** · 依赖对数凹条件，实际隐式求解成本需比较。

**可复用机制** · 在逆问题大步后验采样中并行监控混合和方差偏差。

<a id="paper-151815"></a>

## Predicting and improving test-time scaling laws via reward tail-guided search

[官方论文页](https://neurips.cc/virtual/2026/poster/151815) · [作者来源](https://openreview.net/forum?id=Xmsq17qK8L)

- **问题 / 瓶颈** · 固定 Best-of-N 不决定中间状态如何加算力。
- **核心创新 / 方法** · 估计奖励尾部，预测增加采样后最佳奖励，再自适应拨预算。
- **Baseline** · 同预算 Best-of-N，理论上对照全信息 oracle。
- **Benchmark** · 不同语言模型与奖励模型，奖励产出。
- **关键结果 / 消融** · 同算力下更高奖励，额外规律性条件下遗憾趋零。
- **适用条件 / 局限** · 奖励必须能作为目标代理，性能依赖尾部估计。

**可复用机制** · 后续采样价值取决于上尾，可按潜在峰值而非中间分数调算力。

<a id="paper-150880"></a>

## Predicting Human-Gain Curves under Local Proxy Optimization from Repeated Ratings

[官方论文页](https://neurips.cc/virtual/2026/poster/150880) · [作者来源](https://openreview.net/forum?id=ehnuc3RcGX)

- **问题 / 瓶颈** · 平均相关性看不到增益弯曲。
- **核心创新 / 方法** · 用重复人评估计 KL 邻域指数倾斜的一阶对齐和二阶修正。
- **Baseline** · 仅一阶、零收益、仅可靠性。
- **Benchmark** · SummEval、WMT MQM、OpenMEVA-MAGS、GPT-4o 裁判实验；留出收益误差。
- **关键结果 / 消融** · 预测误差下降，目标校准优于只迁移系数。
- **适用条件 / 局限** · 局部近似依赖重复标注和足够小的 KL 半径。

**可复用机制** · 把代理是否相关改为它在拟定优化强度下会带来多少人评收益。

<a id="paper-139254"></a>

## Predicting Nothing Beats SAM 3: Revisiting Evaluation in Video Object Segmentation

[官方论文页](https://neurips.cc/virtual/2026/poster/139254) · [作者来源](https://openreview.net/forum?id=briRpXpg3v)

- **问题 / 瓶颈** · 逐帧平均会奖励大量空预测。
- **核心创新 / 方法** · 以时空体积计算 J&F，降低缺席帧的奖励权重。
- **Baseline** · 传统 J&F、全空掩码、SAM 3。
- **Benchmark** · FaVOS 低可见率视频分割。
- **关键结果 / 消融** · 全空预测在传统评价可超 SAM 3，摘要未报告改进幅度。
- **适用条件 / 局限** · 不同缺席处理业务仍需单独评估。

**可复用机制** · 稀疏目标评测先加入恒空基线，再以事件或时空整体聚合。

<a id="paper-150685"></a>

## Predicting Only from Selected Evidence: A Tempered Product-of-Experts Bottleneck for Auditable EEG Diagnosis

[官方论文页](https://neurips.cc/virtual/2026/poster/150685) · [作者来源](https://openreview.net/forum?id=gGPUE5wzpp)

- **问题 / 瓶颈** · 事后解释可能回避真实预测输入。
- **核心创新 / 方法** · 将选中时空证据映成高斯专家，温度化乘积聚合，仅用受 KL 限速的潜变量分类。
- **Baseline** · 预训练 EEG 主干和代表性事后解释法。
- **Benchmark** · 六项 EEG 诊断任务，balanced accuracy 和插删、门因果及专家移除。
- **关键结果 / 消融** · 准确率有竞争力，选取忠实度审计优于比较对象。
- **适用条件 / 局限** · 需校准温度与门，实证为 EEG。

**可复用机制** · 证据选取和聚合均应有可干预瓶颈，避免用看似合理的证据替代预测证据。

<a id="paper-151631"></a>

## Predicting Plasticity in Deep Continual Learning: A Theoretical Perspective

[官方论文页](https://neurips.cc/virtual/2026/poster/151631) · [作者来源](https://openreview.net/forum?id=Z8JDztVnTJ)

- **问题 / 瓶颈** · 表征秩与 NTK 秩可能不预测可塑性。
- **核心创新 / 方法** · 结合梯度强度和可靠性构成优化准备度。
- **Baseline** · 表征秩和神经切线核秩。
- **Benchmark** · Slowly-Changing Regression、Permuted MNIST 等；训练能力排序。
- **关键结果 / 消融** · 平滑性下给出单步改进下界，少样本排序更可靠。
- **适用条件 / 局限** · 理论约束单步，需要目标任务样本。

**可复用机制** · 代理指标应直接刻画未来更新方向的稳定改进。

<a id="paper-153413"></a>

## Predicting Quantization Price for Selecting PTQ Configurations Before Deployment

[官方论文页](https://neurips.cc/virtual/2026/poster/153413) · [作者来源](https://openreview.net/forum?id=LWK4LetKST)

- **问题 / 瓶颈** · 只在固定配置族内打分难找到更优部署配置。
- **核心创新 / 方法** · 以层输出误差协方差与下游曲率的半迹量估算 forward KL 代价，再预算选择。
- **Baseline** · 重建误差和对角敏感性分数为简化代理。
- **Benchmark** · 摘要未报告实验数据或指标。
- **关键结果 / 消融** · 推导代价及选择器，未报告实证幅度。
- **适用条件 / 局限** · 二阶局部近似和校准分布代表性需检验。

**可复用机制** · 先把不同配置的误差转成同一输出漂移单位，再和实际代价共同比较。

<a id="paper-154820"></a>

## Predicting What Changes: Causal Delta World Models for Risk-Aware LLM Agent Planning

[官方论文页](https://neurips.cc/virtual/2026/poster/154820) · [作者来源](https://openreview.net/forum?id=AiYvJPM2Oy)

- **问题 / 瓶颈** · 完整画面或 HTML 预测成本高，单个价值分不解释副作用。
- **核心创新 / 方法** · 预测实体、属性和关系变动，另输出信心、不可逆代价及相关动作范围。
- **Baseline** · 完整观测预测与标量价值模型。
- **Benchmark** · 高代价交互和闭环任务；具名设置待核实。
- **关键结果 / 消融** · 摘要给出面向差量、校准和执行的联合训练目标。
- **适用条件 / 局限** · 预测不能代替权限判断，闭环净收益待查。

**可复用机制** · 验收时检查动作影响是否落在预期实体及是否能撤回。

<a id="paper-150796"></a>

## Prediction-Augmented Trees for Reliable Statistical Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/150796) · [作者来源](https://openreview.net/forum?id=fLL6UFq9R4)

- **问题 / 瓶颈** · 一个全局整流项会忽略局部系统误差。
- **核心创新 / 方法** · 自适应树分区后，用各区域的真标签残差修正估计。
- **Baseline** · 单全局校正的 PPI。
- **Benchmark** · 生态等真实数据，比较置信区间宽度。
- **关键结果 / 消融** · 摘要报告得到更紧区间。
- **适用条件 / 局限** · 叶样本不足与数据复用是否影响有效性需查。

**可复用机制** · 与全局校正比较时控制标注预算，并确认缩短区间不牺牲覆盖。

<a id="paper-155200"></a>

## Prediction-Powered Active Testing

[官方论文页](https://neurips.cc/virtual/2026/poster/155200) · [作者来源](https://openreview.net/forum?id=7YBe8ZysCG)

- **问题 / 瓶颈** · 将预测视为真标签可能产生偏差。
- **核心创新 / 方法** · 用预测作为 LURE 的控制变量，再按损失残差设计获取策略。
- **Baseline** · 既有主动测试和无控制变量的 LURE。
- **Benchmark** · 表格回归与图像分类，考察标签数、偏差、覆盖。
- **关键结果 / 消融** · 摘要报告维持无偏并用更少标签达到目标覆盖。
- **适用条件 / 局限** · 区间性质为渐近，残差代理不准时的效率待查。

**可复用机制** · 按校正后残差分配标注，而非只选模型预测置信低的样本。

<a id="paper-149115"></a>

## Prediction-Powered Inference Across Many Tasks for AI Evaluations and Social Science Research

[官方论文页](https://neurips.cc/virtual/2026/poster/149115) · [作者来源](https://openreview.net/forum?id=smHkoEf2vb)

- **问题 / 瓶颈** · 直接汇集标签会丢任务级有效性。
- **核心创新 / 方法** · 用其他任务学习代理结果，每个任务用本身真标签整流。
- **Baseline** · 逐任务 PPI 和功率调节 PPI。
- **Benchmark** · 半合成任务和大模型信息审计。
- **关键结果 / 消融** · 证明仿射跨任务重校准与原代理 oracle 等价，额外收益需要非线性结构。
- **适用条件 / 局限** · 任务可迁移性与每任务标签质量待查。

**可复用机制** · 先检查代理到真值的非线性异质，再决定跨任务共享是否值得。

<a id="paper-151013"></a>

## Predictive but Not Plannable: RC-aux for Latent World Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151013) · [作者来源](https://openreview.net/forum?id=dbTgKHgLeI)

- **问题 / 瓶颈** · 局部预测准确并不保证欧氏距离能代表可达。
- **核心创新 / 方法** · 用多视距开放预测和预算条件可达性训练，加入时间维度难负例。
- **Baseline** · 未加辅助目标的 LeWorldModel。
- **Benchmark** · 潜在模型的短期预测、长程规划和目标可达。
- **关键结果 / 消融** · 摘要将可达信号用于偏好有限预算可执行轨迹。
- **适用条件 / 局限** · 需要可达监督，复杂环境和模型外验证待查。

**可复用机制** · 以最终能到达和当前预算够得着构建配对样本，然后独立测预测和计划。

<a id="paper-155827"></a>

## Predictive Geometry of Hidden Trajectories in Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/155827) · [作者来源](https://openreview.net/forum?id=2abHWd81WV)

- **问题 / 瓶颈** · 高注意力不保证改变最终预测。
- **核心创新 / 方法** · 用剩余网络得到逐层损失，以拉回 Fisher 与矩阵无关乘积估计方向和 token 敏感性。
- **Baseline** · 注意力大小及单层局部指标。
- **Benchmark** · 含 WikiText 的多语言建模验证轨迹。
- **关键结果 / 消融** · 理论给出近似可观测方向及因果祖先外敏感度为零。
- **适用条件 / 局限** · 是局部低损失近似，较大干预及长依赖需查。

**可复用机制** · 将小扰动结果与注意力排序关联，区分读取与真正影响预测。

<a id="paper-156090"></a>

## Predict-Project-Renoise: Sampling Diffusion Models under Hard Constraints

[官方论文页](https://neurips.cc/virtual/2026/poster/156090) · [作者来源](https://openreview.net/forum?id=0RZexLnRZZ)

- **问题 / 瓶颈** · 末端投影可保持约束却破坏数据分布。
- **核心创新 / 方法** · 由去噪器估计信号，投影后用前向核重噪并重复，使过程向约束边缘逼近。
- **Baseline** · 无约束扩散及现有硬约束采样。
- **Benchmark** · 二维分布、Kuramoto–Sivashinsky 和大型全球天气。
- **关键结果 / 消融** · 摘要报告约束违规低且分布保真高。
- **适用条件 / 局限** · 投影成本和核近似误差依任务而变。

**可复用机制** · 同时验收可行性与分布，不将投影后的零违规视为质量保持。

<a id="paper-149722"></a>

## Preference Conditioned Multi-Objective Reinforcement Learning: Decomposed, Diversity-Driven Policy Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/149722) · [作者来源](https://openreview.net/forum?id=ntjuLx6iMB)

- **问题 / 瓶颈** · 过早标量化会抵消具有相反符号的优势。
- **核心创新 / 方法** · 分解 PPO 学习信号后加权，并按偏好距离奖励适量行为差异。
- **Baseline** · 早标量化的多目标强化及单一偏好策略。
- **Benchmark** · Pareto 覆盖及行为多样性；具名基准待查。
- **关键结果 / 消融** · 摘要指出信号分开可降低两类信息损失。
- **适用条件 / 局限** · 需验证目标分解、权重和监督尺度的影响。

**可复用机制** · 对正负优势冲突样本分层测梯度与前沿覆盖，隔离延迟聚合收益。

<a id="paper-154181"></a>

## Preference-Guided Adaptation for Open-Vocabulary Semantic Segmentation via Prompt Disagreement

[官方论文页](https://neurips.cc/virtual/2026/poster/154181) · [作者来源](https://openreview.net/forum?id=FcPsdOYorV)

- **问题 / 瓶颈** · 开放词汇分割逐像素标注昂贵
- **核心创新 / 方法** · 跨模板找高分歧区域，局部做偏好优化，区域外施加一致性
- **Baseline** · 不同分割骨干适配，具体方法名单未报告
- **Benchmark** · MESS，含噪声偏好设置
- **关键结果 / 消融** · 跨骨干均有提升，摘要未列数值
- **适用条件 / 局限** · 依赖提示分歧能够定位有效标注区域

**可复用机制** · 把需要标注的像素块集中到模板间争议高的位置

<a id="paper-154693"></a>

## Prefill-Guided Trace Allocation for Sample-Efficient Test-Time Scaling

[官方论文页](https://neurips.cc/virtual/2026/poster/154693) · [作者来源](https://openreview.net/forum?id=BhyoBRJYPG)

- **问题 / 瓶颈** · 固定自一致性浪费易例的解码预算
- **核心创新 / 方法** · 用前填隐藏态预测贪心轨迹可靠性，经首条验证后按难度分配候选数量
- **Baseline** · 固定四样本自一致性
- **Benchmark** · MATH-500、DeepSeek-R1-Distill-Qwen-7B 单卡；准确率、样本数、解码 token
- **关键结果 / 消融** · 维持 80.6% 准确率，样本少 48%，解码 token 少 40%
- **适用条件 / 局限** · 结果为特定模型、基准及服务设置

**可复用机制** · 预算紧时先定何时值得再采样，跨样本留出核验调度器

<a id="paper-139170"></a>

## Prefix Executability: Evaluating Tool-Using Agents Beyond Final Success

[官方论文页](https://neurips.cc/virtual/2026/poster/139170) · [作者来源](https://openreview.net/forum?id=gi2VS1WMce)

- **问题 / 瓶颈** · 任务完成会掩盖中途工具参数错误或恢复过程
- **核心创新 / 方法** · 依工具 schema、状态前提及数据依赖逐段核对，汇总首错位置与恢复率
- **Baseline** · 只评终局；加执行前计划检查作为干预
- **Benchmark** · BFCL-v3 多轮抽样及 ToolSandbox；前缀存活曲线和恢复率
- **关键结果 / 消融** · 排名出现分歧，执行前检查修复较多前缀可靠性损失
- **适用条件 / 局限** · 需要可追踪依赖和明确状态规则

**可复用机制** · 在沙盒里验收工具 Agent，加入前缀可执行性作为回归门槛

<a id="paper-151570"></a>

## PreFT: Prefill-only finetuning for inference efficiency

[官方论文页](https://neurips.cc/virtual/2026/poster/151570) · [作者来源](https://openreview.net/forum?id=ZbSJScTRJE)

- **问题 / 瓶颈** · 逐 token 个性化适配拖慢批量解码
- **核心创新 / 方法** · 将可训练适配限定于前填并提高秩以补偿 SFT 落差
- **Baseline** · 全 token PEFT
- **Benchmark** · Llama 3.1 70B 和 512 适配器吞吐，以及多任务 SFT、RL
- **关键结果 / 消融** · 吞吐 1.90 倍；RL 接近对照，SFT 损失可用更高秩补偿
- **适用条件 / 局限** · 需要支持分离前填与解码，任务影响需实测

**可复用机制** · 多租户服务在相同吞吐下比较扩大前填秩与逐步适配

<a id="paper-153705"></a>

## PREPING: Building Agent Memory without Tasks

[官方论文页](https://neurips.cc/virtual/2026/poster/153705) · [作者来源](https://openreview.net/forum?id=JOK7XgSXEU)

- **问题 / 瓶颈** · 没有真实任务历史时经验库冷启动
- **核心创新 / 方法** · 由提议者根据状态生成任务、执行者探索、验证者决定入库并反馈
- **Baseline** · 无记忆、离线或在线经验构建的 playbook
- **Benchmark** · AppWorld、BFCL v3、MCP-Universe
- **关键结果 / 消融** · 接近强经验库，前两个基准部署成本分别低约 2.99 倍、2.23 倍
- **适用条件 / 局限** · 依赖可模拟状态和有效验证器

**可复用机制** · 先控制合成任务可行性、去重和覆盖，再扩大预算

<a id="paper-154128"></a>

## Preserving Exploration for LLM Reasoning via Mean Order-Statistic Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/154128) · [作者来源](https://openreview.net/forum?id=G3nrmCAXwT)

- **问题 / 瓶颈** · 只调平均熵无法反映不同置信排名的变化
- **核心创新 / 方法** · 按每 token 词表概率排序后对各秩取平均，以 KL 约束；保留 top-K 与尾部桶
- **Baseline** · 现有探索策略，摘要未报告名称
- **Benchmark** · Countdown、六数学及两代码基准，pass@1/K
- **关键结果 / 消融** · 发现更多不同可行解，两类通过率均升，最大模型 32B
- **适用条件 / 局限** · 排序消除了具体 token 身份，无法直接约束语义多样性

**可复用机制** · 需要维持解法多样性时，对照秩谱目标与熵目标

<a id="paper-148179"></a>

## Pretext Reasoning: Scaling the Building Blocks of Interleaved Multimodal Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/148179) · [作者来源](https://openreview.net/forum?id=zhyLVCaMI0)

- **问题 / 瓶颈** · 端到端任务轨迹难单独学会中间图像读写
- **核心创新 / 方法** · 两阶段构造思考—图像—思考的视觉自监督轨迹及任务级视觉状态训练
- **Baseline** · 同预算 BAGEL
- **Benchmark** · 感知、空间理解、心理世界建模三类指标
- **关键结果 / 消融** · 7B 模型比分别增 10.40、5.93、15.70，轨迹更短
- **适用条件 / 局限** · 依赖统一多模态生成读取能力与训练数据构造

**可复用机制** · 把空间推理所需画图、读图拆为前置技能，然后测组合任务转移

<a id="paper-151759"></a>

## Pretraining Data Statistics Shape the Phases of Learning Entity Comparison in Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151759) · [作者来源](https://openreview.net/forum?id=YFAKZxppJB)

- **问题 / 瓶颈** · 早期比较任务可能靠实体频率捷径
- **核心创新 / 方法** · 改变实体样本频率和证据量，追踪规则学习阶段并核对 OLMo
- **Baseline** · Zipf 对均匀；不同证据量
- **Benchmark** · 合成实体比较与 OLMo 训练记录
- **关键结果 / 消融** · 均匀设定首个阶段消失，大量证据时跳过中间阶段
- **适用条件 / 局限** · 规律主要来自实体比较，迁移到其他捷径需对照

**可复用机制** · 组训练样本时做均衡和自然分布对照，监测是否学习捷径

<a id="paper-150570"></a>

## Prevailing Bisimulation Metric Learning Is Biased: Implicit Regularization and Its Remedy

[官方论文页](https://neurips.cc/virtual/2026/poster/150570) · [作者来源](https://openreview.net/forum?id=hB5eZI6Iyp)

- **问题 / 瓶颈** · 常用目标混入转移噪声并可导致不收敛
- **核心创新 / 方法** · 以原始—对偶形式和辅助网络估计期望 Bellman 误差
- **Baseline** · 代表性样本双模拟基线
- **Benchmark** · 随机连续及离散控制、视觉干扰；控制表现与收敛
- **关键结果 / 消融** · 高噪环境改善尤其明显，摘要未给幅度
- **适用条件 / 局限** · 依赖辅助网络可靠估计与相应随机设置

**可复用机制** · 先用受控转移噪声区分距离估计错误和控制器失败

<a id="paper-149654"></a>

## Preventing Error Cascades in Long-Horizon Multimodal Agents with Edge-Reliability Graph Memory

[官方论文页](https://neurips.cc/virtual/2026/poster/149654) · [作者来源](https://openreview.net/forum?id=oSvwY9Jnn1)

- **问题 / 瓶颈** · 早期工具错误被写入记忆并传播
- **核心创新 / 方法** · 把跨时刻复用组织为稀疏图，学习边可靠度并据此校正
- **Baseline** · 可靠性和记忆增强的强基线
- **Benchmark** · 11 项多模态任务；干预和人工标注验证
- **关键结果 / 消融** · 干预相关 0.71，人工标注 ROC-AUC 0.94；噪声长程胜过对照
- **适用条件 / 局限** · 结果监督为相关代理，清洁感知收益未显示

**可复用机制** · 对证据来源、传递和二次引用分别评估可靠性

<a id="paper-153837"></a>

## PriFT: Prior-Support Guided Token Reweighting for Supervised Fine-Tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/153837) · [作者来源](https://openreview.net/forum?id=ILf5dWUdsd)

- **问题 / 瓶颈** · 在线学习改变权重依据并造成不稳定参考
- **核心创新 / 方法** · 用微调前目标 token 概率或相对支持集合重加权
- **Baseline** · 同样加权或选择规则的在线统计实现
- **Benchmark** · 数学、代码、医学问答，含后续 RL 初始化
- **关键结果 / 消融** · 换固定先验后多种规则持续改善，摘要未给数值
- **适用条件 / 局限** · 需要基座分布，偏低支持的必要知识如何处理需核验

**可复用机制** · 把数据加权标准固定成外生分数，与在线难度策略做匹配对照

<a id="paper-151600"></a>

## Primal-Dual Representation Learning for Low-Rank Constrained MDPs

[官方论文页](https://neurips.cc/virtual/2026/poster/151600) · [作者来源](https://openreview.net/forum?id=ZKslJI2cOt)

- **问题 / 瓶颈** · 低秩连续 CMDP 需要在学习特征时控制违规。
- **核心创新 / 方法** · 衰减探索和最大似然估计特征，以不确定性奖励做拉格朗日规划，硬约束用保守证书。
- **Baseline** · 区分软累计和硬累计约束。
- **Benchmark** · 理论分析回报及违规界。
- **关键结果 / 消融** · 回报策略界约为根号 K，计探索总体样本界约 K 的 3/4 次方。
- **适用条件 / 局限** · 依赖低秩与证书条件。

**可复用机制** · 用同一特征置信界把探索、回报和安全验证拆成可审计环节。

<a id="paper-152535"></a>

## Primal Generation, Dual Judgment: Self-Training from Test-Time Scaling

[官方论文页](https://neurips.cc/virtual/2026/poster/152535) · [作者来源](https://openreview.net/forum?id=SQVg5yUdpq)

- **问题 / 瓶颈** · 单候选的执行反馈稀疏。
- **核心创新 / 方法** · 只保留成功与失败兼具的组，用 GRPO 训练模型区分候选。
- **Baseline** · 原始模型的 Best-of-4。
- **Benchmark** · LiveCodeBench，两个家族、五个 4B 至 30B 模型。
- **关键结果 / 消融** · Best-of-4 一致改善。
- **适用条件 / 局限** · 依赖可信的可执行验证与正负并存采样。

**可复用机制** · 训练候选评判器也可间接提高候选生成。

<a id="paper-153567"></a>

## PRIME: A Modular Approach for Private Synthetic Data

[官方论文页](https://neurips.cc/virtual/2026/poster/153567) · [作者来源](https://openreview.net/forum?id=KQh9ulA7J7)

- **问题 / 瓶颈** · 高树宽使图模型合成不可计算。
- **核心创新 / 方法** · 把合成限制在 K 个候选支持点，凸优化其权重匹配测量。
- **Baseline** · PrivatePGM，接入 ResidualPlanner 或 AIM+GReM。
- **Benchmark** · 差分隐私表格合成，比较测量误差和稠密查询可行性。
- **关键结果 / 消融** · 每迭代 O(K×测量数)；相同测量下误差相近。
- **适用条件 / 局限** · 覆盖欠佳的支持集限制效果；支持构造须遵守隐私约束。

**可复用机制** · 把隐私测量与后端生成解耦，用可审计支持集控制复杂度。

<a id="paper-154522"></a>

## PRIME: Poincaré return induced measure for learning partially observed dynamical systems

[官方论文页](https://neurips.cc/virtual/2026/poster/154522) · [作者来源](https://openreview.net/forum?id=CzBDTAXvts)

- **问题 / 瓶颈** · 逐点 MSE 诱导收缩，静态不变分布缺时序。
- **核心创新 / 方法** · 对回归块的诱导返回映射匹配经验图测度。
- **Baseline** · 逐点 MSE 和不变测度匹配。
- **Benchmark** · 部分观测 Lorenz63、Kuramoto–Sivashinsky 及圆柱绕流。
- **关键结果 / 消融** · 缓解拓扑坍缩，改善时序和几何或频谱。
- **适用条件 / 局限** · 需要可估计复现事件。

**可复用机制** · 用重复进入局部区域的转移约束替代不稳定的精确轨迹配对。

<a id="paper-150891"></a>

## PRIM: Meta-Learned Bayesian Root Cause Analysis

[官方论文页](https://neurips.cc/virtual/2026/poster/150891) · [作者来源](https://openreview.net/forum?id=edcYZi5wbN)

- **问题 / 瓶颈** · 测试时结构未知，重新拟合昂贵。
- **核心创新 / 方法** · 从合成因果模型先验训练联合看正常和异常数据的 Transformer。
- **Baseline** · 已知图和未知图 RCA 方法。
- **Benchmark** · 合成基准、PetShop、CausRCA。
- **关键结果 / 消融** · 最多 100 变量约 17 ms，未知图任务多项改善。
- **适用条件 / 局限** · 依赖合成先验覆盖目标机制。

**可复用机制** · 当运行时必须快速定位机制变化时，将多种候选因果结构预先边缘化。
