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
