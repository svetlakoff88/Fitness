#!usr/bin/env python3
# -*- coding:utf-8 -*-

from tkinter import END, messagebox
from sqlite3 import ProgrammingError
from random import choice
from string import digits
from datetime import date


def client_check(client_ent, curs):
    sql_cli = """SELECT FIO FROM Clients WHERE FIO LIKE(?)"""
    res = curs.execute(sql_cli, (client_ent,)).fetchone()
    if res is None:
        messagebox.askokcancel('Ошибка', 'Клиент не найден в базе данных')
    else:
        messagebox.askokcancel('Проверка', 'Клиент зарегистрирован в базе данных')


def price_getter(lesson, curs, price_entry, coach):
    sql_price = """SELECT Price FROM Activities WHERE Lesson LIKE(?) AND Trainer LIKE(?)"""
    try:
        price_entry.delete(0, END)
        price_entry.insert(0, str(curs.execute(sql_price, (lesson, coach)).fetchone()[0]))
    except ProgrammingError:
        messagebox.askokcancel('Ошибка', 'Невозможно получить цену')
    except TypeError:
        messagebox.askokcancel('Ошибка', 'Заполните поле Тренер!')


def discount_getter(price, discount, price_ent):
    try:
        price_ent.delete(0, END)
        price_ent.insert(0, int(int(price)-(int(price)/100*int(discount))))
    except ValueError:
        if discount == '':
            messagebox.askokcancel('Ошибка', 'Некорректно введена скидка!')
        else:
            messagebox.askokcancel('Ошибка', 'Некорректно введена цена!')


def coach_getter(lesson, curs, coach_ent):
    sql_coach = """SELECT Trainer FROM Activities WHERE Lesson LIKE(?)"""
    if lesson != '':
        coach_ent['values'] = [i[0] for i in set(curs.execute(sql_coach, (lesson,)).fetchall())]
    else:
        coach_ent['values'] = [r'empty']


def num_generator(con_id, mode):
    number = ''
    for i in range(6):
        number += choice(digits)
        con_id.delete(0, END)
    if mode == 'pt':
        return con_id.insert(0, str(date.today().__format__("%d%m%Y") + "/" + number + 'PT'))
    elif mode == 'ab':
        return con_id.insert(0, str(date.today().__format__("%d%m%Y") + "/" + number + 'AB'))


def sale_insert():
    pass
