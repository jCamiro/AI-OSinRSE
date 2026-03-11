## Overview

This assesment anayses 10 open access research papers in the AI filed using
Grobid.
The objective is to extract information from the files and generate:

1. Keyword cloud based on abstracts.
2. Visualization of the number of figures per article.
3. List of links found in each paper.

## Dataset

The analysis uses 10 open-access articles obtained from arXiv.

Each article was downloaded in PDF format and processed using Grobid
to generate TEI XML files.

The PDFs are located in:

assessment1/data/pdfs/

## Methodology and results

The analysis consists of the following steps:

1. PDF processing with Grobid to generate TEI XML files.
2. Extraction of abstracts from the XML files.
3. Generation of a keyword cloud from the abstracts.
4. Counting figures per article.
5. Extraction of links from the XML content.

The results are stored in the following directory:

assessment1/results/

## Validation

Validation was performed by manually inspecting several papers.

Abstract extraction was validated by comparing the extracted text
with the abstract shown in the original PDF.

Figure counting was validated by manually counting figures in selected
articles and comparing them with the values obtained from the TEI XML.

Link extraction was validated by verifying that the URLs detected in
the XML correspond to links present in the original articles.

## Reproducibility

To reproduce the analysis:

1. Install Python dependencies
2. Run Grobid server
3. Execute the scripts in the src folder

python assessment1/src/run_grobid.py
python assessment1/src/parse_abstracts.py
python assessment1/src/wordcloud_generator.py
python assessment1/src/count_figures.py
python assessment1/src/extract_links.py
