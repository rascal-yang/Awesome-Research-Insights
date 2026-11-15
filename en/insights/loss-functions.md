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

## Latent Action Alignment

<a id="align-action-features-with-latent-actions"></a>

### Align Action-Expert Features with Latent Actions

**Source**

[LARA](https://proceedings.mlr.press/v306/liu26bl.html) (Mengya Liu et al., ICML 2026) · [§4.1, Figure 3, Eqs. 6–7](https://raw.githubusercontent.com/mlresearch/v306/main/assets/liu26bl/liu26bl.pdf#page=4) · [Table 2](https://raw.githubusercontent.com/mlresearch/v306/main/assets/liu26bl/liu26bl.pdf#page=7) · [§5.6, Figure 6](https://raw.githubusercontent.com/mlresearch/v306/main/assets/liu26bl/liu26bl.pdf#page=8) · [Paper index](../papers/robotics.md#vision-language-action-models)

**Core Idea**

Align intermediate action-expert features with a latent action inferred from two frames, adding supervision about state changes.

**Mechanism**

An inverse dynamics encoder extracts a continuous latent action from the current and future frame. Project an intermediate action DiT feature and apply cosine alignment to the pre-quantization latent action. Jointly optimize action flow matching, alignment, and future-frame reconstruction in the latent action model, allowing alignment gradients into both branches. The future frame supplies training supervision.

**Motivation**

Video reconstruction can encode nuisance changes such as lighting. Behavior cloning mainly supervises action prediction. Joint training lets visual changes and the action representation constrain each other.

**Potential Applications**

- **Paper evidence** · In GR00T-N1.6 post-training on G1, average full-task success rose from 72% to 76% across two tasks with 50 trials each. Full Grasp-n-Pour success was 68% in both settings. On LIBERO-Long, joint training beat the frozen latent-action baseline. The best alignment layer varied by backbone.
- **Transfer hypothesis** · For a small VLA, compare action loss alone, frozen latent-action supervision, and joint training. This needs aligned frame pairs and action labels. A layer near the action output is a starting point.
