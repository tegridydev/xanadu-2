import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'server')))
from id_generator import generate_unique_id
from document.link import Link

class Document:
    def __init__(self, title, content, owner_id):
        self.document_id = generate_unique_id()
        self.title = title
        self.content = content
        self.owner_id = owner_id
        self.parts = []
        self.links = []

    def add_part(self, part):
        self.parts.append(part)

    def add_link(self, link):
        self.links.append(link)

    def to_json(self):
        return json.dumps({
            "document_id": self.document_id,
            "title": self.title,
            "content": self.content,
            "owner_id": self.owner_id,
            "parts": self.parts,
            "links": [link.to_dict() for link in self.links]
        })

    @staticmethod
    def from_json(json_data):
        data = json.loads(json_data)
        document = Document(data['title'], data['content'], data['owner_id'])
        document.document_id = data['document_id']
        document.parts = data['parts']
        document.links = [Link.from_dict(link) for link in data['links']]
        return document

if __name__ == "__main__":
    doc = Document("Sample Title", "Sample Content", "Owner ID")
    print("Document Initialized with ID:", doc.document_id)
