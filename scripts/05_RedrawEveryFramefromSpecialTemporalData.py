import cv2
import numpy as np
import pandas as pd
from tkinter import Tk, filedialog
import os

def load_coordinates_from_excel():
    """
    Opens a file dialog to ask the user for an Excel file containing coordinates.

    Returns:
        list: A list of dictionaries with 'Time', 'X', and 'Y' coordinates if a valid file is provided, otherwise None.
    """
    Tk().withdraw()  # Hide the main tkinter window
    file_path = filedialog.askopenfilename(
        title="Select an Excel File with Coordinates",
        filetypes=(("Excel Files", "*.xlsx *.xls"), ("All Files", "*.*"))
    )
    if not file_path:
        print("No file selected.")
        return None

    try:
        # Load the Excel file into a DataFrame
        df = pd.read_excel(file_path)

        # Validate that the file contains Time, X, and Y columns
        if 'Time' in df.columns and 'X' in df.columns and 'Y' in df.columns:
            coordinates = df.to_dict(orient='records')  # Convert DataFrame to a list of dictionaries
            return coordinates
        else:
            print("Excel file must contain 'Time', 'X', and 'Y' columns.")
            return None
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

def save_frames_as_images(coordinates, canvas_size=(400, 200), output_dir="data/frames"):
    """
    Saves each coordinate point as an individual image frame in sequence.

    Parameters:
        coordinates (list): List of dictionaries with 'Time', 'X', and 'Y' to redraw.
        canvas_size (tuple): Dimensions of the canvas (width, height).
        output_dir (str): Directory to save the frames.
    """
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Create a blank canvas
    canvas = np.zeros((canvas_size[1], canvas_size[0], 3), dtype=np.uint8)

    # Set the drawing color (white)
    draw_color = (255, 255, 255)

    # Iterate over coordinates and save each frame
    for i, coord in enumerate(coordinates):
        x, y = coord['X'], coord['Y']
        if 0 <= x < canvas_size[0] and 0 <= y < canvas_size[1]:  # Ensure coordinates are within canvas bounds
            # Draw a small circle at the current point
            cv2.circle(canvas, (x, y), radius=1, color=draw_color, thickness=-1)

        # Save the current canvas as an image
        frame_filename = os.path.join(output_dir, f"{i}.jpg")
        cv2.imwrite(frame_filename, canvas)
        print(f"Frame {i} saved to: {frame_filename}")

# Main script
if __name__ == "__main__":
    print("Please select the Excel file containing coordinates.")
    coordinates = load_coordinates_from_excel()
    if coordinates:
        save_frames_as_images(coordinates)
