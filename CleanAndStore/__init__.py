import datetime
import logging
import requests
import azure.functions as func
import pandas as pd


def main(myblob: func.InputStream, outputblob: func.Out[str]) -> None:
    df = pd.read_csv(myblob, sep=';')
    check_columns = ['DR', 'RH']
    df.dropna(subset=check_columns, inplace=True)
    csv = df.to_csv(sep=';', index=False)
    outputblob.set(csv)
