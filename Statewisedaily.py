import pandas as pd
import numpy as np

def transform(df,text):
    lst=[]
    dates=df['date']
    df.drop(['status','date','total'],axis=1,inplace=True)
    for i,dt in enumerate(dates):
        for j,col in enumerate(df.columns):
            lst.append([dt,col,df.iloc[i,j]])
    df = pd.DataFrame(lst)
    df.columns=['Date','State',text]
    return df

def main():
    import urllib.request, json 
    with urllib.request.urlopen("https://api.covid19india.org/states_daily.json") as url:
        data = json.loads(url.read().decode())
        df=pd.DataFrame(data["states_daily"])
        df_conf = df[df['status']=='Confirmed']
        df_rec = df[df['status']=='Recovered']
        df_death = df[df['status']=='Deceased']
        df_conf=transform(df_conf,'Confirmed')
        df_rec=transform(df_rec,'Recovered')
        df_death=transform(df_death,'Deaths')
        df = df_conf.merge(df_rec,how='left',on=['Date','State'])
        df = df.merge(df_death,how='left',on=['Date','State'])
        df.to_csv('.\\statedaily.csv',index=False)
if __name__ == '__main__':
    main()

