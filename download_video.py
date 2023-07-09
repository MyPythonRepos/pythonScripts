from pytube import YouTube
import os
  
def Download(link, save_path):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        if not save_path:
            save_path = os.path.dirname(os.path.abspath(__file__))
        youtubeObject.download(save_path)        
    except:
        print("An error has occurred")
        exit(1)
    print("Download is completed successfully")


link = input("Indica la URL del video de Youtube: ")
save_path = input("Indica la ruta donde guardar el video: ")

Download(link, save_path)