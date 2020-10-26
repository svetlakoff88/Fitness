#!usr/bin/env python3
# -*- coding:utf-8 -*-

from tkinter import END, messagebox
from sqlite3 import ProgrammingError, IntegrityError
from src.variables import curs as cursor, conn as connect
from string import ascii_lowercase, digits
from random import choice
from datetime import date

def price_getter(lesson, curs, price_entry, coach):
    sql_price = """SELECT Price FROM Activities WHERE Lesson LIKE(?) AND Trainer LIKE(?)"""
    try:
        price_entry.delete(0, END)
        price_entry.insert(0, str(curs.execute(sql_price, (lesson, coach)).fetchone()[0]))
    except ProgrammingError:
        messagebox.askokcancel('Ошибка', 'Невозможно получить цену')


def discount_getter(price, discount, price_ent):
    price_ent.delete(0, END)
    price_ent.insert(0, int(int(price)-(int(price)/100*int(discount))))


def coach_getter(lesson, curs, coach_ent):
    sql_coach = """SELECT Trainer FROM Activities WHERE Lesson LIKE(?)"""
    if lesson != '':
        coach_ent['values'] = [i[0] for i in set(curs.execute(sql_coach, (lesson,)).fetchall())]
    else:
        coach_ent['values'] = [r'empty']


def setter(curs, conn):
    sql = """insert into Activities (Lesson, Trainer, Price) values ('Кроссфит', 'Светлакова Екатерина', '13000')"""
    try:
        curs.execute(sql)
        conn.commit()
        conn.close()
    except IntegrityError:
        curs.execute(sql)
        conn.commit()
        conn.close()


# setter(cursor, connect)

def num_generator(con_id):
    number = ''
    for i in range(6):
        number += choice(digits)
        con_id.delete(0, END)
    return con_id.insert(0, str(date.today().__format__("%d%m%Y") + "/" + number))



