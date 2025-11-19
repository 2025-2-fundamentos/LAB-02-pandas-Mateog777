import pandas as pd

def pregunta_11():
    df = pd.read_csv("files/input/tbl1.tsv", sep="\t")
    tabla = df.groupby("c0")["c4"].apply(lambda x: ",".join(sorted(x)))
    return tabla.reset_index()
