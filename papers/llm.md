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

<a id="by-modules"></a>

### 模块

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="bonnet26a-modules"></a>[Learning to Remember, Learn, and Forget in Attention-Based Models](https://proceedings.mlr.press/v306/bonnet26a.html) | 线性注意力记忆 | 为每个注意力状态维护重要性，用它调节状态可塑性，使固定容量记忆根据此前积累的知识决定可更新程度。 |
| <a id="byun26a-modules"></a>[Bounded Hyperbolic Tangent: A Stable and Efficient Alternative to Pre-Layer Normalization in Large Language Models](https://proceedings.mlr.press/v306/byun26a.html) | 归一化替换 | 把 tanh 输入约束在非饱和区间来控制深层激活增长，每个块只计算一次精确统计量，另一处用轻量的方差估计替代。 |

<a id="by-loss-functions"></a>

### 损失函数

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="abas26a-loss-functions"></a>[TUR-DPO: Topology- and Uncertainty-Aware Direct Preference Optimization](https://proceedings.mlr.press/v306/abas26a.html) | 偏好学习 | 把回答抽成主张及其依赖图，用推理结构质量和不确定性加权偏好训练。 |
| <a id="aouad26a-loss-functions"></a>[The Sign Estimator: Preference Modeling for LLM Alignment under Heterogeneity](https://proceedings.mlr.press/v306/aouad26a.html) | 异质偏好学习 | 把成对偏好的交叉熵改成二分类式损失，在论文的假设下，学到的排序与总体平均效用一致。 |

<a id="by-optimization"></a>

### 优化

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="abbasi26a-optimization"></a>[Zero Sum SVD: Balancing Loss Sensitivity for Low Rank LLM Compression](https://proceedings.mlr.press/v306/abbasi26a.html) | 模型压缩 | 在全模型固定参数预算下，用校准损失的一阶估计决定跨层删哪些奇异成分。 |
| <a id="cai26a-optimization"></a>[AdaMeZO: Adam-style Zeroth-Order Optimizer for LLM Fine-tuning Without Maintaining the Moments](https://proceedings.mlr.press/v306/cai26a.html) | 低显存零阶微调 | 在只需前向计算的零阶微调中引入 Adam 式一阶和二阶矩估计，同时省去持久化矩状态，以少量显存获得更快收敛。 |

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

<a id="by-representation-learning"></a>

### 表征学习

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="akhauri26b-representation-learning"></a>[Regression Language Models for Code](https://proceedings.mlr.press/v306/akhauri26b.html) | 代码性能预测 | 冻结统一的语言编码器，直接从代码文本回归内存、内核延迟或模型架构性能等数值，可共享跨语言和任务的表征。 |

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
<!-- classification:end -->
