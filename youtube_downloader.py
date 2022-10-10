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
    print("Téléchargement...")
    stream_video.download()
    stream_audio.download()
    print("OK")


def download_audio(url):
    youtube_video = YouTube(url)
    youtube_video.register_on_progress_callback(on_download_progress)
    streams = youtube_video.streams.filter(progressive=False, file_extension='mp4', type="audio").order_by('abr').desc()
    stream_audio = streams[0]
    print("Téléchargement...")
    stream_audio.download()
    print("OK")
   

if __name__ == "__main__":

    check_url("https://www.yutube.com/watch?v=BhZXw32pNVQ&ab_channel=L%E2%80%99OiseauRare8G")
    
    """
    # Récupérer le lien de téléchargement
    url = r"https://www.youtube.com/watch?v=BhZXw32pNVQ&ab_channel=L%E2%80%99OiseauRare8G"
    # url = get_video_url_from_user()

    

    

    print(f"TITRE : {youtube_video.title}")
    print(f"NB VUES : {youtube_video.views}")

    print("")
    print("CHOIX DES RESOLUTIONS")
    

    

    print(f"STREAM Video: {stream_video}")
    print(f"STREAM Audio: {stream_audio}")

    # itag = get_video_stream_itag_from_user(streams)

    # stream = youtube_video.streams.get_by_itag(itag)
    
    """


