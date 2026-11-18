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
