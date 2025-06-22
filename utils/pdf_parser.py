from pdfminer.high_level import extract_text
import tiktoken

def read_pdf(file_path):
    text = extract_text(file_path)
    return text

def chunk_text(text, max_tokens=500, overlap=50):
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    words = text.split()
    
    chunks = []
    start = 0
    while start < len(words):
        chunk = words[start:start + max_tokens]
        encoded_len = len(encoding.encode(" ".join(chunk)))
        
        while encoded_len > max_tokens:
            chunk = chunk[:-1]
            encoded_len = len(encoding.encode(" ".join(chunk)))
        
        chunks.append(" ".join(chunk))
        start += max_tokens - overlap
    
    return chunks
