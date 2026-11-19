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
