from pathlib import Path
import pandas as pd
from wordcloud import WordCloud

BASE_DIR = Path(__file__).resolve().parent.parent
input_file = BASE_DIR / "data" / "intermediate" / "abstracts.csv"
output_dir = BASE_DIR / "results"
output_dir.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(input_file)

text = " ".join(df["abstract"].dropna().astype(str))

wordcloud = WordCloud(
    width=1200,
    height=600,
    background_color="white"
).generate(text)

output_file = output_dir / "keyword_cloud.png"
wordcloud.to_file(output_file)

print(f"Keyword cloud saved to: {output_file}")
