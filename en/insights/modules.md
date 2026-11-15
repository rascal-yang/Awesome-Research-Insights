# Modules

[Home](../../README.en.md) · [Contributing](../CONTRIBUTING.md) · [简体中文](../../insights/modules.md)

Reusable components and local changes to model inputs or connections.

## Multimodal Token Layout

### Instruction Prefixes for Causal Visual Grounding

**Source**

ReconVLA (Song et al., AAAI 2026) · [§3.2, Figure 3 and the causal-attention discussion](https://ojs.aaai.org/index.php/AAAI/article/download/38921/42883#page=4) · [Paper index](../papers/robotics.md#vision-language-action-models)

**Core Idea**

Put the task instruction before the image tokens when a causal decoder needs to produce task-conditioned visual representations.

**Mechanism**

In a decoder with a standard causal mask, an image-token hidden state can attend to earlier instruction tokens. ReconVLA places instruction tokens before image tokens so that the visual states used to condition the reconstruction branch can carry task information. The order acts inside the multimodal decoder. The vision encoder still processes the image separately.

**Motivation**

The same image can contain several manipulable objects. A reconstruction target selected by the instruction is easier to represent when the visual states can see the task before the reconstruction head reads them.

**Potential Applications**

- **Paper use · Language-conditioned reconstruction.** ReconVLA uses this layout in its reconstruction pipeline. The paper does not report a controlled token-order ablation that isolates its effect on policy success.
- **Transfer hypothesis · Decoder-only vision-language policies.** Move a goal or question ahead of image tokens if an auxiliary head reads their hidden states. Check the actual attention mask and readout position. A head that already reads a post-instruction state can have access to the goal under either layout.

Related insight: [Target-Region Reconstruction as Auxiliary Supervision](loss-functions.md#target-region-reconstruction-as-auxiliary-supervision).

## Distillation Interface Design

### Widen the Student Distillation Interface

**Source**

[Lift / WideLast](https://proceedings.mlr.press/v306/tian26k.html) (Huiyuan Tian et al., ICML 2026) · [§§2.1–2.3](https://raw.githubusercontent.com/mlresearch/v306/main/assets/tian26k/tian26k.pdf#page=4) · [§§3.1–3.3 and Table 2](https://raw.githubusercontent.com/mlresearch/v306/main/assets/tian26k/tian26k.pdf#page=6) · [Table 8](https://raw.githubusercontent.com/mlresearch/v306/main/assets/tian26k/tian26k.pdf#page=9) · [Paper index](../papers/computer-vision.md#vision-model-distillation)

**Core Idea**

When distilling into a substantially narrower ViT, widen the interface where it meets the teacher and keep most earlier layers narrow.

**Mechanism**

Lift applies a token-wise linear expansion after the final student layer. The classifier consumes the expanded features, and the projection remains at inference. WideLast widens only the final Transformer block to teacher width. Either interface can take a feature loss.

**Motivation**

Teacher features can be low rank for each image while occupying different subspaces across inputs. Shared PCA across images gives a better check on whether a fixed, narrow interface can cover those features than per-image SVD alone.

**Potential Applications**

- **Paper evidence** · On ImageNet-1K with CaiT-S24 as teacher and DeiT-Tiny as student, the standalone baseline was 74.86% top-1. The best Lift and WideLast settings reached 77.53% and 78.23% (Table 2). Wider interfaces also helped without distillation (Table 8).
- **Transfer hypothesis** · For a compact visual encoder, compare widening alone with widening plus distillation and report deployment cost. This can help isolate benefits from capacity and from teacher supervision.
