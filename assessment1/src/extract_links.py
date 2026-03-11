from pathlib import Path
from bs4 import BeautifulSoup
import pandas as pd
import re

BASE_DIR = Path(__file__).resolve().parent.parent
input_dir = BASE_DIR / "data" / "tei_xml"
output_dir = BASE_DIR / "results"
output_dir.mkdir(parents=True, exist_ok=True)

rows = []
url_pattern = re.compile(r'https?://\S+')

for file_path in sorted(input_dir.glob("*.xml")):
    with open(file_path, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "xml")

    found_links = set()

    for ref in soup.find_all("ref"):
        target = ref.get("target")
        if target and (target.startswith("http://") or target.startswith("https://")):
            found_links.add(target.strip())

    full_text = soup.get_text(" ", strip=True)
    regex_links = url_pattern.findall(full_text)
    for link in regex_links:
        cleaned = link.strip().rstrip('.,);]')
        found_links.add(cleaned)

    if found_links:
        for link in sorted(found_links):
            rows.append({
                "paper": file_path.stem,
                "link": link
            })
    else:
        rows.append({
            "paper": file_path.stem,
            "link": ""
        })

df = pd.DataFrame(rows)

csv_path = output_dir / "links_per_article.csv"
df.to_csv(csv_path, index=False)

print(f"Saved links to: {csv_path}")
