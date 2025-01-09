import cv2
import numpy as np
import pandas as pd  

def analyze_canvas_video(video_path, canvas_size=(400, 200)):
    """
    Analyzes a video of canvas drawing to detect writing start and end times
    and records coordinates with their corresponding timestamps.

    Parameters:
        video_path (str): Path to the recorded video.
        canvas_size (tuple): Dimensions of the canvas (width, height).

    Returns:
        list: A list of dictionaries containing coordinates and their timestamps.
    """
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Cannot open video file {video_path}")
        return None

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_duration = 1 / fps

    prev_frame = None
    frame_index = 0

    recorded_data = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_index += 1
        current_time = frame_index * frame_duration

        # Resize frame to canvas size (if needed)
        frame = cv2.resize(frame, canvas_size)

        # Convert to grayscale for pixel comparison
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, binary_frame = cv2.threshold(gray_frame, 50, 255, cv2.THRESH_BINARY)

        if prev_frame is None:
            prev_frame = binary_frame
            continue

        # Detect differences between current and previous frames
        diff = cv2.absdiff(prev_frame, binary_frame)
        non_zero_coords = cv2.findNonZero(diff)

        if non_zero_coords is not None:
            for coord in non_zero_coords:
                x, y = coord[0].tolist()  # Extract [x, y] values
                recorded_data.append({"Time": current_time, "X": x, "Y": y})

        prev_frame = binary_frame

    cap.release()
    return recorded_data

def save_coordinates_with_time_to_excel(recorded_data, output_file="data\canvas_analysis.xlsx"):
    """
    Saves the coordinates with timestamps to an Excel file.

    Parameters:
        recorded_data (list): List of dictionaries containing time, X, and Y values.
        output_file (str): The name of the Excel file to save.
    """
    # Create DataFrame
    df = pd.DataFrame(recorded_data)

    # Write to Excel
    df.to_excel(output_file, sheet_name="Coordinates with Time", index=False)

    print(f"Coordinates with timestamps saved to {output_file}")

# Input recorded video path
video_path = "data/canvas_recording.mp4"

# Analyze video
recorded_data = analyze_canvas_video(video_path)

# Output results (save all data to Excel)
if recorded_data:
    print(f"Total Data Points Recorded: {len(recorded_data)}")

    # Save coordinates with timestamps to Excel
    save_coordinates_with_time_to_excel(recorded_data)
