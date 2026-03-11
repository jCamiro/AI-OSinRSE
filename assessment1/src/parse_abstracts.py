from bs4 import BeautifulSoup
import os
import pandas as pd

input_folder = "../data/tei_xml"

abstracts = []

for file in os.listdir(input_folder):

    if file.endswith(".xml"):

        path = os.path.join(input_folder, file)

        with open(path) as f:
            soup = BeautifulSoup(f, "xml")

        abstract = soup.find("abstract")

        if abstract:
            text = abstract.text.strip()
        else:
            text = ""

        abstracts.append({
            "paper": file,
            "abstract": text
        })

df = pd.DataFrame(abstracts)

df.to_csv("../data/intermediate/abstracts.csv", index=False)

print("Abstracts extracted")
