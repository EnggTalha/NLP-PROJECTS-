Text Summarizer

This project is a Streamlit-based application that uses the TextRank algorithm to summarize input text. It leverages the spacy library and pytextrank for natural language processing and text summarization.

Features

Summarizes large pieces of text into concise, meaningful summaries.

Interactive web app interface using Streamlit.

Easy-to-use text input field for summarization.

Installation

Prerequisites

Python 3.7 or later.

Ensure pip is installed on your system.

Steps

Clone the repository or copy the project files.

Navigate to the project directory:

cd <project_directory>

Install the required dependencies:

pip install -r requirements.txt

Download the SpaCy language model:

python -m spacy download en_core_web_lg

Usage

Run the Streamlit app:

streamlit run textrank_summary.py

Open the provided local URL in your browser (e.g., http://localhost:8501).

Enter the text you want to summarize in the text area and click the Summarize button.

File Descriptions

textrank_summary.py: The main Python script containing the Streamlit app and text summarization logic.

requirements.txt: Contains the list of dependencies required for the project.

README.md: Documentation for setting up and using the project.