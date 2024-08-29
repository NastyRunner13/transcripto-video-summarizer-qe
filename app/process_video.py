from utils.is_16_9_ratio import is_16_9_ratio
from moviepy.editor import VideoFileClip
from moviepy.video.fx.all import resize, margin
import os

def process_video(video_path, upload_dir):
    video = VideoFileClip(f"file:{video_path}")
    # Resize and add black borders if necessary
    if not is_16_9_ratio(video.size):
        video = resize(video, height=1080)
        video = margin(video, top=(1080 - video.size[1]) // 2, bottom=(1080 - video.size[1]) // 2,
                       left=(1920 - video.size[0]) // 2, right=(1920 - video.size[0]) // 2, color=(0, 0, 0))
    processed_video_path = os.path.join(upload_dir, "processed_video.mp4")
    video.write_videofile(processed_video_path, codec='libx264')
    return processed_video_path