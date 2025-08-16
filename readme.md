# screenshot to text

A Python application that allows you to select a screen area,
perform OCR (Optical Character Recognition), and copy the text to the clipboard.

## Features
- Select any area of the screen
- OCR with [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- Copy recognized text directly to clipboard
- Works in the background, triggered by a hotkey


## Installation
1. Install Python.
2. Install [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki) (must be installed and added to PATH)
3. Install required Python packages:
```bash
pip install -r requirements.txt