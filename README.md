# AMIE Python backend experiments

This repository contains exploratory Flask, speech, and integration code for AMIE.

| File | What it contains |
| --- | --- |
| `main.py` | Flask route sketches that depend on guided SEL, memory, and LiveKit modules outside this repository |
| `main_new.py` | An experimental Flask text-to-speech route |
| `speak.py`, `tts_test.py` | Speech client experiments |
| `load_user_preferences.py` | A user-preferences helper sketch |

The historical Flask launcher and TTS sketch currently contain syntax errors. The launcher also references modules missing from this repository. For a runnable, self-contained portfolio demo, see the [AMIE Frontend draft](https://github.com/r-aaron-graham/Amie-Chatbot-Frontend/pull/1). It uses fictional educational activity cards and does not call this backend.

To reproduce the current syntax failures locally without calling external services:

```bash
python -m compileall -q .
```
