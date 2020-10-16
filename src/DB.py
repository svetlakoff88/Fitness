#!usr/bin/env python3
# -*- coding:utf-8 -*-

import sqlite3

conn_db = "/home/vyacheslav/Projects/Fitness/data/ClientBase.db"

conn = sqlite3.connect(conn_db)
curs = conn.cursor()


class DB:
    def __init__(self):
        curs.executescript("""CREATE TABLE IF NOT EXISTS Clients(
        Contract_ID varchar,
        FIO text,
        Template text,
        ContractType text,
        PhoneNumber int,
        Date date,
        Description text,
        Result text,
        PRIMARY KEY(Contract_ID)
        );
        CREATE TABLE IF NOT EXISTS Employees(
        FIO text,
        Training_direction text,
        PRIMARY KEY(Training_direction)
        );
        CREATE TABLE IF NOT EXISTS Activities(
        Lesson text,
        Trainer text,
        Price float,
        PRIMARY KEY(Lesson)
        );
        CREATE TABLE IF NOT EXISTS Sales(
        Contract_ID varchar,
        Employ text,
        Client text,
        Price float,
        Discount varchar,
        PRIMARY KEY(Contract_ID)
        );
        """)
        conn.commit()
        conn.close()



