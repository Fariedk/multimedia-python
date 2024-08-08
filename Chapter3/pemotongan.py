from moviepy.editor import VideoFileClip

video = VideoFileClip('result.mp4')

short_video = video.subclip(0, 10)  # Mendapatkan 10 detik pertama
short_video.write_videofile('short_result.mp4')