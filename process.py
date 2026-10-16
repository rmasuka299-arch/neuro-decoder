import numpy as np
import matplotlib.pyplot as plt

# 1. Generate the CLEAN brainwave (what we did last time)
sample_rate = 100
duration = 1
frequency = 10
time_points = np.linspace(0, duration, sample_rate * duration, endpoint=False)
clean_brainwave = np.sin(2 * np.pi * frequency * time_points)

# 2. Generate the NOISE (the static)
# np.random.normal creates random numbers. 
# scale=0.6 means the noise is pretty strong (60% of the brainwave amplitude)
noise = np.random.normal(0, 0.6, len(clean_brainwave))

# 3. Add the noise to the clean signal
# This is what a real EEG machine reads: the signal plus the static.
noisy_brainwave = clean_brainwave + noise

# 4. The FILTER (The Moving Average)
# This is the magic algorithm. It takes a window of 5 points, averages them, and slides forward.
window_size = 5
filtered_brainwave = np.convolve(noisy_brainwave, np.ones(window_size)/window_size, mode='same')

# 5. Plot all three on the Cartesian plane
plt.figure(figsize=(12, 6))
plt.plot(time_points, clean_brainwave, color='cyan', label='Clean Signal (The Truth)')
plt.plot(time_points, noisy_brainwave, color='grey', alpha=0.5, label='Noisy Signal (What an EEG sees)')
plt.plot(time_points, filtered_brainwave, color='red', linewidth=2, label='Filtered Signal (The cleaned data)')

plt.title("Brainwave Signal Processing: Cleaning the Noise")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.legend() # This shows the box explaining what each color is
plt.grid(True)
plt.show()