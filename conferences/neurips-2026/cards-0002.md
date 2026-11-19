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

<a id="paper-148679"></a>

## Better Source, Better Flow: Learning Condition-Dependent Source Distribution for Flow Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/148679) · [作者来源](https://openreview.net/forum?id=vtr94l6tFI)

- **问题 / 瓶颈** · 标准高斯忽略条件与目标结构
- **核心创新 / 方法** · 以方差正则和源目标方向对齐稳定条件源学习
- **Baseline** · 固定高斯及已有条件源与条件耦合
- **Benchmark** · 多个文本生图基准及骨干，比较 FID 和 CLIP 收敛
- **关键结果 / 消融** · 最高分别加速 3.01 倍和 2.48 倍
- **适用条件 / 局限** · 收益依赖目标表征

**可复用机制** · 按潜空间类型测学习源的收益

<a id="paper-152044"></a>

## Beyond Adjacent Layers: Graph-Guided Layer Fusion for Compressing Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152044) · [作者来源](https://openreview.net/forum?id=VvbFs1vt1f)

- **问题 / 瓶颈** · 相邻分组遗漏远距离重复
- **核心创新 / 方法** · 用 CKA 建图做谱聚类，每组保留高影响层再 LoRA 恢复
- **Baseline** · ShortGPT、FlattenGPT、SWM、DeltaLLM
- **Benchmark** · 13 个模型及五项推理基准
- **关键结果 / 消融** · 二倍压缩时十个模型困惑度显著改善，Mistral-7B 退化
- **适用条件 / 局限** · 需校准和恢复数据

**可复用机制** · 比较相邻划分与全局社区，并报告退化模型

<a id="paper-150087"></a>

## Beyond Appearance Shifts: Task-Semantic Action Calibration for VLA Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150087) · [作者来源](https://openreview.net/forum?id=kp5MjxtJIC)

- **问题 / 瓶颈** · 外观扰动过度改变动作，真实目标变化反而不敏感
- **核心创新 / 方法** · 冻结策略上优先校准语义变化，再按证据启用外观稳健辅助
- **Baseline** · OpenPI-pi0.5 原策略
- **Benchmark** · LIBERO-Object Milk-Swap 与风格变化
- **关键结果 / 消融** · 风格变化成功率 42% 到 70%，交换后旧任务成功率为零
- **适用条件 / 局限** · 旧任务抑制不等于新任务成功

**可复用机制** · 分开报告目标变化后的旧目标抑制和新目标达成

<a id="paper-148942"></a>

## Beyond Augmented-Action Surrogates for Multi-Expert Learning-to-Defer

[官方论文页](https://neurips.cc/virtual/2026/poster/148942) · [作者来源](https://openreview.net/forum?id=u1sVK3I1mr)

- **问题 / 瓶颈** · 共享动作归一化会耦合类别和专家并弱化稀有专家
- **核心创新 / 方法** · 类别 softmax 分支与独立专家 sigmoid，消除交叉 Hessian 项
- **Baseline** · 共享类别专家动作的替代损失
- **Benchmark** · 合成、CIFAR-10、CIFAR-10H、Covertype
- **关键结果 / 消融** · 摘要报告专家数增大时更稳定并保留罕见专家
- **适用条件 / 局限** · 需要获得专家表现监督

**可复用机制** · 单独检验稀有专家召回与系统准确率

<a id="paper-150477"></a>

## Beyond Average Flatness: Domain-wise Flatness for Domain Generalization

[官方论文页](https://neurips.cc/virtual/2026/poster/150477) · [作者来源](https://openreview.net/forum?id=hlSHsj1M7I)

- **问题 / 瓶颈** · 平均损失平坦可掩盖单域尖锐
- **核心创新 / 方法** · 惩罚平均逐域尖锐度并用平方变异系数避免不平衡退化
- **Baseline** · 对平均域损失做 SAM
- **Benchmark** · 标准域泛化评测及 Hessian 诊断
- **关键结果 / 消融** · 摘要报告平均表现和主方向对齐改善
- **适用条件 / 局限** · 需要清楚的训练域划分

**可复用机制** · 固定模型预算对照平均梯度和逐域扰动

<a id="paper-139620"></a>

## Beyond Bag-of-Words: Diagnosing Compositional Binding Failures in Vision-Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139620) · [作者来源](https://openreview.net/forum?id=Ew0J173lER)

- **问题 / 瓶颈** · 复杂图像会混淆绑定能力与干扰鲁棒性
- **核心创新 / 方法** · 按概念生成最小及场景化样本并检测交换与混淆
- **Baseline** · CLIP、SigLIP 等超过 25 个模型
- **Benchmark** · 颜色、形状颜色、位置和相对尺寸
- **关键结果 / 消融** · 场景上下文有助关系推理却妨碍属性绑定
- **适用条件 / 局限** · 人工生成数据的真实性需校验

**可复用机制** · 将同一关系的简单版和复杂版成对用于评测

<a id="paper-139462"></a>

## Beyond Chamfer Distance: Granular Order-aware Evaluation Metric For Online Mapping

[官方论文页](https://neurips.cc/virtual/2026/poster/139462) · [作者来源](https://openreview.net/forum?id=OFy3tWBIVi)

- **问题 / 瓶颈** · Chamfer 距离忽略顺序，硬阈值掩盖误差
- **核心创新 / 方法** · 用顺序感知距离和软分配联合评估
- **Baseline** · 基于 Chamfer 的 mAP、MapTRv2、StreamMapNet、MapTracker
- **Benchmark** · nuScenes 在线地图
- **关键结果 / 消融** · 分解诊断发现检出是主要瓶颈
- **适用条件 / 局限** · 结论待跨地图数据复核

**可复用机制** · 按拓扑对象顺序设计距离并分开报告漏检和几何误差

<a id="paper-153088"></a>

## Beyond Clipping: Signed Logarithmic Smoothing for Policy Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/153088) · [作者来源](https://openreview.net/forum?id=O4LWIO9opj)

- **问题 / 瓶颈** · 比率裁剪造成非光滑与尾部偏差
- **核心创新 / 方法** · 对加权更新做带符号对数平滑
- **Baseline** · 裁剪代理和 GRPO
- **Benchmark** · 上下文赌博机与数学推理 RLVR
- **关键结果 / 消融** · 摘要报告参考策略 KL 更低且熵更高，准确率未降
- **适用条件 / 局限** · 遗憾理论限于赌博机

**可复用机制** · 同时比较裁剪和平滑的偏差、策略漂移与效果

<a id="paper-152728"></a>

## Beyond Copy-Paste: How Well Do Subject-Driven Video Models Understand Their Subjects?

[官方论文页](https://neurips.cc/virtual/2026/poster/152728) · [作者来源](https://openreview.net/forum?id=QnZfz1xiAO)

- **问题 / 瓶颈** · 与参考相似的自由生成可能只在复制外观
- **核心创新 / 方法** · 构造锚定的视角变化与退化恢复两类探针
- **Baseline** · 传统自由生成与参考相似评分
- **Benchmark** · 七个主体驱动视频模型
- **关键结果 / 消融** · VACE-14B 原评第一，锚定评测 Phantom-14B 领先
- **适用条件 / 局限** · 探针依赖目标素材和推理适配

**可复用机制** · 将可见细节复现和未见内容泛化分离验收

<a id="paper-151953"></a>

## Beyond Correctness: Robustness-Driven Evolutionary Self-Training for Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151953) · [作者来源](https://openreview.net/forum?id=WZIsP7IaVI)

- **问题 / 瓶颈** · 二元正确标签混合了脆弱和稳健轨迹
- **核心创新 / 方法** · 进化筛选鲁棒轨迹，再做监督微调
- **Baseline** · 按结果筛选的后训练
- **Benchmark** · 复杂数学题，预算匹配
- **关键结果 / 消融** · 摘要报告优于结果基线，幅度待核
- **适用条件 / 局限** · 稳健性与数学洞察的联系依赖扰动定义

**可复用机制** · 固定训练预算比较仅按正确率与按局部稳定性筛选

<a id="paper-155956"></a>

## Beyond Data Scaling: Representation-Centric Pre-training for Vision-Language-Action Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155956) · [作者来源](https://openreview.net/forum?id=1ZmDZUFxCk)

- **问题 / 瓶颈** · 机器人轨迹少，单动作头易使骨干专门化
- **核心创新 / 方法** · 保留语言视觉先验，用多个动作头和部分统一动作布局联合训练
- **Baseline** · ABot-M0、LingBot-VLA、GR00T-N1.6
- **Benchmark** · LIBERO-Plus、RoboTwin 2.0、RoboCasa-GR1
- **关键结果 / 消融** · 前两项成功率 82.6% 和 92.5%，未见本体用两成轨迹超全数据对照
- **适用条件 / 局限** · 各子设计贡献待全文核实

**可复用机制** · 固定下游协议比较跨本体复用与后端可替换性

<a id="paper-153695"></a>

## Beyond Decoupled PEFT: Geometry-Aware Low-Rank Adaptation via Riemannian Reparameterization

[官方论文页](https://neurips.cc/virtual/2026/poster/153695) · [作者来源](https://openreview.net/forum?id=JSyN48PcBY)

- **问题 / 瓶颈** · 欧氏方向更新后再归一化会浪费径向容量
- **核心创新 / 方法** · 切空间正交投影后用黎曼指数映射构造球面路径
- **Baseline** · LoRA 与权重分解适配
- **Benchmark** · 语言、视觉、代码与多模态推理
- **关键结果 / 消融** · 作者报告持续优于对照且离线合并后无额外推理开销
- **适用条件 / 局限** · 几何假设与增益幅度待核

**可复用机制** · 在相同秩和算力下比较切空间更新和直接归一化

<a id="paper-149187"></a>

## Beyond difficulties: Insights for provably efficient design of autocurriculum in RLVR

[官方论文页](https://neurips.cc/virtual/2026/poster/149187) · [作者来源](https://openreview.net/forum?id=sFKx4xt4ab)

- **问题 / 瓶颈** · 难度无法隔离实际训练效用
- **核心创新 / 方法** · 以无穷小 GRPO 更新后单题期望奖励的增量定义改进函数，据此判定能力边缘
- **Baseline** · 成功率难度选题
- **Benchmark** · 多步组合题下的 GRPO 分析
- **关键结果 / 消融** · 给出能力边缘与近最大改进之间的形式联系
- **适用条件 / 局限** · 理论收益依赖小步更新和任务设定

**可复用机制** · 对比同难度题的实际学习增益

<a id="paper-154363"></a>

## Beyond Distribution Matching: Self-Supervised Representation Forcing for Few-Step Video Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/154363) · [作者来源](https://openreview.net/forum?id=E8R0wavtfd)

- **问题 / 瓶颈** · 极少步数下仅匹配输出难保时空结构
- **核心创新 / 方法** · 以不同噪声级别输入学生和 EMA 教师，用表示预测补充 DMD
- **Baseline** · 纯 DMD
- **Benchmark** · 少步视频生成与时空一致性
- **关键结果 / 消融** · 作者报告细节与时域一致性改善
- **适用条件 / 局限** · 受教师质量与噪声调度影响

**可复用机制** · 固定生成步数检查内部监督是否改善结构

<a id="paper-139098"></a>

## Beyond Downstream Scores: Controlled Diagnostics for Point-Cloud Self-Supervised Learning Evaluation

[官方论文页](https://neurips.cc/virtual/2026/poster/139098) · [作者来源](https://openreview.net/forum?id=l885Aav1TV)

- **问题 / 瓶颈** · 下游成绩无法说明提升来源
- **核心创新 / 方法** · 对坐标信号和几何删除等因素做控制诊断
- **Baseline** · 跨模态、自回归与掩码预训练
- **Benchmark** · ScanNet 等点云任务
- **关键结果 / 消融** · Concerto 中仅坐标解释 28.9% 的预训练损失响应，但只恢复 6.9% 下游增益
- **适用条件 / 局限** · 结论受具体读出与遮挡方式影响

**可复用机制** · 评估表征时分别定位预训练响应与迁移收益

<a id="paper-152248"></a>

## Beyond DSA: Conjugacy-based Comparison of Dynamical Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/152248) · [作者来源](https://openreview.net/forum?id=UUFDG6BQLR)

- **问题 / 瓶颈** · Koopman 正交等价与拓扑共轭不等价
- **核心创新 / 方法** · CSA 以候选状态双射约束算子对齐
- **Baseline** · DSA 正交对齐
- **Benchmark** · 拓扑共轭判别与动力系统比较
- **关键结果 / 消融** · 论文给出正交对齐不充分也非必要的反例
- **适用条件 / 局限** · 有限观测与候选映射质量限制判别

**可复用机制** · 比较系统前明确所需的等价关系

<a id="paper-153338"></a>

## Beyond Eigenfunctions: Divergence Principal Functions for Representation Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/153338) · [作者来源](https://openreview.net/forum?id=M4JVbTCh2k)

- **问题 / 瓶颈** · 不同学习目标并非同一核的等价估计器
- **核心创新 / 方法** · 以散度主函数推广平方误差下的特征函数
- **Baseline** · 平方误差谱分解
- **Benchmark** · 不同统计散度下的低秩表示分析
- **关键结果 / 消融** · 平方误差是特例，光滑散度诱导不同局部几何
- **适用条件 / 局限** · 局部分析依赖散度与光滑设定

**可复用机制** · 更换对比目标时评估是否也改变了保留的方向

<a id="paper-152266"></a>

## Beyond Encoder Accumulation: Measuring Encoder Roles in Multi-Encoder VLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/152266) · [作者来源](https://openreview.net/forum?id=ULmvjjKzd3)

- **问题 / 瓶颈** · 固定检查点遮蔽会混入训练时耦合效应
- **核心创新 / 方法** · 重训五种编码器的 31 个非空子集，分解独立能力与移除影响
- **Baseline** · 固定检查点遮蔽
- **Benchmark** · Cambrian-1 的 16 个基准
- **关键结果 / 消融** · 两种评测改变编码器排序，包括第一名
- **适用条件 / 局限** · 完整子集重训成本高

**可复用机制** · 架构选型区分独立容量、组内必要性和替代性

<a id="paper-155700"></a>

## Beyond Exemplar Selection: Value-Aware Memory Allocation in Replay-Based Continual Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/155700) · [作者来源](https://openreview.net/forum?id=3bHKdbo9Qx)

- **问题 / 瓶颈** · 仅优化类内样本时类别配额往往均匀
- **核心创新 / 方法** · 用 Shapley 启发的样本效用估计类别价值，正则约束偏离均衡
- **Baseline** · 类别均衡回放
- **Benchmark** · 固定缓存持续学习
- **关键结果 / 消融** · 作者将收益归因对象明确为类别级预算，精确结果待核
- **适用条件 / 局限** · 效用估计须稳健，任务间仍保持平衡

**可复用机制** · 固定类内采样器只改类配额来隔离收益

<a id="paper-149403"></a>

## Beyond Expected Values: Risk-Sensitive Planning with Distributional Monte-Carlo Tree Search

[官方论文页](https://neurips.cc/virtual/2026/poster/149403) · [作者来源](https://openreview.net/forum?id=qKB3gDxeBz)

- **问题 / 瓶颈** · 均值备份无法区分尾部风险
- **核心创新 / 方法** · 以分类原子或自适应粒子近似边回报，按采样 CVaR 加乐观项选动作
- **Baseline** · 均值 MCTS 与两种分布表示
- **Benchmark** · 有限深度嵌套 CVaR 规划
- **关键结果 / 消融** · 根值误差界为每 n 次滚动 O(n^-1/2)
- **适用条件 / 局限** · 结论针对有限深度和指定风险目标

**可复用机制** · 比较均值与 CVaR 规划时同时测尾部失败和算力

<a id="paper-152802"></a>

## Beyond FLOPs: Train-Full, Deploy-Partial Multi-Exit Inference via Selective Lightweight IC Ensemble

[官方论文页](https://neurips.cc/virtual/2026/poster/152802) · [作者来源](https://openreview.net/forum?id=QGgoHv7Q3A)

- **问题 / 瓶颈** · 动态分支阻碍编译融合，低 FLOPs 未必低延迟
- **核心创新 / 方法** · 训练全骨干和中间头，部署前校准静态深度及头集合
- **Baseline** · SDN 和 ResNet-56
- **Benchmark** · Jetson Orin Nano 上图像分类推理
- **关键结果 / 消融** · SDN 虽只用 40% FLOPs，实测约慢两倍
- **适用条件 / 局限** · 结果依赖设备和编译器

**可复用机制** · 选择退出深度时用实际时延与帧率验收

<a id="paper-155609"></a>

## Beyond Global Alignment: Structured Compositional Reasoning for Vision-Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155609) · [作者来源](https://openreview.net/forum?id=4HnBl3JKLK)

- **问题 / 瓶颈** · 全局图文对齐无法区分语义反转
- **核心创新 / 方法** · 用关系方向分桶及绑定定位补充全局对齐
- **Baseline** · 全局图文对齐
- **Benchmark** · 关系和属性绑定组合推理
- **关键结果 / 消融** · 作者提出针对两种错误的结构监督，定量待核
- **适用条件 / 局限** · 依赖关系与绑定证据质量

**可复用机制** · 以交换关系方向和交换属性的最小对作为独立测试

<a id="paper-150916"></a>

## Beyond Hard Negatives: Grounded Positive Supervision for Compositional CLIP

[官方论文页](https://neurips.cc/virtual/2026/poster/150916) · [作者来源](https://openreview.net/forum?id=eQSREPESTi)

- **问题 / 瓶颈** · 全局图文对齐会弱化局部属性和关系，模板式硬负例可能引入偏差。
- **核心创新 / 方法** · 以 IoU 加权区域和文本跨度的多正例对齐，同时对齐关系三元组。
- **Baseline** · 标准 CLIP 及硬负例变体。
- **Benchmark** · SugarCrepe、What'sUp、COLA、Winoground，另有检索和零样本识别。
- **关键结果 / 消融** · 作者报告组合评测与既有基线相比改善，具体幅度待核。
- **适用条件 / 局限** · 微调需要区域标注；推理仍用图文双编码器。

**可复用机制** · 固定骨干比较区域正监督和改写负例，分开测组合与全局检索。

<a id="paper-139490"></a>

## Beyond IID: How General Are Tabular Foundation Models, Really?

[官方论文页](https://neurips.cc/virtual/2026/poster/139490) · [作者来源](https://openreview.net/forum?id=Mk0ohjszwO)

- **问题 / 瓶颈** · 常见基准容易偏向基础模型已占优的规模和数据性质。
- **核心创新 / 方法** · BeyondArena 用 DataFoundry 统一异质任务和元数据。
- **Baseline** · 11 个基础、树和深度模型。
- **Benchmark** · 142 个数据集，按划分方式、样本规模、维度和特征类型比较。
- **关键结果 / 消融** · 基础模型在小中型 IID 表上强，树和深度模型在非 IID、大样本或高维设置仍占优。
- **适用条件 / 局限** · 模型排名与划分和调参预算有关。

**可复用机制** · 对实际项目用相同切分协议复现不同模型族排名。

<a id="paper-154427"></a>

## Beyond Imputation: Mask-Adaptive Conformal Prediction via Tree Embeddings on General Missing Data Mechanisms

[官方论文页](https://neurips.cc/virtual/2026/poster/154427) · [作者来源](https://openreview.net/forum?id=DfxyPWNH8L)

- **问题 / 瓶颈** · 边际覆盖可能隐藏特定缺失模式的欠覆盖，插补也可能遮蔽模式。
- **核心创新 / 方法** · 联合树嵌入与原始缺失掩码学习正则化分位数分数。
- **Baseline** · 边际及其他缺失数据校准方式，具名基线待核。
- **Benchmark** · 合成和真实数据，分析 MCAR、MAR、MNAR 下的条件覆盖和区间。
- **关键结果 / 消融** · 作者区分逐坐标、已观测掩码的精确保证及一般机制下的近似保证。
- **适用条件 / 局限** · 保证随增强、惩罚和缺失条件变化。

**可复用机制** · 部署区间时按掩码分层对比直接建模与插补方案。

<a id="paper-152763"></a>

## Beyond Incremental Beam Search for Compositional Explanations of Neurons

[官方论文页](https://neurips.cc/virtual/2026/poster/152763) · [作者来源](https://openreview.net/forum?id=QYZFm5iY4H)

- **问题 / 瓶颈** · 增量束搜索会漏掉需整块逻辑组合才能得到的解释。
- **核心创新 / 方法** · 加入非增量扩展并合并功能等价逻辑公式。
- **Baseline** · 增量束搜索及可计算时的最优解。
- **Benchmark** · 语言和视觉任务，测逻辑解释与激活对齐、运行时间和最优解数。
- **关键结果 / 消融** · 作者报告对齐更高，时间可比，找到更多可算最优解。
- **适用条件 / 局限** · 依赖概念集和等价判定效率。

**可复用机制** · 搜索组合解释时预算固定，以功能等价类减少重复探索。

<a id="paper-148658"></a>

## Beyond Interpretability: When, Why, and How Sparse Autoencoders Enable Label-Free Visual Steering

[官方论文页](https://neurips.cc/virtual/2026/poster/148658) · [作者来源](https://openreview.net/forum?id=w6uFnfYXcZ)

- **问题 / 瓶颈** · 能重建视觉激活的特征未必有助于分类。
- **核心创新 / 方法** · 无标签训练 top-k SAE，放大活跃特征并解码差值；重建不可靠时回退。
- **Baseline** · 零样本 CLIP 和选择性放大的上界实验。
- **Benchmark** · 九个图像分类数据集，测准确率和额外算力。
- **关键结果 / 消融** · 作者报告最高 4.12% 的准确率增益及低于 0.1% 附加推理计算；选择性上界更大。
- **适用条件 / 局限** · 需要目标域无标签激活，特征重建重要性与任务价值仍可能分离。

**可复用机制** · 按样本可靠性门控表征干预，并对照所有特征与选择性干预。

<a id="paper-154771"></a>

## Beyond Isolation: Neighbor-Consistent Data Pruning for Multivariate Time Series Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/154771) · [作者来源](https://openreview.net/forum?id=B5ACjqvQ2x)

- **问题 / 瓶颈** · 逐条算损失忽略窗口重叠产生的依赖。
- **核心创新 / 方法** · 在多尺度比较排序损失轨迹的邻居 Wasserstein 距离，以相对秩剪枝。
- **Baseline** · 五种剪枝方法及未剪枝模型。
- **Benchmark** · 六个多变量预测基准、四种预测长度、五个种子及合成污染审计。
- **关键结果 / 消融** · 平均重训时间约为未剪枝的 48%，相对 MSE 最多降 1.56%。
- **适用条件 / 局限** · 依赖窗口邻居具备共享结构；真实突变也可能被识别为异常。

**可复用机制** · 数据窗口高度重叠时优先利用局部不一致，并单测突变期误剪。

<a id="paper-149858"></a>

## Beyond Isotropy in JEPAs: Hamiltonian Geometry and Symplectic Prediction

[官方论文页](https://neurips.cc/virtual/2026/poster/149858) · [作者来源](https://openreview.net/forum?id=mkhuJqvXlz)

- **问题 / 瓶颈** · 固定各向同性边缘分布难适配未知下游几何，也不能决定联合耦合。
- **核心创新 / 方法** · 用相空间表征和学习的 Hamiltonian leapfrog 预测跨视图变换。
- **Baseline** · SIGReg 和匹配的 MLP 预测器消融。
- **Benchmark** · CIFAR-100 与 ImageNet-100，测 kNN@20 和线性探针。
- **关键结果 / 消融** · CIFAR-100 的 80 轮线性探针较 SIGReg 高 10.64 点。
- **适用条件 / 局限** · 收益来自所测训练设置，换预测器或数据仍需验证。

**可复用机制** · 固定编码器边缘约束，单独改变跨视图耦合并测近邻几何。

<a id="paper-148807"></a>

## Beyond Linear Activation Steering: Invertible Latent Transformations for Controlling LLM Behavior

[官方论文页](https://neurips.cc/virtual/2026/poster/148807) · [作者来源](https://openreview.net/forum?id=uyN7V3sdbW)

- **问题 / 瓶颈** · 全局固定偏移难适配弯曲、各向异性的行为表征。
- **核心创新 / 方法** · 学习可逆表征映射，使原空间中的非线性调整可表示为潜空间平移。
- **Baseline** · 线性、运输及非线性表征控制方法。
- **Benchmark** · 多个模型家族和行为指标，另测语言流畅度。
- **关键结果 / 消融** · 作者报告控制效果提高，整体流畅度大致保持，数值待核。
- **适用条件 / 局限** · 依赖训练数据覆盖与映射泛化，不同任务间需重新验证。

**可复用机制** · 选择表征干预时联合检查任务行为与通用语言质量。

<a id="paper-149719"></a>

## Beyond LLM-Based Reasoning: Lightweight GNNs for Agent Failure Attribution

[官方论文页](https://neurips.cc/virtual/2026/poster/149719) · [作者来源](https://openreview.net/forum?id=nw9eqYKGy0)

- **问题 / 瓶颈** · 直接用大模型读历史轨迹成本高，效果也有限。
- **核心创新 / 方法** · 在图内编码步骤语义及 Agent 间关系，预测责任方与错误类型。
- **Baseline** · 直接提示、微调和基于语言模型的归因流程。
- **Benchmark** · 域内与域外故障归因评测，具名数据集待核。
- **关键结果 / 消融** · 作者报告域内可追平或超过语言模型方法，域外可用低成本适配改善。
- **适用条件 / 局限** · 依赖可抽取的步骤语义和交互关系。

**可复用机制** · 对固定故障集比较图分类和生成式诊断的准确率、开销与跨域表现。

<a id="paper-154880"></a>

## Beyond LoRA vs. Full Fine-Tuning: Gradient-Guided Optimizer Routing for LLM Adaptation

[官方论文页](https://neurips.cc/virtual/2026/poster/154880) · [作者来源](https://openreview.net/forum?id=AC9LxjWtTf)

- **问题 / 瓶颈** · 有些任务需要全量表达能力，有些任务更受益于低秩正则。
- **核心创新 / 方法** · 保证两个更新方式可访问梯度，并按训练情况路由；省内存版本只在低秩专家间路由。
- **Baseline** · LoRA、全量微调及其他自适应 LoRA。
- **Benchmark** · SQL、医学问答和反事实知识，覆盖 Gemma 与 Qwen。
- **关键结果 / 消融** · 作者报告 MoLF 达到较优对照或差距不超过 1.5%，省内存版本在所测任务有额外增益。
- **适用条件 / 局限** · 全量更新和双专家成本随实现而异。

**可复用机制** · 先用两种静态方案测任务需求，再和动态优化器路由比较。

<a id="paper-148662"></a>

## Beyond Low-Pass Dynamics: Frequency-Selective Spiking Reservoirs with Resonant Neurons

[官方论文页](https://neurips.cc/virtual/2026/poster/148662) · [作者来源](https://openreview.net/forum?id=w4gGQ1ybW6)

- **问题 / 瓶颈** · 泄漏积分发放单元低通特性容易忽略高频信息。
- **核心创新 / 方法** · 用固有振荡频率不同的发放单元构成固定储备池。
- **Baseline** · LIF 储备池及非脉冲振荡储备池。
- **Benchmark** · 八个时序、逐序图像、音频脉冲和神经形态视觉基准。
- **关键结果 / 消融** · 作者报告分类改善，对等非脉冲储备池能耗低 9–14 倍。
- **适用条件 / 局限** · 能耗结果依赖硬件及估算协议，频率分布需按任务验证。

**可复用机制** · 对有已知谱多样性的信号比较低通和共振储备池的性能与成本。

<a id="paper-153265"></a>

## Beyond Marginal Coverage: Efficient Localized Conformal Prediction via Residual Rank Calibration

[官方论文页](https://neurips.cc/virtual/2026/poster/153265) · [作者来源](https://openreview.net/forum?id=MYBb7WHPyQ)

- **问题 / 瓶颈** · 边际有效不能确保局部覆盖，完整估计条件分布的成本高。
- **核心创新 / 方法** · 先拟合位置和噪声尺度，再用残差直方图及局部秩比较。
- **Baseline** · CQR、CHR 和加权局部化 RBC-CHR。
- **Benchmark** · 合成和真实数据，评估最差局部覆盖、区间宽度与成本。
- **关键结果 / 消融** · 作者证明有限样本边际保证及条件满足时的渐近局部保证，并报告区间改善。
- **适用条件 / 局限** · 局部保证依赖残差分布稳定性，有限样本只保证边际。

**可复用机制** · 按局部覆盖和推理开销对照完整条件模型与残差秩校准。

<a id="paper-150469"></a>

## Beyond Masked Sparsity: SNACK Enables Truly Sparse Neural Networks on GPU

[官方论文页](https://neurips.cc/virtual/2026/poster/150469) · [作者来源](https://openreview.net/forum?id=hoB9d0ONXQ)

- **问题 / 瓶颈** · 掩码仍执行稠密计算
- **核心创新 / 方法** · 仅存非零连接并用面向小批量的 COO SpMM
- **Baseline** · Dense+Mask、稠密层和多个稀疏库
- **Benchmark** · 算子、GPT-2 训练及图推理
- **关键结果 / 消融** · 90% 稀疏时单层训练相对掩码快 8 倍；GPT-2 峰值显存最多降 40%
- **适用条件 / 局限** · 收益依赖稀疏率和批量

**可复用机制** · 把真实稀疏算子与掩码按端到端成本对照

<a id="paper-151995"></a>

## Beyond MMSE: Enhancing PnP Restoration with ProxiMAP

[官方论文页](https://neurips.cc/virtual/2026/poster/151995) · [作者来源](https://openreview.net/forum?id=WIEiYfccQR)

- **问题 / 瓶颈** · 学习分数有偏，追求 MAP 收敛可能过度平滑
- **核心创新 / 方法** · 按噪声匹配调度做近似 MAP，可只替换后期迭代
- **Baseline** · MMSE PnP、MAP 迭代和全程替换
- **Benchmark** · 去模糊、修复、超分、相位恢复
- **关键结果 / 消融** · 报告更锐利，后期替换以更低开销达到可比结果
- **适用条件 / 局限** · 依赖残差噪声估计及去噪器

**可复用机制** · 扫描停止位置与训练噪声匹配程度

<a id="paper-155113"></a>

## Beyond Modality Fusion: Deep Ensembles for Multimodal Classification

[官方论文页](https://neurips.cc/virtual/2026/poster/155113) · [作者来源](https://openreview.net/forum?id=8Im8HCejDY)

- **问题 / 瓶颈** · 强弱模态失衡时联合优化困难
- **核心创新 / 方法** · 独立训练单模态模型并选择各模态成员数
- **Baseline** · 晚期、中期和混合融合
- **Benchmark** · 模态失衡分类，具体数据待核
- **关键结果 / 消融** · 报告集成胜过所测融合；小集成极端失衡时可只用强模态
- **适用条件 / 局限** · 优势受失衡和容量影响

**可复用机制** · 随集成预算扫各模态成员分配

<a id="paper-154780"></a>

## Beyond Outcome Rewards: Step-Level Self-Distilled Policy Optimization for Deep Search Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/154780) · [作者来源](https://openreview.net/forum?id=B1ywhnzK7h)

- **问题 / 瓶颈** · 特权教师直接蒸馏会泄露答案路径
- **核心创新 / 方法** · 以局部证据片段构造教师，用分歧加权 GRPO 步优势
- **Baseline** · 结果奖励及直接自蒸馏
- **Benchmark** · 深度搜索任务，名称与数值待核
- **关键结果 / 消融** · 摘要提出将更新方向和步幅解耦，完整结果待核
- **适用条件 / 局限** · 证据锚点的质量影响权重

**可复用机制** · 让教师决定更新幅度，方向仍由任务反馈决定

<a id="paper-154868"></a>

## Beyond Oversquashing: Understanding Signal Propagation in GNNs Via Observables

[官方论文页](https://neurips.cc/virtual/2026/poster/154868) · [作者来源](https://openreview.net/forum?id=AItejpYJ0K)

- **问题 / 瓶颈** · 平滑或压缩指标不能直接描述传播方向
- **核心创新 / 方法** · 用可观测量刻画位置、集中和输运，提出 Schrödinger GNN
- **Baseline** · 标准谱 GNN
- **Benchmark** · 谱 GNN 信号传播理论
- **关键结果 / 消融** · 给出标准谱方法输运受限及新方法改进结果
- **适用条件 / 局限** · 实际数据收益和图类型条件待核

**可复用机制** · 用定向输入扰动测目标区域响应

<a id="paper-150929"></a>

## Beyond Pairs: Your Language Model is Secretly Optimizing a Preference Graph

[官方论文页](https://neurips.cc/virtual/2026/poster/150929) · [作者来源](https://openreview.net/forum?id=eIAc9sNGjK)

- **问题 / 瓶颈** · 独立成对比较丢失传递结构或重复监督
- **核心创新 / 方法** · 用有向无环优先图与邻域聚合，平局合等价层
- **Baseline** · 标准 DPO 为特例
- **Benchmark** · 同提示多回答的偏好学习，实验细节待核
- **关键结果 / 消融** · 每提示可线性复杂度聚合
- **适用条件 / 局限** · 需偏好关系可表达为无环图

**可复用机制** · 先识别平局与支配再构造优化目标

<a id="paper-155550"></a>

## Beyond Parameter Aggregation: Semantic Consensus for Federated Fine-Tuning of LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/155550) · [作者来源](https://openreview.net/forum?id=4jInQZ53nD)

- **问题 / 瓶颈** · 聚合参数要求结构一致及白盒访问
- **核心创新 / 方法** · 公共提示上的生成结果映射到语义空间，聚合为伪标签
- **Baseline** · 强联邦微调基线，具体名称待核
- **Benchmark** · 异构模型开放生成，比较通信与性能
- **关键结果 / 消融** · 报告性能可比且通信下降
- **适用条件 / 局限** · 依赖公共提示覆盖，不等于形式化隐私保证

**可复用机制** · 按公共提示预算比较行为交换和参数交换

<a id="paper-149097"></a>

## Beyond Parameter Arithmetic: Sparse Complementary Fusion for Distribution-Aware Model Merging

[官方论文页](https://neurips.cc/virtual/2026/poster/149097) · [作者来源](https://openreview.net/forum?id=swWyB0I1Tq)

- **问题 / 瓶颈** · 权重平均会导致循环或不终止
- **核心创新 / 方法** · 以参数组代理分布的反向 KL 筛互补稀疏参数
- **Baseline** · 参数平均等训练免合并
- **Benchmark** · 7B 至 32B、24 项评测
- **关键结果 / 消融** · 报告异常比例由既有方法超过 97% 的情形降到低于 1%
- **适用条件 / 局限** · 依赖代理分布与源模型兼容

**可复用机制** · 在合并评测中单独记录重复与终止失败

<a id="paper-152220"></a>

## Beyond Pixel Space: Frequency-Domain Uncertainty Estimation for Structure-Aware Diffusion Guidance

[官方论文页](https://neurips.cc/virtual/2026/poster/152220) · [作者来源](https://openreview.net/forum?id=UfOJVYkmfd)

- **问题 / 瓶颈** · 像素独立估计忽视结构相关
- **核心创新 / 方法** · 频域不确定性梯度调节反向均值，同时用不确定性调整噪声
- **Baseline** · 像素空间不确定性
- **Benchmark** · ImageNet、LSUN-Churches、DrawBench，三种网络架构
- **关键结果 / 消融** · 报告不确定性与伪影关联，采样结果改善
- **适用条件 / 局限** · 额外计算开销及频域归因待核

**可复用机制** · 将均值引导和注入噪声分开消融

<a id="paper-155042"></a>

## Beyond Prediction: Steering VLM Agents with Retrospective World Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/155042) · [作者来源](https://openreview.net/forum?id=8sWyZTPe9o)

- **问题 / 瓶颈** · 只预测未来并不检验动作是否与实际转移一致
- **核心创新 / 方法** · 根据转移前后状态估计动作归因分布，以与实际动作的吻合度作奖励
- **Baseline** · 只做前向建模的路线，具名对照待核
- **Benchmark** · 多种智能体任务，实验细项待核
- **关键结果 / 消融** · 摘要报告策略表现改善，数值待核
- **适用条件 / 局限** · 多动作能产生同一转移时归因可能歧义

**可复用机制** · 在预测奖励外对照加入逆向一致性奖励

<a id="paper-150607"></a>

## Beyond RAG for Agent Memory: Retrieval by Decoupling and Aggregation

[官方论文页](https://neurips.cc/virtual/2026/poster/150607) · [作者来源](https://openreview.net/forum?id=gtGRNOmx4m)

- **问题 / 瓶颈** · 近重复对话使平坦检索冗余
- **核心创新 / 方法** · 将原消息组织成可修订的片段、成分和组
- **Baseline** · 平坦 top-k 与摘要层级
- **Benchmark** · 对话记忆任务，具名设定待核
- **关键结果 / 消融** · 摘要未量化结果或独立消融，待全文核查。
- **适用条件 / 局限** · 细节辨别与冗余取舍待核

**可复用机制** · 比较相同预算下的先分解与先摘要

<a id="paper-151291"></a>

## Beyond Row Alignment: Virtual-Camera-Aware Online Stereo Rectification

[官方论文页](https://neurips.cc/virtual/2026/poster/151291) · [作者来源](https://openreview.net/forum?id=bWCyY4WYr9)

- **问题 / 瓶颈** · 行对齐不能保证立体几何可靠
- **核心创新 / 方法** · 按虚拟相机约束设计校正
- **Baseline** · 仅优化行对齐
- **Benchmark** · 在线校正及深度估计，设置待核
- **关键结果 / 消融** · 摘要未量化结果或独立消融，待全文核查。
- **适用条件 / 局限** · 漂移与对应点覆盖边界待核

**可复用机制** · 在相同行误差下继续检查下游深度

<a id="paper-153671"></a>

## Beyond Scalar Distances: Semantic Attribute Gradients from Frozen MLLMs for Visual Embeddings

[官方论文页](https://neurips.cc/virtual/2026/poster/153671) · [作者来源](https://openreview.net/forum?id=JddD3RHEz2)

- **问题 / 瓶颈** · 类别标签将多种属性差异压缩成标量
- **核心创新 / 方法** · 冻结多模态模型并以成对判断奖励给视觉表征提供信号
- **Baseline** · 类别标签的拉近或推远目标
- **Benchmark** · 视觉检索，具体基准待核
- **关键结果 / 消融** · 摘要未量化结果或独立消融，待全文核查。
- **适用条件 / 局限** · 依赖教师辨认属性和奖励质量

**可复用机制** · 用相同类别标签比较属性监督和标量监督

<a id="paper-151663"></a>

## Beyond Selection: Token Parameterization for Extreme Visual Token Compression

[官方论文页](https://neurips.cc/virtual/2026/poster/151663) · [作者来源](https://openreview.net/forum?id=YySQ07LVAC)

- **问题 / 瓶颈** · 极限剪枝损伤视觉定位，重采样又增加代价
- **核心创新 / 方法** · 基底截断配坐标嵌入及预算相关正交重参数化
- **Baseline** · 视觉 token 剪枝及学习式重采样
- **Benchmark** · 极低视觉 token 预算，任务待核
- **关键结果 / 消融** · 摘要未量化结果或独立消融，待全文核查。
- **适用条件 / 局限** · 坐标组织依赖压缩预算

**可复用机制** · 固定 token 数对照保留子空间和坐标布局

<a id="paper-149809"></a>

## Beyond Semantic Alignment: Geometric Incomparability in Multi-Oracle Soft Fusion

[官方论文页](https://neurips.cc/virtual/2026/poster/149809) · [作者来源](https://openreview.net/forum?id=nBr25BUjYj)

- **问题 / 瓶颈** · 共享标签不能保证各模型的置信度几何一致
- **核心创新 / 方法** · 在概率单纯形上以各模型专有校正映射学习共识
- **Baseline** · 直接软融合
- **Benchmark** · 多决策源融合，数据集待核
- **关键结果 / 消融** · 摘要未量化结果或独立消融，待全文核查。
- **适用条件 / 局限** · 依赖几何描述符及校准数据

**可复用机制** · 比较融合前对齐与直接平均并单独测尾部

<a id="paper-156774"></a>

## Beyond Semantics: The Unreasonable Effectiveness of Reasonless Intermediate Tokens

[官方论文页](https://neurips.cc/virtual/2026/poster/156774) · [作者来源](https://neurips.cc/virtual/2026/poster/156774)

- **问题 / 瓶颈** · 可读推理轨迹可能并不忠实暴露内部计算
- **核心创新 / 方法** · 从头训练受形式规则约束的模型以控制轨迹和答案
- **Baseline** · 语义可解释的推导轨迹
- **Benchmark** · 形式可验证推理任务，基准待核
- **关键结果 / 消融** · 摘要未量化结果或独立消融，待全文核查。
- **适用条件 / 局限** · 从头训练的实验不一定外推到大模型

**可复用机制** · 固定答案监督并改变中间符号的语义，比较解题表现

<a id="paper-152213"></a>

## Beyond Single-Step Likelihood: Gibbs Variational Last Layers for Long-Horizon Dynamics Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/152213) · [作者来源](https://openreview.net/forum?id=Uj5JEkvShR)

- **问题 / 瓶颈** · 单步似然无法保证长期滚动校准
- **核心创新 / 方法** · 用 Gibbs 变分推断纳入多步损失、CRPS 及自回归滚动
- **Baseline** · 单步似然 VBLL
- **Benchmark** · 概率动力系统长期预测，基准待核
- **关键结果 / 消融** · 摘要未量化结果或独立消融，待全文核查。
- **适用条件 / 局限** · 训练成本与不同滚动长度的稳定性待核

**可复用机制** · 在相同末层结构下扫训练时域并比较概率校准

<a id="paper-149352"></a>

## Beyond Spatial and Temporal Priors: A Generalizable Approach for Dense Correspondence Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/149352) · [作者来源](https://openreview.net/forum?id=qhc3sU3mz5)

- **问题 / 瓶颈** · 编辑变化可违反刚体和运动平滑先验
- **核心创新 / 方法** · 先训练带标注匹配，再用缺少密集标注的数据弱监督细化
- **Baseline** · 经典对应匹配方法
- **Benchmark** · 经典匹配与视觉语言引导图像编辑
- **关键结果 / 消融** · 经典设置具竞争力，编辑一致性评分与人评接近
- **适用条件 / 局限** · 弱监督目标和量化细节待核

**可复用机制** · 分开测试物理位移和语义编辑后的身份保持

<a id="paper-150788"></a>

## Beyond Spatial-Domain Supervision: A Relation Constrained Space for Multi-Modal Image Fusion

[官方论文页](https://neurips.cc/virtual/2026/poster/150788) · [作者来源](https://openreview.net/forum?id=fOruP1Bc1v)

- **问题 / 瓶颈** · 没有真实融合图片作为监督
- **核心创新 / 方法** · 对齐冻结的 DINO 与 CLIP 特征，学习共享性、主导性和协调边界，交替优化
- **Baseline** · 多种融合骨干及空间域损失
- **Benchmark** · 多模态图像融合，具体基准待核
- **关键结果 / 消融** · 作者报告更换骨干仍有收益
- **适用条件 / 局限** · 依赖表征提供者适配目标模态

**可复用机制** · 以关系损失对照像素重建，分别测互补信息和冲突

<a id="paper-155564"></a>

## Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention

[官方论文页](https://neurips.cc/virtual/2026/poster/155564) · [作者来源](https://openreview.net/forum?id=4edRXBSyRO)

- **问题 / 瓶颈** · 固定单步干预在未见概念上可能弱于提示
- **核心创新 / 方法** · 在冻结模型的中间表征学习概念条件流
- **Baseline** · 提示与已有激活干预
- **Benchmark** · AxBench，Gemma-2-2B-IT 与 9B-IT
- **关键结果 / 消融** · 留出概念的调和均值分别为 1.015 和 1.113
- **适用条件 / 局限** · 额外推理成本和超出概念测试范围的泛化待核

**可复用机制** · 在未见概念按固定预算评估曲线干预与提示

<a id="paper-151865"></a>

## Beyond Structural Agnosticism: Stable-Rank-Guided LoRA for Structure-Aware Fine-Tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/151865) · [作者来源](https://openreview.net/forum?id=XJnhTtLoXc)

- **问题 / 瓶颈** · 统一配置忽视层间差异
- **核心创新 / 方法** · 稳定秩作先验，梯度反馈作校准，并保留总预算
- **Baseline** · LoRA 等参数高效微调基线
- **Benchmark** · 摘要未给具名任务
- **关键结果 / 消融** · 作者报告稳定且优于所比基线
- **适用条件 / 局限** · 需验证谱先验与任务梯度的各自作用

**可复用机制** · 固定参数预算做按层统一和自适应分配对照

<a id="paper-139429"></a>

## Beyond Success Rates: Trainability and Extractability in Offline GCRL

[官方论文页](https://neurips.cc/virtual/2026/poster/139429) · [作者来源](https://openreview.net/forum?id=RMzSje9qtp)

- **问题 / 瓶颈** · 最优一次成功率不反映稳定性
- **核心创新 / 方法** · 固定 AWR 提取器扫描学习率和温度，并测目标区分与权重集中
- **Baseline** · GCIQL、GCIVL、QRL、CRL
- **Benchmark** · AntMaze、Cube、Scene
- **关键结果 / 消融** · 目标排序在操作环境可与控制效果脱钩
- **适用条件 / 局限** · 结论依赖共享策略提取器

**可复用机制** · 同时报告成功上限和有效参数区域

<a id="paper-152482"></a>

## Beyond Suspicious Steps: Ontological Trust in Long-Horizon Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/152482) · [作者来源](https://openreview.net/forum?id=Skjgiw2yTJ)

- **问题 / 瓶颈** · 逐步合法不能排除整体目标漂移
- **核心创新 / 方法** · 用角色、目标、证据三路结构化表示，确定性更新并回放
- **Baseline** · 规则、裁判和防护式监控
- **Benchmark** · OSWorld、FinanceBench、EICU-AC
- **关键结果 / 消融** · 较大估计模型 Drift F1 均超 93%，良性覆盖至少 95.8%
- **适用条件 / 局限** · 隐含完成状态不易检测

**可复用机制** · 用良性和漂移配对前缀评估整体授权监控

<a id="paper-139465"></a>

## Beyond Task Success: Probing Cognitive Primitives in Web Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/139465) · [作者来源](https://openreview.net/forum?id=O8gCSB4In6)

- **问题 / 瓶颈** · 事后看轨迹无法证明任务必须使用某能力
- **核心创新 / 方法** · 对原任务添加使目标能力变得必要的条件
- **Baseline** · 六个前沿智能体与人类
- **Benchmark** · 七环境、七类能力、519 对任务
- **关键结果 / 消融** · 智能体下降 18–28%，人类下降 5.7%
- **适用条件 / 局限** · 需要证明两变体的差异确实隔离能力

**可复用机制** · 用严格配对替代单独排行榜判断能力缺口

<a id="paper-155487"></a>

## Beyond the Dirac Delta: Mitigating Diversity Collapse in Reinforcement Fine-Tuning for Image Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/155487) · [作者来源](https://openreview.net/forum?id=5EU8Z7LSE8)

- **问题 / 瓶颈** · 强化微调可能促使生成分布塌缩
- **核心创新 / 方法** · 筛掉奖励离群值、扰动提示并以势函数奖励组内多样性
- **Baseline** · 生成强化微调基线，名称待核
- **Benchmark** · 图像生成任务，对照匹配对齐度或多样性
- **关键结果 / 消融** · 匹配对齐时作者报告多样性高 7.19% 至 93.40%
- **适用条件 / 局限** · 三个组件的独立贡献待核

**可复用机制** · 扫描对齐与多样性的 Pareto 前沿

<a id="paper-149458"></a>

## Beyond the Full Slate: Evaluating MNL Algorithms on All Slates

[官方论文页](https://neurips.cc/virtual/2026/poster/149458) · [作者来源](https://openreview.net/forum?id=pwV1APiNY8)

- **问题 / 瓶颈** · 总体拟合好仍可能在某些子集失准
- **核心创新 / 方法** · 高效评估小候选集误差，用难度指导自适应采样
- **Baseline** · 最大似然、非自适应和自适应算法
- **Benchmark** · 多项 logit 推荐设置，测平均和最坏子集表现
- **关键结果 / 消融** · 最大似然最坏子集较差，自适应采样能缓解
- **适用条件 / 局限** · 依赖部署子集和稳健性目标

**可复用机制** · 同一模型同时测平均和最差候选集指标

<a id="paper-150344"></a>

## Beyond the Golden Teacher: Enhancing Graph Learning through LLM-GNN Co-teaching

[官方论文页](https://neurips.cc/virtual/2026/poster/150344) · [作者来源](https://openreview.net/forum?id=iq83tsXsBG)

- **问题 / 瓶颈** · 少标注时两模型都有独特盲区
- **核心创新 / 方法** · 互换小损失伪标签，将由冲突转一致的答案作为偏好对
- **Baseline** · 单向教导及 GNN-as-Judge
- **Benchmark** · 六个图基准，含 Cora 和 ogbn-arxiv
- **关键结果 / 消融** · 3-shot 绝对增益分别为 7.86% 和 7.73%
- **适用条件 / 局限** · 一致并不保证正确，需测共同错误

**可复用机制** · 少样本跨视图训练中比较固定教师和双向更新

<a id="paper-151808"></a>

## Beyond the Grid: Continuous Dictionary Pursuit for Interpretable Signal Decomposition

[官方论文页](https://neurips.cc/virtual/2026/poster/151808) · [作者来源](https://openreview.net/forum?id=XrVRVRXvqa)

- **问题 / 瓶颈** · 离散网格失配造成谱泄漏
- **核心创新 / 方法** · 用可微解析原子贪心拟合残差，并由原子预算控制稀疏性
- **Baseline** · 固定字典方法及端到端序列训练
- **Benchmark** · 合成与真实信号分解及预测
- **关键结果 / 消融** · 摘要报告降低谱泄漏并改善预测
- **适用条件 / 局限** · 只能解析所选原子族覆盖的成分

**可复用机制** · 测固定和连续字典的频率恢复及下游价值

<a id="paper-156758"></a>

## Beyond the Linear Separability Ceiling: Aligning Representations in VLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/156758) · [作者来源](https://neurips.cc/virtual/2026/poster/156758)

- **问题 / 瓶颈** · 生成回答低分无法定位感知或推理瓶颈
- **核心创新 / 方法** · 以线性分类器作参照，加对比目标促进视觉比较
- **Baseline** · 原始视觉线性探针和标准下一词训练
- **Benchmark** · Bongard 式抽象组合任务
- **关键结果 / 消融** · 作者报告多数模型未超过探针，训练调整能改善
- **适用条件 / 局限** · 线性探针是诊断参照，非一般上界

**可复用机制** · 固定视觉编码分别测线性探针与生成决策

<a id="paper-149841"></a>

## Beyond the Node Barrier: Zero-Shot Strategy Planning for LLM Training on Super-Nodes

[官方论文页](https://neurips.cc/virtual/2026/poster/149841) · [作者来源](https://openreview.net/forum?id=mtK2qojsrZ)

- **问题 / 瓶颈** · 沿用节点内部并行规则可能错过最优配置
- **核心创新 / 方法** · 根据模型形状、集合通信和硬件规格作符号打分
- **Baseline** · 节点内 Megatron 式配置
- **Benchmark** · 传统集群与超级节点，含 128 芯片训练
- **关键结果 / 消融** · 报告步时加速 1.40 倍，MFU 提高 10.62 个百分点
- **适用条件 / 局限** · 模型与拓扑变化时需要再次验证

**可复用机制** · 部署前按硬件拓扑比较跨节点与节点内并行

<a id="paper-151177"></a>

## Beyond the Prompt: Leveraging Pre-Decoding States for Jailbreak Detection in dLLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/151177) · [作者来源](https://openreview.net/forum?id=cQKisMHGgm)

- **问题 / 瓶颈** · 单看输入会漏掉响应生成阶段的风险信号
- **核心创新 / 方法** · 融合冻结的输入与解码前响应分类器
- **Baseline** · 无防护和两个单独检测器
- **Benchmark** · LLaDA-8B-Instruct 安全测试及正常任务误拒率
- **关键结果 / 消融** · 攻击成功率由 63.29% 降至 3.31%，正常误拒低于 1%
- **适用条件 / 局限** · 自适应与跨模型证据待核

**可复用机制** · 双视角检测分别报告漏检与正常误拒

<a id="paper-152483"></a>

## Beyond the Readout: Reservoir State Statistics for Model-Space Learning under Sparse Observations

[官方论文页](https://neurips.cc/virtual/2026/poster/152483) · [作者来源](https://openreview.net/forum?id=Skj69JdWAO)

- **问题 / 瓶颈** · 观测少时逐通道读出不稳
- **核心创新 / 方法** · 连续时间储备网络配合质心、离散程度和末状态摘要
- **Baseline** · 仅读出及其他少样本模型
- **Benchmark** · 多异步时序数据集，测准确率和 CPU 时间
- **关键结果 / 消融** · 少样本精度具竞争力，CPU 秒级运行
- **适用条件 / 局限** · 各数据集的缺测分布与消融待核

**可复用机制** · 对照模型参数和无需求逆的轨迹摘要

<a id="paper-149001"></a>

## Beyond the Training Distribution: Evaluating Predictions Under Distribution Shift and Selection Bias

[官方论文页](https://neurips.cc/virtual/2026/poster/149001) · [作者来源](https://openreview.net/forum?id=tZ71MZ096G)

- **问题 / 瓶颈** · 只校正一种偏差会误估部署风险
- **核心创新 / 方法** · 基于目标风险影响函数构造双重机器学习估计
- **Baseline** · 只修正一种偏差和直接代入
- **Benchmark** · eICU 电子病历，比较目标风险误差
- **关键结果 / 消融** · 作者报告更接近真实目标风险
- **适用条件 / 局限** · 依赖识别条件及标签机制由已观测特征解释

**可复用机制** · 上线前用带两种偏移的回放验证风险估计

<a id="paper-150603"></a>

## Beyond the Trial-and-Error Loop: Hybrid Projection and Automated Tuning for Distributed Training

[官方论文页](https://neurips.cc/virtual/2026/poster/150603) · [作者来源](https://openreview.net/forum?id=guQo7FnJYI)

- **问题 / 瓶颈** · 多节点实测搜索昂贵且易因显存失败
- **核心创新 / 方法** · 采样核函数和通信，外推大集群吞吐，并用显存约束预筛组合
- **Baseline** · 真实多节点测量及公开 BF16 配置
- **Benchmark** · Llama 3.1、Mixtral 8×22B 与两代 GPU
- **关键结果 / 消融** · 预测误差约 10% 内，案例吞吐高 27%
- **适用条件 / 局限** · 需要可校准的硬件与调度模型

**可复用机制** · 用少量实测验证模拟排序再扩大训练

<a id="paper-149744"></a>

## Beyond Thinking: Imagining in 360$^\circ$ for Humanoid Visual Search

[官方论文页](https://neurips.cc/virtual/2026/poster/149744) · [作者来源](https://openreview.net/forum?id=nf3SdflMnP)

- **问题 / 瓶颈** · 整段推理轨迹标注昂贵。
- **核心创新 / 方法** · 单步预测可见与遮挡区域的语义布局，采样多个假设供动作模块使用。
- **Baseline** · 累积式多轮推理。
- **Benchmark** · 复杂全景视觉搜索，测效率及成功率。
- **关键结果 / 消融** · 作者报告两项改善，并构建超过196万样本。
- **适用条件 / 局限** · 真实部署与标注成本对照待核。

**可复用机制** · 固定动作模块比较单一布局与多假设先验。

<a id="paper-155293"></a>

## Beyond Token Representations: Explicit Visual Object Grounding for Video Reasoning Segmentation

[官方论文页](https://neurips.cc/virtual/2026/poster/155293) · [作者来源](https://openreview.net/forum?id=6eYrXF03nQ)

- **问题 / 瓶颈** · 少量隐式分割 token 难表达空间对应。
- **核心创新 / 方法** · 多步对话细化提示，以同目标改写约束一致性，再筛关键帧传播掩码。
- **Baseline** · 分割 token 路线。
- **Benchmark** · 八个视频推理分割数据集。
- **关键结果 / 消融** · 作者报告优于对照；分项待核。
- **适用条件 / 局限** · 依赖提示和关键帧质量。

**可复用机制** · 为同一物体构造多种查询，检查空间定位一致性。

<a id="paper-155442"></a>

## Beyond Trajectory Matching: Reflow with Marginal Distribution Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/155442) · [作者来源](https://openreview.net/forum?id=5a2Wi08KqE)

- **问题 / 瓶颈** · 轨迹匹配损失相同的学生可能产生不同边际。
- **核心创新 / 方法** · 跟踪学生 ODE 的对数密度并用冻结教师分数计算正则。
- **Baseline** · 普通及分段 reflow。
- **Benchmark** · 少步生成基准与总变差理论界。
- **关键结果 / 消融** · 作者证明局部边际误差控制最终差异。
- **适用条件 / 局限** · 教师评分与密度计算开销待核。

**可复用机制** · 在固定采样预算下比较仅拟合轨迹与额外对齐边际。

<a id="paper-155755"></a>

## Beyond Uniform Detection: Adaptive Hallucination Detection for RAG Across Response Regimes

[官方论文页](https://neurips.cc/virtual/2026/poster/155755) · [作者来源](https://openreview.net/forum?id=3Bp2vd7ixA)

- **问题 / 瓶颈** · 短回答选错答案与长文逐步漂移需要不同观测。
- **核心创新 / 方法** · 短答用双向似然，长答跟踪隐藏状态中证据与内部知识方向。
- **Baseline** · 统一输出或表征检测。
- **Benchmark** · 多项长短文本 RAG 基准。
- **关键结果 / 消融** · 作者报告两种设置均有改善。
- **适用条件 / 局限** · 适用模型需能提供相应内部信号。

**可复用机制** · 比较统一门限与按回答长度和任务切换的校验。

<a id="paper-149242"></a>

## Beyond Unit-Circle Eigenvalues: Invariant Bases for Stable State Space Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/149242) · [作者来源](https://openreview.net/forum?id=rsTdJke80K)

- **问题 / 瓶颈** · 单位模只保证模式幅度，不保证任务守恒量。
- **核心创新 / 方法** · 对各向同性成对系统以图拉普拉斯特征基对角化。
- **Baseline** · 稳定 LRU、随机基、学习基及 PCA 基底。
- **Benchmark** · 视觉 N 体、长滚动和尺度外推。
- **关键结果 / 消融** · 动量漂移低于万分之一百分比；第999步约21.19 dB。
- **适用条件 / 局限** · 精确守恒依赖所设相互作用结构。

**可复用机制** · 谱稳定实验应直接测物理守恒量漂移。

<a id="paper-139396"></a>

## Beyond Visual Boundaries: Rethinking Scene Segmentation for Movie RAG

[官方论文页](https://neurips.cc/virtual/2026/poster/139396) · [作者来源](https://openreview.net/forum?id=TDlUSc9Koz)

- **问题 / 瓶颈** · 视觉显著转场不等于叙事边界。
- **核心创新 / 方法** · 按物理、角色和叙事变化标注，要求有效边界包含叙事变化。
- **Baseline** · 传统分场与均匀时间切分。
- **Benchmark** · NarraScene 与下游电影理解。
- **关键结果 / 消融** · 传统分场未超过均匀切分，叙事分段超过。
- **适用条件 / 局限** · 标注主观性和跨媒体迁移待核。

**可复用机制** · 检索单元按下游问题验证而非只测边界准确率。

<a id="paper-151533"></a>

## Beyond What Seems Necessary: Hidden Gains from Scaling Training-Time Reasoning Length under Outcome Supervision

[官方论文页](https://neurips.cc/virtual/2026/poster/151533) · [作者来源](https://openreview.net/forum?id=Zz2YaAr1JB)

- **问题 / 瓶颈** · 同分布表现饱和可能掩盖继续增长的稳健性。
- **核心创新 / 方法** · 用归纳偏置与正则抑制捷径解释更长训练推理的影响。
- **Baseline** · 不同循环数或 RL token 预算。
- **Benchmark** · 循环 Transformer 合成任务及数学、代码、跨表征任务。
- **关键结果 / 消融** · 作者观察到同分布饱和后分布外仍可改善。
- **适用条件 / 局限** · 结论针对结果监督和所测试条件。

**可复用机制** · 预算扫描联合记录域内和域外曲线。

<a id="paper-155672"></a>

## Beyond World-Frame Action Heads: Motion-Centric Action Frames for Vision-Language-Action Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155672) · [作者来源](https://openreview.net/forum?id=3qVJc7Gwrz)

- **问题 / 瓶颈** · 固定世界坐标直接预测难表达共用运动原语。
- **核心创新 / 方法** · 预测旋转，用共享原型合成局部动作并映回世界坐标。
- **Baseline** · 固定世界坐标动作头。
- **Benchmark** · 机器人操作及几何扰动。
- **关键结果 / 消融** · 作者报告表征更紧凑、扰动鲁棒性改善。
- **适用条件 / 局限** · 未见机构和几何域的迁移待核。

**可复用机制** · 固定演示与骨干对照局部原型和世界系直接回归。

<a id="paper-153204"></a>

## Bias, Measurement Error, and Double-Dipping: When Can GNN Convolutions Help Brain Connectome Prediction?

[官方论文页](https://neurips.cc/virtual/2026/poster/153204) · [作者来源](https://openreview.net/forum?id=N3upYxYotA)

- **问题 / 瓶颈** · 同一连接矩阵既作为特征也定义图，可放大相关误差。
- **核心创新 / 方法** · 以测量误差模型拆解平滑、估图误差及重复使用效应。
- **Baseline** · 无图模型、oracle 图及独立估计图。
- **Benchmark** · 模拟和真实 fMRI 连接预测。
- **关键结果 / 消融** · 仅目标在社区内平滑且序列长度合适时卷积有利。
- **适用条件 / 局限** · 理论基于线性渐近及社区模型。

**可复用机制** · 特征同时生成边时，用独立子样本估图做诊断。

<a id="paper-152470"></a>

## Bias-Variance Optimized Preference Optimization for Large Reasoning Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152470) · [作者来源](https://openreview.net/forum?id=SqjlMwxRLI)

- **问题 / 瓶颈** · 单条随机轨迹近似答案级目标导致高梯度方差。
- **核心创新 / 方法** · 在固定题目和答案下构造复合估计量，分析条件均方误差最优混合。
- **Baseline** · 单轨迹偏好优化。
- **Benchmark** · AlpacaEval 2、Arena-Hard 及六个数学任务。
- **关键结果 / 消融** · 作者报告训练梯度方差降低且总体保持数学推理。
- **适用条件 / 局限** · 条件方差结果不覆盖所有随机成分。

**可复用机制** · 配对跟踪梯度方差与答案质量，比较单轨迹和混合分支。

<a id="paper-154292"></a>

## Bidirectional Sparse Attention for Faster Video Diffusion Training

[官方论文页](https://neurips.cc/virtual/2026/poster/154292) · [作者来源](https://openreview.net/forum?id=Es6mFi84XA)

- **问题 / 瓶颈** · 视频全注意力代价平方增长
- **核心创新 / 方法** · 剪时空冗余查询，仅选全局高相关键值并调整阈值
- **Baseline** · 全注意力 DiT
- **Benchmark** · 长视频训练，比较 FLOPs、速度和生成质量
- **关键结果 / 消融** · 注意力训练最高快 17.79 倍，FLOPs 最多降至二十分之一
- **适用条件 / 局限** · 端到端训练加速待核

**可复用机制** · 匹配生成质量分别测两个方向的剪枝收益

<a id="paper-149009"></a>

## Bifurcation Models: Learning Set-Valued Solution Maps with Weight-Tied Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/149009) · [作者来源](https://openreview.net/forum?id=tVZohLsVHC)

- **问题 / 瓶颈** · 单一标签可能引入不连续选择器
- **核心创新 / 方法** · 权重共享动力系统以不同初态收敛到不同稳定平衡
- **Baseline** · 单分支监督
- **Benchmark** · 受挫 Ising 与 Allen–Cahn
- **关键结果 / 消融** · 无分支标签可找多个平衡；多样性与精度存在权衡
- **适用条件 / 局限** · 分支须满足理论正则性；多样性不会自动出现

**可复用机制** · 用多初态测有效解覆盖及每解误差

<a id="paper-156775"></a>

## Bigger Isn't Always Memorizing: Early Stopping Overparameterized Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/156775) · [作者来源](https://neurips.cc/virtual/2026/poster/156775)

- **问题 / 瓶颈** · 过参数化扩散先泛化后记忆
- **核心创新 / 方法** · 分析低噪声拟合时间尺度，并用随机文法验证
- **Baseline** · 训练时间与数据量不同的扩散模型
- **Benchmark** · 图像、语言扩散及随机上下文无关文法
- **关键结果 / 消融** · 作者观察到记忆时间与数据集规模成比例
- **适用条件 / 局限** · 经验比例常数及适用分布待核

**可复用机制** · 随数据规模同步扫描训练步数并分别评估泛化和复制

<a id="paper-155173"></a>

## Bilevel Optimization of Synthetic Trajectories for Multi-Turn LLM Fine-Tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/155173) · [作者来源](https://openreview.net/forum?id=7kLOx2KkF4)

- **问题 / 瓶颈** · 等权合成轨迹可能放大任务偏移
- **核心创新 / 方法** · 内层用重加权轨迹训练，外层学习连续权重
- **Baseline** · 等权及多种比较；名称待核
- **Benchmark** · 多轮离线强化学习任务
- **关键结果 / 消融** · 作者报告胜过对照，并给出多样性、偏移和有效样本量的权衡
- **适用条件 / 局限** · 依赖代表真实需求的留出任务

**可复用机制** · 评估加权时同步记录有效样本数和目标域得分

<a id="paper-149557"></a>

## Bilinear Matching Bandits

[官方论文页](https://neurips.cc/virtual/2026/poster/149557) · [作者来源](https://openreview.net/forum?id=pDNMIRZc3y)

- **问题 / 瓶颈** · Kronecker 展平带来维数代价
- **核心创新 / 方法** · 把消除与分数匹配多面体上的分行正则采样结合
- **Baseline** · Kronecker 线性化半赌博机
- **Benchmark** · 半反馈匹配的遗憾界与数值实验
- **关键结果 / 消融** · 领先维数因子从 d1d2 改为 d2√d1，大物品数时下界匹配
- **适用条件 / 局限** · 依赖双线性收益及部分反馈设定

**可复用机制** · 在线分配前检验结构先验能否降低探索维数

<a id="paper-149418"></a>

## BiLoCo: Binary Low-Rank Corrections for LLM FP4 Decode

[官方论文页](https://neurips.cc/virtual/2026/poster/149418) · [作者来源](https://openreview.net/forum?id=qC1Ogzw65q)

- **问题 / 瓶颈** · 高精度残差占存储并争抢 Tensor Core
- **核心创新 / 方法** · 二值存储左右因子，CUDA Core 执行加减修正
- **Baseline** · 等存储 SVDQuant 和纯 FP4
- **Benchmark** · 4–32B 模型量化与 B200 解码
- **关键结果 / 消融** · 每秩存储降至 BF16 残差的十六分之一，等存储下匹配或超过 SVDQuant。
- **适用条件 / 局限** · 依赖硬件并发和最终输出合并开销

**可复用机制** · 比较固定存储下的误差与端到端延迟

<a id="paper-149098"></a>

## Binding Multiple Modalities via Multimodal Wasserstein Barycenter

[官方论文页](https://neurips.cc/virtual/2026/poster/149098) · [作者来源](https://openreview.net/forum?id=swVrjlNX4Q)

- **问题 / 瓶颈** · 指定单一锚点会偏向该模态
- **核心创新 / 方法** · 计算 Wasserstein 重心并以重心单纯形体积构造联合目标
- **Baseline** · 固定模态锚定方法
- **Benchmark** · 文本视频音频检索、分类、视频问答及生成
- **关键结果 / 消融** · 作者报告对缺失模态仍稳健，并可扩至三种以上
- **适用条件 / 局限** · 重心计算代价及配对要求待核

**可复用机制** · 比较语义锚点与分布重心在模态缺失时的表现

<a id="paper-148298"></a>

## Binding Visual Features Point by Point

[官方论文页](https://neurips.cc/virtual/2026/poster/148298) · [作者来源](https://openreview.net/forum?id=yu8ajcYUw2)

- **问题 / 瓶颈** · 多物体属性容易互串
- **核心创新 / 方法** · 学习文本坐标指向，以机制分析识别内部视觉搜索并微调迁移
- **Baseline** · 无指向的多模态推理
- **Benchmark** · 多物体理解与组合泛化任务
- **关键结果 / 消融** · 作者观察到指向诱导视觉搜索，迁移后减少绑定错误
- **适用条件 / 局限** · 相关性与因果消融细节待核

**可复用机制** · 保持任务与图像不变，有无坐标中间表示分别测错绑率

<a id="paper-152242"></a>

## BIRD-RL: Scaling Agentic Reinforcement Learning over Stateful Data-Centric Environments

[官方论文页](https://neurips.cc/virtual/2026/poster/152242) · [作者来源](https://openreview.net/forum?id=UWzAnfVNIa)

- **问题 / 瓶颈** · 轨迹状态串扰会污染策略更新
- **核心创新 / 方法** · 四阶段课程配合轨迹级持久执行隔离
- **Baseline** · Claude Opus 4.6 Agent
- **Benchmark** · BIRD-CRITIC-SQLite 成功率
- **关键结果 / 消融** · 空间效率12.8倍，7B与14B成功率44.4%和48%
- **适用条件 / 局限** · 验证集中于数据库任务

**可复用机制** · 在可变状态环境中把副本复用和轨迹隔离同时测量

<a id="paper-153956"></a>

## BitDance: Scaling Autoregressive Generative Models with Binary Tokens

[官方论文页](https://neurips.cc/virtual/2026/poster/153956) · [作者来源](https://openreview.net/forum?id=HI2nlULbg7)

- **问题 / 瓶颈** · 高容量码本无法直接用普通分类器枚举
- **核心创新 / 方法** · 二值扩散头与并行图块解码
- **Baseline** · 并行自回归生成器
- **Benchmark** · ImageNet 256图像生成FID和速度
- **关键结果 / 消融** · FID 1.24，260M模型相较所比大模型加速8.7倍
- **适用条件 / 局限** · 速度依赖硬件及生成配置

**可复用机制** · 高维离散码可用分量生成替代显式类别枚举

<a id="paper-154757"></a>

## BitMTP: When Multi-Token Prediction Meets Low-Bit Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154757) · [作者来源](https://openreview.net/forum?id=BBFcLluA5v)

- **问题 / 瓶颈** · 低比特算术加速后，前缀处理开销成为瓶颈
- **核心创新 / 方法** · 以接受前缀统一KV缓存与图调度
- **Baseline** · BitNet b1.58-2B-SFT
- **Benchmark** · 2B解码吞吐与预测精度
- **关键结果 / 消融** · 峰值964.2 token/s，吞吐2.64倍
- **适用条件 / 局限** · 峰值取决于硬件及前缀接受分布

**可复用机制** · 组合压缩和多token预测时先做端到端开销分解

<a id="paper-150556"></a>

## Bits Beat Tokens: A Regret Rate Distortion Theory for Large Language Model Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/150556) · [作者来源](https://openreview.net/forum?id=hGYPDaFTPP)

- **问题 / 瓶颈** · 长上下文未必携带足够行动证据
- **核心创新 / 方法** · 以贝叶斯遗憾定义率失真下界
- **Baseline** · 同信息率比较与思维链对照
- **Benchmark** · 441组单步工具选择，三模型三数据集
- **关键结果 / 消融** · 所有设置符合理论下界
- **适用条件 / 局限** · 实证限于单步平衡分类代理

**可复用机制** · 固定任务遗憾目标后比较检索策略保留的决策信息

<a id="paper-150476"></a>

## BitShift-RoPE: Zero-FLOP Relative Positional Encoding for Spiking Neural Network Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/150476) · [作者来源](https://openreview.net/forum?id=hlVtSHax4T)

- **问题 / 瓶颈** · 浮点旋转破坏二值稀疏计算
- **核心创新 / 方法** · 把RoPE频率映射成循环移位
- **Baseline** · 原始Spikformer
- **Benchmark** · 时序预测、文本及图像分类
- **关键结果 / 消融** · 图像准确率84.17%，报告能耗0.216mJ每样本
- **适用条件 / 局限** · 依赖位移和内存寻址实现

**可复用机制** · 硬件受限时按实际内存操作测编码能耗

<a id="paper-155774"></a>

## Black-Box Followers, White-Box Leaders: Partial Zeroth-Order Methods for MPECs

[官方论文页](https://neurips.cc/virtual/2026/poster/155774) · [作者来源](https://openreview.net/forum?id=317Kb0r0vX)

- **问题 / 瓶颈** · 全黑盒估计浪费已知目标导数
- **核心创新 / 方法** · 组合目标的精确偏导与响应雅可比估计
- **Baseline** · 整体黑盒零阶方法
- **Benchmark** · 均衡约束优化及路网定价
- **关键结果 / 消融** · 作者证明方差上界降低并报告收敛改善
- **适用条件 / 局限** · 依赖目标偏导和可查询响应

**可复用机制** · 复合问题中按可访问导数拆分估计器

<a id="paper-151082"></a>

## Black-Box Uncertainty Quantification for Large Language Models via Ensemble-of-Ensembles

[官方论文页](https://neurips.cc/virtual/2026/poster/151082) · [作者来源](https://openreview.net/forum?id=d6Lh3e1MsW)

- **问题 / 瓶颈** · 单一一致性分数混淆问题歧义与知识缺口
- **核心创新 / 方法** · 嵌套采样与嵌套提示，按全协方差分解变异
- **Baseline** · 强白盒与一致性方法
- **Benchmark** · 五个短问答基准，含AmbigQA与Natural Questions
- **关键结果 / 消融** · 作者报告可区分两类失效并与白盒可比
- **适用条件 / 局限** · 语义保留质量影响估计

**可复用机制** · 分别按采样与提示变化比较澄清和复核信号

<a id="paper-152234"></a>

## BLADE: Scalable Bi-level Adaptive Data Selection for LLM Training

[官方论文页](https://neurips.cc/virtual/2026/poster/152234) · [作者来源](https://openreview.net/forum?id=UZM2vsjS66)

- **问题 / 瓶颈** · 固定参考与训练中的代理逐渐失配
- **核心创新 / 方法** · 用惩罚单层目标替代双层优化，以随机块坐标方法选批次
- **Baseline** · 影响函数与固定参考超额损失
- **Benchmark** · 语言模型数据选择，具体基准待核
- **关键结果 / 消融** · 作者报告超过所比基线并证明一阶收敛
- **适用条件 / 局限** · 代理对最终模型的代表性待核

**可复用机制** · 在同训练预算下比较动态和静态参考的选样变化

<a id="paper-155644"></a>

## BLANP: Memory-Efficient Backpropagation-Free Local Training via Antithetic Node Perturbation

[官方论文页](https://neurips.cc/virtual/2026/poster/155644) · [作者来源](https://openreview.net/forum?id=446EXQoY2A)

- **问题 / 瓶颈** · 跨层反传需要保存全网络激活
- **核心创新 / 方法** · 用正负节点扰动与冻结滑动平均评价器做局部更新
- **Baseline** · 反向传播及已有局部学习方法
- **Benchmark** · MNIST、Fashion-MNIST、CIFAR-10
- **关键结果 / 消融** · 精确局部版本在CIFAR-10比最强局部对照高2.40%，距反传3.90%
- **适用条件 / 局限** · 两次前向的成本与深模型表现待核

**可复用机制** · 同时测局部更新的激活峰值与准确率

<a id="paper-155225"></a>

## BLARM: Animating 3D Objects from Video via Blending LAtent Rigid Motion Primitives

[官方论文页](https://neurips.cc/virtual/2026/poster/155225) · [作者来源](https://openreview.net/forum?id=7KoU7zMcDg)

- **问题 / 瓶颈** · 直接估计全部顶点运动难保时间一致
- **核心创新 / 方法** · 学时变刚体和时不变顶点混合权重
- **Baseline** · 显式骨架和顶点回归路线，实验对照待核
- **Benchmark** · 单目视频驱动网格动画，数据集及指标待核
- **关键结果 / 消融** · 作者报告动画稳定且运动结构紧凑
- **适用条件 / 局限** · 需要静态网格；大幅非刚性变形适用性待核

**可复用机制** · 用时不变混合权重约束低维部件运动

<a id="paper-151100"></a>

## BlenderFORGE: Framework for Optimizing Reactive 3D-Graphics Editing Ability of MLLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/151100) · [作者来源](https://openreview.net/forum?id=czK5BBdtMP)

- **问题 / 瓶颈** · 仅检查代码或视觉结果难确认局部编辑是否正确
- **核心创新 / 方法** · 隔离环境确定性执行并导出结构化状态用于多轮训练
- **Baseline** · 基础Qwen3-VL-8B及零样本闭源模型
- **Benchmark** · 位置、形变键、灯光和材质四类Blender任务
- **关键结果 / 消融** · 作者报告较底座改善并与部分闭源方法可比
- **适用条件 / 局限** · 依赖状态可直接读取，开放式审美任务未验证

**可复用机制** · 用目标状态和非目标属性保持分别做验收

<a id="paper-150222"></a>

## Blind-Window Forecasting: Real-Time Benchmarking and Multimodal Reconstruction for Tropical Cyclones

[官方论文页](https://neurips.cc/virtual/2026/poster/150222) · [作者来源](https://openreview.net/forum?id=jrRFzggOc0)

- **问题 / 瓶颈** · 最新再分析场在发报时可能不存在
- **核心创新 / 方法** · 以延迟再分析和即时遥感重建预报所需的风暴状态
- **Baseline** · 理想即时分析与仅延迟再分析
- **Benchmark** · 1980–2023热带气旋，测路径和强度
- **关键结果 / 消融** · 作者报告两项均优于延迟对照
- **适用条件 / 局限** · 历史观测覆盖和延迟策略影响结论

**可复用机制** · 用即时与延迟数据双对照量化事后输入优势

<a id="paper-148271"></a>

## Blocked Gibbs meets Diffusion Transformers: Unsupervised Learning for Constraint Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/148271) · [作者来源](https://openreview.net/forum?id=z5oDNb2lwJ)

- **问题 / 瓶颈** · 全局渐进降噪不利于同时改动相关变量
- **核心创新 / 方法** · 在扩散 Transformer 中迭代块高斯重采样并退火块大小
- **Baseline** · 标准联合降噪及既有求解器
- **Benchmark** · 数独、图着色、最大独立集、最大割
- **关键结果 / 消融** · 作者报告持平或优于现有方法，幅度待核
- **适用条件 / 局限** · 依赖变量分块与任务约束

**可复用机制** · 比较全局小步和块级大步对可行率的影响

<a id="paper-152355"></a>

## Block-OBS-GS: Exact Per-Block Joint Brain Surgery with Gauss–Seidel Refinement for LLM Pruning

[官方论文页](https://neurips.cc/virtual/2026/poster/152355) · [作者来源](https://openreview.net/forum?id=TgdviE0ING)

- **问题 / 瓶颈** · 逐列近似忽略权重耦合，直接联合求解昂贵
- **核心创新 / 方法** · 分行对阻尼 Hessian 做 Cholesky 分解求块内解，再做一次 Gauss–Seidel
- **Baseline** · SparseGPT、Wanda
- **Benchmark** · Llama-3 和 Qwen-3，WikiText-2、常识任务、MMLU 和结构化稀疏
- **关键结果 / 消融** · Llama-3.1-8B 在 87.5% 稀疏度下困惑度较 SparseGPT 降 47%
- **适用条件 / 局限** · 保证针对固定掩码和重建目标

**可复用机制** · 在相同掩码下比较局部精确求解与跨块更新的收益

<a id="paper-139480"></a>

## Block-R1: Rethinking the Role of Block Size in Multi-domain Reinforcement Learning for Diffusion Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139480) · [作者来源](https://openreview.net/forum?id=NQxRm8kEK2)

- **问题 / 瓶颈** · 不同领域的并行粒度偏好可能冲突
- **核心创新 / 方法** · 标注样本的最优训练块大小并定义冲突分数，用于分配 rollout
- **Baseline** · 统一块大小等对照待全文核实
- **Benchmark** · Block-R1 上 13 数据集、7 种 RL 算法及多个骨干
- **关键结果 / 消融** · 摘要报告广泛评测，具体收益待核
- **适用条件 / 局限** · 选择块大小的搜索开销和迁移边界待核

**可复用机制** · 将训练粒度当作与数据领域交互的变量，在等预算下对照统一分配

<a id="paper-155122"></a>

## Block Sparse Flash Attention

[官方论文页](https://neurips.cc/virtual/2026/poster/155122) · [作者来源](https://openreview.net/forum?id=8GItn9bqi9)

- **问题 / 瓶颈** · 先验筛选可能误删重要上下文
- **核心创新 / 方法** · 一次校准各层各头分数阈值，筛选价值块并用 CUDA 实现
- **Baseline** · SpargeAttention、MInference、FlexPrefill、XAttention、BLASST
- **Benchmark** · LongBench、针检索，Llama 与 Qwen，A6000 和 H100
- **关键结果 / 消融** · Llama-3.1-8B 端到端最高 1.13 倍与 1.24 倍，准确率分别降 1.1% 与 1%
- **适用条件 / 局限** · 阈值依赖校准分布和硬件

**可复用机制** · 稀疏内核同时报告端到端时延、检索准确率与块跳过比例

<a id="paper-152314"></a>

## Block Sphere Vector Quantization

[官方论文页](https://neurips.cc/virtual/2026/poster/152314) · [作者来源](https://openreview.net/forum?id=U13XD8SxhN)

- **问题 / 瓶颈** · 不同量化器在不同失真尺度下难直接比较
- **核心创新 / 方法** · 统一理论对照，在旋转后的分块球面上量化以保几何
- **Baseline** · EDEN、RabitQ、TurboQuant
- **Benchmark** · 真实嵌入及重建 MSE、内积误差和高概率界
- **关键结果 / 消融** · 理论和实验支持降低期望失真，各基线优势依指标而异
- **适用条件 / 局限** · 高概率与期望改进不可互换

**可复用机制** · 用任务对应的失真量选量化器，并分别比较尾部误差

<a id="paper-152092"></a>

## BMAttn: Block-Aligned Mixed-Precision Attention Quantization for LLM Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/152092) · [作者来源](https://openreview.net/forum?id=VZRJp36FMB)

- **问题 / 瓶颈** · 逐 token 自适应的访存开销可能抵消压缩收益
- **核心创新 / 方法** · 用仿射窗口按序列长度调整高低精度及稀疏区块，以显著性校准
- **Baseline** · 均匀压缩和细粒度自适应，具名基线待核
- **Benchmark** · 长上下文任务，细项待核
- **关键结果 / 消融** · 报告 3.3 倍加速且准确率损失小，部分设置达 5 倍
- **适用条件 / 局限** · 速度依赖内核、显卡和长度

**可复用机制** · 在相同准确率下对照按 token 与按块精度策略的端到端耗时

<a id="paper-138938"></a>

## BO-Arena: An Evolving Benchmark for High-Dimensional Bayesian Optimisation

[官方论文页](https://neurips.cc/virtual/2026/poster/138938) · [作者来源](https://openreview.net/forum?id=vGjqfKbR8v)

- **问题 / 瓶颈** · 漏比强基线或错误实现会扭曲排序
- **核心创新 / 方法** · 提供可扩展规范实现并在统一平台复评
- **Baseline** · 简单高斯过程及多种高维 BO 方法
- **Benchmark** · 高维贝叶斯优化，含大量观测设置
- **关键结果 / 消融** · 作者质疑复杂方法已稳定超越简单 GP，具名数值待核
- **适用条件 / 局限** · 依赖测试函数与评估预算

**可复用机制** · 发布优化结果前复用标准基线并扫观测预算

<a id="paper-155059"></a>

## BONSAI: Bayesian Optimization with Natural Simplicity and Interpretability

[官方论文页](https://neurips.cc/virtual/2026/poster/155059) · [作者来源](https://openreview.net/forum?id=8ltIqoRvDz)

- **问题 / 瓶颈** · 普通 BO 常无必要地改动低影响参数
- **核心创新 / 方法** · 在采集值约束下删去低影响偏离，兼容 EI 和 GP-UCB
- **Baseline** · 标准 BO、IR、ER、SEBO
- **Benchmark** · 真实应用及理论遗憾、非默认参数数和耗时
- **关键结果 / 消融** · 平均候选生成成本约标准 BO 的 1.5 倍，对照稀疏方法约 7 至 34 倍
- **适用条件 / 局限** · 精确恢复相关坐标需已知 ARD 长度尺度

**可复用机制** · 对有成熟默认值的调参同时记录性能和实际改动数

<a id="paper-149759"></a>

## Boosting Inference with Guided Reasoning: Stochastic Exploration for Recursive Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149759) · [作者来源](https://openreview.net/forum?id=nZD0FHMUmR)

- **问题 / 瓶颈** · 确定性递归只探索一条潜在轨迹
- **核心创新 / 方法** · 加入状态扰动并用现有停止头重加权，检查局部稳定和引导对齐
- **Baseline** · 确定性递归
- **Benchmark** · Sudoku-Extreme 与 Maze-Hard，测精确解题和诊断
- **关键结果 / 消融** · 数独精确解从 85.9% 到 98.0%，迷宫诊断提示引导失配
- **适用条件 / 局限** · 内部引导不可靠时扩搜索未必有益

**可复用机制** · 增加推理计算前先在验证集检查早停信号能否排序候选

<a id="paper-149143"></a>

## Boosting Multiagent Reinforcement Learning at High Replay Ratios with Ensemble Reset

[官方论文页](https://neurips.cc/virtual/2026/poster/149143) · [作者来源](https://openreview.net/forum?id=sW2PazNAB1)

- **问题 / 瓶颈** · 频繁更新导致集中式 Q 网络容量下降
- **核心创新 / 方法** · 使用多 Q 网络周期重置，通过平移不变性多样化经验
- **Baseline** · 多种 MARL 算法，具名对照待核
- **Benchmark** · SMAC、MPE、SMACv2，测高回放比下的环境步数与表现
- **关键结果 / 消融** · 作者报告多算法稳定改善，数值待核
- **适用条件 / 局限** · 依赖多智能体场景的平移不变性

**可复用机制** · 提高回放比时同步测休眠比例，用同环境步数对照单网络与周期重置集成

<a id="paper-154959"></a>

## Boosting Off-Policy RLVR with Data-Centric Replay

[官方论文页](https://neurips.cc/virtual/2026/poster/154959) · [作者来源](https://openreview.net/forum?id=9dxvGd7Shr)

- **问题 / 瓶颈** · 旧轨迹的大量信号会被稳定性机制舍弃
- **核心创新 / 方法** · STAR 选择低陈旧且高质量轨迹
- **Baseline** · 在线及离线策略训练
- **Benchmark** · 数学推理与代码生成
- **关键结果 / 消融** · 相对提升最高19%，约13%采样数据并快5–6倍
- **适用条件 / 局限** · 陈旧度阈值与成本待核

**可复用机制** · 固定训练算法，分桶比较不同陈旧度的有效更新量

<a id="paper-154872"></a>

## Boost Reasoning Evolution via Responsive Rollout Difficulty Manipulation

[官方论文页](https://neurips.cc/virtual/2026/poster/154872) · [作者来源](https://openreview.net/forum?id=AG7LEXWKt1)

- **问题 / 瓶颈** · 太难缺少有效探索，太易缺少学习信号
- **核心创新 / 方法** · 多轮采样拟合提示长度与成功率，再选下一轮提示
- **Baseline** · GRPO、SFT及既有提示辅助方法
- **Benchmark** · 六个数学推理基准
- **关键结果 / 消融** · 均值分别比三类对照高10.0、8.4及3.8点
- **适用条件 / 局限** · 需要参考解与多轮采样

**可复用机制** · 用实例级成功率调整辅助强度而非统一提示长度

<a id="paper-151994"></a>

## BootstrapAgent: Turning Repository Setup into Reusable Agent Knowledge

[官方论文页](https://neurips.cc/virtual/2026/poster/151994) · [作者来源](https://openreview.net/forum?id=WIItfKBPZm)

- **问题 / 瓶颈** · 仓库配置试错难跨会话复用
- **核心创新 / 方法** · 提取CI证据、生成契约、用容器冷重放验证局部修补
- **Baseline** · 常规仓库配置代理
- **Benchmark** · 三个仓库配置基准
- **关键结果 / 消融** · 报告成功率92.9%，下游token减少25.9%
- **适用条件 / 局限** · 依赖可重放环境和明确检查

**可复用机制** · 允许热修复加速，但用干净环境验收可复用配置

<a id="paper-155139"></a>

## Bootstrapped Bipartite Actor-Critic for Diffusion RL

[官方论文页](https://neurips.cc/virtual/2026/poster/155139) · [作者来源](https://openreview.net/forum?id=85aIcxYmr9)

- **问题 / 瓶颈** · 只建模正样本浪费坏动作信息
- **核心创新 / 方法** · 用Bradley–Terry式排序引入负样本，并按Q差软门控
- **Baseline** · 无模型与生成式策略
- **Benchmark** · 六个MuJoCo和四个H1Bench任务
- **关键结果 / 消融** · 摘要报告各环境均改善
- **适用条件 / 局限** · 依赖Q估计可用于排序

**可复用机制** · 对采样动作构造优劣对并隔离门控权重贡献

<a id="paper-139737"></a>

## Bottleneck Benchmark: Sequence Compression Under Controlled Difficulty and Fixed Latent Size

[官方论文页](https://neurips.cc/virtual/2026/poster/139737) · [作者来源](https://openreview.net/forum?id=7MkLtoyPdq)

- **问题 / 瓶颈** · 架构比较易混入潜容量差别
- **核心创新 / 方法** · 仅允许固定潜表示传递信息并分别改变长度词表与噪声
- **Baseline** · BiLSTM、Transformer和双向SSM
- **Benchmark** · 复制、排序和集合任务
- **关键结果 / 消融** · 差异随噪声和长度变化
- **适用条件 / 局限** · 合成任务向真实文本迁移待核

**可复用机制** · 固定压缩预算后按扰动类型分开比较重建

<a id="paper-155598"></a>

## Boundary-Induced Forgetting in Large Language Model Tool Chains: Measuring Field-Routing Failures

[官方论文页](https://neurips.cc/virtual/2026/poster/155598) · [作者来源](https://openreview.net/forum?id=4NNekFkfV8)

- **问题 / 瓶颈** · 上下文仍含值也可能没绑到后续参数
- **核心创新 / 方法** · 构建字段路由图并提醒下一步仍需字段
- **Baseline** · 基础GPT-4o与自预测检索
- **Benchmark** · ToolSandbox及τ-bench共357题
- **关键结果 / 消融** · 单到五次边界利用率降31.4点，提醒使成功率增13.4点
- **适用条件 / 局限** · 依赖字段提取且其他工具协议待测

**可复用机制** · 同时记录字段使用与最终成功，并按边界数分桶

<a id="paper-149689"></a>

## Boundary Mass in Feature Space as a Label-Budget Diagnostic for Representations

[官方论文页](https://neurips.cc/virtual/2026/poster/149689) · [作者来源](https://openreview.net/forum?id=oAolQpqUNY)

- **问题 / 瓶颈** · 全局相似度难刻画下游分类歧义
- **核心创新 / 方法** · 在线性探针留出集统计薄边界带质量并按类别平衡归一化
- **Baseline** · 全局迁移评分及法向切向变换
- **Benchmark** · CIFAR-100与Tiny-ImageNet
- **关键结果 / 消融** · 代理损失在匹配准确率下降低复杂度16–36%
- **适用条件 / 局限** · 依赖线性边界及标签预算网格

**可复用机制** · 候选表征近似同分时比较探针边界附近的样本质量

<a id="paper-149342"></a>

## Bound-Conditioned Latent Inference for Progressive Image Compression

[官方论文页](https://neurips.cc/virtual/2026/poster/149342) · [作者来源](https://openreview.net/forum?id=qoLGM98t8z)

- **问题 / 瓶颈** · 概率建模忽略前缀定义的可行区间
- **核心创新 / 方法** · 用区间中心宽度及超先验同时更新熵模型和重建估计
- **Baseline** · DPICT与CTC
- **Benchmark** · Kodak、CLIC及JPEG-AI
- **关键结果 / 消融** · Kodak BD-rate分别降17.80%和7.98%
- **适用条件 / 局限** · 需要可从前缀恢复的单调区间

**可复用机制** · 让渐进解码明确利用部分观测规定的潜变量范围

<a id="paper-148822"></a>

## Bounding Global and Local Compression Error of Signal Parameterizations

[官方论文页](https://neurips.cc/virtual/2026/poster/148822) · [作者来源](https://openreview.net/forum?id=ut4H4goukL)

- **问题 / 瓶颈** · 没有真值时难判断有限表示的重建质量
- **核心创新 / 方法** · 在满足性质的参数化族中缩放不同级别预测差异
- **Baseline** · 以真值误差曲线对照估计
- **Benchmark** · 信号直接拟合、辐射场及MRI逆问题
- **关键结果 / 消融** · 报告跟踪全局误差且局部热图有信息
- **适用条件 / 局限** · 理论依赖表示族满足指定性质

**可复用机制** · 在选表示大小时先检查多压缩级预测是否提供稳定误差代理

<a id="paper-153578"></a>

## Bounds on Extrapolation across Phase Transitions with Generalized Regression

[官方论文页](https://neurips.cc/virtual/2026/poster/153578) · [作者来源](https://openreview.net/forum?id=KMhpQBznmA)

- **问题 / 瓶颈** · 单相训练误差不足以说明跨相预测表现
- **核心创新 / 方法** · 界定外推区和训练区均方误差比的最坏上界
- **Baseline** · 多项式、核回归和常规神经网络
- **Benchmark** · Heisenberg模型与超导ARPES数据
- **关键结果 / 消融** · 多项式和核法恢复相结构，普通神经网络失败
- **适用条件 / 局限** · 证据限分析的两种系统

**可复用机制** · 用训练区与外推区的误差倍率而非训练损失比较候选函数族

<a id="paper-149729"></a>

## BQ-LoRA: Binary-Quantized Low-Rank Adapters as Implicit Regularizers for Parameter-Efficient Fine-Tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/149729) · [作者来源](https://openreview.net/forum?id=nnhvsIx2Kl)

- **问题 / 瓶颈** · 适配器存储限制多任务部署
- **核心创新 / 方法** · 每层学习缩放并用缩放直通估计训练二值低秩参数
- **Baseline** · QLoRA与LoftQ
- **Benchmark** · 多尺度Qwen2.5及LLaMA-2
- **关键结果 / 消融** · 存储约少14–16倍且表现相当或更优
- **适用条件 / 局限** · 真实收益依赖内核与请求分布

**可复用机制** · 同时测适配器精度、缓存命中和服务延时

<a id="paper-150021"></a>

## BRACE: Bipolar Reference-Aware Calibration and Estimation for Incomplete Multimodal Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/150021) · [作者来源](https://openreview.net/forum?id=lLcmkgW4CK)

- **问题 / 瓶颈** · 缺失模态时粗状态可能不能确定残差符号
- **核心创新 / 方法** · 检索更高和更低标签参考，按有序差异门控状态修正
- **Baseline** · HME及缺失模态方法
- **Benchmark** · 四个情感与虚假信息检测基准
- **关键结果 / 消融** · 固定缺失下Acc-2最高比HME高7.4点
- **适用条件 / 局限** · 标签需可排序且参考库须覆盖测试状态

**可复用机制** · 为不完整输入明确区分基础估计与方向校正

<a id="paper-148431"></a>

## BRAVO: Bridge Matching for Autoregressive Video Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/148431) · [作者来源](https://openreview.net/forum?id=xsOb1nnuLg)

- **问题 / 瓶颈** · 逐帧从噪声复原会重复重建布局。
- **核心创新 / 方法** · 相邻真帧构造布朗桥，因果历史条件下训练并递归采样。
- **Baseline** · 噪声到数据的逐帧基线与更大模型。
- **Benchmark** · 多个图生视频数据集；指标待核。
- **关键结果 / 消融** · 报告超出噪声到数据基线。
- **适用条件 / 局限** · 递归误差传播边界待核。

**可复用机制** · 固定历史缓存，对照上一帧桥与重启噪声。

<a id="paper-150356"></a>

## Breaking $\textit{Winner-Takes-All}$: Cooperative Policy Optimization Improves Diverse LLM Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/150356) · [作者来源](https://openreview.net/forum?id=iiwmhPUMvv)

- **问题 / 瓶颈** · 组内只按单个答案正确性竞争会压缩探索。
- **核心创新 / 方法** · 在正确性加权语义嵌入上计算行列式体积，按平均边际贡献分配优势。
- **Baseline** · GRPO 和多样性基线。
- **Benchmark** · 多个推理基准，测准确率与多样性。
- **关键结果 / 消融** · 作者报告两项均改善，幅度待核。
- **适用条件 / 局限** · 依赖可信验证器及语义距离。

**可复用机制** · 固定采样预算比较单条奖励与覆盖边际奖励。

<a id="paper-153915"></a>

## Breaking Adversarial Transferability in Fine-Tuned Speech Recognition

[官方论文页](https://neurips.cc/virtual/2026/poster/153915) · [作者来源](https://openreview.net/forum?id=Hk5S6s2xN9)

- **问题 / 瓶颈** · 接口受限不能保证鲁棒。
- **核心创新 / 方法** · 将鲁棒微调与隐表示敏感度正则结合。
- **Baseline** · 普通微调 ASR。
- **Benchmark** · 三种语言、四个模型，测受扰 WER。
- **关键结果 / 消融** · 作者报告 WER 从 92.6 降至 27.8。
- **适用条件 / 局限** · 特定威胁测试结果不代表所有场景。

**可复用机制** · 每次更换底座后重新验收受扰与正常识别性能。

<a id="paper-148208"></a>

## Breaking BAD: Heterogeneous Byzantine-Robust Federated Learning via Gather and Scatter Scores

[官方论文页](https://neurips.cc/virtual/2026/poster/148208) · [作者来源](https://openreview.net/forum?id=zYNKoIyYhj)

- **问题 / 瓶颈** · 异质正常更新会削弱单一离群判定。
- **核心创新 / 方法** · 用聚集与离散分数辅助选择可信聚合，并给出收敛保证。
- **Baseline** · 现有 Byzantine 鲁棒聚合。
- **Benchmark** · FEMNIST、Shakespeare、CIFAR-10。
- **关键结果 / 消融** · 报告防御下保留较高准确率，幅度待核。
- **适用条件 / 局限** · 正常群组也可能聚集，需校准。

**可复用机制** · 把跨客户端异质性作为鲁棒聚合测试变量。

<a id="paper-154130"></a>

## Breaking Curse of Dimensionality for Mutual Information Estimation with Vine Copulas

[官方论文页](https://neurips.cc/virtual/2026/poster/154130) · [作者来源](https://openreview.net/forum?id=G2wwtzIvKy)

- **问题 / 瓶颈** · 非参数联合密度估计在高维困难。
- **核心创新 / 方法** · 用藤 copula 的成对分解估计互信息。
- **Baseline** · 神经互信息估计器。
- **Benchmark** · 已知真值的多种维度、数据类型和依赖结构。
- **关键结果 / 消融** · 报告误差与耗时折衷改善。
- **适用条件 / 局限** · 结论依赖分解与估计条件。

**可复用机制** · 在已知互信息的合成任务单独扫描维度和依赖结构。

<a id="paper-155451"></a>

## Breaking Information Islands in Sparse Tuning via Small-World Connectivity

[官方论文页](https://neurips.cc/virtual/2026/poster/155451) · [作者来源](https://openreview.net/forum?id=5VR2N1lVBd)

- **问题 / 瓶颈** · 稀疏参数可形成信息孤岛。
- **核心创新 / 方法** · 结合块对角更新和固定散射置换，为远端特征组建立捷径。
- **Baseline** · 随机或块稀疏调优、其他 PEFT 和全量微调。
- **Benchmark** · 常识推理、生成及图像分类。
- **关键结果 / 消融** · 报告优于所比 PEFT，部分可匹配或超过全量。
- **适用条件 / 局限** · 置换适配不同骨干的边界待核。

**可复用机制** · 比较稀疏微调时同时控制非零参数数量和连接拓扑。

<a id="paper-153382"></a>

## Breaking Modality Heterogeneity in Low-Bit Quantization for Large Vision-Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153382) · [作者来源](https://openreview.net/forum?id=LmpNnlBWG5)

- **问题 / 瓶颈** · 视觉与文本的离群通道通常不同。
- **核心创新 / 方法** · 隔离少数离群通道，用轻量双分支校准剩余差异。
- **Baseline** · 已有 PTQ 及 FP16。
- **Benchmark** · 六个多模态数据集，覆盖多个权重和激活位宽。
- **关键结果 / 消融** · 摘要报告 W3A3 保留 95.3% 的 FP16 表现；汇总口径待核。
- **适用条件 / 局限** · 依赖校准数据覆盖模态输入。

**可复用机制** · 固定比特预算，按模态检查量化误差集中在哪些通道。

<a id="paper-153415"></a>

## Breaking Noise Shortcuts in Self-Supervised Learning via Noise-Aligned View Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/153415) · [作者来源](https://openreview.net/forum?id=LVFnNTcwSo)

- **问题 / 瓶颈** · 共享信号相关噪声是视图匹配捷径。
- **核心创新 / 方法** · 学习可逆方差稳定变换，在变换空间重采样噪声。
- **Baseline** · 标准自监督和预去噪。
- **Benchmark** · 含合成噪声的 CIFAR-10、ImageNet-100 和真实荧光显微。
- **关键结果 / 消融** · 显微细胞分类较标准自监督最多高 28.6 个百分点。
- **适用条件 / 局限** · 噪声结构必须可从观测估计。

**可复用机制** · 用独立噪声视图对照共享噪声增强，并在干净测试分布评测。

<a id="paper-154531"></a>

## Breaking the Bias Barrier in Concave Multi-Objective Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/154531) · [作者来源](https://openreview.net/forum?id=Ctg1L7RlkF)

- **问题 / 瓶颈** · 把采样回报代入非线性效用导数会产生梯度偏差。
- **核心创新 / 方法** · 向自然策略梯度加入多层估计以控偏，并分析二阶平滑下的偏差抵消。
- **Baseline** · 经验插值策略梯度与普通自然策略梯度。
- **Benchmark** · 凹多目标强化学习的样本复杂度理论。
- **关键结果 / 消融** · 作者给出误差平方倒数型最优阶；二阶平滑时普通方法也可达。
- **适用条件 / 局限** · 结论依赖论文的平滑性及理论设定。

**可复用机制** · 在实现前先判断非线性效用对估计偏差的敏感度。

<a id="paper-154778"></a>

## Breaking the Exactness Barrier: Interleaved DeepSeek Sparse Attention for Efficient Long Context Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/154778) · [作者来源](https://openreview.net/forum?id=B2d9y3Xf62)

- **问题 / 瓶颈** · 全局 Top-K 同步拖慢长文本推理。
- **核心创新 / 方法** · 独立选局部 Top-m，再用候选并集覆盖关键 token。
- **Baseline** · 精确 DSA。
- **Benchmark** · DeepSeek-V3.2、GLM-5，AIME 和 Needle-In-A-Haystack。
- **关键结果 / 消融** · 超过 100K token 时吞吐提高，精度可比或更好。
- **适用条件 / 局限** · 需验证局部排名对关键 token 的召回。

**可复用机制** · 测试候选召回与设备同步开销的折衷。

<a id="paper-151813"></a>

## Breaking the Grid: Distance-Guided Reinforcement Learning in Large Discrete Action Spaces

[官方论文页](https://neurips.cc/virtual/2026/poster/151813) · [作者来源](https://openreview.net/forum?id=XosdW9LFxs)

- **问题 / 瓶颈** · 离散动作数量大时探索和梯度估计昂贵。
- **核心创新 / 方法** · 动态抽样邻域并以动作距离组织回归更新。
- **Baseline** · 现有大动作空间强化学习方法，名称待核。
- **Benchmark** · 规则与不规则结构环境，最多约 10^20 动作。
- **关键结果 / 消融** · 作者报告最高 66% 改善；结构任务证明局部改进。
- **适用条件 / 局限** · 依赖有意义的动作距离。

**可复用机制** · 先验证动作邻域内回报是否平滑，再比较局部抽样与全局策略头。

<a id="paper-151142"></a>

## Breaking the Second Barrier: Sub-Second Timestamped Omni-Modal Captioning

[官方论文页](https://neurips.cc/virtual/2026/poster/151142) · [作者来源](https://openreview.net/forum?id=chPpkbsh0f)

- **问题 / 瓶颈** · 全局优势归一化会稀释局部时间边界误差。
- **核心创新 / 方法** · 以 OCR 和 ASR 校准边界，再按段独立估计 RL 优势。
- **Baseline** · 统一优势归一化及 Gemini 系列。
- **Benchmark** · AVUT、UGC、VCapsBench、Deci-Timestamp Bench。
- **关键结果 / 消融** · 摘要报告时间基准超越所比闭源模型。
- **适用条件 / 局限** · 依赖外部锚点质量；提升幅度待核。

**可复用机制** · 当输出含多类弱耦合片段时，比较分段与全局信用分配。

<a id="paper-152353"></a>

## Breaking the Static: Dynamic Text Conditioning for Diverse Image Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/152353) · [作者来源](https://openreview.net/forum?id=ThOsV8XidT)

- **问题 / 瓶颈** · 静态文本条件可能过早压缩生成多样性。
- **核心创新 / 方法** · 免训练的动态语义插值与由粗到细的去噪配合。
- **Baseline** · 静态条件扩散模型。
- **Benchmark** · 多种图像生成模型，比较多样性、对齐和审美。
- **关键结果 / 消融** · 作者报告多样性改善且对齐与画质保持。
- **适用条件 / 局限** · 具体频段和时间设置待核。

**可复用机制** · 固定采样预算对照不同条件释放时机。

<a id="paper-152515"></a>

## Breaking the Uniformity Trap: Scaling Video Diffusion Model via SplitMoE

[官方论文页](https://neurips.cc/virtual/2026/poster/152515) · [作者来源](https://openreview.net/forum?id=SYResv1L06)

- **问题 / 瓶颈** · 逐 token 均衡可能打散时空相干区域。
- **核心创新 / 方法** · 用原型引导和推拉正则把高层语义及残余视觉信息分流。
- **Baseline** · 传统均衡 MoE，激活参数预算相同。
- **Benchmark** · 视频生成基准，测收敛、路由一致性和质量。
- **关键结果 / 消融** · 作者报告三方面改善；量值待核。
- **适用条件 / 局限** · 对原型质量和数据长尾敏感。

**可复用机制** · 在固定激活参数下同时测路由一致性与生成质量。

<a id="paper-150618"></a>

## BReD: Block Replay Dithering for Stable Low-Bit EMA Optimizer States

[官方论文页](https://neurips.cc/virtual/2026/poster/150618) · [作者来源](https://openreview.net/forum?id=gnKli42BZO)

- **问题 / 瓶颈** · EMA 会跨步骤累积舍入误差。
- **核心创新 / 方法** · 确定性种子重放和块共享抖动，节省额外随机状态。
- **Baseline** · 全精度优化器状态，含 AdamW、Muon。
- **Benchmark** · 120M 至 3.4B 预训练及 7B 微调。
- **关键结果 / 消融** · 4 位下预训练困惑度变化不超过 0.5、微调不超过 0.2。
- **适用条件 / 局限** · 3 位稳定性仅验证所测配置。

**可复用机制** · 量化递归状态时测长程偏差而非仅单步重建误差。

<a id="paper-152709"></a>

## Brenier Meets Adversarial Training: Optimal Transport Geometry for Robust Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/152709) · [作者来源](https://openreview.net/forum?id=QzN8ycFg2x)

- **问题 / 瓶颈** · 逐样本更新可能不能实现有效的联合运输。
- **核心创新 / 方法** · 使用带重分配的粒子优化，或将映射限制为凸函数梯度。
- **Baseline** · 标准鲁棒训练方法。
- **Benchmark** · 鲁棒回归、图像分类和控制。
- **关键结果 / 消融** · 作者报告分布偏移下表现改善。
- **适用条件 / 局限** · 结果对应 Wasserstein 惩罚设定。

**可复用机制** · 训练时比较独立样本扰动与受结构约束的联合运输。

<a id="paper-154364"></a>

## BrickAnything: Geometry-Conditioned Buildable Brick Generation with Structure-Aware Tokenization

[官方论文页](https://neurips.cc/virtual/2026/poster/154364) · [作者来源](https://openreview.net/forum?id=E8PQVRghmQ)

- **问题 / 瓶颈** · 逐件生成可能产生不可施工的中间状态。
- **核心创新 / 方法** · 点云条件下预测连接关系序列，配合合法性检查和回退。
- **Baseline** · 常规部件排序。
- **Benchmark** · 积木三维生成，测几何保真及可建造性。
- **关键结果 / 消融** · 作者报告回退与重生成减少。
- **适用条件 / 局限** · 依赖约束判定与部件库。

**可复用机制** · 输出离散装配序列时把合法连接作为基本 token。

<a id="paper-151991"></a>

## BrickFlow: Connectivity-Guided Brick Reconstruction

[官方论文页](https://neurips.cc/virtual/2026/poster/151991) · [作者来源](https://openreview.net/forum?id=WJX7hy4lhB)

- **问题 / 瓶颈** · 学习的全局几何先验不能保证连接。
- **核心创新 / 方法** · 训练集合条件 SE(3) 流并加入图像条件，测试时向连接流形修正。
- **Baseline** · 无连接引导的生成流。
- **Benchmark** · 给定零件和图像的积木装配。
- **关键结果 / 消融** · 作者报告重建与有效性改善；幅度待核。
- **适用条件 / 局限** · 依赖已知部件和连接几何。

**可复用机制** · 将离散可行性和全局形状的评测分开，比较有无解析约束。

<a id="paper-148153"></a>

## Bridge Graphical Models: Coupling, Projection, and Current-Preserving Dynamics for Generative Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/148153) · [作者来源](https://openreview.net/forum?id=zu4l4sQPdU)

- **问题 / 瓶颈** · 马尔可夫速度场压缩端点相关信息，训练前难评估损失。
- **核心创新 / 方法** · 定义给定马尔可夫状态的桥速度积分条件方差，分离耦合、桥法则及投影。
- **Baseline** · 不同端点耦合和桥选择。
- **Benchmark** · 合成、潜空间以及 CIFAR-10、Fashion-MNIST 像素试验。
- **关键结果 / 消融** · CPU 分钟级代理排序与 GPU 小时级训练损失和 FID 趋势一致。
- **适用条件 / 局限** · 证据为试验规模，代理不保证任意模型排序。

**可复用机制** · 把速度条件方差作为低成本选型筛查并在少量训练上校验。

<a id="paper-151655"></a>

## BridgeMVS: Bridging Multi-View Stereo and Monodepth via Bidirectional Dynamic Fusion

[官方论文页](https://neurips.cc/virtual/2026/poster/151655) · [作者来源](https://openreview.net/forum?id=Z1iGG61Tr4)

- **问题 / 瓶颈** · 单向融合难用多视角证据纠正单目错误。
- **核心创新 / 方法** · 分级更新代价体与单目特征，并加入逐尺度单目监督。
- **Baseline** · 单向融合与级联 MVS，具名对照待核。
- **Benchmark** · DTU、Tanks and Temples、ETH3D。
- **关键结果 / 消融** · 作者报告三个基准均具竞争力，数值待核。
- **适用条件 / 局限** · 依赖跨视图对齐与单目先验质量。

**可复用机制** · 对比单向与双向融合，并在反光和低纹理区域分别测深度。

<a id="paper-151085"></a>

## BridgeTwist: Twisting Schrödinger Bridges for Training-Free Conditional Sampling

[官方论文页](https://neurips.cc/virtual/2026/poster/151085) · [作者来源](https://openreview.net/forum?id=d5smsmfpBy)

- **问题 / 瓶颈** · 现有免训练扩散条件采样不直接覆盖一般源分布的桥。
- **核心创新 / 方法** · 由速度和分数构造端点代理，早期降权，通过序贯蒙特卡洛校正。
- **Baseline** · 免训练条件采样方法。
- **Benchmark** · MNIST、CIFAR-10 分类条件生成和修补，CelebA-HQ 文本生成。
- **关键结果 / 消融** · 作者报告优于所比基线，并给出渐近正确性。
- **适用条件 / 局限** · 有限粒子成本和退化待核。

**可复用机制** · 在冻结生成先验时比较额外粒子预算和条件满足率。

<a id="paper-152887"></a>

## Bridging CLIP with DINO: Cross-Modal Information Maximization for Online Test-Time Adaptation

[官方论文页](https://neurips.cc/virtual/2026/poster/152887) · [作者来源](https://openreview.net/forum?id=PeeVlwPgi8)

- **问题 / 瓶颈** · 熵最小化会强化由视觉扰动造成的高置信错误。
- **核心创新 / 方法** · 融合 CLIP 与 DINO logits，门控信息最大化并在线校正类别偏斜。
- **Baseline** · 标准熵最小化与在线适配方法。
- **Benchmark** · 连续适配、混合域变化和域泛化基准。
- **关键结果 / 消融** · 作者报告稳健且具竞争力；指标与数值待核。
- **适用条件 / 局限** · 需额外视觉骨干及可靠小批多样性估计。

**可复用机制** · 对照单骨干置信度和跨骨干一致性作为适配门控。

<a id="paper-155350"></a>

## Bridging Compute- and Data-Optimal Pretraining

[官方论文页](https://neurips.cc/virtual/2026/poster/155350) · [作者来源](https://openreview.net/forum?id=6HVSfPO1cT)

- **问题 / 瓶颈** · 经典缩放假设数据无限
- **核心创新 / 方法** · 拟合衍生 token 相对新 token 的有效性
- **Baseline** · 经典计算最优缩放
- **Benchmark** · Dolma-3，14M–600M，重复与改写
- **关键结果 / 消融** · 有效性随模型、token 配比和衍生量变化并饱和
- **适用条件 / 局限** · 外推至更大模型待核

**可复用机制** · 数据固定时先测衍生数据边际收益再扩大计算。

<a id="paper-155931"></a>

## Bridging Diffusion and Autoregression for Flexible Time Series Synthesis

[官方论文页](https://neurips.cc/virtual/2026/poster/155931) · [作者来源](https://openreview.net/forum?id=1jBDu9GqnS)

- **问题 / 瓶颈** · 自回归积累误差，扩散长度受限
- **核心创新 / 方法** · 用块间因果块内双向掩码与块长度课程训练
- **Baseline** · 自回归与扩散基线，名称待核
- **Benchmark** · 时序合成，测保真、多样性和下游效用
- **关键结果 / 消融** · 摘要报告外推至训练长度四倍仍稳定
- **适用条件 / 局限** · 极长时域和课程的独立贡献待核

**可复用机制** · 分别扫块长度与总时域，区分局部质量和长程漂移。

<a id="paper-153651"></a>

## Bridging Image Restoration and Recognition via Causal Mediated Unrolling

[官方论文页](https://neurips.cc/virtual/2026/poster/153651) · [作者来源](https://openreview.net/forum?id=JkqJjv4paC)

- **问题 / 瓶颈** · 恢复会丢任务线索或产生识别捷径
- **核心创新 / 方法** · 半二次分裂下交替作带中介的任务更新与流形投影
- **Baseline** · 冻结识别器下的图像恢复方法
- **Benchmark** · 退化图像恢复和识别，细节待核
- **关键结果 / 消融** · 摘要提出兼顾识别与外观，量化幅度待核
- **适用条件 / 局限** · 依赖识别器和图像先验

**可复用机制** · 同时测任务准确率与保真度，检验交替约束能否抑制捷径。

<a id="paper-156072"></a>

## Bridging Modalities, Spanning Time: Structured Memory for Ultra-Long Agentic Video Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/156072) · [作者来源](https://openreview.net/forum?id=0evT0zV3xO)

- **问题 / 瓶颈** · 抽帧与割裂检索使长程证据丢失
- **核心创新 / 方法** · 用类型化图连接视觉语义事件，并维护实体与活动叙事链
- **Baseline** · 通用、长视频及 Agent 系统
- **Benchmark** · EgoLifeQA、Ego-R1、MM-Lifelong
- **关键结果 / 消融** · 较最强旧 Agent 分别高 10.1、7.4、5.9 点
- **适用条件 / 局限** · 图可受事件抽取和摘要错误污染

**可复用机制** · 将局部证据和长期摘要分两层检索，分别消融。

<a id="paper-150549"></a>

## Bridging Risk Approximation Gaps in Model Predictive Task Sampling via In-Context Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/150549) · [作者来源](https://openreview.net/forum?id=hJMwdk9jfG)

- **问题 / 瓶颈** · 历史稀疏且当前风险预测滞后一轮
- **核心创新 / 方法** · 上下文序列模型用一步前瞻和时间加权滑窗预测风险
- **Baseline** · 既有预测式任务采样
- **Benchmark** · 鲁棒 Meta-RL、域随机化、语言模型提示课程
- **关键结果 / 消融** · 作者报告难度估计和表现改善，幅度待核
- **适用条件 / 局限** · 依赖优化历史能预测下一轮

**可复用机制** · 在相同交互预算下对照当前难度与前瞻难度。

<a id="paper-151833"></a>

## Bridging Scene Generation and Planning: Driving with World Model via Unifying Vision and Motion Representation

[官方论文页](https://neurips.cc/virtual/2026/poster/151833) · [作者来源](https://openreview.net/forum?id=XbmmVXqaHc)

- **问题 / 瓶颈** · 视频生成特征与实时规划的运动语义脱节
- **核心创新 / 方法** · 以轨迹词表调节场景预测，再向多模态规划器迁移编码器
- **Baseline** · 既有驾驶世界模型，具名方法待核
- **Benchmark** · 视觉预测和车端规划，数据集指标待核
- **关键结果 / 消融** · 摘要报告生成和规划可联合利用，具体结果待核
- **适用条件 / 局限** · 依赖轨迹条件覆盖与未来预测质量

**可复用机制** · 对照只迁移视觉编码和共同迁移运动编码。

<a id="paper-151850"></a>

## Bridging Simulation and Reality: Geometry and Decision Alignment for Autonomous Driving

[官方论文页](https://neurips.cc/virtual/2026/poster/151850) · [作者来源](https://openreview.net/forum?id=XQr8N3Wv5o)

- **问题 / 瓶颈** · 图像外观接近仍可能输出不同动作
- **核心创新 / 方法** · 对齐场景几何与潜表征，并对齐结构条件下的动作分布
- **Baseline** · 外观级适配方法
- **Benchmark** · 重新划分的 nuScenes
- **关键结果 / 消融** · 摘要报告迁移改善，具体分数待核
- **适用条件 / 局限** · 依赖可用几何和结构信息

**可复用机制** · 分别消融感知和决策对齐，比较闭环表现。

<a id="paper-151879"></a>

## Bridging Structure and Language: Graph-Based Visual Reasoning for Autonomous Road Understanding

[官方论文页](https://neurips.cc/virtual/2026/poster/151879) · [作者来源](https://openreview.net/forum?id=XDFxPupil1)

- **问题 / 瓶颈** · 视觉语言模型难同时理解空间关系和开放语义
- **核心创新 / 方法** · 将结构与语义统一为图，用递归查询生成问答和证据链
- **Baseline** · 大型开闭源 VLM
- **Benchmark** · 道路结构组合问答及不同推理深度
- **关键结果 / 消融** · 摘要报告 2B 或 4B 模型用 20–80 个场景训练即可改善
- **适用条件 / 局限** · 图结构错误会传播到监督

**可复用机制** · 复杂场景问答同时保存查询、标签和支持节点以可追溯。

<a id="paper-149662"></a>

## Bridging the Gap Between Harmfulness Belief and Refusal Behavior for Safety Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/149662) · [作者来源](https://openreview.net/forum?id=oNxj0lY1EY)

- **问题 / 瓶颈** · 模型识别风险也可能输出不当响应
- **核心创新 / 方法** · 用适配器保持风险判断信号并门控拒答学习
- **Baseline** · 既有拒答导向对齐
- **Benchmark** · 多个语言模型和安全基准，名称待核
- **关键结果 / 消融** · 摘要报告安全响应改进，消融待核
- **适用条件 / 局限** · 须同时监控正常请求误拒

**可复用机制** · 把风险检测和行动执行当成可分别失效的环节。

<a id="paper-152513"></a>

## Bridging the Gap: Position-Independent Cache Reuse for Hybrid SSM-Attention Architectures

[官方论文页](https://neurips.cc/virtual/2026/poster/152513) · [作者来源](https://openreview.net/forum?id=SZ24HRIAMK)

- **问题 / 瓶颈** · SSM 缓存失配让邻层复用失效
- **核心创新 / 方法** · 重算少量边界 token 并校正残差状态及衰减
- **Baseline** · 混合架构的既有缓存策略
- **Benchmark** · 多种混合模型与数据集，测首 token 延迟和准确率
- **关键结果 / 消融** · 摘要报告首 token 约加速两倍且准确率有竞争力
- **适用条件 / 局限** · 依赖状态可高效更新及缓存命中

**可复用机制** · 用相同命中条件比较各层联动复用的端到端延迟。

<a id="paper-151598"></a>

## Bridging the Simulation-to-Experiment Gap with Adversarial Distribution Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/151598) · [作者来源](https://openreview.net/forum?id=ZN3nHHOt4r)

- **问题 / 瓶颈** · 实验变量部分可见，模拟完整但有偏
- **核心创新 / 方法** · 先在完整仿真训练，再对齐真实观测的分布
- **Baseline** · 未校准仿真生成器
- **Benchmark** · 合成与科学实验分布对齐，细节待核
- **关键结果 / 消融** · 作者证明所设条件下恢复目标观测分布
- **适用条件 / 局限** · 观测校准不保证所有隐藏状态正确

**可复用机制** · 明确区分观测拟合与潜变量可辨识性。

<a id="paper-139284"></a>

## Brittlebench: Quantifying LLM robustness via prompt sensitivity

[官方论文页](https://neurips.cc/virtual/2026/poster/139284) · [作者来源](https://openreview.net/forum?id=ZRbmggXS7S)

- **问题 / 瓶颈** · 单一题面掩盖提示敏感性
- **核心创新 / 方法** · 给基准构造保义变体并分解题目和措辞方差
- **Baseline** · 原题及现有模型
- **Benchmark** · 多种开放和商业模型的公开任务
- **关键结果 / 消融** · 摘要报告表现最多降约 21%，单一改写在 63% 情况改变相对排序
- **适用条件 / 局限** · 依赖语义保持的验证

**可复用机制** · 为基准结果报告改写方差和排序翻转率。

<a id="paper-149705"></a>

## BROS: Bias-Corrected Randomized Subspaces for Memory-Efficient Single-Loop Bilevel Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/149705) · [作者来源](https://openreview.net/forum?id=o4aIX9knRi)

- **问题 / 瓶颈** · 全空间辅助变量内存大或替代方法收敛弱
- **核心创新 / 方法** · 随机子空间更新，加双探针校正得到无偏估计
- **Baseline** · MA-SOBA 及全空间双层优化
- **Benchmark** · 数据清洗、混合、表示学习及 ViT 重加权
- **关键结果 / 消融** · 理论保持同阶样本复杂度，峰值内存最多降 44.9%
- **适用条件 / 局限** · 依赖论文中的双层优化假设

**可复用机制** · 同时记录内存、目标性能和取样成本。

<a id="paper-156078"></a>

## BSO: Safety Alignment Is Density Ratio Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/156078) · [作者来源](https://openreview.net/forum?id=0akpzKEMx0)

- **问题 / 瓶颈** · 多阶段训练依赖辅助模型与启发式安全项
- **核心创新 / 方法** · 从最优安全策略的似然比推导单阶段 Bregman 损失族
- **Baseline** · 既有安全偏好优化方法
- **Benchmark** · 安全对齐任务，衡量有用性与安全性
- **关键结果 / 消融** · 作者报告改善取舍并可恢复部分既有方法
- **适用条件 / 局限** · 最优恢复依赖理论条件及偏好数据

**可复用机制** · 在同样偏好数据和预算下比较不同散度的安全效用曲线。

<a id="paper-151140"></a>

## BSTabDiff: Block-Subunit Diffusion Priors for High-Dimensional Tabular Data Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/151140) · [作者来源](https://openreview.net/forum?id=ciPCMXX1aj)

- **问题 / 瓶颈** · 样本少、特征多时全维密度估计病态。
- **核心创新 / 方法** · 用共享低维子单元解码块内特征，并在块级建模全局依赖。
- **Baseline** · 无结构表格生成器。
- **Benchmark** · 高维低样本表格生成。
- **关键结果 / 消融** · 摘要报告保真度和稳定性改善。
- **适用条件 / 局限** · 要求存在局部分组结构，跨块依赖过密时可能受限。

**可复用机制** · 按跨块依赖强度分组测试块压缩与全维建模。

<a id="paper-150613"></a>

## Budget-Conditioned Clipping Policies for Differentially Private Federated Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/150613) · [作者来源](https://openreview.net/forum?id=greiwlIhYZ)

- **问题 / 瓶颈** · 私有梯度驱动的裁剪调整会增加记账负担。
- **核心创新 / 方法** · 预拟合确定裁剪策略，并将部署阈值仅条件化于声明预算和轮次。
- **Baseline** · 固定阈值与自适应差分隐私联邦方法。
- **Benchmark** · MNIST、CIFAR-10、CIFAR-100、Heart Disease。
- **关键结果 / 消融** · 匹配预算时作者报告隐私效用折衷和通信效率改善。
- **适用条件 / 局限** · 代理数据须公开或单独隐私化；代理迁移需验证。

**可复用机制** · 把超参数调节从私有训练循环移到代理校准，并保留匹配预算比较。

<a id="paper-155643"></a>

## Budgeted Multi-Source Counterfactual Annotation for Off-Policy Evaluation

[官方论文页](https://neurips.cc/virtual/2026/poster/155643) · [作者来源](https://openreview.net/forum?id=446GKdY1L2)

- **问题 / 瓶颈** · 日志覆盖不足时估计方差高，补标来源质量不同。
- **核心创新 / 方法** · 将上下文、动作与来源的选择建模为方差最小化的整数分配。
- **Baseline** · 不加标注。
- **Benchmark** · 模拟临床及模型标注教育赌博机。
- **关键结果 / 消融** · 可优化方差分量降低 20.58% 和 10.77%。
- **适用条件 / 局限** · 依赖来源误差估计，改善的只是方差分量。

**可复用机制** · 在采购补标前，比较各候选来源第一条标注的边际价值。

<a id="paper-149709"></a>

## Bug or Feature$^2$: Weight Drift, Activation Sparsity, and Spikes

[官方论文页](https://neurips.cc/virtual/2026/poster/149709) · [作者来源](https://openreview.net/forum?id=o1pategtiw)

- **问题 / 瓶颈** · 激活函数和损失会在早期共同塑造权重漂移。
- **核心创新 / 方法** · 分析正偏置激活下初始梯度符号，并比较平方和截断变体。
- **Baseline** · ReLU、GELU、SiLU 及平方变体。
- **Benchmark** · 跨架构和 79 组稀疏度配置。
- **关键结果 / 消融** · GPT-nano 稀疏度最高 90%，约 70% 以上见准确率骤降；截断改善平方 ReLU 尖峰。
- **适用条件 / 局限** · 阈值随训练配置变化。

**可复用机制** · 绘制稀疏度、精度和尖峰的联合曲线来选激活。

<a id="paper-151890"></a>

## Busemannformer: Horospherical Self-Attention for Hyperbolic Graph Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/151890) · [作者来源](https://openreview.net/forum?id=XAJBBFiTpE)

- **问题 / 瓶颈** · 常见双曲注意力未直接利用理想边界。
- **核心创新 / 方法** · 查询选择理想边界方向，按键在该方向的 Busemann 深度打分。
- **Baseline** · 欧氏对照与各打分变体。
- **Benchmark** · Disease-NC、PubMed-LP、Disease-LP、Airport。
- **关键结果 / 消融** · PubMed 对称变体比非对称高 10.3 个百分点 AUC；Airport 中心性任务出现失效。
- **适用条件 / 局限** · 树深假设不适合中心性标签。

**可复用机制** · 在定向和无向边任务分别评估核对称性。

<a id="paper-156083"></a>

## Bypassing PC1 Makes SAEs More Reproducible

[官方论文页](https://neurips.cc/virtual/2026/poster/156083) · [作者来源](https://openreview.net/forum?id=0YAxdKV85F)

- **问题 / 瓶颈** · 主方向被不同种子分解成不同原子，重要性排行失真。
- **核心创新 / 方法** · 单独路由第一主成分，稀疏字典仅分解其余变化。
- **Baseline** · 标准 SAE 多种子及字典整体回收。
- **Benchmark** · 五个家族九种语言模型。
- **关键结果 / 消融** · 前 50 特征回收率达 74%–97%，共享特征的 logit-lens 预测更准。
- **适用条件 / 局限** · 适配强各向异性的中间层，其他层需测。

**可复用机制** · 测主要协方差方向与跨种子特征回收，再决定是否旁路。

<a id="paper-149633"></a>

## ByteDistill: Cross-Tokenizer Distillation via Chunk-wise Byte-Level Distribution Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/149633) · [作者来源](https://openreview.net/forum?id=od5PZv55K2)

- **问题 / 瓶颈** · 教师学生 token 支持与切分不一致。
- **核心创新 / 方法** · 在对齐解码块中投影到 256 类下一字节空间，并边缘化分词边界。
- **Baseline** · 监督微调及既有跨分词蒸馏。
- **Benchmark** · 离策略、在线策略设置和 GSM8K。
- **关键结果 / 消融** · 离策略 GSM8K 比最强对照高 1.75 个百分点。
- **适用条件 / 局限** · 仅覆盖对齐块及其观测路径；额外代价待核。

**可复用机制** · 在同训练轨迹下比较词元映射和字节分布对齐。

<a id="paper-151433"></a>

## C2FT: Enhancing Fine-Grained Perception in MLLMs via Confuse-then-Contrast Fine-Tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/151433) · [作者来源](https://openreview.net/forum?id=aktp1wVAdL)

- **问题 / 瓶颈** · 独立样本微调难强调局部视觉区别。
- **核心创新 / 方法** · 从模型不确定性发现混淆，用困难正负例构成联合视觉提示。
- **Baseline** · 标准 SFT、GRPO。
- **Benchmark** · 细粒度分类和视觉问答。
- **关键结果 / 消融** · Qwen3-VL-4B 平均分别高 3.87、4.35 个百分点。
- **适用条件 / 局限** · 需固定训练 token 并核对组构造偏差。

**可复用机制** · 用同预算比较随机组与模型混淆驱动的组。

<a id="paper-151786"></a>

## C3: Long-Horizon Character Consistency via Causal-Continuous State Dynamics and Memory Rewriting

[官方论文页](https://neurips.cc/virtual/2026/poster/151786) · [作者来源](https://openreview.net/forum?id=Y0keyhhQHc)

- **问题 / 瓶颈** · 离散阈值会使角色突变，长历史会弱化当前指令。
- **核心创新 / 方法** · 将连续状态动力学与条件化记忆重写耦合。
- **Baseline** · 平滑离散情感状态机。
- **Benchmark** · Chronos-Sim 百轮会话、两种底座及人工审核。
- **关键结果 / 消融** · SAR 提高 10.5 个百分点；报告长会话 token 减少约 60%。
- **适用条件 / 局限** · 重写需事实核查，结果依赖角色和底座。

**可复用机制** · 在长期角色代理上独立检查叙事一致性和记忆事实保真。

<a id="paper-150465"></a>

## CAB: Accelerating Flow and Diffusion Sampling via Rectification and Corrected Adams-Bashforth

[官方论文页](https://neurips.cc/virtual/2026/poster/150465) · [作者来源](https://openreview.net/forum?id=hpZ7epyUY4)

- **问题 / 瓶颈** · 少量模型评估下，高阶求解和蒸馏都可能损害质量。
- **核心创新 / 方法** · 统一变换到整流坐标，用已有速度修正 Adams–Bashforth 预测，无额外函数评估。
- **Baseline** · 强免训练采样器，具体名称待核。
- **Benchmark** · 预训练流和扩散模型的分类条件、文本到图像任务，测质量与 NFE。
- **关键结果 / 消融** · 在 6–20 NFE 改善质量与开销权衡，局部截断误差至少三阶、全局误差二阶。
- **适用条件 / 局限** · 高步数优势因模型而异。

**可复用机制** · 固定 NFE 对照坐标变换和历史校正，对低步数单独作质量曲线。

<a id="paper-153622"></a>

## CaC: Advancing Video Reward Models via Hierarchical Spatiotemporal Concentrating

[官方论文页](https://neurips.cc/virtual/2026/poster/153622) · [作者来源](https://openreview.net/forum?id=K18iJJE8cU)

- **问题 / 瓶颈** · 整体画质分数容易漏掉少量局部或瞬时异常。
- **核心创新 / 方法** · 先扫时间窗再定位区域，以时空 IoU 监督两轮 GRPO 的中间定位。
- **Baseline** · 对照整体奖励与现有模型，具名项待核。
- **Benchmark** · 生成视频细粒度异常定位及生成后异常评测。
- **关键结果 / 消融** · 摘要报告准确率改善 25.7%，作为奖励使异常减少 11.7%。
- **适用条件 / 局限** · 依赖带时空标注的训练集，罕见异常覆盖待核。

**可复用机制** · 给稀疏错误的奖励模型分别监督找错时间和位置，再同时测定位和最终质量。

<a id="paper-154215"></a>

## CacheMAS: Cache Communication for Single-Pass, Jointly-Optimized Multi-Agent Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/154215) · [作者来源](https://openreview.net/forum?id=FKl2gcTSgN)

- **问题 / 瓶颈** · 中间文本在角色之间反复解码和预填充。
- **核心创新 / 方法** · 用预填充缓存作为通信状态，将流程编成单一自回归轨迹，以序列级奖励联合优化。
- **Baseline** · 既有多智能体系统。
- **Benchmark** · 数学、多跳问答、代码；评估 token、时延与任务表现。
- **关键结果 / 消融** · 约少三倍 token、快两倍，联合优化后领先 1–8 点。
- **适用条件 / 局限** · 需要可访问兼容的缓存，跨异构模型通信待核。

**可复用机制** · 固定任务预算，比较自然语言消息和缓存共享，并分开测前向时延和联合优化收益。

<a id="paper-149314"></a>

## Cache the Future: Training-Free Self-Revision for Diffusion Transformer Acceleration

[官方论文页](https://neurips.cc/virtual/2026/poster/149314) · [作者来源](https://openreview.net/forum?id=r6WJ2zUzRI)

- **问题 / 瓶颈** · 仅向前外推历史特征会随预测距离积累误差。
- **核心创新 / 方法** · 缓存未来特征，修正潜状态和速度，并插值恢复跳过的步。
- **Baseline** · 现有免训练缓存和加速方案。
- **Benchmark** · FLUX.1-dev、Qwen-Image、Wan2.1-1.3B、Hunyuan Video；测速度和重建质量。
- **关键结果 / 消融** · 摘要报告图像最高约 5 倍、视频超过 4.3 倍加速。
- **适用条件 / 局限** · 实际收益取决于可跳步跨度和插值误差。

**可复用机制** · 比较仅外推和后续锚点修订，扫锚点间距测质量与时延。

<a id="paper-139801"></a>

## CADMA: Capacity-Aware Recall Decomposition for Generative Model Assessment

[官方论文页](https://neurips.cc/virtual/2026/poster/139801) · [作者来源](https://openreview.net/forum?id=3iWHOoWmt3)

- **问题 / 瓶颈** · 仅按几何邻近计召回会重复用到少数生成样本，混淆模式丢失和塌缩。
- **核心创新 / 方法** · 用一对一匹配区分几何覆盖与可分配的有效覆盖，并分解召回诊断。
- **Baseline** · 现有基于几何的生成召回指标。
- **Benchmark** · 玩具分布及生成模型，诊断模式丢失和塌缩。
- **关键结果 / 消融** · 作者报告更少出现过于乐观的召回，并可区分多类失败。
- **适用条件 / 局限** · 结果依赖特征空间和局部匹配尺度。

**可复用机制** · 做生成评估时构造不同类型的缺失分布，验证指标能区分重复与未覆盖。

<a id="paper-151842"></a>

## CAFE: Causally-Guided Automated Feature Engineering with Multi-Agent Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151842) · [作者来源](https://openreview.net/forum?id=XWuLGI5zio)

- **问题 / 瓶颈** · 统计启发式选出的特征可能在分布漂移时失效。
- **核心创新 / 方法** · 先学稀疏因果图并分组，再由多智能体 Q 学习按组选择变换。
- **Baseline** · 最强自动特征工程对照及非因果多智能体对照。
- **Benchmark** · 15 个公开基准，分类 macro-F1，回归逆相对绝对误差，另测 Folktables 和受控偏移。
- **关键结果 / 消融** · 相对非因果多智能体对照，分布外性能下降最多约缩小至四分之一。
- **适用条件 / 局限** · 依赖因果图先验质量，观测图不保证真实因果。

**可复用机制** · 固定搜索预算，将软分组与无先验、硬限制分别比较。

<a id="paper-151831"></a>

## CAIRN: Cross-Room 3D Scene Understanding with Topology-Aware Large Multimodal Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151831) · [作者来源](https://openreview.net/forum?id=Xcm4VFn0nR)

- **问题 / 瓶颈** · 单房间三维问答训练难覆盖跨房间关系。
- **核心创新 / 方法** · 图网络编码房内关系，学习房间 token，用分层掩码和几何偏置按拓扑路由注意力。
- **Baseline** · 以既有 3D-LLM 为对照，具名项待核。
- **Benchmark** · 基于 HM3D 的 CAIRN-MR，覆盖定位、描述和四项问答；另测五个单房间基准。
- **关键结果 / 消融** · 作者报告多房间任务全面改善，单房间表现仍具竞争力。
- **适用条件 / 局限** · 需要可靠房间拓扑和场景分割。

**可复用机制** · 对层次场景加入显式房间级路由，并分别测房内和跨房间查询。

<a id="paper-139709"></a>

## CalArena: A Large Scale Post-Hoc Calibration Benchmark

[官方论文页](https://neurips.cc/virtual/2026/poster/139709) · [作者来源](https://openreview.net/forum?id=97NdFtMyZ3)

- **问题 / 瓶颈** · 校准误差指标和不统一的实验配置难公平比较后处理。
- **核心创新 / 方法** · 用统一后处理实现和 Post-Hoc Improvement 比较校准方法。
- **Baseline** · 分箱、平滑、专用多分类与通用学习校准方法。
- **Benchmark** · 约 2000 项表格与视觉实验，覆盖二分类、多分类及大规模分类。
- **关键结果 / 消融** · 多数设置平滑优于分箱，高维多分类宜用专用方法。
- **适用条件 / 局限** · 结论依赖评分规则和模型分布。

**可复用机制** · 选校准方法时同时核对概率可靠性与预测质量有无下降。

<a id="paper-150100"></a>

## Calibeating Prediction-Powered Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/150100) · [作者来源](https://openreview.net/forum?id=kh57rITtAA)

- **问题 / 瓶颈** · 黑盒分数未校准时，直接作为回归调整可能损失统计效率。
- **核心创新 / 方法** · 线性或保序校准后平均预测，给出等价 AIPW 表达。
- **Baseline** · PPI、AIPW、PPI++。
- **Benchmark** · 模拟、复现任务及语言模型评估，比较均值估计效率。
- **关键结果 / 消融** · 线性校准与 PPI++ 一阶等价，保序校准在所设条件下有推断保证。
- **适用条件 / 局限** · 理论使用固定或交叉拟合分数；弱预测器收益有限。

**可复用机制** · 小标注预算下对照原始预测调整和后校准调整，并报告区间覆盖与宽度。

<a id="paper-148367"></a>

## Calibrated Safe Policy Improvement for Continuous Offline Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/148367) · [作者来源](https://openreview.net/forum?id=yOfHpD0Pkv)

- **问题 / 瓶颈** · 离线连续控制缺少离散访问计数提供的支持度。
- **核心创新 / 方法** · 在留出数据上校准模型集成分歧，在树搜索中设硬门，并按相对基线收益切换。
- **Baseline** · 原有行为策略和离线改进对照。
- **Benchmark** · 三个 MuJoCo 连续控制域，比较不同数据量下表现。
- **关键结果 / 消融** · 低数据时作者报告避免退化，信任可靠后改善；理论界针对通过门控的根决策。
- **适用条件 / 局限** · 证书依赖校准数据代表性，不自动覆盖全轨迹。

**可复用机制** · 用独立误差校准数据设搜索门槛，并在低覆盖下对照是否回退。

<a id="paper-154444"></a>

## Calibrated Target Noise Recovers Curvature from the Gradients

[官方论文页](https://neurips.cc/virtual/2026/poster/154444) · [作者来源](https://openreview.net/forum?id=DVmkA0zr2U)

- **问题 / 瓶颈** · 缺少逐样本梯度和高阶导数时难以估计训练曲率。
- **核心创新 / 方法** · 注入方差按输出曲率校准的零均值目标噪声，利用新批梯度的协方差恢复曲率。
- **Baseline** · 与目标曲率及既有训练设置比较；具名对照待核。
- **Benchmark** · 曲率恢复、预条件优化和提前停止实验；数据集待核。
- **关键结果 / 消融** · 作者报告恢复 GGN，在前馈 ReLU 设置还恢复总体 Hessian 对角块。
- **适用条件 / 局限** · 需能重复取得受控扰动下的梯度，模型条件待核正文。

**可复用机制** · 当二阶自动微分不可用时，比较噪声梯度估计的精度、批次数和优化收益。

<a id="paper-154784"></a>

## Calibrating LLMs with Semantic-level Reward

[官方论文页](https://neurips.cc/virtual/2026/poster/154784) · [作者来源](https://openreview.net/forum?id=B12bR4cE0U)

- **问题 / 瓶颈** · 等价答案的文字不同，显式 token 置信度可能不一致。
- **核心创新 / 方法** · 将正确性奖励和语义奖励结合，对正确答案鼓励语义一致，对错误答案降低伪一致。
- **Baseline** · 显式置信度奖励对照。
- **Benchmark** · HotpotQA、TriviaQA、MSMARCO、NQ-Open，三类模型，测 ECE 与 AUROC。
- **关键结果 / 消融** · 摘要报告 ECE 最多降 40%、AUROC 最多升 31%。
- **适用条件 / 局限** · 依赖语义等价判定及可核验正确性。

**可复用机制** · 训练开放式问答校准时比较语义等价类和字符串层置信度，并做域外评估。

<a id="paper-149357"></a>

## Calibration Is Not Control: Intervention Advantage for LLM-Agent Oversight

[官方论文页](https://neurips.cc/virtual/2026/poster/149357) · [作者来源](https://openreview.net/forum?id=qeqOwa6tud)

- **问题 / 瓶颈** · 同等失败风险的前缀可能有不同的可恢复程度。
- **核心创新 / 方法** · 用前缀分支构造干预反事实，以动作条件价值决定是否切换。
- **Baseline** · 标量风险路由和同一风险分数再校准。
- **Benchmark** · 四项基准，含 ALFWorld，比较控制遗憾。
- **关键结果 / 消融** · 再校准可改善风险预测却不改变控制遗憾；最强互动设置遗憾从 0.506 降到 0.110。
- **适用条件 / 局限** · 若干预本身弱，动作条件优势也会收缩。

**可复用机制** · 评估 Agent 守护器时对同一状态试验多种干预，而非只用风险预测指标得出控制结论。

<a id="paper-152525"></a>

## Calibration without Ground Truth

[官方论文页](https://neurips.cc/virtual/2026/poster/152525) · [作者来源](https://openreview.net/forum?id=STxXui2w7z)

- **问题 / 瓶颈** · 强模型可能失校准而部署数据缺标签。
- **核心创新 / 方法** · 在两个模型不能同时校准的条件下，以 Bregman 投影调整强模型输出。
- **Baseline** · 未处理主模型，弱而校准较好的参考模型。
- **Benchmark** · 多规模语言模型的常见基准，测 ECE；具体基准待核。
- **关键结果 / 消融** · 作者给出严格最坏情况改善保证，并报告 ECE 降逾 40%。
- **适用条件 / 局限** · 需要可靠参考和相互校准判定；条件不成立时无严格改进保证。

**可复用机制** · 有配对预测无真值时先诊断参考是否提供互补校准约束。

<a id="paper-150537"></a>

## CAM: Question Answering on Entity-Centric Videos with Continuous Extraction and Adaptive Querying

[官方论文页](https://neurips.cc/virtual/2026/poster/150537) · [作者来源](https://openreview.net/forum?id=hPMIoGy7je)

- **问题 / 瓶颈** · 独立片段记忆丢失跨时间关系，相似度检索可能漏掉细节。
- **核心创新 / 方法** · 知识图累积实体关系，局部子图到阈值时总结，按需组合图遍历和音视频复查。
- **Baseline** · 已有长视频问答基线。
- **Benchmark** · 三个长视频问答基准，名称待核。
- **关键结果 / 消融** · 准确率最多提高 23 个百分点。
- **适用条件 / 局限** · 图谱错误和回查预算可能限制收益。

**可复用机制** · 按问题意图选择结构化记忆或回看证据，并控制跨轮摘要粒度。

<a id="paper-139573"></a>

## Can 4D Foundation Models Remember?

[官方论文页](https://neurips.cc/virtual/2026/poster/139573) · [作者来源](https://openreview.net/forum?id=Hg58xidgpB)

- **问题 / 瓶颈** · 像素相似度缺少视野外物体的参考。
- **核心创新 / 方法** · 以 360 度视频为参照，分开测物体永久性、运动连续和外观保留。
- **Baseline** · 多类 4D 重建和相机可控视频模型。
- **Benchmark** · PersistBench 的物体级指标。
- **关键结果 / 消融** · 对象离开视野后，一致性明显下降。
- **适用条件 / 局限** · 依赖具备充分可见性的全景视频。

**可复用机制** · 对世界模型按不可见持续时间分桶，独立测重新出现的物体状态。

<a id="paper-155822"></a>

## Can Circuit Alignment Predict OOD Generalization?

[官方论文页](https://neurips.cc/virtual/2026/poster/155822) · [作者来源](https://openreview.net/forum?id=2cBK6cvSiw)

- **问题 / 瓶颈** · 激活相似度可能看不到结构改路。
- **核心创新 / 方法** · 通过图核比较类别电路，区分同类一致和跨类混淆。
- **Baseline** · CKA、SVCCA、RSA。
- **Benchmark** · PACS 上的 48 个学习器，测预测排名与跨域精度的相关性。
- **关键结果 / 消融** · CAS 相关性为 0.88，三个对照分别为 0.58、0.23、0.14。
- **适用条件 / 局限** · 一致性结论依赖领域采样设定和电路构造。

**可复用机制** · 跨域选模型时对照电路及激活指标，并报告域采样预算。

<a id="paper-154679"></a>

## Can Entry-Wise Clipping Give Spectral Control of Stochastic Gradients?

[官方论文页](https://neurips.cc/virtual/2026/poster/154679) · [作者来源](https://openreview.net/forum?id=BoiVQ3v6kN)

- **问题 / 瓶颈** · 向量裁剪忽略矩阵结构，谱操作成本较高。
- **核心创新 / 方法** · 在局部化条件下分析逐元素操作与谱归一化的关系，构造平滑估计。
- **Baseline** · Adam、Muon 以及谱归一化。
- **Benchmark** · NanoGPT 预训练的训练 token 效率，含柯西污染理论。
- **关键结果 / 消融** · 较 Adam 约节省 8% token，叠加在 Muon 上约节省 2%。
- **适用条件 / 局限** · 谱等效依赖局部化条件，规模外推待测。

**可复用机制** · 在固定损失目标下将逐元素收缩和矩阵归一化拆开做消融。

<a id="paper-149399"></a>

## Can Hybrid-Parallel Planning Support Alternating Model–Strategy Design? Dependency-Keyed Per-Layer Primitives for Re-Planning

[官方论文页](https://neurips.cc/virtual/2026/poster/149399) · [作者来源](https://openreview.net/forum?id=qLgijcuHlO)

- **问题 / 瓶颈** · 每次修改模型后重搜耗时，盲目缓存可能改变可行集合。
- **核心创新 / 方法** · 通信、显存和时间原语公开输入依赖，根据值签名决定复用。
- **Baseline** · 禁用缓存的完整搜索与专家调优 Megatron 风格方案。
- **Benchmark** · 256 至 4096 卡多个 MoE 配置和长上下文设置。
- **关键结果 / 消融** · 热重算中位快 2.74 倍，54 个配对设置的最优计划一致。
- **适用条件 / 局限** · 依赖原语完整声明依赖及签名。

**可复用机制** · 训练计划缓存用依赖失效检查，并与冷启动逐一核对可行集和最优计划。

<a id="paper-151481"></a>

## Can In-Context Learning Support Intrinsic Curiosity?

[官方论文页](https://neurips.cc/virtual/2026/poster/151481) · [作者来源](https://openreview.net/forum?id=aHSKeImV3Z)

- **问题 / 瓶颈** · 传统好奇心奖励需要在线更新世界模型。
- **核心创新 / 方法** · 用上下文反事实和预测误差估计学习进展，并分析可识别性。
- **Baseline** · 内循环学习进展与不更新的上下文奖励。
- **Benchmark** · 连续与符号环境，覆盖主动学习和实验设计分析。
- **关键结果 / 消融** · 一般 MDP 中不能无偏实现，部分非时序设定可收敛。
- **适用条件 / 局限** · 正面结论不能外推到任意时序探索任务。

**可复用机制** · 先确定数据选择是否涉及行动改变未来分布，再决定用免更新代理奖励。

<a id="paper-153028"></a>

## Can Language Models Actually Retrieve In-Context? Drowning in Documents at Million Token Scale

[官方论文页](https://neurips.cc/virtual/2026/poster/153028) · [作者来源](https://openreview.net/forum?id=OYj8yMVkLx)

- **问题 / 瓶颈** · 无关文档抬高 softmax 分母，即使相关文档原始分数不变也可能失检。
- **核心创新 / 方法** · 比较长度感知归一化与文档稀疏注意力。
- **Baseline** · BlockSearch、MSA 及稠密检索。
- **Benchmark** · 百万 token 和超训练长度检索。
- **关键结果 / 消融** · BlockSearch 可外推约十倍但极长时失效，调整后与稠密检索相近。
- **适用条件 / 局限** · 稀疏选择仍可能漏掉候选，跨领域边界待核。

**可复用机制** · 同时记录相关文档的原始分数与归一化质量，定位长上下文失败。

<a id="paper-150242"></a>

## Can LLMs explain themselves truthfully with code?

[官方论文页](https://neurips.cc/virtual/2026/poster/150242) · [作者来源](https://openreview.net/forum?id=jg5HryRQQg)

- **问题 / 瓶颈** · 文本解释难执行和量化。
- **核心创新 / 方法** · 采样多段可执行解释并按行为一致性选择。
- **Baseline** · 自由文本解释及随机一致性参考。
- **Benchmark** · 三个开源代码模型、八项不同难度语言任务。
- **关键结果 / 消融** · 复杂任务一致性常接近随机，内部表示也不能可靠预判。
- **适用条件 / 局限** · 匹配输出不证明解释忠实于内部计算。

**可复用机制** · 将可执行解释放到独立数据上测试，单独报告复杂样本和硬编码依赖。

<a id="paper-152833"></a>

## Can Metadata Fix the Gauge? Calibration Turns Sparse Multi-Source Learning from Sparse PCA into Sparse Mean Recovery

[官方论文页](https://neurips.cc/virtual/2026/poster/152833) · [作者来源](https://openreview.net/forum?id=Q5Hpa44zeJ)

- **问题 / 瓶颈** · 来源标签不能恢复坐标方向，直接汇总抹去均值信号。
- **核心创新 / 方法** · 用元数据同步来源符号，以对齐质量衡量恢复的一阶信号量。
- **Baseline** · 仅来源标签以及错误校准信息。
- **Benchmark** · 多源稀疏高斯设定及施加坐标变换的真实特征。
- **关键结果 / 消融** · 理论区分稀疏 PCA 和稀疏均值恢复，实验验证相变与复用。
- **适用条件 / 局限** · 依赖有效且任务独立的相对校准。

**可复用机制** · 合并异构数据时用共享校准图恢复方向，先做错误元数据对照。

<a id="paper-154631"></a>

## Canonical Predictive Quotients: A Theory of Prediction under Hidden Predictive State Uncertainty with ICL Implications

[官方论文页](https://neurips.cc/virtual/2026/poster/154631) · [作者来源](https://openreview.net/forum?id=C9jkpSSGyn)

- **问题 / 瓶颈** · 完整隐态识别可能超出预测所需。
- **核心创新 / 方法** · 按查询对应的贝叶斯最优行为划分隐状态，推导保留适应收益的商表示。
- **Baseline** · 状态感知 oracle 和折叠高斯参考。
- **Benchmark** · 有限状态与线性高斯精确例，以及预训练上下文预测器测试。
- **关键结果 / 消融** · 论文给出收益从零到正的边界与可保留完整收益的条件。
- **适用条件 / 局限** · 依赖预测损失及隐态模型。

**可复用机制** · 为上下文适配构造只改变预测决策的状态标签并测 oracle 差距。

<a id="paper-154204"></a>

## Canopy: Tree-Aware Rollout Scheduling for Agent Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/154204) · [作者来源](https://openreview.net/forum?id=FPJ4b4JwEE)

- **问题 / 瓶颈** · 独立调度兄弟分支易重复预填充和释放共享前缀。
- **核心创新 / 方法** · 共置共享前缀、单独抢占私有后缀并比较迁移和重算成本。
- **Baseline** · 树不可见调度与原有四种树 rollout 算法。
- **Benchmark** · 多轮长时程 Agent rollout，衡量速度和前缀失效。
- **关键结果 / 消融** · 作者报告生成加速最高 2.11 倍，共享前缀完全释放平均减少 51.1%。
- **适用条件 / 局限** · 依赖前缀共享度及通信开销估计。

**可复用机制** · 缓存生命周期按共享和私有部分拆分，并按负载比较重算与迁移。

<a id="paper-149781"></a>

## Can the Parts Fool the Test? Counterfactual Pairing Cycles for Relational OOD

[官方论文页](https://neurips.cc/virtual/2026/poster/149781) · [作者来源](https://openreview.net/forum?id=nLCr7f3CZV)

- **问题 / 瓶颈** · 常见负例可被单模态捷径区分。
- **核心创新 / 方法** · 两图两文组成配对循环，使单模态与可加性捷径抵消。
- **Baseline** · 常规负例和快捷验证 AUROC 选模。
- **Benchmark** · 合成控制、GQA 和 COCO 的关系 OOD。
- **关键结果 / 消融** · COCO 压力测试中循环训练将 CycleAcc 从 0.576 提至 0.911。
- **适用条件 / 局限** · 需要可交换且语义可靠的反事实配对。

**可复用机制** · 对跨模态耦合声明加入配对交换对照，固定两端边际。

<a id="paper-148170"></a>

## CanvasMAR: Improving Masked Autoregressive Video Prediction With Canvas

[官方论文页](https://neurips.cc/virtual/2026/poster/148170) · [作者来源](https://openreview.net/forum?id=znXlOaeZCI)

- **问题 / 瓶颈** · 少步掩码自回归采样难形成整体结构。
- **核心创新 / 方法** · 以单步未来期望帧构造非均匀画布，按运动大小先静后动合成。
- **Baseline** · 既有掩码自回归及扩散视频方法。
- **Benchmark** · BAIR、UCF-101、Kinetics-600，比较质量和采样步数。
- **关键结果 / 消融** · 作者报告用更少步骤提高质量。
- **适用条件 / 局限** · 粗画布错误可能传播，独立模块贡献待核。

**可复用机制** · 固定步数对照全局粗预测及运动感知补全顺序。

<a id="paper-151128"></a>

## CanViT: Toward Active-Vision Foundation Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151128) · [作者来源](https://openreview.net/forum?id=cnV9GA4pKU)

- **问题 / 瓶颈** · 顺序局部观察既需要全局整合，也要求低增量开销。
- **核心创新 / 方法** · 用场景相对位置编码和非对称注意力写入记忆，用随机观察序列蒸馏全景教师。
- **Baseline** · 既有主动视觉模型和计算量或输入匹配的 DINOv3。
- **Benchmark** · ADE20K 分割和 ImageNet-1k 分类。
- **关键结果 / 消融** · 冻结单次观察 38.5% mIoU，多次达 45.9%。
- **适用条件 / 局限** · 依赖蒸馏教师，训练数据量与结构作用须区分。

**可复用机制** · 固定观察预算比较全局记忆与重算，并扫描观察次数。

<a id="paper-139187"></a>

## Can VLMs Reason When to Stop for Human Safety?

[官方论文页](https://neurips.cc/virtual/2026/poster/139187) · [作者来源](https://openreview.net/forum?id=fkR4UeSeRN)

- **问题 / 瓶颈** · 识别已发生危险不等同于预测并主动停止。
- **核心创新 / 方法** · 用匹配视频同时评估风险预判和安全优先决策。
- **Baseline** · 21 个视觉语言模型，模型名称待核。
- **Benchmark** · VESPER 的 458 段安全与危险配对视频。
- **关键结果 / 消融** · 作者报告当前模型仍难作出正确继续或停止决定。
- **适用条件 / 局限** · 视频判断不等于实体系统安全认证。

**可复用机制** · 分别报告危险场景漏停和安全场景误停，避免整体准确率掩盖取舍。

<a id="paper-139287"></a>

## Can We Trust Item Response Theory for AI Evaluation?

[官方论文页](https://neurips.cc/virtual/2026/poster/139287) · [作者来源](https://openreview.net/forum?id=ZKNcOHJwjy)

- **问题 / 瓶颈** · AI 基准常有很少的模型和大量题目，违反估计器熟悉的应用条件。
- **核心创新 / 方法** · 从真实基准提取参数，模拟能力分布与响应并比较四类估计器。
- **Baseline** · 边际极大似然、MCMC、变分与神经估计器。
- **Benchmark** · 六个基准派生设定，三个 IRT 模型，1.8 万次模拟。
- **关键结果 / 消融** · 经典方案可能不可计算，可扩展方案在小或非正态样本时排序和题级推断可能失真。
- **适用条件 / 局限** · 仿真覆盖有限，实际模型依赖可能更复杂。

**可复用机制** · 在使用估计难度选题前检查排序稳定性和预测误差随样本量的变化。

<a id="paper-148802"></a>

## Capacity Allocation at the Source: Sparse Target Optimization for LLM Knowledge Editing

[官方论文页](https://neurips.cc/virtual/2026/poster/148802) · [作者来源](https://openreview.net/forum?id=v1KYgyV6TY)

- **问题 / 瓶颈** · 只优化参数写入忽略了编辑目标本身对容量的竞争。
- **核心创新 / 方法** · 分析目标向量干扰和参数干扰的联系，对目标向量加 L1 正则。
- **Baseline** · 现有两阶段知识编辑及无目标正则版本。
- **Benchmark** · 多模型知识编辑基准，具体数据和指标待核。
- **关键结果 / 消融** · 作者报告稀疏目标有助于多编辑共存。
- **适用条件 / 局限** · 正则过强会损伤编辑表达，跨方法边界待核。

**可复用机制** · 固定参数更新规则，对照稠密与稀疏编辑目标并同时测旧知识保持。

<a id="paper-151561"></a>

## Capacity-Constrained Online Convex Optimization with Delayed Feedback

[官方论文页](https://neurips.cc/virtual/2026/poster/151561) · [作者来源](https://openreview.net/forum?id=ZgUQ4y3khF)

- **问题 / 瓶颈** · 超过容量后反馈丢失，延迟又不可提前知道。
- **核心创新 / 方法** · 把容量限制转化为带权延迟在线优化，用 FTRL 及其赌博机版本分析。
- **Baseline** · 无限追踪容量和惯用延迟优化速率。
- **Benchmark** · 凸或强凸损失，一阶与赌博机反馈的理论设定。
- **关键结果 / 消融** · 一阶情形对数容量可恢复标准速率至对数因子，赌博机退化受峰值积压与容量比影响。
- **适用条件 / 局限** · 需要在线察觉到期并符合分析假设。

**可复用机制** · 根据反馈模式分别设计追踪预算，并用随机化防止调度采样偏差。

<a id="paper-149623"></a>

## CAPER: Clause-Aligned Process Supervision for Text-to-SQL

[官方论文页](https://neurips.cc/virtual/2026/poster/149623) · [作者来源](https://openreview.net/forum?id=oj9P3hyKy9)

- **问题 / 瓶颈** · 执行成功只提供末端信号，逐 token 标签可能惩罚等价查询。
- **核心创新 / 方法** · 用 AST 子句级对照导出监督，训练子句奖励模型用于候选核验及策略优化。
- **Baseline** · GPT-5.4 等对照，具体设置待核。
- **Benchmark** · BIRD、Spider 和留出失败集合，测执行准确率及定位。
- **关键结果 / 消融** · 执行准确率最高相对提升 15.3%，定位准确率 84.53%、MRR 90.60%。
- **适用条件 / 局限** · 依赖结构化语法与可执行核验，等价性仍需验证。

**可复用机制** · 对程序生成把监督边界放在语义决策单位，并分开评估执行和定位。

<a id="paper-149769"></a>

## CAPO: A Primal-Dual Framework for Constraint-Aware Prompt Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/149769) · [作者来源](https://openreview.net/forum?id=nS6hVWW0JO)

- **问题 / 瓶颈** · 仅提高任务分数可能忽略成本、格式和策略约束。
- **核心创新 / 方法** · 用原始对偶方法在目标和约束间动态调整权重，并蒸馏反馈改写器。
- **Baseline** · 原提示优化方法及非摊销 CAPO，具名基线待核。
- **Benchmark** · 三个 Agent 基准及助手格式和隐私安全评测。
- **关键结果 / 消融** · 作者报告更常达到经验可行解，改写器保持准确率并改善权衡。
- **适用条件 / 局限** · 经验达标不代表分布外保证；需量化约束。

**可复用机制** · 把任务成功和约束通过率分别报告，并扫描可行阈值。

<a id="paper-138881"></a>

## CapTrack: Multifaceted Evaluation of Forgetting in LLM Post-Training

[官方论文页](https://neurips.cc/virtual/2026/poster/138881) · [作者来源](https://openreview.net/forum?id=yznJFH0LsX)

- **问题 / 瓶颈** · 单看事实准确率遗漏默认行为变化
- **核心创新 / 方法** · 构建能力分类和专属指标
- **Baseline** · 指令微调与偏好优化
- **Benchmark** · 多模型族、领域和算法，最大80B
- **关键结果 / 消融** · 稳健性与默认行为明显漂移，偏好优化可部分恢复能力
- **适用条件 / 局限** · 任务与模型覆盖限定外推

**可复用机制** · 分别测事实、稳健性和默认行为，比较不同训练阶段

<a id="paper-149094"></a>

## Capturing In-Context Learning Dynamics with Task Operators

[官方论文页](https://neurips.cc/virtual/2026/poster/149094) · [作者来源](https://openreview.net/forum?id=sx3XAheEWd)

- **问题 / 瓶颈** · 固定向量忽略任务与输入的交互
- **核心创新 / 方法** · 把注意力头的带上下文输出写成屏蔽上下文后的仿射变换，并折入输出投影
- **Baseline** · 固定激活向量与完整上下文学习
- **Benchmark** · 词汇、算法和推理任务
- **关键结果 / 消融** · 报告缩小零样本与完整上下文差距
- **适用条件 / 局限** · 依赖任务内仿射参数稳定

**可复用机制** · 测试投影更新能否替代重复处理演示

<a id="paper-148906"></a>

## Capturing LLM Capabilities via Evidence-Calibrated Query Clustering

[官方论文页](https://neurips.cc/virtual/2026/poster/148906) · [作者来源](https://openreview.net/forum?id=uHwV5V8KiK)

- **问题 / 瓶颈** · 语义相似不保证考查相同能力
- **核心创新 / 方法** · 用有限模型比较校准嵌入，以Bradley–Terry能力轮廓和混合权重描述各题
- **Baseline** · 人工类别和语义嵌入
- **Benchmark** · 能力排名与查询路由
- **关键结果 / 消融** · 排名质量分别提高17.64和18.02个百分点
- **适用条件 / 局限** · 依赖校准模型与查询的代表性

**可复用机制** · 先测一小组模型的相对表现，再决定评测题如何分组

<a id="paper-150315"></a>

## Cardinality-Decomposed Loss for Heterogeneous GNNs

[官方论文页](https://neurips.cc/virtual/2026/poster/150315) · [作者来源](https://openreview.net/forum?id=j0w8m1D6QO)

- **问题 / 瓶颈** · 统一排序损失可隐藏属性嵌入塌缩
- **核心创新 / 方法** · 对不同关系使用交叉熵和BPR，检查共享编码器中的目标冲突
- **Baseline** · 统一BPR
- **Benchmark** · 五个数据集，测排序及表征，细项待核
- **关键结果 / 消融** · 作者发现排序不变时属性几何仍可退化
- **适用条件 / 局限** · 适配其他基数及梯度权重待核

**可复用机制** · 分关系测表示质量和梯度方向，避免只看推荐排名

<a id="paper-152838"></a>

## CARD: Internalizing Expert Critique into Reinforcement Learning for Deep Search

[官方论文页](https://neurips.cc/virtual/2026/poster/152838) · [作者来源](https://openreview.net/forum?id=Q15eHqL9AR)

- **问题 / 瓶颈** · 终局奖励无法指出哪步需修正
- **核心创新 / 方法** · 屏蔽直接复述评论的token，提升修正token权重，并蒸馏评论有效的无评论轨迹
- **Baseline** · 基础GRPO
- **Benchmark** · 长程深度搜索，具名设置待核
- **关键结果 / 消融** · 作者提出两种互补训练信号，量化待核
- **适用条件 / 局限** · 需要可校验且有用的评论

**可复用机制** · 把反馈复述和反馈驱动的修正分开监督

<a id="paper-151526"></a>

## CARVE: Counterfactual Video Editing for Auditing and Hardening Video Detectors

[官方论文页](https://neurips.cc/virtual/2026/poster/151526) · [作者来源](https://openreview.net/forum?id=a0f5OM9rop)

- **问题 / 瓶颈** · 观测划分下的高AUC可能来自环境
- **核心创新 / 方法** · 为同一视频构造环境和事件独立变化的四元组并过滤编辑结果
- **Baseline** · 常规观测划分与检测模型
- **Benchmark** · 视频事件检测，报告阈值和连续分数
- **关键结果 / 消融** · 可分辨环境引起的漂移和事件响应，定量待核
- **适用条件 / 局限** · 编辑质量与因子控制仍需检查

**可复用机制** · 联合报告阈值性能和连续响应，以免统一降分伪装成鲁棒

<a id="paper-152013"></a>

## CASAM: Consistency-Anchored Sharpness-Aware Minimization for Improved Model Generalization

[官方论文页](https://neurips.cc/virtual/2026/poster/152013) · [作者来源](https://openreview.net/forum?id=WABAB6cGkw)

- **问题 / 瓶颈** · 平坦度指标不总预测泛化
- **核心创新 / 方法** · 分析批次扰动下预测KL及梯度项，并按梯度一致性重加权
- **Baseline** · SAM及其他优化对照待全文核实
- **Benchmark** · 泛化实验，具名设置待核
- **关键结果 / 消融** · 作者观察到一致性随训练下降
- **适用条件 / 局限** · 额外梯度成本及异常样本影响待核

**可复用机制** · 匹配算力比较按梯度一致性加权和仅选困难样本

<a id="paper-151133"></a>

## Cascaded Sparse Autoencoders LearnMulti-Level Visual Concepts in Multimodal LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/151133) · [作者来源](https://openreview.net/forum?id=cl4vXMku1D)

- **问题 / 瓶颈** · 平坦字典难显式组织概念层级
- **核心创新 / 方法** · 第二层SAE直接编码第一层解码器权重
- **Baseline** · 嵌套和堆叠SAE
- **Benchmark** · Qwen3-VL、Gemma-3、LLaVA的视觉概念
- **关键结果 / 消融** · 作者报告层级概念一致性改善
- **适用条件 / 局限** · 层级连贯性不等同于因果解释

**可复用机制** · 对照编码字典方向与编码激活在层级组织上的差异

<a id="paper-149782"></a>

## Casper: A Projection-Based Neurosymbolic Layer for Scalable & Guaranteed Constraint Satisfaction

[官方论文页](https://neurips.cc/virtual/2026/poster/149782) · [作者来源](https://openreview.net/forum?id=nKVmBxaagL)

- **问题 / 瓶颈** · 精确搜索难扩展，近似方法可输出无效解
- **核心创新 / 方法** · 将输出通过闭式欧氏投影映射到约束可行域
- **Baseline** · 精确与近似求解方法
- **Benchmark** · MNIST算术、数独和Warcraft寻路
- **关键结果 / 消融** · 30×30寻路中有效率100%，近似对照低于7%，精确对照超时
- **适用条件 / 局限** · 保证适用的约束类别需全文核实

**可复用机制** · 在支持投影的问题上同时报告有效率、延迟和任务质量

<a id="paper-150932"></a>

## CASPIAN: Online Detection and Attribution of Cascade Attacks in LLM Multi-Agent Systems via Cross-Channel Causal Monitoring

[官方论文页](https://neurips.cc/virtual/2026/poster/150932) · [作者来源](https://openreview.net/forum?id=eERJSSfRu8)

- **问题 / 瓶颈** · 单看局部文本可能漏掉系统级异常
- **核心创新 / 方法** · 在线估计跨渠道影响，定位异常传播中的不同角色
- **Baseline** · 局部与文本监测方案
- **Benchmark** · 多智能体系统的在线检测及归因
- **关键结果 / 消融** · 摘要报告能够检测传播起点并执行归因
- **适用条件 / 局限** · 统计影响不自动证明因果，需要验证

**可复用机制** · 防御审计应对比单信号和多信号告警，并检查定位误判

<a id="paper-155150"></a>

## CAST: Causal Anchored Simplex Transport for Distribution-Valued Time Series

[官方论文页](https://neurips.cc/virtual/2026/poster/155150) · [作者来源](https://openreview.net/forum?id=7wHSu87prc)

- **问题 / 瓶颈** · 相同聚合分布在不同状态下可能走向不同
- **核心创新 / 方法** · 按历史上下文检索转移后继，用持续性锚点和局部随机传输保持概率单纯形
- **Baseline** · 仅依赖混叠摘要的预测器
- **Benchmark** · 分布值在线预测，以加权JS风险分析
- **关键结果 / 消融** · 给出忽略转移上下文时不可消除的超额风险界
- **适用条件 / 局限** · 有序支持与历史样本覆盖影响复用

**可复用机制** · 构造同观测异机制的配对测试，并检查约束保持

<a id="paper-151249"></a>

## CAST: Certifiable Aggregation of Smoothed Teachers for Robust Policy Adaptation

[官方论文页](https://neurips.cc/virtual/2026/poster/151249) · [作者来源](https://openreview.net/forum?id=bmqxbwQYk6)

- **问题 / 瓶颈** · 奖励变更使源策略证书不能直接复用
- **核心创新 / 方法** · 无需重训练聚合多个平滑教师，并分别认证动作和累计奖励
- **Baseline** · 通常需目标侧再训练的迁移方法
- **Benchmark** · 强化学习策略迁移及稳健性认证
- **关键结果 / 消融** · 作者提出动作和累计回报双层证书，细项待核
- **适用条件 / 局限** · 证书依赖威胁模型及教师条件

**可复用机制** · 迁移控制时分别审核单步决策证书和累计回报证书

<a id="paper-139489"></a>

## Castle-in-the-Air: Probing the Foundational Visual Deficits of MLLMs via Bottom-Up Cognitive Factors

[官方论文页](https://neurips.cc/virtual/2026/poster/139489) · [作者来源](https://openreview.net/forum?id=MxjxPW0HSQ)

- **问题 / 瓶颈** · 复杂任务表现可能掩盖低层视觉缺陷
- **核心创新 / 方法** · 将认知测验数字化并自动生成可验证的难度变体
- **Baseline** · 39个前沿多模态模型
- **Benchmark** · VisFactor的20项视觉子测验
- **关键结果 / 消融** · 最高55.9%，心理旋转及图形背景分离等仍失败
- **适用条件 / 局限** · 测验的人类构念与机器失效机制不必一致

**可复用机制** · 对视觉模型分解测试基础技能，并记录随难度变化的失效曲线

<a id="paper-152630"></a>

## Catch Your Breath: Adaptive Computation for Self-Paced Sequence Production

[官方论文页](https://neurips.cc/virtual/2026/poster/152630) · [作者来源](https://openreview.net/forum?id=RfZGk8kzTr)

- **问题 / 瓶颈** · 固定暂停步不能表达就绪程度
- **核心创新 / 方法** · 把暂停建模为顺序决策并用专门监督损失训练
- **Baseline** · 末步交叉熵
- **Benchmark** · 预训练和微调的困惑度与任务准确率
- **关键结果 / 消融** · 作者报告两指标改善
- **适用条件 / 局限** · 计算预算与任务细节待核

**可复用机制** · 固定预算对照学习暂停与固定暂停

<a id="paper-154883"></a>

## CATS: Acceptance-Oriented Critical Token Adaptive Selection for Multimodal Speculative Decoding

[官方论文页](https://neurips.cc/virtual/2026/poster/154883) · [作者来源](https://openreview.net/forum?id=AAzuOWs11n)

- **问题 / 瓶颈** · 全局对齐忽略误差集中结构
- **核心创新 / 方法** · 先全局训练草稿模型，再精调两类关键 token 的并集
- **Baseline** · EAGLE-2 和监督微调
- **Benchmark** · 三个基准，LLaVA 与 Qwen2.5-VL，测接受率与速度
- **关键结果 / 消融** · 最高报告 3.05 倍加速
- **适用条件 / 局限** · 依赖关键 token 识别与目标骨干

**可复用机制** · 按拒绝原因分桶优化草稿模型

<a id="paper-155095"></a>

## Causal Attribution via Activation Patching

[官方论文页](https://neurips.cc/virtual/2026/poster/155095) · [作者来源](https://openreview.net/forum?id=8SdGwDmfly)

- **问题 / 瓶颈** · 输入扰动或注意力只是间接代理
- **核心创新 / 方法** · 把源图块激活移植到中性目标上下文，以类别分数估计贡献
- **Baseline** · 梯度、注意力及扰动归因
- **Benchmark** · 多种 ViT 与标准定位指标
- **关键结果 / 消融** · 作者报告定位和忠实性改善
- **适用条件 / 局限** · 取决于中性上下文与层段选择

**可复用机制** · 扫描移植层段并报告定位和忠实性

<a id="paper-154338"></a>

## CausalCine: Real-Time Autoregressive Generation for Multi-Shot Video Narratives

[官方论文页](https://neurips.cc/virtual/2026/poster/154338) · [作者来源](https://openreview.net/forum?id=ELwIR2S82B)

- **问题 / 瓶颈** · 只保留近期帧易导致跨镜头漂移
- **核心创新 / 方法** · 训练真实多镜头的因果底座，按相关性检索历史缓存并蒸馏
- **Baseline** · 自回归及双向视频模型
- **Benchmark** · 多镜头流式视频生成，具名数据及指标待核
- **关键结果 / 消融** · 报告优于自回归对照且接近双向模型
- **适用条件 / 局限** · 依赖多镜头训练数据及缓存预算

**可复用机制** · 固定记忆容量比较按内容和按时间选缓存

<a id="paper-139526"></a>

## CausalCompass: Evaluating the Robustness of  Time-Series Causal Discovery in Misspecified Scenarios

[官方论文页](https://neurips.cc/virtual/2026/poster/139526) · [作者来源](https://openreview.net/forum?id=KYrd3OXJlO)

- **问题 / 瓶颈** · 单一假设下排名不能代表稳健性
- **核心创新 / 方法** · 逐项改变时序因果发现的建模假设
- **Baseline** · 代表性时序因果发现算法，含 NTS-NOTEARS
- **Benchmark** · 八种违背场景和超参敏感性
- **关键结果 / 消融** · 无方法始终最优，NTS-NOTEARS 对标准化敏感
- **适用条件 / 局限** · 结论受场景覆盖与调参协议限制

**可复用机制** · 把预处理作为实验变量纳入横向比较
