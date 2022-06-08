'''
Autor: Zel
Email: 2995441811@qq.com
Date: 2022-05-29 17:51:22
LastEditors: Zel
LastEditTime: 2022-06-07 22:45:46
'''
from email.mime import image
import backend
import tkinter as tk
from PIL import ImageTk, Image
#背景
# canvas = tk.Canvas(root, width=1200, height=900, bd=0, highlightthickness=0)
main_bg_path = r'figures/main_bgr.gif'
app_name = "T大体育公园信息管理系统"
bg_w, bg_h = (685, 386)
# bg_w, bg_h = (1200, 600)

class App(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.main_bg_img = Image.open(main_bg_path)
        self.main_bg = ImageTk.PhotoImage(image=self.main_bg_img) 
        print(self.main_bg_img)#不加self无法显示图片
        self.backgroud = tk.Canvas(self, width=bg_w, height=bg_h)
        self.backgroud.create_image(bg_w/2, bg_h/2, image=self.main_bg)
        self.backgroud.pack()

        self.login_bt = tk.Button(self, text='登录', command=self.login)
        self.login_bt.place(x=bg_w/2-100, y=bg_h/2-50, width=200, height=30)
        
    def login(self):
        login_window = tk.Tk()
        login_window.title('登录')
        login_window.mainloop()
        
        
        pass

def run_app():
    root = tk.Tk()
    root.title(app_name)   
    app = App(root)
    root.mainloop()
    
# def test():
#     root = tk.Tk()
#     root.title("T大体育公园信息管理系统")   
#     canvas = tk.Canvas(root, width=1200,height=699,bd=0, highlightthickness=0)
#     imgpath = main_bg_path
#     img = Image.open(imgpath)
#     photo = ImageTk.PhotoImage(img)
    
#     canvas.create_image(700, 500, image=photo)
#     canvas.pack()
#     root.mainloop()
    


if __name__ == '__main__':
    # run_app()
    root = tk.Tk()
    root.title("T大体育公园信息管理系统")   
    app = App(root)
    root.mainloop()
    # test()
    pass

