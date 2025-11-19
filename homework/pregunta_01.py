import pandas as pd

def pregunta_01():
    df = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    return df.shape[0]
