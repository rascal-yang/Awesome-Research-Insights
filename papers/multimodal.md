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
| <a id="chen26go-architecture"></a>[Any2Any: Unified Arbitrary Modality Translation for Remote Sensing](https://proceedings.mlr.press/v306/chen26go.html) | 遥感跨模态的共享潜空间扩散 | 先用配对观测对齐各模态编码器的潜空间，再将源潜变量和加噪目标潜变量拼接后输入共享扩散 Transformer，用源、目标模态标识调制归一化，直接回归干净目标潜变量。一个主干即可用于多个转换方向。 |

<a id="by-modules"></a>

### 模块

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="barrios26a-modules"></a>[MoDA: Modulation Adapter for Fine-Grained Visual Understanding in Instructional MLLMs](https://proceedings.mlr.press/v306/barrios26a.html) | 细粒度视觉定位 | 用指令和对齐后的视觉特征做交叉注意力，生成逐通道乘法掩码，可在每个 patch 内放大与当前指令有关的特征。 |
| <a id="chen26ch-modules"></a>[Hamiltonian Asymmetric Fusion: One-Way Safe Directed Refinement under Modality Imbalance](https://proceedings.mlr.press/v306/chen26ch.html) | 非对称 RGB-D 特征融合 | 用主模态的频域相关性引导辅助特征，并用门控动量反复更新辅助查询。将主模态输出中的辅助残差系数设为零，可在该融合块内切断辅助噪声的回流。 |
| <a id="chen26dv-modules"></a>[SPR: A Structured Prompt Refinement Network for Modality Missing](https://proceedings.mlr.press/v306/chen26dv.html) | 缺失模态的结构化提示 | 根据图像和文本是否可用选择可学习提示，先跨层融合，再聚合相邻提示词元并按缺失状态门控通道，最后把提示注入冻结的 CLIP 主干做分类。 |

<a id="by-loss-functions"></a>

### 损失函数

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="chefer26a-loss-functions"></a>[Self-Supervised Flow Matching for Scalable Multi-Modal Synthesis](https://proceedings.mlr.press/v306/chefer26a.html) | 自监督流匹配 | 让同一样本中不同 token 承受不同噪声程度，使低噪 token 为高噪 token 提供可学习的语义线索，在生成训练中一并学习表征。 |
| <a id="chen26au-loss-functions"></a>[Do-Prompt: Causal Interventions Meet Variational Prompt Bottlenecks](https://proceedings.mlr.press/v306/chen26au.html) | 多模态提示泛化 | 先用变分瓶颈限制可学习提示的容量，再扰动提示中与环境有关的成分并要求输出一致，减少迁移时对训练域捷径的依赖。 |
| <a id="chen26bn-loss-functions"></a>[Language Bias in LVLMs: From In-Depth Analysis to Simple and Effective Mitigation](https://proceedings.mlr.press/v306/chen26bn.html) | 视觉指令微调的语言偏差正则 | 在视觉指令微调时，额外惩罚去掉图像后当前模型与参考模型对同一回答的对数概率差。约束纯文本预测的漂移，有助于视觉问答使用图像信息。 |
| <a id="chen26dq-loss-functions"></a>[AudioChat: Unified Audio Storytelling, Editing, and Understanding with Transfusion Forcing](https://proceedings.mlr.press/v306/chen26dq.html) | 多轮音频编辑的独立加噪 | 把文字推理的自回归损失与音频潜变量的扩散损失联合训练。对同一对话的不同轮音频独立采样加噪时刻，降低模型靠复制上一轮潜变量完成去噪的倾向。 |
| <a id="cheong26a-loss-functions"></a>[FairSSL: Fair Multimodal Self-Supervised Learning](https://proceedings.mlr.press/v306/cheong26a.html) | 可变长多模态样本的公平自监督 | 把每个受试者的可变长模态划成片段后池化，用同一受试者的片段建立跨模态对齐，同时约束受试者内方差和表征的冗余。论文在异质数据上观察到预测性能接近时的群体差距缩小。 |

<a id="by-reinforcement-learning"></a>

### 强化学习方法

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="cao26m-reinforcement-learning"></a>[VideoTrace-R1: Long Video-based Retrieval-Augmented Generation via Reinforcement Learning](https://proceedings.mlr.press/v306/cao26m.html) | 长视频推理奖励 | 把视频事件编成可查询的时间链，用符号验证器给每个中间时间主张单独打分，避免仅凭最终答案正确放过错误的事件顺序。 |
| <a id="chen26bk-reinforcement-learning"></a>[RuCL: Stratified Rubric-Based Curriculum Learning for Multimodal Large Language Model Reasoning](https://proceedings.mlr.press/v306/chen26bk.html) | 分层评分规则的强化学习课程 | 把可复用的视觉推理评分规则分为基础层和进阶层，与最终答案校验一起组成奖励。等模型在基础规则上表现稳定后再激活进阶规则，逐步把训练重点从感知移到复杂推理。 |
| <a id="chen26ed-reinforcement-learning"></a>[OmniVideo-R1: Reinforcing Audio-visual Reasoning with Query Intention and Modality Attention](https://proceedings.mlr.press/v306/chen26ed.html) | 音视频联合推理奖励 | 对同一道题分别用完整音视频、静音视频和纯音频生成答案。当完整输入的答案得分至少等于两个单模态得分时，才发放额外奖励，用于训练依赖联合线索的音视频推理。 |

<a id="by-training-strategies"></a>

### 训练策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="alipour-talemi26a-training-strategies"></a>[Hyper-ICL: Attention Calibration with Hyperbolic Anchor Distillation for Multimodal In-Context Learning](https://proceedings.mlr.press/v306/alipour-talemi26a.html) | 多模态上下文学习 | 用带示例的教师监督注意力分布及层间表征，再按当前查询调节低秩适配器的作用强度，把示例效果内化到推理无需示例的学生中。 |
| <a id="asadollahzadeh26a-training-strategies"></a>[TRACER: Persistent Regularization for Robust Multimodal Finetuning](https://proceedings.mlr.press/v306/asadollahzadeh26a.html) | 多模态微调 | 用加权移动平均教师做持续自蒸馏，在目标任务方向适应的同时，约束正交方向偏离预训练知识。 |
| <a id="buzeta26a-training-strategies"></a>[Seeing to Generalize: How Visual Data Corrects Binding Shortcuts](https://proceedings.mlr.press/v306/buzeta26a.html) | 视觉数据与符号绑定 | 在受控检索任务里，把同一符号数据改写成图像训练可打破位置捷径，学到更稳健的绑定机制，随后切回纯文本也保留收益。 |
| <a id="chen26am-training-strategies"></a>[Gated Relational Alignment via Confidence-based Distillation for Efficient VLMs](https://proceedings.mlr.press/v306/chen26am.html) | 视觉语言蒸馏与量化 | 做量化感知训练时，用教师置信度筛选蒸馏信号，并用中心核对齐保留视觉 token 之间的关系，在受限容量中优先保住任务信息。 |
| <a id="chen26gr-training-strategies"></a>[Beyond Next-Token Alignment: Distilling Multimodal Large Language Models via Token Interactions](https://proceedings.mlr.press/v306/chen26gr.html) | 多模态蒸馏的视觉与转移对齐 | 用教师的指令到图像注意力给视觉 token 的蒸馏损失加权，让指令相关区域获得更多监督。再以学生采样的回复 token 为条件对齐教师和学生的后续分布，补充真实前缀上的下一 token 蒸馏。 |
| <a id="cheng26p-training-strategies"></a>[HypCL: Adapting CLIP in Hyperbolic Space for Continual Learning](https://proceedings.mlr.press/v306/cheng26p.html) | 双曲空间中的 CLIP 持续适配 | 给连续任务添加轻量适配器，在庞加莱球内依次复合适配更新。用适配后视觉特征生成的类别原型校准测试 logits，可帮助区分随任务增加的新旧类别。 |

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
| <a id="chen26gb-data-strategies"></a>[CAPTCHA Solving for Native GUI Agents: Automated Reasoning-Action Data Generation and Self-Corrective Training](https://proceedings.mlr.press/v306/chen26gb.html) | GUI 智能体的失败轨迹纠错数据 | 在可自动判定结果的合成界面中收集学生模型的失败轨迹，让专家结合中间截图和正确解回顾错误并写出纠正过程。把这些轨迹与正常解题轨迹一起微调，给原生视觉语言智能体提供从中途错误恢复的监督。 |

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
| <a id="chen26dx-inference"></a>[Beyond Logits: Coherent Hallucination Mitigation via Attention Contrastive Decoding](https://proceedings.mlr.press/v306/chen26dx.html) | 注意力层对比解码 | 在解码器注意力层比较干净输入与诱发幻觉的扰动输入。增强干净分支权重较高的位置，并用对比减法压低扰动分支权重较高的位置，无需重新训练。 |
| <a id="chen26dz-inference"></a>[Beyond Blind Noising: Disentangled Visual Rectification for Hallucination Mitigation in MLLMs](https://proceedings.mlr.press/v306/chen26dz.html) | 双编码器视觉幻觉校正 | 对同一图像加噪后，比较图文预训练编码器与对齐后的自监督视觉编码器的响应变化，用后者估计结构损失。按响应差抑制幻觉主导区域、补偿结构损失主导区域，再用校正特征与加噪图像特征各自得到的 logits 做对比解码。 |
| <a id="chen26fv-inference"></a>[Show, Don’t Tell: Morphing Latent Reasoning into Image Generation](https://proceedings.mlr.press/v306/chen26fv.html) | 图像生成的潜空间推理调度 | 压缩近期图像词元的隐状态供策略判断何时推理。触发后将推理结果映射为控制信号，直接写入生成分支的 KV 缓存，引导后续图像词元，无需在每次推理时把半成品图像解码为像素。 |
| <a id="cheng26d-inference"></a>[Mitigating Hallucinations in Large Vision-Language Models via Causal Route Gating](https://proceedings.mlr.press/v306/cheng26d.html) | 视觉语言模型注意力通路门控 | 把各注意力头的输出拆为视觉与文本两路，用一次前向及一次梯度查询近似估计两路对当前词元决策的影响，再只抑制冲突头的文本分量，保留视觉分量。 |
| <a id="cho26b-inference"></a>[Improving Visual Token Reduction via Rectifying Distortions for Efficient Multimodal LLM Inference](https://proceedings.mlr.press/v306/cho26b.html) | 视觉词元删减后的注意力校准 | 减少视觉词元后仍保留原位置，用 RoPE 的相对距离衰减估计补偿注意力，合并时同时计入每个词元代表的原词元数。在稀疏视觉序列上恢复部分注意力，无需补回被删词元。 |

<a id="by-representation-learning"></a>

### 表征学习

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="chen26ag-representation-learning"></a>[Information-Theoretic Disentangled Latent Modeling with Conditional Diffusion for Incomplete Multi-View Clustering](https://proceedings.mlr.press/v306/chen26ag.html) | 不完整多视图聚类 | 用信息论目标拆出共享语义和各视图特有因素，再用 Wasserstein 混合汇聚语义。条件扩散同时读取全局语义和视图因素，补全缺失观测。 |
| <a id="chen26cx-representation-learning"></a>[Beyond Global Alignment: Fine-Grained Motion-Language Retrieval via Pyramidal Shapley-Taylor Learning](https://proceedings.mlr.press/v306/chen26cx.html) | 关节与片段级动作文本对齐 | 把人体动作拆成时间片段和空间关节，用 Shapley–Taylor 交互建模逐级学习它们与词元的对应，让检索分数能够反映整段相似度容易掩盖的局部动作。 |
| <a id="chen26fo-representation-learning"></a>[MetaStreet: Semi-Supervised Multimodal Learning for Street-Level Socioeconomic Prediction](https://proceedings.mlr.press/v306/chen26fo.html) | 利用地理邻接的半监督街景对比学习 | 为无标签街段从其已标注邻居继承负样本候选，即选择与邻居标签不同的街段作负例。若街段属性具有空间自相关，可据此让未标注街景参与视觉和文本的联合表征学习。 |
| <a id="cheng26k-representation-learning"></a>[Deep Discriminative Structure Proxy Hashing for Cross-modal Retrieval](https://proceedings.mlr.press/v306/cheng26k.html) | 结构化代理的跨模态哈希 | 为每个样本从同标签代理中选近邻形成稀疏子图，按关联强度聚合候选代理的标签响应。以子图约束代理间竞争，可改善多标签样本在汉明空间中的可分性。 |
| <a id="choi26h-representation-learning"></a>[Toward Structural Multimodal Representations: Specialization, Selection, and Sparsification via Mixture-of-Experts](https://proceedings.mlr.press/v306/choi26h.html) | 可稀疏选择的多模态专家表征 | 先预训练各模态的 MoE 编码器，让专家子空间承载可对齐的语义成分，再训练任务路由器选择专家，并在推理时按批次保留评分最高的一定比例的输入与专家配对。MultiBench 实验中，中等稀疏率的表现优于研究中测试的更高稀疏率。 |

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
| <a id="chen26dl-evaluation"></a>[DOUBT: Decoupled Object-level Understanding and Bridging via vMF-based Trustworthiness for Hallucination Detection in MLLMs](https://proceedings.mlr.press/v306/chen26dl.html) | 基于物体提示的幻觉检测 | 对同一图像问题采样直接回答和先识别物体再回答的两组结果。分别把各组句向量归一化后取向量均值的模长，再对两组分数取平均，以较低的语义方向集中度标记幻觉风险。 |
| <a id="chen26en-evaluation"></a>[OrchJail: Jailbreaking Tool-Calling Text-to-Image Agents by Orchestration-Guided Fuzzing](https://proceedings.mlr.press/v306/chen26en.html) | 文生图工具链越狱评测 | 把成功越狱的工具调用轨迹分解为任务规划、步骤调度和工具选择，再将这些行为与提示词片段建立经验关联，引导模糊测试查找由多步组合触发的风险。 |
| <a id="chen26fj-evaluation"></a>[BabyVision: Visual Reasoning Beyond Language](https://proceedings.mlr.press/v306/chen26fj.html) | 基础视觉推理诊断 | 把视觉推理拆成细粒度辨别、轨迹追踪、空间感知和图案识别四类，构造尽量少依赖语言知识的题目并与真人成绩比较，单独检验视觉语言模型对基础视觉线索的处理能力。 |
| <a id="chen26gz-evaluation"></a>[HoloFair: Unified T2I Fairness Evaluation and Fair-GRPO Debiasing](https://proceedings.mlr.press/v306/chen26gz.html) | 文生图人口属性多样性评测 | 用属性分类器统计生成样本，把性别、年龄和种族分布的归一化熵以几何平均合并，再取易触发刻板印象的提示词中该分数的第 10 百分位，衡量较差情境下的多样性。 |
| <a id="cherep26a-evaluation"></a>[Visual Persuasion: What Influences Decisions of Vision-Language Models?](https://proceedings.mlr.press/v306/cherep26a.html) | 视觉语言模型的选择偏好审计 | 将图像编辑封装成可迭代更新的文字提示，在尽量保持对象身份的前提下改变构图、光照等属性。让被测模型在成对图片中做选择，以选择率变化衡量视觉属性能在多大程度上左右决策。 |
| <a id="chi26a-evaluation"></a>[GameDevBench: Evaluating Agentic Capabilities Through Game Development](https://proceedings.mlr.press/v306/chi26a.html) | 游戏开发智能体的运行时反馈 | 用含着色器、精灵图和动画等资产的 Godot 开发任务评测多模态智能体。把编辑器截图与运行视频作为反馈，分别暴露场景配置和时序行为，在论文测试中提高了智能体的任务完成率。 |
| <a id="cohen26d-evaluation"></a>[MET-Bench: Multimodal Entity Tracking for Evaluating the Limitations of Vision-Language and Reasoning Models](https://proceedings.mlr.press/v306/cohen26d.html) | 视觉实体追踪的感知与推理解耦 | 对同一实体状态变化分别给出图像和文字，还测试先把图像动作转成文字再追踪的级联系统。对能够正确识别画面动作的测试条件，这种对照仍能发现视觉状态更新中的推理瓶颈。 |

<a id="by-theory-statistics"></a>

### 理论与统计

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="cai26o-theory-statistics"></a>[The Geometric Mechanics of Contrastive Representation Learning: Alignment Potentials, Entropic Dispersion, and Cross-Modal Divergence](https://proceedings.mlr.press/v306/cai26o.html) | 跨模态对比学习 | 成对样本高度对齐时，两种模态的边缘分布仍可持续分离。可分别测配对质量与模态间距，避免用一个指标替代另一个。 |
<!-- classification:end -->
