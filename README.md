# Keyword Extraction System

## Description

This project extracts important keywords and phrases from a given text using Natural Language Processing.

## Technologies Used

- Python
- Natural Language Processing
- RAKE Algorithm
- rake-nltk

## How It Works

1. The user enters a paragraph.
2. The text is analyzed using the RAKE algorithm.
3. Common stop words are removed.
4. Important keywords and phrases are ranked.
5. The top keywords are displayed.

## Installation

```bash
pip install rake-nltk
python -m nltk.downloader stopwords punkt