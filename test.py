import pandas as pd 

print(pd.__version__)

df = pd.DataFrame([], columns=["pro", "fpr", "threshold"])

df = df._append({"pro": "aa", "fpr": "aa", "threshold": "aa"}, ignore_index=True)