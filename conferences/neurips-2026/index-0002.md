# NeurIPS 2026 论文索引 · 第 2 卷

[会议首页](README.md)

| 领域 | 技术类型 | 论文卡 | 能改变的技术选择 |
| --- | --- | --- | --- |
| 多模态 | 功能 token | [ATLAS: Agentic or Latent Visual Reasoning? One Word is Enough for Both](cards-0002.md#paper-155024) | 把视觉操作编码成共享的离散词元 |
| 图学习 | 跨域表示 | [AtlasULP: Domain-aware Universal Link Prediction via Relation Atlas](cards-0002.md#paper-150816) | 用关系图谱补充局部采样 |
| 视频生成 | 多尺度生成 | [AtlasVid: Efficient Ultra-High-Resolution Long Video Generation via Decoupled Global-Local Modeling](cards-0002.md#paper-150426) | 先规划低分辨率全局视频再细化 |
| 科学机器学习 | 可验证奖励 | [AtmoZero: Self-Play Post-Training for Caption-Free Weather Time-Series Captioning](cards-0002.md#paper-152217) | 用观测证据反驳不实描述 |
| 科学机器学习 | 材料模拟 | [AtomMOF: All-Atom Flow Matching for MOF-Adsorbate Structure Prediction](cards-0002.md#paper-149909) | 对比联合柔性建模与刚性宿主假设 |
| 算法 | 近似聚类 | [Atoms and Pivot Based Correlation Clustering](cards-0002.md#paper-153440) | 识别不应拆分的顶点组再执行 pivot |
| 科学机器学习 | 时序记忆 | [AtomWorld-Mem: Memory-Restored World States for Long-Horizon Atomistic Evolution](cards-0002.md#paper-155270) | 用历史恢复瞬时晶体快照遗漏的状态 |
| 图学习 | 拓扑预测 | [A Topological Encoder Decoder Framework for Temporal Graph Learning](cards-0002.md#paper-151161) | 先预测未来拓扑再生成节点及边 |
| 因果推断 | 基准诊断 | [A Topological Sorting Criterion for Random Causal Directed Acyclic Graphs](cards-0002.md#paper-154767) | 检查随机因果图能否由亲缘计数轻易排序 |
| 多模态 | 提示选择 | [A Training-Free Video Moment Retrieval Framework via Selection from Multiple Visual Prompts](cards-0002.md#paper-149512) | 分别运行提示并保留原始预测作为候选 |
| 数值优化 | 预条件 | [A Transformer-Derived Iterative Preconditioner](cards-0002.md#paper-153148) | 从模型发现迭代式预条件，再写成独立算法 |
| 概率建模 | 信赖域 | [A Trust Region Approach for Learning Schrödinger Bridges](cards-0002.md#paper-149517) | 目标仅有非归一密度时约束桥接迭代步幅 |
| 图优化 | 投影加速 | [AT-SKM-Net: An Accelerated Trainable Sampling Kaczmarz-Motzkin Framework for Linear Hard-Constraint Feasibility on Dynamic Graphs](cards-0002.md#paper-149152) | 在动态硬约束中复用低秩分解更新 |
| 视觉学习 | 特征提取 | [Attending on Attention ($A^2$): Smaller Self-Supervised ViTs Localize Better Than Larger Ones](cards-0002.md#paper-154201) | 小模型负责定位、大模型负责局部嵌入 |
| 视频生成 | 流式记忆 | [Attend Locally, Remember Linearly: Linear Attention as Cross-Frame Memory for Autoregressive Video Diffusion](cards-0002.md#paper-154730) | 在帧内保留 softmax，跨帧使用固定状态 |
| 多模态 | 人类注视对照 | [Attention Alignment Between Humans and Vision-Language Models](cards-0002.md#paper-155371) | 分开检查编码器与解码器对注意力匹配的影响 |
| 学习理论 | 经验贝叶斯 | [Attention as In-Context Empirical Bayes: A Two-Stage View via Particle Dynamics](cards-0002.md#paper-149497) | 分开调节上下文精炼深度和原始查询保留。 |
| 学习理论 | 谱估计 | [Attention-based PCA](cards-0002.md#paper-154448) | 将上下文主方向恢复用于诊断注意力表示。 |
| 因果学习 | 摊销推断 | [Attention-Based Pretraining for Unsupervised Amortized Causal Discovery](cards-0002.md#paper-153811) | 多个域共享图结构求解器。 |
| 科学机器学习 | 多模态路由 | [Attention-based Routing for Interpretable Multimodal Brain Encoding](cards-0002.md#paper-152519) | 用脑区查询替代全局静态融合。 |
| 大语言模型 | 扩散采样 | [Attention-Based Sampler for Diffusion Language Models](cards-0002.md#paper-149963) | 按注意力列和排序解掩码位置。 |
| 神经符号学习 | 软约束 | [Attention-Based Soft Answer Sets](cards-0002.md#paper-151077) | 将离散求解替换为可微不动点残差。 |
| 大语言模型 | 并行解码 | [Attention-Discounted Adaptive Sampler for Masked Diffusion Language Models](cards-0002.md#paper-150267) | 对依赖已选低置信位置的候选打软折扣。 |
| 大语言模型 | 推测解码 | [Attention Drift: What Auto-Regressive Speculative Decoding Models Learn](cards-0002.md#paper-152952) | 按草稿深度监控状态范数并加归一化。 |
| 多模态学习 | 视觉定位 | [Attention Heads are Complementary Visual Units: Mitigating Hallucinations in LVLMs via Adaptive Visual Cues Focusing](cards-0002.md#paper-149428) | 保留各注意头独有的视觉证据。 |
| 大语言模型 | 路由压缩 | [Attention Is More Than You Need: Spectral Redundancy in Multi-Head Routing](cards-0002.md#paper-155116) | 分别测共享 KV 与实际路由谱冗余。 |
| 计算机视觉 | 流式重建 | [Attention Itself Could Retrieve. RetrieveVGGT: Training-Free Long Context Streaming 3D Reconstruction via Query-Key Similarity Retrieval](cards-0002.md#paper-150300) | 用早层查询键相似度选取固定数量历史帧。 |
| 大语言模型 | 量化稳定性 | [Attention Sinks and Outliers in Attention Residuals](cards-0002.md#paper-148314) | 允许跨层路由显式表达空选择。 |
| 可解释性 | 谱诊断 | [Attention Sinks as Spectral Spikes: A Mechanism Analysis of Gated Attention](cards-0002.md#paper-153587) | 按谱和梯度两条路径检验注意力门控。 |
| 可解释性 | 梯度诊断 | [Attention Sinks Induce Gradient Sinks: Massive Activations as Gradient Regulators in Transformers](cards-0002.md#paper-151217) | 用值路径梯度干预区分汇聚和大激活。 |
| 强化学习 | 训练诊断 | [Attention Trajectories as a Diagnostic Axis for Deep Reinforcement Learning](cards-0002.md#paper-156756) | 按对象和模态追踪显著性轨迹。 |
| 计算机视觉 | 注意力蒸馏 | [Attention Transfer Is Not Universally Effective for Vision Transformers](cards-0002.md#paper-156052) | 跨教师家族前先验证学生架构兼容。 |
| 模型审计 | 来源验证 | [AttnDiff: Attention-based Differential Fingerprinting for Large Language Models](cards-0002.md#paper-151981) | 用差分行为表征交叉验证模型谱系。 |
| 学习理论 | 鲁棒学习 | [Attribute-Efficient Learning of Sparse Halfspaces with Constant Malicious Noise Rate](cards-0002.md#paper-153863) | 稀疏分类遇固定比例污染时按有效维数估算数据。 |
| 高效推理 | 早退出 | [Attribution-Guided Exit Policy for Reliable Early-Exit Inference](cards-0002.md#paper-152941) | 把跨层归因稳定性作为置信度的补充。 |
| 多模态学习 | 表征对齐 | [Attribution-Guided Shared-Private Decoupling for Noise-Reduced Audio-Visual Representation Learning](cards-0002.md#paper-150554) | 用跨模态相关片段监督共享特征。 |
| 可解释性 | 二阶归因 | [Attributions All the Way Down? The Metagame of Interpretability](cards-0002.md#paper-148384) | 分开测特征对输出和对彼此归因的影响。 |
| 联邦学习 | 张量语言 | [A typed tensor language for federated learning](cards-0002.md#paper-150243) | 先检查分布式计算能否表示成固定共享状态。 |
| 强化学习 | 多目标调度 | [Auction-Based Online Policy Adaptation for Evolving Objectives](cards-0002.md#paper-153035) | 为运行期出现或消失的目标动态插拔局部策略。 |
| 多模态学习 | 空间音频 | [Audible World Models: Spatially Aware Sound Generation for 3D Worlds](cards-0002.md#paper-154507) | 把声源附着到三维几何，再按听者位置渲染。 |
| 语音 Agent | 故障归因 | [AudioAgentBench: Evaluating Multi-Turn Voice Agents on Real-World Tasks](cards-0002.md#paper-139120) | 按回合定位第一次失误并避免重复扣分。 |
| 音频生成 | 条件路由 | [AudioCALM: Continuous Autoregressive Language Modeling for Universal Audio Generation](cards-0002.md#paper-149240) | 共享音效和音乐模型，并为语音保留独立残差。 |
| 音频学习 | 压缩表征 | [AudioGS: High-Fidelity Neural Audio Compression via Continuous Gaussian Splatting](cards-0002.md#paper-149852) | 用可渲染基元分解代替训练期码本量化。 |
| 音频学习 | 自监督表征 | [AudioSphere: Towards Self-Supervised Spatial Audio Representation Models](cards-0002.md#paper-151452) | 掩码重建时同时恢复频谱与方向线索。 |
| 多模态学习 | 时序推理 | [Audio-Visual Flamingo: Open Audio-Visual Intelligence for Long and Complex Videos](cards-0002.md#paper-153983) | 用时间戳连接长视频的中间音视频证据。 |
| 科学评测 | 错误诊断 | [Auditing AI peer reviewers: a dose-response and false-positive benchmark on real scientific papers](cards-0002.md#paper-152885) | 用严重度梯度和误报率联合评估自动审稿。 |
| 可靠性 | 分布外诊断 | [Auditing Attention Head Masking for Out-of-Distribution Detection: Cross-Architecture Wins, Failures, and Polarity Inversions](cards-0002.md#paper-139256) | 先检查异常分数方向再跨骨干部署。 |
| 医学影像 | 数据审计 | [Auditing Capsule Vision 2024: Within-Split Train-to-Validation Re-Exposure and a Kvasir-Channel Sensitivity Diagnostic](cards-0002.md#paper-139763) | 对视频帧基准按来源视频溯源去重。 |
| 学习理论 | 复现诊断 | [Auditing Closed-Loop Learning in Recurrent Neural Networks: Reproduction, Robustness, and Generalization](cards-0002.md#paper-157025) | 分别衡量闭环训练中的短暂损失峰、最终损失和耦合稳定性。 |
| 统计学习 | 共形校准 | [Auditing Conformal Prediction for Language Models Under Inference-Time Model Shift](cards-0002.md#paper-138875) | 按真实量化与温度配置做覆盖验收。 |
| 医学影像 | 集成诊断 | [Auditing Correlated Failures in Frozen-Feature Pretrained-Encoder Pools for Medical Segmentation](cards-0002.md#paper-138982) | 用病例级误差相关检查骨干是否真的互补。 |
| 多语言学习 | 水印评测 | [Auditing Cross-Lingual Fairness in Language Model Watermarking](cards-0002.md#paper-138923) | 对不同语言分别校准阈值并测阈值无关区分度。 |
| 科研计量 | 证据审计 | [Auditing Evidence Framing at NeurIPS: A Decade-Scale Study of Accepted Papers](cards-0002.md#paper-139236) | 对会议证据风格的时间趋势按主题调整。 |
| 隐私评测 | 表征审计 | [Auditing Privacy Leakage in Tabular Foundation Model Embeddings](cards-0002.md#paper-149397) | 共享嵌入前评估辅助信息存在时的联合泄漏。 |
| 科研可靠性 | 防御审计 | [Auditing Sabotage Bench: A Benchmark for Detecting and Fixing Research Sabotage in ML Codebases](cards-0002.md#paper-139641) | 在科研复现中分别验收检测和修复。 |
| 表征学习 | 部署评测 | [Auditing Single-Query Recoverability in Self-Supervised Representations](cards-0002.md#paper-152886) | 单输入系统按单输入验收。 |
| 大语言模型 | 评审校准 | [Auditing the Judge: Human-Grounded Bias Discovery, Quantification, and Mitigation in LLM Judges](cards-0002.md#paper-153728) | 用人机分歧发现偏差，再用受控改写测量偏差。 |
| 大语言模型 | 身份核验 | [Auditor-Assisted Summary-Channel Verification for Hosted LLM Identity Substitution](cards-0002.md#paper-154384) | 以公开推理摘要作为托管模型身份的审计信号。 |
| 计算机视觉 | 输入增强 | [AuGhostmentation: The Eyes Never Stand Still—$\textit{Why Should CNNs?}$](cards-0002.md#paper-152194) | 将弱位移副本叠到原图增强扰动鲁棒性。 |
| 医学影像 | 几何等变 | [Augmented Equivariant Mesh Networks for Anatomical Segmentation](cards-0002.md#paper-153175) | 分别评估网格在标准位姿和旋转扰动下的分割。 |
| 强化学习 | 约束优化 | [Augmented Lagrangian Method for Last-Iterate Convergence for Constrained MDPs](cards-0002.md#paper-155499) | 单策略部署时检验最终迭代收敛。 |
| 优化 | 局部学习 | [Augmented Lagrangian Predictive Coding](cards-0002.md#paper-154623) | 用逐层对偶变量累积预测约束误差。 |
| 统计学习 | 最优传输 | [A Unified Approach for Computing Wasserstein Barycenters of Discrete and Continuous Measures](cards-0002.md#paper-154277) | 混合点云和密度输入时使用统一的重心求解。 |
| 多模态学习 | 音频标记化 | [A Unified Audio Language Model with Text-Aligned Factorized Audio Tokenization](cards-0002.md#paper-154205) | 将语言可表达信息与波形保真信息分开编码。 |
| 隐私 | 风险界 | [A Unified Framework for Adversary-Aware Differential Privacy Bounds](cards-0002.md#paper-153636) | 评估差分隐私时将无输出时的先验成功率纳入比较。 |
| 计算机视觉 | 条件生成 | [A Unified Framework for Image-to-3D Part Generation via Variable Granularity](cards-0002.md#paper-150141) | 在单模型内比较点、框和掩码三种控制。 |
| 机制设计 | 资源分配 | [A Unified Framework for Uniform-Price Resource Allocation Mechanisms](cards-0002.md#paper-154380) | 采用比例式分配时比较统一价格规则。 |
| 图学习 | 跨域对齐 | [A Unified Graph Language Model for Multi-Domain Multi-Task Graph Alignment Instruction Tuning](cards-0002.md#paper-148900) | 按图数据和指令的对齐难度组织训练。 |
| 多模态学习 | 时空编码 | [A Unified Image and Video Encoder for Multimodal LLMs](cards-0002.md#paper-154993) | 把低层时序建模前移到视觉编码器。 |
| 优化 | 学习率迁移 | [A Unified Merge Calculus for Learning-Rate Scaling on Neural Computation Graphs](cards-0002.md#paper-152315) | 按计算图合并方式而非只按深度迁移学习率。 |
| 统计学习 | 结构约束 | [A Unified Neural Architecture for Variable-Wise Shape Constraints](cards-0002.md#paper-149870) | 用结构保证逐变量单调性或曲率。 |
| 图学习 | 域适应 | [A unified pairwise distribution matching framework for graph domain adaptation under structure shift](cards-0002.md#paper-154823) | 边结构变化时对齐连接节点对的分布。 |
| 评测 | 稳健性审计 | [A Unified Perturbation Framework for Analyzing Leaderboard Stability and Manipulation](cards-0002.md#paper-148880) | 给成对偏好排行榜同时报告名次集合、全序和置信区间稳定性。 |
| 优化 | 稀疏求解 | [A Unified Semismooth Newton Approach to Multitask and Multivariate Square-Root Lasso Problems](cards-0002.md#paper-151762) | 多响应平方根 Lasso 用降维半光滑牛顿法。 |
| 多模态 | 目标函数 | [A Unified Spectral Theory of Multimodal Losses](cards-0002.md#paper-155760) | 单侧噪声重时优先检验定向生成 |
| 学习理论 | 上下文学习 | [A Unified Theoretical Framework for Task Recognition and Task Learning in In-Context Learning](cards-0002.md#paper-149830) | 按任务频率分组测提示长度收益 |
| 图学习 | 不确定性 | [A Unified Uncertainty Representation for Graph Neural Networks via Doubly-Spectral Stochastic Expansion](cards-0002.md#paper-151405) | 共享随机嵌入并为校准与 OOD 分设读出 |
| 可解释性 | 组合表示 | [A Unifying Perspective on Language Model Interpretability](cards-0002.md#paper-148396) | 用共同的张量积假设交叉检验探针与干预 |
| 优化 | 算子正则 | [A Unifying View of Anchoring via Operator-Side Tikhonov Regularization](cards-0002.md#paper-153667) | 在算子查询端加入消失的正则以复用原更新 |
| 视觉 / Agent | 闭环工具 | [AURA: An Autonomous Retouching Agent with Photographic Visual Thinking](cards-0002.md#paper-148451) | 长程编辑每步回读图像再决定局部工具操作 |
| 视频生成 | 结构化控制 | [Auteur: Language-Driven Cinematographic Framing for Human-Centric Video Generation](cards-0002.md#paper-155137) | 用相对演员的镜头语言生成关键帧 |
| 大语言模型 | 数据管线评测 | [AutoDataBench: How Far Are LLM Agents from Autonomously Engineering Post-Training Data Pipelines?](cards-0002.md#paper-139001) | 固定学生模型，以训练后的效果检验数据管线 |
| Agent | 离线记忆 | [Auto-Dreamer: Learning Offline Memory Consolidation for Language Agents](cards-0002.md#paper-152534) | 把即时记忆采集和跨会话压缩拆成两个阶段 |
| 计算机视觉 | 标注迁移 | [AutoExpert: Automating 3D LiDAR Annotation from Expert-Crafted Guidelines](cards-0002.md#paper-139399) | 把专家标注规范作为少样本跨模态评测输入 |
| 信息检索 | 多跳推理 | [Autofocus Retrieval: An Effective Pipeline for Multi-Hop Question Answering With Semi-Structured Knowledge](cards-0002.md#paper-156757) | 先提取关系约束，再逐步扩大候选范围 |
| AI 安全 | 防御评测 | [AutoHoney: Automating, Deploying, and Evaluating Scheming Honeypots Across Production Codebases](cards-0002.md#paper-139153) | 分开测任务范围和评测知情状态对审计结果的影响 |
| 可视分析 | 算法选型 | [AutoManifold: Agentic Design of Data Visualisation Algorithms via Manifold Embedding](cards-0002.md#paper-154589) | 按用户的结构保留目标评测嵌入算法 |
| Agent | 故障检测 | [Automata from Agent Traces: Failure and Next-Step Prediction](cards-0002.md#paper-148996) | 跨轨迹建有限状态机并监控各状态失败信号 |
| 因果推断 | 方法搜索 | [Automated Causal Effect Estimation through Self-Evolving AI](cards-0002.md#paper-150563) | 有代理回报时分别评估代理和真实效应误差 |
| 数据质量 | 标注诊断 | [Automated Hypothesis Discovery for Characterizing Annotation Disagreement](cards-0002.md#paper-139723) | 留出验证用于筛选生成的分歧假设 |
| 优化 | 核设计 | [Automated Kernel Discovery Towards Understanding High-dimensional Bayesian Optimization](cards-0002.md#paper-149210) | 用留一概率评分选核并分离数学提案和实现 |
| 优化 / Agent | 经验记忆 | [Automated Reformulation of Robust Optimization via Memory-Augmented Large Language Models](cards-0002.md#paper-148230) | 把失败推导整理成可跨底座移植的重写经验 |
| 软件工程 | 规则优化 | [Automatically Refining Coding Rules for AI Coding Agents](cards-0002.md#paper-153609) | 用留出功能测试筛选自动变异的编程规则 |
| 强化学习 | 约束优化 | [Automatic Constraint Policy Optimization based on Continuous Constraint Interpolation Framework for Offline Reinforcement Learning](cards-0002.md#paper-151401) | 用验证反馈自调离线策略约束类型。 |
| Agent / 科学机器学习 | 研究评测 | [Automating ML for Science: Can Frontier Agents Climb Scientific Hills in the Wild?](cards-0002.md#paper-139352) | 区分智能体的工程调参与领域创新。 |
| Agent | 记忆学习 | [AUTOMEM: Automated Learning of Memory as a Cognitive Skill](cards-0002.md#paper-150660) | 把文件记忆决策与任务动作分开优化。 |
| 多模态 | 状态评测 | [Automotive-ENV: Benchmarking Multimodal Models in Automotive Cockpit Environments](cards-0002.md#paper-139849) | 用环境状态验收 GUI 行为。 |
| Agent | 持续适配 | [Autonomous Continual Learning for Environment Adaptation of Computer-Use Agents](cards-0002.md#paper-154225) | 用上一轮反馈生成贴近当前能力的课程。 |
| 科学机器学习 | 假设检验 | [Autonomous Scientific Discovery via Iterative Meta-Reflection](cards-0002.md#paper-149249) | 将已验证的发现作为下一轮假设生成输入。 |
| 计算机视觉 | 动态表征 | [Autoregressive Appearance Prediction for 3D Gaussian Avatars](cards-0002.md#paper-154526) | 用历史外观隐状态解释同姿态不同外观。 |
| Agent | 离线评估 | [Autoregressive Diffusion World Models for Off-Policy Evaluation of LLM Agents](cards-0002.md#paper-153481) | 让目标策略在每个模拟转移后重新行动。 |
| 学习理论 | 自回归估计 | [Autoregressive Learning in Joint KL: Sharp Oracle Bounds and Lower Bounds](cards-0002.md#paper-154406) | 用联合 KL 区分错设近似与序列估计误差。 |
| 多模态 | 奖励分解 | [Auto-Rubric as Reward: From Implicit Preference to Explicit Generative Criteria](cards-0002.md#paper-151565) | 比较输出前先生成任务特定的质量细则。 |
| Agent | 执行迭代 | [AutoSaddler: Automatic Harness Optimization with Durable Updates from Agent Execution Traces](cards-0002.md#paper-151256) | 用留出任务检验从失败轨迹提出的配置修订。 |
| Agent | 协作管理 | [AutoScientists: Self-Organizing Agent Teams for Long-Running Scientific Experimentation](cards-0002.md#paper-151734) | 在固定预算下比较共享实验状态和固定中央分工。 |
| 数学推理 | 数据合成 | [AuxGeoAgent: Synthesizing Challenging Geometry Proving Data via Planning and Symbolic Deduction](cards-0002.md#paper-139298) | 按是否需要辅助构造定向生成练习。 |
| 多模态 | 强化学习 | [Auxiliary Clues Aware’s Geometry Problem Solving](cards-0002.md#paper-149037) | 按图形线索对证明推理的贡献加权。 |
| 多模态 | 编辑评测 | [AVENUE: Audio-Video Editing Understanding and Evaluation](cards-0002.md#paper-138887) | 逐样本记录目标改动及应保留模态。 |
| 脑科学 | 混杂控制 | [AVID: A 5T fMRI Dataset for Benchmarking Auditory-induced Visual Mental Imagery Decoding](cards-0002.md#paper-139564) | 用听觉诱发想象控制视觉刺激混杂。 |
| 多模态 | 传感融合 | [AVI-HT: Adaptive Vision-IMU Fusion for 3D Hand Tracking](cards-0002.md#paper-154518) | 遮挡条件下按传感器动态调节可信度。 |
| 多模态 | 推理预算 | [AVIS: Adaptive Test-Time Scaling for Vision–Language Models](cards-0002.md#paper-150182) | 联合分配视觉 token 和推理采样次数。 |
| Agent / 系统 | 进化搜索 | [AVO: Agentic Variation Operators for Autonomous Evolutionary Search](cards-0002.md#paper-153311) | 让变异算子访问谱系和执行反馈。 |
| 多模态学习 | 令牌压缩 | [AVOC: Enhancing Hour-Level Audio-Video Understanding in Omni-Modal LLMs via Retrieval-Inspired Token Compression](cards-0002.md#paper-154191) | 按相关性、重要性和多样性选择长视频令牌。 |
| 图学习 | 拓扑学习 | [Avoiding Feature Collapse in Graph ODEs via Hysteretic Topology Evolution](cards-0002.md#paper-150833) | 需要长期保留差异时改变有效边支持。 |
| AI 对齐 | 监督协议 | [Avoiding Obfuscation with Prover-Estimator Debate](cards-0002.md#paper-148404) | 审查递归辩论双方的计算负担。 |
| 大语言模型 | 自蒸馏 | [AVSD: Adaptive-View Self-Distillation by Balancing Consensus and Teacher-Specific Privileged Signals](cards-0002.md#paper-150780) | 用跨教师视图共识确定更新方向。 |
| 医学影像 | 表征预训练 | [A World Model of Radiologist Reading for Medical Image Representation Learning](cards-0002.md#paper-154476) | 把专家扫视顺序作为训练监督。 |
| 计算机视觉 | 推理剪枝 | [AWP: Activation-based Window Pruning for Gigapixel Object Detection](cards-0002.md#paper-151192) | 先测 FFN 激活均值能否无训练地选窗。 |
| 强化学习 | 多智能体分解 | [Axiomatic Reinforcement Learning for Open Multi-Agent Systems from Shapley Axioms](cards-0002.md#paper-148243) | 以合作博弈公理约束开放队伍的个体值。 |
| 大语言模型 / 科学推理 | 奖励设计 | [Axiomatic World Modeling for Physics Reasoning](cards-0002.md#paper-150823) | 给物理前提建模和求解过程分别评分。 |
| 优化 / 系统 | 并行求解 | [B$^3$-PWL: GPU-Batched Branch-and-Bound for Piecewise-Linear Optimization with SOS2 Constraints](cards-0002.md#paper-150051) | 批量求解分支定界中的松弛子问题。 |
| 优化 | 梯度估计 | [B2P-Corr: Batch-to-Population Gradient Estimators for Non-Decomposable Correlation Losses](cards-0002.md#paper-154786) | 对相关系数损失维护跨批矩统计量。 |
| Agent / 世界模型 | 在线模型修订 | [Baba in Wonderland: Online Self-Supervised Dynamics Discovery for Executable World Models](cards-0002.md#paper-150860) | 把更新后丢失的旧转移用作反例。 |
| 学习理论 / 评测 | 观察式归纳 | [BabyTheorist: A Benchmark for Learning to Theorize the World from Observation Alone](cards-0002.md#paper-139168) | 测试从未标组的持续观测里归纳可复用规则。 |
| 科学机器学习 | 动态图估计 | [BACE: Behavior-Adaptive Connectivity Estimation from Multi-Region Neural Recordings](cards-0002.md#paper-151970) | 用行为条件图预测神经活动并检查边稳定性。 |
| 生成模型 / 评测 | 异常检测 | [Backbone-Equated Diffusion OOD via Sparse Internal Snapshots](cards-0002.md#paper-154161) | 在匹配骨干和测试成本后检查单次内部快照。 |
| 模型安全 | 防御评测 | [Backdoor Attacks Rerouted: BatchNorm as a Sink for Adversarial Signals](cards-0002.md#paper-155957) | 单独检验可疑模型的归一化统计及防御效果。 |
| 模型安全 | 适配器净化 | [Backdoor Purification for LoRA-Tuned LLMs via Null-Space Projection](cards-0002.md#paper-153189) | 在隔离验证环境检查可疑适配器的净化与技能保留。 |
| 大语言模型 | 多目标偏好 | [Back to Blackwell: Closing the Loop on Intransitivity in Multi-Objective Preference Fine-Tuning](cards-0002.md#paper-148405) | 当偏好循环时保留多目标判据。 |
| 语言模型 | 推理搜索 | [Backtracking with Linear-in-Depth Search-Space Growth: Width-Limited Tree Search for Large Language Models](cards-0002.md#paper-155253) | 同预算比较有无回溯及宽度约束 |
| 优化 | 多任务学习 | [Balanced Multi-Task Learning from an Optimality-Gap Perspective](cards-0002.md#paper-153699) | 比较损失尺度与局部改进上限两种归一化 |
| 生成模型 | 频谱损失 | [Balancing Frequencies and Pixels in Flow Matching](cards-0002.md#paper-151310) | 分别消融频谱监督和阶段切换 |
| 生成模型 | 分层编码 | [Balancing Image Compression and Generation with Bootstrapped Tokenization](cards-0002.md#paper-155939) | 固定 token 预算对照分层与混合编码 |
| 视觉 | 自监督表征 | [BAL: Bidirectional Autoregression in Latent Space for Learning Human Movement Representations](cards-0002.md#paper-152565) | 分别消融双向训练与局部目标 |
| 多模态 | 奖励设计 | [BalCapRL : A Balanced Framework for RL-Based MLLM Image Captioning](cards-0002.md#paper-149366) | 分别测长度、忠实性和表达后再调组合奖励 |
| Agent | 模型路由 | [Ballad: Bandit-Based LLM Routing for Automated Heuristic Discovery](cards-0002.md#paper-154569) | 同预算对照均值路由与谱系信用 |
| 语言模型 | 信用分配 | [BALTO: Balanced Token-Level Policy Optimization for Hallucination Mitigation](cards-0002.md#paper-150212) | 在混合正误回答中对照局部和整段奖励 |
| 强化学习 | 在线表示 | [Bandits via Additive Quantized Representations](cards-0002.md#paper-155168) | 固定内存比较原特征及分级量化表示 |
| Agent | 评测 | [BankerToolBench: Evaluating AI Agents in End-to-End Investment Banking Workflows](cards-0002.md#paper-139094) | 分别统计单产物错误与跨文档矛盾 |
| 视觉 | 少样本分割 | [BAPM: Boundary-Aware Prompt Mining for Training-Free Few-Shot Medical Image Segmentation](cards-0002.md#paper-155064) | 同预算比较随机负提示和可信边界负提示 |
| 语言模型 | 安全控制 | [BarrierSteer: LLM Safety via Learning Barrier Steering](cards-0002.md#paper-148333) | 联合测量漏判、误拒与任务质量 |
| 视觉 | 连续控制 | [Barycentric Guidance: Turning Foundation Image Editors into Continuous Affective Controllers](cards-0002.md#paper-153096) | 用控制平面全域误差替代少量端点测试 |
| 推荐 / 语言模型 | 持续适配 | [Base Items Overfit, New Items Underfit: Hidden Cost of Joint Training in Incremental Adaptation](cards-0002.md#paper-156066) | 绘制旧新质量随训练时长变化的独立曲线 |
| 视觉 | 长尾学习 | [BasicLT: Basic-Level Abstraction and Selective Differentiation for Long-Tailed Recognition](cards-0002.md#paper-150159) | 按类频率和粗类置信分组测细化收益 |
| 科学机器学习 | 摊销推断 | [BASIL-DCM: Biophysical Amortized Scalable Inference for Latent Dynamic Causal Modeling](cards-0002.md#paper-152400) | 用前向谱一致性验证摊销生成参数 |
| 深度学习 | 注意力参数化 | [Basis-Mediated Bilinear Attention: A New Method for Greatly Reducing Query--Key Pathway Parameters](cards-0002.md#paper-154941) | 同预算比较共享基、完全共享和独立低秩 |
| 语言模型 | 推理解码 | [BASTION: Budget-Aware Speculative Decoding with Tree-structured Block Diffusion Drafting](cards-0002.md#paper-151263) | 相同草稿下比较固定及自适应预算 |
| 视觉 | 流式重建 | [BAT3R: Robust Online 3D Reconstruction with Bayesian Adaptive State Updates](cards-0002.md#paper-153286) | 分开测历史区域保护及新场景更新 |
| 视觉 | 几何细化 | [BA-T: An Iterative Transformer for Two-View Bundle Adjustment](cards-0002.md#paper-148295) | 同延迟比较重复几何层和加深解码器 |
| 多模态 | 测试时适配 | [Batch-Conditioned Semantic Anchors for Robust Transductive Adaptation of Vision--Language Models](cards-0002.md#paper-154091) | 按批次可靠性移动语义锚点 |
| 学习理论 | 受限通信 | [Batched Stochastic Linear Bandits with 1-Bit Communication Constraints](cards-0002.md#paper-150229) | 将批反馈位预算单列为遗憾项 |
| 多模态 | 联合生成 | [Baton: Explicit Semantic Blueprints for Joint Video-Audio Generation](cards-0002.md#paper-153708) | 去噪前对齐关键帧级音视频计划 |
| 鲁棒学习 | 蒸馏 | [BayesAT: Bayes-Guided Progressive Distillation for Semi-Supervised Adversarial Training](cards-0002.md#paper-150593) | 按学习阶段提高教师标签温度 |
| 统计学习 | 分布回归 | [Bayesian Additive Distribution Regression](cards-0002.md#paper-152064) | 用浅树先验表达分布值输入的低维边际 |
| 统计学习 | 不确定性估计 | [Bayesian Backprop as Belief Propagation: Single-Pass Predictive Uncertainty](cards-0002.md#paper-154383) | 用单次矩传播代替重复采样推理 |
| 因果推断 | 实验设计 | [Bayesian Causal Experimental Design for CATE Estimation under Noncompliance](cards-0002.md#paper-154028) | 以处理效应的信息增益挑选鼓励实验 |
| 因果推断 | 敏感性分析 | [Bayesian Causal Stress Testing: Posterior Fragility of Treatment-Effect Conclusions](cards-0002.md#paper-155177) | 分别报告后验区间和推翻主张的最小扰动 |
| 决策理论 | 专家反馈 | [Bayesian Decision Making around Experts](cards-0002.md#paper-149882) | 用单位更新预算的信息价值选择专家或自身数据 |
| 优化 | 函数空间搜索 | [Bayesian Optimization on Function Spaces via Sparse RKHS Manifolds](cards-0002.md#paper-150567) | 在稀疏核表示中直接优化函数 |
| 优化 | 信赖域 | [Bayesian Optimization with Fisher Information Geometry: Gradient Bounds and Trust-Region Methods](cards-0002.md#paper-156134) | 用代理后验局部敏感度设置搜索尺度 |
| 大语言模型 | 奖励适配 | [Bayesian Preference Learning for Test-Time Steerable Reward Models](cards-0002.md#paper-150486) | 通过示例更新潜在偏好以调节奖励模型 |
| 大语言模型 | 测试时搜索 | [Bayesian Test-Time Inference of Task-Aligned Similarity from Weak Interactive Feedback](cards-0002.md#paper-152715) | 根据少量反馈动态推断当前任务的相似性轴 |
| 评测 | 评判校准 | [BayesJudge: Uncertainty-Aware Bayesian Meta-Evaluation of Human and LLM Judgments](cards-0002.md#paper-138918) | 保留平局并交换候选次序以测位置偏差 |
| 统计学习 | 评测上限 | [Bayes-Optimal BER and AUC: Estimation and Evaluation of Estimators](cards-0002.md#paper-152377) | 类别失衡时估计最优 BER 或 AUC 而非准确率上限 |
| 联邦学习 | 持续学习 | [Bayes-pFCL:Bayesian Personalized Federated Continual Learning](cards-0002.md#paper-149379) | 分别量化任务更新和聚合造成的知识漂移 |
| 多模态 | 检索增强 | [BayesRAG: Probabilistic Mutual Evidence Corroboration for Multimodal Retrieval-Augmented Generation](cards-0002.md#paper-154974) | 用语义与版面互证重排图文组合 |
| Agent | 协作诊断 | [Bayes-Sufficient Compression Is Not Enough: How Communication Helps in Multi-Agent Systems?](cards-0002.md#paper-155601) | 比较压缩消息、原始上下文和不通信 |
| Agent / 优化 | 基准诊断 | [BBOWP-Bench: Evaluating LLMs on Black-Box Optimization Word Problems](cards-0002.md#paper-139160) | 分别验收黑箱优化的搜索空间构造和算法选择 |
| 统计学习 | 因果推断 | [B-CALM: Bias-Limited Bayesian Borrowing for RCT-Anchored Treatment Effects under Covariate Mismatch](cards-0002.md#paper-155646) | 用偏差先验限制外部数据借用。 |
| 大语言模型 | 模型融合 | [BDC-Merge: Cross-Architecture Model Merging via Dependency Alignment](cards-0002.md#paper-151593) | 用非线性依赖对齐异构模型。 |
| 具身智能 | 域适应 | [BEACON: Cross-Domain Co-Training of Generative Robot Policies via Best-Effort Adaptation](cards-0002.md#paper-151303) | 按样本差异学习源示范权重。 |
| Agent / 教育 | 行为模拟 | [BEAGLE: Behavior-Enforced Agent for Grounded Learner Emulation](cards-0002.md#paper-155338) | 把策略决策与执行生成分开，保留模拟学习者错误。 |
| 多模态学习 | 分层评测 | [BEAKER: An Expert-Curated Benchmark for Embodied Brains in Self-Driving Chemical Laboratories](cards-0002.md#paper-139293) | 分别评估识别状态与判断动作可执行性。 |
| 图学习 | 子图搜索 | [BeamWitness: Rooted Subgraph Beam Search for Selective Graph Representation Learning](cards-0002.md#paper-149610) | 预测前显式搜索有限数量的连通证据子图。 |
| 科学机器学习 | 三维表征 | [BEAST3D: animal behavioral analysis and neural encoding from multi-view video via Gaussian splatting](cards-0002.md#paper-149762) | 已知标定时用留出视角渲染预训练行为表征。 |
| Agent / 数据库 | 运行合规评测 | [Be CARE-ful with Text-to-SQL Benchmarks](cards-0002.md#paper-139633) | 将查询正确性与并发、权限、完整性和效率分开验收。 |
| 生成模型 | 流匹配 | [Beckmann Transport Models: From Autonomous Flows to One-Step Maps](cards-0002.md#paper-154577) | 在低维目标分布条件下比较自治流与直接一步映射。 |
| 强化学习 | 部分可观测控制 | [BECON: Belief-Conditioned Constrained Multi-Objective Reinforcement Learning under Drifting Preferences and Budgets](cards-0002.md#paper-153172) | 按不确定性融合推断的任务偏好与外部信号。 |
| 多模态学习 | 表征诊断 | [Before It Fades: Reinforcing Temporal Representations at Inference Time in VideoLLMs](cards-0002.md#paper-155460) | 用反转帧序定位时间信号衰减并在推理期补回。 |
| 多模态学习 | 分层评测 | [Before Words, Beyond Speech: Evaluating Nonverbal Social Reasoning in Early Childhood](cards-0002.md#paper-139741) | 把社会推理拆成情景、行为和人际关系层级。 |
| 大语言模型 | 后训练诊断 | [Behaving Better, Thinking Worse: Sycophancy Across Post-Training Stages](cards-0002.md#paper-153819) | 联合比较生成翻转率与同样本预测概率。 |
| 强化学习 | 行为搜索 | [Behavioral Foundation Models for Quality Diversity](cards-0002.md#paper-148386) | 在预训练行为潜空间内做质量多样性搜索。 |
| 计算机视觉 | 表征对齐 | [Behavioral Geometric Supervision Aligns Video Foundation Models with Human Social Perception](cards-0002.md#paper-149277) | 用人类视频相似性判断监督局部和全局嵌入几何。 |
| Agent | 信息流诊断 | [Behavioral Probes for Information Flow in LLM Swarms](cards-0002.md#paper-149644) | 用外部依赖与参数知识依赖辅助智能体结构选择。 |
| 个性化建模 | 离线评测 | [BehaviorBench: Modeling Real-World User Decisions from Behavioral Traces](cards-0002.md#paper-138919) | 将用户信念推断与下一步动作预测分别测量。 |
| 模仿学习 | 蒸馏理论 | [Behavior Cloning is Not All You Need: The Optimality of On-Policy Distillation for Noisy Expert Feedback](cards-0002.md#paper-150673) | 有噪教师下优先验证学生访问状态上的在线蒸馏。 |
| 强化学习 | 奖励鲁棒性 | [Behavior-Discriminative Reward Shaping for Reward-Robust Reinforcement Learning](cards-0002.md#paper-155941) | 按策略排序等价类定义奖励不确定集。 |
| 多模态学习 | 强化后训练 | [Behavior Pack Optimization for Video MLLM Post-Training](cards-0002.md#paper-150981) | 把同一视频问题的反事实视图作为联合奖励单位。 |
| 表情分析 | 多任务优化 | [Behaviour4All: A Dependency-Aware Toolkit for in-the-wild Facial Behaviour Analysis](cards-0002.md#paper-150818) | 用任务依赖约束部分标注联合训练 |
| Agent | 状态更新 | [Belief Engine: Configurable Stance Dynamics for Multi-Agent LLM Deliberation](cards-0002.md#paper-151258) | 让立场变化受显式证据吸收与先验锚定控制 |
| 强化学习 | 收缩性分析 | [Bellman Contraction under MMD: A Unified Framework](cards-0002.md#paper-150640) | 用差分核条件检验分布式 Bellman 更新的收缩 |
| 大语言模型 | 防御评测 | [BELLS-O: Evaluating the Operational Trade-offs of LLM Supervision Systems](cards-0002.md#paper-139421) | 采购监督模型时联测检出、误报、成本和延迟 |
| Agent | 评估偏差 | [Below the Reliability Floor: Recovering True Success from Judge-Gated Loops](cards-0002.md#paper-156773) | 重试门控后独立抽取金标准验证真实成功率 |
| 大语言模型 | 表示诊断 | [Benchmark for Assessing Olfactory Perception of Large Language Models](cards-0002.md#paper-139778) | 对同一问题比较名称输入和结构输入 |
| 大语言模型 | 基准审计 | [Benchmark Health Index: A Systematic Framework for Benchmarking the Benchmarks of LLMs](cards-0002.md#paper-138960) | 区分基准的辨别力、饱和余量和实际采用 |
| 大语言模型 | 防御监测 | [Benchmarking and Improving Monitors for Out-Of-Distribution Alignment Failure in LLMs](cards-0002.md#paper-139423) | 将安全分类与分布外报警独立融合 |
| 多模态学习 | 结构生成 | [Benchmarking and Optimizing Multimodal Structured Generation: The OracleGraph Dataset and PRISM Framework](cards-0002.md#paper-149901) | 用图级诊断向自蒸馏教师提供结构错误信息 |
| 表格学习 | 算子选型 | [Benchmarking Attention for Tabular Foundation Models](cards-0002.md#paper-139839) | 按行列注意力形状分别选择计算后端 |
| 科学机器学习 | 泛化评估 | [Benchmarking Compositional Generalisation for Machine Learning Interatomic Potentials](cards-0002.md#paper-139491) | 以组合留出代替只做随机样本划分 |
| 具身多模态 | 评测分解 | [Benchmarking Fine-Grained Spatio-Temporal Awareness in Embodied Brain Models](cards-0002.md#paper-139463) | 单独评估语义理解与时空定位 |
| 图学习 | 基准复核 | [Benchmarking Graph Self-Supervised Learning for Node-Level Tasks: Insights and Strong Baseline](cards-0002.md#paper-138872) | 公平调参后再决定采用生成式或对比式预训练 |
| 大语言模型 | 隐私审计 | [Benchmarking Membership Privacy Risks in Preference-Based LLM Post-Training](cards-0002.md#paper-139392) | 按完整偏好记录衡量隐私风险 |
| 多模态学习 | 视觉推理评测 | [Benchmarking Multimodal Mathematical Reasoning with Explicit Visual Dependency](cards-0002.md#paper-139044) | 用多图显式依赖检查何时真的需要视觉 |
| Agent | 协作评测 | [Benchmarking Open-Ended Multi-Agent Coordination in Language Agents](cards-0002.md#paper-139589) | 用可控协作难度区分个人生存和团队协调 |
| 大语言模型 | 行为评估 | [Benchmarking Risk Attitudes of LLMs](cards-0002.md#paper-139608) | 在相同感知风险下比较模型采取的动作 |
| 时序预测 | 故障评测 | [Benchmarking Sensor-Fault Robustness in Forecasting](cards-0002.md#paper-138912) | 单独比较干净精度与故障最坏误差。 |
| 科学机器学习 | 基准诊断 | [Benchmarking sequence-to-ensemble predictors on UNICORNEdb, a UniProt-grouped database of PDB-derived conformational ensembles](cards-0002.md#paper-138904) | 按同一实体配对观测，避免相似样本差异混入状态变化。 |
| 大语言模型 | 领域评测 | [Benchmarking Vietnamese Legal Knowledge of Large Language Models](cards-0002.md#paper-139241) | 按法条层级和认知难度分层构造评测。 |
| Agent | 部署审计 | [Benchmark Recovery Does Not Certify a Frozen Tool-Trigger Contract After Quantization](cards-0002.md#paper-155241) | 量化验收时固定工具权限与参考标签，再单独检查触发。 |
| 大语言模型 | 基准诊断 | [Benchmarks Are Not Atomic: Composition-Aware LLM Evaluation using BenchHub](cards-0002.md#paper-139267) | 用属性分布匹配应用后再比较模型。 |
| 统计学习 | 测量可靠性 | [Benchmarks as Measurement Instruments: Quantifying Signal and Noise for More Efficient AI Evaluations Under Distribution Shift](cards-0002.md#paper-139555) | 按目标模型群体估计题目对排名的测量价值。 |
| 大语言模型 | 数据消融 | [Benchmark Shadows: How Data Regimes Shape Parameter Footprints and Generalization](cards-0002.md#paper-154989) | 把重复和频率集中分开，对照后续多样数据能否修复。 |
| 多智能体学习 | 实验设计 | [Bench-MFG: A Benchmark Suite for Learning in Stationary Mean Field Games](cards-0002.md#paper-139725) | 按耦合类型分层生成随机博弈实例。 |
| 科学机器学习 | 诊断评测 | [BenchRep-T: A Systematic Evaluation of T-Cell Repertoire-Based Disease Diagnostics](cards-0002.md#paper-139621) | 在诊断模型选型中同时控制测序深度和人口统计混杂。 |
| 大语言模型 | 防御验收 | [Benign Reinforcement Learning Can Amplify Latent Backdoors](cards-0002.md#paper-149677) | 在强化学习后重新进行安全回归测试。 |
| 统计学习 | 序贯推断 | [Bentkus-type asymptotic e-values](cards-0002.md#paper-155963) | 需要较紧的事后区间时对照 Bentkus 型 e 值。 |
| 多模态学习 | 生成架构 | [Bernini: Latent Semantic Planning for Video Diffusion](cards-0002.md#paper-154106) | 用视觉语义潜变量作为规划器和视频渲染器的接口。 |
| 生成模型 | 快速采样 | [Bernoulli Flow Models: Self-Consistent Generative Modeling for Binary Data](cards-0002.md#paper-155986) | 二值扩散跳步时使用与间隔一致的后验。 |
| 科学机器学习 | 表征诊断 | [BESS-Bench: Benchmarking Spectral Representations for Be-Star Variability](cards-0002.md#paper-139851) | 分别用形态探测和下一观测预测选时序模型。 |
| 强化学习 | 纯探索 | [Best Arm Identification for Bandits with Shifting Means](cards-0002.md#paper-153746) | 奖励存在共同漂移时用重要性加权取代固定均值停止检验。 |
| 强化学习 | 主动查询 | [Best Arm Identification in Generalized Linear Bandits via Hybrid Feedback](cards-0002.md#paper-151037) | 把单臂绝对观测和成对比较纳入同一查询设计。 |
| 生成模型 | 推理引导 | [Best-of-$N$ Guidance for Test-time Diffusion Alignment](cards-0002.md#paper-154666) | 并行去噪过程中用当前优选粒子引导其余样本。 |
| 统计学习 | 序贯检验 | [Bet Imaginatively, not Historically in Independent-Data Sequential Testing](cards-0002.md#paper-155229) | 独立同分布假设成立时，用重排历史估计下注收益。 |
| 大语言模型 | 架构诊断 | [Better Language Models Require Better Domain-Specific Inductive Biases](cards-0002.md#paper-140098) | 激活函数搜索后加跨领域移植对照。 |
| 生成模型 | 流匹配 | [Better Source, Better Flow: Learning Condition-Dependent Source Distribution for Flow Matching](cards-0002.md#paper-148679) | 学习条件源分布 |
| 科学机器学习 | 高分辨率表示 | [Beyond 3 Million Tokens: A Multi-Modal Foundation Model for Full-Resolution Heliophysics](cards-0002.md#paper-152539) | 保留掩码区域的压缩频率视图 |
| Agent | 诊断评测 | [Beyond Accuracy: A Diagnostic Benchmark for Hypothesis-Driven Experiment Planning in LLM Agents](cards-0002.md#paper-139344) | 拆分实验规划各环节评测 |
| 大语言模型 | 压缩 | [Beyond Adjacent Layers: Graph-Guided Layer Fusion for Compressing Large Language Models](cards-0002.md#paper-152044) | 按全层相似性选保留层 |
| 具身智能 | 行为校准 | [Beyond Appearance Shifts: Task-Semantic Action Calibration for VLA Models](cards-0002.md#paper-150087) | 分别测任务保持和任务改变后的动作 |
| 多模态学习 | 数据审计 | [Beyond a Single Score: An Audit of Aesthetic Evaluation in Text-to-Image Pipelines Across Subcultural Visual Languages](cards-0002.md#paper-139303) | 按风格报告审美过滤保留率 |
| 学习理论 | 专家路由 | [Beyond Augmented-Action Surrogates for Multi-Expert Learning-to-Defer](cards-0002.md#paper-148942) | 解耦类别与各专家的训练头 |
| 优化 | 域泛化 | [Beyond Average Flatness: Domain-wise Flatness for Domain Generalization](cards-0002.md#paper-150477) | 按域测尖锐度并约束域间不平衡 |
| 多模态学习 | 组合评测 | [Beyond Bag-of-Words: Diagnosing Compositional Binding Failures in Vision-Language Models](cards-0002.md#paper-139620) | 配对最小场景和真实上下文 |
| 计算机视觉 | 来源标识 | [Beyond Bit Matching: Orthogonal Watermarks for Collusion-Resistant Image Fingerprinting](cards-0002.md#paper-148565) | 按检测误报约束设计图像指纹 |
| 优化 | 随机优化 | [Beyond Bounded Variance: Variance-Reduced Normalized Methods for Nonconvex Optimization under Blum-Gladyshev Noise](cards-0002.md#paper-150036) | 根据噪声增长和光滑性选择归一化更新 |
| 具身智能 | 地图评测 | [Beyond Chamfer Distance: Granular Order-aware Evaluation Metric For Online Mapping](cards-0002.md#paper-139462) | 区分折线排序、定位和检出 |
| 强化学习 | 策略优化 | [Beyond Clipping: Signed Logarithmic Smoothing for Policy Optimization](cards-0002.md#paper-153088) | 平滑整个重要性加权优势而非只截断比率 |
| 大语言模型 | 置信校准 | [Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in LLMs](cards-0002.md#paper-149177) | 按任务类型选择自评维度 |
| 可视化 | 降维 | [Beyond Contraction: Geometry-Faithful Supervised Dimensionality Reduction for Data Visualization](cards-0002.md#paper-155065) | 优先正则读出平滑并约束邻域扭曲 |
| 图学习 | 结构编码 | [Beyond Coordinates: Encoding Graph Structure via Contextual Distribution and Relational Similarity](cards-0002.md#paper-148246) | 使用上下文分布和相似核表示局部结构 |
| 视频生成 | 诊断评测 | [Beyond Copy-Paste: How Well Do Subject-Driven Video Models Understand Their Subjects?](cards-0002.md#paper-152728) | 用未见同主体目标检验身份保持 |
| 大语言模型 | 后训练 | [Beyond Correctness: Robustness-Driven Evolutionary Self-Training for Large Language Models](cards-0002.md#paper-151953) | 按推理轨迹的扰动稳健性筛选正确答案 |
| 具身智能 | 表征预训练 | [Beyond Data Scaling: Representation-Centric Pre-training for Vision-Language-Action Models](cards-0002.md#paper-155956) | 共享跨本体动作监督并允许下游换头 |
| 大语言模型 / 多模态 | 参数高效适配 | [Beyond Decoupled PEFT: Geometry-Aware Low-Rank Adaptation via Riemannian Reparameterization](cards-0002.md#paper-153695) | 把低秩方向预算限定在权重方向的切空间 |
| 强化学习 | 课程学习 | [Beyond difficulties: Insights for provably efficient design of autocurriculum in RLVR](cards-0002.md#paper-149187) | 按训练收益而非当前成功率选题 |
| 视觉生成 | 蒸馏 | [Beyond Distribution Matching: Self-Supervised Representation Forcing for Few-Step Video Generation](cards-0002.md#paper-154363) | 在输出分布匹配外加入内部预测监督 |
| 智能体 | 技能迁移 | [Beyond Domains: Reusing Web Skills via Transferable Interaction Patterns](cards-0002.md#paper-152827) | 按页面布局结构复用正常交互技能 |
| 三维视觉 | 控制诊断 | [Beyond Downstream Scores: Controlled Diagnostics for Point-Cloud Self-Supervised Learning Evaluation](cards-0002.md#paper-139098) | 将预训练信号、可见几何和读出分别消融 |
| 科学机器学习 | 评测设计 | [Beyond Drug Discovery: The Nanotechnology Molecular Optimization (NMO) Benchmark](cards-0002.md#paper-139426) | 采用物理模拟检验代理分数能否代表科学效用 |
| 动力系统 | 相似性 | [Beyond DSA: Conjugacy-based Comparison of Dynamical Systems](cards-0002.md#paper-152248) | 将对齐约束为状态双射诱导的变换 |
| 表征学习 | 谱分析 | [Beyond Eigenfunctions: Divergence Principal Functions for Representation Learning](cards-0002.md#paper-153338) | 按训练散度选择低秩表示几何 |
| 可靠性 | 分布外评测 | [Beyond Empirical Support: Structured Outlier Generation via Sinkhorn Optimal Transport](cards-0002.md#paper-151741) | 在弱支持边界构造受语义约束的压力样本 |
| 多模态学习 | 组件消融 | [Beyond Encoder Accumulation: Measuring Encoder Roles in Multi-Encoder VLMs](cards-0002.md#paper-152266) | 重新训练编码器组合而非仅在固定权重上遮蔽 |
| 持续学习 | 记忆预算 | [Beyond Exemplar Selection: Value-Aware Memory Allocation in Replay-Based Continual Learning](cards-0002.md#paper-155700) | 在固定缓存中按类别效用调整配额 |
| 强化学习 | 风险规划 | [Beyond Expected Values: Risk-Sensitive Planning with Distributional Monte-Carlo Tree Search](cards-0002.md#paper-149403) | 在树边维护回报分布以评估嵌套尾部风险 |
| 三维视觉 | 结构先验 | [Beyond Family Labels: A Taxonomic Ornstein-Uhlenbeck Prior for Avian 3D Shape Recovery](cards-0002.md#paper-151996) | 用连续分类树距离替代同科二元标签 |
| 大语言模型 | 能力校准 | [Beyond Fixed Benchmarks and Worst-Case Attacks: Dynamic Boundary Evaluation for Language Models](cards-0002.md#paper-139552) | 用靠近模型能力边界的题估计可比较分数 |
| 多模态学习 | 长视频 | [Beyond Flat Frames: Hierarchical Graph Reasoning for Long Video Understanding](cards-0002.md#paper-152948) | 用事件图粗检索后再找关键帧 |
| 分布式学习 | 通信 | [Beyond Flat Gossip: Tiered Gossip Learning for Scalable Collaborative AI](cards-0002.md#paper-154579) | 将数据持有节点与高容量混合节点分层 |
| 图学习 | 层次生成 | [Beyond Flat Walks: Compositional Abstraction for Autoregressive Graph Generation](cards-0002.md#paper-152657) | 在复杂图上对照社区分解与平坦线性化 |
| 高效推理 | 静态部署 | [Beyond FLOPs: Train-Full, Deploy-Partial Multi-Exit Inference via Selective Lightweight IC Ensemble](cards-0002.md#paper-152802) | 使用校准后的静态截断替代逐样本动态退出 |
| 视觉表征 | 生成蒸馏 | [Beyond Generation: Unlocking Discriminative Representations from Diffusion Models](cards-0002.md#paper-150350) | 以生成的类 token 作为判别学习教师 |
| 多模态学习 | 组合对齐 | [Beyond Global Alignment: Structured Compositional Reasoning for Vision-Language Models](cards-0002.md#paper-155609) | 分开监督关系方向与属性的对象归属 |
| 大语言模型 | 评测诊断 | [Beyond Ground Truth: Evaluating Non-Verifiable Reasoning in LLMs through Moral Robustness](cards-0002.md#paper-154911) | 用多轮一致性评估价值判断。 |
| 多模态学习 | 区域对齐 | [Beyond Hard Negatives: Grounded Positive Supervision for Compositional CLIP](cards-0002.md#paper-150916) | 用结构化正例改善属性绑定。 |
| 大语言模型 | 模拟诊断 | [Beyond High and Low: Evaluating Graded Cognitive Diversity in LLM Persona Simulations](cards-0002.md#paper-138966) | 使用反思错误分布检验模拟人群。 |
| 学习理论 | 可识别性 | [Beyond ICA: Identifiability by Symmetry Breaking](cards-0002.md#paper-150471) | 用对称性条件判断潜表示能否恢复。 |
| 表格学习 | 基准诊断 | [Beyond IID: How General Are Tabular Foundation Models, Really?](cards-0002.md#paper-139490) | 选表格模型时分别检查时间、分组与 IID 划分。 |
| 统计学习 | 保形校准 | [Beyond Imputation: Mask-Adaptive Conformal Prediction via Tree Embeddings on General Missing Data Mechanisms](cards-0002.md#paper-154427) | 在缺失掩码层面检查覆盖率。 |
| 可解释性 | 组合搜索 | [Beyond Incremental Beam Search for Compositional Explanations of Neurons](cards-0002.md#paper-152763) | 避免按单个概念增量扩展时过早丢掉解释候选。 |
| 多模态学习 | 表征干预 | [Beyond Interpretability: When, Why, and How Sparse Autoencoders Enable Label-Free Visual Steering](cards-0002.md#paper-148658) | 用逐样本重建误差决定是否采用稀疏特征修正。 |
| 推荐系统 | 离线评测 | [Beyond IPS: Reliable Counterfactual Evaluation in Multi-Stage Ad Systems without Logged Propensities](cards-0002.md#paper-151796) | 无记录倾向时对直接奖励估计做目标分布校正。 |
| 时序学习 | 训练数据剪枝 | [Beyond Isolation: Neighbor-Consistent Data Pruning for Multivariate Time Series Forecasting](cards-0002.md#paper-154771) | 用重叠窗口的损失轨迹一致性诊断异常样本。 |
| 自监督学习 | 表征几何 | [Beyond Isotropy in JEPAs: Hamiltonian Geometry and Symplectic Prediction](cards-0002.md#paper-149858) | 通过跨视图预测耦合注入结构先验。 |
| 统计学习 | 排序聚合 | [Beyond Kemeny Medians: Consensus Ranking Distributions. Definition, Properties and Statistical Learning](cards-0002.md#paper-149736) | 用多个局部共识代表有分群的排序分布。 |
| 概率建模 | 采样 | [Beyond Langevin: Sampling Multimodal Densities using the Witten Laplacian on 1-forms](cards-0002.md#paper-155804) | 区分跨模态路径探索和盆地内采样。 |
| 大语言模型 | 表征控制 | [Beyond Linear Activation Steering: Invertible Latent Transformations for Controlling LLM Behavior](cards-0002.md#paper-148807) | 对照固定方向和随输入变化的潜空间干预。 |
| 时序学习 | 专家路由 | [Beyond Linear Decoders: Dynamic Expert-Coupled Optimal Decoding for Time Series Forecasting](cards-0002.md#paper-153816) | 依据变量动态选择预测解码专家。 |
| Agent | 故障归因 | [Beyond LLM-Based Reasoning: Lightweight GNNs for Agent Failure Attribution](cards-0002.md#paper-149719) | 用轻量轨迹图替代长文本故障归因。 |
| 图学习 | 分数阶扩散 | [Beyond Local Neighborhoods: Fractional Diffusion with Levy Flights on Simplicial Complexes for Link Prediction](cards-0002.md#paper-148623) | 需要跨远距离高阶关系时测试单纯形上的非局部扩散。 |
| 大语言模型 | 微调路由 | [Beyond LoRA vs. Full Fine-Tuning: Gradient-Guided Optimizer Routing for LLM Adaptation](cards-0002.md#paper-154880) | 在优化器层动态分配低秩和全量更新。 |
| 神经形态计算 | 频率选择 | [Beyond Low-Pass Dynamics: Frequency-Selective Spiking Reservoirs with Resonant Neurons](cards-0002.md#paper-148662) | 用异构共振单元辨别不同时标。 |
| 统计学习 | 局部校准 | [Beyond Marginal Coverage: Efficient Localized Conformal Prediction via Residual Rank Calibration](cards-0002.md#paper-153265) | 用标准化残差的局部秩代替逐查询的加权分位数。 |
| 系统效率 | 稀疏算子 | [Beyond Masked Sparsity: SNACK Enables Truly Sparse Neural Networks on GPU](cards-0002.md#paper-150469) | 高稀疏度时改用真正稀疏的前后向 |
| 统计学习 | 参数估计 | [Beyond Maximum Likelihood: Variational Inequality Estimation for Generalized Linear Models](cards-0002.md#paper-152448) | 对非标准链接用变分不等式估计 |
| 视觉 | 逆问题 | [Beyond MMSE: Enhancing PnP Restoration with ProxiMAP](cards-0002.md#paper-151995) | 使残余噪声匹配去噪器训练噪声 |
| 量子学习 | 表征诊断 | [Beyond MNIST: Limitations of Amplitude Encoding on Quantum Classification](cards-0002.md#paper-150197) | 诊断编码集中后再投入训练 |
| 多模态 | 模型融合 | [Beyond Modality Fusion: Deep Ensembles for Multimodal Classification](cards-0002.md#paper-155113) | 等参数比较单模态集成和特征融合 |
| 信号处理 | 结构保真 | [Beyond MSE: Differentiable Complexity Priors for Structure-Preserving Neural Denoising](cards-0002.md#paper-153782) | 用复杂度一致性监督去噪 |
| 图学习 | 离散扩散 | [Beyond Node Sequences: Relational Diffusion for Unified Graph Learning](cards-0002.md#paper-148255) | 以边为基本生成单位 |
| 视觉 | 异常检测 | [Beyond Normal References: Discriminative Few-Shot Anomaly Detection](cards-0002.md#paper-153262) | 将异常参考用于学习偏离正常的方向 |
| 强化学习 | 先验诊断 | [Beyond One-Size-Fits-All: Diagnosis-Driven Online Reinforcement Learning with Offline Priors](cards-0002.md#paper-140053) | 用在线证据决定何时削弱离线先验 |
| Agent | 过程奖励 | [Beyond Outcome Rewards: Process-Aware Optimization for Search Agents](cards-0002.md#paper-148305) | 按结果和当前证据调整搜索奖励 |
| Agent | 自蒸馏 | [Beyond Outcome Rewards: Step-Level Self-Distilled Policy Optimization for Deep Search Agents](cards-0002.md#paper-154780) | 只在失败轨迹上按步骤调整优势幅度 |
| 大语言模型 | 提示优化 | [Beyond Outcome: Trajectory-Driven Prompt Optimization via Multi-Dimensional Rewards](cards-0002.md#paper-150285) | 监督反思过程的一致性 |
| 图学习 | 传播诊断 | [Beyond Oversquashing: Understanding Signal Propagation in GNNs Via Observables](cards-0002.md#paper-154868) | 测特定源到目标区域的信号输运 |
| 大语言模型 | 偏好优化 | [Beyond Pairs: Your Language Model is Secretly Optimizing a Preference Graph](cards-0002.md#paper-150929) | 按偏好图聚合多样本，平局不给梯度 |
| 联邦学习 | 行为蒸馏 | [Beyond Parameter Aggregation: Semantic Consensus for Federated Fine-Tuning of LLMs](cards-0002.md#paper-155550) | 异构客户端共享行为语义而非参数 |
| 大语言模型 | 模型合并 | [Beyond Parameter Arithmetic: Sparse Complementary Fusion for Distribution-Aware Model Merging](cards-0002.md#paper-149097) | 合并时跟踪终止和重复异常 |
| 强化学习 | 离线博弈 | [Beyond Pessimism: Offline Learning in KL-regularized Games](cards-0002.md#paper-153617) | 在 KL 正则下检验是否需要悲观估计 |
| 视觉 | 扩散采样 | [Beyond Pixel Space: Frequency-Domain Uncertainty Estimation for Structure-Aware Diffusion Guidance](cards-0002.md#paper-152220) | 在频域估计不确定性并引导去噪 |
| 视觉 | 边界监督 | [Beyond Pixel-wise Supervision: Local Structure Regularization for Semantic Segmentation](cards-0002.md#paper-154585) | 监督语义概率的局部结构强度与方向 |
| Agent | 世界模型 | [Beyond Prediction: Steering VLM Agents with Retrospective World Modeling](cards-0002.md#paper-155042) | 用逆向解释一致性作为过渡奖励 |
| 可解释性 | 人机评测 | [Beyond Proxy Metrics: MLLM-Based Human Surrogate Evaluation for Explainable AI](cards-0002.md#paper-152905) | 按解释用途选择指标并校验模型代评 |
| Agent | 记忆检索 | [Beyond RAG for Agent Memory: Retrieval by Decoupling and Aggregation](cards-0002.md#paper-150607) | 先拆出区分性事实再聚合 |
| 大语言模型 | 联邦检索 | [Beyond Raw Context Transfer: Representation-based Federated Retrieval-Augmented Generation](cards-0002.md#paper-150023) | 比较跨站点表征与原文交换 |
| 自动驾驶 | 记忆表征 | [Beyond Raw Observations: Distilling and Storing Invariant Driving Memories for Generalizable Autonomous Driving](cards-0002.md#paper-152198) | 检索决策相关不变量 |
| 计算机视觉 | 图像取证 | [Beyond Real or Fake: A Dual-Channel Authenticity and Reasoning Protocol for Photographic Assessment](cards-0002.md#paper-154533) | 分别审计相机指纹和内容一致性 |
| 大语言模型 | 社会推理评测 | [Beyond Right and Wrong: Evaluating Second-order Social Reasoning in Large Language Models](cards-0002.md#paper-139315) | 将规范识别与观察者反应分开测试 |
| 多模态学习 | 安全数据 | [Beyond Risky Activities: Bridging the Supervision Gap for Situational Risk Reasoning](cards-0002.md#paper-139234) | 构造同一行为在不同场景的风险对照 |
| 计算机视觉 | 立体校正 | [Beyond Row Alignment: Virtual-Camera-Aware Online Stereo Rectification](cards-0002.md#paper-151291) | 用深度可用性评价在线校正 |
| 多模态学习 | 属性监督 | [Beyond Scalar Distances: Semantic Attribute Gradients from Frozen MLLMs for Visual Embeddings](cards-0002.md#paper-153671) | 从成对图像的属性判断学习检索表征 |
| 计算机视觉 | 视频分割 | [Beyond [SEG] Tokens: Training-Free Video Reasoning Segmentation via Counterfactual Inference  and Contrastive Concept](cards-0002.md#paper-154601) | 先离散选择实例再跟踪 |
| 多模态学习 | 视觉压缩 | [Beyond Selection: Token Parameterization for Extreme Visual Token Compression](cards-0002.md#paper-151663) | 将基底截断与坐标组织独立设计 |
| 自动驾驶 | 基准诊断 | [Beyond Self-Play and Scale: A Behavior Benchmark for Generalization in Autonomous Driving](cards-0002.md#paper-139295) | 将训练模拟器表现与标准规划基准分开验证 |
| 统计学习 | 概率融合 | [Beyond Semantic Alignment: Geometric Incomparability in Multi-Oracle Soft Fusion](cards-0002.md#paper-149809) | 先校准概率几何再做软融合 |
| Agent | 检索 | [Beyond Semantic Similarity: Rethinking Retrieval for Agentic Search via Direct Corpus Interaction](cards-0002.md#paper-155649) | 允许检索策略根据中间证据调整查询操作 |
| 学习理论 | 推理诊断 | [Beyond Semantics: The Unreasonable Effectiveness of Reasonless Intermediate Tokens](cards-0002.md#paper-156774) | 单独区分中间计算支架与可读语义的贡献 |
| 多模态学习 | 后训练 | [Beyond SFT-to-RL: Pre-alignment via Black-box On-policy Distillation for Multimodal RL](cards-0002.md#paper-153111) | 在监督微调和强化学习间加入分布对齐 |
| 多模态学习 | 空间先验 | [Beyond Single Expert: Harmonizing Diverse Visual Priors in MLLMs for Spatial Understanding](cards-0002.md#paper-150326) | 按任务融合互补视觉先验 |
| 计算机视觉 | 扩散推理 | [Beyond Single-Shot Conditioning: Test-Time Condition Refinement for Diffusion-Based Image Restoration](cards-0002.md#paper-153799) | 在推理期间更新视觉条件 |
| 科学机器学习 | 动力学建模 | [Beyond Single-Step Likelihood: Gibbs Variational Last Layers for Long-Horizon Dynamics Learning](cards-0002.md#paper-152213) | 用多步损失训练贝叶斯末层 |
| 医学影像 / 多模态 | 弱监督对齐 | [Beyond Sparse Captions: Aligning Slide-Level Text and Patch-Level Vision in Pathology](cards-0002.md#paper-149751) | 用切片级报告查询局部图像特征 |
| 计算机视觉 | 密集匹配 | [Beyond Spatial and Temporal Priors: A Generalizable Approach for Dense Correspondence Matching](cards-0002.md#paper-149352) | 以身份一致性学习非物理连续的对应关系 |
| 多模态学习 | 表征约束 | [Beyond Spatial-Domain Supervision: A Relation Constrained Space for Multi-Modal Image Fusion](cards-0002.md#paper-150788) | 在关系空间监督融合 |
| 医学影像 | 半监督学习 | [Beyond Stabilization: Dual-EMA Teachers for Global–Local Semantic Learning in Semi-Supervised Medical Image Segmentation](cards-0002.md#paper-153534) | 用两种 EMA 时间尺度分别监督整体和局部 |
| 大语言模型 | 推理干预 | [Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention](cards-0002.md#paper-155564) | 比较激活上的固定向量与概念条件动态变换 |
| 大语言模型 | 参数高效微调 | [Beyond Structural Agnosticism: Stable-Rank-Guided LoRA for Structure-Aware Fine-Tuning](cards-0002.md#paper-151865) | 按层谱结构与任务梯度分配低秩容量 |
| 强化学习 | 评测诊断 | [Beyond Success Rates: Trainability and Extractability in Offline GCRL](cards-0002.md#paper-139429) | 以超参数景观比较策略提取的鲁棒性 |
| Agent | 在线监控 | [Beyond Suspicious Steps: Ontological Trust in Long-Horizon Agents](cards-0002.md#paper-152482) | 检查长程前缀是否仍符合授权任务 |
| Agent | 能力诊断 | [Beyond Task Success: Probing Cognitive Primitives in Web Agents](cards-0002.md#paper-139465) | 用配对任务隔离规划和探索能力 |
| 生成模型 | 强化微调 | [Beyond the Dirac Delta: Mitigating Diversity Collapse in Reinforcement Fine-Tuning for Image Generation](cards-0002.md#paper-155487) | 在固定对齐要求下显式评估多样性 |
| 推荐系统 | 稳健性评测 | [Beyond the Full Slate: Evaluating MNL Algorithms on All Slates](cards-0002.md#paper-149458) | 按实际小候选集而非全库误差选模型 |
| 图学习 | 双向蒸馏 | [Beyond the Golden Teacher: Enhancing Graph Learning through LLM-GNN Co-teaching](cards-0002.md#paper-150344) | 让文本和图模型互教并追踪何时由冲突转为一致 |
| 信号处理 | 连续稀疏分解 | [Beyond the Grid: Continuous Dictionary Pursuit for Interpretable Signal Decomposition](cards-0002.md#paper-151808) | 在连续参数空间拟合可解释信号原子 |
| 在线优化 | 公平分配 | [Beyond the Half Approximation: Fair and Efficient Online Class Matching](cards-0002.md#paper-153402) | 按阈值在类别公平和匹配效率之间切换 |
| 多模态学习 | 表征诊断 | [Beyond the Linear Separability Ceiling: Aligning Representations in VLMs](cards-0002.md#paper-156758) | 用线性探针区分视觉表示不足和读出失败 |
| 机器学习系统 | 并行策略 | [Beyond the Node Barrier: Zero-Shot Strategy Planning for LLM Training on Super-Nodes](cards-0002.md#paper-149841) | 在高速互连平台重新评估跨节点张量和专家并行 |
| 大语言模型 | 防护检测 | [Beyond the Prompt: Leveraging Pre-Decoding States for Jailbreak Detection in dLLMs](cards-0002.md#paper-151177) | 用扩散解码前的响应表征补充输入风险检测 |
| 时间序列 | 表示学习 | [Beyond the Readout: Reservoir State Statistics for Model-Space Learning under Sparse Observations](cards-0002.md#paper-152483) | 用动态轨迹统计补充稀疏通道的拟合参数 |
| 统计学习 | 偏移风险估计 | [Beyond the Training Distribution: Evaluating Predictions Under Distribution Shift and Selection Bias](cards-0002.md#paper-149001) | 同时校正目标协变量偏移和选择性标签 |
| 机器学习系统 | 分布式训练调参 | [Beyond the Trial-and-Error Loop: Hybrid Projection and Automated Tuning for Distributed Training](cards-0002.md#paper-150603) | 先用小规模测量和全局推演筛训练配置 |
| 具身智能 | 空间先验 | [Beyond Thinking: Imagining in 360$^\circ$ for Humanoid Visual Search](cards-0002.md#paper-149744) | 用多假设空间布局引导主动搜索。 |
| 多模态 | 时空定位 | [Beyond Token Representations: Explicit Visual Object Grounding for Video Reasoning Segmentation](cards-0002.md#paper-155293) | 将分割目标明确为框和点，并跨查询校准。 |
| 生成模型 | 蒸馏 | [Beyond Trajectory Matching: Reflow with Marginal Distribution Alignment](cards-0002.md#paper-155442) | 沿每段蒸馏轨迹同时约束终点边际。 |
| 大语言模型 | 行为评测 | [Beyond Truthfulness: Evaluating Honesty in Large Language Models](cards-0002.md#paper-139425) | 将模型知道正确答案和是否如实表达分开计分。 |
| 计算机视觉 | 可控恢复 | [Beyond Unidirectional: Unsupervised Trajectory Learning for Omnidirectional Controllable Underwater Image Enhancement](cards-0002.md#paper-151882) | 训练任意源目标强度间的相对变换。 |
| 大语言模型 | 检索校验 | [Beyond Uniform Detection: Adaptive Hallucination Detection for RAG Across Response Regimes](cards-0002.md#paper-155755) | 按回答类型切换幻觉检测信号。 |
| 科学机器学习 | 守恒动力学 | [Beyond Unit-Circle Eigenvalues: Invariant Bases for Stable State Space Dynamics](cards-0002.md#paper-149242) | 同时约束特征值和守恒量对应的模态基底。 |
| 多模态 | 视频检索 | [Beyond Visual Boundaries: Rethinking Scene Segmentation for Movie RAG](cards-0002.md#paper-139396) | 按叙事事件切分电影检索单元。 |
| 医学影像 | 密集表征 | [Beyond ViT Tokens: Masked-Diffusion Pretrained Convolutional Pathology Foundation Model for Cell-Level Dense Prediction](cards-0002.md#paper-148943) | 需要像素级连续性时比较卷积掩蔽扩散与 patch 预训练。 |
| 学习理论 | 推理预算 | [Beyond What Seems Necessary: Hidden Gains from Scaling Training-Time Reasoning Length under Outcome Supervision](cards-0002.md#paper-151533) | 用分布外验证决定训练推理长度。 |
| 具身智能 | 动作表征 | [Beyond World-Frame Action Heads: Motion-Centric Action Frames for Vision-Language-Action Models](cards-0002.md#paper-155672) | 先在学习的运动局部坐标中组装动作。 |
| 优化 | 数据压缩 | [Beyond Worst-Case Coreset Bounds for $k$-Clustering via Determinantal Sampling](cards-0002.md#paper-148163) | 自然分布假设成立时比较行列式采样构造聚类核心集。 |
| 生理信号 | 连续表征 | [B[FM]$^2$: Brain Foundation Model via Flow Matching with SplitUNet](cards-0002.md#paper-148190) | 按时间和电极轴分别卷积，只沿时间下采样。 |
| 大语言模型 | 强化学习 | [BFS-PO: Best-First Search for Large Reasoning Models](cards-0002.md#paper-153193) | 训练时将最短正确分支作为优先探索对象。 |
| Agent | 运维编排 | [Bian Que: An Agentic Framework with Flexible Skill Arrangement for Online System Operations](cards-0002.md#paper-148501) | 将事件相关数据和知识选择封装为可修订技能。 |
| 计算机视觉 | 检测审计 | [BIAS-ID: A Framework for Analyzing Transformation Biases in AI-Generated Image Detectors](cards-0002.md#paper-139597) | 分开评估变换偏差与一般鲁棒性。 |
| 图学习 | 误差诊断 | [Bias, Measurement Error, and Double-Dipping: When Can GNN Convolutions Help Brain Connectome Prediction?](cards-0002.md#paper-153204) | 用独立估计图与同样本图对照检查重复使用测量噪声。 |
| 大语言模型 | 偏好优化 | [Bias-Variance Optimized Preference Optimization for Large Reasoning Models](cards-0002.md#paper-152470) | 把普通推理梯度与空推理分支梯度混合降方差。 |
| 优化 | 层级代理 | [Bidirectional Information Flow (BIF) - A Sample Efficient Hierarchical Gaussian Process for Bayesian Optimization](cards-0002.md#paper-149175) | 用父子双向反馈拟合组合目标 |
| 生成模型 | 稀疏注意力 | [Bidirectional Sparse Attention for Faster Video Diffusion Training](cards-0002.md#paper-154292) | 同时筛查询和键值 |
| 科学机器学习 | 多解建模 | [Bifurcation Models: Learning Set-Valued Solution Maps with Weight-Tied Dynamics](cards-0002.md#paper-149009) | 用吸引子集合表示多个正确解 |
| 计算机视觉 | 大图生成 | [BigCell: Generating Gigapixel Whole-Slide Images](cards-0002.md#paper-152972) | 按区域重要性调度滑窗生成 |
| 生成模型 | 记忆诊断 | [Bigger Isn't Always Memorizing: Early Stopping Overparameterized Diffusion Models](cards-0002.md#paper-156775) | 数据规模变化后重新校准早停点 |
| 计算机视觉 | 稀疏检测 | [BiHashFormer: Hash-Driven Dual-Branch Transformer for Efficient Object Detection in HRW Shots](cards-0002.md#paper-152107) | 用快速补偿支路覆盖主检测器遗漏 |
| 大语言模型 | 数据加权 | [Bilevel Optimization of Synthetic Trajectories for Multi-Turn LLM Fine-Tuning](cards-0002.md#paper-155173) | 用真实验证任务学习合成轨迹权重 |
| 机器人学 | 定位 | [BiLi: Bridging the Last Mile in LiDAR Localization](cards-0002.md#paper-153081) | 将地图流形约束与时序蒸馏结合 |
| 学习理论 | 在线匹配 | [Bilinear Matching Bandits](cards-0002.md#paper-149557) | 利用双线性结构设计分行探索 |
| 大语言模型 | 低比特推理 | [BiLoCo: Binary Low-Rank Corrections for LLM FP4 Decode](cards-0002.md#paper-149418) | 用符号低秩残差和主矩阵乘并行 |
| 多模态学习 | 离散扩散 | [BiMoGen: Bidirectional Motion-Text Generation via Unified Masked Discrete Diffusion](cards-0002.md#paper-152019) | 训练时暴露自身预测并在早期纠错 |
| 统计学习 | 结构表示 | [Binary Regression:  Universal Ising Model, Binary Expansion and Beyond](cards-0002.md#paper-155424) | 以辅助二值变量表示高阶依赖 |
| 多模态学习 | 表征对齐 | [Binding Multiple Modalities via Multimodal Wasserstein Barycenter](cards-0002.md#paper-149098) | 用跨模态重心作为对齐中心 |
| 多模态学习 | 视觉推理 | [Binding Visual Features Point by Point](cards-0002.md#paper-148298) | 让模型先指向对象再判断其属性 |
| 科学机器学习 | 结构正则化 | [Biological Graph Priors Enable Representation Learning for Cellular Microscopy](cards-0002.md#paper-150999) | 用已知关系约束显微图像表征 |
| 多模态学习 | 域适应 | [Biomedical Acquisition-induced Style Shifts as Mixture Shifts: Style-aware Mixture-of-Experts Multimodal Prompt Learning](cards-0002.md#paper-152391) | 将设备风格偏移当成潜在成分比例变化 |
| 科学机器学习 | 图像质量验证 | [BioMicroAgents: A Co-evolutionary Multi-Agent Framework for High-Fidelity Biomicroscopy Imaging](cards-0002.md#paper-155868) | 用独立验证阶段检查增强是否保留结构 |
| 安全评测 | 级联验证 | [BioSafetyBench: Agentic Cascade Evaluation for the Bio-AI Ecosystem](cards-0002.md#paper-138924) | 用独立评估器核对中间产物与下游风险 |
| Agent | 能力评测 | [BioXArena: Benchmarking LLM Agents on Multi-Modal Biomedical Machine Learning Tasks](cards-0002.md#paper-138952) | 固定骨干和资源再比较代理框架 |
| Agent | 强化学习 | [BIRD-RL: Scaling Agentic Reinforcement Learning over Stateful Data-Centric Environments](cards-0002.md#paper-152242) | 复用数据库副本时保证轨迹状态隔离 |
| 视觉 | 三维重建 | [Birth-Death Structural Learning for 3D Gaussian Splatting](cards-0002.md#paper-155061) | 用重建损失的一阶变化选增删原语 |
| 安全 | 防护验证 | [BiShield-TEE: On the (In-)Security of Unilateral Weight Obfuscation in On-Device TEE-Shielded LLM Partition](cards-0002.md#paper-152920) | 对可信执行环境的参数隔离做独立验证 |
| 视觉 | 生成建模 | [BitDance: Scaling Autoregressive Generative Models with Binary Tokens](cards-0002.md#paper-153956) | 用扩散预测高容量二值视觉码而非枚举类别 |
| 语言模型 | 推理加速 | [BitMTP: When Multi-Token Prediction Meets Low-Bit Large Language Models](cards-0002.md#paper-154757) | 将接受前缀同时对齐缓存与执行图复用 |
| Agent | 学习理论 | [Bits Beat Tokens: A Regret Rate Distortion Theory for Large Language Model Agents](cards-0002.md#paper-150556) | 用决策相关信息量衡量上下文而非长度 |
| 模型架构 | 脉冲网络 | [BitShift-RoPE: Zero-FLOP Relative Positional Encoding for Spiking Neural Network Transformers](cards-0002.md#paper-150476) | 用整数循环移位实现相对位置编码 |
| 优化 | 零阶估计 | [Black-Box Followers, White-Box Leaders: Partial Zeroth-Order Methods for MPECs](cards-0002.md#paper-155774) | 仅对不可微的未知响应做零阶估计 |
| 统计学习 | 模型审计 | [Black-box model classification under the discriminative factorization](cards-0002.md#paper-154419) | 先估计查询集合的判别能力再分配审计预算 |
| 语言模型 | 不确定性量化 | [Black-Box Uncertainty Quantification for Large Language Models via Ensemble-of-Ensembles](cards-0002.md#paper-151082) | 比较同提示采样和语义等价改写的变异 |
| 语言模型 | 数据选择 | [BLADE: Scalable Bi-level Adaptive Data Selection for LLM Training](cards-0002.md#paper-152234) | 动态更新用于超额损失选择的参考模型 |
| 模型训练 | 局部学习 | [BLANP: Memory-Efficient Backpropagation-Free Local Training via Antithetic Node Perturbation](cards-0002.md#paper-155644) | 内存紧张时比较局部反向梯度与对偶扰动更新 |
| 视觉 | 三维动画 | [BLARM: Animating 3D Objects from Video via Blending LAtent Rigid Motion Primitives](cards-0002.md#paper-155225) | 将网格变形表示为共享刚体运动的混合 |
| 多模态 | 联邦学习 | [BLEND: Balancing Personalization vs. Generalization in Federated Vision–Language Models](cards-0002.md#paper-154470) | 将共享跨模态调节与客户端投影分开 |
| 科学机器学习 | 集合预报 | [BlendCast: Teaching Vision-Language Model to Anticipate Member Skill in Weather Ensembles](cards-0002.md#paper-149073) | 按变量和大气状态预估成员权重 |
| 多模态 | 可验证智能体 | [BlenderFORGE: Framework for Optimizing Reactive 3D-Graphics Editing Ability of MLLMs](cards-0002.md#paper-151100) | 按场景状态差异为3D编辑生成可验证奖励 |
| 科学机器学习 | 预报评测 | [Blind-Window Forecasting: Real-Time Benchmarking and Multimodal Reconstruction for Tropical Cyclones](cards-0002.md#paper-150222) | 按推理时真实可获得的时间戳构造预报测试 |
| 优化 | 块重采样 | [Blocked Gibbs meets Diffusion Transformers: Unsupervised Learning for Constraint Optimization](cards-0002.md#paper-148271) | 用退火块大小实现离散约束的局部大步修正 |
| 科学机器学习 | 逆问题 | [BlockFormer: Transformer-based inference from interaction maps](cards-0002.md#paper-153580) | 让交互图逆推模型兼容实体数量和大小变化 |
| 大语言模型 | 剪枝 | [Block-OBS-GS: Exact Per-Block Joint Brain Surgery with Gauss–Seidel Refinement for LLM Pruning](cards-0002.md#paper-152355) | 固定剪枝掩码后精确求块内权重并做跨块校正 |
| 强化学习 | 遗憾分析 | [Block Optimism for Nonstationary Bandits with Latent Linear Dynamics](cards-0002.md#paper-151108) | 潜状态受动作影响时按有限记忆块做乐观探索 |
| 大语言模型 | 强化学习后训练 | [Block-R1: Rethinking the Role of Block Size in Multi-domain Reinforcement Learning for Diffusion Large Language Models](cards-0002.md#paper-139480) | 训练扩散语言模型时按样本选 rollout 块大小 |
| 大语言模型 | 稀疏注意力 | [Block Sparse Flash Attention](cards-0002.md#paper-155122) | 在计算精确查询键分数后按块阈值省去低价值计算 |
| 高效机器学习 | 向量量化 | [Block Sphere Vector Quantization](cards-0002.md#paper-152314) | 根据重建或检索目标选择量化准则 |
| 高效机器学习 | 注意力求导 | [Block-Wise Differentiable Sinkhorn Attention: Tail-Refinement Gradients with a Gap-Aware Dustbin Bridge](cards-0002.md#paper-155973) | 只对迭代求解器的短精修尾部求导，以降低存储 |
| 计算机视觉 | 三维重建 | [Blur Issue Matters for Thermal Novel View Synthesis: A Floating Gaussian Suppression Approach](cards-0002.md#paper-148566) | 识别单通道成像中亮度和透明度相互补偿 |
| 大语言模型 | 注意力量化 | [BMAttn: Block-Aligned Mixed-Precision Attention Quantization for LLM Inference](cards-0002.md#paper-152092) | 分块分配精度以兼顾重要性和 GPU 规则访存 |
| 大语言模型 | 推理评测 | [BoardGameArena: A Multi-Dimensional Benchmark for Strategic Reasoning of LLMs in Board Games](cards-0002.md#paper-139541) | 分别测试合法走子和实际策略选择 |
| 优化 | 基准审计 | [BO-Arena: An Evolving Benchmark for High-Dimensional Bayesian Optimisation](cards-0002.md#paper-138938) | 用公共实现和简单 GP 对照检验高维优化新方法 |
| 可信机器学习 | 防御评测 | [BodyBench: Evaluating Adversarial Image Defenses Against AI Nudification Inpainting](cards-0002.md#paper-139845) | 以实际危害指标验证隐私防护 |
| 优化 | 稀疏决策 | [BONSAI: Bayesian Optimization with Natural Simplicity and Interpretability](cards-0002.md#paper-155059) | 在限制采集效用损失时尽量保留默认配置 |
| 神经科学 / 多模态 | 数据增强 | [Boosting Brain-to-Image Decoding with TRIBE v2 Data Augmentation](cards-0002.md#paper-154738) | 按数据来源调节合成与真实观测的训练配比 |
| 图学习 | 对比表征 | [Boosting Graph Contrastive Learning via Manifold-Guided Representation Disentanglement](cards-0002.md#paper-151362) | 对增强视图只在共享子空间约束一致性 |
| 大语言模型 | 递归推理 | [Boosting Inference with Guided Reasoning: Stochastic Exploration for Recursive Models](cards-0002.md#paper-149759) | 仅在停止头能区分好轨迹时用随机推理搜索 |
| 大语言模型 | 奖励塑形 | [Boosting LLM Reasoning via Human-Inspired Reward Shaping](cards-0002.md#paper-153592) | 错误阶段鼓励探索，成功后再惩罚冗长 |
| 强化学习 | 经验回放 | [Boosting Multiagent Reinforcement Learning at High Replay Ratios with Ensemble Reset](cards-0002.md#paper-149143) | 高回放比下监控休眠神经元并周期重置价值集成 |
| 强化学习 | 经验回放 | [Boosting Off-Policy RLVR with Data-Centric Replay](cards-0002.md#paper-154959) | 控制轨迹陈旧度 |
| 视觉生成 | 推理筛选 | [Boosting Text-to-Image Diffusion Models via Core Token Attention-Based Seed Selection](cards-0002.md#paper-152409) | 按早期注意力挑种子 |
| 统计学习 | 多重检验 | [BOOST: Power-Optimal Strong-FWER Testing for Block-Structured Multiplicity](cards-0002.md#paper-152078) | 按块分配检验预算 |
| 强化学习 | 课程设计 | [Boost Reasoning Evolution via Responsive Rollout Difficulty Manipulation](cards-0002.md#paper-154872) | 按单题成功率调整提示长度 |
| Agent | 开发环境 | [BootstrapAgent: Turning Repository Setup into Reusable Agent Knowledge](cards-0002.md#paper-151994) | 把安装与诊断记录为可冷启动复验的契约 |
| 强化学习 | 生成策略 | [Bootstrapped Bipartite Actor-Critic for Diffusion RL](cards-0002.md#paper-155139) | 用动作Q差为成对偏好加权 |
| 学习理论 | 偏好决策 | [Borda-Based Fair Multi-User Dueling Bandit in Tabular and Generalized Linear Settings](cards-0002.md#paper-155261) | 按用户Borda效用构建纳什福利 |
| 表征学习 | 压缩评测 | [Bottleneck Benchmark: Sequence Compression Under Controlled Difficulty and Fixed Latent Size](cards-0002.md#paper-139737) | 固定潜变量尺寸再扫任务难度 |
| 大语言模型 | 推理诊断 | [Boule or Baguette? A Study on Task Topology, Length Generalization, and the Benefit of Reasoning Trace](cards-0002.md#paper-151781) | 分开测证明深度和任务广度 |
| Agent | 工具链诊断 | [Boundary-Induced Forgetting in Large Language Model Tool Chains: Measuring Field-Routing Failures](cards-0002.md#paper-155598) | 按字段依赖测跨工具传播 |
| 表征学习 | 数据效率 | [Boundary Mass in Feature Space as a Label-Budget Diagnostic for Representations](cards-0002.md#paper-149689) | 测边界附近的特征质量判断标注需求 |
| 计算机视觉 | 渐进压缩 | [Bound-Conditioned Latent Inference for Progressive Image Compression](cards-0002.md#paper-149342) | 用已解码符号约束连续潜变量 |
| 计算成像 | 误差估计 | [Bounding Global and Local Compression Error of Signal Parameterizations](cards-0002.md#paper-148822) | 用不同压缩级预测之差估计误差 |
| 科学机器学习 | 外推诊断 | [Bounds on Extrapolation across Phase Transitions with Generalized Regression](cards-0002.md#paper-153578) | 用广义特征值问题估计跨相外推风险 |
| 多模态学习 | 视觉提示 | [BoxTuning: Object-Aware Visual Prompting for  Multimodal Model Fine-Tuning](cards-0002.md#paper-149433) | 在视频帧中直接绘制物体空间状态 |
| 大语言模型 | 量化微调 | [BQ-LoRA: Binary-Quantized Low-Rank Adapters as Implicit Regularizers for Parameter-Efficient Fine-Tuning](cards-0002.md#paper-149729) | 用二值适配器替代半精度适配器 |
| 多模态学习 | 缺失模态 | [BRACE: Bipolar Reference-Aware Calibration and Estimation for Incomplete Multimodal Learning](cards-0002.md#paper-150021) | 利用上下参考群判断修正方向 |
| 神经科学 | 语音解码 | [Brain2voice 2.0: High-performance voice synthesis brain-computer interface](cards-0002.md#paper-148803) | 联合监督连续声学、离散声学和音素 |
| 神经科学 | 证据监督 | [BrainCoT: A Multi-Task Zero-Shot Brain Signal Foundation Model with Neurometric-Anchored Chain-of-Thought Reasoning](cards-0002.md#paper-155614) | 将神经指标作为可核对的预测依据 |
| 神经科学 | 图注意力 | [Brain Economy-Aligned Graph Transformers](cards-0002.md#paper-153903) | 把结构成本注入连接而非节点 |
| 科学机器学习 | 评测 | [BrainEM: A Large-Scale and Diverse Benchmark for EM Neuron Segmentation in Connectomics](cards-0002.md#paper-139121) | 分开测目标域少量标注与纯跨源复用。 |
| 多模态学习 | 时频预训练 | [Brain-OF: An Omnifunctional Foundation Model for fMRI, EEG and MEG](cards-0002.md#paper-155505) | 共享专家与模态专属专家分工。 |
| 多模态学习 | 证据评测 | [BrainTRACE: Tracing Longitudinal, Multimodal, and Volumetric Evidence in Brain MRI Clinical Reasoning](cards-0002.md#paper-139162) | 把纵向综合结论拆为可核查的证据链。 |
| 科学机器学习 | 时序预测 | [BrainVista: Modeling Naturalistic Brain Dynamics as Multimodal Next-Token Prediction](cards-0002.md#paper-153166) | 把刺激输入对齐到预测查询，并切断未来信息。 |
| 多模态学习 | 迁移适配 | [BrainWhisperer: Leveraging Whisper for Speech Decoding in Neuroprosthetics](cards-0002.md#paper-155029) | 将会话漂移交给分层低秩投影。 |
| 科学机器学习 | 条件生成 | [BrainWorld: A Structural-Prior-Conditioned Generative Model for Whole-Brain 4D fMRI Dynamics](cards-0002.md#paper-155412) | 用受试者的静态结构条件约束动态生成。 |
| 大语言模型 | 形式化评测 | [BraveATA: Benchmarking Broad and Verifiable End-to-End Automated Theoretical Analysis of Large Language Models](cards-0002.md#paper-139549) | 拆测理论发现、建模和证明。 |
| 计算机视觉 | 生成 | [BRAVO: Bridge Matching for Autoregressive Video Generation](cards-0002.md#paper-148431) | 从上一帧出发学习相邻帧运输。 |
| 强化学习 | 信用分配 | [Breaking $\textit{Winner-Takes-All}$: Cooperative Policy Optimization Improves Diverse LLM Reasoning](cards-0002.md#paper-150356) | 按对有效解集合的边际贡献分奖励。 |
| 语音识别 | 鲁棒微调 | [Breaking Adversarial Transferability in Fine-Tuned Speech Recognition](cards-0002.md#paper-153915) | 部署前验证公开底座的风险是否残留在微调模型。 |
| 联邦学习 | 鲁棒聚合 | [Breaking BAD: Heterogeneous Byzantine-Robust Federated Learning via Gather and Scatter Scores](cards-0002.md#paper-148208) | 同时检查更新的局部聚集与整体离散。 |
| 统计学习 | 信息估计 | [Breaking Curse of Dimensionality for Mutual Information Estimation with Vine Copulas](cards-0002.md#paper-154130) | 依赖复杂时比较藤 copula 与神经互信息估计。 |
| 时序学习 | 自监督 | [Breaking feature collapse in self-supervised time series encoder](cards-0002.md#paper-155178) | 以表示空间约束补充掩码重建。 |
| 深度学习 | 稀疏微调 | [Breaking Information Islands in Sparse Tuning via Small-World Connectivity](cards-0002.md#paper-155451) | 相同参数预算下改善跨块连接。 |
| 多模态学习 | 量化 | [Breaking Modality Heterogeneity in Low-Bit Quantization for Large Vision-Language Models](cards-0002.md#paper-153382) | 将模态特有的离群通道分开校准。 |
| 科学机器学习 | 数据增强 | [Breaking Noise Shortcuts in Self-Supervised Learning via Noise-Aligned View Generation](cards-0002.md#paper-153415) | 对同图的两个自监督视图重采样独立噪声。 |
| 统计学习 | 联邦采样 | [Breaking the $\sqrt{d}$ Communication Barrier in Federated Sampling with Adaptive Hamiltonian Monte Carlo](cards-0002.md#paper-152679) | 按客户端偏移调整同步频率。 |
| 强化学习 | 梯度估计 | [Breaking the Bias Barrier in Concave Multi-Objective Reinforcement Learning](cards-0002.md#paper-154531) | 检查效用平滑性后决定是否用多层蒙特卡洛。 |
| 推理系统 | 稀疏注意力 | [Breaking the Exactness Barrier: Interleaved DeepSeek Sparse Attention for Efficient Long Context Reasoning](cards-0002.md#paper-154778) | 按设备交错切分上下文并用放宽的局部排名替代精确全局排名。 |
| 强化学习 | 动作搜索 | [Breaking the Grid: Distance-Guided Reinforcement Learning in Large Discrete Action Spaces](cards-0002.md#paper-151813) | 按动作距离抽样邻域而非遍历整个动作空间。 |
| 生成模型 | 多体生成 | [Breaking the Group Size Barrier: Parameter-Efficient Group Dance Generation with Chain-of-Dancers](cards-0002.md#paper-151566) | 冻结单体生成器，按个体顺序生成并聚合已生成同伴。 |
| 统计学习 | 隐私评测 | [Breaking the Quality–Privacy Tradeoff in Tabular Data Generation via In-Context Learning](cards-0002.md#paper-152928) | 小样本表格合成优先比较上下文适配和逐表训练。 |
| 多模态学习 | 时序信用分配 | [Breaking the Second Barrier: Sub-Second Timestamped Omni-Modal Captioning](cards-0002.md#paper-151142) | 分别给字幕结构片段分配语义与时间奖励。 |
| 生成模型 | 条件调度 | [Breaking the Static: Dynamic Text Conditioning for Diverse Image Generation](cards-0002.md#paper-152353) | 初段只保留低频语义，后段逐步恢复完整提示。 |
| 生成模型 | 专家路由 | [Breaking the Uniformity Trap: Scaling Video Diffusion Model via SplitMoE](cards-0002.md#paper-152515) | 视频 MoE 给语义专家与通用专家分工，避免强制全局均匀路由。 |
| 训练系统 | 优化器量化 | [BReD: Block Replay Dithering for Stable Low-Bit EMA Optimizer States](cards-0002.md#paper-150618) | 为反复量化的 EMA 状态控制舍入偏差与方差。 |
| 优化 | 分布稳健训练 | [Brenier Meets Adversarial Training: Optimal Transport Geometry for Robust Learning](cards-0002.md#paper-152709) | 用运输映射的循环单调性检查分布鲁棒目标。 |
| 生成模型 | 结构化解码 | [BrickAnything: Geometry-Conditioned Buildable Brick Generation with Structure-Aware Tokenization](cards-0002.md#paper-154364) | 用局部连接树替代仅按空间坐标排列的生成序列。 |
| 计算机视觉 | 成像恢复 | [Bricker to BRACE: A Bracket Exposure RAW Dataset and Restoration Model for Flicker-Banding](cards-0002.md#paper-149112) | 用包围曝光捕获条纹随曝光变化的特征。 |
| 计算机视觉 | 约束引导 | [BrickFlow: Connectivity-Guided Brick Reconstruction](cards-0002.md#paper-151991) | 推理时加解析连接场修正生成的部件位姿。 |
| 多模态学习 | 时序对齐 | [BRIDGE: Brain-Vision Representation Integration through Depth and Granularity Encoding](cards-0002.md#paper-155233) | 让视觉教师提供跨层表示，并分阶段池化脑信号。 |
| 生成模型 | 训练前诊断 | [Bridge Graphical Models: Coupling, Projection, and Current-Preserving Dynamics for Generative Modeling](cards-0002.md#paper-148153) | 先用桥速度的条件方差筛选耦合，再投入长时间训练。 |
| 计算机视觉 | 深度融合 | [BridgeMVS: Bridging Multi-View Stereo and Monodepth via Bidirectional Dynamic Fusion](cards-0002.md#paper-151655) | 让单目先验和多视角几何双向校准并跨尺度传递。 |
| 生成模型 | 条件采样 | [BridgeTwist: Twisting Schrödinger Bridges for Training-Free Conditional Sampling](cards-0002.md#paper-151085) | 冻结桥生成器，以端点估计和退火重要性权重做条件采样。 |
| 多模态学习 | 三维建模 | [Bridging 1D, 2D, and 3D with Any-to-Any Multimodal Modeling](cards-0002.md#paper-156144) | 用离散 token 和共同掩码任务联训不同三维表示。 |
| 图学习 | 可扩展评测 | [Bridging Academia and Industry: A Comprehensive Benchmark for Attributed Graph Clustering](cards-0002.md#paper-139018) | 按规模、同配性和标签可得性验证图聚类。 |
| 多模态学习 | 测试时适配 | [Bridging CLIP with DINO: Cross-Modal Information Maximization for Online Test-Time Adaptation](cards-0002.md#paper-152887) | 将文本原型投影到冻结自监督视觉空间，并过滤不可靠样本梯度。 |
| 语言模型 | 缩放律 | [Bridging Compute- and Data-Optimal Pretraining](cards-0002.md#paper-155350) | 按新鲜数据约束分配训练预算 |
| 时间序列 | 生成架构 | [Bridging Diffusion and Autoregression for Flexible Time Series Synthesis](cards-0002.md#paper-155931) | 跨块自回归、块内联合去噪 |
| 图学习 | 距离近似 | [Bridging Graph Worlds: Neural Approximation of Gromov-Wasserstein Distances](cards-0002.md#paper-151656) | 用学习代理批量比较图结构 |
| 计算机视觉 | 交替优化 | [Bridging Image Restoration and Recognition via Causal Mediated Unrolling](cards-0002.md#paper-153651) | 把识别信号和自然图像先验分步施加 |
| 多模态 Agent | 结构化记忆 | [Bridging Modalities, Spanning Time: Structured Memory for Ultra-Long Agentic Video Reasoning](cards-0002.md#paper-156072) | 长视频同时索引局部证据与跨时段叙事 |
| 强化学习 | 课程采样 | [Bridging Risk Approximation Gaps in Model Predictive Task Sampling via In-Context Modeling](cards-0002.md#paper-150549) | 按下一次策略更新后的难度选任务 |
| 强化学习 | 约束学习 | [Bridging Safety and Performance in Autonomous Systems using Offline Reinforcement Learning](cards-0002.md#paper-150431) | 将安全约束写入状态可行域而非仅作软惩罚 |
| 自动驾驶 | 表征迁移 | [Bridging Scene Generation and Planning: Driving with World Model via Unifying Vision and Motion Representation](cards-0002.md#paper-151833) | 将生成阶段学到的运动编码器与视觉编码器一同迁移 |
| 通用机器学习 | 域适配 | [Bridging Sequence and Structure with Unified Domain Adaptation for Drug-Target Interaction Prediction](cards-0002.md#paper-156127) | 推迟使用目标域伪标签，先校准预测 |
| 自动驾驶 | 域对齐 | [Bridging Simulation and Reality: Geometry and Decision Alignment for Autonomous Driving](cards-0002.md#paper-151850) | 同时检查几何对齐与策略行为对齐 |
| 多模态学习 | 可追溯监督 | [Bridging Structure and Language: Graph-Based Visual Reasoning for Autonomous Road Understanding](cards-0002.md#paper-151879) | 用可执行图查询生成有可验证落点的问答 |
| 推荐系统 | 表示对齐 | [Bridging Textual Profiles and Latent User Embeddings for Personalization](cards-0002.md#paper-152825) | 按检索效用训练可读用户画像 |
| 语言模型 | 安全对齐 | [Bridging the Gap Between Harmfulness Belief and Refusal Behavior for Safety Alignment](cards-0002.md#paper-149662) | 分开测风险判断与最终拒答 |
| 语言模型 | 缓存复用 | [Bridging the Gap: Position-Independent Cache Reuse for Hybrid SSM-Attention Architectures](cards-0002.md#paper-152513) | 统一混合注意力和状态空间层的跨位置缓存粒度 |
| 医学影像 | 跨模态蒸馏 | [Bridging the Modality Bottleneck in Pathology MIL through Virtual Molecular Staining](cards-0002.md#paper-150709) | 训练时以配对观测改造投影层，部署只用图像 |
| 科学机器学习 | 分布校准 | [Bridging the Simulation-to-Experiment Gap with Adversarial Distribution Alignment](cards-0002.md#paper-151598) | 用真实部分观测校准完整仿真的生成模型 |
| 语言模型 | 稳健评测 | [Brittlebench: Quantifying LLM robustness via prompt sensitivity](cards-0002.md#paper-139284) | 以语义等价改写测试排行榜稳定性 |
| 优化 | 双层优化 | [BROS: Bias-Corrected Randomized Subspaces for Memory-Efficient Single-Loop Bilevel Optimization](cards-0002.md#paper-149705) | 用随机子空间估计 Hessian 作用节省内存 |
| 语言模型 | 安全优化 | [BSO: Safety Alignment Is Density Ratio Matching](cards-0002.md#paper-156078) | 把安全偏好优化定义成比率匹配 |
| 表格生成 | 分块扩散 | [BSTabDiff: Block-Subunit Diffusion Priors for High-Dimensional Tabular Data Generation](cards-0002.md#paper-151140) | 用块级潜变量替代高维联合密度建模。 |
| 时间序列 | 计算分配 | [BucpTSF: Breaking the Uniform Computation Paradigm in Time-Series Forecasting](cards-0002.md#paper-148238) | 按信息密度、频带和预测跨度分配计算。 |
| 联邦学习 | 隐私训练 | [Budget-Conditioned Clipping Policies for Differentially Private Federated Learning](cards-0002.md#paper-150613) | 在公开代理上学习预算与轮次到裁剪阈值的映射后冻结。 |
| 强化学习 | 离策略估计 | [Budgeted Multi-Source Counterfactual Annotation for Off-Policy Evaluation](cards-0002.md#paper-155643) | 按成本与误差分配有限的反事实标注。 |
| 决策理论 | 预算分配 | [Budgeting Discretion: Theory and Evidence on Street-Level Decision-Making](cards-0002.md#paper-153217) | 依据收益分布尾部形态决定保留多少人工覆盖额度。 |
| 计算机视觉 | 三维高斯剪枝 | [BudSplat: Feed-forward 3D Gaussian Splatting under a Rendering Budget](cards-0002.md#paper-148823) | 按细节重要性和渲染贡献共同分配高斯。 |
| 深度学习 | 训练动力学 | [Bug or Feature$^2$: Weight Drift, Activation Sparsity, and Spikes](cards-0002.md#paper-149709) | 修改激活函数时同时监控稀疏度与异常尖峰。 |
| 智能体 | 代码工件评测 | [Build-and-Find: An Effort-Aware Protocol for Evaluating Agent-Managed Codebases](cards-0002.md#paper-138900) | 只有意图可可靠找回时才比较代码库检索开销。 |
| 几何深度学习 | 流形层 | [Building Transformation Layers for Riemannian Neural Networks](cards-0002.md#paper-151412) | 在相同层构造框架下比较不同流形。 |
| 量子机器学习 | 后验生成 | [BuresTomFlow: Bures-Geometric Flow Matching for Posterior Quantum Tomography](cards-0002.md#paper-148329) | 在保真度几何中学习量子态后验而非仅估点。 |
| 图学习 | 双曲注意力 | [Busemannformer: Horospherical Self-Attention for Hyperbolic Graph Transformers](cards-0002.md#paper-151890) | 按任务对称性和标签的层级属性选几何打分。 |
| 多模态学习 | 视频取证 | [BusterX: MLLM-Powered AI-Generated Video Forgery Detection and Explanation](cards-0002.md#paper-151123) | 把检测泛化和解释质量分开评估。 |
| 图学习 | 解释评测 | [B-XAIC Dataset: Benchmarking Explainable AI for Graph Neural Networks Using Chemical Data](cards-0002.md#paper-139598) | 用已知理由验证图解释而不仅依赖数据代理分数。 |
| 可解释性 | 特征复现 | [Bypassing PC1 Makes SAEs More Reproducible](cards-0002.md#paper-156083) | 训练稀疏自编码器时旁路主成分再在推理加回。 |
| 语言模型 | 蒸馏 | [ByteDistill: Cross-Tokenizer Distillation via Chunk-wise Byte-Level Distribution Alignment](cards-0002.md#paper-149633) | 跨分词器时对齐下一个可观测字节的分布。 |
| 多模态学习 | 细粒度微调 | [C2FT: Enhancing Fine-Grained Perception in MLLMs via Confuse-then-Contrast Fine-Tuning](cards-0002.md#paper-151433) | 按目标模型的具体混淆组织多图对照监督。 |
| 强化学习 | 分层控制评测 | [C2G-BENCH: A Cyber-Physical Evaluation Benchmark for Hierarchical Reinforcement Learning in Grid-Interactive Hyperscale Data Centers](cards-0002.md#paper-139076) | 用耦合的双时间尺度测试上层计划与下层控制。 |
| 智能体 | 角色记忆 | [C3: Long-Horizon Character Consistency via Causal-Continuous State Dynamics and Memory Rewriting](cards-0002.md#paper-151786) | 用连续状态和滞回更新角色，并按当前关系重释事件。 |
| 医学影像 | 压力测试 | [C3VD-DEFCOL: A Deformable Colonoscopy Dataset with Time-Resolved 3D Ground Truth and Realistic Appearance](cards-0002.md#paper-139182) | 按已知形变强度分层评估位姿估计。 |
| 生成模型 | 数值采样 | [CAB: Accelerating Flow and Diffusion Sampling via Rectification and Corrected Adams-Bashforth](cards-0002.md#paper-150465) | 低步数采样时比较带历史速度校正的多步积分。 |
| 计算机视觉 | 奖励建模 | [CaC: Advancing Video Reward Models via Hierarchical Spatiotemporal Concentrating](cards-0002.md#paper-153622) | 为视频奖励模型监督异常所在时间和空间。 |
| Agent | 缓存通信 | [CacheMAS: Cache Communication for Single-Pass, Jointly-Optimized Multi-Agent Systems](cards-0002.md#paper-154215) | 让多个角色通过预填充缓存共享状态，最终角色一次生成。 |
| 生成模型 | 推理缓存 | [Cache the Future: Training-Free Self-Revision for Diffusion Transformer Acceleration](cards-0002.md#paper-149314) | 用稀疏计算的后续状态修订此前跳过的时间步。 |
| 生成模型 | 覆盖诊断 | [CADMA: Capacity-Aware Recall Decomposition for Generative Model Assessment](cards-0002.md#paper-139801) | 用一对一局部分配评估生成分布的有效覆盖。 |
| 表格学习 | 特征构造 | [CAFE: Causally-Guided Automated Feature Engineering with Multi-Agent Reinforcement Learning](cards-0002.md#paper-151842) | 用软因果结构先验约束特征搜索，而非硬删除候选。 |
| 多模态学习 | 拓扑注意力 | [CAIRN: Cross-Room 3D Scene Understanding with Topology-Aware Large Multimodal Models](cards-0002.md#paper-151831) | 给多房间场景按物体和房间两层建立信息路径。 |
| 视频理解 | 比较式评估 | [CA-Judge: Teach Large Models to Judge Anomalies via Comparison for Video Anomaly Detection](cards-0002.md#paper-153516) | 用少数有信息量的参考比较代替绝对异常打分。 |
| 统计学习 | 校准评测 | [CalArena: A Large Scale Post-Hoc Calibration Benchmark](cards-0002.md#paper-139709) | 用恰当评分规则的改善度同时监测校准收益和预测质量。 |
| 统计学习 | 半监督估计 | [Calibeating Prediction-Powered Inference](cards-0002.md#paper-150100) | 先用小标注集校准预测分数，再用全量协变量估计均值。 |
| 强化学习 | 安全策略改进 | [Calibrated Safe Policy Improvement for Continuous Offline Reinforcement Learning](cards-0002.md#paper-148367) | 用校准的一步模型误差证书限制连续域搜索。 |
| 优化 | 曲率估计 | [Calibrated Target Noise Recovers Curvature from the Gradients](cards-0002.md#paper-154444) | 只有批梯度时用校准目标扰动估计曲率。 |
| 医学人工智能 | 概率校准 | [Calibrating Agentic LLMs for Clinical Prediction](cards-0002.md#paper-149149) | 临床预测 Agent 的验证同时检查风险概率校准和区分能力。 |
| 大语言模型 | 语义校准 | [Calibrating LLMs with Semantic-level Reward](cards-0002.md#paper-154784) | 通过答案语义一致性训练校准，减少置信度措辞影响。 |
| 科学机器学习 | 不确定性估计 | [Calibrating Scientific Foundation Models with Inference-Time Stochastic Attention](cards-0002.md#paper-153839) | 固定模型，通过随机注意力生成集合预测。 |
| Agent | 干预决策 | [Calibration Is Not Control: Intervention Advantage for LLM-Agent Oversight](cards-0002.md#paper-149357) | 从同一轨迹前缀比较继续和采取干预的预期效用。 |
| 统计学习 | 无标签校准 | [Calibration without Ground Truth](cards-0002.md#paper-152525) | 检查主模型和参考模型是否相互可校准，再决定是否转移校准信息。 |
| 统计学习 | 统计校准 | [Calibration without labels in multiple testing](cards-0002.md#paper-150447) | 校准局部错误率时用伪标签代替真实标签 |
| Agent | 隔离防御 | [CaMeLs Can Use Computers Too: System-level Security for Computer Use Agents](cards-0002.md#paper-155134) | 将可信规划与界面感知隔离 |
| 多模态 | 记忆机制 | [CAM: Question Answering on Entity-Centric Videos with Continuous Extraction and Adaptive Querying](cards-0002.md#paper-150537) | 将实体级长期摘要和按问题回查原始视频结合 |
| 视觉 | 记忆评测 | [Can 4D Foundation Models Remember?](cards-0002.md#paper-139573) | 用全景参考评估物体离开视野后的记忆 |
| Agent | 流程评测 | [Can Agents Price a Reaction? Evaluating LLMs on Chemical Cost Reasoning](cards-0002.md#paper-139478) | 用冻结价格快照和阶段分数评估工具代理 |
| Agent | 证据评测 | [Can AI Agents Synthesize Scientific Conclusions?](cards-0002.md#paper-139077) | 科学结论评估隔离答案泄漏并测事实级覆盖 |
| 法律AI | 证据归因 | [Can an LLM Reason Like a Lawyer? Benchmarking the ability of LLMs to map the facts of a case to the elements of the applicable legal rule](cards-0002.md#paper-139058) | 对法律模型测试事实到规则要件的显式归因 |
| 隐私 | 编码 | [Can Bits Seal Language?](cards-0002.md#paper-153783) | 把输入离散编码的隐私与效用一起比较 |
| 学习理论 | 鲁棒评测 | [Can Circuit Alignment Predict OOD Generalization?](cards-0002.md#paper-155822) | 用计算路径对齐而非仅激活相似度估计跨域性能 |
| 推荐 | 图表示 | [Can Complementary Signals Bridge Similarity Islands?  Manifold-Augmented Graph Embedding for Multimodal Recommendation](cards-0002.md#paper-155124) | 显式区分互补关系与相似替代关系 |
| Agent | 约束设计 | [CANDO: Cooperative Agentic Network for Layout Design Optimization](cards-0002.md#paper-153174) | 以场地约束验证器指导布局迭代 |
| 优化 | 梯度估计 | [Can Entry-Wise Clipping Give Spectral Control of Stochastic Gradients?](cards-0002.md#paper-154679) | 梯度噪声重尾时试验逐元素平滑收缩 |
| 系统 | 并行规划 | [Can Hybrid-Parallel Planning Support Alternating Model–Strategy Design? Dependency-Keyed Per-Layer Primitives for Re-Planning](cards-0002.md#paper-149399) | 并行策略重算时仅复用依赖签名一致的层级原语 |
| 公平性 | 排序诊断 | [Can Ideologues Agree on Quality? From Non-identifiable Latent Factors to Collective Outcomes](cards-0002.md#paper-154284) | 众包评分模型中明示何谓中立评价者 |
| 强化学习 | 探索奖励 | [Can In-Context Learning Support Intrinsic Curiosity?](cards-0002.md#paper-151481) | 按任务是否有时间依赖决定用上下文预测误差近似学习进展 |
| 大语言模型 | 长上下文 | [Can Language Models Actually Retrieve In-Context? Drowning in Documents at Million Token Scale](cards-0002.md#paper-153028) | 百万 token 检索单独诊断注意力归一化稀释 |
| Agent | 风险评测 | [Can Large Language Models Develop Gambling Addiction?](cards-0002.md#paper-149163) | 分别测试下注自主权和目标自主权的风险 |
| 多模态 | 表征适配 | [Can Linguistic Reasoning Vectors Enhance Multimodal Reasoning Ability?](cards-0002.md#paper-155152) | 从基础语言模型抽取推理方向辅助视觉语言模型 |
| Agent | 工具评测 | [Can LLM Agents Respond to Disasters? Benchmarking Heterogeneous Geospatial Reasoning in Emergency Operations](cards-0002.md#paper-139774) | 将地理工具代理的工具选择和参数定位分开评估 |
| 可解释性 | 行为诊断 | [Can LLMs explain themselves truthfully with code?](cards-0002.md#paper-150242) | 用留出输入上的行为一致性验证自解释。 |
| 大语言模型 | 数学评测 | [Can LLMs Reliably Grade Olympiad Proofs? A Controlled Study of Mathematical Verification with LLMs](cards-0002.md#paper-153381) | 将证明评分视为离散评分选择并报告序数一致性。 |
| 大语言模型 | 检索校准 | [Can LLMs Take Retrieved Information with a Grain of Salt?](cards-0002.md#paper-148640) | 衡量模型在来源不确定时是否调整回答置信。 |
| 统计学习 | 多源校准 | [Can Metadata Fix the Gauge? Calibration Turns Sparse Multi-Source Learning from Sparse PCA into Sparse Mean Recovery](cards-0002.md#paper-152833) | 优先采集可验证的相对坐标信息，再合并来源。 |
| 机器学习系统 | 分布式训练 | [Can Model Merging Improve Aggregation in DiLoCo?](cards-0002.md#paper-154543) | 局部训练间隔较长时对比合并式聚合和伪梯度平均。 |
| 深度学习 | 稀疏训练 | [Cannistraci-Hebb Channel-wise Dynamic Sparse Training of Convolutional Neural Networks with Contextual Modulation](cards-0002.md#paper-149797) | 按卷积通道构建拓扑并更新稀疏连接。 |
| 学习理论 | 条件预测 | [Canonical Predictive Quotients: A Theory of Prediction under Hidden Predictive State Uncertainty with ICL Implications](cards-0002.md#paper-154631) | 只恢复会改变当前最优预测的隐状态区别。 |
| 机器学习系统 | 推理调度 | [Canopy: Tree-Aware Rollout Scheduling for Agent Reinforcement Learning](cards-0002.md#paper-154204) | 把 rollout 树结构传给调度与 KV 缓存管理。 |
| 计算机视觉 | 来源验证 | [Can Pixels Alone Reveal Image Origin? Minimax Limits and Learnable Interfaces for Passive Provenance](cards-0002.md#paper-154460) | 分别验证来源统计可分性与接口暴露带来的风险。 |
| 多模态学习 | 反事实评测 | [Can the Parts Fool the Test? Counterfactual Pairing Cycles for Relational OOD](cards-0002.md#paper-149781) | 保持图和文字成分不变，仅更换配对测试关系绑定。 |
| 视频生成 | 采样调度 | [CanvasMAR: Improving Masked Autoregressive Video Prediction With Canvas](cards-0002.md#paper-148170) | 先提供全局未来帧粗预测，再逐区补细节。 |
| 计算机视觉 | 主动感知 | [CanViT: Toward Active-Vision Foundation Models](cards-0002.md#paper-151128) | 将局部感知骨干与可持续更新的场景记忆分离。 |
| 具身智能 | 安全评测 | [Can VLMs Reason When to Stop for Human Safety?](cards-0002.md#paper-139187) | 对同一任务构造应停止和可继续的配对场景。 |
| 计算机视觉 | 伪影定位 | [Can We Model the Artifacts Explicitly? Disentangle Artifacts via Pairwise Edit Relations for Image Manipulation Localization](cards-0002.md#paper-155638) | 用同源编辑之间的关系监督潜在伪影表征。 |
| 统计学习 | 评测诊断 | [Can We Trust Item Response Theory for AI Evaluation?](cards-0002.md#paper-139287) | 使用 IRT 前按模型数量和能力分布做仿真校准。 |
| 大语言模型 | 知识编辑 | [Capacity Allocation at the Source: Sparse Target Optimization for LLM Knowledge Editing](cards-0002.md#paper-148802) | 在求目标隐态时约束稀疏度，减少多次编辑干扰。 |
| 优化 | 延迟反馈 | [Capacity-Constrained Online Convex Optimization with Delayed Feedback](cards-0002.md#paper-151561) | 用随机调度和重要性权重管理有限反馈追踪预算。 |
| 自然语言处理 | 过程监督 | [CAPER: Clause-Aligned Process Supervision for Text-to-SQL](cards-0002.md#paper-149623) | 将 SQL 语义子句作为奖励和故障定位单元。 |
| Agent | 约束优化 | [CAPO: A Primal-Dual Framework for Constraint-Aware Prompt Optimization](cards-0002.md#paper-149769) | 为工具使用和输出要求设显式阈值后优化系统提示。 |
| 机器学习系统 | 隐私推理 | [Capricorn: Highly Efficient and Secure Mixture of Experts Inference Framework](cards-0002.md#paper-152572) | 分别优化安全 MoE 路由与激活的通信开销。 |
| 大语言模型 | 遗忘评测 | [CapTrack: Multifaceted Evaluation of Forgetting in LLM Post-Training](cards-0002.md#paper-138881) | 按能力拆分后训练漂移 |
| 大语言模型 | 上下文蒸馏 | [Capturing In-Context Learning Dynamics with Task Operators](cards-0002.md#paper-149094) | 用输入相关算子代替固定任务向量 |
| 大语言模型 | 能力评测 | [Capturing LLM Capabilities via Evidence-Calibrated Query Clustering](cards-0002.md#paper-148906) | 按模型表现校准语义聚类 |
| 科学机器学习 | 算子学习 | [Capturing Membrane Dynamics and Spike Timing of Human Neurons at Scale using Neural Operators](cards-0002.md#paper-149091) | 同类神经元共享条件算子 |
| 推荐系统 | 多关系损失 | [Cardinality-Decomposed Loss for Heterogeneous GNNs](cards-0002.md#paper-150315) | 按关系基数配置训练损失 |
| Agent | 强化学习 | [CARD: Internalizing Expert Critique into Reinforcement Learning for Deep Search](cards-0002.md#paper-152838) | 对被反馈真正改写的步骤提高权重 |
| 医疗多模态 | 评测诊断 | [CardioLens: Revealing the Clinical Reality Gap of MLLMs via Multi-Sequence Cardiac MRI Evaluations](cards-0002.md#paper-139679) | 按完整影像流程分层验收 |
| 大语言模型 | 过程评测 | [CAREBench: Evaluating LLMs' Emotion Understanding by Assessing Cognitive Appraisal Reasoning](cards-0002.md#paper-139329) | 把情绪推断过程与终局标签分开测 |
| 计算机视觉 | 反事实评测 | [CARVE: Counterfactual Video Editing for Auditing and Hardening Video Detectors](cards-0002.md#paper-151526) | 正交干预环境和事件来诊断检测捷径 |
| 优化 | 泛化正则 | [CASAM: Consistency-Anchored Sharpness-Aware Minimization for Improved Model Generalization](cards-0002.md#paper-152013) | 用样本与批梯度的一致性分配训练权重 |
| 多模态学习 | 解释性 | [Cascaded Sparse Autoencoders LearnMulti-Level Visual Concepts in Multimodal LLMs](cards-0002.md#paper-151133) | 用特征字典训练上层稀疏编码器 |
| 大语言模型 | 自博弈 | [CasePlay: Self-Play Reinforcement Learning from Case Reports for Medical Reasoning](cards-0002.md#paper-153097) | 用信息点覆盖和题目质量分别约束自博弈 |
| 生成模型 | 可解释性 | [CASL: Concept-Aligned Sparse Latents for Interpreting Diffusion Models](cards-0002.md#paper-149923) | 先训练稀疏字典再以少量概念标签建立映射 |
| 统计学习 | 结构化潜变量 | [CASL-VAE: Learning Structured Latent Variables from Unpaired Data for Semi-supervised Clustering and Paired Sample Generation](cards-0002.md#paper-150313) | 把共享变化和目标群体内部变化分解 |
| 神经符号学习 | 约束投影 | [Casper: A Projection-Based Neurosymbolic Layer for Scalable & Guaranteed Constraint Satisfaction](cards-0002.md#paper-149782) | 把可行性作为可微输出层 |
| Agent | 防御监测 | [CASPIAN: Online Detection and Attribution of Cascade Attacks in LLM Multi-Agent Systems via Cross-Channel Causal Monitoring](cards-0002.md#paper-150932) | 合并多渠道信号识别异常传播 |
| 推荐系统 | 离散表征 | [CASQRec: Collaborative-Adaptive Semantic Quantization for Multimodal Recommendation](cards-0002.md#paper-155565) | 让协同行为监督语义码分配 |
| 时间序列 | 分布预测 | [CAST: Causal Anchored Simplex Transport for Distribution-Valued Time Series](cards-0002.md#paper-155150) | 用上下文区分同状态下的不同转移规律 |
| 强化学习 | 稳健迁移 | [CAST: Certifiable Aggregation of Smoothed Teachers for Robust Policy Adaptation](cards-0002.md#paper-151249) | 聚合带证书的源策略并复查目标侧保证 |
| 多模态学习 | 能力诊断 | [Castle-in-the-Air: Probing the Foundational Visual Deficits of MLLMs via Bottom-Up Cognitive Factors](cards-0002.md#paper-139489) | 在高层问答之外测可控难度的基础视觉 |
| 按授权模型评估数据重编码 | 数据授权 | [Catch-Only-One: Non-Transferable Examples for Model-Specific Authorization](cards-0002.md#paper-151014) | 检验授权与未知模型的效用差距 |
| 语言模型 | 自适应计算 | [Catch Your Breath: Adaptive Computation for Self-Paced Sequence Production](cards-0002.md#paper-152630) | 让模型学习何时暂停和继续 |
| 语言模型安全 | 偏好优化 | [Cat-DPO: Category-Adaptive Safety Alignment](cards-0002.md#paper-151048) | 按风险类别分别调节训练边际 |
| 认知建模 | 状态估计 | [Categorical Bayes filtering for computational phenotyping in adaptive learning](cards-0002.md#paper-153212) | 用可微分网格替代随机外层粒子 |
| 图学习 | 归纳偏置 | [Caterpillar GNN: Replacing Message Passing with Graph-Level Aggregation](cards-0002.md#paper-148837) | 按任务需求限制图网络表达力 |
| 多模态学习 | 推理加速 | [CATS: Acceptance-Oriented Critical Token Adaptive Selection for Multimodal Speculative Decoding](cards-0002.md#paper-154883) | 优先对齐视觉依赖或高拒绝率 token |
| 科学机器学习 | 消融设计 | [Cauchy Scientific Networks: Loss–Architecture Alignment and Its Limit](cards-0002.md#paper-148993) | 交叉消融损失与激活函数 |
| 因果学习 | 理论 | [Causal Abstractions, Categorically Unified](cards-0002.md#paper-153629) | 分开验证图兼容与变量聚合 |
| 计算机视觉 | 结构监督 | [CausalAffect: Causally Guided Learning of Psychology-Aligned Facial Affect Relations](cards-0002.md#paper-148159) | 将全局关系与样本关系分开拟合 |
| 计算机视觉 | 可解释性 | [Causal Attribution via Activation Patching](cards-0002.md#paper-155095) | 在中间层直接检验图块表征贡献 |
| 公平性 | 因果分解 | [Causal Bias Detection in Generative Artifical Intelligence](cards-0002.md#paper-149915) | 审计生成模型时区分路径效应和机制替换效应 |
| 计算机视觉 | 记忆路由 | [CausalCine: Real-Time Autoregressive Generation for Multi-Shot Video Narratives](cards-0002.md#paper-154338) | 跨镜头视频按内容相关性选缓存 |
| 因果学习 | 鲁棒评测 | [CausalCompass: Evaluating the Robustness of  Time-Series Causal Discovery in Misspecified Scenarios](cards-0002.md#paper-139526) | 把标准化与假设违背分别做对照 |
