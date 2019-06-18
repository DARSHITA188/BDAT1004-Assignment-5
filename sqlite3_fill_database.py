# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 11:44:16 2019

@author: 17057
"""

import os
import sqlite3

db_filename = 'groups.db'
schema_filename = 'groups_schema.sql'

db_is_new = not os.path.exists(db_filename)

with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print('Creating Schema')
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)
        
        print('Inserting initial data')
            
        conn.executescript("""
            insert into grp (ID, Name, Course_ID)
            values ('200425025', 'Manish', 'BDAT1004');
            
            insert into grp (ID, Name, Course_ID)
            values ('200424007', 'Zishan', 'BDAT1002');
            
            insert into grp (ID, Name, Course_ID)
            values ('200424891', 'Diksha', 'BDAT1001');
            
            insert into grp (ID, Name, Course_ID)
            values ('200425942', 'Darshita', 'BDAT1002');
            
            insert into course (Course_ID, Course_Name)
            values ('BDAT1003', 'Business Processes');
            
            insert into course (Course_ID, Course_Name)
            values ('BDAT1004', 'Data Programming');
            
            insert into course (Course_ID, Course_Name)
            values ('BDAT1000', 'Data Manipulation Techniques');
            
            insert into course (Course_ID, Course_Name)
            values ('BDAT1001', 'Information Encoding Standards');
            
            insert into course (Course_ID, Course_Name)
            values ('BDAT1002', 'Data Systems Architecture');
            
            insert into course (Course_ID, Course_Name)
            values ('BDAT1005', 'Math for Data Analytics'); 
            """)
        
    else:
        
        print('Database exists, assuming that schema exists too..')
        
        