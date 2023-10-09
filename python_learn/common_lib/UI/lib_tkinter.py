# 引入 tkinter 模組
import tkinter as tk
import tkinter.messagebox # 還不能用 tk.messagebox

# << 視窗設定 >> ######################################
# 建立主視窗 Frame
window = tk.Tk()
# 設定視窗標題
window.title('Hello World')
# <視窗大小>
# # 設定視窗大小為 300x100，視窗（左上角）在螢幕上的座標位置為 (250, 150)
# window.geometry("300x100+250+150")
# # 視窗最大化 方法1 (只適用 windows)
window.state("zoomed")
# # 視窗最大化 方法2
# w, h = window.maxsize()
    # 同樣的數值
    # print("window.maxsize()",window.maxsize())
    # print("window.winfo_screenwidth(), ", window.winfo_screenwidth(), window.winfo_screenheight())
# window_place_str = f"{w}x{h}"
# window.geometry(window_place_str)
# print("window_place_str :",window_place_str)
# # 設定成全螢幕
# window.attributes('-fullscreen', True) 

# # << 標示文字 >> ######################################
# font = (字體, 大小, [其他])
    # 字體 : 'Arial','黑體'
    # 其他 : 
        # "bold" : 粗體
        # "italic" : 斜體
        # "underline" : 底線
        # "overstrike" : 刪除縣

show_txt = tk.Label(window,                 # 文字標示所在視窗
                 text = 'Hello, world',  # 顯示文字
                 bg = '#EEBB00',         #  背景顏色
                 font = ('Arial', 12),   # 字型與大小
                 width = 15, height = 2  # 文字標示尺寸   
                )
show_txt.pack() # 以預設方式排版按鈕
# 取得顯示的文字
print("目前顯示的文字 :", show_txt.cget("text"))

# 修改顯示的文字
def change_show_text():
    show_txt.configure(text="change_Label_text")
    print("目前顯示的文字 :", show_txt.cget("text"))
change_Label = tk.Button(window,          # 按鈕所在視窗
                   text = 'change_Label',  # 顯示文字
                   command = lambda : change_show_text()) # 按下按鈕所執行的函數
change_Label.pack() # 以預設方式排版按鈕
# # << 輸入欄位 >> ######################################
entry = tk.Entry(window,     # 輸入欄位所在視窗
                 width = 20) # 輸入欄位的寬度
entry.pack()
# 取得輸入文字
# print(entry.get())

# # << 按鈕 >> ######################################
def hello():
    print("Hello, world.", entry.get())
# 建立按鈕
button = tk.Button(window,          # 按鈕所在視窗
                   text = 'Hello',  # 顯示文字
                   command = hello) # 按下按鈕所執行的函數
# 以預設方式排版按鈕
button.pack()

# # << 排版相關 >> ######################################
test_widget = tk.Label(window,                 # 文字標示所在視窗
    text = 'test_widget',  # 顯示文字
    bg = '#EEBB00',         #  背景顏色
    font = ('Arial', 12),   # 字型與大小
    width = 15, height = 2  # 文字標示尺寸   
)
# # <顯示方法>
# # 1.預設顯示
# test_widget.pack()
# # 2.比例
test_widget.place(relx=0,rely=0.5,relheight=0.4,relwidth=1)

# # <隱藏> 要使用跟顯示方法對應的隱藏function
    # # 如果要再顯示就再呼叫 顯示方法 即可
    # # 如果真的不想要了 可以用 destroy
# # 1. 預設顯示 : pack_forget
# button = tk.Button(window, text = '隱藏/顯示',
#                 command = test_widget.pack_forget)
# # 2. 比例 : pack_forget
button = tk.Button(window, text = '隱藏/顯示',
                command = test_widget.place_forget)
button.pack()

# # << 跳出視窗 >> ######################################
# tkinter.messagebox.showinfo(title = 'Hello', # 視窗標題
#                             message = 'pop')   # 訊息內容

# # << 執行主程式 >>
window.mainloop()