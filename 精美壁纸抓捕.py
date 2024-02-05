import tkinter as tk
from tkinter import ttk
import requests
import re
import time

class Main:
    def __init__(self, master):
        # 初始化界面
        self.master = master
        master.title("壁纸下载器.作者：马梓程")

        # 创建并放置Frame框架


        self.frame1 = tk.Frame(master, padx=10, pady=10)
        self.frame1.pack()

        # 创建标签并放置在Frame框架上
        self.label = tk.Label(self.frame1, text="请选择要下载的类型:")
        self.label.pack(side=tk.LEFT)
        self.label2 = tk.Label(self.frame1, text="马梓程专用！打赏联系马梓程！")
        self.label2.pack(padx=0,pady=5)

        # 创建下拉列表并放置在Frame框架上
        self.combobox = ttk.Combobox(self.frame1, values=["动漫", "风景", "美女", "背景", "游戏"])
        self.combobox.pack(side=tk.LEFT, padx=10)

        # 创建按钮并放置在Frame框架上
        self.button = tk.Button(self.frame1, text="选择", command=self.click_button)
        self.button.pack(side=tk.LEFT, padx=10)

        # 创建退出按钮并放置在主界面上
        self.quit_button = tk.Button(master, text="退出", command=master.quit)
        self.quit_button.pack(pady=10)

    # 处理按钮点击事件
    def click_button(self):
        input1 = self.combobox.get()
        self.get(input1)

    # 请求网址并下载图片
    def get(self, input1):
        self.master.withdraw()
        lin = ''
        classes = [
            ['动漫','dongman','共165页'],
            ['风景','fengjing','共212页'],
            ['美女','meinv','共197页'],
            ['背景','beijing','共87页'],
            ['游戏','youxi','共204页'],
        ]
        for f in classes:
            if input1 in f:
                lin = f[1]
        # 拼接网址并请求
        url = f"https://pic.netbian.com/4k{lin}"
        key = True
        # 循环请求不同的页面
        while key:
            # 输入需要下载的页面
            input2 = str(input("你需要第几页？输入q返回："))

            if input2 == "q":
                # 输入q退出循环
                key = False
            else:
                # 拼接请求网址
                an_key = f"/index_{input2}.html"
                if input2 == "1":
                    an_key = "/"
                # 请求网址
                resp = requests.get(url+an_key)
                resp.encoding = "gbk"
                page = resp.text
                # 正则匹配每条记录的标题和图片地址
                obj = re.compile(r'<img src="(?P<url>.*?)" alt="(?P<hart>.*?)".*?</b></a></li>', re.S)
                op = obj.finditer(page)
                # 循环下载图片
                num = 0
                for it in op:
                    num+=1
                    print(str(num)+"."+it.group("hart") + ":")
                    print("https://pic.netbian.com/"+it.group("url"))
                    int1 = "https://pic.netbian.com/" + it.group("url")
                    resp_int1 = requests.get(int1)
                    with open(it.group("hart")+".jpg", mode="wb") as f:
                        f.write(resp_int1.content)
                resp.close()

if __name__ == '__main__':
    # 创建界面
    root = tk.Tk()
    my_gui = Main(root)
    root.mainloop()