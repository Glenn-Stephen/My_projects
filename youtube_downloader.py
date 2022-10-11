from pytube import YouTube
import ffmpeg
import os


def on_download_progress(stream, chunk, bytes_remaining):
    bytes_download = stream.filesize - bytes_remaining
    percent = bytes_download * 100 / stream.filesize
    print(f"Progression du téléchargement : {int(percent)}%")

    
def download_video(url):
    youtube_video = YouTube(url)

    youtube_video.register_on_progress_callback(on_download_progress)

    streams = youtube_video.streams.filter(progressive=False, file_extension='mp4', type="video").order_by('resolution').desc()
    stream_video = streams[0]
    streams = youtube_video.streams.filter(progressive=False, file_extension='mp4', type="audio").order_by('abr').desc()
    stream_audio = streams[0]

    print(f"Titre: {stream_video.title}")
    print(f"Taille: {stream_video.filesize_mb + stream_audio.filesize_mb}")
    print("Téléchargement...")
    stream_video.download("video")
    stream_audio.download("audio")

    video_filename = os.path.join("video", stream_video.default_filename)
    audio_filename = os.path.join("audio", stream_audio.default_filename)
    output_filename = stream_video.default_filename

    ffmpeg.output(ffmpeg.input(audio_filename), ffmpeg.input(video_filename), output_filename, vcodec="copy", acodec="copy", loglevel="quiet").run(overwrite_output=True)
    print("OK")

    os.remove(audio_filename)
    os.remove(video_filename)
    os.rmdir("audio")
    os.rmdir("video")


def download_audio(url):
    youtube_video = YouTube(url)
    youtube_video.register_on_progress_callback(on_download_progress)
    streams = youtube_video.streams.filter(progressive=False, file_extension='mp4', type="audio").order_by('abr').desc()
    stream_audio = streams[0]
    print(f"Titre: {stream_audio.title}")
    print(f"Taille: {stream_audio.filesize_mb}")
    print("Téléchargement...")
    stream_audio.download()
    print("OK")
   

if __name__ == "__main__":

    download_video("https://www.youtube.com/watch?v=zBjJUV-lzHo&ab_channel=MEMESHUB")
    


