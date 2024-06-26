# -*- coding: utf-8 -*-
"""AI-Powered Document Processing Pipeline.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dkmKDmcEMXEgCsCNqVvX0kwIGpw6sEVB
"""

!pip install PyMuPDF
!pip install pytesseract
!pip install pdf2image
!pip install nltk


!apt-get install -y poppler-utils
!apt-get install -y tesseract-ocr


import fitz
import pytesseract
from pdf2image import convert_from_path
import nltk
import re


nltk.download('punkt')

# Function to convert PDF to text
def pdf_to_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

# Function to extract images from PDF
def pdf_to_images_ocr(pdf_path):
    images = convert_from_path(pdf_path)
    ocr_text = ""
    for image in images:
        ocr_text += pytesseract.image_to_string(image)
    return ocr_text


def preprocess_text(text):

    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    sentences = nltk.sent_tokenize(text)

    tokenized_text = [nltk.word_tokenize(sentence) for sentence in sentences]
    return tokenized_text


pdf_path = '/content/sample1.pdf'
text_from_pdf = pdf_to_text(pdf_path)
text_from_images = pdf_to_images_ocr(pdf_path)
combined_text = text_from_pdf + text_from_images
preprocessed_text = preprocess_text(combined_text)

print(preprocessed_text)

def process_pdf(pdf_path):
    text_from_pdf = pdf_to_text(pdf_path)
    text_from_images = pdf_to_images_ocr(pdf_path)
    combined_text = text_from_pdf + text_from_images
    preprocessed_text = preprocess_text(combined_text)
    return preprocessed_text

pdf_path = '/content/sample1.pdf'
final_processed_text = process_pdf(pdf_path)

for sentence in final_processed_text:
    print(' '.join(sentence))

from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("t5-base")


def extract_information(text):
    nlp = pipeline("ner", model=model, tokenizer=tokenizer)
    return nlp(text)

def classify_document(text):
    classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)
    return classifier(text)

# Function to translate text
def translate_text(text, target_language="es"):
    # T5 is versatile and can handle tasks like translation with task-specific prefixes
    input_text = f"translate English to {target_language}: {text}"
    inputs = tokenizer(input_text, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(inputs["input_ids"], max_length=512, num_beams=4, early_stopping=True)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

!pip install streamlit --quiet
!pip install --upgrade streamlit
!pip install PyMuPDF pdf2image pytesseract transformers nltk --quiet
!pip install pyngrok --quiet

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st
# import fitz  # PyMuPDF
# from pdf2image import convert_from_path
# import pytesseract
# import nltk
# import re
# from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
# 
# # Functions for processing
# def pdf_to_text(pdf_path):
#     doc = fitz.open(pdf_path)
#     text = ""
#     for page_num in range(len(doc)):
#         page = doc.load_page(page_num)
#         text += page.get_text()
#     return text
# 
# def pdf_to_images_ocr(pdf_path):
#     images = convert_from_path(pdf_path)
#     ocr_text = ""
#     for image in images:
#         ocr_text += pytesseract.image_to_string(image)
#     return ocr_text
# 
# def preprocess_text(text):
#     nltk.download('punkt', quiet=True)
#     text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
#     sentences = nltk.sent_tokenize(text)
#     tokenized_text = [nltk.word_tokenize(sentence) for sentence in sentences]
#     return tokenized_text
# 
# tokenizer = AutoTokenizer.from_pretrained("t5-base")
# model = AutoModelForSeq2SeqLM.from_pretrained("t5-base")
# 
# def extract_information(text):
#     nlp = pipeline("ner", model=model, tokenizer=tokenizer)
#     return nlp(text)
# 
# def classify_document(text):
#     classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)
#     return classifier(text)
# 
# def translate_text(text, target_language="es"):
#     input_text = f"translate English to {target_language}: {text}"
#     inputs = tokenizer(input_text, return_tensors="pt", max_length=512, truncation=True)
#     outputs = model.generate(inputs["input_ids"], max_length=512, num_beams=4, early_stopping=True)
#     return tokenizer.decode(outputs[0], skip_special_tokens=True)
# 
# def process_pdf(pdf_path):
#     text_from_pdf = pdf_to_text(pdf_path)
#     text_from_images = pdf_to_images_ocr(pdf_path)
#     combined_text = text_from_pdf + text_from_images
#     preprocessed_text = preprocess_text(combined_text)
#     return preprocessed_text, combined_text
# 
# def main():
#     st.set_page_config(page_title="AI Document Processing", layout="wide", initial_sidebar_state="expanded")
#     st.title("📝 AI-Powered Document Processing Pipeline")
#     st.write("Upload a document to process.")
# 
#     uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
# 
#     if uploaded_file is not None:
#         with open("uploaded_file.pdf", "wb") as f:
#             f.write(uploaded_file.getbuffer())
# 
#         st.write("Processing the document...")
#         preprocessed_text, combined_text = process_pdf("uploaded_file.pdf")
# 
#         st.subheader("Extracted Text:")
#         st.text_area("Combined Text", combined_text, height=300)
# 
#         col1, col2, col3 = st.columns(3)
# 
#         with col1:
#             if st.button("Extract Information"):
#                 st.write("Extracting information...")
#                 extracted_info = extract_information(combined_text)
#                 st.write("Extracted Information:")
#                 st.json(extracted_info)
# 
#         with col2:
#             if st.button("Classify Document"):
#                 st.write("Classifying document...")
#                 classification = classify_document(combined_text)
#                 st.write("Document Classification:")
#                 st.json(classification)
# 
#         with col3:
#             if st.button("Translate Text"):
#                 st.write("Translating text...")
#                 translated_text = translate_text(combined_text)
#                 st.write("Translated Text:")
#                 st.text_area("Spanish Translation", translated_text, height=200)
# 
# if __name__ == "__main__":
#     main()
#

!streamlit run app.py & npx localtunnel --port 8501