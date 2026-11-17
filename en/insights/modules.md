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

<!-- classification:start -->
## Browse by Research Domain

### Large Language Models

- [Learning to Remember, Learn, and Forget in Attention-Based Models](../../papers/llm.md#bonnet26a-modules) · 中文
- [Bounded Hyperbolic Tangent: A Stable and Efficient Alternative to Pre-Layer Normalization in Large Language Models](../../papers/llm.md#byun26a-modules) · 中文
- [SpanNorm: Reconciling Training Stability and Performance in Deep Transformers](../../papers/llm.md#chao26b-modules) · 中文
- [Doc-to-LoRA: Learning to Instantly Internalize Contexts](../../papers/llm.md#charakorn26a-modules) · 中文
- [Multi-Head Attention as a Source of Catastrophic Forgetting in MoE Transformers](../../papers/llm.md#chen26aw-modules) · 中文
- [SimpleGPT: Improving GPT via A Simple Normalization Strategy](../../papers/llm.md#chen26dj-modules) · 中文
- [Toward Stable Value Alignment: Introducing Independent Modules for Consistent Value Guidance](../../papers/llm.md#chen26dw-modules) · 中文
- [Learning When to Attend: Conditional Memory Access for Long-Context LLMs](../../papers/llm.md#choudhary26a-modules) · 中文
- [CoFrGeNet: Continued Fraction Architectures for Language Generation](../../papers/llm.md#dhurandhar26a-modules) · 中文
- [Eigenvectors of Experts are Training-free Non-collapsing Routers](../../papers/llm.md#do26a-modules) · 中文
- [LUCID: Attention with Preconditioned Representations](../../papers/llm.md#duvvuri26a-modules) · 中文
- [ExpWeaver: LLM Agents Learn from Experience via Latent RAG](../../papers/llm.md#feng26i-modules) · 中文
- [DAG-MoE: From Simple Mixture to Structural Aggregation in Mixture-of-Experts](../../papers/llm.md#feng26v-modules) · 中文
- [Softplus Attention with Re-weighting Boosts Length Extrapolation in Large Language Models](../../papers/llm.md#gao26y-modules) · 中文
- [AdaSplash-2: Faster Differentiable Sparse Attention](../../papers/llm.md#goncalves26a-modules) · 中文

### Computer Vision

- [FOVI: A biologically-inspired foveated interface for deep vision models](../../papers/computer-vision.md#blauch26a-modules) · 中文
- [Spatial Priors via Space Filling Curves for Small and Limited Data Vision Transformers](../../papers/computer-vision.md#candogan26a-modules) · 中文
- [Multi-Label Learning with Contrastive Cluster Self-Supervision for 3D Hierarchical Semantic Segmentation](../../papers/computer-vision.md#cao26j-modules) · 中文
- [LiteVSR: Lightweight Adaptation of Frozen Diffusion Transformers for Video Super-Resolution](../../papers/computer-vision.md#cao26n-modules) · 中文
- [StructMAR: Structure-Aware Masked Autoregression for Explicit Layout Alignment in Text-to-Image Generation](../../papers/computer-vision.md#cao26ab-modules) · 中文
- [WEVSR: Video Diffusion Generators for Real-World Video Super-Resolution with Wavelet-Enhanced VAE Encoder](../../papers/computer-vision.md#chen26ce-modules) · 中文
- [Attentive Multi-Layer Fusion for Vision Transformers](../../papers/computer-vision.md#ciernik26a-modules) · 中文
- [Prototype-Grounded Concept Models for Verifiable Concept Alignment](../../papers/computer-vision.md#colamonaco26a-modules) · 中文
- [Does a Hybrid Space-Aware Randomized Defense Improve Empirical and Certified Adversarial Robustness?](../../papers/computer-vision.md#dhar26a-modules) · 中文
- [PolarDepth: Monocular Transparent Object Depth from Polar-Physics Priors](../../papers/computer-vision.md#dong26i-modules) · 中文
- [MobileFusion: Mobile-Friendly Infrared and Visible Image Fusion via Structural Re-parameterization](../../papers/computer-vision.md#duan26a-modules) · 中文
- [WildActor: Unconstrained Identity-Preserving Video Generation](../../papers/computer-vision.md#guo26ad-modules) · 中文
- [Hierarchical Image Tokenization for Multi-Scale Image Super Resolution](../../papers/computer-vision.md#hadji26a-modules) · 中文
- [From Per-Image Low-Rank to Encoding Mismatch: Rethinking Feature Distillation in Vision Transformers](../insights/modules.md#widen-the-student-distillation-interface)

### Natural Language Processing

- [AgentVocab: Structure-Aware Vocabulary Adaptation for Efficient LLM Agents](../../papers/nlp.md#bian26c-modules) · 中文

### Robotics

- [See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model](../../papers/robotics.md#feng26x-modules) · 中文
- [StableVLA: Towards Robust Vision-Language-Action Models without Extra Data](../../papers/robotics.md#fu26x-modules) · 中文
- [Fourier Features Let Agents Learn High Precision Policies with Imitation Learning](../../papers/robotics.md#gyenes26a-modules) · 中文
- [ReconVLA](../insights/modules.md#instruction-prefixes-for-causal-visual-grounding)

### Multimodal Learning

- [MoDA: Modulation Adapter for Fine-Grained Visual Understanding in Instructional MLLMs](../../papers/multimodal.md#barrios26a-modules) · 中文
- [Hamiltonian Asymmetric Fusion: One-Way Safe Directed Refinement under Modality Imbalance](../../papers/multimodal.md#chen26ch-modules) · 中文
- [SPR: A Structured Prompt Refinement Network for Modality Missing](../../papers/multimodal.md#chen26dv-modules) · 中文
- [OmniSIFT: Modality-Asymmetric Token Compression for Efficient Omni-modal Large Language Models](../../papers/multimodal.md#ding26e-modules) · 中文
- [EchoingPixels: Aliasing-Resistant Joint Token Reduction for Audio-Visual LLMs](../../papers/multimodal.md#gong26g-modules) · 中文
- [DreamID-Omni: Unified Framework for Controllable Human-Centric Audio-Video Generation](../../papers/multimodal.md#guo26af-modules) · 中文

### Machine Learning Foundations and Statistics

- [Affine-Scaled Attention: Towards Flexible and Stable Transformer Attention](../../papers/ml-foundations.md#bae26d-modules) · 中文
- [Diving into Kronecker Adapters: Component Design Matters](../../papers/ml-foundations.md#bai26l-modules) · 中文
- [DOT-MoE: Differentiable Optimal Transport for MoEfication](../../papers/ml-foundations.md#bamba26a-modules) · 中文
- [Efficient Continuous-Depth Modeling with GRU Equivalents](../../papers/ml-foundations.md#banerjee26b-modules) · 中文
- [Memory Caching: RNNs with Growing Memory](../../papers/ml-foundations.md#behrouz26a-modules) · 中文
- [ATLAS: Learning to Optimally Memorize the Context at Test Time](../../papers/ml-foundations.md#behrouz26b-modules) · 中文
- [Time Series Forecasting Through the Lens of Dynamics](../../papers/ml-foundations.md#brachet26a-modules) · 中文
- [Improving the Performance and Learning Stability of Parallelizable RNNs Designed for Ultra-Low Power Applications](../../papers/ml-foundations.md#brandoit26a-modules) · 中文
- [Enhanced Multi-Instance Partial Label Learning via Average Gradient Outer Product](../../papers/ml-foundations.md#cao26af-modules) · 中文
- [The Geometry of Projection Heads: Conditioning, Invariance, and Collapse](../../papers/ml-foundations.md#chaudhry26a-modules) · 中文
- [Riemannian Networks over Full-Rank Correlation Matrices](../../papers/ml-foundations.md#chen26fb-modules) · 中文
- [Beyond Extrapolation: Knowledge Utilization Paradigm with Bidirectional Inspiration for Time Series Forecasting](../../papers/ml-foundations.md#chong26c-modules) · 中文
- [PLATE: Plasticity-Tunable Efficient Adapters for Geometry-Aware Continual Learning](../../papers/ml-foundations.md#cosentino26a-modules) · 中文
- [Rethinking Sparse Mixture of Experts from a Unified Perspective](../../papers/ml-foundations.md#do26b-modules) · 中文
- [FlashSketch: Sketch-Kernel Co-Design for Fast Sparse Sketching on GPUs](../../papers/ml-foundations.md#dwaraknath26a-modules) · 中文
- [Hide&Seek: Learning to Explain in an End-to-End Differentiable Network](../../papers/ml-foundations.md#ellinson26a-modules) · 中文
- [VBA: Vector Bundle Attention for Intrinsically Geometric Representation Learning](../../papers/ml-foundations.md#fang26q-modules) · 中文
- [Olivia: Harmonizing Time Series Foundation Models with Power Spectral Density](../../papers/ml-foundations.md#fei26b-modules) · 中文
- [Mantis: Lightweight Foundation Model for Time Series Classification](../../papers/ml-foundations.md#feofanov26a-modules) · 中文
- [HiPPO Zoo: Explicit Memory Mechanisms for Interpretable State Space Models](../../papers/ml-foundations.md#goffinet26a-modules) · 中文
- [Decoupling The "What" and "Where" With Polar Coordinate Positional Embedding](../../papers/ml-foundations.md#gopalakrishnan26a-modules) · 中文
- [Byte Pair Encoding for Efficient Time Series Forecasting](../../papers/ml-foundations.md#gotz26a-modules) · 中文
- [Temporal Weighted Encoding: Towards Maximal-Capacity Spike Coding for ANN–SNN Conversion](../../papers/ml-foundations.md#gu26d-modules) · 中文
- [GOTabPFN: From Feature Ordering to Compact Tokenization for Tabular Foundation Models on High-Dimensional Data](../../papers/ml-foundations.md#habib26a-modules) · 中文

### Graph Learning and Recommendation

- [GI-GCN: Global Interacted Graph Convolutional Networks via Dominant Sets for Graph Classification](../../papers/graph-and-recommendation.md#bai26i-modules) · 中文
- [Message Passing on the Edge: Towards Scalable and Expressive GNNs](../../papers/graph-and-recommendation.md#barcelo26a-modules) · 中文
- [Weaving Graph over Tokens: Contextualizing Structured Sequences for LLMs](../../papers/graph-and-recommendation.md#chen26gm-modules) · 中文
- [Gauge-Equivariant Graph Networks via Self-Interference Cancellation](../../papers/graph-and-recommendation.md#choi26d-modules) · 中文
- [Unitary Convolutions for Message-passing and Positional Encodings on Directed Graphs](../../papers/graph-and-recommendation.md#fesser26b-modules) · 中文

### Scientific Machine Learning

- [Smoothness Errors in Dynamics Models and How to Avoid Them](../../papers/scientific-ml.md#berman26d-modules) · 中文
- [MedSIGHT: Towards Grounded Visual Comprehension in Medical Large Vision-Language Models](../../papers/scientific-ml.md#chang26b-modules) · 中文
- [TSMGen: Target-Specific Molecule Generation via Higher-Order Structural Dependencies and Context-Aware Bidirectional Fusion](../../papers/scientific-ml.md#chen26bw-modules) · 中文
- [PCRNet: Phase-aware Complex Refinement Network for EEG-based Auditory Attention Decoding](../../papers/scientific-ml.md#chen26fr-modules) · 中文
- [BLIPs: Bayesian Learned Interatomic Potentials](../../papers/scientific-ml.md#coscia26a-modules) · 中文
- [Learning the Interaction Prior for Protein-Protein Interaction Prediction: A Model-Agnostic Approach](../../papers/scientific-ml.md#gao26ap-modules) · 中文
<!-- classification:end -->
