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
        Price float,
        PhoneNumber int,
        Date date,
        Description text,
        Template_status text,
        Is_active bool,
        Result text,
        Register date,
        PRIMARY KEY(Contract_ID)
        );
        CREATE TABLE IF NOT EXISTS Employees(
        FIO text,
        Training_direction text,
        PRIMARY KEY(Training_direction)
        );
        CREATE TABLE IF NOT EXISTS Activities(
        ID integer primary key autoincrement,
        Lesson text,
        Trainer text,
        Price int
        );
        CREATE TABLE IF NOT EXISTS Sales(
        Contract_ID varchar,
        Lesson text,
        Employ text,
        Client text,
        Price float,
        Discount varchar,
        Register date,
        PRIMARY KEY(Contract_ID)
        );
        CREATE TABLE IF NOT EXISTS Discounts(
        Label text,
        Description text,
        Percent int,
        Start_date date,
        End_date date,
        Param_coach text,
        Param_AB text,
        Param_prolongOrNew text,
        PRIMARY KEY (Label)
        );""")
        conn.commit()
        conn.close()
