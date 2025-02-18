import pickle
import pandas as pd
import os

# Ensure the artifacts3 directory exists
os.makedirs("artifacts3", exist_ok=True)

# Load books dataset from CSV
try:
    books_df = pd.read_csv("books_random_subset.csv")
    print("📂 CSV Data Loaded Successfully!")
except FileNotFoundError:
    print("⚠️ books_random_subset.csv not found! Ensure it's in the project folder.")
    books_df = pd.DataFrame()  # Create an empty DataFrame to avoid crashes

# Extract necessary columns (handle missing columns)
if not books_df.empty:
    books_df = books_df.fillna("Unknown")  # Replace NaN values with "Unknown"

    # Split the titles into individual rows
    books_df = books_df['title'].str.split(', ', expand=True).stack().reset_index(level=1, drop=True).to_frame('title')

    # Add dummy data for other columns
    books_df['isbn'] = books_df['title'].apply(lambda x: f"ISBN-{x[:3].upper()}")
    books_df['coverImg'] = "https://dummyimage.com/100x150/000/fff&text=No+Image"
    books_df['genres'] = [["Unknown"]]
    books_df['rating'] = 0

    books_names_list = books_df["title"].tolist()
    req_updated_books = books_df[["title", "isbn", "coverImg", "genres", "rating"]]

    # Save extracted data as Pickle files for use in `app.py`
    pickle.dump(books_names_list, open("artifacts3/books_names_list.pkl", "wb"))
    pickle.dump(req_updated_books, open("artifacts3/req_updated_books.pkl", "wb"))

    print("✅ Data processed and saved successfully!")
else:
    print("⚠️ No valid data found in CSV!")

print("✅ Data Upload Script Executed Successfully!")
