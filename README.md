# Rishikesh

### AI Research Engineer · Voice AI, LLMs & Agentic Systems · Co-founder & CTO

I build at the intersection of **model research and practical AI systems**: speech synthesis, real-time voice agents, language-model architectures, efficient inference, retrieval, and agent orchestration.

I have **10+ years in software development, including 8+ years in AI and generative systems**. I am **Co-founder & CTO at Dubpro.ai / DeepSync Technologies**, and recently completed a six-month AI consulting engagement with **MyClone.is**.

**[Explore my portfolio](https://rishikksh20.github.io/)** · **[Detailed CV](PROFILE.md)** · **[Printable résumé](https://rishikksh20.github.io/resume.html)** · **[Original résumé](docs/Rishikesh_Resume.docx)**

[GitHub](https://github.com/rishikksh20) · [X / @ai_rishikesh](https://twitter.com/ai_rishikesh) · [rishikksh20@gmail.com](mailto:rishikksh20@gmail.com)

## Research with an open-source footprint

Five selected deep learning research implementations together received **1,977 GitHub stars and 308 forks** in the **October 18, 2026** snapshot.

| Implementation | Focus | Stars | Forks |
|---|---|---:|---:|
| [ViViT](https://github.com/rishikksh20/ViViT-pytorch) | Video transformers and spatiotemporal representations | 560 | 71 |
| [ResUNet / ResUNet++](https://github.com/rishikksh20/ResUnet) | Residual U-Net semantic segmentation | 551 | 75 |
| [VocGAN](https://github.com/rishikksh20/VocGAN) | Modified GAN vocoder with a MelGAN-based discriminator | 321 | 59 |
| [iSTFTNet](https://github.com/rishikksh20/iSTFTNet-pytorch) | Lightweight inverse-STFT neural waveform synthesis | 281 | 51 |
| [FNet](https://github.com/rishikksh20/FNet-pytorch) | Fourier transforms for sequence token mixing | 264 | 36 |

These are dated engagement counts, not claims of citations, production adoption, or independently validated benchmarks. ViViT is partial/work in progress; ResUNet is no longer maintained and is not production-ready. More implementation details and source notes are in the [full profile](PROFILE.md).

## Current research & engineering

I enjoy implementing model architectures, inspecting their computational trade-offs, and connecting them to inference and agent workflows.

- **[Mamba-3](https://github.com/rishikksh20/mamba3-pytorch)** — Plain-PyTorch reference covering SISO/MIMO recurrence, trapezoidal discretization, rotary state updates, and cached autoregressive inference.
- **[LFM2.5 2.6B](https://github.com/rishikksh20/lfm25-pytorch)** — Hybrid convolution/attention implementation with official checkpoint loading, KV/convolution caching, sampling, and optional Triton kernels.
- **[Qwen3.5 0.8B](https://github.com/rishikksh20/qwen3-5-playground)** — Exploration of hybrid GatedDeltaNet and grouped-query attention.
- **[Gemma 3 270M](https://github.com/rishikksh20/gemma3-270m-playground)** — Small-model PyTorch architecture playground.
- **[Triton Kernel Tutorials](https://github.com/rishikksh20/triton-kernel-python)** — 31 tutorials covering tiled GEMM, normalization, attention, quantization, KV caching, and inference techniques.
- **[Coding Agent RL Lab](https://github.com/rishikksh20/rl-env-harness-training)** — Sandboxed code-repair environments, correctness rewards, model rollouts, evaluation, and optional TRL GRPO integration. Experimental training infrastructure without a demonstrated policy-improvement claim.

The newer repositories represent current experiments and research engineering; their public engagement is still developing.

## Voice AI & intelligent agents

### [MyClone — Real-time digital personas](https://github.com/myclone-dev/myclone)

Contributed backend engineering for voice AI that combines a user's voice, knowledge, conversational style, retrieval, and persistent memory. My work covered streaming voice workflows, persona-aware RAG, source-level access filters, and real-time sessions.

**LiveKit · LlamaIndex · FastAPI · PostgreSQL · pgvector**

### [Nexus Code Agent](https://github.com/rishikksh20/nexus-code-agent)

A work-in-progress CLI coding-agent runtime exploring MCP, sub-agents, tools and skills, session/context management, persistent memory, and sandboxed execution.

**MCP · Multi-agent orchestration · Context compaction · Tool calling**

### [Voice AI Agent](https://github.com/rishikksh20/voice-ai-agent-basic)

A real-time assistant demo for inbound/outbound Twilio calls, browser WebRTC, and text chat, connected through Pipecat STT–LLM–TTS pipelines.

**Pipecat · Twilio · WebRTC · Streaming speech**

## Speech, audio & vision explorations

- **[SoundStorm](https://github.com/rishikksh20/SoundStorm-pytorch)** — Work-in-progress parallel acoustic-token generation using bidirectional attention and confidence-based decoding.
- **[Voxtral Codec](https://github.com/rishikksh20/voxtral-codec-pytoch)** — Experimental neural audio codec with semantic/acoustic quantization and approximate distillation alignment.
- **[NU-Wave](https://github.com/rishikksh20/NU-Wave-pytorch)** — Diffusion-based neural audio upsampling.
- **[FastSpeech2](https://github.com/rishikksh20/FastSpeech2)** — Experimental speech synthesis implementation with pitch, energy and duration modeling, based on ESPnet. Work in progress; **237 stars / 53 forks** in the October 18, 2026 snapshot.
- **Vision and architecture implementations:** [CvT](https://github.com/rishikksh20/convolution-vision-transformers), [LocalViT](https://github.com/rishikksh20/LocalViT-pytorch), [CoaT](https://github.com/rishikksh20/CoaT-pytorch), and [SiT](https://github.com/rishikksh20/SiT-pytorch).
- **External contribution:** [Merged bug fixes to AcademiCodec / HiFi-Codec](https://github.com/yangdongchao/AcademiCodec/pull/8).

## Professional experience

| Role | Organization | Period |
|---|---|---|
| AI Consultant / Developer | MyClone.is, formerly Rappo · Remote | Completed six-month engagement |
| Co-founder & CTO | Dubpro.ai / DeepSync Technologies · Noida | Jan 2019–Present |
| Data Science / Software Development Engineer | Boutiqaat · Gurugram | Oct 2018–Jan 2019 |
| Data Scientist | Humonics Global · Gurugram | Dec 2017–Oct 2018 |
| Software Engineer | Nucleus Software · India | Jun 2015–Dec 2017 |

At **MyClone**, my résumé reports approximately **3× lower vector storage**, **2–2.5× faster retrieval**, and **15–20% lower voice-chat latency** after migrating embeddings from 1,536 to 512 dimensions. At **Dubpro.ai**, it reports approximately **2× faster dubbing** through agentic RAG workflows with human review. These figures come from the [supplied résumé](docs/Rishikesh_Resume.docx).

**Education:** B.Tech, Electronics and Instrumentation Engineering — National Institute of Technology Silchar, **2011–2015**.

## Technical toolkit

| Area | Tools & methods |
|---|---|
| Models & training | PyTorch, Hugging Face, Transformers, SSMs, SFT, RLHF, RLVR, GRPO, distillation |
| Speech & audio | TTS, voice cloning, vocoders, neural codecs, diffusion, flow matching |
| Inference | Triton, CUDA, Flash Attention, vLLM, KV caching, quantization |
| Agents & voice | MCP, RAG, LlamaIndex, LangChain, LiveKit, Pipecat, Twilio |
| Backend & infrastructure | Python, FastAPI, PostgreSQL, pgvector, Redis, Docker, AWS, GCP |

See the [detailed profile](PROFILE.md) for experience, project status, and research interests behind this toolkit.

## Connect

I am interested in research collaborations and engineering problems involving **voice AI, efficient LLMs, GPU inference, generative audio, and intelligent agents**.

[Email me](mailto:rishikksh20@gmail.com) · [GitHub](https://github.com/rishikksh20) · [X](https://twitter.com/ai_rishikesh)

## About this portfolio

The website and CV draw on [ABOUTME.md](ABOUTME.md), the [original résumé](docs/Rishikesh_Resume.docx), public repositories, and the supplied October 18, 2026 review. [Source notes](docs/portfolio-sources.md) document the collection scope.

| File | Purpose |
|---|---|
| [index.html](index.html) | Public portfolio website |
| [PROFILE.md](PROFILE.md) | Detailed professional profile and CV |
| [resume.html](resume.html) | Readable, printable CV |
| [docs/Rishikesh_Resume.docx](docs/Rishikesh_Resume.docx) | Original résumé |
| [docs/portfolio-sources.md](docs/portfolio-sources.md) | Source notes and claim boundaries |

Preview the static site locally from this directory:

```bash
python3 -m http.server 8000
```

Open [localhost:8000](http://localhost:8000). No build step is required.

The CV page is generated from `PROFILE.md`. After editing the profile, regenerate it with:

```bash
python3 -m pip install -r scripts/requirements.txt
python3 scripts/build_cv.py
```

Its layout lives in [scripts/cv-template.html](scripts/cv-template.html). The renderer is a development tool; visitors need no dependencies or JavaScript to read the portfolio and CV.
