import tkinter as tk
from tkinter import filedialog
import subprocess

root = tk.Tk()
root.title("MP4 to MP3 Converter")

file_path = ""

def select_file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("MP4 Files", "*.mp4")])
    file_path_label.config(text=file_path)

def convert_to_mp3():
    if not file_path:
        return
    output_file = file_path.replace(".mp4", ".mp3")
    command = f"ffmpeg -i \"{file_path}\" -vn -ab 192000 \"{output_file}\""
    subprocess.call(command, shell=True)
    success_label.config(text="Conversion successful!")

def clear_fields():
    file_path_label.config(text="")
    success_label.config(text="")

file_path_label = tk.Label(root, text="")
select_button = tk.Button(root, text="Select MP4", command=select_file)
convert_button = tk.Button(root, text="Convert to MP3", command=convert_to_mp3)
success_label = tk.Label(root, text="")

file_path_label.pack()
select_button.pack()
convert_button.pack()
success_label.pack()

root.mainloop()