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

table = pq.read_table('train.parquet')
df = table.to_pandas()
df = df.drop(columns=df.columns[[0,2,3]])
dfTrain = df[:2000]
dfTest = df[2000:2500]
dfTrain = cleanData(dfTrain)
dfTest  = cleanData(dfTest)
with open('train.txt', 'w',encoding='utf8') as ftxt:
    for row in dfTrain.itertuples():
        mes = str(getattr(row, 'text'))
        if len(mes)<256:
            continue
        ftxt.writelines(mes+ "\t__label__" + 'math' + "\n")
with open('test.txt', 'w',encoding='utf8') as ftxt:
    for row in dfTest.itertuples():
        mes = str(getattr(row, 'text'))
        if len(mes)<256:
            continue
        ftxt.writelines(mes+ "\t__label__" + 'math' + "\n")

table2 = pq.read_table('000_00000.parquet')
df = table2.to_pandas()
df = df.drop(columns=df.columns[[1,2,3]])
dfTrain = df[:2000]
dfTest = df[2000:2500]
dfTrain = cleanData(dfTrain)
dfTest  = cleanData(dfTest)
with open('train.txt', 'a',encoding='utf8') as ftxt:
    for row in dfTrain.itertuples():
        mes = str(getattr(row, 'text'))
        if len(mes)<256:
            continue
        ftxt.writelines(mes+ "\t__label__" + 'notmath' + "\n")
with open('test.txt', 'a',encoding='utf8') as ftxt:
    for row in dfTest.itertuples():
        mes = str(getattr(row, 'text'))
        if len(mes)<256:
            continue
        ftxt.writelines(mes+ "\t__label__" + 'notmath' + "\n")