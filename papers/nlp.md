# 自然语言处理

[首页](../README.md) · [参与贡献](../CONTRIBUTING.md) · [English](../en/papers/nlp.md)

语言处理、检索与结构化预测。

<!-- classification:start -->
## 按技术类型浏览

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

<a id="by-reinforcement-learning"></a>

### 强化学习方法

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="bu26e-reinforcement-learning"></a>[Grounding Multi-Hop Reasoning in Structural Causal Models via Group Relative Policy Optimization](https://proceedings.mlr.press/v306/bu26e.html) | 多跳事实核查 | 要求模型输出证据与结论的依赖图，再用 GRPO 的规则奖励约束推理深度与冗余。实测过长的依赖链也会拉低核查准确率。 |

<a id="by-data-strategies"></a>

### 数据策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="banayeeanzade26a-data-strategies"></a>[EPSVec: Efficient and Private Synthetic Data Generation via Dataset Vectors](https://proceedings.mlr.press/v306/banayeeanzade26a.html) | 差分隐私合成数据 | 只提取和净化一次私有数据相对公共先验的激活偏移向量，之后用它引导解码。重复合成样本属于后处理，无需重复消耗隐私预算。 |

<a id="by-inference"></a>

### 推理策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="agrawal26d-inference"></a>[BlitzRank: Principled Zero-shot Ranking Agents with Tournament Graphs](https://proceedings.mlr.press/v306/agrawal26d.html) | 排序与检索 | 把一次多项排序转换成多条比较边，用传递闭包复用查询结果，再围绕前 k 名继续查询。循环偏好可合成同一档。 |
| <a id="ai26b-inference"></a>[PASA: A Principled Embedding-Space Watermarking Approach for LLM-Generated Text under Semantic-Invariant Attacks](https://proceedings.mlr.press/v306/ai26b.html) | 文本水印 | 把水印放到语义簇层，通过密钥与语义历史同步随机性，让释义改写后仍可在语义层检测水印。 |
| <a id="an26a-inference"></a>[IPMark: A Sentence-Level Watermark for LLMs with Hierarchical Personalization and Efficient Detection](https://proceedings.mlr.press/v306/an26a.html) | 句子级水印 | 按模型和用户组织分层水印标识，用语义及句法信号筛选句子候选，再用分层检索缩小溯源检测范围。 |

<a id="by-representation-learning"></a>

### 表征学习

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="cao26p-representation-learning"></a>[Orthogonal Hierarchical Decomposition for Structure-Aware Table Understanding with Large Language Models](https://proceedings.mlr.press/v306/cao26p.html) | 复杂表格理解 | 按空间与语义约束同时构建行树和列树，再用双路径恢复每个单元格的层级语义，保留合并单元格和多级表头中的依赖。 |

<a id="by-evaluation"></a>

### 评测与诊断

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="altintas26a-evaluation"></a>[TokSuite: Measuring the Impact of Tokenizer Choice on Language Model Behavior](https://proceedings.mlr.press/v306/altintas26a.html) | 分词器评测 | 训练模型时固定架构、数据、训练预算和初始化，只改变分词器，再用原生语言者整理的真实扰动测试分词的影响。 |
| <a id="basha26a-evaluation"></a>[VocSim A Training-free Benchmark for Zero-shot Content Identity in Single-source Audio](https://proceedings.mlr.press/v306/basha26a.html) | 音频表征评测 | 只用单声源片段测冻结嵌入的几何，并以置换基线校准近邻纯度与全局分离率，可单独暴露低资源语言的表示差距。 |

<a id="by-theory-statistics"></a>

### 理论与统计

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="adler26b-theory-statistics"></a>[Efficient Mismatch-Tolerant Coding for Model-Driven Compression](https://proceedings.mlr.press/v306/adler26b.html) | 无损压缩 | 编码器和解码器的模型预测有界不一致时，可通过重新优化概率匹配区间编码的参数，在保留鲁棒性的同时降低码长。 |
| <a id="arenas26a-theory-statistics"></a>[Language Generation in the Limit: Complexity Barriers and Implications for Learning](https://proceedings.mlr.press/v306/arenas26a.html) | 语言学习复杂度 | 只从正例最终生成目标形式语言在可计算意义下成立，但样本复杂度障碍甚至出现在正则语言的严格子类。 |
| <a id="ashrafi26a-theory-statistics"></a>[The Crowded Embedding Space: A Mean-Field Mechanism for Emergent Marginalization in Retrieval-Augmented Agents](https://proceedings.mlr.press/v306/ashrafi26a.html) | 检索公平性 | 在共享向量空间里，语义相邻的多数文档变得密集后，可能把少数目标挤出前 k 位。按查询孤立评测容易漏掉这种跨目标相互作用。 |
| <a id="banihashem26b-theory-statistics"></a>[Adversarially Robust Approximate Furthest Neighbor](https://proceedings.mlr.press/v306/banihashem26b.html) | 自适应近似检索 | 查询会参考历史返回值时，经典近似最远邻结构可能失去保证。为自适应查询设计的结构仍能在一部分参数范围保持次线性查询开销。 |
<!-- classification:end -->
