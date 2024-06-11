# AI-Powered-Document-Processing-Pipeline

AI-Powered Document Processing Pipeline
Overview
This project demonstrates an AI-powered pipeline for understanding and processing documents using advanced NLP techniques, Large Language Models (LLMs), and Optical Character Recognition (OCR). The pipeline can handle various document formats, particularly PDF files with both text and image content. It can extract essential information, classify documents, and translate text. The user interacts with the system through a user-friendly chatbot interface built with Streamlit.

Features
Document Conversion and OCR: Converts PDF files to text, extracts text from images within PDFs using OCR.
Preprocessing: Cleans, tokenizes, and segments the text for optimal NLP performance.
Information Extraction: Extracts key entities like names, dates, and locations.
Document Classification: Classifies documents into predefined categories.
Text Translation: Translates text into different languages.
User Interface: A Streamlit-based chatbot UI for user interaction.
Setup and Installation
Prerequisites
Python 3.7+
Google Colab (for running the project in a cloud environment)
GitHub account (for cloning the repository)
Clone the Repository
bash

Install Required Libraries
Install the necessary Python libraries:

bash

pip install streamlit PyMuPDF pytesseract pdf2image nltk transformers pyngrok
Additionally, you may need to install system dependencies for poppler-utils and tesseract-ocr:

bash

apt-get install -y poppler-utils
apt-get install -y tesseract-ocr
Download NLTK Data
python

import nltk
nltk.download('punkt')
Running the Application
Open Google Colab and upload the app.py file.
Install the required libraries in the Colab environment using the provided commands.
Run the Streamlit application and create a public URL using ngrok:
bash

!streamlit run app.py & npx localtunnel --port 8501
Usage
Uploading and Processing Documents
Upload Document: Click on the "Choose a PDF file" button to upload a PDF document.
View Extracted Text: The extracted text from the PDF and images will be displayed.
Extract Information: Click the "Extract Information" button to view extracted entities.
Classify Document: Click the "Classify Document" button to see the document classification.
Translate Text: Click the "Translate Text" button to translate the text into Spanish.
Streamlit Interface
The Streamlit interface provides a clean and intuitive UI for interacting with the document processing pipeline. Users can easily upload documents, view extracted text, and perform various NLP tasks with just a few clicks.

Project Structure
app.py: The main Streamlit application file.
requirements.txt: A list of required Python libraries.
README.md: Project documentation.
sample1.pdf: Sample PDF file for testing.


