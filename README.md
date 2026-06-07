# REEL_ML_Model# 🎬 REEL - AI Powered Movie Recommendation System

REEL is a Content-Based Movie Recommendation System that helps users discover movies similar to their favorite films using Machine Learning and Natural Language Processing (NLP).

The system analyzes movie metadata such as genres, keywords, cast members, and plot descriptions, converts them into numerical vectors, and recommends movies based on content similarity.

---

## 🚀 Features

- AI-powered movie recommendations
- Content-based filtering approach
- NLP using CountVectorizer
- Cosine Similarity recommendation engine
- FastAPI backend
- Netflix-inspired responsive UI
- TMDB API integration for movie posters
- Autocomplete movie search
- Lazy image loading
- Infinite scrolling
- Poster caching for improved performance

---

## 🛠️ Tech Stack

### Machine Learning
- Python
- Pandas
- Scikit-learn
- CountVectorizer
- Cosine Similarity

### Backend
- FastAPI
- Uvicorn
- Requests

### Frontend
- HTML5
- CSS3
- JavaScript

### APIs
- TMDB API

---

## 📊 Dataset

The project uses a movie dataset containing:

- Movie Title
- Genres
- Cast
- Keywords
- Overview / Storyline

These features are combined into a single **tags** column which is used for NLP preprocessing.

---

## ⚙️ How It Works

### Step 1: Data Preprocessing

- Clean movie metadata
- Combine relevant features into a single tags column
- Remove unnecessary words
- Convert text into vectors using CountVectorizer

### Step 2: Feature Extraction

CountVectorizer transforms textual movie information into numerical vectors.

### Step 3: Similarity Calculation

Cosine Similarity is used to calculate the similarity between movies.
