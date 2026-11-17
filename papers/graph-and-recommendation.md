# 图学习与推荐

[首页](../README.md) · [English](../en/papers/graph-and-recommendation.md)

图模型、知识图谱与推荐系统。

<!-- classification:start -->
## 按技术类型浏览

<a id="by-architecture"></a>

### 模型架构

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="bandyopadhyay26a-architecture"></a>[RSF-GLLM: Bridging the Semantic Gap in Multi-Hop Knowledge Graph QA via Recurrent Soft-Flow and Decoupled LLM Generation](https://proceedings.mlr.press/v306/bandyopadhyay26a.html) | 知识图谱多跳问答 | 用 GRU 更新查询表示，让连续相关性分数穿过与问题缺少词汇重合的桥接节点，再提取稀疏推理路径给生成器。 |
| <a id="chen26al-architecture"></a>[OneSearch: A Preliminary Exploration of the Unified End-to-End Generative Framework for E-commerce Search](https://proceedings.mlr.press/v306/chen26al.html) | 生成式电商检索 | 用关键词增强的层级量化编码表示商品，再把短期和长期用户行为送入同一个生成检索模型，统一学习相关性与个体偏好。 |

<a id="by-modules"></a>

### 模块

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="bai26i-modules"></a>[GI-GCN: Global Interacted Graph Convolutional Networks via Dominant Sets for Graph Classification](https://proceedings.mlr.press/v306/bai26i.html) | 图卷积 | 用 Dominant Set 迭代估计全图节点的重要性，在每层局部消息传播前重加权，令邻域卷积也能利用非邻接节点的关联。 |
| <a id="barcelo26a-modules"></a>[Message Passing on the Edge: Towards Scalable and Expressive GNNs](https://proceedings.mlr.press/v306/barcelo26a.html) | 图神经网络表达力 | 把消息传播的中心从点移到边，并沿三角形交换信息，可区分更多图结构，在论文考虑的实际图负载上仍保持近线性开销。 |

<a id="by-optimization"></a>

### 优化

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="bai26g-optimization"></a>[Rethinking Efficient Graph Coarsening via a Non-Selfishness Principle](https://proceedings.mlr.press/v306/bai26g.html) | 图粗化 | 评估合并时优先考虑对整个邻域的干扰，减少逐节点全局匹配。局部各向同性允许把高节点度带来的额外计算消掉。 |
| <a id="chakraborty26b-optimization"></a>[Fairness in Aggregation: Optimal Top-$k$ and Improved Full Ranking](https://proceedings.mlr.press/v306/chakraborty26b.html) | 公平排序聚合 | 把群体代表性约束写入前 k 位的排序聚合，可求得该前缀问题的最优解。若要为所有候选排序，则论文给出二倍近似。 |
| <a id="chen26b-optimization"></a>[Differentially Private Range Subgraph Counting](https://proceedings.mlr.press/v306/chen26b.html) | 隐私图查询 | 把属性范围内固定模式的子图计数映射为加权正交范围查询，再用局部灵敏度加噪。理论下界说明高维属性会使误差显著增加。 |

<a id="by-reinforcement-learning"></a>

### 强化学习方法

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="agarwal26a-reinforcement-learning"></a>[Efficient Online Influence Maximization under the Independent Cascade Model with Node-Level Feedback](https://proceedings.mlr.press/v306/agarwal26a.html) | 在线影响力最大化 | 独立级联只观察节点是否激活时，可用标准的离线种子选择 oracle 构造在线算法，达到平方根量级的遗憾界。 |
| <a id="bisht26a-reinforcement-learning"></a>[CORAL: Uncertainty-Aware Regulation of Exposure Concentration in Recommender Systems](https://proceedings.mlr.press/v306/bisht26a.html) | 推荐曝光控制 | 把类别曝光累积量当成状态，对超出曝光约束的概率估计上置信界，再随风险提高惩罚，抑制反馈循环中的集中化。 |

<a id="by-training-strategies"></a>

### 训练策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="arafat26a-training-strategies"></a>[Adversarial Attacks and Robust Training for Hypergraph Neural Networks](https://proceedings.mlr.press/v306/arafat26a.html) | 超图鲁棒训练 | 把超图拉普拉斯作为统一的攻击目标，在同一预算框架下测试结构及特征扰动，再用相应扰动做超图模型的对抗训练。 |
| <a id="canturk26a-training-strategies"></a>[Can Computational Reducibility Lead to Transferable Models for Graph Combinatorial Optimization?](https://proceedings.mlr.press/v306/canturk26a.html) | 图组合优化迁移 | 用计算复杂性中的任务归约关系选择预训练组合，再共享图编码器微调。留一任务评测中，多任务预训练通常加快收敛。 |
| <a id="chen26cz-training-strategies"></a>[Message Tuning Outshines Graph Prompt Tuning: A Prismatic Space Perspective](https://proceedings.mlr.press/v306/chen26cz.html) | 图基础模型的消息微调 | 冻结预训练 GNN，在每层加入少量可学习的消息原型，并动态融合原型和原生消息。逐层改变消息聚合可提高适配能力，论文在其刻画的模型条件下给出了超出输入提示微调上界的构造。 |

<a id="by-data-strategies"></a>

### 数据策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="azizpour26a-data-strategies"></a>[From Moments to Models: Graphon-Mixture Learning for Mixup and Contrastive Learning](https://proceedings.mlr.press/v306/azizpour26a.html) | 图数据增强 | 用模体密度给图数据估计潜在生成分量，再让 mixup 与对比学习利用分量信息，避免把结构来源差异当作可任意混合的扰动。 |
| <a id="chen26cr-data-strategies"></a>[DANCE: Dynamic, Available, Neighbor-gated Condensation for Federated Text-Attributed Graphs](https://proceedings.mlr.press/v306/chen26cr.html) | 联邦文本图证据凝缩 | 每轮用上一轮的图编码器更新核心节点的邻居和句段选择，在逐跳预算和文本预算内聚合证据，并在客户端保留选中邻居和原句段的映射，以便审计压缩后的表征。 |

<a id="by-inference"></a>

### 推理策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="ai26c-inference"></a>[PromptDyG: Test-Time Prompt Adaptation on Dynamic Graphs](https://proceedings.mlr.press/v306/ai26c.html) | 图模型测试时适应 | 冻结图骨干，用当前快照的无标签特征熵更新动态图提示，持续跟随图结构与测试分布的变化。 |
| <a id="bisht26b-inference"></a>[CARE: Adaptive Calibration for Reliable Recommendations](https://proceedings.mlr.press/v306/bisht26b.html) | 在线推荐校准 | 持续监测推荐损失并在用户行为变化时重新定阈值，同时在线调整不同集合预测器的权重，使可变长度推荐列表保持紧凑。 |

<a id="by-representation-learning"></a>

### 表征学习

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="behmanesh26a-representation-learning"></a>[Graph Alignment via Dual-Pass Spectral Encoding and Latent Space Communication](https://proceedings.mlr.press/v306/behmanesh26a.html) | 跨图对齐 | 先向节点嵌入注入高频信息以保留局部区分度，再在对应映射上做低通平滑，分别处理节点过平滑与跨图匹配噪声。 |
| <a id="cai26f-representation-learning"></a>[CONTEXTOR: Contextualized High-order Contrastive Learning](https://proceedings.mlr.press/v306/cai26f.html) | 高阶关系表征 | 把高阶关系拆成多个不完整查询与补全实体，用查询非对称地调制候选实体表征，再做对比对齐。 |
| <a id="chen26ak-representation-learning"></a>[SynGR: Unleashing the Potential of Cross-Modal Synergy for Generative Recommendation](https://proceedings.mlr.press/v306/chen26ak.html) | 跨模态生成式推荐 | 抑制模型过度依赖占优模态，让推荐生成器学习只有联合读取图像与文本才能辨识的商品属性。 |

<a id="by-evaluation"></a>

### 评测与诊断

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="agbaje26a-evaluation"></a>[Revisiting Asymmetries in Black-box Link Stealing against Graph Neural Networks](https://proceedings.mlr.press/v306/agbaje26a.html) | 图模型隐私评测 | 连边泄漏应在极低误报率下分组测量。同类节点的后验几何可能压缩判别方向，重调距离后会暴露平均结果遗漏的风险。 |
| <a id="akula26a-evaluation"></a>[Same Graph Cross-Task Transfer in GNNs: Protocols and Predictors](https://proceedings.mlr.press/v306/akula26a.html) | 图模型迁移 | 同一图上，节点分类迁往链路预测在同质性强的图上更可靠。反向迁移要尤其关注结构信号强度，并固定消息传递图及测试负样本防止泄漏。 |

<a id="by-theory-statistics"></a>

### 理论与统计

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="adriaens26a-theory-statistics"></a>[Simple Algorithms for Bad Triangle Transversals with Applications to Correlation Clustering](https://proceedings.mlr.press/v306/adriaens26a.html) | 相关聚类 | 完整符号图上，先找到击中所有恰有一条负边三角形的删除边集，再通过枢轴过程转成聚类，两类最优代价相差至多 1.5 倍。 |
| <a id="amran26a-theory-statistics"></a>[A Graphop Analysis of Graph Neural Networks on Sparse Graphs: Generalization and Universal Approximation](https://proceedings.mlr.press/v306/amran26a.html) | 图神经网络理论 | 扩展 graphop 极限框架，构造跨图规模和稀疏度的紧致度量，用同一套等度连续性分析 MPNN 的泛化和逼近。 |
| <a id="badanidiyuru26a-theory-statistics"></a>[Model Monotonicity in Autobidding Auctions: When Do Better Predictions Lead to Better Outcomes?](https://proceedings.mlr.press/v306/badanidiyuru26a.html) | 拍卖中的预测改进 | 提高预测分辨率对拍卖收入的影响依赖出价规则。无预算限制的目标成本出价者满足文中的一价拍卖单调性，二价机制可打破它。 |
| <a id="badreddine26a-theory-statistics"></a>[On the Theoretical Limitations of Embedding-based Link Prediction](https://proceedings.mlr.press/v306/badreddine26a.html) | 知识图谱链路预测 | 线性输出层使嵌入维度必须随图规模和连通性增长才能表达训练关系。混合式非线性输出可打破这一秩瓶颈，且参数开销较低。 |
| <a id="charpenay26a-theory-statistics"></a>[Faithful Relational Reasoning with Region-based Embeddings: Expressivity of Convex Coordinate-wise Models](https://proceedings.mlr.press/v306/charpenay26a.html) | 关系嵌入表达力 | 用逐坐标比较定义的凸区域能高效编码部分关系规则，但参数化会限制可忠实表达的规则集合，应按目标规则选区域形式。 |
<!-- classification:end -->
