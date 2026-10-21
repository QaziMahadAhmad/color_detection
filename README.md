# Real-Time Color Detection with OpenCV

A simple computer vision project built with Python and OpenCV that detects objects of a selected color in real time using a webcam. It uses HSV color thresholding, binary masking, contour detection, and bounding boxes to locate matching regions in a video stream.

## Overview

This project demonstrates how basic image processing techniques can be used to identify colored regions in real-time video.

The webcam captures video frames, converts them from BGR to HSV color space, and creates a mask based on the selected color range. OpenCV then identifies contours in the mask and draws bounding boxes around sufficiently large detected regions.

## Features

- Real-time webcam video processing
- BGR to HSV color space conversion
- Color range thresholding
- Binary mask generation
- Contour detection for matching regions
- Bounding boxes around detected regions
- Minimum contour area filtering to reduce small, unwanted detections
- Separate windows for the original video and color mask

## Technologies Used

- **Python** — application logic
- **OpenCV** — image processing and computer vision
- **NumPy** — numerical arrays and color limit handling

## Project Structure

```text
color_detection/
├── main.py
├── util.py
├── requirements.txt
└── README.md
```

| File | Description |
|---|---|
| `main.py` | Captures webcam frames, generates the color mask, detects contours, and draws bounding boxes. |
| `util.py` | Calculates the lower and upper HSV limits for the selected BGR color. |
| `requirements.txt` | Lists the Python dependencies required to run the project. |
| `README.md` | Project documentation and setup instructions. |

## How It Works

The application follows this computer vision pipeline:

1. **Capture video:** OpenCV reads frames from the webcam.
2. **Convert color space:** Each frame is converted from BGR to HSV.
3. **Calculate color limits:** The selected BGR color is converted to HSV, and a range of acceptable values is calculated.
4. **Create a mask:** `cv2.inRange()` identifies pixels within the specified HSV range. Matching pixels become white, and other pixels become black.
5. **Detect contours:** OpenCV finds the outer boundaries of connected white regions.
6. **Filter small regions:** Contours below the configured area threshold are ignored.
7. **Draw bounding boxes:** Green rectangles are drawn around the remaining detected regions.
8. **Display results:** The original webcam feed and binary mask are displayed in separate windows.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/color_detection.git
cd color_detection
```

Replace `YOUR_USERNAME/color_detection` with your actual GitHub repository path.

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

**Ubuntu / Linux / macOS**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

If `requirements.txt` has not been created yet, install the dependencies directly:

```bash
python -m pip install opencv-python numpy
```

### 5. Run the application

```bash
python main.py
```

Make sure your webcam is connected and accessible. If the default camera does not work, change `cv2.VideoCapture(0)` in `main.py` to `cv2.VideoCapture(1)` and try again.

Press **`q`** to exit the application.

## Configuration

### Change the detected color

The selected color is defined in `main.py` using BGR values:

```python
yellow = [0, 255, 255]
```

You can replace it with another BGR color:

| Color | BGR Values |
|---|---|
| Blue | `[255, 0, 0]` |
| Green | `[0, 255, 0]` |
| Red | `[0, 0, 255]` |
| Yellow | `[0, 255, 255]` |

For example, to detect blue:

```python
blue = [255, 0, 0]
```

Then pass `blue` to `get_limits()` and use the corresponding variable throughout the detection pipeline.

### Adjust the detection sensitivity

In `util.py`, the HSV range is calculated using a hue tolerance of 10:

```python
lowerLimit = np.array(
    [max(0, hue - 10), 100, 100],
    dtype=np.uint8
)

upperLimit = np.array(
    [min(179, hue + 10), 255, 255],
    dtype=np.uint8
)
```

The saturation and value thresholds help exclude dull or dark pixels. These values may need adjustment depending on lighting conditions and the selected object.

In `main.py`, the minimum contour area is set to 500 pixels:

```python
if cv2.contourArea(contour) > 500:
```

Increasing this value filters out more small regions, while decreasing it allows smaller regions to be detected.

## Output

The application displays two windows:

- **Color Detection:** The live webcam feed with green bounding boxes around detected regions.
- **Color Mask:** A binary image showing detected color regions in white against a black background.

Detection quality depends on lighting, background colors, camera quality, and the selected HSV thresholds.

## Limitations

- Detects colors rather than identifying object categories.
- Similar-colored objects and background regions may also be detected.
- Changes in lighting can affect detection accuracy.
- Objects with overlapping or connected regions may be represented by a single contour.
- The current implementation uses a fixed color range and a fixed minimum contour area.

## Learning Outcomes

Through this project, I explored:

- Fundamental image processing with OpenCV
- BGR and HSV color representations
- HSV thresholding and binary masks
- Contour detection and contour area filtering
- Bounding rectangle calculation and drawing
- Real-time video processing with a webcam
- Organizing a Python project across multiple files

## Future Improvements

- Detect multiple colors simultaneously.
- Add interactive color selection.
- Tune HSV thresholds dynamically using trackbars.
- Improve robustness under different lighting conditions.
- Add object tracking across consecutive video frames.
- Display the detected color name and bounding box coordinates.

## License

This project is available for educational and personal learning purposes. Add a `LICENSE` file if you want to specify formal reuse and distribution terms.

---

**Author:** [Mahad](https://github.com/QaziMahadAhmad)

**GitHub:** [QaziMahadAhmad](https://github.com/QaziMahadAhmad)
