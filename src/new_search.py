#!usr/bin/env/python3
# -*- coding:utf-8 -*-

from tkinter import filedialog as fd
from src import table_search as tb


def file_open():
    filename = fd.askopenfilename(initialdir="/", title="Select file", filetypes=(("jpeg files", "*.jpg", ),
                                                                                  ("all files", "*.*")))
    try:
        tb.table_in(filename)
    except ValueError:
        pass
