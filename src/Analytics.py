#! usr/bin/env python3
# -*- coding:utf-8 -*-

import src.variables as v
from tkinter import messagebox
import matplotlib
matplotlib.use("TkAgg")


def sale_data_get(client, curs=v.curs):
    dat_lst = list()
    sal_lst = list()
    try:
        for i in curs.execute("""SELECT Register FROM Sales WHERE Client LIKE(?)""", (
                client.item(client.focus()).get('values')[0],)).fetchall():
            dat_lst.append(i[0])
        for j in curs.execute("""SELECT Price FROM Sales WHERE Client LIKE(?)""", (
                client.item(client.focus()).get('values')[0],)).fetchall():
            sal_lst.append(j[0])
    except IndexError:
        messagebox.showerror('Ошибка', 'Проверьте заполнение полей!')
    return dat_lst, sal_lst


def predict_data_get(trainer, date, conn=v.conn):
    curs = conn.cursor()
    trainer_price = [i for i in curs.execute("""SELECT Price FROM Sales WHERE Employ LIKE(?)
                                                AND Register LIKE(?)""", (trainer, date)).fetchall()]
    return trainer_price


def predict_data_prepend(data):
    window = 2
    horizon = 2
