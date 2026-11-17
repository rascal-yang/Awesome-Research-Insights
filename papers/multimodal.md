# 多模态学习

[首页](../README.md) · [参与贡献](../CONTRIBUTING.md) · [English](../en/papers/multimodal.md)

结合图像、文本、音频等模态进行学习。

<!-- classification:start -->
## 按技术类型浏览

<a id="by-architecture"></a>

### 模型架构

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="bai26j-architecture"></a>[Interactive Person Retrieval via Multi-Turn Multimodal Conversation](https://proceedings.mlr.press/v306/bai26j.html) | 交互式人物检索 | 允许用户针对返回图像指出与目标不同的视觉属性，先逐轮编码反馈，再聚合历史记忆逐步修正检索结果。 |

<a id="by-modules"></a>

### 模块

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="barrios26a-modules"></a>[MoDA: Modulation Adapter for Fine-Grained Visual Understanding in Instructional MLLMs](https://proceedings.mlr.press/v306/barrios26a.html) | 细粒度视觉定位 | 用指令和对齐后的视觉特征做交叉注意力，生成逐通道乘法掩码，可在每个 patch 内放大与当前指令有关的特征。 |
| <a id="chen26ch-modules"></a>[Hamiltonian Asymmetric Fusion: One-Way Safe Directed Refinement under Modality Imbalance](https://proceedings.mlr.press/v306/chen26ch.html) | 非对称 RGB-D 特征融合 | 用主模态的频域相关性引导辅助特征，并用门控动量反复更新辅助查询。将主模态输出中的辅助残差系数设为零，可在该融合块内切断辅助噪声的回流。 |

<a id="by-loss-functions"></a>

### 损失函数

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="chefer26a-loss-functions"></a>[Self-Supervised Flow Matching for Scalable Multi-Modal Synthesis](https://proceedings.mlr.press/v306/chefer26a.html) | 自监督流匹配 | 让同一样本中不同 token 承受不同噪声程度，使低噪 token 为高噪 token 提供可学习的语义线索，在生成训练中一并学习表征。 |
| <a id="chen26au-loss-functions"></a>[Do-Prompt: Causal Interventions Meet Variational Prompt Bottlenecks](https://proceedings.mlr.press/v306/chen26au.html) | 多模态提示泛化 | 先用变分瓶颈限制可学习提示的容量，再扰动提示中与环境有关的成分并要求输出一致，减少迁移时对训练域捷径的依赖。 |
| <a id="chen26bn-loss-functions"></a>[Language Bias in LVLMs: From In-Depth Analysis to Simple and Effective Mitigation](https://proceedings.mlr.press/v306/chen26bn.html) | 视觉指令微调的语言偏差正则 | 在视觉指令微调时，额外惩罚去掉图像后当前模型与参考模型对同一回答的对数概率差。约束纯文本预测的漂移，有助于视觉问答使用图像信息。 |

<a id="by-reinforcement-learning"></a>

### 强化学习方法

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="cao26m-reinforcement-learning"></a>[VideoTrace-R1: Long Video-based Retrieval-Augmented Generation via Reinforcement Learning](https://proceedings.mlr.press/v306/cao26m.html) | 长视频推理奖励 | 把视频事件编成可查询的时间链，用符号验证器给每个中间时间主张单独打分，避免仅凭最终答案正确放过错误的事件顺序。 |
| <a id="chen26bk-reinforcement-learning"></a>[RuCL: Stratified Rubric-Based Curriculum Learning for Multimodal Large Language Model Reasoning](https://proceedings.mlr.press/v306/chen26bk.html) | 分层评分规则的强化学习课程 | 把可复用的视觉推理评分规则分为基础层和进阶层，与最终答案校验一起组成奖励。等模型在基础规则上表现稳定后再激活进阶规则，逐步把训练重点从感知移到复杂推理。 |

<a id="by-training-strategies"></a>

### 训练策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="alipour-talemi26a-training-strategies"></a>[Hyper-ICL: Attention Calibration with Hyperbolic Anchor Distillation for Multimodal In-Context Learning](https://proceedings.mlr.press/v306/alipour-talemi26a.html) | 多模态上下文学习 | 用带示例的教师监督注意力分布及层间表征，再按当前查询调节低秩适配器的作用强度，把示例效果内化到推理无需示例的学生中。 |
| <a id="asadollahzadeh26a-training-strategies"></a>[TRACER: Persistent Regularization for Robust Multimodal Finetuning](https://proceedings.mlr.press/v306/asadollahzadeh26a.html) | 多模态微调 | 用加权移动平均教师做持续自蒸馏，在目标任务方向适应的同时，约束正交方向偏离预训练知识。 |
| <a id="buzeta26a-training-strategies"></a>[Seeing to Generalize: How Visual Data Corrects Binding Shortcuts](https://proceedings.mlr.press/v306/buzeta26a.html) | 视觉数据与符号绑定 | 在受控检索任务里，把同一符号数据改写成图像训练可打破位置捷径，学到更稳健的绑定机制，随后切回纯文本也保留收益。 |
| <a id="chen26am-training-strategies"></a>[Gated Relational Alignment via Confidence-based Distillation for Efficient VLMs](https://proceedings.mlr.press/v306/chen26am.html) | 视觉语言蒸馏与量化 | 做量化感知训练时，用教师置信度筛选蒸馏信号，并用中心核对齐保留视觉 token 之间的关系，在受限容量中优先保住任务信息。 |

<a id="by-data-strategies"></a>

### 数据策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="acuna26a-data-strategies"></a>[Long Grounded Thoughts: Synthesizing Visual Problems and Reasoning Chains at Scale](https://proceedings.mlr.press/v306/acuna26a.html) | 数据与后训练 | 视觉推理数据可先根据图像标注构造问题，再用多次 rollout 估计难度并分层检查推理轨迹。 |
| <a id="assouel26a-data-strategies"></a>[PGT: Procedurally Generated Tasks for improving visual grounding in MLLMs](https://proceedings.mlr.press/v306/assouel26a.html) | 视觉定位监督 | 在真实图像上叠加明确的几何图元并程序化生成问题，让模型练习细粒度位置关系，同时降低依赖物体语义猜答案的机会。 |
| <a id="bo26b-data-strategies"></a>[Efficient Multi-modal Dataset Distillation via Analytic Parameter Matching](https://proceedings.mlr.press/v306/bo26b.html) | 多模态数据蒸馏 | 用解析解求模态投影器参数，再匹配教师与学生的投影器，替代双层训练及轨迹匹配。论文中只需缓存两个矩阵。 |
| <a id="cao26aa-data-strategies"></a>[Learning to Label: A Reinforced Self-Evolving Framework for Semi-supervised Referring Expression Segmentation](https://proceedings.mlr.press/v306/cao26aa.html) | 弱监督指代分割 | 把多模态模型产出的软掩码当候选，依据语言先验和当前分割预测训练伪标签选择器，让分割器和监督信号相互更新。 |
| <a id="chai26b-data-strategies"></a>[From Diagrams to Code: Multilingual Programming with Visual Design](https://proceedings.mlr.press/v306/chai26b.html) | 图解到代码 | 用多种编程语言的图解和文本指令做联合微调，并设置相应的多语言视觉编程基准，检验模型能否跨语言解释设计。 |
| <a id="chen26c-data-strategies"></a>[OpenGPT-4o-Image: A Comprehensive Dataset for Advanced Image Generation and Editing](https://proceedings.mlr.press/v306/chen26c.html) | 多模态图像编辑数据 | 先定义编辑操作、科学图示和文字渲染等分层任务，再从各分支合成多步骤指令图像对，能按能力覆盖定向扩充数据。 |

<a id="by-inference"></a>

### 推理策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="alshehri26a-inference"></a>[Similarity Is Not Logic: Factored Inference for Dual-Encoder Vision-Language Models](https://proceedings.mlr.press/v306/alshehri26a.html) | 视觉语言检索 | 用冻结双编码器给各个概念打分，再在外部显式执行与、或、非等约束，绕开整体相似度容易平均概念证据的问题。 |
| <a id="arora26a-inference"></a>[Stream RAG: Instant and Accurate Spoken Dialogue Systems with Streaming Tool Usage](https://proceedings.mlr.press/v306/arora26a.html) | 流式语音工具调用 | 用户还在说话时并行预测检索查询，并分别训练工具触发时机和检索结果的语音总结，以缩短答复等待时间。 |
| <a id="avogaro26a-inference"></a>[SPARC: Separating Perception And Reasoning Circuits for Test-time Scaling of VLMs](https://proceedings.mlr.press/v306/avogaro26a.html) | 视觉推理预算 | 先用低分辨率全局搜索定位相关区域，再对少数区域用高分辨率处理并推理。感知和推理的测试预算可以分别分配。 |
| <a id="baek26c-inference"></a>[Diagnosing and Correcting Concept Omission in Multimodal Diffusion Transformers](https://proceedings.mlr.press/v306/baek26c.html) | 文本到图像生成 | 在文本 token 隐状态中线性探测概念遗漏信号，再沿该信号干预激活，可在生成时减少指令中的对象或属性被漏画。 |
| <a id="bai26b-inference"></a>[Two Modalities Are Better Than One: Efficient Adversarial Purification via Multimodal Diffusion Models](https://proceedings.mlr.press/v306/bai26b.html) | 扩散对抗净化 | 从干净样本学习类别无关的连续提示词，用它约束少量 DDPM 优化步，使净化后的图像保留语义。 |
| <a id="bai26d-inference"></a>[Let Language Constrain Geometry: Vision–Language Models as Semantic and Spatial Critics for 3D Generation](https://proceedings.mlr.press/v306/bai26d.html) | 三维生成引导 | 分别询问 VLM 语义与空间一致性问题，将 Yes/No 对数赔率作为可微评价，可以接入优化式生成或测试时的采样引导。 |
| <a id="bi26d-inference"></a>[Does Reasoning Improve Seeing? Understanding When Vision-Language Models Benefit from Thinking](https://proceedings.mlr.press/v306/bi26d.html) | 视觉语言推理控制 | 分别缩放较浅层的长度控制头与较深层的推理头，可以在测试时分开调节回答长度和感知与推理的取舍。 |
| <a id="chen26m-inference"></a>[Task-Aware Structured Memory for Dynamic Multi-modal In-Context Learning](https://proceedings.mlr.press/v306/chen26m.html) | 多模态上下文记忆 | 用任务级方向压缩示例，通过二分图匹配合并语义相近的 token，再把记忆分为常驻核心和按查询取用的潜变量库。 |
| <a id="chen26bx-inference"></a>[Code2Video: A Code-centric Paradigm for Educational Video Creation](https://proceedings.mlr.press/v306/chen26bx.html) | 教学视频布局修正 | 把渲染画布离散成 6×6 锚点，并维护元素占位与代码行的映射。视觉语言模型检查渲染结果时可据此指出遮挡元素及其新位置，把布局反馈转换为可执行的动画代码编辑。 |

<a id="by-representation-learning"></a>

### 表征学习

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="chen26ag-representation-learning"></a>[Information-Theoretic Disentangled Latent Modeling with Conditional Diffusion for Incomplete Multi-View Clustering](https://proceedings.mlr.press/v306/chen26ag.html) | 不完整多视图聚类 | 用信息论目标拆出共享语义和各视图特有因素，再用 Wasserstein 混合汇聚语义。条件扩散同时读取全局语义和视图因素，补全缺失观测。 |
| <a id="chen26cx-representation-learning"></a>[Beyond Global Alignment: Fine-Grained Motion-Language Retrieval via Pyramidal Shapley-Taylor Learning](https://proceedings.mlr.press/v306/chen26cx.html) | 关节与片段级动作文本对齐 | 把人体动作拆成时间片段和空间关节，用 Shapley–Taylor 交互建模逐级学习它们与词元的对应，让检索分数能够反映整段相似度容易掩盖的局部动作。 |

<a id="by-evaluation"></a>

### 评测与诊断

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="azulay26a-evaluation"></a>[Jailbreaking Vision-Language Models Through the Visual Modality](https://proceedings.mlr.press/v306/azulay26a.html) | 视觉语言安全评测 | 用同一意图在文本和图像中的不同表达配对测安全性。文中发现，模型在文本上已学会的拒绝行为可能无法跨到视觉通道。 |
| <a id="borchmann26a-evaluation"></a>[Strategic Navigation or Stochastic Search? How Agents and Humans Reason Over Document Collections](https://proceedings.mlr.press/v306/borchmann26a.html) | 文档 Agent 评测 | 评测多文档问答时，同时比较答题正确率与检索成本，并与知道相关证据位置的 oracle 对照，以暴露暴力搜索和无效循环。 |
| <a id="bouguerra26a-evaluation"></a>[Less Precise Can Be More Reliable: A Systematic Evaluation of Quantization’s Impact on VLMs Beyond Accuracy](https://proceedings.mlr.press/v306/bouguerra26a.html) | 视觉语言模型量化 | 量化压弱了部分高秩分量，在论文的 CLIP 评测中有时改善校准和噪声鲁棒性。协变量偏移和伪相关要分别测，收益未延伸到这两类问题。 |
| <a id="cao26i-evaluation"></a>[UniPercept: Towards Unified Perceptual-Level Image Understanding across Aesthetics, Quality, Structure, and Texture](https://proceedings.mlr.press/v306/cao26i.html) | 图像感知评测 | 将审美、质量、结构和纹理拆成可评级或可问答的感知任务。细粒度分项能暴露常规分割、定位和描述评测遗漏的能力缺口。 |
| <a id="cao26v-evaluation"></a>[T2AV-Compass: Towards Unified Evaluation for Text-to-Audio-Video Generation](https://proceedings.mlr.press/v306/cao26v.html) | 音视频生成评测 | 同时评估音频和视频的各自质量、信号级跨模态同步，以及复杂指令遵循和真实感，避免单模态分数掩盖声音与画面错位。 |
| <a id="chen26ad-evaluation"></a>[FutureOmni: Evaluating Future Forecasting from Omni-Modal Context for Multimodal LLMs](https://proceedings.mlr.press/v306/chen26ad.html) | 音视频未来预测评测 | 在未来事件出现前截断音视频，再比较全模态与仅视频模型，可以看出未来预测对听觉线索的依赖，尤其是语音丰富场景。 |
| <a id="chen26dh-evaluation"></a>[MVI-Bench: A Comprehensive Benchmark for Evaluating Robustness to Misleading Visual Inputs in LVLMs](https://proceedings.mlr.press/v306/chen26dh.html) | 误导视觉线索的配对评测 | 固定问题和主体语义，配对正常图像与带概念、属性或关系干扰线索的图像，并用两种条件的相对性能下降衡量视觉语言模型的敏感性。 |

<a id="by-theory-statistics"></a>

### 理论与统计

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="cai26o-theory-statistics"></a>[The Geometric Mechanics of Contrastive Representation Learning: Alignment Potentials, Entropic Dispersion, and Cross-Modal Divergence](https://proceedings.mlr.press/v306/cai26o.html) | 跨模态对比学习 | 成对样本高度对齐时，两种模态的边缘分布仍可持续分离。可分别测配对质量与模态间距，避免用一个指标替代另一个。 |
<!-- classification:end -->
