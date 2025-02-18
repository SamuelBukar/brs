import pickle
import streamlit as st
import pandas as pd
import os

# Ensure the artifacts3 folder exists
os.makedirs("artifacts3", exist_ok=True)

# Load books dataset from CSV
try:
    books_df = pd.read_csv("books_random_subset.csv")
    st.success("📂 CSV Data Loaded Successfully!")
except FileNotFoundError:
    st.error("⚠️ books_random_subset.csv not found! Ensure it's in the project folder.")
    books_df = pd.DataFrame()  # Create an empty DataFrame to avoid crashes

# Extract necessary columns (handle missing columns)
if not books_df.empty:
    books_df = books_df.fillna("Unknown")  # Replace NaN values with "Unknown"

    books_names_list = books_df["title"].tolist() if "title" in books_df.columns else []
    req_updated_books = books_df[["title", "isbn", "coverImg", "genres", "rating"]] if all(col in books_df.columns for col in ["title", "isbn", "coverImg", "genres", "rating"]) else pd.DataFrame()

    # Save extracted data as Pickle files for use in `app.py`
    pickle.dump(books_names_list, open("artifacts3/books_names_list.pkl", "wb"))
    pickle.dump(req_updated_books, open("artifacts3/req_updated_books.pkl", "wb"))

    st.success("✅ Data processed and saved successfully!")
else:
    st.error("⚠️ No valid data found in CSV!")

print("✅ Data Upload Script Executed Successfully!")