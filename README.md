# Hand Detection and Action Monitoring System

## Overview

This project is a video surveillance system that utilizes advanced computer vision techniques to detect and monitor specific actions in real-time. The current implementation focuses on detecting raised hands through pose estimation using the YOLO model. This serves as the first step towards creating a fully automated surveillance system capable of identifying suspicious activities and reducing the reliance on traditional NVR (Network Video Recorder) systems.

## Features

- **Real-time Hand Detection**: The system uses a pre-trained YOLO model (`yolo11n-pose.pt`) to perform real-time pose estimation and extract keypoints related to human body positions.
- **Suspicious Action Detection**: Specifically, the system identifies if hands are raised (e.g., wrist above elbow), a common gesture in various activities that might be deemed suspicious.
- **Flexible Keypoint Extraction**: The system extracts specific keypoints like the wrist, elbow, and other relevant points to determine the posture of individuals.
- **Efficient Storage Management**: By focusing on identifying only key actions, the system has the potential to reduce video storage requirements by saving only significant moments, like when suspicious actions are detected.

## How It Works

1. **Pose Estimation with YOLO**: The system uses a YOLO model trained for pose detection to estimate human keypoints in each frame of the video. It specifically tracks keypoints like wrists and elbows to check if a hand is raised above the elbow.
   
2. **Keypoint Extraction**: The function `extract_keypoints()` is used to extract keypoints from the detected poses, which are then stored in a dictionary format for easy access.

3. **Hand Raised Detection**: The function `are_hands_raised()` checks if the wrist is above the elbow for both the left and right hands. If either hand is raised, the system prints "RAISED"; otherwise, it prints "NOT RAISED".

4. **Real-Time Video Surveillance**: The system continuously captures video frames from a webcam or video source, processes each frame to detect human poses, and identifies whether hands are raised.

5. **Future Improvements**: The system is designed to be easily extendable. In the future, new suspicious actions (such as unusual posture, rapid movement, or specific gestures) will be added, and a database of detected actions can be maintained for further analysis.

## Future Scope

The system has significant potential for growth and improvement in the field of video surveillance:

- **Suspicious Action Logging**: In the future, the system will be able to save bounding boxes around detected suspicious actions, allowing security personnel to focus on critical moments without needing to sift through hours of footage.
- **Expanded Action Detection**: More actions will be added for detection, such as unusual movements, falls, or violent behavior, increasing the system's ability to identify potential security threats.
- **Intelligent Video Storage Management**: The system will eliminate the need for bulky storage solutions like NVR by intelligently deciding which video segments to store, thereby saving space and reducing costs. Only moments involving suspicious actions or critical events will be saved.
- **Multiple Cameras Integration**: The system can be scaled to work with multiple cameras, aggregating data from various sources to provide a comprehensive view of an area.
- **Anomaly Detection**: By integrating machine learning models that can detect anomalies based on historical behavior, the system could automatically flag potential threats that deviate from normal patterns of activity.
- **Cloud Integration**: Video data and detected events could be uploaded to the cloud for remote access, sharing, and further analysis.
- **Real-time Alerts**: The system will be able to send real-time alerts (emails, messages, etc.) when suspicious actions are detected, ensuring rapid response times for security teams.

## Setup Instructions

### Requirements

- Python 3.6+
- OpenCV
- Ultralytics YOLO package (for pose detection)
- A webcam or video file for input

### Installation

1. Clone this repository or download the source code.
2. Install the required dependencies:
   ```bash
   pip install opencv-python ultralytics
3. **Download the YOLO model weights**:
Ensure you have the YOLO model weights file (`yolo11n-pose.pt`) in your project directory. You can download it from the Ultralytics repository or any other source.

## Usage

1. **Run the script**:
Execute the Python script to start detecting hands in real-time:
```python hand_detection.py```

2. **Interact with the application**:
- The application will display a video feed from your webcam.
- The console will output "RAISED" if hands are detected as raised, otherwise it will output "NOT RAISED".
- Press 'q' to exit the application.

## Code Overview

The main components of the code include:

### Loading the Model

```from ultralytics import YOLO```
```model = YOLO("yolo11n-pose.pt")```

### Keypoint Extraction

The `extract_keypoints` function extracts specific keypoints from the detected results:

def extract_keypoints(keypoints):

### Hand Raise Detection Logic

The `are_hands_raised` function checks if either wrist is above its corresponding elbow:

```def are_hands_raised(keypoints_dict):```

### Video Processing Loop

The main loop captures video frames and processes them for hand detection:

```cap = cv2.VideoCapture(0)```
```while True:```

# Frame processing...

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to modify this README as needed for your specific project requirements or additional features!
