# Loss Functions

[Home](../../README.en.md) · [Contributing](../CONTRIBUTING.md) · [简体中文](../../insights/loss-functions.md)

Objectives, auxiliary supervision, and regularization.

## Auxiliary Visual Supervision

### Target-Region Reconstruction as Auxiliary Supervision

**Source**

ReconVLA (Song et al., AAAI 2026) · [§§3.2–3.3, Figure 3 and Eq. 3](https://ojs.aaai.org/index.php/AAAI/article/download/38921/42883#page=4) · [§4.4, Table 2](https://ojs.aaai.org/index.php/AAAI/article/download/38921/42883#page=6) · [Paper index](../papers/robotics.md#vision-language-action-models)

**Core Idea**

Train a policy representation to recover the region the task depends on. The same camera image supplies the policy observation and the pixels used to build the auxiliary target.

**Mechanism**

Use an instruction-conditioned detector to prepare a target crop for training. Encode the crop with a VAE, add noise to its latent tokens, and train a diffusion transformer to predict the noise using reconstruction tokens from the policy backbone as its conditioning. Optimize the denoising loss jointly with action-token cross-entropy. At deployment, the policy takes its usual observations and instruction and emits actions.

**Motivation**

The authors observed that action prediction could attend to distractors. A target-region objective gives the shared representation a direct reason to retain fine details of the object being acted on.

**Potential Applications**

- **Paper evidence · Robot manipulation.** On CALVIN ABC→D, without large-scale pretraining, target-crop reconstruction averaged 3.85 consecutive tasks completed out of 5, versus 3.42 for whole-image reconstruction and 3.36 for the baseline (Table 2).
- **Transfer hypothesis · Small visuomotor policies.** Supervise the features that feed the action head using target or contact patches. This requires reliable per-frame crops during training, such as projected ground-truth boxes in simulation. A lightweight feature-prediction head is a possible adaptation whose effectiveness needs testing.

Related insight: [Instruction Prefixes for Causal Visual Grounding](modules.md#instruction-prefixes-for-causal-visual-grounding).
