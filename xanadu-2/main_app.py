import os
from server.server import Server
from user.user import User
from document.document import Document
from server.auth import AccessControl
from tumbler.tumbler import Tumbler
from document.storage_manager import StorageManager

class MainApp:
    def __init__(self, storage_path):
        self.server = Server()
        self.storage_manager = StorageManager(storage_path)
        self.access_control = AccessControl()
        self.current_user = None

    def register_user(self, username):
        user = User(username)
        self.server.register_user(user)
        return user

    def login_user(self, username):
        for user in self.server.users.values():
            if user.username == username:
                self.current_user = user
                return user
        return None

    def create_document(self, title, content):
        if not self.current_user:
            raise ValueError("No user logged in")
        document = self.current_user.create_document(title, content)
        self.server.add_document(document)
        self.storage_manager.store_document(document)
        self.access_control.grant_permission(self.current_user.user_id, document.document_id)
        return document

    def retrieve_document(self, document_id):
        if not self.current_user:
            raise ValueError("No user logged in")
        if self.access_control.check_permission(self.current_user.user_id, document_id):
            document_json = self.storage_manager.retrieve_document(document_id)
            if document_json:
                return Document.from_json(document_json)
        return None

    def list_documents(self):
        if not self.current_user:
            raise ValueError("No user logged in")
        return [doc for doc in self.current_user.documents]

    def edit_document(self, document_id, new_title, new_content):
        if not self.current_user:
            raise ValueError("No user logged in")
        document = self.retrieve_document(document_id)
        if document:
            document.title = new_title
            document.content = new_content
            self.storage_manager.store_document(document)
            return document
        return None

    def create_link(self, source_document_id, target_document_id, link_type):
        if not self.current_user:
            raise ValueError("No user logged in")
        source_document = self.retrieve_document(source_document_id)
        target_document = self.retrieve_document(target_document_id)
        if source_document and target_document:
            link = Link(target_document_id, link_type)
            source_document.add_link(link)
            self.storage_manager.store_document(source_document)
            return link
        else:
            raise ValueError("Source or target document not found")

import tkinter as tk
from tkinter import messagebox, ttk

class MainAppGUI:
    def __init__(self, root, app):
        self.app = app
        self.root = root
        self.root.title("Xanadu Hypertext System")
        
        # Frame for user actions
        user_frame = tk.Frame(root)
        user_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.username_label = tk.Label(user_frame, text="Username:")
        self.username_label.grid(row=0, column=0)
        self.username_entry = tk.Entry(user_frame)
        self.username_entry.grid(row=0, column=1)
        self.register_button = tk.Button(user_frame, text="Register", command=self.register_user)
        self.register_button.grid(row=0, column=2)
        self.login_button = tk.Button(user_frame, text="Login", command=self.login_user)
        self.login_button.grid(row=0, column=3)
        self.current_user_label = tk.Label(user_frame, text="Current User: None")
        self.current_user_label.grid(row=0, column=4)

        # Frame for document actions
        doc_frame = tk.LabelFrame(root, text="Document Actions")
        doc_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.title_label = tk.Label(doc_frame, text="Document Title:")
        self.title_label.grid(row=0, column=0)
        self.title_entry = tk.Entry(doc_frame)
        self.title_entry.grid(row=0, column=1)

        self.content_label = tk.Label(doc_frame, text="Document Content:")
        self.content_label.grid(row=1, column=0)
        self.content_text = tk.Text(doc_frame, height=10, width=40)
        self.content_text.grid(row=1, column=1, columnspan=3)

        self.create_doc_button = tk.Button(doc_frame, text="Create Document", command=self.create_document)
        self.create_doc_button.grid(row=2, column=1)
        
        self.doc_listbox = tk.Listbox(doc_frame)
        self.doc_listbox.grid(row=3, column=0, columnspan=2)
        self.view_doc_button = tk.Button(doc_frame, text="View Document", command=self.view_document)
        self.view_doc_button.grid(row=3, column=2)
        self.edit_doc_button = tk.Button(doc_frame, text="Edit Document", command=self.edit_document)
        self.edit_doc_button.grid(row=3, column=3)

        # Frame for link actions
        link_frame = tk.LabelFrame(root, text="Link Actions")
        link_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.link_doc_label = tk.Label(link_frame, text="Link to Document ID:")
        self.link_doc_label.grid(row=0, column=0)
        self.link_doc_entry = tk.Entry(link_frame)
        self.link_doc_entry.grid(row=0, column=1)
        self.link_type_label = tk.Label(link_frame, text="Link Type:")
        self.link_type_label.grid(row=0, column=2)
        self.link_type_entry = tk.Entry(link_frame)
        self.link_type_entry.grid(row=0, column=3)
        self.create_link_button = tk.Button(link_frame, text="Create Link", command=self.create_link)
        self.create_link_button.grid(row=1, column=1)
        self.explorer_button = tk.Button(link_frame, text="Open Explorer", command=self.open_explorer)
        self.explorer_button.grid(row=1, column=2)

    def register_user(self):
        username = self.username_entry.get()
        if username:
            user = self.app.register_user(username)
            messagebox.showinfo("Registration", f"User '{username}' registered with ID: {user.user_id}")
        else:
            messagebox.showwarning("Registration", "Please enter a username")

    def login_user(self):
        username = self.username_entry.get()
        if username:
            user = self.app.login_user(username)
            if user:
                self.current_user_label.config(text=f"Current User: {username}")
                self.update_doc_list()
                messagebox.showinfo("Login", f"User '{username}' logged in")
            else:
                messagebox.showwarning("Login", "Username not found")
        else:
            messagebox.showwarning("Login", "Please enter a username")

    def create_document(self):
        if not self.app.current_user:
            messagebox.showwarning("Create Document", "Please log in first")
            return

        title = self.title_entry.get()
        content = self.content_text.get("1.0", tk.END).strip()
        if title and content:
            document = self.app.create_document(title, content)
            self.update_doc_list()
            messagebox.showinfo("Create Document", f"Document '{title}' created with ID: {document.document_id}")
        else:
            messagebox.showwarning("Create Document", "Please enter both title and content")

    def update_doc_list(self):
        self.doc_listbox.delete(0, tk.END)
        if self.app.current_user:
            documents = self.app.list_documents()
            for doc in documents:
                self.doc_listbox.insert(tk.END, f"{doc.document_id}: {doc.title}")

    def view_document(self):
        selection = self.doc_listbox.curselection()
        if selection:
            doc_id = self.doc_listbox.get(selection[0]).split(":")[0]
            document = self.app.retrieve_document(doc_id)
            if document:
                self.title_entry.delete(0, tk.END)
                self.title_entry.insert(0, document.title)
                self.content_text.delete("1.0", tk.END)
                self.content_text.insert("1.0", document.content)
                messagebox.showinfo("View Document", f"Viewing document '{document.title}'")

    def edit_document(self):
        selection = self.doc_listbox.curselection()
        if selection:
            doc_id = self.doc_listbox.get(selection[0]).split(":")[0]
            new_title = self.title_entry.get()
            new_content = self.content_text.get("1.0", tk.END).strip()
            if new_title and new_content:
                document = self.app.edit_document(doc_id, new_title, new_content)
                self.update_doc_list()
                messagebox.showinfo("Edit Document", f"Document '{document.title}' updated")
            else:
                messagebox.showwarning("Edit Document", "Please enter both title and content")

    def create_link(self):
        if not self.app.current_user:
            messagebox.showwarning("Create Link", "Please log in first")
            return

        selection = self.doc_listbox.curselection()
        if selection:
            source_doc_id = self.doc_listbox.get(selection[0]).split(":")[0]
            target_doc_id = self.link_doc_entry.get()
            link_type = self.link_type_entry.get()
            if target_doc_id and link_type:
                try:
                    link = self.app.create_link(source_doc_id, target_doc_id, link_type)
                    messagebox.showinfo("Create Link", f"Link created with ID: {link.link_id}")
                except ValueError as e:
                    messagebox.showwarning("Create Link", str(e))
            else:
                messagebox.showwarning("Create Link", "Please enter both target document ID and link type")

    def open_explorer(self):
        explorer_window = tk.Toplevel(self.root)
        explorer_window.title("Document Explorer")
        explorer_canvas = tk.Canvas(explorer_window, bg="white", width=800, height=600)
        explorer_canvas.pack(fill="both", expand=True)

        documents = self.app.list_documents()
        doc_positions = {}

        for i, doc in enumerate(documents):
            x = 100 + (i % 4) * 150
            y = 100 + (i // 4) * 150
            doc_positions[doc.document_id] = (x, y)
            explorer_canvas.create_rectangle(x-50, y-50, x+50, y+50, fill="lightblue")
            explorer_canvas.create_text(x, y, text=doc.title)

            for link in doc.links:
                target_pos = doc_positions.get(link.target_document_id)
                if target_pos:
                    explorer_canvas.create_line(x, y, target_pos[0], target_pos[1], arrow=tk.LAST)

if __name__ == "__main__":
    storage_path = "./storage"
    app = MainApp(storage_path)

    root = tk.Tk()
    gui = MainAppGUI(root, app)
    root.mainloop()

