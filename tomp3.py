import yt_dlp

print("=== YouTube → MP3 Downloader ===")

url = input("Dose to link tou YouTube: ")

options = {
    "format": "bestaudio/best",
    "outtmpl": "%(title)s.%(ext)s",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
}

try:
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])

    print("✅ To MP3 katevike epitixos!")

except Exception as e:
    print("❌ Sfalmα:", e)
