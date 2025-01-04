from pdf2docx import Converter
import os

class PdfToWordService:
    def __init__(self):
        pass

    def convert_pdf_to_word(self, pdf_path, word_path=None):
        # Determine the Word file path if not provided
        if word_path is None:
            base_name = os.path.splitext(os.path.basename(pdf_path))[0]  # Get the file name without extension
            word_path = os.path.join(os.path.dirname(pdf_path), f"{base_name}.docx")
        
        # Convert PDF to Word
        cv = Converter(pdf_path)
        cv.convert(word_path, start=0, end=None)
        cv.close()
        
        return word_path