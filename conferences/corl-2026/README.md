# CoRL 2026

[首页](../../README.md) · [官方录用名单](https://2026.corl.org/program/accepted-papers)

已筛选 **687 / 687** 篇，按四项暂定评分保留 **343** 篇。规则排除 **47** 篇，排名移出 **297** 篇。[筛选底册](papers.tsv) · [评分与排名](scores.tsv)

| 领域 | 技术类型 | 论文卡 | 能改变的技术选择 |
| --- | --- | --- | --- |
| 具身智能 | 数据策略 | [Diagnosing Compositional Generalization in Sequential Robot Tasks](cards.md#paper-gqfyim5djy) | 示范预算固定时，优先覆盖决定动作的指令组合 |
| 具身智能 | 推理与部署 | [EmbodiSteer](cards.md#paper-2z8xqxrlsy) | 在扩散采样中处理目标机器人的全身约束 |
| 具身智能 / 多模态 | 记忆与表征 | [MEM](cards.md#paper-5tiity1fk3) | 分开保留近期视频与长时语义事件 |
| 具身智能 / 多模态 | 推理与部署 | [When Vision Overrides Language](cards.md#paper-hmdwoezjlq) | 固定画面替换指令，分测语言落地和成功率 |
| 具身智能 | 数据策略 | [FAKTUAL](cards.md#paper-tscng5wcwn) | 固定示范预算下按轨迹核熵选样 |
| 具身智能 | 评测与诊断 | [ZETA](cards.md#paper-4rljgpefph) | 分开评估目标本体完全未见和预训练已见 |
| 具身智能 / 多模态 | 表征学习 | [Semantic Anchoring for Robotic Action Representations](cards.md#paper-ytw6loo9c5) | 微调时分开保护可迁移语义与动作专有信息 |
| 具身智能 / 多模态 | 训练数据与条件化 | [π0.7](cards.md#paper-5xkfwwrw0v) | 混用低质轨迹时显式标注执行策略和质量 |
| 具身智能 / 多模态 | 评测与诊断 | [What Are We Actually Benchmarking in Robot Manipulation?](cards.md#paper-rdvh11pafj) | 用缺失目标能力的探针和受控扰动检验基准能否支持能力声明 |
| 具身智能 | 策略优化 | [Chunk-wise Model-based Policy Optimization](cards.md#paper-dngzli0slv) | 训练时用一次前向评估整段动作的价值 |
| 具身智能 / 多模态 | 动作生成 | [Diffusion ReRoll](cards.md#paper-hbux1fe8bl) | 采样时给已去噪片段保留利用后续上下文修订的机会 |
| 具身智能 / 多模态 | 推理与部署 | [EagleVLA](cards.md#paper-ockqyiy2qm) | 用未来状态预测对齐异步动作起点并动态分配调用预算 |
| 具身智能 / 多模态 | 动作生成 | [REACT](cards.md#paper-ffb8qnjwv2) | 跨观测修订未执行动作块兼顾连续性与反应 |
| 具身智能 | 策略优化 | [TARC](cards.md#paper-wvr13crtrf) | 将动作保持时间纳入策略输出并约束控制切换次数 |
| 具身智能 / 多模态 | 世界模型 | [Mem-World](cards.md#paper-f9grq4ncx9) | 按动态表面元素检索腕部视角历史 |
| 强化学习 | 策略优化 | [FedGuide](cards.md#paper-qbaa8svaik) | 按行为分布聚合异构客户端而非直接混合策略参数 |
| 具身智能 / 多模态 | 模型架构 | [CoRE-VLA](cards.md#paper-qku6lifnpu) | 分开用传感器可用性与任务意图路由专家 |
| 具身智能 / 多模态 | 动作表示 | [X-Tokenizer](cards.md#paper-mg3ebtsbig) | 按量化层区分动作意图与运动细节 |
| 具身智能 / 多模态 | 动作表示 | [ActionCodec](cards.md#paper-wrlegprnvr) | 用下游训练难度和闭环指标一起选动作 tokenizer |
| 具身智能 / 多模态 | 世界模型 | [Unified Motion Action Model](cards.md#paper-efgcnzgmvn) | 用可切换的掩码统一物体运动预测与机器人控制 |
| 具身智能 / 多模态 | 表征学习 | [FIBERTUNE](cards.md#paper-ynhgrgatuy) | 将动作可预测方向滤除后再蒸馏视觉残差 |
| 具身智能 / 多模态 | 动作表示 | [AC-LAM](cards.md#paper-03qrtmw4qx) | 通过跨时间可加约束减少潜动作对场景外观的依赖 |
| 具身智能 / 多模态 | 动作表示 | [PoLAR](cards.md#paper-jkop9l6myq) | 显式分开潜动作的变化幅度与变化类别 |
| 具身智能 / 多模态 | 表征学习 | [GeoProp](cards.md#paper-rce4amkjbq) | 用运动学投影把本体状态对准同位置的视觉特征 |
| 具身智能 / 多模态 | 传感器融合 | [MoSS](cards.md#paper-wkrawikmug) | 为力觉、触觉与力矩建立独立传感流并预测未来反馈 |
| 具身智能 / Agent | 长时记忆 | [TRACE](cards.md#paper-apppmsjzb5) | 用已执行轨迹给早期视觉证据建立检索键 |
| 具身智能 / Agent | 长时记忆 | [Gated Memory Policy](cards.md#paper-tzm6j864lf) | 让策略选择何时读取历史并训练其容忍错误历史动作 |
| 具身智能 / 多模态 | 长时记忆 | [EventVLA](cards.md#paper-8fgh4qadnb) | 在视觉证据消失前预测其未来价值并决定是否写入 |
| 具身智能 / Agent | 长时记忆 | [Chameleon](cards.md#paper-ttj3uxlcxl) | 在最终画面相同的条件下分测记忆决策和实际执行 |
| 具身智能 / Agent | 长时记忆 | [MessyMem](cards.md#paper-gqqwqejrtq) | 将交互得知的属性与关键帧绑定到可更新场景图 |
| 具身智能 / Agent | 长时记忆 | [Workspace Models](cards.md#paper-aposmvav9y) | 把任务显著性标注搬到训练并蒸馏成潜工作记忆 |
| 具身智能 | 持续学习 | [Memory Anchors](cards.md#paper-dsbthpqfj9) | 回放优先保留与新任务表征近但动作冲突的旧样本 |
| 具身智能 / 多模态 | 世界模型 | [WLA-0](cards.md#paper-oihlruloiq) | 用共享查询吸收未来预测监督并按需启用显式预测 |
| 具身智能 | 数据策略 | [RoboPocket](cards.md#paper-thg2jwuii6) | 采集时先显示当前策略的预测轨迹，再补失败附近的示范 |
| 具身智能 / Agent | 偏好学习 | [IMPLIED](cards.md#paper-qxboq98qn4) | 把固定规则推导的偏好标签当作可更新的先验 |
| 具身智能 / Agent | 评测与诊断 | [Learning to Assist](cards.md#paper-79jc3quhgp) | 检查动作块是否跨过人类尚未准备好的协作边界 |
| 具身智能 / 多模态 | 安全评测 | [TouchSafeBench](cards.md#paper-hvarz6f8ea) | 分开测当前接触与提前预警，并按碰撞对象分层 |
| 具身智能 / Agent | 偏好学习 | [Asking Smarter Questions](cards.md#paper-hfhtppdbyr) | 针对示范中监督不足的奖励特征生成并解释偏好问题 |
| 具身智能 / 强化学习 | 策略优化 | [PIVOT](cards.md#paper-2vx7i6arps) | 在流匹配后训练中按带符号优势吸引或排斥部署数据 |
| 具身智能 / 强化学习 | 策略优化 | [DIQL](cards.md#paper-vvdyxlghxh) | 根据数据支持程度按状态选择乐观分位 |
| 具身智能 / 强化学习 | 策略优化 | [Robo-ValueRL](cards.md#paper-qx5mpyixvi) | 用全局任务进度和局部动作排序分别诊断价值函数 |
| 具身智能 / 强化学习 | 策略优化 | [TIGER](cards.md#paper-az2ojk8zxd) | 用模仿策略提供末端任务进度奖励而非直接执行其动作 |
| 具身智能 / 强化学习 | 策略优化 | [UniIntervene](cards.md#paper-ar3ewq6mh4) | 用近期价值趋势触发恢复，并从历史干预中找恢复目标 |
| 具身智能 / 强化学习 | 策略优化 | [Preference-calibrated Actor-Critic Training](cards.md#paper-tpevwyct8w) | 给人工接管前的低效片段重新分配回报 |
| 具身智能 / 强化学习 | 偏好学习 | [DCCP](cards.md#paper-pnsqn6bng7) | 固定同一观测前缀，只替换第一动作块来形成局部偏好 |
| 具身智能 / 强化学习 | 奖励设计 | [RARM](cards.md#paper-aan8ouehwo) | 按单条参考示范匹配进度并在低置信时抑制奖励 |
| 具身智能 / 强化学习 | 奖励设计 | [HiRE](cards.md#paper-0ua1khfiud) | 用成功与失败轨迹回看并修正误导控制的进度奖励 |
| 具身智能 / 强化学习 | 策略优化 | [EXPO-FT](cards.md#paper-u3nmrhun8b) | 动作块中只覆盖人工纠正的时间段并保存实际执行块 |
| 具身智能 / Agent | 任务规划 | [M³P-R1](cards.md#paper-gfxjqzvsnd) | 让模型生成可由求解器验证的规划约束 |
| 具身智能 | 示范采集 | [PAKT](cards.md#paper-2vdrocnuih) | 采集时约束人工引导轨迹以匹配部署执行接口 |
| 具身智能 / 强化学习 | 策略优化 | [Q-OIL](cards.md#paper-9seu2keixr) | 用真实停滞干预数据校准模拟人类，并重访有信息的状态 |
| 具身智能 / 强化学习 | 部署适配 | [TERRA](cards.md#paper-w443fvglzc) | 按预测的任务相关模型误差选择部署时采样路线 |
| 具身智能 | 推理与部署 | [One-step action generation](cards.md#paper-4dqrad2snp) | 部署前先试同一流策略的一步积分再决定是否蒸馏 |
| 具身智能 / Agent | 多机器人协作 | [Learning Coordinated Visuomotor Box-Pushing from Solo Demonstrations](cards.md#paper-gpc0ncixhz) | 分开测试单机示范能传授什么以及协作数据仍缺什么 |
| 具身智能 / 多模态 | 推理与部署 | [OmniGuide](cards.md#paper-pewwdul10x) | 用统一三维能量接口接入不同来源的空间引导 |
| 具身智能 / 多模态 | 表征学习 | [SFHand](cards.md#paper-p8h2wzh2tw) | 用人手未来三维运动作为人类视频的预训练监督 |
| 具身智能 / 强化学习 | 策略优化 | [MERL](cards.md#paper-0pthtaiwpd) | 按世界模型可靠性调整想象比例、长度和样本权重 |
| 具身智能 / Agent | 长时记忆 | [Procedural Assistance Memory](cards.md#paper-nxfwmrzxzz) | 把个性化帮助规则写成可修订的事件状态机 |
| 具身智能 / 多模态 | 训练策略 | [ABC](cards.md#paper-qd6clcx6qy) | 一次视觉语言前向复用多个扩散噪声和时间样本 |
| 具身智能 | 动作生成 | [Mixture of Frames Policy](cards.md#paper-f5329hhiji) | 在同一去噪过程中融合不同参考系的预测 |
| 具身智能 / 多模态 | 传感器融合 | [GeoHAT](cards.md#paper-qhndjmxgs1) | 仅在深度可信的位置向视觉主干注入三维特征 |
| 具身智能 / Agent | 数据策略 | [AIDA-OWMM](cards.md#paper-4m7c3psa78) | 直接用部署时可用的观测和技能接口采教师示范 |
| 具身智能 / Agent | 表征学习 | [A4D](cards.md#paper-8qefjwsgyu) | 用功能距离触发可供性发现 |
| 具身智能 / 多模态 | 三维表征 | [Phase-Conditioned Affordance Fields](cards.md#paper-zhig7xb56d) | 随操作阶段改变等变策略的局部参考点 |
| 具身智能 / 多模态 | 数据策略 | [SimHum](cards.md#paper-cvpjguuatq) | 让仿真提供机器人动作监督，让人类视频提供真实视觉经验 |
| 具身智能 | 动作表示 | [BiRoAD](cards.md#paper-keuuzk1rsd) | 将双臂表示分为交换不变的协调部分与随角色交换改变的部分 |
| 具身智能 | 动作表示 | [Foci Policy](cards.md#paper-aztnrtznof) | 只学习关键交互时段内的物体间相对运动 |
| 具身智能 / 强化学习 | 策略优化 | [Interaction-weighted Resampling](cards.md#paper-qlhhholka7) | 在接触改变动力学的前中后阶段重新分配对比样本 |
| 具身智能 / 多模态 | 数据增强 | [SIDO](cards.md#paper-mqly5j6pnd) | 用静态示范合成指向未来物体位姿的动作块 |
| 具身智能 / 机器人学习 | 数据采集 | [SuperSuit: An Isomorphic Bimodal Interface for Scalable Mobile Manipulation](cards.md#paper-penaq22jh1) | 设计共享的关节增量动作接口，使穿戴示范和遥操作数据能在同一策略中混用。 |
| 具身智能 / 规划 | 启发式搜索 | [REAP: Learning General Rearrangement Heuristics from Motion-Planner Feedback](cards.md#paper-pax622bsf6) | 用运动规划器反馈训练符号搜索启发式，减少昂贵的几何查询。 |
| 具身智能 / 多模态 | 视觉表示 | [ReSiReg: Towards Spatially Consistent Semantics in Language-Conditioned Robotic Tasks](cards.md#paper-1hqdyvwaxi) | 用空间稳定的中间特征重建开放词汇定位图。 |
| 具身智能 / 多模态 | 表示对齐 | [LCLA: Language-Conditioned Latent Alignment for Vision-Language Navigation](cards.md#paper-av4ykymvpx) | 迁移导航控制时让新感知适配冻结专家的内部状态。 |
| 具身智能 / 世界模型 | 扩散策略 | [WAM-Nav: Asymmetric Latent World-Action Modeling for Unified Visual Navigation](cards.md#paper-pjzsychbzg) | 联合生成长动作与短视觉预测，减少为远期控制生成远期视觉的成本。 |
| 具身智能 / 规划 | 采样策略 | [Self-supervised Dispersive Sampling for Quadrotor Motion Planning](cards.md#paper-8xayrudune) | 根据控制经动力学映射后的状态覆盖训练采样器。 |
| 具身智能 / 导航 | 评测与诊断 | [TopoUrbanBench: Group-Structural Compliance Evaluation for Urban Robot Navigation](cards.md#paper-1jcoslxzhb) | 评测社会导航时同时统计轨迹是否穿越队列或人群交互区域。 |
| 具身智能 / 世界模型 | 不确定性建模 | [Schrödinger's Navigator: Imagining an Ensemble of Futures for Zero-Shot Object Navigation](cards.md#paper-forrdaq3mz) | 遮挡严重时按候选轨迹生成多种可能观测，再聚合价值选路。 |
| 具身智能 / 规划 | 观测设计 | [Task-Aware Environment Augmentation for Reliable Navigation via Shielded Conditional Diffusion](cards.md#paper-odfnfgiie3) | 把有限的定位标记布在即将出现高风险定位误差的路段。 |
| 具身智能 / 多模态 | 决策接口 | [PIGEON: VLM-Driven Object Navigation via Points of Interest Selection](cards.md#paper-a1wg3rqdsr) | 把航点和原始观测绑定为可验证的任务候选，交给 VLM 稀疏选择。 |
| 具身智能 / 多模态 | 不确定性校准 | [CoSMO: Conformal Semantic Mapping for Open-World Safe Robot Navigation](cards.md#paper-ptqogquuch) | 先校准开放词汇危险类别预测集合，再按语义风险扩张避障区域。 |
| 具身智能 / 规划 | 代价建模 | [CoGeL: Constraint-to-Geometry Learning from Demonstrations and Failures for Safe Long-Horizon Robot Navigation](cards.md#paper-xm8lpylbxa) | 将从干预和失败学来的局部风险直接写入用于长程规划的目标距离。 |
| 具身智能 / 规划 | 风险控制 | [Adaptive Risk-Certified Event-Triggered Replanning for Dynamic Navigation](cards.md#paper-xyrbf93mwh) | 用未来轨迹的尾部风险触发换规划模式，同时保留下一步安全过滤。 |
| 具身智能 / 强化学习 | 扩散策略 | [X-NavDP: Generalizing Navigation Diffusion Policy to Novel Behavior and Embodiments with Group Q-score Reweighted Matching](cards.md#paper-c0ygolwl7i) | 用同状态的轨迹 Q 分组归一化来加权 score matching，后训练扩散策略。 |
| 具身智能 / 多模态 | 主动感知 | [LIME: Learning Intent-aware Camera Motion from Egocentric Video](cards.md#paper-erptr7eec1) | 从被动视频构造意图、预期观测和相对位姿监督，学习按需移动相机。 |
| 具身智能 / 视觉 | 几何监督 | [Geometry-Aware Absolute Pose Regression via Geometric Pose Proxy](cards.md#paper-whavgmiwj3) | 在绝对位姿回归中预测含透视约束的中间表示，并在几何空间增强视角。 |
| 具身智能 / 视觉 | 特征匹配 | [CoReMatch: Recurrent Continuous Coordinate Refinement for Real-Time Robotic Feature Matching](cards.md#paper-ojmvvfkk6t) | 在连续坐标中迭代修正对应点，以低分辨率特征保留几何精度。 |
| 具身智能 / 视觉 | 推理缓存 | [LateMatch: Breaking the Interaction Bottleneck via Cacheable Matching for Efficient Visual Localization](cards.md#paper-a9tbpzfswi) | 延迟跨输入交互，让重复使用的单图特征可预计算并缓存。 |
| 具身智能 / 视觉 | 几何校准 | [LSPR: Init-Anchored Score-Based Multi-Camera Calibration for Indoor Robot Manipulation](cards.md#paper-2aoavwqgc6) | 学习强初始化器的局部标定误差，并在置信度低时回退至原估计。 |
| 具身智能 / 视觉 | 监督去偏 | [OptiGeo: Efficient Monocular Geometry for Embodied Perception in Optically Challenging Scenes](cards.md#paper-7bckvvmpuj) | 对已知会失效的传感器区域，引入干净几何监督而非直接拟合传感器读数。 |
| 具身智能 / 定位 | 状态估计 | [MaD-PF: Modular and Differentiable Particle Filter for Cross-Environment SE(3) LiDAR Localization](cards.md#paper-l8atlvewkt) | 保留粒子多假设，分别评估可微运动、观测及重采样模块的迁移和耗时。 |
| 具身智能 / 视觉 | 自动标注 | [AmodalBox: Automated 3D Bounding Box Annotation under Partial Visibility](cards.md#paper-0o1c1xxn1m) | 稀疏点云只覆盖局部时，以图像生成的完整几何作为伪标签先验。 |
| 具身智能 / 定位 | 场景图 | [Functional-SLAM: Interaction-Aware Mapping with Online Functional Scene Graphs](cards.md#paper-9gwuac6oum) | 在线积累物体功能关系，将稳定拓扑作为额外闭环线索。 |
| 具身智能 / 强化学习 | 辅助控制 | [AI Coaching for Accelerating Human Skill Development with Reinforcement Learning](cards.md#paper-m0zqqi9lfr) | 辅助训练系统以撤掉辅助后的独立能力为目标，并允许用户经历有助于学习的失败。 |
| 具身智能 / 视觉 | 在线建图 | [RoMo-GS: Efficient Online 3D Gaussian Splatting for Robot Mapping via Exposure-Integrated Motion Blur](cards.md#paper-1j0hw81jy9) | 按曝光时间解析积分运动中的高斯投影，避免逐子帧渲染。 |
| 具身智能 / 定位 | 自监督状态估计 | [Learning Contact Representation for Leg Odometry](cards.md#paper-4uxhlsonz5) | 用连续支撑信念调整滤波噪声，并按里程计误差选择接触表征。 |
| 具身智能 / 定位 | 等变表示 | [GINIO: A Geometric SO(3)-Equivariant Interface for Neural Inertial Odometry](cards.md#paper-nl8ibtm3mt) | 要求学习测量的均值与协方差都按传感器安装旋转正确变换。 |
| 具身智能 / 多模态 | 概率地图 | [Language as a Sensor: Calibrated Spatial Belief Estimation in 3D Scenes from Natural Language](cards.md#paper-yz4p3wbwkx) | 把自然语言描述作为可校准传感观测融入地图。 |
| 具身智能 / 机器人学习 | 数据增强 | [Worlds in One Demo: A Synthetic Data Engine for Learning Open-World Mobile Manipulation](cards.md#paper-w1x9mho93e) | 拼接保留接触的轨迹片段并主动扩增纠错状态。 |
| 具身智能 / 规划 | 生成规划 | [Safe Streaming Flow Planning by Aligning Sampling Dynamics with Execution Dynamics](cards.md#paper-gvm7kwehvi) | 使生成路径逐步随物理执行更新，并仅认证实际执行的步。 |
| 具身智能 / 规划 | 空间表示 | [Learning Unions of Convex Sets via Invertible Latent Decomposition for Path Planning](cards.md#paper-txufbhgqg2) | 把高维自由空间映射为可连接的潜空间凸集以便显式规划。 |
| 具身智能 / 控制 | 扩散策略 | [Grounding Generative Policies in Physics: Optimization-Guided Diffusion for Robot Control](cards.md#paper-eaejdjpdzm) | 去噪时直接优化物理可行的校正量。 |
| 具身智能 / 控制 | 轨迹表示 | [PolyFusion: Collision-Free Robot Learning using Bernstein Polynomials](cards.md#paper-m8nqiskmdr) | 用分段多项式控制点代替稠密动作头。 |
| 具身智能 / 控制 | 跨构型迁移 | [CMRDF: Morphology-Conditioned Reachability Fields for Task-Space Robot Policy Transfer](cards.md#paper-dga5zlu7ck) | 将可达性拆成全局位置与局部姿态，集中逆运动学预算。 |
| 具身智能 / 规划 | 理论与诊断 | [On the Limits of Sampling-Based Reachability: Geometry, Dynamics, and Sample Complexity](cards.md#paper-wylezeakfi) | 高维长时域下避免仅凭采样质量保证宣称几何覆盖。 |
| 具身智能 / 多模态 | 不确定性校准 | [SentryVLA: Uncertainty-Guided Action Selection and State Monitoring for Vision-Language-Action Robotic Control](cards.md#paper-snidokrnny) | 给冻结 VLA 加候选重排与独立执行异常监测。 |
| 具身智能 / 人机交互 | 主动查询 | [Simultaneous Forward and Inverse Human-in-the-Loop Optimization](cards.md#paper-cqkikio00k) | 以同一次用户查询同时降低结果模型和偏好模型的不确定性。 |
| 具身智能 / 强化学习 | 课程生成 | [Generative Flow on Symbolic Abstractions for Embodiment Capability Discovery](cards.md#paper-weyfps89nj) | 用低层策略实测学习表现训练任务生成器。 |
| 具身智能 / 规划 | 推理调度 | [When Should a Robot Replan? Regret-Guided Update Scheduling in Time-Varying MDPs](cards.md#paper-4pwzyvbjxy) | 按累计遗憾分配有限的模型更新和重规划预算。 |
| 具身智能 / 多模态 | 数据策略 | [EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data](cards.md#paper-wf4x17al2r) | 用人类视频验证损失作为决定继续扩数据还是进入机器人中训的候选信号。 |
| 具身智能 / 强化学习 | 技能预训练 | [Play2Perfect: What Matters in Dexterous Play Pretraining for Precise Assembly?](cards.md#paper-rrl1xxzldm) | 先用自由操作预训练可达性和重定向能力，再把探索集中到精密接触阶段。 |
| 具身智能 / 模仿学习 | 重采样 | [FACTR 2: Learning External Force Sensing for Commodity Robot Arms Improves Policy Learning](cards.md#paper-03zmmfktxk) | 根据估计外力找到接触边界，在行为克隆中提高接触前片段的采样率。 |
| 具身智能 | 评测诊断 | [Automating the Design of Embodied Agent Architectures](cards.md#paper-2lnbcnztqk) | 用独立环境审计自动架构搜索 |
| 具身智能 | 共享自治 | [Efficient and Reliable Teleoperation through Real-to-Sim-to-Real Shared Autonomy](cards.md#paper-qgzgvp8rnk) | 用少量示范拟合操作者代理，再在仿真学残差辅助 |
| 具身智能 | 策略适配 | [FlowDAgger: Human-in-the-Loop Adaptation of Generative Robot Policies in Latent Space](cards.md#paper-aspenn9eir) | 将纠正动作反演成冻结生成策略的输入噪声 |
| 具身智能 | 动作表示 | [KPGrasp: Scalable Keypoint Flow Matching for Dexterous Grasp Generation](cards.md#paper-bxnvzgsyfe) | 把混合关节和刚体坐标改成同一参考系下的欧氏关键点 |
| 具身智能 | 多智能体协作 | [Leave It Better Than Found: Value-Guided Cooperation in Sequential Tasks](cards.md#paper-n77om40jwl) | 跨机器人共享后续任务价值，筛除分布外估值 |
| 具身智能 | 世界模型 | [WM-Craftnet: World Synesthesia Model for Robust and Generalizable Dexterous In-Hand Manipulation](cards.md#paper-amqh2hu9gs) | 让多模态动力学潜状态作为策略上下文，并显式监督深度去噪 |
| 具身智能 | 策略梯度 | [Flow Policy Gradients for Robot Control](cards.md#paper-acslhrig33) | 在需要多峰动作时测试免似然流策略梯度 |
| 具身智能 | 接触反馈 | [PACE: Temporal-Role Tactile Conditioning for Chunk-Based Insertion Policies](cards.md#paper-aiinkhzlvb) | 分开处理持续接触、突发事件和未来接触 |
| 具身智能 | 合成监督 | [GRAIL: Generating Humanoid Loco-Manipulation from World Models](cards.md#paper-2defaneql7) | 生成视频前锁定几何与标定参数供重建复用 |
| 具身智能 | 世界模型 | [SuperMimic: Scaling Humanoid Whole-Body Control with One Differentiable World Model](cards.md#paper-psnqjklvok) | 用共享可微动力学为多动作跟踪提供解析梯度 |
| 具身智能 | 探索初始化 | [Combining Constrained Sampling and Reinforcement Learning for Manipulation](cards.md#paper-cjgmjqlgz5) | 按接触模式覆盖设计训练重置分布 |
| 具身智能 | 阻抗控制 | [Constraint-Decomposed Impedance Control from Generative Policy for Articulated Object Manipulation](cards.md#paper-mjpidvjnms) | 用生成策略样本估计可动方向并设各向异性阻抗 |
| 具身智能 | 失败诊断 | [Demystifying When and Why VLAs Fail in Contact-Rich Tasks and How to Fix Them](cards.md#paper-bv0t1o1zil) | 先区分流匹配精度失败与力反馈失败，再分别修正 |
| 具身智能 | 多模态融合 | [FingerEye: Learning Dexterous Manipulation with Continuous Vision-Tactile Sensing](cards.md#paper-raa96lpixj) | 按指尖传感组组织特征以抑制单模态捷径 |
| 具身智能 | 策略后训练 | [Never Too Late for Force: Accelerating VLA Post-Training with Reactive Force Injection](cards.md#paper-19iadsbo9a) | 以零初始化力注意力在保留原技能时加入接触反应 |
| 具身智能 | 触觉表示 | [Visible Touch: Rendering Contact for Visuomotor Policies](cards.md#paper-ult1vxdeub) | 把接触信号放入现有视觉模型使用的空间参考系 |
| 具身智能 | 混合动力学 | [Learning Physics-Guided Residual Dynamics for Deformable Object Simulation](cards.md#paper-3hsq75gmr9) | 在物理骨架上学习速度残差，补足形变模拟误差 |
| 具身智能 | 几何不确定性 | [Noise-Invariant Spatial Encoding for 3D Manipulation Policies under Depth Corruption](cards.md#paper-r8moxo93mv) | 把深度位置不确定性传入注意力，避免几何 token 一律视为准确 |
| 具身智能 | 可达性代理 | [RAM: Reachability Across Morphologies](cards.md#paper-samjmur6xc) | 用形态条件化神经场替代在线逐姿态计算 |
| 具身智能 | 鲁棒规划 | [Robustness without Wrinkles: Parallel Simulation and Robust MPC for Certified Deformable Manipulation](cards.md#paper-uvjpdrcmlf) | 用实测感知误差标定可达管，并结合可微仿真规划 |
| 具身智能 | 形态优化 | [Shape Your Body: Value Gradients for Multi-Embodiment Robot Design](cards.md#paper-xho9wj1ggt) | 冻结多形态价值函数以梯度优化新机器人。 |
| 具身智能 | 失败诊断 | [WireCraft: A Simulation Benchmark for Industrial DLO Manipulation](cards.md#paper-cqpnbrggwm) | 把接近插座与接触对齐分开评估，定位视觉策略瓶颈。 |
| 具身智能 | 潜空间预测 | [LaWAM: Latent World Action Models for Efficient Dynamics-Aware Robot Policies](cards.md#paper-mw8bge8ado) | 预测视觉特征子目标以替代逐像素未来视频。 |
| 具身智能 | 推理路由 | [DIRECT: When and Where Should You Allocate Test-Time Compute in Embodied Planners?](cards.md#paper-r2uabmvwgh) | 按场景选择推理深度、模型大小或历史长度。 |
| 具身智能 | 推理预算 | [ELASTIC: Efficiently Learning to Adaptively Scale Test-Time Compute for Generative Control Policies](cards.md#paper-wxv81vb0xt) | 学习按状态同时分配去噪深度和并行候选数。 |
| 具身智能 | 蒸馏 | [W2A: Distilling World Priors into Action Models for Real-Time Robotic Control](cards.md#paper-gtazi5d0fj) | 训练期蒸馏视频去噪中间表征，推理期移除视频模型。 |
| 具身智能 | 闭环去噪 | [Catch Me If You Can: Real-Time Feedback Denoising for Responsive VLAs](cards.md#paper-7cfcazwfp6) | 预留最后去噪阶段以接入控制频率的新观测。 |
| 具身智能 | 异步连续性 | [Barrier-Constrained Guidance For Real-time Asynchronous VLA Execution](cards.md#paper-uhhneb0osw) | 对动作块交界施加逐步收紧的闭式一致性约束。 |
| 具身智能 | 离散动作生成 | [DiscreteRTC: Discrete Diffusion Policies are Natural Asynchronous Executors](cards.md#paper-lorikyekax) | 用离散扩散的原生解掩码完成异步动作补全。 |
| 具身智能 | 流式解码 | [FlashVLA: Streaming Action Decoding for Fast and Asynchronous VLA Inference](cards.md#paper-05ne8s5e7i) | 让错开噪声级别的若干动作块在同一前向中推进。 |
| 具身智能 | 噪声选择 | [Start Right, Arrive Right: Asynchronous Execution via Initial Noise Selection](cards.md#paper-9ih6ylxhi5) | 通过反推初始噪声对齐前缀，保留原流生成路径。 |
| 具身智能 | 动态预测 | [F2F-AP: Flow-to-Future Asynchronous Policy for Real-time Dynamic Manipulation](cards.md#paper-ixjwiekme1) | 异步推理用预期执行时刻的视觉特征替代过时观察。 |
| 具身智能 | 异步多模态 | [DAM-VLA: Decoupled Asynchronous Multimodal Vision Language Action model](cards.md#paper-mr4l9laugj) | 每种传感器按自身频率刷新潜变量缓存。 |
| 具身智能 | 设计诊断 | [How to Build an Efficient VLA: A Design Space Study for Modular Vision-Language-Action Models](cards.md#paper-pprwdhxw93) | 先扫描动作头初始化，再决定模块扩容。 |
| 具身智能 | 在线调度 | [Action Chunk Scheduling for Batched Robot Policy Serving](cards.md#paper-2vstg6wu2p) | 按各机器人动作块消费速度分配 GPU 排队优先级。 |
| 具身智能 | 压缩诊断 | [Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered](cards.md#paper-zylula1tsy) | 剪枝后测试安全和成功，并用权重空间校正尝试恢复。 |
| 具身智能 | 部署评测 | [The Speedup Paradox: Rethinking Inference Optimization in Embodied Tasks](cards.md#paper-vxuazhduwe) | 按闭环完成时间选推理优化 |
| 具身智能 | 模型压缩 | [AgileDP: Quantizing Diffusion Policy via Dynamic Scaling and Reweighted Distillation](cards.md#paper-gr9nftftjn) | 按去噪时步动态缩放量化 |
| 具身智能 | 架构设计 | [What Do You Need for Compositional Generalization in Diffusion Planning?](cards.md#paper-hbhr1gxas0) | 扩散规划骨干优先测试平移等变和局部感受野 |
| 具身智能 | 推理控制 | [VLS: Steering Pretrained Robot Policies via Vision–Language Models](cards.md#paper-rmp7m64fq6) | 用三维关键点上的可导任务目标引导冻结策略去噪 |
| 具身智能 | 任务结构 | [Inference-Time Robot Behavior Steering through Physically-Aware Reconfiguration of Task-Structure](cards.md#paper-nceeehy8d5) | 用户偏好用自动机组合，保持连续控制器冻结 |
| 具身智能 | 策略适配 | [Proxy Policy Steering](cards.md#paper-tfc6lmd02z) | 通过两个代理的速度差隔离任务监督的动作改变量 |
| 具身智能 | 离线强化学习 | [AWLS: Advantage-Weighted Latent Steering for One-Step Generative Robotic Manipulation Policies](cards.md#paper-z35bac5jbe) | 冻结单步生成器，用优势加权监督训练噪声残差 |
| 具身智能 | 训练监督 | [CounterAlign: Counterfactual Supervision for Vision-Language-Action Models](cards.md#paper-ay4totylcx) | 把正确动作配错指令形成离线奖励负例 |
| 具身智能 | 跨本体迁移 | [Cloak: Zero-Shot Cross-Embodiment Manipulation by Masking the End-Effector from the VLA](cards.md#paper-7kv78k8rcv) | 抹去腕部画面中的末端外观以检验跨机械手迁移 |
| 具身智能 | 表示对齐 | [UniLatent: Cross-Embodiment Transfer via Latent Observation Alignment](cards.md#paper-s3fvtypvnz) | 用仿真配对观测对齐编码器替代图像翻译 |
| 具身智能 | 机制解释 | [Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models](cards.md#paper-lfugzn8an2) | 用跨回合可复用性与因果干预测试 VLA 内部特征 |
| 具身智能 / 模仿学习 | 流匹配推理 | [Improving Robotic Generalist Policies via Flow Reversal Steering](cards.md#paper-ahph1ngaup) | 用粗动作反求噪声，再生成邻近的预训练行为模式。 |
| 具身智能 / 多模态 | 表示对齐 | [Relational Spatial Alignment for Vision-Language-Action Models](cards.md#paper-p1r9ibkyv4) | 注入三维先验时，对齐成对空间关系并监控特征有效秩。 |
| 具身智能 / 多模态 | 空间查询 | [GeoAlign: Beyond Semantics with State-Guided Spatial Alignment in VLA Models](cards.md#paper-am3agfollh) | 用机器人状态查询几何特征，避免在每个动作阶段输入同一组静态空间 token。 |
| 具身智能 / 规划 | 迁移诊断 | [To Route or to Adapt? Multi-Expert Diffusion Planners in Unseen Regions](cards.md#paper-pjuqx9kbg5) | 先用 oracle 测现有专家的路由收益上限，若上限低则将预算用在目标域适配。 |
| 具身智能 | 世界模型 | [PhysCoRe: Physics-Corrected Residual World Models for Material-Aware Deformable Dynamics](cards.md#paper-go08puaqia) | 先辨识可解释物性，再拟合解析模拟器的系统残差 |
| 具身智能 | 系统辨识 | [Wiggle and Go! System Identification for Zero-Shot Dynamic Rope Manipulation](cards.md#paper-n1gnyxww2f) | 先用短时探测区分物理参数，再让多个控制任务共用辨识结果 |
| 具身智能 | 世界动作模型 | [EgoWAM: World Action Models Beyond Pixels with In-the-Wild Egocentric Human Data](cards.md#paper-efkpqttjky) | 人机联合训练时优先比较特征及三维运动预测目标 |
| 具身智能 | 模仿学习重加权 | [Graph-Reweighted Behavior Cloning with Human Interventions for Precise Robotic Manipulation](cards.md#paper-bsjuf5kla3) | 用离线图的剩余步数差筛出失败回合中的有效恢复动作 |
| 具身智能 | 生成策略 | [Unified Condition-Action Modeling for Accurate One-Step Action Generation](cards.md#paper-eiwbkqs5pz) | 将观测和时间条件与动作放进同一 token 序列，联合更新表示 |
| 具身智能 | 空间条件化 | [Spatially Conditioned Diffusion Policy: Learning Precise and Robust Manipulation with a Single RGB Camera](cards.md#paper-ey3y7lxwy1) | 在每次去噪时沿中间轨迹查询图像特征 |
| 具身智能 | 约束采样 | [BayesFP: Posterior Estimation with Flow-Based Policy Priors via Feynman-Kac Sampling](cards.md#paper-unsv9dsbfo) | 把推理期新增代价写成似然，修正现成流或扩散策略的样本 |
| 具身智能 | 探索与重训练 | [Guided Discovery of New Behaviors using Diffusion Policies](cards.md#paper-6en09r3ngp) | 针对欠覆盖行为定向采样，修复后再作为新示范 |
| 具身智能 / 机器人学习 | 扩散策略 | [Where Should Action Generation Begin? A Learnable Source Prior for Generative Robot Policies](cards.md#paper-ao1shrwa8h) | 在生成器和求解器固定时，改用状态条件的随机动作先验。 |
| 具身智能 / 机器人学习 | 策略表示 | [PRISM: Polynomial Representations for Interaction-Structured Motor Control](cards.md#paper-rqzhmvtyyy) | 给策略显式建模观测变量的乘法交互。 |
| 具身智能 / 机器人学习 | 行为表示 | [Implicit Neural Representations of Individual Behavior](cards.md#paper-0gwpqwbvhj) | 从无身份标注的多策略轨迹学习 episode 级状态动作函数。 |
| 具身智能 / 机器人学习 | 行为克隆 | [Why Does Action Chunking Improve Behavioral Cloning Performance in Robotic Control?](cards.md#paper-u56z5kqtki) | 用延迟单步策略与显式集成拆解动作分块的收益。 |
| 具身智能 / 机器人学习 | 扩散策略 | [Learning to be Different: Component Specialization for Compositional Diffusion Policies](cards.md#paper-va3t8yk04w) | 对组合去噪器的噪声预测做去相关以降低重复计入。 |
| 具身智能 / 机器人学习 | 策略编辑 | [Behavior Uncloning: Distilling Mode Redirection into Policy Weights without Inference-Time Steering](cards.md#paper-tjg1zvcdxu) | 将临时模式判别器的修正写入策略权重。 |
| 具身智能 / 机器人学习 | 持续学习 | [When Robots Sleep: Offline Skill Consolidation for Shared-Policy Robot Learning](cards.md#paper-jqaoksg9bd) | 在统一控制器中存紧凑技能替代监督，并评估技能对可靠性。 |
| 具身智能 / 机器人学习 | 价值学习 | [Beyond Monotonic Progress: Retry-Supervised Value Learning for Robot Imitation](cards.md#paper-5fzzu1zwzg) | 用重试关键点监督非单调价值，保留有用纠错片段。 |
| 具身智能 / 机器人学习 | 推理剪枝 | [ACE-VLA: Action Centric Evaluation for Token Pruning in Vision-Language-Action Models](cards.md#paper-qu7v3gmydu) | 以动作梯度归因替代视觉文本注意力给视觉 token 排序。 |
| 具身智能 / 机器人学习 | 指令评测 | [RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents](cards.md#paper-a9aqjk3dat) | 让同一场景支持多条有效指令，避免视觉捷径掩盖指令忽略。 |
| 具身智能 / 机器人学习 | 模仿评测 | [The Imitator Game: Benchmarking Robot Imitative Ability Beyond Action Prediction](cards.md#paper-qh1h7ukk0k) | 把功能替代单独设为压力测试，区分轨迹复现与任务意图。 |
| 具身智能 / 机器人学习 | 故障检测 | [VLA-FAIL: Efficient Task Failure Detection for Finetuned Vision-Language-Action Models](cards.md#paper-mg7x6sfe75) | 融合特征分布偏离与预测动作块重叠区不一致，无需失败轨迹。 |
| 具身智能 / 机器人学习 | 失败恢复 | [Recover, Discover, Plan: Learning Skills and Concepts from Robot Failures](cards.md#paper-hufkyua5rr) | 从失败恢复轨迹学习关系谓词，让规划阶段主动避开同类失败。 |
| VLA / 安全 | 鲁棒训练 | [Lights, Camera, Malfunction: When Illumination Robustness Leaves VLA Models Blind to Color](cards.md#paper-7qmrpmvhzl) | 照明增强时保留颜色语义，并独立测试颜色依赖任务。 |
| 操作 / 数据 | 数据采集 | [Scale Up Strategically: Learning Compositional Generalization via Bias-Aware Evaluation and Data Collection for Robotic Manipulation](cards.md#paper-quvj7qbql6) | 按模型最不依赖的指令因子补采示范。 |
| 操作 / 评测 | 随机任务协议 | [Benchmarking Real-World Robotic Manipulation through Stochastic Challenges](cards.md#paper-mwhlzlo4ud) | 跨实验室从同一分布各自抽样，兼顾可比性和隐蔽测试。 |
| 具身智能 / 安全 | 主动评测 | [Coverage Aware Active Evaluation for Failure Discovery with Paired Systems](cards.md#paper-qji3n7jzbc) | 用少量真实试验修正便宜代理，优先测试可信且有覆盖价值的区域。 |
| 具身智能 / 评测 | 序贯统计 | [AnyRank: Reliable Anytime Policy Ranking via Sequential Testing](cards.md#paper-iou9zkasbg) | 将真机预算投向排名难区分的策略，随时输出有保证的部分排序。 |
| 操作 / VLA | 失败边界训练 | [Where Success Breaks: Failure-Boundary Learning for Robust Vision-Language-Action Models](cards.md#paper-3jf63cw3cj) | 定位失败发生的进度，用失败方向监督生成流。 |
| 具身智能 / 机器人设计 | 扩散引导 | [Transformer Transformer: A Unified Model for Motion-Conditioned Robot Co-design](cards.md#paper-ypkdkkod11) | 复用与奖励无关的动力学模型，为不同设计目标提供扩散采样引导。 |
| 具身智能 / 灵巧操作 | 形态条件化 | [DiffMorphGrasp: A Diffusion Framework Conditioned on Hand Morphology for Cross-Embodiment Grasp Generation](cards.md#paper-4soiqrxqxj) | 跨手共用规范化动作空间，但按具体运动链计算关节损失。 |
| 具身智能 / 灵巧操作 | 技能预训练 | [From Grasps to Dexterity: Large-Scale Grasp Pretraining for Dexterous Manipulation](cards.md#paper-hdnvcokmxh) | 把静态抓取标注变成低层控制预训练数据，用于操作有活动部件的工具。 |
| 具身智能 / 灵巧操作 | 交互动力学 | [ProxiDex: Learning Dynamics-Guided Proximity Policy for Dexterous Manipulation](cards.md#paper-ulcexirzjd) | 用手物距离作为硬件无关的动态状态，并随操作阶段调节其权重。 |
| 具身智能 / 灵巧操作 | 隐式几何 | [PartialBiGrasp: Inferring Hidden Local Geometry for Bimanual Grasping from Partial Views](cards.md#paper-jhewj56sh3) | 局部厚度比全形状更关乎成功时，用隐式占据推断当前不可见的抓取结构。 |
| 具身智能 / 灵巧操作 | 动作生成 | [DexHandover: Learning Bimanual Dexterous Handovers from Large-Scale Synthetic Data](cards.md#paper-zmbovwpuuw) | 先生成双手交接的共享接触状态，再将长运动优化锚定在该状态。 |
| 具身智能 / 灵巧操作 | 跨传感对齐 | [TACTX: Learning Shared Tactile Representations Across Diverse Sensors](cards.md#paper-xn8hwa4hpq) | 用同一接触事件配对不同触觉数据，使策略可直接换传感器。 |
| 具身智能 / 灵巧操作 | 跨传感预训练 | [Heterogeneous Tactile Transformer](cards.md#paper-0dopzpplvw) | 对齐触觉传感器时同时保留各模态内部可恢复信息。 |
| 具身智能 / 灵巧操作 | 跨频率融合 | [Multi-Resolution Tactile Imitation Learning for Contact-Rich Robotic Manipulation](cards.md#paper-b2gsinmx3r) | 训练时接入高频触觉，并测试在部署移除该传感器后能否保留增益。 |
| 具身智能 / 灵巧操作 | 触觉世界模型 | [Learning to Feel the Future: DreamTacVLA for Contact-Rich Manipulation](cards.md#paper-yeakwjw5xa) | 先把触觉对齐到各视觉视角对应位置，再用未来触觉监督动作。 |
| 具身智能 / 机器人学习 | 条件门控 | [FR-VLA: Implicit Force Reasoning VLA for Contact-Rich Manipulation](cards.md#paper-q1q252tit0) | 按任务阶段决定物理反馈何时进入动作头 |
| 具身智能 / 机器人学习 | 记忆机制 | [FM-VLA: Force-based Memory for Vision-Language-Action Models in Contact-Rich Manipulation](cards.md#paper-42z4ov9nrq) | 视觉难分辨重复事件时用力觉潜变量记录历史 |
| 具身智能 / 机器人学习 | 残差适配 | [OmniTacTune: Policy-Agnostic Real-World RL for Tactile Residual Adaptation of Visual Policies](cards.md#paper-vg6uymddy4) | 冻结视觉运动先验，用在线触觉策略学习局部修正 |
| 具身智能 / 机器人学习 | 跨模态监督 | [Dex-X: Learning Visual-Tactile Dexterous Manipulation From Human Demonstration with Simulated Interaction](cards.md#paper-surtjlxvxi) | 用仿真重建接触以补齐视频中缺失的触觉 |
| 具身智能 / 机器人学习 | 特权蒸馏 | [PTLD: Sim-to-Real Privileged Tactile Latent Distillation for dexterous manipulation](cards.md#paper-tjpi5d27wh) | 触觉仿真不可靠时，将真机触觉映射到仿真教师潜状态 |
| 具身智能 / 机器人学习 | 联合表征学习 | [MDF++: Visuo-Tactile World Action Model with End-to-end Representation Learning](cards.md#paper-d0ltfevdad) | 联合训练世界动作模型时用跨模态任务防潜表示坍缩 |
| 具身智能 / 机器人学习 | 推理引导 | [Inference-time Policy Steering via Vision and Touch](cards.md#paper-bc8sv8wttl) | 以视觉选长时行为模式，以触觉在短时局部编辑动作 |
| 具身智能 / 机器人学习 | 多任务强化学习 | [SkillX: Unified Multi-Skill Policy Learning for Humanoid Soccer](cards.md#paper-chcwuratwl) | 共享执行策略，让每技能使用专门价值估计与运动先验 |
| 具身智能 / 机器人学习 | 集合表示 | [S2M-Trek: From Single to Multi-Sphere Transport via Per-Frame Deep Sets on a Wheel-Legged Robot](cards.md#paper-vtsuekrcnh) | 无跨帧身份的观测先逐帧做集合池化，再读时序 |
| 具身智能 / 全身控制 | 数据生成 | [Counterfactual Video Generation Enables Scalable Humanoid Loco-Manipulation](cards.md#paper-uzalccyrvl) | 用接触锚定重建与重定向将反事实视频转成物理可行示范。 |
| 具身智能 / 全身控制 | 评测诊断 | [SIMPLE: Simulation-Based Policy Learning and Evaluation for Humanoid Loco-manipulation](cards.md#paper-artb8nigc3) | 采用模拟对真实排序的相关性作为基准验收标准。 |
| 具身智能 / 全身控制 | 合成监督 | [VLK: Learning Humanoid Loco-Manipulation from Synthetic Interactions in Reconstructed Scenes](cards.md#paper-qmafkdmtoy) | 先在重建空间用特权信息规划，再回渲染与运动同步的第一视角。 |
| 具身智能 / 全身控制 | 技能接口 | [OmniContact: Chaining Meta-Skills via Contact Flow for Generalizable Humanoid Loco-Manipulation](cards.md#paper-r27ers063s) | 用身体关键轨迹加接触开关作为分层共享接口。 |
| 具身智能 / 全身控制 | 控制覆盖 | [Humanoid Hanoi: Investigating Shared Whole-Body Control for Skill-Based Box Rearrangement](cards.md#paper-3ex2negqhp) | 用各技能闭环执行产生的状态增补共享追踪器训练。 |
| 具身智能 / 全身控制 | 交互重定向 | [Social Humanoid: Socially Responsive Human–Humanoid Interaction](cards.md#paper-hf8x30fatz) | 双人示范转人机示范时，同时调整双方以保护接触。 |
| 具身智能 / 全身控制 | 技能发现 | [MotionDisco: Motion Discovery for Extreme Humanoid Loco-manipulation](cards.md#paper-xjgz1ik29g) | 在离散接触序列上搜索，把物理验证委托给顺序轨迹优化器。 |
| 具身智能 / 全身控制 | 视觉迁移 | [LEGS: Fine-Tuning Teleop-Free VLAs for Humanoid Loco-manipulation in an Embodied Gaussian Splatting World](cards.md#paper-0jy75qydmn) | 将动作数据与场景外观分离，同一条示范按目标环境反复渲染。 |
| 具身智能 / 全身控制 | 可验证状态 | [Closing the Loop in Humanoid VLA: Persistent 3D Object Tokens for Verifiable Loco-Manipulation](cards.md#paper-e9oq6xsma9) | 让动作生成与完成判定读取同一持久物体记录。 |
| 具身智能 / 全身控制 | 触觉反馈 | [Unified Whole-Body Control for Quadrupedal Tactile-Informed Loco-Manipulation](cards.md#paper-r1fgjzlfnx) | 以触觉潜变量协调全身控制和抓力，而非维持常数大力。 |
| 具身智能 / 全身控制 | 力监督 | [WT-UMI: Tactile-based Whole-Body Manipulation via Force-Supervised Contact-Aware Planning](cards.md#paper-gkka9vehwb) | 用少量遥操作修正人类目标位姿，同时保留自然接触力监督。 |
| 具身智能 / 人形控制 | 约束控制 | [Constrained Whole-Body Tracking for Humanoid Robots](cards.md#paper-nzvfxorvoc) | 把部署后新增的约束同时施加到运动参考和底层动力学。 |
| 具身智能 / 人形控制 | 低秩适配 | [CA-GMT: Contact-Aware Low-Rank Adaptation of Motion Tracking for Whole-Body Teleoperation](cards.md#paper-u2dtqwafqo) | 只在相关动作相位施加接触适配，并以接触错误衡量收益。 |
| 具身智能 / 人形控制 | 接触控制 | [Learning Functional Compliance in Whole-body Manipulation](cards.md#paper-walhowqwnx) | 按任务方向和阶段分配柔顺性，保留关键轴上的控制权。 |
| 具身智能 / 人形控制 | 闭环规划 | [Reactive Closed-Loop Motion Planning Towards Universal Humanoid Whole-Body Control](cards.md#paper-2tjuz95jmb) | 用实际跟踪偏离的前缀训练生成规划器，并异步重规划。 |
| 具身智能 / 人形控制 | 低延迟控制 | [ExtremControl: Low-Latency Humanoid Teleoperation with Scaled Velocity Feedforward](cards.md#paper-x4i3ksa2kd) | 测量位置控制滞后，按理论比例加入缩放速度前馈。 |
| 具身智能 | 分层控制 | [HLO-AMP: Hierarchical Loco-Manipulation from Object-Aware Motion Priors](cards.md#paper-l8hoz8lovg) | 低层预训直接保留真实分布接触，高层约束在已见命令域。 |
| 具身智能 | 故障适配 | [FT-WBC: Learning Fault-Tolerant Whole-Body Control for Legged Loco-Manipulation](cards.md#paper-mjvsjnqufv) | 利用本体历史估计下肢故障，先修正上肢规划要求的底座姿态。 |
| 具身智能 | 接触控制 | [ContactMimic: Humanoid Object Interaction via Contact Control](cards.md#paper-wxbkimuzti) | 将部件接触作为独立可控命令，并打破命令与几何轨迹共线性。 |
| 具身智能 | 可微仿真 | [Learning Visuomotor Quadrotor Flight Through Dynamic Narrow Gaps via Differentiable Simulation](cards.md#paper-nwlhqecx3l) | 精度关键且动力学可微时优先对比路径梯度训练。 |
| 具身智能 | 代价表示 | [Plann3r: Predicting Planning Costs Grounded in 3D](cards.md#paper-rexyyvslbt) | 把标量图像距离换成由目标像素索引的像素级测地代价。 |
| 具身智能 | 自蒸馏 | [Training Generalist Navigation Policies via Action Self-Distillation](cards.md#paper-lwmnsycnck) | 只在训练时利用完整轨迹反推目标与推理，再让学生用机载观测预测。 |
| 具身智能 | 评测诊断 | [ATOM-Bench: A Real-World Benchmark for Atomic Skills and Compositional Generalization in Manipulation Policies](cards.md#paper-dpovq6ne2d) | 用原子能力和组合失败占比分离动作不足与组合泛化失败。 |
| 具身智能 | 主动澄清 | [Bayesian Active Learning for Intent Disambiguation in Interactive Robot Planning](cards.md#paper-el4edbhqcg) | 用具身任务规范候选的信息增益挑澄清问题，再交由可验证规划器。 |
| 具身智能 | 不确定性 | [Control-Ready Uncertainty for Trajectory Diffusion](cards.md#paper-c9tcchtvcs) | 蒸馏扩散分数曲率，输出可在线使用的逐步协方差。 |
| 具身智能 | 可微优化 | [Scalable Deep Unfolding of Conic Optimizers](cards.md#paper-csya6ohdle) | 按矩阵向量积实现隐式反传，并稳定处理重复特征值 |
| 具身智能 | 在线建图 | [Anchor3R: Streaming 3D Reconstruction with Transient Anchors for Long-Horizon Visual Mapping](cards.md#paper-q53aygo2ie) | 以当前帧局部坐标预测，再通过运动图对齐长期轨迹 |
| 具身智能 | 约束生成 | [Collaborative Planning for UAV-UGV Teams under Operational Constraints via Masked Error-bounded Neuro-Symbolic Diffusion](cards.md#paper-lsrxdurldg) | 在符号约束过滤之后计算熵并决定掩码解码顺序 |
| 具身智能 | 时间规划 | [OSCAR: Obstacle Survival Curves for Adaptive Robot Navigation](cards.md#paper-hr2fyfod4n) | 用类别条件清障生存曲线估计应等多久再绕行 |
| 具身智能 / 强化学习 | 安全约束 | [SCoCaT: Success Conditioned Constrained Reinforcement Learning for Spacecraft Docking](cards.md#paper-suv5pudsyi) | 给终止式约束强化学习加成功价值监督。 |
| 具身智能 / 模仿学习 | 风险监督 | [TRIAD Planner : Three-Level Robust Imitation Learning for Autonomous Driving](cards.md#paper-98pbd92mei) | 在模仿训练中用尾部风险调整多模态候选监督，部署保持相同开销。 |
| 具身智能 / 世界模型 | 层级规划 | [Hierarchical Planning with Latent World Models](cards.md#paper-zts11nhglq) | 用同一潜空间连接不同时间尺度的预测模型做 MPC。 |
| 具身智能 / 世界模型 | 失败监督 | [FACT: Failure-Aware Causal Training for World-Action Models](cards.md#paper-yrnlvjcapo) | 用实际动作与失败后果训练进度预测，抑制成功偏置。 |
| 具身智能 / 世界模型 | 推理筛选 | [τ0-WM: A Unified Video-Action World Model for Robotic Manipulation](cards.md#paper-qvol1xoutn) | 以重去噪一致性先排序，只对低质量动作候选调用后果模拟。 |
| 具身智能 / 世界模型 | 动作编码 | [TAPESTRY: A Single Backbone for Video Generation and Robot Control](cards.md#paper-ailv1lyfxf) | 把动作投影成单个视频块 token，复用视频骨干并做单步动作推理。 |
| 具身智能 / 世界模型 | 条件分解 | [AnyWorld: Factorized Egocentric World Models for Cross-Embodiment Generalization](cards.md#paper-0w0ylgezd5) | 独立调节动作、视角与本体生成同一交互的机器人数据。 |
| 具身智能 / 世界模型 | 频域编码 | [From Video Frames to Robot Meta-Frames: A Unified Latent Interface for World Action Models](cards.md#paper-nbdd4rvq5q) | 用冻结去噪器诊断机器人变量编码是否贴合视频先验。 |
| 具身智能 / 世界模型 | 表征诊断 | [What Makes Video World Model Latents Action-Relevant: Prediction over Reconstruction](cards.md#paper-lsfm8tzuh2) | 用逆动力学探针选择视频表示，不以像素重构质量代替动作可恢复性。 |
| 具身智能 / 世界模型 | 三维对齐 | [GSWAM: A Unified Gaussian World Action Model for Robotic Manipulation](cards.md#paper-u5pojpnj6j) | 在共享三维锚空间内建模动作和场景，并对两类变量使用不同流时间步。 |
| 具身智能 / 世界模型 | 刚体动力学 | [ORD-WM: Learning Object-Centric Rigid Dynamics for 3D World Modeling in Robotic Manipulation](cards.md#paper-xhjeeyhkhy) | 预测逐物体刚体变换并解析作用在潜变量上，避免多步几何漂移。 |
| 具身智能 / 世界模型 | 时序诊断 | [Understanding and Mitigating the Video-Action Generalization Gap via Temporal Ratio](cards.md#paper-mlf6dhhbnf) | 监控动作头对未来潜变量的依赖，只在适合的阶段增强视频引导。 |
| 具身智能 / 多模态 | 辅助监督 | [Pri4R: Learning World Dynamics for Vision-Language-Action Models with Privileged 4D Representation](cards.md#paper-8yqfxyof0y) | 训练时预测未来三维点轨迹，部署时移除预测头。 |
| 具身智能 / 世界模型 | 延迟补偿 | [Intercepting the Future: Latent-Space Predictive World Model for Dynamic VLA Manipulation](cards.md#paper-ddzwaomwze) | 在冻结 VLA 前预测预计执行时刻的视觉 token，并按不确定性截断预测。 |
| 具身智能 / 世界模型 | 测试时适配 | [WAM-TTT: Steering World-Action Models by Watching Human Play at Test Time](cards.md#paper-ox3ertz3rv) | 测试时用未标注人类视频更新小型记忆，保持动作世界模型冻结。 |
| 具身智能 / 多模态 | 训练重采样 | [Enhancing Robotic Control Robustness through Generative Visual Model](cards.md#paper-e5lvpa2glx) | 在固定合成量下对照按控制表现重加权与静态混合。 |
| 具身智能 / 世界模型 | 数据策略 | [PlayWorld: Learning Robot World Models from Autonomous Play Data](cards.md#paper-hatezfmdn5) | 预留数据预算采集非任务自由交互，并以固定模型比较反事实动作泛化。 |
| 具身智能 / 强化学习 | 梯度估计 | [Coupled Local and Global World Models for Efficient First Order RL](cards.md#paper-zdglinpebl) | 将前向保真和反传成本分开，用局部代理验证优化方向。 |
| 具身智能 / 世界模型 | 安全诊断 | [How Well Do Latent World Models Understand Partially Observable Safety Constraints?](cards.md#paper-587eukwa7d) | 先区分观测缺失与预测失准，再选择增传感监督或风险校准。 |
| 具身智能 / 模仿学习 | 动作对齐 | [Imitation from Heterogeneous Demonstrations using Grounded Latent-Action World Models](cards.md#paper-rlsvfgv1ps) | 以环境效果对齐异构动作，再独立检测目标本体解码可行性。 |
| 具身智能 / 规划 | 符号建模 | [STRIPS-WM: Learning Grounded Propositional STRIPS-style World Models from Images](cards.md#paper-fvphddjumi) | 用动作前提和后效评价压缩表征是否保留规划信息。 |
| 具身智能 / 世界模型 | 三维轨迹 | [μ0: A Scalable 3D Interaction-Trace World Model](cards.md#paper-shbmwdrpvu) | 用稀疏三维交互轨迹作跨本体条件，对照像素预测的计算和效果。 |
| 具身智能 / 世界模型 | 推理缓存 | [C³ache: Accelerating World Action Models with Cross Inference Chunk Cache](cards.md#paper-t3iohvur0r) | 同时比较块内和跨块缓存，在急转接触场景单独测失效。 |
| 具身智能 / 世界模型 | 关键帧生成 | [SKIP: Sparse Keyframe Interpolation Paradigm for Efficient Embodied World Models](cards.md#paper-hgrivs5qzu) | 做视频压缩生成时按事件选锚点并测下游学习，而不只测画质。 |
| 具身智能 / 世界模型 | 数据采集 | [Training Controllable World Models via Action Influence Maximization](cards.md#paper-oocwc3dn5d) | 采集时主动覆盖同一状态下多类动作，以反事实对照测试模型是否服从动作。 |
| 具身智能 / 世界模型 | 故障诊断 | [Adaptive World-Models for Anomaly Recognition (AWARE): A Framework for Robot Dynamics Prediction and Introspection](cards.md#paper-994ptkadnu) | 用可解释动力学参数区分观测噪声与设备退化，并分开测检测和定位。 |
| 具身智能 / 灵巧操作 | 重定向 | [AnyDexRT: Calibration-Efficient Dexterous Hand Retargeting with Few-Shot Human Guidance](cards.md#paper-dyonmedjxv) | 把少量人工指导放在操作相关接触附近，与全空间均匀校准对照。 |
| 具身智能 | 重定向 | [TopoRetarget: Interaction-centric retarget for dexterous manipulation](cards.md#paper-9w3pec3xlg) | 保持手物局部拓扑 |
| 具身智能 | 奖励设计 | [Learning Dexterous Manipulation Using Contact Wrench Guidance From Human Demonstration](cards.md#paper-depcm83k5i) | 在物体受力空间比较人机演示 |
| 具身智能 | 主动感知 | [ActiveMimic: Egocentric Video Pretraining with Active Perception](cards.md#paper-j5rzynkq8z) | 把相机运动视作可学习动作 |
| 具身智能 | 动作表示 | [AdvDex: Learning Dexterous Manipulation from Human Demonstrations via Joint-Aligned Actions and Adversarial Learning](cards.md#paper-tswzwxgz5p) | 共享腕姿与手指动作后，消去视觉本体信息 |
| 具身智能 | 数据筛选 | [VISTA: Vision-Grounded and Physics-Validated Adaptation of UMI data for VLA Training](cards.md#paper-xagvjptxtr) | 训练前按目标本体的轨迹可执行性筛选人类示范 |
| 具身智能 | 偏好学习 | [Freeform Preference Learning for Robotic Manipulation](cards.md#paper-fylym2c6xc) | 将整体偏好拆成可命名的多个质量轴 |
| 具身智能 | 分层优化 | [Beyond the End-Effector: Learning Whole-Arm Contact Manipulation from Human Demonstrations](cards.md#paper-c08kkstfex) | 把非末端接触定义与机器人的接触连杆选择解耦 |
| 具身智能 | 数据配比 | [Human-like autonomy emerges from self-play and a pinch of human data](cards.md#paper-lovzujpkxn) | 以少量人类轨迹打破自博弈形成的不兼容约定 |
| 具身智能 | 策略优化 | [Efficient On-policy Visual-RL via Stochastic Decoupled Policy Gradient](cards.md#paper-c7bvd59rpp) | 渲染预算受限时用轨迹随机扰动估计策略梯度 |
| 具身智能 | 策略优化 | [FlowDPG: Deterministic Policy Gradient on Flow Matching Policies for Real-World Manipulation](cards.md#paper-wv9xf5ii7l) | 用 critic 梯度监督流速度场，省去跨 ODE 步反传 |
| 具身智能 | 偏好优化 | [FlowPRO: Reward-Free Fine-Tuning of Flow-Matching VLAs via Proximalized Preference Optimization](cards.md#paper-ftx97rpoow) | 显式约束隐式奖励的绝对大小，并用干预回滚形成偏好对 |
| 具身智能 | 强化学习后训练 | [RoboFFT: Finetuning generative robot policy via online reinforcement learning with forward process](cards.md#paper-efjcm9am0o) | 用正向加噪构造 PPO 替代比率。 |
| 具身智能 | 强化学习后训练 | [Optimal Transport Q-Learning for Flow Policy Steering and Acceleration](cards.md#paper-uni5vigrgr) | 用优势加权条件最优传输同时优化流策略和推理步数。 |
| 具身智能 | 相对进度监督 | [WARP-RM: A Warp-Augmented Relative Progress Reward Model for Data Curation](cards.md#paper-yaym35u9su) | 用变速和逆序构造有符号进度来加权动作块。 |
| 具身智能 | 主动感知 | [Learning Decomposed Visibility for Efficient Active Exploration of Cluttered Scenes](cards.md#paper-qgk0k192w6) | 把换视角和推动分别预测，再用统一可见性收益选模式。 |
| 具身智能 | 干预后训练 | [TUTOR: Learning Recovery from Policy-Induced Deviations](cards.md#paper-gusryiaaen) | 把人工接管前轨迹拆成保留与抑制信号。 |
| 具身智能 | 噪声条件训练 | [Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics](cards.md#paper-sh0dg0hwvk) | 按扩散噪声水平限制次优示范的贡献。 |
| 具身智能 | 监督路由 | [Supervise What Survives: Geometry-Guided VLA Adaptation from Synthetic Robot Videos](cards.md#paper-dfblf2ss7m) | 只以生成视频监督视觉几何，不用伪动作监督控制头。 |
| 具身智能 | 生成表示 | [ArticFlow: Action-Conditioned Flow Matching for Skeleton-Free Articulated Generation](cards.md#paper-xxnpkl2igd) | 用形状潜流和动作条件点流分开建模拓扑变化与形变。 |
| 具身智能 | 策略搜索 | [ExpertGen: Scalable Sim-to-Real Expert Policy Learning from Imperfect Behavior Priors](cards.md#paper-gk8bvfszq3) | 冻结扩散去噪器，只在初始噪声空间做稀疏奖励强化学习。 |
| 具身智能 / 多模态 | 标注校准 | [SPARC: Reliable Spatial Annotations from Robot Demonstrations at Scale](cards.md#paper-gx5xey9ade) | 用操作阶段和跨帧一致性校准空间伪标签，再按精度要求选择训练样本。 |
| 具身智能 / 模仿学习 | 主动数据采集 | [GUILD: Guided Iterative Data Collection for Imitation Learning](cards.md#paper-6txmwx1wih) | 在采集前用任务归因反馈选择下一批遥操数据。 |
| 具身智能 / 模仿学习 | 多动作监督 | [CrowdMAPS: Crowdsourcing Multiple Actions per State for Real-World Robot Imitation Learning](cards.md#paper-gvdqtvona1) | 为已访问状态标注多个可行动作，和继续采集新轨迹比较标注收益。 |
| 具身智能 | 数据归因 | [ATHENA: Accelerated Multi-Task Heterogeneous Influence Functions for Robot Data Curation](cards.md#paper-dpgz9kssgo) | 在多任务 VLA 上用可扩展影响估计筛选示范 |
| 具身智能 | 仿真设计 | [Active Generative Simulation: Meta-Learning What to Simulate for Sim-and-Real Policy Co-Training](cards.md#paper-xxhkql5u5p) | 用少量真实验证反馈学习模拟器采样分布 |
| 具身智能 | 损失重加权 | [Where Small Mistakes Matter: Quantifying State Criticality for Imitation Learning](cards.md#paper-x05rf7l7h4) | 按小动作误差造成的下游价值损失给示范状态加权 |
| 具身智能 | 测试时适配 | [Scouting the Dynamics Gap: Test-Time Policy Adaptation via Action-Outcome Feedback](cards.md#paper-fyntpa7rwn) | 用动作结果预测误差在线更新共享动力学信念 |
| 具身智能 | 系统辨识 | [Drifting on Demand: A Profiled-Likelihood Transformer for Online Parameter Estimation](cards.md#paper-zwuhb2fawb) | 状态残差各通道尺度变化时分离动力学参数与噪声估计 |
| 具身智能 | 物性估计 | [Beyond Semantic Classes: Online Physical Parameter Estimation via Embedding-Conditioned Gaussian Mixtures](cards.md#paper-y6pog6ygix) | 按连续视觉嵌入检索交互历史并保留物性多峰分布 |
| 具身智能 | 动力学正则 | [Sensitivity Shaping for Latent Modeling](cards.md#paper-kggi0115rg) | 拟合动力学时在高支持区域保留局部控制敏感性 |
| 具身智能 | 生成式策略 | [Learning Robust Visuomotor Policies via Dynamics Alignment](cards.md#paper-cautgdv8l0) | 让动作流与未来观测流在采样时交互更新 |
| 具身智能 | 等变模仿 | [MIRROR: Reflecting Hidden Symmetries from Offline Robot Interaction Data](cards.md#paper-glj2rsqis4) | 从离线转移联合学习观测和动作的群作用 |
| 具身智能 | 强化学习后训练 | [ADEPT: Accelerating Dexterity via Pre-Training and Post-Training using Reinforcement Learning](cards.md#paper-2qcsjfv9pr) | 新奖励下先冻结 actor 暖启动 critic，再保守更新 |
| 具身智能 | 行为动力学 | [Going with the Flow: Koopman Behavioral Models as Pseudo Planners for Visuo-Motor Dexterity](cards.md#paper-8t3fxlyk9k) | 以预测视觉流与实际偏差触发按需重规划 |
| 具身智能 | 空间对齐 | [Dexterity-BEV: Aligning 3D World and Actions for Generalizable Robot Policies Learning](cards.md#paper-z5cgs0xgek) | 把每个相机像素对应几何和动作统一到规范鸟瞰坐标 |
| 具身智能 | 异步策略 | [LiMA: Bridging Long-term Imagination to Real-time Dexterous Manipulation via Asynchronous Diffusion](cards.md#paper-fsgxevflkn) | 用熵正则桥将低频意图约束传给高频控制 |
| 具身智能 | 风险塑形 | [How to Learn from What a Human Would Avoid? Intervention-Aware World Models with Real-World RL for Dexterous Manipulation](cards.md#paper-lgosjtsr5q) | 把人类接管的预测概率作为 actor 的前瞻风险代价 |
| 具身智能 | 依赖图规划 | [Minimal-Intervention Target Retrieval in Cluttered Scenes with Grasp-Conditioned Dependency Graphs](cards.md#paper-ng11daafix) | 按候选抓取和动作阶段预测真正的阻挡对象 |
| 具身智能 | 视觉蒸馏 | [Anchoring Attention in Clutter: Mask-Guided Latent Distillation for Vision-Language-Action Towards Dexterous Grasping](cards.md#paper-fgyol5tngl) | 把训练期区域掩膜变成控制路径内的注意力监督 |
| 具身智能 | 触觉表示 | [Learning with Object-centric Representations of Tactile Interactive Perception for Robot Manipulation](cards.md#paper-s0rbnmokit) | 从探索过程选择少量表征片段，将物性上下文提供给操作策略 |
| 具身智能 | 示范采集 | [What is the Better Curriculum: Controller-Shaped Grasping Behavior for Contact Force-Sensitive Manipulation](cards.md#paper-f3dic5djnz) | 用触觉反射在线修正示范 |
| 具身智能 | 视觉表征 | [Robot-DIFT: Correspondence-Sensitive Diffusion Features for Contact-Rich Robot Manipulation](cards.md#paper-zshxqqyhfn) | 用蒸馏保留稠密对应，再比较多尺度读出 |
| 具身智能 | 等变表示 | [Equivariant Visual-Tactile Diffusion Policy for Contact-Rich Manipulation](cards.md#paper-40csfpl2cq) | 用末端姿态旋转共享视触球谐表示 |
| 具身智能 | 柔顺控制 | [TDC: Sim-to-Real Transferable Directional Compliance for Contact-Rich Manipulation](cards.md#paper-lomft7cfyl) | 从仿真迁移柔顺方向，现场调幅度 |
| 具身智能 | 候选规划 | [DexFLEX: Contact-Aware Foundation Controller for Command-Guided Dexterity](cards.md#paper-kduigyxutd) | 以预测的接触稳定性筛选上游动作草案 |
| 具身智能 | 动作接口 | [Mind the Gap: Rethinking I/O Design for Contact-Rich Visuomotor Policy Learning](cards.md#paper-patsmtswir) | 同时条件化执行状态和领导器命令，预测未来命令 |
| 具身智能 | 探索奖励 | [Tactile Curiosity Drives Robot Interaction](cards.md#paper-h26amtgnfu) | 把好奇心奖励限制到触觉不确定性 |
| 具身智能 | 失败诊断 | [KlaskTron-IL: A Contact-Rich Adversarial Imitation Learning Benchmark with a Validated Sim-to-Real Bridge](cards.md#paper-ik1sflqgza) | 同时检查判别器语义准确性和用于优化的梯度 |
| 具身智能 | 世界模型 | [FACA: Force-Aware Contact Adaptation for Task-Parameterized Robotic Assembly](cards.md#paper-ch33xueibo) | 分开已知装配参数与在线隐式接触残差 |
| 具身智能 | 价值估计 | [MorFiC: Fixing Value Miscalibration for Zero-Shot Quadruped Transfer](cards.md#paper-x7qoq3qota) | 在 critic 用乘法形态条件化避免跨本体价值平均 |
| 具身智能 | 世界模型 | [Morphology-Conditioned World Model for Cross-Embodiment Quadrupedal Locomotion](cards.md#paper-yqoallpdd3) | 把形态描述输入动力学而不仅是 actor |
| 具身智能 | 对称增强 | [SSR: Scaling Surefooted and Symmetric Humanoid Traversal Toward the Open World](cards.md#paper-4it3fcnny2) | 在潜空间做双侧等变增强，并提前判断摆脚支撑 |
| 具身智能 | 特权蒸馏 | [Perceptive Behavior Foundation Model: Adapting Human Motion Priors to Robot-Centric Terrain](cards.md#paper-c5oil7jqbq) | 部署保留原始动作指令，仅用地形残差在局部修正 |
| 具身智能 | 轨迹蒸馏 | [SOLO: Stable Omni-terrain Long-Horizon Perceptive Humanoid Locomotion](cards.md#paper-jwkaxdmqkb) | 把下一状态的师生分歧放进 RL 奖励 |
| 具身智能 | 传感回退 | [PROOF: Perceptive Robustness via Out-of-Distribution Fallback for Legged Locomotion](cards.md#paper-317szv2vus) | 训练本体感知回退，并以外感不确定性抑制受损特征 |
| 具身智能 | 结构化动作 | [HAF-VLA: Hierarchical Action Flow Framework for Humanoid Vision-Language-Action Control](cards.md#paper-l9rkfeukrc) | 按移动、腰部和操作顺序细化同一全身动作 |
| 具身智能 | 候选验证 | [TEXEDO : Test Time Scaling for Controller-aware Language-conditioned Humanoid Motion Generation](cards.md#paper-uscrywxsuc) | 先硬筛动态可行，再按语言匹配排序 |
| 具身智能 / 腿式控制 | 本体动力学 | [HumanoidNDM: Closing the Training-Deployment Gap of Motion Tracking via Humanoid Neural Dynamics Model](cards.md#paper-xcdyj95l5p) | 按适应强度低频扰动参考，结合可微正运动学训练历史动力学，再通过模型梯度微调 |
| 具身智能 / 腿式控制 | 动力学适配 | [FADA: Few-Shot Domain Adaptation via Dynamics Alignment for Humanoid Control](cards.md#paper-mmrhlrwlfx) | 用 DAgger 蒸馏特权教师为规划器和逆动力学，部署仅微调逆模型 |
| 具身智能 / 腿式控制 | 残差辨识 | [Unsupervised Actuator Networks as a Residual World Model for Humanoid Control](cards.md#paper-8klpl3fxjn) | 从本体传感对齐浮基速度及接触力，再开环回放辨识执行器残差 |
| 具身智能 / 腿式控制 | 平衡表示 | [Koopman DCM: Unstable Eigenfunctions as Data-driven Representations for Legged Balancing](cards.md#paper-mday00wzfr) | 从测量历史寻找不稳定 Koopman 特征函数并按控制耦合正则化 |
| 具身智能 / 腿式控制 | 动力学课程 | [Actuator Dynamics Curricula for Narrow-Viability Tasks in Legged Robot Learning](cards.md#paper-mru8ihzsqr) | 从高刚度开始并按完成时长逐步退火到辨识刚度 |
| 具身智能 / 腿式控制 | 课程学习 | [Trajectory-Level Automatic Curriculum Learning for Legged Locomotion on Unstructured Terrain](cards.md#paper-0muj0bxujh) | 按当前策略学习轨迹难度，迭代引导地图上的轨迹采样 |
| 具身智能 / 腿式控制 | 表示诊断 | [Mind the Phase: Effective Rank and Representation Health in Legged Locomotion](cards.md#paper-fk33gnkkgf) | 按摆动和支撑分别统计雅可比有效秩，比较归一化及残差结构 |
| 具身智能 / 腿式控制 | 奖励设计 | [Push the Limit: Learning High-Speed Sprinting and Aggressive Cornering on a Full-Scale Humanoid](cards.md#paper-xqgbzwsuxt) | 用低频速度方向取代瞬时偏航率目标，辅以时序注意力与技能条件判别器 |
| 具身智能 / 腿式控制 | 专家优化 | [MAPO: Mixture of Experts with Alternating Policy Optimization for Universal Humanoid Motion Tracking](cards.md#paper-tk1gtgoesr) | 交替更新专家与路由器以避免同步更新混淆 |
| 具身智能 / 腿式控制 | 柔顺控制 | [CHIP: Adaptive Compliance for Humanoid Control through Hindsight Perturbation](cards.md#paper-gqmj7sik5q) | 事后按扰动改写稀疏目标，保留稠密参考 |
| 具身智能 / 腿式控制 | 安全值学习 | [λ-Reachability: Geometric-Horizon Safety Bellman Equations for Humanoid Safety](cards.md#paper-siyferhqrn) | 采用几何分布的随机预测长度与概率吸收终点，构造多步安全值估计 |
| 具身智能 / 导航与驾驶 | 开闭环诊断 | [BridgeSim: Unveiling the OL-CL Gap in End-to-End Autonomous Driving](cards.md#paper-ynmzwxz68a) | 分别分析观测偏移与目标错配，并在测试时校准偏移、值偏差和时间一致性 |
| 具身智能 / 导航与驾驶 | 仿真度量 | [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](cards.md#paper-lqur3gxkdh) | 在多个公开策略的场景特征空间测 Fréchet 距离 |
| 具身智能 / 导航与驾驶 | 可验证元动作 | [DriveMA: Driving Vision-Language-Action Models with verifiable Meta-Actions](cards.md#paper-b7gccztjye) | 以规则从轨迹抽取并核验元动作，指导监督训练和轮次信用分配 |
| 具身智能 / 导航与驾驶 | 瓶颈监督 | [NTR: Neural Token Reconstruction for Scene Token Bottleneck in End-to-End Driving](cards.md#paper-f4ib3mxhbo) | 只允许解码器读取场景 token 重建掩蔽图块潜变量，推理时移除重建组件 |
| 具身智能 / 导航与驾驶 | 可解释诊断 | [Mechanistic Interpretability for End-to-End Self-Driving](cards.md#paper-bqxys2gkba) | 用稀疏自编码器提取特征，以配对反事实编辑和激活干预区分关联与因果 |
| 具身智能 / 导航与驾驶 | 动作表示 | [CoFL-S: Spatially Queryable Sector Flow Fields for Local Language-Conditioned Navigation](cards.md#paper-hi8mv09noi) | 预测可查询的方位扇区流场，从原轨迹构造逐帧子指令和流监督 |
| 具身智能 / 导航与驾驶 | 序贯判断 | [Observe Before You Alert: Belief-State Driver Alerting with Vision–Language Models](cards.md#paper-g6vrrbo3ne) | 增加内部观察动作，按需累计证据再告警，以结构化安全证据池化为信念 |
| 具身智能 / 导航与驾驶 | 剪枝时点 | [Before Parc Fermé: RL-Time Pruning for Efficient Embodied LLMs in Autonomous Driving](cards.md#paper-jydy4anb01) | 在 RL 训练仍有任务反馈时分阶段裁剪，也可提前在 SFT 裁剪一部分 |
| 具身智能 / 导航与驾驶 | 计算路由 | [An Adaptive Slow-Fast Framework for Real-Time Anomaly Detection in Autonomous Driving](cards.md#paper-egz6ymfvzu) | 以快速 LiDAR 异常检测常开，按碰撞时间切换昂贵语义推理 |
| 具身智能 / 导航与驾驶 | 推理预算 | [FlashDrive: Flash Vision-Language-Action Inference Framework for Autonomous Driving](cards.md#paper-sdujbb3p4e) | 跨帧复用缓存、对推理 token 并行预测，按去噪速度变化缓存步进 |
| 具身智能 / 导航与驾驶 | 规划蒸馏 | [VIGOR-MPC: Vision-Guided Objective Regulation MPC](cards.md#paper-alu9elt93i) | 从特权长时教师蒸馏视觉条件的代价参数，让短时 MPC 保留控制结构 |
