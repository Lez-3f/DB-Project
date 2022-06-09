# from email.mime import image
# import backend
# import tkinter as tk
# from PIL import ImageTk, Image
# #背景
# # canvas = tk.Canvas(root, width=1200, height=900, bd=0, highlightthickness=0)
# main_bg_path = r'figures/main_bg.gif'
# app_name = "T大体育公园信息管理系统"
# class App(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master, width=400, height=300)
#         self.pack()
#         self.pilImage = Image.open(main_bg_path)
#         self.tkImage = ImageTk.PhotoImage(image=self.pilImage)
#         self.label = tk.Label(self, image=self.tkImage)
#         self.label.pack()

#     def processEvent(self, event):
#         pass

# if __name__ == '__main__':
#     root = tk.Tk()
#     app = App(root)
#     root.mainloop()
def main2():
  # 1.tab2窗口中划分2个子窗口
    monty2 = ttk.LabelFrame(tab2, text='控件示范区2')
    monty2.grid(column=0, row=0, sticky='W',padx=8, pady=4)
    monty2_1 = ttk.LabelFrame(tab2, text='控件示范区2')
    monty2_1.grid(column=0, row=1,sticky='W', padx=4, pady=4)
  # 2. 设置查询结果显示的子窗口 
    tree=ttk.Treeview(monty2_1)#表格
    tree["columns"]=("站点名称(局向)","告警对象名称","告警对象类型","告警对象ID","告警码",\
        "告警编号","发生时间","告警恢复时间")
    tree.column("站点名称(局向)",width=50)   #表示列,不显示
    tree.column("告警对象名称",width=50)
    tree.column("告警对象类型",width=50)
    tree.column("告警对象ID",width=50)   #表示列,不显示
    tree.column("告警码",width=50)
    tree.column("告警编号",width=50)   #表示列,不显示
    tree.column("发生时间",width=50)
    tree.column("告警恢复时间",width=50)
 
    tree.heading("站点名称(局向)",text="站点名称(局向)")  #显示表头
    tree.heading("告警对象名称",text="告警对象名称")
    tree.heading("告警对象类型",text="告警对象类型")
    tree.heading("告警对象ID",text="告警对象ID")  #显示表头
    tree.heading("告警码",text="告警码")
    tree.heading("告警编号",text="告警编号")  #显示表头
    tree.heading("发生时间",text="发生时间")
    tree.heading("告警恢复时间",text="告警恢复时间")
 
    tree.grid(column=0,row=1,sticky='NSEW')
  # 3.设置查询条件的子窗口
    input_name1 = ttk.Label(monty2, text = '站点名称(局向):').grid(column=0, row=0, sticky='W',pady=5)
    label1 = tkinter.StringVar()
    entry1 = tkinter.Entry(monty2,bg='#ffffff',width=20,textvariable=label1).grid(column=1, row=0, sticky='W')
    
    input_name2 = ttk.Label(monty2, text = '告警对象名称').grid(column=3, row=0, sticky='W')
    label2 = tkinter.StringVar()
    entry2 = tkinter.Entry(monty2,bg='#ffffff',width=20,textvariable=label2).grid(column=4, row=0, sticky='W')
                          
    input_name3 = ttk.Label(monty2, text = '告警对象类型:').grid(column=0, row=1, sticky='W',pady=5)
    label3 = tkinter.StringVar()
    entry3 = tkinter.Entry(monty2,bg='#ffffff',width=20,textvariable=label3).grid(column=1, row=1, sticky='W')
    
    input_name4 = ttk.Label(monty2, text = '告警对象ID').grid(column=3, row=1, sticky='W')
    label4 = tkinter.StringVar()
    entry4 = tkinter.Entry(monty2,bg='#ffffff',width=20,textvariable=label4).grid(column=4, row=1, sticky='W')
    
    input_name5 = ttk.Label(monty2, text = '告警码:').grid(column=0, row=2, sticky='W',pady=5)
    label5 = tkinter.StringVar()
    entry5 = tkinter.Entry(monty2,bg='#ffffff',width=20,textvariable=label5).grid(column=1, row=2, sticky='W')
                          
    input_name6 = ttk.Label(monty2, text = '发生时间:').grid(column=0, row=3, sticky='W',pady=5)
    label6 = tkinter.StringVar()
    entry6 = tkinter.Entry(monty2,bg='#ffffff',width=20,textvariable=label6).grid(column=1, row=3, sticky='W')
#    entry = tkinter.Entry(monty2,bg='#ffffff',width=20,textvariable=label).grid(column=2, row=3, sticky='W',padx=15)
 
    input_name7 = ttk.Label(monty2, text = '告警恢复时间:').grid(column=0, row=4, sticky='W',pady=5)
    label7 = tkinter.StringVar()
    entry7 = tkinter.Entry(monty2,bg='#ffffff',width=20,textvariable=label7).grid(column=1, row=4, sticky='W')
#    entry = tkinter.Entry(monty2,bg='#ffffff',width=20,textvariable=label).grid(column=2, row=4, sticky='W',padx=15)
  # 4.点击按钮调用查询函数
    select_button = tkinter.Button(monty2,bg='white',text='查询',width=10,height=1,\
       command=lambda :select2(monty2, label1,tree)).grid(column=3, row=4, sticky='W',padx=5)