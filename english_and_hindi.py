

import streamlit as st
import pytesseract
from PIL import Image
import os
os.system("apt-get update")
os.system("apt-get install -y tesseract-ocr")
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Hindi and English Text Extractor")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    file_size_mb = uploaded_file.size / (1024 * 1024)  
    if file_size_mb > 200:
        st.error("File size exceeds the 200MB limit.")
    else:
        try:
            
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            
            extracted_text = pytesseract.image_to_string(image, lang='hin+eng')

            st.subheader("Extracted Text:")
            st.text(extracted_text)
            keyword = st.text_input("Enter a keyword to search within the extracted text:")

            if keyword:
                if keyword in extracted_text:
                    
                    highlighted_text = extracted_text.replace(
                        keyword, f"<span style='color: red; font-weight: bold;'>{keyword}</span>"
                    )
                    st.subheader("Search Results:")
                    st.markdown(highlighted_text.replace("\n", "  \n"), unsafe_allow_html=True)
                else:
                    st.write("Keyword not found.")
        except pytesseract.pytesseract.TesseractNotFoundError:
            st.error("Tesseract not found. Please ensure it is installed and the path is configured correctly.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
