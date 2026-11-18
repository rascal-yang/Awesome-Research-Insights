# CoRL 2026

[首页](../../README.md) · [官方录用名单](https://2026.corl.org/program/accepted-papers)

已筛选 **24 / 687** 篇，当前收录 **24** 篇。[筛选底册](papers.tsv)录用名单按 OpenReview 论文 ID 去重。通过收录门槛的论文进入后续统一评分，保留比例上限为 50%。

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
