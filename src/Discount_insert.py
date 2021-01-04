#!usr/bin/env python3
# -*- coding:utf-8-*-

def disc_insert(name, description, percent, start, end, coach, abon_type,
                long_or_new, conn):
    conn.cursor().execute("""INSERT INTO Discounts(Label, 
                                                Description, 
                                                Percent, 
                                                Start_date, 
                                                End_date, 
                                                Param_coach, 
                                                Param_AB, 
                                                Param_longornew)""", (name,
                                                                      description,
                                                                      percent,
                                                                      start,
                                                                      end,
                                                                      coach,
                                                                      abon_type,
                                                                      long_or_new))
    conn.cursor().commit()
    conn.cursor().close()
    conn.close()
