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

<!-- classification:start -->
## Browse by Research Domain

### Large Language Models

- [TUR-DPO: Topology- and Uncertainty-Aware Direct Preference Optimization](../../papers/llm.md#abas26a-loss-functions) · 中文
- [The Sign Estimator: Preference Modeling for LLM Alignment under Heterogeneity](../../papers/llm.md#aouad26a-loss-functions) · 中文
- [What Makes Effective Supervision in Latent Chain-of-Thought: An Information-Theoretic Analysis](../../papers/llm.md#chen26bi-loss-functions) · 中文
- [$φ$-Balancing for Mixture-of-Experts Training](../../papers/llm.md#chen26br-loss-functions) · 中文
- [Discrete Tilt Matching](../../papers/llm.md#chen26el-loss-functions) · 中文
- [$\textitS$-SPPO: Semantic-Calibrated Self-Play Preference Optimization](../../papers/llm.md#chen26hc-loss-functions) · 中文
- [Don’t Ignore the Tail: Decoupled Distillation Produces Top Maths Students on an Academic Budget](../../papers/llm.md#dasgupta26a-loss-functions) · 中文
- [Navigating the Pareto Frontier of Alignment: Spectrum-Adaptive Fine-Tuning for LLMs](../../papers/llm.md#fan26j-loss-functions) · 中文
- [Self-correcting for Debiasing Large Language Models](../../papers/llm.md#feng26z-loss-functions) · 中文
- [Attention Sink Forges Native MoE in Attention Layers: Sink-Aware Training to Address Head Collapse](../../papers/llm.md#fu26v-loss-functions) · 中文
- [From Prompts to Responses: Dual-Sided Data Leakage and Defense in Split Large Language Models](../../papers/llm.md#gu26o-loss-functions) · 中文

### Computer Vision

- [Threshold-Guided Optimization for Visual Generative Models](../../papers/computer-vision.md#bai26c-loss-functions) · 中文
- [Benchmarking Dense and Indiscernible Object Counting with Blueberries](../../papers/computer-vision.md#bo26a-loss-functions) · 中文
- [Joint Geometric and Trajectory Consistency Learning for One-Step Real-World Super-Resolution](../../papers/computer-vision.md#deng26e-loss-functions) · 中文
- [BiRQA: Bidirectional Robust Quality Assessment for Images](../../papers/computer-vision.md#gushchin26a-loss-functions) · 中文
- [Unlearning’s Blind Spots: Over-Unlearning and Prototypical Relearning Attack](../../papers/computer-vision.md#ha26b-loss-functions) · 中文

### Natural Language Processing

- [ElicitR: Unlocking Latent Reasoning in Dense Retrievers via Generative Regularization](../../papers/nlp.md#cai26d-loss-functions) · 中文

### Reinforcement Learning

- [Continuity-Regularized Flow Matching for Offline Reinforcement Learning](../../papers/reinforcement-learning.md#chen26ep-loss-functions) · 中文

### Robotics

- [DT²: Decision-Targeted Digital Twins](../../papers/robotics.md#amad26a-loss-functions) · 中文
- [OMP: One-step Meanflow Policy with Directional Alignment](../../papers/robotics.md#fang26h-loss-functions) · 中文
- [LARA: Latent Action Representation Alignment for Vision-Language-Action Models](../insights/loss-functions.md#align-action-features-with-latent-actions)
- [ReconVLA](../insights/loss-functions.md#target-region-reconstruction-as-auxiliary-supervision)

### Multimodal Learning

- [Self-Supervised Flow Matching for Scalable Multi-Modal Synthesis](../../papers/multimodal.md#chefer26a-loss-functions) · 中文
- [Do-Prompt: Causal Interventions Meet Variational Prompt Bottlenecks](../../papers/multimodal.md#chen26au-loss-functions) · 中文
- [Language Bias in LVLMs: From In-Depth Analysis to Simple and Effective Mitigation](../../papers/multimodal.md#chen26bn-loss-functions) · 中文
- [AudioChat: Unified Audio Storytelling, Editing, and Understanding with Transfusion Forcing](../../papers/multimodal.md#chen26dq-loss-functions) · 中文
- [FairSSL: Fair Multimodal Self-Supervised Learning](../../papers/multimodal.md#cheong26a-loss-functions) · 中文
- [SALSA-V: Shortcut-Augmented Long-form Synchronized Audio from Videos](../../papers/multimodal.md#dellali26a-loss-functions) · 中文
- [Learning from Fine-Grained Visual Discrepancies: Mitigating Multimodal Hallucinations via In-Context Visual Contrastive Optimization](../../papers/multimodal.md#deng26z-loss-functions) · 中文
- [Weakly Supervised Cross-Modal Learning for 4D Radar Scene Flow Estimation](../../papers/multimodal.md#fu26r-loss-functions) · 中文
- [Twins: Learn to Predict Unified Representations with Focal Loss](../../papers/multimodal.md#gong26b-loss-functions) · 中文
- [GEM: Geometric Erasure by Contrastive Velocity Matching in Rectified Flows](../../papers/multimodal.md#grebe26a-loss-functions) · 中文
- [Bridging Tokens and Geometry: Token-wise 3D Supervision for CAD Generation](../../papers/multimodal.md#guan26g-loss-functions) · 中文

### Machine Learning Foundations and Statistics

- [Iterative Robust Satisficing: Minimizing Performance Degradation Under Distribution Shift](../../papers/ml-foundations.md#agirman26a-loss-functions) · 中文
- [Optimal Learning from Label Proportions with General Loss Functions](../../papers/ml-foundations.md#applebaum26a-loss-functions) · 中文
- [Approximate Equivariance via Projection-Based Regularisation](../../papers/ml-foundations.md#berndt26a-loss-functions) · 中文
- [Negatives-Dominant Contrastive Learning for Generalization in Imbalanced Domains](../../papers/ml-foundations.md#cao26k-loss-functions) · 中文
- [One-shot Conditional Sampling: MMD meets Nearest Neighbors](../../papers/ml-foundations.md#chatterjee26a-loss-functions) · 中文
- [Colorful Pinball: Density-Weighted Quantile Regression for Conditional Guarantee of Conformal Prediction](../../papers/ml-foundations.md#chen26bm-loss-functions) · 中文
- [Optimized Deferral for Imbalanced Settings](../../papers/ml-foundations.md#cortes26b-loss-functions) · 中文
- [Positive-Unlabeled Learning with Extreme Scarcity of Labeled Positives](../../papers/ml-foundations.md#dai26f-loss-functions) · 中文
- [Expectation Consistency Loss: Rethink Confidence Calibration under Covariate Shift](../../papers/ml-foundations.md#dong26e-loss-functions) · 中文
- [When Softmax Fails at the Top: Extreme-Value Corrections for InfoNCE](../../papers/ml-foundations.md#erol26a-loss-functions) · 中文
- [Information Geometry Loss for Time Series Forecasting](../../papers/ml-foundations.md#fang26m-loss-functions) · 中文
- [$f$-Trajectory Balance: A Loss Family for Tuning GFlowNets, Generative Models, and LLMs with Off- and On-Policy Data](../../papers/ml-foundations.md#fawkes26a-loss-functions) · 中文
- [Nonconvex Low-Rank Tensor Representation with Deep Priors for Multiview Subspace Clustering](../../papers/ml-foundations.md#fu26g-loss-functions) · 中文
- [Learning Coherent Representations: A Topological Approach to Interpretability](../../papers/ml-foundations.md#gaukstad26a-loss-functions) · 中文

### Graph Learning and Recommendation

- [Mitigating Reward Hacking in LLM-based Recommendation: A Preference Optimization Approach](../../papers/graph-and-recommendation.md#chen26ez-loss-functions) · 中文
- [GraphP-FL: Personalized Federated Graph Learning via Dynamic Structure Awareness and Fisher Information Elastic Alignment](../../papers/graph-and-recommendation.md#chen26gu-loss-functions) · 中文
- [ST-TGExplainer: Disentangling Stability and Transition Patterns for Temporal GNN Interpretability](../../papers/graph-and-recommendation.md#chen26gx-loss-functions) · 中文
- [Discriminative Mixture-of-Experts on Graphs with Reliable Expert Fusion](../../papers/graph-and-recommendation.md#deng26u-loss-functions) · 中文
- [Discriminative Attribute Graph Clustering Through Topology-Guided Contrastive Learning](../../papers/graph-and-recommendation.md#ding26v-loss-functions) · 中文
- [Watermarking Graph Neural Networks via Explanations for Ownership Protection](../../papers/graph-and-recommendation.md#downer26a-loss-functions) · 中文

### Scientific Machine Learning

- [Heavy-tailed Physics-Informed Neural Networks](../../papers/scientific-ml.md#abijuru26b-loss-functions) · 中文
- [Certificates for Complex-Compatible Learned Cochain Laplacians](../../papers/scientific-ml.md#anwer26a-loss-functions) · 中文
- [HEXST: Hexagonal Shifted-Window Transformer for Spatial Transcriptomics Gene Expression Prediction](../../papers/scientific-ml.md#byeon26a-loss-functions) · 中文
- [MetaPerch: Learning from metadata for bioacoustics foundation models](../../papers/scientific-ml.md#chasmai26a-loss-functions) · 中文
- [SGERA: Stein-Guided ECG-Report Alignment for ECG Representation Learning](../../papers/scientific-ml.md#chen26y-loss-functions) · 中文
- [FACT: Fuzzy Alignment with Comorbidity Topology for Reliable Multi-Label Medical Image Diagnosis](../../papers/scientific-ml.md#chen26at-loss-functions) · 中文
- [Self-Supervised Dynamical System Representations for Physiological Time-Series](../../papers/scientific-ml.md#chen26fk-loss-functions) · 中文
- [S2M-Net: Spectral-Spatial Mixing with Morphology-Aware Adaptive Loss for Medical Image Segmentation](../../papers/scientific-ml.md#chowdhury26b-loss-functions) · 中文
- [Physics-informed Neural Operator Learning for Nonlinear Grad-Shafranov Equation](../../papers/scientific-ml.md#ding26w-loss-functions) · 中文
- [Derivative Informed Learning of Exchange-Correlation Functionals](../../papers/scientific-ml.md#eberhard26a-loss-functions) · 中文
- [CellBRIDGE: Learning Cellular Trajectories via Interaction-Aware Alignment](../../papers/scientific-ml.md#estevez26b-loss-functions) · 中文
<!-- classification:end -->
