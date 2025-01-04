from app.services.gemini_service import GeminiService
import os
from app.main.settings import Config

class GetStandardWordService():
    def __init__(self):
        self.gemini_service = GeminiService()
    
    def get_result(self, file_path, user_id):
        return None