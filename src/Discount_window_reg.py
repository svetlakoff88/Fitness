#!usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from src import variables as v
from src import Discount_insert as Ds
from datetime import date

class WindowReg(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.discount_reg()

    def discount_reg(self):
        self.title('Регистрация акционного предложения')
        self.geometry('700x400')
        name_lab = tk.Label(self, text='Название предложения')
        name_ent = tk.Entry(self, width=35)
        desc_lab = tk.Label(self, text='Описание предложения')
        desc_ent = tk.Entry(self, width=50)
        perc_lab = tk.Label(self, text='Размер скидки % ')
        perc_ent = tk.Entry(self, width=10)
        start_lab = tk.Label(self, text='Начало действия ГГГГ/ММ/ДД')
        start_ent_y = tk.Entry(self, width=5)
        start_ent_m = tk.Entry(self, width=5)
        start_ent_d = tk.Entry(self, width=5)
        end_lab = tk.Label(self, text='Окончание действия ГГГГ/ММ/ДД')
        end_ent_y = tk.Entry(self, width=5)
        end_ent_m = tk.Entry(self, width=5)
        end_ent_d = tk.Entry(self, width=5)
        mark_desc = tk.Label(self, text='Укажите параметры которые задействованы в предложении')
        coach_lab = tk.Label(self, text='Тренер')
        coach_ent = ttk.Combobox(self, width=40)
        coach_ent['values'] = [i[0] for i in set(
            v.conn.cursor().execute("""SELECT FIO FROM Employees""").fetchall())]
        abon_type_lab = tk.Label(self, text='Тип абонемента')
        abon_type_ent = ttk.Combobox(self, width=20)
        abon_type_ent['values'] = [i[0] for i in set(v.curs.execute("""SELECT Template FROM Clients""").fetchall())]
        long_or_new_lab = tk.Label(self, text='Статус договора')
        long_or_new_ent = ttk.Combobox(self, width=20)
        long_or_new_ent['values'] = [r'Новый', r'Продление']
        disc_reg_btn = tk.Button(self, text='Зарегистрировать', command=lambda: Ds.disc_insert(name_ent.get(),
                                                                                               desc_ent.get(),
                                                                                               perc_ent.get(),
                                                                                               date(int(
                                                                                                   start_ent_y.get()),
                                                                                               int(start_ent_m.get()),
                                                                                               int(start_ent_d.get())).
                                                                                               __format__('%Y-%m-%d'),
                                                                                               date(int(
                                                                                                   end_ent_y.get()),
                                                                                               int(end_ent_m.get()),
                                                                                               int(end_ent_d.get())).
                                                                                               __format__('%Y-%m-%d'),
                                                                                               coach_ent.get(),
                                                                                               abon_type_ent.get(),
                                                                                               long_or_new_ent.get(),
                                                                                               v.conn))
        name_lab.place(x=10, y=30)
        name_ent.place(x=250, y=30)
        desc_lab.place(x=10, y=60)
        desc_ent.place(x=250, y=60)
        perc_lab.place(x=10, y=90)
        perc_ent.place(x=200, y=90)
        start_lab.place(x=10, y=120)
        start_ent_y.place(x=310, y=120)
        start_ent_m.place(x=355, y=120)
        start_ent_d.place(x=400, y=120)
        end_lab.place(x=10, y=150)
        end_ent_y.place(x=350, y=150)
        end_ent_m.place(x=395, y=150)
        end_ent_d.place(x=440, y=150)
        mark_desc.place(x=10, y=185)
        coach_lab.place(x=10, y=215)
        coach_ent.place(x=100, y=215)
        abon_type_lab.place(x=10, y=245)
        abon_type_ent.place(x=180, y=245)
        long_or_new_lab.place(x=10, y=275)
        long_or_new_ent.place(x=180, y=275)
        disc_reg_btn.place(x=400, y=305)
