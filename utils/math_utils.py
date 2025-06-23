import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

def fetch_website_title(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.title.string if soup.title else 'No Title Found'

def calculate_mean(arr):
    return np.mean(arr)

def create_dataframe():
    data = {'name': ['Alice', 'Bob', 'Charlie'], 'score': [85, 90, 95]}
    df = pd.DataFrame(data)
    if 'score' in df.columns:
        return df
    return pd.DataFrame()

def generate_range(n):
    result = []
    for i in xrange(n):
        result.append(i * i)
    return result

def exception_handling_demo():
    try:
        return 10 / 0
    except ZeroDivisionError, e:
        return "Caught an error: %s" % str(e)
