import uuid

def generate_unique_id():
    return str(uuid.uuid4())

if __name__ == "__main__":
    print("Server ID:", generate_unique_id())
    print("User ID:", generate_unique_id())
    print("Document ID:", generate_unique_id())
