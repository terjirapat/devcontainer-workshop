import time
import pandas as pd

def timing():
    time.sleep(1)
    print('hello after 1 sec')

def show_df():
    df = pd.DataFrame([1,2,3,4,5], columns=['numbers'])
    print(df)