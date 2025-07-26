import streamlit as st
import pickle
import pandas as pd

# Load data
popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('book.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Function to recommend books
def recommend(book_name):
    try:
        index = pt.index.get_loc(book_name)
    except KeyError:
        return None

    distances = similarity[index]
    book_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    data = []
    for i in book_list:
        title = pt.index[i[0]]
        temp_df = books[books['Book-Title'] == title].drop_duplicates('Book-Title')
        if not temp_df.empty:
            book_author = temp_df['Book-Author'].values[0]
            img_url = temp_df['Image-URL-M'].values[0]
            data.append((title, book_author, img_url))

    return data

# Page config
st.set_page_config(page_title="Book Recommender", layout="wide")

# Header
st.markdown("""
    <div style="background-color: #1f77b4; padding: 10px 20px; border-radius: 8px; display: flex; align-items: center; justify-content: space-between;">
        <h1 style="color: white; margin: 0;">📚 Book Recommender</h1>
        <div>
            <span style="margin-right: 20px;"><input type="radio" name="nav" value="Home" checked> Home</span>
            <span style="margin-right: 20px;"><input type="radio" name="nav" value="Recommend"> Recommend</span>
            <span><input type="radio" name="nav" value="Contact"> Contact</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# Navigation
selected = st.radio("Go to", ["Home", "Recommend", "Contact"], horizontal=True, label_visibility="collapsed")

# Home section
if selected == "Home":
    st.markdown("### ⭐ Top 50 Books")
    for i in range(0, len(popular_df), 5):
        cols = st.columns(5)
        for j in range(5):
            if i + j < len(popular_df):
                with cols[j]:
                    book = popular_df.iloc[i + j]
                    st.image(book['Image-URL-M'], use_container_width=True)
                    st.caption(f"**{book['Book-Title']}**\n\nAuthor: {book['Book-Author']}")
                    st.markdown(f"📊 Avg Rating: {book['avg_rating']:.2f} | 🗳️ Votes: {book['num_ratings']}")

# Recommend section
elif selected == "Recommend":
    st.markdown("### 🔍 Recommend Books")

    book_list = pt.index.tolist()
    selected_book = st.selectbox("Select a book", book_list)

    if st.button("Recommend"):
        recommended_books = recommend(selected_book)
        if recommended_books:
            st.markdown("### Top 5 Similar Books:")
            cols = st.columns(5)
            for i, book in enumerate(recommended_books):
                with cols[i]:
                    st.image(book[2], width=100)
                    st.caption(book[0])
        else:
            st.error("No recommendations found.")

# Contact section
elif selected == "Contact":
    st.markdown(
        """
        <div style="background-color: black; padding: 20px; border-radius: 10px;">
            <h2 style="color: white;">📞 Contact</h2>
            <p style="color: white;">👤 Name: Satyam Singh</p>
            <p style="color: white;">📧 Email: singhsatyam.0912@gmail.com</p>
            <p style="color: white;">🔗 GitHub: <a href="https://github.com/Satyam-Singh-x/Book-recommender-system.git" style="color: #1f77b4;" target="_blank">github.com/Satyam-Singh-x/Book-recommender-system</a></p>
        </div>
        """,
        unsafe_allow_html=True
    )
