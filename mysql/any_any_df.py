"""mysqlからの出力を簡単に!"""
"""使い方は　『python any_any_df.py sql文　出力ファイル名』　"""

import pymysql
import numpy as np
import pickle
import sys
import pandas as pd

con = pymysql.connect('localhost','root','3251006r','Flaming')
sql = ' '.join(sys.argv[1:-1])
df = pd.read_sql(sql=sql, con=con)
print("実行したsql文{}".format(sql))
with open('/Users/ryusuke/Downloads/研究/Flaming/pymysql/{}.pkl'.format(sys.argv[-1]), 'wb') as f:
    pickle.dump(df,f)
