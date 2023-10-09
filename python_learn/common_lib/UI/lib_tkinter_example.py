# 引入 tkinter 模組
import tkinter as tk
import tkinter.messagebox # 還不能用 tk.messagebox

# <視窗設定> ######################################
# 建立主視窗 Frame
window = tk.Tk()
# 設定視窗標題
window.title('Hello World')
# 設定視窗大小為 300x100，視窗（左上角）在螢幕上的座標位置為 (250, 150)
window.geometry("300x100+250+150")

# <標示文字> ######################################
show_txt = tk.Label(window,                 # 文字標示所在視窗
                 text = 'Hello, world',  # 顯示文字
                 bg = '#EEBB00',         #  背景顏色
                 font = ('Arial', 12),   # 字型與大小
                 width = 15, height = 2  # 文字標示尺寸   
                )
show_txt.pack()

# <輸入欄位> ######################################
entry = tk.Entry(window,     # 輸入欄位所在視窗
                 width = 20) # 輸入欄位的寬度
entry.pack()
# 取得輸入文字
# print(entry.get())

# <按鈕> ######################################
def hello():
    print("Hello, world.", entry.get())
# 建立按鈕
button = tk.Button(window,          # 按鈕所在視窗
                   text = 'Hello',  # 顯示文字
                   command = hello) # 按下按鈕所執行的函數
# 以預設方式排版按鈕
button.pack()

# <跳出視窗> ######################################
# tkinter.messagebox.showinfo(title = 'Hello', # 視窗標題
#                             message = 'pop')   # 訊息內容

# <執行主程式>
window.mainloop()