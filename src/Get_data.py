#!usr/bin/env python3
# -*- coding:utf-8 -*-

import tkinter as tk
from tkinter import ttk, messagebox
from src import variables as v
from src import Analytics as a
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


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
        cont_lab = tk.Label(self, text='Номер договора')
        cont_ent = tk.Entry(self)
        typ_lab = tk.Label(self, text='Карта')
        clear_sale_view = tk.Button(self, text='Очистить график продаж')
        typ_add = ttk.Combobox(self, width=40)
        typ_add['values'] = [i for i in set(v.curs.execute("""SELECT Template FROM Clients""").fetchall())]
        get_btn = tk.Button(self, text='Получить', command=lambda: records())
        cle_btn = tk.Button(self, text='Очистить', command=lambda: clear())
        grph_btn = tk.Button(self, text='Продажи', command=lambda: graph(a.sale_data_get(dat_view), sale_view,
                                                                         clear_sale_view))
        predict_btn = tk.Button(self, text='Прогноз', command=lambda: predict())
        dat_view = ttk.Treeview(self, columns=('FIO', 'Card'), height=20, show='headings')
        sale_view = tk.Canvas(self, width=900, height=200, bg='white')
        predict_view = tk.Canvas(self, width=900, height=200, bg='white')
        yscr = ttk.Scrollbar(self, orient='vertical', command=dat_view.yview())
        xscr = ttk.Scrollbar(self, orient='horizontal', command=dat_view.xview())
        dat_view.configure(yscroll=yscr.set, xscroll=xscr.set)
        dat_view.column('FIO', width=250, anchor=tk.CENTER)
        dat_view.column('Card', width=70, anchor=tk.CENTER)
        dat_view.heading('FIO', text='ФИО')
        dat_view.heading('Card', text='Карта')
        para_lab.pack()
        fio_lab.place(x=10, y=50)
        fio_add.place(x=52, y=48)
        cont_lab.place(x=10, y=90)
        cont_ent.place(x=130, y=90)
        tel_lab.place(x=10, y=125)
        tel_add.place(x=120, y=125)
        typ_lab.place(x=10, y=155)
        typ_add.place(x=120, y=155)
        dat_view.place(x=10, y=200)
        sale_view.place(x=350, y=200)
        predict_view.place(x=350, y=420)
        get_btn.place(x=40, y=630)
        cle_btn.place(x=40, y=655)
        grph_btn.place(x=700, y=655)
        predict_btn.place(x=850, y=655)
        clear_sale_view.place(x=1000, y=655)

        def graph(params, base_canvas, button):
            if params:
                figure = Figure(figsize=(9, 2))
                fig_sub = figure.add_subplot(111)
                fig_sub.plot(params[0], params[1], color='green')
                space = FigureCanvasTkAgg(figure, master=base_canvas)
                space.get_tk_widget().pack()
                button['command'] = lambda: sale_graph_clear(figure, space)
                space.draw()
            else:
                messagebox.showerror('Ошибка', 'Проверьте заполнение полей!')

        def sale_graph_clear(figure, canv):
            figure.clear()
            canv.get_tk_widget().pack_forget()

        def predict():
            """Here will be a function for the predict sale visualisation"""
            pass

        def records():
            for row in v.curs.execute("""SELECT FIO, Template, PhoneNumber, Contract_ID FROM Clients """).fetchall():
                for feat in [int(tel_add.get()), cont_ent.get(), fio_add.get(), typ_add.get()]:
                    if feat in row:
                        dat_view.insert('', tk.END, values=row)

        def clear():
            dat_view.delete(*dat_view.get_children())
