# Content-Based Movie Recommendation System

This repository contains a content-based movie recommendation system that suggests the top 5 similar movies based on cosine similarity. The system utilizes TF-IDF vectorization to analyze movie features and recommend similar ones.

## Features
The system considers the following features for movie analysis:
- **Poster_Link**: Link to the movie's poster image.
- **Series_Title**: Title of the movie.
- **Released_Year**: Year of release.
- **Genre**: Genre of the movie.
- **Overview**: Brief overview or summary of the movie.
- **Star1, Star2, Star3, Star4**: Leading stars or actors in the movie.
- **Director**: Director of the movie.

## Implementation
The implementation involves the following steps:
1. **Feature Selection**: Only specific features are selected for analysis, including Released_Year, Genre, Overview, Star1, Star2, Star3, Star4, and Director.
2. **TF-IDF Vectorization**: The selected features are vectorized using TF-IDF vectorization to represent the textual data numerically.
3. **Cosine Similarity**: Cosine similarity is calculated between the TF-IDF vectors of movies to find similarity scores.
4. **Recommendation**: Based on the cosine similarity scores, the system recommends the top 5 movies that are most similar to the input movie.

## Usage
To use the recommendation system:
1. Clone or download this repository.
2. Open the provided Google Colab notebook ([here](https://colab.research.google.com/drive/1ixxyzdD6N7kATIsK3B3As1yB1JG85RQL#scrollTo=D1F-7ybS0-02)).
3. Follow the instructions in the notebook to input a movie and receive recommendations.

## Note
- This system relies solely on content-based filtering and does not take into account user preferences or interactions.
- The quality of recommendations depends on the accuracy and relevance of the features provided for analysis.

Feel free to contribute to this project by forking and submitting pull requests!
