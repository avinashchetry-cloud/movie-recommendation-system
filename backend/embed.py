import pandas as pd
import pickle
from sentence_transformers import SentenceTransformer

df = pd.read_csv('data/movies_df.csv')

df = df.drop_duplicates()

df['overview'] = df['overview'].fillna('')
df['genres'] = df['genres'].fillna('')

df['text'] = df['title'] + " " + df['genres'] + " " + df['overview']

model = SentenceTransformer('all-MiniLM-L6-v2')

embeddings = model.encode(df['text'].tolist(), show_progress_bar=True)

pickle.dump(embeddings, open('models/embeddings.pkl', 'wb'))
pickle.dump(df, open('models/movie_df.pkl', 'wb'))
