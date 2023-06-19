import os # Check dir_path and create a "Videos" folder.
from pytube import YouTube # Importa la classe "YouTube" dal modulo "pytube"
from moviepy.video.io.VideoFileClip import VideoFileClip # Importa la classe "VideoFileClip" dal modulo "moviepy.video.io.VideoFileClip"
import Python_image_rc
import instaloader as inst

dir_path = os.path.dirname(os.path.abspath(__file__))

# Imposta la directory di lavoro corrente sulla directory che contiene lo script principale
os.chdir(dir_path)

# Crea la cartella per salvare il film.
path = os.getcwd() + '//Videos//'
if not os.path.exists(path):
        os.makedirs(path)
        

def convert_time_to_seconds(min, sec): # FUNZIONE DEPRECATA
        # Converte il tempo da minuti e secondi a secondi
        correct_rime = min*60 + sec
        return correct_rime

def check_path_exist(path):
        if os.path.exists(path):
                print(f"{path} already exists.")
                return True

def segment_video(video_path, start_time, end_time, mp4_name):
        video = VideoFileClip(video_path)
        if start_time < end_time:
                # Estrae il segmento di video specificato
                segmento = video.subclip(start_time, end_time)

                # Salva il segmento di video
                segment_path = f"{os.getcwd()}//Videos//segment_{mp4_name}"
                if check_path_exist(segment_path):
                        return
                segmento.write_videofile(segment_path, codec="libx264")
      
def download(url, start_time, end_time, filename, format = 'mp4'):

        print('start:', start_time, 'end:', end_time)
        
        # Crea un oggetto YouTube usando l'URL fornito
        yt = YouTube(url)

        # Scarica il video con la qualità progressiva e l'estensione mp4
        video_path = yt.streams.filter(progressive=True, file_extension=format).order_by('resolution').desc().first().download()

        # Rinomina il file video scaricato
        mp4_name = f"Video_{filename}.mp4"
        mp4_dir = f"{os.getcwd()}//Videos//"
        if check_path_exist(mp4_dir + mp4_name):
                return
        os.rename(video_path, mp4_dir + mp4_name)
        
        # Carica il video utilizzando la classe VideoFileClip
        video = VideoFileClip(mp4_dir + mp4_name)
        
        # Segmenta il video quando si è verificato che start_time < end_time
        segment_video(video, start_time, end_time, mp4_name)
        
# download(
#     'https://www.youtube.com/watch?v=pj7rCxAsjL0',
#     convert_time_to_seconds(22, 1), 
#     convert_time_to_seconds(27, 29),
#     'Rand_sentimento'
#     #format = 'mp3'

# )


segment_video('D:\WORKSPACE\Download_Video\Videos//Video_Rand_sentimento.mp4',
    convert_time_to_seconds(22, 1), 
    convert_time_to_seconds(27, 29),
    'salvar_capitalismo.mp4')

