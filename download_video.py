from pytube import YouTube, Playlist
from tqdm import tqdm
import os


def download(link, save_path):
    youtube_object = YouTube(link)
    youtube_object = youtube_object.streams.get_highest_resolution()
    try:
        if not save_path:
            save_path = os.path.dirname(os.path.abspath(__file__))
        for i in tqdm (range (100), desc="Loading..."):
            youtube_object.download(save_path)
    except Exception:
        print(f"An error has occurred: \n{Exception}")
        exit(1)
    print("Download is completed successfully")


def download_playlist(link, save_path):
    pl = Playlist(link)
    for idx, video in enumerate(pl.videos):
        print(f"Descargando: {video.title}")
        video.streams.get_highest_resolution().download(save_path)
        out_file = save_path+"\\"+video.streams.get_highest_resolution().default_filename
        new_file = save_path+"\\"+str(idx)+"_"+video.streams.get_highest_resolution().default_filename
        os.rename(out_file, new_file)


# tipo_descarga = input("¿Tipo de descarga (video/playlist)?")
# link = input("Indica la URL del video de Youtube: ")
# save_path = input("Indica la ruta donde guardar el video: ")

tipo_descarga = "playlist"
link = "https://www.youtube.com/watch?v=PAT_W1F6FzA&list=PLNXwhzx0-DmRlCz9lKPLRWdv5visGlNNT"
save_path = "d:\Bibliotecas\Videos\pruebas"

download(link, save_path) if tipo_descarga == "video" else download_playlist(link, save_path)

