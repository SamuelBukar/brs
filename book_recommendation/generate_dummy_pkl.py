import pickle
import numpy as np
import os
import pandas as pd

# Ensure the artifacts3 folder exists
os.makedirs("artifacts3", exist_ok=True)

# Dummy model
dummy_model = {"message": "This is a dummy model"}
pickle.dump(dummy_model, open("artifacts3/model.pkl", "wb"))

# Dummy pivot table (collaborative filtering)
collab_pivot = pd.DataFrame(np.random.rand(10, 10))
pickle.dump(collab_pivot, open("artifacts3/collab_pivot.pkl", "wb"))

# Dummy book names list
books_names_list = ["Book " + str(i) for i in range(1, 11)]
pickle.dump(books_names_list, open("artifacts3/books_names_list.pkl", "wb"))

# Dummy book data (Ensure all columns have the same length)
req_updated_books = pd.DataFrame({
    "title": books_names_list,
    "isbn": [str(i) for i in range(1, 11)],
    "coverImg": [f"https://dummyimage.com/100x150/000/fff&text=Book{i}" for i in range(1, 11)],
    "genres": [["Fiction"] for _ in range(10)],  # Ensure this matches the number of books
    "rating": np.random.randint(1, 6, size=10)
})
pickle.dump(req_updated_books, open("artifacts3/req_updated_books.pkl", "wb"))

# Dummy content similarity matrix
content_similarity = np.random.rand(10, 10)
pickle.dump(content_similarity, open("artifacts3/content_similarity.pkl", "wb"))

print("✅ Dummy .pkl files generated successfully!")