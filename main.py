"""
screenshot to text
-----------
A background application that allows you to select a screen area,
perform OCR, and copy the text to clipboard using a hotkey.
"""

import pyautogui
import pytesseract
import pyperclip
import keyboard
import tkinter as tk


HOTKEY = "ctrl+alt+z"  # Global hotkey.

start_x = start_y = end_x = end_y = 0

def on_mouse_down(event):
    global start_x, start_y
    start_x, start_y = event.x, event.y
    canvas.delete("selection")

def on_mouse_drag(event):
    canvas.delete("selection")
    canvas.create_rectangle(start_x, start_y, event.x, event.y, outline="red", width=2, tags="selection")

def on_mouse_up(event):
    global end_x, end_y
    end_x, end_y = event.x, event.y
    capture_selection()

def capture_selection():
    overlay.destroy()
    x1, y1 = min(start_x, end_x), min(start_y, end_y)
    x2, y2 = max(start_x, end_x), max(start_y, end_y)

    try:
        screenshot = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
        text = pytesseract.image_to_string(screenshot, lang="eng")
        pyperclip.copy(text)
        print("\n--- OCR TEXT ---\n")
        print(text)
        print("\n(Copied to clipboard)")
    except Exception as e:
        print("OCR error:", e)

def start_capture():
    global overlay, canvas

    overlay = tk.Tk()
    overlay.attributes("-fullscreen", True)
    overlay.attributes("-topmost", True)
    overlay.attributes("-alpha", 0.3)

    canvas = tk.Canvas(overlay, cursor="cross", bg="black")
    canvas.pack(fill="both", expand=True)
    canvas.bind("<ButtonPress-1>", on_mouse_down)
    canvas.bind("<B1-Motion>", on_mouse_drag)
    canvas.bind("<ButtonRelease-1>", on_mouse_up)

    overlay.mainloop()

def main():
    print(f"📌 Press '{HOTKEY}' to start screen capture + OCR.")
    while True:
        keyboard.wait(HOTKEY)
        start_capture()

if __name__ == "__main__":
    main()