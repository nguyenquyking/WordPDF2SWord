from app.services.pdf_to_standardword_service import PdfToStandardWordService
import os

class GetStandardWordService():
    def __init__(self):
        self.pdf_to_standardword_service = PdfToStandardWordService()
    
    def get_result(self, file_path):
        word_path = self.pdf_to_standardword_service.convert_pdf_to_standardword(file_path)
        return word_path