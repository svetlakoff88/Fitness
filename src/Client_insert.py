#!usr/bin/env python3
# -*- coding:utf-8 -*-

from src.variables import curs, conn


def insert(con_id_add, fio_add, temp_add, mem_add, tel_add, dat_add, desc_add, res_add, reg_dat):
    sql_cl_ins = """INSERT INTO Clients(Contract_ID,
                                        FIO,
                                        Template,
                                        ContractType,
                                        PhoneNumber,
                                        Date,
                                        Description,
                                        Result,
                                        Register
                                        )
                                        VALUES(?,?,?,?,?,?,?,?,?)"""
    curs.execute(sql_cl_ins, (con_id_add.get(),
                              fio_add.get(),
                              temp_add.get(),
                              mem_add.get(),
                              tel_add.get(),
                              dat_add.get(),
                              desc_add.get(),
                              res_add.get(),
                              reg_dat))
    conn.commit()
    # curs.close()
