# BibTeX to CSV Batch Converter

This project features a Python script that automatically converts multiple BibTeX (`.bib`) files into individual CSVs and merges them into a single, consolidated dataset. 

## 📌 Motivation
This tool was originally developed to automate the data extraction and organization phase of a Systematic Mapping study focusing on Artificial Intelligence in business management. When retrieving literature from various academic databases (like Scopus, IEEE, Web of Science, or ACM), exporting data in BibTeX format is standard. This script eliminates the manual labor of converting and compiling these files, making it easier to filter, analyze, and remove duplicates using tabular data.

## 🚀 Features
- **Auto-discovery:** Automatically detects all `.bib` files within a specified directory.
- **Batch Processing:** Converts each BibTeX file into its own CSV file.
- **Data Consolidation:** Merges all generated dataframes into one final `base_artigos_unificada.csv` file.
- **Error Handling:** Built with `os.path.join` and `utf-8` encoding to prevent path errors and character encoding issues.

## 📋 Prerequisites
Make sure you have Python installed. You will need to install the following libraries:

```bash
pip install pandas bibtexparser
