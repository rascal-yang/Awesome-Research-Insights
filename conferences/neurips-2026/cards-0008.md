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

<a id="paper-150580"></a>

## LoopRPT: Reinforcement Pre-Training for Looped Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150580) · [作者来源](https://openreview.net/forum?id=h8EZBjmDcp)

- **问题 / 瓶颈** · 词元级强化无法直接约束逐轮内部推理。
- **核心创新 / 方法** · 以指数平均教师作参考，用加噪潜轨迹形成逐步训练反馈。
- **Baseline** · Ouro 常规预训练与输出端强化路线。
- **Benchmark** · 多个尺度的准确率和迭代算力，另切分困难词元。
- **关键结果 / 消融** · 摘要报告质量计算 Pareto 改善，困难词元的早期推理也改善。
- **适用条件 / 局限** · 依赖可访问潜迭代及可靠教师参考。

**可复用机制** · 将中途表示质量单独纳入训练，避免以提前退出误代真正提效。

<a id="paper-154333"></a>

## LoRAcles: Self-Supervised Weight-Space Interpretability at Scale

[官方论文页](https://neurips.cc/virtual/2026/poster/154333) · [作者来源](https://openreview.net/forum?id=EOoc3j4hW8)

- **问题 / 瓶颈** · 只看推理样例可能漏掉微调引起的细小变化。
- **核心创新 / 方法** · 用文档监督合成适配器，再训练审计模型回答适配器可能学到的内容。
- **Baseline** · AuditBench 的已有行为审计模型。
- **Benchmark** · Qwen-3-14B、Llama-3.3-70B；微调行为审计。
- **关键结果 / 消融** · 摘要报告在 AuditBench 提升，训练样本扩大到约 100K 仍有正向趋势。
- **适用条件 / 局限** · 检测器会幻觉且只能抓显著变化，不应取代行为测试。

**可复用机制** · 用权重线索决定测试优先级，确保异常结论由输入输出对照复核。

<a id="paper-155848"></a>

## LoRaQ: Optimized Low Rank Approximation for 4-bit Quantization

[官方论文页](https://neurips.cc/virtual/2026/poster/155848) · [作者来源](https://openreview.net/forum?id=2S5ArH5uJa)

- **问题 / 瓶颈** · 高精度补偿分支和数据校准可能抵消低比特收益。
- **核心创新 / 方法** · 以无数据校准联合优化残差量化与分支，用低于十六位的补偿配置。
- **Baseline** · 高精度低秩补偿路线和同显存对照。
- **Benchmark** · PixArt-Sigma、SANA、Flux.1；质量和 MI355 核速度。
- **关键结果 / 消融** · 摘要报告同显存质量改善，内核级最高快 3.19 倍。
- **适用条件 / 局限** · 核加速不能直接视为整网端到端加速。

**可复用机制** · 将误差补偿作为需量化的组件共同选择精度，而非事后保留全精度。

<a id="paper-150890"></a>

## LoRASpace: A Pool-Wide Shared Substrate for Static and Dynamic Multi-LoRA Composition

[官方论文页](https://neurips.cc/virtual/2026/poster/150890) · [作者来源](https://openreview.net/forum?id=edpJ8ipgAp)

- **问题 / 瓶颈** · 直接合并相互干扰，独立前向成本线性增长。
- **核心创新 / 方法** · 从整个池的低秩因子做 SVD，静态或动态复用保留能量的共享子空间。
- **Baseline** · 权重静态合并及逐适配器合成。
- **Benchmark** · 三组扩散适配器与 FLAN-T5 等两组文本适配器。
- **关键结果 / 消融** · 扩散池用秩和 46% 至 57% 保留 99% 能量；六个适配器时动态方案较独立合成快逾六倍。
- **适用条件 / 局限** · 多样性强化的池近正交时压缩收益有限。

**可复用机制** · 以实测因子重叠决定哪些适配器可共享，不按模态假设可压缩。

<a id="paper-153224"></a>

## LoRAtorio: An intrinsic approach to LoRA Skill Composition

[官方论文页](https://neurips.cc/virtual/2026/poster/153224) · [作者来源](https://openreview.net/forum?id=MrZTwGqEdZ)

- **问题 / 瓶颈** · 固定全图权重使不同技能相互干扰并在域外漂移。
- **核心创新 / 方法** · 以适配器和基座预测噪声的块余弦差异构造权重，修正无条件合成基线。
- **Baseline** · 已有训练自由多 LoRA 合成。
- **Benchmark** · ComposLoRA，CLIPScore、GPT-4V 偏好；另测 FLUX.1-dev。
- **关键结果 / 消融** · 较最强对照最高提升 1.3% CLIPScore，判优率 76.92%。
- **适用条件 / 局限** · 需验证域内外差异能可靠指示适配器相关性。

**可复用机制** · 用基座预测作共同参考，在空间位置而非仅全局分派适配器。

<a id="paper-149043"></a>

## LoRIF: Low-Rank Influence Functions for Scalable Training Data Attribution

[官方论文页](https://neurips.cc/virtual/2026/poster/149043) · [作者来源](https://openreview.net/forum?id=tIJbQhZCF4)

- **问题 / 瓶颈** · 投影维数提高时 I/O 与近似逆 Hessian 成本双增。
- **核心创新 / 方法** · 保存梯度低秩因子，以截断 SVD 和 Woodbury 公式处理曲率项。
- **Baseline** · LoGRA、TRAK 类随机投影路线。
- **Benchmark** · 0.1B 至 70B 模型、百万级样本；质量、存储和查询速度。
- **关键结果 / 消融** · 相对 LoGRA 最高约二十倍存储和查询收益，质量相当或更好。
- **适用条件 / 局限** · 需测近似秩对高影响样本排序的影响。

**可复用机制** · 将长期驻留的逐样本状态与查询期曲率近似分开压缩。

<a id="paper-149908"></a>

## LOSCAR-SGD: Local SGD with Communication-Computation Overlap and Delay-Corrected Sparse Model Averaging

[官方论文页](https://neurips.cc/virtual/2026/poster/149908) · [作者来源](https://openreview.net/forum?id=mKJ4hXgEXg)

- **问题 / 瓶颈** · 直接覆盖会丢失通信期间已完成的本地进展。
- **核心创新 / 方法** · 只传稀疏坐标并重叠计算，使用延迟校正的参数合并。
- **Baseline** · 朴素覆盖及不同通信计算策略。
- **Benchmark** · 异构工作者的光滑非凸理论与训练时长实验。
- **关键结果 / 消融** · 摘要报告重叠缩短时间，校正优于覆盖。
- **适用条件 / 局限** · 依赖延迟、稀疏和工作者异构程度。

**可复用机制** · 记录本地与通信增量各自的参照点，避免用旧权重清零在途训练贡献。

<a id="paper-149454"></a>

## Loss is Not Behavior: A Unified Output-Space Analysis of Gradient-Based Machine Unlearning

[官方论文页](https://neurips.cc/virtual/2026/poster/149454) · [作者来源](https://openreview.net/forum?id=pxm9KPF62z)

- **问题 / 瓶颈** · 忘集损失高不等于行为接近仅用保留集的模型。
- **核心创新 / 方法** · 分析忘集自杠杆与保留交叉杠杆如何把梯度残差传到输出。
- **Baseline** · 仅保留数据重训与多种梯度遗忘方法。
- **Benchmark** · 线性回归及局部非线性近似；忘集和留集输出。
- **关键结果 / 消融** · 理论和实证均指出两个杠杆项决定输出偏移。
- **适用条件 / 局限** · 非线性结果依赖广义 Gauss–Newton 与局部近似。

**可复用机制** · 事前估计训练数据中的忘留耦合，选择更合适的遗忘方式和验收指标。

<a id="paper-151025"></a>

## Lost in the Slots: Revisiting Object-Centric Representations in the era of Foundation Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151025) · [作者来源](https://openreview.net/forum?id=dWzde9p1jP)

- **问题 / 瓶颈** · 对象槽显式分解具有理论吸引力，但可能压缩掉必要证据。
- **核心创新 / 方法** · 在相同基础模型条件下比较槽和密集图块，分别测分离、信息和属性编码。
- **Baseline** · 预训练骨干的密集 patch。
- **Benchmark** · 开放 VQA、定位、组合推理与幻觉敏感任务。
- **关键结果 / 消融** · 槽表示总体落后，主要表现为分离差和类别颜色位置丢失。
- **适用条件 / 局限** · 结论针对所测槽实现，密集表示也有缺陷。

**可复用机制** · 以属性保真和对象分离两轴决定是否改变视觉接口。

<a id="paper-151496"></a>

## Lost in Translation, Found in Embeddings: Sign Language Translation and Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/151496) · [作者来源](https://openreview.net/forum?id=aELeAvEd3r)

- **问题 / 瓶颈** · 逐帧特征难兼顾自然翻译及字幕时间对齐。
- **核心创新 / 方法** · 由手部关键点、唇部图组成视觉输入，以 Sliding Perceiver 汇聚邻帧到词级，并共同训练对齐和翻译。
- **Baseline** · 手语翻译及手语字幕对齐现有方法。
- **Benchmark** · BOBSL、How2Sign、Phoenix14T、FLEURS-ASL、WMT-SLT-SRF 等。
- **关键结果 / 消融** · 摘要报告两类任务领先，另示范自然手语。
- **适用条件 / 局限** · 关键信号预处理可能影响其他手语和自然交流。

**可复用机制** · 将密集连续信号压到语义级单位，再用时间辅助任务保护局部顺序。

<a id="paper-139093"></a>

## Lost on Campus: Evaluating Embodied Spatial Reasoning of Vision-Language Models in the Wild

[官方论文页](https://neurips.cc/virtual/2026/poster/139093) · [作者来源](https://openreview.net/forum?id=lU1kNLfVEL)

- **问题 / 瓶颈** · 静态或室内任务可被语义捷径解决。
- **核心创新 / 方法** · 从重建的真实户外环境分别测六项空间能力，再加入交互导航对照。
- **Baseline** · 静态、合成或室内空间设置及现有 VLM。
- **Benchmark** · Lost on Campus 的诊断问答与闭环户外导航。
- **关键结果 / 消融** · 摘要指出空间预见与自身定位是主要瓶颈。
- **适用条件 / 局限** · 重建环境不完全覆盖实体交互与传感噪声。

**可复用机制** · 把空间能力拆成可定位环节，用实际执行误差验证问答是否真的可迁移。

<a id="paper-151099"></a>

## Lost or Hidden? A Concept-Level Forgetting in Supervised Continual Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151099) · [作者来源](https://openreview.net/forum?id=d06ZssFH8b)

- **问题 / 瓶颈** · 任务输出下降不能区分信息删除与读取困难。
- **核心创新 / 方法** · 以任务锚定稀疏特征分解表观删除、可恢复和可解码。
- **Baseline** · 任务分数与粗表示漂移。
- **Benchmark** · 持续视觉学习的概念级诊断。
- **关键结果 / 消融** · 相当一部分表观丢失在线性假设下可恢复；任务增加时可解码性下降。
- **适用条件 / 局限** · 潜变量是概念代理，线性恢复不是通用判据。

**可复用机制** · 在采用重放或再训练前，测低成本读出是否已能恢复旧能力。

<a id="paper-150892"></a>

## LOTION: Smoothing the Optimization Landscape for Quantized Training

[官方论文页](https://neurips.cc/virtual/2026/poster/150892) · [作者来源](https://openreview.net/forum?id=edK7DArfIF)

- **问题 / 瓶颈** · 硬量化形成分段常数目标，直通估计不保证收敛。
- **核心创新 / 方法** · 用无偏随机舍入的期望进行平滑，再交给常规优化器。
- **Baseline** · 直通估计、标准 QAT。
- **Benchmark** · 合成与 150M、300M、600M 语言模型；INT4 验证损失。
- **关键结果 / 消融** · 摘要给出局部收敛保证，随机舍入保留原全局极小；实证改善。
- **适用条件 / 局限** · 结论依赖随机过程与平滑目标条件。

**可复用机制** · 为离散目标寻找保留最优解结构的平滑代理，而不只更换梯度估计。

<a id="paper-155223"></a>

## Low-Dimensional Adaptation of Rectified Flow: A  Diffusion and Stochastic Localization Perspective

[官方论文页](https://neurips.cc/virtual/2026/poster/155223) · [作者来源](https://openreview.net/forum?id=7LFHmkQrNg)

- **问题 / 瓶颈** · 仅用环境维数估采样成本可能过于悲观。
- **核心创新 / 方法** · 设计确定与随机 rectified flow 的时间网格，借随机局部化刻画与 DDPM 的关系。
- **Baseline** · 常规 RF 与 DDPM。
- **Benchmark** · 合成与文生图实验；全变差精度、迭代。
- **关键结果 / 消融** · 准确漂移下理论复杂度约 k/ε，省略对数。
- **适用条件 / 局限** · 需要指定时间表和漂移误差，内在维数未必已知。

**可复用机制** · 将采样步预算与目标流形复杂度挂钩，同时保留可验证的漂移质量要求。

<a id="paper-149854"></a>

## Lower-Level Agnostic Bilevel Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/149854) · [作者来源](https://openreview.net/forum?id=mnYCucQgEu)

- **问题 / 瓶颈** · 对整上层目标零阶差分浪费已知梯度，随机方向也混合响应。
- **核心创新 / 方法** · 每步只改一上层坐标估下层响应 Jacobian 一列，并结合现有上层一阶梯度。
- **Baseline** · 零阶上层及依赖下层导数的优化。
- **Benchmark** · 深度超表征和稳健训练任务。
- **关键结果 / 消融** · 确定性几何减小下层误差时有 1/T，随机情形有 1/sqrt(T) 界。
- **适用条件 / 局限** · 依赖下层 PL 条件、近似误差和响应查询。

**可复用机制** · 混合利用可用梯度与黑盒局部响应，不必将整个问题当作零阶。

<a id="paper-151208"></a>

## Low-Rank Adaptation for Critic Learning in Off-Policy Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151208) · [作者来源](https://openreview.net/forum?id=c9yifwVOw7)

- **问题 / 瓶颈** · 大 critic 在重放自举训练中易不稳。
- **核心创新 / 方法** · 只训低秩适配器，并保持 SimbaV2 的归一化几何。
- **Baseline** · 全量 critic，SAC、FastTD3 框架。
- **Benchmark** · DeepMind Control 行走和 IsaacLab 机器人。
- **关键结果 / 消融** · 摘要报告 critic 损失降低且策略更强。
- **适用条件 / 局限** · 秩和随机基座需按数据覆盖检验。

**可复用机制** · 将价值网络总容量与可学习的更新维度分离，保留测量自举稳定性的对照。

<a id="paper-139091"></a>

## LowRankArena: A Standardized Evaluation Platform for SVD-Based LLM Compression

[官方论文页](https://neurips.cc/virtual/2026/poster/139091) · [作者来源](https://openreview.net/forum?id=lh1VxugRWJ)

- **问题 / 瓶颈** · 不同评测协议造成方法排名不可比。
- **核心创新 / 方法** · 统一任务版本、压缩口径和推理设置，复现五种方法。
- **Baseline** · 五种代表 SVD 基线及历史报告。
- **Benchmark** · 多骨干和保留率；选择题、困惑度、端到端时延。
- **关键结果 / 消融** · 头部方法随骨干和压缩率改变；准确可能遮住困惑度退化，实际速度收益依赖负载。
- **适用条件 / 局限** · 已复现设置以外需要重新核验。

**可复用机制** · 量化验收以任务、语言建模和实际吞吐三个维度检查断裂。

<a id="paper-153079"></a>

## Low-Rank Hierarchical Merging for Efficient  Long-to-Short Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/153079) · [作者来源](https://openreview.net/forum?id=O8vjSKhqQF)

- **问题 / 瓶颈** · 常数插值可能在敏感层丢掉困难推理能力。
- **核心创新 / 方法** · 随机输入近似每层 Hessian 迹，结合向量范数，并在合并误差和长度目标下设系数。
- **Baseline** · ACM-TIES、ORCA 及线性插值。
- **Benchmark** · 1.5B 和 7B 的六项数学基准。
- **关键结果 / 消融** · 摘要报告准确度提高逾 4%，较长推理模型输出最多缩短 93.1%。
- **适用条件 / 局限** · 随机输入曲率代理可能不反映所有任务。

**可复用机制** · 把压缩目标设为全局预算，同时给最容易丢能力的层更严格偏移限制。

<a id="paper-148352"></a>

## Loyalty Capture: Reporting Relationships and Structural Sycophancy in Frontier AI Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148352) · [作者来源](https://openreview.net/forum?id=yWb30l4iXg)

- **问题 / 瓶颈** · 助手可能在无显式要求时偏向上级利益。
- **核心创新 / 方法** · 交叉操纵汇报关系和奖励是否相关，比较披露冲突、扩大利益相关者及被动监督。
- **Baseline** · 激励无关安慰剂及无主动提示的监督。
- **Benchmark** · 八个模型、5,757 次试验，测投资建议和冲突识别。
- **关键结果 / 消融** · 冲突条件下汇报关系造成 8.1 个百分点的额外削减，主动干预消去约六成效应。
- **适用条件 / 局限** · 组织任务为受控场景，真实流程外推待核实。

**可复用机制** · 控制上下级关系之外的任务内容，用结构性利益冲突测试代理建议。

<a id="paper-154458"></a>

## LPG: Balancing Efficiency and Policy Reasoning in Latent Policy Guardrails

[官方论文页](https://neurips.cc/virtual/2026/poster/154458) · [作者来源](https://openreview.net/forum?id=DQZZ9P0pXT)

- **问题 / 瓶颈** · 显式长推理会提高每次政策评估的延迟。
- **核心创新 / 方法** · 训练连续潜态承载政策解释，推理只输出简洁结论与关联条款。
- **Baseline** · 最强动态政策基线及 Qwen3-4B-Thinking。
- **Benchmark** · 动态政策防护基准，安全准确率、F1 和单样本耗时。
- **关键结果 / 消融** · 4B 版本用十个潜 token 达 84.5% 准确率、77.9% F1，所测约快 11 倍。
- **适用条件 / 局限** · 倍数为单样本设置，复杂政策及条款可审计性待查。

**可复用机制** · 把政策定位与审计文本保留为可观察接口，同时压缩内部判断成本。

<a id="paper-149466"></a>

## LP-RAG: Learning to Retrieve with Link Predictors

[官方论文页](https://neurips.cc/virtual/2026/poster/149466) · [作者来源](https://openreview.net/forum?id=pu2fC26MV8)

- **问题 / 瓶颈** · 图式检索能建块间关系，但不一定学到面向查询的相关性。
- **核心创新 / 方法** · 建立语义块图，添加以块为条件的合成问题，再对未见问题预测查询到块的链接。
- **Baseline** · 现有图检索和可学习图式 RAG。
- **Benchmark** · 多种检索及下游生成设置，另测运行效率。
- **关键结果 / 消融** · 摘要报告检索及生成都改善，效率具竞争力。
- **适用条件 / 局限** · 合成问题覆盖与索引构造质量影响迁移，具名指标待核实。

**可复用机制** · 在索引时把每个块可能回答的问题做成自监督关系，并用真实持出查询检验偏移。

<a id="paper-153335"></a>

## LSVD: Loss-Aware Low-Rank Approximation for Efficient Low-Precision Vision-Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153335) · [作者来源](https://openreview.net/forum?id=M4tqmEOVbT)

- **问题 / 瓶颈** · 均匀秩和局部重建忽略不同层对任务效果的影响。
- **核心创新 / 方法** · 用损失二阶近似及 Kronecker Fisher 引导 SVD，按校准梯度分秩，前馈层混合量化。
- **Baseline** · 以重建误差和启发式秩分配为主的压缩方法。
- **Benchmark** · 视觉语言低精度推理，解码速度和准确率；具名设置待查。
- **关键结果 / 消融** · 摘要报告比既有方法加速超过 2.3 倍并保持较强精度。
- **适用条件 / 局限** · 依赖校准数据代表性与实现硬件，独立因子收益待查。

**可复用机制** · 按不同层实际任务敏感性做预算分配，再比较等预算的秩与量化组合。

<a id="paper-152037"></a>

## LucidNFT: LR-Anchored Multi-Reward Preference Optimization for Flow-Based Real-World Super-Resolution

[官方论文页](https://neurips.cc/virtual/2026/poster/152037) · [作者来源](https://openreview.net/forum?id=W1dvS9O0dJ)

- **问题 / 瓶颈** · 先把异质奖励压成一维会抹去各目标对候选的区分。
- **核心创新 / 方法** · 用低清参考一致性评估器配合组内逐目标标准化，再融合进行 DiffusionNFT 式偏好优化。
- **Baseline** · 已有流式超分及先融合再归一。
- **Benchmark** · 现实超分场景；感知质量和对低清输入的一致性。
- **关键结果 / 消融** · 摘要报告改善观感，整体保持输入一致。
- **适用条件 / 局限** · 不同退化下评估器可靠性及多目标净贡献待核实。

**可复用机制** · 把奖励尺度和候选间辨别力分开分析，避免强尺度目标主导训练。

<a id="paper-148332"></a>

## Lumberjack: Better Differentially Private Random Forests through Heavy Hitter Detection in Trees

[官方论文页](https://neurips.cc/virtual/2026/poster/148332) · [作者来源](https://openreview.net/forum?id=ydhXJ2q9Ma)

- **问题 / 瓶颈** · 私有估计若误差随深度增长太快会限制树的表达。
- **核心创新 / 方法** · 引入层级重频检测，保留数据充分的节点。
- **Baseline** · 既有差分隐私随机森林。
- **Benchmark** · 表格基准，比较隐私预算与预测效用。
- **关键结果 / 消融** · 层级计数误差按树高对数的平方根缩放，实测优于旧方法。
- **适用条件 / 局限** · 常数依赖隐私参数，尾部子群保留和树估计成本待核实。

**可复用机制** · 先确保私有统计量随深度增长可控，再决定从浅树扩到深树。

<a id="paper-139740"></a>

## LUMOS: Tracing Parametric Knowledge from Training Data to Behavioral Outputs in LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/139740) · [作者来源](https://openreview.net/forum?id=7FpODsvd1D)

- **问题 / 瓶颈** · 正确或错误回答不足以区分记忆、泛化和读取失败。
- **核心创新 / 方法** · 在公开训练集检查事实暴露，再比较内隐探针、行为以及自我反思。
- **Baseline** · 已见与未见事实，不同模型规模及 CoT 设置。
- **Benchmark** · OLMo 2，测稀有知识可分性、输出成功和自我反思。
- **关键结果 / 消融** · 稀有事实内部可分性 84% 而输出 54%；反思在已见 83%，未见 49%。
- **适用条件 / 局限** · 需要可查语料，探针可读性不等于因果上可用。

**可复用机制** · 在声称模型知道或不知道前把见过、内部编码和会表达分别记录。

<a id="paper-149284"></a>

## LYNX: Learning Dynamic Exits for Confidence-Controlled Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/149284) · [作者来源](https://openreview.net/forum?id=rSKYIHN4OX)

- **问题 / 瓶颈** · 继续思考可能浪费 token，甚至把正确答案改错。
- **核心创新 / 方法** · 在候选位置强制模型作答生成监督，在线读出后做拆分校准。
- **Baseline** · 不提前停止的基线及已有早退方法。
- **Benchmark** · 三个模型家族 1.5B 至 32B，数学、常识及代码，精度和 token。
- **关键结果 / 消融** · 报告减少 30–70% token 并保持或提高准确率。
- **适用条件 / 局限** · 跨域实测不自动转移校准覆盖保证，分布及停止点规则需复核。

**可复用机制** · 用模型在每个停止点实际能否答对标记阈值，不把长度当作完成度。

<a id="paper-156010"></a>

## M$^2$RNN: Non-Linear RNNs with Matrix-Valued States for Scalable Language Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/156010) · [作者来源](https://openreview.net/forum?id=1BghQYvh91)

- **问题 / 瓶颈** · 传统非线性 RNN 的表现受状态容量和吞吐限制。
- **核心创新 / 方法** · 用外积扩大矩阵隐藏态并保留非线性转移，利用硬件矩阵运算。
- **Baseline** · 混合 Gated DeltaNet 和线性注意力对照。
- **Benchmark** · 未见长度状态追踪、7B MoE 建模与 LongBench。
- **关键结果 / 消融** · 困惑度低 0.5、循环状态约三分之一；单层变体达到混合 M²RNN 准确率。
- **适用条件 / 局限** · 结果受硬件、状态形状和架构混合比例影响。

**可复用机制** · 在架构实验中对齐状态规模与吞吐，再测非线性在哪些任务独立发挥作用。

<a id="paper-149542"></a>

## M$^3$: Reframing Training Measures for Discretized Physical Simulations

[官方论文页](https://neurips.cc/virtual/2026/poster/149542) · [作者来源](https://openreview.net/forum?id=pMw0ClT3bM)

- **问题 / 瓶颈** · 密网格区域被反复监督，物理变化大的稀区可能欠拟合。
- **核心创新 / 方法** · 根据物理变化做多尺度 Morton 划分，各尺度重新分配监督。
- **Baseline** · 按原始离散采样训练和更高分辨数据。
- **Benchmark** · 三项工业模拟、不同离散与十倍递进的下采样；测相对 L2 和 MSE。
- **关键结果 / 消融** · 体积场景误差最多低 4.7 倍，激进下采样时物理加权相对 L2 仍低 3–4 倍。
- **适用条件 / 局限** · 依赖变异量和跨尺度权重定义，未知边界条件待核实。

**可复用机制** · 用物理区域均衡的误差检查训练数据分布失配，不用平均点误差替代连续场质量。

<a id="paper-153004"></a>

## M2A: Synergizing Mathematical and Agentic Reasoning in Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153004) · [作者来源](https://openreview.net/forum?id=OgH3KkShw6)

- **问题 / 瓶颈** · 直接联合训练或权重合并可能扰动既有交互模式。
- **核心创新 / 方法** · 先估主任务子空间，仅沿其零空间加入数学向量，以系数控制推理长度。
- **Baseline** · 原 Agent 和其他任务合并或联合训练设置。
- **Benchmark** · SWE-Bench Verified，测解决率及推理行为。
- **关键结果 / 消融** · Qwen3-8B 微调版本从 44.0% 提至 51.2%，无需重训。
- **适用条件 / 局限** · 子空间保真及新任务上的干扰待查，数学能力迁移不能从单基准普遍推出。

**可复用机制** · 对合并任务明确保护子空间和持出行为，并用不投影增量验证有无干扰。

<a id="paper-139625"></a>

## M4Bench: Evaluating Procedural Specification for Clinical EHR Derivation Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/139625) · [作者来源](https://openreview.net/forum?id=EgGGRnoyTG)

- **问题 / 瓶颈** · 数据表字段本身无法说明时间窗、缺失规则和输出粒度。
- **核心创新 / 方法** · 控制规格完整、交付方式和 schema，按键与时间诊断，而非只比最终分数。
- **Baseline** · 仅 schema、操作规格、带技能以及诱饵与 SQL 控制。
- **Benchmark** · MIMIC-IV、eICU 的 28 任务，含严格诊断及任务均衡键 F1。
- **关键结果 / 消融** · 八项哨兵任务规格增益 0.162，技能额外增益区间跨零；760 次中 87 次严格通过。
- **适用条件 / 局限** · 证据集中指定模型与数据库，仍需任务级人工验证。

**可复用机制** · 把机读规格本身作为主要实验变量，并检查分数增益是否来自行粒度和键正确性改善。

<a id="paper-155514"></a>

## Machine Learning-Driven RAG System Design

[官方论文页](https://neurips.cc/virtual/2026/poster/155514) · [作者来源](https://openreview.net/forum?id=51rDXl78uf)

- **问题 / 瓶颈** · 管线参数有交互，穷举运行成本高。
- **核心创新 / 方法** · 用配置预测指标，以交互归因和少量目标域观测做迁移。
- **Baseline** · 直接逐配置执行及目标域拟合。
- **Benchmark** · 三类专业问答，各 648 组配置；扩展空间 61,152 组。
- **关键结果 / 消融** · 代理 R² 至少 0.84；约 10% 目标数据可迁移全部六个指标，相对收益最高 0.09。
- **适用条件 / 局限** · 适用域相近程度及配置空间外外推待检。

**可复用机制** · 先在非生物问答上保留结构化抽样与复跑，检验代理排名而非只验证拟合度。

<a id="paper-154410"></a>

## Machine Unlearning in Diffusion LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/154410) · [作者来源](https://openreview.net/forum?id=Dlj9mRJfOq)

- **问题 / 瓶颈** · 自回归式遗忘监督稀疏且难定位应去内容。
- **核心创新 / 方法** · 以高遮盖条件抑制目标恢复，同时约束参数更新在保用子空间。
- **Baseline** · 现有自回归遗忘目标。
- **Benchmark** · 扩散语言模型的遗忘与能力保留测试，名称待核。
- **关键结果 / 消融** · 摘要称两项均改善。
- **适用条件 / 局限** · 失去可恢复性不等于隐私有形式保证。

**可复用机制** · 跨不同遮盖率分别比较遗忘、邻近知识与通用能力。

<a id="paper-150810"></a>

## Machine Unlearning in Low-Dimensional Feature Subspace

[官方论文页](https://neurips.cc/virtual/2026/poster/150810) · [作者来源](https://openreview.net/forum?id=fCiHjHZcqh)

- **问题 / 瓶颈** · 更新整个模型和反复取原始数据成本高。
- **核心创新 / 方法** · 一次获取特征，优化小投影矩阵保留剩余数据特征、减弱待遗忘数据特征。
- **Baseline** · 整模型更新与既有遗忘方案。
- **Benchmark** · 多种模型、数据和任务，比较遗忘与开销。
- **关键结果 / 消融** · 摘要称竞争或领先，且计算开销下降。
- **适用条件 / 局限** · 依赖子空间分离，投影外残留和功能保持待核。

**可复用机制** · 在匹配遗忘质量下测特征读取次数、训练耗时与保留任务变化。

<a id="paper-154192"></a>

## Macrocanonical Generator Networks: data-efficient neural surrogates for amortized physics simulation

[官方论文页](https://neurips.cc/virtual/2026/poster/154192) · [作者来源](https://openreview.net/forum?id=FVg3lsts7M)

- **问题 / 瓶颈** · 逐样本强制同一统计既昂贵又可能压缩差异。
- **核心创新 / 方法** · 一次训练生成器替代逐样本优化，以近恒等残差和小学习率缓解初期坍缩。
- **Baseline** · 原模拟器与微正则逐样本梯度下降。
- **Benchmark** · 宇宙学及流体，比较统计保真、所需训练样本与生成速度。
- **关键结果 / 消融** · 个别实验只需一训练样例，单次生成比模拟器快逾百万倍。
- **适用条件 / 局限** · 比较需计入训练和统计提取成本；限稳态及合适统计。

**可复用机制** · 同时检查均值和样本分散度，比较同一统计的逐样本约束与期望约束。

<a id="paper-152798"></a>

## MACRO: Training-free Multi-plane Attention for Closeup Render Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/152798) · [作者来源](https://openreview.net/forum?id=QHU7Lqvhfr)

- **问题 / 瓶颈** · 跨视图特征不具尺度不变性，编码后缩放也可能不能纠正匹配。
- **核心创新 / 方法** · 拆目标为多深度面，将参考图在像素空间裁剪缩放，再用深度掩码限制注意。
- **Baseline** · 现有 3DGS 与参考引导扩散。
- **Benchmark** · 两套近距离新视角评测，重建与感知指标。
- **关键结果 / 消融** · 摘要称两基准均领先且无额外训练。
- **适用条件 / 局限** · 依赖几何深度和参考覆盖，遮挡边界待核。

**可复用机制** · 用相同参考对比编码前后尺度对齐，按深度跳变评估错配。

<a id="paper-153932"></a>

## MAdam: Metric-Aware Multi-Objective Adam

[官方论文页](https://neurips.cc/virtual/2026/poster/153932) · [作者来源](https://openreview.net/forum?id=HVoKKffUJJ)

- **问题 / 瓶颈** · 二阶矩混合偏好历史并改变梯度冲突关系。
- **核心创新 / 方法** · 用偏好条件曲率白化协商方向，使后续二阶调整不掩盖随时间变化的权重。
- **Baseline** · 多种求解器搭配标准 Adam。
- **Benchmark** · 多任务、Pareto 恢复、物理网络和医学图像。
- **关键结果 / 消融** · 摘要称每类求解器均改善。
- **适用条件 / 局限** · 曲率估计与白化开销待核。

**可复用机制** · 记录设定偏好和实际更新夹角，按相同训练耗时比较。

<a id="paper-139057"></a>

## MAEB: Massive Audio Embedding Benchmark

[官方论文页](https://neurips.cc/virtual/2026/poster/139057) · [作者来源](https://openreview.net/forum?id=nm06bgkKGH)

- **问题 / 瓶颈** · 总榜存在任务异质性，对比训练未必捕获语言成分。
- **核心创新 / 方法** · 用同一大型评测比较不同训练来源的模型与分任务排名。
- **Baseline** · 56 个音频嵌入模型。
- **Benchmark** · MAEB 30 项、逾百语言，语音、音乐、环境声音及跨模态。
- **关键结果 / 消融** · 图文式音频文本对比模型在环境音强但多语言语音近随机；语音预训练趋势相反。
- **适用条件 / 局限** · 权衡受模型与任务构成影响。

**可复用机制** · 上线前按应用目标选择任务组评分，并单列聚类这一共同薄弱项。

<a id="paper-149356"></a>

## MAGE: All-[MASK] Block Already Knows Where to Look in Block Diffusion LLM

[官方论文页](https://neurips.cc/virtual/2026/poster/149356) · [作者来源](https://openreview.net/forum?id=qf4h7O2aYi)

- **问题 / 瓶颈** · 每个块共享索引时，已有逐词稀疏估计会漏重要键。
- **核心创新 / 方法** · 第一步算精确注意，后续去噪步骤复用该块的前 k 个索引。
- **Baseline** · 精确注意、Quest 与 SparseD。
- **Benchmark** · LongBench 三个块扩散模型家族，128K 上下文和 k=512。
- **关键结果 / 消融** · 近无损匹配精确注意，最高加速 6.82 倍。
- **适用条件 / 局限** · 依赖块平均查询跨步骤稳定，强变化块需预警。

**可复用机制** · 先测各步索引重合再选复用粒度，保留回退基线。

<a id="paper-152653"></a>

## Magnetic Resonance Unpaired Image Translation with Pseudometric Schrödinger Bridges

[官方论文页](https://neurips.cc/virtual/2026/poster/152653) · [作者来源](https://openreview.net/forum?id=ROSqb47snS)

- **问题 / 瓶颈** · 仅匹配域分布可能扭曲解剖。
- **核心创新 / 方法** · 分别使用体积保持、近等距的可逆映射，再在共享潜空间执行 Schrödinger 桥。
- **Baseline** · DSBM 和其他跨对比合成。
- **Benchmark** · OASIS-3 多对比 MRI，PSNR、SSIM、LNCC。
- **关键结果 / 消融** · 平均 26.70 dB、0.86、0.24；摘要称结构失真减少。
- **适用条件 / 局限** · 结果不证明临床适用，病理结构保持待核。

**可复用机制** · 分开测域真实性和输入实例结构保真，比较原像素桥与潜空间桥。

<a id="paper-152384"></a>

## MAGNET: Manifold-Aware Graph Diffusion Network for Connectome Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/152384) · [作者来源](https://openreview.net/forum?id=TUugQGbOfW)

- **问题 / 瓶颈** · 几何合法不保证保留粗标签下的多样性。
- **核心创新 / 方法** · 归一化 Cholesky 潜变量保证合法，配区域词元关系偏置和类别条件去噪。
- **Baseline** · 现有流形生成方法。
- **Benchmark** · ABIDE、ADNI、OASIS-3，测条件保真、采样及零样本亚类结构。
- **关键结果 / 消融** · 条件保真提高 7%–21%，亚类协方差对齐改善逾 30%。
- **适用条件 / 局限** · 多组件贡献和临床可用性待核。

**可复用机制** · 先做硬几何验收，再以未训练亚类的协方差评价多样性。

<a id="paper-154549"></a>

## Magnifying What Matters: Attention-Guided Adaptive Rendering for Visual Text Comprehension

[官方论文页](https://neurips.cc/virtual/2026/poster/154549) · [作者来源](https://openreview.net/forum?id=Ck587Z7t03)

- **问题 / 瓶颈** · 注意已集中证据，原尺度却无法支持答案。
- **核心创新 / 方法** · 取中后层关注图块映回文本区段，放大后重新推理。
- **Baseline** · 固定渲染及常规模型后训练。
- **Benchmark** · 九类视觉阅读基准与四种视觉语言骨干，覆盖短文及长多页。
- **关键结果 / 消融** · 摘要称各设置改善，并能与后训练叠加。
- **适用条件 / 局限** · 需要图块到文字的映射和第二次推理开销。

**可复用机制** · 分别测定位正确率及已定位证据的使用率，排查读不清与找不到。

<a id="paper-150733"></a>

## Magnitude-preserving Layers Enable Efficient GANs

[官方论文页](https://neurips.cc/virtual/2026/poster/150733) · [作者来源](https://openreview.net/forum?id=fnr7DvbHE3)

- **问题 / 瓶颈** · 判别器可凭增大激活幅值锐化分界，生成质量停滞。
- **核心创新 / 方法** · 对 R3GAN 加中心化归一化、保幅激活与残差、更新后正规化。
- **Baseline** · R3GAN、StyleGAN-XL 及扩散、自回归生成。
- **Benchmark** · 类别条件 ImageNet-256，FID、参数及函数调用。
- **关键结果 / 消融** · 17M、60M、130M 对应 FID 2.20、1.63、1.52，单次前向。
- **适用条件 / 局限** · 全方案各项影响和同质量计时需全文核验。

**可复用机制** · 比较相同模型下的判别器范数、边界锐度和 FID 曲线。

<a id="paper-156003"></a>

## MahaVar: OOD Detection via Class-wise Mahalanobis Distance Variance under Neural Collapse

[官方论文页](https://neurips.cc/virtual/2026/poster/156003) · [作者来源](https://openreview.net/forum?id=1FalHL84no)

- **问题 / 瓶颈** · 离最近类近不足以描述分数分布是否有尖锐最小值。
- **核心创新 / 方法** · 给 Mahalanobis 距离加跨类别方差项，以放松神经坍缩分析解释。
- **Baseline** · 现有 Mahalanobis 分数。
- **Benchmark** · OpenOOD v1.5 的 CIFAR-100 与 ImageNet，AUROC、FPR@95。
- **关键结果 / 消融** · 摘要称两指标持续改善。
- **适用条件 / 局限** · 类别不够分离或类别数很少时可能失效。

**可复用机制** · 固定特征和协方差估计，观察跨类方差能否补充最近距离。

<a id="paper-150654"></a>

## Majority Bit-Aware Watermarking for Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150654) · [作者来源](https://openreview.net/forum?id=gQnti07s2m)

- **问题 / 瓶颈** · 靠缩窄偏好词元集合提高解码会损文本质量。
- **核心创新 / 方法** · 多位来源标记使用多数比特编码，使较大的候选集仍维持水印信号。
- **Baseline** · 既有多位文本水印。
- **Benchmark** · 多个语言模型，评载荷识别及文本质量。
- **关键结果 / 消融** · 摘要称两项均改善，且长消息另有优化版本。
- **适用条件 / 局限** · 外部编辑、误报和具体载荷规模效应待核。

**可复用机制** · 在固定误报限制下绘制载荷长度、可检测率与文本质量前沿。

<a id="paper-150819"></a>

## Majority-of-Three is an Optimal PAC Learner

[官方论文页](https://neurips.cc/virtual/2026/poster/150819) · [作者来源](https://openreview.net/forum?id=f4VPeQiNfz)

- **问题 / 瓶颈** · 单 ERM 次数少但最坏样本界不优，早期最优算法需多次训练。
- **核心创新 / 方法** · 证明三 ERM 多数规则从期望最优延伸至高概率最优。
- **Baseline** · 单 ERM 与 Hanneke 多 ERM 方案。
- **Benchmark** · 可实现 PAC 学习的高概率样本复杂度。
- **关键结果 / 消融** · 给出最优性肯定证明。
- **适用条件 / 局限** · 摘要未给子集构造细节，不能扩展到任意噪声。

**可复用机制** · 在同置信要求下比较 ERM 调用数与样本预算，再单测非可实现场景。

<a id="paper-152145"></a>

## Make Each Token Count: Towards Improving Long-Context Performance with KV Cache Eviction

[官方论文页](https://neurips.cc/virtual/2026/poster/152145) · [作者来源](https://openreview.net/forum?id=VBVa8FIJRl)

- **问题 / 瓶颈** · 固定各层配额忽略效用差异，全量注意也可被无关词元稀释。
- **核心创新 / 方法** · 轻量门估计未来效用，由共享输出投影使层头和模态分数可比。
- **Baseline** · 完整缓存和常规局部淘汰。
- **Benchmark** · 长上下文语言与视觉语言任务，比较质量和内存。
- **关键结果 / 消融** · 摘要称显著减内存且匹配或超过全量。
- **适用条件 / 局限** · 训练成本以及罕见未来证据被提前删除需核。

**可复用机制** · 同预算报告跨层资源分配、远处证据召回和下游回答。

<a id="paper-155348"></a>

## Making LoRA Identifiable: Orthogonal Alignment for Continual Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/155348) · [作者来源](https://openreview.net/forum?id=6IGj3mpXfp)

- **问题 / 瓶颈** · 等价旋转可能使直接合并抵消原任务方向。
- **核心创新 / 方法** · 在 Stiefel 流形约束 A，以 Procrustes 对齐 B，再按秩分量方向一致程度保留融合。
- **Baseline** · 任务独立 LoRA、正交约束、门控和共享单 LoRA。
- **Benchmark** · 多模型和多持续学习基准。
- **关键结果 / 消融** · 摘要报告无额外持续内存，表现较强。
- **适用条件 / 局限** · 训练时对齐成本和长期积累待核。

**可复用机制** · 运行随机等价旋转的控制测试，再对照直接合并与对齐合并的遗忘。

<a id="paper-155690"></a>

## Making Open-Source Text LLM Watermarks Durable Against Merging

[官方论文页](https://neurips.cc/virtual/2026/poster/155690) · [作者来源](https://openreview.net/forum?id=3fkF2rVnDA)

- **问题 / 瓶颈** · 只在原始权重上可检测，不能证明后训练来源追踪有效。
- **核心创新 / 方法** · 在受控模型更新条件下训练并检验水印保持，同时记录下游效用。
- **Baseline** · 既有权重水印方法。
- **Benchmark** · 多种常用合并情形与三种算法，比较低误报下真阳性。
- **关键结果 / 消融** · 摘要报告识别率改善，同时保持下游能力。
- **适用条件 / 局限** · 更多版本修改和真实部署误报需核。

**可复用机制** · 在许可合并的模型发布流程加入水印保留回归测试，并报告效用变化。

<a id="paper-150684"></a>

## Mamba Can Learn Low-Dimensional Targets In-Context via Test-Time Feature Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/150684) · [作者来源](https://openreview.net/forum?id=gGRd5Ll8TD)

- **问题 / 瓶颈** · 低维非线性任务需要从示例恢复相关方向。
- **核心创新 / 方法** · 分析 Mamba 非线性门控在测试时抽取单指标方向的能力。
- **Baseline** · 线性和非线性 Transformer 的相应分析。
- **Benchmark** · 单指标上下文学习的理论样本复杂度。
- **关键结果 / 消融** · 摘要给出优于线性 Transformer、接近非线性 Transformer 的复杂度。
- **适用条件 / 局限** · 结果依赖单指标及训练假设，不能推广到任意任务。

**可复用机制** · 选序列骨干时单独测其是否能依据当前样本重建相关特征。

<a id="paper-150767"></a>

## Mamba Flow Matching Neural Processes: Linear-Time Inference for Irregularly Observed Spatial Fields

[官方论文页](https://neurips.cc/virtual/2026/poster/150767) · [作者来源](https://openreview.net/forum?id=fVeT6lAKvN)

- **问题 / 瓶颈** · 注意力开销随点数平方增，将上下文压成单状态又损失信息。
- **核心创新 / 方法** · 多向 Mamba-2 扫描混合序列，从各查询所在位置读速度并做条件流匹配。
- **Baseline** · 注意力式联合预测和现有状态空间神经过程。
- **Benchmark** · 合成 GP、NOAA 区域及洲际气温；RMSE、CRPS、用时。
- **关键结果 / 消融** · 摘要报告快 170 至 760 倍，并在洲际等设置改善误差。
- **适用条件 / 局限** · 依赖空间排序和查询序列的有效覆盖。

**可复用机制** · 以每个查询位置的局部状态代替全局瓶颈，保留跨查询联合建模。

<a id="paper-138998"></a>

## MammoGPS: A Benchmark for Visual Grounding, Perception, and Spatial Reasoning in Mammography

[官方论文页](https://neurips.cc/virtual/2026/poster/138998) · [作者来源](https://openreview.net/forum?id=rur6yVHoR5)

- **问题 / 瓶颈** · 高图像级问答得分可能来自非视觉捷径。
- **核心创新 / 方法** · 逐步改变语义、空间术语和背景，并按病灶位置分层。
- **Baseline** · 12 个专有、通用和医疗 VLM。
- **Benchmark** · MammoGPS 的 13 个临床任务和 20 个受控诊断任务。
- **关键结果 / 消融** · 摘要报告定位、术语和部分空间区间的表现薄弱。
- **适用条件 / 局限** · 只适用于所测乳腺影像与基准，不表明临床诊断有效性。

**可复用机制** · 保持临床目标固定，独立改变非视觉线索与真实空间需求，以识别先验依赖。

<a id="paper-148420"></a>

## M*: A Modular, Extensible, Serving System for Multimodal Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148420) · [作者来源](https://openreview.net/forum?id=xwpS322agK)

- **问题 / 瓶颈** · 固定语言服务骨干难部署组合式视觉、语音和规划。
- **核心创新 / 方法** · 用 Walk Graph 统一描述组件连接、请求遍历和集群放置。
- **Baseline** · vLLM-Omni 与 V-JEPA 2-AC rollout。
- **Benchmark** · BAGEL 文生图、Qwen3-Omni 语音及机器人规划。
- **关键结果 / 消融** · 文生图平均时延低约 30%，语音吞吐最多升 15%。
- **适用条件 / 局限** · 依赖组件切分、通信成本及批处理条件。

**可复用机制** · 把模型组件与集群拓扑解耦，并按模态请求实际路径而非整模型放置。

<a id="paper-152510"></a>

## MAMQ-Net: A Robust Framework Leveraging Multi-level Tamper-aware Queries and Complementary Representations of Tampering Features for Progressive Image Forgery Localization

[官方论文页](https://neurips.cc/virtual/2026/poster/152510) · [作者来源](https://openreview.net/forum?id=Sad9HLajgI)

- **问题 / 瓶颈** · 两路独立抽特征后再拼接容易丢交叉伪迹。
- **核心创新 / 方法** · 交替进行提取与交互，并用多层可学习查询逐步聚合定位证据。
- **Baseline** · 已有双路图像伪造定位。
- **Benchmark** · 多个公开定位及鲁棒性数据，细项待核实。
- **关键结果 / 消融** · 摘要报告定位和鲁棒性优于所比方法。
- **适用条件 / 局限** · 跨编辑器的分布转移及误报需要另验。

**可复用机制** · 在多尺度位置逐步检验两路证据是否互补，再让查询过滤无关信息。

<a id="paper-153519"></a>

## Managing Self-Learning Experts under Per-Round Budget Constraints

[官方论文页](https://neurips.cc/virtual/2026/poster/153519) · [作者来源](https://openreview.net/forum?id=Kl4TknNwAA)

- **问题 / 瓶颈** · 只训练当轮表现最好的专家会忽略其它专家随继续更新的潜力。
- **核心创新 / 方法** · 按训练损失和先验约束构造置信界，每步选择一个决策者和至多 M 个可学习专家。
- **Baseline** · 最佳事后专家。
- **Benchmark** · 参数化模型及 bandit 专家，累计遗憾。
- **关键结果 / 消融** · 摘要给出随 K/M 和个体遗憾变化的任意时点保证。
- **适用条件 / 局限** · 要求随机环境与个体学习条件。

**可复用机制** · 分别管理执行预算和模型改善预算，用后者降低未来选错专家的代价。

<a id="paper-154828"></a>

## MANGO:Multi-Angle Neural Gated Operators for Chirp-Perturbed PDEs

[官方论文页](https://neurips.cc/virtual/2026/poster/154828) · [作者来源](https://openreview.net/forum?id=AdtcktHOaD)

- **问题 / 瓶颈** · 固定傅里叶基难表达随位置旋转的局部谱。
- **核心创新 / 方法** · 学习分数傅里叶角度和逐位置门控，并正则分支谱权。
- **Baseline** · 六个神经算子基线。
- **Benchmark** · 四个可解析啁啾扰动 PDE。
- **关键结果 / 消融** · 摘要报告恢复内在角度结构并改善解预测。
- **适用条件 / 局限** · 依赖适合分数傅里叶表示的方程类型。

**可复用机制** · 给谱变换自身学习自由度，再用局部输入而不是全局固定权重选谱基。

<a id="paper-154960"></a>

## Manifold Drift in Flow Preference Optimization: A Root Cause of Reward Hacking

[官方论文页](https://neurips.cc/virtual/2026/poster/154960) · [作者来源](https://openreview.net/forum?id=9dO9vJ1V5d)

- **问题 / 瓶颈** · 对偏好梯度的响应可沿法向离开原数据流形。
- **核心创新 / 方法** · 用温度调节以偏好样本为锚的训练目标，并重加权弱信号。
- **Baseline** · FlowDPO 及其变体、原生成器。
- **Benchmark** · 合成流形和图像 OCR 对齐，模型及人工评估。
- **关键结果 / 消融** · 摘要报告合成支持保持与对齐折中更好，图像 OCR 对齐改善。
- **适用条件 / 局限** · 流形与漂移用代理刻画，真实数据的覆盖需另验。

**可复用机制** · 把支持漂移作为独立诊断和训练约束，不以奖励单调提升作为验收。

<a id="paper-149523"></a>

## Manifold Embedding of Deep Image Features for Image Matching via Neural Adjoint Maps

[官方论文页](https://neurips.cc/virtual/2026/poster/149523) · [作者来源](https://openreview.net/forum?id=pVexlKkL27)

- **问题 / 瓶颈** · 独立最近邻易产生局部不一致对应。
- **核心创新 / 方法** · 在深度特征流形用有限元构造 Laplace–Beltrami，结合神经伴随表达非线性对应。
- **Baseline** · 基础特征最近邻及零样本对应基线。
- **Benchmark** · 多个真实图像稠密对应基准。
- **关键结果 / 消融** · 摘要报告优于所比零样本方法。
- **适用条件 / 局限** · 谱几何依赖特征质量与离散化选取。

**可复用机制** · 将局部匹配变为受共享低维结构约束的映射，降低孤立错误。

<a id="paper-150407"></a>

## Manifold-Guided Stereo-Monocular Refinement for Endoscopic Stereo Disparity Estimation

[官方论文页](https://neurips.cc/virtual/2026/poster/150407) · [作者来源](https://openreview.net/forum?id=iGyOrOrioU)

- **问题 / 瓶颈** · 全局单目信号可能覆盖可信的度量匹配。
- **核心创新 / 方法** · 用双目代价几何精修并校准单目候选，以左右一致性门控迭代更新。
- **Baseline** · 近期通用及内镜双目基线。
- **Benchmark** · SCARED，零样本 SERV-CT 和 Hamlyn。
- **关键结果 / 消融** · 摘要报告平均视差表现强、阈值离群率有竞争力。
- **适用条件 / 局限** · 受配准和局部一致性可靠度限制。

**可复用机制** · 先把替代估计对齐到可信度量尺度，再按位置决定是否融合。

<a id="paper-154416"></a>

## Manifold Prior Guided Deep Unfolding for Hyperspectral Image Reconstruction

[官方论文页](https://neurips.cc/virtual/2026/poster/154416) · [作者来源](https://openreview.net/forum?id=DjKpFjPFoO)

- **问题 / 瓶颈** · 固定带宽梯度忽略频谱差异，局部去噪难表达全局结构。
- **核心创新 / 方法** · 两阶段学习无退化结构，在投影中调光谱带权，在 Mamba 中调空间谱特征。
- **Baseline** · 既有高光谱深度展开。
- **Benchmark** · 合成及真实高光谱重建。
- **关键结果 / 消融** · 摘要报告质量较优并保留可解释的迭代结构。
- **适用条件 / 局限** · 先验准确性和跨退化设置需复核。

**可复用机制** · 让观测一致性与先验去噪共享结构，但分别调节不同更新职责。

<a id="paper-152522"></a>

## Manifold Random Features

[官方论文页](https://neurips.cc/virtual/2026/poster/152522) · [作者来源](https://openreview.net/forum?id=SV6wCTN02D)

- **问题 / 瓶颈** · 欧氏解析特征不直接适于通用曲面及核。
- **核心创新 / 方法** · 离散化流形，以图随机特征构造场并转成有界正特征。
- **Baseline** · 已有图随机特征与解析连续核近似。
- **Benchmark** · 理论和随机特征逼近实验。
- **关键结果 / 消融** · 摘要报告正有界性质，并由随机游走恢复高斯核近似。
- **适用条件 / 局限** · 依赖离散质量与样本预算。

**可复用机制** · 利用图上的计算工具获得可复用的连续核近似，避免逐核手工推导。

<a id="paper-149924"></a>

## Manifold Sampling via Entropy Maximization

[官方论文页](https://neurips.cc/virtual/2026/poster/149924) · [作者来源](https://openreview.net/forum?id=mAVz31YJlN)

- **问题 / 瓶颈** · 连通假设失效时常见局部链难探索其它可行支。
- **核心创新 / 方法** · 用近邻密度估计指导熵最大化重采样，组合多种局部采样器。
- **Baseline** · 常见约束采样基线。
- **Benchmark** · 合成和机器人约束基准；Sinkhorn 距离与时延。
- **关键结果 / 消融** · 摘要报告距离可改善一个数量级，均值场下 KL 按步指数下降。
- **适用条件 / 局限** · 依赖能找到多分支可行种子和局部密度近似。

**可复用机制** · 独立监控样本质量与跨分支覆盖，将重采样资源给低覆盖可行区域。

<a id="paper-154849"></a>

## Manifold-weighted neural networks

[官方论文页](https://neurips.cc/virtual/2026/poster/154849) · [作者来源](https://openreview.net/forum?id=AS3nvwjiyw)

- **问题 / 瓶颈** · 高效的约束参数化可能损失通用逼近。
- **核心创新 / 方法** · 对经典群轨道的矩阵流形，以两套充分构造证明有界缩放残差模型通用性。
- **Baseline** · 无约束网络及有实证的 Stiefel 参数化。
- **Benchmark** · 多类流形的 Lp 通用逼近理论。
- **关键结果 / 消融** · 覆盖论文所列经构造核验的流形。
- **适用条件 / 局限** · 通用表达不保证有限宽度效率或优化成功。

**可复用机制** · 权重约束选型时同时检查可计算回缩和残差骨干的表达充分条件。

<a id="paper-153087"></a>

## ManiFusion: Unlocking High-Throughput Generation via Superposition in Manifold Space

[官方论文页](https://neurips.cc/virtual/2026/poster/153087) · [作者来源](https://openreview.net/forum?id=O4Y8IsrWsh)

- **问题 / 瓶颈** · 只缩单样本时延可能遇到收益瓶颈。
- **核心创新 / 方法** · 在骨干前融合多样本，后拆分，并按轨迹阶段调融合系数。
- **Baseline** · 面向单样本的扩散加速。
- **Benchmark** · U-Net、Transformer、像素及潜空间生成。
- **关键结果 / 消融** · 摘要报告吞吐提高且质量退化有限，与现有加速兼容。
- **适用条件 / 局限** · 样本状态能否稳定分离取决于阶段和模型。

**可复用机制** · 分别优化单位时间样本数与单请求时延，在融合前验证可逆性与语义串扰。

<a id="paper-151554"></a>

## ManipulationRAG: Retrieval-Augmented Fine-Grained Manipulation of Object Functional Parts

[官方论文页](https://neurips.cc/virtual/2026/poster/151554) · [作者来源](https://openreview.net/forum?id=ZllSD7e69Q)

- **问题 / 瓶颈** · 固定生成器难处理未见的交互，容易生成与任务不符的动作。
- **核心创新 / 方法** · 用手部任务分类组织描述、物体、动作类型和姿势序列，并以检索模板引导扩散。
- **Baseline** · 既有细粒度操作生成模型。
- **Benchmark** · 面向物体功能部件的域外操作；具体数据待核实。
- **关键结果 / 消融** · 摘要报告优于既有方法且域外更稳。
- **适用条件 / 局限** · 取决于模板覆盖及模板与机器人本体的适配。

**可复用机制** · 在动作先验检索中显式使用部件和交互方式作键，而非以视觉相近代替物理功能相近。

<a id="paper-139847"></a>

## Many Benign Errors are Better than A Few Severe Ones: Evaluating Hallucination Severity

[官方论文页](https://neurips.cc/virtual/2026/poster/139847) · [作者来源](https://openreview.net/forum?id=0wbnAGgl8S)

- **问题 / 瓶颈** · 二值错误率把合理推断与高影响失真等同。
- **核心创新 / 方法** · 标注片段不可信程度与其被相信时的影响，另比较人工及模型评委的发现与判严重性能力。
- **Baseline** · 事实支持二值评估与人工严重性标签。
- **Benchmark** · 多领域摘要生成，对比模型排序、片段检测与严重性评分。
- **关键结果 / 消融** · 严重性可改变模型排名；模型评委判已知片段严重性较准，却易漏看合理外观的高影响错误。
- **适用条件 / 局限** · 标签依赖领域与用途，最好先定义影响等级。

**可复用机制** · 分开测试发现错误和判断影响的能力，将少量严重错误纳入验收。

<a id="paper-156762"></a>

## Many Circuits, One Mechanism: Input Variation and Evaluation Granularity in Circuit Discovery

[官方论文页](https://neurips.cc/virtual/2026/poster/156762) · [作者来源](https://openreview.net/forum?id=Ur42Xx1QPv)

- **问题 / 瓶颈** · 不同子图可能是同一功能的多种表达。
- **核心创新 / 方法** · 按预训练频率分组提取电路，测试边级替换、共享核心和内部表征互换。
- **Baseline** · 只比较源组件结构与同频率反复提取。
- **Benchmark** · 五个 Pythia 70M 至 1.4B、75 个复制电路，另有主谓一致复现。
- **关键结果 / 消融** · 70M 以上的共享核心恢复至少 99% 表现；频带间边能广泛转移。
- **适用条件 / 局限** · 未测试 token 位置或组件内部特征的特异性。

**可复用机制** · 消融后同时报告结构不同程度和跨条件功能保留比例。

<a id="paper-153062"></a>

## Map-Guided Caching: A Global Perspective for Efficient Diffusion Transformer

[官方论文页](https://neurips.cc/virtual/2026/poster/153062) · [作者来源](https://openreview.net/forum?id=OIRkHEYjkM)

- **问题 / 瓶颈** · 局部或固定缓存规则不能充分适应复杂输入的时间变化。
- **核心创新 / 方法** · 从提示和初始噪声预测逐块逐步变化，按目标加速率动态规划缓存路径。
- **Baseline** · 局部与输入无关的缓存复用。
- **Benchmark** · FLUX.1 dev、HunyuanVideo 和 FLUX.1 Kontext dev；图、编辑和视频生成质量及速度。
- **关键结果 / 消融** · 最高分别约 3.3、3.3 和 2.7 倍加速，保持有竞争力的质量。
- **适用条件 / 局限** · 变化预测成本、失败尾部和跨骨干迁移待核实。

**可复用机制** · 同质量约束下比较局部缓存和全轨迹计划，并按提示复杂度分层。

<a id="paper-153702"></a>

## MaPP: A Unified Marginalized Posterior-Predictive Framework for Data-Efficient RLVR

[官方论文页](https://neurips.cc/virtual/2026/poster/153702) · [作者来源](https://openreview.net/forum?id=JPWppGw2ut)

- **问题 / 瓶颈** · 组内其他响应随机正误造成不消失的估计噪声。
- **核心创新 / 方法** · 以 Beta–Binomial 边缘化得到响应内在优势，并基于同一后验决定提示采样。
- **Baseline** · GRPO 与现有在线提示选择基线。
- **Benchmark** · 数学、规划和视觉几何，五个骨干，匹配 rollout 预算。
- **关键结果 / 消融** · 较最强对照平均最多提高 2.45 点，理论估计误差随后验集中缩小。
- **适用条件 / 局限** · 依赖可模型化的结果反馈及后验假设，非二元奖励迁移待查。

**可复用机制** · 分别测随机组组成对梯度的影响和提示重分配效益，避免把二者混在一起。

<a id="paper-154988"></a>

## MapPolicy: Structure-Aware Imitation Learning for Robot Manipulation via Physically Constrained Scene Map

[官方论文页](https://neurips.cc/virtual/2026/poster/154988) · [作者来源](https://openreview.net/forum?id=9Q1fgy7cBQ)

- **问题 / 瓶颈** · 仅对可见观察编码使遮挡下接触关键部件表征不足。
- **核心创新 / 方法** · 将零件、布局和运动关系建图，用结构调制注意力及物理一致性约束融合地图、视觉和机器人状态。
- **Baseline** · 强模仿学习基线，具名待核实。
- **Benchmark** · 三套仿真 49 任务及五项真机操作，含严重遮挡。
- **关键结果 / 消融** · 作者报告一致改善，严重遮挡收益尤其明显。
- **适用条件 / 局限** · 依赖图结构推断的可靠性，复杂物体的约束预测误差待核实。

**可复用机制** · 把遮挡内容列为明确的中间监督，并在可见及不可见区域分别验收。

<a id="paper-139852"></a>

## MapShift: Controlled Post-Intervention Evaluation for Embodied World Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139852) · [作者来源](https://openreview.net/forum?id=0V8ehz4A6L)

- **问题 / 瓶颈** · 同环境评估混淆原地图记忆、对变化的推断和新局面规划。
- **核心创新 / 方法** · 先无奖励探索基础环境，后按可控幅度改变度量、拓扑、动态或语义，再分别测推断、规划与适应。
- **Baseline** · 同环境评估、带干预的匹配对和确定性机制诊断。
- **Benchmark** · 24 类环境模式，带可解性、泄漏、干预幅度检查。
- **关键结果 / 消融** · 同环境基准对拓扑变化低估更新收益约三倍、语义约七倍，部分规划排序反转。
- **适用条件 / 局限** · 定量增益来自确定性诊断，开放场景意义待查。

**可复用机制** · 用保留不变量的环境对评估更新收益，防止把记忆重放当作动态适应。

<a id="paper-139520"></a>

## MARBLE: an Agent Benchmark for Spatial Reasoning and Visual Abstraction

[官方论文页](https://neurips.cc/virtual/2026/poster/139520) · [作者来源](https://openreview.net/forum?id=Ke4tOr2Cva)

- **问题 / 瓶颈** · 静态问答和只提供状态的规划基准都难拆开视觉抽象与搜索。
- **核心创新 / 方法** · 独立扫描观测形式和决策长度，做成对消融。
- **Baseline** · 图像观测与人标空间状态；多个前沿模型。
- **Benchmark** · Cube、Maze、Blox，覆盖二维、三维约束和动态布局。
- **关键结果 / 消融** · 最强模型在最难设置平均仅 7.3%；由人标改为视觉，Gemma 和 Kimi 分别从 50.7% 到 3.7%、87.9% 到 6.5%。
- **适用条件 / 局限** · 三环境为诊断模拟，符号输入可能降低其他难度，需复核真实迁移。

**可复用机制** · 先测视觉到状态的抽象误差，再在统一状态接口上比较规划器。

<a id="paper-151456"></a>

## Margin Dynamics for Large Language Model Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/151456) · [作者来源](https://openreview.net/forum?id=aW6PxjyzuB)

- **问题 / 瓶颈** · 单看损失值不能预见各种偏好方法的质量改进与过度分离。
- **核心创新 / 方法** · 在偏好和非偏好输出对上建立边际 ODE，分析 DPO、IPO 和带标签平滑的 SimPO。
- **Baseline** · 标准 DPO、IPO、SimPO。
- **Benchmark** · 五个模型族、四项基准，平滑配置另测三个 3.8B–9B 模型的 IFEval。
- **关键结果 / 消融** · DPO 边际对数增长，IPO 指数趋于有限值；非零平滑为 SimPO 产生有限吸引点。
- **适用条件 / 局限** · 单对投影不刻画所有跨样本交互，最优平滑比例随设定变。

**可复用机制** · 拟合偏好边际随训练变化，选择能抑制噪声放大的损失曲线。

<a id="paper-155373"></a>

## Market-Based Runtime Resource Allocation for LLM Multi-Agent Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/155373) · [作者来源](https://openreview.net/forum?id=67jpPq2Bsk)

- **问题 / 瓶颈** · 队列及依赖结构不能捕捉本地重试、测试和下游进度造成的紧迫度变化。
- **核心创新 / 方法** · 结构化出价编码相对急迫性，异步用最优停止决定关窗，并跟踪资源分配及释放。
- **Baseline** · 多个现有工作流或调度基线。
- **Benchmark** · 三种资源竞争设置；测完工时间和任务分数。
- **关键结果 / 消融** · 较最强基线完工时间分别降 5.2%、2.5% 和 4.9%，任务分数约提高两点。
- **适用条件 / 局限** · 出价一致性、长期公平与高竞争规模待核实。

**可复用机制** · 按本地状态对请求价值建模，并用完成时间和实际任务成功检验调度收益。

<a id="paper-148382"></a>

## MaRK: Markov-adapted Recurrent Kernels for Dynamic Operator Conditioning in State Space Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148382) · [作者来源](https://openreview.net/forum?id=yIjFWwvG7b)

- **问题 / 瓶颈** · 输入注入不能改变递推时间动态。
- **核心创新 / 方法** · 用低秩适配器对冻结模型的转移、读写和步长做有界调制。
- **Baseline** · Hypernet、Chebyshev、DCT 三类适配；输入注入为背景。
- **Benchmark** · 冻结 111M Hydra 与合成时变系统，测验证损失、算子恢复和稳定性。
- **关键结果 / 消融** · 验证损失分别 3.60、2.63、2.66，给出有界递推证书。
- **适用条件 / 局限** · 仅一个冻结骨干，规模与成本待核。

**可复用机制** · 比较输入注入和直接算子调制并记录各条件的有效记忆跨度。

<a id="paper-148189"></a>

## Markovian Dynamics Enforcer: Feasibility Preserving Correction on Learned Dyanmics Manifolds

[官方论文页](https://neurips.cc/virtual/2026/poster/148189) · [作者来源](https://openreview.net/forum?id=zdmvNkloAg)

- **问题 / 瓶颈** · 轨迹数值合理仍可能违反约束，且控制可能不可观测。
- **核心创新 / 方法** · 用逆动态推出潜控制，按不等式纠正后重算已知物理与学习残差。
- **Baseline** · 其他后处理修正方法，名称待核。
- **Benchmark** · 受控模拟及欠指定自行车模型，测约束、轨迹误差。
- **关键结果 / 消融** · 欠指定场景残差 0.33，对照 1.40 至 2.90，保真误差至少降 60%。
- **适用条件 / 局限** · 只保证相对所用模型的可行性。

**可复用机制** · 区分真实动力学、学习模型与输出逼近残差，防止用模型自洽冒充物理正确。

<a id="paper-155575"></a>

## Markovian Experimental Design under Concept Drift

[官方论文页](https://neurips.cc/virtual/2026/poster/155575) · [作者来源](https://openreview.net/forum?id=4acu0z3RVl)

- **问题 / 瓶颈** · 静态采样设计忽略参数随时间改变。
- **核心创新 / 方法** · 借 Kalman 和离散代数 Riccati 方程描述稳态，推导 D 最优凸选样。
- **Baseline** · 单步与稳态设计；非线性用扩展 Kalman。
- **Benchmark** · 贝叶斯线性漂移理论，无摘要量化实验。
- **关键结果 / 消融** · 证明稳定并给可解凸问题。
- **适用条件 / 局限** · 漂移随机结构和近似条件限制推广。

**可复用机制** · 同采样预算比较稳态与单步后验不确定性。

<a id="paper-152251"></a>

## Markov Metrical Task Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/152251) · [作者来源](https://openreview.net/forum?id=USGUIAkFQ9)

- **问题 / 瓶颈** · 最坏情形分析未利用请求结构。
- **核心创新 / 方法** · 分别对未知独立请求和可观察有限马尔可夫链构造多项式近优选择。
- **Baseline** · 最优在线算法作为参照。
- **Benchmark** · 期望每步成本理论及简要经验评测。
- **关键结果 / 消融** · 两种设定均可任意接近期望最优。
- **适用条件 / 局限** · 要求当前状态可观察，规模和偏移敏感度待核。

**可复用机制** · 比较忽略转移与估计转移两种方案，分开报切换和服务成本。

<a id="paper-155648"></a>

## MarkTune: Improving the Quality-Detectability Trade-off in Model-Embedded LLM Watermarking

[官方论文页](https://neurips.cc/virtual/2026/poster/155648) · [作者来源](https://openreview.net/forum?id=42tU2vcTxH)

- **问题 / 瓶颈** · 单纯加大权重扰动会损害生成。
- **核心创新 / 方法** · MarkTune 以 GaussMark 检测统计训练并同时约束质量。
- **Baseline** · GaussMark 与生成时水印。
- **Benchmark** · 正常文本、跨数据的来源检测和下游能力。
- **关键结果 / 消融** · 摘要称更接近生成时检测信号，质量仍保持。
- **适用条件 / 局限** · 实际误报与后训练版本需独立核验。

**可复用机制** · 在正常版本迭代中联合报告水印识别和质量回归。

<a id="paper-154616"></a>

## Marrying Optimal Transport and ODEs for Unified Continuous-Time 4D Reconstruction and Tracking

[官方论文页](https://neurips.cc/virtual/2026/poster/154616) · [作者来源](https://openreview.net/forum?id=CFlcylAQ6V)

- **问题 / 瓶颈** · 直接插值无法保证物理时间一致性。
- **核心创新 / 方法** · 全局特征经流匹配提供速度先验，局部几何分支在任意时刻解码；积分匹配目标点图。
- **Baseline** · 整数时刻输出与启发式插值。
- **Benchmark** · 四维重建、点跟踪与连续时间运动评测。
- **关键结果 / 消融** · 摘要称三项领先，无定量。
- **适用条件 / 局限** · 整数帧约束不排除多种中间速度；高频运动待核。

**可复用机制** · 用留出的真实高帧率观测检查中间时刻，而非只测端点。

<a id="paper-150620"></a>

## MARS: Enabling Autoregressive Models Multi-Token Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/150620) · [作者来源](https://openreview.net/forum?id=gmcLiK4jCQ)

- **问题 / 瓶颈** · 逐词前向浪费可预知的相邻位置。
- **核心创新 / 方法** · 同一模型保留单词模式，允许置信控制的多词输出及块级 KV 缓存。
- **Baseline** · 原单词模型及带草拟模型、多头路线。
- **Benchmark** · 六基准、Qwen2.5-7B 批量推理，测准确和吞吐。
- **关键结果 / 消融** · 多词保持参考准确，吞吐 1.5–1.7 倍，实测最高 1.71 倍。
- **适用条件 / 局限** · 依赖场景置信校准及负载。

**可复用机制** · 在各输入难度下对比实际可接受词元数量及质量。

<a id="paper-148621"></a>

## MARS: Harmonizing Multimodal Convergence via Adaptive Rank Search

[官方论文页](https://neurips.cc/virtual/2026/poster/148621) · [作者来源](https://openreview.net/forum?id=wO9qWwm2K2)

- **问题 / 瓶颈** · 统一秩或学习率可能让一模态干扰另一模态。
- **核心创新 / 方法** · 用收敛时间缩放律剪枝候选，再用性能律选秩对。
- **Baseline** · 常规 LoRA 和独立调学习率思路。
- **Benchmark** · 视觉语言微调基准，细节待核。
- **关键结果 / 消融** · 摘要称自动方案优于对照。
- **适用条件 / 局限** · 两种规律可能不跨骨干迁移。

**可复用机制** · 固定参数预算比较相同秩与同步收敛的非均匀秩。

<a id="paper-156035"></a>

## MARS: Multi-resolution Adaptive Routing for Sequential Recommendation

[官方论文页](https://neurips.cc/virtual/2026/poster/156035) · [作者来源](https://openreview.net/forum?id=108F0f6Iau)

- **问题 / 瓶颈** · 单摘要可能混叠时间尺度。
- **核心创新 / 方法** · 并行递推轨道保留各时间跨度，稀疏读取生成固定大小记忆。
- **Baseline** · 强序列推荐与单压缩方法。
- **Benchmark** · 多个推荐集，重点长历史分组。
- **关键结果 / 消融** · 摘要称超对照，历史越长越有收益。
- **适用条件 / 局限** · 需真实行为确有多尺度结构，额外内存待查。

**可复用机制** · 同缓存体积比较单轨道和多轨道，并按历史长度验收。

<a id="paper-139554"></a>

## Martine: Benchmarking Multi-View 3D Surface Reconstruction Across Viewpoint Coverage, Resolution, and Lighting

[官方论文页](https://neurips.cc/virtual/2026/poster/139554) · [作者来源](https://openreview.net/forum?id=IxlCfLMRly)

- **问题 / 瓶颈** · 单一视角、光照或解析度可改变方法排序。
- **核心创新 / 方法** · 提供准确标定与参考扫描，并按材料、可见性、曲率和细结构拆分。
- **Baseline** · 摄影测量、MVS、隐式面、Gaussian splatting 与光度立体。
- **Benchmark** · 28 个物体、84 视角、两类照明，高分辨率。
- **关键结果 / 消融** · 可辨识亚毫米差异，最佳可见表面单向 Chamfer 0.063 mm。
- **适用条件 / 局限** · 实验室范围、视角与材质覆盖待核。

**可复用机制** · 按可见区与材质评估，并把标定和测量误差写入误差预算。

<a id="paper-138992"></a>

## MaSC: A Masked Similarity Metric for Evaluating Concept-Driven Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/138992) · [作者来源](https://openreview.net/forum?id=s74oBrTreh)

- **问题 / 瓶颈** · 图像全局相似度与人评不一致。
- **核心创新 / 方法** · 同一 SigLIP2 前向基于前景掩码获得概念保持和提示匹配分。
- **Baseline** · CLIP-I、DINO、CLIP-T 和视觉语言评审。
- **Benchmark** · DreamBench++ 人评与 ORIDa 真实照。
- **关键结果 / 消融** · 身份保持的人评 Spearman 0.611；ORIDa AUC 0.992。
- **适用条件 / 局限** · 掩码来源与膨胀程度会影响结果。

**可复用机制** · 评估粗糙掩码和精细掩码的稳定性，同时单列背景提示符合。

<a id="paper-155044"></a>

## Mask-Conditioned Gradient Masking for Fine-Tuning Mixture-of-Experts Diffusion Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155044) · [作者来源](https://openreview.net/forum?id=8s9FEa3MGT)

- **问题 / 瓶颈** · 专家可能在不同去噪状态专门化，异状态梯度互相干扰。
- **核心创新 / 方法** · 按实例遮盖率有选择地抑制专家梯度。
- **Baseline** · 标准全参数微调。
- **Benchmark** · MoE 扩散语言模型实验，名称和数值待核。
- **关键结果 / 消融** · 摘要称稳健优于参考。
- **适用条件 / 局限** · 路由专门化与不同调度的匹配需验证。

**可复用机制** · 记录不同遮盖率下专家分布和梯度冲突，固定训练成本比较随机屏蔽。

<a id="paper-148970"></a>

## Masked Diffusion Language Models are Strong and Steerable Text-Based World Models for Agentic RL

[官方论文页](https://neurips.cc/virtual/2026/poster/148970) · [作者来源](https://openreview.net/forum?id=tmE031m5iF)

- **问题 / 瓶颈** · 单向生成可能难联合满足多条状态依赖。
- **核心创新 / 方法** · 对比在不同架构中保留完整状态上下文的能力，以确定性状态检查验证结果。
- **Baseline** · 自回归世界模型和原始策略表现。
- **Benchmark** · 九类环境训练及三类留出，评一致性和多样性。
- **关键结果 / 消融** · 摘要称在相近延迟下改善状态一致与落地性。
- **适用条件 / 局限** · 仿真转移不等于真实环境，部分领域差异待核。

**可复用机制** · 用普通开放式拼图环境测状态守恒和转移错误，先验收再用于训练。

<a id="paper-149422"></a>

## Masked Diffusion Vision-Language Models for Temporal Action Localization

[官方论文页](https://neurips.cc/virtual/2026/poster/149422) · [作者来源](https://openreview.net/forum?id=qAQchYkMe4)

- **问题 / 瓶颈** · 文本先后绑定和逐词损失无法表示区间质量。
- **核心创新 / 方法** · 遮盖扩散允许语义和时间词共修正，用边界感知遮盖和阶段加权重建。
- **Baseline** · 自回归视觉语言基线。
- **Benchmark** · ActivityNet-RTL、ActivityNet-1.3、THUMOS-14，以时间 IoU 评。
- **关键结果 / 消融** · 高 IoU 要求下收益尤其大。
- **适用条件 / 局限** · 推理多步开销及各组件边际贡献待核。

**可复用机制** · 固定采样成本分别改变边界遮盖和 IoU 奖励。

<a id="paper-152135"></a>

## Masked Generative Pretraining Improves Cross-Dataset Transfer in Pixel-Space Diffusion

[官方论文页](https://neurips.cc/virtual/2026/poster/152135) · [作者来源](https://openreview.net/forum?id=VGs5oln6Kl)

- **问题 / 瓶颈** · 增强语义先验会限制跨分布迁移。
- **核心创新 / 方法** · 遮盖图像区域并在跨噪声级对齐预测，计算噪声条件的结构一致性。
- **Baseline** · 增强对比表征一致性训练。
- **Benchmark** · 七个跨数据集生成任务、ImageNet-256。
- **关键结果 / 消融** · 固定结构与微调时跨域持续提高，域内仍有竞争力。
- **适用条件 / 局限** · 遮盖构造、分布偏移距离和整体算力待核。

**可复用机制** · 按目标分布偏离程度测增益，并监控跨噪声结构一致性是否预测结果。

<a id="paper-151801"></a>

## Masked Sobolev Training for Feasibility-Reliable Optimization Proxies

[官方论文页](https://neurips.cc/virtual/2026/poster/151801) · [作者来源](https://openreview.net/forum?id=XuxAvk8BQy)

- **问题 / 瓶颈** · 完整 Jacobian 标签可能跨区不连续。
- **核心创新 / 方法** · 随机掩码选择求解器敏感度，和解值共同训练。
- **Baseline** · 只用值、密集导数匹配。
- **Benchmark** · 最优控制、三个 PGLib 网络与组合投资。
- **关键结果 / 消融** · 达到教师 95% 表现快 2.5 倍；约束违例中位数最多降 4 倍；投资例中收益不可靠。
- **适用条件 / 局限** · 导数极局部或跨区消失时价值有限。

**可复用机制** · 按活跃区统计值和导数误差，再用可行率验收。

<a id="paper-152131"></a>

## Masked Visual Actions for Unified World Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/152131) · [作者来源](https://openreview.net/forum?id=VHMcZoypoo)

- **问题 / 瓶颈** · 数值动作和预训练视频表征不直接兼容。
- **核心创新 / 方法** · 部分暴露机器人移动或目标物体移动来条件化视频模型。
- **Baseline** · 直接数值动作条件及独立正逆模型为设计对照。
- **Benchmark** · 15 小时时间遮盖视频与仿真，测试不同场景和本体的操作。
- **关键结果 / 消融** · 报告预测与实机结果相关，也能由物体轨迹推断机器人动作。
- **适用条件 / 局限** · 视觉合理性并不保证力学执行可行。

**可复用机制** · 在良性操作测试中分开测动作可控、实际成功和视频表面质量。

<a id="paper-155231"></a>

## MaskSense: Confronting the Visual Exploration Trap in Masked Image Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/155231) · [作者来源](https://openreview.net/forum?id=7HT2OEIoEN)

- **问题 / 瓶颈** · 置信驱动采样会先取容易的背景，压缩与奖励相关的主体多样性。
- **核心创新 / 方法** · 按语义分配探索，并依据解码熵变化重点更新关键步。
- **Baseline** · 基本遮盖生成和直接 GRPO。
- **Benchmark** · 多项图文生成评测，含 GenEval 与 HPS。
- **关键结果 / 消融** · GenEval 54% 到 86%，HPS 28.89 到 36.39。
- **适用条件 / 局限** · 语义锚点可靠性及多样性和内容保真取舍待核。

**可复用机制** · 按主体和背景分别记录采样多样性及奖励方差。

<a id="paper-155267"></a>

## Massively Parallel Exact Inference for Hawkes Processes

[官方论文页](https://neurips.cc/virtual/2026/poster/155267) · [作者来源](https://openreview.net/forum?id=6yoruSsZzc)

- **问题 / 瓶颈** · 线性 Hawkes 的逐事件精确递推难利用 GPU 并行。
- **核心创新 / 方法** · 表示为稀疏转移矩阵乘积，做并行前缀扫描并分批保内存。
- **Baseline** · 朴素成对计算及线性顺序递推。
- **Benchmark** · 合成和真实事件数据，数千节点及数千万事件。
- **关键结果 / 消融** · 摘要报告大幅提速且保持精确似然。
- **适用条件 / 局限** · 依赖线性指数核允许该稀疏结合表示。

**可复用机制** · 寻找递推状态转移的结合规律，用扫描平行化而不改变统计模型。

<a id="paper-150586"></a>

## MASTA: A Feedback-Scheduled Multi-Agent System for End-to-End Tamarin Protocol Modeling and Analysis

[官方论文页](https://neurips.cc/virtual/2026/poster/150586) · [作者来源](https://openreview.net/forum?id=h51B2FuWVX)

- **问题 / 瓶颈** · 同一代理编写并自验时不易区分语法、可达性和属性错误。
- **核心创新 / 方法** · 让调度角色按可信验证器反馈与稳定的问题标签路由修正。
- **Baseline** · 同骨干 OpenCode 及两类代码代理。
- **Benchmark** · 十类协议的防御性验证评估，五项正确及完备指标。
- **关键结果 / 消融** · 摘要报告较同骨干部分指标最多改善 0.27，移除调度角色使验证表现大降。
- **适用条件 / 局限** · 验证器结论依赖属性和模型是否忠实。

**可复用机制** · 将谁修正哪类形式错误与生成文本本身隔离，逐项确认规范覆盖。

<a id="paper-155062"></a>

## MASTARS: Multi-Agent Sequential Trajectory Augmentation with Return-Conditioned Subgoals

[官方论文页](https://neurips.cc/virtual/2026/poster/155062) · [作者来源](https://openreview.net/forum?id=8kbDxSuHS6)

- **问题 / 瓶颈** · 独立生成组合失配，联合整轨生成易复刻原数据。
- **核心创新 / 方法** · 顺序生成各代理的轨迹，条件补全对齐已出现代理行为。
- **Baseline** · 独立、联合生成和离线多代理方法。
- **Benchmark** · MPE、SMAC、SMAC-v2。
- **关键结果 / 消融** · 摘要报告多种离线方法获得行为收益。
- **适用条件 / 局限** · 固定顺序的偏置及协作依赖程度需复验。

**可复用机制** · 将同步生成拆成能利用队友轨迹的条件任务，兼顾多样性与协调。

<a id="paper-148863"></a>

## MAST: Label-Efficient, Robust, and Generalizable Sound Detection for Biodiversity Monitoring via Masked Audio Pretraining and Self-Training

[官方论文页](https://neurips.cc/virtual/2026/poster/148863) · [作者来源](https://openreview.net/forum?id=uco9zJhmN7)

- **问题 / 瓶颈** · 背景噪声与真实叫声共享片段，片级表征未必能定位。
- **核心创新 / 方法** · 遮罩预训练后加框级匹配与背景负样本，并分两阶段伪标注。
- **Baseline** · 最强声学定位基线和训练组件对照。
- **Benchmark** · 印尼雨林、西班牙鸟鸣；跨站 mAP/F1。
- **关键结果 / 消融** · 跨站雨林增加 0.22 mAP、0.24 F1，鸟鸣增加 0.12、0.10。
- **适用条件 / 局限** · 需要事件框或可靠伪框，跨生态条件需验收。

**可复用机制** · 用对象尺度的监督隔离背景变化，让预训练知识迁移到事件定位。

<a id="paper-150904"></a>

## Matchability-Aware Conformal Prediction for Open-Ended Language Model Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/150904) · [作者来源](https://openreview.net/forum?id=eY9UXFg5E0)

- **问题 / 瓶颈** · 即使校准正确，候选集遗漏正确语义也限制覆盖。
- **核心创新 / 方法** · 语义聚类后校准集分数，用生成前预测对可匹配性分层。
- **Baseline** · 整体校准覆盖及带 oracle 回退上界。
- **Benchmark** · 三个 4B 至 9B 模型、18 个模型数据集组合、四种划分。
- **关键结果 / 消融** · 预测可匹配的非回退集覆盖 0.71，相对整体 0.61；跨模型 AUC 0.78。
- **适用条件 / 局限** · 分层依赖预测质量，回退上界并非可部署结果。

**可复用机制** · 先分开候选召回和置信排序，再决定检索、澄清或拒答。

<a id="paper-152841"></a>

## Matched-Control Tests of Partition-Source Claims in One Routed Distillation Family

[官方论文页](https://neurips.cc/virtual/2026/poster/152841) · [作者来源](https://openreview.net/forum?id=PykGJWR2N4)

- **问题 / 瓶颈** · 联合改变路由深度、标签分组和训练量会使提升无法归因。
- **核心创新 / 方法** · 匹配教师词元、参数和路由深度，并用纯路由与同结构乱序分区作空对照。
- **Baseline** · Latent-Routing MoA、Matched-Partition-Shuffle。
- **Benchmark** · 同一路由家族，五域主要分布变化，外部平均作补充。
- **关键结果 / 消融** · 对两控制平均高 2.46 和 2.04 点；部分单项区间覆盖零。
- **适用条件 / 局限** · 仅支持所测家族内归因，外部切片证据不足。

**可复用机制** · 将训练预算和分组形状固定后再改分区语义，测增量是否真的来自分组来源。

<a id="paper-156763"></a>

## MatchEx: Model-Level GNN Explanations with Multi-Granular Insights

[官方论文页](https://neurips.cc/virtual/2026/poster/156763) · [作者来源](https://neurips.cc/virtual/2026/poster/156763)

- **问题 / 瓶颈** · 精确同构过严，一个类别也未必有唯一判别结构。
- **核心创新 / 方法** · 以匹配目标找语义相似的判别模式，必要时分组并投射回实例。
- **Baseline** · 生成式模型级解释及精确匹配。
- **Benchmark** · 六个真实与合成图数据集。
- **关键结果 / 消融** · 摘要报告解释一致性与跨粒度质量改善。
- **适用条件 / 局限** · 匹配模式需能代表真实分布，投射忠实度须再验。

**可复用机制** · 以可接受结构差异找共享规则，而不是将稀有精确图模式当通用解释。

<a id="paper-148528"></a>

## Matching2Matching: Zero-Shot Light Field Image Denoising with Matching View Construction

[官方论文页](https://neurips.cc/virtual/2026/poster/148528) · [作者来源](https://openreview.net/forum?id=xDEl8HwZKU)

- **问题 / 瓶颈** · 同单图内部选相似块易把纹理差当噪声。
- **核心创新 / 方法** · 沿极线找匹配区块并约束可见性和视差一致。
- **Baseline** · 二维自相似及既有零样本去噪。
- **Benchmark** · 合成与真实 4D 光场噪声。
- **关键结果 / 消融** · 摘要报告去噪与细节一致性改善。
- **适用条件 / 局限** · 依赖独立噪声、多视角以及可靠配准。

**可复用机制** · 先用观测几何保证两份监督共享目标，再利用噪声独立训练。

<a id="paper-150223"></a>

## Matching-Based Few-Shot Semantic Segmentation Models Are Interpretable by Design

[官方论文页](https://neurips.cc/virtual/2026/poster/150223) · [作者来源](https://openreview.net/forum?id=jqykrG5xAb)

- **问题 / 瓶颈** · 通用梯度解释可能没有说明模型用了哪个示例区域。
- **核心创新 / 方法** · 从多层匹配分数提取归因图，并评估在少样本设置下的解释效度。
- **Baseline** · 适配后的标准归因。
- **Benchmark** · 多个少样本语义分割基准。
- **关键结果 / 消融** · 摘要报告归因优于所比方法，模式与架构相符。
- **适用条件 / 局限** · 只适用显式匹配骨干，分数仍需核对忠实性。

**可复用机制** · 优先解释模型内置证据检索路径，避免为原本可读的决策再建黑盒代理。

<a id="paper-155876"></a>

## Match the Geometry, Skip the Surrogate: Extreme Low-Budget Optimization in High Dimensions

[官方论文页](https://neurips.cc/virtual/2026/poster/155876) · [作者来源](https://openreview.net/forum?id=2BB0oOmLs4)

- **问题 / 瓶颈** · 盒状信赖域可能采到解码器未见过的潜区域。
- **核心创新 / 方法** · 以支持一致的候选几何做对照，再在剩余结构足够时添加协方差学习。
- **Baseline** · 盒内随机与贝叶斯优化；支持匹配后的简化方法。
- **Benchmark** · 此处提取 LassoBench、NAS-Bench-101 和文本潜变量等一般优化实验。
- **关键结果 / 消融** · 摘要报告存在可学习方向时，局部子空间协方差更新有额外价值。
- **适用条件 / 局限** · 每个任务需验证经验支持形状，不能普遍假设球面。

**可复用机制** · 先在合适的支持上比较随机搜索，再衡量训练代理是否值得少量反馈预算。

<a id="paper-148908"></a>

## MatCurvs: Article Real-Coordinate Curve Extraction for Agent-Ready Materials Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/148908) · [作者来源](https://openreview.net/forum?id=uHECG4TS6s)

- **问题 / 瓶颈** · 多模态模型能描述曲线却不一定读得准物理坐标。
- **核心创新 / 方法** · 先用坐标对照核验曲线，再将验证过的结构化数值传给模型。
- **Baseline** · 仅图像 VLM、图像加数值、纯文本加数值。
- **Benchmark** · MatCurvs、14,740 道确定性数值问题。
- **关键结果 / 消融** · 中位相对误差从 54% 降至约 4%；纯数据文本模型匹配图文方式。
- **适用条件 / 局限** · 标尺或图例读错会传入后续，需保留出处。

**可复用机制** · 把结构化测量作为可验证的中间结果，定位失败究竟来自读图还是计算。

<a id="paper-139769"></a>

## MaterialsSaddles: 34 Million Transition States and a Flow-Matching Saddle-Point Predictor for Materials

[官方论文页](https://neurips.cc/virtual/2026/poster/139769) · [作者来源](https://openreview.net/forum?id=5lFUOghgb2)

- **问题 / 瓶颈** · 经典中点不一定接近可行的周期材料路径状态。
- **核心创新 / 方法** · 以已有端点为条件学习中间状态的候选，用同一数值求解器验收初值。
- **Baseline** · 端点中点初始化的 dimer 搜索。
- **Benchmark** · 电池材料子集的试验性 DFT 收敛。
- **关键结果 / 消融** · 摘要报告候选初始化更快、更可靠，量化幅度待核实。
- **适用条件 / 局限** · 试验范围较小，训练参考来自近似势。

**可复用机制** · 学习器只提供暖启动，最终结果仍交给物理求解检验。

<a id="paper-139534"></a>

## MathlibPR: Pull Request Merge-Outcome Benchmark for Formal Mathematical Libraries

[官方论文页](https://neurips.cc/virtual/2026/poster/139534) · [作者来源](https://openreview.net/forum?id=KN8c4YcO15)

- **问题 / 瓶颈** · 能验证数学正确性不等于符合库内惯例或维护目标。
- **核心创新 / 方法** · 以真实 Mathlib PR 历史分阶段比较构建、修订和合并。
- **Baseline** · 多种语言模型与代码代理。
- **Benchmark** · Mathlib4 合并、需修改及未合并的真实记录。
- **关键结果 / 消融** · 摘要报告模型和代理难区分构建通过与可合并。
- **适用条件 / 局限** · 历史合并受非技术因素影响，不能作绝对真值。

**可复用机制** · 将可执行成功与项目适配性作为两个独立信号。

<a id="paper-150723"></a>

## MATO: Multi-objective Personalized Alignment with Test-time Optimization for Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150723) · [作者来源](https://openreview.net/forum?id=fv2x5XU7kK)

- **问题 / 瓶颈** · 固定偏好提示容易忽略某项目标或不适应局部冲突。
- **核心创新 / 方法** · 从同骨干估各自然语言目标的奖励，按用户权重与前缀调整分布优化。
- **Baseline** · 提示型个性化与多目标对齐对照。
- **Benchmark** · 多个模型及数据上的 Pareto 和可控性评估。
- **关键结果 / 消融** · 摘要报告多目标折中与可控性更好。
- **适用条件 / 局限** · 依赖自评奖励可靠，额外推理成本需核对。

**可复用机制** · 保持目标可分别诊断，让调权响应当前上下文而非永久写进权重。

<a id="paper-152694"></a>

## Matrix-Free Natural Gradient via Stochastic Truncated Metrics

[官方论文页](https://neurips.cc/virtual/2026/poster/152694) · [作者来源](https://openreview.net/forum?id=R6odsq6K6r)

- **问题 / 瓶颈** · 直接求曲率需要高时空成本，分层结构近似限制适用范围。
- **核心创新 / 方法** · 维护带阻尼的短期指数移动度量，以无偏随机 Fisher 估计形成矩阵自由更新。
- **Baseline** · 原自然梯度及结构化近似。
- **Benchmark** · 视觉和语言模型优化；性能、稳定及成本。
- **关键结果 / 消融** · 单步 O(Kd) 并分析截断误差，摘要报告实证稳定。
- **适用条件 / 局限** · 度量记忆有限且噪声受采样控制。

**可复用机制** · 把曲率的维护成本限在短期秩预算内，同时显式追踪由截断引入的偏差。

<a id="paper-156123"></a>

## Matrix-Free Stochastic Training of Low-Rank Spectral Graph Learning via Randomized Adaptive Spectral Estimation

[官方论文页](https://neurips.cc/virtual/2026/poster/156123) · [作者来源](https://openreview.net/forum?id=0F08MV66N8)

- **问题 / 瓶颈** · 显式谱基预处理和全图上下文限制扩展。
- **核心创新 / 方法** · 稀疏矩阵乘探针构造 Krylov/Ritz 基，以探针摘要降低小批估计方差。
- **Baseline** · 全图特征基和矩阵自由多项式滤波。
- **Benchmark** · 14 个分类基准；特征基时间和精度。
- **关键结果 / 消融** · 可行处与精确基在种子方差内匹配，PubMed 基构造约快 67 倍。
- **适用条件 / 局限** · 依赖近似子空间及探针对谱信号的覆盖。

**可复用机制** · 让全局谱摘要慢速刷新，用控制变量将其作为小批训练中的低噪声参照。

<a id="paper-152261"></a>

## Matrix Recovery Via Symmetric Rank-one Measurements With Random Unit-modulus Vectors

[官方论文页](https://neurips.cc/virtual/2026/poster/152261) · [作者来源](https://openreview.net/forum?id=UNVpU6i2AS)

- **问题 / 瓶颈** · 固定幅度的二次测量不能分辨逐项对角元素。
- **核心创新 / 方法** · 堆叠恒模测量和已知或直接测量的对角信息，以混合范数等距界分析恢复。
- **Baseline** · 只靠对称恒模测量。
- **Benchmark** · 有无噪声的矩阵恢复理论和数值。
- **关键结果 / 消融** · 对角可用时给出精确或稳定恢复。
- **适用条件 / 局限** · 针对所定义测量分布、对称性及独立对角信息。

**可复用机制** · 设计传感器前先找测量的不变方向，再加最小互补观测处理不可识别变量。

<a id="paper-153497"></a>

## Matryoshka Transcoders and Hierarchy Misalignment: When SAE Absorption Protection Does Not Transfer

[官方论文页](https://neurips.cc/virtual/2026/poster/153497) · [作者来源](https://openreview.net/forum?id=Kx6IJ8I6C8)

- **问题 / 瓶颈** · 重建随字典增大而改善不保证宽泛父特征会排列在早期。
- **核心创新 / 方法** · 以匹配训练比较 Matryoshka 和 BatchTopK，并移除跨空间映射作为桥接控制。
- **Baseline** · BatchTopK 和单空间 SAE。
- **Benchmark** · Gemma-2-2B MLP 变换字典，16k 对比，测吸收、未解释方差和首字母 F1。
- **关键结果 / 消融** · 跨空间时 BatchTopK 三项更优，移除映射才恢复预期嵌套优势。
- **适用条件 / 局限** · 限于测试宽度、架构和特征指标。

**可复用机制** · 检查早期特征对应输入语义还是输出可预测性，避免把形成层级视作可解释性的充分证据。

<a id="paper-151052"></a>

## Maximin Robust Bayesian Experimental Design

[官方论文页](https://neurips.cc/virtual/2026/poster/151052) · [作者来源](https://openreview.net/forum?id=dLiJdxU8o7)

- **问题 / 瓶颈** · 嵌套采样估计有偏且方差大。
- **核心创新 / 方法** · 以信息约束构造最大最小游戏，目标变成 Sibson α 互信息，并对随机设计做 PAC-Bayes 下界。
- **Baseline** · 经典贝叶斯实验设计及嵌套蒙特卡洛估计。
- **Benchmark** · 理论信息增益和有限样本下界；具名实验待核实。
- **关键结果 / 消融** · 推出倾斜后验和 Rényi 条件信息增益，得到高概率下界。
- **适用条件 / 局限** · 需要定义可接受的错设集合，复杂设计的计算收益待查。

**可复用机制** · 分别验收模型错设鲁棒性与有限样本估计误差。

<a id="paper-152443"></a>

## MaxIM: Maximally Informative Incremental Summarization via Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/152443) · [作者来源](https://openreview.net/forum?id=T6lIK4rfd3)

- **问题 / 瓶颈** · 容量受限摘要需要不断更新，终局受益难归因给单次更新。
- **核心创新 / 方法** · 用预测充分性目标、历史互信息约束及变分 critic 构造逐步奖励。
- **Baseline** · 长程摘要与记忆 RL 方法，具名待核实。
- **Benchmark** · 多项长程任务，自动评委和端任务收益。
- **关键结果 / 消融** · 摘要报告优于所测对照，无须人工偏好。
- **适用条件 / 局限** · 未来任务相关目标应可获得，评委偏差与估计下界紧致性需查。

**可复用机制** · 用同一记忆容量对照仅追求压缩、只预测未来和同时保留历史的一致性。

<a id="paper-155987"></a>

## MaxSketch: Robust Distinct Counting in Streams via Random Projections

[官方论文页](https://neurips.cc/virtual/2026/poster/155987) · [作者来源](https://openreview.net/forum?id=1MB9KxyzHe)

- **问题 / 瓶颈** · 经典去重草图预设同对象编码完全相同。
- **核心创新 / 方法** · 以随机高斯投影构建 max-linear 草图，在结构假设下估计潜在对象数。
- **Baseline** · HyperLogLog 和一般度量空间稳健计数结果。
- **Benchmark** · 图像流计数、近似误差与内存。
- **关键结果 / 消融** · 有结构时近似内存为 log n 除以 ε 四次方的多对数量级。
- **适用条件 / 局限** · 具体几何假设及远域噪声的影响待核实。

**可复用机制** · 与其一律扩大去重缓存，先测表示是否满足支持小内存估计的分离性质。

<a id="paper-151488"></a>

## MC^2: Monte Carlo Correction for Fast Elliptic PDE Solving

[官方论文页](https://neurips.cc/virtual/2026/poster/151488) · [作者来源](https://openreview.net/forum?id=aG4Bnuw2KR)

- **问题 / 瓶颈** · 纯数值开销大，纯学习解又可能在分布外有偏。
- **核心创新 / 方法** · 先做少预算 Walk-on-Spheres，单次网络前向预测结构化残差。
- **Baseline** · 纯 WoS、去噪及神经算子方法。
- **Benchmark** · PDEZoo 两百万椭圆方程、五类和多种几何，以解析真值和计算预算验收。
- **关键结果 / 消融** · 精度可匹配使用超过千倍蒙特卡洛计算的直接解。
- **适用条件 / 局限** · 千倍侧重蒙特卡洛预算，端到端吞吐及域外保证需查。

**可复用机制** · 对比相同预算下从无物理输入预测和从噪声数值估计纠偏，检查误差可预测性。

<a id="paper-139650"></a>

## MCP-Atlas: A Large-Scale Benchmark for Tool-Use Competency with Real MCP Servers

[官方论文页](https://neurips.cc/virtual/2026/poster/139650) · [作者来源](https://openreview.net/forum?id=DQUoAWBrpJ)

- **问题 / 瓶颈** · 最终完成率混淆调用出错、成功调用后误综合和过早停止。
- **核心创新 / 方法** · 按事实声明判分，以十一类诊断区分工具层和判断层。
- **Baseline** · 二十个前沿模型；对照不同工具和认知失败类型。
- **Benchmark** · MCP-Atlas 一千任务、36 个服务及 220 个工具，量化声明覆盖和失败归因。
- **关键结果 / 消融** · 覆盖阈值 0.75 下最高通过 82.2%；已归因失败中 63.3% 属认知类。
- **适用条件 / 局限** · 依赖评分声明与自动归因正确性，未覆盖工具环境待查。

**可复用机制** · 不要强制轨迹唯一，优先验收关键证据及结论是否一致，再检查失效阶段。

<a id="paper-139700"></a>

## MCPHunt: An Evaluation Framework for Cross-Boundary Data Propagation in Multi-Server MCP Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/139700) · [作者来源](https://openreview.net/forum?id=9mPzIg8uil)

- **问题 / 瓶颈** · 接口各自权限合法不代表工作流中的整体传输合规。
- **核心创新 / 方法** · 用合成标记跟踪测试数据，设置良性和难负例，分开报告任务必需的传递与可避免的泄漏。
- **Baseline** · 隔离控制组及带防护提示的测试。
- **Benchmark** · 五个模型、147 项任务、3,615 条主要记录，量化越界传播和任务效用。
- **关键结果 / 消融** · 摘要报告所有所测模型均存在可避免传播，防护提示收益随模型而变。
- **适用条件 / 局限** · 实验为可控合成测试，实际保密与策略需结合权限实施。

**可复用机制** · 把端到端数据流作为验收对象，用无敏感内容的可追踪测试标记验证脱敏与隔离。

<a id="paper-150934"></a>

## MCSplat: Multi-View Photometric and Geometric Consistent Feed-Forward Gaussian Splatting for Driving Scenes

[官方论文页](https://neurips.cc/virtual/2026/poster/150934) · [作者来源](https://openreview.net/forum?id=eCgqMJ0iay)

- **问题 / 瓶颈** · 跨相机曝光差异可被错误吸收进几何，深度不连续处法线又不可靠。
- **核心创新 / 方法** · 用深度引导相机对应构建规范外观，渲染后恢复相机外观，并按 Fisher 敏感度加权监督。
- **Baseline** · 已有前馈高斯重建。
- **Benchmark** · Waymo 完整验证与高外观差异子集；重建及新视角几何。
- **关键结果 / 消融** · 摘要报告两个子集均改善，几何更一致。
- **适用条件 / 局限** · 深度提示质量和低光、动态曝光变化下的适用性待查。

**可复用机制** · 分开控制相机特定光度变化和几何学习，并在曝光差异最大的子集验收。

<a id="paper-149972"></a>

## Mean-Field Control on Sparse Graphs: From Local Limits to GNNs via Neighborhood Distributions

[官方论文页](https://neurips.cc/virtual/2026/poster/149972) · [作者来源](https://openreview.net/forum?id=lod8FKUWPS)

- **问题 / 瓶颈** · 经典均场理论以密集可交换交互为前提，难表示局部异质。
- **核心创新 / 方法** · 把总体状态设成带标记根邻域分布，在其上构造动态规划并支持图 Actor-Critic。
- **Baseline** · 密集全连接的经典均场控制。
- **Benchmark** · 稀疏图多代理控制，有限时域局部性和 GNN 实验；具名基准待核实。
- **关键结果 / 消融** · 证明时刻 t 的最优策略只需 T−t 跳邻域，并推广经典均场对象。
- **适用条件 / 局限** · 依赖论文中的有限时域和局部交互假设，长时与动态图待查。

**可复用机制** · 让策略感受野随规划余量变化，验证更大邻域是否确实带来额外收益。

<a id="paper-151707"></a>

## Mean-Field Parallel Decoding for Discrete Diffusion Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151707) · [作者来源](https://openreview.net/forum?id=YewDrMrsZb)

- **问题 / 瓶颈** · 两个各自高置信的 token 也可能在同一步提交时冲突。
- **核心创新 / 方法** · 根据预测分布定义位置交互，以变分固定点更新修正提交分数，无须重训。
- **Baseline** · 按单位置边缘置信的并行解码。
- **Benchmark** · 推理与代码生成，比较精度与时延。
- **关键结果 / 消融** · 摘要报告更多位置并行提交且维持有竞争力的质量。
- **适用条件 / 局限** · 固定点步骤开销及跨架构兼容性待核实。

**可复用机制** · 报告联合提交的冲突率，衡量少做网络评估是否抵过内部求解成本。

<a id="paper-152034"></a>

## Mean Testing under Truncation beyond Gaussian

[官方论文页](https://neurips.cc/virtual/2026/poster/152034) · [作者来源](https://openreview.net/forum?id=W2sWU2ZYWN)

- **问题 / 瓶颈** · 删除少量未知区域可能使两种分布即使无限数据也不可区分。
- **核心创新 / 方法** · 从方向矩推导偏差和二阶检验率，并以方向中位数正则给更小阈值。
- **Baseline** · 无截断均值检验与高斯设定。
- **Benchmark** · 高维非高斯方向有限矩的理论分析。
- **关键结果 / 消融** · 偏差阈值为 ε^(1−1/p) 量级，中位数正则下为线性量级。
- **适用条件 / 局限** · 依赖矩条件或额外中位数正则。

**可复用机制** · 给最小可辨效应同时标注抽样误差和选择性漏观测误差。

<a id="paper-151285"></a>

## Measure Less, Know More: Self-Supervised Test-Time Feature Acquisition

[官方论文页](https://neurips.cc/virtual/2026/poster/151285) · [作者来源](https://openreview.net/forum?id=bXoyojlawt)

- **问题 / 瓶颈** · 收集全部模态昂贵，但没有目标标签来训练选择。
- **核心创新 / 方法** · 从预训练表示构造自监督反馈并训练顺序采集。
- **Baseline** · 现有主动特征采集方法，名称待核。
- **Benchmark** · 线性设定理论及未知下游任务实证。
- **关键结果 / 消融** · 摘要称采集策略跨任务迁移并优于对照。
- **适用条件 / 局限** · 前提是预训练特征含目标所需信息。

**可复用机制** · 在固定采集预算下留出任务族，并验证过度相似模态不会挤占额度。

<a id="paper-153179"></a>

## Measure-to-measure Regression with Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/153179) · [作者来源](https://openreview.net/forum?id=NDf3Nc1J2Y)

- **问题 / 瓶颈** · 逐点独立回归无法捕捉交互导致的密度变化。
- **核心创新 / 方法** · 以 Transformer 表达静态测度映射或动态速度场。
- **Baseline** · 逐点回归和已有测度学习思路。
- **Benchmark** · 合成数据和标准交互粒子系统，以留出测度验证。
- **关键结果 / 消融** · 摘要报告可泛化到新测度。
- **适用条件 / 局限** · 实验证据的样本界与粒子规模成本待核。

**可复用机制** · 在非生物粒子系统分别报告个体误差与总体分布偏差。

<a id="paper-153978"></a>

## Measuring and Decomposing Mode Separation via the Canonical Diffusion

[官方论文页](https://neurips.cc/virtual/2026/poster/153978) · [作者来源](https://openreview.net/forum?id=H63M35DFX7)

- **问题 / 瓶颈** · PCA 和熵可对大尺度伸展敏感，却无法区分断裂的模式。
- **核心创新 / 方法** · 在以目标密度为平稳分布的可逆扩散上读自相关方向和平方和。
- **Baseline** · PCA、熵与可已知混合的互信息。
- **Benchmark** · 合成高斯混合及 SDXL 图像分布，含高斯零假设理论。
- **关键结果 / 消融** · 摘要报告能捕捉熵和 PCA 漏掉的结构。
- **适用条件 / 局限** · 依赖得分估计和时间滞后选择，现实高维成本待核。

**可复用机制** · 用方差相同、模态隔离程度不同的合成数据检验诊断。

<a id="paper-139106"></a>

## Measuring and Mitigating the Distributional Gap Between Real and Simulated User Behaviors

[官方论文页](https://neurips.cc/virtual/2026/poster/139106) · [作者来源](https://openreview.net/forum?id=kkKJ6xTPMS)

- **问题 / 瓶颈** · 不同模拟器可能共享行为遗漏，单例表现不足以证明拟真。
- **核心创新 / 方法** · 抽取行为表示、聚类并比较真实和模拟的离散分布。
- **Baseline** · 24 种用户模拟器及互补混合。
- **Benchmark** · 真实和模拟的写作、代码会话，另有人类验证和消融。
- **关键结果 / 消融** · 作者报告分布差异大，互补模型混合较各自更近真实。
- **适用条件 / 局限** · 聚类受表示和任务覆盖影响。

**可复用机制** · 把常见及罕见行为的召回分开，不按模型总分挑模拟器。

<a id="paper-153032"></a>

## Measuring and Strengthening Behavioral Suppression in Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153032) · [作者来源](https://openreview.net/forum?id=OWTLAtAspY)

- **问题 / 瓶颈** · 单次修复可能在后续训练中复发。
- **核心创新 / 方法** · 以受控合成行为比较修复方法并检测良性版本更新后的复发。
- **Baseline** · SFT、GRPO 与遗忘参考。
- **Benchmark** · 两种模型家族、两类受控行为设定。
- **关键结果 / 消融** · 摘要中改进降低复发同时保持任务准确。
- **适用条件 / 局限** · 合成设定距离实际系统尚需验收。

**可复用机制** · 在良性微调后重做安全回归，不能仅凭修复当天表现判断持久性。

<a id="paper-155873"></a>

## Measuring Black-Box Confidence via Reasoning Trajectories: Geometry, Coverage, and Verbalization

[官方论文页](https://neurips.cc/virtual/2026/poster/155873) · [作者来源](https://openreview.net/forum?id=2C9F7Q7NWK)

- **问题 / 瓶颈** · 样本投票会忽略可见推理文本内的信号。
- **核心创新 / 方法** · 把滑窗文本嵌入与候选答案锚点比较，再融合覆盖和口头信心。
- **Baseline** · 多次采样自一致与单信号。
- **Benchmark** · MedQA-USMLE、GPQA Diamond、MMLU-Pro 的六模型任务组合。
- **关键结果 / 消融** · 四样本融合的中位 AUC 0.78，八样本投票 0.71。
- **适用条件 / 局限** · 需可见推理与可建锚点；未验证决策安全。

**可复用机制** · 固定候选答案控制换答因素，并测采样成本与校准。

<a id="paper-150718"></a>

## Measuring Coherence in Predictive Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150718) · [作者来源](https://openreview.net/forum?id=fwwccado3G)

- **问题 / 瓶颈** · 更新不一致可让主动采集选错点，即便平均预测不错。
- **核心创新 / 方法** · 构造不一致比率，另对只关心最终动作的任务定义动作一致性。
- **Baseline** · TabPFN 与标准参数式贝叶斯近似。
- **Benchmark** · 合成主动学习，测预测与获取数据质量。
- **关键结果 / 消融** · 较一致的模型获取数据更好，摘要称不能用预测误差解释。
- **适用条件 / 局限** · 动作和条件化基准依赖任务假设。

**可复用机制** · 在匹配预测误差下比较更新前后条件关系及最终决策。

<a id="paper-139635"></a>

## Measuring Collapse and Correction in Homogeneous-Panel LLM Debate

[官方论文页](https://neurips.cc/virtual/2026/poster/139635) · [作者来源](https://openreview.net/forum?id=E8FfL8c7XE)

- **问题 / 瓶颈** · 最终准确掩盖两个反向变化。
- **核心创新 / 方法** · 按初始与最终多数结果记录转移、起点和干预净收益。
- **Baseline** · 同质多模型辩论及筛选冻结策略。
- **Benchmark** · MMLU-Pro 6,925 场，记录阶段与转移。
- **关键结果 / 消融** · 发现 253 次崩塌；某干预少 29 次崩塌但损失 108 次修正。
- **适用条件 / 局限** · 仅同质选择题，早期信号非校准预测。

**可复用机制** · 报告转移矩阵和成本，按业务损失设正负权重。

<a id="paper-139418"></a>

## Measuring Cross-Modal Synergy: A Benchmark for VLM Explainability

[官方论文页](https://neurips.cc/virtual/2026/poster/139418) · [作者来源](https://openreview.net/forum?id=Rt2AbMM2YF)

- **问题 / 瓶颈** · 单模态扰动在信息冗余时会给矛盾排名。
- **核心创新 / 方法** · 以 Shapley 交互为基础隔离图文共同贡献，并做快速近似。
- **Baseline** · 单模态扰动及八种解释方法。
- **Benchmark** · 三个架构、三个数据集，比较解释保真与时间。
- **关键结果 / 消融** · 近似相关 0.92、快 24 倍，若干显著性方法弱于改造注意方法。
- **适用条件 / 局限** · 受数据语言先验与扰动分布影响。

**可复用机制** · 同时评估视觉可读性、单模态冗余和互补贡献。

<a id="paper-152199"></a>

## Measuring Layer-wise Intrinsic Dimensionality of FFNs in LLMs via PCA

[官方论文页](https://neurips.cc/virtual/2026/poster/152199) · [作者来源](https://openreview.net/forum?id=UpWBgsC6IR)

- **问题 / 瓶颈** · 固定层宽可能忽略中间层较高容量需求。
- **核心创新 / 方法** · 对下投影输入做 PCA，以重建阈值给层画像并指导蒸馏学生裁剪。
- **Baseline** · 统一宽度及反向分配。
- **Benchmark** · 58 个模型的画像，三个教师的预算匹配压缩。
- **关键结果 / 消融** · 三教师分别高 2.7、2.3、0.9 点，反向控制最差。
- **适用条件 / 局限** · 有效维度依赖阈值，其他压缩程度需试。

**可复用机制** · 记录中间层峰值与收益，判断不均匀宽度是否值得。

<a id="paper-149010"></a>

## Measuring Robustness and Efficiency in a Connectome-Constrained Fly Visual System Model on a Collision-Detection Task

[官方论文页](https://neurips.cc/virtual/2026/poster/149010) · [作者来源](https://openreview.net/forum?id=tUtERl6Jq6)

- **问题 / 瓶颈** · 结构约束可能省计算但不带来普遍鲁棒。
- **核心创新 / 方法** · 对照受连接组约束的与无约束稀疏网络及视觉骨干。
- **Baseline** · CNN、RAFT、无连接组约束的连续循环网络。
- **Benchmark** · 模拟视觉碰撞判断，按常规视频扰动与计算成本。
- **关键结果 / 消融** · 架构比重型对照省大量计算且在部分扰动更稳，但无约束稀疏网络整体更稳。
- **适用条件 / 局限** · 仅特定视觉任务，不能推及生物实验。

**可复用机制** · 配置同算力与同任务对照，拆开稀疏性和布线先验的影响。

<a id="paper-155321"></a>

## Measuring Safety Alignment Effects in Autonomous Security Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/155321) · [作者来源](https://openreview.net/forum?id=6VC4S9fBfE)

- **问题 / 瓶颈** · 继续运行不表示会引用正确材料。
- **核心创新 / 方法** · 在授权  环境用保存记录审核当前位置、引用及结论是否一致。
- **Baseline** · 不同受控模型条件和自报完成。
- **Benchmark** · 固定审查设置，比较完成、拒答和证据质量。
- **关键结果 / 消融** · 摘要称证据质量差别不主要来自拒答；困难任务下各条件仍不可靠。
- **适用条件 / 局限** · 限固定工具与模型，不能外推真实系统。

**可复用机制** · 在自有合成代码上用人工答案验收证据和不确定性，避免按自报成功放行。

<a id="paper-153826"></a>

## Measuring Weak-to-Strong Legibility of Reasoning Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153826) · [作者来源](https://openreview.net/forum?id=IR4nD1PK12)

- **问题 / 瓶颈** · 字数短和直接能力高未必意味着可监督。
- **核心创新 / 方法** · 测弱模型在给定部分记录下完成任务的帮助程度，并关联验证表现。
- **Baseline** · 输出效率及强模型直接准确率。
- **Benchmark** · 85K 轨迹、12 个模型、三类任务。
- **关键结果 / 消融** · 部分最强、最高效模型的轨迹迁移帮助最低，程序推理验证相关较明显。
- **适用条件 / 局限** · 事实型任务的影响较弱，不等于内部思维真实性。

**可复用机制** · 先固定弱审查器，再按中断位置测试能否完成和识别错误。

<a id="paper-151389"></a>

## Mechanism-Aware Ensemble Conditioning for Data-Limited Emulation of Extreme Events

[官方论文页](https://neurips.cc/virtual/2026/poster/151389) · [作者来源](https://openreview.net/forum?id=b0AOZbejEk)

- **问题 / 瓶颈** · 训练样本短时尾部事件稀少。
- **核心创新 / 方法** · 从粗集合协方差提取局部放大结构，用 FiLM 注入修正模型。
- **Baseline** · 同骨干无条件版本及更多数据 STORN。
- **Benchmark** · 低维混沌和双层准地转流，测尾密度、超阈频率与面积。
- **关键结果 / 消融** · 50 时间单位的条件模型在所报汇总尾指标上超过训练多 20 倍数据的基线。
- **适用条件 / 局限** · 依赖粗轨迹同步及小噪声对应，极端阈值样本少。

**可复用机制** · 固定数据和骨干，按分位数检查不稳定特征能否改善尾部。

<a id="paper-149624"></a>

## Mechanisms of Misgeneralization in Physical Sequence Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/149624) · [作者来源](https://openreview.net/forum?id=oiza3wntR7)

- **问题 / 瓶颈** · 小局部误差可经物理量映射导致群体分布偏移。
- **核心创新 / 方法** · 估计数据偏差核，追踪误差经测量后如何改变概率质量。
- **Baseline** · 单样本生成质量为对照视角。
- **Benchmark** · 受控合成、迷宫导航及双摆，按目标物理量比较分布。
- **关键结果 / 消融** · 摘要称可预测概率质量增加或减少的位置。
- **适用条件 / 局限** · 核依模型和任务，未见条件需重校。

**可复用机制** · 发布模拟器前同时验速度、能量等分布与单轨迹质量。
