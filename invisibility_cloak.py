import cv2
import numpy as np
import time

# Open webcam (Windows fix included)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Allow camera to warm up
time.sleep(2)

# Capture background (no person in frame)
for i in range(30):
    ret, background = cap.read()

background = np.flip(background, axis=1)

# Kernel for morphology
kernel = np.ones((5, 5), np.uint8)

print("Background captured. Now wear the GREEN cloak!")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = np.flip(frame, axis=1)

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # ✅ Correct GREEN color range (important!)
    lower_green = np.array([35, 80, 40])
    upper_green = np.array([90, 255, 255])

    # Create mask
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Remove noise
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)

    # Inverse mask
    mask_inv = cv2.bitwise_not(mask)

    # Segment out cloak from background
    cloak_area = cv2.bitwise_and(background, background, mask=mask)

    # Segment rest of frame
    current_area = cv2.bitwise_and(frame, frame, mask=mask_inv)

    # Combine both
    final_output = cv2.add(cloak_area, current_area)

    cv2.imshow("🧙 Harry Potter Invisibility Cloak", final_output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
