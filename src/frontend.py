'''
Autor: Zel
Email: 2995441811@qq.com
Date: 2022-05-29 17:51:22
LastEditors: Zel
LastEditTime: 2022-06-08 16:55:58
'''
import backend as bk
import tkinter as tk
from PIL import ImageTk, Image
import time

from utils import ADMIN, FAIL_CODE, STUDENT, SUCCESS_CODE

from modules import Court, Equipment, Rental, Reservation, User, Admin, Student, Teacher

main_bg_path = r'figures/main_bgr.gif'
rsv_bt_img_path = r'figures/court.gif'
rt_bt_img_path = r'figures/ball.gif'
user_bt_img_path = r'figures/account.gif'
app_name = "T大体育设施管理系统"
bg_w, bg_h = (685, 386)

class App(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.main_bg_img = Image.open(main_bg_path)
        self.main_bg = ImageTk.PhotoImage(image=self.main_bg_img) #不加self无法显示图片
        self.backgroud = tk.Canvas(self, width=bg_w, height=bg_h)
        self.backgroud.create_image(bg_w/2, bg_h/2, image=self.main_bg)
        self.backgroud.pack()

        self.login_bt = tk.Button(self, text='登录', command=self.login)
        self.login_bt.place(x=bg_w/2-100, y=bg_h/2-50, width=200, height=30)
        
        self.about_bt = tk.Button(self, text='关于', command=self.show_about)
        self.about_bt.place(x=bg_w/2-100, y=bg_h/2, width=200, height=30)
    
    def show_about(self):
        self.windows_about = tk.Tk()
        self.windows_about.title('关于本应用')
        about = """
        作者：Zel\n
        邮箱：2995441811@qq.com\n
        """
        self.about_text = tk.Label(self.windows_about, text=about)
        self.about_text.pack(side=tk.LEFT)
        self.windows_about.mainloop()
        pass
    
    def enter(self):
        no = self.entry_no.get()
        passwd = self.entry_pswd.get()
        
        check = bk.login(no, passwd)
        
        if check['ret'] == FAIL_CODE:
            self.entry_hint['text'] = check['err_msg']
            return
        
        self.entry_hint['text'] = '登录成功!'
        self.user = check['user']
        print(self.user)
        time.sleep(1.0)
        self.window_login.destroy()
        
        # 清除组件
        self.login_bt.place_forget()
        print('已经隐藏')
        self.about_bt.place_forget()
        
        return self.user_homepage()
                 
        
    def login(self):
        
        self.window_login = tk.Tk()
        self.window_login.title('登录')
        
        self.frame_no = tk.Frame(self.window_login)
        tk.Label(self.frame_no, text=' 账号 ').pack(side=tk.LEFT)
        self.entry_no = tk.Entry(self.frame_no, width=30)
        self.entry_no.pack(side=tk.LEFT)
        self.frame_no.pack()
        
        self.frame_pswd = tk.Frame(self.window_login)
        tk.Label(self.frame_pswd, text=' 密码 ').pack(side=tk.LEFT)
        self.entry_pswd = tk.Entry(self.frame_pswd, width=30)
        self.entry_pswd['show'] = '*'
        self.entry_pswd.pack(side=tk.LEFT)
        self.frame_pswd.pack()
        
        self.frame_hint = tk.Frame(self.window_login)
        self.entry_hint = tk.Label(self.frame_hint, text="")
        self.entry_hint.pack()
        self.frame_hint.pack()
        
        frame_cf_bt = tk.Frame(self.window_login)
        tk.Button(frame_cf_bt, text=u'登录', command=self.enter).pack()
        frame_cf_bt.pack()
        
        self.window_login.mainloop()
        
        pass
    
    def user_homepage(self):
        
        self.rsv_bt_img = ImageTk.PhotoImage(image=Image.open(rsv_bt_img_path))
        self.rt_bt_img = ImageTk.PhotoImage(image=Image.open(rt_bt_img_path))
        self.user_bt_img = ImageTk.PhotoImage(image=Image.open(user_bt_img_path))
        
        self.rsv_bt = tk.Button(self, text='场地预约', font=('Arial', 20), fg = 'black', image=self.rsv_bt_img, compound=tk.CENTER)
        self.rsv_bt.place(x=bg_w/2-250, y=bg_h/2-50, width=150, height=150)
        
        self.rt_bt = tk.Button(self, text='器材租借', font=('Arial', 20), fg = 'black', image=self.rt_bt_img, compound=tk.CENTER)
        self.rt_bt.place(x=bg_w/2-75, y=bg_h/2-50, width=150, height=150)
        
        self.user_bt = tk.Button(self, text='个人信息', font=('Arial', 20), fg = 'white', image=self.user_bt_img, compound=tk.CENTER)
        self.user_bt.place(x=bg_w/2+100, y=bg_h/2-50, width=150, height=150)
        
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
    root.title(app_name)   
    app = App(root)
    root.mainloop()
    # test()
    pass

