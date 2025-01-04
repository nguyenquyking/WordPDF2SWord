from flask_restful import Resource
from flask import send_from_directory
from app.services.upload_file_service import FileService
import os
from werkzeug.utils import safe_join
from app.main.settings import Config

DATASET_FOLDER = os.path.abspath(os.path.join(Config.CHROMA_DB_PATH, 'files_upload'))
GET_FILE_ROUTE = '/get-file/<path:filename>'

class GetFile(Resource):
    def __init__(self):
        self.file_service = FileService(DATASET_FOLDER)

    def get(self, filename):
        # Ensure the requested file exists in the dataset folder
        if self.file_service.file_exists(filename):
            # Join the path safely to avoid directory traversal vulnerabilities
            path = safe_join(os.fspath(DATASET_FOLDER), os.fspath(filename))
            return send_from_directory(DATASET_FOLDER, filename, as_attachment=True)
        else:
            return {'message': 'File not found'}, 404