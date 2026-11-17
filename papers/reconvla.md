# ReconVLA 论文卡

[机器人学索引](robotics.md)

<a id="paper-reconvla"></a>

## ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver

[原文](https://arxiv.org/abs/2508.10333) · [用目标区域重建做辅助监督](../insights/loss-functions.md#target-region-reconstruction-as-auxiliary-supervision) · [用指令前缀让视觉表征感知任务](../insights/modules.md#instruction-prefixes-for-causal-visual-grounding)

- **问题 / 瓶颈** · 现有机器人 VLA 的视觉注意力容易散落在背景上，精细操作依赖对指令指定物体的定位。
- **核心创新 / 方法** · 把指令词元置于图像词元之前，再用扩散解码器重建同一图像中的目标裁剪区域，给动作策略的视觉特征提供辅助训练监督。
- **Baseline** · 改进来源为使用因果注意力的 VLA。实验对照含同一底座上的显式目标裁剪、输出目标框的 CoT Grounding、去掉重建或目标裁剪的消融，以及 OpenVLA、PD-VLA 等系统。
- **Benchmark** · CALVIN 五步任务链在 ABC→D 等划分上做 500 次 rollout，报各步成功率和平均完成长度。真机用 AgileX PiPer 机械臂做水果入碗、叠碗、翻杯和清桌，每模型每任务评 20 次。
- **关键结果 / 消融** · CALVIN ABC→D 全模型平均完成 3.95 步、五步成功率 64.1%，去掉重建及相关设置的基线为 3.36 步和 49.0%，保留目标区域重建但去掉预训练为 3.85 步和 58.2%。真机四项任务中全模型均高于 OpenVLA 和 PD-VLA。
- **适用条件 / 局限** · 训练阶段需能标出或提取指令目标区域，并依赖机器人示范。未见目标的泛化评测是四类操作中的物体替换，真机使用同一机械臂，跨硬件迁移未在该实验中报告。

**原文定位** · [§§3.2–3.3、图 3](https://arxiv.org/pdf/2508.10333#page=4) · [§4.4、表 2](https://arxiv.org/pdf/2508.10333#page=6) · [§4.6、图 5–6](https://arxiv.org/pdf/2508.10333#page=7)
