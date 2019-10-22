import pymysql
import numpy as np
import pickle

con = pymysql.connect('localhost','root','3251006r','Flaming')
with con:
    tweet_number=[]
    cur = con.cursor()
    cur.execute("select count(user_id) from KyotoAnimation group by user_id")
    number_tuple = cur.fetchall()
    half_tuple = list(number_tuple)
    len_tuple = len(half_tuple)
    for i in range(len_tuple):
        part_number = list(half_tuple[i])
        tweet_number.append(part_number)
    tweet_number = list(np.array(tweet_number).reshape(-1))
    with open('/Users/ryusuke/Downloads/研究/Flaming/pymysql/user_number.pickle', 'wb') as f:
        pickle.dump(tweet_number, f)
