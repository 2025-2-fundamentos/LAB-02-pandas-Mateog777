import pandas as pd

def pregunta_09():
    df = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    df["year"] = df["c3"].str.slice(0, 4)
    return df
