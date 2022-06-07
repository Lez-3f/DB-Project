'''
Autor: Zel
Email: 2995441811@qq.com
Date: 2022-05-29 17:51:22
LastEditors: Zel
LastEditTime: 2022-06-07 21:20:31
'''
import backend
import tkinter as tk
#背景
# canvas = tk.Canvas(root, width=1200, height=900, bd=0, highlightthickness=0)
main_bg_path = r'figures/main_bg.gif'
app_name = "T大体育公园信息管理系统"

class App(object):
    
    def __init__(self, root):
        main_bg = tk.PhotoImage(file=main_bg_path)
        print(main_bg)
        self.backgroud = tk.Label(root, image=main_bg)
        self.backgroud.pack()
        # self.title = tk.Label(root, text=app_name)
        # self.title.pack()

def run_app():
    root = tk.Tk()
    root.title("T大体育公园信息管理系统")   
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
    run_app()
    pass

