# Phases Of Moon

A lightweight animated desktop moon that subtly cycles through the lunar phases — with a system tray icon, adjustable speed, and a keyboard shortcut toggle.

---

## Features

- Displays an animated moon on your desktop.
- Click & drag to reposition it anywhere.
- Right-click tray icon to:
  - Show/Hide the moon
  - Adjust phase animation speed
  - Quit the app
- Press `Ctrl + M` anytime to toggle moon visibility.
- Runs in background — perfect ambient companion.

---

## Technologies Used

- `Python 3`
- `Tkinter` – GUI
- `Pillow (PIL)` – Image processing
- `pystray` – System tray integration
- `keyboard` – Global hotkey handling
- `PyInstaller` – Executable packaging

---

## How to Run

### Option 1: Use the Executable

If you have the `.exe` file (`Phases Of Moon.exe`), simply **double-click** to run.  
No installation or dependencies needed.

---

### Option 2: Run from Source (for developers)

#### 1. Install dependencies

```bash
pip install pillow pystray keyboard
```

#### 2. Run the app

```bash
python app.py
```
---

## Shortcut

- Press `Ctrl + M` to instantly show/hide the moon.

---

## Changing the Phase Speed

- Right-click the tray icon → Set Phase Speed
- Enter time (in seconds) between phase changes (minimum: `0.5` seconds)

## Build Instructions

To package as a standalone `.exe`, run:

```bash
pyinstaller --onefile --noconsole --name "Phases Of Moon" --icon=Images/MoonIcon.ico --add-data "Images;Images" app.py
```

## Notes

- Images are bundled inside the `.exe` — no need to share separately.
- Works only on Windows (due to global hotkey library `keyboard`).

## Screenshots
![image](https://github.com/user-attachments/assets/e5b3ddea-fa11-458a-8c12-bc677e611e0f)



## Author

Kushal Ravindrakumar Gupta

