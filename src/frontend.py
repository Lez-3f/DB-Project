'''
Autor: Zel
Email: 2995441811@qq.com
Date: 2022-05-29 17:51:22
LastEditors: Zel
LastEditTime: 2022-06-08 21:10:34
'''
import backend as bk
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import LEFT, ttk

import time

from utils import ADMIN, FAIL_CODE, STUDENT, SUCCESS_CODE

from modules import Court, Equipment, Rental, Reservation, User, Admin, Student, Teacher

TEST:bool = True

main_bg_path = r'figures/main_bgr.gif'
rsv_bt_img_path = r'figures/basket.gif'
rt_bt_img_path = r'figures/ball.gif'
user_bt_img_path = r'figures/account.gif'
app_name = "T大体育设施管理系统"
bg_w, bg_h = (685, 386)

class ToolTip(object):
    
    # this class is copied from https://www.coder.work/article/363943

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                      background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

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
        
        if TEST:
            self.test_bt = tk.Button(self, text='测试', command=self.test)
            self.test_bt.place(x=bg_w/2-100, y=bg_h/2+50, width=200, height=30)
        
        self.quit_bt = tk.Button(self, text='退出', command=self.quit)
        self.quit_bt.place(x = bg_w/2 + 250, y=bg_h/2 + 150, width=50, height=20)
    
    def test(self):
        return self.view_info(['eno', 'ename', 'ebrand', 'enum_a'], ['编号','器材','品牌', '可用数量'], bk.get_eqs_info(), '器材信息表')
    
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
        
        self.rsv_bt = tk.Button(self, image=self.rsv_bt_img, compound=tk.CENTER,\
            command=self.reservation_page)
        self.rsv_bt.place(x=bg_w/2-200, y=bg_h/2-50, width=100, height=100)
        CreateToolTip(self.rsv_bt, text = '场地预约')
        
        self.rt_bt = tk.Button(self, image=self.rt_bt_img, compound=tk.CENTER,\
            )
        self.rt_bt.place(x=bg_w/2-50, y=bg_h/2-50, width=100, height=100)
        CreateToolTip(self.rt_bt, text = '器材租借')
        
        self.user_bt = tk.Button(self, image=self.user_bt_img, compound=tk.CENTER,\
            )
        self.user_bt.place(x=bg_w/2+100, y=bg_h/2-50, width=100, height=100)
        CreateToolTip(self.user_bt, text = '个人信息')
        
        pass
    
    def reservation_page(self):
        
        print('预约页面')
        pass
    
    def rental_page(self):
        pass
    
    def user_page(self):
        pass
    
    ## reservation 
    def view_court_info(self):
        pass
    
    def manage_court_info(self):
        pass

    def check_reservation(self):
        pass
    
    def view_info(self, cols_model, cols_print, module_list, window_name):
        
        col_num = len(cols_model)
        row_num = len(module_list)
        
        view_window = tk.Tk()
        view_window.title(window_name)
        
        frame_search = tk.Frame(view_window)
        search_col = 0
        def choose(*args):
            search_col = cols_model[cols_print.index(comboxlist.get())]
        print(search_col)
            
        comvalue=tk.StringVar() #窗体自带的文本，新建一个值
        comboxlist=ttk.Combobox(frame_search, textvariable=comvalue)
        comboxlist["values"]=cols_print
        comboxlist.current(0)   #选择第一个
        comboxlist.bind("<<ComboboxSelected>>", func=choose)
        comboxlist.pack(side=tk.LEFT)

        
        entry_in = tk.Entry(frame_search, width=10)
        entry_in.pack(side=tk.LEFT)
        
        # 用下滑栏搜索
        def show_table_sel():
            info = entry_in.get()
            # 清空数据
            data = table
            if not info:
                return
                
            else:
                module_list_sel = []
                for md in module_list:
                    if info not in str(getattr(md, search_col)):
                        module_list_sel.append(md)
                        table.delete('', values=[getattr(md, col, None) for col in cols_model])
                        
        bt_search = tk.Button(frame_search, text="查询", width=10, command=show_table_sel)
        bt_search.pack(side=tk.LEFT)
        
        frame_search.pack()
            
        frame_table = tk.Frame(view_window)
        table = ttk.Treeview(frame_table, height=10, columns=cols_model, show='headings')
        
        for j in range(col_num):
            table.column(str(cols_model[j]), width=100, anchor='center')
            table.heading(cols_model[j], text=cols_print[j])

        for i in range(row_num):
            table.insert('', i, values=[getattr(module_list[i], col, None) for col in cols_model])

        def on_click(event):
            item = table.selection()[0]
            print(table.item(item, "value"))
            
        table.bind('<Double-1>', on_click)
        table.pack()
        frame_table.pack()

        vbar = ttk.Scrollbar(frame_table, orient=tk.VERTICAL, command=table.yview)
        table.configure(yscrollcommand=vbar.set)
        
        pass
    
    ## rental
    
    ## user
    
    
     
    

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
    
def main():
    root = tk.Tk()
    root.title(app_name)   
    app = App(root)
    root.mainloop()
    

if __name__ == '__main__':
    main()
    pass

