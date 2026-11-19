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
