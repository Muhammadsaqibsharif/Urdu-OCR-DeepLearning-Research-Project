import tkinter as tk
from PIL import Image, ImageDraw
import cv2
import numpy as np
import threading

# Global variables
width = 400
height = 200
bg_color = "black"
pen_color = "white"
is_recording = False
video_writer = None
frames = []

# Function to initialize drawing canvas
def initialize_canvas():
    global canvas, image, draw
    canvas = tk.Canvas(root, width=width, height=height, bg=bg_color, cursor="cross")
    canvas.pack()
    image = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(image)

# Function to draw on the canvas
def paint(event):
    x1, y1 = (event.x - 2), (event.y - 2)
    x2, y2 = (event.x + 2), (event.y + 2)
    canvas.create_oval(x1, y1, x2, y2, fill=pen_color, outline=pen_color)
    draw.line([x1, y1, x2, y2], fill=pen_color, width=2)

    if is_recording:
        record_frame()

# Function to clear the canvas
def clear_canvas():
    canvas.delete("all")
    draw.rectangle([0, 0, width, height], fill=bg_color)

# Function to start recording
def start_recording():
    global is_recording, frames
    is_recording = True
    frames = []
    label_text.set("Recording started. Draw on the canvas.")

# Function to stop recording and save the video
def stop_recording():
    global is_recording, video_writer, frames
    if not is_recording:
        label_text.set("Recording is not active.")
        return

    is_recording = False
    label_text.set("Recording stopped. Saving video...")

    # Convert frames to video
    output_file = "data\canvas_recording.mp4"
    fps = 10  # Frames per second
    frame_array = [cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR) for frame in frames]

    # Create a VideoWriter object
    video_writer = cv2.VideoWriter(
        output_file,
        cv2.VideoWriter_fourcc(*"mp4v"),
        fps,
        (width, height)
    )
    for frame in frame_array:
        video_writer.write(frame)
    video_writer.release()

    label_text.set(f"Recording saved as {output_file}")

# Function to capture a frame
def record_frame():
    global image
    frames.append(image.copy())

# Main application window
root = tk.Tk()
root.title("Canvas Recorder")

label_text = tk.StringVar()
label_text.set("Draw on the canvas. Press 'Record' to start recording.")

# Initialize UI elements
initialize_canvas()
canvas.bind("<B1-Motion>", paint)

label = tk.Label(root, textvariable=label_text, font=("Helvetica", 16), fg="white", bg="black")
label.pack()

button_frame = tk.Frame(root)
button_frame.pack()

clear_button = tk.Button(button_frame, text="Clear", command=clear_canvas)
clear_button.pack(side=tk.LEFT, padx=10)

record_button = tk.Button(button_frame, text="Record Canvas", command=start_recording)
record_button.pack(side=tk.LEFT, padx=10)

stop_button = tk.Button(button_frame, text="Stop Recording", command=stop_recording)
stop_button.pack(side=tk.RIGHT, padx=10)

# Start the Tkinter event loop
root.mainloop()
