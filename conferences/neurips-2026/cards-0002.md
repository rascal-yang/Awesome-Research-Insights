# NeurIPS 2026 论文卡 2

[会议索引](README.md)

<a id="paper-155024"></a>

## ATLAS: Agentic or Latent Visual Reasoning? One Word is Enough for Both

[官方论文页](https://neurips.cc/virtual/2026/poster/155024) · [作者来源](https://openreview.net/forum?id=96LglEyISE)

- **问题 / 瓶颈** · 外部工具切换慢而隐向量难复用
- **核心创新 / 方法** · 同一词元代表内部视觉操作并参与下一词训练
- **Baseline** · 外部工具与连续隐推理
- **Benchmark** · 视觉推理任务；基准细项待核
- **关键结果 / 消融** · 提出统一操作接口；具体增益待核
- **适用条件 / 局限** · 取决于可用操作集合

**可复用机制** · 固定操作集合比较离散内部操作和外部调用的质量与延迟。

<a id="paper-150816"></a>

## AtlasULP: Domain-aware Universal Link Prediction via Relation Atlas

[官方论文页](https://neurips.cc/virtual/2026/poster/150816) · [作者来源](https://openreview.net/forum?id=f8yctrr8CX)

- **问题 / 瓶颈** · 高阶邻域难直接扩展且不同图域信号不同
- **核心创新 / 方法** · 通用链路预测通过关系图谱引入领域结构
- **Baseline** · 基于子图采样的通用链路预测
- **Benchmark** · 未见图链路预测
- **关键结果 / 消融** · 精确数据与指标待复核
- **适用条件 / 局限** · 图谱对未见结构的覆盖限制迁移

**可复用机制** · 在未见图上控制采样预算比较关系图谱与局部表示。

<a id="paper-150426"></a>

## AtlasVid: Efficient Ultra-High-Resolution Long Video Generation via Decoupled Global-Local Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/150426) · [作者来源](https://openreview.net/forum?id=i7HwynFyoG)

- **问题 / 瓶颈** · 长单镜头高分视频需要兼顾一致性和局部细节
- **核心创新 / 方法** · 缩放时间位置编码生成低帧率全局代理，再用局部模型生成高分细节
- **Baseline** · 直接高分扩散及分段拼接路线
- **Benchmark** · 高分长单镜头生成
- **关键结果 / 消融** · 质量与耗时细节待核
- **适用条件 / 局限** · 全局代理漏掉快速运动时局部难补

**可复用机制** · 把全局一致性和局部纹理分开评估。

<a id="paper-152217"></a>

## AtmoZero: Self-Play Post-Training for Caption-Free Weather Time-Series Captioning

[官方论文页](https://neurips.cc/virtual/2026/poster/152217) · [作者来源](https://openreview.net/forum?id=Ugpq0GTKKc)

- **问题 / 瓶颈** · 相似度奖励无法区分描述正确与被实际天气记录否定
- **核心创新 / 方法** · 无人工描述的自博弈后训练结合七项站点可观测验证和显式反驳通道
- **Baseline** · 相似度及下游任务奖励路线
- **Benchmark** · 天气多变量时序描述
- **关键结果 / 消融** · 分项验证和结果幅度待核
- **适用条件 / 局限** · 停留在站点能检验的陈述

**可复用机制** · 在科学文本生成中分别奖励证实和惩罚可验证的矛盾。

<a id="paper-149909"></a>

## AtomMOF: All-Atom Flow Matching for MOF-Adsorbate Structure Prediction

[官方论文页](https://neurips.cc/virtual/2026/poster/149909) · [作者来源](https://openreview.net/forum?id=mJ3KktOdtZ)

- **问题 / 瓶颈** · 单独固定宿主难表达材料与吸附质共同变化
- **核心创新 / 方法** · 在全原子空间联合预测，以建筑块关系作为注意力偏置，并用材料势约束结构
- **Baseline** · 刚体生成及已知宿主条件的传统路线
- **Benchmark** · BW 材料结构集
- **关键结果 / 消融** · 摘要描述模型扩展趋势；具体幅度待核
- **适用条件 / 局限** · 取决于势函数适用范围

**可复用机制** · 材料结构筛选时分开报告宿主变化、联合结构有效性和计算成本。

<a id="paper-153440"></a>

## Atoms and Pivot Based Correlation Clustering

[官方论文页](https://neurips.cc/virtual/2026/poster/153440) · [作者来源](https://openreview.net/forum?id=LICZTK9DS7)

- **问题 / 瓶颈** · 经典 pivot 最坏情形集中于强团结构
- **核心创新 / 方法** · 证明达到最坏近似比须在原子组上犯错，并据此修改 pivot
- **Baseline** · 经典三近似 pivot 算法
- **Benchmark** · 相关聚类理论；目标为边与非边的划分分歧
- **关键结果 / 消融** · 最坏情形与原子错误存在联系；新比率待全文核对
- **适用条件 / 局限** · 依赖原子识别及理论设定

**可复用机制** · 分析近似算法时定位最坏误差集中在哪类结构上。

<a id="paper-155270"></a>

## AtomWorld-Mem: Memory-Restored World States for Long-Horizon Atomistic Evolution

[官方论文页](https://neurips.cc/virtual/2026/poster/155270) · [作者来源](https://openreview.net/forum?id=6wc2BIP9Oe)

- **问题 / 瓶颈** · 相近构型可对应不同演化驱动力
- **核心创新 / 方法** · 编码局部拓扑和长程缺陷的关键帧，以短期事件及长期结构记忆预测演化
- **Baseline** · 只看当前快照的预测路线
- **Benchmark** · 合金长时演化；实验设置待核
- **关键结果 / 消融** · 记忆贡献与结果幅度待核
- **适用条件 / 局限** · 依赖历史轨迹和可辨识缺陷

**可复用机制** · 用相似快照但历史不同的样本诊断记忆是否有益。

<a id="paper-151161"></a>

## A Topological Encoder Decoder Framework for Temporal Graph Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151161) · [作者来源](https://openreview.net/forum?id=cZEj9pgOP7)

- **问题 / 瓶颈** · 只在持久节点集合上做判别难测节点变化
- **核心创新 / 方法** · 预测未来多尺度拓扑描述，再在归纳约束下重建图
- **Baseline** · 时序图预测模型
- **Benchmark** · 14 个时序图数据集，节点、边和图属性任务
- **关键结果 / 消融** · 作者报告性能改善，分任务数值待核
- **适用条件 / 局限** · 拓扑描述不唯一确定图

**可复用机制** · 图区分节点进入或退出和持久节点场景，再对比边预测。

<a id="paper-154767"></a>

## A Topological Sorting Criterion for Random Causal Directed Acyclic Graphs

[官方论文页](https://neurips.cc/virtual/2026/poster/154767) · [作者来源](https://openreview.net/forum?id=B65Mjlgily)

- **问题 / 瓶颈** · 常用合成图可能让因果排序过于简单
- **核心创新 / 方法** · 在随机 DAG 中分析开放路径可达亲缘数的单调性，构建计数排序对照
- **Baseline** · 基于随机 DAG 的因果发现评测
- **Benchmark** · Erdős–Rényi 与无标度 DAG 的数值检验
- **关键结果 / 消融** · 严格单调时马尔可夫等价类为单元素
- **适用条件 / 局限** · 结论依赖图生成过程

**可复用机制** · 合成基准报告结构捷径，并增加时间序列图对照。

<a id="paper-149512"></a>

## A Training-Free Video Moment Retrieval Framework via Selection from Multiple Visual Prompts

[官方论文页](https://neurips.cc/virtual/2026/poster/149512) · [作者来源](https://openreview.net/forum?id=paLWDpXw1a)

- **问题 / 瓶颈** · 多种视觉标记叠加可能让边界和物体更难辨认
- **核心创新 / 方法** · 分开使用事件分段、检测和关键帧标记，再选择候选
- **Baseline** · 原始视频与直接融合标记
- **Benchmark** · 文本查询定位视频片段
- **关键结果 / 消融** · 摘要称各提示单独可改善而直接混合变差
- **适用条件 / 局限** · 依赖选择器可识别错误标记

**可复用机制** · 固定模型比较选一种提示、混合提示与不加提示。

<a id="paper-153148"></a>

## A Transformer-Derived Iterative Preconditioner

[官方论文页](https://neurips.cc/virtual/2026/poster/153148) · [作者来源](https://openreview.net/forum?id=NW9Z1nrWSP)

- **问题 / 瓶颈** · 黑盒学习式求解器难解释和复用
- **核心创新 / 方法** · 通过逐层对称干预抽出 Gram 矩阵合同变换，并以快速随机混合和稀疏更新实现
- **Baseline** · 共轭梯度和无预条件求解
- **Benchmark** · 显式对称正定线性系统，比较条件数与求解时间
- **关键结果 / 消融** · 每个迭代前缀都形成有效预条件；实际提速待核
- **适用条件 / 局限** · 适用显式 SPD 系统

**可复用机制** · 对时限任务比较不同迭代预算的预处理成本与求解收益。

<a id="paper-149517"></a>

## A Trust Region Approach for Learning Schrödinger Bridges

[官方论文页](https://neurips.cc/virtual/2026/poster/149517) · [作者来源](https://openreview.net/forum?id=pXZ4KjVpoE)

- **问题 / 瓶颈** · 目标远离初始化时比例拟合可能数值不稳
- **核心创新 / 方法** · 用固定 KL 信赖域限制相邻更新，可解释为自适应步长镜像下降
- **Baseline** · 经典 IPF 及变体
- **Benchmark** · 多个采样任务；具名案例待核
- **关键结果 / 消融** · 作者报告稳定性改善；掉稳比例待核
- **适用条件 / 局限** · 依赖密度访问和 KL 约束求解

**可复用机制** · 比较远初始化时的失稳率及收敛成本，而非只比较最后误差。

<a id="paper-149152"></a>

## AT-SKM-Net: An Accelerated Trainable Sampling Kaczmarz-Motzkin Framework for Linear Hard-Constraint Feasibility on Dynamic Graphs

[官方论文页](https://neurips.cc/virtual/2026/poster/149152) · [作者来源](https://openreview.net/forum?id=sSAcXhJXvH)

- **问题 / 瓶颈** · 每次扫全部约束并重新分解昂贵
- **核心创新 / 方法** · 图感知混合采样聚焦活跃约束，Cholesky 更新处理低秩拓扑变化
- **Baseline** · T-SKM-Net 和重新分解路线
- **Benchmark** · 动态随机几何图；详细指标待核
- **关键结果 / 消融** · 作者给出低秩扰动下等式投影从三次到二次复杂度
- **适用条件 / 局限** · 扰动须足够低秩

**可复用机制** · 将约束选择与投影复用分开消融，记录真正达到可行的耗时。

<a id="paper-154201"></a>

## Attending on Attention ($A^2$): Smaller Self-Supervised ViTs Localize Better Than Larger Ones

[官方论文页](https://neurips.cc/virtual/2026/poster/154201) · [作者来源](https://openreview.net/forum?id=FS61bwr6ZM)

- **问题 / 瓶颈** · 更大骨干的特征强但其注意力定位未必更准
- **核心创新 / 方法** · 用小型自监督 ViT 的注意力峰做裁剪，再用大模型嵌入
- **Baseline** · 骨干匹配的 DFR 及端到端注意力训练
- **Benchmark** · 五个含前景与干扰物的基准
- **关键结果 / 消融** · 作者报告小模型定位更稳，强干扰下组合效果更好
- **适用条件 / 局限** · 空间可分离的干扰物更适用

**可复用机制** · 独立验证定位和嵌入两个模块的规模收益。

<a id="paper-154730"></a>

## Attend Locally, Remember Linearly: Linear Attention as Cross-Frame Memory for Autoregressive Video Diffusion

[官方论文页](https://neurips.cc/virtual/2026/poster/154730) · [作者来源](https://openreview.net/forum?id=BScHl5MZ8h)

- **问题 / 瓶颈** · 跨帧 KV 缓存随时长增加
- **核心创新 / 方法** · 将扩散注意力拆为帧内空间分支和门控循环线性记忆
- **Baseline** · 稀疏注意力和 KV 压缩路线
- **Benchmark** · 自回归视频扩散的长序列生成
- **关键结果 / 消融** · 跨帧状态不随视频长度增长；质量结果待核
- **适用条件 / 局限** · 长期小状态可能遗忘细节

**可复用机制** · 比较不同视频时长下显存、跨帧一致性和细节质量。

<a id="paper-155371"></a>

## Attention Alignment Between Humans and Vision-Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155371) · [作者来源](https://openreview.net/forum?id=6839tYClgV)

- **问题 / 瓶颈** · 模型注意力与人注视差异不能仅归因于视觉骨干
- **核心创新 / 方法** · 用编码器和解码器交叉组合，与两种任务下的人类注视热图对照
- **Baseline** · CNN、ViT 和 LSTM、Transformer 组合，另含 Molmo 和 Qwen
- **Benchmark** · 200 张图像，通用描述与社交描述，以人类噪声上限归一
- **关键结果 / 消融** · LSTM 与 Transformer 解码器相差约 40–50 个百分点
- **适用条件 / 局限** · 样本较小，注意力对齐不代表任务质量

**可复用机制** · 切换架构时在相同图与任务上分别比较注意图与输出表现。

<a id="paper-149497"></a>

## Attention as In-Context Empirical Bayes: A Two-Stage View via Particle Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/149497) · [作者来源](https://openreview.net/forum?id=pgcuFj2z7T)

- **问题 / 瓶颈** · 全 token 噪声下两种作用难区分。
- **核心创新 / 方法** · 用粒子动力学精炼经验先验，长跳连保留带噪查询，注意力求核后验均值。
- **Baseline** · 单步核估计与贝叶斯最优预测。
- **Benchmark** · 最小注意力网络的理论去噪设定。
- **关键结果 / 消融** · 固定带宽与有限积分可去噪，特定先验下渐近恢复后验均值。
- **适用条件 / 局限** · 最小模型及正则先验。

**可复用机制** · 以固定噪声扫描深度并消融长跳连。

<a id="paper-154448"></a>

## Attention-based PCA

[官方论文页](https://neurips.cc/virtual/2026/poster/154448) · [作者来源](https://openreview.net/forum?id=DTfQiEFRDM)

- **问题 / 瓶颈** · 无监督注意力学到何种统计量不明确。
- **核心创新 / 方法** · 分析 softmax 和线性注意力最优参数与协方差特征方向的关系。
- **Baseline** · 经典 PCA 方向及两种注意力形式。
- **Benchmark** · 有限和无限高斯提示、尖峰 Wishart 协方差。
- **关键结果 / 消融** · 无限提示最优解对齐领先方向，有限提示有采样偏差。
- **适用条件 / 局限** · 依赖高斯与尖峰等分析假设。

**可复用机制** · 用主特征向量夹角诊断上下文长度的影响。

<a id="paper-153811"></a>

## Attention-Based Pretraining for Unsupervised Amortized Causal Discovery

[官方论文页](https://neurips.cc/virtual/2026/poster/153811) · [作者来源](https://openreview.net/forum?id=IWyVTvkGab)

- **问题 / 瓶颈** · 逐域 DAG 求解代价高且少样本不稳。
- **核心创新 / 方法** · 线性 Transformer 从观察样本映射到图和结构方程参数，注意力可解释为不动点迭代。
- **Baseline** · 逐域无监督 DAG 学习。
- **Benchmark** · 合成及现实型基准，名称待核。
- **关键结果 / 消融** · 作者报告精度与效率改善，少样本更明显。
- **适用条件 / 局限** · 依赖跨域知识与结构方程假设。

**可复用机制** · 在留出方程参数的域测试冻结求解器。

<a id="paper-152519"></a>

## Attention-based Routing for Interpretable Multimodal Brain Encoding

[官方论文页](https://neurips.cc/virtual/2026/poster/152519) · [作者来源](https://openreview.net/forum?id=SWM0cCjlXg)

- **问题 / 瓶颈** · 不同脑区使用的视觉听觉语言线索不相同。
- **核心创新 / 方法** · 可学习脑区查询交叉注意各模态，再线性预测不同分辨率响应。
- **Baseline** · 静态聚合与线性读出，具名对照待核。
- **Benchmark** · 自然视频观看的脑区及体素 fMRI，含分布外刺激。
- **关键结果 / 消融** · 作者报告准确预测并跨刺激泛化。
- **适用条件 / 局限** · 注意力模式是描述性证据。

**可复用机制** · 在同一骨干下比较共享融合与脑区条件路由。

<a id="paper-149963"></a>

## Attention-Based Sampler for Diffusion Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149963) · [作者来源](https://openreview.net/forum?id=lspyzSyqOj)

- **问题 / 瓶颈** · 逐 token 置信度忽略全局依赖。
- **核心创新 / 方法** · 从似然排序的困难问题导出秩近似，并以动态注意力阈值实现训练免调采样。
- **Baseline** · 贪心及 token 局部排序。
- **Benchmark** · 多个生成基准，名称待核。
- **关键结果 / 消融** · 作者报告生成质量与并行性改善。
- **适用条件 / 局限** · 最优性针对近似目标。

**可复用机制** · 固定去噪次数比较置信度排序与注意力排序。

<a id="paper-151077"></a>

## Attention-Based Soft Answer Sets

[官方论文页](https://neurips.cc/virtual/2026/poster/151077) · [作者来源](https://openreview.net/forum?id=d7gqN6IVHL)

- **问题 / 瓶颈** · 外部求解器阻断端到端优化。
- **核心创新 / 方法** · 在有限符号概率分布上提升 ASP 直接后果算子，以约束组嵌入给出位置结构。
- **Baseline** · 神经与离散求解流水线。
- **Benchmark** · Visual Sudoku、CLEVR-Hans3/7。
- **关键结果 / 消融** · 数独单元准确率 99.89%，约束满足率 100%；后两项准确率 99.94% 和 87.77%。
- **适用条件 / 局限** · 其他约束规模和规则的迁移待核。

**可复用机制** · 同时报告预测正确率和约束满足率。

<a id="paper-150267"></a>

## Attention-Discounted Adaptive Sampler for Masked Diffusion Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150267) · [作者来源](https://openreview.net/forum?id=jRWyysR7NV)

- **问题 / 瓶颈** · 单点置信度不能保证联合提交可靠。
- **核心创新 / 方法** · 保留停止规则，仅用连续注意力惩罚做贪心重排。
- **Baseline** · Top-k、Fast-dLLM、EB-Sampler。
- **Benchmark** · LLaDA-8B-Base、Dream-7B-Base 上的数学与代码任务。
- **关键结果 / 消融** · 匹配去噪次数时作者报告低步数平均增益 9.11 和 10.46 个百分点，前向开销约 3.1%。
- **适用条件 / 局限** · 依赖注意力反映耦合。

**可复用机制** · 固定停止策略单独测试候选重排。

<a id="paper-152952"></a>

## Attention Drift: What Auto-Regressive Speculative Decoding Models Learn

[官方论文页](https://neurips.cc/virtual/2026/poster/152952) · [作者来源](https://openreview.net/forum?id=P9bn0DEION)

- **问题 / 瓶颈** · 草稿链越长越偏向最近自生成 token。
- **核心创新 / 方法** · 定位未归一化残差增长，并对草稿与捕获目标状态做归一化。
- **Baseline** · 预归一化 EAGLE3，另观察 MTP。
- **Benchmark** · 模板扰动、长上下文与七项标准基准。
- **关键结果 / 消融** · 接受长度最高分别达对照的 2、1.18、1.10 倍。
- **适用条件 / 局限** · 接受长度与端到端加速应分别核算。

**可复用机制** · 按链深度记录范数与提示注意力，再评估归一化。

<a id="paper-149428"></a>

## Attention Heads are Complementary Visual Units: Mitigating Hallucinations in LVLMs via Adaptive Visual Cues Focusing

[官方论文页](https://neurips.cc/virtual/2026/poster/149428) · [作者来源](https://openreview.net/forum?id=q8PFA0lviK)

- **问题 / 瓶颈** · 跨头平均可能抹掉互补图像线索。
- **核心创新 / 方法** · 按头去冗余，用距离衰减减少局部文本偏置并重分配注意。
- **Baseline** · 现有视觉语言幻觉缓解方法。
- **Benchmark** · 多个模型和基准，细项待核。
- **关键结果 / 消融** · 作者报告幻觉减少且开销可忽略。
- **适用条件 / 局限** · 注意权重不是因果证据。

**可复用机制** · 对照逐头选线索与跨头聚合。

<a id="paper-155116"></a>

## Attention Is More Than You Need: Spectral Redundancy in Multi-Head Routing

[官方论文页](https://neurips.cc/virtual/2026/poster/155116) · [作者来源](https://openreview.net/forum?id=8I6ozAPipF)

- **问题 / 瓶颈** · 共享键值不保证查询头路由可合并。
- **核心创新 / 方法** · 给出最坏情形下界，并用校准谱分开评估不同可实现压缩。
- **Baseline** · 逐头计算与共享路由近似。
- **Benchmark** · 四个模型族的 14 个 GQA 检查点。
- **关键结果 / 消融** · 八条路线在所测模型中保留超过 90% 路由能量。
- **适用条件 / 局限** · 谱能量不等于精度或实际加速。

**可复用机制** · 在压缩前测路由谱与端到端质量。

<a id="paper-150300"></a>

## Attention Itself Could Retrieve. RetrieveVGGT: Training-Free Long Context Streaming 3D Reconstruction via Query-Key Similarity Retrieval

[官方论文页](https://neurips.cc/virtual/2026/poster/150300) · [作者来源](https://openreview.net/forum?id=jAIfluCaNL)

- **问题 / 瓶颈** · 流式缓存随帧数增长。
- **核心创新 / 方法** · 加分段采样和按估计姿态组织的历史检索。
- **Baseline** · StreamVGGT、TTT3R、InfiniteVGGT。
- **Benchmark** · 长序列三维重建及内存。
- **关键结果 / 消融** · 作者报告优于所比方法，内存不随序列长度增长。
- **适用条件 / 局限** · 姿态误差及长期历史存储细节待核。

**可复用机制** · 固定上下文预算对照最近帧与多段检索。

<a id="paper-148314"></a>

## Attention Sinks and Outliers in Attention Residuals

[官方论文页](https://neurips.cc/virtual/2026/poster/148314) · [作者来源](https://openreview.net/forum?id=yjVSLVS0Dh)

- **问题 / 瓶颈** · 深度归一化可能加剧注意力汇聚与激活异常。
- **核心创新 / 方法** · 用 Softmax1 空间把 token 的空证据传到层间路由。
- **Baseline** · 五种对照，名称待核。
- **Benchmark** · 三个数据集及 W8A8/W4A4。
- **关键结果 / 消融** · 摘要报告最大无穷范数平均降 9.26%，另有量化表现改善。
- **适用条件 / 局限** · 量化与训练条件需核对。

**可复用机制** · 测异常激活及量化任务表现的联动。

<a id="paper-153587"></a>

## Attention Sinks as Spectral Spikes: A Mechanism Analysis of Gated Attention

[官方论文页](https://neurips.cc/virtual/2026/poster/153587) · [作者来源](https://openreview.net/forum?id=KJKRoPhwQg)

- **问题 / 瓶颈** · 只看注意力占比不足以追踪表示与反传。
- **核心创新 / 方法** · 将 sink 建模为 token 协方差低秩模态，分析门控的收缩。
- **Baseline** · 门控与未门控注意力。
- **Benchmark** · 随机矩阵、值路径梯度和训练期诊断。
- **关键结果 / 消融** · 门控降低异常谱能量并减弱首 token 值梯度。
- **适用条件 / 局限** · 结果针对所测门控位置。

**可复用机制** · 同时监控有效秩与梯度集中度。

<a id="paper-151217"></a>

## Attention Sinks Induce Gradient Sinks: Massive Activations as Gradient Regulators in Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/151217) · [作者来源](https://openreview.net/forum?id=c49EUKrp1G)

- **问题 / 瓶颈** · 前向解释忽略 RMSNorm 在反传中的调节。
- **核心创新 / 方法** · 分析因果掩码下的梯度集中，用 V-scale 定向调节值路径。
- **Baseline** · 标准预归一化 Transformer。
- **Benchmark** · 理论和训练干预，基准细节待核。
- **关键结果 / 消融** · 保留注意力汇聚的同时压制大激活。
- **适用条件 / 局限** · 依赖因果掩码及所测归一化。

**可复用机制** · 将前向汇聚与梯度因果干预分开。

<a id="paper-156756"></a>

## Attention Trajectories as a Diagnostic Axis for Deep Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/156756) · [作者来源](https://openreview.net/forum?id=0aa9zthk7k)

- **问题 / 瓶颈** · 最终回报掩盖捷径和冗余通道依赖。
- **核心创新 / 方法** · 聚合显著图并对照行为与多种显著性方法。
- **Baseline** · 不同算法、受控设置和显著性工具。
- **Benchmark** · Atari、Pong 和视觉运动模拟。
- **关键结果 / 消融** · 发现算法偏差、非预期奖励行为和冗余过拟合。
- **适用条件 / 局限** · 显著性仍需行为干预验证。

**可复用机制** · 每阶段同时记录表征依赖和行为变化。

<a id="paper-156052"></a>

## Attention Transfer Is Not Universally Effective for Vision Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/156052) · [作者来源](https://openreview.net/forum?id=0o4UJkkMvY)

- **问题 / 瓶颈** · 注意力可匹配但不一定对学生有用。
- **核心创新 / 方法** · 对照多种教师，并给学生补入随机初始化的教师原生组件。
- **Baseline** · 从零训练、默认学生及架构匹配学生。
- **Benchmark** · 11 个 ViT 家族、20 个教师，含分布外评测。
- **关键结果 / 消融** · 四族失败，最差低于从零基线 5.1%；补组件后逆转。
- **适用条件 / 局限** · 结论限所测家族。

**可复用机制** · 单独验收匹配损失和学生实际性能。

<a id="paper-151981"></a>

## AttnDiff: Attention-based Differential Fingerprinting for Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151981) · [作者来源](https://openreview.net/forum?id=WO87YWvex8)

- **问题 / 瓶颈** · 压缩和微调可能改变权重级指纹。
- **核心创新 / 方法** · 比较配对输入引发的注意力差异，用谱描述及 CKA 衡量相似性。
- **Baseline** · 相关衍生模型与不相关家族。
- **Benchmark** · Llama、Qwen 等开放权重模型。
- **关键结果 / 消融** · 摘要举例相关相似度大于 0.98，不相关低于 0.22。
- **适用条件 / 局限** · 需要白盒访问，阈值需独立校准。

**可复用机制** · 将相似性作为多项来源审计信号之一。

<a id="paper-153863"></a>

## Attribute-Efficient Learning of Sparse Halfspaces with Constant Malicious Noise Rate

[官方论文页](https://neurips.cc/virtual/2026/poster/153863) · [作者来源](https://openreview.net/forum?id=IB6y1X9QFZ)

- **问题 / 瓶颈** · 环境维数大时朴素采样界难用。
- **核心创新 / 方法** · 在集中性和间隔条件下分析稀疏约束 hinge 最小化。
- **Baseline** · 信息论下界及既有稀疏半空间结果。
- **Benchmark** · 常量恶意噪声的 PAC 理论设定。
- **关键结果 / 消融** · 样本上界为 O(s² log⁵ d)，另给下界。
- **适用条件 / 局限** · 集中性与间隔同时成立。

**可复用机制** · 在移植样本复杂度前检查边际和尾部分布。

<a id="paper-152941"></a>

## Attribution-Guided Exit Policy for Reliable Early-Exit Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/152941) · [作者来源](https://openreview.net/forum?id=PEGeDfsZ2w)

- **问题 / 瓶颈** · 高置信度不一定足以决定何时停止。
- **核心创新 / 方法** · 用归因强度和稳定性生成退出分数，再训练便宜代理。
- **Baseline** · 置信度阈值与全深度推理。
- **Benchmark** · ResNet、MobileNet、MSDNet，另测试 ViT 与 BERT 类模型。
- **关键结果 / 消融** · 最高准确率增益 2.5%，时长最多降 24%。
- **适用条件 / 局限** · 摘要未确认两个最优数字是否同设置。

**可复用机制** · 用离线归因监督在线退出代理。

<a id="paper-150554"></a>

## Attribution-Guided Shared-Private Decoupling for Noise-Reduced Audio-Visual Representation Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/150554) · [作者来源](https://openreview.net/forum?id=hHHYsu22Sj)

- **问题 / 瓶颈** · 聚合全部 token 会将模态私有残差拉入对齐。
- **核心创新 / 方法** · 截断层归因找共享子视图，以教师学生训练分解共享和私有表征。
- **Baseline** · 样本级对齐及强基线，名称待核。
- **Benchmark** · AudioSet、VGGSound 检索及 AS20K 分类。
- **关键结果 / 消融** · 平均零样本 R@1 提高 4.0，分类 mAP 提高 3.1。
- **适用条件 / 局限** · 依赖归因对子视图的可靠性。

**可复用机制** · 将共享对齐和私有信息保留分别消融。

<a id="paper-148384"></a>

## Attributions All the Way Down? The Metagame of Interpretability

[官方论文页](https://neurips.cc/virtual/2026/poster/148384) · [作者来源](https://openreview.net/forum?id=yHeBdE6C4F)

- **问题 / 瓶颈** · 单层归因压缩了影响方向。
- **核心创新 / 方法** · 把归因过程本身视为合作博弈并计算 Shapley 值。
- **Baseline** · 一阶归因和既有交互指标。
- **Benchmark** · 指令模型、跨模态编码器与文生图模型的解释案例。
- **关键结果 / 消融** · 证明分层分解并展示方向性交互。
- **适用条件 / 局限** · 计算成本和归因稳定性待核。

**可复用机制** · 对同一交互报告两个方向的解释贡献。

<a id="paper-150243"></a>

## A typed tensor language for federated learning

[官方论文页](https://neurips.cc/virtual/2026/poster/150243) · [作者来源](https://openreview.net/forum?id=jfzDfme1bL)

- **问题 / 瓶颈** · 逐协议描述掩盖公共结构。
- **核心创新 / 方法** · 区分记录分片张量与共享张量，证明单轮程序的共享状态分解及可表达条件下的逆命题。
- **Baseline** · 以虚拟全局张量语义作理论参照。
- **Benchmark** · 单轮及跨轮仅共享状态的程序。
- **关键结果 / 消融** · 状态尺寸不随客户端及记录数增长。
- **适用条件 / 局限** · 逆命题受编码器和解码器可表达性限制。

**可复用机制** · 先写本地编码、可合并聚合与共享解码，再检查所需状态维度。

<a id="paper-153035"></a>

## Auction-Based Online Policy Adaptation for Evolving Objectives

[官方论文页](https://neurips.cc/virtual/2026/poster/153035) · [作者来源](https://openreview.net/forum?id=OV5qcOHgej)

- **问题 / 瓶颈** · 固定多目标策略难应对目标集合变化。
- **核心创新 / 方法** · 用广义和马尔可夫博弈学习局部策略，以状态紧迫度竞价选择行动。
- **Baseline** · 摘要未列具名比较。
- **Benchmark** · 同族目标的在线适配，摘要所举例如可达性。
- **关键结果 / 消融** · 作者报告可通过增删策略立即调整；数值待核。
- **适用条件 / 局限** · 依赖目标共享参数化结构及竞价可协调性。

**可复用机制** · 同族目标变化时检验可插拔目标策略与重训策略的适配开销。

<a id="paper-154507"></a>

## Audible World Models: Spatially Aware Sound Generation for 3D Worlds

[官方论文页](https://neurips.cc/virtual/2026/poster/154507) · [作者来源](https://openreview.net/forum?id=D4dGC6P0dI)

- **问题 / 瓶颈** · 文本或画面生成的音轨缺乏持久空间位置。
- **核心创新 / 方法** · 拆解全景三维代理语义层，生成干声并以几何声学传播渲染。
- **Baseline** · 文本、视频和全景条件音频生成。
- **Benchmark** · 80 个生成场景，人评及视觉语言模型评估。
- **关键结果 / 消融** · 空间一致性改善，语义对齐仍具竞争力。
- **适用条件 / 局限** · 依赖代理几何和对象识别。

**可复用机制** · 将音色生成与声源定位解耦，沿听者轨迹评估一致性。

<a id="paper-139120"></a>

## AudioAgentBench: Evaluating Multi-Turn Voice Agents on Real-World Tasks

[官方论文页](https://neurips.cc/virtual/2026/poster/139120) · [作者来源](https://openreview.net/forum?id=jvvUbIXK5F)

- **问题 / 瓶颈** · 只看最终数据库会掩盖错误起点。
- **核心创新 / 方法** · 固定音频轨迹，按金标准调用和状态诊断，并用跨轮重对齐处理级联错误。
- **Baseline** · 七种端到端语音模型。
- **Benchmark** · 六项任务、221 轮、420 次会话，含真人和 TTS。
- **关键结果 / 消融** · 摘要报告分项诊断，具体排名待核。
- **适用条件 / 局限** · 预录轨迹限制开放交互覆盖。

**可复用机制** · 同时报告首错、恢复与最终成功。

<a id="paper-149240"></a>

## AudioCALM: Continuous Autoregressive Language Modeling for Universal Audio Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/149240) · [作者来源](https://openreview.net/forum?id=rta7h4O2eL)

- **问题 / 瓶颈** · 逐时语音转录与整体描述的对齐范围不同。
- **核心创新 / 方法** · 连续潜变量自回归配流匹配头，统一描述条件并给语音加专属专家。
- **Baseline** · 具名生成基线待核。
- **Benchmark** · 语音、音乐、音效生成。
- **关键结果 / 消融** · 作者指出混合转录条件会损伤音乐与音效，方案的量化结果待核。
- **适用条件 / 局限** · 依赖潜编码与描述质量。

**可复用机制** · 多任务训练先诊断条件对齐粒度，再将梯度冲突大的模态单独路由。

<a id="paper-149852"></a>

## AudioGS: High-Fidelity Neural Audio Compression via Continuous Gaussian Splatting

[官方论文页](https://neurips.cc/virtual/2026/poster/149852) · [作者来源](https://openreview.net/forum?id=mpOLhvRzOy)

- **问题 / 瓶颈** · 离散码本是主流瓶颈，但可能限制表征。
- **核心创新 / 方法** · 拟合一维高斯加权和，训练预测器替代推理期内循环，训练后再量化参数。
- **Baseline** · 残差向量量化、有限标量量化等设计。
- **Benchmark** · 语音编解码；具体指标待核。
- **关键结果 / 消融** · 提出单次推断的压缩表示；码率质量幅度待核。
- **适用条件 / 局限** · 参数量化和解码成本须计入端到端比较。

**可复用机制** · 固定码率比较离散索引与量化后的连续基元。

<a id="paper-151452"></a>

## AudioSphere: Towards Self-Supervised Spatial Audio Representation Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151452) · [作者来源](https://openreview.net/forum?id=aa8QwF7hqk)

- **问题 / 瓶颈** · 单通道通用模型缺空间结构，片级监督缺帧级定位。
- **核心创新 / 方法** · 对 Ambisonics 掩码时频图块和强度向量。
- **Baseline** · 既有通用音频嵌入。
- **Benchmark** · RealSELD 冻结骨干定位和 HEAR 片级测试。
- **关键结果 / 消融** · 支持冻结骨干执行 SELD，HEAR 表现相当或更好。
- **适用条件 / 局限** · 依赖多通道录音，设备迁移待核。

**可复用机制** · 统一表征应同时测逐帧与聚合后的能力。

<a id="paper-153983"></a>

## Audio-Visual Flamingo: Open Audio-Visual Intelligence for Long and Complex Videos

[官方论文页](https://neurips.cc/virtual/2026/poster/153983) · [作者来源](https://openreview.net/forum?id=H4Lfwx7aXK)

- **问题 / 瓶颈** · 短片训练难支持跨事件推理。
- **核心创新 / 方法** · 渐进从短时感知训练至多事件推理，并给中间推理关联时间戳。
- **Baseline** · 同尺寸开放模型与更大模型。
- **Benchmark** · 超过 15 项视听与单模态基准。
- **关键结果 / 消融** · 作者报告长复杂视频有优势；课程和时间戳独立效果待核。
- **适用条件 / 局限** · 训练数据量本身也可能解释收益。

**可复用机制** · 固定数据与模型比较有无时间戳监督的长程证据定位。

<a id="paper-152885"></a>

## Auditing AI peer reviewers: a dose-response and false-positive benchmark on real scientific papers

[官方论文页](https://neurips.cc/virtual/2026/poster/152885) · [作者来源](https://openreview.net/forum?id=Pf1SuIB41Z)

- **问题 / 瓶颈** · 只有检出率会奖励无依据的质疑。
- **核心创新 / 方法** · 在真实预印本植入可验证错误，拆分数学、引文和数值等错误。
- **Baseline** · 12 个审稿系统，含结构化和自由提示。
- **Benchmark** · 15 篇天体物理预印本、177 个错误。
- **关键结果 / 消融** · 同一 Claude Code 模型改结构化提示后检出率升 32.2 个百分点。
- **适用条件 / 局限** · 样本限天体物理，人工标注一致性与跨领域表现待核。

**可复用机制** · 同时记录剂量响应、漏报与原文无误处的误报。

<a id="paper-139256"></a>

## Auditing Attention Head Masking for Out-of-Distribution Detection: Cross-Architecture Wins, Failures, and Polarity Inversions

[官方论文页](https://neurips.cc/virtual/2026/poster/139256) · [作者来源](https://openreview.net/forum?id=bqTe5C6VVH)

- **问题 / 瓶颈** · 同一方向的分数在不同模型可能翻转。
- **核心创新 / 方法** · 统一协议跨文档、图像和文本审计注意力头遮蔽。
- **Baseline** · 17 个对照，含 AHSS、X-Mahalanobis。
- **Benchmark** · 三类 Transformer、五种子与配对检验。
- **关键结果 / 消融** · RoBERTa 的 AHSS 位移平均 AUROC 为 0.296，所测 ViT 的 MC Dropout 接近随机。
- **适用条件 / 局限** · 结论限给定模型和数据。

**可复用机制** · 封存部署架构的独立校准集，分别检验极性及绝对区分能力。

<a id="paper-139763"></a>

## Auditing Capsule Vision 2024: Within-Split Train-to-Validation Re-Exposure and a Kvasir-Channel Sensitivity Diagnostic

[官方论文页](https://neurips.cc/virtual/2026/poster/139763) · [作者来源](https://openreview.net/forum?id=69GCzBgr1S)

- **问题 / 瓶颈** · 随机按帧划分会产生训练验证重现。
- **核心创新 / 方法** · 联合感知哈希、像素相关和特征检查并追溯视频前缀。
- **Baseline** · 原发布划分与移除 Kvasir 来源的划分。
- **Benchmark** · Capsule Vision 2024 公共验证，核对重现和分类平衡准确率。
- **关键结果 / 消融** · 11,581 条中 1,381 条哈希精确匹配，540 条满足高像素相关阈值。
- **适用条件 / 局限** · 移除来源也改变域组成，分数差不能直接归因于泄漏。

**可复用机制** · 报告重复审计和去来源敏感度，并避免将后者当隐藏测试代理。

<a id="paper-157025"></a>

## Auditing Closed-Loop Learning in Recurrent Neural Networks: Reproduction, Robustness, and Generalization

[官方论文页](https://neurips.cc/virtual/2026/poster/157025) · [作者来源](https://openreview.net/forum?id=e0pSqIqwXO)

- **问题 / 瓶颈** · 仅看终态会漏掉训练期的损失峰。
- **核心创新 / 方法** · 复现双积分器并扰动随机种子、任务与网络结构。
- **Baseline** · 开环与闭环训练，另比较 GRU、低秩及 tanh RNN。
- **Benchmark** · 配对种子和闭环耦合系统诊断。
- **关键结果 / 消融** · 50 个配对种子均见开环部署损失峰，平均峰初比 19.1，但最终损失趋同。
- **适用条件 / 局限** · 跨架构和路径积分任务的迁移不均。

**可复用机制** · 以轨迹级统计和终点统计分别验收闭环学习规律。

<a id="paper-138875"></a>

## Auditing Conformal Prediction for Language Models Under Inference-Time Model Shift

[官方论文页](https://neurips.cc/virtual/2026/poster/138875) · [作者来源](https://openreview.net/forum?id=zYzgw5b6rP)

- **问题 / 瓶颈** · 输入分布不变也可能因推理配置变化破坏交换性。
- **核心创新 / 方法** · 定义推理时模型偏移并比较匹配与不匹配配置的共形分数。
- **Baseline** · 匹配校准和部署的协议。
- **Benchmark** · 8 个模型、4 个有限标签基准、12 种推理配置。
- **关键结果 / 消融** · 匹配评测可能高估部署覆盖，幅度随模型与数据变化。
- **适用条件 / 局限** · 有限标签基准不能直接代表开放生成。

**可复用机制** · 将推理配置视为独立校准轴，量化配置变化后的覆盖与集合大小。

<a id="paper-138982"></a>

## Auditing Correlated Failures in Frozen-Feature Pretrained-Encoder Pools for Medical Segmentation

[官方论文页](https://neurips.cc/virtual/2026/poster/138982) · [作者来源](https://openreview.net/forum?id=sgt45cOBtI)

- **问题 / 瓶颈** · 单模型指标不能判断输出失败是否重叠。
- **核心创新 / 方法** · 比较同包和跨包 Dice 相关，另改变解码器并控制病例难度。
- **Baseline** · 11 个编码器包，弱读出和更丰富读出。
- **Benchmark** · Kvasir、ACDC、BraTS 和 RIGA 五项分割。
- **关键结果 / 消融** · 弱读出相关差 0.261–0.638；更强解码器可明显缩小差距。
- **适用条件 / 局限** · 效应大小依赖读出配方。

**可复用机制** · 选集成成员时固定解码器并报告联合失败率。

<a id="paper-138923"></a>

## Auditing Cross-Lingual Fairness in Language Model Watermarking

[官方论文页](https://neurips.cc/virtual/2026/poster/138923) · [作者来源](https://openreview.net/forum?id=wcDXaLSf2C)

- **问题 / 瓶颈** · 英语阈值和单一质量测量会掩盖跨语言差异。
- **核心创新 / 方法** · 组合部署校准、阈值无关指标、三种质量测量及语言家族分解。
- **Baseline** · 六种水印、三个开放生成器。
- **Benchmark** · 11 种语言、四种书写系统，并区分基础与指令模型。
- **关键结果 / 消融** · 检测与质量差异主要见于语言家族之间。
- **适用条件 / 局限** · 取决于家族划分与生成设置。

**可复用机制** · 跨语言部署同时比较阈值迁移、独立校准和语义质量。

<a id="paper-139236"></a>

## Auditing Evidence Framing at NeurIPS: A Decade-Scale Study of Accepted Papers

[官方论文页](https://neurips.cc/virtual/2026/poster/139236) · [作者来源](https://openreview.net/forum?id=d3J7bxCLHH)

- **问题 / 瓶颈** · 主题迁移会混入证据风格变化。
- **核心创新 / 方法** · 用对比嵌入量化证据维度，再用盲评、词汇探针和主题调整检查。
- **Baseline** · 未经调整的趋势与独立词汇主题模型。
- **Benchmark** · 2015–2024 年 19,361 篇 NeurIPS 录用论文。
- **关键结果 / 消融** · 制品发布的措辞原始上升 0.226 标准差，主题调整后接近零或为负。
- **适用条件 / 局限** · 测量的是标题摘要措辞；不能直接据此判断实际制品发布率。

**可复用机制** · 同报原始趋势和主题内趋势，避免将写作变化解释为科研行为变化。

<a id="paper-149397"></a>

## Auditing Privacy Leakage in Tabular Foundation Model Embeddings

[官方论文页](https://neurips.cc/virtual/2026/poster/149397) · [作者来源](https://openreview.net/forum?id=qLsP2gDvC0)

- **问题 / 瓶颈** · 只做单属性或无辅助信息审计会低估风险。
- **核心创新 / 方法** · 按不同辅助信息预算测敏感属性恢复，并对比独立及联合审计。
- **Baseline** · 联合探测与优化式对照。
- **Benchmark** · 四种表格基础模型与八个数据集。
- **关键结果 / 消融** · 作者报告无辅助信息时仍有 65–95% 的敏感属性可恢复，单一已知属性可提升其余属性恢复率。
- **适用条件 / 局限** · 数值受数据、属性相关性和评测协议影响。

**可复用机制** · 在发布表征前按外部信息预算分层测泄漏，检查常用压缩与加噪后是否仍存在风险。
