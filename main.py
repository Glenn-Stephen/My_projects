# Projet "Youtube Downloader"

from pytube import YouTube

url = r"https://www.youtube.com/watch?v=9bZkp7q19f0&ab_channel=officialpsy"

def on_download_progress(stream, chunk, bytes_remaining):
    bytes_download = stream.filesize - bytes_remaining
    percent = bytes_download * 100 / stream.filesize
    print(f"Progression du téléchargement : {int(percent)}%")

youtube_video = YouTube(url)

youtube_video.register_on_progress_callback(on_download_progress)

print(f"TITRE : {youtube_video.title}")
print(f"NB VUES : {youtube_video.views}")

# print("STREAMS")
# for stream in youtube_video.streams.fmt_streams:
#     print(f"    {stream}")



stream = youtube_video.streams.get_by_itag(18)
print("Téléchargement...")
stream.download()
print("OK")



