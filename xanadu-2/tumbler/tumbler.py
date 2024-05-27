class Tumbler:
    def __init__(self, author, document_id, document_version, byte_span, links):
        self.author = author
        self.document_id = document_id
        self.document_version = document_version
        self.byte_span = byte_span
        self.links = links

    def generate_address(self):
        return f"{self.author}.{self.document_id}.{self.document_version}.{self.byte_span}.{'.'.join(self.links)}"

    @staticmethod
    def parse_address(address):
        parts = address.split('.')
        author = parts[0]
        document_id = parts[1]
        document_version = parts[2]
        byte_span = parts[3]
        links = parts[4:]
        return Tumbler(author, document_id, document_version, byte_span, links)

    def validate_address(self):
        if not all([self.author, self.document_id, self.document_version, self.byte_span]):
            raise ValueError("Invalid tumbler address components")
        if not isinstance(self.links, list):
            raise ValueError("Links must be a list")

if __name__ == "__main__":
    tumbler = Tumbler("AuthorID", "DocID", "1.0", "0-100", ["LinkID1", "LinkID2"])
    address = tumbler.generate_address()
    print("Generated Tumbler Address:", address)
    parsed_tumbler = Tumbler.parse_address(address)
    print("Parsed Tumbler Address:", parsed_tumbler.generate_address())
    try:
        parsed_tumbler.validate_address()
        print("Address is valid")
    except ValueError as e:
        print("Address validation error:", e)
