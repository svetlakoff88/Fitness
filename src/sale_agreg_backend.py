#!usr/bin/env python3
# -*- coding:utf-8 -*-

from tkinter import END, messagebox
from sqlite3 import ProgrammingError


def price_getter(lesson, curs, price_entry):
    sql_price = """SELECT Price FROM Activities WHERE Lesson LIKE(?)"""
    try:
        price_entry.delete(0, END)
        price_entry.insert(0, str(curs.execute(sql_price, (lesson,)).fetchone()[0]))
    except ProgrammingError:
        messagebox.askokcancel('Ошибка', 'Невозможно получить цену')


def discount_getter(price, discount, price_ent):
    price_ent.delete(0, END)
    price_ent.insert(0, int(int(price)-(int(price)/100*int(discount))))



