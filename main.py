import os
import sys
import customtkinter as ctk
import yt_dlp
from tkinter import messagebox

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOWNLOADS_DIR = os.path.join(BASE_DIR, "downloads")

BROWSERS = {
    "Brave": "brave",
    "Chrome": "chrome",
    "Edge": "edge",
    "Firefox": "firefox",
    "Opera": "opera",
    "Safari": "safari",
    "Vivaldi": "vivaldi",
    "None (No Cookies)": None
}

FORMATS = {
    "Best quality": "bestvideo+bestaudio/best",
    "1080p": "bv*[height<=1080]+ba/b",
    "720p": "bv*[height<=720]+ba/b",
    "480p": "bv*[height<=480]+ba/b",
    "Worst quality": "worstvideo+worstaudio/worst",
}

def show_cookie_consent(parent):
    response = messagebox.askyesno(
        "Cookie Usage Consent",
        "This application uses your browser's local cookies to download age-restricted or private videos you have access to.\n\n"
        "Do you agree to allow the system to read cookies from your selected browser?",
        parent=parent
    )
    if not response:
        messagebox.showinfo(
            "Notice",
            "We are sorry, but without cookie access, the application cannot assist you in downloading videos. The app will now close.",
            parent=parent
        )
        sys.exit()

def download():
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("Warning", "Please enter a valid URL.", parent=app)
        return

    os.makedirs(DOWNLOADS_DIR, exist_ok=True)

    selected_browser_key = browser_var.get()
    browser_value = BROWSERS.get(selected_browser_key)

    ydl_opts = {
        "format": FORMATS[quality_var.get()],
        "merge_output_format": "mp4",
        "outtmpl": os.path.join(DOWNLOADS_DIR, "%(title)s.%(ext)s"),
    }

    if browser_value:
        ydl_opts["cookiesfrombrowser"] = (browser_value,)

    try:
        status_label.configure(text="Downloading... please wait", text_color="blue")
        app.update()

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        status_label.configure(text="Download finished!", text_color="green")
        messagebox.showinfo("Success", "Download finished successfully!", parent=app)

    except Exception as e:
        status_label.configure(text="Download Error", text_color="red")
        messagebox.showerror("Error", f"Failed to download video:\n{e}", parent=app)

app = ctk.CTk()
app.title("YouTube Video Downloader")
app.geometry("420x450")

url_label = ctk.CTkLabel(app, text="Insert Video URL", font=("Helvetica", 14, "bold"))
url_label.pack(pady=(20, 5))

url_entry = ctk.CTkEntry(
    master=app,
    width=320,
    height=35,
    border_width=2,
    corner_radius=8,
    placeholder_text="https://www.youtube.com/watch?v=..."
)
url_entry.pack(pady=5)

browser_label = ctk.CTkLabel(app, text="Select Your Browser (for Cookies)", font=("Helvetica", 14, "bold"))
browser_label.pack(pady=(15, 5))

browser_var = ctk.StringVar(value="Brave")
browser_menu = ctk.CTkOptionMenu(app, variable=browser_var, values=list(BROWSERS.keys()), width=200)
browser_menu.pack(pady=5)

quality_label = ctk.CTkLabel(app, text="Select Video Quality", font=("Helvetica", 14, "bold"))
quality_label.pack(pady=(15, 5))

quality_var = ctk.StringVar(value="Best quality")
quality_menu = ctk.CTkOptionMenu(app, variable=quality_var, values=list(FORMATS.keys()), width=200)
quality_menu.pack(pady=5)

download_button = ctk.CTkButton(
    master=app,
    text="Download Video",
    command=download,
    font=("Helvetica", 13, "bold"),
    height=35,
    width=200
)
download_button.pack(pady=20)

status_label = ctk.CTkLabel(app, text="", font=("Helvetica", 12))
status_label.pack(pady=5)

app.after(100, lambda: show_cookie_consent(app))

app.mainloop()