# 图学习与推荐

[首页](../README.md) · [English](../en/papers/graph-and-recommendation.md)

图模型、知识图谱与推荐系统。

<!-- classification:start -->
## 按技术类型浏览

<a id="by-architecture"></a>

### 模型架构

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="bandyopadhyay26a-architecture"></a>[RSF-GLLM: Bridging the Semantic Gap in Multi-Hop Knowledge Graph QA via Recurrent Soft-Flow and Decoupled LLM Generation](https://proceedings.mlr.press/v306/bandyopadhyay26a.html) · [论文卡](../conferences/icml-2026/cards/0201-0300.md#paper-bandyopadhyay26a) | 知识图谱多跳问答 | 用 GRU 更新查询表示，让连续相关性分数穿过与问题缺少词汇重合的桥接节点，再提取稀疏推理路径给生成器。 |
| <a id="chen26al-architecture"></a>[OneSearch: A Preliminary Exploration of the Unified End-to-End Generative Framework for E-commerce Search](https://proceedings.mlr.press/v306/chen26al.html) | 生成式电商检索 | 用关键词增强的层级量化编码表示商品，再把短期和长期用户行为送入同一个生成检索模型，统一学习相关性与个体偏好。 |
| <a id="de-castelli26a-architecture"></a>[Adaptive Memory Retention in Dynamic Graphs](https://proceedings.mlr.press/v306/de-castelli26a.html) | 动态图的可学习信息耗散 | 在快照之间用反对称参数化的神经 ODE 传播节点信息，并在快照到达时注入观测更新。加入依节点状态调节的耗散项，可抑制噪声累积并保留跨时间的有效依赖。 |
| <a id="eliasof26a-architecture"></a>[Graph Neural Dynamics via Learned Energy and Tangential Flows](https://proceedings.mlr.press/v306/eliasof26a.html) | 图动力学的能量与切向流 | 将节点表征的演化拆成能量梯度下降和与梯度正交的消息传递流。后者可沿等能面继续传播信息，使能量下降的约束允许表征在梯度很小的区域继续更新。 |
| <a id="fang26g-architecture"></a>[MC-HNN: Learning Latent Structural Semantics and High-Rank Representations for Hypergraph Neural Networks](https://proceedings.mlr.press/v306/fang26g.html) | 超边潜类型与多通道传播 | 让各超边以可学习权重混合共享码本中的类型原型，给超边聚合额外提供独立于输入节点特征的类型信息。再用多通道消息传递为节点表示保留更高的秩容量。 |
| <a id="fernandez26a-architecture"></a>[L2G-NET: Local to Global Spectral Graph Neural Networks via Cauchy Factorizations](https://proceedings.mlr.press/v306/fernandez26a.html) | 图傅里叶变换的柯西分解 | 把全图傅里叶变换分解为小子图的谱算子和跨割连接的柯西因子，在因子之间插入可学习局部滤波器，逐级整合远程信息并避免全图特征分解。 |
| <a id="gailhard26a-architecture"></a>[Feature-Aware (Hyper)graph Generation via Next-Scale Prediction](https://proceedings.mlr.press/v306/gailhard26a.html) | 超图生成的多尺度展开 | 把节点和超边写成二部表示，由粗到细复制父节点及其连接。细化阶段在子节点间重分配尺度编码，并更新属性、移除多余的边，使每一步同时恢复结构和特征。 |
| <a id="gantes26a-architecture"></a>[SuperHype: Hypergraph Generation via Graph-Superposition Decomposition](https://proceedings.mlr.press/v306/gantes26a.html) | 以分层极大团表示超边 | 把超图拆成共享节点集合的多层普通图，令各层极大团的不交并集恰好还原原始超边。扩散 Transformer 在这一层序列上生成，再从各层提取极大团复原高阶连边。 |

<a id="by-modules"></a>

### 模块

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="bai26i-modules"></a>[GI-GCN: Global Interacted Graph Convolutional Networks via Dominant Sets for Graph Classification](https://proceedings.mlr.press/v306/bai26i.html) · [论文卡](../conferences/icml-2026/cards/0101-0200.md#paper-bai26i) | 图卷积 | 用 Dominant Set 迭代估计全图节点的重要性，在每层局部消息传播前重加权，令邻域卷积也能利用非邻接节点的关联。 |
| <a id="barcelo26a-modules"></a>[Message Passing on the Edge: Towards Scalable and Expressive GNNs](https://proceedings.mlr.press/v306/barcelo26a.html) · [论文卡](../conferences/icml-2026/cards/0201-0300.md#paper-barcelo26a) | 图神经网络表达力 | 把消息传播的中心从点移到边，并沿三角形交换信息，可区分更多图结构，在论文考虑的实际图负载上仍保持近线性开销。 |
| <a id="chen26gm-modules"></a>[Weaving Graph over Tokens: Contextualizing Structured Sequences for LLMs](https://proceedings.mlr.press/v306/chen26gm.html) | 兼顾图拓扑与因果顺序的注意力 | 同一图元素的 token 块内保留因果掩码，不同图元素块之间允许双向注意。将序列位置与图谱坐标共同编码到 RoPE 旋转相位，让 Q、K 点积同时反映 token 顺序和图结构。 |
| <a id="choi26d-modules"></a>[Gauge-Equivariant Graph Networks via Self-Interference Cancellation](https://proceedings.mlr.press/v306/choi26d.html) | 异配图消息的自成分消除 | 先用 U(1) 传输把复数邻居消息对齐到目标节点的规范，再投影去除沿目标特征的分量。对残差用规范不变的相位对齐量门控，并与原消息混合后计算注意力，以控制自平行成分的强化。 |
| <a id="fesser26b-modules"></a>[Unitary Convolutions for Message-passing and Positional Encodings on Directed Graphs](https://proceedings.mlr.press/v306/fesser26b.html) | 有向带属性图的酉卷积 | 将带边属性的有向邻接矩阵变换为斜厄米矩阵并做矩阵指数，得到酉传播算子。它在两个方向传递消息时仍可区分边的方向，并保持传播步中的特征范数。 |

<a id="by-loss-functions"></a>

### 损失函数

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="chen26ez-loss-functions"></a>[Mitigating Reward Hacking in LLM-based Recommendation: A Preference Optimization Approach](https://proceedings.mlr.press/v306/chen26ez.html) | 推荐排序的伪负例偏好优化 | 两两偏好更新可能几乎不改变正例和未采样负例的相对次序。加入带锚定奖励的伪负例作为额外比较对象，可为这些容易被原有梯度忽略的排序关系补充监督。 |
| <a id="chen26gu-loss-functions"></a>[GraphP-FL: Personalized Federated Graph Learning via Dynamic Structure Awareness and Fisher Information Elastic Alignment](https://proceedings.mlr.press/v306/chen26gu.html) | 联邦图学习的 Fisher 参数对齐 | 用服务端下发的对角 Fisher 信息加权本地参数与全局参数的平方差，使高敏感参数受到更强的偏移惩罚。服务端再依据客户端 Fisher 信息的迹分配模型聚合权重。 |
| <a id="chen26gx-loss-functions"></a>[ST-TGExplainer: Disentangling Stability and Transition Patterns for Temporal GNN Interpretability](https://proceedings.mlr.press/v306/chen26gx.html) | 时序图解释的稳定与转变证据 | 按交互频率对解释子图做软拆分，使重复互动偏向稳定分量、首次或罕见互动偏向转变分量，再用以事件标签为条件的互信息惩罚压低两部分的冗余。 |
| <a id="deng26u-loss-functions"></a>[Discriminative Mixture-of-Experts on Graphs with Reliable Expert Fusion](https://proceedings.mlr.press/v306/deng26u.html) | 图混合专家的分组对比路由 | 同时按原始节点属性和个性化 PageRank 得到分组，只将两种分组标签都相同的节点放在一起。对比损失让节点的路由分布靠近本组平均分布并区分其他组，以抑制路由坍缩。 |
| <a id="ding26v-loss-functions"></a>[Discriminative Attribute Graph Clustering Through Topology-Guided Contrastive Learning](https://proceedings.mlr.press/v306/ding26v.html) | 属性图聚类的双视图去冗余 | 直接将属性自编码器与图自编码器的嵌入用作两种视图，再通过互信息估计和去相关约束减少重叠信息，使聚类表征能利用属性和拓扑的互补线索。 |
| <a id="downer26a-loss-functions"></a>[Watermarking Graph Neural Networks via Explanations for Ownership Protection](https://proceedings.mlr.press/v306/downer26a.html) | 基于子图解释的模型水印 | 在节点分类损失外，约束一组保密子图的解释向量在指定特征维度上与签名符号一致。验证时向模型查询子图预测、重算解释，并用符号匹配的统计显著性检验所有权。 |

<a id="by-optimization"></a>

### 优化

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="bai26g-optimization"></a>[Rethinking Efficient Graph Coarsening via a Non-Selfishness Principle](https://proceedings.mlr.press/v306/bai26g.html) · [论文卡](../conferences/icml-2026/cards/0101-0200.md#paper-bai26g) | 图粗化 | 评估合并时优先考虑对整个邻域的干扰，减少逐节点全局匹配。局部各向同性允许把高节点度带来的额外计算消掉。 |
| <a id="chakraborty26b-optimization"></a>[Fairness in Aggregation: Optimal Top-$k$ and Improved Full Ranking](https://proceedings.mlr.press/v306/chakraborty26b.html) · [论文卡](../conferences/icml-2026/cards/0401-0500.md#paper-chakraborty26b) | 公平排序聚合 | 把群体代表性约束写入前 k 位的排序聚合，可求得该前缀问题的最优解。若要为所有候选排序，则论文给出二倍近似。 |
| <a id="chen26b-optimization"></a>[Differentially Private Range Subgraph Counting](https://proceedings.mlr.press/v306/chen26b.html) | 隐私图查询 | 把属性范围内固定模式的子图计数映射为加权正交范围查询，再用局部灵敏度加噪。理论下界说明高维属性会使误差显著增加。 |
| <a id="cheng26j-optimization"></a>[What Makes a Desired Graph for Relational Deep Learning?](https://proceedings.mlr.press/v306/cheng26j.html) | 关系数据库的任务感知图结构优化 | 对关系图同时学习过滤任务无关的列和连接，并补入符合目标任务关系的边。实验发现过滤越多并不总会提升性能，注入的连接也需和下游任务的关系语义对应。 |
| <a id="gupta26b-optimization"></a>[Adapting to Evolving Graphs: A Scalable Framework for Dynamic Coarsening](https://proceedings.mlr.press/v306/gupta26b.html) | 演化图的粗化映射增量更新 | 从已有粗化矩阵出发，只优化新节点的分配和旧映射的修正项。目标同时惩罚粗图邻接变化、特征重建误差和不合理重分配，使拓扑演化时能复用上一时刻的粗化解。 |

<a id="by-reinforcement-learning"></a>

### 强化学习方法

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="agarwal26a-reinforcement-learning"></a>[Efficient Online Influence Maximization under the Independent Cascade Model with Node-Level Feedback](https://proceedings.mlr.press/v306/agarwal26a.html) · [论文卡](../conferences/icml-2026/cards/0001-0100.md#paper-agarwal26a) | 在线影响力最大化 | 独立级联只观察节点是否激活时，可用标准的离线种子选择 oracle 构造在线算法，达到平方根量级的遗憾界。 |
| <a id="bisht26a-reinforcement-learning"></a>[CORAL: Uncertainty-Aware Regulation of Exposure Concentration in Recommender Systems](https://proceedings.mlr.press/v306/bisht26a.html) · [论文卡](../conferences/icml-2026/cards/0201-0300.md#paper-bisht26a) | 推荐曝光控制 | 把类别曝光累积量当成状态，对超出曝光约束的概率估计上置信界，再随风险提高惩罚，抑制反馈循环中的集中化。 |

<a id="by-training-strategies"></a>

### 训练策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="arafat26a-training-strategies"></a>[Adversarial Attacks and Robust Training for Hypergraph Neural Networks](https://proceedings.mlr.press/v306/arafat26a.html) · [论文卡](../conferences/icml-2026/cards/0101-0200.md#paper-arafat26a) | 超图鲁棒训练 | 把超图拉普拉斯作为统一的攻击目标，在同一预算框架下测试结构及特征扰动，再用相应扰动做超图模型的对抗训练。 |
| <a id="canturk26a-training-strategies"></a>[Can Computational Reducibility Lead to Transferable Models for Graph Combinatorial Optimization?](https://proceedings.mlr.press/v306/canturk26a.html) · [论文卡](../conferences/icml-2026/cards/0301-0400.md#paper-canturk26a) | 图组合优化迁移 | 用计算复杂性中的任务归约关系选择预训练组合，再共享图编码器微调。留一任务评测中，多任务预训练通常加快收敛。 |
| <a id="chen26cz-training-strategies"></a>[Message Tuning Outshines Graph Prompt Tuning: A Prismatic Space Perspective](https://proceedings.mlr.press/v306/chen26cz.html) | 图基础模型的消息微调 | 冻结预训练 GNN，在每层加入少量可学习的消息原型，并动态融合原型和原生消息。逐层改变消息聚合可提高适配能力，论文在其刻画的模型条件下给出了超出输入提示微调上界的构造。 |
| <a id="gao26ai-training-strategies"></a>[GKD-Recruiter: Jointly Modeling Social and Task Heterogeneity for Spatial Crowdsourcing via Graph Knowledge Distillation](https://proceedings.mlr.press/v306/gao26ai.html) | 空间众包的双视图蒸馏 | 以门控融合社交影响、工人任务匹配与邻居信息，并把融合表征蒸馏给单视图模型，帮助种子选择同时考虑邀请能否传播及被邀请者能否完成线下任务。 |
| <a id="gosch26a-training-strategies"></a>[Certifying Graph Neural Networks Against Label and Structure Poisoning](https://proceedings.mlr.press/v306/gosch26a.html) | 图分区投毒认证的半监督增强 | 各分区仅用本区可用信息生成伪标签或补边，再训练基模型，用集成票差计算能抵御的改动预算。分区增强减轻稀疏标签或边使基模型投票失真的问题。 |
| <a id="grover26a-training-strategies"></a>[Feedback Control for Multi-Objective Graph Self-Supervision](https://proceedings.mlr.press/v306/grover26a.html) | 图自监督任务的反馈式预算调度 | 按任务难度与目标间冲突制定各预训练目标的更新配额，再用 PID 控制器追踪每个目标已获得的更新块数。每块只训练一个目标，可显式纠正长期得不到更新的目标。 |

<a id="by-data-strategies"></a>

### 数据策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="azizpour26a-data-strategies"></a>[From Moments to Models: Graphon-Mixture Learning for Mixup and Contrastive Learning](https://proceedings.mlr.press/v306/azizpour26a.html) · [论文卡](../conferences/icml-2026/cards/0101-0200.md#paper-azizpour26a) | 图数据增强 | 用模体密度给图数据估计潜在生成分量，再让 mixup 与对比学习利用分量信息，避免把结构来源差异当作可任意混合的扰动。 |
| <a id="chen26cr-data-strategies"></a>[DANCE: Dynamic, Available, Neighbor-gated Condensation for Federated Text-Attributed Graphs](https://proceedings.mlr.press/v306/chen26cr.html) | 联邦文本图证据凝缩 | 每轮用上一轮的图编码器更新核心节点的邻居和句段选择，在逐跳预算和文本预算内聚合证据，并在客户端保留选中邻居和原句段的映射，以便审计压缩后的表征。 |
| <a id="eremeev26a-data-strategies"></a>[GraphPFN: A Prior-Data Fitted Graph Foundation Model](https://proceedings.mlr.press/v306/eremeev26a.html) | 图基础模型的合成预训练先验 | 叠合多个随机块模型以生成可重叠的社区，再用混合图聚合与逐节点变换的结构因果模型生成属性和标签，让预训练任务同时提供拓扑与属性依赖。 |

<a id="by-inference"></a>

### 推理策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="ai26c-inference"></a>[PromptDyG: Test-Time Prompt Adaptation on Dynamic Graphs](https://proceedings.mlr.press/v306/ai26c.html) · [论文卡](../conferences/icml-2026/cards/0001-0100.md#paper-ai26c) | 图模型测试时适应 | 冻结图骨干，用当前快照的无标签特征熵更新动态图提示，持续跟随图结构与测试分布的变化。 |
| <a id="bisht26b-inference"></a>[CARE: Adaptive Calibration for Reliable Recommendations](https://proceedings.mlr.press/v306/bisht26b.html) · [论文卡](../conferences/icml-2026/cards/0201-0300.md#paper-bisht26b) | 在线推荐校准 | 持续监测推荐损失并在用户行为变化时重新定阈值，同时在线调整不同集合预测器的权重，使可变长度推荐列表保持紧凑。 |
| <a id="fomina26a-inference"></a>[On Efficient Scaling of GNNs via IO-Aware Layers Implementations](https://proceedings.mlr.press/v306/fomina26a.html) | 图注意力的 I/O 融合优化 | 将逐边计算与邻居聚合融合在 GPU 核内，减少把边级中间量写回显存。图重排序的收益取决于线程映射，实验中对邻居并行的 gather 型核比对特征并行核更稳定。 |
| <a id="gao26t-inference"></a>[Beyond Explicit Edges: Robust Reasoning over Noisy and Sparse Knowledge Graphs](https://proceedings.mlr.press/v306/gao26t.html) | 知识图多跳搜索的语义补边 | 在语言模型引导的邻接遍历中，将高于嵌入相似度阈值的近邻也加入前沿，再排除已访问节点。这样可按查询跨过显式知识图中缺失的连接。 |
| <a id="guo26t-inference"></a>[GRASP: Graph Reasoning via Agentic Solving and Probing of LLMs](https://proceedings.mlr.press/v306/guo26t.html) | 按需探查图拓扑的工具推理 | 让智能体按推理需要查询节点邻居，并把连通性或数值计算交给代码解释器。这样可以在观测不足时主动扩大局部感受野，避免固定展开深度在部分数据上引入大量无关节点。 |
| <a id="guo26ac-inference"></a>[X-EviProbe: Post-hoc Parameter-Free Evidential Uncertainty Quantification for Frozen Graph Neural Networks](https://proceedings.mlr.press/v306/guo26ac.html) | 冻结图网络的后验不确定性证据 | 用节点潜表示的几何关系为 logit 证据总量做门控，再按原预测概率将总量分配成各类的 Dirichlet 参数。图传播作用于证据强度，使邻居可靠性可参与校准，同时沿用原分类模型。 |

<a id="by-representation-learning"></a>

### 表征学习

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="behmanesh26a-representation-learning"></a>[Graph Alignment via Dual-Pass Spectral Encoding and Latent Space Communication](https://proceedings.mlr.press/v306/behmanesh26a.html) · [论文卡](../conferences/icml-2026/cards/0201-0300.md#paper-behmanesh26a) | 跨图对齐 | 先向节点嵌入注入高频信息以保留局部区分度，再在对应映射上做低通平滑，分别处理节点过平滑与跨图匹配噪声。 |
| <a id="cai26f-representation-learning"></a>[CONTEXTOR: Contextualized High-order Contrastive Learning](https://proceedings.mlr.press/v306/cai26f.html) · [论文卡](../conferences/icml-2026/cards/0301-0400.md#paper-cai26f) | 高阶关系表征 | 把高阶关系拆成多个不完整查询与补全实体，用查询非对称地调制候选实体表征，再做对比对齐。 |
| <a id="chen26ak-representation-learning"></a>[SynGR: Unleashing the Potential of Cross-Modal Synergy for Generative Recommendation](https://proceedings.mlr.press/v306/chen26ak.html) | 跨模态生成式推荐 | 抑制模型过度依赖占优模态，让推荐生成器学习只有联合读取图像与文本才能辨识的商品属性。 |
| <a id="chen26fu-representation-learning"></a>[Boundary Embedding Shaping with Adaptive Contrastive Learning for Graph Structural Disentanglement](https://proceedings.mlr.press/v306/chen26fu.html) | 图节点边界的自适应对比更新 | 在类别嵌入簇的边界区域选择结构混杂的节点做对比学习。先虚拟更新边界注意力层并测量全图嵌入变化，再按变化量的倒数缩放实际更新，限制少量边界样本对其他节点的扰动。 |
| <a id="choromanski26a-representation-learning"></a>[Computationally-efficient Graph Modeling with Refined Graph Random Features](https://proceedings.mlr.press/v306/choromanski26a.html) | 短随机游走拼接图特征 | 把较长图游走的核估计拆成可并行采样的短游走，再用对应随机特征矩阵的乘积组合多段覆盖范围，在论文的构造下保留图核估计的无偏性。 |
| <a id="debaussart-joniec26a-representation-learning"></a>[Parametrized Power-Iteration Clustering for Directed Graphs](https://proceedings.mlr.press/v306/debaussart-joniec26a.html) | 有向图的参数化幂迭代聚类 | 先构造保留方向信息的可逆随机游走算子，再用选定扩散时间下的迭代算子行作节点嵌入。自动选择扩散时间并截断嵌入，可在弱连通有向图上省去特征分解并降低聚类开销。 |
| <a id="du26o-representation-learning"></a>[From Distribution to Geometry: Stable Graph Generalization via Invariant Barycenters](https://proceedings.mlr.press/v306/du26o.html) | 图分布的跨环境重心对齐 | 把各环境同类图的子图嵌入分布视为共享原型的不同变形，用 Wasserstein 重心估计这一原型。对齐各环境表征到同类重心，并以对抗训练分离仍可辨识环境的成分。 |
| <a id="ezoe26a-representation-learning"></a>[Unfolded Laplacian Spectral Embedding: A Theoretically Grounded Approach to Dynamic Network Representation](https://proceedings.mlr.press/v306/ezoe26a.html) | 动态图的展开归一化拉普拉斯嵌入 | 把各时刻的归一化拉普拉斯算子展开到同一谱嵌入空间。在动态随机块模型下，论文证明同一时刻的节点间比较和同一节点的跨时刻比较都具有稳定性，并用 Cheeger 型不等式把谱与跨时刻最差导通性联系起来。 |
| <a id="guo26p-representation-learning"></a>[CCLRec: Consensus-driven Contrastive Learning for LLM-enhanced Graph Recommendation](https://proceedings.mlr.press/v306/guo26p.html) | 结构与语义共识的推荐对比学习 | 分别从交互图邻域和语言模型的物品语义嵌入获取候选，再取交集形成高置信正样本。对比学习重点利用同时符合协同交互和语义相似性的样本对。 |

<a id="by-evaluation"></a>

### 评测与诊断

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="agbaje26a-evaluation"></a>[Revisiting Asymmetries in Black-box Link Stealing against Graph Neural Networks](https://proceedings.mlr.press/v306/agbaje26a.html) · [论文卡](../conferences/icml-2026/cards/0001-0100.md#paper-agbaje26a) | 图模型隐私评测 | 连边泄漏应在极低误报率下分组测量。同类节点的后验几何可能压缩判别方向，重调距离后会暴露平均结果遗漏的风险。 |
| <a id="akula26a-evaluation"></a>[Same Graph Cross-Task Transfer in GNNs: Protocols and Predictors](https://proceedings.mlr.press/v306/akula26a.html) · [论文卡](../conferences/icml-2026/cards/0001-0100.md#paper-akula26a) | 图模型迁移 | 同一图上，节点分类迁往链路预测在同质性强的图上更可靠。反向迁移要尤其关注结构信号强度，并固定消息传递图及测试负样本防止泄漏。 |
| <a id="ferrini26a-evaluation"></a>[Rethinking GNNs and Missing Features: Challenges, Evaluation and a Robust Solution](https://proceedings.mlr.press/v306/ferrini26a.html) | 缺失节点特征的压力测试 | 评估缺失特征时使用信息量较高的密集属性，并让更能预测标签的列具有更高的遮盖率。这样可测出在稀疏节点特征、均匀随机遮盖下不易暴露的性能退化。 |
| <a id="forbat26a-evaluation"></a>[Is Graph Mixup Beneficial? Investigating Interpolation And Empirical Performance of Graph Mixup Methods](https://proceedings.mlr.press/v306/forbat26a.html) | 图 Mixup 插值质量诊断 | 统一图分类的评测协议后，同时测合成图的插值误差和下游收益。高误差可拖累准确率，但低误差本身也未带来显著增益，所测 Mixup 方法均未显著优于无 Mixup 的基线。 |
| <a id="guan26b-evaluation"></a>[VENOMREC: Cross-Modal Interactive Poisoning for Targeted Promotion in Multimodal LLM Recommender Systems](https://proceedings.mlr.press/v306/guan26b.html) | 多模态推荐的同步污染诊断 | 分别评测单模态与联合污染对推荐曝光和正常效用的影响。论文发现视觉与文本扰动相互配合时，即使整体效用接近原模型，个别商品的曝光仍可能明显偏移，因此需单独测跨模态协同风险。 |

<a id="by-theory-statistics"></a>

### 理论与统计

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="adriaens26a-theory-statistics"></a>[Simple Algorithms for Bad Triangle Transversals with Applications to Correlation Clustering](https://proceedings.mlr.press/v306/adriaens26a.html) · [论文卡](../conferences/icml-2026/cards/0001-0100.md#paper-adriaens26a) | 相关聚类 | 完整符号图上，先找到击中所有恰有一条负边三角形的删除边集，再通过枢轴过程转成聚类，两类最优代价相差至多 1.5 倍。 |
| <a id="amran26a-theory-statistics"></a>[A Graphop Analysis of Graph Neural Networks on Sparse Graphs: Generalization and Universal Approximation](https://proceedings.mlr.press/v306/amran26a.html) · [论文卡](../conferences/icml-2026/cards/0001-0100.md#paper-amran26a) | 图神经网络理论 | 扩展 graphop 极限框架，构造跨图规模和稀疏度的紧致度量，用同一套等度连续性分析 MPNN 的泛化和逼近。 |
| <a id="badanidiyuru26a-theory-statistics"></a>[Model Monotonicity in Autobidding Auctions: When Do Better Predictions Lead to Better Outcomes?](https://proceedings.mlr.press/v306/badanidiyuru26a.html) · [论文卡](../conferences/icml-2026/cards/0101-0200.md#paper-badanidiyuru26a) | 拍卖中的预测改进 | 提高预测分辨率对拍卖收入的影响依赖出价规则。无预算限制的目标成本出价者满足文中的一价拍卖单调性，二价机制可打破它。 |
| <a id="badreddine26a-theory-statistics"></a>[On the Theoretical Limitations of Embedding-based Link Prediction](https://proceedings.mlr.press/v306/badreddine26a.html) · [论文卡](../conferences/icml-2026/cards/0101-0200.md#paper-badreddine26a) | 知识图谱链路预测 | 线性输出层使嵌入维度必须随图规模和连通性增长才能表达训练关系。混合式非线性输出可打破这一秩瓶颈，且参数开销较低。 |
| <a id="charpenay26a-theory-statistics"></a>[Faithful Relational Reasoning with Region-based Embeddings: Expressivity of Convex Coordinate-wise Models](https://proceedings.mlr.press/v306/charpenay26a.html) · [论文卡](../conferences/icml-2026/cards/0401-0500.md#paper-charpenay26a) | 关系嵌入表达力 | 用逐坐标比较定义的凸区域能高效编码部分关系规则，但参数化会限制可忠实表达的规则集合，应按目标规则选区域形式。 |
| <a id="colini-baldeschi26a-theory-statistics"></a>[Multicalibration Yields Better Matchings](https://proceedings.mlr.press/v306/colini-baldeschi26a.html) | 用匹配决策约束边权多重校准 | 从竞争的匹配规则提取边权残差的校准约束，再用校准后的权重做普通最大权匹配。在论文的随机边权设定下，这可使所得决策与在原预测上使用比较类中最优规则的表现竞争。 |
| <a id="fan26c-theory-statistics"></a>[Graph-Preference Learning: Debiasing Network-Sampled Human Feedback for Target Welfare Estimation](https://proceedings.mlr.press/v306/fan26c.html) | 网络抽样偏好的福利校正 | 让相邻标注者共享奖励模型信息，再用稳定化的目标权重与入样概率之比聚合个人奖励。若反馈招募偏向网络中心，这可减小聚合奖励偏离预设目标群体福利的程度。 |
| <a id="fetrat-qharabagh26a-theory-statistics"></a>[Learning to Execute Graph Algorithms Exactly with Graph Neural Networks](https://proceedings.mlr.press/v306/fetrat-qharabagh26a.html) | 图算法的局部指令精确执行 | 先用 MLP 集成学习单节点的局部指令，再把它作为图网络的消息更新函数。在度数、状态大小及消息精度有界的理论设定下，网络可高概率无误地执行 LOCAL 算法。 |
| <a id="flora26a-theory-statistics"></a>[Understanding Truncated Positional Encodings for Graph Neural Networks](https://proceedings.mlr.press/v306/flora26a.html) | 截断图位置编码的表达能力 | 完整谱编码与随机游走编码虽同等可表达，截断后不同编码可区分的图会分化。论文给出截断谱编码无法保留相对 1-WL 的严格优势的例子，并在真实数据上验证混合多类截断编码的收益。 |
| <a id="guo26d-theory-statistics"></a>[Delving into Non-Exchangeability for Conformal Prediction in Graph-Structured Multivariate Time Series](https://proceedings.mlr.press/v306/guo26d.html) | 图时序的条件频谱共形校准 | 用图小波分解预测残差，将低频全局趋势编码为条件，对高频残差做自适应共形校准。给定低频信息后高频残差满足交换性时，可得到文中有限样本覆盖保证。 |
<!-- classification:end -->
