import os
import sys
import yt_dlp

def main():
    print("=" * 45)
    print("      YouTube Video & Audio Downloader      ")
    print("=" * 45)

    url = input("\nEnter YouTube Video URL: ").strip()
    if not url:
        print("[!] URL cannot be empty.")
        sys.exit(1)

    print("\nSelect Download Type:")
    print("  [1] Video (MP4 - supports up to 4K / Best)")
    print("  [2] Audio Only (MP3)")
    type_choice = input("Enter choice (1 or 2): ").strip()

    if type_choice == "1":
        print("\nSelect Video Resolution:")
        print("  [1] 4K / Best Available (Highest Quality)")
        print("  [2] 1080p (Full HD)")
        print("  [3] 720p (HD)")
        print("  [4] 480p (Standard)")
        quality_choice = input("Enter quality choice (1-4) [Default: 1]: ").strip()

        quality_selectors = {
            "1": "bestvideo+bestaudio/best",
            "2": "bestvideo[height<=1080]+bestaudio/best[height<=1080]",
            "3": "bestvideo[height<=720]+bestaudio/best[height<=720]",
            "4": "bestvideo[height<=480]+bestaudio/best[height<=480]",
        }
        selected_format = quality_selectors.get(quality_choice, quality_selectors["1"])

        ydl_opts = {
            "format": selected_format,
            "outtmpl": "%(title)s.%(ext)s",
            "merge_output_format": "mp4",
        }

    elif type_choice == "2":
        print("\nSelect MP3 Bitrate:")
        print("  [1] 320 kbps (High)")
        print("  [2] 192 kbps (Medium)")
        print("  [3] 128 kbps (Low)")
        bitrate_choice = input("Enter choice (1-3) [Default: 1]: ").strip()

        bitrate_map = {"1": "320", "2": "192", "3": "128"}
        selected_bitrate = bitrate_map.get(bitrate_choice, "320")

        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": "%(title)s.%(ext)s",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": selected_bitrate,
                }
            ],
        }

    else:
        print("[!] Invalid option selected. Exiting.")
        sys.exit(1)

    try:
        print("\n[+] Fetching video information and downloading...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\n[✓] Download and processing completed successfully!")
    except yt_dlp.utils.DownloadError as err:
        print(f"\n[!] Download failed: {err}")
    except KeyboardInterrupt:
        print("\n[!] Download canceled by user.")

if __name__ == "__main__":
    main()

