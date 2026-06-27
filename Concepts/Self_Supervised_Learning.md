---
type: concept
title: Self-Supervised Learning
description: Generating supervision from the data itself via pretext tasks — the pretraining paradigm behind modern LLMs and embedding models.
tags: [machine-learning, self-supervised-learning, pretraining, representation-learning]
reviewed: 2026-06
evidence_status: has_receipts
---

## Why It Matters
- Self-supervised learning (SSL) is **why foundation models exist**. It manufactures labels *for free* from unlabeled data, learning reusable representations on internet-scale corpora that you then adapt to a task with little labeled data. Formally it is a branch of [[Concepts/Unsupervised_Learning]] (no human labels) that borrows *supervised-style* losses over pseudo-labels generated from the data — the pretrain-once / adapt-many economics behind the field.

## The Core Trick: Pretext Tasks
Hide part of the input, make the model predict it — the "label" is the held-out part. Three families:
- **Masked / denoising** — predict masked tokens *bidirectionally* (**BERT**); strong for understanding & embeddings. In vision, **MAE** masks ~**75%** of patches (vs BERT's ~15%) because image patches are spatially redundant, using an asymmetric encoder that sees only visible patches.
- **Autoregressive** — strictly left-to-right next-token prediction (**GPT**); strong for generation. Same free-label idea, different directionality → different downstream fit.
- **Contrastive** — pull related items together, push others apart. **SimCLR** contrasts two *augmented views of the same image*; **CLIP** contrasts *naturally paired (image, caption)* across a batch — note these are different mechanisms, not one "contrastive" recipe.

## Representation Collapse (the central SSL failure mode)
- Contrastive methods need **negatives** to avoid trivial constant embeddings — SimCLR via large batches/NT-Xent, **MoCo** via a momentum memory queue.
- **Non-contrastive** methods (BYOL, SimSiam, DINO, Barlow Twins, VICReg) drop explicit negatives and prevent collapse via stop-gradient / predictor asymmetry or redundancy-reduction regularization.

## Pretrain → Adapt
- The payoff is **label efficiency**: SimCLR's linear probe matches a *supervised* ResNet-50; CLIP matches ResNet-50 ImageNet accuracy **zero-shot**, using none of the 1.28M labeled images.
- Downstream, you **fine-tune** or transfer on top of the representation — see _next-wave_ `Fine_Tuning_Adaptation_Strategies`.
- **SSL → embeddings, with nuance:** encoder MLM models (BERT) and contrastive objectives (CLIP, sentence encoders) produce the dense retrieval vectors of [[Concepts/Text_Embeddings]]. Decoder-only LLMs are *not* natively strong sentence embedders (naive mean-pooling underperforms), so production text-embedding models add a **contrastive fine-tuning** stage on the pretrained backbone.

## Related
- [[Concepts/Unsupervised_Learning]], [[Concepts/Supervised_Learning]], [[Concepts/Text_Embeddings]]
- _Next-wave (forward refs):_ [[Concepts/Fine_Tuning_Adaptation_Strategies]], [[Concepts/Transformer_Architecture]], [[Concepts/Representation_Learning_For_Vision]]
- Hub: [[Hubs/Machine_Learning]]

## Sources
- [BERT: Pre-training of Deep Bidirectional Transformers (Devlin et al., arXiv:1810.04805)](https://arxiv.org/abs/1810.04805) — masked language modeling; the bidirectional encoder behind understanding/embeddings.
- [Language Models are Few-Shot Learners (Brown et al., GPT-3, arXiv:2005.14165)](https://arxiv.org/abs/2005.14165) — autoregressive pretraining at scale; SSL → foundation models.
- [A Simple Framework for Contrastive Learning (SimCLR, Chen et al., arXiv:2002.05709)](https://arxiv.org/abs/2002.05709) — contrastive SSL via augmented views + NT-Xent.
- [Learning Transferable Visual Models From NL Supervision (CLIP, Radford et al., arXiv:2103.00020)](https://arxiv.org/abs/2103.00020) — multimodal contrastive pretraining; zero-shot transfer.
- [Masked Autoencoders Are Scalable Vision Learners (MAE, He et al., arXiv:2111.06377)](https://arxiv.org/abs/2111.06377) — masked SSL in vision; the 75% mask ratio.
- [Self-Supervised Representation Learning (Lilian Weng, Lil'Log)](https://lilianweng.github.io/posts/2019-11-10-self-supervised/) — survey/taxonomy of pretext tasks and contrastive families.

> Core Node: [[START_HERE]]
