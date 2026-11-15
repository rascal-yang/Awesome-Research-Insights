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
