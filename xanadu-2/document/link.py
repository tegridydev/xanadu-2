import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'server')))
from id_generator import generate_unique_id

class Link:
    def __init__(self, target_document_id, link_type):
        self.link_id = generate_unique_id()
        self.target_document_id = target_document_id
        self.link_type = link_type

    def to_dict(self):
        return {
            "link_id": self.link_id,
            "target_document_id": self.target_document_id,
            "link_type": self.link_type
        }

    @staticmethod
    def from_dict(link_data):
        return Link(link_data['target_document_id'], link_data['link_type'])

if __name__ == "__main__":
    link = Link("Target Document ID", "hyperlink")
    print("Link Initialized with ID:", link.link_id)
