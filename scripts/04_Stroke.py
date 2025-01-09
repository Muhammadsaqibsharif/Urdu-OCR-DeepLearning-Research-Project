import cv2
import numpy as np
import pandas as pd
from tkinter import Tk, filedialog

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


def classify_arrows(coordinates):
    """
    Classifies strokes into arrow directions to differentiate Urdu characters based on drawing patterns.

    Parameters:
        coordinates (list): List of dictionaries with 'Time', 'X', and 'Y'.

    Returns:
        list: Classified directions of the strokes (e.g., 'up', 'down', 'left', 'right', etc.).
    """
    directions = []

    for i in range(1, len(coordinates)):
        prev_coord = coordinates[i - 1]
        curr_coord = coordinates[i]

        dx = curr_coord['X'] - prev_coord['X']
        dy = curr_coord['Y'] - prev_coord['Y']

        if abs(dx) > abs(dy):
            if dx > 0:
                directions.append('right')
            else:
                directions.append('left')
        else:
            if dy > 0:
                directions.append('down')
            else:
                directions.append('up')

    return directions


def differentiate_urdu_characters(directions):
    """
    Maps stroke directions to Urdu characters based on predefined patterns.

    Parameters:
        directions (list): List of stroke directions.

    Returns:
        str: Recognized Urdu character or a message indicating no match.
    """
    urdu_patterns = {
        'up-right-down': 'Alif',
        'right-down-left': 'Bay',
        'down-right-up-left': 'Jeem',
        # Add more patterns as needed for different Urdu characters
    }

    pattern_key = '-'.join(directions)
    return urdu_patterns.get(pattern_key, "No matching Urdu character found.")


def visualize_character_on_canvas(coordinates, directions, recognized_character, canvas_size=(400, 400)):
    """
    Visualizes the strokes and recognized Urdu character on a canvas.

    Parameters:
        coordinates (list): List of dictionaries with 'Time', 'X', and 'Y'.
        directions (list): Detected stroke directions.
        recognized_character (str): The recognized Urdu character.
        canvas_size (tuple): Dimensions of the canvas (width, height).
    """
    canvas = np.zeros((canvas_size[1], canvas_size[0], 3), dtype=np.uint8)

    # Draw strokes on the canvas
    for i in range(1, len(coordinates)):
        start = (coordinates[i - 1]['X'], coordinates[i - 1]['Y'])
        end = (coordinates[i]['X'], coordinates[i]['Y'])
        cv2.line(canvas, start, end, (255, 255, 255), thickness=2)

        # Overlay direction text
        if i - 1 < len(directions):
            midpoint = ((start[0] + end[0]) // 2, (start[1] + end[1]) // 2)
            cv2.putText(canvas, directions[i - 1], midpoint, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    # Overlay recognized character
    cv2.putText(canvas, f"Recognized Character: {recognized_character}", (10, canvas_size[1] - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

    # Display the canvas
    cv2.imshow("Urdu Character Recognition", canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Main script
if __name__ == "__main__":
    print("Please select the Excel file containing coordinates.")
    coordinates = load_coordinates_from_excel()

    if coordinates:
        print("Classifying strokes into directions...")
        directions = classify_arrows(coordinates)
        print("Detected stroke directions:", directions)

        print("Differentiating Urdu character...")
        character = differentiate_urdu_characters(directions)
        print("Recognized Urdu character:", character)

        print("Visualizing on canvas...")
        visualize_character_on_canvas(coordinates, directions, character)
