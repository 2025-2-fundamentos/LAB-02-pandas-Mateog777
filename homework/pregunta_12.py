import pandas as pd

def pregunta_12():
    df = pd.read_csv("files/input/tbl2.tsv", sep="\t")
    df["c5"] = df["c5a"] + ":" + df["c5b"].astype(str)
    tabla = df.sort_values("c5a").groupby("c0")["c5"].apply(lambda x: ",".join(x))
    return tabla.reset_index()
