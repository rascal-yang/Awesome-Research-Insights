# 损失函数

[首页](../README.md) · [参与贡献](../CONTRIBUTING.md) · [English](../en/insights/loss-functions.md)

训练目标、辅助监督与正则化。

## 视觉辅助监督

<a id="target-region-reconstruction-as-auxiliary-supervision"></a>

### 用目标区域重建做辅助监督

**来源**

ReconVLA（Song 等，AAAI 2026） · [§§3.2–3.3、图 3 与公式 3](https://ojs.aaai.org/index.php/AAAI/article/download/38921/42883#page=4) · [§4.4、表 2](https://ojs.aaai.org/index.php/AAAI/article/download/38921/42883#page=6) · [论文索引](../papers/robotics.md#vision-language-action-models)

**核心思路**

给策略增加一个辅助目标，让它的特征能恢复与当前任务有关的局部区域。策略输入和辅助目标来自同一张图像。

**实现机制**

训练时，用能根据语言指令定位目标的检测器制作物体裁剪图。用 VAE 把裁剪图编码为潜变量并加噪，再用扩散 Transformer 预测噪声。去噪器以策略主干产生的重建 token 为条件。去噪损失与动作 token 的交叉熵一起优化。部署时，策略用常规观测和指令输出动作。

**设计动机**

作者发现，预测动作时模型的注意力容易散到干扰物上。重建局部目标为共享表征提供了训练信号，使它有理由保留操作对象的细节。

**潜在应用**

- **论文证据 · 机器人操作。** CALVIN ABC→D 中，在未加入大规模预训练的条件下，重建目标区域平均连续完成 3.85 项任务（满分 5），重建整图为 3.42，基线为 3.36（表 2）。
- **迁移设想 · 小型视觉运动策略。** 可以对送入动作头的特征加目标区域或接触区域监督，例如用仿真真值投影得到训练用裁剪区域。把扩散分支换成轻量特征预测头是一个待验证的改法。

相关 Insight · [用指令前缀让视觉表征感知任务](../insights/modules.md#instruction-prefixes-for-causal-visual-grounding)
