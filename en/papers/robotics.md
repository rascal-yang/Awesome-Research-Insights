# Robotics

[Home](../../README.en.md) · [Contributing](../CONTRIBUTING.md) · [简体中文](../../papers/robotics.md)

Robot perception, policy learning, planning, and control.

## Vision-Language-Action Models

| Paper | First public / venue | Transferable insights | Resources |
| :--- | :--- | :--- | :--- |
| **ReconVLA**<br>Song et al., *ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver* | 2025-08-14<br><sub>[AAAI 2026](https://ojs.aaai.org/index.php/AAAI/article/download/38921/42883)</sub> | [Target-Region Reconstruction as Auxiliary Supervision](../insights/loss-functions.md#target-region-reconstruction-as-auxiliary-supervision) · [Instruction Prefixes for Causal Visual Grounding](../insights/modules.md#instruction-prefixes-for-causal-visual-grounding) | [Paper](https://arxiv.org/abs/2508.10333) · [Paper card (中文)](../../papers/reconvla.md#paper-reconvla) · [Project](https://zionchow.github.io/ReconVLA/) · [Code](https://github.com/OpenHelix-Team/ReconVLA) |
| [**LARA**](https://proceedings.mlr.press/v306/liu26bl.html) · [Paper card (中文)](../../conferences/icml-2026/cards/2801-2900.md#paper-liu26bl)<br><sub>Mengya Liu et al., LARA: Latent Action Representation Alignment for Vision-Language-Action Models</sub> | [2026-06-05](https://arxiv.org/abs/2606.07100)<br><sub>[ICML 2026](https://proceedings.mlr.press/v306/liu26bl.html)</sub> | [Align Action-Expert Features with Latent Actions](../insights/loss-functions.md#align-action-features-with-latent-actions) | [PMLR](https://proceedings.mlr.press/v306/liu26bl.html) · [arXiv](https://arxiv.org/abs/2606.07100) · [Code](https://github.com/lmy1001/LARA) |

<!-- classification:start -->
## Browse by Technique

The linked short insights are available in Chinese.

<a id="by-architecture"></a>

### Architectures

| Paper | Insight |
| :--- | :--- |
| [Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models](https://proceedings.mlr.press/v306/bai26h.html) · [Paper card (中文)](../../conferences/icml-2026/cards/0101-0200.md#paper-bai26h) | [Read insight (中文)](../../papers/robotics.md#bai26h-architecture) |
| [Hierarchical Policy Learning via Spectral Decomposition](https://proceedings.mlr.press/v306/cao26u.html) · [Paper card (中文)](../../conferences/icml-2026/cards/0401-0500.md#paper-cao26u) | [Read insight (中文)](../../papers/robotics.md#cao26u-architecture) |
| [The Lie We Tell: Correcting the Euclidean Fallacy in Vision Language Action Policies via Score Matching on Tangent Space](https://proceedings.mlr.press/v306/chuang26a.html) · [Paper card (中文)](../../conferences/icml-2026/cards/0701-0800.md#paper-chuang26a) | [Read insight (中文)](../../papers/robotics.md#chuang26a-architecture) |
| [Embodied-DETR: End-to-End Temporal 3D Object Detection in Egocentric Views](https://proceedings.mlr.press/v306/ding26x.html) · [Paper card (中文)](../../conferences/icml-2026/cards/0901-1000.md#paper-ding26x) | [Read insight (中文)](../../papers/robotics.md#ding26x-architecture) |

<a id="by-modules"></a>

### Modules

| Paper | Insight |
| :--- | :--- |
| [See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model](https://proceedings.mlr.press/v306/feng26x.html) · [Paper card (中文)](../../conferences/icml-2026/cards/1101-1200.md#paper-feng26x) | [Read insight (中文)](../../papers/robotics.md#feng26x-modules) |
| [StableVLA: Towards Robust Vision-Language-Action Models without Extra Data](https://proceedings.mlr.press/v306/fu26x.html) · [Paper card (中文)](../../conferences/icml-2026/cards/1101-1200.md#paper-fu26x) | [Read insight (中文)](../../papers/robotics.md#fu26x-modules) |
| [Fourier Features Let Agents Learn High Precision Policies with Imitation Learning](https://proceedings.mlr.press/v306/gyenes26a.html) | [Read insight (中文)](../../papers/robotics.md#gyenes26a-modules) |
| [ReconVLA](https://arxiv.org/abs/2508.10333) · [Paper card (中文)](../../papers/reconvla.md#paper-reconvla) | [Read insight (中文)](../../papers/robotics.md#reconvla-modules) · [Full entry](../insights/modules.md#instruction-prefixes-for-causal-visual-grounding) |

<a id="by-loss-functions"></a>

### Loss Functions

| Paper | Insight |
| :--- | :--- |
| [DT²: Decision-Targeted Digital Twins](https://proceedings.mlr.press/v306/amad26a.html) · [Paper card (中文)](../../conferences/icml-2026/cards/0001-0100.md#paper-amad26a) | [Read insight (中文)](../../papers/robotics.md#amad26a-loss-functions) |
| [OMP: One-step Meanflow Policy with Directional Alignment](https://proceedings.mlr.press/v306/fang26h.html) · [Paper card (中文)](../../conferences/icml-2026/cards/1001-1100.md#paper-fang26h) | [Read insight (中文)](../../papers/robotics.md#fang26h-loss-functions) |
| [LARA: Latent Action Representation Alignment for Vision-Language-Action Models](https://proceedings.mlr.press/v306/liu26bl.html) · [Paper card (中文)](../../conferences/icml-2026/cards/2801-2900.md#paper-liu26bl) | [Read insight (中文)](../../papers/robotics.md#liu26bl-loss-functions) · [Full entry](../insights/loss-functions.md#align-action-features-with-latent-actions) |
| [ReconVLA](https://arxiv.org/abs/2508.10333) · [Paper card (中文)](../../papers/reconvla.md#paper-reconvla) | [Read insight (中文)](../../papers/robotics.md#reconvla-loss-functions) · [Full entry](../insights/loss-functions.md#target-region-reconstruction-as-auxiliary-supervision) |

<a id="by-optimization"></a>

### Optimization

| Paper | Insight |
| :--- | :--- |
| [Blending Neural Control Density Functions for Stabilization and Safety](https://proceedings.mlr.press/v306/chaudhary26a.html) · [Paper card (中文)](../../conferences/icml-2026/cards/0401-0500.md#paper-chaudhary26a) | [Read insight (中文)](../../papers/robotics.md#chaudhary26a-optimization) |
| [De4D-SLAM: Gradient-Isolated Static-Dynamic Decoupling for Monocular SLAM in Dynamic Environments](https://proceedings.mlr.press/v306/fan26g.html) · [Paper card (中文)](../../conferences/icml-2026/cards/1001-1100.md#paper-fan26g) | [Read insight (中文)](../../papers/robotics.md#fan26g-optimization) |

<a id="by-reinforcement-learning"></a>

### Reinforcement Learning Methods

| Paper | Insight |
| :--- | :--- |
| [Learning to Search and Searching to Learn for Generalization in Planning](https://proceedings.mlr.press/v306/aichmuller26a.html) · [Paper card (中文)](../../conferences/icml-2026/cards/0001-0100.md#paper-aichmuller26a) | [Read insight (中文)](../../papers/robotics.md#aichmuller26a-reinforcement-learning) |
| [LAGEA: Language Guided Embodied Agents for Robotic Manipulation](https://proceedings.mlr.press/v306/chowdhury26a.html) · [Paper card (中文)](../../conferences/icml-2026/cards/0701-0800.md#paper-chowdhury26a) | [Read insight (中文)](../../papers/robotics.md#chowdhury26a-reinforcement-learning) |
| [Dyn-VPP: Video Prediction Policy Optimization for Improved Visual Dynamics](https://proceedings.mlr.press/v306/ge26a.html) · [Paper card (中文)](../../conferences/icml-2026/cards/1201-1300.md#paper-ge26a) | [Read insight (中文)](../../papers/robotics.md#ge26a-reinforcement-learning) |
| [CorrectionPlanner: Self-Correction Planner with Reinforcement Learning in Autonomous Driving](https://proceedings.mlr.press/v306/guo26ae.html) | [Read insight (中文)](../../papers/robotics.md#guo26ae-reinforcement-learning) |

<a id="by-training-strategies"></a>

### Training Strategies

| Paper | Insight |
| :--- | :--- |
| [NOMAD: Lifelong Trajectory Planning via Non-Parametric Bayesian Memory-Adaptive Diffusion Experts](https://proceedings.mlr.press/v306/chen26d.html) · [Paper card (中文)](../../conferences/icml-2026/cards/0401-0500.md#paper-chen26d) | [Read insight (中文)](../../papers/robotics.md#chen26d-training-strategies) |
| [Generalizable and Actionable Parts Pose Estimation with Symmetry Annotation-Free Learning Strategy](https://proceedings.mlr.press/v306/chen26fw.html) · [Paper card (中文)](../../conferences/icml-2026/cards/0601-0700.md#paper-chen26fw) | [Read insight (中文)](../../papers/robotics.md#chen26fw-training-strategies) |
| [Knowledge Diversion for Efficient Morphology Control and Policy Transfer](https://proceedings.mlr.press/v306/feng26n.html) · [Paper card (中文)](../../conferences/icml-2026/cards/1101-1200.md#paper-feng26n) | [Read insight (中文)](../../papers/robotics.md#feng26n-training-strategies) |
| [VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model](https://proceedings.mlr.press/v306/guo26i.html) | [Read insight (中文)](../../papers/robotics.md#guo26i-training-strategies) |

<a id="by-data-strategies"></a>

### Data Strategies

| Paper | Insight |
| :--- | :--- |
| [RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation](https://proceedings.mlr.press/v306/chen26j.html) · [Paper card (中文)](../../conferences/icml-2026/cards/0401-0500.md#paper-chen26j) | [Read insight (中文)](../../papers/robotics.md#chen26j-data-strategies) |
| [PhyScene3D: Physically Consistent Interactive 3D Tabletop Scene Generation](https://proceedings.mlr.press/v306/chen26ab.html) · [Paper card (中文)](../../conferences/icml-2026/cards/0401-0500.md#paper-chen26ab) | [Read insight (中文)](../../papers/robotics.md#chen26ab-data-strategies) |
| [Escaping the Diversity Trap in Robotic Manipulation via Anchor-Centric Adaptation](https://proceedings.mlr.press/v306/chen26cy.html) · [Paper card (中文)](../../conferences/icml-2026/cards/0501-0600.md#paper-chen26cy) | [Read insight (中文)](../../papers/robotics.md#chen26cy-data-strategies) |
| [EMBGuard: Constructing Hazard-Aware Guardrails for Safe Planning in Embodied Agents](https://proceedings.mlr.press/v306/choi26i.html) · [Paper card (中文)](../../conferences/icml-2026/cards/0701-0800.md#paper-choi26i) | [Read insight (中文)](../../papers/robotics.md#choi26i-data-strategies) |
| [Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds](https://proceedings.mlr.press/v306/fan26b.html) · [Paper card (中文)](../../conferences/icml-2026/cards/1001-1100.md#paper-fan26b) | [Read insight (中文)](../../papers/robotics.md#fan26b-data-strategies) |
| [DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos](https://proceedings.mlr.press/v306/gao26q.html) · [Paper card (中文)](../../conferences/icml-2026/cards/1201-1300.md#paper-gao26q) | [Read insight (中文)](../../papers/robotics.md#gao26q-data-strategies) |
| [LIMMT: Less Is More for Motion Tracking](https://proceedings.mlr.press/v306/guan26f.html) | [Read insight (中文)](../../papers/robotics.md#guan26f-data-strategies) |

<a id="by-inference"></a>

### Inference Strategies

| Paper | Insight |
| :--- | :--- |
| [PRISM: Perception Reasoning Interleaved for Sequential Decision Making.](https://proceedings.mlr.press/v306/aissi26a.html) · [Paper card (中文)](../../conferences/icml-2026/cards/0001-0100.md#paper-aissi26a) | [Read insight (中文)](../../papers/robotics.md#aissi26a-inference) |
| [Model-Based Diffusion Sampling for Predictive Control in Offline Decision Making](https://proceedings.mlr.press/v306/balim26a.html) · [Paper card (中文)](../../conferences/icml-2026/cards/0201-0300.md#paper-balim26a) | [Read insight (中文)](../../papers/robotics.md#balim26a-inference) |
| [Motion Planning in Compressed Representation Spaces](https://proceedings.mlr.press/v306/beyer26a.html) · [Paper card (中文)](../../conferences/icml-2026/cards/0201-0300.md#paper-beyer26a) | [Read insight (中文)](../../papers/robotics.md#beyer26a-inference) |
| [N2M: Bridging Navigation and Manipulation by Learning Pose Preference from Rollout](https://proceedings.mlr.press/v306/chai26a.html) · [Paper card (中文)](../../conferences/icml-2026/cards/0401-0500.md#paper-chai26a) | [Read insight (中文)](../../papers/robotics.md#chai26a-inference) |
| [PSG-Nav: Probabilistic Scene Graph Navigation via Multiverse Decision Making](https://proceedings.mlr.press/v306/chen26i.html) · [Paper card (中文)](../../conferences/icml-2026/cards/0401-0500.md#paper-chen26i) | [Read insight (中文)](../../papers/robotics.md#chen26i-inference) |
| [Rethinking Instruction Drift as a Sampling Error: SNR-Aware Power Distributions for Long-Horizon Robotic Planning](https://proceedings.mlr.press/v306/chen26co.html) · [Paper card (中文)](../../conferences/icml-2026/cards/0501-0600.md#paper-chen26co) | [Read insight (中文)](../../papers/robotics.md#chen26co-inference) |
| [EvoCF: Multi-Agent Collaboration via Agentic Memory-Driven Evolutionary Counterfactual Planning](https://proceedings.mlr.press/v306/chi26b.html) · [Paper card (中文)](../../conferences/icml-2026/cards/0701-0800.md#paper-chi26b) | [Read insight (中文)](../../papers/robotics.md#chi26b-inference) |
| [SCALE: Self-uncertainty Conditioned Adaptive Looking and Execution for Vision-Language-Action Models](https://proceedings.mlr.press/v306/choi26a.html) · [Paper card (中文)](../../conferences/icml-2026/cards/0701-0800.md#paper-choi26a) | [Read insight (中文)](../../papers/robotics.md#choi26a-inference) |
| [Efficient Skill Grounding via Code Refactoring with Small Language Models](https://proceedings.mlr.press/v306/choi26c.html) · [Paper card (中文)](../../conferences/icml-2026/cards/0701-0800.md#paper-choi26c) | [Read insight (中文)](../../papers/robotics.md#choi26c-inference) |
| [Functional Cache Grafting: Robust and Rapid Code-Policy Synthesis for Embodied Agents](https://proceedings.mlr.press/v306/chun26a.html) · [Paper card (中文)](../../conferences/icml-2026/cards/0701-0800.md#paper-chun26a) | [Read insight (中文)](../../papers/robotics.md#chun26a-inference) |
| [AdaNav: Adaptive Reasoning with Uncertainty for Vision-Language Navigation](https://proceedings.mlr.press/v306/ding26r.html) · [Paper card (中文)](../../conferences/icml-2026/cards/0901-1000.md#paper-ding26r) | [Read insight (中文)](../../papers/robotics.md#ding26r-inference) |
| [Reflex: Real-Time Vision-Language-Action Control through Streaming Inference](https://proceedings.mlr.press/v306/guo26l.html) | [Read insight (中文)](../../papers/robotics.md#guo26l-inference) |

<a id="by-representation-learning"></a>

### Representation Learning

| Paper | Insight |
| :--- | :--- |
| [XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations](https://proceedings.mlr.press/v306/fan26f.html) · [Paper card (中文)](../../conferences/icml-2026/cards/1001-1100.md#paper-fan26f) | [Read insight (中文)](../../papers/robotics.md#fan26f-representation-learning) |
| [Geodesic Flow Matching for Denoising High-Dimensional Structured Representations](https://proceedings.mlr.press/v306/habashy26a.html) | [Read insight (中文)](../../papers/robotics.md#habashy26a-representation-learning) |

<a id="by-evaluation"></a>

### Evaluation and Diagnostics

| Paper | Insight |
| :--- | :--- |
| [SafeLab: An Interactive High-Fidelity Benchmark for Embodied Safety in Scientific Robotics](https://proceedings.mlr.press/v306/bai26e.html) · [Paper card (中文)](../../conferences/icml-2026/cards/0101-0200.md#paper-bai26e) | [Read insight (中文)](../../papers/robotics.md#bai26e-evaluation) |
| [DLO-Lab: Benchmarking Deformable Linear Object Manipulations with Differentiable Physics](https://proceedings.mlr.press/v306/cao26w.html) · [Paper card (中文)](../../conferences/icml-2026/cards/0401-0500.md#paper-cao26w) | [Read insight (中文)](../../papers/robotics.md#cao26w-evaluation) |
| [RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies](https://proceedings.mlr.press/v306/dai26c.html) · [Paper card (中文)](../../conferences/icml-2026/cards/0801-0900.md#paper-dai26c) | [Read insight (中文)](../../papers/robotics.md#dai26c-evaluation) |
| [Rethinking Video Generation Model for the Embodied World](https://proceedings.mlr.press/v306/deng26r.html) · [Paper card (中文)](../../conferences/icml-2026/cards/0801-0900.md#paper-deng26r) | [Read insight (中文)](../../papers/robotics.md#deng26r-evaluation) |
| [Demystifying Action Space Design for Robotic Manipulation Policies](https://proceedings.mlr.press/v306/feng26ab.html) · [Paper card (中文)](../../conferences/icml-2026/cards/1101-1200.md#paper-feng26ab) | [Read insight (中文)](../../papers/robotics.md#feng26ab-evaluation) |
| [CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation](https://proceedings.mlr.press/v306/fu26u.html) · [Paper card (中文)](../../conferences/icml-2026/cards/1101-1200.md#paper-fu26u) | [Read insight (中文)](../../papers/robotics.md#fu26u-evaluation) |

<a id="by-theory-statistics"></a>

### Theory and Statistics

| Paper | Insight |
| :--- | :--- |
| [Temporal Difference Calibration in Sequential Tasks: Application to Vision-Language-Action Models](https://proceedings.mlr.press/v306/francis-meretzki26a.html) · [Paper card (中文)](../../conferences/icml-2026/cards/1101-1200.md#paper-francis-meretzki26a) | [Read insight (中文)](../../papers/robotics.md#francis-meretzki26a-theory-statistics) |
<!-- classification:end -->
