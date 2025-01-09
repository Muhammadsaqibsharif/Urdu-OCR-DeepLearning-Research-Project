import cv2
import os

def create_video_from_frames(input_dir="data/frames", output_file="data\output_video.avi", frame_rate=30):
    """
    Creates a video from a sequence of image frames stored in a directory.

    Parameters:
        input_dir (str): Directory containing image frames.
        output_file (str): Path to save the output video file.
        frame_rate (int): Frame rate of the output video.
    """
    # Get a sorted list of frame file names
    frame_files = sorted([f for f in os.listdir(input_dir) if f.endswith('.jpg')], key=lambda x: int(x.split('.')[0]))

    if not frame_files:
        print("No frames found in the directory.")
        return

    # Read the first frame to get the dimensions
    first_frame = cv2.imread(os.path.join(input_dir, frame_files[0]))
    height, width, layers = first_frame.shape

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec for .avi file
    video = cv2.VideoWriter(output_file, fourcc, frame_rate, (width, height))

    # Read and write each frame
    for frame_file in frame_files:
        frame_path = os.path.join(input_dir, frame_file)
        frame = cv2.imread(frame_path)
        video.write(frame)
        print(f"Adding frame: {frame_path}")

    # Release the video writer
    video.release()
    print(f"Video saved as: {output_file}")

# Main script
if __name__ == "__main__":
    create_video_from_frames()
