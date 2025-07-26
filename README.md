📚 Book Recommender System

A personalized Book Recommendation Web App built with Streamlit, offering recommendations based on collaborative filtering. The app showcases the Top 50 Most Popular Books and recommends similar books based on user ratings using cosine similarity.

Live Demo Link: https://book-recommender-system-bysatyam.streamlit.app/#contact

🚀 Features

🎯 Top 50 Popular Books displayed with cover images

🔍 Book Recommendations using similarity scores

✅ Clean and responsive UI with navigation (Home, Recommend, Contact)

🧠 Built using pandas, scikit-learn, numpy, Streamlit





📁 Book-Recommender-System

├── app.py                 # Main Streamlit app

├── books.csv              # Books dataset

├── ratings.csv            # Ratings dataset

├── users.csv              # Users dataset

├── similarity.pkl         # Pickled similarity matrix

├── pt.pkl                 # Pivot table (user-item matrix)

├── popular_df.pkl         # Pickled top 50 books dataframe

├── requirements.txt       # Required Python packages

└── README.md              # This file

🔧 Setup & Run Locally

1. Clone the repo
   
bash

git clone https://github.com/Satyam-Singh-x/Book-recommender-system.git

cd Book-recommender-system

3. Create a virtual environment and activate it
bash

python -m venv venv

venv\Scripts\activate  # On Windows

3. Install dependencies
   
bash

pip install -r requirements.txt

5. Run the Streamlit app
   
bash

streamlit run app.py
🤖 Recommendation System Logic
Constructed a user-book rating matrix (pivot table).

Filtered books with 35+ ratings from users who rated 200+ books.

Used cosine similarity on the matrix to find similar books.

Recommendations are based on collaborative filtering.

📬 Contact

👤 Satyam Singh

📧 Email: singhsatyam.0912@gmail.com

🔗 GitHub: Satyam-Singh-x

📌 TODO / Future Improvements

Add book descriptions, genres, and author bios

Integrate content-based filtering (NLP-based)

Enable user login and personalized dashboards

Deploy to Streamlit Cloud or Heroku

⭐ Show Some Love

If you found this helpful or cool, leave a ⭐ on the repo.

It motivates me to build more awesome stuff! 💙

