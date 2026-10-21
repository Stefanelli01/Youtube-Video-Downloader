# YouTube Video Downloader

A desktop video downloading application built with Python, **CustomTkinter**, and **yt-dlp**. It supports quality selection and browser cookie integration to download age-restricted or private videos accessible through your web browser session.

## ⚠️ Important Note on Chromium-Based Browsers

If you select a **Chromium-based browser** (such as Google Chrome, Microsoft Edge, Brave, Opera, or Vivaldi), you may occasionally encounter cookie extraction errors (e.g., `Failed to decrypt with DPAPI`).

### Why does this happen?
Modern Chromium browsers encrypt local cookie databases using OS-level security features (**DPAPI** on Windows or **App-Bound Encryption** in newer Chrome versions). Additionally, Chromium browsers place an exclusive file lock on their database files while the browser process is actively running. 

### How to avoid this:
1. **Close your browser completely** before initiating a download so `yt-dlp` can access the cookie database.
2. If the issue persists on Windows, run the application or terminal **as Administrator**.
3. Alternatively, export a `cookies.txt` file from your browser as a fallback.

---

## Prerequisites & Requirements

- **Python 3.8+** installed on your system.
- **FFmpeg**: Required by `yt-dlp` to merge video and audio streams into a single file.

---

## How to Install FFmpeg

FFmpeg is essential for processing high-quality downloads and merging separate video/audio streams into a single `.mp4` file.
Linux systems are not listed because the method for installing FFmpeg varies from one distribution to another.

### Windows

#### Package Manager (Recommended)
Open **PowerShell** or **Command Prompt** as Administrator and run:
```powershell
winget install ffmpeg