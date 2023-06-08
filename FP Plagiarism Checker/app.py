import os
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import Word2Vec
from sklearn.cluster import DBSCAN

# Mendapatkan teks dari dokumen
def get_text_from_documents(documents):
    texts = []
    for doc in documents:
        with open(doc, 'r', encoding='utf-8') as file:
            text = file.read()
            text = re.sub(r'\s+', ' ', text)  # Menghapus karakter whitespace yang berlebihan
            texts.append(text)
    return texts

# Membuat representasi vektor kata menggunakan Word2Vec
def create_word_embeddings(texts):
    sentences = [text.split() for text in texts]
    model = Word2Vec(sentences, min_count=1)
    return model

# Mendapatkan vektor teks menggunakan TF-IDF
def get_text_vectors(texts):
    vectorizer = TfidfVectorizer()
    text_vectors = vectorizer.fit_transform(texts).toarray()
    return text_vectors

# Melakukan clustering menggunakan algoritma DBSCAN
def perform_clustering(text_vectors):
    dbscan = DBSCAN(metric='cosine', eps=0.3, min_samples=2)
    cluster_labels = dbscan.fit_predict(text_vectors)
    return cluster_labels

# Melakukan deteksi plagiarisme
def detect_plagiarism(cluster_labels, documents, text_vectors):
    plagiarism_results = []
    num_docs = len(documents)
    for i in range(num_docs):
        for j in range(i+1, num_docs):
            if cluster_labels[i] == cluster_labels[j]:
                similarity = cosine_similarity([text_vectors[i]], [text_vectors[j]])[0][0]
                plagiarism_results.append((documents[i], documents[j], similarity))
    return plagiarism_results

# Daftar dokumen yang akan diperiksa plagiarismenya
documents = ['brian.txt', 'john.txt']

# Mendapatkan teks dari dokumen
texts = get_text_from_documents(documents)

# Membuat representasi vektor kata menggunakan Word2Vec
word_embeddings_model = create_word_embeddings(texts)

# Mengubah teks menjadi vektor menggunakan TF-IDF
text_vectors = get_text_vectors(texts)

# Melakukan clustering menggunakan algoritma DBSCAN
cluster_labels = perform_clustering(text_vectors)

# Melakukan deteksi plagiarisme
plagiarism_results = detect_plagiarism(cluster_labels, documents, text_vectors)

# Menampilkan hasil deteksi plagiarisme
for result in plagiarism_results:
    print("Similarity between", result[0], "and", result[1], "is", round(result[2]*100, 2), "%")
