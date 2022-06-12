'''
Autor: Zel
Email: 2995441811@qq.com
Date: 2022-06-10 17:56:05
LastEditors: Zel
LastEditTime: 2022-06-10 17:57:09
'''
import tkinter as tk
from frontend import App, app_name

def main():
    root = tk.Tk()
    root.title(app_name)   
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
    main()
