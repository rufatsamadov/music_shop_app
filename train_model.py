import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

# Load Track and Genre tables
track_df = pd.read_csv('data/Track.csv')
genre_df = pd.read_csv('data/Genre.csv')

# Merge to get genre names
df = track_df.merge(genre_df, on='GenreId')

# Feature columns
X = df[['Milliseconds', 'Bytes', 'UnitPrice']]
y = df['Name_y']  # Genre name

X.fillna(0, inplace=True)

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Save model
with open('model/genre_classifier.pkl', 'wb') as f:
    pickle.dump(clf, f)
