#!usr/bin/env python3
# -*- coding:utf-8 -*-

import tkinter as tk
from tkinter import ttk
from src import Client_insert_check as Chk
from src.variables import curs
from datetime import date, timedelta
from src.sale_agreg_backend import num_generator, discount_getter


class Client(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.client()

    def client(self):
        self.title('Внесение продажи в базу данных')
        self.geometry('800x500')
        con_id_lab = tk.Label(self, text='Номер контракта')
        con_id_add = tk.Entry(self)
        con_number_btn = tk.Button(self, text='Присвоить номер', command=lambda: num_generator(con_id_add, 'AB'))
        fio_lab = tk.Label(self, text='ФИО')
        fio_add = tk.Entry(self, width=60)
        temp_lab = tk.Label(self, text='Тип членства')
        temp_add = ttk.Combobox(self, width=30)
        temp_add['values'] = [r'Дневное', r'Стандарт']
        mem_lab = tk.Label(self, text='Карта')
        mem_add = ttk.Combobox(self)
        mem_add['values'] = [r'Базовая', r'Серебро', r'Золото', r'Платина']
        price_lab = tk.Label(self, text='Цена')
        price_ent = tk.Entry(self)
        discount_lab = tk.Label(self, text='Скидка %')
        discount_ent = tk.Entry(self)
        discount_btn = tk.Button(self, text='Применить скидку', command=lambda: discount_getter(price_ent.get(),
                                                                                                discount_ent.get(),
                                                                                                price_ent))
        tel_lab = tk.Label(self, text='Номер телефона')
        tel_add = tk.Entry(self)
        dat_lab = tk.Label(self, text='Дата активации')
        dat_add = tk.Entry(self)
        dat_today_btn = tk.Button(self, text='Сегодня', command=lambda: (dat_add.delete(0, tk.END),
                                                                         dat_add.insert(0,
                                                                         date.today().__format__('%Y-%m-%d'))))
        dat_tomorrow_btn = tk.Button(self, text='Завтра', command=lambda: (dat_add.delete(0, tk.END),
                                                                           dat_add.insert(0, str(date.today() +
                                                                                                 timedelta(days=1)))))
        desc_lab = tk.Label(self, text='Комментарий')
        desc_add = tk.Entry(self, width=50)
        res_lab = tk.Label(self, text='Результат')
        res_add = tk.Entry(self, width=40)
        emp_lab = tk.Label(self, text='Тренер')
        emp_add = ttk.Combobox(self, width=40)
        emp_add['values'] = [i[0] for i in set(curs.execute("""SELECT FIO FROM Employees""").fetchall())]
        reg_btn = tk.Button(self, text='Добавить клиента', command=lambda: insert_call())
        con_id_lab.place(x=10, y=15)
        con_id_add.place(x=200, y=15)
        con_number_btn.place(x=400, y=15)
        fio_lab.place(x=10, y=55)
        fio_add.place(x=100, y=55)
        temp_lab.place(x=10, y=95)
        temp_add.place(x=200, y=95)
        mem_lab.place(x=10, y=135)
        mem_add.place(x=100, y=135)
        tel_lab.place(x=10, y=175)
        tel_add.place(x=200, y=175)
        dat_lab.place(x=10, y=215)
        dat_add.place(x=200, y=215)
        dat_today_btn.place(x=370, y=210)
        dat_tomorrow_btn.place(x=500, y=210)
        desc_lab.place(x=10, y=255)
        desc_add.place(x=200, y=255)
        res_lab.place(x=10, y=295)
        res_add.place(x=200, y=295)
        emp_lab.place(x=10, y=335)
        emp_add.place(x=150, y=335)
        price_lab.place(x=10, y=375)
        price_ent.place(x=150, y=375)
        discount_lab.place(x=10, y=415)
        discount_ent.place(x=150, y=415)
        discount_btn.place(x=350, y=410)
        reg_btn.place(x=230, y=450)

        def insert_call():
            """Добавить цену и скидку на запись в базу"""
            Chk.check(con_id_add, fio_add, temp_add, mem_add, tel_add, dat_add, desc_add, res_add, price_ent,
                      date.today())
            self.destroy()
