from moviepy.editor import vfx
from pemotongan import short_video

speed_up_video = short_video.fx(vfx.speedx, 2)  # Mempercepat video 2x
speed_up_video.write_videofile('speed_up_result.mp4')