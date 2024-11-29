# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Gti9KNYRzJpS3VVTNgzgx0gmkCtPWNMq
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def generate_spectrogram(wav_file):
    # Read the WAV file
    sample_rate, data = wavfile.read(wav_file)

    # Check if data is stereo or mono
    if len(data.shape) > 1:
        data = data[:, 0]  # Use one channel if stereo

    # Create a spectrogram
    plt.figure(figsize=(12, 6))
    plt.specgram(data, Fs=sample_rate, NFFT=1024, noverlap=512, cmap='inferno')

    plt.title(f'Spectrogram of {wav_file}')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.colorbar(label='Intensity (dB)')
    plt.xlim(0, len(data) / sample_rate)  # Set x-axis limit
    plt.ylim(0, sample_rate / 2)           # Frequency range from 0 to Nyquist frequency
    plt.grid(True)
    plt.show()

# Example usage
wav_file_path = 'abc.wav'  # Replace with your WAV file path
generate_spectrogram(wav_file_path)

pip install gtts

from gtts import gTTS
import os

text = "Hello world"

language = 'en'
tts = gTTS(text=text, lang=language, slow=False)

audio_file = "output.mp3"
tts.save(audio_file)

from IPython.display import Audio
Audio(audio_file,)

# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TCvrZL3Vcxf6ZIjqjTxd1ImagfwN9-Sy
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

# Set up the figure and the axis
fig, ax = plt.subplots()
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1, 1)

# Initialize an empty line object
line, = ax.plot([], [], lw=2)

# Initialize the data
x = np.linspace(0, 2 * np.pi, 100)

# Initialization function to plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# Animation function which updates the plot
def animate(i):
    y = np.sin(x + i / 10.0)
    line.set_data(x, y)
    return line,

# Create the animation
ani = FuncAnimation(fig, animate, init_func=init, frames=100, interval=50, blit=True)

# Display the animation in the notebook
HTML(ani.to_jshtml())