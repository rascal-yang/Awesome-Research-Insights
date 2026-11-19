# NeurIPS 2026 论文索引 · 第 5 卷

[会议首页](README.md)

| 领域 | 技术类型 | 论文卡 | 能改变的技术选择 |
| --- | --- | --- | --- |
| 统计学习 | 结构约束 | [Embedding Foundation Model Predictions in Discrete-Choice Models with Structural Guarantees](cards-0005.md#paper-153155) | 冻结受约束选择模型的结构系数，再利用基础模型提高精度。 |
| 自然语言处理 | 偏好表征 | [Embeddings for Preferences, Not Semantics](cards-0005.md#paper-155251) | 训练偏好编码器时解除立场与措辞的相关性。 |
| 计算机视觉 | 自监督对齐 | [Emergence of a Shared Canonical Object Frame from In-the-Wild Videos](cards-0005.md#paper-149226) | 用共享粗网格作为跨实例的姿态对齐瓶颈。 |
| 生成模型 | 采样理论 | [Emergence of Distortions in High-Dimensional Guided Diffusion Models](cards-0005.md#paper-152320) | 通过引导时间表同时监测条件分离和方差损失。 |
| 强化学习 | 内在奖励 | [Emergence of Physical Intelligence via Controllable Information Production](cards-0005.md#paper-152582) | 按系统可控信息的产生速率选探索目标。 |
| 优化 | 预条件 | [Emergence, Retention and Mitigation of Ill-conditioning due to Basis Lifting in KANs](cards-0005.md#paper-150542) | 检查基函数提升后 Gram 矩阵，再决定是否学习坐标变换。 |
| 学习理论 | 低秩训练 | [Emergent Low-Rank Training Dynamics in MLPs with Smooth Activations](cards-0005.md#paper-151342) | 按训练不变子空间初始化低秩网络 |
| 模型安全 | 防御评测 | [Emergent Misalignment as Data-Mediated Transfer](cards-0005.md#paper-150105) | 区分训练分布和训练渠道做安全回归 |
| 自然语言处理 | 语义探针 | [Emergent Semantic Role Understanding in Language Models](cards-0005.md#paper-152210) | 先查冻结骨干是否已编码语义角色，再决定是否微调 |
| 多模态学习 | 因果表征 | [Emergent Visual Thinking in Text-Only Reasoning through Multimodal Training](cards-0005.md#paper-153218) | 用干预区分可解码的视觉信息与推理实际使用的信息 |
| 神经符号学习 | 概率推断 | [EM-NeSy: Expectation Maximization for Neurosymbolic Learning](cards-0005.md#paper-149935) | 符号推理不可微时以隐变量后验训练神经前端 |
| 大语言模型 | 专家路由 | [EMO: Pretraining Mixture of Experts for Emergent Modularity](cards-0005.md#paper-151720) | 预训练用文档边界约束专家池，便于部署裁剪 |
| 计算机视觉 | 神经表征评测 | [Emotion-Trained Vision Models Do Not Necessarily Learn EEG-Aligned Facial Dynamics](cards-0005.md#paper-150276) | 以同架构随机权重作为脑对齐基线 |
| 统计学习 | 经验贝叶斯 | [Empirical Bayes Rebiasing](cards-0005.md#paper-152794) | 偏差估计很噪时学习部分校正以缩短区间 |
| 大语言模型 | 偏好评测 | [Empirical regularities in subjective decision-making by LLMs](cards-0005.md#paper-150340) | 把候选生成偏好与筛选偏好分开测试 |
| 大语言模型 | 扩散训练 | [Empowering Masked Diffusion Models to Self-Correct with Leave-One-Out Transformers](cards-0005.md#paper-150367) | 对未遮盖位置也施加留一预测监督 |
| 大语言模型 | 扩散采样 | [Enabling approximate joint sampling in diffusion LMs](cards-0005.md#paper-149410) | 用轻量条件采样头代替多 token 并行独立解遮盖 |
| 具身智能 | 候选重排 | [Enabling VLA Action Self-Verification via VLM Token Probability Bucketing](cards-0005.md#paper-155216) | 复用策略骨干验证候选动作 |
| 计算机视觉 | 结构化生成 | [ENACT: Single-Image Human-Scene Interaction Motion from Language via Foundation-Model Orchestration](cards-0005.md#paper-150626) | 用带接触约束的关键帧连接图像理解与动作生成 |
| 具身智能 | 预测监督 | [Endowing Your Vision-Language-Action Model with a Predictive Mind](cards-0005.md#paper-155390) | 直接在策略实际读取的中间特征上加未来监督 |
| 优化 / 生成模型 | 条件优化 | [End-to-End Differentiable Diffusion Conditioning for Physics-Informed Optimization](cards-0005.md#paper-153367) | 对冻结生成器的条件变量进行测试时优化 |
| 统计学习 | 切换动力学 | [End-to-End Identifiable and Consistent Recurrent Switching Dynamical Systems](cards-0005.md#paper-148468) | 在需要潜在状态可辨识时比较精确似然和变分估计 |
| 生成模型 | 联合训练 | [End-to-End Training for Unified Tokenization and Latent Denoising](cards-0005.md#paper-155881) | 让分词器和去噪器共享编码权重 |
| 组合优化 | 精确推断 | [EnerGNN: Learning Optimization-Compatible Energy Functions for Exact Constrained Combinatorial Inference](cards-0005.md#paper-148678) | 学习适合混合整数求解的能量，部署时直接加硬约束 |
| 科学机器学习 | 能量算子 | [Energy-Based Operator Learning in Function Space](cards-0005.md#paper-153867) | 用条件能量同时支持多解预测及无监督异常评分 |
| 科学机器学习 | 物理约束 | [Energy-Guided Transport for Projection-Free Physics-Informed Flow Matching](cards-0005.md#paper-154978) | 用连续能量引导替代去噪过程中的离散强投影 |
| 联邦学习 | 能耗优化 | [Energy Is All We Need: Beyond FLOPs in Model-Heterogeneous Federated Learning](cards-0005.md#paper-151795) | 按每焦耳的原型对齐改善分配本地训练轮次 |
| 大语言模型 | 零阶优化 | [ENGINE: Endogenous Variational MultiScale Optimization for Zeroth-Order LLM Fine-Tuning](cards-0005.md#paper-151095) | 交替用高维探针修正低维零阶微调 |
| Agent | 状态复用 | [EngramState: Loadable Tool Priors for Efficient Function Calling](cards-0005.md#paper-150845) | 把工具说明预编码为可加载的循环状态 |
| 软件工程 / Agent | 代码定位 | [Enhancing Agentic Code Localization with Traceability Recovered from Repository Evolution](cards-0005.md#paper-152178) | 检索维护历史恢复问题描述与实现的对应 |
| 语音多模态 | 行为对齐 | [Enhancing Speech Large Language Models through Reinforced Behavior Alignment](cards-0005.md#paper-154532) | 在等义异声输入下直接优化行为一致性 |
| 统计学习 | 拒答校准 | [Ensemble Selective Classification](cards-0005.md#paper-152721) | 用部署标注组合多个置信度分数 |
| 大语言模型 | 集成解码 | [Ensembling Language Models with Sequential Monte Carlo](cards-0005.md#paper-148212) | 在共享字符空间集成不同词表模型 |
| 控制 | 安全验证 | [Ensuring Deployment-Time Safety of Neural Network Controlled Systems via Localized Certificate Repair](cards-0005.md#paper-150792) | 环境改变后优先修复局部安全证书 |
| 大语言模型 | 推理缓存 | [EntropyCache: Decoded Token Entropy Guided KV Caching for Diffusion Language Models](cards-0005.md#paper-152767) | 依据新解码 token 熵决定刷新缓存 |
| 大语言模型 | 幻觉检测 | [Entropy Distribution as a Fingerprint for Hallucinations in Generative Models](cards-0005.md#paper-148328) | 用校准的熵尾部补充均值 |
| Agent | 训练诊断 | [Entropy Dynamics of Agent Reinforcement Learning](cards-0005.md#paper-149956) | 多轮强化学习监控循环熵暴涨和退化积累 |
| 大语言模型 | 推理解码 | [Entropy-Gated Latent Recursion](cards-0005.md#paper-152175) | 把递归层跨度作为随机温度外的候选维度 |
| 多模态学习 | 测试时适配 | [Entropy Minimization without Model Collapse: Mitigating Prediction Bias in Medical Imaging](cards-0005.md#paper-149828) | 按预测类平衡熵损失 |
| 强化学习 | 策略优化 | [Entropy Polarity in Reinforcement Fine-Tuning:  Direction, Asymmetry, and Control](cards-0005.md#paper-152571) | 按 token 熵极性重加权优势 |
| 统计学习 | 跨环境建模 | [Environment-Robust Representation Learning with Empirical Bayes](cards-0005.md#paper-151010) | 用层级先验平衡环境潜变量 |
| 科学机器学习 | 概率预报 | [EO-WM: A Physically Informed World Model for Probabilistic Earth Observation Forecasting](cards-0005.md#paper-153039) | 分开输入气候基线、异常及累计应力 |
| 多模态学习 | 生成推理 | [EPIC: Efficient Predicate-Guided Inference-Time Control for Compositional Text-to-Image Generation](cards-0005.md#paper-152068) | 按失败谓词选择局部编辑或重采样 |
| 具身智能 | 不确定性规划 | [EpicWorldModel: Exploration-driven Planning with Latent World Models](cards-0005.md#paper-150907) | 用随机潜状态预测引导探索 |
| 优化 | 求解器控制 | [EpiPivot: Learning to Control the Simplex Method under Epistemic Uncertainty](cards-0005.md#paper-153200) | 用不确定性预测选择单纯形枢轴规则 |
| 机器学习 | 数据选择 | [Epiplexity Guided Data Selection and Generation for Out-of-Distribution Generalization](cards-0005.md#paper-153698) | 按可学习结构增益动态调整域采样 |
| Agent | 交互学习 | [Epistemic Social Learning: Latent Behavioral Structure under Endogenous Multi-Agent Interaction](cards-0005.md#paper-150541) | 分开快速推断与慢速更新行为原型 |
| 多模态学习 | 流式记忆 | [EpiStream: Utility-Aware Temporal Abstraction for Dense-Action Streams](cards-0005.md#paper-153023) | 按下游效用决定何时提交视频片段 |
| 生成模型 | 采样优化 | [Equilibrium Forcing: Adaptive Video Generation Without Noise Conditioning](cards-0005.md#paper-149913) | 训练去噪场后按数据自适应步长 |
| 生成模型 | 能量模型 | [Equilibrium Matching: Generative Modeling with Implicit Energy-Based Models](cards-0005.md#paper-148529) | 用可优化能量场支持自适应采样 |
| 机器人学 | 覆盖规划 | [Ergodic Trajectory Design by Learned Pushforward Maps: Provable Coverage via Conditional Flow Matching](cards-0005.md#paper-148507) | 分离规则域中的遍历轨迹与目标覆盖密度 |
| 大语言模型 / 医疗 | 评测 | [ER-Reason: A Benchmark Dataset for LLM Clinical Reasoning in the Emergency Room](cards-0005.md#paper-138971) | 在逐步补充证据时以专家分布验证信念更新 |
| 强化学习 | 价值校准 | [Error-Guided Bellman Calibration for Semi-Offline Value Estimation](cards-0005.md#paper-149993) | 用少量在策略样本学习偏差轴再做价值校准 |
| 多模态学习 | 注意力编辑 | [eSAM: Editing SAM3 Attention for Training-Free Referring Segmentation](cards-0005.md#paper-153788) | 抑制注意力汇点后显式引导注意力重分配 |
| 学习理论 | 泛化认证 | [Escaping Parameter Space: Tight Generalization Bounds via Representation Quality](cards-0005.md#paper-154899) | 用表示的局部类结构、解码一致性和稳定性诊断泛化 |
| 强化学习 | 离线规划 | [Escaping Path Mirages in Offline Goal-Conditioned Reinforcement Learning](cards-0005.md#paper-151359) | 把高随机分叉设为子目标并分段评估路径 |
| 大语言模型 | 推理搜索 | [Escaping Reasoning Basins: Basin-Aware Search for  Inference-Time  LLM Reasoning](cards-0005.md#paper-148924) | 对重复访问的推理簇降权以扩大搜索覆盖 |
| 大语言模型 | 证明验证 | [Escaping the Cognitive Well: Efficient Competition Math with Off-the-Shelf Models](cards-0005.md#paper-150429) | 在独立上下文中验证抽出的命题及其否定 |
| 软件工程 | 泛化评测 | [EsoLang-Bench: Evaluating Large Language Models via Esoteric Programming Languages](cards-0005.md#paper-139789) | 固定算法题并更换程序语言，分离题解能力与语言熟悉度 |
| 大语言模型 | 低显存训练 | [ESSAM: A Novel Competitive Evolution Strategies Approach to Reinforcement Learning for Memory Efficient LLMs Fine-Tuning](cards-0005.md#paper-154196) | 显存紧张时比较零阶演化搜索和反向传播式强化学习 |
| 大语言模型 | 持续学习 | [Estimating and Orthogonalizing Unknown Pre-training Gradients for Continual Fine-tuning of Large Language Models](cards-0005.md#paper-152597) | 用易遗忘伪样本估计未知预训练梯度，再约束新任务更新方向。 |
| 学习理论 | 训练诊断 | [Estimating Implicit Regularization in Deep Learning](cards-0005.md#paper-155112) | 从实际权重更新与损失梯度之差估计等效正则。 |
| 生成模型 | 排列建模 | [Euclidean Score-Based Generative Modeling with Permutation Semantics](cards-0005.md#paper-154221) | 在连续坐标排序区域中建模排列，末端仅排序一次。 |
| 隐私 | 遗忘诊断 | [Evaluating an Evaluation: Membership Inference Attacks as Machine Unlearning Diagnostics](cards-0005.md#paper-139219) | 遗忘验收同时检查指标可分性和随遗忘量变化的单调性。 |
| 学习理论 | 泛化诊断 | [Evaluating Compositional Generalization in Transformers: The Role of Composition Equivalence and Module Coverage](cards-0005.md#paper-139422) | 组合泛化评测同时控制端到端函数等价与模块覆盖。 |
| 计算机视觉 | 推理校准 | [Evaluating Deployable Inference-Time Error Prediction in Vision MoEs](cards-0005.md#paper-139655) | 额外专家的预算优先用于判别路由错误，再评估能否提升准确率。 |
| 计算机视觉 | 推理预算 | [Evaluating Depth and Breadth in Test-Time Scaling for Compositional Visual Generation](cards-0005.md#paper-139290) | 按提示复杂度在并行探索与串行修正间调预算。 |
| 统计学习 | 不确定性评测 | [Evaluating Epistemic Uncertainty: Beyond OOD Detection and Active Learning](cards-0005.md#paper-139438) | 用风险、可约减误差和覆盖率曲面判断不确定性是否有决策用处。 |
| 科学机器学习 | 预训练评测 | [Evaluating Synthetic ECG Pretraining: When Can Patient-Free Simulators Substitute for Real ECG Data?](cards-0005.md#paper-139147) | 分别用冻结探针和全量微调判断合成数据是否可替代实测 |
| Agent | 推理预算 | [Evaluating Test-Time Scaling of General LLM Agents](cards-0005.md#paper-139634) | 分别测增加交互步数和并行轨迹的边际收益 |
| 时间序列 | 校准评测 | [Evaluating Uncertainty Calibration in Probabilistic Time Series Foundation Models](cards-0005.md#paper-138974) | 按预测步长和条件分别测不确定性校准 |
| 大语言模型 | 安全评测 | [Evaluation Awareness in Language Models Has Limited Effect on Behaviour](cards-0005.md#paper-148437) | 用行为差异验证评测意识，避免只看自述频率 |
| 计算机视觉 | 事件成像 | [Event based Multi-Velocity-Scale Imaging](cards-0005.md#paper-150183) | 按运动尺度分配对比度阈值 |
| 具身智能 | 可解释性 | [Event-Grounded Sparse Autoencoders for Vision-Language-Action Policies](cards-0005.md#paper-151283) | 用闭环行为事件排序稀疏自编码器特征 |
| 多模态学习 | 时序训练 | [EventLens: Event-Structure Reinforcement Learning for Video Understanding](cards-0005.md#paper-153545) | 用可验证的事件结构任务替代单纯字幕监督 |
| 多模态学习 | 推理剪枝 | [EventPrune: Cascaded Event-Assisted Token Pruning for Efficient First-Person Dynamic Spatial Reasoning](cards-0005.md#paper-151793) | 用异步事件信号给视频token排序保留动态区域 |
| 强化学习 | 角色适配 | [Events as Triggers for Behavioral Diversity in Multi-Agent Reinforcement Learning](cards-0005.md#paper-153421) | 让事件触发行为切换 |
| 大语言模型 | 水印 | [Every Bit, Everywhere, All At Once: A Binomial Multibit LLM Watermark](cards-0005.md#paper-154368) | 按逐位置信度评估多位水印 |
| 大语言模型 | 约束优化 | [Every Sample Counts: Supervised Fine-Tuning of Language Models with Pointwise Constraints](cards-0005.md#paper-155361) | 用逐样本约束减少尾部违反 |
| 计算机视觉 | 扩散生成 | [Everything at Every Scale: Scale-Invariant Diffusion with Continuous Super-Resolution](cards-0005.md#paper-150103) | 通过同一逆过程的不同起点覆盖连续超分辨率 |
| 计算机视觉 | 开放集检测 | [EviAttr-OW: Evidential Attribute Reasoning for Open World Object Detection](cards-0005.md#paper-152262) | 分开衡量物体证据与已知类支持 |
| 多模态学习 | 奖励设计 | [Evidence-RL: Towards Evidence-intensive Visual Reasoning](cards-0005.md#paper-150393) | 奖励对真正图像证据敏感的正确答案 |
| 大语言模型 | 不确定性 | [Evidential Semantic Uncertainty Decomposition for Large Language Models](cards-0005.md#paper-154010) | 区分语义歧义和模型支持不足 |
| 多模态学习 | 视频定位 | [EVIDENT: Routing MLLM Adaptation through Entity-Grounded Visual Evidence for Cross-Domain Video Temporal Grounding](cards-0005.md#paper-150339) | 用对象槽位约束跨域定位适配 |
| Agent | 软件维护评测 | [EvoCodeBench: Evaluating Coding Agents in Multi-Turn Iterative Interactions](cards-0005.md#paper-139527) | 用累积测试捕捉多轮需求回归 |
| Agent | 合成经验 | [EvoCUA: Evolving Computer Use Agents via Learning from Scalable Synthetic Experience](cards-0005.md#paper-153228) | 为普通桌面任务设计可执行成功判据并复用失败经验 |
| 具身智能 | 几何表征 | [Evo-Depth: A Lightweight Depth-Enhanced Vision-Language-Action Model](cards-0005.md#paper-154131) | 用多视角 RGB 提取隐式深度调制动作表示 |
| 大语言模型 | 强化学习 | [Evolutionary System Prompt Learning for Reinforcement Learning in LLMs](cards-0005.md#paper-149312) | 同时更新提示和权重。 |
| 大语言模型 | 中训练 | [Evolution Fine-Tuning: Learning to Discover Across 371 Optimization Tasks](cards-0005.md#paper-148564) | 把优化搜索过程转成跨任务监督。 |
| 优化 / 大语言模型 | 训练数据 | [EvoOptiGraph: Weakness-Driven Coevolution via Graph-Based Structural Generation for Optimization Modeling](cards-0005.md#paper-155640) | 用建模错误触发保可行的数据变换。 |
| 生成模型 | 量化 | [Exact Channel Decoupling via Joint Diagonalization and Uniform Splicing for Diffusion Transformer Quantization](cards-0005.md#paper-149899) | 联合校准激活和权重，并避免平均时间步。 |
| 大语言模型 | 注意力 | [Exact Flow Linear Attention: Exact Solution from Continuous-Time Dynamics](cards-0005.md#paper-154073) | 以精确流更新替换 delta rule 欧拉步。 |
| 统计学习 | 不确定性传播 | [Exact Gaussian Moment Matching for Residual Networks: a Second-Order Method](cards-0005.md#paper-155943) | 对特定激活直接传播高斯矩。 |
| 优化 | 无损压缩 | [Exact Instance Compression for Convex Empirical Risk Minimization via Color Refinement](cards-0005.md#paper-153709) | 按结构对称性压缩凸经验风险。 |
| 计算机视觉 | 逆问题 | [Exact Posterior Score Estimation for Solving Linear Inverse Problems](cards-0005.md#paper-155154) | 将观测条件融合到去噪训练而保持原采样器。 |
| 生成模型 | 约束采样 | [Exact Regular-Constrained Sampling for Variable-Order Markov Generation](cards-0005.md#paper-155888) | 将可变阶稀疏上下文图与约束自动机相乘。 |
| 图学习 | 约束生成 | [Exact Topological Compliance: Generating Persistence-Equivalent Graphs](cards-0005.md#paper-148463) | 硬性拓扑描述用约束求解验证。 |
| 统计学习 | 机器遗忘 | [Exact Unlearning via Quantized Sufficient Statistics](cards-0005.md#paper-152457) | 把常规删除转化为充分统计更新。 |
| Agent | 协作纠错 | [ExComm: Exploration-Stage Communication for Error-Resilient Agentic Test-Time Scaling](cards-0005.md#paper-154319) | 在探索中间核验分支冲突 |
| 多模态学习 | 合成监督 | [Exemplar2VQA: A Scalable Exemplar-Driven Visual Question Answering Generation Framework via Multi-Agent Coding](cards-0005.md#paper-150839) | 用可运行几何程序生成问答真值 |
| 时间序列 | 缺失建模 | [Existence Precedes Value: Joint Modeling of Observational Existence and Evolving States in Time Series Forecasting](cards-0005.md#paper-148905) | 联合预测观测是否发生和数值 |
| 生成模型 | 流映射 | [Expanding Flow Maps](cards-0005.md#paper-155702) | 让生成流学习输出长度 |
| Agent | 策略探索 | [Expanding LLM Agent Boundaries with Strategy-Guided Exploration](cards-0005.md#paper-152089) | 先采样策略再采样任务动作 |
| 优化 | 最优传输 | [Expected Batch Optimal Transport Plans and Consequences for Flow Matching](cards-0005.md#paper-154399) | 按耦合偏差和积分成本选择小批量大小 |
| 大语言模型 | 安全评测 | [Expected Harm: Rethinking Safety Evaluation of (Mis)Aligned LLMs](cards-0005.md#paper-139760) | 分别评估危害严重性与现实发生可能性 |
| 统计学习 | 假设检验 | [ExperiGen: Agentic Hypothesis Discovery from Observational Data](cards-0005.md#paper-149912) | 要求生成假设经独立证据检验 |
| 大语言模型 | 稀疏化 | [ExpertNavigator: Functionally Coherent Expert Grouping and Pairwise-Ranked Routing for High-Fidelity Dense-to-MoE Conversion](cards-0005.md#paper-149707) | 按功能分组专家并依排序信号训练路由 |
| 大语言模型 | 偏好对齐 | [Explaining and Breaking the Safety-Helpfulness Ceiling via Preference Dimensional Expansion](cards-0005.md#paper-151817) | 改善提示覆盖的目标维度再做多目标对齐 |
| 强化学习 | 奖励建模 | [Explaining and Preventing Alignment Collapse in Iterative RLHF](cards-0005.md#paper-155701) | 迭代 RLHF 中约束策略对后续奖励模型的影响 |
| 多模态学习 | 可解释性 | [Explaining Cross-Modal Model Behavior with Gradient-Estimation-Based Feature Interaction](cards-0005.md#paper-150190) | 估计像素与文本的交互贡献 |
| 强化学习 | 人机协作评测 | [Explanation Mechanism Influences Human Reliance on Reinforcement Learning Agents](cards-0005.md#paper-156138) | 分别检验采纳正确动作和拒绝错误动作 |
| 可解释性 | 稳定性诊断 | [Explanation Multiplicity in SHAP: Characterization and Assessment](cards-0005.md#paper-139691) | 评估归因排名时同时换模型和解释种子 |
| 大语言模型 | 强化学习后训练 | [ExpLang: Improved Exploration and Exploitation in LLM Reasoning with On-Policy Thinking Language Selection](cards-0005.md#paper-153929) | 让策略主动选择推理语言并与固定语言等预算比较。 |
| 表征学习 | 伪标签 | [Exploiting Negative Multi-Cluster Structure in Class-Wise Embeddings for Weakly Supervised Multi-Label Learning](cards-0005.md#paper-153676) | 按类空间保留负例子群。 |
| 强化学习 | 探索设计 | [Exploration as Constrained Policy-Space Optimization](cards-0005.md#paper-153038) | 按任务冲突动态重加权内在奖励。 |
| 强化学习 | 联邦探索 | [Exploration via Exploitation: The Blessing of Reward Diversity in Personalized Federated RL](cards-0005.md#paper-152906) | 在奖励多样性充分时对照显式探索与贪心协作。 |
| 强化学习 | 非平稳评测 | [Exploring Lifelong Adaptation: In-Context Reinforcement Learning in Non-Stationary Environments](cards-0005.md#paper-154772) | 在单段交互里区分突变和渐变的动力学测试。 |
| 多模态学习 | 生成接口 | [Exploring MLLM-Diffusion Information Transfer with MetaCanvas](cards-0005.md#paper-151074) | 让局部空间 token 条件化扩散而非只给全局编码。 |
| 强化学习 | 收敛诊断 | [Exploring Starts Are Not Enough: Counterexamples and a Fix for Monte Carlo Exploring Starts](cards-0005.md#paper-148417) | 按动作更新频率调节蒙特卡罗控制的学习率。 |
| 机器学习系统 | 异步训练 | [Exploring the Limitations of Layer Synchronization in Spiking Neural Networks](cards-0005.md#paper-156760) | 训练时显式纳入部署的异步神经元调度。 |
| 具身智能 | 技能组合诊断 | [Exploring the Limits of Compositional Generalization in Vision-Language-Action Manipulation](cards-0005.md#paper-139255) | 训练与测评覆盖前序技能产生的交接状态。 |
| 大语言模型 | 高效注意力 | [Express Language Modeling](cards-0005.md#paper-149745) | 将双向近似转为因果近似 |
| 大语言模型 | 离线强化学习 | [ExpRFT: Exponential Reward-Weighted Fine-Tuning for Offline RL in Multi-Turn Dialogue](cards-0005.md#paper-154489) | 用温度控制噪声奖励的权重 |
| 计算机视觉 | 低秩适配 | [Extending 3D Reconstruction Models to Any Camera](cards-0005.md#paper-156110) | 先尝试适配而非重训跨相机重建模型 |
| 统计学习 | 评测指标 | [Extending ROC Analysis to Uncertainty-Aware Risk Prediction with an Interval-Based AUC (iAUC)](cards-0005.md#paper-150218) | 对区间预测分别测确定排序和不确定排序 |
| 大语言模型 | 结构化推理 | [Externalized CPDAG Summaries Improve LLM Causal Deduction](cards-0005.md#paper-150273) | 外显因果等价类再回答因果问题 |
| 科学机器学习 | 动力学辨识 | [Extracting Governing Equations from Latent Dynamics via Multi-View Contrastive Learning](cards-0005.md#paper-155982) | 用独立噪声的多视图分离潜动态与观测噪声 |
| 大语言模型 | 推理诊断 | [Extracting Search Trees from LLM Reasoning Traces Reveals Myopic Planning](cards-0005.md#paper-154324) | 检查深层搜索是否实际改变决策 |
| 大语言模型 | 提示评测 | [Extraneous Cognitive Load in Large Language Models](cards-0005.md#paper-150343) | 固定任务难度，仅变动呈现干扰 |
| 大语言模型 | 权重合并 | [Extrapolative Weight Averaging Reveals Correctness–Efficiency Frontiers in Code RL](cards-0005.md#paper-151744) | 比较权重插值和外推能否扩展正确率与效率前沿 |
| 计算机视觉 | 分辨率外推 | [ExtraVAR: Stage-Aware RoPE Remapping for Resolution Extrapolation in Visual Autoregressive Models](cards-0005.md#paper-149109) | 按生成阶段重映射 RoPE 频带 |
| 科学机器学习 | 逆问题 | [Extremely Sparse-View Computed Tomography from 2D Projections via Pose-Aware Diffusion Priors](cards-0005.md#paper-153894) | 仅有二维训练投影时用共享体重投影约束三维反演 |
| 优化 | 流式学习 | [Factor Augmented High-Dimensional SGD](cards-0005.md#paper-148617) | 在高维流式 SGD 中显式建模潜因子估计误差 |
| 优化 | 梯度计算 | [Factorized Gradients for Scalable Highly-expressive Parametric Diffeomorphisms](cards-0005.md#paper-149013) | 将连续变换的轨迹积分与参数投影分开 |
| 计算机视觉 | 三维人体估计 | [FactorizedHMR: A Hybrid Framework for Video Human Mesh Recovery](cards-0005.md#paper-155234) | 稳定主体用回归，模糊关节用概率生成 |
| 强化学习 | 谱表征 | [Factorized Spectral Representations for Reinforcement Learning](cards-0005.md#paper-149364) | 把转移按状态、动作和下一状态拆成三模张量 |
| 大语言模型 | 蒸馏诊断 | [Facts Don't Speak Louder than Words: The Behavioral Essence of Long-CoT Distillation](cards-0005.md#paper-153530) | 分开评估推理过程行为与新增事实的蒸馏收益 |
| 生成模型 | 推理加速 | [FADE: Fractional Anomalous Dynamics Extrapolation for Training-Free Diffusion Transformers Acceleration](cards-0005.md#paper-149903) | 缓存间隔内用分数阶动力学外推扩散特征 |
| 大语言模型安全 | 冗余防御 | [Fail-Closed Alignment for Large Language Models](cards-0005.md#paper-149405) | 用多个相互独立的安全路径降低单点失效 |
| 具身智能 | 失败学习 | [Failing Forward: Adaptive Failure-Informed Learning for Vision-Language-Action Models](cards-0005.md#paper-155737) | 从策略自身失败轨迹学习负向动作引导 |
| 大语言模型 | 行为诊断 | [Failing to Falsify: Evaluating and Mitigating Confirmation Bias in Language Models](cards-0005.md#paper-152161) | 主动提出反例来测试模型假设 |
| 检索系统 | 风险校准 | [Failure-Band Authorization for Filtered Retrieval](cards-0005.md#paper-153631) | 排名不确定时对候选检索计划做校准和回退 |
| 大语言模型 | 蒸馏选样 | [Failure Profiling and Reachable Trajectory Selection for Reasoning Distillation](cards-0005.md#paper-149263) | 按学生失败模式选择其可达的正确教师轨迹 |
| 公平性 | 排序优化 | [Fair Bubble Sort: Provably Optimal Fair Ranking with Continuous Sensitive Attributes](cards-0005.md#paper-155445) | 直接约束连续敏感属性和排名间的秩相关 |
| 多任务学习 | 公平约束 | [FairMT: Fairness for Heterogeneous Multi-Task Learning](cards-0005.md#paper-148409) | 将异构任务的群体差距归一再分配约束压力 |
| 多模态学习 | 公平评测 | [Fairness Failure Modes of Multimodal LLMs](cards-0005.md#paper-149831) | 区分信息充足时过度拒答与歧义时不当断言 |
| 时间序列 | 异步输入编码 | [Faithful Embeddings of Irregular and Asynchronous Data for Online Log-NCDEs](cards-0005.md#paper-150604) | 以事件增量编码替代对观测变量的插值 |
| 可解释性 | 元评测 | [Faithfulness Metrics Don't Measure Faithfulness: A Meta-Evaluation with Ground Truth](cards-0005.md#paper-139844) | 用已知中间计算真值验证思维链忠实度指标 |
| 大语言模型 | 形式验证 | [FaithSieve: Fine-Grained Evaluation of Math Proofs with Faithful Formal Evidence](cards-0005.md#paper-149124) | 形式证明结果须经语义对齐才纳入首错判定 |
| 计算机视觉 | 防御评测 | [FakeParts: a New Family of AI-Generated Video Forgeries](cards-0005.md#paper-138979) | 将媒体检测器在整段合成与局部篡改场景下分别验收 |
| 计算机视觉 | 强化学习后训练 | [FalconPerception-HD: High Density Perception via Reinforcement Learning](cards-0005.md#paper-150365) | 直接对集合级漏检和误检给奖励 |
| 时间序列 | 变量表征 | [Falcon-X: A Time Series Foundation Model for Heterogeneous Multivariate Modeling](cards-0005.md#paper-150872) | 先将异构变量对齐到共享潜原型再建模交互 |
| 计算机视觉 | 时空重建 | [Fast 4D Mesh Generation by Spatio-Temporal Attention Chains](cards-0005.md#paper-151229) | 复用生成骨干内部早期对应以省去显式网格匹配 |
| 学习理论 | 表示对齐 | [Fast Alignment of Embeddings: Computational Guarantees for Anisotropic Procrustes-Wasserstein](cards-0005.md#paper-149973) | 各向异性明显时先估计主方向 |
| 大语言模型 | 训练评测 | [Fast and Accurate Probing of In-Training LLMs' Downstream Performances](cards-0005.md#paper-151812) | 用检查点探针筛选需要生成式复评的时点 |
| 大语言模型 | 线性注意力 | [Fast and Stable Triangular Inversion for Delta-Rule Linear Transformers](cards-0005.md#paper-150772) | 同时按数值准确性和硬件效率选三角求逆 |
| 大语言模型 | 并行解码 | [Fast-dLLM++: Fr\'{e}chet Profile Decoding for Faster Diffusion LLM Inference](cards-0005.md#paper-154725) | 按全体置信度轮廓确定并行提交集合 |
| 强化学习 | 探索 | [FastDSAC: Unlocking the Potential of Maximum Entropy RL in High-Dimensional Humanoid Control](cards-0005.md#paper-151622) | 高速全身控制中按动作维度分配熵 |
| 具身智能 | 实时推理 | [FASTER: Rethinking Real-Time Flow VLAs](cards-0005.md#paper-156001) | 按动作时域优先生成先执行的动作 |
| 强化学习 | 候选筛选 | [FASTER: Value-Guided Sampling for Fast RL](cards-0005.md#paper-149442) | 在去噪尚未完成时筛除低价值动作 |
| 优化 | 曲率近似 | [Fast Gauss-Newton for Multiclass Cross-Entropy](cards-0005.md#paper-153523) | 类别较多时只保留真类对其余类的曲率 |
| 科学机器学习 | 统计速率 | [Fast Learning Rates for Physics-Informed Kernel Methods](cards-0005.md#paper-152762) | 微分数据达到饱和阈值后增加函数值观测 |
| 科学机器学习 | 滚动校正 | [Exactness Matters for Physical Rule Enforcement](cards-0005.md#paper-152917) | 先测校正算子在真实目标上的失真 |
| 科学机器学习 | 物理约束架构 | [Fast Reconstruction of Exact Maxwell Dynamics from Sparse Data](cards-0005.md#paper-148197) | 将可解析物理约束放入基函数 |
| 统计学习 | 判别降维 | [Fast, Relaxation‑ and Hyperparameter‑Free Pairwise Worst-Case Class Separation](cards-0005.md#paper-149044) | 按最难分的类别对选择投影 |
| 大语言模型 | 推理强化学习 | [Fast-RL: Accelerating Reinforcement Learning for LongCoT Reasoning Models](cards-0005.md#paper-148369) | 用短轨迹训练，再在长轨迹模式评估 |
| 机器学习系统 | 结构化计算 | [Fast Sandwich Products in Clifford Algebra](cards-0005.md#paper-149383) | 用低维旋转分解计算多向量作用 |
| 具身智能 | 世界模型消融 | [Fast-WAM: Do World Action Models Need Test-time Future Imagination?](cards-0005.md#paper-149922) | 保留视频共训练并单独测试是否需要推理生成 |
| 统计学习 | 图结构估计 | [Fast Wasserstein rates for estimating probability distributions of probabilistic graphical models](cards-0005.md#paper-156637) | 用节点和父节点局部维度估算分布学习难度 |
| 大语言模型 | 容错训练 | [Fault Tolerance in Transformers Favors Output Alignment over Hidden-State Consistency](cards-0005.md#paper-148441) | 给故障一致性训练优先加输出分布约束 |
| 机器学习基础 | 鲁棒数据压缩 | [Fault Tolerant Coresets](cards-0005.md#paper-153584) | 按允许损坏点数分配核心集冗余 |
| 机器学习系统 | 分布式训练 | [FAUST: Federated Asynchronous Update with Staggered Timescales for Low-Communication Foundation Model Training](cards-0005.md#paper-151814) | 按参数及两阶动量的时间尺度分别同步 |
| 具身智能 | 异步动作反馈 | [FAVLA: A Force-Adaptive Multi-Rate VLA model for Contact-Rich Robotic Manipulation](cards-0005.md#paper-156009) | 按预测力变化安排动作纠正频率 |
| 隐私保护 | 自适应组合 | [𝑓-Differential Privacy Filters: Validity and Approximate Solutions](cards-0005.md#paper-156133) | 动态隐私预算需要重新验证累积规则 |
| 强化学习 | 安全约束优化 | [Feasible Policy Optimization for Safe Reinforcement Learning](cards-0005.md#paper-151552) | 为可行区内外采用不同策略目标 |
| 模型融合 | 特征校准 | [FeatCal: Feature Calibration for Post-Merging Models](cards-0005.md#paper-152364) | 按前向次序修复合并模型表征 |
| 图学习 | 防御诊断 | [Feature-Context Consistency: Unsupervised Adversarial Detection with Drift Stability on Attributed Graphs](cards-0005.md#paper-148620) | 用节点及邻域属性一致性检测异常 |
| 生成模型 | 扩散诊断 | [Feature Information Dynamics in Diffusion](cards-0005.md#paper-152004) | 按去噪时刻量化特征何时出现 |
| 学习理论 | 尺度规律 | [Feature learning  in high-dimensions under structured covariance: Scaling laws in quadratic networks](cards-0005.md#paper-149864) | 将输入协方差谱纳入样本复杂度预测 |
| 计算机视觉 | 表征恢复 | [Feature Recovery for Object Understanding Under Physical Transformation](cards-0005.md#paper-151094) | 用成对变换前后特征监督轻量恢复模块 |
| 统计学习 | 公平校准 | [FedCF: Fair Federated Conformal Prediction](cards-0005.md#paper-152149) | 对联邦保形预测逐组审计覆盖差 |
| 联邦学习 | 概念建模 | [Federated Concept-Based Models: Interpretable models with distributed supervision](cards-0005.md#paper-153466) | 允许解释概念随分布式监督动态扩充 |
| 优化 / 联邦学习 | 分布鲁棒优化 | [Federated Distributionally Robust Neural Combinatorial Optimization with Convergence Guarantees](cards-0005.md#paper-155993) | 用有界成本处理策略梯度方差，并防止最坏组权重塌缩 |
| 图学习 | 联邦消息补偿 | [Federated Graph Learning with Local Message Compensation](cards-0005.md#paper-152765) | 图节点不能跨端共享时用局部代理恢复外邻域信息 |
| 联邦学习 | 参与约束 | [Federated Learning by Utility-Constrained Stochastic Aggregation for Improving Rational Participation](cards-0005.md#paper-150671) | 把客户端留存写入随机聚合优化 |
| 大语言模型 | 模型路由 | [Federate the Router: Learning Language Model Routers with Sparse and Decentralized Evaluations](cards-0005.md#paper-153323) | 用分散、稀疏的查询评估训练跨端共享路由器 |
| 联邦学习 | 连续域适配 | [FedIndex: Federated Domain Adaptation with Continuous Domain Indices](cards-0005.md#paper-156743) | 用连续域索引代替硬分域 |
| 大语言模型 | 联邦低秩微调 | [FedLoVA: Value-Only Aggregation for Federated LoRA Fine-Tuning of Large Language Models](cards-0005.md#paper-148442) | 本地训练查询和值投影，只聚合收敛较快的值投影 |
| 联邦学习 | 代理蒸馏 | [FedPeel: Peeling Stabilized Layers for Robust Heterogeneous Federated Learning](cards-0005.md#paper-151499) | 仅聚合已稳定代理层，并按置信度控制蒸馏 |
| 大语言模型 / 联邦学习 | 参数化 | [Fed-SB: A Silver Bullet for Extreme Communication Efficiency and Performance in (Private) Federated LoRA Fine-Tuning](cards-0005.md#paper-156778) | 共享冻结低秩基，只聚合低维中间矩阵。 |
| 联邦学习 / 优化 | 梯度校准 | [FedVSSAM: Mitigating Flatness Incompatibility in Sharpness-Aware Federated Learning](cards-0005.md#paper-153077) | 让局部扰动、下降和全局步共享更一致的方向估计。 |
| 机器人学 | 闭环预测 | [Feedback World Model Enables Precise Guidance of Diffusion Policy](cards-0005.md#paper-152267) | 部署时用执行反馈修正世界模型预测。 |
| 计算机视觉 | 跨投影表征 | [Feedforward Novel View Synthesis for Heterogeneous Cameras](cards-0005.md#paper-149287) | 让视觉 token 携带图块内完整射线分布。 |
| 大语言模型 | 置信校准 | [Feeling of Knowing in Large Language Models](cards-0005.md#paper-150142) | 知识后训练后重新校准回答、检索或弃答决策。 |
| 优化 | 高阶重参数化 | [FerQ: Fermat Quotient Reformulation of High-Order Binary Optimization](cards-0005.md#paper-152029) | 为高阶二进制项使用精确闭式重写，减少中间变量。 |
| 计算机视觉 | 机制诊断 | [Few Channels Draw The Whole Picture: Revealing Massive Activations in Diffusion Transformers](cards-0005.md#paper-156119) | 检验图像语义是否集中在少量高激活通道 |
| 多模态学习 | 空间定位 | [Few Contrastive Attention Heads Enable Visual Grounding in Large Vision-Language Models](cards-0005.md#paper-156779) | 利用目标与对照描述的差异筛选定位头 |
| 具身智能 | 组合泛化 | [Few-shot Task Learning via Compositional Concept Inference](cards-0005.md#paper-150752) | 从少量示范推断可组合概念再执行 |
| 计算机视觉 | 生成控制 | [Few-Shot Visual Concept Extraction for Steering Diffusion Transformers](cards-0005.md#paper-150793) | 对局部属性用区域内激活均值差，避免全图平均稀释信号 |
| 生成模型 | 密度蒸馏 | [Few-Step Boltzmann Generators via Scalable Likelihood Flow Maps](cards-0005.md#paper-154720) | 在图像生成中比较可向量化密度蒸馏与随机迹估计 |
| 大语言模型 | 轨迹蒸馏 | [Few-Step Diffusion Language Models via Trajectory Self-Distillation](cards-0005.md#paper-151333) | 少步并行解码时让学生匹配完整教师轨迹 |
| 大语言模型 | 稀疏推理 | [FFTSparse: Relative-Position Correlation Guided Sparse Attention for Long-Context Language Models](cards-0005.md#paper-149510) | 用频域相关筛选高响应的相对位置带 |
| 大语言模型 | 模型剪枝 | [FiedlerPrune: Connectivity-Preserving Cross-Layer Pruning for Large Language Models](cards-0005.md#paper-155948) | 将跨层连通性与层内权重重要性一起打分 |
| 因果学习 | 结构正则 | [Fiedler-Regularized Causal Discovery for Sparse Connected DAGs](cards-0005.md#paper-152438) | 已知变量来自同一相连过程时显式约束骨架连通 |
| 多模态学习 | 潜变量对齐 | [Fill the GAP: A Granular Alignment Paradigm for Visual Reasoning in Multimodal Large Language Models](cards-0005.md#paper-149180) | 把解码隐藏态变换到模型输入的特征空间再反馈 |
| 多模态学习 | 特征调节 | [FiLoRA: Focus-and-Ignore LoRA for Controllable Feature Reliance](cards-0005.md#paper-155819) | 固定任务目标，用指令门控改变模型对特征组的依赖 |
| 安全机器学习 | 可信隔离 | [FILOsofer: A TEE-Shielded Model Partitioning Framework based on Fisher Information-Guided LoRA Obfuscation](cards-0005.md#paper-148574) | 将轻量修复参数放入可信端，联合测白盒暴露风险和计算成本 |
| 时间序列 | 低秩建模 | [Filter Banks: from Low-Rank Representations to Deep Models for Efficient Time Series Forecasting](cards-0005.md#paper-152048) | 以可解释秩预算选择滤波器组复杂度 |
| 统计学习 | 联合校准 | [Filtered Conformal Ellipsoids for Graph-Native Time Series](cards-0005.md#paper-155800) | 用状态滤波器定预测椭球形状，用保形校准定半径 |
| 机器学习系统 | 在线训练 | [Filtered-Trace Online Variational Training for Probabilistic Spiking Neural Networks](cards-0005.md#paper-153422) | 用有限维历史迹和截断估计控制时序训练内存 |
| 计算机视觉 | 测试时适配 | [FIND: Frequency Invariance Disentanglement for Test-Time Adaptation in LiDAR 3D Detection](cards-0005.md#paper-155504) | 用频域分支分离内容和传感器变化 |
| 可解释性 | 注意力归因 | [Finding Interpretable Prompt-Specific Circuits in Language Models](cards-0005.md#paper-154226) | 按提示结构比较注意力通信线路 |
| 科学机器学习 | 动力学表示 | [Finding Koopman Invariant Subspaces via Personalized PageRank](cards-0005.md#paper-150950) | 按算子泄漏选择小型观测字典 |
| 优化 | 证明简化 | [Finding Simple Proofs for First-Order Optimization](cards-0005.md#paper-153132) | 对优化收敛证书做稀疏化再人工验证 |
| 评测与诊断 | 基准构建 | [Fine-Grained Benchmark Generation for Comprehensive Evaluation of Foundation Models](cards-0005.md#paper-138954) | 用参考材料覆盖矩阵与解题图验收新题 |
| 大语言模型 | 稀疏架构 | [FineRMoE: Dimension Expansion for Finer-Grained Expert with an Upcycling Approach](cards-0005.md#paper-156104) | 将专家细分扩展到输出维度 |
| 大语言模型 | 防御评测 | [Fine-tuning Does Not Reach All: Uneven Safety and Knowledge Dynamics in Language Models](cards-0005.md#paper-155221) | 安全微调后按知识概念做回归验收 |
| 大语言模型 | 生成诊断 | [Fine-Tuning Improves Information Conveyance in Language Models](cards-0005.md#paper-152334) | 把回答长度和内容不确定性一起分析 |
| 神经科学 | 跨模态迁移 | [Fine-tuning language encoding models on slow fMRI improves prediction for fast ECoG](cards-0005.md#paper-153546) | 用低时间分辨率观测训练表示再评估高频数据 |
| 大语言模型 | 置信度评测 | [Fine-Tuning Language Models to Know What They Know](cards-0005.md#paper-149889) | 优先用区分正确与错误的元认知指标验收 |
| 大语言模型 | 训练数据 | [Finetuning with Sampling: Make SFT Generalize, Not Forget](cards-0005.md#paper-150118) | 用参考模型重采样专家轨迹再监督微调 |
| 具身智能 | 动作监督 | [FineVLA: Fine-Grained Instruction Alignment for Steerable Vision-Language-Action Policies](cards-0005.md#paper-154540) | 为同一任务目标标注执行方式差异 |
| 强化学习 | 有限记忆 | [Finite-Memory Control of POMDPs: Fundamental Limits and Efficient Design](cards-0005.md#paper-153239) | 按混淆后产生的决策损失分配记忆状态 |
| 多模态学习 | 信用分配 | [FiRe: Fine-grained Multimodal Reasoning for Enhanced Image Generation](cards-0005.md#paper-152686) | 对多步生成按中间可检查属性分配奖励 |
| Agent | 数据策略 | [Firefly: Illuminating Verified Real-world Tool Call Data Generation](cards-0005.md#paper-155698) | 从可验证终态反推训练任务，检查可达性与语义一致性 |
| 科学机器学习 | 代理建模 | [First-Order Trajectory Matching: Fast Ensemble Predictions of Chaotic, Turbulent, Stochastic Systems](cards-0005.md#paper-150161) | 从轨迹直接估计概率流，并分开验证边缘分布与通量 |
| 学习理论 | 序列诊断 | [First-Token Attraction in Mamba Dynamics](cards-0005.md#paper-149171) | 比较层间方向与首位置贡献，检测状态空间模型的汇聚 |
| 强化学习 | 策略精修 | [Fisher Decorator: Refining Flow Policy via  A Local Transport Map](cards-0005.md#paper-151066) | 离线策略精修按行为密度方向约束残差 |
| Agent | 统计证据评测 | [Fisher-R1: Training LLM Agents for Reliable Hypothesis Testing](cards-0005.md#paper-152494) | 把统计有效性作为独立验收项，避免只检查执行 |
| 生成模型 | 自适应计算 | [Fixed-Point Masked Generative Modeling](cards-0005.md#paper-155218) | 按变化状态复用上一步隐变量，与冷启动对照 |
| 学习架构 | 迭代停止 | [Fixed-Point Reasoning: Stable and Adaptive Deep Looped Models](cards-0005.md#paper-148540) | 以状态收敛决定循环深度 |
| 统计学习 | 主动抽样 | [Fixed-Size Active Statistical Inference](cards-0005.md#paper-153159) | 固定标注预算时比较条件泊松抽样 |
| 学习理论 | 模型表达 | [Fixed Universal Transformers](cards-0005.md#paper-149666) | 比较权重适配与输入编码的表达能力 |
| 大语言模型 | 上下文压缩 | [Fix the Structural Bottleneck: Context Compression via Explicit Information Transmission](cards-0005.md#paper-152205) | 用全局槽位分配替代逐槽独立聚合 |
| 强化学习 | 策略优化 | [FLAG: Flow Policy MaxEnt-RL by Latent Augmented Guidance](cards-0005.md#paper-151542) | 高维动作策略使用局部采样减缓重要性权重退化 |
| 多模态学习 | 检索评测 | [FLARE: Full-Modality Long-Video Audiovisual Retrieval Benchmark with User-Simulated Queries](cards-0005.md#paper-139338) | 以单模态失败、双模态成功筛选联合检索样例 |
| 优化 / Agent | 形式验证 | [FLARE: Verifying MILP Reformulations with LLM-Based Formal Proof Synthesis](cards-0005.md#paper-149137) | 给整数规划重写加入可核验的等价证明 |
| 机器学习系统 | 高阶微分 | [FlashBoB: I/O-Efficient Exact Backward-over-Backward for Softmax Attention](cards-0005.md#paper-150295) | 以逐行充分量设计注意力二阶反传内核 |
| 大语言模型 | 推理加速 | [Flash-dLLM: IO-Aware KV Caching and Parallel Decoding for Fast, Memory-Efficient Diffusion LLMs](cards-0005.md#paper-152191) | 联合设计扩散解码缓存和候选验证 |
| 机器人学 | 动作表示 | [FLASH: Efficient Visuomotor Policy via Sparse Sampling](cards-0005.md#paper-153691) | 用连续多项式表示动作并从历史系数启动生成 |
| Agent | 异步执行 | [FlashEvolve: Accelerating Agent Self-Evolution with Asynchronous Stage Orchestration](cards-0005.md#paper-150533) | 按版本处理过期的提示或工作流产物 |
| 机器学习系统 | 模型架构 | [FlashFFN: Multi-Head Decomposition Enables I/O-Aware Feed-Forward Network](cards-0005.md#paper-151360) | 以片上累加空间约束设计 FFN 的分头宽度 |
| 机器学习系统 | 聚类加速 | [Flash-KMeans: Fast and Memory-Efficient Exact K-Means](cards-0005.md#paper-151963) | 融合距离与在线最小值，并用逆映射消除更新争用 |
| 机器学习系统 | 分布式注意力 | [FlashMask-3: Efficient and Expressive Mask-Aware Distributed Attention](cards-0005.md#paper-148370) | 用键索引的边界向量在本地裁剪结构掩码 |
| 序列模型 | 状态转移 | [Flash PD-SSM: Memory-Optimized Structured Sparse State-Space Models](cards-0005.md#paper-153142) | 用稀疏转移矩阵库替代单一固定转移。 |
| 自动驾驶 | 闭环规划 | [FlashPlanner: Real-Time Goal-Conditioned Flow-Matching Planning for Autonomous Driving with Online RL Fine-Tuning](cards-0005.md#paper-151391) | 用紧凑连续目标连接导航意图与生成式规划。 |
| 统计学习 / 系统 | 计算重排 | [Flash-SD-KDE: Accelerating SD-KDE with Tensor Cores](cards-0005.md#paper-151863) | 先将核估计重写成矩阵乘，再决定是否保留统计修正。 |
| 三维视觉 | 几何蒸馏 | [FlashSSM-3D: A Distilled State Space Model for Lightning-Fast Dense 3D Reconstruction](cards-0005.md#paper-149335) | 跨架构蒸馏时直接约束全局几何和视角一致。 |
| 序列模型 | 线性注意力 | [Flexformer: Flexible Linear Transformer with Learnable Attention Kernel](cards-0005.md#paper-154501) | 训练 Fourier 特征的频率以调节线性注意力核。 |
| 统计学习 | 基准诊断 | [Flexible Intensities Matter: A comprehensive re-evaluation of Classical and Neural Temporal Point Processes](cards-0005.md#paper-139473) | 比较神经和经典点过程前先匹配强度函数的灵活性。 |
| 机器学习系统 | 推理路由 | [Flexible Routing via Uncertainty Decomposition](cards-0005.md#paper-149927) | 区分可由专家降低的不确定性和应触发弃答的歧义。 |
| 大语言模型 | 模型压缩 | [FlexMoE: One-for-All Nested Intra-Expert Pruning for MoE Language Models](cards-0005.md#paper-151034) | 训练一系列可嵌套的专家子网以跨设备切换预算。 |
| 计算机视觉 | 逆问题 | [FLINT: Coupling Proximal Initialization and Bounded Stochasticity for Flow-Matching Inverse Problems](cards-0005.md#paper-149594) | 联合选择初始化与累积采样噪声预算。 |
| 学习理论 | 稳健性估计 | [FLIP: Fast and Accurate Global Lipschitz Estimation for Large Feedforward Networks](cards-0005.md#paper-152411) | 用递归传播把全局 SDP 估计拆为一维凸子问题。 |
| 优化 | 离散训练 | [Flipping Bits, Not Gradients: Sharpness-Aware Minimization Directly on the Boolean Hypercube](cards-0005.md#paper-150844) | 用 Hamming 扰动定义二值网络的锐度。 |
| 联邦学习 | 参数高效训练 | [FLoRA-Chef: Making A Good LoRA Recipe in Federated Generalization](cards-0005.md#paper-149413) | 分别决定两个 LoRA 因子的聚合时机和权重。 |
| 科学机器学习 | 后验采样 | [Flow Annealing Posterior Sampling for Function-Space Regression and Inverse Problems](cards-0005.md#paper-148653) | 用函数空间先验推断不同查询网格上的后验。 |
| Agent | 工作流路由 | [FlowBank: Query-Adaptive Agentic Workflows Optimization through Precompute-and-Reuse](cards-0005.md#paper-153098) | 离线构建互补流程库，在线按查询选择。 |
| 统计学习 | 共形预测 | [Flow-Based Conformal Predictive Distributions](cards-0005.md#paper-153168) | 从共形集合构造可采样分布。 |
| 深度学习 | 注意力 | [Flow-based Spectral Kernel Learning for Nonstationary Attention](cards-0005.md#paper-151466) | 以非平稳核替换固定相似度。 |
| 计算机视觉 | 形状优化 | [Flow-Corrected Shape Optimization: Taming Manifold Drift in High-Dimensional 3D Models](cards-0005.md#paper-148446) | 分开做目标优化和有效形状校正。 |
| 时间序列 | 异常检测 | [Flow+Diff: Unifying Flow and Diffusion Representations for Multivariate Time Series Anomaly Detection](cards-0005.md#paper-152468) | 用两种潜表征的分歧替代总重建误差。 |
| 生成模型 | 黑盒引导 | [Flow-Direct: Feedback-Efficient and Reusable Guidance for Flow Models via Non-Parametric Guidance Field](cards-0005.md#paper-151143) | 缓存历史奖励样本以复用引导。 |
| 强化学习 | 生成策略优化 | [Flow-DPPO: Divergence Proximal Policy Optimization for Flow Matching Models](cards-0005.md#paper-150977) | 以逐步高斯 KL 代替单样本比率剪切。 |
| 深度学习 | 时空建模 | [Flow Equivariant State Space Model](cards-0005.md#paper-149264) | 先沿运动输送记忆再更新。 |
| 具身智能 | 动作生成 | [FlowHOI: Flow-based Semantics-Grounded Generation of Hand-Object Interactions for Dexterous Robot Manipulation](cards-0005.md#paper-155765) | 显式生成手、物体和接触状态。 |
| 计算机视觉 | 图像复原 | [Flow Map Denoisers: Traversing the Distortion-Perception Plane for Inverse Problems](cards-0005.md#paper-154398) | 以展望时间控制保真与感知质量。 |
| 大语言模型 | 少步生成 | [Flow Map Language Models: One-step Language Modeling via Continuous Denoising](cards-0005.md#paper-152052) | 用连续 token 流蒸馏单步映射。 |
| 强化学习 | 离散策略 | [Flow Matching for Offline Reinforcement Learning with Discrete Actions](cards-0005.md#paper-153771) | 把流匹配推广到离散动作。 |
| 强化学习 | 策略优化 | [Flow Matching Policy Optimization with Mirror Descent and Entropy Constraints](cards-0005.md#paper-148142) | 用优势加权流匹配实现镜像下降。 |
| 强化学习 | 训练部署迁移 | [Flow Matching Reinforcement Learning via SDE Inference](cards-0005.md#paper-153016) | 训练采用随机推理，部署采用确定性推理。 |
| 计算机视觉 | 异常检测 | [Flow Mismatching: Unsupervised Anomaly Detection via Velocity Discrepancies in Flow Matching Models](cards-0005.md#paper-148833) | 对照重建误差和场速度偏差，检查异常是否被过强生成器掩盖。 |
| 统计学习 | 随机估计 | [Flow Perturbation++: Multi-Step Unbiased Jacobian Estimation for High-Dimensional Boltzmann Sampling](cards-0005.md#paper-152021) | 在同计算预算下比较单次估计和分步估计的方差及有效样本量。 |
| 自动驾驶 | 条件策略 | [FlowR2A: Learning Reward-to-Action Distribution for Multimodal Driving Planning](cards-0005.md#paper-148780) | 在固定候选数量下对照奖赏条件生成和生成后打分。 |
| Agent | 工作流构建 | [FlowSteer: Towards Agents Designing Agentic Workflows via Reinforced Progressive Canvas Editing](cards-0005.md#paper-152705) | 在同执行预算下比较原子编辑与一次性生成，记录修复成功率。 |
| 计算机视觉 | 视频编辑 | [FlowTrack: Controlling Edit-Signal Execution in Inversion-Free Flow Video Editing](cards-0005.md#paper-152250) | 以相同编辑信号比较直接注入与有记忆控制，分测语义和运动保持。 |
| 大语言模型 | 稀疏推理 | [Flux Attention: Context-Aware Hybrid Attention for Efficient LLMs Inference](cards-0005.md#paper-154703) | 同时测算量和墙钟时间，避免忽略不均衡的同步成本。 |
| 生成模型 | 采样 | [FluxLite: Inference-Time Proposal Control for Discrete Diffusion Models](cards-0005.md#paper-152301) | 同时报告权重方差和有效样本量，区分目标正确与有限预算下的效率。 |
| 机器学习系统 | 数据调度 | [Flux: Online, Fine-Grained Data Scheduling for Training Machine Learning Interatomic Potentials](cards-0005.md#paper-151170) | 按真实计算负载而非样本数做分布式均衡。 |
| Agent | 检索策略评测 | [FML-bench: A Controlled Study of AI Research Agent Strategies from the Perspective of Search Dynamics](cards-0005.md#paper-139220) | 固定基础设施和等预算，对照策略时记录探索过程而非只看终分。 |
| 可解释性 | 跨层字典 | [fmxcoders: Factorized Masked Crosscoders for Cross-Layer Feature Discovery](cards-0005.md#paper-154897) | 用功能一致性验证跨层特征 |
| 强化学习 | 奖励聚合 | [Focal Reward: Balanced Reinforcement Learning under Rubric-Based Rewards](cards-0005.md#paper-150481) | 按当前准则饱和程度动态分配奖励权重 |
| 计算机视觉 | 深度估计 | [Focusable Monocular Depth Estimation](cards-0005.md#paper-153419) | 用提示为特定区域分配深度估计能力 |
| 可靠性 | 形式验证 | [FocusBranch: Combinatorial Branch-and-Bound for $\ell_0$ Neural Network Robustness Verification](cards-0005.md#paper-152059) | 按局部错误预算组织可验证子问题 |
| 视频生成 | 缓存优化 | [Focused Forcing: Content-Aware Per-Frame KV Selection for Efficient Autoregressive Video Diffusion](cards-0005.md#paper-148676) | 按生成帧和注意力头分配历史缓存 |
| 多模态学习 | 幻觉诊断 | [Focus Matters: Attention-Value Dynamics for Hallucination Mitigation in Vision-Language Models](cards-0005.md#paper-155092) | 检查低注意力位置的值向量对幻觉的作用 |
| 具身智能 | 导航监督 | [FocusNav: Learning Task-directed Perception via Action-Aware Future Reconstruction in Vision-and-Language Navigation](cards-0005.md#paper-149699) | 给感知增加动作条件的未来视觉监督 |
| 联邦学习 | 优化 | [Focus on Where You Aggregate: Restricted SAM for Non-IID Federated Learning](cards-0005.md#paper-150522) | 把平坦化限制在参数实际聚合区域 |
| 优化 | 梯度干扰 | [FOGO: Forgetting-aware Orthogonalization Optimizer](cards-0005.md#paper-152816) | 用历史方向识别当前更新对稀有模式的干扰 |
| 具身智能 | 闭环评测 | [Follow-Bench 2.0: An End-to-End 3D Benchmark for Socially-Aware Robot Person Following](cards-0005.md#paper-139022) | 联合测跟随中的身份保持、遮挡恢复和舒适距离 |
| 生成模型 | 流匹配 | [Follow the Mean: Reference-Guided Flow Matching](cards-0005.md#paper-150971) | 换参考集而不重训模型以控制生成属性 |
| 优化 | 收敛反例 | [Follow the Regularized Leader Does Not Converge in Constrained Optimization](cards-0005.md#paper-150986) | 同时监测目标值和 KKT 残差 |
| 强化学习 | 策略更新 | [Follow the Winners: Conservative Policy Improvement with the Cross-Entropy Method for Critic-Free RFT](cards-0005.md#paper-148167) | 用回报排序的多项式集中控制无评论器微调 |
| 机器学习基础 | 多目标优化 | [FoMEMO: Towards Foundation Models for Expensive Multi-objective Optimization](cards-0005.md#paper-154247) | 按偏好拆解后验学习 |
| 计算机视觉 | 质量评测 | [FoMo: Forking Moment in Generative Trajectory as a Perceptual Distance](cards-0005.md#paper-152890) | 用扩散分叉时刻生成感知距离标注 |
| 机器人学 | 不确定性监督 | [ForceBody: Force-Paired Parametric Body Motion with Torque Uncertainty](cards-0005.md#paper-138956) | 用标签不确定度加权逆动力学监督 |
| 大语言模型 | 基准诊断 | [Forced Orders: What LLM Leaderboards Hide About Model Comparisons](cards-0005.md#paper-139069) | 用能力分层表达榜单无法支持的精细排序 |
| 机器人学 | 力觉控制 | [ForceFlow: Learning to Feel and Act via Contact-Driven Flow Matching](cards-0005.md#paper-151896) | 分别建模视觉接近与力觉接触 |
| 机器人学 | 特权蒸馏 | [ForceLDM: A Force-aware Latent Dynamics Model for Contact-Rich Manipulation](cards-0005.md#paper-156065) | 用未来力觉教当前观测策略预测接触 |
| 大语言模型 | 代理评测 | [Forecasting Downstream Performance of LLMs With Proxy Metrics](cards-0005.md#paper-152033) | 用专家解答上的分布统计预测模型下游能力 |
| 机器人学 | 流匹配 | [ForesightFlow: Self-Guided Flow Matching for Improving Vision-Language-Action Models](cards-0005.md#paper-151608) | 把动作改进加权与成功评分校准分开 |
| 多模态学习 | 防御检测 | [Forgery Evidence Peaks Mid-Stack: Forensic Evidence Relay for Multimodal Forgery Detection](cards-0005.md#paper-153986) | 按逐层证据探针选择检测特征读出层 |
| 机器学习基础 | 遗忘评测 | [Forgetting Has Neighbors: Localized Collateral Forgetting in Machine Unlearning](cards-0005.md#paper-152962) | 在删除集合邻域单独衡量遗忘副作用 |
| 统计学习 | 数据筛选 | [Forgetting to Improve: Principled Data Removal in Active Learning](cards-0005.md#paper-148637) | 模型失配时检验删除有害样本能否改进目标任务 |
| 机器学习基础 | 主动特征获取 | [Forward Shapley Scoring for Non-Myopic Active Feature Acquisition](cards-0005.md#paper-149516) | 用组合边际价值选择当前查询 |
| 优化 | 二阶预条件 | [FOAM: Factored One-sided Adam-Moment for Practical and Scalable SOAP](cards-0005.md#paper-149122) | 输出曲率近各向同性时，仅预条件输入侧。 |
| 强化学习 | 多目标流策略 | [Foundation Pareto Flow Policy for Multi-Objective Reinforcement Learning](cards-0005.md#paper-150940) | 以轨迹流匹配学习可按偏好适配的 Pareto 策略。 |
| 大语言模型 | 蒸馏 | [Found in Conversation: LLMs Teach Themselves to Close the Multi-Turn Gap](cards-0005.md#paper-148841) | 让教师读聚合信息、学生读同信息的多轮对话。 |
| 计算机视觉 | 三维重建 | [FoundSurface: Feedforward Ray-Based 3D Scene Surface Reconstruction from Unposed Images](cards-0005.md#paper-149835) | 用点图筛参考视角，再在射线上求连续表面。 |
| 计算机视觉 | 视觉状态空间 | [Foveal-Mamba: Inside-Out Ring Scanning with Recurrent Offset Prediction for Visual State Space Models](cards-0005.md#paper-148775) | 让形变采样偏移依赖沿扫描累积的隐状态。 |
| 计算机视觉 | 可解释架构 | [Foveated BagNet: Inherent Interpretability Does Not Exclude Global Context](cards-0005.md#paper-149976) | 在局部分类器中用清晰中心加低分辨率外围。 |
| 大语言模型 | 推理量化 | [Fractional Power-of-Two Quantization for Efficient and Effective Multiplier-Free LLM Inference](cards-0005.md#paper-152899) | 半倍频量化网格让低位宽移位加法保留更密权重刻度。 |
| 序列建模 | 长记忆状态空间 | [Fractional State Space Transition for Long Sequence Modeling](cards-0005.md#paper-150427) | 用对数间隔指数模态模拟幂律衰减，并保留有界状态。 |
| 多模态学习 | 推理预算 | [FrameRouter: Frame Budget Routing for Long-Video Understanding on Video-MME-v2 and Beyond](cards-0005.md#paper-155391) | 保持平均帧数不变，按问题证据需求分配预算。 |
| 计算机视觉 | 流式几何记忆 | [FrameVGGT: Coherence-Preserving Memory for Bounded Streaming Geometry](cards-0005.md#paper-154230) | 以完整帧为缓存单元，保留互补视角和稀疏长期锚点。 |
| 具身智能 | 伪标注 | [FreeAct: Demonstration-Free Robot Adaptation via Action-Grounded Generated Videos](cards-0005.md#paper-148622) | 先对齐末端运动再从生成视频提取监督 |
| 大语言模型 | 并行解码 | [Free Draft-and-Verification: Toward Lossless Parallel Decoding for Diffusion Large Language Models](cards-0005.md#paper-153859) | 复用扩散模型预测并逐轮校验静态解码一致性 |
| 优化理论 | 重尾梯度 | [Free Heavy-Tailed Lunch for Muon: A Theoretical Justification of Empirical Success](cards-0005.md#paper-155600) | 按矩阵几何与驻点指标比较优化器 |
| 大语言模型 | 多样采样 | [Free Lunch for Pass@$k$? Low Cost Diverse Sampling for Diffusion Language Models](cards-0005.md#paper-148432) | 在生成中对既有候选的特征做排斥 |
| 具身智能 | 占据预测 | [FreeOcc: Decoupling Ego-Motion for Efficient 4D Occupancy Forecasting via Continuous Flow Matching](cards-0005.md#paper-149840) | 显式消去已知自运动，并让求解预算集中于模糊区域 |
| 计算机视觉 | 视频生成 | [FreeSpec: Training-Free Long Video Generation via Singular-Spectrum Reconstruction](cards-0005.md#paper-149836) | 按奇异谱融合长程一致性和局部动态 |
| 计算机视觉 | 缓存加速 | [FreqCa: Accelerating Image generation and editing via Frequency-Aware Caching](cards-0005.md#paper-148488) | 低频直接复用，高频按时间走势预测 |
| 具身智能 | 动作表示 | [Frequency‑Aware Flow Matching for Continuous and Consistent Robotic Action Generation](cards-0005.md#paper-154121) | 在频域学习动作并用连续基重建 |
| 序列建模 | 循环架构 | [Frequency Domain Reservoir Computing](cards-0005.md#paper-151162) | 把循环更新与非线性留在频域 |
| 科学机器学习 | 结构保持 | [Frequency-Structured Hamiltonian Neural Network for Multi-Timescale Dynamics](cards-0005.md#paper-149155) | 分频训练动力学，再合成为一个守恒生成量 |
| 机器学习系统 | 并行训练 | [FRESCO: A Novel Consistency Control for Asynchronous Pipeline Parallel Training](cards-0005.md#paper-154282) | 限制异步更新改变前向激活子空间的程度。 |
| 强化学习 | 世界模型 | [Freshness-Gated Imagination: Step-Level Trust for Latent World Models](cards-0005.md#paper-150248) | 一起验证轨迹级采样与步级梯度门控。 |
| 可解释性 | 梯度归因 | [FRInGe: Distribution-Space Integrated Gradients with Fisher–Rao Geometry](cards-0005.md#paper-149612) | 用预测分布几何替换任意输入插值。 |
| 强化学习 | 持续适配 | [From Anti-Forgetting to Fast Adaptation: Continual Reinforcement Learning with World Models](cards-0005.md#paper-150468) | 任务切换时按奖励分歧探索、按动力学误差调整规划长度。 |
| 可解释性 | 归因路径 | [From Baselines to Transport Geodesics: Axiomatic Attribution via Optimal Generative Flows](cards-0005.md#paper-155282) | 把特征归因的积分规则和参考到数据的路径分别设计。 |
| Agent | 状态监督 | [From Click Imitation to Transition Equivalence: Rethinking Supervision for GUI Agents](cards-0005.md#paper-152618) | 用可验证状态转移定义等价操作。 |
| 多模态学习 | 流式翻译 | [From Clips to Streams: A Unified Framework for Streaming Sign Language Translation](cards-0005.md#paper-155080) | 联合优化事件定位和翻译，并比较学习边界与人工边界。 |
| 学习理论 | 合成数据 | [From Collapse to Improvement:  Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources](cards-0005.md#paper-148326) | 迭代自训练时联合选择新鲜真实样本比例与采样量。 |
| 多模态学习 | 离散扩散 | [From Denoising to Refining: A Corrective Framework for Vision-Language Diffusion Model](cards-0005.md#paper-150917) | 让并行生成器学会重访和更正已有输出。 |
| 大语言模型 / 优化 | 原型监督 | [From Expert Knowledge to Optimization Modeling: Prototype-Based Data Synthesis and Logical Reinforcement Learning](cards-0005.md#paper-153007) | 先识别经典优化原型，再监督变量到约束的构造顺序。 |
| 大语言模型 | 参数高效微调 | [From Experts to Sub-experts: Fine-grained Parameter-Efficient Fine-Tuning for MoE LLMs](cards-0005.md#paper-155254) | 在 MoE 内选通道组微调。 |
| 多模态学习 | 跨视频推理 | [From Finding to Linking: Benchmarking and Advancing Cross-Long-Video Reasoning for Multimodal LLMs](cards-0005.md#paper-148946) | 将视频定位和跨视频证据绑定拆成可独立核验的阶段。 |
