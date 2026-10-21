
import cv2
import numpy as np
from util import get_limits


# BGR color values: Blue, Green, Red
yellow = [0, 255, 255]

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Could not access the webcam.")
        break

    # Convert the frame from BGR to HSV
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get the HSV limits for yellow
    lowerLimit, upperLimit = get_limits(yellow)

    # Create a mask for the selected color
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    # Find the objects matching the color
    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    # Draw a rectangle around detected objects
    for contour in contours:
        if cv2.contourArea(contour) > 500:
            x, y, w, h = cv2.boundingRect(contour)

            cv2.rectangle(
                frame, (x, y), (x + w, y + h), (0, 255, 0), 2
            )

    cv2.imshow("Color Detection", frame)
    cv2.imshow("Color Mask", mask)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
