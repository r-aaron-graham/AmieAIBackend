# AMIE Python backend experiments

This repository contains exploratory Flask, speech, and integration code for AMIE.

| File | What it contains |
| --- | --- |
| `main.py` | Local Flask landing route and an explicit unavailable response for the unfinished LiveKit integration |
| `main_new.py` | An experimental Flask text-to-speech route |
| `speak.py`, `tts_test.py` | Speech client experiments |
| `load_user_preferences.py` | A user-preferences helper sketch |

The local Flask launcher serves a landing page. The LiveKit token route returns HTTP 503 because the integration is absent from this checkout. The experimental TTS provider contract is unverified. For a runnable, self-contained portfolio demo, see the [AMIE classroom activity lookup demo](https://github.com/r-aaron-graham/Amie-Chatbot-Frontend/tree/undefined). It uses fictional educational activity cards and does not call this backend.

To run the local launcher or check syntax without calling external services:

```bash
python -m pip install Flask
python -m compileall -q .
python main.py
```
