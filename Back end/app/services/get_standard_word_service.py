from app.services.gemini_service import GeminiService
from app.services.pdf_to_word_service import PdfToWordService
import os
from app.main.settings import Config

class GetStandardWordService():
    def __init__(self):
        self.gemini_service = GeminiService()
        self.pdf_to_word_service = PdfToWordService()
    
    def get_result(self, file_path):
        word_path = self.pdf_to_word_service.convert_pdf_to_word(file_path)
        return word_path