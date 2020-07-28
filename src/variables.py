#!usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

conn_db = "/home/vyacheslav/Projects/Fitness/data/ClientBase.db"

conn = sqlite3.connect(conn_db)
curs = conn.cursor()

in_tab = 'Clients'
