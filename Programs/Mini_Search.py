import tkinter as tk
from tkinter import scrolledtext

class MiniSearchEngine:
    def __init__(self, master):
        self.master = master
        master.title("MiniSearch Engine")

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Enter your search query:")
        self.label.pack()

        self.query_entry = tk.Entry(self.master, width=30)
        self.query_entry.pack()

        self.search_button = tk.Button(self.master, text="Search", command=self.search)
        self.search_button.pack()

        self.results_text = scrolledtext.ScrolledText(self.master, width=40, height=10)
        self.results_text.pack()

    def search(self):
        query = self.query_entry.get().lower()
        results = []

        # Example documents
        documents = [
            "Python is a powerful programming language.",
            "Tkinter is a GUI toolkit for Python.",
            "Search engines help find information on the web.",
            "Python developers create amazing projects."
        ]

        # Perform a simple keyword search
        for idx, doc in enumerate(documents, start=1):
            if query in doc.lower():
                results.append(f"Document {idx}: {doc}\n")

        # Display the results
        if results:
            result_text = "\n".join(results)
        else:
            result_text = "No results found."

        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, result_text)

# Create the Tkinter window
root = tk.Tk()
app = MiniSearchEngine(root)
root.mainloop()
