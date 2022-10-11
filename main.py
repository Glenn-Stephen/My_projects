import youtube_downloader

BASE_YOUTUBE = "https://www.youtube.com/"

urls = []
while True:
    url = input("Veillez entrer le lien à télécharger: ")
    if url == "":
        print("Veillez entrer un lien !")
        print()
    elif not url.lower().startswith(BASE_YOUTUBE):
        print("ERREUR: Veillez entrer un lien youtube !")
        print()
    else:
        urls.append(url)
        while True:
            add_url = input("Souhaitez-vous ajouter un autre lien (y/n) ? ")
            if add_url.lower() == "n":
                leave = True
                break
            elif add_url.lower() == "y":
                leave = False
                break
            else:
                print("Veillez répondre par 'y' ou 'n' !")
                print()
        if leave:
            break

while True:
    choice = input("""
    Voulez-vous télécharger en audio ou en vidéo ?
    1 - Audio
    2 - Vidéo

    Votre réponse: """)

    if choice == "1" or choice.lower() == "audio":
        for url in urls:
            youtube_downloader.download_audio(url)
            leave = True
            break
    elif choice == "2" or choice.lower() == "vidéo":
        for url in urls:
            youtube_downloader.download_video(url)
            leave = True
            break
    else:
        print("Veillez faire un choix entre un et deux !")
    if leave:
        break
