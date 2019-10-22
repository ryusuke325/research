"""元がdfのpklファイルをロードして、ツイート数0の日もデータフレームに加える"""
def process(pklfile):
    with open(pklfile,'rb') as f:
        df = pickle.load(f)
    with open('time.pkl','rb') as f:
        df_time = pickle.load(f)
    df = pd.merge(df_time, df, on='date(time)',how='left')
    df= df.fillna(0.9)
    return df

"""dfの可視化"""
def visual(df_time_soku):
    fig = plt.figure(figsize=(10,7))
    ax = fig.add_subplot(111, xticks=df_time_soku['date(time)'][::10],xticklabels=df_time_soku['date(time)'][::10])
    ax.plot(df_time_soku['date(time)'] ,df_time_soku['count(time)'])
    #ax.set_yscale('log')
