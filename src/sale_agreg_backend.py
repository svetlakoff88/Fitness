#!usr/bin/env python3
# -*- coding:utf-8 -*-

from tkinter import END, messagebox
from sqlite3 import ProgrammingError, IntegrityError
from src.variables import curs as cursor, conn as connect


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


def coach_getter(lesson, curs):
    sql_coach = """SELECT Trainer FROM Activities WHERE Lesson LIKE(?)"""
    res = curs.execute(sql_coach, (lesson,)).fetchall()
    return res


# print([str(i[0]) for i in coach_getter('Кроссфит', cursor)])

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

