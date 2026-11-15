# 模块

[首页](../README.md) · [参与贡献](../CONTRIBUTING.md) · [English](../en/insights/modules.md)

可复用组件与局部连接方式。

## 多模态 token 排列

<a id="instruction-prefixes-for-causal-visual-grounding"></a>

### 用指令前缀让视觉表征感知任务

**来源**

ReconVLA（Song 等，AAAI 2026） · [§3.2、图 3 与因果注意力说明](https://ojs.aaai.org/index.php/AAAI/article/download/38921/42883#page=4) · [论文索引](../papers/robotics.md#vision-language-action-models)

**核心思路**

如果下游模块读取因果解码器里的图像 token，把任务指令放在图像 token 前面，使这些视觉隐藏状态能读到指令。

**实现机制**

在标准因果掩码下，一个位置只能读取自己与此前位置。ReconVLA 把指令 token 放在图像 token 前面，让用于给重建分支提供条件的视觉状态能融合任务信息。顺序调整发生在多模态解码器中，视觉编码器仍单独处理图像。

**设计动机**

同一张图里可能有多个可操作物体。重建分支要恢复指令指定的物体，读到的视觉状态需要带有区分当前目标的信息。

**潜在应用**

- **论文用法 · 语言条件重建。** ReconVLA 在重建流程中使用这一顺序。论文对该设计的结论来自完整系统，单独改变 token 顺序对策略成功率的影响待验证。
- **迁移设想 · 仅解码器式视觉语言策略。** 如果辅助头读取图像 token 的隐藏状态，可以把目标指令或问题移到图像 token 之前。迁移前看清注意力掩码和读出位置。若读出位置本来就在指令之后，两种排列都可能让辅助头读到指令。

相关 Insight · [用目标区域重建做辅助监督](../insights/loss-functions.md#target-region-reconstruction-as-auxiliary-supervision)

## 蒸馏接口设计

<a id="widen-the-student-distillation-interface"></a>

### 只加宽学生模型的蒸馏接口

**来源**

[Lift / WideLast](https://proceedings.mlr.press/v306/tian26k.html) (Huiyuan Tian 等, ICML 2026) · [§2.1–2.3](https://raw.githubusercontent.com/mlresearch/v306/main/assets/tian26k/tian26k.pdf#page=4) · [§3.1–3.3、表 2](https://raw.githubusercontent.com/mlresearch/v306/main/assets/tian26k/tian26k.pdf#page=6) · [表 8](https://raw.githubusercontent.com/mlresearch/v306/main/assets/tian26k/tian26k.pdf#page=9) · [论文索引](../papers/computer-vision.md#vision-model-distillation)

**核心思路**

学生 ViT 大幅缩窄时，可以只扩大与教师特征对齐的末端通道，保留前面的大部分窄层。

**实现机制**

Lift 在学生末层之后给每个 token 加线性升维，分类头读取升维后的特征，推理时也保留这层。WideLast 则只把最后一个 Transformer 块加宽到教师宽度。两种情况下都可以对蒸馏接口加特征损失。

**设计动机**

单张图的教师特征即使是低秩，不同图像也可能占据不同子空间。跨图像的共享 PCA 比逐图 SVD 更能检验一个固定窄接口是否覆盖得住教师特征。

**潜在应用**

- **论文证据** · 在 ImageNet-1K 上，CaiT-S24 蒸馏到 DeiT-Tiny 时，原学生 Top-1 为 74.86%，Lift 和 WideLast 的最佳配置分别为 77.53% 和 78.23%（表 2）。加宽在没有蒸馏时也有收益（表 8）。
- **迁移设想** · 可用于小型视觉编码器的特征蒸馏。对比「只加宽」和「加宽加蒸馏」，同时记录部署开销，以区分额外容量和教师监督的作用。
