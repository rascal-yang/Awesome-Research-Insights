# 计算机视觉

[首页](../README.md) · [参与贡献](../CONTRIBUTING.md) · [English](../en/papers/computer-vision.md)

视觉识别、表征学习与生成。

<a id="vision-model-distillation"></a>

## 视觉模型蒸馏

| 论文 | 首次公开 / 发表 | 可借鉴的技术 | 资源 |
| :--- | :--- | :--- | :--- |
| [**Lift / WideLast**](https://proceedings.mlr.press/v306/tian26k.html)<br><sub>Huiyuan Tian 等, From Per-Image Low-Rank to Encoding Mismatch: Rethinking Feature Distillation in Vision Transformers</sub> | 首次公开日期待核实<br><sub>[ICML 2026](https://proceedings.mlr.press/v306/tian26k.html)</sub> | [只加宽学生模型的蒸馏接口](../insights/modules.md#widen-the-student-distillation-interface) | [PMLR](https://proceedings.mlr.press/v306/tian26k.html) · [OpenReview](https://openreview.net/forum?id=2Ud1nkQrVZ) · [代码](https://github.com/thy960112/From-Per-Image-Low-Rank-to-Encoding-Mismatch) |

<!-- classification:start -->
## 按技术类型浏览

<a id="by-architecture"></a>

### 模型架构

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="atanov26a-architecture"></a>[VideoFlexTok: Flexible-Length Coarse-to-Fine Video Tokenization](https://proceedings.mlr.press/v306/atanov26a.html) | 视频分词 | 让视频 token 按粗到细排列，前面少量 token 保留语义与运动，尾部补充细节。生成式解码器可以在不同截断长度重建视频。 |
| <a id="baade26a-architecture"></a>[Latent Forcing: Reordering the Diffusion Trajectory for Pixel-Space Image Generation](https://proceedings.mlr.press/v306/baade26a.html) | 像素空间扩散 | 给潜变量和像素安排不同噪声日程，使模型先形成可作中间计算的潜表示，再补出高频像素细节。 |
| <a id="bao26f-architecture"></a>[Envisioning Beyond the Few: Disentangled Semantics and Primitives for Few-Shot Atypical Layout-to-Image Generation](https://proceedings.mlr.press/v306/bao26f.html) | 少样本布局生成 | 用类别锚点保留对象身份，将局部视觉细节编码成可重组原语，缓解小样本非典型布局生成中的语义碎裂。 |

<a id="by-modules"></a>

### 模块

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="blauch26a-modules"></a>[FOVI: A biologically-inspired foveated interface for deep vision models](https://proceedings.mlr.press/v306/blauch26a.html) | 主动视觉分辨率 | 在传感器坐标中保留中心高分辨率和周边低分辨率，再映射到均匀的处理流形做近邻卷积，减少全视野处理所需的像素与计算。 |
| <a id="tian26k-modules"></a>[From Per-Image Low-Rank to Encoding Mismatch: Rethinking Feature Distillation in Vision Transformers](https://proceedings.mlr.press/v306/tian26k.html) | 视觉特征蒸馏 | 给小型 ViT 的特征输出接口或最后一个 Transformer 块加宽，以匹配教师模型的编码空间。 [详细解读](../insights/modules.md#widen-the-student-distillation-interface) |

<a id="by-loss-functions"></a>

### 损失函数

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="bai26c-loss-functions"></a>[Threshold-Guided Optimization for Visual Generative Models](https://proceedings.mlr.press/v306/bai26c.html) | 视觉生成偏好对齐 | 用经验分数阈值把独立评分转成正负样本，并按离阈值的距离加权，使没有成对偏好的数据也能训练对齐。 |

<a id="by-reinforcement-learning"></a>

### 强化学习方法

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="ba26a-reinforcement-learning"></a>[Pareto-Guided Optimal Transport for Multi-Reward Alignment](https://proceedings.mlr.press/v306/ba26a.html) | 多奖励生成优化 | 对同一个提示构造样本的 Pareto 前沿，再用最优传输把被支配样本推向前沿，降低整个数据集共用一个加权奖励所带来的投机空间。 |

<a id="by-training-strategies"></a>

### 训练策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="bai26n-training-strategies"></a>[Optimizing Few-Step Generation with Adaptive Matching Distillation](https://proceedings.mlr.press/v306/bai26n.html) | 少步生成蒸馏 | 当真实教师的引导失真、生成教师的排斥又不足时，用奖励代理识别异常区域，重新分配纠偏梯度并加强对坍缩模式的排斥。 |

<a id="by-inference"></a>

### 推理策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="alesiani26a-inference"></a>[Logical Guidance for the Exact Composition of Diffusion Models](https://proceedings.mlr.press/v306/alesiani26a.html) | 扩散模型逻辑控制 | 将逻辑约束编译成电路，若合取子式条件独立、析取子式条件独立或互斥，即可从原子属性的后验和分数递推精确引导。 |
| <a id="bae26b-inference"></a>[Training-Free Coverless Multi-Image Steganography with Access Control](https://proceedings.mlr.press/v306/bae26b.html) | 图像隐写 | 用随机基压制潜变量中的结构残留，再融合多张图像的潜变量，使同一扩散载体可按授权分别恢复不同隐藏内容。 |
| <a id="bang26a-inference"></a>[Triadic Dynamics Aware Diffusion Posterior Sampling for Inverse Problems: Optimizing Guidance and Stochasticity Schedules](https://proceedings.mlr.press/v306/bang26a.html) | 扩散逆问题 | 早期大幅 CFG 可能与观测一致性更新冲突。采样中逐步降低数据一致性引导和随机性、提高 CFG，可以分别兼顾观测和生成质量。 |

<a id="by-representation-learning"></a>

### 表征学习

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="bian26d-representation-learning"></a>[CURE: Consistency-under-Unified Semantic Regularization for Generalized Category Discovery](https://proceedings.mlr.press/v306/bian26d.html) | 新类别发现 | 先用已知类原型训练语义结构，再用带语义正则的一致性学习扩展未知类，避免过早的全局均匀排布冲淡类别结构。 |

<a id="by-evaluation"></a>

### 评测与诊断

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="acuaviva26a-evaluation"></a>[Rethinking Visual Intelligence: Insights from Video Pretraining](https://proceedings.mlr.press/v306/acuaviva26a.html) | 视觉推理评测 | 比较视频扩散模型与 LLM 的适配能力时，让两类模型分别用自己的输入模态，并报告数据效率。 |
| <a id="ahmed26a-evaluation"></a>[Med-SegLens: Latent-Level Model Diffing for Interpretable Medical Image Segmentation](https://proceedings.mlr.press/v306/ahmed26a.html) | 分割模型诊断 | 用稀疏自编码器拆解并对齐不同架构及人群的分割激活，再干预与分布偏移相关的潜特征定位和修复错误。 |
| <a id="alexis26a-evaluation"></a>[GEPC: Group-Equivariant Posterior Consistency for Out-of-Distribution Detection in Diffusion Models](https://proceedings.mlr.press/v306/alexis26a.html) | 扩散模型域外检测 | 检查输入做旋转或翻转后，扩散分数场是否相应变换。即使分数幅值相近，等变性残差也能暴露域外样本。 |
| <a id="baek26e-evaluation"></a>[Proactive Defense Benchmark against Deepfake Generation](https://proceedings.mlr.press/v306/baek26e.html) | 深伪防御评测 | 把输出画质和身份保真度分开评估，并校准生成器固有的身份偏差。白盒防御表现特别强时也要检查是否损害跨生成器迁移。 |
<!-- classification:end -->
