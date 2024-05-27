import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from server.id_generator import generate_unique_id

class Server:
    def __init__(self):
        self.server_id = generate_unique_id()
        self.documents = {}
        self.users = {}
        self.networked_servers = []

    def register_user(self, user):
        self.users[user.user_id] = user

    def add_document(self, document):
        self.documents[document.document_id] = document

    def retrieve_document(self, document_id):
        return self.documents.get(document_id, None)

    def network_with(self, other_server):
        self.networked_servers.append(other_server)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

if __name__ == "__main__":
    server = Server()
    print("Server Initialized with ID:", server.server_id)
