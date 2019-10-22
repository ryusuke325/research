import pymysql
import pickle
import datetime

con = pymysql.connect('localhost','root','3251006r','Flaming')
with con:
    tweet_number=[]
    #総日数の取得が必要
    cur_day = con.cursor()
    cur_day.execute("select count(distinct DATE(time)) from KyotoAnimation")
    all_days = cur_day.fetchone()[0]
    #始まりの日を取ってくる
    cur_start = con.cursor()
    cur_start.execute("select distinct DATE(time) from KyotoAnimation limit 1")
    start_day = cur_start.fetchone()[0]
    for i in range(all_days):
        end_day = start_day+datetime.timedelta(days=1)
        cur = con.cursor()
        sql = "select count(user_id) from KyotoAnimation where time > %s and time < %s "
        cur.execute(sql,(start_day,end_day))
        start_day = end_day
        tweet_number.append(cur.fetchone()[0])
    with open('/Users/ryusuke/Downloads/研究/date_number.pickle', 'wb') as f:
        pickle.dump(tweet_number, f)
    #parse("{:d}-{:d}-{:d} {:d}:{:d}:{:d}",t)

#これもしかしてgroupbyで出来た？？
# select count(time) from test group by date(time);
#これで出来る、、、
