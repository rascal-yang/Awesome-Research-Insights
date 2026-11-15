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

**Latest additions · 2026-11-15** · [Two insights from ReconVLA](#recent-updates)

**Last reviewed · 2026-11-15** · Initial entries and cross-links

**Contents**

- [Papers by Domain](#papers-by-domain)
  - [Robotics](#robotics)
- [Insights by Technical Category](#insights-by-technical-category)
  - [Loss Functions](#loss-functions)
  - [Modules](#modules)
- [Conference Sources and Update Cadence](#conference-sources)
- [Recent Updates](#recent-updates)
- [Contributing](#contributing)

## Papers by Domain

Browse by the paper’s primary field, then follow its links to individual techniques.

### Robotics

| Paper | First public / venue | Transferable insights | Resources |
| :--- | :--- | :--- | :--- |
| [**ReconVLA**](en/papers/robotics.md#vision-language-action-models)<br><sub>Song et al.</sub> | 2025-08-14<br><sub>[AAAI 2026](https://ojs.aaai.org/index.php/AAAI/article/download/38921/42883)</sub> | [Target-region reconstruction](en/insights/loss-functions.md#target-region-reconstruction-as-auxiliary-supervision)<br>[Instruction prefixes](en/insights/modules.md#instruction-prefixes-for-causal-visual-grounding) | [Paper](https://arxiv.org/abs/2508.10333) · [Project](https://zionchow.github.io/ReconVLA/) · [Code](https://github.com/OpenHelix-Team/ReconVLA) |

**All Paper Domains**

| Domain | Papers | Scope |
| :--- | ---: | :--- |
| <a id="large-language-models"></a>[Large Language Models](en/papers/llm.md) | 0 | Language modeling, post-training, and reasoning. |
| <a id="computer-vision"></a>[Computer Vision](en/papers/computer-vision.md) | 0 | Recognition, visual representations, and generation. |
| <a id="natural-language-processing"></a>[Natural Language Processing](en/papers/nlp.md) | 0 | Language processing, retrieval, and structured prediction. |
| <a id="reinforcement-learning"></a>[Reinforcement Learning](en/papers/reinforcement-learning.md) | 0 | Learning from interaction, feedback, and offline experience. |
| [Robotics](en/papers/robotics.md) | 1 | Robot perception, policy learning, planning, and control. |
| <a id="multimodal-learning"></a>[Multimodal Learning](en/papers/multimodal.md) | 0 | Learning from images, text, audio, and other modalities. |

<p align="right"><a href="#top">↑ Back to top</a></p>

## Insights by Technical Category

Start with the kind of change you want to borrow, such as an auxiliary loss, a module, or a training strategy.

### Loss Functions

| Insight | One-sentence takeaway | Source |
| :--- | :--- | :--- |
| [**Target-Region Reconstruction as Auxiliary Supervision**](en/insights/loss-functions.md#target-region-reconstruction-as-auxiliary-supervision) | Train the policy representation with a latent reconstruction objective on a crop of the target object. | [ReconVLA](en/papers/robotics.md#vision-language-action-models) |

### Modules

| Insight | One-sentence takeaway | Source |
| :--- | :--- | :--- |
| [**Instruction Prefixes for Causal Visual Grounding**](en/insights/modules.md#instruction-prefixes-for-causal-visual-grounding) | Place instruction tokens before image tokens so visual hidden states can attend to the task under a causal mask. | [ReconVLA](en/papers/robotics.md#vision-language-action-models) |

**All Technical Categories**

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

We screen papers by technical topic when a conference publishes its official main-conference acceptance list or proceedings. To include an insight, we look for an accessible full paper, a traceable source for the method, and a concrete transfer scenario. Batches follow conference announcements.

## Recent Updates

- **2026-11-15** · Added two insights from ReconVLA (AAAI 2026). [Target-region reconstruction](en/insights/loss-functions.md#target-region-reconstruction-as-auxiliary-supervision) · [Instruction prefixes](en/insights/modules.md#instruction-prefixes-for-causal-visual-grounding)

## Contributing

See the [contribution guide](en/CONTRIBUTING.md) to submit a paper, add an insight, or correct an entry.

[MIT License](LICENSE)
