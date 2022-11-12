import requests
import json
import pandas as pd
import os
from io import StringIO

def handler():

    # League leaders
    google_sheet = {
        "id": os.environ.get('SHEET_ID'),
    }

    # Get the sheet as csv
    google_sheet_url = "https://docs.google.com/spreadsheets/d/" + google_sheet["id"] +"/gviz/tq?tqx=out:csv&sheet=League Leaders"
    res = requests.get(google_sheet_url)

    # pandas formatting
    csvStringIO = StringIO(res.text)
    table = pd.read_csv(csvStringIO, sep=",")

    # dataframe setup
    df = pd.DataFrame(table)
    df = df.dropna(axis='columns')

    # clean percentages
    percentCol = ['FG%', '3PT%', 'FT%']
    for p in percentCol:
        df[p] = df[p].str.rstrip('%').astype('float') / 100.0

    # save as json
    result = df.to_json(orient="split")

    with open('./res.json', 'w') as f:
        parsed = json.loads(result)
        json.dump(parsed, f)

    print(result)


handler()