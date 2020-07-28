#!usr/bin/env python3
# -*- coding:utf-8 -*-

import tkinter as tk
from tkinter import ttk
from src import Client_insert_check as Chk
from src.variables import curs


class Client(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.client()

    def client(self):
        self.title('Внесение продажи в базу данных')
        self.geometry('400x350')
        con_id_lab = tk.Label(self, text='Номер контракта')
        con_id_add = tk.Entry(self)
        fio_lab = tk.Label(self, text='ФИО')
        fio_add = tk.Entry(self, width=40)
        temp_lab = tk.Label(self, text='Тип членства')
        temp_add = tk.Entry(self)
        mem_lab = tk.Label(self, text='Карта')
        mem_add = tk.Entry(self)
        tel_lab = tk.Label(self, text='Номер телефона')
        tel_add = tk.Entry(self)
        dat_lab = tk.Label(self, text='Дата активации')
        dat_add = tk.Entry(self)
        desc_lab = tk.Label(self, text='Комментарий')
        desc_add = tk.Entry(self, width=50)
        res_lab = tk.Label(self, text='Результат')
        res_add = tk.Entry(self, width=40)
        emp_lab = tk.Label(self, text='Тренер')
        emp_add = ttk.Combobox(self, width=40)
        emp_add['values'] = [i for i in curs.execute("""SELECT FIO FROM Employees""").fetchall()]
        reg_btn = tk.Button(self, text='Добавить клиента', command=lambda: insert_call())
        con_id_lab.pack()
        con_id_add.pack()
        fio_lab.pack()
        fio_add.pack()
        temp_lab.pack()
        temp_add.pack()
        mem_lab.pack()
        mem_add.pack()
        tel_lab.pack()
        tel_add.pack()
        dat_lab.pack()
        dat_add.pack()
        desc_lab.pack()
        desc_add.pack()
        res_lab.pack()
        res_add.pack()
        emp_lab.pack()
        emp_add.pack()
        reg_btn.place(x=100, y=310)

        def insert_call():
            Chk.check(con_id_add, fio_add, temp_add, mem_add, tel_add, dat_add, desc_add, res_add)

    # noinspection PyMethodMayBeStatic
    def glob_call(self, employ):
        sq_el = """SELECT FIO FROM Employees"""
        for i in curs.fetchall(sq_el):
            employ.append(i)
        return employ
