import requests
import streamlit as st
import pandas as pd

st.set_page_config(
        page_title="Movie recommendation system",
)

movies = pd.read_pickle('movies.pkl')
cosine_matrix = pd.read_pickle('cosine_matrix.pkl')

def recommend(series_title):
    recommend_movie = []
    try:    
        index = movies[movies['Series_Title'] == series_title].index[0]
        movies_list = sorted(list(enumerate(cosine_matrix[index])), reverse=True, key=lambda x: x[1])[:5]
        for item in movies_list:
            recommend_movie.append([movies.iloc[item[0]]['Series_Title'],movies.iloc[item[0]]['Poster_Link']])
    except Exception as e:
        st.warning('Movie not found', icon="⚠️")
    return recommend_movie   
 
def load_image(image_url):
    dummy_image_url = "https://via.placeholder.com/150/FFFFFF/000000/?text=No+Image+Available"
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            return image_url
        else:
            raise Exception('image not found')
    except Exception as e:
        return dummy_image_url

st.title('Movie Recommendation System')

selected_movie = st.selectbox(
    'Choose the Movie',
    movies.Series_Title.values)


    
if st.button('Recommend'):
    recommend_movie = recommend(selected_movie)
    st.subheader('Recommended movies')
    if len(recommend_movie):
        col1, col2 = st.columns(2, gap="medium")

        col1.header(recommend_movie[0][0])
        col1.image(load_image(recommend_movie[0][1]), width=100, caption='Image not found' if recommend_movie[0][1] is None else None)

        col2.header(recommend_movie[1][0])
        col2.image(load_image(recommend_movie[1][1]), width=100, caption='Image not found' if recommend_movie[1][1] is None else None)

        col1, col2 = st.columns(2, gap="medium")

        col1.header(recommend_movie[2][0])
        col1.image(load_image(recommend_movie[2][1]), width=100, caption='Image not found' if recommend_movie[2][1] is None else None)

        col2.header(recommend_movie[3][0])
        col2.image(load_image(recommend_movie[3][1]), width=100, caption='Image not found' if recommend_movie[3][1] is None else None)

        st.header(recommend_movie[4][0])
        st.image(load_image(recommend_movie[4][1]), width=100, caption='Image not found' if recommend_movie[4][1] is None else None)
    else:
        st.header("Movie not found!")
else:
    st.subheader('Select a movie for recommendation')
