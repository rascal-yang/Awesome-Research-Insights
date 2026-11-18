# NeurIPS 2026 论文卡 7

[会议索引](README.md)

<a id="paper-155683"></a>

## IdealCache: Rethinking Cache Scheduling in Diffusion Transformers via Ideal Trajectories

[官方论文页](https://neurips.cc/virtual/2026/poster/155683) · [作者来源](https://openreview.net/forum?id=3jq55sxmcq)

- **问题 / 瓶颈** · 轨迹匹配会把未经缓存的参考输出当成质量上限。
- **核心创新 / 方法** · 从候选目标解构造轨迹集合，用图汇总后以约束最短路径找非均匀缓存日程。
- **Baseline** · 以参考去噪状态为目标的已有缓存方法。
- **Benchmark** · Qwen-Image、Qwen-Image-Edit、HunyuanVideo，比较质量与速度。
- **关键结果 / 消融** · 报告分别提速 6.35、5.84 和 4.32 倍，质量相当或更优。
- **适用条件 / 局限** · 候选目标和搜索成本、日程能否复用待核。

**可复用机制** · 在包含目标生成与日程搜索的完整耗时下对照逐步误差目标。

<a id="paper-152556"></a>

## IDEAL: In-DEpth ALignment Makes A Discrete Representation AutoEncoder

[官方论文页](https://neurips.cc/virtual/2026/poster/152556) · [作者来源](https://openreview.net/forum?id=SFMjikixfq)

- **问题 / 瓶颈** · 仅用深层语义特征会丢细节，量化使损失更严重。
- **核心创新 / 方法** · 量化表示同时学习浅层局部结构和深层语义对齐。
- **Baseline** · 已有表示自编码器及离散生成对照。
- **Benchmark** · ImageNet 重建 rFID 和自回归生成 gFID。
- **关键结果 / 消融** · rFID 0.61，较先前最好低 0.28；gFID 1.89。
- **适用条件 / 局限** · 依赖视觉教师层间互补性，其他分辨率和域待核。

**可复用机制** · 在相同码率下分别验证浅层对细节与深层对语义的贡献。

<a id="paper-153659"></a>

## IDEAL: Interaction Dynamics and Force-Aware Learning for Dual-Humanoid Collaborative Manipulation

[官方论文页](https://neurips.cc/virtual/2026/poster/153659) · [作者来源](https://openreview.net/forum?id=JhPYWytFsc)

- **问题 / 瓶颈** · 闭链交互与局部观测使只模仿运动难保持两人协同力。
- **核心创新 / 方法** · 从双人视频得到并校正参考运动，再根据刚体和接触约束建立力参考以指导强化学习。
- **Baseline** · 既有双人形模仿和协作路线，具体名称待核。
- **Benchmark** · 双人形协同操作，覆盖模拟和实体机器人。
- **关键结果 / 消融** · 摘要称可在两类环境完成稳健协作，未给数值或消融。
- **适用条件 / 局限** · 依赖视频重建、接触和动力学模型；人机近距离应用待验证。

**可复用机制** · 在普通协同搬运中分别测运动同步、载荷分担和滑移，筛查仅运动模仿的缺口。

<a id="paper-151393"></a>

## IDEA: Unwrapping Visual Black-box Models by Interaction Decomposition

[官方论文页](https://neurips.cc/virtual/2026/poster/151393) · [作者来源](https://openreview.net/forum?id=azDcnhfVNx)

- **问题 / 瓶颈** · 单一概念重要性不能识别上下文依赖。
- **核心创新 / 方法** · 黑盒事后分解概念与语境的预测信息，无须任务专用概念标注。
- **Baseline** · 传统标量概念重要性方法。
- **Benchmark** · 受控和真实视觉评测，判断交互模式是否可见。
- **关键结果 / 消融** · 作者称能揭示标量分数未呈现的依赖。
- **适用条件 / 局限** · 信息估计及概念边界对结果的影响待核。

**可复用机制** · 在概念跨背景配对时检查交互项，定位由背景共同驱动的预测。

<a id="paper-155537"></a>

## Idempotency Exposes Consistency Problems in Sparse Autoencoders

[官方论文页](https://neurips.cc/virtual/2026/poster/155537) · [作者来源](https://openreview.net/forum?id=4rnCZcVRKZ)

- **问题 / 瓶颈** · 低重建误差可能与活跃特征集不稳并存。
- **核心创新 / 方法** · 将解码结果重新编码，比较稀疏坐标、范数、输入缩放敏感性；另加入辅助幂等损失。
- **Baseline** · 常规稀疏自编码器及有无辅助损失。
- **Benchmark** · 多种稀疏自编码器、单潜变量复原、缩放敏感性。
- **关键结果 / 消融** · 多数模型离幂等很远，观察到范数增长与活跃集合变化；辅助损失可缓和。
- **适用条件 / 局限** · 幂等性与真实语义的关系及牺牲的重建质量待核。

**可复用机制** · 给特征字典加重编码回归，分报坐标变化、范数与重建。

<a id="paper-151829"></a>

## Identifiable alignment of unpaired representations

[官方论文页](https://neurips.cc/virtual/2026/poster/151829) · [作者来源](https://openreview.net/forum?id=XeeLVJHtXH)

- **问题 / 瓶颈** · GW 耦合不直接给唯一映射，仅匹配边缘分布也无法识别映射。
- **核心创新 / 方法** · 在度量测度空间上检查局部距离分布的单射性，将耦合化为凸线性规划，再估计地图。
- **Baseline** · GWOT、GAN 映射及监督对齐。
- **Benchmark** · 理论比较同源点无配对样本与独立样本，并与监督基线实证对照。
- **关键结果 / 消融** · 分情况证明有限样本与渐近可识别；算法达到或超过监督基线。
- **适用条件 / 局限** · 局部距离同构或采样噪声过大时可能缺少区分度。

**可复用机制** · 把可辨识诊断放到昂贵拟合前，避免将训练损失低误读成唯一对齐。

<a id="paper-150669"></a>

## Identification and Bounding of Joint Expectation over Potential Outcomes

[官方论文页](https://neurips.cc/virtual/2026/poster/150669) · [作者来源](https://openreview.net/forum?id=gMaaGOx3Yl)

- **问题 / 瓶颈** · 分别观察两个边缘结果不足以确定个体效应分布。
- **核心创新 / 方法** · 在同单调和反单调假设下识别联合函数期望；无此假设时为两类函数构造锐界。
- **Baseline** · 摘要未列命名估计基线；比较有无相依假设的识别范围。
- **Benchmark** · 模拟和真实数据示例，分析离散、连续和混合结果。
- **关键结果 / 消融** · 推导统一识别方式及个体效应矩的边界。
- **适用条件 / 局限** · 需要逐一核实函数类别及其假设；观察数据不能直接验证个体配对。

**可复用机制** · 同时报告可识别边缘、无依赖假设的区间、以及假设下的点估计。

<a id="paper-149969"></a>

## Identified-Set Geometry of Distributional Model Extraction under Top-K Censored API Access

[官方论文页](https://neurips.cc/virtual/2026/poster/149969) · [作者来源](https://openreview.net/forum?id=lqDgPjh2zT)

- **问题 / 瓶颈** · 只限制可见分数不能从分布恢复受限推断能力安全。
- **核心创新 / 方法** · 用理论刻画接口可观测信息下的分布不确定性，并用独立评测比较能力迁移风险。
- **Baseline** · 不同分数可见性和输出接口条件。
- **Benchmark** · Qwen3 数学推理设置，测分布误差与能力迁移。
- **关键结果 / 消融** · 摘要显示二者可显著分离；只看分布恢复会漏估风险。
- **适用条件 / 局限** · 证据限所测接口与数学教师模型。

**可复用机制** · 防御侧审计同时做两类检验，避免用单一分布指标作泄漏保证。

<a id="paper-149053"></a>

## Identifying and Mitigating Diversity Collapse in Zero-Shot Personalization with I2I Editing Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149053) · [作者来源](https://openreview.net/forum?id=tDe4M34lN8)

- **问题 / 瓶颈** · 图像身份与提示对齐较强时，多种种子仍可能产生高度相似结果。
- **核心创新 / 方法** · 发现潜词元轨迹过度对齐，训练外仅干预早期生成潜词元的注意输出，保持图文条件词元。
- **Baseline** · FLUX.1 Kontext、FLUX.2 默认推理。
- **Benchmark** · 多主题与提示，测 Vendi、LPIPS、身份和文本吻合。
- **关键结果 / 消融** · Kontext 上 Vendi 1.546 到 2.066，LPIPS 0.475 到 0.621，条件保真小幅下降。
- **适用条件 / 局限** · 其他编辑架构及高保真身份场景待核。

**可复用机制** · 用固定条件、多种子试验画出多样性和保真度的折中。

<a id="paper-151974"></a>

## Identifying Latent Neural Dynamics with Recognition-Parameterized Gaussian Process Dynamical Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/151974) · [作者来源](https://openreview.net/forum?id=WQv6IOqNHC)

- **问题 / 瓶颈** · 不同观测生成成分的错设会扭曲潜状态和动态估计。
- **核心创新 / 方法** · 以高斯过程非参数地建模状态转移，用识别参数化模型隐式连接观测。
- **Baseline** · 显式流场、观测映射和响应噪声的生成建模路线。
- **Benchmark** · 合成数据及真实神经记录，观察行为相关潜变量。
- **关键结果 / 消融** · 摘要报告发现有意义的行为相关状态和动态。
- **适用条件 / 局限** · 识别参数化和真实潜动态可验证程度待核。

**可复用机制** · 从生成观测族失配的模拟出发，比较识别方案是否减少潜轨迹偏差。

<a id="paper-151733"></a>

## Identifying Structural Biases from Causal Mechanism Shifts

[官方论文页](https://neurips.cc/virtual/2026/poster/151733) · [作者来源](https://openreview.net/forum?id=YUeprsuXFc)

- **问题 / 瓶颈** · 独立同分布与无潜变量假设失效会误导因果发现。
- **核心创新 / 方法** · 将相关机制变化写成互信息判据，按节点分类偏差类型。
- **Baseline** · 现有结构偏差发现方法；名称待核。
- **Benchmark** · 合成与真实数据，评价受影响变量集及偏差类型。
- **关键结果 / 消融** · 摘要称能准确恢复受影响节点及类型并明显领先对照。
- **适用条件 / 局限** · 依赖多环境和识别条件，环境共同变化的影响待核。

**可复用机制** · 拟因果图前单列机制协变诊断，避免把跨环境关联直接当因果边。

<a id="paper-150886"></a>

## i-DEQ: A stable inertial Deep Equilibrium model for image restoration

[官方论文页](https://neurips.cc/virtual/2026/poster/150886) · [作者来源](https://openreview.net/forum?id=efDZxWqk5d)

- **问题 / 瓶颈** · 原平衡模型推理成本高，训练和粗初始化下不稳定。
- **核心创新 / 方法** · 在显式非凸正则框架下为求解迭代引入动量，由理论给出收敛与加速条件。
- **Baseline** · 常规 DEQ 与已有恢复方法。
- **Benchmark** · 多种线性和非线性逆问题，比较重建、推理及初值敏感性。
- **关键结果 / 消融** · 恢复质量相当，推理时间约减半，作者称训练更稳。
- **适用条件 / 局限** · 受正则、迭代与收敛假设限制，其他问题待核。

**可复用机制** · 比较目标残差、解的质量与时延，检验动量是在省步数还是改变解。

<a id="paper-151442"></a>

## iDETR: Implicit DETR for Tiny Object Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/151442) · [作者来源](https://openreview.net/forum?id=afWSKToToO)

- **问题 / 瓶颈** · 离散特征格点定位误差大，多尺度成本高。
- **核心创新 / 方法** · 隐式注意允许连续坐标采样，质心引导查询初始化；按注意头条件采样缩减开销。
- **Baseline** · 已有微小目标检测及多尺度路线。
- **Benchmark** · AI-TODv2，整体 AP、极小对象 AP、计算和内存。
- **关键结果 / 消融** · 整体 +0.2%、极小 +1.1% AP，计算降 37%；条件采样减少查询成本。
- **适用条件 / 局限** · 低分辨率是否丢失可复原信号取决于任务，跨域待核。

**可复用机制** · 等计算比较连续查询与增加特征分辨率，并按目标尺寸分桶。

<a id="paper-148764"></a>

## IFDECORATOR: Wrapping Instruction Following Reinforcement Learning with Verifiable Rewards

[官方论文页](https://neurips.cc/virtual/2026/poster/148764) · [作者来源](https://openreview.net/forum?id=vEcdUTiDxm)

- **问题 / 瓶颈** · 形式验证可能给走捷径的回答奖励。
- **核心创新 / 方法** · 用协作对抗数据过程调整难度，以 IntentCheck 门控，并以诊断独立评估异常。
- **Baseline** · 原始 Qwen2.5-32B-Instruct、GPT-4o；其他配置待核实。
- **Benchmark** · IFEval、FollowBench 和通用能力检查。
- **关键结果 / 消融** · 3,625 个训练例得到 IFEval 87.43%；FollowBench 改善 4.2%。
- **适用条件 / 局限** · 意图检查和诊断的错误率、可扩展性需核实。

**可复用机制** · 把训练任务难度和验证器忠实度分开调节，并保留独立的可靠性诊断。

<a id="paper-155215"></a>

## IGGT4D: Streaming 4D Instance-Grounded Geometry Transformer

[官方论文页](https://neurips.cc/virtual/2026/poster/155215) · [作者来源](https://openreview.net/forum?id=7Q59ZVBlfK)

- **问题 / 瓶颈** · 仅维护几何难表示运动、消失与重现的实体。
- **核心创新 / 方法** · 逐帧因果建模复用历史上下文，在统一表示中增量更新运动、几何和对象身份。
- **Baseline** · 已有流式重建方法，具体名称待核实。
- **Benchmark** · 三维重建、位姿、空间实例追踪、开放词汇分割；InsScene4D-147K。
- **关键结果 / 消融** · 摘要报告多项优于既有流式方法，长动态序列可在线推理。
- **适用条件 / 局限** · 依赖跨时间一致的实例监督；极长序列开销待核实。

**可复用机制** · 让对象身份成为在线场景图的持久状态，避免在独立语义管线中逐帧重建关联。

<a id="paper-151662"></a>

## I Have a Stream: Making Self-Supervised Learning Work on Continuous Video

[官方论文页](https://neurips.cc/virtual/2026/poster/151662) · [作者来源](https://openreview.net/forum?id=YycCzzfac3)

- **问题 / 瓶颈** · 严格视频流不允许全局重排，标准 MAE 和对比等方法退化。
- **核心创新 / 方法** · 保留 MAE 目标，加入流感知正则和运动偏置的裁剪。
- **Baseline** · 流式的对比、蒸馏及 MAE，独立采样 MAE。
- **Benchmark** · WT++ 95 小时城市视频和多项迁移评估。
- **关键结果 / 消融** · 批内重复是主要障碍；StreamMAE 匹配所比独立采样 MAE。
- **适用条件 / 局限** · 结果基于连续城市视频及选定窗口协议。

**可复用机制** · 不打乱到达顺序时，先用批内有效观测多样性改善学习，再调跨批更新。

<a id="paper-155681"></a>

## IIDiff: Learning Cross-Domain Frequency Transitions with Diffusion Mixture-of-Experts

[官方论文页](https://neurips.cc/virtual/2026/poster/155681) · [作者来源](https://openreview.net/forum?id=3lbpq6bC01)

- **问题 / 瓶颈** · 固定频率专家不适配各域和各时步的频率变化。
- **核心创新 / 方法** · 逐步调整专家频率感受野，并据频率噪声分布估计瞬时变化以路由。
- **Baseline** · 频率专家混合和现有跨域生成基线。
- **Benchmark** · 四域 12 个时序集，KL 和 MMD。
- **关键结果 / 消融** · 摘要报告 KL 平均改善 27.59%，MMD 改善 6.00%。
- **适用条件 / 局限** · 需要稳定的频率变化估计，对不同采样率的稳健性待核实。

**可复用机制** · 路由同时依赖当前去噪阶段和观测域的频谱变化，避免专家只按静态域标签分工。

<a id="paper-152124"></a>

## Illusory Pattern Perception Drives Spurious Inference in Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152124) · [作者来源](https://openreview.net/forum?id=VLcmdFfRQc)

- **问题 / 瓶颈** · 频率共现容易被模型解读为结构或因果。
- **核心创新 / 方法** · 把经典心理实验改成三类任务，对比人类和模型，并用稀疏自编码器分析。
- **Baseline** · 人类行为与多个语言模型。
- **Benchmark** · 三个模式错觉任务；分组关联和模糊事件解释。
- **关键结果 / 消融** · 模型往往强于人类地过度关联及编造因果；摘要指出若干内部特征相关。
- **适用条件 / 局限** · 内部特征关系不足以证明所有行为的因果机制。

**可复用机制** · 在评测中独立操纵真实依赖和边际频率，测模型是否凭频次误报关联。

<a id="paper-151849"></a>

## Image2Sim: Scaling Embodied Navigation via Generative Neural Simulator

[官方论文页](https://neurips.cc/virtual/2026/poster/151849) · [作者来源](https://openreview.net/forum?id=XQspWihxY2)

- **问题 / 瓶颈** · 扫描环境规模有限，纯合成环境可能跨域泛化不足。
- **核心创新 / 方法** · 用带位姿 RGB-D 提取三维特征高斯，再以几何条件单步像素流合成全景 RGB-D。
- **Baseline** · 扫描型和合成型环境，逐项对照待核实。
- **Benchmark** · 导航基准及零样本真实转移；论文生成近两万场景和逾千万训练样本。
- **关键结果 / 消融** · 摘要报告在主要基准改善且可迁移真实场景。
- **适用条件 / 局限** · 需要 RGB-D 与位姿质量；具体交互动力学边界待核实。

**可复用机制** · 让三维状态负责持续一致性，图像生成器只恢复感知细节，分别监督两部分。

<a id="paper-151641"></a>

## Image Generation for Automotive Lidar Open-vocabulary Semantic Segmentation

[官方论文页](https://neurips.cc/virtual/2026/poster/151641) · [作者来源](https://openreview.net/forum?id=Z5dOCGOl4Y)

- **问题 / 瓶颈** · 直接在文本空间匹配蒸馏得到的点特征存在模态差距。
- **核心创新 / 方法** · 从文本生成代表图像，用视觉骨干提图像特征，与已蒸馏的三维点特征匹配。
- **Baseline** · 依赖 CLIP 等图文匹配的方法。
- **Benchmark** · nuScenes、SemanticKITTI 零样本开放词汇分割。
- **关键结果 / 消融** · 摘要报告领先，具体分数待核实。
- **适用条件 / 局限** · 依赖合成原型代表性与二维到三维蒸馏质量。

**可复用机制** · 将类别定义投到已和目标传感器对齐的中间模态，避免直跨两个不对齐空间。

<a id="paper-151905"></a>

## Image Matting without Matting-Specific Annotations via Eikonal Fields

[官方论文页](https://neurips.cc/virtual/2026/poster/151905) · [作者来源](https://openreview.net/forum?id=X2jELwz645)

- **问题 / 瓶颈** · 抠图标注昂贵，粗二值分割不能表达软边界。
- **核心创新 / 方法** · 以粗前景作源，解基于图像与先验的 Eikonal 方程，转到达时间为置信加权监督。
- **Baseline** · 任务专用监督抠图方法。
- **Benchmark** · 20 项数据集指标组合；具体集合待核实。
- **关键结果 / 消融** · 13 项排名前二。
- **适用条件 / 局限** · 对粗前景和边界信号质量敏感。

**可复用机制** · 从可靠区域传播可达证据，并把不确定过渡带留为低置信监督。

<a id="paper-140042"></a>

## ImageNet FID is a Pass Check, Not a Finish Line

[官方论文页](https://neurips.cc/virtual/2026/poster/140042) · [作者来源](https://openreview.net/forum?id=cRKDUddr0V)

- **问题 / 瓶颈** · 接近的单一 FID 排名可能依赖评估参数。
- **核心创新 / 方法** · 固定每个生成器的输出，只改参考集、样本量和特征抽取器。
- **Baseline** · 常规 ImageNet 50K 与 Inception-v3 的 FID。
- **Benchmark** · 47 个生成器，另用 CLIP、DINOv2、VGG16 等。
- **关键结果 / 消融** · 相同输出在不同设置下得到不同排名。
- **适用条件 / 局限** · 结论集中于 ImageNet 类条件生成；不测人类偏好。

**可复用机制** · 用冻结样本排除采样变化，再以多协议交叉校验微小分数差是否稳健。

<a id="paper-149868"></a>

## Imagine3D-LLM: Teaching MLLMs to Imagine 3D Scenes Before Answering

[官方论文页](https://neurips.cc/virtual/2026/poster/149868) · [作者来源](https://openreview.net/forum?id=masWIidGAx)

- **问题 / 瓶颈** · 多图问题需要跨视角聚合，外部几何特征难直接体现可用结构。
- **核心创新 / 方法** · 把摘要词元解码为紧凑三维高斯表示，联合光度重建和下一个词元损失。
- **Baseline** · 跨视角像素匹配和注入外部三维几何的路线。
- **Benchmark** · 多个空间推理与三维理解基准，具体名称待核实。
- **关键结果 / 消融** · 摘要报告整体改善，重建也提高底层跨帧对应。
- **适用条件 / 局限** · 需要多视图重建监督，遮挡与少视角条件待核实。

**可复用机制** · 让结构化重建损失作用于少量潜变量，同时保留语言问题监督，检验几何是否迁移到下游。

<a id="paper-156043"></a>

## Imagine Before You Draw: Visual Prompt Engineering for Image Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/156043) · [作者来源](https://openreview.net/forum?id=0qIxwwc2xH)

- **问题 / 瓶颈** · 分离语义规划与扩散解码可能丢掉编辑所需原图细节。
- **核心创新 / 方法** · 先自回归生成语义计划词元，再在同一模型内部按计划和输入生成完整图像。
- **Baseline** · X-Omni、BLIP3o-Next 外部管线及内部生成框架。
- **Benchmark** · 类条件、文生图与编辑；保留 PSNR 和指令响应。
- **关键结果 / 消融** · 同参数规模的编辑保留 PSNR 26.76 对 19.92。
- **适用条件 / 局限** · 依赖中间词元及内部条件交互质量。

**可复用机制** · 中间计划降难度，原始输入保留细节；不要把计划作为解码器的唯一条件。

<a id="paper-150345"></a>

## Imagine, Don't Narrate: The Generative Bottleneck in World Models of Interaction Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/150345) · [作者来源](https://openreview.net/forum?id=ipFW6QeUtY)

- **问题 / 瓶颈** · 自然语言输出可能丢掉模型已表示的状态并放大延迟。
- **核心创新 / 方法** · 用可观测真实潜变量的受控测试床比较表征预测和文字输出。
- **Baseline** · 三种 117M 至 350M 的生成模型与表征预测。
- **Benchmark** · LID-Bench 的潜变量误差、时域和运行效率。
- **关键结果 / 消融** · 摘要报告到五步文字呈现损失 89% 至 100% 的信号，表征预测更快且更准。
- **适用条件 / 局限** · 合成状态和任务的外部有效性需核查。

**可复用机制** · 以内部状态读出与末端输出的分离评估定位信息瓶颈。

<a id="paper-151209"></a>

## Imitation Dominates Reinforcement: Direct In-Context RL Is Closer to ICL Than RL

[官方论文页](https://neurips.cc/virtual/2026/poster/151209) · [作者来源](https://openreview.net/forum?id=c9GSAkKpkb)

- **问题 / 瓶颈** · 随着示例积累而提升，不代表模型在用奖励推理。
- **核心创新 / 方法** · 在保留主要上下文结构时移除或置乱奖励，并对比腐化、真实轨迹。
- **Baseline** · 真实轨迹奖励对、无奖励及置乱对照。
- **Benchmark** · 三个基准、六种模型的改进曲线。
- **关键结果 / 消融** · 改变奖励效果很小，部分腐化轨迹与真实轨迹等效。
- **适用条件 / 局限** · 针对直接传入轨迹奖励的设定，不涵盖所有推理时 RL。

**可复用机制** · 先验证增益是否真的可归因于反馈，再决定优化奖励还是演示分布。

<a id="paper-151602"></a>

## Imitation from Observations with Trajectory-Level Generative Embeddings

[官方论文页](https://neurips.cc/virtual/2026/poster/151602) · [作者来源](https://openreview.net/forum?id=ZKbWAjL1zV)

- **问题 / 瓶颈** · 离线次优数据与专家差异大时，单步动作支持约束易失败。
- **核心创新 / 方法** · 在次优轨迹上训练时序扩散，用该嵌入中的粒子熵估计优化专家轨迹似然。
- **Baseline** · 既有离线仅状态模仿方法。
- **Benchmark** · D4RL 行走与操作任务。
- **关键结果 / 消融** · 摘要报告匹配或超过既有方法。
- **适用条件 / 局限** · 依赖次优数据仍可提供可迁移时序空间。

**可复用机制** · 以轨迹级几何补充逐步支持判断，降低无专家动作时对单步预测的依赖。

<a id="paper-152450"></a>

## ImmuVis: Hyperconvolutional Foundation Models for Imaging Mass Cytometry

[官方论文页](https://neurips.cc/virtual/2026/poster/152450) · [作者来源](https://openreview.net/forum?id=T2RPhW9u1M)

- **问题 / 瓶颈** · 不同研究测量的成像标记物不同，固定输入通道违反实际分布。
- **核心创新 / 方法** · 以标记物嵌入调制超卷积，再用遮罩重建训练。
- **Baseline** · Transformer 备选模型和组件消融。
- **Benchmark** · IMC17M 的虚拟染色与分类；算力和校准。
- **关键结果 / 消融** · 摘要报告优于对照且算力更低，并采用异方差似然预测不确定性。
- **适用条件 / 局限** · 任意已支持标记子集与全新标记的效果需分开验证。

**可复用机制** · 让输入特征的语义身份决定卷积接口，使多个传感通道组合共享同个模型。

<a id="paper-149015"></a>

## Impacts of Aggregation on Model Diversity and Consumer Utility

[官方论文页](https://neurips.cc/virtual/2026/poster/149015) · [作者来源](https://openreview.net/forum?id=tTHBShRcR3)

- **问题 / 瓶颈** · 普通胜率可能奖励模型相互同质化，降低路由收益。
- **核心创新 / 方法** · 在有噪声的模型选择环境理论分析胜率，并用答案质量加权。
- **Baseline** · 普通胜率与无差异模型选择。
- **Benchmark** · 理论模型与基准数据分析；专门化及消费者效用。
- **关键结果 / 消融** · 加权胜率在论文条件下鼓励专门化并改善效用。
- **适用条件 / 局限** · 依赖质量权重与路由噪声的设定。

**可复用机制** · 评价被组合的组件时计入其擅长子域的质量幅度，避免只按总体排名激励。

<a id="paper-153488"></a>

## Imperfect Influence, Reliable Rankings: A Theory of TRAK for Data Attribution

[官方论文页](https://neurips.cc/virtual/2026/poster/153488) · [作者来源](https://openreview.net/forum?id=L0YFMm2CYO)

- **问题 / 瓶颈** · 核近似和留一风险近似的误差边界不清楚。
- **核心创新 / 方法** · 逐层分析 TRAK 近似引入的影响量误差及排序后果。
- **Baseline** · 留一风险及 TRAK 的近似组成。
- **Benchmark** · 模拟和实证归因；影响值及高低影响组的分离。
- **关键结果 / 消融** · 数值近似可有显著偏差，高低影响组仍能区分。
- **适用条件 / 局限** · 不能由组间分离推出细粒度相邻排名完全可靠。

**可复用机制** · 按用途检验归因稳定性，候选过滤与精确权重归因要用不同容错标准。

<a id="paper-154874"></a>

## Imperfect World Models are Exploitable

[官方论文页](https://neurips.cc/virtual/2026/poster/154874) · [作者来源](https://openreview.net/forum?id=AFrqAcX9ti)

- **问题 / 瓶颈** · 不完美世界模型可能颠倒真实环境中的策略优劣。
- **核心创新 / 方法** · 以策略相对偏好反转定义误导，分析大策略集并为放松判据导出安全时域。
- **Baseline** · 既有奖励投机的形式刻画。
- **Benchmark** · 理论分析策略集合与规划时域，无具体实验指标。
- **关键结果 / 消融** · 理论指出误导在大策略集几乎不可避免，放松版本可界定一定安全时域。
- **适用条件 / 局限** · 时域保证针对放松定义及给定形式条件。

**可复用机制** · 验证世界模型时检查策略排序的一致性，限制搜索远期真实价值难校准的轨迹。

<a id="paper-150321"></a>

## Implicit Bias in State Space Models and Linear Autoregressive Training

[官方论文页](https://neurips.cc/virtual/2026/poster/150321) · [作者来源](https://openreview.net/forum?id=iz9ERtKfxJ)

- **问题 / 瓶颈** · 共享参数被重复使用，各例的有效预测阶数不同。
- **核心创新 / 方法** · 将例子建模为共享参数的非齐次多项式预测器，并刻画有效阶最大间隔。
- **Baseline** · 齐次模型的隐式偏置理论。
- **Benchmark** · 线性状态空间和自回归训练的理论分析。
- **关键结果 / 消融** · 最小有效阶示例施加渐近硬边际约束，其他示例可能仅约束可行性。
- **适用条件 / 局限** · 依赖插值、方向收敛及有效阶条件。

**可复用机制** · 增加序列长度未必增加该样本影响力，按轨迹诱导的有效阶而非样本数诊断长度偏置。

<a id="paper-149406"></a>

## Implicit Bias of Mirror Flow in Homogeneous Neural Networks: Sparse and Dense Feature Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149406) · [作者来源](https://openreview.net/forum?id=qIshuUKij9)

- **问题 / 瓶颈** · 梯度流的极限间隔结果不足以刻画一般镜像流的动力学。
- **核心创新 / 方法** · 从凸对偶导出平衡关系，刻画支配间隔的渐近函数并分析速率和范数增长。
- **Baseline** · 经典梯度流与不同非齐次镜像映射。
- **Benchmark** · 合成数据及标准视觉任务，比较最大间隔、收敛及激活密度。
- **关键结果 / 消融** · 不同映射可通向同一最大间隔但激活稀疏性不同；存在很慢的收敛区间。
- **适用条件 / 局限** · 结论建立于齐次激活等条件，实测任务与速率细节待核实。

**可复用机制** · 终点指标相同也应比较表示形态和训练预算，避免过早截断得出隐式偏置结论。

<a id="paper-153972"></a>

## Implicit Drifting Policy: One-Step Action Generation via Conditional Expert Geometry

[官方论文页](https://neurips.cc/virtual/2026/poster/153972) · [作者来源](https://openreview.net/forum?id=H7VRIbdX6F)

- **问题 / 瓶颈** · 迭代采样有延迟，条件下示范稀疏使显式漂移估计病态。
- **核心创新 / 方法** · 比较观测近邻的专家动作几何与全局参照，自适应加权标量势，并检查终点是否靠近专家。
- **Baseline** · 显式漂移与现有一步生成基线。
- **Benchmark** · 二维、三维和真实操作任务，考察动作流形有效性与策略表现。
- **关键结果 / 消融** · 报告优于显式漂移，与强一步基线表现有竞争力。
- **适用条件 / 局限** · 观测近邻的质量及多模态动作覆盖限制待核实。

**可复用机制** · 以局部动作分布和全局参照的差异给一步策略提供隐式纠正信号。

<a id="paper-151746"></a>

## Implicit-Euler Value Iteration: Long-Horizon Planning via Stable Integration of the Bellman Residual Flow

[官方论文页](https://neurips.cc/virtual/2026/poster/151746) · [作者来源](https://openreview.net/forum?id=YPZmHZA1Ut)

- **问题 / 瓶颈** · 显式 Euler 解释揭示长有效时域下的步幅限制。
- **核心创新 / 方法** · 以隐式 Euler 离散 Bellman 残差流，在近似模型内规划并周期性查询真模型更新缺陷项。
- **Baseline** · 普通价值迭代及仅在近似模型上规划。
- **Benchmark** · 策略评估与控制的收缩率和迭代复杂度，另给表格 Dyna 变体。
- **关键结果 / 消融** · 任意正步幅收缩，每步因子为 1/(1+h(1−γ))；模型误差满足缩放条件时复杂度为有效时域的多对数。
- **适用条件 / 局限** · 真实 Bellman 查询或其采样替代是必要条件；大规模函数逼近需另验。

**可复用机制** · 把近似模型用作求解加速器，并让真残差决定最终固定点。

<a id="paper-154628"></a>

## Implicit Goal Conditioning via Value Disaggregation

[官方论文页](https://neurips.cc/virtual/2026/poster/154628) · [作者来源](https://openreview.net/forum?id=CB1gJdJWSh)

- **问题 / 瓶颈** · 串行子目标方法依赖测试时选择，也难覆盖非序列目标。
- **核心创新 / 方法** · 以各子目标价值的线性组合训练一个不随子目标改变的策略。
- **Baseline** · 子目标条件策略及自然对照；具名实现待核实。
- **Benchmark** · 长时域 RoboCasa、非序列目标和多目标任务，比较成功率。
- **关键结果 / 消融** · 作者报告持平或超过常见基线，并从成功率近零的行为克隆初始化解决困难任务。
- **适用条件 / 局限** · 价值组合权重、泛化和切换约束待核实。

**可复用机制** · 将子目标用于改善 critic 学习，独立检验策略端是否还需要子目标输入。

<a id="paper-156079"></a>

## Importance-Weighted Operator Learning Under Probability Measure Shifts

[官方论文页](https://neurips.cc/virtual/2026/poster/156079) · [作者来源](https://openreview.net/forum?id=0afkWPjBeM)

- **问题 / 瓶颈** · 通常重要权重依赖绝对连续，且可能无界。
- **核心创新 / 方法** · 从训练测试混合取得相对权重，用以函数为输入的核积分分类器估计。
- **Baseline** · 标准算子训练和绝对连续下的精确重要加权。
- **Benchmark** · 多种 PDE 基准与神经算子架构，测试分布偏移下误差。
- **关键结果 / 消融** · 报告偏移下提升；绝对连续下给出精确目标等式，相对权重则保持有界。
- **适用条件 / 局限** · 相对重权对应调整后的目标；实际依赖测试分布样本和估计质量。

**可复用机制** · 分别报告权重尾部、离散分辨率迁移和偏移下误差，以选平滑强度。

<a id="paper-149451"></a>

## Impossibility of Distribution-Free Predictive Inference for Individual Treatment Effects

[官方论文页](https://neurips.cc/virtual/2026/poster/149451) · [作者来源](https://openreview.net/forum?id=pyIv9zfcdd)

- **问题 / 瓶颈** · 标准可忽略性与重叠不足以辨识可预测的个体反事实差。
- **核心创新 / 方法** · 将覆盖问题连接到条件独立检验的难度，给出有限样本及渐近不可能性。
- **Baseline** · 仅依赖标准因果假设的分布无关覆盖目标。
- **Benchmark** · 连续协变量个体效应，指标为覆盖和期望区间长度。
- **关键结果 / 消融** · 要求分布无关覆盖的区间必须具有无限期望长度。
- **适用条件 / 局限** · 结论限于相应假设、目标及连续协变量，附加结构下可另行评估。

**可复用机制** · 在声称覆盖前，写明额外识别条件并把有限区间长度作为同时验收的标准。

<a id="paper-149740"></a>

## Improved Baselines with Representation Autoencoders

[官方论文页](https://neurips.cc/virtual/2026/poster/149740) · [作者来源](https://openreview.net/forum?id=nikMBZQUOk)

- **问题 / 瓶颈** · 编码器末层难保留重建细节，基线还可能需要训练第二个引导模型。
- **核心创新 / 方法** · 汇总冻结编码器末 k 层，用同一表示作为中层对齐目标，并重参数化 DiT 输出得到引导。
- **Baseline** · 原始 RAE、REPA 与 AutoGuidance。
- **Benchmark** · ImageNet-256 及文生图、导航世界模型；gFID、FDr 指标与达成指定 gFID 的轮数。
- **关键结果 / 消融** · 80 轮取得 gFID 1.06，达到无引导 gFID 2 用 35 轮，原 RAE 为 177 轮。
- **适用条件 / 局限** · 各改动的跨骨干收益及对齐系数待核实。

**可复用机制** · 把编码表征的重建能力与去噪器的中层监督分开消融，同一特征可能承担两种互补角色。

<a id="paper-155618"></a>

## Improved Leverage Score Sampling for Constrained Active Linear Regression

[官方论文页](https://neurips.cc/virtual/2026/poster/155618) · [作者来源](https://openreview.net/forum?id=4DVNqdoLKl)

- **问题 / 瓶颈** · 常规杠杆分数忽略约束或只用各向同性岭正则，浪费标签。
- **核心创新 / 方法** · 用外接椭球近似可行域，并以其形状矩阵构造椭球正则杠杆分数。
- **Baseline** · 标准和岭正则杠杆分数采样。
- **Benchmark** · 约束线性回归，测达到 1+ε 相对误差的响应查询量。
- **关键结果 / 消融** · 给出按各向异性有效维数缩放的复杂度，凸约束下改善 ε 依赖，并证明对应下界。
- **适用条件 / 局限** · 依赖已知设计矩阵和可计算的外椭球，非线性回归尚待核实。

**可复用机制** · 让标签预算偏向约束允许变化的方向，并以有效维数估计其潜在节省。

<a id="paper-148144"></a>

## Improved Robust Verifiable Federated Learning Based on Packed Secret Sharing

[官方论文页](https://neurips.cc/virtual/2026/poster/148144) · [作者来源](https://openreview.net/forum?id=zvSw7s379j)

- **问题 / 瓶颈** · 单个更新不可见，使验证稳健聚合规则变得困难。
- **核心创新 / 方法** · 重新设计打包秘密共享的降阶与点积验证，简化余弦相似度校验。
- **Baseline** · RFLPA、FLTrust 及 BGW 类计算。
- **Benchmark** · 高维联邦模型更新，关注协议正确性、通信轮次及恶意参与方鲁棒性。
- **关键结果 / 消融** · 作者报告减少通信轮次并保留 N/3 鲁棒性，支持高维更新的可行性。
- **适用条件 / 局限** · 依赖威胁模型及秘密共享设置，严格参数待核实。

**可复用机制** · 同时验证共享运算的正确性和剩余鲁棒界，再判断单个验证原语的通信优化是否有效。

<a id="paper-152218"></a>

## Improved State Mixing in Higher-order and Block Diagonal Linear Recurrent Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/152218) · [作者来源](https://openreview.net/forum?id=UgQaUtjeXS)

- **问题 / 瓶颈** · 对角状态转移限制表达，密集循环计算成本高。
- **核心创新 / 方法** · 以高阶循环混合历史状态，或以块对角转移混合组内通道，并配合门控归一化和平行扫描。
- **Baseline** · 对角线性循环与线性状态空间模型。
- **Benchmark** · 合成序列与语言建模，比较预测效果、状态混合及吞吐。
- **关键结果 / 消融** · 作者报告结构混合改善效果，中等阶数或块尺寸保持有竞争力的吞吐。
- **适用条件 / 局限** · 大阶数或大块时的扫描成本、稳定性及硬件适用性待查。

**可复用机制** · 把时间轴和通道轴混合作为两个结构选项，依任务需求与吞吐分别消融。

<a id="paper-154921"></a>

## Improved techniques for fine-tuning flow models via adjoint matching: a deterministic control pipeline

[官方论文页](https://neurips.cc/virtual/2026/poster/154921) · [作者来源](https://openreview.net/forum?id=9ye0wbdavj)

- **问题 / 瓶颈** · 完整轨迹伴随计算成本高，奖励相关信号可能集中在末段。
- **核心创新 / 方法** · 把速度场控制回归到值梯度诱导目标，截取终端段计算，并允许灵活正则。
- **Baseline** · 完整伴随匹配及标准 KL 正则，具名对照待核实。
- **Benchmark** · SiT-XL/2、FLUX.2-Klein-4B，比较偏好对齐、多样性及模式保持。
- **关键结果 / 消融** · 报告截断节省计算且保持质量，对齐指标和多样性改善。
- **适用条件 / 局限** · 末段信号集中是所提设计的关键，早期高影响的任务需重验。

**可复用机制** · 在选择伴随预算前先比较沿轨迹的信号价值，并对齐成本后检查模式丢失。

<a id="paper-148140"></a>

## Improving Audit Realism with Inference-Time Compute and Deployment Scaffolds

[官方论文页](https://neurips.cc/virtual/2026/poster/148140) · [作者来源](https://openreview.net/forum?id=zzlztyx1yj)

- **问题 / 瓶颈** · 目标模型能识别被评测，可能让审计结果低估部署风险。
- **核心创新 / 方法** · 比较不同审计环境与实际部署记录，由独立评估判断真实感和评测意识。
- **Baseline** · Petri 默认审计配置及不同部署环境参考。
- **Benchmark** · Sonnet-4.6、Haiku-4.5、Opus-4.7，比较真实感胜率与自述评测意识。
- **关键结果 / 消融** · 代码场景下改变环境后 Sonnet-4.6 真实感胜率由 7% 到 18%，跨模型并非同样叠加。
- **适用条件 / 局限** · 真实感和自述是代理指标，不能替代部署风险验证。

**可复用机制** · 在将审计结果用于上线决定前，测部署与审计两类记录的可区分性。

<a id="paper-153775"></a>

## Improving Causal Explanations

[官方论文页](https://neurips.cc/virtual/2026/poster/153775) · [作者来源](https://openreview.net/forum?id=IkOHPX9dDS)

- **问题 / 瓶颈** · 不同归因方法可给出冲突解释。
- **核心创新 / 方法** · 定义四个要求，从自然总效应聚合反事实 Shapley 值并求紧界。
- **Baseline** · SHAP、LIME 和其他已有归因方法。
- **Benchmark** · 理论证明与实验佐证；数据和指标待核。
- **关键结果 / 消融** · 证明无因果假设时四个要求不能同时满足，新归因在条件下满足四项。
- **适用条件 / 局限** · 依赖可辩护的因果条件；区间宽时不能直接排序。

**可复用机制** · 出具归因时并列因果假设和区间，用敏感性分析甄别可稳定解释的变量。

<a id="paper-149052"></a>

## Improving Conditional Modeling via Inter-Class Likelihood-Ratio Maximization and Unifying Classifier-Free Guidance with Alignment Objectives

[官方论文页](https://neurips.cc/virtual/2026/poster/149052) · [作者来源](https://openreview.net/forum?id=tDqT2QD3Da)

- **问题 / 瓶颈** · 普通去噪分数匹配的类间区分不足。
- **核心创新 / 方法** · 微调时最大化类间似然比；推导 CFG 分数等价于样本自适应加权目标的最优解。
- **Baseline** · 普通 DSM 与推理期 CFG。
- **Benchmark** · 条件生成和无引导采样；具体数据及指标待核。
- **关键结果 / 消融** · 摘要称无引导质量明显改善，与 CFG 质量差距缩小。
- **适用条件 / 局限** · 受目标和模型分布条件限制，类别外迁移待核。

**可复用机制** · 同采样预算比较训练期分离目标与推理期引导，分别看质量和条件一致性。

<a id="paper-150565"></a>

## Improving Consistency in Retrieval Augmented Systems  With Group Similarity Rewards

[官方论文页](https://neurips.cc/virtual/2026/poster/150565) · [作者来源](https://openreview.net/forum?id=hCpmScyCoy)

- **问题 / 瓶颈** · 同义问题可能取回不同证据，生成结果反复变化。
- **核心创新 / 方法** · PS-GRPO 对改写组采样，以答案相似性给组奖励，并以近似降低配对成本。
- **Baseline** · 强检索增强和生成训练基线；名称待核。
- **Benchmark** · 短答、多跳、长答，分别测检索、生成和端到端一致性及准确性。
- **关键结果 / 消融** · 摘要称无需显式标准答案即可改善一致性和准确性。
- **适用条件 / 局限** · 相似性可能奖励一致的错误；需外部准确度与检索证据对照。

**可复用机制** · 改写输入、固定检索和变动检索分开测试，明确一致性问题来自哪一层。

<a id="paper-151902"></a>

## Improving constraint-based discovery with robust propagation and LLM priors

[官方论文页](https://neurips.cc/virtual/2026/poster/151902) · [作者来源](https://openreview.net/forum?id=X5adrFr97k)

- **问题 / 瓶颈** · 独立性检验误差会从初始碰撞结构传播，语言模型也会不稳定。
- **核心创新 / 方法** · 融合条件独立证据与语言先验建立高置信定向，再用 SPR 传播。
- **Baseline** · PC 及已有混合因果发现方法。
- **Benchmark** · 13 个真实基准，测结构准确性；另有理论可靠性条件。
- **关键结果 / 消融** · 摘要报告定向更准，给出理想检验下传播的正确性。
- **适用条件 / 局限** · 取决于骨架、分隔集合和种子质量；需检验错误先验影响。

**可复用机制** · 分别污染种子与分隔集合，比较碰撞优先和可信种子传播的级联误差。

<a id="paper-150848"></a>

## Improving Context-Shift Robustness of Convolutional Networks via Context-Regularized Cross-Entropy

[官方论文页](https://neurips.cc/virtual/2026/poster/150848) · [作者来源](https://openreview.net/forum?id=eu0NxAFRN2)

- **问题 / 瓶颈** · 模型利用非因果上下文，换背景即失准。
- **核心创新 / 方法** · 先用 ContrastiveCAMs 产生空间归因，再用 CR-CE 抑制上下文区域影响。
- **Baseline** · 普通交叉熵及已有空间归因途径。
- **Benchmark** · Waterbirds、Spawrious、ImageNet 与 ImageNet-BG、Hard-ImageNet。
- **关键结果 / 消融** · 摘要报告跨基准上下文偏移鲁棒性改善。
- **适用条件 / 局限** · 依赖能区分主体与上下文；部分任务上下文本身是有效信号。

**可复用机制** · 测主体、背景分别替换后的性能，并用等信息主体监督比较惩罚效果。

<a id="paper-151348"></a>

## Improving Diffusion Posterior Samplers with Lagged Temporal Corrections for Image Restoration

[官方论文页](https://neurips.cc/virtual/2026/poster/151348) · [作者来源](https://openreview.net/forum?id=bCS5vqUUqK)

- **问题 / 瓶颈** · 瞬时的数据一致估计波动会传到反向动态。
- **核心创新 / 方法** · 在后验采样残差框架下以二阶方式加入滞后时间修正。
- **Baseline** · DiffPIR、DDRM。
- **Benchmark** · 多个成像恢复任务，比较质量和去噪调用数；另做单步偏差方差分析。
- **关键结果 / 消融** · 无额外去噪调用而改善恢复。
- **适用条件 / 局限** · 收益依赖跨步估计误差结构，极稀疏采样或严重噪声待核。

**可复用机制** · 在等去噪调用下比较一阶与滞后二阶修正，监控反向步估计的抖动。

<a id="paper-149748"></a>

## Improving Flexible Image Tokenizers for Autoregressive Image Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/149748) · [作者来源](https://openreview.net/forum?id=neJJASNqpr)

- **问题 / 瓶颈** · 嵌套尾部截断让早期词元信息过度集中，增加采样长度边际收益小。
- **核心创新 / 方法** · 冗余填充提高尾词元使用频率，视觉语义对齐从前到后逐渐减弱。
- **Baseline** · 固定长度和传统灵活词元器。
- **Benchmark** · ImageNet 256×256 自回归生成，具体指标待核。
- **关键结果 / 消融** · 摘要报告超越两类词元器。
- **适用条件 / 局限** · 其他分辨率、词元开销与两部分的独立收益待核。

**可复用机制** · 画随前缀长度增加的重建与生成曲线，检查尾端是否真正带来细节收益。

<a id="paper-152774"></a>

## Improving Function Space Flow Matching with Kernel Optimal Transport

[官方论文页](https://neurips.cc/virtual/2026/poster/152774) · [作者来源](https://openreview.net/forum?id=QT7iczCUkm)

- **问题 / 瓶颈** · 独立配对让桥接同时承担共性结构和实例残差，平坦欧式代价忽略路径几何。
- **核心创新 / 方法** · 保留神经算子骨干，以核希尔伯特空间的熵正则最优传输替换独立配对。
- **Baseline** · FFM、扩散、对抗模型和有限维 OT。
- **Benchmark** · 时间序列和 PDE 分布生成，MMD-RBF；另有目标良定性和网格截断理论。
- **关键结果 / 消融** · 摘要报告一致改善，函数几何核在 PDE 和路径数据上最好。
- **适用条件 / 局限** · 依赖核选择与数据正则性，训练时批内传输开销待核。

**可复用机制** · 固定网络与步数扫独立、欧式和函数核配对，报告分辨率变化下的稳定性。

<a id="paper-154485"></a>

## Improving General Role-Playing Agents via Psychology-Grounded Reasoning and Role-Aware Policy Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/154485) · [作者来源](https://openreview.net/forum?id=DF7xRhiXvd)

- **问题 / 瓶颈** · 角色特异表达与通用高分语句可能获得相同更新。
- **核心创新 / 方法** · RAPO 用角色描述与词元互信息在正负优势下非对称调权；另测试结构化角色推理。
- **Baseline** · GRPO 和既有角色推理。
- **Benchmark** · CoSER、CharacterBench、CharacterEval，多个模型规模。
- **关键结果 / 消融** · 摘要称角色推理优于已有提示路线，RAPO 一致优于 GRPO。
- **适用条件 / 局限** · 互信息代理可能放大词面角色线索，跨表述和通用能力待核。

**可复用机制** · 对角色或其他条件生成，用语义等效改写验证特异词权重是否学到条件本身。

<a id="paper-151051"></a>

## Improving Generative Adversarial Networks with Self-Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/151051) · [作者来源](https://openreview.net/forum?id=dM03KyhkmA)

- **问题 / 瓶颈** · 标准 GAN 周期振荡，EMA 的优势只在部署时使用。
- **核心创新 / 方法** · 用感知损失将当前生成器向 EMA 生成器蒸馏，在简化博弈分析稳定性。
- **Baseline** · 常规 GAN 与仅推理使用 EMA。
- **Benchmark** · 多架构、数据和预训练微调，测 FID、random-FID 与优化轨迹。
- **关键结果 / 消融** · 证明 Dirac-GAN 局部稳定并减弱循环，实证提升生成质量。
- **适用条件 / 局限** · 局部理论不能必然外推深层 GAN，额外教师代价待核。

**可复用机制** · 在原 GAN 保持相同 EMA 更新，分别比较部署使用与训练期间教师的边际收益。

<a id="paper-152467"></a>

## Improving Guidance-Free Visual Generation via Self-Contrastive Alignment for Likelihood Estimation

[官方论文页](https://neurips.cc/virtual/2026/poster/152467) · [作者来源](https://openreview.net/forum?id=SsWOUYStqy)

- **问题 / 瓶颈** · 模仿 CFG 的单前向方法继承教师上限。
- **核心创新 / 方法** · 将模型自身在真实和生成样本上的对比信号重参数化纳入似然训练。
- **Baseline** · 模仿 CFG 的无引导方法，另对照结合 DPO。
- **Benchmark** · 扩散及自回归的类条件和文本到图像生成，质量与单次前向。
- **关键结果 / 消融** · 摘要称优于模仿 CFG 方法，与 DPO 有互补收益。
- **适用条件 / 局限** · 依赖自生成样本的代表性，定量质量和训练成本待核。

**可复用机制** · 对比蒸馏手工引导与直接拟合真实生成差异，并匹配推理预算。

<a id="paper-150649"></a>

## Improving LLM Final Representations with Inter-Layer Geometry

[官方论文页](https://neurips.cc/virtual/2026/poster/150649) · [作者来源](https://openreview.net/forum?id=gUPzBRGNCS)

- **问题 / 瓶颈** · 最后层可能漏信号，全层注意聚合又较贵。
- **核心创新 / 方法** · 把各层作为图节点，以稀疏规则 Cayley 图代替全连接图做聚合。
- **Baseline** · 仅最后层、择层、注意聚合、全连接图与 LoRA。
- **Benchmark** · 13 项任务、9 个模型及少样本，测预测与参数量。
- **关键结果 / 消融** · 准确率最高提升 40 个百分点，额外参数至多 0.1%。
- **适用条件 / 局限** · 需要访问中间层，具体任务增益和运行成本待核。

**可复用机制** · 在冻结骨干下同参数比较稀疏图、全连接图与末层，并消融图直径。

<a id="paper-148845"></a>

## Improving Neural Processes in the Low-Data Regime via Context-Subset Training and Self-Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/148845) · [作者来源](https://openreview.net/forum?id=uieGKHJk47)

- **问题 / 瓶颈** · 神经过程少任务训练会记忆任务，且子集预测不稳。
- **核心创新 / 方法** · 随机子集监督加教师全上下文分布前向 KL，网络结构与推理保持。
- **Baseline** · 普通神经过程，有无子集训练与蒸馏。
- **Benchmark** · 多种神经过程和预测任务，重点少元数据。
- **关键结果 / 消融** · 摘要报告更稳健且泛化更好；校准教师条件下不改渐近目标。
- **适用条件 / 局限** · 教师需校准，子集采法和跨任务偏移待核。

**可复用机制** · 对比同任务全信息教师与等上下文教师，测缩减上下文下的校准和误差。

<a id="paper-155969"></a>

## Improving Quantized Zeroth-Order Optimization through Reconstructed Low-Rank Structures

[官方论文页](https://neurips.cc/virtual/2026/poster/155969) · [作者来源](https://openreview.net/forum?id=1UKJD5PlWg)

- **问题 / 瓶颈** · 低比特抹去更新结构，零阶估计在量化时更不稳。
- **核心创新 / 方法** · 结构化矩阵分解扰动，采用二值聚合高斯方案控高阶矩，并重整量化尺度组。
- **Baseline** · 量化与全精度零阶方法。
- **Benchmark** · 多种 LLM 位宽含 INT2，另验证视觉 Transformer。
- **关键结果 / 消融** · 平均提升 2.0%–3.3%，给出收敛保证并缩小超低位宽差距。
- **适用条件 / 局限** · 低秩假设、量化设置和内存实际开销待核。

**可复用机制** · 以等内存与函数评估次数比较低秩和常规扰动，拆开位宽与梯度估计方差。

<a id="paper-151171"></a>

## Improving Self-Supervised Vision Transformers with Cross Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/151171) · [作者来源](https://openreview.net/forum?id=cSTY1Titxd)

- **问题 / 瓶颈** · CLS 注意力使全局语义梯度集中，低注意区域易产生密集预测错误。
- **核心创新 / 方法** · 对遮盖补丁目标混入少量教师 CLS 分布，维持骨干结构。
- **Baseline** · 标准补丁自蒸馏及全局图像预训练。
- **Benchmark** · 对齐的预训练设置，比较密集和图像级任务。
- **关键结果 / 消融** · 摘要报告两类任务均改善，梯度分析给出注意权重解释。
- **适用条件 / 局限** · 过多全局监督可能淡化局部信息，混合强度待核。

**可复用机制** · 按原 CLS 注意量分桶评估密集预测，检查收益是否集中于低注意区。

<a id="paper-150734"></a>

## Improving the Diffusability of Motion Tokenizer

[官方论文页](https://neurips.cc/virtual/2026/poster/150734) · [作者来源](https://openreview.net/forum?id=fnQkgTUCzX)

- **问题 / 瓶颈** · 提高重建容量未必带来生成收益，潜空间可能偏高频。
- **核心创新 / 方法** · 用预训练扩散作为评审抑制过高潜高频，通过平均速度预测做一步生成解码。
- **Baseline** · 现有动作 VAE 词元器及文本到动作扩散。
- **Benchmark** · 多种文本到动作评测，比较动作保真和文本对齐。
- **关键结果 / 消融** · 摘要称两类指标优于既有方法，未给定量。
- **适用条件 / 局限** · 高频也可承载真实快速动作，抑制强度和解码伪影需核。

**可复用机制** · 联合画潜频谱、重建、生成保真的关系，区分压高频与毁细节。

<a id="paper-149121"></a>

## Improving the Efficiency of Language Agent Teams with Adaptive Task Graphs

[官方论文页](https://neurips.cc/virtual/2026/poster/149121) · [作者来源](https://openreview.net/forum?id=sjSjyEGmnu)

- **问题 / 瓶颈** · 固定分工难适应新子任务，自由协作容易重复和冲突。
- **核心创新 / 方法** · 让团队共享子任务依赖、责任与进度，可随证据调整任务图。
- **Baseline** · MetaGPT、去中心化、领导者与执行者、静态分解。
- **Benchmark** · 多类协作和多种基础模型，对照准确率、用时、词元与冲突。
- **关键结果 / 消融** · 摘要称协调失败及开销减少，准确率相当或更好。
- **适用条件 / 局限** · 共享状态一致性成本和跨更长任务的可扩展性待核。

**可复用机制** · 固定模型和预算，在良性文件整理或分析中比较静态与动态任务依赖维护。

<a id="paper-151753"></a>

## Improving the Optimization Landscape of Matrix Completion with $\epsilon$-close Surrogates

[官方论文页](https://neurips.cc/virtual/2026/poster/151753) · [作者来源](https://openreview.net/forum?id=YJGa7iqmAu)

- **问题 / 瓶颈** · 部分观测的非凸优化可能缺乏合适等距条件。
- **核心创新 / 方法** · 向观测掩码零空间加 ε 级扰动，构造有受限等距性质的矩阵感知代理。
- **Baseline** · 原非凸矩阵补全和经典矩阵感知设定。
- **Benchmark** · 独立观测假设下的理论恢复分析，无摘要实证。
- **关键结果 / 消融** · 代理解与真值相距 O(ε)，并推导不显式要求采样率或不相干性的恢复保证。
- **适用条件 / 局限** · 依赖独立观测与代理结构；真实缺失机制和数值表现待核。

**可复用机制** · 选代理目标时同时约束观测保持与解偏差，并比较扰动大小对优化和误差的影响。

<a id="paper-154661"></a>

## IMTS-Tokenizer: Time-Aware Tokenization for Irregular Multivariate Time Series Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/154661) · [作者来源](https://openreview.net/forum?id=ByB7qk2CMI)

- **问题 / 瓶颈** · 异步、稀疏观测在常规聚合中易丢时间关系。
- **核心创新 / 方法** · 用可学习时间锚点和高斯核注意力聚合，并在聚合前编码相对时间。
- **Baseline** · 已有不规则预测方法，名称待核实。
- **Benchmark** · 四项不规则时序基准，八项指标。
- **关键结果 / 消融** · 七项最佳，摘要报告总体显著。
- **适用条件 / 局限** · 锚点初始化与观测稀疏程度的适配需验证。

**可复用机制** · 用连续时间核聚合到少量锚点，让分词过程保留近邻强度。

<a id="paper-150515"></a>

## IncAgg: Efficient Memory-Enhanced Graph Learning via Incremental Aggregation

[官方论文页](https://neurips.cc/virtual/2026/poster/150515) · [作者来源](https://openreview.net/forum?id=hX0lLa5bcj)

- **问题 / 瓶颈** · 历史嵌入缓存仍需逐批取回大量批外数据。
- **核心创新 / 方法** · 按周期预聚合全局历史嵌入，每批仅传播当前残差后融合。
- **Baseline** · 强历史记忆增强 GNN 基线。
- **Benchmark** · 四个大图和四种骨干；准确率与训练加速。
- **关键结果 / 消融** · 精度匹配或改善，最高单设置 18.6 倍加速。
- **适用条件 / 局限** · 刷新频率决定内存开销和陈旧偏差。

**可复用机制** · 将可跨批复用的慢变化聚合与需要梯度的局部增量分开。

<a id="paper-149120"></a>

## Incentivizing Agentic Retrieval for Disease-Centric Clinical Case Search via Trajectory Memory

[官方论文页](https://neurips.cc/virtual/2026/poster/149120) · [作者来源](https://openreview.net/forum?id=sjtN3Mjrl6)

- **问题 / 瓶颈** · 临床病例查询字段经常缺失，扁平匹配无法按情况调整。
- **核心创新 / 方法** · 把可直接匹配和需作假设的字段分开安排检索及重排，并保留已验证的搜索策略模板。
- **Baseline** · 同接口稀疏、稠密及推理检索。
- **Benchmark** · PMC-Patients、MIMIC-IV 回顾性检索及诊断遮罩的下游预测。
- **关键结果 / 消融** · 两数据集均有增益，PMC-Patients 更明显。
- **适用条件 / 局限** · 仅回顾性证据；假设补全不是临床判断。

**可复用机制** · 将证据充分度作为逐字段选择工具的依据，避免对缺失字段机械匹配。

<a id="paper-156128"></a>

## Incentivizing Medical Vision Capabilities from Large-Scale Multimodal Pre-training

[官方论文页](https://neurips.cc/virtual/2026/poster/156128) · [作者来源](https://openreview.net/forum?id=0BXKsjKlFJ)

- **问题 / 瓶颈** · 大规模医学预训练后的知识未必能通过 SFT 表现。
- **核心创新 / 方法** · 从同批语料合成可验证及有量表的任务，再做强化后训练。
- **Baseline** · 传统 SFT、同规模医学 VLM 及专有模型。
- **Benchmark** · 医学视觉基准与专家评价；预训练资料来自 PubMed。
- **关键结果 / 消融** · 摘要报告 RL 更能调用预训练知识并超越同规模对照。
- **适用条件 / 局限** · 数据重叠检查和等算力比较待核实。

**可复用机制** · 后训练设计先验证知识是否已经存在，再为必要的证据调用设计可评分任务。

<a id="paper-154755"></a>

## In-Context Benign Overfitting: A Feature-Selection Model in Linear Regression ICL

[官方论文页](https://neurips.cc/virtual/2026/poster/154755) · [作者来源](https://openreview.net/forum?id=BCHILY5fm6)

- **问题 / 瓶颈** · 训练中见过任务和新任务上的成功易被合并。
- **核心创新 / 方法** · 用线性回归特征选择模型分别分析两种能力随规模变化。
- **Baseline** · 标准上下文线性回归模型。
- **Benchmark** · 训练任务的新提示和未见任务的提示。
- **关键结果 / 消融** · 特征选择模型可让两者共同改善，标准模型存在折中。
- **适用条件 / 局限** · 证明限于简化回归模型。

**可复用机制** · 分别构造新提示和新任务，验证记忆预训练任务是否真的排挤任务泛化。

<a id="paper-154930"></a>

## In-Context Black-Box Optimization with Unreliable Feedback

[官方论文页](https://neurips.cc/virtual/2026/poster/154930) · [作者来源](https://openreview.net/forum?id=9slt6ZbEiI)

- **问题 / 瓶颈** · 专家或低成本模拟反馈可能随输入变化而有偏。
- **核心创新 / 方法** · 预训练时模拟不同反馈源的可见性、相关性和失真，推理按实际目标记录和辅助反馈联合选点。
- **Baseline** · 反馈感知贝叶斯优化与只用历史的上下文优化。
- **Benchmark** · 合成和真实黑盒任务；查询质量和误导反馈鲁棒性。
- **关键结果 / 消融** · 摘要报告能利用可靠反馈并抑制弱反馈。
- **适用条件 / 局限** · 外推依赖预训练反馈分布。

**可复用机制** · 让已验证的目标观察用于校准低成本信号，避免把来源意见当作真实观测。

<a id="paper-148820"></a>

## In-Context Learning Can Help Vision Language Models Overcome Training Prior

[官方论文页](https://neurips.cc/virtual/2026/poster/148820) · [作者来源](https://openreview.net/forum?id=utoGFkBj7z)

- **问题 / 瓶颈** · 训练先验可能盖过模型已有的视觉证据。
- **核心创新 / 方法** · 对先验一致和对立图像分别比较有无视觉演示，并诊断注意指向。
- **Baseline** · 无演示设定及五个视觉语言模型家族。
- **Benchmark** · 五种视觉任务，真实与反事实输入。
- **关键结果 / 消融** · 反事实下 Qwen3-VL 235B 提升 27.2%，真实准确率接近不变。
- **适用条件 / 局限** · 基础视觉能力不足时演示作用有限。

**可复用机制** · 在宣布模型没有某项能力前，测试受控演示能否释放已有能力。

<a id="paper-156780"></a>

## In-context Learning in Presence of Spurious Correlations

[官方论文页](https://neurips.cc/virtual/2026/poster/156780) · [作者来源](https://openreview.net/forum?id=C9CSaTR1iA)

- **问题 / 瓶颈** · 单任务的上下文元训练可退化为权重记忆且受伪特征影响。
- **核心创新 / 方法** · 比较单任务和多样合成任务分布，验证上下文依赖及跨任务泛化。
- **Baseline** · ERM、GroupDRO 和常规上下文训练。
- **Benchmark** · 含伪特征的分类，包含新任务迁移。
- **关键结果 / 消融** · 单任务方法可匹配基线但迁移弱；多任务合成训练改善新任务泛化。
- **适用条件 / 局限** · 任务分布多样性需与目标环境匹配。

**可复用机制** · 训练时让不同上下文真正改变最优预测规则，才能检验模型是否使用示例。

<a id="paper-155891"></a>

## In-context learning to predict critical transitions in dynamical systems

[官方论文页](https://neurips.cc/virtual/2026/poster/155891) · [作者来源](https://openreview.net/forum?id=24hX13I66G)

- **问题 / 瓶颈** · 相关噪声和少样本使常规方差预警与固定深度分类器失灵。
- **核心创新 / 方法** · 从典型分岔出发随机化动力学，用先验数据拟合网络从短序列判断距转变的程度。
- **Baseline** · 传统统计与谱预警及既有深分类器。
- **Benchmark** · 未见临界区间、模拟到真实、真实观测。
- **关键结果 / 消融** · 摘要报告上下文推断及零样本下均能提前检测。
- **适用条件 / 局限** · 真实世界结果依赖合成先验覆盖实际转变机制。

**可复用机制** · 用可控的机制多样性而非大量重复单一模拟，训练稀有事件预警模型。

<a id="paper-154682"></a>

## In-Context Multi-Operator Learning with DeepOSets

[官方论文页](https://neurips.cc/virtual/2026/poster/154682) · [作者来源](https://openreview.net/forum?id=Bla1smpZ8X)

- **问题 / 瓶颈** · 单算子网络即使输入相似也无法选择不同边界及动力学规则。
- **核心创新 / 方法** · 改造 DeepOSets 聚合上下文示例，给出统一多算子定义及通用逼近。
- **Baseline** · 单算子学习框架；具体实证对照待核实。
- **Benchmark** · 多种初值及边值微分方程算子。
- **关键结果 / 消融** · 摘要报告理论通用性及示范实验有效。
- **适用条件 / 局限** · 通用逼近不直接证明有限训练下的未见算子泛化。

**可复用机制** · 把用于选择运算规则的示例和要计算的查询分开输入，并使集合排序不影响选择。

<a id="paper-150330"></a>

## In-Context Optimization for Retrieval-Augmented Generation: A Gradient-Descent Perspective

[官方论文页](https://neurips.cc/virtual/2026/poster/150330) · [作者来源](https://openreview.net/forum?id=iuTd9AXKQN)

- **问题 / 瓶颈** · 静态文档使用接口不能随证据结构变化，测试时反传代价较高。
- **核心创新 / 方法** · 从线性自注意力的梯度对应启发，以前向网络预测证据接口更新，保持骨干与检索固定。
- **Baseline** · 固定共享接口、测试时梯度适配。
- **Benchmark** · 七项问答、两种检索器和两个冻结模型。
- **关键结果 / 消融** · 摘要报告优于固定接口，可迁移到留出任务并接近反传适配，成本更低。
- **适用条件 / 局限** · 非线性下线性对应需由特征分布决定。

**可复用机制** · 不改检索候选也能提升证据利用，在使用证据的低维位置预测上下文更新。

<a id="paper-153834"></a>

## Incorporating Neural Network Structure in the Bayesian Learning Rule

[官方论文页](https://neurips.cc/virtual/2026/poster/153834) · [作者来源](https://openreview.net/forum?id=IMo3RbNPJF)

- **问题 / 瓶颈** · 将整体模型平铺求变分近似使层间结构难利用。
- **核心创新 / 方法** · 借助反向传播与指数族变分推断的对偶联系，逐层传递伴随敏感度并转换成损失位点自然参数。
- **Baseline** · 标准 IVON、反向传播与 Hessian 反向传播。
- **Benchmark** · 高斯权重后验及状态投影的理论与实践；细项待核实。
- **关键结果 / 消融** · 可在近似下恢复已有传播规则，并推导新 IVON 变体。
- **适用条件 / 局限** · 取决于投影分布与 delta 方法近似的有效性。

**可复用机制** · 将贝叶斯更新的局部统计量通过层间敏感度传递，减少对整网无结构建模的依赖。

<a id="paper-150555"></a>

## Incremental Learning in Transformers for In-Context Associative Recall

[官方论文页](https://neurips.cc/virtual/2026/poster/150555) · [作者来源](https://openreview.net/forum?id=hH5NAvxmMz)

- **问题 / 瓶颈** · 最终分数无法说明多个注意电路的分阶段习得。
- **核心创新 / 方法** · 利用数据与模型对称性推导两层梯度流，并识别耦合层参数的守恒关系。
- **Baseline** · 不同初始化及注意力模型变体。
- **Benchmark** · 随机映射的合成关联回忆，观察层行为与阶段跃迁。
- **关键结果 / 消融** · 初始化控制出现时间，小初始化极限呈从鞍点到鞍点的动力学。
- **适用条件 / 局限** · 精确闭式结果限于简化注意力网络。

**可复用机制** · 记录学习阶段与层间响应而非单个终点，找出初始化导致的能力延迟。

<a id="paper-155693"></a>

## Incremental Multiple Oracle

[官方论文页](https://neurips.cc/virtual/2026/poster/155693) · [作者来源](https://openreview.net/forum?id=3eGkK2Bn1c)

- **问题 / 瓶颈** · 策略池随迭代增长，并反复求精确元博弈与全局最佳响应，开销高。
- **核心创新 / 方法** · 以固定池逐步降低元博弈可利用度，并在连续空间逐步改进候选响应。
- **Baseline** · 传统多重预言机和双预言机路线。
- **Benchmark** · 多项连续动作博弈，可利用度。
- **关键结果 / 消融** · 摘要报告固定内存下获得低可利用度近似均衡。
- **适用条件 / 局限** · 池大小和局部响应改进可能限制最终近似。

**可复用机制** · 将内层均衡精度与响应搜索都做增量更新，以可监测的可利用度约束预算。

<a id="paper-148392"></a>

## Independent Latents, Robust Neural Operators

[官方论文页](https://neurips.cc/virtual/2026/poster/148392) · [作者来源](https://openreview.net/forum?id=yBABg3BBFr)

- **问题 / 瓶颈** · 离线基正交主要服务压缩，不确保噪声下恢复可靠。
- **核心创新 / 方法** · 端到端训练时直接促进潜特征统计独立。
- **Baseline** · POD-DeepONet、PCA-Net 代表结构化基路线。
- **Benchmark** · 三个典型 PDE 任务、五种传感噪声设置。
- **关键结果 / 消融** · 摘要报告噪声重建改善并保留干净数据表现。
- **适用条件 / 局限** · 目前证据限于所测加性扰动，具体独立统计量待核实。

**可复用机制** · 使冗余潜特征的约束参与任务训练，再对干净与受扰输入分别验收。

<a id="paper-150509"></a>

## Independent Learning of Nash Equilibria in Partially Observable Markov Potential Games with Decoupled Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/150509) · [作者来源](https://openreview.net/forum?id=hZFxJatIxq)

- **问题 / 瓶颈** · 全历史策略与多参与方集中训练易造成复杂度激增。
- **核心创新 / 方法** · 在滤波稳定下用有限历史构造近似势博弈，支持只观测自身信息的学习。
- **Baseline** · 集中式或信息共享方法。
- **Benchmark** · 解耦转移的部分可观测马尔可夫势博弈；样本和计算复杂度。
- **关键结果 / 消融** · 理论达到准多项式复杂度并近似收敛到 Nash。
- **适用条件 / 局限** · 要求独立状态转移、势结构和滤波稳定。

**可复用机制** · 用可验证的历史遗忘速度选窗口，支持无通信训练而不用强行假设即时观测充分。

<a id="paper-153680"></a>

## InduceKV: Fixed-Footprint Continual Adaptation of Multimodal LLMs via Inducing KV Memories

[官方论文页](https://neurips.cc/virtual/2026/poster/153680) · [作者来源](https://openreview.net/forum?id=Jb8bv8eTGB)

- **问题 / 瓶颈** · 累积参数更新与回放存储使适配状态不断增长。
- **核心创新 / 方法** · 将训练前缀存为冻结检索键和压缩层级 KV，通过双层过程联合校准检索与选择覆盖、保留、新任务似然兼顾的记忆。
- **Baseline** · PEFT、MoE、回放和提示检索。
- **Benchmark** · 任务增量指令、持续视觉问答、域增量及终身多模态指令，含 CoIN、内存和计算匹配诊断。
- **关键结果 / 消融** · 摘要报告固定预算下持续优于对照。
- **适用条件 / 局限** · 位置兼容性以及记忆构建成本待核实。

**可复用机制** · 把部署记忆数和存储字节设置为预算，再检验直接读 KV 是否比重编码文本更合算。

<a id="paper-150230"></a>

## Inductive Deductive Synthesis: Enabling AI to Generate Formally Verified Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/150230) · [作者来源](https://openreview.net/forum?id=jp8UqwXlAw)

- **问题 / 瓶颈** · 测试覆盖不足以证明分布式系统所有交错都符合规格。
- **核心创新 / 方法** · 在同一循环中合成实现与证据，不可通过时用失败反馈改变策略，随后纳入性能反馈。
- **Baseline** · Claude Code 搭配 Opus 4.6、Codex 搭配 GPT-5.4，以及已发表的验证实现。
- **Benchmark** · 七份分布式键值存储规格，测验证通过率、时间、成本和运行性能。
- **关键结果 / 消融** · IDS 七项均成功，对照仅两项；平均每项约 6.8 小时、106 美元。
- **适用条件 / 局限** · 依赖可机读规范及证明工具，其他领域和规格编写代价待核实。

**可复用机制** · 尽早让证明义务约束实现搜索，并在正确性成立后继续优化速度。

<a id="paper-154584"></a>

## INEUS: Iterative Neural Solver for High-Dimensional PIDEs

[官方论文页](https://neurips.cc/virtual/2026/poster/154584) · [作者来源](https://openreview.net/forum?id=CUrpPtcWL3)

- **问题 / 瓶颈** · 完整 PIDE 残差求导和跳积分在高维中昂贵。
- **核心创新 / 方法** · 以单跳采样替代积分，并将全域解改写成递归回归序列。
- **Baseline** · 与基于残差的 PINN 思路比较，具名实验待核实。
- **Benchmark** · 高维线性和非线性 PDE、PIDE，指标为精度和扩展性。
- **关键结果 / 消融** · 线性情形有收缩收敛证明，数值例子展示高维应用。
- **适用条件 / 局限** · 非线性案例属于经验结果，跳分布及近似条件待核实。

**可复用机制** · 对昂贵非局部项先判断可否用条件采样生成回归目标，再比较积分与采样成本。

<a id="paper-155946"></a>

## Inexact Bregman Sparse Newton Method for Efficient Optimal Transport

[官方论文页](https://neurips.cc/virtual/2026/poster/155946) · [作者来源](https://openreview.net/forum?id=1bW1n2cWFS)

- **问题 / 瓶颈** · 高精度下熵正则会牺牲目标精度且可能数值不稳定。
- **核心创新 / 方法** · 生成半对偶子问题，用带 Hessian 稀疏化的 Newton 型法不精确求解。
- **Baseline** · 精确最优传输及熵正则方案，具名待核实。
- **Benchmark** · 最优传输速度、内存和计划精度；数据规模待核实。
- **关键结果 / 消融** · 给出全局收敛保证，摘要报告速度和精度优于对照。
- **适用条件 / 局限** · 不精确容忍度、稀疏近似条件和实际内存收益待核实。

**可复用机制** · 把近似误差限制在内层数值解而非最终目标，分别记录外层收敛和单步成本。

<a id="paper-151715"></a>

## In-Expectation Convergence of Stochastic Gradient Methods under Heavy-Tailed Noise

[官方论文页](https://neurips.cc/virtual/2026/poster/151715) · [作者来源](https://openreview.net/forum?id=Ybxgq6TUcv)

- **问题 / 瓶颈** · 二阶矩不存在常被用来预设传统更新无法收敛。
- **核心创新 / 方法** · 分析凸问题随机镜像下降及非凸问题 SGD 的期望收敛。
- **Baseline** · 已有有界域凸 SGD 分析和常规不改动算法。
- **Benchmark** · p 在 1 与 2 之间的重尾噪声，理论指标为期望收敛。
- **关键结果 / 消融** · 在没有有界域限制的所研究条件下得到期望收敛。
- **适用条件 / 局限** · 结果只针对期望；步长、光滑性及高概率保证需查正文。

**可复用机制** · 区分目标是期望收敛还是尾部风险控制，再决定有无必要引入裁剪等修改。

<a id="paper-150869"></a>

## InfCLIP: Unified Data Valuation for CLIP Pretraining via Influence-Inspired Scoring

[官方论文页](https://neurips.cc/virtual/2026/poster/150869) · [作者来源](https://openreview.net/forum?id=elAMBRgvsw)

- **问题 / 瓶颈** · 图文训练数据过滤常混用对齐、覆盖和多样性启发式。
- **核心创新 / 方法** · 用表征和温度重缩放 softmax 估计样本对目标任务的贡献，无需重训。
- **Baseline** · 既有 CLIP 数据选取方法。
- **Benchmark** · ImageNet 零样本及分布偏移数据，另做噪声检测与记忆分析。
- **关键结果 / 消融** · 摘要报告多个基准稳定改善，Self-InfCLIP 支持不重训的数据分析。
- **适用条件 / 局限** · 依赖表征与目标任务分布，分数与真正训练影响的误差待核实。

**可复用机制** · 把目标相关性和数据冗余放进同一可比较分数，再按偏移条件验证选择顺序。

<a id="paper-152598"></a>

## InfCoiL: Coordinated Planner-Controller Learning for Closed-Loop Physics-Based Human-Object Interaction

[官方论文页](https://neurips.cc/virtual/2026/poster/152598) · [作者来源](https://openreview.net/forum?id=RvZ2OxrgcE)

- **问题 / 瓶颈** · 开环规划与控制序列偏移使接触动作难执行。
- **核心创新 / 方法** · 自回归规划执行并交替闭环微调；用物理回放组相对奖励和语义协方差更新生成规划器。
- **Baseline** · 开环规划执行系统；具名基线待核实。
- **Benchmark** · 多物体和人形形态的物理交互任务，动作质量及成功率。
- **关键结果 / 消融** · 摘要报告动作质量及成功率较基线提升。
- **适用条件 / 局限** · 仿真到真机及协方差构造细节待核实。

**可复用机制** · 将计划对语义目标的符合与控制可执行性分开评估，再用闭环回放把两者接起来。

<a id="paper-148280"></a>

## Inference for Many Quantiles under Local Differential Privacy

[官方论文页](https://neurips.cc/virtual/2026/poster/148280) · [作者来源](https://openreview.net/forum?id=z2oKVYmfLa)

- **问题 / 瓶颈** · 逐个分位推断可能交叉，联合协方差与密度又难估计。
- **核心创新 / 方法** · 将分位数问题转换为类别独热估计，投影 Robbins–Monro 保持序列单调，结合平均与多变量自归一化。
- **Baseline** · kRR、OUE、OLH、Hadamard 响应是可替换的本地隐私机制。
- **Benchmark** · 数值实验与理论分析，考察多个分位数的联合椭球区间。
- **关键结果 / 消融** · 给出联合渐近枢轴区间，无须直接估计干扰密度或协方差。
- **适用条件 / 局限** · 结论是渐近的，分位数量、隐私强度和样本量有限时需复核。

**可复用机制** · 先用投影满足结构约束，再报告联合置信区域而不是逐点区间。

<a id="paper-153713"></a>

## Inference Time Nash Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/153713) · [作者来源](https://openreview.net/forum?id=JKuHvi1fHD)

- **问题 / 瓶颈** · Bradley–Terry 标量模型难表达一般偏好，训练对齐还要求访问参数。
- **核心创新 / 方法** · 把策略间偏好写成双人零和博弈，以 Best-of-Nash 或 Nash 镜像下降估计均衡。
- **Baseline** · 基础策略、已微调模型和标量奖励式推理对齐。
- **Benchmark** · 三个数据集，测偏好表现和正则超参鲁棒性。
- **关键结果 / 消融** · 两种方法对偶间隙达到问题下界，实测优于基础策略并接近微调模型。
- **适用条件 / 局限** · 依赖可调用的成对偏好估计器；成本及偏好不稳定性待核实。

**可复用机制** · 偏好可能有循环时，改用策略混合的博弈目标并报告额外比较次数。

<a id="paper-151371"></a>

## Inference-Time Refinement Closes the Synthetic-Real Gap in Tabular Diffusion

[官方论文页](https://neurips.cc/virtual/2026/poster/151371) · [作者来源](https://openreview.net/forum?id=b4cH8bQHbT)

- **问题 / 瓶颈** · 仅改生成器训练难弥合合成数据下游效用差距。
- **核心创新 / 方法** · 以合成与真实样本间对称 Chamfer 目标提供逆扩散梯度并进行批次排序，按数据集选择配置。
- **Baseline** · TabDiff 和真实训练数据。
- **Benchmark** · 15 个分类与回归基准，比较下游效用，以及保真、多样性和隐私。
- **关键结果 / 消融** · 相对真数据的下游表现中位数提升 8.6%，15 项均超过 TabDiff。
- **适用条件 / 局限** · 推理配置仍依赖真实样本；搜索成本和测试集泄漏防控需复核。

**可复用机制** · 将覆盖目标跨采样和重排共享，在预留真实验证集上分别评估两阶段贡献。

<a id="paper-155309"></a>

## Inference-Time Self-Aligned Drifting for Few-Step Flow Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/155309) · [作者来源](https://openreview.net/forum?id=6ZIc3ymky8)

- **问题 / 瓶颈** · 少步确定积分易均值集中，无方向随机噪声又会在积分中削弱保真。
- **核心创新 / 方法** · 根据采样历史外推运动残差，通过局部 OU 过程约束漂移，无额外网络评估。
- **Baseline** · 确定 ODE 与 250 步 SDE。
- **Benchmark** · ImageNet-256 FID 以及 TurboDiffusion、Wan2.1 的快速视频生成。
- **关键结果 / 消融** · 20 次网络评估 FID 2.00，250 步 SDE 为 2.06。
- **适用条件 / 局限** · 对基础模型质量和轨迹参数敏感性待核实。

**可复用机制** · 同等网络评估次数下，对比分布扩展是否沿现有轨迹局部方向，避免把方差改善和增加计算混在一起。

<a id="paper-156068"></a>

## Inference-Time Vulnerability Beyond Shallow Safety: Alignment Along Generation Trajectories

[官方论文页](https://neurips.cc/virtual/2026/poster/156068) · [作者来源](https://openreview.net/forum?id=0hBB2oa8uG)

- **问题 / 瓶颈** · 只关注答复开头和隐状态拒绝信号易高估整体防护。
- **核心创新 / 方法** · 比较输出全过程的安全表现，并测试加入过程级防护训练的效果。
- **Baseline** · 既有面向输出的安全对齐和基于隐状态的拒绝信号。
- **Benchmark** · 多阶段生成安全压力测试，具体模型与指标待核实。
- **关键结果 / 消融** · 摘要报告内部拒绝信号不足以预测实际稳健性，过程级防护训练改善所测阶段。
- **适用条件 / 局限** · 结论依赖所测模型和压力评测，无法直接推出广泛部署保证。

**可复用机制** · 验收同时检查过程级和最终输出指标，防止仅靠早期拒绝判定安全。

<a id="paper-152708"></a>

## Inferotemporal Cortex Collaborates Before It Codes: Non-Serial Inter-Area Synergy in the Macaque Ventral Stream

[官方论文页](https://neurips.cc/virtual/2026/poster/152708) · [作者来源](https://openreview.net/forum?id=QzsZg9sldw)

- **问题 / 瓶颈** · 单区信息出现时间不能代表整个系统整合顺序。
- **核心创新 / 方法** · 用部分信息分解对 V1、V4、IT 并行记录分离独有与协同信息。
- **Baseline** · 串行前馈层级为解释对照。
- **Benchmark** · 两只猕猴、逾 25,000 张图、五类视觉目标、5 毫秒分辨率。
- **关键结果 / 消融** · 跨区协同比 IT 独有信息早 15–65 毫秒，V1 与 IT 协同可在 V1 独有信息消失后继续逾 120 毫秒。
- **适用条件 / 局限** · 样本动物少，观测时序不能证明连接因果。

**可复用机制** · 诊断分层网络时将层级探针和跨层组合探针按时间分别画出。

<a id="paper-153994"></a>

## Inferring Computational Structure from Neural Recordings with Gain-Modulated Linear Dynamical Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/153994) · [作者来源](https://openreview.net/forum?id=H0jkombMst)

- **问题 / 瓶颈** · 错误的假定激活可让低秩 RNN 拟合活动却错误解释回路。
- **核心创新 / 方法** · gmLDS 用状态依赖的逐单元增益和固定低秩连通矩阵分解动力学。
- **Baseline** · 给定固定激活的低秩 RNN。
- **Benchmark** · 多组已知真机制合成数据及感知、情境决策记录。
- **关键结果 / 消融** · 作者称合成中能恢复局部有效连通性，真实记录形成可检验假设。
- **适用条件 / 局限** · 真实回路缺直接真值；拟合适配不等于识别机制。

**可复用机制** · 用激活错配的仿真测试，对比观测误差与线性化动力学恢复误差。

<a id="paper-149640"></a>

## Inferring how internal brain state shapes neural responses with state-dependent diffusion models

[官方论文页](https://neurips.cc/virtual/2026/poster/149640) · [作者来源](https://openreview.net/forum?id=oaGzFBAs66)

- **问题 / 瓶颈** · 有限记录缺条件配对且已见配对重复次数少，两类误差易混淆。
- **核心创新 / 方法** · 扩散以过去状态和外部刺激为条件，分别对重新配对和重复采样做评估。
- **Baseline** · 受限调制模型、无显式状态的神经活动生成路线。
- **Benchmark** · 小鼠 V1、猴 V4、小鼠纹状体记录，比较状态依赖结构和覆盖。
- **关键结果 / 消融** · 摘要称生成样本保持记录结构并扩展覆盖。
- **适用条件 / 局限** · 未观察组合的真实效应仍难验证，合理性不能视为反事实真值。

**可复用机制** · 在其他条件过程模拟中主动留出组合并独立测条件插值与重复波动。

<a id="paper-148570"></a>

## Inferring learning rules in deep neural network architectures from animal learning data

[官方论文页](https://neurips.cc/virtual/2026/poster/148570) · [作者来源](https://openreview.net/forum?id=wsgPXDF5VH)

- **问题 / 瓶颈** · 深网络能任意近似浅网络的梯度下降，拟合好不足以确定深度。
- **核心创新 / 方法** · 用不可辨识性分析修正拟合，以初始参数、学习率和选择随机性拟合个体。
- **Baseline** · 单层线性、两层线性和两层 sigmoid。
- **Benchmark** · 两组小鼠感知决策记录，比较 AIC、准确率、偏差及刺激敏感度。
- **关键结果 / 消融** · 两层非线性在 88 只中的 84 只获最佳 AIC。
- **适用条件 / 局限** · 比较只覆盖三种候选，无法确证真实实现。

**可复用机制** · 模拟不同学习规则并做可恢复性检验，再报告可辨识的行为量。

<a id="paper-148677"></a>

## InfoFlow: A Framework for Multi-Layer Transformer Analysis

[官方论文页](https://neurips.cc/virtual/2026/poster/148677) · [作者来源](https://openreview.net/forum?id=vtzQl6Q3H4)

- **问题 / 瓶颈** · 单层 softmax 的高效读取偏向最大得分项，多条耦合信息解码进一步变贵。
- **核心创新 / 方法** · InfoFlow 按层追踪可访问信息位置，给不同信息传播模式分配近似率。
- **Baseline** · 单层及每层单头的两层 Transformer。
- **Benchmark** · 构造检索任务及训练网络观察，以所需参数和精度衡量。
- **关键结果 / 消融** · 指定任务中单层参数随序列长度的精度指数增大，两层可用 O(ε^-1) 参数。
- **适用条件 / 局限** · 定理针对特定任务和架构，常规语料不直接满足。

**可复用机制** · 对排序检索和多证据绑定分别做宽度与深度控制试验。

<a id="paper-149947"></a>

## InfoNav: A Unified Value Framework Integrating Semantic Relevance and Information Gain for Zero-Shot Object Goal Navigation

[官方论文页](https://neurips.cc/virtual/2026/poster/149947) · [作者来源](https://openreview.net/forum?id=lzhhlAlmjK)

- **问题 / 瓶颈** · 区域语义影响范围不同，探索利用分离时弱证据下行动不稳。
- **核心创新 / 方法** · 分层空间影响场估计语义价值，以视觉语义连通近似信息增益；不确定检测延后复查。
- **Baseline** · BeliefMapNav 和代表性大语言模型导航方案。
- **Benchmark** · HM3Dv1、HM3Dv2、MP3D，零样本成功率和多模态调用数。
- **关键结果 / 消融** · 成功率 62.0%、81.5%、41.8%；较代表性方法少超过 96% 多模态模型调用；消融显示两价值互补。
- **适用条件 / 局限** · 依赖语义地图和连通估计，实机边界待核。

**可复用机制** · 按线索强弱分层评估探索，避免只测平均成功率。

<a id="paper-153429"></a>

## Information bottleneck dynamics during learning across artificial and biological neural systems

[官方论文页](https://neurips.cc/virtual/2026/poster/153429) · [作者来源](https://openreview.net/forum?id=LOW2f7vBIQ)

- **问题 / 瓶颈** · 信息瓶颈的压缩阶段可能被误当作通用学习规律。
- **核心创新 / 方法** · 以匹配分析流程比较训练中的脉冲网络、鼠视觉皮层与海马表征。
- **Baseline** · 不同层、行为与解码器对照。
- **Benchmark** · CIFAR-10 脉冲 ResNet-18、公开视觉皮层和海马记录。
- **关键结果 / 消融** · 三个系统相关性轴均随学习变化，明显压缩有任务和层依赖。
- **适用条件 / 局限** · 跨系统的轴定义不同，信息估计受方法影响。

**可复用机制** · 跨任务画两条信息曲线并做解码对照，避免把压缩当作统一进度条。

<a id="paper-154972"></a>

## Information-Directed Offline-to-Online Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/154972) · [作者来源](https://openreview.net/forum?id=9YV37OfwpJ)

- **问题 / 瓶颈** · 行为数据会排除一部分不确定性，盲从后验最优策略可能忽视高信息动作。
- **核心创新 / 方法** · 对离线数据条件化，信息定向采样权衡即时遗憾与在线轨迹信息增益。
- **Baseline** · 同随机策略类下的 Thompson sampling。
- **Benchmark** · 已知动力学线性奖励理论、受控老虎机及 D4RL 转在线。
- **关键结果 / 消融** · 证明可继承信息比界，展示被支配但有信息的探测可获得常数因子遗憾优势。
- **适用条件 / 局限** · 可计算界依赖先验与模型设定，现实在线步数和探测成本待核。

**可复用机制** · 量化离线覆盖后单列探测动作的遗憾和消除不确定性收益。

<a id="paper-154203"></a>

## Information Discernment in Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154203) · [作者来源](https://openreview.net/forum?id=FQemc5OlfD)

- **问题 / 瓶颈** · 模型可能把流行度当可靠性，也可能同样接纳纠正和误导信息。
- **核心创新 / 方法** · 定义两类辨别指标，通过控制来源和主张做更新试验。
- **Baseline** · 13 个模型及不同规模代际；另有人类偏好验证。
- **Benchmark** · 约 67 万试验及 299 人预注册研究。
- **关键结果 / 消融** · 两类表现接近随机；流行度权重约为可靠性的两倍；增大规模未改善来源辨别。
- **适用条件 / 局限** · 指标依赖真值和可靠性定义，开放域扩展待核。

**可复用机制** · 对检索系统置换来源名和保持主张不变，检查是否真按可信度更新。

<a id="paper-149101"></a>

## Information-Geometric Forward Policy Training in GFlowNets

[官方论文页](https://neurips.cc/virtual/2026/poster/149101) · [作者来源](https://openreview.net/forum?id=suXwdFeEA9)

- **问题 / 瓶颈** · 参数共享会改变时间得分相关与优化几何。
- **核心创新 / 方法** · 把轨迹 Fisher 分解为逐步条件二阶矩，按可计算性选择精确、蒙特卡洛或结构化近似。
- **Baseline** · 欧式优化与信息几何自然梯度。
- **Benchmark** · GFlowNet 探索和收敛示例；具体实例待核。
- **关键结果 / 消融** · 理论说明何时交互消失，并用示例比较优化表现。
- **适用条件 / 局限** · 需精确或足够好的 Fisher 近似；规模和求解成本待核。

**可复用机制** · 存在局部因子时比较结构化自然梯度与相同算力的简单预条件。

<a id="paper-151063"></a>

## Information Loss and Disparate Effects in Network Embeddings

[官方论文页](https://neurips.cc/virtual/2026/poster/151063) · [作者来源](https://openreview.net/forum?id=dHN3oKgj42)

- **问题 / 瓶颈** · 整体指标可能掩盖小而稀疏群体的不可逆损失。
- **核心创新 / 方法** · 用随机块模型刻画密度和同配性条件下嵌入不可逆性。
- **Baseline** · 未施公平干预的低维嵌入为分析对象。
- **Benchmark** · 随机块模型的渐近分析及下游链路预测。
- **关键结果 / 消融** · 不同图可趋于相同嵌入，稀疏小社群受损更重且预测误差增大。
- **适用条件 / 局限** · 依赖生成模型和渐近条件，真实图需单独验证。

**可复用机制** · 按社群大小和稀疏度分层同时测重建与链路误差。

<a id="paper-139705"></a>

## Information Parity for Code: The Scope of Transfer in Multilingual Code Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139705) · [作者来源](https://openreview.net/forum?id=9Vw26t3fU5)

- **问题 / 瓶颈** · 任务长度与语言差距混杂时单一排名难解释。
- **核心创新 / 方法** · 对 20 种语言、22 算法构造语义对齐平行代码，计算 Code IP 并跨任务关联。
- **Baseline** · 自然语言 Information Parity 为方法来源，比较三种任务。
- **Benchmark** · 跨语言训练模型代码任务，比较 Spearman 相关。
- **关键结果 / 消融** · 短生成相关为 -0.55 到 -0.81，执行为 -0.429，整程序为 +0.105。
- **适用条件 / 局限** · 相关不能外推为因果，平行语料算法覆盖有限。

**可复用机制** · 先控制语义和模板代码，再按任务时域评估跨语言迁移。

<a id="paper-151344"></a>

## Information Propagation via Sign-Flip Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/151344) · [作者来源](https://openreview.net/forum?id=bDaqHSFP9J)

- **问题 / 瓶颈** · 方差不变仍可能逐坐标毁掉信号身份。
- **核心创新 / 方法** · 通过带符号间隔的首达分析推导噪声临界尺度与层数平方根成反比，并反推目标翻转率。
- **Baseline** · 传统方差、相关和雅可比条件指标。
- **Benchmark** · 合成与真实训练任务，观察末层符号翻转率及训练表现。
- **关键结果 / 消融** · 给出跨深度校准规则；摘要称翻转率影响训练。
- **适用条件 / 局限** · 针对恒等加噪类初始结构，激活和架构变化需检验。

**可复用机制** · 同时固定方差并扫符号保留率，分清常规尺度和信号身份的影响。

<a id="paper-152156"></a>

## Information Templates: A New Paradigm for Intelligent Active Feature Acquisition

[官方论文页](https://neurips.cc/virtual/2026/poster/152156) · [作者来源](https://openreview.net/forum?id=V6ZmfeWyKM)

- **问题 / 瓶颈** · 贪心不足以发现互补特征，直接训练强化策略动作空间大。
- **核心创新 / 方法** · 学习共同提供信息的特征子集模板，推理时按实例选后续特征。
- **Baseline** · 强化学习采集和贪心方法。
- **Benchmark** · 合成与真实数据，比较预测、采集代价与计算。
- **关键结果 / 消融** · 报告性能提升、采集与计算成本降低。
- **适用条件 / 局限** · 依赖模板覆盖少见特征依赖，换成本设定需复验。

**可复用机制** · 在合成互补信号上验证模板，再画成本与预测质量前沿。

<a id="paper-149551"></a>

## Information-Theoretic Generalization Bounds for Sequential Decision Making

[官方论文页](https://neurips.cc/virtual/2026/poster/149551) · [作者来源](https://openreview.net/forum?id=pIr4aHBv2v)

- **问题 / 瓶颈** · 经典 supersample 的条件互信息界不能直接处理因果揭露数据。
- **核心创新 / 方法** · 分开实际学习过滤与证明用扩展，对逐行可交换情形定义逐轮 CMI，并给 Bernstein 细化。
- **Baseline** · 批量独立同分布的 supersample 界。
- **Benchmark** · 在线学习、加权流式主动学习、随机多臂老虎机理论特例。
- **关键结果 / 消融** · 推导逐轮控制界，方差条件下收敛更快。
- **适用条件 / 局限** · 逐行可交换等假定需全文明确；无摘要实证。

**可复用机制** · 验证顺序评估方法前先检查数据揭露机制是否满足可交换条件。

<a id="paper-153827"></a>

## Information-Theoretic Generalization for Set-Input Optimization-Valued Objectives

[官方论文页](https://neurips.cc/virtual/2026/poster/153827) · [作者来源](https://openreview.net/forum?id=IR2PNGshps)

- **问题 / 瓶颈** · CVaR 等依赖全批和事后优化器，不能用固定逐样本损失的界。
- **核心创新 / 方法** · 在选择差浓度条件下以预测与选择器的条件互信息界定差距，并用稳定性和凸 Lipschitz 条件验证。
- **Baseline** · 标准逐例平均的信息论泛化框架。
- **Benchmark** · 理论覆盖多重校准、CVaR 与 Cressie–Read 稳健目标。
- **关键结果 / 消融** · 给出不显式依赖辅助优化器类别复杂度的界，稳定时还有细化。
- **适用条件 / 局限** · 适用目标需满足选择差集中，实证与常数的实用度待核。

**可复用机制** · 评估风险估计器时区分评估样本波动与辅助最优点重新选择导致的差异。

<a id="paper-155089"></a>

## Informed Posterior Sampling: More Efficient Online Learning with Few Offline Demonstrations in Average-Reward MDPs

[官方论文页](https://neurips.cc/virtual/2026/poster/155089) · [作者来源](https://openreview.net/forum?id=8WF7tRvbkZ)

- **问题 / 瓶颈** · 把历史专家动作当最优可能错误消除在线探索。
- **核心创新 / 方法** · 给离线行为策略加未知胜任度参数，用条件后验采样并以 iRLSVI 近似。
- **Baseline** · 在线学习方法；另有是否建模专家能力的理论对照。
- **Benchmark** · 无限时域平均奖励 MDP 和高探索难度实验。
- **关键结果 / 消融** · 精确方法获近似平方根阶遗憾界；小规模示范即可让近似法优于纯在线。
- **适用条件 / 局限** · 行为模型与专家胜任度先验需合理，跨类型专家待核。

**可复用机制** · 在不同示范噪声水平测试固定专家假设与显式不确定性的区别。

<a id="paper-138981"></a>

## InformedXRD: Reproducible Benchmarks and Physics-Informed Evaluation for Powder Diffraction Symmetry Classification

[官方论文页](https://neurips.cc/virtual/2026/poster/138981) · [作者来源](https://openreview.net/forum?id=snum235vrK)

- **问题 / 瓶颈** · 粉末衍射实验的类别、预处理及指标不一致，聚合分数掩盖难度。
- **核心创新 / 方法** · 把 230 个空间群映射到 99 个消光群，按先验频率和层级错误严重性报告。
- **Baseline** · 频率先验、公开 ViT 与一维残差 CNN。
- **Benchmark** · RRUFF-473、RRUFF-325，Top-1、Top-5 和分层错误。
- **关键结果 / 消融** · 排名受指标选择影响，分层暴露标签熵混淆。
- **适用条件 / 局限** · 可辨程度依赖所用观测和系统消光假设。

**可复用机制** · 使标签符合测量设备的分辨能力，并检查表面提升是否来自标签构成。

<a id="paper-155588"></a>

## InfoSFT: Learn More and Forget Less with Information-Aware Token Weighting

[官方论文页](https://neurips.cc/virtual/2026/poster/155588) · [作者来源](https://openreview.net/forum?id=4UGod3zYeD)

- **问题 / 瓶颈** · 均匀拟合容易记低概率样本，简单剔除低概率又会损失新行为。
- **核心创新 / 方法** · 用基座对词元的置信度定权，让中等置信提供主要学习信号。
- **Baseline** · 原始 SFT、似然加权方法。
- **Benchmark** · 数学、代码、思维链和旧能力保留，多模型家族。
- **关键结果 / 消融** · 摘要报告泛化和旧能力保留均改善。
- **适用条件 / 局限** · 依赖基座置信可区分熟悉程度及更新风险；精确权重待核实。

**可复用机制** · 把权重高峰放在模型尚未熟练而又不属于极端离群的监督点。

<a id="paper-153094"></a>

## INFUSER: Influence-Guided Self-Evolution Improves Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/153094) · [作者来源](https://openreview.net/forum?id=O0Hwud8ZLX)

- **问题 / 瓶颈** · 任务难度未必等于训练价值。
- **核心创新 / 方法** · 让生成器从文档产题，以优化器感知的影响分数回报生成器，并为噪声分数引入双归一化 GRPO。
- **Baseline** · 强自演化基线和冻结 32B 生成器。
- **Benchmark** · Qwen3-8B-Base，奥赛、SuperGPQA、数学和代码。
- **关键结果 / 消融** · 奥赛及 SuperGPQA 报告超过 20% 相对改进，摘要报告消融支持。
- **适用条件 / 局限** · 影响估计依赖目标分布及训练算力。

**可复用机制** · 把在线合成数据的质量定义为当前学习者的边际收益，避免只按难度选样。

<a id="paper-152644"></a>

## Inline Critic Steers Image Editing

[官方论文页](https://neurips.cc/virtual/2026/poster/152644) · [作者来源](https://openreview.net/forum?id=RT1DXXQkZm)

- **问题 / 瓶颈** · 整图或整步生成后才开始修复，纠正信号太迟。
- **核心创新 / 方法** · 加入可学习评论词元，在中层读出误差并引导后续隐藏状态。
- **Baseline** · 同冻结编辑骨干及其他编辑模型。
- **Benchmark** · GEdit-Bench、RISEBench、KRIS-Bench。
- **关键结果 / 消融** · 早层误差图与最终图排序相关 0.83；RISEBench 相对同骨干提高 9.4。
- **适用条件 / 局限** · 依赖存在可辨识的早期误差信号及追加评论器训练。

**可复用机制** · 先测早层质量代理能否预示错误，再将局部修复放入同一次前向。

<a id="paper-155393"></a>

## Inner Product Aware Quantization: Provably Fast, Accurate, and Adaptive Algorithms

[官方论文页](https://neurips.cc/virtual/2026/poster/155393) · [作者来源](https://openreview.net/forum?id=60WCaegfit)

- **问题 / 瓶颈** · 低均方重建误差不保证未见向量的内积保真。
- **核心创新 / 方法** · 分别定义最坏和平均查询的内积保持目标，借助自适应随机量化求解。
- **Baseline** · 已有自适应随机量化算法。
- **Benchmark** · 多种工作负载；内积质量和量化速度。
- **关键结果 / 消融** · 标准 ASQ 报告同质量下加速 2 至 10 倍。
- **适用条件 / 局限** · 结果依赖查询分布、最坏情况模型和压缩约束。

**可复用机制** · 按压缩后真正使用的算子衡量误差，避免优化无关坐标偏差。

<a id="paper-148598"></a>

## Innocuous-Seeming Data, Latent Ideology: Ideological Generalisation in Finetuned LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/148598) · [作者来源](https://openreview.net/forum?id=wYDEd2wtpL)

- **问题 / 瓶颈** · 一般能力不变时，窄领域训练仍可能改变未见议题上的输出。
- **核心创新 / 方法** · 分别衡量漂移的领域广度和微调相对同样例提示的放大程度。
- **Baseline** · 基座、少样本提示及混合通用数据设置。
- **Benchmark** · GPT-4.1、Gemma-3 的跨主题评测及 GSM8K。
- **关键结果 / 消融** · 摘要报告漂移跨主题复现，而 GSM8K 波动仍约在一百分点内。
- **适用条件 / 局限** · 结论依赖题集、模型与评分定义；不代表所有用户或社会情境。

**可复用机制** · 将通用能力回归和安全倾向回归独立验收，各自覆盖训练外主题。

<a id="paper-155045"></a>

## Inpainting physics: self-supervised learning for context-driven fluid simulation

[官方论文页](https://neurips.cc/virtual/2026/poster/155045) · [作者来源](https://openreview.net/forum?id=8rpCiIZ22W)

- **问题 / 瓶颈** · 直接前向代理绑定训练时的边界规范，局部改几何需重新预测全域。
- **核心创新 / 方法** · 训练速度场自监督先验，在推理固定已知区域；用邻域分词将三维网格压到空间潜变量。
- **Baseline** · 显式条件的监督流体代理。
- **Benchmark** · 颅内血流，边界条件和数据集偏移及局部几何变化。
- **关键结果 / 消融** · 摘要报告偏移下优于监督代理，可复用未改变区域。
- **适用条件 / 局限** · 针对稳态流体模拟，需已知条件足以约束场。

**可复用机制** · 把已知物理状态作为可交换的推理约束，减少训练时对条件格式的绑定。

<a id="paper-155795"></a>

## InQuant: In-Place Mixed-Precision KV Cache Quantization via Saliency-Aware Neighbor-Slot Reuse

[官方论文页](https://neurips.cc/virtual/2026/poster/155795) · [作者来源](https://openreview.net/forum?id=2qVEX3Ujtr)

- **问题 / 瓶颈** · 传统离群通道保存引入额外内存及索引。
- **核心创新 / 方法** · 保持四位打包布局，把高显著八位值的额外半字节写入可牺牲的邻槽并以描述符恢复。
- **Baseline** · 代表性离群值感知量化。
- **Benchmark** · 六个语言模型和长上下文负载；精度、压缩和编解码延迟。
- **关键结果 / 消融** · 固定四倍物理压缩，量化和反量化延迟改善 2.2 至 3.4 倍。
- **适用条件 / 局限** · 需存在邻近低显著通道；标记处理与硬件布局相关。

**可复用机制** · 先定物理存储预算，再用低价值字段容纳必要精度，而不额外分配缓冲。

<a id="paper-151787"></a>

## Inside Emergence: Structure-Behaviour Gaps in Language Model Training

[官方论文页](https://neurips.cc/virtual/2026/poster/151787) · [作者来源](https://openreview.net/forum?id=Y0OKwBDt0b)

- **问题 / 瓶颈** · 单看行为分数无法区分突然重组与延迟显现。
- **核心创新 / 方法** · 沿训练追踪平均消融修补矩阵的谱，估结构完成相对行为跃迁的时间差。
- **Baseline** · 行为曲线与结构谱的并行对照。
- **Benchmark** · 150 条 Pythia 轨迹，五任务、三尺度、十种子。
- **关键结果 / 消融** · 94% 的轨迹结构先出现，早期显著组件承载之后 86% 至 99% 的所测能力。
- **适用条件 / 局限** · 覆盖有限模型尺度和任务；结构指标定义依赖干预。

**可复用机制** · 将内部成熟时间与外部达标时间分开测，选择更有信息的早期检查点。

<a id="paper-150577"></a>

## Inside the Loop: A Mechanistic Study of Weight-Tied Transformers on Depth-Bound Algorithmic Tasks

[官方论文页](https://neurips.cc/virtual/2026/poster/150577) · [作者来源](https://openreview.net/forum?id=h8PkVhb8VI)

- **问题 / 瓶颈** · 有效深度相同不一定意味着学到可复用的单步规则。
- **核心创新 / 方法** · 按批采样跳数，训练共享块循环；用残差探针检查每次循环解码哪一步。
- **Baseline** · 等有效深度的非共享固定深度 Transformer。
- **Benchmark** · 16 实体定向排列遍历，最多 15 跳。
- **关键结果 / 消融** · 3.2M 共享模型完成 15 跳，25.8M 对照仅三跳；每次循环推进一跳。
- **适用条件 / 局限** · 来自合成遍历与相应训练分布。

**可复用机制** · 任务具有重复算法步骤时尝试结构化权重共享，再用逐步探针验证执行规律。

<a id="paper-155553"></a>

## Insight-Driven Search: A Framework for Multi-objective Automated Heuristic Design with Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155553) · [作者来源](https://openreview.net/forum?id=4hPzFmpJng)

- **问题 / 瓶颈** · 只保存候选程序不便复用此前搜索经验，质量与效率也常冲突。
- **核心创新 / 方法** · 抽取成功启发式的设计见解并维护池，用 UCB 式选择组合，奖励基于当前 Pareto 档案。
- **Baseline** · 代表性语言模型启发式设计方法。
- **Benchmark** · TSP、CVRP、VRPTW；解质和计算效率。
- **关键结果 / 消融** · 摘要报告收敛更快且质量效率折中改善。
- **适用条件 / 局限** · 依赖可用的文本见解提取及成本评价。

**可复用机制** · 给搜索历史中的可组合决策单独建池，按边际 Pareto 贡献选择复用。

<a id="paper-153491"></a>

## INSPO : Unlocking Intrinsic Self-Reflection for LLM Preference Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/153491) · [作者来源](https://openreview.net/forum?id=L04yHIK5g8)

- **问题 / 瓶颈** · 标准 DPO 未完整利用成对对照，选参考策略也可能影响结果。
- **核心创新 / 方法** · 将最优策略写成对上下文与备选响应的条件策略，再蒸馏为推理无需备选的模型。
- **Baseline** · DPO 系列和标准 RLHF 目标。
- **Benchmark** · 胜率、长度受控指标，多种 DPO 变体。
- **关键结果 / 消融** · 摘要报告理论不变性和实证改善，无新增推理开销。
- **适用条件 / 局限** · 理论结论依赖论文建模和特权蒸馏有效性。

**可复用机制** · 把回答间的比较结构用于训练教师，而不是迫使部署时额外生成对照答案。

<a id="paper-150789"></a>

## Instability of Meta-Learning Intrinsic Rewards for Policy Gradient Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/150789) · [作者来源](https://openreview.net/forum?id=fO6evIFLoV)

- **问题 / 瓶颈** · 稠密非平稳内在奖会放大价值损失，压制共享编码器中的政策学习。
- **核心创新 / 方法** · 分析 LIRPG 崩溃并改用分阶段的策略梯度解耦优化。
- **Baseline** · 原 LIRPG 与共享编码器策略价值更新。
- **Benchmark** · 高维环境，特别是纯内在奖训练。
- **关键结果 / 消融** · 摘要报告基线可降到近随机，分阶段训练可缓解。
- **适用条件 / 局限** · 风险集中于共享表征和相应奖励条件。

**可复用机制** · 先量化策略与价值损失对共享特征的竞争，再决定是否分时训练。

<a id="paper-148452"></a>

## Instance-Adaptive Online Multicalibration

[官方论文页](https://neurips.cc/virtual/2026/poster/148452) · [作者来源](https://openreview.net/forum?id=xjc4HHAmIS)

- **问题 / 瓶颈** · 统一最坏情况算法无法利用稳定段落。
- **核心创新 / 方法** · 维护动态二分网格，误差用细分树叶数及相对群体族的阈值复杂度控制。
- **Baseline** · 已知最坏情况校准率。
- **Benchmark** · 最坏、边际随机及分段平稳序列的理论累计误差。
- **关键结果 / 消融** · 最坏为 T 的三分之二次方量级，随机情形为平方根量级，分段为 sqrt(JT)，略去对数项。
- **适用条件 / 局限** · 依赖相应序列类及组族定义。

**可复用机制** · 让概率分桶复杂度随数据变化增加，而非在稳定时承担过细划分的代价。

<a id="paper-153738"></a>

## Instance-Dependent Bandit Convex Optimization in One Dimension

[官方论文页](https://neurips.cc/virtual/2026/poster/153738) · [作者来源](https://openreview.net/forum?id=J6eKxKuBeW)

- **问题 / 瓶颈** · 两种一维凸 bandit 停止标准表面相近，却可能有不同样本难度。
- **核心创新 / 方法** · 用长度对应于定位半径的子水平集刻画难度，构造二分式算法。
- **Baseline** · 问题的下界与固定置信最小后悔结果。
- **Benchmark** · 一维随机凸 bandit 理论样本复杂度。
- **关键结果 / 消融** · 定位算法匹配实例下界至对数因子；近优值仍需精度倒数平方量级。
- **适用条件 / 局限** · 要求一维凸问题，定位结果假设唯一最小点。

**可复用机制** · 先用业务需求明确误差单位，避免把位置精度所享有的简单实例优势误用于值误差。

<a id="paper-149650"></a>

## Instance-Optimal Estimation with Multiple LLM Judges on a Budget

[官方论文页](https://neurips.cc/virtual/2026/poster/149650) · [作者来源](https://openreview.net/forum?id=oUcOaeF67J)

- **问题 / 瓶颈** · 均匀分配忽略问题难度、评审价格和稳定性。
- **核心创新 / 方法** · 用带乐观偏差的方差估计自适应分配，再以逆方差汇总评分。
- **Baseline** · 均匀分配和已知方差的预言分配。
- **Benchmark** · 合成基准及 HelpSteer2，预算下的得分向量误差。
- **关键结果 / 消融** · 理论接近预言误差率并有匹配下界，实证优于均匀分配。
- **适用条件 / 局限** · 依赖评审成本可知、误差模型与评分重复可获得。

**可复用机制** · 将额外查询投向信息增益与价格比更高的题目评审组合。

<a id="paper-139657"></a>

## Instantiation of Human Values in Image Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/139657) · [作者来源](https://openreview.net/forum?id=CaD34X3ptc)

- **问题 / 瓶颈** · 单看单图与提示匹配无法识别模式在群体层面的收缩。
- **核心创新 / 方法** · 从多模型样本提取反复出现的视觉原型，并与人类描述的组合宽度比较。
- **Baseline** · 人类描述与四种文本到图像模型。
- **Benchmark** · 70 项价值、28,000 张图，原型集中度及社会构型覆盖。
- **关键结果 / 消融** · 摘要报告生成图的解释范围比人类更集中，覆盖的社会构型有偏。
- **适用条件 / 局限** · 依赖文化框架与提示措辞，样本不能代表全球视角。

**可复用机制** · 在样本集层面验收同一概念的表达多样性，用原型频率发现遗漏。

<a id="paper-155402"></a>

## In STeP: Speculative Tensor Parallelism for Concurrent Heterogeneous Inference of LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/155402) · [作者来源](https://openreview.net/forum?id=5ujmDrit5K)

- **问题 / 瓶颈** · 异构解码通常用独立草案，CPU、GPU 等待且显存利用不足。
- **核心创新 / 方法** · 在 GPU 放验证器最显著的 FFN 通道子网作草案，其余在 CPU；两设备并行核验。
- **Baseline** · SpecExec、SubSpec、单独张量并行与推测解码。
- **Benchmark** · 24B 至 123B 稠密模型、32 至 192 GB 显存、五个基准。
- **关键结果 / 消融** · 分别较 SpecExec 和 SubSpec 最高快 1.4、1.8 倍；理论保持采样分布。
- **适用条件 / 局限** · 依赖子网近似质量及 CPU、GPU 与互联的特定平衡。

**可复用机制** · 以共享参数的可调规模草案占满 GPU，并让两设备的核验计算重叠。

<a id="paper-150433"></a>

## Instruction Anchor: Dissecting the Mechanistic Dynamics of Modality Arbitration

[官方论文页](https://neurips.cc/virtual/2026/poster/150433) · [作者来源](https://openreview.net/forum?id=i55gKixTsv)

- **问题 / 瓶颈** · 总体准确率无法指出指令依从失效的机制。
- **核心创新 / 方法** · 沿指令 token 跟踪信息流，并定点阻断或增强参与仲裁的注意力头。
- **Baseline** · 未干预模型与一般语言、视觉能力控制。
- **Benchmark** · 多模态指令依从和干预后的失败样本恢复；具名模型和基准待核实。
- **关键结果 / 消融** · 屏蔽约 5% 的已识别头显著削弱模态依从，增强可恢复最多约 60% 的失败样本。
- **适用条件 / 局限** · 识别头的跨架构稳定性及其他能力副作用需复核。

**可复用机制** · 先识别选择证据与理解证据分别发生的位置，再以能力控制检验干预特异性。

<a id="paper-153831"></a>

## Instruct-Particulate: Scaling Feed-Forward 3D Object Articulation with Kinematic Control

[官方论文页](https://neurips.cc/virtual/2026/poster/153831) · [作者来源](https://openreview.net/forum?id=IOqjhePFzC)

- **问题 / 瓶颈** · 同一网格可按多种粒度拆分，混合异构标注会造成目标歧义。
- **核心创新 / 方法** · 输入网格、零件描述、连接、关节类型及可选点提示，以部分标注扩展训练。
- **Baseline** · 已有三维关节重建网络，具名对照待核实。
- **Benchmark** · 超过十五万个物体，评估跨类别、生成网格和基于图像的资产重建。
- **关键结果 / 消融** · 摘要报告跨分类和生成网格的泛化提升。
- **适用条件 / 局限** · 推理依赖可用的规格；自动生成规格的错误效应待查。

**可复用机制** · 让标注粒度成为显式条件而非数据噪声，并区分规格预测和执行的误差。

<a id="paper-152300"></a>

## Integral Probability Boundaries

[官方论文页](https://neurips.cc/virtual/2026/poster/152300) · [作者来源](https://openreview.net/forum?id=U5cCG37Q3M)

- **问题 / 瓶颈** · 单一最大期望差可能给尾部约束带来宽松或无效界。
- **核心创新 / 方法** · 构建 Integral Probability Boundaries，导出性质并提出多设置估计方法。
- **Baseline** · 基于 Integral Probability Metrics 的界及当时的对照方法。
- **Benchmark** · 对齐、无评委性能估计和生成公平案例，测界宽度与精度。
- **关键结果 / 消融** · 稀有群体公平差距估计在一个生成任务中精确约 15 个百分点。
- **适用条件 / 局限** · 边界构造和尾部样本代价待核实。

**可复用机制** · 按风险区域评估界的紧致性，避免仅凭分布整体差距判断稀有事件风险。

<a id="paper-149201"></a>

## Integrated Imputation-Classification for Supervised Learning with Missing Data

[官方论文页](https://neurips.cc/virtual/2026/poster/149201) · [作者来源](https://openreview.net/forum?id=sAQTY54J7W)

- **问题 / 瓶颈** · 先做逼真补全再分类可能保留了不相关特征。
- **核心创新 / 方法** · 以额外的补全类构造 n+1 类判别器，与补全器用统一分类目标做对抗训练。
- **Baseline** · 经典先补全后分类和生成式基线。
- **Benchmark** · FashionMNIST、CIFAR-10 及自然缺失表格；关注分类鲁棒性与准确率。
- **关键结果 / 消融** · 理论上全局最优时对缺失坐标边缘化并达到 Bayes 分类；实测优于所列基线。
- **适用条件 / 局限** · 理论以全局最优为条件，缺失机制变化和训练稳定性待核实。

**可复用机制** · 用最终决策目标约束补全过程，并与独立补全基线对照，以免把重建质量当成代理。

<a id="paper-149096"></a>

## Integrating digital twins with randomized experiments

[官方论文页](https://neurips.cc/virtual/2026/poster/149096) · [作者来源](https://openreview.net/forum?id=sweF37THPZ)

- **问题 / 瓶颈** · 试验样本和生成样本都可能偏离目标人群。
- **核心创新 / 方法** · 用目标汇总构造校准混合，并将生成的辅助结局预测作为回归精度辅助。
- **Baseline** · 试验样本单独估计以及未经校准的合成协变量。
- **Benchmark** · 理论及模拟，测总体和子群体目标效应的偏差与效率。
- **关键结果 / 消融** · 报告较仅试验估计偏差更低，辅助预测可改善精度而不改变目标估计量。
- **适用条件 / 局限** · 依赖外部目标汇总的质量与代表性，实证迁移待验证。

**可复用机制** · 合成数据仅在通过目标分布约束后提供协变量信息，辅助预测与因果目标分开。

<a id="paper-150760"></a>

## Integrating Local and Global Entropy for Uncertainty Quantification in LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/150760) · [作者来源](https://openreview.net/forum?id=fbOMEeETpt)

- **问题 / 瓶颈** · 只用末层熵漏检高置信整体错误。
- **核心创新 / 方法** · 单次生成提取隐藏表示几何复杂度与 token 熵，通过乘法门组合。
- **Baseline** · 无监督不确定性方法及缺乏跨数据集泛化的监督对照。
- **Benchmark** · 三个基准和三个模型家族，评估错误检测和无监督泛化。
- **关键结果 / 消融** · 报告两类信号弱相关，融合匹配或优于所有所测无监督基线。
- **适用条件 / 局限** · 要求可访问内部表示，两类信号在新领域互补性待验证。

**可复用机制** · 检测置信但错误的样本时，把中间表示与输出不确定性分别消融。

<a id="paper-139337"></a>

## IntegrityBench: Can LLMs Be Trusted as Co-Scientists? A Research Integrity Benchmark

[官方论文页](https://neurips.cc/virtual/2026/poster/139337) · [作者来源](https://openreview.net/forum?id=W5vETfjQkH)

- **问题 / 瓶颈** · 问答合规分数可能掩盖实际研究决策失误。
- **核心创新 / 方法** · 为 misconduct 与合规控制构造配对任务，按压力等级分层并分开评估三种能力。
- **Baseline** · 十八个前沿模型变体及不同推理设置。
- **Benchmark** · 36 组配对覆盖三领域四阶段，关注失误、过度拒绝及产物决策准确率。
- **关键结果 / 消融** · 最高压力下约三分之一关键决策失败；隐性情境变更更多造成误拒，分类成功与产物决策并非一致。
- **适用条件 / 局限** · 压力设置与真实研究工作差异待核实，相关性不能用于推断因果。

**可复用机制** · 同时记录误放与误拒，在匹配任务中检验分类错误是否实际改变处理结果。

<a id="paper-155244"></a>

## Intent2CAD: How Semantic-Parametric Supervision Shapes Text-to-CAD Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/155244) · [作者来源](https://openreview.net/forum?id=7BejwX1V86)

- **问题 / 瓶颈** · 可执行 CAD 程序未必能恢复可复用设计意图。
- **核心创新 / 方法** · 先将可靠的低层原语组提升为特征操作，再显化轻量参数关系，不改架构和解码。
- **Baseline** · 低层结构监督、语义提升和再加参数提升的受控微调。
- **Benchmark** · IntentCAD-100K、IntentCAD-Edit-1K，测 IR、API Recovery 和零样本编辑。
- **关键结果 / 消融** · 语义提升让 IR 从 2.39% 到 0.22%，API Recovery 为 99.96%；参数化主要改善关系编辑。
- **适用条件 / 局限** · 依赖可靠的低层到高层映射，其他语言和几何工具待查。

**可复用机制** · 同时检查程序正确性和可维护结构，比较追加结构标签是否改善编辑而非只改善执行。

<a id="paper-150630"></a>

## Intent-Aware Caching for Efficient LLM Serving

[官方论文页](https://neurips.cc/virtual/2026/poster/150630) · [作者来源](https://openreview.net/forum?id=gebB3q0INK)

- **问题 / 瓶颈** · 相同过去命中行为不等于未来轮次续接时间一致。
- **核心创新 / 方法** · 对请求做意图分类，在线更新按组的复用统计，用于淘汰。
- **Baseline** · LPC 与 LRU。
- **Benchmark** · ShareChat 等真实负载，衡量缓存命中和平均服务延迟。
- **关键结果 / 消融** · 命中率 34.6%，LPC 和 LRU 分别为 18.8%、12.2%；延迟最多下降 54.6%。
- **适用条件 / 局限** · 依赖稳定或能在线追踪的意图组；分类成本、隐私和流量漂移待核实。

**可复用机制** · 把缓存的语义访问模式当作可变条件，并以低开销统计而非静态优先级调度。

<a id="paper-150506"></a>

## Intent Factored Generation: Unleashing the Diversity in Your Language Model

[官方论文页](https://neurips.cc/virtual/2026/poster/150506) · [作者来源](https://openreview.net/forum?id=haufpYkZZz)

- **问题 / 瓶颈** · 只调 token 采样容易得到同一思路的改写。
- **核心创新 / 方法** · 先生成摘要、关键词或分步意图作为锚，再结合原提示生成内容。
- **Baseline** · 直接采样和验证反馈强化学习的组合设置。
- **Benchmark** · 数学、代码、指令生成和语言建模，比较探索、效果与语义多样性。
- **关键结果 / 消融** · 报告与验证反馈组合有效，且在多个任务保持质量并增加多样性。
- **适用条件 / 局限** · 额外输出计算量及意图错误导致的锚定待核实。

**可复用机制** · 用两种采样温度控制概念覆盖与文本一致性，并与相同预算直接采样对照。

<a id="paper-155579"></a>

## Interaction-Aligned Robot Learning from Human Videos with Structured Graph Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/155579) · [作者来源](https://openreview.net/forum?id=4ZFPxw5n09)

- **问题 / 瓶颈** · 人机表示失配使轨迹模仿无法共享物理互动知识。
- **核心创新 / 方法** · 通过跟踪、手姿态映射和点云建统一表示，用图注意力编码交互，再做离散抽象和层次分布对齐。
- **Baseline** · 既有人类视频迁移及机器人示范方法，具名待核实。
- **Benchmark** · RLBench、ManiSkill2 和真机，少示范、仅人类视频和组件消融。
- **关键结果 / 消融** · 报告少示范下的收益，并展示仅人视频训练的零样本迁移。
- **适用条件 / 局限** · 复杂接触下映射误差和零样本任务覆盖待核实。

**可复用机制** · 对齐交互实体及关系后再做跨本体迁移，并分开测人手追踪与技术迁移所贡献的收益。

<a id="paper-148672"></a>

## Interaction Value Inference for Multi-Agent Reinforcement Learning via a Hierarchical Agent-Centric World Model

[官方论文页](https://neurips.cc/virtual/2026/poster/148672) · [作者来源](https://openreview.net/forum?id=vxZDvmWQyz)

- **问题 / 瓶颈** · 局部效用难反映合作依赖。
- **核心创新 / 方法** · 用带角色的 Transformer 世界模型预测队友行为，把预测转成辅助交互效用。
- **Baseline** · 集中训练去中心执行方法，具体名称待核。
- **Benchmark** · SMAC 和 SMACv2，比较团队表现。
- **关键结果 / 消融** · 摘要报告超过强基线。
- **适用条件 / 局限** · 队友预测错配及其他任务迁移待核。

**可复用机制** · 在固定局部价值架构下单独消融队友行为与效用转换。

<a id="paper-155706"></a>

## Interactive 4D Volumetric Liquid Forecasting under Moving-Solid Interaction

[官方论文页](https://neurips.cc/virtual/2026/poster/155706) · [作者来源](https://openreview.net/forum?id=3Xq2VKLpwE)

- **问题 / 瓶颈** · 局部扰动驱动长程全域场，直接滚动易累积误差。
- **核心创新 / 方法** · TIDE 做局部界面预测，TIDES 加传播耦合与显式稳定。
- **Baseline** · 从相邻任务适配的方法及组件消融。
- **Benchmark** · 稠密三维液体速度滚动，测试物体运动、尺度分布外与长时预测。
- **关键结果 / 消融** · 摘要称 TIDES 最优，三组件各有贡献。
- **适用条件 / 局限** · 依赖运动条件，真实数据验证待核。

**可复用机制** · 在其他局部激励的物理场预测中分开评价近界面与远场误差。

<a id="paper-155091"></a>

## Interactive Combinatorial Reinforcement Learning for Knowledge Graph Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/155091) · [作者来源](https://openreview.net/forum?id=8Vo01NLzG6)

- **问题 / 瓶颈** · 自由探索产生大量图上不存在的关系路径。
- **核心创新 / 方法** · 检索查询相关候选关系，限定组合路径空间，再用分阶段反馈做 GRPO。
- **Baseline** · 自由形式滚动与已有知识图谱问答；名称待核。
- **Benchmark** · 多个 KGQA 数据集；指标待核。
- **关键结果 / 消融** · 摘要称约束搜索能改善训练和问答。
- **适用条件 / 局限** · 候选召回低时会删掉正确路径。

**可复用机制** · 分别记录可执行率、答案正确率和候选召回，定位约束造成的损益。

<a id="paper-148176"></a>

## Inter-Agent Influence: Evaluating Persuasion, Deception and Coercion in Multi-Agent Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/148176) · [作者来源](https://openreview.net/forum?id=ziYeGq8OOt)

- **问题 / 瓶颈** · 单轮拒绝率可能高估系统对影响的稳健性。
- **核心创新 / 方法** · 比较多个模拟工作流下互动前后的审核与协商行为。
- **Baseline** · 初始决策和多种前沿模型。
- **Benchmark** · 五个环境，比较决策变化与风险行为。
- **关键结果 / 消融** · 摘要报告多模型出现违规审核翻转，胁迫类证据较弱。
- **适用条件 / 局限** · 实验条件与自然部署的可比性待核。

**可复用机制** · 用受控无害用例审计审批规则在交互后是否仍一致。

<a id="paper-151321"></a>

## Inter-domain Inference for Gaussian Process Variational Autoencoders

[官方论文页](https://neurips.cc/virtual/2026/poster/151321) · [作者来源](https://openreview.net/forum?id=bNAgSziur6)

- **问题 / 瓶颈** · 诱导点局限于输入域的点值，难表达算子结构。
- **核心创新 / 方法** · 改用潜高斯过程的线性泛函，傅里叶捕捉谱相关，样条诱导带状协方差。
- **Baseline** · 标准诱导点 GPVAE。
- **Benchmark** · 表示学习、缺失值插补与条件生成。
- **关键结果 / 消融** · 摘要报告精度效率折中有竞争力。
- **适用条件 / 局限** · 依赖泛函和核的计算可行性。

**可复用机制** · 在相同诱导预算下按全局频率与局部性选择特征，并比较求解开销。

<a id="paper-154807"></a>

## Interleaved Head Attention

[官方论文页](https://neurips.cc/virtual/2026/poster/154807) · [作者来源](https://openreview.net/forum?id=AoSjvxQp5K)

- **问题 / 瓶颈** · 独立注意矩阵让关系组合主要靠增加深度。
- **核心创新 / 方法** · 伪查询、键和值由所有原头线性混合，令每头出现更多交互模式。
- **Baseline** · 多头注意力与全注意。
- **Benchmark** · Polynomial Filters、CPM-3 理论，RULER、GSM8K、MATH-500 实证。
- **关键结果 / 消融** · RULER 多键检索改善 10%–20%；数学评测亦有提升。
- **适用条件 / 局限** · 吞吐与长上下文代价需按实现复核。

**可复用机制** · 对照同预算加头、加层与层内混合，单列组合任务效率。

<a id="paper-154542"></a>

## Interleaved Latent Thinking and Adaptive Termination for Efficient Reasoning LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/154542) · [作者来源](https://openreview.net/forum?id=Co9TkIuLP9)

- **问题 / 瓶颈** · 纯潜词元会放大不确定性，刚性停止容易过早或过晚。
- **核心创新 / 方法** · 冻结语言模型，强化学习训练轻量门以交替显式和潜词元，并累计退出概率。
- **Baseline** · 显式思维链和已有潜推理。
- **Benchmark** · 多模型大小及推理评测；准确率和词元消耗。
- **关键结果 / 消融** · 摘要称准确率约增 3%，词元最多减 40%。
- **适用条件 / 局限** · 潜步骤的真实计算量和退出校准待核。

**可复用机制** · 在同实际计算预算下拆分门控与停止策略的收益。

<a id="paper-139056"></a>

## Internal Evaluation of Unsupervised Anomaly Detection Algorithms with Explanation

[官方论文页](https://neurips.cc/virtual/2026/poster/139056) · [作者来源](https://openreview.net/forum?id=nph44qznwG)

- **问题 / 瓶颈** · 无标注条件下仅看异常分数分布缺少可解释性。
- **核心创新 / 方法** · SSSD 用邻近分数和邻近距离识别局部平滑性违例。
- **Baseline** · 分数分布内评估与辅助分类器路线。
- **Benchmark** · 人工和真实数据集；对照无监督检测评估。
- **关键结果 / 消融** · 摘要报告跨数据设置有效且稳健。
- **适用条件 / 局限** · 依赖输入度量和局部平滑假设，真实异常边界也可能违例。

**可复用机制** · 将邻域违例用于抽样复核，避免直接当成误标真值。

<a id="paper-149907"></a>

## Internalize External Competence for Visual Instruction Editing

[官方论文页](https://neurips.cc/virtual/2026/poster/149907) · [作者来源](https://openreview.net/forum?id=mKfQzVpQIM)

- **问题 / 瓶颈** · 在线串联增加延迟和跨模型错误。
- **核心创新 / 方法** · 由视觉模型合成配对监督，以 LoRA 让扩散编辑器识别图中指示。
- **Baseline** · 纯文本编辑与在线视觉规划器辅助。
- **Benchmark** · 多个扩散架构，空间控制、指令遵循与标记移除。
- **关键结果 / 消融** · 摘要称改善对照且接近辅助流程效果，无额外规划延迟。
- **适用条件 / 局限** · 图上文字适合短标签，复杂语言仍靠文本输入。

**可复用机制** · 同任务匹配采样成本，比较配对蒸馏和保留在线规划。

<a id="paper-148657"></a>

## Internal Safety Collapse in Frontier Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148657) · [作者来源](https://openreview.net/forum?id=w7YzZDE3Ei)

- **问题 / 瓶颈** · 表面正常的流程也可能在内部产生不合规的中间结果。
- **核心创新 / 方法** · 作者在多学科受控评测中分别检查任务完成与安全表现。
- **Baseline** · 四个前沿模型与三种交互条件。
- **Benchmark** · 53 个受控流程、八个学科，测安全失败率。
- **关键结果 / 消融** · 最差条件下模型平均安全失败率为 95.3%。
- **适用条件 / 局限** · 结果限所测流程，跨系统的失效率不能直接外推。

**可复用机制** · 验收时以无害替代数据检查端到端审核点，并分别看中间状态与输出。

<a id="paper-152947"></a>

## Intern-Atlas: A Methodological Evolution Graph as Research Infrastructure for AI Scientists

[官方论文页](https://neurips.cc/virtual/2026/poster/152947) · [作者来源](https://openreview.net/forum?id=PBFQonL9J2)

- **问题 / 瓶颈** · 文献级引用不能说明改进了哪个部件或解决什么限制。
- **核心创新 / 方法** · 提取方法实体和带类型的谱系边，以时间搜索生成可核验的沿革链。
- **Baseline** · 普通篇级引文图为结构对照，命名基线待核。
- **Benchmark** · 逾百万论文、逾九百万关系，使用专家沿革链验证。
- **关键结果 / 消融** · 摘要称与专家链较一致。
- **适用条件 / 局限** · 自动抽取关系并非因果证明，领域覆盖与误链率待核。

**可复用机制** · 以原文证据抽审每条演化边，分别测谱系顺序与瓶颈归因。

<a id="paper-150129"></a>

## Interpretability-by-Design with Accurate Locally Additive Models and Conditional Feature Effects

[官方论文页](https://neurips.cc/virtual/2026/poster/150129) · [作者来源](https://openreview.net/forum?id=kTrJguvQVX)

- **问题 / 瓶颈** · 全局加性欠拟合，显式二维交互增加审计复杂度。
- **核心创新 / 方法** · 用简单逻辑阈值切分邻域，以蒸馏选交互有限区域并做区域回拟合。
- **Baseline** · GAM 和含成对交互的 GA²M。
- **Benchmark** · 多种分类和回归，比较准确性及局部解释。
- **关键结果 / 消融** · 摘要报告优于 GAM，接近 GA²M。
- **适用条件 / 局限** · 区域越多越难审计，规模与阈值稳定性待核。

**可复用机制** · 同解释预算对照区域加性和成对交互，抽查跨区域连续性。

<a id="paper-154045"></a>

## Interpretable but Fragile? Robustness of Concept Bottlenecks under Geometric-Semantic Perturbations

[官方论文页](https://neurips.cc/virtual/2026/poster/154045) · [作者来源](https://openreview.net/forum?id=GckHR5gDV2)

- **问题 / 瓶颈** · 混合扰动和鲁棒定义会导致矛盾结论。
- **核心创新 / 方法** · 生成式控制两类扰动，测预测及概念敏感度，并用随机平滑验证。
- **Baseline** · 标准分类器及概念瓶颈模型。
- **Benchmark** · CUB-200-2011 和 RIVAL-10 变体，控制语义相似性与概念数。
- **关键结果 / 消融** · 解释结构改变敏感度的位置和方式，收益依赖扰动和任务。
- **适用条件 / 局限** · 生成扰动与现实环境的对应待核。

**可复用机制** · 固定任务分布，分开报告预测与概念级经验、认证鲁棒性。

<a id="paper-155490"></a>

## Interpretable Multiway-Split Trees

[官方论文页](https://neurips.cc/virtual/2026/poster/155490) · [作者来源](https://openreview.net/forum?id=5CCv49ib3F)

- **问题 / 瓶颈** · 二叉树可为表达单条规则变得很深，多路划分又组合爆炸。
- **核心创新 / 方法** · 用动态规划和分支定界筛选候选，并近似枚举近优树。
- **Baseline** · 贪心多路与近优二叉树。
- **Benchmark** · 分类数据，比较准确性、路径长度和训练成本。
- **关键结果 / 消融** · 摘要报告更短路径下有更高准确率。
- **适用条件 / 局限** · 节点划分复杂度仍随分箱数改变。

**可复用机制** · 在匹配精度下比较路径长度与训练时间，再人工抽查近优备选。

<a id="paper-154449"></a>

## Interpretable Relational Inference with LLM-Guided Symbolic Dynamics Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/154449) · [作者来源](https://openreview.net/forum?id=DTEngzO4Ry)

- **问题 / 瓶颈** · 固定已知图或符号库限制结构发现。
- **核心创新 / 方法** · 联合学习稀疏符号表达与图，并用外层反馈筛选候选表达。
- **Baseline** · 黑盒图代理和已知拓扑的符号回归。
- **Benchmark** · 合成和真实动力学，比较结构恢复与表达紧凑性。
- **关键结果 / 消融** · 摘要称恢复稳健、表达和机制相符。
- **适用条件 / 局限** · 需观测条件支持可识别性，实证不必然代表因果发现。

**可复用机制** · 在良性机械振子上对照固定候选库和反馈调整，分开测边恢复与预测。

<a id="paper-155074"></a>

## Interpreting Neural Combinatorial Optimization via Evolving Programmatic Bottlenecks

[官方论文页](https://neurips.cc/virtual/2026/poster/155074) · [作者来源](https://openreview.net/forum?id=8fI7m5Dxno)

- **问题 / 瓶颈** · 固定概念瓶颈难覆盖动态组合优化决策。
- **核心创新 / 方法** · 在良性优化任务中以可读程序作为瓶颈，通过局部分析增补缺失策略、移除冗余。
- **Baseline** · 概念瓶颈与被解释的神经组合求解器。
- **Benchmark** · 多种组合优化实验，比较保真度并分析阶段差别。
- **关键结果 / 消融** · 摘要称策略组合多数情况下接近原模型，并发现阶段行为转换。
- **适用条件 / 局限** · 学生拟合逼真也不能证明源模型使用同一机制。

**可复用机制** · 按优化阶段测蒸馏保真度，防止总成绩掩盖特定阶段行为差异。

<a id="paper-154529"></a>

## Intersectional Fairness via Mixed-Integer Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/154529) · [作者来源](https://openreview.net/forum?id=CvEVWYfVb5)

- **问题 / 瓶颈** · 单一属性的公平度可能掩盖小交叉群体受损。
- **核心创新 / 方法** · 用混合整数优化寻最坏子群并训练带偏差界的可解释分类器，证明两种指标识别等效。
- **Baseline** · MSD、SPSF 与现有偏差检测方法。
- **Benchmark** · 摘要报告在高风险分类数据中比较偏差寻找与分类；集名待核。
- **关键结果 / 消融** · 报告改善偏差检测，并令分类器交叉偏差低于设定阈值。
- **适用条件 / 局限** · 细分组样本量和优化成本需审计。

**可复用机制** · 固定可解释性约束，检查多个交叉群体与总体准确率的折中。

<a id="paper-154481"></a>

## Intervene3D: Intervention-Based Controlled Inference for Multimodal Perception under Partial Observability

[官方论文页](https://neurips.cc/virtual/2026/poster/154481) · [作者来源](https://openreview.net/forum?id=DGYMQ4bD4b)

- **问题 / 瓶颈** · 遮挡、稀疏和失准下，普通融合检测器无法控制外部先验的影响。
- **核心创新 / 方法** · 用预测不确定性定义 BEV 信赖域，以少量投影步降低数量和空间约束能量。
- **Baseline** · 无约束的 BEV 融合检测；具体基线待核实。
- **Benchmark** · 严重度扫描；鲁棒性 AUC、约束可行性、冲突假阳性。
- **关键结果 / 消融** · 摘要列诊断指标，未给出结果数值。
- **适用条件 / 局限** · 错误外部约束仍可能产生偏差，依赖不确定性校准。

**可复用机制** · 给证据强弱不同的特征不同更新半径，同时报告有冲突时的异常行为。

<a id="paper-148473"></a>

## Intervention-Guided Image-Free Classifier Expansion for Fine-Grained Recognition

[官方论文页](https://neurips.cc/virtual/2026/poster/148473) · [作者来源](https://openreview.net/forum?id=xXksVKeYKi)

- **问题 / 瓶颈** · 细粒度类别描述中的共现属性压过判别属性。
- **核心创新 / 方法** · 先比较类别拆分两类属性，再合成干预语义以约束权重生成。
- **Baseline** · 传统语义到权重的关联映射。
- **Benchmark** · 细粒度无图零样本分类；数据名待核实。
- **关键结果 / 消融** · 摘要报告超过既有方法，边界更清晰。
- **适用条件 / 局限** · 依赖属性分解质量与语义是否覆盖真实类间差异。

**可复用机制** · 针对判别属性生成人工反事实约束，而非从所有语义共现直接读出分类器。

<a id="paper-154546"></a>

## interwhen: A Generalizable Framework for Steering Reasoning Models with Test-time Verification

[官方论文页](https://neurips.cc/virtual/2026/poster/154546) · [作者来源](https://openreview.net/forum?id=Cl5QbTUZrf)

- **问题 / 瓶颈** · 末端验证错过早期错误，多分支搜索又贵。
- **核心创新 / 方法** · 周期性短程分叉抽取状态，由异步验证器处理，仅在违规时反馈；可从政策文本生成验证器。
- **Baseline** · 仅终点验证与分支验证。
- **Benchmark** · 数学逻辑及 tau²-bench 代理任务。
- **关键结果 / 消融** · Qwen3-30B 电信任务完成率报告从 32% 到 87%。
- **适用条件 / 局限** · 自然语言政策能否被忠实形式化需另验。

**可复用机制** · 将状态抽取和验证与主推理并行，避免每次正确推理都支付同步等待成本。

<a id="paper-149125"></a>

## Intra-Option Fitted Q-Evaluation: Evaluating Hierarchical Policies from Non-Hierarchical Data

[官方论文页](https://neurips.cc/virtual/2026/poster/149125) · [作者来源](https://openreview.net/forum?id=shxhGfhWBq)

- **问题 / 瓶颈** · 平坦 FQE 忽略选项持续性，选项级重要性采样又需标注。
- **核心创新 / 方法** · 将选项纳入价值的自变量，利用未标选项的基础动作数据实现 IO-FQE。
- **Baseline** · 朴素 FQE 与选项级重要性采样。
- **Benchmark** · AntMaze、OGBench Puzzle；价值偏差及均方误差。
- **关键结果 / 消融** · 摘要报告消除朴素方法偏差，并比重要性采样显著降误差。
- **适用条件 / 局限** · 需给定待评估策略的选项定义和终止，离线覆盖限制待核实。

**可复用机制** · 保留决定未来分布的持续控制状态，即使日志未显式记录该层标签。

<a id="paper-152659"></a>

## Intrinsically Interpretable Attention via Sparse Post-Training

[官方论文页](https://neurips.cc/virtual/2026/poster/152659) · [作者来源](https://openreview.net/forum?id=RMkXEqB3sY)

- **问题 / 瓶颈** · 普通稀疏方法面向速度，不直接验证电路是否更容易解释。
- **核心创新 / 方法** · 给注意力连通施加稀疏正则，同时约束预训练损失。
- **Baseline** · 原始稠密模型及任务电路分析。
- **Benchmark** · 最高 7B 模型；损失、边数、跨层转码器归因。
- **关键结果 / 消融** · 报告注意边余约 0.4%，电路边最多减少百倍。
- **适用条件 / 局限** · 保留损失不保证所有罕见能力持平，也不等于实测加速。

**可复用机制** · 将稀疏性设为可解释结构约束，并同时验证宏观能力和电路规模。

<a id="paper-148546"></a>

## Intrinsic-dimension empirical Bernstein inequalities for bounded self-adjoint operators

[官方论文页](https://neurips.cc/virtual/2026/poster/148546) · [作者来源](https://openreview.net/forum?id=x4akadcHLx)

- **问题 / 瓶颈** · 未知真方差和高维系数可能让界不可计算或过宽。
- **核心创新 / 方法** · 用经验方差估计导出独立有界紧自伴算子的 Bennett 和 Bernstein 界。
- **Baseline** · 依赖真实方差的 oracle 界。
- **Benchmark** · 理论比较非各向同性随机矩阵和无限维 Hilbert 空间。
- **关键结果 / 消融** · 报告渐近可达到已知 oracle 速率。
- **适用条件 / 局限** · 依赖独立、有界及所用算子条件。

**可复用机制** · 对有谱集中结构的估计量，先用数据测有效维数再计算误差界。

<a id="paper-155566"></a>

## Intrinsic Information Theoretic Analysis of ReLU Nets

[官方论文页](https://neurips.cc/virtual/2026/poster/155566) · [作者来源](https://openreview.net/forum?id=4dnKZPefBt)

- **问题 / 瓶颈** · 外部分桶、核宽或邻域选择会主导高维互信息估计。
- **核心创新 / 方法** · 从分段线性网络取区域标签，用插件估计读出路由信息；饱和时以函数等价合并区域。
- **Baseline** · 三种互信息估计基线。
- **Benchmark** · 分段线性表示的相关性和分区饱和实验。
- **关键结果 / 消融** · 原始估计无需外部超参且与基线高度相关；合并可恢复饱和时信息。
- **适用条件 / 局限** · 函数合并需要容差，纯路由量不等同完整互信息。

**可复用机制** · 优先利用模型天然离散结构，避免人为量化几何决定信息结论。

<a id="paper-148345"></a>

## Intrinsic Muon: Spectral Optimization on Riemannian Matrix Manifolds

[官方论文页](https://neurips.cc/virtual/2026/poster/148345) · [作者来源](https://openreview.net/forum?id=yYWccp8wIs)

- **问题 / 瓶颈** · 直接加切空间约束的 Muon 可能破坏商空间对称并失去闭式更新。
- **核心创新 / 方法** · 从黎曼度量提升酉不变范数，在其约束下做线性最大化。
- **Baseline** · 环境空间或朴素切空间 Muon。
- **Benchmark** · LoRA、图像分类和子空间学习；固定秩、SPD、Stiefel、Grassmann 分析。
- **关键结果 / 消融** · 所列流形给闭式更新；固定秩的速率常数只依赖秩而非因子条件。
- **适用条件 / 局限** · 结论依赖所定义流形和度量。

**可复用机制** · 先用约束自身的几何定义可比较步长，再移植谱更新。

<a id="paper-152274"></a>

## Intrinsic-Preserving Schrödinger Bridge for Direct Part-Aware 3D Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/152274) · [作者来源](https://openreview.net/forum?id=UIvwoPccJx)

- **问题 / 瓶颈** · 对称跨模态约束可能既破坏语义对齐又限制目标结构。
- **核心创新 / 方法** · 建立对应的层级部件图，用非对称关系正则约束桥接，仅重采样目标部件轨迹。
- **Baseline** · CFG 和已有 Schrödinger bridge 生成。
- **Benchmark** · 部件级三维生成和编辑；具体指标待核实。
- **关键结果 / 消融** · 摘要报告无需整物重生成即可修改目标部件。
- **适用条件 / 局限** · 依赖部件拓扑及对应可靠。

**可复用机制** · 将应保持的部件轨迹冻结，把编辑的自由度局限于被选中的结构节点。

<a id="paper-148988"></a>

## Intrinsic Riemannian Cross-covariance for Manifold-valued Random Objects

[官方论文页](https://neurips.cc/virtual/2026/poster/148988) · [作者来源](https://openreview.net/forum?id=teJdXSWBH8)

- **问题 / 瓶颈** · 直接对不同局部坐标的变化做交叉协方差不具坐标独立性。
- **核心创新 / 方法** · 用平行移动将局部变化表达在公共切空间，定义交叉协方差及相关。
- **Baseline** · 传统欧氏协方差。
- **Benchmark** · 球面、SPD 与 Kendall 形状空间的数值及真实形状实验。
- **关键结果 / 消融** · 摘要报告继承部分欧氏性质并给出渐近刻画。
- **适用条件 / 局限** · 依赖所选流形几何及传输定义，具体唯一性条件待核实。

**可复用机制** · 共变分析前先对齐比较变化量的几何参考，分离坐标差和真实相关。

<a id="paper-149807"></a>

## Intrinsic Selection and Particle Resampling for Inference-Time Scaling Beyond Domain Verifiability

[官方论文页](https://neurips.cc/virtual/2026/poster/149807) · [作者来源](https://openreview.net/forum?id=nCaIsLevLx)

- **问题 / 瓶颈** · 固定采样预算与共识排序难应对系统性错假设。
- **核心创新 / 方法** · 使用长度校正尾熵先作难度门控，再选最终候选或逐步粒子重采样。
- **Baseline** · pass@1、共识选择及依赖外部验证的路线。
- **Benchmark** · 工程设计、困难数学和临床回应量表。
- **关键结果 / 消融** · 工程选择报告较 pass@1 提高 20%；困难数学平均提高 6.1 点。
- **适用条件 / 局限** · 模型自信不保证正确，特别是系统错误时；部分扩展需要特权指导。

**可复用机制** · 先验证内部信号能否稳定排序，再让不确定样本获得额外算力。

<a id="paper-154036"></a>

## Introspective Coupling: LMs Learn to Explain Themselves Better Than Their Training Targets

[官方论文页](https://neurips.cc/virtual/2026/poster/154036) · [作者来源](https://openreview.net/forum?id=GgruvAw5m1)

- **问题 / 瓶颈** · 模仿外部解释并不天然产生对自身行为真实的解释。
- **核心创新 / 方法** · 改变解释训练目标与学习中行为的一致度，同时追踪训练内行为变动后的解释。
- **Baseline** · 更不相容的解释目标、不同强度监督及行为位移条件。
- **Benchmark** · 迎合、拒答等多个行为任务和标签噪声设置。
- **关键结果 / 消融** · 解释可更忠实于当前模型而非原监督目标，且在部分行为变化下仍跟随。
- **适用条件 / 局限** · 要求训练期间保持足够相容性，不能保证普遍自省。

**可复用机制** · 评估解释忠实时，用模型自己的行为变化做对照，而非仅对齐标注来源。

<a id="paper-152764"></a>

## Invaria: Learning Scale and Density Invariance in Point Clouds via Next-Resolution Prediction

[官方论文页](https://neurips.cc/virtual/2026/poster/152764) · [作者来源](https://openreview.net/forum?id=QYAtNtsZ3S)

- **问题 / 瓶颈** · 编码器对点密度和物体尺度变化敏感。
- **核心创新 / 方法** · 把下一分辨率预测作为训练目标，并校准感受野。
- **Baseline** · 既有三维点云编码器。
- **Benchmark** · ScanNet，三倍降分辨率和三倍缩尺度的 mIoU。
- **关键结果 / 消融** · 报告前者 mIoU 相对高 56%，后者改善 20%。
- **适用条件 / 局限** · 不同真实传感退化或非均匀密度仍需另验。

**可复用机制** · 用重采样后的同一结构做迁移监督，而非单一网格密度上的重建。

<a id="paper-154396"></a>

## Invariance and Body-Order Compose Additively: Minimax Rates on $\mathrm{SO}(3)^n$

[官方论文页](https://neurips.cc/virtual/2026/poster/154396) · [作者来源](https://openreview.net/forum?id=DtDqsME3PW)

- **问题 / 瓶颈** · 两种结构先验改善样本复杂度的机制难区分。
- **核心创新 / 方法** · 对旋转群积空间的四类函数给配套 minimax 界，并样本划分选体阶。
- **Baseline** · 有无全局不变与有无体阶截断的四类估计。
- **Benchmark** · 五项谱估计实验，含 Maier–Saupe。
- **关键结果 / 消融** · 有效维数分别减少 3 和 3(n-K)，报告部分实验有 2 至 17 倍样本效率。
- **适用条件 / 局限** · 受所分析群作用、平滑条件及截断类别限制。

**可复用机制** · 用群对称减少共同自由度，再检验目标是否仅需有限交互阶数。

<a id="paper-152361"></a>

## Invariant Features in Language Models: Geometric Characterization and Model Attribution

[官方论文页](https://neurips.cc/virtual/2026/poster/152361) · [作者来源](https://openreview.net/forum?id=TdITA4NH7Z)

- **问题 / 瓶颈** · 直接测表征距离会将改写和真实语义变化混合。
- **核心创新 / 方法** · 对比同义与异义输入的局部位移，分离形式扰动方向，再干预验证。
- **Baseline** · 不同模型、层与表示对照；具体待核实。
- **Benchmark** · 释义不变、语义位移与零样本模型归因。
- **关键结果 / 消融** · 语义改变量多落在形式扰动子空间外，部分层出现稳定结构。
- **适用条件 / 局限** · 依赖释义构造和局部几何范围。

**可复用机制** · 先估计只反映语言表达变化的方向，再测模型是否真正保留语义。

<a id="paper-152389"></a>

## Invariant Hyperbolic Unfolding: Radial Canonicalization for Label-Free Cross-Graph Link Prediction

[官方论文页](https://neurips.cc/virtual/2026/poster/152389) · [作者来源](https://openreview.net/forum?id=TTSdpjkgcF)

- **问题 / 瓶颈** · 学出半径虽可拟合图内层级，却难跨图比较。
- **核心创新 / 方法** · 按 coreness 等结构分数排名确定半径，仍学习角向表示。
- **Baseline** · 配对的冻结双曲编码器。
- **Benchmark** · 无目标标签、保留目标拓扑的跨图链路预测；HR@50。
- **关键结果 / 消融** · 比最强匹配基线高 2.7 个百分点，低度和缺边时优势增大。
- **适用条件 / 局限** · 需要目标拓扑且结构分数含良好层级信号。

**可复用机制** · 将跨域可比的秩当成固定坐标，留下其余维度学习域内差异。

<a id="paper-149017"></a>

## Inverse Linear Bandits via Linear Programs

[官方论文页](https://neurips.cc/virtual/2026/poster/149017) · [作者来源](https://openreview.net/forum?id=tSF5baGOM3)

- **问题 / 瓶颈** · 只观察单条行动序列，隐藏状态和超参无法访问。
- **核心创新 / 方法** · 刻画被选动作的置信区间并转成线性程序估计奖励。
- **Baseline** · 针对 Phased Elimination 的已有估计器。
- **Benchmark** · LinUCB 与 Phased Elimination 的合成和真实构造记录。
- **关键结果 / 消融** · 误差匹配信息下界至多项式因子，摘要报告较好实证。
- **适用条件 / 局限** · 假设随机线性 bandit、知晓算法族及动作特征。

**可复用机制** · 若能刻画示范者的决策约束，就优先拟合这些约束而非假定观察到真实奖励。

<a id="paper-153595"></a>

## Inverse Modeling of Neural Recordings via Differentiable Biophysical Simulation

[官方论文页](https://neurips.cc/virtual/2026/poster/153595) · [作者来源](https://openreview.net/forum?id=KFA1usL2kP)

- **问题 / 瓶颈** · 阈下区域的损失近乎平坦，阈值突跳破坏端到端梯度。
- **核心创新 / 方法** · 联合拟合细胞外信号和已观测尖峰时间，使事件级监督通过模拟向前因回传。
- **Baseline** · 依赖低维摘要或黑盒潜变量的逆推路线。
- **Benchmark** · 配对 patch-clamp 与 Neuropixels SPE-1；定位和活动场。
- **关键结果 / 消融** · 摘要报告被配对神经元平均定位误差在 40 微米以内。
- **适用条件 / 局限** · 依赖尖峰排序及生物物理与电极模型质量。

**可复用机制** · 对难以从连续误差学到的阈值过程，加可测事件锚点提供跨时域监督。

<a id="paper-149272"></a>

## Inverse Reinforcement Learning with Just Classification and a Few Regressions

[官方论文页](https://neurips.cc/virtual/2026/poster/149272) · [作者来源](https://openreview.net/forum?id=rZaXY04Gvf)

- **问题 / 瓶颈** · 最大熵策略可由多个奖励与价值对产生，奖励只部分可识别。
- **核心创新 / 方法** · 在一般状态级仿射约束下估计策略，再用 Bellman 方程做拟合 Q 评估并恢复奖励。
- **Baseline** · DeepPQR 和锚定动作规范化。
- **Benchmark** · 示范奖励恢复，考察奖励误差及有限样本分解。
- **关键结果 / 消融** · 作者报告奖励恢复优于 DeepPQR，理论界分别计入策略和价值误差。
- **适用条件 / 局限** · 归一化决定恢复的是哪个奖励，非最大熵假设和实测场景待核实。

**可复用机制** · 将策略估计、值评估、奖励识别分成可替换模块，分别验证误差来源。

<a id="paper-154602"></a>

## Inverted Detection and Control in Steering Vectors

[官方论文页](https://neurips.cc/virtual/2026/poster/154602) · [作者来源](https://openreview.net/forum?id=CO7o8sDgso)

- **问题 / 瓶颈** · 正例可解码方向也可能促成反向行为。
- **核心创新 / 方法** · 分析下游判别头在干预后的表示移动，筛查需要翻转符号的向量。
- **Baseline** · 基于检测方向的 Inference Time Intervention。
- **Benchmark** · Gemma 3 12B、Qwen 2.5 14B、Olmo 3 7B 和五种概念。
- **关键结果 / 消融** · 30 项实验中有 27 项改善，作者所报幅度为 +0.9% 到 +138%。
- **适用条件 / 局限** · 概念、问题与干预层变化下的效果待核实。

**可复用机制** · 在信任线性检测方向之前做控制符号验证，并保留未翻转对照。

<a id="paper-153997"></a>

## Invertible Logits Transformation for Accuracy-Preserving Post-Hoc Uncertainty Calibration

[官方论文页](https://neurips.cc/virtual/2026/poster/153997) · [作者来源](https://openreview.net/forum?id=GywVajmdc3)

- **问题 / 瓶颈** · 温度缩放不够灵活，按类参数随类别数增长或改变排序。
- **核心创新 / 方法** · 对每个 logit 用同一个标量 MLP，再以配对逆网络软约束单调性。
- **Baseline** · 温度缩放、其他事后校准和数值积分型单调方法。
- **Benchmark** · 图像分类标准基准与多个骨干，比较分类准确率和校准指标。
- **关键结果 / 消融** · 作者报告所有实测设置保持准确率，校准优于广泛对照。
- **适用条件 / 局限** · 单调性是软约束；保持准确率不自动保证完全相同的逐样本分类。

**可复用机制** · 分别报告校准误差、预测改变比例和类别数扩展成本。

<a id="paper-153840"></a>

## Inverting the Bellman Equation: From $Q$-Values to World Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153840) · [作者来源](https://openreview.net/forum?id=ILIYkAejvy)

- **问题 / 瓶颈** · 模型无关价值函数表面上不提供显式动力学。
- **核心创新 / 方法** · 利用丰富奖励族的 Bellman 关系约束转移核，用 P-learning 从价值与奖励抽取环境模型。
- **Baseline** · 常规模型无关价值学习与真实动力学参照。
- **Benchmark** · 随机 FourRooms、MountainCar、Reacher，评估动力学和未见目标策略。
- **关键结果 / 消融** · 有限确定状态下单个通用目标即可识别；随机环境所需目标取决于奖励族，实测小规模稀疏目标也能提取有用动力学。
- **适用条件 / 局限** · 需要足够准确的 Q 和目标覆盖，随机情形假设更强。

**可复用机制** · 先用未训练目标验证提取模型是否包含可规划的动力学，而非只复现训练奖励。

<a id="paper-152321"></a>

## Invisible Ink, Visible Lies: How Production Watermarking Causes LLMs to Hallucinate

[官方论文页](https://neurips.cc/virtual/2026/poster/152321) · [作者来源](https://openreview.net/forum?id=TwmIdwMjZ8)

- **问题 / 瓶颈** · 水印可保持流畅度却引入事实错误。
- **核心创新 / 方法** · 在受控 RAG 比较未加和加水印生成，并评估用于保持事实的 token 与注意力干预。
- **Baseline** · KGW、SWEET、DiPmark、Gumbel 系列及 SynthID 风格水印。
- **Benchmark** · 上下文已有证据的配对生成，测事实错误、流畅和解码效率。
- **关键结果 / 消融** · 摘要报告两类干预组合缓解约九成所测水印诱发错误，流畅度和效率相近。
- **适用条件 / 局限** · 依赖上下文含证据；对检测率和跨模型稳健性的边界待核实。

**可复用机制** · 部署验收时把事实保持、可检出性和效率作为独立指标，定位误差是即时还是由前缀积累。

<a id="paper-153721"></a>

## I-PTC: Interactive Programmatic Tool Calling for Stateful Tool-Augmented Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/153721) · [作者来源](https://openreview.net/forum?id=JGKsz3cGPf)

- **问题 / 瓶颈** · 无状态模式反复传入中间结果，难处理跟进和暂态故障。
- **核心创新 / 方法** · 以执行代码片段调用工具，保留可复用状态并以更正更新工具接口。
- **Baseline** · 传统逐次工具调用和原始无状态 PTC。
- **Benchmark** · PTC-BENCH，大初始状态、多次依赖交互和故障恢复；测任务表现与 token。
- **关键结果 / 消融** · 摘要报告复杂任务表现改善及大幅 token 节省。
- **适用条件 / 局限** · 执行状态的一致性、权限边界和容错成本需查。

**可复用机制** · 对固定任务比较重放中间状态与持久状态的成本，并单独检查恢复质量。

<a id="paper-148291"></a>

## IRIS: Interpolative Rényi Iterative Self-play for Large Language Model Fine-Tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/148291) · [作者来源](https://openreview.net/forum?id=yx017YEEPx)

- **问题 / 瓶颈** · 固定散度可能只适合某种分布差距。
- **核心创新 / 方法** · 将 Rényi 目标拆成真实与合成数据的两个加权风险，以阶数动态调整权重。
- **Baseline** · SPIN、SPACE、SPIF 及标准监督微调。
- **Benchmark** · Zephyr-7B、Qwen2.5-3B 的十项基准，报告平均分和标注量。
- **关键结果 / 消融** · 所测平均分 44.57%，26k 标注训练的版本超过使用 200k 的标准监督微调。
- **适用条件 / 局限** · 阶数适应与数据质量、模型大小的交互待核实。

**可复用机制** · 把散度阶数当作训练日程变量，并按轮次测权重集中和分布差距。

<a id="paper-149659"></a>

## Irreducible Supervision Enables Compositional Generalization in Post-Training

[官方论文页](https://neurips.cc/virtual/2026/poster/149659) · [作者来源](https://openreview.net/forum?id=oQZ7gy7rrG)

- **问题 / 瓶颈** · 表面多步示例可能由更浅程序同样解释。
- **核心创新 / 方法** · 在有类型 DSL 中控制结构不可约，并选输入输出排除浅层替代，再对照结果奖励 RL。
- **Baseline** · 不同可约示例污染比例、SFT、GRPO 和 PPO。
- **Benchmark** · 119 个原语，在 Qwen3-8B 及其他规模和 Llama 上复现，指标含 pass@64。
- **关键结果 / 消融** · 完全可约污染时 pass@64 为零；两类不可约性均需满足，后续标准 RL 保持但未扩展所测能力。
- **适用条件 / 局限** · 结论局限该 DSL 及可验证深度，开放任务的不可约性难判。

**可复用机制** · 在加大 RL 预算之前，检查训练样本是否迫使模型学习目标组合，而非只模仿输出。

<a id="paper-139277"></a>

## Is Agentic AI Ready for Real-World Hardware Engineering? A Deep Dive with Phoenix-bench

[官方论文页](https://neurips.cc/virtual/2026/poster/139277) · [作者来源](https://openreview.net/forum?id=ZrY50l0nRz)

- **问题 / 瓶颈** · 软件调优的调用链定位假设在并行硬件实例中不适用。
- **核心创新 / 方法** · 在固定 EDA 环境构造修复评测，比较文件级 oracle 和一轮测试台日志反馈。
- **Baseline** · 四个商业代理、八个开放结构、四种模型骨干，以及两种诊断干预。
- **Benchmark** · 114 个仓库、511 个 Verilator 任务，含验证测试及维护修复，测解决率。
- **关键结果 / 消融** · 文件级 oracle 仅提高约 1.4%，测试反馈让解决率相对提高约 42–45%。
- **适用条件 / 局限** · 依赖 Verilator 和所测缺陷分布，不宜外推到所有硬件工具。

**可复用机制** · 分别比较知道出错位置与知道行为偏差所带来的帮助，据此选择反馈接口。

<a id="paper-151738"></a>

## Is a Linear Probe Evidence of a Linear Representation?

[官方论文页](https://neurips.cc/virtual/2026/poster/151738) · [作者来源](https://openreview.net/forum?id=YSsvDcEXdV)

- **问题 / 瓶颈** · 高读取准确率并不能证明概念占据模型表征的主要变化方向。
- **核心创新 / 方法** · 构造三种非对称诊断，并在已知真值模拟及配对视觉风格的 SVG-World 验证。
- **Baseline** · 标准正向线性探针。
- **Benchmark** · 全观测模拟和预训练视觉编码器，关注反向预测、谱与跨风格泛化。
- **关键结果 / 消融** · 作者发现线性可读性系统性高估更强的线性特征主张。
- **适用条件 / 局限** · 结论范围为模拟和所测视觉编码器。

**可复用机制** · 把线性可读取作为证据起点，只有通过反向及迁移检查后再主张结构特性。

<a id="paper-152783"></a>

## Is Backpropagation Optimal? When Synthetic Gradients Improve Sample Efficiency

[官方论文页](https://neurips.cc/virtual/2026/poster/152783) · [作者来源](https://openreview.net/forum?id=QND70yOOUm)

- **问题 / 瓶颈** · 可微性并不保证反传得到的随机估计样本效率最高。
- **核心创新 / 方法** · 统一向量化损失和奖励反馈，推导合成梯度取得更低估计 MSE 的条件。
- **Baseline** · 普通反向传播估计。
- **Benchmark** · 构造例子、上下文赌博机与强化学习，指标为梯度估计误差和样本效率。
- **关键结果 / 消融** · 理论构造的效率差可任意大，摘要报告赌博机和 RL 结果支持潜力。
- **适用条件 / 局限** · 优势取决于任务及梯度估计噪声结构，实际选型条件需查正文。

**可复用机制** · 比较误差分解与采样预算，避免把对单个样本梯度精确等同于总体估计方差最小。

<a id="paper-152780"></a>

## Is Complex Training Necessary for Long-Tailed OOD Detection? A Re-think from Feature Geometry

[官方论文页](https://neurips.cc/virtual/2026/poster/152780) · [作者来源](https://openreview.net/forum?id=QOPXWKIOWU)

- **问题 / 瓶颈** · 类频率影响范数，尾类单独估计协方差样本少。
- **核心创新 / 方法** · 冻结特征归一至球面，以岭正则池化协方差衡量到各类均值的距离。
- **Baseline** · 原始 Mahalanobis、不同后处理及 PC-ERM。
- **Benchmark** · CIFAR-10-LT、CIFAR-100-LT 与 ImageNet-100-LT，AUROC 和训练效率。
- **关键结果 / 消融** · PC-ERM 的 AUROC 分别由 46.49 到 85.67、50.40 到 78.35。
- **适用条件 / 局限** · 结果依赖方向特征质量及分布外样本类型。

**可复用机制** · 固定骨干分别消融归一化和池化，按类频率报告 OOD 结果。

<a id="paper-152469"></a>

## Is Decentralized LLM Agent RL Robust to Heterogeneity? An Asymmetric Tale

[官方论文页](https://neurips.cc/virtual/2026/poster/152469) · [作者来源](https://openreview.net/forum?id=SsF2kYJfYC)

- **问题 / 瓶颈** · 客户端的任务提示和不可观测环境差异会造成不同更新干扰。
- **核心创新 / 方法** · FedAgent 对任务输入与环境转移分开分析，检验何时环境异质性破坏泛化。
- **Baseline** · 中央训练和纯本地训练。
- **Benchmark** · WebShop、ALFWorld，按异质来源比较训练曲线。
- **关键结果 / 消融** · 均质设置接近集中基线；任务异质较稳，环境异质可从退化到崩溃。
- **适用条件 / 局限** · 所测假设及恢复条件需细读，隐环境信息可观测性影响结论。

**可复用机制** · 先按环境动力学分客户端做鲁棒测试，再决定是否共享同一策略。

<a id="paper-148654"></a>

## Is Dimensionality a Barrier for Retrieval Models?

[官方论文页](https://neurips.cc/virtual/2026/poster/148654) · [作者来源](https://openreview.net/forum?id=w8VsusUqRS)

- **问题 / 瓶颈** · 数据库体量本身解释不了嵌入为何够用。
- **核心创新 / 方法** · 以二元相关矩阵最大内积间隔定义问题，借助压缩感知推导边际保持维度界。
- **Baseline** · 既有通信复杂度界及 InfoNCE 和 sigmoid 损失。
- **Benchmark** · 稀疏相关矩阵理论和两种损失的边际实证。
- **关键结果 / 消融** · 全体 k 稀疏行设置需且足约 k log(n/k) 维达到最大阶边际；sigmoid 实证更优。
- **适用条件 / 局限** · 理论为归一化向量、二元标签和特定结构。

**可复用机制** · 分别扫相关文档稀疏度和维数，在检索值外报告正负边际。

<a id="paper-156025"></a>

## Is Memorization Actually Necessary for Generalization

[官方论文页](https://neurips.cc/virtual/2026/poster/156025) · [作者来源](https://openreview.net/forum?id=14Cuwh2N4C)

- **问题 / 瓶颈** · 基于影响分数删除样本会受采样、阈值、假阳性和交叉污染干扰。
- **核心创新 / 方法** · 修改评分估计与定义，使用有依据的阈值和设计过的隔离测试集。
- **Baseline** · Feldman 等的原流程。
- **Benchmark** · 删除被判为记忆的训练点后对照测试准确度；数据细节待核。
- **关键结果 / 消融** · 摘要称纠正后删除通常不降准确率，多数情形反而改善。
- **适用条件 / 局限** · 结论受修改后记忆定义和测例影响。

**可复用机制** · 用阈值敏感性和泄漏对照检验删除结论能否复现。

<a id="paper-154076"></a>

## Isotropic Activation Functions Enable Deindividuated Neurons and Adaptive Topologies

[官方论文页](https://neurips.cc/virtual/2026/poster/154076) · [作者来源](https://openreview.net/forum?id=GNcZkqvGqw)

- **问题 / 瓶颈** · 逐坐标激活使神经元锁定在特定基底，难无损重构连接。
- **核心创新 / 方法** · 用各向同性激活和仿射映射的奇异值分解重参数化，再对低影响连接剪减或维护备用容量。
- **Baseline** · 通常逐元素激活的稠密结构为背景。
- **Benchmark** · 理论等价、拓扑变化及稀疏分析；经验数据待核。
- **关键结果 / 消融** · 摘要给出扩容精确等价和剪减近似等价，并称渐近参数可稀疏一半。
- **适用条件 / 局限** · 适用于特殊激活和参数化，常见网络兼容性待核。

**可复用机制** · 将扩容或剪减即刻函数误差与后续适应能力分开验证。

<a id="paper-148810"></a>

## Is Text All You Need? Text as a Universal Information Bottleneck for Speech LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/148810) · [作者来源](https://openreview.net/forum?id=ux19efk62R)

- **问题 / 瓶颈** · 离散化会丢语音情感，无约束映射又可能偏离语言输入。
- **核心创新 / 方法** · 每帧表示为词嵌入凸组合，可在词之间保留连续运动轨迹。
- **Baseline** · 离散词对齐及无约束连续接口。
- **Benchmark** · LibriSpeech WER 与情感分类，另有几何和轨迹因果干预。
- **关键结果 / 消融** · WER 最大相对降低 48.7%，并匹配或超过单任务情感准确率。
- **适用条件 / 局限** · 极端非语音噪声、语言迁移及词表成本待核。

**可复用机制** · 分别打乱时间轨迹和移出嵌入区域，验证结构和对齐各自必要性。

<a id="paper-152454"></a>

## Is the Importance Ratio Necessary for Stable Reinforcement Learning in LLMs?

[官方论文页](https://neurips.cc/virtual/2026/poster/152454) · [作者来源](https://openreview.net/forum?id=T0HJLu9Gie)

- **问题 / 瓶颈** · 旧新策略比计算昂贵，全 on-policy 下比值恒一也可能失去裁剪。
- **核心创新 / 方法** · LGPO 用基于似然的软门控提供约束，免算旧策略似然。
- **Baseline** · 标准 GRPO、去校正及去信任域变体。
- **Benchmark** · 标准与全 on-policy 后训练，比较稳定、性能和耗时。
- **关键结果 / 消融** · 标准设置平均节省约 18%；全 on-policy 下报告更稳定。
- **适用条件 / 局限** · 门控阈值和策略漂移对高异步环境的影响待核。

**可复用机制** · 分别消融比值与门控，记录训练崩溃率和实际策略移动程度。

<a id="paper-139736"></a>

## Is Your LLM-as-a-Recommender Agent Trustable? LLMs' Recommendation is Easily Hacked by Biases (Preferences)

[官方论文页](https://neurips.cc/virtual/2026/poster/139736) · [作者来源](https://openreview.net/forum?id=7MpLcC0zEL)

- **问题 / 瓶颈** · 总体准确率会掩盖选项质量接近时的排序偏向。
- **核心创新 / 方法** · 在已知质量差的候选集上比较上下文变化前后结果。
- **Baseline** · 不同规模模型和基准质量排序。
- **Benchmark** · 论文评阅、商品和招聘三域，测选择偏差。
- **关键结果 / 消融** · 强弱模型均出现排序脆弱性，即使具备识别真实质量的能力。
- **适用条件 / 局限** · 合成评测与真实业务相符程度需核。

**可复用机制** · 防御测试按质量差分桶，并检查公平性回归是否影响正常区分。

<a id="paper-154420"></a>

## It Cancels: O(r²) Cholesky Updates for Whitened Operators

[官方论文页](https://neurips.cc/virtual/2026/poster/154420) · [作者来源](https://openreview.net/forum?id=DiPStsh1m2)

- **问题 / 瓶颈** · 因子变化后重做双边白化可能使每步耗时为三次。
- **核心创新 / 方法** · 在预白化空间对零填充矩阵做双边 Givens 旋转与秩一修正，省去中间 Cholesky 因子。
- **Baseline** · 完整重分解和仅单边更新。
- **Benchmark** · 流式稀疏 GP 与自然梯度等，比较耗时、精度。
- **关键结果 / 消融** · 精度匹配重分解，实验最高 5.4 倍；秩 1024 时训练 1075 秒到 198 秒。
- **适用条件 / 局限** · 适用于文中秩一条件，长序列的数值误差待核。

**可复用机制** · 在非生物流式回归中以完整重分解验算相对残差和累计漂移。

<a id="paper-152685"></a>

## Iterative Chow Filtering for Learning with Distribution Shift

[官方论文页](https://neurips.cc/virtual/2026/poster/152685) · [作者来源](https://openreview.net/forum?id=RBxhiGn1aP)

- **问题 / 瓶颈** · 已有 PQ 学习需强 L2 夹逼，对基本函数类界偏弱。
- **核心创新 / 方法** · 证明 L1 夹逼足够，并用迭代 Chow 筛选识别与训练分布不符的样本。
- **Baseline** · 既有 L2 夹逼 PQ 理论。
- **Benchmark** · 均匀分布下 DNF 与常深电路、常次数阈值函数。
- **关键结果 / 消融** · DNF 获准多项式时间，若干类获得指数改善。
- **适用条件 / 局限** · 理论依赖逼近及分布条件，无摘要实证。

**可复用机制** · 比较检测后拒答策略时单列分布外拒绝和分布内覆盖。

<a id="paper-148385"></a>

## Iterative Critique-and-Routing Controller for Multi-Agent Systems with Heterogeneous LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/148385) · [作者来源](https://openreview.net/forum?id=yFoPKj8BCA)

- **问题 / 瓶颈** · 单次路由忽略草稿质量的反馈。
- **核心创新 / 方法** · 把草稿检查、停止与下一模型选择建模为有限时域决策，在模型调用额度下训练。
- **Baseline** · 单次路由和先进多模型对照。
- **Benchmark** · 七个推理评测，多种异构模型团队。
- **关键结果 / 消融** · 摘要称超过基线，仅不到四分之一调用用最强模型。
- **适用条件 / 局限** · 训练与推理成本、错误自我确认待核。

**可复用机制** · 在良性推理校对中用相同强模型调用预算比较单次与递进审核。

<a id="paper-150597"></a>

## Iterative Gumbel Planning for Continuous Control

[官方论文页](https://neurips.cc/virtual/2026/poster/150597) · [作者来源](https://openreview.net/forum?id=gxzYBTetUi)

- **问题 / 瓶颈** · 有限动作搜索再拟合连续高斯会留下投影误差。
- **核心创新 / 方法** · 采用按动作维度分解的类别策略、无放回 Gumbel Top-K 抽样和同状态重复精炼。
- **Baseline** · 高斯策略蒸馏与搜索方法，思路来自 MPPI。
- **Benchmark** · DMControl、HumanoidBench，评回报、样本效率与动作方差。
- **关键结果 / 消融** · 作者称表现领先且动作方差更低；理论剩余误差可随网格控制。
- **适用条件 / 局限** · 高维动作耦合和网格代价需检验。

**可复用机制** · 等搜索次数下对比分布投影残差与网格细化误差。

<a id="paper-151893"></a>

## Iterative ILP with Update-Size Control for Reducing Surrogate-Task Mismatch in Bit-Width Selection

[官方论文页](https://neurips.cc/virtual/2026/poster/151893) · [作者来源](https://openreview.net/forum?id=X9Qr7zejV9)

- **问题 / 瓶颈** · 可加代理在同时改很多层时误差放大。
- **核心创新 / 方法** · 从当前参考出发解多种改动上限的 ILP，仅接受真实损失降低的配置。
- **Baseline** · 统一精度及既有混合精度方法。
- **Benchmark** · PTQ 和 QAT；真实损失及量化质量。
- **关键结果 / 消融** · 摘要称真实最优常在中间上限，得到更好精度效率。
- **适用条件 / 局限** · 额外候选评估成本、校准样本代表性待核。

**可复用机制** · 绘制层改动数、代理和真实损失三者关系再选更新步长。

<a id="paper-154947"></a>

## Iterative Latent Refinement for Value Learning in Offline Goal-Conditioned RL

[官方论文页](https://neurips.cc/virtual/2026/poster/154947) · [作者来源](https://openreview.net/forum?id=9ifoNWFpH3)

- **问题 / 瓶颈** · 单次价值读出难兼顾长程可达性及策略抽取。
- **核心创新 / 方法** · 用共享迭代权重和轻量步特异参数重复细化潜表示。
- **Baseline** · 各现有离线算法的前馈价值骨干。
- **Benchmark** · 21 个算法与数据组合，重点拼接和瓶颈迷宫。
- **关键结果 / 消融** · 平均提高 10.7 个百分点，目标区分与行为支持代理也改善。
- **适用条件 / 局限** · 多次计算的实际成本和长程外推待核。

**可复用机制** · 对照等计算前馈与循环价值，分解循环深度与单步表达力。

<a id="paper-151990"></a>

## Iterative Nonlinear Computation Underlying Abstract Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/151990) · [作者来源](https://openreview.net/forum?id=WJZTqX8nzZ)

- **问题 / 瓶颈** · 复杂启发设计会掩盖通用 Transformer 的主要增益。
- **核心创新 / 方法** · URM 在前馈内加短卷积增强非线性，多循环训练中截断早期循环梯度。
- **Baseline** · 通用 Transformer 变体和普通 8B 骨干。
- **Benchmark** · ARC-AGI 1、2 与 8B 预训练后逻辑评测。
- **关键结果 / 消融** · ARC-AGI pass@1 分别 57.5%、16.0%；作者报告大模型推理改善。
- **适用条件 / 局限** · 循环计算成本及各消融的等训练预算待核。

**可复用机制** · 固定参数与 FLOPs，交叉消融共享、非线性与截断。

<a id="paper-154982"></a>

## Iterative Scarcity-Guided Exploration: Bootstrapping Generative Auto-bidding from Narrow Support

[官方论文页](https://neurips.cc/virtual/2026/poster/154982) · [作者来源](https://openreview.net/forum?id=9S00kkyYbM)

- **问题 / 瓶颈** · 弱回报信号被曲率惩罚盖住，反复自训练停滞。
- **核心创新 / 方法** · 在回报信号衰减时引入轨迹稀缺评分，与回报共同引导候选生成。
- **Baseline** · 代表生成出价与全数据基线。
- **Benchmark** · AuctionNet 冷启动设置和多轮迭代。
- **关键结果 / 消融** · 摘要称三轮内超过全数据基线。
- **适用条件 / 局限** · 仅一工业场景，稀有但低质量候选的筛查待核。

**可复用机制** · 在良性离线模拟器分别测覆盖扩展和收益，检查稀缺信号是否真在回报不足时有效。

<a id="paper-150804"></a>

## It Just Takes Two: Scaling Amortized Inference to Large Sets

[官方论文页](https://neurips.cc/virtual/2026/poster/150804) · [作者来源](https://openreview.net/forum?id=fH4iGkHcRV)

- **问题 / 瓶颈** · 按部署集合规模端到端训练会耗尽内存。
- **核心创新 / 方法** · 用至多双样本集合训练均值池化编码器，再用预聚合表示微调推理头。
- **Baseline** · 标准端到端摊销后验方法。
- **Benchmark** · 标量、图像、多视角等条件任务，集合达数千；比较质量和计算。
- **关键结果 / 消融** · 摘要报告低得多计算量下持平或领先。
- **适用条件 / 局限** · 表示可聚合与共享未知因素的假设需核；高阶组交互待测。

**可复用机制** · 对固定集合核测试双样本编码是否保留大集合统计，并单列头部微调花费。

<a id="paper-152722"></a>

## Itô maps for any-step SDEs

[官方论文页](https://neurips.cc/virtual/2026/poster/152722) · [作者来源](https://openreview.net/forum?id=QqN3QhHfCr)

- **问题 / 瓶颈** · 常见一步蒸馏从确定 ODE 出发，无法直接表达条件未来多样性。
- **核心创新 / 方法** · Itô 映射从任意中间时刻的状态和布朗路径单前向预测未来。
- **Baseline** · 确定性流映射；具体经验基线待核。
- **Benchmark** · 合成与图像生成，检查端点条件有效性、多样性与控制。
- **关键结果 / 消融** · 摘要报告固定中间态下保持多样性，且控制效果良好。
- **适用条件 / 局限** · 随机路径表示、不同步长的误差界和计算仍需核查。

**可复用机制** · 同起点复用多条噪声路径，对比一步与逐步采样的条件分布。

<a id="paper-152157"></a>

## ITO: Multi-View Alignment and Training-Time Fusion for Image-Text Pretraining

[官方论文页](https://neurips.cc/virtual/2026/poster/152157) · [作者来源](https://openreview.net/forum?id=V6FtgDk4Nx)

- **问题 / 瓶颈** · 对比特征可能仍按模态分隔，过强训练会后期过拟合。
- **核心创新 / 方法** · 多视图图像产生多重图文对齐，另加轻量融合头约束共同几何。
- **Baseline** · 强图文对比预训练双编码器。
- **Benchmark** · 百万至十亿规模预训练，分类、检索及多模态测评。
- **关键结果 / 消融** · 作者称多视图贡献主要判别增益，融合减少模态分隔并稳定后期训练。
- **适用条件 / 局限** · 训练开销与未见配对数据中的效果待核。

**可复用机制** · 部署结构固定时拆分多视图与融合，对照后期验证损失和跨模态邻域。
