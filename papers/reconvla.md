# ReconVLA 论文卡

[机器人学索引](robotics.md)

<a id="paper-reconvla"></a>

## ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver

[原文](https://arxiv.org/abs/2508.10333)

- **问题 / 瓶颈** · 现有机器人 VLA 的视觉注意力容易散落在背景上，精细操作依赖对指令指定物体的定位。
- **核心创新 / 方法** · 把指令词元置于图像词元之前，再用扩散解码器重建同一图像中的目标裁剪区域，给动作策略的视觉特征提供辅助训练监督。
- **Baseline** · 改进来源为使用因果注意力的 VLA。实验对照含同一底座上的显式目标裁剪、输出目标框的 CoT Grounding、去掉重建或目标裁剪的消融，以及 OpenVLA、PD-VLA 等系统。
- **Benchmark** · CALVIN 五步任务链在 ABC→D 等划分上做 500 次 rollout，报各步成功率和平均完成长度。真机用 AgileX PiPer 机械臂做水果入碗、叠碗、翻杯和清桌，每模型每任务评 20 次。
- **关键结果 / 消融** · CALVIN ABC→D 全模型平均完成 3.95 步、五步成功率 64.1%，去掉重建及相关设置的基线为 3.36 步和 49.0%，保留目标区域重建但去掉预训练为 3.85 步和 58.2%。真机四项任务中全模型均高于 OpenVLA 和 PD-VLA。
- **适用条件 / 局限** · 训练阶段需能标出或提取指令目标区域，并依赖机器人示范。未见目标的泛化评测是四类操作中的物体替换，真机使用同一机械臂，跨硬件迁移未在该实验中报告。

**原文定位** · [§§3.2–3.3、图 3（PDF 第 4 页）](https://arxiv.org/pdf/2508.10333#page=4) · [§4.4、表 2（PDF 第 6 页）](https://arxiv.org/pdf/2508.10333#page=6) · [§4.6、图 5–6（PDF 第 7 页）](https://arxiv.org/pdf/2508.10333#page=7)

**首次公开 / 发表** · 2025-08-14 · [AAAI 2026](https://ojs.aaai.org/index.php/AAAI/article/download/38921/42883)

**资源** · [项目](https://zionchow.github.io/ReconVLA/) · [代码](https://github.com/OpenHelix-Team/ReconVLA)

<a id="target-region-reconstruction-as-auxiliary-supervision"></a>
<a id="reconvla-loss-functions"></a>

### 用目标区域重建做辅助监督

**来源**

ReconVLA（Song 等，AAAI 2026） · [§§3.2–3.3、图 3 与公式 3（PDF 第 4 页）](https://ojs.aaai.org/index.php/AAAI/article/download/38921/42883#page=4) · [§4.4、表 2（PDF 第 6 页）](https://ojs.aaai.org/index.php/AAAI/article/download/38921/42883#page=6)

**核心思路**

给策略增加一个辅助目标，让它的特征能恢复与当前任务有关的局部区域。策略输入和辅助目标来自同一张图像。

**实现机制**

训练时，用能根据语言指令定位目标的检测器制作物体裁剪图。用 VAE 把裁剪图编码为潜变量并加噪，再用扩散 Transformer 预测噪声。去噪器以策略主干产生的重建 token 为条件。去噪损失与动作 token 的交叉熵一起优化。部署时，策略用常规观测和指令输出动作。

**设计动机**

作者发现，预测动作时模型的注意力容易散到干扰物上。重建局部目标为共享表征提供了训练信号，使它有理由保留操作对象的细节。

**潜在应用**

- **论文证据 · 机器人操作。** CALVIN ABC→D 中，在未加入大规模预训练的条件下，重建目标区域平均连续完成 3.85 项任务（满分 5），重建整图为 3.42，基线为 3.36（表 2）。
- **迁移设想 · 小型视觉运动策略。** 可以对送入动作头的特征加目标区域或接触区域监督，例如用仿真真值投影得到训练用裁剪区域。把扩散分支换成轻量特征预测头是一个待验证的改法。

<details>
<summary>English</summary>

**Source**

ReconVLA (Song et al., AAAI 2026) · [§§3.2–3.3, Figure 3 and Eq. 3（PDF 第 4 页）](https://ojs.aaai.org/index.php/AAAI/article/download/38921/42883#page=4) · [§4.4, Table 2（PDF 第 6 页）](https://ojs.aaai.org/index.php/AAAI/article/download/38921/42883#page=6)

**Core Idea**

Train a policy representation to recover the region the task depends on. The same camera image supplies the policy observation and the pixels used to build the auxiliary target.

**Mechanism**

Use an instruction-conditioned detector to prepare a target crop for training. Encode the crop with a VAE, add noise to its latent tokens, and train a diffusion transformer to predict the noise using reconstruction tokens from the policy backbone as its conditioning. Optimize the denoising loss jointly with action-token cross-entropy. At deployment, the policy takes its usual observations and instruction and emits actions.

**Motivation**

The authors observed that action prediction could attend to distractors. A target-region objective gives the shared representation a direct reason to retain fine details of the object being acted on.

**Potential Applications**

- **Paper evidence · Robot manipulation.** On CALVIN ABC→D, without large-scale pretraining, target-crop reconstruction averaged 3.85 consecutive tasks completed out of 5, versus 3.42 for whole-image reconstruction and 3.36 for the baseline (Table 2).
- **Transfer hypothesis · Small visuomotor policies.** Supervise the features that feed the action head using target or contact patches. This requires reliable per-frame crops during training, such as projected ground-truth boxes in simulation. A lightweight feature-prediction head is a possible adaptation whose effectiveness needs testing.

</details>

<a id="instruction-prefixes-for-causal-visual-grounding"></a>
<a id="reconvla-modules"></a>

### 用指令前缀让视觉表征感知任务

**来源**

ReconVLA（Song 等，AAAI 2026） · [§3.2、图 3 与因果注意力说明（PDF 第 4 页）](https://ojs.aaai.org/index.php/AAAI/article/download/38921/42883#page=4)

**核心思路**

如果下游模块读取因果解码器里的图像 token，把任务指令放在图像 token 前面，使这些视觉隐藏状态能读到指令。

**实现机制**

在标准因果掩码下，一个位置只能读取自己与此前位置。ReconVLA 把指令 token 放在图像 token 前面，让用于给重建分支提供条件的视觉状态能融合任务信息。顺序调整发生在多模态解码器中，视觉编码器仍单独处理图像。

**设计动机**

同一张图里可能有多个可操作物体。重建分支要恢复指令指定的物体，读到的视觉状态需要带有区分当前目标的信息。

**潜在应用**

- **论文用法 · 语言条件重建。** ReconVLA 在重建流程中使用这一顺序。论文对该设计的结论来自完整系统，单独改变 token 顺序对策略成功率的影响待验证。
- **迁移设想 · 仅解码器式视觉语言策略。** 如果辅助头读取图像 token 的隐藏状态，可以把目标指令或问题移到图像 token 之前。迁移前看清注意力掩码和读出位置。若读出位置本来就在指令之后，两种排列都可能让辅助头读到指令。

<details>
<summary>English</summary>

**Source**

ReconVLA (Song et al., AAAI 2026) · [§3.2, Figure 3 and the causal-attention discussion（PDF 第 4 页）](https://ojs.aaai.org/index.php/AAAI/article/download/38921/42883#page=4)

**Core Idea**

Put the task instruction before the image tokens when a causal decoder needs to produce task-conditioned visual representations.

**Mechanism**

In a decoder with a standard causal mask, an image-token hidden state can attend to earlier instruction tokens. ReconVLA places instruction tokens before image tokens so that the visual states used to condition the reconstruction branch can carry task information. The order acts inside the multimodal decoder. The vision encoder still processes the image separately.

**Motivation**

The same image can contain several manipulable objects. A reconstruction target selected by the instruction is easier to represent when the visual states can see the task before the reconstruction head reads them.

**Potential Applications**

- **Paper use · Language-conditioned reconstruction.** ReconVLA uses this layout in its reconstruction pipeline. The paper does not report a controlled token-order ablation that isolates its effect on policy success.
- **Transfer hypothesis · Decoder-only vision-language policies.** Move a goal or question ahead of image tokens if an auxiliary head reads their hidden states. Check the actual attention mask and readout position. A head that already reads a post-instruction state can have access to the goal under either layout.

</details>
