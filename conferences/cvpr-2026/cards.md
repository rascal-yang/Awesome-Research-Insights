# CVPR 2026 论文卡

[返回会议页](README.md)

<a id="paper-ecosplat"></a>

## EcoSplat: Efficiency-controllable Feed-forward 3D Gaussian Splatting from Multi-view Images

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Bui_EcoSplat_Efficiency-controllable_Feed-forward_3D_Gaussian_Splatting_from_Multi-view_Images_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Bui_EcoSplat_Efficiency-controllable_Feed-forward_3D_Gaussian_Splatting_from_Multi-view_Images_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 前馈 3D 高斯重建随输入视角增加产生大量逐像素基元，部署时难以直接控制表示大小。
- **核心创新 / 方法** · 先训练逐像素高斯，再学习重要性排序，并根据指定预算调整保留基元参数。
- **Baseline** · 与 GGN 及 MVSplat、DepthSplat、NoPoSplat 等比较；消融像素对齐预训练和重要性学习组件。
- **Benchmark** · RE10K 新视角合成，输入 16、20、24 视角；以 PSNR、SSIM、LPIPS 和基元数衡量；在 ACID 做零样本迁移。
- **关键结果 / 消融** · 表 1 比较原始逐像素基元数的 5%、10%、40%、70%，GGN 无法提供低于 15% 的配置。表 4 去掉像素对齐预训练后 PSNR 下降 1.5 dB。
- **适用条件 / 局限** · 评测主要覆盖多视角输入的新视角合成；迁移到实时系统时还需单测排序、预测和渲染的端到端开销。

**可复用机制** · 将基元预算作为模型输入，比较预算感知预测和事后剪枝。

<a id="paper-season"></a>

## SEASON: Mitigating Temporal Hallucination in Video Large Language Models via Self-Diagnostic Contrastive Decoding

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_SEASON_Mitigating_Temporal_Hallucination_in_Video_Large_Language_Models_via_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wu_SEASON_Mitigating_Temporal_Hallucination_in_Video_Large_Language_Models_via_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 视频模型会生成语言上通顺但时序错误的回答，普通视频问答分数难以定位此类错误。
- **核心创新 / 方法** · 构造时序被削弱的对照视频，逐词判断时序或空间幻觉风险，再选择相应的对比解码信号。
- **Baseline** · 在 LLaVA-OV-7B 等骨干上比较原解码、TCD 与 DINO-HEAL；另比较平均、打乱和倒序等时序负样本。
- **Benchmark** · 表 1 用 VidHalluc、VideoHallucer、EventHallusion 的子任务准确率；表 2 补测 TempCompass、TVBench、VideoMME 和 MVBench。
- **关键结果 / 消融** · 表 1 中 LLaVA-OV-7B 的 VideoHallucer 平均准确率从 46.40% 到 48.50%，TCD 为 48.10%；同一骨干的 EventHallusion 从 60.15% 到 69.19%，TCD 为 68.46%。表 3 单独比较负样本构造。
- **适用条件 / 局限** · 需要能读取解码分数并对照不同视频输入；部分子项下降，例如 LLaVA-OV-7B 的 VidHalluc 二元问答准确率从 74.36% 到 73.15%。

**可复用机制** · 对照正常和时序负样本的解码，诊断逐词时序依赖。

<a id="paper-hycal"></a>

## HyCal: A Training-Free Prototype Calibration Method for Cross-Discipline Few-Shot Class-Incremental Learning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Lee_HyCal_A_Training-Free_Prototype_Calibration_Method_for_Cross-Discipline_Few-Shot_Class-Incremental_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Lee_HyCal_A_Training-Free_Prototype_Calibration_Method_for_Cross-Discipline_Few-Shot_Class-Incremental_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 跨学科小样本类增量学习存在域间样本量不均；统一距离可能在不同特征几何下偏置预测。
- **核心创新 / 方法** · 在冻结 CLIP 特征上以少量标注构造原型，动态融合余弦相似度和马氏距离。
- **Baseline** · 冻结 CLIP；对照零样本 CLIP、Primal-RAIL、FeCAM、RanPAC、KLDA，并比较固定与动态融合。
- **Benchmark** · XD-VSCIL 的类内均衡和域不均衡设置，报告增量平均准确率、末轮准确率及 SCDE；表 2 对 8 域用 4 个随机种子。
- **关键结果 / 消融** · 表 2 高域间不均衡设置平均准确率 54.48%、末轮准确率 63.50%；表 3 类内均衡 SCDE 为 60.92，Primal-RAIL 为 59.19。
- **适用条件 / 局限** · 训练免梯度仍需标注样本估计原型统计；小样本协方差、域漂移及更换冻结骨干后的效果需验证。

**可复用机制** · 冻结特征时比较余弦、协方差距离与动态融合。

<a id="paper-quantiphy"></a>

## QUANTIPHY: A Quantitative Benchmark Evaluating Physical Reasoning Abilities of Vision-Language Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Puyin_QUANTIPHY_A_Quantitative_Benchmark_Evaluating_Physical_Reasoning_Abilities_of_Vision-Language_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Puyin_QUANTIPHY_A_Quantitative_Benchmark_Evaluating_Physical_Reasoning_Abilities_of_Vision-Language_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 定性视觉问答难以检验模型是否从视频推断数值物理量。
- **核心创新 / 方法** · 固定提示与数值计分，并将视频、文字先验及反事实先验组合为对照，区分视觉取证与先验猜测。
- **Baseline** · 比较 21 个模型及变体，含 ChatGPT-5.1、Gemini 2.5 Pro/Flash、Qwen3-VL；同模型比较视频加先验、仅先验和反事实先验。
- **Benchmark** · QUANTIPHY 含 3,300 多个视频文本实例，在指定时刻估计尺寸、速度或加速度；报告四类场景及平均 MRA。
- **关键结果 / 消融** · 表 2 的 161 对分析子集上，多数模型的仅先验与视频加先验表现差距有限；反事实先验进一步检验模型对输入的依赖。
- **适用条件 / 局限** · 覆盖固定相机下刚体平移及相对简单的独立运动，旋转、变形物体和移动视角尚未验证。

**可复用机制** · 用仅先验和反事实先验对照，检验数值回答是否依赖视频。

<a id="paper-unikpt"></a>

## Generalizable Structure-Aware Keypoint Correspondence for Category-Unified 3D Single Object Tracking

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_Generalizable_Structure-Aware_Keypoint_Correspondence_for_Category-Unified_3D_Single_Object_Tracking_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xiao_Generalizable_Structure-Aware_Keypoint_Correspondence_for_Category-Unified_3D_Single_Object_Tracking_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 面向多类别的点云单目标跟踪需要跨尺度和跨结构匹配，同类专用模型的先验难以直接共享。
- **核心创新 / 方法** · 提取尺度感知关键点，逐步对齐跨帧对应，再以置信度和几何结构定位目标。
- **Baseline** · 表 1 对照统一跟踪器 MoCUT、TrackAny3D 及按类训练的 P2P；表 3 消融坐标监督等组件。
- **Benchmark** · nuScenes 的汽车、行人、卡车、拖车和公交车及 KITTI 的四类目标，报告 Success 和 Precision。
- **关键结果 / 消融** · 表 1 中 nuScenes 均值为 64.21/77.29，TrackAny3D 为 54.57/66.25。表 3 移除坐标监督后降为 60.63/73.30。
- **适用条件 / 局限** · 现有证据来自道路点云单目标跟踪；极稀疏观测、遮挡和新类别下的收益需单独复测。

**可复用机制** · 稀疏点云跟踪时，比较尺度适配关键点的渐进匹配与密集对应。

<a id="paper-directfisheye-gs"></a>

## DirectFisheye-GS: Enabling Native Fisheye Input in Gaussian Splatting with Cross-View Joint Optimization

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_DirectFisheye-GS_Enabling_Native_Fisheye_Input_in_Gaussian_Splatting_with_Cross-View_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yang_DirectFisheye-GS_Enabling_Native_Fisheye_Input_in_Gaussian_Splatting_with_Cross-View_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 先去畸变会丢失鱼眼边缘视野并降低细节密度；即使用原生相机模型，逐视角训练仍会出现边缘漂浮伪影。
- **核心创新 / 方法** · 将鱼眼相机模型接入 3DGS，再用特征重叠选择视角，共同约束跨视角几何和光度。
- **Baseline** · 以 3DGS 为底座，比较去畸变输入的 3DGS、Fisheye-GS 等；消融比较仅使用鱼眼模型与增加跨视角联合优化。
- **Benchmark** · FisheyeNeRF、ScanNet++、DenSOFT 的训练视角或留出视角，报告 SSIM、PSNR 和 LPIPS；区分表 1 训练视角和表 2 留出视角。
- **关键结果 / 消融** · 表 2 的 ScanNet++ 留出视角平均 PSNR 为 28.37 dB，去畸变 3DGS 为 25.88 dB，Fisheye-GS 为 27.86 dB。
- **适用条件 / 局限** · 需要与原生相机模型相符的标定及可测的视角重叠；在低重叠或新镜头上的效果需验证。

**可复用机制** · 用特征重叠挑选联合优化视角，并测试跨视角约束能否抑制边缘漂浮伪影。

<a id="paper-compbench"></a>

## CompBench: Benchmarking Complex Instruction-guided Image Editing

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Jia_CompBench_Benchmarking_Complex_Instruction-guided_Image_Editing_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Jia_CompBench_Benchmarking_Complex_Instruction-guided_Image_Editing_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 简单指令掩盖了图像编辑模型在多目标、空间关系和连续修改中的错误。
- **核心创新 / 方法** · 将编辑意图拆成位置、外观、动态和对象四维，用人工与多模态模型协作构建复杂任务。
- **Baseline** · 基准层面对比既有图像编辑数据集；模型层面对照 InstructPix2Pix、MagicBrush、SmartEdit 等。
- **Benchmark** · CompBench 覆盖七项编辑任务。局部、多对象和隐式推理用前景 LC-T、LC-I；多轮编辑兼看背景 PSNR、SSIM、LPIPS；动作、位置及视角结果另含人工评价。
- **关键结果 / 消融** · 表 2–4 分任务比较。讨论指出动作和视角编辑中仍频繁出现形状扭曲，语义对齐分数无法单独保证几何一致性。
- **适用条件 / 局限** · 局部 CLIP 相似度依赖区域划分及参考结果，遇到空间关系和多种合理输出时仍需人工或几何验证。

**可复用机制** · 把编辑指令拆成位置、外观、动态和对象条件，并分别验收目标变化与背景保留。

<a id="paper-chord"></a>

## Choreographing a World of Dynamic Objects

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Lyu_Choreographing_a_World_of_Dynamic_Objects_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Lyu_Choreographing_a_World_of_Dynamic_Objects_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 多物体交互动画很难靠类别专用规则扩展，分别生成多个视角又容易产生不一致的运动。
- **核心创新 / 方法** · 把视频模型的图像序列监督蒸馏到随时间移动的三维场景表示；为 rectified flow 视频模型推导相应的分数蒸馏目标。
- **Baseline** · 比较 Animate3D、AnimateAnyMesh、MotionDreamer 和从 TrajectoryCrafter 视频重建动态场景。
- **Benchmark** · 表 1 在六段场景动画上做人评，报告提示对齐和真实感的选择比例，并用 VideoPhy-2 评语义遵循和物理常识。
- **关键结果 / 消融** · CHORD 的提示对齐与真实感人评选择比例为 87.71% 和 87.37%；VideoPhy-2 物理常识为 4.25，低于 AnimateAnyMesh 的 4.50。
- **适用条件 / 局限** · 评测覆盖有限，人评真实感不能验证力学或接触正确性；沉淀到控制策略前需要额外检验动作可执行性。

**可复用机制** · 从冻结视频生成器蒸馏持久的三维运动表示，并把跨视角一致性作为独立验收项。

<a id="paper-spk2vidnet"></a>

## Spk2VidNet: A Hierarchical Recurrent Architecture for High-Fidelity Video Reconstruction from Long Spike-Camera Streams

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Spk2VidNet_A_Hierarchical_Recurrent_Architecture_for_High-Fidelity_Video_Reconstruction_from_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_Spk2VidNet_A_Hierarchical_Recurrent_Architecture_for_High-Fidelity_Video_Reconstruction_from_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 固定窗口的脉冲相机超分辨率只利用局部时间信息，脉冲波动会影响强度重建。
- **核心创新 / 方法** · 以分层递归扩大时间感受野，并用多帧运动一致性改进对齐、多尺度相似性融合；分段训练时传递状态。
- **Baseline** · 表 1 对比 Spk2SRImgNet 和 SCSRNet 等；表 2 对比运动对齐、融合和传播层数。
- **Benchmark** · REDS-LSSR 和 Adobe240-LSSR 合成测试的 4 倍及 8 倍重建，报告 PSNR、SSIM、LPIPS、运行时间和显存，另展示实拍脉冲数据。
- **关键结果 / 消融** · 表 1 的 4 倍重建在 REDS-LSSR 为 29.92 dB、Adobe240-LSSR 为 32.36 dB；该配置报告 43 ms、4,606 MB。
- **适用条件 / 局限** · 跨帧融合依赖运动对齐，遮挡或突变下应复测；表 1 的量化结果来自合成基准，实拍展示不能替代有参考的误差测量。

**可复用机制** · 在显存固定时分段传递循环状态，并把跨帧对齐与可用历史长度分开消融。

<a id="paper-se2d"></a>

## Continual Distillation of Teachers from Different Domains

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Michel_Continual_Distillation_of_Teachers_from_Different_Domains_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Michel_Continual_Distillation_of_Teachers_from_Different_Domains_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 依次接收异域教师且无法保留旧教师时，学生会遗忘先前从外部无标签数据学到的知识。
- **核心创新 / 方法** · SE2D 用外部样本得到当前教师监督，同时保持学生在外部样本上的旧 logits。
- **Baseline** · 分别对照只用内部数据、使用外部数据及自蒸馏等方案。
- **Benchmark** · CIFAR20、Digits、DomainNet 的顺序跨域蒸馏；表 2–4 报告训练结束时分域及平均分类准确率。
- **关键结果 / 消融** · 相关外部数据能帮助保持跨域知识；论文报告 DomainNet 上 SE2D 落后于自蒸馏，且与 CIFAR20 不相关的 MNIST 外部数据削弱收益。
- **适用条件 / 局限** · 依赖外部数据与教师覆盖的相关性，也需区分内外部数据来源。教师输出不具信息时保持 logits 未必有用。

**可复用机制** · 连续蒸馏时保留相关外部样本上的输出，并把旧域遗忘和当前域适配分开衡量。

<a id="paper-gt-svj"></a>

## GT-SVJ: Generative-Transformer-Based Self-Supervised Video Judge For Efficient Video Reward Modeling

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Shekhar_GT-SVJ_Generative-Transformer-Based_Self-Supervised_Video_Judge_For_Efficient_Video_Reward_Modeling_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Shekhar_GT-SVJ_Generative-Transformer-Based_Self-Supervised_Video_Judge_For_Efficient_Video_Reward_Modeling_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 通用视觉语言奖励模型容易忽视细微的时序退化，人类视频偏好标注也昂贵。
- **核心创新 / 方法** · 用视频生成骨干表示视频，以受控的潜空间时序扰动形成难负样本，做对比预训练后再拟合人类偏好。
- **Baseline** · 以 CogVideoX 为骨干；对照 VideoScore、VisionReward、VideoReward，表 1 另列 p=0 和 No DM。
- **Benchmark** · GenAI-Bench、MonteBench、VideoReward-Bench，按计入或排除平局分别报告与人类偏好一致的准确率。
- **关键结果 / 消融** · 表 1 排除平局时，GT-SVJ 在 MonteBench 为 77.76%，VisionReward 为 72.10%；VideoReward-Bench 为 68.57%，低于 VideoReward 的 73.59%。
- **适用条件 / 局限** · 受控退化只覆盖部分生成错误，仍使用 30.4K 人类标注样本；跨生成器或域迁移需复测。

**可复用机制** · 复用视频生成骨干做偏好评分，用受控时序退化训练评审器，并以人类偏好排序验证。

<a id="paper-kl-barycentric-consensus"></a>

## Beyond Euclidean Gossip: KL-Barycentric Consensus on Heterogeneous and Imbalanced Images

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_Beyond_Euclidean_Gossip_KL-Barycentric_Consensus_on_Heterogeneous_and_Imbalanced_Images_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_Beyond_Euclidean_Gossip_KL-Barycentric_Consensus_on_Heterogeneous_and_Imbalanced_Images_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 站点标签与样本量不均时，在权重空间直接平均可能与本地模型分布不一致。
- **核心创新 / 方法** · 以对角高斯后验表示客户端模型，在指数族期望参数空间线性混合得到正向 KL 重心，并将本地 Adam 更新写入同一坐标。
- **Baseline** · 比较 Gossip-SGD、SGP、GT-SGD、QGM、Euclidean-Adam；另报告集中训练参照。
- **Benchmark** · CIFAR-100 的 8 或 16 客户端非 IID 和样本量偏斜设置，测测试准确率；Kvasir-SEG 测 Dice 和 IoU。
- **关键结果 / 消融** · 表 1 中 8 客户端一组强非 IID 设置，KL 共识 Adam 达 54.39%，Euclidean-Adam 为 35.18%，QGM 为 40.85%；统计来自三次运行。
- **适用条件 / 局限** · 收敛证明限连通图和凸损失；非凸网络中的收益属于实证结果，且方法只使用对角后验。

**可复用机制** · 去中心化训练时，用后验期望参数做共识，并在相同通信预算下对照欧氏平均。

<a id="paper-hybriddrivevla"></a>

## HybridDriveVLA: Vision-Language-Action Model with Visual CoT reasoning and ToT Evaluation for Autonomous Driving

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Bassole_HybridDriveVLA_Vision-Language-Action_Model_with_Visual_CoT_reasoning_and_ToT_Evaluation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Bassole_HybridDriveVLA_Vision-Language-Action_Model_with_Visual_CoT_reasoning_and_ToT_Evaluation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 从当前图像生成单一轨迹，难以判断显式未来预测能否改善多目标轨迹选择。
- **核心创新 / 方法** · 先预测未来场景，再从安全、进度和舒适角度分别评价候选路点，比较单项优先和综合评分。
- **Baseline** · 与 DriveVLM、OpenDriveVLA 等对照；消融移除视觉预测，仅保留候选路点评价。
- **Benchmark** · nuScenes 验证集用 ST-P3 和 UniAD 口径衡量碰撞及轨迹误差；NAVSIM 另报告 PDMS、碰撞和舒适等维度。
- **关键结果 / 消融** · 第 4.2 节报告 ST-P3 平均碰撞率在仅候选评价时为 0.23%，加入视觉预测后为 0.17%。
- **适用条件 / 局限** · 碰撞数字来自基准测试；迁移到控制任务需另评预测偏差、推理时延及闭环安全。

**可复用机制** · 固定候选轨迹评分流程，对照是否加入视觉未来预测，并分别监测安全、进度和舒适。

<a id="paper-commutator-zero-diffusion-preview"></a>

## Training-free, Perceptually Consistent Low-Resolution Previews with High-Resolution Image for Efficient Workflows of Diffusion Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Jeong_Training-free_Perceptually_Consistent_Low-Resolution_Previews_with_High-Resolution_Image_for_Efficient_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Jeong_Training-free_Perceptually_Consistent_Low-Resolution_Previews_with_High-Resolution_Image_for_Efficient_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 同一提示和种子在不同分辨率下，扩散轨迹会产生构图偏移，使低分辨率生成难充当高分辨率预览。
- **核心创新 / 方法** · 先沿高分辨率轨迹去噪，再从保持噪声特性的候选降采样矩阵中选择使速度场交换误差较小的矩阵，用缓存的速度预测校正低分辨率潜变量，随后继续低分辨率去噪。
- **Baseline** · 比较减少去噪步数、全程低分辨率、切换时用最近邻降采样，并检验与 TaylorSeer 合用。
- **Benchmark** · 从 PixArt-Eval30K 随机取 5,000 个提示，用 FLUX.1-dev 和 SD3.5-Large 的 1,024 像素输出作参考；比较 512 像素预览的延迟、PIQE、DreamSim、DiffSim、PSNR 和 FSIM。
- **关键结果 / 消融** · 表 2 的 FLUX.1-dev 预览耗时 9.76 秒，参考耗时 14.78 秒；DreamSim 为 6.83，全程低分辨率为 21.02，但后者仅 4.94 秒。表 5 移除交换误差引导时 PSNR 从 20.962 降至 19.115 dB。
- **适用条件 / 局限** · 需先支付部分高分辨率去噪成本，适用于预览必须与指定高分辨率结果一致的工作流；更大分辨率跨度和视频尚需验证。

**可复用机制** · 扩散预览切换空间分辨率时，用可测的速度场交换误差选择降采样并校正潜变量；见 §3.3–3.4、表 2 和表 5。

<a id="paper-catalyst4d"></a>

## Catalyst4D: High-Fidelity 3D-to-4D Scene Editing via Dynamic Propagation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Catalyst4D_High-Fidelity_3D-to-4D_Scene_Editing_via_Dynamic_Propagation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_Catalyst4D_High-Fidelity_3D-to-4D_Scene_Editing_via_Dynamic_Propagation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 将静态高斯编辑应用到动态序列时，新高斯缺少运动对应，逐点近邻会把相互接近但属于不同区域的变形混合。
- **核心创新 / 方法** · 从原始与编辑后的高斯选空间稳定锚，按最优传输建立区域对应，再传播变形；用颜色不确定性筛选需要外观细化的高斯。
- **Baseline** · 比较 Instruct 4D-to-4D、Instruct-4DGS、CTRL-D；消融用三个原始近邻加权变形代替区域锚引导。
- **Benchmark** · 表 1 包含 DyNeRF 的 Sear-steak、Coffee-martini 与 MeetRoom 的 Trimming；报告提示 CLIP 相似度、VBench 时间一致性与优化时间。
- **关键结果 / 消融** · Sear-steak 上 CLIP 相似度为 0.252，CTRL-D 为 0.249；时间一致性分别为 0.983 和 0.985。图 6 中近邻传播会把手部运动误传到躯干。
- **适用条件 / 局限** · 依赖可编辑的高斯场景、已有变形与稳定锚；未重新训练变形网络，不能据此保证大幅拓扑改变或新增运动的正确性。

**可复用机制** · 静态编辑向动态重建传播变形时，以区域锚及最优传输替代逐点近邻，避免把相邻肢体的运动混在一起；见 §5.4、图 6。

<a id="paper-grwm-latent-geometry"></a>

## Cloning Deterministic Worlds: The Critical Role of Latent Geometry in Long-Horizon World Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xia_Cloning_Deterministic_Worlds_The_Critical_Role_of_Latent_Geometry_in_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xia_Cloning_Deterministic_Worlds_The_Critical_Role_of_Latent_Geometry_in_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 单帧重建好仍可能得到缺乏状态连续性的潜空间，滚动预测会跳过真实状态或逐渐漂移。
- **核心创新 / 方法** · 因果编码器读短历史；同轨迹上下文窗口内的归一化潜嵌入拉近，同时让跨轨迹嵌入保持分散以防坍塌。
- **Baseline** · 与标准 VAE 世界模型和真状态 oracle 对比；另外在数种视频预测器上替换为几何正则编码器。
- **Benchmark** · 在固定地图的 3×3、9×9 迷宫和 Minecraft-DET 预测动作条件视频；比较逐帧 MSE 与冻结编码器上的真实位姿回归 MSE。
- **关键结果 / 消融** · 表 1 中相较 VAE-WM，位姿探测 MSE 在三个环境分别从 0.082、0.106、0.137 降至 0.031、0.058、0.081。
- **适用条件 / 局限** · 结论集中于确定性受控世界，随机、部分可观测或真实视觉环境仍待检验；与 oracle 还有差距，时间聚合增加开销。

**可复用机制** · 长时世界模型应单独对潜在状态的时间几何做监督和探测，而不是只用逐帧重建误差挑选编码器；见 §5.2、§6.4。

<a id="paper-single-life-geometry"></a>

## Unique Lives, Shared World: Learning from Single-Life Videos

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Han_Unique_Lives_Shared_World_Learning_from_Single-Life_Videos_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Han_Unique_Lives_Shared_World_Learning_from_Single-Life_Videos_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 多视角几何学习常依赖跨视频的大规模多样数据，但不清楚单一持续经历能否形成可迁移的几何表示。
- **核心创新 / 方法** · 把单个长视频经历内的时间邻近帧作多视角配对，分别训练编码器，并用跨注意力相似性衡量不同经历得到的功能表示是否对齐。
- **Baseline** · 主要采用 CroCo 并补测 DINOv2；比较等规模 Kinetics-400、同帧增强配对和随机帧对。
- **Benchmark** · 覆盖 Walking Tours、HD-Epic 和 Anonymous Lives；NYU-Depth-v2 用 ε1、ScanNet 用 AbsRel，HPatches 零样本匹配用 AEPE。
- **关键结果 / 消融** · 图 7 中约 30 小时单一经历在若干几何任务达到等规模 K400；Walking Tours 预训练在 NYU-Depth-v2 上 DINOv2 平均 ε1 为 0.562，CroCo 为 0.538；HPatches 上 CroCo 的 AEPE 反而更低。
- **适用条件 / 局限** · 需要第一视角流含足够的真实视角变化和重叠；几何任务上的表示对齐不能直接推出语义识别与控制迁移。

**可复用机制** · 采集几何表征训练数据时，可对照等规模多样网络视频，先测试单一长程第一视角流中的时间配对；见 §5.2、图 7–9。

<a id="paper-qr-prompt"></a>

## Quantized Residuals to Continuous Prompts for Few-Shot Class Incremental Learning in Vision-Language Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Sinha_Quantized_Residuals_to_Continuous_Prompts_for_Few-Shot_Class_Incremental_Learning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Sinha_Quantized_Residuals_to_Continuous_Prompts_for_Few-Shot_Class_Incremental_Learning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 少量新类标签下，直接拟合新提示易漂移，静态提示又可能漏掉图像中的细粒度属性。
- **核心创新 / 方法** · 用判别式子空间量化储存视觉—文本特征残差，随后将离散残差码分层编码并合成为类条件连续提示。
- **Baseline** · 比较 VQPrompt、CoDAPrompt、BiMC、FDR 等；消融用视觉特征替代残差，或关闭子空间旋转和提示模块。
- **Benchmark** · 在 CUB200、CIFAR100 和 miniImageNet 上做少样本类增量分类；报告分阶段 top-1、阶段均值及首末性能下降。
- **关键结果 / 消融** · 表 1 中 CIFAR100 平均准确率为 97.43%，VQPrompt 为 96.61%，性能下降分别为 1.64 与 1.41 个百分点。表 2 中 CUB200 最后阶段使用视觉特征为 78.59%，改用残差为 80.68%。
- **适用条件 / 局限** · 依赖基础类和新类有部分属性重合；属性完全不同或视觉文本特征未对齐时应重新验证残差码本。

**可复用机制** · 少样本增量分类时，将视觉与文本间残差信号量化后生成可适配的连续提示；用等架构直接量化视觉特征作对照，见表 2。

<a id="paper-unicomp"></a>

## UniComp: Rethinking Video Compression Through Informational Uniqueness

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yuan_UniComp_Rethinking_Video_Compression_Through_Informational_Uniqueness_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yuan_UniComp_Rethinking_Video_Compression_Through_Informational_Uniqueness_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 长视频的视觉词元预算有限，按帧统一保留可能重复编码相似画面，也可能丢掉识别细节所需的词元。
- **核心创新 / 方法** · UniComp 以所选集合能否近似重建被删特征为设计依据，先融合冗余帧组，再分配词元预算并做帧内选择与融合。
- **Baseline** · 比较完整输入、VisionZip、HoliTom、FastVid、FastV 等，并消融帧组融合、空间压缩与分配策略。
- **Benchmark** · 表 1 用 32 帧，在 LLaVA-OneVision-7B 上比较 10% 至 25% 保留率，报告 LongVideoBench、EgoSchema、MLVU 和 VideoMME 的准确率。表 2 固定 6272 词元再比较输入帧数。
- **关键结果 / 消融** · 表 1 保留 10% 时四项平均准确率为 59.80%，HoliTom 为 58.90%，完整输入为 59.95%。表 2 同预算最多读 320 帧时为 62.45%。
- **适用条件 / 局限** · 重建代理从各向同性高斯假设出发。词元数量相同也应另验实际耗时，以及高相似画面中短暂事件的召回。

**可复用机制** · 在视觉词元总预算固定时，按跨帧与帧内的信息独特性分配预算，可与均匀分配做受控对照。

<a id="paper-ad-gbc"></a>

## AD-GBC: Anisotropic Granular-Ball Skip-Connection Refiner for UNet-Based Medical Image Segmentation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Shen_AD-GBC_Anisotropic_Granular-Ball_Skip-Connection_Refiner_for_UNet-Based_Medical_Image_Segmentation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Shen_AD-GBC_Anisotropic_Granular-Ball_Skip-Connection_Refiner_for_UNet-Based_Medical_Image_Segmentation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 分割跳连中的点原型或各向同性区域难以概括形状和尺度各异的局部特征。
- **核心创新 / 方法** · AD-GBC 用可学中心和逐轴尺度表示区域，先将像素特征汇聚到区域，再回传精化特征；加入多样性及尺度一致性正则。
- **Baseline** · 以 Rolling-UNet 和 U-KAN 为插入骨干，对照裸骨干、各向同性尺度和两种几何正则的组合。
- **Benchmark** · 表 2 在 BUSI、GlaS、CVC-ClinicDB、ISIC17 上报告三次运行的 IoU 和 F1。表 4 在 GlaS 报告 IoU、F1 和 HD95。
- **关键结果 / 消融** · 表 4 中 Rolling-UNet-L 的 IoU 为 87.99%，各向同性粒球为 88.12%，无正则的逐轴尺度为 88.28%，两正则齐用为 89.63%。
- **适用条件 / 局限** · 证据来自医学二维分割；尺度建模与正则的单独收益需要在其他图像条件及计算预算下复测。

**可复用机制** · 用逐轴尺度把点原型推广为可微区域，并单独验证区域几何、正则与额外计算的收益。

<a id="paper-vlm-cc"></a>

## White-Balance First, Adjust Later: Cross-Camera Color Constancy via Vision-Language Evaluation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_White-Balance_First_Adjust_Later_Cross-Camera_Color_Constancy_via_Vision-Language_Evaluation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_White-Balance_First_Adjust_Later_Cross-Camera_Color_Constancy_via_Vision-Language_Evaluation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 色恒常学习容易拟合采集相机的颜色响应，视觉语言模型也难以直接从原始像素精确输出连续照明色值。
- **核心创新 / 方法** · 先按当前照明估计白平衡并映射到近似 sRGB；以物体颜色为先验，让微调后的视觉语言模型判断残余色偏方向，据此多轮更新估计。
- **Baseline** · 用 Gray-World 初始化；比较 Gray-Edge、CCMNet 等色恒常方法，以及视觉语言模型单步回归、迭代数值回归和离散迭代。
- **Benchmark** · 正文表 1–7 使用 Gehler-Shi、NUS-8、Cube+ 等，报告角误差及其均值、中位数和最差四分位，并做跨数据与跨传感器对照。
- **关键结果 / 消融** · 表 7 在留出的 Gehler-Shi 上，单步数值回归平均角误差 3.59°、迭代数值回归 1.70°、迭代离散反馈 1.52°。不微调版本为 14.33°。
- **适用条件 / 局限** · 依赖相机转换矩阵、可靠物体颜色先验及模型微调。多轮反馈的时延和遇到不典型物体配色时的误差需要分别验证。

**可复用机制** · 从初始估计渲染可读反馈，再用离散残差方向修正连续变量，可对照直接让视觉语言模型回归数值。

<a id="paper-attention-head-reallocation"></a>

## Reallocating Attention Across Layers to Reduce Multimodal Hallucination

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Lu_Reallocating_Attention_Across_Layers_to_Reduce_Multimodal_Hallucination_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Lu_Reallocating_Attention_Across_Layers_to_Reduce_Multimodal_Hallucination_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 多模态推理中视觉证据提取不足和后续推理漂移会同时造成错误，对所有层统一放大视觉注意力可能改变推理表现。
- **核心创新 / 方法** · 按深度和视觉词元注意力占比识别浅层感知头与深层推理头，在推理时对两类头的输出分别加权。
- **Baseline** · 以 Kimi-VL-A3B-Thinking、Ocean-R1、R1-Onevision 的原配置为起点，与 VCD、CGD、AGLA 和去掉任一加权支路的变体比较。
- **Benchmark** · 表 1–2 使用 MathVista mini、MathVision mini、HallusionBench、MMStar 和 SEED-Bench，报告准确率及适用任务的 F1。
- **关键结果 / 消融** · Kimi-VL 的 HallusionBench 准确率从 64.76% 到 68.19%。同一模型的 MathVision mini 去掉感知加权为 62.84%，高于完整方案 60.54%，说明不同任务的最优分配不同。
- **适用条件 / 局限** · 注意占比是功能代理，深度截点和放大系数需按模型复验。注意头加权依赖可访问内部注意力，已有消融显示两类增强并非各任务都互补。

**可复用机制** · 感知和推理错误可按注意力头功能分开干预，并以双向消融验证同一模型在看图和推理任务上的取舍。

<a id="paper-panoenv"></a>

## PanoEnv: Exploring 3D Spatial Intelligence in Panoramic Environments with Reinforcement Learning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Lin_PanoEnv_Exploring_3D_Spatial_Intelligence_in_Panoramic_Environments_with_Reinforcement_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Lin_PanoEnv_Exploring_3D_Spatial_Intelligence_in_Panoramic_Environments_with_Reinforcement_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 全景投影中的空间推理需要连续几何证据；结构化题训练容易改善答案格式，却可能无法迁移到开放题。
- **核心创新 / 方法** · 从三维真值构造几何奖励，以 GRPO 先训判断与选择题，再以平衡的开放题和结构化题混合训练。
- **Baseline** · 在 Qwen2.5-VL-7B-Instruct 上对比零样本、单阶段、仅结构题、仅开放题与反向课程。
- **Benchmark** · PanoEnv-QA 合成全景基准包含 1.48 万题；表 3–4 分别报告总准确率、判断题、选择题、开放题和两个模型评审分。
- **关键结果 / 消融** · 表 4 完整课程开放题 14.8%、总准确率 52.9%；仅结构题开放题 5.7%，低于未训练 6.4%；单阶段开放题 11.8%，反向课程 7.0%。
- **适用条件 / 局限** · 主要证据来自带精确三维标注的合成测试和单一微调骨干。课程选型需要控制不同阶段的超参数以及开放题评分方式。

**可复用机制** · 用结构化任务预热开放式空间问答时保留结构化回放，并以反向课程和单阶段对照检查格式熟练是否带来开放题迁移。

<a id="paper-etc"></a>

## Erasing Thousands of Concepts: Towards Scalable and Practical Concept Erasure for Text-to-Image Diffusion Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Seo_Erasing_Thousands_of_Concepts_Towards_Scalable_and_Practical_Concept_Erasure_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Seo_Erasing_Thousands_of_Concepts_Towards_Scalable_and_Practical_Concept_Erasure_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 大量概念共用表示，扩展移除规模时容易损伤相邻概念及图像质量。
- **核心创新 / 方法** · 以低秩重尾混合分布描述概念，在目标分布边界构造保留锚，再配合共享和专用编辑容量。
- **Baseline** · 对照 MACE、CPE、SPEED 等概念擦除方法。
- **Benchmark** · 正文表 2 比较 SDv1.4 与 SDv3.5 在人物、艺术风格和角色上的人工保留与画质；表 3 的 50 人物设置以 GCD 准确率、FID、KID 评估。
- **关键结果 / 消融** · 全文报告涉及超过 2,000 个概念的设置；小规模另报与未移除概念和 COCO 数据的比较，避免只用目标消失衡量成功。
- **适用条件 / 局限** · 依赖概念表达在嵌入空间中的可分性，人工画质评级不能覆盖所有提示和模型。

**可复用机制** · 大规模概念移除时把目标移除与邻近概念保留作为独立目标。

<a id="paper-talon"></a>

## TALON: Test-time Adaptive Learning for On-the-Fly Category Discovery

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_TALON_Test-time_Adaptive_Learning_for_On-the-Fly_Category_Discovery_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wu_TALON_Test-time_Adaptive_Learning_for_On-the-Fly_Category_Discovery_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 冻结特征和二值原型使连续新类样本可能被反复切成多个伪类别。
- **核心创新 / 方法** · 以间隔校准决定类别分配，在线更新语义原型并适配模型；三项可分别消融。
- **Baseline** · 比较 SMILE、PHE 与 DiffGRE 系变体，表 2 对照原型、模型更新和间隔校准。
- **Benchmark** · CUB-200-2011 与 Stanford Cars 等数据的无标签流，分别报告旧类、新类和整体准确率及估计类别数。
- **关键结果 / 消融** · Stanford Cars 整体准确率从基线 47.8% 到 53.5%，但 CUB 新类由 37.9% 变为 37.8%；CUB 上不带模型更新的校准加原型更新为 41.2%。
- **适用条件 / 局限** · 更新不一定兼顾旧类和新类，应按流顺序与类占比复验累积错误。

**可复用机制** · 在线类别发现应分开选择新类判阈和更新旧类表示。

<a id="paper-sensesearch"></a>

## SenseSearch: Empowering Vision-Language Models with High-Resolution Agentic Search-Reasoning via Reinforcement Learning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Chng_SenseSearch_Empowering_Vision-Language_Models_with_High-Resolution_Agentic_Search-Reasoning_via_Reinforcement_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Chng_SenseSearch_Empowering_Vision-Language_Models_with_High-Resolution_Agentic_Search-Reasoning_via_Reinforcement_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 视觉裁剪、图搜与文本查询的训练样本回报尺度不同，工具学习可能偏向单一能力。
- **核心创新 / 方法** · 给工具型视觉语言代理加入裁剪、图搜和文本检索，以 BN-GSPO 对优势做批归一。
- **Baseline** · 对照直接作答、检索增强及代理，表 3 无冷启动对照 GRPO 与 GSPO。
- **Benchmark** · MMSearch、HR-MMSearch 等搜索基准与 V* Bench、HR-Bench 等视觉评测；表 4 分别改变搜索和感知训练数据。
- **关键结果 / 消融** · 表 3 在 MMSearch、V*、HR-Bench 4K 的 BN-GSPO 为 56.72、79.05、69.12，GSPO 为 53.80、53.93、44.50。
- **适用条件 / 局限** · 搜索结果及接口质量会改变反馈分布，公开基准准确率不能覆盖所有查询成本和高分辨来源。

**可复用机制** · 工具混用时批量归一优势，独立检查检索和细粒度感知是否一起改善。

<a id="paper-reartgs-plus"></a>

## REArtGS++: Generalizable Articulation Reconstruction with Temporal Geometry Constraint via Planar Gaussian Splatting

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_REArtGS_Generalizable_Articulation_Reconstruction_with_Temporal_Geometry_Constraint_via_Planar_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wu_REArtGS_Generalizable_Articulation_Reconstruction_with_Temporal_Geometry_Constraint_via_Planar_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 两端观测重建易在多部件、复合关节及未观测状态中出现不一致几何。
- **核心创新 / 方法** · 联合学习分部件平面高斯和螺旋关节参数，通过一阶时间展开约束法线和深度。
- **Baseline** · 比较 REArtGS 等；表 3 去掉平面高斯、螺旋运动及相对距离。
- **Benchmark** · PARIS、ArtGS-Multi 及额外两个螺旋关节对象，不用深度监督，报告关节轴角度、位置、部件运动和 Chamfer 距离。
- **关键结果 / 消融** · 表 3 去螺旋运动时轴角误差 22.78、轴位置误差 88.26 mm，完整模型为 0.41、1.18 mm。
- **适用条件 / 局限** · 螺旋关节专门测试只有两个对象；强遮挡、非刚性及多关节同步可辨识性需另验。

**可复用机制** · 把关节类型统一为可分解螺旋运动，利用深度与法线时间一致性约束未见状态。

<a id="paper-quant-experts"></a>

## Quant Experts: Token-aware Adaptive Error Reconstruction with Mixture of Experts for Large Vision-Language Models Quantization

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Jia_Quant_Experts_Token-aware_Adaptive_Error_Reconstruction_with_Mixture_of_Experts_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Jia_Quant_Experts_Token-aware_Adaptive_Error_Reconstruction_with_Mixture_of_Experts_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 全局异常通道补偿忽略视觉和文字及同模态词元间的局部误差差异。
- **核心创新 / 方法** · 用共享低秩专家修复普遍误差，再路由特定词元到低秩局部专家。
- **Baseline** · 比较 RTN、SmoothQuant、LQER、MBQ；表 4 比较共享和路由专家配置。
- **Benchmark** · Qwen2VL-2B/72B 与 InternVL2-8B 等在不同权重、激活位宽评估 MMMU、OCRBench、ScienceQA、TextVQA、VizWiz 等。
- **关键结果 / 消融** · 表 3 的 Qwen2VL-72B W4A6，MBQ 与 QE 的 OCRBench 为 69.70 和 76.60，FP16 为 78.70。
- **适用条件 / 局限** · 依赖校准数据代表未来词元分布；应把适配器参数、路由时延与实际压缩收益一并核算。

**可复用机制** · 区分跨词元共享误差与特定词元的量化误差，再决定修复是否路由。

<a id="paper-omniret"></a>

## Efficient and High-Fidelity Omni Modality Retrieval

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Huynh_Efficient_and_High-Fidelity_Omni_Modality_Retrieval_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Huynh_Efficient_and_High-Fidelity_Omni_Modality_Retrieval_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 音频、图像、视频和文字合成查询时输入过长，单一读出词元容易丢失细节。
- **核心创新 / 方法** · 以共享注意力重采样压缩模态序列，再用注意力切片 Wasserstein 池化将保留的分布信息编码为检索向量。
- **Baseline** · 比较 QwenOmni 加 Gemma、CLAP、ImageBind 等；表 5 对照单 EOS 和 16 向量读出。
- **Benchmark** · 扩展 M-BEIR 的 13 类检索任务、MMEBv2 子集与 ACM 音视检索；表 5 在 100 万样本训练下报告 6 任务平均 Recall。
- **关键结果 / 消融** · 表 5 默认方案平均 Recall 50.2，单 EOS 43.4，16 向量为 49.8。
- **适用条件 / 局限** · 依赖多模态配对训练数据，ACM 各项难度不等，音频转字幕也可在部分设置提供强线索。

**可复用机制** · 分开验收固定长度重采样和分布式池化，避免多模态检索的单向量读出损失。

<a id="paper-synclip"></a>

## SynCLIP: Synonym-Coherent Language-Image Pretraining for Robust Open-Vocabulary Dense Perception

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xie_SynCLIP_Synonym-Coherent_Language-Image_Pretraining_for_Robust_Open-Vocabulary_Dense_Perception_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xie_SynCLIP_Synonym-Coherent_Language-Image_Pretraining_for_Robust_Open-Vocabulary_Dense_Perception_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 语义相近的类别提示可导致不同空间定位，常规 AP 无法衡量改写带来的下降。
- **核心创新 / 方法** · 用同义名称及定义扩展预训练文本，约束同义表达的注意力图一致，再强化对齐图中的相关区域。
- **Baseline** · 统一 F-ViT 检测骨干，比较 CLIPSelf 与 DeCLIP；分别去掉空间一致性和空间细化模块。
- **Benchmark** · 在 OV-COCO 和 OV-LVIS 比较开放词汇检测；OV-COCO 额外评估同义词替换前后的新类和基础类 AP50。
- **关键结果 / 消融** · 表 3 中新类 AP50 在改用同义词后分别下降 4.4、8.8 与 9.5 点，对应 SynCLIP、CLIPSelf、DeCLIP。表 4 中只开一致性模块的新类 AP50 为 41.1，两模块同开为 43.6。
- **适用条件 / 局限** · 依赖同义文本在图像语境确实等价，层级变化、歧义或有意修改定位条件时应重新验证。

**可复用机制** · 开放词汇定位应对同义改写单独验收，并训练同义提示间的空间注意力一致性。见 §4.3.2、表 3–4。

<a id="paper-adaspot"></a>

## AdaSpot: Spend Resolution Where It Matters for Precise Event Spotting

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xarles_AdaSpot_Spend_Resolution_Where_It_Matters_for_Precise_Event_Spotting_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xarles_AdaSpot_Spend_Resolution_Where_It_Matters_for_Precise_Event_Spotting_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 统一高分辨率视频处理浪费算力；全程低分辨率则可能丢掉判定事件时刻的动作细节。
- **核心创新 / 方法** · 低分辨率分支提取全局表示，用其响应图做时空平滑并选出每帧高分辨率局部窗，再融合局部特征；各分支带辅助监督。
- **Baseline** · 比较低分辨率或高分辨率单分支、未平滑响应、固定及自适应窗口，并对照已有精准事件检测器。
- **Benchmark** · Tennis、FineDiving、FineGym、F3Set 及足球 SN-BAS；报告基于容忍帧数的检测 mAP，并在 Tennis、SN-BAS 做部件消融。
- **关键结果 / 消融** · 未平滑的裁剪相对平滑裁剪在 Tennis 和 SN-BAS 分别下降 1.63 和 3.03 点；Tennis 自适应窗较固定窗提高 0.49 mAP@0，SN-BAS 则固定窗更优。
- **适用条件 / 局限** · 现有验证主要在体育视频；单窗可能忽略同帧多事件，平滑窗口在突发视角切换下也应复验。

**可复用机制** · 视频事件定位时，以时空平滑的低分辨率响应分配高分辨率裁剪，按事件规模测试固定和自适应窗口。见 §4、表 3。

<a id="paper-precision-recall-rank-tradeoff"></a>

## What Is the Optimal Ranking Score Between Precision and Recall? We Can Always Find It and It Is Rarely F1

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Pierard_What_Is_the_Optimal_Ranking_Score_Between_Precision_and_Recall_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Pierard_What_Is_the_Optimal_Ranking_Score_Between_Precision_and_Recall_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · F1 同等加权数值不保证模型排序同等接近精确率排名和召回率排名。
- **核心创新 / 方法** · 用 Kendall 排名相关形式化两项排序的折中，刻画 Fβ 排名路径，并给出合适 β 的计算表达式。
- **Baseline** · 比较固定 F1、论文中的先验无关固定分数和启发式折中。
- **Benchmark** · 包含六类分析或数值案例，其中一类是 53 组真实模型表现集合；报告式 16 定义的最优度。
- **关键结果 / 消融** · 真实集合中表 1 给出的 F1 平均最优度为 78.44%，启发式为 89.53%；闭式选择针对论文定义的折中目标。
- **适用条件 / 局限** · 适合排序折中目标；如果部署已明确误报和漏报代价，应按代价选择指标。候选组成或数据分布变化时要重新计算。

**可复用机制** · 如果综合排名希望兼顾精确率与召回率的排序，应针对候选集合计算 Fβ，而非默认 F1。见 §3.3–3.4、式 12、表 1。

<a id="paper-probabilistic-gs-pose-refinement"></a>

## Rethinking Pose Refinement in 3D Gaussian Splatting under Pose Prior and Geometric Uncertainty

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Kong_Rethinking_Pose_Refinement_in_3D_Gaussian_Splatting_under_Pose_Prior_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Kong_Rethinking_Pose_Refinement_in_3D_Gaussian_Splatting_under_Pose_Prior_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 单一初始位姿可能进入错误匹配盆地；渲染外观可信时，重建深度仍可能让重投影估计偏移。
- **核心创新 / 方法** · 围绕先验采样位姿，用基于 Fisher 信息的深度不确定性为几何约束加权，再对精化候选做加权汇总。
- **Baseline** · 比较 ACE、DFNet、Merapo 等先验与 GS-CPR 系列等精化对照，并对粒子数和噪声强度做敏感性评估。
- **Benchmark** · 7-Scenes、12-Scenes、Cambridge Landmarks，报告位移和旋转误差中位数，以及严格误差阈值内召回。
- **关键结果 / 消融** · 12-Scenes 的 2 cm、2° 阈值准确率达到 99.1%；Cambridge 用 DFNet 先验时，2 到 16 粒子将表 5 的平均位移误差从 11.8 降至 10.3 cm。
- **适用条件 / 局限** · 依赖重建场景和初始先验，粒子增加有推理成本；候选若均离真实盆地很远，或者图像缺少稳定对应，改进无法保证。

**可复用机制** · 定位精化应分开处理初始位姿偏差与高斯深度不确定性，分别用多候选和加权 PnP，见 §3.2–3.3。

<a id="paper-retouchiq-generalist-reward"></a>

## RetouchIQ: MLLM Agents for Instruction-Based Image Retouching with Generalist Reward

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_RetouchIQ_MLLM_Agents_for_Instruction-Based_Image_Retouching_with_Generalist_Reward_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wu_RetouchIQ_MLLM_Agents_for_Instruction-Based_Image_Retouching_with_Generalist_Reward_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 不同图像编辑指令需要不同质量标准，对固定参考做像素相似度容易忽略局部意图和审美权衡。
- **核心创新 / 方法** · 奖励模型根据编辑前后图像和指令先生成判分维度，再输出评分；通过策略生成样本补充奖励训练。
- **Baseline** · 比较 RETOUCHIQ-SFT、固定规则奖励、MonetGPT、JarvisArt 和通用多模态模型。
- **Benchmark** · RetouchEval 覆盖质量提升、风格改变和局部修图，报告像素误差和 GLM-4.5V 感知与语义评分；MIT-Adobe5K 报告 PSNR、LPIPS、SSIM。
- **关键结果 / 消融** · 表 1 质量提升赛道的综合评分，生成式奖励为 7.51，固定规则 6.87，SFT 6.69；局部修图的参考像素差异仍有更低的对照。
- **适用条件 / 局限** · 依赖策略能输出可执行工具参数，以及评判器可靠识别指令相关变化。换编辑工具或审美偏好时需独立复核奖励和人评相关性。

**可复用机制** · 主观编辑任务中，奖励模型可先生成指令相关的评判维度，再对执行结果评分，并用策略当前样本检查奖励排序。见 §4、图 5。

<a id="paper-anomaly-residual-evolution-field"></a>

## Anomaly-Related Residual Fields for Cross-domain Anomaly Detection

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Gao_Anomaly-Related_Residual_Fields_for_Cross-domain_Anomaly_Detection_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Gao_Anomaly-Related_Residual_Fields_for_Cross-domain_Anomaly_Detection_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 单步重建差包含正常外观变化及真正缺陷，域转移会放大这种混淆。
- **核心创新 / 方法** · 在逆扩散各步提取局部残差演化特征，以源域标签校准持久异常分量，再向无标注目标域对齐。
- **Baseline** · 比较 DDAD、DDPM、GLASS 和现有域适配或泛化方法；消融残差场与跨域对齐。
- **Benchmark** · 在 MVTec、VisA、DAGM 的九个源目标转移中比较异常检测，正文报告 AUROC，AUPRC 和 Rec@K 见附录。
- **关键结果 / 消融** · 表 1 平均 AUROC 为 95.22%，平均最高的对照 DDAD 为 82.21%；该结果支持联合方法并需结合表 2 区分两部件。
- **适用条件 / 局限** · 需要标注源域和可供对齐的目标域样本；若正常罕见纹理也产生持久残差，需按域重测误报率。

**可复用机制** · 做跨域视觉异常检测可比较末步重建残差与残差随去噪时间持续性的证据。见 §3、表 1–2。

<a id="paper-longstream"></a>

## LongStream: Long-Sequence Streaming Autoregressive Visual Geometry

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Cheng_LongStream_Long-Sequence_Streaming_Autoregressive_Visual_Geometry_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Cheng_LongStream_Long-Sequence_Streaming_Autoregressive_Visual_Geometry_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 始终参考首帧时，长视频的位姿预测要外推更远，易积累尺度漂移；训练与部署缓存不一致还会放大误差。
- **核心创新 / 方法** · 改用关键帧相对位姿，分开学习几何与尺度，训练复现流式缓存并在部署定期刷新。
- **Baseline** · 比较优化式重建、流式几何模型及内部缓存和尺度设计变体。
- **Benchmark** · 正文表 1–4 用 KITTI、vKITTI、TUM、7Scenes 等评估 ATE 与点云距离，采用在线不可见未来帧设置。
- **关键结果 / 消融** · 正文报告单 GPU 达 18 FPS，vKITTI 的表 3 中在所列序列均取得最佳精度。
- **适用条件 / 局限** · 绝对尺度监督依赖已校准数据。长间隔和跟踪丢失后仍应单测局部坐标拼接漂移。

**可复用机制** · 流式几何以局部关键帧作为位姿参考，将尺度估计独立处理，并在训练复现部署缓存状态。

<a id="paper-visref"></a>

## VisRef: Visual Refocusing while Thinking Improves Test-Time Scaling in Multi-Modal Large Reasoning Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Ghosal_VisRef_Visual_Refocusing_while_Thinking_Improves_Test-Time_Scaling_in_Multi-Modal_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Ghosal_VisRef_Visual_Refocusing_while_Thinking_Improves_Test-Time_Scaling_in_Multi-Modal_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 模型写出更长的文字推理时可能逐渐忽略图像，整图重复读入又占用推理预算。
- **核心创新 / 方法** · 无需微调，按当前推理状态用行列式点过程挑选相关且彼此多样的视觉词元并重新注入；用熵和最大轮数终止推理。
- **Baseline** · 对比标准思考、纯文本自反思和训练式 Look-Back，另做移除相关性或多样性的消融。
- **Benchmark** · 表 1 在 MathVision、MathVista、MM-Star 上测三个视觉推理模型的准确率，所有表中方法使用相同的自适应停止准则。
- **关键结果 / 消融** · InternVL3.5-8B 的 MathVista 准确率从标准推理 68.1% 和文本反思 73.9% 提升到 79.3%；固定计算预算的并行缩放另有对照。
- **适用条件 / 局限** · 需要能访问和重注视觉词元。视觉覆盖度、语义相关性及置信停止均需在新模型和分布上校验。

**可复用机制** · 推理中访问图像时同时按当前上下文相关性和视觉覆盖选证据，可在固定预算对照纯文本反思。

<a id="paper-ultra-diffusion-poser"></a>

## Ultra Diffusion Poser: Diffusion-Based Human Motion Tracking from Sparse Inertial Sensors and Ranging-based Between-sensor Distances

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Hollidt_Ultra_Diffusion_Poser_Diffusion-Based_Human_Motion_Tracking_from_Sparse_Inertial_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Hollidt_Ultra_Diffusion_Poser_Diffusion-Based_Human_Motion_Tracking_from_Sparse_Inertial_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 稀疏惯性信号会漂移，直接加传感器间测距特征仍可能预测出违背测距的姿态。
- **核心创新 / 方法** · 从 UWB 距离重建三维传感器布局，与惯性和测距一起作为扩散条件；采样时增加测距一致性反馈。
- **Baseline** · 比较已有惯性与测距姿态估计方法，以及去掉布局或测距引导的变体。
- **Benchmark** · 正文实验评估稀疏穿戴传感器的人体姿态估计，报告关节位置等误差。
- **关键结果 / 消融** · 正文报告相对既有方法关节位置误差最多下降 22%，并拆解布局和采样引导。
- **适用条件 / 局限** · 依赖测距和传感器安装可靠性。新遮挡条件下需区分几何退化和测距异常。

**可复用机制** · 同一距离观测可先解析出几何布局，再作为扩散采样一致性约束，并和把测距只当输入的方案做对照。

<a id="paper-pair-d-star"></a>

## Beyond Mimicry: Learning Whole-Body Human-Humanoid Interaction from Human-Human Demonstrations

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_Beyond_Mimicry_Learning_Whole-Body_Human-Humanoid_Interaction_from_Human-Human_Demonstrations_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_Beyond_Mimicry_Learning_Whole-Body_Human-Humanoid_Interaction_from_Human-Human_Demonstrations_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 人类协作演示转给人形机器人时，运动学轨迹看似相似也可能丢失接触；单纯模仿轨迹还会错过互动时机。
- **核心创新 / 方法** · PAIR 以两阶段物理约束重定向保留接触，D-STAR 用时相注意与多尺度空间分支分别组织动作时机和位置。
- **Baseline** · 表 1 比较单阶段及各重定向损失消融；表 3 比较行为克隆、纯强化学习、Diffusion Policy 和不同策略结构。
- **Benchmark** · 表 1–2 测关节及接触误差、接触精确与召回等；表 3 在六类交互任务上报告成功率。
- **关键结果 / 消融** · 正文报告把粗到细重定向合并成单阶段时接触 F1 降至 0.788。用同数据和控制器的 Diffusion Policy 对照表明互动策略设计存在独立贡献。
- **适用条件 / 局限** · 结论依赖接触标记、机器人形态和控制器。新接触任务还需独立测安全性与闭环执行。

**可复用机制** · 跨形态重定向先保留接触关系，策略再将接触时机和空间位置解耦学习。

<a id="paper-ppcl"></a>

## Pluggable Pruning with Contiguous Layer Distillation for Diffusion Transformers

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Ma_Pluggable_Pruning_with_Contiguous_Layer_Distillation_for_Diffusion_Transformers_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Ma_Pluggable_Pruning_with_Contiguous_Layer_Distillation_for_Diffusion_Transformers_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 扩散 Transformer 的深度与宽度裁剪通常各自需要恢复训练，多部署档位会重复付费。
- **核心创新 / 方法** · 用探测与层相似度变化选择连续可裁层段，并以交替教师与学生蒸馏联合训练不同深度和宽度的子模型。
- **Baseline** · 以完整 DiT 作教师，对照深度裁剪、宽度裁剪和多个压缩配置的恢复。
- **Benchmark** · 正文在多个多模态扩散 Transformer 上对照生成性能、参数规模以及不同裁剪档位。
- **关键结果 / 消融** · 正文报告部分配置减少一半参数时，关键客观指标损失低于 3%。
- **适用条件 / 局限** · 连续层段的可替换性取决于原主干和探测样本。参数减少要另测实际吞吐，未验证档位不能自动沿用。

**可复用机制** · 为多档部署预算训练可插拔连续层块，在一次联合蒸馏中覆盖深宽切换。

<a id="paper-appo"></a>

## APPO: Attention-guided Perception Policy Optimization for Video Reasoning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Du_APPO_Attention-guided_Perception_Policy_Optimization_for_Video_Reasoning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Du_APPO_Attention-guided_Perception_Policy_Optimization_for_Video_Reasoning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 视频强化学习按整条回答打分，可能把感知错误与后续推理错误混在同一个更新里。
- **核心创新 / 方法** · APPO 使用注意力把组内聚焦同一关键帧的词元作为感知单元，给这些词元更细粒度的训练信号。
- **Baseline** · 表 1 在相同数据与骨干上对比 SFT、GRPO、DAPO；图 6–7 消融词元与帧选择参数和注意力层。
- **Benchmark** · 在 Qwen2.5-VL 3B、7B 上使用多个视频基准，以总体和分级正确率评估。
- **关键结果 / 消融** · 正文报告相较 GRPO 或 DAPO 的增益为 0.5 至 4 个百分点，并单独检验所用注意力层。
- **适用条件 / 局限** · 注意力仅是感知归因代理，依赖帧采样、模型注意力结构和组内回答差异；只有答案正确率无法证明证据可靠。

**可复用机制** · 把组内不同回答中关注同一关键视频帧的词元放在一起分配感知信用，可与全序列共享奖励直接比较。

<a id="paper-graphvlm"></a>

## GraphVLM: Benchmarking Vision Language Models for Multimodal Graph Learning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_GraphVLM_Benchmarking_Vision_Language_Models_for_Multimodal_Graph_Learning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_GraphVLM_Benchmarking_Vision_Language_Models_for_Multimodal_Graph_Learning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 多模态图方法的骨干和信息入口差异使收益难以归因。
- **核心创新 / 方法** · 分别把 VLM 作为编码器、对齐器和预测器，并比较图结构提示、隐空间融合和微调。
- **Baseline** · 比较 UniGraph2 等图模型及 LLaVA-1.5、Qwen-VL、Qwen2.5-VL。
- **Benchmark** · 六个数据集的多模态图学习对照，分别评估零样本、上下文学习和监督微调；表 2 报告节点分类准确率。
- **关键结果 / 消融** · 表 4 和图 4 显示图结构加入预测、对齐角色的提升较一致，而对编码器做结构微调的收益不稳。
- **适用条件 / 局限** · 结论依图的模态信息与结构信号质量，迁移应保持骨干、监督和计算预算可比。

**可复用机制** · 以角色对照选择让视觉语言模型直接预测，还是只作为图模型的编码器或对齐器。

<a id="paper-dasq"></a>

## Rethinking Asymmetric Quantization: Hidden Symmetry in Vision Model Weights

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Mori_Rethinking_Asymmetric_Quantization_Hidden_Symmetry_in_Vision_Model_Weights_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Mori_Rethinking_Asymmetric_Quantization_Hidden_Symmetry_in_Vision_Model_Weights_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 非对称低位量化虽能补偿权重偏移，但附带零点运算且未必充分利用量化级。
- **核心创新 / 方法** · 将权重拆为近对称稠密核心与稀疏异常分量，分别做对称量化再合并。
- **Baseline** · 比较 RepQ-ViT 原非对称、改对称和加稀疏分量的版本。
- **Benchmark** · ImageNet 分类、检测和实例分割；图 7 用 FPGA 估计功耗，图 8 分析 ViT-S。
- **关键结果 / 消融** · 图 8 在 W4/A4 时原非对称和裸对称分别为 64.62% 与 61.56%；加入稀疏分量缩小差距，DASQ 超过原非对称 W5/A4 的准确率。
- **适用条件 / 局限** · 取决于异常值的稀疏程度及硬件稀疏执行支持；BOPs 不能独自代表部署耗时。

**可复用机制** · 先检查权重异常值移除后是否近对称，再选择无零点的低位算子。

<a id="paper-hesp"></a>

## Hierarchical Enhancement of Semantic Priors for Disentangled Text-Driven Motion Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Lv_Hierarchical_Enhancement_of_Semantic_Priors_for_Disentangled_Text-Driven_Motion_Generation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Lv_Hierarchical_Enhancement_of_Semantic_Priors_for_Disentangled_Text-Driven_Motion_Generation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 各向同性的动作生成潜空间可能压混动作类别、时序和文本语义。
- **核心创新 / 方法** · 以自适应 Gaussian VAE 学习更集中的潜区域，并使用动态跨模态记忆与分层跨模态注意。
- **Baseline** · 表 1 对照 SALAD、MoMask、MDM 等，表 2 对照标准 VAE，表 4 去除两种融合组件。
- **Benchmark** · HumanML3D、KIT-ML 测文本检索对齐与动作生成；HumanML3D 测 CH、DB 等聚类指标。
- **关键结果 / 消融** · 表 2 的 CH 从 11.95 提高到 48.81，DB 从 7.83 降到 5.39；表 4 分别去掉记忆或注意后均退化。
- **适用条件 / 局限** · 聚类改善不能确认因素独立可控，具身控制应用应另验接触及物理约束。

**可复用机制** · 动作生成若有独立语义因素，可先替换潜先验，再分别测语言融合和分层注意。

<a id="paper-movierecapsqa"></a>

## MovieRecapsQA: A Multimodal Open-Ended Video Question-Answering Benchmark

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Shaar_MovieRecapsQA_A_Multimodal_Open-Ended_Video_Question-Answering_Benchmark_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Shaar_MovieRecapsQA_A_Multimodal_Open-Ended_Video_Question-Answering_Benchmark_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 选择题给答题线索，开放视频 QA 又难靠单一参考字符串准确打分。
- **核心创新 / 方法** · 由电影解说转写构建开放问题及必需事实，将解说片段对齐到原片视觉和字幕，比较不同证据供给。
- **Baseline** · 表 1 对照 CinePile 等视频 QA 数据的问答格式，正文在完整电影、解说视觉与对齐片段间比较。
- **Benchmark** · 60 个 recap 视频衍生 8,231 道问题；四种输入设置控制可见片段，评分核查必要事实。
- **关键结果 / 消融** · 正文构建对齐原片与解说的事实级评分，可验原片无显式解说时证据是否足以支持自由答案。
- **适用条件 / 局限** · 选片来自解说创作者选取的情节，事实清单及自动判分可能漏掉其他合理表述。

**可复用机制** · 开放问答逐条验必要事实，并控制可见剪辑与对话范围，区分检索和多模态作答。

<a id="paper-quatrope"></a>

## Scalable Object Relation Encoding for Better 3D Spatial Reasoning in Large Language Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhou_Scalable_Object_Relation_Encoding_for_Better_3D_Spatial_Reasoning_in_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhou_Scalable_Object_Relation_Encoding_for_Better_3D_Spatial_Reasoning_in_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 绝对坐标加到对象表示后相对关系难读出，而枚举对象对使序列二次增长。
- **核心创新 / 方法** · 用四元数旋转位置编码在注意力点积中计算三维相对关系，配独立门控制其影响。
- **Baseline** · 同模型、同分割条件比较 Chat-Scene 与 3DGraphLLM 加或不加 QuatRoPE。
- **Benchmark** · 在三维指代和论文空间推理基准评估，报告 IoU 0.25、0.5 下准确率，并比较真值或预测分割。
- **关键结果 / 消融** · 表 2 中 Chat-Scene 1B 从 22.92 提到 27.38；3DGraphLLM 同样出现收益。
- **适用条件 / 局限** · 输入长度线性不代表注意力总计算线性，效果依赖对象定位与坐标可靠程度。

**可复用机制** · 将关系计算放到注意力相互作用里，保留对象线性长度，避免为对象对另加输入词元。

<a id="paper-psivg"></a>

## Physical Simulator In-the-Loop Video Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Foo_Physical_Simulator_In-the-Loop_Video_Generation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Foo_Physical_Simulator_In-the-Loop_Video_Generation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 视频扩散能生成可信外观，碰撞、重力和物体跨帧纹理仍可能失配。
- **核心创新 / 方法** · 从模板视频重建场景和网格，以模拟轨迹指导视频扩散，并用模拟像素对应调节外观特征。
- **Baseline** · 与 CogVideoX、HunyuanVideo、PISA-Seg、SG-I2V 和 MotionClone 等比较。
- **Benchmark** · 单及多物体、静止及移动相机的文本视频生成；报告掩码 IoU、对应像素误差、CLIP 和一致性及人评。
- **关键结果 / 消融** · 表 1 报告 SAM mIoU 0.84、对应像素 MSE 0.007；表 2 的人评偏好为 82.3%。
- **适用条件 / 局限** · 依赖模板三维重建和材料模拟近似，视觉对应不能验证真实力值或接触。

**可复用机制** · 先由物理模拟产生轨迹，再以投影对应约束视频外观，单独核运动与纹理。

<a id="paper-pr-iqa"></a>

## PR-IQA: Partial-Reference Image Quality Assessment for Diffusion-Based Novel View Synthesis

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Choi_PR-IQA_Partial-Reference_Image_Quality_Assessment_for_Diffusion-Based_Novel_View_Synthesis_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Choi_PR-IQA_Partial-Reference_Image_Quality_Assessment_for_Diffusion-Based_Novel_View_Synthesis_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 扩散新视角有结构和光度伪影，直接当稠密监督会污染 3DGS。
- **核心创新 / 方法** · 在不同相机的重叠区域计算局部质量，并以跨注意力补全质量图；只让高置信区域监督。
- **Baseline** · 比较 CrossScore、PuzzleSim 与完全参考质量指标，并消融注意次序及辅助输入。
- **Benchmark** · Mip-NeRF 360、Tanks and Temples、RealEstate10K；质量图看 PLCC/SRCC，稀疏重建看 PSNR、SSIM、LPIPS。
- **关键结果 / 消融** · 论文报告 DINOv2 质量图设定在三个重建集均有最高 PSNR、SSIM 和最低 LPIPS；图 4 展示伪影和错位减少。
- **适用条件 / 局限** · 几何质量估计依赖相机参数、视角重叠和可用参考，补全质量在遮挡区域可能不可靠。

**可复用机制** · 只采用其他真实视角能验证的伪视图局部，并用空间质量映射决定监督掩码。

<a id="paper-floverse"></a>

## FloVerse: Floor Plan-Guided Multi-Modal Navigation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_FloVerse_Floor_Plan-Guided_Multi-Modal_Navigation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_FloVerse_Floor_Plan-Guided_Multi-Modal_Navigation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 仅靠局部观察探索慢，平面图先验在点、图像和物体目标上的作用难直接比较。
- **核心创新 / 方法** · 用掩模态训练扩散规划器从不同目标与平面图规划，再以近场深度细化轨迹。
- **Baseline** · 表 2 对照保持其他组件相同但从头训练、移除图纸的 ThreeDiff w/o F。
- **Benchmark** · FloVerse-1.6K 的 HM3D 和 Gibson 4+ 设置，按 PointNav、ImageNav、ObjectNav 报成功率 SR 与路径加权 SPL。
- **关键结果 / 消融** · PointNav 加图纸后 SR 25.8 到 42.0，SPL 25.6 到 36.6；ImageNav 与 ObjectNav 两项也改善。
- **适用条件 / 局限** · 平面图不一定与现地通路一致，结果主要来自模拟；每步平均多条轨迹的成本须计入。

**可复用机制** · 隔离平面图先验和近场反馈，检验同一规划器对不同目标模态的收益。

<a id="paper-conceptpose"></a>

## ConceptPose: Training-Free Zero-Shot Object Pose Estimation using Concept Vectors

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Kuang_ConceptPose_Training-Free_Zero-Shot_Object_Pose_Estimation_using_Concept_Vectors_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Kuang_ConceptPose_Training-Free_Zero-Shot_Object_Pose_Estimation_using_Concept_Vectors_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 少量参考视角和跨域观测下，依赖对象特定训练的位姿估计难以直接迁移。
- **核心创新 / 方法** · 将视觉语言模型的概念显著图变为点云的逐点概念向量，在参考与查询点云之间匹配三维对应并估计相对位姿。
- **Baseline** · 比较 SIFT、Oryon、Horyon、Any6D 和 One2Any；消融概念提示及体素化。
- **Benchmark** · REAL275、Toyota-Light、YCB-Video、LINEMOD，双视角相对位姿报告 ADD(-S) 与 BOP 平均召回。
- **关键结果 / 消融** · 表 1 四个数据集的平均 ADD(-S) 为 51.6，Horyon 为 31.7；但 LINEMOD 的 BOP 平均召回为 31.0，低于 Horyon 的 34.4。
- **适用条件 / 局限** · 需同对象参考观测和可建三维对应的输入。每对约 7 秒，极端视角变化及严重遮挡下性能降低。

**可复用机制** · 无对象专用训练时，检验开放词汇概念显著向量能否替代外观特征作跨视角三维对应。见表 1–3。

<a id="paper-joppo"></a>

## JoPPO: Hierarchical Photography Assessment via Contrastive Joint Conditional Probabilistic Reinforcement Learning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_JoPPO_Hierarchical_Photography_Assessment_via_Contrastive_Joint_Conditional_Probabilistic_Reinforcement_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yang_JoPPO_Hierarchical_Photography_Assessment_via_Contrastive_Joint_Conditional_Probabilistic_Reinforcement_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 视觉语言模型的单一整体评分不易区分接近样本，也不能说明判定由哪些属性驱动。
- **核心创新 / 方法** · 先用合成摄影构图样本微调，再以批内细粒度属性分的条件分布构造总体分排序奖励，优化候选的预期胜率。
- **Baseline** · 对照去掉 JoPPO 和去掉 SFT 的版本，以及原有整体审美评分器。
- **Benchmark** · PICD、MMP 用排序准确率，CADB、PARA 用 Spearman 与 Pearson 相关，并在 PARA 检验属性到整体的评分。
- **关键结果 / 消融** · 表 3 中去掉 JoPPO 后 CADB 的 Spearman 相关从 0.629 降至 0.566，PARA 从 0.789 降至 0.723；MMP 准确率只由 0.624 降至 0.621。
- **适用条件 / 局限** · 依赖可信属性标签和总体偏好排序；当任务属性冲突或偏好人群变化时仍需检查条件分布与评分一致性。

**可复用机制** · 多属性视觉评分可按各属性条件下的总分胜率给强化学习信号，而不是直接优化一个整体分。见表 3–4。

<a id="paper-functional-mean-flow"></a>

## Functional Mean Flow in Hilbert Space

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Functional_Mean_Flow_in_Hilbert_Space_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Functional_Mean_Flow_in_Hilbert_Space_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 有限维网格上的单步生成目标难直接表达连续函数，并可能绑定训练采样分辨率。
- **核心创新 / 方法** · 在 Hilbert 空间定义函数流，用坐标采样实现单步 Functional Mean Flow；引入终点预测变体改善速度参数化的训练稳定性。
- **Baseline** · 比较单步 GEM、GASP、D2F，以及多步 ∞-Diff、DPF；论文另外比较终点与速度参数化。
- **Benchmark** · 除时间序列、偏微分方程和三维场外，表 3–4 比较 CelebA-HQ、FFHQ、Church 图像 FIDCLIP 及跨分辨率生成。
- **关键结果 / 消融** · 表 3 中 CelebA-HQ 64 上单步 FMF 的 FIDCLIP 为 3.48，单步 GASP 为 9.29；128 分辨率的 FMF 为 7.18，仍落后于 100 步 ∞-Diff 的 3.02。
- **适用条件 / 局限** · 需指定可计算的函数空间和坐标观察模型，单步速度不能消除跨分辨率误差，也不保证在全部质量指标领先多步方法。

**可复用机制** · 不规则坐标或多分辨率函数生成需要单步采样时，可对照 Hilbert 空间 Mean Flow 的终点预测与速度预测。见函数域构造和表 3–4。

<a id="paper-causalvad-shortcut-intervention"></a>

## CausalVAD: De-confounding End-to-End Autonomous Driving via Causal Intervention

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Tang_CausalVAD_De-confounding_End-to-End_Autonomous_Driving_via_Causal_Intervention_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Tang_CausalVAD_De-confounding_End-to-End_Autonomous_Driving_via_Causal_Intervention_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 驾驶策略可能过度依赖自车速度等训练相关量，在场景偏移或该输入失真时失效。
- **核心创新 / 方法** · 构造驾驶上下文原型字典，并对规划器稀疏场景查询做原型干预；利用受扰输入和场景泛化对照诊断捷径。
- **Baseline** · 基于 VAD-tiny，对比不干预与表 5 的单部件和双部件版本。
- **Benchmark** · nuScenes 开环规划报告 1–3 秒位移误差、碰撞率及扰动后表现，另在 NAVSIM 与 Bench2Drive 测泛化。
- **关键结果 / 消融** · 表 5 的平均 L2 从 0.74 降到 0.54 米，碰撞率从 0.44% 降到 0.11%；速度置零时 CausalVAD 的 L2 仍上升至 4.80 米。
- **适用条件 / 局限** · 潜在混杂由原型作近似，不能以原型干预证明因果变量完全可辨识；离线指标和所测场景不能替代新环境闭环验证。

**可复用机制** · 动作策略训练应对速度等容易形成捷径的输入做分桶和反事实扰动，并比较上下文原型干预前后退化。见表 2–5。

<a id="paper-adabet"></a>

## AdaBet: Gradient-free Layer Selection for Efficient Training of Deep Neural Networks

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Tenison_AdaBet_Gradient-free_Layer_Selection_for_Efficient_Training_of_Deep_Neural_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Tenison_AdaBet_Gradient-free_Layer_Selection_for_Efficient_Training_of_Deep_Neural_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 用完整反传计算层重要性容易超过端侧峰值显存；简单更新末端层的规则无法随数据分布适配。
- **核心创新 / 方法** · 根据前向层激活空间的 Betti 数排序，随后在给定预算下选择层和通道再训练。
- **Baseline** · 比较全量训练、迁移学习、Last-K Layers、Fisher、PruneTrain 和 ElasticTrainer。
- **Benchmark** · 十六组模型与数据集组合，报告 top-1；分开测量选层和重训练峰值内存，并评估选层耗时。
- **关键结果 / 消融** · 表 2 中 Stanford Dogs 上 ResNet50 的 AdaBet 为 75.52%，ElasticTrainer 为 72.55%；ViT 上则为 85.12% 和 87.79%。正文报告重训练平均峰值内存约少 40%。
- **适用条件 / 局限** · 选层来自无标签前向，但实际适配需要目标训练信号。拓扑统计及收集激活也有开销，网络和数据改变时应检查排序是否稳定。

**可复用机制** · 端侧适配前可先用无标签前向激活的拓扑特征挑选待训练层，避免完整反传才能决定选哪些层。见表 2–3。

<a id="paper-dual-ascent-diffusion"></a>

## Dual Ascent Diffusion for Inverse Problems

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Kim_Dual_Ascent_Diffusion_for_Inverse_Problems_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Kim_Dual_Ascent_Diffusion_for_Inverse_Problems_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 强生成先验容易得到自然却与观测不一致的解，直接约束观测又会损害感知质量。
- **核心创新 / 方法** · 把数据一致项和扩散先验拆成两段原变量更新，交替执行带噪近端去噪与对偶上升以协调两者。
- **Baseline** · 比较 DAPS 等求逆方法；同一 DDIM 噪声表下比较 DDiff-HQS、Diff-PnP-ADMM、Diff-PnP-HQS。
- **Benchmark** · FFHQ、ImageNet 的五种线性和三种非线性图像退化，报告 PSNR、SSIM、LPIPS、观测残差和时间。
- **关键结果 / 消融** · 表 2 的 10 张 FFHQ 4 倍超分消融中，完整模型 30.10 dB；去对偶项 25.45 dB，去加噪项 13.79 dB。
- **适用条件 / 局限** · 依赖可求解的观测算子、噪声模型及适合的预训练先验，十图消融不能替代跨域稳定性评估。

**可复用机制** · 扩散先验求逆问题时，分别消融观测一致性的对偶变量及噪声步骤，避免把所有收益归因于去噪器。见 §3、表 2。

<a id="paper-patch-ioner"></a>

## One Patch to Caption Them All: A Unified Zero-Shot Captioning Framework

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Bianchi_One_Patch_to_Caption_Them_All_A_Unified_Zero-Shot_Captioning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Bianchi_One_Patch_to_Caption_Them_All_A_Unified_Zero-Shot_Captioning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 全图视觉嵌入擅长描述整体，却很难为任意区域组合或非连续轨迹生成文本。
- **核心创新 / 方法** · 把对齐的图像 patch 作为基本描述单元，按区域或轨迹聚合成条件表示，再复用文本解码；不需区域级描述监督。
- **Baseline** · 比较 CLIP、ProxyCLIP、SigLIP2、DINO.txt 和 Talk2DINO 骨干并和零样本描述方法比较。
- **Benchmark** · 在 COCO 衍生集以及 Visual Genome、Flickr30k 等比较轨迹、稠密区域、区域集合和全图描述，报告 CIDEr 与 RefPAC-S。
- **关键结果 / 消融** · 表 1 中COCO Entities 区域集合描述的 CIDEr 为 Talk2DINO 109.1、DINO.txt 91.8、ProxyCLIP 40.6；正文也指出全图描述并非各项领先。
- **适用条件 / 局限** · 依赖预训练编码器保留局部语义，并需提供区域或轨迹。单纯聚合可能丢掉对象关系与空间顺序。

**可复用机制** · 开放词汇区域描述可先在对齐空间聚合局部 patch，再用同一解码器描述离散区域或轨迹。见表 1–2。

<a id="paper-masked-region-transformer-layer-editing"></a>

## Masked Region Transformer for Layered Image Generation and Editing at Scale

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Tang_Masked_Region_Transformer_for_Layered_Image_Generation_and_Editing_at_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Tang_Masked_Region_Transformer_for_Layered_Image_Generation_and_Editing_at_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 整图生成工件无法直接重组或只改某图层，裁切到可视范围的训练样本也无法保留画布外组件。
- **核心创新 / 方法** · 以区域和图层词元掩码统一文本到图层、图像分层和图层到图层编辑，并显式建模可超出画布的透明区域。
- **Baseline** · 比较 Qwen-Image-Layered 等方法；消融是否训练画布外图层及不同三任务混训配比。
- **Benchmark** · 评估图像分层、文本分层与跨图层编辑；表 2–3 汇报合成整图 FID、PSNR 和 SSIM。
- **关键结果 / 消融** · 表 3 中仅文本到层的 FID 为 16.15，加入图像到层为 15.68，三任务同训为 17.06；表 2 加入画布外数据提高 PSNR，但 FID 略差。
- **适用条件 / 局限** · 实现依赖分层透明训练样本、显式边界标记与大规模扩散骨干。任务混训并非总会改善每个子任务，非设计类自然图像还需量化。

**可复用机制** · 独立透明图层的生成、分解和局部编辑可用同一条件掩码参数化；任务混训比例要验证负迁移。见表 2–3。

<a id="paper-gr3d"></a>

## Grounded 3D-Aware Spatial Vision-Language Modeling

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Cheng_Grounded_3D-Aware_Spatial_Vision-Language_Modeling_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Cheng_Grounded_3D-Aware_Spatial_Vision-Language_Modeling_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 仅以文本描述位置容易丢失视觉对象指代和坐标。
- **核心创新 / 方法** · 在生成时为实体插入对应区域词元，用区域查询预测单目三维框并归一化相机内参。
- **Baseline** · 表5分别移除二维到三维步骤、预训练和相机归一化。
- **Benchmark** · Omni3D 用 AP15 和三维 AP，MM-GCoT 分测答案、定位与一致性。
- **关键结果 / 消融** · 表5在 KITTI 上，仅加入二维到三维步骤使三维 AP 从6.22提高至10.03，完整模型为14.75。
- **适用条件 / 局限** · 第二阶段受区域召回及相机内参约束，单目模糊时仍需检验三维误差。

**可复用机制** · 先落到图像区域再做三维推断，并将区域词元接回文本推理。

<a id="paper-qig-ptq"></a>

## Fine-Grained Post-Training Quantization for Large Vision Language Models with Quantization-Aware Integrated Gradients

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xiang_Fine-Grained_Post-Training_Quantization_for_Large_Vision_Language_Models_with_Quantization-Aware_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xiang_Fine-Grained_Post-Training_Quantization_for_Large_Vision_Language_Models_with_Quantization-Aware_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 按图像和文本各自统一赋权会忽略模态内部词元差异。
- **核心创新 / 方法** · 以量化输入相对全精度路径做积分梯度归因，用词元敏感度引导训练后校准。
- **Baseline** · 对照 FP16、MBQ 及以零参考和原任务输出为目标的归因配置。
- **Benchmark** · 正文表2–4测多个视觉语言模型的 W3A16、W4A8，在 ChartQA、VizWiz、MMMU 等上报告任务正确率。
- **关键结果 / 消融** · 表3中 InternVL2-26B 的 W3A16 在 ChartQA 与 VizWiz 优于 MBQ，正文报告与 FP16 的差异在2%以内。
- **适用条件 / 局限** · 逐词元归因依赖校准样本，离线校准代价和实际推理吞吐需分别报告。

**可复用机制** · 用实际量化误差归因逐词元校准，检查模态标签是否足以反映量化敏感度。

<a id="paper-dr-seg"></a>

## Dr. Seg: Revisiting GRPO Training for Visual Large Language Models through Perception-Oriented Design

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Sun_Dr._Seg_Revisiting_GRPO_Training_for_Visual_Large_Language_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Sun_Dr._Seg_Revisiting_GRPO_Training_for_Visual_Large_Language_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 分割候选需要空间覆盖，直接使用原始感知分数还可能造成更新不稳。
- **核心创新 / 方法** · Look-to-Confirm 扩展定位与确认过程，Distribution-Ranked Reward 按组内表现提供细粒度排序信号。
- **Baseline** · 对照感知任务的原始奖励、普通训练和组件变体。
- **Benchmark** · 正文表1–3覆盖分布内外推理分割，另测检测及计数，并报告分割与任务准确性指标。
- **关键结果 / 消融** · 正文显示原始奖励训练不稳定，组合设计在复杂视觉分割和分布外评估上改善。
- **适用条件 / 局限** · 需要可比较的感知反馈，分割上的结论不可直接推广至没有空间真值的任务。

**可复用机制** · 把尝试定位后的视觉确认和稳定排序奖励作为可分离因素，检验语言推理式 GRPO 能否迁移到感知。

<a id="paper-gr-gauge"></a>

## GR-Gauge: Cost-efficient Training Configuration By Gauging the Gradient Redundancy

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_GR-Gauge_Cost-efficient_Training_Configuration_By_Gauging_the_Gradient_Redundancy_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_GR-Gauge_Cost-efficient_Training_Configuration_By_Gauging_the_Gradient_Redundancy_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 超参搜索等到验证集分数明显变化才淘汰试验，消耗较多计算。
- **核心创新 / 方法** · 监测两个方向的梯度一致程度，用局部统计帮助选配置和停止低收益试验。
- **Baseline** · 表3对照随机搜索、Successive Halving、Hyperband、BOHB、CFO。
- **Benchmark** · ResNet18、NeuMF、BERT 等，报告达到验证目标的 GPU 时间，以及同预算验证表现。
- **关键结果 / 消融** · ResNet18 达85%用977秒，BOHB 用时约7.53倍；NeuMF 的55%低门槛上 BOHB 用时约0.61倍，节省并非普遍。
- **适用条件 / 局限** · 冗余标定依赖优化器及任务，低难度阈值应另测统计开销。

**可复用机制** · 按跨样本与跨更新两种梯度冗余估计学习率和批大小，验证能否降低搜索开销。

<a id="paper-droid-w"></a>

## DROID-SLAM in the Wild

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_DROID-SLAM_in_the_Wild_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_DROID-SLAM_in_the_Wild_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 动态场景中的像素误匹配会破坏默认静态的位姿估计。
- **核心创新 / 方法** · 将逐像素跨视图特征不一致转成不确定度，并参与可微光束平差。
- **Baseline** · 以 DROID-SLAM 为起点，对照 WildGS-SLAM、Splat-SLAM 等及不确定度组件消融。
- **Benchmark** · Bonn RGB-D Dynamic、TUM、DyCheck 和 DROID-W，评估 ATE RMSE 及运行帧率。
- **关键结果 / 消融** · 表4在 DROID-W 上平均 ATE RMSE 为0.230米，DROID-SLAM为1.460米；正文报告约10 FPS。
- **适用条件 / 局限** · 低纹理、反光及真实物体运动都可能导致特征不一致，权重估计需依环境校验。

**可复用机制** · 用多视特征不一致估计几何观测的不确定度，直接降低不可靠像素在位姿优化中的权重。

<a id="paper-robustseg"></a>

## Towards Robust Multi-Modal Semantic Segmentation with Teacher-Student Framework and Hybrid Prototype Distillation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Tan_Towards_Robust_Multi-Modal_Semantic_Segmentation_with_Teacher-Student_Framework_and_Hybrid_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Tan_Towards_Robust_Multi-Modal_Semantic_Segmentation_with_Teacher-Student_Framework_and_Hybrid_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 直接模仿全模态教师易将强模态的表示偏好带给缺失模态学生。
- **核心创新 / 方法** · 用跨模态原型对齐类语义，同时蒸馏类内差异，并用非主导模态的学生反馈修正教师。
- **Baseline** · 以 MIT-B0 等为骨干，消融跨模态原型、类内变化特征及反馈方案。
- **Benchmark** · 正文三个多模态分割数据集，按传感器可用组合分别计算 mIoU。
- **关键结果 / 消融** · 表3显示部分失效组合中，直接加入单模态变化将49.06%降至48.63%，改用主导特征选择后达49.10%。
- **适用条件 / 局限** · 收益依赖主导模态判定，未见传感器噪声和组合需要独立复测。

**可复用机制** · 缺失模态训练分开蒸馏共享语义和模态专属变化，并验证弱模态反馈方向。

<a id="paper-kontinuous-kontext"></a>

## Kontinuous Kontext: Continuous Strength Control for Instruction-based Image Editing

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Parihar_Kontinuous_Kontext_Continuous_Strength_Control_for_Instruction-based_Image_Editing_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Parihar_Kontinuous_Kontext_Continuous_Strength_Control_for_Instruction-based_Image_Editing_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 不同强度难以只靠文本表述，图像端点插值不一定保持内容和编辑语义。
- **核心创新 / 方法** · 用轻量投影器将编辑指令与强度标量变为调制系数，利用过滤后的合成编辑序列训练。
- **Baseline** · 以既有指令编辑器为起点，对比 Diffmorpher、Freemorph、WAN-Video 等，以及文本空间条件和无过滤变体。
- **Benchmark** · 正文表1–3以编辑平滑度及 CLIP 方向一致性衡量，并辅以人评。
- **关键结果 / 消融** · 表3调制条件平滑误差0.329，文本空间条件为1.468；去掉数据过滤时为0.483。
- **适用条件 / 局限** · 合成编辑需符合强度顺序，平滑度也无法单独保证身份保持与单调改变。

**可复用机制** · 将编辑强度映射到模型调制空间，直接对照在文本嵌入或成图之间做插值。

<a id="paper-raynova"></a>

## RAYNOVA: Scale-Temporal Autoregressive World Modeling in Ray Space

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xie_RAYNOVA_Scale-Temporal_Autoregressive_World_Modeling_in_Ray_Space_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xie_RAYNOVA_Scale-Temporal_Autoregressive_World_Modeling_in_Ray_Space_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 多视视频分别生成空间和时序内容时，跨相机约束与长时一致性容易脱节。
- **核心创新 / 方法** · 以相对 Plücker 射线作为跨视图、帧和尺度的位置编码，在尺度与时间双因果顺序上生成，并以递归训练减轻漂移。
- **Baseline** · 表 1 对照 MagicDrive、DriveDreamer；表 2 比较 Panacea、X-Drive 与真实数据上限。
- **Benchmark** · nuScenes 多视视频，FID、FVD、吞吐；以 StreamPETR、SparseFusion 验对象条件下的 NDS。
- **关键结果 / 消融** · 表 2 中相机 NDS 41.9 对 Panacea 32.1，多传感 NDS 72.0 对 X-Drive 69.6。
- **适用条件 / 局限** · 主要评估驾驶视频，检测一致不代表控制动力学正确；跨相机需可获得射线几何。

**可复用机制** · 在统一射线坐标中按尺度和时间联合自回归，避免相机换位时复用固定视图索引。

<a id="paper-spegc"></a>

## SPEGC: Continual Test-Time Adaptation via Semantic-Prompt-Enhanced Graph Clustering for Medical Image Segmentation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Du_SPEGC_Continual_Test-Time_Adaptation_via_Semantic-Prompt-Enhanced_Graph_Clustering_for_Medical_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Du_SPEGC_Continual_Test-Time_Adaptation_via_Semantic-Prompt-Enhanced_Graph_Clustering_for_Medical_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 持续测试时适应的局部相似度易被噪声污染，错误伪标签累积导致退化。
- **核心创新 / 方法** · 分开学习共有与域异质语义提示，用最优传输稀疏图边，以簇级结构引导更新。
- **Baseline** · 对照无适应、NC-TTT 等；表 4 消融模块。
- **Benchmark** · 眼底 OD/OC 及息肉分割按源域训练和其他域连续测试，五次运行，报告 Dice。
- **关键结果 / 消融** · 表 1 的 OD/OC 跨域总体 DSC 83.10%，表 4 报告完整组合较基线提升 10.35 点。
- **适用条件 / 局限** · 聚类依赖增强特征保持真实结构；新检查设备及改变域顺序时需监测边界漂移。

**可复用机制** · 持续域漂移时先构造稳健图，再以簇级一致性更新决策边界。

<a id="paper-extrinsplat"></a>

## ExtrinSplat: Decoupling Geometry and Semantics for Open-Vocabulary Understanding in 3D Gaussian Splatting

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Ding_ExtrinSplat_Decoupling_Geometry_and_Semantics_for_Open-Vocabulary_Understanding_in_3D_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Ding_ExtrinSplat_Decoupling_Geometry_and_Semantics_for_Open-Vocabulary_Understanding_in_3D_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 逐高斯写入语义向量有高存储成本，也会混淆同一对象不同粒度的说法。
- **核心创新 / 方法** · 将高斯聚为可重叠的多粒度对象组，由 VLM 生成文字假设构建几何外索引。
- **Baseline** · 比较 LEGaussians、LangSplat、LUDVIG 等嵌入法。
- **Benchmark** · LERF 开放词汇三维对象选择的 mIoU，并测语义分割以及 Figurines 适配资源。
- **关键结果 / 消融** · 表 2 平均 mIoU 54.3 对 LUDVIG 50.4；表 1 的语义存储约 3 MB，而对照有约 3 GB 的配置。
- **适用条件 / 局限** · 需有可分割的几何和足够视图供文字描述；小对象的索引误判仍可能扩散。

**可复用机制** · 把空间几何和可多义的对象语义分开存，语义可以多粒度重建索引。

<a id="paper-svft"></a>

## Vocabulary Scaling Law: Tuning Open-vocabulary Predictors for Their Openness

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Vocabulary_Scaling_Law_Tuning_Open-vocabulary_Predictors_for_Their_Openness_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_Vocabulary_Scaling_Law_Tuning_Open-vocabulary_Predictors_for_Their_Openness_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 只优化闭集类时，加入未见标签会改变竞争关系并降低开放集性能。
- **核心创新 / 方法** · 约束子模选择信息量大的类别名，微调类名嵌入并约束训练和开放类的嵌入正交性。
- **Baseline** · 与闭集提示微调及其他开放词表方法比较；表 1 比较不同模型和词表规模。
- **Benchmark** · CIFAR100、ImageNet Entity13 与 Living17，按扩大词表报告闭集准确及开放性指标。
- **关键结果 / 消融** · 正文观察到只调闭集提示难以保持稳定和扩展性，SVFT 在多设置改善两类指标。
- **适用条件 / 局限** · 依赖候选类覆盖和类名质量；词表外仍可能出现语义近邻冲突。

**可复用机制** · 按子模覆盖挑选训练类之外的词表进行微调，随词表扩大验开放性。

<a id="paper-imagecritic"></a>

## The Consistency Critic: Correcting Inconsistencies in Generated Images via Reference-Guided Attentive Alignment

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Ouyang_The_Consistency_Critic_Correcting_Inconsistencies_in_Generated_Images_via_Reference-Guided_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Ouyang_The_Consistency_Critic_Correcting_Inconsistencies_in_Generated_Images_via_Reference-Guided_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 参考生成图会错写局部文字、纹理或标志，直接重生成可能改动空间布局。
- **核心创新 / 方法** · 构造参考、损坏输入和真值三元组，以注意对齐损失和细节编码训练局部后编辑。
- **Baseline** · CriticBench、DreamBench++ 对比原生成、其他后处理及局部编辑；表 3 消融对齐损失和细节编码。
- **Benchmark** · 多类生成器的定制图片上用 CLIP-I、DINO 与 DreamSim 分别核对一致性。
- **关键结果 / 消融** · 表 3 独立比较两种模块，表 1–2 报告跨多个生成器的编辑前后一致性。
- **适用条件 / 局限** · 依赖退化分布覆盖及可靠参考图，感知相似度难完全替代小文字和标识的真值。

**可复用机制** · 训练参考校正器时用可控降质作监督，并分开核对布局与细节。

<a id="paper-styledoctor"></a>

## StyleDoctor: Towards Specialist Reward Model for Style-centric Generation Tasks

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/He_StyleDoctor_Towards_Specialist_Reward_Model_for_Style-centric_Generation_Tasks_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/He_StyleDoctor_Towards_Specialist_Reward_Model_for_Style-centric_Generation_Tasks_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 通用人类偏好奖励对画风不敏感，可能奖励内容或美学而忽略风格。
- **核心创新 / 方法** · 用风格偏好对训练多模态奖励模型，加入专用风格表征词元，同时预测图对一致和文本风格对齐。
- **Baseline** · 表 2 比较 CSD、CLIP 等视觉编码及多模态模型。
- **Benchmark** · 约 40 万样本和 1,000 风格类别，测风格检索准确及多模态风格理解并评生成。
- **关键结果 / 消融** · 正文表 2 将检索与风格理解分开，论文报告专门奖励在两类评测及风格引导生成上提高。
- **适用条件 / 局限** · 风格归属及偏好受标注定义影响，同内容下的独立风格对照仍重要。

**可复用机制** · 需要风格时单独学习奖励并把图图风格对应和图文风格对齐分验。

<a id="paper-contrastive-attention-fusion"></a>

## Where Does Vision Meet Language? Understanding and Refining Visual Fusion in MLLMs via Contrastive Attention

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Song_Where_Does_Vision_Meet_Language_Understanding_and_Refining_Visual_Fusion_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Song_Where_Does_Vision_Meet_Language_Understanding_and_Refining_Visual_Fusion_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 多模态注意力在无关区域也可持续偏高，平均注意权重难指示图文融合位置。
- **核心创新 / 方法** · 逐层遮蔽测融合；推理时比较早期融合与末层注意变化以突出文本相关区域。
- **Baseline** · 表 1 对照原 LLaVA、CD 等行为干预，在多骨干比较。
- **Benchmark** · 跨 GQA、VQAv2、OKVQA、VizWiz、TextVQA、DocVQA、MMBench 计准确率。
- **关键结果 / 消融** · 论文观察融合集中在特定层，部分模型有末段重新取视觉；对照显示免训练注意调整改善综合表现。
- **适用条件 / 局限** · 层位置依模型而变，不能默认相同层号或将注意变化直接视为因果解释。

**可复用机制** · 逐层屏蔽视觉再做末层对照，定位真正参与融合的层及无关注意噪声。

<a id="paper-evdehaze"></a>

## From Events to Clarity: The Event-Guided Diffusion Framework for Dehazing

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_From_Events_to_Clarity_The_Event-Guided_Diffusion_Framework_for_Dehazing_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_From_Events_to_Clarity_The_Event-Guided_Diffusion_Framework_for_Dehazing_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · RGB 去雾受动态范围制约，生成过程可能丢掉真实边缘及亮度。
- **核心创新 / 方法** · 将稀疏事件的结构信息投到扩散潜空间，通过跨注意引导恢复。
- **Baseline** · 表 2 对照 ResShift、移除事件、移除跨注意。
- **Benchmark** · SOTS 及 NH-HAZE 用 PSNR、SSIM；另用同步 RGB—事件设备收集真实重雾样本。
- **关键结果 / 消融** · 表 2 完整法为 34.12 dB、0.986；无事件为 30.15 dB、0.957，无跨注意为 33.65 dB、0.981。
- **适用条件 / 局限** · 需注册并同步的事件相机，低运动区域或事件噪声分布变化可能限制结构增益。

**可复用机制** · 把高动态事件边缘作为独立生成条件，按无事件和无跨注意分别量化。

<a id="paper-d2-align"></a>

## Taming Preference Mode Collapse via Directional Decoupling Alignment in Diffusion Reinforcement Learning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Taming_Preference_Mode_Collapse_via_Directional_Decoupling_Alignment_in_Diffusion_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_Taming_Preference_Mode_Collapse_via_Directional_Decoupling_Alignment_in_Diffusion_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 扩散模型过度追逐通用奖励时可能收敛到少数高分风格或光照模式。
- **核心创新 / 方法** · 保持奖励模型冻结，在其嵌入空间学习方向校正，并以校正信号更新生成模型。
- **Baseline** · 用 FLUX 及直接按偏好奖励优化的方法对照，表 1–2 比较两种奖励配置。
- **Benchmark** · DivGenBench 测身份、风格覆盖及空间多样性，同时验语义对齐和偏好。
- **关键结果 / 消融** · 正文区分偏好变好与模式收窄；表 2 分维度报告多样性，避免单用一个质量分数选策略。
- **适用条件 / 局限** · 需确定偏置方向能从偏好信号中分离；各多样性指标与用户需求的关系应另作核验。

**可复用机制** · 对生成偏好奖励的偏置方向单独校正，分开监测奖励增益与多样性。

<a id="paper-docprune"></a>

## DocPrune: Efficient Document Question Answering via Background, Question, and Comprehension-aware Token Pruning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Choi_DocPrune_Efficient_Document_Question_Answering_via_Background_Question_and_Comprehension-aware_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Choi_DocPrune_Efficient_Document_Question_Answering_via_Background_Question_and_Comprehension-aware_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 文档页面有大片背景，但自然图像裁剪规则会误删稀疏的文本、表或图像证据。
- **核心创新 / 方法** · 渐进执行背景过滤、问题相关性过滤和按理解程度选择剪枝层。
- **Baseline** · 对照原 M3DocRAG、固定注意力比例及其他词元削减策略。
- **Benchmark** · M3DocRAG 报告不同证据模态的 EM、F1，编码和解码吞吐及 FLOPs。
- **关键结果 / 消融** · 论文报告编码与解码吞吐为 3.0 倍和 3.3 倍，F1 提升 1.0 点。
- **适用条件 / 局限** · 小字、密集表格及跨页证据可能在早期裁除，迁移时应按证据类型分层测。

**可复用机制** · 先裁文档背景，再按问题挑证据，最后依模型理解程度调起始层。

<a id="paper-pour-representation-unlearning"></a>

## POUR: A Provably Optimal Method for Unlearning Representation via Neural Collapse

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Le_POUR_A_Provably_Optimal_Method_for_Unlearning_Representation_via_Neural_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Le_POUR_A_Provably_Optimal_Method_for_Unlearning_Representation_via_Neural_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 分类器不再输出某类时，内部仍可能保留识别该类的信息。
- **核心创新 / 方法** · 利用神经坍塌下的类均值几何构造正交投影；另用特征蒸馏修改编码器，并以 CKA 构造表征遗忘评分。
- **Baseline** · 对照原模型、重训、随机标签、梯度上升和边界调整；分别比较只修改分类端的 POUR-P 与修改表征的 POUR-D。
- **Benchmark** · CIFAR-10/100、PathMNIST，另含 CLIP 与分割验证；记录保留/遗忘类分类、重新训练探针、CKA 和 RUS。
- **关键结果 / 消融** · 表 1 中 POUR-D 的保留类准确率 92.86%，遗忘类 0.37%；相对原模型的 RUS 为 0.85。POUR-P 分类遗忘类为 0%，但编码器未改变，表征指标不参与比较。
- **适用条件 / 局限** · 最优性依赖类先验平衡、近似各向同性等假设，实测表征相似度与分类错误率不能单独证明训练样本已被遗忘。

**可复用机制** · 类别遗忘验收应分别检查输出、可恢复表征和保留类结构；神经坍塌近似成立时再比较投影与蒸馏。见定理 4.2 和表 1。

<a id="paper-flowmotion"></a>

## FlowMotion: Training-Free Flow Guidance for Video Motion Transfer

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_FlowMotion_Training-Free_Flow_Guidance_for_Video_Motion_Transfer_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_FlowMotion_Training-Free_Flow_Guidance_for_Video_Motion_Transfer_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 取视频扩散模型内部注意力或特征计算运动引导，往往内存占用较大且需要接入模型内部。
- **核心创新 / 方法** · 从早期潜预测中提取跨帧运动表示，使生成视频与源视频运动对齐，并用速度正则稳定更新。
- **Baseline** · 比较 DiTFlow、SMM、DeT、MotionInversion；消融速度正则及对齐，并比较不同引导项的显存。
- **Benchmark** · 在所构建的视频运动迁移样本上报告文本相似、运动保真、时间一致性、运行时间和显存，另做人评。
- **关键结果 / 消融** · 表 1 移植运动保真为 0.850，DiTFlow 为 0.691；显存分别为 19.3 和 63.5 GB。表 3 去速度正则后运动保真降至 0.809。
- **适用条件 / 局限** · 对照骨干不同，不能把整段速度差都归因于引导方式；需要可访问流模型潜预测，遮挡或源目标几何显著不同仍应复测。

**可复用机制** · 无训练视频运动迁移可直接用早期潜预测构造时间引导，并分开消融速度正则。见表 1、3–4。

<a id="paper-skyra-grounded-video-detection"></a>

## Skyra: AI-Generated Video Detection via Grounded Artifact Reasoning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Skyra_AI-Generated_Video_Detection_via_Grounded_Artifact_Reasoning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Skyra_AI-Generated_Video_Detection_via_Grounded_Artifact_Reasoning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 仅报告视频真假分数难以复核模型是否识别了相关证据。
- **核心创新 / 方法** · 先用人标视觉证据训练多模态检测器的解释和分类，再用强化学习改进检测维度。
- **Baseline** · 比较去解释监督、去冷启动及去强化学习，并与专用检测器及通用多模态模型比较。
- **Benchmark** · ViF-Bench 和 GenVideo 检测，评估准确率、召回、F1，以及变换后稳健性。
- **关键结果 / 消融** · 表 4 的监督阶段有解释训练时 F1 为 88.76，去解释监督后为 16.72；追加强化学习的完整 F1 为 90.27。
- **适用条件 / 局限** · 依赖人工证据标签覆盖，预测理由可读不能证明实际分类因果，也需独立核验新生成器和现实视频分布。

**可复用机制** · 合成视频检测应将判断依据作为带人工标注的中间监督，并分别比较二分类和解释训练。见表 3–4。

<a id="paper-lattice-voxset"></a>

## LATTICE: Democratize High-Fidelity 3D Generation at Scale

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Lai_LATTICE_Democratize_High-Fidelity_3D_Generation_at_Scale_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Lai_LATTICE_Democratize_High-Fidelity_3D_Generation_at_Scale_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 无结构潜向量便于压缩几何，但生成器缺少显式的空间锚来匹配局部细节。
- **核心创新 / 方法** · 先生成稀疏粗体素几何锚，再用流 Transformer 生成体素索引下的压缩向量，解码细粒度几何。
- **Baseline** · 比较 VecSet 类查询与 VoxSet 表示，以及 Michelangelo、Craftsman、Trellis、Hunyuan3D 和 Direct3D-s2。
- **Benchmark** · 对三维几何重建和图像条件生成分别评估，生成报告 ULIP、Uni3D 相似度。
- **关键结果 / 消融** · 表 2 的 Uni3D 文本相似度为 0.254，Hunyuan3D 2.0 为 0.251，图像相似度均为 0.315；图 10 对粗体素查询与 VoxSet 的细节贡献做了比较。
- **适用条件 / 局限** · 粗体素锚若漏掉细小或分离部件，后续细化未必可恢复；自动嵌入相似度与局部拓扑或可制造性是不同指标。

**可复用机制** · 三维资产生成可给压缩潜令牌绑定粗体素位置再生成精细几何，分别检查同分布重建和稀疏锚推理差异。见图 10、表 1–3。

<a id="paper-deltaworld-delta-tokens"></a>

## A Frame is Worth One Token: Efficient Generative World Modeling with Delta Tokens

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Kerssies_A_Frame_is_Worth_One_Token_Efficient_Generative_World_Modeling_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Kerssies_A_Frame_is_Worth_One_Token_Efficient_Generative_World_Modeling_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 逐帧生成多个可能未来计算昂贵，压缩完整帧又容易丢失跨帧小变化。
- **核心创新 / 方法** · 在视觉基础模型特征空间将相邻帧差压成连续单个令牌，联合预测多个未来并监督最匹配的样本。
- **Baseline** · 比较判别 DINO-world、直接多假设训练、整帧压缩，以及其他生成世界模型。
- **Benchmark** · VSPW 和 Cityscapes 的短中期稠密分割预测，另看深度预测；报告最佳与平均 mIoU、FLOPs、时延与内存。
- **关键结果 / 消融** · 表 2 中 Cityscapes 的中期最佳/平均 mIoU，整帧压缩为 42.7/35.5，差值压缩为 48.7/45.5；差值压缩计算量略高于整帧压缩。
- **适用条件 / 局限** · 主要验证约 0.2 和 0.6 秒未来，单令牌能否保留突然的大变化和任务所需细节，以及更长滚动误差，仍需独立检查。

**可复用机制** · 多未来世界模型可压缩相邻冻结视觉表示的差值，再对均值和最佳样本同时验收，避免奖励随机发散。见表 2–3。

<a id="paper-harmony-synccfg"></a>

## Harmony: Harmonizing Audio and Video Generation through Cross-Task Synergy

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Hu_Harmony_Harmonizing_Audio_and_Video_Generation_through_Cross-Task_Synergy_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Hu_Harmony_Harmonizing_Audio_and_Video_Generation_through_Cross-Task_Synergy_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 联合去噪的噪声状态同时变化，常规条件引导改善各模态保真时仍可能漏掉时间同步。
- **核心创新 / 方法** · 加入音频给定的视频生成和视频给定的音频生成辅助训练，分离全局风格和局部时间交互；推理时单独增强音视频对齐信号。
- **Baseline** · 对照只用常规引导的基线，依次加入全局局部交互、时间尺度位置对齐、跨任务训练和 SyncCFG。
- **Benchmark** · 比较环境声、说话人与复杂场景，表 3 在人类语音数据消融 Sync-C、Sync-D 和 IB；另报告视听质量。
- **关键结果 / 消融** · 加 SyncCFG 前后 Sync-C 从 5.09 到 6.51，Sync-D 从 10.16 到 8.63；语音消融使用的设置与综合对比不同。
- **适用条件 / 局限** · 需要音视频配对及时间尺度校准，语音同步指标不能覆盖所有环境音或多发声源，部署需考虑引导开销。

**可复用机制** · 音视频联合扩散可把跨模态时间对齐引导与各模态的条件引导分开，并以同步指标独立消融。见 §3.4、表 3。

<a id="paper-mamma"></a>

## MAMMA: Markerless Accurate Multi-person Motion Acquisition

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Velasquez_MAMMA_Markerless_Accurate_Multi-person_Motion_Acquisition_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Velasquez_MAMMA_Markerless_Accurate_Multi-person_Motion_Acquisition_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 稀疏关节点难以约束多人接触与遮挡时的人体表面。
- **核心创新 / 方法** · 从分割掩码和每个标志点的可学查询得到接触与可见性感知的密集二维对应，再做多视人体拟合。
- **Baseline** · 正文表1–2对照 Look-Ma、CameraHMR、带或不带 SAM2 掩码的 MammaNet。
- **Benchmark** · 在 RICH、MOYO、Harmony4D、CHI3D 等报告标志点误差，多人表按人体框 IoU 大于0.5挑高重叠样本；另测穿透与三维拟合。
- **关键结果 / 消融** · 表2 Harmony4D 中 CameraHMR 为32.84，MammaNet 无掩码31.96，加入 SAM2 掩码后18.33。
- **适用条件 / 局限** · 掩码漏分会传播到对应估计；多视训练结论应在视角少或被同时遮挡时复测。

**可复用机制** · 用逐人掩码及可见性约束密集表面对应，优先解决互相遮挡中的身份串扰。

<a id="paper-lapnet"></a>

## Dual Graph Regularized Deep Unfolding Network for Guided Depth Map Super-resolution

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhong_Dual_Graph_Regularized_Deep_Unfolding_Network_for_Guided_Depth_Map_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhong_Dual_Graph_Regularized_Deep_Unfolding_Network_for_Guided_Depth_Map_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 同一图结构容易把颜色纹理误写入深度，直接迭代图优化又增加处理成本。
- **核心创新 / 方法** · 在引导深度超分辨中用双图拉普拉斯约束保留两类结构，并展开优化为固定步骤网络。
- **Baseline** · 正文表1–2对比既有引导深度超分方法，图6–7比较正则和展开迭代设置。
- **Benchmark** · 在合成降采样基准和真实 RGB-D-D 中报告深度 RMSE，按超分倍率分组。
- **关键结果 / 消融** · 表1–2报告误差比较，图7显示迭代数可单独调以权衡重建精度和计算成本。
- **适用条件 / 局限** · 需要配准的导引图像，颜色边缘与深度边缘不一致时应另行检查纹理串扰。

**可复用机制** · 分别编码导引图像结构和深度本身的结构，再将图正则求解展开成可训练迭代。

<a id="paper-vit-robustness-paths"></a>

## Towards Robust Vision Transformers: Path Dependency Analysis and a Simple Two-Stage Adversarial Training

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Kim_Towards_Robust_Vision_Transformers_Path_Dependency_Analysis_and_a_Simple_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Kim_Towards_Robust_Vision_Transformers_Path_Dependency_Analysis_and_a_Simple_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 视觉 Transformer 的早期表征与后期鲁棒特征面临不同优化需求。
- **核心创新 / 方法** · 以遮挡内部梯度通路做防御诊断，并对不同训练阶段采用不同目标以缓解不稳定。
- **Baseline** · 正文表3–4与标准训练、常规鲁棒训练及各阶段组件变体比较。
- **Benchmark** · 在 CIFAR-10、ImageNette 上分别报告干净正确率与鲁棒正确率；另在 Pascal VOC 2012 评估语义分割迁移。
- **关键结果 / 消融** · 正文表3–4报告两阶段方案的精度与鲁棒性，并用组件消融定位收益。
- **适用条件 / 局限** · 结论依赖视觉 Transformer 与所测评估设定，不能自动外推到其他架构和威胁模型。

**可复用机制** · 防御训练中分别审计残差通路与变换通路，验证统一扰动训练是否损伤早期表征。

<a id="paper-ffgo"></a>

## First Frame Is the Place to Go for Video Content Customization

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_First_Frame_Is_the_Place_to_Go_for_Video_Content_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_First_Frame_Is_the_Place_to_Go_for_Video_Content_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 参考实体常靠专用适配或大量训练融入视频，难复用原图生视频能力。
- **核心创新 / 方法** · 利用首帧可承载后续复用的参考对象，用少量示例适配原视频模型。
- **Baseline** · Wan2.2-I2V-A14B 为基础；与原模型、SkyReels-A2、VACE 比较。
- **Benchmark** · 正文表1由40位用户给出200次标注，衡量整体质量、对象身份、场景身份和排名。
- **关键结果 / 消融** · 50个训练示例的 FFGo 获81.2%首选，VACE为11.1%；对象身份评分4.53对3.50。
- **适用条件 / 局限** · 证据为特定生成骨干和人评，复杂遮挡及大量参考对象需测身份保持。

**可复用机制** · 把视频模型首帧当作视觉实体记忆，可用少量示例训练模型复用其中实体。

<a id="paper-ehetm"></a>

## High-Quality and Efficient Turbulence Mitigation with Events

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_High-Quality_and_Efficient_Turbulence_Mitigation_with_Events_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_High-Quality_and_Efficient_Turbulence_Mitigation_with_Events_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 湍流复原依赖更多传统帧会拉长延迟，且边缘易受随机形变影响。
- **核心创新 / 方法** · 融合传统帧与高时间分辨率事件，利用湍流诱发事件的反向变化补充结构与运动线索。
- **Baseline** · 表1比较单帧及多帧复原方法，含 DATUM；表2分别消融事件处理和运动对齐。
- **Benchmark** · CTTH、LATH、UDET，报告 PSNR、SSIM、LPIPS、NIQE 和系统耗时。
- **关键结果 / 消融** · 正文相对 DATUM 报告 PSNR 提高0.38 dB，5帧加事件设置为29.5 FPS、160 ms。
- **适用条件 / 局限** · 依赖同步帧与事件观测、极性线索和设备标定；真实物体运动可能混入扰动估计。

**可复用机制** · 把事件极性交替当作边缘线索、事件方向用于去除扰动运动，在同等时延下比较帧序列重建。

<a id="paper-cadsketcher"></a>

## Bidirectional Query-Driven Generation of Parametric CAD Sketch

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_Bidirectional_Query-Driven_Generation_of_Parametric_CAD_Sketch_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_Bidirectional_Query-Driven_Generation_of_Parametric_CAD_Sketch_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 参数化 CAD 草图可从不完整、任意跨度的状态继续，单向序列模型容易忽略另一侧上下文。
- **核心创新 / 方法** · 双向查询生成前后候选，置信门选择扩展方向，以编译检查和渐进上下文更新保持可执行性。
- **Baseline** · 表 1 对比其他草图补全法，表 2 在 CAD as a Language 上做跨数据验证。
- **Benchmark** · 部分到完整补全与早期草图扩展，报告多级准确率、F1、无效比例和分布覆盖。
- **关键结果 / 消融** · 正文分别消融双向序列与位置编码；完整方案在表 1 的补全结果报告无效比例为 0。
- **适用条件 / 局限** · 可执行不等于符合设计意图；依赖已有 CAD 操作和约束语言。

**可复用机制** · 将草图续写改为缺口两侧的候选扩展，并用执行检查决定保留方向。

<a id="paper-illustrators-depth"></a>

## Illustrator's Depth: Monocular Layer Index Prediction for Image Decomposition

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Maruani_Illustrators_Depth_Monocular_Layer_Index_Prediction_for_Image_Decomposition_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Maruani_Illustrators_Depth_Monocular_Layer_Index_Prediction_for_Image_Decomposition_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 物理深度会把同一可编辑部件映成多个距离，无法直接给一致的图层遮挡顺序。
- **核心创新 / 方法** · 用分层矢量图监督像素的全局一致离散图层索引，并将索引用到矢量化。
- **Baseline** · 对照 Depth Pro、Depth Anything v2 和 Vtracer、LIVE、StarVector 等矢量化方法。
- **Benchmark** · 在 MMSVG 比较层预测与渲染结果，并在下游矢量化中测试效果；表 2 消融数据清理、深度先验和视差空间。
- **关键结果 / 消融** · 正文显示物理深度模型在层次排序上表现较弱，专门训练的层预测改善矢量化。
- **适用条件 / 局限** · 插画层标签依创作者的可编辑目的，同一图可有多个合理分层，照片表示需另验。

**可复用机制** · 编辑任务使用离散图层次序而不是物理深度，用可编辑渲染检验分解。

<a id="paper-tg-reg"></a>

## On the Role of Temporal Granularity in the Robustness of Spiking Neural Networks

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_On_the_Role_of_Temporal_Granularity_in_the_Robustness_of_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_On_the_Role_of_Temporal_Granularity_in_the_Robustness_of_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 按总序列聚合鲁棒性会掩盖少数高敏感时间步。
- **核心创新 / 方法** · 用逐步 Temporal Sensitivity Value 估计鲁棒性，并以 TG-Reg 约束整条时间轴的敏感度。
- **Baseline** · 与基线训练及其他鲁棒训练对照，表 1 比较不同时间约束。
- **Benchmark** · 含 CIFAR100 上 VGG11、8 时间步配置，分报正常性能及防护评测。
- **关键结果 / 消融** · 正文报告逐步正则能改善整体鲁棒性，验证不限于训练直接观察的条件。
- **适用条件 / 局限** · 只能在既定架构、时间分辨率和防护测评设定中解释敏感度。

**可复用机制** · 按时间步监测脉冲网络敏感度并正则不稳定步，同时保留干净准确率验收。

<a id="paper-srgcd"></a>

## SRGCD: Stability-Driven Region Growth Framework for 3D Change Detection

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_SRGCD_Stability-Driven_Region_Growth_Framework_for_3D_Change_Detection_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wu_SRGCD_Stability-Driven_Region_Growth_Framework_for_3D_Change_Detection_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 逐点分类易让变化区内部留空、边沿模糊，扫描噪声和类不平衡会放大问题。
- **核心创新 / 方法** · 用几何一致性筛高置信种子，逐步扩展稳定区域并优化点特征。
- **Baseline** · 比较传统、CNN 和 Transformer 方法；表 3 消融种子及传播设计。
- **Benchmark** · Urb3DCD-V1 与实景 HKCD，用 mIoU、mAcc 核对变化。
- **关键结果 / 消融** · 表 1 的 SRGCD 报告 94.11 mIoU、96.95 mAcc；表 2 对实景也有独立比较。
- **适用条件 / 局限** · 小而孤立变化及无可靠种子的区域可能无法充分扩展，边界应另测。

**可复用机制** · 变化检测从可信种子生长连通区域，再显式约束边界。

<a id="paper-mocodiff"></a>

## MoCoDiff: A Controllable Autoregressive Diffusion Model for Expressive Motion Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Song_MoCoDiff_A_Controllable_Autoregressive_Diffusion_Model_for_Expressive_Motion_Generation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Song_MoCoDiff_A_Controllable_Autoregressive_Diffusion_Model_for_Expressive_Motion_Generation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 多条件共用通道会互相干扰，长段自回归还会累积漂移。
- **核心创新 / 方法** · 用独立线性注入模块处理每类条件，用时序模块在不同去噪阶段引入历史。
- **Baseline** · 比较已有文本／风格动作生成，另比较逐帧和较短上下文方式。
- **Benchmark** · 表 1–2 测内容保留、风格保真、转场和生成效率。
- **关键结果 / 消融** · 正文报告冻结骨干基础上的多路控制能兼顾长时转场平滑及风格，不必针对每种组合重训。
- **适用条件 / 局限** · 需基础模型覆盖各条件；分支独立不等于输出因素在新动作中完全解耦。

**可复用机制** · 冻结动作生成骨干时分开注入文本、风格及历史，对历史采用时步相关校正。

<a id="paper-sharp"></a>

## SHARP: Short-Window Streaming for Accurate and Robust Prediction in Motion Forecasting

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Prutsch_SHARP_Short-Window_Streaming_for_Accurate_and_Robust_Prediction_in_Motion_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Prutsch_SHARP_Short-Window_Streaming_for_Accurate_and_Robust_Prediction_in_Motion_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 代理进入视野时间不同，用固定观察长度训练会使短历史与长历史的预测品质不一致。
- **核心创新 / 方法** · 实例级保存和递增更新隐状态，通过双目标让不同已观测窗口长度都能预测。
- **Baseline** · 与其他流式轨迹方法在默认配置比较，表 2 不用模型集成。
- **Benchmark** · Argoverse 2 多代理，nuScenes 和 Argoverse 1 单代理；按历史及预测时刻报告 minADE、minFDE、漏检、Brier 与时延。
- **关键结果 / 消融** · 表 1 在多组上下文长度下测量，表 2 提供多代理无集成结果；论文报告对短历史的稳健性和低时延。
- **适用条件 / 局限** · 依赖主体关联稳定，身份错配或突然出现的新主体仍要专项验收。

**可复用机制** · 流式轨迹预测按主体更新记忆，并联合训练不同历史长度。

<a id="paper-dual-e"></a>

## Dual-Estimator: Decoupling Global and Local Semantic Shift for Drift Compensation in Class-Incremental Learning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_Dual-Estimator_Decoupling_Global_and_Local_Semantic_Shift_for_Drift_Compensation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_Dual-Estimator_Decoupling_Global_and_Local_Semantic_Shift_for_Drift_Compensation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 以均匀方向校正旧类表征会忽略低频类及类间漂移程度的差异。
- **核心创新 / 方法** · 局部专家建模任务内漂移，再以类级全局投影选择校正尺度。
- **Baseline** · 比较既有 exemplar-free 增量算法，并将模块接入现有方法，对照其他漂移补偿。
- **Benchmark** · CIFAR-100、TinyImageNet 和 ImageNet-Subset 的 10/20 任务划分及细粒度数据，测平均和结束准确率。
- **关键结果 / 消融** · 表 1 和表 4 分别比较独立方法与可插入性，不同类上的涨幅允许独立检查。
- **适用条件 / 局限** · 输入流如果缺代表性旧语义，局部估计可能不可靠；还需保持同一任务划分。

**可复用机制** · 无回放增量学习把局部语义漂移和类级全局变化分开校正。

<a id="paper-sam-3d-body"></a>

## SAM 3D Body: Robust Full-Body Human Mesh Recovery

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_SAM_3D_Body_Robust_Full-Body_Human_Mesh_Recovery_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yang_SAM_3D_Body_Robust_Full-Body_Human_Mesh_Recovery_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 单图人体网格容易在罕见姿势、遮挡及手脚细节上失效。
- **核心创新 / 方法** · 使用 Momentum Human Rig 将骨架和表面参数分离，在编码解码器中接入可选掩码及关键点提示。
- **Baseline** · 表 2 比较已有 HMR，标明公开权重及是否训练用 RICH。
- **Benchmark** · 五套人体网格数据，对姿态和表面使用关节与网格误差评估。
- **关键结果 / 消融** · 表 2 比较两种骨干配置，正文展示提示可用于难见人体局部重估。
- **适用条件 / 局限** · 整体系统含多阶段标注，需单独控制标注、骨干和提示，才能确认具体表示的增量。

**可复用机制** · 人体网格模型用骨骼与表面解耦的身体表示，并把二维提示用于难例修正。

<a id="paper-qica"></a>

## Boosting Quantitive and Spatial Awareness for Zero-Shot Object Counting

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Boosting_Quantitive_and_Spatial_Awareness_for_Zero-Shot_Object_Counting_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Boosting_Quantitive_and_Spatial_Awareness_for_Zero-Shot_Object_Counting_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 按类别特化训练计数解码器会抹掉预训练的开放词汇能力，局部密度和总量也可能冲突。
- **核心创新 / 方法** · 在图文相似度上做空间代价聚合，并用多级数量一致损失约束全管线。
- **Baseline** · FSC-147 对比零样本方法和带样例方法，区分是否微调、所用骨干。
- **Benchmark** · FSC-147、CARPK、ShanghaiTech-A，以 MAE/RMSE 衡量；后两项用于跨域。
- **关键结果 / 消融** · 表 1 的 ViT-L/14 在 FSC-147 测试为 12.41 MAE、97.28 RMSE；CARPK 无微调达到 6.07 MAE。
- **适用条件 / 局限** · 图文相似度未必能分开密集且极小物体，跨类评价需核目标词描述。

**可复用机制** · 开放词汇计数直接处理图文相似度图，并让不同读出层的总量一致。

<a id="paper-guardtrace-vl"></a>

## GuardTrace-VL: Detecting Unsafe Multimodel Reasoning via Iterative Safety Supervision

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xiang_GuardTrace-VL_Detecting_Unsafe_Multimodel_Reasoning_via_Iterative_Safety_Supervision_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xiang_GuardTrace-VL_Detecting_Unsafe_Multimodel_Reasoning_via_Iterative_Safety_Supervision_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 模型最终回复合规时，中间的解释仍可能含有需要审核的内容；文字转述可能丢掉视觉语境。
- **核心创新 / 方法** · 让独立审核模型读取原图以及问题、推理、答案三部分，监督微调后迭代优化审核偏好。
- **Baseline** · 以 Qwen2.5-VL-3B-Instruct 为基座，与只做 SFT、标准 DPO、完整偏好训练和 ReasoningShield-3B 对比。
- **Benchmark** · GuardTrace-Test 的 S-Eval-VL、HADES-Eval、MM-Eval 和 MMJ-Eval 子集；表 2 报告 F1。
- **关键结果 / 消融** · S-Eval-VL 上基座 F1 为 43.61%，SFT 为 89.89%，完整训练为 93.33%。最大增益出现在监督训练后。
- **适用条件 / 局限** · 依赖系统可依法取得推理记录并提供可信风险标签；数据集 F1 不能单独推导实际部署的误报率或风险覆盖。

**可复用机制** · 多模态审核可分别检查推理过程与最终回答，并对照仅提供图片描述的文本审核器。见表 1–2。

<a id="paper-span-staged-geometric-alignment"></a>

## SPAN: Spatial-Projection Alignment for Monocular 3D Object Detection

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_SPAN_Spatial-Projection_Alignment_for_Monocular_3D_Object_Detection_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_SPAN_Spatial-Projection_Alignment_for_Monocular_3D_Object_Detection_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 分别估计中心、深度、尺寸和朝向会导致预测三维框投影互不一致；过早强制整体几何也会干扰学习。
- **核心创新 / 方法** · 对预测三维角点及三维框投影与二维框加联合约束，利用分层训练延后引入这些几何项。
- **Baseline** · 以 MonoDGP 为消融基线，另接入 MonoDETR、MoVis；比较各自单用角点或投影约束和分层训练。
- **Benchmark** · KITTI 验证及测试划分，按难度分层报告 R40 的三维 AP 与 BEV AP；Waymo 见附录。
- **关键结果 / 消融** · 表 4 难例三维 AP 从 19.02 提高到 20.17；单独直接加入角点或投影约束时为 18.82 或 18.97，均低于基线。
- **适用条件 / 局限** · 依赖准确内参和二维位置监督，直接投影约束在标签偏差或强遮挡时需重新校准权重与启用阶段。

**可复用机制** · 对解耦回归头加整体几何损失时，应在低阶属性学稳后逐步启用，并对比一开始就启用的方案。见 §3.4、表 3–4。

<a id="paper-modality-gap-robustness"></a>

## Is the Modality Gap a Bug or a Feature? A Robustness Perspective

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Chowers_Is_the_Modality_Gap_a_Bug_or_a_Feature_A_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Chowers_Is_the_Modality_Gap_a_Bug_or_a_Feature_A_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 图文对比表征形成分离的模态簇，单看干净准确率很难判断这种分离是否有用。
- **核心创新 / 方法** · 理论在模态均值差近似正交等条件下分离间隔与判别几何；推理时沿均值差平移一模态并比较不同幅度。
- **Baseline** · 对比保持原间隔、扩大间隔和缩小间隔，在多套公开对比 VLM 上不重新训练。
- **Benchmark** · 在多模型零样本分类、多选视觉问答中分别测干净准确率与高斯嵌入扰动下的最近邻决策一致率，并评估低比特量化与措辞改变。
- **关键结果 / 消融** · 图 8 中已测条件表现为缩小间隔使噪声下决策更稳定，而干净准确率基本保持；图 9 的量化验证方向一致。
- **适用条件 / 局限** · 正交假设仅近似成立，需用代表性批次估计均值。噪声一致性不能直接外推到真实域变化或任意对抗扰动。

**可复用机制** · 视觉语言模型做低精度部署前，可用零样本基线检验沿模态均值方向缩小间隔是否保留干净准确率并改善扰动稳定性。见定理 3.4–3.5、图 8–9。

<a id="paper-fairfal-local-global-querying"></a>

## Federated Active Learning Under Extreme Non-IID and Global Class Imbalance

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zong_Federated_Active_Learning_Under_Extreme_Non-IID_and_Global_Class_Imbalance_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zong_Federated_Active_Learning_Under_Extreme_Non-IID_and_Global_Class_Imbalance_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 联邦模型面对全局类别长尾和客户端数据分布不同，两类偏斜共同改变不确定性采样的覆盖。
- **核心创新 / 方法** · 按两类偏斜选择询标模型，并用原型引导的类平衡采样及不确定性和多样性两段筛选。
- **Baseline** · 分别比较本地与全局询标、随机、KAFAL、LoGo、IFAL，并消融模型选择与类别平衡。
- **Benchmark** · FMNIST、CIFAR-10/100 上模拟不同程度非独立同分布与长尾；OctMNIST、DermaMNIST 检验自然类别不平衡，报告标注轮次准确率及学习曲线面积。
- **关键结果 / 消融** · 观察 1 报告本地不确定性通常更好，但全局严重长尾且客户端近同质时有反转。表 3 的 OctMNIST 末轮为 72.80%，KAFAL 为 70.40%。
- **适用条件 / 局限** · 需要能估计客户端差异和全局长尾；默认每轮有可用标注预算，少客户端及持续变化条件应另测。

**可复用机制** · 联邦主动学习先按全局长尾与客户端异质性分别测本地和全局询标器，避免固定选全局模型。见观察 1、表 1–3。

<a id="paper-lmee-memory-retrieval-training"></a>

## Explore with Long-term Memory: A Benchmark and Multimodal LLM-based Reinforcement Learning Framework for Embodied Exploration

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Explore_with_Long-term_Memory_A_Benchmark_and_Multimodal_LLM-based_Reinforcement_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_Explore_with_Long-term_Memory_A_Benchmark_and_Multimodal_LLM-based_Reinforcement_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 导航成功率不能区分代理是否保存并在后续使用探索中得到的证据。
- **核心创新 / 方法** · 将多目标导航与途中情景记忆问答联合设置，使用检索工具并对不同类型问答做强化微调。
- **Baseline** · 比较 RA-Mem 与在不同训练问答类型上的强化微调。
- **Benchmark** · LMEE-Bench 报告导航成功率、路径长度加权成功率和问答分；GOAT-Bench 报告两项导航指标。
- **关键结果 / 消融** · 表 4 中 GOAT-Bench 成功率从基线 42.81% 到全部问答 48.20%；LMEE 的单独多选训练成功率 23.53%，高于全部训练的 22.06%。
- **适用条件 / 局限** · 依赖环境允许记录和检索信息，问答分可能受评判模型影响；不能从模拟探索直接推断长时实物部署可靠性。

**可复用机制** · 长程探索应分别训练和测量记忆检索与导航，使用不同问答监督检查哪类记忆任务真正提升行动。见表 4。

<a id="paper-intervention-stable-modal-fusion"></a>

## Multi-Modal Image Fusion via Intervention-Stable Feature Learning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Multi-Modal_Image_Fusion_via_Intervention-Stable_Feature_Learning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_Multi-Modal_Image_Fusion_via_Intervention-Stable_Feature_Learning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 多个传感器在训练数据中经常同时有效，相关性驱动的融合难以判断究竟哪一模态可补足缺失。
- **核心创新 / 方法** · 用互补区域掩蔽、同区域掩蔽、整模态丢弃产生不同视图；通过干预稳定性与模态必要性约束训练融合门控。
- **Baseline** · 比较去掉特征整合、稳定损失、必要性损失、所有干预的不同方案，以及其他红外与可见图像融合方法。
- **Benchmark** · 在三个红外可见融合基准比较空间细节、PSNR、相关性等指标，另测试检测及分割迁移。
- **关键结果 / 消融** · 表 2 完整模型平均梯度 6.136，去必要性项为 4.016；完整 PSNR 为 63.62，去全部干预反而为 63.95，显示质量指标取舍。
- **适用条件 / 局限** · 合成掩蔽依赖双传感器空间对齐，需确保遮挡和故障模型代表真实失效；实验未证明学习到真实因果关系。

**可复用机制** · 多模态融合训练应分别测试互补、共同缺失与整模态缺失，用独立约束衡量稳定性及模态必要性。见 §3、表 2。

<a id="paper-dark3r"></a>

## Dark3R: Learning Structure from Motion in the Dark

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Guo_Dark3R_Learning_Structure_from_Motion_in_the_Dark_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Guo_Dark3R_Learning_Structure_from_Motion_in_the_Dark_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 极低光下特征匹配和位姿估计易退化，直接沿用正常曝光的模型会失配。
- **核心创新 / 方法** · 以干净曝光作为教师输入，使用实拍或噪声合成的配对 RAW 监督暗光学生，不用三维标签训练。
- **Baseline** · 正文表1比较传统与学习式几何模型，表2用 Dark3R 或 MASt3R-SfM 的位姿做视图合成。
- **Benchmark** · 表1低光测试场景平均信噪比为−3.87 dB，按120图或330至500图对齐参考位姿后测误差。
- **关键结果 / 消融** · 正文报告低信噪比下匹配及位姿更准确；扩展到全序列并更多依赖光束平差后，平均位姿精度略有下降。
- **适用条件 / 局限** · 依赖对齐噪声与干净视图、RAW 数据及合理噪声统计。位姿参考来自长曝光 COLMAP。

**可复用机制** · 用配对曝光训练低信噪比几何模型，在没有三维训练标签时迁移干净图像的匹配信号。

<a id="paper-single-image-patch-diffusion"></a>

## Efficient and Training-Free Single-Image Diffusion Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Qiu_Efficient_and_Training-Free_Single-Image_Diffusion_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Qiu_Efficient_and_Training-Free_Single-Image_Diffusion_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 每张参考图训练一个扩散网络代价很高，训练式模型也可能只产生接近原图的样本。
- **核心创新 / 方法** · 把多尺度图块视为有限的低维样本集，从闭式去噪估计构造扩散采样。
- **Baseline** · 表1比较训练式单图生成器和图块方法，包括 SinGAN、GPNN、GPDM。
- **Benchmark** · 表1用 SIFID、感知质量、LPIPS 多样性和运行时间；表2按图像分辨率测试耗时。
- **关键结果 / 消融** · 正文报告无需逐图训练，一组近邻近似设置只损失0.09 SIFID，并指出 GPNN 和 GPDM 的 SIFID 优势可能伴随近重复。
- **适用条件 / 局限** · 局部图块先验适合可重复纹理，全局物体和跨区域关系仍需验证。去噪开销依赖图块维数与邻居搜索。

**可复用机制** · 单图生成可用多尺度图块经验分布构造闭式去噪器，替换逐图训练。

<a id="paper-osa"></a>

## OSA: Echocardiography Video Segmentation via Orthogonalized State Update and Anatomical Prior-aware Feature Enhancement

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_OSA_Echocardiography_Video_Segmentation_via_Orthogonalized_State_Update_and_Anatomical_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_OSA_Echocardiography_Video_Segmentation_via_Orthogonalized_State_Update_and_Anatomical_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 超声噪声与器官运动容易让无约束循环状态的奇异值衰减，细节逐步丢失。
- **核心创新 / 方法** · 对记忆更新做 Stiefel 流形约束，辅以基于解剖结构的特征增强。
- **Baseline** · 对照现有超声分割方法及正文的状态更新、特征增强组件。
- **Benchmark** · CAMUS 与 EchoNet-Dynamic，表1报告 mDice、mHD95 和射血分数估计指标。
- **关键结果 / 消融** · 正文展示约束改善状态演化并提高所测分割表现，分别比较结构特征增强。
- **适用条件 / 局限** · 需验证强正交约束是否限制不同状态动力。解剖增强及当前结果针对左心室超声。

**可复用机制** · 监控线性循环记忆秩，并考虑以正交状态更新抵消长序列衰减。

<a id="paper-compression-phase-detection"></a>

## Detecting Compressed AI-Generated Images via Phase Spectrum Robustness

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Detecting_Compressed_AI-Generated_Images_via_Phase_Spectrum_Robustness_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Detecting_Compressed_AI-Generated_Images_via_Phase_Spectrum_Robustness_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 压缩会破坏脆弱检测线索并引入混杂伪影，使原图检测分数不能代表部署性能。
- **核心创新 / 方法** · 把相位信号和视觉表征结合做稳健检测，在没有配对压缩图和标签时训练，并另验有限标签设置。
- **Baseline** · 对既有检测器做质量已知和质量未知两组对照，再消融相位及适配组件。
- **Benchmark** · 正文表1–4分别按 GAN 与扩散生成器以及压缩质量可见程度报告检测表现。
- **关键结果 / 消融** · 正文报告在两类生成器上改善压缩后检测，并用表5消融质量已知设置中的组件。
- **适用条件 / 局限** · 频谱在其他图像处理和新生成分布下未必保持，需要对实际平台压缩及误报率重新验收。

**可复用机制** · 防御性合成图检测可将不同图像质量分层验收，并测阶段频谱线索是否保持。

<a id="paper-tunable-soft-equivariance"></a>

## Tunable Soft Equivariance with Guarantees

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Rahman_Tunable_Soft_Equivariance_with_Guarantees_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Rahman_Tunable_Soft_Equivariance_with_Guarantees_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 强制严格对称会改变已有主干的预测，现实数据的变换条件通常只近似成立。
- **核心创新 / 方法** · 将预训练权重投影到设计的子空间，调节软等变程度，并给出等变误差界。
- **Baseline** · 与未调整主干和 canonicalization 对照，包含 ViT、DINOv2、ResNet-50。
- **Benchmark** · 正文表1–4覆盖 CIFAR、ImageNet、PASCAL VOC，报告准确率、增广精度、不变误差和 mIoU。
- **关键结果 / 消融** · 表2的 ImageNet ViT 原输入准确率81.67%变82.28%，不变误差按表中尺度由0.36降至0.15；canonicalization 的准确率为76.51%。
- **适用条件 / 局限** · 约束依赖选定变换与权重子空间；先验对称不适用时需同时复验原分布精度。

**可复用机制** · 用可调权重投影平衡对称误差与原始任务性能，避免在数据近似对称时硬性约束。

<a id="paper-generalized-cvo"></a>

## Generalized-CVO: Fast and Correspondence-Free Local Point Cloud Registration with Second Order Riemannian Optimization

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Generalized-CVO_Fast_and_Correspondence-Free_Local_Point_Cloud_Registration_with_Second_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Generalized-CVO_Fast_and_Correspondence-Free_Local_Point_Cloud_Registration_with_Second_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 显式匹配和各向同性核在几何稀疏区域难以约束位姿，迭代次数也可能过高。
- **核心创新 / 方法** · 用编码局部表面几何的逐点各向异性核做无对应配准，以近似黎曼 Hessian 加速求解。
- **Baseline** · 对照一阶 G-CVO、各向同性 CVO 二阶变体、Fast-VGICP、GICP 和 ICP。
- **Benchmark** · 表1–4覆盖 KITTI、特征稀疏序列、ETH3D RGB-D 与 ModelNet40，用位姿误差和配准指标评价。
- **关键结果 / 消融** · 表2 Dirt Track 平移误差从一阶20.8969降至二阶6.0791，Skid Pad 上 Fast-VGICP 的1.8999优于二阶方案的2.5076。
- **适用条件 / 局限** · 这是局部注册，需要可用初值和稳定法向；强错位下需另验全局初始化。

**可复用机制** · 将点云核的法向和切向灵敏度分开，并在相同目标下比较一阶与二阶流形求解。

<a id="paper-multianimate"></a>

## MultiAnimate: Pose-Guided Image Animation Made Extensible

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Hu_MultiAnimate_Pose-Guided_Image_Animation_Made_Extensible_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Hu_MultiAnimate_Pose-Guided_Image_Animation_Made_Extensible_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 单人扩散动画直接复制到多人会混身份和遮挡。
- **核心创新 / 方法** · 以人物掩码和标识适配器为每个姿态提供归属，并保留人物空间关系。
- **Baseline** · 表 1 比较 MimicMotion 等动画方法，表 2 比较单人系统。
- **Benchmark** · Swing Dance、合成及未见舞蹈，另用 TikTok 单人集，报告 PSNR、LPIPS、FVD。
- **关键结果 / 消融** · 正文报告双人训练可外推多人物，TikTok 单人表现仍可比。
- **适用条件 / 局限** · 依赖可靠姿态和掩码，密集交互的遮挡需另测。

**可复用机制** · 为每个角色分配显式标识和遮挡位置，用少角色训练外推多角色。

<a id="paper-gui-hallubench"></a>

## Exposing and Evaluating Hallucinations for GUI Grounding

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Exposing_and_Evaluating_Hallucinations_for_GUI_Grounding_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Exposing_and_Evaluating_Hallucinations_for_GUI_Grounding_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 只看任务成功会混淆结构误读、错误选择和无依据输出。
- **核心创新 / 方法** · 构造结构解析和幻觉子集，分别用解析提示与感知幻觉微调缓解。
- **Baseline** · 表 2 比较原有多模态模型及两种缓解方案。
- **Benchmark** · GUI-HalluBench 按布局解析和含干扰或不存在目标的定位设置计分。
- **关键结果 / 消融** · 正文将解析弱点关联到两类幻觉，并报告提示及微调降低部分错误。
- **适用条件 / 局限** · 依赖目标缺失标注和控件语义，不直接等于闭环任务可靠性。

**可复用机制** · GUI 定位区分点错现有控件和凭空定位不存在控件。

<a id="paper-dynamic-expert-restoration"></a>

## Beyond Sequential Tools: A Unified VLM Agent System for Photographic Post-Processing via Dynamic Multi-Expert Fusion

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xiong_Beyond_Sequential_Tools_A_Unified_VLM_Agent_System_for_Photographic_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xiong_Beyond_Sequential_Tools_A_Unified_VLM_Agent_System_for_Photographic_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 串行修复有累积误差，普适模型又可能无法覆盖新组合。
- **核心创新 / 方法** · VLM 判断退化后给专门 LoRA 分配权重，只改注意力 K/V 并合入扩散骨干。
- **Baseline** · 对照串行工具调用及 Real-1000 中其他恢复模型。
- **Benchmark** · Real-1000 按单、双、三种退化分组，另验证自然退化。
- **关键结果 / 消融** · 正文报告对复合和真实退化有效，表 1 按复杂程度独立比较。
- **适用条件 / 局限** · 取决于专家是否互补及路由能否识别分布外退化。

**可复用机制** · 对复合退化一次融合专家，用独立 K/V 适配替代逐个工具执行。

<a id="paper-reattnclip"></a>

## ReAttnCLIP: Training-Free Open-Vocabulary Remote Sensing Image Segmentation via Re-defined Attention in CLIP

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Niu_ReAttnCLIP_Training-Free_Open-Vocabulary_Remote_Sensing_Image_Segmentation_via_Re-defined_Attention_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Niu_ReAttnCLIP_Training-Free_Open-Vocabulary_Remote_Sensing_Image_Segmentation_via_Re-defined_Attention_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 末层全局图文对齐会削弱遥感分割需要的 patch 结构。
- **核心创新 / 方法** · patch 间用中层特征相似度，类对 patch 用中层注意，并去 CLS 自注意项。
- **Baseline** · 对照原 CLIP 和已有免训练开放词汇分割。
- **Benchmark** · 表 1 覆盖 OpenEarthMap、LoveDA 等八套遥感数据，以 mIoU 计。
- **关键结果 / 消融** · 正文报告八套语义分割均改善，并另查路网和建筑。
- **适用条件 / 局限** · 层选择和局部相似度受成像尺度影响，跨自然图像需再验。

**可复用机制** · 冻结 CLIP 时按局部关系与类定位分别替换注意力来源。

<a id="paper-libero-plus"></a>

## LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Fei_LIBERO-Plus_A_Progressive_Robustness_Benchmark_for_Visual-Language-Action_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Fei_LIBERO-Plus_A_Progressive_Robustness_Benchmark_for_Visual-Language-Action_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 干净模拟任务接近饱和仍可能掩盖对相机和布局的依赖。
- **核心创新 / 方法** · 自动控制七个扰动轴，包括相机、语言、照明、布局和传感噪声。
- **Baseline** · 表 2 对照十种 VLA 在干净任务和不同扰动轴的表现。
- **Benchmark** · LIBERO-Plus 仿真，逐轴及组合测任务成功率。
- **关键结果 / 消融** · 报告部分设置中模型从约 95% 下降到低于 30%，各轴的下降不同。
- **适用条件 / 局限** · 模拟扰动不是实际真机失效保证，轴与强度需匹配部署。

**可复用机制** · 操作策略上线评测加入可复现单轴扰动，测正常与扰动成功率差。

<a id="paper-anylift"></a>

## AnyLift: Scaling Motion Reconstruction from Internet Videos via 2D Diffusion

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_AnyLift_Scaling_Motion_Reconstruction_from_Internet_Videos_via_2D_Diffusion_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_AnyLift_Scaling_Motion_Reconstruction_from_Internet_Videos_via_2D_Diffusion_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 动态相机和少见动作让单目人体及人–物重建难保持一致。
- **核心创新 / 方法** · 将网络视频二维关键点用于构造域内多视二维训练数据，再以多视相机条件去噪。
- **Baseline** · 与现有人体重建和人–物重建方法比较。
- **Benchmark** · AIST++ 在动、静相机分别测试三维关节及全局轨迹，并评网络视频。
- **关键结果 / 消融** · 表 1 的动态相机结果提供根运动改进，表 2 报网络视频多指标改善。
- **适用条件 / 局限** · 依关键点和相机估计，互联网结果可能缺精确真值。

**可复用机制** · 难动作缺三维数据时先扩增多视二维轨迹，再用相机条件扩散提升到世界坐标。

<a id="paper-hybridiff"></a>

## Accelerating Diffusion via Hybrid Data-Pipeline Parallelism Based on Conditional Guidance Scheduling

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Jung_Accelerating_Diffusion_via_Hybrid_Data-Pipeline_Parallelism_Based_on_Conditional_Guidance_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Jung_Accelerating_Diffusion_via_Hybrid_Data-Pipeline_Parallelism_Based_on_Conditional_Guidance_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 扩散各步与设备通信同时制约吞吐，恒定并行方案可能失真。
- **核心创新 / 方法** · 用导引双路径做数据分区，依两路径差异决定是否流水化。
- **Baseline** · 表 2 对比单卡、仅条件分区及混合并行。
- **Benchmark** · SDXL、SD3 在 RTX 3090 的 1/2/4 卡及不同分辨率，测生成时延与质量。
- **关键结果 / 消融** · 双卡报告 SDXL 2.31 倍、SD3 2.07 倍加速，SDXL 仅分区 1.78 倍。
- **适用条件 / 局限** · 收益受互联及导引机制影响，不可仅用多卡加速比替代功耗和成本。

**可复用机制** · 将有条件和无条件导引先映射到两设备，再按去噪差异切换流水调度。

<a id="paper-universe"></a>

## UniVerse: Empower Unified Generation with Reasoning and Knowledge

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Sun_UniVerse_Empower_Unified_Generation_with_Reasoning_and_Knowledge_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Sun_UniVerse_Empower_Unified_Generation_with_Reasoning_and_Knowledge_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 直接图像监督无法说明模型为何这么理解隐含条件。
- **核心创新 / 方法** · 用隐式提示、推理步骤、明确提示、图像组成样本微调 Bagel。
- **Baseline** · 表 1 比较原 Bagel、无推理链注入和带链注入。
- **Benchmark** · 约 12 万图文样本，在推理及知识类生成基准区分是否开启生成前思考。
- **关键结果 / 消融** · 正文报告带链版本在多个设定优于原模型，并显式比较只提供提示的版本。
- **适用条件 / 局限** · 需单验推理链正确性和训练语料覆盖，开放新知识的外推证据有限。

**可复用机制** · 把隐含请求转成明确视觉描述作为中间监督，比较需要和不需要推理链的配方。

<a id="paper-inside-out-vit-generalization"></a>

## Inside-Out: Measuring Generalization in Vision Transformers Through Inner Workings

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Peng_Inside-Out_Measuring_Generalization_in_Vision_Transformers_Through_Inner_Workings_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Peng_Inside-Out_Measuring_Generalization_in_Vision_Transformers_Through_Inner_Workings_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 不掌握目标标签时，源域准确率或输出置信度可能不能正确排序候选模型。
- **核心创新 / 方法** · 从视觉 Transformer 的依赖电路构造深度偏置代理用于部署前选模；部署后用电路变化量监控分布偏移。
- **Baseline** · 比较源域准确率、平均置信度、熵、ATC、RANKME 等，另比较不同电路指标。
- **Benchmark** · PACS 风格偏移、Camelyon17 机构偏移和 Terra Incognita 地域偏移；报告 R²、Spearman、Kendall 与真实目标准确率的关系。
- **关键结果 / 消融** · 表 1 中 DDBout 的九项平均分为 0.766，源域准确率代理为 0.632；但 Camelyon17 的 Spearman 项仍需和输出代理逐项对照。
- **适用条件 / 局限** · 要能访问中间表征且承担发现电路的开销；代理相关性不能给出单模型在新域的误差保证。

**可复用机制** · 目标域无标签时，比较内部依赖结构与置信度作为选模代理，并将部署后漂移单独校准。见表 1、3。

<a id="paper-c3r-variable-sensor-channels"></a>

## Building Robust Vision Encoders for Cross-Dataset Evaluation in Immunofluorescent Microscopy

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Marikkar_Building_Robust_Vision_Encoders_for_Cross-Dataset_Evaluation_in_Immunofluorescent_Microscopy_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Marikkar_Building_Robust_Vision_Encoders_for_Cross-Dataset_Evaluation_in_Immunofluorescent_Microscopy_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 多通道视觉数据因设备和成像协议而异，单一固定通道配置训练的编码器可能无法直接接收新配置。
- **核心创新 / 方法** · 将通道区分为参考上下文和变化观测，使用可变通道编码器及基于此划分的掩蔽知识蒸馏。
- **Baseline** · 比较固定通道 ViT、ChannelViT、DiChaViT 及针对目标通道重训的 Base-CP。
- **Benchmark** · HPA-Loc、JUMP-Ret 和 CHAMMI-FE，区分通道组合内外的评测；报告分类和检索指标，包括 mAP 与 kNN。
- **关键结果 / 消融** · 表 2 的 ViT-S 在 JUMP-Ret 上 mAP 为 0.354，接近按目标通道重训的 0.355，kNN 为 0.518 对 0.507。
- **适用条件 / 局限** · 依赖目标数据仍有可识别的共享参考通道；无参考或参考本身漂移的传感器环境需要另测。正文验证来自细胞影像。

**可复用机制** · 针对设备通道配置不统一的视觉编码，可区分稳定参考与变化观测，训练时做掩蔽蒸馏，并用从未见过的通道组合验收。见表 1–3。

<a id="paper-gated-kalmanet"></a>

## Gated KalmaNet: A Fading Memory Layer through Test-time Ridge Regression

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Peng_Gated_KalmaNet_A_Fading_Memory_Layer_through_Test-time_Ridge_Regression_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Peng_Gated_KalmaNet_A_Fading_Memory_Layer_through_Test-time_Ridge_Regression_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 线性状态层内存不随序列增长，但历史压缩使召回变弱，直接使用 Kalman 更新又容易在低精度下数值不稳。
- **核心创新 / 方法** · 以在线岭回归更新记忆，对正则做输入门控以兼顾条件数和保留历史，用分块 Chebyshev 迭代替代直接求解。
- **Baseline** · 对照 Transformer、GLA、DeltaNet、Mamba2 和 Gated DeltaNet，长上下文使用固定比较协议。
- **Benchmark** · 短上下文评估 2.8B 模型十项任务；长上下文用 HELMET 的 RAG/多样例学习和 RULER 的问答/合成召回，最长 128K。
- **关键结果 / 消融** · 表 2 短任务平均为 58.89，Gated DeltaNet 57.00，Transformer 63.92。图 3 长问答与 RAG 提升较明显，合成召回过 4K 后并不占优。
- **适用条件 / 局限** · 依赖实现的分块和数值精度，理论常量状态不等于同等实际吞吐；长期记忆收益随语义结构和召回任务而变。

**可复用机制** · 低精度长序列状态层若用在线岭回归，应对条件数做输入相关正则，并把实际召回和合成任务测开。见表 2、图 3。

<a id="paper-vit-p-point-mask-classification"></a>

## The Missing Point in Vision Transformers for Universal Image Segmentation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Shahabodini_The_Missing_Point_in_Vision_Transformers_for_Universal_Image_Segmentation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Shahabodini_The_Missing_Point_in_Vision_Transformers_for_Universal_Image_Segmentation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 掩码位置和形状可较准确，而长尾或边界模糊区域仍易分类错。
- **核心创新 / 方法** · 分离类别无关掩码提议与分类，用预训练 ViT 的点级特征对候选掩码赋类别。
- **Baseline** · 对比不同代表点选择、DINOv2/ViT/MAE 骨干及粗、细标注训练。
- **Benchmark** · ADE20K、Cityscapes、COCO，对实例、语义和全景分割报告 AP、mIoU 和 PQ。
- **关键结果 / 消融** · 表 4 中随机选点的 mIoU 为 58.7，中心或响应最高点均为 59.7；Cityscapes 仅粗标注 PQ 为 70.0，精细标注为 69.8。
- **适用条件 / 局限** · 分类上限受候选掩码和取样点限制；相关实验不能推出粗标注普遍优于精标注。

**可复用机制** · 现有分割器的掩码几何已足够时，可用点级 ViT 对候选掩码再分类，并对照粗注释和精细掩码。见表 4。

<a id="paper-fcdm-convolutional-diffusion"></a>

## Reviving ConvNeXt for Efficient Convolutional Diffusion Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Kwon_Reviving_ConvNeXt_for_Efficient_Convolutional_Diffusion_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Kwon_Reviving_ConvNeXt_for_Efficient_Convolutional_Diffusion_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · Transformer 扩散的质量提升常伴随训练开销，现代全卷积骨干在同类生成设置中的效率需要实测。
- **核心创新 / 方法** · 用类似 ConvNeXt 的全卷积分层骨干结合扩散条件注入进行潜空间建模，比较不同容量和分辨率。
- **Baseline** · 比较 DiT-XL/2 及 DiCo，在类别条件生成 benchmark 汇总其他图像生成模型。
- **Benchmark** · ImageNet 256×256 和 512×512；报告 FID-50K、IS、精确率、召回、吞吐、训练步数和 FLOPs。
- **关键结果 / 消融** · 表 3 的 FCDM-XL 单次约 64.6 GFLOPs，约为 DiT-XL/2 一半；表 4 的 256 分辨率有引导 FID 为 2.03。
- **适用条件 / 局限** · 证据来自类别条件潜扩散和特定硬件，复杂文本条件、全球空间关系和视频时序任务需比较。

**可复用机制** · 做固定训练资源的图像扩散时，应把条件化 ConvNeXt 纳入骨干对照，分别看迭代数、单步 FLOPs 和吞吐。见表 2–4。

<a id="paper-detany4d-temporal-box-stability"></a>

## DetAny4D: Detect Anything 4D Temporally in a Streaming RGB Video

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Hou_DetAny4D_Detect_Anything_4D_Temporally_in_a_Streaming_RGB_Video_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Hou_DetAny4D_Detect_Anything_4D_Temporally_in_a_Streaming_RGB_Video_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 逐帧三维检测可以取得类似 AP，却在相邻帧输出位置、形状与朝向不稳定的框。
- **核心创新 / 方法** · 因果时空解码器处理 RGB 序列，用尺寸、角点、相机和深度、位姿等多头监督及跨帧约束。
- **Baseline** · 比较逐帧三维检测与分阶段 4D 模型，固定消融子集逐项添加时序和几何监督。
- **Benchmark** · DA4D 流式检测数据，报告 AP3D 和框稳定性指标；表 3 用完整训练集的 10% 做部件对照。
- **关键结果 / 消融** · 表 3 从基础因果注意力到完整方案，AP3D 从 26.78 到 27.29，两项方差由 0.95/1.01 降至 0.54/0.48。
- **适用条件 / 局限** · 训练需要能可靠生成连续三维标注，方差降低也可能掩盖真实快速运动，动态场景应另测响应延迟。

**可复用机制** · 流式三维检测的训练应以跨帧抖动单独验收几何辅助头，避免仅按每帧 AP 选择模型。见表 3。

<a id="paper-metacompress"></a>

## Rethinking Token Reduction for Large Vision-Language Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Rethinking_Token_Reduction_for_Large_Vision-Language_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_Rethinking_Token_Reduction_for_Large_Vision-Language_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 根据首问裁剪的词元可能缺少后续问题所需区域。
- **核心创新 / 方法** · MetaCompress 学习与提示独立的视觉压缩映射，统一裁剪和融合。
- **Baseline** · 完整输入、随机选择、FastV、PruMerge；消融各训练目标。
- **Benchmark** · 表1在 MT-VQA-v2、MT-GQA、ConvBench 按轮报告结果，另测效率。
- **关键结果 / 消融** · LLaVA-1.5-7B 移除90%词元时 MT-VQA-v2 平均70.65，FastV 48.06，完整输入77.18。
- **适用条件 / 局限** · 不能恢复被压掉的细节，需复测后续问题与首问无关时的准确率。

**可复用机制** · 跨轮视觉问答应在未知后续问题的情况下学习压缩，按轮检查信息丢失。

<a id="paper-captionqa"></a>

## CaptionQA: Is Your Caption as Useful as the Image Itself?

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_CaptionQA_Is_Your_Caption_as_Useful_as_the_Image_Itself_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yang_CaptionQA_Is_Your_Caption_as_Useful_as_the_Image_Itself_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 通用描述指标难检验描述是否保留后续任务所需细节。
- **核心创新 / 方法** · 构造需图像证据的多选题，将只读描述的问答表现与原图问答对照。
- **Baseline** · 比较所测 VLM 对原图和描述输入的同题表现，并分领域与任务类别。
- **Benchmark** · 自然场景、文档、电商、具身四域共33027题，表4比较分域绝对分差。
- **关键结果 / 消融** · 表4中 LLaVA-OV-7B 在具身问答上的图像与描述分差为41.81分，Qwen3-VL-30B-A3B 为16.96分。
- **适用条件 / 局限** · 指标受答题模型及题目组成影响。选型时应使用部署任务确实需要的视觉证据。

**可复用机制** · 同题分别用图像和描述作输入，用分域问答差值决定是否能把图像替换成文本。

<a id="paper-cw-dpo"></a>

## Dynamics-Aware Preference Optimization for Vision-Language Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Dynamics-Aware_Preference_Optimization_for_Vision-Language_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Dynamics-Aware_Preference_Optimization_for_Vision-Language_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 显然错误的负例仍可能产生大的错向梯度，损伤校准。
- **核心创新 / 方法** · 先用低权重负例做受限 SFT，再按模型逐词元概率调整 DPO 的负例梯度。
- **Baseline** · 与常规偏好对齐和 PPO 比较，表3分离预热和冷却加权。
- **Benchmark** · 表2覆盖 COCO、Flickr30k、NoCaps、MMMU、MMBench1.1，报告图像描述及问答指标。
- **关键结果 / 消融** · 正文报告相对 PPO 的 CIDEr 改善3.4，MMMU 绝对正确率增加2.4个百分点。
- **适用条件 / 局限** · 负例权重依赖模型置信和负例生成方式，需核查难负例是否被误抑制。

**可复用机制** · 偏好训练即使易负例损失很低，也应审计其梯度，通过能力相关权重减少无信息更新。

<a id="paper-flowdc"></a>

## FlowDC: Flow-Based Decoupling-Decay for Complex Image Editing

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Jiang_FlowDC_Flow-Based_Decoupling-Decay_for_Complex_Image_Editing_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Jiang_FlowDC_Flow-Based_Decoupling-Decay_for_Complex_Image_Editing_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 一次指令复杂时容易漏子目标，逐轮编辑又会积累图像偏移。
- **核心创新 / 方法** · 拆分不同子编辑的速度贡献并在采样中叠加，减弱相对编辑位移的正交速度。
- **Baseline** · 与 SDEdit、MultiTurn、RF-Inv 等比较，消融并行叠加和正交衰减。
- **Benchmark** · Complex-PIE-Bench 及 PIE-Bench++，表1–2测 CLIP-T、CLIP-I、DINO、LPIPS。
- **关键结果 / 消融** · 正文报告移除并行叠加降低 CLIP-T，正交衰减主要改善源图一致性。
- **适用条件 / 局限** · 互相冲突或空间重合的编辑目标未必可线性叠加。

**可复用机制** · 并行叠加多个编辑方向，并独立抑制造成源结构偏移的正交速度。

<a id="paper-pdcr"></a>

## PDCR: Perception-Decomposed Confidence Reward for Vision-Language Reasoning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yoon_PDCR_Perception-Decomposed_Confidence_Reward_for_Vision-Language_Reasoning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yoon_PDCR_Perception-Decomposed_Confidence_Reward_for_Vision-Language_Reasoning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 视觉步骤少于文本步骤，全局归一化会被文字步骤主导。
- **核心创新 / 方法** · 内部视觉依赖分数划分步骤，再在相同类别内归一答案置信增量。
- **Baseline** · 与 GRPO、DAPO、PACR 及随机分组做对照。
- **Benchmark** · 以 Qwen2.5-VL 3B、7B 在 MMMU、RealWorldQA、MathVerse、HallusionBench 等七项测准确率。
- **关键结果 / 消融** · 表1 7B 的七项平均为52.9，对照 GRPO 51.5。表2比较随机划分与按视觉依赖划分。
- **适用条件 / 局限** · 视觉依赖分数只是步骤功能代理，需检查感知与文本紧密交织的任务。

**可复用机制** · 用视觉依赖划分感知和文字推理，在各类内部标准化同一个信心增长奖励。

<a id="paper-mf-rae"></a>

## MeanFlow Transformers with Representation Autoencoders

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Hu_MeanFlow_Transformers_with_Representation_Autoencoders_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Hu_MeanFlow_Transformers_with_Representation_Autoencoders_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 在表示自编码器潜空间直接训练 MeanFlow 会发生梯度爆炸，传统 VAE 解码也较贵。
- **核心创新 / 方法** · 在语义潜表示上先做一致性中期训练，再从流匹配教师蒸馏；可追加引导降低平均速度偏差。
- **Baseline** · 对照 SD-VAE 与 RAE 潜表示、MeanFlow 训练和蒸馏；比较是否加入生成引导。
- **Benchmark** · ImageNet 256 类条件生成，正文表1–2测 FID、函数评估次数和训练成本。
- **关键结果 / 消融** · 表2报告 RAE 加蒸馏配置在无需引导下取得所列最低的一步、两步 FID，并在固定潜空间内检验蒸馏。
- **适用条件 / 局限** · 依赖流教师和表示编码器，需要计入教师获取成本。当前验证集中于图像类条件生成。

**可复用机制** · 少步生成更换潜表示后应先检验梯度稳定性，再决定从轨迹初始化还是直接训练。

<a id="paper-clay"></a>

## CLAY: Conditional Visual Similarity Modulation in Vision-Language Embedding Space

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Lim_CLAY_Conditional_Visual_Similarity_Modulation_in_Vision-Language_Embedding_Space_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Lim_CLAY_Conditional_Visual_Similarity_Modulation_in_Vision-Language_Embedding_Space_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 视觉近邻取决于此刻关注的属性，固定距离不能组合多个条件。
- **核心创新 / 方法** · 从冻结视觉语言空间构造文本条件相似度，分离文本条件计算与图像特征提取。
- **Baseline** · 表 1–2 对照已有条件相似度及检索方法。
- **Benchmark** · 标准条件检索与由 CLEVR 构建的 CLAY-EVAL，以单条件 mAP 及多条件表现评估。
- **关键结果 / 消融** · 论文报告固定缓存嵌入仍能处理多重条件并维持效率。
- **适用条件 / 局限** · 嵌入若不表达所需属性，后置距离调整不能补回信息。

**可复用机制** · 固定图像索引后，以查询文字改变相似度定义，避免为每种条件重建索引。

<a id="paper-noise-pretraining-inr"></a>

## The Surprising Effectiveness of Noise Pretraining for Implicit Neural Representations

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Vyas_The_Surprising_Effectiveness_of_Noise_Pretraining_for_Implicit_Neural_Representations_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Vyas_The_Surprising_Effectiveness_of_Noise_Pretraining_for_Implicit_Neural_Representations_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 隐式网络初始化敏感，数据预训练的优势成因不清。
- **核心创新 / 方法** · 以不同噪声分布预训同类 INR，比较无结构噪声和带自然频谱的初始化。
- **Baseline** · 对照随机 SIREN、STRAINER、元学习及其他数据初始化。
- **Benchmark** · 表 1 图像拟合 2,000 步，表 2 十段 Pexel 视频 100,000 步拟合和去噪，指标 PSNR。
- **关键结果 / 消融** · 无结构噪声改善拟合，但不是好的去噪先验；自然频谱噪声兼顾两者，近数据预训。
- **适用条件 / 局限** · 训练分布及坐标网络会影响可迁移性，优良训练误差不保证恢复质量。

**可复用机制** · 缺领域数据时按任务选择无结构或自然频谱噪声预训练，分开验拟合和逆问题。

<a id="paper-lease"></a>

## Learning from Semantic Dictionaries: Discriminative Codebook Contrastive Learning for Unified Visual Representation and Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Estepa_Learning_from_Semantic_Dictionaries_Discriminative_Codebook_Contrastive_Learning_for_Unified_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Estepa_Learning_from_Semantic_Dictionaries_Discriminative_Codebook_Contrastive_Learning_for_Unified_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 判别和生成表征对语义与细节的偏好不同。
- **核心创新 / 方法** · 预计算两类离散码本，在掩码重建外用自适应质心加权做判别码本对比。
- **Baseline** · 对照 MAGE、复现 MAGE 和 Sorcen。
- **Benchmark** · ImageNet-1K 线性探针、无条件 FID/IS，并比较少样本和迁移。
- **关键结果 / 消融** · 表 1 LEASE 探针 76.7、FID 9.62，对复现 MAGE 75.0、10.88。
- **适用条件 / 局限** · 离线码本仍有预计算成本，语义质量依两种码本覆盖。

**可复用机制** · 将生成字典的细节重建与判别字典的语义对齐作为可独立验收目标。

<a id="paper-zipmap"></a>

## ZipMap: Linear-Time Stateful 3D Reconstruction via Test-Time Training

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Jin_ZipMap_Linear-Time_Stateful_3D_Reconstruction_via_Test-Time_Training_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Jin_ZipMap_Linear-Time_Stateful_3D_Reconstruction_via_Test-Time_Training_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 全图注意重建的成本随视图二次增长，纯顺序方法常牺牲质量。
- **核心创新 / 方法** · 测试时训练层把图像集编码为紧凑状态，解耦写入和场景查询。
- **Baseline** · 比较 VGGT、π³、CUT3R、TTT3R 等。
- **Benchmark** · RealEstate10K 和 Co3Dv2 报 5/15/30 度姿态 AUC，Sintel、TUM、ScanNet 报旋转和平移误差。
- **关键结果 / 消融** · 单 H100 超过 700 帧低于 10 秒，论文称相较 VGGT 等超过 20 倍，并验流式扩展。
- **适用条件 / 局限** · 隐状态容量和训练集重合需单列，速度依显卡和输入长度。

**可复用机制** · 将多视重建压入可查询隐状态，使一次前向和流式累计共享表示。

<a id="paper-sgdrive"></a>

## SGDrive: Scene-to-Goal Hierarchical World Cognition for Autonomous Driving

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_SGDrive_Scene-to-Goal_Hierarchical_World_Cognition_for_Autonomous_Driving_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_SGDrive_Scene-to-Goal_Hierarchical_World_Cognition_for_Autonomous_Driving_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 通用视觉语言特征不一定表达当前几何和短期运动。
- **核心创新 / 方法** · 学习场景占用、相关主体和目标的层次监督，再用于相机轨迹预测。
- **Baseline** · 对照相机式驾驶方法，表 2 对照仅基础、加入当前及未来信号。
- **Benchmark** · NAVSIM v1 navtest，记录 NC、DAC、TTC、EP 和 PDMS。
- **关键结果 / 消融** · 表 2 的 PDMS 82.2 至 84.7，加入未来监督到 85.5。
- **适用条件 / 局限** · 数据是闭环模拟评分，层次定义迁往其他控制任务须重验。

**可复用机制** · 驾驶规划监督分场景、主体和局部目标，并显式消融未来状态。

<a id="paper-onlinepg"></a>

## OnlinePG: Online Open-Vocabulary Panoptic Mapping with 3D Gaussian Splatting

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhai_OnlinePG_Online_Open-Vocabulary_Panoptic_Mapping_with_3D_Gaussian_Splatting_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhai_OnlinePG_Online_Open-Vocabulary_Panoptic_Mapping_with_3D_Gaussian_Splatting_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 滑窗内实例缺片，局部地图直接最近邻并入会造成身份错配。
- **核心创新 / 方法** · 局部几何语义图聚类并用空间网格表示，在局部与全局间双向二分匹配。
- **Baseline** · 对照在线方法及最近邻、单向匹配。
- **Benchmark** · ScanNetV2、Replica 的全景分割和实时性，表 2 报 PRQ。
- **关键结果 / 消融** · 表 2 最近邻总 PRQ 为 24.67，只前向 35.83，只后向 33.71；正文报告双向改进。
- **适用条件 / 局限** · 依赖窗口有足够视图和可匹配实例，动态拓扑与长遮挡仍需验。

**可复用机制** · 在线语义地图从局部成实例，再以双向匹配更新全局身份。

<a id="paper-if-edit"></a>

## Are Image-to-Video Models Good Zero-Shot Image Editors?

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Are_Image-to-Video_Models_Good_Zero-Shot_Image_Editors_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Are_Image-to-Video_Models_Good_Zero-Shot_Image_Editors_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 图像编辑器对非刚体和物理关系变化难以泛化。
- **核心创新 / 方法** · 转为视频式变化描述，按去噪阶段压缩潜帧，并以短静止轨迹自一致精修。
- **Baseline** · 与既有图像编辑器比较，在四基准分别评非刚体和常规编辑。
- **Benchmark** · TEdBench 报 CLIP-I、LPIPS、CLIP-T，ByteMorph 按镜头、人体和互动类别作 VLM 评价。
- **关键结果 / 消融** · 正文发现视频先验更擅长非刚体与需要推理的变化，一般编辑表现有竞争力。
- **适用条件 / 局限** · 输入和提示必须能表达为时间变化，裁帧及额外推理增加成本。

**可复用机制** · 以视频运动先验执行静态图难以描述的编辑，再选帧并修复锐度。

<a id="paper-pyratok"></a>

## PyraTok: Language-Aligned Pyramidal Tokenizer for Video Understanding and Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Susladkar_PyraTok_Language-Aligned_Pyramidal_Tokenizer_for_Video_Understanding_and_Generation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Susladkar_PyraTok_Language-Aligned_Pyramidal_Tokenizer_for_Video_Understanding_and_Generation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 单尺度视觉词元在语言对齐及细节重建之间受限。
- **核心创新 / 方法** · 在预训视频 VAE 多层用共享二进制码本离散化，以文本量化目标和全局自回归监督联合对齐。
- **Baseline** · 比较先前视频词元器，并进行生成骨干有无 PyraTok 对照。
- **Benchmark** · WebVid-10M、COCO-Val 图像／视频重建，测 PSNR、SSIM、LPIPS 和 V100 延迟；另测文本视频 FVD 与零样本任务。
- **关键结果 / 消融** · 表 2 多骨干加入词元器后改善感知及语义指标，正文报告 零样本分割与定位。
- **适用条件 / 局限** · 依赖预训练编码器和语言标注，额外尺度耗费需要等词元预算比较。

**可复用机制** · 视频词元跨时空尺度共用码本，同时验重建和语言下游。

<a id="paper-rt-splatting"></a>

## RT-Splatting: Joint Reflection-Transmission Modeling with Gaussian Splatting

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Shi_RT-Splatting_Joint_Reflection-Transmission_Modeling_with_Gaussian_Splatting_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Shi_RT-Splatting_Joint_Reflection-Transmission_Modeling_with_Gaussian_Splatting_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 单一透明度同时解释可见反射与透射时易混淆，会产生模糊和浮点。
- **核心创新 / 方法** · 同一组高斯分别作表面反射和体积透射，并对传输支路屏蔽误导梯度。
- **Baseline** · 对照 3DGS、2DGS、反射方法及无门控。
- **Benchmark** · Ref-Real、NeRF-Casting、EnvGS、T&T 和自采透明场景，分整图和透明区测 PSNR、SSIM、LPIPS、FPS。
- **关键结果 / 消融** · 表 1 报告透明区指标和实时渲染，正文观察门控减少浮点。
- **适用条件 / 局限** · 依赖视图能区分反射与透射，复杂折射和材质编辑需再测。

**可复用机制** · 把高斯的几何占据和光学透明度分开，并按反光程度限制跨支路误梯度。

<a id="paper-laps"></a>

## From Observation to Action: Latent Action-based Primitive Segmentation for VLA Pre-training in Industrial Settings

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_From_Observation_to_Action_Latent_Action-based_Primitive_Segmentation_for_VLA_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_From_Observation_to_Action_Latent_Action-based_Primitive_Segmentation_for_VLA_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 连续生产视频缺细粒度动作标记，直接切窗会截断原语。
- **核心创新 / 方法** · 先训轻量潜动作词元器，再由动作能量找边界并聚类原语。
- **Baseline** · 比较 ABD、OTAS，工业设置另比较光流。
- **Benchmark** · GTEA、Breakfast 和工业电机装配的俯视及外视，报告 F1@2s、F1@5s。
- **关键结果 / 消融** · 表 1 GTEA F1@2s 为 63.20，对 ABD 74.23；Breakfast 为 36.72，对 OTAS 39.49。
- **适用条件 / 局限** · 分段性能依动作重复与视角，正文未证明分段提升下游 VLA 控制。

**可复用机制** · 无标人演示以潜动作能量切分，允许和光流边界做等标签对照。

<a id="paper-retrieve-and-segment"></a>

## Retrieve and Segment: Are a Few Examples Enough to Bridge the Supervision Gap in Open-Vocabulary Segmentation?

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Aravanis_Retrieve_and_Segment_Are_a_Few_Examples_Enough_to_Bridge_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Aravanis_Retrieve_and_Segment_Are_a_Few_Examples_Enough_to_Bridge_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 图文预训练对齐较粗，同名类别也可能有视觉歧义。
- **核心创新 / 方法** · 为每张查询图像检索支持类别与标注区域特征，再融合文字和视觉证据拟合轻量分类器。
- **Baseline** · 对照去文本、随机检索及不同融合设置，并比较监督分割。
- **Benchmark** · PASCAL VOC、PASCAL Context、COCO Object、COCO-Stuff、Cityscapes 和 ADE20K，按每类 1、5、10 张支持图报告平均 mIoU。
- **关键结果 / 消融** · 表 1 在 1 图支持时完整方法为 41.59 mIoU，去文本为 34.11；10 图时为 49.02 对 48.00。
- **适用条件 / 局限** · 依赖可检索的像素标注支持和特征相似性；新类的近邻质量与在线拟合开销需另外评估。

**可复用机制** · 当像素标注只有几例时，以查询为条件检索并融合视觉支持与类别文本，见图 5、表 1。

<a id="paper-feco-contact-style-randomization"></a>

## Shoe Style-Invariant and Ground-Aware Learning for Dense Foot Contact Estimation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Jung_Shoe_Style-Invariant_and_Ground-Aware_Learning_for_Dense_Foot_Contact_Estimation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Jung_Shoe_Style-Invariant_and_Ground-Aware_Learning_for_Dense_Foot_Contact_Estimation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 单图密集足接触容易学习鞋型外观捷径，地面纹理也常缺乏辨识度。
- **核心创新 / 方法** · 独立随机化鞋部内容与风格，用对抗训练降低风格依赖，并加入地面感知特征。
- **Baseline** · 对照不随机化、仅风格或仅内容随机化，并拆分地面感知部件。
- **Benchmark** · MMVP 用接触区域精确率、召回与 F1，COFE 检查训练数据变化。
- **关键结果 / 消融** · 表 3 无两项随机化 F1 为 0.522，只做风格为 0.554，两项均用为 0.577。
- **适用条件 / 局限** · 前提是被改动外观与接触真值可分离；外观变化若同时改变摩擦或几何，应使用真实接触标注再验证。

**可复用机制** · 接触点学习可分别扰动外观风格与接触部件内容，测外观捷径；同时分开评估地面约束。见表 2–4。

<a id="paper-shiftlut"></a>

## ShiftLUT: Spatial Shift Enhanced Look-Up Tables for Efficient Image Restoration

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zeng_ShiftLUT_Spatial_Shift_Enhanced_Look-Up_Tables_for_Efficient_Image_Restoration_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zeng_ShiftLUT_Spatial_Shift_Enhanced_Look-Up_Tables_for_Efficient_Image_Restoration_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 增大查表恢复感受野容易使查找表和运算量一起增长。
- **核心创新 / 方法** · 用可学通道空间位移将远邻特征混入局部表，并用不对称分支和自适应采样压缩 LUT。
- **Baseline** · 比较 TinyLUT、去位移方案和其他表压缩方法。
- **Benchmark** · 四倍超分的 Set5、Set14、B100 等并报告 PSNR；另测灰度去噪、去块和实际查表开销。
- **关键结果 / 消融** · 表 4 未额外压缩的 ShiftLUT 是 217 KB、81 ms、Set5 31.33 dB；配 DDM 是 172 KB、98 ms、31.26 dB，显示更小表未必更快。
- **适用条件 / 局限** · 依赖查表平台的访存和索引代价；批次、硬件和误差容忍度变化时应重测。

**可复用机制** · 端侧 LUT 图像恢复可用通道位移传递局部信息，并以误差有界采样在表大小、延迟和质量间选点。见表 4 和图 8。

<a id="paper-natex-native-color-diffusion"></a>

## NaTex: Seamless Texture Generation as Latent Color Diffusion

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Lai_NaTex_Seamless_Texture_Generation_as_Latent_Color_Diffusion_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Lai_NaTex_Seamless_Texture_Generation_as_Latent_Color_Diffusion_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 多视角生成再烘焙会在遮挡、边缘和颜色过渡处产生不一致。
- **核心创新 / 方法** · 将颜色看作附在几何点上的稠密点云，通过几何感知 VAE 与直接三维条件的扩散模型生成颜色。
- **Baseline** · 比较 Paint3D、TexGen、RomanTex、MaterialMVP 与多视角贴图或补全基线。
- **Benchmark** · 纹理生成比较 cFID、CMMD、CLIP、LPIPS；观察图 8 遮挡区的补色与边界。
- **关键结果 / 消融** · 表 2 NaTex 的 cFID 为 21.96，MaterialMVP 为 24.78；CLIP 分数则为 0.908 对 0.921。
- **适用条件 / 局限** · 需要质量合适的三维几何以及足够着色资产；渲染指标不能单独保证复杂材质或任意视角一致。

**可复用机制** · 三维纹理可直接在原生表面颜色点上生成，避免跨视角烘焙拼接，再用遮挡区域验收。见 §3.2、表 2 与图 8。

<a id="paper-honeybee-data-interventions"></a>

## HoneyBee: Data Recipes for Vision-Language Reasoners

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Bansal_HoneyBee_Data_Recipes_for_Vision-Language_Reasoners_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Bansal_HoneyBee_Data_Recipes_for_Vision-Language_Reasoners_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 数据规模、上下文来源与解题链长度同时变化，会掩盖实际有效的数据干预。
- **核心创新 / 方法** · 控制视觉推理训练及验证设置，逐项比较图片描述、纯文本推理等干预，并分别扩大图像、问题和解答数。
- **Baseline** · 对照原数据、文字丰富图、图像扰动、更长思维链和均匀难度等条件。
- **Benchmark** · 按多个视觉推理验证任务平均准确率评估干预，并对照 PLM-3B 和 8B 数据扩规模。
- **关键结果 / 消融** · 表 3 原始数据平均 40.1，先描述图再求解 41.4，加入纯文本 43.1；更长推理链为 36.4。
- **适用条件 / 局限** · 依赖相同模型、训练分配与解答质量，文字推理提升不能推出所有任务上视觉依据更可靠。

**可复用机制** · 视觉推理训练在扩数据前可比较增加图像描述和纯文本解题，警惕更长思维链或更多干扰项反而降低收益。见表 3。

<a id="paper-one-shot-flow-any-time-frame"></a>

## One-Shot Flow, Any-Time Frame: A Bidirectional Warping Framework for Event-Based Video Frame Interpolation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Fu_One-Shot_Flow_Any-Time_Frame_A_Bidirectional_Warping_Framework_for_Event-Based_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Fu_One-Shot_Flow_Any-Time_Frame_A_Bidirectional_Warping_Framework_for_Event-Based_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 前向扭曲高效但容易留下孔洞，逐时刻反向估计在插入许多帧时很贵。
- **核心创新 / 方法** · 通过事件观测一次估计双向轨迹，再查询任意目标时间的两向流并融合两类扭曲结果。
- **Baseline** · 比较 TimeLens、CBM-Net、TLXNet、TimeTracker 与去双向估计或双向扭曲版本。
- **Benchmark** · GOPRO、SNU-FILM、BS-ERGB、HS-ERGB；质量报告 PSNR/SSIM，GOPRO 比较 31、63、127 帧成本。
- **关键结果 / 消融** · 表 3 中 TLXNet 在 63 和 127 帧设置上超出 24 GB，本文在三种设置均完成；表 4 单独比较双向部件对质量影响。
- **适用条件 / 局限** · 需要事件数据及端点观测，遮挡与轨迹不连续时仍可能出错；无事件传感器时不能直接复用性能结论。

**可复用机制** · 需要在同一输入区间产出多帧时，先缓存可按时间查询的双向流轨迹，减少每个时刻重复流估计。见表 3–4。

<a id="paper-ri-mamba-point-ordering"></a>

## RI-Mamba: Rotation-Invariant Mamba for Robust Text-to-Shape Retrieval

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Nguyen_RI-Mamba_Rotation-Invariant_Mamba_for_Robust_Text-to-Shape_Retrieval_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Nguyen_RI-Mamba_Rotation-Invariant_Mamba_for_Robust_Text-to-Shape_Retrieval_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 点云状态空间编码依赖顺序，任意旋转会破坏空间局部性及文本检索。
- **核心创新 / 方法** · 用全局和局部参考框架分离形状与姿态，对点做 Hilbert 排序，再以条件调制回注方向信息。
- **Baseline** · 对比 RITransformer、PointBERT-TAMM、DuoMamba 等，分别消融排序、位置、方向和双向扫描。
- **Benchmark** · Text2Shape、OmniObject3D 和 ModelNet40，测文到形状检索、三维检索与零样本分类。
- **关键结果 / 消融** · 表 5 Omni3D 得分完整 14.7，去 Hilbert 排序 13.9，联合去位置及方向等信息 8.2。
- **适用条件 / 局限** · 依赖参考框架可稳定估计；高度对称或局部观测不足时应复测不变性、方向恢复和语义效果。

**可复用机制** · 对任意旋转点云可先在局部坐标建立稳定序列，再以独立分支回注方向信息，见 §4.5 和表 5。

<a id="paper-pointthinker-pointwise-credit"></a>

## PointThinker: Point-Incentivized Parallel Thinking for Multimodal Large Language Model

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Hu_PointThinker_Point-Incentivized_Parallel_Thinking_for_Multimodal_Large_Language_Model_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Hu_PointThinker_Point-Incentivized_Parallel_Thinking_for_Multimodal_Large_Language_Model_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 多条推理经常重复，同一总体正确性奖励也掩盖有效证据和无效证据。
- **核心创新 / 方法** · 先列多个视觉关键点并独立推理，再以单点自验证与整条轨迹奖励联合分配局部信用。
- **Baseline** · 以 Qwen2.5-VL-7B 为底座，对照标准并行推理、只加点结构及加 GPPO。
- **Benchmark** · Hallusion、MathVista、MMVet 等图像理解与视频基准，报告任务准确率或官方得分。
- **关键结果 / 消融** · 表 3 Hallusion/MathVista 平均分，标准并行为 63.5，按点并行为 64.9；表 4 只加点结构的 Hallusion/MMVet 为 56.8/71.2，再加 GPPO 为 58.7/73.4。
- **适用条件 / 局限** · 关键点可能只是模型的概念提示，仍需独立验证是否真正依据图像，且自评信号可能与最终答案同源。

**可复用机制** · 并行视觉推理可按视觉关键点分支，并对同一整条轨迹内各点分配不同奖励。见表 3–4。

<a id="paper-balanced-hierarchical-contrast"></a>

## Balanced Hierarchical Contrastive Learning with Decoupled Queries for Fine-grained Object Detection in Remote Sensing Images

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Balanced_Hierarchical_Contrastive_Learning_with_Decoupled_Queries_for_Fine-grained_Object_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_Balanced_Hierarchical_Contrastive_Learning_with_Decoupled_Queries_for_Fine-grained_Object_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 细粒度类别不平衡使常见类别主导跨层对比，语义梯度还会干扰通用定位。
- **核心创新 / 方法** · 用可学原型均衡同层类别贡献，并分开负责层次语义与定位的查询。
- **Baseline** · 以 DETR 系统为底座，表1消融均衡对比和查询解耦，表2比较原型实现。
- **Benchmark** · ShipRSImageNet、FAIR1M-v1.0/v2.0 的细粒度检测，正文表1–3汇报各比较。
- **关键结果 / 消融** · 正文表1显示两组件可分别对照，表2验证可学类别原型。
- **适用条件 / 局限** · 依赖可靠层次标签及训练批次覆盖；稀有样本不足时应单独测长尾召回。

**可复用机制** · 对层次类别按批次均衡梯度，并将层次语义学习与定位查询解耦。

<a id="paper-svd-style-personalization"></a>

## A Training-Free Style-Personalization via SVD-Based Feature Decomposition

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Lee_A_Training-Free_Style-Personalization_via_SVD-Based_Feature_Decomposition_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Lee_A_Training-Free_Style-Personalization_via_SVD-Based_Feature_Decomposition_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 参考风格特征容易同时携带主体内容，影响目标提示和结构。
- **核心创新 / 方法** · 在关键尺度以奇异值分解重组主要风格特征，并在细尺度校正结构注意。
- **Baseline** · 正文对照训练式风格定制以及不同控制环节。
- **Benchmark** · 用单参考风格的图像生成测试风格遵循、提示遵循和运行速度。
- **关键结果 / 消融** · 正文报告无需额外训练即可取得相近的风格与提示忠实度，并将两类控制分开分析。
- **适用条件 / 局限** · 奇异分量的功能归因依赖生成主干及尺度，细图案可能同时承担风格和结构。

**可复用机制** · 用逐生成尺度的奇异值诊断选择风格注入位置，细尺度单独验结构。

<a id="paper-frequency-mixup-supervision"></a>

## Beyond the Ground Truth: Enhanced Supervision for Image Restoration

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Ryou_Beyond_the_Ground_Truth_Enhanced_Supervision_for_Image_Restoration_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Ryou_Beyond_the_Ground_Truth_Enhanced_Supervision_for_Image_Restoration_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 真实采集中的监督图不够清晰，直接采用超分结果又会把幻觉写进训练标签。
- **核心创新 / 方法** · 由条件掩码决定各频率处使用原监督还是超分监督，再以增强标签训练轻量精化器。
- **Baseline** · 对照原标签、超分替换及选择性融合，精化模块接在既有修复器输出。
- **Benchmark** · 正文多个真实图像复原实验，比较感知质量及内容保持。
- **关键结果 / 消融** · 正文显示增强监督改善复原，机制在保留原图成分的同时增加可用细节。
- **适用条件 / 局限** · 超分偏差难仅凭频率完全分离，需有参考内容或人工检查以检验细节保真。

**可复用机制** · 修复训练标签本身有退化时，分频融合原标签与超分版本，并独立验细节真实性。

<a id="paper-sineproject"></a>

## SineProject: Machine Unlearning for Stable Vision-Language Alignment

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Garg_SineProject_Machine_Unlearning_for_Stable_Vision-Language_Alignment_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Garg_SineProject_Machine_Unlearning_for_Stable_Vision-Language_Alignment_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 删除特定知识会引起图文表示漂移，使正常任务也退化。
- **核心创新 / 方法** · 冻结原投影器，以可训练正弦调制增量稳定其条件数。
- **Baseline** · 表1–2比较常见遗忘方法，另消融不同层和调制函数。
- **Benchmark** · LLaVA-v1.5 7B及13B，在 SafeEraser 与 MLLMU-Bench 分测遗忘、保留与正常查询。
- **关键结果 / 消融** · 正文报告所测目标知识遗忘与正常请求拒绝之间的权衡改善。
- **适用条件 / 局限** · 证据限于所测投影结构和数据，遗忘完整性需对其他访问形式独立检验。

**可复用机制** · 进行防御性遗忘时监控跨模态投影器条件数，并把无关正常查询误拒纳入验收。

<a id="paper-p2t-reward-attribution"></a>

## Unlocking Token Rewards via Training-Free Reward Attribution

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_Unlocking_Token_Rewards_via_Training-Free_Reward_Attribution_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wu_Unlocking_Token_Rewards_via_Training-Free_Reward_Attribution_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 阶段或整条答案的奖励不能说明哪些词元有实际贡献。
- **核心创新 / 方法** · 以语义空词元为参照，用一次奖励前向和反传近似对各词元的影响，供现有强化学习更新使用。
- **Baseline** · 对照结果奖励、替代稠密奖励及 P2T 内部变体。
- **Benchmark** · 正文表1–3在数学推理任务上比较正确率及奖励配置。
- **关键结果 / 消融** · 正文报告在所测多个数学推理设置优于整段结果奖励，表3检验所用归因设计。
- **适用条件 / 局限** · 一阶近似对替换幅度敏感，且取决于原过程奖励是否可信及空词元意义。

**可复用机制** · 用过程奖励对词元替换的一阶近似提供信用分配，可避免逐词元运行奖励模型。

<a id="paper-aleatoric-uncertainty-spectrum"></a>

## Delving Aleatoric Uncertainty in Medical Image Segmentation via Vision Foundation Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Delving_Aleatoric_Uncertainty_in_Medical_Image_Segmentation_via_Vision_Foundation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Delving_Aleatoric_Uncertainty_in_Medical_Image_Segmentation_via_Vision_Foundation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 分割训练数据同时存在采集噪声和含糊标注，平均加权会放大部分噪声监督。
- **核心创新 / 方法** · 基于视觉基础分割模型解码特征的奇异值能量构造逐类感知尺度，用于样本筛选、动态损失调权和标签去噪。
- **Baseline** · 表1–3比较相同骨干的原始训练、替代不确定性量化方法及不同基础模型；MedSAM2是被检验的量化基础模型之一。
- **Benchmark** · 五个公开 CT/MRI 多器官及肿瘤分割数据集，统一预处理后在测试集衡量 Dice 和 mIoU。
- **关键结果 / 消融** · 表1–3显示滤样和动态优化各可改善多个骨干的测试集分割，且替换奇异值能量量化会影响效果。
- **适用条件 / 局限** · 感知尺度依赖基础模型特征覆盖；难例和误标可能得到相似评分，不能把代理量直接当作已校准的噪声概率。

**可复用机制** · 用解码特征的奇异值能量估计训练样本难度，决定筛除样本还是逐类调权。

<a id="paper-visual-feature-steering"></a>

## Language Models Can Explain Visual Features via Steering

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Ferrando_Language_Models_Can_Explain_Visual_Features_via_Steering_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Ferrando_Language_Models_Can_Explain_Visual_Features_via_Steering_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 最高激活图像同时有多个视觉概念，自动解释可能抓住共现物。
- **核心创新 / 方法** · 将空白输入送入视觉语言模型，分别干预视觉编码器的 SAE 特征并读取语言解释，再由真实激活示例校正。
- **Baseline** · Top-k 示例解释、纯 Steering、随机等范数干预和扰动方向对照。
- **Benchmark** · 对 Gemma 3 和 InternVL3-14B 等的视觉 SAE 测试，比较 AUROC、分割重叠、合成激活及 CLIP 对齐。
- **关键结果 / 消融** · 表1显示 Steering-informed Top-k 整体优于单独 Steering；纯 Steering 的分割重叠尚可，但合成激活及 AUROC 落后于混合版本。
- **适用条件 / 局限** · 依赖视觉特征能被语言头读取，干预强度或视觉编码器变化均可能改变解释质量。

**可复用机制** · 解释视觉 SAE 特征时，在最高激活示例外加入因果干预来减少共现概念误归因。

<a id="paper-panda-multimodal-domain-adaptation"></a>

## PanDA: Unsupervised Domain Adaptation for Multimodal 3D Panoptic Segmentation in Autonomous Driving

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Pan_PanDA_Unsupervised_Domain_Adaptation_for_Multimodal_3D_Panoptic_Segmentation_in_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Pan_PanDA_Unsupervised_Domain_Adaptation_for_Multimodal_3D_Panoptic_Segmentation_in_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · RGB 或 LiDAR 单路退化时，跨模态融合不稳。只保留高置信区域使实例伪掩码碎片化。
- **核心创新 / 方法** · 非对称地丢弃不同区域模拟模态退化，用二维类别和三维几何专家先验分别纠正类别、补足实例掩码。
- **Baseline** · 源域监督、无新增模块的 Mean Teacher、Pano-xMUDA 和 Pano-UniDseg，以及目标域监督上界。
- **Benchmark** · USA→SG、Sunny→Rainy、Day→Night、SemanticKITTI→nuScenes；以 PQ、PQth、PQst 评估。
- **关键结果 / 消融** · 表1中最终方法相对源域基线在四种设置的 PQ 分别提升 13.2%、8.9%、8.4%、53.3%（作者报告相对提升）；表2–3分别检验增强与伪标签。
- **适用条件 / 局限** · 要求两种模态较好对齐且二维和三维专家仍能提供先验，双模态同时失效的场景缺乏证据。

**可复用机制** · 单传感器退化的目标域适配中，用实例补全修复伪掩码，并模拟模态局部失真。

<a id="paper-freeartgs"></a>

## FreeArtGS: Articulated Gaussian Splatting Under Free-moving Scenario

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Dai_FreeArtGS_Articulated_Gaussian_Splatting_Under_Free-moving_Scenario_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Dai_FreeArtGS_Articulated_Gaussian_Splatting_Under_Free-moving_Scenario_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 自由采集时关节和物体整体都在运动，静止基座假设失效。
- **核心创新 / 方法** · 以跟踪和特征模型作先验，从相对运动分割刚性部件；校准统一物体位姿并估计关节，再用可微高斯渲染联合细化。
- **Baseline** · 与 RSRD、Articulate-Anything 等关节估计和重建方案比较；消融平滑、初始化、抗噪和混合渲染。
- **Benchmark** · FreeArt-21、Video2Articulation-S 及真实采集物体；评估关节误差、几何重建和渲染。
- **关键结果 / 消融** · 表1–3显示自由移动设置下关节与几何表现优于所测对照，去掉抗噪估计也会损害结果。
- **适用条件 / 局限** · 当前假设对象只有两个部件，要求 RGB-D，且依赖外部跟踪与特征先验质量。

**可复用机制** · 从自由移动的 RGB-D 视频识别关节时，先用部件相对运动消去物体全局位姿变化。

<a id="paper-recofuse"></a>

## ReCoFuse: Ultra-Robust Image Fusion via Restorative Multi-Modal Diffusion Reciprocal Coupling

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_ReCoFuse_Ultra-Robust_Image_Fusion_via_Restorative_Multi-Modal_Diffusion_Reciprocal_Coupling_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_ReCoFuse_Ultra-Robust_Image_Fusion_via_Restorative_Multi-Modal_Diffusion_Reciprocal_Coupling_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 独立恢复后再融合无法及时利用另一模态补回缺失信息，直接硬回归融合也容易继承退化。
- **核心创新 / 方法** · 各模态使用独立扩散恢复分支，以时间感知模块在每个采样步聚合信息并反馈到恢复分支，配合交替正则优化。
- **Baseline** · 比较 OmniFuse、Text-IF、CrossFuse、U2Fusion、LRRNet 等，涵盖外加恢复与重训对照。
- **Benchmark** · MFNet、FMB、LLVIP 的红外及可见光融合，加入弱光、条纹、噪声等退化，报告 MI、CC、VIF 等，并在 AWMM-100k 做泛化评估。
- **关键结果 / 消融** · 表1–3比较多种退化和消融，双向耦合的总体结果优于单独恢复及融合方案。
- **适用条件 / 局限** · 需配对模态和可用互补信息；逐步聚合增加推理开销。

**可复用机制** · 单路信号退化的多模态融合中，把跨模态信息反馈给每次恢复迭代，而非只融合最终恢复结果。

<a id="paper-diffusion-drift-kernel"></a>

## The Drift Kernel: Why Diffusion Models Change Even When Told Not To

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Ram_The_Drift_Kernel_Why_Diffusion_Models_Change_Even_When_Told_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Ram_The_Drift_Kernel_Why_Diffusion_Models_Change_Even_When_Told_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 即便要求保持原图，扩散编辑也会产生变化，原始编辑指标混入模型自身漂移。
- **核心创新 / 方法** · 定义空编辑漂移核，估计噪声强度条件下的期望平方图像偏差；用解码器雅可比分析二次趋势，并用可控合成解码器区分噪声与编辑偏置。
- **Baseline** · SD1.5、SD2.1、SDXL 和 InstructPix2Pix 对照，比较空提示和复制提示，并构造不同类型合成解码器。
- **Benchmark** · NoOp-Bench 有12万基线输出及9600份消融输出，主要分析像素偏差和拟合 R²，并补充 LPIPS 与 CLIP。
- **关键结果 / 消融** · 前三种模型聚合二次拟合 R²=0.97，逐模型仅0.10–0.26；InstructPix2Pix 均值趋势较平但变异较高。
- **适用条件 / 局限** · 二阶近似和聚合统计无法可靠预测单张图的偏差，像素距离也不能覆盖所有感知变化。

**可复用机制** · 评价扩散编辑时，先测空编辑漂移并按模型和噪声强度建立身份保真基线。

<a id="paper-arcache"></a>

## Accelerating Autoregressive Video Diffusion via History-Guided Cache and Residual Correction

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Nan_Accelerating_Autoregressive_Video_Diffusion_via_History-Guided_Cache_and_Residual_Correction_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Nan_Accelerating_Autoregressive_Video_Diffusion_via_History-Guided_Cache_and_Residual_Correction_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 固定片段扩散缓存用在自回归长视频时，近似误差会通过历史条件蔓延。
- **核心创新 / 方法** · 用历史引导缓存调度减少段内误差，并在跨段时修正缓存残差轨迹，训练无需改动。
- **Baseline** · 无缓存原模型、PAB、TeaCache、TaylorSeer；表2分别消融缓存调度和残差修正。
- **Benchmark** · FramePack-F1、SkyReels-V2 和 Matrix-Game，比较推理加速及 PSNR、SSIM、LPIPS 等与原视频的相似性指标。
- **关键结果 / 消融** · 三个模型分别加速2.88×、1.87×、3.13×；表2检验两个组件，时序指标显示后段漂移得到抑制。
- **适用条件 / 局限** · 仍要手调重算阈值，保真指标以未加速模型输出为参照。

**可复用机制** · 滚动生成视频时，以历史偏差决定每段何时重算，并校正向后传播的残差。

<a id="paper-hypernas"></a>

## HyperNAS: Enhancing Architecture Representation for NAS Predictor via Hypernetwork

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Lv_HyperNAS_Enhancing_Architecture_Representation_for_NAS_Predictor_via_Hypernetwork_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Lv_HyperNAS_Enhancing_Architecture_Representation_for_NAS_Predictor_via_Hypernetwork_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 只编码局部结构并直接回归性能，低样本下难学到候选架构之间的共性。
- **核心创新 / 方法** · 把完整宏观架构编码交给排序预测器，同时训练共享超网络学习跨架构模式，以动态多任务权重平衡辅助信号。
- **Baseline** · 对比 PINAT、GMAE-NAS、NP、NAO、CTNAS 等排序预测器；完整搜索另与论文表3–4列出的 NAS 方法比较。
- **Benchmark** · 覆盖 NAS-Bench-101、NAS-Bench-201 及 ViT 在内的五种搜索空间，以排序相关性、试验样本数和分类 top-1 评估。
- **关键结果 / 消融** · NAS-Bench-101 仅用50个样本时，表1的排序分数为0.678，PINAT为0.580；CIFAR-10和ImageNet搜索结果 top-1 分别为97.60%和82.4%。
- **适用条件 / 局限** · 依赖候选架构能被共同编码、超网络能在候选间共享；辅助目标增加训练成本。

**可复用机制** · 昂贵的架构试验样本不足时，用共享超网络作为排序预测器的训练辅助目标。

<a id="paper-dehallu3d-cyclic-view-consistency"></a>

## Dehallu3D: Hallucination-Mitigated 3D Generation from a Single Image via Cyclic View Consistency Refinement

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Dehallu3D_Hallucination-Mitigated_3D_Generation_from_a_Single_Image_via_Cyclic_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_Dehallu3D_Hallucination-Mitigated_3D_Generation_from_a_Single_Image_via_Cyclic_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 稀疏生成视图不连续会使重建出现孔洞或突起；统一平滑又会抹掉有用几何。
- **核心创新 / 方法** · 加入密集相邻视角的一致性和自适应平滑，辅以几何异常风险度量。
- **Baseline** · 比较 Wonder3D、InstantMesh 等重建方法，以及去掉一致性或平滑项的版本。
- **Benchmark** · 单图生成三维网格，在新视图测 PSNR、SSIM、LPIPS、CLIP 相似度，在几何上测 CD 和 F-Score，并报告优化耗时。
- **关键结果 / 消融** · 表 3 从 15° 改到 5° 的相邻视角，F-Score 从 0.3936 到 0.4212，耗时从 110.8 秒到 163.3 秒；加密到 3° 得分 0.4203。
- **适用条件 / 局限** · 多视角先验若在遮挡区系统错误，一致性也可能固化错误；相机分布和细长结构需另查。

**可复用机制** · 稀疏视角三维生成应联合检查视角间连续性和锐利几何保留，测视角加密收益和耗时。见表 2–3。

<a id="paper-afss-anti-forgetting-sampling"></a>

## Does YOLO Really Need to See Every Training Image in Every Epoch?

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xie_Does_YOLO_Really_Need_to_See_Every_Training_Image_in_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xie_Does_YOLO_Really_Need_to_See_Every_Training_Image_in_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 每轮完整遍历会在已学会的样本上重复计算，永久筛掉易例则可能遗忘。
- **核心创新 / 方法** · 取逐图召回和精确率的较小值衡量学习充分度。难例每轮保留，中等例部分采样，易例按上次见到的时间稀疏复习。
- **Baseline** · 比较完整遍历、课程学习、自步学习、数据裁剪和数据蒸馏。
- **Benchmark** · MS COCO 2017、PASCAL VOC 2007，以及 DOTA-v1.0、DIOR-R 旋转框，报告 AP 和训练耗时。
- **关键结果 / 消融** · 表 3 YOLO11s 基线为 47.0 AP、43.9 小时，AFSS 为 47.2 AP、28.4 小时；静态数据裁剪为 40.5 AP、31.8 小时。
- **适用条件 / 局限** · 需要逐样本可评估且预算容得下定期更新；极少见类别或噪声标签应按子组检查是否被错误降频。

**可复用机制** · 检测训练按图像是否已学会动态降频，并优先复看最长未见的易例，见表 3–5。

<a id="paper-private-personalized-federated-diffusion"></a>

## Personalized Federated Training of Diffusion Models with Privacy Guarantees

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Patel_Personalized_Federated_Training_of_Diffusion_Models_with_Privacy_Guarantees_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Patel_Personalized_Federated_Training_of_Diffusion_Models_with_Privacy_Guarantees_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 独立训练在客户端的稀缺类别上数据不足，共享生成器则需控制单个参与方贡献造成的信息泄漏。
- **核心创新 / 方法** · 共同学习共享扩散结构并保留客户端个性化模型，给出差分隐私与高斯混合假设下的效用分析。
- **Baseline** · 对照非私有集中训练、非私有 FedDM、私有非协作训练。
- **Benchmark** · CIFAR-10、Colorized MNIST、CelebA；分多数与少数类报告 FID，并另做隐私防护评估。
- **关键结果 / 消融** · 表 1 CelebA 少数类 FID 从私有非协作的 41.38 降到 28.09；CIFAR-10 从 36.44 到 35.78，收益受任务影响。
- **适用条件 / 局限** · 理论效用结论有分布假设，隐私保证取决于具体隐私会计和参与协议；不同泄漏渠道需独立验证。

**可复用机制** · 私有多方生成训练可把共享成分与客户端个性化条件分开，并按少数类别检查隐私约束下的质量。见理论部分、表 1。

<a id="paper-kalos-localization-first-agreement"></a>

## KaLOS finds Consensus: A Meta-Algorithm for Evaluating Inter-Annotator Agreement in Complex Vision Tasks

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Tschirschwitz_KaLOS_finds_Consensus_A_Meta-Algorithm_for_Evaluating_Inter-Annotator_Agreement_in_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Tschirschwitz_KaLOS_finds_Consensus_A_Meta-Algorithm_for_Evaluating_Inter-Annotator_Agreement_in_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 框或区域标注没有预先给定的一一对应，直接计标签共识会同时混入位置误差与偶然一致。
- **核心创新 / 方法** · 先用按经验分布校准的空间匹配将实例对齐，再构成名义一致性矩阵，补充标注者聚类与定位灵敏性。
- **Baseline** · 比较不同空间对应求解器及未校准的局部匹配；用已知扰动检查一致性响应。
- **Benchmark** · 正文以对象检测多标注数据和从真实分布构造的噪声设定作为主要验证；比较对应 F1 及一致性指标随噪声变化。
- **关键结果 / 消融** · 图 3–6 比较求解和扰动设定，平均 KαLOS 对一致性水平呈单调响应。
- **适用条件 / 局限** · 一致性不能判定谁标得正确；正文实证主要是检测，推广到三维分割或关键点要重新校准匹配。

**可复用机制** · 检测或空间标注评估先校准跨标注者的实例对应，再计类别一致性，用人为注入噪声验证指标。见 §4、图 3–6。

<a id="paper-pld-blackbox-debias"></a>

## Rank-Guided Pseudo-Bias Learning for Robust Black-Box Adaptation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Dwivedi_Rank-Guided_Pseudo-Bias_Learning_for_Robust_Black-Box_Adaptation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Dwivedi_Rank-Guided_Pseudo-Bias_Learning_for_Robust_Black-Box_Adaptation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 冻结视觉编码器可能保留与标签偶然相关的特征，而目标域缺少真实偏差组标注。
- **核心创新 / 方法** · 用秩正则适配器放大潜在偏差，聚类得到代理组，再用组感知边际对比目标改善表征。
- **Baseline** · 比较 ERM、Co-Adapt、CM，并消融对比学习与组边界项。
- **Benchmark** · CelebA、Waterbirds、CMNIST，分编码器和偏差强度，报告最差组、平均组准确率及差距。
- **关键结果 / 消融** · 表 1 Waterbirds ResNet-18 上最差组为 83.01%，CM 为 80.29%；平均组分别为 85.26% 和 84.56%。
- **适用条件 / 局限** · 训练可不见目标组标签，但验证仍需独立组定义；存在多个相关偏差时，代理聚类可能只恢复最显著的一种。

**可复用机制** · 只有冻结特征时，可先训练偏差放大探测器构造伪分组，再用最差组验证去偏收益。见表 1、4。

<a id="paper-tacs-learned-context-selection"></a>

## Learning What Helps: Task-Aligned Context Selection for Vision Tasks

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Guo_Learning_What_Helps_Task-Aligned_Context_Selection_for_Vision_Tasks_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Guo_Learning_What_Helps_Task-Aligned_Context_Selection_for_Vision_Tasks_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 外观相似的上下文可能与当前问题冗余，模型也可能只受额外输入或重复视图影响。
- **核心创新 / 方法** · 联合训练选择器与下游模型，将任务损失和强化学习反馈用于选择能补足查询的示例。
- **Baseline** · 对照无上下文、空图、重复图、带噪图、DINOv3 相似检索，以及不训练选择策略版本。
- **Benchmark** · 18 个细粒度识别与医学分类、分割任务；按任务使用准确率、AUC、召回或分割指标。
- **关键结果 / 消融** · 表 4 汇总的 15 项均值，无上下文 87.6、DINOv3 相似图 88.0、任务感知选择 89.5。
- **适用条件 / 局限** · 需要规模合适的候选库和下游监督，换目标任务应重估什么是互补；汇总不同指标易掩盖个别任务反向。

**可复用机制** · 可将检索上下文按下游预测收益学习，且须对照重复输入、空输入和相似检索。见表 4–5。

<a id="paper-r-ground-region-search"></a>

## Breaking the Regional Perception Bottleneck of Multimodal Large Language Models via External Reasoning Framework

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Breaking_the_Regional_Perception_Bottleneck_of_Multimodal_Large_Language_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Breaking_the_Regional_Perception_Bottleneck_of_Multimodal_Large_Language_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 语言模型规模上升不一定改善像素坐标定位，部分误差来自缺少对区域的检索及复核。
- **核心创新 / 方法** · 将定位动作组织成树搜索，用跨模态特征对齐评估候选，再根据局部证据加权投票。
- **Baseline** · 同一 Qwen2.5-VL-7B 上比较无推理、视觉链、语义链；另测 Qwen3-VL-8B。
- **Benchmark** · RefCOCO/+/g 指代表达定位，按划分报告 AP@0.5，并做候选组合和打分消融。
- **关键结果 / 消融** · 表 2 RefCOCO+ 平均无推理 83.4、语义链 88.27、R-Ground 91.93。
- **适用条件 / 局限** · 需多个推理步和可靠区域打分，不能将准确率差当成等成本收益；对复杂场景的耗时及误定位仍应独立核验。

**可复用机制** · 区域定位相比继续扩模型，可对同一骨干测试把额外计算放到搜索局部证据的收益，见表 2–4。

<a id="paper-sensenova-si-spatial-diagnostics"></a>

## Scaling Spatial Intelligence with Multimodal Foundation Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Cai_Scaling_Spatial_Intelligence_with_Multimodal_Foundation_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Cai_Scaling_Spatial_Intelligence_with_Multimodal_Foundation_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 总体空间问答分数上升可能来自训练分布贴合及语言捷径，不能揭示空间依据。
- **核心创新 / 方法** · 按空间任务分类构建训练和分析，并在 MindCube 更换评测口径，包含去视觉对照。
- **Baseline** · 比较 SenseNova-SI-InternVL3-8B、MindCube-SFT-RawQA 与 Gemini-3-Pro-Preview，另测输入帧数变化。
- **Benchmark** · 正文§5.3–5.4、表2–3比较 VSI-Bench、VSI-Debiased、MindCube 多种条件下的准确率。
- **关键结果 / 消融** · 表3中 SenseNova-SI 标准 MindCube 为85.6，Hard circular 为75.6，去视觉仍为52.5；MindCube-SFT-RawQA 去视觉50.7，接近标准51.7。
- **适用条件 / 局限** · 去视觉只是定位捷径的诊断，仍需用保持答案语义的视觉变换确认真实空间依据。

**可复用机制** · 扩张空间训练数据时，应同时追踪能力分项，并在去掉视觉或改变视角顺序后复测。

<a id="paper-savn-ce-magnet"></a>

## Semantic Audio-Visual Navigation in Continuous Environments

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zeng_Semantic_Audio-Visual_Navigation_in_Continuous_Environments_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zeng_Semantic_Audio-Visual_Navigation_in_Continuous_Environments_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 连续导航中目标变静默会中断当前可观测的声源信号。
- **核心创新 / 方法** · MAGNet 结合目标空间和语义编码、历史音视频以及自运动信息。
- **Baseline** · 与 SAVi 等方法比较，并消融目标推断、记忆和自运动。
- **Benchmark** · SAVN-CE 仿真连续导航，洁净和干扰两类环境。表1测导航成功率，表2按声源时段测定位，表3做组件消融。
- **关键结果 / 消融** · 表2在洁净环境的静默段，20°阈值 F 从 SAVi 的0.006增至0.140；正文报告导航成功率最多改善12.1个百分点。
- **适用条件 / 局限** · 真实房间混响、设备位姿误差和移动声源需单独验证，当前证据来自仿真。

**可复用机制** · 为断续声源保留时序记忆并用自运动更新目标方位，按有声和静默分别验收。

<a id="paper-ces-execution-feedback"></a>

## Training High-Level Schedulers with Execution-Feedback Reinforcement Learning for Long-Horizon GUI Automation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Deng_Training_High-Level_Schedulers_with_Execution-Feedback_Reinforcement_Learning_for_Long-Horizon_GUI_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Deng_Training_High-Level_Schedulers_with_Execution-Feedback_Reinforcement_Learning_for_Long-Horizon_GUI_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 统一策略容易混淆高层任务进度与底层界面动作，长程执行容易丢状态。
- **核心创新 / 方法** · 用协调器拆分任务，以状态跟踪器压缩进度，根据执行反馈阶段性训练高层角色。
- **Baseline** · 对照原执行器、仅提示分角色的 CES-P 和训练后的 CES，表3消融角色与阶段。
- **Benchmark** · AITZ、AMEX、GUI-Odyssey 的长程任务，正文表1–2报告动作类型、定位及成功率。
- **关键结果 / 消融** · 表2使用 UI-R1-3B 时 GUI-Odyssey 成功率32.49，提示分工后14.44，训练高层后38.04，提示式分角色并不保证增益。
- **适用条件 / 局限** · 需要可获得的状态反馈，迁移至有不可逆副作用的任务应另做权限及副作用验收。

**可复用机制** · 长程良性 GUI 自动化可冻结执行器，把训练资源集中在有执行反馈的调度与状态维护。

<a id="paper-direct-ovss"></a>

## Direct Segmentation without Logits Optimization for Training-Free Open-Vocabulary Semantic Segmentation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Direct_Segmentation_without_Logits_Optimization_for_Training-Free_Open-Vocabulary_Semantic_Segmentation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Direct_Segmentation_without_Logits_Optimization_for_Training-Free_Open-Vocabulary_Semantic_Segmentation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 图文相似度的逐像素最大值容易产生错分，进一步训练或改写注意力增加模型依赖。
- **核心创新 / 方法** · 从特征分布差异导出分割解析量，结合空间后处理生成语义图。
- **Baseline** · 对照原 logits 取最大值、仅 KL、最优路径及最大速度方案。
- **Benchmark** · VOC21、COCO-Stuff、Cityscapes、ADE20K 等开放词表分割，表2比较各组件指标。
- **关键结果 / 消融** · 表2仅原始 logits 四项均值8.9，KL 加后处理19.6，加入最大速度40.8；两种解析量合用为38.4。
- **适用条件 / 局限** · 同类空间块共享差异结构是假设，小遮挡与跨域提示要复测后处理误差。

**可复用机制** · 在开放词表分割中将分布差异作为直接解码信号，对照迭代优化或直接取 logits 最大值。

<a id="paper-moving-border-ownership"></a>

## Moving Border Ownership for Event-based Motion Segmentation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Hua_Moving_Border_Ownership_for_Event-based_Motion_Segmentation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Hua_Moving_Border_Ownership_for_Event-based_Motion_Segmentation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 事件密集于运动边界，二值掩码未显式编码遮挡哪一侧属于前景。
- **核心创新 / 方法** · 用合成事件生成边界及归属真值，联合学习带符号的距离场和运动掩码。
- **Baseline** · 与传统及学习式事件分割比较，§7.1固定架构及训练数据只移除归属监督。
- **Benchmark** · EED、EVIMO1、EVIMO2、EMSMC 的零样本评测，报告检测和分割指标及吞吐。
- **关键结果 / 消融** · EVIMO2 中，仅掩码监督为76.00 mIoU，增加边界归属为81.55。
- **适用条件 / 局限** · 依赖合成得到准确归属，实际低事件率和特殊传感器噪声仍需复查。

**可复用机制** · 用有符号边界归属场表示运动前景在哪一侧，并控制网络和数据比较二值监督。

<a id="paper-tgtrack"></a>

## TGTrack: Temporal Generative Learning for Unified Single Object Tracking

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Geng_TGTrack_Temporal_Generative_Learning_for_Unified_Single_Object_Tracking_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Geng_TGTrack_Temporal_Generative_Learning_for_Unified_Single_Object_Tracking_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 仅更新模板或传递词元难以显式学习目标动态。
- **核心创新 / 方法** · 用生成式解码器从历史预测未来，辅以门控融合及时序标记。
- **Baseline** · 比较既有目标跟踪器，表5移除生成解码器、时间标记或两者。
- **Benchmark** · LaSOT、DepthTrack、LasHeR、VisEvent、TNL2K 等跨模态测试，报告 AUC 或 F-score。
- **关键结果 / 消融** · 表5去掉生成解码器平均降低1.50，去掉时间标记降低0.44，两者同时移除降低2.36。
- **适用条件 / 局限** · 依赖训练序列能代表目标变化，未来预测目标对于长期遮挡及重新出现仍需单测。

**可复用机制** · 跟踪模型除跨帧传递状态外，训练时可加入预测未来的生成监督，并与仅时间位置标记比较。

<a id="paper-orienpose"></a>

## OrienPose: Orientation-Guided Novel View Synthesis for Single-Image Unseen Object Pose Estimation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_OrienPose_Orientation-Guided_Novel_View_Synthesis_for_Single-Image_Unseen_Object_Pose_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_OrienPose_Orientation-Guided_Novel_View_Synthesis_for_Single-Image_Unseen_Object_Pose_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 仅靠像素相似度驱动新视角合成时，起始朝向不明确，容易得到外观近似但几何有误的模板。
- **核心创新 / 方法** · 将参考图估计朝向写入潜变量，并以朝向一致性损失约束合成结果；引导和监督采用同一估计坐标域。
- **Baseline** · 与原文表1–2中单参考图无 CAD 位姿估计方案对照，另消融朝向引导和一致性损失。
- **Benchmark** · 在 ShapeNet 的10个类别及真实 NAVI 的5个未见实例测位姿；表3另检验图像退化。
- **关键结果 / 消融** · 表1–2报告多个类别与真实实例上位姿指标改善，并通过去除朝向相关设计对比验证。
- **适用条件 / 局限** · 依赖参考图朝向可估，旋转对称物体和参考图严重遮挡时可能出现多解。

**可复用机制** · 在合成位姿匹配模板时，为相对视角变换增加同一坐标域里的几何监督。

<a id="paper-entropy-based-gaussianity"></a>

## What Is It Like to Be a Noise? An Entropy-based Gaussian Noise Regularization for Diffusion Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Chang_What_Is_It_Like_to_Be_a_Noise_An_Entropy-based_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Chang_What_Is_It_Like_to_Be_a_Noise_An_Entropy-based_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 优化生成奖励可能把输入噪声推离典型高斯实现，产生伪影或奖励投机。
- **核心创新 / 方法** · 把单个噪声张量转换为局部经验分布，用成对马尔可夫随机场近似与高斯先验的 KL，并结合边际、空间邻域和多尺度约束。
- **Baseline** · 比较无正则、点似然风格正则和原文表1–2列出的潜变量优化对照。
- **Benchmark** · SDXL-Turbo 的动物提示美学生成和亮度最小化，比较目标值、视觉输出及每步计算时间，另检验其他扩散模型。
- **关键结果 / 消融** · 表2展示引入高斯性约束时可在获取奖励的同时保留图像内容；表1量化额外耗时。
- **适用条件 / 局限** · 核密度熵计算较贵，成对局部近似不能排除全部长程相关。

**可复用机制** · 推理时优化扩散初始噪声，用局部熵与跨尺度相关性约束代替只约束噪声范数。

<a id="paper-physvid"></a>

## PhysVid: Physics Aware Local Conditioning for Generative Video Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Pathak_PhysVid_Physics_Aware_Local_Conditioning_for_Generative_Video_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Pathak_PhysVid_Physics_Aware_Local_Conditioning_for_Generative_Video_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 整段提示缺乏局部因果时序，逐帧额外条件又难以覆盖通用物理事件。
- **核心创新 / 方法** · 对连续帧块标注物理状态和约束，用分块交叉注意力与全局提示联合训练；推理可用同一时间定位的负提示。
- **Baseline** · 与 Wan-14B、WISA、VideoREPA、PhyT2V 等比较，并消融局部条件与负提示。
- **Benchmark** · VideoPhy 和 VideoPhy2 文本生成视频，测语义对齐 SA 和物理常识 PC。
- **关键结果 / 消融** · 表1相对 Wan-14B 的 PC 在 VideoPhy 提升约33%，在 VideoPhy2 提升约8%；表3检验各条件组件。
- **适用条件 / 局限** · 文字描述的物理约束是软条件，评测分数不能保证可量测的动力学守恒。

**可复用机制** · 视频中物理约束随时间变化时，将状态和相互作用描述分段注入注意力。

<a id="paper-motion-turing-test"></a>

## Towards Motion Turing Test: Evaluating Human-Likeness in Humanoid Robots

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Towards_Motion_Turing_Test_Evaluating_Human-Likeness_in_Humanoid_Robots_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Towards_Motion_Turing_Test_Evaluating_Human-Likeness_in_Humanoid_Robots_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 外观会干扰对运动自然度的判断，平均得分也会掩盖跑跳等类别的偏差。
- **核心创新 / 方法** · 将真人及机器人动作统一成 SMPL-X 表示，再用盲评人类相似度比较各动作和自动评分方法。
- **Baseline** · 对照真实人体动作；自动打分对比运动数据基线与多模态大模型。
- **Benchmark** · HHMotion 包含1000段、15类动作、11种人形机器人和10名真人，30名评审按0至5评分，以人评分为自动评估参考。
- **关键结果 / 消融** · 表2显示跑、跳、拳击等动态动作的人机差异明显；表3显示所测通用多模态模型落后于任务基线。
- **适用条件 / 局限** · 动作自然度是主观量，标准化骨架还会消除形态因素；结论依赖所测动作和机器人。

**可复用机制** · 检验人形运动自然度时统一骨架去除外观，按动态动作类别分层，并用人评核对自动评分器。

<a id="paper-crosshoi"></a>

## CrossHOI: Learning Cross-View Representations for Monocular 3D Human-Object Interaction Reconstruction

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Geng_CrossHOI_Learning_Cross-View_Representations_for_Monocular_3D_Human-Object_Interaction_Reconstruction_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Geng_CrossHOI_Learning_Cross-View_Representations_for_Monocular_3D_Human-Object_Interaction_Reconstruction_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 人和物体相互遮挡时，一个真实视角缺少用于接触定位的证据。
- **核心创新 / 方法** · 学习从输入图生成新视角特征，先融合空间特征得到初始网格，再对双视角顶点特征做双向注意力并以接触图细化。
- **Baseline** · 对照 METRO、Graphormer 改造版与原文表1中的人-物重建方法；表2–3比较顶点和图像特征融合。
- **Benchmark** · BEHAVE 和 InterCap，指标为人和物体 Chamfer 距离，及接触精确率与召回率。
- **关键结果 / 消融** · 表1报告两个数据集的重建与接触指标改善，严重遮挡切分的改进突出。
- **适用条件 / 局限** · 补充视角来自预测，其几何线索受训练分布制约，不能补回真正不可辨识的接触信息。

**可复用机制** · 单目接触估计受遮挡时，生成补充视角的特征并在网格顶点层融合。

<a id="paper-decoupled-diffusion-transformer"></a>

## DDT: Decoupled Diffusion Transformer

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_DDT_Decoupled_Diffusion_Transformer_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_DDT_Decoupled_Diffusion_Transformer_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 每步同时提取低频语义与恢复细节，可能产生优化目标冲突且重复提取条件。
- **核心创新 / 方法** · 独立条件编码器和速度解码器，并用统计动态规划选择相邻步共享自条件的方案。
- **Baseline** · 对比 DiT 等类别条件生成模型；原文表2改变编码与解码容量，另检验共享步数。
- **Benchmark** · ImageNet 256×256 与512×512 类别条件图像生成，比较 FID、训练收敛及推理共享。
- **关键结果 / 消融** · DDT-XL/2 报告 FID 1.31 与1.28；256分辨率作者报告收敛约快4倍，编码器增容实验支持容量取舍。
- **适用条件 / 局限** · 推理收益取决于相邻步骤条件变化幅度；图像类别条件结果尚不能外推到所有生成任务。

**可复用机制** · 扩散 Transformer 中将语义编码与速度解码拆开，缓存相邻去噪步可复用的语义条件。

<a id="paper-dit360"></a>

## DiT360: High-Fidelity Panoramic Image Generation via Hybrid Training

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Feng_DiT360_High-Fidelity_Panoramic_Image_Generation_via_Hybrid_Training_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Feng_DiT360_High-Fidelity_Panoramic_Image_Generation_via_Hybrid_Training_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 等距柱状全景存在首尾接缝和极区失真，而清晰全景数据较少。
- **核心创新 / 方法** · 联合透视和全景数据训练 DiT，在潜空间使用环形填充、偏航约束和立方体投影损失，分别约束接缝、旋转及失真。
- **Baseline** · 对比表1中的全景生成方案，表2逐项消融透视参考和全景几何设计。
- **Benchmark** · 文本生成全景、补绘和外绘；报告 FID、极区与赤道分区 FID、FAED、CLIP 分数等。
- **关键结果 / 消融** · 表1显示多项保真与边界相关指标提升，表2检验周期与几何监督作用。
- **适用条件 / 局限** · 移植时需明确周期轴和有效的投影变换，对普通平面图像不具备同样的几何假设。

**可复用机制** · 数据稀缺的周期视觉生成中，将边界周期先验与几何变换一致性同时纳入训练。

<a id="paper-ants-ood-negative-labels"></a>

## ANTS: Adaptive Negative Textual Space Shaping for OOD Detection via Test-Time MLLM Understanding and Reasoning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhu_ANTS_Adaptive_Negative_Textual_Space_Shaping_for_OOD_Detection_via_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhu_ANTS_Adaptive_Negative_Textual_Space_Shaping_for_OOD_Detection_via_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 固定负标签缺少实际远域图像的描述，也很难覆盖与已知类外观相似的近域样本。
- **核心创新 / 方法** · 从历史测试缓存中生成疑似远域的文本描述，同时针对频现且相似的已知类生成近域负标签，按样本动态结合两种分数。
- **Baseline** · 比较 NegLabel 与关闭远域挖掘、相似已知类挖掘或自适应打分的版本。
- **Benchmark** · 以 ImageNet-1K 等作为已知类，同时评估近域、远域分布外检测，报告 FPR95 等。
- **关键结果 / 消融** · 表 4 完整方法近域、远域 FPR95 分别为 60.98、15.38，NegLabel 为 68.18、27.34。
- **适用条件 / 局限** · 依赖历史批次代表部署分布；缓存被已知类或错误描述污染时应复查误报与拒绝率。

**可复用机制** · 开放集检测应分开构造近域难负标签和远域描述，分别验收误报。见表 4。

<a id="paper-httm-vggt-headwise-merging"></a>

## HTTM: Head-wise Temporal Token Merging for Faster VGGT

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_HTTM_Head-wise_Temporal_Token_Merging_for_Faster_VGGT_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_HTTM_Head-wise_Temporal_Token_Merging_for_Faster_VGGT_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 跨所有视图密集注意力随帧数迅速变贵；跨头一致合并容易让输出位置变得重复。
- **核心创新 / 方法** · 分别按注意力头匹配并合并时空令牌，保留离群查询，再拼接各头的结果。
- **Baseline** · 对照 FlashAttention VGGT、FastVGGT 和固定合并后长度下不同的离群过滤比。
- **Benchmark** · 在视频三维重建评估 Chamfer 准确度与完整度；另测 100–1,000 帧时延，离群消融使用 NRGBD。
- **关键结果 / 消融** · 表 2 的 1,000 帧从 724.6 秒降到 102.8 秒，FastVGGT 为 175.2 秒。表 4 等令牌长度下，移除离群过滤的准确度距离为 0.240，保留过滤为 0.012–0.013。
- **适用条件 / 局限** · 依赖注意力头的局部时空冗余；输入视角稀疏、快速运动或纹理弱时需要重新校验合并率。

**可复用机制** · 多视角注意力合并应允许各头保留不同信息，并在相同令牌长度对照离群信息的保留。见表 2–4。

<a id="paper-sencache"></a>

## SenCache: Accelerating Diffusion Model Inference via Sensitivity-Aware Caching

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Haghighi_SenCache_Accelerating_Diffusion_Model_Inference_via_Sensitivity-Aware_Caching_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Haghighi_SenCache_Accelerating_Diffusion_Model_Inference_via_Sensitivity-Aware_Caching_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 去噪刷新周期可能跨过对输入变化敏感的时刻，固定间隔复用会造成质量波动。
- **核心创新 / 方法** · 用有限差分校准输出对噪声潜变量及时间变化的敏感度，据估计误差做逐样本缓存决策。
- **Baseline** · 比较 TeaCache、MagCache，在相同函数评估次数优先比较速度质量折中。
- **Benchmark** · VBench 提示生成，覆盖 Wan 2.1、CogVideoX、LTX-Video；报告调用次数、缓存比、LPIPS、PSNR 和 SSIM。
- **关键结果 / 消融** · 表 1 Wan 2.1 的 21 次调用下，SenCache 的 LPIPS 为 0.0540，MagCache 为 0.0603；25 次调用的两者几乎持平。
- **适用条件 / 局限** · 需要代表性视频校准敏感度，函数调用数并非实际延迟，高动态、不同采样器或不同分辨率应复测。

**可复用机制** · 扩散缓存何时刷新可按去噪器对当前输入的敏感度预估误差，并固定实际函数调用数评估。见表 1。

<a id="paper-pai-bench-physical-grounding"></a>

## PAI-Bench: A Comprehensive Benchmark For Physical AI

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhou_PAI-Bench_A_Comprehensive_Benchmark_For_Physical_AI_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhou_PAI-Bench_A_Comprehensive_Benchmark_For_Physical_AI_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 视觉质量高不保证事件动态合理，模型增加文字推理也可能不改善具身判断。
- **核心创新 / 方法** · 按生成、条件生成和理解设立真实场景及任务指标，并拆分单/多控制输入和思考开关。
- **Baseline** · 对照多种专有及开放视频生成器和多模态模型，比较相同骨干开启与关闭思考。
- **Benchmark** · PAI-Bench 共 2,808 个案例。条件生成测对应控制的保真；理解部分区分常识与具身推理。
- **关键结果 / 消融** · 表 6 Qwen3-VL-8B 开启思考后总体从 56.8 到 57.3，具身推理由 58.7 到 57.7；32B 的具身推理由 61.1 到 58.4。
- **适用条件 / 局限** · 结论限所测评估及思考模式，离线视频评测不能替代交互控制验证；自动评分也需人工校准。

**可复用机制** · 物理视频及具身推理验收应分别看视觉逼真、物理约束和预测，把启用思考与不用思考拆开。见表 3–6。

<a id="paper-bolt-spectral-transfer"></a>

## Basis-Oriented Low-rank Transfer for Few-Shot and Test-Time Adaptation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Park_Basis-Oriented_Low-rank_Transfer_for_Few-Shot_and_Test-Time_Adaptation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Park_Basis-Oriented_Low-rank_Transfer_for_Few-Shot_and_Test-Time_Adaptation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 权重插值会混合不同源任务更新，少样本下重新学习整个低秩方向也可能不稳。
- **核心创新 / 方法** · 逐层从多个任务向量抽主要奇异方向并正交化，冻结形成的谱基，仅学习新任务的对角系数。
- **Baseline** · 比较零样本 CLIP、线性探针、LoRA、TIP、LP++ 和 aTLAS。
- **Benchmark** · 在通用及遥感分类集合做 1–16 shot，三种 CLIP 骨干上报告平均准确率，另测测试时适配。
- **关键结果 / 消融** · 表 1 通用 1-shot 为 71.30%，aTLAS 为 66.34%；遥感 1-shot 为 80.77%，LoRA 为 70.12%。
- **适用条件 / 局限** · 要求源权重可构成可对齐的任务向量，若目标更新不在源任务方向张成的空间内，仅调系数可能欠拟合。

**可复用机制** · 多个同源已微调模型用于新任务时，可重用更新方向而保留独立的可学习尺度，比较直接合并与从头学习低秩方向。见表 1。

<a id="paper-spatialstack-geometry-layer-injection"></a>

## SpatialStack: Layered Geometry-Language Fusion for 3D VLM Spatial Reasoning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_SpatialStack_Layered_Geometry-Language_Fusion_for_3D_VLM_Spatial_Reasoning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_SpatialStack_Layered_Geometry-Language_Fusion_for_3D_VLM_Spatial_Reasoning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 只用末层几何可能漏掉局部结构，把多层几何信号平铺拼接也可能干扰语言推理。
- **核心创新 / 方法** · 从 VGGT 不同深度提取几何，按尺度对齐，作为残差依次注入语言模型的浅层解码块。
- **Baseline** · 同微调 Qwen3.5、单层几何视觉融合及多层几何视觉融合对照。
- **Benchmark** · VSI-Bench、SPAR-Bench、BLINK-Spatial、CV-Bench，报告各基准得分和跨任务均值。
- **关键结果 / 消融** · 表 2 SpatialStack 平均 69.14，视觉端多层融合为 67.99；BLINK-Spatial 52.12 仍低于基础微调模型的 56.10。
- **适用条件 / 局限** · 依赖外部几何编码和各层对齐；不适用于所有空间任务，图像重叠不足及新骨干影响需再测。

**可复用机制** · 接入多层三维几何时，比较在视觉端一次融合与逐层接入语言解码器，见表 1–2。

<a id="paper-hint2gen"></a>

## Hint2Gen: Bridging Understanding and Generation via Code-structured Hints

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Tu_Hint2Gen_Bridging_Understanding_and_Generation_via_Code-structured_Hints_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Tu_Hint2Gen_Bridging_Understanding_and_Generation_via_Code-structured_Hints_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 模型可能知道解法却无法把路线或组合规则直接体现在生成画面里。
- **核心创新 / 方法** · 以 SVG 或 HTML 叠图编码推理结果，并以叠图作为 FLUX.1 Kontext 的条件。
- **Baseline** · 表2对照移除提示、换文字推理及不同提示生成与评估模型。
- **Benchmark** · Reason2Gen 含3300样本、22类任务，表1–2按路径、组装等能力报告准确率。
- **关键结果 / 消融** · 表2移除提示的平均准确率6.93，只提供文字推理10.94，使用结构化提示的多组配置约30至31。
- **适用条件 / 局限** · 依赖约束能编码在图像平面，评分会受所用评估模型影响。

**可复用机制** · 把图像推理结果编码成与画面坐标对齐的结构化提示，比只传递文字更容易保留空间约束。

<a id="paper-goldilocks-verification-audit"></a>

## Goldilocks Test Sets for Face Verification

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_Goldilocks_Test_Sets_for_Face_Verification_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wu_Goldilocks_Test_Sets_for_Face_Verification_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 常见人脸核验测试趋于饱和，简单劣化图像不能诊断身份判别混淆。
- **核心创新 / 方法** · 按外观变化和难度组织配对，并控制样本重复以及不同组参与频次。
- **Baseline** · 用同一 ResNet100 骨干比较既有测试集与 Hadrian、Eclipse、ND-Twins，并做域因素消融。
- **Benchmark** · 表1–3采用十折核验设置，报告不同受控数据集的准确率。
- **关键结果 / 消融** · 正文表2显示受控高质量难例仍能分开在常见测试集已饱和的方法。
- **适用条件 / 局限** · 配对采样改变了总体构成，困难集结果不能代替部署人群上的误识率验证。

**可复用机制** · 防御性核验用受控难例区分身份判别与外观相似性，并限制少数样本反复影响分数。

<a id="paper-lrdun"></a>

## LRDUN: A Low-Rank Deep Unfolding Network for Efficient Spectral Compressive Imaging

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_LRDUN_A_Low-Rank_Deep_Unfolding_Network_for_Efficient_Spectral_Compressive_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_LRDUN_A_Low-Rank_Deep_Unfolding_Network_for_Efficient_Spectral_Compressive_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 二维压缩测量直接还原整个高维光谱立方体既昂贵又欠定。
- **核心创新 / 方法** · 显式分解光谱基和子空间图像，展开近端梯度联合更新，并将物理秩与先验通道数解耦。
- **Baseline** · 表2对照完整立方体展开、核范数、截断 SVD 和其他低秩嵌入。
- **Benchmark** · 正文表1–2在仿真场景比较 PSNR、SSIM、参数和 FLOPs，另展示实拍光谱复原。
- **关键结果 / 消融** · 表2 LRDUN 的39.44 dB、10.26 GFLOPs 对应完整立方体基线的38.16 dB、26.95 GFLOPs。
- **适用条件 / 局限** · 物体光谱需可由低秩子空间近似，迁移需可区分测量模型和先验表示。

**可复用机制** · 将物理重建的秩约束和学习先验的特征宽度分开设定，避免低秩物理模型限制网络容量。

<a id="paper-gsi-spatial-transfer"></a>

## Exploring Spatial Intelligence from a Generative Perspective

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhu_Exploring_Spatial_Intelligence_from_a_Generative_Perspective_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhu_Exploring_Spatial_Intelligence_from_a_Generative_Perspective_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 只看图像生成拟合或综合空间分数，会遗漏生成训练对不同理解能力的作用。
- **核心创新 / 方法** · 用三维约束明确的空间编辑任务微调统一模型，再分别验收空间编辑和空间理解。
- **Baseline** · 以原 BAGEL 为主对照，另比较已有视觉语言模型。
- **Benchmark** · GSI-Real、GSI-Syn、OmniSpatial、SAT-Real，分别以生成约束遵循和理解准确率衡量。
- **关键结果 / 消融** · 表3中 BAGEL 加 GSI-Syn 后 OmniSpatial 总分41.55至42.07，空间交互45.67至47.67，逻辑32.14降至28.97。
- **适用条件 / 局限** · 收益依赖编辑数据与下游技能的匹配，目前不能概括所有空间推理。

**可复用机制** · 空间生成监督能迁移到部分理解任务，但可能损伤逻辑，选数据时应按空间能力分项比较。

<a id="paper-driving-adaptation-forgetting"></a>

## The Blind Spot of Adaptation: Quantifying and Mitigating Forgetting in Fine-tuned Driving Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Mao_The_Blind_Spot_of_Adaptation_Quantifying_and_Mitigating_Forgetting_in_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Mao_The_Blind_Spot_of_Adaptation_Quantifying_and_Mitigating_Forgetting_in_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 领域微调可能提高驾驶数据分数，却削弱基础模型原有的长尾知识。
- **核心创新 / 方法** · 以场景线索路由知识专家，在提示空间做适配，同时保留基础参数。
- **Baseline** · 正文表3–5对照未微调基础模型、LoRA 前后和不同适配策略。
- **Benchmark** · 驾驶视觉问答及针对遗忘构建的场景评测，分别估计专项表现和知识保留。
- **关键结果 / 消融** · 表4直接量化 LoRA 前后的得失，表5报告提示适配的保留与适配权衡。
- **适用条件 / 局限** · 专家覆盖与路由质量依赖交通数据分布，问答结果不能直接代表真实驾驶安全。

**可复用机制** · 驾驶适配应在同一评测上同时记录专项增益和通用知识遗忘，并比较改权重与运行时路由。

<a id="paper-av-deepfake-representation-audit"></a>

## Investigating Self-Supervised Representations for Audio-Visual Deepfake Detection

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Boldisor_Investigating_Self-Supervised_Representations_for_Audio-Visual_Deepfake_Detection_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Boldisor_Investigating_Self-Supervised_Representations_for_Audio-Visual_Deepfake_Detection_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 不同检测流水线的探针和训练数据不同，难判别收益来自表征还是分类器。
- **核心创新 / 方法** · 使用统一线性探针比较不同模态的自监督表示，并报告域外结果与组合收益。
- **Baseline** · 表2–4比较 Wav2Vec2、BRAVEn、AV-HuBERT 及已有防御检测方法。
- **Benchmark** · AV1M、FAVC、AVLips、DFE-2024 等，表2–3按域报告 AUC。
- **关键结果 / 消融** · 表3的线性探针中，BRAVEn 四集平均91.1，AV-HuBERT 84.5；结果显著随训练域和测试域变化。
- **适用条件 / 局限** · 有些数据缺少完整音频变化，音频探针不适合单独概括多模态整体鲁棒性。

**可复用机制** · 防御检测先用相同线性探针比较冻结表示，并把同域和域外拆分，避免复杂检测头掩盖表征差距。

<a id="paper-clp-restore-segment-tradeoff"></a>

## CLP: A Real-World Dataset of Contaminated Lens Protectors for Robust Semantic Segmentation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Park_CLP_A_Real-World_Dataset_of_Contaminated_Lens_Protectors_for_Robust_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Park_CLP_A_Real-World_Dataset_of_Contaminated_Lens_Protectors_for_Robust_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 训练中常将真实污染简化为全局图像退化，复原也可能损失分割线索。
- **核心创新 / 方法** · 收集带语义标签和对齐清晰参考的真实污染图，比较直接分割与串接复原。
- **Baseline** · 同一 Mask2Former 单独运行，或接 NAFNet、DiffUIR、URIE 等。
- **Benchmark** · CLP 的水、泥、凝露及不同污染距离，表1–4分别衡量 mIoU 和复原质量。
- **关键结果 / 消融** · 表3 DiffUIR 在凝露 mIoU 从32.5升至34.9，但水从39.8降至37.9，泥从29.5降至29.2。
- **适用条件 / 局限** · 证据来自特定镜头保护片，复用时应按目标光学位置和污染类型重新分层。

**可复用机制** · 真实镜头污染下先分污染类型比较恢复后的分割与直接分割，避免只按恢复质量接入前处理。

<a id="paper-queryocc"></a>

## QueryOcc: Query-based Self-Supervision for 3D Semantic Occupancy

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Lilja_QueryOcc_Query-based_Self-Supervision_for_3D_Semantic_Occupancy_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Lilja_QueryOcc_Query-based_Self-Supervision_for_3D_Semantic_Occupancy_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 图像渲染一致性只间接约束三维结构，而累积激光点云后离散成栅格会牺牲监督精度与扩展性。
- **核心创新 / 方法** · 由相邻帧伪点云或原始激光数据采样独立时空查询，直接监督连续语义占据；用空间收缩压缩远处并保留近场细节。
- **Baseline** · 表1比较 SelfOcc、OccNeRF、GaussianFlowOcc 等；QueryOcc+ 同时使用多种监督与高分辨率输入。
- **Benchmark** · Occ3D-nuScenes 自监督占据测试，报告语义及占据 RayIoU、体素 IoU 与推理速度。
- **关键结果 / 消融** · 文中相对 GaussianFlowOcc 报告语义 RayIoU 提升26%、占据 RayIoU 提升25%，推理11.6 FPS。
- **适用条件 / 局限** · 伪点云质量取决于视觉基础模型，远处压缩影响细节；部分罕见类别仍落后。

**可复用机制** · 训练相机三维占据模型时，用跨帧独立四维查询监督连续占据，减少稠密体素和渲染依赖。

<a id="paper-structure-to-intensity-diffusion"></a>

## Structure-to-Intensity Diffusion for Adverse-Weather LiDAR Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Ni_Structure-to-Intensity_Diffusion_for_Adverse-Weather_LiDAR_Generation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Ni_Structure-to-Intensity_Diffusion_for_Adverse-Weather_LiDAR_Generation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 坏天气改变激光点云几何和反射强度的机制不同，直接联合去噪使二者相互干扰。
- **核心创新 / 方法** · 每个扩散步先去噪点云结构，再用估得结构条件化强度去噪；训练增加根据真实统计生成的退化样本。
- **Baseline** · 对比 WeatherGen，表3拆分其 MDP/SMG 与本文 SiD、RPWS，并测真实数据微调。
- **Benchmark** · STF 多种恶劣天气与 KITTI-360；分别衡量点云结构及反射强度相关分布。
- **关键结果 / 消融** · 表1–3报告相近复杂度下结构和强度总体更接近真实数据，并在 STF 雪景消融分解设计。
- **适用条件 / 局限** · 依赖结构对强度有方向性解释，天气仿真还依赖采集统计；新型号传感器需复核。

**可复用机制** · 当传感器强度取决于几何时，在每个去噪步先估结构，再让强度分支以该结构为条件。

<a id="paper-instap"></a>

## InstAP: Instance-Aware Vision-Language Pre-Train for Spatial-Temporal Understanding

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Kumar_InstAP_Instance-Aware_Vision-Language_Pre-Train_for_Spatial-Temporal_Understanding_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Kumar_InstAP_Instance-Aware_Vision-Language_Pre-Train_for_Spatial-Temporal_Understanding_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 只做全局对齐时，模型可凭场景理解完成检索，却不能可靠区分同场景个体。
- **核心创新 / 方法** · 联合全局图文与实例级对比目标，把实例文本同图像区域或视频时空区域显式对齐。
- **Baseline** · UMT-L 使用完全相同训练语料的全局描述版，以及把实例描述也当全局描述的版本。
- **Benchmark** · InstVL 图像、零样本图像和视频用实例与全局 T2V/V2T R@1；InstVL-1K 测 IoU@50/70/90；另测 MSR-VTT 和 DiDeMo。
- **关键结果 / 消融** · 表1显示同语料条件下实例级目标明显改善实例检索；表3检验定位而非只看全局分数。
- **适用条件 / 局限** · 依赖实例文本和定位数据质量，误指代会直接污染局部对比信号。

**可复用机制** · 需要实例指代或时空检索时，在全局图文对齐外用区域和文本提及做对比学习。

<a id="paper-av-reasoner"></a>

## AV-Reasoner: Improving and Benchmarking Clue-Grounded Audio-Visual Counting for MLLMs

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Lu_AV-Reasoner_Improving_and_Benchmarking_Clue-Grounded_Audio-Visual_Counting_for_MLLMs_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Lu_AV-Reasoner_Improving_and_Benchmarking_Clue-Grounded_Audio-Visual_Counting_for_MLLMs_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 端到端计数错了时，单一正确率不能判断是漏找事件、定位错误还是计数失败。
- **核心创新 / 方法** · 用带时段线索的视听问题组织整段输入和参考线索输入，并联合度量线索定位及计数；模型端另对照课程学习与 GRPO。
- **Baseline** · 比较 Gemini 2.5 Pro 等视听或视觉语言模型，以及训练策略变化。
- **Benchmark** · CG-AV-Counting 为497个长视频、1027个问题及5845条线索；报告精确匹配、差一容忍与定位-计数联合指标，另测外部基准。
- **关键结果 / 消融** · 模型训练提高多项计数指标，但正文报告在域外基准上语言空间推理的提升有限。
- **适用条件 / 局限** · 结论依赖计数及证据标注任务，不能推断语言推理对所有域外视频任务均无益。

**可复用机制** · 给长视频计数模型做诊断时分开测试线索定位和给定线索后的计数，并在外部数据验证语言推理收益。

<a id="paper-wadi"></a>

## WaDi: Weight Direction-aware Distillation for One-step Image Synthesis

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_WaDi_Weight_Direction-aware_Distillation_for_One-step_Image_Synthesis_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_WaDi_Weight_Direction-aware_Distillation_for_One-step_Image_Synthesis_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 一步学生需要重构去噪行为，全参训练昂贵，常规低秩增量未利用教师与学生之间的变化结构。
- **核心创新 / 方法** · 对比 U-Net 和 DiT 教师学生的权重方向及范数变化，以低秩旋转 LoRaD 参数化方向，再与变分分数蒸馏联用。
- **Baseline** · 表1比较既有一步蒸馏；表2固定 SD1.5 和 VSD 比较适配器类型，表3改变秩。
- **Benchmark** · COCO 2014/2017 零样本文本生图，比较 FID、参数量以及权重方向和范数变化。
- **关键结果 / 消融** · 作者报告蒸馏后方向变化超过范数变化；WaDi 约用全参 U-Net/DiT 的10%可训练参数，表2检验参数化收益。
- **适用条件 / 局限** · 低秩方向偏好在所测扩散师生配置得到支持，跨架构和不同目标的蒸馏需重测。

**可复用机制** · 从多步扩散蒸馏到一步时，根据教师到学生的权重变化选择低秩旋转适配器。

<a id="paper-viaformer"></a>

## VIAFormer: Voxel-Image Alignment Transformer for High-Fidelity Voxel Refinement

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Fang_VIAFormer_Voxel-Image_Alignment_Transformer_for_High-Fidelity_Voxel_Refinement_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Fang_VIAFormer_Voxel-Image_Alignment_Transformer_for_High-Fidelity_Voxel_Refinement_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 从噪声重新生成会浪费粗体素中的正确结构，而图像 token 没有直接的三维定位。
- **核心创新 / 方法** · 把相机标定对应关系编码成图像索引，用混合流 Transformer 融合体素与视图信息，学习从有损体素到干净体素的修正流。
- **Baseline** · 表1–2比较视觉基础模型产出的粗体素、已有重建与体素修复方案，并分别测真实伪影和合成损坏。
- **Benchmark** · Toys4k、Dora；衡量体积 IoU、表面 Chamfer 距离，并记录生成开销。
- **关键结果 / 消融** · 表1–2显示两类损坏下修正后整体指标改善；正文给出10步求解约14.5秒的配置。
- **适用条件 / 局限** · 需要校准图像并依赖粗形状输入含有有用结构；迭代成本及域外形状需另估。

**可复用机制** · 修复已有粗三维表示时，使生成轨迹从受损潜变量直接走向干净目标，并显式对齐校准图像。

<a id="paper-mv-tap"></a>

## MV-TAP: Tracking Any Point in Multi-View Videos

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Koo_MV-TAP_Tracking_Any_Point_in_Multi-View_Videos_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Koo_MV-TAP_Tracking_Any_Point_in_Multi-View_Videos_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 逐路独立追踪无法用其他相机补偿遮挡，两视角对应错误也会累积到后续帧。
- **核心创新 / 方法** · 依据相机几何从当前轨迹构建跨视图信息交换，再结合时序特征迭代更新二维轨迹和遮挡状态。
- **Baseline** · 对照 CoTracker2/3 的单视角或多视角扩展，并比较所测多视角方案。
- **Benchmark** · Studio、Kubric、Harmony4D 等多视角序列，测跟踪精度、AJ 和遮挡相关指标。
- **关键结果 / 消融** · 原文定量结果与样例显示动态遮挡和困难视角下联合追踪提升，跨视图信息消融检验其贡献。
- **适用条件 / 局限** · 依赖同步及相机几何质量，所有视角都不可见时仍缺少观察证据。

**可复用机制** · 多相机追踪遇到遮挡时，将相机几何作为跨视角注意力的约束，联合更新轨迹和可见性。

<a id="paper-mhopreg"></a>

## MHopReg: Efficient Hierarchical Multi-Hop Graph Search for Point Cloud Registration

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_MHopReg_Efficient_Hierarchical_Multi-Hop_Graph_Search_for_Point_Cloud_Registration_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wu_MHopReg_Efficient_Hierarchical_Multi-Hop_Graph_Search_for_Point_Cloud_Registration_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 低重叠时正确匹配稀疏且分散，单次全局挑选容易遗漏，密集场景穷举又昂贵。
- **核心创新 / 方法** · 在变换不变的对应兼容图上均衡取各簇种子，再从粗到细多跳扩张，按一致性与空间覆盖给变换打分。
- **Baseline** · 比较 SC2-PCR、PointDSC 等，并消融采样、扩张和排序。
- **Benchmark** · 3DMatch、3DLoMatch、KITTI，报告配准召回和误差；KITTI 另看 500–20,000 个对应的处理耗时。
- **关键结果 / 消融** · 图 5 在 500 对应时召回 97.82%，SC2-PCR为 54.05%，PointDSC 为 97.47%；20,000 对应时 99.82% 且耗时 0.24 秒。
- **适用条件 / 局限** · 依赖初始匹配质量与兼容图，重叠趋零或重复几何会使多跳传播误匹配。

**可复用机制** · 低重叠点云存在分散内点时，比较簇平衡种子及分层多跳扩张和穷举全局搜索。见图 5、表 4。

<a id="paper-ppisp-photometric-reconstruction"></a>

## PPISP: Physically-Plausible Compensation and Control of Photometric Variations in Radiance Field Reconstruction

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Deutsch_PPISP_Physically-Plausible_Compensation_and_Control_of_Photometric_Variations_in_Radiance_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Deutsch_PPISP_Physically-Plausible_Compensation_and_Control_of_Photometric_Variations_in_Radiance_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 跨视角曝光、白平衡及暗角变化会被吸收到三维外观或几何中，干扰新视图。
- **核心创新 / 方法** · 将曝光、暗角、颜色及响应曲线拆成可解释的成像模块，并训练控制器预测新视角的拍摄参数。
- **Baseline** · 对照仿射或潜变量补偿方案、GLO、ADOP、BilaRF，以及有无控制器和各物理项。
- **Benchmark** · 在 Tanks and Temples 等新视图上测 PSNR、SSIM、LPIPS，补充有 EXIF 的数据。
- **关键结果 / 消融** · 表 2 完整新视图 PSNR 为 24.62 dB，去曝光为 23.33，去暗角为 24.08。
- **适用条件 / 局限** · 需要训练视图能支持光度变化估计；视角独有的非朗伯反射或自动处理突变不一定能由该模型解释。

**可复用机制** · 多视角重建宜把传感器固有偏差与拍摄条件变化分开估计，并在未知目标视图单独测试光度控制。见表 1–2。

<a id="paper-evatok-adaptive-video-token-budget"></a>

## EVATok: Adaptive Length Video Tokenization for Efficient Visual Autoregressive Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xiong_EVATok_Adaptive_Length_Video_Tokenization_for_Efficient_Visual_Autoregressive_Generation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xiong_EVATok_Adaptive_Length_Video_Tokenization_for_Efficient_Visual_Autoregressive_Generation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 固定每个时间块的词元量浪费在静态片段，在动态片段则可能不足。
- **核心创新 / 方法** · 离线求质量与成本折中的块级分配，再以轻量路由预测长度，让分词器适应可变长度。
- **Baseline** · 与 LARP、AdapTok、固定长度对照和不同解码器规模比较。
- **Benchmark** · WebVid/UCF 上评估重建，UCF-101 类条件生成和 Kinetics-600 帧预测比较词元量及生成质量。
- **关键结果 / 消融** · 表 3 重建平均从 1,024 词元降到约 774，UCF 类生成约 756；相对固定 1,024 分别减少 24.4%、26.2%。
- **适用条件 / 局限** · 路由误差可能压缩掉短时关键事件；平均长度下降不能直接换算成任何系统的延迟收益。

**可复用机制** · 视频生成可按时间块分配不同离散词元长度，再测等生成骨干下的质量与成本。见表 1–3。

<a id="paper-sentinel-language-action-history"></a>

## End-to-End Language-Action Model for Humanoid Whole Body Control

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_End-to-End_Language-Action_Model_for_Humanoid_Whole_Body_Control_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_End-to-End_Language-Action_Model_for_Humanoid_Whole_Body_Control_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 生成的人体动作在语义上相符，也未必满足机器人全身执行和稳定性约束。
- **核心创新 / 方法** · 用模拟跟踪人类动作生成语言与低层动作对，以流匹配从文字和本体状态生成分块动作，部署时增加残差修正。
- **Baseline** · 对照 MDM 加重定向、LangWBC；消融观测时窗、状态预测及完成预测。
- **Benchmark** · 文本命令全身控制的模拟测试，测 R@1、MMD 与物理成功率，并报告真机演示。
- **关键结果 / 消融** · 表 3 基础模型 R@1 为 0.582、成功 99.45；0.2 秒观测变为 0.153、99.50，说明只看执行成功会漏掉语义失效。
- **适用条件 / 局限** · 依赖模拟跟踪控制器和动作覆盖；真机演示不能保证未见动作、不同机器人或复杂接触稳定。

**可复用机制** · 语言驱动全身控制应把语义对齐与动作执行成功分开验收，并在固定骨干上对照本体观测时窗。见表 2–3。

<a id="paper-deblursdi-blind-self-diffusion"></a>

## Self-Diffusion Driven Blind Imaging

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_Self-Diffusion_Driven_Blind_Imaging_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yang_Self-Diffusion_Driven_Blind_Imaging_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 光学像差叠加运动模糊时，退化核未知，用单一预设退化训练的模型可能失效。
- **核心创新 / 方法** · 以单幅观测自监督，从噪声开始反向自扩散，迭代细化图像和模糊核，无需额外预训练。
- **Baseline** · 比较 Phase-Only、FFT-ReLU Deblur、SelfDeblur、FastDiffusionEM。
- **Benchmark** · Levin、Cho、Kohler 和 FFHQ 的光学像差去模糊以及运动模糊案例，报告 PSNR、SSIM。
- **关键结果 / 消融** · 表 4 Levin 上为 28.36 dB/0.8598，SelfDeblur 为 18.13 dB/0.4706。
- **适用条件 / 局限** · 图像和核联合恢复仍不唯一；仿真与光路变化、空间变化模糊以及逐图优化耗时须单独评估。

**可复用机制** · 未知成像退化下，可测试同一观测自扩散同时更新图像与核，作为预训练恢复先验的对照。见表 4。

<a id="paper-drfs-path-aware-editing"></a>

## Delta Rectified Flow Sampling for Text-to-Image Editing

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Beaudouin_Delta_Rectified_Flow_Sampling_for_Text-to-Image_Editing_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Beaudouin_Delta_Rectified_Flow_Sampling_for_Text-to-Image_Editing_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 以速度差直接蒸馏进行编辑时容易过度平滑，偏离目标路径，也可能改变背景。
- **核心创新 / 方法** · 用源与目标速度场差配合时变轨迹位移引导；正文给出关掉位移与选取线性位移时分别与 DDS 和 FlowEdit 的关系。
- **Baseline** · 比较 FlowEdit、iRFDS、RF-Solver 等，区分 SD3 和 SD3.5 骨干。
- **Benchmark** · PIE-Bench 上测结构距离、背景 PSNR/LPIPS/SSIM 和全图及编辑区 CLIP 相似度。
- **关键结果 / 消融** · 表 2 同 SD3.5 下 FlowEdit 的背景 PSNR 为 26.59、编辑区 CLIP 为 23.00；DRFS 分别为 26.97、23.17。
- **适用条件 / 局限** · 需要能计算来源和目标条件速度，位移强度要随骨干和编辑幅度校准；像素保真与语义变化并非同一指标。

**可复用机制** · 无需反演的流编辑可独立调整源目标轨迹位移，并分别检查保背景和改语义；见表 1–2。

<a id="paper-egoprox-transfer-diagnostic"></a>

## EgoProx: Evaluating MLLMs on Egocentric 3D Proximity Reasoning Across a Cognitive Hierarchy

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_EgoProx_Evaluating_MLLMs_on_Egocentric_3D_Proximity_Reasoning_Across_a_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_EgoProx_Evaluating_MLLMs_on_Egocentric_3D_Proximity_Reasoning_Across_a_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 总体第一视角问答分数会隐藏模型能判断自身附近对象，却不能正确推断动作链的情况。
- **核心创新 / 方法** · 将接近推理分成意图、探索、利用和动作链，按类别追加数据、交叉测量其余类别。
- **Baseline** · 比较未微调 Qwen2.5-VL-7B 和只在特定类别增强后的版本，同时测多种现有模型。
- **Benchmark** · EgoProx 的近似/相对距离、动作准确与动作链关系判断，另测跨数据集迁移。
- **关键结果 / 消融** · 表 3 加意图数据后，利用类别的近似分从 38.63 到 64.93，动作链长程关系却从 46.21 降到 14.29。
- **适用条件 / 局限** · 问答层级与控制表现仍有距离，交叉退化可能受指令样式或标注分布影响，应在真实行为和新视角上复核。

**可复用机制** · 具身空间推理微调须区分一阶接近判断和多步动作链，跨子任务对照迁移与遗忘。见表 3–4。

<a id="paper-idesplat-iterative-depth"></a>

## IDESplat: Iterative Depth Probability Estimation for Generalizable 3D Gaussian Splatting

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Long_IDESplat_Iterative_Depth_Probability_Estimation_for_Generalizable_3D_Gaussian_Splatting_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Long_IDESplat_Iterative_Depth_Probability_Estimation_for_Generalizable_3D_Gaussian_Splatting_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 单次极线对齐容易输出粗或不可靠的深度概率，三维高斯中心随之偏移。
- **核心创新 / 方法** · 级联跨视图 warping，把极线注意力置信作乘性积累，逐轮更新深度候选并映射到高斯中心。
- **Baseline** · 比较 DepthSplat、MVSplat、MonoSplat，另消融迭代深度、概率增强及高斯模块。
- **Benchmark** · RealEstate10K、ACID 和 DL3DV 的新视图合成测 PSNR、LPIPS、SSIM，另报告深度估计及效率。
- **关键结果 / 消融** · 表 5 在 RE10K 中完整版本 PSNR 为 27.56 dB；把概率增强加入已有迭代过程约提高 0.46 dB。
- **适用条件 / 局限** · 依赖跨视图场景一致和相机标定；大遮挡下多次置信乘积可能强化相关错误，需测随迭代和视图跨度的稳定性。

**可复用机制** · 前馈高斯重建遇到单次跨视图对齐不可靠时，比较迭代深度候选和多次匹配置信连乘。见表 5–6。

<a id="paper-lactok"></a>

## LacTokGen: Latent Consistency Tokenizer for 1024-pixel Image Generation by 256 Tokens

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xie_LacTokGen_Latent_Consistency_Tokenizer_for_1024-pixel_Image_Generation_by_256_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xie_LacTokGen_Latent_Consistency_Tokenizer_for_1024-pixel_Image_Generation_by_256_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 高分辨图像需要很多离散词元；直接采用扩散解码会带来颜色和亮度偏差。
- **核心创新 / 方法** · 量化编码接入预训练扩散潜空间，将多步解码器改为少步一致性解码并加入像素监督。
- **Baseline** · 表1–3比较 VQGAN 等词元器及 LacTok 变体，正文另做解码消融。
- **Benchmark** · ImageNet、MSCOCO-2017 和 MJHQ-5K 的重建实验，以及表4的文字生成图像实验。
- **关键结果 / 消融** · 正文报告1024×1024的输入可用256词元表示，较该 VQGAN 配置压缩16倍。
- **适用条件 / 局限** · 词元数减少不等于整体加速，仍须计入解码器计算及细节丢失。

**可复用机制** · 压低视觉词元数时可用一步或两步一致性解码器支持直接像素监督，检查保真是否受解码器瓶颈限制。

<a id="paper-forehoi"></a>

## ForeHOI: Feed-forward 3D Object Reconstruction from Daily Hand-Object Interaction Videos

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_ForeHOI_Feed-forward_3D_Object_Reconstruction_from_Daily_Hand-Object_Interaction_Videos_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_ForeHOI_Feed-forward_3D_Object_Reconstruction_from_Daily_Hand-Object_Interaction_Videos_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 手部遮挡和相机、物体耦合运动使单目互动视频中的三维物体不完整。
- **核心创新 / 方法** · 在同一前馈框架联合预测二维遮罩和三维形状，令二者共享补全证据。
- **Baseline** · 正文表2–3对照 EasyHOI、HOLD、HORT、MagicHOI 及主干与训练数据变化。
- **Benchmark** · HO3D 和 HOI 实拍数据，报告 Chamfer 距离、F@5、F@10及耗时。
- **关键结果 / 消融** · 表2在 HO3D 的 Chamfer 距离为0.79厘米，HOLD 为1.36；两数据集平均耗时为1.1分钟，HORT 为0.8分钟但仅列出 HOI 结果。
- **适用条件 / 局限** · 严重遮挡下补全仍受未见物体几何和真实手部遮挡覆盖限制。

**可复用机制** · 严重遮挡时可以让二维遮罩补全与三维形状补全交换信息，再与独立重建比较。

<a id="paper-mass-mask-guided-ssl"></a>

## Learning Generalizable 3D Medical Image Representations from Mask-Guided Self-Supervision

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Gao_Learning_Generalizable_3D_Medical_Image_Representations_from_Mask-Guided_Self-Supervision_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Gao_Learning_Generalizable_3D_Medical_Image_Representations_from_Mask-Guided_Self-Supervision_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 重建和对比预训练可能学习低层纹理，忽略三维区域和周围解剖关系。
- **核心创新 / 方法** · 以自动生成的无类别候选掩码定义上下文分割任务，学习外观、结构及位置关联。
- **Baseline** · 比较常见自监督预训练和从头训练，并消融掩码来源及骨干。
- **Benchmark** · 正文表1–4测不同规模下的分割 Dice、分类 AUC，以及自动掩码质量与单样本分割。
- **关键结果 / 消融** · 表4的 BCV 自动候选平均重叠 Dice 15.2，MASS 单样本上下文分割 Dice 65.5，说明不完美候选仍可用。
- **适用条件 / 局限** · 结构来自自动候选，少见或难分病变可能在预训练中缺少覆盖。

**可复用机制** · 用无需语义类别的区域掩码做上下文分割预训练，可测试不完美结构伪标签能否支持少样本迁移。

<a id="paper-freqwarm"></a>

## Toward Diffusible High-Dimensional Latent Spaces: A Frequency Perspective

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Lai_Toward_Diffusible_High-Dimensional_Latent_Spaces_A_Frequency_Perspective_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Lai_Toward_Diffusible_High-Dimensional_Latent_Spaces_A_Frequency_Perspective_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 高维自编码器可提高重建，生成模型仍可能在高频欠拟合。
- **核心创新 / 方法** · 受控扰动定位编码与解码的频率错配，在扩散或流匹配早期提高高频暴露，保持自编码器冻结。
- **Baseline** · 同一潜空间和生成器对比无热身，另比较不同频带划分和自编码器。
- **Benchmark** · ImageNet 256和512 等，正文表1–4报告生成 FID 等并切换引导。
- **关键结果 / 消融** · 表1报告 USiT-H 无分类器引导时，Wan2.2 的 gFID 改善14.11、LTX 改善6.13。
- **适用条件 / 局限** · 频率错配与编码器、数据和分辨率相关，边界频带需重新验证。

**可复用机制** · 潜空间越大未必越适合生成，先拆开测频带的编码覆盖和解码依赖，再以高频热身调整训练。

<a id="paper-soap-mim-artifacts"></a>

## Suppressing Non-Semantic Noise in Masked Image Modeling Representations

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Hjelkrem-Tan_Suppressing_Non-Semantic_Noise_in_Masked_Image_Modeling_Representations_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Hjelkrem-Tan_Suppressing_Non-Semantic_Noise_in_Masked_Image_Modeling_Representations_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 掩码图像建模的表示可能保留与语义无关的图块信息，影响零样本迁移。
- **核心创新 / 方法** · 用真实和合成非语义图像做 PCA 捕捉伪影分量，在推理中通过线性投影抑制。
- **Baseline** · 对照原特征、不同投影尺度及 RASA，在多个 MIM 骨干比较。
- **Benchmark** · 表2测 ECSSD、DUTS、DUT-OMRON 的零样本显著分割，表3–4用 ADE20K 与 ImageNet 的近邻评测。
- **关键结果 / 消融** · 正文报告多个 MIM 模型零样本分割改善，非 MIM 模型的结果取决于其原有表征。
- **适用条件 / 局限** · 无语义探针可能并未覆盖所有伪影，投影也可能移除任务需要的信息。

**可复用机制** · 用无语义输入估计表征中的伪影方向，并在冻结骨干上先做投影对照。

<a id="paper-core-object-token-merging"></a>

## CORE: Compact Object-centric REpresentations as a New Paradigm for Token Merging in LVLMs

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Lei_CORE_Compact_Object-centric_REpresentations_as_a_New_Paradigm_for_Token_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Lei_CORE_Compact_Object-centric_REpresentations_as_a_New_Paradigm_for_Token_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 固定格点或按相似度合并容易跨过对象边界，破坏实体提问所需信息。
- **核心创新 / 方法** · 轻量分割解码器生成对象掩码，以掩码聚合视觉 token，再按质心排序。
- **Baseline** · 比较 ToMe、FastV 等，以及同骨干全 token CORE 作为保留率参照。
- **Benchmark** · 六个 LVLM 基准，含 MME、MMBench-CN、ScienceQA-IMG；对比固定和自适应 token 预算、任务分数及计算量。
- **关键结果 / 消融** · 作者报告自适应极端设定保留2.2% token 时，仍达到自己全 token 基线97.4%的表现。
- **适用条件 / 局限** · 依赖对象掩码质量；文本、背景关系和掩码遗漏的小物体可能在压缩时丢失。

**可复用机制** · 压缩视觉 token 时按对象掩码合并，并用对象质心恢复合并后序列的空间顺序。

<a id="paper-frequency-prompt-multi-rater-segmentation"></a>

## Harmonized Feature Conditioning and Frequency-Prompt Personalization for Multi-Rater Medical Segmentation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Karimijafarbigloo_Harmonized_Feature_Conditioning_and_Frequency-Prompt_Personalization_for_Multi-Rater_Medical_Segmentation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Karimijafarbigloo_Harmonized_Feature_Conditioning_and_Frequency-Prompt_Personalization_for_Multi-Rater_Medical_Segmentation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 信号噪声和专家对边界的真实分歧可能被模型混为一谈。
- **核心创新 / 方法** · 以 Harmonizer 调制图像特征，给标注者加入高频提示，并用 GED 正则拟合标注分布。
- **Baseline** · 对照 PHiSeg、单标注者 U-Net 及表2–3的个性化分割方法。
- **Benchmark** · LIDC-IDRI 和 NPC-170；以多标注分布 GED 和分割 Dice 等评估。
- **关键结果 / 消融** · 表1–3显示模型在分布拟合及个体分割表现上改善，正文报告额外参数较少。
- **适用条件 / 局限** · 需要每例多标注或可追踪的标注者标签；高频提示只能表示模型已学到的样式差异。

**可复用机制** · 多标注者分割中降除扫描差异，同时显式用频域提示保存标注者的边界偏好。

<a id="paper-velox-4d-representation"></a>

## Velox: Learning Representations of 4D Geometry and Appearance

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Malik_Velox_Learning_Representations_of_4D_Geometry_and_Appearance_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Malik_Velox_Learning_Representations_of_4D_Geometry_and_Appearance_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 逐帧三维编码缺少统一动态表示，纯渲染监督也可能不足以定位几何。
- **核心创新 / 方法** · 编码非结构化时空彩色点云，用4D表面解码器和高斯解码器分别监督几何与外观。
- **Baseline** · 与逐帧或独立编码方案比较；视频生成比较 GVF 等相关基线。
- **Benchmark** · Objaverse 三维点追踪用 L2 和 APD；Consistent4D 与 Objaverse 视频到4D测输入视角和九个新视角；另测布料模拟。
- **关键结果 / 消融** · 原文表2–3报告共享动态表示可用于追踪和生成，输入视角重建优于所测生成基线。
- **适用条件 / 局限** · 点云覆盖和时间采样决定可编码的信息，验证以对象级动态为主。

**可复用机制** · 压缩动态物体点云时，用时变表面与可渲染外观两条监督共同训练一组 4D token。

<a id="paper-trm-vla"></a>

## TRM-VLA: Temporal-Aware Chain-of-Thought Reasoning and Memorization for Vision-Language-Action Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_TRM-VLA_Temporal-Aware_Chain-of-Thought_Reasoning_and_Memorization_for_Vision-Language-Action_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_TRM-VLA_Temporal-Aware_Chain-of-Thought_Reasoning_and_Memorization_for_Vision-Language-Action_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 每帧生成完整推理导致延迟，独立生成还会在长程任务中前后冲突。
- **核心创新 / 方法** · KTR 仅在关键决策帧生成分层显式计划，GCM 按所需粒度存取历史推理。
- **Baseline** · 基于 CogACT，对照 CogACT-Base、CogACT-ECoT 等；在模拟和实机任务中比较。
- **Benchmark** · LIBERO-90、SIMPLER 的 SimplerEnv-Bridge 与4项实机操作；报告成功率、进度和每步生成 token。
- **关键结果 / 消融** · 表1报告模拟任务平均成功率72.9%；表2–3显示长程成功和推理开销相较所测对照改善。
- **适用条件 / 局限** · 依赖关键帧判定和历史记录的正确性；任务环境变化时旧计划可能失效。

**可复用机制** · 机器人滚动决策时，仅在任务进展关键帧触发推理，并按粒度检索历史推理状态。

<a id="paper-sing-classifier-invariants"></a>

## Make it SING: Analyzing Semantic Invariants in Classifiers

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yadid_Make_it_SING_Analyzing_Semantic_Invariants_in_Classifiers_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yadid_Make_it_SING_Analyzing_Semantic_Invariants_in_Classifiers_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 两个样本可有相同读出却存在语义差异，常见显著性方法难指出哪些属性被读出忽略。
- **核心创新 / 方法** · 分析线性分类映射的零空间，将等效特征的差异交由视觉语言映射生成自然语言解释和视觉例子。
- **Baseline** · 在相同干预标准下对照 ResNet50、ResNeXt101 与 DinoViT 等骨干。
- **Benchmark** · 从单图到类和模型级做等输出语义分析；表1用标准化干预的语义变化角度对比。
- **关键结果 / 消融** · 表1所测 DinoViT 的语义变化最小，ResNet 系列部分相关属性变化落在读出忽略的空间。
- **适用条件 / 局限** · 线性读出假设及跨模型映射忠实度限制解释；等输出特征未必对应真实图像分布。

**可复用机制** · 审计分类器特征时，通过读出层零空间区分已表征的属性与最终分类采用的属性。

<a id="paper-prism-semantic-prototypes"></a>

## PRISM: Prototype-based Reasoning with Inter-modal Semantic Mining for Interpretable Image Recognition

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yu_PRISM_Prototype-based_Reasoning_with_Inter-modal_Semantic_Mining_for_Interpretable_Image_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yu_PRISM_Prototype-based_Reasoning_with_Inter-modal_Semantic_Mining_for_Interpretable_Image_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 纯视觉原型能定位局部证据，却容易缺少可解释概念或重复聚焦同一区域。
- **核心创新 / 方法** · 用信息论归因从描述获得相关区域，令原型激活对齐，并约束各原型空间集中及减少重叠。
- **Baseline** · 对照 ProtoPNet、TesNet、ProtoViT、Label-Free CBM 等。
- **Benchmark** · CUB-200-2011 等两个细粒度数据集，跨 CNN/ViT 骨干比较 top-1 与局部解释。
- **关键结果 / 消融** · 表1–3报告对比视觉原型和图文解释基线的性能，消融验证归因与空间约束的贡献。
- **适用条件 / 局限** · 描述覆盖和视觉语言归因质量影响原型语义；共现概念仍可能被误配。

**可复用机制** · 让细粒度分类的部件原型对齐文本相关区域，并用紧致性约束减少原型重复。

<a id="paper-kyvo-3d-token-alignment"></a>

## Aligning Text, Images and 3D Structure Token-by-Token

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Sahoo_Aligning_Text_Images_and_3D_Structure_Token-by-Token_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Sahoo_Aligning_Text_Images_and_3D_Structure_Token-by-Token_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 原始网格和位姿没有适于自回归模型的统一序列单位，离散过粗还会损失空间细节。
- **核心创新 / 方法** · 将对象几何及位姿编码成三维场景词元，与文本和图像共同自回归训练，并比较几何重建辅助项与量化粒度。
- **Baseline** · 表1比较带或去掉辅助重建的分词器，表2比较三维分词方案，表3比较位姿粒度。
- **Benchmark** · Objaverse、CLEVR 等四个三维数据集，覆盖渲染、识别、指令遵循和问答；分词实验用人工平均排名等指标。
- **关键结果 / 消融** · 表3中0.05是所测 CLEVR 上最优粒度；表1–2报告分词和重建监督影响人评。
- **适用条件 / 局限** · 最佳粒度取决于场景尺寸与布局，依赖结构化对象表示，开放世界未分割场景仍需验证。

**可复用机制** · 把结构化三维场景加入多模态语言模型时，分别选对象形状和位姿的离散粒度，并以重建辅助目标检验。

<a id="paper-event-structural-valley"></a>

## Event Structural Valley: A Unified Theoretical and Practical Framework for Event Camera Autofocus

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xiang_Event_Structural_Valley_A_Unified_Theoretical_and_Practical_Framework_for_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xiang_Event_Structural_Valley_A_Unified_Theoretical_and_Practical_Framework_for_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 运动和离焦共同影响事件率，用最大事件率对焦假设可能错过最清晰位置。
- **核心创新 / 方法** · 从事件触发推导事件率双峰一谷规律，使用平滑和一致性约束提取主峰之间的谷。
- **Baseline** · 原文表1–3对照已有事件相机自动对焦算法。
- **Benchmark** · SYN、DAVIS、EVK4 上不同光照与运动条件，以平均对焦时间戳误差（毫秒）评估。
- **关键结果 / 消融** · 表1–3报告所测合成和实拍环境误差改善，展示无需重建图像的事件对焦度量。
- **适用条件 / 局限** · 需要扫焦窗内观察到两侧结构；缺纹理、事件稀疏或场景迅速变化时峰谷可能难辨。

**可复用机制** · 事件相机扫描焦距时，找两峰之间的事件率谷，而非将事件率峰值当焦点。

<a id="paper-confidence-driven-visual-reasoning"></a>

## Linking Perception, Confidence and Accuracy in MLLMs

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Du_Linking_Perception_Confidence_and_Accuracy_in_MLLMs_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Du_Linking_Perception_Confidence_and_Accuracy_in_MLLMs_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 感知证据受损时多模态模型仍可能过度自信，固定次数复核浪费计算。
- **核心创新 / 方法** · 对原图和加噪图配对施加置信奖励；测试时用置信信号调度一致性、反思和视觉复核，由外部专家提供判断。
- **Baseline** · Qwen2.5-VL-7B 训练及免训练对照，表2分别消融置信训练和推理调度，表3替换专家。
- **Benchmark** · Math-Vision、MathVista 等四个视觉推理基准，比较开放问答和选择题准确率及测试时扩展。
- **关键结果 / 消融** · 作者报告整套方法跨四基准约8.8%的总体增益，表2显示单项与联合效果。
- **适用条件 / 局限** · 加噪样本未必覆盖真实感知失败；外部专家会带来额外成本、偏差和相关错误。

**可复用机制** · 多模态推理训练用清晰与扰动图像的配对置信奖励，推理时按置信度分配验证预算。

<a id="paper-bimotion-spline-motion"></a>

## BiMotion: B-spline Motion for Text-guided Dynamic 3D Character Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_BiMotion_B-spline_Motion_for_Text-guided_Dynamic_3D_Character_Generation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_BiMotion_B-spline_Motion_for_Text-guided_Dynamic_3D_Character_Generation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 固定帧数或逐帧离散化容易丢失长动作的中间状态和子动作。
- **核心创新 / 方法** · 对输入动作求 Laplacian 正则的连续 B 样条控制点，生成固定长度表示后可以恢复不同时长，并约束局部刚性。
- **Baseline** · 比较固定帧采样加线性插值，并消融控制点编码、对应损失、刚性损失和法线融合。
- **Benchmark** · BIMO 的变长三维角色动作，报告重建逐轨迹 L1，另评文本对齐和生成时间。
- **关键结果 / 消融** · 表 2 中带对应、刚性和法线的线性设置重建误差 2.674，完整样条版 1.078，均为 10⁻² 尺度。
- **适用条件 / 局限** · 固定控制点仍可能漏掉高度不连续事件；离线动画可表达性不能直接推出机器人动力学或接触可执行性。

**可复用机制** · 变长三维动作可用固定数量 B 样条控制点做生成表示，在同容量下单测连续时域重建。见图 5、表 2。

<a id="paper-ava-bench-atomic-abilities"></a>

## AVA-Bench: Atomic Visual Ability Benchmark for Vision Foundation Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Mai_AVA-Bench_Atomic_Visual_Ability_Benchmark_for_Vision_Foundation_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Mai_AVA-Bench_Atomic_Visual_Ability_Benchmark_for_Vision_Foundation_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 复合问答失败既可能来自视觉短板，也可能来自指令微调分布或定位难度，平均分不易诊断。
- **核心创新 / 方法** · 将感知拆成 14 项原子能力并对齐每项训练与测试，加入已知框的条件以排查定位对空间推理的影响。
- **Baseline** · 对照多个视觉基础模型，区分预训练是否对齐文字，并比较有无提供真框。
- **Benchmark** · AVA-Bench 测定位、空间、相对深度、OCR 等；定位按框大小分组并报 GIoU。
- **关键结果 / 消融** · 图 8 中提供框后所测视觉骨干在空间能力任务均取得满分，无框时 MiDaS 和 SAM 对定位的弱点变得明显。
- **适用条件 / 局限** · 原子任务分数不能覆盖多能力联合时的交互，选模应结合目标任务分布；提供框的诊断仅隔离部分视觉错误。

**可复用机制** · 选视觉骨干时可保持语言头和训练任务分布一致，拆测单项能力，并用给定框的对照定位复合任务瓶颈。见图 5–8。

<a id="paper-mactok-mask-alignment"></a>

## MacTok: Robust Continuous Tokenization for Image Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zeng_MacTok_Robust_Continuous_Tokenization_for_Image_Generation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zeng_MacTok_Robust_Continuous_Tokenization_for_Image_Generation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 较强 KL 正则和低令牌预算使编码器可能忽略输入，单看重建又难代表生成能力。
- **核心创新 / 方法** · 图像遮盖混合随机和 DINO 指导，配合全局与局部特征对齐训练一维连续分词器。
- **Baseline** · 对照仅随机遮盖、100% 语义遮盖、混合遮盖和不同模块消融。
- **Benchmark** · ImageNet 256 和 512 类条件生成，报告重建 FID、生成 FID、PSNR/SSIM 与令牌预算。
- **关键结果 / 消融** · 表 4 同最大遮盖率 0.7，随机 gFID 为 14.59，全语义为 14.84，半数语义混合为 13.95；混合的重建 FID 为 0.57，随机为 0.56。
- **适用条件 / 局限** · 依赖教师有用的区域语义及合适的遮盖比例；覆盖关键目标时，要独立检查重建与生成的质量取舍。

**可复用机制** · 极少连续图像词元容易后验坍塌，可混合随机与语义遮盖并同时验收重建与下游生成。见表 4–5。

<a id="paper-jrm-negative-support-reconstruction"></a>

## JRM: Joint Reconstruction Model for Multiple Objects without Alignment

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_JRM_Joint_Reconstruction_Model_for_Multiple_Objects_without_Alignment_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wu_JRM_Joint_Reconstruction_Model_for_Multiple_Objects_without_Alignment_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 重复观测有信息，但严格几何配准或错误的对象关联会把不相关几何传播到重建。
- **核心创新 / 方法** · 采用三维流匹配在潜空间隐式聚合未对齐的同类或同实例观测，并以错配组合监督模型何时忽略支持。
- **Baseline** · 比较单对象重建及显式配准相关方法，在固定模型内改变负配对比例。
- **Benchmark** · 合成重复和铰接对象及 Replica、ScanNet 场景；按同一、相似、不匹配对象报告 Chamfer、法向及 F1。
- **关键结果 / 消融** · 正文表 5 指出仅用正配对时对错误匹配敏感，负配对比例为 1 时模型忽略辅助对象，中间比例在聚合和抗错配间折中。
- **适用条件 / 局限** · 需要可构造代表性配对；大型变化或相似但结构关键不同的对象仍可能错误融合。

**可复用机制** · 跨观测联合重建的支持项可能匹配错误，训练时应混入一定比例错配组合，并单独测误匹配和正确匹配两类表现。见表 5。

<a id="paper-momo-validation-loss-checkpoint-alignment"></a>

## MOMO: Mars Orbital MOdel Foundation Model for Mars Orbital Applications

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Purohit_MOMO_Mars_Orbital_MOdel_Foundation_Model_for_Mars_Orbital_Applications_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Purohit_MOMO_Mars_Orbital_MOdel_Foundation_Model_for_Mars_Orbital_Applications_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 各传感器预训练进展速度不同，同时取末次检查点可能合并处于不同阶段的权重。
- **核心创新 / 方法** · 在同源模型上用验证损失选择收敛阶段接近的检查点，然后用任务算术合并。
- **Baseline** · 比较同一合并管线的 ES、LE 和 EVL，另测独立传感器及合并训练数据。
- **Benchmark** · Mars-Bench 九项下游任务，使用分类加权 F1 或分割 mIoU，另报告检查点选择波动。
- **关键结果 / 消融** · 表 2 Boulder 的 EVL 0.20 ± 0.005，LE 0.18 ± 0.031，ES 0.12 ± 0.078；Crater Binary 分别为 0.54、0.50、0.50。
- **适用条件 / 局限** · 验证损失须可跨传感器比较；损失尺度、标签定义或预训练目标不同则需先标定。具体证据来自火星多传感器。

**可复用机制** · 跨传感器权重合并可比较按验证损失匹配收敛阶段与直接用各自末次或早停检查点。见表 2。

<a id="paper-llada-v-attention-mask-tradeoff"></a>

## LLaDA-V: Large Language Diffusion Models with Visual Instruction Tuning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/You_LLaDA-V_Large_Language_Diffusion_Models_with_Visual_Instruction_Tuning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/You_LLaDA-V_Large_Language_Diffusion_Models_with_Visual_Instruction_Tuning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 文本扩散允许并行生成，但多模态问答的性能与延迟是否受益，以及何种对话掩码合适，需要对照。
- **核心创新 / 方法** · 将视觉编码通过 MLP 接入 LLaDA 做指令微调，并比较跨对话轮双向注意力与因果掩码。
- **Baseline** · 对照同指令数据下的 LLaMA3-V、自身两种掩码和已有纯扩散多模态模型。
- **Benchmark** · 十二项任务的掩码比较含 MMMU、MMMU-Pro 和 MuirBench；MathVerse 另比生成效率。
- **关键结果 / 消融** · 表 3 不计 MME 的平均值双向为 49.73、对话因果为 49.03，十二项中七项领先；RealworldQA 双向为 60.26、因果为 61.18。
- **适用条件 / 局限** · 双向处理要求当前可见上下文完整。扩散不能复用常规自回归 KV 缓存，并行多词生成仍可能有质量代价。

**可复用机制** · 多模态扩散语言模型先在同数据和骨干下消融对话因果掩码与双向注意力，再测有效并行增益。见表 3–4。

<a id="paper-c-genreg"></a>

## C-GenReg: Training-Free 3D Point Cloud Registration by Multi-View-Consistent Geometry-to-Image Generation with Probabilistic Modalities Fusion

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Haitman_C-GenReg_Training-Free_3D_Point_Cloud_Registration_by_Multi-View-Consistent_Geometry-to-Image_Generation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Haitman_C-GenReg_Training-Free_3D_Point_Cloud_Registration_by_Multi-View-Consistent_Geometry-to-Image_Generation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 弱重叠及跨传感器点云难以直接匹配，生成图像给补充证据也可能引入误差。
- **核心创新 / 方法** · 从点云生成一致多视图，经视觉模型找像素对应再映回三维，以独立几何支路的对应做概率融合。
- **Baseline** · 对照 FCGF、Predator、GeoTransformer 及拼接特征和不同后验融合方式。
- **Benchmark** · 3DMatch、ScanNet、Waymo，表1–4报告旋转和平移误差及阈值内比例。
- **关键结果 / 消融** · 表4对固定 MASt3R 与 GeoTransformer 的组合，三档旋转阈值的命中由拼接的79.4、83.4、86.1提高到 Noisy AND 的94.2、97.5、98.3。
- **适用条件 / 局限** · 生成视图可能构造不实纹理，融合依赖两路可靠程度可估计，推理需另算生成开销。

**可复用机制** · 几何与生成图像两路先各自匹配再融置信，不在特征层提前混合。

<a id="paper-drivemvs"></a>

## LiDAR Prompted Spatio-Temporal Multi-View Stereo for Autonomous Driving

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Sun_LiDAR_Prompted_Spatio-Temporal_Multi-View_Stereo_for_Autonomous_Driving_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Sun_LiDAR_Prompted_Spatio-Temporal_Multi-View_Stereo_for_Autonomous_Driving_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 仅靠视觉多视约束容易出现尺度误差，而只把稀疏 LiDAR 当输入特征难保证绝对深度。
- **核心创新 / 方法** · 以稀疏深度约束代价体假设，同时与其他特征软融合，时空解码使用邻帧。
- **Baseline** · 与既有深度估计方法比较，表4拆分硬锚、软融合和时空解码。
- **Benchmark** · KITTI、DDAD 和 Waymo 等报告度量深度误差及跨域表现，表3–4给出时序相关指标。
- **关键结果 / 消融** · 表4列出各项组合的 KITTI AbsRel、阈值准确率和时间误差，完整模块行的 AbsRel 为2.76。
- **适用条件 / 局限** · 依赖稀疏传感器配准和读数质量，缺测和动态遮挡情形应另测。

**可复用机制** · 把稀疏度量观测分别作为代价体的几何锚和软特征，独立检验尺度精度与跨帧稳定性。

<a id="paper-longvideo-r1"></a>

## LongVideo-R1: Smart Navigation for Low-cost Long Video Understanding

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Qiu_LongVideo-R1_Smart_Navigation_for_Low-cost_Long_Video_Understanding_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Qiu_LongVideo-R1_Smart_Navigation_for_Low-cost_Long_Video_Understanding_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 穷举视频片段成本高，只用终局答题对错也难教会代理寻找关键段。
- **核心创新 / 方法** · 从分层视频摘要逐轮定位，再由低层片段验证；SFT 后用强化学习及位置奖励改善取证。
- **Baseline** · 对照仅 SFT、有 RL 无位置奖励及完整方法。
- **Benchmark** · 表1–5覆盖 LVBench、V-MME/L 及 CGBench 子任务，报告问答正确率。
- **关键结果 / 消融** · 表5移除位置奖励时 LVBench 为45.8、V-MME/L 为61.4，完整模型为50.0与64.4。
- **适用条件 / 局限** · 依赖训练时有可用证据位置，语义相关的非答案片段仍可能使搜索停止或陷入错误分支。

**可复用机制** · 给逐步缩窄长视频检索范围的代理加入证据定位奖励，用同一问答测试检查额外导航监督。

<a id="paper-zs-hpd"></a>

## Zero-Shot Image Denoising via Hybrid Prior-Guided Pseudo Sample Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_Zero-Shot_Image_Denoising_via_Hybrid_Prior-Guided_Pseudo_Sample_Generation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_Zero-Shot_Image_Denoising_via_Hybrid_Prior-Guided_Pseudo_Sample_Generation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 只依赖局部邻域会遗漏非局部重复，单用全局配对也可能破坏局部纹理。
- **核心创新 / 方法** · 分别用局部梯度结构与全图非局部相似构造伪样本，另用频带损失调权。
- **Baseline** · 与 Pixel2Pixel、ZS-N2N 及仅用单个采样器比较。
- **Benchmark** · 在 Kodak24、McMaster18 与真实噪声 PolyU、SIDD、FMD 上报告 PSNR、SSIM，表4分噪声强度。
- **关键结果 / 消融** · 表4在 Kodak24 高斯噪声σ25时组合为29.88 dB，两个单采样方案为29.07及29.49；σ10时 ZS-N2N 33.69高于组合33.57。
- **适用条件 / 局限** · 依赖单图存在足够局部及非局部重复；运行成本及收益均随噪声分布变化。

**可复用机制** · 单张图像的零样本复原可同时构造局部邻域对与全局自相似对，按噪声强度做失效对照。

<a id="paper-sorl-latent-diffusion"></a>

## When Local Rules Create Global Order: Self-Organized Representation Learning for Latent Diffusion Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Lian_When_Local_Rules_Create_Global_Order_Self-Organized_Representation_Learning_for_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Lian_When_Local_Rules_Create_Global_Order_Self-Organized_Representation_Learning_for_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 只强调局部平滑可能让编码聚集，降低扩散采样能覆盖的区域。
- **核心创新 / 方法** · 对近邻编码施加重建层局部吸引和防拥挤的局部排斥，通过局部作用共同塑造潜空间。
- **Baseline** · 比较标准 VAE、RV-VAE、EQ-VAE、VA-VAE 等。
- **Benchmark** · CelebA-HQ 无条件生成用 FID、IS、精确率和召回率；ADE20K 训练后在 MS-COCO、LSDIR、DIV2K 测域外重建。
- **关键结果 / 消融** · 表2–3展示生成分布与跨域重建结果，正文比较局部结构及两种作用。
- **适用条件 / 局限** · 邻域定义、训练数据覆盖及分散强度影响效果；图像潜空间结论需在其他模态复验。

**可复用机制** · 训练扩散模型的自编码器时同时检验邻近重建平滑性与潜变量分散度。

<a id="paper-meshflow"></a>

## MeshFlow: Efficient Artistic Mesh Generation via MeshVAE and Flow-based Diffusion Transformer

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_MeshFlow_Efficient_Artistic_Mesh_Generation_via_MeshVAE_and_Flow-based_Diffusion_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_MeshFlow_Efficient_Artistic_Mesh_Generation_via_MeshVAE_and_Flow-based_Diffusion_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 自回归网格序列生成成本随网格大小增加，坐标离散化会损害几何精度。
- **核心创新 / 方法** · 以带对比监督的 MeshVAE 联合编码连续顶点和离散连接，在压缩潜空间上用 Rectified Flow Transformer 并行生成。
- **Baseline** · 对照 MeshGPT、MeshAnything 等自回归路径，表3改变 MeshVAE 设置。
- **Benchmark** · Toys4K 形状条件网格生成比较 Chamfer 距离、Hausdorff 距离和推理时间，表1另评估网格重建。
- **关键结果 / 消融** · 作者报告比所测最快自回归生成器快约18倍，表1–3比较精度和自编码器配置。
- **适用条件 / 局限** · 受训练网格拓扑分布、压缩容量及解码器可表示性限制。

**可复用机制** · 生成拓扑离散、坐标连续的网格时，先学共享潜变量，再选择并行流生成替代顶点序列生成。

<a id="paper-remora-compressed-motion"></a>

## ReMoRa: Multimodal Large Language Model based on Refined Motion Representation for Long-Video Understanding

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yashima_ReMoRa_Multimodal_Large_Language_Model_based_on_Refined_Motion_Representation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yashima_ReMoRa_Multimodal_Large_Language_Model_based_on_Refined_Motion_Representation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 逐帧 RGB 输入昂贵且冗余，直接读取块运动又粗糙且有噪。
- **核心创新 / 方法** · 以稀疏关键帧加经细化的块运动表示分离外观与动态，再以近线性方式压缩序列。
- **Baseline** · 对照 BIMBA、LLaVA-Video 和表1中其他视频 MLLM。
- **Benchmark** · LongVideoBench、NExT-QA、MLVU、VideoMME 等问答；另比较吞吐和峰值显存。
- **关键结果 / 消融** · 表1报告五项总体均分69.8；表3显示吞吐接近 BIMBA，显存约为所测 LLaVA-Video 的一半。
- **适用条件 / 局限** · 需要可提取的运动码流，运动线索受压缩器与镜头变化影响，短暂细粒度外观仍可能漏检。

**可复用机制** · 长视频问答用稀疏 RGB 取外观、压缩码流运动取动态，避免解码全部帧。

<a id="paper-camformer"></a>

## Seeing without Pixels: Perception from Camera Trajectories

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xue_Seeing_without_Pixels_Perception_from_Camera_Trajectories_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xue_Seeing_without_Pixels_Perception_from_Camera_Trajectories_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 像素并非行为线索的唯一来源，但相机移动本身包含多少可辨语义缺乏系统检验。
- **核心创新 / 方法** · 用轻量轨迹编码器将相机位姿和语言描述做对比对齐，再跨位姿估计来源和下游任务比较。
- **Baseline** · 多种轨迹及视觉处理对照；表3比较 Aria 与 MegaSaM、ViPE 等估计位姿。
- **Benchmark** · Ego-Exo4D 和 Nymeria 五选一文字检索，用 top-1 与20%随机参照；另测分类和时间分析。
- **关键结果 / 消融** · 表2–3显示无像素推理取得超随机检索表现，在多种位姿来源下仍可保留有用语义。
- **适用条件 / 局限** · 轨迹反映拍摄行为相关性，不能恢复颜色、文字或不影响相机运动的事件。

**可复用机制** · 视频行为检索或具身轨迹学习中，将相机位姿序列对齐文本，并用轨迹单模态作旁路基线。

<a id="paper-unils"></a>

## UniLS: End-to-End Audio-Driven Avatars for Unified Listening and Speaking

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Chu_UniLS_End-to-End_Audio-Driven_Avatars_for_Unified_Listening_and_Speaking_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Chu_UniLS_End-to-End_Audio-Driven_Avatars_for_Unified_Listening_and_Speaking_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 听者反应和他人语音耦合较弱，直接音频监督容易平均成僵硬动作。
- **核心创新 / 方法** · 先无音频自回归建模人脸运动，再引入双轨语音微调，对说和听共同建模。
- **Baseline** · 对照 FaceFormer、Learning2Listen 等说话与聆听模型，以及去掉预训练阶段的方案。
- **Benchmark** · Seamless Interaction 测说话和聆听，表2以25人进行唇同步、表情、反应等偏好评估。
- **关键结果 / 消融** · 作者报告听者侧所测指标最高改善44.1%；表3对照两阶段训练和组件。
- **适用条件 / 局限** · 验证限于可捕获自然运动的训练分布，弱条件策略无法补足情绪或互动语义等未输入信息。

**可复用机制** · 当条件模态与输出弱相关时，先无条件学自然动态，再微调用弱条件修饰，而非从头强条件拟合。

<a id="paper-no-data-imitation-learning"></a>

## NIL: No-data Imitation Learning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Albaba_NIL_No-data_Imitation_Learning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Albaba_NIL_No-data_Imitation_Learning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 非人体形态的专家三维演示难收集，直接追踪生成视频又可能继承不合物理的运动。
- **核心创新 / 方法** · 将生成视频与仿真渲染瓦片对比，用预训练视频嵌入与分割掩码相似性组成无判别器的模拟训练奖励。
- **Baseline** · 与对抗式视频模仿路径比较，表1对奖励分量做消融。
- **Benchmark** · 多种形态的模拟运动技能，以任务环境奖励及运动相似性等检验。
- **关键结果 / 消融** · 表1报告视频嵌入和掩码信号的相对贡献，正文展示部分非常规形态也可学到动作。
- **适用条件 / 局限** · 依赖渲染和目标视频的视角、形态可比性及仿真有效性，实机迁移仍需验证。

**可复用机制** · 缺少动作捕捉演示时，可用合成视频作为视觉奖励参照，由仿真器负责约束物理可行性。

<a id="paper-crackssm-dynamic-scan"></a>

## CrackSSM: Reviving SSMs for Crack Segmentation via Dynamic Scanning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Gu_CrackSSM_Reviving_SSMs_for_Crack_Segmentation_via_Dynamic_Scanning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Gu_CrackSSM_Reviving_SSMs_for_Crack_Segmentation_via_Dynamic_Scanning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 固定扫描打断细长弯曲结构的像素相邻性。
- **核心创新 / 方法** · 估计四方向响应并重排 SSM 输入，让高相关结构在序列中邻近；另用小波引导解码。
- **Baseline** · 比较 VMamba 等固定扫描以及既有裂纹分割方案；表3消融动态扫描及解码。
- **Benchmark** · Crack500、TUT 等三套数据，比较分割准确性及 FLOPs、参数和显存。
- **关键结果 / 消融** · 表1–3显示方法在相关分割指标改善，TUT 消融用于区分动态扫描与小波解码。
- **适用条件 / 局限** · 方向候选与细长结构假设限制迁移，重排的实际时延仍须随规模测量。

**可复用机制** · 对细长结构使用视觉状态空间模型时，依当前样本方向响应改变序列顺序。

<a id="paper-bidirectional-wavelet-model-scaling"></a>

## A Unified Framework for Knowledge Transfer in Bidirectional Model Scaling

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Shen_A_Unified_Framework_for_Knowledge_Transfer_in_Bidirectional_Model_Scaling_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Shen_A_Unified_Framework_for_Knowledge_Transfer_in_Bidirectional_Model_Scaling_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 模型扩容和缩容常分别训练映射或选择权重，难共用参数转移方案。
- **核心创新 / 方法** · 用离散小波变换及其逆操作把已有权重重采样至目标维数，共用多尺度分解逻辑。
- **Baseline** · 对照 LiGO、Mango 等扩容方法，以及相应缩容和标准初始化对照。
- **Benchmark** · DeiT、BERT、GPT；衡量预训练 FLOPs 和下游性能，含 GLUE、SQuAD 的准确率、F1、EM 等。
- **关键结果 / 消融** · 作者报告扩容最高节省67.1%、缩容最高52.8%预训练 FLOPs，表2–3报告直接微调性能。
- **适用条件 / 局限** · 依赖可对应的参数轴和架构，跨拓扑差异或任意通道排列下的小波局部性需要核验。

**可复用机制** · 缩放预训练模型时，把同层权重当作多分辨率信号，用小波重采样初始化大小两种目标。

<a id="paper-moeclip-expert-diversity"></a>

## MoECLIP: Patch-Specialized Experts for Zero-shot Anomaly Detection

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Park_MoECLIP_Patch-Specialized_Experts_for_Zero-shot_Anomaly_Detection_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Park_MoECLIP_Patch-Specialized_Experts_for_Zero-shot_Anomaly_Detection_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 所有局部区域共用适配器会削弱异常区域特化，而多个专家又可能重复学习。
- **核心创新 / 方法** · 按 patch 路由低秩专家，用固定正交投影分割专家输入，并约束专家输出近似单纯形等角紧框架。
- **Baseline** · 比较原始 CLIP、仅去正交输入、仅去等角损失和两者都去，另比零样本异常检测方法。
- **Benchmark** · 14 组工业和医学数据，表 2 使用 MVTec-AD、DTD-Synthetic、Head CT、ColonDB，报告像素或图像 AUROC。
- **关键结果 / 消融** · 完整方法平均像素/图像 AUROC 为 92.2/95.3；两种专家多样化项都去掉为 91.2/93.1，说明多数增益仍来自主体适配。
- **适用条件 / 局限** · 依赖多专家实际能分工，正交子空间也可能舍弃共用信号；其他任务需等训练预算验证路由利用率和收益。

**可复用机制** · 逐 patch 的 LoRA 专家出现冗余时，可分别消融输入子空间正交化和输出等角约束。见表 2。

<a id="paper-reflection-equivariant-latents"></a>

## Rectifying Latent Space for Generative Single-Image Reflection Removal

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Rectifying_Latent_Space_for_Generative_Single-Image_Reflection_Removal_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Rectifying_Latent_Space_for_Generative_Single-Image_Reflection_Removal_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 反射和透射在观测中叠加，普通语义 VAE 的潜变量没有显式保持这种混合关系。
- **核心创新 / 方法** · 在 VAE 中以反射等变约束对齐潜表示与线性叠加，同时学习任务条件和早期采样分支。
- **Baseline** · 比较原 VAE、仅用重建损失微调及完整等变方案，另对照 RDNet、DAI 等去反射方法。
- **Benchmark** · Real20、SIR2、Nature 等真实单图去反射集合，报告 PSNR、SSIM 和人评。
- **关键结果 / 消融** · 表 4 仅重建微调为 25.79 dB/0.842，加入完整方案为 27.27 dB/0.871。
- **适用条件 / 局限** · 依赖线性成像混合近似；饱和、多重反射或散射会破坏假设，生成输出仍可能补出错误细节。

**可复用机制** · 用生成模型分离叠加成像时，应检测编码器能否保留物理混合关系，并与仅重建微调比较。见表 4。

<a id="paper-chimera-temporal-risk"></a>

## Unstitching the Chimera: Frame-Level Risk and Train-Free Mitigation for Video Hallucination

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_Unstitching_the_Chimera_Frame-Level_Risk_and_Train-Free_Mitigation_for_Video_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yang_Unstitching_the_Chimera_Frame-Level_Risk_and_Train-Free_Mitigation_for_Video_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 单帧细节都真实，模型也可能误把不同时间片段拼成连续事件。
- **核心创新 / 方法** · 以覆盖文本证据所需的片段数及早期时序路径的排序一致性度量风险，再重分配片段注意力和片段内词元权重。
- **Baseline** · 对比原模型、仅片段分配、仅词元校准和两阶段反序。
- **Benchmark** · 九个视频基准、六种视频语言模型；表 3 在 NExT-QA 和 VidHalluc 比较准确率及风险变化。
- **关键结果 / 消融** · 表 3 NExT-QA/VidHalluc 由 73.2/76.6 提升到 75.1/80.2，反序为 74.7/79.7。
- **适用条件 / 局限** · 需要内部注意力访问和可靠分段；多时段确实属于同一事件时，片段覆盖广不代表幻觉。

**可复用机制** · 视频问答可单独检测把本来存在但互不相干的片段拼成同一叙事的失效，并比较先分段再校准的顺序。见表 2–3。

<a id="paper-physical-refraction-generation"></a>

## Refracting Reality: Generating Images with Realistic Transparent Objects

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yin_Refracting_Reality_Generating_Images_with_Realistic_Transparent_Objects_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yin_Refracting_Reality_Generating_Images_with_Realistic_Transparent_Objects_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 生成器常把透明物折射画得视觉合理，实际折射像素却不能解释为同一背景表面的映射。
- **核心创新 / 方法** · 每步按 Snell 定律建立透明物内外的光线路径，将对应像素变换并调和；对视野外反射或折射使用对应的生成全景。
- **Baseline** · 比较 FLUX 等生成基线及去掉反射、全景和重照明的版本。
- **Benchmark** · 受控渲染与实拍透明物，表 2 在六个球形场景测 MAE、PSNR、LPIPS、CLIP 与 ImageReward。
- **关键结果 / 消融** · 表 2 去全景或反射会削弱像素保真；加入照明阴影后像素指标未必上升，说明感知合理性需要另测。
- **适用条件 / 局限** · 光线路径依赖透明物几何及光学参数正确；复杂材料、粗糙散射和多重反射需要额外建模。

**可复用机制** · 当图像生成受可计算成像方程约束时，可以在去噪过程中显式同步图内和旁视角的同源像素，并分开检查物理与感知指标。见表 2。

<a id="paper-stochastic-gaussian-raytracing"></a>

## Stochastic Ray Tracing for the Reconstruction of 3D Gaussian Splatting

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_Stochastic_Ray_Tracing_for_the_Reconstruction_of_3D_Gaussian_Splatting_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_Stochastic_Ray_Tracing_for_the_Reconstruction_of_3D_Gaussian_Splatting_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 高斯光追会为穿过的所有高斯排序，尤其拖慢可微重建和带阴影重照明。
- **核心创新 / 方法** · 用每条射线抽取少量高斯的 Monte Carlo 估计颜色梯度，绕开排序；重照明沿用同估计器与阴影射线。
- **Baseline** · 比较光栅化 3DGS、排序式 3DGRT 和不同抽样数量。
- **Benchmark** · MipNeRF360、Tanks & Temples、Deep Blending 的新视图 PSNR/SSIM/LPIPS 及训练耗时；另用 NRHints 验证重照明。
- **关键结果 / 消融** · 表 2 MipNeRF360 单迭代 39.8 ms，3DGRT 87.5 ms，光栅 31.4 ms；表 1 的 PSNR 分别为 28.31、28.40 和 28.69。
- **适用条件 / 局限** · 抽样无偏不代表低方差或更快收敛，采样量、遮挡与 GPU 光追性能需针对场景测量。

**可复用机制** · 训练可微高斯光追时，可用每条光线的无偏随机梯度替代确定性遍历排序，并对照时间与画质。见表 1–2。

<a id="paper-ralu-edge-aware-latent-upsampling"></a>

## Training-free Mixed-Resolution Latent Upsampling for Spatially Accelerated Diffusion Transformers

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Jeong_Training-free_Mixed-Resolution_Latent_Upsampling_for_Spatially_Accelerated_Diffusion_Transformers_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Jeong_Training-free_Mixed-Resolution_Latent_Upsampling_for_Spatially_Accelerated_Diffusion_Transformers_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 低分辨率潜变量粗升采样会在边缘产生混叠，改变分辨率后原去噪时刻也可能失配。
- **核心创新 / 方法** · 先提升边缘区域的潜分辨率，再按分辨率匹配噪声水平和时间步，晚些升级平滑区域。
- **Baseline** · 比较均匀升采样、不同边缘占比和不同噪声时间配对，另测与时间加速组合。
- **Benchmark** · FLUX.1-dev、Stable Diffusion 3，报告速度、TFLOPs、ImageReward、NIQE 和组合提示指标。
- **关键结果 / 消融** · 图 8 的质量随提前升采样比例先升后平，约 0.3 附近最好；表 3 在 FLUX 约 7 倍设置中，校准配对 ImageReward 为 0.999。
- **适用条件 / 局限** · 依赖高频边缘足以定位关键细节；低对比细纹或多尺度语义可能漏掉，应另验视觉质量和真实延迟。

**可复用机制** · 扩散空间加速应分别处理边缘混叠和上采样后噪声时刻失配；对比不同区域预算和噪声匹配。见图 8、表 3。

<a id="paper-prom3e"></a>

## ProM3E: Probabilistic Masked MultiModal Embedding Model for Ecology

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Sastry_ProM3E_Probabilistic_Masked_MultiModal_Embedding_Model_for_Ecology_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Sastry_ProM3E_Probabilistic_Masked_MultiModal_Embedding_Model_for_Ecology_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 生态数据各样本往往只有部分图像、声音或描述，统一融合可能加入误导信息。
- **核心创新 / 方法** · 在嵌入中做掩码模态重建以预测缺失表示，再以模态内及模态间相似度共同检索。
- **Baseline** · 与 TaxaBench-8k 上的基线及单模态输入比较，表2比较双模态。
- **Benchmark** · 表1–4报告物种零样本分类、跨模态检索和鸟类音频线性探针。
- **关键结果 / 消融** · 表3报告组合相似度在所列检索任务上改善，另用表4验证表示可用于分类。
- **适用条件 / 局限** · 潜空间可补全不等于能重建细粒度原信号，物种覆盖及缺失方式变化需复测。

**可复用机制** · 缺失模态不必重建原始信号，可学习潜表示分布并以检索对照判断融合哪些模态。

<a id="paper-unified-camera-positional-encoding"></a>

## Unified Camera Positional Encoding for Controlled Video Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Unified_Camera_Positional_Encoding_for_Controlled_Video_Generation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Unified_Camera_Positional_Encoding_for_Controlled_Video_Generation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 针孔近似丢失真实镜头差异，只给相对相机轨迹也不能设定起始朝向。
- **核心创新 / 方法** · 用几何一致的相对射线编码全部相机变量，以俯仰和滚转提供绝对朝向条件。
- **Baseline** · 与已有相机位置及姿态编码比较，另消融空间压缩配置。
- **Benchmark** · 合成镜头及相机控制数据和 RealEstate10K，表1–2报告镜头、朝向和位姿控制误差。
- **关键结果 / 消融** · 表1报告相对基线的初始俯仰和滚转误差降低，表2测试实景相机轨迹。
- **适用条件 / 局限** · 需要相机参数可信，真实非针孔设备的校准误差应另测。

**可复用机制** · 以相对射线表达相机姿态、内参和镜头畸变，并将初始绝对朝向单独编码。

<a id="paper-mvc-zigal"></a>

## Refining Few-Step Text-to-Multiview Diffusion via Reinforcement Learning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Refining_Few-Step_Text-to-Multiview_Diffusion_via_Reinforcement_Learning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Refining_Few-Step_Text-to-Multiview_Diffusion_via_Reinforcement_Learning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 逐图奖励不能发现不同视图彼此矛盾，少步采样可用的训练反馈又少。
- **核心创新 / 方法** · 联合建模生成视图，同时使用视图内与联合视图奖励，并以自细化采样产生优势对照。
- **Baseline** · 正文对照 PG、MV-DPO、MV-RDL，以及采样和约束的消融。
- **Benchmark** · 正文表1–2在未见提示上评估多项生成奖励及一致性。
- **关键结果 / 消融** · 表2用不同版本区分自细化样本、联合奖励和约束更新的贡献。
- **适用条件 / 局限** · 奖励一致性不能代替真实三维重建误差，需复验采样预算和奖励泛化。

**可复用机制** · 少步多视图生成的奖励要同时测视图保真和跨视一致，可在同一采样预算验证约束取舍。

<a id="paper-seam"></a>

## Rethinking Intermediate Representation for VLM-based Robot Manipulation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Tang_Rethinking_Intermediate_Representation_for_VLM-based_Robot_Manipulation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Tang_Rethinking_Intermediate_Representation_for_VLM-based_Robot_Manipulation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 自由文本难可靠映射到动作，过于固定的指令模板又难组合新任务。
- **核心创新 / 方法** · SEAM 将语义丰富的操作词和可执行语法分开，并用部件定位补充对应的视觉对象。
- **Baseline** · 表2–4与不同操作表示、定位方案及词汇语法组合比较。
- **Benchmark** · 正文测试任务执行、动作泛化、模型输出有效性与运行时间。
- **关键结果 / 消融** · 正文分别比较表示形式和部件定位，并以任务成功之外的指标检查表示选择。
- **适用条件 / 局限** · 只可执行已覆盖的操作原语，部件误定位与执行安全仍需独立验收。

**可复用机制** · 在高层 VLM 和机器执行之间分别定义操作词汇与组合语法，检验新任务重组是否可执行。

<a id="paper-sgdir"></a>

## Learning Diffeomorphism for Medical Image Registration with Time-Embedded Architectures Using Semigroup Regularization

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Matinkia_Learning_Diffeomorphism_for_Medical_Image_Registration_with_Time-Embedded_Architectures_Using_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Matinkia_Learning_Diffeomorphism_for_Medical_Image_Registration_with_Time-Embedded_Architectures_Using_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 显式积分及多个辅助项增加可逆形变训练的复杂度。
- **核心创新 / 方法** · 让时间条件网络直接输出变形，通过半群组合正则约束其对应自主 ODE 流。
- **Baseline** · 与微分同胚方法、非同胚配准及不同正则强度比较。
- **Benchmark** · 正文表1–5覆盖 OASIS 等脑 MRI 和多套 CT，报告 Dice 和 Jacobian 拓扑违例等。
- **关键结果 / 消融** · 较严格正则下正文报告接近无拓扑违例，放宽正则可提高配准准确性。
- **适用条件 / 局限** · 理论要求组合律严格满足，实际训练只近似满足，需核查背离理论的局部折叠。

**可复用机制** · 连续形变用时间半群一致性约束取代显式积分，并按正则强度验拓扑与配准精度。

<a id="paper-e2oal"></a>

## Revisiting Unknowns: Towards Effective and Efficient Open-Set Active Learning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zong_Revisiting_Unknowns_Towards_Effective_and_Efficient_Open-Set_Active_Learning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zong_Revisiting_Unknowns_Towards_Effective_and_Efficient_Open-Set_Active_Learning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 未知类常被当作标注预算损失，单独训练检测器也会提高成本。
- **核心创新 / 方法** · 聚类已确认未知样本，用 Dirichlet 辅助头联合建模已知与未知；先按纯度选池，再按信息量选标注样本。
- **Baseline** · 与 EOAL、MQNet 等主动学习方法及去掉未知标签的同框架方案比较。
- **Benchmark** · CIFAR-10/100、Tiny-ImageNet 开放集主动学习，不同已知未知比例，测末轮准确率、查询纯度及信息性。
- **关键结果 / 消融** · 表1–3显示纳入未知标签提高末轮准确率，分开检验候选纯度与查询信息性。
- **适用条件 / 局限** · 需要能区分已知与未知的表示和人工标签；未知类比例或类别结构变化需重新核验。

**可复用机制** · 开放集主动学习中保存人工确认的未知样本，用其校准查询池并训练辅助类别头。

<a id="paper-drivor-camera-registers"></a>

## Driving on Registers

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Kirby_Driving_on_Registers_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Kirby_Driving_on_Registers_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 把所有相机 patch token 送入下游解码器代价高，单一轨迹预测也不方便根据不同目标选择结果。
- **核心创新 / 方法** · 带相机标识的寄存器形成紧凑场景表示，两个轻量解码器分别生成候选和拟合可解释的多项分数。
- **Baseline** · 表1–3比较 NAVSIM 的现有相机方案；另在闭环 HUGSIM 对照。
- **Benchmark** · NAVSIM-v1/v2 用 PDMS、EPDMS 等规划指标，另在 HUGSIM 闭环评估。
- **关键结果 / 消融** · 表1–3报告压缩场景表示时仍达到有竞争力的规划表现，并展示子分数用于行为选择。
- **适用条件 / 局限** · 聚合可能丢失未被寄存器捕捉的小目标证据，闭环仿真分数不能取代真实道路验证。

**可复用机制** · 多相机行为模型让相机感知的寄存器 token 先压缩视图，再让同一紧凑表示服务候选与打分。

<a id="paper-moe-grpo-routing"></a>

## MoE-GRPO: Optimizing Mixture-of-Experts via Reinforcement Learning in Vision-Language Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Ko_MoE-GRPO_Optimizing_Mixture-of-Experts_via_Reinforcement_Learning_in_Vision-Language_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Ko_MoE-GRPO_Optimizing_Mixture-of-Experts_via_Reinforcement_Learning_in_Vision-Language_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 逐层确定性 top-k 会反复选择类似专家，可能掩盖其他专家组合。
- **核心创新 / 方法** · 把专家组合视为连续决策，用 GRPO 优化路由并加入模态相关的路由引导。
- **Baseline** · 确定性 top-k 及其变体，比较激活专家规模；另检验跨数据集设置。
- **Benchmark** · 多模态图像及视频理解平均准确率；ImageNet 16-shot 训练后迁移到10个目标集及4个域外集。
- **关键结果 / 消融** · 表1–3报告所测标准与迁移任务的总体表现提升，并分析更分散的专家选择。
- **适用条件 / 局限** · 训练需要多次试验路由并获得可靠奖励，模态先验可能限制发现低频有用专家。

**可复用机制** · 稀疏多模态专家中，用奖励反馈探索专家组合，并按模态约束不必要的探索。

<a id="paper-steph-sparse-task-mixup"></a>

## Sparse Task Vector Mixup with Hypernetworks for Efficient Knowledge Transfer in Whole-Slide Image Prognosis

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_Sparse_Task_Vector_Mixup_with_Hypernetworks_for_Efficient_Knowledge_Transfer_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_Sparse_Task_Vector_Mixup_with_Hypernetworks_for_Efficient_Knowledge_Transfer_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 单癌种数据少，联合训练和多模型推理都昂贵。
- **核心创新 / 方法** · 配对混合源与目标任务向量，然后用超网络驱动稀疏聚合，把归纳知识写回单一目标模型。
- **Baseline** · 对照癌种专用单模型、知识迁移基线及 TIES 等合并方法。
- **Benchmark** · 13个全切片癌症预后数据集，用五折交叉验证 C-index 的均值和标准差。
- **关键结果 / 消融** · 摘要报告相对单癌种学习和既有迁移基线分别改善5.14%与2.01%；表2消融，表3将聚合用于其他合并方法。
- **适用条件 / 局限** · 需要参数可对齐的源模型，来源域不相关或权重基底不同的情况须复核。

**可复用机制** · 目标数据少且已有多个任务模型时，先混合源与目标的任务向量，再稀疏选择贡献。

<a id="paper-tokentrace"></a>

## TokenTrace: Multi-Concept Attribution through Watermarked Token Recovery

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_TokenTrace_Multi-Concept_Attribution_through_Watermarked_Token_Recovery_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_TokenTrace_Multi-Concept_Attribution_through_Watermarked_Token_Recovery_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 同一生成图可组合对象和风格，检测整图签名无法判定某个概念来自哪里。
- **核心创新 / 方法** · 在生成时记录概念相关的潜空间签名，归因时以文本查询限定要验证的概念。
- **Baseline** · 表1对比主动及被动归因方法，表3消融训练损失。
- **Benchmark** · WikiArt 与 ImageNet 单概念归因，另测2个、4个概念的组合、视觉质量及常见变换。
- **关键结果 / 消融** · 表1–2报告单概念及组合归因表现改善；表3检验组合目标。
- **适用条件 / 局限** · 只适用于生成阶段可合作写入签名的模型；未覆盖的概念、强变换及任意生成器不可直接归因。

**可复用机制** · 生成图的多概念归因需要按查询解码，先区分概念级可验证性与整图水印存在性。

<a id="paper-twin-t-structure-detail"></a>

## Twin-T & TwintVQA: A Reliable Structure-Detail Separating VLM and a Comprehensive Benchmark for Chart and Table Tasks

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Bao_Twin-T__TwintVQA_A_Reliable_Structure-Detail_Separating_VLM_and_a_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Bao_Twin-T__TwintVQA_A_Reliable_Structure-Detail_Separating_VLM_and_a_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 文字语义相似时仍可能读错数字、表格位置或图表尺度。
- **核心创新 / 方法** · 视觉双头分别处理结构与细节，MINT 对数值、关键词与图文匹配进行偏好学习。
- **Baseline** · GPT-4o、Gemini 2.5 Pro 与开源 VLM 等；比较公开图表任务和 TwintVQA。
- **Benchmark** · ChartQA、CharXiv、TableVQA 等，TwintVQA 扩展至17类图表、11类任务、3种格式和不同问答长度。
- **关键结果 / 消融** · 表1–3报告在多项开源模型比较中获得提升，细分表可观察任务和长度差异。
- **适用条件 / 局限** · 依赖结构可读、数字能稳定提取；非结构化网页和低质扫描尚需证据。

**可复用机制** · 训练图表问答时，把布局理解与数字细节分开建模，并在偏好目标中显式核对数值和关键词。

<a id="paper-nanosd-latency-aware-distillation"></a>

## NanoSD: Edge Efficient Foundation Model for Real Time Image Restoration

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Sanyal_NanoSD_Edge_Efficient_Foundation_Model_for_Real_Time_Image_Restoration_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Sanyal_NanoSD_Edge_Efficient_Foundation_Model_for_Real_Time_Image_Restoration_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 只缩小去噪器或参数个数不能保证整条链路的时延改善，可能损坏潜空间。
- **核心创新 / 方法** · 基于 SD1.5 对去噪器与 VAE 共同做结构裁剪和特征蒸馏，以硬件延迟和教师对齐 FID 选择帕累托配置。
- **Baseline** · 比较 TinySD、手工调节模型及多个 NanoSD 配置。
- **Benchmark** · Qualcomm NPU 采用8位权重及16位激活测时延和 taFID；DIV2K 与合成 CelebA 测恢复质量。
- **关键结果 / 消融** · 表1报告不同参数量的延迟排序并不一致，部分配置达到约20毫秒；表2–3比较恢复效果。
- **适用条件 / 局限** · 硬件内核、量化和输入尺寸影响延迟排序，迁移平台需要重新测。

**可复用机制** · 边缘扩散部署时把 VAE 和去噪器共同蒸馏，并用目标硬件实测延迟选结构。

<a id="paper-mad-modality-adaptive-decoding"></a>

## MAD: Modality-Adaptive Decoding for Mitigating Cross-Modal Hallucinations in Multimodal Large Language Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Chung_MAD_Modality-Adaptive_Decoding_for_Mitigating_Cross-Modal_Hallucinations_in_Multimodal_Large_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Chung_MAD_Modality-Adaptive_Decoding_for_Mitigating_Cross-Modal_Hallucinations_in_Multimodal_Large_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 与问题无关的音频或画面可误导另一路感知，统一降低所有模态影响也会损失有用证据。
- **核心创新 / 方法** · 让模型自评问题需要的模态，以所得概率动态加权对比解码分支，无需训练。
- **Baseline** · 同一骨干的原始解码、VCD-Extended、AVCD，表2–3消融融合方式和各分支权重。
- **Benchmark** · CMM 与 AVHBench，两类跨模态幻觉评测；跨多个音视频语言模型对照。
- **关键结果 / 消融** · 作者报告 VideoLLaMA2-AV 分别改善7.8%和2.0%，Qwen2.5-Omni 改善8.7%和4.7%。
- **适用条件 / 局限** · 依赖模型自评模态相关性的可靠性，多分支解码也增加推理成本。

**可复用机制** · 音视频问答先估计问题需要哪些模态，再按该概率调整不同解码分支。

<a id="paper-fft-minimal-polynomial-solvers"></a>

## Solving Minimal Problems Without Matrix Inversion Using FFT-Based Interpolation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_Solving_Minimal_Problems_Without_Matrix_Inversion_Using_FFT-Based_Interpolation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wu_Solving_Minimal_Problems_Without_Matrix_Inversion_Using_FFT-Based_Interpolation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 相机几何最小问题常需多变量消元，在线矩阵求逆带来耗时及数值风险。
- **核心创新 / 方法** · 通过稀疏隐变量结式构造矩阵，对行列式采样并逆 FFT 插值，求根后用秩亏子矩阵和 Cramer 法恢复其余变量。
- **Baseline** · 比较 SparseR、GAPS 的速度、候选根与稳定性。
- **Benchmark** · 在相对位姿、未知焦距与拼接等最小问题上比较求解时间、根数及数值误差。
- **关键结果 / 消融** · 表 2 的 E+f 六点问题为 0.154 ms，SparseR 为 0.345 ms，GAPS 为 0.235 ms，三者均返回 9 根。
- **适用条件 / 局限** · 优势主要见小规模系统，行列式次数、采样病态和根筛选会改变大问题的成本。

**可复用机制** · 小规模几何最小问题的消元可比较用 FFT 插值重建行列式多项式和传统在线矩阵求逆。见表 1–2。

<a id="paper-tgr-moe-teacher-routing"></a>

## Teacher-Guided Routing for Sparse Vision Mixture-of-Experts

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Kada_Teacher-Guided_Routing_for_Sparse_Vision_Mixture-of-Experts_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Kada_Teacher-Guided_Routing_for_Sparse_Vision_Mixture-of-Experts_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 只更新被选专家可能使未选路由缺少梯度，训练中专家分工反复变化。
- **核心创新 / 方法** · 从冻结稠密教师的中间表征训练补充路由器，以其分配分布指导学生的稀疏路由。
- **Baseline** · 比较稠密 ViT、VMoE、z-loss 及不同训练阶段保留教师引导的版本。
- **Benchmark** · ImageNet-1K 与转移分类任务；报告 top-1 和路由一致性，表 3 为 CIFAR-100 单专家配置。
- **关键结果 / 消融** · 表 3 的 Base 规模，VMoE 89.04%，教师引导仅预训练 90.05%，微调继续引导 91.07%。
- **适用条件 / 局限** · 需要已有可复用教师；教师分配可能不适用于目标域，额外训练不能与同推理 FLOPs 混为一谈。

**可复用机制** · 稀疏专家反馈只覆盖已选路由时，可加冻结稠密教师派生的路由监督，单独测路由稳定性及迁移。见图 3、表 3。

<a id="paper-deltaquant-video-local-residual"></a>

## DeltaQuant: 4-bit Video Diffusion Models with Spatiotemporal Delta Smoothing

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_DeltaQuant_4-bit_Video_Diffusion_Models_with_Spatiotemporal_Delta_Smoothing_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_DeltaQuant_4-bit_Video_Diffusion_Models_with_Spatiotemporal_Delta_Smoothing_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 不同去噪步的激活异常通道不固定，直接全量低位宽量化产生明显失真。
- **核心创新 / 方法** · 将激活按局部时空块分组，以块均值作 FP8 核，对差值做 4 位量化。
- **Baseline** · 比较 RTN、SmoothQuant、SVDQuant、S2Q-VDiT 及 W4A16。
- **Benchmark** · 对 Wan2.2 I2V/T2V 等生成比较 16 位参考的 LPIPS、PSNR、SSIM，以及 VBench 和延迟。
- **关键结果 / 消融** · 表 1 的 Wan2.2 I2V，W4A4 DeltaQuant 为 23.2 dB，W4A4 SVDQuant 为 21.9，W4A16 为 23.2。
- **适用条件 / 局限** · 需要硬件支持低精度核，时空邻域出现切镜或突变时，共量残差假设需复测。

**可复用机制** · 视频低位宽量化可把邻近时空激活的共量保留高精度，只量化局部残差。见表 1。

<a id="paper-astranav-memory-compression"></a>

## AstraNav-Memory: Contexts Compression for Long Memory

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Hu_AstraNav-Memory_Contexts_Compression_for_Long_Memory_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Hu_AstraNav-Memory_Contexts_Compression_for_Long_Memory_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 对象记忆依赖检测和重建，而把历史帧直接放入上下文很耗内存。
- **核心创新 / 方法** · 用冻结视觉特征及轻量空间压缩生成每帧少量词元，并联合训练导航策略。
- **Baseline** · 对照同策略的未压缩历史、不同帧数和压缩率。
- **Benchmark** · GOAT-Bench 和 HM3D-OVON 测成功率和 SPL，另在抽样子集测内存、训练及推理时间。
- **关键结果 / 消融** · 表 4 的 50 帧不压缩成功率为 60.2，100 帧 4 倍压缩为 63.2；即使留 500 帧，64 倍压缩也只有 47.6。
- **适用条件 / 局限** · 依赖历史画面含能找回的空间语义，极高压缩会丢掉细目标；子集取舍应在新域重复测量。

**可复用机制** · 长程导航的图像记忆可联合扫描保留长度与每帧压缩率，避免把更长历史当成自动收益。见表 3–4。

<a id="paper-adaptive-lowpass-i2v-motion"></a>

## Improving Motion in Image-to-Video Models via Adaptive Low-Pass Guidance

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Choi_Improving_Motion_in_Image-to-Video_Models_via_Adaptive_Low-Pass_Guidance_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Choi_Improving_Motion_in_Image-to-Video_Models_via_Adaptive_Low-Pass_Guidance_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 参考图在去噪早期暴露细纹可能把模型锁到静止外观捷径。
- **核心创新 / 方法** · 早期对图像条件施自适应低通，再以条件引导恢复外观细节，无需训练。
- **Baseline** · 对照固定 CFG，跨 Wan 2.1/2.2 和 LTX-Video；另比运动增强提示。
- **Benchmark** · VBench、PVD、VidProM，测动态度、视频质量、参考一致性、DOVER 与 Vision Reward。
- **关键结果 / 消融** · 表 2 Wan2.2 的动态度由 31.7 到 39.0，I2V 一致性保持 98.5；Wan2.1 的一致性从 98.3 微降到 98.0。
- **适用条件 / 局限** · 依赖高频图像条件是静止原因；主动追求静态、关键细纹或需要精确身份的任务宜单测。

**可复用机制** · 图生视频不动时，可测试早期衰减参考图高频信息、大体运动形成后再恢复，与注意力路径调整区分。见表 2–3。

<a id="paper-orthographic-silhouette-pose-search"></a>

## Globally Optimal Pose from Orthographic Silhouettes

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Sengupta_Globally_Optimal_Pose_from_Orthographic_Silhouettes_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Sengupta_Globally_Optimal_Pose_from_Orthographic_Silhouettes_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 点对应不可用时，已知三维物体的姿态求解可能依赖易卡局部极值的轮廓匹配。
- **核心创新 / 方法** · 按旋转预计算正交投影面积响应面，以轮廓面积连续性约束多分辨率搜索，辅以投影椭圆轴比。
- **Baseline** · 比较 NlR、Nl-PaR、Ms-GO、STI-Pose 与完整搜索方法。
- **Benchmark** · 斯坦福兔和其他已知形状的合成及真实样例，报告平移、方向及重建误差。
- **关键结果 / 消融** · 表 1 在不同实物轮廓上完整方案误差较低，实验从独立采样点云估计姿态，避免复用预计算样本。
- **适用条件 / 局限** · 依赖已知几何、正交投影及无明显遮挡，旋转对称的物体可能出现不可辨别的等价姿态。

**可复用机制** · 已知几何在无对应轮廓场景中，可预计算旋转对应的全局轮廓签名以约束分支搜索。见 §4、表 1–4。

<a id="paper-otil-selective-latent-synchronization"></a>

## Otil: Accelerating Diffusion Model Inference via Communication-Efficient Multi-GPU Parallelism

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Otil_Accelerating_Diffusion_Model_Inference_via_Communication-Efficient_Multi-GPU_Parallelism_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Otil_Accelerating_Diffusion_Model_Inference_via_Communication-Efficient_Multi-GPU_Parallelism_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 并行去噪每步跨 GPU 传完整潜表示可能抵消并行收益。
- **核心创新 / 方法** · 根据相邻步变化选出值得同步的空间块，同时周期遍历全部空间以避免长期陈旧。
- **Baseline** · 比较 AsyncDiff、DistriFusion 及不同同步比例和块大小。
- **Benchmark** · 在 SD 1.5、SDXL 等测多 GPU 单步延迟、端到端耗时和 LPIPS。
- **关键结果 / 消融** · 表 4 的双卡 SDXL，8×8 块为 27.53 ms、LPIPS 0.0142；16×16 胜在小幅更快（27.11 ms），但 LPIPS 升至 0.0294。
- **适用条件 / 局限** · 收益随跨卡带宽、拓扑和潜状态变化速度而变，小批次或激烈变化应复测实际吞吐。

**可复用机制** · 多 GPU 扩散加速可只同步变化大的潜块并轮询全区，用通信时延和质量共同调块大小。见表 3–4。

<a id="paper-vde-rectified-flow"></a>

## VDE: Training-Free Accelerating Rectified Flow Model via Velocity Decomposition and Estimation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Tan_VDE_Training-Free_Accelerating_Rectified_Flow_Model_via_Velocity_Decomposition_and_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Tan_VDE_Training-Free_Accelerating_Rectified_Flow_Model_via_Velocity_Decomposition_and_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 直接缓存先前步骤的激活会随去噪状态变化产生偏差。
- **核心创新 / 方法** · 将速度拆为平行及正交分量，以时序估计补中间步，定期完整前向重置误差。
- **Baseline** · 与标准采样及缓存加速方法比较，表3–4消融分量和锚点间隔。
- **Benchmark** · 表1–2覆盖 FLUX.1、Qwen-Image、Wan-2.1，比较加速及输出距离等。
- **关键结果 / 消融** · 正文报告 FLUX 加速3.22倍，Qwen-Image 的 LPIPS 为0.069。
- **适用条件 / 局限** · 分解收益依赖分量局部变化的规律性，锚点间隔应在新模型和新采样日程复测。

**可复用机制** · 沿当前输入方向分解速度并随输入估计，可与直接复用陈旧速度缓存比较。

<a id="paper-implicit-lidar-design"></a>

## Task-Driven Implicit Representations for Automated Design of LiDAR Systems

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Behari_Task-Driven_Implicit_Representations_for_Automated_Design_of_LiDAR_Systems_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Behari_Task-Driven_Implicit_Representations_for_Automated_Design_of_LiDAR_Systems_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 手动设计容易把逻辑采样价值和硬件约束混在一起，遮挡还会造成配置失效。
- **核心创新 / 方法** · 以流模型学习连续设计空间的任务密度，并用参数分布拟合受约束传感器设置。
- **Baseline** · 正文 Expt. E 对照去掉射线可见性以及占用网格建模。
- **Benchmark** · 仿真中的面部扫描、机械末端跟踪和目标检测，以采样预算、重建及轨迹误差评估。
- **关键结果 / 消融** · 图11中考虑遮挡的配置用约一半射线达到近似的末端轨迹误差。
- **适用条件 / 局限** · 依赖仿真几何和遮挡分布，实机标定、环境变化及成本需另核。

**可复用机制** · 传感器设计可先学习任务下的有效采样分布，再在明确硬件约束内拟合配置。

<a id="paper-label-aligned-transfer"></a>

## Mind the Gap: Transferring Labels to Align Object Detection Datasets

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Kennerley_Mind_the_Gap_Transferring_Labels_to_Align_Object_Detection_Datasets_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Kennerley_Mind_the_Gap_Transferring_Labels_to_Align_Object_Detection_Datasets_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 同名类与边界框经常并不同义，直接并数据会混淆定位及类别。
- **核心创新 / 方法** · 训练来源检测器产生伪标，将其和真值融合为共享候选，再以类感知区域特征过滤噪声。
- **Baseline** · 与直接标签或数据合并以及基于 VLM 的标签迁移比较。
- **Benchmark** · 表1–3比较类别差异和小到大数据集设置下的目标检测效果。
- **关键结果 / 消融** · 正文报告类别差异设置下 LAT 优于所测标签基线，允许多个来源类别映射同一目标类别。
- **适用条件 / 局限** · 依赖来源教师伪标准确和目标标注足够，罕见类不能靠框对齐自动解决。

**可复用机制** · 合并有标签冲突的数据集时，可在候选区域内对齐到目标定义，并保留不同来源的粒度。

<a id="paper-proxy3d"></a>

## Proxy3D: Efficient 3D Representations for Vision-Language Models via Semantic Clustering and Alignment

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Jiang_Proxy3D_Efficient_3D_Representations_for_Vision-Language_Models_via_Semantic_Clustering_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Jiang_Proxy3D_Efficient_3D_Representations_for_Vision-Language_Models_via_Semantic_Clustering_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 逐帧序列长且缺少三维归并，短序列又容易遗漏物体。
- **核心创新 / 方法** · 提取语义和几何后按三维语义聚类，用多阶段训练对齐 VLM。
- **Baseline** · 与像素或对应表示的模型比较，消融语义聚类、跨帧注意和动态代理数量。
- **Benchmark** · 表2–5包含三维问答、指代定位、稠密描述与 VSI-Bench。
- **关键结果 / 消融** · 表4–5将分组和代理预算独立比较，正文报告较短输入仍保留空间任务表现。
- **适用条件 / 局限** · 深度或帧间几何误差可导致错聚类，小对象需单测。

**可复用机制** · 将多帧中语义相似的三维特征聚成代理词元，可在固定长度下比较与像素词元的空间一致性。

<a id="paper-hicogen-decaying-stochasticity"></a>

## HiCoGen: Hierarchical Compositional Text-to-Image Generation in Diffusion Models via Reinforcement Learning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_HiCoGen_Hierarchical_Compositional_Text-to-Image_Generation_in_Diffusion_Models_via_Reinforcement_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yang_HiCoGen_Hierarchical_Compositional_Text-to-Image_Generation_in_Diffusion_Models_via_Reinforcement_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 少数候选易反复产出近似构图，影响多目标指令的强化反馈。
- **核心创新 / 方法** · 复杂提示拆成子目标逐步合成，训练时用随步数衰减的随机性增强早期探索。
- **Baseline** · 比较整提示生成及不同噪声时序，正文分析噪声分配和候选差异。
- **Benchmark** · 以 HiCoPrompt 和其他组合生成测试验证指令完成、图像一致性等。
- **关键结果 / 消融** · 正文将早期噪声与候选多样性联系起来，实验验证组合生成表现。
- **适用条件 / 局限** · 理论所需的过程条件和实际扩散近似可能有差异，随机性提高也需检查最终保真。

**可复用机制** · 扩散强化学习可把探索噪声更多放在早期决策，评估与固定噪声下的结构覆盖差异。

<a id="paper-nas3r"></a>

## From None to All: Self-Supervised 3D Reconstruction via Novel View Synthesis

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_From_None_to_All_Self-Supervised_3D_Reconstruction_via_Novel_View_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_From_None_to_All_Self-Supervised_3D_Reconstruction_via_Novel_View_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 监督式快速重建依赖位姿及三维标签，未标定视图中的几何与相机联合估计容易不稳定。
- **核心创新 / 方法** · 从未标定位姿和内参的参考图预测深度参数化高斯及相机，使用掩码注意力限制共享骨干的信息流，以目标视图渲染误差训练。
- **Baseline** · 比较 pixelSplat、MVSplat、NoPoSplat、SPFSplat 系列，区分随机初始化和监督先验。
- **Benchmark** · RE10K 和域外 ACID、DL3DV 等两视图数据；报告新视角 PSNR、SSIM、LPIPS 及位姿 AUC。
- **关键结果 / 消融** · 表2–3显示无监督先验下与所测自监督方法相比取得较好渲染及位姿结果。
- **适用条件 / 局限** · 仍依赖多视图有可辨的共视区域和光度证据；动态物体与反光区域可能破坏约束。

**可复用机制** · 没有相机参数标注时，让几何和相机预测共用骨干，由目标视图的重投影误差同时监督。

<a id="paper-retimegs"></a>

## RetimeGS: Continuous-Time Reconstruction of 4D Gaussian Splatting

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_RetimeGS_Continuous-Time_Reconstruction_of_4D_Gaussian_Splatting_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_RetimeGS_Continuous-Time_Reconstruction_of_4D_Gaussian_Splatting_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 逐帧训练时，重建质量好不保证任意两个帧之间的插值无重影。
- **核心创新 / 方法** · 显式建模高斯的时间行为，用光流初始化及监督，并结合三次渲染监督约束插帧。
- **Baseline** · 表1对照既有时变高斯方法；表2分别移除或替换运动约束。
- **Benchmark** · 在含快速运动、非刚体变形及遮挡的数据上测试连续帧，含 Stage-Capture；报告 PSNR、SSIM 等，另外计算前景质量。
- **关键结果 / 消融** · 表1给出连续时刻质量改善，表2检验去掉组件后前景插值变化。
- **适用条件 / 局限** · 依赖运动估计和可观察性，极端遮挡或急剧运动仍可能使中间状态不确定。

**可复用机制** · 拟合动态高斯场景时，用连续时间参数化和中间时刻监督缓解离散帧拟合的混叠。

<a id="paper-mv3dis-3d-guided-masks"></a>

## MV3DIS: Multi-View Mask Matching via 3D Guides for Zero-Shot 3D Instance Segmentation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_MV3DIS_Multi-View_Mask_Matching_via_3D_Guides_for_Zero-Shot_3D_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_MV3DIS_Multi-View_Mask_Matching_via_3D_Guides_for_Zero-Shot_3D_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · SAM 逐图产生的掩码在视点变化时不一致，直接合并会碎裂或错误连接实例。
- **核心创新 / 方法** · 用粗三维分段建立跨视图掩码关联，以覆盖分布整合，再细化实例；深度一致性用于遮挡下的可靠性权重。
- **Baseline** · 对照既有利用 SAM 的零样本或开放词汇三维分割方案，并检查掩码匹配与深度权重。
- **Benchmark** · ScanNetV2、ScanNet200、ScanNet++、Replica、Matterport3D，用三维实例分割 AP 等指标。
- **关键结果 / 消融** · 作者报告多个数据集上的实例分割改善，并分析多视角匹配与深度权重。
- **适用条件 / 局限** · 需要可靠的几何、相机对齐与粗分段；漏掉掩码和薄结构时有效证据仍可能不足。

**可复用机制** · 从二维分割融合三维实例时，用同一个粗三维分段配准各视图掩码，并按深度一致性定权。

<a id="paper-invad-latent-inversion"></a>

## InvAD: Inversion-based Reconstruction-Free Anomaly Detection with Diffusion Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Sakai_InvAD_Inversion-based_Reconstruction-Free_Anomaly_Detection_with_Diffusion_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Sakai_InvAD_Inversion-based_Reconstruction-Free_Anomaly_Detection_with_Diffusion_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 生成式异常检测需要调噪声强度，还需反复去噪才能得到重建误差。
- **核心创新 / 方法** · 用少步 DDIM 反演将输入映到最终潜变量，直接计算其偏离已知先验的程度。
- **Baseline** · 表1–2与扩散重建类及其他统一异常检测方法对照，分别比较函数求值次数和检测指标。
- **Benchmark** · MVTecAD、VisA、MPDD 等，包含多类无监督设置，比较图像与像素级 AUROC 等。
- **关键结果 / 消融** · 表2报告三个数据集的图像级指标整体较强，像素级与重建类方法接近；表1描述较少反演步数。
- **适用条件 / 局限** · 对先验敏感，成像域变化也可能被计为异常；潜空间分辨率限制微小缺陷定位。

**可复用机制** · 用扩散模型做异常分数时，检验反演潜变量偏离先验能否取代往返像素重建。

<a id="paper-log-linear-sparse-attention"></a>

## Trainable Log-linear Sparse Attention for Efficient Diffusion Transformers

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhou_Trainable_Log-linear_Sparse_Attention_for_Efficient_Diffusion_Transformers_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhou_Trainable_Log-linear_Sparse_Attention_for_Efficient_Diffusion_Transformers_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 单级 Top-K 在候选块增多时筛选仍有平方成本，固定预算也会削弱长序列覆盖。
- **核心创新 / 方法** · 递归从粗到细选块，将不同分辨率的键值组合补充全局信息；训练和推理使用稀疏索引。
- **Baseline** · 对照其他可训练 Top-K 稀疏注意力，表1改变分层选择及键值补充。
- **Benchmark** · FFHQ-128/256 与 PixelFlow ImageNet-256 像素生成，报告 FID、IS 和吞吐。
- **关键结果 / 消融** · 论文将注意力及选择整体降至对数线性，表2–3测短训练下生成分数与训练吞吐。
- **适用条件 / 局限** · 收益依赖空间信息能被分块层次覆盖，也依赖稀疏 GPU 内核；孤立远程细节可能漏选。

**可复用机制** · 长视觉序列不止稀疏注意力，还要把块筛选做成多层细化，并保留未选区域的粗粒度上下文。

<a id="paper-placid-synthetic-trajectories"></a>

## PLACID: Identity-Preserving Multi-Object Compositing via Video Diffusion with Synthetic Trajectories

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Tarres_PLACID_Identity-Preserving_Multi-Object_Compositing_via_Video_Diffusion_with_Synthetic_Trajectories_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Tarres_PLACID_Identity-Preserving_Multi-Object_Compositing_via_Video_Diffusion_with_Synthetic_Trajectories_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 直接多对象合成容易改外观、漏物体或重复对象，静态监督难复用视频模型的跟踪能力。
- **核心创新 / 方法** · 从对象参考图合成平滑摆位序列，微调图生视频模型并以终帧完成组合。
- **Baseline** · 原文比较基础模型、同数据微调、增加对象与背景条件等路径。
- **Benchmark** · 用 ABO 等对象构建多物体合成，评估身份、布局和背景保真度。
- **关键结果 / 消融** · 表2对照数据微调与条件注入的贡献，正文报告多对象保留和位置控制改善。
- **适用条件 / 局限** · 合成轨迹不能表示任意遮挡与相互作用，终帧质量还依赖视频模型的持续身份一致性。

**可复用机制** · 训练视频模型做静态组合时，将初始随机摆放过渡到目标布局，复用时序一致性来保留各实体。

<a id="paper-omnizip-audio-guided-pruning"></a>

## OmniZip: Audio-Guided Dynamic Token Compression for Fast Omnimodal Large Language Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Tao_OmniZip_Audio-Guided_Dynamic_Token_Compression_for_Fast_Omnimodal_Large_Language_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Tao_OmniZip_Audio-Guided_Dynamic_Token_Compression_for_Fast_Omnimodal_Large_Language_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 联合音视频输入很长；全局均匀压缩可能丢掉短时跨模态事件。
- **核心创新 / 方法** · 按时窗估计音频保留率和跨模态关联，据此给视频词元分配更高或更低的预算，窗口内交错做时空压缩。
- **Baseline** · 比较 FastV、DyCoke、全词元和不同保留率配置。
- **Benchmark** · WorldSense 等音视频问答，测任务分数、预填充时延、显存和整次推理时间。
- **关键结果 / 消融** · 表 3 的 3B 模型减至 45% 时，预填从 258 ms 降到 104 ms，端到端从 3.61 秒降到 2.86 秒，任务分由 46.4 降到 45.2。
- **适用条件 / 局限** · 依赖音频能反映视觉事件；静音动作、无关声源和音画错位条件应分开验收。

**可复用机制** · 音视频长上下文压缩可按音频事件时窗调节视频预算，并同时报告预填充与端到端延迟。见表 3–4。

<a id="paper-3dthinker-distilled-geometry"></a>

## Think with 3D: Geometric Imagination Grounded Spatial Reasoning from Limited Views

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Think_with_3D_Geometric_Imagination_Grounded_Spatial_Reasoning_from_Limited_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_Think_with_3D_Geometric_Imagination_Grounded_Spatial_Reasoning_from_Limited_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 少量视图的空间问答依赖隐含三维结构，文字链和外部先验各有表达或部署成本。
- **核心创新 / 方法** · 监督对齐视觉语言模型推理期间的三维潜表示和几何基础模型表示，再用结果信号调整整段推理。
- **Baseline** · 比较 Ego3D-VLM 的推理外部先验、普通问答微调和思维链微调。
- **Benchmark** · Ego3D-Bench、MindCube-Tiny 和其他空间理解基准，按技能测准确率。
- **关键结果 / 消融** · 表 3 Qwen2.5-VL-3B 为 50.8 对 Ego3D-VLM 的 44.4；InternVL3-38B 两者均为 68.0。
- **适用条件 / 局限** · 需可取得训练用几何教师及覆盖良好的有限视图；离线空间问答不能证明生成了物理一致的内部地图。

**可复用机制** · 只在训练能获得昂贵三维教师时，可蒸馏中间几何表示并在推理时移除教师；与推理调用深度先验比较。见表 3–4。

<a id="paper-difference-of-gaussians-primitives"></a>

## Prune Wisely, Reconstruct Sharply: Compact 3D Gaussian Splatting via Adaptive Pruning and Difference-of-Gaussian Primitives

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Prune_Wisely_Reconstruct_Sharply_Compact_3D_Gaussian_Splatting_via_Adaptive_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_Prune_Wisely_Reconstruct_Sharply_Compact_3D_Gaussian_Splatting_via_Adaptive_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 大量高斯保存细节但使模型过大，简单删除基元易使边缘模糊。
- **核心创新 / 方法** · 按重建质量决定剪枝及细化时机，并用包含正、负密度的三维高斯差原语补足有限基元的表达。
- **Baseline** · 比较 3DGS、逐项加入剪枝/细化、以及追加高斯差的版本。
- **Benchmark** · Mip-NeRF360、Deep Blending 等新视图，测 PSNR、SSIM、LPIPS、训练时间与渲染 FPS。
- **关键结果 / 消融** · 表 2 的最终高斯差组件将 PSNR 从 26.99 提到 27.16，但 FPS 从 361.9 降到 289.0；普通 3DGS 是 27.47 和 143.5。
- **适用条件 / 局限** · 紧凑表达的收益随显卡和场景分布变化，负密度原语与原有渲染管线兼容性需复核。

**可复用机制** · 三维高斯压缩在边缘质量下降时，可对照同剪枝配置下用正负联合原语增强表达。见表 2。

<a id="paper-ideal-noise-correction-failure"></a>

## Deconstructing the Failure of Ideal Noise Correction: A Three-Pillar Diagnosis

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Feng_Deconstructing_the_Failure_of_Ideal_Noise_Correction_A_Three-Pillar_Diagnosis_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Feng_Deconstructing_the_Failure_of_Ideal_Noise_Correction_A_Three-Pillar_Diagnosis_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 噪声校正的理论一致性没有解释有限样本训练中的性能下降，常见归因是转移矩阵估计不准确。
- **核心创新 / 方法** · 用 oracle 转移矩阵观察训练退化，再区分优化动态、收敛解和标注信息量；对照理想干净筛选。
- **Baseline** · 比较估计及真值矩阵校正、理想干净样本筛选与正则化校正。
- **Benchmark** · 模拟噪声与 Clothing1M 等，记录测试准确率和校准误差；图 3 比较每个样本 1 到 10 份标签。
- **关键结果 / 消融** · 提供真矩阵时仍可出现性能退化；增加每样本标签数使校正法逐渐接近理想筛选，校准误差还可更低。
- **适用条件 / 局限** · oracle 矩阵在真实问题中通常不可得，结论依赖所测噪声机制及任务；需分开验证样本依赖噪声。

**可复用机制** · 标签噪声校正实验先用真值转移矩阵排除估计误差，再分别检查训练轨迹与每样本标签信息。见 §5.3、图 3。

<a id="paper-md-mixer-spiking-temporal-delays"></a>

## Temporal Interaction in Spiking Transformers with Multi-Delay Mixer

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Shi_Temporal_Interaction_in_Spiking_Transformers_with_Multi-Delay_Mixer_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Shi_Temporal_Interaction_in_Spiking_Transformers_with_Multi-Delay_Mixer_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 脉冲 Transformer 的空间注意力通常独立处理各时刻，难形成多种时间依赖。
- **核心创新 / 方法** · 用多种延迟混合进入空间注意力的脉冲，并用 Temporal Interaction Coefficient 检查时刻间相互作用。
- **Baseline** · 在 Spikformer、QKFormer、Spike-driven Transformer 中对照原模块、TIM 和 STAtten。
- **Benchmark** · 包括 ImageNet、CIFAR10-DVS、N-Caltech101、UCF101-DVS 等，测分类准确率和算子成本。
- **关键结果 / 消融** · 表 2 Spikformer 的 CIFAR10-DVS/N-Caltech101 从 80.90/80.23 升至 83.37/84.57；STAtten 为 82.40/83.12。
- **适用条件 / 局限** · 不同采样速率或延迟预算会改变最佳混合方式；理论运算效率需在目标神经形态硬件上另测。

**可复用机制** · 事件驱动 Transformer 可在空间注意力前混合不同延迟的脉冲，并用跨时刻依赖测量确认是否超出逐帧空间处理。见表 2–3。

<a id="paper-g2rpo-stepwise-preference"></a>

## Fine-Grained GRPO for Precise Preference Alignment in Flow Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhou_Fine-Grained_GRPO_for_Precise_Preference_Alignment_in_Flow_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhou_Fine-Grained_GRPO_for_Precise_Preference_Alignment_in_Flow_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 对全轨迹仅提供终局奖励时，有用的去噪方向难与局部无效方向区分。
- **核心创新 / 方法** · 以细粒度的随机去噪探索产生局部对照，再把多个偏好指标形成可用于策略更新的局部优势。
- **Baseline** · 比较 DanceGRPO、MixGRPO，消融多指标优势组合与不同去噪粒度。
- **Benchmark** · 文生图偏好训练，报告 HPS、CLIP、PickScore、ImageReward 和统一奖励等。
- **关键结果 / 消融** · 表 1 在 HPS 与 CLIP 奖励设置中，完整 G2RPO 的 ImageReward 为 1.483，去多指标优势组合为 1.421；MixGRPO 为 1.436。
- **适用条件 / 局限** · 需要偏好打分和足够训练样本，多个代理指标仍可能同源；换骨干或人评需独立检验局部信用分配。

**可复用机制** · 流模型偏好训练可把噪声搜索限制在可比较的局部去噪步骤，并对多个偏好维度分开衡量。见表 1–3。

<a id="paper-paparazzo"></a>

## Paparazzo: Active Mapping of Moving 3D Objects

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Allegro_Paparazzo_Active_Mapping_of_Moving_3D_Objects_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Allegro_Paparazzo_Active_Mapping_of_Moving_3D_Objects_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 静态场景的选视角策略不能补偿目标运动，可能重复观察已建区域。
- **核心创新 / 方法** · 在物体运动预测下评估视角信息量，再规划观测路径。
- **Baseline** · 正文表1–2对照随机行走、随机视角及只追踪目标的策略。
- **Benchmark** · 在四类运动和多个场景与物体上报告覆盖、完整性误差与 AUC。
- **关键结果 / 消融** · 表2前后移动情形，Paparazzo 平均覆盖67.73%，只追踪为62.05%，完整性误差为1.23与1.45厘米。
- **适用条件 / 局限** · 运动预测错误或遮挡会破坏视角选择，当前证据依赖所设运动类别及仿真场景。

**可复用机制** · 主动重建动态物体时，依据预测轨迹选择能补足覆盖的未来视角。

<a id="paper-drivegatr"></a>

## Efficient Equivariant Transformer for Self-Driving Agent Modeling

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_Efficient_Equivariant_Transformer_for_Self-Driving_Agent_Modeling_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_Efficient_Equivariant_Transformer_for_Self-Driving_Agent_Modeling_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 成对相对位置编码会给多实体建模增加额外二次开销。
- **核心创新 / 方法** · 以二维射影几何代数多向量表示场景元素，在网络层保持平面旋转和平移等变。
- **Baseline** · 表2–3比较普通 Transformer、相对位置编码和 DriveGATr 及多模型规模。
- **Benchmark** · WOSAC 2024 验证集，报告 RMM、运动学、交互、地图和 minADE。
- **关键结果 / 消融** · 相同3M参数时 DriveGATr 的 RMM 为0.7620，普通 Transformer 为0.7257，相对位置编码为0.7251。
- **适用条件 / 局限** · 保证针对平面变换，标准注意力本身仍有计算开销。开放三维环境需要重新验证对称条件。

**可复用机制** · 以几何代数编码各实体以实现平面刚体变换等变性，单独核查成对位置编码的计算代价。

<a id="paper-tre-spiking"></a>

## Temporal Representation Enhancement (TRE): Learning to Forget Dominant Patterns for Enhanced Temporal Spiking Features

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_Temporal_Representation_Enhancement_TRE_Learning_to_Forget_Dominant_Patterns_for_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_Temporal_Representation_Enhancement_TRE_Learning_to_Forget_Dominant_Patterns_for_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 静态监督在各时间步反复鼓励同一响应，浪费动态模型的表示容量。
- **核心创新 / 方法** · 累计类别相关特征贡献，按动态门控减弱过度占优模式。
- **Baseline** · 对照无附加目标、TET 和固定 Top-k 门控。
- **Benchmark** · CIFAR-100、ImageNet、DVS-CIFAR10。正文表3–5报告不同时间步准确率及跨步特征相似度。
- **关键结果 / 消融** · 表3在 CIFAR-100 四步下为81.27%，TET 为80.16%；在 DVS-CIFAR10 十步下为83.60%和83.00%。
- **适用条件 / 局限** · 有效性依赖类别贡献估计及步长，门控也可能压低真正关键证据。

**可复用机制** · 时序表征易重复同一判别线索时，可训练时抑制长期占优响应，再测不同时步是否互补。

<a id="paper-dtr-safe-token-reweighting"></a>

## Dynamic Token Reweighting for Robust Vision-Language Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Jiang_Dynamic_Token_Reweighting_for_Robust_Vision-Language_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Jiang_Dynamic_Token_Reweighting_for_Robust_Vision-Language_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 引入防护有时会降低正常任务性能或显著拉长推理时间。
- **核心创新 / 方法** · DTR 在模型内部自适应调整视觉词元权重，以弱化异常视觉证据并保持正常推理。
- **Baseline** · 比较原模型及 AdaShield、CoCA、ShiftDC 等防御。
- **Benchmark** · 表1评安全表现，表2在 MM-Vet 测正常任务，表3测平均推理时延。
- **关键结果 / 消融** · 表3 DTR 为4.01秒，原模型3.65秒，AdaShield 5.24秒；正文同时报告防护及正常任务对照。
- **适用条件 / 局限** · 推理干预需要内部缓存访问，安全收益应在模型、任务和部署条件变化后复测。

**可复用机制** · 部署视觉语言防护时，同时检查推理干预对防御可靠性、正常视觉任务与时延的影响。

<a id="paper-chorus-3dgs"></a>

## Chorus: Multi-Teacher Pretraining for Holistic 3D Gaussian Scene Encoding

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Chorus_Multi-Teacher_Pretraining_for_Holistic_3D_Gaussian_Scene_Encoding_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Chorus_Multi-Teacher_Pretraining_for_Holistic_3D_Gaussian_Scene_Encoding_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 三维高斯原语能很好渲染，却不自带通用理解所需特征。
- **核心创新 / 方法** · 蒸馏语言对齐、通用和对象级教师，以教师专属投影保留互补信号。
- **Baseline** · 比较 Sonata、PTv3、PPT 等方法和不同探针配置；另训练点云版。
- **Benchmark** · 表1–5覆盖 ScanNet++、Matterport3D、ScanNet 等开放词表分割、三维问答与少标注评测。
- **关键结果 / 消融** · 表5显示在多个标签预算下可通过微调接近或超越所列对照，线性探针和微调分开报告。
- **适用条件 / 局限** · 二维教师意见可能冲突，训练需要可靠二维到三维对齐，新传感器数据应独立验收。

**可复用机制** · 共享三维编码器接受不同二维教师的专属投影，并以少标注探针检查语义和实例细节能否共存。

<a id="paper-residual-diffusion-bridge"></a>

## Residual Diffusion Bridge Model for Image Restoration

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Residual_Diffusion_Bridge_Model_for_Image_Restoration_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_Residual_Diffusion_Bridge_Model_for_Image_Restoration_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 全局加噪会破坏原输入完好区域，现有扩散桥也难在统一设置下比较。
- **核心创新 / 方法** · 推导通用前向与反向扩散桥，并利用端点分布残差分配噪声；常见桥可表达为特定配置。
- **Baseline** · 表1讨论 I2SB、ColdDiffusion 等，表2对照通用和任务专用修复方法。
- **Benchmark** · 五种图像修复任务，以恢复质量和256×256推理 FLOPs 比较。
- **关键结果 / 消融** · 表2报告多任务质量与成本，表3对照不同噪声调度。
- **适用条件 / 局限** · 可迁移性取决于残差能否定位需修复内容，颜色漂移等全局退化收益可能不同。

**可复用机制** · 当输入多数位置无需改变时，用端点残差调制扩散桥的加噪与恢复强度。

<a id="paper-rewis3d"></a>

## Rewis3d: Reconstruction Improves Weakly-Supervised Semantic Segmentation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Ernst_Rewis3d_Reconstruction_Improves_Weakly-Supervised_Semantic_Segmentation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Ernst_Rewis3d_Reconstruction_Improves_Weakly-Supervised_Semantic_Segmentation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 稀疏标注便宜但像素覆盖低，逐帧学习无法共享同一表面的语义证据。
- **核心创新 / 方法** · 以快速前馈重建生成三维点，双教师学生训练对齐三维点与二维投影语义，并抑制不可靠点。
- **Baseline** · 同骨干 EMA 基线、稀疏监督已有方案、全监督参照。
- **Benchmark** · Waymo、KITTI-360、Cityscapes、NYUv2 等，用 mIoU 及缩小全监督差距比例评价；测试不同稀疏标注。
- **关键结果 / 消融** · 作者报告相对现有方案提高2–7%，不增加部署开销；Waymo 消融从49.4 mIoU 的 EMA 基线比较。
- **适用条件 / 局限** · 需要训练视频的可重建几何，失配、动态和稀疏共视会传播错误。

**可复用机制** · 训练稀疏标注分割时，把视频可重建三维点云用作跨视图语义传播，部署仍只用二维模型。

<a id="paper-sympl"></a>

## Keep it SymPL: Symbolic Projective Layout for Allocentric Spatial Reasoning in Vision-Language Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Jang_Keep_it_SymPL_Symbolic_Projective_Layout_for_Allocentric_Spatial_Reasoning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Jang_Keep_it_SymPL_Symbolic_Projective_Layout_for_Allocentric_Spatial_Reasoning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 模型能回答观察者视角问题，但换成物体视角后参考系易混。
- **核心创新 / 方法** · 将物体和视角投影到符号布局，依次抽象、分区和定位，再交给 VLM 作答。
- **Baseline** · 原图直接问答与布局转换、各因素消融比较。
- **Benchmark** · 物体中心及观察者中心空间问答，并正面测试视觉错觉和多视图；指标为回答正确性。
- **关键结果 / 消融** · 表1–3报告两种参考视角均有改善，对错觉和多视图也更稳。
- **适用条件 / 局限** · 场景对象识别、参考物朝向或投影出错会传递到符号答案。

**可复用机制** · 物体中心视角推理时，先显式变换参考系并以符号布局缩短视觉推导。

<a id="paper-portable-active-learning-detection"></a>

## Portable Active Learning for Object Detection

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Sharma_Portable_Active_Learning_for_Object_Detection_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Sharma_Portable_Active_Learning_for_Object_Detection_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 依赖隐层或者修改训练的主动学习难迁移到不同检测器。
- **核心创新 / 方法** · 训练轻量类别逻辑分类器区分框的真假匹配，用熵排样本，再用类别覆盖、图像熵和相似度筛选批次。
- **Baseline** · PPAL、随机采样等；在 RetinaNet、YOLOX-Tiny 等检测器上比较。
- **Benchmark** · COCO、PASCAL VOC、BDD100K 多轮主动学习，报告 AP、mAP 和达到相近表现所需标注。
- **关键结果 / 消融** · 表1–3给出不同检测器及基准的标签效率和检测指标改善。
- **适用条件 / 局限** · 初始标注中类别过少会使分类器校准不稳；框坐标和分数仍须可见。

**可复用机制** · 不能读取检测器内部时，用输出框的类别校准不确定性和输入多样性选标注批次。

<a id="paper-lasar-cognitive-map"></a>

## LASAR: Towards Spatio-temporal Reasoning with Latent Cognitive Map

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Tang_LASAR_Towards_Spatio-temporal_Reasoning_with_Latent_Cognitive_Map_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Tang_LASAR_Towards_Spatio-temporal_Reasoning_with_Latent_Cognitive_Map_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 成功复现专家路径不代表能编码跨片段空间关系，距离和拓扑缺少明确监督。
- **核心创新 / 方法** · 双记忆分别记录经历与认知地图，使用仿真时空标注构造认知问答对比样本。
- **Baseline** · 表1和基础导航、推理方法对照；表2去掉语义记忆等组件。
- **Benchmark** · MindCraft 测双负载推理，R2R/RxR 测导航，VSI-Bench 测零样本空间推理。
- **关键结果 / 消融** · 作者报告导航/空间推理零样本收益约2–3.5%，表2分析记忆组件。
- **适用条件 / 局限** · 依赖仿真提示覆盖所需空间关系，存在可迁移仿真和真实环境差距。

**可复用机制** · 训练导航智能体时分开存情节记忆和语义地图，再用关系对比目标直接约束地图。

<a id="paper-dream-prototype-memory"></a>

## DREAM: Document Recognition with Explicit Adaptive Memory

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_DREAM_Document_Recognition_with_Explicit_Adaptive_Memory_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_DREAM_Document_Recognition_with_Explicit_Adaptive_Memory_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 隐式权重难显式复用局部字体、布局与边界模式。
- **核心创新 / 方法** · 局部区域稀疏检索不同分辨率下的原型，并将检索结果和视觉特征一同解码；由注意力加权 EMA 更新原型，以正则阻止坍塌。
- **Baseline** · 原文比较无新增原型的编码解码器和文档/手写识别方法。
- **Benchmark** · Fox、DreamDoc 及 SCUT-HCCDoc、SCUT-EPT，检验文档识别和手写识别表现。
- **关键结果 / 消融** · 原文各基准表报告对照识别指标提升，说明模块可以接入不同编码解码设置。
- **适用条件 / 局限** · 新域版式缺少重复模式时原型收益可能下降，显著分布变化时需重学记忆。

**可复用机制** · 文档识别反复遇到相似版式时，可为局部视觉块添加多尺度原型记忆。

<a id="paper-yose-essential-tokens"></a>

## YOSE: You Only Select Essential Tokens for Efficient DiT-based Video Object Removal

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_YOSE_You_Only_Select_Essential_Tokens_for_Efficient_DiT-based_Video_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wu_YOSE_You_Only_Select_Essential_Tokens_for_Efficient_DiT-based_Video_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 小掩码也跑全时空网格浪费计算，直接删掉背景则降低前景时序一致性。
- **核心创新 / 方法** · 可微批内变长索引选取关键 token，DiffSim 近似背景在注意力中的贡献。
- **Baseline** · MiniMax Remover 等原始去物方法，表2消融 DiffSim 和融合。
- **Benchmark** · 视频物体移除评测，用 VBench 和背景保真指标，另测480p帧率及掩码比例变化。
- **关键结果 / 消融** · 文中报告约20%掩码区域时达到约25 FPS，MiniMax Remover 约10 FPS；表2检验近似路径。
- **适用条件 / 局限** · 优势取决于掩码面积与背景可近似性，广域编辑或图外互相作用可能降低收益。

**可复用机制** · 局部视频编辑只计算掩码内关键 token，并用低成本路径近似掩码外上下文影响。

<a id="paper-geoint-verified-auxiliary-geometry"></a>

## Geoint-R1: Formalizing Multimodal Geometric Reasoning with Dynamic Auxiliary Constructions

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wei_Geoint-R1_Formalizing_Multimodal_Geometric_Reasoning_with_Dynamic_Auxiliary_Constructions_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wei_Geoint-R1_Formalizing_Multimodal_Geometric_Reasoning_with_Dynamic_Auxiliary_Constructions_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 最终几何答案正确也可能掩盖辅助线构造错误，视觉描述难以直接验真。
- **核心创新 / 方法** · 模型根据图文产生辅助几何元素，在 Lean4 表示中做形式推理，并用验证和课程学习训练。
- **Baseline** · 比较去 Verify、去强化学习、去课程学习，以及现有多模态与数学模型。
- **Benchmark** · Geoint 共 1,885 道平面、空间及立体几何题；分答案题和证明题、有无辅助构造报告准确率。
- **关键结果 / 消融** · 表 4 辅助构造答案题完整模型 68.63%，去验证为 32.35%，证明题对应 68.40% 与 64.15%。
- **适用条件 / 局限** · 形式验证依赖题意成功形式化，形式系统内的正确性不能弥补输入图形歧义或假设遗漏。

**可复用机制** · 视觉几何证明可把辅助构造作为程序可验的中间步骤，并单独比较需要与不需要辅助线的题。见表 3–4。

<a id="paper-nrmf-motion-distance-fields"></a>

## Geometric Neural Distance Fields for Learning Human Motion Priors

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yu_Geometric_Neural_Distance_Fields_for_Learning_Human_Motion_Priors_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yu_Geometric_Neural_Distance_Fields_for_Learning_Human_Motion_Priors_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 逐帧姿态先验可输出合理静态姿势，但拼起来未必时序连续或接触可信。
- **核心创新 / 方法** · 在关节旋转、角速度和角加速度的乘积空间学习神经距离场，用几何投影及积分恢复运动。
- **Baseline** · 对照 HuMoR、RoHM、MDM、PoseNDF 组合和 Motion-NDF。
- **Benchmark** · AMASS 训练，测含噪三维、部分三维与 3DPW 二维拟合，并报告关节位置和运动指标。
- **关键结果 / 消融** · 表 1 去噪位置误差 NRMF 为 16.4 mm、NRDF+T-NRDF 为 16.7、RoHM 为 20.9；加速度误差分别为 2.25、2.97、2.61。
- **适用条件 / 局限** · 依赖运动先验覆盖目标形态，优化可能付出迭代成本；人体关节几何不能直接替代机器人动力学或力约束。

**可复用机制** · 拟合含噪或局部人体运动可把旋转、速度和加速度分别作为可投影的几何先验，并同时测位置和运动误差。见表 1–3。

<a id="paper-farmer-likelihood-latent-partition"></a>

## FARMER: Flow AutoRegressive Transformer over Pixels

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zheng_FARMER_Flow_AutoRegressive_Transformer_over_Pixels_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zheng_FARMER_Flow_AutoRegressive_Transformer_over_Pixels_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 逐个自回归连续像素使序列过长；外部压缩可能失去完整像素似然。
- **核心创新 / 方法** · 用可逆流把图像转成序列，学习划分信息性与冗余潜通道，由自回归模型重点建模前者。
- **Baseline** · 对照去掉降维、不同流结构和朴素 CFG，另外比较重采样 CFG。
- **Benchmark** · ImageNet 256×256 类条件生成，报告 FID、IS 与速度，并评估似然建模设置。
- **关键结果 / 消融** · 表 2 单加入潜通道降维使 FID 从 61.17 降到 49.29，IS 从 22.10 到 30.61；其他采样改动另测。
- **适用条件 / 局限** · 可逆变换及通道独立近似仍影响计算和似然，需要在复杂条件或高分辨率上验证真实开销。

**可复用机制** · 可逆像素生成可把信息性潜通道与冗余通道拆开建模，在显式似然与自回归计算之间做比较。见表 2。

<a id="paper-cccaption-symmetric-visual-rewards"></a>

## CCCaption: Dual-Reward Reinforcement Learning for Complete and Correct Image Captioning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Tang_CCCaption_Dual-Reward_Reinforcement_Learning_for_Complete_and_Correct_Image_Captioning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Tang_CCCaption_Dual-Reward_Reinforcement_Learning_for_Complete_and_Correct_Image_Captioning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 人工参考常遗漏事实，单一匹配分数会把更完整的描述误判或无意奖励虚构。
- **核心创新 / 方法** · 从图像生成问题估计覆盖，从生成描述拆出待验证断言估计正确，再联合强化学习。
- **Baseline** · 比较基座 Qwen3-VL-2B、CapRL 和其他图文描述器。
- **Benchmark** · CapArena、Prism 多任务转问答评估与专门的描述幻觉评估。
- **关键结果 / 消融** · 表 2 CCCaption-2B 的 Prism 平均 70.57，基座 70.19；Hallusion 项为 76.72，基座 77.51，收益并非所有维度同步。
- **适用条件 / 局限** · 两边事实核验都依赖自动评审能力，复用时应报告标注者一致性并处理不可视、模糊和遗漏事实。

**可复用机制** · 描述生成奖励可分开计来自图像的事实覆盖和来自文本的事实真实性，避免单边奖励鼓励遗漏或编造。见表 2–3。

<a id="paper-linvideo-selective-linear-attention"></a>

## LinVideo: A Post-Training Framework towards O(n) Attention in Efficient Video Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_LinVideo_A_Post-Training_Framework_towards_On_Attention_in_Efficient_Video_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_LinVideo_A_Post-Training_Framework_towards_On_Attention_in_Efficient_Video_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 把预训练视频扩散的注意力全改为线性计算会破坏时空生成结构，又难以承担重训。
- **核心创新 / 方法** · 选择性逐步替换部分二次注意力，用任意去噪时刻的分布匹配做免真实训练数据的后训练。
- **Baseline** · 比较同层手工一次替换、启发式网格搜索选择，以及用 MSE 或单纯分布匹配的版本。
- **Benchmark** · VBench 的成像、美学、平滑度、动态度、整体一致性等；另对比转换层预算。
- **关键结果 / 消融** · 表 3 完整方法整体一致性 26.52，手工 20.08、启发式 18.94；成像质量分别为 66.07、62.97、60.74。
- **适用条件 / 局限** · 线性转换比例越高会损失质量；依赖教师样本和骨干表达能力，应核对最终画质及真实墙钟加速。

**可复用机制** · 后训练转换视频注意力时可逐步选择容易替换的层，同时让学生在不同去噪时刻贴近教师。见表 3–4。

<a id="paper-affordance-geometry-interaction-probing"></a>

## Probing and Bridging Geometry-Interaction Cues for Affordance Reasoning in Vision Foundation Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Probing_and_Bridging_Geometry-Interaction_Cues_for_Affordance_Reasoning_in_Vision_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Probing_and_Bridging_Geometry-Interaction_Cues_for_Affordance_Reasoning_in_Vision_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 部件可见不等于部件可用于指定动作，纯几何或纯交互提示各会产生误定位。
- **核心创新 / 方法** · 从 DINO 取部件几何原型，从 Flux 取动词条件注意力，组合成训练免除的可供性图。
- **Baseline** · 比较只用交互图与几何交互联合，并对照 LOCATE 和 Affordance-R1。
- **Benchmark** · AGD20K 的零样本可供性定位，报告 KLD、SIM 和 NSS。
- **关键结果 / 消融** · 表 2 联合相对于仅交互的 KLD 从 1.825 到 1.493，SIM 从 0.271 到 0.326；LOCATE 的 SIM 仍为 0.372。
- **适用条件 / 局限** · 依赖几何与动词响应对齐，可供性热图是候选接触区，需用真实动作验证可达性和力学可行性。

**可复用机制** · 无动作标签的可供性定位可把部件几何和动词条件热图作为两路证据，再与单路探针对照。见表 2。

<a id="paper-vita-shared-action-vision-latents"></a>

## Unifying Perception and Action: A Hybrid-Modality Pipeline with Implicit Visual Chain-of-Thought for Robotic Action Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Ma_Unifying_Perception_and_Action_A_Hybrid-Modality_Pipeline_with_Implicit_Visual_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Ma_Unifying_Perception_and_Action_A_Hybrid-Modality_Pipeline_with_Implicit_Visual_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 文字推理遗漏感知细节；未来画面和低层控制分别预测时，两路梯度也可能争用容量。
- **核心创新 / 方法** · 以共享离散空间共同编码视觉与动作，自回归预测的词元可分别解码未来帧与动作序列。
- **Baseline** · 比较 DeFI、UniVLA、CoT-VLA 等，实机另与 Pi0、OpenVLA、GR00T N1.5 对照。
- **Benchmark** · CALVIN 连续五条命令、LIBERO、SimplerEnv，以及 UR-5e 桌面任务的域内外设置。
- **关键结果 / 消融** · 表 1 CALVIN 完成连续五个任务的比例为 84.5%，DeFI 为 81.2%，UniVLA 为 75.1%。
- **适用条件 / 局限** · 需要动作与视频时序对齐，共享词元未必能表示短时接触或遮挡中的关键状态；结果应在不同机械臂和控制频率复测。

**可复用机制** · 机器人策略可测试让动作与未来图像共用离散词元，并用同一分段的两路监督对照仅动作目标。见 §4 与消融。

<a id="paper-eagc-gcd"></a>

## The Devil Is in Gradient Entanglement: Energy-Aware Gradient Coordinator for Robust Generalized Category Discovery

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zheng_The_Devil_Is_in_Gradient_Entanglement_Energy-Aware_Gradient_Coordinator_for_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zheng_The_Devil_Is_in_Gradient_Entanglement_Energy-Aware_Gradient_Coordinator_for_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 联合训练会改变有标注梯度并使新旧类表征重叠。
- **核心创新 / 方法** · 用锚点校正梯度方向，并按能量调整弹性投影。
- **Baseline** · 与既有类别发现方法及单独使用各机制的配置比较。
- **Benchmark** · 表1–4报告已知类、未知类及总准确率，另测梯度偏离系数。
- **关键结果 / 消融** · 正文称完整机制相对两个单组件设计的总准确率分别改善1.6和3.6个百分点。
- **适用条件 / 局限** · 依赖有标注目标可提供可靠锚点，冲突方向在新数据上需重测。

**可复用机制** · 混合有标注与无标注目标时诊断梯度纠缠，再调无标注更新方向。

<a id="paper-matanyone2-mqe"></a>

## MatAnyone 2: Scaling Video Matting via a Learned Quality Evaluator

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_MatAnyone_2_Scaling_Video_Matting_via_a_Learned_Quality_Evaluator_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yang_MatAnyone_2_Scaling_Video_Matting_via_a_Learned_Quality_Evaluator_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 廉价分割标注增加覆盖却缺乏精细透明边缘。
- **核心创新 / 方法** · 学习无需真实 alpha 的逐像素评估信号，以此调在线监督并挑选可靠伪标签。
- **Baseline** · 以 MatAnyone 为基线，表3依次增加评估引导、VMReal 数据与参考帧训练。
- **Benchmark** · YouTubeMatte 1080p 等，报告 MAD、MSE、Grad、dtSSD。
- **关键结果 / 消融** · 表3基线 Grad 为8.91，只加在线引导为8.20，后续组合为7.13。
- **适用条件 / 局限** · 评估器误差会传到数据筛选和训练，半透明或陌生材料需保留人工核查。

**可复用机制** · 把像素级质量评估器同时用于在线监督和离线筛标签，分别验收边缘质量收益。

<a id="paper-vold"></a>

## VOLD: Reasoning Transfer from LLMs to Vision-Language Models via On-Policy Distillation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Bousselham_VOLD_Reasoning_Transfer_from_LLMs_to_Vision-Language_Models_via_On-Policy_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Bousselham_VOLD_Reasoning_Transfer_from_LLMs_to_Vision-Language_Models_via_On-Policy_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 跨模态师生若生成轨迹差异过大，直接用学生采样做教师监督可能没有净收益。
- **核心创新 / 方法** · 先用教师生成的视觉推理样式做冷启动，再在学生在线轨迹上结合 GRPO 与教师蒸馏。
- **Baseline** · 表2对照沿用原 MoT 数据造成的分布失配，表3依次加入 GRPO 和蒸馏。
- **Benchmark** · MMMU-Pro、MMStar、MathVision、MathVista 等八个任务；正文表2–3报告准确率。
- **关键结果 / 消融** · 表3的 MathVision 从仅 SFT 18.6到加 RL 的24.0，再到加蒸馏的28.0；表2指出失配配置下在线蒸馏无额外收益。
- **适用条件 / 局限** · 涉及教师能接收的视觉语义接口，冷启动未过滤轨迹可暂时降低能力。

**可复用机制** · 用纯文本教师在线蒸馏视觉语言策略前，先检查学生是否与教师输出分布对齐。

<a id="paper-fov-net"></a>

## FoV-Net: Rotation-Invariant CAD B-rep Learning via Field-of-View Ray Casting

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Ballegeer_FoV-Net_Rotation-Invariant_CAD_B-rep_Learning_via_Field-of-View_Ray_Casting_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Ballegeer_FoV-Net_Rotation-Invariant_CAD_B-rep_Learning_via_Field-of-View_Ray_Casting_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · CAD 边界模型可能在对齐基准上高度依赖全局坐标和法向。
- **核心创新 / 方法** · 用面局部网格和射线交点表征邻接几何，再沿边界图传播。
- **Baseline** · 对照使用绝对信息的边界表示方法并分别测对齐及旋转输入。
- **Benchmark** · 正文表1–2测 SolidLetters、Fusion360、MFCAD++ 等分类或分割数据，报告准确率和 IoU。
- **关键结果 / 消融** · 正文报告有的方法对齐时超过95%，任意旋转后可降到约10%，并验证局部几何表示。
- **适用条件 / 局限** · 局部坐标定义需稳定，近退化或高度对称面可能仍有表示歧义。

**可复用机制** · 通过面局部坐标系表达边界表示，并用局部射线保留全局几何；评测须包含任意三维旋转。

<a id="paper-videocof"></a>

## VideoCoF: Unified Video Editing with Temporal Reasoner

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_VideoCoF_Unified_Video_Editing_with_Temporal_Reasoner_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yang_VideoCoF_Unified_Video_Editing_with_Temporal_Reasoner_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 统一编辑器直接生成时难以把指令和随时间变化的区域对应。
- **核心创新 / 方法** · 先预测编辑区域潜表示，再生成目标视频的词元。
- **Baseline** · 与 TokenFlow、InsV2V、Señorita 和不使用中间定位的设计比较。
- **Benchmark** · VideoCoF-Bench 的200段视频覆盖四类编辑，正文表1–3比较编辑和时序表现。
- **关键结果 / 消融** · 表2–3独立比较帧链及位置编码和定位帧格式，报告中间区域推理对局部编辑的价值。
- **适用条件 / 局限** · 需要区域监督或生成可用的定位真值，复杂对象遮挡仍需分别测定位和保真。

**可复用机制** · 复杂视频编辑先生成定位表征再出成片，比较是否比无定位的时序生成更能保护非目标区域。

<a id="paper-mosaic-scaling-aware-selection"></a>

## Scaling-Aware Data Selection for End-to-End Autonomous Driving Systems

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Dimlioglu_Scaling-Aware_Data_Selection_for_End-to-End_Autonomous_Driving_Systems_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Dimlioglu_Scaling-Aware_Data_Selection_for_End-to-End_Autonomous_Driving_Systems_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 单一不确定性或总体增益无法反映驾驶指标间的冲突。
- **核心创新 / 方法** · 分域拟合数据增量对各指标的响应，按边际收益迭代选择采集组合。
- **Baseline** · 与随机及不确定性采样比较，正文检查不同预算与单项评测。
- **Benchmark** · OpenScene 和 Navtrain 测 EPDMS 及达到随机基线性能所需预算比，表2拆分规则指标。
- **关键结果 / 消融** · 正文表1在两个设置比较不同策略的分数和预算，表2显示单项分数可单独核查。
- **适用条件 / 局限** · 规模曲线须经小规模样本拟合，部署分布一变需要重新验证排序。

**可复用机制** · 数据采集可按域拟合多个指标的规模曲线，再用边际收益确定下一批选择。

<a id="paper-c-flat-turbo"></a>

## A Faster Path to Continual Learning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_A_Faster_Path_to_Continual_Learning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_A_Faster_Path_to_Continual_Learning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · C-Flat 可促进旧任务和新任务的平坦低损失区，但每轮额外计算三次梯度。
- **核心创新 / 方法** · 分析一阶平坦度梯度的方向不变分量，跳过部分扰动梯度；根据稳定性触发线性调度。
- **Baseline** · 同持续学习算法下的 C-Flat、C-Flat Turbo 及其他优化器；含 L2P、EASE。
- **Benchmark** · CIFAR100、CUB200 等序贯类别实验，含打乱任务顺序、预训练 ViT 和从零训练 ResNet，比较准确率和训练速度。
- **关键结果 / 消融** · 表1–3报告相对 C-Flat 约1.0–1.25倍速度及相近或更高准确率。
- **适用条件 / 局限** · 任务剧烈切换时历史梯度方向可能不再稳定，调度的触发条件须重新观察。

**可复用机制** · 当平坦度优化的梯度方向可复用时，跨扰动步骤共享计算，并随任务逐渐加大复用步。

<a id="paper-heterogeneity-aware-distillation"></a>

## HAD: Heterogeneity-Aware Distillation for Lifelong Heterogeneous Learning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_HAD_Heterogeneity-Aware_Distillation_for_Lifelong_Heterogeneous_Learning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_HAD_Heterogeneity-Aware_Distillation_for_Lifelong_Heterogeneous_Learning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 分类、深度及法线的输出结构不同，统一蒸馏损失容易偏重大面积常见预测。
- **核心创新 / 方法** · 阶段性自蒸馏旧任务，采用输出分布平衡项，并以 Sobel 找显著像素加权局部蒸馏。
- **Baseline** · 表1–3比较不同编码器、持续学习基线和其他训练范式。
- **Benchmark** · NYUv2 三任务、Taskonomy 十任务，另测 Cityscapes；使用各密集任务的原生指标。
- **关键结果 / 消融** · 表1–2比较末阶段旧任务保留，正文对照各蒸馏项的贡献。
- **适用条件 / 局限** · 显著像素及分布估计依赖输出类型，非空间输出或深度噪声边界需重配。

**可复用机制** · 连续训练异构密集任务时，按每项输出分布平衡蒸馏，同时保护显著边界。

<a id="paper-paq-detr"></a>

## PaQ-DETR: Learning Pattern and Quality-Aware Dynamic Queries for Object Detection

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Kang_PaQ-DETR_Learning_Pattern_and_Quality-Aware_Dynamic_Queries_for_Object_Detection_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Kang_PaQ-DETR_Learning_Pattern_and_Quality-Aware_Dynamic_Queries_for_Object_Detection_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 查询固定或正例不均衡会使少数查询负责大部分目标，限制场景适应性。
- **核心创新 / 方法** · 通过内容权重组合共享潜模式，辅以按定位与分类一致性的一对多正例分配。
- **Baseline** · 在 DINO 等 DETR 系列比较原实现或同条件复现，以及其他一对多分配模式。
- **Benchmark** · COCO val2017、Cityscapes，以 mAP 比较，覆盖 ResNet、Swin 及不同训练周期。
- **关键结果 / 消融** · 作者报告跨骨干 mAP 改善1.5%–4.2%，表1–3检验不同配置。
- **适用条件 / 局限** · 仍依赖训练时正例质量，分布改变可能使模式使用重新偏斜。

**可复用机制** · 集合预测中固定查询利用率偏斜时，用少量共享模式组合按图生成查询，再按分类定位匹配质量分配正例。

<a id="paper-vcu-bridge"></a>

## VCU-Bridge: Hierarchical Visual Connotation Understanding via Semantic Bridging

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhong_VCU-Bridge_Hierarchical_Visual_Connotation_Understanding_via_Semantic_Bridging_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhong_VCU-Bridge_Hierarchical_Visual_Connotation_Understanding_via_Semantic_Bridging_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 只看抽象答案无法区分低层观察失败与上层推断失败。
- **核心创新 / 方法** · 构建分级证据链评测，并用搜索辅助生成带层次的指令训练样本。
- **Baseline** · HVCU-Bench 上对照多个多模态模型，另比较分层数据与其他生成策略。
- **Benchmark** · HVCU-Bench 覆盖三个任务家族和15个方面，按推理层比较正确性，另检查通用基准。
- **关键结果 / 消融** · 作者报告能力随推理层级上升而下降；加强低层训练能改善部分高层和通用基准结果。
- **适用条件 / 局限** · 证据链质量依赖人工任务定义，评测相关性不能等同于对模型内部推理的因果确认。

**可复用机制** · 诊断抽象视觉推理时，把低层观察、中间语义和抽象结论标注为可追踪链，并测试低层训练能否向上传导。

<a id="paper-vipo-visual-advantages"></a>

## Seeing What Matters: Visual Preference Policy Optimization for Visual Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Ni_Seeing_What_Matters_Visual_Preference_Policy_Optimization_for_Visual_Generation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Ni_Seeing_What_Matters_Visual_Preference_Policy_Optimization_for_Visual_Generation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 整图共享标量奖励会使局部瑕疵与正确区域收到近似相同训练信号。
- **核心创新 / 方法** · 用预训练视觉骨干的时空特征构造结构化优势图，在 GRPO 升降更新中重分配学习压力。
- **Baseline** · 原始 Flux、Wan2.1、DanceGRPO 与不同感知骨干，包括 DINOv2 和 SAM。
- **Benchmark** · 图像及视频偏好对齐，另测域外标准，视频用 VBench 等指标。
- **关键结果 / 消融** · 表1–2报告相较同类标量奖励方法的偏好和域外表现提升；附录对照感知骨干。
- **适用条件 / 局限** · 需要感知骨干正确反映人感知的重要位置；奖励偏置仍会保留。

**可复用机制** · 视觉生成后训练可把整图或整段标量优势分配为局部优势，以强调感知重要区域。

<a id="paper-motion-3-to-4"></a>

## Motion 3-to-4: 3D Motion Reconstruction for 4D Synthesis

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Motion_3-to-4_3D_Motion_Reconstruction_for_4D_Synthesis_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_Motion_3-to-4_3D_Motion_Reconstruction_for_4D_Synthesis_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 联合生成形状和运动受数据及单目歧义制约，连续帧容易产生不一致几何。
- **核心创新 / 方法** · 先确定规范空间网格，再以压缩运动隐变量及逐帧 Transformer 预测顶点轨迹。
- **Baseline** · 表1对照单目动态重建方案，表2比较是否提供真值参考网格，并区分长短序列。
- **Benchmark** · Motion-80 测真实几何下的时序重建，Consistent4D 测渲染，含 LPIPS、CLIP 等。
- **关键结果 / 消融** · 表2–3报告较好的空间与时间一致性，真值网格对照量化静态阶段限制。
- **适用条件 / 局限** · 依赖规范网格保留所需拓扑，形状错误会传到运动阶段，拓扑改变不适合固定顶点轨迹。

**可复用机制** · 从单目视频重建动态资产时，把静态网格生成与逐顶点时序变形分开建模。

<a id="paper-generated-weights-memorization"></a>

## Generative Modeling of Weights: Generalization or Memorization?

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zeng_Generative_Modeling_of_Weights_Generalization_or_Memorization_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zeng_Generative_Modeling_of_Weights_Generalization_or_Memorization_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 新权重准确率提高，可能只是在复制或插值训练检查点，不能单凭指标判断生成了新函数。
- **核心创新 / 方法** · 分别比较生成权重与训练最近邻的距离、预测行为和性能，再重置训练权重以诊断直接记忆。
- **Baseline** · 对照四种权重生成方法、加噪、权重均值和逐参数高斯采样。
- **Benchmark** · 在所测权重生成任务上联合测权重距离、功能相似度和任务质量，并测试参数置换增强。
- **关键结果 / 消融** · 表 1 全层随机重置后，HyperDiffusion 生成与训练近邻平均距离 0.8，训练样本之间的近邻距离 16.0；仍能复制训练数据。
- **适用条件 / 局限** · 权重距离本身受参数对称影响，须和功能对比同看。结论限所测方法和规模，增加数据对部分方法有帮助。

**可复用机制** · 权重生成方法必须与权重加噪和均值插值比较，并同时用参数近邻与功能相似判断新颖性。见 §3、表 1。

<a id="paper-onlinehmr-causal-delay-evaluation"></a>

## OnlineHMR: Video-based Online World-Grounded Human Mesh Recovery

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_OnlineHMR_Video-based_Online_World-Grounded_Human_Mesh_Recovery_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_OnlineHMR_Video-based_Online_World-Grounded_Human_Mesh_Recovery_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 允许看到未来帧的批式网格恢复可能显示吞吐可用，却无法实时响应。
- **核心创新 / 方法** · 用因果 KV 缓存与滑窗训练做在线网格恢复，增量人体中心 SLAM 将结果对齐世界坐标。
- **Baseline** · 对比 TRACE、GLAMR、SLAHMR、WHAM、TRAM 等在线或非在线方法。
- **Benchmark** · EMDB 中报告世界或相机坐标运动误差、FPS 和平均输出延迟，并补测动态视频。
- **关键结果 / 消融** · 表 3 OnlineHMR 为 3.3 FPS、0.30 秒、WA-MPJPE100 93.5；TRAM 是 2.1 FPS、115.95 秒和 76.4。
- **适用条件 / 局限** · 世界轨迹依赖增量定位和可见人体，3.3 FPS 无法满足所有高频控制需求，应按场景测端到端反馈。

**可复用机制** · 流式人体网格恢复应同时验收因果性、单帧等待时间与世界坐标误差，不能只看处理 FPS。见表 3。

<a id="paper-imap-motion-token-diagnostics"></a>

## I'm a Map! Interpretable Motion-Attentive Maps: Spatio-Temporally Localizing Concepts in Video Diffusion Transformers

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Jun_Im_a_Map_Interpretable_Motion-Attentive_Maps_Spatio-Temporally_Localizing_Concepts_in_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Jun_Im_a_Map_Interpretable_Motion-Attentive_Maps_Spatio-Temporally_Localizing_Concepts_in_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 直接显示交叉注意力常偏对象而非动作，在每帧看起来合理却无法指出动作时刻。
- **核心创新 / 方法** · 从概念特征产生逐帧空间图，再筛选与运动有关的注意力层或头形成时空热图，无需训练。
- **Baseline** · 比较交叉注意力、ConceptAttention、全层 GramCol 和逐项筛层筛头。
- **Benchmark** · 动作定位五项度量含时间和空间定位，另测零样本视频语义分割。
- **关键结果 / 消融** · 表 2 交叉注意力平均 0.36，GramCol 全层 0.41，加层选择 0.46，再加运动头为 0.47。
- **适用条件 / 局限** · 仅说明内部特征与可定位动作相关，尚不能当因果证据；多对象共同行为和抽象动作需单测。

**可复用机制** · 视频扩散的概念解释应分别找在哪帧、哪里、哪个对象发生动作，并把动作相关头与全头对照。见表 1–2。

<a id="paper-parallel-jacobi-image-decoding"></a>

## Parallel Jacobi Decoding for Fast Autoregressive Image Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Liao_Parallel_Jacobi_Decoding_for_Fast_Autoregressive_Image_Generation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Liao_Parallel_Jacobi_Decoding_for_Fast_Autoregressive_Image_Generation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 延长一维 Jacobi 草稿会积累依赖误差，迭代速度收益趋于饱和。
- **核心创新 / 方法** · 利用图像的二维邻域相关性在空间上展开预测并调整注意力掩码，反复并行精化草稿。
- **Baseline** · 比较原始自回归、SJD、GSD，保持生成骨干不变。
- **Benchmark** · MS-COCO、PartiPrompt，在 Lumina-mGPT 和 LlamaGen-XL 等模型报单图延迟、步数、FID、CLIP 和 IS。
- **关键结果 / 消融** · 表 1 Lumina-mGPT 一项设置为 24.78 秒、FID 32.38，原自回归为 197.16 秒、30.79。
- **适用条件 / 局限** · 依赖二维词元布局及模型对局部相关的利用；图像布局一致性和随机采样分布应独立复测。

**可复用机制** · 对自回归图像尝试从一维连续草稿切到二维局部并行更新，并在相同骨干测收敛与 FID。见表 1–2。

<a id="paper-few-shot-attention-sink"></a>

## Addressing Exacerbated Attention Sink for Source-Free Cross-Domain Few-Shot Learning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yi_Addressing_Exacerbated_Attention_Sink_for_Source-Free_Cross-Domain_Few-Shot_Learning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yi_Addressing_Exacerbated_Attention_Sink_for_Source-Free_Cross-Domain_Few-Shot_Learning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 目标标签稀少时训练可能放大本来就与文本类名接近的特征，挤压其他判别线索。
- **核心创新 / 方法** · 在原模型和目标微调模型间诊断注意力汇聚，抑制易词元并增强较难但有区分力的词元。
- **Baseline** · 对照原微调、仅抑制、仅增强和完整策略。
- **Benchmark** · CropDiseases、EuroSAT、ISIC2018、ChestX，做 5-way 1-shot 和 5-shot 准确率比较。
- **关键结果 / 消融** · 表 2 的 5-shot 平均由 65.99 升至 68.44；仅抑制为 67.66，仅增强为 67.23。
- **适用条件 / 局限** · 少样本中所谓难词元也可能是噪声或背景，换骨干与大域差时应复审其关注的部位。

**可复用机制** · 用少量目标域样本微调视觉语言模型时，应诊断是否进一步集中注意到原本容易对齐的词元，再分别测试抑制与增强。见表 2。

<a id="paper-modix-position-stride"></a>

## MODIX: A Training-Free Multimodal Information-Driven Positional Index Scaling for Vision-Language Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_MODIX_A_Training-Free_Multimodal_Information-Driven_Positional_Index_Scaling_for_Vision-Language_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_MODIX_A_Training-Free_Multimodal_Information-Driven_Positional_Index_Scaling_for_Vision-Language_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 位置编号等距分配可能让冗余模态或重复画面占用过多位置分辨率。
- **核心创新 / 方法** · 用模态内协方差熵和跨模态对齐估计信息，对不同模态重新缩放位置索引步幅，无需训练。
- **Baseline** · 对照同模型原索引、不同位置编码变体、不同熵与对齐权重。
- **Benchmark** · 图像问答、图表与 Video-MME 长中短视频，比较公开骨干的任务准确率。
- **关键结果 / 消融** · 表 2 Qwen3-VL-8B 的 Video-MME 中等时长由 58.79 到 61.45，长时长由 48.86 到 49.44。
- **适用条件 / 局限** · 需可访问模型位置参数且改后不超训练长度范围；熵、对齐与真正的任务信息可能偏离。

**可复用机制** · 视觉语言推理可只改位置索引跨度来检验信息分配作用，避免与删词元的效果混在一起。见表 2–4。

<a id="paper-cgu-bayes-graph-uncertainty"></a>

## CGU-Bayes: Causal Graph Uncertainty-Guided Bayesian Inference for Domain Generalization

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yin_CGU-Bayes_Causal_Graph_Uncertainty-Guided_Bayesian_Inference_for_Domain_Generalization_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yin_CGU-Bayes_Causal_Graph_Uncertainty-Guided_Bayesian_Inference_for_Domain_Generalization_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 数据不足或存在偏差时，单一估计因果图可能将偶然关联视为稳定关系。
- **核心创新 / 方法** · 对候选图进行贝叶斯推断，以任务相关的图不确定性给预测加权，让不确定边影响减弱。
- **Baseline** · 比较 ERM、IRM 等，以及去掉不确定性引导和加入模型集合的版本。
- **Benchmark** · BLT 一组设定用域外相对 MSE，CMNIST、VLCS、PACS、OfficeHome 比较准确率。
- **关键结果 / 消融** · 表 1 的平均域外相对 MSE 从去不确定性引导的 59.7 降至 54.2；正文说明单模型在自然视觉数据上未一致改善。
- **适用条件 / 局限** · 估计分布受因果候选模型和独立性假设限制，准确率提升不能证明恢复真实因果图。

**可复用机制** · 域泛化若依赖推断的因果图，应比较固定图、等权候选图和不确定性加权，区分真实数据与已知机制仿真。见表 1–3。

<a id="paper-tanl"></a>

## Activation Matters: Test-time Activated Negative Labels for OOD Detection with Vision-Language Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Activation_Matters_Test-time_Activated_Negative_Labels_for_OOD_Detection_with_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Activation_Matters_Test-time_Activated_Negative_Labels_for_OOD_Detection_with_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 语义距离远的负类标签未必在真正外域样本上得到响应。
- **核心创新 / 方法** · 用保留的高置信测试图估计语料标签活跃度，按历史或当前批次更新负标签和分数。
- **Baseline** · 以 NegLabel 为直接对照，表4消融负类选取及打分。
- **Benchmark** · ImageNet-1k 及 OpenOOD，表1–4报告 FPR95、AUROC、域内准确率。
- **关键结果 / 消融** · 正文报告相对固定负类方法的改进，并比较自动与手工置信阈值。
- **适用条件 / 局限** · 测试序列需要足够代表性；流式偏移或批次强相关时需重新测误报。

**可复用机制** · 开放集检测选负类时用测试分布的激活统计，检查固定文本负类是否与真实外域样本脱节。

<a id="paper-cvm-dense-mtl"></a>

## 3D-Aware Multi-Task Learning with Cross-View Correlations for Dense Scene Understanding

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_3D-Aware_Multi-Task_Learning_with_Cross-View_Correlations_for_Dense_Scene_Understanding_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_3D-Aware_Multi-Task_Learning_with_Cross-View_Correlations_for_Dense_Scene_Understanding_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 纯二维特征使联合分割与深度缺少三维约束。
- **核心创新 / 方法** · 以共享跨视模块向编码器注入代价体和增强跨视特征。
- **Baseline** · 比较标准多任务编码器、只用代价体及只用跨视增强。
- **Benchmark** · NYUv2、PASCAL-Context；表4分测 mIoU、深度 RMSE、法向和边界。
- **关键结果 / 消融** · 表4完整模块使 mIoU 从64.03到65.27、深度 RMSE 从0.3954降到0.3836，法向误差同为15.35。
- **适用条件 / 局限** · 跨视证据取决于几何质量，各输出量的收益可能不一致。

**可复用机制** · 多任务密集预测共享跨视相关信息，不只在同一图像特征上学习任务关系。

<a id="paper-coin3d"></a>

## CoIn3D: Revisiting Configuration-Invariant Multi-Camera 3D Object Detection

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Kuang_CoIn3D_Revisiting_Configuration-Invariant_Multi-Camera_3D_Object_Detection_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Kuang_CoIn3D_Revisiting_Configuration-Invariant_Multi-Camera_3D_Object_Detection_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 内外参和相机阵列的同时变化会破坏在固定配置中学到的空间先验。
- **核心创新 / 方法** · 在输入层做相机感知增广，在特征层加入焦距、地面几何及射线表示。
- **Baseline** · 以 BEVDepth、BEVFormer、PETR 为基础，表3–4分别消融观测和特征模块。
- **Benchmark** · nuScenes、Waymo 等跨配置测试，报告 mAP、平移和朝向误差及 NDS。
- **关键结果 / 消融** · 表1–2验证在不同检测主干和训练测试配置上的迁移，表3列出两个改动的组合。
- **适用条件 / 局限** · 依赖可用相机内外参，域间目标类别和成像变化也可能影响结果。

**可复用机制** · 换相机阵列部署三维检测时，分别验证观测增广与显式相机特征调制。

<a id="paper-fisherposer"></a>

## FisherPoser: Human Motion Estimation from Sparse Observations with Hierarchical Region-Wise Fisher-Matrix Uncertainty Modeling

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xia_FisherPoser_Human_Motion_Estimation_from_Sparse_Observations_with_Hierarchical_Region-Wise_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xia_FisherPoser_Human_Motion_Estimation_from_Sparse_Observations_with_Hierarchical_Region-Wise_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 仅头显加双手控制器不足以唯一推断全身姿势，不同关节的歧义也不相同。
- **核心创新 / 方法** · 在 SO(3) 上按关节输出矩阵 Fisher 分布，结合区域词元并用父关节分布细化子关节。
- **Baseline** · 与常用稀疏运动估计方法比较，表2–3消融姿态结构与不确定性估计。
- **Benchmark** · 正文表1–3分别报告姿态估计及不确定性比较。
- **关键结果 / 消融** · 正文对照点式姿态及概率配置，检验层级结构和不确定表征。
- **适用条件 / 局限** · 边缘旋转分布未必覆盖联合多峰姿态，传感器布局变化需校验。

**可复用机制** · 稀疏姿态估计可直接预测旋转分布，再沿运动链条件化传播不确定性。

<a id="paper-action-motifs"></a>

## Action Motifs: Self-Supervised Hierarchical Representation of Human Body Movements

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Kinoshita_Action_Motifs_Self-Supervised_Hierarchical_Representation_of_Human_Body_Movements_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Kinoshita_Action_Motifs_Self-Supervised_Hierarchical_Representation_of_Human_Body_Movements_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 定长帧词元难表达共享身体动作和持续时间差异。
- **核心创新 / 方法** · A4Mer 对三维姿态学习短时潜词元和组合模式，在两层潜空间做掩码预测。
- **Baseline** · 表2比较同数据预训练方法，表3拆分层级组件。
- **Benchmark** · AMD 上预训练，正文评动作识别、运动相关任务及消融。
- **关键结果 / 消融** · 表2–3分别检验表示迁移和各层级贡献。
- **适用条件 / 局限** · 三维姿态质量和动作分段影响模式发现，与机器人控制语义的对应待验。

**可复用机制** · 运动序列先学习可变长的局部动作单位，再对其组合做掩码预测，以检查跨动作的复用。

<a id="paper-perceval"></a>

## Improving Vision-language Models with Perception-centric Process Reward Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Min_Improving_Vision-language_Models_with_Perception-centric_Process_Reward_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Min_Improving_Vision-language_Models_with_Perception-centric_Process_Reward_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 终局反馈无法指出是哪个感知声明导致错误，可能惩罚正确推理。
- **核心创新 / 方法** · 感知过程评审逐条比对视觉声明和图像，只降低错误片段词元的优势。
- **Baseline** · 对照普通 GRPO、不同局部惩罚强度及不同测试时策略。
- **Benchmark** · 正文表1–3覆盖视觉查找、RealWorldQA、MathVision 和 ChartQA 等正确率。
- **关键结果 / 消融** · 表3设局部惩罚为零的基线，并对照开启不同惩罚强度后的各项表现。
- **适用条件 / 局限** · 评审器会错定位或漏标，正常答复和感知错误应分别验收。

**可复用机制** · 用视觉声明核验定位错误片段，按词元调优势并对照整轨迹奖励。

<a id="paper-rng-3d-kv-cache"></a>

## RnG: A Unified Transformer for Complete 3D Modeling from Partial Observations

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xiang_RnG_A_Unified_Transformer_for_Complete_3D_Modeling_from_Partial_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xiang_RnG_A_Unified_Transformer_for_Complete_3D_Modeling_from_Partial_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 快速重建只覆盖视频或图像已观测部分，单独生成又可能扭曲可见几何。
- **核心创新 / 方法** · 重建引导因果注意力隔离重建和生成，以 Transformer KV 缓存作为可由目标位姿查询的三维表示。
- **Baseline** · 表1–2比较已有重建和新视角生成方法，表3与 LVSM 对照训练效率并做结构消融。
- **Benchmark** · GSO 稀疏视图重建与生成测试，比较新视角 RGBD 的几何、外观及开销。
- **关键结果 / 消融** · 表2–3显示同一模型兼顾观测区重建与不可见视角生成，原文报告缓存可快速查询。
- **适用条件 / 局限** · 未见区域只能生成合理解释，不能当作真实可测的几何。

**可复用机制** · 稀疏视图三维推理时，隔离观测重建和不可见区域生成，并用同一缓存支持反复视角查询。

<a id="paper-s2ft-sparse-spectrum"></a>

## S2FT: Parameter-Efficient Fine-Tuning in Sparse Spectrum Domain

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_S2FT_Parameter-Efficient_Fine-Tuning_in_Sparse_Spectrum_Domain_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_S2FT_Parameter-Efficient_Fine-Tuning_in_Sparse_Spectrum_Domain_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 原始权重轴上微调增量的能量近似均匀，冻结大部分傅里叶系数可能丢掉信号。
- **核心创新 / 方法** · 先估计粗增量，以行列重排促进局部平滑和频谱稀疏，再只学习重排频谱中的少量系数。
- **Baseline** · 与直接傅里叶参数适配及其他 PEFT 方案在同骨干对照。
- **Benchmark** · ImageNet-21K 预训练 ViT-B/16 在 VTAB-1k 与 FGVC 测分类，另有主观生成评测。
- **关键结果 / 消融** · 表1–3比较参数预算下的任务表现，正文的频谱诊断支持重排的必要性。
- **适用条件 / 局限** · 需要预估增量，所得重排未必适合不同任务、骨干或权重层。

**可复用机制** · 傅里叶微调前先测权重增量的频谱，若不稀疏则以可逆神经元重排聚拢能量。

<a id="paper-perturbation-aware-filtering"></a>

## PAF: Perturbation-Aware Filtering for Open-Set Semi-Supervised Learning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Han_PAF_Perturbation-Aware_Filtering_for_Open-Set_Semi-Supervised_Learning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Han_PAF_Perturbation-Aware_Filtering_for_Open-Set_Semi-Supervised_Learning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 未标注池同时有已知和未知类别，单看分类分数可能保留与已知类别不相干的样本。
- **核心创新 / 方法** · 用保语义扰动构造同样本变体，测其表示变化作为过滤分数；先利用未标注数据，再进入过滤适配阶段。
- **Baseline** · 同任务其他开放集半监督方法，并用不同外部域外源对照。
- **Benchmark** · 四套开放集分类数据；表1报告已知类准确率，表2报告域外识别 AUC，表3改变 CIFAR-10 外部域外来源。
- **关键结果 / 消融** · 表1–3报告不稳定性过滤在多个条件改善域外识别及已知类分类。
- **适用条件 / 局限** · 扰动必须对已知样本保留语义，天然不稳定的困难类可能被误过滤。

**可复用机制** · 开放集半监督数据清理可用语义保持扰动下的表示不稳定性评估样本是否域外。

<a id="paper-global-information-thresholding"></a>

## Global Information Thresholding for Sufficient and Necessary Circuits

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Cho_Global_Information_Thresholding_for_Sufficient_and_Necessary_Circuits_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Cho_Global_Information_Thresholding_for_Sufficient_and_Necessary_Circuits_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 固定电路预算不保证剩余边足以重现行为，也不反映删除这些边会造成的损失。
- **核心创新 / 方法** · 用保留符号的积分梯度评分，以目标行为保留率确定全局阈值，通过反事实消融检查选中电路和补集。
- **Baseline** · 与 EAP-IG-inputs (CF) 等归因定位方法比较。
- **Benchmark** · Mechanistic Interpretability Benchmark 测 CPR、CMD 和部分任务 AUROC；GPT-2 IOI 另外测 ΔNLL、Brier 和 ECE。
- **关键结果 / 消融** · 表1–2显示跨任务结果有竞争力；表3报告在 IOI 的充分性及所报必要性诊断改善。
- **适用条件 / 局限** · 电路及阈值依赖任务、行为指标和消融基准；验证范围不足以断言全局唯一电路。

**可复用机制** · 定位模型电路时，用行为保留阈值自动决定边数，并分开报告充分性与必要性。

<a id="paper-m3grounder"></a>

## M3Grounder: Mask-Based Multi-Span and Multi-Granular Grounding for Document QA

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Venna_M3Grounder_Mask-Based_Multi-Span_and_Multi-Granular_Grounding_for_Document_QA_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Venna_M3Grounder_Mask-Based_Multi-Span_and_Multi-Granular_Grounding_for_Document_QA_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 答案可能来自多个不连续区域；粗框遇弯曲文字或图文混排会连入无关像素。
- **核心创新 / 方法** · 在答案文字中穿插引用令牌，预测短语、行与块的掩码，以溢出抑制及包含损失约束。
- **Baseline** · 表1与文档证据定位方法比较，表3在普通文档问答对照相似规模模型。
- **Benchmark** · BoundingDocs、DOGR-Bench、MMDocBench 与 GroundingDocQA-Bench；多粒度测 F1g。
- **关键结果 / 消融** · 表1–2报告短语及多粒度定位改善，原文比较常规文档问答表现。
- **适用条件 / 局限** · 需要细粒度掩码及对应层级，非嵌套证据不能直接套用包含约束。

**可复用机制** · 文档问答需要可定位证据时，让每个答案短语输出掩码，并约束粒度间的包含关系。

<a id="paper-geork2"></a>

## GeoRK2: Geometry-Guided Runge-Kutta Integration for Diffusion Transformer Acceleration

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Sun_GeoRK2_Geometry-Guided_Runge-Kutta_Integration_for_Diffusion_Transformer_Acceleration_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Sun_GeoRK2_Geometry-Guided_Runge-Kutta_Integration_for_Diffusion_Transformer_Acceleration_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 抽稀采样步会放大误差，欧氏积分无法量化特征中的各向异性变化。
- **核心创新 / 方法** · 以经验协方差度量模型激活几何，将噪声预测引出的几何流与二阶 Runge–Kutta 积分结合。
- **Baseline** · 与 DDIM-50 及相应模型50步参考和少步采样对照。
- **Benchmark** · DiT-XL/2 的 ImageNet-256、FLUX.1-dev 图像生成、HunyuanVideo 的 VBench；五次运行均值。
- **关键结果 / 消融** · 作者报告所测场景约4–5倍加速，FID 差约0.81；表1–3按模型列出速度和质量。
- **适用条件 / 局限** · 通道协方差估计稳定性及重计算开销随模型而异，极少步数不能保证保真。

**可复用机制** · 为扩散推理减少步数时，用经验激活协方差定义积分几何，检验大步长下保真度。

<a id="paper-wonderzoom-scale-adaptive-surfels"></a>

## WonderZoom: Multi-Scale 3D World Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Cao_WonderZoom_Multi-Scale_3D_World_Generation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Cao_WonderZoom_Multi-Scale_3D_World_Generation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 统一高斯尺度表示难同时保留粗场景和局部细节，引入细层也会增加渲染成本。
- **核心创新 / 方法** · 用尺度自适应高斯 surfel，并随着放大逐级生成更细结构，按尺度调制透明度。
- **Baseline** · 对比较不同视频与三维生成模型，并将同方法去掉不透明度调制。
- **Benchmark** · 在多尺度世界生成比较 CLIP 分数和人评，并报告 FPS 和显存。
- **关键结果 / 消融** · 表 3 完整调制为 3.40 GB、97.2 FPS，去调制为 7.96 GB、1.4 FPS。
- **适用条件 / 局限** · 生成的微小结构属于推断内容，不能作为实物测量；收益依赖选择性渲染与所测显卡。

**可复用机制** · 多尺度场景渲染可按当前尺度调节粗细基元不透明度，并分别测切尺度的一致性和显存。见表 3。

<a id="paper-concept-aware-batch-sampling"></a>

## Concept-Aware Batch Sampling Improves Language-Image Pretraining

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Ghosh_Concept-Aware_Batch_Sampling_Improves_Language-Image_Pretraining_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Ghosh_Concept-Aware_Batch_Sampling_Improves_Language-Image_Pretraining_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 静态过滤后的语料仍可能导致每批被常见概念主导，限制长尾覆盖和特定任务学习。
- **核心创新 / 方法** · 从预采样批按概念覆盖得分选训练样本，也可把多实例频次作为目标。
- **Baseline** · 与 IID、MetaCLIP 式整理和其他批构造方法对照。
- **Benchmark** · 28 项评估，包括 ImageNet、域偏移分类和 Let-it-Wag 长尾任务。
- **关键结果 / 消融** · 表 2 ViT-B/32-CLIP 的 alt 设置 ImageNet 验证从 IID 的 17.3 到 21.9；recap 的场景项从 43.1 到 42.8，非所有维度提升。
- **适用条件 / 局限** · 需要可靠的概念抽取及可接受的数据加载开销，概念标签偏差或指标不齐时应检查采样是否放大偏差。

**可复用机制** · 图文预训练可按目标概念直方图动态抽批，分别调节覆盖种类和批内出现频次。见表 2–4。

<a id="paper-geofree-coseg-semantic-correspondence"></a>

## GeoFree-CoSeg: Unsupervised Point Cloud-Image Cross-Modal Co-Segmentation Without Geometric Alignment

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Duan_GeoFree-CoSeg_Unsupervised_Point_Cloud-Image_Cross-Modal_Co-Segmentation_Without_Geometric_Alignment_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Duan_GeoFree-CoSeg_Unsupervised_Point_Cloud-Image_Cross-Modal_Co-Segmentation_Without_Geometric_Alignment_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 无对齐的图像和点云难直接用点像素匹配，但不同模态仍包含共同物体语义。
- **核心创新 / 方法** · 先各自抽取粗语义，用跨模态公共图细化，再在两支互相增强一致对象的特征。
- **Baseline** · 与 K-means、AdaCoSeg、GrowSP、LogoSP 等及移除语义/对象损失对照。
- **Benchmark** · ScanObjectNN 和 S3DIS 的无监督分割报告 mIoU，另做图像共分割和部件消融。
- **关键结果 / 消融** · 表 2 S3DIS 平均 mIoU 0.54，LogoSP 0.48；表 1 ScanObjectNN 为 0.63，表中另一基线为 0.61。
- **适用条件 / 局限** · 需要两组观测有可识别的共同语义，无几何对齐不等于可容忍任意类集合差异；小部件要单列验证。

**可复用机制** · 点云和图像缺乏标定对应时，可先各自发现粗语义，再用公共语义图筛选共有区域。见表 1–3。

<a id="paper-negative-binomial-count-latents"></a>

## Negative Binomial Variational Autoencoders for Overdispersed Latent Modeling

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Negative_Binomial_Variational_Autoencoders_for_Overdispersed_Latent_Modeling_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Negative_Binomial_Variational_Autoencoders_for_Overdispersed_Latent_Modeling_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 泊松潜变量假定均值等于方差，不能灵活表达方差显著更大的计数分布。
- **核心创新 / 方法** · 用带离散程度参数的负二项潜变量替代泊松，并给出 KL 估计和重参数化。
- **Baseline** · 比较高斯、连续稀疏及泊松 VAE 等，考察不同估计方法。
- **Benchmark** · 四个图像数据集上的重建 MSE、SSIM 以及生成 FID/KID，另做表征探针。
- **关键结果 / 消融** · 表 1 的 CIFAR 16×16 中 MC-G 版本 FID@5k 为 40.28，泊松为 60.37；重建 MSE 则为 0.0470 和 0.0357。
- **适用条件 / 局限** · 证据来自实验型单层图像 VAE；对更大模型、真实脉冲数据和其它稀疏离散潜变量应重测。

**可复用机制** · 离散计数潜变量若呈过度离散，可比较负二项和泊松先验，同时测重建与生成而非只看其中一项。见表 1–3。

<a id="paper-urgt-multipatch-geometry"></a>

## Any Resolution Any Geometry: From Multi-View To Multi-Patch

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Cui_Any_Resolution_Any_Geometry_From_Multi-View_To_Multi-Patch_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Cui_Any_Resolution_Any_Geometry_From_Multi-View_To_Multi-Patch_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 逐块估深可保细节，却在块连接处不一致；整图低分辨率则丢失细结构。
- **核心创新 / 方法** · 将图块连同粗深度和法线先验输入统一 VGGT 变体，用跨块注意力建几何关系，训练时混合切块网格。
- **Baseline** · 对照 Depth Anything v2、PatchRefiner 类方案，以及固定与混合网格、不同位置编码。
- **Benchmark** · UnrealStereo4K、ETH3D、Middlebury 等，报告深度 AbsRel、δ1、RMSE 与接缝/法线指标。
- **关键结果 / 消融** · 表 3 混合网格的 AbsRel 0.0295，单一配置 (1,0,0,0) 为 0.0500；CE 分别为 0.0418、0.0648。
- **适用条件 / 局限** · 依赖粗几何先验可用，极端细长图、严重跨块遮挡或输入非常大时应同时测接缝和显存。

**可复用机制** · 高分图像深度与法线可把图块当多视图共享几何注意力，并随机化图块网格测接缝。见表 3–4。

<a id="paper-rehyat-chunk-recurrent-hybrid-attention"></a>

## ReHyAt: Recurrent Hybrid Attention for Video Diffusion Transformers

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Ghafoorian_ReHyAt_Recurrent_Hybrid_Attention_for_Video_Diffusion_Transformers_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Ghafoorian_ReHyAt_Recurrent_Hybrid_Attention_for_Video_Diffusion_Transformers_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 纯 softmax 注意力计算随视频长度平方上升，全部线性化又会损害生成能力。
- **核心创新 / 方法** · 把 softmax 和线性注意力结合成分块递归计算，从已有视频扩散模型蒸馏。
- **Baseline** · 比较 Wan2.1 的 FlashAttention、HedgeHog 和均匀混合，视频质量另比高效生成模型。
- **Benchmark** · VBench、VBench-2.0、人评，表 4 在 Snapdragon8 Gen4 上测不同帧数的注意力块延迟。
- **关键结果 / 消融** · 表 4 ReHyAt 的 121 帧为 302 ms，FlashAttention 4,809 ms；161 帧 ReHyAt 为 384 ms，其他表列变体超出内存。
- **适用条件 / 局限** · 移动端数字是注意力块测量，端到端扩散还需解码和去噪；跨块运动与未来帧一致性要独立验收。

**可复用机制** · 长视频扩散可以混合精确局部注意力与递归跨块线性状态，并按设备跨帧数测延迟。见表 4。

<a id="paper-geocodebench"></a>

## Benchmarking PhD-Level Coding in 3D Geometric Computer Vision

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Benchmarking_PhD-Level_Coding_in_3D_Geometric_Computer_Vision_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Benchmarking_PhD-Level_Coding_in_3D_Geometric_Computer_Vision_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 通用编程分数难反映三维几何算法的正确实现。
- **核心创新 / 方法** · 从作者仓库筛核心函数，用覆盖边界条件的可重复单元测试评价实现。
- **Baseline** · 比较八种公开与闭源模型，并区分通用及特定论文的几何任务。
- **Benchmark** · GeoCodeBench 采用函数填空及自动通过率，正文表2按技能分组。
- **关键结果 / 消融** · 正文报告所测最强模型 GPT-5 仍只有36.6%通过率。
- **适用条件 / 局限** · 结果依赖人筛的函数和单测覆盖，同样通过的实现未必能恢复完整研究结果。

**可复用机制** · 复现科学算法时验收论文的核心函数及边界条件，和整仓运行成功分开。

<a id="paper-ddg-fast-robust-training"></a>

## Mitigating Error Amplification in Fast Adversarial Training

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_Mitigating_Error_Amplification_in_Fast_Adversarial_Training_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_Mitigating_Error_Amplification_in_Fast_Adversarial_Training_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 快速稳健训练可能过拟合训练扰动，干净数据精度也可能下降。
- **核心创新 / 方法** · 用置信感知的动态训练引导调节各组的稳健监督。
- **Baseline** · 正文表1–4对照其他快速防御训练、整组同权及组件变体。
- **Benchmark** · CIFAR-10、CIFAR-100 等，分别评价干净精度与稳健精度。
- **关键结果 / 消融** · 正文按置信组归因误差放大，表3–4检查动态训练组件。
- **适用条件 / 局限** · 置信未校准时分组会失真，收益需以独立防御测试集验证。

**可复用机制** · 防御训练按样本置信分层检查精度与鲁棒性，避免低置信样本主导错误放大。

<a id="paper-poco-reference-positioning"></a>

## Rethinking Position Embedding as a Context Controller for Multi-Reference and Multi-Shot Video Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_Rethinking_Position_Embedding_as_a_Context_Controller_for_Multi-Reference_and_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_Rethinking_Position_Embedding_as_a_Context_Controller_for_Multi-Reference_and_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 依赖语义相似度会把相近参考错配到人物或镜头。
- **核心创新 / 方法** · 在旋转位置编码中增加参考和目标位置关系，让标识信息补足外观特征。
- **Baseline** · 与既有多参考、多镜头生成基线及不同位置编码配置对照。
- **Benchmark** · 正文表1–2分别测综合生成表现与位置通道消融。
- **关键结果 / 消融** · 正文报告参考保真及跨段一致性改善，表2比较多种时间通道布局。
- **适用条件 / 局限** · 适用于参考标识可信的内容控制，镜头切换和主体遮挡下仍需单测。

**可复用机制** · 当多路参考外观相似时，可用独立位置信息约束引用关系，按参考混淆和跨段一致性验收。

<a id="paper-msrl-multimodal-reward"></a>

## MSRL: Scaling Generative Multimodal Reward Modeling via Multi-Stage Reinforcement Learning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_MSRL_Scaling_Generative_Multimodal_Reward_Modeling_via_Multi-Stage_Reinforcement_Learning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_MSRL_Scaling_Generative_Multimodal_Reward_Modeling_via_Multi-Stage_Reinforcement_Learning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 直接使用多模态偏好做强化训练需要大量昂贵标签。
- **核心创新 / 方法** · 先在文本偏好上建立可用奖励推理，再经描述过渡到多模态并做跨模态蒸馏。
- **Baseline** · 与生成式奖励基线比较，表4消融各阶段、描述数据和蒸馏。
- **Benchmark** · 正文表2–4在 VL-RewardBench、Multimodal RewardBench 等评估正确率。
- **关键结果 / 消融** · 表4完整模型75.9、生成基线66.6，去第一阶段68.8，去描述数据74.3。
- **适用条件 / 局限** · 移除第一阶段同时移除了冷启动 SFT，不能将全差值归给文本强化学习。

**可复用机制** · 多模态偏好标签少时，可先训练文本奖励推理，再依次检验描述桥接和原始图像阶段。

<a id="paper-pixelrush"></a>

## PixelRush: Ultra-Fast, Training-Free High-Resolution Image Generation via One-step Diffusion

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Lai_PixelRush_Ultra-Fast_Training-Free_High-Resolution_Image_Generation_via_One-step_Diffusion_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Lai_PixelRush_Ultra-Fast_Training-Free_High-Resolution_Image_Generation_via_One-step_Diffusion_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 高分辨率图像的分块推理常靠反复反演，少步配置出现拼接与细节问题。
- **核心创新 / 方法** · 用少步分块去噪配合连续拼接和噪声补偿，避免多次整块重生成。
- **Baseline** · 表1比较已有免训练高分辨生成，表3–4比较配置和去掉组件。
- **Benchmark** · 正文测试 4K 等分辨率，辅以量化质量、时间和盲评偏好。
- **关键结果 / 消融** · 正文约20秒生成 4K，并报告相对所测方法加速约10至35倍。
- **适用条件 / 局限** · 耗时随硬件和采样器变化，丰富纹理和大结构一致性应分开测。

**可复用机制** · 极少步数的分块生成须单独处理拼接重叠和低频平滑，不能套用多步循环。

<a id="paper-scaleformer"></a>

## Cross-Scale Pansharpening via ScaleFormer and the PanScale Benchmark

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Cao_Cross-Scale_Pansharpening_via_ScaleFormer_and_the_PanScale_Benchmark_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Cao_Cross-Scale_Pansharpening_via_ScaleFormer_and_the_PanScale_Benchmark_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 固定裁块训练无法直接涵盖高分辨率全场。
- **核心创新 / 方法** · 尺度感知分块后分别建模块内空间和块间依赖，并以旋转位置编码支持变长。
- **Baseline** · 表2–3与已有全色锐化方法对照。
- **Benchmark** · PanScale 及三个真实全分辨率数据集，对比跨尺度融合质量。
- **关键结果 / 消融** · 表2–3报告在未见尺度和完整场景的改善。
- **适用条件 / 局限** · 取决于局部统计能否跨分辨率复用，序列开销随尺寸增长。

**可复用机制** · 跨图像分辨率泛化时固定局部块尺度，把尺寸变化转成序列长度外推。

<a id="paper-matlat-locality-regularization"></a>

## MatLat: Material Latent Space for PBR Texture Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yeo_MatLat_Material_Latent_Space_for_PBR_Texture_Generation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yeo_MatLat_Material_Latent_Space_for_PBR_Texture_Generation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 直接加入材质通道导致潜分布偏移；特征对应注意力也不能弥补解码非局部性。
- **核心创新 / 方法** · 微调预训练 VAE 接纳材质通道，并约束潜片解码得到对应像素区域。
- **Baseline** · 表1消融注意力及潜空间设计，表2比较已有 PBR 纹理生成。
- **Benchmark** · 已知网格的 PBR 纹理生成，以跨视角一致性及材质质量对比。
- **关键结果 / 消融** · 消融指出只加对应注意力的收益有限，局部约束补足对应性。
- **适用条件 / 局限** · 目标通道需要稳定空间配准，局部约束不应消除材质本身的长程结构。

**可复用机制** · 给预训练图像生成器新增空间通道时，用裁剪潜片并解码的局部一致性避免跨视角对应失效。

<a id="paper-diffusion-noise-diversity-recovery"></a>

## It's Never Too Late: Noise Optimization for Collapse Recovery in Trained Diffusion Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Harrington_Its_Never_Too_Late_Noise_Optimization_for_Collapse_Recovery_in_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Harrington_Its_Never_Too_Late_Noise_Optimization_for_Collapse_Recovery_in_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 同提示不同随机种子依然可能产生相似结果。
- **核心创新 / 方法** · 固定生成器，以多样性目标优化候选初始噪声，同时检验白噪与有色噪声。
- **Baseline** · 比较固定生成器通常采样、不同初始化及结合 HPSv2 质量奖励的优化。
- **Benchmark** · GenEval 与 SDXL-Turbo，报告 DINOv2、DreamSim、LPIPS、Vendi 以及对齐和 HPSv2。
- **关键结果 / 消融** · 表1–2报告优化可提升多样性；改变初噪频谱进一步影响质量与搜索。
- **适用条件 / 局限** · 需为同提示联合处理多个样本；多样性度量可能诱导语义不相关的变化。

**可复用机制** · 已训练扩散模型在同提示下重复时，直接优化多样性目标的初噪，并比较噪声频谱。

<a id="paper-star-kvqa"></a>

## StaR-KVQA: Structured Reasoning Traces for Implicit-Knowledge Visual Question Answering

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wen_StaR-KVQA_Structured_Reasoning_Traces_for_Implicit-Knowledge_Visual_Question_Answering_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wen_StaR-KVQA_Structured_Reasoning_Traces_for_Implicit-Knowledge_Visual_Question_Answering_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 仅答案微调不能约束实体证据或事实推理结构。
- **核心创新 / 方法** · 离线从同一多模态模型构造和选择双路径轨迹，再做结构感知自蒸馏；推理无需外部检索。
- **Baseline** · 对照答案监督及现有隐式知识视觉问答模型。
- **Benchmark** · OK-VQA 与 FVQA，比较视觉知识问答正确率。
- **关键结果 / 消融** · 表1–2比较双路径训练和已有方法，正文分析先验与监督取舍。
- **适用条件 / 局限** · 模型错误知识可被自蒸馏放大，轨迹可解释性不能代替事实校验。

**可复用机制** · 视觉问答自蒸馏时，同时监督符号实体关系与依该路径写的自然语言解释。

<a id="paper-clip-irm"></a>

## A Causal Marriage between VLM and IRM from Understanding to Reasoning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_A_Causal_Marriage_between_VLM_and_IRM_from_Understanding_to_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_A_Causal_Marriage_between_VLM_and_IRM_from_Understanding_to_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 类别与上下文共同出现时可能形成脆弱的捷径。
- **核心创新 / 方法** · 在指定词表和因子假设下关联受约束 InfoNCE 与 IRM，应用于 CLIP 中期训练，并以不变对齐分数作多模态过程奖励。
- **Baseline** · 原 CLIP、域外泛化方案和多模态模型基线。
- **Benchmark** · 图文零样本域外泛化及多模态推理设置，比较任务准确率。
- **关键结果 / 消融** · 表1报告域外泛化对照，理论等价依赖正文设定，实验展示过程奖励的收益。
- **适用条件 / 局限** · 类特定词与环境词未必可稳定分离，不变性结论不能脱离推导条件。

**可复用机制** · 当图文模型依赖背景时，按词元分开类别语义和环境线索，对比目标显式引入不变性。

<a id="paper-camdirector-world-cache"></a>

## CamDirector: Towards Long-Term Coherent Video Trajectory Editing

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yin_CamDirector_Towards_Long-Term_Coherent_Video_Trajectory_Editing_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yin_CamDirector_Towards_Long-Term_Coherent_Video_Trajectory_Editing_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 单帧重投影无法积累完整场景证据，长序列重采样容易漂移。
- **核心创新 / 方法** · 混合变换，将静态区融合为持续缓存，动态区直接变换，再以历史条件的自回归扩散细化。
- **Baseline** · 表1–2对照已有轨迹编辑；表3消融混合变换及条件。
- **Benchmark** · iPhone、iPhone-PTZ 的短片和全片设置，报告轨迹编辑质量及 VBench。
- **关键结果 / 消融** · 表1–3比较长序列一致性并检验缓存相关设计。
- **适用条件 / 局限** · 外参、深度和动静分离错误会进入持久缓存。

**可复用机制** · 长视频相机重拍时用世界坐标缓存静态背景、单独变换动态区域，并让后段复用历史。

<a id="paper-patch-forcing"></a>

## Denoising, Fast and Slow: Difficulty-Aware Adaptive Sampling for Image Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Schusterbauer_Denoising_Fast_and_Slow_Difficulty-Aware_Adaptive_Sampling_for_Image_Generation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Schusterbauer_Denoising_Fast_and_Slow_Difficulty-Aware_Adaptive_Sampling_for_Image_Generation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 全图同进度浪费算力；任意混合块时间步又会造成训练推理差距。
- **核心创新 / 方法** · 用信息量受限的块时间步采样训练和难度头，推理先更新容易块，再让其为困难块提供上下文。
- **Baseline** · 同架构同 NFE 的全局时间步，及原文表2–3现有扩散生成方案。
- **Benchmark** · ImageNet 256 类别条件生成及 T2I-CompBench++；比较生成质量、函数评估次数和组合能力。
- **关键结果 / 消融** · 表1固定架构与 NFE 仍报告收益，正文对照朴素块时间步并测自适应方案。
- **适用条件 / 局限** · 需修改训练和采样；难度预测及训练信息量与推理不匹配会损害效果。

**可复用机制** · 扩散以块为单位动态分配步数时，训练先限制跨块可见信息，避免产生推理见不到的提示。

<a id="paper-minimal-grounding-cot-generalization"></a>

## Revisiting the Necessity of Lengthy Chain-of-Thought in Vision-centric Reasoning Generalization

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Du_Revisiting_the_Necessity_of_Lengthy_Chain-of-Thought_in_Vision-centric_Reasoning_Generalization_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Du_Revisiting_the_Necessity_of_Lengthy_Chain-of-Thought_in_Vision-centric_Reasoning_Generalization_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 更长或用图的思维链可能只是早期优化更快，未必更有利于泛化。
- **核心创新 / 方法** · 在网格迷宫控制难度，统一用 SFT 后 RL，对比语言、坐标落点和图像操作监督，并逐步删去落点中可省的信息。
- **Baseline** · Qwen2.5-VL-7B 基座及长短语言、坐标和视觉链版本。
- **Benchmark** · 不同迷宫尺寸与 V*Bench、HR-Bench 4K、Frozenlake 等跨任务验证。
- **关键结果 / 消融** · 表 1 V*Bench 整体的精简落点 RL 为 85.86，视觉链 RL 为 83.25；迷宫比较显示视觉链主要加快训练，未提高最终上限。
- **适用条件 / 局限** · 依赖任务可以自动生成或验证落点；不能外推到需展示复杂中间状态的任务。

**可复用机制** · 制作视觉推理监督时应对比最少可核验落点与完整长轨迹，同时测收敛速度和未见难度的最终上限。见 §4.2、表 1。

<a id="paper-uni-dad-dual-domain-distillation"></a>

## Uni-DAD: Unified Distillation and Adaptation of Diffusion Models for Few-step Few-shot Image Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Bahram_Uni-DAD_Unified_Distillation_and_Adaptation_of_Diffusion_Models_for_Few-step_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Bahram_Uni-DAD_Unified_Distillation_and_Adaptation_of_Diffusion_Models_for_Few-step_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 分别适配再蒸馏或先蒸馏再适配会带来过拟合、细节平滑或少数样本反复生成。
- **核心创新 / 方法** · 单阶段匹配源和目标教师分布，让源域保持多样性，并用多尺度多头判别器约束目标真实性。
- **Baseline** · 对比从头少样本适配、DMD2-FT、FT-DMD2，以及无目标教师的版本。
- **Benchmark** · Babies、Sunglasses、MetFaces、Cats 十样本生成，以及主体个性化；测 FID、Intra-LPIPS 和生成步数。
- **关键结果 / 消融** · 表 1 Cats 的 3 步 FID 完整为 55.32，去目标教师为 199.91，但先适配再蒸馏为 51.85。
- **适用条件 / 局限** · 依赖可获得目标教师或较近源域，少样本 FID 方差和域差距应分别核查。

**可复用机制** · 少目标样本又要求少步采样时，应比较同时保留源教师和目标教师监督，与先迁移再蒸馏的效果。见表 1–2。

<a id="paper-reference-guided-causal-video-vae"></a>

## Real-Time Generation of Streamable Talking Portrait Video with Reference-Guided Deep Compression VAEs

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_Real-Time_Generation_of_Streamable_Talking_Portrait_Video_with_Reference-Guided_Deep_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_Real-Time_Generation_of_Streamable_Talking_Portrait_Video_with_Reference-Guided_Deep_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 高压缩因果视频 VAE 容易重复保存身份与静态背景，留给运动的信息不足。
- **核心创新 / 方法** · 允许多张参考图作为因果压缩条件，结合残差自编码分块生成后续视频。
- **Baseline** · 比较无参考、一至三张参考，以及去掉视频残差自编码。
- **Benchmark** · VoxCeleb2、HDTF 上用 L1、PSNR、LPIPS 检验 512 像素头像视频，并测推理速度。
- **关键结果 / 消融** · 表 2 HDTF 使用残差方案时，0 参考为 28.678 dB，3 参考为 35.374 dB；复用参考是主要收益来源之一。
- **适用条件 / 局限** · 静态身份和背景可复用是关键，剧烈遮挡、参考不匹配和跨镜头需复测；不应将头像指标外推到通用视频。

**可复用机制** · 压缩参考条件下的流视频时可绕过重复的静态外观编码，用参考图辅助因果 VAE 表示动态残差。见表 2。

<a id="paper-ae2vid-active-event-acquisition"></a>

## AE2VID: Event-based Video Reconstruction via Aperture Modulation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Bai_AE2VID_Event-based_Video_Reconstruction_via_Aperture_Modulation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Bai_AE2VID_Event-based_Video_Reconstruction_via_Aperture_Modulation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 运动事件主要覆盖变化区域，静态部分长时间没有观测会积累重建错误。
- **核心创新 / 方法** · 周期调光圈以获得携带强度的补充事件，并为主动事件和运动事件分别设处理网络。
- **Baseline** · 比较 E2VID、FireNet、ETNet、V2V-E2VID 等。
- **Benchmark** · EvAid、HQF 和采集的真实样本，测 MSE、SSIM、MS-SSIM、LPIPS。
- **关键结果 / 消融** · 表 1 EvAid 的 MSE 和 SSIM 为 0.037、0.707，V2V-E2VID 为 0.052、0.642；后者 LPIPS 略低 0.409 对 0.411。
- **适用条件 / 局限** · 需要可调光圈和同步机制，过快变化可能超过事件带宽，太长间隔也会积累漂移。

**可复用机制** · 事件视觉对静态区域信息不足时，可主动调节采集条件产生强度事件，并与仅靠场景运动的事件对照。见 §4、表 1–2。

<a id="paper-keyframe-anchored-inbetweening"></a>

## Anchoring and Rescaling Attention for Semantically Coherent Inbetweening

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Choi_Anchoring_and_Rescaling_Attention_for_Semantically_Coherent_Inbetweening_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Choi_Anchoring_and_Rescaling_Attention_for_Semantically_Coherent_Inbetweening_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 固定起终点仍对应多个合理路径，跨度变长后会语义漂移或运动断续。
- **核心创新 / 方法** · 给中间帧对关键帧和文本注意力增加偏置，同时重缩放时间 RoPE。
- **Baseline** · 比较不加两项、仅关键帧偏置、仅时间重缩放以及完整设置。
- **Benchmark** · TGI-Bench 的时间补帧与语义挑战，测长达 81 帧的 PSNR、SSIM、LPIPS、FID、FVD 和 VBench。
- **关键结果 / 消融** · 表 3 完整相对基线 LPIPS 0.3818 对 0.3945、VBench 10.022 对 9.904；仅重缩放的 PSNR 18.18，略高于完整 18.17。
- **适用条件 / 局限** · 关键帧相互冲突或文本未规定精确运动路径时，调整注意力不能保证动作可执行。

**可复用机制** · 生成式补帧跨度较大时，可分别对照关键帧条件强化和时间位置重缩放，估计语义与连贯性的取舍。见表 3。

<a id="paper-veridou-combined-verification"></a>

## Verifying Neural Network Robustness with Dual Perturbations

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Duong_Verifying_Neural_Network_Robustness_with_Dual_Perturbations_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Duong_Verifying_Neural_Network_Robustness_with_Dual_Perturbations_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 分别验证两类输入变化不能据此获得二者同时存在时的安全保证。
- **核心创新 / 方法** · 使用统一的形式化验收接口，对复合扰动明确区分已证明可靠、未证实和超时状态。
- **Baseline** · 比较只覆盖一项变化的验收及多种形式化求解设置。
- **Benchmark** · 共 14,340 项多领域验证实例，记录正确样本中的已证实比例与超时。
- **关键结果 / 消融** · 图 7 的低覆盖设定三求解配置已证实比例为 44.0%、47.7%、39.0%；提高覆盖时超时明显增加。
- **适用条件 / 局限** · 证明只适用于形式化假设和验证域，超时属于未知，不能计为安全或不安全。

**可复用机制** · 模型鲁棒验收应区分单一变化条件和复合变化条件的保证，单独报告求解超时。见实验部分、图 7。

<a id="paper-vertex-random-graph-adapter"></a>

## Beyond Graph Model: Reliable VLM Fine-Tuning via Random Graph Adapter

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Jiang_Beyond_Graph_Model_Reliable_VLM_Fine-Tuning_via_Random_Graph_Adapter_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Jiang_Beyond_Graph_Model_Reliable_VLM_Fine-Tuning_via_Random_Graph_Adapter_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 用确定性向量代表每个类别时，类描述的多样性与近邻类别关系难同时体现。
- **核心创新 / 方法** · 随机图顶点表示类别描述分布，概率消息传递传播类间语义，再按不确定性融合多个预测。
- **Baseline** · 对比 CLIP 原型、GraphAdapter、辅助分支及有无不确定性融合。
- **Benchmark** · ImageNet-1K 的 1–16 shot，另测域外分类和不同骨干。
- **关键结果 / 消融** · 表 3 的 ImageNet 1-shot 原型 59.42%，仅随机图 62.49%，完整 63.93%；16-shot 分别为 64.46%、66.03%、71.37%。
- **适用条件 / 局限** · 依赖可用的类别描述采样和类图质量，并应检验不确定性是否实际校准。

**可复用机制** · 少样本提示存在同名多属性时，可把每类文本适配为分布并传播类间消息，再和确定性图及辅助分类器做消融。见表 3。

<a id="paper-vgent"></a>

## VGent: Visual Grounding via Modular Design for Disentangling Reasoning and Prediction

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Kang_VGent_Visual_Grounding_via_Modular_Design_for_Disentangling_Reasoning_and_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Kang_VGent_Visual_Grounding_via_Modular_Design_for_Disentangling_Reasoning_and_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 直接自回归框坐标速度较慢，也可能输出缺乏视觉依据的位置。
- **核心创新 / 方法** · 冻结多模态编码器并以检测器框作为解码查询，查询经跨注意读取推理特征后选择目标。
- **Baseline** · 对照已有指代定位与分割器，表3–4比较解码监督及候选相关变体。
- **Benchmark** · 正文表1–2在 ORES 及 RefCOCO 系列评测分割和单目标指代。
- **关键结果 / 消融** · 正文显示模块化模型可保持底层定位和高层理解的独立升级，并消融精化组件。
- **适用条件 / 局限** · 目标必须在检测候选中，遇到漏检时更强推理不能恢复未知候选。

**可复用机制** · 把视觉推理留在冻结编码器，用候选框选择替代逐词元生成坐标，分别测召回上限和选择质量。

<a id="paper-hulluedit"></a>

## HulluEdit: Single-Pass Evidence-Consistent Subspace Editing for Mitigating Hallucinations in Large Vision-Language Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Lin_HulluEdit_Single-Pass_Evidence-Consistent_Subspace_Editing_for_Mitigating_Hallucinations_in_Large_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Lin_HulluEdit_Single-Pass_Evidence-Consistent_Subspace_Editing_for_Mitigating_Hallucinations_in_Large_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 统一缩放或多次解码可能压低真实视觉证据或增加延迟。
- **核心创新 / 方法** · 将隐藏状态拆成视觉证据、冲突先验和剩余不确定性，仅在选定子空间编辑。
- **Baseline** · 对照原模型、对比解码及不同内部编辑和消融组件。
- **Benchmark** · 正文表1–4在 POPE、MSCOCO CHAIR、MME 检查物体幻觉、描述幻觉及通用表现。
- **关键结果 / 消融** · 正文报告在不同模型上改善 POPE 与 CHAIR，同时测 MME 的细项。
- **适用条件 / 局限** · 保证只针对构造出的视觉分量，代理子空间不等同真实因果证据，应在新模型复验。

**可复用机制** · 抑制视觉幻觉时先隔离与证据正交的冲突分量，在同一次推理验收真实证据保留。

<a id="paper-livegesture"></a>

## LiveGesture: Streamable Co-Speech Gesture Generation Model

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Saleem_LiveGesture_Streamable_Co-Speech_Gesture_Generation_Model_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Saleem_LiveGesture_Streamable_Co-Speech_Gesture_Generation_Model_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 离线全身动作生成依赖未来语音，分区独立生成容易让肢体动作不同步。
- **核心创新 / 方法** · 因果词元化各区域，再用区域专家和因果跨区融合处理实时语音。
- **Baseline** · 正文表1比较已有语音动作模型，表2消融词元器、融合和音频编码。
- **Benchmark** · BEAT 基准，表1–2对照手势质量和流式条件。
- **关键结果 / 消融** · 正文报告在零前瞻下支持任意长度序列，并比较分区协调组件。
- **适用条件 / 局限** · 离线模型的生成质量不能直接代表同等延迟下的表现；复用需检查音频编码和动作同步。

**可复用机制** · 实时多区域动作应同时满足局部词元因果和跨区协调，分别评估无前瞻条件下的同步性。

<a id="paper-activityforensics-eval"></a>

## ActivityForensics: A Comprehensive Benchmark for Localizing Manipulated Activity in Videos

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Bao_ActivityForensics_A_Comprehensive_Benchmark_for_Localizing_Manipulated_Activity_in_Videos_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Bao_ActivityForensics_A_Comprehensive_Benchmark_for_Localizing_Manipulated_Activity_in_Videos_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 外观层面的防伪基准无法说明检测器是否发现动作语义发生改变。
- **核心创新 / 方法** · 建立行为层操纵的时间定位验收，并在域内、跨域和开放环境分别评测。
- **Baseline** · 比较 ActionFormer 和其他时间检测方法、加入防御特征正则的变体。
- **Benchmark** · ActivityForensics 的活动时间段，表2–4在多个时间重叠阈值报告 AP。
- **关键结果 / 消融** · 正文以跨域与开放环境单列结果，并在相同检测器上测特征正则的独立变化。
- **适用条件 / 局限** · 评测依赖操纵类型和视频来源，真实开放流量中的检出和误报需另验。

**可复用机制** · 防御评测要检验篡改时间段的定位和域外泛化，不能只验整段真假。

<a id="paper-affine-p3p"></a>

## Affine Perspective-Three-Point Problem

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Nakano_Affine_Perspective-Three-Point_Problem_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Nakano_Affine_Perspective-Three-Point_Problem_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 完整透视 P3P 的高次方程求解复杂，而仿射近似在深度变化大时偏差增大。
- **核心创新 / 方法** · 弱透视和伪透视先用双二次闭式解，再迭代校正到完整透视解。
- **Baseline** · 与精确 P3P 求解器及仿射变体比较。
- **Benchmark** · 合成数据、EPOS 和 IMC2023；正文表1–2以召回等位姿指标报告。
- **关键结果 / 消融** · 正文报告两次校正后的性能与所测强 P3P 求解器接近。
- **适用条件 / 局限** · 初值质量在深度跨度大、三点退化和强噪声时应另验。

**可复用机制** · 将便宜的近似几何闭式解作为初值，再用少次校正恢复精确相机模型。

<a id="paper-refacade"></a>

## Refacade: Editing Object with Given Reference Texture

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_Refacade_Editing_Object_with_Given_Reference_Texture_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_Refacade_Editing_Object_with_Given_Reference_Texture_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 原图和参考图都同时包含结构与材质，直接注入条件会互相干扰。
- **核心创新 / 方法** · 用配对网格渲染训练去纹理模块保留目标结构，再拼图打乱参考图的布局。
- **Baseline** · 对照直接以结构和原始参考图作为条件的方案，表3分别消融训练设计。
- **Benchmark** · UHRSD 图像和 Pexels 视频，测背景及前景 LPIPS、CLIP、DINO、DreamSim 等。
- **关键结果 / 消融** · 表1–3报告纹理相似和背景保持收益，并检验处理参考图与目标图的设计。
- **适用条件 / 局限** · 拼图适用于局部统计，但有方向、周期或长程边界的纹理可能受损。

**可复用机制** · 参考图纹理迁移时打乱参考全局结构，用局部纹理统计防止复制参考形状。

<a id="paper-diffusion-dataset-distribution-shift"></a>

## Mitigating The Distribution Shift of Diffusion-based Dataset Distillation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_Mitigating_The_Distribution_Shift_of_Diffusion-based_Dataset_Distillation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_Mitigating_The_Distribution_Shift_of_Diffusion-based_Dataset_Distillation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 小预算合成集既受复杂目标分布拖累，又可能仅因独立抽样覆盖失衡。
- **核心创新 / 方法** · 训练用 L1 稀疏促进紧凑流形，采样以分布约束同步去噪整个合成集。
- **Baseline** · 与常规独立采样扩散蒸馏及已有蒸馏方法比较。
- **Benchmark** · ImageNette、ImageWoof 与 ImageNet-1K，训练多种架构后测分类表现。
- **关键结果 / 消融** · 表1–2报告不同架构及蒸馏设置的性能改善。
- **适用条件 / 局限** · 联合优化需同时处理整个合成集，扩大预算会增加计算和内存。

**可复用机制** · 合成少量蒸馏样本时，联合去噪整批以控制覆盖，并在训练限制模型对原分布复杂性的拟合。

<a id="paper-moeactok"></a>

## MoEActok: A MoE-based Action Tokenizer for Vision-Language-Action Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_MoEActok_A_MoE-based_Action_Tokenizer_for_Vision-Language-Action_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_MoEActok_A_MoE-based_Action_Tokenizer_for_Vision-Language-Action_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 单码本同时编码多种技能会产生量化折衷。
- **核心创新 / 方法** · 聚类切分动作块，训练专家 VQ-VAE，并用前后适配器对齐专用潜空间与共享重建空间。
- **Baseline** · 单码本及不同 VLA 动作词元化方案，表3对技能及量化设计做消融。
- **Benchmark** · RoboTwin 12项模拟任务、Simpler-Env 4项模拟任务，报告操作成功率。
- **关键结果 / 消融** · 表1–3报告跨任务和 VLA 的成功率变化及专家方案对照。
- **适用条件 / 局限** · 动作块聚类不一定对应真实技能，混合动作和低频技能可能量化不良。

**可复用机制** · 多个技能共用动作词元时，按动作块聚类训练专家量化器，再映回共享动作空间。

<a id="paper-confidence-aware-optimal-correspondence"></a>

## COG: Confidence-aware Optimal Geometric Correspondence for Unsupervised Single-reference Novel Object Pose Estimation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Che_COG_Confidence-aware_Optimal_Geometric_Correspondence_for_Unsupervised_Single-reference_Novel_Object_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Che_COG_Confidence-aware_Optimal_Geometric_Correspondence_for_Unsupervised_Single-reference_Novel_Object_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 遮挡和离群点导致离散匹配不稳定，难端到端学习。
- **核心创新 / 方法** · 以点置信度确定软传输边际，按语义先验正则约束可匹配区域，再估计姿态。
- **Baseline** · 对照已有单参考姿态方法，并比较监督与无监督运行。
- **Benchmark** · LM-O、TUD-L、YCB-V，比较位姿与推理效率，TUD-L 另测重叠 IoU。
- **关键结果 / 消融** · 表1给出无监督情形接近所测监督方法的结果，表2检查重叠区域。
- **适用条件 / 局限** · 无共视或对称结构条件下仍会存在几何多解，置信度误差也会进入匹配。

**可复用机制** · 存在未重叠视野的位姿配准时，把点置信度作为最优传输边际，而非一一硬匹配。

<a id="paper-gvc1d"></a>

## Generative Video Compression with One-Dimensional Latent Representation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zheng_Generative_Video_Compression_with_One-Dimensional_Latent_Representation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zheng_Generative_Video_Compression_with_One-Dimensional_Latent_Representation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 二维潜栅格保留相邻块相似性，难集中复用跨帧内容。
- **核心创新 / 方法** · 使用紧凑一维潜词元，结合短长期上下文，以一维记忆传递长期信息。
- **Baseline** · 对照已有视频编解码器，表2–3比较词元数与有无长期记忆及自回归熵模型。
- **Benchmark** · 率失真比较，用 BD-Rate 衡量配置间压缩收益。
- **关键结果 / 消融** · 表2–3给出词元容量、记忆与熵建模对码率的影响。
- **适用条件 / 局限** · 生成式重建可能牺牲精确细节，感知品质与保真码率需分别评估。

**可复用机制** · 高压缩率下用不绑定二维位置的词元和长程记忆，减少局部及跨帧冗余。

<a id="paper-expose-pose-consistency"></a>

## ExPose: Reinforcing Video Generation Models for Extreme Pose Estimation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yoon_ExPose_Reinforcing_Video_Generation_Models_for_Extreme_Pose_Estimation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yoon_ExPose_Reinforcing_Video_Generation_Models_for_Extreme_Pose_Estimation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 视频看起来平滑并不保证生成帧满足共同三维几何。
- **核心创新 / 方法** · 以姿态评估得到的几何信号给生成视频作 GRPO 微调，再将中间帧作为辅助输入。
- **Baseline** · 与其他视频生成插值方案及下游估计器 VGGT、MapAnything 对照。
- **Benchmark** · DL3DV、NAVI、ScanNet、Cambridge Landmarks，考察宽视角间的相机位姿准确性。
- **关键结果 / 消融** · 表1–3报告在两种姿态估计器下的改善。
- **适用条件 / 局限** · 奖励依赖姿态估计器的可靠性，对几乎无共视的场景，生成帧可能引入错误结构。

**可复用机制** · 用生成中间帧辅助稀疏位姿估计时，用下游几何一致性奖励优化插值模型。

<a id="paper-flatness-aware-prompt-pretraining"></a>

## Improving Calibration in Test-Time Prompt Tuning for Vision-Language Models via Data-Free Flatness-Aware Prompt Pretraining

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Jang_Improving_Calibration_in_Test-Time_Prompt_Tuning_for_Vision-Language_Models_via_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Jang_Improving_Calibration_in_Test-Time_Prompt_Tuning_for_Vision-Language_Models_via_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 测试适配可导致过信，显式输出正则有时会损伤准确率。
- **核心创新 / 方法** · 用无标注数据的平坦感知提示预训练选择初值，不修改测试时适配算法。
- **Baseline** · 以 CLIP-ViT/B16 对照 TPT、DynaPrompt 的普通初值及 CoOp、MaPLe 学得初值。
- **Benchmark** · 在图像识别测试时提示调优中比较准确率与校准误差。
- **关键结果 / 消融** · 表1–3报告替换初值后两类指标改善，新增准备不增加测试时计算。
- **适用条件 / 局限** · 局部平坦度与校准的关系依赖损失和模型，跨域预测仍需实测。

**可复用机制** · 测试时提示词调优前，选平坦度更高的无数据初始化以改善置信校准。

<a id="paper-nesycr-cross-domain-procedure-checks"></a>

## Cross-Domain Demo-to-Code via Neurosymbolic Counterfactual Reasoning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Kim_Cross-Domain_Demo-to-Code_via_Neurosymbolic_Counterfactual_Reasoning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Kim_Cross-Domain_Demo-to-Code_via_Neurosymbolic_Counterfactual_Reasoning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 人类或仿真示范的步骤可能在目标机器人或不同环境下失效，即使视觉语义看似相同。
- **核心创新 / 方法** · 把示范抽象为符号状态序列，用目标观测找出不兼容条件并核验替代步骤。
- **Baseline** · 比较 Demo2Code、GPT4V-Robotics、Statler 等，另移除替代动作验证及反事实识别。
- **Benchmark** · 机器人跨域任务中比较仿真示范和人类视频示范，按环境差异量化成功率、流程符合度等。
- **关键结果 / 消融** · 表 3 组合变化设置中完整成功率 68.42%，去替代验证 50.00%，去反事实识别 47.37%。
- **适用条件 / 局限** · 依赖符号状态抽取和环境规则覆盖，未被模型表达的接触或安全约束仍需在真实部署前单独核验。

**可复用机制** · 示范迁移时，可先测试符号任务条件和可执行替代行为，再生成机器人任务代码。见表 3。

<a id="paper-adaptive-vlm-information-flow"></a>

## Aligning What Vision-Language Models See and Perceive with Adaptive Information Flow

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_Aligning_What_Vision-Language_Models_See_and_Perceive_with_Adaptive_Information_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_Aligning_What_Vision-Language_Models_See_and_Perceive_with_Adaptive_Information_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 视觉语言模型可以看到正确区域，却在解码时将注意力分给无关视觉信息而答错。
- **核心创新 / 方法** · 用各解码阶段的词元激活动态估计视觉词元重要性，再调整它向文本输出的可见性。
- **Baseline** · 比较标准因果掩码与信息流调整，区分遮挡高分和低分视觉词元。
- **Benchmark** · RealWorldQA、TextVQA、CountBench 等问答及定位任务，另比 POPE。
- **关键结果 / 消融** · 表 1 LLaVA-1.5-7B 人工调制的 RealWorldQA 为 61.6、TextVQA 49.9，标准掩码 55.6、47.8。
- **适用条件 / 局限** · 依赖白盒词元访问，人工诊断的数字不能等同自动版；OCR 小目标比一般分类更容易受错筛影响。

**可复用机制** · 图文模型定位正确但作答错时，应对照屏蔽关键与次要视觉词元，区分信息流和定位失败。见图 3、表 1。

<a id="paper-megadepth-x-sparse-view-sampling"></a>

## Long-Tail Internet Photo Reconstruction

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Long-Tail_Internet_Photo_Reconstruction_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Long-Tail_Internet_Photo_Reconstruction_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 网络照片有长尾视角质量和覆盖率，直接使用密集著名地标训练不会自动适应稀疏场景。
- **核心创新 / 方法** · 整理密集可重建照片，从中抽成不同间隔和视点覆盖的稀疏子集，再混合稠密与稀疏样本微调。
- **Baseline** · 对照原 π3、未清洗数据、随机视角抽取、纯稠密或纯稀疏。
- **Benchmark** · MegaDepth-X 难易集上测位姿 RRA、RTA、AUC 与点图误差，另测 RealEstate10K、DTU、ETH3D 等。
- **关键结果 / 消融** · 表 2 难集的 AUC@5 基座 36.93，随机抽取 47.17，完整方案 47.93；未清洗训练为 43.74。
- **适用条件 / 局限** · 模拟的稀疏模式仍来自可重建地点，对几乎无重叠、严重反射和罕见室内几何需另验。

**可复用机制** · 真实稀疏场景难获深度监督时，可从可重建密集场景按真实长尾的视角分布抽样，并保留清洗和抽样对照。见表 2。

<a id="paper-docseeker-evidence-resolution"></a>

## DocSeeker: Structured Visual Reasoning with Evidence Grounding for Long Document Understanding

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yan_DocSeeker_Structured_Visual_Reasoning_with_Evidence_Grounding_for_Long_Document_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yan_DocSeeker_Structured_Visual_Reasoning_with_Evidence_Grounding_for_Long_Document_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 无关页会稀释信号，只提供短答案监督也不会教会模型定位支持页。
- **核心创新 / 方法** · 以分析、页定位和推理做有结构监督，再联合奖励证据及答案；训练时按页证据分配视觉分辨率。
- **Baseline** · 比较短答案、普通 CoT、证据结构训练、固定低分辨率及截断高分辨率。
- **Benchmark** · DUDE 等五套长文档；表 4 的 MMLong. 报准确率与 F1。
- **关键结果 / 消融** · 表 4 完整页证据分配的准确率/F1 为 38.6/36.9；固定低分辨率为 34.2/33.5。
- **适用条件 / 局限** · 依赖正确页证据；跨页互补或关键小字可能因误降分辨率而丢失，需记录证据召回和视觉预算。

**可复用机制** · 长视觉文档训练应同步验收页证据和回答，并只给相关页高分辨率。见表 3–4。

<a id="paper-flashin-learned-inversion"></a>

## FlashIn: Fast and Accurate Image Inversion for Real-time Image Editing

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_FlashIn_Fast_and_Accurate_Image_Inversion_for_Real-time_Image_Editing_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_FlashIn_Fast_and_Accurate_Image_Inversion_for_Real-time_Image_Editing_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 逐步反演耗时且会产生累计重建差，导致编辑后背景改变。
- **核心创新 / 方法** · 训练图像到噪声的直接映射，使用可知来源噪声的合成图做循环监督，并用真实图对抗训练。
- **Baseline** · 对比现有图像反演和编辑方法、无循环与无对抗训练版本。
- **Benchmark** · PIE-Bench，报告背景 PSNR、SSIM、CLIP 及 A100 上的时间。
- **关键结果 / 消融** · 表 2 无两项为 26.19 dB，加入循环为 28.40，两项齐全为 31.91。
- **适用条件 / 局限** · 映射与生成骨干和反演分布耦合，复杂真实内容仍需独立检查噪声重建和编辑可控性。

**可复用机制** · 需交互速度的图像编辑可用合成图和已知起始噪声训练直接反演，再以真实图像验背景保真。见表 1–2。

<a id="paper-adaptive-3d-watermark-quality-tradeoff"></a>

## Write Where It Matters: Policy-Guided Watermarks for 3D Gaussian Splatting

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Write_Where_It_Matters_Policy-Guided_Watermarks_for_3D_Gaussian_Splatting_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Write_Where_It_Matters_Policy-Guided_Watermarks_for_3D_Gaussian_Splatting_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 水印策略一刀切会增加画质损失，逐基元优化又会带来较高训练成本。
- **核心创新 / 方法** · 依据场景对区域级锚分配水印强度，以渲染保真和提取可靠性共同评估。
- **Baseline** · 比较固定嵌入策略、逐基元强化学习和区域锚策略。
- **Benchmark** · Blender 等三维资产上测 32–64 位的提取准确率、PSNR、SSIM、LPIPS 与训练开销。
- **关键结果 / 消融** · 表 4 的 48 位区域锚方案准确率 96.76%、9 分钟、9.52 GB，逐基元为 98.97%、42 分钟、16.04 GB。
- **适用条件 / 局限** · 适用于支持结构锚的高斯表示，提取可靠性依赖所测渲染和变换；仍需在合法资产工作流上核查画质。

**可复用机制** · 为三维资产做内容溯源时，可用区域级嵌入预算避免逐基元训练，并同时验收画质和提取率。见表 4–5。

<a id="paper-covft"></a>

## CoVFT: Context-aware Visual Fine-tuning for Multimodal Large Language Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhou_CoVFT_Context-aware_Visual_Fine-tuning_for_Multimodal_Large_Language_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhou_CoVFT_Context-aware_Visual_Fine-tuning_for_Multimodal_Large_Language_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 跨论文配置差异掩盖视觉微调收益，统一视觉更新在不同上下文可能相互冲突。
- **核心创新 / 方法** · 提取上下文向量以调节视觉专家，将不同输入的更新信号分开。
- **Baseline** · 统一 LLaVA-1.5 配置比较冻结与已有微调，另对照稠密、稀疏、随机及均匀专家使用。
- **Benchmark** · 表1–3在12个多模态基准上测视觉微调、上下文提取及跨架构表现。
- **关键结果 / 消融** · 多种视觉微调未稳定超越冻结；正文表2的稠密专家优于 Sparse@2，随机激活和均匀权重未带来稳定改善。
- **适用条件 / 局限** · 不同骨干和数据配比会改变冲突强度，稠密专家成本及稀疏专家欠训练需单测。

**可复用机制** · 视觉骨干解冻前先和同配置冻结基线比较；当不同多模态上下文梯度冲突时，考虑上下文条件化适配。

<a id="paper-faster-gs-optimization"></a>

## Faster-GS: Analyzing and Improving Gaussian Splatting Optimization

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Hahlbohm_Faster-GS_Analyzing_and_Improving_Gaussian_Splatting_Optimization_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Hahlbohm_Faster-GS_Analyzing_and_Improving_Gaussian_Splatting_Optimization_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 既有结果混合了算法变化与实现优化，难以判断真实速度和质量损失。
- **核心创新 / 方法** · 整合高斯截断、梯度近似和数值优化，分别测各组件及反向中的优化器更新。
- **Baseline** · 对照原始 3DGS 与已有加速实现，并逐项消融。
- **Benchmark** · Mip-NeRF360、Tanks and Temples、Deep Blending；表1–4评训练时间、峰值显存和渲染质量，含不同显卡。
- **关键结果 / 消融** · 表4正文称 RTX 5090 上平均163秒、较原始实现加速约5倍；提速随显卡代际变化。
- **适用条件 / 局限** · 上述速度是整套组合结果，单个近似引起的画质退化应在目标硬件和场景另测。

**可复用机制** · 三维优化提速应固定重建质量，再单独对照算子实现、优化器更新和数值近似。

<a id="paper-diversegrpo"></a>

## DiverseGRPO: Mitigating Mode Collapse in Image Generation via Diversity-Aware GRPO

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_DiverseGRPO_Mitigating_Mode_Collapse_in_Image_Generation_via_Diversity-Aware_GRPO_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_DiverseGRPO_Mitigating_Mode_Collapse_in_Image_Generation_via_Diversity-Aware_GRPO_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 只给高质量单样本奖励会使同提示输出聚集于少数模式。
- **核心创新 / 方法** · 用同提示候选的语义簇定义分布多样性奖励，并给早期去噪更多多样性正则。
- **Baseline** · 与普通 GRPO、其他生成奖励及去掉分布奖励或阶段正则的配置比较。
- **Benchmark** · 正文在多个视觉生成骨干与奖励模型上比较感知质量和语义多样性，并跟踪随训练迭代的变化。
- **关键结果 / 消融** · 正文消融显示分组奖励提高候选语义多样性，分阶段正则减缓训练后期多样性下降。
- **适用条件 / 局限** · 语义簇的细粒度取决于特征和样本数量，质量和覆盖必须同时测。

**可复用机制** · 生成强化学习同时验收样本质量和同提示分布覆盖，并把多样性正则按去噪阶段分配。

<a id="paper-dynuav-motion-failure-audit"></a>

## Breaking Smooth-Motion Assumptions: A UAV Benchmark for Multi-Object Tracking in Complex and Adverse Conditions

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Ye_Breaking_Smooth-Motion_Assumptions_A_UAV_Benchmark_for_Multi-Object_Tracking_in_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Ye_Breaking_Smooth-Motion_Assumptions_A_UAV_Benchmark_for_Multi-Object_Tracking_in_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 相对稳定的测试场景可能高估平滑运动假设的可用范围。
- **核心创新 / 方法** · 用动态相机和视角变化构造压力评测，对照常用数据与相机运动补偿。
- **Baseline** · 比较 BoostTrack、ByteTrack、OC-SORT 等在常见数据和动态数据的效果。
- **Benchmark** · 正文表3–4使用 DynUAV、MOT-17、MOT-20、DanceTrack，报告 MOTA、IDF1 和 HOTA。
- **关键结果 / 消融** · 表4中 ByteTrack 的 MOTA 相对 MOT-17 低17.27分，IDF1 低16.52分。
- **适用条件 / 局限** · 跨数据集差值也受类别、标注和环境差异影响，不能把完整差值归因于自运动。

**可复用机制** · 良性移动相机跟踪应把检测和关联拆开，在不平滑自运动下验收两者。

<a id="paper-action-geometry-prediction"></a>

## Action-Geometry Prediction with 3D Geometric Prior for Bimanual Manipulation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_Action-Geometry_Prediction_with_3D_Geometric_Prior_for_Bimanual_Manipulation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_Action-Geometry_Prediction_with_3D_Geometric_Prior_for_Bimanual_Manipulation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 二维语义不能明确表达双臂和对象的空间约束，真实点云也不总可用。
- **核心创新 / 方法** · 融合 RGB 提取的三维几何先验、二维语义和本体信号，联合扩散预测动作与可解码为点图的未来三维潜变量。
- **Baseline** · 比较二维和显式三维输入策略，并检验联合几何预测。
- **Benchmark** · RoboTwin 仿真与实机；按16项选臂、8项同步双臂和8项顺序协作报告三随机种子成功率。
- **关键结果 / 消融** · 表1–3报告多任务组的成功率改善及方差。
- **适用条件 / 局限** · 依赖视觉几何先验准确，遮挡与快速形变可能造成未来潜变量偏差。

**可复用机制** · 双臂策略学习时把未来三维几何和动作块作为同一预测问题。

<a id="paper-laver-latent-visual-reconstruction"></a>

## Unleashing the Intrinsic Visual Representation Capability of Multimodal Large Language Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Unleashing_the_Intrinsic_Visual_Representation_Capability_of_Multimodal_Large_Language_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Unleashing_the_Intrinsic_Visual_Representation_Capability_of_Multimodal_Large_Language_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 逐层只受文本预测监督可能导致视觉特征趋同，密集感知下降。
- **核心创新 / 方法** · 在语言模型共享潜空间构造掩码视觉恢复监督，无需在像素层重建。
- **Baseline** · 同架构原模型、其他基于重建的基线，并消融空间感知和损失组成。
- **Benchmark** · VLMEvalKit 多模态任务以及更复杂的密集视觉任务，表1–3报告百分比分数。
- **关键结果 / 消融** · 原文比较多种架构并报告密集视觉优势，注意力诊断显示模型更多使用视觉信息。
- **适用条件 / 局限** · 合适的重建层和目标取决于潜表示，注意力比例不能单独证明感知因果性。

**可复用机制** · 纯文本词元训练让视觉表示退化时，在共享语义空间加入掩码视觉重建。

<a id="paper-motionnft"></a>

## MotionEdit: Benchmarking and Learning Motion-Centric Image Editing

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wan_MotionEdit_Benchmarking_and_Learning_Motion-Centric_Image_Editing_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wan_MotionEdit_Benchmarking_and_Learning_Motion-Centric_Image_Editing_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 通用编辑奖励往往偏向纹理及语义外观，忽略动作或交互变化。
- **核心创新 / 方法** · 从连续视频构造动作编辑对，用运动对齐的正负训练信号微调，再用相应基准测量。
- **Baseline** · 与 Step1X-Edit、BAGEL、AnyEdit、MagicBrush 等比较，表3对照只用多模态奖励。
- **Benchmark** · MotionEdit-Bench，使用生成、判别和偏好类指标测试运动编辑与主体保持。
- **关键结果 / 消融** · 表1显示通用编辑器在此任务的不足，表3报告专门运动反馈相对单一奖励的改善。
- **适用条件 / 局限** · 抽帧主要涵盖视频已有动作，动作与相机移动的区分及域外动作需核验。

**可复用机制** · 动作编辑后训练中，用独立运动对齐信号区分动作正确和仅在外观上像目标。

<a id="paper-anymc3d-frozen-2d-transfer"></a>

## Revisiting 2D Foundation Models for Scalable 3D Medical Image Classification

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_Revisiting_2D_Foundation_Models_for_Scalable_3D_Medical_Image_Classification_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_Revisiting_2D_Foundation_Models_for_Scalable_3D_Medical_Image_Classification_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 医学专用预训练与三维架构的价值容易被数据量、适配方式和任务覆盖混淆。
- **核心创新 / 方法** · 以冻结二维骨干和每任务轻量插件适配三维输入，并有控制地比较预训练域与二维/三维架构。
- **Baseline** · 通用与医学基础模型、原生三维模型及二维或2.5D 分类器。
- **Benchmark** · 12项跨解剖、病理及成像模态任务；表2在10项对照结果与可训练参数。
- **关键结果 / 消融** · 所测正确适配下通用模型可匹配医学专用骨干，二维路径在所测三维分类中强，每任务约100万可训练参数。
- **适用条件 / 局限** · 结论限于所测分类，不能据此推断三维分割或体积几何任务。

**可复用机制** · 三维分类资源有限时，先以冻结通用二维基础模型和轻量多视角适配作受控基线。

<a id="paper-anatomica-local-constraints"></a>

## Anatomica: Localized Control over Geometric and Topological Properties for Anatomical Diffusion Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Kadry_Anatomica_Localized_Control_over_Geometric_and_Topological_Properties_for_Anatomical_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Kadry_Anatomica_Localized_Control_over_Geometric_and_Topological_Properties_for_Anatomical_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 全局条件不容易精确控制局部结构的几何或连通性。
- **核心创新 / 方法** · 推理时在指定子域以体素矩约束位置、形状等，以持久同调约束连通体、环、空腔，利用神经场对潜扩散做局部解码。
- **Baseline** · 表1比较不同几何控制方式，表2–3比较几何与拓扑约束结果。
- **Benchmark** · 三维多类解剖分割生成，报告目标几何吻合、样本质量及 Betti 精确率。
- **关键结果 / 消融** · 表2–3量化局部控制满足程度及生成保真。
- **适用条件 / 局限** · 约束域和目标必须预先定义，局部约束可能彼此冲突，合成分割不代表真实分布。

**可复用机制** · 需要区域级三维形状控制时，只解码目标子域并组合可微几何与拓扑约束。

<a id="paper-edit-r1-verifier-reward"></a>

## Leveraging Verifier-Based Reinforcement Learning in Image Editing

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Guo_Leveraging_Verifier-Based_Reinforcement_Learning_in_Image_Editing_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Guo_Leveraging_Verifier-Based_Reinforcement_Learning_in_Image_Editing_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 整体打分掩盖编辑漏项或不该改变的区域，导致强化学习信号偏置。
- **核心创新 / 方法** · 训练可推理的验证奖励模型，先拆编辑要求，再逐项核对前后图并聚合，最后用于下游编辑强化学习。
- **Baseline** · 对照传统奖励模型及仅思考、仅验证、两者结合的设置。
- **Benchmark** · 内部验证准确率，GEdit-Bench-EN 报告11个编辑类别的 SC 等。
- **关键结果 / 消融** · 表2比较验证拆解收益，表3比较接入强化学习后的编辑表现。
- **适用条件 / 局限** · 验证器可能偏见、漏项或依赖可见证据，聚合权重仍影响行为。

**可复用机制** · 多条件图像编辑策略训练时，把一条指令拆成可核查要求再聚合奖励。

<a id="paper-unicompress-bidirectional-token-bottleneck"></a>

## UniCompress: Token Compression for Unified Vision-Language Understanding and Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_UniCompress_Token_Compression_for_Unified_Vision-Language_Understanding_and_Generation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_UniCompress_Token_Compression_for_Unified_Vision-Language_Understanding_and_Generation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 同一自回归骨干处理图像理解和生成时，大量视觉词元拉高成本，而生成端还需保留局部信息。
- **核心创新 / 方法** · 在既有统一骨干外挂由全局可学习词元引导的压缩及解压模块，无需全量重训。
- **Baseline** · 比较 UniTok、VILA-U 原版及其压缩版本，另消融局部聚合方法。
- **Benchmark** · 用标准视觉理解任务和 MJHQ-30K 图像生成测任务成绩、FID、图文相似度；表 3 单测墙钟。
- **关键结果 / 消融** · 表 3 UniTok 的生成推理由 32.25 降为 18.96 分钟，理解推理仅由 5.41 降为 5.25 分钟。
- **适用条件 / 局限** · 解压不能保证恢复已丢失细节；不同负载下两条路径的成本收益需分开验证。

**可复用机制** · 统一图像理解和生成可在主模型前压缩、在生成解码前恢复局部视觉词元，独立测两条路径的墙钟时间。见表 1–3。

<a id="paper-sparse-point-future-ensembles"></a>

## Envisioning the Future, One Step at a Time

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Baumann_Envisioning_the_Future_One_Step_at_a_Time_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Baumann_Envisioning_the_Future_One_Step_at_a_Time_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 预测稠密外观会挤占搜索大量运动未来的计算，而单个预测会忽略结果不确定性。
- **核心创新 / 方法** · 对稀疏点轨迹做逐短步自回归扩散，并在滚动中生成多个未来。
- **Baseline** · 对照 MAGI、Wan、CV-X、SRv2、SVD 等视频预测及二维轨迹训练变体。
- **Benchmark** · 开放世界及物理约束的运动预测，用最佳 5 个及五分钟预算中的备选最小误差评估，另测台球规划。
- **关键结果 / 消融** · 表 1 和图 10 显示少量候选时已可比，按墙钟允许多采样时差距更大；作者用 665M 参数模型报告结果。
- **适用条件 / 局限** · 最小误差指标受样本数及候选挑选器影响；稀疏点不必保留接触力、遮挡或任务语义，部署需检验平均质量。

**可复用机制** · 探索大量未来时，可以把稠密视频预测换成短步自回归点轨迹，并同时比较等样本和等墙钟的最好候选。见表 1、图 10。

<a id="paper-metom-codec-guided-token-merging"></a>

## MeToM: Metadata-Guided Token Merging for Efficient Video LLMs

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_MeToM_Metadata-Guided_Token_Merging_for_Efficient_Video_LLMs_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wu_MeToM_Metadata-Guided_Token_Merging_for_Efficient_Video_LLMs_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 固定删词元忽略镜头与区域复杂度差异，编码完成后才筛也省不掉视觉编码成本。
- **核心创新 / 方法** · 用视频编解码残差信号指示空间密度，用 GoP 包大小指示时间复杂度，在编码前分配并合并视觉词元。
- **Baseline** · 比较 FastV、ToMe、DyCoke、STTM、HoliTom 和全词元。
- **Benchmark** · VideoMME、LongVideoBench、MLVU、EgoSchema、NExT-QA；测相对完整模型的准确率、TTFT 与视觉词元数。
- **关键结果 / 消融** · 表 1 在约 30% 词元预算中，五任务平均相对准确率为 101.2%，平均相对 TTFT 为 27.3%。
- **适用条件 / 局限** · 依赖输入视频保有可解释的编码元数据；强压缩、重编码及小而静态的关键线索应独立分组复测。

**可复用机制** · 视频问答压缩可用现成编码元数据决定每帧预算与空间合并位置，再用端到端首词元时延核算。见表 1–4。

<a id="paper-pmatrack-progressive-rgbt-alignment"></a>

## Progressive Multi-cue Alignment for Unaligned RGBT Tracking

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Jin_Progressive_Multi-cue_Alignment_for_Unaligned_RGBT_Tracking_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Jin_Progressive_Multi-cue_Alignment_for_Unaligned_RGBT_Tracking_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 一次拟合全部跨模态偏移既容易失败，也为轻度偏移过度计算。
- **核心创新 / 方法** · 把中心、尺度及剩余局部偏差分段估计，按难度启用空间线索。
- **Baseline** · 比较无对齐主干及逐项使用组件，另对照现有 RGBT 跟踪器。
- **Benchmark** · LasHeR-Unaligned、MUART244 用 PR、NPR、SR 与 FLOPs。
- **关键结果 / 消融** · 表 3 MUART244 的 PR/NPR/SR 从 58.7/51.1/42.1 变为 62.7/55.9/45.8，完整 FLOPs 为 72.6G。
- **适用条件 / 局限** · 依赖两通道仍有共同可定位目标；极端非重叠、异步或尺度错位需要独立验证。

**可复用机制** · 视野未标定的红外可见跟踪宜分开估计平移、尺度和局部残差，并依对齐难度选择提示。见表 3。

<a id="paper-dynamicvggt-future-point-map"></a>

## DynamicVGGT: Learning Dynamic Point Maps for 4D Scene Reconstruction in Autonomous Driving

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/He_DynamicVGGT_Learning_Dynamic_Point_Maps_for_4D_Scene_Reconstruction_in_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/He_DynamicVGGT_Learning_Dynamic_Point_Maps_for_4D_Scene_Reconstruction_in_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 静态前馈几何网络在运动物体和变视角下不能维持跨帧点对应。
- **核心创新 / 方法** · 在同一参考坐标预测各时刻点图，以运动注意力连接帧，再用显式运动头给高斯估速度。
- **Baseline** · 比较原 VGGT、加动态点图及运动注意力的消融和已有场景重建模型。
- **Benchmark** · KITTI 单目及 Waymo 三摄像头片段测点图精度、完整性和法向一致性，也评新视图及单目深度。
- **关键结果 / 消融** · 正文表 4 把动态约束和时序模块逐项加入，报告 KITTI 和 Waymo 的点图改善；两者的输入视角协议不同。
- **适用条件 / 局限** · 依赖参考坐标稳定，快速突变、非车载场景和跟踪标签长时正确性需另测。

**可复用机制** · 动态三维网络可在共享世界坐标直接联合预测当前和未来点图，显式测对应连续性而非只评逐帧几何。见表 4。

<a id="paper-self-e-any-step-self-evaluation"></a>

## Self-Evaluation Unlocks Any-Step Text-to-Image Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yu_Self-Evaluation_Unlocks_Any-Step_Text-to-Image_Generation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yu_Self-Evaluation_Unlocks_Any-Step_Text-to-Image_Generation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 常规流匹配依赖许多采样步；借助已有教师的蒸馏又要求额外可用模型。
- **核心创新 / 方法** · 用模型自己的分数估计评估生成样本，与瞬时局部监督一起训练，不需要预训练教师。
- **Baseline** · 比较 Flow Matching、IMM；消融目标归一化和全程开启辅助损失。
- **Benchmark** · GenEval 对 2、4、8、50 步的生成做同训练迭代比较。
- **关键结果 / 消融** · 表 2 在 300K 迭代，两步 Self-E 为 0.6097，Flow Matching 为 0.2523；50 步为 0.7543 与 0.7311。
- **适用条件 / 局限** · 自评分会随训练阶段变化，辅助项过早使用会有退化；分数收益需要进一步核对视觉伪影和实际延迟。

**可复用机制** · 希望从头训练可任意步数生成的模型时，应试验局部流目标加自评全局匹配，分别看极少步和多步质量。见表 2。

<a id="paper-avatar-av-rl"></a>

## AVATAR: Reinforcement Learning to See, Hear, and Reason Over Video

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Kulkarni_AVATAR_Reinforcement_Learning_to_See_Hear_and_Reason_Over_Video_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Kulkarni_AVATAR_Reinforcement_Learning_to_See_Hear_and_Reason_Over_Video_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 近似相同的采样结果让组相对奖励没有梯度，均匀权重还忽略计划和汇总阶段。
- **核心创新 / 方法** · 用分层回放复用异策略样本，并以阶段加权区分计划、主体推理与总结。
- **Baseline** · 对照 GRPO、无分层回放、均匀及反向阶段权重。
- **Benchmark** · 表2–5用 OmniBench、DailyOmni、MMVU、Video-Holmes 等音视频和视频推理题。
- **关键结果 / 消融** · 图5所示实验在1600次独立生成达0.80，GRPO 在8000次后仍未达到；表5单独对照阶段权重。
- **适用条件 / 局限** · 旧样本会出现策略漂移，首尾权重也未必适于所有轨迹长度和任务。

**可复用机制** · 组内优势消失时从含不同奖励的历史轨迹补信号，并单独检验推理首尾的信用权重。

<a id="paper-semantic-first-diffusion"></a>

## Semantics Lead the Way: Harmonizing Semantic and Texture Modeling with Asynchronous Latent Diffusion

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Pan_Semantics_Lead_the_Way_Harmonizing_Semantic_and_Texture_Modeling_with_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Pan_Semantics_Lead_the_Way_Harmonizing_Semantic_and_Texture_Modeling_with_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 同步去噪没有利用语义结构较早确定的生成顺序。
- **核心创新 / 方法** · 组合独立语义潜量和纹理潜量，以不同噪声日程让语义先形成。
- **Baseline** · 表3对比基础模型、REPA、加 SemVAE 及加入语义优先，表5另验证 ReDi。
- **Benchmark** · ImageNet 类条件图像生成，使用 FID 等指标。
- **关键结果 / 消融** · 表3在 REPA 与 SemVAE 已启用时，加入语义优先使 FID 从5.24降到3.03；表5在 ReDi 为5.33降至4.41。
- **适用条件 / 局限** · 依赖语义表示确实反映目标构图，同步任务及强局部条件下需复测。

**可复用机制** · 语义和纹理采用错开的去噪日程，对照同步去噪能否改善细节形成。

<a id="paper-aard-geometry-noise"></a>

## Geometry-Aligned and Anomaly-Aware Reconstruction for 3D Anomaly Detection

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_Geometry-Aligned_and_Anomaly-Aware_Reconstruction_for_3D_Anomaly_Detection_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wu_Geometry-Aligned_and_Anomaly-Aware_Reconstruction_for_3D_Anomaly_Detection_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 无约束随机噪声会扰动法向和局部表面，重建残差混入正常区域误差。
- **核心创新 / 方法** · 逐步沿法向校准扰动方向并维持图结构，加入面向异常的参考条件。
- **Baseline** · 对照其他三维异常检测器，表4消融几何和参考组件。
- **Benchmark** · Real3D-AD、Anomaly-ShapeNet；正文表1–4报告对象及点级 AUROC。
- **关键结果 / 消融** · 正文分开测对象级和点级检出，并用表4检验几何约束及条件贡献。
- **适用条件 / 局限** · 法向不可靠、表面稀疏或扫描噪声变化会影响约束效果。

**可复用机制** · 点云复原的扰动分布可按局部表面几何约束，再测是否兼顾结构保留和异常定位。

<a id="paper-versecrafter-4d-control"></a>

## VerseCrafter: Dynamic Realistic Video World Model with 4D Geometric Control

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zheng_VerseCrafter_Dynamic_Realistic_Video_World_Model_with_4D_Geometric_Control_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zheng_VerseCrafter_Dynamic_Realistic_Video_World_Model_with_4D_Geometric_Control_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 仅用二维控制图容易把相机运动和物体运动混为一谈。
- **核心创新 / 方法** · 以静态点云与动态高斯轨迹编码世界状态，渲染时空控制图引导视频生成。
- **Baseline** · 表1–2对比相机与对象控制基线，表3消融掩码、深度及几何表达。
- **Benchmark** · VerseControl4D 测 VBench-I2V、旋转等三维控制误差及单相机条件。
- **关键结果 / 消融** · 表3对比三维表示和解耦控制，正文分别报告观感与几何控制结果。
- **适用条件 / 局限** · 条件质量依赖初始几何及物体轨迹，视频可控不保证物理可执行。

**可复用机制** · 视频世界模型把静态几何、对象轨迹和镜头变化分开表示，在同一条件下核查几何与观感。

<a id="paper-physskin"></a>

## PhysSkin: Real-Time and Generalizable Physics-Based Animation via Self-Supervised Neural Skinning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Lei_PhysSkin_Real-Time_and_Generalizable_Physics-Based_Animation_via_Self-Supervised_Neural_Skinning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Lei_PhysSkin_Real-Time_and_Generalizable_Physics-Based_Animation_via_Self-Supervised_Neural_Skinning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 高维物理模拟成本高，依赖拓扑的皮肤权重难迁移到其他网格。
- **核心创新 / 方法** · 学习连续皮肤权重场，将低维控制变换提升为完整空间形变，以自监督能量和冲突感知梯度约束训练。
- **Baseline** · 在 RigNet 和 ShapeNet 对照既有方法，表3比较逐步仿真开销并在表4做消融。
- **Benchmark** · 正文表1–4报告权重表现、逐步耗时、正交性与条件性。
- **关键结果 / 消融** · 表3在10K元素飞机上所提方法为12.26毫秒，表列另两方法为79.83及141.83毫秒。
- **适用条件 / 局限** · 泛化受控制柄布局及物理目标影响，复杂碰撞时需重新验证变形和能量误差。

**可复用机制** · 把连续形变基从离散网格中分离，检验同一子空间是否可迁移到不同几何采样。

<a id="paper-reliqs-quality-aware-saliency"></a>

## Learning Where to Look and How to Judge: Resolution-agnostic Image Quality Assessment with Quality-aware Saliency

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Gedik_Learning_Where_to_Look_and_How_to_Judge_Resolution-agnostic_Image_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Gedik_Learning_Where_to_Look_and_How_to_Judge_Resolution-agnostic_Image_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 统一缩图会丢掉微小失真，拼接主观评分也会混入量表差异。
- **核心创新 / 方法** · 多尺度采样固定大小块，由 CLIP 编码后预测质量显著性，用少量块汇聚潜在质量分。
- **Baseline** · 对照单数据训练和多数据训练下的现有无参考质量模型。
- **Benchmark** · KonIQ-10K 训练及其他真实、合成、AIGC 数据测试，另测 UHD；报告 PLCC 和 SRCC。
- **关键结果 / 消融** · 表1–3比较不同训练和分辨率的相关性，支持保留原始分辨率特征。
- **适用条件 / 局限** · 稀疏采样可能漏局部缺陷，质量轴是否跨人群和评价量表一致仍需验证。

**可复用机制** · 高分辨率质量评估使用按预算选择的原尺寸小块，并以潜在评分轴联合不同数据集。

<a id="paper-fbta-feature-bridging"></a>

## FBTA: Enabling Single-GPU End-to-End Gigapixel WSI Classification with Feature Bridging and Translation Alignment

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Dong_FBTA_Enabling_Single-GPU_End-to-End_Gigapixel_WSI_Classification_with_Feature_Bridging_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Dong_FBTA_Enabling_Single-GPU_End-to-End_Gigapixel_WSI_Classification_with_Feature_Bridging_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 冻结提取器有下游语义差距，整图端到端训练又超出单卡显存。
- **核心创新 / 方法** · 把可梯度优化的端到端特征袋与冻结特征袋桥接，以翻译特征对齐训练和推理过程。
- **Baseline** · 同提取器和 MIL 有无 FBTA 对照，覆盖 ABMIL、MambaMIL 及监督或自监督初始化。
- **Benchmark** · TCGA-NSCLC 的 Shot20/50/100 和 TCGA-STAD；用 AUC、ACC、F1 及单卡显存评估。
- **关键结果 / 消融** · 作者报告单24 GB GPU 可训练，ResNet-50 下 ABMIL 在 Shot50 和 STAD 准确率改善13.1%和15.8%。
- **适用条件 / 局限** · 特征翻译需保留任务信息，证据以全切片分类为主。

**可复用机制** · 高分辨率多实例学习显存不足时，将端到端、冻结以及可部署的翻译特征袋分别用于优化、稳定和推理。

<a id="paper-tqd-video-diffusion"></a>

## Beyond the Golden Data: Resolving the Motion-Vision Quality Dilemma via Timestep Selective Training

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Luo_Beyond_the_Golden_Data_Resolving_the_Motion-Vision_Quality_Dilemma_via_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Luo_Beyond_the_Golden_Data_Resolving_the_Motion-Vision_Quality_Dilemma_via_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 运动丰富与外观清晰往往不能兼得，只挑双高样本会损失训练覆盖。
- **核心创新 / 方法** · 用梯度分析找质量不均数据有效的时间步，偏向在高噪声步采运动丰富样本、低噪声步采视觉清晰样本。
- **Baseline** · 对照统一时间步采样、各种筛选数据设置，表3分解时间步策略。
- **Benchmark** · Wan 视频训练等设置，VBench、VideoAlign，VideoPhy2 用主体对齐和提示一致性。
- **关键结果 / 消融** · 表1–3报告针对采样时间步分配可改善运动与视觉综合表现。
- **适用条件 / 局限** · 时间步与所学内容的关系依赖噪声调度和数据质量测量，需针对骨干复核。

**可复用机制** · 视频去噪训练时根据样本的运动和画质差异调整采样时间步。

<a id="paper-agile-deliberation"></a>

## Agile Deliberation: Concept Deliberation for Subjective Visual Classification

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Agile_Deliberation_Concept_Deliberation_for_Subjective_Visual_Classification_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_Agile_Deliberation_Concept_Deliberation_for_Subjective_Visual_Classification_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 用户实际偏好会在看例子后变动，固定概念的主动学习会收集互相冲突的监督。
- **核心创新 / 方法** · 先构造概念和子概念，再展示语义边界案例，让用户反思并反馈。
- **Baseline** · 人工请用户自行审议与 Agile Deliberation 的系统辅助对照。
- **Benchmark** · 两种主观视觉概念的用户实验，记录参与者与分类器的 F1、查准查全及主观评级。
- **关键结果 / 消融** · 表1–2提供分类对齐及主观体验对照，验证流程中的概念迭代。
- **适用条件 / 局限** · 依赖用户持续参与，少量概念与给定参与者结果不代表一般偏好。

**可复用机制** · 主观概念标注中先分解待定义概念，再用边界样例迭代修正概念及分类器。

<a id="paper-emma-multimodal-dynamics"></a>

## EMMA: Extracting Multiple physical parameters from Multimodal Data

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Shaikh_EMMA_Extracting_Multiple_physical_parameters_from_Multimodal_Data_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Shaikh_EMMA_Extracting_Multiple_physical_parameters_from_Multimodal_Data_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 单视频下有遮挡和隐藏外力，部分参数不可仅凭视觉轨迹识别。
- **核心创新 / 方法** · 用液态时间常数网络建模共享潜动态，以方程损失约束参数、潜状态和校准量的联合推断。
- **Baseline** · 原文表1–2与基于视频的参数恢复及多系统基线比较。
- **Benchmark** · 摆、滑块、流出等动力学系统，含 Delfys 视频与非运动观测，比较参数估计误差。
- **关键结果 / 消融** · 表2报告在多种动力参数任务表现有竞争力，正文展示部分非运动观测扩展。
- **适用条件 / 局限** · 参数可辨识性和方程先验决定能否恢复；不充分观测下可能有等价解释。

**可复用机制** · 从异构时间序列推断动力参数时，让观测通道共享连续时间隐状态并以已知物理方程约束。

<a id="paper-tracegen-3d-trace-space"></a>

## TraceGen: World Modeling in 3D Trace Space Enables Learning from Cross-Embodiment Videos

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Lee_TraceGen_World_Modeling_in_3D_Trace_Space_Enables_Learning_from_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Lee_TraceGen_World_Modeling_in_3D_Trace_Space_Enables_Learning_from_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 外观、视角和机体差异使跨具身视频难直接用于少样本操作。
- **核心创新 / 方法** · 将视频转换成统一三维场景轨迹，在轨迹空间预测后续运动，并用少量目标机器人视频适配。
- **Baseline** · 对照无跨具身预训练、不同适配数据量及基于视频的世界模型。
- **Benchmark** · 四项操作任务的5或15视频适配、任务成功率与推理开销。
- **关键结果 / 消融** · 作者在5个目标视频的条件下报告四任务80%成功率，较所测视频世界模型快50–600倍。
- **适用条件 / 局限** · 依赖点追踪和三维配准质量，轨迹不会表达纹理、力或所有接触信息。

**可复用机制** · 跨机器人和人类视频预训练时，预测场景三维点轨迹而非像素，以复用运动先验。

<a id="paper-have-bench-speech-text-controlled"></a>

## HAVE-Bench: Hierarchical Audio-Visual Evaluation from Perception to Interaction

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhong_HAVE-Bench_Hierarchical_Audio-Visual_Evaluation_from_Perception_to_Interaction_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhong_HAVE-Bench_Hierarchical_Audio-Visual_Evaluation_from_Perception_to_Interaction_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 音画模型的感知成绩无法说明它能否利用语音指令进行多轮视觉推理。
- **核心创新 / 方法** · 按感知、推理、交互分层，另用同任务语音加图像和文本加图像对比模态差距。
- **Baseline** · 比较 Gemini2.5-Flash、Qwen2.5-Omni、MiniCPM-o 等及 ASR 加模型。
- **Benchmark** · HAVE-Bench 2,451 条；测识别、图中文字、数学、多学科题和交互。
- **关键结果 / 消融** · 表 2 Qwen2.5-Omni 总分语音 69.1、文本 70.9，但数学语音 47.0、文本 46.0；应按子任务判断。
- **适用条件 / 局限** · 语音识别误差、说话节奏和输出协议可影响差值，不宜只凭总体分认定推理短板。

**可复用机制** · 选择语音控制视觉代理时，应将同题的语音输入、转录文本与语言推理分开对照。见表 2。

<a id="paper-diffusion-probe-early-quality"></a>

## Diffusion Probe: Generated Image Result Prediction Using CNN Probes

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_Diffusion_Probe_Generated_Image_Result_Prediction_Using_CNN_Probes_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_Diffusion_Probe_Generated_Image_Result_Prediction_Using_CNN_Probes_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 为选种子或提示而完整生成大量候选耗费算力，早期图像像素本身也难直接评价。
- **核心创新 / 方法** · 训练轻量 CNN 从早期交叉注意力统计预测终局质量，作为提前排序依据。
- **Baseline** · 比较随机选种子、原提示和 LLM 提示改写，另比较不同早期步数。
- **Benchmark** · SDXL 和 FLUX 的提示优化及种子选择，报告 CLIP、ImageReward、审美分及预测表现。
- **关键结果 / 消融** · 表 2 SDXL 种子选择的 ImageReward 从随机 0.71 到 0.82，FLUX 从 1.02 到 1.06。
- **适用条件 / 局限** · 依赖内部注意力可读及质量标签；同一探针跨骨干和提示分布需重验，代理得分不等同人评。

**可复用机制** · 多候选生成可预测早期去噪的终局质量，再决定是否继续完成整段去噪。见表 1–2。

<a id="paper-free-sinewich-task-modulation"></a>

## Frequency Switching Mechanism for Parameter-Efficient Multi-Task Learning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_Frequency_Switching_Mechanism_for_Parameter-Efficient_Multi-Task_Learning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_Frequency_Switching_Mechanism_for_Parameter-Efficient_Multi-Task_Learning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 每任务独立适配的存储随任务数增长，而完全共享权重可能导致表征冲突。
- **核心创新 / 方法** · 共享低秩与卷积权重，用可控频率正弦调制构造任务权重，Clock Net 约束调制。
- **Baseline** · 比较关掉正弦、局部卷积和低通，并与单任务及参数高效多任务方法对照。
- **Benchmark** · PASCAL-Context 和 NYUDv2 的语义、显著性、人体部件及法线等稠密预测任务。
- **关键结果 / 消融** · 表 3 同为 6.53M 参数，完整语义 mIoU 71.25，去正弦为 69.68；法线误差 16.14 对 16.37。
- **适用条件 / 局限** · 依赖任务标识可获得和适配权重可共享，频率分离并非保证任意任务无冲突。

**可复用机制** · 多任务低秩更新可测试以任务频率生成不同权重，比较等参数下任务干扰与低秩容量。见表 3。

<a id="paper-fluidgaussian-functional-reconstruction"></a>

## FluidGaussian: Propagating Simulation-Based Uncertainty Toward Functionally-Intelligent 3D Reconstruction

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_FluidGaussian_Propagating_Simulation-Based_Uncertainty_Toward_Functionally-Intelligent_3D_Reconstruction_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_FluidGaussian_Propagating_Simulation-Based_Uncertainty_Toward_Functionally-Intelligent_3D_Reconstruction_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 仅看渲染精度难发现对交互模拟重要的局部几何错误。
- **核心创新 / 方法** · 用仿真反馈定位对功能敏感的区域，辅助选择后续视图和评价重建。
- **Baseline** · 对比 ActiveNeRF、FisherRF 各自添加功能模拟反馈前后。
- **Benchmark** · Blender、MipNeRF360 等重建，比较视觉指标与功能几何偏差。
- **关键结果 / 消融** · 表 3 Blender 的 ActiveNeRF 偏差从 0.0262 到 0.0145，FisherRF 从 0.0144 到 0.0124。
- **适用条件 / 局限** · 依赖可信的模拟边界和材料假设，从模拟一致性不能推出真实交互质量。

**可复用机制** · 三维数字孪生面向后续物理模拟时，应将功能区模拟一致性与外观误差分开评估。见表 3–4。

<a id="paper-daaam-queryable-spatiotemporal-memory"></a>

## Describe Anything Anywhere At Any Moment

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Gorlo_Describe_Anything_Anywhere_At_Any_Moment_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Gorlo_Describe_Anything_Anywhere_At_Any_Moment_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 帧级记忆能回答见过什么，却可能无法定位对象及回忆它何时出现。
- **核心创新 / 方法** · 批处理局部描述并写入分层时空场景图，将语义检索结果与空间位置、时间关联。
- **Baseline** · 比较 ReMEmbR、Concept Graphs 和直接多帧 VLM。
- **Benchmark** · NaVQA、OC-NaVQA及顺序任务定位，报告描述准确率、位置和时间误差。
- **关键结果 / 消融** · 表 1 NaVQA 中 DAAAM 总准确率 0.672，NVILA-Lite-8B+GPT-5-mini 的 ReMEmbR 为 0.607；总时间误差 1.591 对 2.840 分钟。
- **适用条件 / 局限** · 要求定位与对象关联足够可靠，重识别错误会传播到历史图；跨环境规模和频繁场景变化应另测。

**可复用机制** · 长期场景记忆应保存对象描述及可查询的位置和观测时刻，并用时间误差核验索引。见表 1–4。

<a id="paper-terraseg-offline-pseudolabel-distillation"></a>

## TerraSeg: Self-Supervised Ground Segmentation for Any LiDAR

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Lentsch_TerraSeg_Self-Supervised_Ground_Segmentation_for_Any_LiDAR_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Lentsch_TerraSeg_Self-Supervised_Ground_Segmentation_for_Any_LiDAR_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 手写地面分割依赖雷达配置，逐点人工标签昂贵，慢优化不适合在线。
- **核心创新 / 方法** · 统一多个公开 LiDAR 流，在每一扫描上优化生成地面伪标签，训练通用学生。
- **Baseline** · 比较伪标注器、RANSAC、PatchWork++、TRAVEL 及有监督分割。
- **Benchmark** · nuScenes、SemanticKITTI 验证地面和非地面 IoU、召回与吞吐。
- **关键结果 / 消融** · 表 3 nuScenes 中伪标注器 90.63 mIoU、0.5 Hz，TerraSeg-B 92.47、28.0 Hz，有监督 95.31、28.0 Hz。
- **适用条件 / 局限** · 伪标签的几何偏差可能随设备、坡度及稀疏性传递，应测传感器外推和误判障碍。

**可复用机制** · 逐扫描核验代价高时，可用慢几何估计离线生成跨设备伪标签，再训练实时学生。见表 3–4。

<a id="paper-meta-tool-trajectory-abstraction"></a>

## META: Meta Evolution of Tool Trajectory Adaptation for Long-Video Understanding

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_META_Meta_Evolution_of_Tool_Trajectory_Adaptation_for_Long-Video_Understanding_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_META_Meta_Evolution_of_Tool_Trajectory_Adaptation_for_Long-Video_Understanding_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 长视频工具链每次重建，重复消耗推理且会重犯相同失败。
- **核心创新 / 方法** · 将成功轨迹归纳成可重用多步宏工具，并把失败轨迹记成使用约束，通过两阶段循环选择和精简。
- **Baseline** · 比较原代理、工具但无演化、只微工具演化和只宏工具演化。
- **Benchmark** · MLVU、Video-MME 等长视频理解，报告准确率和演化迭代消融。
- **关键结果 / 消融** · 表 2 不启用两类演化的工具版为 80.8/73.5，只宏演化 83.0/76.6，两者均启用 83.6/77.7。
- **适用条件 / 局限** · 轨迹必须可验证、工具组合要在新任务重新核验；积累的失败规律可能随模型和工具接口改变。

**可复用机制** · 工具代理可以复用既往操作序列并记录失败原因，分别消融宏工具和微工具改良。见表 2–3。

<a id="paper-wanderland-geometry-audit"></a>

## Wanderland: Geometrically Grounded Simulation for Open-World Embodied AI

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_Wanderland_Geometrically_Grounded_Simulation_for_Open-World_Embodied_AI_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_Wanderland_Geometrically_Grounded_Simulation_for_Open-World_Embodied_AI_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 仅按新视图观感选重建方案可能掩盖导航所依赖的几何误差。
- **核心创新 / 方法** · 将多传感捕捉和几何约束重建用于闭环仿真，比较影像方案与传感融合。
- **Baseline** · 与纯视觉重建、LIV-SLAM 和替代渲染条件比较。
- **Benchmark** · 正文表2–5评相同图像数量的重建、视图合成和导航。
- **关键结果 / 消融** · 表2报告视觉重建仍不及 LIV-SLAM，表3–4观察几何质量对合成及闭环训练的影响。
- **适用条件 / 局限** · 依赖采集传感及几何参考，仿真行为不能代替实机闭环验证。

**可复用机制** · 实景仿真应将几何重建质量对视图合成和闭环表现的影响分层验证。

<a id="paper-attribute-lora-subspaces"></a>

## Mining Attribute Subspaces for Efficient Fine-tuning of 3D Foundation Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Jiang_Mining_Attribute_Subspaces_for_Efficient_Fine-tuning_of_3D_Foundation_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Jiang_Mining_Attribute_Subspaces_for_Efficient_Fine-tuning_of_3D_Foundation_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 有限标注下任意低秩方向可能将几何、光照和纹理干扰混在一起。
- **核心创新 / 方法** · 针对每种受控变化拟合 LoRA 并抽取子空间，验证近似解耦后联合适配。
- **Baseline** · 正文表1–5和普通 LoRA、不同子空间构造对照。
- **Benchmark** · 涵盖合成和实拍人脸、着衣人体和透明物体重建。
- **关键结果 / 消融** · 正文验证多个属性子空间近似分离，并比较同任务预测精度。
- **适用条件 / 局限** · 属性变化难在合成中隔离时，方向可能不够纯或不足以覆盖真实数据。

**可复用机制** · 低秩适配可先用单因素可控数据找属性方向，再组合为受约束微调子空间。

<a id="paper-weakmed"></a>

## Rethinking Box Supervision: Bias-Free Weakly Supervised Medical Segmentation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wei_Rethinking_Box_Supervision_Bias-Free_Weakly_Supervised_Medical_Segmentation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wei_Rethinking_Box_Supervision_Bias-Free_Weakly_Supervised_Medical_Segmentation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 医学分割框标注便宜却带来矩形偏置。
- **核心创新 / 方法** · 把预测掩码转成框域监督，并约束不同尺度的预测。
- **Baseline** · 以 BoxSup 和其他弱监督方法为对照，表2移除两种新增监督。
- **Benchmark** · 正文表1–3覆盖多种医学图像，报告 Dice 和 IoU。
- **关键结果 / 消融** · 表2单独比较两类训练改动，表3展示多数据集表现；新增模块无需在推理使用。
- **适用条件 / 局限** · 框和对象不紧贴时会削弱约束，极小或形状不规则区域需独立验证。

**可复用机制** · 用预测掩码导出可与框比较的量，再用跨尺度一致性约束掩码，而避免学习矩形形状。

<a id="paper-cva-temporal-grounding"></a>

## CVA: Context-aware Video-text Alignment for Video Temporal Grounding

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Moon_CVA_Context-aware_Video-text_Alignment_for_Video_Temporal_Grounding_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Moon_CVA_Context-aware_Video-text_Alignment_for_Video_Temporal_Grounding_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 任意替换背景会意外加入正确片段，从而构造假负例。
- **核心创新 / 方法** · 以视频文本相似度过滤替换池，以对比损失让边界特征对上下文变化更稳定。
- **Baseline** · 对照既有时间定位方法和去掉查询过滤及边界损失的设置。
- **Benchmark** · QVHighlights、TACoS、Charades-STA；正文表1–5报告检索定位指标。
- **关键结果 / 消融** · 表4–5分别检验查询无关的上下文替换和边界损失。
- **适用条件 / 局限** · 依赖相关性检索器不会把近义视频段当负例，语义边界模糊时需抽查。

**可复用机制** · 训练时替换视频背景先检验与查询无关，并在时间边界做反事实一致性。

<a id="paper-pas-temporal-encoding"></a>

## PAS: A Training-Free Stabilizer for Temporal Encoding in Video LLMs

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Sun_PAS_A_Training-Free_Stabilizer_for_Temporal_Encoding_in_Video_LLMs_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Sun_PAS_A_Training-Free_Stabilizer_for_Temporal_Encoding_in_Video_LLMs_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 帧间很小的时间变化可能经多模态 RoPE 改写本应相近的注意关系。
- **核心创新 / 方法** · 在不同头施加小的相位偏移再聚合，保留各头频谱幅值。
- **Baseline** · 在相同词元数下比较原模型、多种免训练校准及叠加配置。
- **Benchmark** · 正文表1–2按视频任务和时间采样条件对比。
- **关键结果 / 消融** · 正文结合核的频谱分析和配对设定验平滑机制减轻相位敏感性。
- **适用条件 / 局限** · 依赖可获模型头及位置编码，保持频谱幅值也需检查是否损失短时精确定位。

**可复用机制** · 视频位置编码可按帧时刻扰动诊断相位不稳，并利用跨注意头聚合平滑。

<a id="paper-asymmetric-mistake-severity"></a>

## Every Error has Its Magnitude: Asymmetric Mistake Severity Training for Multiclass Multiple Instance Learning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Hong_Every_Error_has_Its_Magnitude_Asymmetric_Mistake_Severity_Training_for_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Hong_Every_Error_has_Its_Magnitude_Asymmetric_Mistake_Severity_Training_for_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 普通多类训练均等看待不同误诊，且忽略类别间严重程度关系。
- **核心创新 / 方法** · 按诊断层级为错误赋非对称权重，约束层级预测概率一致，并重新混合实例袋。
- **Baseline** · 表1比较既有误差严重度方法，表2–3分别消融损失与实例混合。
- **Benchmark** · BRACS 等公开及内部全切片数据，另测自然图像；按分类及错误严重度指标评价。
- **关键结果 / 消融** · 原文报告高严重度错误减少，BRACS 消融检验各组件。
- **适用条件 / 局限** · 误差代价需要领域共识，降低严重错误可能伴随其他错误变化。

**可复用机制** · 误分类代价不等时，使用有方向的分层损失和配套代价指标。

<a id="paper-tfgc-token-flow-compression"></a>

## Towards Unified Human Perception and Machine Understanding: Token Flow Guided Compression Framework

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_Towards_Unified_Human_Perception_and_Machine_Understanding_Token_Flow_Guided_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_Towards_Unified_Human_Perception_and_Machine_Understanding_Token_Flow_Guided_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 像素保真压缩在极低码率下难保持机器所需语义，且解码再编码增加开销。
- **核心创新 / 方法** · 以一维词元流传播补齐缺失内容，以语义引导对齐压缩表示并支持变码率。
- **Baseline** · 比较重建后送入视觉模型的压缩方案及现有码率设置；表3测编码解码成本。
- **Benchmark** · 机器理解与人类感知两组基准，记录平均 bpp、任务表现、视觉质量和256分辨率延时。
- **关键结果 / 消融** · 表1–2报告多个低码率区间同时支持任务识别及视觉恢复。
- **适用条件 / 局限** · 直接读词元需兼容的模型接口，超低码率可能不可逆丢失文字和小物体。

**可复用机制** · 要求人机共用压缩流时，允许 VLM 直接读可变数量的潜词元，由上下文预测未传词元。

<a id="paper-tmfs-shared-degradation"></a>

## Physically-Grounded Turbulence Mitigation with Frame-Shared Degradation Parameters

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xie_Physically-Grounded_Turbulence_Mitigation_with_Frame-Shared_Degradation_Parameters_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xie_Physically-Grounded_Turbulence_Mitigation_with_Frame-Shared_Degradation_Parameters_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 独立估计每一帧的形变和模糊欠约束，合成训练退化又可能偏离真实成像。
- **核心创新 / 方法** · 以倾斜后模糊的观测模型，将退化解为共用相关函数和逐帧噪声图。
- **Baseline** · 表1比较有监督及无监督恢复，表2对比传统去模糊设置。
- **Benchmark** · 合成及 Heat 等实拍湍流数据，对比恢复质量。
- **关键结果 / 消融** · 原文报告共享建模在多套条件下改善重建，包含真实热室退化。
- **适用条件 / 局限** · 要求多帧共享的退化结构能合理近似，场景切换和退化机制变化可能失效。

**可复用机制** · 同场景多帧恢复中，把共享退化结构与逐帧随机项分开估计。

<a id="paper-point4cast"></a>

## Point4Cast: Streaming Dynamic Scene Reconstruction and Forecasting

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_Point4Cast_Streaming_Dynamic_Scene_Reconstruction_and_Forecasting_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_Point4Cast_Streaming_Dynamic_Scene_Reconstruction_and_Forecasting_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 常规在线重建只能恢复已观察时刻，不能从同一状态预测动态。
- **核心创新 / 方法** · 新图像只更新持久时空潜表示；按请求时间读出点图与相机参数，兼顾过去与未来。
- **Baseline** · 表1–3比较已有动态重建和预测方法。
- **Benchmark** · PointOdyssey 重建及预测，TAPVid-3D 重建，测三维时序点轨迹与定位表现。
- **关键结果 / 消融** · 原文分别比较已观察重建和未来预测，支持同一表示用于两者。
- **适用条件 / 局限** · 不可见变化及长期预测歧义较大，状态误差可能累积。

**可复用机制** · 流式世界模型用持续更新的潜状态，把观测更新与任意时间几何读出分开。

<a id="paper-short-gaussian-lists"></a>

## Speeding Up the Learning of 3D Gaussians with Much Shorter Gaussian Lists

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_Speeding_Up_the_Learning_of_3D_Gaussians_with_Much_Shorter_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_Speeding_Up_the_Learning_of_3D_Gaussians_with_Much_Shorter_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 相同高斯总数仍可能有大量重叠，像素级混合的开销由列表长度决定。
- **核心创新 / 方法** · 周期重置高斯尺度并以混合权熵惩罚大量平弱贡献，结合分辨率调度缩短列表。
- **Baseline** · Taming-3DGS、Mini-Splatting2、FastGS 等设置，按总高斯数或训练步数分别对照。
- **Benchmark** · 三个新视角数据集，含 Mip-NeRF 360，在等目标数量或对应配置下比较速度与画质。
- **关键结果 / 消融** · 表1–3比较不同骨干及预算，表1按相同目标高斯数控制主要混杂因素。
- **适用条件 / 局限** · 熵与尺度过强可能抑制半透明和细结构，对不同渲染实现的加速需重测。

**可复用机制** · 优化高斯泼溅速度时，直接减少每条射线的候选长度而不只约束总体高斯数。

<a id="paper-internal-guidance-dit"></a>

## Guiding a Diffusion Transformer with the Internal Dynamics of Itself

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhou_Guiding_a_Diffusion_Transformer_with_the_Internal_Dynamics_of_Itself_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhou_Guiding_a_Diffusion_Transformer_with_the_Internal_Dynamics_of_Itself_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 传统 CFG 可能过度约束，另训练退化模型或额外采样也会加开销。
- **核心创新 / 方法** · 训练时对中层加去噪辅助监督，推理时外推中层和深层输出。
- **Baseline** · 同 SiT 骨干的无引导、传统 CFG 或不同中层位置，表1–2比较配置。
- **Benchmark** · ImageNet 256 类别条件生成，报告 FID 与训练阶段收敛。
- **关键结果 / 消融** · SiT-XL/2+IG 在80和800训练轮的 FID 分别为5.31和1.75。
- **适用条件 / 局限** · 须训练具有可用中层读出的模型，过浅太弱、过深可能缺乏互补，最佳层随架构变化。

**可复用机制** · 扩散 Transformer 采样时可使用同一次前向的浅层预测作引导参照。

<a id="paper-weak-to-strong-video-quality"></a>

## Generalizable Video Quality Assessment via Weak-to-Strong Learning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Cao_Generalizable_Video_Quality_Assessment_via_Weak-to-Strong_Learning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Cao_Generalizable_Video_Quality_Assessment_via_Weak-to-Strong_Learning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 人工评分难收且跨视频域泛化弱，不同教师的评分量表又不一致。
- **核心创新 / 方法** · 使用排序目标混合现有质量模型和模拟退化教师，迭代将学生回用为教师。
- **Baseline** · 表2以最佳单教师监督作为对照，并和其他视频质量方法比较。
- **Benchmark** · 视频画质域内及域外基准，测与主观质量的一致性和训练成本。
- **关键结果 / 消融** · 原文发现强学生在部分域外集超过弱教师，混合及迭代方案扩展了这一效果。
- **适用条件 / 局限** · 相关性不说明所有失真类别都能泛化，迭代也可能强化教师偏差。

**可复用机制** · 没有统一标注时，先把不同弱教师信号转为相对排序，再检验强学生的域外表现和迭代收益。

<a id="paper-dig-differential-grounding"></a>

## DiG: Differential Grounding for Enhancing Fine-Grained Perception in Multimodal Large Language Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Tao_DiG_Differential_Grounding_for_Enhancing_Fine-Grained_Perception_in_Multimodal_Large_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Tao_DiG_Differential_Grounding_for_Enhancing_Fine-Grained_Perception_in_Multimodal_Large_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 单图问答难判断模型能否区分细微形变或位置差异，也缺少局部可核验监督。
- **核心创新 / 方法** · 用三维渲染控制成对图像差异，先学单差异再多差异，并联合奖励位置 IoU 与发现差异的 F1。
- **Baseline** · 比较基座、只训单差异及只用 IoU 或 F1 的奖励。
- **Benchmark** · RefCOCO、RefCOCO+、RefCOCOg 及 HalBench、MMBench、AI2D 等。
- **关键结果 / 消融** · 表 4 RefCOCO testB@50 中 IoU 奖励为 76.7，F1 奖励为 82.4，两项为 83.5。
- **适用条件 / 局限** · 合成样本的变化要能代表目标数据；真实图像光照或视角变化仍可能被误判成目标差异。

**可复用机制** · 细粒度视觉训练可用可控变更的成对图像，循序训练找出和定位数量未知的全部差异。见图 3、表 4。

<a id="paper-group-revision-relative-reward"></a>

## From Failure to Feedback: Group Revision Unlocks Hard Cases in Object-Level Grounding

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_From_Failure_to_Feedback_Group_Revision_Unlocks_Hard_Cases_in_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_From_Failure_to_Feedback_Group_Revision_Unlocks_Hard_Cases_in_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 组内答案都失败会让基于阈值的终局奖难以区分有用努力。
- **核心创新 / 方法** · 围绕一个初答生成多条修订，以相对于初答的定位改善同时塑造奖励和优势。
- **Baseline** · 比较原组相对训练、只生成修订和追加相对改进奖励。
- **Benchmark** · ReasonSeg、RefCOCO 系列和 PixMoCount，衡量分割、边框定位与计数。
- **关键结果 / 消融** · 表 4 单对象 ReasonSeg 验证从基线 62.54 到仅修订 64.97，到完整版本 66.99。
- **适用条件 / 局限** · 相对增量需要可靠的连续误差，同时应跟踪最终绝对失败率，避免单纯奖励从很差状态略有改善。

**可复用机制** · 一组定位候选都达不到正确阈值时，可以按相对原始尝试的改进给有效信号，见表 4。

<a id="paper-visplay-questioner-reasoner-self-training"></a>

## VisPlay: Self-Evolving Vision-Language Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/He_VisPlay_Self-Evolving_Vision-Language_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/He_VisPlay_Self-Evolving_Vision-Language_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 自生成简单题难继续提升模型，提高问题难度又可能让伪答案质量下降。
- **核心创新 / 方法** · 从同一视觉语言模型训练问题生成器与回答器，用多样性和难度控制生成内容，并按迭代刷新。
- **Baseline** · 比较模型基座、不同自训练迭代和人工标注 GRPO。
- **Benchmark** · 八项视觉推理与幻觉测试，另用外部模型估计自生成标签准确率。
- **关键结果 / 消融** · 表 2 估计伪标签准确率随数据迭代从 72.0 降至 61.0；表 3 的 3B 版本综合均值为 47.3，人工 GRPO 为 47.1，但单项差异大。
- **适用条件 / 局限** · 问题和答案共享模型偏差；需独立人工审计标签及视觉依据，比较计算预算和样本重用。

**可复用机制** · 使用无标注图像自训练时，可同时测问题难度进阶与伪答案准确度下降。见表 2–3。

<a id="paper-ccl-background-invariance"></a>

## Consistency Beyond Contrast: Enhancing Open-Vocabulary Object Detection Robustness via Contextual Consistency Learning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Consistency_Beyond_Contrast_Enhancing_Open-Vocabulary_Object_Detection_Robustness_via_Contextual_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Consistency_Beyond_Contrast_Enhancing_Open-Vocabulary_Object_Detection_Robustness_via_Contextual_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 对象相同但背景变换时，图文对比对齐未必让检测表征稳定。
- **核心创新 / 方法** · 生成同一对象在多种上下文的成对图像，并令两视图的对象区域特征保持一致。
- **Baseline** · 比较 GLIP-T、FIBER-B，只用生成数据和再加一致性损失。
- **Benchmark** · OmniLabel、D3 等描述驱动检测，测分项与总体 AP。
- **关键结果 / 消融** · 表 3 GLIP-T 在 OmniLabel 的 AP 19.3，增加数据 24.8，再加一致性损失 32.2；D3 FULL 对应 19.1、23.2、30.0。
- **适用条件 / 局限** · 背景应改变干扰而保持对象真值；与语义相关的场景条件不能机械去除，且需核查生成伪影。

**可复用机制** · 开放词汇检测若依赖背景，可生成保对象改背景的成对样本，比较只做数据增强和追加对象一致性损失。见表 3。

<a id="paper-neurok-latent-object-kinematics"></a>

## NeuROK: Generative 4D Neural Object Kinematics

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Geng_NeuROK_Generative_4D_Neural_Object_Kinematics_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Geng_NeuROK_Generative_4D_Neural_Object_Kinematics_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 静态三维生成缺少形变空间，按类别预设运动模型又难扩展到新对象。
- **核心创新 / 方法** · 在四维数据上训练共享对象状态潜空间，将每一状态通过形变解码为三维几何。
- **Baseline** · 对照 CANOR、KeyPointDeformer、FreeArt3D 等，消融模型降维和姿态参数化。
- **Benchmark** · 逆运动学用 Chamfer 与 IoU，运动生成另测人评、VBench、WorldScore。
- **关键结果 / 消融** · 表 1 完整 IoU 为 0.764，KeyPointDeformer 为 0.570，移除模型降维为 0.711。
- **适用条件 / 局限** · 形变先验接近训练分布时较可靠，接触力、刚体可行性及从视频向实际机器人迁移仍需单独确认。

**可复用机制** · 对象可动几何可先学形状到运动状态可解码的低维先验，再以同先验比较逆运动恢复。见表 1。

<a id="paper-red-rationale-conditional-decoding"></a>

## Rationale-Enhanced Decoding for Multi-modal Chain-of-Thought

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yamaguchi_Rationale-Enhanced_Decoding_for_Multi-modal_Chain-of-Thought_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yamaguchi_Rationale-Enhanced_Decoding_for_Multi-modal_Chain-of-Thought_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 模型可写出思维链，但在最终解码时忽略其中内容，常规准确率看不出。
- **核心创新 / 方法** · 分别从图像条件和依据条件计算词元分布并联合解码，加强答案对显式依据的依赖。
- **Baseline** · 对照标准 CoT、CCoT，以及保持图像时将原解释置换为无关文本。
- **Benchmark** · GQA 的解释干预与 SEED-I 等视觉推理，报告准确率和响应对条件变化。
- **关键结果 / 消融** · 表 1 中图像仍在时，用无关解释替换真实解释常不会造成预期幅度的下降；移去图像后无关解释造成较明显下降。
- **适用条件 / 局限** · 解释有误时增强其影响也可能带来误导，证据来源和双条件计算开销应另验。

**可复用机制** · 多模态思维链应通过无关依据替换检查模型是否实际用到解释，再对照显式联合两种条件分布。见表 1、4。

<a id="paper-spherical-voronoi"></a>

## Spherical Voronoi: Directional Appearance as a Differentiable Partition of the Sphere

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Di_Sario_Spherical_Voronoi_Directional_Appearance_as_a_Differentiable_Partition_of_the_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Di_Sario_Spherical_Voronoi_Directional_Appearance_as_a_Differentiable_Partition_of_the_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 球谐在高频边界易振铃，镜面光随视角急变。
- **核心创新 / 方法** · 以平滑边界的可学球面 Voronoi 区域刻画方向外观，并用反射方向查询。
- **Baseline** · 比较球谐、球面高斯等颜色参数化。
- **Benchmark** · 正文表1–4测辐射、反射、光探针，以及训练与渲染效率。
- **关键结果 / 消融** · 正文分别验证一般视角外观和反射，避免用漫反射平均指标掩盖镜面表现。
- **适用条件 / 局限** · 可学区域依赖观测方向覆盖，高频结果也受几何和法向质量影响。

**可复用机制** · 用可微球面分区表达视角相关外观，镜面成分以反射方向建模。

<a id="paper-countscope"></a>

## Understanding Counting Mechanisms in Large Language and Vision-Language Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Hasani_Understanding_Counting_Mechanisms_in_Large_Language_and_Vision-Language_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Hasani_Understanding_Counting_Mechanisms_in_Large_Language_and_Vision-Language_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 最终答对数量不足以说明模型沿序列如何表示和累积数量。
- **核心创新 / 方法** · 以 CountScope 读中间表示，比较层级与空间位置，并干预计数相关状态。
- **Baseline** · 用受控文本与图像、替换背景和前景及不同读出假说互相对照。
- **Benchmark** · 正文表1–4用预测真值的概率及因果干预分数验证不同计数假说。
- **关键结果 / 消融** · 正文观察到后层支持更大计数，序列末位或图像区域可携带计数，但视觉位置随构图而变。
- **适用条件 / 局限** · 受控重复项与开放场景不同，探针能读出仍需要干预验证实际作用。

**可复用机制** · 计数可先用受控重复项探测中间计数信号，再做因果干预区分局部计数和最终聚合。

<a id="paper-dc-pgn"></a>

## Test-time Ego-Exo-centric Adaptation for Action Anticipation via Multi-Label Prototype Growing and Dual-Clue Consistency

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Shi_Test-time_Ego-Exo-centric_Adaptation_for_Action_Anticipation_via_Multi-Label_Prototype_Growing_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Shi_Test-time_Ego-Exo-centric_Adaptation_for_Action_Anticipation_via_Multi-Label_Prototype_Growing_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 在线适配遇到复合动作时，硬单标签更新容易放大视角偏差。
- **核心创新 / 方法** · 多标签原型逐步增长，按置信重加权，并以跨模态一致性约束更新。
- **Baseline** · 比较既有测试时适配，表2–3分别消融线索、原型及候选数。
- **Benchmark** · EgoMe-anti 和 EgoExoLearn，对照第三至第一视角及反方向的动作预测。
- **关键结果 / 消融** · 表1–3分别检验跨视角效果和更新选择数对结果的影响。
- **适用条件 / 局限** · 误标可在在线记忆中积累，输入视角与动作组合变化时需控制更新。

**可复用机制** · 跨第一与第三视角时，原型更新应允许多个候选动作，并用第二模态复核伪标签。

<a id="paper-dreamstereo"></a>

## DreamStereo: Towards Real-Time Stereo Inpainting for HD Videos

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_DreamStereo_Towards_Real-Time_Stereo_Inpainting_for_HD_Videos_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_DreamStereo_Towards_Real-Time_Stereo_Inpainting_for_HD_Videos_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 整帧处理浪费算力，立体视差变换同时须保留遮挡边界。
- **核心创新 / 方法** · 用坐标映射梯度辅助视差变换和训练配对，并按补全需求调整计算。
- **Baseline** · 与立体补全和二维转三维方法比较，表3–4分别比较数据与推理设置。
- **Benchmark** · HD-100、Dynamic Replica 和 SVD AVP，测图像质量及每帧耗时。
- **关键结果 / 消融** · 表1–4区分训练配对和推理配置带来的变化，并报告固定函数评估次数的消融。
- **适用条件 / 局限** · 遮挡范围扩大或视差估计错误时，稀疏计算及边缘效果需重新验证。

**可复用机制** · 立体视频补全可让昂贵计算优先覆盖小面积遮挡区域，再独立校验边缘一致性。

<a id="paper-freeloc"></a>

## Free-Lunch Long Video Generation via Layer-Adaptive O.O.D Correction

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Tian_Free-Lunch_Long_Video_Generation_via_Layer-Adaptive_O.O.D_Correction_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Tian_Free-Lunch_Long_Video_Generation_via_Layer-Adaptive_O.O.D_Correction_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 短片预训练模型在长序列推理时会遇到陌生相对位置及注意力容量。
- **核心创新 / 方法** · 分别重编码相对位置和分层稀疏注意，并探测哪一层需要哪种干预。
- **Baseline** · 对照原长序列推理、统一改层及去掉每一项的版本。
- **Benchmark** · 正文表1–4对照2倍和4倍长度的生成质量与模块设置。
- **关键结果 / 消融** · 正文实验显示按层处理可在扩展长度下保留质量，并隔离位置和注意机制。
- **适用条件 / 局限** · 不同主干需重估层敏感性，接近原训练长度时额外修正未必划算。

**可复用机制** · 长视频扩散的外推失败应分别诊断帧相对距离和总上下文长度，按层选修正。

<a id="paper-activation-replay"></a>

## Boosting Reasoning in Large Multimodal Models via Activation Replay

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xing_Boosting_Reasoning_in_Large_Multimodal_Models_via_Activation_Replay_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xing_Boosting_Reasoning_in_Large_Multimodal_Models_via_Activation_Replay_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 整体推理增益难说明强化学习改写了哪些视觉表示。
- **核心创新 / 方法** · 用 logit lens 分析激活置信度，并从基础模型回放选定低熵视觉激活给强化学习版本。
- **Baseline** · 对照不回放、不同熵组干预以及多个既有推理模型。
- **Benchmark** · 正文表1–4涵盖 MathVerse 等视觉推理、图像辅助代理及16帧视频推理。
- **关键结果 / 消融** · 正文报告低熵受强化训练的变化更明显；表2–4检查不同模型上的无训练干预效果。
- **适用条件 / 局限** · 需要兼容的基础检查点和强化学习变体，低熵是可靠性代理而非真实性标签。

**可复用机制** · 诊断 RLVR 是否改写低熵证据表征，再用基础模型同位置激活做无训练替换对照。

<a id="paper-part-grounding-attention-to-point"></a>

## Enhancing Part-Level Point Grounding for Any Open-Source MLLMs

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Jhang_Enhancing_Part-Level_Point_Grounding_for_Any_Open-Source_MLLMs_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Jhang_Enhancing_Part-Level_Point_Grounding_for_Any_Open-Source_MLLMs_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 对象级定位无法满足部件级点选，生成坐标也可能缺少空间监督。
- **核心创新 / 方法** · 在中层合成文本条件查询，再以轻量解码器将注意力转换为点热图。
- **Baseline** · 同冻结主干的原始生成定位方式及现有部件指向方法。
- **Benchmark** · PACO 直接指点和 InstructPart 推理指点，比较点定位准确性。
- **关键结果 / 消融** · 表2报告不同开源骨干上效果改善，包括原先不能直接输出点位的模型。
- **适用条件 / 局限** · 骨干中层必须含可读空间信息，细小及遮挡部件仍受视觉分辨率限制。

**可复用机制** · 冻结多模态主干时，用文本条件中层注意力热图预测部件坐标。

<a id="paper-ifa-net-forgery-localization"></a>

## Detecting AI-Generated Forgeries via Iterative Manifold Deviation Amplification

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Detecting_AI-Generated_Forgeries_via_Iterative_Manifold_Deviation_Amplification_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Detecting_AI-Generated_Forgeries_via_Iterative_Manifold_Deviation_Amplification_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 针对旧伪造类型学判别特征难泛化到新编辑器。
- **核心创新 / 方法** · 冻结自然图像 MAE，融合其重建残差做粗定位，再以粗定位引导残差细化。
- **Baseline** · 表1比较多个篡改定位方法，表2拆分两阶段。
- **Benchmark** · GIT、TT 等篡改定位基准，比较区域 IoU 与 F1。
- **关键结果 / 消融** · 作者报告四组扩散修补基准平均改善 IoU 6.5%、F1 8.1%，表2检验组件。
- **适用条件 / 局限** · 先验域之外的真实图像也可能难重建，部署时应核验误报。

**可复用机制** · 取证检测可从自然图像重建残差出发，用初步区域预测引导第二轮定位。

<a id="paper-onecat-scale-aware-autoregression"></a>

## OneCAT: Decoder-Only Auto-Regressive Model for Unified Understanding and Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_OneCAT_Decoder-Only_Auto-Regressive_Model_for_Unified_Understanding_and_Generation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_OneCAT_Decoder-Only_Auto-Regressive_Model_for_Unified_Understanding_and_Generation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 同时支持理解、生成和编辑的模型常依赖外部编码器并承担高分辨率成本。
- **核心创新 / 方法** · 训练单一自回归主干，按模态选择专家，并用尺度适配器完成多尺度生成。
- **Baseline** · 表2–3比较其他统一多模态模型以及使用外部视觉编码器或提示改写的方案。
- **Benchmark** · 多模态理解以及 DPG-Bench、GenEval 等生成，报告准确性、生成分数、激活参数与解码延迟。
- **关键结果 / 消融** · 原文报告视觉主干集成后仍有竞争力，尺度自回归带来延迟优势。
- **适用条件 / 局限** · 具体收益依赖规模与训练成本，外部预训练接口的便利性有待比较。

**可复用机制** · 统一多模态模型可在解码器内用模态专家和尺度适配，减少外部视觉组件及逐像素解码开销。

<a id="paper-closed-form-vlm-debiasing"></a>

## A Closed-Form Solution for Debiasing Vision-Language Models with Utility Guarantees Across Modalities and Tasks

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Lian_A_Closed-Form_Solution_for_Debiasing_Vision-Language_Models_with_Utility_Guarantees_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Lian_A_Closed-Form_Solution_for_Debiasing_Vision-Language_Models_with_Utility_Guarantees_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 很多去偏方法改善公平指标却不给任务效用损失上界。
- **核心创新 / 方法** · 在共享表征求免训练闭式解，同时处理图像与文本，并在假设下保证公平和效用的帕累托取舍。
- **Baseline** · 表1梳理已有去偏方案，表2–3对比零样本和检索实验。
- **Benchmark** · 零样本分类、图文检索及生成，涵盖性别、年龄、肤色等群体及交叉公平性。
- **关键结果 / 消融** · 作者报告多项公平评估改善且维持任务效用，理论保证适用于文中定义。
- **适用条件 / 局限** · 受敏感属性定义、表征和效用代理限制，不能将上界直接外推到部署影响。

**可复用机制** · 跨模态去偏前确定可接受任务效用下限，再用闭式变换评估公平性取舍。

<a id="paper-evotrack-occlusion-cues"></a>

## Tracking through Severe Occlusion via Event-Derived Transient Cues

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Dong_Tracking_through_Severe_Occlusion_via_Event-Derived_Transient_Cues_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Dong_Tracking_through_Severe_Occlusion_via_Event-Derived_Transient_Cues_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 遮挡会破坏空间匹配，逐帧运动也难表达高速非线性变化。
- **核心创新 / 方法** · 组合事件时序运动和目标外观匹配，并用双向运动一致性约束模型。
- **Baseline** · 表1对照事件追踪方法，表2–3改变关键模块与遮挡掩码。
- **Benchmark** · FE108、VisEvent、COESOT、FEOT，比较跟踪表现及遮挡相关对照。
- **关键结果 / 消融** · 表1–3给出跟踪性能与部件消融，支持事件运动与外观互补。
- **适用条件 / 局限** · 依赖有足量可观测事件，当所有信息源同时失效时仍无法可靠恢复位置。

**可复用机制** · 强遮挡时分开检查事件运动提示与外观匹配，避免遮挡模板污染。

<a id="paper-iamsb-asymmetric-multimodal-localization"></a>

## Inconsistency-aware Multimodal Schrodinger Bridge for Deepfake Localization

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xiong_Inconsistency-aware_Multimodal_Schrodinger_Bridge_for_Deepfake_Localization_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xiong_Inconsistency-aware_Multimodal_Schrodinger_Bridge_for_Deepfake_Localization_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 单路受扰或时序不同步时，对称融合会把局部异常传播到另一模态。
- **核心创新 / 方法** · 粗阶段估计跨模态一致性及候选时段，细阶段用不对称预算融合并定位。
- **Baseline** · 对照音视频伪造定位方法，表3消融粗估和细化结构。
- **Benchmark** · LAV-DF、TVIL、AV-Deepfake1M 的时间区间定位评测。
- **关键结果 / 消融** · 表1–2报告多数据集定位改善，表3检验一致性选择及非对称策略。
- **适用条件 / 局限** · 依赖一致性估计与音视频原有同步，真实不同步也可能引发误报。

**可复用机制** · 多模态防御定位时依据两路证据的一致性决定融合强度和各路计算预算。

<a id="paper-vitprompt-test-time-visual-box-refresh"></a>

## ViTPrompt: Training-Free Prompt Refinement with Visual Tokens for Open-Vocabulary Detection

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Qin_ViTPrompt_Training-Free_Prompt_Refinement_with_Visual_Tokens_for_Open-Vocabulary_Detection_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Qin_ViTPrompt_Training-Free_Prompt_Refinement_with_Visual_Tokens_for_Open-Vocabulary_Detection_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 域变化同时损害分类和边框定位，仅调整类别置信无法纠正位置。
- **核心创新 / 方法** · 从首轮高置信检测的区域取视觉词元，用池化与原文字提示融合，再做一次框与类别解码。
- **Baseline** · 比较原 Grounding DINO、纯文本提示和视觉区域融合。
- **Benchmark** · FoggyCityscapes、PASCAL-C、COCO-C，报告 mAP 并消融提示融合。
- **关键结果 / 消融** · 表 4 Swin-T 上更换提示后 FoggyCityscapes 为 29.10 对 28.89，COCO-C 平均为 26.25 对 25.57。
- **适用条件 / 局限** · 依赖首轮有可信正例，严重域移可能形成错误自反馈；应核算第二轮开销与定位净收益。

**可复用机制** · 开放词汇检测测试时适配应分别检查框定位和类别分数，可用首轮可信候选的视觉特征更新第二轮提示。见表 4。

<a id="paper-foleydirector-temporal-audio-scripts"></a>

## FoleyDirector: Fine-Grained Temporal Steering for Video-to-Audio Generation via Structured Scripts

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_FoleyDirector_Fine-Grained_Temporal_Steering_for_Video-to-Audio_Generation_via_Structured_Scripts_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_FoleyDirector_Fine-Grained_Temporal_Steering_for_Video-to-Audio_Generation_via_Structured_Scripts_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 视觉不可见的声源和多个同时事件难从视频本身恢复，整段提示也不规定精确时段。
- **核心创新 / 方法** · 用带时间段的结构化字幕作为条件，借助时间脚本注意力融合，并分内外画面生成路径。
- **Baseline** · 比较原视频到音频骨干、是否启用双分支及已有配音模型。
- **Benchmark** · DirectorBench 对时间与反事实控制打分，基于音频检测时段和目标时段重叠，另测音质与语义。
- **关键结果 / 消融** · 表 3 重标注子集使用双分支时总分 0.4613，无该分支为 0.4178。
- **适用条件 / 局限** · 依赖脚本准确指定事件和时间；重叠指标随音频定位模型变化，复杂声源混合仍需人工核查。

**可复用机制** · 视频生成配音应将事件发生时段作为显式脚本条件，并在可见与画外事件上分别检查同步。见表 3。

<a id="paper-hcl-ff-local-hierarchical-training"></a>

## HCL-FF: Hierarchical and Contrastive Learning for Forward-Forward Algorithm

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yao_HCL-FF_Hierarchical_and_Contrastive_Learning_for_Forward-Forward_Algorithm_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yao_HCL-FF_Hierarchical_and_Contrastive_Learning_for_Forward-Forward_Algorithm_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 逐层 Forward-Forward 只根据本层好坏更新，可能忽略跨深度语义结构。
- **核心创新 / 方法** · 以粗到细类别训练不同层，并为局部表示加监督对比目标。
- **Baseline** · 比较 FF 基线、只有层级、只有对比、去数据增强，以及标准反传网络。
- **Benchmark** · CIFAR-10/100、Tiny-ImageNet 等图像分类，测正确率及标签层级策略。
- **关键结果 / 消融** · 表 3 CIFAR-100 只增强为 54.65%，增强加对比为 63.77%，完整为 70.76%；Tiny-ImageNet 的标准反传仍更强。
- **适用条件 / 局限** · 需要有意义的类别层级，收益取决于本地学习假设；尚未证明可扩展到同规模大模型或无类别层级任务。

**可复用机制** · 无法端到端反传的逐层学习，可对照浅层粗类、深层细类的协调监督与局部对比学习。见表 2–4。

<a id="paper-humanba-dynamic-landmark-recovery"></a>

## HumanBA: Human-Aware Bundle Adjustment via Global Human-Camera Decoupling

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_HumanBA_Human-Aware_Bundle_Adjustment_via_Global_Human-Camera_Decoupling_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yang_HumanBA_Human-Aware_Bundle_Adjustment_via_Global_Human-Camera_Decoupling_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 单目 SLAM 屏蔽动态人体会失去大量约束，直接使用动态关键点又会偏置相机运动。
- **核心创新 / 方法** · 从人体关节轨迹分离独立人体运动，给剩余相机成分按运动和时间跨度加权后加入束调整。
- **Baseline** · 比较无掩码、只掩码 DROID、加入尺度估计、无权重及完整 HumanBA。
- **Benchmark** · EMDB2、SLOPER4D，报告 ATE、ATE-S 和世界坐标姿态误差。
- **关键结果 / 消融** · 表 1 掩码加尺度估计相较完整 HumanBA，ATE 0.369 对 0.358，W-MPJPE 230.97 对 195.97；无权重引入所有关节时 ATE 退化到 0.508。
- **适用条件 / 局限** · 依赖能分离人体动作及可靠姿态估计，遮挡、跟踪漂移或大幅突变时应降低这些约束权重。

**可复用机制** · 动态主体占据画面时，可测试先分离主体运动后重新利用其残余观测，而不是一律掩蔽前景。见表 1–2。

<a id="paper-co-manipulation-simulation-stability"></a>

## Stability-Driven Motion Generation for Object-Guided Human-Human Co-Manipulation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_Stability-Driven_Motion_Generation_for_Object-Guided_Human-Human_Co-Manipulation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_Stability-Driven_Motion_Generation_for_Object-Guided_Human-Human_Co-Manipulation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 多人看似协调不代表共享物体和手接触稳定，单加接触目标还可能增加穿模。
- **核心创新 / 方法** · 用物体可供性给流匹配提供交互策略，再以仿真反馈修正不稳定状态。
- **Baseline** · 比较流匹配原版及单加接触、先验或仿真的版本。
- **Benchmark** · Core4D-S1/S2 比较接触准确率、穿模、FID 和多样性。
- **关键结果 / 消融** · 表 2 接触准确率由基线 0.35 到仅加接触 0.40，但穿模从 0.15 到 0.20；仅加仿真时穿模 0.02，FID 从 26.3 变差到 28.6。
- **适用条件 / 局限** · 依赖对象几何及仿真接触可信；人体合成指标不等同机器人负载能力，应另做实体和时序扰动验证。

**可复用机制** · 联合操作动作生成应分别试接触先验与仿真修正，并同时检查穿模、接触与自然度。见表 2。

<a id="paper-care-dual-modal-safety-evaluation"></a>

## Diagnosing and Repairing Unsafe Channels in Vision-Language Models via Causal Discovery and Dual-Modal Safety Subspace Projection

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Fu_Diagnosing_and_Repairing_Unsafe_Channels_in_Vision-Language_Models_via_Causal_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Fu_Diagnosing_and_Repairing_Unsafe_Channels_in_Vision-Language_Models_via_Causal_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 只在单一输入模态评估可能漏掉另一模态引发的安全退化。
- **核心创新 / 方法** · 将视觉、文本及联合防护分别消融，用随机选择的干预作为负对照，同时评估一般任务。
- **Baseline** · 比较原模型、视觉或文本一侧防护、双路防护和随机干预。
- **Benchmark** · 两个视觉语言骨干的多项安全测试，另测通用多模态能力。
- **关键结果 / 消融** · 表 2 中 Qwen-VL 的一项综合安全测试里原版风险率为 36.29，双路防护为 8.72；不同单侧设定的收益不一致。
- **适用条件 / 局限** · 依赖独立白盒评估和覆盖真实输入的安全测试，实验数据中的风险下降不能代替线上验证。

**可复用机制** · 多模态安全修复验收应分别测试图像端、文本端和组合干预，再比较任务保留。见表 1–2。

<a id="paper-cd-cca"></a>

## Resolving the Stability-Plasticity Dilemma in Reinforcement Learning via Complementary Continual Critics

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Sun_Resolving_the_Stability-Plasticity_Dilemma_in_Reinforcement_Learning_via_Complementary_Continual_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Sun_Resolving_the_Stability-Plasticity_Dilemma_in_Reinforcement_Learning_via_Complementary_Continual_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 一套视觉价值网络同时应对分布变化和遗忘，容易出现表示漂移。
- **核心创新 / 方法** · 分别用持续反传和弹性权重巩固训练评论器，并用跨注意融合估值。
- **Baseline** · 比较既有视觉强化学习和去掉评论器或跨注意融合的变体。
- **Benchmark** · DMControl 四个难任务与 CARLA，正文表1–2报告不同训练步的环境表现。
- **关键结果 / 消融** · 正文报告双评论器提高视觉强化学习的环境表现，§5.3检查组件。
- **适用条件 / 局限** · 双估值增加训练成本，两支错误相关时融合也可能失效。

**可复用机制** · 把快速适应与长期保留交给不同评论网络，再按观测融合价值。

<a id="paper-hierarchical-robust-vlm"></a>

## Hierarchically Robust Zero-shot Vision-language Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Dong_Hierarchically_Robust_Zero-shot_Vision-language_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Dong_Hierarchically_Robust_Zero-shot_Vision-language_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 只对叶类做稳健对齐可能留下父类分类的风险。
- **核心创新 / 方法** · 结合类别层级约束图文嵌入，并区分对齐深度。
- **Baseline** · 与普通零样本及既有稳健微调基线比较。
- **Benchmark** · ImageNet 微调后在15个数据集报告干净、父子类及零样本鲁棒准确率。
- **关键结果 / 消融** · 正文表1–3分开展示干净和稳健表现，并比较层次设定。
- **适用条件 / 局限** · 依赖可用且正确的类别层级，结果不能外推到未测防御环境。

**可复用机制** · 防御验收应分别测父类和叶类的鲁棒正确率，视觉语义对齐可按层级分别约束。

<a id="paper-pact-continuous-adapters"></a>

## PACT: Phase-Like Transition Constraints in Adapter-Based Continual Learning of Vision-Language Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_PACT_Phase-Like_Transition_Constraints_in_Adapter-Based_Continual_Learning_of_Vision-Language_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_PACT_Phase-Like_Transition_Constraints_in_Adapter-Based_Continual_Learning_of_Vision-Language_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 固定正交虽能减少干扰，也会切断相近任务之间的共享。
- **核心创新 / 方法** · 训练当前适配器后施加显式跨适配器关系约束，区隔应共享与应独立的更新。
- **Baseline** · 与旧任务保持及正交适配等持续学习方法比较。
- **Benchmark** · MTIL、FS-MTIL 与 TinyImageNet，使用迁移、平均和末任务表现。
- **关键结果 / 消融** · 正文表1–3将迁移收益与最终总体指标分开报告。
- **适用条件 / 局限** · 共享先验若与任务关系不符仍会造成负迁移，应在不同任务顺序复验。

**可复用机制** · 持续适配不必把所有任务的方向都做正交，应检验共享方向是否改善正迁移。

<a id="paper-recurrent-video-mae"></a>

## Recurrent Video Masked Autoencoders

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zoran_Recurrent_Video_Masked_Autoencoders_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zoran_Recurrent_Video_Masked_Autoencoders_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 常规全时域注意开销较高，小视频骨干常需蒸馏，空间表示也未必保留。
- **核心创新 / 方法** · 将循环 Transformer 和非对称掩码配对，仅用像素重建学时序状态。
- **Baseline** · 与 VideoMAE、V-JEPA、DINOv2 等比较，正文表3消融循环和训练设计。
- **Benchmark** · 表1–3评动作分类、点和物体跟踪及需要密集几何表示的任务。
- **关键结果 / 消融** · 正文报告小模型无需蒸馏即可取得有竞争力的时序和空间表示。
- **适用条件 / 局限** · 像素目标不保证保留高层语义，应验证更长序列的状态衰减。

**可复用机制** · 把循环状态与非对称视频掩码共同用于预训练，再分测时间任务及静态空间任务。

<a id="paper-lens-component-deletion"></a>

## Lens Component Deletion based on Differentiable Ray Tracing

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Lens_Component_Deletion_based_on_Differentiable_Ray_Tracing_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Lens_Component_Deletion_based_on_Differentiable_Ray_Tracing_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 直接删除镜片可能降低画质，单独优化硬件或后处理也会错估影响。
- **核心创新 / 方法** · 在可微光线模型中评价镜片贡献并删减，再联合优化光学及后处理。
- **Baseline** · 正文表2–3对照不同删减及光学约束。
- **Benchmark** · FiveK 图像与正文光学实验，比较图像质量及不同设计。
- **关键结果 / 消融** · 表1–3将总体性能、镜片删减及约束的收益分别报告。
- **适用条件 / 局限** · 依赖光学仿真精度、加工容差与目标任务，实物需复验。

**可复用机制** · 设计紧凑成像系统时按部件对任务的贡献做消融，再联合优化剩余光学器件与恢复模型。

<a id="paper-beyond-caption-video-moment-retrieval"></a>

## Beyond Caption-Based Queries in Video Moment Retrieval

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Pujol-Perich_Beyond_Caption-Based_Queries_in_Video_Moment_Retrieval_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Pujol-Perich_Beyond_Caption-Based_Queries_in_Video_Moment_Retrieval_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 看过视频再写的描述细于真实检索意图，且默认单片段会掩盖多解问题。
- **核心创新 / 方法** · 分开构造语言欠指定和多片段测试，以活跃解码查询坍缩诊断性能下降，并用结构调整缓解。
- **Baseline** · 在 CG-DETR、LD-DETR 上比较默认和结构改版。
- **Benchmark** · HD-EPIC、YouCook2、ActivityNet-Captions 的搜索式查询和多片段变体。
- **关键结果 / 消融** · 表2–3报告改版减缓跨查询风格及多片段下的性能下降。
- **适用条件 / 局限** · 改写搜索语句不完全等同于真实搜索日志，相关片段覆盖决定评估可靠性。

**可复用机制** · 视频片段检索应以真实搜索语句和多答案标注检验解码器查询是否坍缩。

<a id="paper-budget-adaptive-micro-task-nas"></a>

## Vision-Oriented Lightweight Neural Architecture Search with Budget-Adaptive Evaluation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Fan_Vision-Oriented_Lightweight_Neural_Architecture_Search_with_Budget-Adaptive_Evaluation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Fan_Vision-Oriented_Lightweight_Neural_Architecture_Search_with_Budget-Adaptive_Evaluation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 完整训练排序可靠但昂贵，无训练估计速度快却可能排名失真。
- **核心创新 / 方法** · 以六种微型视觉任务探测不同能力，用预算自适应评估器组合代理排序。
- **Baseline** · 表1与免训练 NAS 对照，表2比较训练搜索，表3同一算力预算替换代理。
- **Benchmark** · 公开 NAS 基准的排序相关性，另测搜索 GPU 时长与所得网络分类、分割指标。
- **关键结果 / 消融** · 正文报告成本近免训练的搜索得到有竞争力结构，表3给出一 GPU 小时的代理对比。
- **适用条件 / 局限** · 微型任务与真实训练目标是否对齐须单独检查，跨模态不能直接复用排序。

**可复用机制** · 算力有限时，用一组短视觉探针给候选模型排序，并按可用预算选择评估配置。

<a id="paper-nvgs-neural-visibility"></a>

## NVGS: Neural Visibility for Occlusion Culling in 3D Gaussian Splatting

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zoomers_NVGS_Neural_Visibility_for_Occlusion_Culling_in_3D_Gaussian_Splatting_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zoomers_NVGS_Neural_Visibility_for_Occlusion_Culling_in_3D_Gaussian_Splatting_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 半透明高斯使普通遮挡剔除困难，大资产场景的实例重复也增加显存。
- **核心创新 / 方法** · 逐资产共享小型 MLP 估计视点可见性，将查询整合进实例光栅化。
- **Baseline** · gsplat、半径裁剪和无 MLP 版本，以及 V3DG。
- **Benchmark** · 三个约6000万高斯的大场景，1080p 对比显存、画质、FPS 与构建时间。
- **关键结果 / 消融** · 表1–3报告重复实例场景的资源与画质权衡，并通过距离实验检查遮挡剔除。
- **适用条件 / 局限** · 需预先拟合资产可见性，少重复资产、形变或不同硬件下收益可能降低。

**可复用机制** · 对于重复资产，用共享视点可见性模型在高斯光栅化前过滤，不把半透明遮挡硬当作二值深度。

<a id="paper-glyphprinter-region-grouped-dpo"></a>

## GlyphPrinter: Region-Grouped Direct Preference Optimization for Glyph-Accurate Visual Text Rendering

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Shuai_GlyphPrinter_Region-Grouped_Direct_Preference_Optimization_for_Glyph-Accurate_Visual_Text_Rendering_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Shuai_GlyphPrinter_Region-Grouped_Direct_Preference_Optimization_for_Glyph-Accurate_Visual_Text_Rendering_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · OCR 与全图偏好无法稳定捕获复杂字形里的局部错误。
- **核心创新 / 方法** · 按字形区域构造偏好并用分组 DPO 训练，直接表达细粒度正确性。
- **Baseline** · 现有视觉文字生成方法，与常规偏好及整图条件比较。
- **Benchmark** · GlyphAcc 多语言和复杂字形，另用人评测美学、图文一致和字形。
- **关键结果 / 消融** · 表1–3对照字形正确性与全局质量的取舍。
- **适用条件 / 局限** · 区域需要较可靠的定位，字符分组较难覆盖重叠文字和复杂版式。

**可复用机制** · 视觉生成的瑕疵局部集中时，将偏好比较分组到区域，不让全图得分稀释字形错误。

<a id="paper-cheem-hierarchical-continual-learning"></a>

## CHEEM: Continual Learning by Reuse, New, Adapt and Skip - A Hierarchical Exploration-Exploitation Approach

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Savadikar_CHEEM_Continual_Learning_by_Reuse_New_Adapt_and_Skip_-_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Savadikar_CHEEM_Continual_Learning_by_Reuse_New_Adapt_and_Skip_-_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 统一增加容量或共享全部层难匹配各任务相似性。
- **核心创新 / 方法** · 用分层探索利用搜索逐层决策，外部任务质心用于无样本条件下识别任务。
- **Baseline** · 与无样本持续学习基线、不同架构扩展及各任务上界比较。
- **Benchmark** · MTIL、VDD，比较 FoM 与多种种子下任务表现。
- **关键结果 / 消融** · 表1–3报告在多任务序列的结果和上界距离。
- **适用条件 / 局限** · 任务质心可能无法分开相似任务，持续新增容量也须控预算。

**可复用机制** · 持续学习为每个任务分别选择层的复用、新建、适配或跳过，显式平衡旧知识与容量。

<a id="paper-ovrcoat"></a>

## Mitigating Objectness Bias and Region-to-Text Misalignment for Open-Vocabulary Panoptic Segmentation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Kormushev_Mitigating_Objectness_Bias_and_Region-to-Text_Misalignment_for_Open-Vocabulary_Panoptic_Segmentation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Kormushev_Mitigating_Objectness_Bias_and_Region-to-Text_Misalignment_for_Open-Vocabulary_Panoptic_Segmentation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 封闭集前景头压制未见对象，CLIP 全局对齐也难直接应用于局部掩码。
- **核心创新 / 方法** · 通过 CLIP 调整前景与背景概率，再修正掩码区域到文本的分类匹配。
- **Baseline** · 表1对照开放词汇全景分割，表2分别消融 COAT 和 OVR。
- **Benchmark** · ADE20K、Mapillary Vistas、Cityscapes，报告 PQ 并区分同词表测试。
- **关键结果 / 消融** · 作者报告 PQ 的提升分别为5.5%、7.1%、3%，表2区分候选筛选和区域识别增益。
- **适用条件 / 局限** · 若模型从未提出该对象的候选掩码，后置校准无法恢复；文本词汇质量仍影响表现。

**可复用机制** · 开放词汇检测分别校准前景提议和区域文本分类，防止新类别在分类前被筛掉。

<a id="paper-relational-visual-similarity-structural-metric"></a>

## Relational Visual Similarity

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Nguyen_Relational_Visual_Similarity_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Nguyen_Relational_Visual_Similarity_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 类比编辑要求保持功能和部件关系，常用语义和外观相似度对这项要求不敏感。
- **核心创新 / 方法** · 从 LAION-2B 筛出约 11.5 万张图及其关系描述，以对应的关系监督学习可独立使用的视觉关系相似度。
- **Baseline** · 编辑系统与 FLUX-Kontext 等比较，评估同时报告 LPIPS、CLIP 和关系得分。
- **Benchmark** · 类比图像编辑，表 2 报告 LPIPS、CLIP 及关系相似度。
- **关键结果 / 消融** · Example Output 的 LPIPS、CLIP、关系得分为 0.60、0.66、0.88，分数分化说明关系排序可以区别于外观排序。
- **适用条件 / 局限** · 关系监督依赖筛选出的关系及其描述，应用于新领域应由人检查关系分数是否对应当地功能要求。

**可复用机制** · 评估类比编辑时，把部件关系是否保持作为独立指标。表 2 显示关系得分与外观得分会出现不同排序。

<a id="paper-evo1-staged-vlm-action-alignment"></a>

## Evo-1: Lightweight Vision-Language-Action Model with Preserved Semantic Alignment

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Lin_Evo-1_Lightweight_Vision-Language-Action_Model_with_Preserved_Semantic_Alignment_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Lin_Evo-1_Lightweight_Vision-Language-Action_Model_with_Preserved_Semantic_Alignment_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 小型视觉语言动作模型在动作模块初次接入时可能丢失预训练语义能力。
- **核心创新 / 方法** · 先冻结视觉语言骨干，只训练动作专家和集成模块，待两者对齐后解冻共同微调。
- **Baseline** · 同架构单阶段联合训练用于隔离训练顺序，效率和真实成功率与 SmolVLA、OpenVLA、π0 比较。
- **Benchmark** · Meta-World、LIBERO、RoboTwin 模拟任务，以及有干扰物、背景与位置变化的真实任务；指标为任务成功率、显存和推理频率。
- **关键结果 / 消融** · 图 8(b) 中两阶段优于单阶段的各难度组。表 2 的整套 Evo-1 达 78.0% 成功率、16.4 Hz 和 2.3 GB，π0 为 73.0%、11.5 Hz 和 17.9 GB。
- **适用条件 / 局限** · 阶段调度依赖可保留的预训练骨干和动作模块，整套系统的速度不能单独归因给训练顺序。

**可复用机制** · 接入新动作头时，可比较先冻结语义骨干对齐动作头、再联合微调，与一开始联合训练的差异。见图 7 和图 8(b)。

<a id="paper-variational-graph-normal-integration"></a>

## Variational Graph-based Normal Integration

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Variational_Graph-based_Normal_Integration_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_Variational_Graph-based_Normal_Integration_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 表面法线积分面对不规则像素域和深度断裂，统一施加连续性会平滑错误边界。
- **核心创新 / 方法** · 在有向加权图上用投影点到平面目标重建深度，交替优化深度及区分连续与断裂的混合后验。
- **Baseline** · 比较 Bilateral Normal Integration、IPF 和 MD。
- **Benchmark** · DiLiGenT-MV 渲染法线图的正面及侧面形状重建，报告平均绝对深度误差。
- **关键结果 / 消融** · 表 2 侧视牛的 GNI 为 0.36，BiNI 为 9.84；侧视佛像 GNI 为 4.04，BiNI 为 3.81，收益随形状变化。
- **适用条件 / 局限** · 需要法线估计和与模型相符的成像条件；侧视个例已有相对退化。

**可复用机制** · 对不规则域上的法线积分，可用区分可连续边与深度断裂边的后验，检验是否改善边界误差。见表 2。

<a id="paper-remoe-region-aware-defensive-vision"></a>

## ReMoE: Region-Mixture Experts for Adversarially-Robust Vision Transformers

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhong_ReMoE_Region-Mixture_Experts_for_Adversarially-Robust_Vision_Transformers_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhong_ReMoE_Region-Mixture_Experts_for_Adversarially-Robust_Vision_Transformers_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 局部图像信息损坏会扩散到视觉 Transformer 的分类结果。
- **核心创新 / 方法** · 用覆盖不同空间范围的专家处理视觉特征，同时保留区域特征和全局语义。
- **Baseline** · DeiT-T 的标准鲁棒训练作为基线，分别移除区域、全局和中心专家作消融。
- **Benchmark** · CIFAR-10、ImageNet 图像分类，作者报告干净与鲁棒准确率。
- **关键结果 / 消融** · 表 4 的 DeiT-T/CIFAR-10 干净准确率从 79.84% 到 83.52%，一项综合鲁棒评测从 44.90% 到 48.93%；三种专家各自去除时该鲁棒分数下降。
- **适用条件 / 局限** · 评估集中于视觉分类和论文设置中的损坏与扰动模型，跨任务迁移未由本消融验证。

**可复用机制** · 设计防御性视觉骨干时，可比较区域与全局特征建模，并在干净准确率之外单列鲁棒准确率。见表 4。

<a id="paper-hypergram-mixed-geometry-alignment"></a>

## Hyperbolic Gramian Volumes for Multimodal Alignment

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Na_Hyperbolic_Gramian_Volumes_for_Multimodal_Alignment_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Na_Hyperbolic_Gramian_Volumes_for_Multimodal_Alignment_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 归一化嵌入的欧氏体积对部分高阶关系压缩过强，纯双曲几何也可能牺牲跨类别区分。
- **核心创新 / 方法** · 学习融合权重，将欧氏与 Lorentz 双曲 Gram 体积同时用于高阶跨模态对齐。
- **Baseline** · VAST、欧氏 GRAM，以及中间的几何曲率、纯双曲和不同模态组合消融。
- **Benchmark** · MSR-VTT 零样本文本检索视频和视频检索文本，比较 R@1。
- **关键结果 / 消融** · 表 4 混合几何双向 R@1 为 0.566、0.536，欧氏版为 0.548、0.521，纯双曲为 0.548、0.525。
- **适用条件 / 局限** · 曲率与模态组合影响收益，二模态提升较小；增加模态时需单独衡量高阶计算开销。

**可复用机制** · 多模态高阶对齐可消融欧氏和双曲 Gram 体积，并比较可学习混合权重对双向检索的影响。见表 4、5。

<a id="paper-prosoftarena-hierarchical-agent-evaluation"></a>

## ProSoftArena: Benchmarking Hierarchical Capabilities of Multi-modal Agents in Professional Software Environments

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Ai_ProSoftArena_Benchmarking_Hierarchical_Capabilities_of_Multi-modal_Agents_in_Professional_Software_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Ai_ProSoftArena_Benchmarking_Hierarchical_Capabilities_of_Multi-modal_Agents_in_Professional_Software_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 低级界面操作的成功无法说明智能体能完成完整的专业工作流。
- **核心创新 / 方法** · 把可执行任务按能力分层并分别计算完成率，定位从单项交互到跨软件过程的失效位置。
- **Baseline** · 比较 GPT 与 Claude 系列智能体及截图、可访问性树、SoM 等输入组合。
- **Benchmark** · ProSoftArena 的 456 个任务覆盖 6 个学科与 13 种专业软件，以分层完成率衡量执行。
- **关键结果 / 消融** · 表 3 最优 L2 软件级成功率为 20.6%，测试智能体在 L3 跨软件任务的成功率为 0%。
- **适用条件 / 局限** · 分层结果取决于任务构成和试验工具配置，不能外推到未测软件或所有开放式工作流。

**可复用机制** · 评估专业软件智能体时，单列软件内与跨软件的执行成功率，避免简单交互覆盖掉复杂工作流的低成功率。见表 3。

<a id="paper-dynamicgtr-query-adaptive-graph-rendering"></a>

## DynamicGTR: Leveraging Graph Topology Representation Preferences to Boost VLM Capabilities on Graph QAs

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wei_DynamicGTR_Leveraging_Graph_Topology_Representation_Preferences_to_Boost_VLM_Capabilities_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wei_DynamicGTR_Leveraging_Graph_Topology_Representation_Preferences_to_Boost_VLM_Capabilities_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 统一使用邻接文本或图像渲染可能使模型难以读取所需图结构，也可能浪费词元。
- **核心创新 / 方法** · DynamicGTR 在模型和问题层面选用文本格式或图像表示，借此调整模型可见的结构信息。
- **Baseline** · 比较普通输入、固定的 GITA 表示及动态选择设置。
- **Benchmark** · 使用六个真实图数据集以及合成图任务，报告准确率与表 4 的词元量。
- **关键结果 / 消融** · 表 4 的 GPT-4o/Cora 普通、GITA、DynamicGTR 三组准确率为 52.2%、56.8%、64.5%，相应词元量为 228.5、184.4、99.2。
- **适用条件 / 局限** · 输入选择依赖目标模型、图规模和查询类型，模型或数据变化时应重复验证准确率及开销。

**可复用机制** · 图推理先按任务与模型选择输入表示，再用准确率和词元量对比固定格式。见表 4。

<a id="paper-openvo"></a>

## OpenVO: Open-World Visual Odometry with Temporal Dynamics Awareness

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Nguyen_OpenVO_Open-World_Visual_Odometry_with_Temporal_Dynamics_Awareness_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Nguyen_OpenVO_Open-World_Visual_Odometry_with_Temporal_Dynamics_Awareness_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 定帧率训练会把位移与采样间隔混淆，依赖相机标定也限制公开视频复用。
- **核心创新 / 方法** · 在单目里程计中编码观测时刻并适配未标定相机。
- **Baseline** · 正文表1对照已有里程计，表2–3拆分时间编码和训练频率。
- **Benchmark** · 三项大规模驾驶基准，按度量平移及旋转误差评估。
- **关键结果 / 消融** · 正文报告跨未见帧率与相机配置的结果，并对训练频率做消融。
- **适用条件 / 局限** · 远离训练速度、减帧模式及光照时需复测。

**可复用机制** · 从不同帧率的视频估计运动时显式输入帧间时间，并按未见帧率和相机配置验收。

<a id="paper-hg-i2p"></a>

## Hg-I2P: Bridging Modalities for Generalizable Image-to-Point-Cloud Registration via Heterogeneous Graphs

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/An_Hg-I2P_Bridging_Modalities_for_Generalizable_Image-to-Point-Cloud_Registration_via_Heterogeneous_Graphs_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/An_Hg-I2P_Bridging_Modalities_for_Generalizable_Image-to-Point-Cloud_Registration_via_Heterogeneous_Graphs_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 二维图像和三维点云的特征域不同，独立提取后容易得到不一致匹配。
- **核心创新 / 方法** · 以分割的二维及三维区域为节点，用跨区域边传递特征并过滤不一致对应。
- **Baseline** · 比较已有二维三维配准及图组件变体。
- **Benchmark** · 正文表1–3包括7-Scenes、ScanNet和跨数据评测。
- **关键结果 / 消融** · 正文分开报告跨场景与跨数据设置中的配准表现。
- **适用条件 / 局限** · 区域分割及图边构造错误可能同时损伤两路特征，域外需独立验。

**可复用机制** · 跨模态配准可用区域级异构图一起校正特征及局部对应，再核查图条件是否保留有效匹配。

<a id="paper-zoo-prune"></a>

## ZOO-Prune: Training-Free Token Pruning via Zeroth-Order Gradient Estimation in Vision-Language Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Kim_ZOO-Prune_Training-Free_Token_Pruning_via_Zeroth-Order_Gradient_Estimation_in_Vision-Language_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Kim_ZOO-Prune_Training-Free_Token_Pruning_via_Zeroth-Order_Gradient_Estimation_in_Vision-Language_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 仅按注意或多样性裁剪可能丢掉影响输出的图像区域。
- **核心创新 / 方法** · 以小扰动测量投影处的敏感度，作为免训练词元裁剪信号。
- **Baseline** · 与注意力、多样性及不裁剪基线比较。
- **Benchmark** · 正文表1–3覆盖 LLaVA-1.5、LLaVA-NeXT 和 Qwen2.5-VL 的多模态测试。
- **关键结果 / 消融** · 正文对照多个骨干和保留预算的准确率表现。
- **适用条件 / 局限** · 零阶探针需控制额外开销，局部敏感也未必对应跨轮视觉证据。

**可复用机制** · 裁剪视觉词元前用轻量投影层的零阶响应估计敏感度，并比较直接利用注意分数。

<a id="paper-ontoaug"></a>

## OntoAug: Rethinking Generative Data Augmentation via Ontology Guidance

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_OntoAug_Rethinking_Generative_Data_Augmentation_via_Ontology_Guidance_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_OntoAug_Rethinking_Generative_Data_Augmentation_via_Ontology_Guidance_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 全图同幅度生成增强可能连类别主体一起改变。
- **核心创新 / 方法** · 按类别本体区分前景及上下文，对两者施加不同条件的增强。
- **Baseline** · 对照常规增强、结合 Mix 增强以及不同骨干。
- **Benchmark** · 正文表1–3在图像分类上比较 ResNet-50、ViT 的 Top-1。
- **关键结果 / 消融** · 正文分别报告从头训练与混合增强的表现。
- **适用条件 / 局限** · 需要稳定主体分离，场景本身决定标签时不能把背景任意替换。

**可复用机制** · 图像增强应优先保持主体语义，分开控制背景变化，再验收标签漂移。

<a id="paper-energyaction"></a>

## EnergyAction: Unimanual to Bimanual Composition with Energy-Based Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Song_EnergyAction_Unimanual_to_Bimanual_Composition_with_Energy-Based_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Song_EnergyAction_Unimanual_to_Bimanual_Composition_with_Energy-Based_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 单臂策略有较多训练数据，但直接并行不能保证双臂协作。
- **核心创新 / 方法** · 以能量模型表示单臂策略并组合，加入双臂协调。
- **Baseline** · 比较直接双臂训练及去掉各组合组件的变体。
- **Benchmark** · RLBench2 上20与100条演示，正文表1报告三次种子平均任务成功率。
- **关键结果 / 消融** · 正文表1–2分别检查低示范预算与组件贡献。
- **适用条件 / 局限** · 两臂任务必须能部分因子化，强接触和共同负载时需专门协调示范。

**可复用机制** · 双臂示范少时可分别利用单臂策略的能量并学习协调约束，再与双臂直接训练对照。

<a id="paper-clamp-defense"></a>

## Immunizing Models Against Harmful Long-Horizon Fine-Tuning via Contractive Optimization Dynamics

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Sarker_Immunizing_Models_Against_Harmful_Long-Horizon_Fine-Tuning_via_Contractive_Optimization_Dynamics_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Sarker_Immunizing_Models_Against_Harmful_Long-Horizon_Fine-Tuning_via_Contractive_Optimization_Dynamics_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 初始状态看似稳健的保护可能在许多次更新后退化。
- **核心创新 / 方法** · 通过约束受保护模型的微调动力学，尝试限制长期退化速度。
- **Baseline** · 对照既有保护与未保护模型，分别考察正常用途及防护保持。
- **Benchmark** · 正文表1–3包含分类、扩散和自回归模型的防御评测。
- **关键结果 / 消融** · 正文报告长程保护评测，并以若干模型家族检查迁移。
- **适用条件 / 局限** · 依赖所测训练条件，不能用短次测试或单模型保证其他部署范围。

**可复用机制** · 防御性模型保护应把长程微调纳入验收，短程表现不足以代表持续保护。

<a id="paper-projective-conditioning-view-synthesis"></a>

## From Rays to Projections: Better Inputs for Feed-Forward View Synthesis

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_From_Rays_to_Projections_Better_Inputs_for_Feed-Forward_View_Synthesis_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wu_From_Rays_to_Projections_Better_Inputs_for_Feed-Forward_View_Synthesis_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · Plücker 射线表示绑在任选世界坐标系上，对小幅相机变换敏感。
- **核心创新 / 方法** · 用目标视图投影线索进行图像到图像建模，另设计掩码预训练以利用未标定数据。
- **Baseline** · 射线条件模型、前馈三维高斯模型，RealEstate10K 对照包含 RayZer。
- **Benchmark** · 四种相机变换的一致性评测与 RealEstate10K 新视角任务，另分已见和未见像素。
- **关键结果 / 消融** · 表1显示投影输入更稳，表2–3比较新视角质量及覆盖区域。
- **适用条件 / 局限** · 投影输入受相机或几何信息质量制约，极低共视时需依赖生成先验。

**可复用机制** · 前馈新视角生成用目标图像平面的投影线索替代世界坐标射线。

<a id="paper-nexusflow"></a>

## NexusFlow: Unifying Disparate Tasks under Partial Supervision via Invertible Flow Networks

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Lin_NexusFlow_Unifying_Disparate_Tasks_under_Partial_Supervision_via_Invertible_Flow_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Lin_NexusFlow_Unifying_Disparate_Tasks_under_Partial_Supervision_via_Invertible_Flow_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 异构任务输出结构不同，共享训练信号难在无对应标签下获得。
- **核心创新 / 方法** · 以双射耦合层将各任务特征变换到规范空间，用可逆约束保留信息。
- **Baseline** · 与原多任务框架以及去掉可逆对齐的配置比较。
- **Benchmark** · 驾驶域划分下在线地图和多目标追踪，测分割 IoU、跟踪性能及特征 MMD，另测同构环境。
- **关键结果 / 消融** · 表1–3报告表示对齐和两任务的结果，检验耦合层贡献。
- **适用条件 / 局限** · 双射只保证可逆性，任务独有信息是否利于共享仍需实测。

**可复用机制** · 多任务标注不重叠时，以可逆坐标变换对齐特征，避免对齐损失直接丢弃原信息。

<a id="paper-mds-vqa"></a>

## MDS-VQA: Model-Informed Data Selection for Video Quality Assessment

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zou_MDS-VQA_Model-Informed_Data_Selection_for_Video_Quality_Assessment_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zou_MDS-VQA_Model-Informed_Data_Selection_for_Video_Quality_Assessment_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 目标域随机标注可能错过当前模型难例，单追难例又会集中在少数重复内容。
- **核心创新 / 方法** · 以排序目标训练错误预测器，贪心选同时覆盖高难度与内容多样性的视频。
- **Baseline** · 表2比较八种失败预测方法，表3同样5%预算比较标注选择。
- **Benchmark** · CGVDS、LIVE-Livestream、YouTube-SFV、AIGVQA-DB 等，报告 SRCC、PLCC 和 gMAD。
- **关键结果 / 消融** · 作者报告按目标域只选5%，均值 SRCC 从0.651至0.722。
- **适用条件 / 局限** · 需要初始带质量标注的信息学习失败预测；新域失败模式不总能被旧模型识别。

**可复用机制** · 制定小规模新域标注预算时，以排序预测模型失败程度，再用语义多样性避免重复采样。

<a id="paper-adpo-multi-aspect-preferences"></a>

## Aligning Multi-Character Narrative Image Generation with Multi-Aspect Human Preferences

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Gao_Aligning_Multi-Character_Narrative_Image_Generation_with_Multi-Aspect_Human_Preferences_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Gao_Aligning_Multi-Character_Narrative_Image_Generation_with_Multi-Aspect_Human_Preferences_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 单一奖励难同时代表提示遵循、身份和画质，强弱偏好也容易混同。
- **核心创新 / 方法** · 用分维度人类批评训练奖励模型，再根据维度支配关系及分差做自适应偏好优化。
- **Baseline** · 基础扩散模型、已有评价信号及去掉 ADPO 组件的对照。
- **Benchmark** · NI-RLHF 训练，NI-Bench 测偏好准确率，另报告美学、提示遵循、身份一致、视觉质量。
- **关键结果 / 消融** · 表1–3比较分维度奖励及训练结果，并做方法消融。
- **适用条件 / 局限** · 人类维度选择和奖励校准影响取舍，维度常冲突时不保证各项皆提高。

**可复用机制** · 多目标生成偏好不一致时，用维度优势和奖励边际分配训练强度。

<a id="paper-cad-ambiguity-weighted-partial-label-learning"></a>

## Mitigating Instance Entanglement in Instance-Dependent Partial Label Learning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_Mitigating_Instance_Entanglement_in_Instance-Dependent_Partial_Label_Learning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_Mitigating_Instance_Entanglement_in_Instance-Dependent_Partial_Label_Learning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 候选标签由样本特征决定时，近邻类别可能同时共享特征和候选标签，导致模型混淆。
- **核心创新 / 方法** · 增强候选类别特征并对齐同类增强表示，同时给较模糊的标签施加更强的区分惩罚。
- **Baseline** · 与偏标签学习方法比较，并以标准加权损失替代置信调整、移除表征学习或同时移除两者做消融。
- **Benchmark** · 实例相关偏标签分类，CIFAR-10、Fashion-MNIST 等，报告多次运行的分类准确率与标准差。
- **关键结果 / 消融** · Fashion-MNIST 准确率为 92.14%，改回标准加权为 91.19%，移除表征模块为 91.48%，两者均移除为 85.30%。
- **适用条件 / 局限** · 依赖候选集合和能表达类别差异的增强，作者指出扩散实现于细粒度数据存在相对弱点。

**可复用机制** · 候选标签随样本特征而变化时，可对照统一加权与偏重高歧义标签的间隔惩罚。见附录表 5。

<a id="paper-interrvos-role-conditioned-segmentation"></a>

## InterRVOS: Interaction-Aware Referring Video Object Segmentation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Jin_InterRVOS_Interaction-Aware_Referring_Video_Object_Segmentation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Jin_InterRVOS_Interaction-Aware_Referring_Video_Object_Segmentation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 单一指代表达的分割输出容易只找出施动者，忽略交互目标或混淆角色。
- **核心创新 / 方法** · ReVIOSa 为两个角色使用各自的分割标记，并对注意力施加角色掩膜监督。
- **Baseline** · 与 Sa2VA 等视频指代分割模型比较，消融无专用标记、无注意力掩膜损失和完整架构。
- **Benchmark** · InterRVOS-127K 的交互表达和分角色掩膜评测，报告 J、F 与 J&F。
- **关键结果 / 消融** · 表 3 无双角色标记且无注意力损失为 57.0 J&F，单独加损失为 58.5，单独加标记为 59.6，两者同用为 62.0。
- **适用条件 / 局限** · 依赖角色明确的表达和成对掩膜；多角色、角色发生改变或遮挡严重的设置需要另测。

**可复用机制** · 语言指令指定交互时，可给施动者和受动目标分配不同输出标记，并用角色级注意力监督和分项指标核对证据。见表 3。

<a id="paper-videoweaver-asynchronous-view-conditioning"></a>

## VideoWeaver: Multimodal Multi-View Video-to-Video Transfer for Embodied Agents

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Eskandar_VideoWeaver_Multimodal_Multi-View_Video-to-Video_Transfer_for_Embodied_Agents_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Eskandar_VideoWeaver_Multimodal_Multi-View_Video-to-Video_Transfer_for_Embodied_Agents_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 独立编辑机器人的多路视频容易产生跨视角外观与几何矛盾，固定路数也难适配不同相机数。
- **核心创新 / 方法** · 以 Pi3 产生的共享时空点云条件对齐视角，在不同视角采样不同扩散时步，让同一模型学习从已有视角生成新视角。
- **Baseline** · 与相机射线编码的多视角基线、直接加入共享时空点云的版本比较。
- **Benchmark** · Agibot 与 Droid 多视角测试集，报告 Met3R 一致性；单视角另测外观与指令质量。
- **关键结果 / 消融** · 表 2 两个测试集的基线 Met3R 为 0.597、0.481，加入点云为 0.612、0.533，异步时步且条件为单视角时为 0.624、0.578。
- **适用条件 / 局限** · 共享空间条件依赖视觉几何估计质量，作者报告强时间下采样会引入轻度模糊。

**可复用机制** · 需要从已有相机视角补齐新视角时，可训练各视角位于不同加噪阶段，并对照统一阶段的跨视角一致性。见表 2。

<a id="paper-toposlide-cluster-topology-pretext"></a>

## TopoSlide: Topologically-Informed Histopathology Whole Slide Image Representation Learning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Abousamra_TopoSlide_Topologically-Informed_Histopathology_Whole_Slide_Image_Representation_Learning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Abousamra_TopoSlide_Topologically-Informed_Histopathology_Whole_Slide_Image_Representation_Learning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 切片区域很大，基于块外观的聚合容易漏掉同类组织的空间组织。
- **核心创新 / 方法** · 按局部表示聚类，用持久同调描述各簇空间分布，以预测拓扑和对比学习共同训练切片表征。
- **Baseline** · 与同训练数据的 TITAN-V、GigaPath 以及冻结块编码器的均值池化比较。
- **Benchmark** · DHMC-LUAD 五类形态检索，以 1、3、5 近邻多数投票报告平衡准确率和宏 F1，另有生存与突变任务。
- **关键结果 / 消融** · 表 1 以 TCGA-LUAD 预训练时，1 近邻宏 F1 为 51.388，TITAN-V 为 41.570；CPTAC-LUAD 训练条件下，3 近邻没有超出 TITAN-V。
- **适用条件 / 局限** · 依赖局部簇能反映有用的形态，证据来自病理切片。迁移到遥感或长序列前需验证拓扑目标的语义。

**可复用机制** · 超大图像的局部块聚合可增加拓扑自监督，让全局表示预测各语义簇的空间形态。见第 3 节与表 1。

<a id="paper-resdit-position-extrapolation-resolution"></a>

## ResDiT: Evoking the Intrinsic Resolution Scalability in Diffusion Transformers

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Ma_ResDiT_Evoking_the_Intrinsic_Resolution_Scalability_in_Diffusion_Transformers_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Ma_ResDiT_Evoking_the_Intrinsic_Resolution_Scalability_in_Diffusion_Transformers_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 预训练 DiT 无训练增大分辨率时，空间布局可能塌陷，也可能保留布局但丢失细节。
- **核心创新 / 方法** · 对高分辨率推理的位置编码重定标，再使用训练分辨率大小的局部注意力和重叠融合补足纹理。
- **Baseline** · 与 DemoFusion、DiffuseHigh、I-Max、HiFlow 等高分辨率推理方案比较。
- **Benchmark** · 3072×3072 和 4096×4096 文本到图像，以 KID、IS、CLIP、局部指标与用户评分评估。
- **关键结果 / 消融** · 3072 分辨率 KID 为 0.0189，HiFlow 为 0.0190；4096 分辨率分别为 0.0217 和 0.0203，较大外推倍率已有退化。
- **适用条件 / 局限** · 要求能更改预训练 DiT 的位置编码和注意力，极端倍率仍需重新检验布局与画质。

**可复用机制** · 扩散 Transformer 外推分辨率时，可先检查位置编码，再比较局部细节模块是否必要。见正文位置编码分析及表 1。

<a id="paper-reach-error-conditioned-action-recovery"></a>

## REACH: Explicit Recovery Behavior for Diffusion Policies

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Ke_REACH_Explicit_Recovery_Behavior_for_Diffusion_Policies_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Ke_REACH_Explicit_Recovery_Behavior_for_Diffusion_Policies_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 扩散策略采样的动作存在多个模式，执行偏差会被后续动作放大。
- **核心创新 / 方法** · 用执行历史的误差检测触发扩散策略的负条件，抑制已经表现不佳的动作模式。
- **Baseline** · 比较 Diffusion Policy、没有错误检测器的 REACH 与完整 REACH。
- **Benchmark** · 仿真操控及真实机械臂的拿杯、放香蕉和叠积木，报告任务成功率。
- **关键结果 / 消融** · 真实叠积木中基础策略 32%，无检测器版本 30%，完整版本 42%；拿杯相应为 58%、66%、74%。
- **适用条件 / 局限** · 依赖历史能提供可区分的偏差证据，检测错误可能压制正确动作；真实实验证据来自三项操控任务。

**可复用机制** · 扩散策略执行错位时，先检测异常历史，再把不希望延续的动作模式作为负条件；可分别测提示和检测贡献。见表 4。

<a id="paper-rest-render-equivalence-consistency"></a>

## Same Content, Different Answers: Cross-Modal Inconsistency in MLLMs

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/van_Sprang_Same_Content_Different_Answers_Cross-Modal_Inconsistency_in_MLLMs_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/van_Sprang_Same_Content_Different_Answers_Cross-Modal_Inconsistency_in_MLLMs_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 多模态模型即使读对可见文字，也可能随语义相同输入的表示形式而改变回答。
- **核心创新 / 方法** · 构造等价的文本、图像和混合形式，分开测答题率和回答一致性，并以字符识别正确的样本控制 OCR 失误。
- **Baseline** · 比较 15 个多模态语言模型，并对照转换呈现形式和先识别后解题的策略。
- **Benchmark** · REST 与 REST+，指标包括 RER、CFR 和字符错误率，另控制颜色、分辨率和视觉词元量。
- **关键结果 / 消融** · 表 1 在 OCR 正确子集中，GPT-5-mini 的 CFR 为 8.7%，Qwen-2.5 32B 为 13.6%；表 4 先 OCR 再作答的表现也可能下降。
- **适用条件 / 局限** · 可控语义等价基于所构造题目，嵌入相似性和一致性的相关性不直接建立机制因果。

**可复用机制** · 诊断多模态推理时，把同一题变成文本、图片、混合输入，再在 OCR 完全正确子集检查跨模态一致性。见表 1、4。

<a id="paper-vibetoken"></a>

## VibeToken: Scaling 1D Image Tokenizers and Autoregressive Models for Dynamic Resolution Generations

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Patel_VibeToken_Scaling_1D_Image_Tokenizers_and_Autoregressive_Models_for_Dynamic_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Patel_VibeToken_Scaling_1D_Image_Tokenizers_and_Autoregressive_Models_for_Dynamic_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 固定网格词元器会随像素数增大推理开销，也限制不同长宽比的部署。
- **核心创新 / 方法** · 以分辨率无关的一维编码器输出32至256个词元，再用自回归模型生成。
- **Baseline** · 正文表1–3对照位置编码、图块设置和已有词元器与生成器。
- **Benchmark** · 按不同分辨率和长宽比评估重建与类条件生成，并比较生成 FID 和计算。
- **关键结果 / 消融** · 正文报告64词元生成1024×1024图像时 gFID 为3.94。
- **适用条件 / 局限** · 生成结论主要来自所测类条件数据，大分辨率下细节和推理吞吐应分别验证。

**可复用机制** · 将生成分辨率和视觉词元数分开设定，按长宽比和预算验收重建及生成。

<a id="paper-video-gmae"></a>

## Tracking by Predicting 3-D Gaussians Over Time

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Baranwal_Tracking_by_Predicting_3-D_Gaussians_Over_Time_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Baranwal_Tracking_by_Predicting_3-D_Gaussians_Over_Time_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 普通视频重建特征未显式维持跨帧三维对应。
- **核心创新 / 方法** · 掩码预训练学习时间变化的高斯原语，将高斯轨迹投影到二维做追踪。
- **Baseline** · 对照 VideoMAE 等自监督骨干，区分冻结编码器和少量追踪微调。
- **Benchmark** · 正文表1–3在 Kinetics、Kubric 等分别检验追踪、跨数据效果和设计消融。
- **关键结果 / 消融** · 正文报告少量微调后在 Kinetics 与 Kubric 相比既有自监督方案改善，冻结表示也能追踪。
- **适用条件 / 局限** · 高斯投影依赖可稳定关联的三维结构，复杂遮挡或快速运动时需额外验证。

**可复用机制** · 把视频隐表示建模成动态三维高斯，测试追踪是否能不经显式轨迹标注自然形成。

<a id="paper-tokensplat"></a>

## TokenSplat: Token-aligned 3D Gaussian Splatting for Feed-forward Pose-free Reconstruction

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_TokenSplat_Token-aligned_3D_Gaussian_Splatting_for_Feed-forward_Pose-free_Reconstruction_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_TokenSplat_Token-aligned_3D_Gaussian_Splatting_for_Feed-forward_Pose-free_Reconstruction_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 无位姿多视重建同时学习相机和场景，重复高斯及视角特征混入会造成不一致。
- **核心创新 / 方法** · 以粗词元位置及置信度融合跨视特征，使用非对称双流解码限制相机与图像词元的通信。
- **Baseline** · 比较既有无位姿前馈高斯模型及不同参考视图数量。
- **Benchmark** · 正文表1–4在 RE10K 与 ScanNet 比较新视图及相机位姿。
- **关键结果 / 消融** · 正文分别报告跨数据迁移、视角数变化下的画质和位姿。
- **适用条件 / 局限** · 依赖跨视语义对应及参考图覆盖，遮挡和低重叠场景可能产生融合错误。

**可复用机制** · 将相机词元和场景词元采用有方向的信息交换，并分开验收位姿与渲染质量。

<a id="paper-iris-spectral-depth"></a>

## Iris: Bringing Real-World Priors into Diffusion Model for Monocular Depth Estimation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Cai_Iris_Bringing_Real-World_Priors_into_Diffusion_Model_for_Monocular_Depth_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Cai_Iris_Bringing_Real-World_Priors_into_Diffusion_Model_for_Monocular_Depth_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 直接生成先验偏重外观，合成深度训练也易带入域偏差。
- **核心创新 / 方法** · 先做频率门控蒸馏迁移低频先验，再用高频一致性及合成真值细化，共享模型权重。
- **Baseline** · 与前馈及扩散深度估计比较，表3消融两阶段及频带约束。
- **Benchmark** · 正文表1–3评零样本仿射不变深度、推理耗时和训练组件。
- **关键结果 / 消融** · 正文分别比较跨域深度和有效推理开销，并评估频段分工。
- **适用条件 / 局限** · 合成与实际的频带差异未必可清晰切分，窄边缘、透明体等需复测。

**可复用机制** · 实域先验与合成真值可分别用于低频和高频约束，验证是否改善仿真到实拍的深度精细度。

<a id="paper-vifailback"></a>

## Diagnose, Correct, and Learn from Manipulation Failures via Visual Symbols

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zeng_Diagnose_Correct_and_Learn_from_Manipulation_Failures_via_Visual_Symbols_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zeng_Diagnose_Correct_and_Learn_from_Manipulation_Failures_via_Visual_Symbols_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 仿真失败样本往往不代表实机失败，而只标成功与否无法指导纠正。
- **核心创新 / 方法** · 对真实失败轨迹用视觉符号提供位置及动作纠正线索，构建诊断和修正对应。
- **Baseline** · 比较多种 VLM 并对照不同评测难度，表4另测任务成功率。
- **Benchmark** · 58128个视觉问答、5202条轨迹，正文表1–4报告诊断题准确率与纠正任务表现。
- **关键结果 / 消融** · 正文分别报告 Lite、Hard 的模型结果及三项操作任务成功率。
- **适用条件 / 局限** · 符号的标注一致性及实机动作接口会影响迁移，诊断准确不能代替安全执行验收。

**可复用机制** · 操控失败应分开考核识别、空间定位和纠正反馈，单独验证人能否把标注转为可执行信号。

<a id="paper-prelim-attention-hallucination"></a>

## PAS: Prelim Attention Score for Detecting Object Hallucinations in Large Vision-Language Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Hoang_PAS_Prelim_Attention_Score_for_Detecting_Object_Hallucinations_in_Large_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Hoang_PAS_Prelim_Attention_Score_for_Detecting_Object_Hallucinations_in_Large_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 模型可以沿已生成文本继续推论对象，而移除视觉信号也不改变判断。
- **核心创新 / 方法** · 用条件依赖分析声称的物体，再以历史词元注意构成无需新前向的代理分数。
- **Baseline** · 比较条件依赖估计、常用无训练检测以及不同解码设置。
- **Benchmark** · 正文表1–4在三个模型和两套数据上报告 AUROC、内存及解码影响。
- **关键结果 / 消融** · 正文给出跨模型和数据对照，并测轻量注意检测与更贵依赖估计的关系。
- **适用条件 / 局限** · 历史注意仅是相关代理，应复测真正依赖上下文但未幻觉的样本。

**可复用机制** · 检测物体幻觉时区分视觉条件与前文条件，先测额外推理前能否用历史注意做代理。

<a id="paper-unified-image-generation-risk-audit"></a>

## When Understanding Becomes a Risk: Authenticity and Safety Risks in the Emerging Image Generation Paradigm

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Leng_When_Understanding_Becomes_a_Risk_Authenticity_and_Safety_Risks_in_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Leng_When_Understanding_Becomes_a_Risk_Authenticity_and_Safety_Risks_in_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 输出失真会混入安全评估，旧架构上的检测精度也未必泛化到新生成器。
- **核心创新 / 方法** · 以相同评测维度比较多模态和扩散生成模型，区分正常输出、损坏输出与真实性检测表现。
- **Baseline** · 扩散生成模型、多模态生成模型及已有伪造检测器。
- **Benchmark** · 多套安全生成测试和真实性检测；报告输出损坏比例及安全分数等。
- **关键结果 / 消融** · 表1–3显示各模型损坏率和风险分布不同，原文也观察到生成架构切换后的检测退化。
- **适用条件 / 局限** · 结果受安全定义、模型版本和评测覆盖限制，不宜外推到所有生成器。

**可复用机制** · 比较生成器安全性时单独统计损坏输出，并按生成架构验证取证检测器。

<a id="paper-pamotion-contact-acceleration"></a>

## PAMotion: Physics-Aware Motion Generation for Full-Body Interaction with Multiple Objects

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Di_PAMotion_Physics-Aware_Motion_Generation_for_Full-Body_Interaction_with_Multiple_Objects_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Di_PAMotion_Physics-Aware_Motion_Generation_for_Full-Body_Interaction_with_Multiple_Objects_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 文本或姿态监督难保证手和多个物体交互的物理合理性。
- **核心创新 / 方法** · 同时预测人、物运动和加速度，用软损失联系加速度与接触，再分阶段细化手及旋转。
- **Baseline** · HIMO 原方法及已有多物体生成，表2–3去掉物理损失比较。
- **Benchmark** · HIMO 双物体和三物体交互设置，比较动作生成与文本检索相关指标。
- **关键结果 / 消融** · 表1报告除双物体 MM-Dist 等个别指标外总体改善，表2–3检验物理损失。
- **适用条件 / 局限** · 无显著加速度不排除静止接触，摩擦、约束和估计噪声可能破坏代理。

**可复用机制** · 人体物体运动生成时，将物体非重力加速度作为接触一致性的软监督。

<a id="paper-remix-continuous-decoding"></a>

## Rejection Mixing: Fast Semantic Propagation of Mask Tokens for Efficient DLLM Inference

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Ye_Rejection_Mixing_Fast_Semantic_Propagation_of_Mask_Tokens_for_Efficient_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Ye_Rejection_Mixing_Fast_Semantic_Propagation_of_Mask_Tokens_for_Efficient_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 多个词元同时提交可能各自高置信却彼此冲突。
- **核心创新 / 方法** · 在掩码态和已解码态之间加连续混合态并迭代表征，低置信时回退重处理，无需训练。
- **Baseline** · 同骨干常规并行解码及原文各表的其他加速方法。
- **Benchmark** · 语言与多模态理解推理基准，以准确率、Flickr30k CIDEr 和速度评估，并改变生成、块长度。
- **关键结果 / 消融** · 作者报告所测配置2–8倍加速，表1–3同时报告质量。
- **适用条件 / 局限** · 依赖模型能有效处理混合表征，不同序列长度、更近似的采样或阈值会改变收益。

**可复用机制** · 扩散语言模型并行解码时，先交换连续候选的信息，再提交离散词元，不确定位置退回掩码。

<a id="paper-ditta-video-distillation"></a>

## Bootstrapping Video Semantic Segmentation Model via Distillation-assisted Test-Time Adaptation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Kim_Bootstrapping_Video_Semantic_Segmentation_Model_via_Distillation-assisted_Test-Time_Adaptation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Kim_Bootstrapping_Video_Semantic_Segmentation_Model_via_Distillation-assisted_Test-Time_Adaptation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 逐帧语义模型不连续，每帧调用 SAM2 又昂贵且缺少语义。
- **核心创新 / 方法** · 在短时单遍初始化从 SAM2 蒸馏掩码传播，并加轻量时间融合。
- **Baseline** · 逐帧图像模型、视频监督模型和持续调用 SAM2 的零样本细化。
- **Benchmark** · VSPW 和 Cityscapes，按不同适配片段比例比较视频语义分割。
- **关键结果 / 消融** · 原文报告前10%片段即可在所测条件超过若干零样本细化方法；表2区分模块。
- **适用条件 / 局限** · 初始片段可能不代表后续场景，教师传播误差会进入学生。

**可复用机制** · 只能短时调用视频教师时，用开头片段蒸馏时序一致性，随后让轻量学生独立预测。

<a id="paper-svsm-compute-matched-scaling"></a>

## Scaling View Synthesis Transformers

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Kim_Scaling_View_Synthesis_Transformers_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Kim_Scaling_View_Synthesis_Transformers_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 过往架构比较受参数选择及训练算力不等影响。
- **核心创新 / 方法** · 在多算力预算下重做受控比较并拟合模型和数据缩放规律。
- **Baseline** · Geometry-free 新视角合成的纯解码方案与编码器—解码器，统一预算。
- **Benchmark** · 真实场景双视图新视角合成，256分辨率、相同片大小，比较重建、训练算力及 FPS。
- **关键结果 / 消融** · 表1显示最大规格用不到一半训练算力获得更好的所测重建指标，表2给出回归系数。
- **适用条件 / 局限** · 规律受所覆盖分辨率、架构族和训练规模限制。

**可复用机制** · 比较新视角模型架构时对齐训练 FLOPs，检验编码器—解码器是否真的不如纯解码器。

<a id="paper-multimodal-gaussian-tta"></a>

## Multi-modal Test-time Adaptation via Adaptive Probabilistic Gaussian Calibration

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_Multi-modal_Test-time_Adaptation_via_Adaptive_Probabilistic_Gaussian_Calibration_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_Multi-modal_Test-time_Adaptation_via_Adaptive_Probabilistic_Gaussian_Calibration_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 直接共享判别统计会让较强或较弱模态扭曲决策边界。
- **核心创新 / 方法** · 建立多模态类别条件分布，以自适应对比校正非对称性。
- **Baseline** · 对照经典 GDA、多模态测试适配方法与去校正版本。
- **Benchmark** · Kinetics50-C 与 VGGSound-C，分别扰动音频或视频，各类型和平均分类准确率。
- **关键结果 / 消融** · 表1–3报告双数据集不同损坏条件下的准确率。
- **适用条件 / 局限** · 分布可能非高斯，未标注伪标签不可靠或两路同时损坏时需要额外验证。

**可复用机制** · 测试时音视频质量不对称时，用类别条件高斯校准并纠正跨模态分布偏差。

<a id="paper-mpa-progressive-query-view-adaptation"></a>

## Cross-Domain Few-Shot Segmentation via Multi-view Progressive Adaptation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Nie_Cross-Domain_Few-Shot_Segmentation_via_Multi-view_Progressive_Adaptation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Nie_Cross-Domain_Few-Shot_Segmentation_via_Multi-view_Progressive_Adaptation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 源域训练的小样本分割模型在目标域起点较弱，直接使用强增强或只使用少量目标样本可能限制适配。
- **核心创新 / 方法** · 累积强增强得到逐渐更难的查询视图；顺序与并行预测路径共同利用这些视图，提升跨增强预测一致性。
- **Baseline** · 与 TAFT、CPFT、IFA 等适配策略相比；表 7 对照固定一个增强查询、始终使用简单增强与渐进调度。
- **Benchmark** · 四种低样本目标域的跨域小样本分割，作者比较目标域 mIoU 和不同适配设置。
- **关键结果 / 消融** · 表 7 固定单个增强查询为 50.5 mIoU，逐渐增加视图数为 52.0；始终使用简单增强为 51.3，逐渐提高增强难度为 52.4，两种进度组合为 53.1。
- **适用条件 / 局限** · 需要增强变换在任务中保持或可恢复标签，困难程度与额外视图的开销应随目标域重新评估。

**可复用机制** · 目标域只有少量监督时，可分别提高增强视图的难度和数量，并比较各进度对适配效果的影响。见表 7。

<a id="paper-c2lip-concept-phrase-contrastive-binding"></a>

## No Hard Negatives Required: Concept Centric Learning Leads to Compositionality without Degrading Zero-shot Capabilities of Contrastive Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Pham_No_Hard_Negatives_Required_Concept_Centric_Learning_Leads_to_Compositionality_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Pham_No_Hard_Negatives_Required_Concept_Centric_Learning_Leads_to_Compositionality_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 整句图文对比和全局池化允许模型识别概念，却可能不必区分某个属性依附于哪个对象。
- **核心创新 / 方法** · 从现有标题提取短名词短语，增加短语图像对比监督；用无参数的跨模态注意力池化汇聚短语对应的图像信息。
- **Baseline** · 以原 SigLIP ViT-B/16、同 CC3M 微调模型及只加入短语损失的模型为对照，并与使用困难负例的组合感知模型比较。
- **Benchmark** · SugarCrepe 等组合评估、属性绑定和 Flickr8K 检索，同时检查零样本和通用图文能力。
- **关键结果 / 消融** · 表 5 中 CC3M 微调基线的 SugarCrepe 平均为 81.7，增加短语损失后为 85.3，再加概念池化为 85.6；Flickr8K 从 95.2 到 96.4，但属性替换一列的完整模型略低于仅加短语损失。
- **适用条件 / 局限** · 依赖原始标题包含可分解的概念，且短语抽取质量影响监督；结果不能外推到没有明确局部绑定的语句。

**可复用机制** · 视觉语言模型的属性绑定不佳时，可先增加短概念短语监督，再核对概念条件池化的边际收益和通用检索表现。见表 5。

<a id="paper-ccf-complementary-sensor-masking"></a>

## CCF: Complementary Collaborative Fusion for Domain Generalized Multi-Modal 3D Object Detection

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_CCF_Complementary_Collaborative_Fusion_for_Domain_Generalized_Multi-Modal_3D_Object_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wu_CCF_Complementary_Collaborative_Fusion_for_Domain_Generalized_Multi-Modal_3D_Object_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 点云和图像融合检测中，点云主导的训练容易忽略图像，在点云退化时暴露弱点。
- **核心创新 / 方法** · 将不同传感器的空间区域互补遮盖，避免二者同时依赖同一可见区域；再为各单模态及融合查询分别提供监督。
- **Baseline** · 同一双分支检测器移除所有新模块作基线，分别加入解耦损失、深度先验或互补遮盖。
- **Benchmark** · nuScenes 划分源域、雨天、夜间和 Boston，以 mAP 与 NDS 衡量跨域检测。
- **关键结果 / 消融** · 表 3 只加互补遮盖时雨天 mAP 从 41.9 到 44.5，Boston 从 47.4 到 49.6，源域维持 68.4；只加解耦损失时夜间 mAP 从 42.9 降至 42.1。
- **适用条件 / 局限** · 空间互补依赖模态配准及其冗余结构，两者同时损坏或各自观察到互不重叠的内容时仍需验证。

**可复用机制** · 一个传感器主导融合时，可对照互补空间遮盖与原训练，检验弱模态是否成为有用后备。见表 3。

<a id="paper-hilbert-geo-formal-parse-solver-control"></a>

## Hilbert-Geo: Solving Solid Geometric Problems by Neural-Symbolic Reasoning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_Hilbert-Geo_Solving_Solid_Geometric_Problems_by_Neural-Symbolic_Reasoning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_Hilbert-Geo_Solving_Solid_Geometric_Problems_by_Neural-Symbolic_Reasoning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 立体图与自然语言条件交织，使直接作答的模型容易犯不可追溯的空间推理错误。
- **核心创新 / 方法** · 把图文解析成统一的条件描述语言，再用符号定理库做关系推断与代数计算；分别检查解析和可验证求解。
- **Baseline** · 比较 Gemini 2.5 Pro 等直接作答、使用同一模型生成形式条件，以及输入人工标注条件的求解器设置。
- **Benchmark** · SolidFGeo2k 四类立体几何问题和 MathVerse-Solid，以答案准确率衡量；另用模糊 Jaccard 评价形式解析。
- **关键结果 / 消融** · 表 1 中 Gemini 2.5 Pro 直接作答 54.2%，Hilbert-Geo 使用该模型解析为 77.3%，使用人工条件为 78.7%；后者仍低于人工解答 81.8%。
- **适用条件 / 局限** · 依赖领域谓词与定理库覆盖有效解法，人工条件下未解决的案例也可能来自搜索和规则覆盖。

**可复用机制** · 对图文推理接符号求解器时，可以用人工形式化输入测试求解上限，再与真实解析的端到端结果对照。见表 1 及第 6.3 节。

<a id="paper-opent2m-partwise-2d-motion-quantization"></a>

## OpenT2M: No-frill Motion Generation with Open-source, Large-scale, High-quality Data

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Cao_OpenT2M_No-frill_Motion_Generation_with_Open-source_Large-scale_High-quality_Data_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Cao_OpenT2M_No-frill_Motion_Generation_with_Open-source_Large-scale_High-quality_Data_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 把人体动作压到单一时间轴可能破坏同时发生的局部运动与部位依赖。
- **核心创新 / 方法** · 2D-PRQ 按身体部位组织动作，并用二维卷积在空间与时间轴共同做表征，再残差量化。
- **Baseline** · 比较 VQ-VAE、FSQ、RQ-VAE 和 PRQ，并用相同量化层数对照普通 PRQ 与 2D-PRQ。
- **Benchmark** · HumanML3D、Motion-X 与 OpenT2M 的动作重建，以 FID 和 MPJPE 衡量；另外评估文字到动作生成。
- **关键结果 / 消融** · 表 6 四层 2D-PRQ 与 PRQ 的 MPJPE 在 HumanML3D 为 28.628 与 28.703，Motion-X 为 54.493 与 73.989，OpenT2M 为 49.134 与 95.743。
- **适用条件 / 局限** · 依赖可定义的部位划分和固定拓扑；同一重建改进未必对应新骨架或少量数据上的生成表现。

**可复用机制** · 动作表示可以按身体部位保留空间轴并与时间联合量化；先在不同动作复杂度的数据上实测重建，再决定是否换分词器。见表 6。

<a id="paper-genmask"></a>

## GenMask: Adapting DiT for Segmentation via Direct Mask Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_GenMask_Adapting_DiT_for_Segmentation_via_Direct_Mask_Generation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yang_GenMask_Adapting_DiT_for_Segmentation_via_Direct_Mask_Generation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 直接借用图像去噪分布训练掩码会忽略掩码潜变量的高可分性。
- **核心创新 / 方法** · 用预训练 DiT 直接生成掩码，并为二值目标增加对极端噪声级的采样。
- **Baseline** · 与间接提取生成特征及其他时间步采样策略比较。
- **Benchmark** · 正文表1–3报告指代分割及 ReasonSeg，表3比较采样策略。
- **关键结果 / 消融** · 正文展示用面向掩码的采样调整后可直接做生成式分割。
- **适用条件 / 局限** · 依赖掩码编码器保留窄区域与边界，软标签或多类别掩码必须重新测噪声分布。

**可复用机制** · 根据输出潜分布设定扩散采样日程，二值掩码与自然图像分开对照。

<a id="paper-dpl-missing-modality"></a>

## DPL: Decoupled Prototype Learning for Enhancing Robustness of Vision-Language Transformers to Missing Modalities

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Lu_DPL_Decoupled_Prototype_Learning_for_Enhancing_Robustness_of_Vision-Language_Transformers_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Lu_DPL_Decoupled_Prototype_Learning_for_Enhancing_Robustness_of_Vision-Language_Transformers_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 用同一分类头处理完整和缺失输入会让类别证据不对称。
- **核心创新 / 方法** · 依缺失模式选择原型，再分解为图像和文字分量以计算类别分数。
- **Baseline** · 正文表3比较全连接头、DePT 和 DPL，表1–2变化缺失率及骨干。
- **Benchmark** · 正文包含 Hateful-Memes 等数据，按不同模态可得条件测分类表现和 AUROC。
- **关键结果 / 消融** · 正文在多骨干和缺失场景检验分类头的收益。
- **适用条件 / 局限** · 未见缺失组合和低质量但未缺失的模态需要独立评估。

**可复用机制** · 缺失模态时不仅调整输入提示，也应让分类原型按实际可用模态变化。

<a id="paper-fedcart-defense"></a>

## FedCART: Tackling Long-Tailed Distributions in Federated Adversarial Training via Classifier Refinement

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Qin_FedCART_Tackling_Long-Tailed_Distributions_in_Federated_Adversarial_Training_via_Classifier_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Qin_FedCART_Tackling_Long-Tailed_Distributions_in_Federated_Adversarial_Training_via_Classifier_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 全局长尾与客户端异质性可能使低频类表现被整体分数掩盖。
- **核心创新 / 方法** · 用分类器精化处理特征偏斜与分类边界问题，改善防御训练。
- **Baseline** · 与常用联邦稳健训练方法对照，并按类频率和异质性分层。
- **Benchmark** · 正文表1–3使用不同数据和异质性条件，分别报告自然和稳健准确率。
- **关键结果 / 消融** · 正文定位长尾条件下的表征及分类器问题，并报告不同类别组表现。
- **适用条件 / 局限** · 结论依赖分组样本量和客户端构成，未测部署条件需要重新核查。

**可复用机制** · 联邦稳健训练要按类别频率分拆干净与稳健表现，再判断是否进行分类器精化。

<a id="paper-aemg"></a>

## Reading Your Actions: Learning Generalizable Action Representations via Pre-training AEMG

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_Reading_Your_Actions_Learning_Generalizable_Action_Representations_via_Pre-training_AEMG_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_Reading_Your_Actions_Learning_Generalizable_Action_Representations_via_Pre-training_AEMG_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 设备、人员和动作协议差异使直接共享原始时序表示失效。
- **核心创新 / 方法** · 用收缩级词元编码基础动态，利用跨设备信号和自监督时序上下文预训练。
- **Baseline** · 对照现有肌电表示及不同少样本适配预算。
- **Benchmark** · 正文表1做留一受试者识别，表2比较少样本适配。
- **关键结果 / 消融** · 正文报告未见受试者手势识别和少样本迁移，并将两种设置区分。
- **适用条件 / 局限** · 依赖设备与个体的收缩事件可对齐，传感布置变化需要单独复验。

**可复用机制** · 生理时序预训练可先将局部收缩与跨时模式分成不同层级，再按未见受试者和设备分别验证。

<a id="paper-dfa-frequency-affinity"></a>

## Frequency-Aware Affinity for Weakly Supervised Semantic Segmentation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_Frequency-Aware_Affinity_for_Weakly_Supervised_Semantic_Segmentation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yang_Frequency-Aware_Affinity_for_Weakly_Supervised_Semantic_Segmentation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 视觉注意力的平滑性会让伪标签混过边缘或无法覆盖内部。
- **核心创新 / 方法** · 用低频相关增强类内一致，并保留高频关联约束边界。
- **Baseline** · 对照原始类别激活结果与仅使用分频单支路的变体。
- **Benchmark** · 正文表1–3在 PASCAL 等分割上分开报告种子、伪标签及最终结果。
- **关键结果 / 消融** · 正文比较不同模块对初始定位和最终分割的作用。
- **适用条件 / 局限** · 高频不一定是真实边界，噪声和纹理复杂时要控制误扩散。

**可复用机制** · 弱监督分割扩散伪标签时可将低频语义和高频边界作为不同传播信号。

<a id="paper-openvision-2-generative-pretraining"></a>

## OpenVision 2: A Family of Generative Pretrained Visual Encoders for Multimodal Learning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_OpenVision_2_A_Family_of_Generative_Pretrained_Visual_Encoders_for_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_OpenVision_2_A_Family_of_Generative_Pretrained_Visual_Encoders_for_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 对比目标额外需要文本编码器和大批次资源，其下游增益不明。
- **核心创新 / 方法** · 移除 OpenVision 文本编码器与对比损失，仅由描述生成监督视觉编码。
- **Baseline** · 原 OpenVision、CLIP 变体，接入 LLaVA-1.5 与 Open-LLaVA-Next 对照。
- **Benchmark** · 多模态理解和 OCR 等任务；TPU v4-512 测训练效率。
- **关键结果 / 消融** · ViT-L/14 训练从83小时到57小时，显存从24.5 GB到13.8 GB；下游整体有竞争力。
- **适用条件 / 局限** · 结论主要针对接入生成式解码器，检索等依赖直接图文嵌入对齐的任务需另验。

**可复用机制** · 面向多模态解码器预训练视觉编码器时，把只用描述损失作为单独受控的低成本基线。

<a id="paper-failureatlas"></a>

## FailureAtlas: Mapping the Failure Landscape of T2I Models via Active Exploration

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_FailureAtlas_Mapping_the_Failure_Landscape_of_T2I_Models_via_Active_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_FailureAtlas_Mapping_the_Failure_Landscape_of_T2I_Models_via_Active_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 固定提示集合难定位哪种条件组合触发错误，也难估计遗漏范围。
- **核心创新 / 方法** · 以可组合概念展开主动诊断并收缩到较小错误切片，之后关联训练数据稀缺性。
- **Baseline** · 表1与固定评测的概念覆盖比较，并分析多个 Stable Diffusion 模型。
- **Benchmark** · 概念和属性覆盖、错误切片大小及训练数据频次，表2按模型和层级报告。
- **关键结果 / 消融** · SD1.5 发现超过24.7万个切片，作者强调不能直接把数量作为跨模型排名。
- **适用条件 / 局限** · 诊断依赖评价器、概念词表及训练统计，数据稀缺与错误的相关性不能确立全部因果。

**可复用机制** · 审计生成模型时搜索导致稳定错误的最小概念组合，并用训练分布频次检查覆盖缺口。

<a id="paper-srcp-visual-unsupervised-rl"></a>

## Saliency-Guided Representation with Consistency Policy Learning for Visual Unsupervised Reinforcement Learning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Sun_Saliency-Guided_Representation_with_Consistency_Policy_Learning_for_Visual_Unsupervised_Reinforcement_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Sun_Saliency-Guided_Representation_with_Consistency_Policy_Learning_for_Visual_Unsupervised_Reinforcement_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 高维观测下后继目标可能关注无关区域，损害零样本技能控制。
- **核心创新 / 方法** · 引入显著性引导的动态任务，独立于后继训练，并以快速一致性策略建模多种可能技能。
- **Baseline** · 已有后继类无监督策略及不同表征和策略消融。
- **Benchmark** · 16项零样本控制任务，四数据集四种子，比较回报；RND 用于模块和参数消融。
- **关键结果 / 消融** · 表1–3报告跨任务及领域回报，并检查显著性与策略模块。
- **适用条件 / 局限** · 环境动态不易从图像辨识时，显著性代理可能误选背景，仿真不能代替实机。

**可复用机制** · 视觉无监督强化学习先单独学习动力相关表征，再估计后继测度和训练技能策略。

<a id="paper-i-scene-instance-generator"></a>

## I-Scene: 3D Instance Models are Implicit Generalizable Spatial Learners

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Ling_I-Scene_3D_Instance_Models_are_Implicit_Generalizable_Spatial_Learners_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Ling_I-Scene_3D_Instance_Models_are_Implicit_Generalizable_Spatial_Learners_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 真实场景组合规模有限，场景模型容易记忆布局。
- **核心创新 / 方法** · 在视角中心空间把实例生成器调整为可编码场景关系的模型，并用无语义随机对象组合监督。
- **Baseline** · 与 PartCrafter 等景物生成方法比较，消融场景上下文、坐标与无语义组合。
- **Benchmark** · 3D-FRONT、BlendSwap、Scenethesis，按场景和物体测 Chamfer、F-score 和边界框体积 IoU。
- **关键结果 / 消融** · 表1–3给出未见组合表现及随机组合监督的效果。
- **适用条件 / 局限** · 实例先验覆盖受限，几何关系不一定对应语义、物理支撑或可操作性。

**可复用机制** · 场景训练数据少时，用预训练单物体生成器的几何先验在随机组合场景中学习布局。

<a id="paper-synthetic-data-aesthetic-bias"></a>

## When Pretty Isn't Useful: Investigating Why Modern Text-to-Image Models Fail as Reliable Training Data Generators

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Adamkiewicz_When_Pretty_Isnt_Useful_Investigating_Why_Modern_Text-to-Image_Models_Fail_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Adamkiewicz_When_Pretty_Isnt_Useful_Investigating_Why_Modern_Text-to-Image_Models_Fail_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 生成外观指标变好可能与训练样本对真实分布的覆盖下降同时发生。
- **核心创新 / 方法** · 以受控类别提示为2022–2025年的生成器构建合成集，训练固定分类器，再按真实测试和覆盖指标比较。
- **Baseline** · 不同年代模型的合成训练集，以标准 ResNet-50 和真实测试作为共同设置。
- **Benchmark** · ImageNet-1K 的200类别子集，合成训练并在真实相应类别评测，同时分析语义匹配和分布。
- **关键结果 / 消融** · 图1及正文报告新生成器的审美和提示对齐更好，但真实分类准确率呈下降，伴随更集中覆盖。
- **适用条件 / 局限** · 仅用所测模型和分类条件，不代表合成数据用于检测或操作时必然同趋势。

**可复用机制** · 选择合成训练数据生成器时，用真实下游准确率及覆盖度作门槛，不以图好看或提示匹配选型。

<a id="paper-refine-active-learning"></a>

## Cleaning the Pool: Progressive Filtering of Unlabeled Pools in Deep Active Learning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Huseljic_Cleaning_the_Pool_Progressive_Filtering_of_Unlabeled_Pools_in_Deep_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Huseljic_Cleaning_the_Pool_Progressive_Filtering_of_Unlabeled_Pools_in_Deep_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 只用不确定性或代表性在不同轮次和数据集的表现不稳。
- **核心创新 / 方法** · 迭代筛选候选并以覆盖目标组批，使不同策略偏好的样本都可能留下。
- **Baseline** · 单策略主动学习和已有组合方法，另检验对单策略加预筛。
- **Benchmark** · 六个分类集、三个基础模型，另测音频频谱；以学习曲线面积等评价。
- **关键结果 / 消融** · 作者报告多数据集组合改善，音频例说明预筛本身也可带来收益。
- **适用条件 / 局限** · 选择依据及过滤强度影响少数类，集成查询比单策略有额外成本。

**可复用机制** · 每轮主动学习先用多个策略交替缩小未标注池，再按不同信息价值的覆盖选最终批次。

<a id="paper-spectemp-draft-frame-proposal"></a>

## Thinking with Drafts: Speculative Temporal Reasoning for Efficient Long Video Understanding

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Hu_Thinking_with_Drafts_Speculative_Temporal_Reasoning_for_Efficient_Long_Video_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Hu_Thinking_with_Drafts_Speculative_Temporal_Reasoning_for_Efficient_Long_Video_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 推理与反复看帧共用一个模型时，多模态上下文越积越大。
- **核心创新 / 方法** · 用轻量草稿模型在候选时间段找证据帧，目标模型核实这些帧并逐轮修正检索和推理。
- **Baseline** · 比较均匀选帧、目标模型加 CLIP 选帧、单独 7B 或 3B 的设置。
- **Benchmark** · 长视频问答任务包括 LongVideoBench、Video-MME 与 Video-Holmes，报告准确率、帧数和推理时延。
- **关键结果 / 消融** · 表 4 中 7B 单模型为 54.1%、3.1 秒，7B 加 3B 为 57.5%、2.3 秒；表 3 中该组合平均使用 14.1 帧，目标加 CLIP 使用 16 帧。
- **适用条件 / 局限** · 时延收益取决于两个模型的部署安排，低质量候选帧可能让验证器找不到正确证据。

**可复用机制** · 长视频推理可以把密集找帧交给轻量模型，将判断和复核留给大模型，并以准确率和实际时延一起评价。见表 3、4。

<a id="paper-infmatch-terminal-data-influence"></a>

## Dataset Distillation by Influence Matching

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Tan_Dataset_Distillation_by_Influence_Matching_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Tan_Dataset_Distillation_by_Influence_Matching_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 逐步匹配梯度或训练轨迹，可能仍得到对最终模型作用不同的合成样本。
- **核心创新 / 方法** · 展开优化过程并以一阶近似估计增减样本对终点参数的影响，通过匹配真实和合成数据集的影响优化合成数据。
- **Baseline** · 分类与 NCFM 等比较；图文蒸馏与 DATM、梯度匹配、随机与 Herding 选择比较。
- **Benchmark** · CIFAR、Tiny-ImageNet 的低样本分类及 Flickr30K 图文双向检索。
- **关键结果 / 消融** · 每类 10 张时 Tiny-ImageNet 准确率 31.5%，高于 NCFM 4.7 个百分点；图 4 的 200 个样本图搜文结果为 7.4%，DATM 为 1.3%。
- **适用条件 / 局限** · 结果依赖一阶近似和展开轨迹能否近似收敛后的相对影响，换优化器或网络应重新检查迁移。

**可复用机制** · 合成数据蒸馏可直接匹配样本对最终参数的影响，并用下游检索与分类对比轨迹匹配。见第 4、5 节。

<a id="paper-rds-mask-conditioned-video-routing"></a>

## Efficient Video Object Segmentation and Tracking with Recurrent Dynamic Submodel

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Tang_Efficient_Video_Object_Segmentation_and_Tracking_with_Recurrent_Dynamic_Submodel_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Tang_Efficient_Video_Object_Segmentation_and_Tracking_with_Recurrent_Dynamic_Submodel_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 视频跟踪与分割输入难度变化大，固定模型剪枝和仅看当前帧的动态路由难以利用任务时序。
- **核心创新 / 方法** · 预测感知路由器融合前帧掩膜与当前视觉特征，一次选择该帧使用的子模型块。
- **Baseline** · 比较静态剪枝、仅图像或仅掩膜路由，以及使用一帧、多帧掩膜的路由器。
- **Benchmark** · 在 SAM2 系列视频分割和跟踪上评测 J&F、路由开销以及少帧率下的稳定性。
- **关键结果 / 消融** · 表 5 仅前一帧为 89.6 J&F，增加到两帧仍为 89.6，四帧为 89.4；图 7 单独依赖掩膜会错过外观变化。
- **适用条件 / 局限** · 需要上轮预测可信，遮挡、长时间跟踪丢失或场景切换时应评估错误是否传给后续路由。

**可复用机制** · 视频推理的条件路由可以使用上一帧的预测掩膜和当前帧特征，比较更长预测记忆是否值得。见表 4、5 和图 7。

<a id="paper-sparse-depth-vlm-mask-guidance"></a>

## Zero-Shot Depth Completion with Vision-Language Model

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yan_Zero-Shot_Depth_Completion_with_Vision-Language_Model_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yan_Zero-Shot_Depth_Completion_with_Vision-Language_Model_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 纯 RGB 模型缺少绝对尺度，直接插入稀疏距离值还可能扰动预训练视觉表示。
- **核心创新 / 方法** · 以稀疏深度提供视觉标记的几何信息，再用观测掩膜提示需要保持与补全的位置，以稀疏数据生成文本监督。
- **Baseline** · 比较拼接、不同初始化的视觉注入，以及逐步加入掩膜提示和稀疏监督。
- **Benchmark** · VOID 的 150 个深度点消融，报告米制 MAE、RMSE；零样本评测涵盖其他传感器、密度与场景。
- **关键结果 / 消融** · 表 5 在基础软注入之后增加掩膜提示，MAE 从 0.197 米降为 0.188 米，RMSE 从 0.623 米降为 0.608 米。
- **适用条件 / 局限** · 需要与图像对齐的物理深度观测；点位偏差、距离噪声或观测分布变化时需要重新量化误差。

**可复用机制** · 当几何传感器只给出少量观测时，可以把观测数值和观测位置分开编码，测量位置本身对补全误差的影响。见表 5。

<a id="paper-ldf-vfi-skip-concatenate-sampling"></a>

## Towards Holistic Modeling for Video Frame Interpolation with Auto-regressive Diffusion Transformers

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Peng_Towards_Holistic_Modeling_for_Video_Frame_Interpolation_with_Auto-regressive_Diffusion_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Peng_Towards_Holistic_Modeling_for_Video_Frame_Interpolation_with_Auto-regressive_Diffusion_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 按时间顺序逐段插帧会把上一段生成误差传递下去；完全独立生成则可能产生接缝。
- **核心创新 / 方法** · 周期性生成不依赖最近生成块的片段，随后用相邻上下文填补间隔，减少错误传播同时保持衔接。
- **Baseline** · 以同一模型、同一无条件 VAE 的标准因果顺序为对照；另比较条件 VAE。
- **Benchmark** · SNU-FILM 4、8、16 倍插帧及 X4K，报告 FVD、LPIPS 和推理时间。
- **关键结果 / 消融** · 表 3 保持无条件 VAE 不变时，改变采样顺序使平均 FVD 从 22.67 降为 17.05，LPIPS 从 0.062 降为 0.060。
- **适用条件 / 局限** · 利用已知低帧率视频的时间锚点，纯向前预测或缺乏锚点的任务需要重新设计顺序并验证。

**可复用机制** · 长序列自回归生成出现漂移时，可以检验跳过最近生成片段作为条件的采样次序，并比较块边界一致性。见图 5、表 3。

<a id="paper-r4-semantic-spatiotemporal-memory-retrieval"></a>

## R4: Retrieval-Augmented Reasoning for Vision-Language Models in 4D Spatio-Temporal Space

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Sohn_R4_Retrieval-Augmented_Reasoning_for_Vision-Language_Models_in_4D_Spatio-Temporal_Space_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Sohn_R4_Retrieval-Augmented_Reasoning_for_Vision-Language_Models_in_4D_Spatio-Temporal_Space_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 文本或帧相似度检索容易遗漏问题要求的位置、时间和物体历史。
- **核心创新 / 方法** · 将物体语义写入度量坐标和时间索引，拆分查询的语义、空间与时间条件，检索相关事件并迭代回答。
- **Baseline** · 对照不使用检索键、单独使用某个键及多键组合；与现有视觉语言模型和情景问答系统比较。
- **Benchmark** · OpenEQA 的 ScanNet 和 HM3D 情景记忆问答，以 LLM-Match 衡量；另测试 ERQA 与 VLM4D。
- **关键结果 / 消融** · 表 5 的 All 分数无键 49.8、仅语义 56.2、语义加空间 74.7、再加时间 78.6。
- **适用条件 / 局限** · 依赖位姿和对象级描述对齐，位置误差或重识别失败可能写入错误记忆；自动评分还需人评补充。

**可复用机制** · 空间问答的情景记忆应分别评估语义、空间和时间索引，并检验定位键加入语义检索后的增量。见表 5。

<a id="paper-semanticvla"></a>

## SemanticVLA: Towards Semantic Reasoning over Action Memorization via Synergistic Explicit Trace and Latent Action Planning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Ni_SemanticVLA_Towards_Semantic_Reasoning_over_Action_Memorization_via_Synergistic_Explicit_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Ni_SemanticVLA_Towards_Semantic_Reasoning_over_Action_Memorization_via_Synergistic_Explicit_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · VLA 易记住动作模式，遇到指令改写或新任务组合时语义迁移不稳。
- **核心创新 / 方法** · 联合预测显式末端执行器轨迹与隐式动作 token，用两者共同向低层策略提供计划。
- **Baseline** · 表1比较 π0、UniVLA、MolmoAct、ThinkAct 等。
- **Benchmark** · 表1为 LIBERO 四任务套件与 SimplerEnv WidowX 的成功率，表2评估真实 Franka，§4.3 测试指令变化。
- **关键结果 / 消融** · 表1平均成功率 LIBERO 为97.0%，SimplerEnv 为65.1%。表2真实机器人平均62.3%，π0 为48.0%。
- **适用条件 / 局限** · 显式末端轨迹依赖可获得的动作标注和坐标定义，换用非机械臂动作空间需重新验证。

**可复用机制** · 把可解释轨迹和隐动作计划作为两路接口，分别检验语义泛化与精细控制。

<a id="paper-aergs-slam"></a>

## AERGS-SLAM: Auto-Exposure-Robust Stereo 3D Gaussian Splatting SLAM

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhou_AERGS-SLAM_Auto-Exposure-Robust_Stereo_3D_Gaussian_Splatting_SLAM_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhou_AERGS-SLAM_Auto-Exposure-Robust_Stereo_3D_Gaussian_Splatting_SLAM_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 自动曝光改变亮度外观，干扰视觉里程计和光度重建。
- **核心创新 / 方法** · 将相机曝光网络整合进高斯渲染；定位与地图初始化另外使用光照鲁棒几何特征。
- **Baseline** · 表1–2比较 Photo-SLAM、SEGS-SLAM 等，图6加入换用 HDRGS 的系统变体。
- **Benchmark** · EuRoC MAV 与自采序列的定位 RMSE 和光真实建图指标，表3消融曝光与光照鲁棒组件。
- **关键结果 / 消融** · 表1–3报告模型在曝光变化下的定位和建图结果；图示报告渲染3700 FPS，HDR-GS 变体为416 FPS。
- **适用条件 / 局限** · 依赖双目输入，自采序列部分定位用 DROID-SLAM 位姿作参考，不能视作外部真值。

**可复用机制** · 让定位用光照鲁棒特征，渲染端单独估计曝光。

<a id="paper-rosetta-unified-tokenizer"></a>

## Rosetta Stone For Unified MLLMs: A Unified Tokenizer to Decipher Understanding and Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Sun_Rosetta_Stone_For_Unified_MLLMs_A_Unified_Tokenizer_to_Decipher_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Sun_Rosetta_Stone_For_Unified_MLLMs_A_Unified_Tokenizer_to_Decipher_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 同一视觉码本同时对比对齐和像素重建时，两类目标可能竞争。
- **核心创新 / 方法** · 分层解耦冲突代理任务，扩充语义监督，并以注意力优先映射把语义先验传给细粒度生成。
- **Baseline** · 表1比较像素、语义或混合 tokenizer，表3比较 TokenFlow 等统一模型。
- **Benchmark** · ImageNet 验证集 rFID、PSNR、SSIM、零样本准确率；表3理解集与表4 GenAI-Bench、MJHQ-30K。
- **关键结果 / 消融** · 表1在256分辨率取得 rFID 0.33 和零样本80.9%；表3离散7B理解均分63.23。
- **适用条件 / 局限** · 需要独立监督特征和训练 tokenizer，原文结果集中在图像输入，迁移到视频或动作需重新验证。

**可复用机制** · 按量化层分配语义和纹理目标，并分开审计理解与生成。

<a id="paper-anoco"></a>

## Anomaly as Non-Conformity via Training-Free Graph Laplacian Energy Minimization

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Seo_Anomaly_as_Non-Conformity_via_Training-Free_Graph_Laplacian_Energy_Minimization_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Seo_Anomaly_as_Non-Conformity_via_Training-Free_Graph_Laplacian_Energy_Minimization_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 只按局部相似度比较可能漏掉细微缺陷，而联合平滑会稀释异常证据。
- **核心创新 / 方法** · 仅连查询和正常锚点，求解锚定图能量，取查询特征被迫调整的幅度为异常分数。
- **Baseline** · 表1比较 SPADE、PatchCore、WinCLIP、PromptAD 等，表2单独变动打分和二部图。
- **Benchmark** · MVTec-AD、VisA 的少样本图像级检测与像素级定位，表4另列 OCT2017。
- **关键结果 / 消融** · 表1–3支持位移打分和二部图在少样本下的组合，表4给出跨到 OCT 图像的补充证据。
- **适用条件 / 局限** · 仍需少量可信正常锚点和可比的冻结特征；参考受污染或工况变化须复验。

**可复用机制** · 少正常样本时，试用与固定参考对齐所需的位移替代最近邻距离。

<a id="paper-ttl-ood"></a>

## TTL: Test-time Textual Learning for OOD Detection with Pretrained Vision-Language Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Ye_TTL_Test-time_Textual_Learning_for_OOD_Detection_with_Pretrained_Vision-Language_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Ye_TTL_Test-time_Textual_Learning_for_OOD_Detection_with_Pretrained_Vision-Language_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 预先给出的负类文字难覆盖持续出现的未知语义。
- **核心创新 / 方法** · 用无标签流生成伪标签并筛选可信异常样本，以更新负提示和维护文本特征库。
- **Baseline** · 表1–2比较 MCM 等 VLM OOD 方法，表3消融学习、纯化和特征库。
- **Benchmark** · ImageNet-1k 与 CIFAR-100 OOD 协议，FPR95 和 AUROC。
- **关键结果 / 消融** · 表1平均12.46 FPR95、97.29 AUROC；表2分别为2.36和99.26。
- **适用条件 / 局限** · 自适应受伪标签和批次组成影响，部署前需测试随时间转变的类别比例。

**可复用机制** · 面对未知类变化，可用冻结视觉编码和自更新负文本提示校准，而非增加固定负类词表。

<a id="paper-egovit"></a>

## Towards Stable Self-Supervised Object Representations in Unconstrained Egocentric Video

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Tan_Towards_Stable_Self-Supervised_Object_Representations_in_Unconstrained_Egocentric_Video_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Tan_Towards_Stable_Self-Supervised_Object_Representations_in_Unconstrained_Egocentric_Video_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 第一人称视频的遮挡和相机运动使逐帧整体一致性难稳定追踪对象。
- **核心创新 / 方法** · 在帧内蒸馏中形成 proto-object，以单目深度正则约束，再用教师筛选可跨帧施加一致性的对象。
- **Baseline** · 表1同数据从头训练 DINO 等，表2–3比较几何先验与帧级、未过滤原型级一致性。
- **Benchmark** · 表1覆盖语义/实例分割、检测、VOS、对象发现和分类；表4比较深度质量与来源。
- **关键结果 / 消融** · 65分钟视频训练的 EgoViT 相比 DINO，表1语义分割 mIoU +4.8点，对象发现 CorLoc +8.0点；表2 P+T 缺深度时退化。
- **适用条件 / 局限** · 要求视频中有足够的对象重现及可用几何先验，表1主要验证视觉任务。

**可复用机制** · 跨帧一致性应作用在可信对象原型上，同时单测几何先验是否必要。

<a id="paper-aeic"></a>

## Ultra-Low Bitrate Perceptual Image Compression with Shallow Encoder

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Ultra-Low_Bitrate_Perceptual_Image_Compression_with_Shallow_Encoder_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Ultra-Low_Bitrate_Perceptual_Image_Compression_with_Shallow_Encoder_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 极低码率下缩减编码网络会同时损害重建，且生成解码可能过慢。
- **核心创新 / 方法** · 用浅层编码器和单步扩散解码，让中等编码器版本跨编码、解码两侧蒸馏特征。
- **Baseline** · 表2比较实际编码与解码延迟，表3比较参数及 MAC，表4消融空间压缩率。
- **Benchmark** · 低于0.05 bpp 的率失真与感知权衡，表2跨 GPU 和分辨率测试。
- **关键结果 / 消融** · 官方正文报告1080p 实际编码达到35.8 FPS，表2将自回归熵编码一并计入。
- **适用条件 / 局限** · 偏重发送侧轻量且接受生成式重建的场景，真实纹理保真应另测。

**可复用机制** · 边缘端预算更紧时可把容量移向解码端，并用跨端蒸馏稳定浅编码。

<a id="paper-t2sgrid"></a>

## T2SGrid: Temporal-to-Spatial Gridification for Video Temporal Grounding

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Guo_T2SGrid_Temporal-to-Spatial_Gridification_for_Video_Temporal_Grounding_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Guo_T2SGrid_Temporal-to-Spatial_Gridification_for_Video_Temporal_Grounding_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 逐帧时间标注增大开销或遮挡画面，纯位置编码又难输出绝对时间。
- **核心创新 / 方法** · 将重叠时间窗口的帧按行排列成网格图，并以组合文本时间戳定位网格的全局位置。
- **Baseline** · 表1比较视频定位模型，表2以相同数据和设置比较 LLaVA-OneVision-1.5-8B 普通微调，表4消融。
- **Benchmark** · Charades-STA、ActivityNet 的 Recall@IoU 和 mIoU；表3 Video-MME、MVBench、VideoInstruct。
- **关键结果 / 消融** · 表2同设置下网格微调优于普通微调；正文去重叠对照 mIoU 由41.2变为44.3，但耗时由1.43 s 增至2.31 s。
- **适用条件 / 局限** · 帧压成网格会牺牲空间细节，且更多重叠提高成本；细微物体或短动作需单测。

**可复用机制** · 当视觉模型更擅长空间注意力时，把局部时间顺序编码为图像排布，并保留全局时间锚。

<a id="paper-ovi-map"></a>

## OVI-MAP: Open-Vocabulary Instance-Semantic Mapping

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Deng_OVI-MAP_Open-Vocabulary_Instance-Semantic_Mapping_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Deng_OVI-MAP_Open-Vocabulary_Instance-Semantic_Mapping_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 对所有帧逐像素融合语言特征，算力开销大且跨视角语义容易波动。
- **核心创新 / 方法** · 从 RGB-D 维护增量实例图，仅对选择视图提取视觉语言特征。
- **Baseline** · 对照在线和离线开放词汇地图方法，覆盖点云及高斯表示。
- **Benchmark** · Replica、ScanNet 实例分割以及开放词汇语义映射与在线开销。
- **关键结果 / 消融** · 原文报告实时运行；表2比较两个数据集的实例分割。
- **适用条件 / 局限** · 依赖 RGB-D 对齐及类别无关跟踪质量，代表视图可能漏掉区分性线索。

**可复用机制** · 在线语义建图先更新类别无关实例，再从少量代表视图给实例添加语义。

<a id="paper-embedlens-visual-token-sparsity"></a>

## What Do Visual Tokens Really Encode? Uncovering Sparsity and Redundancy in Multimodal Large Language Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Fan_What_Do_Visual_Tokens_Really_Encode_Uncovering_Sparsity_and_Redundancy_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Fan_What_Do_Visual_Tokens_Really_Encode_Uncovering_Sparsity_and_Redundancy_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 视觉词元的显著性、内容信息和后续计算作用并不相同。
- **核心创新 / 方法** · 以 EmbedLens 分析输入词元语义，再对照裁剪、层解耦和中层注入。
- **Baseline** · 同模型随机移除等量词元、完整输入及推理计算对照。
- **Benchmark** · 视觉语义压缩测试及多模态理解任务，涵盖对象、颜色、OCR 和强视觉需求任务。
- **关键结果 / 消融** · 作者在所测配置中识别约60%图像特定词元，表2–3比较裁剪和跳层。
- **适用条件 / 局限** · 词元分组及深层需要随模型和任务不同，不能用固定比例剪所有样本。

**可复用机制** · 压缩视觉词元或跳层前，先用语义探针和随机等量裁剪定位真正承载实例信息的词元。

<a id="paper-simple-synthetic-video-controls"></a>

## Less is More: Data-Efficient Adaptation for Controllable Text-to-Video Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Cheng_Less_is_More_Data-Efficient_Adaptation_for_Controllable_Text-to-Video_Generation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Cheng_Less_is_More_Data-Efficient_Adaptation_for_Controllable_Text-to-Video_Generation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 真实控制样本难采，其他外观属性可能与目标条件纠缠。
- **核心创新 / 方法** · 在少量简单合成视频上微调新控制，再以解耦方式组合已学控制与原生成。
- **Baseline** · 原骨干、Full-LoRA 和解耦推理；正文对比合成和逼真训练源。
- **Benchmark** · 相机相关的三个控制设置，评估控制表现以及同原骨干的行为偏差。
- **关键结果 / 消融** · 作者报告低质量合成数据仍可学习控制，所测结果优于逼真数据路径。
- **适用条件 / 局限** · 需能合成足够明确且可分离的干预，复杂物体交互控制未必可这样分解。

**可复用机制** · 学习新视频物理控制时，先用因素独立的简单合成数据，对照逼真数据是否引入混杂。

<a id="paper-socratic-geo-failure-directed-synthesis"></a>

## Socratic-Geo: Synthetic Data Generation and Cross-Modal Geometric Reasoning via Multi-Agent Interaction

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Jiao_Socratic-Geo_Synthetic_Data_Generation_and_Cross-Modal_Geometric_Reasoning_via_Multi-Agent_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Jiao_Socratic-Geo_Synthetic_Data_Generation_and_Cross-Modal_Geometric_Reasoning_via_Multi-Agent_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 随机合成后筛选难针对当前模型薄弱点，也可能出现图文冲突。
- **核心创新 / 方法** · 生成器以结构化图形程序构造例题，用可解性和图文检查验收，求解器的失败用于调节后续采样。
- **Baseline** · 表1对照其他几何合成策略，表2测试对其他推理域的泛化。
- **Benchmark** · MathVerse、GeomVerse、GeoQA、MathVision、MathVista、WeMath 测 Mean@1，另用 GenExam-Math 测图形生成。
- **关键结果 / 消融** · 表1–3报告跨推理基准收益及严格、宽松生成分数。
- **适用条件 / 局限** · 依赖问题结构可验证，失败预测若含系统偏差会让数据反复集中于错误概念。

**可复用机制** · 训练几何推理时利用求解失败轨迹驱动可验证的合成数据补齐。

<a id="paper-drainage-class-uncertainty"></a>

## Drainage: A Unifying Framework for Addressing Class Uncertainty

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Taha_Drainage_A_Unifying_Framework_for_Addressing_Class_Uncertainty_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Taha_Drainage_A_Unifying_Framework_for_Addressing_Class_Uncertainty_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 封闭集合输出必须将全部概率分给既有类别，模糊样本会拉动边界。
- **核心创新 / 方法** · 加入 drainage 节点分流不确定样本的部分概率，以可微目标共同训练。
- **Baseline** · 和现有噪声标签方法比较人工噪声与真实噪声场景。
- **Benchmark** · CIFAR-10/100 的非对称及实例相关噪声，mini-WebVision、mini-ImageNet、Clothing-1M 分类。
- **关键结果 / 消融** · 作者在高噪声设定报告最高约10%的准确率改善。
- **适用条件 / 局限** · 拒判可能集中到稀有、困难但正确样本，使用时还需检查类别覆盖。

**可复用机制** · 噪声标签或类歧义明显时，给输出层预留可学习的拒判概率。

<a id="paper-cycle-consistent-cross-view-masks"></a>

## Learning Cross-View Object Correspondence via Cycle-Consistent Mask Prediction

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yan_Learning_Cross-View_Object_Correspondence_via_Cycle-Consistent_Mask_Prediction_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yan_Learning_Cross-View_Object_Correspondence_via_Cycle-Consistent_Mask_Prediction_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 第一和第三人称视觉差异大，直接匹配依赖跨视角标注。
- **核心创新 / 方法** · 以原对象掩码为条件预测目标视角掩码，再用预测掩码回到源视图重建。
- **Baseline** · 跨视角对应基线及不做测试时训练的对照。
- **Benchmark** · Ego-Exo4D 对应 v2 和 HANDAL-X，检查跨视角掩码重叠等指标。
- **关键结果 / 消融** · Ego-Exo4D 表1报告44.57% mIoU，原文给出2.9%相对提升。
- **适用条件 / 局限** · 循环一致不能排除两个视角同时错配类似物体，适配也带来时间成本。

**可复用机制** · 跨视角对象对应缺少标注时，用预测掩码回映原视角约束训练和测试时适配。

<a id="paper-flowsg-mixed-state-scene-graph-flow"></a>

## Can We Build Scene Graphs, Not Classify Them? FlowSG: Progressive Image-Conditioned Scene Graph Generation with Flow Matching

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Hu_Can_We_Build_Scene_Graphs_Not_Classify_Them_FlowSG_Progressive_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Hu_Can_We_Build_Scene_Graphs_Not_Classify_Them_FlowSG_Progressive_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 一次分类容易把边框、对象和关系当作相对独立的输出，关系的几何约束难以在预测过程中反复修正。
- **核心创新 / 方法** · 将场景图表示为连续边框与离散对象、关系标记。图 Transformer 预测速度场和离散后验，通过边与节点消息联合更新。
- **Baseline** · 与一步式场景图方法比较；消融流感知消息聚合、节点或边聚合及图像交叉注意力。
- **Benchmark** · Visual Genome 与 Panoptic Scene Graph 的闭集和开放词汇协议，以关系 R 和 mR 及图指标衡量。
- **关键结果 / 消融** · PSG 闭集表 4 的 R@50、mR@50 为 46.3、42.7，移除流感知聚合降到 40.5、37.1，移除跨注意力降到 39.2、34.3。
- **适用条件 / 局限** · 量化字典和关系长尾依赖训练数据，迭代采样的成本与不同候选初始化的长尾效果需单独衡量。

**可复用机制** · 如果输出含连续坐标和离散关系，可各自定义流更新，再用共享的节点与边消息协调两类变量。见表 4。

<a id="paper-sattc-frozen-retrieval-hubness-calibration"></a>

## SATTC: Structure-Aware Label-Free Test-Time Calibration for Cross-Subject EEG-to-Image Retrieval

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_SATTC_Structure-Aware_Label-Free_Test-Time_Calibration_for_Cross-Subject_EEG-to-Image_Retrieval_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_SATTC_Structure-Aware_Label-Free_Test-Time_Calibration_for_Cross-Subject_EEG-to-Image_Retrieval_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 跨被试 EEG 图像检索存在嵌入分布漂移，少数样本反复出现在短名单中。
- **核心创新 / 方法** · 冻结编码器后，在相似度矩阵融合被试自适应白化与局部相似度重标定，以及互近邻、双向排序和类别流行度证据。
- **Baseline** · 比较原始 ATM、标准预处理、固定和自适应 CSLS，另评估多个 EEG 编码器。
- **Benchmark** · THINGS-EEG 严格留一被试的 200 类候选检索，报告 Top-1、Top-5 和枢纽偏差。
- **关键结果 / 消融** · 表 1 标准化基线 Top-1 与 Top-5 为 9.2%、30.5%，完整方法为 14.8%、38.4%；仅使用自适应 CSLS 的 Top-5 为 38.8%。
- **适用条件 / 局限** · 需要无标注查询和候选提供稳定的邻域统计，候选池很小或类分布漂移时应重测。

**可复用机制** · 跨分布检索先建立归一化和候选白化基线，再用邻域结构重排，并分别核查 Top-1 与 Top-5。见表 1。

<a id="paper-latent-replay-angular-task-margin"></a>

## Lifelong Imitation Learning with Multimodal Latent Replay and Incremental Adjustment

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yu_Lifelong_Imitation_Learning_with_Multimodal_Latent_Replay_and_Incremental_Adjustment_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yu_Lifelong_Imitation_Learning_with_Multimodal_Latent_Replay_and_Incremental_Adjustment_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 连续学习机器人任务时，保存原始多模态轨迹成本高，任务适配还会不断改变过去表征。
- **核心创新 / 方法** · 回放视觉、语言和机器人状态的紧凑表示，并用角间隔调整相近任务的表示，维持可分性。
- **Baseline** · 与 LIBERO 持续模仿学习的回放与策略基线比较，直接对照只做潜空间回放与加表示约束。
- **Benchmark** · LIBERO-OBJECT、LIBERO-GOAL 和更长任务序列，以学习 AUC、前向迁移和负向后向迁移衡量。
- **关键结果 / 消融** · 表 1 中 LIBERO-GOAL 仅潜空间回放 AUC 为 74.6，加入任务表示调整后为 77.2，NBT 从 10.0 降到 6.9。
- **适用条件 / 局限** · 缓存需要与持续更新的编码器保持可用，任务边界、仿真序列或内存大小改变时应重查。

**可复用机制** · 顺序模仿学习可在有限回放内存下存多模态潜表示，再用角间隔约束任务表示更新并单测遗忘。见表 1、2。

<a id="paper-cci-concept-cluster-occlusion-diagnosis"></a>

## Concept Regions Matter: Benchmarking CLIP with a New Cluster-Importance Approach

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Agarwal_Concept_Regions_Matter_Benchmarking_CLIP_with_a_New_Cluster-Importance_Approach_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Agarwal_Concept_Regions_Matter_Benchmarking_CLIP_with_a_New_Cluster-Importance_Approach_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 整图准确率下降可能由背景、缩放、视角或细粒度物体混淆造成，单一准确率不能区分。
- **核心创新 / 方法** · 用 CLIP 的块级表示聚类，逐簇遮盖并测预测变化；配合前背景掩膜与可控前景和背景的 COVAR 数据。
- **Baseline** · 与 MaskCLIP、Grad-ECLIP、Grad-CAM 等重要性方法比较，另检查 18 个 CLIP 变体。
- **Benchmark** · ImageNet 与 MS COCO Karpathy 划分的解释忠实度用删除、插入曲线 AUC；COVAR 分析前景、背景及细粒度错误。
- **关键结果 / 消融** · 表 2 的 COCO 图像检索 R@1 删除 AUC 为 0.0650，Grad-ECLIP 为 0.1246；插入 AUC 分别为 0.1812 和 0.1576。
- **适用条件 / 局限** · 遮盖本身会改变输入分布，簇与掩膜的质量也会影响诊断，分数主要衡量受控扰动效果。

**可复用机制** · 诊断图文模型的背景依赖时，可以按特征簇做区域删除，并独立改变前景和背景以区分错误来源。见表 2–4。

<a id="paper-mioh-joint-versus-decomposed-visual-verification"></a>

## Fine-Grained Multi Image Object Hallucination Benchmark

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Min_Fine-Grained_Multi_Image_Object_Hallucination_Benchmark_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Min_Fine-Grained_Multi_Image_Object_Hallucination_Benchmark_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 单图或仅汇总得分的基准，无法区分单图识别失误与跨图整合错误。
- **核心创新 / 方法** · 控制图片内容不变，将存在判断改写成逐图判断，再聚合为与联合回答一致的全局目标，对照正确率。
- **Baseline** · 同一模型的全图联合回答与逐图回答后合并；总体对比 GPT-5、Gemini 2.5 Pro 等 29 个模型。
- **Benchmark** · MIOH 的存在、计数、属性和位置任务，涉及综合、比较、选择推理；图 5 的受控消融以存在判断的准确率衡量。
- **关键结果 / 消融** · 图 5 中逐图处理的存在判断准确率高于联合处理，作者据此把跨图整合作为可单独检验的失效环节。
- **适用条件 / 局限** · 存在判断可以用逻辑或合并，复杂比较和跨图对应不能直接沿用，另需计入多次调用成本。

**可复用机制** · 多图任务出现物体幻觉时，用完全相同图片对照联合回答与逐图作答后汇总，可检查错误是在感知还是跨图整合发生。见图 5。

<a id="paper-come-confidence-guided-geometric-token-merging"></a>

## Co-Me: Confidence Guided Token Merging for Visual Geometric Transformers

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Co-Me_Confidence_Guided_Token_Merging_for_Visual_Geometric_Transformers_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_Co-Me_Confidence_Guided_Token_Merging_for_Visual_Geometric_Transformers_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 多视图 Transformer 随输入帧数迅速变慢，按相似度合并可能丢掉几何上重要的空间信息。
- **核心创新 / 方法** · 蒸馏轻量的置信度预测器，用较低置信度的标记参与合并，保留高置信度信息。
- **Baseline** · 与原 VGGT、Pi3、ToMeSD 和 FastVGGT 对照，也报告其他几何骨干的变化。
- **Benchmark** · NYUd-v2、ETH3D、DTU-MVS、KITTI Depth 的尺度对齐深度误差、阈值准确率和毫秒时延，另测位姿、点云。
- **关键结果 / 消融** · 表 1 的 DTU-MVS 32 帧中 VGGT 时延 6094 毫秒、L1 0.89 厘米，Co-Me 为 788 毫秒、1.10 厘米；ToMeSD 为 1091 毫秒、0.93 厘米。
- **适用条件 / 局限** · 标记重叠度影响合并损失和速度，较少重叠场景与单图输入应按允许误差重新设定合并比例。

**可复用机制** · 多视角几何模型加速时，可按置信度选择合并对象，并随相机重叠程度报告耗时和深度误差。见表 1。

<a id="paper-stereoworld"></a>

## Stereo World Model: Camera-Guided Stereo Video Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Sun_Stereo_World_Model_Camera-Guided_Stereo_Video_Generation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Sun_Stereo_World_Model_Camera-Guided_Stereo_Video_Generation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 单目生成再转双目成本高，且视角差异难与运动同步。
- **核心创新 / 方法** · 建立相机与帧统一的 RoPE，并将完整四维注意力拆为视内三维注意力和跨视水平行注意力。
- **Baseline** · 表2比较 Voyager、DeepVerse、Aether、SEVA、ViewCrafter，表4–5消融相机注入和注意力。
- **Benchmark** · 表2评估 FID、FVD、相机误差、跨视同步和 FPS，表3给出 VBench 指标。
- **关键结果 / 消融** · 表2 StereoWorld 达0.49 FPS、跨视 FVD-V 22.00，对比 SEVA 的0.10 FPS、31.10。
- **适用条件 / 局限** · 水平行约束依赖双目极线可按行对齐，未校正相机或非双目设置需更换几何约束。

**可复用机制** · 双目生成可用极线结构节省跨视注意力，把相机姿态作为相对位置条件。

<a id="paper-motionenhancer"></a>

## MotionEnhancer: Leveraging Video Diffusion for Motion-Enhanced Vision-Language Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_MotionEnhancer_Leveraging_Video_Diffusion_for_Motion-Enhanced_Vision-Language_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_MotionEnhancer_Leveraging_Video_Diffusion_for_Motion-Enhanced_Vision-Language_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 视频 VLM 擅长事件语义，但容易遗漏局部运动。
- **核心创新 / 方法** · 从视频扩散模型挑选运动敏感头和运动显著文字 token，以注意力对齐提供辅助监督。
- **Baseline** · 表1–2对照同骨干未加 MotionEnhancer 的 Qwen2.5-VL 等，表3消融两个筛选模块。
- **Benchmark** · MotionBench 与 FAVOR-Bench，分别评估总体得分和多类动作理解。
- **关键结果 / 消融** · Qwen2.5-VL-3B 总体分数在两表分别由53.56升至56.60及37.43升至44.53，部分子项下降。
- **适用条件 / 局限** · 需要训练时访问可提供注意力的生成教师，视频中未采样到的短时动作仍难恢复。

**可复用机制** · 动作细节不足时，可用视频生成模型的运动注意力监督理解模型。

<a id="paper-orionedit"></a>

## OrionEdit: Bridging Reference and Source Images for Generalized Cross-Image Editing

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Jiang_OrionEdit_Bridging_Reference_and_Source_Images_for_Generalized_Cross-Image_Editing_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Jiang_OrionEdit_Bridging_Reference_and_Source_Images_for_Generalized_Cross-Image_Editing_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 跨图编辑时参考属性与源内容易混在一起，影响保真与控制。
- **核心创新 / 方法** · 对不同条件设置正交更新子空间，并用定向注意力遮罩约束潜变量依赖。
- **Baseline** · 基于扩散骨干，表1含 UNO 等；表2比较正交约束、随机遮罩、定向遮罩和更新秩。
- **Benchmark** · 表1三类任务为属性转移、风格对齐和融合，指标含 DPG、DINOv3、SigLip-I 等。
- **关键结果 / 消融** · 表2单加定向遮罩使 DPG 从53.81增至72.74，随机遮罩降至49.37。
- **适用条件 / 局限** · 依赖能区分条件角色的编辑训练；对互相冲突或更大量的参考条件需另测。

**可复用机制** · 参考图与源图各有不同职责时，可分别约束参数子空间和信息流向，并与随机遮罩对照。

<a id="paper-streaming-token-compression"></a>

## Accelerating Streaming Video Large Language Models via Hierarchical Token Compression

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Accelerating_Streaming_Video_Large_Language_Models_via_Hierarchical_Token_Compression_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_Accelerating_Streaming_Video_Large_Language_Models_via_Hierarchical_Token_Compression_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 流式视频相邻帧重复编码，视觉序列过长还会抬高 LLM 预填充成本。
- **核心创新 / 方法** · STC-Cacher 重用相似帧特征，STC-Pruner 结合空间与时间显著性筛选视觉 token。
- **Baseline** · 表1–3比较四个流式视频模型加入压缩前后的表现，表4–5改变复用特征和动态打分。
- **Benchmark** · OVO-Bench、StreamingBench、EgoSchema、MLVU-dev、VideoMME，另报视觉编码和预填充耗时。
- **关键结果 / 消融** · 表1分列编码与预填充耗时，表2–3检验压缩后的流式和离线答题得分。
- **适用条件 / 局限** · 运动突变或极短事件可能被误判冗余，应按事件密度验证复用阈值和裁剪比例。

**可复用机制** · 先测哪段延迟占主导，再分别压缩视觉编码重算和语言模型输入。

<a id="paper-g-mixer"></a>

## G-MIXER: Geodesic Mixup-based Implicit Semantic Expansion and Explicit Semantic Re-ranking for Zero-Shot Composed Image Retrieval

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Lim_G-MIXER_Geodesic_Mixup-based_Implicit_Semantic_Expansion_and_Explicit_Semantic_Re-ranking_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Lim_G-MIXER_Geodesic_Mixup-based_Implicit_Semantic_Expansion_and_Explicit_Semantic_Re-ranking_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 把参考图和修改指令压成单一生成文本描述时会丢掉含混的组合意图。
- **核心创新 / 方法** · 沿归一化嵌入间的测地路径用不同混合比构造查询，合并候选后用 MLLM 提取的显式语义重排。
- **Baseline** · 表1–3比较 SEARLE、CIReVL 等，表4消融语义扩张与重排。
- **Benchmark** · CIRCO、CIRR、FashionIQ 和 GeneCIS，按协议评估 mAP 与 Recall。
- **关键结果 / 消融** · 表1–3报告跨多个组合检索集合的表现，表4对候选扩张和重排作独立对照。
- **适用条件 / 局限** · 需要跨模态嵌入上的方向有可解释语义，候选规模与重排复杂度需按检索库重测。

**可复用机制** · 图文组合意图不唯一时，先用多个几何插值候选覆盖语义，再用显式语义排序。

<a id="paper-denserc"></a>

## Reconstructing CLIP for Open-Vocabulary Dense Perception

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_Reconstructing_CLIP_for_Open-Vocabulary_Dense_Perception_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_Reconstructing_CLIP_for_Open-Vocabulary_Dense_Perception_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 全局分类训练让 CLIP 的密集特征缺乏区域语义对齐。
- **核心创新 / 方法** · 从多层值嵌入构造密集特征，用选择性门控重加权不同注意力头，减少不当空间聚合。
- **Baseline** · 表1比较同 ViT-B/16 的 CLIPSelf 与 R-SC-CLIPSelf，另有检测及分割基线。
- **Benchmark** · 表1报告区域零样本分类 Top1/Top5；表2–4为开放词汇检测、跨数据集及语义分割。
- **关键结果 / 消融** · 表1无 RPN 时 thing mask Top1 为78.1，R-SC-CLIPSelf 为76.2；stuff mask 为55.8对53.5。
- **适用条件 / 局限** · 目前验证集中在 CLIP 类模型的静态图像，其他训练目标可能改变各层和值头的用途。

**可复用机制** · 重用 CLIP 做开放词汇定位时，先检查值嵌入与空间聚合，再决定是否改变注意力头权重。

<a id="paper-jointwise-motion-delta"></a>

## Cross-Axis Feature Fusion with Joint-Wise Motion Difference Prediction for Text-Based 3D Human Motion Editing

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Han_Cross-Axis_Feature_Fusion_with_Joint-Wise_Motion_Difference_Prediction_for_Text-Based_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Han_Cross-Axis_Feature_Fusion_with_Joint-Wise_Motion_Difference_Prediction_for_Text-Based_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 仅建模编辑发生的时间，难确定哪些关节该动。
- **核心创新 / 方法** · 用沿关节和时间轴的双 Transformer 融合特征，辅助回归配对源动作和目标动作关节旋转的 Soft-DTW 距离。
- **Baseline** · 表1比较 TMED 等，表2对照无辅助目标及 L2 距离，表3比较 Soft-DTW 平滑参数。
- **Benchmark** · MotionFix 的生成到目标动作检索 R@1/2/3、平均排名与 FID。
- **关键结果 / 消融** · 表1全测试集 R@1 29.45、批内74.38，FID 0.097；表2对照 L2 与 Soft-DTW。
- **适用条件 / 局限** · 训练需要成对骨架动作和旋转表示，机器人不同运动学约束下需重新定义部件及距离。

**可复用机制** · 局部动作编辑可用对齐后的部件变化量做辅助监督，保护未编辑关节。

<a id="paper-geco-geometry-consistent-regularization"></a>

## GeCo: Geometry-Consistent Regularization for Domain Generalized Semantic Segmentation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zang_GeCo_Geometry-Consistent_Regularization_for_Domain_Generalized_Semantic_Segmentation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zang_GeCo_Geometry-Consistent_Regularization_for_Domain_Generalized_Semantic_Segmentation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 随机扰动可缓解适配器过拟合，但会改变预训练流形上的语义邻域。
- **核心创新 / 方法** · 以预训练特征的局部几何选扰动强度，再用测地约束保持适配前后的关系。
- **Baseline** · 表1比较可训参数与适配方法，表2–3比较领域泛化分割方案。
- **Benchmark** · 源域训练与未见目标域语义分割，比较 mIoU 等分割表现与参数量。
- **关键结果 / 消融** · 文中报告多目标域的改善并比较几何约束与扰动的配置。
- **适用条件 / 局限** · 局部曲率和测地距离须有效近似；预训练流形存在偏差时保留结构可能保留偏差。

**可复用机制** · 对基础特征作域泛化微调时，用局部曲率控制扰动、用测地关系保持结构。

<a id="paper-gen3r-aligned-geometry-latents"></a>

## Gen3R: 3D Scene Generation Meets Feed-Forward Reconstruction

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_Gen3R_3D_Scene_Generation_Meets_Feed-Forward_Reconstruction_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_Gen3R_3D_Scene_Generation_Meets_Feed-Forward_Reconstruction_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 视频生成缺少显式可用几何，独立重建在遮挡和稀疏观察下容易不完整。
- **核心创新 / 方法** · 将 VGGT 词元适配为几何潜变量，匹配预训练视频潜空间的结构并联合生成视频、深度和点图。
- **Baseline** · 表1–2与生成方案比较，表3含 WVD 的 RGB VAE 对照。
- **Benchmark** · 单图与双图条件的场景生成，分别评价外观及几何提取，另测重建。
- **关键结果 / 消融** · 表1–3报告两类输出及重建改善。
- **适用条件 / 局限** · 不可见内容仍是生成推断，几何和外观联合一致不能保证是真实场景。

**可复用机制** · 生成动态视图又需要可查询几何时，学习对齐的外观及几何潜变量，并在同一轨迹联合采样。

<a id="paper-hierarchical-prompts-positive-transfer"></a>

## Unlocking Positive Transfer in Incrementally Learning Surgical Instruments: A Self-reflection Hierarchical Prompt Framework

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhu_Unlocking_Positive_Transfer_in_Incrementally_Learning_Surgical_Instruments_A_Self-reflection_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhu_Unlocking_Positive_Transfer_in_Incrementally_Learning_Surgical_Instruments_A_Self-reflection_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 只抑制遗忘会漏掉旧部件对新类别的帮助，及新类别对已有类别的修正。
- **核心创新 / 方法** · 冻结骨干，以根节点共享提示、中间共享部件和叶提示组织新增类别，并用反思机制更新。
- **Baseline** · 表1–2比较类增量分割方法，表3消融提示组织和更新。
- **Benchmark** · 机器人辅助肾切除及腹腔镜胆囊切除的器械视频分割，报告最终轮及跨轮 IoU。
- **关键结果 / 消融** · 原文报告新旧器械分割改善，表3用于区分组件。
- **适用条件 / 局限** · 需存在有意义的类间共享结构；提示树错配可能造成负迁移。

**可复用机制** · 增量类别有共享部件时，按类别及部件搭建提示树，用前向和反向迁移指标检查新增知识。

<a id="paper-avggt-global-attention"></a>

## AVGGT: Rethinking Global Attention for Accelerating VGGT

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Sun_AVGGT_Rethinking_Global_Attention_for_Accelerating_VGGT_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Sun_AVGGT_Rethinking_Global_Attention_for_Accelerating_VGGT_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 直接统一压缩全局注意力可能破坏关键视图对应。
- **核心创新 / 方法** · 根据诊断区分早层、对齐中层和末层；替换早层注意力，其余进行保对角键值子采样和均值补充。
- **Baseline** · 原 VGGT、π3 等及稀疏注意力版本。
- **Benchmark** · RealEstate10K、TUM-dynamics 相机姿态与 DTU 点图，并比较100至800帧开销。
- **关键结果 / 消融** · 作者报告100帧约2倍、300帧约4–5倍、800帧约8–10倍加速。
- **适用条件 / 局限** · 层作用分布依赖骨干和输入，快速变动视点可能更加依赖全局信息。

**可复用机制** · 多视图模型加速时先测各层跨视图作用，再将早层改为逐帧并对其余全局键值采样。

<a id="paper-rar-latent-restoration-assessment"></a>

## Restore, Assess, Repeat: A Unified Framework for Iterative Image Restoration

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Restore_Assess_Repeat_A_Unified_Framework_for_Iterative_Image_Restoration_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_Restore_Assess_Repeat_A_Unified_Framework_for_Iterative_Image_Restoration_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 单轮方法难处理未知或组合退化，分立质量评估会增加时延及转码损失。
- **核心创新 / 方法** · 在共享潜空间内统一恢复、退化判别和质量验证，按质量动态继续。
- **Baseline** · 表1–3对照单退化及统一恢复方案。
- **Benchmark** · 组合退化、UDC 未知退化和多类单退化，比较恢复表现。
- **关键结果 / 消融** · 论文分别报告三种退化情形的改善。
- **适用条件 / 局限** · 停止与操作决策依赖内置质量代理，域外错误评价可能导致过度迭代。

**可复用机制** · 多步图像恢复时在潜空间内同时判断退化和复核质量，减少反复解码。

<a id="paper-timebridge"></a>

## TimeBridge: Self-Supervised Video Representation Learning via Start-End Joint Embedding and In-Between Frame Prediction

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_TimeBridge_Self-Supervised_Video_Representation_Learning_via_Start-End_Joint_Embedding_and_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_TimeBridge_Self-Supervised_Video_Representation_Learning_via_Start-End_Joint_Embedding_and_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 纯帧间对齐容易忽略变化，单端未来预测又有歧义。
- **核心创新 / 方法** · 交叉拼接起止帧的类词元，由轻量解码器重建中间帧，联合学习时间变换。
- **Baseline** · 对照2D预训练、视频嵌入和既有视频表示学习方案。
- **Benchmark** · DAVIS 2017 目标分割 J&F、VIP 部件传播 mIoU，并做分类线性探测。
- **关键结果 / 消融** · 摘要报告 DAVIS 73.5 J&F、VIP 47.5 mIoU。
- **适用条件 / 局限** · 端点可能不足以唯一解释动作，中间帧恢复代理可能偏向像素可预测内容。

**可复用机制** · 自监督视频学习时同时对齐起止帧表示，并要求从两端恢复中间帧。

<a id="paper-vital-difficulty-balanced-multitask-grpo"></a>

## Thinking With Videos: Multimodal Tool-Augmented Reinforcement Learning for Long Video Reasoning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Thinking_With_Videos_Multimodal_Tool-Augmented_Reinforcement_Learning_for_Long_Video_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Thinking_With_Videos_Multimodal_Tool-Augmented_Reinforcement_Learning_for_Long_Video_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 长视频定位的 IoU 奖励增长慢，选择题奖励增长快，混合训练可能偏向容易优化的目标。
- **核心创新 / 方法** · DGRPO 根据任务难度与样本难度调节奖励尺度；整套方法随后加入按需重新观察视频的工具策略。
- **Baseline** · 表 5 在有文本推理的相同阶段比较 SFT 加 GRPO 与 SFT 加 DGRPO，并另列加入工具训练。
- **Benchmark** · 长视频问答、通用多模态问答与时间定位等任务，报告准确率和 mIoU。
- **关键结果 / 消融** · 表 5 在加入工具训练之前，DGRPO 使四项平均分从 50.3 增至 52.1；LVR 为 66.0 到 70.2，Cha mIoU 由 57.2 略降至 57.1。
- **适用条件 / 局限** · 难度估计依赖训练奖励的可解释性和覆盖面，不能把随后加入工具的额外收益归给奖励重标定。

**可复用机制** · 联合优化问答正确率与时间定位时，可先比较普通 GRPO 和任务、样本难度加权，核对不同奖励量尺上的表现。见表 5。

<a id="paper-wfs-semantic-boundary-wavelet-selection"></a>

## Wavelet-based Frame Selection by Detecting Semantic Boundary for Long Video Understanding

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Wavelet-based_Frame_Selection_by_Detecting_Semantic_Boundary_for_Long_Video_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_Wavelet-based_Frame_Selection_by_Detecting_Semantic_Boundary_for_Long_Video_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 依据帧与问题的瞬时相似度取高分帧会过度集中在少数片段，并漏掉叙事转折。
- **核心创新 / 方法** · 对问题与各帧的相似度信号作小波分解，从粗尺度定位语义变化，再分配各片段的选帧预算。
- **Baseline** · 同一模型对照均匀采样、不做小波时的原始局部极小值与梯度、固定预算和直接取 Top-K。
- **Benchmark** · Qwen2.5-VL-7B 在 VideoMME 和 MLVU 的 16 帧预算，报告问答准确率。
- **关键结果 / 消融** · 表 4 完整方法为 61.9%、67.9%，改用原始梯度为 61.2%、66.8%，均匀采样为 57.7%、56.2%。
- **适用条件 / 局限** · 短促事件可能被粗尺度信号平滑，任务若要求找瞬时细节，应另测召回率。

**可复用机制** · 按查询压缩视频时，可先在相关性序列里找低频语义变化，再在段内选帧，比较直接用原始分数找边界。见表 4。

<a id="paper-codev-evidence-based-visual-tool-reward"></a>

## CodeV: Code with Images for Faithful Visual Reasoning via Tool-Aware Policy Optimization

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Hou_CodeV_Code_with_Images_for_Faithful_Visual_Reasoning_via_Tool-Aware_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Hou_CodeV_Code_with_Images_for_Faithful_Visual_Reasoning_via_Tool-Aware_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 答案正确时，模型仍可能做无关裁剪甚至完全没有利用工具。
- **核心创新 / 方法** · 根据问题和视觉操作结果给出步骤奖励，提高有证据支持的工具调用，并保留最终正确性监督。
- **Baseline** · 对照只奖励答案、回答一致性、评判模型，以及 Pixel-Reasoner、DeepEyes、Thyme 等基线。
- **Benchmark** · V* 和 HRBench-4K 评估忠实、非忠实和无工具使用，另报告推理和感知任务均值。
- **关键结果 / 消融** · 表 2 中只奖准确率的推理、感知均值为 51.2、67.5，完整模型为 54.2、69.7；图 5 的忠实使用提高约 1.3–2 倍。
- **适用条件 / 局限** · 可见证据与答案相关不等价于证明模型依赖该证据；迁移需能检查工具返回内容。

**可复用机制** · 视觉工具智能体可把奖励落在工具输出是否包含问题证据，并把忠实调用率与答案准确率分开报告。见图 5、表 2。

<a id="paper-neural-differentiation-loss-aware-pruning"></a>

## Neural Differentiation in Deep Networks: A Theoretical Framework for Expressivity and Representational Diversity

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Neural_Differentiation_in_Deep_Networks_A_Theoretical_Framework_for_Expressivity_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_Neural_Differentiation_in_Deep_Networks_A_Theoretical_Framework_for_Expressivity_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 按权重幅度或单一敏感度剪枝可能误删承担互补表示的单元。
- **核心创新 / 方法** · 用神经分化指数衡量环境中的单元差异与损失代价，将几何、信息及曲率信号用于训练期结构化裁剪，再进行针对性微调。
- **Baseline** · 与 CroPit-S、EarlyCroP-S、EarlySNAP、SNAP 等早期稀疏化方法比较。
- **Benchmark** · CIFAR-10 ResNet-18 和其他分类架构，以权重稀疏度、准确率及计算指标评估。
- **关键结果 / 消融** · 表 2 在 95% 稀疏度时 NDP 准确率为 92.56%，EarlyCroP-S 为 91.31%；98% 时为 90.03%、88.57%。
- **适用条件 / 局限** · 误差界受正文假设约束，权重稀疏率不能直接换算成特定硬件或端到端延迟。

**可复用机制** · 结构化剪枝可以基于损失与表征差异估计删除代价，同时检查给定稀疏度的准确率和实际吞吐。见理论章节与表 2。

<a id="paper-star-r1-referent-selection-rewards"></a>

## STAR-R1: Multi-View Spatial TrAnsformation Reasoning by Reinforcing Multimodal LLMs

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_STAR-R1_Multi-View_Spatial_TrAnsformation_Reasoning_by_Reinforcing_Multimodal_LLMs_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_STAR-R1_Multi-View_Spatial_TrAnsformation_Reasoning_by_Reinforcing_Multimodal_LLMs_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 模型从多个视角理解变换时，常先认错对应物体再产生结论，只有答案的奖励难定位这一失败。
- **核心创新 / 方法** · 用结构化空间推理轨迹做监督热启动，再以物体选择、属性等细粒度监督和最终正确性共同优化。
- **Baseline** · 对照朴素 GRPO、逐项去掉物体和属性奖励等策略。
- **Benchmark** · TVR 多视角空间变换的整体准确率、对象准确率和按难度分组得分，另用 MMSI-Bench、MindCube-Tiny、SPAR-Bench 评估。
- **关键结果 / 消融** · 表 3 完整方法 TAcc 为 61.4%，去掉对象项为 58.0%，普通 GRPO 为 54.5%；最难组分别为 37.5%、34.6%、31.1%。
- **适用条件 / 局限** · 训练依赖物体与属性可以可靠标注，开放词汇、遮挡或难对应场景下的奖励质量需单独检查。

**可复用机制** · 训练多视角推理时，可分别奖励指代物体选择和最终答案，避免仅靠答案奖励时对齐错误。见表 3。

<a id="paper-shapear"></a>

## ShapeAR: Generating Editable Shape Layers via Autoregressive Diffusion

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Chakraborty_ShapeAR_Generating_Editable_Shape_Layers_via_Autoregressive_Diffusion_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Chakraborty_ShapeAR_Generating_Editable_Shape_Layers_via_Autoregressive_Diffusion_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 边界追踪或联合优化会留下破碎的路径，遮挡时难保留可编辑层。
- **核心创新 / 方法** · 用 flow matching 逐步生成 RGBA 形状层，每步同时看全图和已生成层的部分合成。
- **Baseline** · 表2比较 Adobe Illustrator，表3比较不同矢量化方法，表1改变层数。
- **Benchmark** · 评估重建 L1、冗余和混合损失，并报告形状几何质量。
- **关键结果 / 消融** · 表3三项指标为0.005、0.020、0.014，图6展示遮挡情形下形状完整性。
- **适用条件 / 局限** · 目前面向图形形状分解，照片中透明材质与不可唯一分解的重叠区域需复验。

**可复用机制** · 把难以一次求解的可编辑分解改写为依赖当前合成画布的逐层生成。

<a id="paper-l3dr"></a>

## L3DR: 3D-aware LiDAR Diffusion and Rectification

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_L3DR_3D-aware_LiDAR_Diffusion_and_Rectification_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_L3DR_3D-aware_LiDAR_Diffusion_and_Rectification_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 二维范围视图的 LiDAR 扩散可能产生深度泄漏和弯曲表面。
- **核心创新 / 方法** · 以三维残差网络预测逐点偏移，使用 Welsch 损失减弱异常区域对纠正训练的影响。
- **Baseline** · 表1直接比较 R2DM、LiDM 与加纠正网络后的变体，表3比较骨干和损失。
- **Benchmark** · KITTI360 无条件生成及 nuScenes、Waymo 等语义条件生成，表4报告开销。
- **关键结果 / 消融** · 表1在多个骨干和数据集上给出校正对照，表3单测损失，表4量化额外计算。
- **适用条件 / 局限** · 仍有赖二维生成器提供合理初始点云；语义条件实验纠正阶段还会输入分割图。

**可复用机制** · 快速生成保留二维范围视图，纠正边缘与表面伪影时再回到三维空间。

<a id="paper-bpfedctta"></a>

## Towards Stable Federated Continual Test-Time Adaptation in Wild World

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Towards_Stable_Federated_Continual_Test-Time_Adaptation_in_Wild_World_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_Towards_Stable_Federated_Continual_Test-Time_Adaptation_in_Wild_World_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 客户端依次出现时，持续接受单个域更新容易让共享模型被带偏。
- **核心创新 / 方法** · 用共享模型作为本地后验估计的先验，再以不确定性门控决定单客户端更新是否聚合。
- **Baseline** · 表1–3比较源模型与联邦、个性化及测试时适应方法，表4消融更新组件，表5比较不确定性估计。
- **Benchmark** · CIFAR10-C、CIFAR100-C 准确率，Cityscapes 到 ACDC 的 mIoU，眼底及前列腺 MRI 分割 Dice。
- **关键结果 / 消融** · 表1平均准确率分别为68.44%和67.58%，表4比较两个组件同时使用与单独使用。
- **适用条件 / 局限** · 依赖不确定性能够预示更新质量，连续强漂移或新域与既有域置信度不可比时需检查门控误判。

**可复用机制** · 把无标签局部自适应与是否写回共享模型分成两个决策。

<a id="paper-iqpir"></a>

## Beyond Ground-Truth: Leveraging Image Quality Priors for Real-World Image Restoration

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_Beyond_Ground-Truth_Leveraging_Image_Quality_Priors_for_Real-World_Image_Restoration_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xiao_Beyond_Ground-Truth_Leveraging_Image_Quality_Priors_for_Real-World_Image_Restoration_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 把所有配对真值作为同质量监督会让恢复模型学到训练集平均质量。
- **核心创新 / 方法** · 用无参考图像质量评分条件化恢复网络，并用双分支码本区分共有特征与高质量特征。
- **Baseline** · 表1–4比较各恢复任务方法，表5分解质量条件与码本等组件，表6做人评。
- **Benchmark** · 盲人脸恢复、低照度、水下、逆光增强；表1含 TOPIQ、MUSIQ、CLIP-IQA 等。
- **关键结果 / 消融** · 表5提供组件对照，表6在人脸恢复与低照度上补充人评。
- **适用条件 / 局限** · 质量教师的分数可能奖励锐化或改变真实细节，感知质量与观测保真需分别评价。

**可复用机制** · 当配对标签质量参差不齐时，用显式质量条件保留不同等级的数据，推理选择目标质量。

<a id="paper-minddriver"></a>

## MindDriver: Introducing Progressive Multimodal Reasoning for Autonomous Driving

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_MindDriver_Introducing_Progressive_Multimodal_Reasoning_for_Autonomous_Driving_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_MindDriver_Introducing_Progressive_Multimodal_Reasoning_for_Autonomous_Driving_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 文本推理与轨迹坐标存在表示落差，通用未来帧可能忽略规划相关场景变化。
- **核心创新 / 方法** · 先做语义理解，再生成规划相关的未来画面，最后输出轨迹；训练用反馈筛选多模态数据，并分阶段施加奖励。
- **Baseline** · Qwen2.5-VL-3B 骨干，表1比较 UniAD、VAD 等，表4–7对照推理结构、未来帧、数据过滤与渐进奖励。
- **Benchmark** · nuScenes 开环 L2 误差与碰撞率、未来帧质量，Bench2Drive/CARLA 闭环。
- **关键结果 / 消融** · 表1报告开环结果，表3验证闭环，表4–7拆解中间态及训练组件贡献。
- **适用条件 / 局限** · 闭环证据来自仿真，预测画面错误可能传给规划头，真实道路和其他控制域需另测。

**可复用机制** · 需把语义推理转成动作时，可尝试预测与决策直接相关的物理中间态，并对各阶段分开消融。

<a id="paper-htc-vlm"></a>

## Hybrid Token Compression for Vision-Language Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Hybrid_Token_Compression_for_Vision-Language_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Hybrid_Token_Compression_for_Vision-Language_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 单用连续压缩可能淡化对象身份，纯量化可能损失纹理。
- **核心创新 / 方法** · 拼接 ViT 连续 patch 和四个 MGVQ 离散锚点，利用解耦注意力遮罩和 voco 瓶颈聚合为单 token。
- **Baseline** · 表1比较之前的视觉压缩方法和连续基线，表2改变 token 预算，表3–4探测语义与消融配置。
- **Benchmark** · GQA、VQAv2、MMBench、MME、POPE、SEED-Bench、ScienceQA-Image，采用相对上下界归一化的保留率。
- **关键结果 / 消融** · 单 token 平均保留率87.2%，领先连续基线为81.0%；表3检查离散与连续表征。
- **适用条件 / 局限** · 保留率随所选上下界改变，细粒度空间定位和流式视频输入需另测。

**可复用机制** · 极端视觉 token 压缩时为可辨对象保留离散语义锚点，并留连续通道承载细节。

<a id="paper-tcl-long-tail"></a>

## Trust-calibrated Collaborative Learning for Long-Tailed Visual Recognition

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhou_Trust-calibrated_Collaborative_Learning_for_Long-Tailed_Visual_Recognition_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhou_Trust-calibrated_Collaborative_Learning_for_Long-Tailed_Visual_Recognition_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 多专家相互蒸馏会传播单个专家偏差，错误一致时还会强化误判。
- **核心创新 / 方法** · 以知识质量门控选择可传递监督，尾类单独补偿，再压低专家一致高置信的负类。
- **Baseline** · 表1含重现的既有长尾专家方法，表4–5消融质量门控与共识校准。
- **Benchmark** · CIFAR10/100-LT、ImageNet-LT、Places-LT、iNaturalist 2018 的 Top-1，另比较头中尾类别。
- **关键结果 / 消融** · 表1 CIFAR100-LT 不平衡率100时 Top-1 58.7%，尾类38.3%；表2–3给多个数据集对照。
- **适用条件 / 局限** · 依赖专家保有互补性及训练标签能辨别错误共识，领域漂移或标签噪声下需复验。

**可复用机制** · 互蒸馏时应筛掉专家的错误共识，并对尾类单独补偿监督。

<a id="paper-imod-modality-decomposition"></a>

## Parameter-Efficient Adaptation for MLLMs via Implicit Modality Decomposition

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Parameter-Efficient_Adaptation_for_MLLMs_via_Implicit_Modality_Decomposition_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Parameter-Efficient_Adaptation_for_MLLMs_via_Implicit_Modality_Decomposition_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 混合监督时文本梯度占优，视觉或音频适配不足。
- **核心创新 / 方法** · 将可训练增量拆为三类并施加模态特定解耦与共享对齐约束。
- **Baseline** · 对照普通 LoRA 与表1–3列出的多模态参数高效微调方案。
- **Benchmark** · 覆盖音视文本、图文、语音等设置，并比较任务分数与适配矩阵数量。
- **关键结果 / 消融** · 表1–3报告多模态任务上的改善，验证分解比一体化更新更有利。
- **适用条件 / 局限** · 模态特定和共享因素难完全分开，配比和参数分组会影响迁移。

**可复用机制** · 多模态 LoRA 中将文本、非文本和共享更新分开，并约束干扰与对齐。

<a id="paper-nadb-noise-aligned-bridge"></a>

## Resolving Endpoint Underfitting in Diffusion Bridges via Noise Alignment

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Gao_Resolving_Endpoint_Underfitting_in_Diffusion_Bridges_via_Noise_Alignment_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Gao_Resolving_Endpoint_Underfitting_in_Diffusion_Bridges_via_Noise_Alignment_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 标准扩散目标直接移植到扩散桥后，接近干净终点出现预测方差和方向偏差。
- **核心创新 / 方法** · 先用均值网络得到较干净条件目标，再建立噪声对齐的桥映射。
- **Baseline** · I2SB、标准扩散模型与其他图像翻译扩散桥。
- **Benchmark** · 多种图像修复及翻译；表2以100次函数求值比较。
- **关键结果 / 消融** · 表1–3报告多任务恢复或翻译收益，正文诊断终点处欠拟合。
- **适用条件 / 局限** · 要求均值预测有用；不同端点、随机过程和少步求解设置需核验。

**可复用机制** · 扩散桥终点附近欠拟合时，先核对输入和回归目标的噪声尺度，再修正监督。

<a id="paper-faithfusion-information-gain"></a>

## FaithFusion: Harmonizing Reconstruction and Generation via Pixel-wise Information Gain

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_FaithFusion_Harmonizing_Reconstruction_and_Generation_via_Pixel-wise_Information_Gain_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_FaithFusion_Harmonizing_Reconstruction_and_Generation_via_Pixel-wise_Information_Gain_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 扩散模型大范围恢复可能损坏已有可靠几何，逐像素信任机制缺失。
- **核心创新 / 方法** · 以预期信息增益约束空间编辑，并以该权重更新高斯表示。
- **Baseline** · 对照三维高斯和扩散融合方案，表2逐项消融增益策略。
- **Benchmark** · Waymo 上不同车道偏移，报告 NTA-IoU、NTL-IoU 和 FID。
- **关键结果 / 消融** · 作者报告6米偏移下 FID 107.47，表2检验组件。
- **适用条件 / 局限** · 信息增益代理若错误标记遮挡或噪声，仍可能将虚假生成内容写回地图。

**可复用机制** · 混合重建与生成时，以同一个像素级信息增益分数选择修补位置，以及控制编辑蒸馏回三维模型的权重。

<a id="paper-pointer-cad"></a>

## Pointer-CAD: Unifying B-Rep and Command Sequences via Pointer-based Edges & Faces Selection

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Qi_Pointer-CAD_Unifying_B-Rep_and_Command_Sequences_via_Pointer-based_Edges__CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Qi_Pointer-CAD_Unifying_B-Rep_and_Command_Sequences_via_Pointer-based_Edges__CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 纯命令序列不能方便表示选择某一边或面，离散几何还会造成错误。
- **核心创新 / 方法** · 根据已有 B-rep 实体特征预测指针，生成一步命令后再用更新后的状态作为下一步条件。
- **Baseline** · 与普通 CAD 命令序列及其他表示比较。
- **Benchmark** · 评测 CAD 生成、几何实体选择与表示覆盖，表1比较表示差异。
- **关键结果 / 消融** · 原文展示指针可表达依赖面和边选择的命令。
- **适用条件 / 局限** · 依赖有效的结构执行器和实体特征；中间操作失败会影响后续指针集合。

**可复用机制** · 让序列模型输出操作时，用指针选择当前结构中的实体，避免把动态对象列表硬编码到词表。

<a id="paper-varsplat-uncertainty"></a>

## VarSplat: Uncertainty-aware 3D Gaussian Splatting for Robust RGB-D SLAM

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Tran_VarSplat_Uncertainty-aware_3D_Gaussian_Splatting_for_Robust_RGB-D_SLAM_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Tran_VarSplat_Uncertainty-aware_3D_Gaussian_Splatting_for_Robust_RGB-D_SLAM_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 隐式可靠性在低纹理、透明和复杂反射区容易让位姿漂移。
- **核心创新 / 方法** · 通过全方差公式与 alpha 合成渲染每像素不确定度，传给追踪、子图配准和回环。
- **Baseline** · 对照现有 RGB-D SLAM 及原文方差引导配置。
- **Benchmark** · Replica、TUM-RGBD、ScanNet、ScanNet++，评估 ATE RMSE、建图及重渲染。
- **关键结果 / 消融** · 原文报告合成及真实数据追踪和建图表现，表1、3给出轨迹误差。
- **适用条件 / 局限** · 外观方差只是观测可靠性的代理；错误置信会削弱有用点，深度质量仍制约结果。

**可复用机制** · 高斯 SLAM 中学习逐图元方差，并用与渲染一致的像素不确定度为追踪和回环定权。

<a id="paper-streamdit-moving-buffer"></a>

## StreamDiT: Real-Time Streaming Text-to-Video Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Kodaira_StreamDiT_Real-Time_Streaming_Text-to-Video_Generation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Kodaira_StreamDiT_Real-Time_Streaming_Text-to-Video_Generation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 离线整段扩散不能边出帧边保有长历史一致性。
- **核心创新 / 方法** · 在流匹配训练中引入逐步去噪缓冲区和混合分区，用分段少步蒸馏实现流式推理。
- **Baseline** · 表2比较视频生成方法，表3比较固定与混合分区。
- **Benchmark** · 512p 文生视频；VBench、人评、FPS 与函数评估次数。
- **关键结果 / 消融** · 作者报告4B模型单卡达到512p 16 FPS，蒸馏后评估次数降至缓冲区块数。
- **适用条件 / 局限** · 延迟、内容连贯性及内存依赖缓冲长度和分区，实时数字随硬件变化。

**可复用机制** · 流式视频生成用移动缓冲区维护多噪声级片段，再按片段蒸馏减少函数评估。

<a id="paper-guideflow-constraints-inside-trajectory-generation"></a>

## GuideFlow: Constraint-Guided Flow Matching for Planning in End-to-End Autonomous Driving

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_GuideFlow_Constraint-Guided_Flow_Matching_for_Planning_in_End-to-End_Autonomous_Driving_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_GuideFlow_Constraint-Guided_Flow_Matching_for_Planning_in_End-to-End_Autonomous_Driving_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 轨迹生成可能产生多样但不合约束的路径，统一靠后处理会延迟发现不可行轨迹。
- **核心创新 / 方法** · 在流匹配中显式引入状态和速度场约束，联训能量模型用于继续修正候选轨迹。
- **Baseline** · 与 DiffusionDrive 等端到端规划器比较，并在同架构中移除约束和能量校正。
- **Benchmark** · NavSim 难例、Bench2Drive、nuScenes、ADV-nuScenes，报告 EPDMS、驾驶分、成功率、进度与碰撞率。
- **关键结果 / 消融** · 表 5 无新增模块的 EPDMS 为 23.1，双模块配置可达 27.1，同一行的进度分由 84.1 降至 79.6。
- **适用条件 / 局限** · 约束含有特定场景、车辆状态与测试设定，驾驶仿真分数不足以推定其他环境的安全性。

**可复用机制** · 可在候选轨迹生成期间约束状态和速度场，并将进度与约束指标分开比较。见表 5。

<a id="paper-adv-grpo-reference-updated-image-reward"></a>

## The Image as Its Own Reward: Reinforcement Learning with Adversarial Reward for Image Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Mao_The_Image_as_Its_Own_Reward_Reinforcement_Learning_with_Adversarial_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Mao_The_Image_as_Its_Own_Reward_Reinforcement_Learning_with_Adversarial_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 图像生成优化固定 OCR 或偏好奖励时，高代理分可能伴随视觉质量降低。
- **核心创新 / 方法** · 将参考图像作为正样本，把生成图像用于更新判别式奖励，并与待优化生成器迭代联训。
- **Baseline** · 比较 SD3 原模型和仅优化固定奖励的 Flow-GRPO。
- **Benchmark** · 分别使用 PickScore、OCR 准确率、DINO 相似度与专家成对比较衡量目标分和感知保真。
- **关键结果 / 消融** · 表 1 的 Adv-GRPO 与 Flow-GRPO 都达到 0.91 OCR 准确率，PickScore 分别为 22.78、22.82，作者另用专家比较识别同分时的质量差异。
- **适用条件 / 局限** · 动态判别奖励由参考图像分布决定，参考覆盖不足可能导致偏好偏移，也增加训练成本。

**可复用机制** · 固定偏好分数引发图像质量失真时，可比较加入由真实参照图与当前产物持续更新的奖励，并做独立人评。见表 1 和第 4.3 节。

<a id="paper-pda-phasewise-open-vocabulary-action-alignment"></a>

## Decompose and Transfer: CoT-Prompting Enhanced Alignment for Open-Vocabulary Temporal Action Detection

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhu_Decompose_and_Transfer_CoT-Prompting_Enhanced_Alignment_for_Open-Vocabulary_Temporal_Action_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhu_Decompose_and_Transfer_CoT-Prompting_Enhanced_Alignment_for_Open-Vocabulary_Temporal_Action_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 全局动作描述常略过前后阶段，未见动作难借用已见动作共有的时序线索。
- **核心创新 / 方法** · 用语言模型产生连贯的阶段描述，分别选择匹配的视频前景并汇聚阶段级图文相似度。
- **Baseline** · 对照仅全局描述、不同阶段数及 Ti-FAD 等开放词汇检测方法。
- **Benchmark** · THUMOS14、ActivityNet v1.3 的已见至未见类检测，以不同 tIoU 阈值的 mAP 和时间衡量。
- **关键结果 / 消融** · 表 3 的 THUMOS14 半数未见类设置中，全局描述平均 mAP 42.5、用时 27.6 秒；三阶段 45.3、30.5 秒；六个描述 47.8、37.3 秒。
- **适用条件 / 局限** · 动作需能拆为可辨识阶段，对于重复、任意顺序和极短动作要重新检查阶段划分。

**可复用机制** · 对未见动作做时间定位时，可以把类级标签拆为阶段，再用阶段数消融去确定效果与开销。见表 3。

<a id="paper-edfilter-inter-event-probability-flux"></a>

## Event Stream Filtering via Probability Flux Estimation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Event_Stream_Filtering_via_Probability_Flux_Estimation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_Event_Stream_Filtering_via_Probability_Flux_Estimation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 离散事件的去噪常直接删事件，忽略间隔里包含的连续亮度变化信息。
- **核心创新 / 方法** · 以辐照度随机过程的过阈概率通量描述事件生成，用核估计与递推恢复连续的事件密度。
- **Baseline** · 与原始事件、EventZoom、EvFlow、MLPF、Ynoise 比较。
- **Benchmark** · RED 受控序列与两种相机的辐照度 NMSE，另评估 E-MLB、估计延迟和吞吐。
- **关键结果 / 消融** · 表 1 的 EVK 文本序列 NMSE 为 0.038，原始事件为 0.052，MLPF 为 0.049；在 DVS 的 Kanizsa 模式上弱于原始事件。
- **适用条件 / 局限** · 建立于阈值触发机制与受控参考，换传感器、光照噪声模型或非阈值事件后应重验。

**可复用机制** · 过滤异步感知时，将事件间隔作为重建连续状态的证据并比较能否保留快速动态。见表 1、4。

<a id="paper-layerbind-early-latent-occlusion-composition"></a>

## Layer-wise Instance Binding for Regional and Occlusion Control in Text-to-Image Diffusion Transformers

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Layer-wise_Instance_Binding_for_Regional_and_Occlusion_Control_in_Text-to-Image_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_Layer-wise_Instance_Binding_for_Regional_and_Occlusion_Control_in_Text-to-Image_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 区域提示可以约束对象出现位置，但多个区域重叠时遮挡顺序不稳定。
- **核心创新 / 方法** · 先在共享背景条件下初始化独立实例分支，早期按层序合并其潜状态，再维持各层语义。
- **Baseline** · 与 RAGD、HybridLayout 等区域方法比较，单独检查不同实例绑定阶段。
- **Benchmark** · BindBench 的相对深度、布局、图文对应，以及 CLIP、VQAScore、HPS 指标。
- **关键结果 / 消融** · 表 3 的 VQAScore 在分阶段配置中从 38.36 到完整设置的 52.55，HPS 从 28.27 到 29.66。
- **适用条件 / 局限** · 依赖区域和深度次序作为输入，透明、复杂互相遮挡和次序不明时仍需验证。

**可复用机制** · 要控制对象遮挡顺序，可在去噪早期按深度顺序合并局部实例潜状态，再共享语义细化。见表 1、3。

<a id="paper-partitioned-unrolling-global-normal-operator"></a>

## Efficient Unrolled Networks for Large-Scale 3D Inverse Problems

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Vo_Efficient_Unrolled_Networks_for_Large-Scale_3D_Inverse_Problems_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Vo_Efficient_Unrolled_Networks_for_Large-Scale_3D_Inverse_Problems_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 大规模三维前向算子的显存开销限制端到端展开训练，独立切块又会损害全局测量一致性。
- **核心创新 / 方法** · 分区执行展开网络的更新，并对全局正则方程算子做可选近似以保留数据一致性。
- **Baseline** · 比较完整三维展开、仅近似算子、仅分区及两者组合。
- **Benchmark** · Calgary-Campinas 多线圈 MRI 与 Walnut-CBCT，比较平均 PSNR、峰值显存和训练步时。
- **关键结果 / 消融** · 表 4 中 MRI 仅分区时显存由 75.93 降到 37.02 GB，PSNR 从 36.23 到 35.85；CBCT 完整展开超显存，分区并近似达到 34.15 PSNR。
- **适用条件 / 局限** · 正文使用高斯噪声下的最小二乘一致性，移至泊松等噪声模型需重新定义数据一致性。

**可复用机制** · 大体积逆问题可将域分块与全局数据一致性联合起来，先验证分块节省显存，再看近似算子值不值得。见表 4。

<a id="paper-slideredit-shared-continuous-instruction-adapters"></a>

## SliderEdit: Continuous Image Editing with Fine-Grained Instruction Control

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zarei_SliderEdit_Continuous_Image_Editing_with_Fine-Grained_Instruction_Control_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zarei_SliderEdit_Continuous_Image_Editing_with_Fine-Grained_Instruction_Control_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 多项编辑通常都以固定强度施加，调整其中一项容易扰动其他项。
- **核心创新 / 方法** · 学习跨编辑共享的低秩适配，用各指令独立强度控制其贡献，支持推理时连续调节。
- **Baseline** · 对比为概念定制的 Concept Slider、连续属性控制和显式、隐式 CFG。
- **Benchmark** · 单指令与多指令强度扫描考察外推、连续性和解耦，报告 CLIP、SigLIP、BLIP、LPIPS、DINO。
- **关键结果 / 消融** · 表 1 的 GSTLoRA 在 CLIP 连续性上为 0.2998，显式 CFG 为 0.1993；对应外推为 0.2648、0.2731，连续性收益伴随外推差异。
- **适用条件 / 局限** · 适配依赖基础编辑器能理解指令，冲突指令或极端强度下仍可能串扰和丢失身份。

**可复用机制** · 多指令编辑可给每条指令保留独立连续强度，用共享低秩参数支持新编辑，并单测连续性和编辑串扰。见表 1、2。

<a id="paper-atomic-motion-recomposition"></a>

## Open the Motion Door: Atomic Motion Decomposition and Recomposition for Open-Vocabulary Motion Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Fan_Open_the_Motion_Door_Atomic_Motion_Decomposition_and_Recomposition_for_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Fan_Open_the_Motion_Door_Atomic_Motion_Decomposition_and_Recomposition_for_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 直接用原句生成动作容易将语言表达与有限的训练动作配对记忆。
- **核心创新 / 方法** · 文本分解模块提取原子动作，重组模块融合部件级信息生成最终动作。
- **Baseline** · 表1比较前序文本到动作模型，表2拆解文本动作对齐和组合特征融合。
- **Benchmark** · HumanML3D 域内，IDEA400 与 Mixamo 域外；表1报告多项文本动作匹配和生成指标。
- **关键结果 / 消融** · 表1显示主要收益来自两个域外集合，表2检验分别移去组件后在域内外的变化。
- **适用条件 / 局限** · 原子词表仍限制表达范围，同时发生且有力学耦合的动作需要单独验证。

**可复用机制** · 新指令超出训练词汇时，将文本先映射到可重组的身体部位动作，再检查组合泛化。

<a id="paper-faithful-contouring"></a>

## Faithful Contouring: Near-Lossless 3D Voxel Representation Free from Iso-surface

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Luo_Faithful_Contouring_Near-Lossless_3D_Voxel_Representation_Free_from_Iso-surface_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Luo_Faithful_Contouring_Near-Lossless_3D_Voxel_Representation_Free_from_Iso-surface_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 水密化或渲染优化会改变细薄、开放和含内部结构的网格。
- **核心创新 / 方法** · 用稀疏体素直接记录表面信息，重网格不做等值面提取；另设计双模式自编码器。
- **Baseline** · 表1比较已有体素表示，表2比较各 VAE 及体素/点输入配置。
- **Benchmark** · 直接网格表示的 Hausdorff 和 Chamfer 距离；VAE 重建按全集与水密子集分别报告。
- **关键结果 / 消融** · 正文报告直接表示的距离误差达到约10⁻⁵量级，表2分别检验512与1024分辨率的重建。
- **适用条件 / 局限** · 适用条件是可取得原始网格并在稀疏网格上表示表面；实际存储和解码开销取决于表面复杂度。

**可复用机制** · 输入可能非水密且需保留内层或锐边时，考虑直接编码局部表面而非依赖隐式等值面。

<a id="paper-stage-aware-prompt-decomposition"></a>

## Image Generation from Contextually-Contradictory Prompts

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Huberman_Image_Generation_from_Contextually-Contradictory_Prompts_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Huberman_Image_Generation_from_Contextually-Contradictory_Prompts_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 关系上看似矛盾但可实现的提示会被模型替换成常见语义。
- **核心创新 / 方法** · 由 LLM 找出冲突后生成按阶段使用的代理提示，使整体构型与后期局部细节分别进入去噪。
- **Baseline** · 表1–2含 SD3、FLUX 和阶段提示对照，表3检验分解，表4扰动阶段区间。
- **Benchmark** · 多套矛盾提示基准的 GPT-4o 对齐评估和人工对齐、画质偏好；表3在 Whoops-Hard 消融。
- **关键结果 / 消融** · 表3与表4分别提供分解和阶段位置的对照，表2以人评补充自动判分。
- **适用条件 / 局限** · 依赖语言模型能生成保持原意的代理提示，不同扩散模型何时生成关系或纹理需重新测。

**可复用机制** · 罕见组合被生成先验覆盖时，可把冲突概念放到不同去噪阶段表达，并对去噪时间段做扰动验证。

<a id="paper-bips"></a>

## See Less, See Right: Bi-directional Perceptual Shaping For Multimodal Reasoning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_See_Less_See_Right_Bi-directional_Perceptual_Shaping_For_Multimodal_Reasoning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_See_Less_See_Right_Bi-directional_Perceptual_Shaping_For_Multimodal_Reasoning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 模型能靠文本捷径回答，并忽略决定答案的细部像素。
- **核心创新 / 方法** · 以提问生成保留/移除证据两种视图，在前者加 KL 一致约束，在后者加 KL 分离约束。
- **Baseline** · Qwen2.5-VL-7B 与 GRPO 基线，表2消融两个约束，表3测试课程，表4测试对照视图生成。
- **Benchmark** · 表1为图表理解和通用感知推理八项基准，包含未见数据或图像类型。
- **关键结果 / 消融** · 原文报告 Qwen2.5-VL-7B 跨八基准平均提升8.2%，表2验证约束的独立作用。
- **适用条件 / 局限** · 需能正确生成问题相关遮罩，移除关键区域后若仍可推断答案，分离目标会误罚合理推理。

**可复用机制** · 同时训练证据充分性与必要性，让模型对保留答案证据的裁剪稳定，对遮掉关键证据敏感。

<a id="paper-mesh-pro-arpo"></a>

## Mesh-Pro: Asynchronous Advantage-guided Ranking Preference Optimization for Artist-style Quadrilateral Mesh Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhou_Mesh-Pro_Asynchronous_Advantage-guided_Ranking_Preference_Optimization_for_Artist-style_Quadrilateral_Mesh_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhou_Mesh-Pro_Asynchronous_Advantage-guided_Ranking_Preference_Optimization_for_Artist-style_Quadrilateral_Mesh_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 网格生成的离线偏好模型难适应新样本，在线同步又被采样等待限制。
- **核心创新 / 方法** · 异步产生并优化样本，将组内优势转化为排名偏好，还加入针对网格完整性的奖励。
- **Baseline** · 表2消融异步组件，表3比较 DPO、GRPO 与 ARPO，表5比较网格 token 表示。
- **Benchmark** · 艺术网格和稠密网格，通过 CD、HD、BR、QR、用户评分及训练耗时量化。
- **关键结果 / 消融** · 正文报告异步比同步 RL 快3.75倍；表1稠密和艺术网格 QR 为81%和78%。
- **适用条件 / 局限** · 排序依赖奖励区分几何缺陷的能力，异步更新的样本陈旧程度在其他生成域需测。

**可复用机制** · 生成样本昂贵时，可比较异步在线偏好排序和同步策略更新，并监测训练效率与几何奖励。

<a id="paper-separable-causal-diffusion"></a>

## Causality in Video Diffusers is Separable from Denoising

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Bai_Causality_in_Video_Diffusers_is_Separable_from_Denoising_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Bai_Causality_in_Video_Diffusers_is_Separable_from_Denoising_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 每个去噪步重复全量跨帧注意力，延迟随帧与去噪步增加。
- **核心创新 / 方法** · 逐帧运行因果 Transformer 编码器，并用轻量逐帧扩散解码器迭代渲染。
- **Baseline** · 表1–2对比联合架构和变体；表3对比参数量、分辨率相近的文生视频模型。
- **Benchmark** · TECO-Minecraft、UCF-101 的 LPIPS、SSIM、PSNR、FVD，VBench 总分和单 H100 吞吐延时。
- **关键结果 / 消融** · 表3 SCD 1.6B 在832×480达11.1 FPS、延迟0.29秒、VBench总分84.03。
- **适用条件 / 局限** · 跨帧关系要能提前压进编码表征，依赖去噪后信息的细粒度动态可能需要更强的耦合。

**可复用机制** · 先逐层测去噪步间冗余与跨帧依赖，再将可复用的时序编码移出迭代循环。

<a id="paper-video-llm-layer-knockout"></a>

## An Empirical Study on How Video-LLMs Answer Video Questions

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Gou_An_Empirical_Study_on_How_Video-LLMs_Answer_Video_Questions_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Gou_An_Empirical_Study_on_How_Video-LLMs_Answer_Video_Questions_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 最终准确率难辨模型在哪些层从视频取证或只在做语言推理。
- **核心创新 / 方法** · 分别屏蔽视频时序、空间或语言读视频的注意力并滑动干预层窗口，再按发现验证退出和局部注意力。
- **Baseline** · 表1对照原模型、只提前退出视频 token、退出加时间窗口等配置。
- **Benchmark** · 三套视频问答基准，使用 LLaVA-OneVision、LLaVA-Video 等模型比较答题表现。
- **关键结果 / 消融** · 正文显示低层普遍做视频证据抽取，部分中间层对答案有突出影响；表1对比由此设计的简化。
- **适用条件 / 局限** · 注意力屏蔽引入分布变化，层定位结论依赖模型与问题类型，替换骨干须重测。

**可复用机制** · 决定何处丢弃或缩窗视频 token 前，先按层定位时空信息进入推理的关键窗口。

<a id="paper-todsynth-control-rectify"></a>

## Task-Oriented Data Synthesis and Control-Rectify Sampling for Remote Sensing Semantic Segmentation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_Task-Oriented_Data_Synthesis_and_Control-Rectify_Sampling_for_Remote_Sensing_Semantic_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yang_Task-Oriented_Data_Synthesis_and_Control-Rectify_Sampling_for_Remote_Sensing_Semantic_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 生成图可能与配对掩码不符，视觉质量高也不保证可用于下游训练。
- **核心创新 / 方法** · 图文与掩码共同作为生成条件，并由语义反馈在早期调整流匹配采样方向。
- **Baseline** · 表1与既有合成数据方案比较，表2和3改变控制和后处理。
- **Benchmark** · FUSU-4k 等遥感分割设置，含少样本及复杂场景，以分割效果衡量生成数据。
- **关键结果 / 消融** · 正文报告配对和采样控制对下游分割的贡献。
- **适用条件 / 局限** · 任务反馈准确性和掩码覆盖限制收益，采样期反馈还增加计算。

**可复用机制** · 合成带分割标签的训练样本时，在采样早期以任务损失校正语义掩码一致性。

<a id="paper-temporal-mutual-information-snn"></a>

## Robust Spiking Neural Networks by Temporal Mutual Information

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_Robust_Spiking_Neural_Networks_by_Temporal_Mutual_Information_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_Robust_Spiking_Neural_Networks_by_Temporal_Mutual_Information_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 静态鲁棒性诊断不能区分跨时刻的脉冲信息传递。
- **核心创新 / 方法** · 从信息瓶颈分析鲁棒性误差与时序互信息，构造 TMI 正则。
- **Baseline** · 同脉冲网络去掉 TMI 的训练结果及其他鲁棒训练配置。
- **Benchmark** · CIFAR-10/100、DVS-CIFAR10、Tiny-ImageNet 和 ImageNet，测普通及扰动条件准确率。
- **关键结果 / 消融** · 原文报告跨架构的鲁棒性改善，表3给出 CIFAR-100 的有无正则比较。
- **适用条件 / 局限** · 误差界依赖理论假设，过强压缩可能丢失类别相关时序。

**可复用机制** · 训练脉冲网络追求鲁棒性时，针对时序潜表示施加互信息正则。

<a id="paper-r2vlm-recurrent-progress"></a>

## Recurrent Reasoning with Vision-Language Models for Estimating Long-Horizon Embodied Task Progress

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Recurrent_Reasoning_with_Vision-Language_Models_for_Estimating_Long-Horizon_Embodied_Task_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Recurrent_Reasoning_with_Vision-Language_Models_for_Estimating_Long-Horizon_Embodied_Task_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 整段视频推理开销大，逐段独立处理又遗失已完成步骤。
- **核心创新 / 方法** · 循环维护任务拆解和完成状态的显式记录，并用局部片段更新。
- **Baseline** · 原文表1比较其他进度估计及三种自身变体，表2比较奖励设置。
- **Benchmark** · ALFRED、Ego4D 长任务进度及受进度信号辅助的策略任务。
- **关键结果 / 消融** · 表1–3报告进度估计及后续策略收益，验证状态可指导不同环节。
- **适用条件 / 局限** · 错误状态可能递归传播，任务中途改变或步骤顺序不唯一时需核验。

**可复用机制** · 估计长程任务进度时逐段处理视频，只向下一段传递可更新的任务状态摘要。

<a id="paper-sra2-vae-feature-alignment"></a>

## SRA 2: Variational Autoencoder Self-Representation Alignment  for Efficient Diffusion Training

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_SRA_2_Variational_Autoencoder_Self-Representation_Alignment__for_Efficient_Diffusion_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_SRA_2_Variational_Autoencoder_Self-Representation_Alignment__for_Efficient_Diffusion_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · REPA 额外编码特征，既有自对齐方法还维护双模型。
- **核心创新 / 方法** · 用轻量投影对齐 DiT 中层与冻结 VAE 特征，保留常规去噪训练。
- **Baseline** · 标准 SiT、REPA、SRA 等对齐方案，表1检查不同对齐配置。
- **Benchmark** · ImageNet 256×256，按训练迭代比较 FID，无 CFG 设置另做消融。
- **关键结果 / 消融** · 表1–3报告相对于普通扩散训练的收敛和生成质量改善。
- **适用条件 / 局限** · VAE 特征容量、目标层及领域会改变可对齐信息。

**可复用机制** · 训练扩散模型时先尝试把中层对齐到已有 VAE 特征，省去额外表征编码器。

<a id="paper-cameo-correspondence-attention"></a>

## Correspondence-Attention Alignment for Multi-View Diffusion Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Kwon_Correspondence-Attention_Alignment_for_Multi-View_Diffusion_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Kwon_Correspondence-Attention_Alignment_for_Multi-View_Diffusion_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 模型能自发对齐部分像素，但大视点变化时注意力对应不准。
- **核心创新 / 方法** · 将已知几何对应做为注意力显式监督，并比较所监督层数和位置。
- **Baseline** · 同多视图扩散骨干无额外监督及不同注意力层对照。
- **Benchmark** · RealEstate10K 等新视角评测，比较不同训练轮次的合成表现。
- **关键结果 / 消融** · 原文报告约一半训练迭代达收敛，且单层监督已有效。
- **适用条件 / 局限** · 依赖监督对应质量，遮挡区域不能应用同一配对约束。

**可复用机制** · 多视角扩散训练中直接监督一层跨视图注意力的几何对应，作为提高视角一致性的低开销选择。

<a id="paper-cigma-causal-head-attribution"></a>

## CIGMA: Causal Information-Gain Mechanistic Attribution of Attention Heads in Vision Transformers

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Maliha_CIGMA_Causal_Information-Gain_Mechanistic_Attribution_of_Attention_Heads_in_Vision_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Maliha_CIGMA_Causal_Information-Gain_Mechanistic_Attribution_of_Attention_Heads_in_Vision_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 单看准确率或剪枝难区分模型根据前景还是背景预测。
- **核心创新 / 方法** · 以预测分布的 Jensen–Shannon 信息差比较两类遮挡，定位相应注意力子网。
- **Baseline** · 同骨干原模型及表1–2所列诊断干预配置。
- **Benchmark** · CIFAR-10、CIFAR-100、Tiny-ImageNet，跨 InternVL2-26B、LLaVA-1.6 和 LLaVA-1.5-13B 分类。
- **关键结果 / 消融** · 原文报告对象和背景敏感头可分，并在多架构测分类。
- **适用条件 / 局限** · 遮挡可能引入非自然图像变化；因果解释限于实际干预和目标任务。

**可复用机制** · 模型依赖背景捷径时，用去对象和去背景两种成对干预区分注意力头处理的证据。

<a id="paper-atoken-covariance-loss-visual-tokenizer"></a>

## AToken: A Unified Tokenizer for Vision

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Lu_AToken_A_Unified_Tokenizer_for_Vision_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Lu_AToken_A_Unified_Tokenizer_for_Vision_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 多模态 tokenizer 要同时保留纹理与语义，Transformer 判别器过强时会使重建退化。
- **核心创新 / 方法** · 作者先分解 rFID 的均值与协方差成分，再用特征 Gram 矩阵损失和感知监督直接约束二阶统计，无需训练判别器。
- **Baseline** · 图 3 比较有无对抗训练和 Gram 损失；表 1 对照 VA-VAE、UniTok 等 tokenizer。
- **Benchmark** · ImageNet 重建与零样本分类、TokenBench 和 MSR-VTT 的视频重建与检索、Toys4k 三维重建与分类。
- **关键结果 / 消融** · 图 3 中协方差占该设置重建 FID 误差 86.6%；表 1 连续 tokenizer 的 ImageNet rFID 为 0.21、分类为 82.2%，视频 rFVD 为 3.01。
- **适用条件 / 局限** · 协方差占比依赖数据与特征空间，统一 tokenizer 的整体收益还含课程训练与共享架构。

**可复用机制** · 视觉编码重建若在对抗训练中不稳定，可先分解重建误差，再检验特征二阶统计损失能否代替判别器。见图 3、表 1。

<a id="paper-uniprior-invariant-target-self-correlation-alignment"></a>

## Towards Generalized Representations for Low-Light Understanding: When Signal Constancy Meets Semantic Enrichment

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Towards_Generalized_Representations_for_Low-Light_Understanding_When_Signal_Constancy_Meets_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Towards_Generalized_Representations_for_Low-Light_Understanding_When_Signal_Constancy_Meets_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 暗光适配在没有真实暗光训练数据时容易过拟合某类退化，直接匹配基础模型特征可能迁移背景差异。
- **核心创新 / 方法** · 同时输入并重建光照不变先验，用视觉基础模型的自相关图为对比学习提供语义结构。
- **Baseline** · 比较朴素特征对齐、移除先验重建损失、先验解码器、对比增强或相关对齐等。
- **Benchmark** · CoDaN 的低照分类 Top-1、Nighttime Driving 的分割 mIoU，另测暗光人脸检测。
- **关键结果 / 消融** · 表 3 高层完整方案分类为 74.52%、分割为 48.20%，朴素特征对齐为 63.26%、41.72%，去掉相关对齐为 69.71%、46.67%。
- **适用条件 / 局限** · 依赖可计算且保留任务信号的光照先验；更换退化方式需要确认先验不会抹掉目标线索。

**可复用机制** · 光照分布变化时，可以对照直接对齐特征与对齐图像内部关系，并用重建不变量为模型提供稳定目标。见表 3。

<a id="paper-tsd-pair-specific-shared-subspaces"></a>

## Tri-Subspaces Disentanglement for Multimodal Sentiment Analysis

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Meng_Tri-Subspaces_Disentanglement_for_Multimodal_Sentiment_Analysis_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Meng_Tri-Subspaces_Disentanglement_for_Multimodal_Sentiment_Analysis_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 语言、视觉、声音可能只在某一对模态中共享有效信号，全共享与私有的二分法会漏掉这种结构。
- **核心创新 / 方法** · 显式建立全共享、两两共享、模态私有子空间，分别约束再以子空间感知注意力融合。
- **Baseline** · 对照 EMOE、MISA 等，以及同一架构下移除某类子空间和直接融合的版本。
- **Benchmark** · CMU-MOSI、CMU-MOSEI 的 MAE 与七分类准确率，以及 MIntRec 意图分类准确率。
- **关键结果 / 消融** · 表 3 完整模型 MIntRec 准确率 73.67%、MOSI MAE 0.691，移除两两共享子空间分别为 72.3%、0.705。
- **适用条件 / 局限** · 主要验证三模态；更多传感器时两两组合增多，对共享信号的定义与开销需重测。

**可复用机制** · 三模态以上的融合可检验是否保留两两共享的表示，而不把信号只分为全局共有与模态私有。见表 3。

<a id="paper-ais-neighbor-seeded-deformation-optimization"></a>

## Event-based Visual Deformation Measurement

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_Event-based_Visual_Deformation_Measurement_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wu_Event-based_Visual_Deformation_Measurement_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 快速形变会使帧间对应困难，稀疏事件还会让局部位移拟合停在不稳定解。
- **核心创新 / 方法** · 以仿射不变单纯形划分局部变形，用已收敛区域逐步为邻近的未收敛区域提供优化引导。
- **Baseline** · 对照相同多尺度搜索与 Adam 设置的普通局部优化，并和帧或事件视觉基线比较。
- **Benchmark** · 事件和图像融合的变形数据，以位移估计、有效子域比例与优化收敛时间衡量。
- **关键结果 / 消融** · 表 3 将有效子域比例从 39.0% 提至 65.7%，平均收敛时间由 26.5 秒降至 7.2 秒。
- **适用条件 / 局限** · 局部模型假设形变可线性化且邻域相关，断裂、遮挡或邻域分属不同物体时需加边界判断。

**可复用机制** · 局部形变拟合不稳时，可以让高置信的子域引导邻域搜索，用收敛时间和有效子域比例核对。见表 3。

<a id="paper-3d-slim-geometry-instruction-attention-mask"></a>

## Masking Matters: Unlocking the Spatial Reasoning Capabilities of LLMs for 3D Scene-Language Understanding

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Jeon_Masking_Matters_Unlocking_the_Spatial_Reasoning_Capabilities_of_LLMs_for_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Jeon_Masking_Matters_Unlocking_the_Spatial_Reasoning_Capabilities_of_LLMs_for_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 因果注意力将对象输入顺序误作空间先验，也限制对象利用后出现的任务指令。
- **核心创新 / 方法** · 对象之间用几何密度自适应的可见邻域替代因果遮罩，并在对象与指令间开放任务相关注意力。
- **Baseline** · 以 Chat-Scene 的因果、全局、对角和固定邻域遮罩比较，并分别消融几何遮罩和指令遮罩。
- **Benchmark** · ScanRefer、Multi3DRefer、Scan2Cap、ScanQA、SQA3D，分别评估定位、描述和问答。
- **关键结果 / 消融** · 表 4 的 ScanRefer Acc@0.5 从因果基线 49.5 到单独几何遮罩 53.1，再到组合 54.1；ScanQA CIDEr 由单独几何的 94.2 略降至组合的 94.0。
- **适用条件 / 局限** · 依赖对象几何位置与划分质量，稠密视角、远距离关系和对象缺失需另行验证。

**可复用机制** · LLM 接收无序对象集合时，可将对象间注意力从因果顺序改为随空间密度调整的邻域，并允许对象直接关注指令。见表 3、4。

<a id="paper-geodexgrasp-factorized-geometric-conditioning"></a>

## GeoDexGrasp: Geometry-aware Generation for Data-efficient and Physics-plausible Dexterous Grasping

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Han_GeoDexGrasp_Geometry-aware_Generation_for_Data-efficient_and_Physics-plausible_Dexterous_Grasping_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Han_GeoDexGrasp_Geometry-aware_Generation_for_Data-efficient_and_Physics-plausible_Dexterous_Grasping_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 一次生成手型与根部姿态很难分清物体几何因素，易增加手物穿透。
- **核心创新 / 方法** · 用 SIM(3) 等变网络解耦姿态、方向、形状和大小，按因素分别为根部旋转与后续抓取生成提供条件。
- **Baseline** · 比较不解耦、分阶段、逐步加入各条件和关系解耦预训练；另与已有灵巧抓取方法比较。
- **Benchmark** · 五个抓取数据集和真实机械手测试，报告成功率与穿透距离，另测不同尺寸泛化。
- **关键结果 / 消融** · 表 3 无解耦基线的成功率与穿透指标为 41.8、40.7；只分阶段时为 56.1、33.8；完整方案为 67.5、15.5。
- **适用条件 / 局限** · 接触对象的几何质量是前提，真实设置需要从部分 RGB-D 观察补全对象；不同手部结构应重验条件划分。

**可复用机制** · 抓取生成可按几何因素分配条件，先用姿态和交互方向规划根部旋转，再用形状和尺寸拟合手型。见表 3。

<a id="paper-orthogonal-gradient-matching"></a>

## Beyond Soft Label: Dataset Distillation via Orthogonal Gradient Matching

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Bo_Beyond_Soft_Label_Dataset_Distillation_via_Orthogonal_Gradient_Matching_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Bo_Beyond_Soft_Label_Dataset_Distillation_via_Orthogonal_Gradient_Matching_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 匹配批归一化统计主要约束梯度尺度，合成样本的更新方向仍可能和真实样本不同。
- **核心创新 / 方法** · 对真实和合成梯度做奇异值分解，将奇异值置一后匹配正交化梯度，以最小二乘实现。
- **Baseline** · 表1–2比较 RDED 等蒸馏方法，表3消融 SVD。
- **Benchmark** · ImageNet-1K，按每类合成数和软/硬标签评价分类准确率。
- **关键结果 / 消融** · 论文报告软标签47.0%、硬标签16.7%的配置；表3在 IPC=10 单列有无 SVD 对照。
- **适用条件 / 局限** · 现有理论与实证依赖所用梯度结构，去除尺度对其他优化器和模型的影响需重测。

**可复用机制** · 预算有限且只用硬标签时，数据蒸馏应测梯度方向是否随合成集保留。

<a id="paper-cubic-bimanual"></a>

## CUBic: Coordinated Unified Bimanual Perception and Control Framework

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_CUBic_Coordinated_Unified_Bimanual_Perception_and_Control_Framework_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_CUBic_Coordinated_Unified_Bimanual_Perception_and_Control_Framework_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 完全解耦会遗漏臂间关系，强绑定则限制任一手独立动作。
- **核心创新 / 方法** · 单向汇聚感知，用两套码本和共享映射建立双向协调，再把共享 token 表征接入控制。
- **Baseline** · 表1比较 RoboTwin 策略含 DP3，表4消融共享映射与两阶段训练。
- **Benchmark** · RoboTwin 七项任务、三随机种子成功率，表2–3报告真实任务及域内外物体位置。
- **关键结果 / 消融** · 表1作者报告相对之前最佳方法平均成功率改善12.0%，表4比较共享映射设计。
- **适用条件 / 局限** · 不同机械结构或独立视角下的码本映射需重训，颜色任务限制点云基线直接比较。

**可复用机制** · 两控制臂既需局部自治也需协调时，可保留各自离散码本，用共享映射协调。

<a id="paper-chips-data-selection"></a>

## CHIPS: Efficient CLIP Adaptation via Curvature-aware Hybrid Influence-based Data Selection

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhuang_CHIPS_Efficient_CLIP_Adaptation_via_Curvature-aware_Hybrid_Influence-based_Data_Selection_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhuang_CHIPS_Efficient_CLIP_Adaptation_via_Curvature-aware_Hybrid_Influence-based_Data_Selection_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 直接扩大领域数据或仅按相似度筛选，无法判断样本对对比学习更新和通用保留的影响。
- **核心创新 / 方法** · 在 CLIP 末端投影子空间近似曲率感知影响，用 JL 草图压缩估计并加入选择相关性和可学习性权重。
- **Baseline** · 以 MetaCLIP 持续预训练为入口，表2对比不同数据选择，表4消融。
- **Benchmark** · B16-400M 在 BIOMEDICA 不同保留比10/20/30/50%下比较专科下游表现，表3比较跨骨干泛化。
- **关键结果 / 消融** · 表2–4在固定保留比下对比选择策略、模型规模与组件，支持先筛样再分配预训练预算。
- **适用条件 / 局限** · 近似依赖投影头能代理全参数影响，同时需要代表性的目标参考；领域参考偏移时应复核。

**可复用机制** · 领域适配预算有限时，按影响力同时考虑目标收益与通用能力保留。

<a id="paper-fast-thinkact"></a>

## Fast-ThinkAct: Efficient Vision-Language-Action Reasoning via Verbalizable Latent Planning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_Fast-ThinkAct_Efficient_Vision-Language-Action_Reasoning_via_Verbalizable_Latent_Planning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_Fast-ThinkAct_Efficient_Vision-Language-Action_Reasoning_via_Verbalizable_Latent_Planning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 显式视觉语言思维链较长，会拖慢具身动作生成。
- **核心创新 / 方法** · 从教师蒸馏可语言化的潜在推理，以轨迹偏好目标对齐计划与操作，并连接低层策略。
- **Baseline** · 图3比较 ThinkAct 和 OpenVLA 等，表3消融训练目标和潜在学习。
- **Benchmark** · LIBERO 与 SimplerEnv 成功率和推理延迟，RoboTwin2.0 难度分组及 EgoPlan-Bench2、RoboVQA、OpenEQA。
- **关键结果 / 消融** · 图3报告3B 模型相对 ThinkAct-3B 推理延迟减少89.3%，表3核查目标贡献。
- **适用条件 / 局限** · 潜计划依赖教师监督和轨迹偏好，罕见任务及真实部署闭环安全约束要重新评估。

**可复用机制** · 把可解释推理留作训练监督，部署使用能解码为语言的潜计划以减小决策时延。

<a id="paper-geo3dpruner"></a>

## Geometry-Guided 3D Visual Token Pruning for Video-Language Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Geometry-Guided_3D_Visual_Token_Pruning_for_Video-Language_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Geometry-Guided_3D_Visual_Token_Pruning_for_Video-Language_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 时间邻近性不能充分识别多视重复，也不能保证保留的 token 覆盖场景。
- **核心创新 / 方法** · 由几何感知注意力建跨帧相关性，体素内选代表特征，体素之间按空间多样性裁剪。
- **Baseline** · 表1–2比较既有视觉 token 裁剪法，表3消融体素内和体素间阶段，表4比较体素选择。
- **Benchmark** · 16及32帧输入，五基准九指标的平均性能保留率，随裁剪比例比较。
- **关键结果 / 消融** · 表1–2验证不同序列长度，表3区分去冗余与保覆盖的贡献。
- **适用条件 / 局限** · 依赖可靠的深度和位姿，将很小的物体映射进稀疏体素时需单独测未覆盖率。

**可复用机制** · 多视角输入压缩先按同一3D位置去重，再按空间覆盖选保留 token。

<a id="paper-dip-pixel-diffusion"></a>

## DiP: Taming Diffusion Models in Pixel Space

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_DiP_Taming_Diffusion_Models_in_Pixel_Space_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_DiP_Taming_Diffusion_Models_in_Pixel_Space_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 潜扩散有 VAE 重建损失，直接像素扩散又受序列计算量拖累。
- **核心创新 / 方法** · 用大 patch 的 DiT 处理全局结构，再以轻量共训 detailer head 恢复局部像素信息。
- **Baseline** · 表1比较像素和潜空间模型，表2消融不同计算/设计方案。
- **Benchmark** · ImageNet 256×256，Euler 求解器与 CFG，比较 FID、耗时和参数；表3给其他设置。
- **关键结果 / 消融** · 表1 DiP-XL/16 一组报告 FID 1.79、0.92秒、631M；正文报告 detailer 只增加约0.3%参数。
- **适用条件 / 局限** · 大 patch 会压缩全局级空间粒度，跨 patch 微结构与实际硬件生成成本需单测。

**可复用机制** · 高分辨率像素扩散中，用大 patch 构造全局上下文，让局部头承担像素细节。

<a id="paper-reasonx"></a>

## ReasonX: MLLM-Guided Intrinsic Image Decomposition

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Dirik_ReasonX_MLLM-Guided_Intrinsic_Image_Decomposition_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Dirik_ReasonX_MLLM-Guided_Intrinsic_Image_Decomposition_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 仅在合成标注训练的分解模型迁移到真实场景表现不稳定，绝对物理监督昂贵。
- **核心创新 / 方法** · 用 MLLM 给出相对比较，与模型预测解析所得关系比较，再以 GRPO 优化。
- **Baseline** · 表1–4比较原分解基模型、ReasonX 变体与具备相关监督的既有方法。
- **Benchmark** · IIW 反照率 WHDR、MAW 强度及色度，NYUv2 与 ETH3D 相对深度，以及表4表面法线。
- **关键结果 / 消融** · 正文报告不同基模型在 IIW 的 WHDR 降低9–25%，并单独验证深度和法线。
- **适用条件 / 局限** · 奖励可靠性依赖判断者对相对关系的准确性，绝对物理尺度仍需额外约束。

**可复用机制** · 真实图像无密集真值时，可收集教师相对判断，并与预测中可算出的物理关系比较作为奖励。

<a id="paper-relax-latent-exploration"></a>

## ReLaX: Reasoning with Latent Exploration for Large Reasoning Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_ReLaX_Reasoning_with_Latent_Exploration_for_Large_Reasoning_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_ReLaX_Reasoning_with_Latent_Exploration_for_Large_Reasoning_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 可验证奖励可能导致探索过早收敛，仅提高 token 熵未必增加不同推理过程。
- **核心创新 / 方法** · 用 Koopman 线性近似表示隐状态动态，以动态谱分散评估和引导探索。
- **Baseline** · 表1比较不同规模的视觉语言推理模型，表2同基座对照其他 RLVR 方法。
- **Benchmark** · 多模态推理 mean@1 与纯文本数学 mean@1/mean@32。
- **关键结果 / 消融** · 表1 ReLaX-VL-3B 与7B的平均 mean@1 分别为48.1和53.2，表2跨纯文本基座比较。
- **适用条件 / 局限** · 谱量依赖隐藏层选择和线性化假设，其他自由文本或连续动作策略需要验证它能预测有效探索。

**可复用机制** · 策略探索应同时看生成 token 多样性和中间状态动态的多样性。

<a id="paper-resfit-superfrusta"></a>

## Residual Primitive Fitting of 3D Shapes with SuperFrusta

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Ganeshan_Residual_Primitive_Fitting_of_3D_Shapes_with_SuperFrusta_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Ganeshan_Residual_Primitive_Fitting_of_3D_Shapes_with_SuperFrusta_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 密集网格难编辑，而简单基元过多会降低可控性。
- **核心创新 / 方法** · 用8参数可微 SuperFrustum 表示多种立体形状，交替分析全局残差与局部拟合。
- **Baseline** · 表1与已有基元重建比较；表2–3分别消融基元表示、残差拟合。
- **Benchmark** · 3DGen-Prim 和 Toys4K，测重建 IoU、基元数量和程序质量。
- **关键结果 / 消融** · 作者报告 IoU 提高超过9点而数量约减半。
- **适用条件 / 局限** · 基元族仍限制异形细节，可编辑性和覆盖之间需要取舍。

**可复用机制** · 拟合可编辑的几何基元时，从未解释残差增添基元，直接平衡覆盖和基元数量。

<a id="paper-bricknet-connectivity-programs"></a>

## BrickNet: Graph-Backed Generative Brick Assembly

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Kulits_BrickNet_Graph-Backed_Generative_Brick_Assembly_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Kulits_BrickNet_Graph-Backed_Generative_Brick_Assembly_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 直接生成每块位姿会使少数步骤后违反连接约束。
- **核心创新 / 方法** · 构造以部件和连接为边的装配程序，用语言模型生成图结构对应的序列。
- **Baseline** · 对照直接位姿表示的生成及无条件、文本条件配置。
- **Benchmark** · 十万余人造 LDraw 对象和场景，测无条件、文本条件装配及结构可执行性。
- **关键结果 / 消融** · 原文报告连接表示比位姿生成更容易得到有效结构。
- **适用条件 / 局限** · 需有零件接口拓扑；局部可连接不保证整体承载或稳定性。

**可复用机制** · 当零件装配受连接约束时，用连接关系而非裸三维位姿作为自回归生成单位。

<a id="paper-diffusion-mental-averages"></a>

## Diffusion Mental Averages

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Thawatdamrongkit_Diffusion_Mental_Averages_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Thawatdamrongkit_Diffusion_Mental_Averages_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 像素平均会抹除实体细节，单原型也会掩盖概念内不同模式。
- **核心创新 / 方法** · 让多个初噪的去噪语义轨迹向共识靠近；对多峰概念先聚类再映回生成空间。
- **Baseline** · 与图像集合外的平均或概念代表方案比较。
- **Benchmark** · Animal、Person、Object、Abstract 四类提示，用一致性、代表性和画质等指标。
- **关键结果 / 消融** · 表1给出概念原型量化比较，原文展示多峰与抽象案例。
- **适用条件 / 局限** · 依赖模型潜语义和聚类，生成原型不能视作真实训练集均值。

**可复用机制** · 审计生成器的概念原型时，比较去噪轨迹的语义中心，避免直接均值造成模糊。

<a id="paper-rned-continuous-number-tokens"></a>

## RNED: Rotary Number Encoding and Decoding for Medical VLMs

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_RNED_Rotary_Number_Encoding_and_Decoding_for_Medical_VLMs_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_RNED_Rotary_Number_Encoding_and_Decoding_for_Medical_VLMs_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 数字分词不天然保持数量邻近，影响测量和坐标预测。
- **核心创新 / 方法** · 对专用数值嵌入施加范数不变旋转，并用分数匹配式解码处理隐层噪声。
- **Baseline** · 与已有视觉语言模型及其他数字表示方案比较。
- **Benchmark** · Opport-CT、CT-RATE 的测量 MAE，医学视觉定位 IoU 和 Acc@5。
- **关键结果 / 消融** · 表1–3报告连续编码在测量和坐标任务均改善。
- **适用条件 / 局限** · 数值范围与频率配置影响可辨识性；需有可监督连续真值。

**可复用机制** · 多模态回归用数值相关旋转编码连续数，在隐层解码实数，避免把数值当普通离散字符串。

<a id="paper-lumimotion-dynamic-inverse-rendering"></a>

## LumiMotion: Improving Gaussian Relighting with Scene Dynamics

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Kaleta_LumiMotion_Improving_Gaussian_Relighting_with_Scene_Dynamics_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Kaleta_LumiMotion_Improving_Gaussian_Relighting_with_Scene_Dynamics_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 静态照片中高光和阴影容易被解释成固定材质。
- **核心创新 / 方法** · 学习动态二维高斯和形变，并用不同时刻在几何对应表面上的变化约束光照与反射分解。
- **Baseline** · 在多视图单时刻静态方法与现有可重光照方法间比较，表3做组件消融。
- **Benchmark** · 动态场景的反照率估计及重光照，以 LPIPS 等评价。
- **关键结果 / 消融** · 作者报告相对次佳方法反照率 LPIPS 好23%、重光照好15%。
- **适用条件 / 局限** · 需要可追踪表面及有效光照变化，非刚体对应失真或纯静态场景缺少该监督。

**可复用机制** · 动态逆渲染利用同一表面随运动经过不同光照的观测，辅助分离材质和照明。

<a id="paper-clean-pretraining-feature-target-multimodal-fusion"></a>

## Distribution-Aligned Multimodal Fusion for Robust Object Detection

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Hao_Distribution-Aligned_Multimodal_Fusion_for_Robust_Object_Detection_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Hao_Distribution-Aligned_Multimodal_Fusion_for_Robust_Object_Detection_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 针对训练退化优化 RGB 和红外融合，可能会损害新退化下的检测。
- **核心创新 / 方法** · 从正常图像估计冻结检测器的特征分布，训练轻量融合层将退化观测映射到该分布。
- **Baseline** · 对照不对齐、对齐训练退化分布、冻结模型只优化任务损失及端到端更新。
- **Benchmark** · 包括 LLVIP 等数据集，训练使用过曝样本，测试过曝与未见的夜间、欠曝和模糊，使用 IoU 0.5 的 mAP。
- **关键结果 / 消融** · 表 3 对齐正常分布的夜间、模糊结果为 76.8、40.6，对齐过曝分布为 67.5、28.5；过曝条件则为 47.3 对 48.2。
- **适用条件 / 局限** · 依赖取得能代表良好工作区间的正常数据，也依赖另一模态提供退化时仍有效的信息。

**可复用机制** · 训练只包含少数退化时，可让融合特征对齐冻结检测器已熟悉的正常分布，并用未见退化对照。见表 3。

<a id="paper-driffusion-parallel-draft-noise-refinement"></a>

## DRiffusion: Draft-and-Refine Process Parallelizes Diffusion Models with Ease

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Bai_DRiffusion_Draft-and-Refine_Process_Parallelizes_Diffusion_Models_with_Ease_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Bai_DRiffusion_Draft-and-Refine_Process_Parallelizes_Diffusion_Models_with_Ease_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 扩散采样各步依赖上一步，直接并行会破坏走过的状态或需要复制大量中间特征。
- **核心创新 / 方法** · 跳步构造未来时间的候选状态，并行计算噪声估计，再把结果用于常规去噪过程，提供保守与激进两种模式。
- **Baseline** · 与单设备原采样、少步采样、AsyncDiff 在 SDXL 上比较。
- **Benchmark** · MS-COCO 上以加速比、额外显存、FID、CLIP、PickScore 衡量。
- **关键结果 / 消融** · 表 2 四设备激进模式相对单设备快 3.6 倍、增加 222 MB、FID 24.14；AsyncDiff 四设备一配置快 3.4 倍、增加 554 MB、FID 24.25。
- **适用条件 / 局限** · 需要多设备有效并行与通信，草稿近似误差和加速受模型及采样计划影响。

**可复用机制** · 多设备扩散加速可比较先草拟未来状态并批量计算去噪，再以常规轨迹细化，检查延迟、显存和图像质量。见表 2。

<a id="paper-feat-shared-prototype-geometry-replay"></a>

## From Selection to Scheduling: Federated Geometry-Aware Correction Makes Exemplar Replay Work Better under Continual Dynamic Heterogeneity

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Qi_From_Selection_to_Scheduling_Federated_Geometry-Aware_Correction_Makes_Exemplar_Replay_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Qi_From_Selection_to_Scheduling_Federated_Geometry-Aware_Correction_Makes_Exemplar_Replay_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 客户端与任务的类比例会变，代表样本回放仍可能把稀有类表征拉向常见类。
- **核心创新 / 方法** · 用固定等角原型约束各端的表征角度结构，利用基于能量的推理几何校正减弱常见类偏置。
- **Baseline** · 在 FedCBDR 上比较只设固定原型、加入几何结构对齐、加入推理校正与组合。
- **Benchmark** · 五个客户端的 CIFAR-10 三任务和 CIFAR-100 五任务，在不同异质性参数下比较平均准确率。
- **关键结果 / 消融** · 表 2 的 CIFAR-10 在 β=0.5 时，FedCBDR 为 63.32%，只加固定原型反降到 62.17%，再加两项完整机制为 72.67%。
- **适用条件 / 局限** · 依赖客户端间可协调的类别和参照空间；固定原型本身未必有利，开放标签或更复杂任务需重测。

**可复用机制** · 联邦回放发生少数类塌缩时，可用跨客户端共享固定原型作角度锚点，再单测训练时几何对齐和推理校正。见表 2。

<a id="paper-star-separability-gated-test-time-prompts"></a>

## STAR: Test-Time Adaptation Can Enhance Universal Prompt Learning for Vision-Language Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Fu_STAR_Test-Time_Adaptation_Can_Enhance_Universal_Prompt_Learning_for_Vision-Language_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Fu_STAR_Test-Time_Adaptation_Can_Enhance_Universal_Prompt_Learning_for_Vision-Language_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 无标签测试流可能包含易被模型高置信误识别的域外样本。
- **核心创新 / 方法** · 用 Fisher 可分性软门控区分样本，以不确定性感知的共轭优化构造伪标签并通过原型检索校准。
- **Baseline** · 与 LoCoOp 等提示适配法比较，并消融软门控、共轭优化和测试时独立提示更新。
- **Benchmark** · ImageNet-1k 作为域内集，表 3 在 iNaturalist 与 SUN 汇总 FPR95 和 AUROC。
- **关键结果 / 消融** · 表 3 的 STAR-L 完整设置 FPR95、AUROC 为 14.55、97.08，移除软门控后为 83.02、74.28。
- **适用条件 / 局限** · 依赖域内和域外在当前嵌入下具有一定可分性，目标流中发生分布占比改变时需重验门控。

**可复用机制** · 测试流混有域外数据时，用可分性门控划分提示更新与伪标注，避免把低熵直接当作高可信。见表 3。

<a id="paper-almc-nullspace-retained-view-updates"></a>

## Anti-Degradation Lifelong Multi-View Clustering

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Anti-Degradation_Lifelong_Multi-View_Clustering_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Anti-Degradation_Lifelong_Multi-View_Clustering_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 新增视图的梯度可能改坏旧视图的聚类空间，仅对齐现有分布不足以确保旧结构保持。
- **核心创新 / 方法** · 以保存的表征知识定义零空间，只允许新更新沿与旧知识正交的方向改变，并配合结构保持目标。
- **Baseline** · 与 DSVC、ICMVC、MCMVC 等对照，表 3 同框架比较去掉零空间投影以及其他损失。
- **Benchmark** · Oxford4、ALOI-10、NUS 等持续多视图聚类，以 ACC 与 NMI 评估。
- **关键结果 / 消融** · 表 3 的 ALOI-10 去掉零空间投影时 ACC、NMI 为 76.92、80.08，完整设置为 90.90、87.32。
- **适用条件 / 局限** · 约束基于可保存的近似旧子空间，若有效子空间逐渐占满，新视图可使用的方向会收缩。

**可复用机制** · 持续新增视图时，可把更新限制在旧表征的零空间，再与同模型不投影的版本比较聚类稳定性。见表 3。

<a id="paper-fedsdr-spectral-fidelity-client-aggregation"></a>

## FedSDR: Federated Graph Learning with Structural Noise Detection and Reconstruction

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_FedSDR_Federated_Graph_Learning_with_Structural_Noise_Detection_and_Reconstruction_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_FedSDR_Federated_Graph_Learning_with_Structural_Noise_Detection_and_Reconstruction_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 节点关系记录不可靠会使图网络邻域传播偏离，并通过聚合影响其他客户端。
- **核心创新 / 方法** · 用谱结构保真度调整客户端上行权重，同时在客户端重建结构以改善本地传播。
- **Baseline** · 对照 FedAvg、其他联邦图方法，以及只用聚合或只做重建的消融。
- **Benchmark** · PubMed、Actor、ogbn-products 的非独立同分布子图任务，报告节点分类准确率与不同结构噪声水平。
- **关键结果 / 消融** · 表 2 的 ogbn-products 无两模块为 72.66%，只加聚合为 74.25%，只加重建为 75.92%，完整 78.57%。
- **适用条件 / 局限** · 结构保真度低也可能表示真实分布差异，应用到异质图时需检验是否压低有价值的少数客户端。

**可复用机制** · 联邦图协作时可单独比较结构质量加权聚合和本地拓扑重建，分清全局与客户端收益。见表 2。

<a id="paper-speede3dgs"></a>

## SpeeDe3DGS: Speedy Deformable 3D Gaussian Splatting with Temporal Pruning and Motion Grouping

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Tu_SpeeDe3DGS_Speedy_Deformable_3D_Gaussian_Splatting_with_Temporal_Pruning_and_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Tu_SpeeDe3DGS_Speedy_Deformable_3D_Gaussian_Splatting_with_Temporal_Pruning_and_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 动态3DGS 对每个高斯执行神经形变，限制实时渲染。
- **核心创新 / 方法** · 按时间聚合敏感度裁剪，扰动时间戳训练以减轻漂浮点，再以 GroupFlow 得到共享 SE(3) 变换。
- **Baseline** · 基于 DeformableGS，表2也在4DGS上累积加入组件。
- **Benchmark** · NeRF-DS 七真实场景，MonoDyGauBench 五数据集50场景，比较渲染速度、训练耗时和画质。
- **关键结果 / 消融** · 正文报告 DeformableGS 加两项时间机制后平均渲染加速6.78倍，加入 GroupFlow 后13.71倍。
- **适用条件 / 局限** · 依赖运动可被分组近似为刚体，细薄且快速非刚性形变需单测。

**可复用机制** · 动态场景可先按跨时间贡献裁剪，再把多点的形变蒸馏为共享刚体运动。

<a id="paper-scar-semantic-context"></a>

## Semantic Context Matters: Improving Conditioning for Autoregressive Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Jin_Semantic_Context_Matters_Improving_Conditioning_for_Autoregressive_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Jin_Semantic_Context_Matters_Improving_Conditioning_for_Autoregressive_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 仅在解码阶段注入条件，或用密集视觉 token 作前缀，会遗漏高层语义或增加开销。
- **核心创新 / 方法** · 压缩预填充中的语义表示，解码时用末端视觉状态对齐目标语义。
- **Baseline** · 表1比较 next-token、next-set，表2基于 LlamaGen-XL，表3包含重训 ControlAR。
- **Benchmark** · ImageNet 条件生成、MultiGen-20M 深度/边缘控制及 PIE-Bench 编辑，报告 FID、控制一致性与 CLIP 等。
- **关键结果 / 消融** · 表2跨四种控制类型比较画质与条件一致性，表5比较压缩率。
- **适用条件 / 局限** · 需能取得可靠的目标语义，压缩前缀不足以保证小区域和低层条件被保留。

**可复用机制** · 自回归视觉编辑可同时压缩语义前缀，并使解码隐藏状态对齐目标语义。

<a id="paper-sra-det"></a>

## SRA-Det: Learning Omni-Grained Open-Vocabulary Detection Beyond Category Names

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_SRA-Det_Learning_Omni-Grained_Open-Vocabulary_Detection_Beyond_Category_Names_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yang_SRA-Det_Learning_Omni-Grained_Open-Vocabulary_Detection_Beyond_Category_Names_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 按类别名称匹配的检测器难区分同类对象的颜色、材质或纹理。
- **核心创新 / 方法** · 从文本 token 检索多个语义分面，使用 soft-min 匹配模拟逻辑 AND，并利用筛验的属性标注训练。
- **Baseline** · 表1–2比较既有开放词汇检测器，表3加入 MLLM。
- **Benchmark** · LVIS minival 按频率组报 AP，FG-OVD 八子集报细粒度检测。
- **关键结果 / 消融** · Swin-T 达 FG-OVD 零样本54.9 mAP、LVIS 40.4 AP。
- **适用条件 / 局限** · soft-min 可能对噪声属性过于敏感，含可选条件、否定或逻辑 OR 的查询需单测。

**可复用机制** · 组合检索或检测含多个必要属性时，评估可微合取，防止一项高分掩盖缺少的约束。

<a id="paper-rescene4d"></a>

## ReScene4D: Temporally Consistent Semantic Instance Segmentation of Evolving Indoor 3D Scenes

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Steiner_ReScene4D_Temporally_Consistent_Semantic_Instance_Segmentation_of_Evolving_Indoor_3D_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Steiner_ReScene4D_Temporally_Consistent_Semantic_Instance_Segmentation_of_Evolving_Indoor_3D_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 独立分割再匹配不利用跨次语义，高频跟踪假设又不符合间歇重扫。
- **核心创新 / 方法** · 在3D实例分割器中用时空对比损失、掩码和序列化跨扫描分享信息。
- **Baseline** · 表1比较时序实例分割对照，表2比较逐阶段3D预测，表3拆解时序共享策略。
- **Benchmark** · 3RScan 18类，不同 IoU 阈值的时序 t-mAP 和3D mAP。
- **关键结果 / 消融** · 表1–2同时评估跨扫描身份一致性和单次分割，表3区分时空组件。
- **适用条件 / 局限** · 要求存在足够重叠的室内扫描和可用于训练的时序关联，长间隔重现、剧烈布局变化需复验。

**可复用机制** · 低频观测的对象跟踪可把跨次扫描的关联融入分割训练，并用带身份约束的指标检验。

<a id="paper-lite-vggt"></a>

## LiteVGGT: Boosting Vanilla VGGT via Geometry-aware Cached Token Merging

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Shu_LiteVGGT_Boosting_Vanilla_VGGT_via_Geometry-aware_Cached_Token_Merging_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Shu_LiteVGGT_Boosting_Vanilla_VGGT_via_Geometry-aware_Cached_Token_Merging_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · VGGT 长序列的全局注意和相似度计算在数百张图像下开销高。
- **核心创新 / 方法** · 用几何重要性挑选合并锚点，缓存相邻层可复用的 token 合并索引。
- **Baseline** · 基于原 VGGT，正文比较几何重建对照，另验证微调与 FP8。
- **Benchmark** · ScanNet-50、7 Scenes、NRGBD、Tanks & Temples，比较点云质量、耗时和显存可用性。
- **关键结果 / 消融** · 官方正文报告最高约10倍加速并处理1000张图的场景，表1–4量化质量和时延。
- **适用条件 / 局限** · 缓存依赖层间特征近邻保持稳定，低重叠或跨层几何特征改变时应重算并验质量。

**可复用机制** · 长多视图网络先测相邻层合并决策是否稳定，再缓存索引，避免重复匹配。

<a id="paper-homography-verification"></a>

## Lipschitz Optimization for Formal Verification of Homographies

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Durand_Lipschitz_Optimization_for_Formal_Verification_of_Homographies_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Durand_Lipschitz_Optimization_for_Formal_Verification_of_Homographies_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 常见像素范数或仿射认证未覆盖投影成像变化。
- **核心创新 / 方法** · 从相机位姿推导像素映射，利用单应连续性和 Lipschitz 优化计算线性像素界。
- **Baseline** · 表1与 PWL 比较，表2非仿射扰动认证，表3–4测试偏航与填充。
- **Benchmark** · MNIST、CIFAR-10 的变换下认证比例及验证时间。
- **关键结果 / 消融** · 表2表明既有 PGD 训练并不保证对3D相机运动的认证；表3–4考察角度和填充。
- **适用条件 / 局限** · 平面假设限制对明显视差或被遮挡内容的适用性，完整分支定界运行时间也可能较高。

**可复用机制** · 对近似平面视觉任务，把相机位姿扰动直接编码进形式验证范围。

<a id="paper-planner-rft"></a>

## PlannerRFT: Reinforcing Diffusion Planners through Closed-Loop and Sample-Efficient Fine-Tuning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_PlannerRFT_Reinforcing_Diffusion_Planners_through_Closed-Loop_and_Sample-Efficient_Fine-Tuning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_PlannerRFT_Reinforcing_Diffusion_Planners_through_Closed-Loop_and_Sample-Efficient_Fine-Tuning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 固定锚点或普通扩散采样容易重复不适合当前场景的轨迹，奖励利用效率低。
- **核心创新 / 方法** · 双分支同时更新轨迹分布与去噪探索策略；训练使用并行闭环仿真。
- **Baseline** · 表1比较 Diffusion Planner、Flow Planner 等，表2用相同5步 DDIM 比较探索，表3–4消融数据和奖励。
- **Benchmark** · 闭环规划在 NR/R 设置下比较，表2看采样多模态性和奖励统计。
- **关键结果 / 消融** · 表1四列均优于 Diffusion Planner，最后一列由69.22升至72.21；表2在相同采样步数下对照引导策略。
- **适用条件 / 局限** · 闭环证据依赖仿真和奖励设计，硬件上更换动力学或安全约束须复验。

**可复用机制** · 闭环奖励稀疏时，训练阶段专门控制去噪探索分布并保留部署路径。

<a id="paper-dynamic-attention-sae"></a>

## Improving Sparse Autoencoder with Dynamic Attention

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Improving_Sparse_Autoencoder_with_Dynamic_Attention_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_Improving_Sparse_Autoencoder_with_Dynamic_Attention_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 固定稀疏预算在不同输入上难兼顾可解释性与恢复。
- **核心创新 / 方法** · 让潜特征查询可学习字典键值，以 sparsemax 激活生成稀疏概念子集。
- **Baseline** · 与 ReLU、TopK 等稀疏自编码器设定比较，改变字典大小。
- **Benchmark** · OpenWeb、WikiText-103 测 NMSE 与交叉熵退化，ImageNet 做消融。
- **关键结果 / 消融** · 表1–3比较适应性稀疏的重建、语言性能改变与视觉消融。
- **适用条件 / 局限** · 字典规模、训练稳定和概念解释仍需分别检验，自动稀疏不会保证语义可分。

**可复用机制** · 训练稀疏自编码器时，用 sparsemax 求输入依赖的激活数量，比较固定 TopK。

<a id="paper-switchcraft-event-aligned-steering"></a>

## SwitchCraft: Training-Free Multi-Event Video Generation with Attention Controls

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_SwitchCraft_Training-Free_Multi-Event_Video_Generation_with_Attention_Controls_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_SwitchCraft_Training-Free_Multi-Event_Video_Generation_with_Attention_Controls_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 同一文本作用在全部帧会混合不同事件，强行隔离又可能损伤转场。
- **核心创新 / 方法** · 用帧级查询引导注意力到相应事件，自动调节强度保持过渡。
- **Baseline** · 对比标准生视频及已有多事件条件方法，表1做消融。
- **Benchmark** · 多事件提示视频，量化文本对齐、时序平滑；人评关注漏项、串扰。
- **关键结果 / 消融** · 表1–2对比事件完整性、对齐和时序质量。
- **适用条件 / 局限** · 要求能把事件映射到时间段，重叠事件和不确定顺序可能降低适用性。

**可复用机制** · 多事件视频按帧段注入各自事件条件，并动态控制强度以维持时间连贯。

<a id="paper-hificl-virtual-kv"></a>

## HiFICL: High-Fidelity In-Context Learning for Multimodal Tasks

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_HiFICL_High-Fidelity_In-Context_Learning_for_Multimodal_Tasks_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_HiFICL_High-Fidelity_In-Context_Learning_for_Multimodal_Tasks_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 用一个固定偏移向量无法模拟示例对不同查询的动态权重。
- **核心创新 / 方法** · 根据注意力分解构造低秩可训虚拟键和值，再做端到端训练。
- **Baseline** · 现有偏移向量近似和原始上下文演示设置。
- **Benchmark** · 多模态任务与 COCO Captioning；表3用 Idefics2 分析生成幻觉。
- **关键结果 / 消融** · 原文报告在多项任务超出之前近似，并检查提示替代的幻觉风险。
- **适用条件 / 局限** · 虚拟上下文依赖任务训练，遇到新任务或演示变化时可能仍需适配。

**可复用机制** · 近似多模态示例学习时，拟合虚拟键值以保留依查询而变的注意力分量。

<a id="paper-binaural-spatial-reasoning"></a>

## Hear you are: Teaching LLMs Spatial Reasoning with Vision and Spatial Sound

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Ryu_Hear_you_are_Teaching_LLMs_Spatial_Reasoning_with_Vision_and_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Ryu_Hear_you_are_Teaching_LLMs_Spatial_Reasoning_with_Vision_and_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 现有语义或时间配对任务可用声音类别捷径完成，不能确认是否会声源定位。
- **核心创新 / 方法** · 构造必须根据空间吻合或多个同类声源消歧的问题，比较不同模态信号。
- **Baseline** · 对照 RGB、单声道、双耳等输入组合及原有模型。
- **Benchmark** · 空间视听问答和声源定位，按题型比较正确性。
- **关键结果 / 消融** · 原文表2区分不同模态输入在需空间理解题目上的表现。
- **适用条件 / 局限** · 双耳线索取决于采集几何，房间声学、传感配置与合成题迁移需复核。

**可复用机制** · 验证视听空间推理时设置语义不匹配但位置吻合的样本，并比较双耳和单声道。

<a id="paper-energy-wave-test-time-adaptation"></a>

## Energy Waveify and Redistribution for Test-Time Adaptation: A Control System Perspective

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Energy_Waveify_and_Redistribution_for_Test-Time_Adaptation_A_Control_System_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_Energy_Waveify_and_Redistribution_for_Test-Time_Adaptation_A_Control_System_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 蒙特卡洛或 Langevin 近似需要对每实例反复采样，部署延时高。
- **核心创新 / 方法** · 将能量表示为复值波，以随时间演化及概率流守恒作不含额外随机采样的适配。
- **Baseline** · 以 WRN-28-10、ResNet-50 等，比现有能量式和其他测试适配方法。
- **Benchmark** · CIFAR-10-C、CIFAR-100-C、TinyImageNet-200-C 的图像扰动，另测 PACS 域泛化。
- **关键结果 / 消融** · 表1–3报告准确率，正文比较不经额外采样的适配开销。
- **适用条件 / 局限** · 依赖所设能量动力学与目标域的连续性，突变和预测高置信错误时需验证。

**可复用机制** · 能量式测试时适配可检验确定性概率流更新能否减少逐样本随机采样。

<a id="paper-olmoearth-modality-masked-latent-modeling"></a>

## OlmoEarth: Stable Latent Image Modeling for Multimodal Earth Observation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Herzog_OlmoEarth_Stable_Latent_Image_Modeling_for_Multimodal_Earth_Observation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Herzog_OlmoEarth_Stable_Latent_Image_Modeling_for_Multimodal_Earth_Observation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 空间、时间和不同传感器混合的数据存在缺失模态，直接随机遮盖的潜空间建模可能失稳。
- **核心创新 / 方法** · 在简化的潜空间遮盖建模上加入模态遮盖，再逐步加入模态内块判别和跨模态对比目标。
- **Baseline** · 表 4 对照标准 Latent MIM、轻量版，以及连续添加模态遮盖与其他训练目标的配置。
- **Benchmark** · 三组消融验证使用 m-So2Sat、m-EuroSAT、PASTIS 的近邻或线性探针；正文还按任务评估微调。
- **关键结果 / 消融** · 表 4 的标准 Latent MIM 出现坍塌；在 Lite 上增加模态遮盖后，m-So2Sat 从 42.2 到 53.6，PASTIS 从 35.2 到 46.6。
- **适用条件 / 局限** · 依赖模态间存在可预测的互补信号；嵌入任务上的大模型收益并不稳定，一次逐步消融不能说明所有配置可加。

**可复用机制** · 多传感器预训练可优先实测整模态遮盖，并区分潜空间预测方案本身是否存在训练坍塌。见表 4。

<a id="paper-infinibench-irrelevant-object-spatial-stress-test"></a>

## InfiniBench: Infinite Benchmarking for Visual Spatial Reasoning with Customizable Scene Complexity

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_InfiniBench_Infinite_Benchmarking_for_Visual_Spatial_Reasoning_with_Customizable_Scene_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_InfiniBench_Infinite_Benchmarking_for_Visual_Spatial_Reasoning_with_Customizable_Scene_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 整体复杂度评分难以判断模型是在度量、视角变化还是跨时间追踪阶段出错。
- **核心创新 / 方法** · 用可调的三维场景合成管线控制无关物体与观察条件，分项比较跟踪、度量和视角任务。
- **Baseline** · 同一模型跨低、中、高无关物体比例的比较，包含 Gemini 2.5 Pro、GPT-5、InternVL 等。
- **Benchmark** · InfiniBench 的度量、视角转换和时空推理任务，以合成视频问答准确率衡量。
- **关键结果 / 消融** · 表 5 的 Gemini 2.5 Pro 时空题从 87.9 降到 56.2，度量题从 69.2 至 66.4，说明无关物体对不同任务的作用相差较大。
- **适用条件 / 局限** · 场景与问答由合成管线控制，需在实采视频验证纹理、遮挡和计数干扰是否得到相同排序。

**可复用机制** · 空间推理测试可固定目标关系，只分别改变无关物体数，避免总体分数掩盖对时空跟踪的特定影响。见表 5。

<a id="paper-dicart-discrete-kinematic-pose-diffusion"></a>

## DICArt: Advancing Category-level Articulated Object Pose Estimation in Discrete State-Spaces

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_DICArt_Advancing_Category-level_Articulated_Object_Pose_Estimation_in_Discrete_State-Spaces_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_DICArt_Advancing_Category-level_Articulated_Object_Pose_Estimation_in_Discrete_State-Spaces_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 关节物体逐部件回归面对大的连续搜索空间，也可能输出互相不符合运动学的位姿。
- **核心创新 / 方法** · 在离散姿态状态中按条件去噪，根据状态决定去噪或重置，并按对象运动链层次估计刚性部件。
- **Baseline** · 与连续扩散、移除重新定义的去噪流程及现有类别级位姿方法对照。
- **Benchmark** · ArtImage、ReArtMix 和七部件 RobotArm，评价逐部件旋转与平移误差。
- **关键结果 / 消融** · 表 2 Drawer 的连续扩散为 3.1 度与 0.143 米，离散扩散为 1.7 度与 0.072 米。
- **适用条件 / 局限** · 离散粒度和运动链结构影响精度，拓扑未知或自由度增加时需重新检验搜索和量化误差。

**可复用机制** · 估计具有运动学约束的姿态时，可对照离散扩散与连续扩散，并用部件间层次关系减少独立搜索。见表 2。

<a id="paper-affordgen-geometry-demonstration-budget"></a>

## AffordGen: Generating Diverse Demonstrations for Generalizable Object Manipulation with Affordance Correspondence

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_AffordGen_Generating_Diverse_Demonstrations_for_Generalizable_Object_Manipulation_with_Affordance_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_AffordGen_Generating_Diverse_Demonstrations_for_Generalizable_Object_Manipulation_with_Affordance_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 机器人模仿学习即使有大量增强演示，也可能因为物体形状覆盖不足而无法迁移到新对象。
- **核心创新 / 方法** · 在生成的物体网格之间找语义功能关键点对应，迁移示教轨迹并训练闭环策略。
- **Baseline** · 比较 DemoGen、CPGen，以及在 1000 条轨迹预算内改变每个网格的演示数与网格数。
- **Benchmark** · 仿真倒水、挂杯、切割和对齐任务以及真实机器人任务，区分源对象与未见对象的成功率。
- **关键结果 / 消融** · 表 1 未见倒水对象的成功率在 50 网格×20 轨迹为 0.553，1000×1 为 0.242，DemoGen 的 1×1000 为 0.131。
- **适用条件 / 局限** · 需要可信的功能点对应与可执行迁移轨迹；不同任务的最佳预算分配不同，不能直接固定同一比例。

**可复用机制** · 示教增强时可固定总轨迹数，分别试验多对象网格与每对象多轨迹如何分配预算。见表 1。

<a id="paper-oacir-instance-anchor-retrieval"></a>

## Beyond Semantic Search: Towards Referential Anchoring in Composed Image Retrieval

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_Beyond_Semantic_Search_Towards_Referential_Anchoring_in_Composed_Image_Retrieval_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yang_Beyond_Semantic_Search_Towards_Referential_Anchoring_in_Composed_Image_Retrieval_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 图文组合检索往往把类别相似当作正确，容易返回外观相近但不同的具体实例。
- **核心创新 / 方法** · 用参考图上的框明确锚定对象，以上下文感知局部适配保持目标实例与文本修改的联合约束。
- **Baseline** · 比较不加 CAAM、池化、MLP 与 Transformer 调制，并消融查询标记是否可学习。
- **Benchmark** · OACIRR 的多域真实图片与相似实例干扰图库，使用 RID@1、标准 R@1 与 R@5。
- **关键结果 / 消融** · 表 3 无 CAAM 时 RID@1、R@1 为 77.74、58.39；Transformer 与可学习标记组合为 82.59、62.88。
- **适用条件 / 局限** · 依赖准确的选框和可辨识的实例特征，严重遮挡和物体没有稳定外观时仍需重测。

**可复用机制** · 当检索必须找回同一实例，可在查询中提供显式局部锚点，并对相似实例干扰单列身份召回。见表 3。

<a id="paper-uplift-local-attender-iterative-feature-upsampling"></a>

## UPLiFT: Efficient Pixel-Dense Feature Upsampling with Local Attenders

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Walmer_UPLiFT_Efficient_Pixel-Dense_Feature_Upsampling_with_Local_Attenders_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Walmer_UPLiFT_Efficient_Pixel-Dense_Feature_Upsampling_with_Local_Attenders_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 高分辨率骨干特征计算昂贵，上采样中的全局跨注意力也会随像素增长。
- **核心创新 / 方法** · 以局部注意算子逐次将低分辨率特征增密，并在训练中反复应用模块，匹配高分辨率特征。
- **Baseline** · 比较最近邻、双线性、LiFT、FeatUp、LoftUp、JAFAR 与 AnyUp。
- **Benchmark** · COCO、VOC、ADE20K、Cityscapes 语义分割 mIoU 和像素准确率、COCO 深度的 δ1 与 RMSE，以及毫秒时延。
- **关键结果 / 消融** · 表 1 UPLiFT 用时 79.4 毫秒，Cityscapes mIoU 65.38；AnyUp 为 146.7 毫秒、61.33，两者深度 RMSE 都是 0.63。
- **适用条件 / 局限** · 仍慢于简单插值，需要有可用于训练监督的骨干高分辨率特征；换倍率和输入尺寸时需复查细结构。

**可复用机制** · 稠密下游任务可比较逐级局部上采样和大规模跨注意力，联合看时延、分割精度与深度误差。见表 1。

<a id="paper-self1e"></a>

## Rethinking MLLM Itself as a Segmenter with a Single Segmentation Token

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Rethinking_MLLM_Itself_as_a_Segmenter_with_a_Single_Segmentation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Rethinking_MLLM_Itself_as_a_Segmenter_with_a_Single_Segmentation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · MLLM 压缩图像特征降低掩码空间分辨率，以往多依赖专用解码器。
- **核心创新 / 方法** · 保留原分辨率视觉特征，加入经 MLLM 处理的压缩特征残差并用 pixel-unshuffle 暴露细节，由单个分割 token 表达目标。
- **Baseline** · 表1标注是否用专门解码器和单 token，表2–4比较其他分割方法。
- **Benchmark** · RefCOCO/+/g 的 cIoU、广义指代分割及开放词汇分割。
- **关键结果 / 消融** · 表1 未采用专用头的单 token 模型达到有竞争力的结果，表2补充广义指代评估。
- **适用条件 / 局限** · 需访问未压缩视觉特征和压缩变换，极小目标或超长图文上下文的开销需另测。

**可复用机制** · 想去掉外部分割头时，保留未压缩视觉网格，并把语言侧语义作为残差补回。

<a id="paper-temporal-adjusted-loss"></a>

## Temporal Imbalance of Positive and Negative Supervision in Class-Incremental Learning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Ma_Temporal_Imbalance_of_Positive_and_Negative_Supervision_in_Class-Incremental_Learning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Ma_Temporal_Imbalance_of_Positive_and_Negative_Supervision_in_Class-Incremental_Learning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 越早出现的类在后续任务中承受更长时间的负监督，最终偏向新类别。
- **核心创新 / 方法** · 用时间衰减核构建类别监督强度向量，动态调整交叉熵中的负监督。
- **Baseline** · 表1比较同增量方法加与不加 TAL，所有对照每类回放20个样本；表2调整核参数。
- **Benchmark** · CIFAR-100、ImageNet-100、Food101，10及20任务的平均准确率与最终准确率。
- **关键结果 / 消融** · 正文理论表明平衡时回到标准交叉熵，表1覆盖三数据集多个增量方法。
- **适用条件 / 局限** · 依赖已知任务历史，任务边界模糊、无回放或类频率突变时需验证。

**可复用机制** · 类别分期到达时，统计旧类被当负样本的累计监督，再决定是否重加权交叉熵。

<a id="paper-global-edge-prior"></a>

## Global-Aware Edge Prioritization for Pose Graph Initialization

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wei_Global-Aware_Edge_Prioritization_for_Pose_Graph_Initialization_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wei_Global-Aware_Edge_Prioritization_for_Pose_Graph_Initialization_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 独立检索近邻可能聚集在相似视图，留下弱连接或过大的图直径。
- **核心创新 / 方法** · 以 GNN 预测全局可靠边，按多最小生成树组图，再按连通性调分。
- **Baseline** · 表1比较 MegaLoc 相似度与预测边排序，表3比较 SALAD、去掉 GNN 和 oracle 对照。
- **Benchmark** · VisymScenes 位姿 AUC@5°，PhotoTourism 几何重建与组件对照。
- **关键结果 / 消融** · 表1逐列比较开关连通性调分，表3显示移除 GNN 会降低整体排序表现。
- **适用条件 / 局限** · 仍受检索候选池限制，真实跨区域边没入池时重排不能补回。

**可复用机制** · 昂贵几何验证前按全图约束排序候选边，优先补弱连通区域而非仅做节点最近邻。

<a id="paper-adaptvision"></a>

## AdaptVision: Efficient Vision-Language Models via Adaptive Visual Acquisition

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Lin_AdaptVision_Efficient_Vision-Language_Models_via_Adaptive_Visual_Acquisition_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Lin_AdaptVision_Efficient_Vision-Language_Models_via_Adaptive_Visual_Acquisition_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 固定比率缩减视觉 token 无法适应图像问题对细节的需求差异。
- **核心创新 / 方法** · 先看低分辨率图，在需要时用框工具获取局部高分辨率区域；DTPO 分别优化工具回合与答题。
- **Baseline** · 表1比较原生 Qwen2.5-VL-7B-Instruct、下采样、既有压缩与去掉 DTPO。
- **Benchmark** · 表1跨视觉问答和理解评测比较相对表现及 token 比率，图4测推理时间。
- **关键结果 / 消融** · 表1使用33%视觉 token 保留97.9%平均相对性能，去掉 DTPO 时需57% token 且平均96.7%。
- **适用条件 / 局限** · 依赖可靠裁剪与工具调用开销低，跨远距离区域的关系可能需要多次观察。

**可复用机制** · 按问题主动获取视觉细节，把何时裁剪与答题质量的优化信号分开。

<a id="paper-geometry-driven-ood-heads"></a>

## Geometry-driven OOD Detectors Are Class-Incremental Learners

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Jia_Geometry-driven_OOD_Detectors_Are_Class-Incremental_Learners_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Jia_Geometry-driven_OOD_Detectors_Are_Class-Incremental_Learners_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 线性或余弦头可能把未知样本归进旧类，难通过每个任务自己的阈值区分。
- **核心创新 / 方法** · 固定等角紧框架锚点，以 ETF 损失和 ArcFace 分别约束分离与紧致。
- **Baseline** · 表1比较 DS-AL、Aper、EASE、NC-CIPM、LoRA-DRS 等无样本回放方法，表3比较 top-k。
- **Benchmark** · CIFAR-100、ImageNet-A/R、Stanford Cars 的平均增量准确率与末任务准确率，含5或10任务。
- **关键结果 / 消融** · 表1多数据集比较增量性能，表2在 ImageNet-A 比较计算与内存，GOD 可训练参数2.64M。
- **适用条件 / 局限** · 每任务接收分数须可比较，高重合新旧类可能削弱域外拒绝，应报告阈值敏感性。

**可复用机制** · 增量分类可将任务头同时训练成域内分类器与域外拒绝器，并联合考察类间分离和类内紧致。

<a id="paper-realign-forgery-detection"></a>

## ReAlign: Generalizable Image Forgery Detection via Reasoning-Aligned Representation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_ReAlign_Generalizable_Image_Forgery_Detection_via_Reasoning-Aligned_Representation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_ReAlign_Generalizable_Image_Forgery_Detection_via_Reasoning-Aligned_Representation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 轻量检测器擅长视觉伪影，复杂模型能抓语义不一致但推理更慢。
- **核心创新 / 方法** · 从用 GRPO 优化的教师获取解释，再以跨模态对比学习蒸馏到轻量检测器。
- **Baseline** · 表1–3比较 CNNSpot、UniFD、AIDE 和 AIGI-R1 等，表4按监督文本类型消融。
- **Benchmark** · AIGCDetectBenchmark、AIGI-Holmes、UltraSynth-10k，按生成器分组报告分类准确率。
- **关键结果 / 消融** · 表3新生成器集合平均准确率97.09%，表4对比推理文本与类别标签等。
- **适用条件 / 局限** · 教师解释可能沿用生成器偏差，遇到照片后期编辑或未见生成方式应分别评估。

**可复用机制** · 只在训练使用教师提供语义异常解释，用对比蒸馏比较解释、描述和类别标签的贡献。

<a id="paper-sad-tm-saliency-merging"></a>

## Saliency-Driven Token Merging for Vision Transformers

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xie_Saliency-Driven_Token_Merging_for_Vision_Transformers_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xie_Saliency-Driven_Token_Merging_for_Vision_Transformers_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 注意力特征变化大，尤其早层类注意力还未稳定。
- **核心创新 / 方法** · 结合注意力相似与输入显著性，用显著性相对全局方向的异常辅助决定合并。
- **Baseline** · 对照其他无训练词元合并与同骨干未压缩版。
- **Benchmark** · DeiT-Small、DeiT-Tiny、MAE-Huge 等视觉模型，比较识别准确性及压缩开销。
- **关键结果 / 消融** · 表1–3给出不同骨干上的速度准确率结果，原文分析推迟早层合并。
- **适用条件 / 局限** · 显著性异常不总代表可丢弃，稀有前景和精定位任务需单独验证。

**可复用机制** · 免训练裁并视觉词元时，将输入显著性异常作为补充，并推迟早层的合并。

<a id="paper-fastgs-multiview-consistency"></a>

## FastGS: Training 3D Gaussian Splatting in 100 Seconds

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Ren_FastGS_Training_3D_Gaussian_Splatting_in_100_Seconds_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Ren_FastGS_Training_3D_Gaussian_Splatting_in_100_Seconds_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 训练中无效或重复高斯会拖慢渲染，数量目标又无法区分重要性。
- **核心创新 / 方法** · 根据多视图一致性设计增密和剪枝，直接调节训练中实际图元。
- **Baseline** · DashGaussian、标准3DGS 及已有快速优化方案。
- **Benchmark** · Mip-NeRF 360、Tanks & Temples、Deep Blending，测训练时间及渲染质量，外加动态重建。
- **关键结果 / 消融** · 相较 DashGaussian，Mip-NeRF 360 约3.29倍加速；Deep Blending 相对标准 3DGS 约15.45倍。
- **适用条件 / 局限** · 收益和质量取决于视点覆盖，少数视图独有的薄结构可能被误剪。

**可复用机制** · 三维高斯训练时使用多视图一致性定新增和剪枝优先级，而非先锁定统一数量预算。

<a id="paper-learning-from-itself-clip-continual"></a>

## Learning from Itself: Mining Internal Knowledge from Vision Language Models for Continual Learning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Gong_Learning_from_Itself_Mining_Internal_Knowledge_from_Vision_Language_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Gong_Learning_from_Itself_Mining_Internal_Knowledge_from_Vision_Language_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 类别名与预训练描述分布不同，单视觉和图文支路在自然图与细粒度任务各有所长。
- **核心创新 / 方法** · 在模型自身对比目标下优化伪描述词元，另让临时视觉头与文本分类做性能加权的双向蒸馏。
- **Baseline** · OpenAI CLIP、OpenCLIP 上比较持续学习基线及目标消融。
- **Benchmark** · 五套持续学习数据的10任务和6任务设置，比较准确性。
- **关键结果 / 消融** · 表1–3比较双向蒸馏与伪描述效果；部署只用原图文架构。
- **适用条件 / 局限** · 瞬时准确率会受样本噪声影响，强支路的偏差也可能蒸馏到弱支路。

**可复用机制** · 持续适配图文模型时，根据当前强弱动态调整视觉分类支路与文本支路之间的蒸馏方向。

<a id="paper-veason-r1-sequential-segmentation"></a>

## Reinforcing Video Object Segmentation to Think before it Segments

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Gong_Reinforcing_Video_Object_Segmentation_to_Think_before_it_Segments_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Gong_Reinforcing_Video_Object_Segmentation_to_Think_before_it_Segments_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 压到单个分割词元难区分时序选错、目标找错与掩码传播错误。
- **核心创新 / 方法** · 先模仿层次化步骤，再以 GRPO 用时间、空间和跨帧三类反馈优化。
- **Baseline** · 与现有视频推理分割和仅监督训练策略比较。
- **Benchmark** · ReVOS、ReasonVOS、MeViS 的视频目标分割。
- **关键结果 / 消融** · 表1–3报告单来源训练的跨基准表现，正文比较奖励设计。
- **适用条件 / 局限** · 依赖传播器和关键帧标签，遮挡或多个同样适合帧时评分会不稳定。

**可复用机制** · 视频分割需要多步推理时，把关键帧选择、框定位和传播一致性变成分别可核查的奖励。

<a id="paper-edit-as-act-goal-regressive"></a>

## Edit-As-Act: Goal-Regressive Planning for Open-Vocabulary 3D Indoor Scene Editing

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Noh_Edit-As-Act_Goal-Regressive_Planning_for_Open-Vocabulary_3D_Indoor_Scene_Editing_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Noh_Edit-As-Act_Goal-Regressive_Planning_for_Open-Vocabulary_3D_Indoor_Scene_Editing_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 全局重生成或二维改图可能改动无关空间和破坏接触支撑。
- **核心创新 / 方法** · 编译目标谓词，以带前置条件及效果的动作语言规划，并由几何验证器检查。
- **Baseline** · 对照生成编辑与现有推理规划方案。
- **Benchmark** · 九类室内场景及指令，评估编辑结果、物理可行和未触及内容。
- **关键结果 / 消融** · 表2–3报告跨类结果及同任务规划比较。
- **适用条件 / 局限** · 依赖谓词及动作库覆盖和既有几何正确，无法直接表达开放式材质或模糊风格编辑。

**可复用机制** · 编辑三维环境时先写目标状态，再反向规划最少可验操作，保留未涉及对象。

<a id="paper-videocups-video-droploss"></a>

## Scene-Centric Unsupervised Video Panoptic Segmentation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Reich_Scene-Centric_Unsupervised_Video_Panoptic_Segmentation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Reich_Scene-Centric_Unsupervised_Video_Panoptic_Segmentation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 无标注视频中深度、运动及空间分割提示会互相冲突。
- **核心创新 / 方法** · 利用深度与运动等生成跨帧伪标签，再通过 Video DropLoss 学习时序全景。
- **Baseline** · 四个从无监督图像全景和视频实例方法扩展来的基线。
- **Benchmark** · Cityscapes-VPS 验证及域外泛化，报告 STQ、AQ 等。
- **关键结果 / 消融** · 表1–3比较性能和伪标签生成组件的贡献。
- **适用条件 / 局限** · 损失过滤可能压制遮挡及少见类别，深度和运动错误仍会传播。

**可复用机制** · 时序全景伪标签噪声大时，在训练损失侧排除不可靠监督，并单独评估关联和语义。

<a id="paper-b3seg-information-gain-view-selection"></a>

## B$^3$-Seg: Camera-Free, Training-Free 3DGS Segmentation via Analytic EIG and Beta-Bernoulli Bayesian Updates

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Kamata_B3-Seg_Camera-Free_Training-Free_3DGS_Segmentation_via_Analytic_EIG_and_Beta-Bernoulli_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Kamata_B3-Seg_Camera-Free_Training-Free_3DGS_Segmentation_via_Analytic_EIG_and_Beta-Bernoulli_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 重建后的三维分割若依赖原相机视角或均匀采样，模糊区域可能得不到新增证据。
- **核心创新 / 方法** · 以 Beta–Bernoulli 后验累积视角提供的掩膜证据，按解析期望信息增益顺序挑选视角。
- **Baseline** · 与 FlashSplat 的均匀球面采样和重建相机采样比较；需要标注或重训的方法仅作背景。
- **Benchmark** · LERF-Mask 与 3D-OVS，使用 mIoU、边界 mBIoU、视角预算和运行时间。
- **关键结果 / 消融** · 表 1 的 20 视角下，B3-Seg 为 84.5 mIoU、12.1 秒，FlashSplat 的重建相机采样为 76.5、10.1 秒，球面采样为 69.6、10.2 秒。
- **适用条件 / 局限** · 信息增益依赖可见性、候选视角和上游掩膜；已有几何重建偏差可能使置信度计算过度乐观。

**可复用机制** · 需要主动挑选有限视角时，可按可见点的预期后验信息增益选下一视角，与固定或重建视角采样对照。见表 1 和第 5.4 节。

<a id="paper-causal-ot-cross-channel-alignment"></a>

## Towards Uncertainty-aware Unsupervised Domain Adaptation for Videos and Time-Series with Causal Optimal Transport

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Mishra_Towards_Uncertainty-aware_Unsupervised_Domain_Adaptation_for_Videos_and_Time-Series_with_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Mishra_Towards_Uncertainty-aware_Unsupervised_Domain_Adaptation_for_Videos_and_Time-Series_with_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 视频与多通道时间序列同时有时间变化和域漂移，单纯对齐表示可能丢掉通道依赖。
- **核心创新 / 方法** · 在源域和目标域估计通道依赖图，把结构约束纳入不确定性感知的最优传输对齐。
- **Baseline** · 与 TA3N、MA2LT-D、TransferAttn 以及不同传输求解器比较。
- **Benchmark** · WISDM、UCIHAR 等传感序列和 UCF101、HMDB51 的双向跨域视频分类，报告准确率。
- **关键结果 / 消融** · 表 4 双向平均准确率为 89.85%，TransferAttn 为 88.2%；求解器消融的对齐指标中 Sinkhorn 为 0.84，Greenkhorn 为 0.81。
- **适用条件 / 局限** · 通道关系来自观测估计，在混杂、时序干预变化或两个域依赖机制不同的情况下需重验。

**可复用机制** · 跨域时序适配除了匹配特征边缘分布，也可约束通道依赖在迁移前后保持，比较不同传输求解方式。见表 4。

<a id="paper-synthetic-stereo-camera-baseline-distribution"></a>

## What Makes Good Synthetic Training Data for Zero-Shot Stereo Matching?

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yan_What_Makes_Good_Synthetic_Training_Data_for_Zero-Shot_Stereo_Matching_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yan_What_Makes_Good_Synthetic_Training_Data_for_Zero-Shot_Stereo_Matching_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 合成立体匹配数据的样本总量无法说明相机布置和材质分布是否覆盖目标域。
- **核心创新 / 方法** · 每次只改变生成参数，用同样大小的数据训练同一模型，再观察零样本误差对不同目标域的变化。
- **Baseline** · 采用 RAFT-Stereo，对照不同相机基线范围、物体密度、背景、光照和材质。
- **Benchmark** · 每种生成设定用 5000 对合成立体图训练并零样本评估 Middlebury、ETH3D、KITTI 和 Booster。
- **关键结果 / 消融** · 表 1 的窄基线范围 [0.04,0.1] 在 Middlebury 2014-F 和 ETH3D 的误差为 32.47、2.89；宽范围 [0.04,0.4] 为 9.19、3.92，广覆盖有显著收益也有局部代价。
- **适用条件 / 局限** · 参数与真实部署的相机、视差、透明和反射分布相关，同一生成范围无法统一最小化所有误差。

**可复用机制** · 渲染训练数据时固定样本规模，依据目标场景分布选择相机基线范围，并分别报告各目标域误差。见表 1。

<a id="paper-solace-denoising-self-confidence-reward"></a>

## Improving Text-to-Image Generation with Intrinsic Self-Confidence Rewards

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Kim_Improving_Text-to-Image_Generation_with_Intrinsic_Self-Confidence_Rewards_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Kim_Improving_Text-to-Image_Generation_with_Intrinsic_Self-Confidence_Rewards_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 外部偏好模型有标注成本，也可能把优化导向高代理分但质量低的样本。
- **核心创新 / 方法** · 对自身生成的图像潜变量重新加噪，用恢复已知噪声的准确程度定义自信度并给强化学习奖励。
- **Baseline** · 与原 SD3.5、外部奖励 FlowGRPO、离线自信度和不同探针数量比较。
- **Benchmark** · GenEval、文本生成 OCR、CLIP、审美和偏好评分，以及 PartiPrompts 和 HPSv2 人评。
- **关键结果 / 消融** · 表 2 的在线奖励 GenEval、OCR 为 0.71、0.67，离线为 0.69、0.61；8 次探针到 16 次时 OCR 持平。
- **适用条件 / 局限** · 模型可能对自己熟悉的错误也很自信，需在独立质量与多样性指标下检查偏差。

**可复用机制** · 缺少可靠偏好模型时，可以把生成结果重新加噪后的恢复误差当作内在奖励，并与外部指标分开验证。见表 1、2。

<a id="paper-r2r-retrieved-degradation-prior-bank"></a>

## Retrieve-to-Restore: Efficient All-in-One Image Restoration with a Retrieval-Based Degradation Bank

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Retrieve-to-Restore_Efficient_All-in-One_Image_Restoration_with_a_Retrieval-Based_Degradation_Bank_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_Retrieve-to-Restore_Efficient_All-in-One_Image_Restoration_with_a_Retrieval-Based_Degradation_Bank_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 去雨、去雾、去噪等任务共享参数会竞争，单一重建特征难兼顾退化识别。
- **核心创新 / 方法** · 训练时聚合代表性退化先验，推理时从小型先验库检索与输入最相关的条件来调节共享骨干。
- **Baseline** · 比较统一恢复模型以及不同库容量；表 6 逐步加入频域、退化和匹配损失。
- **Benchmark** · SOTS、Rain100L 和 BSD68 的多退化恢复，指标为 PSNR 和 SSIM。
- **关键结果 / 消融** · 表 6 加匹配损失后均值 PSNR 从 32.29 增至 32.53 dB；表 5 字典由 64 增至 128 时反降到 32.34。
- **适用条件 / 局限** · 训练利用配对清晰参考，未见退化是否能用现有先验组合需要专门验证。

**可复用机制** · 多个退化任务共用骨干时，可把退化先验移到外部字典，通过检索做条件调整，再核对容量和失真干扰。见表 5、6。

<a id="paper-geniedrive-normalized-multiview-occupancy-conditioning"></a>

## GenieDrive: Towards Physics-Aware Driving World Model with 4D Occupancy Guided Video Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_GenieDrive_Towards_Physics-Aware_Driving_World_Model_with_4D_Occupancy_Guided_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yang_GenieDrive_Towards_Physics-Aware_Driving_World_Model_with_4D_Occupancy_Guided_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 直接从动作生成多路视频，很难同时满足需要的结构与动态一致性。
- **核心创新 / 方法** · 先预测三维空间随时间变化的占据，压缩到连续三平面潜表示，再以归一化多视角注意力生成视频。
- **Baseline** · 比较既有占据预测与驾驶视频模型，分别移除跨视角注意力或归一化。
- **Benchmark** · 驾驶占据预测与多视角视频生成，采用 FVD、mIoU 和 mAP 等指标。
- **关键结果 / 消融** · 表 5 的完整 FVD 为 98.06，无归一化为 212.67；相应 mIoU 为 31.44、21.49。
- **适用条件 / 局限** · 依赖训练占据数据与坐标对齐。占据改善及视频观感都不足以单独证明闭环动力学正确。

**可复用机制** · 世界模型可用可编辑的占据中间表示约束多视角合成，并消融归一化以检查跨视角注意力稳定性。见表 5。

<a id="paper-usrl"></a>

## Human-like Abstract Visual Reasoning via Understanding and Solving Reasoning Loop

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Human-like_Abstract_Visual_Reasoning_via_Understanding_and_Solving_Reasoning_Loop_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_Human-like_Abstract_Visual_Reasoning_via_Understanding_and_Solving_Reasoning_Loop_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 固定编码少量示例后直接输出，无法利用求解失败修正对规则的理解。
- **核心创新 / 方法** · 用理解模块维护规则表示、求解模块生成草案，两者通过迭代与门控相互更新。
- **Baseline** · 表2比较通用模型含 Gemini 2.5 Pro 32K、o3-mini-high 与 DeepSeek-R1；表3比较仅求解模块。
- **Benchmark** · ARC-AGI-1 评测集，每题最多两次尝试，准确率。
- **关键结果 / 消融** · 表2 7M USRL 达47.2%；表3仅求解模块36.5%，增加无门控理解模块后40.8%。
- **适用条件 / 局限** · 证据集中在网格变换，迭代和门控能否迁移到开放动作任务需另测。

**可复用机制** · 少样本规则推断可交替更新规则假设与暂定解，并对仅求解的模型做对照。

<a id="paper-motionhiflow"></a>

## MotionHiFlow: Text-to-Motion via Hierarchical Flow Matching

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_MotionHiFlow_Text-to-Motion_via_Hierarchical_Flow_Matching_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_MotionHiFlow_Text-to-Motion_via_Hierarchical_Flow_Matching_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 单一时间尺度同时承担全局语义与快速局部动作，难兼顾对齐和连贯。
- **核心创新 / 方法** · 从低到高时间尺度构造流匹配路径，用跨尺度过渡保持噪声一致；骨架拓扑辅助关节建模。
- **Baseline** · 表1含 TEMOS、T2M-GPT 等，表2–3比较层级数和组件。
- **Benchmark** · HumanML3D 与 KIT-ML 的 R-Precision、FID、多模态距离和多样性。
- **关键结果 / 消融** · 表1 MotionHiFlow 的 FID 分别0.032与0.135，表2报告不同尺度组合。
- **适用条件 / 局限** · 输出依赖固定骨架假设，迁移到不同控制频率与拓扑时需重估过渡。

**可复用机制** · 分层生成动作时，把跨尺度噪声连续性当作设计变量。

<a id="paper-mr-rag"></a>

## MR-RAG: Multimodal Relevance-Aware Retrieval-Augmented Generation for Medical Visual Question Answering

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_MR-RAG_Multimodal_Relevance-Aware_Retrieval-Augmented_Generation_for_Medical_Visual_Question_Answering_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_MR-RAG_Multimodal_Relevance-Aware_Retrieval-Augmented_Generation_for_Medical_Visual_Question_Answering_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 单一检索相似度难判断图文联合相关性，直接拼接会稀释关键信息。
- **核心创新 / 方法** · 结合模态内和模态间相关性检索，再按重要性调整生成时证据信息流。
- **Baseline** · 表1–2比较已有开源医疗 LVLM，表3在 LLaVA-Med-1.5 等对照组件。
- **Benchmark** · Harvard-FairVLMed、IU-Xray、MIMIC-CXR，报告准确率、精确率、召回与 F1。
- **关键结果 / 消融** · 表3在三个集合上平均比较检索与生成端模块，表1分数据集报告。
- **适用条件 / 局限** · 相关性分数需要能预测事实效用，证据冲突或跨域时弱相关文档可能仍是关键。

**可复用机制** · 分别校准检索相关性与生成阶段对每份证据的依赖，避免弱证据均匀注入。

<a id="paper-octomed-reasoning-length"></a>

## OctoMed: Data Recipes for State-of-the-Art Multimodal Medical Reasoning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Ossowski_OctoMed_Data_Recipes_for_State-of-the-Art_Multimodal_Medical_Reasoning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Ossowski_OctoMed_Data_Recipes_for_State-of-the-Art_Multimodal_Medical_Reasoning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 统一长链监督可能在简短分类任务增加推理而没有收益。
- **核心创新 / 方法** · 对多模态样本使用结构化且长短不同的推理轨迹进行监督微调。
- **Baseline** · 表1比较直接提示与 CoT 提示，表2含同规模开放模型与商业模型。
- **Benchmark** · 医学纯文本、多模态推理及分类，表1按任务报告指标。
- **关键结果 / 消融** · 表1报告 CoT 帮助推理任务，直接提示在分类略优；正文观察训练后的轨迹长度随任务变化。
- **适用条件 / 局限** · 缺少严格等数据量的跨领域长度配比实验，不能将总收益都归因于轨迹长度。

**可复用机制** · 微调时可混合不同长度的结构化轨迹，并按任务分别审计直接输出与推理模式。

<a id="paper-physics-guided-sds"></a>

## Let it Snow! Animating 3D Gaussian Scenes with Dynamic Weather Effects via Physics-Guided Score Distillation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Fiebelman_Let_it_Snow_Animating_3D_Gaussian_Scenes_with_Dynamic_Weather_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Fiebelman_Let_it_Snow_Animating_3D_Gaussian_Scenes_with_Dynamic_Weather_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 纯物理运动难达到感知保真，纯视频蒸馏在多粒子环境难维持一致运动。
- **核心创新 / 方法** · 用神经动态模型预测粒子运动与外观，联合优化物理引导及视频 SDS。
- **Baseline** · 表1对比 ClimateNeRF、GaussCtrl 和 Instruct-4DGS；表2去掉碰撞、外观、运动和物理引导。
- **Benchmark** · 静态3D场景添加雪、雨、雾、沙暴等动态效果；表1按效果报告量化指标。
- **关键结果 / 消融** · 表2分离固定运动、物理引导和外观模块的贡献。
- **适用条件 / 局限** · 需要可构建方向正确的模拟先验，天气粒子之外的复杂接触行为尚需验证。

**可复用机制** · 编辑动态3D场景时可让物理模拟给运动先验，同时允许视觉蒸馏更新外观和运动。

<a id="paper-flow3r-factored-flow"></a>

## Flow3r: Factored Flow Prediction for Scalable Visual Geometry Learning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Cong_Flow3r_Factored_Flow_Prediction_for_Scalable_Visual_Geometry_Learning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Cong_Flow3r_Factored_Flow_Prediction_for_Scalable_Visual_Geometry_Learning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 几何和相机真值昂贵，直接从联合特征预测二维对应可能无法约束各分量。
- **核心创新 / 方法** · 从一帧的几何潜表示和另一帧的位姿潜表示预测稠密对应，通过流监督训练两路。
- **Baseline** · 同骨干不同对应流分解及其他现有几何重建方案。
- **Benchmark** · 八个静态和动态基准；动态使用旋转与平移 RPE，静态用 RTA/AUC，几何用 MSE 和 F-score。
- **关键结果 / 消融** · 表1支持分解设计，表2–3报告不同数据条件；作者在约80万无标签视频训练后指出动态场景收益最大。
- **适用条件 / 局限** · 伪流错误、运动遮挡及尺度歧义可传入几何；数据规模变化不等同于质量改善。

**可复用机制** · 用无标签视频学习几何时，将对应流的预测分解为一侧几何与另一侧位姿。

<a id="paper-spatial-sam-sdf-memory"></a>

## Spatial-SAM: Spatially Consistent 3D Electron Microscopy Segmentation with SDF Memory and Semi-Supervised Learning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_Spatial-SAM_Spatially_Consistent_3D_Electron_Microscopy_Segmentation_with_SDF_Memory_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_Spatial-SAM_Spatially_Consistent_3D_Electron_Microscopy_Segmentation_with_SDF_Memory_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · SAM2 的切片记忆缺少体积边界约束，零散人工标注难保持连贯。
- **核心创新 / 方法** · 以三维 U-Net 预计算 SDF 作为 SAM2 几何记忆，再迭代使用双路伪标签。
- **Baseline** · 与既有半监督及全监督体积分割比较，表3直接替换记忆。
- **Benchmark** · MitoEM 等电子显微三维分割，测 Dice、mIoU，及不同标注比例。
- **关键结果 / 消融** · 表1–3比较低标注性能并检验 SDF 记忆的贡献。
- **适用条件 / 局限** · 距离场质量依赖预计算模型，拓扑复杂时错误边界可传播。

**可复用机制** · 逐切片分割要保持三维连贯时，用显式距离场替代通用传播记忆。

<a id="paper-face2scene-degradation-oracle"></a>

## Face2Scene: Using Facial Degradation as an Oracle for Diffusion-Based Scene Restoration

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Kazerouni_Face2Scene_Using_Facial_Degradation_as_an_Oracle_for_Diffusion-Based_Scene_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Kazerouni_Face2Scene_Using_Facial_Degradation_as_an_Oracle_for_Diffusion-Based_Scene_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 整图恢复缺乏退化约束，而专用脸部恢复无法覆盖背景。
- **核心创新 / 方法** · 以参照恢复人脸，从清晰与退化对应区域提取多尺度退化词元，用以条件化一步扩散恢复场景。
- **Baseline** · 全图恢复方法和脸部替换对照，含直接插入真值人脸。
- **Benchmark** · InScene 合成与真实验证，区分人脸和场景恢复质量。
- **关键结果 / 消融** · 表2–3报告局部估计转移到全图的收益，并对照理想人脸输入。
- **适用条件 / 局限** · 需要可靠参考且局部与背景退化相关，空间非均匀失真时可能误导恢复。

**可复用机制** · 若局部目标有可靠复原参照，从该局部估计退化后条件化整图恢复。

<a id="paper-waterflow-temporal-watermark"></a>

## WaTeRFlow: Watermark Temporal Robustness via Flow Consistency

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Jeong_WaTeRFlow_Watermark_Temporal_Robustness_via_Flow_Consistency_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Jeong_WaTeRFlow_Watermark_Temporal_Robustness_via_Flow_Consistency_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 静态图片可读的标记不一定经时间演变仍能恢复，独立逐帧预测会波动。
- **核心创新 / 方法** · 训练同时包含视频转换及运动对齐一致性，保护整体语义和恢复稳定性。
- **Baseline** · 对比图像水印方法与去掉时序训练的版本。
- **Benchmark** · 多个图生视频模型，用首帧与逐帧 bit accuracy，另评估图像和视频质量。
- **关键结果 / 消融** · 表1–3报告更稳的逐帧恢复并检验时序项影响。
- **适用条件 / 局限** · 仅适用于自愿写入标记的来源，不保证所有生成器、重编码和编辑均可追溯。

**可复用机制** · 需要从图生视频保留来源证据时，将水印恢复视作沿运动对应的跨帧稳定问题。

<a id="paper-long-video-sink-collapse"></a>

## LoL: Longer than Longer, Scaling Video Generation to Hour

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Cui_LoL_Longer_than_Longer_Scaling_Video_Generation_to_Hour_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Cui_LoL_Longer_than_Longer_Scaling_Video_Generation_to_Hour_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 固定锚帧用于缓解长程衰退，却可能反复重置场景。
- **核心创新 / 方法** · 分析 RoPE 周期与跨头趋同的关系，以训练无关的跨头位置扰动分散同步。
- **Baseline** · LongLive、Self-Forcing++ 在相同锚帧设置下有无机制，及其他自回归模型。
- **Benchmark** · 75秒和100秒定量视频，另展示小时级流式生成。
- **关键结果 / 消融** · 表1–2及长视频示例表明所测重复回跳减轻，短期质量保持。
- **适用条件 / 局限** · 更长可生成演示不证明无限时域稳定，结论依赖锚点及位置编码设计。

**可复用机制** · 自回归视频出现周期回跳时，先诊断多头位置编码是否共同锁到同一注意力锚点。

<a id="paper-reward-model-demographic-audit"></a>

## Bias at the End of the Score

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Magid_Bias_at_the_End_of_the_Score_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Magid_Bias_at_the_End_of_the_Score_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 奖励作为筛选、训练或评估指标时，其群体偏置可能贯穿整个生成流程。
- **核心创新 / 方法** · 审计奖励分数，并检查经奖励引导后生成的人口流形、表征和多样性变化。
- **Baseline** · 多个现有奖励模型及相应奖励引导设置。
- **Benchmark** · 文生图的人口属性切分，比较评分、刻板表征和人口多样性。
- **关键结果 / 消融** · 原文报告打分存在群体差异，奖励优化时会放大部分刻板印象并压缩多样性。
- **适用条件 / 局限** · 群体判断依赖模型、提示分布与属性定义，审计不能替代特定部署检验。

**可复用机制** · 选择文生图奖励模型时，按群体检查打分及优化后生成分布，避免总体质量掩盖偏差。

<a id="paper-markov-var-sliding-scale-history"></a>

## Markovian Scale Prediction: A New Era of Visual Autoregressive Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Markovian_Scale_Prediction_A_New_Era_of_Visual_Autoregressive_Generation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Markovian_Scale_Prediction_A_New_Era_of_Visual_Autoregressive_Generation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 视觉自回归模型为预测下一个尺度保留所有先前尺度，生成分辨率增加时成本高。
- **核心创新 / 方法** · 把当前尺度作为状态，并用滑窗压缩选定的前序尺度为历史向量，供下一尺度预测。
- **Baseline** · 比较无历史、全局历史、混合补偿，以及原 VAR 的时间和显存。
- **Benchmark** · ImageNet 256×256 类条件生成报告 FID 和 IS，另测不同分辨率推理用时与峰值显存。
- **关键结果 / 消融** · 表 4 深度同为 16 时，滑窗方案 FID 3.23，无历史为 3.64，全局历史为 3.41；混合历史 IS 略高。
- **适用条件 / 局限** · 尺度序列越长越需要验证远距离结构，消融参数量也略有差异，不能将差值全归于窗口。

**可复用机制** · 逐尺度生成时可以只保留临近尺度的压缩历史，比较全量、局部或无历史对画质和显存的影响。见表 3、4。

<a id="paper-grip-foot-contact-versus-inertial-sensors"></a>

## Ground Reaction Inertial Poser: Physics-based Human Motion Capture from Sparse IMUs and Insole Pressure Sensors

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Hori_Ground_Reaction_Inertial_Poser_Physics-based_Human_Motion_Capture_from_Sparse_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Hori_Ground_Reaction_Inertial_Poser_Physics-based_Human_Motion_Capture_from_Sparse_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 稀疏 IMU 给出局部动力信息，却难直接推断脚是否着地及接触状态。
- **核心创新 / 方法** · 用鞋垫压力和惯性信号估计运动状态，基于预测与数字人体的残差，在物理仿真重建动作。
- **Baseline** · 同一框架对照 2 至 6 个 IMU、有无足底压力，以及其他姿态捕捉方案。
- **Benchmark** · PRISM 等人体动作数据集，用关节误差 MPJPE、对齐关节误差与成功率评价。
- **关键结果 / 消融** · 表 3 四个 IMU 加压力后 MPJPE 从 194.48 降到 182.44 毫米，成功率从 88.58% 到 94.49%；只用六个 IMU 误差为 160.76 毫米，成功率为 87.01%。
- **适用条件 / 局限** · 需校准可穿戴传感器和人体模型；不同地面、鞋与非标准动作下应单测估计和接触。

**可复用机制** · 可穿戴动作捕捉应比较增加接触模态与再加同类惯性测量哪种更能改善物理稳定性。见表 3。

<a id="paper-seetn-continuous-label-affinity-denoising"></a>

## See Through the Noise: Improving Domain Generalization in Gaze Estimation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Peng_See_Through_the_Noise_Improving_Domain_Generalization_in_Gaze_Estimation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Peng_See_Through_the_Noise_Improving_Domain_Generalization_in_Gaze_Estimation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 视线标签难以高精度测量，带噪标注在跨域评估时会放大误差。
- **核心创新 / 方法** · 以原型保持连续标签和表征的相对邻域，根据两者的亲和一致性识别疑似噪声，再以亲和正则传递可靠信息。
- **Baseline** · 与 SUGE 等标签去噪方法对照，在相同骨干上比较仅回归损失和逐步添加两种亲和损失。
- **Benchmark** · 跨四种视线估计源、目标设置，以角误差衡量泛化。
- **关键结果 / 消融** · 表 4 的 DE→DM 基线为 8.07 度，加入一项亲和约束为 7.14 度，两项为 6.58 度。
- **适用条件 / 局限** · 依赖初始嵌入能够反映连续标签邻域，真实罕见标签或域外合法样本可能被误判为噪声。

**可复用机制** · 连续回归标签有噪声时，可用标签近邻与特征近邻的相容性筛样，避免把连续目标硬当成纠错类别。见表 4。

<a id="paper-poisson-gaussian-to-occupancy-weak-supervision"></a>

## Monocular Open Vocabulary Occupancy Prediction for Indoor Scenes

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhou_Monocular_Open_Vocabulary_Occupancy_Prediction_for_Indoor_Scenes_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhou_Monocular_Open_Vocabulary_Occupancy_Prediction_for_Indoor_Scenes_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 室内开放词汇占据面临无稠密语义标注及多重遮挡；部分高斯聚合在弱监督下无法收敛。
- **核心创新 / 方法** · 用带不透明度的 Poisson 聚合把语言嵌入高斯变成占据体素，并为对齐的语义信号调度温度。
- **Baseline** · 与 GaussianFormer2 聚合、Bernoulli 聚合及多种固定与动态温度比较。
- **Benchmark** · Occ-ScanNet 的单目室内重建，闭集和开放词汇设置，报告 IoU 与 mIoU。
- **关键结果 / 消融** · 表 2 开放词汇下 Poisson 为 21.05 mIoU、59.50 IoU，Bernoulli 为 17.25、46.65；GaussianFormer2 在该配置中为零。
- **适用条件 / 局限** · 依赖对齐的视觉语义和场景几何监督，新的对象密度、输入遮挡和语义噪声需重验。

**可复用机制** · 只有占据几何标签时，可比较高斯到体素的聚合概率模型和语义温度调度，避免弱监督训练坍塌。见表 2、3。

<a id="paper-evograph-online-multimodal-graph-refinement"></a>

## EvoGraph-R1: Self-Evolving Multimodal Knowledge Hypergraphs for Agentic Retrieval

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Lin_EvoGraph-R1_Self-Evolving_Multimodal_Knowledge_Hypergraphs_for_Agentic_Retrieval_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Lin_EvoGraph-R1_Self-Evolving_Multimodal_Knowledge_Hypergraphs_for_Agentic_Retrieval_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 离线构建的一次性检索图不能根据当前查询补回漏掉关系，也会让多模态证据信息碎片化。
- **核心创新 / 方法** · 把图检索表示为交互过程，检索器可把新证据组织成多模态超边并据此更新图，再重复检索。
- **Baseline** · 与文本及多模态检索基线比较，分别移除超图、插入、更新与搜索。
- **Benchmark** · 2WikiMulti-HopQA 和 E-VQA 分别用 F1、准确率及平均检索轮数评测。
- **关键结果 / 消融** · 表 3 的 2Wiki 中完整方案为 68.5 F1 和 2.57 轮，移除插入为 60.1 和 3.48 轮；E-VQA 准确率为 43.6%、36.8%。
- **适用条件 / 局限** · 图更新会继承证据与关系错误，检索轮数无法涵盖搜索、推理和图写入的真实总成本。

**可复用机制** · 多跳回答遇到新证据时，可让检索策略在当前问答中更新图结构，并检查各更新操作对答案和检索轮数的影响。见表 3。

<a id="paper-edge-recvit-boundary-aware-token-depth"></a>

## Edge-RecViT: Efficient Vision Transformer via Semantic-Refined Dynamic Recursion

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Edge-RecViT_Efficient_Vision_Transformer_via_Semantic-Refined_Dynamic_Recursion_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Edge-RecViT_Efficient_Vision_Transformer_via_Semantic-Refined_Dynamic_Recursion_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 普通注意力打分可能让边缘标记过早退出，把额外计算留给大量相似前景标记。
- **核心创新 / 方法** · 用边缘感知标记排名分配递归深度，递归 Transformer 的隐藏层共享参数。
- **Baseline** · 对比固定深度、不共享参数和其他排名正则，分别看深度分配和共享作用。
- **Benchmark** · ImageNet-1K、CIFAR-10/100 图像分类，以 Top-1、参数量与 FLOPs 衡量。
- **关键结果 / 消融** · 表 3 两版本都是 23M 参数，固定深度为 35.2 GFLOPs、82.1% Top-1，边缘排名为 24.4 GFLOPs、82.0%。
- **适用条件 / 局限** · 图像边缘未必对应下游语义，实际推理耗时还取决于设备和索引调度；应单测纹理丰富或低对比条件。

**可复用机制** · 视觉标记早退时可以给含结构信息的边缘标记更深预算，并对照固定深度的精度与 FLOPs。见表 3。

<a id="paper-raas-agent-architecture"></a>

## RAAS: LLM Agentic System Architecture Search with GRPO

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_RAAS_LLM_Agentic_System_Architecture_Search_with_GRPO_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yang_RAAS_LLM_Agentic_System_Architecture_Search_with_GRPO_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 绝对分数混入问题难度，单次运行混入采样随机性。
- **核心创新 / 方法** · 候选在相同问题成组比较，再汇总独立执行试验，将相对信号用于架构搜索。
- **Baseline** · 表1在 GPT-4o-mini 与 Qwen2.5-72B 上比较既有 Agentic Supernet 与其他系统；表2比较通用模型。
- **Benchmark** · MATH、GSM8K、HumanEval、MBPP 准确率，GAIA 按难度分组。
- **关键结果 / 消融** · 表1两种骨干平均84.13%和83.59%，论文另在 GAIA 测泛化。
- **适用条件 / 局限** · 重复运行增加搜索预算，执行成本差异大的架构应同时按成本比较。

**可复用机制** · 搜索工作流时，对同一问题比较候选架构，并在多个独立运行中汇总。

<a id="paper-jiti-elegant-execution"></a>

## Beyond Success: Refining Elegant Robot Manipulation from Mixed-Quality Data via Just-in-Time Intervention

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Mao_Beyond_Success_Refining_Elegant_Robot_Manipulation_from_Mixed-Quality_Data_via_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Mao_Beyond_Success_Refining_Elegant_Robot_Manipulation_from_Mixed-Quality_Data_via_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 演示混合了不同质量，基本成功指标不反映动作是否满足隐式约束。
- **核心创新 / 方法** · 离线训练执行质量 critic，推理以置信度监控候选动作并及时介入，保持原策略参数。
- **Baseline** · 表1比较 SmolVLA、GR00T N1.5 加与不加框架；图4比较全程引导和选择性介入。
- **Benchmark** · LIBERO-Elegant 八项任务 Elegant Success Rate、未见任务与真实机械臂操作。
- **关键结果 / 消融** · 表1在 SmolVLA 上平均 ESR 由49.8%升至67.2%，表2比较奖励，表3测试未见任务。
- **适用条件 / 局限** · 依赖可标注的执行约束和置信度校准，低置信度环境需明确可接受的介入风险。

**可复用机制** · 成功率相近时，可独立评估执行约束，仅在关键动作由置信度门控触发修正。

<a id="paper-earl-video-evidence"></a>

## Select Less, Reason More: Prioritizing Evidence Purity for Video Reasoning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Select_Less_Reason_More_Prioritizing_Evidence_Purity_for_Video_Reasoning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Select_Less_Reason_More_Prioritizing_Evidence_Purity_for_Video_Reasoning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 固定均匀帧遗漏短暂证据，仅从预采样帧中选取无法补充分辨率。
- **核心创新 / 方法** · 用证据感知 RL 动态选帧，围绕关键帧局部重采样并在正确奖励中施加 IoU 约束。
- **Baseline** · 表1比较 Qwen2.5-VL 与其他模型，表2去掉 IoU，表3去掉动态调整。
- **Benchmark** · MLVU、VideoMME 无字幕、LongVideoBench、LVBench、MVBench，按帧预算比较答题准确率。
- **关键结果 / 消融** · 表1同7B、32帧记录 MLVU 41.6 到49.3，表2去掉 IoU 后为47.9。
- **适用条件 / 局限** · 需可回看原视频与可用时间证据；直播无缓存或证据分布很离散时应重新评估。

**可复用机制** · 视频取证应允许在已选时间附近重新高频采样，并奖励证据定位而不只答对。

<a id="paper-multishot-narrative-rope"></a>

## MultiShotMaster: A Controllable Multi-Shot Video Generation Framework

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_MultiShotMaster_A_Controllable_Multi-Shot_Video_Generation_Framework_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_MultiShotMaster_A_Controllable_Multi-Shot_Video_Generation_Framework_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 单镜头生成扩展到多镜头时缺少顺序承接及跨镜头身份条件。
- **核心创新 / 方法** · 给镜头过渡显式相移，并把参考 token 及定位信号写入时空 RoPE。
- **Baseline** · 以单镜头预训练模型扩展，表1比较 EchoShot、CineTrans、Phantom、VACE 等。
- **Benchmark** · 多镜头文本到视频、参考到视频，评估镜头一致、转场偏差、叙事及参考一致性。
- **关键结果 / 消融** · 表1有参考模型镜头一致性0.702，Phantom 为0.585；转场偏差0.495，高于 Phantom 的0.462。
- **适用条件 / 局限** · 依赖镜头分段与参考信号，目标允许 abrupt cut 时需检验跨镜头一致性是否适当。

**可复用机制** · 有分段结构的序列可用显式位置相位标识段边界，同时维持段内时空参考。

<a id="paper-cubic-discrete-diffusion"></a>

## Cubic Discrete Diffusion: Discrete Visual Generation on High-Dimensional Representation Tokens

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Cubic_Discrete_Diffusion_Discrete_Visual_Generation_on_High-Dimensional_Representation_Tokens_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_Cubic_Discrete_Diffusion_Discrete_Visual_Generation_on_High-Dimensional_Representation_Tokens_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 低维离散视觉 token 丢语义，高维 token 逐维解码成本过高。
- **核心创新 / 方法** · 在离散表示的任意空间位置和维度独立遮罩预测，用固定去噪步数恢复。
- **Baseline** · 表2比较 DINOv2、SigLIP2 连续与离散配置，表3比较 LLaVA 理解评测，表4消融。
- **Benchmark** · ImageNet-256 生成及重建 rFID、IS，还测试 LLaVA 理解能力。
- **关键结果 / 消融** · 表2显示相应量化级别可达到接近连续配置的重建表现，表3检验量化后的语义保留。
- **适用条件 / 局限** · 量化级别依赖特征分布，视频和动作上的稳定性需要额外测试。

**可复用机制** · 高维理解特征用于离散生成时，可按位置和特征坐标共同遮罩，使生成轮数不随维数线性增加。

<a id="paper-nerfify"></a>

## NERFIFY: A Multi-Agent Framework for Turning NeRF Papers into Code

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Jain_NERFIFY_A_Multi-Agent_Framework_for_Turning_NeRF_Papers_into_Code_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Jain_NERFIFY_A_Multi-Agent_Framework_for_Turning_NeRF_Papers_into_Code_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 通用生成器易产出语法正确但不能训练的多文件项目。
- **核心创新 / 方法** · 用 Nerfstudio 语法约束模块接口，按依赖图顺序生成，并在训练后用视觉反馈定位退化。
- **Baseline** · 表2比较 Paper2Code、AutoP2C 等通用基线，表1与人工实现比较，表3与作者实现比较。
- **Benchmark** · NERFIFY-BENCH 的可训练性，重建比较 PSNR、SSIM、LPIPS。
- **关键结果 / 消融** · 正文表2显示语法可通过与实际可训练存在差距；表1和表3用渲染指标核对行为。
- **适用条件 / 局限** · 迁移需要可形式化的宿主接口及可执行训练检查，结论仅在 NeRF 工作流验证。

**可复用机制** · 论文到代码应先将目标框架的模块契约形式化，然后按依赖顺序生成并验证各节点。

<a id="paper-gated-condition-linear-attention"></a>

## Gated Condition Injection without Multimodal Attention: Towards Controllable Linear-Attention Transformers

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_Gated_Condition_Injection_without_Multimodal_Attention_Towards_Controllable_Linear-Attention_Transformers_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_Gated_Condition_Injection_without_Multimodal_Attention_Towards_Controllable_Linear-Attention_Transformers_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · ControlNet 或既有注入方法在线性注意力骨干上收敛慢或支持条件类型有限。
- **核心创新 / 方法** · 在双路径结构中以统一门控注入对齐和非对齐视觉条件。
- **Baseline** · 以 SANA 为骨干，表2比较 ControlNet 等，表3消融门控。
- **Benchmark** · 五个空间对齐任务比较可控性、SSIM、FID、MUSIQ 与 CLIP，正文也评估非对齐条件。
- **关键结果 / 消融** · 表2按任务报告画质及控制收益，表3检验门控对训练融合的作用。
- **适用条件 / 局限** · 需适配骨干和条件的编码分支，训练未覆盖的组合条件仍需评估。

**可复用机制** · 在线性注意力骨干上做异构条件控制时，比较独立条件支路加门控与传统条件注入。

<a id="paper-monocop-uncertainty-routing"></a>

## Unleashing the Power of Chain-of-Prediction for Monocular 3D Object Detection

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Unleashing_the_Power_of_Chain-of-Prediction_for_Monocular_3D_Object_Detection_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Unleashing_the_Power_of_Chain-of-Prediction_for_Monocular_3D_Object_Detection_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 深度、尺寸和朝向相关，但顺序预测在遮挡与截断时会放大早期误差。
- **核心创新 / 方法** · 学习与聚合属性特征链，并以逐物体不确定性在链式与并行分支间选择。
- **Baseline** · KITTI、nuScenes、Waymo 上与单目检测方案比较，原文对照并行、链式和动态选择。
- **Benchmark** · KITTI val/test 的3D IoU 0.7，nuScenes 验证及 Waymo 验证分难度评估。
- **关键结果 / 消融** · 表1–3报告多基准表现及不同难度效应。
- **适用条件 / 局限** · 依赖属性不确定度准确，域外校准错误会导致选择失效。

**可复用机制** · 多属性预测中，低不确定时利用属性链，高不确定样本切换并行以阻断传播误差。

<a id="paper-any4d-modular-coordinate-factors"></a>

## Any4D: Unified Feed-Forward Metric 4D Reconstruction

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Karhade_Any4D_Unified_Feed-Forward_Metric_4D_Reconstruction_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Karhade_Any4D_Unified_Feed-Forward_Metric_4D_Reconstruction_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 只做两帧场景流或少量点追踪难恢复完整动态几何，异构输入不易接入。
- **核心创新 / 方法** · 在局部坐标预测深度和内参，在全局坐标预测外参和场景流，可接入 RGB-D、惯性里程或雷达。
- **Baseline** · 与稀疏追踪、密集场景流及视频深度方案比较。
- **Benchmark** · 表1–3分别以三维点跟踪、场景流 EPE 与视频深度误差评估。
- **关键结果 / 消融** · 作者报告多个设置误差低约2–3倍、速度约15倍。
- **适用条件 / 局限** · 要求时间及传感器对齐，场景尺度及绝对参考质量受可用传感信息制约。

**可复用机制** · 多传感器动态几何建模中，按局部相机系和全局世界系因子化预测。

<a id="paper-progressive-mask-distillation"></a>

## Progressive Mask Distillation for Self-supervised Video Representation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_Progressive_Mask_Distillation_for_Self-supervised_Video_Representation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wu_Progressive_Mask_Distillation_for_Self-supervised_Video_Representation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 固定掩码比例难兼顾局部细节和高层语义。
- **核心创新 / 方法** · 从低掩码逐步升高并跨阶段蒸馏，结合困难区域增强和跨层特征对齐。
- **Baseline** · 与已有视频掩码自监督方法及不同掩码训练配置比较。
- **Benchmark** · 视频自监督表征下游评估，含 Top-1 分类及特征迁移对照。
- **关键结果 / 消融** · 表1–3报告性能和特征迁移，并比较渐进策略。
- **适用条件 / 局限** · 需要多阶段训练，教师弱点可能继承；阶段和遮盖率应针对视频规律验证。

**可复用机制** · 掩码视频预训练时，让低遮盖阶段的学生教高遮盖阶段，避免大遮盖初期无法学习。

<a id="paper-gthinker-cue-rethinking"></a>

## GThinker: Towards General Multimodal Reasoning via Cue-Guided Rethinking

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhan_GThinker_Towards_General_Multimodal_Reasoning_via_Cue-Guided_Rethinking_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhan_GThinker_Towards_General_Multimodal_Reasoning_via_Cue-Guided_Rethinking_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 模型会在语言内部反思，却常把首次视觉判断当作无误前提。
- **核心创新 / 方法** · 以带线索复查的示范冷启动，再用失败筛选和强化学习训练按需复审。
- **Baseline** · 表1–2对照现有多模态模型，表3消融迭代数据流程。
- **Benchmark** · M3CoT 综合推理，以及数学、多领域与细粒度视觉基准。
- **关键结果 / 消融** · 作者报告 M3CoT 达81.5%，正文检验视觉重新检查。
- **适用条件 / 局限** · 复审能力依赖视觉线索是否可重新获取，额外推理增加开销。

**可复用机制** · 多模态模型推理初始观察可能错误时，引入证据冲突触发的视觉重新检查。

<a id="paper-analytic-concepts-articulation"></a>

## Physically Ground Commonsense Knowledge for Articulated Object Manipulation with Analytic Concepts

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wei_Physically_Ground_Commonsense_Knowledge_for_Articulated_Object_Manipulation_with_Analytic_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wei_Physically_Ground_Commonsense_Knowledge_for_Articulated_Object_Manipulation_with_Analytic_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 类别名称或描述难直接变成开合等机械控制目标。
- **核心创新 / 方法** · 将语义级知识映射到可计算和模拟的解析概念，以对象结构和功能引导策略。
- **Baseline** · ManipLLM、A3VLM 等操作方法。
- **Benchmark** · 多类可动对象的仿真和真实操作，以平均成功率评价，另考察末端执行器。
- **关键结果 / 消融** · 表1–3报告跨类别及实机结果。
- **适用条件 / 局限** · 需要解析概念覆盖对象形态和功能，未知或复杂变形结构须扩展表达。

**可复用机制** · 把语言常识作为对象功能假设，再用可计算几何与物理概念约束操作。

<a id="paper-osfed-compact-learned-update-snapshot"></a>

## OS-Fed: One Snapshot Is All You Need

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Qian_OS-Fed_One_Snapshot_Is_All_You_Need_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Qian_OS-Fed_One_Snapshot_Is_All_You_Need_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 压缩逐元素更新可能丢掉有效梯度，导致异质客户端收敛性能下降。
- **核心创新 / 方法** · 将本地训练更新编码为图像形状的紧凑快照及可学习标签，并在服务器用快照重建训练更新。
- **Baseline** · 比较 FedAvg、RandTopk、LoRA-FAIR 及用相同优化目标但无多网格快照的 FedAF+。
- **Benchmark** · AGNews、Sogou 和图像分类，以 Top-1、通信大小、压缩与解压时间衡量。
- **关键结果 / 消融** · 表 4 的 AGNews 上快照为 80.0%、7.66 MB，FedAvg 为 82.3%、3124 MB，FedAF+ 为 80.0%、11.2 MB。
- **适用条件 / 局限** · 上报成本之外仍有客户端优化开销，重建精度依赖架构与数据；实验结果不构成隐私保证。

**可复用机制** · 联邦通信受限时，可比较把更新编码成少量可学习样本与发送稀疏梯度，并同时计入编码、解码和精度。见表 4。

<a id="paper-backsplit-fine-grained-background-supervision"></a>

## BackSplit: The Importance of Sub-dividing the Background in Biomedical Lesion Segmentation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Saluja_BackSplit_The_Importance_of_Sub-dividing_the_Background_in_Biomedical_Lesion_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Saluja_BackSplit_The_Importance_of_Sub-dividing_the_Background_in_Biomedical_Lesion_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 将病灶之外的全部像素标成背景，会丢掉组织间有助于识别稀疏目标的区别。
- **核心创新 / 方法** · 训练时把背景按支持结构细分，使用现有架构学习辅助标签，再针对目标报告分割。
- **Baseline** · 同 U-Net、ResEncU-Net、SegResNet 的原始训练比较；另测自动生成辅助标注。
- **Benchmark** · KiTS23、PANTHER-MR、NSCLC-Radiomics 等，五折验证，报告 Dice、HD95、NSD。
- **关键结果 / 消融** · 表 1 的 NSCLC 上，ResEncU-Net 的 Dice 从 0.5020 到 0.5386，HD95 从 145.0108 到 125.9383；SegResNet 的 NSD 由 0.3921 降至 0.3842。
- **适用条件 / 局限** · 需要与目标有稳定关系且质量足够的背景结构标签，辅助标签错误和新的采集域应单测。

**可复用机制** · 稀疏目标分割可在训练时细分异质背景，仅在输出时合并，验证辅助标签加到现有分割器是否有效。见表 1。

<a id="paper-flashdecoder-rolling-kv-streaming-video-decode"></a>

## FlashDecoder: Real-Time Latent-to-Pixel Streaming Decoder with Transformers

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Kang_FlashDecoder_Real-Time_Latent-to-Pixel_Streaming_Decoder_with_Transformers_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Kang_FlashDecoder_Real-Time_Latent-to-Pixel_Streaming_Decoder_with_Transformers_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 视频潜变量的三维卷积解码在高分辨率和长序列上成本较高。
- **核心创新 / 方法** · 用逐帧 Transformer 把潜变量解码为像素，只关注固定长度历史，以滚动缓存和窗口内相对位置支持持续生成。
- **Baseline** · 与 Wan2.1、Wan2.2 的卷积解码器对照，并消融 2、3、4 帧窗口。
- **Benchmark** · UltraVideo 的 480p、720p、1080p 重建，比较 PSNR、LPIPS、rFVD、FPS 与显存。
- **关键结果 / 消融** · 表 3 的 Wan2.2 原解码器为 16.1 FPS、19.3 GB，替换后为 76.3 FPS、2.4 GB，rFVD 从 10.39 增至 12.75。
- **适用条件 / 局限** · 窗口会截断长期信息；帧率收益须在目标硬件和完整生成流程中验证。

**可复用机制** · 流式视频解码可对照固定长度的滚动 KV 窗口，按窗口大小测画质、峰值显存和帧率。见表 3、4。

<a id="paper-diffuview-camera-conditioned-diffusion-features"></a>

## DiffuView: Multi-View Diffusion Pretraining for 3D Aware Robotic Manipulation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_DiffuView_Multi-View_Diffusion_Pretraining_for_3D_Aware_Robotic_Manipulation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_DiffuView_Multi-View_Diffusion_Pretraining_for_3D_Aware_Robotic_Manipulation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 视觉操控遇到新相机位姿时，单视图掩码预训练往往缺少一致的三维对应。
- **核心创新 / 方法** · 预训练相机条件的多视图扩散模型，用其特征和基于射线的 Plücker 表示为闭环模仿策略提供条件。
- **Baseline** · 与现有操控表征基线比较，移除机器人数据预训练、射线嵌入或 FiLM。
- **Benchmark** · LIBERO、MetaWorld、多视图基准和真实操控，以任务成功率评估。
- **关键结果 / 消融** · 表 5 总体成功率 89.2%，去掉机器人数据预训练为 63.3%，去掉 Plücker 嵌入为 76.2%。
- **适用条件 / 局限** · 需要视角几何与额外机器人预训练数据，未标定相机、严重遮挡或新动作空间需单测。

**可复用机制** · 视觉操控可从相机条件多视角扩散取特征，再分别检查机器人数据和相机编码对新视角的贡献。见表 5。

<a id="paper-flowsteer-online-teacher-trajectory-alignment"></a>

## FlowSteer: Guiding Few-Step Image Synthesis with Authentic Trajectories

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Ke_FlowSteer_Guiding_Few-Step_Image_Synthesis_with_Authentic_Trajectories_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Ke_FlowSteer_Guiding_Few-Step_Image_Synthesis_with_Authentic_Trajectories_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 分段 ReFlow 在训练和采样时遇到的状态分布不同，少步推理时误差容易集中。
- **核心创新 / 方法** · 训练学生时让时间段与教师实际轨迹对齐，再结合蒸馏损失改善有限步数生成。
- **Baseline** · 比较 PeRFlow、PCM、Hyper-SD、Flash Diffusion 与原模型，并报告实际函数评估次数。
- **Benchmark** · COCO 10k 和 GenEval，比较 PickScore、HPSv2、CLIP 及组合生成得分。
- **关键结果 / 消融** · 表 3 对 SD3-Medium，以 4 次函数评估得到 GenEval 0.6859，PeRFlow 为 0.6357，Flash Diffusion 为 0.6672。
- **适用条件 / 局限** · 依赖可生成轨迹的教师，在线对齐增加训练开销；不同骨干对单项能力的增益不完全一致。

**可复用机制** · 少步流模型蒸馏可检验在线对齐真实教师轨迹，以减少分段重流与推理时轨迹的分布差。见表 3。

<a id="paper-syncmos-dependency-conditioned-time-warp"></a>

## SyncMos: Scalable Motion Synchronisation for Multi-Agent Scene Interaction

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_SyncMos_Scalable_Motion_Synchronisation_for_Multi-Agent_Scene_Interaction_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_SyncMos_Scalable_Motion_Synchronisation_for_Multi-Agent_Scene_Interaction_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 分别生成多个角色的动作，即使动作各自合理，也可能错过共同接触或传递的时机。
- **核心创新 / 方法** · 先把文本拆成具有依赖的事件，再在单人动作生成之上用时间变形与条件采样对齐交互。
- **Baseline** · 与 LINGO 单角色运动基线和无时序依赖的规划比较。
- **Benchmark** · 合成交互的事件覆盖和依赖测试，以及正负偏移下的抓取对时成功率。
- **关键结果 / 消融** · 表 2 在 +0.5 秒成功率为 84.7%，-1.5 秒为 37.3%，基线在所列偏移均为 0。
- **适用条件 / 局限** · 极端提前的效果较差；生成动作同步不等同于真实多机器人硬件上的闭环接触可行。

**可复用机制** · 用单个动作模型生成多角色交互时，可以先显式列出事件依赖，再根据同步目标做时间变形，单测偏移范围。见表 2、3。

<a id="paper-cloud-edge-cross-architecture-distillation"></a>

## Cross-Architecture Adaptation: Cloud-Edge Continual Test-Time Adaptation with Dynamic Sampling and Heterogeneous Distillation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_Cross-Architecture_Adaptation_Cloud-Edge_Continual_Test-Time_Adaptation_with_Dynamic_Sampling_and_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_Cross-Architecture_Adaptation_Cloud-Edge_Continual_Test-Time_Adaptation_with_Dynamic_Sampling_and_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 实时边缘模型适配漂移时，云端模型与端侧通常具有不同表示和计算预算。
- **核心创新 / 方法** · 从边缘流动态选样上传，以异构教师和学生间蒸馏适配端侧。
- **Baseline** · 对比 Tent、CoTTA、ETA、CEMA 与 CoLA，并消融云边采样和异构蒸馏。
- **Benchmark** · ImageNet-C 五级持续退化，报告各退化分类准确率及上报样本。
- **关键结果 / 消融** · 表 1 使用 ViT-B 云教师与 ResNet-18 边模型，平均 41.2%，CoLA 为 38.6%；表 2 去掉 MAHD 后为 36.2%。
- **适用条件 / 局限** · 依赖网络传输和云教师的可信度，弱网络、教师误判或训练流不可上传时需重新评估。

**可复用机制** · 边缘模型遇到持续分布漂移时，可选择只上传有价值的样本，由更强异构云模型提供蒸馏信号，再逐项测适配收益和传输。见表 1–3。

<a id="paper-uz3dvg"></a>

## UZ3DVG: Unaided Zero-Shot 3D Visual Grounding with Generated Language Conditions

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Tan_UZ3DVG_Unaided_Zero-Shot_3D_Visual_Grounding_with_Generated_Language_Conditions_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Tan_UZ3DVG_Unaided_Zero-Shot_3D_Visual_Grounding_with_Generated_Language_Conditions_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 零样本3D指代模型常在推理需要外部视觉或重复模型调用。
- **核心创新 / 方法** · 教师产生物体级空间伪标签及推理链，以几何感知模块把空间推理蒸馏进轻量学生。
- **Baseline** · 表1比较 LERF、VLM-G 等，协议区分是否用 Mask3D，表3消融。
- **Benchmark** · ScanRefer 验证集 Acc@0.25/0.5、单3090吞吐；Nr3D 用同一检查点直接推理。
- **关键结果 / 消融** · 表1无 Mask3D 配置总体43.13/35.05，吞吐9.43 FPS；较小子集协议需分开看。
- **适用条件 / 局限** · 要求投影视图与三维点的配准可靠，遮挡会污染教师标签。

**可复用机制** · 把跨模态教师移到离线数据生成，部署只留点云和指令，单测外部依赖与定位准确率。

<a id="paper-d2mil"></a>

## Learning from Noisy Supervision: A Denoising-Debiasing Framework for Weakly Supervised Video Anomaly Detection

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_Learning_from_Noisy_Supervision_A_Denoising-Debiasing_Framework_for_Weakly_Supervised_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_Learning_from_Noisy_Supervision_A_Denoising-Debiasing_Framework_for_Weakly_Supervised_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 正样本包仍包含大量正常片段，按损失一次丢弃会同时丢掉难异常。
- **核心创新 / 方法** · 动态过滤可疑高损失片段，再以视觉语言模型重新检查被滤实例。
- **Baseline** · 表1–3比较原 MIL 方法和加入 D2MIL 的结果，含 UR-DMU 等。
- **Benchmark** · ShanghaiTech、UCF-Crime、MSAD 的视频异常检测 AUC。
- **关键结果 / 消融** · 表1–3在多个数据集比较原基线与嵌入 D2MIL 后的表现。
- **适用条件 / 局限** · 需要教师适于识别异常，误判高度相关时复核无法恢复真阳性。

**可复用机制** · 在弱监督多实例训练中，把大损失样本暂缓训练并用独立教师复核，保留难正例。

<a id="paper-color-scene-coordinate-regression"></a>

## CoLoR: The Devil is in Scene Coordinate Regression for Large-Scale Visual Localization

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Mao_CoLoR_The_Devil_is_in_Scene_Coordinate_Regression_for_Large-Scale_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Mao_CoLoR_The_Devil_is_in_Scene_Coordinate_Regression_for_Large-Scale_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 大规模场景共视稀疏、局部外观重复，单一监督无法覆盖全部点。
- **核心创新 / 方法** · 显式切分单/多视点，两阶段自举；对图像级与像素级特征共同施加检索目标。
- **Baseline** · 表1比较特征匹配和场景坐标回归，表3逐步加入机制。
- **Benchmark** · Aachen Day-Night 与 Hyundai 室内，报告地图大小和三档位姿容差的通过率。
- **关键结果 / 消融** · 表1 CoLoR 地图47 MB，Aachen 日间最严格阈值78.6%、夜间67.3%。
- **适用条件 / 局限** · 自举依赖初始几何和可用多视对应，重复结构或单视占比更高需重新验证。

**可复用机制** · 按观察冗余分开训练可靠多视点与弱单视点，再统一局部和全局检索特征。

<a id="paper-splat-ct-pose-sensitivity"></a>

## Revisiting Pose Sensitivity in Splat-based Computed Tomography under Sparse-view Reconstruction

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Choi_Revisiting_Pose_Sensitivity_in_Splat-based_Computed_Tomography_under_Sparse-view_Reconstruction_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Choi_Revisiting_Pose_Sensitivity_in_Splat-based_Computed_Tomography_under_Sparse-view_Reconstruction_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 实测稀疏 CT 的条纹常归因于视角稀少，掩盖采集几何误差。
- **核心创新 / 方法** · 分析扰动如何经可微投影传播，并在重建时联合校准几何参数。
- **Baseline** · 表1–3对比原始 splat 重建和加入校准，表4报告耗时。
- **Benchmark** · 有/无几何噪声的稀疏视角 CT，PSNR 和位姿平移/旋转 RMSE。
- **关键结果 / 消融** · 表1显示无噪声时差异小，加入位姿噪声时联合校准获益；表3改变扰动幅度。
- **适用条件 / 局限** · 校准依赖初始几何可辨识，错误严重与真实散射等其他伪影要单独评估。

**可复用机制** · 稀疏视角重建遇到条纹时，应先把姿态误差和视图数量作为独立因素诊断。

<a id="paper-real2edit2real"></a>

## Real2Edit2Real: Generating Robotic Demonstrations via a 3D Control Interface

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_Real2Edit2Real_Generating_Robotic_Demonstrations_via_a_3D_Control_Interface_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_Real2Edit2Real_Generating_Robotic_Demonstrations_via_a_3D_Control_Interface_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 真实演示难覆盖对象空间布局，纯2D编辑不能保证几何一致。
- **核心创新 / 方法** · 多视重建再编辑点云，调整姿态和深度，以深度、动作、边缘和射线图约束合成。
- **Baseline** · 表1比较 Go-1 与 π0.5 分别用实采和生成增强训练，表2–3比较高度与桌面纹理。
- **Benchmark** · 四项实机操作任务成功率及未见高度与纹理。
- **关键结果 / 消融** · 作者报告从1–5条原始演示合成的数据在实验任务上可匹配或超过50条实采训练。
- **适用条件 / 局限** · 需要可靠的度量重建，复杂接触、遮挡及不同机械臂运动学需重新验证。

**可复用机制** · 扩增操作演示时，可先在度量3D空间编辑轨迹和姿态，再用校准深度作视频生成主约束。

<a id="paper-u4d-uncertainty-first"></a>

## U4D: Uncertainty-Aware 4D World Modeling from LiDAR Sequences

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_U4D_Uncertainty-Aware_4D_World_Modeling_from_LiDAR_Sequences_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_U4D_Uncertainty-Aware_4D_World_Modeling_from_LiDAR_Sequences_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 统一分配生成容量会忽视几何或语义困难区域，造成时序不稳。
- **核心创新 / 方法** · 由分割模型给出不确定图，依次生成高熵区域和剩余结构，并融合时空特征。
- **Baseline** · 与既有激光雷达生成及原文组件配置比较。
- **Benchmark** · 表1–3比较激光雷达场景生成质量与四维时序一致性。
- **关键结果 / 消融** · 原文报告几何及时间一致性提升。
- **适用条件 / 局限** · 分割熵不一定反映真实几何难度，错误锚点可能污染后续生成。

**可复用机制** · 生成时序三维场景时，先从高不确定区域构建结构锚点，再用其条件化剩余区域。

<a id="paper-hrnet-hybrid-multimodal-registration"></a>

## Disentangle-then-Align: Non-Iterative Hybrid Multimodal Image Registration via Cross-Scale Feature Disentanglement

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Disentangle-then-Align_Non-Iterative_Hybrid_Multimodal_Image_Registration_via_Cross-Scale_Feature_Disentanglement_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Disentangle-then-Align_Non-Iterative_Hybrid_Multimodal_Image_Registration_via_Cross-Scale_Feature_Disentanglement_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 只约束共享表示容易漏入模态私有线索；单一变换难建模全局与局部变化。
- **核心创新 / 方法** · 用模态特定归一化、跨尺度解耦及投影提取共享表示，粗到细一次预测刚体和形变。
- **Baseline** · 与既有刚体及多模态配准方案比较。
- **Benchmark** · 四套多模态图像配准数据，测重投影等配准精度并按变换类型比较。
- **关键结果 / 消融** · 原文报告各类配准场景的表现，并比较训练配置与刚体结果。
- **适用条件 / 局限** · 共享特征需要真正对应的跨模态证据，极少重叠或强非刚性仍会困难。

**可复用机制** · 同时存在大尺度错位和局部形变时，先对齐去模态差异的特征，再联合预测两类变换。

<a id="paper-introsvg-render-feedback"></a>

## IntroSVG: Learning from Rendering Feedback for Text-to-SVG Generation via an Introspective Generator-Critic Framework

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_IntroSVG_Learning_from_Rendering_Feedback_for_Text-to-SVG_Generation_via_an_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_IntroSVG_Learning_from_Rendering_Feedback_for_Text-to-SVG_Generation_via_an_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 基于源码的自回归目标无法检查实际显示结果。
- **核心创新 / 方法** · 示范草稿与渲染批评，重用早期失败样本做纠正监督，再用偏好优化及迭代细化。
- **Baseline** · 表1比较数据标准化配置，表2比较不同生成模型。
- **Benchmark** · 文本到 SVG，以渲染图画质及文本语义等评价。
- **关键结果 / 消融** · 原文比较生成、评审和修正流程的表现。
- **适用条件 / 局限** · 依赖可靠的渲染器和评审，单视图渲染不能评估全部代码结构及可编辑性。

**可复用机制** · 生成可执行视觉程序时，用渲染反馈构造自我修正数据并训练同一模型扮演生成器与评审。

<a id="paper-pcmci-action-confounders"></a>

## Progressive Cross-Modal Causal Intervention for Long-Term Action Recognition

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_Progressive_Cross-Modal_Causal_Intervention_for_Long-Term_Action_Recognition_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_Progressive_Cross-Modal_Causal_Intervention_for_Long-Term_Action_Recognition_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 上下文共现和动作依赖会引入虚假跨模态对齐。
- **核心创新 / 方法** · 以最优传输校正共现，建模动作相互依赖，并用校正文本作为中介开展前门式调整。
- **Baseline** · 对比有无 VLM 的长程动作方法，表3对干预模块消融。
- **Benchmark** · Breakfast、COIN、Charades，报告准确率和 mAP。
- **关键结果 / 消融** · 表1–3显示所测动作识别提升并给出消融。
- **适用条件 / 局限** · 中介和混淆变量的因果假设需独立成立，预测改善本身不能证明去混淆。

**可复用机制** · 长视频动作识别要减轻场景共现捷径时，先校正动作文本关系，再作为视觉去混淆的中介。

<a id="paper-bpgo-reward-trust"></a>

## Learning What to Trust: Bayesian Prior-Guided Optimization for Visual Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_Learning_What_to_Trust_Bayesian_Prior-Guided_Optimization_for_Visual_Generation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_Learning_What_to_Trust_Bayesian_Prior-Guided_Optimization_for_Visual_Generation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 一条提示可对应多种输出，评分噪声使各组和组内差异的置信度不一。
- **核心创新 / 方法** · 用语义先验锚定奖励，给一致组更多更新权，再按先验重新缩放组内优势。
- **Baseline** · 标准 GRPO 及近期变体，表3消融组间和组内调整。
- **Benchmark** · 图像与视频生成，评价语义对齐、画质与收敛，含 VideoAlign 相关结果。
- **关键结果 / 消融** · 表1–3报告生成和训练改善，分别检查两级权重。
- **适用条件 / 局限** · 先验可能偏向常见模式和已有审美，错误锚定可损害多样性。

**可复用机制** · 组相对策略优化可分别估计组间奖励可信度与组内样本区分度。

<a id="paper-binaryattention-one-bit-qk"></a>

## BinaryAttention: One-Bit QK-Attention for Vision and Diffusion Transformers

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_BinaryAttention_One-Bit_QK-Attention_for_Vision_and_Diffusion_Transformers_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xiao_BinaryAttention_One-Bit_QK-Attention_for_Vision_and_Diffusion_Transformers_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 常见4位和8位量化仍保留部分乘加成本，二值化又会损失幅度信息。
- **核心创新 / 方法** · 用符号表示 Q/K 并执行位运算，加学习偏置，以量化感知训练和自蒸馏缓解误差。
- **Baseline** · 全精度注意力、其他量化比较及 FlashAttention2 性能对照。
- **Benchmark** · ImageNet-1K、COCO、ADE20K 及扩散 Transformer，衡量任务表现及 A100 速度。
- **关键结果 / 消融** · 作者报告 A100 上比 FlashAttention2 快超2倍，任务分数保持在所测全精度附近。
- **适用条件 / 局限** · 需要可用内核及重训练，幅值信息关键的层或其他硬件上须重测。

**可复用机制** · 若硬件支持位运算，可只二值化查询键相似度，再用学习补偿和自蒸馏恢复质量。

<a id="paper-flowportal-source-residual-video-editing"></a>

## FlowPortal: Residual-Corrected Flow for Training-Free Video Relighting and Background Replacement

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Gao_FlowPortal_Residual-Corrected_Flow_for_Training-Free_Video_Relighting_and_Background_Replacement_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Gao_FlowPortal_Residual-Corrected_Flow_for_Training-Free_Video_Relighting_and_Background_Replacement_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 直接用新条件降噪会产生与目标编辑无关的结构和细节变化，同条件也可能重建不准。
- **核心创新 / 方法** · 以原样重建应走的路径与实际源条件预测流间的差作为一致性残差，校正目标条件流。
- **Baseline** · 与直接推理、移除前景掩膜和移除高频迁移的方案比较。
- **Benchmark** · 视频重光照和背景替换，报告结构、运动、细节、身份一致以及 CLIP-T、CLIP-I。
- **关键结果 / 消融** · 表 3 移除残差时结构和身份一致性为 0.8516、0.4153，完整时为 0.8804、0.7328；CLIP-T 从 0.3310 略降至 0.3271。
- **适用条件 / 局限** · 残差主要校正源重建偏差，若编辑要求大幅几何变化或掩膜不准，保真约束可能反而限制编辑。

**可复用机制** · 在无训练流编辑中，可以用同条件重建误差校正编辑流，并检查保真与指令匹配的取舍。见图 2、表 3。

<a id="paper-stcdit-first-latent-anchor-guidance"></a>

## STCDiT: Spatio-Temporally Consistent Diffusion Transformer for High-Quality Video Super-Resolution

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_STCDiT_Spatio-Temporally_Consistent_Diffusion_Transformer_for_High-Quality_Video_Super-Resolution_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_STCDiT_Spatio-Temporally_Consistent_Diffusion_Transformer_for_High-Quality_Video_Super-Resolution_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 视频 VAE 的后续潜帧受时序压缩，强运动下难保存局部结构。
- **核心创新 / 方法** · 按运动把视频分段，提取每段未受同等时间压缩的首帧潜变量，给恢复过程提供结构锚点。
- **Baseline** · 比较无锚、只用首帧、不同局部注入方法和用均匀采样替代首帧。
- **Benchmark** · REDS30、UDM10 及真实视频超分辨率；锚帧消融以 MUSIQ 和 DOVER 衡量。
- **关键结果 / 消融** · 表 3 完整方案 MUSIQ、DOVER 为 73.57、60.81，改为均匀采样为 69.72、56.39。
- **适用条件 / 局限** · 依赖具体 VAE 的首帧编码差异，换编码器或遇到首帧损坏时需验证锚点是否有效。

**可复用机制** · 视频潜变量存在时间压缩不均时，可比较优先取未压缩锚帧和均匀取帧对低清视频恢复的影响。见表 3。

<a id="paper-bdmerging-evidence-routed-model-merging"></a>

## BD-Merging: Bias-Aware Dynamic Model Merging with Evidence-Guided Contrastive Learning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xie_BD-Merging_Bias-Aware_Dynamic_Model_Merging_with_Evidence-Guided_Contrastive_Learning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xie_BD-Merging_Bias-Aware_Dynamic_Model_Merging_with_Evidence-Guided_Contrastive_Learning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 静态合并默认测试样本可靠且来自已知任务，偏移后不同专家的可信度变化。
- **核心创新 / 方法** · 在共同标签空间估计证据与不确定性，用多种任务级证据驱动动态合并路由。
- **Baseline** · 比较通用模型合并方案和去掉路由、分布邻域选择或单个置信项的同架构变体。
- **Benchmark** · 视觉多任务分类，在干净与带偏移输入、已见与未见任务下报告准确率。
- **关键结果 / 消融** · 表 3 完整方法在干净、偏移条件为 87.15%、78.78%；去掉路由为 78.31%、67.25%。
- **适用条件 / 局限** · 专家标签语义必须能对齐，辅助证据可能在新的偏移中失准，动态路由也有额外推理成本。

**可复用机制** · 合并专家模型时可用统一标签空间中的不确定性决定路由，并把干净、偏移和未知任务分开评估。见表 3。

<a id="paper-promptdepth-joint-dense-prediction-alignment"></a>

## PromptDepth: Efficient and Promptable Geometric 3D Vision Model for Embodied Intelligence

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_PromptDepth_Efficient_and_Promptable_Geometric_3D_Vision_Model_for_Embodied_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_PromptDepth_Efficient_and_Promptable_Geometric_3D_Vision_Model_for_Embodied_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 几何深度与实例分割都需稠密特征，但测量目标不同，直接共享会拖累其中一项。
- **核心创新 / 方法** · 共享可提示的稠密预测模块，使用 Gram 一致性对齐两项任务的关系表征并调整深度监督。
- **Baseline** · 与各任务单练、联合训练去掉 Gram 或去掉改进深度损失对照。
- **Benchmark** · 两帧在线深度、单目深度和视频对象分割，衡量 AbsRel、δ1、mIoU 和速度。
- **关键结果 / 消融** · 表 4 完整训练 AbsRel 0.075、mIoU 67.1，去掉 Gram 为 0.091、62.4，单练分割为 67.0。
- **适用条件 / 局限** · 实验依赖相邻视图、提示输入和数据中几何与实例的相关性；遮挡和不同来源任务组合需另测。

**可复用机制** · 一个骨干共学深度和交互分割时，可测两任务表示的二阶结构对齐能否缓解负迁移。见表 4。

<a id="paper-elit-tail-drop-budgeted-latent-interface"></a>

## One Model, Many Budgets: Elastic Latent Interfaces for Diffusion Transformers

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Haji-Ali_One_Model_Many_Budgets_Elastic_Latent_Interfaces_for_Diffusion_Transformers_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Haji-Ali_One_Model_Many_Budgets_Elastic_Latent_Interfaces_for_Diffusion_Transformers_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 图像尺寸固定时，空间标记数量决定多数扩散 Transformer 的开销，不能在同模型中平滑调节。
- **核心创新 / 方法** · 用读写交叉注意力把空间标记投影到可变长度的潜序列，训练中随机截掉尾部形成顺序化表示。
- **Baseline** · 与改变补丁大小、随机删除潜标记和各层分配策略比较。
- **Benchmark** · ImageNet-1K 多分辨率、Kinetics-700 及图文生成，以 FID、FDD、IS 等和预算比较。
- **关键结果 / 消融** · 表 4 在保留 25% 标记时，随机删除 FID 为 38.6，截尾为 36.3，直接变补丁的 DiT 为 85.25。
- **适用条件 / 局限** · 极低预算会先损失细节，读写开销与批处理方式也可能限制端到端速度。

**可复用机制** · 给 DiT 提供多档推理预算时，可训练固定顺序的潜变量并随机截断尾部，比较删到同样比例时的质量。见表 4。

<a id="paper-omnisonic-audio-source-gated-conditioning"></a>

## OmniSonic: Towards Universal and Holistic Audio Generation from Video and Text

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Pian_OmniSonic_Towards_Universal_and_Holistic_Audio_Generation_from_Video_and_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Pian_OmniSonic_Towards_Universal_and_Holistic_Audio_Generation_from_Video_and_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 单一视频或文本条件难分辨镜头外事件，联合处理语音和环境声还可能出现一种声音压过另一种。
- **核心创新 / 方法** · 分开用视频和文本为镜头内事件、镜头外事件与语音提供条件，通过专家门控联合生成音频。
- **Baseline** · 与已有视频到音频或文本加视频的模型比较，并对照移除专家门控。
- **Benchmark** · UniHAGen-Bench 评估 FAD、视听对齐、文字对齐、词错误率与时序偏差。
- **关键结果 / 消融** · 表 3 移除门控时 FAD 为 6.12、WER 为 0.56，完整为 3.07、0.14。
- **适用条件 / 局限** · 部分条件依赖已知转录或文本描述，多人重叠说话和未知声音来源仍需验证。

**可复用机制** · 联合生成说话、镜头内和镜头外声音时，可按来源分别建条件并用门控融合，检查环境对齐和语音字错率。见表 3。

<a id="paper-residual-decoding"></a>

## Residual Decoding: Mitigating Hallucinations in Large Vision-Language Models via History-Aware Residual Guidance

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Residual_Decoding_Mitigating_Hallucinations_in_Large_Vision-Language_Models_via_History-Aware_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_Residual_Decoding_Mitigating_Hallucinations_in_Large_Vision-Language_Models_via_History-Aware_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 当前步的高概率候选可能来自语言共现，与图像无关。
- **核心创新 / 方法** · 保存生成时的历史 logits，将由此计算的残差融入当前解码。
- **Baseline** · 表1比较 LLaVA-1.5、InstructBLIP 及 Qwen2.5-VL 的常规解码和替代方法，表5比较解码策略。
- **Benchmark** · POPE 三子集、HallusionBench、CHAIR 以及八个通用评测。
- **关键结果 / 消融** · 表1–3分别报告对象幻觉和普通视觉能力，表4–5评估权重及解码设计。
- **适用条件 / 局限** · 缓存额外使用内存，历史本身失去视觉依据时不能保证纠偏。

**可复用机制** · 视觉生成答复被语言先验带偏时，对照历史 logits 残差和常规解码，再检查幻觉与任务性能。

<a id="paper-a2gc-vpr"></a>

## A2GC: Asymmetric Aggregation with Geometric Constraints for Locally Aggregated Descriptors

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_A2GC_Asymmetric_Aggregation_with_Geometric_Constraints_for_Locally_Aggregated_Descriptors_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_A2GC_Asymmetric_Aggregation_with_Geometric_Constraints_for_Locally_Aggregated_Descriptors_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 对称归一化约束可能不适合图像局部特征与原型的边缘分布。
- **核心创新 / 方法** · 分别校准行列归一化再求平均，将可学习位置兼容性加入相似度。
- **Baseline** · 表1比较已有地点识别方法，表2–5比较骨干、描述符大小、训练策略和组件。
- **Benchmark** · Pitts30k/250k、MSLS 和 NordLand 的检索，报告不同 Recall@K。
- **关键结果 / 消融** · 表1跨场景列比较既有方法，表5单测聚合与空间约束。
- **适用条件 / 局限** · 需要空间近邻支持语义聚合，重复纹理或视角差别很大时需重新评估。

**可复用机制** · 源特征和目标原型分布差异大时，比较非对称聚合和标准双边 Sinkhorn。

<a id="paper-dasp-multimodal-tta"></a>

## Decoupling Stability and Plasticity for Multi-Modal Test-Time Adaptation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/He_Decoupling_Stability_and_Plasticity_for_Multi-Modal_Test-Time_Adaptation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/He_Decoupling_Stability_and_Plasticity_for_Multi-Modal_Test-Time_Adaptation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 同时调整模态会损伤仍可靠的模态，连续调整又会让偏移模态遗忘。
- **核心创新 / 方法** · 由跨特征维冗余诊断模态，以稳定和可塑两支适配器非对称更新，配合 KL 约束。
- **Baseline** · 表1–4比较既有多模态测试时适应，表5分解检测与更新组件。
- **Benchmark** · Kinetics50-C、VGGSound-C 的音视频扰动，单次及持续适应的准确率。
- **关键结果 / 消融** · 表1–4在各噪声及两种更新协议报告结果，表5检验组件贡献。
- **适用条件 / 局限** · 依赖冗余确实反映偏移，多模态同步漂移或天然高相关特征须重新校准诊断。

**可复用机制** · 多模态漂移时先诊断哪个模态偏移，再决定哪组适配参数更新。

<a id="paper-activevla"></a>

## ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_ActiveVLA_Injecting_Active_Perception_into_Vision-Language-Action_Models_for_Precise_3D_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_ActiveVLA_Injecting_Active_Perception_into_Vision-Language-Action_Models_for_Precise_3D_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 固定相机输入无法针对精细控制动态调整观察范围。
- **核心创新 / 方法** · 将3D输入投影到多视角，确定关键区域并据此优化后续感知。
- **Baseline** · 表1–3比较既有 VLA 或三维操作方法，表4消融关键信息。
- **Benchmark** · RLBench 18项任务、COLOSSEUM 14种泛化扰动及 GemBench 的成功率。
- **关键结果 / 消融** · 表1在18项任务中10项排名第一，表2–4对照扰动泛化及组件。
- **适用条件 / 局限** · 依赖可投影且几何可信的三维输入，真实传感延迟和遮挡需独立检验。

**可复用机制** · 三维操作中先定位动作关键区域，再按目标需要选择可用视角与分辨率。

<a id="paper-maskadapt"></a>

## MaskAdapt: Learning Flexible Motion Adaptation via Mask-Invariant Prior for Physics-Based Characters

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Park_MaskAdapt_Learning_Flexible_Motion_Adaptation_via_Mask-Invariant_Prior_for_Physics-Based_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Park_MaskAdapt_Learning_Flexible_Motion_Adaptation_via_Mask-Invariant_Prior_for_Physics-Based_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 直接重训策略为局部目标可能改变其他部位已有行为。
- **核心创新 / 方法** · 随机掩码并约束动作分布稳定后冻结基础策略，只对目标部件训练残差。
- **Baseline** · 表1比较 AMP 与有无 MI 损失，表3比较 AdaptNet、CML，表5比较 MaskedMimic。
- **Benchmark** · 物理角色的动作组合、文本部分目标跟踪，评估归一化熵、成功率及跟踪误差。
- **关键结果 / 消融** · 表1–2分开测掩码稳健性和动作组合，表3比较目标任务成功率。
- **适用条件 / 局限** · 部件并非严格独立，强接触、平衡约束或真实硬件行为需另测。

**可复用机制** · 需要局部改动作而保全身技能时，先训练不随局部缺失显著改变的基础策略，再学被掩码部件的残差。

<a id="paper-medloc-r1"></a>

## MedLoc-R1: Performance-Aware Curriculum Reward Scheduling for GRPO-Based Medical Visual Grounding

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_MedLoc-R1_Performance-Aware_Curriculum_Reward_Scheduling_for_GRPO-Based_Medical_Visual_Grounding_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yang_MedLoc-R1_Performance-Aware_Curriculum_Reward_Scheduling_for_GRPO-Based_Medical_Visual_Grounding_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 严格固定 IoU 奖励在训练前期不够密，可能让组相对更新停滞。
- **核心创新 / 方法** · 滑窗跟踪当前能力并用多条件规则从宽松到严格更新奖励准则。
- **Baseline** · 基于 GRPO，表2–4对照奖励、线性/余弦或固定节奏。
- **Benchmark** · 三医学视觉定位基准，A@0.5、A@0.8 等协议，三次随机运行。
- **关键结果 / 消融** · 表1分模型规模和调度报告效果，表3–4比较固定调度与表现自适应。
- **适用条件 / 局限** · 要求有可逐步加严且能衡量能力的标量反馈，窗口会受任务混合比例影响。

**可复用机制** · 稀疏奖励下按模型近期表现收紧定位门槛，并与固定步数调度对照。

<a id="paper-revisor-dual-attribution"></a>

## REVISOR: Beyond Textual Reflection, Towards Multimodal Introspective Reasoning in Long-Form Video Understanding

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_REVISOR_Beyond_Textual_Reflection_Towards_Multimodal_Introspective_Reasoning_in_Long-Form_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_REVISOR_Beyond_Textual_Reflection_Towards_Multimodal_Introspective_Reasoning_in_Long-Form_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 纯文字反思不会重新获取视觉证据，最终正确也不能说明所重看的片段有用。
- **核心创新 / 方法** · 工具支持按需重看视频段，GRPO 中用双归因奖励分离片段相关性与答案作用。
- **Baseline** · 同模型的纯文本反思、原始基线及去掉归因分量。
- **Benchmark** · VideoMME、LongVideoBench、MLVU、LVBench；另测 Charades-STA、NExT-GQA 的时序定位。
- **关键结果 / 消融** · 原文低视频 token 设置报告 VideoMME 65.7%，表3比较奖励分量。
- **适用条件 / 局限** · 依赖重新采样捕获可辨证据；错误片段归因会训练错误工具使用。

**可复用机制** · 长视频复查时分别奖励选对需重看片段与根据片段修正答案，避免只强化文本自检。

<a id="paper-hcep-hierarchical-concepts"></a>

## Hierarchical Concept Embedding & Pursuit for Interpretable Image Classification

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Nguyen_Hierarchical_Concept_Embedding__Pursuit_for_Interpretable_Image_Classification_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Nguyen_Hierarchical_Concept_Embedding__Pursuit_for_Interpretable_Image_Classification_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 无约束稀疏编码可能命中类别但回收互相冲突的祖先概念。
- **核心创新 / 方法** · 按概念树构造带几何层次的嵌入，再做分层稀疏追踪；分析根路径恢复条件。
- **Baseline** · 普通稀疏编码及已有概念可解释分类方案。
- **Benchmark** · ImageNette、ImageNet、CIFAR-100，测分类和概念支持恢复，ImageNet 有少样本结果。
- **关键结果 / 消融** · 图8–9报告较好的路径及分类恢复表现。
- **适用条件 / 局限** · 假设概念具有可信层级，多个并行概念或非树结构不一定满足恢复条件。

**可复用机制** · 用概念向量解释分类时，如果概念有层级，应在表示与稀疏解码同时保证父子一致。

<a id="paper-alvts-layer-wise-token-routing"></a>

## One Layer's Trash is Another Layer's Treasure: Adaptive Layer-wise Visual Token Selection in LVLMs

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_One_Layers_Trash_is_Another_Layers_Treasure_Adaptive_Layer-wise_Visual_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_One_Layers_Trash_is_Another_Layers_Treasure_Adaptive_Layer-wise_Visual_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 一层不重要的视觉区域可能在其他层变重要，永久裁剪会丢失后续证据。
- **核心创新 / 方法** · 用带重要性一致约束的低秩选择器识别本层需更新的词元，跳过部分下一层与已更新词元重新合并。
- **Baseline** · 不同预算下比较现有视觉裁剪及完整 LLaVA。
- **Benchmark** · LLaVA-1.5-7B/13B 和 LLaVA-NeXT-7B 多模态任务，测平均性能和减少 token 比例。
- **关键结果 / 消融** · 表1–3报告多个压缩率下的保真表现。
- **适用条件 / 局限** · 未选词元仍占内存，路由自身也要成本，短序列或注意力强耦合时收益可能小。

**可复用机制** · 按层压缩视觉计算时让未选 token 跳过本层并保留给后层重新选择。

<a id="paper-bise-bias-invariant-subnetworks"></a>

## Bias In, Bias Out? Finding Unbiased Subnetworks in Vanilla Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/De_Moura_Matos_Bias_In_Bias_Out_Finding_Unbiased_Subnetworks_in_Vanilla_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/De_Moura_Matos_Bias_In_Bias_Out_Finding_Unbiased_Subnetworks_in_Vanilla_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 架构已编码群体或环境捷径，收集无偏新数据和完整重训成本高。
- **核心创新 / 方法** · 学习筛选现有网络参数，保留所测偏置较低的子网，原参数不更新。
- **Baseline** · 原始模型和现有去偏方法，改变稀疏设置。
- **Benchmark** · BiasedMNIST、Corrupted-CIFAR10 等偏置控制设置，报告准确率、稀疏度和 MFLOPs。
- **关键结果 / 消融** · 表1–3显示所测训练好的网络可抽到较少依赖设定偏置的子网。
- **适用条件 / 局限** · 能抑制已知偏置不意味着无偏；剪枝可能舍弃少数类的有用特征。

**可复用机制** · 训练后去捷径可先比较从冻结模型抽取的稀疏子网与重新训练，而非假设整网均依赖偏置。

<a id="paper-conceptprism-residual-tokens"></a>

## ConceptPrism: Concept Disentanglement in Personalized Diffusion Models via Residual Token Optimization

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Kim_ConceptPrism_Concept_Disentanglement_in_Personalized_Diffusion_Models_via_Residual_Token_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Kim_ConceptPrism_Concept_Disentanglement_in_Personalized_Diffusion_Models_via_Residual_Token_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 背景和姿态等偶然因素容易被身份词元记住，妨碍文本编辑。
- **核心创新 / 方法** · 联合优化目标和逐图残差词元，以重建损失保留信息，以排斥损失将跨图共性移到共享词元。
- **Baseline** · DreamBench 个性化基线，表2–3消融词元设置与残差长度。
- **Benchmark** · DreamBench，CLIP-T 测文本对齐，DINO 和 CLIP-I 测参考概念一致性。
- **关键结果 / 消融** · 表1–3比较共享概念保真和文本匹配，指出残差词元及长度影响。
- **适用条件 / 局限** · 参考图共同出现的背景可能仍被当成目标，需视角或环境多样性才能更好分离。

**可复用机制** · 少量参考图个性化时，给共享概念及每个实例分别分配 token，并阻止实例 token 吞掉共享属性。

<a id="paper-fine-active-forgetting-noisy-supervision"></a>

## Revisiting Learning with Noisy Labels: Active Forgetting and Noise Suppression

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Sheng_Revisiting_Learning_with_Noisy_Labels_Active_Forgetting_and_Noise_Suppression_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Sheng_Revisiting_Learning_with_Noisy_Labels_Active_Forgetting_and_Noise_Suppression_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 筛选低损失样本只能减少继续接触错标，不能直接纠正已拟合的错误。
- **核心创新 / 方法** · 训练中评估可能被吸收的标签噪声，以主动遗忘清理已学错误，再用负学习抑制进一步拟合。
- **Baseline** · 在 SED 上分别加入主动遗忘、噪声抑制和完整方案，对照 SED、ACT 和 CA2C 等。
- **Benchmark** · CIFAR100N、CIFAR80N 不同对称与非对称噪声条件，以及 Web-Aircraft、Web-Bird、Web-Car，以分类准确率评估。
- **关键结果 / 消融** · 表 3 在 CIFAR100N 的 80% 对称噪声下，SED 为 38.15%，主动遗忘为 42.46%，仅噪声抑制为 42.70%，联合为 45.54%。
- **适用条件 / 局限** · 错标识别不准时，遗忘可能损害难学但合法的样本；需单测真实标签噪声与长尾效果。

**可复用机制** · 对已被模型拟合的错标样本，可比较主动清除已学噪声与仅抑制后续学习，再用不同噪声类型验证。见表 3。

<a id="paper-finer-paired-fine-grained-visual-negatives"></a>

## FINER: MLLMs Hallucinate under Fine-grained Negative Queries

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_FINER_MLLMs_Hallucinate_under_Fine-grained_Negative_Queries_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xiao_FINER_MLLMs_Hallucinate_under_Fine-grained_Negative_Queries_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 模型会因看到真实对象，就认同同一问题里不存在的属性、对象或关系。
- **核心创新 / 方法** · 构造细粒度负查询与对应正查询，基于两类查询的答案偏好更新模型。
- **Baseline** · 对照 InternVL-3.5-8B、仅负查询 DPO 和正负查询下的监督微调。
- **Benchmark** · FINER-CompreCap、FINER-DOCCI 的对象、属性、关系及开放式问题，用配对准确率，另测 RePOPE 和 MMStar。
- **关键结果 / 消融** · 表 4 完整 DPO 的关系得分 64.1，基础为 49.8，仅负查询 DPO 为 52.4；正负查询的 SFT 在对象分下降。
- **适用条件 / 局限** · 需要合成的错误只改变指定属性，生成时引入其他歧义可能让配对得分和真实幻觉偏离。

**可复用机制** · 视觉幻觉训练可用同时包含真细节和局部错误的正负问题对，并比较 DPO 与只给正确答案的监督微调。见表 4。

<a id="paper-morel-bidirectional-keyframe-anchor-relay"></a>

## MoRel: Long-Range Flicker-Free 4D Motion Modeling via Anchor Relay-based Bidirectioanl Blending with Hierarchical Densification

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Kwak_MoRel_Long-Range_Flicker-Free_4D_Motion_Modeling_via_Anchor_Relay-based_Bidirectioanl_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Kwak_MoRel_Long-Range_Flicker-Free_4D_Motion_Modeling_via_Anchor_Relay-based_Bidirectioanl_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 直接延长单一动态高斯模型会抬高显存，独立分段又会引入跨段闪烁。
- **核心创新 / 方法** · 在不同关键帧建立局部基准，在锚点层学习双向形变并自适应混合。
- **Baseline** · 与 4DGS、MoDec-GS、LocalDyGS、GIFStream 和分块 4DGS 比较。
- **Benchmark** · SelfCapLR 的长视频新视角，报告画质、时间一致性 tOF、训练显存与渲染速度。
- **关键结果 / 消融** · 表 2 的 MoRel tOF 为 0.203、训练显存约 6000 MB，全局 4DGS 为 0.222、约 18000 MB，独立分块为 0.680、约 4500 MB。
- **适用条件 / 局限** · 关键帧选择和双向匹配依赖视角覆盖，快速运动、长遮挡以及无可重见的对象需重试。

**可复用机制** · 建模长期动态场景时可转发多个局部基准，并双向融合段间形变，比较一次全局建模和独立分段。见表 2。

<a id="paper-mulo-sd-spatial-local-draft-verification"></a>

## Multi-Scale Local Speculative Decoding for Image Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Peruzzo_Multi-Scale_Local_Speculative_Decoding_for_Image_Generation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Peruzzo_Multi-Scale_Local_Speculative_Decoding_for_Image_Generation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 逐标记图像生成慢，按光栅顺序重采样不能利用错误多集中在局部空间的性质。
- **核心创新 / 方法** · 从低分辨率起草，放大到高分辨率候选，由主模型平行验证，在出错的空间邻域局部处理。
- **Baseline** · 比较正常解码、ZipAR、EAGLE-2 和 LANTERN。
- **Benchmark** · MS-COCO 5k 等图像生成，用 512p 与 1024p 的实际时延、GenEval、DPG-Bench、FID、HPSv2。
- **关键结果 / 消融** · 表 1 的 512p Tar-7B 加速 2.03 倍，GenEval 保持 85.1；但 LlamaGen-XL 上仅 1.40 倍，慢于 ZipAR 的 1.88 倍。
- **适用条件 / 局限** · 收益受低分辨率草稿质量和骨干影响，细纹理和非局部一致性要求高时需检查。

**可复用机制** · 图像自回归加速可用低分辨率草稿，并把拒绝后的重采样局限在空间邻域，与按序全量重试比较。见表 1。

<a id="paper-decentralized-certified-unlearning-client-views"></a>

## Fully Decentralized Certified Unlearning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Lamri_Fully_Decentralized_Certified_Unlearning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Lamri_Fully_Decentralized_Certified_Unlearning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 去中心化网络没有维护统一状态的服务器，遗忘保证要明确每个参与方能观察到什么。
- **核心创新 / 方法** · 按客户端视图定义网络遗忘证书，以受约束的随机游走更新在删除与保留数据之间修正模型并分析隐私代价。
- **Baseline** · 在凸情形对照通过群体隐私复用去中心化差分隐私的方案，实证采用去中心化图像分类设置。
- **Benchmark** · 理论比较凸与非凸目标的遗忘、效用和规模边界，实证包括 CIFAR-10 与 MNIST 的保留测试和汇总防御效果。
- **关键结果 / 消融** · 表 2 给出通用群体隐私的噪声随删除规模线性增加，专门遗忘方案在给定凸设置可避免同一依赖。
- **适用条件 / 局限** · 证书依赖固定拓扑和可观察视图等假设；节点串通、拓扑变动和非独立划分需要独立审查。

**可复用机制** · 无中心协调的数据删除可采用客户端消息视图定义认证边界，并比较通用差分隐私与专门事后遗忘的可承受规模。见定理 3.5 与表 2。

<a id="paper-cov-align-query-independent-visual-grouping"></a>

## CoV-Align: Efficient Fine-grained Cross-Modal Alignment with Cohesive Visual Semantics Priority

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_CoV-Align_Efficient_Fine-grained_Cross-Modal_Alignment_with_Cohesive_Visual_Semantics_Priority_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_CoV-Align_Efficient_Fine-grained_Cross-Modal_Alignment_with_Cohesive_Visual_Semantics_Priority_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 所有文字与视觉块逐对比较成本大，重复的视觉区域还会削弱可区分语义。
- **核心创新 / 方法** · 在不依赖文本查询的视觉分支上聚合相近的块，再约束组内凝聚和组间判别进行细粒度对齐。
- **Baseline** · 与 LAPS 等图文检索方法和同模型消融比较，分别增添粗粒度区域、视觉对比和空间集中损失。
- **Benchmark** · Flickr30K、MS-COCO 的图文双向检索，用 R@1、R@10、FLOPs、显存。
- **关键结果 / 消融** · 表 3 文搜图 R@1 从 70.4 到加入粗视觉语义后的 73.9，完整为 78.5；把区域由 8 增至 16 时降到 75.2。
- **适用条件 / 局限** · 查询无关的聚合可能压掉低显著性区域，对指代、细粒度和不同图像密度应重新设区域数。

**可复用机制** · 大量图文匹配前可先独立压缩视觉块为语义区域，比较区域数对双向检索的作用。见表 3、4。

<a id="paper-qvic-memory-feedback-visual-compression"></a>

## Question-guided Visual Compression with Memory Feedback for Long-Term Video Understanding

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yamao_Question-guided_Visual_Compression_with_Memory_Feedback_for_Long-Term_Video_Understanding_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yamao_Question-guided_Visual_Compression_with_Memory_Feedback_for_Long-Term_Video_Understanding_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 逐帧压缩不易保留完整事件；只存历史表征无法改变后续片段会压掉什么。
- **核心创新 / 方法** · 把问句和相关历史表征一起输入视觉压缩注意力，让过去信息决定当前片段保留的证据。
- **Baseline** · 比较朴素压缩、只加记忆、加反馈及不同注意力掩膜。
- **Benchmark** · MLVU 和 VNBench 长视频问答，报告准确率与采样率。
- **关键结果 / 消融** · 表 3 在同为 2 FPS 下，VNBench 长组由只加记忆的 40.9 提高到反馈时的 55.1，完整为 58.7。
- **适用条件 / 局限** · 依赖找回正确历史片段，记忆错误也可能让压缩丢掉新证据，应加测很长干扰段。

**可复用机制** · 长视频的记忆可以在压缩之前反向引导视觉注意，而非只供解码读取；应在固定采样率上比较效果。见表 3。

<a id="paper-did-generated-image-detection"></a>

## A Difference-in-Difference Approach to Detecting AI-Generated Images

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Qi_A_Difference-in-Difference_Approach_to_Detecting_AI-Generated_Images_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Qi_A_Difference-in-Difference_Approach_to_Detecting_AI-Generated_Images_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 先进生成图像越来越接近真实输入，单次重建残差的类别区分变弱。
- **核心创新 / 方法** · 构造比较和对照两组的重建误差，再取两组误差的差作为检测特征。
- **Baseline** · 表1–4比较其他已训练检测器及不同训练数据来源。
- **Benchmark** · ImageNet 与 ADM、LAION 与 Kan.3 或 SDXL 训练，测试多生成器准确率，表3单测 GAN。
- **关键结果 / 消融** · 表1–4报告跨训练域和生成来源评估，正文解释二阶误差对方差的作用。
- **适用条件 / 局限** · 依赖对照组跟踪共同误差，域变化同时改变对照误差时须复验。

**可复用机制** · 当重建误差的样本间方差掩盖来源差别时，用二阶差分抵消共同误差。

<a id="paper-competitorformer"></a>

## CompetitorFormer: Mitigating Query Conflicts for 3D Instance Segmentation via Competitive Strategy

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_CompetitorFormer_Mitigating_Query_Conflicts_for_3D_Instance_Segmentation_via_Competitive_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_CompetitorFormer_Mitigating_Query_Conflicts_for_3D_Instance_Segmentation_via_Competitive_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 多个查询争同一目标会碎片化掩码并减慢收敛。
- **核心创新 / 方法** · 每阶段前加入查询竞争层，结合相对关系编码与排名交叉注意力。
- **Baseline** · 表1比较 Relation3D 等，表2逐项切换三个部件。
- **Benchmark** · 四项3D实例分割基准，比较 mAP，ScanNetV2 消融另报告 mAP50、mAP25。
- **关键结果 / 消融** · 正文报告相对 Relation3D 的改进并以图3展示去掉竞争层后的分数分布。
- **适用条件 / 局限** · 相似但真正重叠的实例可能被竞争抑制，应按拥挤程度评估。

**可复用机制** · 并行查询争抢同一实例时，可在每层解码前建查询间竞争，而非只在输出去重。

<a id="paper-lenswalk"></a>

## LensWalk: Agentic Video Understanding by Planning How You See in Videos

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_LensWalk_Agentic_Video_Understanding_by_Planning_How_You_See_in_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_LensWalk_Agentic_Video_Understanding_by_Planning_How_You_See_in_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 预处理后一次性看固定表示，无法依据刚发现的线索重新观察。
- **核心创新 / 方法** · 推理器在看、规划和回看之间循环，配置观察器的时间区间及采样密度。
- **Baseline** · 表1–2比较固定或代理视频模型，表3组合不同推理器和观察器。
- **Benchmark** · 长视频和视频推理基准，评价准确率并比较不同控制/观察模型。
- **关键结果 / 消融** · 表1显示同一 o3 推理器更换观察器会明显改变各项得分，表3检验组件可替换性。
- **适用条件 / 局限** · 依赖按需访问原视频，也会产生多回合调用开销；极短事件当初未发现时仍可能漏掉。

**可复用机制** · 视频代理应控制取证的时间范围和密度，并保留可核验的异时证据。

<a id="paper-tpsegformer"></a>

## Hilbert Curve-Based Attention Enabling Topology-Preserving Image Tensor Representation for Semantic Segmentation Network

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_Hilbert_Curve-Based_Attention_Enabling_Topology-Preserving_Image_Tensor_Representation_for_Semantic_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_Hilbert_Curve-Based_Attention_Enabling_Topology-Preserving_Image_Tensor_Representation_for_Semantic_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 图像显著边界在逐行展开时可能被远距分开，增加序列模块恢复空间关系的难度。
- **核心创新 / 方法** · 在分割解码器用 Hilbert 曲线展平，同时用轻量多尺度融合。
- **Baseline** · 表3比较不同分割网络，表4同框架比较各展平曲线。
- **Benchmark** · BD3 与 Dacl10k 的 mIoU、准确率；表1分析局部性损失，表2比耗时。
- **关键结果 / 消融** · BD3 mIoU 80.77%，表4逐行展平为75.58%；Dacl10k mIoU 44.27%。
- **适用条件 / 局限** · Hilbert 仅减少二维邻接断裂，不能保证任意相邻区域都连续，长宽不整齐的输入需评估填充。

**可复用机制** · 将二维网格展平进入序列模块前，对照局部性更强的 Hilbert 排序与普通逐行排序。

<a id="paper-myego-evidence-audit"></a>

## Ego-Grounding for Personalized Question-Answering in Egocentric Videos

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_Ego-Grounding_for_Personalized_Question-Answering_in_Egocentric_Videos_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xiao_Ego-Grounding_for_Personalized_Question-Answering_in_Egocentric_Videos_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 只报总体准确率无法判断模型没看到关键片段还是看到了但认不出佩戴者。
- **核心创新 / 方法** · 构造针对佩戴者活动、物品及过去行为的问题，并对比均匀采样与答案时刻关键帧。
- **Baseline** · 表2比较开闭源、显式推理及规模模型，含 GPT-5 和 Qwen3-VL；表3同模型切换输入。
- **Benchmark** · MyEgo 541长视频、约5000问题，多选与开放问答，按当前与过去证据分组。
- **关键结果 / 消融** · 表3明确提供关键时刻可改善表现，但过去事件的证据增益减弱；论文未观察到扩规模或显式推理带来一致收益。
- **适用条件 / 局限** · 答案时刻是诊断上界，部署时通常不可用；跨不同事件时间分布需重测。

**可复用机制** · 第一视角记忆问答可用已知答案时刻作对照，区分证据检索失败与对证据的推理失败。

<a id="paper-game-evolving-scenes"></a>

## Gaussian Mapping for Evolving Scenes

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yugay_Gaussian_Mapping_for_Evolving_Scenes_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yugay_Gaussian_Mapping_for_Evolving_Scenes_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 离开视野期间发生的对象移动与旧帧共同优化会产生重影或错误结构。
- **核心创新 / 方法** · 检测可见结构变化后局部更新高斯图，并管理关键帧以减少陈旧证据的干扰。
- **Baseline** · 表1–2比较静态地图方案，表3–4分别消融场景更新和关键帧管理。
- **Benchmark** · Flat、Aria，报告视角渲染 PSNR、SSIM、LPIPS 和耗时。
- **关键结果 / 消融** · 表3–4分开验证新观测适应与旧帧管理，两者均可影响渲染。
- **适用条件 / 局限** · 改变必须在重访时可观测，持续遮挡和相机姿态偏差可能干扰更新判据。

**可复用机制** · 维护长期3D记忆时，按局部变化淘汰过时观测并保留仍有效的关键帧。

<a id="paper-merit-raw-translation"></a>

## MERIT: Multi-domain Efficient RAW Image Translation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_MERIT_Multi-domain_Efficient_RAW_Image_Translation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_MERIT_Multi-domain_Efficient_RAW_Image_Translation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 逐相机对训练不易扩展，图像相似损失不保证目标传感噪声统计正确。
- **核心创新 / 方法** · 用单模型条件化目标传感器，并加入显式匹配噪声统计的损失。
- **Baseline** · 表3比较 UVCGAN、Xie 等和 MERIT，表4消融。
- **Benchmark** · MDRAW 跨相机 RAW 转换，报告 MAE、PSNR、SSIM、KL 散度。
- **关键结果 / 消融** · 表3逐一列出转换方向，表4验证设计作用。
- **适用条件 / 局限** · 真实输入缺像素级对齐，结果的对应误差可能影响噪声评测，新传感器需要校准统计。

**可复用机制** · 跨传感器统一映射时，可将信号依赖噪声匹配单独作为目标，并按方向验收。

<a id="paper-masked-dual-path-distillation"></a>

## Memory-Efficient Transfer Learning with Fading Side Networks via Masked Dual Path Distillation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Memory-Efficient_Transfer_Learning_with_Fading_Side_Networks_via_Masked_Dual_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Memory-Efficient_Transfer_Learning_with_Fading_Side_Networks_via_Masked_Dual_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 旁路免去对大骨干反传却增加上线时延。
- **核心创新 / 方法** · 冻结骨干与可学旁路互相传递知识，利用掩码和跨层特征蒸馏使部署路径无需旁路。
- **Baseline** · 比较 PETL、METL 及多种骨干下的已有旁路机制。
- **Benchmark** · GLUE、VTAB-1K 和视觉语言任务，比较准确率、参数、显存与时延。
- **关键结果 / 消融** · 作者报告较现有方案推理至少加速25.2%。
- **适用条件 / 局限** · 训练旁路仍须算力，骨干能否吸收新任务信号取决于读出与特征可适配性。

**可复用机制** · 用轻量旁路节省微调显存时，可在训练阶段做双路蒸馏，部署时移除旁路。

<a id="paper-laof-latent-action-flow"></a>

## LAOF: Robust Latent Action Learning with Optical Flow Constraints

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Bu_LAOF_Robust_Latent_Action_Learning_with_Optical_Flow_Constraints_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Bu_LAOF_Robust_Latent_Action_Learning_with_Optical_Flow_Constraints_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 像素重建会编码背景干扰，动作标签稀少。
- **核心创新 / 方法** · 以智能体运动的光流作伪监督学习潜动作，对照连续和离散编码。
- **Baseline** · 比较现有潜动作及少标注动作监督方法。
- **Benchmark** · LIBERO 模仿学习评估误差与任务表现，PROCGEN 评估离散潜动作和强化学习。
- **关键结果 / 消融** · 原文报告零动作标签在所测设置达到或超过1%监督基线，也检验最高10%标注。
- **适用条件 / 局限** · 光流不是动作因果信号，若相机与环境运动占主导则需过滤。

**可复用机制** · 从无动作标签视频学潜动作时，用智能体相关光流隔离任务无关运动。

<a id="paper-x-avdt-cross-modal-forensics"></a>

## X-AVDT: Audio-Visual Cross-Attention for Robust Deepfake Detection

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Kim_X-AVDT_Audio-Visual_Cross-Attention_for_Robust_Deepfake_Detection_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Kim_X-AVDT_Audio-Visual_Cross-Attention_for_Robust_Deepfake_Detection_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 只学习某家合成器的像素伪影容易在新生成器上失效。
- **核心创新 / 方法** · 以生成模型表示中的视听对应与视频差异作为检测证据，按生成器划分验证。
- **Baseline** · 对照现有深度伪造检测器并测外部基准。
- **Benchmark** · MMDF 集合包含多类生成范式，另有未见生成器和外部数据，以准确率等评价。
- **关键结果 / 消融** · 作者报告所测条件下准确率提升13.1%。
- **适用条件 / 局限** · 视听不同步也可来自真实录制条件，检测信号随生成器变化仍需校准。

**可复用机制** · 评估合成视频检测时，应把音画一致性信号与视觉残差一起做跨生成器验证。

<a id="paper-surf-noise-reshifting"></a>

## SURF: Signature-Retained Fast Video Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Ding_SURF_Signature-Retained_Fast_Video_Generation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Ding_SURF_Signature-Retained_Fast_Video_Generation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 从一开始直接用低分辨率推理会丢全局布局与运动特征。
- **核心创新 / 方法** · 用无需训练的重调噪声在早期后切换分辨率，再训练预览到高分辨率的短步细化映射。
- **Baseline** · Wan 2.1 原生推理、其他生成加速插件和视频超分。
- **Benchmark** · 高分辨率视频的速度、布局语义和运动一致性；表3与超分比较。
- **关键结果 / 消融** · 原文报告生成提速并较低分辨率直接运行保留更多特征。
- **适用条件 / 局限** · 分辨率切换时间及映射可能随骨干变化，细化也可能引入新细节错误。

**可复用机制** · 预览生成先按模型原分辨率完成早期去噪，之后降分辨率再用映射细化。

<a id="paper-star-gui-state-aware"></a>

## See, Think, Act: Teaching Multimodal Agents to Effectively Interact with GUI by Identifying Toggles

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_See_Think_Act_Teaching_Multimodal_Agents_to_Effectively_Interact_with_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wu_See_Think_Act_Teaching_Multimodal_Agents_to_Effectively_Interact_with_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 代理常把开启或关闭理解为无条件点击，导致已有正确状态被切换。
- **核心创新 / 方法** · 训练代理识别当前和期望状态，再据此决定动作。
- **Baseline** · 四种代理有无状态推理，另比较公用代理基准。
- **Benchmark** · 二元界面控件执行准确率，三套代理任务及动态环境评测。
- **关键结果 / 消融** · 作者在四种代理实验报告执行改善超30%。
- **适用条件 / 局限** · 状态不可见、控件异步及多状态设置需要独立验证。

**可复用机制** · 执行二元界面目标前先读当前状态；若已符合目标，输出不操作。

<a id="paper-braincodec-contextual-sensor-encoding-inversion"></a>

## Meta-Learning In-Context Enables Training-Free Cross Subject Brain Decoding

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Nan_Meta-Learning_In-Context_Enables_Training-Free_Cross_Subject_Brain_Decoding_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Nan_Meta-Learning_In-Context_Enables_Training-Free_Cross_Subject_Brain_Decoding_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 不同被试的体素及其功能响应会变化，直接共享同一空间映射或逐人训练代价高。
- **核心创新 / 方法** · 用图像与响应示例在上下文中先估计各体素的编码特征，再合并体素上下文进行刺激语义反演。
- **Baseline** · 与采用解剖对齐的 MindEye2 和 TGBD 比较，同时在未见被试上测无需微调的推理。
- **Benchmark** · 自然场景 fMRI 的未见受试者，表 1 在 907 个图像候选中报告 Top-1、Top-5。
- **关键结果 / 消融** · 表 1 用 200 个示例时 BrainCoDec 平均为 22.7%、54.0%，MindEye2 为 3.90%、9.81%。
- **适用条件 / 局限** · 需要新被试有图像与传感配对示例，扫描协议、目标域或信号噪声变化时应单测。

**可复用机制** · 传感维度跨个体变化时，可先按维度从少量配对示例估计个体编码，再从新观测逆推，而无需对齐坐标或更新权重。见表 1。

<a id="paper-clex-non-target-logit-consistency"></a>

## CLEX: Complementary Label Exchange Learning for Noisy Facial Expression Recognition

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_CLEX_Complementary_Label_Exchange_Learning_for_Noisy_Facial_Expression_Recognition_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_CLEX_Complementary_Label_Exchange_Learning_for_Noisy_Facial_Expression_Recognition_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 错标场景中只监督目标类，无法约束两个增强视图对非目标类产生的假高置信度。
- **核心创新 / 方法** · 随机交换增强视图中部分非目标 logit，对其归一化并施加跨视图约束。
- **Baseline** · 对照交叉熵、逐步加入增强一致性、非目标交换和归一化，并与 SCN、DMUE、NLA 等比较。
- **Benchmark** · RAF-DB 的 30% 对称标签噪声和 AffectNet 等分类，报告测试准确率。
- **关键结果 / 消融** · 表 3 的基线为 81.36%，加增强一致性为 84.94%，再加交换单步为 84.73%，完整组合为 87.35%。
- **适用条件 / 局限** · 假设增强没有改变正确标签，交换单独加入未必改善；应在非对称错标和分布差异中验证。

**可复用机制** · 带噪标签分类可以增加增强视图间的非目标类别约束，区分 logit 交换、归一化与完整损失的作用。见表 3。

<a id="paper-clip-intramodal-misalignment-task-axis-control"></a>

## Reevaluating the Intra-Modal Misalignment Hypothesis in CLIP

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Herzog_Reevaluating_the_Intra-Modal_Misalignment_Hypothesis_in_CLIP_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Herzog_Reevaluating_the_Intra-Modal_Misalignment_Hypothesis_in_CLIP_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 从 CLIP 图搜图表现或文本投影收益直接推断图像模态内失配，可能混淆任务标签语义与嵌入几何。
- **核心创新 / 方法** · 在多种模型复核模态内指标，并把图像投影到类别名方差轴上，与转为文本匹配对照。
- **Baseline** · 比较 CLIP、SigLIP 及含图像内目标的 DINO、SigLIP2，并对照原嵌入与 OTI。
- **Benchmark** · 13 个图搜图数据集的 mAP，以及不使用文本提示的小样本分类。
- **关键结果 / 消融** · 表 3 中 CLIP-B/32 的平均 mAP 为 41.6，OTI 为 42.9，沿类别语义轴投影为 49.0；类似趋势不限于图文训练。
- **适用条件 / 局限** · 投影收益更依赖任务标签指向图像主要概念，细粒度和非主语义检索未必因此获益。

**可复用机制** · 图像检索变差时先测试嵌入评测的语义轴是否与任务匹配，并用图像内对比模型做对照，再决定是否改训练损失。见表 3。

<a id="paper-relzero-patch-relations-defensive-authentication"></a>

## Rel-Zero: Harnessing Patch-Pair Invariance for Robust Zero-Watermarking Against AI Editing

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Rel-Zero_Harnessing_Patch-Pair_Invariance_for_Robust_Zero-Watermarking_Against_AI_Editing_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_Rel-Zero_Harnessing_Patch-Pair_Invariance_for_Robust_Zero-Watermarking_Against_AI_Editing_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 修改图像会改变内容外观，使只使用全局特征的来源指纹难以稳定确认原始内容。
- **核心创新 / 方法** · 使用图像块之间的关系作为无嵌入验证特征，避免为了标记本身改变原图。
- **Baseline** · 与其他水印及零水印方法比较，并替换特征骨干和关系模块做消融。
- **Benchmark** · 作者的图像编辑鲁棒性集，报告固定 0.1% 误报率的真阳率及图像保真指标。
- **关键结果 / 消融** · 表 2 指定编辑条件下，完整配置真阳率 97.43%，替换为 ResNet-50 骨干为 85.21%。
- **适用条件 / 局限** · 原文发现大范围语义重生成更难，鲁棒验证也不等于判断图中事件是否真实。

**可复用机制** · 图像来源验证可比较局部特征关系与整图表示，按固定误报率报告编辑后检测效果。见表 1、2。

<a id="paper-cooperative-unrolling-task-feature-exchange"></a>

## Joint Spectral Image Reconstruction and Semantic Segmentation with Cooperative Unfolding

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/He_Joint_Spectral_Image_Reconstruction_and_Semantic_Segmentation_with_Cooperative_Unfolding_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/He_Joint_Spectral_Image_Reconstruction_and_Semantic_Segmentation_with_Cooperative_Unfolding_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 先从压缩高光谱测量重建再分割，重建优化不一定保留对语义有用的信号。
- **核心创新 / 方法** · 同时展开测量一致性和分割更新，并借助交叉聚合超标记使两支交换信息。
- **Baseline** · 对照先重建再分割及同骨干逐步加入耦合更新和 LISTA。
- **Benchmark** · FVgNET 的合成与真实高光谱测量，以重建 PSNR、语义 mIoU 和 FLOPs 衡量。
- **关键结果 / 消融** · 表 2 从 37.33 dB、84.31% mIoU 到耦合后的 37.90 dB、86.08%，再加 LISTA 到 38.03 dB、86.55%。
- **适用条件 / 局限** · 依赖有效测量模型与带语义标注的数据，重建和语义不一致时应单独检查任务耦合是否引入偏差。

**可复用机制** · 测量重建与语义任务强相关时，可比较平行交互更新和单向先重建后识别，按质量和语义指标共同评估。见表 2。

<a id="paper-rsiat-fixed-shared-incremental-adapter"></a>

## Representation-Steered Incremental Adapter-Tuning for Class-Incremental Learning with Pre-Trained Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_Representation-Steered_Incremental_Adapter-Tuning_for_Class-Incremental_Learning_with_Pre-Trained_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_Representation-Steered_Incremental_Adapter-Tuning_for_Class-Incremental_Learning_with_Pre-Trained_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 每新增任务训练独立适配器会令参数线性增长，多个适配器的类表示也可能不一致。
- **核心创新 / 方法** · 维持单适配器，先整理类间表征，然后用带残差的自编码投影对齐任务切换前后的特征。
- **Baseline** · 比较预训练 ViT 的类增量基线，并消融正交、对齐、残差投影与额外表示训练。
- **Benchmark** · ImageNet-R/A 与其他类增量基准，使用任务平均准确率及最后任务后的整体准确率。
- **关键结果 / 消融** · 表 3 的 ImageNet-R B0I20 平均为 86.92%，基线 83.63%；移除残差投影结构的对应变体为 80.59%。
- **适用条件 / 局限** · 共享容量不随任务增长，强分布漂移或多类高度重叠时需验证旧表征保持。

**可复用机制** · 类增量学习可以保持一个共享适配器，通过对齐新旧表示控制遗忘，比较残差对齐和不对齐的差异。见表 3。

<a id="paper-sed-ud"></a>

## SeD-UD: An Influence-Driven and Hierarchically-Decoupled Information Bottleneck for Multimodal Intent Recognition

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_SeD-UD_An_Influence-Driven_and_Hierarchically-Decoupled_Information_Bottleneck_for_Multimodal_Intent_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_SeD-UD_An_Influence-Driven_and_Hierarchically-Decoupled_Information_Bottleneck_for_Multimodal_Intent_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 固定维数不能覆盖不同输入的噪声水平，一次压缩不易兼顾去重和去噪。
- **核心创新 / 方法** · 按估计的冗余和噪声影响动态选择压缩维数与参数，用分层信息瓶颈处理。
- **Baseline** · 表1比较多模态意图识别，表2比较 CH-SIMS，表3报告单样本推理时长。
- **Benchmark** · 两套意图识别数据及 CH-SIMS 跨任务实验，附时延比较。
- **关键结果 / 消融** · 表1–3分别报告主任务、迁移设置与运行开销。
- **适用条件 / 局限** · 门控需要可靠估计噪声，罕见但关键细节可能被误当作冗余。

**可复用机制** · 把跨模态重复与各模态噪声分开压缩，并按输入决定瓶颈维度。

<a id="paper-mira-visual-cot"></a>

## When Visualizing is the First Step to Reasoning: MIRA, a Benchmark for Visual Chain-of-Thought

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhou_When_Visualizing_is_the_First_Step_to_Reasoning_MIRA_a_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhou_When_Visualizing_is_the_First_Step_to_Reasoning_MIRA_a_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 仅比较文本答对率难定位视觉推理是构图失败还是读图失败。
- **核心创新 / 方法** · 对同一问题比较直接作答、文本思维链和给定中间图的视觉思维链。
- **Baseline** · 表1按开闭源及不同模型比较，表2比较通用与定制文本提示。
- **Benchmark** · MIRA 共546道含草图、结构图及路径中间态的题，评估答题结果。
- **关键结果 / 消融** · 表1用同题多输入协议定位视觉辅助的潜在收益，表2检查文本提示选择。
- **适用条件 / 局限** · 人工中间图在实际推理不可用，评估内置绘图能力时需要另外测试生成图。

**可复用机制** · 评估生成式视觉草图时，另给人工中间图作上界，以区分草图生成和后续推断。

<a id="paper-spectral-scalpel"></a>

## Spectral Scalpel: Amplifying Adjacent Action Discrepancy via Frequency-Selective Filtering for Skeleton-Based Action Segmentation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Ji_Spectral_Scalpel_Amplifying_Adjacent_Action_Discrepancy_via_Frequency-Selective_Filtering_for_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Ji_Spectral_Scalpel_Amplifying_Adjacent_Action_Discrepancy_via_Frequency-Selective_Filtering_for_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 骨架序列相邻动作的共性使边界模糊且易混类别。
- **核心创新 / 方法** · 多尺度可调频域滤波配合相邻动作差异损失，并用频感知通道混合补充长时序建模。
- **Baseline** · 表1–2比较时序动作分割方法，表3消融滤波、差异目标与通道混合。
- **Benchmark** · PKU-MMD v2 跨视角/主体、MCFS-130、TCG-15、LARa 的动作分割。
- **关键结果 / 消融** · 表1–2覆盖多数据集的边界与分类结果，表3分解互补作用。
- **适用条件 / 局限** · 训练依赖相邻动作的分段标签，真实平滑过渡或多动作并行时强拉开边界可能不合适。

**可复用机制** · 相邻动作边界不清时，专门压低相邻动作共享频谱，而非统一增强高频。

<a id="paper-duetsvg"></a>

## DuetSVG: Unified Multimodal SVG Generation with Internal Visual Guidance

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_DuetSVG_Unified_Multimodal_SVG_Generation_with_Internal_Visual_Guidance_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_DuetSVG_Unified_Multimodal_SVG_Generation_with_Internal_Visual_Guidance_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 文本方式生成 SVG 缺少图像级反馈，容易语法正确但几何失真。
- **核心创新 / 方法** · 联合生成光栅图像 token 与 SVG token，推理借原生图像预测改进 SVG。
- **Baseline** · 表1–2比较已有 SVG 及 VLM 方法，表3移除视觉输出做消融。
- **Benchmark** · SVG-Hub-5M 测试集和 VLM 对照，评估渲染保真、语义对齐和语法质量。
- **关键结果 / 消融** · 表3对照视觉输出，表1–2对比不同类型基线。
- **适用条件 / 局限** · 图像预测错误可能传给结构解码，测试时扩展增加成本。

**可复用机制** · 需要输出结构化程序时，可让同一模型生成视觉参考并在测试时指导结构解码。

<a id="paper-face-mesh-token"></a>

## FACE: A Face-based Autoregressive Representation for High-Fidelity and Efficient Mesh Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_FACE_A_Face-based_Autoregressive_Representation_for_High-Fidelity_and_Efficient_Mesh_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_FACE_A_Face-based_Autoregressive_Representation_for_High-Fidelity_and_Efficient_Mesh_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 顶点坐标展平成长序列，限制网格生成的计算效率。
- **核心创新 / 方法** · 用一三角面一 token 表示网格并配 VecSet 编码器，在潜空间做图到网格生成。
- **Baseline** · 表1比较网格表示压缩，表2比较重建，表3消融面排序。
- **Benchmark** · 多个网格数据集，比较序列压缩比及重建质量。
- **关键结果 / 消融** · 正文报告相较坐标展开缩短约九倍，压缩比0.11，表2检验重建。
- **适用条件 / 局限** · 以三角面为原子，对非流形、混合面或特殊拓扑的适用性需复验。

**可复用机制** · 结构序列按基本部件而不是每个标量分词，同时用解码结果验证压缩是否造成质量损失。

<a id="paper-faar-rank-shrinking"></a>

## FAAR: Efficient Frequency-Aware Multi-Task Fine-Tuning via Automatic Rank Selection

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Fontana_FAAR_Efficient_Frequency-Aware_Multi-Task_Fine-Tuning_via_Automatic_Rank_Selection_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Fontana_FAAR_Efficient_Frequency-Aware_Multi-Task_Fine-Tuning_via_Automatic_Rank_Selection_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 固定 LoRA 秩难反映各任务和位置的容量需要。
- **核心创新 / 方法** · 绩效驱动的秩收缩分配适配器容量，并用频谱金字塔辅助空间偏置。
- **Baseline** · 表1–2用同 Swin-Tiny 比较 LoRA 类多任务方案，表3分解模块。
- **Benchmark** · PASCAL-Context、NYUD-v2 的多任务指标和参数预算。
- **关键结果 / 消融** · 表3在 PASCAL 分别验证自适应秩与频谱模块，表1–2给跨数据集证据。
- **适用条件 / 局限** · 需要有稳定的任务性能信号，弱任务验证噪声可能导致错误削减容量。

**可复用机制** · 多任务适配先为各任务及层保留选择空间，再按绩效缩减秩。

<a id="paper-geoworld"></a>

## GeoWorld: Geometric World Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_GeoWorld_Geometric_World_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_GeoWorld_Geometric_World_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 欧氏潜变量可能压平层级关系，多步预测误差还会积累。
- **核心创新 / 方法** · Hyperbolic JEPA 映射潜表示到双曲空间，并用几何强化学习优化能量规划。
- **Baseline** · 表1–2比较 V-JEPA 2 等，表3延长 CrossTask 规划。
- **Benchmark** · CrossTask 与 COIN 的图像、视频目标条件规划，按步数测成功率。
- **关键结果 / 消融** · 正文报告相对 V-JEPA 2 三步、四步约提高3和2个百分点的成功率。
- **适用条件 / 局限** · 评估为任务视频上的视觉规划，真实闭环执行中误差积累尚需验证。

**可复用机制** · 潜世界模型用于长时计划时，可用非欧几何表示层级关系，并与欧氏表征对照。

<a id="paper-meshmosaic-boundary-conditioned-patches"></a>

## MeshMosaic: Scaling Artist Mesh Generation via Local-to-Global Assembly

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_MeshMosaic_Scaling_Artist_Mesh_Generation_via_Local-to-Global_Assembly_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_MeshMosaic_Scaling_Artist_Mesh_Generation_via_Local-to-Global_Assembly_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 全局三角序列过长，统一位置量化难保留局部细节。
- **核心创新 / 方法** · 分块生成各自网格，条件中保留相邻块共有边界。
- **Baseline** · 表1–2对照已有艺术网格生成方案。
- **Benchmark** · ShapeNet、Thingi10K 等；测几何保真和27名专业人士偏好。
- **关键结果 / 消融** · 作者报告支持十万以上三角面，相对既有约八千面配置显著扩展。
- **适用条件 / 局限** · 分块或边界失误可能传给相邻面，局部一致不能代替全局拓扑验证。

**可复用机制** · 大网格生成按局部区域量化与自回归，再用共享边界保持装配一致。

<a id="paper-genmatter-motion-grouping"></a>

## GenMatter: Perceiving Physical Objects with Generative Matter Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_GenMatter_Perceiving_Physical_Objects_with_Generative_Matter_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_GenMatter_Perceiving_Physical_Objects_with_Generative_Matter_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 纯外观跟踪在点阵和形貌不稳定时不能可靠分出物理对象。
- **核心创新 / 方法** · 把低层运动和外观聚合成局部高斯粒子，再用贝叶斯采样聚合可动体。
- **Baseline** · 与人类感知结果及已有学习跟踪器对照。
- **Benchmark** · 随机点运动、140段 Gestalt 视频及 TAP-Vid DAVIS 跟踪。
- **关键结果 / 消融** · 原文报告模拟人类感知和不确定性，并比较真实跟踪。
- **适用条件 / 局限** · 依赖可辨运动，静止或共速相邻物体可能无法分离；采样有成本。

**可复用机制** · 按可共同独立移动的层级从粒子归并出对象，使稀疏运动与自然视频共享同一推断。

<a id="paper-ifcsr-endpoint-image-control"></a>

## IFCSR: Inference-Free Fidelity-Realism Control for One-Step Diffusion-based Real-World Image Super-Resolution

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Back_IFCSR_Inference-Free_Fidelity-Realism_Control_for_One-Step_Diffusion-based_Real-World_Image_Super-Resolution_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Back_IFCSR_Inference-Free_Fidelity-Realism_Control_for_One-Step_Diffusion-based_Real-World_Image_Super-Resolution_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 每调整一次潜变量插值都要重新运行生成器。
- **核心创新 / 方法** · 以两阶段训练学习保真和自然端点，再在输出图像直接插值。
- **Baseline** · 比较现有单步扩散超分及需要反复推理的控制。
- **Benchmark** · RealSR 和 DRealSR，测超分保真、感知质量及不同控制值。
- **关键结果 / 消融** · 原文报告可预先计算端点，控制变化不再调用模型。
- **适用条件 / 局限** · 端点融合可能有重影；有很大语义差异的输出不适用简单插值。

**可复用机制** · 交互改变复原的保真—自然感平衡时，预生成两个端点，在图像空间调整以免重推理。

<a id="paper-ga4dpf-global-pose-reference"></a>

## 4D Local Modeling Toward Dynamic Global Perception for Ambiguity-free Rotation-Invariant Point Cloud Analysis

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Guo_4D_Local_Modeling_Toward_Dynamic_Global_Perception_for_Ambiguity-free_Rotation-Invariant_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Guo_4D_Local_Modeling_Toward_Dynamic_Global_Perception_for_Ambiguity-free_Rotation-Invariant_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 局部坐标在重复和对称结构上易出现多个等价参考。
- **核心创新 / 方法** · 将几何等变地提升至四维，再用 Bingham 分布估计动态全局旋转参考并融合局部特征。
- **Baseline** · 对照已有旋转不变和几何点云模型。
- **Benchmark** · ScanObjectNN 分类与 ShapeNetPart 部件分割，比较不同旋转设置的准确率或分割指标。
- **关键结果 / 消融** · 表2–3展示真实点云和部件分割表现。
- **适用条件 / 局限** · 全球参考在强对称或部分可见时可能仍不可辨，复杂度取决于表示尺寸。

**可复用机制** · 做旋转不变点云任务时，以可转向局部表示配合概率化全局姿态参考，处理对称引起的不确定。

<a id="paper-os-oracle-consistent-critics"></a>

## OS-Oracle: A Comprehensive Framework for Cross-Platform GUI Critic Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_OS-Oracle_A_Comprehensive_Framework_for_Cross-Platform_GUI_Critic_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wu_OS-Oracle_A_Comprehensive_Framework_for_Cross-Platform_GUI_Critic_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 仅凭最终成功率难定位中间错误，不可撤销动作还需要事前评估。
- **核心创新 / 方法** · 合成步骤级评审数据，监督微调后以保持一致性的组相对策略优化训练。
- **Baseline** · OS-Oracle-7B 与开源和专有视觉语言模型比较，另对比不同轨迹数据配置。
- **Benchmark** · OS-Critic Bench 的移动端、网页和桌面，测单步评审表现。
- **关键结果 / 消融** · 作者报告所测开源 VLM 评审中领先，正文比较跨平台。
- **适用条件 / 局限** · 需要代表性的中间失败与状态，评审置信不能取代不可逆操作的用户控制。

**可复用机制** · 长程 GUI 操作可在执行前检查单步，并对不同平台验证评审的一致性。

<a id="paper-mocap-2-to-3"></a>

## Mocap-2-to-3: Multi-view Lifting for Monocular Motion Recovery with 2D Pretraining

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Mocap-2-to-3_Multi-view_Lifting_for_Monocular_Motion_Recovery_with_2D_Pretraining_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_Mocap-2-to-3_Multi-view_Lifting_for_Monocular_Motion_Recovery_with_2D_Pretraining_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 单目全局位移和尺度不确定，而三维动作数据通常受拍摄场地约束。
- **核心创新 / 方法** · 二维单视图扩散预训练后做三维多视图微调，并分开局部姿态和全局运动。
- **Baseline** · 与现有单目人体运动恢复比较。
- **Benchmark** · RICH 局部对齐和世界系，以及 AIST++ 的动作误差。
- **关键结果 / 消融** · 表2–3报告局部及绝对运动的受控比较。
- **适用条件 / 局限** · 依赖地面与视角先验，复杂非平面场景及尺度歧义仍存在。

**可复用机制** · 真实三维动作标签不足时，把单目动作升维写成多视图合成，以大量二维动作预训练。

<a id="paper-stitch-a-demo-coherence-hard-negatives"></a>

## Stitch-a-Demo: Creating Video Demonstrations from Multistep Descriptions

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_Stitch-a-Demo_Creating_Video_Demonstrations_from_Multistep_Descriptions_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wu_Stitch-a-Demo_Creating_Video_Demonstrations_from_Multistep_Descriptions_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 逐步骤独立检索容易拼出动作都对、但对象或前后状态不一致的演示。
- **核心创新 / 方法** · 从弱标注过程构造候选视频组合，加入步骤错误、视觉冲突与状态不连续的难负例，学习整体检索。
- **Baseline** · 与 CoVR、VidDetours、InternVideo、Recipe2Video 及仅文本检索比较。
- **Benchmark** · 烹饪等多领域视频演示检索，包含 SaD-MC、SaD-VD、HT-Step 等，用中位排名、R@50 和人类偏好。
- **关键结果 / 消融** · 表 1 的 SaD-VD 烹饪检索中，本方法中位排名 3.5、R@50 0.91，InternVideo 为 8、0.71。
- **适用条件 / 局限** · 训练弱标注和候选库可能错误表达步骤，脱离已有视频素材的流程无法靠检索覆盖。

**可复用机制** · 组装多步骤视频时，可以训练模型拒绝单步正确但状态衔接错误的组合，再分别评估步骤与整体连贯。见图 3、表 1。

<a id="paper-indis-instance-conditioned-sampling-grid"></a>

## Few-Step Diffusion Sampling Through Instance-Aware Discretizations

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yuan_Few-Step_Diffusion_Sampling_Through_Instance-Aware_Discretizations_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yuan_Few-Step_Diffusion_Sampling_Through_Instance-Aware_Discretizations_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 统一时序网格无法适应不同输入下的流轨迹与局部复杂度。
- **核心创新 / 方法** · 学习按输入条件分配少量采样时点，通过实例条件改变离散化，保持主生成器。
- **Baseline** · 与 RDS、全局优化离散 GOD 及不同求解器或蒸馏配置对比。
- **Benchmark** · 像素和潜空间图像生成、FLUX.1-dev 及 LTX-Video，按函数评估次数比较 FID、CLIP、CMMD 等。
- **关键结果 / 消融** · 表 4 FLUX.1-dev 三次评估时 FID 44.35，GOD 为 56.82；七次时该方法 FID 22.70，RDS 为 22.58。
- **适用条件 / 局限** · 时点预测有额外开销，且已测优势主要集中在非常少步的设定。

**可复用机制** · 少步采样应对照全局最优时点和按样本分配时点，尤其在极小函数评估预算下实测。见表 4。

<a id="paper-reconstruction-kernel-frequency-shape"></a>

## Revisiting 3D Reconstruction Kernels as Low-Pass Filters

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Revisiting_3D_Reconstruction_Kernels_as_Low-Pass_Filters_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Revisiting_3D_Reconstruction_Kernels_as_Low-Pass_Filters_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 离散像素采样带来周期性频谱扩展，核的非理想截止会使高频与低频重叠。
- **核心创新 / 方法** · 把重建核当作低通滤波器，使用 Jinc 的截止特性，再做调制以改善其空间尾部衰减。
- **Baseline** · 对照 3DGS 与 SSS 的原核，同时对比等类新视角方法。
- **Benchmark** · Mip-NeRF360、Tanks & Temples 与 Deep Blending 的新视角，报告 PSNR、SSIM、LPIPS。
- **关键结果 / 消融** · 表 3 的 3DGS 在 Tanks & Temples 由 23.14 到 23.86 dB；SSS 在同集从 24.87 到 24.95 dB。
- **适用条件 / 局限** · 核的截止与采样条件有关，尾部影响开销，且已有较强重建核时边际收益有限。

**可复用机制** · 选择三维重建核时可单独比较频域截止形状和空间衰减，并在不同骨干检查是否减少混叠。见表 1、3。

<a id="paper-p2gs-factorized-camera-photometric-rendering"></a>

## P2GS: Physical Prior-guided Gaussian Splatting for Photometrically Consistent Urban Reconstruction

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Shimomura_P2GS_Physical_Prior-guided_Gaussian_Splatting_for_Photometrically_Consistent_Urban_Reconstruction_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Shimomura_P2GS_Physical_Prior-guided_Gaussian_Splatting_for_Photometrically_Consistent_Urban_Reconstruction_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 各视角的曝光和色调不同会使高斯重建把相机偏差误作物体辐射变化。
- **核心创新 / 方法** · 联合估计不随曝光变化的场景、每视角曝光与色调映射，学习符合物理成像的重渲染。
- **Baseline** · 比较 3DGS、PVG、仿射曝光修正和 Luminance-GS，消融曝光与正则损失。
- **Benchmark** · Waymo 与 CARLA 的重建与新视角，报告 PSNR、SSIM、LPIPS；模拟改变相机间曝光。
- **关键结果 / 消融** · 表 3 高曝光差下的新视角 PSNR 为 21.77 dB，原 3DGS 为 16.04 dB，仿射修正为 16.14 dB。
- **适用条件 / 局限** · 需要相机响应可辨识，场景照明变化或饱和像素可能与曝光混淆。

**可复用机制** · 多相机观测外观不一致时，可把曝光与相机响应设为成像变量，避免重建把采集偏差写入场景。见表 3。

<a id="paper-uni-ood-object-and-context-diagnostic"></a>

## UNI-OOD: Unified Object- and Image-level Out-of-Distribution Detection via Cross-Context Attentive Vision-Language Modeling

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_UNI-OOD_Unified_Object-_and_Image-level_Out-of-Distribution_Detection_via_Cross-Context_Attentive_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_UNI-OOD_Unified_Object-_and_Image-level_Out-of-Distribution_Detection_via_Cross-Context_Attentive_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 全图域外检测常假定只有一个主对象，背景容易掩盖单个目标是否属于未知类。
- **核心创新 / 方法** · 分别建模对象内部细节和跨图背景，通过图文对齐汇合证据，同时支持对象与图像两级检测。
- **Baseline** · 比较对象级 RUNA 与图像级视觉语言基线，并去掉跨图、图内注意力和文本对齐做消融。
- **Benchmark** · BDD-100k、PASCAL-VOC 等对象级设置及以 ImageNet-1K 为域内的图像级测试，使用 AUROC、FPR95。
- **关键结果 / 消融** · 表 1 对象级 16-shot 设置中平均 AUROC、FPR95 为 96.83、15.93，RUNA 为 93.32、26.58。
- **适用条件 / 局限** · 依赖对象候选和背景描述，拥挤场景漏检或背景持续漂移会影响校准。

**可复用机制** · 多对象场景不能用单个全图域外分数，可分别估计目标与背景的证据，在同一模型上按两个粒度验证。见表 1–3。

<a id="paper-airknow-external-arbitration-partial-match-triplets"></a>

## Air-Know: Arbiter-Calibrated Knowledge-Internalizing Robust Network for Composed Image Retrieval

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Fu_Air-Know_Arbiter-Calibrated_Knowledge-Internalizing_Robust_Network_for_Composed_Image_Retrieval_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Fu_Air-Know_Arbiter-Calibrated_Knowledge-Internalizing_Robust_Network_for_Composed_Image_Retrieval_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 由参考图、改写文本和目标图组成的三元组即使只部分正确，也可能让当前学员给出较低损失。
- **核心创新 / 方法** · 用独立多模态模型审查匹配程度，再让可信匹配和疑似错配采用不同的训练目标。
- **Baseline** · 对照去掉外部仲裁、多步核实及以普通 InfoNCE 替换双流。
- **Benchmark** · FashionIQ 与 CIRR 的组合检索，用 R@10、R@50 与 CIRR 总体和子集召回。
- **关键结果 / 消融** · 表 3 FashionIQ R@10 为 55.18，去外部仲裁为 53.99，去双流为 49.53。
- **适用条件 / 局限** · 外部判断质量取决于专家的视觉对齐，还可能继承其偏好；检索代理变化时需新核验。

**可复用机制** · 图文三元组部分匹配常使低损失分不出错标，可用离线独立验证与双流训练处理不确定数据。见表 3。

<a id="paper-meshsplatting-connected-opaque-geometry-optimization"></a>

## MeshSplatting: Differentiable Rendering with Opaque Meshes

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Held_MeshSplatting_Differentiable_Rendering_with_Opaque_Meshes_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Held_MeshSplatting_Differentiable_Rendering_with_Opaque_Meshes_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 点基元渲染速度很高，但通常不能直接作为常规引擎的连通网格使用。
- **核心创新 / 方法** · 利用受限 Delaunay 三角化保持连接，用可微渲染共同优化表面几何与外观。
- **Baseline** · 与 GOF、RaDe-GS、MiLo 对照，并消融连通与正则模型。
- **Benchmark** · Mip-NeRF360、Tanks & Temples 的新视角，测 PSNR、LPIPS、训练时间、内存及引擎渲染速度。
- **关键结果 / 消融** · 表 2 的 Mip-NeRF360 上 MeshSplatting 训练 48 分钟、100 MB，MiLo 为 106 分钟、253 MB；全高清分别为 190 和 160 FPS。
- **适用条件 / 局限** · 不透明网格对透明与体积效应表示有限，速度依赖具体引擎和设备。

**可复用机制** · 若输出要进网格引擎，可在可微渲染中直接优化互相连接的不透明网格，比较导出、显存和视角结果。见表 1–4。

<a id="paper-reasonmap"></a>

## ReasonMap: Towards Fine-Grained Visual Reasoning from Transit Maps

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Feng_ReasonMap_Towards_Fine-Grained_Visual_Reasoning_from_Transit_Maps_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Feng_ReasonMap_Towards_Fine-Grained_Visual_Reasoning_from_Transit_Maps_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 总体正确率难区分模型用图求解或凭语言先验猜测。
- **核心创新 / 方法** · 构造高分辨率交通图问题，以分级评分和去图对照诊断看图与推理。
- **Baseline** · 表2比较16个 MLLM，表3移除视觉，表4另列 RL 训练模型。
- **Benchmark** · 30城、1008问，按长短及题型测分。
- **关键结果 / 消融** · 原文发现开放模型中基础版和推理版的相对关系与闭源组不同。
- **适用条件 / 局限** · 对照结论依赖交通图与当前模型版本，不能据此泛化所有视觉推理任务。

**可复用机制** · 细粒度图图推理应测有图与无图，并比较相同系列基础版和推理版。

<a id="paper-lam3c-video-pointcloud"></a>

## 3D sans 3D Scans: Scalable Pre-training from Video-Generated Point Clouds

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yamada_3D_sans_3D_Scans_Scalable_Pre-training_from_Video-Generated_Point_Clouds_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yamada_3D_sans_3D_Scans_Scalable_Pre-training_from_Video-Generated_Point_Clouds_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 网络视频便宜，估计点云却有局部噪声及尺度差异。
- **核心创新 / 方法** · 视频生成点云，结合拉普拉斯感知多级聚类和噪声正则维持几何与表示稳定。
- **Baseline** · 表1–2比较现有自监督方法，表3在 PTv3 上消融。
- **Benchmark** · 室内语义、实例分割，比较全量微调和线性评估。
- **关键结果 / 消融** · 表3报告尺度对齐及正则的作用，表1–2测两类下游。
- **适用条件 / 局限** · 视频重建偏向可见充分的区域，室外快速运动或遮挡域需复验。

**可复用机制** · 缺扫描数据时，视频重建可作3D预训练输入，但应对几何噪声验证正则。

<a id="paper-cupid-object-pose"></a>

## CUPID: Generative 3D Reconstruction via Joint Object and Pose Modeling

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_CUPID_Generative_3D_Reconstruction_via_Joint_Object_and_Pose_Modeling_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_CUPID_Generative_3D_Reconstruction_via_Joint_Object_and_Pose_Modeling_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 生成先验可能产生合理外观却偏离输入视角。
- **核心创新 / 方法** · 第一阶段生成粗3D和2D–3D对应，第二阶段以估计位姿注入像素对齐特征。
- **Baseline** · 表1–3比较重建、生成与点图基线，表4消融位姿条件。
- **Benchmark** · 单视图几何、输入视角一致性与整体3D质量，含 Chamfer、PSNR。
- **关键结果 / 消融** · 摘要报告相对既有方法超过3 dB PSNR 提升及10% Chamfer 改善。
- **适用条件 / 局限** · 粗对应错误会传给精化，严重遮挡或难区分对称姿态需另外检验。

**可复用机制** · 由粗几何对应先估计相机位姿，再对齐像素条件细化对象。

<a id="paper-gslr-low-rank-tensor"></a>

## Gaussian Splatting-based Low-Rank Tensor Representation for Multi-Dimensional Image Recovery

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zeng_Gaussian_Splatting-based_Low-Rank_Tensor_Representation_for_Multi-Dimensional_Image_Recovery_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zeng_Gaussian_Splatting-based_Low-Rank_Tensor_Representation_for_Multi-Dimensional_Image_Recovery_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 低秩潜张量与固定 DFT/DCT 基底都可能损失局部细节。
- **核心创新 / 方法** · 用2D与1D Gaussian 分别参数化潜张量和变换矩阵。
- **Baseline** · 表1–3比较图像恢复及张量基线，表4对照不同近似。
- **Benchmark** · 多维图像随机缺失、管状缺失和切片缺失。
- **关键结果 / 消融** · 表1–3跨缺失模式检验，表4对比表示近似。
- **适用条件 / 局限** · 高斯局部基能否覆盖快速变化取决于尺度与密度，复杂非局部缺失需重测。

**可复用机制** · 低秩张量补全时同时检验潜张量和变换基底能否表征局部高频。

<a id="paper-must-missing-modality"></a>

## MUST: Modality-Specific Representation-Aware Transformer for Diffusion-Enhanced Survival Prediction with Missing Modality

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Kim_MUST_Modality-Specific_Representation-Aware_Transformer_for_Diffusion-Enhanced_Survival_Prediction_with_Missing_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Kim_MUST_Modality-Specific_Representation-Aware_Transformer_for_Diffusion-Enhanced_Survival_Prediction_with_Missing_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 直接特征对齐可能混淆跨模态共识与某模态独有证据。
- **核心创新 / 方法** · 用低秩子空间约束拆分私有和共享上下文，再用条件生成建模缺失部分。
- **Baseline** · 表1–2比较可见和缺失情形，表3消融渐进训练与条件生成。
- **Benchmark** · 五个 TCGA 数据集，病理和基因输入的生存排序 C-index。
- **关键结果 / 消融** · 表1–2按模态可用性分别报告，表3验证训练组件。
- **适用条件 / 局限** · 生成私有部分有不可约不确定性，不能把估计当成有效观测，迁移需校准。

**可复用机制** · 填补缺失模态之前先分解可从其他模态推断的共有信息与不可观测的私有部分。

<a id="paper-fm-steer"></a>

## FM-Steer: Enhance Generalist Policies with Value-Guided Cascaded Denoising

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Song_FM-Steer_Enhance_Generalist_Policies_with_Value-Guided_Cascaded_Denoising_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Song_FM-Steer_Enhance_Generalist_Policies_with_Value-Guided_Cascaded_Denoising_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 多候选全部完整去噪会增加推理开销，单样本又缺少纠错。
- **核心创新 / 方法** · 训练中间流动作价值验证器，级联去噪时筛掉较低价值候选。
- **Baseline** · 表2比较 V-GPS 与 RoboMonkey，表3消融级联及策略配置。
- **Benchmark** · LIBERO 四套任务、SimplerEnv，比较成功率及运算分配。
- **关键结果 / 消融** · 表1报告成功率和标准误，表3比较采样和验证器作用。
- **适用条件 / 局限** · 验证器须能可靠评价未充分去噪的轨迹，策略和硬件变化时需重校。

**可复用机制** · 实时控制可以在早期含噪动作上做价值筛选，再精化保留候选。

<a id="paper-laser-layer-wise-scale-alignment"></a>

## LASER: Layer-wise Scale Alignment for Training-Free Streaming 4D Reconstruction

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Ding_LASER_Layer-wise_Scale_Alignment_for_Training-Free_Streaming_4D_Reconstruction_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Ding_LASER_Layer-wise_Scale_Alignment_for_Training-Free_Streaming_4D_Reconstruction_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 相邻窗口近远景之间的相对尺度会不一致。
- **核心创新 / 方法** · 分层估计尺度并跨窗传播，复用原模型权重。
- **Baseline** · VGGT、π3 及全局 Sim(3) 等窗对齐或重建方案。
- **Benchmark** · Sintel、ScanNet、TUM、KITTI 等，评估深度、ATE、平移及旋转 RPE。
- **关键结果 / 消融** · 作者报告 RTX A6000 上14 FPS、峰值6 GB，表1–3比较几何精度。
- **适用条件 / 局限** · 深度分层需要共视和可靠对应，纯转动或快速动态场景可能出错。

**可复用机制** · 离线重建改成滑窗流式时，按深度层对齐尺度，避免整窗只拟合一个相似变换。

<a id="paper-fase3d-fourier-tokenizer"></a>

## Efficient Encoder-Free Fourier-based 3D Large Multimodal Model

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Mei_Efficient_Encoder-Free_Fourier-based_3D_Large_Multimodal_Model_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Mei_Efficient_Encoder-Free_Fourier-based_3D_Large_Multimodal_Model_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 点云无序且点数多，外部编码器推理昂贵。
- **核心创新 / 方法** · 超点结构压缩后经空间填充曲线序列化和 FFT 混合，图式合并词元并用频域 LoRA 补上下文。
- **Baseline** · 编码器式三维多模态模型，及表3不同视觉嵌入模块。
- **Benchmark** · ScanQA、SQA3D 问答和 ScanRefer、Nr3D 密集描述，统计参数与 FLOPs。
- **关键结果 / 消融** · 表1–3报告近似的任务表现与较低编码计算。
- **适用条件 / 局限** · 序列化和频域近似不保证保留所有三维邻接关系，细对象或密度变化需另测。

**可复用机制** · 场景点云太长时，使用空间序列化及频域混合设计轻量 tokenizer，并测不依赖重型视觉编码器的代价。

<a id="paper-sparvar-cross-scale-sparsity"></a>

## SparVAR: Exploring Sparsity in Visual AutoRegressive Modeling for Training-Free Acceleration

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_SparVAR_Exploring_Sparsity_in_Visual_AutoRegressive_Modeling_for_Training-Free_Acceleration_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_SparVAR_Exploring_Sparsity_in_Visual_AutoRegressive_Modeling_for_Training-Free_Acceleration_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 高分辨率注意力昂贵，跳过大尺度会丢细节。
- **核心创新 / 方法** · 利用锚点、跨尺度激活相似性与局部性，在决策尺度生成稀疏索引并映射给高分辨率。
- **Baseline** · 常规全注意力生成和已有加速方法。
- **Benchmark** · 1024×1024 GenEval，另以 HPSv2.1 等测偏好和质量，记录推理开销。
- **关键结果 / 消融** · 表2–3报告所测加速与质量的权衡。
- **适用条件 / 局限** · 跨尺度显著性可能变化，稀有高频细节和不同尺度日程需重新评估。

**可复用机制** · 多尺度自回归生图应从中间尺度推断后续稀疏注意力，保留高分辨率生成步骤。

<a id="paper-harope-head-wise-position"></a>

## Head-wise Adaptive Rotary Positional Encoding for Fine-Grained Image Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Head-wise_Adaptive_Rotary_Positional_Encoding_for_Fine-Grained_Image_Generation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Head-wise_Adaptive_Rotary_Positional_Encoding_for_Fine-Grained_Image_Generation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 分轴且各头共享的 RoPE 难表达细粒度布局。
- **核心创新 / 方法** · 旋转前加入以 SVD 参数化的可学线性变换，让各头感受野与旋转平面可适配。
- **Baseline** · 标准多维 RoPE、其他位置编码变体及绝对位置嵌入。
- **Benchmark** · ImageNet 类条件生成，Flux、SD3 文生图及图像理解对照。
- **关键结果 / 消融** · 原文显示不同生成骨干的视觉表现改善，并分析细粒度布局。
- **适用条件 / 局限** · 需学习位置参数，分辨率外推及不同坐标系仍要验证。

**可复用机制** · 生成任务的位置编码可按注意力头拟合坐标投影，在保持相对性时允许空间轴耦合。

<a id="paper-so-bench-structured-output-diagnostics"></a>

## SO-Bench: A Structural Output Evaluation of Multimodal LLM

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Feng_SO-Bench_A_Structural_Output_Evaluation_of_Multimodal_LLM_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Feng_SO-Bench_A_Structural_Output_Evaluation_of_Multimodal_LLM_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 有效 JSON 可能没有依据，正确值也可能落在错误字段。
- **核心创新 / 方法** · 构造跨视觉域的图像—结构模式题，比较通用、结构化接口和调整训练后的输出。
- **Baseline** · 开源及专有多模态模型，比较结构化输出 API 和指令遵循。
- **Benchmark** · UI、自然图、文档、图表；超过6500种 JSON schema，约1800个人工核对图像—模式对。
- **关键结果 / 消融** · 原文报告语义正确与模式遵守仍有明显缺口，且有训练对照。
- **适用条件 / 局限** · 字段答案和模式需有可靠人工核对，合法输出率不能代表下游工作流完成率。

**可复用机制** · 评估视觉智能体的结构化输出时，将模式合规与字段事实正确分别验收。

<a id="paper-eulerian-gaussian-splatting"></a>

## Eulerian Gaussian Splatting using Hashed Probability Pyramids

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Polansky_Eulerian_Gaussian_Splatting_using_Hashed_Probability_Pyramids_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Polansky_Eulerian_Gaussian_Splatting_using_Hashed_Probability_Pyramids_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 手工切分、删除和移动图元难由最终误差统一驱动。
- **核心创新 / 方法** · 以哈希多尺度网格学习位置概率，并用控制变量降低密度梯度方差。
- **Baseline** · Taming-3DGS、3DGS-MCMC 与去掉组件配置。
- **Benchmark** · mip-NeRF 360、Tanks & Temples 等，比较重建和渲染速率。
- **关键结果 / 消融** · 表1–2报告重建质量及密度相关消融，保持接近3DGS渲染效率。
- **适用条件 / 局限** · 取样和密度优化会增加训练开销，细薄表面的覆盖依赖概率网格。

**可复用机制** · 优化离散渲染图元分布时，把图元位置视作可训练连续密度的样本。

<a id="paper-rebrl-discrete-token-timestep-credit"></a>

## RebRL: Reinforcing Discrete Visual Diffusion Models with Rebalanced Timestep Credits

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_RebRL_Reinforcing_Discrete_Visual_Diffusion_Models_with_Rebalanced_Timestep_Credits_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_RebRL_Reinforcing_Discrete_Visual_Diffusion_Models_with_Rebalanced_Timestep_Credits_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 对各时点采用同一权重时，决定全局布局的早期标记可能对训练贡献偏小。
- **核心创新 / 方法** · 依据掩膜阶段重配训练信用，使不同时间的生成标记获得更均衡的梯度贡献。
- **Baseline** · 在 MMaDA 上比较 diffu-GRPO、UniGRPO、MaskGRPO，另列连续与离散模型基线。
- **Benchmark** · GenEval 的对象、计数、颜色、位置、属性绑定，以及人类偏好代理指标。
- **关键结果 / 消融** · 表 1 的整体 GenEval 为 0.86，MaskGRPO 为 0.84；计数为 0.81 对 0.69，颜色为 0.88 对 0.90。
- **适用条件 / 局限** · 机制基于离散掩膜生成顺序，对连续模型或不同阶段信息密度需重验。

**可复用机制** · 给离散扩散做强化学习时，可按掩膜阶段重配信用并核对早期决策是否在训练中被低估。见图 5、表 1。

<a id="paper-copo-token-sufficiency-necessity-grounding"></a>

## COPO: Causal-Oriented Policy Optimization for Hallucinations of MLLMs

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Guo_COPO_Causal-Oriented_Policy_Optimization_for_Hallucinations_of_MLLMs_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Guo_COPO_Causal-Oriented_Policy_Optimization_for_Hallucinations_of_MLLMs_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 结果奖励与背景相关性可能共变，使视觉语言模型生成无证据描述。
- **核心创新 / 方法** · 在推理所用标记中评量证据的充分与必要条件，构成完整性奖励以促进视觉约束输出。
- **Baseline** · 比较移除任一约束或同时移除的版本，以及 OPERA、DeCo、VCD 等。
- **Benchmark** · CHAIR、POPE F1、MME 与 GPT-4 辅助评价。
- **关键结果 / 消融** · 表 3 同时移除两约束时 CHAIR-S 为 30.5，完整为 19.8，POPE 由 85.9 到 88.0。
- **适用条件 / 局限** · 充分与必要是基于模型内的受控比较，结果依赖证据划分准确性，不能直接证明真实场景因果关系。

**可复用机制** · 若只奖励答对导致模型利用背景捷径，可分别检验相关证据的充分性和必要性，并将结果加入训练奖励。见表 3。

<a id="paper-autotraces-hybrid-continuous-waypoint-tokens"></a>

## AutoTraces: Autoregressive Trajectory Forecasting via Multimodal Large Language Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_AutoTraces_Autoregressive_Trajectory_Forecasting_via_Multimodal_Large_Language_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_AutoTraces_Autoregressive_Trajectory_Forecasting_via_Multimodal_Large_Language_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 把连续轨迹串行化成文本可能损失数值关系，固定长度解码又不便长期预测。
- **核心创新 / 方法** · 以专用点标记保持序列位置与类别，用轻量编解码器把坐标表示为连续嵌入。
- **Baseline** · 与 LLaVA-Video 文本序列、CityWalker、ViNT 等比较，另消融思维轨迹与输出形式。
- **Benchmark** · SCAND、未见 GoStanford 与 RECON 的导航轨迹预测，按不同秒级预测长度报告 L1、L2。
- **关键结果 / 消融** · 表 2 的 GoStanford 10 步 L2，AutoTraces 为 1.772 米，LLaVA-Video 为 2.141 米；RECON 为 2.837 对 4.211。
- **适用条件 / 局限** · 依赖轨迹坐标和成像一致性，预测误差无法代替闭环碰撞与任务完成评估。

**可复用机制** · 接入轨迹回归时可对照文字序列与专用标记加连续坐标嵌入，保留自回归生成以支持可变长度。见表 2 和图 4。

<a id="paper-arc-modality-routed-rule-reasoning"></a>

## Think Visually, Reason Textually: Vision-Language Synergy in Abstract Reasoning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Think_Visually_Reason_Textually_Vision-Language_Synergy_in_Abstract_Reasoning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Think_Visually_Reason_Textually_Vision-Language_Synergy_in_Abstract_Reasoning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 纯文本不便发现二维全局模式，纯图像又可能难做逐格精确变换。
- **核心创新 / 方法** · 视觉阶段归纳空间规则，文本阶段落实符号操作，另用跨模态切换重新查验答案。
- **Baseline** · 同一骨干对照纯文本、单加两阶段协作、单加切换校正及组合。
- **Benchmark** · ARC-AGI、BARC-100 和 Re-ARC 的抽象网格推理，报告任务准确率。
- **关键结果 / 消融** · 表 2 Gemini 2.5 Pro 在 ARC-AGI 从 35.0 到组合的 42.25；o4-mini 从 42.25 到 46.75。
- **适用条件 / 局限** · 依赖任务可以无损表达为文本并有可复核的视觉形式，模态转换也可能带来新错误和推理开销。

**可复用机制** · 可在同一空间推理任务中用视觉归纳规则、文本精确执行，并切换模态复核错误。见表 2。

<a id="paper-lyapunov-probes-perturbation-stability-for-hallucination"></a>

## Lyapunov Probes for Hallucination Detection in Large Foundation Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Luan_Lyapunov_Probes_for_Hallucination_Detection_in_Large_Foundation_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Luan_Lyapunov_Probes_for_Hallucination_Detection_in_Large_Foundation_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 仅依据一次隐状态分类，难以捕捉事实边界处回答对小变化的敏感性。
- **核心创新 / 方法** · 训练轻量多层探针，以导数约束和局部扰动响应刻画答案状态的稳定程度。
- **Baseline** · 比较移除扰动数据、两阶段、多层特征和稳定约束，并与已有幻觉检测器对照。
- **Benchmark** · 不同语言及多模态模型的幻觉检测和跨域迁移，以 AUPRC 评估。
- **关键结果 / 消融** · 表 4 Llama-3-8B 完整为 86.46，去稳定约束为 82.86；Qwen-3-4B 完整为 79.47，移除扰动数据反达 79.92。
- **适用条件 / 局限** · 探针需要访问隐状态，稳定性只反映受控输入的响应规律，正确而敏感及稳定而错误的输出都可能出现。

**可复用机制** · 幻觉探针可同时检查隐状态的局部稳定性和静态可分性，比较显式稳定约束及跨域迁移。见表 3、4。

<a id="paper-vi-probe-perception-versus-template-recall"></a>

## Do VLMs Perceive or Recall? Probing Visual Perception vs. Memory with Classic Visual Illusions

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Sun_Do_VLMs_Perceive_or_Recall_Probing_Visual_Perception_vs._Memory_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Sun_Do_VLMs_Perceive_or_Recall_Probing_Visual_Perception_vs._Memory_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 熟悉错觉原图时答对可能来自记住模板，原图平均准确率会掩盖视觉改变后的失效。
- **核心创新 / 方法** · 生成不同程度的线索翻转和移除诱因的匹配控制，用成对一致性与模板固定度检查。
- **Baseline** · 同模型对照原错觉、翻转错觉和相应控制，并比较多种视觉语言模型。
- **Benchmark** · VI-Probe 的多类经典视觉错觉，使用成对翻转一致性、模板固定指数和控制归一化指标。
- **关键结果 / 消融** · 表 2 的归一化倍数 GPT-5 为 1.97、GPT-5-Nano 为 0.12；同族模型平均表现不能揭示其对翻转的响应。
- **适用条件 / 局限** · 错觉家族、熟悉度及合成可辨识度影响结论，需对具体视觉任务重建匹配控制。

**可复用机制** · 判断模型依赖视觉还是图式记忆时，可翻转视觉线索并保留无诱因匹配控制，分别报告翻转一致性与固定答法。见表 2。

<a id="paper-cross-modal-stereo-dual-domain-projection"></a>

## Bidirectional Cross-Modal Prompting for Event-Frame Asymmetric Stereo

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_Bidirectional_Cross-Modal_Prompting_for_Event-Frame_Asymmetric_Stereo_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_Bidirectional_Cross-Modal_Prompting_for_Event-Frame_Asymmetric_Stereo_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 帧与事件的语义和时间结构不同，预先压到同一种特征可能遮掉一侧有效线索。
- **核心创新 / 方法** · 通过双向提示把帧与事件分别投影到两个传感域获取互补对应，再逐级细化视差。
- **Baseline** · 与事件、图像和混合模态立体匹配方法比较，并消融 CDEA、SCC 与等迭代预算的单尺度优化。
- **Benchmark** · DSEC、MVSEC、M3ED，采用 MAE、1 像素和 2 像素误差率及 RMSE。
- **关键结果 / 消融** · 表 5 的 DSEC 完整 MAE 为 0.565，移除双组件为 0.594，移除级联为 0.588。
- **适用条件 / 局限** · 依赖两路传感器时空对齐，遮挡、时钟偏差与缺少事件活动时仍应另测。

**可复用机制** · 异构相机匹配可同时在两个传感域映射对方的信息，比较只做单域对齐时的视差误差。见表 5。

<a id="paper-maskdexgrasp"></a>

## MaskDexGrasp: Generative Masked Modeling for Part-Aware Dexterous Grasp Synthesis

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zuo_MaskDexGrasp_Generative_Masked_Modeling_for_Part-Aware_Dexterous_Grasp_Synthesis_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zuo_MaskDexGrasp_Generative_Masked_Modeling_for_Part-Aware_Dexterous_Grasp_Synthesis_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 整手单个隐向量难以在维持抓取整体一致时单独调整手指。
- **核心创新 / 方法** · 手掌和五指分别使用离散码本，双向掩码 Transformer 按物体几何和任务描述生成。
- **Baseline** · 表1与既有抓取生成器比较，表3更改码本和掩码模型。
- **Benchmark** · 两个语义抓取子集，测成功率、穿透和抓取质量；图5展示局部编辑。
- **关键结果 / 消融** · 表1两子集成功率44.68%及75.16%，表3验证分部件表征和生成机制。
- **适用条件 / 局限** · 码本依赖手的拓扑，改变关节和接触约束需重新训练及硬件验证。

**可复用机制** · 抓取动作可按手掌与各指分词，使用掩码建模支持补全和局部改动。

<a id="paper-infinity-rope"></a>

## Infinity-RoPE: Action-Controllable Infinite Video Generation Emerges From Autoregressive Self-Rollout

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yesiltepe_Infinity-RoPE_Action-Controllable_Infinite_Video_Generation_Emerges_From_Autoregressive_Self-Rollout_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yesiltepe_Infinity-RoPE_Action-Controllable_Infinite_Video_Generation_Emerges_From_Autoregressive_Self-Rollout_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 固定时间坐标限制外推，保留全部历史导致新提示响应滞后。
- **核心创新 / 方法** · 按 latent 块旋转位置坐标以维持相对关系，用缓存刷新及位置切换控制语义和剪接。
- **Baseline** · 图2与 Self-Forcing 比较，图4对照全缓存和无缓存，表1–2比较视频生成系统。
- **Benchmark** · 5、60、120及240秒视频评估动态程度及一致性，表3有人评。
- **关键结果 / 消融** · 表2在120及240秒跨多质量指标列出表现，图4对比切换行为。
- **适用条件 / 局限** · 长达240秒的实验支持有限外推，远程事件依赖和人物状态持久度仍需另测。

**可复用机制** · 长序列滚动生成可将位置编码动态重基准化，并只在切换任务时有限重置缓存。

<a id="paper-purecc"></a>

## PureCC: Pure Learning for Text-to-Image Concept Customization

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Liao_PureCC_Pure_Learning_for_Text-to-Image_Concept_Customization_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Liao_PureCC_Pure_Learning_for_Text-to-Image_Concept_Customization_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 概念特化可改变原有生成行为，定制分数未反映这一代价。
- **核心创新 / 方法** · 冻结负责新概念的提取分支，训练时与原条件预测分离，并自适应调节引导强度。
- **Baseline** · 表1比较 DreamBooth、Mix-of-Show、DreamO、UNO 等，表2–3消融分阶段与引导强度。
- **Benchmark** · DreamBenchCC 比较原能力漂移和概念响应，图2分析原分布 KL。
- **关键结果 / 消融** · 图2两概念展示对原分布漂移小于 LoRA 和 DreamBooth，表2–3单测设计。
- **适用条件 / 局限** · 旧能力依赖测试提示覆盖度，新旧概念重合较大时需另测干扰。

**可复用机制** · 注入个性概念时，将新概念增量和原条件预测分离，并将旧能力漂移纳入评价。

<a id="paper-u2flow"></a>

## U^2Flow: Uncertainty-Aware Unsupervised Optical Flow Estimation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Sun_U2Flow_Uncertainty-Aware_Unsupervised_Optical_Flow_Estimation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Sun_U2Flow_Uncertainty-Aware_Unsupervised_Optical_Flow_Estimation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 仅凭重建误差难区分可靠光流与遮挡等不可匹配区域。
- **核心创新 / 方法** · 用解耦的 Laplace 最大似然从增强一致性构建不确定性监督，并指导平滑、细化和双向融合。
- **Baseline** · RAFT 式递归骨干，表1–2比较 SMURF 等，表3–5消融分支、细化和融合。
- **Benchmark** · Sintel、KITTI 2012/2015；光流误差及 AUSE，分遮挡与非遮挡。
- **关键结果 / 消融** · 表5对照有无融合，正文另报跨域迁移；图4对比不确定性排序与真实误差。
- **适用条件 / 局限** · 增强须保留真实时序对应，遮挡或新域下应重新校准置信度。

**可复用机制** · 无标签位移估计可先由增强一致性学习逐像素不确定性，再用于细化和融合。

<a id="paper-jit-denoise-clean-data"></a>

## Back to Basics: Let Denoising Generative Models Denoise

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Back_to_Basics_Let_Denoising_Generative_Models_Denoise_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Back_to_Basics_Let_Denoising_Generative_Models_Denoise_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 高维像素噪声可能无法由小模型有效表达，即使干净图像有低维结构。
- **核心创新 / 方法** · 直接预测干净像素，用大块 ViT 做扩散；需要时变换输出后计算速度或噪声空间损失。
- **Baseline** · 表1–2组合 x、v、epsilon 输出与损失空间，图2验证低维数据嵌入高维的现象。
- **Benchmark** · ImageNet 256和512分辨率，FID-50K；表5延展到1024，表6测规模。
- **关键结果 / 消融** · 表2给同架构不同预测目标的对照；表6 JiT-B/16 在256分辨率报告 FID 3.66。
- **适用条件 / 局限** · 收益与输入高维、干净数据的低维结构及模型容量相关，低维潜空间不必有同样差距。

**可复用机制** · 选择扩散网络输出时要单独比较干净数据预测与噪声预测，损失的计算空间可另选。

<a id="paper-pvp-privileged-proprioception"></a>

## PvP: Data-Efficient Humanoid Robot Learning with Proprioceptive-Privileged Contrastive Representations

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yuan_PvP_Data-Efficient_Humanoid_Robot_Learning_with_Proprioceptive-Privileged_Contrastive_Representations_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yuan_PvP_Data-Efficient_Humanoid_Robot_Learning_with_Proprioceptive-Privileged_Contrastive_Representations_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 人形机器人受部分可观测和高维控制限制，直接强化学习样本昂贵。
- **核心创新 / 方法** · 从同一动力学状态得到本体与特权视图，对比学习紧凑表示，再用于策略训练。
- **Baseline** · 图5比较原 PPO 和四种状态表示方法，图6比较动作平滑。
- **Benchmark** · LimX Oli 的速度跟踪和动作模仿任务，报告学习曲线及平滑度。
- **关键结果 / 消融** · 图5分别比较两任务的学习进展，图6报告动作平滑优化。
- **适用条件 / 局限** · 特权状态需由训练环境可靠提供，模拟器偏差和实机泛化须校准。

**可复用机制** · 训练时将本体观测与特权状态配对做对比学习，减少手写增强并保持部署输入简单。

<a id="paper-structure-aware-event-distillation"></a>

## Scaling Dense Event-Stream Pretraining from Visual Foundation Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Scaling_Dense_Event-Stream_Pretraining_from_Visual_Foundation_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_Scaling_Dense_Event-Stream_Pretraining_from_Visual_Foundation_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 图像与事件流稀疏程度和粒度不同，密集原始特征对齐易在高分辨率语义坍塌。
- **核心创新 / 方法** · 从同步图像和事件对提取教师语义结构，用结构感知蒸馏建立稠密对应。
- **Baseline** · 对照传统事件训练、图像教师直接蒸馏及不同标注预算。
- **Benchmark** · 事件语义分割的线性探测、少样本和全量微调；MVSEC-Depth、DSEC-Depth 深度估计。
- **关键结果 / 消融** · 表1–3报告多个标注预算下的分割表现和深度结果。
- **适用条件 / 局限** · 依赖同步数据及教师结构与事件可观测运动一致，静止结构可能缺少事件。

**可复用机制** · 将稠密视觉教师蒸馏到稀疏传感器时，对齐语义结构而非只逐位置回归。

<a id="paper-layer-wise-decision-timeline"></a>

## When Do Models Actually Decide? Mapping the Layer-Wise Decision Timeline in Pretrained Neural Networks

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Lee_When_Do_Models_Actually_Decide_Mapping_the_Layer-Wise_Decision_Timeline_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Lee_When_Do_Models_Actually_Decide_Mapping_the_Layer-Wise_Decision_Timeline_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 相同骨干的输入可能在不同层才获得决策信息，单一平均深度会遮蔽分布。
- **核心创新 / 方法** · 冻结 ResNet 做逐层线性探针，比较不同连续稳定条件得到的层深。
- **Baseline** · 对照 ResNet-18/50/101，以及不同稳定阈值。
- **Benchmark** · ImageNet 分类，测首次持续稳定深度、探针准确率和早晚样本比例。
- **关键结果 / 消融** · 较深两种 ResNet 中，33–39%在首三分之一稳定，39–42%在末30%；改变稳定标准明显移动均值。
- **适用条件 / 局限** · 线性可解码性不是原网络因果决策；迁移到其他架构需重测。

**可复用机制** · 设计早退时按多层稳定协议报告哪些样本可早退，避免单层探针首次命中等同于已决策。

<a id="paper-cowtracker-warping"></a>

## CoWTracker: Tracking by Warping instead of Correlation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Lai_CoWTracker_Tracking_by_Warping_instead_of_Correlation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Lai_CoWTracker_Tracking_by_Warping_instead_of_Correlation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 构建全局相关体随空间尺度快速增大，限制密集追踪。
- **核心创新 / 方法** · 基于当前位移将目标特征变换到查询帧，用时空 Transformer 联合优化轨迹。
- **Baseline** · 当前相关体式点跟踪方法，另对照专用光流及模型设计消融。
- **Benchmark** · TAP-Vid DAVIS、RGB-Stacking、Kinetics 和 RoboTAP，测 AJ 等；Sintel、KITTI、Spring 测零样本光流。
- **关键结果 / 消融** · 表1–3给出两类任务的竞争表现及变换设计消融。
- **适用条件 / 局限** · 粗始位移很偏或目标长期不可见时，局部变换不能可靠找回对应。

**可复用机制** · 高分辨率点跟踪用当前轨迹回变目标特征并迭代更新，避免显式相关体。

<a id="paper-tcas-temporal-attention-discriminability"></a>

## Understanding Temporal Logic Consistency in Video-Language Models through Cross-Modal Attention Discriminability

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Understanding_Temporal_Logic_Consistency_in_Video-Language_Models_through_Cross-Modal_Attention_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Understanding_Temporal_Logic_Consistency_in_Video-Language_Models_through_Cross-Modal_Attention_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 定位视频片段后换种问法仍可能答出互相矛盾的结果。
- **核心创新 / 方法** · 诊断各跨模态头对时间词元的区分性，并在干预中强化时间差异。
- **Baseline** · 有无 TCAS、不同干预强度及原视频语言模型。
- **Benchmark** · 基于视频时间定位的重述一致性，按注意力和干预后得分评价。
- **关键结果 / 消融** · 表2报告部分干预强度下的一致性改善。
- **适用条件 / 局限** · 尖锐注意力可能聚焦错误帧；一致回答不保证事实正确。

**可复用机制** · 视频答案改写后不一致时，检查跨模态注意力是否区分时间点，再实验性增强时序区分。

<a id="paper-capnav-capability-conditioned-navigation"></a>

## CapNav: Benchmarking Vision Language Models on Capability-conditioned Indoor Navigation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Su_CapNav_Benchmarking_Vision_Language_Models_on_Capability-conditioned_Indoor_Navigation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Su_CapNav_Benchmarking_Vision_Language_Models_on_Capability-conditioned_Indoor_Navigation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 同一场景对不同机体的可达性不同，通用路线评价无法揭示错误。
- **核心创新 / 方法** · 为五类主体标注移动、尺寸与交互限制，按主体生成可行性和障碍问答。
- **Baseline** · 对照13个视觉语言模型与多种帧输入设置。
- **Benchmark** · 45个实景、473个导航任务、2365条问答，分主体和空间障碍评估。
- **关键结果 / 消融** · 约束加严时模型表现下降，空间尺寸相关障碍仍难。
- **适用条件 / 局限** · 问答和图上可达不能替代闭环控制，主体规格不全也会扭曲结论。

**可复用机制** · 衡量跨机体导航时按具体尺寸和越障能力划分可行路径，避免用统一可达标签。

<a id="paper-cultural-representation-activation"></a>

## Where Culture Fades: Revealing the Cultural Gap in Text-to-Image Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Shi_Where_Culture_Fades_Revealing_the_Cultural_Gap_in_Text-to-Image_Generation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Shi_Where_Culture_Fades_Revealing_the_Cultural_Gap_in_Text-to-Image_Generation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 逼真图像仍可偏向文化中性或英语语境，直接加数据无法区分缺少知识和未调用知识。
- **核心创新 / 方法** · 通过文化提示探测定位一小部分相关表征，比较推理激活及定层适配。
- **Baseline** · 两种代表性扩散模型和原文文化对齐基线。
- **Benchmark** · CultureBench 含跨语言及只含名词的控制提示，测文化一致、保真和多样性。
- **关键结果 / 消融** · 原文报告文化一致性改善并检查是否牺牲保真及多样性。
- **适用条件 / 局限** · 文化概念区分及评测依赖标注语境，少量模型结果不能证明普遍存在文化专属单元。

**可复用机制** · 跨语言生图出现文化泛化时，先探测表征是否可激活，再决定做定层调整还是更新整网。

<a id="paper-hypodepth-discrete-hypothesis-residual-search"></a>

## Depth Hypothesis Guided Iterative Refinement for Event-Image Monocular Depth Estimation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_Depth_Hypothesis_Guided_Iterative_Refinement_for_Event-Image_Monocular_Depth_Estimation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_Depth_Hypothesis_Guided_Iterative_Refinement_for_Event-Image_Monocular_Depth_Estimation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 事件与图像的融合能够补足输入，却不能解决直接回归整个深度场的歧义。
- **核心创新 / 方法** · 构建离散深度假设体，以相关代价从粗到细检索并细化残差。
- **Baseline** · 与迭代连续深度、去除 GRU 或多尺度查找等变体和其他单目方法比较。
- **Benchmark** · DSEC、MVSEC 的事件和图像单目深度，使用 δ1、绝对相对误差、RMSE 及算力。
- **关键结果 / 消融** · 表 4 轻量模型完整 δ1 为 0.885、AbsRel 为 0.105，去掉离散假设体分别为 0.873、0.113。
- **适用条件 / 局限** · 候选深度的取值范围与尺度分配影响精度，稀疏与非同步事件场景需重测。

**可复用机制** · 单目传感深度可先保留离散候选，再做逐尺度残差搜索，用同骨干的连续深度反馈验证收敛与误差。见表 4。

<a id="paper-tmd-backbone-reuse-inner-transition-head"></a>

## Transition Matching Distillation for Fast Video Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Nie_Transition_Matching_Distillation_for_Fast_Video_Generation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Nie_Transition_Matching_Distillation_for_Fast_Video_Generation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 从多步视频教师直接压到很少的整网去噪步，可能丢失过渡动态。
- **核心创新 / 方法** · 用外层主干提取语义，复用语义状态驱动轻量流头做若干内层过渡，匹配教师轨迹。
- **Baseline** · 与 Wan2.1 教师、rCM、DMD2-v 等蒸馏比较，区分名义步数与整网等效评估次数。
- **Benchmark** · VBench 的视频整体、质量与语义得分，另测人类偏好和推理开销。
- **关键结果 / 消融** · 表 1 在 Wan2.1 1.3B 上，TMD 的等效 NFE 为 2.33 时整体 84.68，DMD2-v 在 2 次为 84.39、4 次为 84.60。
- **适用条件 / 局限** · 块数等效成本不能直接换成时延；分阶段共享依赖外层状态在内层间仍有效。

**可复用机制** · 少步视频蒸馏可在外层更新语义、内层只用轻量头细化，并按实际执行的主干块数计算成本。见表 1。

<a id="paper-mocapanything-reference-conditioned-skeleton-ik"></a>

## MoCapAnything: Unified 3D Motion Capture for Arbitrary Skeletons from Monocular Videos

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Gong_MoCapAnything_Unified_3D_Motion_Capture_for_Arbitrary_Skeletons_from_Monocular_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Gong_MoCapAnything_Unified_3D_Motion_Capture_for_Arbitrary_Skeletons_from_Monocular_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 固定关节输出层难处理未知拓扑，重新定义关节标签也难直接输出可用旋转。
- **核心创新 / 方法** · 根据给定资产的骨架、网格与渲染图建立关节查询，推断关节轨迹后再用受约束逆运动学求资产旋转。
- **Baseline** · 与适配输出层的 HRNet、ViTPose、VIBE、GLoT 比较，消融资产图像和网格。
- **Benchmark** · Truebones Zoo 的已见、少见、未见类别，报告 MPJPE 和 MPJVE。
- **关键结果 / 消融** · 表 1 未见类别 MPJPE 为 1.76，GLoT 为 7.42；表 2 去掉网格时由 1.76 升到 3.16。
- **适用条件 / 局限** · 需要合理绑定的参考资产，真实视频中的遮挡、尺度变化及不同动力学不由该测试独立覆盖。

**可复用机制** · 面向变化骨架时，可将关节轨迹估计与目标资产旋转解算分开，以参考几何条件控制输出。见表 1、2。

<a id="paper-cross-sensor-confidence-densification-and-self-match"></a>

## No Calibration, No Depth, No Problem: Cross-Sensor View Synthesis with 3D Consistency

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_No_Calibration_No_Depth_No_Problem_Cross-Sensor_View_Synthesis_with_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wu_No_Calibration_No_Depth_No_Problem_Cross-Sensor_View_Synthesis_with_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 跨传感器图像不易得到稠密同位训练对，直接映射外观不能保证三维一致性。
- **核心创新 / 方法** · 先跨模态对应，在高置信区域递推加密，以自匹配核验后合并到三维高斯表示。
- **Baseline** · 比较 PixNext、XoFTR、LightGlue、LoFTR、MINIMA，并逐项去掉自匹配、置信度和三维融合。
- **Benchmark** · RGB-NIR-Stereo、RGBT-Scenes 及 METU-VisTIR-Cloudy，报告 PSNR、SSIM、LPIPS 与一致性。
- **关键结果 / 消融** · 表 5 完整 PSNR 21.152，移除自匹配核验为 20.235，移除置信度为 19.621；去掉 3DGS 的 SSIM 反而更高。
- **适用条件 / 局限** · 仍借助 RGB 相机重建和可用跨传感器对应，极端光谱差异或时间不同步需重测。

**可复用机制** · 跨传感器难标定时，可以把稀疏跨域匹配先用置信度补稠，再用同域自匹配剔除不一致，分别查看增益。见表 5。

<a id="paper-cosettle-temporal-consistency-semantic-separability"></a>

## From Static to Dynamic: Exploring Self-supervised Image-to-Video Representation Transfer Learning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_From_Static_to_Dynamic_Exploring_Self-supervised_Image-to-Video_Representation_Transfer_Learning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_From_Static_to_Dynamic_Exploring_Self-supervised_Image-to-Video_Representation_Transfer_Learning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 重度视频微调可能降低跨视频语义区分，过少训练则不足以让同一对象的表示随时间保持。
- **核心创新 / 方法** · 在冻结图片编码器上学习轻量投影，以时间循环一致性结合语义可分性约束重排表示空间。
- **Baseline** · 对照 MAE 与 DINO 图片骨干、不同投影层，以及逐项移除目标。
- **Benchmark** · VIP、DAVIS17、JHMDB 的密集视频任务，使用 mIoU、J&F、PCK。
- **关键结果 / 消融** · 表 5 的 DINO 系列完整配置为 39.8 VIP mIoU、64.2 DAVIS J&F，表中第一消融行分别为 17.5 和 30.6。
- **适用条件 / 局限** · 依赖输入骨干的图像语义，长遮挡和极端新域易同时破坏循环追踪与区分。

**可复用机制** · 图像骨干转到视频时，可冻结骨干并同时考核跨视频可分性和同视频时序一致性，避免只优化同视频匹配。见表 4、5。

<a id="paper-tim-finite-interval-generation-objective"></a>

## Transition Models: Rethinking the Generative Learning Objective

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Transition_Models_Rethinking_the_Generative_Learning_Objective_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_Transition_Models_Rethinking_the_Generative_Learning_Objective_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 只学习瞬时动力学需要许多步，只学习终点则可能无法用更多步改善输出。
- **核心创新 / 方法** · 用连续时间动力学定义任意有限时间间隔的状态转移，让单个模型可按不同步数走同一路径。
- **Baseline** · 与 SD3.5-Large、FLUX.1-Dev 及少步版本 SD3.5-Turbo、FLUX.1-Schnell 比较。
- **Benchmark** · GenEval、DPGBench 和 ImageNet-256 等，报告不同 NFE 下的生成质量。
- **关键结果 / 消融** · 表 6 TiM 在 1、8、32 次评估的 GenEval 为 0.67、0.76、0.80，FLUX.1-Schnell 相应为 0.68、0.67、0.63。
- **适用条件 / 局限** · 不同模型对照的架构、训练集与计算预算有差异，实际吞吐和新任务迁移需要另测。

**可复用机制** · 希望同一模型可一次生成或多步逐级改进时，可直接学习任意有限区间的生成转移，并画出函数评估数与质量的关系。见表 6。

<a id="paper-global-video-token-selection-with-redundancy-refill"></a>

## Unified Spatiotemporal Token Compression for Video-LLMs at Ultra-Low Retention

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Du_Unified_Spatiotemporal_Token_Compression_for_Video-LLMs_at_Ultra-Low_Retention_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Du_Unified_Spatiotemporal_Token_Compression_for_Video-LLMs_at_Ultra-Low_Retention_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 先空间后时序的独立压缩会在很低保留率时丢掉少数关键画面或区域。
- **核心创新 / 方法** · 在统一时空池依据注意力和相似度挑选贡献高且互补的标记，对未选标记聚类合并后回填紧凑信息。
- **Baseline** · 对照主流视频压缩方法，以及注意力、相似度和聚类的组合消融。
- **Benchmark** · LLaVA-OneVision 等视频模型，在 MVBench、EgoSchema、MLVU、LongVideoBench、VideoMME 比较得分与标记保留率。
- **关键结果 / 消融** · 表 5 的完整三组件平均 50.4，单用注意力为 41.8，单用相似度为 49.2。
- **适用条件 / 局限** · 极低预算仍会错过短暂或语义罕见证据；采样、保留率和下游问法变化时应重新验算。

**可复用机制** · 视频标记保留率很低时，可在统一时空池分配预算，把显著性与去冗余及合并协同，并测哪些任务仍丢证据。见表 5。

<a id="paper-bml-noisy-correspondence"></a>

## Bootstrapping Multi-view Learning for Test-time Noisy Correspondence

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/He_Bootstrapping_Multi-view_Learning_for_Test-time_Noisy_Correspondence_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/He_Bootstrapping_Multi-view_Learning_for_Test-time_Noisy_Correspondence_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 只在对齐视图学习置信度，测试时的异步或语义错配无法从单视图质量推断。
- **核心创新 / 方法** · 通过训练内部的对应扰动构造样本，监督估计视内不确定性及视间预测差异。
- **Baseline** · 表1–2比较多视图方法，表3在50% TNC下消融。
- **Benchmark** · Caltech、Leaves、HW、LandUse、Scene 等多视分类，多个噪声率和十随机种子，准确率与标准差。
- **关键结果 / 消融** · 表1–2按噪声率给出对照，表3比较单模块移除。
- **适用条件 / 局限** · 人为错配需近似部署的采样错误，时间相关延迟和语义相似的错置应分别复验。

**可复用机制** · 将模态本身质量与视图配错视为异质误差，使用人为控制的错配标注训练两类可靠性。

<a id="paper-octopus-hifgo"></a>

## Octopus: History-Free Gradient Orthogonalization for Continual Learning in Multimodal Large Language Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_Octopus_History-Free_Gradient_Orthogonalization_for_Continual_Learning_in_Multimodal_Large_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_Octopus_History-Free_Gradient_Orthogonalization_for_Continual_Learning_in_Multimodal_Large_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 旧样本回放有存储成本，普通正则难完全避免任务更新互相干扰。
- **核心创新 / 方法** · 用无历史数据的梯度正交化约束更新，两阶段分别侧重当前适配与稳定。
- **Baseline** · 表1含顺序 LoRA 和多任务训练，表2–4改变正交法、阶段和范数控制。
- **Benchmark** · UCIT 各任务 Avg 和 Last，表5比较任务顺序。
- **关键结果 / 消融** · 表1报告相对先前最好方法 Avg 和 Last 的改善，表2–4拆分来源。
- **适用条件 / 局限** · 测试范围集中于 UCIT，若新旧梯度高度同向或任务变化很快，正交可能降低可塑性。

**可复用机制** · 不能存旧数据时，分阶段执行当前任务适配和梯度去干扰，并显式比较任务顺序。

<a id="paper-self-swap-guidance"></a>

## Guiding a Diffusion Model by Swapping Its Tokens

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Guiding_a_Diffusion_Model_by_Swapping_Its_Tokens_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Guiding_a_Diffusion_Model_by_Swapping_Its_Tokens_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · CFG依赖条件与无条件差值，纯无条件生成缺少这一对照。
- **核心创新 / 方法** · 在空间或通道维换位不相似 token，利用原预测与扰动预测的差指引采样。
- **Baseline** · 表1–4与条件及无条件引导法比较，表5对照交换策略。
- **Benchmark** · MS-COCO 2014/2017、ImageNet，测 FID、IS、精度召回及文本对齐。
- **关键结果 / 消融** · 表1–2提供无条件比较，表3–4有条件比较，表5定位换位规则的作用。
- **适用条件 / 局限** · 需要潜 token 具有可比较的语义并允许额外前向，扩散结构改变时需重校。

**可复用机制** · 没有可用条件分支时，可用语义错配潜 token 生成对照预测，再利用两支差异指导扩散。

<a id="paper-clivis-cognitive-map"></a>

## CLiViS: Unleashing Cognitive Map through Linguistic-Visual Synergy for Embodied Visual Reasoning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_CLiViS_Unleashing_Cognitive_Map_through_Linguistic-Visual_Synergy_for_Embodied_Visual_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_CLiViS_Unleashing_Cognitive_Map_through_Linguistic-Visual_Synergy_for_Embodied_Visual_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 静态字幕遗漏细节，端到端模型难多步组合跨时间观察。
- **核心创新 / 方法** · 以 LLM 制订取证步骤，用开放世界视觉模型迭代感知并更新认知地图。
- **Baseline** · 表1统一 FPS、温度等配置比较，表2在同一 LLM 下换 VLM，表3做组件消融。
- **Benchmark** · OpenEQA、EgoTempo、EgoSchema 的具身和第一视角视频问答。
- **关键结果 / 消融** · 表2比较不同观察模型的收益，表3检验地图和取证组件。
- **适用条件 / 局限** · 地图一致性依赖视觉模型可追踪对象与时间，长片段的错误累积和调用成本需测。

**可复用机制** · 跨时刻具身推理可让计划器按需调视觉模型，再累计可更新的结构化场景记忆。

<a id="paper-next-scale-prediction"></a>

## Next-Scale Prediction: A Self-Supervised Approach for Real-World Image Denoising

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Shan_Next-Scale_Prediction_A_Self-Supervised_Approach_for_Real-World_Image_Denoising_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Shan_Next-Scale_Prediction_A_Self-Supervised_Approach_for_Real-World_Image_Denoising_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 同尺度下采样太大损细节，太小不能解相关。
- **核心创新 / 方法** · 让盲点网络从已去相关的低分辨率子图预测较高分辨率目标，构建跨尺度配对。
- **Baseline** · 表1比较 DBSN、TBSN 等，表3对照训练目标，表4改升采样倍率。
- **Benchmark** · SIDD validation、benchmark 与 DND 的 PSNR/SSIM，表2另测噪声图超分。
- **关键结果 / 消融** · NSP(TBSN) 在 SIDD benchmark 为37.46 dB，DND 较 TBSN 低0.03 dB。
- **适用条件 / 局限** · 以降采样能破除噪声相关为前提，跨尺度相关强的传感噪声须复验。

**可复用机制** · 去噪自监督可分别选择输入和目标尺度，以较粗输入降低噪声相关，同时保留细目标监督。

<a id="paper-oco-object-cooccurrence-ood"></a>

## Mitigating Simplicity Bias in OOD Detection through Object Co-occurrence Analysis

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Dai_Mitigating_Simplicity_Bias_in_OOD_Detection_through_Object_Co-occurrence_Analysis_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Dai_Mitigating_Simplicity_Bias_in_OOD_Detection_through_Object_Co-occurrence_Analysis_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 模型可能偏向简单单物体特征，忽略异常来自已知对象的陌生组合。
- **核心创新 / 方法** · 从图像提取解耦对象线索，按训练内共现模式分情形评分。
- **Baseline** · 比较经典和近期 OOD 检测方法，另做共现相关消融。
- **Benchmark** · ImageNet-1K 训练、五个 OOD集及 ImageNet-v2/C/R 偏移集，使用 FPR95 等指标。
- **关键结果 / 消融** · 表1–3比较近 OOD、偏移和模块贡献。
- **适用条件 / 局限** · 训练中少见但合理组合会被误报，检测质量依赖对象识别。

**可复用机制** · 单个对象看起来都熟悉时，用对象组合共现的异常程度判断近分布外。

<a id="paper-groundingme-rejection-tests"></a>

## GroundingME: Exposing the Visual Grounding Gap in MLLMs through Multi-Dimensional Evaluation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_GroundingME_Exposing_the_Visual_Grounding_Gap_in_MLLMs_through_Multi-Dimensional_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_GroundingME_Exposing_the_Visual_Grounding_Gap_in_MLLMs_through_Multi-Dimensional_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 简单指代不考验相似目标、弱可见性及无目标时的拒绝。
- **核心创新 / 方法** · 划分相似辨别、关系、受限视觉和不可定位四类，以人工核实自动构造题。
- **Baseline** · 对照25种 MLLM，表3使用可选的非思考设置。
- **Benchmark** · GroundingME 的1005个案例，按任务维度测准确。
- **关键结果 / 消融** · 作者报告最高总体45.1%，多数模型在拒绝维度为0%。
- **适用条件 / 局限** · 题目筛选和提示会影响拒绝率，需按目标部署重新设置无法定位的条件。

**可复用机制** · 视觉指代评估单设不可定位的拒答场景，避免常规准确率掩盖强行输出。

<a id="paper-agft-soft-alignment"></a>

## AGFT: Alignment-Guided Fine-Tuning for Zero-Shot Adversarial Robustness of Vision-Language Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Cui_AGFT_Alignment-Guided_Fine-Tuning_for_Zero-Shot_Adversarial_Robustness_of_Vision-Language_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Cui_AGFT_Alignment-Guided_Fine-Tuning_for_Zero-Shot_Adversarial_Robustness_of_Vision-Language_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 硬分类标签容易破坏预训练图文相对关系，降低干净零样本表现。
- **核心创新 / 方法** · 以原模型软图文分布监督鲁棒适配，并作温度分布一致性校准。
- **Baseline** · 与标签监督微调及现有鲁棒适配方法比较。
- **Benchmark** · 15个零样本数据集，分开测干净与受扰条件准确率。
- **关键结果 / 消融** · 表1–3显示所测鲁棒性提升，并对照干净性能。
- **适用条件 / 局限** · 教师原有偏差会保留，所测扰动鲁棒不能代表部署安全。

**可复用机制** · 视觉语言模型做防御微调时保留原模型对全部文本的软语义对齐，并校准新的输出分布。

<a id="paper-gem-tfl-weak-temporal-localization"></a>

## GEM-TFL: Bridging Weak and Full Supervision for Forgery Localization through EM-Guided Decomposition and Temporal Refinement

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhu_GEM-TFL_Bridging_Weak_and_Full_Supervision_for_Forgery_Localization_through_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhu_GEM-TFL_Bridging_Weak_and_Full_Supervision_for_Forgery_Localization_through_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 二元弱标签监督稀疏，离散聚合阻断梯度，候选之间的关系被忽略。
- **核心创新 / 方法** · 以 EM 估计潜在属性，分类后回归时段，再使用候选图和时序一致性细化。
- **Baseline** · 对照充分及弱监督时间定位方法，表3检验组件。
- **Benchmark** · LAV-DF、AV-Deepfake1M 的伪造区间定位。
- **关键结果 / 消融** · 表1–3报告弱标签下的定位表现及各项增益。
- **适用条件 / 局限** · 潜在属性不保证有可辨语义，平滑可能合并相邻的短事件。

**可复用机制** · 只有视频级标签但要定位时段时，用潜属性丰富训练信号并联合重排相邻候选。

<a id="paper-ltc-hopfield-memory"></a>

## Coupling Liquid Time-Constant Encoders with Modern Hopfield Memory

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Swain_Coupling_Liquid_Time-Constant_Encoders_with_Modern_Hopfield_Memory_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Swain_Coupling_Liquid_Time-Constant_Encoders_with_Modern_Hopfield_Memory_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 高频输入更新会覆写慢上下文。
- **核心创新 / 方法** · 将当前液态时间常数状态作为现代 Hopfield 记忆查询，两个分量拼接至读出，并分析有界性与梯度。
- **Baseline** · 标准 LTC、添加或移除联想记忆及其他时序模型。
- **Benchmark** · 公开时间序列数据，比较任务性能及优化统计。
- **关键结果 / 消融** · 表1–2对照性能和 Hopfield 对优化指标的影响。
- **适用条件 / 局限** · 梯度收缩结论需要范数及 Lipschitz 条件，检索错误或容量变化会影响收益。

**可复用机制** · 连续时间模型中可把快速动态与较长期内容检索分开，避免单隐状态互相覆盖。

<a id="paper-vlm-loc-partial-scene-node-assignment"></a>

## VLM-Loc: Localization in Point Cloud Maps via Vision-Language Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Kang_VLM-Loc_Localization_in_Point_Cloud_Maps_via_Vision-Language_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Kang_VLM-Loc_Localization_in_Point_Cloud_Maps_via_Vision-Language_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 自然语言只提及局部地标，强制完整匹配会把未提及对象误当作定位约束。
- **核心创新 / 方法** · 以鸟瞰图和场景图表示点云，允许模型部分匹配图中节点，再根据匹配确定位置。
- **Baseline** · 比较完整与部分节点分配，也消融鸟瞰图、场景图和文本方向等输入。
- **Benchmark** · CityLoc-K 验证和测试集，以 5、10、15 米检索阈值的召回率衡量。
- **关键结果 / 消融** · 表 2 测试集的 5 米和 10 米召回率，部分分配为 35.91、63.81，完整分配为 17.81、41.55。
- **适用条件 / 局限** · 依赖点云图和描述中的地标可识别；重复地标或方向含混时仍需验证。

**可复用机制** · 用描述在地图中找位置时，应允许只对齐一部分图节点，避免未被描述的对象强制参与。见表 2。

<a id="paper-flooddiffusion-streaming-motion-noise-schedule"></a>

## FloodDiffusion: Tailored Diffusion Forcing for Streaming Motion Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Cai_FloodDiffusion_Tailored_Diffusion_Forcing_for_Streaming_Motion_Generation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Cai_FloodDiffusion_Tailored_Diffusion_Forcing_for_Streaming_Motion_Generation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 现有扩散强制直接用于连续动作时可能偏离真实动作分布，尤其在文本指令随时间改变时。
- **核心创新 / 方法** · 用训练内双向注意力、下三角时点安排和连续文本条件适配流式动作。
- **Baseline** · 与 ReMoDiffuse、T2M-GPT、MDM 等比较，并去除双向注意力或替换下三角计划。
- **Benchmark** · HumanML3D、BABEL 动作生成和流式设置，以 FID、文本动作匹配、召回和多样性衡量。
- **关键结果 / 消融** · 表 3 完整方案 FID 0.057，去双向为 3.377，去下三角为 3.883。
- **适用条件 / 局限** · 结果依赖动作表示与流式条件安排；训练中的双向注意力应按实际推理可见范围验证，避免未来信息泄漏。

**可复用机制** · 把视频扩散强制迁移到流式动作前，可对照训练内双向注意力和下三角噪声计划，验证条件变化与动作衔接。见表 3。

<a id="paper-panel2patch-hierarchical-figure-supervision"></a>

## From Panel to Pixel: Zoom-In Vision-Language Pretraining from Biomedical Scientific Literature

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yuan_From_Panel_to_Pixel_Zoom-In_Vision-Language_Pretraining_from_Biomedical_Scientific_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yuan_From_Panel_to_Pixel_Zoom-In_Vision-Language_Pretraining_from_Biomedical_Scientific_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 把复合科学图作为单张图与整段图说配对，会使文字指向的具体区域缺少监督。
- **核心创新 / 方法** · 从现成版式解析独立面板、视觉标记与相关文本，构造图、面板与标记区域三个粒度的监督。
- **Baseline** · 与 CLIP、仅面板和仅区域数据训练比较。
- **Benchmark** · 生物医学图的面板短描述检索、边框与描述检索，以双向 R@5、R@10 评估。
- **关键结果 / 消融** · 表 4 的框到文本 R@5，混合为 20.24，仅面板为 17.65，仅区域为 18.90；面板短描述的图到文 R@5 分别为 68.14、66.67、61.60。
- **适用条件 / 局限** · 依赖版式、标注符号与文中描述能自动对应，外推到没有明确面板的图或其他文档须重验。

**可复用机制** · 图文语料存在图、面板、局部标记多级结构时，可为各级保留分别对应的文本并单测局部检索。见表 4。

<a id="paper-pqdt-pseudo-query-spatial-restoration"></a>

## PQDT: Pseudo-Query Dual Transformer for Robust Point Cloud Restoration

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_PQDT_Pseudo-Query_Dual_Transformer_for_Robust_Point_Cloud_Restoration_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wu_PQDT_Pseudo-Query_Dual_Transformer_for_Robust_Point_Cloud_Restoration_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 点云缺失、不均匀和含噪时，全局特征瓶颈容易平滑局部结构。
- **核心创新 / 方法** · 用伪查询产生局部重建种子，再基于几何嵌入细化形状。
- **Baseline** · 对照原查询、线性种子投影、查询解码和几何位置编码等配置。
- **Benchmark** · ShapeNetCar-Occ 等点云退化基准，使用 Chamfer 距离和 F1。
- **关键结果 / 消融** · 表 3 的基线 CDℓ2 和 F1 为 0.857、0.243，加入伪查询为 0.840、0.255，完整为 0.818、0.261。
- **适用条件 / 局限** · 种子先验可能影响形状多样性，极端遮挡或真实传感器噪声不同于合成点云时需另测。

**可复用机制** · 点云退化时可让重建查询从局部种子出发，而非压缩进单一全局表示，并逐项比较种子和位置编码。见表 3。

<a id="paper-lapr-label-consistent-demonstration-retrieval"></a>

## Love Me, Love My Label: Rethinking the Role of Labels in Prompt Retrieval for Visual In-Context Learning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Luo_Love_Me_Love_My_Label_Rethinking_the_Role_of_Labels_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Luo_Love_Me_Love_My_Label_Rethinking_the_Role_of_Labels_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 外观接近的示例可能使用不一致的目标标签，反而改变模型正在被提示的任务。
- **核心创新 / 方法** · 将示例图像和标签联合表示，以路由模块推断查询在检索时所需的标签线索。
- **Baseline** · 对照移除路由、移除提示标签和不同训练配置，另对比 SupPR、ParPR 等。
- **Benchmark** · 视觉上下文学习的分割与单对象检测等任务，使用分折 mIoU。
- **关键结果 / 消融** · 表 3 分割与检测分别为 41.36、32.01，去提示标签为 39.19、30.94，去路由为 38.20、29.69。
- **适用条件 / 局限** · 示例标签必须可靠，检索器在开放类和弱标签变化时可能发生误路由。

**可复用机制** · 挑视觉上下文示例时可把标签兼容性与外观相似性分开考虑，以相同示例预算检验标签信息的增量。见表 3。

<a id="paper-meshripple-frontier-topology-tokenization"></a>

## MeshRipple: Structured Autoregressive Generation of Artist-Meshes

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Lin_MeshRipple_Structured_Autoregressive_Generation_of_Artist-Meshes_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Lin_MeshRipple_Structured_Autoregressive_Generation_of_Artist-Meshes_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 网格面序列截断和滑窗推理会切断拓扑关系，造成破洞或碎片。
- **核心创新 / 方法** · 使用按边界展开的广度优先标记顺序，生长相邻面，并以全局稀疏记忆关联较远结构。
- **Baseline** · 与其他网格生成方法比较，并分别去掉边界掩膜、上下文注入、根约束及稀疏注意力。
- **Benchmark** · Dense-Mesh、Artist-Mesh 和场景网格生成，报告 Chamfer 距离、Hausdorff 距离和开销。
- **关键结果 / 消融** · 表 2 完整 CD 为 52.67，去边界掩膜为 54.79，去上下文注入是 60.56；无稀疏注意力时指标略好。
- **适用条件 / 局限** · 拓扑遍历依赖连通分量和根的选择，全局记忆的算力用途应与其轻微质量取舍一起衡量。

**可复用机制** · 生成连通离散结构时可把顺序设为沿当前拓扑边界扩张，而非机械串行化，并把生成质量和长程记忆开销分开测。见表 2、4。

<a id="paper-visualad"></a>

## VisualAD: Language-Free Zero-Shot Anomaly Detection via Vision Transformer

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Hou_VisualAD_Language-Free_Zero-Shot_Anomaly_Detection_via_Vision_Transformer_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Hou_VisualAD_Language-Free_Zero-Shot_Anomaly_Detection_via_Vision_Transformer_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 用文字分开描述正常和异常依赖跨模态对齐，也可能使检测不稳定。
- **核心创新 / 方法** · 冻结视觉骨干，以两个可训练锚 token 与各层 patch 交互，并在像素级融合局部信息。
- **Baseline** · 表1比较已有零样本检测法，表2–4比较架构组件、锚数量和层组合。
- **Benchmark** · 工业和医疗基准，图像级检测及像素级定位。
- **关键结果 / 消融** · 表1跨两类基准比较结果，表2报告逐个移除模块的影响。
- **适用条件 / 局限** · 需有训练域用于学习正常与异常锚，强域偏差下不能假定锚仍通用。

**可复用机制** · 零样本异常检测可先检验纯视觉正常/异常锚 token 能否替代文本提示。

<a id="paper-spectrum-diffusion-forecast"></a>

## Adaptive Spectral Feature Forecasting for Diffusion Sampling Acceleration

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Han_Adaptive_Spectral_Feature_Forecasting_for_Diffusion_Sampling_Acceleration_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Han_Adaptive_Spectral_Feature_Forecasting_for_Diffusion_Sampling_Acceleration_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 缓存局部历史的外推误差会随跳步距离放大。
- **核心创新 / 方法** · 把去噪特征视为时间函数，用岭回归拟合 Chebyshev 基并预测后续特征。
- **Baseline** · 表1–2在不同骨干比较推理加速方案；表3–4拆分调度和缓存位置。
- **Benchmark** · DrawBench 的 Flux、SD3.5；VBench 的 Wan2.1、HunyuanVideo，50步参考，表5测潜特征 RMSE。
- **关键结果 / 消融** · 表3–5分别检查调度、末层缓存和对真特征近似。
- **适用条件 / 局限** · 高频突变会破坏光滑假设，换任务应重新测步段误差和收益。

**可复用机制** · 跳过多个去噪步时以全局光滑基预测特征，并用实际误差自适应安排重算。

<a id="paper-progressive-architecture-generation"></a>

## Progressive Neural Architecture Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yu_Progressive_Neural_Architecture_Generation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yu_Progressive_Neural_Architecture_Generation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 一次性生成的大结构可能不合法，且直接搜索大量候选开销高。
- **核心创新 / 方法** · 多尺度向量量化逐级解码子架构，借逐步一致性约束做修正。
- **Baseline** · 表1–4分别比较四类搜索空间的既有方法，表5改变搜索目标。
- **Benchmark** · NB201、MBV3、DARTS、AutoFormer，分类准确率及效率。
- **关键结果 / 消融** · 表1–4覆盖多种结构族，表5验证目标切换。
- **适用条件 / 局限** · 要求搜索空间能层级描述，复杂跨层连接约束须明确建模。

**可复用机制** · 架构生成先产粗子结构后扩张，在每次扩张时检查有效性。

<a id="paper-shape-of-you-fgw"></a>

## Shape-of-You: Fused Gromov-Wasserstein Optimal Transport for Semantic Correspondence in-the-Wild

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Im_Shape-of-You_Fused_Gromov-Wasserstein_Optimal_Transport_for_Semantic_Correspondence_in-the-Wild_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Im_Shape-of-You_Fused_Gromov-Wasserstein_Optimal_Transport_for_Semantic_Correspondence_in-the-Wild_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 纹理重复和对称会让视觉近邻误匹配。
- **核心创新 / 方法** · 以3D特征约束 FGW，锚点线性化近似求解，得到软运输计划和预测混合作监督。
- **Baseline** · 表1–2比较既有语义对应方案，表3消融伪标签结构，表4消融训练设计。
- **Benchmark** · SPair-71k 的逐关键点 PCK@0.1，另报告多个阈值及类别。
- **关键结果 / 消融** · 表3验证结构来源，表4检查训练组件贡献。
- **适用条件 / 局限** · 依赖场景内结构可被几何特征捕获，锚点稀少会引入局部近似误差。

**可复用机制** · 伪标签匹配时，将特征相似和结构相似合并，并保留软分配而非硬最近邻。

<a id="paper-edgs-dense-initialization"></a>

## EDGS: Eliminating Densification for Efficient Convergence of 3DGS

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Kotovenko_EDGS_Eliminating_Densification_for_Efficient_Convergence_of_3DGS_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Kotovenko_EDGS_Eliminating_Densification_for_Efficient_Convergence_of_3DGS_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 从稀疏 SfM 初始化重复拆分高斯，慢且高频区域仍可能不足。
- **核心创新 / 方法** · 三角化稠密对应直接初始化高斯位置、颜色和尺度，随后优化而不做常规增密。
- **Baseline** · 表1比较既有3DGS，表2比较早停，表3作为其他增密方法初值，表5换匹配器。
- **Benchmark** · Mip-NeRF 360、Tanks & Temples、Deep Blending 的重建质量和训练开销。
- **关键结果 / 消融** · 表2对比早停，表3–5验证初始化及去增密能否分别使用。
- **适用条件 / 局限** · 依赖相机和稠密对应可靠，无纹理或动态遮挡会影响三角化。

**可复用机制** · 若可获得高质量稠密像素对应，可从初始化解决细几何覆盖，减少逐步增密。

<a id="paper-numina"></a>

## When Numbers Speak: Aligning Textual Numerals and Visual Instances in Text-to-Video Diffusion Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Sun_When_Numbers_Speak_Aligning_Textual_Numerals_and_Visual_Instances_in_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Sun_When_Numbers_Speak_Aligning_Textual_Numerals_and_Visual_Instances_in_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 文字数词和视频里实例数常不一致，换 seed 无法定向约束错误。
- **核心创新 / 方法** · 选自注意和跨注意头获取布局，保守修正并调制跨注意生成。
- **Baseline** · 表1比较 seed 搜索、提示增强等方案，表2–4拆分布局与注意力选择。
- **Benchmark** · CountBench，多尺度视频模型的计数正确、CLIP 对齐及时序一致性。
- **关键结果 / 消融** · 正文报告 Wan2.1-1.3B 最高改善7.4%，5B及14B分别4.9%和5.5%。
- **适用条件 / 局限** · 依赖可从注意力分离目标实例，遮挡和多个同类群体仍需单测。

**可复用机制** · 生成对数量敏感时，先从隐场定位可计数实例，再调整布局并重生成。

<a id="paper-tigon-conditioned-3d"></a>

## Text-Image Conditioned 3D Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Cen_Text-Image_Conditioned_3D_Generation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Cen_Text-Image_Conditioned_3D_Generation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 图像条件有视角偏差，纯文本缺少局部外观。
- **核心创新 / 方法** · 以图像和文本条件双支路为基础，用轻量连接融合，保留单模态与无连接对照。
- **Baseline** · 表1比较多种单模态及融合模型，表3消融连接。
- **Benchmark** · Toys4K 和 UniLat1K，按单图像、单文本、联合条件比较重建或生成指标。
- **关键结果 / 消融** · 表1给简单后融合的诊断证据，表2及表3比较双条件和连接。
- **适用条件 / 局限** · 输入图文冲突时晚融合的取舍需校准，几何隐区域评价仍受可用视角局限。

**可复用机制** · 联合图文条件前先做各自独立推理及晚融合，测两个模态在几何和语义上的互补。

<a id="paper-smoes-soft-modality-routing"></a>

## Soft Modality-Guided Expert Specialization in MoE-VLMs

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Bo_Soft_Modality-Guided_Expert_Specialization_in_MoE-VLMs_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Bo_Soft_Modality-Guided_Expert_Specialization_in_MoE-VLMs_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 硬分模态会忽略中间层跨模态混合，完全无约束路由又分组不集中。
- **核心创新 / 方法** · 从注意力或统计量获得软分数，与按部署划分的专家组做互信息正则。
- **Baseline** · DeepSeekMoE、OLMoE 等骨干上的原路由，另改模态分数和分组约束。
- **Benchmark** · 四种视觉语言 MoE、16项多模态和语言任务，评估分数、通信和吞吐。
- **关键结果 / 消融** · 作者报告通信开销减少56.1%、吞吐升12.3%，所测任务总体改善。
- **适用条件 / 局限** · 依赖组间通信成本及软分数质量，专家负载与上下文长短会影响收益。

**可复用机制** · 多模态 MoE 训练可用随层变化的软模态分数引导专家分组，以减少跨设备通信。

<a id="paper-cps-prompt-edge-continual"></a>

## Critical Patch-Aware Sparse Prompting with Decoupled Training for Continual Learning on the Edge

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Lim_Critical_Patch-Aware_Sparse_Prompting_with_Decoupled_Training_for_Continual_Learning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Lim_Critical_Patch-Aware_Sparse_Prompting_with_Decoupled_Training_for_Continual_Learning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 只减少可训练参数，仍可能在设备上缓存过多激活。
- **核心创新 / 方法** · 任务相关图块稀疏采样，结合解耦的提示、分类训练降低反传。
- **Baseline** · CODA-Prompt、C-Prompt 与其他持续学习方案。
- **Benchmark** · 三个公开数据集含 ImageNet-R，并实测边缘设备峰值内存、耗时、能耗。
- **关键结果 / 消融** · 作者报告相对 CODA-Prompt 三项效率约1.6倍，平均准确率距 C-Prompt 约2%内。
- **适用条件 / 局限** · 全局场景或小目标关键区域可能被采样遗漏，硬件实现会改变收益。

**可复用机制** · 边缘持续学习时按任务选择训练图块，并将提示和分类头反传拆开。

<a id="paper-online-mapping-failure-mode-controls"></a>

## Failure Modes for Deep Learning-Based Online Mapping: How to Measure and Address Them

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Hubbertz_Failure_Modes_for_Deep_Learning-Based_Online_Mapping_How_to_Measure_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Hubbertz_Failure_Modes_for_Deep_Learning-Based_Online_Mapping_How_to_Measure_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 只做地理去重仍可能保留相似道路几何，无法识别模型到底记忆了什么。
- **核心创新 / 方法** · 用受控子集及 Fréchet 路径统计度量定位线索和形状偏见，再以最小生成树疏减冗余。
- **Baseline** · 现有在线制图方法及原始、地理不交叠、几何分割对照。
- **Benchmark** · nuScenes、Argoverse 2，报告定位及几何过拟合分数和布局覆盖。
- **关键结果 / 消融** · 表1–2呈现两种划分及模型退化的差异，正文检验减冗余。
- **适用条件 / 局限** · 几何相似度不能度量所有场景难度，两个因素仍可能部分相关。

**可复用机制** · 地图模型的域外评估同时控制地理邻近和几何相似度，并分别报告两种过拟合。

<a id="paper-think360-reasoning-width"></a>

## Think 360deg: Beyond Depth: Evaluating the Width-centric Reasoning Capability of MLLMs

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Think_360deg_Beyond_Depth_Evaluating_the_Width-centric_Reasoning_Capability_of_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_Think_360deg_Beyond_Depth_Evaluating_the_Width-centric_Reasoning_Capability_of_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 长推理链不等价于能在多约束下覆盖候选空间。
- **核心创新 / 方法** · 构建宽度与深度联合控制的题目和搜索树评价。
- **Baseline** · 对照12个模型家族、超过30个开源及专有模型。
- **Benchmark** · 1200余图文题，跨难度、问题类别和所需搜索能力。
- **关键结果 / 消融** · 所测模型一般问答较强，但同时需要宽搜索和深验证时仍困难。
- **适用条件 / 局限** · 题目构造与可观察输出只能约束所测行为，不可直接还原模型内部搜索树。

**可复用机制** · 评估多模态搜索时除了推理步数，还控制需要探索的并行候选和回溯。

<a id="paper-pgbl-boundary-anomaly-synthesis"></a>

## Multi-Prototype Compactness and Boundary-Aware Synthesis for Unsupervised Anomaly Detection

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Liao_Multi-Prototype_Compactness_and_Boundary-Aware_Synthesis_for_Unsupervised_Anomaly_Detection_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Liao_Multi-Prototype_Compactness_and_Boundary-Aware_Synthesis_for_Unsupervised_Anomaly_Detection_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 单球包住所有正常模式会在中间留下宽松边界。
- **核心创新 / 方法** · 学习多个紧致语义原型，在簇边界合成伪异常，再训练判别边界。
- **Baseline** · 对照既有无监督异常检测和组件去除。
- **Benchmark** · MVTec-AD、VisA、Real-IAD，比较工业异常检测。
- **关键结果 / 消融** · 表1–3给出多个基准结果和原型、伪异常各项贡献。
- **适用条件 / 局限** · 模式覆盖不充分时，簇边界可能包含罕见正常状态，伪负例需审计。

**可复用机制** · 正常类别有多个模式时，以多原型建模，并在簇边界构造难伪异常。

<a id="paper-orbit-panoramic-pose-reference"></a>

## ORBIT: Benchmarking SfM in the Wild with 360deg Video

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Sabour_ORBIT_Benchmarking_SfM_in_the_Wild_with_360deg_Video_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Sabour_ORBIT_Benchmarking_SfM_in_the_Wild_with_360deg_Video_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 困难相机运动或遮挡下，窄视角位姿真值难可靠得到。
- **核心创新 / 方法** · 借全景的丰富上下文恢复参照轨迹，再将指定区域投影为测试输入。
- **Baseline** · COLMAP 及现代多视图估计方法。
- **Benchmark** · ORBIT 有100个片段，测 ATE、平移和旋转 RPE 与成功率。
- **关键结果 / 消融** · 论文报告高难窄视角输入下多个现有 SfM 方法明显受限。
- **适用条件 / 局限** · 全景恢复仅是伪参考，其误差和裁剪选择会影响评估。

**可复用机制** · 要低成本获得窄视场视频难例的位姿参照，可用同一全景视频先估轨迹再进行裁剪重投影。

<a id="paper-videonet-single-action-filtering"></a>

## VideoNet: A Large-Scale Dataset for Domain-Specific Action Recognition

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yadav_VideoNet_A_Large-Scale_Dataset_for_Domain-Specific_Action_Recognition_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yadav_VideoNet_A_Large-Scale_Dataset_for_Domain-Specific_Action_Recognition_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 关键词和字幕包含许多同时活动的画面，弱标注难以指向一个明确动作。
- **核心创新 / 方法** · 对训练视频按单动作或字幕定位等条件过滤，并用同域难负例检验动作区分。
- **Baseline** · 比较原 Molmo2-4B、单动作过滤、字幕定位和字幕标题双匹配。
- **Benchmark** · VideoNet 的 38 个领域与 1087 种动作，报告领域内二选一等识别准确率。
- **关键结果 / 消融** · 表 5 单动作过滤 16.3 万条整体为 67.36%，字幕定位 50.1 万条为 65.11%，基座 55.01%；食品领域字幕定位反而更高。
- **适用条件 / 局限** · 过滤会缩减动作多样性，各领域收益不同，需要控制同样的优化预算和采集覆盖。

**可复用机制** · 训练细粒度视频识别时应对照按单一动作净化与仅按字幕定位扩样，分开测数据量和任务准确率。见表 5。

<a id="paper-dynbridge-shared-interaction-dynamics"></a>

## DynBridge: Bridging Imagination and Control through Interaction Dynamics for Robot Manipulation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_DynBridge_Bridging_Imagination_and_Control_through_Interaction_Dynamics_for_Robot_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_DynBridge_Bridging_Imagination_and_Control_through_Interaction_Dynamics_for_Robot_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 预测画面连贯也可能产生对当前动作不可实现或无帮助的结果。
- **核心创新 / 方法** · 以对象运动位置和作用方式构成共享交互表征，作为未来动态预测和动作解码的中间条件。
- **Baseline** · 比较行为克隆、UniPi、ATM、GraphMimic 等，并消融交互动态生成器及条件。
- **Benchmark** · LIBERO 五个任务集合和真实机器人，成功率对三个随机种子求均值。
- **关键结果 / 消融** · 表 1 在 LIBERO-Long 本方法为 0.71，GraphMimic 为 0.56；LIBERO-90 为 0.75 对 0.67。
- **适用条件 / 局限** · 成功率同时受到架构与数据来源影响，动态表征预测不能证明已掌握一般因果机制。

**可复用机制** · 将未来预测用于动作时，可共享对象位移与交互表征，比较面向控制的变化模型和仅预测画面或轨迹的方案。见第 4.2 节、表 1。

<a id="paper-vrga-reasoning-visual-attention-dispersion"></a>

## Deeper Thought, Weaker Aim: Understanding and Mitigating Perceptual Impairment during Reasoning in Multimodal Large Language Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Peng_Deeper_Thought_Weaker_Aim_Understanding_and_Mitigating_Perceptual_Impairment_during_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Peng_Deeper_Thought_Weaker_Aim_Understanding_and_Mitigating_Perceptual_Impairment_during_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 显式多步推理后，模型可能把图像注意力分散到与问题无关的区域。
- **核心创新 / 方法** · 按注意力熵与聚焦程度识别重要视觉头，对照遮蔽实验后，在推理时引导相关区域注意。
- **Baseline** · 比较无处理、随机遮蔽、按低视觉注意遮蔽和按空间聚焦遮蔽。
- **Benchmark** · TextVQA 用遮蔽准确率验证关键头，另用 HALO、HallusionBench、MMStar 测问答表现。
- **关键结果 / 消融** · 表 2 Qwen2.5-VL-7B 原准确率 86.88%，随机遮蔽为 86.95%，聚焦指标选头后遮蔽降至 40.52%。
- **适用条件 / 局限** · 遮蔽改变模型计算，可用于定位依赖，不能单独证明注意力是推理失误的唯一来源。

**可复用机制** · 长推理若降低视觉题表现，可用空间聚焦而非只用图像注意总量定位关键头，再做遮蔽对照。见表 2。

<a id="paper-bullettime-independent-world-time-camera-control"></a>

## BulletTime: Decoupled Control of Time and Camera Pose for Video Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_BulletTime_Decoupled_Control_of_Time_and_Camera_Pose_for_Video_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_BulletTime_Decoupled_Control_of_Time_and_Camera_Pose_for_Video_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 按视频帧序号建模会绑定对象运动和相机运动，无法单独改变世界时间流速。
- **核心创新 / 方法** · 将连续世界时间和相机轨迹作为独立条件，放入四维位置编码和自适应归一化。
- **Baseline** · 在 CogVideoX 上比较普通 RoPE、Time-RoPE、交叉注意力、通道相加和 AdaLN。
- **Benchmark** · 合成与实拍视频的相机及时间可控生成，以 PSNR、SSIM、LPIPS 衡量。
- **关键结果 / 消融** · 表 4 的 Time-RoPE 加 AdaLN 达 32.15 dB，标准 RoPE 加 AdaLN 为 29.83 dB。
- **适用条件 / 局限** · 独立控制依赖训练时两类因素有足够组合覆盖，极端路径、反向时间和遮挡需分别验证。

**可复用机制** · 视频世界模型可将世界时间与相机轨迹独立采样和输入，并单独验证时间控制、位置编码与归一化。见表 4、5。

<a id="paper-aac-action-entropy-adaptive-horizon"></a>

## Adaptive Action Chunking at Inference-time for Vision-Language-Action Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Liang_Adaptive_Action_Chunking_at_Inference-time_for_Vision-Language-Action_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Liang_Adaptive_Action_Chunking_at_Inference-time_for_Vision-Language-Action_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 固定长动作块降低反应速度，固定短块则容易在策略模式间跳变。
- **核心创新 / 方法** · 在推理时估计候选动作分布的熵，动态调整执行块长度，无需重训骨干。
- **Baseline** · 以固定执行块的 GR00T、π0.5 和不同熵样本数比较。
- **Benchmark** · LIBERO、LIBERO-Pro、RoboCasa 和真实操控，测任务成功率与推理时延。
- **关键结果 / 消融** · 表 3 的 π0.5 平均成功率为 30.9%，加 AAC 为 34.8%；表 4 五样本为 94.7%、83.5 毫秒，40 样本为 95.5%、157.0 毫秒。
- **适用条件 / 局限** · 熵需能代表真正需要重规划的状态，分布退化和严重扰动时应校准。

**可复用机制** · 视觉动作控制可用多个候选动作块的分歧决定执行多久后重新观测，同时测选样开销。见表 3、4。

<a id="paper-chain-of-merging-activation-matched-layers"></a>

## Beyond Layer-Wise Merging: Chain-of-Merging for Vision-Language Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Beyond_Layer-Wise_Merging_Chain-of-Merging_for_Vision-Language_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Beyond_Layer-Wise_Merging_Chain-of-Merging_for_Vision-Language_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 同层序号并不保证两个模型承担相同功能，统一权重融合可能削弱已有视觉能力。
- **核心创新 / 方法** · 用结构相似性和池化表示的语义相似性选配层并筛掉低分配对，对保留配对按不同权重球面插值。
- **Baseline** · 比较原 Qwen2.5-VL、LLaVA-NeXT、逐层线性合并和 IP-Merging。
- **Benchmark** · MathVista、MathVision、MathVerse、DynaMath、M3CoT、MMStar、Charxiv 的 Pass@1。
- **关键结果 / 消融** · 表 1 Qwen2.5-VL-7B 与 Qwen2.5-Math 的 MathVision 为 25.69，线性融合为 22.04，原模型为 18.09。
- **适用条件 / 局限** · 逐样本构建融合计划增加开销，权重插值仍要求层参数形状与结构足以兼容。

**可复用机制** · 融合语言模型与视觉语言模型时，可按输入的层激活结构选配层，再决定每层合并权重。见第 3.3、3.4 节与表 1。

<a id="paper-soc-label-preserving-object-composition"></a>

## Synthetic Object Compositions for Scalable and Accurate Learning in Detection, Segmentation, and Grounding

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_Synthetic_Object_Compositions_for_Scalable_and_Accurate_Learning_in_Detection_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_Synthetic_Object_Compositions_for_Scalable_and_Accurate_Learning_in_Detection_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 直接生成图与标签难持续保持边界和关系准确，大数据量也可能重复旧的组合。
- **核心创新 / 方法** · 先从独立对象掩膜按几何与相机布局组合画面，再做修补、重光照和按掩膜面积调节的融合。
- **Baseline** · 比较真片段、加合成片段、不同外观协调及相机或布局增强。
- **Benchmark** · COCO 零样本实例分割 AP，以及图像检测、区域定位与指代表达测试。
- **关键结果 / 消融** · 表 4 无外观协调 AP 6.28，修补、重光照和融合的完整设置为 12.79。
- **适用条件 / 局限** · 合成可能在对象边界或遮挡关系留下偏差，类别覆盖和标注一致性需要发布前检查。

**可复用机制** · 需要准确掩膜的合成训练可从独立对象片段与可控布局出发，再做保标签的外观协调。见表 4。

<a id="paper-weavetime"></a>

## WeaveTime: Streaming from Earlier Frames into Emergent Memory in VideoLLMs

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_WeaveTime_Streaming_from_Earlier_Frames_into_Emergent_Memory_in_VideoLLMs_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_WeaveTime_Streaming_from_Earlier_Frames_into_Emergent_Memory_in_VideoLLMs_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 离线训练的模型可能把视频当证据集合，难判顺序与现在/过去。
- **核心创新 / 方法** · 用时间重建任务训练顺序感知，在线用过去与当前的差异化缓存检索。
- **Baseline** · 表2含 ReKV 等，表3拆开顺序训练及缓存机制，表4比较检索。
- **Benchmark** · OVO-Bench 和 Streaming-Bench 实时子集，表1比较乱序/时间戳条件与人类。
- **关键结果 / 消融** · 表1证实乱序诊断与人类对照，表3检验训练及缓存互补。
- **适用条件 / 局限** · 需要各帧正确排序，延迟或丢帧会改变缓存选择的效果。

**可复用机制** · 先用打乱帧对照诊断时序盲区，再对在线缓存分别处理当前帧和历史证据。

<a id="paper-multimodal-homography-synthesis"></a>

## Towards Generalized Multimodal Homography Estimation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/You_Towards_Generalized_Multimodal_Homography_Estimation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/You_Towards_Generalized_Multimodal_Homography_Estimation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 用固定模态对训练的单应模型容易依赖颜色纹理。
- **核心创新 / 方法** · 由单图产生带已知几何偏移和不同纹理颜色的配对；网络用多尺度特征并弱化颜色。
- **Baseline** · 表1–4区分模型只用合成训练与向目标集使用合成方案。
- **Benchmark** · 跨 GoogleMap、GoogleEarth、RGB-NIR、PDSCOCO 的单应评估。
- **关键结果 / 消融** · 表1–4各自包含跨数据及合成配置，检验外观合成是否有域外收益。
- **适用条件 / 局限** · 几何必须保持单应关系，真实视差和传感器特有缺失需额外验证。

**可复用机制** · 没有目标传感器配对监督时，可保留几何结构并合成外观差异，再在真实未知模态上测试。

<a id="paper-flare-retry-reset"></a>

## FLARE: A Failure-Aware Framework for Autonomous Correction and Recovery in Visual-Language Robotic Manipulation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_FLARE_A_Failure-Aware_Framework_for_Autonomous_Correction_and_Recovery_in_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_FLARE_A_Failure-Aware_Framework_for_Autonomous_Correction_and_Recovery_in_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 仅用成功示范训练的 VLA 不懂从漏抓、掉落等异常返回任务。
- **核心创新 / 方法** · 训练注入扰动及恢复桥接片段，严重失败用离线分析确定重置数据的采集重点。
- **Baseline** · 表1比较九项 RoboMimic 策略，表2同 π0.5 基座对照，表3比较框架变体。
- **Benchmark** · RoboMimic 九类模拟任务及两项真实操作，衡量成功率。
- **关键结果 / 消融** · 表1平均84.0%，9项中8项排名最好；表2在真实任务对照。
- **适用条件 / 局限** · 严重失败可能需人或专门策略回收，重置成本和误判必须在真实场景测。

**可复用机制** · 按错误是否能从现有环境状态继续，把可重试偏差和需重置的失败分开收集。

<a id="paper-render-to-adapt"></a>

## Render-to-Adapt: Unsupervised Personal Adaptation for Gaze Estimation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Ge_Render-to-Adapt_Unsupervised_Personal_Adaptation_for_Gaze_Estimation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Ge_Render-to-Adapt_Unsupervised_Personal_Adaptation_for_Gaze_Estimation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 分组领域适配的平均值不保证每个用户都改善。
- **核心创新 / 方法** · 按预测视线渲染图像，以眼区一致性训练少量无标签个体样本上的适配。
- **Baseline** · 表1比较无适配及跨域个性化，表2比较组级适配，表3改变样本量与损失。
- **Benchmark** · 多个跨数据源个性化组合，凝视角误差。
- **关键结果 / 消融** · 表1–2对照组级与个人级，表3测适配样本量和组件。
- **适用条件 / 局限** · 渲染器偏差和初始视线预测错误可能互相强化，极少样本要做留出检查。

**可复用机制** · 个体适配缺标注时，可从模型预测渲染对照，再按观测局部一致性优化，并报告个体退化。

<a id="paper-videoauto-r1"></a>

## VideoAuto-R1: Video Auto Reasoning via Thinking Once, Answering Twice

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_VideoAuto-R1_Video_Auto_Reasoning_via_Thinking_Once_Answering_Twice_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_VideoAuto-R1_Video_Auto_Reasoning_via_Thinking_Once_Answering_Twice_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 总进行思维链会增加生成 token，视频任务并非都有收益。
- **核心创新 / 方法** · 先答、推理、再复答，两个答案均用可验证奖励；推理时门控是否复核。
- **Baseline** · 表1同视频条件比较直接与 CoT，表3比较仅思考模型，表4做时间定位。
- **Benchmark** · 视频问答、时间定位，报告准确率、答复长度和触发推理比例。
- **关键结果 / 消融** · 表1统一256帧及16K视频 token 证实直接回答有时相当或更优，表4评估早退。
- **适用条件 / 局限** · 依赖首答置信度对错误敏感，开放任务或新采样条件需重新校准。

**可复用机制** · 训练时同时奖励首答与复核答案，推理按首答置信度决定是否继续长链。

<a id="paper-refact"></a>

## ReFAct: Empowering Multimodal Web Agents with Visual and Context Focusing

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_ReFAct_Empowering_Multimodal_Web_Agents_with_Visual_and_Context_Focusing_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wu_ReFAct_Empowering_Multimodal_Web_Agents_with_Visual_and_Context_Focusing_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 每轮累积所有多模态页面会分散注意，过早删除又难恢复证据。
- **核心创新 / 方法** · 使用视觉定位工具获得区域，通过外部记忆机制减少当前上下文并允许复读。
- **Baseline** · 表2比较 Qwen2.5-VL 等原基座与搜索模型，表3拆解不同操作。
- **Benchmark** · GroundedVQA、MMSearch、SimpleVQA、LiveVQA，表2报告任务得分。
- **关键结果 / 消融** · 表2平均由原 Qwen2.5-VL-7B 的0.162到 ReFAct-7B 的0.460，表3诊断聚焦组件。
- **适用条件 / 局限** · 依赖外部搜索与区域定位，图面噪声减少后工具成本与收益应重新比较。

**可复用机制** · 网页视觉噪声大时，代理应能聚焦判断相关区域，并将暂时无关信息放入可回读记忆。

<a id="paper-sharptimegs-lifespan-modulation"></a>

## SharpTimeGS: Sharp and Stable Dynamic Gaussian Splatting via Lifespan Modulation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Liao_SharpTimeGS_Sharp_and_Stable_Dynamic_Gaussian_Splatting_via_Lifespan_Modulation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Liao_SharpTimeGS_Sharp_and_Stable_Dynamic_Gaussian_Splatting_via_Lifespan_Modulation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 统一衰减会用多个图元解释同一点，静态长寿命图元也可能漂移。
- **核心创新 / 方法** · 学习图元寿命并调节运动和增密，保留短寿命动态能力。
- **Baseline** · 表1比较动态高斯，表2去掉寿命和相关训练设计。
- **Benchmark** · Neural3DV、ENeRF-Outdoor、SelfCap，测 PSNR 等新视图渲染指标。
- **关键结果 / 消融** · 表1–2报告时序与画质表现及组件贡献。
- **适用条件 / 局限** · 平顶寿命假设不适合反复周期显隐，训练窗口也限制寿命可辨识。

**可复用机制** · 动态场景用平顶时域可见性记录图元何时存在，并以寿命调节运动先验。

<a id="paper-meanflow-discriminative-text"></a>

## Extending One-Step Image Generation from Class Labels to Text via Discriminative Text Representation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_Extending_One-Step_Image_Generation_from_Class_Labels_to_Text_via_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_Extending_One-Step_Image_Generation_from_Class_Labels_to_Text_via_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 无后续细化步骤时，语义高相似而内容不同的提示可能产生混淆。
- **核心创新 / 方法** · 诊断文本和图像对应的区分性，使用更可区分的文本表示适配 MeanFlow。
- **Baseline** · 类别 MeanFlow、常规文本编码方式及 BLIP3o-NEXT 等。
- **Benchmark** · GenEval 及对应的文本解耦、DINO 图像特征相似度。
- **关键结果 / 消融** · 表1–3显示编码器区分性与少步生成表现有关，并比较不同训练产物。
- **适用条件 / 局限** · 区分性代理不保证复杂提示依从；结论主要针对极少步生成。

**可复用机制** · 把一步生图扩展到开放文本时，单独测条件的区分性，而不只扩大文本编码器。

<a id="paper-filtr-topology-probes"></a>

## FILTR: Extracting Topological Features from Pretrained 3D Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Martinez_FILTR_Extracting_Topological_Features_from_Pretrained_3D_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Martinez_FILTR_Extracting_Topological_Features_from_Pretrained_3D_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 三维预训练通常测语义或几何误差，无法判断特征是否保持多尺度拓扑。
- **核心创新 / 方法** · 用受控合成拓扑数据，训练集合预测解码器由冻结表示恢复持久图。
- **Baseline** · Point-BERT、Point-MAE 等预训练表示及相应预测设定。
- **Benchmark** · DONUT 控制拓扑的分类和持久图重建，含留出集。
- **关键结果 / 消融** · 表1–3报告全局拓扑信号较有限，但可用解码器近似持久图。
- **适用条件 / 局限** · 合成拓扑与真实采样存在差别，探针可训练并不能证明骨干原读出使用了该信号。

**可复用机制** · 几何任务表现好也应探测冻结点云特征是否包含需要的拓扑环和空腔。

<a id="paper-msgnav-visual-scene-graph-edges"></a>

## MSGNav: Unleashing the Power of Multi-modal 3D Scene Graph for Zero-Shot Embodied Navigation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_MSGNav_Unleashing_the_Power_of_Multi-modal_3D_Scene_Graph_for_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_MSGNav_Unleashing_the_Power_of_Multi-modal_3D_Scene_Graph_for_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 文本关系边压缩后丢掉关键证据，开放词汇导航到目标附近也可能看不到目标。
- **核心创新 / 方法** · 场景图以代表图像作为关系证据，选子图做闭环推理，并显式选择终点视角。
- **Baseline** · GOAT-Bench 和 HM3D-ObjNav 的现有零样本导航，表3检查组件。
- **Benchmark** · GOAT-Bench 未见场景、HM3D-ObjNav，比较导航结果。
- **关键结果 / 消融** · 表1–3给出跨基准导航及图关系、收尾步骤的对照。
- **适用条件 / 局限** · 图像证据和图关联需要持续准确，存储与查询成本随场景增长。

**可复用机制** · 导航场景图的关系边保留可重查图像，决策终点时另检查目标可见性。

<a id="paper-noise-bilateral-defense-synergy"></a>

## A Combination of Noise and Bilateral Filters Achieve Supralinear and Scalable Adversarial Robustness in CNNs

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Stalder_A_Combination_of_Noise_and_Bilateral_Filters_Achieve_Supralinear_and_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Stalder_A_Combination_of_Noise_and_Bilateral_Filters_Achieve_Supralinear_and_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 只单独应用预处理或使用昂贵的鲁棒训练，难充分利用互补效果。
- **核心创新 / 方法** · 分析随机噪声与双边滤波的互补性，以受控消融验证组合，再比较与鲁棒训练叠加。
- **Baseline** · 分别使用噪声、滤波及组合，另比较现有防御。
- **Benchmark** · CIFAR-10、RobustBench，分开报告干净与鲁棒准确率及训练 FLOPs。
- **关键结果 / 消融** · 原文报告超线性收益，所测组合约使用对照35%的训练 FLOPs。
- **适用条件 / 局限** · 评估必须覆盖对随机防御适配的威胁，干净质量和部署域仍需另测。

**可复用机制** · 鲁棒视觉防御可比较随机化和保边去噪的组合收益，单项增益不足以预测叠加。

<a id="paper-qdwc-geometric-teacher-distillation"></a>

## Distilling Quasi-Conformal Mapping: A Generalizable and Efficient Solution for Wide-Angle Correction

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_Distilling_Quasi-Conformal_Mapping_A_Generalizable_and_Efficient_Solution_for_Wide-Angle_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_Distilling_Quasi-Conformal_Mapping_A_Generalizable_and_Efficient_Solution_for_Wide-Angle_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 广角变形既要保直线也要保人物轮廓，逐图几何优化成本高。
- **核心创新 / 方法** · 用拟共形能量和线条、人体约束离线创建位移真值，以网络回归校正流。
- **Baseline** · 拟共形求解教师及既有广角修正方法。
- **Benchmark** · Tan 智能手机测试及 Zhu 泛化集，报告 LineAcc、FaceAcc、BodyAcc 等。
- **关键结果 / 消融** · 作者报告从26.33秒降到0.81秒，约32倍，并列出跨域指标。
- **适用条件 / 局限** · 依赖教师约束正确及目标图像的结构覆盖，教师的错误也可能被继承。

**可复用机制** · 昂贵几何求解器无需人工标签也可当教师，蒸馏预测连续校正流。

<a id="paper-cca-cl-crossmodal-drift-sufficient-statistics"></a>

## Subspace Alignment for CLIP-based Continual Learning via Canonical Correlation Analysis

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Subspace_Alignment_for_CLIP-based_Continual_Learning_via_Canonical_Correlation_Analysis_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Subspace_Alignment_for_CLIP-based_Continual_Learning_via_Canonical_Correlation_Analysis_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 视觉数据随任务更新、文本提示相对固定时，预训练图文对齐会逐步偏移。
- **核心创新 / 方法** · 累积当前与先前任务的图文统计，用典型相关分析恢复共同投影，再配合轻量特征扩展。
- **Baseline** · 以全冻结 Continual-CLIP 作基础，依次加入 CCA、随机特征投影与首任务训练。
- **Benchmark** · CIFAR-100 等四组持续学习基准，报告分类准确率和学习开销。
- **关键结果 / 消融** · 表 2 CIFAR-100 基础为 66.7%，仅 CCA 为 76.5%，加投影为 81.0%，完整为 83.0%。
- **适用条件 / 局限** · 协方差样本需代表新旧类，强非线性漂移或类别极不平衡时应检验共享空间是否仍可估计。

**可复用机制** · 一侧模态持续漂移时，可累计图文协方差并用 CCA 重建共享子空间，先对照不作任何对齐的基线。见表 2。

<a id="paper-cgl-constrained-rl-for-continual-gui-retention"></a>

## CGL: Advancing Continual GUI Learning via Reinforcement Fine-Tuning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yao_CGL_Advancing_Continual_GUI_Learning_via_Reinforcement_Fine-Tuning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yao_CGL_Advancing_Continual_GUI_Learning_via_Reinforcement_Fine-Tuning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 应用界面更新时，仅监督微调能很快拟合新动作，却可能覆盖旧操作技能。
- **核心创新 / 方法** · 在连续学习中结合带 KL 约束的强化微调和按需调整比例的监督微调，减少互相冲突的更新。
- **Baseline** · 对照只做监督、加入 GRPO 或 KL，以及不同任务顺序和完整方案。
- **Benchmark** · 连续 GUI 任务报告单步准确率、轨迹准确率与遗忘量。
- **关键结果 / 消融** · 表 4 监督基线的轨迹准确率和遗忘为 23.53、−5.73，带 KL 的 SFT 加 GRPO 为 36.78、−0.62，完整为 38.03、−0.02。
- **适用条件 / 局限** · 依赖可可靠反馈的界面操作和已有能力，正文中未约束的 GRPO 不稳定；应用更换需验证任务差异。

**可复用机制** · 连续学习 GUI 操作时，可把新任务成功率和旧技能遗忘一起测，验证受约束强化学习与监督微调比例。见表 4。

<a id="paper-advanced-functional-maps-learned-spectral-basis"></a>

## From Feature Learning to Spectral Basis Learning: A Unifying and Flexible Framework for Efficient and Robust Shape Matching

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Luo_From_Feature_Learning_to_Spectral_Basis_Learning_A_Unifying_and_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Luo_From_Feature_Learning_to_Spectral_Basis_Learning_A_Unifying_and_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 固定拉普拉斯基限制功能映射的表达，单调特征无法克服谱基不匹配。
- **核心创新 / 方法** · 以可学习基替换固定基，使跨形状功能图在学习表征和基坐标中共同优化。
- **Baseline** · 比较 GeomFmaps、DiffZO、HybridFMaps 与 ULRSSM，涵盖有监督和无监督方案。
- **Benchmark** · FAUST、SCAPE、SHREC’19、SMAL、DT4D-H 的近等距、跨数据集及非等距对应，比较乘 100 的平均测地误差。
- **关键结果 / 消融** · 表 4 的 SMAL 误差为 2.6，HybridFMaps 微调为 2.8；FAUST 同域本方法 1.8，HybridFMaps 为 1.4。
- **适用条件 / 局限** · 学习基函数对训练形状及网格分布有依赖，优势并非各形态设置都成立。

**可复用机制** · 形状对应可在优化特征的同时学习映射所用基函数，对照固定谱基在跨数据、各向异性网格下的表现。见表 4。

<a id="paper-dfp-annealed-history-conditioning-for-planning"></a>

## Diffusion Forcing Planner: History-Annealed Planning with Time-Dependent Guidance for Autonomous Driving

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Diffusion_Forcing_Planner_History-Annealed_Planning_with_Time-Dependent_Guidance_for_Autonomous_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Diffusion_Forcing_Planner_History-Annealed_Planning_with_Time-Dependent_Guidance_for_Autonomous_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 把历史轨迹当作恒定条件可能缓和抖动，也可能在外部变化时复制已经失效的走法。
- **核心创新 / 方法** · 分开设置过去、当前和未来片段的噪声，使历史和未来共同去噪，并以随时间调整的条件控制历史作用。
- **Baseline** · 对照基础扩散规划器，单独加入扩散强制、分块或固定历史引导。
- **Benchmark** · nuPlan Val14 的非反应式与反应式闭环综合评分。
- **关键结果 / 消融** · 表 3 固定历史引导对应配置为 89.24、79.16，加入历史退火后为 90.33、79.97；只用扩散强制低于基础。
- **适用条件 / 局限** · 历史引导依赖轨迹可靠，突发安全变化和分布改变需另测响应时间。

**可复用机制** · 历史既提供平滑性也会诱使规划器照搬旧轨迹，可以比较固定历史引导和随去噪阶段变化的引导。见表 3。

<a id="paper-tc-pade-rational-feature-trajectory-extrapolation"></a>

## TC-Pade: Trajectory-Consistent Pade Approximation for Diffusion Acceleration

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/He_TC-Pade_Trajectory-Consistent_Pade_Approximation_for_Diffusion_Acceleration_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/He_TC-Pade_Trajectory-Consistent_Pade_Approximation_for_Diffusion_Acceleration_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 缓存间隔相对变大时，直接复用或多项式外推特征可能积累漂移。
- **核心创新 / 方法** · 用 Padé 有理近似预测缓存间的残差或特征演变，按去噪轨迹的阶段变化调整刷新。
- **Baseline** · 与原 FLUX.1-dev、ToCa、Δ-DiT、TeaCache、TaylorSeer 等比较。
- **Benchmark** · COCO 2017 图像生成、Wan2.1 视频 VBench 与 ImageNet 类条件生成，报告时延、FLOPs、FID 等。
- **关键结果 / 消融** · 表 1 的 20 步 FLUX 为 9.22 秒、FID 23.38，快速设置为 3.20 秒、FID 24.14。
- **适用条件 / 局限** · 近似稳定性受缓存步宽与特征变化影响，极少步生成和未测骨干应重设阈值。

**可复用机制** · 低步扩散缓存可以比较有理与多项式外推，并根据轨迹变化动态刷新，统计时延和输出质量。见表 1、5。

<a id="paper-splatent-geometry-detail-split-latent-rendering"></a>

## Splatent: Splatting Diffusion Latents for Novel View Synthesis

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Hirschorn_Splatent_Splatting_Diffusion_Latents_for_Novel_View_Synthesis_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Hirschorn_Splatent_Splatting_Diffusion_Latents_for_Novel_View_Synthesis_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 通用 VAE 潜变量缺乏稳定的跨视角细节，直接从图像生成细节又容易补出互相冲突的纹理。
- **核心创新 / 方法** · 先用三维高斯提供一致的低频渲染潜变量，再用扩散依据少量参考图补充细节。
- **Baseline** · 与 Feature-3DGS 和 LRF 比较，并对照 0、1、3、5 个参考图。
- **Benchmark** · DL3DV-10K、LLFF、Mip-NeRF360，评估 PSNR、LPIPS、FID 和视角一致性 MEt3R。
- **关键结果 / 消融** · 表 2 的密集 MEt3R 为 0.0774，LRF 为 0.1082；表 3 的三参考图 PSNR 为 21.94，五图为 21.96。
- **适用条件 / 局限** · 无法可靠复原所有参考视图都不可见的纹理，结构误差和判别性细节须另行测量。

**可复用机制** · 潜空间多视图重建可把低频几何交给三维渲染，仅以参考图引导扩散补充高频，单测参考数量与跨视角一致性。见表 2、3。

<a id="paper-franca-nested-clustering"></a>

## Franca: Nested Matryoshka Clustering for Scalable Visual Representation Learning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Venkataramanan_Franca_Nested_Matryoshka_Clustering_for_Scalable_Visual_Representation_Learning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Venkataramanan_Franca_Nested_Matryoshka_Clustering_for_Scalable_Visual_Representation_Learning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 单一粒度的聚类不稳定，固定 patch 坐标也可能被表征当作语义。
- **核心创新 / 方法** · 在共享表示内嵌套从粗到细的聚类头，并沿估计位置子空间作解耦。
- **Baseline** · 表2在 IN-21K 控制条件与 DINOv2 比较，表3–4涵盖其他视觉基础模型。
- **Benchmark** · 分类线性探测、密集分割与 DAVIS 等视频目标分割。
- **关键结果 / 消融** · 表2用控制比较分离训练差异，表3–4分别报告像素级与图像级。
- **适用条件 / 局限** · 需要有效的聚类分配和合理层级，坐标对空间推理本身有用时不宜直接压除。

**可复用机制** · 自监督聚类用多粒度嵌套标签处理语义歧义，并分离与内容无关的空间位置偏差。

<a id="paper-slow4fast-vln"></a>

## Towards Open Environments and Instructions: General Vision-Language Navigation via Fast-Slow Interactive Reasoning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Towards_Open_Environments_and_Instructions_General_Vision-Language_Navigation_via_Fast-Slow_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Towards_Open_Environments_and_Instructions_General_Vision-Language_Navigation_via_Fast-Slow_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 用相同风格环境和指令训练的快导航器难直接外推。
- **核心创新 / 方法** · 快慢推理交互，将高层解释和低时延动作选择分工，并随观察调整。
- **Baseline** · 表1–3比较 GSA-R2R 适配方法，表4模块消融。
- **Benchmark** · GSA-R2R 的基础及用户风格指令等协议，比较导航性能。
- **关键结果 / 消融** · 表1–3按指令条件对比，表4验证快慢交互贡献。
- **适用条件 / 局限** · 效果依赖慢规划能纠正错误而不持续干扰，延迟与真实环境分布需重测。

**可复用机制** · 陌生环境导航可用慢推理提供开放语义策略，再让快策略在闭环按最新观测执行。

<a id="paper-streamready"></a>

## StreamReady: Learning What to Answer and When in Long Streaming Videos

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Azad_StreamReady_Learning_What_to_Answer_and_When_in_Long_Streaming_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Azad_StreamReady_Learning_What_to_Answer_and_When_in_Long_Streaming_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 时序系统可能答得对却太早或太迟，只看最终准确率不反映实时效用。
- **核心创新 / 方法** · 用标注证据窗口定义非对称 Answer Readiness Score，并用轻量准备度模块控制回答时机。
- **Baseline** · 表2比较不同准备度模型，表3–4比较实时与离线结果。
- **Benchmark** · ProReady-QA 主动多轮、局部与全局问题，按证据时间与答案正确性评分。
- **关键结果 / 消融** · 表2按准备度与正确性评估，表3–4补充跨流式协议。
- **适用条件 / 局限** · 窗口标注需可靠，延迟成本在不同交互场景不对称程度不同，应重校。

**可复用机制** · 在线答复应把证据出现前猜测与出现后延迟分开处罚，结合正确性报告有效准确率。

<a id="paper-flatsounds-single-factor"></a>

## Benchmarking Single-Factor Physical Video-to-Audio Generation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Benchmarking_Single-Factor_Physical_Video-to-Audio_Generation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Benchmarking_Single-Factor_Physical_Video-to-Audio_Generation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 声音逼真不能证明模型从视觉知道物理成因，字幕可能遮盖视觉不足。
- **核心创新 / 方法** · 构造只改变一个物理因素的视频对，辅以单样本随时间规律测试。
- **Baseline** · 表1–4比较 MMAudio、Hunyuan 系等模型的有/无字幕条件。
- **Benchmark** · FlatSounds-Physics、FlatSounds-Single 及 VGGSound，报告物理指标、触发覆盖及时间误差。
- **关键结果 / 消融** · 正文发现字幕通常提高物理和语义准确性，却会损害时间对齐。
- **适用条件 / 局限** · 结论来自可控物理因素，开放真实场景的多同时成因尚不能直接外推。

**可复用机制** · 评估跨模态物理推理时用单因素反事实和有无文本对照，同时监测正确性与时序。

<a id="paper-unish-real-geometry-supervision"></a>

## UniSH: Unifying Scene and Human Reconstruction in a Feed-Forward Pass

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_UniSH_Unifying_Scene_and_Human_Reconstruction_in_a_Feed-Forward_Pass_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_UniSH_Unifying_Scene_and_Human_Reconstruction_in_a_Feed-Forward_Pass_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 人体和场景联合重建仅用合成监督会缺损表面细节与度量对齐。
- **核心创新 / 方法** · 蒸馏深度专家的高频细节，并在真实数据把 SMPL 网格与人体点云几何对应作为监督。
- **Baseline** · 表1–2比较深度与人体运动方法，表3消融人体表面细化。
- **Benchmark** · 人体中心视频深度与 EMDB-2、RICH 全局人体运动估计。
- **关键结果 / 消融** · 表1–2分开验证深度与运动，表3展示细节蒸馏作用。
- **适用条件 / 局限** · 依赖人体代理几何和专家深度在真实数据上可用，遮挡和人体之外仍需验证。

**可复用机制** · 合成数据学粗几何后，用真实无标签数据上可量化的跨表示对应缩小域差。

<a id="paper-spacemind"></a>

## SpaceMind: Camera-Guided Modality Fusion for Spatial Reasoning in Vision-Language Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_SpaceMind_Camera-Guided_Modality_Fusion_for_Spatial_Reasoning_in_Vision-Language_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_SpaceMind_Camera-Guided_Modality_Fusion_for_Spatial_Reasoning_in_Vision-Language_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · RGB 空间推理的浅融合难识别哪些特征与相机运动或视角相关。
- **核心创新 / 方法** · 双编码提取通用视觉及空间特征，用相机条件偏置、几何权重和门控融合。
- **Baseline** · 作者全文表4比较仅浅层交叉注意、增加 token 权重和完整几何模块。
- **Benchmark** · VSI-Bench、SQA3D、SPBench；用数值题、选择题和精确匹配评分。
- **关键结果 / 消融** · 作者全文表4逐级添加融合机制改善 VSI-Bench，表1–3分报告三基准。[作者全文](https://arxiv.org/html/2511.23075)
- **适用条件 / 局限** · 依赖可读的相机表示，对未知运动和严重动态几何误差需要单测。

**可复用机制** · 将相机嵌入用于几何 token 选择与融合门控，而非仅作附带信息。

<a id="paper-concept-guided-vit"></a>

## Concept-Guided Fine-Tuning: Steering ViTs away from Spurious Correlations to Improve Robustness

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Elisha_Concept-Guided_Fine-Tuning_Steering_ViTs_away_from_Spurious_Correlations_to_Improve_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Elisha_Concept-Guided_Fine-Tuning_Steering_ViTs_away_from_Spurious_Correlations_to_Improve_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 普通前景掩码没有区分哪些区域定义对象，模型仍会利用偶然背景。
- **核心创新 / 方法** · 生成类别相关概念并自动分割区域，对齐内部相关性图，压低非相关背景。
- **Baseline** · 表1比较分布外和分布内，表3比较相关性图与真区域对齐。
- **Benchmark** · 分布移位及 SI-Score 几何扰动，类别 Top-1、归因区域对齐。
- **关键结果 / 消融** · 表1–3同时检查可靠性和归因，降低从单个总体正确率推断捷径的误判。
- **适用条件 / 局限** · 概念提名及分割若错会带入新捷径，相关性图的改善并不单独证明真实因果机制。

**可复用机制** · 为降低背景捷径，用多个属性级概念区域监督相关性，而不是只提供前景掩码。

<a id="paper-car-spectral-confusion-regularizer"></a>

## Confusion-Aware Spectral Regularizer for Long-Tailed Recognition

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhu_Confusion-Aware_Spectral_Regularizer_for_Long-Tailed_Recognition_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhu_Confusion-Aware_Spectral_Regularizer_for_Long-Tailed_Recognition_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 重采样或重加权可能提高平均分，却未减少最弱类之间的混淆。
- **核心创新 / 方法** · 用可微软混淆及 EMA 统计近似谱范数正则，并分析其与最坏类误差上界的关系。
- **Baseline** · 比较现有长尾分类及相同骨干的未正则对照。
- **Benchmark** · ImageNet-LT、CIFAR100-LT、Tiny-ImageNet-LT、iNaturalist；ViT-Small 分类 top-1 及分组表现。
- **关键结果 / 消融** · 表1–2报告多套长尾分布的结果，理论上界含模型复杂度项。
- **适用条件 / 局限** · 软混淆估计依赖尾类覆盖；降低谱范数不保证所有类别同步改善。

**可复用机制** · 关注长尾最差类别时，把频率加权的混淆谱范数纳入训练。

<a id="paper-srpo-self-referential-policy"></a>

## SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Fei_SRPO_Self-Referential_Policy_Optimization_for_Vision-Language-Action_Models_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Fei_SRPO_Self-Referential_Policy_Optimization_for_Vision-Language-Action_Models_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 失败轨迹并非每一段都无价值，像素相似也不能可靠表示任务进展。
- **核心创新 / 方法** · 用世界模型的潜表示比较失败和成功轨迹，形成自参考密集反馈。
- **Baseline** · 以现有 VLA 鲁棒性与强化学习设置对照，包括 OpenVLA-OFT 系列。
- **Benchmark** · LIBERO 和 LIBERO-Plus，按机器人操作任务及扰动测成功率。
- **关键结果 / 消融** · 表1–2报告模拟操作与鲁棒性结果。
- **适用条件 / 局限** · 训练批需出现较可靠的成功轨迹，多种有效解或错误视觉相似可能误导反馈。

**可复用机制** · 二元成功奖励太稀疏时，可用同批成功轨迹给失败轨迹的进度分级。

<a id="paper-flashvggt-descriptor-attention"></a>

## FlashVGGT: Efficient and Scalable Visual Geometry Transformers with Compressed Descriptor Attention

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_FlashVGGT_Efficient_and_Scalable_Visual_Geometry_Transformers_with_Compressed_Descriptor_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_FlashVGGT_Efficient_and_Scalable_Visual_Geometry_Transformers_with_Compressed_Descriptor_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 跨图像匹配的全局注意力随序列长度和词元数增长。
- **核心创新 / 方法** · 保留细粒度图像查询，对少数描述符作跨注意力，递归复用先前分块缓存。
- **Baseline** · 原 VGGT 和其他前馈注意力或重建方案。
- **Benchmark** · RealEstate10K 相机姿态，Sintel、Bonn 深度，100/500/1000图像密集重建。
- **关键结果 / 消融** · 表1–3比较精度与长序列效率，描述符压缩后仍保持竞争力。
- **适用条件 / 局限** · 压缩可能漏掉只出现在少数帧的细节，缓存需要应对累积误差。

**可复用机制** · 前馈多视图重建可将跨帧的全局键值替换为每帧压缩描述符，并缓存跨块。

<a id="paper-auditdm-model-disagreement"></a>

## Differences That Matter: Auditing Models for Capability Gap Discovery and Rectification

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_Differences_That_Matter_Auditing_Models_for_Capability_Gap_Discovery_and_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_Differences_That_Matter_Auditing_Models_for_Capability_Gap_Discovery_and_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 静态平均分不能定位哪些能力差异稳定，随机补数据不一定命中失败。
- **核心创新 / 方法** · 训练评审利用模型分歧选择诊断问图对，并聚合为可解释失败类型及修正数据。
- **Baseline** · 原模型和失败发现、修正对照；原文评估 Gemma-3、PaliGemma-2。
- **Benchmark** · 16项多模态基准及主动审计任务，测故障识别和修正后表现。
- **关键结果 / 消融** · 作者报告发现超过20种失败，并有3B模型在所测设置超过28B对照。
- **适用条件 / 局限** · 模型一致犯错不会产生分歧，高分歧也不能替代事实核验。

**可复用机制** · 对照多个模型的相互分歧，主动构造诊断样例，再把找到的失败用于定向修正训练。

<a id="paper-tg-dp-decoupled-masking"></a>

## Semantic Noise Reduction via Teacher-Guided Dual-Path Audio-Visual Representation Learning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Semantic_Noise_Reduction_via_Teacher-Guided_Dual-Path_Audio-Visual_Representation_Learning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_Semantic_Noise_Reduction_via_Teacher-Guided_Dual-Path_Audio-Visual_Representation_Learning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 适合恢复的随机掩码可去掉视听对齐必需的语义证据。
- **核心创新 / 方法** · 重建和对齐分别前向，用教师组织对比路径的不同可见片。
- **Baseline** · CAV-MAE Sync 与常规共享可见性配置。
- **Benchmark** · AudioSet、VGGSound 零样本视听检索 R@1；AS20K、VGGSound 做线性探测。
- **关键结果 / 消融** · AudioSet 视频到音频 R@1 从35.2%至37.4%，音频到视频从27.9%至37.1%。
- **适用条件 / 局限** · 拆分前向增加训练成本，教师可能偏向最显著而非真正对应的事件。

**可复用机制** · 同时做掩码恢复和跨模态对比时，分开为两路选择可见 token。

<a id="paper-differentiable-straightest-geodesics"></a>

## Parallelised Differentiable Straightest Geodesics for 3D Meshes

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Verninas_Parallelised_Differentiable_Straightest_Geodesics_for_3D_Meshes_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Verninas_Parallelised_Differentiable_Straightest_Geodesics_for_3D_Meshes_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 离散网格的黎曼算子求导和并行困难，限制端到端学习。
- **核心创新 / 方法** · 并行追踪最直测地线并实现两种梯度近似，展示测地卷积和网格流匹配。
- **Baseline** · 比较原有几何算子及 XYZ、HKS 等表示，评估梯度和方向误差。
- **Benchmark** · 网格测地精度、部件分割，并测试质心 Voronoi 优化。
- **关键结果 / 消融** · 表1–2和实例表明算子支持几何优化与学习。
- **适用条件 / 局限** · 网格不均匀、尖角及离散近似会影响梯度，GPU 性能取决于批规模。

**可复用机制** · 网格模型需要沿曲面卷积或流动时，使用可并行、可微的指数映射代替欧氏邻域。

<a id="paper-floorplan-distribution-aware-depth-semantic-fusion"></a>

## Fusion of Depth and Semantics for Probabilistic Floorplan Localization

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Ye_Fusion_of_Depth_and_Semantics_for_Probabilistic_Floorplan_Localization_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Ye_Fusion_of_Depth_and_Semantics_for_Probabilistic_Floorplan_Localization_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 遮挡、相似房间与语义误判都可能让点值射线与平面图匹配到错误位置。
- **核心创新 / 方法** · 统一融合深度与语义分布，按射线分布估计可靠性，并对语义概率使用 Jensen–Shannon 距离。
- **Baseline** · 比较 SemRayLoc、单独平面图条件、射线置信度与概率语义匹配。
- **Benchmark** · S3D 与 ZInD 的室内平面图定位，以相机位置召回率和姿态误差评估。
- **关键结果 / 消融** · 表 4 S3D(full) 上 UFA 单独加置信度与精化为 69.8，完整方案召回为 71.4。
- **适用条件 / 局限** · 高度依赖平面图可用且深度与语义预测经过校准，修改后布局或透明遮挡需再测。

**可复用机制** · 用二维地图定位时，可匹配射线概率分布并按不确定性降权，减少遮挡导致的虚假几何约束。见表 4。

<a id="paper-mta-intermediate-alignment-for-joint-perception-captioning"></a>

## MTA: Multimodal Task Alignment for BEV Perception and Captioning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Ma_MTA_Multimodal_Task_Alignment_for_BEV_Perception_and_Captioning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Ma_MTA_Multimodal_Task_Alignment_for_BEV_Perception_and_Captioning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 单独优化鸟瞰三维检测与物体描述会丢掉两项任务可共享的关系线索。
- **核心创新 / 方法** · 对齐鸟瞰场景语义与语言，通过跨模态目标补充检测输出，并比较在 Q-Former 不同层施加约束。
- **Baseline** · 以 TOD3Cap 为基础，分别加入 BLA、DCA，比较同一 Q-Former 的首层、中层和末层。
- **Benchmark** · TOD3Cap 的三维密集描述与 nuScenes 三维检测，报告 CIDEr、BLEU-4、NDS 与 mAP。
- **关键结果 / 消融** · 表 5 中层 CIDEr 为 111.9、mAP 为 27.7，首层为 111.2、27.3，末层为 107.7、27.1。
- **适用条件 / 局限** · 中层选择依赖桥接深度与感知模型，别的模态组合需要重新寻找对齐位置。

**可复用机制** · 让语言与三维感知共享信息时，可以在跨模态桥的不同深度挂对齐目标，分别检查感知与描述的变化。见表 4、5。

<a id="paper-geosam2-geometry-aware-prompted-part-segmentation"></a>

## GeoSAM2: Unleashing the Power of SAM2 for 3D Part Segmentation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Deng_GeoSAM2_Unleashing_the_Power_of_SAM2_for_3D_Part_Segmentation_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Deng_GeoSAM2_Unleashing_the_Power_of_SAM2_for_3D_Part_Segmentation_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 无纹理三维模型缺少自然图像线索，直接渲染后使用分割器难区分部件。
- **核心创新 / 方法** · 渲染法线与点图，用残差几何融合和低秩适配把几何引入共享 SAM2，再反投影多视角掩膜。
- **Baseline** · 与原始 SAM2 及去点图、去特征融合等版本对照。
- **Benchmark** · PartObjaverse-Tiny 与 PartNetE 的开放类别部件分割，以平均 IoU 衡量。
- **关键结果 / 消融** · 表 3 PartObjaverse-Tiny 原始 SAM2 为 62.59%，去点图的模型为 75.56%，完整模型为 84.06%。
- **适用条件 / 局限** · 依赖可渲染视角和已知几何；可见性稀疏、内部部件与不到位提示仍可能失败。

**可复用机制** · 把二维提示分割用到无纹理物体，可渲染不同几何视图，以残差适配复用分割先验，再回投到三维。见表 3。

<a id="paper-pseudo-time-masked-image-pretraining-for-video-sr"></a>

## Time Without Time: Pseudo-Temporal Representation for Space-Time Super-Resolution

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Choi_Time_Without_Time_Pseudo-Temporal_Representation_for_Space-Time_Super-Resolution_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Choi_Time_Without_Time_Pseudo-Temporal_Representation_for_Space-Time_Super-Resolution_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 时空超分依赖有高质量时空细节的训练视频，少量下游数据难以充分训练模型。
- **核心创新 / 方法** · 复制单图为多个伪时间帧，每帧遮盖不同像素区域，用超分骨干从互补观测恢复干净稠密输出。
- **Baseline** · 同一 Zooming、TMNet、RSTT 对照有无预训练，另消融预训练集与遮盖。
- **Benchmark** · Vimeo-90K 快速动作和 REDS 的不同微调样本比例，报告 PSNR、SSIM、LPIPS。
- **关键结果 / 消融** · 表 1 在 1% Vimeo-90K 上 TMNet 从 28.91 到 34.79 dB，RSTT 从 31.66 到 34.18 dB；REDS 全量时 TMNet 从 26.56 到 26.93。
- **适用条件 / 局限** · 静态伪序列无法提供真实位移规律，仍需真实动态数据微调，完整下游数据时收益有限。

**可复用机制** · 缺少视频标注时，可把一张图变成互补缺失的伪时序预训练输入，尤其检查低数据微调是否改善。见表 1。

<a id="paper-unsafe2safe-privacy-utility-edit-evaluation"></a>

## Unsafe2Safe: Controllable Image Anonymization for Downstream Utility

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Dinh_Unsafe2Safe_Controllable_Image_Anonymization_for_Downstream_Utility_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Dinh_Unsafe2Safe_Controllable_Image_Anonymization_for_Downstream_Utility_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 删掉所有含个体线索的图像会损害数据覆盖，全面改写又可能破坏任务所需语义。
- **核心创新 / 方法** · 把包含与不包含敏感属性的描述分开，用中性的编辑条件修改隐私相关区域，并检查剩余可识别性。
- **Baseline** · 比较原图、不同提示条件，以及 DeepPrivacy2、FaceAnonSimple。
- **Benchmark** · Caltech101、室内图像分类、MS-COCO 描述与 OK-VQA，测下游分数与身份、文本隐私代理。
- **关键结果 / 消融** · 表 3 的 Caltech101 中，cedit 设置分类为 94.792%、FaceSim 0.3658；原图为 94.277%、1.0000。同配置室内分类从 83.881% 降至 77.090%。
- **适用条件 / 局限** · 代理分数无法保证匿名，漏识别区域与无脸身份线索需要另行审核。

**可复用机制** · 训练图像匿名化可只编辑敏感区域，并以模型效用和身份残留分别对比不同文本条件。见表 3。

<a id="paper-gaussianvision"></a>

## GaussianVision: Vision-Language Alignment from Compressed Image Representations using 2D Gaussian Splatting

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Omri_GaussianVision_Vision-Language_Alignment_from_Compressed_Image_Representations_using_2D_Gaussian_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Omri_GaussianVision_Vision-Language_Alignment_from_Compressed_Image_Representations_using_2D_Gaussian_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 传输完整 RGB 和编码密集图块对端侧带宽与注意力都有开销。
- **核心创新 / 方法** · 将图像拟合为2D高斯，冻结既有 RGB Transformer，用专用输入层及 resampler 适配图文对齐。
- **Baseline** · 表1比较 RGB 与高斯表示，正文对照已有高斯拟合实现和图文适配。
- **Benchmark** · 比较压缩比、加载解码速度及图文表征表现。
- **关键结果 / 消融** · 作者报告拟合相比已有实现快90倍以上，适配训练约9.7–13.8%参数。
- **适用条件 / 局限** · 仍有拟合和抽样成本，预算应端到端核算，文字与小目标的损失需单测。

**可复用机制** · 视觉输入压缩可从空间自适应表示直接接到跨模态骨干，并对照解码回像素的成本。

<a id="paper-test-time-3d-priors"></a>

## Learning 3D Reconstruction with Priors in Test Time

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhou_Learning_3D_Reconstruction_with_Priors_in_Test_Time_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhou_Learning_3D_Reconstruction_with_Priors_in_Test_Time_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 预训练图像重建器通常无法直接接收不同形式先验。
- **核心创新 / 方法** · 在推理优化多视渲染一致性，并对已有信息加入对应输出的惩罚项。
- **Baseline** · 表1–4比较图像基座与先验感知网络。
- **Benchmark** · ETH3D、DTU、7-Scenes、NRGBD，点图与相机估计。
- **关键结果 / 消融** · 作者报告在 ETH3D、7-Scenes、NRGBD 点图距离误差较仅图像基线减半以上。
- **适用条件 / 局限** · 按实例优化增加延迟，错误先验或重复纹理可能使优化收敛到错误解。

**可复用机制** · 相机姿态、内参和深度不规则可用时，将它们转为输出约束，避免为每种输入组合重训。

<a id="paper-fedfip"></a>

## Domain Sensitive Federated Learning with Fisher-Informed Pruning

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Lin_Domain_Sensitive_Federated_Learning_with_Fisher-Informed_Pruning_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Lin_Domain_Sensitive_Federated_Learning_with_Fisher-Informed_Pruning_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 统一掩码忽略客户端内部多域，独立掩码又会降低可聚合性。
- **核心创新 / 方法** · 用分域 Fisher 估重要性，聚合共享掩码，客户端重激活域特异通道并使用域原型正则。
- **Baseline** · 表1比较联邦方法，表2–3消融 Fisher 裁剪和正则等。
- **Benchmark** · Digits、Office-Caltech、PACS 的平均 Top-1 与离散性。
- **关键结果 / 消融** · 表1跨三数据集对照，表2–3区分各模块作用。
- **适用条件 / 局限** · 需要可区分的域信号，域稀少时 Fisher 估计和跨端聚合应做稳健性检验。

**可复用机制** · 联邦模型需要结构对齐又有域偏差时，共享稀疏核心并允许客户端恢复少数域特异通道。

<a id="paper-egoxtreme-pose-evaluation"></a>

## EgoXtreme: A Dataset for Robust Object Pose Estimation in Egocentric Views under Extreme Conditions

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yoon_EgoXtreme_A_Dataset_for_Robust_Object_Pose_Estimation_in_Egocentric_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yoon_EgoXtreme_A_Dataset_for_Robust_Object_Pose_Estimation_in_Egocentric_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 常规位姿基准难体现极端第一视角视觉歧义。
- **核心创新 / 方法** · 采集第一视角6D位姿并在不同扰动条件下评测，同基座测试预处理。
- **Baseline** · 表3比较多种可泛化姿态估计器，表4对 Pi 系方法做预处理条件比较。
- **Benchmark** · 第一视角极端条件，ADD(S) 在0.1d、0.2d、0.3d 的召回。
- **关键结果 / 消融** · 作者报告常规泛化能力在极端条件下不能保持，表4将预处理和位姿指标连接。
- **适用条件 / 局限** · 不同情境中多种扰动可能共现，未独立控制的效应需要进一步实验。

**可复用机制** · 可穿戴位姿评估按光照、模糊和遮挡分层，检查预处理能否真正改善下游位姿。

<a id="paper-pavas-physical-video-audio"></a>

## PAVAS: Physics-Aware Video-to-Audio Synthesis

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Hyun-Bin_PAVAS_Physics-Aware_Video-to-Audio_Synthesis_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Hyun-Bin_PAVAS_Physics-Aware_Video-to-Audio_Synthesis_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 外观相关性能拟合声音风格，但不能保证视频物理状态改变时声音随之变化。
- **核心创新 / 方法** · 以估计的质量和三维轨迹导出物理条件，经适配器输入音频扩散模型。
- **Baseline** · 表1比较既有视频生音频方法，表3消融适配及物理特征。
- **Benchmark** · VGGSound、人评和 VGG-Impact 的物理声学一致性 APCC。
- **关键结果 / 消融** · 表2用27参与者的人评补充自动指标，表3分解物理条件贡献。
- **适用条件 / 局限** · 质量和轨迹来自估计，材质、接触和不可见声源会削弱物理条件的解释力。

**可复用机制** · 视频到音频生成可加入物体级物理条件，并用声学物理一致性与同步指标分别验收。

<a id="paper-amr-skeleton"></a>

## Exploring Adaptive Masked Reconstruction for Self-Supervised Skeleton-Based Action Recognition

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Sun_Exploring_Adaptive_Masked_Reconstruction_for_Self-Supervised_Skeleton-Based_Action_Recognition_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Sun_Exploring_Adaptive_Masked_Reconstruction_for_Self-Supervised_Skeleton-Based_Action_Recognition_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 重建大量骨架时空块训练慢，等权重点又会落在静态片段。
- **核心创新 / 方法** · 解耦编码和重建块尺寸，自适应标出每个块中有动作信息的位置。
- **Baseline** · 表1–4比较此前掩码骨架重建方法，含线性与其他训练协议。
- **Benchmark** · NTU 和 PKU-II 等动作识别，线性、微调及半监督结果。
- **关键结果 / 消融** · 正文比较重建训练效率与识别结果，并评估大块及引导组件。
- **适用条件 / 局限** · 运动幅度代理可能漏掉关键的微动作或静态姿态，其他传感器需校准选择规则。

**可复用机制** · 自监督重建可用更大输出块加速，再以运动信息聚焦解码监督。

<a id="paper-optimusvla-dual-memory"></a>

## Global Prior Meets Local Consistency: Dual-Memory Augmented Vision-Language-Action Model for Efficient Robotic Manipulation

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Global_Prior_Meets_Local_Consistency_Dual-Memory_Augmented_Vision-Language-Action_Model_for_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Global_Prior_Meets_Local_Consistency_Dual-Memory_Augmented_Vision-Language-Action_Model_for_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 各向同性初噪距真实动作远，单帧条件也看不到任务进展。
- **核心创新 / 方法** · 全局记忆检索类似轨迹并替代高斯初始化，局部记忆编码已执行序列以控制连续性。
- **Baseline** · 比较表1–3的现有 VLA，并检查动作生成配置。
- **Benchmark** · LIBERO、CALVIN、RoboTwin 2.0，比较操作成功率与生成函数评估开销。
- **关键结果 / 消融** · 三基准报告成功率和效率，在 RoboTwin Hard 以100次执行评估。
- **适用条件 / 局限** · 库中近邻不一定可行；环境变化和历史错误需要防止错误动作先验。

**可复用机制** · 将相似任务轨迹检索为动作生成先验，再用已执行动作约束当前生成。

<a id="paper-3d-ide-privileged-geometry"></a>

## 3D-IDE: 3D Implicit Depth Emergent

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_3D-IDE_3D_Implicit_Depth_Emergent_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_3D-IDE_3D_Implicit_Depth_Emergent_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 显式深度和位姿增加部署依赖，接入额外模型也会影响延迟。
- **核心创新 / 方法** · 使用局部几何验证和全局表征约束训练视觉特征，使空间信息从统一表示可读。
- **Baseline** · 比较需要显式三维输入的专用或通用方法，以及无几何训练骨干。
- **Benchmark** · 室内三维场景理解，表1去掉推理时几何，表2–3比较任务和组件。
- **关键结果 / 消融** · 原文报告只用二维推理的任务改善与去模块对照。
- **适用条件 / 局限** · 特权监督覆盖决定可迁移范围，单视图歧义不会被训练完全消除。

**可复用机制** · 视觉语言模型需要空间理解时，可在训练提供几何特权信息，而部署只读二维观察。

<a id="paper-corim-conflict-risk-fusion"></a>

## CoRiM: Conflict-driven Risk Minimization for Dynamic Multimodal Fusion

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zou_CoRiM_Conflict-driven_Risk_Minimization_for_Dynamic_Multimodal_Fusion_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zou_CoRiM_Conflict-driven_Risk_Minimization_for_Dynamic_Multimodal_Fusion_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 只按各路置信或损失加权可能忽略高置信但互相矛盾的模态。
- **核心创新 / 方法** · 定义融合冲突风险，在概率单纯形用无投影 Frank-Wolfe 优化权重。
- **Baseline** · 和已有动态多模态融合及单路/均匀融合方法对照。
- **Benchmark** · MVSA、NYUD 等，比较平均及最差分类准确率。
- **关键结果 / 消融** · 表1–2报告融合平均和最差准确率，正文分析目标平滑性及收敛。
- **适用条件 / 局限** · 收敛不等于全局最优；预测分布失校准或所有模态同时错误会损害融合。

**可复用机制** · 按样本动态融合时权重应同时反映预测分布冲突及不确定性。

<a id="paper-sculpt4d-sparse-time-mask"></a>

## Sculpt4D: Generating 4D Shapes via Sparse-Attention Diffusion Transformers

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yin_Sculpt4D_Generating_4D_Shapes_via_Sparse-Attention_Diffusion_Transformers_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yin_Sculpt4D_Generating_4D_Shapes_via_Sparse-Attention_Diffusion_Transformers_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 全时序注意力昂贵，过度裁剪又易丢身份或动作连贯性。
- **核心创新 / 方法** · 由静态三维 DiT 扩展为动态生成，按首帧锚定和时间稀疏块分配注意力。
- **Baseline** · 已有四维生成方法及去掉时序稀疏结构的对照。
- **Benchmark** · 四维对象序列，比较形状质量、时间一致性及计算量。
- **关键结果 / 消融** · 原文报告总计算减少56%，并以表2对照稀疏设计。
- **适用条件 / 局限** · 首帧不是总能提供后续部件信息，周期和突变运动的稀疏规则须另测。

**可复用机制** · 动态对象生成可同时保留首帧身份锚点和随时间衰减的局部上下文。

<a id="paper-fedara-anchor-rank-adaptation"></a>

## FedARA: Resource-adaptive Low-rank Personalized Federated Learning via Anchor-driven Representation Alignment on Heterogeneous Edge Devices

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_FedARA_Resource-adaptive_Low-rank_Personalized_Federated_Learning_via_Anchor-driven_Representation_Alignment_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_FedARA_Resource-adaptive_Low-rank_Personalized_Federated_Learning_via_Anchor-driven_Representation_Alignment_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 统一提取器忽略端侧预算，非独立同分布又会使模型表征偏离。
- **核心创新 / 方法** · 对共享提取器分解后按设备预算选秩，用锚一致性训练聚合后的表示。
- **Baseline** · 对照个性化联邦学习及异构模型配置。
- **Benchmark** · CIFAR-10、CIFAR-100，分别比较数据异构和模型异构的客户端准确率。
- **关键结果 / 消融** · 表1–3覆盖两种异构性及相应训练结果。
- **适用条件 / 局限** · 需要代表性锚点和可兼容层结构；不代表额外隐私保证。

**可复用机制** · 异构设备共同训练时，让不同客户端选低秩容量，以公共锚表征对齐不同子模型。

<a id="paper-whispernet-receiver-centric-budget"></a>

## WhisperNet: A Scalable Solution for Bandwidth-Efficient Collaboration

[官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_WhisperNet_A_Scalable_Solution_for_Bandwidth-Efficient_Collaboration_CVPR_2026_paper.html) · [官方正文](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_WhisperNet_A_Scalable_Solution_for_Bandwidth-Efficient_Collaboration_CVPR_2026_paper.pdf)

- **问题 / 瓶颈** · 固定码率和逐发送端区域选择可能重复发送同类内容，遗漏全局上下文。
- **核心创新 / 方法** · 发送显著性摘要，由接收者按预算选信息块，再进行对齐和融合。
- **Baseline** · 对比协同感知压缩与稀疏传输方法，测试作为插件的已有骨干。
- **Benchmark** · OPV2V，测 AP@0.7、带宽及定位噪声下表现。
- **关键结果 / 消融** · 作者报告使用0.5%通信成本时 AP@0.7 改善2.4%，并测试5%带宽配置。
- **适用条件 / 局限** · 需往返通信且摘要可信，链路延迟与异步传输可能削弱收益。

**可复用机制** · 多智能体共享观察时，由接收者看低带宽摘要再全局分配请求，而非各发送端彼此独立筛选。
