
import pandas as pd
import os
import kagglehub

# Download latest version of the dataset using kagglehub
path = kagglehub.dataset_download("rounakbanik/the-movies-dataset")
print("Path to dataset files:", path)

# Path to the CSV file (update as needed)
csv_path = os.path.join(path, 'movies_metadata.csv')

try:

    # Check if the CSV exists in the downloaded dataset
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Could not find 'movies_metadata.csv' in the downloaded dataset at {path}.")

    # Load the CSV file

    df = pd.read_csv(csv_path, low_memory=False)

    # Check for required columns
    # The new dataset uses 'genres' (JSON string) and 'vote_average' for rating
    required_cols = {'title', 'genres', 'vote_average'}
    if not required_cols.issubset(df.columns.str.lower()):
        raise ValueError(f"CSV must contain columns: {required_cols}")

    # Ensure at least 20 rows
    if len(df) < 20:
        raise ValueError("CSV must have at least 20 rows.")

    # Ask user for genre
    genre = input("Enter a genre (e.g., Action): ").strip()
    if not genre:
        raise ValueError("Genre cannot be empty.")

    import json
    # Parse genres and filter
    def has_genre(genres_str, genre):
        try:
            genres_list = json.loads(genres_str.replace("'", '"'))
            return any(g['name'].lower() == genre.lower() for g in genres_list)
        except Exception:
            return False

    filtered = df[df['genres'].apply(lambda x: has_genre(x, genre))]

    if filtered.empty:
        print(f"No movies found for genre '{genre}'.")
    else:
        # Sort by vote_average descending
        filtered_sorted = filtered.sort_values(by='vote_average', ascending=False)
        # Show up to 5 movies
        top_movies = filtered_sorted.head(5)
        print(f"\nTop {min(5, len(top_movies))} movies in genre '{genre}':")
        for idx, row in top_movies.iterrows():
            print(f"- {row['title']} (Rating: {row['vote_average']})")
except Exception as e:
    print(f"Error: {e}")
