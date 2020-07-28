#! usr/bin/env python3
# -*- coding:utf-8 -*-

import tkinter as tk


class Analytic(tk.Frame):
    def __init__(self):
        super().__init__()

    def set(self):
        pass


if __name__ == '__main__':
    root = tk.Tk()
    app = Analytic()
    app.pack()
    root.title('Аналитика')
    root.geometry('700x500+300+100')
    root.mainloop()
