# main.py

from src.loader import load_document
from src.chunker import chunk_text
def main ():
    path = "data/sample.txt"
    text = load_document(path)
    print("Document Length: ", len(text))
    
    chunks = chunk_text(text, chunk_size=500, overlap=100)
    print("No. of chunks: ", len(chunks))
    print("\nFirst 2 chunks:\n")
    print("Chunk 1:\n", chunks[0])
    print("Chunk 2:\n", chunks[1])
    print("Last chunk length: ", len(chunks[-1]))
    
    assert all(len(chunk.strip()) > 0 for chunk in chunks), "Empty chunk detected"
    
if __name__ == "__main__":
    main()
