# Rishikesh

**AI Research Engineer · Voice AI, LLMs & Agentic Systems · Co-founder & CTO**

New Delhi, India · [rishikksh20@gmail.com](mailto:rishikksh20@gmail.com) · +91 96501 84220

[Portfolio](https://rishikksh20.github.io/) · [GitHub](https://github.com/rishikksh20) · [X / @ai_rishikesh](https://twitter.com/ai_rishikesh) · [Printable CV](https://rishikksh20.github.io/resume.html) · [Original résumé](docs/Rishikesh_Resume.docx)

## Professional summary

AI research engineer and technical founder with **10+ years in software development, including 8+ years in AI and generative systems**. My work connects research implementations with practical systems across multilingual speech synthesis, voice cloning, real-time voice agents, language-model architectures, retrieval, and efficient inference.

As **Co-founder and CTO of Dubpro.ai / DeepSync Technologies**, I lead AI and engineering work on multilingual dubbing and generative audio. I also completed a six-month AI consulting engagement with **MyClone.is**, building real-time digital-persona capabilities, retrieval, persistent memory, and conversational infrastructure.

I implement research papers to understand their architecture and computational trade-offs, then explore training, decoding, GPU kernels, and application integration. My open-source portfolio spans established speech and vision implementations and newer work on selective state-space models, hybrid LLMs, Triton kernels, and coding agents.

## Selected impact

- **Open-source engagement:** ViViT, ResUNet, VocGAN, iSTFTNet, and FNet together received **1,977 stars and 308 forks** in the October 18, 2026 snapshot.
- **Voice retrieval optimization:** At MyClone, migrated embeddings from **1,536 to 512 dimensions**, with improvements of approximately **3× lower vector storage**, **2–2.5× faster retrieval**, and **15–20% lower voice-chat latency**.
- **AI dubbing workflows:** At Dubpro.ai, architected agentic RAG workflows with human review, achieving approximately **2× faster dubbing**.
- **Research-to-system range:** Work spans neural vocoders, video transformers, segmentation, state-space models, real-time audio pipelines, persistent memory, and agent orchestration.

*Engagement counts are a dated snapshot, not evidence of citations, production adoption, or benchmark superiority. Repository performance observations are identified separately below.*

## Professional experience

### AI Consultant / Developer — MyClone.is, formerly Rappo

**Completed six-month engagement · Remote · San Francisco-based company**

- Developed backend features for a real-time Voice AI digital-persona platform that reproduces a user's voice, conversational style, knowledge, and communication patterns from text and voice data.
- Built low-latency conversational workflows with **LiveKit**, streaming STT/TTS, LLM orchestration, agent tools, and real-time session management.
- Implemented persona-aware retrieval and persistent memory using **LlamaIndex, PostgreSQL/pgvector, hybrid RAG, document ingestion, and source-level access filters**.
- Migrated embeddings from **1,536 to 512 dimensions**; reported approximately **3× lower vector storage**, **2–2.5× faster retrieval**, and **15–20% lower voice-chat latency**.

**Stack:** Python · FastAPI · LiveKit · LlamaIndex · PostgreSQL · pgvector · RAG · Streaming STT/TTS

[Open-source project](https://github.com/myclone-dev/myclone) · [MyClone.is](https://www.myclone.is)

### Co-founder & CTO — Dubpro.ai / DeepSync Technologies

**January 2019–Present · Noida, India**

- Co-founded and led development of AI dubbing, multilingual text-to-speech, voice cloning, speech transformation, and generative audio systems.
- Architected agentic RAG dubbing workflows with **human-in-the-loop review**, increasing dubbing speed by approximately **2×**.
- Developed an in-house dubbing harness and tools, including an **LLM-as-judge quality verifier**, to automate dubbing and quality analysis, reduce reliance on human review, and save approximately **40% in time** and **25% in costs**.
- Developed multilingual foundation-model capabilities and applied **RLHF-based post-training** for translation-specific quality and alignment.

**Focus:** Multilingual speech · Neural TTS · Voice conversion · Translation · Agentic RAG · Human review · RLHF

[Dubpro.ai](https://www.dubpro.ai/)

### Data Science / Software Development Engineer — Boutiqaat

**October 2018–January 2019 · Gurugram, India**

- Built text-and-image product matching, hybrid recommendation systems, and automated product categorization tools for commercial catalogs.
- Developed clustering, tagging, and product-labeling algorithms to support e-commerce data operations.

**Focus:** Multimodal matching · Recommendations · Classification · Catalog intelligence

### Data Scientist — Humonics Global

**December 2017–October 2018 · Gurugram, India**

- Built automated question-answer generation systems for reading comprehension.
- Developed an **LSTM/WaveNet-based TTS engine** for conversational applications.
- Worked on face recognition and liveness detection solutions.

**Focus:** Speech synthesis · NLP · Conversational AI · Computer vision

### Software Engineer — Nucleus Software

**June 2015–December 2017 · India**

- Developed banking transaction analytics and loan-default prediction systems.
- Designed and implemented financial supply-chain management software using **MVC architecture**.

**Focus:** Financial software · Predictive analytics · Enterprise application development

## Selected open-source AI research

These implementations reflect work across video understanding, segmentation, speech synthesis, and efficient sequence modeling. The work implements and explores research by the original paper authors.

### Community engagement snapshot

| Repository | Stars | Forks | Research area |
|---|---:|---:|---|
| [ViViT-pytorch](https://github.com/rishikksh20/ViViT-pytorch) | 560 | 71 | Video transformers |
| [ResUnet](https://github.com/rishikksh20/ResUnet) | 551 | 75 | Semantic segmentation |
| [VocGAN](https://github.com/rishikksh20/VocGAN) | 321 | 59 | Neural vocoders |
| [iSTFTNet-pytorch](https://github.com/rishikksh20/iSTFTNet-pytorch) | 281 | 51 | Efficient audio generation |
| [FNet-pytorch](https://github.com/rishikksh20/FNet-pytorch) | 264 | 36 | Fourier token mixing |
| **Total across these five repositories** | **1,977** | **308** | **Five research implementations** |

*Snapshot: October 18, 2026. The supplied review's counts matched the GitHub metadata checked for this portfolio update.*

### ViViT — Video Vision Transformer

[Repository](https://github.com/rishikksh20/ViViT-pytorch) · **560 stars · 71 forks**

- Implemented the **factorized-encoder variant** of ViViT for video classification in **PyTorch**.
- Explored how transformer architectures represent spatial and temporal information in video.
- Provides a research implementation reference for spatiotemporal representation learning and video understanding.
- **Status:** Partial, work-in-progress implementation. The README identifies Model 2 as implemented and Models 3/4 as unimplemented; this is not a complete reproduction.

**Themes:** Video understanding · Spatiotemporal modeling · Transformers · PyTorch

### ResUNet / ResUNet++ — Residual image segmentation

[Repository](https://github.com/rishikksh20/ResUnet) · **551 stars · 75 forks**

- Implemented residual U-Net architectures for **semantic image segmentation**.
- Included crop preprocessing and training workflows for the **Massachusetts Roads Dataset**.
- Explored residual learning and encoder–decoder design for dense image prediction.
- **Status:** The README states that the repository is **no longer maintained**, experimental, and **not production-ready**.

**Themes:** Semantic segmentation · Residual networks · U-Net · Road extraction

### VocGAN — Modified GAN neural vocoder

[Repository](https://github.com/rishikksh20/VocGAN) · **321 stars · 59 forks**

- Developed a modified VocGAN implementation with a **MelGAN-based discriminator** to reduce training overhead.
- Replaced the hierarchically nested JCU discriminator and modified the generator; the baseline branch preserves the original model.
- Included preprocessing, training, inference, pretrained models, and linked audio samples.
- Provided checkpoints for **English LJSpeech, Korean KSS, and multispeaker VCTK** datasets.

**Themes:** GANs · Neural vocoders · Speech synthesis · Training efficiency

### iSTFTNet — Efficient neural waveform synthesis

[Repository](https://github.com/rishikksh20/iSTFTNet-pytorch) · **281 stars · 51 forks**

- Implemented the **C8C8I** variant of iSTFTNet for lightweight mel-to-waveform synthesis using inverse short-time Fourier transforms.
- Explored how signal-processing structure can reduce neural audio synthesis cost.
- The README reports approximately **60% faster inference than HiFi-GAN** and good audio quality with approximately **30% less training**.
- **Status and measurement scope:** Experimental implementation for testing, without performance optimization. These observations are repository-reported and were not independently reproduced.

**Themes:** Inverse STFT · Neural audio · Efficient synthesis · Vocoders

### FNet — Fourier token mixing

[Repository](https://github.com/rishikksh20/FNet-pytorch) · **264 stars · 36 forks**

- Implemented FNet in **PyTorch**, exploring Fourier transforms as a replacement for attention-based token mixing.
- Studied an alternative sequence-modeling design through a compact research implementation.
- Connects earlier efficient token-mixing work with my continuing interest in hybrid attention and selective state-space models.

**Themes:** Fourier transforms · Sequence modeling · Attention alternatives · Efficient architectures

### Mamba-3 — Selective state-space language models

[Repository](https://github.com/rishikksh20/mamba3-pytorch) · **40 stars · 3 forks** in the snapshot

- Implemented Mamba-3 in **plain PyTorch**, including **SISO/MIMO recurrence**, exponential-trapezoidal discretization, and per-head accumulated rotary state updates.
- Included residual blocks, a stacked language model, an inference cache, and single-token autoregressive decoding.
- Built a readable reference for investigating state updates and efficient sequence modeling.
- **Status:** Educational/research reference with serial scans; no custom CUDA/Triton kernels or production inference optimization.

**Themes:** Selective SSMs · MIMO recurrence · Rotary state updates · Cached decoding

## Current architecture, inference & agent research

### LFM2.5 2.6B — Hybrid convolution / attention LLM

[Repository](https://github.com/rishikksh20/lfm25-pytorch) · **3 stars · 1 fork** in the snapshot

- Implemented LiquidAI's **LFM2.5-2.6B** architecture in PyTorch with official checkpoint loading.
- Combines causal depthwise-convolution blocks and grouped-query attention, with **KV/convolution caching, RoPE, RMSNorm, SwiGLU, and streaming sampling**.
- Includes optional **Triton RMSNorm, short-context GQA decoding, and sampling kernels**, alongside portable fallbacks.
- The README reports **26.69→40.22 tokens/second** on an **RTX 4060 8 GB** under its stated BF16 setup, approximately **50.7% higher throughput**; this repository-reported result was not independently reproduced.

### Qwen3.5 0.8B — Hybrid linear-attention exploration

[Repository](https://github.com/rishikksh20/qwen3-5-playground)

- From-scratch PyTorch architecture implementation aligned with the official checkpoint.
- Explores hybrid **GatedDeltaNet linear attention and full grouped-query attention**, learned decay, partial RoPE, gated RMSNorm, checkpoint mapping, and sampling.

### Gemma 3 270M — Small-model architecture playground

[Repository](https://github.com/rishikksh20/gemma3-270m-playground)

- PyTorch architecture exploration with sliding/full attention, grouped-query attention, gated feed-forward layers, RMSNorm, and RoPE.
- Focused on model internals and inference experimentation, without a claimed training or benchmark achievement.

### Triton Kernel Tutorials — GPU programming experiments

[Repository](https://github.com/rishikksh20/triton-kernel-python) · **2 stars · 0 forks** in the snapshot

- Created **31 self-contained tutorials** with PyTorch references, correctness checks, and benchmarks.
- Covers tiled GEMM, reductions, normalization, FlashAttention forward/backward, quantization, RoPE, KV caches, decoding, SwiGLU, and mixture-of-experts operations.
- **Scope:** Educational kernels and fixed-configuration experiments; tutorial-specific results do not imply a general production kernel library.

### Coding Agent RL Lab — Environment & training infrastructure

[Repository](https://github.com/rishikksh20/rl-env-harness-training) · **1 star · 0 forks** in the snapshot

- Stateful code-repair environment with immutable tasks, independent correctness grading, and **Docker resource/network sandboxing**.
- Includes CPU model rollouts, held-out evaluation, checkpoint auditing, and optional native **TRL GRPO** training integration.
- Provides tools for listing files, reading, patching, and running tests, with an MCP bridge for agent experimentation.
- **Status:** Experimental research infrastructure; successful environment/training integration does not establish improved policy learning or held-out model performance.

## Voice AI & agent systems

### MyClone — Real-time voice AI & digital personas

[Repository](https://github.com/myclone-dev/myclone)

- Contributed backend engineering during a six-month consulting engagement, as detailed in the professional experience above.
- Combined real-time voice conversations with persona-aware retrieval, knowledge, persistent memory, and agent orchestration.
- Used **LiveKit, LlamaIndex, FastAPI, PostgreSQL, and pgvector** in voice and retrieval workflows.
- An organization project with multiple contributors; the role description reflects my supplied professional experience.

### Nexus Code Agent — CLI-first coding assistant

[Repository](https://github.com/rishikksh20/nexus-code-agent)

- Experimental Python coding-agent runtime with **MCP integration, sub-agents, skills/plugins, and tool orchestration**.
- Explores persistent sessions, context compaction, repository memory, sandboxed commands, and resumable approvals.
- **Status:** Work in progress / active scaffold.

### Voice AI Agent — Telephony, browser voice & chat

[Repository](https://github.com/rishikksh20/voice-ai-agent-basic)

- Real-time assistant demo supporting **inbound/outbound Twilio calls**, browser **WebRTC**, and streamed text chat.
- Uses **FastAPI and Pipecat-based STT–LLM–TTS pipelines** with shared prompts and conversational logic.
- Basic showcase; extended RAG, long-term memory, and CRM workflows are potential extensions rather than claimed implemented features.

## Additional speech & generative audio work

| Project | Research / engineering focus |
|---|---|
| [FastSpeech2](https://github.com/rishikksh20/FastSpeech2) | Experimental, work-in-progress FastSpeech 2 implementation based on ESPnet, with pitch/energy/duration modeling, a MelGAN vocoder, LJSpeech alignment and TorchScript export. **237 stars / 53 forks** in the snapshot. |
| [SoundStorm-pytorch](https://github.com/rishikksh20/SoundStorm-pytorch) | Work-in-progress semantic-to-acoustic codec-token generation with bidirectional attention and confidence-based parallel decoding. **131 stars / 13 forks** in the snapshot. |
| [Voxtral Codec](https://github.com/rishikksh20/voxtral-codec-pytoch) | Experimental causal convolution-transformer audio codec with semantic/acoustic quantization; approximate distillation alignment, without a final-scale reproduction claim. |
| [NU-Wave-pytorch](https://github.com/rishikksh20/NU-Wave-pytorch) | Diffusion-probabilistic neural audio upsampling with training and inference workflows. |

### External open-source contribution — AcademiCodec / HiFi-Codec

[Merged contribution: PR #8](https://github.com/yangdongchao/AcademiCodec/pull/8) · [Upstream repository](https://github.com/yangdongchao/AcademiCodec)

- Contributed merged bug fixes to the AcademiCodec HiFi-Codec implementation.
- Addressed a missing MelSpectrogram import, input tensor shape handling during encoding, and required module files with upstream attribution.
- Listed as a contribution to an external research project, separate from repository or paper authorship.

## Additional vision & architecture implementations

| Project | Research focus |
|---|---|
| [CvT](https://github.com/rishikksh20/convolution-vision-transformers) | Convolutional vision-transformer architecture implementation. |
| [LocalViT](https://github.com/rishikksh20/LocalViT-pytorch) | Locality-aware vision-transformer implementation. |
| [CoaT](https://github.com/rishikksh20/CoaT-pytorch) | CoaT-Lite and parallel CoaT convolutional-attention image-transformer implementation. |
| [SiT](https://github.com/rishikksh20/SiT-pytorch) | The 2021 Self-supervised vIsion Transformer: rotation prediction, contrastive learning and image reconstruction. |

## Technical skills & research interests

| Area | Technologies and methods |
|---|---|
| Model development | Python, PyTorch, Hugging Face, Transformers, hybrid/linear attention, state-space models, Mamba |
| Training & post-training | SFT, RLHF, RLVR, GRPO, distillation, alignment |
| Speech & generative audio | TTS, STT, voice cloning, voice conversion, vocoders, neural codecs, diffusion, flow matching |
| Efficient inference | Triton, CUDA, Flash Attention, vLLM, KV caching, quantization, GPU memory and latency optimization |
| Agents & retrieval | MCP, multi-agent orchestration, tool calling, skills, RAG, LlamaIndex, LangChain, vector search, persistent memory, sandboxing |
| Real-time voice | LiveKit, Pipecat, Twilio, streaming STT/TTS, WebRTC |
| Backend & data | FastAPI, PostgreSQL, pgvector, Redis, SQL |
| Infrastructure | Docker, AWS, GCP |
| Additional programming experience | C++, Rust, Java |

These areas combine professional experience, open-source implementations, and active research interests; individual projects above show where specific methods were applied.

## Education & languages

**Bachelor of Technology — Electronics and Instrumentation Engineering**  
National Institute of Technology Silchar · **2011–2015**

**Languages:** Hindi — native · English — proficient

## Collaboration interests

Open to research collaborations and engineering problems involving voice AI, efficient language models, GPU inference, generative audio, and intelligent agents.

[Email](mailto:rishikksh20@gmail.com) · [GitHub](https://github.com/rishikksh20) · [X](https://twitter.com/ai_rishikesh)

## Sources & scope

This profile combines the [supplied résumé](docs/Rishikesh_Resume.docx), [brief biography](ABOUTME.md), project repositories, and the user's GitHub review dated **October 18, 2026**. Exact calendar dates for the MyClone engagement were not provided. Model performance observations are repository-reported. Paper authorship, publication records, independent benchmark validation, and production adoption are not inferred from implementations or engagement counts.

See [portfolio source notes](docs/portfolio-sources.md) for the collection record and claim boundaries.
