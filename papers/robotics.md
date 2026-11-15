# 机器人学

[首页](../README.md) · [参与贡献](../CONTRIBUTING.md) · [English](../en/papers/robotics.md)

机器人感知、策略学习、规划与控制。

<a id="vision-language-action-models"></a>

## 视觉—语言—动作模型

| 论文 | 首次公开 / 发表 | 可借鉴的技术 | 资源 |
| :--- | :--- | :--- | :--- |
| [**ReconVLA**](https://arxiv.org/abs/2508.10333)<br><sub>Song et al., ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver</sub> | 2025-08-14<br><sub>[AAAI 2026](https://ojs.aaai.org/index.php/AAAI/article/download/38921/42883)</sub> | [用目标区域重建做辅助监督](../insights/loss-functions.md#target-region-reconstruction-as-auxiliary-supervision)<br>[用指令前缀让视觉表征感知任务](../insights/modules.md#instruction-prefixes-for-causal-visual-grounding) | [论文](https://arxiv.org/abs/2508.10333) · [项目](https://zionchow.github.io/ReconVLA/) · [代码](https://github.com/OpenHelix-Team/ReconVLA) |
| [**LARA**](https://proceedings.mlr.press/v306/liu26bl.html)<br><sub>Mengya Liu 等, LARA: Latent Action Representation Alignment for Vision-Language-Action Models</sub> | [2026-06-05](https://arxiv.org/abs/2606.07100)<br><sub>[ICML 2026](https://proceedings.mlr.press/v306/liu26bl.html)</sub> | [用潜动作监督动作专家的中间层](../insights/loss-functions.md#align-action-features-with-latent-actions) | [PMLR](https://proceedings.mlr.press/v306/liu26bl.html) · [arXiv](https://arxiv.org/abs/2606.07100) · [代码](https://github.com/lmy1001/LARA) |
