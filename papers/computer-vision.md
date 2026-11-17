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
| <a id="chen26du-architecture"></a>[Autoregression with Self-Token Prediction](https://proceedings.mlr.press/v306/chen26du.html) | 按空间分组的同位词元预测 | 把图像词元按空间顺序分组，用已生成组构造与当前组位置对齐的输入。当前组输入内部可做全注意力，并行预测对应位置，组间掩码保证预测只依赖先前生成的真实词元。 |

<a id="by-modules"></a>

### 模块

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="blauch26a-modules"></a>[FOVI: A biologically-inspired foveated interface for deep vision models](https://proceedings.mlr.press/v306/blauch26a.html) | 主动视觉分辨率 | 在传感器坐标中保留中心高分辨率和周边低分辨率，再映射到均匀的处理流形做近邻卷积，减少全视野处理所需的像素与计算。 |
| <a id="candogan26a-modules"></a>[Spatial Priors via Space Filling Curves for Small and Limited Data Vision Transformers](https://proceedings.mlr.press/v306/candogan26a.html) | 小型视觉 Transformer | 沿多条空间填充曲线扫描图像，把路径距离转成衰减掩码乘到注意力上，用很少的新参数注入空间邻近先验。 |
| <a id="cao26j-modules"></a>[Multi-Label Learning with Contrastive Cluster Self-Supervision for 3D Hierarchical Semantic Segmentation](https://proceedings.mlr.press/v306/cao26j.html) | 分层三维语义分割 | 共享点云编码，临近输出再按层级拆分解码器，并引入粗到细一致性。基于点簇的对比自监督补充不平衡类别的特征。 |
| <a id="cao26n-modules"></a>[LiteVSR: Lightweight Adaptation of Frozen Diffusion Transformers for Video Super-Resolution](https://proceedings.mlr.press/v306/cao26n.html) | 轻量视频超分 | 冻结整个扩散 Transformer，用双流适配器分别读低清视频的静态结构和当前去噪状态，再按时间步调节结构对齐与纹理细化。 |
| <a id="cao26ab-modules"></a>[StructMAR: Structure-Aware Masked Autoregression for Explicit Layout Alignment in Text-to-Image Generation](https://proceedings.mlr.press/v306/cao26ab.html) | 结构化图像生成 | 用二维旋转位置编码保持潜变量拓扑，通过布局引导的注意力偏置把各位置分配到相应实例，再用检测指标微调布局对齐。 |
| <a id="chen26ce-modules"></a>[WEVSR: Video Diffusion Generators for Real-World Video Super-Resolution with Wavelet-Enhanced VAE Encoder](https://proceedings.mlr.press/v306/chen26ce.html) | 视频超分的小波编码前端 | 逐帧做多级离散小波变换，递归分解低频子带，并把各级高频子带与同尺度的 VAE 编码器特征拼接，用 1×1 卷积投影回原通道数。这样可把细节线索送入潜空间，并沿用冻结的预训练解码器。 |
| <a id="tian26k-modules"></a>[From Per-Image Low-Rank to Encoding Mismatch: Rethinking Feature Distillation in Vision Transformers](https://proceedings.mlr.press/v306/tian26k.html) | 视觉特征蒸馏 | 给小型 ViT 的特征输出接口或最后一个 Transformer 块加宽，以匹配教师模型的编码空间。 [详细解读](../insights/modules.md#widen-the-student-distillation-interface) |

<a id="by-loss-functions"></a>

### 损失函数

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="bai26c-loss-functions"></a>[Threshold-Guided Optimization for Visual Generative Models](https://proceedings.mlr.press/v306/bai26c.html) | 视觉生成偏好对齐 | 用经验分数阈值把独立评分转成正负样本，并按离阈值的距离加权，使没有成对偏好的数据也能训练对齐。 |
| <a id="bo26a-loss-functions"></a>[Benchmarking Dense and Indiscernible Object Counting with Blueberries](https://proceedings.mlr.press/v306/bo26a.html) | 密集小目标计数 | 用视觉语言模型生成伪分割掩码压制背景，再用对比损失分离果实与叶片表征。按边缘调整裁剪也可减少密集簇中的目标截断。 |

<a id="by-reinforcement-learning"></a>

### 强化学习方法

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="ba26a-reinforcement-learning"></a>[Pareto-Guided Optimal Transport for Multi-Reward Alignment](https://proceedings.mlr.press/v306/ba26a.html) | 多奖励生成优化 | 对同一个提示构造样本的 Pareto 前沿，再用最优传输把被支配样本推向前沿，降低整个数据集共用一个加权奖励所带来的投机空间。 |
| <a id="chen26as-reinforcement-learning"></a>[Test-Time Reinforcement Learning for Flow Matching](https://proceedings.mlr.press/v306/chen26as.html) | 流匹配测试时优化 | 把中间潜变量看作待选择状态，在同一速度场中用随机 rollout 探索。先按高噪声阶段的奖励差稳定结构，再用组相对优势调整低噪声细节。 |
| <a id="chen26ea-reinforcement-learning"></a>[RELO: Reinforcement Learning to Localize for Visual Object Tracking](https://proceedings.mlr.press/v306/chen26ea.html) | 目标跟踪定位策略 | 先预热边界框回归头，再把特征图上的位置作为动作，用采样位置对应的预测框计算逐帧 IoU 和序列 AUC 奖励，以 actor-critic 更新定位策略，使训练能直接利用跟踪评测指标。 |

<a id="by-training-strategies"></a>

### 训练策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="bai26n-training-strategies"></a>[Optimizing Few-Step Generation with Adaptive Matching Distillation](https://proceedings.mlr.press/v306/bai26n.html) | 少步生成蒸馏 | 当真实教师的引导失真、生成教师的排斥又不足时，用奖励代理识别异常区域，重新分配纠偏梯度并加强对坍缩模式的排斥。 |
| <a id="cai26h-training-strategies"></a>[Mode Seeking meets Mean Seeking for Fast Long Video Generation](https://proceedings.mlr.press/v306/cai26h.html) | 长视频生成 | 用有限长视频监督全局流匹配头学习叙事与运动，再用冻结的短视频教师对滑窗局部做反向 KL 匹配，让长程一致性与局部质感各有监督。 |
| <a id="cao26o-training-strategies"></a>[Beyond Static Allocation: Dynamic Sensitivity-Aware Fine-Tuning for Vision Transformers](https://proceedings.mlr.press/v306/cao26o.html) | 动态参数高效微调 | 定期重测视觉 Transformer 各处的敏感性，把学过的适配模块冻结，再将可训练参数额度分给新出现的敏感位置。 |
| <a id="chavhan26a-training-strategies"></a>[NanoFLUX: Distillation-Driven Compression of Large Text-to-Image Generation Models for Mobile Devices](https://proceedings.mlr.press/v306/chavhan26a.html) | 端侧文生图蒸馏 | 分阶段裁剪扩散 Transformer，并只让中间块用降采样 token；再用去噪器早期层的视觉信号蒸馏文本编码器，把压缩分摊到多个环节。 |
| <a id="chen26cn-training-strategies"></a>[Focusing: View-Consistent Sparse Voxels for Efficient 3D VAE Training](https://proceedings.mlr.press/v306/chen26cn.html) | 视图一致的三维 VAE 稀疏训练 | 训练时将潜体素投影到当前视角，用真值网格的渲染深度筛除远离可见表面的体素，并保留命中体素的邻域，使解码和注意力的开销集中在当前渲染损失可监督的区域。 |
| <a id="chen26dm-training-strategies"></a>[3DGS-HPC: Distractor-free 3D Gaussian Splatting with Hybrid Patch-wise Classification](https://proceedings.mlr.press/v306/chen26dm.html) | 高斯泼溅的瞬态区域筛除 | 以规则图像块为单位汇总训练图与渲染图之间的误差。用 RGB 差异估计静态区域比例，再据此约束感知误差的筛除阈值，减少把纹理弱的静态区域误判成瞬态干扰。 |
| <a id="chen26eu-training-strategies"></a>[Context Forcing: Consistent Autoregressive Video Generation with Long Context](https://proceedings.mlr.press/v306/chen26eu.html) | 长上下文视频蒸馏 | 让教师和学生都读取长视频历史，避免短窗口教师给出的监督只覆盖局部时序。缓存用滚动队列保留近期帧，并按相邻键向量的差异挑选有新信息的词元长期保留。 |

<a id="by-data-strategies"></a>

### 数据策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="cai26m-data-strategies"></a>[FUSE: Full-spectrum Unlearnable Examples via Spectral Equalization](https://proceedings.mlr.press/v306/cai26m.html) | 图像训练数据保护 | 训练扰动生成器时随机遮掉连续频带，再约束高低频一致，降低保护信号被低通滤波一次清除的风险。 |
| <a id="cao26s-data-strategies"></a>[Where Detectors Fail: Probing Generative Space for Generalizable AI-Generated Image Detection](https://proceedings.mlr.press/v306/cao26s.html) | 合成图检测 | 用当前检测器给生成样本打分，再沿生成模型的内部表征寻找难识别的真实感图像。把这些漏检候选回灌训练，可补足标准采样探索不到的区域。 |
| <a id="chen26s-data-strategies"></a>[When Preference Labels Fall Short: Aligning Diffusion Models from Real Data](https://proceedings.mlr.press/v306/chen26s.html) | 生成偏好数据 | 以真实图像作偏好基准，将模型生成结果或扰动样本作为对照，可以在缺少人工偏好对时构造图像对齐监督。 |
| <a id="chen26bj-data-strategies"></a>[Amodal Instance Segmentation with IRAIS Dataset for Sim-to-Real Transfer](https://proceedings.mlr.press/v306/chen26bj.html) | 跨域遮挡分割数据 | 对物理仿真中摆放的三维商品场景做多视角渲染，自动生成可见与完整实例掩码。让合成集和人工标注的真实集共享标签定义与评测协议，可直接测量遮挡分割的跨域表现。 |

<a id="by-inference"></a>

### 推理策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="alesiani26a-inference"></a>[Logical Guidance for the Exact Composition of Diffusion Models](https://proceedings.mlr.press/v306/alesiani26a.html) | 扩散模型逻辑控制 | 将逻辑约束编译成电路，若合取子式条件独立、析取子式条件独立或互斥，即可从原子属性的后验和分数递推精确引导。 |
| <a id="bae26b-inference"></a>[Training-Free Coverless Multi-Image Steganography with Access Control](https://proceedings.mlr.press/v306/bae26b.html) | 图像隐写 | 用随机基压制潜变量中的结构残留，再融合多张图像的潜变量，使同一扩散载体可按授权分别恢复不同隐藏内容。 |
| <a id="bang26a-inference"></a>[Triadic Dynamics Aware Diffusion Posterior Sampling for Inverse Problems: Optimizing Guidance and Stochasticity Schedules](https://proceedings.mlr.press/v306/bang26a.html) | 扩散逆问题 | 早期大幅 CFG 可能与观测一致性更新冲突。采样中逐步降低数据一致性引导和随机性、提高 CFG，可以分别兼顾观测和生成质量。 |
| <a id="briq26a-inference"></a>[Exploring and Exploiting Stability in Latent Flow Matching](https://proceedings.mlr.press/v306/briq26a.html) | 潜空间流匹配 | 不同容量的模型对同一噪声种子会生成相近内容，因此可用小模型完成前段流轨迹，再交给大模型补后段细节。 |
| <a id="cai26g-inference"></a>[Improving Classifier-Free Guidance of Flow Matching via Manifold Projection](https://proceedings.mlr.press/v306/cai26g.html) | 无分类器引导 | 把 CFG 视为带流形约束的连续优化，在每个采样阶段加入投影式修正，并利用 Anderson 加速抑制引导强度敏感性。 |
| <a id="cai26n-inference"></a>[TIMI: Training-Free Image-to-3D Multi-Instance Generation with Spatial Fidelity](https://proceedings.mlr.press/v306/cai26n.html) | 多实例图像到三维 | 去噪早期用实例级分离引导避免对象粘连，再用几何适应更新稳住形状及相对布局，无需训练多实例模型。 |
| <a id="cao26e-inference"></a>[Efficient Learned Image Compression without Entropy Coding](https://proceedings.mlr.press/v306/cao26e.html) | 低延迟图像压缩 | 用向量量化减小索引频率不均，再用条件自回归变换减少潜变量间依赖，使紧凑码流可以省掉串行熵编码。 |
| <a id="chang26c-inference"></a>[ContrastiveCFG: Guiding Diffusion Sampling by Contrasting Positive and Negative Concepts](https://proceedings.mlr.press/v306/chang26c.html) | 扩散正负概念引导 | 用对比损失分别吸引所需概念和排斥不需要的概念，避免简单取反无分类器引导时把样本推离可生成的分布。 |
| <a id="chen26v-inference"></a>[PRISM: Training-Free Video Anomaly Detection via Intrinsic Statistical Modeling](https://proceedings.mlr.press/v306/chen26v.html) | 免训练视频异常检测 | 利用冻结多模态嵌入，在特征空间做差分放大和白化，抑制正常背景共有成分，从而用低开销提高异常信号的可辨识度。 |
| <a id="chen26aj-inference"></a>[Normalizing Flows with Iterative Denoising](https://proceedings.mlr.press/v306/chen26aj.html) | 归一化流采样 | 保持训练端到端最大似然，采样时在自回归输出后追加迭代去噪，从而把精确似然训练与多步图像细化结合。 |
| <a id="chen26bp-inference"></a>[Bi-Anchor Interpolation Solver for Accelerating Generative Modeling](https://proceedings.mlr.press/v306/chen26bp.html) | 流匹配的双锚点积分 | 用冻结主干确定积分区间两端的速度，再由轻量旁路网络从两个方向批量估计区间内速度并做高阶数值积分。在 ImageNet-256 实验中，用 10 次主干评估达到与百步欧拉法相近的生成质量。 |
| <a id="chen26dn-inference"></a>[XSpecMesh: Quality-Preserving Auto-Regressive Mesh Generation Acceleration via Multi-Head Speculative Decoding](https://proceedings.mlr.press/v306/chen26dn.html) | 网格词元的投机解码 | 让轻量多头并行预测后续网格词元，主干用一次带因果掩码的前向计算核验。保留主干赋予概率达到阈值的连续前缀，从第一个未通过的位置重新采样。 |
| <a id="chen26ey-inference"></a>[SemanticNVS: Improving Semantic Scene Understanding in Generative Novel View Synthesis](https://proceedings.mlr.press/v306/chen26ey.html) | 新视角扩散的语义条件 | 逐步去噪时，在有观测覆盖的像素用从输入视图变换过来的语义特征，在其余像素从当前预测的干净图中提取 DINO 特征，让相机位移较大时仍有语义条件可用。 |
| <a id="chen26fc-inference"></a>[ScalingAR: Scaling Confidence for Autoregressive Image Generation](https://proceedings.mlr.press/v306/chen26fc.html) | 自回归图像采样的轨迹剪枝 | 用视觉 token 的预测熵与条件信号评估正在生成的轨迹，并随置信度调整条件引导强度、提前停止低分轨迹。这样可在潜 token 空间分配采样预算，省去中途解码图像和调用外部评分器。 |
| <a id="chen26fq-inference"></a>[GuidedBridge: Training-freely Improving Bridge Models with Prior Guidance](https://proceedings.mlr.press/v306/chen26fq.html) | 桥式生成模型的分频先验引导 | 对输入先验做模糊等退化构造弱版本，每步外推强弱先验下的去噪结果。按桥采样两端信噪比较高的特点，在早段和末段加强高频引导，低频引导则贯穿整个轨迹。 |

<a id="by-representation-learning"></a>

### 表征学习

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="bian26d-representation-learning"></a>[CURE: Consistency-under-Unified Semantic Regularization for Generalized Category Discovery](https://proceedings.mlr.press/v306/bian26d.html) | 新类别发现 | 先用已知类原型训练语义结构，再用带语义正则的一致性学习扩展未知类，避免过早的全局均匀排布冲淡类别结构。 |
| <a id="boduljak26a-representation-learning"></a>[VFMF: Dense Forecasting by Generating Vision Foundation Model Features](https://proceedings.mlr.press/v306/boduljak26a.html) | 视频特征预测 | 先把视觉基础模型特征压到适合生成的紧凑潜空间，再用条件流匹配采样未来。在部分可见时可表达多个可能未来，且比直接扩散原特征或 PCA 压缩保留更多信息。 |
| <a id="cao26h-representation-learning"></a>[On the Power of Statistics in Class-Incremental Learning with Pretrained Models](https://proceedings.mlr.press/v306/cao26h.html) | 类别增量学习 | 冻结视觉骨干，只维护逐类的特征统计量并用它们推断，可以作为检验复杂持续训练方法是否带来收益的强基线。 |
| <a id="cassano26a-representation-learning"></a>[SAEmnesia: Erasing Concepts in Diffusion Models with Supervised Sparse Autoencoders](https://proceedings.mlr.press/v306/cassano26a.html) | 扩散概念遗忘 | 用标签训练稀疏自编码器，将每个概念的激活集中在单个可解释神经元，便于有针对性地擦除并依次处理多个概念。 |
| <a id="cendra26a-representation-learning"></a>[PartCo: Part-Level Correspondence Priors Enhance Category Discovery](https://proceedings.mlr.press/v306/cendra26a.html) | 细粒度类别发现 | 用图像局部部件之间的特征对应为类别聚类补充先验，可以区分全局语义相近、只在局部有差异的类别。 |
| <a id="chen26ca-representation-learning"></a>[Rotation-Invariant Spherical Watermarking via Third-Order SO(3) Representation Coupling](https://proceedings.mlr.press/v306/chen26ca.html) | 球面旋转不变水印 | 对球谐系数做三阶张量耦合并投影到 SO(3) 的平凡表示，构造保留相对相位信息的旋转不变双谱。可在高阶球谐系数中嵌入水印，再从双谱标量中解码全景图的水印。 |
| <a id="chen26ee-representation-learning"></a>[DynaTok: Token-Based 4D Reconstruction from Partial Point Clouds](https://proceedings.mlr.press/v306/chen26ee.html) | 动态点云的参考与残差表征 | 把逐帧不完整点云编码成固定数量的 token 并跨帧聚合，以首帧为共享参考，用潜空间残差表示各帧变化。条件流匹配解码器利用两者重建完整点云，训练只需要各帧完整点云监督，无需点对应或运动标签。 |
| <a id="chen26ek-representation-learning"></a>[Multiview Self-Representation Learning across Heterogeneous Views](https://proceedings.mlr.press/v306/chen26ek.html) | 异构视觉表征的聚类共识 | 对同一张无标签图像，各预训练模型的特征分别经对应视图模型预测簇分配概率。对这些概率取平均并选概率最高的簇作伪标签，再用它监督所有视图，使一致性约束建立在共同的簇空间上。 |
| <a id="chen26fh-representation-learning"></a>[TrustworthyQENN: A Quantum Evidential Neural Network Based on Complex-Valued Contrastive Learning for Uncertainty Pattern Classification](https://proceedings.mlr.press/v306/chen26fh.html) | 复数表征的分布外识别 | 用监督对比损失同时约束复数特征的幅值和相位，使同类样本靠近，再将特征转换为含未知类状态的证据幅，并融合多个视图的证据。在所测遥感数据上，联合使用幅相信息可改善分布外识别。 |

<a id="by-evaluation"></a>

### 评测与诊断

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="acuaviva26a-evaluation"></a>[Rethinking Visual Intelligence: Insights from Video Pretraining](https://proceedings.mlr.press/v306/acuaviva26a.html) | 视觉推理评测 | 比较视频扩散模型与 LLM 的适配能力时，让两类模型分别用自己的输入模态，并报告数据效率。 |
| <a id="ahmed26a-evaluation"></a>[Med-SegLens: Latent-Level Model Diffing for Interpretable Medical Image Segmentation](https://proceedings.mlr.press/v306/ahmed26a.html) | 分割模型诊断 | 用稀疏自编码器拆解并对齐不同架构及人群的分割激活，再干预与分布偏移相关的潜特征定位和修复错误。 |
| <a id="alexis26a-evaluation"></a>[GEPC: Group-Equivariant Posterior Consistency for Out-of-Distribution Detection in Diffusion Models](https://proceedings.mlr.press/v306/alexis26a.html) | 扩散模型域外检测 | 检查输入做旋转或翻转后，扩散分数场是否相应变换。即使分数幅值相近，等变性残差也能暴露域外样本。 |
| <a id="baek26e-evaluation"></a>[Proactive Defense Benchmark against Deepfake Generation](https://proceedings.mlr.press/v306/baek26e.html) | 深伪防御评测 | 把输出画质和身份保真度分开评估，并校准生成器固有的身份偏差。白盒防御表现特别强时也要检查是否损害跨生成器迁移。 |
| <a id="braun26b-evaluation"></a>[Erased but Not Forgotten: How Backdoors Compromise Concept Erasure](https://proceedings.mlr.press/v306/braun26b.html) | 扩散模型概念遗忘 | 通过测试擦除前写入的触发关联能否在遗忘后复现概念，可以检查现有擦除方法是否还保留潜在生成路径。 |
| <a id="chen26az-evaluation"></a>[Semantic-level Backdoor Attack against Text-to-Image Diffusion Models](https://proceedings.mlr.press/v306/chen26az.html) | 生成模型后门评测 | 后门可能对语义相同的改写提示共同触发，枚举固定字符串容易漏检。可用语义等价改写、部分语义和正常输入分别测触发、误触发和正常质量。 |

<a id="by-theory-statistics"></a>

### 理论与统计

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="bradley26a-theory-statistics"></a>[Local Mechanisms of Compositional Generalization in Conditional Diffusion](https://proceedings.mlr.press/v306/bradley26a.html) | 扩散组合泛化 | 当条件分数只依赖局部像素及局部条件时，生成可以处理超出训练对象数的场景。显式施加这种局部性，使原先未泛化的 CLEVR 模型也能泛化。 |
| <a id="brady26b-theory-statistics"></a>[Is Generation Required for Data-Efficient Perception?](https://proceedings.mlr.press/v306/brady26b.html) | 低数据视觉泛化 | 在论文设定的组合生成过程中，解码器只需较简单的组合归纳偏置。训练解码器再做反演，在受控视觉数据中能用更少数据外推新组合。 |
<!-- classification:end -->
