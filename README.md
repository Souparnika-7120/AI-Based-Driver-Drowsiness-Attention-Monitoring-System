Overview

This project presents a real-time AI-powered Driver Drowsiness Detection System built using computer vision techniques.

The system monitors facial and eye activity using a live camera feed and detects prolonged eye closure to identify signs of driver fatigue.

This prototype simulates a modular AI-based driver monitoring solution that can be integrated into Advanced Driver Assistance Systems (ADAS) and intelligent vehicle safety platforms.

Problem Statement

Driver fatigue is a significant contributor to road accidents worldwide.

Manual monitoring methods are inefficient and unreliable. An automated real-time detection system can reduce risk by identifying early fatigue symptoms and triggering timely alerts.

Working Principle

The system operates through the following pipeline:

1️. Video Capture

The webcam continuously captures real-time video frames.

2️. Preprocessing

Each frame is converted to grayscale to improve detection efficiency and reduce computational complexity.

3️. Face Detection

Haar Cascade classifier is used to detect faces within each frame.

4️. Eye Detection

Within the detected face region, the Haar Eye Cascade identifies eye regions.

5️. Drowsiness Logic

If eyes are not detected for consecutive frames, the system increments a counter.

If the counter exceeds a predefined threshold (EYE_CLOSED_FRAMES), the system interprets this as prolonged eye closure.

6️. Alert Mechanism

When drowsiness is detected:

A visual alert message is displayed on screen.

The event is logged with a timestamp in a CSV file.

 Detection Algorithm Logic
If (Number of detected eyes == 0)
    Increase closed-eye frame counter
Else
    Reset counter

If (Closed-eye counter > threshold)
    Trigger Alert
    Log event

 System Architecture
Camera Input
      ↓
Frame Preprocessing (Grayscale Conversion)
      ↓
Face Detection
      ↓
Eye Detection
      ↓
Frame Counter Logic
      ↓
Alert Generation + Event Logging

 Tech Stack

Python

OpenCV

NumPy

Haar Cascade Classifiers
