import numpy as np
import scipy as scp
import matplotlib.pyplot as plt

samples = int(1e5)
interval_len = 5e3
time_steps = np.linspace(0, interval_len, samples)

freq_offset = 0.1

base_freq = 2 * np.pi
freq_ratio = (2*base_freq + freq_offset) / 2 / np.pi
beating_freq = freq_offset / base_freq

tone1 = np.cos(time_steps)
tone2 = np.cos(freq_ratio * time_steps)

beating_tone = np.cos(beating_freq * time_steps)
envelope = 2 * np.cos(beating_freq / 2 * time_steps)

bi_tone = tone1 + tone2

plt.plot(time_steps, bi_tone)
plt.plot(time_steps, envelope, linewidth=3)
plt.show()
