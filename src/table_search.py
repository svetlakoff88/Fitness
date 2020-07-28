#!usr/bin/env python3
# -*- coding:utf-8 -*-

import pandas as pd
from src.variables import conn, in_tab


def table_in(filename):
    df = pd.ExcelFile(filename)
    sheet = df.sheet_names
    df1 = df.parse(sheet[0])
    return df1.to_sql(in_tab, conn, if_exists='replace', index=False)
