from flask import Flask, request, jsonify
from model import recommend
import requests
import urllib.parse

app = Flask(__name__)

API_KEY = "88866be496b8e9a4c37e23d8cd1ecff8" 

def get_movie_details(title):
    
    query = urllib.parse.quote(title)
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={query}"

    try:
        res = requests.get(url, timeout=5)

        if res.status_code != 200:
            print("TMDB error:", res.status_code)
            return None

        data = res.json()

        if not data['results']:
            print("No TMDB results for:", title)
            return None


        best_movie = None

        for m in data['results']:
            if m.get("poster_path") and m.get("vote_average", 0) > 5:
                best_movie = m
                break

        if not best_movie:
            best_movie = data['results'][0]

        print("Searching:", title)
        print("Selected:", best_movie.get("title"))

        poster_path = best_movie.get("poster_path")

        poster = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else None

        return {
            "title": best_movie.get("title"),
            "overview": best_movie.get("overview"),
            "release_date": best_movie.get("release_date"),
            "poster": poster
        }

    except Exception as e:
        print("API error:", e)

    return None


@app.route('/recommend', methods=['POST'])
def recommend_api():

    data = request.get_json()
    movie = data.get('movie')

    if not movie:
        return jsonify({"error": "No movie provided"}), 400

    recommendations = recommend(movie)

    results = []

    for rec in recommendations:
        details = get_movie_details(rec)
        if details:
            results.append(details)

    return jsonify({
        "movie": movie,
        "recommendations": results
    })


if __name__ == "__main__":
    app.run(debug=True)