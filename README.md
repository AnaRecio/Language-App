# AI Language App

A voice-first, open source language tutor that helps you practice speaking a language every day.

## Why

Many people want to improve a language they already know a bit, but they don't have someone to talk to every day. The idea is to have a language companion that is always at hand, keeps you using the language, and gets to know you over time: your level, the mistakes you repeat, and the words you are learning.

## How it works

The app is a pipeline of three pieces:

1. **STT (speech to text):** turns what you say into text.
2. **LLM:** acts as the tutor. It reads your words and writes a reply.
3. **TTS (text to speech):** turns the tutor's reply into audio.

Keeping three separate pieces, instead of a single speech-to-speech model, means there is always a transcript of what you said. The tutor uses it to find your mistakes. Each piece can also be swapped for a different model, depending on which one works best for each language.

## Languages

The first languages are **Italian** and **French**.

## Status

**Phase 0: exploring the pieces.** Right now I am running the models locally to test them, see what works, and learn how to use each piece on its own.

## What it does NOT do (yet)

- No voice conversation yet: the pieces work separately.
- No app or web interface.
- No learner profile: it doesn't remember you between sessions.

## License

[Apache 2.0](LICENSE)
