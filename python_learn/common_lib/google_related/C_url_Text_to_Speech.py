import requests
import os

word = "this is a word"
language = "en"
url = f"http://translate.google.com/translate_tts?client=tw-ob&ie=UTF-8&tl={language}&q={word}"

response = requests.get(url)
print(type(response))
print(type(response.content))
save_path = os.path.dirname(__file__) + r"\C_url_Text_to_Speech_download_test.mp3"
# 儲存成 mp3
open(save_path, "wb").write(response.content)

from pygame import mixer
from pygame import time as pygame_time
import time
from io import BytesIO
mixer.init()
mp3_stream = BytesIO(response.content)
sound = mixer.Sound(mp3_stream)
time.sleep(0.3)
sound.play()
pygame_time.wait(int(sound.get_length() * 1000))