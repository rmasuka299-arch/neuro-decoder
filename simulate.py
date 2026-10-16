import numpy as np
import matplotlib.pyplot as plt
# Parameters for our mock brainwave
sample_rate = 100  # How many data points per second (Hz)
duration = 1       # Length of the recording in seconds
frequency = 10     # Alpha brainwaves are around 10 Hz

# Generate the time points
time_points = np.linspace(0, duration, sample_rate * duration, endpoint=False)

# Generate the brainwave using a sine wave
brainwave = np.sin(2 * np.pi * frequency * time_points)

# Print the results
print("🧠 Mock Brainwave Generated!")
print(f"Total data points captured: {len(brainwave)}")
print(f"First 5 signal values: {brainwave[:5]}")
# --- NEW CODE TO DRAW THE GRAPH ---
plt.figure(figsize=(10, 4)) # Make a wide box
plt.plot(time_points, brainwave, color='cyan') # Draw the wave in cyan
plt.title("Mock Alpha Brainwave (10 Hz)")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude (Voltage)")
plt.grid(True)
plt.show() # This pops up the window with the graph!