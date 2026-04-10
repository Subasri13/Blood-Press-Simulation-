# ------------------------------------------
# Dynamic Simulation of Systolic and Diastolic Pressure
# Using Heart Rate Trends
# PSNA College of Engineering and Technology
# Biomedical Engineering - Mini Project
# ------------------------------------------
# HOW TO RUN:
#   1. Install libraries once:  pip install numpy matplotlib
#   2. Run this file:           python blood_pressure_simulation.py
# ------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# Seed for reproducibility
np.random.seed(42)

# ---- Generate synthetic heart rate data ----
heart_rates_fixed = [
    60.5, 61.1, 61.8, 62.3, 62.9, 63.4, 64.0, 64.6, 65.1, 65.7,
    66.3, 66.9, 67.5, 68.0, 68.6, 69.2, 69.8, 70.3, 70.9, 71.5,
    72.0, 72.6, 73.2, 73.8, 74.3, 74.9, 75.5, 76.1, 76.6, 77.2,
    77.8, 78.4, 78.9, 79.5, 80.1, 80.7, 81.2, 81.8, 82.4, 83.0,
    83.5, 84.1, 84.7, 85.3, 85.8, 86.4, 87.0, 87.6, 88.1, 88.7,
    89.3, 89.9, 90.4, 91.0, 91.6, 92.2, 92.7, 93.3, 93.9, 94.5,
    95.0, 95.6, 96.2, 96.8, 97.3, 97.9, 98.5, 99.1, 99.6, 100.0,
]
heart_rates_random = np.linspace(60, 100, 130) + np.random.randn(130) * 1.5
heart_rates = np.array(heart_rates_fixed + list(heart_rates_random))

# ---- Generate synthetic amplitude variations ----
amplitudes_fixed = [
    0.050, 0.052, 0.054, 0.056, 0.058, 0.060, 0.062, 0.064, 0.066, 0.068,
    0.070, 0.072, 0.074, 0.076, 0.078, 0.080, 0.082, 0.084, 0.086, 0.088,
    0.090, 0.092, 0.094, 0.096, 0.098, 0.100, 0.102, 0.104, 0.106, 0.108,
    0.110, 0.112, 0.114, 0.116, 0.118, 0.120, 0.122, 0.124, 0.126, 0.128,
    0.130, 0.132, 0.134, 0.136, 0.138, 0.140, 0.142, 0.144, 0.146, 0.148,
    0.150, 0.148, 0.146, 0.144, 0.142, 0.140, 0.138, 0.136, 0.134, 0.132,
    0.130, 0.128, 0.126, 0.124, 0.122, 0.120, 0.118, 0.116, 0.114, 0.112,
    0.110, 0.108, 0.106, 0.104, 0.102, 0.100, 0.098, 0.096, 0.094, 0.092,
    0.090, 0.088, 0.086, 0.084, 0.082, 0.080, 0.078, 0.076, 0.074, 0.072,
    0.070, 0.068, 0.066, 0.064, 0.062, 0.060, 0.058, 0.056, 0.054, 0.052,
]
amplitudes_random = np.linspace(0.05, 0.15, 120) + np.random.randn(120) * 0.005
amplitudes = np.array(amplitudes_fixed + list(amplitudes_random))

# ---- Trim to 200 points ----
heart_rates = heart_rates[:200]
amplitudes  = amplitudes[:200]

# ---- Simulate Blood Pressure ----
base_systolic  = 90
hr_factor      = 0.5    # sensitivity to heart rate
amp_factor     = 100    # sensitivity to amplitude
noise          = np.random.randn(200) * 2

systolic_bp    = base_systolic + heart_rates * hr_factor + amplitudes * amp_factor + noise
pulse_pressure = 35 + np.random.randn(200) * 2
diastolic_bp   = systolic_bp - pulse_pressure

# ---- Display first 5 data points ----
print("First 5 simulated data points:")
print(f"{'HeartRate':>12} {'Amplitude':>12} {'SystolicBP':>12} {'DiastolicBP':>12}")
print("-" * 52)
for i in range(5):
    print(f"{heart_rates[i]:>12.1f} {amplitudes[i]:>12.3f} {systolic_bp[i]:>12.1f} {diastolic_bp[i]:>12.1f}")

# ---- Plotting ----
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7))

ax1.plot(systolic_bp,  'r', linewidth=1.5, label='Systolic BP')
ax1.plot(diastolic_bp, 'b', linewidth=1.5, label='Diastolic BP')
ax1.legend()
ax1.set_title('Simulated Blood Pressure Over Time')
ax1.set_xlabel('Time Index')
ax1.set_ylabel('Pressure (mmHg)')
ax1.grid(True)

ax2.plot(heart_rates, 'k')
ax2.set_title('Heart Rate Over Time')
ax2.set_xlabel('Time Index')
ax2.set_ylabel('Heart Rate (BPM)')
ax2.grid(True)

plt.tight_layout()
plt.show()
