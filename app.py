import tkinter as tk
from PIL import Image, ImageTk
import os
import threading
import sys
import keyboard
from pystray import Icon, Menu, MenuItem
from PIL import Image as PILImage, ImageDraw
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class MoonAvatar(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Moon")
        self.overrideredirect(True)
        self.wm_attributes("-topmost", True)
        self.wm_attributes("-transparentcolor", "white")
        self.configure(bg="white")

        self.moon_images = []
        for i in range(1, 9):
            img_path = resource_path(f"Images/Moon{i}.png")
            img = Image.open(img_path).resize((120, 120), Image.Resampling.LANCZOS)
            self.moon_images.append(ImageTk.PhotoImage(img))

        self.current_index = 0
        self.label = tk.Label(self, image=self.moon_images[self.current_index], bg="white", bd=0)
        self.label.pack()

        self.is_visible = True
        self.drag_offset = None
        self.phase_interval = 2

        self.bind("<ButtonPress-1>", self.start_drag)
        self.bind("<B1-Motion>", self.do_drag)

        self.animate_moon()

    def start_drag(self, event):
        self.drag_offset = (event.x_root - self.winfo_x(), event.y_root - self.winfo_y())

    def do_drag(self, event):
        x, y = event.x_root - self.drag_offset[0], event.y_root - self.drag_offset[1]
        self.geometry(f"+{x}+{y}")

    def animate_moon(self):
        self.current_index = (self.current_index + 1) % len(self.moon_images)
        self.label.config(image=self.moon_images[self.current_index])
        self.after(int(self.phase_interval * 1000), self.animate_moon)

    def toggle_visibility(self):
        if self.is_visible:
            self.withdraw()
        else:
            self.deiconify()
        self.is_visible = not self.is_visible

    def set_phase_speed(self):
        def save_speed():
            try:
                val = float(entry.get())
                self.phase_interval = max(0.5, val)
                speed_window.destroy()
            except ValueError:
                entry.delete(0, tk.END)
                entry.insert(0, "Invalid")

        speed_window = tk.Toplevel(self)
        speed_window.title("Speed")
        speed_window.geometry("250x100")
        speed_window.attributes("-topmost", True)

        tk.Label(speed_window, text="Enter speed (seconds):").pack(pady=5)
        entry = tk.Entry(speed_window)
        entry.insert(0, str(self.phase_interval))
        entry.pack()
        tk.Button(speed_window, text="Apply", command=save_speed).pack(pady=5)

def listen_for_shortcut(avatar):
    keyboard.add_hotkey('ctrl+m', avatar.toggle_visibility)
    keyboard.wait()

def create_tray_icon(avatar):
    def toggle_window(icon, item):
        avatar.toggle_visibility()

    def open_speed_setting(icon, item):
        avatar.set_phase_speed()

    def exit_app(icon, item):
        icon.stop()
        avatar.destroy()
        sys.exit(0)

    icon_image = PILImage.open(resource_path("Images/MoonIcon.png")).convert("RGBA").resize((64, 64), PILImage.Resampling.LANCZOS)
    menu = Menu(
        MenuItem("Show/Hide Moon", toggle_window),
        MenuItem("Set Phase Speed", open_speed_setting),
        MenuItem("Quit", exit_app)
    )

    icon = Icon("The Moon", icon_image, "The Moon", menu)
    icon.run()


if __name__ == "__main__":
    moon_avatar = MoonAvatar()

    tray_thread = threading.Thread(target=create_tray_icon, args=(moon_avatar,), daemon=True)
    tray_thread.start()

    shortcut_thread = threading.Thread(target=listen_for_shortcut, args=(moon_avatar,), daemon=True)
    shortcut_thread.start()

    moon_avatar.mainloop()

# pyinstaller --onefile --noconsole --name "Phases Of Moon" --icon=Images/MoonIcon.ico --add-data "Images;Images" app.py