import numpy as np
from scipy.io.wavfile import write

# Same Manim Parameters
v_sound = 5.0
v_car = 2.2
f_src = 1213
duration = 7.0
sample_rate = 44100  # Standard audio sample rate

# Time array
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Car position math (starts at x = -7, moves right at 2.2 m/s)
x_car = -7 + (v_car * t)
y_diff = 1.12  # Vertical gap between car (-1.3) and observer (-0.18)

# Radial velocity and Doppler frequency
dist = np.sqrt(x_car**2 + y_diff**2)
diff_x = 0 - x_car  # Observer x is 0
v_rad = v_car * diff_x / dist
f_obs = f_src * v_sound / (v_sound - v_rad)

# Generate waveform (Integrate frequency to get continuous phase)
phase = 2 * np.pi * np.cumsum(f_obs) / sample_rate
waveform = np.sin(phase)

# Reduce volume slightly and convert to 16-bit PCM format
waveform = waveform * 0.5 
waveform_int = np.int16(waveform * 32767)

# Save the audio file
write("doppler_sound.wav", sample_rate, waveform_int)
print("Sound file generated successfully!")
