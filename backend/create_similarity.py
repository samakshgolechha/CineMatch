import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("Loading movies.pkl...")
movies_dict = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# If genres are stored as lists, convert to strings
movies['genres'] = movies['genres'].apply(lambda x: " ".join(x) if isinstance(x, list) else str(x))

print("Vectorizing text...")
cv = CountVectorizer(stop_words='english')
vector = cv.fit_transform(movies['genres'].fillna(""))

print("Calculating cosine similarity matrix...")
similarity = cosine_similarity(vector)

print("Saving similarity.pkl...")
with open('similarity.pkl', 'wb') as f:
    pickle.dump(similarity, f)

print("\n🎉 Done! 'similarity.pkl' created successfully.")
