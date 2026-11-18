# CoRL 2026

[首页](../../README.md) · [官方录用名单](https://2026.corl.org/program/accepted-papers)

已筛选 **687 / 687** 篇，当前收录 **640** 篇。[筛选底册](papers.tsv)录用名单按 OpenReview 论文 ID 去重。通过收录门槛的论文进入后续统一评分，保留比例上限为 50%。

| 领域 | 技术类型 | 论文卡 | 能改变的技术选择 |
| --- | --- | --- | --- |
| 具身智能 | 数据策略 | [Diagnosing Compositional Generalization in Sequential Robot Tasks](cards.md#paper-gqfyim5djy) | 示范预算固定时，优先覆盖决定动作的指令组合 |
| 具身智能 | 推理与部署 | [EmbodiSteer](cards.md#paper-2z8xqxrlsy) | 在扩散采样中处理目标机器人的全身约束 |
| 具身智能 / Agent | 推理与部署 | [Learning What to Say to Your VLA](cards.md#paper-z47bcul4zk) | 用校准门槛决定何时改写指令并保留回退 |
| 具身智能 / 多模态 | 记忆与表征 | [MEM](cards.md#paper-5tiity1fk3) | 分开保留近期视频与长时语义事件 |
| 具身智能 / 多模态 | 推理与部署 | [When Vision Overrides Language](cards.md#paper-hmdwoezjlq) | 固定画面替换指令，分测语言落地和成功率 |
| 具身智能 | 时序表征 | [TEMPO](cards.md#paper-fvzkpmphv8) | 分别用场景运动和本体历史解决两类单帧歧义 |
| 具身智能 | 数据策略 | [FAKTUAL](cards.md#paper-tscng5wcwn) | 固定示范预算下按轨迹核熵选样 |
| 具身智能 | 评测与诊断 | [ZETA](cards.md#paper-4rljgpefph) | 分开评估目标本体完全未见和预训练已见 |
| 具身智能 / 多模态 | 表征学习 | [Semantic Anchoring for Robotic Action Representations](cards.md#paper-ytw6loo9c5) | 微调时分开保护可迁移语义与动作专有信息 |
| 具身智能 / Agent | 长时记忆 | [RoboTTT](cards.md#paper-nhe9q2cz1n) | 用快速权重压缩长历史并做上下文长度对照 |
| 具身智能 / 多模态 | 推理与部署 | [MolmoAct2-Think](cards.md#paper-q6xwlhyg6x) | 按区域变化决定何时重算深度 token |
| 具身智能 / 多模态 | 训练目标 | [PRTS](cards.md#paper-qwpni3blwt) | 把离线轨迹的目标可达性作为 VLA 辅助目标 |
| 具身智能 / 多模态 | 训练数据与条件化 | [π0.7](cards.md#paper-5xkfwwrw0v) | 混用低质轨迹时显式标注执行策略和质量 |
| 具身智能 / 多模态 | 世界模型 | [DreamZero](cards.md#paper-bshs9hddiu) | 联合预测视频和动作，并用实测帧更新下一步上下文 |
| 具身智能 / 多模态 | 评测与诊断 | [What Are We Actually Benchmarking in Robot Manipulation?](cards.md#paper-rdvh11pafj) | 用缺失目标能力的探针和受控扰动检验基准能否支持能力声明 |
| 具身智能 / 多模态 | 数据策略 | [MolmoB0T](cards.md#paper-c4z0y8gvni) | 用固定视角对照区分相机覆盖与仿真数据收益 |
| 具身智能 | 策略优化 | [Chunk-wise Model-based Policy Optimization](cards.md#paper-dngzli0slv) | 训练时用一次前向评估整段动作的价值 |
| 具身智能 / 多模态 | 动作生成 | [Diffusion ReRoll](cards.md#paper-hbux1fe8bl) | 采样时给已去噪片段保留利用后续上下文修订的机会 |
| 具身智能 / 多模态 | 推理与部署 | [EagleVLA](cards.md#paper-ockqyiy2qm) | 用未来状态预测对齐异步动作起点并动态分配调用预算 |
| 具身智能 / 多模态 | 量化与部署 | [BitVLA](cards.md#paper-mhcqiruihi) | 将视觉编码器也纳入极低位训练和整机内存对照 |
| 具身智能 / 多模态 | 动作生成 | [REACT](cards.md#paper-ffb8qnjwv2) | 跨观测修订未执行动作块兼顾连续性与反应 |
| 具身智能 | 策略优化 | [TARC](cards.md#paper-wvr13crtrf) | 将动作保持时间纳入策略输出并约束控制切换次数 |
| 具身智能 / 多模态 | 世界模型 | [Mem-World](cards.md#paper-f9grq4ncx9) | 按动态表面元素检索腕部视角历史 |
| 具身智能 | 世界模型 | [MoRE](cards.md#paper-v24do7joun) | 用交互历史显式路由到不同物理运动专家 |
| 具身智能 / 多模态 | 表征学习 | [SPARK](cards.md#paper-jenvgujqrb) | 让单帧紧凑特征预测未来局部，同时保留冻结教师语义 |
| 具身智能 / 多模态 | 训练目标 | [FlowVLA](cards.md#paper-zadtlinund) | 用训练期三维点位移和工具中心位移共同监督二维策略 |
| 强化学习 | 策略优化 | [FedGuide](cards.md#paper-qbaa8svaik) | 按行为分布聚合异构客户端而非直接混合策略参数 |
| 具身智能 / 多模态 | 模型架构 | [CoRE-VLA](cards.md#paper-qku6lifnpu) | 分开用传感器可用性与任务意图路由专家 |
| 具身智能 / 多模态 | 感知路由 | [FocusVLA](cards.md#paper-3m39fmw8mx) | 按预测交互阶段调整全局相机与腕部相机的权重 |
| 具身智能 | 动作表示 | [DualSpace-VLA](cards.md#paper-x2mryigshj) | 用末端位移监督动作意图并直接生成关节轨迹 |
| 具身智能 / 多模态 | 动作表示 | [X-Tokenizer](cards.md#paper-mg3ebtsbig) | 按量化层区分动作意图与运动细节 |
| 具身智能 | 动作表示 | [Neural Action Codec](cards.md#paper-uhnmcdamca) | 借用神经音频编解码结构时按运动信号重选重建损失 |
| 具身智能 / 多模态 | 动作表示 | [ActionCodec](cards.md#paper-wrlegprnvr) | 用下游训练难度和闭环指标一起选动作 tokenizer |
| 具身智能 / 多模态 | 三维表征 | [GeomVLA](cards.md#paper-hvkifhmhcm) | 让场景、未来运动和动作共用机器人坐标系 |
| 具身智能 / 多模态 | 三维表征 | [SAGE-3D](cards.md#paper-z04kxywc6v) | 用任务语义组织深度特征再调制动作头 |
| 具身智能 / 多模态 | 动作生成 | [TBD-VLA](cards.md#paper-vy6u0drx88) | 块间按时间自回归，块内并行生成离散动作 |
| 具身智能 / Agent | 动作规划 | [Coarse-to-Control](cards.md#paper-tegllxbrcu) | 先在执行词表内预测粗动作计划，再细化为可执行动作 |
| 具身智能 / Agent | 动作规划 | [ThinkingVLA](cards.md#paper-fgwkovhmqe) | 先预测子目标画面，再根据画面推断如何达到它 |
| 具身智能 / 多模态 | 世界模型 | [Unified Motion Action Model](cards.md#paper-efgcnzgmvn) | 用可切换的掩码统一物体运动预测与机器人控制 |
| 具身智能 / 多模态 | 动作表示 | [ELA](cards.md#paper-iy5oceldef) | 用下游控制与解码目标一起训练视频潜动作 |
| 具身智能 / 多模态 | 动作表示 | [HARP-VLA](cards.md#paper-ghx1d6pqur) | 用少量配对示范对齐人机视觉后再混训潜动作 |
| 具身智能 / 多模态 | 表征学习 | [FIBERTUNE](cards.md#paper-ynhgrgatuy) | 将动作可预测方向滤除后再蒸馏视觉残差 |
| 具身智能 / 多模态 | 动作表示 | [AC-LAM](cards.md#paper-03qrtmw4qx) | 通过跨时间可加约束减少潜动作对场景外观的依赖 |
| 具身智能 / 多模态 | 动作表示 | [PoLAR](cards.md#paper-jkop9l6myq) | 显式分开潜动作的变化幅度与变化类别 |
| 具身智能 / 多模态 | 表征学习 | [DILL](cards.md#paper-xnidgatbx7) | 用跨域一致的未来表征监督策略 |
| 具身智能 / 多模态 | 感知路由 | [Artificial Foveated Perception](cards.md#paper-ijncc1oznj) | 用任务条件掩码暴露并压低无关视觉证据 |
| 具身智能 / Agent | 策略接口 | [See Less, Specify More](cards.md#paper-rykaehgzzo) | 保留全局目标，另给执行器局部指令和显式视觉预算 |
| 具身智能 / 多模态 | 感知路由 | [ThinkProprio](cards.md#paper-u620dzd51n) | 用离散本体状态和指令在主干计算前筛选视觉片段 |
| 具身智能 / 多模态 | 表征学习 | [GeoProp](cards.md#paper-rce4amkjbq) | 用运动学投影把本体状态对准同位置的视觉特征 |
| 具身智能 / 多模态 | 感知路由 | [FocusPool](cards.md#paper-1ukisrjcvt) | 用当前本体状态在 CNN 中间特征上选择性汇聚 |
| 具身智能 / 多模态 | 感知路由 | [Seeker](cards.md#paper-afq9dtkp09) | 用动作监督学习随任务进度变化的感兴趣区域 |
| 具身智能 / 多模态 | 时序表征 | [MotionVLA](cards.md#paper-okjnhtluoa) | 以连续轨迹场表示历史而非独立堆叠帧 |
| 具身智能 / 多模态 | 传感器融合 | [MoSS](cards.md#paper-wkrawikmug) | 为力觉、触觉与力矩建立独立传感流并预测未来反馈 |
| 具身智能 | 持续学习 | [LIFELONGVLA](cards.md#paper-0hncthl4fw) | 分开短期适配和长期巩固并限制回放存储 |
| 具身智能 / Agent | 长时记忆 | [TRACE](cards.md#paper-apppmsjzb5) | 用已执行轨迹给早期视觉证据建立检索键 |
| 具身智能 / Agent | 长时记忆 | [Gated Memory Policy](cards.md#paper-tzm6j864lf) | 让策略选择何时读取历史并训练其容忍错误历史动作 |
| 具身智能 / 多模态 | 长时记忆 | [EventVLA](cards.md#paper-8fgh4qadnb) | 在视觉证据消失前预测其未来价值并决定是否写入 |
| 具身智能 / Agent | 任务规划 | [LoHo-Manip](cards.md#paper-n31eeof0k3) | 让高层每轮重算剩余步骤并用二维轨迹指引短程执行 |
| 具身智能 / Agent | 长时记忆 | [Chameleon](cards.md#paper-ttj3uxlcxl) | 在最终画面相同的条件下分测记忆决策和实际执行 |
| 具身智能 / 多模态 | 长时记忆 | [NativeMEM](cards.md#paper-hjv9yhbgxr) | 复用视觉编码器将每帧每视角压成一个记忆 token |
| 具身智能 / Agent | 长时记忆 | [MessyMem](cards.md#paper-gqqwqejrtq) | 将交互得知的属性与关键帧绑定到可更新场景图 |
| 具身智能 / Agent | 长时记忆 | [Workspace Models](cards.md#paper-aposmvav9y) | 把任务显著性标注搬到训练并蒸馏成潜工作记忆 |
| 具身智能 / Agent | 评测与诊断 | [ARMS](cards.md#paper-ndhpq86ixs) | 用不中断的并发任务检验按手臂记录的自行动历史 |
| 具身智能 | 持续学习 | [Memory Anchors](cards.md#paper-dsbthpqfj9) | 回放优先保留与新任务表征近但动作冲突的旧样本 |
| 具身智能 / 多模态 | 世界模型 | [Light-WAM](cards.md#paper-kb0ko1wife) | 将未来视频监督留在低分辨率潜空间，用跨层融合头一次输出动作块 |
| 具身智能 / 多模态 | 世界模型 | [WLA-0](cards.md#paper-oihlruloiq) | 用共享查询吸收未来预测监督并按需启用显式预测 |
| 具身智能 | 数据策略 | [RoboPocket](cards.md#paper-thg2jwuii6) | 采集时先显示当前策略的预测轨迹，再补失败附近的示范 |
| 具身智能 / Agent | 偏好学习 | [IMPLIED](cards.md#paper-qxboq98qn4) | 把固定规则推导的偏好标签当作可更新的先验 |
| 具身智能 / Agent | 评测与诊断 | [Learning to Assist](cards.md#paper-79jc3quhgp) | 检查动作块是否跨过人类尚未准备好的协作边界 |
| 具身智能 / Agent | 多机器人协作 | [CHORUS](cards.md#paper-mwjwaq0cxt) | 复用同一预训练控制器并用机器人身份提示区分执行角色 |
| 具身智能 / 多模态 | 安全评测 | [TouchSafeBench](cards.md#paper-hvarz6f8ea) | 分开测当前接触与提前预警，并按碰撞对象分层 |
| 具身智能 | 表征学习 | [STARS](cards.md#paper-rayg2mjka5) | 先在时空交互图上自监督，再用少量社会行为标签训练读出头 |
| 具身智能 / Agent | 偏好学习 | [Asking Smarter Questions](cards.md#paper-hfhtppdbyr) | 针对示范中监督不足的奖励特征生成并解释偏好问题 |
| 具身智能 / 强化学习 | 策略优化 | [PIVOT](cards.md#paper-2vx7i6arps) | 在流匹配后训练中按带符号优势吸引或排斥部署数据 |
| 具身智能 / 强化学习 | 策略优化 | [Learning While Deploying](cards.md#paper-656ph9mvla) | 用共享部署经验估计分布价值，再提取流策略 |
| 具身智能 / 强化学习 | 策略优化 | [DIQL](cards.md#paper-vvdyxlghxh) | 根据数据支持程度按状态选择乐观分位 |
| 具身智能 / 强化学习 | 策略优化 | [Robo-ValueRL](cards.md#paper-qx5mpyixvi) | 用全局任务进度和局部动作排序分别诊断价值函数 |
| 具身智能 / 强化学习 | 策略优化 | [TIGER](cards.md#paper-az2ojk8zxd) | 用模仿策略提供末端任务进度奖励而非直接执行其动作 |
| 具身智能 / 强化学习 | 策略优化 | [UniIntervene](cards.md#paper-ar3ewq6mh4) | 用近期价值趋势触发恢复，并从历史干预中找恢复目标 |
| 具身智能 / 强化学习 | 策略优化 | [Preference-calibrated Actor-Critic Training](cards.md#paper-tpevwyct8w) | 给人工接管前的低效片段重新分配回报 |
| 具身智能 / 强化学习 | 偏好学习 | [DCCP](cards.md#paper-pnsqn6bng7) | 固定同一观测前缀，只替换第一动作块来形成局部偏好 |
| 具身智能 / 多模态 | 奖励设计 | [TOPReward](cards.md#paper-zdnuar0gmn) | 用视频语言模型的完成判断概率作为零样本进度信号 |
| 具身智能 / 强化学习 | 奖励设计 | [RARM](cards.md#paper-aan8ouehwo) | 按单条参考示范匹配进度并在低置信时抑制奖励 |
| 具身智能 / 强化学习 | 奖励设计 | [HiRE](cards.md#paper-0ua1khfiud) | 用成功与失败轨迹回看并修正误导控制的进度奖励 |
| 具身智能 / 强化学习 | 策略优化 | [EXPO-FT](cards.md#paper-u3nmrhun8b) | 动作块中只覆盖人工纠正的时间段并保存实际执行块 |
| 具身智能 / Agent | 任务规划 | [M³P-R1](cards.md#paper-gfxjqzvsnd) | 让模型生成可由求解器验证的规划约束 |
| 具身智能 | 示范采集 | [PAKT](cards.md#paper-2vdrocnuih) | 采集时约束人工引导轨迹以匹配部署执行接口 |
| 具身智能 / 强化学习 | 数据策略 | [Scaling Sim-to-Real VLA RL with Generative 3D Worlds](cards.md#paper-z5mgc1ggjp) | 用生成式交互场景增加微调时的环境覆盖 |
| 具身智能 / Agent | 训练策略 | [R³](cards.md#paper-9i9dpyr2f9) | 用离线动作评分训练生成自由文本指导的高层模型 |
| 具身智能 / 强化学习 | 策略优化 | [Q-OIL](cards.md#paper-9seu2keixr) | 用真实停滞干预数据校准模拟人类，并重访有信息的状态 |
| 具身智能 / 强化学习 | 课程学习 | [Success Guided Sampling](cards.md#paper-mqdt80qztp) | 按当前成功率筛选训练起点与任务配置 |
| 具身智能 / 强化学习 | 部署适配 | [TERRA](cards.md#paper-w443fvglzc) | 按预测的任务相关模型误差选择部署时采样路线 |
| 具身智能 / 多模态 | 动作生成 | [SlotFlow](cards.md#paper-dkrgzycdrv) | 为基于历史动作的低步数流模型分开编码物体语义和几何位置 |
| 具身智能 | 推理与部署 | [One-step action generation](cards.md#paper-4dqrad2snp) | 部署前先试同一流策略的一步积分再决定是否蒸馏 |
| 具身智能 | 示范采集 | [GLIDE](cards.md#paper-jnehlrywtz) | 从采集失败归纳状态约束并在部署阶段复用 |
| 具身智能 / Agent | 动作规划 | [BiCICLe](cards.md#paper-blqynefrlp) | 把双臂预测拆为有条件的先后决策 |
| 具身智能 / 多模态 | 长时记忆 | [MemoryVAM](cards.md#paper-aitdchsctw) | 给视频预测和动作解码提供同一份压缩事件记忆 |
| 具身智能 / Agent | 多机器人协作 | [Learning Coordinated Visuomotor Box-Pushing from Solo Demonstrations](cards.md#paper-gpc0ncixhz) | 分开测试单机示范能传授什么以及协作数据仍缺什么 |
| 具身智能 / 多模态 | 推理与部署 | [OmniGuide](cards.md#paper-pewwdul10x) | 用统一三维能量接口接入不同来源的空间引导 |
| 具身智能 / 多模态 | 表征学习 | [SFHand](cards.md#paper-p8h2wzh2tw) | 用人手未来三维运动作为人类视频的预训练监督 |
| 具身智能 / 强化学习 | 策略优化 | [MERL](cards.md#paper-0pthtaiwpd) | 按世界模型可靠性调整想象比例、长度和样本权重 |
| 具身智能 / Agent | 长时记忆 | [Procedural Assistance Memory](cards.md#paper-nxfwmrzxzz) | 把个性化帮助规则写成可修订的事件状态机 |
| 具身智能 / 多模态 | 动作表示 | [Being-H0.5](cards.md#paper-cfzfrojmka) | 用语义槽复用人机动作数据，同时将执行分给本体专家 |
| 具身智能 / 强化学习 | 偏好学习 | [PAWN](cards.md#paper-kcefeylouw) | 在同一动作块内按运动模式组织局部偏好 |
| 具身智能 / 多模态 | 训练策略 | [ABC](cards.md#paper-qd6clcx6qy) | 一次视觉语言前向复用多个扩散噪声和时间样本 |
| 具身智能 | 动作生成 | [Mixture of Frames Policy](cards.md#paper-f5329hhiji) | 在同一去噪过程中融合不同参考系的预测 |
| 具身智能 / 多模态 | 传感器融合 | [GeoHAT](cards.md#paper-qhndjmxgs1) | 仅在深度可信的位置向视觉主干注入三维特征 |
| 具身智能 / 多模态 | 感知路由 | [InCoM](cards.md#paper-nfz7om0vwz) | 按潜在运动意图重加权移动操作的多尺度视觉特征 |
| 具身智能 / 强化学习 | 部署适配 | [HiRe-MoMa](cards.md#paper-orkjlylohv) | 用单向条件耦合底座和臂的残差更新 |
| 具身智能 / Agent | 安全评测 | [SafeMem](cards.md#paper-rnp2bj4rux) | 将视野外的历史危险纳入候选动作审核 |
| 具身智能 / Agent | 数据策略 | [AIDA-OWMM](cards.md#paper-4m7c3psa78) | 直接用部署时可用的观测和技能接口采教师示范 |
| 具身智能 / 多模态 | 空间表征 | [RoboMAP](cards.md#paper-xohvcwilyj) | 对具有多个可行位置的指令输出稠密空间得分图 |
| 具身智能 / Agent | 表征学习 | [A4D](cards.md#paper-8qefjwsgyu) | 用功能距离触发可供性发现 |
| 具身智能 / 多模态 | 三维表征 | [Phase-Conditioned Affordance Fields](cards.md#paper-zhig7xb56d) | 随操作阶段改变等变策略的局部参考点 |
| 具身智能 / 多模态 | 空间表征 | [GROW²](cards.md#paper-kglogzktyq) | 通过部件语义把工具选择与三维接触定位分开 |
| 具身智能 / 多模态 | 空间表征 | [VoxAfford](cards.md#paper-umhg65uhcy) | 在开放词表 token 生成后补入多尺度体素几何 |
| 具身智能 / Agent | 任务规划 | [VoLo](cards.md#paper-sf3yzbbtnx) | 允许监控器在动作执行中打断和更换技能 |
| 具身智能 / Agent | 任务规划 | [NovaPlan](cards.md#paper-5cxsyqajns) | 在执行前筛视频候选并按执行偏差做局部修复 |
| 具身智能 / 多模态 | 数据策略 | [SimHum](cards.md#paper-cvpjguuatq) | 让仿真提供机器人动作监督，让人类视频提供真实视觉经验 |
| 具身智能 | 动作表示 | [BiRoAD](cards.md#paper-keuuzk1rsd) | 将双臂表示分为交换不变的协调部分与随角色交换改变的部分 |
| 具身智能 / 多模态 | 接触控制 | [CoStream](cards.md#paper-wentff2rks) | 比较持续融合动作建议与按阶段切换控制器 |
| 具身智能 | 模仿学习 | [COWBOY](cards.md#paper-84ea2xep60) | 将场景相关到达与局部物体交互分开生成教学轨迹 |
| 具身智能 | 动作表示 | [Foci Policy](cards.md#paper-aztnrtznof) | 只学习关键交互时段内的物体间相对运动 |
| 具身智能 / 强化学习 | 策略优化 | [Interaction-weighted Resampling](cards.md#paper-qlhhholka7) | 在接触改变动力学的前中后阶段重新分配对比样本 |
| 具身智能 / 多模态 | 数据增强 | [SIDO](cards.md#paper-mqly5j6pnd) | 用静态示范合成指向未来物体位姿的动作块 |
| 具身智能 / 多模态 | 扩散策略 | [Compositional Diffusion Policy for Vision–Language–Action Agents](cards.md#paper-y55ijjxmsh) | 将动作生成的任务语义和可微物理约束分开建模，以便测试未见任务组合。 |
| 具身智能 / 多模态 | 评测与诊断 | [RoboAffect: Egocentric Emotion Reasoning for Robot Companions in Shared Viewing](cards.md#paper-xwoyo2bpcl) | 测量机器人视角采集对多模态任务的性能损失，据此决定是否采集视角匹配的训练数据。 |
| 具身智能 / 强化学习 | 策略优化 | [Self-play is not enough: human imitation improves self-play autonomy in the wild](cards.md#paper-s8ziyian3z) | 在自博弈策略部署前，测试用真人日志修正行为分布，同时用冻结策略 KL 约束保留原有能力。 |
| 具身智能 / 机器人学习 | 数据采集 | [SuperSuit: An Isomorphic Bimodal Interface for Scalable Mobile Manipulation](cards.md#paper-penaq22jh1) | 设计共享的关节增量动作接口，使穿戴示范和遥操作数据能在同一策略中混用。 |
| 具身智能 / 规划 | 启发式搜索 | [REAP: Learning General Rearrangement Heuristics from Motion-Planner Feedback](cards.md#paper-pax622bsf6) | 用运动规划器反馈训练符号搜索启发式，减少昂贵的几何查询。 |
| 具身智能 / 多模态 | 视觉表示 | [ReSiReg: Towards Spatially Consistent Semantics in Language-Conditioned Robotic Tasks](cards.md#paper-1hqdyvwaxi) | 用空间稳定的中间特征重建开放词汇定位图。 |
| 具身智能 / 多模态 | 异步控制 | [AsyncVLA: An Asynchronous VLA for Fast and Robust Navigation on the Edge](cards.md#paper-jimwz6u93i) | 远端模型提供语义引导，边缘适配器持续按新观测修正动作。 |
| 具身智能 / 多模态 | 表示对齐 | [LCLA: Language-Conditioned Latent Alignment for Vision-Language Navigation](cards.md#paper-av4ykymvpx) | 迁移导航控制时让新感知适配冻结专家的内部状态。 |
| 具身智能 / 世界模型 | 扩散策略 | [WAM-Nav: Asymmetric Latent World-Action Modeling for Unified Visual Navigation](cards.md#paper-pjzsychbzg) | 联合生成长动作与短视觉预测，减少为远期控制生成远期视觉的成本。 |
| 具身智能 / 多模态 | 空间表示 | [SPAN-Nav: Generalized Spatial Awareness for Embodied Navigation](cards.md#paper-nykpeymvbg) | 利用真值占据学习空间决策，再用自预测占据训练以缩小部署差距。 |
| 具身智能 / 多模态 | 代价建模 | [G2-Nav: Grounded and Guarded Vision-Language Costmaps for Robot Social Navigation](cards.md#paper-1zwj66605w) | 将 VLM 的社会约束转成空间代价，交给独立规划器与高频安全检查。 |
| 具身智能 / 规划 | 采样策略 | [Self-supervised Dispersive Sampling for Quadrotor Motion Planning](cards.md#paper-8xayrudune) | 根据控制经动力学映射后的状态覆盖训练采样器。 |
| 具身智能 / 导航 | 代价建模 | [Scaled Preference Conditioning for Terrain Costmap Generation](cards.md#paper-5m9zsorosa) | 把任务偏好作为代价图生成的显式输入，任务切换时更新偏好向量。 |
| 具身智能 / 导航 | 偏好学习 | [From Imitation to Alignment: Human-Preference Flow Policies for Long-Horizon Sidewalk Navigation](cards.md#paper-dkaxe3v6uu) | 优先采集人工接管片段，测试它们能否修正模仿策略在困难状态下的行为。 |
| 具身智能 / 导航 | 评测与诊断 | [TopoUrbanBench: Group-Structural Compliance Evaluation for Urban Robot Navigation](cards.md#paper-1jcoslxzhb) | 评测社会导航时同时统计轨迹是否穿越队列或人群交互区域。 |
| 具身智能 / 导航 | 关系建模 | [GRACE: Group-Aware Socially Compliant Visual Navigation in Human Environments](cards.md#paper-7tcspsbyzb) | 用群体空间监督感知并重加权生成轨迹，以减少穿越交互区域。 |
| 具身智能 / 多智能体 | 不确定性建模 | [CoopUQ: Robust Multi-Robot Social Navigation via Uncertainty-Aware Cooperative Forecasting](cards.md#paper-da5vpqa7g7) | 把多机器人协作预测的不确定性纳入策略代价，在遮挡下主动避开未知高风险区域。 |
| 具身智能 / 世界模型 | 不确定性建模 | [Schrödinger's Navigator: Imagining an Ensemble of Futures for Zero-Shot Object Navigation](cards.md#paper-forrdaq3mz) | 遮挡严重时按候选轨迹生成多种可能观测，再聚合价值选路。 |
| 具身智能 / 规划 | 观测设计 | [Task-Aware Environment Augmentation for Reliable Navigation via Shielded Conditional Diffusion](cards.md#paper-odfnfgiie3) | 把有限的定位标记布在即将出现高风险定位误差的路段。 |
| 具身智能 / 导航 | 评测与诊断 | [NavVerse: Benchmarking Indoor-to-Outdoor Embodied Navigation in Continuous Robot Simulation](cards.md#paper-0rvhggryjx) | 把室内外边界穿越加入连续执行评测，并分别记录成功、效率与安全。 |
| 具身智能 / 多模态 | 空间表示 | [PathPainter: Transferring the Generalization Ability of Image Generation Models to Embodied Navigation](cards.md#paper-sal8urvt1f) | 让图像生成模型在鸟瞰图上输出可通行掩码，用跨视角定位将全局先验接入局部规划器。 |
| 具身智能 / Agent | 记忆机制 | [GLST: Global-Local Spatio-Temporal Memory Decomposition Framework for Online Chained-Goal Navigation](cards.md#paper-xyfvvmlqro) | 为目标动态变化的任务分别保留全局探索历史和局部短期执行状态。 |
| 具身智能 / 世界模型 | 安全决策 | [SafeDriveVLA: Navigation-Conditioned World Model Dreaming for Conflict-Aware End-to-End Autonomous Driving](cards.md#paper-7vjpgj7x2b) | 在语言条件动作生成前预测场景冲突，用条件未来预测辅助判断指令可行性。 |
| 具身智能 / 多模态 | 决策接口 | [PIGEON: VLM-Driven Object Navigation via Points of Interest Selection](cards.md#paper-a1wg3rqdsr) | 把航点和原始观测绑定为可验证的任务候选，交给 VLM 稀疏选择。 |
| 具身智能 / 多模态 | 示范监督 | [IntentNav: Learning Spatial-Visual Object Navigation from Human Demonstrations](cards.md#paper-6rjsxvcnhb) | 用示范未来片段反推当前搜索目标，为高层候选选择生成监督。 |
| 具身智能 / 世界模型 | 预测与规划 | [One-Step World Models for Multi-Modal Goal Navigation](cards.md#paper-fuxtpvfynh) | 在固定控制预算下，一次并行预测候选轨迹的未来帧。 |
| 具身智能 / 多模态 | 示范增强 | [Teaching Robots Like Dogs: Learning Navigation in Cluttered Scenes from Luring, Gesture, and Speech](cards.md#paper-g2ja89f1e8) | 重建少量真实示范场景后注入扰动，补充原示范缺少的恢复行为。 |
| 具身智能 / 导航 | 评测与诊断 | [CostNav: A Navigation Benchmark for Real-World Economic-Cost Evaluation of Physical AI Agents](cards.md#paper-qbninlimrj) | 选导航传感器与控制器时，同时比较服务达标和每次运行的边际收益。 |
| 具身智能 / 多模态 | 空间表示 | [One Agent to Guide Them All: Empowering MLLMs for Vision-and-Language Navigation via Explicit World Representation](cards.md#paper-bxqv3kn5ql) | 让多模态规划器按需查询度量世界状态，并由状态层约束动作可执行性。 |
| 具身智能 / 多模态 | 不确定性校准 | [CoSMO: Conformal Semantic Mapping for Open-World Safe Robot Navigation](cards.md#paper-ptqogquuch) | 先校准开放词汇危险类别预测集合，再按语义风险扩张避障区域。 |
| 具身智能 / 规划 | 代价建模 | [CoGeL: Constraint-to-Geometry Learning from Demonstrations and Failures for Safe Long-Horizon Robot Navigation](cards.md#paper-xm8lpylbxa) | 将从干预和失败学来的局部风险直接写入用于长程规划的目标距离。 |
| 具身智能 / 多智能体 | 约束强化学习 | [Prioritized Multi-Constraint Coordination for Safe Multi-Robot Formation Navigation](cards.md#paper-dyo8vc0zyk) | 将避碰与编队变形赋予不同优先级，并让分布式 actor 感知当前预算。 |
| 具身智能 / 规划 | 风险控制 | [Adaptive Risk-Certified Event-Triggered Replanning for Dynamic Navigation](cards.md#paper-xyrbf93mwh) | 用未来轨迹的尾部风险触发换规划模式，同时保留下一步安全过滤。 |
| 具身智能 / 多智能体 | 分层规划 | [Navigating the Clutter: Waypoint-Based Bi-Level Planning for Multi-Robot Systems](cards.md#paper-60tpxlifym) | 以路点定义可验证的低层规划输出，并把运动可行性反馈给任务规划器。 |
| 具身智能 / 强化学习 | 扩散策略 | [X-NavDP: Generalizing Navigation Diffusion Policy to Novel Behavior and Embodiments with Group Q-score Reweighted Matching](cards.md#paper-c0ygolwl7i) | 用同状态的轨迹 Q 分组归一化来加权 score matching，后训练扩散策略。 |
| 具身智能 / 导航 | 策略适配 | [PathLift: Depth-Conditioned Metric Lifting for Visual-Navigation Priors](cards.md#paper-rwx9gcsvjh) | 用传感器深度逐路点校正预训练策略输出的无尺度路径。 |
| 具身智能 / 多模态 | 主动感知 | [LIME: Learning Intent-aware Camera Motion from Egocentric Video](cards.md#paper-erptr7eec1) | 从被动视频构造意图、预期观测和相对位姿监督，学习按需移动相机。 |
| 具身智能 / 多模态 | 场景配准 | [PROSE: Training-Free Egocentric Scene Registration with Vision-Language Models](cards.md#paper-5onzck6sbr) | 用语义候选加几何共识，配准仅部分重叠的自视角 RGB 扫描。 |
| 具身智能 / 视觉 | 几何监督 | [Geometry-Aware Absolute Pose Regression via Geometric Pose Proxy](cards.md#paper-whavgmiwj3) | 在绝对位姿回归中预测含透视约束的中间表示，并在几何空间增强视角。 |
| 具身智能 / 定位 | 位姿估计 | [FreeLoc: Online Floorplan Localization via Diffusion-Aided Pose Refinement](cards.md#paper-usrlwzdtic) | 将平面图作为可在线查询的地图，用候选位姿做连续精修与时间融合。 |
| 具身智能 / 视觉 | 特征匹配 | [CoReMatch: Recurrent Continuous Coordinate Refinement for Real-Time Robotic Feature Matching](cards.md#paper-ojmvvfkk6t) | 在连续坐标中迭代修正对应点，以低分辨率特征保留几何精度。 |
| 具身智能 / 视觉 | 推理缓存 | [LateMatch: Breaking the Interaction Bottleneck via Cacheable Matching for Efficient Visual Localization](cards.md#paper-a9tbpzfswi) | 延迟跨输入交互，让重复使用的单图特征可预计算并缓存。 |
| 具身智能 / 视觉 | 多视角表示 | [G2G: Exploiting Intra-Group Geometry for Inter-Group Pose Estimation](cards.md#paper-33h7bchfgi) | 冻结组内几何编码，只训练轻量的跨组交互和位姿头。 |
| 具身智能 / 视觉 | 几何校准 | [LSPR: Init-Anchored Score-Based Multi-Camera Calibration for Indoor Robot Manipulation](cards.md#paper-2aoavwqgc6) | 学习强初始化器的局部标定误差，并在置信度低时回退至原估计。 |
| 具身智能 / 多智能体 | 特征融合 | [CoLA: Robust Collaborative Perception with Linear Global Spatial Alignment](cards.md#paper-ffiovlfrqn) | 位姿和延迟误差可能超出局部融合窗口时，比较线性复杂度的全局对齐。 |
| 具身智能 / 视觉 | 监督去偏 | [OptiGeo: Efficient Monocular Geometry for Embodied Perception in Optically Challenging Scenes](cards.md#paper-7bckvvmpuj) | 对已知会失效的传感器区域，引入干净几何监督而非直接拟合传感器读数。 |
| 具身智能 / 视觉 | 物体表示 | [3PTv2: Zero-Shot 3D-Object Perception Transformer for Robotics](cards.md#paper-wnz4dr57js) | 用贯穿网络的物体 token 联合检测、分割与位姿估计，减少框级级联误差。 |
| 具身智能 / 多模态 | 跨模态生成 | [Cyclops: LiDAR as a Camera That Dreams in Color](cards.md#paper-mnggg9cnbh) | 低照度时测试由 LiDAR 合成 RGB 后复用现有视觉模型是否可靠。 |
| 具身智能 / 定位 | 状态估计 | [MaD-PF: Modular and Differentiable Particle Filter for Cross-Environment SE(3) LiDAR Localization](cards.md#paper-l8atlvewkt) | 保留粒子多假设，分别评估可微运动、观测及重采样模块的迁移和耗时。 |
| 具身智能 / 视觉 | 自动标注 | [AmodalBox: Automated 3D Bounding Box Annotation under Partial Visibility](cards.md#paper-0o1c1xxn1m) | 稀疏点云只覆盖局部时，以图像生成的完整几何作为伪标签先验。 |
| 具身智能 / 定位 | 场景图 | [Functional-SLAM: Interaction-Aware Mapping with Online Functional Scene Graphs](cards.md#paper-9gwuac6oum) | 在线积累物体功能关系，将稳定拓扑作为额外闭环线索。 |
| 具身智能 / 强化学习 | 偏好学习 | [How to Peel with a Knife: Aligning Fine-Grained Manipulation with Human Preference](cards.md#paper-dzazfcpuip) | 对质量连续且主观的接触任务，在力感知模仿后用定量指标和人类偏好共同微调。 |
| 具身智能 / 多模态 | 候选生成 | [Reactive Task-Oriented Robot-Human Handovers via Generative Hypothesis Selection](cards.md#paper-vnf3d7ia9y) | 先离线或低频生成多个任务相关交互候选，再按实时人体状态选择。 |
| 具身智能 / 强化学习 | 辅助控制 | [AI Coaching for Accelerating Human Skill Development with Reinforcement Learning](cards.md#paper-m0zqqi9lfr) | 辅助训练系统以撤掉辅助后的独立能力为目标，并允许用户经历有助于学习的失败。 |
| 具身智能 / 强化学习 | 技能组合 | [Telescopes are Optomechanical Robots: Training Compositional Visuomotor Policies for Coordinated Control](cards.md#paper-rs2instahx) | 高自由度控制难以端到端训练时，切成低自由度子技能并在共享反馈下组合。 |
| 具身智能 / 视觉 | 在线建图 | [RoMo-GS: Efficient Online 3D Gaussian Splatting for Robot Mapping via Exposure-Integrated Motion Blur](cards.md#paper-1j0hw81jy9) | 按曝光时间解析积分运动中的高斯投影，避免逐子帧渲染。 |
| 具身智能 / 定位 | 自监督状态估计 | [Learning Contact Representation for Leg Odometry](cards.md#paper-4uxhlsonz5) | 用连续支撑信念调整滤波噪声，并按里程计误差选择接触表征。 |
| 具身智能 / 定位 | 等变表示 | [GINIO: A Geometric SO(3)-Equivariant Interface for Neural Inertial Odometry](cards.md#paper-nl8ibtm3mt) | 要求学习测量的均值与协方差都按传感器安装旋转正确变换。 |
| 具身智能 / 定位 | 系统辨识 | [PLATO: Preintegration-Based Likelihood Maximization from Accurate Trajectory Observations for Neural Inertial Odometry](cards.md#paper-awvlnorxds) | 用训练期精确轨迹联合估计偏置动力学与惯性噪声协方差。 |
| 具身智能 / 多模态 | 概率地图 | [Language as a Sensor: Calibrated Spatial Belief Estimation in 3D Scenes from Natural Language](cards.md#paper-yz4p3wbwkx) | 把自然语言描述作为可校准传感观测融入地图。 |
| 具身智能 / 机器人学习 | 数据增强 | [Worlds in One Demo: A Synthetic Data Engine for Learning Open-World Mobile Manipulation](cards.md#paper-w1x9mho93e) | 拼接保留接触的轨迹片段并主动扩增纠错状态。 |
| 具身智能 / Agent | 技能学习 | [MobiAgent: Dual-Loop Recursive Policy Self-Improvement for Long-Horizon Mobile Manipulation](cards.md#paper-w3g5pwur7i) | 用部署回合自动更新技能库，并在执行中滚动重组技能。 |
| 具身智能 / Agent | 数据采集 | [RoboGene: Diversity-Driven Agentic Task Generation Framework for VLA Pre-training](cards.md#paper-uizby3yrgz) | 把人工确认的可执行性反馈写回任务提议器。 |
| 具身智能 / Agent | 工具调用 | [MAESTRO: Orchestrating Robotics Modules with Coding Agents for Zero-Shot Generalist Robots](cards.md#paper-bxw31dilgn) | 扩工具前先保证执行结果可验证且失败可重规划。 |
| 具身智能 / 优化 | 求解器学习 | [Learning Adaptive Solvers for Distributed Factor Graph Optimization on Matrix Lie Groups](cards.md#paper-menelmunwi) | 按优化阶段和通信状态自适应调节分布式求解器。 |
| 具身智能 / 规划 | 安全控制 | [Gradient-Free Neural Hamilton-Jacobi Reachability for Scalable Safety-Critical Control](cards.md#paper-k6kmjcl22t) | 用值探测构造安全教师动作，并以终端为锚分窗逆向训练。 |
| 具身智能 / 规划 | 安全控制 | [VertexCBF: Improving Neural Control Barrier Functions with Vertex-Restricted Control Search](cards.md#paper-dmljkr2f4o) | 动力学满足控制仿射时，用控制多面体顶点搜索生成安全监督。 |
| 具身智能 / 规划 | 安全控制 | [BarrierFormer: Transformer-Guided Predictive Barrier Enforcement for Safe Robot Control](cards.md#paper-y1up4arjzc) | 用预测滚动轨迹的屏障监督训练实时残差控制器。 |
| 具身智能 / 规划 | 生成规划 | [Safe Streaming Flow Planning by Aligning Sampling Dynamics with Execution Dynamics](cards.md#paper-gvm7kwehvi) | 使生成路径逐步随物理执行更新，并仅认证实际执行的步。 |
| 具身智能 / 规划 | 风险建模 | [Uncertainty-Aware Neural Time Fields for Safe Online Motion Planning in Unknown Environments](cards.md#paper-bkafd0mnwy) | 将测距不确定性传播进到达时间场，同时对轨迹施加机会约束。 |
| 具身智能 / 规划 | 空间表示 | [Learning Unions of Convex Sets via Invertible Latent Decomposition for Path Planning](cards.md#paper-txufbhgqg2) | 把高维自由空间映射为可连接的潜空间凸集以便显式规划。 |
| 具身智能 / 控制 | 扩散策略 | [Grounding Generative Policies in Physics: Optimization-Guided Diffusion for Robot Control](cards.md#paper-eaejdjpdzm) | 去噪时直接优化物理可行的校正量。 |
| 具身智能 / 控制 | 流匹配 | [CS-Pi: Constraint-Satisying Flow Policy Sampling](cards.md#paper-2nbzah51if) | 将可行投影作为重采样条件。 |
| 具身智能 / 控制 | 轨迹表示 | [PolyFusion: Collision-Free Robot Learning using Bernstein Polynomials](cards.md#paper-m8nqiskmdr) | 用分段多项式控制点代替稠密动作头。 |
| 具身智能 / 控制 | 跨构型迁移 | [CMRDF: Morphology-Conditioned Reachability Fields for Task-Space Robot Policy Transfer](cards.md#paper-dga5zlu7ck) | 将可达性拆成全局位置与局部姿态，集中逆运动学预算。 |
| 具身智能 / 规划 | 理论与诊断 | [On the Limits of Sampling-Based Reachability: Geometry, Dynamics, and Sample Complexity](cards.md#paper-wylezeakfi) | 高维长时域下避免仅凭采样质量保证宣称几何覆盖。 |
| 具身智能 / 控制 | 评测与诊断 | [Exploring the Intrinsic Geometry of Diffusion Models with Constrained Inverse Kinematics](cards.md#paper-pw8egeb2no) | 用已知约束维数检验扩散模型是否学到真实解流形。 |
| 具身智能 / 多智能体 | 联合生成 | [Robots as Tokens: Unified Diffusion Transformer for Coordinated Multi-Robot Trajectory Generation](cards.md#paper-4ar3f6obiq) | 将机器人作为集合 token 联合去噪，允许冻结部分队员轨迹。 |
| 具身智能 / 多模态 | 动作表示 | [H-VLA: Hierarchical Vision-Language-Action Model with Key-Action Reasoning and Motion Planning in a Unified Action Space](cards.md#paper-st0juml7ma) | 用共享相机坐标的关键动作连接语义计划和稠密控制。 |
| 具身智能 / 多模态 | 不确定性校准 | [SentryVLA: Uncertainty-Guided Action Selection and State Monitoring for Vision-Language-Action Robotic Control](cards.md#paper-snidokrnny) | 给冻结 VLA 加候选重排与独立执行异常监测。 |
| 具身智能 / 控制 | 模型预测控制 | [Optimal Control with Learned Critics under Unmodeled State Dependencies](cards.md#paper-39q3r1h0md) | 在 MPC 中分开修补动力学误差和有限时域短视。 |
| 具身智能 / 人机交互 | 主动查询 | [Simultaneous Forward and Inverse Human-in-the-Loop Optimization](cards.md#paper-cqkikio00k) | 以同一次用户查询同时降低结果模型和偏好模型的不确定性。 |
| 具身智能 / Agent | 验证与修复 | [EvoPlan: Evolutionary Neuro-Symbolic Robot Planning with Spatio-Temporal Guarantees](cards.md#paper-heumgqaw3m) | 用结构验证筛选 LLM 提案并逐轮扩大已验证计划。 |
| 具身智能 / 强化学习 | 课程生成 | [Generative Flow on Symbolic Abstractions for Embodiment Capability Discovery](cards.md#paper-weyfps89nj) | 用低层策略实测学习表现训练任务生成器。 |
| 具身智能 / 控制 | 技能调度 | [Energy-Based Policy Orchestration](cards.md#paper-nzrwlgnr4x) | 运行时联合选技能和技能专属目标。 |
| 具身智能 / 规划 | 推理调度 | [When Should a Robot Replan? Regret-Guided Update Scheduling in Time-Varying MDPs](cards.md#paper-4pwzyvbjxy) | 按累计遗憾分配有限的模型更新和重规划预算。 |
| 具身智能 / 多模态 | 数据策略 | [EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data](cards.md#paper-wf4x17al2r) | 用人类视频验证损失作为决定继续扩数据还是进入机器人中训的候选信号。 |
| 具身智能 / 多模态 | 可供性监督 | [OPENDEXGRASP: Open-vocabulary Task-Oriented Dexterous Grasping](cards.md#paper-wlgeyxjqid) | 在语言条件的抓取模型中，让区域可供性与手部位姿共享潜空间。 |
| 具身智能 / 强化学习 | 技能预训练 | [Play2Perfect: What Matters in Dexterous Play Pretraining for Precise Assembly?](cards.md#paper-rrl1xxzldm) | 先用自由操作预训练可达性和重定向能力，再把探索集中到精密接触阶段。 |
| 具身智能 / 模仿学习 | 重采样 | [FACTR 2: Learning External Force Sensing for Commodity Robot Arms Improves Policy Learning](cards.md#paper-03zmmfktxk) | 根据估计外力找到接触边界，在行为克隆中提高接触前片段的采样率。 |
| 具身智能 | 架构搜索 | [LEMCA: LLM-Guided Synthesis of Efficient Mode-Switching Control Architectures](cards.md#paper-802pzfmfgd) | 同时搜索模式与资源预算 |
| 具身智能 | 评测诊断 | [Automating the Design of Embodied Agent Architectures](cards.md#paper-2lnbcnztqk) | 用独立环境审计自动架构搜索 |
| 具身智能 | 安全学习 | [CAN AI PERCEIVE PHYSICAL DANGER AND INTERVENE?](cards.md#paper-7bxjjyw05e) | 把机器人能力约束显式输入并分开评测危险感知和干预 |
| 具身智能 | 数据合成 | [BiDexGrasp: Coordinated Bimanual Dexterous Grasps across Object Geometries and Sizes](cards.md#paper-odnu3ohjeq) | 用区域初始化降低双手抓取求解成本 |
| 具身智能 | 共享自治 | [Efficient and Reliable Teleoperation through Real-to-Sim-to-Real Shared Autonomy](cards.md#paper-qgzgvp8rnk) | 用少量示范拟合操作者代理，再在仿真学残差辅助 |
| 具身智能 | 策略适配 | [FlowDAgger: Human-in-the-Loop Adaptation of Generative Robot Policies in Latent Space](cards.md#paper-aspenn9eir) | 将纠正动作反演成冻结生成策略的输入噪声 |
| 具身智能 | 动作表示 | [KPGrasp: Scalable Keypoint Flow Matching for Dexterous Grasp Generation](cards.md#paper-bxnvzgsyfe) | 把混合关节和刚体坐标改成同一参考系下的欧氏关键点 |
| 具身智能 | 跨构型迁移 | [Learning Human Intention for Robotic Manipulation](cards.md#paper-l0bwpzwrky) | 用注视作为人类与机器之间的中间意图信号 |
| 具身智能 | 多智能体协作 | [Leave It Better Than Found: Value-Guided Cooperation in Sequential Tasks](cards.md#paper-n77om40jwl) | 跨机器人共享后续任务价值，筛除分布外估值 |
| 具身智能 | 模仿课程 | [Sequential Asymmetric Imitation for Learning Coupled Robot Policies](cards.md#paper-rfrjwmffvv) | 先单边训练再部署对手策略，集中纠正协同时序失败 |
| 具身智能 | 世界模型 | [WM-Craftnet: World Synesthesia Model for Robust and Generalizable Dexterous In-Hand Manipulation](cards.md#paper-amqh2hu9gs) | 让多模态动力学潜状态作为策略上下文，并显式监督深度去噪 |
| 具身智能 | 约束建模 | [Driving, Fast or Slow? Neuro-Symbolic Guidance for Motion Prediction in Multi-Modal Ground Mobility](cards.md#paper-fhzdeyenpf) | 以情境置信度决定何时弱化显式合规约束 |
| 具身智能 | 策略梯度 | [Flow Policy Gradients for Robot Control](cards.md#paper-acslhrig33) | 在需要多峰动作时测试免似然流策略梯度 |
| 具身智能 | 在线强化学习 | [RL Token: Bootstrapping Online RL with Vision-Language-Action Models](cards.md#paper-ryxo2ktk1m) | 用任务相关 token 和锚定小控制头在线修正 VLA |
| 具身智能 / 世界模型 | 安全评测 | [Targeting World Models to Compromise Robot Learning Pipelines](cards.md#paper-6t2ebangy5) | 世界模型合成数据进入训练前独立验收，并在下游策略做安全回归。 |
| 具身智能 / Agent | 记忆机制 | [RoboMemory: A Brain-inspired Multi-memory Agentic Framework for Interactive Environmental Learning in Physical Embodied Systems](cards.md#paper-q4ehhmipmb) | 以可动态更新的空间图组织跨回合积累的异质记忆。 |
| 具身智能 / Agent | 主动信息采集 | [COOL: Curiosity-Driven Object Ownership Learning for Personalized Robotic Assistance](cards.md#paper-v4qudwgroq) | 主动回访可能的信息收益高或记录陈旧的位置，以更新物体关系记忆。 |
| 具身智能 | 搜索蒸馏 | [Long-Horizon Multi-Object Rearrangement via Distilled Tree Search over Continuous Actions](cards.md#paper-hwuk4y2aer) | 用仿真搜索反复改进连续动作提议和价值估计 |
| 具身智能 | 接触反馈 | [PACE: Temporal-Role Tactile Conditioning for Chunk-Based Insertion Policies](cards.md#paper-aiinkhzlvb) | 分开处理持续接触、突发事件和未来接触 |
| 具身智能 | 合成监督 | [GRAIL: Generating Humanoid Loco-Manipulation from World Models](cards.md#paper-2defaneql7) | 生成视频前锁定几何与标定参数供重建复用 |
| 具身智能 | 课程学习 | [RoboNaldo: Accurate, Stable and Powerful Humanoid Soccer Shooting via Motion-Guided Curriculum Reinforcement Learning](cards.md#paper-wbgnjhriso) | 先建立参考动作先验，再逐级放开任务条件 |
| 具身智能 | 世界模型 | [SuperMimic: Scaling Humanoid Whole-Body Control with One Differentiable World Model](cards.md#paper-psnqjklvok) | 用共享可微动力学为多动作跟踪提供解析梯度 |
| 具身智能 | 探索初始化 | [Combining Constrained Sampling and Reinforcement Learning for Manipulation](cards.md#paper-cjgmjqlgz5) | 按接触模式覆盖设计训练重置分布 |
| 具身智能 | 阻抗控制 | [Constraint-Decomposed Impedance Control from Generative Policy for Articulated Object Manipulation](cards.md#paper-mjpidvjnms) | 用生成策略样本估计可动方向并设各向异性阻抗 |
| 具身智能 | 失败诊断 | [Demystifying When and Why VLAs Fail in Contact-Rich Tasks and How to Fix Them](cards.md#paper-bv0t1o1zil) | 先区分流匹配精度失败与力反馈失败，再分别修正 |
| 具身智能 | 触觉解耦 | [DeTac: Dual-branch Decoupling of Texture and Force Signals in Vision-Based Tactile Sensors](cards.md#paper-ymd1ykvind) | 将纹理与标记联合预测，减少串行修补的误差传递 |
| 具身智能 | 多模态融合 | [FingerEye: Learning Dexterous Manipulation with Continuous Vision-Tactile Sensing](cards.md#paper-raa96lpixj) | 按指尖传感组组织特征以抑制单模态捷径 |
| 具身智能 | 策略后训练 | [Never Too Late for Force: Accelerating VLA Post-Training with Reactive Force Injection](cards.md#paper-19iadsbo9a) | 以零初始化力注意力在保留原技能时加入接触反应 |
| 具身智能 | 动力学适配 | [TAM: Torque Adaptation Module for Robust Motion Transfer in Manipulation](cards.md#paper-ti3ok55n1h) | 把机器人动力学差异交给独立扭矩残差模块 |
| 具身智能 | 触觉表示 | [Visible Touch: Rendering Contact for Visuomotor Policies](cards.md#paper-ult1vxdeub) | 把接触信号放入现有视觉模型使用的空间参考系 |
| 具身智能 | 关节估计 | [Articulated 3D Scene Graphs for Open-World Mobile Manipulation](cards.md#paper-fkkr8jks29) | 用同一旋量优化从跟踪点恢复旋转和平移关节 |
| 具身智能 | 形变规划 | [Enabling Robust Cloth Manipulation via Inference-Time Simulator-in-the-Loop Refinement](cards.md#paper-nzychkctvt) | 用策略先验初始化实时仿真搜索以集中计算 |
| 具身智能 | 混合动力学 | [Learning Physics-Guided Residual Dynamics for Deformable Object Simulation](cards.md#paper-3hsq75gmr9) | 在物理骨架上学习速度残差，补足形变模拟误差 |
| 具身智能 | 几何不确定性 | [Noise-Invariant Spatial Encoding for 3D Manipulation Policies under Depth Corruption](cards.md#paper-r8moxo93mv) | 把深度位置不确定性传入注意力，避免几何 token 一律视为准确 |
| 具身智能 | 可达性代理 | [RAM: Reachability Across Morphologies](cards.md#paper-samjmur6xc) | 用形态条件化神经场替代在线逐姿态计算 |
| 具身智能 | 鲁棒规划 | [Robustness without Wrinkles: Parallel Simulation and Robust MPC for Certified Deformable Manipulation](cards.md#paper-uvjpdrcmlf) | 用实测感知误差标定可达管，并结合可微仿真规划 |
| 具身智能 | 时空地图 | [SERF: Spatiotemporal Environment and Robot Feature Map for Long-Horizon Mobile Manipulation](cards.md#paper-nibnbctz79) | 用同一潜空间的神经点记录场景与机身。 |
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
| 具身智能 | 自回归控制 | [Real-Time Execution with Autoregressive Policies](cards.md#paper-jlxzhoksxq) | 对自回归动作设定分词范围与约束解码，按严格时限生成。 |
| 具身智能 | 异步多模态 | [DAM-VLA: Decoupled Asynchronous Multimodal Vision Language Action model](cards.md#paper-mr4l9laugj) | 每种传感器按自身频率刷新潜变量缓存。 |
| 具身智能 | 设计诊断 | [How to Build an Efficient VLA: A Design Space Study for Modular Vision-Language-Action Models](cards.md#paper-pprwdhxw93) | 先扫描动作头初始化，再决定模块扩容。 |
| 具身智能 | 人机协同 | [Flow Control: Steering Vision-Language-Action Models with Simple Real-Time Inputs](cards.md#paper-hsz0lt7tcp) | 用粗粒度人类输入约束生成并回收干预轨迹。 |
| 具身智能 | 训练目标 | [PRISM: Bridging Multimodality and Real-Time Control in Multisensory Policies](cards.md#paper-rtx0zr5fjt) | 迁移 RS-IMLE 时按策略训练批量校准拒绝机制。 |
| 具身智能 | 在线调度 | [Action Chunk Scheduling for Batched Robot Policy Serving](cards.md#paper-2vstg6wu2p) | 按各机器人动作块消费速度分配 GPU 排队优先级。 |
| 具身智能 | 压缩诊断 | [Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered](cards.md#paper-zylula1tsy) | 剪枝后测试安全和成功，并用权重空间校正尝试恢复。 |
| 具身智能 | 部署评测 | [The Speedup Paradox: Rethinking Inference Optimization in Embodied Tasks](cards.md#paper-vxuazhduwe) | 按闭环完成时间选推理优化 |
| 具身智能 | 模型压缩 | [AgileDP: Quantizing Diffusion Policy via Dynamic Scaling and Reweighted Distillation](cards.md#paper-gr9nftftjn) | 按去噪时步动态缩放量化 |
| 具身智能 | 架构设计 | [What Do You Need for Compositional Generalization in Diffusion Planning?](cards.md#paper-hbhr1gxas0) | 扩散规划骨干优先测试平移等变和局部感受野 |
| 具身智能 | 训练目标 | [APT: Action Expert Pretraining Improves Instruction Generalization of Vision-Language-Action Policies](cards.md#paper-8tvqhvkrmd) | 先训练无语言动作先验，再门控引入语言 |
| 具身智能 | 动作条件 | [Direct Action-Head Injection of A Grounded 3D Point Unlocks Spatial and Task Generalization](cards.md#paper-14gtmkgucf) | 把三维目标相对位移直接送动作头 |
| 具身智能 | 动作表示 | [CLAP: Direct VLM-to-VLA Adaptation via Language-Action Grounding](cards.md#paper-geenmbqxhi) | 先生成自然语言动作计划再生成数字动作 token |
| 具身智能 | 推理控制 | [VLS: Steering Pretrained Robot Policies via Vision–Language Models](cards.md#paper-rmp7m64fq6) | 用三维关键点上的可导任务目标引导冻结策略去噪 |
| 具身智能 | 推理控制 | [Steering Autoregressive Vision-Language-Action Policies via Action Token Intervention](cards.md#paper-3kzmpjqupy) | 用低维用户输入介入自回归动作 token |
| 具身智能 | 任务结构 | [Inference-Time Robot Behavior Steering through Physically-Aware Reconfiguration of Task-Structure](cards.md#paper-nceeehy8d5) | 用户偏好用自动机组合，保持连续控制器冻结 |
| 具身智能 | 策略适配 | [Proxy Policy Steering](cards.md#paper-tfc6lmd02z) | 通过两个代理的速度差隔离任务监督的动作改变量 |
| 具身智能 | 离线强化学习 | [AWLS: Advantage-Weighted Latent Steering for One-Step Generative Robotic Manipulation Policies](cards.md#paper-z35bac5jbe) | 冻结单步生成器，用优势加权监督训练噪声残差 |
| 具身智能 | 偏好学习 | [Progress-Guided Preference Generation for Aligning Generative Control Policies](cards.md#paper-j8pjidi6rm) | 用按序覆盖专家片段的进度自动生成偏好对 |
| 具身智能 | 训练监督 | [CounterAlign: Counterfactual Supervision for Vision-Language-Action Models](cards.md#paper-ay4totylcx) | 把正确动作配错指令形成离线奖励负例 |
| 具身智能 | 辅助监督 | [ELAN4D: Embodiment-Centric 4D Supervision for Vision-Language-Action Models via Plug-and-Play Adaptation](cards.md#paper-6bq9ndqzns) | 从机器人自身运动学构造未来关键点轨迹辅助训练 |
| 具身智能 | 跨本体迁移 | [Cloak: Zero-Shot Cross-Embodiment Manipulation by Masking the End-Effector from the VLA](cards.md#paper-7kv78k8rcv) | 抹去腕部画面中的末端外观以检验跨机械手迁移 |
| 具身智能 | 表示对齐 | [UniLatent: Cross-Embodiment Transfer via Latent Observation Alignment](cards.md#paper-s3fvtypvnz) | 用仿真配对观测对齐编码器替代图像翻译 |
| 具身智能 | 示范条件 | [SeeTraceAct: Visibility-Aware Latent Planning from Cross-Embodiment Demonstration Videos](cards.md#paper-dwrc6la1kr) | 为细小目标的视频模仿加入可见性感知的未来末端轨迹判别 |
| 具身智能 | 示范策略 | [Perfect Demo Makes Poor Teacher:Learning Robust Alignment from Critical Motion Segments](cards.md#paper-9jm97ofgua) | 采集对齐示范时让操作者放慢并保留纠偏过程 |
| 具身智能 | 表示编辑 | [Flexible Language-Guided Representation Editing for Adaptive Robot Behavior](cards.md#paper-ojkazbklte) | 语言纠错允许增加、泛化和屏蔽任务特征 |
| 具身智能 | 机制解释 | [Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models](cards.md#paper-lfugzn8an2) | 用跨回合可复用性与因果干预测试 VLA 内部特征 |
| 具身智能 / 模仿学习 | 流匹配推理 | [Improving Robotic Generalist Policies via Flow Reversal Steering](cards.md#paper-ahph1ngaup) | 用粗动作反求噪声，再生成邻近的预训练行为模式。 |
| 具身智能 / 多模态 | 条件适配 | [MAST-VLA: Skill-Conditioned Adaptation with Trajectory-Affordance Priors for Multi-Skill Robot Manipulation](cards.md#paper-zr63f3tmyq) | 用技能条件选适配专家，用空间可供性约束动作头。 |
| 具身智能 / 多模态 | 表示对齐 | [Relational Spatial Alignment for Vision-Language-Action Models](cards.md#paper-p1r9ibkyv4) | 注入三维先验时，对齐成对空间关系并监控特征有效秩。 |
| 具身智能 / 多模态 | 空间查询 | [GeoAlign: Beyond Semantics with State-Guided Spatial Alignment in VLA Models](cards.md#paper-am3agfollh) | 用机器人状态查询几何特征，避免在每个动作阶段输入同一组静态空间 token。 |
| 具身智能 / 多模态 | 持续学习 | [Information-Theoretic Constraints for Continual Vision-Language-Action Alignment](cards.md#paper-h5qwmbcnsu) | 持续学习中同时保留跨模态历史锚点及视觉语言依赖。 |
| 具身智能 / 规划 | 迁移诊断 | [To Route or to Adapt? Multi-Expert Diffusion Planners in Unseen Regions](cards.md#paper-pjuqx9kbg5) | 先用 oracle 测现有专家的路由收益上限，若上限低则将预算用在目标域适配。 |
| 具身智能 | 世界模型 | [PhysCoRe: Physics-Corrected Residual World Models for Material-Aware Deformable Dynamics](cards.md#paper-go08puaqia) | 先辨识可解释物性，再拟合解析模拟器的系统残差 |
| 具身智能 | 部署适配 | [SILO: Simulation-in-the-Loop Sim-to-Real Transfer for Multi-Stage Cable Routing](cards.md#paper-2y1osh6gou) | 部署时保留模拟器并调用局部技能处理不同布线阶段 |
| 具身智能 | 上下文模仿 | [Instant-Fold: In-Context Imitation Learning for Deformable Object Manipulation](cards.md#paper-kakzp9lr9v) | 用整条单次示范作为策略条件，使同任务的动作顺序可变 |
| 具身智能 | 系统辨识 | [Wiggle and Go! System Identification for Zero-Shot Dynamic Rope Manipulation](cards.md#paper-n1gnyxww2f) | 先用短时探测区分物理参数，再让多个控制任务共用辨识结果 |
| 具身智能 | 示范转换 | [EgoEngine: From Egocentric Human Videos to High-Fidelity Dexterous Robot Demonstrations](cards.md#paper-drlpfld34l) | 同时转换人类视频外观和可执行动作，并保持时间对齐 |
| 具身智能 | 数据配比 | [DexRoam: Enabling Mobile Dexterous Manipulation from Egocentric Human Demonstrations](cards.md#paper-myykl10jkd) | 保留遥操作数据，将重定向人类示范用于提高真机样本效率 |
| 具身智能 | 潜动作预训练 | [LAPT-Scale: Scaling Embodied Policies with Latent Action Pre-Training on Human Videos](cards.md#paper-wmrkz9eybg) | 用连续隐动作表达细粒度帧间变化，再对齐实际机器人的动作空间 |
| 具身智能 | 跨构型监督 | [ACE-Ego: Unifying Egocentric Human and Robotic Data for VLA Pretraining](cards.md#paper-atdkkvog7w) | 在统一动作坐标中保留构型标识，并按监督可靠性训练 |
| 具身智能 | 世界动作模型 | [EgoWAM: World Action Models Beyond Pixels with In-the-Wild Egocentric Human Data](cards.md#paper-efkpqttjky) | 人机联合训练时优先比较特征及三维运动预测目标 |
| 具身智能 | 模仿学习重加权 | [Graph-Reweighted Behavior Cloning with Human Interventions for Precise Robotic Manipulation](cards.md#paper-bsjuf5kla3) | 用离线图的剩余步数差筛出失败回合中的有效恢复动作 |
| 具身智能 | 条件行为克隆 | [ALIGN: Aligning Condition Estimation and Expression in Advantage-Conditioned Behavior Cloning](cards.md#paper-mctspd3h0q) | 直接预测策略所需的类别条件，并在动作专家内调制 |
| 具身智能 | 生成策略 | [Unified Condition-Action Modeling for Accurate One-Step Action Generation](cards.md#paper-eiwbkqs5pz) | 将观测和时间条件与动作放进同一 token 序列，联合更新表示 |
| 具身智能 | 跨构型动作表示 | [Flow as Flow: Modeling Robot Velocity Fields as Probability Velocity Fields for Flow-Based Object Manipulation](cards.md#paper-bwhjoo36dr) | 跨机器人学习时拟合稠密连续速度而非稀疏位移 |
| 具身智能 | 潜空间生成 | [LDP: Shaping Latent Spaces for Diffusion-Based Robotic Manipulation](cards.md#paper-f5kmqjcc8x) | 先用观测条件编码集中动作分布，再在潜空间做流匹配 |
| 具身智能 | 空间条件化 | [Spatially Conditioned Diffusion Policy: Learning Precise and Robust Manipulation with a Single RGB Camera](cards.md#paper-ey3y7lxwy1) | 在每次去噪时沿中间轨迹查询图像特征 |
| 具身智能 | 多模态编码 | [UniFlow: A Unified Multi-Modal Policy for Robot Manipulation](cards.md#paper-o03eddno6r) | 把三维观测变成图像形状点图以复用预训练二维编码器 |
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
| 具身智能 / 机器人学习 | 空间表示 | [ObstaDiff: Generalizable Diffusion Policy Learning via Obstacle-aware Representations](cards.md#paper-nnfdatgr3l) | 用目标、障碍和背景分离令策略显式处理遮挡空间。 |
| 具身智能 / 机器人学习 | 动作重排 | [RAMT-VLA: Reliability-Aware Memory Tracing for Historical Support Assessment in Vision-Language-Action Models](cards.md#paper-k9ejtll8ba) | 用历史是否支持候选动作来重排冻结策略输出。 |
| 具身智能 / 机器人学习 | 推理剪枝 | [ACE-VLA: Action Centric Evaluation for Token Pruning in Vision-Language-Action Models](cards.md#paper-qu7v3gmydu) | 以动作梯度归因替代视觉文本注意力给视觉 token 排序。 |
| 具身智能 / 机器人学习 | 指令评测 | [RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents](cards.md#paper-a9aqjk3dat) | 让同一场景支持多条有效指令，避免视觉捷径掩盖指令忽略。 |
| 具身智能 / 机器人学习 | 模仿评测 | [The Imitator Game: Benchmarking Robot Imitative Ability Beyond Action Prediction](cards.md#paper-qh1h7ukk0k) | 把功能替代单独设为压力测试，区分轨迹复现与任务意图。 |
| 具身智能 / 机器人学习 | 人机协作评测 | [HARP-Bench: Benchmarking Robot Manipulation Around Active Humans](cards.md#paper-cci6zzicew) | 构造同一任务的配对人类介入版本，测主动协作者对策略的影响。 |
| 具身智能 / 机器人学习 | 在线监测 | [Online Robot Manipulation Error Detection and Description](cards.md#paper-qdjcwo9pmt) | 把故障监测建模为流式时间定位，同时输出起止与文本原因。 |
| 具身智能 / 机器人学习 | 故障检测 | [VLA-FAIL: Efficient Task Failure Detection for Finetuned Vision-Language-Action Models](cards.md#paper-mg7x6sfe75) | 融合特征分布偏离与预测动作块重叠区不一致，无需失败轨迹。 |
| 具身智能 / 机器人学习 | 关系监测 | [Robot-WATCHDOG : failure detection through object-centric graph representation](cards.md#paper-1yl1d39r7k) | 以物体时空图检测关系故障，数据稀少时使用关系一致性模板。 |
| 具身智能 / 机器人学习 | 失败恢复 | [Recover, Discover, Plan: Learning Skills and Concepts from Robot Failures](cards.md#paper-hufkyua5rr) | 从失败恢复轨迹学习关系谓词，让规划阶段主动避开同类失败。 |
| 操作 / 模仿学习 | 失败恢复 | [FAR: Failure-Aware Retry for Test-Time Recovery and Continual Policy Improvement](cards.md#paper-7jmlatltac) | 用失败轨迹构造负偏好，而不是原样重试。 |
| 操作 / VLA | 视觉条件恢复 | [Back to the Familiar Future: Failure Recovery for VLA Policies via Pre-Imagined Milestone Selection](cards.md#paper-jqvrofu5as) | 用执行前生成的中间目标恢复偏离轨迹的策略。 |
| 操作 / 分层学习 | 反事实监督 | [MAGMA-GEN: Validated Recovery Supervision from Ambiguous Failures via Counterfactual Re-Execution](cards.md#paper-r7zn8cpecj) | 验证失败后的纠正动作，再将其写入训练集。 |
| VLA / 安全 | 闭环评测 | [Trajectory-Level Redirection Attacks on Vision-Language-Action Models](cards.md#paper-e9zyawjqfr) | 在验证指令保持时检查最终任务结果。 |
| VLA / 安全 | 执行一致性 | [ExecGap: Exploiting Command-Execution Gap for Patch Attacks on Vision-Language-Action Models](cards.md#paper-qffjw11nya) | 监测命令与实测执行偏差，以发现动作失败。 |
| VLA / 安全 | 鲁棒训练 | [Lights, Camera, Malfunction: When Illumination Robustness Leaves VLA Models Blind to Color](cards.md#paper-7qmrpmvhzl) | 照明增强时保留颜色语义，并独立测试颜色依赖任务。 |
| 操作 / 数据 | 数据采集 | [Scale Up Strategically: Learning Compositional Generalization via Bias-Aware Evaluation and Data Collection for Robotic Manipulation](cards.md#paper-quvj7qbql6) | 按模型最不依赖的指令因子补采示范。 |
| 操作 / 泛化 | 因子化评测 | [MESA: An Evaluation Framework for Compositional, Semantic, and Spatial Generalization in Robotics](cards.md#paper-br2rxixvyn) | 分别测空间、实例、类别和子任务组合泛化。 |
| 操作 / 评测 | 无重置评测 | [ScaleEvals: Scaling Generalist Policy Evaluation through Reset-Free Autonomous Play](cards.md#paper-bl51sskshm) | 允许场景持续变化，按难度与技能标签校正策略排名。 |
| 操作 / 离线 RL | 离策略评测 | [RoboFQE: Rollout-Free Evaluation of Visual Robot Policies from Offline Trajectories](cards.md#paper-xmysklf2hx) | 用视觉特征上的拟合 Q 评估替代新回合。 |
| 操作 / 评测 | 随机任务协议 | [Benchmarking Real-World Robotic Manipulation through Stochastic Challenges](cards.md#paper-mwhlzlo4ud) | 跨实验室从同一分布各自抽样，兼顾可比性和隐蔽测试。 |
| 具身智能 / 安全 | 主动评测 | [Coverage Aware Active Evaluation for Failure Discovery with Paired Systems](cards.md#paper-qji3n7jzbc) | 用少量真实试验修正便宜代理，优先测试可信且有覆盖价值的区域。 |
| 具身智能 / 评测 | 仿真校准 | [SCAPE: Scenario-Conditioned Simulation-Augmented Policy Evaluation](cards.md#paper-51yzmugrua) | 用少量配对试验校准不同场景的性能与不确定性。 |
| 具身智能 / 评测 | 序贯统计 | [AnyRank: Reliable Anytime Policy Ranking via Sequential Testing](cards.md#paper-iou9zkasbg) | 将真机预算投向排名难区分的策略，随时输出有保证的部分排序。 |
| 操作 / VLA | 失败边界训练 | [Where Success Breaks: Failure-Boundary Learning for Robust Vision-Language-Action Models](cards.md#paper-3jf63cw3cj) | 定位失败发生的进度，用失败方向监督生成流。 |
| 具身智能 / 机器人设计 | 扩散引导 | [Transformer Transformer: A Unified Model for Motion-Conditioned Robot Co-design](cards.md#paper-ypkdkkod11) | 复用与奖励无关的动力学模型，为不同设计目标提供扩散采样引导。 |
| 具身智能 / 灵巧操作 | 形态条件化 | [XDex: Learning Cross-Embodiment Dexterous Grasping with 1000 Hands](cards.md#paper-wt25smjmeq) | 跨手迁移时区分物体、手形态和抓取姿态表示，并把形态多样性作为数据选型变量。 |
| 具身智能 / 灵巧操作 | 形态条件化 | [DiffMorphGrasp: A Diffusion Framework Conditioned on Hand Morphology for Cross-Embodiment Grasp Generation](cards.md#paper-4soiqrxqxj) | 跨手共用规范化动作空间，但按具体运动链计算关节损失。 |
| 具身智能 / 灵巧操作 | 跨形态表示 | [Multi-GraspLLM: Multimodal LLM for Multi-Hand Semantic Guided Grasp Generation](cards.md#paper-hpz010j4ea) | 新手型接入时复用共享抓取潜空间，只适配新手型。 |
| 具身智能 / 灵巧操作 | 抓取优化 | [Guiding Unified Dexterous Grasp Synthesis Across Modes and Scales via Learned Human Priors](cards.md#paper-cxxugluna2) | 用小规模人体抓取先验初始化接触模式及手腕位姿。 |
| 具身智能 / 灵巧操作 | 技能预训练 | [From Grasps to Dexterity: Large-Scale Grasp Pretraining for Dexterous Manipulation](cards.md#paper-hdnvcokmxh) | 把静态抓取标注变成低层控制预训练数据，用于操作有活动部件的工具。 |
| 具身智能 / 灵巧操作 | 分层控制 | [HiFun: a Hierarchical Framework for Efficient Functional Dexterous Manipulation Learning](cards.md#paper-agm5zqrjot) | 分开训练手部精细接触和手臂协同，针对偏离状态收集人类恢复。 |
| 具身智能 / 灵巧操作 | 残差策略 | [MoDex: Towards Universal Multi-Object Dexterous Grasping](cards.md#paper-ukrtsllqs6) | 根据物体相对距离在单次抓取和逐个交互之间切换。 |
| 具身智能 / 灵巧操作 | 数据验证 | [AutoDex: An Automated Real-World System for Dexterous Grasping Data Collection](cards.md#paper-8cdevbqa6x) | 仿真候选先过实物可行性核验，再按覆盖抽样。 |
| 具身智能 / 灵巧操作 | 目标表示 | [GoalDex: Learning Image-Goal-Conditioned Policies for Dexterous In-Hand Manipulation](cards.md#paper-rrnnh3mdah) | 遮挡严重时以目标图像直接条件化手内重定向。 |
| 具身智能 / 灵巧操作 | 交互动力学 | [ProxiDex: Learning Dynamics-Guided Proximity Policy for Dexterous Manipulation](cards.md#paper-ulcexirzjd) | 用手物距离作为硬件无关的动态状态，并随操作阶段调节其权重。 |
| 具身智能 / 灵巧操作 | 观测融合 | [FingerViP: Learning Real-World Dexterous Manipulation with Fingertip Visual Perception](cards.md#paper-pl6udcy9eu) | 给移动的近接相机补位姿和同指电流，分别表达观测方向与接触。 |
| 具身智能 / 灵巧操作 | 持续学习 | [Continual Learning for 6-DoF Grasp Synthesis via Experience and Demonstrations](cards.md#paper-mtz4ekup94) | 部署时更新嵌入空间记忆中的抓取评分与候选。 |
| 具身智能 / 灵巧操作 | 隐式几何 | [PartialBiGrasp: Inferring Hidden Local Geometry for Bimanual Grasping from Partial Views](cards.md#paper-jhewj56sh3) | 局部厚度比全形状更关乎成功时，用隐式占据推断当前不可见的抓取结构。 |
| 具身智能 / 灵巧操作 | 动作生成 | [DexHandover: Learning Bimanual Dexterous Handovers from Large-Scale Synthetic Data](cards.md#paper-zmbovwpuuw) | 先生成双手交接的共享接触状态，再将长运动优化锚定在该状态。 |
| 具身智能 / 灵巧操作 | 偏好适配 | [TacStyle: Personalizing Tactile Robot Policies using Structured Behavior Representations](cards.md#paper-th0fdttvb0) | 用语言模型选择连续行为潜变量，避免对动作策略逐轨迹标注细粒度偏好。 |
| 具身智能 / 灵巧操作 | 跨传感对齐 | [TACTX: Learning Shared Tactile Representations Across Diverse Sensors](cards.md#paper-xn8hwa4hpq) | 用同一接触事件配对不同触觉数据，使策略可直接换传感器。 |
| 具身智能 / 灵巧操作 | 跨传感预训练 | [Heterogeneous Tactile Transformer](cards.md#paper-0dopzpplvw) | 对齐触觉传感器时同时保留各模态内部可恢复信息。 |
| 具身智能 / 灵巧操作 | 跨频率融合 | [Multi-Resolution Tactile Imitation Learning for Contact-Rich Robotic Manipulation](cards.md#paper-b2gsinmx3r) | 训练时接入高频触觉，并测试在部署移除该传感器后能否保留增益。 |
| 具身智能 / 灵巧操作 | 触觉世界模型 | [Learning to Feel the Future: DreamTacVLA for Contact-Rich Manipulation](cards.md#paper-yeakwjw5xa) | 先把触觉对齐到各视觉视角对应位置，再用未来触觉监督动作。 |
| 具身智能 / 机器人学习 | 力觉闭环 | [FAWAM: Force-Aware World Action Models for Closed-Loop Contact-Rich Manipulation](cards.md#paper-1zyrrwoisv) | 用预测力矩作为在线残差控制参考 |
| 具身智能 / 机器人学习 | 条件门控 | [FR-VLA: Implicit Force Reasoning VLA for Contact-Rich Manipulation](cards.md#paper-q1q252tit0) | 按任务阶段决定物理反馈何时进入动作头 |
| 具身智能 / 机器人学习 | 记忆机制 | [FM-VLA: Force-based Memory for Vision-Language-Action Models in Contact-Rich Manipulation](cards.md#paper-42z4ov9nrq) | 视觉难分辨重复事件时用力觉潜变量记录历史 |
| 具身智能 / 机器人学习 | 仿真强化学习 | [TacCoRL: Integrating Tactile Feedback into VLA via Simulation](cards.md#paper-h7b56xk590) | 在仿真训练近失败恢复，用真实监督维持部署分布 |
| 具身智能 / 机器人学习 | 残差适配 | [OmniTacTune: Policy-Agnostic Real-World RL for Tactile Residual Adaptation of Visual Policies](cards.md#paper-vg6uymddy4) | 冻结视觉运动先验，用在线触觉策略学习局部修正 |
| 具身智能 / 机器人学习 | 跨模态监督 | [Dex-X: Learning Visual-Tactile Dexterous Manipulation From Human Demonstration with Simulated Interaction](cards.md#paper-surtjlxvxi) | 用仿真重建接触以补齐视频中缺失的触觉 |
| 具身智能 / 机器人学习 | 触觉表示 | [Blind Dexterous Grasping via Real2Sim2Real Tactile Policy Learning](cards.md#paper-tlwfbm8jtz) | 按接触事件校准仿真，再用传感布局约束触觉编码 |
| 具身智能 / 机器人学习 | 特权蒸馏 | [PTLD: Sim-to-Real Privileged Tactile Latent Distillation for dexterous manipulation](cards.md#paper-tjpi5d27wh) | 触觉仿真不可靠时，将真机触觉映射到仿真教师潜状态 |
| 具身智能 / 机器人学习 | 柔顺控制 | [Current as Touch: Proprioceptive Contact Feedback for Compliant Dexterous Manipulation](cards.md#paper-wiovp2zrwa) | 把电流和关节状态映射为普通 PD 的位置参考 |
| 具身智能 / 机器人学习 | 多模态监督 | [ViTaForce: Pairwise Visuo--Tactile--Force Representation Learning for Contact-Rich Imitation Learning](cards.md#paper-pcvxumrp6n) | 为不同传感器配对分别设定物理预测任务 |
| 具身智能 / 机器人学习 | 联合表征学习 | [MDF++: Visuo-Tactile World Action Model with End-to-end Representation Learning](cards.md#paper-d0ltfevdad) | 联合训练世界动作模型时用跨模态任务防潜表示坍缩 |
| 具身智能 / 机器人学习 | 推理引导 | [Inference-time Policy Steering via Vision and Touch](cards.md#paper-bc8sv8wttl) | 以视觉选长时行为模式，以触觉在短时局部编辑动作 |
| 具身智能 / 机器人学习 | 信息瓶颈 | [Water-Filling Allocation and Phase Transitions in Action-Conditioned Multimodal Information Bottlenecks](cards.md#paper-334wtbspig) | 只在触觉能改变精细动作时给触觉更多表征预算 |
| 具身智能 / 机器人学习 | 运动先验 | [Playing Soccer Like Humans Do: Learning Versatile and Agile Humanoid Soccer via Latent Motion Priors](cards.md#paper-xnyojximak) | 以共享运动潜空间支持多技能切换 |
| 具身智能 / 机器人学习 | 多任务强化学习 | [SkillX: Unified Multi-Skill Policy Learning for Humanoid Soccer](cards.md#paper-chcwuratwl) | 共享执行策略，让每技能使用专门价值估计与运动先验 |
| 具身智能 / 机器人学习 | 闭环适配 | [Towards Professional Tennis Styles for Humanoid Robots with Adaptive Motion Planning and Tracking](cards.md#paper-fp3mckmv24) | 高层计划加入跟踪速度反馈，低层训练覆盖随机速度 |
| 具身智能 / 机器人学习 | 集合表示 | [S2M-Trek: From Single to Multi-Sphere Transport via Per-Frame Deep Sets on a Wheel-Legged Robot](cards.md#paper-vtsuekrcnh) | 无跨帧身份的观测先逐帧做集合池化，再读时序 |
| 具身智能 / 全身控制 | 数据生成 | [Counterfactual Video Generation Enables Scalable Humanoid Loco-Manipulation](cards.md#paper-uzalccyrvl) | 用接触锚定重建与重定向将反事实视频转成物理可行示范。 |
| 具身智能 / 全身控制 | 示范生成 | [HumanoidMimicGen Data Generation for Loco-Manipulation via Whole-Body Planning](cards.md#paper-9kxz22fi7a) | 把示范中的接触技能与全身规划交替连接。 |
| 具身智能 / 全身控制 | 评测诊断 | [SIMPLE: Simulation-Based Policy Learning and Evaluation for Humanoid Loco-manipulation](cards.md#paper-artb8nigc3) | 采用模拟对真实排序的相关性作为基准验收标准。 |
| 具身智能 / 全身控制 | 示范采集 | [HuMI: Humanoid Whole-Body Manipulation from Humanoid-Free Demonstrations](cards.md#paper-aq2hmhw0ku) | 将便携式人类全身示范与机器人执行分层解耦。 |
| 具身智能 / 全身控制 | 全身控制 | [ZeroWBC: Learning Natural Whole-Body Humanoid Interaction from Human Egocentric Data](cards.md#paper-trtmmn2u1g) | 将根部及关键部位的全局对齐设为跟踪奖励。 |
| 具身智能 / 全身控制 | 合成监督 | [VLK: Learning Humanoid Loco-Manipulation from Synthetic Interactions in Reconstructed Scenes](cards.md#paper-qmafkdmtoy) | 先在重建空间用特权信息规划，再回渲染与运动同步的第一视角。 |
| 具身智能 / 全身控制 | 主动感知 | [HuG: Learning Humanoid Whole-Body Affordance-Aware Grasping with Active Perception](cards.md#paper-kpx1kofni5) | 分别管理观察视点与抓取前全身姿态。 |
| 具身智能 / 全身控制 | 示范编辑 | [EVOLVE: Egocentric Vision-based Humanoid Loco-Manipulation via Demonstration Editing](cards.md#paper-qf26obiuex) | 编辑稀疏身体关键点轨迹并保留成功执行的片段。 |
| 具身智能 / 全身控制 | 技能接口 | [OmniContact: Chaining Meta-Skills via Contact Flow for Generalizable Humanoid Loco-Manipulation](cards.md#paper-r27ers063s) | 用身体关键轨迹加接触开关作为分层共享接口。 |
| 具身智能 / 全身控制 | 控制覆盖 | [Humanoid Hanoi: Investigating Shared Whole-Body Control for Skill-Based Box Rearrangement](cards.md#paper-3ex2negqhp) | 用各技能闭环执行产生的状态增补共享追踪器训练。 |
| 具身智能 / 全身控制 | 跨形态控制 | [X-WBC: A Cross-Embodiment Foundation Model for Humanoid Whole-Body Control](cards.md#paper-kbotnjrw4s) | 让不同机器人共用人类运动命令语义、分开建模执行。 |
| 具身智能 / 全身控制 | 交互重定向 | [Social Humanoid: Socially Responsive Human–Humanoid Interaction](cards.md#paper-hf8x30fatz) | 双人示范转人机示范时，同时调整双方以保护接触。 |
| 具身智能 / 全身控制 | 交互蒸馏 | [VLM-Guided Contact Retargeting and Generative Partner Modeling for Humanoid-Human Interaction](cards.md#paper-dhh4gmm3nk) | 用特权接触教师蒸馏至自视角深度，并训练多假设人体姿态辅助头。 |
| 具身智能 / 全身控制 | 闭环控制 | [Pro-HOI: Perceptive Root-guided Humanoid-Object Interaction](cards.md#paper-rk0jcfddwk) | 以根部轨迹作上层控制接口，全身参考仅作训练奖励。 |
| 具身智能 / 全身控制 | 技能发现 | [MotionDisco: Motion Discovery for Extreme Humanoid Loco-manipulation](cards.md#paper-xjgz1ik29g) | 在离散接触序列上搜索，把物理验证委托给顺序轨迹优化器。 |
| 具身智能 / 全身控制 | 视觉迁移 | [LEGS: Fine-Tuning Teleop-Free VLAs for Humanoid Loco-manipulation in an Embodied Gaussian Splatting World](cards.md#paper-0jy75qydmn) | 将动作数据与场景外观分离，同一条示范按目标环境反复渲染。 |
| 具身智能 / 全身控制 | 可验证状态 | [Closing the Loop in Humanoid VLA: Persistent 3D Object Tokens for Verifiable Loco-Manipulation](cards.md#paper-e9oq6xsma9) | 让动作生成与完成判定读取同一持久物体记录。 |
| 具身智能 / 全身控制 | 触觉反馈 | [Unified Whole-Body Control for Quadrupedal Tactile-Informed Loco-Manipulation](cards.md#paper-r1fgjzlfnx) | 以触觉潜变量协调全身控制和抓力，而非维持常数大力。 |
| 具身智能 / 全身控制 | 力监督 | [WT-UMI: Tactile-based Whole-Body Manipulation via Force-Supervised Contact-Aware Planning](cards.md#paper-gkka9vehwb) | 用少量遥操作修正人类目标位姿，同时保留自然接触力监督。 |
| 具身智能 / 全身控制 | 残差控制 | [HERO: Learning Humanoid End-Effector Control for Visual Whole-Body Open-Vocabulary Object Grasping](cards.md#paper-gbchkym28k) | 让开词汇感知提供目标，使用带学习前向模型的末端控制器精确执行。 |
| 具身智能 / 人形控制 | 约束控制 | [Constrained Whole-Body Tracking for Humanoid Robots](cards.md#paper-nzvfxorvoc) | 把部署后新增的约束同时施加到运动参考和底层动力学。 |
| 具身智能 / 人形控制 | 残差适配 | [General Humanoid Whole-Body Control via Pretraining and Fast Adaptation](cards.md#paper-hwaigsxlah) | 对未见动作只训练小型残差，并用正交和 KL 约束限制预训练行为漂移。 |
| 具身智能 / 人形控制 | 低秩适配 | [CA-GMT: Contact-Aware Low-Rank Adaptation of Motion Tracking for Whole-Body Teleoperation](cards.md#paper-u2dtqwafqo) | 只在相关动作相位施加接触适配，并以接触错误衡量收益。 |
| 具身智能 / 人形控制 | 接触控制 | [Learning Functional Compliance in Whole-body Manipulation](cards.md#paper-walhowqwnx) | 按任务方向和阶段分配柔顺性，保留关键轴上的控制权。 |
| 具身智能 / 人形控制 | 闭环规划 | [Reactive Closed-Loop Motion Planning Towards Universal Humanoid Whole-Body Control](cards.md#paper-2tjuz95jmb) | 用实际跟踪偏离的前缀训练生成规划器，并异步重规划。 |
| 具身智能 / 人形控制 | 低延迟控制 | [ExtremControl: Low-Latency Humanoid Teleoperation with Scaled Velocity Feedforward](cards.md#paper-x4i3ksa2kd) | 测量位置控制滞后，按理论比例加入缩放速度前馈。 |
| 具身智能 / 人形控制 | 遥操接口 | [SPOT: Spatial Perception-Oriented Long-Horizon Humanoid Teleoperation](cards.md#paper-pwdt36r945) | 让操作者在稳定广角视图中独立转头观察，避免观察动作误驱动机器人。 |
| 具身智能 / 人形控制 | 探索课程 | [SwingBot: Learning Whole-Body Brachiation for Humanoid Robots](cards.md#paper-wp9ex57z2k) | 以关键帧覆盖长时稀有接触转移，再用可部署传感估计相对位置和接触。 |
| 具身智能 | 遥操课程 | [HEFT: Heavy Load Full-size Humanoid Teleoperation with Privileged Motion Guidance and Windowed Payload Curriculum](cards.md#paper-jhdmnwpt4o) | 以干净重建参考指导含噪 VR 跟踪，并按阶段设置载荷上限。 |
| 具身智能 | 分层控制 | [HLO-AMP: Hierarchical Loco-Manipulation from Object-Aware Motion Priors](cards.md#paper-l8hoz8lovg) | 低层预训直接保留真实分布接触，高层约束在已见命令域。 |
| 具身智能 | 故障适配 | [FT-WBC: Learning Fault-Tolerant Whole-Body Control for Legged Loco-Manipulation](cards.md#paper-mjvsjnqufv) | 利用本体历史估计下肢故障，先修正上肢规划要求的底座姿态。 |
| 具身智能 | 接触控制 | [ContactMimic: Humanoid Object Interaction via Contact Control](cards.md#paper-wxbkimuzti) | 将部件接触作为独立可控命令，并打破命令与几何轨迹共线性。 |
| 具身智能 | 技能控制 | [AcroRL: Learning Aggressive Quadrotor Inversion using Bidirectional Thrust](cards.md#paper-uoffrjhhq8) | 用双方向独立过渡策略衔接常规轨迹控制。 |
| 具身智能 | 可微仿真 | [Learning Visuomotor Quadrotor Flight Through Dynamic Narrow Gaps via Differentiable Simulation](cards.md#paper-nwlhqecx3l) | 精度关键且动力学可微时优先对比路径梯度训练。 |
| 具身智能 | 模态训练 | [Approximate Imitation Learning for Event-based Quadrotor Flight in Cluttered Environments](cards.md#paper-j5qczcrrda) | 先从离线数据学传感表示，再利用低成本模拟状态训练闭环。 |
| 具身智能 | 边缘推理 | [Neuromorphic Control of a Flapping-Wing Robot on Resource-Constrained Hardware](cards.md#paper-yzejd0wik9) | 在普通 MCU 上实测脉冲控制的延迟与功耗，再决定是否替换 ANN。 |
| 具身智能 | 评测设计 | [AM-Bench: A Modular Simulation Suite and Benchmark for Aerial Manipulation Policy Learning](cards.md#paper-8ifziu27yy) | 分开交换机器人形态、低层控制与策略接口以定位空中操作失效。 |
| 具身智能 | 采样引导 | [π, But Make It Fly: Physics-Guided Transfer of VLA Models to Aerial Manipulation](cards.md#paper-sn5svboz8d) | 迁移固定底座 VLA 时在流采样加入载荷约束。 |
| 具身智能 | 测试时适配 | [GeoXel: Geographic Per-pixel 3D Mapping from Aerial Video in the Wild](cards.md#paper-xjym9if1tm) | 用地理锚点监督少量层适配，保持场景结构并纠正长序列漂移。 |
| 具身智能 | 代价表示 | [Plann3r: Predicting Planning Costs Grounded in 3D](cards.md#paper-rexyyvslbt) | 把标量图像距离换成由目标像素索引的像素级测地代价。 |
| 具身智能 | 安全评测 | [Future-Aware Flow Planning for Safe UAV Target Following](cards.md#paper-m94acp7al5) | 安全跟随策略比较时同时测碰撞、持续跟踪和平滑度。 |
| 具身智能 | 自蒸馏 | [Training Generalist Navigation Policies via Action Self-Distillation](cards.md#paper-lwmnsycnck) | 只在训练时利用完整轨迹反推目标与推理，再让学生用机载观测预测。 |
| 具身智能 | 动力学适配 | [Adapting Generalist Vehicle Models for High-Speed MPC Across Terrains](cards.md#paper-qeov7muwix) | 少量实测加识别仿真，并用近期状态动作历史估计动力学上下文。 |
| 具身智能 | 评测诊断 | [ATOM-Bench: A Real-World Benchmark for Atomic Skills and Compositional Generalization in Manipulation Policies](cards.md#paper-dpovq6ne2d) | 用原子能力和组合失败占比分离动作不足与组合泛化失败。 |
| 具身智能 | 主动澄清 | [Bayesian Active Learning for Intent Disambiguation in Interactive Robot Planning](cards.md#paper-el4edbhqcg) | 用具身任务规范候选的信息增益挑澄清问题，再交由可验证规划器。 |
| 具身智能 | 不确定性 | [Control-Ready Uncertainty for Trajectory Diffusion](cards.md#paper-c9tcchtvcs) | 蒸馏扩散分数曲率，输出可在线使用的逐步协方差。 |
| 具身智能 | 控制目标 | [Emergent Control via Prior-Based Free Energy Minimization](cards.md#paper-xy8qpmsxvq) | 偏好状态推断替代显式任务奖励 |
| 具身智能 | 分层规划 | [GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational Automation Tasks](cards.md#paper-c96z0rnfh8) | 通过并行仿真排练选择技能图结构与参数 |
| 具身智能 | 约束解码 | [Meta-Ctrl: Guaranteed Plan Generation by Decoupling Syntactic and Semantic Constraints](cards.md#paper-qqs6jndxfz) | 在 token 层检查语法，在动作层检查可执行前置条件 |
| 具身智能 | 技能记忆 | [Playful Agentic Robot Learning](cards.md#paper-gel3gdwsyo) | 下游任务到达前通过自主探索生成可检索代码技能 |
| 具身智能 | 可微优化 | [Scalable Deep Unfolding of Conic Optimizers](cards.md#paper-csya6ohdle) | 按矩阵向量积实现隐式反传，并稳定处理重复特征值 |
| 具身智能 | 约束控制 | [CMP: Robust Whole-Body Tracking for Loco-Manipulation via Competence Manifold Projection](cards.md#paper-yyitbtz7rq) | 把超出控制能力的指令投影到可执行边界 |
| 具身智能 | 教师蒸馏 | [LadderMan: Learning Humanoid Perceptive Ladder Climbing](cards.md#paper-plnj3a6yht) | 从单一参考学习多个专家，再蒸馏成可感知适应的统一策略 |
| 具身智能 | 离线到在线强化学习 | [Learning Loco-Manipulation From SMPC Demonstrations With Sparse Offline-to-Online RL](cards.md#paper-5b4j0e21aj) | 用可快速调整的规划教师覆盖探索，再用任务稀疏奖励提升策略 |
| 具身智能 | 经验规律 | [OpenHLM: An Empirical Recipe for Whole-Body Humanoid Loco-Manipulation](cards.md#paper-ttfzrb0hw3) | 优先暴露全身关节，并用跨形态预训练及 HuMI 补充目标覆盖 |
| 具身智能 | 数据清洗 | [PHUMA: Physically Reliable Humanoid Locomotion Dataset](cards.md#paper-ly47gbfn32) | 用物理一致性筛选和重定向修复视频动作 |
| 具身智能 | 安全控制 | [ResSafe: Learning Safety Filtering with Residual Reinforcement Learning for Humanoids](cards.md#paper-remmzounpn) | 把任务策略与安全残差分开优化 |
| 具身智能 | 触觉控制 | [TactileStep: Sole Tactile Learning for Regulating Foot--Terrain Interaction in Humanoid Locomotion](cards.md#paper-aglo1l8snb) | 用足底压力划分落地和站稳阶段，分别塑形 |
| 具身智能 | 在线建图 | [Anchor3R: Streaming 3D Reconstruction with Transient Anchors for Long-Horizon Visual Mapping](cards.md#paper-q53aygo2ie) | 以当前帧局部坐标预测，再通过运动图对齐长期轨迹 |
| 具身智能 | 约束生成 | [Collaborative Planning for UAV-UGV Teams under Operational Constraints via Masked Error-bounded Neuro-Symbolic Diffusion](cards.md#paper-lsrxdurldg) | 在符号约束过滤之后计算熵并决定掩码解码顺序 |
| 具身智能 | 评测诊断 | [From Region Arrival to Instance-Level Grounding in Vision-and-Language Navigation](cards.md#paper-rwgnm8fuxx) | 最后靠近阶段用目标可见性决定停步，并细化成功指标 |
| 具身智能 | 惯性定位 | [MosaicIMU: Composing Carrier Experts for Generalizable Neural Inertial Odometry](cards.md#paper-k2qzxbcsbq) | 用载体原型路由组合专家，换平台时只训练新残差分支 |
| 具身智能 | 时间规划 | [OSCAR: Obstacle Survival Curves for Adaptive Robot Navigation](cards.md#paper-hr2fyfod4n) | 用类别条件清障生存曲线估计应等多久再绕行 |
| 具身智能 / 强化学习 | 安全约束 | [SCoCaT: Success Conditioned Constrained Reinforcement Learning for Spacecraft Docking](cards.md#paper-suv5pudsyi) | 给终止式约束强化学习加成功价值监督。 |
| 具身智能 / 模仿学习 | 风险监督 | [TRIAD Planner : Three-Level Robust Imitation Learning for Autonomous Driving](cards.md#paper-98pbd92mei) | 在模仿训练中用尾部风险调整多模态候选监督，部署保持相同开销。 |
| 具身智能 / 世界模型 | 层级规划 | [Hierarchical Planning with Latent World Models](cards.md#paper-zts11nhglq) | 用同一潜空间连接不同时间尺度的预测模型做 MPC。 |
| 具身智能 / 世界模型 | 策略后训练 | [WAM-STEP: Self-Improving World-Action Models Through Efficient Post-Training](cards.md#paper-1u6orijjcu) | 校准训练期视频分支后，将其用于想象回报以更新动作分支。 |
| 具身智能 / 世界模型 | 失败监督 | [FACT: Failure-Aware Causal Training for World-Action Models](cards.md#paper-yrnlvjcapo) | 用实际动作与失败后果训练进度预测，抑制成功偏置。 |
| 具身智能 / 世界模型 | 推理筛选 | [τ0-WM: A Unified Video-Action World Model for Robotic Manipulation](cards.md#paper-qvol1xoutn) | 以重去噪一致性先排序，只对低质量动作候选调用后果模拟。 |
| 具身智能 / 世界模型 | 动作编码 | [TAPESTRY: A Single Backbone for Video Generation and Robot Control](cards.md#paper-ailv1lyfxf) | 把动作投影成单个视频块 token，复用视频骨干并做单步动作推理。 |
| 具身智能 / 世界模型 | 条件分解 | [AnyWorld: Factorized Egocentric World Models for Cross-Embodiment Generalization](cards.md#paper-0w0ylgezd5) | 独立调节动作、视角与本体生成同一交互的机器人数据。 |
| 具身智能 / 世界模型 | 动作条件化 | [Robot-Factored World Models via Robot Rendering](cards.md#paper-2nityixwgj) | 用执行前可得的名义机器人轨迹渲染作视频预测条件。 |
| 具身智能 / 世界模型 | 频域编码 | [From Video Frames to Robot Meta-Frames: A Unified Latent Interface for World Action Models](cards.md#paper-nbdd4rvq5q) | 用冻结去噪器诊断机器人变量编码是否贴合视频先验。 |
| 具身智能 / 世界模型 | 表征诊断 | [What Makes Video World Model Latents Action-Relevant: Prediction over Reconstruction](cards.md#paper-lsfm8tzuh2) | 用逆动力学探针选择视频表示，不以像素重构质量代替动作可恢复性。 |
| 具身智能 / 世界模型 | 推理压缩 | [ImageWAM: Do World Action Models Really Need Video Generation, or Just Image Editing?](cards.md#paper-nthuqgjrgs) | 用目标帧编辑缓存替代全视频生成，为动作头提供变化线索。 |
| 具身智能 / 世界模型 | 紧凑状态 | [Box Trajectories as Compact State Representations for World Action Models](cards.md#paper-khjj1z5m4y) | 对刚性物体运动使用定向框轨迹预测，减少视觉监督成本。 |
| 具身智能 / 世界模型 | 掩码监督 | [MaskWAM: Unifying Mask Prompting and Prediction for World-Action Models](cards.md#paper-ih059vnewq) | 把首帧掩码作为指代输入，同时预测未来掩码作为辅助监督。 |
| 具身智能 / 世界模型 | 三维对齐 | [GSWAM: A Unified Gaussian World Action Model for Robotic Manipulation](cards.md#paper-u5pojpnj6j) | 在共享三维锚空间内建模动作和场景，并对两类变量使用不同流时间步。 |
| 具身智能 / 世界模型 | 刚体动力学 | [ORD-WM: Learning Object-Centric Rigid Dynamics for 3D World Modeling in Robotic Manipulation](cards.md#paper-xhjeeyhkhy) | 预测逐物体刚体变换并解析作用在潜变量上，避免多步几何漂移。 |
| 具身智能 / 世界模型 | 层级规划 | [Scaling World Model for Hierarchical Manipulation Policies](cards.md#paper-hcg12iftej) | 让底层策略同时消费可视子目标和文本，以固定执行器检验分布外增益。 |
| 具身智能 / 世界模型 | 时序诊断 | [Understanding and Mitigating the Video-Action Generalization Gap via Temporal Ratio](cards.md#paper-mlf6dhhbnf) | 监控动作头对未来潜变量的依赖，只在适合的阶段增强视频引导。 |
| 具身智能 / 多模态 | 辅助监督 | [Pri4R: Learning World Dynamics for Vision-Language-Action Models with Privileged 4D Representation](cards.md#paper-8yqfxyof0y) | 训练时预测未来三维点轨迹，部署时移除预测头。 |
| 具身智能 / 世界模型 | 延迟补偿 | [Intercepting the Future: Latent-Space Predictive World Model for Dynamic VLA Manipulation](cards.md#paper-ddzwaomwze) | 在冻结 VLA 前预测预计执行时刻的视觉 token，并按不确定性截断预测。 |
| 具身智能 / 世界模型 | 测试时适配 | [WAM-TTT: Steering World-Action Models by Watching Human Play at Test Time](cards.md#paper-ox3ertz3rv) | 测试时用未标注人类视频更新小型记忆，保持动作世界模型冻结。 |
| 具身智能 / 世界模型 | 执行监控 | [ContactGuard: Pre-Contact Execution Monitoring with Action-Conditioned Latent World Models](cards.md#paper-jq0aplis34) | 监控先按真实计划预测，再在线判定是否中止，不改底层策略。 |
| 具身智能 / 多模态 | 主动感知 | [Seek-before-Act: Generative Visual Foresight for Occlusion-Aware Wrist-View Manipulation](cards.md#paper-hwtnqrjmuq) | 用语义可操作性判定决定继续找视角还是开始动作。 |
| 具身智能 / 多模态 | 训练重采样 | [Enhancing Robotic Control Robustness through Generative Visual Model](cards.md#paper-e5lvpa2glx) | 在固定合成量下对照按控制表现重加权与静态混合。 |
| 具身智能 / 世界模型 | 几何监督 | [DepthWorld: 3D World Model for Robot Manipulation](cards.md#paper-xombt7ofur) | 需保留预训练视频编码器时，以潜空间拼接加入深度并等预算核对 RGB。 |
| 具身智能 / 世界模型 | 强化学习 | [WoVR: World Models as Reliable Simulators for Post-Training VLA Policies with RL](cards.md#paper-qhiz2k4e88) | 对照从头想象与重启中间关键帧，固定交互预算测策略收益。 |
| 具身智能 / 世界模型 | 数据策略 | [PlayWorld: Learning Robot World Models from Autonomous Play Data](cards.md#paper-hatezfmdn5) | 预留数据预算采集非任务自由交互，并以固定模型比较反事实动作泛化。 |
| 具身智能 / 强化学习 | 梯度估计 | [Coupled Local and Global World Models for Efficient First Order RL](cards.md#paper-zdglinpebl) | 将前向保真和反传成本分开，用局部代理验证优化方向。 |
| 具身智能 / 强化学习 | 约束目标 | [SafeDojo: Safe Reinforcement Learning for VLA via Interactive World Model](cards.md#paper-xgth4qbomb) | 分开监督任务收益和安全成本，在相同测试上报告二者权衡。 |
| 具身智能 / 世界模型 | 安全诊断 | [How Well Do Latent World Models Understand Partially Observable Safety Constraints?](cards.md#paper-587eukwa7d) | 先区分观测缺失与预测失准，再选择增传感监督或风险校准。 |
| 具身智能 / 模仿学习 | 动作对齐 | [Imitation from Heterogeneous Demonstrations using Grounded Latent-Action World Models](cards.md#paper-rlsvfgv1ps) | 以环境效果对齐异构动作，再独立检测目标本体解码可行性。 |
| 具身智能 / 规划 | 符号建模 | [STRIPS-WM: Learning Grounded Propositional STRIPS-style World Models from Images](cards.md#paper-fvphddjumi) | 用动作前提和后效评价压缩表征是否保留规划信息。 |
| 具身智能 / 世界模型 | 三维轨迹 | [μ0: A Scalable 3D Interaction-Trace World Model](cards.md#paper-shbmwdrpvu) | 用稀疏三维交互轨迹作跨本体条件，对照像素预测的计算和效果。 |
| 具身智能 / 世界模型 | 推理缓存 | [C³ache: Accelerating World Action Models with Cross Inference Chunk Cache](cards.md#paper-t3iohvur0r) | 同时比较块内和跨块缓存，在急转接触场景单独测失效。 |
| 具身智能 / 世界模型 | 关键帧生成 | [SKIP: Sparse Keyframe Interpolation Paradigm for Efficient Embodied World Models](cards.md#paper-hgrivs5qzu) | 做视频压缩生成时按事件选锚点并测下游学习，而不只测画质。 |
| 具身智能 / 世界模型 | 鲁棒评测 | [StressDream: Steering Video World Models for Robust Policy Evaluation and Improvement](cards.md#paper-9um5jbxz4t) | 在隔离模拟评测中加入定向边界场景，检查策略故障是否可复现。 |
| 具身智能 / 世界模型 | 数据采集 | [Training Controllable World Models via Action Influence Maximization](cards.md#paper-oocwc3dn5d) | 采集时主动覆盖同一状态下多类动作，以反事实对照测试模型是否服从动作。 |
| 具身智能 / 世界模型 | 故障诊断 | [Adaptive World-Models for Anomaly Recognition (AWARE): A Framework for Robot Dynamics Prediction and Introspection](cards.md#paper-994ptkadnu) | 用可解释动力学参数区分观测噪声与设备退化，并分开测检测和定位。 |
| 具身智能 / 模仿学习 | 重定向 | [WARP: Whole-Body Retargeting for Learning from Offline Human Demonstrations](cards.md#paper-5zw401uegd) | 先以固定规则消除冗余动作标签，再比较同数据量下监督收敛。 |
| 具身智能 / 灵巧操作 | 示范采集 | [RealDexUMI: A Wearable Universal Manipulation Interface for Dexterous Robot Learning](cards.md#paper-logykmevvc) | 让采集和机器人执行共享物理末端，固定策略测跨末端与跨底座的数据偏移。 |
| 具身智能 / 灵巧操作 | 重定向 | [AnyDexRT: Calibration-Efficient Dexterous Hand Retargeting with Few-Shot Human Guidance](cards.md#paper-dyonmedjxv) | 把少量人工指导放在操作相关接触附近，与全空间均匀校准对照。 |
| 具身智能 | 遥操校准 | [YOCO: You Only Calibrate Once! Fast Mocap Calibration for Dexterous Teleoperation](cards.md#paper-lhlnvoaehr) | 把跨用户校准变成前向预测 |
| 具身智能 | 接触控制 | [Towards Human-level Dexterous Teleoperation](cards.md#paper-ongdmfjg2i) | 用手物联合子目标指导低层控制 |
| 具身智能 | 重定向 | [TopoRetarget: Interaction-centric retarget for dexterous manipulation](cards.md#paper-9w3pec3xlg) | 保持手物局部拓扑 |
| 具身智能 | 奖励设计 | [Learning Dexterous Manipulation Using Contact Wrench Guidance From Human Demonstration](cards.md#paper-depcm83k5i) | 在物体受力空间比较人机演示 |
| 具身智能 | 规划接口 | [Human2Any: Human-to-Robot Transfer via Constraint-Aware Compositional Planning](cards.md#paper-h1yqzsoz49) | 把物体间相对运动作为跨本体先验 |
| 具身智能 | 评测诊断 | [H2RBench: A Real-to-Sim Benchmark for Evaluating Human-to-Robot Transfer](cards.md#paper-smkzi5hx9p) | 以仿真排名筛选真机候选 |
| 具身智能 | 主动感知 | [ActiveMimic: Egocentric Video Pretraining with Active Perception](cards.md#paper-j5rzynkq8z) | 把相机运动视作可学习动作 |
| 具身智能 | 视角适配 | [WARPED: Wrist-Aligned Rendering for Robot Policy Learning from Egocentric Human Demonstrations](cards.md#paper-xkz7yjefr4) | 从人类第一视角合成策略部署的腕部视角 |
| 具身智能 | 动作表示 | [AdvDex: Learning Dexterous Manipulation from Human Demonstrations via Joint-Aligned Actions and Adversarial Learning](cards.md#paper-tswzwxgz5p) | 共享腕姿与手指动作后，消去视觉本体信息 |
| 具身智能 | 技能接口 | [LUCID: Learning Embodiment-Agnostic Intent Models from Unstructured Human Videos for Scalable Dexterous Robot Skill Acquisition](cards.md#paper-qsmd0pq7up) | 将互联网视频训出的短期意图与本体控制解耦 |
| 具身智能 | 数据筛选 | [VISTA: Vision-Grounded and Physics-Validated Adaptation of UMI data for VLA Training](cards.md#paper-xagvjptxtr) | 训练前按目标本体的轨迹可执行性筛选人类示范 |
| 具身智能 | 数据采集 | [SEED-UMI: Sharing the Exoskeleton between human and robot for onE-to-one Dexterous demonstration](cards.md#paper-lhdmyo4bzs) | 让人和机器人共用外骨骼与相机几何 |
| 具身智能 | 偏好学习 | [Freeform Preference Learning for Robotic Manipulation](cards.md#paper-fylym2c6xc) | 将整体偏好拆成可命名的多个质量轴 |
| 具身智能 | 分层优化 | [Beyond the End-Effector: Learning Whole-Arm Contact Manipulation from Human Demonstrations](cards.md#paper-c08kkstfex) | 把非末端接触定义与机器人的接触连杆选择解耦 |
| 具身智能 | 注意力监督 | [Gaze Prompts: Temporally Dense Human Attention for Vision–Language–Action Fine-Tuning](cards.md#paper-xeoer7gykg) | 将凝视预测画在输入像素中，与辅助损失对照 |
| 具身智能 | 数据配比 | [Human-like autonomy emerges from self-play and a pinch of human data](cards.md#paper-lovzujpkxn) | 以少量人类轨迹打破自博弈形成的不兼容约定 |
| 具身智能 | 策略优化 | [Efficient On-policy Visual-RL via Stochastic Decoupled Policy Gradient](cards.md#paper-c7bvd59rpp) | 渲染预算受限时用轨迹随机扰动估计策略梯度 |
| 具身智能 | 策略优化 | [FlowDPG: Deterministic Policy Gradient on Flow Matching Policies for Real-World Manipulation](cards.md#paper-wv9xf5ii7l) | 用 critic 梯度监督流速度场，省去跨 ODE 步反传 |
| 具身智能 | 偏好优化 | [FlowPRO: Reward-Free Fine-Tuning of Flow-Matching VLAs via Proximalized Preference Optimization](cards.md#paper-ftx97rpoow) | 显式约束隐式奖励的绝对大小，并用干预回滚形成偏好对 |
| 具身智能 | 仿真真机协训 | [Beyond Imitation: Reinforcement Learning-Based Sim-Real Co-Training for VLA Models](cards.md#paper-7hdkicfgrw) | 用仿真在线 RL 优化，同时用真机监督锚定旧能力 |
| 具身智能 | 残差强化学习 | [Object-Centric Residual RL for Zero-Shot Sim-to-Real VLA Enhancement](cards.md#paper-taxtxe4oqd) | 用物体位姿而非像素为冻结 VLA 学习仿真残差。 |
| 具身智能 | 强化学习后训练 | [RoboFFT: Finetuning generative robot policy via online reinforcement learning with forward process](cards.md#paper-efjcm9am0o) | 用正向加噪构造 PPO 替代比率。 |
| 具身智能 | 强化学习后训练 | [Optimal Transport Q-Learning for Flow Policy Steering and Acceleration](cards.md#paper-uni5vigrgr) | 用优势加权条件最优传输同时优化流策略和推理步数。 |
| 具身智能 | 相对进度监督 | [WARP-RM: A Warp-Augmented Relative Progress Reward Model for Data Curation](cards.md#paper-yaym35u9su) | 用变速和逆序构造有符号进度来加权动作块。 |
| 具身智能 | 主动感知 | [Learning Decomposed Visibility for Efficient Active Exploration of Cluttered Scenes](cards.md#paper-qgk0k192w6) | 把换视角和推动分别预测，再用统一可见性收益选模式。 |
| 具身智能 | 训练系统诊断 | [UniLab: A Heterogeneous Architecture for Robot RL Beyond GPU-Dominant Paradigms](cards.md#paper-h4x4aofbgs) | 按端到端吞吐比较 CPU 仿真加 GPU 学习与全 GPU 路线。 |
| 具身智能 | 干预后训练 | [TUTOR: Learning Recovery from Policy-Induced Deviations](cards.md#paper-gusryiaaen) | 把人工接管前轨迹拆成保留与抑制信号。 |
| 具身智能 | 动作适配 | [Cue the Flow: Steering Flow-Matching Policies for Open-World Delivery Manipulation](cards.md#paper-o4lqtmhytc) | 将空间线索映射成预训练动作块的对角仿射校正。 |
| 具身智能 | 移动操作 | [MoFlo: Language-Conditioned Flow Matching for Policy Mobilization](cards.md#paper-bjpoaczbrx) | 让固定操作策略的可执行底盘位姿依赖语言与当前观测。 |
| 具身智能 | 弱监督 | [SurgVIL: Scaling Surgical Robot Imitation Learning with Open-source Surgical Videos](cards.md#paper-qouwcatc3d) | 把缺机器人动作的真实域视频补成弱运动监督，与准确窄域数据混训。 |
| 具身智能 | 噪声条件训练 | [Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics](cards.md#paper-sh0dg0hwvk) | 按扩散噪声水平限制次优示范的贡献。 |
| 具身智能 | 监督路由 | [Supervise What Survives: Geometry-Guided VLA Adaptation from Synthetic Robot Videos](cards.md#paper-dfblf2ss7m) | 只以生成视频监督视觉几何，不用伪动作监督控制头。 |
| 具身智能 | 上下文模仿 | [SynthICL: Scalable In-context Imitation Learning with Synthetic Data](cards.md#paper-6phgtk73zs) | 在 RGB 合成轨迹上下文训练中加入下一子目标图像预测。 |
| 具身智能 | 实景仿真 | [RoboSnap: One-Shot Real-to-Sim Scene Generation for Generalizable Robot Learning and Evaluation](cards.md#paper-mwj9u2vzpx) | 把物理接触区域与视觉背景拆成两层重建。 |
| 具身智能 | 仿真数据诊断 | [SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation](cards.md#paper-8gqhcykrxr) | 分开扰动物体、场景和任务，测哪层变化值得采集。 |
| 具身智能 | 生成表示 | [ArticFlow: Action-Conditioned Flow Matching for Skeleton-Free Articulated Generation](cards.md#paper-xxnpkl2igd) | 用形状潜流和动作条件点流分开建模拓扑变化与形变。 |
| 具身智能 | 场景生成 | [GIF: Agentic Generation of Interactive and Functional Object Compositions for Robot Learning](cards.md#paper-y5z5ccs0bv) | 将物体生成和物理相对位置细化分成两个问题。 |
| 具身智能 | 仿真数据生成 | [IM-ENGINE: Image Editing for Embodied Data Generation](cards.md#paper-6epamjdfwz) | 以未编辑的对象作锚点，把图像生成语义逆映射到可行 3D 状态。 |
| 具身智能 | 策略搜索 | [ExpertGen: Scalable Sim-to-Real Expert Policy Learning from Imperfect Behavior Priors](cards.md#paper-gk8bvfszq3) | 冻结扩散去噪器，只在初始噪声空间做稀疏奖励强化学习。 |
| 具身智能 | 数据增强 | [RoboAug: One Annotation to Hundreds of Scenes via Region-Contrastive Data Augmentation for Robotic Manipulation](cards.md#paper-db6whoqh91) | 用区域对比损失把注意力保留在增强后仍与任务相关的区域。 |
| 具身智能 | 数据质量诊断 | [World In Your Hands: A Large-scale Dataset for Learning Ego-centric Robotic Manipulation In-the-Wild](cards.md#paper-waipztsrpq) | 对自视角预训练优先验证动作标注质量，再追加数据。 |
| 具身智能 / 多模态 | 标注校准 | [SPARC: Reliable Spatial Annotations from Robot Demonstrations at Scale](cards.md#paper-gx5xey9ade) | 用操作阶段和跨帧一致性校准空间伪标签，再按精度要求选择训练样本。 |
| 具身智能 / Agent | 数据生成 | [SkillWeaver: Agentic Exploration over Neural Interaction Skills for Scalable Robot Data Generation](cards.md#paper-uznhskkaab) | 将闭环交互技能作为树搜索动作，在执行失败后重规划并采集恢复示范。 |
| 具身智能 / 模仿学习 | 主动数据采集 | [GUILD: Guided Iterative Data Collection for Imitation Learning](cards.md#paper-6txmwx1wih) | 在采集前用任务归因反馈选择下一批遥操数据。 |
| 具身智能 / 模仿学习 | 多动作监督 | [CrowdMAPS: Crowdsourcing Multiple Actions per State for Real-World Robot Imitation Learning](cards.md#paper-gvdqtvona1) | 为已访问状态标注多个可行动作，和继续采集新轨迹比较标注收益。 |
| 具身智能 | 训练诊断 | [An Empirical Study of Data-Loading Bottlenecks (and Non-Bottlenecks) in Robotic Imitation Learning](cards.md#paper-vv1wxmkstd) | 决定是否优化数据加载前先做端到端剖析 |
| 具身智能 | 数据归因 | [ATHENA: Accelerated Multi-Task Heterogeneous Influence Functions for Robot Data Curation](cards.md#paper-dpgz9kssgo) | 在多任务 VLA 上用可扩展影响估计筛选示范 |
| 具身智能 | 仿真设计 | [Active Generative Simulation: Meta-Learning What to Simulate for Sim-and-Real Policy Co-Training](cards.md#paper-xxhkql5u5p) | 用少量真实验证反馈学习模拟器采样分布 |
| 具身智能 | 损失重加权 | [Where Small Mistakes Matter: Quantifying State Criticality for Imitation Learning](cards.md#paper-x05rf7l7h4) | 按小动作误差造成的下游价值损失给示范状态加权 |
| 具身智能 | 系统辨识 | [Sim-to-Real Transfer for Muscle-Actuated Robots via Generalized Actuator Networks](cards.md#paper-58lip3p4hu) | 无扭矩传感器时用关节轨迹辨识执行器并保留刚体求解器 |
| 具身智能 | 仿真建模 | [Do Rigid-Body Simulators Dream of Soft Robots? Learning Contact-Rich Manipulation for Tendon-Driven Continuum Robots](cards.md#paper-dykg3ed5wy) | 用有物理依据的离散结构将软体接触和肌腱纳入同一仿真 |
| 具身智能 | 测试时适配 | [Scouting the Dynamics Gap: Test-Time Policy Adaptation via Action-Outcome Feedback](cards.md#paper-fyntpa7rwn) | 用动作结果预测误差在线更新共享动力学信念 |
| 具身智能 | 系统辨识 | [Drifting on Demand: A Profiled-Likelihood Transformer for Online Parameter Estimation](cards.md#paper-zwuhb2fawb) | 状态残差各通道尺度变化时分离动力学参数与噪声估计 |
| 具身智能 | 物性估计 | [Beyond Semantic Classes: Online Physical Parameter Estimation via Embedding-Conditioned Gaussian Mixtures](cards.md#paper-y6pog6ygix) | 按连续视觉嵌入检索交互历史并保留物性多峰分布 |
| 具身智能 | 动力学正则 | [Sensitivity Shaping for Latent Modeling](cards.md#paper-kggi0115rg) | 拟合动力学时在高支持区域保留局部控制敏感性 |
| 具身智能 | 生成式策略 | [Learning Robust Visuomotor Policies via Dynamics Alignment](cards.md#paper-cautgdv8l0) | 让动作流与未来观测流在采样时交互更新 |
| 具身智能 | 对称性发现 | [Discovering Control Symmetries via Transition Manifold Tangency](cards.md#paper-xl2er7x00h) | 用转移流形的切向条件检查动力学对称性 |
| 具身智能 | 等变模仿 | [MIRROR: Reflecting Hidden Symmetries from Offline Robot Interaction Data](cards.md#paper-glj2rsqis4) | 从离线转移联合学习观测和动作的群作用 |
| 具身智能 | 数据增强 | [DexNinja: Learning Robust Dexterous Cutting Policy with a Real-to-Sim-to-Real Data Engine](cards.md#paper-sie2lx2haf) | 按类别物性约束扩增会改变物体拓扑的接触示范 |
| 具身智能 | 动作条件 | [Dex4D: Task-Agnostic Point Track Policy for Zero-Shot Dexterous Manipulation](cards.md#paper-qa1uu7lc8n) | 用物体中心三维点轨迹作为任务无关的策略接口 |
| 具身智能 | 采集接口 | [YUBI: Yielding Universal Bidigital Interface for Bimanual Dexterous Manipulation at Scale](cards.md#paper-qahhxvxhtb) | 要复用双臂示范时让采集夹爪与部署夹爪共享动作语义 |
| 具身智能 | 硬件设计 | [Belt-Finger: An Affordable Soft Belt-Driven Gripper for Dexterous In-Hand Manipulation](cards.md#paper-gseucglnto) | 狭窄工作区将夹内平移和旋转交由驱动带完成 |
| 具身智能 | 奖励设计 | [Assembling Two Parts in One Hand](cards.md#paper-eb5tktrt2x) | 以两零件相对位姿和手指分工奖励训练单手装配 |
| 具身智能 | 强化学习后训练 | [ADEPT: Accelerating Dexterity via Pre-Training and Post-Training using Reinforcement Learning](cards.md#paper-2qcsjfv9pr) | 新奖励下先冻结 actor 暖启动 critic，再保守更新 |
| 具身智能 | 行为动力学 | [Going with the Flow: Koopman Behavioral Models as Pseudo Planners for Visuo-Motor Dexterity](cards.md#paper-8t3fxlyk9k) | 以预测视觉流与实际偏差触发按需重规划 |
| 具身智能 | 空间对齐 | [Dexterity-BEV: Aligning 3D World and Actions for Generalizable Robot Policies Learning](cards.md#paper-z5cgs0xgek) | 把每个相机像素对应几何和动作统一到规范鸟瞰坐标 |
| 具身智能 | 异步策略 | [LiMA: Bridging Long-term Imagination to Real-time Dexterous Manipulation via Asynchronous Diffusion](cards.md#paper-fsgxevflkn) | 用熵正则桥将低频意图约束传给高频控制 |
| 具身智能 | 风险塑形 | [How to Learn from What a Human Would Avoid? Intervention-Aware World Models with Real-World RL for Dexterous Manipulation](cards.md#paper-lgosjtsr5q) | 把人类接管的预测概率作为 actor 的前瞻风险代价 |
| 具身智能 | 状态预测 | [Physics-Aware Object-Centric SE(3) Forecasting for Real-Time Proactive Dynamic Grasping](cards.md#paper-tqrhdxuapa) | 动态接触时只预测决定接触时机的物体 SE(3) 状态 |
| 具身智能 | 主动感知 | [MIND-Grasp: Multi-View Imagination-Guided Next-Best-Action Discovery for Occlusion-Aware Grasping](cards.md#paper-mzgjyghofg) | 未知目标位置时先搜可见通道，只有关键遮挡才搬动 |
| 具身智能 | 依赖图规划 | [Minimal-Intervention Target Retrieval in Cluttered Scenes with Grasp-Conditioned Dependency Graphs](cards.md#paper-ng11daafix) | 按候选抓取和动作阶段预测真正的阻挡对象 |
| 具身智能 | 力控制 | [How Firm Should a Grasp Be?](cards.md#paper-iianoce27q) | 在抓取过程中估计物性并按物性调最低所需夹持力 |
| 具身智能 | 视觉蒸馏 | [Anchoring Attention in Clutter: Mask-Guided Latent Distillation for Vision-Language-Action Towards Dexterous Grasping](cards.md#paper-fgyol5tngl) | 把训练期区域掩膜变成控制路径内的注意力监督 |
| 具身智能 | 主动重建 | [AURORA: Active Uncertainty-Driven Re-Orientation for In-Hand Reconstruction](cards.md#paper-cpy2rsdnji) | 按候选观测射线的不确定性决定手内转动目标 |
| 具身智能 | 示范重加权 | [PACER: Process-Aware VLA Policy Learning from Human Corrections for Robotic Disassembly](cards.md#paper-fub1lcfk9g) | 对人类纠错按流程证据重加权，沿用原 VLA 训练目标 |
| 具身智能 | 异步多模态 | [T-Rex: Tactile-Reactive Dexterous Manipulation](cards.md#paper-kdaclhheut) | 让高频触觉支路以自身速率编码，再与低频视觉动作模型交互 |
| 具身智能 | 触觉训练诊断 | [Touch2Trace: Tactile-Driven Imitation Learning for Dexterous Cable Tracing](cards.md#paper-alllacthkq) | 对连续接触任务分别比较控制频率、触觉分辨率与时序上下文 |
| 具身智能 | 触觉融合 | [SlipSense: Multimodal Tactile Learning for Low-Latency and Generalized Slip Detection](cards.md#paper-anfrrenqmn) | 同时观测接触压力与摩擦振动，以低延迟判断滑移 |
| 具身智能 | 触觉表示 | [Learning with Object-centric Representations of Tactile Interactive Perception for Robot Manipulation](cards.md#paper-s0rbnmokit) | 从探索过程选择少量表征片段，将物性上下文提供给操作策略 |
| 具身智能 | 数据生成 | [ControlTac: Scaling Tactile Data with Physically Controlled Tactile Image Generation](cards.md#paper-7ymfgwpcww) | 生成触觉样本时明确控制接触力、位姿和传感器参照 |
| 具身智能 | 示范采集 | [What is the Better Curriculum: Controller-Shaped Grasping Behavior for Contact Force-Sensitive Manipulation](cards.md#paper-f3dic5djnz) | 用触觉反射在线修正示范 |
| 具身智能 | 视觉表征 | [Robot-DIFT: Correspondence-Sensitive Diffusion Features for Contact-Rich Robot Manipulation](cards.md#paper-zshxqqyhfn) | 用蒸馏保留稠密对应，再比较多尺度读出 |
| 具身智能 | 等变表示 | [Equivariant Visual-Tactile Diffusion Policy for Contact-Rich Manipulation](cards.md#paper-40csfpl2cq) | 用末端姿态旋转共享视触球谐表示 |
| 具身智能 | 柔顺控制 | [TDC: Sim-to-Real Transferable Directional Compliance for Contact-Rich Manipulation](cards.md#paper-lomft7cfyl) | 从仿真迁移柔顺方向，现场调幅度 |
| 具身智能 | 柔顺控制 | [CompVLA: A Variable Compliance Vision-Language-Action Model for Contact-rich Manipulation](cards.md#paper-9snxcyklb0) | 为运动策略设置单独的柔顺参数专家 |
| 具身智能 | 候选规划 | [DexFLEX: Contact-Aware Foundation Controller for Command-Guided Dexterity](cards.md#paper-kduigyxutd) | 以预测的接触稳定性筛选上游动作草案 |
| 具身智能 | 动作接口 | [Mind the Gap: Rethinking I/O Design for Contact-Rich Visuomotor Policy Learning](cards.md#paper-patsmtswir) | 同时条件化执行状态和领导器命令，预测未来命令 |
| 具身智能 | 持续学习 | [Multisensory Continual Learning: Adapting Pretrained Visuomotor Policies to Force](cards.md#paper-netxisu52q) | 为新传感器做未来预测，并回放旧视觉数据 |
| 具身智能 | 探索奖励 | [Tactile Curiosity Drives Robot Interaction](cards.md#paper-h26amtgnfu) | 把好奇心奖励限制到触觉不确定性 |
| 具身智能 | 失败诊断 | [KlaskTron-IL: A Contact-Rich Adversarial Imitation Learning Benchmark with a Validated Sim-to-Real Bridge](cards.md#paper-ik1sflqgza) | 同时检查判别器语义准确性和用于优化的梯度 |
| 具身智能 | 世界模型 | [FACA: Force-Aware Contact Adaptation for Task-Parameterized Robotic Assembly](cards.md#paper-ch33xueibo) | 分开已知装配参数与在线隐式接触残差 |
| 具身智能 | 多模态标注 | [ForceBand: Learning Forceful Manipulation with sEMG](cards.md#paper-w2h90oezfp) | 先用力数据校准腕带，再以其自动标注目标示范 |
| 具身智能 | 示范采集 | [Hardware-as-Regularization: Enhancing Data Consistency in Imitation Learning via an Adjustable Passive Compliant Leader Arm](cards.md#paper-riyiqwvpst) | 以可调机械复位作为冗余关节的采集先验 |
| 具身智能 | 系统辨识 | [Just Learn It: A Data-Harvesting Protocol for Empirical Learning of Effective Assistance Torques in Coupled Systems](cards.md#paper-tu2sheg4to) | 通过缓慢被动运动隔离配置相关负载再学习前馈 |
| 具身智能 | 合成数据 | [Unleashing Infinite Motion: Scaling Expressive Quadrupedal Motion via Generative Video Priors](cards.md#paper-oias4zzrun) | 给视频合成加跨帧本体身份约束再提取运动 |
| 具身智能 | 价值估计 | [MorFiC: Fixing Value Miscalibration for Zero-Shot Quadruped Transfer](cards.md#paper-x7qoq3qota) | 在 critic 用乘法形态条件化避免跨本体价值平均 |
| 具身智能 | 世界模型 | [Morphology-Conditioned World Model for Cross-Embodiment Quadrupedal Locomotion](cards.md#paper-yqoallpdd3) | 把形态描述输入动力学而不仅是 actor |
| 具身智能 | 奖励设计 | [LoComposition: Terrain-Adaptive Energy-Efficient Quadruped Locomotion without Gait Priors](cards.md#paper-ss9fjkkksm) | 将运行边界写约束，让能耗目标诱导步态 |
| 具身智能 | 特权监督 | [Physics-Guided Biomechanical Gait Adaptation for Humanoid Locomotion on Extreme Sloped Terrains](cards.md#paper-vkvm1q9fbn) | 按坡面坐标定义稳定性，并仅在训练时使用坡度调节奖励 |
| 具身智能 | 深度蒸馏 | [RPL: Learning Robust Humanoid Perceptive Locomotion on Challenging Terrains](cards.md#paper-zyppmdicvv) | 按命令速度调整深度特征并随机遮侧视角 |
| 具身智能 | 奖励设计 | [Hiking in the Wild: A Scalable Perceptive Legged Parkour Framework for Humanoid Robots](cards.md#paper-o7lrmassjs) | 只采样可站立目标并用足部体积约束边缘着地 |
| 具身智能 | 时序感知 | [Echo in the Steps: Learning Perceptive Humanoid Parkour with Gated Memory](cards.md#paper-eioq9vj6oj) | 以落足显著性门控深度记忆 |
| 具身智能 | 对称增强 | [SSR: Scaling Surefooted and Symmetric Humanoid Traversal Toward the Open World](cards.md#paper-4it3fcnny2) | 在潜空间做双侧等变增强，并提前判断摆脚支撑 |
| 具身智能 | 动作重定向 | [MeshMimic: Geometry-Aware Humanoid Motion Learning through 3D Scene Reconstruction](cards.md#paper-jbpsghdjs9) | 重定向时保持人和场景接触关系 |
| 具身智能 | 特权蒸馏 | [Perceptive Behavior Foundation Model: Adapting Human Motion Priors to Robot-Centric Terrain](cards.md#paper-c5oil7jqbq) | 部署保留原始动作指令，仅用地形残差在局部修正 |
| 具身智能 | 学习辅助控制 | [MARCH: Model-Assisted Reinforcement Learning for the Perceptive Control of Humanoids over Sparse Footholds](cards.md#paper-iy6ti85pg0) | 用简化模型安全轨迹构造 Lyapunov 奖励再蒸馏 |
| 具身智能 | 轨迹蒸馏 | [SOLO: Stable Omni-terrain Long-Horizon Perceptive Humanoid Locomotion](cards.md#paper-jwkaxdmqkb) | 把下一状态的师生分歧放进 RL 奖励 |
| 具身智能 | 传感回退 | [PROOF: Perceptive Robustness via Out-of-Distribution Fallback for Legged Locomotion](cards.md#paper-317szv2vus) | 训练本体感知回退，并以外感不确定性抑制受损特征 |
| 具身智能 | 感知去噪 | [CAP: Continuously Adaptive Perception-Blind Humanoid Locomotion via Learned Denoising](cards.md#paper-oq5byppu7q) | 部分深度损坏时连续使用剩余信号 |
| 具身智能 | 预测控制 | [RoboDreamer: Anticipatory Humanoid Locomotion with Predictive State-Space Models](cards.md#paper-umgoyxmgn2) | 用时序遮蔽训练状态空间模型补全观测 |
| 具身智能 | 结构化动作 | [HAF-VLA: Hierarchical Action Flow Framework for Humanoid Vision-Language-Action Control](cards.md#paper-l9rkfeukrc) | 按移动、腰部和操作顺序细化同一全身动作 |
| 具身智能 | 残差强化学习 | [ADAPT: Agile Diffusion Action Priors for Robust and Steerable Online Text-Driven Humanoid Control](cards.md#paper-7uebdg4kra) | 用残差策略补偿冻结语言动作先验的长程误差 |
| 具身智能 | 候选验证 | [TEXEDO : Test Time Scaling for Controller-aware Language-conditioned Humanoid Motion Generation](cards.md#paper-uscrywxsuc) | 先硬筛动态可行，再按语言匹配排序 |
| 具身智能 | 闭环生成 | [InfiniDanceRobot: A Streaming and Closed-Loop Music-driven Dance Generation for Humanoid Robot](cards.md#paper-93legzrapv) | 训练和推理都用跟踪器反馈校正下一动作潜变量 |
| 具身智能 / 腿式控制 | 本体动力学 | [HumanoidNDM: Closing the Training-Deployment Gap of Motion Tracking via Humanoid Neural Dynamics Model](cards.md#paper-xcdyj95l5p) | 按适应强度低频扰动参考，结合可微正运动学训练历史动力学，再通过模型梯度微调 |
| 具身智能 / 腿式控制 | 黑盒适配 | [CLIFT: Turning Gemini Robotics On-Device into Humanoid Specialists via Non-Invasive Closed-Loop Iterative Fine-Tuning](cards.md#paper-ht8whuvp22) | 将部署奖励反馈转化为下一轮监督数据，反复调用托管接口 |
| 具身智能 / 腿式控制 | 动力学适配 | [FADA: Few-Shot Domain Adaptation via Dynamics Alignment for Humanoid Control](cards.md#paper-mmrhlrwlfx) | 用 DAgger 蒸馏特权教师为规划器和逆动力学，部署仅微调逆模型 |
| 具身智能 / 腿式控制 | 残差辨识 | [Unsupervised Actuator Networks as a Residual World Model for Humanoid Control](cards.md#paper-8klpl3fxjn) | 从本体传感对齐浮基速度及接触力，再开环回放辨识执行器残差 |
| 具身智能 / 腿式控制 | 扰动观测 | [ADAPT: Analytical Disturbance-Aware Policy Training for Humanoid Locomotion](cards.md#paper-pqdtunzqlj) | 将解析全身扰动观察器的力矩残差直接输入策略 |
| 具身智能 / 腿式控制 | 动作风格 | [Walk Like This: Stylized Locomotion for Physics-Based Characters through Example-Driven Diffusion](cards.md#paper-u2oevtdvx8) | 采样训练风格编码器，以参考片段和速度条件自回归扩散生成可跟踪动作 |
| 具身智能 / 腿式控制 | 平衡表示 | [Koopman DCM: Unstable Eigenfunctions as Data-driven Representations for Legged Balancing](cards.md#paper-mday00wzfr) | 从测量历史寻找不稳定 Koopman 特征函数并按控制耦合正则化 |
| 具身智能 / 腿式控制 | 动力学课程 | [Actuator Dynamics Curricula for Narrow-Viability Tasks in Legged Robot Learning](cards.md#paper-mru8ihzsqr) | 从高刚度开始并按完成时长逐步退火到辨识刚度 |
| 具身智能 / 腿式控制 | 课程学习 | [Trajectory-Level Automatic Curriculum Learning for Legged Locomotion on Unstructured Terrain](cards.md#paper-0muj0bxujh) | 按当前策略学习轨迹难度，迭代引导地图上的轨迹采样 |
| 具身智能 / 腿式控制 | 在线适配 | [SHOES: Sim-to-real Hardware-adaptation via On-policy Expansion of Skills for Legged Robots](cards.md#paper-rje0dllpev) | 冻结原策略，训练恒等初始化调制模块，以工作区采样限制收集 |
| 具身智能 / 腿式控制 | 故障训练 | [Damage-Aware Quadruped Locomotion: Zero-Shot Adaptation to Motor Failures via Pain-Inspired Reinforcement Learning](cards.md#paper-jwpvrd730l) | 将健康线索接入策略与奖励，并课程式提高故障概率 |
| 具身智能 / 腿式控制 | 表示诊断 | [Mind the Phase: Effective Rank and Representation Health in Legged Locomotion](cards.md#paper-fk33gnkkgf) | 按摆动和支撑分别统计雅可比有效秩，比较归一化及残差结构 |
| 具身智能 / 腿式控制 | 奖励设计 | [Push the Limit: Learning High-Speed Sprinting and Aggressive Cornering on a Full-Scale Humanoid](cards.md#paper-xqgbzwsuxt) | 用低频速度方向取代瞬时偏航率目标，辅以时序注意力与技能条件判别器 |
| 具身智能 / 腿式控制 | 专家优化 | [MAPO: Mixture of Experts with Alternating Policy Optimization for Universal Humanoid Motion Tracking](cards.md#paper-tk1gtgoesr) | 交替更新专家与路由器以避免同步更新混淆 |
| 具身智能 / 腿式控制 | 柔顺控制 | [CHIP: Adaptive Compliance for Humanoid Control through Hindsight Perturbation](cards.md#paper-gqmj7sik5q) | 事后按扰动改写稀疏目标，保留稠密参考 |
| 具身智能 / 腿式控制 | 安全值学习 | [λ-Reachability: Geometric-Horizon Safety Bellman Equations for Humanoid Safety](cards.md#paper-siyferhqrn) | 采用几何分布的随机预测长度与概率吸收终点，构造多步安全值估计 |
| 具身智能 / 腿式控制 | 回放设计 | [MPC-Injection: Biasing Off-Policy Locomotion RL Toward Controller-Induced Behavior Basins](cards.md#paper-0hs0to0evo) | 把求解同一 MDP 的 MPC 转移加入离策略回放 |
| 具身智能 / 腿式控制 | 技能复用 | [Continual Quadruped Robots Coordination via Sementic Skill Discover](cards.md#paper-2xr8oasjum) | 显式分别编码自身、队友及目标，以任务语义检索，成功后按轨迹语义更新技能库 |
| 具身智能 / 导航与驾驶 | 开闭环诊断 | [BridgeSim: Unveiling the OL-CL Gap in End-to-End Autonomous Driving](cards.md#paper-ynmzwxz68a) | 分别分析观测偏移与目标错配，并在测试时校准偏移、值偏差和时间一致性 |
| 具身智能 / 导航与驾驶 | 自博弈蒸馏 | [Scaling Self-Play for End-to-End Driving](cards.md#paper-eszgt1eizr) | 简化透视渲染，在学生在线自博弈状态向特权 RL 教师蒸馏，再迁移感知 |
| 具身智能 / 导航与驾驶 | 仿真度量 | [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](cards.md#paper-lqur3gxkdh) | 在多个公开策略的场景特征空间测 Fréchet 距离 |
| 具身智能 / 导航与驾驶 | 闭环模仿 | [DriveMLP: When Training Strategy Outperforms Model Complexity in Autonomous Driving](cards.md#paper-9ccdcinkm9) | 以专家轨迹距离为奖励，在闭环用 RL 优化轻量 MLP |
| 具身智能 / 导航与驾驶 | 判断后优化 | [Judge, Then Act: A Critic-Centric Vision Language Action Framework for Autonomous Driving](cards.md#paper-ckvuqg4yqf) | 先生成草案，再用多模态 VLA 评估并做一次优化 |
| 具身智能 / 导航与驾驶 | 可验证元动作 | [DriveMA: Driving Vision-Language-Action Models with verifiable Meta-Actions](cards.md#paper-b7gccztjye) | 以规则从轨迹抽取并核验元动作，指导监督训练和轮次信用分配 |
| 具身智能 / 导航与驾驶 | 几何预测 | [GeoWorldAD: Geometry World Action Model for Autonomous Driving](cards.md#paper-eweki0rf6v) | 以未来深度监督学习自车条件几何 token，用当前和未来 token 精修轨迹 |
| 具身智能 / 导航与驾驶 | 瓶颈监督 | [NTR: Neural Token Reconstruction for Scene Token Bottleneck in End-to-End Driving](cards.md#paper-f4ib3mxhbo) | 只允许解码器读取场景 token 重建掩蔽图块潜变量，推理时移除重建组件 |
| 具身智能 / 导航与驾驶 | 可解释诊断 | [Mechanistic Interpretability for End-to-End Self-Driving](cards.md#paper-bqxys2gkba) | 用稀疏自编码器提取特征，以配对反事实编辑和激活干预区分关联与因果 |
| 具身智能 / 导航与驾驶 | 动作表示 | [CoFL-S: Spatially Queryable Sector Flow Fields for Local Language-Conditioned Navigation](cards.md#paper-hi8mv09noi) | 预测可查询的方位扇区流场，从原轨迹构造逐帧子指令和流监督 |
| 具身智能 / 导航与驾驶 | 序贯判断 | [Observe Before You Alert: Belief-State Driver Alerting with Vision–Language Models](cards.md#paper-g6vrrbo3ne) | 增加内部观察动作，按需累计证据再告警，以结构化安全证据池化为信念 |
| 具身智能 / 导航与驾驶 | 剪枝时点 | [Before Parc Fermé: RL-Time Pruning for Efficient Embodied LLMs in Autonomous Driving](cards.md#paper-jydy4anb01) | 在 RL 训练仍有任务反馈时分阶段裁剪，也可提前在 SFT 裁剪一部分 |
| 具身智能 / 导航与驾驶 | 仿真评测 | [EvoDrive: Pareto Evolution for Safety-Critical Autonomous Driving via Self-Improving LLM Agents](cards.md#paper-omvckdflra) | 在封闭模拟器测试中保存多目标非劣案例，继续验证多种安全边界 |
| 具身智能 / 导航与驾驶 | 计算路由 | [An Adaptive Slow-Fast Framework for Real-Time Anomaly Detection in Autonomous Driving](cards.md#paper-egz6ymfvzu) | 以快速 LiDAR 异常检测常开，按碰撞时间切换昂贵语义推理 |
| 具身智能 / 导航与驾驶 | 几何蒸馏 | [From Foundation VLM to Versatile Driving VLM: A Triplet Incremental Training Approach](cards.md#paper-022k2zipr6) | 图像、深度、问答三元训练；辅助深度分支补几何，冻结副本用 logits KL 保语义 |
| 具身智能 / 导航与驾驶 | 推理预算 | [FlashDrive: Flash Vision-Language-Action Inference Framework for Autonomous Driving](cards.md#paper-sdujbb3p4e) | 跨帧复用缓存、对推理 token 并行预测，按去噪速度变化缓存步进 |
| 具身智能 / 导航与驾驶 | 状态条件模型 | [Structured Perception Representations for Off-road Dynamics Learning](cards.md#paper-vvivf2e7kg) | 每个预测步围绕当前预测状态查询鸟瞰地形特征 |
| 具身智能 / 导航与驾驶 | 规划蒸馏 | [VIGOR-MPC: Vision-Guided Objective Regulation MPC](cards.md#paper-alu9elt93i) | 从特权长时教师蒸馏视觉条件的代价参数，让短时 MPC 保留控制结构 |
| 具身智能 / 导航与驾驶 | 残差控制 | [CoPark: Learning Reactive Parking via Self-Play](cards.md#paper-mskud5twyj) | 按风险调节纵向残差权重，横向保持路径锚定，并做末端闭环修正 |
