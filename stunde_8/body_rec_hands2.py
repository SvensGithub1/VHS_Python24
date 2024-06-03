# -*- coding: utf-8 -*-
"""
Created on Sun May 26 21:30:06 2024

@author: Sven
"""
import cv2
import mediapipe as mp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.signal import butter, filtfilt

# Butterworth Bandpass Filter
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return b, a

def bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = filtfilt(b, a, data)
    return y

# Initialize MediaPipe Hands and OpenCV
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)  # Capture video from the webcam

# Prepare to store hand position data
data = []

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert the BGR image to RGB
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False

    # Process the image and detect hands
    results = hands.process(image)

    # Draw the hand annotations on the image
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Extract hand landmarks
            timestamp = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0  # Time in seconds
            for id, lm in enumerate(hand_landmarks.landmark):
                data.append([timestamp, id, lm.x, lm.y, lm.z])

    cv2.imshow('Hand Tracking', image)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Convert the collected data to a DataFrame
df = pd.DataFrame(data, columns=['Time', 'ID', 'X', 'Y', 'Z'])

# Save DataFrame to CSV
df.to_csv('hand_positions.csv', index=False)

# Plot hand position over time
plt.figure(figsize=(12, 6))

# Filter for a specific landmark ID (e.g., 0 for the wrist)
landmark_id = 0
filtered_df = df[df['ID'] == landmark_id]

# Plot X, Y, Z positions over time
plt.plot(filtered_df['Time'], filtered_df['X'], label='X position')
plt.plot(filtered_df['Time'], filtered_df['Y'], label='Y position')
plt.plot(filtered_df['Time'], filtered_df['Z'], label='Z position')

plt.xlabel('Time (s)')
plt.ylabel('Normalized Position')
plt.title('Hand Position Over Time (Landmark ID: {})'.format(landmark_id))
plt.legend()
plt.show()

# Calculate displacement between consecutive frames
filtered_df['Displacement'] = np.sqrt(filtered_df['X'].diff()**2 + filtered_df['Y'].diff()**2 + filtered_df['Z'].diff()**2)

# Plot displacement over time
plt.figure(figsize=(12, 6))
plt.plot(filtered_df['Time'], filtered_df['Displacement'], label='Displacement')
plt.xlabel('Time (s)')
plt.ylabel('Displacement')
plt.title('Hand Displacement Over Time (Landmark ID: {})'.format(landmark_id))
plt.legend()
plt.show()

# Frequency analysis using FFT
displacement = filtered_df['Displacement'].dropna().values
n = len(displacement)
sample_rate = 30  # Assuming 30 FPS for the webcam

# Apply bandpass filter
lowcut = 0.1  # Low cut frequency in Hz
highcut = 10.0  # High cut frequency in Hz
filtered_displacement = bandpass_filter(displacement, lowcut, highcut, sample_rate)

# Compute FFT
yf = fft(filtered_displacement)
xf = fftfreq(n, 1 / sample_rate)

# Only take the positive half of the frequencies
xf = xf[:n // 2]
yf = np.abs(yf[:n // 2])

# Plot the frequency spectrum
plt.figure(figsize=(12, 6))
plt.plot(xf, yf)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Frequency Spectrum of Hand Motion (Landmark ID: {})'.format(landmark_id))
plt.show()

# Find the dominant frequency
dominant_freq = xf[np.argmax(yf)]
print('Dominant Frequency of Hand Motion: {:.2f} Hz'.format(dominant_freq))
