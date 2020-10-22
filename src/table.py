#!usr/bin/env python3
# -*- coding:utf-8 -*-


def create_sale_tab(curs):
    sql_tb = """CREATE TABLE IF NOT EXISTS Sales(
                FIO text,
                Date date,
                Comment text,
                Result text,
                PRIMARY KEY(FIO))"""
    curs.execute(sql_tb)
