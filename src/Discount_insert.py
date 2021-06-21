#!usr/bin/env python3
# -*- coding:utf-8-*-

def disc_insert(name, description, percent, start, end, coach, abon_type,
                long_or_new, conn, destroy):
    query = conn.cursor().execute("""INSERT INTO Discounts(Label, 
                                                Description, 
                                                Percent, 
                                                Start_date, 
                                                End_date, 
                                                Param_coach, 
                                                Param_AB, 
                                                Param_ProlongOrNew)
                                                VALUES(?,?,?,?,?,?,?,?)""", (name,
                                                                             description,
                                                                             percent,
                                                                             start,
                                                                             end,
                                                                             coach,
                                                                             abon_type,
                                                                             long_or_new))
    conn.commit()
    destroy
