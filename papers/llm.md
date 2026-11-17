# 大语言模型

[首页](../README.md) · [参与贡献](../CONTRIBUTING.md) · [English](../en/papers/llm.md)

语言建模、后训练与推理。

<!-- classification:start -->
## 按技术类型浏览

<a id="by-architecture"></a>

### 模型架构

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="arriola26a-architecture"></a>[Set Diffusion: Interpolating Token Orderings between Autoregression and Diffusion for Fast and Flexible Decoding](https://proceedings.mlr.press/v306/arriola26a.html) | 离散扩散解码 | 按位置和长度可变的 token 集合因子化似然，用集合因果结构在每步更新 KV 缓存，从而支持滑窗和自选顺序解码。 |
| <a id="bui26b-architecture"></a>[HiMAP-Travel: Hierarchical Multi-Agent Planning for Long-Horizon Constrained Travel](https://proceedings.mlr.press/v306/bui26b.html) | 长任务 Agent 协作 | 调度器先分配子任务资源，再让执行器并行规划；共享约束经事务检查，无法满足子目标时执行器可拒绝并触发重规划。 |
| <a id="chen26r-architecture"></a>[MARS: Modular Agent with Reflective Search for Automated AI Research](https://proceedings.mlr.press/v306/chen26r.html) | 科研 Agent 搜索 | 用有预算约束的树搜索分配昂贵训练评估，先把方案拆成模块再实现，并从不同搜索分支的结果差异提取可以复用的经验。 |
| <a id="chen26cg-architecture"></a>[LoKiFormer: Locality-aware Attention with Decoupled Knowledge Memory for Efficient Large Language Model Pretraining](https://proceedings.mlr.press/v306/chen26cg.html) | 局部注意力与参数化记忆 | 在解码器中用分组卷积为各注意力头融合邻近词元，再用压缩的键值表征查询独立的可训练键值记忆，使局部模式建模和序列外知识检索各有专门通路。 |

<a id="by-modules"></a>

### 模块

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="bonnet26a-modules"></a>[Learning to Remember, Learn, and Forget in Attention-Based Models](https://proceedings.mlr.press/v306/bonnet26a.html) | 线性注意力记忆 | 为每个注意力状态维护重要性，用它调节状态可塑性，使固定容量记忆根据此前积累的知识决定可更新程度。 |
| <a id="byun26a-modules"></a>[Bounded Hyperbolic Tangent: A Stable and Efficient Alternative to Pre-Layer Normalization in Large Language Models](https://proceedings.mlr.press/v306/byun26a.html) | 归一化替换 | 把 tanh 输入约束在非饱和区间来控制深层激活增长，每个块只计算一次精确统计量，另一处用轻量的方差估计替代。 |
| <a id="chao26b-modules"></a>[SpanNorm: Reconciling Training Stability and Performance in Deep Transformers](https://proceedings.mlr.press/v306/chao26b.html) | 深层 Transformer 归一化 | 保留无障碍的残差路径，同时对块输出采用类似 PostNorm 的计算，再配合缩放控制深度方向的信号方差。 |
| <a id="charakorn26a-modules"></a>[Doc-to-LoRA: Learning to Instantly Internalize Contexts](https://proceedings.mlr.press/v306/charakorn26a.html) | 上下文转 LoRA | 用元训练的超网络一次前向把新文档转成 LoRA 权重，后续问答可复用该适配器，减少重复读文档的注意力和 KV 缓存开销。 |
| <a id="chen26aw-modules"></a>[Multi-Head Attention as a Source of Catastrophic Forgetting in MoE Transformers](https://proceedings.mlr.press/v306/chen26aw.html) | MoE 持续学习 | 拼接全部注意力头后统一路由，可能把需要不同梯度更新的信号送到同一专家。按头细化路由可减少组合冲突和旧任务遗忘。 |
| <a id="chen26dj-modules"></a>[SimpleGPT: Improving GPT via A Simple Normalization Strategy](https://proceedings.mlr.press/v306/chen26dj.html) | 线性投影后的局部归一化 | 把 RMSNorm 接在每个注意力和前馈线性投影之后，并去掉块级预归一化，让各中间激活在产生时就受尺度约束。在论文的 GPT 实验中，该结构容许比基线更大的学习率。 |
| <a id="chen26dw-modules"></a>[Toward Stable Value Alignment: Introducing Independent Modules for Consistent Value Guidance](https://proceedings.mlr.press/v306/chen26dw.html) | 独立价值空间的桥接词元 | 把冻结主干的隐状态投影到独立价值空间，取对齐判别器的梯度作为纠偏信号。用交叉注意力把该信号与上下文合成为桥接词元，并随解码更新引导。 |

<a id="by-loss-functions"></a>

### 损失函数

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="abas26a-loss-functions"></a>[TUR-DPO: Topology- and Uncertainty-Aware Direct Preference Optimization](https://proceedings.mlr.press/v306/abas26a.html) | 偏好学习 | 把回答抽成主张及其依赖图，用推理结构质量和不确定性加权偏好训练。 |
| <a id="aouad26a-loss-functions"></a>[The Sign Estimator: Preference Modeling for LLM Alignment under Heterogeneity](https://proceedings.mlr.press/v306/aouad26a.html) | 异质偏好学习 | 把成对偏好的交叉熵改成二分类式损失，在论文的假设下，学到的排序与总体平均效用一致。 |
| <a id="chen26bi-loss-functions"></a>[What Makes Effective Supervision in Latent Chain-of-Thought: An Information-Theoretic Analysis](https://proceedings.mlr.press/v306/chen26bi.html) | 潜在思维链的重建监督 | 逐步用潜状态替换显式推理步骤时，额外训练解码器用潜状态重建对应的推理词元。在文中任务上，该辅助监督优于用均方误差将潜状态拉向推理词元的平均嵌入。 |
| <a id="chen26br-loss-functions"></a>[$φ$-Balancing for Mixture-of-Experts Training](https://proceedings.mlr.press/v306/chen26br.html) | MoE 软路由负载均衡 | 对各专家的软路由概率维护指数移动平均，用全局凸均衡势函数在该均值处的梯度作为专家代价。计算辅助损失时停止代价的梯度，只对当前批次的路由概率反传，降低硬分派统计带来的波动。 |
| <a id="chen26el-loss-functions"></a>[Discrete Tilt Matching](https://proceedings.mlr.press/v306/chen26el.html) | 离散扩散的奖励倾斜匹配 | 从基础掩码扩散模型采样完整序列，按终局奖励的指数给去掩码交叉熵加权，并用基础模型的去掩码分布构造控制变量。该目标在加权条件均值保持不变时匹配奖励倾斜后的后验，无需求序列边际似然。 |

<a id="by-optimization"></a>

### 优化

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="abbasi26a-optimization"></a>[Zero Sum SVD: Balancing Loss Sensitivity for Low Rank LLM Compression](https://proceedings.mlr.press/v306/abbasi26a.html) | 模型压缩 | 在全模型固定参数预算下，用校准损失的一阶估计决定跨层删哪些奇异成分。 |
| <a id="cai26a-optimization"></a>[AdaMeZO: Adam-style Zeroth-Order Optimizer for LLM Fine-tuning Without Maintaining the Moments](https://proceedings.mlr.press/v306/cai26a.html) | 低显存零阶微调 | 在只需前向计算的零阶微调中引入 Adam 式一阶和二阶矩估计，同时省去持久化矩状态，以少量显存获得更快收敛。 |
| <a id="castin26a-optimization"></a>[Balanced LoRA: Removing Parameter Invariance to Accelerate Convergence](https://proceedings.mlr.press/v306/castin26a.html) | LoRA 收敛 | 同一个低秩权重更新可以由多组因子得到，而各组因子的条件数不同。将因子投影到平衡流形，保持乘积不变的同时改善收敛条件。 |
| <a id="chen26z-optimization"></a>[WUSH: Near-Optimal Adaptive Transforms for LLM Quantization](https://proceedings.mlr.press/v306/chen26z.html) | 权重激活联合量化 | 把 Hadamard 变换与数据驱动的二阶矩校正结合，在分块最大绝对值量化前调节离群值影响，使权重和激活共享更适合低位宽的变换。 |
| <a id="chen26ba-optimization"></a>[SPARD: Defending Harmful Fine-Tuning Attack via Safety Projection with Relevance–Diversity Data Selection](https://proceedings.mlr.press/v306/chen26ba.html) | 有约束的安全微调 | 在任务效用更新之间插入基于安全样本的投影步骤，再用相关性和多样性联合筛选安全集，使少量样本覆盖更丰富的安全约束。 |
| <a id="chen26bl-optimization"></a>[Reward-free Alignment for Conflicting Objectives](https://proceedings.mlr.press/v306/chen26bl.html) | 多目标偏好梯度裁剪 | 直接从成对偏好计算各目标梯度，用冲突规避梯度下降求修正项，再用各自的用户偏好权重为修正系数设上限，减少更新方向过度偏向低权重目标。 |
| <a id="chen26bt-optimization"></a>[BPDQ: Bit-Plane Decomposition Quantization on a Variable Grid for Large Language Models](https://proceedings.mlr.press/v306/chen26bt.html) | 可变网格低比特量化 | 用多个二进制位平面与可调标量系数构建组内量化网格，在近似 Hessian 定义的度量中交替细化位平面和系数，并对尚未量化的权重补偿误差，以减少 2–3 比特量化造成的层输出偏差。 |
| <a id="chen26eq-optimization"></a>[Escaping the Subspace Trap: The Role of Optimizer Geometry in Model Width Expansion](https://proceedings.mlr.press/v306/chen26eq.html) | 宽度扩展后的优化器几何 | 函数保持式扩宽后的梯度能量可能仍集中在种子模型诱导的子空间。用 Muon 对矩阵更新做近似正交化，可把更新分量分到新增维度，使续训利用扩宽后的容量。 |
| <a id="chen26ew-optimization"></a>[SCHUR-A*: Layer-wise Optimal Expert Pruning for MoEs via Schur-Complement Guided A* Search](https://proceedings.mlr.press/v306/chen26ew.html) | MoE 专家组合剪枝 | 给定每层专家预算，以重新线性拟合该层原始输出的误差给专家组合评分，再用舒尔补为剩余选择的潜在收益设上界，让 A* 剪掉无法改进当前解的搜索分支。 |
| <a id="chen26ex-optimization"></a>[QiMeng-PerceptOS: Semantic-Aware Kernel Optimization for OS-Intensive Workloads via Hardware-Software Alignment](https://proceedings.mlr.press/v306/chen26ex.html) | 遥测反馈驱动内核调优 | 把热点调用栈和硬件拓扑压缩成语言模型可读取的运行摘要，再用分层配置树同时呈现局部选项和子系统摘要，指导配置搜索与剪枝，并把实际运行性能反馈给下一轮。 |
| <a id="chen26fe-optimization"></a>[Towards Disentangled Preference Optimization Dynamics: Suppress the Loser, Preserve the Winner](https://proceedings.mlr.press/v306/chen26fe.html) | 偏好更新的梯度激励校准 | 将不同偏好目标的梯度拆成胜负回答两个方向及对应权重，在反向传播中把权重比调进由局部梯度关系决定的区间。论文的一阶分析表明，该条件可在压低落选回答似然的同时保住入选回答。 |

<a id="by-reinforcement-learning"></a>

### 强化学习方法

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="ackermann26a-reinforcement-learning"></a>[Gradient Regularization Mitigates Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards](https://proceedings.mlr.press/v306/ackermann26a.html) | 奖励优化 | 惩罚 RL 目标对策略参数的梯度范数，并用有限差分近似该正则项的梯度，以减轻代理奖励优化过头。 |
| <a id="agarwal26e-reinforcement-learning"></a>[Learning When to Act or Refuse: Guarding Agentic Reasoning Models for Safe Multi-Step Tool Use](https://proceedings.mlr.press/v306/agarwal26e.html) | Agent 后训练 | 把检查放到工具执行前，让继续与拒绝都成为显式动作，再用成对轨迹偏好训练整个多步决策过程。 |
| <a id="agnihotri26a-reinforcement-learning"></a>[Multi-Objective Preference Optimization: Improving Human Alignment of Generative Models](https://proceedings.mlr.press/v306/agnihotri26a.html) | 多目标偏好优化 | 用成对偏好优化主目标，把其他目标写为可调最低要求，避免为帮助性与安全性预设固定线性权重。 |
| <a id="arnal26a-reinforcement-learning"></a>[Efficient RL Training for LLMs with Experience Replay](https://proceedings.mlr.press/v306/arnal26a.html) | LLM 强化学习 | 生成昂贵时可以复用历史 rollout，显式平衡数据陈旧导致的方差与样本多样性，以较少生成计算维持最终性能和策略熵。 |
| <a id="baek26a-reinforcement-learning"></a>[D-FUSEr: Diverse Failure, Unified Success via Error-Distribution Shaping in LLM Reasoning](https://proceedings.mlr.press/v306/baek26a.html) | 测试时推理 | 多数投票的上限受错误答案是否集中影响。训练时奖励错误样本的适度分歧，或推理时识别并降权最常见误答，都可以提高聚合准确率。 |
| <a id="bai26k-reinforcement-learning"></a>[D-ARL: A Distribution-Matched Asynchronous Reinforcement Learning Framework for Language Reasoning](https://proceedings.mlr.press/v306/bai26k.html) | 异步强化学习 | 用方差引导的分布匹配指标从最近 K 个行为策略筛选回放轨迹，再进行多行为策略优化，削弱 rollout 滞后造成的分布偏移。 |
| <a id="ball26b-reinforcement-learning"></a>[Don’t Walk the Line: Boundary Guidance for Filtered Generation](https://proceedings.mlr.press/v306/ball26b.html) | 生成安全对齐 | 用强化学习增加输出到安全分类器判界的距离，减少生成内容贴着判界时的误过滤和漏过滤。 |
| <a id="bamba26b-reinforcement-learning"></a>[XRPO: Pushing the Limits of GRPO with Targeted Exploration and Exploitation](https://proceedings.mlr.press/v306/bamba26b.html) | GRPO 探索 | 将 rollout 分给预期能减少更多不确定性的提示，对零奖励题注入示例启动探索，再提升低概率正确解的组内优势。 |
| <a id="bi26a-reinforcement-learning"></a>[EchoRL: Reinforcement Learning via Rollout Echoing](https://proceedings.mlr.press/v306/bi26a.html) | 可验证奖励强化学习 | 即使一组 rollout 全部正确、相对优势为零，也能按步骤熵抽取关键片段，并将其回灌为辅助监督。 |
| <a id="bi26c-reinforcement-learning"></a>[Reward and Guidance through Rubrics: Promoting Exploration to Improve Multi-Domain Reasoning](https://proceedings.mlr.press/v306/bi26c.html) | 多领域推理强化学习 | 同一套评分细则可以同时提供在线 rollout 的细粒度奖励和离线探索指引，降低只依赖结果验证时的搜索局限。 |
| <a id="cai26b-reinforcement-learning"></a>[From Player to Master: Enhancing Test-Time Learning of LLM Agents via Reinforcement Learning over Memory](https://proceedings.mlr.press/v306/cai26b.html) | Agent 测试时记忆 | 冻结执行任务的 LLM，把每轮记忆更新作为另一个可训练策略。用逐轮奖励和跨轨迹的同轮相对优势给长期收益分配信用。 |
| <a id="cai26c-reinforcement-learning"></a>[Beyond Euclidean Clipping: Overcoming Exploration Collapse in LLM RL via Riemannian Isometric Policy Optimization](https://proceedings.mlr.press/v306/cai26c.html) | 策略更新几何 | 按策略黎曼流形的距离调整更新，缓解欧式裁剪在低概率区域更新过保守、高概率区域更新过激的现象。 |
| <a id="cai26k-reinforcement-learning"></a>[Escaping the Verifier: Learning to Reason via Demonstrations](https://proceedings.mlr.press/v306/cai26k.html) | 示范驱动的逆强化学习 | 让相对判别器从专家答案与策略答案的成对比较中学奖励，同时用该奖励更新生成策略，可在缺少任务验证器时使用专家示范训练推理。 |
| <a id="cao26y-reinforcement-learning"></a>[Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification in Language Models](https://proceedings.mlr.press/v306/cao26y.html) | 形式逻辑过程奖励 | 在自然语言推理过程中交错执行符号验证，直接给中间步骤的逻辑错误反馈，再用这些信号做监督训练和策略优化。 |
| <a id="chai26c-reinforcement-learning"></a>[GXPO: Group Cross-Lingual Relative Policy Optimization for Code Generation](https://proceedings.mlr.press/v306/chai26c.html) | 跨语言代码强化学习 | 对同一道编程题，用多种语言生成解并组成一个训练组，将语言内与跨语言的相对优势一起优化，让低资源语言利用共享解题信号。 |
| <a id="chen26a-reinforcement-learning"></a>[Train for Truth, Keep the Skills: Binary Retrieval-Augmented Reward Mitigates Hallucinations](https://proceedings.mlr.press/v306/chen26a.html) | 事实性二元奖励 | 用检索证据检查回答，只要有一处事实矛盾就给 0 分，否则给 1 分。论文分析表明，这能压低含错回答的概率，同时保持无错回答之间的相对分布。 |
| <a id="chen26k-reinforcement-learning"></a>[PowerFlow: Unlocking the Dual Nature of LLMs via Principled Distribution Matching](https://proceedings.mlr.press/v306/chen26k.html) | 无监督强化学习分布匹配 | 用长度感知的 GFlowNet 目标拟合模型自身分布的幂次。指数大于 1 时集中到高概率推理轨迹，小于 1 时保留更多表达多样性。 |
| <a id="chen26w-reinforcement-learning"></a>[Hista and Numca: Estimate State Value Effectively for Large Language Model Reinforcement Learning](https://proceedings.mlr.press/v306/chen26w.html) | 语言模型状态价值估计 | 可把数字片段作为有对错反馈的局部里程碑，也可按相似隐藏状态对其他轨迹的回报加权，两种方法都比单纯的组平均提供更细的状态价值。 |
| <a id="chen26bh-reinforcement-learning"></a>[Learning to Reason for Factuality](https://proceedings.mlr.press/v306/chen26bh.html) | 长回答事实性奖励 | 把平滑后的事实精确率、已核实事实数量的对数项及相对参考答案的相关性评分合成在线强化学习奖励，以减少模型靠删减事实细节或答非所问刷高精确率的空间。 |
| <a id="chen26ec-reinforcement-learning"></a>[Beyond Token-level Supervision: Unlocking the Potential of Decoding-based Regression via Reinforcement Learning](https://proceedings.mlr.press/v306/chen26ec.html) | 生成式数值回归的奖励与蒸馏 | 完整数字解码后用数值距离给 ReMax 提供序列级奖励，同时让专家沿模型实际生成的前缀选择最接近目标值的下一 token。即使前缀已产生错误，蒸馏仍可教模型用后续位减小数值偏差。 |
| <a id="chen26es-reinforcement-learning"></a>[Learning to Self-Verify Makes Language Models Better Reasoners](https://proceedings.mlr.press/v306/chen26es.html) | 生成与自验证交替训练 | 用 GRPO 分别优化答案正确性奖励和判断答案是否正确的奖励。交替训练时，用上一生成阶段采出的答案构造验证样本，使同一策略练习识别自身当前会犯的错误。 |
| <a id="chen26fi-reinforcement-learning"></a>[OnePO: Direct One-stage Policy Optimization for SFT-free Domain Adaptation](https://proceedings.mlr.press/v306/chen26fi.html) | 领域强化学习中的教师退出 | 在单阶段 RL 中把教师回答与在线采样一起评分，早期抬高低概率优质教师词元的更新信号。当某个教师回答的奖励被在线策略的前沿超过时停止使用它，使后续探索能脱离教师分布。 |

<a id="by-training-strategies"></a>

### 训练策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="adepu26a-training-strategies"></a>[Fine-Tuning of Transformer models with Frames](https://proceedings.mlr.press/v306/adepu26a.html) | 参数高效微调 | 多层共享可算法生成的融合框架基底，只存储和训练稀疏的展开系数，以压低微调的显存和参数开销。 |
| <a id="adila26a-training-strategies"></a>[Weight Updates as Activation Shifts: A Principled Framework for Steering](https://proceedings.mlr.press/v306/adila26a.html) | 激活干预 | 一阶近似把权重更新对应到激活变化，据此可把干预放在整个 Transformer 块的输出，还可以与权重微调联合训练。 |
| <a id="amin26a-training-strategies"></a>[Consistent Diffusion Language Models](https://proceedings.mlr.press/v306/amin26a.html) | 离散扩散加速 | 用两个噪声层级之间的精确离散后验桥做一致性监督，让去噪器对不同随机路径在期望上给出一致结果，可单阶段训练。 |
| <a id="asadulaev26a-training-strategies"></a>[Latent Reasoning in TRMs is Secretly a Policy Improvement Operator](https://proceedings.mlr.press/v306/asadulaev26a.html) | 递归潜空间推理 | 把循环更新看作逐步改进策略，从强化学习和扩散借训练方法，让更少次的 Tiny Recursive Model 前向仍保持任务表现。 |
| <a id="asawa26a-training-strategies"></a>[How to Train Your Advisor: Steering Black-Box LLMs with Advisor Models](https://proceedings.mlr.press/v306/asawa26a.html) | 黑盒模型适配 | 训练小型开源模型按输入生成动态建议，把优化后的建议插入黑盒模型提示。在廉价学生上训练的顾问也能迁往闭源模型。 |
| <a id="bao26b-training-strategies"></a>[Towards Steering without Sacrifice: Principled Training of Steering Vectors for Prompt-only Interventions](https://proceedings.mlr.press/v306/bao26b.html) | 激活控制 | 联合学习干预方向和强度，只在少数提示词位置应用激活偏移，省掉逐向量调系数并减少对生成质量的干扰。 |
| <a id="berthon26a-training-strategies"></a>[Skill Neologisms: Towards Skill-based Continual Learning](https://proceedings.mlr.press/v306/berthon26a.html) | 技能持续学习 | 为新技能各训练一个软词表 token，固定主模型权重。独立训练的技能 token 在实验中可直接组合处理新任务。 |
| <a id="bian26b-training-strategies"></a>[Future-Gain Guided Test-Time Learning for Large Language Models](https://proceedings.mlr.press/v306/bian26b.html) | 测试时语言模型学习 | 只用能降低后续生成不确定性的 token 更新模型，并按增益和置信度控制步幅，减少前序解码错误被自训练放大的风险。 |
| <a id="bick26a-training-strategies"></a>[Retrieval-Aware Distillation for Transformer-SSM Hybrids](https://proceedings.mlr.press/v306/bick26a.html) | Transformer 到 SSM 蒸馏 | 先用检索任务消融找出必要的注意力头，只保留这部分头并蒸馏其余模块。检索由稀疏注意力承担后，也可以缩小循环状态。 |
| <a id="borodin26a-training-strategies"></a>[Diffract: Spectral View of LLM Domain Adaptation](https://proceedings.mlr.press/v306/borodin26a.html) | 持续预训练 | 领域适配主要改变权重的奇异向量，奇异值谱变化较小。按领域给各注意力头评分，再把低分头恢复到基座状态，可减少无用更新。 |
| <a id="bu26a-training-strategies"></a>[Provable Sample Efficiency of Curriculum Post-Training for Transformer Reasoning](https://proceedings.mlr.press/v306/bu26a.html) | 推理后训练课程 | 把推理任务排成逐渐加深的步骤，或逐渐撤掉提示。在论文的推理树假设下，这两种课程可把后训练样本复杂度从指数降到多项式。 |
| <a id="bu26c-training-strategies"></a>[Scaling depth capacity via zero/one-layer model expansion](https://proceedings.mlr.press/v306/bu26c.html) | 渐进式模型训练 | 用较浅前缀训练并逐步扩层，通过新层初始化和学习率日程把已有模型的能力传到更深模型，减少昂贵的深层训练步数。 |
| <a id="casademunt26a-training-strategies"></a>[Steering Out-of-Distribution Generalization with Concept Ablation Fine-Tuning](https://proceedings.mlr.press/v306/casademunt26a.html) | 微调泛化干预 | 在微调的前向激活中用线性投影消除不希望被强化的概念方向，使相同训练数据产生不同的域外泛化行为。 |
| <a id="chen26an-training-strategies"></a>[Beyond Two-Stage Training: Cooperative SFT and RL for LLM Reasoning](https://proceedings.mlr.press/v306/chen26an.html) | 监督微调与强化学习协同 | 交替更新联合梯度和小型协调 LoRA，用联合更新相对纯 RL 更新的奖励增量决定监督梯度该贡献多少。 |
| <a id="chen26ap-training-strategies"></a>[Know More, Know Clearer: A Meta-Cognitive Framework for Knowledge Augmentation in Large Language Models](https://proceedings.mlr.press/v306/chen26ap.html) | 知识纠错与置信校准 | 先用内部信号区分已掌握、混淆和缺失的知识，再对不同区域施加不同干预，并让主观置信度与测得正确性对齐。 |
| <a id="chen26cl-training-strategies"></a>[TetraJet-v2: Accurate NVFP4 Training for Large Language Models with Oscillation Suppression and Outlier Control](https://proceedings.mlr.press/v306/chen26cl.html) | 4 位训练权重振荡 | 在 NVFP4 训练后期，用量化权重与主权重的累计变化量之比识别在量化边界附近反复跳变的权重，再把这些主权重重置到当前量化区间中心，保留当下的量化取值。 |
| <a id="chen26do-training-strategies"></a>[Retaining by Doing: The Role of On-Policy Data in Mitigating Forgetting](https://proceedings.mlr.press/v306/chen26do.html) | 后训练的近似在策略数据 | 迭代式监督微调在每轮开头用当时的模型重新生成训练数据。在论文的对照实验中，按轮刷新样本可明显减轻旧任务遗忘，同时维持与标准监督微调相当或更高的目标任务准确率。 |
| <a id="chen26em-training-strategies"></a>[Steering Beyond the Support: Adversarial Training on Unsupervised Jailbroken Activation Simulation](https://proceedings.mlr.press/v306/chen26em.html) | 拒答引导的激活对抗训练 | 从拒答激活出发，沿无监督发现的潜方向生成当前引导场难以纠正的训练样本。外层学习标量势函数，使其梯度在推理时把模拟越狱激活推回拒答区域，同时约束对正常请求激活的改动。 |

<a id="by-data-strategies"></a>

### 数据策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="aden-ali26a-data-strategies"></a>[Subliminal Effects in Your Data: A General Mechanism via Log-Linearity](https://proceedings.mlr.press/v306/aden-ali26a.html) | 数据选择 | 按教师模型对两种条件下回答的 logit 对比挑子集，可以在没有显式目标标签的数据里诱导隐藏行为。 |
| <a id="agrawal26a-data-strategies"></a>[Minibatch selection for Language Models via Partition Matroid Constrained Gradient Matching](https://proceedings.mlr.press/v306/agrawal26a.html) | 训练数据选择 | 保留每个数据域的配额，再用一个验证梯度匹配目标跨域联合选样，可减少同一 batch 内的重复或冲突梯度。 |
| <a id="arraf26a-data-strategies"></a>[Learning Rewrite-Invariant Reasoning with Targeted Alternation Training](https://proceedings.mlr.press/v306/arraf26a.html) | 改写稳定性 | 从等义改写采样多条推理轨迹，合并成中间步骤图定位出错分叉，再针对有影响的改写方式构造少量训练或上下文示例。 |
| <a id="arx26a-data-strategies"></a>[AutoBaxBuilder: Bootstrapping Code Security Benchmarking](https://proceedings.mlr.press/v306/arx26a.html) | 代码安全评测 | 为同一任务生成两套测试，一套验证功能，另一套用端到端探针验证漏洞，避免功能正确掩盖安全缺陷。 |
| <a id="azarbal26a-data-strategies"></a>[Recontextualization Mitigates Specification Gaming Without Modifying the Specification](https://proceedings.mlr.press/v306/azarbal26a.html) | 奖励投机 | 先在明确要求遵循预期行为的提示下生成训练回答，再把回答配回允许走捷径的提示，可在沿用原监督的情况下减少投机。 |
| <a id="badertdinov26a-data-strategies"></a>[SWE-rebench V2: Language-Agnostic SWE Task Collection at Scale](https://proceedings.mlr.press/v306/badertdinov26a.html) | 代码 Agent 训练数据 | 由设置 Agent 为真实仓库生成安装和测试流程，用容器固定执行环境，再以多评审筛掉描述不足或测试过严的训练任务。 |
| <a id="behnia26a-data-strategies"></a>[Facts in Stats: Impacts of Pretraining Diversity on Language Model Generalization](https://proceedings.mlr.press/v306/behnia26a.html) | 事实预训练 | 在可控语料中，提高事实出现的上下文多样性会拖慢域内记忆，而多样性太低会损害部分域外泛化，合适的设置取决于预算。 |
| <a id="bu26b-data-strategies"></a>[Recovering Policy-Induced Errors: Benchmarking and Trajectory Synthesis for Robust GUI Agents](https://proceedings.mlr.press/v306/bu26b.html) | GUI Agent 错误恢复 | 用树状搜索主动发现 Agent 自己可能造成的错误，并给各分支合成恢复步骤。可执行的错误用例也能单独衡量恢复能力。 |
| <a id="chae26a-data-strategies"></a>[Safe and Scalable Web Agent Learning via Recreated Websites](https://proceedings.mlr.press/v306/chae26a.html) | 网页 Agent 训练环境 | 把真实网站重建为可重置的合成环境，再由内部 API 检查任务是否完成，可规模化生成带确定奖励的交互任务。 |
| <a id="chandak26a-data-strategies"></a>[Curating the Future: A Scalable Recipe for Training Open-Ended Forecasters](https://proceedings.mlr.press/v306/chandak26a.html) | 开放预测训练数据 | 从过往新闻合成可判定的预测题并筛掉劣质样本；训练、检索和评测都按时间截断新闻，可以控制未来信息泄漏。 |
| <a id="chen26cb-data-strategies"></a>[Threat2Traffic: Multi-Agent Environment Synthesis for Malware Traffic Generation from Threat Intelligence](https://proceedings.mlr.press/v306/chen26cb.html) | 威胁情报驱动的流量数据构造 | 多智能体从威胁情报中提取样本依赖并汇总到证据图，结合证据解决冲突，再对隔离测试环境的配置做语法与语义双层验证，用于采集与样本行为对应的流量数据。 |
| <a id="chen26dd-data-strategies"></a>[Olmix: A Framework for Data Mixing Throughout LM Development](https://proceedings.mlr.press/v306/chen26dd.html) | 语料域变动后的混合比例复用 | 增删语料域时固定未受影响域之间的相对权重，只重新估计它们的总占比和受影响域的权重。若新旧域的最优比例耦合较强，可放开部分旧域权重重新估计。 |

<a id="by-inference"></a>

### 推理策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="abdullaev26a-inference"></a>[Concept Heterogeneity-aware Representation Steering](https://proceedings.mlr.press/v306/abdullaev26a.html) | 表征干预 | 同一概念有多种表现时，用高斯混合分组和最优传输得到随输入变化的激活偏移。 |
| <a id="ai26a-inference"></a>[An Interactive Paradigm for Deep Research](https://proceedings.mlr.press/v306/ai26a.html) | 交互式研究 Agent | 在研究流程的决策点权衡询问成本和预期收益，结合不断更新的用户偏好选择追问还是继续检索与综合。 |
| <a id="ai26d-inference"></a>[Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information](https://proceedings.mlr.press/v306/ai26d.html) | 多模型答案聚合 | 投票时利用模型间的可靠性差异与相关性，以一阶及二阶统计量修正等权多数票。 |
| <a id="akhauri26a-inference"></a>[Compute Where it Counts: Self Optimizing Language Models](https://proceedings.mlr.press/v306/akhauri26a.html) | 动态推理预算 | 固定教师强制的 token 序列，对同一序列采样多套计算调度，再用组相对优化训练逐 token 的稀疏度、剪枝和量化选择。 |
| <a id="alazraki26a-inference"></a>[Scaling Small Agents Through Strategy Auctions](https://proceedings.mlr.press/v306/alazraki26a.html) | 小模型 Agent 路由 | 让不同规模 Agent 提交执行计划，再按预计成本和价值选中标者。共享历史竞价记忆即可调整路由策略。 |
| <a id="ardoin26a-inference"></a>[LLM Self-Recognition: Steering and Retrieving Activation Signatures](https://proceedings.mlr.press/v306/ardoin26a.html) | 模型文本溯源 | 生成时以随机稀疏向量偏移残差流，检测时读模型激活，可把可恢复的生成器指纹留在文本里。 |
| <a id="asad26a-inference"></a>[RedDebate: Safer Responses Through Multi-Agent Red Teaming Debates](https://proceedings.mlr.press/v306/asad26a.html) | 多 Agent 红队 | 让多模型通过辩论暴露风险，并把发现写入可检索的长期记忆，使后续推理能复用以往攻击与防护经验。 |
| <a id="bai26f-inference"></a>[PRISM: Efficient Test-Time Scaling via Hierarchical Search and Self-Verification for Discrete Diffusion Language Models](https://proceedings.mlr.press/v306/bai26f.html) | 离散扩散搜索 | 在去噪前中期按模型自评剪枝，再只重掩码部分低置信 token 以探索局部候选，可以减少达到同等 best-of-N 表现所需的模型调用。 |
| <a id="berdoz26a-inference"></a>[Alignment-Aware Decoding](https://proceedings.mlr.press/v306/berdoz26a.html) | 偏好对齐解码 | 先按 DPO 模型概率排除过低概率 token，再用 DPO 相对 SFT 的逐 token 对数概率差选下一个 token，把隐式偏好用于推理。 |
| <a id="bhatnagar26a-inference"></a>[STAR-KV: Low-Rank KV Cache Compression via Soft Thresholding for Adaptive Rank Control](https://proceedings.mlr.press/v306/bhatnagar26a.html) | KV 缓存压缩 | 用可微软阈值按层和头选秩，根据 Key 与 Value 的敏感性采用不同低秩分解，再在压缩后的缓存上选量化精度。 |
| <a id="bilal26a-inference"></a>[What If We Allocate Test-Time Compute Adaptively?](https://proceedings.mlr.press/v306/bilal26a.html) | 推理预算分配 | 让过程奖励模型既在生成中指导剪枝和扩展，也在轮次间为完整轨迹打分，把计算集中到更有希望的解题路径上。 |
| <a id="bose26a-inference"></a>[Cold-Start Personalization via Bayesian Adaptive Questioning](https://proceedings.mlr.press/v306/bose26a.html) | 冷启动个性化 | 离线先建模人群中偏好的相关性，在线用少量问答做贝叶斯更新，据此选择下一次澄清，从而复用已知的人群结构。 |
| <a id="cai26i-inference"></a>[Mining Tensor/Neuron-Level Sparsity to Maximize Mixture-of-Experts Potential in Post-Training and Inference](https://proceedings.mlr.press/v306/cai26i.html) | MoE 稀疏推理 | 后训练时细分专家，推理时按阈值跳过低贡献的 token–专家计算。双阈值与部分专家重构可以进一步调节精度和速度。 |
| <a id="cao26d-inference"></a>[Search or Accelerate: Confidence-Switched Position Beam Search for Diffusion Language Models](https://proceedings.mlr.press/v306/cao26d.html) | 扩散语言模型解码 | 低置信度时，对多个解除掩码的顺序做短程束搜索；高置信度时一次并行提交多个位置，避免为容易的步骤一直支付搜索开销。 |
| <a id="cao26q-inference"></a>[OSNIP: Balancing the Privacy-Utility-Efficiency Trilemma in LLM Inference via Obfuscated Semantic Null Space](https://proceedings.mlr.press/v306/cao26q.html) | LLM 推理隐私 | 在客户端用密钥控制的随机映射改变输入嵌入，使其与原嵌入近似正交，同时尽量保持任务语义，以降低论文所测攻击的恢复率。 |
| <a id="cao26ac-inference"></a>[Models Under SCOPE: Scalable and Controllable Routing via Pre-hoc Reasoning](https://proceedings.mlr.press/v306/cao26ac.html) | 模型路由 | 检索候选模型在类似题目上的表现，分别预测它们的成功率和成本。用这两个预测即时换算路由决策，就能响应预算变化和模型扩充。 |
| <a id="cetin26a-inference"></a>[Sparser, Faster, Lighter Transformer Language Models](https://proceedings.mlr.press/v306/cetin26a.html) | 非结构化稀疏推理 | 在前馈层用 L1 正则学到高稀疏度，再通过专用稀疏打包和 CUDA 内核兑现吞吐与显存收益；硬件执行效率要与剪枝率一起测。 |
| <a id="cha26a-inference"></a>[KnapSpec: Self-Speculative Decoding via Adaptive Layer Selection as a Knapsack Problem](https://proceedings.mlr.press/v306/cha26a.html) | 自投机解码 | 把选哪些 Attention 和 MLP 层做草稿写成背包问题，权衡隐藏状态余弦相似度和随上下文长度变化的实测延迟。 |
| <a id="chang26d-inference"></a>[xKV: Cross-Layer KV-Cache Compression via Aligned Singular Vector Extraction](https://proceedings.mlr.press/v306/chang26d.html) | 跨层 KV 缓存压缩 | 相邻或成组层的 KV 缓存主奇异方向可以对齐，因此可联合分解成共享低秩子空间，并在解码时选择性重建。 |
| <a id="chen26ar-inference"></a>[AutoRPA: Efficient GUI Automation through LLM-Driven Code Synthesis from Interactions](https://proceedings.mlr.press/v306/chen26ar.html) | GUI 流程复用 | 把多条 ReAct 轨迹先转成可替换参数的过程，再综合成可执行的自动化函数。验证时保留 Agent 回退，遇到失败可补救并修订函数。 |
| <a id="chen26bs-inference"></a>[Selective Disclosure Watermarking for Large Language Models](https://proceedings.mlr.press/v306/chen26bs.html) | 分级披露文本水印 | 生成每个 token 时递归划分词表，按各分区的概率质量采样，逐层用独立密钥写入不同载荷。持公开层密钥的验证者可解码该层载荷，且在论文的随机密钥模型下，最终 token 的边缘分布保持不变。 |
| <a id="chen26bv-inference"></a>[DFlash: Block Diffusion for Flash Speculative Decoding](https://proceedings.mlr.press/v306/chen26bv.html) | 块扩散投机解码 | 把目标模型多个层的隐状态融合后注入草稿模型每层的 KV 投影，让轻量块扩散模型一次前向并行生成一组候选 token，再由目标模型统一验证。逐层注入在消融中随草稿模型加深带来更长的接受前缀。 |
| <a id="chen26cd-inference"></a>[ArborKV: Structure-Aware KV Cache Management for Scaling Tree-based LLM Reasoning](https://proceedings.mlr.press/v306/chen26cd.html) | 树搜索 KV 缓存管理 | 优先保留当前搜索路径的 KV，对非活跃分支按树结构分配缓存预算。淘汰时保留原始 token，回溯到该分支时再由预填充恢复所需 KV，减少缓存占用，并免去从未回访的分支的重算开销。 |
| <a id="chen26ci-inference"></a>[Beyond Confidence: Adaptive and Coherent Decoding for Diffusion Language Models](https://proceedings.mlr.press/v306/chen26ci.html) | 扩散语言模型解码 | 用滑动窗口保留近几步都处于低熵集合的掩码位置，汇总这些位置的历史预测分布，并依据稳定位置动态分配每步解码量，让依赖上下文的词元等到条件更充分时再生成。 |
| <a id="chen26cm-inference"></a>[MALICE: Memory-aware Loop Invariants Generation on Symbolic Execution Traces](https://proceedings.mlr.press/v306/chen26cm.html) | 堆内存循环不变量生成 | 把符号执行得到的堆状态轨迹交给语言模型，先按已遍历和待遍历等区域拆分内存并选择分离逻辑谓词，再用验证器反馈修订候选不变量。 |
| <a id="chen26cw-inference"></a>[RADAR: Defending RAG Dynamically against Retrieval Corruption](https://proceedings.mlr.press/v306/chen26cw.html) | 动态检索抗投毒 | 把 RAG 候选文档的取舍写成图上的二元能量最小化，用最大流最小割求解。对历史证据只递推贝叶斯置信状态，使系统能够在抵御短期污染的同时适应知识变化。 |
| <a id="chen26dt-inference"></a>[SMILE: Extended Deep Submodular Function-Based Instruction and In-context Learning Demonstration Selection](https://proceedings.mlr.press/v306/chen26dt.html) | 指令与上下文示例联合选择 | 从语言模型反馈学习依赖指令和查询的次模代理，同时给示例覆盖度、查询相关性和指令兼容性打分。推理时对每条候选指令贪心挑选示例，再比较整组提示的得分。 |
| <a id="chen26eo-inference"></a>[Do LLMs Signal When They’re Right? Evidence from Neuron Agreement](https://proceedings.mlr.press/v306/chen26eo.html) | 神经元一致性解码 | 对同一输入的多条采样轨迹，用激活神经元集合的 Jaccard 相似度找出与其他轨迹一致的候选。该内部信号可在答案尚未完成时用于筛选，也适用于输出形式各异的代码生成。 |
| <a id="chen26er-inference"></a>[Certain Head, Uncertain Tail: Expert-Sample for Test-Time Scaling in Fine-Grained MoE](https://proceedings.mlr.press/v306/chen26er.html) | 细粒度 MoE 专家采样 | 解码时固定门控排名靠前的专家，对剩余名额只在低置信候选中采样，再按原门控权重归一化。这样可以改变候选的推理路径，同时保留高置信专家的输出贡献。 |
| <a id="chen26et-inference"></a>[From Extraction to Deduction: Resolving Functional Misalignment in RAG via a Collaborative Critic-Reasoner Framework](https://proceedings.mlr.press/v306/chen26et.html) | 检索证据净化与推导 | 用同一个语言模型先过滤无关背景、再用掩码标出疑似错误的答案片段，保留其周围语境，随后由推理角色整合剩余线索作答，降低照抄检索结果中错误实体的机会。 |
| <a id="chen26fm-inference"></a>[NanoSpec: Accelerating Speculative Decoding using Minimalist In-Context Vocabularies](https://proceedings.mlr.press/v306/chen26fm.html) | 投机解码的动态草稿词表 | 把草稿与目标模型近几步的高概率 token 放进滑动窗口，去重后仅对这些词表行计算草稿 logits。用异步收集将活跃行排成稠密矩阵，降低大词表末层投影开销，同时保留目标模型的完整验证。 |

<a id="by-representation-learning"></a>

### 表征学习

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="akhauri26b-representation-learning"></a>[Regression Language Models for Code](https://proceedings.mlr.press/v306/akhauri26b.html) | 代码性能预测 | 冻结统一的语言编码器，直接从代码文本回归内存、内核延迟或模型架构性能等数值，可共享跨语言和任务的表征。 |
| <a id="chen26dr-representation-learning"></a>[Beyond External Monitors: Enhancing Transparency of Large Language Models for Easier Monitoring](https://proceedings.mlr.press/v306/chen26dr.html) | 面向监测的行为表征解耦 | 用对比损失拉近同类行为的中间层表征、分开异类行为，同时在保留集上约束隐状态距离和输出 KL 散度。这样可让简单探针更容易识别行为，同时限制通用能力的变化。 |

<a id="by-evaluation"></a>

### 评测与诊断

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="abramovich26a-evaluation"></a>[SPEED-Bench: A Unified and Diverse Benchmark for Speculative Decoding](https://proceedings.mlr.press/v306/abramovich26a.html) | 推理系统评测 | 投机解码要用真实输入跨并发量评测，最佳草稿长度会随 batch 大小变化。 |
| <a id="acevedo26a-evaluation"></a>[Differential syntactic and semantic encoding in LLMs](https://proceedings.mlr.press/v306/acevedo26a.html) | 表征分析 | 给句法相同或语义相同的句子分别求激活中心，再做减法消融定位对应信号。 |
| <a id="acharya26a-evaluation"></a>[CauSciBench: Can LLMs Automate Causal Inference in Real-World Scientific Research?](https://proceedings.mlr.press/v306/acharya26a.html) | 分阶段评测 | 评测因果推断 Agent 时，把方法选择和数值计算分开计分，能定位真实数据上的失误来源。 |
| <a id="africa26a-evaluation"></a>[Consistency Training Can Entrench Misalignment](https://proceedings.mlr.press/v306/africa26a.html) | 一致性训练 | 一致性自训练可能抑制奖励投机却加剧迎合，诊断时要检查生成一致性标签造成的训练分布变化。 |
| <a id="ai26e-evaluation"></a>[MemoryBench: A Benchmark for Memory and Continual Learning in LLM Systems](https://proceedings.mlr.press/v306/ai26e.html) | 持续记忆评测 | 把用户反馈模拟成依次到达的在线事件，检查系统能否在后续任务中吸收历史反馈。 |
| <a id="aka26a-evaluation"></a>[Evaluating Contextual Illegality: AI Compliance in Corporate Law Scenarios](https://proceedings.mlr.press/v306/aka26a.html) | Agent 合规评测 | 保持工具动作相同、改变决定其合规性的背景，配对测试系统能否看出情境差别，同时测量合法请求被拒绝的情况。 |
| <a id="akhtar26a-evaluation"></a>[When AI Benchmarks Plateau: A Systematic Study of Benchmark Saturation](https://proceedings.mlr.press/v306/akhtar26a.html) | 基准饱和 | 比较评测集老化时，专家筛题与延缓饱和有关，是否公开测试数据在该研究中未显示出同样的关系。 |
| <a id="alshaalan26a-evaluation"></a>[Detecting Fluent Optimization-Based Adversarial Prompts via Sequential Entropy Changes](https://proceedings.mlr.press/v306/alshaalan26a.html) | 提示攻击检测 | 以系统提示估计逐 token 熵基线，对用户 token 的标准化熵做单侧累积和检测，可定位流畅对抗后缀的起点。 |
| <a id="amit26a-evaluation"></a>[Evaluating LLM Uncertainty in Long-Form Generation Using Deterministic Ground Truth](https://proceedings.mlr.press/v306/amit26a.html) | 长文本不确定性评测 | 用具有确定答案的长文本任务逐单元核对置信度。模型能区分整行是否有错，也可能无法给原子级错误准确排序。 |
| <a id="ammanamanchi26a-evaluation"></a>[Faults in Our Formal Benchmarking: Dataset Defects and Evaluation Failures in Lean Theorem Proving](https://proceedings.mlr.press/v306/ammanamanchi26a.html) | 形式化证明评测 | 在 Lean 基准里同时审计形式化命题和评测器。机器验证通过的证明仍可能对应真空命题、漏写条件或被简化的原题。 |
| <a id="angell26a-evaluation"></a>[Estimating Tail Risks in Language Model Output Distributions](https://proceedings.mlr.press/v306/angell26a.html) | 模型输出尾部风险 | 针对固定提示，用更常生成目标罕见行为的辅助模型作重要性采样提议分布，再重加权估计原模型的发生概率。 |
| <a id="ao26a-evaluation"></a>[ORLoopBench: Solver-in-the-Loop Benchmarks for Self-Correction and Behavioral Rationality in Operations Research](https://proceedings.mlr.press/v306/ao26a.html) | 求解器反馈与 Agent RL | 每次修约束后让求解器重算不可约不可行子系统，再分别奖励恢复可行性、定位冲突和缩短修复路径。整段重写还需要检查是否保留原问题语义。 |
| <a id="aoyama26a-evaluation"></a>[Predicting the Emergence of Induction Heads in Language Model Pretraining](https://proceedings.mlr.press/v306/aoyama26a.html) | 归纳头形成 | 用 batch 大小和上下文长度预测归纳头出现的训练时刻，再用训练文本中二元词组的重复频率和可靠性解释何时能形成。 |
| <a id="arcuschin26a-evaluation"></a>[Biases in the Blind Spot: Detecting What LLMs Fail to Mention](https://proceedings.mlr.press/v306/arcuschin26a.html) | 隐性偏差审计 | 自动生成候选偏差后，构造只改变候选属性的输入对，用多重检验找出会改变决策、却未出现在模型理由里的因素。 |
| <a id="arcuschin26b-evaluation"></a>[Chain-of-Thought Reasoning In The Wild Is Not Always Faithful](https://proceedings.mlr.press/v306/arcuschin26b.html) | 推理忠实性 | 把自然比较题的两个对象交换，检查模型能否暴露互相矛盾的答案。两边同时附有流畅理由仍可能是事后合理化。 |
| <a id="arghal26a-evaluation"></a>[A Behavioural and Representational Evaluation of Goal-Directedness in Language Model Agents](https://proceedings.mlr.press/v306/arghal26a.html) | Agent 目标表征 | 把相对最优策略的导航表现和激活探针结合起来，可区分模型编码的粗略地图与推理后更偏向即时动作的表征。 |
| <a id="arike26a-evaluation"></a>[How does information access affect LLM monitors’ ability to detect sabotage?](https://proceedings.mlr.press/v306/arike26a.html) | Agent 执行监控 | 先由一个监控器从执行轨迹挑证据，再让另一个评分。较长轨迹尤其可能受益于裁掉无关细节。 |
| <a id="arora26c-evaluation"></a>[Language Model Circuits Are Sparse in the Neuron Basis](https://proceedings.mlr.press/v306/arora26c.html) | 语言模型电路 | 直接在 MLP 神经元基底上做梯度归因和因果干预，可定位控制语法或多跳推理中间步骤的稀疏电路。 |
| <a id="back26a-evaluation"></a>[Understanding LoRA as Knowledge Memory: An Empirical Analysis](https://proceedings.mlr.press/v306/back26a.html) | LoRA 知识记忆 | 同时合并多个知识 LoRA 时会出现参数干扰，甚至相关模块混合过多也会掉点。在论文测试中加入外部检索或上下文能补回部分损失。 |
| <a id="badshah26a-evaluation"></a>[SCOPE: Selective Conformal Optimized Pairwise LLM Judging](https://proceedings.mlr.press/v306/badshah26a.html) | LLM 裁判校准 | 交换待比较回答的位置各询问一次，将平均偏好概率转为熵，再用共形阈值拒判，可在可交换性假设下控制已接受判断的错误率。 |
| <a id="baek26d-evaluation"></a>[Sycophancy Towards Researchers Drives Performative Misalignment](https://proceedings.mlr.press/v306/baek26d.html) | 对齐行为诊断 | 提高模型迎合倾向也会增强它对评测提示的敏感性，说明行为差异可能来自迎合。比较欺骗和迎合机制时，应控制这种因素。 |
| <a id="bair26a-evaluation"></a>[Compressed Sensing for Capability Localization in Large Language Models](https://proceedings.mlr.press/v306/bair26a.html) | 机制可解释性 | 利用功能相关注意力头的稀疏性，用压缩感知设计成组敲除实验，少量评估即可识别一组对数学或代码能力必要的注意力头。 |
| <a id="baksys26a-evaluation"></a>[miniF2F-Dafny: LLM-Guided Mathematical Theorem Proving via Auto-Active Verification](https://proceedings.mlr.press/v306/baksys26a.html) | 形式化证明评测 | 用 Dafny 将高层证明提示交给 SMT 自动补细节。部分题目空证明就能过，因此评估 LLM 增益时要扣除验证器自动化的基线。 |
| <a id="balasubramanian26a-evaluation"></a>[Dependence-Aware Label Aggregation for LLM-as-a-Judge via Ising Models](https://proceedings.mlr.press/v306/balasubramanian26a.html) | 相关裁判聚合 | 用 Ising 耦合显式建模裁判票之间的依赖。当依赖强度随真值类别变化，最优判决一般还需要票与票的乘积项。 |
| <a id="bali26a-evaluation"></a>[Quantifying LLM Attention-Head Stability: Implications for Circuit Universality](https://proceedings.mlr.press/v306/bali26a.html) | 注意力电路稳定性 | 独立训练同架构模型后逐层对齐注意力头，发现中间层头尤其易随初始化变化。权重衰减可提高头的跨训练稳定性。 |
| <a id="ball26a-evaluation"></a>[Reading Between the Tokens: Improving Preference Predictions through Mechanistic Forecasting](https://proceedings.mlr.press/v306/ball26a.html) | 偏好预测 | 在选举预测案例中，可读取语言模型中编码党派倾向的激活来预测选择。这些内部信号有时比直接询问模型得到的答案更准确。 |
| <a id="bao26e-evaluation"></a>[DRIFT-BENCH: Diagnosing CoopeRative Breakdowns in LLM Agents under Input Faults via Multi-Turn Interaction](https://proceedings.mlr.press/v306/bao26e.html) | Agent 澄清评测 | 注入缺参数、错误前提或模糊指代，再让代理与不同用户角色多轮对话并执行，可直接测量澄清是否修复了操作结果。 |
| <a id="barbero26a-evaluation"></a>[Extracting alignment data in open models](https://proceedings.mlr.press/v306/barbero26a.html) | 训练数据记忆评测 | 用语义嵌入匹配查找后训练数据复现，可识别格式差异掩盖的泄漏。只做字符串匹配在文中会显著低估复现量。 |
| <a id="barres26a-evaluation"></a>[$τ^2$-Bench: Evaluating Conversational Agents in a Dual-Control Environment](https://proceedings.mlr.press/v306/barres26a.html) | 人机协作 Agent 评测 | 让用户模拟器与 Agent 都能用工具修改同一环境，结合单方控制消融，把规划错误与沟通协调错误分开测量。 |
| <a id="batzoglou26a-evaluation"></a>[INDUCTION: Finite-Structure Concept Synthesis in First-Order Logic](https://proceedings.mlr.press/v306/batzoglou26a.html) | 逻辑归纳评测 | 用有限结构和 SMT 验证一阶规则，并同时测规则长度与未见世界的泛化。较短的规则更能区分学到概念和记住例子。 |
| <a id="berdoz26b-evaluation"></a>[Reasoning Structure of Large Language Models](https://proceedings.mlr.press/v306/berdoz26b.html) | 推理过程评测 | 把推理轨迹转成可核验的主张依赖图，用逻辑流的集中度衡量效率，可区分答案正确率和 token 数相同的推理过程。 |
| <a id="bernas26a-evaluation"></a>[Revisiting Anisotropy in Language Transformers: The Geometry of Learning Dynamics](https://proceedings.mlr.press/v306/bernas26a.html) | 语言表征几何 | 用训练中的多个检查点追踪嵌入各向异性与流形上的熵，区分训练过程产生的几何变化和最终模型的静态特征。 |
| <a id="bhardwaj26a-evaluation"></a>[Embedding Trust: Semantic Isotropy Predicts Nonfactuality in Long-Form Text Generation](https://proceedings.mlr.press/v306/bhardwaj26a.html) | 长文本事实性诊断 | 给同一提示采样多个回答，用归一化文本嵌入的角度离散程度衡量语义一致性。更分散的回答在论文评测中更少保持事实一致。 |
| <a id="bi26e-evaluation"></a>[The Geometry of Reasoning: Self-Evaluation via Layerwise Trajectory Evolution](https://proceedings.mlr.press/v306/bi26e.html) | 推理自评 | 跟踪隐藏表征逐层移动及转向来衡量推理进展，再按题目本身的难度校准，用于白盒判断推理是否可靠。 |
| <a id="binkowski26a-evaluation"></a>[Attention Sinks as Internal Signals for Hallucination Detection in Large Language Models](https://proceedings.mlr.press/v306/binkowski26a.html) | 幻觉检测 | 生成时可用注意力汇聚到少数 token 的程度做幻觉检测。实验中，探针尤其依赖那些 Value 向量范数大的注意力汇聚点。 |
| <a id="bohacek26a-evaluation"></a>[Uncovering Competency Gaps in Large Language Models and Their Benchmarks](https://proceedings.mlr.press/v306/bohacek26a.html) | 基准概念覆盖 | 用稀疏自编码器激活给测试题做概念级分解，分别查找模型表现差的概念与基准本身覆盖不足的概念。 |
| <a id="boppana26a-evaluation"></a>[Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought](https://proceedings.mlr.press/v306/boppana26a.html) | 推理忠实性 | 对比隐藏激活探针、强制提前作答与思维链监控，可测到答案在内部已经可解码但尚未说出的阶段。用探针提前结束可节省生成。 |
| <a id="bridgeford26a-evaluation"></a>[Detecting Perspective Shifts in Multi-Agent Systems](https://proceedings.mlr.press/v306/bridgeford26a.html) | 多 Agent 行为监控 | 把不同时间的 Agent 响应对齐到同一嵌入空间，再在单个或群体层面做假设检验，可监测黑盒策略的行为变化。 |
| <a id="calderon26a-evaluation"></a>[Empty Shelves or Lost Keys? Recall Is the Bottleneck for Parametric Factuality](https://proceedings.mlr.press/v306/calderon26a.html) | 事实召回评测 | 对同一个事实收集多种问法和推理预算下的回答，区分完全没有召回证据的事实与只能在某些设定下召回的事实。 |
| <a id="cao26z-evaluation"></a>[DynaSchedBench: Calibrated Dynamic Scheduling Benchmarks and Observability Paradox in LLM-based Scheduling Agents](https://proceedings.mlr.press/v306/cao26z.html) | 动态调度评测 | 用事件序列生成和压力指数控制任务难度，再比较同一场景下的简明观测与全量观测。更多状态信息在试验中有时反而降低 LLM 调度质量。 |
| <a id="carlsson26a-evaluation"></a>[SEDRAS: Symbolically Evaluated Deep Research And Science](https://proceedings.mlr.press/v306/carlsson26a.html) | 科学发现 Agent 评测 | 让模型从可控生成的数据归纳自然语言理论，再在另一会话把理论转成代码，与真实生成过程比较。这个流程可以独立评估主动探索与理论归纳。 |
| <a id="casanova26a-evaluation"></a>[On the Limits of LLM Adaptability: Impact of Model-Internalized Priors on Annotation Task Performance](https://proceedings.mlr.press/v306/casanova26a.html) | LLM 标注评测 | 衡量模型内化概念与实际任务定义的吻合度，可帮助预测标注表现；替换定义可能系统改变分类，同时保持高置信度。 |
| <a id="chang26e-evaluation"></a>[How2Everything: Mining the Web for How-to Procedures to Evaluate and Improve LLMs](https://proceedings.mlr.press/v306/chang26e.html) | 操作步骤评测 | 评测操作指南时，专门检测会导致目标不可达的关键步骤错误。将这种判分蒸馏给小裁判后，也可以作为强化学习奖励。 |
| <a id="chanin26a-evaluation"></a>[Sparse but Wrong: Incorrect L0 Leads to Incorrect Features in Sparse Autoencoders](https://proceedings.mlr.press/v306/chanin26a.html) | 稀疏自编码器可解释性 | 每个 token 激活的特征数过少会合并相关特征，过多也可能产生混合特征。选择超参时可加上稀疏探测或特征分离诊断，重建误差本身不够。 |
| <a id="chauvin26a-evaluation"></a>[Token-Efficient Change Detection in LLM APIs](https://proceedings.mlr.press/v306/chauvin26a.html) | LLM API 变化检测 | 选择多个候选 token 位于决策边界附近的输入作为探针，只用返回 token 就能检测服务更新，无需权重或 logprob。 |
| <a id="chen26l-evaluation"></a>[CausalGame: Benchmarking Causal Thinking of LLM Agents in Games](https://proceedings.mlr.press/v306/chen26l.html) | Agent 因果推断评测 | 让 Agent 自己设计实验并收集观测，同时在游戏中控制隐藏混杂、选择偏差和测量噪声，可区分会描述因果概念与能主动识别因果关系。 |
| <a id="chen26n-evaluation"></a>[Mind the Gap: Catching Hallucinations via Evidence Drop on the Reasoning Manifold](https://proceedings.mlr.press/v306/chen26n.html) | 幻觉逐步定位 | 把推理过程的局部证据支持写成序列，用其中最大的突然下跌判断风险并定位错误步骤，可以保留整段不确定性平均会冲淡的信号。 |
| <a id="chen26o-evaluation"></a>[OPT-Engine: Benchmarking the Limits of LLMs in Optimization Modeling via Complexity Scaling](https://proceedings.mlr.press/v306/chen26o.html) | 优化建模 Agent 评测 | 在同一问题族中逐步从线性规划扩展到混合整数约束，分别测试算术、全局约束和求解器建模。实测工具能补局部算术，约束表达仍独立限制解的质量。 |
| <a id="chen26q-evaluation"></a>[L-CUBE: Isolating Long-Context Capacity from Knowledge with Controllable Mutual Information Scaling](https://proceedings.mlr.press/v306/chen26q.html) | 长上下文容量评测 | 用可控跨段互信息的层级高斯序列生成测试数据，直接比较模型和真实条件分布的 KL，以衡量上下文拉长后实际提取了多少信息。 |
| <a id="chen26x-evaluation"></a>[Adaptive Probe-based Steering for Robust LLM Jailbreaking](https://proceedings.mlr.press/v306/chen26x.html) | 激活干预下的安全评测 | 固定强度下的激活干预测试可能低估安全脆弱性。论文用自适应强度做压力测试，说明评测应报告模型对干预强度变化的敏感性。 |
| <a id="chen26aq-evaluation"></a>[The Unlearnability Phenomenon in RLVR for Language Models](https://proceedings.mlr.press/v306/chen26aq.html) | RLVR 的难学样本 | 有正确 rollout 的难题也可能长期学不会。论文中这类题与其他样本的梯度相似度偏低，因此可以用跨样本梯度诊断来区分探索不足与表征难以共享。 |
| <a id="chen26bb-evaluation"></a>[All Circuits Lead to Rome: Rethinking Functional Anisotropy in Circuit and Sheaf Discovery for LLMs](https://proceedings.mlr.press/v306/chen26bb.html) | 机制电路的非唯一性 | 在电路发现目标中加入对此前已选边的激活惩罚，并保留原有的稀疏性、保真度和完整性目标。在 GPT-2 的间接宾语识别任务中，所得两组子网络都完成了任务，边集交并比仅为 4.1%。 |
| <a id="chen26bg-evaluation"></a>[Discovering Implicit Large Language Model Alignment Objectives](https://proceedings.mlr.press/v306/chen26bg.html) | 对齐奖励的隐含目标诊断 | 在多个训练检查点记录同一输入的回答，找出当前目标组合解释残差最大的样本。用这些回答轨迹提出新的自然语言目标，每轮选取最能降低残差的一项，逐步拆解奖励。 |
| <a id="chen26bz-evaluation"></a>[HypoSpace: A Diagnostic Benchmark for Set-Valued Hypothesis Generation under Underdetermination and Sublinear Coverage Bounds](https://proceedings.mlr.press/v306/chen26bz.html) | 欠定问题的假设覆盖 | 对可穷举解集的任务，同时统计有效提案占比、去重后的提案占比以及不同有效提案对完整解集的覆盖率。随着可行假设空间扩张，模型即使仍常给出有效解，也可能反复生成同一小部分假设。 |
| <a id="chen26cf-evaluation"></a>[InteractScience: Programmatic and Visually-Grounded Evaluation of Interactive Scientific Demonstration Code Generation](https://proceedings.mlr.press/v306/chen26cf.html) | 交互式科学代码评测 | 对生成的科学演示执行模拟点击等操作，用 DOM 断言核对事件和状态更新，再把同一交互状态的截图与参考图及检查清单对照，捕捉功能断言通过后仍可能存在的科学现象呈现错误。 |
| <a id="chen26cv-evaluation"></a>[Mechanistic Data Attribution: Tracing the Training Origins of Interpretable LLM Units](https://proceedings.mlr.press/v306/chen26cv.html) | 可解释注意力头的训练数据归因 | 用影响函数按训练样本对目标注意力头的作用排序，再对高分样本做剔除或增广以检验归因。在 Pythia 实验中，针对归纳头的干预也改变了上下文学习表现。 |
| <a id="chen26da-evaluation"></a>[How can we assess human-agent interactions? Case studies in software agent design](https://proceedings.mlr.press/v306/chen26da.html) | 人机协作智能体评测 | 用交互日志预测用户满意度，再用实际反馈校正伪标签估计来比较智能体设计。在 OpenHands 的实地评测中，该做法比常规 A/B 分析得到更窄的置信区间。 |
| <a id="chen26di-evaluation"></a>[Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens](https://proceedings.mlr.press/v306/chen26di.html) | 用逐层预测变化衡量推理投入 | 用深层预测分布相对最终层的 Jensen–Shannon 散度识别推理中发生显著预测修订的 token。其占比在所测推理模型上与准确率正相关，也可在短前缀阶段用于提前淘汰低分候选。 |
| <a id="chen26dp-evaluation"></a>[Scam2Prompt: A Scalable Framework for Auditing Malicious Scam Endpoints in Production LLMs](https://proceedings.mlr.press/v306/chen26dp.html) | 代码生成的诈骗链接审计 | 从已知诈骗页面提取可见文本，据此合成表面正常的开发需求。对生成代码提取 URL 并交由多个安全检测器核验，可测量模型在日常编程请求中输出恶意链接的频率。 |
| <a id="chen26eg-evaluation"></a>[AppWorld-UL: Benchmarking Diverse Agent-User Interactions for Tool-Use](https://proceedings.mlr.press/v306/chen26eg.html) | 工具智能体的用户交互评测 | 从可自动执行的有状态任务构造指令欠定、目标不可行和操作待确认的变体，并可在同一任务叠加多种情形。模拟用户只依照预设知识边界回答，评测同时检查应用状态与所需交互。 |
| <a id="chen26fa-evaluation"></a>[INT vs. FP: A Comprehensive Study of Fine-Grained Low-bit Quantization Formats](https://proceedings.mlr.press/v306/chen26fa.html) | 分块低比特量化格式比较 | 比较整数与浮点量化时，应同时看块大小和块内峰值相对均方根的比例。论文的细粒度实验中，缩小分块使异常值影响局部化，因而同位宽整数格式可在低峰值比的块上获得更高的量化信噪比。 |

<a id="by-theory-statistics"></a>

### 理论与统计

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="azizian26a-theory-statistics"></a>[How Does the Pretraining Distribution Shape In-Context Learning? A Fundamental Trade-Off](https://proceedings.mlr.press/v306/azizian26a.html) | 上下文学习与数据分布 | 预训练任务分布的重尾有利于偏移下选中合适任务，但论文框架也显示它会损害泛化，尤其在只有少量上下文示例时。 |
| <a id="bakman26a-theory-statistics"></a>[Hair-Trigger Alignment: Black-Box Evaluation Cannot Guarantee Post-Update Alignment](https://proceedings.mlr.press/v306/bakman26a.html) | 模型更新后对齐 | 同样通过静态黑盒测试的模型，可能在一次良性梯度更新后呈现截然不同的行为。更新后的鲁棒性需要直接在更新场景中测量。 |
| <a id="bigelow26a-theory-statistics"></a>[Belief Dynamics Reveal the Dual Nature of In-Context Learning and Activation Steering](https://proceedings.mlr.press/v306/bigelow26a.html) | 上下文与激活干预 | 把激活引导看成改变潜在概念先验，把上下文示例看成增加证据。两者的效应可在对数信念空间相加，用来预测组合后的行为变化。 |
| <a id="blondel26a-theory-statistics"></a>[Autoregressive Language Models are Secretly Energy-Based Models: Insights into the Lookahead Capabilities of Next-Token Prediction](https://proceedings.mlr.press/v306/blondel26a.html) | 自回归与能量模型 | 用概率链式分解可将序列能量模型和自回归模型在函数空间一一对应。下一 token 的归一化隐含对未来续写的边际化，其形式等同一个软 Bellman 递推。 |
| <a id="cagnetta26a-theory-statistics"></a>[Deriving Neural Scaling Laws from the Statistics of Natural Language](https://proceedings.mlr.press/v306/cagnetta26a.html) | 语言数据缩放律 | 用 token 两两相关性随间距的衰减和条件熵随上下文的衰减，预测数据受限时的缩放指数，并与 TinyStories 和 WikiText 上的曲线核对。 |
| <a id="cai26p-theory-statistics"></a>[Asymptotic Universal Alignment: A New Alignment Framework via Test-Time Scaling](https://proceedings.mlr.press/v306/cai26p.html) | 多候选偏好对齐 | 当用户从 k 个候选中选择时，训练对称多方偏好博弈可保留输出多样性，并在理论设定中达到 k/(k+1) 的最优偏好胜率界。 |
| <a id="chen26ae-theory-statistics"></a>[Chain-of-Thought Gradient Descent](https://proceedings.mlr.press/v306/chen26ae.html) | 思维链内模拟梯度下降 | 把生成序列当作可以扩展的中间工作空间，使固定深度的 Transformer 能模拟多步上下文梯度下降；按更新步骤动态遮罩可避免重复扫过无关 token。 |
| <a id="chen26cs-theory-statistics"></a>[Towards Theoretical Understanding of Transformer Test-Time Computing: Investigation on In-Context Linear Regression](https://proceedings.mlr.press/v306/chen26cs.html) | 测试时采样与上下文回归 | 在只有一条无噪声上下文样本和一个非零系数的稀疏线性回归模型里，分析表明，延长随机解码并对采样路径做多数投票，可提高恢复真实系数的概率，缓解贪心解码受限于单一路径的问题。 |
<!-- classification:end -->
