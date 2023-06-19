import youtube_dl
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def download_and_cut_video(start_time, end_time, video_link, video_name):
    # Create options for video download
    options = {
        'format': 'bestvideo+bestaudio',
        'outtmpl': 'path/to/save/video/%(title)s.%(ext)s',
    }

    # Create youtube-dl instance
    ydl = youtube_dl.YoutubeDL(options)

    # Download the video
    ydl.download([video_link])

    # Get the downloaded video filename
    info_dict = ydl.extract_info(video_link, download=False)
    video_filename = ydl.prepare_filename(info_dict)

    # Set the output filename for the cut video
    output_filename = f"{video_name}.mp4"

    # Convert start_time and end_time to float
    start_time = float(start_time)
    end_time = float(end_time)

    # Cut the video using moviepy
    ffmpeg_extract_subclip(video_filename, start_time, end_time, targetname=output_filename)

    print("Video downloaded and cut successfully!")

def convert_time_to_seconds(min, sec): # FUNZIONE DEPRECATA
        # Converte il tempo da minuti e secondi a secondi
        correct_rime = min*60 + sec
        return correct_rime
    
# Example usage
start_time = convert_time_to_seconds(37, 7)  # Start time in seconds
end_time = convert_time_to_seconds(50, 38)  # End time in seconds
video_link = "https://www.youtube.com/watch?v=oInK0VU_O-8"
video_name = "estoicismo"

download_and_cut_video(start_time, end_time, video_link, video_name)
