class AccessControl:
    def __init__(self):
        self.permissions = {}

    def grant_permission(self, user_id, document_id):
        if document_id not in self.permissions:
            self.permissions[document_id] = []
        self.permissions[document_id].append(user_id)

    def check_permission(self, user_id, document_id):
        return user_id in self.permissions.get(document_id, [])

if __name__ == "__main__":
    ac = AccessControl()
    ac.grant_permission("User ID", "Document ID")
    print("Permission Granted")
