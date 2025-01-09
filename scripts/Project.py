import subprocess
import os
import tkinter as tk
from tkinter import messagebox

def run_script(script_name):
    """Run a given script."""
    try:
        # Print current working directory and script folder contents for debugging
        print(f"Current working directory: {os.getcwd()}")
        print(f"Contents of current directory: {os.listdir(os.getcwd())}")

        # Get the absolute path of the script to run
        script_path = os.path.abspath(script_name)
        print(f"Looking for script at: {script_path}")

        # Check if the script exists before attempting to run it
        if not os.path.exists(script_path):
            messagebox.showerror("Error", f"Script not found: {script_path}")
            print(f"Script not found at: {script_path}")
            return

        # Specify the full path to the Python executable (use `python3` if necessary)
        python_exe = "python"  # Change this to the full path if needed, e.g., "C:\\Python39\\python.exe"
        print(f"Using Python executable: {python_exe}")

        # Run the script and capture the output
        result = subprocess.run([python_exe, script_path], capture_output=True, text=True)

        # Print output and error messages for debugging
        print(f"STDOUT: {result.stdout}")
        print(f"STDERR: {result.stderr}")

        # Check if the script ran successfully
        if result.returncode == 0:
            messagebox.showinfo("Success", f"{script_name} ran successfully.")
        else:
            messagebox.showerror("Error", f"Error running {script_name}.\n\n{result.stderr}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        print(f"Error: {str(e)}")

def create_gui():
    """Create GUI interface."""
    window = tk.Tk()
    window.title("Urdu OCR Deep Learning Research Project")

    # Set window size and background color
    window.geometry("600x600")
    window.config(bg="#2c3e50")  # Dark background for a professional look

    # Add a heading label with a modern font style and color
    label = tk.Label(window, text="Select a Script to Run", font=("Helvetica", 20, "bold"), bg="#2c3e50", fg="#ecf0f1")
    label.pack(pady=30)

    # Define the style for the buttons
    button_style = {
        "font": ("Helvetica", 12, "bold"),
        "bg": "#2980b9",  # Blue background for professional look
        "fg": "#fff",  # White text
        "activebackground": "#3498db",  # Slightly lighter blue when clicked
        "relief": "flat",
        "width": 40,
        "height": 2,
        "bd": 0,
        "highlightthickness": 0,
    }

    # Create a frame for the buttons to give some padding and structure
    frame = tk.Frame(window, bg="#2c3e50")
    frame.pack(pady=10)

    # Create buttons with the defined style and add them to the frame
    button1 = tk.Button(frame, text="Run 01_Writing_Recording_Canvas.py", command=lambda: run_script('scripts/01_Writing_Recording_Canvas.py'), **button_style)
    button1.grid(row=0, column=0, pady=10)

    button2 = tk.Button(frame, text="Run 02_EveryFrameCoordinatesVideo_to_Excel.py", command=lambda: run_script('scripts/02_EveryFrameCoordinatesVideo_to_Excel.py'), **button_style)
    button2.grid(row=1, column=0, pady=10)

    button3 = tk.Button(frame, text="Run 03_RedrawfromSpecialTemporalData.py", command=lambda: run_script('scripts/03_RedrawfromSpecialTemporalData.py'), **button_style)
    button3.grid(row=2, column=0, pady=10)

    button4 = tk.Button(frame, text="Run 04_Stroke.py", command=lambda: run_script('scripts/04_Stroke.py'), **button_style)
    button4.grid(row=3, column=0, pady=10)

    button5 = tk.Button(frame, text="Run 05_RedrawEveryFramefromSpecialTemporalData.py", command=lambda: run_script('scripts/05_RedrawEveryFramefromSpecialTemporalData.py'), **button_style)
    button5.grid(row=4, column=0, pady=10)

    button6 = tk.Button(frame, text="Run 06_LigatureStyleVideoRemakeFromFrames.py", command=lambda: run_script('scripts/06_LigatureStyleVideoRemakeFromFrames.py'), **button_style)
    button6.grid(row=5, column=0, pady=10)

    # Add some extra space at the bottom
    frame.pack(pady=40)

    # Start the Tkinter event loop
    window.mainloop()

if __name__ == '__main__':
    create_gui()
