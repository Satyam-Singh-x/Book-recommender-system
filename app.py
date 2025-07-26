import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load saved files
pt = pickle.load(open('pt.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity.pkl', 'rb'))
popularity_df = pickle.load(open('popular.pkl', 'rb'))
books=pickle.load(open('book.pkl', 'rb'))
# Streamlit App Title
st.markdown("""
    <style>
    .topbar {
        background-color: #1f77b4;
        padding: 0.5rem 1rem;
        border-radius: 0.5rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: white;
        margin-bottom: 20px;
    }
    .topbar h1 {
        font-size: 20px;
        margin: 0;
        padding: 0;
    }
    .topbar a {
        color: white;
        text-decoration: none;
        margin-left: 20px;
        font-weight: bold;
    }
    .topbar a:hover {
        text-decoration: underline;
    }
    </style>

    <div class="topbar">
        <h1>📚 Book Recommendation System</h1>
        <div>
            <a href="#home">Home</a>
            <a href="#recommend">Recommend</a>
            <a href="#contact">Contact</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- Home Section Anchor ---
st.markdown('<div id="home"></div>', unsafe_allow_html=True)

# --- Home Section: Top 50 Books ---
st.markdown("### 🔝 Discover the Most Popular Books")
st.header("🔥 Top 50 Most Popular Books")

for i in range(0, 50, 5):
    cols = st.columns(5)
    for j in range(5):
        if i + j < len(popularity_df):
            book = popularity_df.iloc[i + j]
            with cols[j]:
                st.image(book['Image-URL-M'], width=100)
                st.caption(f"**{book['Book-Title']}**")
                st.text(f"by {book['Book-Author']}")
                st.text(f"⭐ {round(book['avg_rating'], 2)} ({book['num_ratings']} ratings)")
# --- Recommend Section Anchor ---
st.markdown('<div id="recommend"></div>', unsafe_allow_html=True)
st.markdown("### 📖 Get Book Recommendations")

# Dropdown to select a book
selected_book = st.selectbox("Select a book you like:", pt.index)

# Recommend function
def recommend(book_name):
    index = pt.index.get_loc(book_name)
    distances = similarity_scores[index]
    book_indices = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]

    recommendations = []
    for i in book_indices:
        book_title = pt.index[i[0]]
        book_info = books[books['Book-Title'] == book_title].drop_duplicates('Book-Title')

        recommendations.append({
            'title': book_title,
            'author': book_info['Book-Author'].values[0],
            'image': book_info['Image-URL-M'].values[0]
        })

    return recommendations

# Show recommendations on button click
if st.button("Recommend"):
    recs = recommend(selected_book)

    st.subheader("📚 Books You Might Like:")

    cols = st.columns(5)
    for i, rec in enumerate(recs):
        with cols[i]:
            st.image(rec['image'], width=100)
            st.caption(f"**{rec['title']}**")
            st.text(f"by {rec['author']}")
