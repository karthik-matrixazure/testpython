# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 15:06:32 2019

@author: Hp
"""

import pandas as pd
import pyodbc

sql_conn = pyodbc.connect(DRIVER='{ODBC Driver 17 for SQL Server}',
                            SERVER='tcp:pythonazuretest.database.windows.net,1433',
                            DATABASE='PythonAzureTest',
#                            Trusted_Connection='yes',
                            uid='PythonAzureTest',
                            pwd='Python@123',
                            Encrypt='yes',
                            TrustServerCertificate='no')
cursor = sql_conn.cursor()
cursor.execute('SELECT * FROM PythonAzureTest.dbo.input_test')

row = cursor.fetchone()
print(row)
cursor.execute("INSERT INTO output_test(output_data) SELECT input_data FROM PythonAzureTest.dbo.input_test;")
cursor.execute('SELECT * FROM PythonAzureTest.dbo.output_test')
row = cursor.fetchone()
print('output',row)
#Commiting any pending transaction to the database.
sql_conn.commit()
print("Data Successfully Inserted")   
sql_conn.close()  



#dns = 'Driver={ODBC Driver 13 for SQL Server};Server=tcp:pythonazuretest.database.windows.net,1433;Database=PythonAzureTest;Uid=PythonAzureTest;Pwd={your_password_here};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30'