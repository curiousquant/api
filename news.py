#https://www.kaggle.com/code/robikscube/sentiment-analysis-python-youtube-tutorial

import pandas as pd
import requests
from config import settings


def readSite():
    key = settings.API_KEY
    x = requests.get('https://api.nytimes.com/svc/topstories/v2/home.json?api-key='+key)
    df = pd.DataFrame(x.json()['results'])
    
    print(df.head())
    return df

def readcsv(file):
    df = pd.read_csv(file)
    # Read in data
    print(df.shape)
    return df

#df = readcsv('./input/Reviews.csv')

df = readSite()
print(df.to_json('temp.json', orient='records', lines=True))
