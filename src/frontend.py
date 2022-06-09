'''
Autor: Zel
Email: 2995441811@qq.com
Date: 2022-05-29 17:51:22
LastEditors: Zel
LastEditTime: 2022-06-09 18:25:04
'''
from sqlalchemy import insert, values
import backend as bk
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk

import time
import datetime

from utils import ADMIN, FAIL_CODE, LEGAL_TIME, STUDENT, SUCCESS_CODE

from modules import Court, Equipment, Rental, Reservation, User, Admin, Student, Teacher

import numpy as np

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
        # return self.view_info(tk.Tk(), ['eno', 'ename', 'ebrand', 'enum_a'], ['编号','器材','品牌', '可用数量'], bk.get_eqs_info)
        return self.view_info(tk.Tk() , ['cno', 'cname', 'cinfo', 'ctype'], ['编号','场地名','描述', '类型'], bk.get_court_info)
        
    
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
        self.window_rsv = tk.Tk()
        self.window_rsv.title('场地预约')
        
        self.window_rsv.minsize(700, 500)
        
        self.nb_rsv = ttk.Notebook(self.window_rsv)
        
        self.tab_view_court = tk.Frame(self.nb_rsv)
        self.tab_manage_court = tk.Frame(self.nb_rsv)
        self.tab_approve_rsv = tk.Frame(self.nb_rsv)
        self.tab_make_rsv = tk.Frame(self.nb_rsv)
        self.tab_cancel_rsv = tk.Frame(self.nb_rsv)
        
        self.nb_rsv.add(self.tab_view_court, text='查看场地')
        self.view_info(self.tab_view_court , ['cno', 'cname', 'cinfo', 'ctype'], ['编号','场地名','描述', '类型'], bk.get_court_info)
        if self.user[0] == ADMIN:
            self.nb_rsv.add(self.tab_manage_court, text='管理场地')
            self.manage_info(self.tab_manage_court,  ['cno', 'cname', 'cinfo', 'ctype'], ['编号','场地名','描述','类型'],\
                bk.get_court, bk.set_court, bk.remove_court, bk.add_court)
            
            self.nb_rsv.add(self.tab_approve_rsv, text='审批预约')
        else:
            self.nb_rsv.add(self.tab_make_rsv, text='预约申请')
            self.nb_rsv.add(self.tab_cancel_rsv, text='取消预约')
        
        self.nb_rsv.pack(fill=tk.BOTH, expand=True)
        self.window_rsv.mainloop()
        
        pass
    
    def rental_page(self):
        pass
    
    def user_page(self):
        pass
    
    def manage_info(self, frame, cols_model, cols_print, get_module, set_module, rm_module, add_module):
        # 增删改
        
        frame_mdf = ttk.LabelFrame(frame, text="修改数据")
        frame_mdf.grid(column=0, row=0, sticky='W', padx=8, pady=4)
        
        frame_add = ttk.LabelFrame(frame, text="插入数据")
        frame_add.grid(column=0, row=1, sticky='W', padx=8, pady=4)
        
        frame_rm = ttk.LabelFrame(frame, text="删除数据")
        frame_rm.grid(column=0, row=2, sticky='W', padx=8, pady=4)
        
        frame_table = ttk.LabelFrame(frame, text='数据信息')
        frame_table.grid(column=0, row=3, sticky='W', padx=8, pady=4)
        
        def show_module(no):
            
            if not no:
                return 
            md = get_module(no)
            
            for widget in frame_table.winfo_children():
                widget.destroy()
            table = ttk.Treeview(frame_table, height=10, columns=cols_model, show='headings')
            col_num = len(cols_model)
        
            for j in range(col_num):
                table.column(str(cols_model[j]), width=150, anchor='center')
                table.heading(cols_model[j], text=cols_print[j])
            
            if not md:
                return
            table.insert('', 0, values=[getattr(md, col, None) for col in cols_model])
            
            def on_click(event):
                item = table.selection()[0]
                # print(table.item(item, "value"))
                
            table.bind('<ButtonRelease-1>', on_click)

            vbar = ttk.Scrollbar(frame_table, orient=tk.VERTICAL, command=table.yview)
            table.configure(yscrollcommand=vbar.set)    
            table.pack()
            pass
        
        # 修改
        tk.Label(frame_mdf, text=" 修改编号 ").grid(row=0, column=0)
        
        mdf_ent_no = tk.Entry(frame_mdf, width=10)
        mdf_ent_no.grid(row=0, column=1)
        
        mdf_bt_ck = tk.Button(frame_mdf, text='查看', width=10,\
                            command=lambda: show_module(mdf_ent_no.get()))
        mdf_bt_ck.grid(row=0, column=2)
        
        tk.Label(frame_mdf, text=" 修改属性 ").grid(row=0, column=3)
        
        mdf_cbl = ttk.Combobox(frame_mdf, textvariable=tk.StringVar(), width=10)
        mdf_cbl['values'] = cols_print[1:]
        mdf_cbl.current(0)   #选择第一个
        mdf_cbl.bind("<<ComboboxSelected>>")
        mdf_cbl.grid(row=0, column=4)
        
        tk.Label(frame_mdf, text=" 修改值 ").grid(row=0, column=5)
        
        mdf_ent_val = tk.Entry(frame_mdf, width=10)
        mdf_ent_val.grid(row=0, column=6)
        
        mdf_bt_cf = tk.Button(frame_mdf, text='确认修改', width=10,\
                    command=lambda: (
                        set_module(mdf_ent_no.get(), cols_model[cols_print.index(mdf_cbl.get())], mdf_ent_val.get()),\
                        show_module(mdf_ent_no.get())
                        )
        )
        mdf_bt_cf.grid(row=1, column=0, columnspan=7)
        
        # 删除
        tk.Label(frame_rm, text=" 删除编号 ").grid(row=0, column=0)
        rm_ent_no = tk.Entry(frame_rm, width=10)
        rm_ent_no.grid(row=0, column=1)
     
        rm_bt_ck = tk.Button(frame_rm, text='查看', width=10,\
                            command=lambda: show_module(rm_ent_no.get()))
        rm_bt_ck.grid(row=0, column=2)
        
        rm_bt_cf = tk.Button(frame_rm, text='确认删除', width=10,\
                    command=lambda: (
                        rm_module(rm_ent_no.get()),\
                        show_module(rm_ent_no.get())
                        )
        )
        rm_bt_cf.grid(row=1, column=0, columnspan=7)
        
        # 插入
        tk.Label(frame_add, text=" 选择属性 ").grid(row=0, column=0)
        
        add_cbl = ttk.Combobox(frame_add, textvariable=tk.StringVar(), width=10)
        add_cbl['values'] = cols_print
        add_cbl.current(0)   #选择第一个
        add_cbl.bind("<<ComboboxSelected>>")
        add_cbl.grid(row=0, column=1)
        
        tk.Label(frame_add, text=" 属性值 ").grid(row=0, column=2)
        
        add_val = {}
        for col in cols_model:
            add_val[col] = None
        add_val_print = {}
        for col in cols_print:
            add_val_print[col] = None
        
        def add_val_update():
            col_print = add_cbl.get()
            col_module = cols_model[cols_print.index(col_print)]
            add_val[col_module] = add_ent_val.get()
            add_val_print[col_print] = add_ent_val.get()
            add_val_ck.config(text=my_dict2str(add_val_print))
            pass
        
        def my_dict2str(d:dict):
            s = '['
            for key in d.keys():
                s += (str(key) + ': ' + str(d[key]) + ' ')
            return s + ']'
        
        def insert():
            cnt = 0
            for k in add_val.keys():
                if add_val[k] != None:
                    cnt = cnt + 1
            if cnt == len(cols_model):
                rtn = add_module(**add_val)
                if rtn['ret'] == SUCCESS_CODE:
                    add_val_ck.config(text=my_dict2str(add_val_print)+'，插入成功！')
                else:
                    add_val_ck.config(text=my_dict2str(add_val_print)+'，插入失败！')
                    
            pass
        
        add_ent_val = tk.Entry(frame_add, width=10)
        add_ent_val.grid(row=0, column=3)
        
        add_bt_upd = tk.Button(frame_add, text='添加', width=10,\
                        command=add_val_update)
        add_bt_upd.grid(row=0, column=4)

        tk.Label(frame_add, text='待插入的数据').grid(row=1, column=0)
        add_val_ck = tk.Label(frame_add, text=my_dict2str(add_val_print))
        add_val_ck.grid(row=1, column=1, columnspan=6)
        
        add_bt_cf = tk.Button(frame_add, text='确认插入', width=10,\
                    command=insert)
        add_bt_cf.grid(row=2, column=0, columnspan=7)
    
    def view_info(self, frame, cols_model, cols_print, get_module_list):
        
        frame_search = ttk.LabelFrame(frame, text="查询框")
        frame_search.grid(column=0, row=0, sticky='W', padx=8, pady=4)
        frame_table  =ttk.LabelFrame(frame, text='查询结果')
        frame_table.grid(column=0, row=1, sticky='W', padx=8, pady=4)
       
        #### table ####
        
        def show_table_sel():
            for widget in frame_table.winfo_children():
                widget.destroy()
            table = ttk.Treeview(frame_table, height=10, columns=cols_model, show='headings')
            col_num = len(cols_model)
        
            for j in range(col_num):
                table.column(str(cols_model[j]), width=150, anchor='center')
                table.heading(cols_model[j], text=cols_print[j])
            
            search_col = cols_model[cols_print.index(cbl.get())]
            # print(search_col)
            info = entry_in.get()
            # print(info)
            
            module_list = get_module_list()
            
            # 无搜索信息，插入所有数据
            if not info:
                row_num = len(module_list)

                for i in range(row_num):
                    table.insert('', i, values=[getattr(module_list[i], col, None) for col in cols_model])
                
            # 插入符合条件的数据   
            else:
                i = 0
                for md in module_list:
                    if str(info) in str(getattr(md, search_col)):
                        # print('find')
                        table.insert('', i, values=[getattr(md, col, None) for col in cols_model])
                        i = i + 1
                print(len(table.get_children()))
            
            def on_click(event):
                item = table.selection()[0]
                print(table.item(item, "value"))
                
            table.bind('<ButtonRelease-1>', on_click)

            vbar = ttk.Scrollbar(frame_table, orient=tk.VERTICAL, command=table.yview)
            table.configure(yscrollcommand=vbar.set)
            
            table.pack()
            # vbar.pack(side=tk.LEFT)
            
            if TEST or frame == self.tab_view_court :
                def show_rsv():
                    ttb = {}
                    cno = table.item( table.selection()[0])['values'][0]
                    print('cno' + str(cno))
                    ct_rsv = bk.get_court_rsv_pass(cno)
                    
                    seven_day = [(datetime.datetime.today() + datetime.timedelta(i)).date() for i in range(7)]
                    time_rg = LEGAL_TIME[1] - LEGAL_TIME[0] + 1
                    for day in seven_day:
                        ttb[day] = [0 for i in range(time_rg+1)]
                    for day in seven_day:
                        print(len(ttb[day]))
                    
                    for rsv in ct_rsv:
                        rsv:Reservation
                        date = rsv.rbegin.date()
                        # print(date)
                        begin, end = rsv.rbegin.hour, rsv.rend.hour
                        for i in range(end-begin):
                            if rsv.rguest == self.user[1].uno:
                                ttb[date][i+begin-LEGAL_TIME[0]] = 2
                            else: 
                                ttb[date][i+begin-LEGAL_TIME[0]] = 1

                    # print(ttb)
                    wd_ttb = tk.Tk()
                    
                    tk.Label(wd_ttb, text='', width=10).grid(row=0, column=0)
                    for i in range(7):
                        date = seven_day[i]
                        tk.Label(wd_ttb, text=str(date), width=10).grid(row=0, column=i+1)
                        
                    for j in range(time_rg):
                        time_str = f'{LEGAL_TIME[0]+j}:00-{LEGAL_TIME[0]+j+1}:00'
                        tk.Label(wd_ttb, text=time_str, width=10).grid(row=j+1, column=0)
                        for k in range(7):
                            date = seven_day[k]
                            if(j >= len(ttb[date])):
                                print(f'{j}  {date} {len(ttb[date])}')
                            if ttb[date][j] == 1: color = 'red'
                            elif ttb[date][j] == 0: color = 'SpringGreen'
                            else: color = 'yellow'
                            tk.Label(wd_ttb, bg=color, width=10).grid(row=j+1, column=k+1)
                            
                    tk.Label(wd_ttb, text='红色表示占用，绿色表示可以预约, 黄色表示本人预约').grid(row=time_rg+1, column=0, columnspan=8)
                    wd_ttb.mainloop()
                
                bt_rsv = tk.Button(frame_table, text='查看预约',command=show_rsv)
                bt_rsv.pack()
        pass  
        
        #### search #####
            
        comvalue=tk.StringVar() #窗体自带的文本，新建一个值
        cbl=ttk.Combobox(frame_search, textvariable=comvalue)
        cbl["values"]=cols_print
        cbl.current(0)   #选择第一个
        cbl.bind("<<ComboboxSelected>>")
        cbl.pack(side=tk.LEFT)
        
        entry_in = tk.Entry(frame_search, width=10)
        entry_in.pack(side=tk.LEFT)     
                        
        bt_search = tk.Button(frame_search, text="查询", width=10, command=lambda: show_table_sel())
        bt_search.pack(side=tk.LEFT)

    

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

