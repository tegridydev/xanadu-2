import os
import json

class StorageManager:
    def __init__(self, storage_path):
        self.storage_path = storage_path
        if not os.path.exists(self.storage_path):
            os.makedirs(self.storage_path)

    def store_document(self, document):
        document_path = os.path.join(self.storage_path, document.document_id)
        with open(document_path, 'w') as file:
            json.dump(document.to_json(), file)

    def retrieve_document(self, document_id):
        document_path = os.path.join(self.storage_path, document_id)
        if os.path.exists(document_path):
            with open(document_path, 'r') as file:
                return json.load(file)
        return None

    def manage_storage(self):
        # TO:DO:Implement storage management 
        pass

if __name__ == "__main__":
    sm = StorageManager("/path/to/storage")
    print("Storage Manager Initialized")
