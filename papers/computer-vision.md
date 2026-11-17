# 计算机视觉

[首页](../README.md) · [参与贡献](../CONTRIBUTING.md) · [English](../en/papers/computer-vision.md)

视觉识别、表征学习与生成。

<a id="vision-model-distillation"></a>

## 视觉模型蒸馏

| 论文 | 首次公开 / 发表 | 可借鉴的技术 | 资源 |
| :--- | :--- | :--- | :--- |
| [**Lift / WideLast**](https://proceedings.mlr.press/v306/tian26k.html) · [论文卡](../conferences/icml-2026/cards/4401-4500.md#paper-tian26k)<br><sub>Huiyuan Tian 等, From Per-Image Low-Rank to Encoding Mismatch: Rethinking Feature Distillation in Vision Transformers</sub> | 首次公开日期待核实<br><sub>[ICML 2026](https://proceedings.mlr.press/v306/tian26k.html)</sub> | [只加宽学生模型的蒸馏接口](../insights/modules.md#widen-the-student-distillation-interface) | [PMLR](https://proceedings.mlr.press/v306/tian26k.html) · [OpenReview](https://openreview.net/forum?id=2Ud1nkQrVZ) · [代码](https://github.com/thy960112/From-Per-Image-Low-Rank-to-Encoding-Mismatch) |

<!-- classification:start -->
## 按技术类型浏览

<a id="by-architecture"></a>

### 模型架构

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="atanov26a-architecture"></a>[VideoFlexTok: Flexible-Length Coarse-to-Fine Video Tokenization](https://proceedings.mlr.press/v306/atanov26a.html) · [论文卡](../conferences/icml-2026/cards/0101-0200.md#paper-atanov26a) | 视频分词 | 让视频 token 按粗到细排列，前面少量 token 保留语义与运动，尾部补充细节。生成式解码器可以在不同截断长度重建视频。 |
| <a id="baade26a-architecture"></a>[Latent Forcing: Reordering the Diffusion Trajectory for Pixel-Space Image Generation](https://proceedings.mlr.press/v306/baade26a.html) · [论文卡](../conferences/icml-2026/cards/0101-0200.md#paper-baade26a) | 像素空间扩散 | 给潜变量和像素安排不同噪声日程，使模型先形成可作中间计算的潜表示，再补出高频像素细节。 |
| <a id="bao26f-architecture"></a>[Envisioning Beyond the Few: Disentangled Semantics and Primitives for Few-Shot Atypical Layout-to-Image Generation](https://proceedings.mlr.press/v306/bao26f.html) · [论文卡](../conferences/icml-2026/cards/0201-0300.md#paper-bao26f) | 少样本布局生成 | 用类别锚点保留对象身份，将局部视觉细节编码成可重组原语，缓解小样本非典型布局生成中的语义碎裂。 |
| <a id="chen26du-architecture"></a>[Autoregression with Self-Token Prediction](https://proceedings.mlr.press/v306/chen26du.html) | 按空间分组的同位词元预测 | 把图像词元按空间顺序分组，用已生成组构造与当前组位置对齐的输入。当前组输入内部可做全注意力，并行预测对应位置，组间掩码保证预测只依赖先前生成的真实词元。 |
| <a id="chen26ga-architecture"></a>[Phy-CoSF: Physics-Guided Continuous Spectral Fields Reconstruction and Spectral Super-Resolution for Snapshot Compressive Imaging](https://proceedings.mlr.press/v306/chen26ga.html) | 压缩成像的连续光谱先验 | 在每一步展开重建中用物理编码掩码约束数据一致性，再以可查询波长的连续光谱场作先验。训练时只对有真值的离散波长切片计算误差，推理时可查询未参与训练的波长。 |
| <a id="choy26a-architecture"></a>[SpaCeFormer: Fast Proposal-Free Open-Vocabulary 3D Instance Segmentation](https://proceedings.mlr.press/v306/choy26a.html) | 开放词汇三维实例分割 | 将固定空间范围的窗口注意力和固定词元数的 Morton 序分段交替使用，以兼顾局部几何与分块计算。解码器直接用可学习查询从体素特征预测实例掩码。 |
| <a id="ding26u-architecture"></a>[Native Spatio-Temporal 4D Variational Autoencoder](https://proceedings.mlr.press/v306/ding26u.html) | 原生四维体素自编码 | 让动态彩色体素始终携带三维位置与时间坐标，用稀疏卷积压缩空间，再用局部四维窗口注意力汇聚时空信息，使时间压缩率可调且保持显式坐标对应。 |
| <a id="du26c-architecture"></a>[AesFormer: Transform Everyday Photos into Beautiful Memories](https://proceedings.mlr.press/v306/du26c.html) | 照片结构重构的动作条件编辑 | 先让规划模型把照片的构图、视角等问题转成结构化编辑动作，再用编辑动作和原图作为流匹配模型的条件。通过已对齐的欠佳与优质照片对监督编辑器，使摄影术语对应具体的像素变化。 |
| <a id="duan26e-architecture"></a>[Discontinuous Galerkin Neural Operator for Pathology Defocus Deblurring](https://proceedings.mlr.press/v306/duan26e.html) | 病理去焦模糊的局部积分算子 | 把全图核积分拆为互不重叠的空间单元，各单元用局部算子拟合不同模糊模式，再用数值通量在单元边界交换特征。这样允许局部核不连续，同时在预测清晰图像时保留跨块联系。 |
| <a id="fu26l-architecture"></a>[CODiff: One-Step Diffusion Model for Camouflaged Object Detection](https://proceedings.mlr.press/v306/fu26l.html) | 单步伪装物体掩码预测 | 从 DINOv2 的全局特征和去噪时刻生成调制参数，注入自注意力和条件融合层，并分层融合局部结构特征。用于单步预测时，模型可同时利用场景语义和伪装物体的细粒度边界。 |
| <a id="gao26aq-architecture"></a>[DecomPose: Disentangling Cross-Category Optimization Contention for Category-Level 6D Object Pose Estimation](https://proceedings.mlr.press/v306/gao26aq.html) | 按类别难度隔离位姿学习梯度 | 用数据估计几何难度，再把类别划到不同的对应点分支，使共享模块少承受方向冲突的梯度。给结构简单的组较高容量作为稳定训练支点，并限制复杂组的分支容量以减少噪声更新。 |
| <a id="garcin26a-architecture"></a>[Beyond Pixel Histories: World Models with Persistent 3D State](https://proceedings.mlr.press/v306/garcin26a.html) | 持久三维状态的交互视频世界模型 | 独立维护随动作演化的潜三维场景和相机状态，每步由相机查询并投影相关场景特征再渲染画面。重访离开视野的区域时可读回场景状态，降低长视频只用近帧记忆造成的空间不一致。 |
| <a id="gong26f-architecture"></a>[Direct 3D-Aware Object Insertion via Decomposed Visual Proxies](https://proceedings.mlr.press/v306/gong26f.html) | 姿态可控插入的三路视觉条件 | 用调整后的三维代理 RGB 渲染引导姿态，原参考图补充代理缺失的外观细节，局部合成图与全图背景特征共同提供场景上下文。通过独立通路注入，可同时处理姿态、身份及背景光照匹配。 |
| <a id="guo26ag-architecture"></a>[OmniAID: Decoupling Semantics and Artifacts for Universal AI-Generated Image Detection in the Wild](https://proceedings.mlr.press/v306/guo26ag.html) | 内容伪迹分离的生成图像鉴别 | 冻结 CLIP 注意力权重的主奇异分量，在残差子空间训练内容专家和通用伪迹专家。通用专家用语义配对的真实图与重建图训练并始终开启，路由器只选择内容专家，以分辨跨领域伪迹与特定内容缺陷。 |
| <a id="han26c-architecture"></a>[Bridging Local–Global Dissonance: Learning from Compressive Measurements for Hyperspectral Reconstruction](https://proceedings.mlr.press/v306/han26c.html) | 压缩高光谱重建的局部与全局协调 | 先用多尺度卷积核混合词元并交换窗口潜特征，保留局部测量线索，再用分层移位注意力恢复跨尺度光谱空间一致性。将该网络作为深度展开的正则器，可和 CASSI 前向物理模型共同约束重建。 |

<a id="by-modules"></a>

### 模块

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="blauch26a-modules"></a>[FOVI: A biologically-inspired foveated interface for deep vision models](https://proceedings.mlr.press/v306/blauch26a.html) · [论文卡](../conferences/icml-2026/cards/0201-0300.md#paper-blauch26a) | 主动视觉分辨率 | 在传感器坐标中保留中心高分辨率和周边低分辨率，再映射到均匀的处理流形做近邻卷积，减少全视野处理所需的像素与计算。 |
| <a id="candogan26a-modules"></a>[Spatial Priors via Space Filling Curves for Small and Limited Data Vision Transformers](https://proceedings.mlr.press/v306/candogan26a.html) · [论文卡](../conferences/icml-2026/cards/0301-0400.md#paper-candogan26a) | 小型视觉 Transformer | 沿多条空间填充曲线扫描图像，把路径距离转成衰减掩码乘到注意力上，用很少的新参数注入空间邻近先验。 |
| <a id="cao26j-modules"></a>[Multi-Label Learning with Contrastive Cluster Self-Supervision for 3D Hierarchical Semantic Segmentation](https://proceedings.mlr.press/v306/cao26j.html) · [论文卡](../conferences/icml-2026/cards/0301-0400.md#paper-cao26j) | 分层三维语义分割 | 共享点云编码，临近输出再按层级拆分解码器，并引入粗到细一致性。基于点簇的对比自监督补充不平衡类别的特征。 |
| <a id="cao26n-modules"></a>[LiteVSR: Lightweight Adaptation of Frozen Diffusion Transformers for Video Super-Resolution](https://proceedings.mlr.press/v306/cao26n.html) · [论文卡](../conferences/icml-2026/cards/0301-0400.md#paper-cao26n) | 轻量视频超分 | 冻结整个扩散 Transformer，用双流适配器分别读低清视频的静态结构和当前去噪状态，再按时间步调节结构对齐与纹理细化。 |
| <a id="cao26ab-modules"></a>[StructMAR: Structure-Aware Masked Autoregression for Explicit Layout Alignment in Text-to-Image Generation](https://proceedings.mlr.press/v306/cao26ab.html) | 结构化图像生成 | 用二维旋转位置编码保持潜变量拓扑，通过布局引导的注意力偏置把各位置分配到相应实例，再用检测指标微调布局对齐。 |
| <a id="chen26ce-modules"></a>[WEVSR: Video Diffusion Generators for Real-World Video Super-Resolution with Wavelet-Enhanced VAE Encoder](https://proceedings.mlr.press/v306/chen26ce.html) | 视频超分的小波编码前端 | 逐帧做多级离散小波变换，递归分解低频子带，并把各级高频子带与同尺度的 VAE 编码器特征拼接，用 1×1 卷积投影回原通道数。这样可把细节线索送入潜空间，并沿用冻结的预训练解码器。 |
| <a id="ciernik26a-modules"></a>[Attentive Multi-Layer Fusion for Vision Transformers](https://proceedings.mlr.press/v306/ciernik26a.html) | ViT 多层注意力探针 | 冻结视觉主干，取各层的分类词元和平均池化表征作为键和值，再由任务训练得到的查询做跨层注意力，使轻量探针能按任务选取不同深度的信息。 |
| <a id="colamonaco26a-modules"></a>[Prototype-Grounded Concept Models for Verifiable Concept Alignment](https://proceedings.mlr.press/v306/colamonaco26a.html) | 视觉概念瓶颈的原型证据 | 把每个概念的得分回溯到匹配的局部图像原型，让读者能检查模型实际使用的概念证据。发现伪相关时可删除对应原型或重标其概念，也可以加入人工选择的图像块。 |
| <a id="dhar26a-modules"></a>[Does a Hybrid Space-Aware Randomized Defense Improve Empirical and Certified Adversarial Robustness?](https://proceedings.mlr.press/v306/dhar26a.html) | 卷积权重与特征的双空间扰动 | 由随机注意力支路输出噪声响应，一方面门控卷积核的随机扰动，另一方面在块末向特征显式注入噪声。递归与非递归支路共同调节逐步平滑和通道特异扰动，训练与推理均保留随机性。 |
| <a id="dong26i-modules"></a>[PolarDepth: Monocular Transparent Object Depth from Polar-Physics Priors](https://proceedings.mlr.press/v306/dong26i.html) | 偏振物理先验的透明物体深度 | 用线偏振度和偏振角推断折射率与表面法向的天顶角、方位角，把这些物理量编码为几何特征，与 RGB 一起估计深度。在透明表面缺少可靠纹理时，偏振仍能提供方向线索。 |
| <a id="duan26a-modules"></a>[MobileFusion: Mobile-Friendly Infrared and Visible Image Fusion via Structural Re-parameterization](https://proceedings.mlr.press/v306/duan26a.html) | 红外可见光融合的卷积分支折叠 | 训练时用多卷积分支促进红外与可见光特征交互。部署时先将批归一化折入各分支卷积，再对齐核的空间尺寸并合并参数，用单个标准卷积执行等价变换。 |
| <a id="guo26ad-modules"></a>[WildActor: Unconstrained Identity-Preserving Video Generation](https://proceedings.mlr.press/v306/guo26ad.html) | 人体视频的非对称身份注意力 | 让脸部与全身参考 token 先独立聚合多视角身份，再由视频 token 单向读取参考表示。LoRA 只作用于参考 token，可向去噪视频传递身份线索，同时减少噪声视频对参考表示的干扰。 |
| <a id="hadji26a-modules"></a>[Hierarchical Image Tokenization for Multi-Scale Image Super Resolution](https://proceedings.mlr.press/v306/hadji26a.html) | 超分辨率的跨尺度词元前缀 | 分辨率逐级提高时，保留较低分辨率已得到的残差词元前缀，只在当前尺度追加新的量化词元，使中间前缀也可解码为相应倍率的超分辨率图像。 |
| <a id="tian26k-modules"></a>[From Per-Image Low-Rank to Encoding Mismatch: Rethinking Feature Distillation in Vision Transformers](https://proceedings.mlr.press/v306/tian26k.html) · [论文卡](../conferences/icml-2026/cards/4401-4500.md#paper-tian26k) | 视觉特征蒸馏 | 给小型 ViT 的特征输出接口或最后一个 Transformer 块加宽，以匹配教师模型的编码空间。 [详细解读](../insights/modules.md#widen-the-student-distillation-interface) |

<a id="by-loss-functions"></a>

### 损失函数

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="bai26c-loss-functions"></a>[Threshold-Guided Optimization for Visual Generative Models](https://proceedings.mlr.press/v306/bai26c.html) · [论文卡](../conferences/icml-2026/cards/0101-0200.md#paper-bai26c) | 视觉生成偏好对齐 | 用经验分数阈值把独立评分转成正负样本，并按离阈值的距离加权，使没有成对偏好的数据也能训练对齐。 |
| <a id="bo26a-loss-functions"></a>[Benchmarking Dense and Indiscernible Object Counting with Blueberries](https://proceedings.mlr.press/v306/bo26a.html) · [论文卡](../conferences/icml-2026/cards/0301-0400.md#paper-bo26a) | 密集小目标计数 | 用视觉语言模型生成伪分割掩码压制背景，再用对比损失分离果实与叶片表征。按边缘调整裁剪也可减少密集簇中的目标截断。 |
| <a id="deng26e-loss-functions"></a>[Joint Geometric and Trajectory Consistency Learning for One-Step Real-World Super-Resolution](https://proceedings.mlr.press/v306/deng26e.html) | 单步超分辨率的全路径对齐 | 把预测的高分辨率图像沿前向加噪过程投影回多个离散时刻，并与真值图像在相同噪声下的状态逐一比较。高噪声时主要约束整体结构，低噪声时可进一步校准细节，以减轻一致性训练中的轨迹漂移。 |
| <a id="gushchin26a-loss-functions"></a>[BiRQA: Bidirectional Robust Quality Assessment for Images](https://proceedings.mlr.press/v306/gushchin26a.html) | 全参考画质的锚定对抗训练 | 给受扰图像匹配质量略高、略低的可靠干净锚点，并约束其预测排序。在双侧锚点覆盖与排序损失受控时，可由相对次序推得单样本评分的误差上界。 |
| <a id="ha26b-loss-functions"></a>[Unlearning’s Blind Spots: Over-Unlearning and Prototypical Relearning Attack](https://proceedings.mlr.press/v306/ha26b.html) | 类别遗忘的邻域保护与表征分散 | 在待遗忘类附近对保留类分布做掩码蒸馏，以保护邻域决策边界，同时用类内分散损失打散待遗忘类嵌入，使少量样本更难重新估稳该类原型。 |

<a id="by-optimization"></a>

### 优化

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="crane26a-optimization"></a>[Scalable and Differentiable Point-Cloud Registration Using Maximum Mean Discrepancy](https://proceedings.mlr.press/v306/crane26a.html) | 可微的随机特征点云配准 | 用随机傅里叶特征的均值差近似两组点云的最大均值差异，把刚体配准写成非线性最小二乘。以隐式微分传递求解结果的梯度，可把无需点对应关系的配准接入端到端训练。 |
| <a id="dai26h-optimization"></a>[TextMesh4D: Zero-shot Text-to-4D Mesh Generation](https://proceedings.mlr.press/v306/dai26h.html) | 动态网格的逐面雅可比形变 | 把每帧形变表示为静态网格的逐三角面雅可比加上该帧偏移，再用可微泊松求解器最小二乘积分得到顶点位移。扩散引导更新局部面形变，积分则让相邻面共享一致的顶点位置。 |
| <a id="denker26a-optimization"></a>[Trajectory Stitching for Solving Inverse Problems with Flow-Based Models](https://proceedings.mlr.press/v306/denker26a.html) | 流模型逆问题的分段轨迹拼接 | 把生成轨迹的起点和多个中间状态都作为优化变量，用短程积分的终点与下一段起点之差约束衔接，再交替更新轨迹和满足观测的最终图像。反传可局限在短段内，降低整条流轨迹反传的显存开销。 |
| <a id="ding26p-optimization"></a>[Improving Explicit Dynamic Gaussian Splatting Optimization via Update Mixture](https://proceedings.mlr.press/v306/ding26p.html) | 动态高斯属性平均 | 逐帧优化时，运动可能使显式高斯基元偏向特定帧。训练后期定期保存基元属性并对末尾若干快照取均值，可减轻由帧偏好引起的测试表现波动。 |

<a id="by-reinforcement-learning"></a>

### 强化学习方法

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="ba26a-reinforcement-learning"></a>[Pareto-Guided Optimal Transport for Multi-Reward Alignment](https://proceedings.mlr.press/v306/ba26a.html) · [论文卡](../conferences/icml-2026/cards/0101-0200.md#paper-ba26a) | 多奖励生成优化 | 对同一个提示构造样本的 Pareto 前沿，再用最优传输把被支配样本推向前沿，降低整个数据集共用一个加权奖励所带来的投机空间。 |
| <a id="chen26as-reinforcement-learning"></a>[Test-Time Reinforcement Learning for Flow Matching](https://proceedings.mlr.press/v306/chen26as.html) | 流匹配测试时优化 | 把中间潜变量看作待选择状态，在同一速度场中用随机 rollout 探索。先按高噪声阶段的奖励差稳定结构，再用组相对优势调整低噪声细节。 |
| <a id="chen26ea-reinforcement-learning"></a>[RELO: Reinforcement Learning to Localize for Visual Object Tracking](https://proceedings.mlr.press/v306/chen26ea.html) | 目标跟踪定位策略 | 先预热边界框回归头，再把特征图上的位置作为动作，用采样位置对应的预测框计算逐帧 IoU 和序列 AUC 奖励，以 actor-critic 更新定位策略，使训练能直接利用跟踪评测指标。 |
| <a id="choi26o-reinforcement-learning"></a>[Rethinking the Design Space of Reinforcement Learning for Diffusion Models: On the Importance of Likelihood Estimation Beyond Loss Design](https://proceedings.mlr.press/v306/choi26o.html) | 扩散强化学习的样本似然估计 | 直接从生成终样本正向加噪，用加权流匹配误差计算 ELBO 似然估计，使策略更新可复用 ODE 采样结果，无需记录随机去噪轨迹。论文交叉比较采样、估计和目标函数，发现似然估计的选择对训练效果影响最大。 |
| <a id="guo26h-reinforcement-learning"></a>[Probabilistic Salient Object Ranking](https://proceedings.mlr.press/v306/guo26h.html) | 显著物体排序的多轨迹奖励 | 用基于人类注视的概率树提供多个合理的注意转移序列及其得分。训练时在每组保留最高分与最低分路径并采样其余路径，以相对奖励学习观看顺序的分布。 |
| <a id="han26o-reinforcement-learning"></a>[ForceForget: Reinforcement Concept Removal for Enhancing Safety in Text-to-Image Models](https://proceedings.mlr.press/v306/han26o.html) | 扩散模型的局部文本概念擦除 | 在交叉注意力中用安全适配器仅变换部分文本特征，再以概念擦除奖励强化目标行为。这样可压低不安全概念的生成，同时在所测数据上保留同一提示中的良性语义。 |

<a id="by-training-strategies"></a>

### 训练策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="bai26n-training-strategies"></a>[Optimizing Few-Step Generation with Adaptive Matching Distillation](https://proceedings.mlr.press/v306/bai26n.html) · [论文卡](../conferences/icml-2026/cards/0101-0200.md#paper-bai26n) | 少步生成蒸馏 | 当真实教师的引导失真、生成教师的排斥又不足时，用奖励代理识别异常区域，重新分配纠偏梯度并加强对坍缩模式的排斥。 |
| <a id="cai26h-training-strategies"></a>[Mode Seeking meets Mean Seeking for Fast Long Video Generation](https://proceedings.mlr.press/v306/cai26h.html) · [论文卡](../conferences/icml-2026/cards/0301-0400.md#paper-cai26h) | 长视频生成 | 用有限长视频监督全局流匹配头学习叙事与运动，再用冻结的短视频教师对滑窗局部做反向 KL 匹配，让长程一致性与局部质感各有监督。 |
| <a id="cao26o-training-strategies"></a>[Beyond Static Allocation: Dynamic Sensitivity-Aware Fine-Tuning for Vision Transformers](https://proceedings.mlr.press/v306/cao26o.html) | 动态参数高效微调 | 定期重测视觉 Transformer 各处的敏感性，把学过的适配模块冻结，再将可训练参数额度分给新出现的敏感位置。 |
| <a id="chavhan26a-training-strategies"></a>[NanoFLUX: Distillation-Driven Compression of Large Text-to-Image Generation Models for Mobile Devices](https://proceedings.mlr.press/v306/chavhan26a.html) | 端侧文生图蒸馏 | 分阶段裁剪扩散 Transformer，并只让中间块用降采样 token；再用去噪器早期层的视觉信号蒸馏文本编码器，把压缩分摊到多个环节。 |
| <a id="chen26cn-training-strategies"></a>[Focusing: View-Consistent Sparse Voxels for Efficient 3D VAE Training](https://proceedings.mlr.press/v306/chen26cn.html) | 视图一致的三维 VAE 稀疏训练 | 训练时将潜体素投影到当前视角，用真值网格的渲染深度筛除远离可见表面的体素，并保留命中体素的邻域，使解码和注意力的开销集中在当前渲染损失可监督的区域。 |
| <a id="chen26dm-training-strategies"></a>[3DGS-HPC: Distractor-free 3D Gaussian Splatting with Hybrid Patch-wise Classification](https://proceedings.mlr.press/v306/chen26dm.html) | 高斯泼溅的瞬态区域筛除 | 以规则图像块为单位汇总训练图与渲染图之间的误差。用 RGB 差异估计静态区域比例，再据此约束感知误差的筛除阈值，减少把纹理弱的静态区域误判成瞬态干扰。 |
| <a id="chen26eu-training-strategies"></a>[Context Forcing: Consistent Autoregressive Video Generation with Long Context](https://proceedings.mlr.press/v306/chen26eu.html) | 长上下文视频蒸馏 | 让教师和学生都读取长视频历史，避免短窗口教师给出的监督只覆盖局部时序。缓存用滚动队列保留近期帧，并按相邻键向量的差异挑选有新信息的词元长期保留。 |
| <a id="chu26b-training-strategies"></a>[End-to-End Autoregressive Image Generation with 1D Semantic Tokenizer](https://proceedings.mlr.press/v306/chu26b.html) | 图像词元化与生成联合训练 | 用量化指示向量与嵌入表的矩阵乘积替代生成器查表，让下一词元预测的梯度可回传到视觉词元化器。词元由此同时接受图像重建和自回归生成监督。 |
| <a id="cui26g-training-strategies"></a>[Hard Labels In! Rethinking the Role of Hard Labels in Mitigating Local Semantic Drift](https://proceedings.mlr.press/v306/cui26g.html) | 稀疏软标签的硬标签校准 | 先用有限裁剪视图的教师软标签训练，再插入图像级硬标签训练以校准受局部裁剪影响的同类语义，最后恢复软标签训练。在论文的数据蒸馏实验中，该顺序改善了低软标签存储预算下的泛化。 |
| <a id="ding26t-training-strategies"></a>[SpeedVFI: One-step Diffusion for Efficient Video Frame Interpolation](https://proceedings.mlr.press/v306/ding26t.html) | 多帧插值扩散的一步蒸馏 | 蒸馏多步教师时，在分布匹配之外加入潜空间流匹配和像素重建监督，使一次去噪能够同时预测多个关键帧之间的过渡帧，并保留运动连续性。 |
| <a id="dong26k-training-strategies"></a>[TurboGS: Accelerating 3D Gaussian Splatting via Error-Guided Sparse Pixel Sampling and Optimization](https://proceedings.mlr.press/v306/dong26k.html) | 高斯泼溅的误差引导像素采样 | 以多视角重建误差选择需要反传的图块和像素，降低对已重建区域的重复计算。在稀疏像素上加归一化互相关结构损失，为细节优化保留局部结构监督。 |
| <a id="dong26l-training-strategies"></a>[RePack then Refine: Efficient Diffusion Transformers with Vision Foundation Models](https://proceedings.mlr.press/v306/dong26l.html) | 视觉基础特征的压缩生成与细化 | 先将高维视觉基础模型特征投影到紧凑潜空间，再在其上训练标准扩散 Transformer。最后用潜变量引导的细化器补回压缩损掉的高频细节，分开承担语义生成与纹理恢复。 |
| <a id="du26g-training-strategies"></a>[Can We Build a Monolithic Model for Fake Image Detection? SICA: Semantic-Induced Constrained Adaptation for Unified-Yet-Discriminative Artifact Feature Space Reconstruction](https://proceedings.mlr.press/v306/du26g.html) | 统一图像取证的受限低秩适配 | 冻结 CLIP 视觉主干以保留图像类别的语义结构，仅在自注意力投影中加入可训练的低秩更新。让同一检测器在保留语义结构的同时拟合不同取证子域的伪造痕迹，减轻多域训练中的表征坍缩。 |
| <a id="du26q-training-strategies"></a>[VideoGPA: Distilling Geometry Priors for 3D-Consistent Video Generation](https://proceedings.mlr.press/v306/du26q.html) | 视频扩散的三维一致性偏好 | 从生成视频估计深度和相机位姿，把各帧反投影成三维点，再根据点投回其他帧的误差给视频打分。用这些分数构造同一条件下的偏好对，以 DPO 微调视频扩散模型。 |
| <a id="esteves26a-training-strategies"></a>[Spectrally-Guided Diffusion Noise Schedules](https://proceedings.mlr.press/v306/esteves26a.html) | 由图像功率谱确定扩散日程 | 按训练图像的径向平均功率谱确定适用的噪声区间和各频段对应的噪声水平。生成时先按类别或提示采样功率谱参数，再构造对应日程，以减少少步去噪中的冗余。 |
| <a id="gong26j-training-strategies"></a>[Light Up Your Face: A Physically Consistent Dataset and Diffusion Model for Face Fill-Light Enhancement](https://proceedings.mlr.press/v306/gong26j.html) | 物理平面光照监督的补光条件 | 将光源的六维物理参数映射为扩散模型条件 token，预训练时用这些 token 重建圆盘光源照到平面的 RGB 辐照度图和逐像素方向场。该辅助任务使控制表示同时编码光强和光照方向，再用于人脸补光。 |

<a id="by-data-strategies"></a>

### 数据策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="cai26m-data-strategies"></a>[FUSE: Full-spectrum Unlearnable Examples via Spectral Equalization](https://proceedings.mlr.press/v306/cai26m.html) · [论文卡](../conferences/icml-2026/cards/0301-0400.md#paper-cai26m) | 图像训练数据保护 | 训练扰动生成器时随机遮掉连续频带，再约束高低频一致，降低保护信号被低通滤波一次清除的风险。 |
| <a id="cao26s-data-strategies"></a>[Where Detectors Fail: Probing Generative Space for Generalizable AI-Generated Image Detection](https://proceedings.mlr.press/v306/cao26s.html) | 合成图检测 | 用当前检测器给生成样本打分，再沿生成模型的内部表征寻找难识别的真实感图像。把这些漏检候选回灌训练，可补足标准采样探索不到的区域。 |
| <a id="chen26s-data-strategies"></a>[When Preference Labels Fall Short: Aligning Diffusion Models from Real Data](https://proceedings.mlr.press/v306/chen26s.html) | 生成偏好数据 | 以真实图像作偏好基准，将模型生成结果或扰动样本作为对照，可以在缺少人工偏好对时构造图像对齐监督。 |
| <a id="chen26bj-data-strategies"></a>[Amodal Instance Segmentation with IRAIS Dataset for Sim-to-Real Transfer](https://proceedings.mlr.press/v306/chen26bj.html) | 跨域遮挡分割数据 | 对物理仿真中摆放的三维商品场景做多视角渲染，自动生成可见与完整实例掩码。让合成集和人工标注的真实集共享标签定义与评测协议，可直接测量遮挡分割的跨域表现。 |
| <a id="cui26f-data-strategies"></a>[Geometry-Aware Dataset Condensation for Diffusion Model Training](https://proceedings.mlr.press/v306/cui26f.html) | 扩散训练子集的单边部分传输 | 按类用嵌入距离匹配训练子集与全量数据，要求子集的概率质量全部运输，同时只限制全量侧的到达容量。允许全量数据的部分质量不匹配，避免少量样本被迫同时代表核心分布和稀疏区域。 |
| <a id="fang26s-data-strategies"></a>[Real Data Lies: Unveiling and Closing the Quality Shortcut in Generalizable AI-Generated Video Detection](https://proceedings.mlr.press/v306/fang26s.html) | 生成视频检测的质量分布配对 | 按质量分布匹配真实与生成视频，再成对补充低质量和超高质量数据源。让两类覆盖相近的质量范围，可抑制检测器把画质当真伪标签的捷径，提升对不同质量真实视频的泛化。 |
| <a id="gan26d-data-strategies"></a>[Set-Coupled Guidance: Set-Level Coordination in Diffusion-Based Dataset Distillation](https://proceedings.mlr.press/v306/gan26d.html) | 扩散数据蒸馏的集合耦合引导 | 同批生成每类的多个合成样本，对它们的去噪潜变量提取低维描述量并匹配真实样本描述量的经验特征函数。再以核耦合协调样本更新，使每步引导能调整整组样本的统计量。 |

<a id="by-inference"></a>

### 推理策略

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="alesiani26a-inference"></a>[Logical Guidance for the Exact Composition of Diffusion Models](https://proceedings.mlr.press/v306/alesiani26a.html) · [论文卡](../conferences/icml-2026/cards/0001-0100.md#paper-alesiani26a) | 扩散模型逻辑控制 | 将逻辑约束编译成电路，若合取子式条件独立、析取子式条件独立或互斥，即可从原子属性的后验和分数递推精确引导。 |
| <a id="bae26b-inference"></a>[Training-Free Coverless Multi-Image Steganography with Access Control](https://proceedings.mlr.press/v306/bae26b.html) · [论文卡](../conferences/icml-2026/cards/0101-0200.md#paper-bae26b) | 图像隐写 | 用随机基压制潜变量中的结构残留，再融合多张图像的潜变量，使同一扩散载体可按授权分别恢复不同隐藏内容。 |
| <a id="bang26a-inference"></a>[Triadic Dynamics Aware Diffusion Posterior Sampling for Inverse Problems: Optimizing Guidance and Stochasticity Schedules](https://proceedings.mlr.press/v306/bang26a.html) · [论文卡](../conferences/icml-2026/cards/0201-0300.md#paper-bang26a) | 扩散逆问题 | 早期大幅 CFG 可能与观测一致性更新冲突。采样中逐步降低数据一致性引导和随机性、提高 CFG，可以分别兼顾观测和生成质量。 |
| <a id="briq26a-inference"></a>[Exploring and Exploiting Stability in Latent Flow Matching](https://proceedings.mlr.press/v306/briq26a.html) · [论文卡](../conferences/icml-2026/cards/0301-0400.md#paper-briq26a) | 潜空间流匹配 | 不同容量的模型对同一噪声种子会生成相近内容，因此可用小模型完成前段流轨迹，再交给大模型补后段细节。 |
| <a id="cai26g-inference"></a>[Improving Classifier-Free Guidance of Flow Matching via Manifold Projection](https://proceedings.mlr.press/v306/cai26g.html) · [论文卡](../conferences/icml-2026/cards/0301-0400.md#paper-cai26g) | 无分类器引导 | 把 CFG 视为带流形约束的连续优化，在每个采样阶段加入投影式修正，并利用 Anderson 加速抑制引导强度敏感性。 |
| <a id="cai26n-inference"></a>[TIMI: Training-Free Image-to-3D Multi-Instance Generation with Spatial Fidelity](https://proceedings.mlr.press/v306/cai26n.html) · [论文卡](../conferences/icml-2026/cards/0301-0400.md#paper-cai26n) | 多实例图像到三维 | 去噪早期用实例级分离引导避免对象粘连，再用几何适应更新稳住形状及相对布局，无需训练多实例模型。 |
| <a id="cao26e-inference"></a>[Efficient Learned Image Compression without Entropy Coding](https://proceedings.mlr.press/v306/cao26e.html) · [论文卡](../conferences/icml-2026/cards/0301-0400.md#paper-cao26e) | 低延迟图像压缩 | 用向量量化减小索引频率不均，再用条件自回归变换减少潜变量间依赖，使紧凑码流可以省掉串行熵编码。 |
| <a id="chang26c-inference"></a>[ContrastiveCFG: Guiding Diffusion Sampling by Contrasting Positive and Negative Concepts](https://proceedings.mlr.press/v306/chang26c.html) | 扩散正负概念引导 | 用对比损失分别吸引所需概念和排斥不需要的概念，避免简单取反无分类器引导时把样本推离可生成的分布。 |
| <a id="chen26v-inference"></a>[PRISM: Training-Free Video Anomaly Detection via Intrinsic Statistical Modeling](https://proceedings.mlr.press/v306/chen26v.html) | 免训练视频异常检测 | 利用冻结多模态嵌入，在特征空间做差分放大和白化，抑制正常背景共有成分，从而用低开销提高异常信号的可辨识度。 |
| <a id="chen26aj-inference"></a>[Normalizing Flows with Iterative Denoising](https://proceedings.mlr.press/v306/chen26aj.html) | 归一化流采样 | 保持训练端到端最大似然，采样时在自回归输出后追加迭代去噪，从而把精确似然训练与多步图像细化结合。 |
| <a id="chen26bp-inference"></a>[Bi-Anchor Interpolation Solver for Accelerating Generative Modeling](https://proceedings.mlr.press/v306/chen26bp.html) | 流匹配的双锚点积分 | 用冻结主干确定积分区间两端的速度，再由轻量旁路网络从两个方向批量估计区间内速度并做高阶数值积分。在 ImageNet-256 实验中，用 10 次主干评估达到与百步欧拉法相近的生成质量。 |
| <a id="chen26dn-inference"></a>[XSpecMesh: Quality-Preserving Auto-Regressive Mesh Generation Acceleration via Multi-Head Speculative Decoding](https://proceedings.mlr.press/v306/chen26dn.html) | 网格词元的投机解码 | 让轻量多头并行预测后续网格词元，主干用一次带因果掩码的前向计算核验。保留主干赋予概率达到阈值的连续前缀，从第一个未通过的位置重新采样。 |
| <a id="chen26ey-inference"></a>[SemanticNVS: Improving Semantic Scene Understanding in Generative Novel View Synthesis](https://proceedings.mlr.press/v306/chen26ey.html) | 新视角扩散的语义条件 | 逐步去噪时，在有观测覆盖的像素用从输入视图变换过来的语义特征，在其余像素从当前预测的干净图中提取 DINO 特征，让相机位移较大时仍有语义条件可用。 |
| <a id="chen26fc-inference"></a>[ScalingAR: Scaling Confidence for Autoregressive Image Generation](https://proceedings.mlr.press/v306/chen26fc.html) | 自回归图像采样的轨迹剪枝 | 用视觉 token 的预测熵与条件信号评估正在生成的轨迹，并随置信度调整条件引导强度、提前停止低分轨迹。这样可在潜 token 空间分配采样预算，省去中途解码图像和调用外部评分器。 |
| <a id="chen26fq-inference"></a>[GuidedBridge: Training-freely Improving Bridge Models with Prior Guidance](https://proceedings.mlr.press/v306/chen26fq.html) | 桥式生成模型的分频先验引导 | 对输入先验做模糊等退化构造弱版本，每步外推强弱先验下的去噪结果。按桥采样两端信噪比较高的特点，在早段和末段加强高频引导，低频引导则贯穿整个轨迹。 |
| <a id="cheng26b-inference"></a>[FS-I2P: A Hierarchical Focus–Sweep Registration Network with Dynamically Allocated Depth](https://proceedings.mlr.press/v306/cheng26b.html) | 图像到点云配准的动态交互深度 | 对每个尺度池化图像和点云词元，交给以匹配误差倒数为奖励训练的策略选择 Mamba 交互次数。允许跳过某一尺度，避免在当前场景不需要的层级反复细化对应关系。 |
| <a id="cho26a-inference"></a>[TAG: Tangential Amplifying Guidance for Hallucination-Resistant Sampling](https://proceedings.mlr.press/v306/cho26a.html) | 扩散采样的切向增量放大 | 用当前潜变量方向分解基础求解器给出的采样增量，保留径向分量，只放大正交的切向分量。该操作直接复用求解器增量，在论文的语义幻觉评测中改善了图像与条件的一致性。 |
| <a id="cho26d-inference"></a>[Balancing Fidelity and Diversity in Diffusion Models via Symmetric Attention Decomposition: Hopfield Perspective](https://proceedings.mlr.press/v306/cho26d.html) | 扩散注意力的反对称分量调节 | 把 softmax 前的注意力矩阵分成对称和反对称部分，缩放反对称部分后重新检索特征，再把特征变化混回原结果并匹配尺度。可用缩放和混合强度调节生成结果的保真度与多样性。 |
| <a id="choi26m-inference"></a>[Concept Removal Guidance: Evidence-Calibrated Negative Guidance for Safe Diffusion Sampling](https://proceedings.mlr.press/v306/choi26m.html) | 扩散负引导的阈值投影 | 在每个去噪步用模型自身的噪声预测估计待抑制概念的存在度，把阈值写成噪声向量上的仿射约束。仅当估计超过阈值时，将原预测投影到可行半空间，以最小的欧氏改动校正该步引导。 |
| <a id="cong26a-inference"></a>[RT-Lynx: Putting GEMM Sparsity in the Right Place for Diffusion Models](https://proceedings.mlr.press/v306/cong26a.html) | 扩散 Transformer 激活稀疏推理 | 对 QKV 投影和 MLP 线性层的输入激活在线施加 N:M 稀疏化，再用低秩 LoRA 补偿重建误差。实验中激活比权重更能承受同类稀疏化，专用 CUDA 核把这一特性转化为线性层加速。 |
| <a id="damblon26a-inference"></a>[SG2Loc: Sequential Visual Localization on 3D Scene Graphs](https://proceedings.mlr.press/v306/damblon26a.html) | 场景图粒子滤波定位 | 对每个候选相机位姿投影场景图中物体的粗网格，用可见物体与图像分块的语义相似度给粒子加权，再用连续帧反复更新位姿分布，无须存储密集参考图像库。 |
| <a id="deng26a-inference"></a>[STORM: Segment, Track, and Object Re-Localization from a Single Image](https://proceedings.mlr.press/v306/deng26a.html) | 六维位姿跟踪的漂移重定位 | 用匹配和错配的观测—记忆对训练二元验证器。跟踪时平滑当前裁剪与高置信历史裁剪的兼容度，连续多帧低于阈值才触发重定位，有助于从遮挡造成的跟踪丢失中恢复。 |
| <a id="deng26i-inference"></a>[Forget-It-All: Multi-Concept Machine Unlearning via Concept-Aware Neuron Masking](https://proceedings.mlr.press/v306/deng26i.html) | 多概念遗忘的掩码合并 | 分别找出对各目标概念敏感的连接，再统计每条连接被多少个概念选中。合并掩码时保留跨许多概念重复出现的连接，只剪除对少数目标敏感的部分，以减轻多概念移除造成的生成退化。 |
| <a id="duan26d-inference"></a>[SlerpFlow: Spherical Trajectory Correction for Rectified Flow Inversion](https://proceedings.mlr.press/v306/duan26d.html) | 整流流反演的球面校正 | 将潜状态拆成模长与单位方向，沿径向速度更新模长，并在当前与预测方向间做球面线性插值。再用校正目标与当前状态的差合成步进速度，缓存后供后续步使用，以少量额外计算修正反演轨迹。 |
| <a id="elbrachter26a-inference"></a>[MAD: Manifold Attracted Diffusion](https://proceedings.mlr.press/v306/elbrachter26a.html) | 带噪训练数据的扩散采样修正 | 在同一采样点用相邻噪声尺度的分数差分估计分数对尺度的导数，再将其与原分数结合更新样本，以压低带噪训练数据中偏离数据流形的小幅扰动。 |
| <a id="fang26n-inference"></a>[Trajectory-Aware Spiking DiTs Conversion via Membrane Potential Error-Feedback](https://proceedings.mlr.press/v306/fang26n.html) | 脉冲扩散的膜电位误差反馈 | 把当前去噪步结束时的残余膜电位用作下一步脉冲神经元的初值。利用相邻去噪步的激活相似性，将尚未触发脉冲的残差传到后续步骤，减少转换误差的累积。 |
| <a id="fang26z-inference"></a>[StreamFlow: Theory, Algorithm, and Implementation for High-Efficiency Rectified Flow Generation](https://proceedings.mlr.press/v306/fang26z.html) | 异构时间步的整流流批处理 | 将批内不同时间步到速度场时间窗的查找写成掩码运算，并并行计算各样本的窗边界和系数，使不同去噪进度的请求能共享批执行，减少逐样本调度。 |
| <a id="feng26g-inference"></a>[Explainable Forensics of Manipulated Segments in Untrimmed Long Videos](https://proceedings.mlr.press/v306/feng26g.html) | 长视频篡改的边界感知定位 | 用滑动窗口把真实、合成、真到假及假到真的过渡分成四类，以过渡信号提出可疑片段，再用多模态模型精修起止时间并解释视觉线索。 |
| <a id="feng26r-inference"></a>[HEDP: A Hybrid Energy-Distance Prompt-based Framework for Domain Incremental Learning](https://proceedings.mlr.press/v306/feng26r.html) | 增量域预测的能量距离加权 | 对测试图像并行计算到各域 CLIP 特征中心的距离和使用各域提示时的预测能量，再把两类分数融合为预测权重，使未知域的输入也可借用已学域的提示。 |
| <a id="feng26t-inference"></a>[Fast-SAM3D: 3Dfy Anything in Images but Faster](https://proceedings.mlr.press/v306/feng26t.html) | 单图三维生成的分量差异缓存 | 稀疏结构去噪中，形状词元的变化较平滑，可从两次实际网络计算的差分外推被跳过的步骤。单独处理波动更大的位姿和尺度词元，可避免相同外推规则引起布局漂移。 |
| <a id="feng26w-inference"></a>[Bridging RGB and RAW: Single-step Deterministic Flow with Homogeneous Representation Alignment](https://proceedings.mlr.press/v306/feng26w.html) | RGB 到 RAW 的一步潜空间传输 | 让同一编码器处理对齐后的 RGB 和 RAW，在其潜变量线性插值路径上学习速度场。推理时从输入 RGB 潜变量执行一步确定性传输，再解码为 RAW。 |
| <a id="feng26ac-inference"></a>[Enhancing Train-Free Infinite-Frame Generation for Consistent Long Videos](https://proceedings.mlr.press/v306/feng26ac.html) | 长视频队列的双向一致性引导 | 在自回归去噪队列尾部评估并修正新加入的高噪潜帧，同时用队列头部的低噪潜帧指导局部去噪，分别约束新帧质量和较远帧之间的连续性。 |
| <a id="frumkin26a-inference"></a>[Q-Sched: Pushing the Boundaries of Few-Step Diffusion Models with Quantization-Aware Scheduling](https://proceedings.mlr.press/v306/frumkin26a.html) | 低比特少步扩散的调度校准 | 冻结量化去噪器，只拟合修正少步轨迹的预条件系数。用少量文本提示优化图文对齐与图像质量的联合指标，可在校准时省去全精度教师前向。 |
| <a id="fu26o-inference"></a>[Dual Optimal Transport for Multi-Concept Composition: Structure Alignment and Texture Injection in Diffusion Models](https://proceedings.mlr.press/v306/fu26o.html) | 低频几何引导的参考纹理迁移 | 先以重心软传输对齐参考对象与生成布局，再用低频特征与空间距离计算传输代价。按该传输计划迁移参考图的高频残差，使纹理细节落在结构相符的位置。 |
| <a id="gao26e-inference"></a>[Taming I2V models for Image HOI Editing: A Cognitive Benchmark and Agentic Self-Correcting Framework](https://proceedings.mlr.press/v306/gao26e.html) | 用图生视频过程纠正人和物的交互编辑 | 先把目标交互指令交给图生视频模型，再用视觉语言模型检查中途帧，定位操作了错误对象等失误。根据诊断更新提示和经验记录并重新生成，最后选出呈现目标交互的视频帧作为编辑图像。 |
| <a id="gao26x-inference"></a>[(1D) Ordered Tokens Enable Efficient Test-Time Search](https://proceedings.mlr.press/v306/gao26x.html) | 粗到细图像词元的前缀搜索 | 图像由粗到细的有序词元表示时，短前缀已能解码成可评价的全局语义图像。用图文验证器逐轮给这些中间图像打分，可在生成早期剪掉与提示不符的分支。 |
| <a id="gu26f-inference"></a>[Mitigating Noise-Induced Layout Priors for Object Counting in Diffusion Models](https://proceedings.mlr.press/v306/gu26f.html) | 扩散生成的实例数布局控制 | 初始噪声可通过早期交叉注意力固定物体布局，使更改提示里的数量仍沿用原布局。采样时先按目标个数调整初始潜噪声，再优化早期注意力以稳定物体布置，可提高指定数量的命中率。 |
| <a id="gu26m-inference"></a>[R$^3$L: Reasoning 3D Layouts from Relative Spatial Relations](https://proceedings.mlr.press/v306/gu26m.html) | 三维相对关系链的坐标分解 | 把长空间关系链拆成参考系较稳定的短段，先生成候选布局并反查关系冲突，再用全局到局部的坐标重参数化优化物体位姿。这样可减少反复变换参考系积累的语义和度量误差。 |
| <a id="guo26s-inference"></a>[Sample Margin-Aware Recalibration of Temperature Scaling](https://proceedings.mlr.press/v306/guo26s.html) | 按分类间隔自适应温度校准 | 让小型 MLP 把最大与次大 logit 的差映射为样本温度，用 Charbonnier 平滑的软分箱校准误差训练。正温度缩放可改变置信度而保持类别排序，映射参数量不随类别数增长。 |
| <a id="gupta26a-inference"></a>[Divide-and-Denoise: A Game-Theoretic Method for Fairly Composing Diffusion Models](https://proceedings.mlr.press/v306/gupta26a.html) | 多扩散模型的公平区域分工 | 每个去噪步把潜特征视为可分配资源，在公平约束下为多个预训练模型分配区域以最大化总效用。对连续两步分配加入 KL 代价，再按区域组合去噪结果，使模型分工随生成逐渐演化。 |
| <a id="han26l-inference"></a>[Physics in 2-Steps: Locking Motion Priors Before Visual Refinement Erases Them](https://proceedings.mlr.press/v306/han26l.html) | 用两步视频生成约束后续运动相位 | 先用两步采样得到运动较一致的潜视频，提取相邻帧差分，并在高保真去噪中持续用它引导运动。频谱分析表明，这种约束可减轻更多去噪步带来的相位衰减。 |

<a id="by-representation-learning"></a>

### 表征学习

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="bian26d-representation-learning"></a>[CURE: Consistency-under-Unified Semantic Regularization for Generalized Category Discovery](https://proceedings.mlr.press/v306/bian26d.html) · [论文卡](../conferences/icml-2026/cards/0201-0300.md#paper-bian26d) | 新类别发现 | 先用已知类原型训练语义结构，再用带语义正则的一致性学习扩展未知类，避免过早的全局均匀排布冲淡类别结构。 |
| <a id="boduljak26a-representation-learning"></a>[VFMF: Dense Forecasting by Generating Vision Foundation Model Features](https://proceedings.mlr.press/v306/boduljak26a.html) · [论文卡](../conferences/icml-2026/cards/0301-0400.md#paper-boduljak26a) | 视频特征预测 | 先把视觉基础模型特征压到适合生成的紧凑潜空间，再用条件流匹配采样未来。在部分可见时可表达多个可能未来，且比直接扩散原特征或 PCA 压缩保留更多信息。 |
| <a id="cao26h-representation-learning"></a>[On the Power of Statistics in Class-Incremental Learning with Pretrained Models](https://proceedings.mlr.press/v306/cao26h.html) · [论文卡](../conferences/icml-2026/cards/0301-0400.md#paper-cao26h) | 类别增量学习 | 冻结视觉骨干，只维护逐类的特征统计量并用它们推断，可以作为检验复杂持续训练方法是否带来收益的强基线。 |
| <a id="cassano26a-representation-learning"></a>[SAEmnesia: Erasing Concepts in Diffusion Models with Supervised Sparse Autoencoders](https://proceedings.mlr.press/v306/cassano26a.html) | 扩散概念遗忘 | 用标签训练稀疏自编码器，将每个概念的激活集中在单个可解释神经元，便于有针对性地擦除并依次处理多个概念。 |
| <a id="cendra26a-representation-learning"></a>[PartCo: Part-Level Correspondence Priors Enhance Category Discovery](https://proceedings.mlr.press/v306/cendra26a.html) | 细粒度类别发现 | 用图像局部部件之间的特征对应为类别聚类补充先验，可以区分全局语义相近、只在局部有差异的类别。 |
| <a id="chen26ca-representation-learning"></a>[Rotation-Invariant Spherical Watermarking via Third-Order SO(3) Representation Coupling](https://proceedings.mlr.press/v306/chen26ca.html) | 球面旋转不变水印 | 对球谐系数做三阶张量耦合并投影到 SO(3) 的平凡表示，构造保留相对相位信息的旋转不变双谱。可在高阶球谐系数中嵌入水印，再从双谱标量中解码全景图的水印。 |
| <a id="chen26ee-representation-learning"></a>[DynaTok: Token-Based 4D Reconstruction from Partial Point Clouds](https://proceedings.mlr.press/v306/chen26ee.html) | 动态点云的参考与残差表征 | 把逐帧不完整点云编码成固定数量的 token 并跨帧聚合，以首帧为共享参考，用潜空间残差表示各帧变化。条件流匹配解码器利用两者重建完整点云，训练只需要各帧完整点云监督，无需点对应或运动标签。 |
| <a id="chen26ek-representation-learning"></a>[Multiview Self-Representation Learning across Heterogeneous Views](https://proceedings.mlr.press/v306/chen26ek.html) | 异构视觉表征的聚类共识 | 对同一张无标签图像，各预训练模型的特征分别经对应视图模型预测簇分配概率。对这些概率取平均并选概率最高的簇作伪标签，再用它监督所有视图，使一致性约束建立在共同的簇空间上。 |
| <a id="chen26fh-representation-learning"></a>[TrustworthyQENN: A Quantum Evidential Neural Network Based on Complex-Valued Contrastive Learning for Uncertainty Pattern Classification](https://proceedings.mlr.press/v306/chen26fh.html) | 复数表征的分布外识别 | 用监督对比损失同时约束复数特征的幅值和相位，使同类样本靠近，再将特征转换为含未知类状态的证据幅，并融合多个视图的证据。在所测遥感数据上，联合使用幅相信息可改善分布外识别。 |
| <a id="cui26k-representation-learning"></a>[Bayesian Gated Non-Negative Contrastive Learning](https://proceedings.mlr.press/v306/cui26k.html) | 概率门控的非负对比表征 | 让门控头为非负特征预测逐维 Bernoulli 概率，只在硬掩码保留的维度计算 InfoNCE，并用到稀疏先验的 KL 约束门控。前向执行离散筛选，反向用连续概率传梯度，使特征参与对比的方式随样本变化。 |
| <a id="dai26b-representation-learning"></a>[Identifying Latent Concepts and Structures for Generalized Category Discovery](https://proceedings.mlr.press/v306/dai26b.html) | 基元场重写局部视觉 token | 把图像 patch 分配给少量可学习的视觉基元，结合初始匹配分数和基元从 patch 吸收证据时的注意力来更新分配。再将基元信息按最终分配写回 patch，使新类别可表现为同一组基元的不同局部组合。 |
| <a id="ding26f-representation-learning"></a>[DDSVM: A Differentiable Framework for Deep Support Vector Machines with Iterative Geometry-Aware Optimization](https://proceedings.mlr.press/v306/ding26f.html) | 用 SVM 边界精炼视觉表征 | 用归一化特征拟合线性 SVM，按类别内到分隔超平面的距离生成目标特征，让靠近边界的样本接受较强的间隔扩张监督。更新骨干时把目标视为常量，球面归一化使梯度沿切空间改变特征方向。 |
| <a id="ding26n-representation-learning"></a>[Learning Gaussian Mixture-distributed Prototypes for 3D Scene Graph Generation from RGB-D Sequences](https://proceedings.mlr.press/v306/ding26n.html) | 三维场景图的混合分布原型 | 为对象与关系各类别学习多个高斯分量，表达类别内的多种特征模式。再对共现的节点与边原型做双向注意力，用得到的偏移校正原型均值，约束对象与关系的匹配。 |
| <a id="dou26b-representation-learning"></a>[DNA: Uncovering Universal Latent Forgery Knowledge](https://proceedings.mlr.press/v306/dou26b.html) | 冻结视觉模型中的伪造敏感单元 | 先用特征与注意力诊断定位从全局语义转向局部异常的中间层，再根据多信号融合分数与曲率拐点筛选伪造敏感单元。仅使用这些单元的特征，在所测少样本和未见生成器上也能检测伪造。 |
| <a id="fang26o-representation-learning"></a>[Event2Vec: Processing neuromorphic events directly by representations in vector space](https://proceedings.mlr.press/v306/fang26o.html) | 异步事件的逐事件向量化 | 把事件的坐标与极性嵌入和相邻事件的相对时间嵌入相加，对聚合事件再按簇中原始事件数的对数缩放。所得向量序列可直接输入 Transformer，并保留事件间的时间间隔。 |
| <a id="gao26ad-representation-learning"></a>[ArcDAE: Asymmetric Rectified Contrastive Diffusion Autoencoder for Unified Representation Learning](https://proceedings.mlr.press/v306/gao26ad.html) | 扩散自编码的非对称语义蒸馏 | 用学生的指数移动平均教师编码干净视图，以其停止梯度的嵌入监督学生对含噪、增强视图的编码，使重建仍保有细节时，语义瓶颈对随机扰动更稳定。 |
| <a id="garrido26a-representation-learning"></a>[Learning Latent Action World Models in the Wild](https://proceedings.mlr.press/v306/garrido26a.html) | 真实视频中的连续潜动作 | 从没有动作标注的视频学习有容量约束的连续潜动作，并用预测未来帧的世界模型验证可迁移性。没有统一本体时，动作多以相机为参照而局部化，再用小控制器把已知动作映射到该潜空间做规划。 |
| <a id="guo26e-representation-learning"></a>[Compression as Adaptation: Implicit Visual Representation with Diffusion Foundation Models](https://proceedings.mlr.press/v306/guo26e.html) | 以生成模型适配器编码视频 | 冻结视觉扩散模型，把每段视频的内容拟合成跨层 LoRA 更新，再通过固定伪随机映射让所有层共享同一紧凑向量。解码时用该向量恢复适配参数并生成视频，把视觉内容存进可执行的生成过程。 |

<a id="by-evaluation"></a>

### 评测与诊断

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="acuaviva26a-evaluation"></a>[Rethinking Visual Intelligence: Insights from Video Pretraining](https://proceedings.mlr.press/v306/acuaviva26a.html) · [论文卡](../conferences/icml-2026/cards/0001-0100.md#paper-acuaviva26a) | 视觉推理评测 | 比较视频扩散模型与 LLM 的适配能力时，让两类模型分别用自己的输入模态，并报告数据效率。 |
| <a id="ahmed26a-evaluation"></a>[Med-SegLens: Latent-Level Model Diffing for Interpretable Medical Image Segmentation](https://proceedings.mlr.press/v306/ahmed26a.html) · [论文卡](../conferences/icml-2026/cards/0001-0100.md#paper-ahmed26a) | 分割模型诊断 | 用稀疏自编码器拆解并对齐不同架构及人群的分割激活，再干预与分布偏移相关的潜特征定位和修复错误。 |
| <a id="alexis26a-evaluation"></a>[GEPC: Group-Equivariant Posterior Consistency for Out-of-Distribution Detection in Diffusion Models](https://proceedings.mlr.press/v306/alexis26a.html) · [论文卡](../conferences/icml-2026/cards/0001-0100.md#paper-alexis26a) | 扩散模型域外检测 | 检查输入做旋转或翻转后，扩散分数场是否相应变换。即使分数幅值相近，等变性残差也能暴露域外样本。 |
| <a id="baek26e-evaluation"></a>[Proactive Defense Benchmark against Deepfake Generation](https://proceedings.mlr.press/v306/baek26e.html) · [论文卡](../conferences/icml-2026/cards/0101-0200.md#paper-baek26e) | 深伪防御评测 | 把输出画质和身份保真度分开评估，并校准生成器固有的身份偏差。白盒防御表现特别强时也要检查是否损害跨生成器迁移。 |
| <a id="braun26b-evaluation"></a>[Erased but Not Forgotten: How Backdoors Compromise Concept Erasure](https://proceedings.mlr.press/v306/braun26b.html) · [论文卡](../conferences/icml-2026/cards/0301-0400.md#paper-braun26b) | 扩散模型概念遗忘 | 通过测试擦除前写入的触发关联能否在遗忘后复现概念，可以检查现有擦除方法是否还保留潜在生成路径。 |
| <a id="chen26az-evaluation"></a>[Semantic-level Backdoor Attack against Text-to-Image Diffusion Models](https://proceedings.mlr.press/v306/chen26az.html) | 生成模型后门评测 | 后门可能对语义相同的改写提示共同触发，枚举固定字符串容易漏检。可用语义等价改写、部分语义和正常输入分别测触发、误触发和正常质量。 |
| <a id="chen26gw-evaluation"></a>[Efficient, Validation-Free Intrinsic Quality Estimation for Large-Scale Face Recognition Datasets](https://proceedings.mlr.press/v306/chen26gw.html) | 人脸数据集内在质量估计 | 用轻量代理模型提取人脸嵌入，联合计算近邻身份标签一致性和嵌入协方差谱的归一化有效秩，分别衡量局部标签可靠性与整体多样性，可在完整训练前筛查数据集。 |
| <a id="chung26a-evaluation"></a>[Global Geometry Is Not Enough for Vision Representations](https://proceedings.mlr.press/v306/chung26a.html) | 视觉表征的组合绑定诊断 | 用输入到嵌入的局部雅可比奇异值计算有效秩，衡量模型对多少独立输入方向敏感。在被测视觉编码器上，这一数值与属性绑定表现相关，而全局嵌入几何指标的相关性接近零。 |
| <a id="ebrahimpour-boroojeny26a-evaluation"></a>[Unlearning Isn’t Forgetting: Revealing Hidden Leakage in Class Unlearning Evaluations](https://proceedings.mlr.press/v306/ebrahimpour-boroojeny26a.html) | 类别遗忘的近邻输出泄漏 | 用模型对近邻保留类别的输出训练判别器，并在完整重训模型上建立参照。遗忘类输入即使不再被判为该类，也可能因其在相似类别上的独特输出而被识别，因而可用此探测残留信息。 |
| <a id="elisha26a-evaluation"></a>[ConEx: Human-Interpretable Saliency Maps via Concept-Aware Attribution](https://proceedings.mlr.press/v306/elisha26a.html) | 概念感知的显著性图 | 将类内发现的概念激活向量在空间维度做池化，用所得通道权重混合待解释图像的特征图，得到概念出现位置，再结合该概念对分类分数的贡献生成解释。 |
| <a id="fang26l-evaluation"></a>[iWorld-Bench: A Benchmark for Interactive World Models with a Unified Action Generation Framework](https://proceedings.mlr.press/v306/fang26l.html) | 交互世界模型的统一动作编码 | 将第一人称平移与转动组合编码，再把同一动作映射为相机参数、独热向量或文字指令。用同一组动作任务分别测量不同接口的世界模型在轨迹跟随、视觉生成及场景记忆上的表现。 |
| <a id="han26t-evaluation"></a>[GaussTrace: Provenance Analysis of 3D Gaussian Splatting Models with Evidence-based LLM Reasoning](https://proceedings.mlr.press/v306/han26t.html) | 高斯泼溅资产的变换溯源 | 为候选资产提取各属性的统计指纹，再模拟常见编辑操作检验可能的来源关系。用统计和模拟结果支持方向判断，能在缺少编辑日志时生成带理由的溯源边。 |

<a id="by-theory-statistics"></a>

### 理论与统计

| 论文 | 技术主题 | Insight |
| :--- | :--- | :--- |
| <a id="bradley26a-theory-statistics"></a>[Local Mechanisms of Compositional Generalization in Conditional Diffusion](https://proceedings.mlr.press/v306/bradley26a.html) · [论文卡](../conferences/icml-2026/cards/0301-0400.md#paper-bradley26a) | 扩散组合泛化 | 当条件分数只依赖局部像素及局部条件时，生成可以处理超出训练对象数的场景。显式施加这种局部性，使原先未泛化的 CLEVR 模型也能泛化。 |
| <a id="brady26b-theory-statistics"></a>[Is Generation Required for Data-Efficient Perception?](https://proceedings.mlr.press/v306/brady26b.html) · [论文卡](../conferences/icml-2026/cards/0301-0400.md#paper-brady26b) | 低数据视觉泛化 | 在论文设定的组合生成过程中，解码器只需较简单的组合归纳偏置。训练解码器再做反演，在受控视觉数据中能用更少数据外推新组合。 |
<!-- classification:end -->
