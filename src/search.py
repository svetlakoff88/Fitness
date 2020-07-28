#!usr/bin/env python3
#-*- coding:utf-8 -*-

import psycopg2 as pg

conn = pg.connect(dbname='globalbase', user='administrator', password='qwerty1234', host='127.0.0.1', port='5432')
curs = conn.cursor()

def search():
    sql = """SELECT * FROM Clients WHERE FIO LIKE('Фомина Лидия Александровна')"""
    curs.execute(sql)
    print(curs.fetchall())


search()