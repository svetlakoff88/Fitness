#!usr/bin/env python3
# -*- coding:utf-8 -*-

from src.variables import curs, conn
#import sqlite3

#conndb = "/home/vyacheslav/Projects/Fitness/data/ClientBase.db"

#conn = sqlite3.connect(conndb)
#curs = conn.cursor()


def insert(con_id_add, fio_add, temp_add, mem_add, tel_add, dat_add, desc_add, res_add):
    sql_cl_ins = """INSERT INTO Clients(Contract_ID,
                                        FIO,
                                        Type,
                                        Membership,
                                        Tel_num,
                                        Date,
                                        Description,
                                        Result)
                                        VALUES(?,?,?,?,?,?,?,?)"""
    curs.execute(sql_cl_ins, (con_id_add.get(),
                              fio_add.get(),
                              temp_add.get(),
                              mem_add.get(),
                              tel_add.get(),
                              dat_add.get(),
                              desc_add.get(),
                              res_add.get()))
    conn.commit()
    curs.close()
