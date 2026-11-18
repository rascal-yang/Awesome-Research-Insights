# CoRL 2026

[首页](../../README.md) · [官方录用名单](https://2026.corl.org/program/accepted-papers)

已筛选 **115 / 687** 篇，当前收录 **112** 篇。[筛选底册](papers.tsv)录用名单按 OpenReview 论文 ID 去重。通过收录门槛的论文进入后续统一评分，保留比例上限为 50%。

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
