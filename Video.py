import os
os.environ["IMAGEIO_FFMPEG_EXE"] = "C:/Program Files/ImageMagick/magick.exe"

from pytube import YouTube
from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.editor import ImageClip, CompositeVideoClip
from moviepy.video.VideoClip import TextClip
from moviepy.video.fx import resize

# Check dir_path and create a "Videos" folder.
dir_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir_path)
path = os.path.join(dir_path, 'Videos')
os.makedirs(path, exist_ok=True)

def segment_video(video_path, start_time, end_time, mp4_name):
    # Load the video using VideoFileClip
    video = VideoFileClip(video_path)
    # Segment the video based on the specified start and end times
    segment = video.subclip(start_time, end_time)
    # Save the segment to a new file
    segment_path = os.path.join(path, f'segment_{mp4_name}')
    segment.write_videofile(segment_path, codec="libx264")

def download(url, start_time, end_time, filename, format='mp4'):
    print('Start:', start_time, 'End:', end_time)
    # Create a YouTube object using the provided URL
    yt = YouTube(url)
    # Download the video with the progressive quality and the specified format
    video = yt.streams.filter(progressive=True, file_extension=format).order_by('resolution').desc().first()
    video_path = video.download(output_path=path)
    # Rename the downloaded video file
    mp4_name = f"Video_{filename}.mp4"
    mp4_path = os.path.join(path, mp4_name)
    os.rename(video_path, mp4_path)
    # Segment the video when start_time < end_time
    if start_time < end_time:
        segment_video(mp4_path, start_time, end_time, mp4_name)

def resize_video(video_path, width, height):
    # Load the video using VideoFileClip
    video = VideoFileClip(video_path)
    # Resize the video to the specified width and height
    resized_video = resize.resize(video, width=width, height=height)
    # Save the resized video to a new file
    resized_path = os.path.join(path, 'resized_video.mp4')
    resized_video.write_videofile(resized_path, codec="libx264")

def combine_video_with_image(video_path, image_path, text=None):
    video = VideoFileClip(video_path)
    image = ImageClip(image_path, duration=video.duration)
    
    # Add text to the image if provided
    if text is not None:
        txt_clip = TextClip(text, fontsize=30, color='white', font='Arial-Bold')
        txt_clip = txt_clip.set_position(('center', 'top')).set_duration(video.duration)
        final_clip = CompositeVideoClip([video, image.set_opacity(1), txt_clip.set_opacity(1)])
    else:
        final_clip = CompositeVideoClip([video, image.set_opacity(1)])
    
    # Save the final video
    final_clip.write_videofile(os.path.join(path, 'final_video.mp4'), codec="libx264", fps=video.fps)

# Example usage
url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
start_time = 10
end_time = 20
filename = 'my_video'

# print('ok')
# download(url, start_time, end_time, filename)
print('ok resize')
resize_video(os.path.join(path, f'Video_{filename}.mp4'), 640, 480)
print('ok combine')
combine_video_with_image(os.path.join(path, f'Video_{filename}.mp4'), 'Capa_videos.png')
print('ok_all')
