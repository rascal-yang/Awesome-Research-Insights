# Robotics

[Home](../../README.en.md) · [Contributing](../CONTRIBUTING.md) · [简体中文](../../papers/robotics.md)

Robot perception, policy learning, planning, and control.

## Vision-Language-Action Models

| Paper | First public / venue | Transferable insights | Resources |
| :--- | :--- | :--- | :--- |
| **ReconVLA**<br>Song et al., *ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver* | 2025-08-14<br><sub>[AAAI 2026](https://ojs.aaai.org/index.php/AAAI/article/download/38921/42883)</sub> | [Target-Region Reconstruction as Auxiliary Supervision](../insights/loss-functions.md#target-region-reconstruction-as-auxiliary-supervision) · [Instruction Prefixes for Causal Visual Grounding](../insights/modules.md#instruction-prefixes-for-causal-visual-grounding) | [Paper](https://arxiv.org/abs/2508.10333) · [Project](https://zionchow.github.io/ReconVLA/) · [Code](https://github.com/OpenHelix-Team/ReconVLA) |
| [**LARA**](https://proceedings.mlr.press/v306/liu26bl.html)<br><sub>Mengya Liu et al., LARA: Latent Action Representation Alignment for Vision-Language-Action Models</sub> | [2026-06-05](https://arxiv.org/abs/2606.07100)<br><sub>[ICML 2026](https://proceedings.mlr.press/v306/liu26bl.html)</sub> | [Align Action-Expert Features with Latent Actions](../insights/loss-functions.md#align-action-features-with-latent-actions) | [PMLR](https://proceedings.mlr.press/v306/liu26bl.html) · [arXiv](https://arxiv.org/abs/2606.07100) · [Code](https://github.com/lmy1001/LARA) |

<!-- classification:start -->
## Browse by Technique

The linked short insights are available in Chinese.

<a id="by-architecture"></a>

### Architectures

| Paper | Insight |
| :--- | :--- |
| [Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models](https://proceedings.mlr.press/v306/bai26h.html) | [Read insight (中文)](../../papers/robotics.md#bai26h-architecture) |
| [Hierarchical Policy Learning via Spectral Decomposition](https://proceedings.mlr.press/v306/cao26u.html) | [Read insight (中文)](../../papers/robotics.md#cao26u-architecture) |
| [The Lie We Tell: Correcting the Euclidean Fallacy in Vision Language Action Policies via Score Matching on Tangent Space](https://proceedings.mlr.press/v306/chuang26a.html) | [Read insight (中文)](../../papers/robotics.md#chuang26a-architecture) |
| [Embodied-DETR: End-to-End Temporal 3D Object Detection in Egocentric Views](https://proceedings.mlr.press/v306/ding26x.html) | [Read insight (中文)](../../papers/robotics.md#ding26x-architecture) |

<a id="by-modules"></a>

### Modules

| Paper | Insight |
| :--- | :--- |
| [ReconVLA](https://arxiv.org/abs/2508.10333) | [Read insight (中文)](../../papers/robotics.md#reconvla-modules) · [Full entry](../insights/modules.md#instruction-prefixes-for-causal-visual-grounding) |

<a id="by-loss-functions"></a>

### Loss Functions

| Paper | Insight |
| :--- | :--- |
| [DT²: Decision-Targeted Digital Twins](https://proceedings.mlr.press/v306/amad26a.html) | [Read insight (中文)](../../papers/robotics.md#amad26a-loss-functions) |
| [LARA: Latent Action Representation Alignment for Vision-Language-Action Models](https://proceedings.mlr.press/v306/liu26bl.html) | [Read insight (中文)](../../papers/robotics.md#liu26bl-loss-functions) · [Full entry](../insights/loss-functions.md#align-action-features-with-latent-actions) |
| [ReconVLA](https://arxiv.org/abs/2508.10333) | [Read insight (中文)](../../papers/robotics.md#reconvla-loss-functions) · [Full entry](../insights/loss-functions.md#target-region-reconstruction-as-auxiliary-supervision) |

<a id="by-optimization"></a>

### Optimization

| Paper | Insight |
| :--- | :--- |
| [Blending Neural Control Density Functions for Stabilization and Safety](https://proceedings.mlr.press/v306/chaudhary26a.html) | [Read insight (中文)](../../papers/robotics.md#chaudhary26a-optimization) |

<a id="by-reinforcement-learning"></a>

### Reinforcement Learning Methods

| Paper | Insight |
| :--- | :--- |
| [Learning to Search and Searching to Learn for Generalization in Planning](https://proceedings.mlr.press/v306/aichmuller26a.html) | [Read insight (中文)](../../papers/robotics.md#aichmuller26a-reinforcement-learning) |
| [LAGEA: Language Guided Embodied Agents for Robotic Manipulation](https://proceedings.mlr.press/v306/chowdhury26a.html) | [Read insight (中文)](../../papers/robotics.md#chowdhury26a-reinforcement-learning) |

<a id="by-training-strategies"></a>

### Training Strategies

| Paper | Insight |
| :--- | :--- |
| [NOMAD: Lifelong Trajectory Planning via Non-Parametric Bayesian Memory-Adaptive Diffusion Experts](https://proceedings.mlr.press/v306/chen26d.html) | [Read insight (中文)](../../papers/robotics.md#chen26d-training-strategies) |
| [Generalizable and Actionable Parts Pose Estimation with Symmetry Annotation-Free Learning Strategy](https://proceedings.mlr.press/v306/chen26fw.html) | [Read insight (中文)](../../papers/robotics.md#chen26fw-training-strategies) |

<a id="by-data-strategies"></a>

### Data Strategies

| Paper | Insight |
| :--- | :--- |
| [RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation](https://proceedings.mlr.press/v306/chen26j.html) | [Read insight (中文)](../../papers/robotics.md#chen26j-data-strategies) |
| [PhyScene3D: Physically Consistent Interactive 3D Tabletop Scene Generation](https://proceedings.mlr.press/v306/chen26ab.html) | [Read insight (中文)](../../papers/robotics.md#chen26ab-data-strategies) |
| [Escaping the Diversity Trap in Robotic Manipulation via Anchor-Centric Adaptation](https://proceedings.mlr.press/v306/chen26cy.html) | [Read insight (中文)](../../papers/robotics.md#chen26cy-data-strategies) |
| [EMBGuard: Constructing Hazard-Aware Guardrails for Safe Planning in Embodied Agents](https://proceedings.mlr.press/v306/choi26i.html) | [Read insight (中文)](../../papers/robotics.md#choi26i-data-strategies) |

<a id="by-inference"></a>

### Inference Strategies

| Paper | Insight |
| :--- | :--- |
| [PRISM: Perception Reasoning Interleaved for Sequential Decision Making.](https://proceedings.mlr.press/v306/aissi26a.html) | [Read insight (中文)](../../papers/robotics.md#aissi26a-inference) |
| [Model-Based Diffusion Sampling for Predictive Control in Offline Decision Making](https://proceedings.mlr.press/v306/balim26a.html) | [Read insight (中文)](../../papers/robotics.md#balim26a-inference) |
| [Motion Planning in Compressed Representation Spaces](https://proceedings.mlr.press/v306/beyer26a.html) | [Read insight (中文)](../../papers/robotics.md#beyer26a-inference) |
| [N2M: Bridging Navigation and Manipulation by Learning Pose Preference from Rollout](https://proceedings.mlr.press/v306/chai26a.html) | [Read insight (中文)](../../papers/robotics.md#chai26a-inference) |
| [PSG-Nav: Probabilistic Scene Graph Navigation via Multiverse Decision Making](https://proceedings.mlr.press/v306/chen26i.html) | [Read insight (中文)](../../papers/robotics.md#chen26i-inference) |
| [Rethinking Instruction Drift as a Sampling Error: SNR-Aware Power Distributions for Long-Horizon Robotic Planning](https://proceedings.mlr.press/v306/chen26co.html) | [Read insight (中文)](../../papers/robotics.md#chen26co-inference) |
| [EvoCF: Multi-Agent Collaboration via Agentic Memory-Driven Evolutionary Counterfactual Planning](https://proceedings.mlr.press/v306/chi26b.html) | [Read insight (中文)](../../papers/robotics.md#chi26b-inference) |
| [SCALE: Self-uncertainty Conditioned Adaptive Looking and Execution for Vision-Language-Action Models](https://proceedings.mlr.press/v306/choi26a.html) | [Read insight (中文)](../../papers/robotics.md#choi26a-inference) |
| [Efficient Skill Grounding via Code Refactoring with Small Language Models](https://proceedings.mlr.press/v306/choi26c.html) | [Read insight (中文)](../../papers/robotics.md#choi26c-inference) |
| [Functional Cache Grafting: Robust and Rapid Code-Policy Synthesis for Embodied Agents](https://proceedings.mlr.press/v306/chun26a.html) | [Read insight (中文)](../../papers/robotics.md#chun26a-inference) |
| [AdaNav: Adaptive Reasoning with Uncertainty for Vision-Language Navigation](https://proceedings.mlr.press/v306/ding26r.html) | [Read insight (中文)](../../papers/robotics.md#ding26r-inference) |

<a id="by-evaluation"></a>

### Evaluation and Diagnostics

| Paper | Insight |
| :--- | :--- |
| [SafeLab: An Interactive High-Fidelity Benchmark for Embodied Safety in Scientific Robotics](https://proceedings.mlr.press/v306/bai26e.html) | [Read insight (中文)](../../papers/robotics.md#bai26e-evaluation) |
| [DLO-Lab: Benchmarking Deformable Linear Object Manipulations with Differentiable Physics](https://proceedings.mlr.press/v306/cao26w.html) | [Read insight (中文)](../../papers/robotics.md#cao26w-evaluation) |
| [RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies](https://proceedings.mlr.press/v306/dai26c.html) | [Read insight (中文)](../../papers/robotics.md#dai26c-evaluation) |
| [Rethinking Video Generation Model for the Embodied World](https://proceedings.mlr.press/v306/deng26r.html) | [Read insight (中文)](../../papers/robotics.md#deng26r-evaluation) |
<!-- classification:end -->
