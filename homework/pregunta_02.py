import pandas as pd

def pregunta_02():
    df = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    return df.shape[1]
