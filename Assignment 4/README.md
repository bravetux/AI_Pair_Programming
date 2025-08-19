# Movie Genre Recommender

This script allows you to find the top-rated movies in a specific genre using the latest movie dataset from Kaggle.

## Features
- Automatically downloads the latest version of the movie dataset from Kaggle using `kagglehub`.
- Prompts the user to enter a movie genre (e.g., Action, Comedy, Drama).
- Displays up to 5 top-rated movies in the selected genre, sorted by rating.

## Requirements
- Python 3.x
- `pandas` library
- `kagglehub` library

Install dependencies with:
```sh
pip install pandas kagglehub
```

## How to Use
1. Run the script:
   ```sh
   python movie.py
   ```
2. When prompted, enter a genre (e.g., Action).
3. The script will display the top 5 movies in that genre based on their average rating.

## Output
- The script prints the top movies in the selected genre to the console.

## Notes
- The script automatically downloads and uses the `movies_metadata.csv` file from the Kaggle dataset `rounakbanik/the-movies-dataset`.
- Make sure you have an internet connection for the dataset download.
- If the genre is not found, the script will notify you.
