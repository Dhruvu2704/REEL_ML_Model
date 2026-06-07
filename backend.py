from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests

poster_cache = {}
app = FastAPI()

# ✅ CORS (ONLY ONCE)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# LOAD DATA
# -------------------------------
movies = pd.read_csv("movies.csv")

cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()

similarity = cosine_similarity(vectors)

# 🔑 PUT YOUR REAL KEY HERE
API_KEY = "PASTE_YOUR_REAL_TMDB_KEY"

# -------------------------------
# FETCH POSTER (SAFE)
# -------------------------------
def fetch_poster(movie_title):

    # return cached poster if exists
    if movie_title in poster_cache:
        return poster_cache[movie_title]

    try:
        url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_title}"

        response = requests.get(url, timeout=3)
        data = response.json()

        if data.get("results"):
            poster_path = data["results"][0].get("poster_path")

            if poster_path:
                poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"

                # save in cache
                poster_cache[movie_title] = poster_url

                return poster_url

    except Exception as e:
        print("Poster fetch error:", e)

    fallback = "https://via.placeholder.com/300x450?text=No+Poster"

    poster_cache[movie_title] = fallback

    return fallback

# -------------------------------
# RECOMMEND FUNCTION 
# -------------------------------
def recommend(movie):
    movie = movie.lower()
    movies['title_lower'] = movies['title'].str.lower()

    matches = movies[movies['title_lower'].str.contains(movie)]

    if len(matches) == 0:
        return []

    index = matches.index[0]

    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    return [movies.iloc[i[0]].title for i in distances[1:6]]

# -------------------------------
# ROUTES
# -------------------------------


@app.get("/movies")
def get_movies():
    return {"movies": movies['title'].tolist()}

@app.get("/recommend")
def get_recommendations(movie: str):
    recs = recommend(movie)

    results = []
    for m in recs:
        results.append({
            "title": m,
            "poster": fetch_poster(m)
        })

    return {"recommendations": results}

from fastapi.staticfiles import StaticFiles

app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")