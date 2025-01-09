import cv2
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolo11n-pose.pt")

# Function to extract selected keypoints (5, 6, 7, 9, 10)
def extract_keypoints(keypoints):
    keypoints_dict = {}
    if keypoints is not None and hasattr(keypoints, 'xy'):
        xy = keypoints.xy.cpu().numpy()  # Extract (x, y) coordinates
        selected_indices = [5, 6, 7, 8, 9, 10]
        for i in selected_indices:
            if i < len(xy[0]):  # Ensure keypoint index exists
                keypoints_dict[i] = {'x': xy[0][i][0], 'y': xy[0][i][1]}
    return keypoints_dict

# Function to check if hands are raised (wrist above elbow)
def are_hands_raised(keypoints_dict):
    # Check for left hand (keypoints 7 for elbow and 9 for wrist)
    if 7 in keypoints_dict and 9 in keypoints_dict:
        left_elbow_y = keypoints_dict[7]['y']
        left_wrist_y = keypoints_dict[9]['y']
        # print( "left_wrist_y:",left_wrist_y, " < left_elbow_y:" ,left_elbow_y)
        if left_wrist_y < left_elbow_y:  # Wrist above elbow
            return True

    # Check for right hand (keypoints 8 for elbow and 10 for wrist)
    if 8 in keypoints_dict and 10 in keypoints_dict:
        right_elbow_y = keypoints_dict[8]['y']
        right_wrist_y = keypoints_dict[10]['y']
        # print("right_wrist_y:", right_wrist_y, " < right_elbow_y:", right_elbow_y)
        if right_wrist_y < right_elbow_y:  # Wrist above elbow
            return True

    return False

# Open video file
cap = cv2.VideoCapture(0)

# Check if video is opened correctly
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    # Read frame by frame
    ret, frame = cap.read()
    if not ret:
        break  # End of video

    # Run inference on the current frame
    results = model(frame, show=True)

    # Extract keypoints for the first detected person (if available)
    detections = results[0].keypoints

    if detections is not None:
        keypoints_dict = extract_keypoints(detections)
        # print(keypoints_dict)

        # Check if hands are raised
        if are_hands_raised(keypoints_dict):
            print()
            print("RAISED")
        else:
            print("NOT RAISED")
    else:
        print("No keypoints detected.")

    # Show the processed frame
    # cv2.imshow("Video", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
