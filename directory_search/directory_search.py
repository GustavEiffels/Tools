import os 
import tkinter as tk
from tkinter import filedialog
os.environ['TK_SILENCE_DEPRECATION'] = '1'

def openMultiFiles():
    
    root = tk.Tk()
    root.withdraw()

    selectMultiFiles = filedialog.askopenfilenames(title="Select Multi Files!")
    
    for item in selectMultiFiles:
        fileName  = os.path.basename(item)
        print('fileName : ',fileName)

    print()



openMultiFiles()