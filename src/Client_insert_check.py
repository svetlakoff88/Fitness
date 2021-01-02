#!usr/bin/env python3
# -*- coding:utf-8 -*-

import sqlite3
from src import Client_insert as Cl_in
from tkinter import messagebox
from src.variables import curs


def check(con_id_add, fio_add, temp_add, mem_add, tel_add, desc_add, dat_add, res_add, price_add, reg_dat):
    sql_cl = """SELECT*
                FROM Clients"""
    curs.execute(sql_cl)
    try:
        cl_lst = [con_id_add.get(), fio_add.get(), temp_add.get(), mem_add.get(), tel_add.get(), desc_add.get(),
                  dat_add.get(), res_add.get(), reg_dat]
        res = curs.fetchall()
        if cl_lst not in res:
            Cl_in.insert(con_id_add, fio_add, temp_add, mem_add, tel_add, desc_add, dat_add, res_add, price_add,
                         reg_dat)
        else:
            pass
    except sqlite3.IntegrityError:
        messagebox.showerror('Error', 'Клиент уже зарегистрирован в базе!')
    finally:
        pass
