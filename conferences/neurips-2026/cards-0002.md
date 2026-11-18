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
