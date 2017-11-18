import pandas as pd
import numpy as np
import tensorflow as tf

#定义常量
rnn_unit=10       #hidden layer units
input_size=7
output_size=1
lr=0.0006         #学习率
f=open('dataset.csv')
df=pd.read_csv(f)     #读入股票数据
data=df.iloc[:,2:10].values   #取第3-10列
