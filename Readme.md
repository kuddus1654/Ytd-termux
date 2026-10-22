================================================================================
             YOUTUBE 4K VIDEO & MP3 DOWNLOADER (TERMUX / PYTHON)
================================================================================

A lightweight command-line YouTube downloader built using Python and yt-dlp,
optimized for Android environments running Termux. Supports up to 4K video 
resolution with merged audio, multiple MP3 bitrates, and direct saving to 
internal phone storage.

--------------------------------------------------------------------------------
1. FEATURES
--------------------------------------------------------------------------------
- Download video up to 4K resolution (4K, 1080p, 720p, 480p).
- High-quality audio extraction (MP3 at 320 kbps, 192 kbps, 128 kbps).
- Direct output to the phone's native internal storage (/sdcard/Download).
- JavaScript runtime support for reliable extraction without deprecation warnings.
- Clean terminal-based interactive UI.

--------------------------------------------------------------------------------
2. PREREQUISITES & REQUIRED PACKAGES
--------------------------------------------------------------------------------
To run the script in Termux without merging or extraction failures, install 
the following system and Python packages:

A. System Packages (Termux/Linux):
   - python      : Python runtime environment (3.10+)
   - ffmpeg      : Merges separate high-res video/audio streams and extracts MP3
   - quickjs     : JavaScript runtime to parse YouTube video metadata signatures

B. Python Libraries:
   - yt-dlp      : Actively maintained YouTube extraction and download engine

--------------------------------------------------------------------------------
3. INSTALLATION & SETUP (TERMUX)
--------------------------------------------------------------------------------
Run the following commands step by step in Termux:

Step 1: Grant storage permission (allow Termux to save files to your device)
  termux-setup-storage

Step 2: Update Termux repository and package index
  pkg update && pkg upgrade -y

Step 3: Install required system packages
  pkg install python ffmpeg quickjs -y

Step 4: Install the yt-dlp library via pip
  pip install --upgrade yt-dlp

--------------------------------------------------------------------------------
4. HOW TO RUN
--------------------------------------------------------------------------------
1. Navigate to the project folder:
   cd /path/to/your/project

2. Execute the script:
   python ytdow.py

3. Follow the on-screen prompts:
   - Paste the YouTube URL
   - Select download type: [1] Video (MP4) or [2] Audio Only (MP3)
   - Choose your preferred resolution or audio bitrate

Downloaded files will be saved directly into your device's "Download" folder.

--------------------------------------------------------------------------------
5. COMMON TROUBLESHOOTING
--------------------------------------------------------------------------------
* ERROR: "ffmpeg is not installed. Aborting due to --abort-on-error"
  Solution: Run `pkg install ffmpeg -y`. Do not use `pip install ffmpeg`.

* WARNING: "No supported JavaScript runtime could be found"
  Solution: Run `pkg install quickjs -y` (or `pkg install nodejs -y`).

* Permission Denied / File Not Found:
  Solution: Re-run `termux-setup-storage` and ensure file permissions are 
  granted under Android App Settings -> Termux -> Permissions.

--------------------------------------------------------------------------------
6. DISCLAIMER
--------------------------------------------------------------------------------
This tool is created for educational and personal archival purposes only.
Please respect YouTube's Terms of Service and content creators' copyrights.
================================================================================
