from moviepy.editor import VideoFileClip

# Memuat file video
video = VideoFileClip('phantom.mp4')

# Menyimpan file video
video.write_videofile('result.mp4')