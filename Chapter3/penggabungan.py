from moviepy.editor import concatenate_videoclips
from pemotongan import short_video

video = VideoFileClip('result.mp4')

combined_video = concatenate_videoclips([video, short_video])
combined_video.write_videofile('combined_result.mp4')