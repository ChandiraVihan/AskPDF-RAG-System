import os
from langchain_community.document_loaders import PyPDFLoader

# load a PDF and print its text
def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    pages = loader.load()
    print(f"Loaded {len(pages)} pages")
    print("Page 1 content:", pages[0].page_content[:100]) # Print first 100 chars

if __name__ == "__main__":
    # Dummy pdf to test
    load_pdf("test_lecture.pdf")