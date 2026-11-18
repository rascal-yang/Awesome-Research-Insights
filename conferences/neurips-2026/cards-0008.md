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
