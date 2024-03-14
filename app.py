import os
import librosa
import librosa.display
import numpy as np
import json
import matplotlib.pyplot as plt

directory = '/path/to/your/audio/files'
all_rhythm_data = []

for filename in os.listdir(directory):
    if filename.endswith('.mp3'):
        audio_path = os.path.join(directory, filename)
        y, sr = librosa.load(audio_path, sr=None)
        onset_frames = librosa.onset.onset_detect(y=y, sr=sr)
        onset_times = librosa.frames_to_time(onset_frames, sr=sr)
        spectral_centroids = librosa.feature.spectral_centroid(y=y, sr=sr)[0]

        rhythm_data = {
            "onset_times": [float(time) for time in onset_times.tolist()],
            "spectral_centroid": [float(value) for value in spectral_centroids.tolist()],
        }

        all_rhythm_data.append(rhythm_data)

with open('all_rhythm_data.json', 'w') as outfile:
    json.dump(all_rhythm_data, outfile)

print("All rhythm data has been written to all_rhythm_data.json")
