#!usr/bin/env python3
# -*- coding:utf-8 -*-

from src import variables as v
import tkinter as tk
from tkinter import ttk


class Aggregation(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.create_window()

    def create_window(self):
        self.title('Оформление продажи')
        self.geometry("500x500")
        cli_lab = tk.Label(self, text='Найти клиента')
        cli_ent = ttk.Combobox(self, width=80)
        cli_ent['values'] = [i for i in set(v.curs.execute("""SELECT FIO FROM Clients""").fetchall())]
        les_lab = tk.Label(self, text='Выбрать тип продукта')
        les_ent = ttk.Combobox(self, width=80)
        les_ent['values'] = [i for i in set(v.curs.execute("""SELECT Lesson FROM Activities"""))]
        trainer_lab = tk.Label(self, text='Выбрать тренера')
        trainer_ent = ttk.Combobox(self, width=80)
        trainer_ent['values'] = [i for i in set(v.curs.execute("""SELECT FIO FROM Employees WHERE Training_direction
                                                                    LIKE (?)""", les_ent.get()).fetchall())]
        cost_lab = tk.Label(self, text='Цена')
        cost_ent = ttk.Treeview(self, width=40, height=5)
        cost_ent.insert(self, tk.END, values=set(v.curs.execute("""SELECT Price FROM Activities 
                                                                WHERE Lesson LIKE (?)""", les_ent.get()).fetchone()))
        discount_lab = tk.Label(self, text='Скидка')
        discount_ent = tk.Entry(self, width=15)
        discount_btn = tk.Button(self, text='Применить скидку')
