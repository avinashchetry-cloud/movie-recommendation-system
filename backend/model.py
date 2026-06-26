from rapidfuzz import process
import pickle
import random


movies = pickle.load(open('models/movie_df.pkl', 'rb'))
similarity = pickle.load(open('models/similarity.pkl', 'rb'))


def find_closest(title):
    titles = movies['title'].tolist()

    match, score, _ = process.extractOne(title, titles)
    
    if score < 60:
        return None
    
    return match



def recommend(title):


    closest_title = find_closest(title)

    if not closest_title:
        print("No match found for:", title)
        return random.sample(list(movies['title']), 5)

    print("User input:", title)
    print("Matched with:", closest_title)


    idx = movies[movies['title'] == closest_title].index[0]


    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)


    filtered = [s for s in scores if s[1] > 0.1]


    if len(filtered) <= 1:
        print("Weak similarity, using fallback")
        return random.sample(list(movies['title']), 5)

    top_movies = filtered[1:6]

    recommendations = []

    for i in top_movies:
        recommendations.append(movies.iloc[i[0]].title)

    return recommendations
