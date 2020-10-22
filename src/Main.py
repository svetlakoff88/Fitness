#!usr/bin/env python3
# -*- coding:utf-8 -*-

import tkinter as tk
from src import DB
from src import Client as Cl
from src import new_search as nw
from src import Get_data as Gt
from src import Series_agregate as Sa

an_img = '/home/vyacheslav/Projects/Fitness/resources/analytics.png'
emp_img = '/home/vyacheslav/Projects/Fitness/resources/employees.png'
cli_img = '/home/vyacheslav/Projects/Fitness/resources/clients.png'
tab_img = '/home/vyacheslav/Projects/Fitness/resources/table.png'
tab_img_out = '/home/vyacheslav/Projects/Fitness/resources/table_out.png'
series_img = '/home/vyacheslav/Projects/Fitness/resources/sale.png'


class Main(tk.Frame):
    def __init__(self, img1, img2, img3, img4, img5):
        super().__init__(root)
        DB.DB()
        self.add_tab_img = tk.PhotoImage(file=img1)
        self.add_cli_img = tk.PhotoImage(file=img2)
        self.out_tab_img = tk.PhotoImage(file=img3)
        self.add_an_img = tk.PhotoImage(file=img4)
        self.add_series_img = tk.PhotoImage(file=img5)
        self.init_main()

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        body_frame = tk.Frame(bg='#d7d8e0', bd=2)
        body_frame.pack(side=tk.TOP, fill=tk.X)
        client_btn = tk.Button(toolbar, text='Добавить клиента', command=lambda: client_call(), bg='#d7d8e0', bd=0,
                               compound=tk.TOP, image=self.add_cli_img)
        tab_in_btn = tk.Button(toolbar, text='Загрузить таблицу', command=lambda: table_in(), bg='#d7d8e0', bd=0,
                               compound=tk.TOP, image=self.add_tab_img)
        tab_out_btn = tk.Button(toolbar, text='Выгрузить таблицу', command=lambda: table_out(), bg='#d7d8e0', bd=0,
                                compound=tk.TOP, image=self.out_tab_img)
        an_btn = tk.Button(body_frame, text='Инструменты Аналитики', command=lambda: an_get(), bg='#d7d8e0', bd=0,
                           compound=tk.TOP, image=self.add_an_img)
        series_btn = tk.Button(body_frame, text='Добавить продажу', command=lambda: series_call(), bg='#d7d8e0', bd=0,
                               compound=tk.TOP, image=self.add_series_img)
        client_btn.pack(side=tk.LEFT)
        tab_in_btn.pack(side=tk.LEFT)
        tab_out_btn.pack(side=tk.LEFT)
        an_btn.pack(side=tk.LEFT)
        series_btn.pack(side=tk.LEFT)

        def series_call():
            Sa.Aggregation()

        def client_call():
            Cl.Client()

        def table_in():
            nw.file_open()

        def table_out():
            pass

        def an_get():
            Gt.Get(root)


if __name__ == '__main__':
    root = tk.Tk()
    app = Main(tab_img, cli_img, tab_img_out, an_img, series_img)
    app.pack()
    root.title('Клиентская База')
    root.geometry('700x200')
    root.resizable(False, False)
    root.mainloop()
