from silero_vad import load_silero_vad, read_audio, get_speech_timestamps
model = load_silero_vad()


wav = read_audio('./test.wav')
speech_timestamps = get_speech_timestamps(
  wav,
  model,
  return_seconds=True,  # Return speech timestamps in seconds (default is samples)
)

print(speech_timestamps)

# Chunks with voice probability 

# SAMPLING_RATE = 16000

# wav = read_audio('./test.wav', sampling_rate=SAMPLING_RATE)
# speech_probs = []
# window_size_samples = 512 if SAMPLING_RATE == 16000 else 256
# for i in range(0, len(wav), window_size_samples):
#     chunk = wav[i: i+window_size_samples]
#     if len(chunk) < window_size_samples:
#         break
#     speech_prob = model(chunk, SAMPLING_RATE).item()
#     speech_probs.append(speech_prob)
# model.reset_states() # reset model states after each audio

# print(speech_probs[:10]) # first 10 chunks predicts