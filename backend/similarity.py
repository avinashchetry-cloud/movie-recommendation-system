import pickle
from sklearn.metrics.pairwise import cosine_similarity

embeddings = pickle.load(open('models/embeddings.pkl', 'rb'))

similarity = cosine_similarity(embeddings)

pickle.dump(similarity, open('models/similarity.pkl', 'wb'))

print("Similarity ready")

