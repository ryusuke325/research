"""未完成"""
import pymysql
import numpy as np
import pickle
import sys

target = sys.argv[1]
column = sys.argv[2]
con = pymysql.connect('localhost','root','3251006r','Flaming')
with con:
    retweet_number=[]
    cur = con.cursor()
    sql = "select count(%s) from KyotoAnimation group by %s"
    cur.execute(sql,(target,columns))
    number_tuple = cur.fetchall()
    half_tuple = list(number_tuple)
    len_tuple = len(half_tuple)
    for i in range(len_tuple):
        part_number = list(half_tuple[i])
        retweet_number.append(part_number)
    tweet_number = list(np.array(tweet_number).reshape(-1))
    with open('/Users/ryusuke/Downloads/研究/Flaming/pymysql/retweet_number.pickle', 'wb') as f:
        pickle.dump(tweet_number, f)
