import pymysql
import numpy as np
import pickle

con = pymysql.connect('localhost','root','3251006r','Flaming')
with con:
    retweet_number=[]
    cur = con.cursor()
    cur.execute("select count(retweet_id) from KyotoAnimation where retweet_id is not null group by retweet_id")
    number_tuple = cur.fetchall()
    half_tuple = list(number_tuple)
    len_tuple = len(half_tuple)
    for i in range(len_tuple):
        part_number = list(half_tuple[i])
        retweet_number.append(part_number)
    retweet_number = list(np.array(retweet_number).reshape(-1))
    with open('/Users/ryusuke/Downloads/研究/Flaming/pymysql/retweet_retweet_list.pickle', 'wb') as f:
        pickle.dump(retweet_number, f)
