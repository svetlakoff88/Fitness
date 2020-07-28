#!usr/bin/env python3
# -*- coding:utf-8 -*-

import tkinter as tk
from tkinter import ttk
from src import variables as v
import matplotlib.pyplot as plt


class Get(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.get_data()

    def get_data(self):
        self.title('Получение информации')
        self.geometry('{}x{}'.format(self.winfo_screenwidth(), self.winfo_screenheight()))
        para_lab = tk.Label(self, text='Укажите параметры')
        fio_lab = tk.Label(self, text='ФИО')
        fio_add = tk.Entry(self, width=50)
        tel_lab = tk.Label(self, text='Телефон')
        tel_add = tk.Entry(self)
        typ_lab = tk.Label(self, text='Карта')
        typ_add = ttk.Combobox(self, width=40)
        typ_add['values'] = [i for i in set(v.curs.execute("""SELECT Template FROM Clients""").fetchall())]
        get_btn = tk.Button(self, text='Получить', command=lambda: records())
        cle_btn = tk.Button(self, text='Очистить', command=lambda: clear())
        grph_btn = tk.Button(self, text='Продажи', command=lambda: graph())
        predict_btn = tk.Button(self, text='Прогноз', command=lambda: predict())
        dat_view = ttk.Treeview(self, columns=('FIO', 'Card'), height=20, show='headings')
        sale_view = tk.Canvas(self, width=900, height=250, bg='white')
        predict_view = tk.Canvas(self, width=900, height=250, bg='white')
        yscr = ttk.Scrollbar(self, orient='vertical', command=dat_view.yview())
        xscr = ttk.Scrollbar(self, orient='horizontal', command=dat_view.xview())
        dat_view.configure(yscroll=yscr.set, xscroll=xscr.set)
        dat_view.column('FIO', width=250, anchor=tk.CENTER)
        dat_view.column('Card', width=70, anchor=tk.CENTER)
        dat_view.heading('FIO', text='ФИО')
        dat_view.heading('Card', text='Карта')
        para_lab.pack()
        fio_lab.place(x=10, y=70)
        fio_add.place(x=52, y=68)
        tel_lab.place(x=10, y=135)
        tel_add.place(x=120, y=135)
        typ_lab.place(x=10, y=165)
        typ_add.place(x=120, y=165)
        dat_view.place(x=10, y=200)
        sale_view.place(x=350, y=200)
        get_btn.place(x=40, y=630)
        cle_btn.place(x=40, y=655)

        def graph():
            """Here will be a function for the sale  visualisation"""
            pass

        def predict():
            """Here will be a function for the predict sale visualisation"""
            pass

        def records():
            for row in v.curs.execute("""SELECT FIO, Template, PhoneNumber FROM Clients """).fetchall():
                for feat in [fio_add.get(), typ_add.get(), tel_add.get()]:
                    if feat in row:
                        dat_view.insert('', tk.END, values=row)

        def clear():
            dat_view.delete(*dat_view.get_children())
