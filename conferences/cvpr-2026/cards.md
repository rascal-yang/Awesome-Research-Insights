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
