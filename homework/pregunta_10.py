import pandas as pd

def pregunta_10():
    df = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    serie = df.groupby("c1")["c2"].apply(lambda x: ":".join(str(v) for v in sorted(x)))
    serie.index.name = "_c1"
    return serie.to_frame(name="c2")
