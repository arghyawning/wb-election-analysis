import pandas as pd

# def sorting_dataframe():
df = pd.read_csv(
    "data_table.csv",
    names=[
        "Sr",
        "Candidate",
        "Constituency",
        "Party",
        "Criminal Case",
        "Education",
        "Total Assets",
        "Approx Assets",
        "Liabilities",
        "Approx Liabilities",
    ],
    delimiter=",",
)
df["Criminal Case"] = pd.to_numeric(df["Criminal Case"])
df = df.sort_values(by=["Criminal Case"])
df.to_csv("sorted_data_table.csv", index=False)
