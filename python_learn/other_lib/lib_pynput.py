from pynput import keyboard
# 就算 python 的畫面不是在最上方，也會觸發
# key
    # 如果是特殊按鍵會有 : .name , .value
    # 如果是普通按鍵會有 : .char

# 會觸發很多次(所以 on_release 比較好用)
def on_press(key):
    try:
        print('Alphanumeric key pressed: {0} '.format(
            key.char))
    except AttributeError:
        print('special key pressed: {0}'.format(
            key))

# 只會觸發一次
def on_release(key):
    print('Key released: {0}'.format(
        key))
    print(dir(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# # 開始偵測
# # 方法1
# with keyboard.Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()
# # 方法2
listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
listener.start()
import time
time.sleep(10)
listener.stop()