from pygame import mixer 
from pygame import time as pygame_time
import time

import os
mp3_path = os.path.dirname(__file__) + r"\C_url_Text_to_Speech_download_test.mp3"

# # music 
# mixer.init()
# mixer.music.load(mp3_path)
# time.sleep(0.5) # 讀取需要一點時間
# mixer.music.set_volume(1)# 来设置播放的音量，音量value的范围为0.0到1.0。
# mixer.music.play(loops=1,start=0.0)
# time.sleep(2)
# mixer.music.stop()

# print("music play finish")
# time.sleep(1)

# # Sound (讀取mp3檔案)
# mixer.init()
# pronounce = mixer.Sound(mp3_path)
# time.sleep(0.5) # 讀取需要一點時間
# pronounce.play()
# pygame_time.wait(int(pronounce.get_length() * 1000))

# print("Sound play finish")
# time.sleep(1)

# # Sound (直接撥放已讀取的mp3)
# with open(mp3_path, "rb") as fr :
#     mp3_byte = fr.read()
# from io import BytesIO
# mixer.init()
# mp3_stream = BytesIO(mp3_byte)
# sound = mixer.Sound(mp3_stream)
# time.sleep(0.5) # 讀取需要一點時間
# sound.play()
# pygame_time.wait(int(sound.get_length() * 1000))

mixer.quit()