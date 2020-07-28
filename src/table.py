#!usr/bin/env python3
# -*- coding:utf-8 -*-

import sqlite3

conndb = "/home/vyacheslav/Projects/Fitness/data/ClientBase.db"

conn = sqlite3.connect(conndb)
curs = conn.cursor()

sql_tb = """CREATE TABLE IF NOT EXISTS VT(
            FIO text,
            Date date,
            Comment text,
            Result text,
            PRIMARY KEY(FIO))"""
curs.execute(sql_tb)