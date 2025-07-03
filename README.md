# VAD Silero Example Repository

This repository provides examples of using the [Silero Voice Activity Detector (VAD)](https://github.com/snakers4/silero-vad) for both basic and real-time speech detection in Python.

## Requirements

Install the required dependencies:

```sh
pip install -r requirements.txt
```


## Repository Structure

- `main-example.py` — Offline VAD example for processing audio files.
- `real-time-example.py` — Real-time VAD example with live microphone input and visualization.
- `test.wav` — Example audio file for offline detection.
- `requirements.txt` — List of required Python packages.

## References

- [Silero VAD GitHub](https://github.com/snakers4/silero-vad)
- [Silero VAD PyPI](https://pypi.org/project/silero-vad/)

---

**Note:**  
- For real-time detection, ensure your microphone is connected and accessible.
- For basic detection, you can replace `test.wav` with your own audio file.
