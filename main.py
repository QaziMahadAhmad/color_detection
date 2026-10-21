
import cv2
import numpy as np
from util import get_limits


# Define colors in BGR format
colors = {
    "Yellow": [0, 255, 255],
    "Green": [0, 255, 0],
    "Blue": [255, 0, 0]
}

# Bounding box colors in BGR format
box_colors = {
    "Yellow": (0, 255, 255),
    "Green": (0, 255, 0),
    "Blue": (255, 0, 0)
}

# Calculate HSV limits for every color
color_limits = {}

for name, color in colors.items():
    lowerLimit, upperLimit = get_limits(color)
    color_limits[name] = (lowerLimit, upperLimit)


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Could not access the webcam.")
        break

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Detect each selected color
    for name, (lowerLimit, upperLimit) in color_limits.items():

        mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        for contour in contours:
            if cv2.contourArea(contour) > 500:
                x, y, w, h = cv2.boundingRect(contour)

                cv2.rectangle(
                    frame,
                    (x, y),
                    (x + w, y + h),
                    box_colors[name],
                    2
                )

                cv2.putText(
                    frame,
                    name,
                    (x, max(y - 10, 20)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    box_colors[name],
                    2
                )

    cv2.imshow("Multi-Color Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
