#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Python 2 and 3
Created on Wed Jan 29 18:40:31 2014
name: inspectsqlite.py
@author: Gribouillis for the python forum at www.daniweb.com
@license: Public Domain
Use this code freely
"""
__version__ = '0.1.1'
import argparse
import contextlib
import prettytable as ptt # sudo pip install prettytable
import sqlite3
def get_table_names(cursor):
    s = "SELECT `name` FROM `sqlite_master` WHERE `type`='table'"
    cursor.execute(s)
    names = [r[0] for r in cursor.fetchall()]
    return names
headers = "table_name cid name type notnull dflt_value pk".split()
def get_columns(cursor):
    tpl = "PRAGMA table_info(`{}`)" #http://www.sqlite.org/pragma.html#pragma_table_info
    names = get_table_names(cursor)
    for n in names:
        s = tpl.format(n)
        cursor.execute(s)
        for row in cursor:
            yield (n,) + tuple(row)
            
def print_all_columns(filename):
    table = ptt.PrettyTable(headers)
    table.align = 'l'
    with contextlib.closing(sqlite3.connect(filename)) as conn:
        with contextlib.closing(conn.cursor()) as cursor:
            for row in get_columns(cursor):
                table.add_row(row)
    print(table)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Display all columns of an sqlite database.")
    parser.add_argument('filename',
        action = 'store',
        help = 'path to database file',
        metavar = 'FILE',
    )
    args = parser.parse_args()
    print_all_columns(args.filename)
""" Exemple use in a linux terminal:
    
$ python inspectsqlite.py ~/.mozilla/firefox/*.default/formhistory.sqlite
+-------------------------+-----+-------------+---------+---------+------------+----+
| table_name              | cid | name        | type    | notnull | dflt_value | pk |
+-------------------------+-----+-------------+---------+---------+------------+----+
| moz_formhistory         | 0   | id          | INTEGER | 0       | None       | 1  |
| moz_formhistory         | 1   | fieldname   | TEXT    | 1       | None       | 0  |
| moz_formhistory         | 2   | value       | TEXT    | 1       | None       | 0  |
| moz_formhistory         | 3   | timesUsed   | INTEGER | 0       | None       | 0  |
| moz_formhistory         | 4   | firstUsed   | INTEGER | 0       | None       | 0  |
| moz_formhistory         | 5   | lastUsed    | INTEGER | 0       | None       | 0  |
| moz_formhistory         | 6   | guid        | TEXT    | 0       | None       | 0  |
| moz_deleted_formhistory | 0   | id          | INTEGER | 0       | None       | 1  |
| moz_deleted_formhistory | 1   | timeDeleted | INTEGER | 0       | None       | 0  |
| moz_deleted_formhistory | 2   | guid        | TEXT    | 0       | None       | 0  |
+-------------------------+-----+-------------+---------+---------+------------+----+
"""
