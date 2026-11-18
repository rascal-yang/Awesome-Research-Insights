# NeurIPS 2026 论文卡 8

[会议索引](README.md)

<a id="paper-155332"></a>

## Linear Regression Under Misalignment: Algorithms and Theoretical Results

[官方论文页](https://neurips.cc/virtual/2026/poster/155332) · [作者来源](https://openreview.net/forum?id=6Q1b0lxekb)

- **问题 / 瓶颈** · 两种数据错位的求解复杂度不同。
- **核心创新 / 方法** · 以预测次序改变的超平面划分区域，固定维数时遍历区域代替枚举所有配对。
- **Baseline** · 高维近似方案和一维精确算法。
- **Benchmark** · 固定特征维数的复杂度分析。
- **关键结果 / 消融** · 整行错位可精确多项式求解；内部错位在二维已 NP-hard。
- **适用条件 / 局限** · 多项式次数随特征维数增长；限于所定义问题。

**可复用机制** · 搜索组合前识别会改变排序的几何边界，以区域共享最优离散配对。

<a id="paper-148416"></a>

## Linear-time rule mining under formal guarantees

[官方论文页](https://neurips.cc/virtual/2026/poster/148416) · [作者来源](https://openreview.net/forum?id=xyPT9RQdve)

- **问题 / 瓶颈** · 逻辑理论靠手写昂贵，通用规则学习也难扩展。
- **核心创新 / 方法** · 挖关系数据的重复模式，用组合精度与召回的效用评估候选。
- **Baseline** · 先进神经规则学习。
- **Benchmark** · 多种关系逻辑任务；预测和运行成本。
- **关键结果 / 消融** · 摘要报告 CPU 时间常小于 GPU 对照的 1%，部分任务更准确。
- **适用条件 / 局限** · 依赖能高效提取的模式族及具体效用定义。

**可复用机制** · 把候选规则搜集和廉价可证排序拆开，避免每次扩展都拟合大模型。

<a id="paper-154523"></a>

## LINE: LLM-based Iterative Neuron Explanations for Vision Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154523) · [作者来源](https://openreview.net/forum?id=Cyqy5Yh0Ho)

- **问题 / 瓶颈** · 固定词表遗漏概念，也可能产生过度具体描述。
- **核心创新 / 方法** · 用模型生成概念和图像，根据黑盒激活历史逐步修改。
- **Baseline** · 固定概念表和依赖梯度的激活最大化。
- **Benchmark** · ImageNet、Places365，多种模型；AUC 和新概念。
- **关键结果 / 消融** · AUC 分别最多改善 0.11 和 0.05，平均发现约 27% 词表外概念。
- **适用条件 / 局限** · 生成器偏置可能限制实际覆盖；相关激活不是因果。

**可复用机制** · 让解释候选通过主动激活探测反复更新，并保留搜索轨迹。

<a id="paper-152183"></a>

## Linguistic Trajectory Encoding for Efficient Long-Horizon Spatial Memory in Embodied Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/152183) · [作者来源](https://openreview.net/forum?id=UwaYppr2E8)

- **问题 / 瓶颈** · 视频级嵌入丢细运动，纯坐标难用语言查询。
- **核心创新 / 方法** · 按运动复杂度保留几何路点、视觉和描述；超出可靠观察时锚定最后位置。
- **Baseline** · 结构记忆、视觉语言模型及 EgoVLPv2。
- **Benchmark** · Spatial Memory Benchmark 与 Ego4D；检索、压缩、延迟。
- **关键结果 / 消融** · 两项 SMB 成功率 45.3%、48.7%，轨迹压缩 8.7 至 26.1 倍。
- **适用条件 / 局限** · 最后观测不等于当前位置；依赖追踪可靠。

**可复用机制** · 在对象级保留可问的状态变化，压缩时显式标识未观测时间段。

<a id="paper-152490"></a>

## LINK: Learning to Localize from Known to Unknown Scenes

[官方论文页](https://neurips.cc/virtual/2026/poster/152490) · [作者来源](https://openreview.net/forum?id=SjJBWDFaTv)

- **问题 / 瓶颈** · 坐标回归遇到无训练覆盖的道路性能骤降。
- **核心创新 / 方法** · 估计连续位姿可靠性，在可信历史定位上拼接相对运动，重新可见时用绝对假设。
- **Baseline** · 直接场景坐标回归及无地图定位。
- **Benchmark** · UrbanUnseen、Oxford、NCLT 的部分覆盖。
- **关键结果 / 消融** · 摘要报告覆盖不全时改善，同时保留已知场景表现。
- **适用条件 / 局限** · 长不可见段存在相对漂移，需校验切换。

**可复用机制** · 将观测置信用于模式选择，保留最近可信绝对参考并控制传播范围。

<a id="paper-149286"></a>

## LIPAR: Latent Inter-Frame Pruning with Attention Recovery

[官方论文页](https://neurips.cc/virtual/2026/poster/149286) · [作者来源](https://openreview.net/forum?id=rREHWFZNpH)

- **问题 / 瓶颈** · 跨帧潜图块冗余高，直接删掉易出现伪影。
- **核心创新 / 方法** · 检测重复后不重算，并近似恢复被剪词元的注意值。
- **Baseline** · 原始扩散和朴素剪枝。
- **Benchmark** · A6000 上的视频吞吐和质量。
- **关键结果 / 消融** · 从 8.4 FPS 至 12.2 FPS，摘要报告质量保留。
- **适用条件 / 局限** · 高速变化削弱可剪机会，恢复开销潜在变化。

**可复用机制** · 快速路径可省去冗余状态更新，但应保留这些状态对应的信息聚合。

<a id="paper-153450"></a>

## Lipschitz Dueling Bandits over Continuous Action Spaces

[官方论文页](https://neurips.cc/virtual/2026/poster/153450) · [作者来源](https://openreview.net/forum?id=LCU19fa0gS)

- **问题 / 瓶颈** · 无直接奖励下难以定位高价值区域。
- **核心创新 / 方法** · 以自适应参考臂分轮比较并递归排除区域。
- **Baseline** · 传统决斗和 Lipschitz bandit 问题设定。
- **Benchmark** · 连续动作 Lipschitz 决斗理论，累计遗憾与内存。
- **关键结果 / 消融** · 遗憾随近最优区维数变化，空间对时域为对数级。
- **适用条件 / 局限** · 要求相对反馈与连续度量满足论文条件。

**可复用机制** · 用临时参考点让不同区域的局部成对观测可比较。

<a id="paper-152273"></a>

## LiSA: Lifelong Safety Adaptation via Conservative Policy Induction

[官方论文页](https://neurips.cc/virtual/2026/poster/152273) · [作者来源](https://openreview.net/forum?id=UJDUd0ySXi)

- **问题 / 瓶颈** · 零散噪声反馈难以频繁微调且容易过度推广。
- **核心创新 / 方法** · 把失败归纳为政策记忆，用冲突感知局部规则和后验下界门控。
- **Baseline** · 强记忆基线和扩大基座。
- **Benchmark** · PrivacyLens+、ConFaide+、AgentHarm；稀疏或有噪反馈。
- **关键结果 / 消融** · 摘要报告到 20% 标签翻转仍有稳健改善。
- **适用条件 / 局限** · 依赖反馈具有一定可辨别性，需治理错误规则的移除。

**可复用机制** · 高风险场景对新例证使用保守置信下界，优先让局部例外覆盖宽泛规则。

<a id="paper-148774"></a>

## Listening to the Retriever: Perturbation-Sensitive Question Selection for Interactive Person Retrieval

[官方论文页](https://neurips.cc/virtual/2026/poster/148774) · [作者来源](https://openreview.net/forum?id=vA4uJHyY6W)

- **问题 / 瓶颈** · 外部问句打分可能不反映检索器真正需要的信息。
- **核心创新 / 方法** · 对属性描述做测试时扰动，以结果排名变化评估追问价值。
- **Baseline** · 外部信号的交互检索与现成图文检索器。
- **Benchmark** · 三项交互检索基准，细项待核实。
- **关键结果 / 消融** · 摘要报告一致增益且无需训练。
- **适用条件 / 局限** · 排名敏感不必然等于有效信息，需在人群和同意边界内验证。

**可复用机制** · 让下游计算对输入变化的响应决定该问什么，而不是依赖与系统无关的先验。

<a id="paper-151680"></a>

## Listening to the Wise Few: Query–Key Alignment Unlocks Latent Correct Answers in Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151680) · [作者来源](https://openreview.net/forum?id=YosIUonuQI)

- **问题 / 瓶颈** · 最终错答仍可能保留正确选项表示。
- **核心创新 / 方法** · 以去旋转位置编码前的注意查询键对齐探测中层选项，再以无标签打分选头。
- **Baseline** · 模型自身零样本及四种位置去偏方式。
- **Benchmark** · 24 个模型，HellaSwag、HaluDialogue 等四项。
- **关键结果 / 消融** · 单头最高相对原输出提升 27.4、49.8 个百分点；消融后接近随机。
- **适用条件 / 局限** · 中心机制证据限于测试模型和多选结构。

**可复用机制** · 诊断时区分选择语义和标签写出，避免用输出校正解释内部语义失败。

<a id="paper-139142"></a>

## ListQA: A Benchmark for Evaluating List-Formatted Factual Knowledge Retrieval in Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139142) · [作者来源](https://openreview.net/forum?id=iRiQtK97gj)

- **问题 / 瓶颈** · 单事实评分或逐序比较无法评价无序列表。
- **核心创新 / 方法** · 以二分图最优匹配配对元素，再做语义核验，并用提供来源页作定位对照。
- **Baseline** · 无检索与提供真实来源页，标准和思考推理。
- **Benchmark** · ListQA 9,045 问题、34 个模型和 42 配置。
- **关键结果 / 消融** · 最佳标准推理低于 37% 评审 F1，给来源页后大幅改善。
- **适用条件 / 局限** · 匹配依赖语义裁判准确，来源页设置偏理想。

**可复用机制** · 用外部真证据对照隔离参数召回瓶颈，再单独评分列表组织能力。

<a id="paper-153692"></a>

## Listwise Policy Optimization: Group-based RLVR as Target-Projection on the LLM Response Simplex

[官方论文页](https://neurips.cc/virtual/2026/poster/153692) · [作者来源](https://openreview.net/forum?id=JUzdxqEbBC)

- **问题 / 瓶颈** · 隐式一阶更新不便比较不同目标和散度造成的差异。
- **核心创新 / 方法** · 在响应单纯形上求近端目标，再精确最小化到目标的散度。
- **Baseline** · 同样目标的典型策略梯度。
- **Benchmark** · 多推理任务与语言骨干，表现和响应多样性。
- **关键结果 / 消融** · 列表目标单调改善且梯度有界零和；摘要报告训练优于基线。
- **适用条件 / 局限** · 组采样不能覆盖所有输出，理论是列表目标。

**可复用机制** · 分开建模希望改变的组内概率与如何稳定更新策略。

<a id="paper-154582"></a>

## LITE: A Lightweight Lazy Sampler for Efficient SGD

[官方论文页](https://neurips.cc/virtual/2026/poster/154582) · [作者来源](https://openreview.net/forum?id=CVmeicsRSC)

- **问题 / 瓶颈** · 代理计算、分数陈旧与采样过度集中抵消方差收益。
- **核心创新 / 方法** · 周期更新廉价分数，以平滑和温度规则控制分布。
- **Baseline** · 均匀采样和标准重要性采样。
- **Benchmark** · 视觉、文本、三维；等更新量与真实总耗时。
- **关键结果 / 消融** · 摘要报告总体持平或更好，预算紧和失衡时增益最清楚。
- **适用条件 / 局限** · 取决于代理质量和漂移；不要只比较更新步数。

**可复用机制** · 把代理维护成本计入收益，并随可靠性降低主动缩小重加权。

<a id="paper-148879"></a>

## Literati: Towards Anytime Optimal Shape Generalized Trees via AO*

[官方论文页](https://neurips.cc/virtual/2026/poster/148879) · [作者来源](https://openreview.net/forum?id=uUYZFj5qPL)

- **问题 / 瓶颈** · 单阈值切分通常要深树表达非线性，贪心广义树又无全局保证。
- **核心创新 / 方法** · 以 AND/OR 图编码树结构及单变量形函数复杂度，用 AO* 改善随时可用性。
- **Baseline** · 现有贪心及最优树方法。
- **Benchmark** · 24 个真实表格集，训练和测试准确。
- **关键结果 / 消融** · 摘要报告更高准确且保留最优性。
- **适用条件 / 局限** · 搜索复杂度与形函数候选增长有关。

**可复用机制** · 在需要可说明决策的任务，将单节点表达能力和整树复杂度一起纳入搜索。

<a id="paper-151492"></a>

## LITHE: Lattice-Indexed Twin Hadamard Encoding for Diffusion Personalization

[官方论文页](https://neurips.cc/virtual/2026/poster/151492) · [作者来源](https://openreview.net/forum?id=aFYphrxbNI)

- **问题 / 瓶颈** · 常驻适配器数量受限，压缩格式未必支持快速异构批。
- **核心创新 / 方法** · 用确定性 Hadamard 码本存索引，可直接路由异构批，也可解码后编译。
- **Baseline** · 优化 LoRA+compile 与匹配秩原适配器。
- **Benchmark** · FLUX.1-dev、80 GB A100；常驻数量、延迟及磁盘。
- **关键结果 / 消融** · 报告同卡容纳 10,000 适配器，1024² 的编译模式距基线 1% 内。
- **适用条件 / 局限** · 质量与吞吐需在不同适配器及实际混合流量下复核。

**可复用机制** · 编码与服务路径共同设计，让压缩格式支持冷启动和高吞吐两种形态。

<a id="paper-150415"></a>

## LITMUS: Benchmarking Behavioral Jailbreaks of LLM Agents in Real OS Environments

[官方论文页](https://neurips.cc/virtual/2026/poster/150415) · [作者来源](https://openreview.net/forum?id=iCXoa3VMy0)

- **问题 / 瓶颈** · 只读对话可能漏掉已经发生的副作用。
- **核心创新 / 方法** · 对语义输出和系统状态独立判分，并通过隔离及恢复状态让测试相互独立。
- **Baseline** · 仅语义判分和没有状态隔离的评估。
- **Benchmark** · 819 个高风险场景及多个代理，测拒绝表述与实际状态的一致性。
- **关键结果 / 消融** · 观察到拒绝表述和已发生副作用不一致，语义评估无法发现这类错误。
- **适用条件 / 局限** · 结果依赖受控系统、动作权限和状态观测覆盖。

**可复用机制** · 助手即使声称拒绝，也应由独立校验器确认受保护资源未改变。

<a id="paper-148220"></a>

## LittleLearner: Language Models Under Pedagogically-Controlled Knowledge Exposure

[官方论文页](https://neurips.cc/virtual/2026/poster/148220) · [作者来源](https://openreview.net/forum?id=zSwgtp9S5a)

- **问题 / 瓶颈** · 常规网页语料难断定模型是否见过相关概念。
- **核心创新 / 方法** · 按课程清理并限定预训练暴露，再比较后训练和上下文示例对范围内外任务的作用。
- **Baseline** · 有无后训练及上下文学习的受控比较。
- **Benchmark** · 88B token 的小学课程语料、2B 模型，测边界内外能力。
- **关键结果 / 消融** · 摘要报告更善于利用已有知识，未见范围外能力提升。
- **适用条件 / 局限** · 课程是暴露代理，需检查残余泄漏及范围外干预的强度。

**可复用机制** · 把已见知识的调用与真正新能力分开评估，并记录预训练覆盖边界。

<a id="paper-139208"></a>

## LL-Bench: Rethinking Low-Level Vision Evaluation in the Era of Large-Scale Generative Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139208) · [作者来源](https://openreview.net/forum?id=eb9dtoJupA)

- **问题 / 瓶颈** · 常用指标可能偏爱清晰但捏造细节的复原。
- **核心创新 / 方法** · 用真实退化及多方法输出收集偏好与评分，并训练同时预测复原质量和幻觉的 LL-Score。
- **Baseline** · 传统复原与大型生成模型，现有图像质量指标。
- **Benchmark** · 2,469 张退化图、16 类任务、28,919 张复原图和 152,020 个偏好标注。
- **关键结果 / 消融** · 作者报告现有指标与人评存在偏差，新指标更贴合人评并可用于奖励。
- **适用条件 / 局限** · 对不同退化、标注者和开放复原场景迁移待核实。

**可复用机制** · 先分开标注细节真假与观感，再比较复原质量度量的误差来源。

<a id="paper-155346"></a>

## LLM-ACES: Closed-Loop Discovery of Dynamic Systems with LLM-Guided Adaptive Search

[官方论文页](https://neurips.cc/virtual/2026/poster/155346) · [作者来源](https://openreview.net/forum?id=6JC2w2LT7i)

- **问题 / 瓶颈** · 固定轨迹无法区分局部近似相同的方程。
- **核心创新 / 方法** · 以语言先验生成候选式，主动查询分歧区域，再用新轨迹更新候选。
- **Baseline** · 已有方程发现方法及闭环组件消融。
- **Benchmark** · 受限仿真预算的动力学恢复，衡量方程正确性。
- **关键结果 / 消融** · 摘要报告恢复优于对照，消融显示候选构建与主动采样耦合有益。
- **适用条件 / 局限** · 依赖可查询系统和至少一组足够合理的候选，噪声及访问成本待查。

**可复用机制** · 用候选模型的预测分歧决定实验位置，检验有限采样能否减少不可区分假设。

<a id="paper-148531"></a>

## LLM Agents Already Know When to Call Tools - Even Without Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/148531) · [作者来源](https://openreview.net/forum?id=xCTlbKHWcR)

- **问题 / 瓶颈** · 只用提示可能连必要调用也抑制，自述理由不能可靠选择工具。
- **核心创新 / 方法** · 训练轻量线性探针读生成前隐藏态，以预填提示改变是否调用。
- **Baseline** · 提示抑制及先推理后行动。
- **Benchmark** · When2Tool 十八环境、六个模型和 Search-o1；AUROC、调用次数、准确率。
- **关键结果 / 消融** · 探针 AUROC 0.89–0.96；调用减少 48% 且准确率仅降 1.7%，Search-o1 调用减少 20–56% 且无准确率下降。
- **适用条件 / 局限** · 需访问模型隐藏态，阈值跨任务、工具与预算需复核。

**可复用机制** · 以漏掉必要调用的代价校准门控，而不是只追求调用率最低。

<a id="paper-149683"></a>

## LLM Alignment--Utility Asymmetry under Semantic-Preserving Transformations

[官方论文页](https://neurips.cc/virtual/2026/poster/149683) · [作者来源](https://openreview.net/forum?id=oD12yQB5qg)

- **问题 / 瓶颈** · 任务还能正确处理并不代表防护随语义迁移。
- **核心创新 / 方法** · 在语义保持的改变及相同任务条件下独立测任务与安全指标。
- **Baseline** · 原输入及微调、上下文适配设置。
- **Benchmark** · 四种开权重及四种商业模型，测任务效用和安全违规。
- **关键结果 / 消融** · 摘要报告多个场景中效用下降有限，但安全失败显著增加。
- **适用条件 / 局限** · 结果依赖所测分布变化和模型，未提供一般保证。

**可复用机制** · 只有在效用仍达标时，另测安全是否随输入表达变化而退化。

<a id="paper-150546"></a>

## LLM-as-a-Tutor: Policy-Aware Prompt Adaptation for Non-Verifiable RL

[官方论文页](https://neurips.cc/virtual/2026/poster/150546) · [作者来源](https://openreview.net/forum?id=hKGWL5CWJn)

- **问题 / 瓶颈** · 策略提高后固定题库难以为评委提供可区分的输出。
- **核心创新 / 方法** · 同一模型先比较 rollout 判断区分度，再为原提示追加原子约束。
- **Baseline** · 固定提示、适应量表及重写提示的方法。
- **Benchmark** · 三项复杂指令遵循基准；具体得分待核实。
- **关键结果 / 消融** · 摘要报告稳定优于非适应和已有适应对照。
- **适用条件 / 局限** · 追加后难度单调增长的经验条件和评委偏差待核实。

**可复用机制** · 用候选输出的可区分性反馈控制课程，保持题意主干稳定。

<a id="paper-151426"></a>

## LLM-Based Multi-Agent Blackboard System for Information Discovery in Data Science

[官方论文页](https://neurips.cc/virtual/2026/poster/151426) · [作者来源](https://openreview.net/forum?id=ao3zijumY7)

- **问题 / 瓶颈** · 中心预先指定合适专家依赖对能力和数据内容的完整观察。
- **核心创新 / 方法** · 中央发布请求，局部数据代理或外部检索代理按能力提供响应。
- **Baseline** · 单代理及强多代理数据发现方法。
- **Benchmark** · KramaBench、修改版 DSBench 和 DA-Code；端到端成功及数据检索 F1。
- **关键结果 / 消融** · 报告成功相对提升 13–57%，相对最强数据发现 F1 提升最高 9%。
- **适用条件 / 局限** · 广播、响应冲突和扩展成本待核实。

**可复用机制** · 比较中心指定和局部自荐的路由，在同一信息预算下测召回及消息负载。

<a id="paper-152529"></a>

## LLM Flow Processes for Text-Conditioned Regression

[官方论文页](https://neurips.cc/virtual/2026/poster/152529) · [作者来源](https://openreview.net/forum?id=ST546vOvbp)

- **问题 / 瓶颈** · 逐步语言回归慢而且累积误差，独立边缘预测又过宽。
- **核心创新 / 方法** · 用扩散神经过程耦合语言模型边缘，并以免梯度方式从乘积专家采样。
- **Baseline** · 逐步语言回归及并行独立边缘。
- **Benchmark** · 文本条件回归与时序轨迹，测校准和局部一致。
- **关键结果 / 消融** · 摘要报告更校准且轨迹局部一致，显示文本驱动函数空间选择。
- **适用条件 / 局限** · 采样方法要求至少一个专家可与高斯闭式卷积，其他情况待核实。

**可复用机制** · 分开让文本先验控制边缘，让学习过程捕捉时间耦合，并同时比较时延及联合一致性。

<a id="paper-154278"></a>

## LLM Judge Validation Under Sparse Overlap: From Inference to Design

[官方论文页](https://neurips.cc/virtual/2026/poster/154278) · [作者来源](https://openreview.net/forum?id=F1iuTzQaMM)

- **问题 / 瓶颈** · 标注总量大也不能弥补请求重叠太少导致的排序误差。
- **核心创新 / 方法** · 推导最小重叠阈值并按可区分层分配比较样本。
- **Baseline** · 随机分配重叠与不同重叠比例。
- **Benchmark** · 十个模型评委、四个评价矩阵，含视觉、因果及摘要，测部署错误与误拒。
- **关键结果 / 消融** · 5% 重叠时错误部署达 25%，十选一错误达 65%；有信息层可使误拒减半。
- **适用条件 / 局限** · 约 25% 的足量阈值针对非边界评委，边界情形及层信息需复核。

**可复用机制** · 采标前先按配对重叠和错误决策成本设计预算，而非只看标注总条数。

<a id="paper-149756"></a>

## LLM Rheology: Auditing Refusal Geometry in Aligned Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149756) · [作者来源](https://openreview.net/forum?id=nbLsmiH2tO)

- **问题 / 瓶颈** · 模型规模与可见拒绝未必反映拒绝机制的稳定。
- **核心创新 / 方法** · 以几何归一的分布响应审计拒绝信号，辅以方向特异性防护对照。
- **Baseline** · 未干预与匹配范数安慰剂。
- **Benchmark** · 六个开放模型家族、22 个检查点，测归一响应及安全与良性推理。
- **关键结果 / 消融** · 报告部分中等规模内部响应较弱，目标防护干预在测试子集恢复拒绝。
- **适用条件 / 局限** · 诊断代理与行为实效仍需扩大样本，不能外推所有模型。

**可复用机制** · 同时保留行为安全和机制诊断，并固定干预强度检查是否仅是总体扰动效应。

<a id="paper-151231"></a>

## LLMs as MDP Designers: A Dependency-Aware Agentic Framework for Automated Robot Policy Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/151231) · [作者来源](https://openreview.net/forum?id=bvhaE5w1Z4)

- **问题 / 瓶颈** · 模拟器能运行也可能因状态、动作、奖励或终止语义错配而无法训练。
- **核心创新 / 方法** · 先验收依赖式 MDP 规格，再在仿真环境独立审核其模块实现和训练表现。
- **Baseline** · 整体生成及普通代理方案。
- **Benchmark** · Isaac Sim 和几个扩展 MDP，检查建模、执行及训练成功。
- **关键结果 / 消融** · 摘要称三项均改善。
- **适用条件 / 局限** · 主要为仿真设计，真机部署与安全许可不在证据范围内。

**可复用机制** · 在无害仿真中逐项验证转移和奖励语义，避免把代码可运行当作训练验收。

<a id="paper-153045"></a>

## LLMs can construct powerful representations and streamline sample-efficient supervised learning

[官方论文页](https://neurips.cc/virtual/2026/poster/153045) · [作者来源](https://openreview.net/forum?id=OQzUaEnhcP)

- **问题 / 瓶颈** · 把原始记录转成文本仍难稳定提取信息。
- **核心创新 / 方法** · 模型从少量序列化样本总结全局规则，再将输入规范化；另比较任务局部规则。
- **Baseline** · 计数特征、普通语言模型、临床基础模型。
- **Benchmark** · EHRSHOT 15 项临床预测任务。
- **关键结果 / 消融** · 摘要报告规则方案优于所列参考。
- **适用条件 / 局限** · 医疗实证不等于临床有效；规则构造的偏差与复用广度待查。

**可复用机制** · 跨表格、文本与时间序列输入验证同一规则及下游性能。

<a id="paper-149675"></a>

## LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling

[官方论文页](https://neurips.cc/virtual/2026/poster/149675) · [作者来源](https://openreview.net/forum?id=oH6xObXkeJ)

- **问题 / 瓶颈** · 反复执行模型搜索启发式计算昂贵。
- **核心创新 / 方法** · 以预采集轨迹和探针信号提供离线表现反馈，在数学题上验证控制器质量。
- **Baseline** · 手工设定的推理计算分配。
- **Benchmark** · 数学推理、留出测试和模型规模变化，比较准确成本。
- **关键结果 / 消融** · 摘要称更优，发现总耗时 160 分钟、费用 39.9 美元。
- **适用条件 / 局限** · 轨迹重放覆盖限制可评价策略，部署成本需独立测。

**可复用机制** · 在受控数学任务比较离线重放分数与真实在线回报的相关性。

<a id="paper-154758"></a>

## LLMs Keep Thinking When Told Not To

[官方论文页](https://neurips.cc/virtual/2026/poster/154758) · [作者来源](https://openreview.net/forum?id=BBASLoS4xf)

- **问题 / 瓶颈** · 功能开关或提示不能可靠预测输出形态。
- **核心创新 / 方法** · 将答前文本和最终答案拆开，分别检查遵循与问题相关性。
- **Baseline** · 思考开关、指令及多个模型。
- **Benchmark** · 布尔、多选和开放题；测答前信息和正确性。
- **关键结果 / 消融** · 布尔易压缩，多选居中，开放难题压缩可能损准确率。
- **适用条件 / 局限** · 只研究可见输出，不能推断内部计算。

**可复用机制** · 以题型和答案空间分桶，单列格式成功和任务得分。

<a id="paper-153146"></a>

## LLMs Optimizing LLMs: Automated MegaKernel Generation for Inference Acceleration

[官方论文页](https://neurips.cc/virtual/2026/poster/153146) · [作者来源](https://openreview.net/forum?id=NYcBKCjBjb)

- **问题 / 瓶颈** · 现有大内核需为不同架构手工改写。
- **核心创新 / 方法** · 把融合拆为可控指令，逐层校验 CUDA 计算等价。
- **Baseline** · vLLM、SGLang、MPK。
- **Benchmark** · 稠密、MoE、VLA 和 NVIDIA Hopper、Ampere、Ada。
- **关键结果 / 消融** · 最高分别快 5.04、2.42、1.92 倍。
- **适用条件 / 局限** · 实现生成成本与其它后端需核。

**可复用机制** · 对比融合前后数值及速度，覆盖跨模型和硬件重新编译。

<a id="paper-148364"></a>

## LLMs Show No Signs Of Individuated Metacognition

[官方论文页](https://neurips.cc/virtual/2026/poster/148364) · [作者来源](https://openreview.net/forum?id=yPoH9lr0AD)

- **问题 / 瓶颈** · 总体校准可能只反映共同难度。
- **核心创新 / 方法** · 对 20 模型信心做四分相关因子分析和成对校准，控制共享难度维度。
- **Baseline** · 直接信心路由与基于可见特征的逻辑回归。
- **Benchmark** · 六个事实、检索和推理基准。
- **关键结果 / 消融** · 事实检索共享因子近秩一，去除共识后信心与模型间性能关系消失。
- **适用条件 / 局限** · 结论限口头置信度和所测领域。

**可复用机制** · 在路由验收中测试分歧集，并区分作答后信心与回答前预判。

<a id="paper-139824"></a>

## LLM-WikiRace: A Benchmark for Planning and Reasoning over Real-World Knowledge Graphs

[官方论文页](https://neurips.cc/virtual/2026/poster/139824) · [作者来源](https://openreview.net/forum?id=2dPdrZwYhb)

- **问题 / 瓶颈** · 知识充足时仍可能无法处理长程和失败重规划。
- **核心创新 / 方法** · 用真实链接图按目标难度评测逐步导航，分析轨迹重复。
- **Baseline** · 多种开闭源模型和人类。
- **Benchmark** · LLM-WikiRace 简单和困难设置，以成功率和轨迹分析。
- **关键结果 / 消融** · 最佳模型困难局仅 29%，强模型失败后常循环。
- **适用条件 / 局限** · 维基导航不是一般世界模型，性能受图路径覆盖影响。

**可复用机制** · 在同知识提示下加入可复现死路，比较恢复而非只记最终成功。

<a id="paper-150857"></a>

## Load Balancing Mixture of Experts with Similarity Preserving Routers

[官方论文页](https://neurips.cc/virtual/2026/poster/150857) · [作者来源](https://openreview.net/forum?id=eqAiBJ58gY)

- **问题 / 瓶颈** · 均匀利用压力可能让相似词元被不一致分配，早期专家重复。
- **核心创新 / 方法** · 负载目标加入相似输入选择一致性的约束。
- **Baseline** · 常用负载均衡损失。
- **Benchmark** · MoE 预训练，考察收敛及专家冗余。
- **关键结果 / 消融** · 摘要报告收敛快 36% 并减少冗余。
- **适用条件 / 局限** · 相似度定义、专家负载与其他规模待核。

**可复用机制** · 同时记录专家使用方差和相似输入路由一致性，确认负载均衡没破坏专门化。

<a id="paper-149786"></a>

## LocalAgent: Collaborative Agentic Verification for Fine-Grained Instance-Level Consistency

[官方论文页](https://neurips.cc/virtual/2026/poster/149786) · [作者来源](https://openreview.net/forum?id=nJtBeEwjzg)

- **问题 / 瓶颈** · 同类实物差别小，整体语义判断不足。
- **核心创新 / 方法** · 局部工具分别估计光照较稳的外观及多视角对应，供全局判决；训练工具调用时机。
- **Baseline** · 直接推理和闭源多模态模型。
- **Benchmark** · 视角、光照、背景变化下核验同一物体。
- **关键结果 / 消融** · 较直接推理平均提高 4.8%。
- **适用条件 / 局限** · 伪定位和工具错误会影响结论，耗时待核。

**可复用机制** · 以同图输入分别测试局部证据有无和结构化反馈有无。

<a id="paper-148228"></a>

## Local FDR Membership Inference Attacks: Multiple Testing and the Role of Ridge Regularization

[官方论文页](https://neurips.cc/virtual/2026/poster/148228) · [作者来源](https://openreview.net/forum?id=zR0MYMNUF1)

- **问题 / 瓶颈** · 单例误报率不能说明一批发现有多少错误。
- **核心创新 / 方法** · 比较正则强度对受控批量隐私审计的影响。
- **Baseline** · 单例误报校准和既有审计。
- **Benchmark** · 高维岭回归理论，含合成和一个真实数据集。
- **关键结果 / 消融** · 所分析设置中增大岭惩罚降低成员泄漏风险。
- **适用条件 / 局限** · 证据依赖特定模型和设计条件。

**可复用机制** · 用授权合成数据同时报告集合误报、模型效用和正则强度。

<a id="paper-149732"></a>

## Local Gaussian Processes on Compact Lie Groups

[官方论文页](https://neurips.cc/virtual/2026/poster/149732) · [作者来源](https://openreview.net/forum?id=nmziO0ZFUz)

- **问题 / 瓶颈** · 欧式距离不能表达旋转对称性。
- **核心创新 / 方法** · 将紧李群分解为极大环面和正交补，构造局部高斯核；对 SO(3) 和 SU(2) 给显式式。
- **Baseline** · 欧式核及普通回归路线。
- **Benchmark** · 紧群的核正定性实验和高斯过程回归。
- **关键结果 / 消融** · 摘要报告全流形预测准确及实验正定性验证。
- **适用条件 / 局限** · 任意群的可用核成本和极端邻域表现待核。

**可复用机制** · 比较等数据下欧式和群核在坐标接缝附近的预测方差。

<a id="paper-151172"></a>

## Local–Global Sparse Autoencoders for Multiscale Interpretability in Vision Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151172) · [作者来源](https://openreview.net/forum?id=cS2IkMjMnL)

- **问题 / 瓶颈** · 单一尺度解释看不到局部对整体的支持。
- **核心创新 / 方法** · LG-SAE 让跨尺度桥学习局部特征对全局特征的支持图。
- **Baseline** · 单尺度解释和概念瓶颈。
- **Benchmark** · 空间定位、预测表现与用户评估。
- **关键结果 / 消融** · 摘要称可定位并维持下游表现，用户验证解释可读。
- **适用条件 / 局限** · 稀疏概念并不保证唯一，稳定性待核。

**可复用机制** · 用局部遮盖验证组合支持边并检查全局概念变化。

<a id="paper-155658"></a>

## Local Guidance, Global Impact: Gaussian-Reshaped Trust Region Unlocks Behavior Transitions

[官方论文页](https://neurips.cc/virtual/2026/poster/155658) · [作者来源](https://openreview.net/forum?id=3yresnLxCf)

- **问题 / 瓶颈** · PPO 局部步骤可能长期方向无效。
- **核心创新 / 方法** · 用有界非单调高斯约束和近期策略混合锚点调整更新。
- **Baseline** · PPO 与单调散度惩罚。
- **Benchmark** · 游戏、模拟控制、探索与语言模型后训练。
- **关键结果 / 消融** · 摘要称多域表现强，未给数值。
- **适用条件 / 局限** · 非单调约束可能放过错误的大步，需监控稳定性。

**可复用机制** · 单列变化点后恢复速度和变化前性能，比较固定锚与近期混合。

<a id="paper-153830"></a>

## Local-Interaction Learning Dynamics: A Markov Random Field Framework for Convergence of Deep Neural Network Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/153830) · [作者来源](https://openreview.net/forum?id=IOtI8jFguP)

- **问题 / 瓶颈** · 完整曲率无法定位是哪层造成不稳定，形成大矩阵昂贵。
- **核心创新 / 方法** · 把参数和中间状态写成局部 Gibbs 系统，消去中间态得参数曲率，构造分隔证书。
- **Baseline** · 密集 Hessian 或 Fisher、纯参数几何。
- **Benchmark** · CIFAR-10、GPT-20M 上 FineWeb-Edu 的检查点。
- **关键结果 / 消融** · 摘要称可诊断学习率稳定、可塑性和泛化，无需形成密集矩阵。
- **适用条件 / 局限** · 证书条件、分解计算成本和广度待核。

**可复用机制** · 用局部模块替换和整数倍学习率核验诊断是否能定位不稳定来源。

<a id="paper-149038"></a>

## Local Intrinsic Dimension Unveils Hallucinations in Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149038) · [作者来源](https://openreview.net/forum?id=tJpnYYu4pi)

- **问题 / 瓶颈** · 训练统计下看似真实的图，可能违反部件或数量约束。
- **核心创新 / 方法** · 评估局部不稳定作为筛选，并测试降低局部内在维数的修正。
- **Baseline** · 时间型过滤以及已有异常降低方法。
- **Benchmark** · 多个图像生成评测；具体数据和约束待核。
- **关键结果 / 消融** · 作者称过滤匹配或超过对照，修正持续降低结构异常。
- **适用条件 / 局限** · 维数估计对噪声和生成阶段敏感，因果范围待核。

**可复用机制** · 分别用合成形状的部件数和视觉质量对照，避免减少多样性掩盖异常。

<a id="paper-152589"></a>

## Locality Sensitive Hashing for p-Exponential Kernels with Applications to Density Estimation

[官方论文页](https://neurips.cc/virtual/2026/poster/152589) · [作者来源](https://openreview.net/forum?id=RyF0cieapR)

- **问题 / 瓶颈** · 已有可哈希对应主要针对 p 等于 1。
- **核心创新 / 方法** · 使用基于泊松超平面的马赛克哈希证明该碰撞关系可扩到 1 小于 p 不超过 2。
- **Baseline** · 既有 p 等于 1 的理论核方法。
- **Benchmark** · 有界高维区域，分析密度估计构造。
- **关键结果 / 消融** · 给出更广 p 范围的可哈希性及新的密度估计方案。
- **适用条件 / 局限** · 超平面采样和区域有界是假设，无摘要实证规模。

**可复用机制** · 对照真实核平均误差和多哈希碰撞方差，独立计采样成本。

<a id="paper-152225"></a>

## Localize Any Object in X-Ray Security Scans without Human Annotation

[官方论文页](https://neurips.cc/virtual/2026/poster/152225) · [作者来源](https://openreview.net/forum?id=UcwEHDEJdH)

- **问题 / 瓶颈** · 自然图像的定位模型遇到吸收叠加、模糊边界和少标注时失配。
- **核心创新 / 方法** · 用成像一致的合成样本和控制遮挡的课程训练通用定位模型。
- **Baseline** · SAM2 及透射任务专用模型。
- **Benchmark** · 六套防御性检测评测，报告密集场景 mAP。
- **关键结果 / 消融** · 摘要报告相对提高 2% 至 23% mAP。
- **适用条件 / 局限** · 合成到真实的差异和误警率待核。

**可复用机制** · 按场景遮挡程度审查通用检测模型的误警和漏警，验证课程贡献。

<a id="paper-151978"></a>

## Localized Dynamics-Aware Domain Adaption for Off-Dynamics Offline Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151978) · [作者来源](https://openreview.net/forum?id=WPPtcvFivw)

- **问题 / 瓶颈** · 全局度量会丢相容区域，逐点过滤昂贵。
- **核心创新 / 方法** · 对源和目标转移聚簇，以领域判别估计簇内差异，保留小差异源簇。
- **Baseline** · 全域适配与逐点过滤离线 RL 方法。
- **Benchmark** · 多级全局和局部动力学变化实验。
- **关键结果 / 消融** · 摘要称持续超过既有方法，对可复用区域利用更好。
- **适用条件 / 局限** · 目标域样本少时簇判定可能过拟合。

**可复用机制** · 固定可用源样本额，按动力学偏移区域比较局部筛选和随机筛选。

<a id="paper-148596"></a>

## Localizing and Repairing Sparse-Prompt Failure in SAM Decoders via Box-to-Point Counterfactual

[官方论文页](https://neurips.cc/virtual/2026/poster/148596) · [作者来源](https://openreview.net/forum?id=wYJKrfS22K)

- **问题 / 瓶颈** · SAM 点提示相对框提示显著退化，整体调参成本高。
- **核心创新 / 方法** · 对齐提示条件做激活修补，在首个图像到词元交叉注意更新位置插轻型残差模块。
- **Baseline** · 原 SAM 与较大的修复基线。
- **Benchmark** · 97,996 个医学图像目标对，CT、MRI、超声、内镜及多个 SAM 模型。
- **关键结果 / 消融** · 不足 9K 参数弥合 89.1% 框点差距。
- **适用条件 / 局限** · 受提示形式和分割分布限制。

**可复用机制** · 用较强提示作受控参照定位最早可修复节点，然后仅在该节点做适配。

<a id="paper-151958"></a>

## Localizing Concepts in Visual Autoregressive Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151958) · [作者来源](https://openreview.net/forum?id=WY3aXqKLtA)

- **问题 / 瓶颈** · 粗到细生成中单一层排名会遗漏尺度或空间差异。
- **核心创新 / 方法** · 用跨尺度探针和因果检查评估概念出现位置。
- **Baseline** · 不同生成模型、类别和位置。
- **Benchmark** · LoCoBench 十类，含 Infinity、HunyuanImage-3.0、InfinityStar。
- **关键结果 / 消融** · 摘要报告可读位置对概念生成有因果作用。
- **适用条件 / 局限** · 依赖尺度分解与探针数据，跨域需要重定位。

**可复用机制** · 检查概念记忆时将内部阶段与空间位置并列，不只看单个注意图。

<a id="paper-152631"></a>

## Localizing Input Uncertainty Quantification for Large Language Models via Shapley Values

[官方论文页](https://neurips.cc/virtual/2026/poster/152631) · [作者来源](https://openreview.net/forum?id=RfKPkFbBsx)

- **问题 / 瓶颈** · 单个不确定标量无法区分知识不足和输入歧义。
- **核心创新 / 方法** · 把候选片段作为玩家，以不同片段组合澄清后条件熵下降估 Shapley 贡献。
- **Baseline** · 全输入歧义打分。
- **Benchmark** · AmbigQA、AmbiEnt 及 MediTOD。
- **关键结果 / 消融** · 摘要报告歧义检测改善，可定位信息不足的表达。
- **适用条件 / 局限** · 依赖合理可生成的澄清候选，不能代替临床判断。

**可复用机制** · 用边际信息增益分配提问预算，并允许片段交互改变优先级。

<a id="paper-151210"></a>

## Local linear convergence of gradient methods for overparameterized Gaussian mixtures

[官方论文页](https://neurips.cc/virtual/2026/poster/151210) · [作者来源](https://openreview.net/forum?id=c9FX4sWgTb)

- **问题 / 瓶颈** · 冗余成分消除部分坏极值，却可能让局部梯度过弱。
- **核心创新 / 方法** · 先用若干短梯度步接近慢增长流形，再用 Polyak 步缩小误差。
- **Baseline** · 梯度 EM 与普通梯度步。
- **Benchmark** · 过参数高斯混合的局部理论；考虑不同权重。
- **关键结果 / 消融** · 特定权重下局部线性收敛，任意权重可达自然误设阈值附近。
- **适用条件 / 局限** · 依赖局部初始化和权重假设，速度不代表全局保证。

**可复用机制** · 按损失地形的快慢方向拆更新，避免在整个空间使用统一步长。

<a id="paper-151248"></a>

## Locally-Additive Regret for Delayed Non-stationary Bandit Convex Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/151248) · [作者来源](https://openreview.net/forum?id=bnpbr6NXNG)

- **问题 / 瓶颈** · 全局延迟惩罚可能掩盖每个稳定段受到的实际影响。
- **核心创新 / 方法** · 用分块与单点平滑乘积的尺度约束消除延迟对估计方差的乘性耦合。
- **Baseline** · 最强不重启对照。
- **Benchmark** · 14 个尺度实验和分段平稳凸 bandit。
- **关键结果 / 消融** · 拟合指数距理论 0.04 内，遗憾最高改善 9.17 倍。
- **适用条件 / 局限** · 所列为 oracle 方法；实际分段未知时需核实。

**可复用机制** · 分段处理改变的反馈行为，按局部时延和估计噪声共同选择更新尺度。

<a id="paper-152505"></a>

## Local Manifold Identification with Latent Linear Models and OT Flows

[官方论文页](https://neurips.cc/virtual/2026/poster/152505) · [作者来源](https://openreview.net/forum?id=SeaR5REYbd)

- **问题 / 瓶颈** · 观测空间的曲率和噪声使局部直接拟合变差。
- **核心创新 / 方法** · 将线性潜变量经运输流映回数据空间，以 Fisher 分数估计处理难算似然。
- **Baseline** · 数据空间的直接线性近似；其他基线待核实。
- **Benchmark** · 合成与真实局部流形。
- **关键结果 / 消融** · 摘要报告最优运输后线性近似误差降低。
- **适用条件 / 局限** · 依赖运输映射质量及流形正则性。

**可复用机制** · 先试可逆的几何标准化，再决定是否需要复杂局部模型。

<a id="paper-149916"></a>

## Local Policy Manifolds for Efficient Multi-Objective Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149916) · [作者来源](https://openreview.net/forum?id=mF8mCetv02)

- **问题 / 瓶颈** · 为 Pareto 前沿每个点单独重训代价大。
- **核心创新 / 方法** · 学习参数和回报的局部关系，在连续策略域内线性外推。
- **Baseline** · 先进多目标强化学习。
- **Benchmark** · 多个连续控制；Pareto 质量与效率。
- **关键结果 / 消融** · 摘要报告前沿质量与效率一致改善。
- **适用条件 / 局限** · 策略流形必须局部平滑连通，断裂模式需重启。

**可复用机制** · 先在现有折中解近邻做廉价拓展，再在局部模型失效时重训。

<a id="paper-154110"></a>

## Local Sparsity Enables Unsupervised LLM Safety Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/154110) · [作者来源](https://openreview.net/forum?id=GBzu2ha5Gf)

- **问题 / 瓶颈** · 高维激活直接拟合正常分布需要过多样本。
- **核心创新 / 方法** · 用稀疏自编码器识别局部共同激活的支持，将异常信号限制到该局部。
- **Baseline** · 安全数据异常检测及能力检测；具体待核实。
- **Benchmark** · 不同模型架构的能力和安全数据。
- **关键结果 / 消融** · 摘要给出环境维数仅对数进入的样本界并有实证。
- **适用条件 / 局限** · 依赖线性表征假设及安全训练分布覆盖。

**可复用机制** · 先压缩需要估计的局部统计范围，再验收部署异常阈值。

<a id="paper-156081"></a>

## Locating and Repairing Domain Shift in VLM Trajectory Planning

[官方论文页](https://neurips.cc/virtual/2026/poster/156081) · [作者来源](https://openreview.net/forum?id=0YmshH9KfL)

- **问题 / 瓶颈** · 均匀分布对齐忽略视觉文本及层级差异。
- **核心创新 / 方法** · 激活修补估因果重要张量，按功能区配 MMD、LoRA 或冻结。
- **Baseline** · 统一 MMD 等修复。
- **Benchmark** · nuScenes、Argoverse 2，三个不同 VLM。
- **关键结果 / 消融** · 每组跨城市轨迹误差差距最低，少 50% 至 60% 可训练参数。
- **适用条件 / 局限** · 仅依所测骨干和两地数据，实际驾驶安全需另验。

**可复用机制** · 将偏移诊断从全模型单一分数扩到模态和层，避免在正常区过度改动。

<a id="paper-153475"></a>

## LOCO: Local Light-Aware Object Compositing with Spatially Varying Illumination-Augmented Data

[官方论文页](https://neurips.cc/virtual/2026/poster/153475) · [作者来源](https://openreview.net/forum?id=L5lQiud81M)

- **问题 / 瓶颈** · 自然合成缺少同一物体在不同位置的照明标注。
- **核心创新 / 方法** · 把每帧视为绑定相机位姿的虚拟聚光灯，改变光束、颜色和强度生成训练样本。
- **Baseline** · 既有物体合成方法。
- **Benchmark** · Laval Indoor SV HDR 与真实采集 LOCO-bench。
- **关键结果 / 消融** · 摘要报告位置照明适应改善且保留物体身份。
- **适用条件 / 局限** · 虚拟光近似难覆盖所有反射和复杂光源。

**可复用机制** · 把多视角的位姿变化变成可控制的环境因素，构造真实背景下的因素干预测试。

<a id="paper-155077"></a>

## LoCo: Selective Local Competition for Discriminative Open-Vocabulary Multi-Label Recognition

[官方论文页](https://neurips.cc/virtual/2026/poster/155077) · [作者来源](https://openreview.net/forum?id=8eYxZ7Wn0X)

- **问题 / 瓶颈** · 全体类别做 softmax 会压制可兼容的细粒度及粗粒度标签。
- **核心创新 / 方法** · 用空间一致特征和选择性 softmax，聚合多尺度局部结果和全图结果。
- **Baseline** · 全局图文匹配及已有开放多标签。
- **Benchmark** · 四个多标签数据集，F1 和 mAP。
- **关键结果 / 消融** · 平均改善 11.3% F1 和 5.2% mAP。
- **适用条件 / 局限** · 局部兼容关系误差会误压正确类别。

**可复用机制** · 先明确标签何时互斥，再决定归一化组，避免将多标签当作局部单选。

<a id="paper-155725"></a>

## LOCU: Löwdin-Orthogonalized Constraint Updates for Multi-Constraint Policy Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/155725) · [作者来源](https://openreview.net/forum?id=3P2JrQgcPN)

- **问题 / 瓶颈** · 约束方向高相关会相互抵消或令信赖域数值不稳定。
- **核心创新 / 方法** · 以 Fisher 度量筛选和压缩近重合方向，Löwdin 正交化后做约化空间活动集求解。
- **Baseline** · 现有多约束策略优化；基线待核实。
- **Benchmark** · 紧可行区、强耦合和不可行初值及不同价值网络。
- **关键结果 / 消融** · 摘要报告所测困难情境下更新稳定。
- **适用条件 / 局限** · Fisher 估计和降维可能错过罕见约束。

**可复用机制** · 把近重复约束压成可稳定求解的子空间，同时确保仍能保护已满足项。

<a id="paper-154983"></a>

## LOFT: Low-Rank Orthogonal Fine-Tuning via Task-Aware Support Selection

[官方论文页](https://neurips.cc/virtual/2026/poster/154983) · [作者来源](https://openreview.net/forum?id=9RrKYAh9GU)

- **问题 / 瓶颈** · 改变参数化常混入选错更新空间的影响。
- **核心创新 / 方法** · 一阶分析建议用任务梯度选支持，再在该支持上应用乘性正交变化。
- **Baseline** · 坐标、蝶形、Householder 和主子空间微调。
- **Benchmark** · 语言理解、视觉、数学、跨语言域迁移；匹配参数内存。
- **关键结果 / 消融** · 摘要报告梯度选支持改善效率性能折中。
- **适用条件 / 局限** · 支持估计受采样梯度质量限制。

**可复用机制** · 同预算做子空间与变换两轴消融，先验证任务梯度能否比主成分更准。

<a id="paper-149279"></a>

## Logarithmic Depth Suffices for In-Context Gradient Descent

[官方论文页](https://neurips.cc/virtual/2026/poster/149279) · [作者来源](https://openreview.net/forum?id=rUh3nJ2f7c)

- **问题 / 瓶颈** · 每层对应一个更新的解释忽略层间复合。
- **核心创新 / 方法** · 对线性注意力及对角二次任务刻画表达最终迭代值的深度。
- **Baseline** · 顺序逐步模拟、核与 oracle 对照。
- **Benchmark** · 控制回归及标准 Transformer 扩展，另有 Qwen2.5 早退探针。
- **关键结果 / 消融** · 理论上 k 步结果需对数级深度，控制实验出现对应转折。
- **适用条件 / 局限** · 紧界针对明确线性任务，不能普适地给真实模型深度。

**可复用机制** · 用优化轨迹的函数表示复杂度而非更新次数判断模型所需计算。

<a id="paper-148791"></a>

## Log-Averaged Mirror Prox for Fast, Large-Scale Optimal Transport in Linear Space

[官方论文页](https://neurips.cc/virtual/2026/poster/148791) · [作者来源](https://openreview.net/forum?id=v3S7acblMZ)

- **问题 / 瓶颈** · 显式运输矩阵的存储随两个边缘支持数相乘。
- **核心创新 / 方法** · 跟踪对数平均的对偶序列以实现原始 mirror prox，保留 GPU 密集归约。
- **Baseline** · 一阶原始对偶方法。
- **Benchmark** · 高精度熵正则等运输问题；CUDA 和大规模离散支撑。
- **关键结果 / 消融** · 存储从 O(nm) 至 O(n+m)，最大双边支持为 2^18。
- **适用条件 / 局限** · 算术成本仍随乘积增长，证书受可行误差影响。

**可复用机制** · 优先压缩优化状态表示而非计算图本身，以继续使用高效密集内核。

<a id="paper-148712"></a>

## Logical Distillation of Transformer Encoders

[官方论文页](https://neurips.cc/virtual/2026/poster/148712) · [作者来源](https://openreview.net/forum?id=vcu7CdwIWi)

- **问题 / 瓶颈** · 稀疏特征只说明存在内容，不能显示跨序列组合规则。
- **核心创新 / 方法** · 蒸馏为迭代时序决策树，后级树复用早级时序公式。
- **Baseline** · 标准时序逻辑学习任务及原编码器。
- **Benchmark** · 线性时序逻辑基准；此处只提取通用算法。
- **关键结果 / 消融** · 摘要报告恢复较简短且准确的逻辑公式。
- **适用条件 / 局限** · 替代规则的忠实度应在未见序列和干预中验证。

**可复用机制** · 当需要可读时序解释时，让代理模型显式表示跨位置条件的组合，而非逐词打分。

<a id="paper-153496"></a>

## LogicDirector: Enforcing Temporal Composition in Text-to-Video Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/153496) · [作者来源](https://openreview.net/forum?id=KxBQdkTg2q)

- **问题 / 瓶颈** · 视频能生成实体和事件却不遵循先后关系。
- **核心创新 / 方法** · 将文本转为可执行约束，以注意证据判断实体、动作绑定和时序；无梯度多选潜状态。
- **Baseline** · 未引导的 CogVideoX 和 Wan 2.1。
- **Benchmark** · TempBench 四类时序运算；分层实体、事件和次序。
- **关键结果 / 消融** · 摘要报告时序遵循改善且保持视觉质量。
- **适用条件 / 局限** · 取决于逻辑解析和注意证据可靠；搜索增加算量。

**可复用机制** · 把复合要求转成独立检查的中间状态约束，发现错误尽早重选候选。

<a id="paper-153327"></a>

## LogicTree-RAG: Logic Tree-guided Retrieval-Augmented Generation for Long-form Patent Drafting

[官方论文页](https://neurips.cc/virtual/2026/poster/153327) · [作者来源](https://openreview.net/forum?id=M9Gxp6XTlc)

- **问题 / 瓶颈** · 局部连贯不保证跨章节依赖、证据和篇幅一致。
- **核心创新 / 方法** · 递归生成检索支撑的技术节点，再混合遍历映射到章节。
- **Baseline** · 强语言模型和此前专利生成方案。
- **Benchmark** · 长篇专利草拟；内容、合规表达及词元效率。
- **关键结果 / 消融** · 摘要报告一致改善，量化细项待核实。
- **适用条件 / 局限** · 证据节点可靠性及外部法律审核仍需独立评估。

**可复用机制** · 分离技术信息依赖与最终文档顺序，使编辑和验收能逐节点追溯。

<a id="paper-152383"></a>

## Logistic Bandits with $\tilde{O}(\sqrt{dT})$ Regret without Context Diversity Assumptions

[官方论文页](https://neurips.cc/virtual/2026/poster/152383) · [作者来源](https://openreview.net/forum?id=TVCHVTTBhf)

- **问题 / 瓶颈** · 协方差满秩假设排除了常见低维集中。
- **核心创新 / 方法** · 一部分样本先估初点，另一部分独立做 Newton 型单步校正。
- **Baseline** · 依赖上下文多样性的既有算法。
- **Benchmark** · K 臂逻辑赌博机，测遗憾与维度依赖。
- **关键结果 / 消融** · 无需多样性仍达近似平方根 dT 遗憾，可改为依赖数据复杂度。
- **适用条件 / 局限** · 逻辑模型和分割精度要求需查。

**可复用机制** · 以独立样本去耦初点估计和偏差修正，再按有效维度报告成本。

<a id="paper-153860"></a>

## Logit-Conditioned Diffusion Decoding for Frozen Discrete-Token VLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/153860) · [作者来源](https://openreview.net/forum?id=ICK4e2LwDl)

- **问题 / 瓶颈** · 只解单个码本索引损失有效候选信息。
- **核心创新 / 方法** · 以原模型 logits 加权码向量，训练时用经校准的编码器代理 logits 训练扩散解码器。
- **Baseline** · 原 VQ-VAE 解码及同骨干图像细化。
- **Benchmark** · ImageNet-1K、MJHQ-30K、GenEval、DPG-Bench、WISE，测重建、生成与对齐。
- **关键结果 / 消融** · 重建 FID 下降 74%，Janus-Pro 7B 生成 FID 下降 34%，语义对齐近似保持。
- **适用条件 / 局限** · 依赖能读取 logits 及训练代理和推理分布匹配。

**可复用机制** · 在重训主干前验证软分布是否含足够信息，并对照同算力的普通后处理。

<a id="paper-149157"></a>

## Logit-Contribution Scoring Identifies Non-Literal Retrieval Heads

[官方论文页](https://neurips.cc/virtual/2026/poster/149157) · [作者来源](https://openreview.net/forum?id=sQe55RhZJ7)

- **问题 / 瓶颈** · 复制词重合漏掉能从相关段落生成新措辞的注意力头。
- **核心创新 / 方法** · 投影 OV 输出到答案词反嵌入，比较目标段和非目标段，并对高分头消融。
- **Baseline** · 纯注意力与词重合检索头识别。
- **Benchmark** · NoLiMa、三种模型家族；ROUGE-L、参数记忆与算术。
- **关键结果 / 消融** · Qwen3-8B 消融 50 头使 ROUGE-L 从 0.401 至 0，而最强基线仍为 0.292；一般任务维持。
- **适用条件 / 局限** · 依赖目标答案和证据位置，开放问题定位需验证。

**可复用机制** · 结合读取位置和写入方向识别功能模块，再用非目标任务控制消融特异性。

<a id="paper-148606"></a>

## Log-Likelihood, Simpson’s Paradox, and the Detection of Machine-Generated Text

[官方论文页](https://neurips.cc/virtual/2026/poster/148606) · [作者来源](https://openreview.net/forum?id=wUQEkUblF7)

- **问题 / 瓶颈** · 将统计机制不同的 token 直接平均会出现类似 Simpson 悖论的信号抵消。
- **核心创新 / 方法** · 估计给定隐藏区域的两类分数分布并做条件校准。
- **Baseline** · 原始 Fast-DetectGPT 与其他平均 token 对照。
- **Benchmark** · 多数据及生成模型；测 AUROC。
- **关键结果 / 消融** · 在 GPT-5.4 文本上，校准版 Fast-DetectGPT AUROC 从 0.63 到 0.85。
- **适用条件 / 局限** · 局部校准依赖训练分布，未知文本域应重新核查。

**可复用机制** · 先诊断组内是否有信号而组间汇总反转，再决定如何校准最终和分。

<a id="paper-149042"></a>

## LogSig-SSM: Time-Series Modelling with Multi-Scale Log-Signature Compression for State-Space Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149042) · [作者来源](https://openreview.net/forum?id=tIKjiGlxPz)

- **问题 / 瓶颈** · 连续时间网络长序列昂贵，直接逐采样 SSM 难结合高阶通道关系。
- **核心创新 / 方法** · 多尺度窗编码组内交互，SSM 传播长程依赖。
- **Baseline** · 既有 SSM 和神经控制或粗糙微分方程。
- **Benchmark** · UEA、PPG-DaLiA、天气预测和 PhysioNet Sepsis；任务效果、训练与显存。
- **关键结果 / 消融** · 摘要报告整体性能及资源优势。
- **适用条件 / 局限** · 窗和签名阶数与数据变化相关，极稀疏窗口需查。

**可复用机制** · 在模型前将局部采样频率与全局状态更新频率解耦。

<a id="paper-156145"></a>

## LogSTOP: Temporal Scores over Prediction Sequences for Matching and Retrieval

[官方论文页](https://neurips.cc/virtual/2026/poster/156145) · [作者来源](https://openreview.net/forum?id=02WO2BFUCS)

- **问题 / 瓶颈** · 检测器只给单帧或短片段证据，整体语义检索忽略顺序。
- **核心创新 / 方法** · 对局部检测序列计算线性时序逻辑查询分数。
- **Baseline** · 大型视觉和音频语言模型、时序逻辑及零样本文本视频检索。
- **Benchmark** · 视频物体动作和音频情感的查询或排序任务。
- **关键结果 / 消融** · 匹配至少改善 16%，物体和动作检索的 mAP 分别改善 28% 与 18%。
- **适用条件 / 局限** · 依赖局部检测质量和可表达的规则，复杂开放语义需查。

**可复用机制** · 把高层顺序约束分离出来，比较同一底层检测器在规则和整体语义检索中的表现。

<a id="paper-154345"></a>

## LoMo: Local Modality Substitution for Deeper Vision-Language Fusion

[官方论文页](https://neurips.cc/virtual/2026/poster/154345) · [作者来源](https://openreview.net/forum?id=EHe0liGkCc)

- **问题 / 瓶颈** · 训练通常是文字提问、图像作参考，模型学出模态角色偏置。
- **核心创新 / 方法** · 动态选择文字范围，渲染成图，形成图文交替输入。
- **Baseline** · 常规监督微调。
- **Benchmark** · 十三项多模态基准，含 LLaVA-OneVision-1.5-8B、Qwen3.5-9B。
- **关键结果 / 消融** · 两个模型较常规微调分别改善 2.67 和 2.82 点。
- **适用条件 / 局限** · 渲染文字和自然视觉信息仍不同，跨字体语言和真实场景的收益待查。

**可复用机制** · 用载体转换构造共享语义对照，直接测回答对同一内容形式变化的敏感性。

<a id="paper-139582"></a>

## Long-Context Generation Is a Sampling Problem

[官方论文页](https://neurips.cc/virtual/2026/poster/139582) · [作者来源](https://openreview.net/forum?id=Gyng0YSjXM)

- **问题 / 瓶颈** · 狭窄截断在接近长文尾部会塌缩至最高概率 token。
- **核心创新 / 方法** · 在同模型上测 P-less、Top-H、top-nσ、min-p 与传统截断，检查全窗排名变化。
- **Baseline** · top-p、top-k、min-p。
- **Benchmark** · 十个 1B 至 120B 模型、8K 至 64K 输出，自动、人工和重复度评估。
- **关键结果 / 消融** · 120B 上人工偏好 P-less 超过九成；64K 的 10-gram 重复接近零。
- **适用条件 / 局限** · 主要开权重模型，任务性事实准确与闭源推理迁移待核实。

**可复用机制** · 用按位置分层的重复和概率排名诊断低多样性，避免归因为上下文长度不足。

<a id="paper-151973"></a>

## Long-Horizon Q-Learning: Accurate Value Learning via n-Step Inequalities

[官方论文页](https://neurips.cc/virtual/2026/poster/151973) · [作者来源](https://openreview.net/forum?id=WRJ62DYfLa)

- **问题 / 瓶颈** · 误差沿 TD 反传会放大。
- **核心创新 / 方法** · 铰链损失惩罚最优价值低于先按观测序列行动再最优接续的情形，复用 TD 前向输出。
- **Baseline** · 一步和多步 TD，以及不同现有价值方法。
- **Benchmark** · 在线及离线到在线强化基准；回报与运行时间。
- **关键结果 / 消融** · 摘要报告在类似时间下超过一步、多步 TD。
- **适用条件 / 局限** · 随机环境下依赖期望含义和轨迹覆盖，具体约束与噪声需查。

**可复用机制** · 将多步回报用作下界约束而非直接目标，分别测估计偏差与端任务效果。

<a id="paper-148330"></a>

## Long-Lived AI Agents Age Too: They Quietly Decay After Deployment

[官方论文页](https://neurips.cc/virtual/2026/poster/148330) · [作者来源](https://openreview.net/forum?id=ye3N1zTJyc)

- **问题 / 瓶颈** · 单次快照漏掉压缩、干扰、改写或维护导致的隐性退化。
- **核心创新 / 方法** · 在多种长期设定用反事实替换记忆组件来定位退化阶段。
- **Baseline** · 不同记忆政策、受控运行环境和实际代理框架。
- **Benchmark** · 七种场景、十四个模型、约四百次运行，覆盖 8 至 200 次会话。
- **关键结果 / 消融** · 动态状态追踪可从满分跌到零，部分强模型主要掉在利用而非写入。
- **适用条件 / 局限** · 退化类型和幅度依赖数据与代理实现。

**可复用机制** · 定期重测相同派生事实并隔离写入与读取，避免只凭任务当日成功推断稳定。

<a id="paper-139600"></a>

## Long-Rollout Stability in AI Weather Models: A Quantitative Benchmark and Analysis

[官方论文页](https://neurips.cc/virtual/2026/poster/139600) · [作者来源](https://openreview.net/forum?id=GDBChfsv9N)

- **问题 / 瓶颈** · 短期准确率和单一不稳定标签掩盖不同失效原因。
- **核心创新 / 方法** · 对九个模型做一年滚动，区分发散、漂移和季节性丧失，并加入输入噪声测试。
- **Baseline** · 多种高水平天气模型及 ViT 架构消融。
- **Benchmark** · 一年预报，测频谱和季节保持。
- **关键结果 / 消融** · 不稳模型放大高频能量，稳定模型对输入噪声表现为去噪且仍生成由初态约束的独特轨迹。
- **适用条件 / 局限** · 非天气系统和更长时间尺度待核实。

**可复用机制** · 在长滚动早期监控小尺度误差增益，用来定位长期发散前兆。

<a id="paper-150236"></a>

## LongSpike: Fractional Order Spiking State Space Models for Efficient Long Sequence Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/150236) · [作者来源](https://openreview.net/forum?id=jkIua01azq)

- **问题 / 瓶颈** · 一阶动态的记忆容易衰减，分数阶又难并行。
- **核心创新 / 方法** · 把长记忆核整合进脉冲状态的可并行表述。
- **Baseline** · 先进脉冲网络及整数阶动态。
- **Benchmark** · Long Range Arena、WikiText-103、Speech Commands，多任务准确及稀疏性。
- **关键结果 / 消融** · 摘要称准确改善并保留稀疏突触计算。
- **适用条件 / 局限** · 实际硬件能耗及长核开销待核。

**可复用机制** · 等突触运算量扫序列长度，比较可记忆跨度而非仅短序列精度。

<a id="paper-151462"></a>

## Long-Term Composition of Human-Object Interactions

[官方论文页](https://neurips.cc/virtual/2026/poster/151462) · [作者来源](https://openreview.net/forum?id=aSgJgrbgM5)

- **问题 / 瓶颈** · 独立人-物动作段会断裂，也无法提前向后续对象导航。
- **核心创新 / 方法** · 扩散联合使用过去和未来上下文，并以碰撞校正和手物位移损失改善接触。
- **Baseline** · 原子交互与不含场景对象的动作组合路线。
- **Benchmark** · ParaHome 上长序列交互生成。
- **关键结果 / 消融** · 摘要称可生成时间连贯的交互，具体量化待核。
- **适用条件 / 局限** · 需可获得后续目标，实际接触有效性待核。

**可复用机制** · 在固定片段生成器下分别消融前段连续性和未来目标，单列碰撞及接触错误。

<a id="paper-155991"></a>

## Long-Term Risks of Risk-Based Allocation

[官方论文页](https://neurips.cc/virtual/2026/poster/155991) · [作者来源](https://openreview.net/forum?id=1LHT6frSus)

- **问题 / 瓶颈** · 训练误差低不能保证部署后支付公平，选择行为会改变服务样本。
- **核心创新 / 方法** · 分析决策者和服务方互动的长期均衡，比较替代补偿规则。
- **Baseline** · 现有风险预测补偿。
- **Benchmark** · Medicare Advantage 背景，以及合成和半合成试验。
- **关键结果 / 消融** · 理论解释特定过付现象，替代规则在假设下消除过付。
- **适用条件 / 局限** · 非现实政策因果验证，依赖成本和选择假定。

**可复用机制** · 在采用预测作支付依据前，用模拟均衡检查选择变化和预算。

<a id="paper-151911"></a>

## Long Video Instructional Editing in the Wild

[官方论文页](https://neurips.cc/virtual/2026/poster/151911) · [作者来源](https://openreview.net/forum?id=WxwO1ainQv)

- **问题 / 瓶颈** · 短视频编辑器不保证跨镜头一致，还容易改到无目标画面。
- **核心创新 / 方法** · 按镜头划任务，维护经评审改良的锚库，用短片训练的 LoRA 编辑器接受锚条件。
- **Baseline** · 强短视频编辑器。
- **Benchmark** · LVEdit-Bench，分测单镜头质量、跨镜头身份与目标缺失。
- **关键结果 / 消融** · 摘要称单段持平、长程身份和时段选择改善。
- **适用条件 / 局限** · 依赖锚质量及镜头边界，VLM 评价误差待核。

**可复用机制** · 固定短片编辑器比较无锚与跨镜头锚，并保留无目标负控。

<a id="paper-154685"></a>

## Look-ahead Variational Flow for Generative Online Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/154685) · [作者来源](https://openreview.net/forum?id=BkbldiALe2)

- **问题 / 瓶颈** · 在线强化学习的目标随策略变化，生成策略尤容易波动。
- **核心创新 / 方法** · 以预测动态形成前瞻目标，用近端变分自由能约束更新，再以粗细结合的传输流生成。
- **Baseline** · 动作价值引导的生成策略及强连续控制方法。
- **Benchmark** · DeepMind Control Suite、Humanoid Bench，测样本效率和最终表现。
- **关键结果 / 消融** · 摘要称两项均超过强参考，并推导较紧漂移界。
- **适用条件 / 局限** · 依赖预测器准确性，错配及计算预算待核。

**可复用机制** · 对照同信任域下前瞻与即时目标，测漂移、覆盖与长期回报。

<a id="paper-153870"></a>

## Lookalike3D: Seeing Double in 3D

[官方论文页](https://neurips.cc/virtual/2026/poster/153870) · [作者来源](https://openreview.net/forum?id=I8MCVub4xs)

- **问题 / 瓶颈** · 单独观察的实例可能只见一侧，普通分类不能识别是否同一类重复实物。
- **核心创新 / 方法** · 用多视角图像与视觉教师做三类相似性学习，配对结果用于重建和部件共分割。
- **Baseline** · 同任务现有对照，名称待核。
- **Benchmark** · ScanNet++ 的 3DTwins 约 7.6 万对以及下游重建。
- **关键结果 / 消融** · 检测比对照高 14% IoU，摘要报告下游受益。
- **适用条件 / 局限** · 依赖配对准确，近似物体的细节差异可能被错误融合。

**可复用机制** · 以人工确认和模型配对作上限对照，检查互补结构与错误配对传导。

<a id="paper-154223"></a>

## Look-Before-Move: Narrative-Grounded World Visual Attention in Dynamic 3D Story Worlds

[官方论文页](https://neurips.cc/virtual/2026/poster/154223) · [作者来源](https://openreview.net/forum?id=FIGk7el4fq)

- **问题 / 瓶颈** · 只有运动平滑不足以满足叙事或可见性。
- **核心创新 / 方法** · 把故事意图转成观察约束，先选几何可行视点，再连续连接。
- **Baseline** · 代表相机规划方法。
- **Benchmark** · StoryBlender 50 故事、457 场景、1585 镜头。
- **关键结果 / 消融** · 摘要称主体可见性、意图一致和轨迹质量提升。
- **适用条件 / 局限** · 基准为动画环境，自动意图匹配的评估可靠性待核。

**可复用机制** · 相同相机预算分别测直接拟轨迹与先约束视点，报告遮挡和构图偏差。

<a id="paper-149054"></a>

## Look Before You Reason: Implicit Visual Thinking for Efficient Multimodal Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/149054) · [作者来源](https://openreview.net/forum?id=tDZnYu9iz9)

- **问题 / 瓶颈** · 反复发送裁剪图会重复计算，且观察同解码脱节。
- **核心创新 / 方法** · 预测关联区域并与图块对齐，在后续解码中加权对应 KV 表示。
- **Baseline** · 显式裁剪、缩放和多轮观察路线。
- **Benchmark** · COCO-ObjQA 与另两项多模态评测，比较正确性和成本。
- **关键结果 / 消融** · 摘要称稳定改善且额外推理成本低。
- **适用条件 / 局限** · 原图低分辨率未保留的细节不能靠重加权恢复。

**可复用机制** · 同视觉分辨率预算比较缓存强调和真实重采样，分开看目标定位和回答。

<a id="paper-150598"></a>

## Looking Through the Mirror: Minimax-Optimal Regularized Regrets in Online Learning and Bandits

[官方论文页](https://neurips.cc/virtual/2026/poster/150598) · [作者来源](https://openreview.net/forum?id=gxjUmgllX0)

- **问题 / 瓶颈** · 线性对抗奖励通常给平方根级遗憾，但目标正则提供曲率。
- **核心创新 / 方法** · 用对偶 Bregman 几何处理平移不变，再用 van Trees 化为估计下界。
- **Baseline** · 标准无正则在线学习与特定曲线损失的下界。
- **Benchmark** · 全信息和老虎机反馈的理论设置。
- **关键结果 / 消融** · 弱正则恢复平方根 T，强正则在指定条件下为 η log T。
- **适用条件 / 局限** · 结论限特定强凸、可分 Legendre 正则。

**可复用机制** · 在超参数比较中标注目标正则差异，避免混比不同遗憾定义。

<a id="paper-151188"></a>

## LookThere! Sparse Vision by Reinforced Selection

[官方论文页](https://neurips.cc/virtual/2026/poster/151188) · [作者来源](https://openreview.net/forum?id=cJeezfL5As)

- **问题 / 瓶颈** · 固定处理全高分辨率输入浪费大量算力。
- **核心创新 / 方法** · 用 actor-critic 联合训练位置选择与提取，只访问高分辨率的所选部分。
- **Baseline** · 现有选择器和全量视觉参照。
- **Benchmark** · 高分辨率交通标志与台球、ImageNet、ADE20K、零样本分类和计数。
- **关键结果 / 消融** · 所测稀疏任务最少处理 0.2% 输入仍能维持准确。
- **适用条件 / 局限** · 强局部证据假设可能不适合密集小目标。

**可复用机制** · 按任务可见关键像素面积分桶，报告真实采集成本和精度。

<a id="paper-149223"></a>

## LookWhen? Fast Video Recognition by Learning When, Where, and What to Compute

[官方论文页](https://neurips.cc/virtual/2026/poster/149223) · [作者来源](https://openreview.net/forum?id=rzaezKzgbP)

- **问题 / 瓶颈** · 浅层选取与深层表征需要不同监督。
- **核心创新 / 方法** · 低清视频全局评分、深层只处理前 K；近邻距离训练选择，帧内归一化教师特征用于变化学习。
- **Baseline** · 高效视频模型与同规模强化基线；速度对照 InternVideo2-B。
- **Benchmark** · 六数据集、两种设置，测准确率、FLOPs 与吞吐。
- **关键结果 / 消融** · 十二项中九项占优，其余接近；等准确率快 6.7 倍。
- **适用条件 / 局限** · 解码和分辨率成本是否计入需核。

**可复用机制** · 相同保留率对照学习选择、均匀抽样和仅时间剪枝，并按速度实测。

<a id="paper-148287"></a>

## Loop alignment: Self-organized Weight Transpose in Predictive Coding through Independent Hebbian Plasticity.

[官方论文页](https://neurips.cc/virtual/2026/poster/148287) · [作者来源](https://openreview.net/forum?id=yyy2M0dK0r)

- **问题 / 瓶颈** · 显式同步转置不是自然回路具备的接口。
- **核心创新 / 方法** · 分别比较独立局部 Hebbian 更新和固定随机反馈，并推导环路对齐。
- **Baseline** · 需同步权重的预测编码。
- **Benchmark** · MNIST、Fashion-MNIST 和共享路径双任务。
- **关键结果 / 消融** · 两变体约匹配普通预测编码 85% MNIST，双任务共享中对齐更强。
- **适用条件 / 局限** · 仅小规模任务，不能证明真实脑系统的机制。

**可复用机制** · 先在相同初始化下监控任务分数及路径对齐，再评估规模。

<a id="paper-152196"></a>

## Looped Diffusion Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152196) · [作者来源](https://openreview.net/forum?id=UqgMsw7AZH)

- **问题 / 瓶颈** · 普遍增深会同时抬升参数与计算，采样各步所需计算不同。
- **核心创新 / 方法** · 复用早中层权重，训练加深实际执行，推理时调轮数。
- **Baseline** · 同参数和相近每步计算的非循环掩码扩散。
- **Benchmark** · 多预训练语料、GSM8K 等推理基准及掩码位置相互作用。
- **关键结果 / 消融** · 最多少 3.3 倍训练 FLOPs 达同等表现；GSM8K 最高多 8.5 点。
- **适用条件 / 局限** · 额外循环的真实端侧延迟和跨数据适配待核。

**可复用机制** · 固定参数分别扫总循环数和每步分配，检查改善是否来自掩码位置通信。

<a id="paper-149678"></a>

## Looped Transformers with Layer Normalization Provably Learn the Power Method

[官方论文页](https://neurips.cc/virtual/2026/poster/149678) · [作者来源](https://openreview.net/forum?id=oFm9j93SjQ)

- **问题 / 瓶颈** · 模型实现算法的能力和训练能否学到算法是两回事。
- **核心创新 / 方法** · 分析仅监督主成分预测的线性循环 Transformer，证明梯度下降得到每层一次幂迭代。
- **Baseline** · 无层归一化，包含逐层迭代监督变体。
- **Benchmark** · 主成分预测理论构造。
- **关键结果 / 消融** · 有层归一化收敛到幂法；无归一化即使逐层指导也无法精确学习。
- **适用条件 / 局限** · 理论依赖线性架构及设定，实际模型不必采用同算法。

**可复用机制** · 在迭代算法诊断中比较每层状态和规范化后的残差，而非仅看末输出。

<a id="paper-152801"></a>

## Loop-Free Inverse Reinforcement Learning via Sequential Value Recovery

[官方论文页](https://neurips.cc/virtual/2026/poster/152801) · [作者来源](https://openreview.net/forum?id=QGmivFge7W)

- **问题 / 瓶颈** · 交替学奖励和策略代价高且不稳。
- **核心创新 / 方法** · 由扩散策略恢复动作价值梯度，估软值及状态偏移，按 Bellman 一致性取奖励。
- **Baseline** · 双层逆强化学习及最快现有参考。
- **Benchmark** · Maze、Franka Kitchen、Adroit Hand Pen、Push-T，测恢复与耗时。
- **关键结果 / 消融** · 相对最快参考快 2–3 倍，恢复质量持平或更高。
- **适用条件 / 局限** · 专家近优性和价值偏移可识别性待核。

**可复用机制** · 用已知奖励的安全仿真分别测值回归误差和恢复奖励可训练性。

<a id="paper-153561"></a>

## LoopPrune: Evolutionary Module Selection with Iterative Execution for Efficient Large Language Model Compression

[官方论文页](https://neurips.cc/virtual/2026/poster/153561) · [作者来源](https://openreview.net/forum?id=KSdT4wLb1i)

- **问题 / 瓶颈** · 静态子图约束会过早丢弃推理能力。
- **核心创新 / 方法** · 以预训练层库搜索跳过、一次执行或有限重复的布局。
- **Baseline** · 传统静态剪枝及未压缩模型。
- **Benchmark** · 多种语言模型及稀疏率，测零样本推理和困惑度。
- **关键结果 / 消融** · 摘要称多个设置优于剪枝参考，某些推理题可匹配甚至超过原模型。
- **适用条件 / 局限** · 搜索成本与实际推理速度未由摘要确认。

**可复用机制** · 在严格相同延迟和内存约束下比较重复层与静态删层。
