# Movie Recommendation System

A content-based movie recommendation system built using Python, Flask, and scikit-learn. The application recommends similar movies based on content similarity and fetches movie posters and details using the TMDb API.

## Features

- Content-based movie recommendations
- Movie posters and details from the TMDb API
- Fast recommendations using a precomputed similarity matrix
- Simple and responsive web interface

## Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- Pickle
- TMDb API
- HTML
- CSS

## Project Structure

```
Movie-Recommendation-System/
│
├── app.py
├── model.py
├── movies.pkl
├── similarity.pkl
├── templates/
├── static/
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Add your TMDb API key in `app.py`:

```python
API_KEY = "YOUR_API_KEY"
```

Run the application:

```bash
python app.py
```

Open the application in your browser:

```
http://127.0.0.1:5000
```

## How It Works

1. The user selects a movie.
2. The application identifies similar movies using cosine similarity.
3. The TMDb API is used to retrieve posters and additional movie information.
4. The recommended movies are displayed in the web interface.

## Recommendation Method

The project uses a content-based filtering approach. Movie metadata is converted into feature vectors, and cosine similarity is used to measure similarity between movies. The most similar movies are returned as recommendations.

## Future Improvements

- Hybrid recommendation system
- Search autocomplete
- Genre and language filters
- User authentication
- User ratings and watchlist

## License

This project is intended for educational and learning purposes.
