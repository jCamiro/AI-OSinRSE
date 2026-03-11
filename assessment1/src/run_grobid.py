import requests
import os

GROBID_URL = "http://localhost:8070/api/processFulltextDocument"

input_folder = "../data/pdfs"
output_folder = "../data/tei_xml"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):

    if filename.endswith(".pdf"):

        pdf_path = os.path.join(input_folder, filename)

        with open(pdf_path, "rb") as pdf_file:

            response = requests.post(
                GROBID_URL,
                files={"input": pdf_file}
            )

        output_file = filename.replace(".pdf", ".tei.xml")

        with open(os.path.join(output_folder, output_file), "w") as f:
            f.write(response.text)

        print(f"Processed {filename}")
