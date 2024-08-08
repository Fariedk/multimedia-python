from moviepy.editor import vfx
from pemotongan import short_video


reversed_video = short_video.fx(vfx.time_mirror)  # Membalikkan video
reversed_video.write_videofile('reversed_result.mp4')