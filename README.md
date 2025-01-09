# Urdu-OCR-DeepLearning-Research-Project

## Project Overview
This research project aims to build an OCR system specifically for the Urdu language using deep learning techniques. The system will leverage Convolutional Neural Networks (CNNs) for feature extraction and Long Short-Term Memory networks (LSTMs) for sequence learning to recognize and transcribe Urdu text. Currently, the project is focused on collecting and preprocessing data to create a robust dataset for training the model.

## Project Structure
1. **data/**  
   Folder for storing frames, videos, and Excel data.

2. **scripts/**  
   All the Python scripts for processing and analysis:
   - `01_Writing_Recording_Canvas.py`  
   - `02_EveryFrameCoordinatesVideo_to_Excel.py`  
   - `03_RedrawfromSpecialTemporalData.py`  
   - `04_Stroke.py`  
   - `05_RedrawEveryFramefromSpecialTemporalData.py`  
   - `06_LigatureStyleVideoRemakeFromFrames.py`

3. **requirements.txt**  
   List of dependencies required to run the project.

4. **README.md**  
   Project documentation file.

5. **LICENSE**  
   License information for the project.

## Overall Workflow
The project involves several scripts that handle different stages of data collection, analysis, and drawing recreation. Here's the workflow of the project:

1. **Drawing and Recording**  
   **Script:** `01_Writing_Recording_Canvas.py`  
   Provides an interface for drawing and recording canvas activity using Tkinter.

2. **Analysis and Data Extraction**  
   **Script:** `02_EveryFrameCoordinatesVideo_to_Excell.py`  
   Processes the recorded video to extract drawing data (coordinates and timestamps) and saves them into an Excel file.

3. **Redrawing**  
   **Script:** `03_RedrawfromSpecialTemporalData.py` & `04_Stroke.py`  
   Uses the extracted data to recreate or analyze the drawing, potentially including advanced stroke analysis to differentiate between continuous strokes and separate drawing events.

4. **Frame-based Redrawing**  
   **Script:** `05_RedrawEveryFramefromSpecialTemporalData.py`  
   Redraws each frame based on the extracted coordinates, saving them as individual images.

5. **Video Remake**  
   **Script:** `06_LigatureStyleVideoRemakeFromFrames.py`  
   Compiles the saved frames into a video, reassembling the drawing into a sequence.

## Detailed Breakdown of Scripts

### `01_Writing_Recording_Canvas.py`
**Key Functions:**
- `initialize_canvas()`: Sets up the drawing canvas.
- `paint(event)`: Records drawing when the mouse is moved with the left button held down.
- `clear_canvas()`: Clears the canvas.
- `start_recording()`: Starts recording the drawing activity.
- `stop_recording()`: Stops recording and saves the frames.
- `record_frame()`: Captures and records frames.

### `02_EveryFrameCoordinatesVideo_to_Excell.py`
**Key Functions:**
- `analyze_canvas_video(video_path, canvas_size)`: Extracts coordinates from a video.
- `save_coordinates_with_time_to_excel()`: Saves extracted data to an Excel file.

### `03_RedrawfromSpecialTemporalData.py`
**Key Functions:**
- `load_coordinates_from_excel()`: Opens an Excel file with coordinates.
- `redraw_from_coordinates()`: Redraws points using the coordinates and saves as an image.

### `04_Stroke.py`
**Expected Functionality:**  
Builds on the redrawing functionality with potentially advanced stroke analysis.

### `05_RedrawEveryFramefromSpecialTemporalData.py`
**Key Functions:**
- `load_coordinates_from_excel()`: Loads coordinates from an Excel file.
- `save_frames_as_images()`: Saves each frame as an image based on the coordinates.

### `06_LigatureStyleVideoRemakeFromFrames.py`
**Key Functions:**
- `create_video_from_frames()`: Converts frames into a video.

## Current Status
The research project is in progress, with the focus currently on gathering and preprocessing data to build an effective dataset. The team is working towards integrating deep learning models, including CNN and LSTM, for accurate Urdu text recognition.

## Future Work
- **Deep Learning Models Integration:** CNN for feature extraction, LSTM for sequential learning.
- **Data Augmentation:** More data preprocessing and augmentation techniques for improved OCR accuracy.

## Requirements
- Python 3.x

The following dependencies are listed in the `requirements.txt` file, and can be installed using the following command:
```bash
pip install -r requirements.txt
