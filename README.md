# Movie Recommendation System

A hybrid movie recommendation system built using Python that combines transformer-based semantic embeddings with fuzzy matching to deliver accurate and intelligent movie suggestions. The system understands movie context using deep learning embeddings and improves user input handling using approximate string matching.

---

## Features

- Hybrid recommendation system using semantic embeddings  
- Transformer-based text understanding using SentenceTransformer (SBERT)  
- Content-aware movie similarity using vector embeddings  
- Robust movie search using RapidFuzz (fuzzy matching)  
- Movie metadata processing (title, genres, overview)  
- Fast recommendation retrieval using precomputed embeddings  
- Movie posters and details fetched using TMDb API  
- Interactive web interface (Streamlit / Flask based on implementation)  

---

## Recommendation Method

The system uses a hybrid NLP and machine learning approach. Movie metadata such as title, genres, and overview are combined into a single text representation. A pretrained SentenceTransformer model (`all-MiniLM-L6-v2`) is used to generate dense semantic embeddings for each movie.

Instead of relying on keyword matching, similarity between movies is computed in embedding space, allowing the system to capture contextual and semantic relationships between movies.

To improve user experience, RapidFuzz is used for fuzzy matching of user input, enabling the system to handle misspelled or partial movie names effectively.

---

## Technologies Used

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- SentenceTransformers (SBERT)  
- RapidFuzz  
- Pickle  
- TMDb API  
- Streamlit / Flask  

---

## Project Structure
