#! usr/bin/env python3
# -*- coding:utf-8 -*-

from src.DB import conn, curs


def search():
    sql = """SELECT fio FROM Clients WHERE type LIKE ('Сотрудник')"""
    curs.execute(sql)
    dat = curs.fetchall()
    for i in dat:
        sql2 = """INSERT INTO employees(fio) VALUES(?)"""
        curs.execute(sql2, i)
        conn.commit()


search()
