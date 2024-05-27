import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'server')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'document')))
from id_generator import generate_unique_id
from document.document import Document

class User:
    def __init__(self, username):
        self.user_id = generate_unique_id()
        self.username = username
        self.documents = []

    def create_document(self, title, content):
        document = Document(title, content, self.user_id)
        self.documents.append(document)
        return document

    def retrieve_document(self, document_id):
        for doc in self.documents:
            if doc.document_id == document_id:
                return doc
        return None

if __name__ == "__main__":
    user = User("Alice")
    print("User Initialized with ID:", user.user_id)
