from pytube import YouTube


def on_download_progress(stream, chunk, bytes_remaining):
    bytes_download = stream.filesize - bytes_remaining
    percent = bytes_download * 100 / stream.filesize
    print(f"Progression du téléchargement : {int(percent)}%")


def get_video_url_from_user():
    BASE_YOUTUBE = "https://www.youtube.com/"
    while True:
        url = input("Donnez l'url de votre video : ")
        if url.lower().startswith(BASE_YOUTUBE):
            break
        print("ERREUR: Veillez entrer l'adresse d'une video de Youtube !")
    return url


def get_video_stream_itag_from_user(streams):
    index = 1
    for stream in streams:
        print(f"{index} - {stream.resolution}")
        index += 1

    while True:
        choice = input("Choisissez la résolution : ")
        if choice == "":
            print("ERREUR: Vous devez rentrer un nombre.")
        else:
            try:
                choice_int = int(choice)
            except:
                print("ERREUR: Vous devez rentrer un nombre")
            else:
                if not 1 <= choice_int <= 2:
                    print(f"Veillez faire un choix entre 1 et {len(streams)}")
                else:
                    break

    itag = streams[choice_int-1].itag
    return itag

# Récupérer le lien de téléchargement
url = r"https://www.youtube.com/watch?v=BhZXw32pNVQ&ab_channel=L%E2%80%99OiseauRare8G"
# url = get_video_url_from_user()

youtube_video = YouTube(url)

youtube_video.register_on_progress_callback(on_download_progress)

print(f"TITRE : {youtube_video.title}")
print(f"NB VUES : {youtube_video.views}")

print("")
print("CHOIX DES RESOLUTIONS")
streams = youtube_video.streams.filter(progressive=True, file_extension='mp4')

itag = get_video_stream_itag_from_user(streams)

stream = youtube_video.streams.get_by_itag(itag)
print("Téléchargement...")
stream.download()
print("OK")

"""
stream = youtube_video.streams.get_highest_resolution()
print("Téléchargement...")
stream.download()
print("OK")
"""


