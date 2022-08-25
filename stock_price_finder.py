import FinanceDataReader as fdr
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# data = pd.read_csv('data.csv')
# data = data.replace(' ', np.NaN)
# data = data.dropna()
#
# data.to_csv("./clear.csv",encoding="utf-8-sig")

from dateutil.relativedelta import relativedelta
from datetime import date
import datetime

data = pd.read_csv('clear.csv', thousands=',')

y = []
index = []

# 범위 설정 파라미터
month = 1
date_min = datetime.datetime(2019, 1, 1)
date_max = datetime.datetime(2022, 1, 1)
cost_min = 0
cost_max = 500000
comp_min = 1000
comp_max = 10000

for i in range(1, len(data)):

    #특정 주식 출력
    # i=11
    # print(str(data.iloc[i]['code']))

    #주식 정보 전처리
    code = str(data.iloc[i]['code'])
    cost = int(data.iloc[i]['cost'])

    competitive_rate = str(data.iloc[i]['competitive rate'])
    competitive_rate = competitive_rate.split(':')[0]
    competitive_rate = competitive_rate.replace(';1', '')
    competitive_rate = competitive_rate.replace(',', '')
    competitive_rate = float(competitive_rate)

    newData = str(data.iloc[i]['date']).replace('.', '-')
    newData = newData.replace(' ', '')
    newData = datetime.datetime.strptime(newData, '%Y-%m-%d')

    # 범위 검사
    if (newData < date_min) | (newData > date_max):
        continue

    if (cost < cost_min) | (cost > cost_max):
        continue

    if (competitive_rate < comp_min) | (competitive_rate > comp_max):
        continue

    afterData = newData + relativedelta(months=month)

    # 값이 온전하지 않은 주식 제외
    df = fdr.DataReader(code, newData, afterData)

    if len(df) != 0:
        if df["Close"][0]/cost > 2.3:
            continue



        temp = []
        for j in range(len(df["Close"])):
            temp.append(df["Close"][j]/cost)
        y.append(temp)
        print(f"{i} Done")

hh = pd.DataFrame(y)
hh.to_csv("./forGraph.csv", encoding="utf-8-sig")

