Speech-to-Text (STT) & Text-to-Speech (TTS) Implementation

1. Overview

The Speech-to-Text (STT) and Text-to-Speech (TTS) modules form the voice interaction backbone of the VoiceAid AI system. These components enable rural and low-literacy users to interact with the system using natural spoken language, eliminating the need for typing or reading complex text.

This implementation focuses on:

Offline operation

Multilingual support (Hindi + English)

Robust handling of accents, pauses, and pronunciation variations

Explainable and realistic AI behavior

2. Speech-to-Text (STT) Module
2.1 Purpose

The STT module converts user voice input into textual form, which is then passed to the Natural Language Understanding (NLU) engine for intent and entity extraction.

2.2 Technology Used

Model: OpenAI Whisper (Small)
Architecture: Transformer-based encoder–decoder
Execution Mode: Fully offline (local inference)

2.3 Model Details
Attribute	Value
Model Variant	Whisper – Small
Parameters	~244 million
Languages Supported	Multilingual (Hindi, English, etc.)
Internet Required	No
Hardware Used	CPU
Precision	FP32 (automatic fallback)

Whisper automatically adjusts its computation precision depending on hardware availability. On CPU-based systems, it falls back from FP16 to FP32 to ensure stability.

2.4 Why Whisper Was Chosen

Strong performance on Indian languages

Handles disfluent speech, pauses, and accents

Works offline, suitable for rural environments

Open-source and well-documented

Widely accepted in academic and industry projects

2.5 Implementation Logic

Capture audio input from the microphone

Convert raw audio into a temporary WAV file

Transcribe audio using Whisper’s transformer model

Return clean text output for NLU processing

2.6 Observed Behavior

Minor spelling variations may occur due to accent or pronunciation

Example:

Spoken: “आज मौसम कैसा है”

Transcribed: “अज मुसम कैसा है”

These variations are handled in the NLU layer using normalization and fuzzy matching.

2.7 Current Status

✔ Implemented
✔ Tested with Hindi and English queries
✔ Integrated into end-to-end pipeline

3. Text-to-Speech (TTS) Module
3.1 Purpose

The TTS module converts system responses into spoken audio, allowing users to receive information without reading text, improving accessibility for low-literacy users.

3.2 Technology Used

Library: pyttsx3
Mode: Offline text-to-speech engine
Platform: OS-level voice support

3.3 Why pyttsx3 Was Chosen

Works without internet connectivity

Simple integration

Lightweight and stable

Suitable for prototype and internship-level projects

3.4 Implementation Logic

Receive simplified response text

Pass text to TTS engine

Play audio output directly on the system

The response language matches the detected input language where possible.

3.5 Limitations (Acknowledged)

Hindi voice quality depends on OS-level voice availability

Pronunciation accuracy may vary across systems

No neural voice customization (by design)

These limitations are acceptable within internship constraints and are transparently documented.