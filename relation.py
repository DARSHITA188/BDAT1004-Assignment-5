# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 00:01:34 2019

@author: 17057
"""

import os
import sqlite3

conn = sqlite3.connect('groups.db')

c = conn.cursor()

c.execute("SELECT * FROM grp INNER JOIN course ON grp.Course_ID = course.Course_ID")

print(c.fetchmany(10))
conn.commit()
conn.close()

