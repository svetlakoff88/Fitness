#!usr/bin/env python3
# -*- coding:utf-8 -*-

from src import variables as v
import tkinter as tk
from tkinter import ttk
from src import sale_agreg_backend as sl


class Aggregation(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.create_window()

    def create_window(self):
        self.title('Оформление продажи')
        self.geometry('{}x{}'.format(self.winfo_screenwidth(), self.winfo_screenheight()))
        cli_lab = tk.Label(self, text='Найти клиента')
        cli_ent = tk.Entry(self, width=80)
        les_lab = tk.Label(self, text='Выбрать тип продукта')
        les_ent = ttk.Combobox(self, width=80)
        les_ent['values'] = [i[0] for i in set(v.curs.execute("""SELECT Lesson FROM Activities""").fetchall())]
        trainer_lab = tk.Label(self, text='Выбрать тренера')
        trainer_ent = ttk.Combobox(self, width=80)
        trainer_btn = tk.Button(self, text='Получить список тренеров', command=lambda: sl.coach_getter(les_ent.get(),
                                                                                                       v.curs,
                                                                                                       trainer_ent))
        cost_lab = tk.Label(self, text='Цена')
        cost_ent = tk.Entry(self, width=10)
        cost_get_btn = tk.Button(self, text='Получить цену', command=lambda: sl.price_getter(les_ent.get(),
                                                                                             v.curs,
                                                                                             cost_ent,
                                                                                             trainer_ent.get()))
        discount_lab = tk.Label(self, text='Скидка %')
        discount_ent = tk.Entry(self, width=5)
        discount_btn = tk.Button(self, text='Применить скидку', command=lambda: sl.discount_getter(cost_ent.get(),
                                                                                                   discount_ent.get(),
                                                                                                   cost_ent))
        cli_lab.place(x=10, y=70)
        cli_ent.place(x=165, y=70)
        les_lab.place(x=10, y=100)
        les_ent.place(x=250, y=100)
        trainer_lab.place(x=10, y=130)
        trainer_ent.place(x=200, y=130)
        trainer_btn.place(x=850, y=130)
        cost_lab.place(x=10, y=160)
        cost_ent.place(x=80, y=160)
        discount_lab.place(x=10, y=190)
        discount_ent.place(x=100, y=190)
        discount_btn.place(x=150, y=190)
        cost_get_btn.place(x=195, y=160)
