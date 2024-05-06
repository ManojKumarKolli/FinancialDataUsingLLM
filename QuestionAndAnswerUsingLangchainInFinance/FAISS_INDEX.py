import requests
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
import pickle
import openai
from transformers import pipeline
from langchain.text_splitter import RecursiveCharacterTextSplitter
from extract_urls import fetch_article_url
import json

def fetch_article_content(url):
    """Fetch article content from URLs."""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text(separator=" ", strip=True)
    return text

# def chunk_articles(articles_text):
#     """Chunk articles."""
#     r_splitter = RecursiveCharacterTextSplitter(
#         separators=["\n\n", "\n", " "],
#         chunk_size=200,
#         chunk_overlap=0,
#         length_function=len
#     )
#     return [chunk for article in articles_text for chunk in r_splitter.split_text(article)]

def chunk_articles(articles_with_urls):
    """Chunk articles along with their source URLs."""
    r_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", " "],
        chunk_size=200,
        chunk_overlap=0,
        length_function=len
    )
    all_chunks_with_urls = []
    for article_text, url in articles_with_urls:
        chunks = r_splitter.split_text(article_text)
        for chunk in chunks:
            all_chunks_with_urls.append((chunk, url))
    return all_chunks_with_urls


# def create_and_save_faiss_index(chunked_articles, filename="faiss_index.pkl"):
#     """Create and save FAISS index and embeddings."""
#     model = SentenceTransformer('all-mpnet-base-v2')
#     embeddings = model.encode(chunked_articles)
#     index = faiss.IndexFlatL2(embeddings.shape[1])
#     index.add(embeddings)
#
#     with open(filename, "wb") as f:
#         pickle.dump((index, chunked_articles), f)

def create_and_save_faiss_index(chunked_articles_with_urls, filename="faiss_index.pkl"):
    # Extract chunks and URLs
    chunks, urls = zip(*chunked_articles_with_urls)
    model = SentenceTransformer('all-mpnet-base-v2')
    embeddings = model.encode(list(chunks))
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    # Save both the FAISS index and the URLs
    with open(filename, "wb") as f:
        pickle.dump((index, list(urls), list(chunks)), f)  # Now saving chunks and URLs as well


# def load_faiss_index(filename="faiss_index.pkl"):
#     """Load FAISS index and embeddings from disk."""
#     with open(filename, "rb") as f:
#         return pickle.load(f)

def load_faiss_index(filename="faiss_index.pkl"):
    with open(filename, "rb") as f:
        index, urls, chunks = pickle.load(f)
    return index, urls, chunks  # Adjusted to return chunks and URLs



# def update_faiss_index():
#     # fetch past 30 days urls from the moneycontrol.com
#     urls = fetch_article_url()
#
#     print("Total Collected Articles:", len(urls))
#
#     # Fetch each article content from the article
#     articles_text = [fetch_article_content(url) for url in urls]
#
#     # create the chunks of the article
#     chunked_articles = chunk_articles(articles_text)
#
#     print("Total Documents created:", len(chunked_articles))
#
#     # Save metrics
#     file_info = {}
#     file_info["Total Collected Articles"] = len(urls)
#     file_info["urls"] = urls
#     with open("file_info.json", "w") as outfile:
#         json.dump(file_info, outfile)
#
#
#     # Save the FAISS Index
#     create_and_save_faiss_index(chunked_articles)

def update_faiss_index():
    # Fetch URLs of the past 30 days from moneycontrol.com
    urls = fetch_article_url()
    print("Total Collected Articles:", len(urls))

    # Pair each article text with its URL
    articles_with_urls = [(fetch_article_content(url), url) for url in urls]

    # Create chunks of the articles along with their URLs
    chunked_articles_with_urls = chunk_articles(articles_with_urls)
    print("Total Documents created:", len(chunked_articles_with_urls))

    # Adjust the structure for embeddings and save the FAISS index along with URLs
    create_and_save_faiss_index(chunked_articles_with_urls)

    # Save metadata
    file_info = {
        "Total Collected Articles": len(urls),
        "urls": urls
    }
    with open("file_info.json", "w") as outfile:
        json.dump(file_info, outfile)

