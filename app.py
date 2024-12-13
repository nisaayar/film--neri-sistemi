import tkinter as tk
from tkinter import messagebox
import sqlite3
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
def fetch_movies_from_db():
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()

    cursor.execute('SELECT title, genres, description FROM movies')
    rows = cursor.fetchall()

    movies = pd.DataFrame(rows, columns=['title', 'genres', 'description'])
    conn.close()
    return movies

movies = fetch_movies_from_db()

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['genres'] + " " + movies['description'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def recommend(movie_title):
    if movie_title not in movies['title'].values:
        return "Film bulunamadı."

    idx = movies.index[movies['title'] == movie_title][0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    top_indices = [i[0] for i in sim_scores[1:4]]
    recommended_movies = movies[['title', 'genres', 'description']].iloc[top_indices]

    recommendations_text = "\n\n".join(
        [f"Film: {row['title']}\nTürler: {row['genres']}\nAçıklama: {row['description']}" for _, row in
         recommended_movies.iterrows()]
    )

    return recommendations_text
def get_recommendations():
    user_input = entry.get()
    recommendations = recommend(user_input)
    if isinstance(recommendations, str):
        messagebox.showinfo("Sonuç", recommendations)
    else:
        messagebox.showinfo("Öneriler", recommendations)

root = tk.Tk()
root.title("Film Öneri Sistemi")
root.geometry("600x500")

label = tk.Label(root, text="Favori filminizi girin:", font=('Arial', 14))
label.pack(pady=10)
entry = tk.Entry(root, font=('Arial', 12), width=40)
entry.pack(pady=10)
button = tk.Button(root, text="Öneri Al", command=get_recommendations, font=('Arial', 12), bg="lightblue")
button.pack(pady=20)
root.mainloop()






