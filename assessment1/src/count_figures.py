from pathlib import Path
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent.parent
input_dir = BASE_DIR / "data" / "tei_xml"
output_dir = BASE_DIR / "results"
output_dir.mkdir(parents=True, exist_ok=True)

rows = []

for file_path in sorted(input_dir.glob("*.xml")):
    with open(file_path, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "xml")

    figures = soup.find_all("figure")

    rows.append({
        "paper": file_path.stem,
        "figures": len(figures)
    })

df = pd.DataFrame(rows)

csv_path = output_dir / "figures_per_article.csv"
png_path = output_dir / "figures_per_article.png"

df.to_csv(csv_path, index=False)

plt.figure(figsize=(10, 6))
plt.bar(df["paper"], df["figures"])
plt.xticks(rotation=90)
plt.xlabel("Article")
plt.ylabel("Number of figures")
plt.title("Number of figures per article")
plt.tight_layout()
plt.savefig(png_path)
plt.close()

print(f"Saved CSV to: {csv_path}")
print(f"Saved figure to: {png_path}")
