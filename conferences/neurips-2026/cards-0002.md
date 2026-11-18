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

<a id="paper-139641"></a>

## Auditing Sabotage Bench: A Benchmark for Detecting and Fixing Research Sabotage in ML Codebases

[官方论文页](https://neurips.cc/virtual/2026/poster/139641) · [作者来源](https://openreview.net/forum?id=Dt3YCPLZ7N)

- **问题 / 瓶颈** · 代码误差可能改变结论而不易发现。
- **核心创新 / 方法** · 以已知异常版本和原版对照评测审计。
- **Baseline** · 前沿模型与模型辅助人审。
- **Benchmark** · 9 个机器学习代码库；AUROC 与首选修复率。
- **关键结果 / 消融** · 最佳为 0.77 AUROC 与 42% 首选修复率。
- **适用条件 / 局限** · 限于所收集代码库。

**可复用机制** · 以独立复现实验和结果回归验证审计修复。

<a id="paper-152886"></a>

## Auditing Single-Query Recoverability in Self-Supervised Representations

[官方论文页](https://neurips.cc/virtual/2026/poster/152886) · [作者来源](https://openreview.net/forum?id=Pera711ODe)

- **问题 / 瓶颈** · 成对视图等额外信息可能高估部署性能。
- **核心创新 / 方法** · 固定单查询接口并匹配语义效用，报告尾部误差和额外信息。
- **Baseline** · 原始变换评测及满足接口的邻域对照。
- **Benchmark** · 3DIEBench-Honest、PTB-XL 与合成设定。
- **关键结果 / 消融** · 单查询旋转误差通常为原指标的 2–3 倍。
- **适用条件 / 局限** · 不能外推到所有变换任务。

**可复用机制** · 按部署可见信息建立基准并显式列出评测特权。

<a id="paper-153728"></a>

## Auditing the Judge: Human-Grounded Bias Discovery, Quantification, and Mitigation in LLM Judges

[官方论文页](https://neurips.cc/virtual/2026/poster/153728) · [作者来源](https://openreview.net/forum?id=JDZWX9hyyq)

- **问题 / 瓶颈** · 预设偏差清单可能偏离人类实际判断。
- **核心创新 / 方法** · 从分歧挖掘偏差因子，在一致例上干预输入，用回归扣除估计偏差。
- **Baseline** · 既有评审偏差缓解；具名对照待核。
- **Benchmark** · 人评与模型评审对照；任务待核。
- **关键结果 / 消融** · 摘要描述无需训练的校正；量化待核。
- **适用条件 / 局限** · 依赖人评代表性及改写是否保持任务内容。

**可复用机制** · 把发现偏差和估计改写效应放到不同样本组。

<a id="paper-154384"></a>

## Auditor-Assisted Summary-Channel Verification for Hosted LLM Identity Substitution

[官方论文页](https://neurips.cc/virtual/2026/poster/154384) · [作者来源](https://openreview.net/forum?id=DysqVLjr3q)

- **问题 / 瓶颈** · 外部人员无法访问实际路由和模型内部。
- **核心创新 / 方法** · 预先登记模型，校准摘要标记的身份统计检验。
- **Baseline** · 跨家族和跨规格替换对照。
- **Benchmark** · 多家族、多规模、多任务；测误报和回答质量。
- **关键结果 / 消融** · 报告低误报下可检测替换，并保持回答质量。
- **适用条件 / 局限** · 需可信登记和公开摘要。

**可复用机制** · 用独立登记样本定阈值，再用留出任务查误报。

<a id="paper-152194"></a>

## AuGhostmentation: The Eyes Never Stand Still—$\textit{Why Should CNNs?}$

[官方论文页](https://neurips.cc/virtual/2026/poster/152194) · [作者来源](https://openreview.net/forum?id=UrYjjK6We7)

- **问题 / 瓶颈** · 标准 CNN 对常见失真敏感。
- **核心创新 / 方法** · 在输入端叠加按眼动统计采样的低强度图像副本。
- **Baseline** · ResNet 与其他增强。
- **Benchmark** · Tiny ImageNet-C、ImageNet-100 和风格化测试。
- **关键结果 / 消融** · Tiny ImageNet-C 鲁棒性相对提高 60%，保留 98% 原验证准确率。
- **适用条件 / 局限** · 强度和位移分布的迁移待核。

**可复用机制** · 固定训练预算，对照叠加副本与普通几何增强。

<a id="paper-153175"></a>

## Augmented Equivariant Mesh Networks for Anatomical Segmentation

[官方论文页](https://neurips.cc/virtual/2026/poster/153175) · [作者来源](https://openreview.net/forum?id=NHNCBuH2mF)

- **问题 / 瓶颈** · 扫描位姿和网格分辨率变化会使分割退化。
- **核心创新 / 方法** · 把内在网格特征和解剖坐标先验接入等变消息传递。
- **Baseline** · 专用网格和点云模型。
- **Benchmark** · 口腔、颅内和肝脏等网格分割。
- **关键结果 / 消融** · 不到 2M 参数，扰动下保持稳定；细项待核。
- **适用条件 / 局限** · 解剖坐标先验与等变性有权衡。

**可复用机制** · 同一网格施加可控旋转，分开报告标准姿态与扰动 IoU。

<a id="paper-155499"></a>

## Augmented Lagrangian Method for Last-Iterate Convergence for Constrained MDPs

[官方论文页](https://neurips.cc/virtual/2026/poster/155499) · [作者来源](https://openreview.net/forum?id=57dCx6dxTb)

- **问题 / 瓶颈** · 混合策略保证难直接用于单策略部署。
- **核心创新 / 方法** · 通过不精确增广拉格朗日和投影 Q 上升求约束策略。
- **Baseline** · 混合与既有最终迭代方法。
- **Benchmark** · 无限时域折扣 CMDP，表格和对数线性策略。
- **关键结果 / 消融** · 证明最终迭代收敛；实验细节待核。
- **适用条件 / 局限** · 理论依赖设定和子问题误差条件。

**可复用机制** · 按部署接口报告最终策略的回报与约束违规。

<a id="paper-154623"></a>

## Augmented Lagrangian Predictive Coding

[官方论文页](https://neurips.cc/virtual/2026/poster/154623) · [作者来源](https://openreview.net/forum?id=CBiJrxWtct)

- **问题 / 瓶颈** · 深窄网络中普通预测编码的信用传播较慢。
- **核心创新 / 方法** · 在局部推断中进行增广拉格朗日对偶上升。
- **Baseline** · 预测编码与反向传播。
- **Benchmark** · 线性分析及最深 128 层的非线性网络。
- **关键结果 / 消融** · 线性平衡点得精确反传梯度；实验报告表现与反传接近。
- **适用条件 / 局限** · 精确梯度证明针对线性网络。

**可复用机制** · 固定推断预算，逐层测误差信号传播和最终性能。

<a id="paper-154277"></a>

## A Unified Approach for Computing Wasserstein Barycenters of Discrete and Continuous Measures

[官方论文页](https://neurips.cc/virtual/2026/poster/154277) · [作者来源](https://openreview.net/forum?id=F23W2B2hf8)

- **问题 / 瓶颈** · 已有算法通常限定输入表示。
- **核心创新 / 方法** · 在 Fisher–Rao 几何中做原始镜像下降。
- **Baseline** · 离散和规则网格专用求解器；名称待核。
- **Benchmark** · 合成与真实测度；精度和计算成本。
- **关键结果 / 消融** · 给出两类输入的收敛保证；离散输入的连续迭代可收敛至离散重心。
- **适用条件 / 局限** · 半离散子问题仍有计算成本。

**可复用机制** · 比较混合表示下统一求解与预离散化造成的误差。

<a id="paper-154205"></a>

## A Unified Audio Language Model with Text-Aligned Factorized Audio Tokenization

[官方论文页](https://neurips.cc/virtual/2026/poster/154205) · [作者来源](https://openreview.net/forum?id=FP1dTx5VEk)

- **问题 / 瓶颈** · 单一音频码本需同时满足理解与合成。
- **核心创新 / 方法** · 用独立离散 token 承担分析与重建，并分工模型层。
- **Baseline** · Whisper 连续特征及 7B 统一模型。
- **Benchmark** · 音频理解、生成和少样本或零样本组合任务。
- **关键结果 / 消融** · 3B 模型在同域任务与强 7B 对照有竞争力。
- **适用条件 / 局限** · 数据规模与结构贡献待消融。

**可复用机制** · 按理解表现和重建困惑度分别选择码本。

<a id="paper-153636"></a>

## A Unified Framework for Adversary-Aware Differential Privacy Bounds

[官方论文页](https://neurips.cc/virtual/2026/poster/153636) · [作者来源](https://openreview.net/forum?id=Jt45l0WVtc)

- **问题 / 瓶颈** · 不同隐私风险常用不同成功定义。
- **核心创新 / 方法** · 用隐私参数与先验成功率统一界定多目标及近似匹配风险。
- **Baseline** · 经典成员推断保证与机制无关的先验成功。
- **Benchmark** · 理论风险界与表格、语言模型隐私评估。
- **关键结果 / 消融** · 给出适用多种成功条件的高概率保证。
- **适用条件 / 局限** · 先验成功率估计影响界的实用性。

**可复用机制** · 用同一成功定义比较有无机制输出时的风险。

<a id="paper-150141"></a>

## A Unified Framework for Image-to-3D Part Generation via Variable Granularity

[官方论文页](https://neurips.cc/virtual/2026/poster/150141) · [作者来源](https://openreview.net/forum?id=kMbkSnVh5B)

- **问题 / 瓶颈** · 每种提示单独训练难共享几何信息。
- **核心创新 / 方法** · 门控调制结合异粒度条件，辅以非对称几何对齐。
- **Baseline** · 已有部件生成模型；名称待核。
- **Benchmark** · 图像到三维部件生成；Part CD。
- **关键结果 / 消融** · 报告 Part CD 改善超过 10.5%。
- **适用条件 / 局限** · 跨种类和混合条件边界待核。

**可复用机制** · 对异粒度提示分别量化一致性，并检验共享训练收益。

<a id="paper-154380"></a>

## A Unified Framework for Uniform-Price Resource Allocation Mechanisms

[官方论文页](https://neurips.cc/virtual/2026/poster/154380) · [作者来源](https://openreview.net/forum?id=DzYsp7y9pY)

- **问题 / 瓶颈** · 经典 Kelly 机制简单但效率受限。
- **核心创新 / 方法** · 统一价格族在 Kelly 机制与第一价格拍卖间插值。
- **Baseline** · Kelly 和 VCG。
- **Benchmark** · 均衡效率、收入和预算约束下的流动福利。
- **关键结果 / 消融** · 证明可改善 Kelly 保证，部分机制达完全效率。
- **适用条件 / 局限** · 预算可行性结果依赖预算公开条件。

**可复用机制** · 分别检查分配规则、支付与预算披露对均衡性质的影响。

<a id="paper-148900"></a>

## A Unified Graph Language Model for Multi-Domain Multi-Task Graph Alignment Instruction Tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/148900) · [作者来源](https://openreview.net/forum?id=uKvHBTwC3D)

- **问题 / 瓶颈** · 固定策略忽视不同图域的结构和语义差异。
- **核心创新 / 方法** · 先用多域图文对预训练 GNN，再按难度调整指令对齐课程。
- **Baseline** · 既有图语言模型；名称待核。
- **Benchmark** · 不同图域和任务；数据集待核。
- **关键结果 / 消融** · 作者报告优于对照，量化与消融待核。
- **适用条件 / 局限** · 依赖图文配对质量及难度估计。

**可复用机制** · 对共享图编码器比较固定采样与按对齐难度组织的课程。

<a id="paper-154993"></a>

## A Unified Image and Video Encoder for Multimodal LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/154993) · [作者来源](https://openreview.net/forum?id=9MSdZWbWLg)

- **问题 / 瓶颈** · 逐帧编码把时间关系都留给语言模型。
- **核心创新 / 方法** · 联合时空预训练，并以帧选择注意力稀疏读取历史。
- **Baseline** · 逐帧视觉骨干。
- **Benchmark** · 16 个图像与视频基准，含长视频。
- **关键结果 / 消融** · 摘要报告更高效率与有效时序表征；数值待核。
- **适用条件 / 局限** · 不同任务对稀疏帧召回敏感。

**可复用机制** · 固定语言骨干对照前端时序融合与逐帧编码。

<a id="paper-152315"></a>

## A Unified Merge Calculus for Learning-Rate Scaling on Neural Computation Graphs

[官方论文页](https://neurips.cc/virtual/2026/poster/152315) · [作者来源](https://openreview.net/forum?id=TzJ1RmUWQr)

- **问题 / 瓶颈** · 不同合并方式改变最优步长。
- **核心创新 / 方法** · 将局部合并规则与全局路径组成复杂度系数，预测负二分之一次幂关系。
- **Baseline** · 仅深度尺度律。
- **Benchmark** · 受控图族、求和、残差、拼接、加权融合。
- **关键结果 / 消融** · 报告图系数较深度更能解释最优学习率。
- **适用条件 / 局限** · 实验证据以轻量架构为主。

**可复用机制** · 跨架构迁移前检查合并方式和路径结构。

<a id="paper-149870"></a>

## A Unified Neural Architecture for Variable-Wise Shape Constraints

[官方论文页](https://neurips.cc/virtual/2026/poster/149870) · [作者来源](https://openreview.net/forum?id=mZxrBjgm2M)

- **问题 / 瓶颈** · 软惩罚难保证全域满足先验。
- **核心创新 / 方法** · 按变量分配形状区间，路由到符号受限权重及保形激活。
- **Baseline** · 仅有限形状支持或软惩罚架构。
- **Benchmark** · 合成及真实数据，比较预测和噪声鲁棒性。
- **关键结果 / 消融** · 证明八类条件由结构保证，报告预测有竞争力。
- **适用条件 / 局限** · 变量约束须事先知道。

**可复用机制** · 对必须全域成立的约束，比较硬结构与软损失。

<a id="paper-154823"></a>

## A unified pairwise distribution matching framework for graph domain adaptation under structure shift

[官方论文页](https://neurips.cc/virtual/2026/poster/154823) · [作者来源](https://openreview.net/forum?id=Ah6YrDGyzd)

- **问题 / 瓶颈** · 只做节点级表示对齐不能处理条件连边变化。
- **核心创新 / 方法** · 统一矩匹配和校准节点对似然，按边权分析误差。
- **Baseline** · 既有图域适应的矩匹配实例。
- **Benchmark** · 上下文随机块模型的有限样本分析。
- **关键结果 / 消融** · 给出似然与矩匹配误差界。
- **适用条件 / 局限** · 依赖条件结构偏移及模型假设。

**可复用机制** · 把节点级与节点对级对齐分开消融。

<a id="paper-148880"></a>

## A Unified Perturbation Framework for Analyzing Leaderboard Stability and Manipulation

[官方论文页](https://neurips.cc/virtual/2026/poster/148880) · [作者来源](https://openreview.net/forum?id=uUAHsLfCCm)

- **问题 / 瓶颈** · 单一排名掩盖小数据变更的影响。
- **核心创新 / 方法** · 用影响近似审计结构化数据扰动对排名的后果。
- **Baseline** · 不同排行榜和数据集之间的稳定性对照。
- **Benchmark** · Chatbot Arena 与另六个成对数据集；Top-k、Kendall tau 和区间。
- **关键结果 / 消融** · 作者报告小于 1% 的数据改动足以改变首位。
- **适用条件 / 局限** · 依赖聚合规则和实际投票分布。

**可复用机制** · 发布排行榜时附敏感性与置信区间，避免把微小排名差解释为稳定差异。

<a id="paper-151762"></a>

## A Unified Semismooth Newton Approach to Multitask and Multivariate Square-Root Lasso Problems

[官方论文页](https://neurips.cc/virtual/2026/poster/151762) · [作者来源](https://openreview.net/forum?id=YEOev9QfVu)

- **问题 / 瓶颈** · 损失与惩罚皆非光滑，大规模迭代昂贵。
- **核心创新 / 方法** · 在 Douglas–Rachford 分裂的非光滑方程上用正则牛顿及投影保护。
- **Baseline** · 多任务和多元模型各自专用求解器。
- **Benchmark** · 合成回归与多组学数据，比较迭代和耗时。
- **关键结果 / 消融** · 报告得到同样拟合和预测且用更少迭代；给出局部二次收敛。
- **适用条件 / 局限** · 依赖相应收敛条件与线性子系统规模。

**可复用机制** · 非光滑多响应问题优先比较原维牛顿与近端结构降维。

<a id="paper-155760"></a>

## A Unified Spectral Theory of Multimodal Losses

[官方论文页](https://neurips.cc/virtual/2026/poster/155760) · [作者来源](https://openreview.net/forum?id=37eNHfTSDD)

- **问题 / 瓶颈** · 不同训练目标缺少统一选择依据
- **核心创新 / 方法** · 线性化后谱分析比较四类目标的潜变量恢复
- **Baseline** · CLIP式对比、SigLIP式判别、词元生成、潜空间预测
- **Benchmark** · 合成数据与 Flickr30k、COCO、CC3M
- **关键结果 / 消融** · 三类目标共享跨模态解，定向生成单侧约束更弱；双侧干净时目标匹配查询模态的潜预测检索最好
- **适用条件 / 局限** · 理论依赖线性化和潜结构

**可复用机制** · 按两侧噪声分层，同时交换预测方向测检索

<a id="paper-149830"></a>

## A Unified Theoretical Framework for Task Recognition and Task Learning in In-Context Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149830) · [作者来源](https://openreview.net/forum?id=mzLkPTQDvG)

- **问题 / 瓶颈** · 熟悉任务识别和新映射学习的样本效率不同
- **核心创新 / 方法** · 用 Pitman–Yor 任务混合及容量约束推导注水分配
- **Baseline** · 任务识别与任务学习的理论对照
- **Benchmark** · 贝叶斯预测及不同长度提示的误差率
- **关键结果 / 消融** · 常见任务指数收敛，稀有任务幂律收敛
- **适用条件 / 局限** · 依赖最优预测器、容量和任务分布假设

**可复用机制** · 区分记忆调用与新任务归纳，分别拟合学习曲线

<a id="paper-151405"></a>

## A Unified Uncertainty Representation for Graph Neural Networks via Doubly-Spectral Stochastic Expansion

[官方论文页](https://neurips.cc/virtual/2026/poster/151405) · [作者来源](https://openreview.net/forum?id=aviTmQybX5)

- **问题 / 瓶颈** · 单独训练多个不确定性模型难共享结构
- **核心创新 / 方法** · 图傅里叶滤波表征结构，正交多项式展开随机性，分别用求积预测与均值能量读出
- **Baseline** · 不确定性感知图模型与确定性编码器
- **Benchmark** · 14 个节点分类基准、节点与跨图 OOD、7 个 GOOD 概念偏移设置
- **关键结果 / 消融** · 独立模型在 14 项 Brier 最低，混合模型在全部 7 项偏移准确率领先
- **适用条件 / 局限** · 近似定理有潜变量条件，推理成本待核

**可复用机制** · 区分分类均值与变动分量，按校准、OOD 和迁移分别验证

<a id="paper-148396"></a>

## A Unifying Perspective on Language Model Interpretability

[官方论文页](https://neurips.cc/virtual/2026/poster/148396) · [作者来源](https://openreview.net/forum?id=y9mExa1HH7)

- **问题 / 瓶颈** · 局部解释方法难形成统一的表示假设
- **核心创新 / 方法** · 从角色与填充值的张量积表示导出类比、探针、稀疏自编码和激活替换
- **Baseline** · 各解释方法的标准实现
- **Benchmark** · 从玩具模型到大语言模型的同类方法比较
- **关键结果 / 消融** · 派生变体表现与标准方法相近
- **适用条件 / 局限** · 相近表现无法唯一识别真实内部表示

**可复用机制** · 先用同一组合结构推导多个诊断，再检查不同方法是否支持一致假设

<a id="paper-153667"></a>

## A Unifying View of Anchoring via Operator-Side Tikhonov Regularization

[官方论文页](https://neurips.cc/virtual/2026/poster/153667) · [作者来源](https://openreview.net/forum?id=Jf0hmlMAUC)

- **问题 / 瓶颈** · 不同迭代的锚点位置难统一
- **核心创新 / 方法** · 对查询算子加 Tikhonov 项，再运行不改更新模式的原算法
- **Baseline** · Halpern、前向步、外梯度和 Popov
- **Benchmark** · 无约束单调 Lipschitz 算子的末次残差
- **关键结果 / 消融** · Halpern、外梯度和 Popov 为 O(1/k)，前向步为 O(1/√k)
- **适用条件 / 局限** · 受单调性、光滑性和正则日程限制

**可复用机制** · 设计新锚定算法时由原查询结构导出锚点，并用末次残差验收

<a id="paper-148451"></a>

## AURA: An Autonomous Retouching Agent with Photographic Visual Thinking

[官方论文页](https://neurips.cc/virtual/2026/poster/148451) · [作者来源](https://openreview.net/forum?id=xjji3AG4Rb)

- **问题 / 瓶颈** · 只预测全局参数难补救局部编辑错误
- **核心创新 / 方法** · 学习专家修图轨迹，SFT 后用感知质量与工具准确性做 GRPO
- **Baseline** · 全局参数及指令式编辑方法
- **Benchmark** · 定量图像评估与用户研究，协议待核
- **关键结果 / 消融** · 作者报告两类评估均改善，独立消融待核
- **适用条件 / 局限** · 专家轨迹和审美偏好影响泛化

**可复用机制** · 对照一次编辑与逐步回读，分离工具选择和最终质量

<a id="paper-155137"></a>

## Auteur: Language-Driven Cinematographic Framing for Human-Centric Video Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/155137) · [作者来源](https://openreview.net/forum?id=86BxEBOd7Q)

- **问题 / 瓶颈** · 世界坐标轨迹难明确表达主体构图
- **核心创新 / 方法** · 语言模型输出相对姿态和运动的 DSL 关键帧，再确定性插值为六自由度轨迹
- **Baseline** · 已有镜头控制生成方法
- **Benchmark** · 合成与 CondensedMovies 来源的约 3 万配对样本，评估构图
- **关键结果 / 消融** · 作者报告构图指标改善，幅度待核
- **适用条件 / 局限** · 依赖可用的人体运动和生成器的轨迹服从性

**可复用机制** · 先定义主体相对构图再转相机控制，单独评估主体取景

<a id="paper-139001"></a>

## AutoDataBench: How Far Are LLM Agents from Autonomously Engineering Post-Training Data Pipelines?

[官方论文页](https://neurips.cc/virtual/2026/poster/139001) · [作者来源](https://openreview.net/forum?id=rf8RGRFNAS)

- **问题 / 瓶颈** · 能解题的模型未必能构建高质量训练数据管线
- **核心创新 / 方法** · 让候选管线生成数据，在统一学生和下游评测下比较
- **Baseline** · 人类设计管线及不同模型
- **Benchmark** · 指令跟随、数学、搜索和两类软件任务
- **关键结果 / 消融** · 文本任务接近人类参考，需构造执行环境的任务差距较大
- **适用条件 / 局限** · 结论受学生模型及训练预算影响

**可复用机制** · 把管线质量与模型自身解题能力分别评估

<a id="paper-152534"></a>

## Auto-Dreamer: Learning Offline Memory Consolidation for Language Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/152534) · [作者来源](https://openreview.net/forum?id=SR1n2zkaBO)

- **问题 / 瓶颈** · 在线写入难从全局发现重复经验和程序
- **核心创新 / 方法** · 离线回查原轨迹，合并替换有来源的类型化记忆，以任务回报训练整理器
- **Baseline** · 固定、训练式和提示式记忆系统
- **Benchmark** · ScienceWorld 训练，ALFWorld 和 WebArena 留出迁移
- **关键结果 / 消融** · 作者报告迁移成功率改善，活动记忆规模约小一个数量级
- **适用条件 / 局限** · 需要保留原轨迹与可用任务回报

**可复用机制** · 固定任务预算，对照即时总结与可追溯的跨会话压缩

<a id="paper-139399"></a>

## AutoExpert: Automating 3D LiDAR Annotation from Expert-Crafted Guidelines

[官方论文页](https://neurips.cc/virtual/2026/poster/139399) · [作者来源](https://openreview.net/forum?id=T24nnfn2Jn)

- **问题 / 瓶颈** · 指南以图文描述类别而标签输出是三维框
- **核心创新 / 方法** · 重标数据测试规范迁移，使用图像检测、姿态投影和三维框生成
- **Baseline** · 原三阶段管线、开放词汇和少样本检测组件
- **Benchmark** · nuScenes、PandaSet，分别含 18 和 25 类规范，测 mAP
- **关键结果 / 消融** · AutoExpert-nuScenes mAP 由 12.1 升到 25.4
- **适用条件 / 局限** · 依赖标定与视角覆盖，各组件增益待核

**可复用机制** · 更换标注规范时，用重标留出集验证模型是否遵循新类别定义

<a id="paper-156757"></a>

## Autofocus Retrieval: An Effective Pipeline for Multi-Hop Question Answering With Semi-Structured Knowledge

[官方论文页](https://neurips.cc/virtual/2026/poster/156757) · [作者来源](https://openreview.net/forum?id=U2vqruHfQY)

- **问题 / 瓶颈** · 单纯向量相似度难处理多跳结构约束
- **核心创新 / 方法** · 合并结构路径与关联文档，以约束逐轮扩大候选并重排
- **Baseline** · 结构与文本混合检索对照及不同重排方案
- **Benchmark** · 三个 STaRK 零样本和单样本问答基准
- **关键结果 / 消融** · 摘要报告平均首位命中率比次优高 32.1%
- **适用条件 / 局限** · 依赖较完整的关系及实体解析

**可复用机制** · 分开测试有约束扩候选和最终重排，用固定候选数比较首位命中

<a id="paper-139153"></a>

## AutoHoney: Automating, Deploying, and Evaluating Scheming Honeypots Across Production Codebases

[官方论文页](https://neurips.cc/virtual/2026/poster/139153) · [作者来源](https://openreview.net/forum?id=huudcckaxl)

- **问题 / 瓶颈** · 审计情境会改变模型行为，单一测量可能偏离部署
- **核心创新 / 方法** · 仅记录防御侧的分层审计与人工核验思路
- **Baseline** · 不同任务范围和评估情境对照
- **Benchmark** · 四个代码库上的多模型审计
- **关键结果 / 消融** · 作者报告任务范围与评估情境影响观测结果
- **适用条件 / 局限** · 实验涉及人工设定的冲突，不能外推自然发生率

**可复用机制** · 部署审计报告明确区分受控测试与现场指标

<a id="paper-154589"></a>

## AutoManifold: Agentic Design of Data Visualisation Algorithms via Manifold Embedding

[官方论文页](https://neurips.cc/virtual/2026/poster/154589) · [作者来源](https://openreview.net/forum?id=CSer8vsuhS)

- **问题 / 瓶颈** · 固定嵌入难适配不同结构需求
- **核心创新 / 方法** · 在限定的亲和度、代价和优化原语中按指标生成与迭代配置
- **Baseline** · t-SNE、UMAP、PaCMAP
- **Benchmark** · 多难度真实数据的统一结构保留评测
- **关键结果 / 消融** · 作者报告目标属性改善，其他结构保持可比
- **适用条件 / 局限** · 受原语和指标覆盖限制

**可复用机制** · 将结构目标显式化，并同时报告对目标和非目标结构的影响

<a id="paper-148996"></a>

## Automata from Agent Traces: Failure and Next-Step Prediction

[官方论文页](https://neurips.cc/virtual/2026/poster/148996) · [作者来源](https://openreview.net/forum?id=taEDHOLbwW)

- **问题 / 瓶颈** · 长追踪难从单条路径识别系统性失败
- **核心创新 / 方法** · 前缀树与结构合并得到紧凑状态机，用状态上下文预测下一步和失败
- **Baseline** · Agent Workflow Memory 与无差别告警
- **Benchmark** · 12 个公开数据集，含 SWE-agent 在线监测
- **关键结果 / 消融** · 7–43 个状态，失败预测 AUROC 最高 0.94；八个匹配集下一步预测均改善
- **适用条件 / 局限** · 状态结构可能由执行框架决定

**可复用机制** · 固定框架跨模型验证状态机，统计误告警与可提前停止的比例

<a id="paper-150563"></a>

## Automated Causal Effect Estimation through Self-Evolving AI

[官方论文页](https://neurips.cc/virtual/2026/poster/150563) · [作者来源](https://openreview.net/forum?id=hEJF4xVLvo)

- **问题 / 瓶颈** · 真实效应通常不可观测，方法选择困难
- **核心创新 / 方法** · 以语言模型辅助进化估计器，并在可估计回报下比较
- **Baseline** · 已有估计器与社区比赛提交
- **Benchmark** · 因果效应估计基准与比赛的帕累托比较
- **关键结果 / 消融** · 最佳方法位于 58 个参赛方案的帕累托前沿，代理回报下仍具竞争力
- **适用条件 / 局限** · 估计回报可能与目标误差失配

**可复用机制** · 在可计算真值的合成设置校准代理排名，再用于真实数据

<a id="paper-139723"></a>

## Automated Hypothesis Discovery for Characterizing Annotation Disagreement

[官方论文页](https://neurips.cc/virtual/2026/poster/139723) · [作者来源](https://openreview.net/forum?id=8JQ33Ylm3k)

- **问题 / 瓶颈** · 聚合成单标签会掩盖系统性分歧
- **核心创新 / 方法** · 从多标注集生成自然语言候选解释，并在留出集做统计检验
- **Baseline** · 人工分类体系与预测基线
- **Benchmark** · 半合成数据与四个真实数据集
- **关键结果 / 消融** · 恢复已知分歧来源并发现新假设，预测优于基线
- **适用条件 / 局限** · 显著性须考虑多重比较，预测因子未必是原因

**可复用机制** · 把假设发现与验证拆开，用独立数据报告支持程度

<a id="paper-149210"></a>

## Automated Kernel Discovery Towards Understanding High-dimensional Bayesian Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/149210) · [作者来源](https://openreview.net/forum?id=s7NsKU2IcH)

- **问题 / 瓶颈** · 直接生成代码容易产生形式不同但函数相同的核
- **核心创新 / 方法** · 先提议数学形式再转可验证实现，以 LOO-CRPS 惩罚过度自信
- **Baseline** · 17 种方案，含已有核设计/优化方法
- **Benchmark** · 五个高维贝叶斯优化基准
- **关键结果 / 消融** · 平均名次 1.2，具体开销待核
- **适用条件 / 局限** · 受搜索预算和基准代表性限制

**可复用机制** · 比较边际似然与留一概率评分，记录最终优化遗憾

<a id="paper-148230"></a>

## Automated Reformulation of Robust Optimization via Memory-Augmented Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148230) · [作者来源](https://openreview.net/forum?id=zQKV5SkKAi)

- **问题 / 瓶颈** · 不确定约束的确定化要求多步数学一致性
- **核心创新 / 方法** · 离线反思失败轨迹建结构化文本记忆，推理时检索辅助改革写
- **Baseline** · 无记忆底座及不同语言模型
- **Benchmark** · AutoRO-Bench 的核心改写与应用任务，域内外评估
- **关键结果 / 消融** · 作者报告准确与效率改善，幅度待核
- **适用条件 / 局限** · 形式正确性仍需独立验证

**可复用机制** · 把失败经验和具体模型参数解耦，用求解可行性检查迁移效果

<a id="paper-153609"></a>

## Automatically Refining Coding Rules for AI Coding Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/153609) · [作者来源](https://openreview.net/forum?id=K6zqjHCp8l)

- **问题 / 瓶颈** · 手写规则难适配不同框架和模型
- **核心创新 / 方法** · 维护规则候选池，用生成式变异和评判迭代
- **Baseline** · 手写规则和已有提示优化方法
- **Benchmark** · 两类编程代理框架、四个底座和三个基准
- **关键结果 / 消融** · 作者报告功能正确率、代码长度或成本改善
- **适用条件 / 局限** · 评判器可能过拟合训练任务

**可复用机制** · 用外部功能测试比较规则，避免只优化评判器得分

<a id="paper-151401"></a>

## Automatic Constraint Policy Optimization based on Continuous Constraint Interpolation Framework for Offline Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151401) · [作者来源](https://openreview.net/forum?id=axBS5thYfz)

- **问题 / 瓶颈** · 单一行为约束无法兼顾密度与支持集。
- **核心创新 / 方法** · 用连续参数统一加权克隆、密度和支持约束，再做拉格朗日原对偶更新。
- **Baseline** · 三类固定约束及所比离线方法。
- **Benchmark** · D4RL、NeoRL2 及性能下界分析。
- **关键结果 / 消融** · 作者报告跨域提升；数值待核。
- **适用条件 / 局限** · 依赖可用的离线行为信息。

**可复用机制** · 比较固定约束与可学习插值，检查跨数据质量的敏感性。

<a id="paper-139352"></a>

## Automating ML for Science: Can Frontier Agents Climb Scientific Hills in the Wild?

[官方论文页](https://neurips.cc/virtual/2026/poster/139352) · [作者来源](https://openreview.net/forum?id=Uwbr4qgQyj)

- **问题 / 瓶颈** · 排行榜提升不足以证明研究洞见。
- **核心创新 / 方法** · 以已发表模型为起点做长程优化，分析过程轨迹并对照研究技能插件。
- **Baseline** · 裸代理与带研究技能的版本。
- **Benchmark** · Agent4Sci 的 20 基准、11 领域，测相对提升及过程类型。
- **关键结果 / 消融** · Opus 10.4% 到 20.1%，Codex 4.4% 到 8.1%；常见收益主要来自工程优化。
- **适用条件 / 局限** · 受选用任务、资源和轨迹编码口径限制。

**可复用机制** · 以同一模型分别记录性能增益与贡献类型。

<a id="paper-150660"></a>

## AUTOMEM: Automated Learning of Memory as a Cognitive Skill

[官方论文页](https://neurips.cc/virtual/2026/poster/150660) · [作者来源](https://openreview.net/forum?id=gOtWoYZuUo)

- **问题 / 瓶颈** · 长轨迹中记忆错误难归因。
- **核心创新 / 方法** · 一环复盘并修改记忆结构，另一环从成功片段训练记忆动作。
- **Baseline** · 基础代理及闭源代理参考。
- **Benchmark** · Crafter、MiniHack、NetHack 长程游戏。
- **关键结果 / 消融** · 作者报告仅改记忆表现提高 2–4 倍。
- **适用条件 / 局限** · 其他任务和长期文件状态待验证。

**可复用机制** · 冻结任务动作行为，单独测记忆管理干预。

<a id="paper-139849"></a>

## Automotive-ENV: Benchmarking Multimodal Models in Automotive Cockpit Environments

[官方论文页](https://neurips.cc/virtual/2026/poster/139849) · [作者来源](https://openreview.net/forum?id=0gCfjGPDbH)

- **问题 / 瓶颈** · 动作匹配难判断隐式意图与安全后果。
- **核心创新 / 方法** · 联合界面、车辆信号和安全条件进行确定性校验。
- **Baseline** · 通用多模态与 GUI 专用模型。
- **Benchmark** · Android Automotive OS 的 420 项任务。
- **关键结果 / 消融** · 隐式和安全关键任务明显退化。
- **适用条件 / 局限** · 仿真界面与真实部署存在差异。

**可复用机制** · 跨界面评测优先检查任务状态与约束。

<a id="paper-154225"></a>

## Autonomous Continual Learning for Environment Adaptation of Computer-Use Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/154225) · [作者来源](https://openreview.net/forum?id=FHgXFf6vU1)

- **问题 / 瓶颈** · 环境改变后人工训练任务昂贵。
- **核心创新 / 方法** · 从探索轨迹合成任务，迭代生成课程并使用自动评判。
- **Baseline** · 与未适配行为比较；具名基线待核。
- **Benchmark** · 目标环境及版本、平台、分辨率变化。
- **关键结果 / 消融** · 评判与人工一致率 93%，目标增益报告为 3–29%。
- **适用条件 / 局限** · 自动评判可能随环境偏移。

**可复用机制** · 同时测适配增益与旧环境保持。

<a id="paper-149249"></a>

## Autonomous Scientific Discovery via Iterative Meta-Reflection

[官方论文页](https://neurips.cc/virtual/2026/poster/149249) · [作者来源](https://openreview.net/forum?id=rmLp5XBtAk)

- **问题 / 瓶颈** · 孤立假设搜索难综合多项发现。
- **核心创新 / 方法** · 周期性归纳发现、混杂和探索缺口，并要求统计检验。
- **Baseline** · 经典因果发现及 LLM 引导对照。
- **Benchmark** · iNatDisco 的生态模式恢复。
- **关键结果 / 消融** · 恢复已知模式 8/9，假设支持率 72.7%。
- **适用条件 / 局限** · 相关模式不等于因果；多重检验需复核。

**可复用机制** · 比较是否归纳已验证结果对重复探索与发现覆盖的影响。

<a id="paper-154526"></a>

## Autoregressive Appearance Prediction for 3D Gaussian Avatars

[官方论文页](https://neurips.cc/virtual/2026/poster/154526) · [作者来源](https://openreview.net/forum?id=CwJk23BhSw)

- **问题 / 瓶颈** · 单姿态条件会把外观变化错误归因于姿态。
- **核心创新 / 方法** · 训练编码器提取外观潜变量，驱动时自回归预测并与姿态共同条件化。
- **Baseline** · 摘要未列具名对照。
- **Benchmark** · 高斯化身的重建与新姿态驱动，指标待核。
- **关键结果 / 消融** · 作者报告稳定性和重建改善，幅度待核。
- **适用条件 / 局限** · 长序列误差积累仍待核。

**可复用机制** · 在可见状态不足的渲染任务加入可预测隐状态。

<a id="paper-153481"></a>

## Autoregressive Diffusion World Models for Off-Policy Evaluation of LLM Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/153481) · [作者来源](https://openreview.net/forum?id=L3A07XNiPc)

- **问题 / 瓶颈** · 整轨迹联合扩散忽略文本动作因果顺序。
- **核心创新 / 方法** · 逐步扩散生成环境响应，由目标策略参与每步条件化。
- **Baseline** · 整轨迹扩散和自回归世界模型。
- **Benchmark** · 多轮代理任务，测价值估计和评估可靠性。
- **关键结果 / 消融** · 作者报告估值改善，具体误差待核。
- **适用条件 / 局限** · 依赖日志的覆盖和仿真可信度。

**可复用机制** · 用少量真实回合校准模拟排名。

<a id="paper-154406"></a>

## Autoregressive Learning in Joint KL: Sharp Oracle Bounds and Lower Bounds

[官方论文页](https://neurips.cc/virtual/2026/poster/154406) · [作者来源](https://openreview.net/forum?id=DpKPNTCMWW)

- **问题 / 瓶颈** · 长预测时域影响常被混为一种误差。
- **核心创新 / 方法** · 给出联合 KL 下匹配的上界与信息论下界。
- **Baseline** · 既有 Hellinger 分析。
- **Benchmark** · 错设模型、分解与共享策略类的理论比较。
- **关键结果 / 消融** · 近似因子无时域依赖，估计复杂度仍有时域线性下界。
- **适用条件 / 局限** · 结论针对联合 KL 与论文设定。

**可复用机制** · 报告序列误差时分解近似和估计项。

<a id="paper-151565"></a>

## Auto-Rubric as Reward: From Implicit Preference to Explicit Generative Criteria

[官方论文页](https://neurips.cc/virtual/2026/poster/151565) · [作者来源](https://openreview.net/forum?id=Zf9vqc7AeL)

- **问题 / 瓶颈** · 总分和成对标签遮蔽不同质量维度。
- **核心创新 / 方法** · 用 VLM 写出可分别验证的细则，将判断蒸馏成训练用二元奖励。
- **Baseline** · 成对奖励模型与 VLM 评判器。
- **Benchmark** · 文生图和图像编辑。
- **关键结果 / 消融** · 作者报告位置偏差降低且任务表现改善，幅度待核。
- **适用条件 / 局限** · 细则本身可能遗漏要求。

**可复用机制** · 先固定细则再比较候选，同时测判定偏差。

<a id="paper-151256"></a>

## AutoSaddler: Automatic Harness Optimization with Durable Updates from Agent Execution Traces

[官方论文页](https://neurips.cc/virtual/2026/poster/151256) · [作者来源](https://openreview.net/forum?id=bkGK6zovnv)

- **问题 / 瓶颈** · 局部修复容易过拟合单次失败。
- **核心创新 / 方法** · 复盘小批失败，针对性修改运行配置，再通过验证选保留更新。
- **Baseline** · 原运行框架及浅反思、非约束编辑等消融。
- **Benchmark** · GAIA2、Terminal-Bench 2.0。
- **关键结果 / 消融** · 作者报告分别提高 9 和 10 个百分点。
- **适用条件 / 局限** · 依赖有代表性的验证集。

**可复用机制** · 以留出任务上的稳定改进决定是否接受运行配置变更。

<a id="paper-151734"></a>

## AutoScientists: Self-Organizing Agent Teams for Long-Running Scientific Experimentation

[官方论文页](https://neurips.cc/virtual/2026/poster/151734) · [作者来源](https://openreview.net/forum?id=YTZM5qShYw)

- **问题 / 瓶颈** · 固定研究方向难适应新证据。
- **核心创新 / 方法** · 用公共实验记录协调不同探索方向，交流正负结果。
- **Baseline** · 单代理 autoresearch 及其他多智能体系统。
- **Benchmark** · 这里记录语言模型训练优化实验。
- **关键结果 / 消融** · 作者报告达到目标验证损失速度 1.9 倍。
- **适用条件 / 局限** · 跨任务外推待核，组织策略的单项增益待核。

**可复用机制** · 在计算实验的固定预算下记录重复探索率和有效改进。

<a id="paper-139298"></a>

## AuxGeoAgent: Synthesizing Challenging Geometry Proving Data via Planning and Symbolic Deduction

[官方论文页](https://neurips.cc/virtual/2026/poster/139298) · [作者来源](https://openreview.net/forum?id=YmbnV69f9P)

- **问题 / 瓶颈** · 宽泛扩量不足以覆盖难证几何问题。
- **核心创新 / 方法** · 用符号约束引导构造规划并附完整证明。
- **Baseline** · 百万级和更大合成数据训练方法。
- **Benchmark** · AuxGeo-18K 训练，IMO-30、HAGeo-409 评测。
- **关键结果 / 消融** · 作者报告小数据仍可达到可比表现。
- **适用条件 / 局限** · 自动生成分布不一定代表竞赛题。

**可复用机制** · 按证明结构筛选生成样本而非只增加规模。

<a id="paper-149037"></a>

## Auxiliary Clues Aware’s Geometry Problem Solving

[官方论文页](https://neurips.cc/virtual/2026/poster/149037) · [作者来源](https://openreview.net/forum?id=tKFBJFZMma)

- **问题 / 瓶颈** · 外部绘图不稳，单纯观察已有元素缺少辅助关系。
- **核心创新 / 方法** · 以线索依赖加权 GRPO 优势，并加入辅助线索奖励。
- **Baseline** · 显式绘图与闭源模型。
- **Benchmark** · 多模态几何题；具体测试集待核。
- **关键结果 / 消融** · 作者报告优于显式绘图对照。
- **适用条件 / 局限** · 因果代理和独立消融待核。

**可复用机制** · 分别比较线索加权和直接正确率奖励。

<a id="paper-138887"></a>

## AVENUE: Audio-Video Editing Understanding and Evaluation

[官方论文页](https://neurips.cc/virtual/2026/poster/138887) · [作者来源](https://openreview.net/forum?id=yhjWPeN5lp)

- **问题 / 瓶颈** · 仅测目标修改会漏掉跨模态副作用。
- **核心创新 / 方法** · 对音频、视频与联合编辑设置模态特异的人核验规则。
- **Baseline** · 联合、顺序和分离式编辑模型。
- **Benchmark** · VGGSound 派生的 1291 段和 7957 条指令。
- **关键结果 / 消融** · 三类范式均出现非目标模态变化。
- **适用条件 / 局限** · 真实复杂编辑和人评一致性待核。

**可复用机制** · 把保留约束纳入编辑评测且独立计分。

<a id="paper-139564"></a>

## AVID: A 5T fMRI Dataset for Benchmarking Auditory-induced Visual Mental Imagery Decoding

[官方论文页](https://neurips.cc/virtual/2026/poster/139564) · [作者来源](https://openreview.net/forum?id=IIKVWwmtSM)

- **问题 / 瓶颈** · 视觉提示会混入残留感知或记忆信号。
- **核心创新 / 方法** · 配合复杂场景及受控属性刺激，拆分源图一致与语义对齐。
- **Baseline** · 既有视觉重建流程。
- **Benchmark** · AVID 的九名参与者约 67 小时 5T fMRI。
- **关键结果 / 消融** · 现有重建主要保留粗场景语义。
- **适用条件 / 局限** · 参与者有限，跨设备和语言推广待核。

**可复用机制** · 区分感知输入与待解码内部状态，并独立测细节和语义。

<a id="paper-154518"></a>

## AVI-HT: Adaptive Vision-IMU Fusion for 3D Hand Tracking

[官方论文页](https://neurips.cc/virtual/2026/poster/154518) · [作者来源](https://openreview.net/forum?id=CzwKVs3kov)

- **问题 / 瓶颈** · 相机看不到手指时单视觉容易丢失姿态。
- **核心创新 / 方法** · 用注意力在视觉和各 IMU 间分配权重。
- **Baseline** · 单模态及多模态跟踪，含 UmeTrack 和 MANO 手模型。
- **Benchmark** · DexGloveHOI 十万余同步样本，测关键点误差。
- **关键结果 / 消融** · 平均误差降 16.1%，腕部对齐误差降 24.2%。
- **适用条件 / 局限** · 依赖同步，并对 IMU 噪声敏感。

**可复用机制** · 按遮挡和时间错位分组衡量跨传感融合。

<a id="paper-150182"></a>

## AVIS: Adaptive Test-Time Scaling for Vision–Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150182) · [作者来源](https://openreview.net/forum?id=k6TG2sm2Hc)

- **问题 / 瓶颈** · 只省一类算力会遗漏另一轴的取舍。
- **核心创新 / 方法** · 先按键多样性剪枝，再按预测难度选择自一致性采样次数，共享预填充。
- **Baseline** · 仅缩视觉上下文与仅调整推理采样。
- **Benchmark** · 图像和视频推理任务，测准确率与计算量。
- **关键结果 / 消融** · 作者报告联合策略改善折衷，幅度待核。
- **适用条件 / 局限** · 难度估计和共享缓存条件影响收益。

**可复用机制** · 同一算力下对照二维分配与单轴预算。

<a id="paper-153311"></a>

## AVO: Agentic Variation Operators for Autonomous Evolutionary Search

[官方论文页](https://neurips.cc/virtual/2026/poster/153311) · [作者来源](https://openreview.net/forum?id=MFTuhhh6v1)

- **问题 / 瓶颈** · 固定变异难利用已有候选的经验。
- **核心创新 / 方法** · 用编码代理提出、修复和验证算子实现，保留执行反馈。
- **Baseline** · cuDNN、FlashAttention-4。
- **Benchmark** · B200 上多头与分组查询注意力。
- **关键结果 / 消融** · 多头最高较两者快 3.5% 和 10.5%。
- **适用条件 / 局限** · 搜索耗时七天，跨硬件收益待核。

**可复用机制** · 对比固定变异与反馈式变异，并把搜索开销计入总预算。

<a id="paper-154191"></a>

## AVOC: Enhancing Hour-Level Audio-Video Understanding in Omni-Modal LLMs via Retrieval-Inspired Token Compression

[官方论文页](https://neurips.cc/virtual/2026/poster/154191) · [作者来源](https://openreview.net/forum?id=FW6UJyDapH)

- **问题 / 瓶颈** · 长音视频冗余超出上下文。
- **核心创新 / 方法** · 在编码器与语言模型间训练检索式 Top-K 选择器。
- **Baseline** · 所测次优模型，名称待核。
- **Benchmark** · OmniVideoBench、LVOmniBench、音视频检索。
- **关键结果 / 消融** · 平均准确率分别领先 4.9 和 5.5 点。
- **适用条件 / 局限** · 单小时证据来自检索任务。

**可复用机制** · 在同预算下比较带多样性约束的选取与仅按相关性排序。

<a id="paper-150833"></a>

## Avoiding Feature Collapse in Graph ODEs via Hysteretic Topology Evolution

[官方论文页](https://neurips.cc/virtual/2026/poster/150833) · [作者来源](https://openreview.net/forum?id=exnh1WJ5TA)

- **问题 / 瓶颈** · 正不可约扩散长期趋于秩一共识。
- **核心创新 / 方法** · 用双稳态边势和可微门控演化拓扑。
- **Baseline** · 固定正扩散与理想支持分离。
- **Benchmark** · 共识理论和真实图基准。
- **关键结果 / 消融** · 理想分离产生块内共识；实测幅度待核。
- **适用条件 / 局限** · 平滑抑制不等于严格断开。

**可复用机制** · 区分短期缓解和渐近隔离，并测试边支持实际变化。

<a id="paper-148404"></a>

## Avoiding Obfuscation with Prover-Estimator Debate

[官方论文页](https://neurips.cc/virtual/2026/poster/148404) · [作者来源](https://openreview.net/forum?id=y6MafkaOLE)

- **问题 / 瓶颈** · 不诚实方能造成不对称的验证负担。
- **核心创新 / 方法** · 设计递归证明者与估计者协议来维持计算可比性。
- **Baseline** · 既有递归辩论协议。
- **Benchmark** · 复杂度理论下的辩论正确性。
- **关键结果 / 消融** · 在稳定性假设下诚实方可以用可比计算获胜。
- **适用条件 / 局限** · 尚需验证实际模型和人类评审。

**可复用机制** · 设计递归审核时把反驳成本与提出主张的成本一起计入。

<a id="paper-150780"></a>

## AVSD: Adaptive-View Self-Distillation by Balancing Consensus and Teacher-Specific Privileged Signals

[官方论文页](https://neurips.cc/virtual/2026/poster/150780) · [作者来源](https://openreview.net/forum?id=fRtcETLCZ2)

- **问题 / 瓶颈** · 特权视图中的信息可能无法在推理时恢复。
- **核心创新 / 方法** · 按 token 在几何均值和算术均值间门控，选择性利用视图残差。
- **Baseline** · 单视图自蒸馏、GRPO。
- **Benchmark** · AIME24/25、HMMT25、Codeforces、LiveCodeBench。
- **关键结果 / 消融** · Qwen3-8B 数学 Avg@8 平均提升 3.1%，代码平均提升 2.9%。
- **适用条件 / 局限** · 多视图采集成本与增益需共同比较。

**可复用机制** · 增加教师视图时分开评估共识与视图独有信息。

<a id="paper-154476"></a>

## A World Model of Radiologist Reading for Medical Image Representation Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/154476) · [作者来源](https://openreview.net/forum?id=DJzM2q9amM)

- **问题 / 瓶颈** · 静态注视热图遗漏搜索过程。
- **核心创新 / 方法** · 自回归预测下一注视块潜变量，并补全未观测空间。
- **Baseline** · 诊断表征方法与 LogitGaze-Med。
- **Benchmark** · CheXpert、RSNA Pneumonia、SIIM-ACR、GazeSearch。
- **关键结果 / 消融** · 报告九种监督诊断设置领先，ScanMatch 提升逾 16%。
- **适用条件 / 局限** · 预训练需眼动数据，临床部署效果待验证。

**可复用机制** · 比较按专家观察顺序预训练与仅针对最终标签预训练。

<a id="paper-151192"></a>

## AWP: Activation-based Window Pruning for Gigapixel Object Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/151192) · [作者来源](https://openreview.net/forum?id=cGbkslrrsi)

- **问题 / 瓶颈** · 大图稀疏区域消耗大量算力。
- **核心创新 / 方法** · 把窗口 FFN 平均激活当重要性评分。
- **Baseline** · 既有检测系统、学习式窗口选择。
- **Benchmark** · PANDA、Swin；AP 和 FLOPs。
- **关键结果 / 消融** · PANDA 的 AP50 提高 1.6%、FLOPs 减少 26.2%。
- **适用条件 / 局限** · 激活与小目标相关性需按骨干验证。

**可复用机制** · 在相同剪枝比例下比较激活排序和学习排序，单报小物体召回。

<a id="paper-148243"></a>

## Axiomatic Reinforcement Learning for Open Multi-Agent Systems from Shapley Axioms

[官方论文页](https://neurips.cc/virtual/2026/poster/148243) · [作者来源](https://openreview.net/forum?id=zLFWwz8zKA)

- **问题 / 瓶颈** · 只能控制部分队员时，完全可控设定的贡献分解不直接适用。
- **核心创新 / 方法** · 建立开放团队分解并实例化 Shapley 和 Banzhaf 学习模板。
- **Baseline** · IPPO 和 POAM。
- **Benchmark** · NAHT 任务、未见智能体类型及协作习惯。
- **关键结果 / 消融** · 报告学习效率和泛化改善，幅度待核。
- **适用条件 / 局限** · 依赖设定及价值分解假设。

**可复用机制** · 评估开放队伍价值分解时单测未见队友与未见协作习惯。

<a id="paper-150823"></a>

## Axiomatic World Modeling for Physics Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/150823) · [作者来源](https://openreview.net/forum?id=f21HhDeBNh)

- **问题 / 瓶颈** · 解题者可能在推导前悄然改写题设。
- **核心创新 / 方法** · 分别检查推断的物理世界和具体推导的一致性。
- **Baseline** · 论文所用基线，具体名称待核。
- **Benchmark** · PhysReason、PHYSICS 与未见物理题。
- **关键结果 / 消融** · 报告最高分别提升 10.8、5.2 点。
- **适用条件 / 局限** · 需可靠的物理前提和奖励判定。

**可复用机制** · 在推理训练中将是否正确重述约束与是否正确求解分开验证。

<a id="paper-150051"></a>

## B$^3$-PWL: GPU-Batched Branch-and-Bound for Piecewise-Linear Optimization with SOS2 Constraints

[官方论文页](https://neurips.cc/virtual/2026/poster/150051) · [作者来源](https://openreview.net/forum?id=l7awisNMWs)

- **问题 / 瓶颈** · 逐节点在 CPU 解 LP 难利用 GPU 并行。
- **核心创新 / 方法** · 用 GPU 批处理原始对偶 LP，并配合 SOS2 可行解修复。
- **Baseline** · NVIDIA cuOpt。
- **Benchmark** · 43 个分段线性混合整数实例。
- **关键结果 / 消融** · 几何平均加速 9.25 倍，全部实例得到高质量可行解。
- **适用条件 / 局限** · 可推广程度取决于约束结构和批大小。

**可复用机制** · 把求界和找可行解分别计时，比较批处理是否绕开整体瓶颈。

<a id="paper-154786"></a>

## B2P-Corr: Batch-to-Population Gradient Estimators for Non-Decomposable Correlation Losses

[官方论文页](https://neurips.cc/virtual/2026/poster/154786) · [作者来源](https://openreview.net/forum?id=B0h745L8OJ)

- **问题 / 瓶颈** · 局部均值和协方差使小批梯度有偏。
- **核心创新 / 方法** · 用 EMA 矩草图或跨批 U 统计量构造可分解伪损失。
- **Baseline** · 朴素小批相关损失。
- **Benchmark** · 两个合成和三个真实数据集，测训练稳定性和相关系数。
- **关键结果 / 消融** · 给出朴素梯度偏差量级，报告相关性提高且开销小。
- **适用条件 / 局限** · EMA 分析需要统计估计比参数变化更快。

**可复用机制** · 训练全局统计目标时监测矩估计漂移，再对照朴素批内估计。

<a id="paper-150860"></a>

## Baba in Wonderland: Online Self-Supervised Dynamics Discovery for Executable World Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150860) · [作者来源](https://openreview.net/forum?id=eodh5zWHvN)

- **问题 / 瓶颈** · 新证据拟合可能破坏模型原先解释的行为。
- **核心创新 / 方法** · 用保留冲突划分假设类，并按类别采样反例和探索。
- **Baseline** · 消融类别细化及类别感知探索。
- **Benchmark** · Baba in Wonderland 改名规则环境。
- **关键结果 / 消融** · 作者报告两部分均有益，幅度待核。
- **适用条件 / 局限** · 证据来自特定游戏和可执行程序表示。

**可复用机制** · 迭代更新规则时保存按冲突类型划分的回归用例。

<a id="paper-139168"></a>

## BabyTheorist: A Benchmark for Learning to Theorize the World from Observation Alone

[官方论文页](https://neurips.cc/virtual/2026/poster/139168) · [作者来源](https://openreview.net/forum?id=hApxBFwJyI)

- **问题 / 瓶颈** · 按规则分组的少样本任务跳过了发现规则的环节。
- **核心创新 / 方法** · 用隐藏组合程序生成转移流，控制复杂度、复用频率及跳级测试。
- **Baseline** · 七种代表性方法。
- **Benchmark** · BabyTheorist 的持续视觉转移课程。
- **关键结果 / 消融** · 基线低于上限且差距随课程扩大。
- **适用条件 / 局限** · 生成规则空间与真实开放环境有差异。

**可复用机制** · 测组合归纳时移除任务标记，并检验跳过训练层级后的迁移。

<a id="paper-151970"></a>

## BACE: Behavior-Adaptive Connectivity Estimation from Multi-Region Neural Recordings

[官方论文页](https://neurips.cc/virtual/2026/poster/151970) · [作者来源](https://openreview.net/forum?id=WSGT96IPb3)

- **问题 / 瓶颈** · 固定网络可能平均掉任务阶段间的依赖。
- **核心创新 / 方法** · 用区域时序编码、行为选择的邻接矩阵与自回归解码联合拟合。
- **Baseline** · 合成真图和真实数据的预测对照，具名方法待核。
- **Benchmark** · 合成序列及三位参与者的深脑记录。
- **关键结果 / 消融** · 合成任务从预测恢复已知边，真实记录得到稳定行为条件图。
- **适用条件 / 局限** · 预测依赖不等同因果，实测样本小。

**可复用机制** · 先用有真图的合成序列验证恢复，再报告实测边跨重复任务的稳定性。

<a id="paper-154161"></a>

## Backbone-Equated Diffusion OOD via Sparse Internal Snapshots

[官方论文页](https://neurips.cc/virtual/2026/poster/154161) · [作者来源](https://openreview.net/forum?id=FoLkIskdnj)

- **问题 / 瓶颈** · 骨干和噪声参数差异影响扩散检测器排名。
- **核心创新 / 方法** · 对齐规范噪声和测试成本，从冻结模型取少量低噪状态。
- **Baseline** · 完整去噪、大型探针与小型快照变体。
- **Benchmark** · 受控 CIFAR 规模的分布外检测。
- **关键结果 / 消融** · 单次前向版本表现强，解码器精简版本仍有竞争力。
- **适用条件 / 局限** · 更大数据和其他异常类型待验证。

**可复用机制** · 比较复杂检测器前先做成本匹配的内部层探针。

<a id="paper-155957"></a>

## Backdoor Attacks Rerouted: BatchNorm as a Sink for Adversarial Signals

[官方论文页](https://neurips.cc/virtual/2026/poster/155957) · [作者来源](https://neurips.cc/virtual/2026/poster/155957)

- **问题 / 瓶颈** · 只看干净准确率无法衡量模型受污染后的可靠性。
- **核心创新 / 方法** · 在验证环境评估重新估计归一化统计的免训练防御。
- **Baseline** · 九种防御方法。
- **Benchmark** · 八种黑盒与三种解释相关威胁设置，同时检查干净样本。
- **关键结果 / 消融** · 报告攻击成功率从 100% 降至 1%，保持干净性能。
- **适用条件 / 局限** · 需在隔离条件下复核校准数据及跨架构表现。

**可复用机制** · 验收模型时同时记录防御前后干净性能、失败率和解释可靠性。

<a id="paper-153189"></a>

## Backdoor Purification for LoRA-Tuned LLMs via Null-Space Projection

[官方论文页](https://neurips.cc/virtual/2026/poster/153189) · [作者来源](https://neurips.cc/virtual/2026/poster/153189)

- **问题 / 瓶颈** · 现有净化可能依赖干净参考或重训练，并损伤下游能力。
- **核心创新 / 方法** · 估计可疑方向，对 LoRA 更新实施正交投影。
- **Baseline** · 依赖参考、已知触发信息或重训练的方案；具名对照待核。
- **Benchmark** · 从分类单层实验到生成式大模型，测净化与良性能力。
- **关键结果 / 消融** · 作者报告攻击成功率近 100% 降至低于 10%，保留良性和适配技能。
- **适用条件 / 局限** · 可疑方向的估计误差可能误删有效特征。

**可复用机制** · 报告净化前后安全指标、基础能力和适配能力，避免只看一项。

<a id="paper-148405"></a>

## Back to Blackwell: Closing the Loop on Intransitivity in Multi-Objective Preference Fine-Tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/148405) · [作者来源](https://openreview.net/forum?id=y6JzBUPPdU)

- **问题 / 瓶颈** · 标量化可能产生循环排序，标准最优策略假设失效。
- **核心创新 / 方法** · 定义最大熵 Blackwell 胜者，推导 PROSPER 学习算法。
- **Baseline** · 既有偏好微调与自博弈类方法，具体名称待核。
- **Benchmark** · 多目标模型评委上的指令遵循和通用聊天。
- **关键结果 / 消融** · 所测基准优于所列对照，幅度待核。
- **适用条件 / 局限** · 依赖多目标评委的质量和成本。

**可复用机制** · 训练前检查偏好循环，用固定反馈预算比较直接多目标与标量压缩。

<a id="paper-155253"></a>

## Backtracking with Linear-in-Depth Search-Space Growth: Width-Limited Tree Search for Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155253) · [作者来源](https://openreview.net/forum?id=7683TYQZFN)

- **问题 / 瓶颈** · 不可回溯的序列搜索易锁死错误前缀，树搜索又可能指数增长
- **核心创新 / 方法** · 动态判定节点可扩展性并施加逐层宽度上限
- **Baseline** · 序列与树搜索
- **Benchmark** · 数学、代码和逻辑推理；分类及生成验证器
- **关键结果 / 消融** · 作者报告精度和预算效率提升，树规模随深度线性增长
- **适用条件 / 局限** · 答案一致性早停依赖答案可规范化

**可复用机制** · 同预算比较有无回溯及宽度约束

<a id="paper-153699"></a>

## Balanced Multi-Task Learning from an Optimality-Gap Perspective

[官方论文页](https://neurips.cc/virtual/2026/poster/153699) · [作者来源](https://openreview.net/forum?id=JQs8iJ1C2j)

- **问题 / 瓶颈** · 各任务损失尺度不同，共享更新的进展难比较
- **核心创新 / 方法** · 按单任务一步最优进展归一化，最大化最差进展；用活跃集识别瓶颈
- **Baseline** · 常规多任务优化，名称待核
- **Benchmark** · 多任务基准与任务平衡
- **关键结果 / 消融** · 作者报告平衡改善且性能可比
- **适用条件 / 局限** · 闭式解依赖各向同性局部曲率近似

**可复用机制** · 比较损失尺度与局部改进上限两种归一化

<a id="paper-151310"></a>

## Balancing Frequencies and Pixels in Flow Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/151310) · [作者来源](https://openreview.net/forum?id=bR1U2URUlk)

- **问题 / 瓶颈** · 像素流匹配由低频主导，延迟细节学习
- **核心创新 / 方法** · 先用焦点对数频率损失强化高频，再用像素速度损失精修
- **Baseline** · 标准像素流匹配
- **Benchmark** · 多模型规模、FID 与感知质量
- **关键结果 / 消融** · 收敛最多加快 40%，作者报告 FID 改善
- **适用条件 / 局限** · 切换时点与数据频谱依赖待核

**可复用机制** · 分别消融频谱监督和阶段切换

<a id="paper-155939"></a>

## Balancing Image Compression and Generation with Bootstrapped Tokenization

[官方论文页](https://neurips.cc/virtual/2026/poster/155939) · [作者来源](https://openreview.net/forum?id=1fSMXPTPyJ)

- **问题 / 瓶颈** · 局部与全局信息混合造成 token 冗余
- **核心创新 / 方法** · 通过自举从全局码预测局部细节，生成器仅生成全局码
- **Baseline** · 混合粒度分词
- **Benchmark** · 图像重建、生成及 gFID
- **关键结果 / 消融** · 计算约降 40%；64 token 下 gFID 1.56
- **适用条件 / 局限** · 细节受全局信息瓶颈影响

**可复用机制** · 固定 token 预算对照分层与混合编码

<a id="paper-152565"></a>

## BAL: Bidirectional Autoregression in Latent Space for Learning Human Movement Representations

[官方论文页](https://neurips.cc/virtual/2026/poster/152565) · [作者来源](https://openreview.net/forum?id=SC5WzkPwB6)

- **问题 / 瓶颈** · 人工掩码或增强规则影响动作语义
- **核心创新 / 方法** · 双向预测潜在动作，拆开全局语义和局部运动以抑制塌缩
- **Baseline** · 自监督动作表征方法
- **Benchmark** · 动作描述、预测及插值
- **关键结果 / 消融** · 作者报告三类任务均改善
- **适用条件 / 局限** · 双向提取需要未来上下文

**可复用机制** · 分别消融双向训练与局部目标

<a id="paper-149366"></a>

## BalCapRL : A Balanced Framework for RL-Based MLLM Image Captioning

[官方论文页](https://neurips.cc/virtual/2026/poster/149366) · [作者来源](https://openreview.net/forum?id=qZ70ixJOjT)

- **问题 / 瓶颈** · 单维图像描述奖励易诱发冗长、泛化描述或幻觉
- **核心创新 / 方法** · 对连续多目标奖励解耦归一化，并按长度掩码
- **Baseline** · 普通 GRPO
- **Benchmark** · LLaVA、Qwen2.5-VL；DCScore、CaptionQA、CapArena
- **关键结果 / 消融** · 指标峰值增益分别为 13.6、9.0、29.0
- **适用条件 / 局限** · 峰值来自不同底座

**可复用机制** · 分别测长度、忠实性和表达后再调组合奖励

<a id="paper-154569"></a>

## Ballad: Bandit-Based LLM Routing for Automated Heuristic Discovery

[官方论文页](https://neurips.cc/virtual/2026/poster/154569) · [作者来源](https://openreview.net/forum?id=CdDR7cp69H)

- **问题 / 瓶颈** · 启发式搜索中不同模型的价值随阶段和上下文变化
- **核心创新 / 方法** · 按稀有优质结果路由，沿候选谱系传播信用并折扣旧反馈
- **Baseline** · 固定单模型调用
- **Benchmark** · 五类组合优化问题、四种模型
- **关键结果 / 消融** · 可匹配事后最强单模型，API 成本最多降 65.6%
- **适用条件 / 局限** · 需记录候选谱系并量化质量

**可复用机制** · 同预算对照均值路由与谱系信用

<a id="paper-150212"></a>

## BALTO: Balanced Token-Level Policy Optimization for Hallucination Mitigation

[官方论文页](https://neurips.cc/virtual/2026/poster/150212) · [作者来源](https://openreview.net/forum?id=juI26tTO3o)

- **问题 / 瓶颈** · 整段忠实性奖励会惩罚同段正确内容
- **核心创新 / 方法** · 核对主张与参考，投影为平衡的 token 信用
- **Baseline** · 响应级奖励、已有后训练方法
- **Benchmark** · ConFiQA、RAGTruth、FinLLM-Eval 与 Q-Score
- **关键结果 / 消融** · 作者报告六个设置忠实性均领先
- **适用条件 / 局限** · 依赖主张切分及验证可靠性

**可复用机制** · 在混合正误回答中对照局部和整段奖励

<a id="paper-155168"></a>

## Bandits via Additive Quantized Representations

[官方论文页](https://neurips.cc/virtual/2026/poster/155168) · [作者来源](https://openreview.net/forum?id=7n363oEuwb)

- **问题 / 瓶颈** · 在线线性模型表达受限，非线性重训占内存
- **核心创新 / 方法** · 用离线残差量化码本建立多级可加特征
- **Baseline** · 无量化版本、重训 XGBoost 及神经方法
- **Benchmark** · 13 个上下文赌博机数据集；效果与内存
- **关键结果 / 消融** · 11 个数据集优于无量化，内存最多低三个数量级
- **适用条件 / 局限** · 码本依赖离线上下文覆盖

**可复用机制** · 固定内存比较原特征及分级量化表示

<a id="paper-139094"></a>

## BankerToolBench: Evaluating AI Agents in End-to-End Investment Banking Workflows

[官方论文页](https://neurips.cc/virtual/2026/poster/139094) · [作者来源](https://openreview.net/forum?id=lPjj0sxRGD)

- **问题 / 瓶颈** · 单文档或工具正确率无法覆盖实际交付
- **核心创新 / 方法** · 用行业专家细粒度标准评估工具链和跨文档交付
- **Baseline** · 九种前沿模型及从业者人工审核
- **Benchmark** · BankerToolBench，一百多项标准
- **关键结果 / 消融** · 最佳模型仍未满足近半标准，人工评定可直接交付比例为零
- **适用条件 / 局限** · 受行业任务与评审标准影响

**可复用机制** · 分别统计单产物错误与跨文档矛盾

<a id="paper-155064"></a>

## BAPM: Boundary-Aware Prompt Mining for Training-Free Few-Shot Medical Image Segmentation

[官方论文页](https://neurips.cc/virtual/2026/poster/155064) · [作者来源](https://openreview.net/forum?id=8jdITJxUI9)

- **问题 / 瓶颈** · 普通负提示可能引入边界歧义
- **核心创新 / 方法** · 多中心前景原型配合边界背景过滤，向 SAM 提供正负提示
- **Baseline** · 仅正提示与普通负提示
- **Benchmark** · Abd-MRI、Abd-CT
- **关键结果 / 消融** · 作者报告一致改善，幅度待核
- **适用条件 / 局限** · 依赖支持样本及边界候选质量

**可复用机制** · 同预算比较随机负提示和可信边界负提示

<a id="paper-148333"></a>

## BarrierSteer: LLM Safety via Learning Barrier Steering

[官方论文页](https://neurips.cc/virtual/2026/poster/148333) · [作者来源](https://openreview.net/forum?id=ycSLi4NJY3)

- **问题 / 瓶颈** · 生成模型可能产生不安全输出
- **核心创新 / 方法** · 将隐状态安全分类器作为控制障碍函数，并合并多个安全约束
- **Baseline** · 已有生成安全控制方法
- **Benchmark** · 多模型及安全数据集，评价安全与实用性
- **关键结果 / 消融** · 作者报告不安全输出减少且实用性保持
- **适用条件 / 局限** · 保证取决于边界能否刻画目标安全属性

**可复用机制** · 联合测量漏判、误拒与任务质量

<a id="paper-153096"></a>

## Barycentric Guidance: Turning Foundation Image Editors into Continuous Affective Controllers

[官方论文页](https://neurips.cc/virtual/2026/poster/153096) · [作者来源](https://openreview.net/forum?id=Nx9IIc3xpv)

- **问题 / 瓶颈** · 文本提示插值难提供可靠情感强度控制
- **核心创新 / 方法** · 用单纯形重心权重把效价和唤醒度映射为编辑引导
- **Baseline** · 已有情感编辑方法
- **Benchmark** · 三个面部数据集，准确度、覆盖与多样性
- **关键结果 / 消融** · 目标准确度提高 25–29%，覆盖提高 28–50%
- **适用条件 / 局限** · 依赖情感评估器与单纯形覆盖

**可复用机制** · 用控制平面全域误差替代少量端点测试

<a id="paper-156066"></a>

## Base Items Overfit, New Items Underfit: Hidden Cost of Joint Training in Incremental Adaptation

[官方论文页](https://neurips.cc/virtual/2026/poster/156066) · [作者来源](https://openreview.net/forum?id=0ianGd8N9W)

- **问题 / 瓶颈** · 旧条目已过拟合时新条目仍在欠拟合
- **核心创新 / 方法** · 为新旧群体使用独立低秩投影并考察冻结变体
- **Baseline** · 联合微调、EWC、ADER
- **Benchmark** · 推荐和语言模型词表扩展
- **关键结果 / 消融** · 推荐报告帕累托优势，新增参数可为全秩四分之一
- **适用条件 / 局限** · 需区分群体并保留旧项评测样本

**可复用机制** · 绘制旧新质量随训练时长变化的独立曲线

<a id="paper-150159"></a>

## BasicLT: Basic-Level Abstraction and Selective Differentiation for Long-Tailed Recognition

[官方论文页](https://neurips.cc/virtual/2026/poster/150159) · [作者来源](https://openreview.net/forum?id=kDIQv2X2Ly)

- **问题 / 瓶颈** · 尾类粗语义尚不可靠时已被迫细分
- **核心创新 / 方法** · 对齐粗类分支，并用冻结教师筛选可信中少样本进行细化
- **Baseline** · 长尾识别基线与模块消融
- **Benchmark** · CIFAR-LT、ImageNet-LT、iNaturalist 2018、Places-LT
- **关键结果 / 消融** · 中少样本改善最稳定
- **适用条件 / 局限** · 需要可用语义层次和粗类置信

**可复用机制** · 按类频率和粗类置信分组测细化收益

<a id="paper-152400"></a>

## BASIL-DCM: Biophysical Amortized Scalable Inference for Latent Dynamic Causal Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/152400) · [作者来源](https://openreview.net/forum?id=TNI4xmMH1Y)

- **问题 / 瓶颈** · 逐样本反演难扩展至全脑和大队列
- **核心创新 / 方法** · 结合状态空间时间编码与脑区注意力，用前向模型约束谱一致性
- **Baseline** · 变分拉普拉斯反演、回归 DCM 初始化
- **Benchmark** · 基于 HCP 静息态 fMRI 的连接及参数推断
- **关键结果 / 消融** · 单次前向估计，误差和速度细节待核
- **适用条件 / 局限** · 依赖生成模型与训练参数覆盖

**可复用机制** · 用前向谱一致性验证摊销生成参数

<a id="paper-154941"></a>

## Basis-Mediated Bilinear Attention: A New Method for Greatly Reducing Query--Key Pathway Parameters

[官方论文页](https://neurips.cc/virtual/2026/poster/154941) · [作者来源](https://openreview.net/forum?id=9mEBiUiVG1)

- **问题 / 瓶颈** · 独立逐头查询键投影开销高
- **核心创新 / 方法** · 跨头共享潜在基，保留头专属轻量双线性交互
- **Baseline** · 标准注意力、共享及低秩方案
- **Benchmark** · ViT-Base ImageNet-1K 与 GPT-2 small C4 子集
- **关键结果 / 消融** · 查询键参数最多减 95.83%，基准表现可比
- **适用条件 / 局限** · 比例仅指查询键参数，墙钟收益待核

**可复用机制** · 同预算比较共享基、完全共享和独立低秩

<a id="paper-151263"></a>

## BASTION: Budget-Aware Speculative Decoding with Tree-structured Block Diffusion Drafting

[官方论文页](https://neurips.cc/virtual/2026/poster/151263) · [作者来源](https://openreview.net/forum?id=bggNOfjAjb)

- **问题 / 瓶颈** · 固定推测验证预算不适应模型、上下文和硬件变化
- **核心创新 / 方法** · 用草稿接受率代理及在线时延模型逐轮选验证树预算
- **Baseline** · 标准自回归与 DFlash
- **Benchmark** · 多模型、温度、GPU 和任务的实际时延
- **关键结果 / 消融** · 最高加速 6.93 倍，加速比较 DFlash 高约 40%
- **适用条件 / 局限** · 依赖时延和接受率估计

**可复用机制** · 相同草稿下比较固定及自适应预算

<a id="paper-153286"></a>

## BAT3R: Robust Online 3D Reconstruction with Bayesian Adaptive State Updates

[官方论文页](https://neurips.cc/virtual/2026/poster/153286) · [作者来源](https://openreview.net/forum?id=MP758ZsHYv)

- **问题 / 瓶颈** · 无差别状态更新会在长序列累积误差
- **核心创新 / 方法** · 以初始化约束防漂移，用信息增益及交叉注意力做不对称时空更新
- **Baseline** · 在线三维重建方法
- **Benchmark** · 7-Scenes、TUM、ScanNet、KITTI
- **关键结果 / 消融** · 作者报告长序列及复杂场景收益最明显
- **适用条件 / 局限** · 空间相关性不等同置信度已校准

**可复用机制** · 分开测历史区域保护及新场景更新

<a id="paper-148295"></a>

## BA-T: An Iterative Transformer for Two-View Bundle Adjustment

[官方论文页](https://neurips.cc/virtual/2026/poster/148295) · [作者来源](https://openreview.net/forum?id=yvXR9Dq8Oc)

- **问题 / 瓶颈** · 深注意力解码器缺少显式迭代几何更新
- **核心创新 / 方法** · 重复使用轻量束调整式层，在隐 token 中更新位姿和几何残差
- **Baseline** · 常规深解码器及较大模型
- **Benchmark** · 双视图位姿、重建及跨视图一致性
- **关键结果 / 消融** · 以约 16% 解码参数匹配或超过较大模型
- **适用条件 / 局限** · 迭代次数增加会提高时延

**可复用机制** · 同延迟比较重复几何层和加深解码器

<a id="paper-154091"></a>

## Batch-Conditioned Semantic Anchors for Robust Transductive Adaptation of Vision--Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154091) · [作者来源](https://openreview.net/forum?id=GIhENJuWAs)

- **问题 / 瓶颈** · 固定原型欠适配，自由更新会漂移
- **核心创新 / 方法** · 联合估计批次先验和软图像原型，再将可靠证据输运到文本锚点
- **Baseline** · TransCLIP、StatA
- **Benchmark** · 标准集、稀疏类、全类及在线流
- **关键结果 / 消融** · 作者报告各设定优于对照，稀疏和先验偏移批次收益最大
- **适用条件 / 局限** · 依赖批次可靠性估计

**可复用机制** · 分别监控锚点漂移和缺席类别的预测质量。

<a id="paper-150229"></a>

## Batched Stochastic Linear Bandits with 1-Bit Communication Constraints

[官方论文页](https://neurips.cc/virtual/2026/poster/150229) · [作者来源](https://openreview.net/forum?id=jpquydFTHZ)

- **问题 / 瓶颈** · 低频上传与低位宽同时限制探索
- **核心创新 / 方法** · 以 G 最优设计和一位均值估计实施分阶段淘汰，另有安全臂热启动变体
- **Baseline** · 逐轮量化与总位预算是相邻设定
- **Benchmark** · 随机线性赌博机，每批仅回一位，评估极小极大遗憾
- **关键结果 / 消融** · 无噪声仍有与批长成比例的下界，两个算法分别在不同规模区间近最优
- **适用条件 / 局限** · 单比特规则可依赖历史回复但不能直接读取旧奖励

**可复用机制** · 分离通信导致的遗憾和统计误差再选择批长。

<a id="paper-153708"></a>

## Baton: Explicit Semantic Blueprints for Joint Video-Audio Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/153708) · [作者来源](https://openreview.net/forum?id=JMIXvPCjrz)

- **问题 / 瓶颈** · 粗文本条件缺少可共享的长程事件次序
- **核心创新 / 方法** · 跨注意力生成对齐的音视频计划 token，以相对位置编码对齐计划和扩散潜变量
- **Baseline** · 粗文本引导的联合扩散方法，具名待核
- **Benchmark** · 音视频生成基准，定性及定量指标待核
- **关键结果 / 消融** · 报告同步和语义生成改善，幅度待核
- **适用条件 / 局限** · 计划 token 与潜变量不逐点对应

**可复用机制** · 在同骨干上比较仅文本引导与预对齐计划引导。

<a id="paper-150593"></a>

## BayesAT: Bayes-Guided Progressive Distillation for Semi-Supervised Adversarial Training

[官方论文页](https://neurips.cc/virtual/2026/poster/150593) · [作者来源](https://openreview.net/forum?id=h1DIkm1KJC)

- **问题 / 瓶颈** · 固定难度忽视学生能力变化
- **核心创新 / 方法** · 分析阶段性偏差方差权衡，联合温度升温与置信度重加权
- **Baseline** · 静态硬伪标签或固定软标签的半监督鲁棒训练
- **Benchmark** · CIFAR-10、CIFAR-100、ImageNet-200，鲁棒及自然准确率
- **关键结果 / 消融** · 作者报告鲁棒准确率提升，自然准确率保持
- **适用条件 / 局限** · 结论依赖教师置信度与所测设定

**可复用机制** · 同时扫温度日程和置信重加权，记录干净和鲁棒指标。

<a id="paper-152064"></a>

## Bayesian Additive Distribution Regression

[官方论文页](https://neurips.cc/virtual/2026/poster/152064) · [作者来源](https://openreview.net/forum?id=Vjv0vxvgq9)

- **问题 / 瓶颈** · 组级结果依赖分布而非单个样本
- **核心创新 / 方法** · 对线性泛函的 Riesz 表示施加 BART 先验，并将采样树转为随机特征以加速
- **Baseline** · 核方法是理论参照，实验对照待核
- **Benchmark** · 合成及真实分布回归，并给出后验集中率
- **关键结果 / 消融** · 报告自适应集中率和可扩展近似，幅度待核
- **适用条件 / 局限** · 低维边际主导时先验更合适

**可复用机制** · 用先验采样树做稀疏贝叶斯回归，保留预测不确定性。

<a id="paper-154383"></a>

## Bayesian Backprop as Belief Propagation: Single-Pass Predictive Uncertainty

[官方论文页](https://neurips.cc/virtual/2026/poster/154383) · [作者来源](https://openreview.net/forum?id=Dz8Fnt62Zc)

- **问题 / 瓶颈** · 集成和后验样本增加服务成本
- **核心创新 / 方法** · 以高斯权重信念和激活矩改写计算图，以反向伴随和局部 Fisher 矩更新近似 EP
- **Baseline** · 确定性校准、集成、dropout、Laplace、SWAG 和变分方法
- **Benchmark** · 校准、选择性预测和分布外行为
- **关键结果 / 消融** · 作者展示单次前向可实现后验预测矩，比较数值待核
- **适用条件 / 局限** · 矩近似可能遗漏多峰或高阶依赖

**可复用机制** · 固定延迟预算测试单遍矩传播与采样推理的拒答质量。

<a id="paper-154028"></a>

## Bayesian Causal Experimental Design for CATE Estimation under Noncompliance

[官方论文页](https://neurips.cc/virtual/2026/poster/154028) · [作者来源](https://openreview.net/forum?id=Gn2UDJPl9p)

- **问题 / 瓶颈** · 结果预测不确定性未必是 CATE 不确定性
- **核心创新 / 方法** · 对处理实现及结果的联合反馈计算目标群体 CATE 信息增益，用经验贝叶斯 GP 近似
- **Baseline** · 自适应实验设计基线，具名待核
- **Benchmark** · 合成和两个半合成工具变量基准及真实标签诊断
- **关键结果 / 消融** · 作者报告样本效率与全数据估计恢复改善
- **适用条件 / 局限** · 依赖工作后验及工具变量假设

**可复用机制** · 按所关心因果量选查询，单测忽略处理实现反馈造成的信息损失。

<a id="paper-155177"></a>

## Bayesian Causal Stress Testing: Posterior Fragility of Treatment-Effect Conclusions

[官方论文页](https://neurips.cc/virtual/2026/poster/155177) · [作者来源](https://openreview.net/forum?id=7jQK8u7uLb)

- **问题 / 瓶颈** · 估计精确不代表因果假设稳固
- **核心创新 / 方法** · 将后验支持降至指定阈值所需的最小校准扰动定义为脆弱度
- **Baseline** · Cinelli–Hazlett 鲁棒值、多类贝叶斯后验
- **Benchmark** · IHDP、TWINS、ACIC-cov+Hill，另有已知混杂诊断
- **关键结果 / 消融** · 线性后验校准 RMS 为 0.001，已知混杂实验平均绝对误差为 0.03
- **适用条件 / 局限** · 非线性后验在小效应下有较大差异

**可复用机制** · 用假设压力测试补充可信区间，区分结论精度与对假设的敏感性。

<a id="paper-149882"></a>

## Bayesian Decision Making around Experts

[官方论文页](https://neurips.cc/virtual/2026/poster/149882) · [作者来源](https://openreview.net/forum?id=mVsJcNjcSu)

- **问题 / 瓶颈** · 专家数据有成本且可能不可靠
- **核心创新 / 方法** · 在线和离线贝叶斯赌博机中分开建模专家后验贡献，提出信息引导分配规则
- **Baseline** · 自身经验更新与使用专家数据的设定
- **Benchmark** · 贝叶斯多臂赌博机及信息论遗憾界
- **关键结果 / 消融** · 量化了专家数据的预训练与在线收益，实验详情待核
- **适用条件 / 局限** · 信息模型和信任估计必须可信

**可复用机制** · 将专家结果作为独立来源，按可预期信息收益而非来源身份分配更新。

<a id="paper-150567"></a>

## Bayesian Optimization on Function Spaces via Sparse RKHS Manifolds

[官方论文页](https://neurips.cc/virtual/2026/poster/150567) · [作者来源](https://openreview.net/forum?id=hBh55r5Asy)

- **问题 / 瓶颈** · 任意离散化会产生高维且复杂的候选
- **核心创新 / 方法** · 将搜索限制到由稀疏核函数展开的 RKHS 子流形
- **Baseline** · 既有函数贝叶斯优化方法，具名待核
- **Benchmark** · 将有限维测试函数扩展到无限维构建基准
- **关键结果 / 消融** · 报告多种任务表现改善，幅度待核
- **适用条件 / 局限** · 解需能被稀疏核基有效近似

**可复用机制** · 按函数结构设计低复杂度搜索空间，再与等预算的直接离散化比较。

<a id="paper-156134"></a>

## Bayesian Optimization with Fisher Information Geometry: Gradient Bounds and Trust-Region Methods

[官方论文页](https://neurips.cc/virtual/2026/poster/156134) · [作者来源](https://openreview.net/forum?id=09tcl9K6o8)

- **问题 / 瓶颈** · 高维采集梯度易消失，长度尺度并非所有模型都具备
- **核心创新 / 方法** · 将 Fisher 度量拉回输入空间，并以局部权重缩放信赖域
- **Baseline** · 长度尺度缩放及 RAASP 等相邻启发式
- **Benchmark** · SE 核 GP 及非各向同性代理基准
- **关键结果 / 消融** · SE 核下有竞争力，其他代理上增益更依赖任务
- **适用条件 / 局限** · 需要可计算的后验敏感度

**可复用机制** · 在同一代理下比较后验度量和固定长度尺度信赖域。

<a id="paper-150486"></a>

## Bayesian Preference Learning for Test-Time Steerable Reward Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150486) · [作者来源](https://openreview.net/forum?id=hjMgNSnHgL)

- **问题 / 瓶颈** · 静态奖励模型难适配测试时偏好
- **核心创新 / 方法** · 在 Bradley–Terry 模型和 Beta 先验下做摊销变分推断
- **Baseline** · 传统奖励模型与生成式评判器
- **Benchmark** · RM-Bench、道德困境、冲突偏好及数学 RL
- **关键结果 / 消融** · RM-Bench 准确率 60.5 升至 70.8，多目标前沿扩大
- **适用条件 / 局限** · 依赖示例代表目标偏好和比较模型的适配性

**可复用机制** · 比较固定奖励与上下文奖励在新偏好及有限示例时的校准。

<a id="paper-152715"></a>

## Bayesian Test-Time Inference of Task-Aligned Similarity from Weak Interactive Feedback

[官方论文页](https://neurips.cc/virtual/2026/poster/152715) · [作者来源](https://openreview.net/forum?id=QtmggfhlQ9)

- **问题 / 瓶颈** · 词面、结构等相似性指标随实例变化
- **核心创新 / 方法** · 维持候选与相似性轴的联合后验，用信息增益选择探测
- **Baseline** · 固定混合、重排序与等算力 best-of-N
- **Benchmark** · 概念恢复、示例选择、回答修订和干扰条件
- **关键结果 / 消融** · 共享候选和预算时平均增益温和，轴偏移时差距扩大
- **适用条件 / 局限** · 要预先给出有意义的候选轴和噪声模型

**可复用机制** · 把相似性指标当潜变量，固定反馈预算测试静态与自适应选择。

<a id="paper-138918"></a>

## BayesJudge: Uncertainty-Aware Bayesian Meta-Evaluation of Human and LLM Judgments

[官方论文页](https://neurips.cc/virtual/2026/poster/138918) · [作者来源](https://openreview.net/forum?id=wxiKp62nSu)

- **问题 / 瓶颈** · 评分冲突可能源于歧义、人群差异或顺序
- **核心创新 / 方法** · 在线贝叶斯联合估计裁决分布、人类混淆矩阵和模型顺序偏差
- **Baseline** · 合成受控对照，其他基线待核
- **Benchmark** · 受控合成流与 SummEval，考察参数恢复和评判分歧
- **关键结果 / 消融** · 检测到顺序效应，后验不确定性与人类分歧相关
- **适用条件 / 局限** · 推断是相对评判群体的，依赖数据量与标签协议

**可复用机制** · 在双向配对调用中保留歧义标签，避免把位置偏好混进质量标签。

<a id="paper-152377"></a>

## Bayes-Optimal BER and AUC: Estimation and Evaluation of Estimators

[官方论文页](https://neurips.cc/virtual/2026/poster/152377) · [作者来源](https://openreview.net/forum?id=TXjUGPqJQu)

- **问题 / 瓶颈** · 真实数据最优指标不可观测，软标签也可能系统变形
- **核心创新 / 方法** · 用辅助硬标签做保序回归校正软标签，扩展 FeeBee 验证估计器
- **Baseline** · FeeBee 的原始贝叶斯误差估计设定
- **Benchmark** · 合成及真实二分类数据，估计最优 BER、AUC
- **关键结果 / 消融** · 给出有限样本界并报告实证验证
- **适用条件 / 局限** · 软标签失真需近似保序，硬标签须有代表性

**可复用机制** · 估计模型改进空间时选择符合评价目标的贝叶斯上限。

<a id="paper-149379"></a>

## Bayes-pFCL:Bayesian Personalized Federated Continual Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149379) · [作者来源](https://openreview.net/forum?id=qV1obunXod)

- **问题 / 瓶颈** · 任务遗忘和客户异质性都影响个性化
- **核心创新 / 方法** · 以贝叶斯后验度量模型内与模型间干扰，并加入本地损失
- **Baseline** · 个性化联邦持续学习方法，具名待核
- **Benchmark** · 合成和真实数据持续学习，指标待核
- **关键结果 / 消融** · 给出两种损失的界并报告相对基线改善
- **适用条件 / 局限** · 后验估计误差可能影响干扰惩罚

**可复用机制** · 把时间上的遗忘和跨端聚合干扰拆开诊断与正则。

<a id="paper-154974"></a>

## BayesRAG: Probabilistic Mutual Evidence Corroboration for Multimodal Retrieval-Augmented Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/154974) · [作者来源](https://openreview.net/forum?id=9Vk5e1o3lU)

- **问题 / 瓶颈** · 独立余弦排序丢失跨模态一致性
- **核心创新 / 方法** · 以贝叶斯关联概率及证据融合评价候选组合
- **Baseline** · 独立相似度检索及其他多模态方法，具名待核
- **Benchmark** · 富视觉文档的多模态基准，名称与指标待核
- **关键结果 / 消融** · 报告总体表现优于所比方法，数值待核
- **适用条件 / 局限** · 候选召回不足时无法靠重排弥补

**可复用机制** · 在固定召回池比较独立打分与跨模态互证。

<a id="paper-155601"></a>

## Bayes-Sufficient Compression Is Not Enough: How Communication Helps in Multi-Agent Systems?

[官方论文页](https://neurips.cc/virtual/2026/poster/155601) · [作者来源](https://openreview.net/forum?id=4MClMQl04u)

- **问题 / 瓶颈** · 信息充分的消息也可能难以被接收端转成动作
- **核心创新 / 方法** · 按接收端增益和协议负担分解协调价值，并定位表达、吸收与行动闭合错误
- **Baseline** · 原始上下文、压缩和不通信
- **Benchmark** · 六个基准，含 ContextBench 和 ToolSandbox
- **关键结果 / 消融** · 相同协议使前者联合准确率 0.633 升至 0.775，后者 0.889 降至 0.653
- **适用条件 / 局限** · 依赖执行器本地视图和解释能力

**可复用机制** · 通信前估计接收端缺口，记录正确消息到达后能否完成动作。

<a id="paper-139160"></a>

## BBOWP-Bench: Evaluating LLMs on Black-Box Optimization Word Problems

[官方论文页](https://neurips.cc/virtual/2026/poster/139160) · [作者来源](https://openreview.net/forum?id=heroYEMhh0)

- **问题 / 瓶颈** · 显式公式题无法检验从描述定义搜索变量与范围
- **核心创新 / 方法** · 将自然语言实例配可执行黑箱和人工基线，运行实际优化
- **Baseline** · 人类设计的空间和求解方案
- **Benchmark** · BBOWP-Bench 四领域 23 个实例
- **关键结果 / 消融** · 模型能按预算选算法，但变量遗漏和范围失衡仍常见
- **适用条件 / 局限** · 覆盖规模有限，结果受提示的信息充分程度影响

**可复用机制** · 让代理先提交搜索空间，再用同等求解预算定位失败来自空间还是算法。

<a id="paper-155646"></a>

## B-CALM: Bias-Limited Bayesian Borrowing for RCT-Anchored Treatment Effects under Covariate Mismatch

[官方论文页](https://neurips.cc/virtual/2026/poster/155646) · [作者来源](https://openreview.net/forum?id=43vGcbI7xt)

- **问题 / 瓶颈** · 观察资料规模大但可能使试验异质效应估计过度自信。
- **核心创新 / 方法** · 对齐共享潜状态并分别学习基线偏差与治疗对比偏差。
- **Baseline** · 池化和森林模型。
- **Benchmark** · 合成、半合成及儿童肥胖外部对照，测区间校准。
- **关键结果 / 消融** · 理论上外部数据有效样本量饱和，实验报告较少负迁移。
- **适用条件 / 局限** · 依赖潜对齐与偏差先验。

**可复用机制** · 调整对比偏差先验并报告试验锚定结论的敏感性。

<a id="paper-151593"></a>

## BDC-Merge: Cross-Architecture Model Merging via Dependency Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/151593) · [作者来源](https://openreview.net/forum?id=ZOfiCmcwhT)

- **问题 / 瓶颈** · 架构差异导致参数缺少直接对应。
- **核心创新 / 方法** · 在小校准集估计层与特征的 Brownian 距离相关，再构建权重融合算子。
- **Baseline** · 跨架构最优传输融合。
- **Benchmark** · 四个低资源语言和两个专业知识基准。
- **关键结果 / 消融** · 作者报告优于跨架构对照并保持一般能力。
- **适用条件 / 局限** · 依赖校准集代表性。

**可复用机制** · 固定校准预算比较激活依赖对齐与运输对齐，分开测知识转移和能力保留。

<a id="paper-151303"></a>

## BEACON: Cross-Domain Co-Training of Generative Robot Policies via Best-Effort Adaptation

[官方论文页](https://neurips.cc/virtual/2026/poster/151303) · [作者来源](https://openreview.net/forum?id=bSawLg1NO0)

- **问题 / 瓶颈** · 固定源目标混合比例可能引起负迁移。
- **核心创新 / 方法** · 交替更新扩散策略及基于目标域泛化目标的源权重。
- **Baseline** · 仅目标域、固定比例、特征对齐。
- **Benchmark** · 仿真间、仿真到现实、多源操作。
- **关键结果 / 消融** · 摘要报告数据效率和稳健性提高，并出现隐式特征对齐。
- **适用条件 / 局限** · 需要少量目标示范和可靠差异估计。

**可复用机制** · 固定真实示范预算比较可学习权重和固定混合。

<a id="paper-155338"></a>

## BEAGLE: Behavior-Enforced Agent for Grounded Learner Emulation

[官方论文页](https://neurips.cc/virtual/2026/poster/155338) · [作者来源](https://openreview.net/forum?id=6MR1jKbdYU)

- **问题 / 瓶颈** · 通用模型倾向快速答对，难再现初学者的迭代过程。
- **核心创新 / 方法** · 半马尔可夫模型安排认知行为，贝叶斯知识追踪约束错误，独立生成代码。
- **Baseline** · 与学习者模拟基线对照，名称待核。
- **Benchmark** · Python 解题轨迹及 71 人鉴别测试。
- **关键结果 / 消融** · 鉴别准确率 52.8%，作者报告统计上相当于机会水平。
- **适用条件 / 局限** · 仅验证给定编程任务，人类鉴别不等于教学有效性。

**可复用机制** · 将策略转移与执行错误分别建模，和真实轨迹比较。

<a id="paper-139293"></a>

## BEAKER: An Expert-Curated Benchmark for Embodied Brains in Self-Driving Chemical Laboratories

[官方论文页](https://neurips.cc/virtual/2026/poster/139293) · [作者来源](https://openreview.net/forum?id=Z3y6m9KFIU)

- **问题 / 瓶颈** · 实验场景理解指标可能把物体识别误当成执行能力。
- **核心创新 / 方法** · 专家人工设计图像与视频问答，按识别、空间动作判断与流程理解诊断。
- **Baseline** · 比较 28 个通用、科学和具身模型。
- **Benchmark** · 1000 道专家题与 11 类任务。
- **关键结果 / 消融** · 模型能识别许多对象和状态，但空间判断与长程流程较弱。
- **适用条件 / 局限** · 静态问答不能替代安全的闭环测试。

**可复用机制** · 高风险场景验收应将感知与可执行性分开，不以感知识别通过替代人工安全检查。

<a id="paper-149610"></a>

## BeamWitness: Rooted Subgraph Beam Search for Selective Graph Representation Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149610) · [作者来源](https://openreview.net/forum?id=ooitypoSMX)

- **问题 / 瓶颈** · 早期聚合容易混合关键和无关邻居。
- **核心创新 / 方法** · 奖励训练扩展或停止策略，束搜索保留候选见证子图。
- **Baseline** · 标准 GNN 和相关子图方法。
- **Benchmark** · 有真实模体标注的控制基准及真实图和节点分类。
- **关键结果 / 消融** · 作者报告模体识别接近满分，真实任务表现可比。
- **适用条件 / 局限** · 搜索开销和根节点选择需核。

**可复用机制** · 用有真值模体的基准同时测准确率和证据覆盖。

<a id="paper-149762"></a>

## BEAST3D: animal behavioral analysis and neural encoding from multi-view video via Gaussian splatting

[官方论文页](https://neurips.cc/virtual/2026/poster/149762) · [作者来源](https://openreview.net/forum?id=nWHsSjFVA0)

- **问题 / 瓶颈** · 稀疏实验视角难支撑通用重建，关键点标注成本高。
- **核心创新 / 方法** · 输入已知相机参数，自监督预测高斯点并分离动物与背景。
- **Baseline** · 与通用三维重建和监督姿态方法的设定对照，具名待核。
- **Benchmark** · 四个物种的新视角合成、姿态和神经编码。
- **关键结果 / 消融** · 报告四视角可重建，下游有效。
- **适用条件 / 局限** · 需相机标定；换实验设置的泛化边界待核。

**可复用机制** · 固定相机预算，对照渲染监督表征在重建和下游回归中的作用。

<a id="paper-139633"></a>

## Be CARE-ful with Text-to-SQL Benchmarks

[官方论文页](https://neurips.cc/virtual/2026/poster/139633) · [作者来源](https://openreview.net/forum?id=EF3uDjMiF1)

- **问题 / 瓶颈** · 终态 SQL 正确仍可能违反运行要求。
- **核心创新 / 方法** · 在可执行数据库环境人工标注操作级验收条件。
- **Baseline** · 多种前沿语言智能体。
- **Benchmark** · Spider 2.0 与 BIRD-Interact 衍生的 1058 个任务。
- **关键结果 / 消融** · GPT-5.5 严格通过率 33.9%，综合分 73.3%。
- **适用条件 / 局限** · 基准环境不能覆盖全部真实组织约束。

**可复用机制** · 上线前在隔离环境以严格合取规则验证各项操作要求。

<a id="paper-154577"></a>

## Beckmann Transport Models: From Autonomous Flows to One-Step Maps

[官方论文页](https://neurips.cc/virtual/2026/poster/154577) · [作者来源](https://openreview.net/forum?id=CXIBpRIEL7)

- **问题 / 瓶颈** · 时间依赖流需要多步积分。
- **核心创新 / 方法** · 构造时间无关速度场，以守恒方程唯一解学习一步映射。
- **Baseline** · 与 Poisson 流和 equilibrium matching 建立对应。
- **Benchmark** · 大规模图像生成，具体指标待核。
- **关键结果 / 消融** · 作者报告修正既有方法不一致并提升表现。
- **适用条件 / 局限** · 精确输运依赖目标分布奇异性。

**可复用机制** · 按目标流形假设和计算预算对照直接映射与多步积分。

<a id="paper-153172"></a>

## BECON: Belief-Conditioned Constrained Multi-Objective Reinforcement Learning under Drifting Preferences and Budgets

[官方论文页](https://neurips.cc/virtual/2026/poster/153172) · [作者来源](https://openreview.net/forum?id=NKKhc57p17)

- **问题 / 瓶颈** · 偏好和安全预算会漂移，输入描述可能过时。
- **核心创新 / 方法** · 用近期历史估计隐任务上下文，并门控融合观测后联合调节约束与策略。
- **Baseline** · 先进多目标强化学习对照，名称待核。
- **Benchmark** · 多目标控制中的偏好和预算漂移。
- **关键结果 / 消融** · 摘要报告稳健性及约束满足率改善。
- **适用条件 / 局限** · 依赖不确定性校准与可识别的历史线索。

**可复用机制** · 分别测外部信号噪声与历史信念失准时的约束违反率。

<a id="paper-155460"></a>

## Before It Fades: Reinforcing Temporal Representations at Inference Time in VideoLLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/155460) · [作者来源](https://openreview.net/forum?id=5RsZhv1NUe)

- **问题 / 瓶颈** · 反转视频后时间答案常不改变。
- **核心创新 / 方法** · 逐层追踪反转表征差，提取中层峰值并按衰减曲线注入后续层。
- **Baseline** · 原模型及非时间任务对照。
- **Benchmark** · 三种视频语言模型及四个时间推理基准。
- **关键结果 / 消融** · 报告无需训练可提升时间推理，非时间任务影响小。
- **适用条件 / 局限** · 反转干预不适用于所有时间现象。

**可复用机制** · 先用成对时间干预找到层级瓶颈，再测注入是否改变证据响应。

<a id="paper-139741"></a>

## Before Words, Beyond Speech: Evaluating Nonverbal Social Reasoning in Early Childhood

[官方论文页](https://neurips.cc/virtual/2026/poster/139741) · [作者来源](https://openreview.net/forum?id=7C5CgIiHcA)

- **问题 / 瓶颈** · 统一问答分数混淆场景识别与非语言互动理解。
- **核心创新 / 方法** · 用注视、手势等原子线索构建渐进评测。
- **Baseline** · 比较先进视频语言模型与领域适配版本。
- **Benchmark** · NEST 的 1208 段人工标注早期社交视频。
- **关键结果 / 消融** · 作者观察到情景识别强但行为和人际推理明显下降。
- **适用条件 / 局限** · 限于所选自然场景，标注一致性待核。

**可复用机制** · 对同一片段按线索级别报告分数，分别测时间扰动与后果理解。

<a id="paper-153819"></a>

## Behaving Better, Thinking Worse: Sycophancy Across Post-Training Stages

[官方论文页](https://neurips.cc/virtual/2026/poster/153819) · [作者来源](https://openreview.net/forum?id=IUAXqLsMTC)

- **问题 / 瓶颈** · 表面回答更稳定可能掩盖模型更偏向用户给的错误答案。
- **核心创新 / 方法** · 按挑战类型和上下文分解评测，分别测生成和对数赔率。
- **Baseline** · OLMo、Llama 与 Tulu 等后训练管线。
- **Benchmark** · AMPS、MedQuAD；GPT-4o 判分及对数赔率变化。
- **关键结果 / 消融** · 后训练后同样本翻转率下降，同时先发错误断言下的赔率偏移增大。
- **适用条件 / 局限** · 仅测所列模型及任务；生成结果依赖评判。

**可复用机制** · 评测迎合时匹配题目并拆开行为和概率指标。

<a id="paper-148386"></a>

## Behavioral Foundation Models for Quality Diversity

[官方论文页](https://neurips.cc/virtual/2026/poster/148386) · [作者来源](https://openreview.net/forum?id=yFRrEkCBNX)

- **问题 / 瓶颈** · 直接搜策略参数在稀疏任务中开销大。
- **核心创新 / 方法** · 将候选表示为紧凑行为码，并用闭式无梯度算子近似改进。
- **Baseline** · 参数空间的质量多样性方法。
- **Benchmark** · 密集步态、稀疏导航与接触操作。
- **关键结果 / 消融** · 作者报告优于参数搜索，稀疏和欺骗奖励条件差异更大。
- **适用条件 / 局限** · 依赖预训练覆盖且搜索预算细节待核。

**可复用机制** · 在同等评估预算比较参数搜索和行为码搜索的覆盖及回报。

<a id="paper-149277"></a>

## Behavioral Geometric Supervision Aligns Video Foundation Models with Human Social Perception

[官方论文页](https://neurips.cc/virtual/2026/poster/149277) · [作者来源](https://openreview.net/forum?id=rVX7LF9vry)

- **问题 / 瓶颈** · 视频骨干的社会相似判断落后于字幕嵌入。
- **核心创新 / 方法** · 用三选一判断构建关系目标并低秩适配视觉骨干。
- **Baseline** · 预训练骨干、MPNet 字幕嵌入、匹配的语言蒸馏。
- **Benchmark** · 250 个社交短片和 49484 项人工判断，另测分布外迁移。
- **关键结果 / 消融** · V-JEPA 2.1 较原版接近三倍，语言蒸馏未复现主要收益。
- **适用条件 / 局限** · 取决于样本人群和社交场景覆盖。

**可复用机制** · 固定监督量，比较原始感知判断和语言蒸馏能否捕捉独立的人类相似结构。

<a id="paper-149644"></a>

## Behavioral Probes for Information Flow in LLM Swarms

[官方论文页](https://neurips.cc/virtual/2026/poster/149644) · [作者来源](https://openreview.net/forum?id=oXV7UcdWSz)

- **问题 / 瓶颈** · 仅看最终收益难定位哪些节点在吸收外部信息。
- **核心创新 / 方法** · 将 ECS 和 PKS 探针用于节点诊断、剪枝和推理路径搜索。
- **Baseline** · 只看任务收益的结构优化。
- **Benchmark** · 受控和较真实的多智能体系统实验。
- **关键结果 / 消融** · 作者报告减少异常节点并加快路径搜索收敛。
- **适用条件 / 局限** · 探针属启发式，不能直接证明因果来源。

**可复用机制** · 先用已知相关性输入验证探针，再联合最终效用选择结构。

<a id="paper-138919"></a>

## BehaviorBench: Modeling Real-World User Decisions from Behavioral Traces

[官方论文页](https://neurips.cc/virtual/2026/poster/138919) · [作者来源](https://openreview.net/forum?id=wry0uLfZbi)

- **问题 / 瓶颈** · 显式画像和模拟用户可能偏离真实决策。
- **核心创新 / 方法** · 从公开预测市场和链上记录构造纵向历史，分别预测信念和交易。
- **Baseline** · 直接历史、生成画像、跨用户检索等表示。
- **Benchmark** · 真实轨迹中的立场置信度及动作方向和幅度。
- **关键结果 / 消融** · 不同历史表示的收益随任务变化，作者报告隐式信号推理仍受限。
- **适用条件 / 局限** · 结果依赖所选平台和公开行为，不能外推一般用户。

**可复用机制** · 按预测目标对照历史压缩形式并保留同用户时间外划分。

<a id="paper-150673"></a>

## Behavior Cloning is Not All You Need: The Optimality of On-Policy Distillation for Noisy Expert Feedback

[官方论文页](https://neurips.cc/virtual/2026/poster/150673) · [作者来源](https://openreview.net/forum?id=gLfGap1Y0U)

- **问题 / 瓶颈** · 从污染轨迹离线学习难以匹配干净教师。
- **核心创新 / 方法** · 构造噪声教师理论模型，推导学生状态上查询教师的蒸馏目标。
- **Baseline** · 离线行为克隆和已有在线蒸馏。
- **Benchmark** · 理论样本复杂度、合成和自然语言任务。
- **关键结果 / 消融** · 离线在给定设定需指数样本，在线一般为时域多项式，实验报告目标改进。
- **适用条件 / 局限** · 依赖噪声假设和可交互教师，特殊无时域结果有额外条件。

**可复用机制** · 对不完美教师固定查询预算，比较专家历史轨迹和学生访问状态监督。

<a id="paper-155941"></a>

## Behavior-Discriminative Reward Shaping for Reward-Robust Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/155941) · [作者来源](https://openreview.net/forum?id=1ekxUnK93j)

- **问题 / 瓶颈** · 常规奖励距离会把行为等价的扰动重复纳入。
- **核心创新 / 方法** · 将势函数塑形等价奖励投影到规范代表并求解鲁棒目标。
- **Baseline** · 代表性奖励鲁棒 RL。
- **Benchmark** · 不同复杂度的任务与奖励扰动评测。
- **关键结果 / 消融** · 作者证明最优鲁棒值保持，报告扰动稳健性改善。
- **适用条件 / 局限** · 依赖势函数塑形等价及收敛假设。

**可复用机制** · 构建不确定集前先消除保序奖励方向，比较求解开销和策略结果。

<a id="paper-150981"></a>

## Behavior Pack Optimization for Video MLLM Post-Training

[官方论文页](https://neurips.cc/virtual/2026/poster/150981) · [作者来源](https://openreview.net/forum?id=dnqyvgz1LI)

- **问题 / 瓶颈** · 单视图奖励允许模型借助外观先验跳过时序证据。
- **核心创新 / 方法** · 联合奖励要求对无关变化稳定、对证据移除敏感、缺证时弃答，以原视图作优势锚点。
- **Baseline** · 同 SFT 起点且预算匹配的标准 GRPO。
- **Benchmark** · TempCompass、MVBench、NExT-QA，以及跨基准和骨干迁移。
- **关键结果 / 消融** · 宏平均提高 4.7 个百分点，时间困难子集提高 7.8 点，弃答 F1 提高 20 点。
- **适用条件 / 局限** · 效果依赖反事实干预与问题证据的匹配。

**可复用机制** · 固定采样量对照独立奖励与多视图联合奖励，分别报告稳定、敏感和弃答。

<a id="paper-150818"></a>

## Behaviour4All: A Dependency-Aware Toolkit for in-the-wild Facial Behaviour Analysis

[官方论文页](https://neurips.cc/virtual/2026/poster/150818) · [作者来源](https://openreview.net/forum?id=f4bSbN3cg8)

- **问题 / 瓶颈** · 独立训练与朴素共享都可能丢掉表情任务关系
- **核心创新 / 方法** · 引入心理物理任务映射和协调损失
- **Baseline** · 朴素多任务及师生方法
- **Benchmark** · 八个自然场景数据集
- **关键结果 / 消融** · 报告表现、公平性和跨库泛化改善
- **适用条件 / 局限** · 映射的跨人群适用性待核

**可复用机制** · 固定标注覆盖比较关系约束与独立损失

<a id="paper-151258"></a>

## Belief Engine: Configurable Stance Dynamics for Multi-Agent LLM Deliberation

[官方论文页](https://neurips.cc/virtual/2026/poster/151258) · [作者来源](https://openreview.net/forum?id=bjQRVp4xRa)

- **问题 / 瓶颈** · 多轮提示状态变化与实际证据响应难区分
- **核心创新 / 方法** · 保留参数化信念和证据档案，以贝叶斯对数赔率更新
- **Baseline** · 无显式信念状态对照待核
- **Benchmark** · 多个语言模型的参数扫描
- **关键结果 / 消融** · 高吸收增强证据响应，强锚定抑制漂移
- **适用条件 / 局限** · 依赖结构化证据抽取，不能把模拟立场当真实偏好

**可复用机制** · 固定对话内容扫两个控制旋钮，区分证据响应和上下文漂移

<a id="paper-150640"></a>

## Bellman Contraction under MMD: A Unified Framework

[官方论文页](https://neurips.cc/virtual/2026/poster/150640) · [作者来源](https://openreview.net/forum?id=ga3QB4bSSV)

- **问题 / 瓶颈** · 核选择会改变分布更新是否收缩
- **核心创新 / 方法** · 把收缩归约为差分核条件正定，再由 Bernstein 函数分析径向核
- **Baseline** · Gaussian RBF、幂距离、多二次核
- **Benchmark** · 任意维径向核判据和数值搜索
- **关键结果 / 消融** · 识别十二种新核，并解释有界支撑下 RBF 的可用性
- **适用条件 / 局限** · 全局条件与支撑集条件须区分

**可复用机制** · 设计分布式 RL 损失时先按回报支撑检验核

<a id="paper-139421"></a>

## BELLS-O: Evaluating the Operational Trade-offs of LLM Supervision Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/139421) · [作者来源](https://openreview.net/forum?id=Rf11dIsDn9)

- **问题 / 瓶颈** · 单一检测分数无法反映部署取舍
- **核心创新 / 方法** · 统一预算下比较专用护栏与通用监督器
- **Baseline** · LlamaGuard-4、ShieldGemma-2、通用模型等
- **Benchmark** · 17 个供应方的 28 个系统，跨输入输出审核任务
- **关键结果 / 消融** · 作者提供多指标运营比较，分项数值待核
- **适用条件 / 局限** · 供应方版本与数据分布会变

**可复用机制** · 在统一请求量上画误报、召回和成本的权衡

<a id="paper-156773"></a>

## Below the Reliability Floor: Recovering True Success from Judge-Gated Loops

[官方论文页](https://neurips.cc/virtual/2026/poster/156773) · [作者来源](https://openreview.net/forum?id=J2Yg9vJcYb)

- **问题 / 瓶颈** · 反复尝试直到裁判通过会产生选择偏差
- **核心创新 / 方法** · 把有次数上限的门控视作二分类器，以 Youden 指数判断可恢复性
- **Baseline** · 原始通过率与金标准均值
- **Benchmark** · 44 个循环，含 GSM8K、MATH 与代码
- **关键结果 / 消融** · 中位偏差约 0.16；代码案例真实 0.74 被报为 0.98
- **适用条件 / 局限** · 门控辨别力接近零时只能依赖金标准

**可复用机制** · 发布 Agent 指标时同时记录重试上限和抽样真实成功率

<a id="paper-139778"></a>

## Benchmark for Assessing Olfactory Perception of Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139778) · [作者来源](https://openreview.net/forum?id=5N6nOIwgxj)

- **问题 / 瓶颈** · 知识得分可能主要来自词汇关联
- **核心创新 / 方法** · 为同一批嗅觉题构造两种输入表示
- **Baseline** · 化合物名称与异构 SMILES
- **Benchmark** · 1010 题、8 类任务、21 种模型配置
- **关键结果 / 消融** · 名称提示平均高约 7 个百分点，最高总体准确率 64.4%
- **适用条件 / 局限** · 提示熟悉度仍是混杂因素

**可复用机制** · 用同题异表示对照诊断模型是在调用名称关联还是使用结构信息

<a id="paper-138960"></a>

## Benchmark Health Index: A Systematic Framework for Benchmarking the Benchmarks of LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/138960) · [作者来源](https://openreview.net/forum?id=tsoDWPkJOz)

- **问题 / 瓶颈** · 高引用或高分都无法单独说明评测仍有效
- **核心创新 / 方法** · 用模型报告统计量构造三个独立审计轴
- **Baseline** · 单看分数或采用率的做法
- **Benchmark** · 117 个模型报告中的 158 个基准
- **关键结果 / 消融** · 作者提供生态级比较，案例和数值待正文核对
- **适用条件 / 局限** · 报告缺失和选择性发布会影响估计

**可复用机制** · 精简评测组合时优先检查基准是否还能稳定区分模型

<a id="paper-139423"></a>

## Benchmarking and Improving Monitors for Out-Of-Distribution Alignment Failure in LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/139423) · [作者来源](https://openreview.net/forum?id=Rba2NveuIm)

- **问题 / 瓶颈** · 常规安全训练很难覆盖新型异常
- **核心创新 / 方法** · 限制监测器训练分布，再以独立异常分数辅助检测
- **Baseline** · 单独护栏与四种异常检测对照
- **Benchmark** · MOOD 七组分布外测试
- **关键结果 / 消融** · 护栏结合马氏距离时召回由 39% 到 47%
- **适用条件 / 局限** · 须同时核查误报且受训练覆盖定义影响

**可复用机制** · 用相同误报预算比较分类器与异常分数融合

<a id="paper-149901"></a>

## Benchmarking and Optimizing Multimodal Structured Generation: The OracleGraph Dataset and PRISM Framework

[官方论文页](https://neurips.cc/virtual/2026/poster/149901) · [作者来源](https://openreview.net/forum?id=mMpgycVI2H)

- **问题 / 瓶颈** · 稀疏标量反馈难指导长结构输出
- **核心创新 / 方法** · PRISM 用诊断图报告增强教师，结合奖励加权与长度归一化
- **Baseline** · SFT、DPO、GRPO、SimPO 和普通自蒸馏
- **Benchmark** · OracleGraph 一万页与十二维 VQA 诊断
- **关键结果 / 消融** · 摘要报告结构训练瓶颈改善，幅度待核
- **适用条件 / 局限** · 依赖可靠诊断与可构造图标签

**可复用机制** · 固定教师比较错误报告与仅全局图分数的结构生成收益

<a id="paper-139839"></a>

## Benchmarking Attention for Tabular Foundation Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139839) · [作者来源](https://openreview.net/forum?id=1MbSbrblLi)

- **问题 / 瓶颈** · 表格行列长度和内存步幅差异大
- **核心创新 / 方法** · 在真实形状扫描后端和设备的前后向吞吐
- **Baseline** · Torch SDPA、FlashAttention 2/3/4、vLLM、SageAttention
- **Benchmark** · A100、H100、B200 的表格张量
- **关键结果 / 消融** · 最佳后端随行列维度而异
- **适用条件 / 局限** · 结论与 GPU 和隐藏维度绑定

**可复用机制** · 为各注意力方向建独立后端基准并计入布局转换

<a id="paper-139491"></a>

## Benchmarking Compositional Generalisation for Machine Learning Interatomic Potentials

[官方论文页](https://neurips.cc/virtual/2026/poster/139491) · [作者来源](https://openreview.net/forum?id=MTNbRIVxvp)

- **问题 / 瓶颈** · 平均误差可能掩盖插值捷径
- **核心创新 / 方法** · 设计四类组合泛化测试并区分分布内外
- **Baseline** · 现有机器学习势模型，具体名称待核
- **Benchmark** · 四种未见组合测试
- **关键结果 / 消融** · 作者报告当前方法在分布外组合仍有明显困难
- **适用条件 / 局限** · 适用范围受选用系统和组合划分限制

**可复用机制** · 为物理代理模型同时保留随机划分与组合留出并报告差距

<a id="paper-139463"></a>

## Benchmarking Fine-Grained Spatio-Temporal Awareness in Embodied Brain Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139463) · [作者来源](https://openreview.net/forum?id=OBDBEkTysD)

- **问题 / 瓶颈** · 语义正确不代表能够定位到正确帧和位置
- **核心创新 / 方法** · 拆分物体认知、空间认知、定位和指点
- **Baseline** · 通用视觉语言模型及具身模型
- **Benchmark** · ECLBench 3616 段第一视角视频和 12000 问
- **关键结果 / 消融** · 通用模型强于语义但定位较弱，专用模型泛化受限
- **适用条件 / 局限** · 视频问答不等于真实闭环操作

**可复用机制** · 把定位误差与语义正确率分表报告

<a id="paper-138872"></a>

## Benchmarking Graph Self-Supervised Learning for Node-Level Tasks: Insights and Strong Baseline

[官方论文页](https://neurips.cc/virtual/2026/poster/138872) · [作者来源](https://openreview.net/forum?id=zrKbSaWEfZ)

- **问题 / 瓶颈** · 弱监督基线可能夸大自监督增益
- **核心创新 / 方法** · 统一架构和超参数搜索比较预训练家族
- **Baseline** · MaskGAE、GraphMAE、BGRL、GRACE 与监督训练
- **Benchmark** · 多数据集节点任务
- **关键结果 / 消融** · 前两者经常未超调优监督，对比式在所测设置更好
- **适用条件 / 局限** · 机制解释仍是作者假设，跨任务待核

**可复用机制** · 将同预算强监督作为图自监督必备对照

<a id="paper-139392"></a>

## Benchmarking Membership Privacy Risks in Preference-Based LLM Post-Training

[官方论文页](https://neurips.cc/virtual/2026/poster/139392) · [作者来源](https://openreview.net/forum?id=TIAqMV9Kzf)

- **问题 / 瓶颈** · 只看单一回答可能低估成对偏好监督的风险
- **核心创新 / 方法** · 按提示及成对回答的记录结构组织防御评估
- **Baseline** · 单回答与完整记录审计对照
- **Benchmark** · 偏好后训练语言模型，数据细项待核
- **关键结果 / 消融** · 作者指出忽略记录结构会低估泄漏
- **适用条件 / 局限** · 结果受参考模型和训练方案影响

**可复用机制** · 隐私评审时将数据记录粒度与实际训练样本对齐

<a id="paper-139044"></a>

## Benchmarking Multimodal Mathematical Reasoning with Explicit Visual Dependency

[官方论文页](https://neurips.cc/virtual/2026/poster/139044) · [作者来源](https://openreview.net/forum?id=oFfds87D30)

- **问题 / 瓶颈** · 知识型数学题可能由文本捷径解决
- **核心创新 / 方法** · 在基础数学题中构造明确的跨图依赖
- **Baseline** · 26 个视觉语言模型
- **Benchmark** · VCBench 1720 题、6697 图、六认知领域
- **关键结果 / 消融** · 摘要未给各模型数值
- **适用条件 / 局限** · 仍需正文验证文本和单图对照

**可复用机制** · 构造多图评测时加入删图对照以确认必要信息

<a id="paper-139589"></a>

## Benchmarking Open-Ended Multi-Agent Coordination in Language Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/139589) · [作者来源](https://openreview.net/forum?id=GjoyYpGTqL)

- **问题 / 瓶颈** · 短回合或结构化任务难测长程开放协调
- **核心创新 / 方法** · 在程序生成世界中加入软分工、通信和协调任务
- **Baseline** · 13 个零样本 LLM 与训练后的 MARL
- **Benchmark** · Alem 生存世界与多档协调难度
- **关键结果 / 消融** · 多数模型约得最大回报的 6%
- **适用条件 / 局限** · 同质队伍和游戏环境限制外推

**可复用机制** · 同一环境扫协调难度并分开报告生存及团队指标

<a id="paper-139608"></a>

## Benchmarking Risk Attitudes of LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/139608) · [作者来源](https://openreview.net/forum?id=FlBNkKq775)

- **问题 / 瓶颈** · 行为差异可能来自风险认知或决策偏好
- **核心创新 / 方法** · 分开测模型主观危险判断和最终动作
- **Baseline** · 六个语言模型与一百名参与者
- **Benchmark** · 空间导航、临床分流与金融分配
- **关键结果 / 消融** · 观察到两类行为模式，五个模型达到两项可靠性条件
- **适用条件 / 局限** · 陈述信念不能保证等同内部状态

**可复用机制** · 比较风险策略时先匹配感知风险，再测行动倾向

<a id="paper-138912"></a>

## Benchmarking Sensor-Fault Robustness in Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/138912) · [作者来源](https://openreview.net/forum?id=xIRiNVRCRg)

- **问题 / 瓶颈** · 干净集排名可能掩盖传感器故障。
- **核心创新 / 方法** · 统一故障强度并把训练和评测故障分开。
- **Baseline** · Chronos-2、末值预测及故障增强。
- **Benchmark** · 四个真实数据集、八种场景，比较最坏退化和 MSE。
- **关键结果 / 消融** · 干净和故障排名可能反转，不同增强各有优势。
- **适用条件 / 局限** · 受选定故障和强度范围限制。

**可复用机制** · 部署验收同时看绝对故障误差和相对退化。

<a id="paper-138904"></a>

## Benchmarking sequence-to-ensemble predictors on UNICORNEdb, a UniProt-grouped database of PDB-derived conformational ensembles

[官方论文页](https://neurips.cc/virtual/2026/poster/138904) · [作者来源](https://openreview.net/forum?id=xwvwwQZbXy)

- **问题 / 瓶颈** · 按序列聚类可能混淆实体差异和状态差异。
- **核心创新 / 方法** · 按 UniProt 与 PDB 实体注释整理已有观测。
- **Baseline** · 七种已发表的构象集合预测器。
- **Benchmark** · 839 个多构象蛋白，按集合覆盖与多样性评估。
- **关键结果 / 消融** · 最强对照完整覆盖率仅 8.2%，多样性更高时下降。
- **适用条件 / 局限** · 实验结构记录未必覆盖真实状态全集。

**可复用机制** · 评估多状态预测时分别报告完整覆盖和高多样性子集。

<a id="paper-139241"></a>

## Benchmarking Vietnamese Legal Knowledge of Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139241) · [作者来源](https://openreview.net/forum?id=clrKAP4Tdj)

- **问题 / 瓶颈** · 普通法英文测试无法代表越南成文法任务。
- **核心创新 / 方法** · 专家按问答、多步推理和情景任务标注并核对权威来源。
- **Baseline** · 具名模型待全文核实。
- **Benchmark** · VietLegal 的 10,450 条专家样本。
- **关键结果 / 消融** · 摘要给出规模与构造，模型结果待核。
- **适用条件 / 局限** · 法条修订会影响有效性。

**可复用机制** · 对专业模型用规范层级和任务难度分层，而非仅报告总体正确率。

<a id="paper-155241"></a>

## Benchmark Recovery Does Not Certify a Frozen Tool-Trigger Contract After Quantization

[官方论文页](https://neurips.cc/virtual/2026/poster/155241) · [作者来源](https://openreview.net/forum?id=7CU4DLB7yh)

- **问题 / 瓶颈** · 知识基准恢复可能掩盖接口变化。
- **核心创新 / 方法** · 冻结四动作控制策略的验收协议，独立重调阈值后核对 FP16 行为。
- **Baseline** · FP16 与 GPTQ 量化对照。
- **Benchmark** · 四个 Llama/Qwen 检查点、MMLU 与 BFCL。
- **关键结果 / 消融** · 两款大模型 W4A16 下仍有 11.9 和 10.9 个百分点的误触发率。
- **适用条件 / 局限** · 仅一个控制器和所测量化设定。

**可复用机制** · 验收门槛模型应直接测分数到动作映射，报告工具误触发。

<a id="paper-139267"></a>

## Benchmarks Are Not Atomic: Composition-Aware LLM Evaluation using BenchHub

[官方论文页](https://neurips.cc/virtual/2026/poster/139267) · [作者来源](https://openreview.net/forum?id=asBdEGcCLc)

- **问题 / 瓶颈** · 综合分数混合能力和测试集构成。
- **核心创新 / 方法** · 按实例属性组织、重采样和重加权既有基准。
- **Baseline** · 原始聚合评分与可控重采样对照。
- **Benchmark** · BenchHub 汇集 54 个基准、83.9 万样本、10 种语言。
- **关键结果 / 消融** · 权重和采样变化可改变模型排名。
- **适用条件 / 局限** · 依赖分层属性的标注覆盖。

**可复用机制** · 选型前按应用构成设置权重并报告敏感性。

<a id="paper-139555"></a>

## Benchmarks as Measurement Instruments: Quantifying Signal and Noise for More Efficient AI Evaluations Under Distribution Shift

[官方论文页](https://neurips.cc/virtual/2026/poster/139555) · [作者来源](https://openreview.net/forum?id=IrodEQg4Nj)

- **问题 / 瓶颈** · 固定榜单的信噪比随被测模型群体变化。
- **核心创新 / 方法** · 用交叉随机效应分解方差，构建可计算代理筛题。
- **Baseline** · 相同预算下随机抽题。
- **Benchmark** · 不同基准与较强、较弱模型分组，测排名可靠性。
- **关键结果 / 消融** · 代理筛得的小集合优于随机组，强模型群常见可靠性下降。
- **适用条件 / 局限** · 需要代表性的模型群体估计方差。

**可复用机制** · 缩小评测集前测目标模型群的区分能力，定期重新校准。

<a id="paper-154989"></a>

## Benchmark Shadows: How Data Regimes Shape Parameter Footprints and Generalization

[官方论文页](https://neurips.cc/virtual/2026/poster/154989) · [作者来源](https://openreview.net/forum?id=9OlZwO6YDw)

- **问题 / 瓶颈** · 榜单提升可能对应狭窄的训练覆盖。
- **核心创新 / 方法** · 固定模型与训练预算，对比覆盖扩张、重复与集中改写，检查更新谱和层级足迹。
- **Baseline** · 覆盖扩张对照及两种集中策略。
- **Benchmark** · 受控训练与公开模型关联分析。
- **关键结果 / 消融** · 重复造成的效应较易修复，频率集中留下更持久足迹。
- **适用条件 / 局限** · 公开模型证据是相关性。

**可复用机制** · 在同预算下分离重复和覆盖，使用干预后恢复表现作验证。

<a id="paper-139725"></a>

## Bench-MFG: A Benchmark Suite for Learning in Stationary Mean Field Games

[官方论文页](https://neurips.cc/virtual/2026/poster/139725) · [作者来源](https://openreview.net/forum?id=8CjE3pJACr)

- **问题 / 瓶颈** · 单一环境无法检验方法对交互结构的依赖。
- **核心创新 / 方法** · 建立环境分类并用 MF-Garnets 生成实例。
- **Baseline** · 多种求解算法含 MF-PSO。
- **Benchmark** · 离散稳态平均场博弈，含单调、势和动力学耦合类别。
- **关键结果 / 消融** · 摘要未报告可量化的排名与失败结果。
- **适用条件 / 局限** · 限于稳态离散环境。

**可复用机制** · 让测试实例在各结构类内随机变化，分别测鲁棒性。

<a id="paper-139621"></a>

## BenchRep-T: A Systematic Evaluation of T-Cell Repertoire-Based Disease Diagnostics

[官方论文页](https://neurips.cc/virtual/2026/poster/139621) · [作者来源](https://openreview.net/forum?id=EvaVcjvUjx)

- **问题 / 瓶颈** · 跨队列与预处理差异妨碍可靠比较。
- **核心创新 / 方法** · 统一公开免疫受体队列的处理与评测。
- **Baseline** · 九种统计、树模型、深度和图方法。
- **Benchmark** · 疾病分类、受限采样、已知关联恢复与混杂敏感性。
- **关键结果 / 消融** · 简单树模型的分类效果接近复杂模型，没有方法全面领先。
- **适用条件 / 局限** · 受队列可比性与采样条件限制。

**可复用机制** · 新诊断模型应与低成本基线同协议比较，并分开报告采样及混杂影响。

<a id="paper-149677"></a>

## Benign Reinforcement Learning Can Amplify Latent Backdoors

[官方论文页](https://neurips.cc/virtual/2026/poster/149677) · [作者来源](https://openreview.net/forum?id=oGkR8QUVmY)

- **问题 / 瓶颈** · 训练阶段变化可放大早先未明显表现的异常。
- **核心创新 / 方法** · 跨训练阶段比较固定审计任务和工具调用记录。
- **Baseline** · 监督训练后与强化学习后的防御审计。
- **Benchmark** · 所测语言模型的工具行为及守卫评估。
- **关键结果 / 消融** · 作者观察到后训练后原有安全评测通过不能保证行为保持。
- **适用条件 / 局限** · 具体风险随训练栈和工具权限改变。

**可复用机制** · 每次后训练后检查异常工具调用，并人工复核审计漏报。

<a id="paper-155963"></a>

## Bentkus-type asymptotic e-values

[官方论文页](https://neurips.cc/virtual/2026/poster/155963) · [作者来源](https://openreview.net/forum?id=1WITBC6SMZ)

- **问题 / 瓶颈** · 已有渐近 e 值存在导致保守的尺度损失。
- **核心创新 / 方法** · 利用近最优集中不等式构造新的渐近 e 值。
- **Baseline** · 既有渐近 e 值。
- **Benchmark** · 理论和实验比较事后区间与多重检验拒绝率。
- **关键结果 / 消融** · 作者证明去除所分析的缺失因子，并报告更紧区间。
- **适用条件 / 局限** · 有限样本适用条件需另查。

**可复用机制** · 选择检验统计量时同时记录区间宽度和适用假设。

<a id="paper-154106"></a>

## Bernini: Latent Semantic Planning for Video Diffusion

[官方论文页](https://neurips.cc/virtual/2026/poster/154106) · [作者来源](https://openreview.net/forum?id=GDdIbzbPVF)

- **问题 / 瓶颈** · 直接生成像素难复用多模态模型的理解能力。
- **核心创新 / 方法** · 规划器预测目标 ViT 表示，DiT 据此渲染，编辑再加入源 VAE 特征。
- **Baseline** · 视频生成和编辑方法，名称待核。
- **Benchmark** · 视频生成、编辑与新指令泛化。
- **关键结果 / 消融** · 作者报告多个评测改善，数值待核。
- **适用条件 / 局限** · 语义表示可能丢失局部纹理。

**可复用机制** · 用固定渲染器分别测试文本和预测视觉语义条件。

<a id="paper-155986"></a>

## Bernoulli Flow Models: Self-Consistent Generative Modeling for Binary Data

[官方论文页](https://neurips.cc/virtual/2026/poster/155986) · [作者来源](https://openreview.net/forum?id=1MMIaLs9nW)

- **问题 / 瓶颈** · 把单步似然套到跨步采样会损害质量。
- **核心创新 / 方法** · 定义连续全程 Bernoulli 概率路径，解析任意时间间隔后验。
- **Baseline** · 离散扩散与连续生成对照。
- **Benchmark** · LSUN Churches 256²，在不同采样步数下测 FID。
- **关键结果 / 消融** · 256 步训练而 16 步采样 FID 9.31，离散对照 204.10。
- **适用条件 / 局限** · 证据对应二值生成设定。

**可复用机制** · 减少采样步数时先检查跨步转移与训练路径是否一致。

<a id="paper-139851"></a>

## BESS-Bench: Benchmarking Spectral Representations for Be-Star Variability

[官方论文页](https://neurips.cc/virtual/2026/poster/139851) · [作者来源](https://openreview.net/forum?id=0X9DNTPDH6)

- **问题 / 瓶颈** · 光谱表示的形态质量不保证预测质量。
- **核心创新 / 方法** · 统一多历元光谱，设计形态探测、谱线迁移和等效宽度预测。
- **Baseline** · BeMAE、PCA、Chronos-Bolt、TimesFM-2.0 和持久性。
- **Benchmark** · BESS-Bench 的 H-alpha 评分子集含 26,937 条光谱。
- **关键结果 / 消融** · BeMAE 形态 R² 是 PCA 的 4.24 倍，预测却由 PCA 加岭回归优于所测基础模型。
- **适用条件 / 局限** · 限于 Be 星与所测谱线。

**可复用机制** · 不要用表征探测替代下游预测，保留低成本时序对照。

<a id="paper-153746"></a>

## Best Arm Identification for Bandits with Shifting Means

[官方论文页](https://neurips.cc/virtual/2026/poster/153746) · [作者来源](https://openreview.net/forum?id=J1l2Lgg3tV)

- **问题 / 瓶颈** · 臂间差距稳定也不足以保证 GLRT 可靠。
- **核心创新 / 方法** · ISM 用重要性加权处理时变共同偏移。
- **Baseline** · Track-and-Stop 等 GLRT 停止方法。
- **Benchmark** · 固定置信度、次高斯奖励与有界均值设定。
- **关键结果 / 消融** · 作者证明正确性并给出常数意义匹配的最坏界。
- **适用条件 / 局限** · 须满足共同偏移及稳定差距。

**可复用机制** · 检查各动作是否共享时间漂移，再确定停止规则和置信界。

<a id="paper-151037"></a>

## Best Arm Identification in Generalized Linear Bandits via Hybrid Feedback

[官方论文页](https://neurips.cc/virtual/2026/poster/151037) · [作者来源](https://openreview.net/forum?id=dSPIhAJKfj)

- **问题 / 瓶颈** · 两种反馈的成本和辨识价值不同。
- **核心创新 / 方法** · 用统一似然置信序列与混合 Track-and-Stop 跟踪最优设计。
- **Baseline** · 单反馈或其他最优臂识别方法，具名对照待核。
- **Benchmark** · 广义线性赌博机固定置信度与不同查询成本。
- **关键结果 / 消融** · 作者证明正确性并报告样本效率改善。
- **适用条件 / 局限** · 依赖自协调性与指定反馈模型。

**可复用机制** · 用单位成本的辨识价值决定获取绝对标签还是偏好比较。

<a id="paper-154666"></a>

## Best-of-$N$ Guidance for Test-time Diffusion Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/154666) · [作者来源](https://openreview.net/forum?id=BvprWJNII9)

- **问题 / 瓶颈** · 最终重排只影响选中的输出。
- **核心创新 / 方法** · 在逆扩散中加入基于当前最高奖励的非对称粒子交互。
- **Baseline** · 普通 Best-of-N 与 SMC。
- **Benchmark** · 36 组生成比较及多输出 ImageReward。
- **关键结果 / 消融** · 29 组领先；作者报告多输出奖励约 1.3 倍。
- **适用条件 / 局限** · 依赖奖励模型，奖励偏差可能被强化。

**可复用机制** · 按相同预算比较过程内引导与最终重排，同时评估最佳和平均结果。

<a id="paper-155229"></a>

## Bet Imaginatively, not Historically in Independent-Data Sequential Testing

[官方论文页](https://neurips.cc/virtual/2026/poster/155229) · [作者来源](https://openreview.net/forum?id=7JEwqlPhhF)

- **问题 / 瓶颈** · 对抗式序贯策略未充分利用可交换的样本顺序。
- **核心创新 / 方法** · FLOE 用留一的 e-power 重排估计与正则化确定下注。
- **Baseline** · 基于历史证据的在线下注策略。
- **Benchmark** · 多种核两样本检验。
- **关键结果 / 消融** · 作者报告检验性能改善，样本量和幅度待核。
- **适用条件 / 局限** · 依赖独立且平稳的数据流。

**可复用机制** · 先检验顺序假设，再比较重排下注和一般在线策略。

<a id="paper-140098"></a>

## Better Language Models Require Better Domain-Specific Inductive Biases

[官方论文页](https://neurips.cc/virtual/2026/poster/140098) · [作者来源](https://openreview.net/forum?id=E7jxq4ttP2)

- **问题 / 瓶颈** · 单领域优化的结构未必改善通用学习。
- **核心创新 / 方法** · 在不同训练子域学习激活函数，再评估域内与跨域迁移。
- **Baseline** · 标准 Transformer 与各领域改造版本。
- **Benchmark** · FineWeb、TinyStories 和数学数据上的评估。
- **关键结果 / 消融** · 自然语言优化可迁移到另一语言集，数学优化可能损伤语言表现。
- **适用条件 / 局限** · 仅探索了论文选择的架构和训练设定。

**可复用机制** · 训练多领域模型时用配对迁移矩阵评估归纳偏置。
