from email.mime import image
import backend
import tkinter as tk
from PIL import ImageTk, Image
#背景
# canvas = tk.Canvas(root, width=1200, height=900, bd=0, highlightthickness=0)
main_bg_path = r'figures/main_bg.gif'
app_name = "T大体育公园信息管理系统"
class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, width=400, height=300)
        self.pack()
        self.pilImage = Image.open(main_bg_path)
        self.tkImage = ImageTk.PhotoImage(image=self.pilImage)
        self.label = tk.Label(self, image=self.tkImage)
        self.label.pack()

    def processEvent(self, event):
        pass

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()