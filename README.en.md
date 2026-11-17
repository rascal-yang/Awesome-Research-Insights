<a id="top"></a>

<p align="center">
  <img src="assets/banner.svg" width="100%" alt="Papers, techniques, and transfer">
</p>

<h1 align="center">Awesome Research Insights</h1>

<p align="center"><strong>Discover ideas. Transfer methods. Explore new possibilities.</strong></p>

<p align="center">
  <a href="README.md">简体中文</a> · <strong>English</strong> · <a href="en/CONTRIBUTING.md">Contribute</a>
</p>

A cross-disciplinary collection of reusable modules, losses, optimization methods, and training strategies from research papers.

**Latest additions · 2026-11-17** · [ICML 2026 · 303 / 6,552 papers with insights](conferences/icml-2026/README.md)

**Last reviewed · 2026-11-15** · Initial entries and cross-links

**Contents**

- [All Paper Domains](#papers-by-domain)
- [ICML 2026 Paper Insights](conferences/icml-2026/README.md)
- [Robotics](#robotics)
  - [Loss Functions](#loss-functions)
  - [Modules](#modules)
- [Computer Vision](#computer-vision)
  - [Modules](#computer-vision-modules)
- [Reinforcement Learning](#reinforcement-learning)
  - [Reward and Advantage Estimation](#reward-and-advantage-estimation)
- [Browse by Technique](#insights-by-technical-category)
- [Conference Sources and Update Cadence](#conference-sources)
- [Recent Updates](#recent-updates)
- [Contributing](#contributing)

<a id="papers-by-domain"></a>

## All Paper Domains

| Domain or conference | Papers | Scope |
| :--- | ---: | :--- |
| <a id="large-language-models"></a>[Large Language Models](en/papers/llm.md) | 0 | Language modeling, post-training, and reasoning. |
| [Computer Vision](#computer-vision) | 1 | Recognition, visual representations, and generation. |
| <a id="natural-language-processing"></a>[Natural Language Processing](en/papers/nlp.md) | 0 | Language processing, retrieval, and structured prediction. |
| [Reinforcement Learning](#reinforcement-learning) | 1 | Learning from interaction, feedback, and offline experience. |
| [Robotics](#robotics) | 2 | Robot perception, policy learning, planning, and control. |
| <a id="multimodal-learning"></a>[Multimodal Learning](en/papers/multimodal.md) | 0 | Learning from images, text, audio, and other modalities. |
| [ICML 2026 (cross-disciplinary)](conferences/icml-2026/README.md) | 303 | Insights in proceedings order across 6,552 papers. This count includes the 3 previously featured papers. |

## Robotics

[Paper index](en/papers/robotics.md)

### Loss Functions

| Insight | One-sentence takeaway | Source |
| :--- | :--- | :--- |
| [**Target-Region Reconstruction as Auxiliary Supervision**](en/insights/loss-functions.md#target-region-reconstruction-as-auxiliary-supervision) | Train the policy representation with a latent reconstruction objective on a crop of the target object. | [ReconVLA](en/papers/robotics.md#vision-language-action-models) |
| [**Align Action-Expert Features with Latent Actions**](en/insights/loss-functions.md#align-action-features-with-latent-actions) | Align an intermediate action-model layer with latent actions learned from frame pairs. | [LARA](en/papers/robotics.md#vision-language-action-models) |

### Modules

| Insight | One-sentence takeaway | Source |
| :--- | :--- | :--- |
| [**Instruction Prefixes for Causal Visual Grounding**](en/insights/modules.md#instruction-prefixes-for-causal-visual-grounding) | Place instruction tokens before image tokens so visual hidden states can attend to the task under a causal mask. | [ReconVLA](en/papers/robotics.md#vision-language-action-models) |

## Computer Vision

[Paper index](en/papers/computer-vision.md)

<a id="computer-vision-modules"></a>

### Modules

| Insight | One-sentence takeaway | Source |
| :--- | :--- | :--- |
| [**Widen the Student Distillation Interface**](en/insights/modules.md#widen-the-student-distillation-interface) | Widen the student’s feature interface or final Transformer block for feature distillation. | [Lift / WideLast](en/papers/computer-vision.md#vision-model-distillation) |

## Reinforcement Learning

[Paper index](en/papers/reinforcement-learning.md)

### Reward and Advantage Estimation

| Insight | One-sentence takeaway | Source |
| :--- | :--- | :--- |
| [**Normalize Each Reward Before Aggregation**](en/insights/reinforcement-learning.md#normalize-each-reward-before-aggregation) | Normalize each reward component within a rollout group before combining advantages. | [GDPO](en/papers/reinforcement-learning.md#group-relative-policy-optimization) |

<a id="insights-by-technical-category"></a>

## Browse by Technique

Browse the complete technique indexes across domains.

| Technique | Scope |
| :--- | :--- |
| <a id="architectures"></a>[Architectures](en/insights/architecture.md) | Model-wide design and information flow. |
| [Modules](en/insights/modules.md) | Reusable components and local changes to model connections. |
| [Loss Functions](en/insights/loss-functions.md) | Objectives, auxiliary supervision, and regularization. |
| <a id="optimization"></a>[Optimization](en/insights/optimization.md) | Gradient updates, parameterization, and optimization dynamics. |
| <a id="reinforcement-learning-methods"></a>[Reinforcement Learning Methods](en/insights/reinforcement-learning.md) | Rewards, exploration, credit assignment, and policy improvement. |
| <a id="training-strategies"></a>[Training Strategies](en/insights/training-strategies.md) | Training schedules, curricula, and task or stage composition. |
| <a id="data-strategies"></a>[Data Strategies](en/insights/data-strategies.md) | Data selection, annotation, augmentation, and sampling. |
| <a id="inference-strategies"></a>[Inference Strategies](en/insights/inference.md) | Decoding, test-time adaptation, and efficient execution. |

<p align="right"><a href="#top">↑ Back to top</a></p>

<a id="conference-sources"></a>

## Conference Sources and Update Cadence

The initial collection prioritizes **main-conference papers from the 2025 and 2026 editions of CCF A venues**. We also consult the specialist venues below when relevant to a topic.

| Source | Conferences | Topics to look for |
| :--- | :--- | :--- |
| CCF A · Machine learning and AI | ICML, NeurIPS, ICLR, AAAI | Losses, representation learning, optimization, training strategies, and reinforcement learning |
| CCF A · Computer vision | CVPR, ICCV | Visual supervision, video and temporal representations, and 3D perception |
| CCF A · Natural language processing | ACL | Instruction following, reasoning, and language representations |
| Robot learning and systems | CoRL, RSS | Policy learning, imitation learning, planning, and manipulation |
| Topic-specific sources | EMNLP, ECCV, ICRA, IROS | Language and multimodal methods, perception and control, contact, and physical robot execution |

We update in batches after conferences publish their official main-conference acceptance lists or proceedings. For ICML 2026, we review papers individually in proceedings order.

**Inclusion criterion.** One clear, independently explainable insight supported by the paper is enough to include it. Record the conditions under which it holds and what the experiment, theorem, or counterexample establishes. Transfer scenarios are optional.

## Recent Updates

- **2026-11-17** · Added Chinese insights for ICML 2026 papers 161–300. [Conference index](conferences/icml-2026/README.md)

- **2026-11-17** · Added the ICML 2026 proceedings index and Chinese insights for papers 1–160, plus links to the three previously featured papers. [ICML 2026 Paper Insights](conferences/icml-2026/README.md)

<a id="icml-2026-first-batch"></a>

- **2026-11-15** · Added three papers and three insights from [ICML 2026](https://proceedings.mlr.press/v306/). [Align Action-Expert Features with Latent Actions](en/insights/loss-functions.md#align-action-features-with-latent-actions) · [Widen the Student Distillation Interface](en/insights/modules.md#widen-the-student-distillation-interface) · [Normalize Each Reward Before Aggregation](en/insights/reinforcement-learning.md#normalize-each-reward-before-aggregation)

- **2026-11-15** · Added two insights from ReconVLA (AAAI 2026). [Target-region reconstruction](en/insights/loss-functions.md#target-region-reconstruction-as-auxiliary-supervision) · [Instruction prefixes](en/insights/modules.md#instruction-prefixes-for-causal-visual-grounding)

## Contributing

See the [contribution guide](en/CONTRIBUTING.md) to submit a paper, add an insight, or correct an entry.

[MIT License](LICENSE)
