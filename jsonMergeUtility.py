import sys
import pandas as pd
import json

def merge(csvFile,sourcejson):
    df = pd.read_csv(csvFile, header=0, names=["stageDNIS", "prodDNIS"],)

    print(df)
    """for index, row in df.iterrows():
        print(f"StageDNIS: {row.Index}, ProdDNIS: {row.prodDNIS}")"""

    with open(sourcejson, "r") as read_file:
        data = json.load(read_file)

    for row in df.itertuples(index=False):
        stageNumber = "+" + str(row.stageDNIS)
        prodNumber = ((row.prodDNIS).replace("-", "")).replace(" ", "")
        print(f"StageDNIS: {stageNumber}, ProdDNIS: {prodNumber}")
        i = 0
        for item in data["seed"]:
            for k, v in item.items():
                if k == "contentKey" and v == stageNumber:
                    data["seed"][i]["contentKey"] = prodNumber
            i = i + 1

    with open("prod.json", "w") as read_file:
        json.dump(data, read_file)

if __name__== "__main__":
    merge(sys.argv[1],sys.argv[2])

