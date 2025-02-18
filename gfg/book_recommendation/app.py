import streamlit as st
import random
import pickle
import pandas as pd

def main():
    # Load processed data from Pickle
    try:
        books_names_list = pickle.load(open("artifacts3/books_names_list.pkl", "rb"))
        req_updated_books = pickle.load(open("artifacts3/req_updated_books.pkl", "rb"))
        st.success("📚 Book dataset loaded successfully!")
    except FileNotFoundError:
        st.error("⚠️ Pickle files not found! Ensure `data_upload.py` has been run.")
        books_names_list = []
        req_updated_books = pd.DataFrame()

    # Try importing the model (Handle missing model.pkl)
    try:
        model = pickle.load(open("artifacts3/model.pkl", "rb"))
        model_available = True
    except FileNotFoundError:
        model_available = False
        st.warning("⚠️ Model not available. Using random recommendations instead.")

    st.header("📚 Book Recommender System")

    # User selects a book
    if books_names_list:
        selected_book = st.selectbox("Select a book:", books_names_list)
    else:
        selected_book = None
        st.error("⚠️ No books available for selection. Please check your dataset.")

    # Collaborative Filtering Recommendation
    def get_collaborative_based_recommendations(selected_book, top_n):
        if not model_available:
            return random.sample(list(req_updated_books["isbn"]), min(top_n, len(req_updated_books)))

        if selected_book not in req_updated_books["title"].values:
            return []

        book_id = req_updated_books[req_updated_books["title"] == selected_book].index[0]

        try:
            n_neighbors = min(top_n, len(req_updated_books))
            distance, suggestion = model.kneighbors(book_id.reshape(1, -1), n_neighbors=n_neighbors)
            collab_books_isbn = suggestion[0]
        except Exception as e:
            st.error(f"⚠️ Error in collaborative filtering: {e}")
            return []

        return collab_books_isbn

    # Content-Based Recommendation
    def get_content_based_recommendations(title, top_n):
        if title not in req_updated_books["title"].values:
            return []

        index = req_updated_books[req_updated_books["title"] == title].index[0]

        try:
            similarity_scores = req_updated_books["rating"].values
            similar_indices = similarity_scores.argsort()[::-1][1:top_n + 1]
            content_books_isbn = req_updated_books.iloc[similar_indices]["isbn"].values
        except Exception as e:
            st.error(f"⚠️ Error in content-based filtering: {e}")
            return []

        return content_books_isbn

    # Hybrid Recommendation
    def hybrid_recommendations(selected_book, top_n):
        collab_books_isbn = get_collaborative_based_recommendations(selected_book, top_n)
        content_books_isbn = get_content_based_recommendations(selected_book, top_n)

        books_isbn = list(set(collab_books_isbn) | set(content_books_isbn))[:top_n]
        books = req_updated_books[req_updated_books["isbn"].isin(books_isbn)]

        if books.empty:
            st.warning("⚠️ No recommendations found. Showing random books instead.")
            return (
                random.sample(books_names_list, min(top_n, len(books_names_list))),
                ["https://dummyimage.com/100x150/000/fff&text=No Image"] * top_n,
                [["Unknown"]] * top_n,
                [0] * top_n,
            )

        books_titles = books["title"].tolist()
        books_urls = books["coverImg"].tolist() if "coverImg" in books.columns else ["https://dummyimage.com/100x150/000/fff&text=No Image"] * len(books_titles)
        books_genres = books["genres"].tolist() if "genres" in books.columns else [["Unknown"]] * len(books_titles)
        books_rating = books["rating"].tolist() if "rating" in books.columns else [0] * len(books_titles)

        return books_titles, books_urls, books_genres, books_rating

    # Display Recommendations
    if st.button("📖 Show Recommendation") and selected_book:
        recommended_books, books_url, books_genres, books_rating = hybrid_recommendations(selected_book, 6)
        cols = st.columns(5)

        for i in range(len(recommended_books)):
            with cols[i % 5]:  # Cycle through columns
                st.text(recommended_books[i])
                # Use a default image if the URL is invalid
                try:
                    st.image(books_url[i], width=120)
                except Exception:
                    st.image("https://dummyimage.com/100x150/000/fff&text=No Image", width=120)
                st.text(f"⭐ Rating: {books_rating[i]}")
                st.text(f"📌 Genre: {', '.join(books_genres[i])}")

    st.success("✅ App Loaded Successfully!")

if __name__ == "__main__":
    main()