import os
import requests
import numpy as np
import pandas as pd
import pyarrow.parquet as pq
import re

def cleanData(df):
    df = df.copy()
    df['text']=df['text'].apply(lambda x : re.sub(r'[^\w\s]', '', x))
    df['text']=df['text'].apply(lambda x : re.sub(r"[|( )'.%#&*=;:___]", ' ', x))
    df['text']=df['text'].apply(lambda x : re.sub(r"[\n]", ' ', x))
    df['text']=df['text'].apply(lambda x : re.sub(r'[^a-zA-Z0-9\s]', '', x))
    df['text']=df['text'].apply(lambda x : re.sub(r'\\u[0-9a-fA-F]{4}', '', x).strip())
    df['text']=df['text'].apply(lambda x : x[:256])
    return df

table2 = pq.read_table('000_00000.parquet')
df = table2.to_pandas()
df = df.drop(columns=df.columns[[1,2,3]])
dfTest = df[2000:7000]
dfTest  = cleanData(dfTest)

with open('predict.txt', 'w',encoding='utf8') as ftxt:
    for row in dfTest.itertuples():
        mes = str(getattr(row, 'text'))
        ftxt.writelines(mes + "\n")