# Portfolio source dossier

Collected and reviewed on **18 October 2026** before the portfolio update.

## Personal and professional sources

- [Original résumé](Rishikesh_Resume.docx): name, New Delhi location, email/phone, employment history and responsibilities, performance figures, skills, education and languages.
- [ABOUTME.md](../ABOUTME.md): research interests, founder role, former MyClone consulting work, project inventory and public contact links.
- User-supplied GitHub portfolio review in the task: dated project engagement snapshot and technical summaries, cross-checked against GitHub metadata and READMEs below.
- [Public GitHub profile](https://github.com/rishikksh20): public repository links, Dubpro affiliation, New Delhi location and X account.

The résumé reports 10+ years in software, including 8+ years in AI; ABOUTME uses approximately 8.5 years for AI. The profile uses the résumé's conservative wording. MyClone is a completed six-month engagement; exact calendar dates were not provided. Dubpro is January 2019–present. Earlier roles are Boutiqaat (October 2018–January 2019), Humonics Global (December 2017–October 2018), and Nucleus Software (June 2015–December 2017). Education is B.Tech in Electronics and Instrumentation Engineering, NIT Silchar, 2011–2015.

## Attribution of results

MyClone's embedding migration (1,536→512 dimensions), approximately 3× lower vector storage, 2–2.5× faster retrieval and 15–20% lower voice-chat latency, plus Dubpro's approximately 2× dubbing improvement, are reported in the supplied résumé. They were not independently benchmarked in this review. No missing calendar dates, publications, awards, citations or customer deployments were inferred. An unverified LinkedIn URL from the old website was removed.

Repository stars and forks are a dated measure of community interest. They do not establish citation counts, production adoption or benchmark superiority. Paper implementations credit the original research and code references through their linked repositories.

## Quantified community interest

Live GitHub API counts matched the user-supplied October 18, 2026 snapshot exactly.

| Repository | Stars | Forks | Scope / status |
|---|---:|---:|---|
| [ViViT-pytorch](https://github.com/rishikksh20/ViViT-pytorch) | 560 | 71 | Unofficial partial research implementation; WIP |
| [ResUnet](https://github.com/rishikksh20/ResUnet) | 551 | 75 | Unofficial ResUNet / ResUNet++; no longer maintained |
| [VocGAN](https://github.com/rishikksh20/VocGAN) | 321 | 59 | Modified paper implementation; training and inference workflows |
| [iSTFTNet-pytorch](https://github.com/rishikksh20/iSTFTNet-pytorch) | 281 | 51 | Experimental C8C8I implementation |
| [FNet-pytorch](https://github.com/rishikksh20/FNet-pytorch) | 264 | 36 | Unofficial Fourier token mixing implementation |
| **Top-five total** | **1,977** | **308** | Community interest; no inference of production adoption/citations |

## Verified project descriptions

### Established research implementations

- **ViViT** — PyTorch implementation of spatiotemporal video transformers. README explicitly says Model 2 is implemented, Models 3/4 are not, and WIP. Base ViT and some factorized logic acknowledged to lucidrains. Safe copy: “Implemented the factorized-encoder variant of ViViT for video classification in PyTorch.” Do not call a complete reproduction or claim original architecture. [README](https://github.com/rishikksh20/ViViT-pytorch/blob/master/README.md)
- **ResUNet / ResUNet++** — implemented these two residual U-Net architectures. Baseline U-Net borrowed from another repository. Includes crop preprocessing and training specific to Massachusetts Roads Dataset; README says no longer maintained, experimental and not production-ready. Safe copy: “Implemented residual U-Net architectures and road-segmentation training workflows.” Do not assert evaluated medical imaging performance. [README](https://github.com/rishikksh20/ResUnet/blob/master/README.md)
- **VocGAN** — modified generator and replaced hierarchically nested JCU discriminator with Full-Band MelGAN discriminator to address slow training. Baseline branch retains original model. Includes preprocessing, training/TensorBoard, inference, pretrained models for English LJSpeech, Korean KSS and multispeaker VCTK, linked audio samples. Real-time fidelity is author's reported testing, not an independent benchmark. Safe copy: “Developed a modified VocGAN implementation with a MelGAN-based discriminator to reduce training overhead.” [README](https://github.com/rishikksh20/VocGAN/blob/master/README.md)
- **iSTFTNet** — paper implementation specifically C8C8I, using inverse STFT for lightweight mel-to-waveform synthesis. README claims ~60% faster than HiFi-GAN and good audio with ~30% less training; context/method not documented, not independently reproduced here. Prefer omit exact metrics from headline or explicitly label repository-reported experimental results. README says test purpose, code not optimized for performance. [README](https://github.com/rishikksh20/iSTFTNet-pytorch/blob/master/README.md)
- **FNet** — PyTorch implementation of “FNet: Mixing Tokens with Fourier Transforms.” Use as efficient token-mixing / attention-alternative research implementation, not original invention. [README](https://github.com/rishikksh20/FNet-pytorch/blob/master/README.md)
- **NU-Wave** — diffusion probabilistic neural audio upsampling implementation with training/inference commands, references official NU-Wave / DDPM / DiffWave / WaveGrad. 37 stars / 5 forks. [README](https://github.com/rishikksh20/NU-Wave-pytorch/blob/master/README.md)

### Current efficient model / GPU work

- **Mamba-3** — clean from-scratch plain PyTorch reference implementation (no custom Triton/CUDA kernels), designed for understanding; exponential-trapezoidal discretization, per-head accumulated rotary states, SISO/MIMO recurrence, residual blocks and stacked language model, inference cache and single-token step. Serial scans are not production optimized. 40 stars / 3 forks. Paper arXiv2603.15569 explicitly cited to original authors. Safe copy: “Implemented Mamba-3 state-space recurrence, rotary state updates, SISO/MIMO variants and cached autoregressive decoding in readable PyTorch.” [README](https://github.com/rishikksh20/mamba3-pytorch/blob/master/README.md)
- **LFM2.5** — minimal implementation of LiquidAI LFM2.5-2.6B using official weights, not a newly trained proprietary model. Hybrid22 causal double-gated depthwise convolution +8 grouped-query attention blocks; RMSNorm, RoPE, SwiGLU, tied embedding/LM head, KV/convolution caching, HF checkpoint mapping and tokenizer, streaming sampling, FastAPI local webchat. Optional Triton inference kernels for RMSNorm, short-context online-softmax GQA decode and sampling, portable fallbacks. 3 stars /1 fork. [README](https://github.com/rishikksh20/lfm25-pytorch/blob/master/README.md)
  - Detailed repository-reported RTX4060 8GB BF16 benchmark:128-token prompt,256 generated tokens,8 warmup; PyTorch2.13.0 CUDA13.0 as reported. Original26.69tok/s → optimized40.22tok/s (~50.7% higher). Measured results include fused SDPA-GQA prefill, fixed-capacity KV cache, device-resident RoPE, last-position prompt projection, vectorized repetition penalty/ring buffer, and optional Triton. Not independently reproduced.
  - Do not generalize microbenchmark kernel speedups to whole-model gains. Some short context optimizations have no gain, custom GQA only dispatched through256 cached tokens because SDPA is faster at longer contexts.
- **Qwen3.5 Playground** — from-scratch PyTorch Qwen3.5-0.8B aligned with official HF checkpoint; hybrid GatedDeltaNet linear/full GQA attention, learned decay, partial RoPE, gated RMSNorm, checkpoint key mapping, tokenizer and sampling.24 layers,6×(3linear+1full).5 stars/1 fork. [README](https://github.com/rishikksh20/qwen3-5-playground/blob/master/README.md)
- **Gemma3-270M Playground** — README is only title and Colab link. Code confirms Gemma3Model,18 layers with sliding/full attention, grouped-query attention, gated feed-forward, RMSNorm, RoPE, checkpoint/inference test file.2 stars/0 forks. Can safely describe as “small-model PyTorch architecture playground,” avoid any claimed training/benchmark achievement. [Model code](https://github.com/rishikksh20/gemma3-270m-playground/blob/master/llm.py)
- **Triton Kernel Tutorials** —31 self-contained Markdown tutorials with PyTorch references, correctness checks and benchmarks, plus standalone GEMM and30 kernel-only topic files. Covers GPU architecture, tiled GEMM, reductions, normalization, FlashAttention forward/backward, INT8/INT4/FP8, RoPE, KV caches, decode attention, SwiGLU, cross entropy, MoE routing/expert computation.2 stars/0 forks. Educational, fixed configurations; tutorial-specific limits, not a universal production kernel library. H100 roofline plots are calculated models, not measurements. README clone URL typo says kernel-triton-python; canonical repo is triton-kernel-python. [README](https://github.com/rishikksh20/triton-kernel-python/blob/master/README.md)

### Neural audio and voice systems

- **SoundStorm** — explicitly WIP. Semantic tokens → non-autoregressive acoustic codec tokens with bidirectional attention and confidence-based parallel decoding. Preprocessing/training format references WhisperSpeech.131stars/13forks. Do not claim final paper reproduction or measured quality/speed. [README](https://github.com/rishikksh20/SoundStorm-pytorch/blob/master/README.md)
- **Voxtral Codec** (canonical repository spelling **voxtral-codec-pytoch**) — partially AI-assisted PyTorch research implementation of causal convolution-transformer autoencoder for24kHz mono speech.292dim latent splits256 semantic VQ +36 acoustic FSQ;8192semantic codebook;21FSQ levels;12.5Hz tokens,37tokens/frame. Multi-resolution STFT discriminator, Whisper ASR distillation support, audio training entrypoint and smoke/unit tests.18stars/1fork. README self-reports33passing tests; distillation alignment approximates parts of paper, no final-scale reproduction. [README](https://github.com/rishikksh20/voxtral-codec-pytoch/blob/master/README.md)
- **Voice AI Agent Basic** — FastAPI/Pipecat showcase combining shared prompts with inbound/outbound Twilio calls, browser WebRTC voice and streamed text chat. AssemblyAI STT, OpenAI LLM, Cartesia TTS; Docker deployment/test setup.8stars/0forks. README differentiates basic demo from potential production extensions; RAG, long-term memory and CRM/handoff listed as extensions, not necessarily implemented in this demo. [README](https://github.com/rishikksh20/voice-ai-agent-basic/blob/master/README.md)
- **MyClone** — organisation project whose README verifies LiveKit, Deepgram STT, ElevenLabs/Cartesia TTS, LlamaIndex/OpenAI embeddings/pgvector RAG, FastAPI/PostgreSQL, Next.js15/React19, NATS, Docker; multi-source ingestion, persistent memory, persona chat, auth, widget, workflows/payments. User explicitly supplies engineering ownership/contribution in their request, so present their reported work without implying sole authorship. Public history has7commits: initial monorepo by vaibhav135; user has a verified merged README overhaul contribution in PR#2. No public commit-level evidence independently attributes all backend architecture to user. [README](https://github.com/myclone-dev/myclone/blob/main/README.md) · [Verified user commit](https://github.com/myclone-dev/myclone/commit/d6f1268b15f5816835bb1741336562aa33ce50f2)

### Agents and RL infrastructure

- **Nexus** — CLI-first coding-agent harness, marked WIP / active scaffold. Typed model/tool runtime; streamed provider clients; REPL/headless mode; session persistence, compaction/summaries, memory; skills/plugins/MCP discovery; cognitive subagents; Docker command sandbox, permission gates, resumable approvals; JSONL/audit observability, optional OpenTelemetry/Sentry.1star/0forks. Safe copy: “Built an experimental Python coding-agent runtime with tool orchestration, persistent sessions, context compaction and sandboxed execution.” Avoid “production-ready.” [README](https://github.com/rishikksh20/nexus-code-agent/blob/main/README.md)
- **Coding Agent RL Lab** — stateful code-repair environment with immutable tasks,4tools(list/read/patch/tests), frozen source, independent binary correctness grading, Docker resource/network sandbox; CPU Transformers rollouts/heldout evaluation; optional native TRL GRPO + LoRA/full training integration, evidence/checkpoint auditing and OpenCode/custom MCP bridge.1star/0forks. [README](https://github.com/rishikksh20/rl-env-harness-training/blob/master/README.md)
  - Latest Phase4status(Oct16) reports183regression tests passing, genuine LFM2.5-350M model probe and capacity measurement,4genuine heldout attempts with0verified successes. Fixture integration exercises real TRL/optimizer/checkpoint mechanics, but informative pretrained learning/update and genuine checkpoint improvement remain open. Describe **research infrastructure**, never demonstrated RL model improvement. [Status](https://github.com/rishikksh20/rl-env-harness-training/blob/master/docs/PHASE_4_STATUS.md)

## Verifiable external contribution

- **AcademiCodec/HiFi-Codec** — [PR#8 “Remove minor bugs from HiFi-Codec code”](https://github.com/yangdongchao/AcademiCodec/pull/8) authored by rishikksh20 and **merged**. Changes include missing MelSpectrogram import, handling input tensor shape in encode, and adding required module files with upstream attribution. Correct portfolio copy: “Contributed merged bug fixes to the AcademiCodec HiFi-Codec implementation.” Distinguish contribution from repository/paper authorship.

## Editorial recommendations

Lead portfolio with research engineering spanning neural speech, efficient sequence models and AI agents, supported by dated1977star/308fork top-five snapshot. Feature MyClone and Voice AI demo as applied systems; VocGAN/iSTFTNet/ViViT as established open-source research implementations; Mamba/LFM/Triton/RL as current work. Keep all model-paper authorship separate. Do not invent publication counts, citations, production customers, performance rankings, maintenance status or measured deployment impact.



# Additional GitHub research — October 18, 2026

GitHub API metadata and default-branch READMEs verified with the GitHub connector.

| Repository | Stars | Forks | Recommended scope sentence |
|---|---:|---:|---|
| [FastSpeech2](https://github.com/rishikksh20/FastSpeech2) | 237 | 53 | Unofficial, work-in-progress PyTorch FastSpeech 2 implementation built on ESPnet, with pitch/energy/duration-conditioned TTS, LJSpeech alignment/preprocessing, MelGAN vocoding, inference and TorchScript export. |
| [convolution-vision-transformers](https://github.com/rishikksh20/convolution-vision-transformers) | 225 | 34 | Unofficial PyTorch implementation of CvT (Introducing Convolutions to Vision Transformers) for image classification, combining convolutional inductive biases with vision transformer processing. |
| [LocalViT-pytorch](https://github.com/rishikksh20/LocalViT-pytorch) | 10 | 2 | Unofficial PyTorch LocalViT implementation exploring locality in vision transformers for image classification. |
| [CoaT-pytorch](https://github.com/rishikksh20/CoaT-pytorch) | 14 | 4 | Unofficial PyTorch implementation of Co-Scale Conv-Attentional Image Transformers, with CoaT-Lite and optional parallel-group CoaT variants for image classification. |
| [SiT-pytorch](https://github.com/rishikksh20/SiT-pytorch) | 21 | 3 | Unofficial PyTorch implementation of the 2021 Self-supervised vIsion Transformer, exposing rotation-prediction, contrastive-representation and reconstructed-image outputs. |

Sources:
- [FastSpeech2 README](https://github.com/rishikksh20/FastSpeech2/blob/master/README.md)
- [convolution-vision-transformers README](https://github.com/rishikksh20/convolution-vision-transformers/blob/master/README.md)
- [LocalViT-pytorch README](https://github.com/rishikksh20/LocalViT-pytorch/blob/master/README.md)
- [CoaT-pytorch README](https://github.com/rishikksh20/CoaT-pytorch/blob/master/README.md)
- [SiT-pytorch README](https://github.com/rishikksh20/SiT-pytorch/blob/master/README.md)

## Scope/status caveats

- FastSpeech2 README explicitly calls the project WIP, experimental, needing cleanup/optimization and model improvements. Current inference supports phoneme-based synthesis. It uses ESPnet FastSpeech as a base, NVIDIA Tacotron2 preprocessing, Montreal Forced Aligner alignment, and MelGAN as vocoder. No independent quality/speed benchmark established here.
- CvT acknowledges lucidrains ViT as base code. README contains model usage but no training or measured benchmark claim.
- LocalViT, CoaT and SiT are explicitly unofficial paper implementations. READMEs show forward-pass examples; do not imply original architecture authorship or production validation.
- **SiT means Self-supervised vIsion Transformer (Atito, Awais and Kittler, arXiv2104.03602, 2021). It is not Scalable Interpolant Transformers / diffusion SiT.** Its usage returns rotation logits, contrastive embedding and image reconstruction.

