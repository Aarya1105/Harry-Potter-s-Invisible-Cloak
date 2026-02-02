# Harry-Potter-s-Invisible-Cloak
A real-time invisibility cloak project using Python and OpenCV that makes a green cloth invisible by replacing it with the captured background, inspired by the Harry Potter cloak.

This project implements a **real-time invisibility cloak effect** using **computer vision techniques** in Python.
By detecting a specific color (green) in the video stream and replacing that region with a previously captured background, the object covered with the cloth appears invisible—similar to the famous *Harry Potter invisibility cloak*.

The project uses the **HSV color space** for accurate color detection, along with **morphological operations** to reduce noise and improve mask quality. The final output seamlessly blends the background with the live video feed to create the illusion of invisibility.

This project is ideal for beginners learning **OpenCV**, **image masking**, and **real-time video processing*

## ⚙️ How It Works
1. The webcam captures the **background frame** without any person present.
2. Each incoming frame is converted from **BGR to HSV color space**.
3. A **green color mask** is created using predefined HSV thresholds.
4. Noise is removed using **morphological operations**.
5. The green cloth area is replaced with the background image.
6. The final frame is displayed with the invisibility effect.

## ✨ Features
* Real-time invisibility effect
* Uses HSV color space for better color detection
* Noise reduction using morphology
* Simple and beginner-friendly code
* Works with standard webcam

## 🛠️ Technologies Used
* Python
* OpenCV
* NumPy

## ▶️ How to Run
```bash
pip install opencv-python numpy
python invisible_cloak.py
```

## 🟢 Usage Tips
* Use a plain **green cloth** for best results
* Ensure good lighting conditions
* Avoid green objects in the background

## 📌 Future Enhancements
* Support for multiple cloak colors
* Background video instead of static background
* Performance optimization
* GUI controls for color calibration

## 🎯 Applications
* Computer vision learning projects
* AR/VR demonstrations
* College mini-projects
* Fun visual effects



Just say the word 😄
