import pandas as pd
import requests

response = requests.get('http://192.168.0.123:7888/home')
if response.status_code==200:
    data=response.json()
    df = pd.DataFrame(data)
    df = df[['이름','국어','영어','수학']]
    df['총점'] = df['국어']+df['영어']+df['수학']
    df['평균'] = df['총점']//3
    print(df)