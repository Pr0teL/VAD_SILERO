import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np
from silero_vad import load_silero_vad
import torch

SAMPLING_RATE = 16000
window_size_samples = 512

model = load_silero_vad()

def audio_callback(indata, frames, time, status):
    global speech_probs
    if status:
        print(status)
    chunk = indata[:, 0]
    if len(chunk) < window_size_samples:
        return
    chunk_tensor = torch.from_numpy(chunk).float()
    speech_prob = model(chunk_tensor, SAMPLING_RATE).item()
    speech_probs.append(speech_prob * 100)
    if len(speech_probs) > 100:
        speech_probs.pop(0)

speech_probs = []

fig, ax = plt.subplots()
x = np.arange(100)
line, = ax.plot(x, np.zeros(100))
ax.set_ylim(0, 100)
ax.set_title("Speech probability (%)")
ax.set_xlabel("Chunk")
ax.set_ylabel("Probability (%)")

def update_plot(frame):
    line.set_ydata(speech_probs + [0]*(100-len(speech_probs)))
    return line,

stream = sd.InputStream(
    channels=1,
    samplerate=SAMPLING_RATE,
    blocksize=window_size_samples,
    callback=audio_callback
)

with stream:
    import matplotlib.animation as animation
    ani = animation.FuncAnimation(fig, update_plot, interval=50)
    plt.show()