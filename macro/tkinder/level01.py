import tkinter as tk
from tkinter import messagebox
import pyautogui
import time
import threading

def start_macro():
    txt1 = entry1.get()
    print(f'text 1 result : {txt1}')

root = tk.Tk()
root.title('MACRO TEST')
win_width  = 700
win_height = 900

screen_width  = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width  // 2) - (win_width  // 2)
y = (screen_height // 2) - (win_height // 2)

root.geometry(f"{win_width}x{win_height}+{x}+{y}")

label1 = tk.Label(root, text="테스트 텍스트 :", anchor='w', width=20, font=("Arial", 12, "bold italic"))
label1.pack(pady=5, padx=30, anchor='w')

entry1 = tk.Entry(root, width=50, font=("Arial", 14, "italic"))
entry1.pack(pady=5, padx=30, anchor='w')

frame = tk.Frame(root)
frame.pack(pady=10, padx=30)

text_frame1 = tk.Frame(frame)
text_frame1.grid(row=0, column=0, padx=5)

text_area1 = tk.Text(text_frame1, height=20, width=30, font=("Arial", 12), wrap=tk.WORD)
text_area1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar1 = tk.Scrollbar(text_frame1, command=text_area1.yview)
scrollbar1.pack(side=tk.RIGHT, fill=tk.Y)

text_area1.config(yscrollcommand=scrollbar1.set)

text_frame2 = tk.Frame(frame)
text_frame2.grid(row=0, column=1, padx=5)

text_area2 = tk.Text(text_frame2, height=20, width=30, font=("Arial", 12), wrap=tk.WORD)
text_area2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar2 = tk.Scrollbar(text_frame2, command=text_area2.yview)
scrollbar2.pack(side=tk.RIGHT, fill=tk.Y)

text_area2.config(yscrollcommand=scrollbar2.set)

frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_rowconfigure(0, weight=1)

button = tk.Button(root, text="매크로 시작", command=start_macro, width=40, height=4, bg="#000000", fg="white", font=("Arial", 10, "bold italic"))
button.pack(pady=10, anchor="center")

root.mainloop()