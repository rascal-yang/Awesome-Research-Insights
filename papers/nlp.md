# 自然语言处理

[首页](../README.md) · [参与贡献](../CONTRIBUTING.md) · [English](../en/papers/nlp.md)

语言处理、检索与结构化预测。

<!-- classification:start -->
## 按技术类型浏览

<a id="by-architecture"></a>

### 模型架构

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="dervishi26a-architecture"></a>[Separating Representation from Reconstruction Enables Scalable Text Encoders](https://proceedings.mlr.press/v306/dervishi26a.html) | 文本编码与掩码重建解耦 | 让编码器表示可见 token，由独立预测器读取表示并重建被遮蔽 token。用互补掩码构造同一句子的两份视图，各视图彼此隔离，两次预测合计能覆盖所有 token，并支持较高掩码率。 |
| <a id="gong26c-architecture"></a>[Scaling Transformers for End-to-End Discrete Audio Tokenization](https://proceedings.mlr.press/v306/gong26c.html) | 纯因果 Transformer 的音频分词 | 用交错的波形分块与因果 Transformer 编码层逐步降采样，经残差向量量化得到离散 token，再由对称解码器重建波形。编码器、量化器和解码器可端到端联合训练，也支持流式编解码。 |

<a id="by-modules"></a>

### 模块

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="bian26c-modules"></a>[AgentVocab: Structure-Aware Vocabulary Adaptation for Efficient LLM Agents](https://proceedings.mlr.press/v306/bian26c.html) | Agent 词表适配 | 从实际工具调用轨迹中提取常见结构和语义单元扩充词表，减少同一调用所需的解码步数。 |

<a id="by-loss-functions"></a>

### 损失函数

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="cai26d-loss-functions"></a>[ElicitR: Unlocking Latent Reasoning in Dense Retrievers via Generative Regularization](https://proceedings.mlr.press/v306/cai26d.html) | 检索器生成正则 | 用检索器的相似度加权其他文本对下 token 预测的条件贡献，与对比目标一起训练，让检索器区分二分类相关性之外的证据联系。 |

<a id="by-optimization"></a>

### 优化

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="feng26p-optimization"></a>[Convex Low-resource Accent-Robust Language Detection in Speech Recognition](https://proceedings.mlr.press/v306/feng26p.html) | 低资源语音语言识别的凸检测头 | 从冻结的语音编码器提取特征并做带掩码的均值池化，用批量 ADMM 在凸重参数化下训练语言识别头。将它预测的语言 token 传给转录解码器，减少口音造成的语言误判向转录阶段传播。 |

<a id="by-reinforcement-learning"></a>

### 强化学习方法

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="bu26e-reinforcement-learning"></a>[Grounding Multi-Hop Reasoning in Structural Causal Models via Group Relative Policy Optimization](https://proceedings.mlr.press/v306/bu26e.html) | 多跳事实核查 | 要求模型输出证据与结论的依赖图，再用 GRPO 的规则奖励约束推理深度与冗余。实测过长的依赖链也会拉低核查准确率。 |

<a id="by-training-strategies"></a>

### 训练策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="geng26c-training-strategies"></a>[Bridging the Stability-Expressivity Gap: Synthetic Data Scaling and Preference Alignment for Low-Resource Spoken Language Models](https://proceedings.mlr.press/v306/geng26c.html) | 低资源语音的多温度自对齐 | 缺少真实语音参照时，对同一文本用多个温度采样，先按重复和时长过滤，再按转写词错率构造偏好对。优选与劣选样本都满足时长与重复限制，让偏好训练集中在发音准确度。 |

<a id="by-data-strategies"></a>

### 数据策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="banayeeanzade26a-data-strategies"></a>[EPSVec: Efficient and Private Synthetic Data Generation via Dataset Vectors](https://proceedings.mlr.press/v306/banayeeanzade26a.html) | 差分隐私合成数据 | 只提取和净化一次私有数据相对公共先验的激活偏移向量，之后用它引导解码。重复合成样本属于后处理，无需重复消耗隐私预算。 |
| <a id="cho26i-data-strategies"></a>[Expert-guided Clinical Text Augmentation via Query-Based Model Collaboration](https://proceedings.mlr.press/v306/cho26i.html) | 临床文本改写的专家约束 | 先让轻量医学专家模型标出临床笔记中必须保留语义的词项，再把原文和词项约束交给通用模型改写，沿用原始标签。实验同时检查词元和医学概念，测量改写对关键内容的保留及幻觉引入。 |
| <a id="dutta26a-data-strategies"></a>[HOBIT: Hardness Optimized Batch Sampling for InfoNCE Training](https://proceedings.mlr.press/v306/dutta26a.html) | 对比学习的困难负例组批 | 组批时用查询与候选负文档的相似度减去正、负文档相似度的加权项，优先选对查询有迷惑性但与正例不近重复的负例。再贪心最大化子模组批目标，让这种难负例随训练批次变化。 |

<a id="by-inference"></a>

### 推理策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="agrawal26d-inference"></a>[BlitzRank: Principled Zero-shot Ranking Agents with Tournament Graphs](https://proceedings.mlr.press/v306/agrawal26d.html) | 排序与检索 | 把一次多项排序转换成多条比较边，用传递闭包复用查询结果，再围绕前 k 名继续查询。循环偏好可合成同一档。 |
| <a id="ai26b-inference"></a>[PASA: A Principled Embedding-Space Watermarking Approach for LLM-Generated Text under Semantic-Invariant Attacks](https://proceedings.mlr.press/v306/ai26b.html) | 文本水印 | 把水印放到语义簇层，通过密钥与语义历史同步随机性，让释义改写后仍可在语义层检测水印。 |
| <a id="an26a-inference"></a>[IPMark: A Sentence-Level Watermark for LLMs with Hierarchical Personalization and Efficient Detection](https://proceedings.mlr.press/v306/an26a.html) | 句子级水印 | 按模型和用户组织分层水印标识，用语义及句法信号筛选句子候选，再用分层检索缩小溯源检测范围。 |
| <a id="chien26b-inference"></a>[MoshiRAG: Asynchronous Knowledge Retrieval for Full-Duplex Speech Language Models](https://proceedings.mlr.press/v306/chien26b.html) | 全双工语音的异步检索 | 语音模型用特殊词元决定是否检索，把流式转录交给后台后继续生成。利用开始应答到说出关键信息的时间差，把返回的检索文本编码后注入后续生成，兼顾语音交互时延与事实性。 |
| <a id="du26i-inference"></a>[Sparse Autoencoders for Interpretable Emotion Control in Text-to-Speech](https://proceedings.mlr.press/v306/du26i.html) | 语音情感的稀疏特征干预 | 用稀疏自编码器分解文本转语音模型的语义隐状态，筛出与特定情感相关的潜特征。生成时只增减这些特征的激活，沿各自的解码方向改变隐状态，无需调整主干权重。 |

<a id="by-representation-learning"></a>

### 表征学习

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="cao26p-representation-learning"></a>[Orthogonal Hierarchical Decomposition for Structure-Aware Table Understanding with Large Language Models](https://proceedings.mlr.press/v306/cao26p.html) | 复杂表格理解 | 按空间与语义约束同时构建行树和列树，再用双路径恢复每个单元格的层级语义，保留合并单元格和多级表头中的依赖。 |
| <a id="gao26h-representation-learning"></a>[InstEmb: Instruction-Following Embeddings through Glimpses of the Future](https://proceedings.mlr.press/v306/gao26h.html) | 用前瞻 token 蒸馏指令嵌入 | 同时对最后一个输入 token 做对比学习，并用若干可学习前瞻 token 蒸馏真实生成后续的隐藏表征。推理把输入末位与前瞻位置的均值合并成向量，在一次计算中纳入输出相关语义，无需逐 token 解码。 |

<a id="by-evaluation"></a>

### 评测与诊断

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="altintas26a-evaluation"></a>[TokSuite: Measuring the Impact of Tokenizer Choice on Language Model Behavior](https://proceedings.mlr.press/v306/altintas26a.html) | 分词器评测 | 训练模型时固定架构、数据、训练预算和初始化，只改变分词器，再用原生语言者整理的真实扰动测试分词的影响。 |
| <a id="basha26a-evaluation"></a>[VocSim A Training-free Benchmark for Zero-shot Content Identity in Single-source Audio](https://proceedings.mlr.press/v306/basha26a.html) | 音频表征评测 | 只用单声源片段测冻结嵌入的几何，并以置换基线校准近邻纯度与全局分离率，可单独暴露低资源语言的表示差距。 |
| <a id="chen26av-evaluation"></a>[Eyes-on-Me: Scalable RAG Poisoning through Transferable Attention-Steering Attractors](https://proceedings.mlr.press/v306/chen26av.html) | 检索增强生成安全评测 | 文档中的注意力集中机制可以在不同检索器和生成器之间迁移。做投毒压力测试时，可单独评估复用型污染对检索排序和生成内容的影响。 |
| <a id="chen26bf-evaluation"></a>[Black-Box Detection of LLM-Generated Text Using Generalized Jensen Shannon Divergence](https://proceedings.mlr.press/v306/chen26bf.html) | 生成文本的惊异度转移检测 | 用代理语言模型单次前向计算词元的负对数条件概率，将其离散为状态，再统计相邻状态的转移。用广义 Jensen–Shannon 散度比较测试文本与预先建立的人类和机器文本转移矩阵。 |
| <a id="dehdashtian26a-evaluation"></a>[FoeGlass: Simple In-Context Learning Is Enough for Red Teaming Audio Deepfake Detectors](https://proceedings.mlr.press/v306/dehdashtian26a.html) | 音频深伪检测的多样性压力测试 | 在黑盒红队评测中同时把检测器反馈和候选音频间的多样性反馈放进上下文，令测试覆盖更多错误模式。论文在所测检测器上确认了部分失效跨模型迁移，且回收测试样本做微调能提高检测稳健性。 |
| <a id="duarte26a-evaluation"></a>[Sem-Detect: Semantic Level Detection of AI Generated Peer-Reviews](https://proceedings.mlr.press/v306/duarte26a.html) | 同行评审来源的声明级检测 | 为目标评审配对同一论文、总体评分相同的多份 AI 参考评审，比较评价意见、建设建议等声明的最佳语义匹配，再加文本特征训练三分类器。在论文数据中，经 AI 润色的人类评审仍常保留有辨识度的判断内容。 |
| <a id="fernandez26b-evaluation"></a>[How Good is Post-Hoc Watermarking With Language Model Rephrasing?](https://proceedings.mlr.press/v306/fernandez26b.html) | 重写式事后文本水印评测 | 用带水印的解码器改写已有文本，联合测量水印可检测性和语义保真。论文比较显示，开放文本可通过束搜索改善折中，但代码的强水印往往伴随功能正确率下降。 |
| <a id="gao26af-evaluation"></a>[FiRE: Fine-grained Ranking Evaluation for Machine Translation](https://proceedings.mlr.press/v306/gao26af.html) | 机器翻译的无参考成对排序 | 给裁判提供源句和两份译文，分别判断忠实度、流畅度与风格一致性。分项成对判断可用人工排序分别校验，并揭示总分掩盖的译文优缺点。 |
| <a id="ghaffari26a-evaluation"></a>[BAT: Better Audio Transformer Guided by Convex Gated Probing](https://proceedings.mlr.press/v306/ghaffari26a.html) | 音频自监督表征的凸门控探测 | 冻结音频编码器，对所有层的块词元与全局词元学习和为一的非负聚合权重，再用汇总特征与可学习原型的相似度做预测。探针可同时评估表示质量和任务信息所处层次。 |

<a id="by-theory-statistics"></a>

### 理论与统计

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="adler26b-theory-statistics"></a>[Efficient Mismatch-Tolerant Coding for Model-Driven Compression](https://proceedings.mlr.press/v306/adler26b.html) | 无损压缩 | 编码器和解码器的模型预测有界不一致时，可通过重新优化概率匹配区间编码的参数，在保留鲁棒性的同时降低码长。 |
| <a id="arenas26a-theory-statistics"></a>[Language Generation in the Limit: Complexity Barriers and Implications for Learning](https://proceedings.mlr.press/v306/arenas26a.html) | 语言学习复杂度 | 只从正例最终生成目标形式语言在可计算意义下成立，但样本复杂度障碍甚至出现在正则语言的严格子类。 |
| <a id="ashrafi26a-theory-statistics"></a>[The Crowded Embedding Space: A Mean-Field Mechanism for Emergent Marginalization in Retrieval-Augmented Agents](https://proceedings.mlr.press/v306/ashrafi26a.html) | 检索公平性 | 在共享向量空间里，语义相邻的多数文档变得密集后，可能把少数目标挤出前 k 位。按查询孤立评测容易漏掉这种跨目标相互作用。 |
| <a id="banihashem26b-theory-statistics"></a>[Adversarially Robust Approximate Furthest Neighbor](https://proceedings.mlr.press/v306/banihashem26b.html) | 自适应近似检索 | 查询会参考历史返回值时，经典近似最远邻结构可能失去保证。为自适应查询设计的结构仍能在一部分参数范围保持次线性查询开销。 |
| <a id="grover26b-theory-statistics"></a>[Text Has Curvature](https://proceedings.mlr.press/v306/grover26b.html) | 双侧上下文的词义收缩曲率 | 在同一词位分别扩展左、右上下文，用去偏传输散度比较扩展一侧前后另一侧引起的词义后验变化。变化收缩对应正曲率，扩张对应负曲率。 |
<!-- classification:end -->
