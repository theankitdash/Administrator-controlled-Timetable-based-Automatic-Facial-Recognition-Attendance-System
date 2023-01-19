import mysql.connector
import pandas as pd 
import numpy as np

conn = mysql.connector.connect(host='localhost', username='root', password='Chiku@3037', database='attendance-system', charset='utf8')
df = pd.read_sql("SELECT Roll_No FROM student",conn)
col_names = ["Roll_No"]

attendance = pd.DataFrame(columns=col_names)