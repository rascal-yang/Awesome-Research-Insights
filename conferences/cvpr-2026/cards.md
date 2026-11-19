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
