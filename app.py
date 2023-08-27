import streamlit as st
import pickle
import numpy as np
import pandas as pd
import requests



st.title('Movie Recommendation System')


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


similarity = pickle.load(open('similarity.pkl','rb'))
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])

    recommend_movie = []
    recommend_poster = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movie_id))
        recommend_movie.append(movies.iloc[i[0]].title)

    return recommend_movie, recommend_poster


movie_list = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movie_list)


selected_movie_name = st.selectbox(
'Which is your favourite MOVIE',
movies['title'].values)

if st.button('RECOMMEND'):
    recommend_movie,recommend_poster = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommend_movie[0])
        st.image(recommend_poster[0])
    with col2:
        st.text(recommend_movie[1])
        st.image(recommend_poster[1])

    with col3:
        st.text(recommend_movie[2])
        st.image(recommend_poster[2])
    with col4:
        st.text(recommend_movie[3])
        st.image(recommend_poster[3])
    with col5:
        st.text(recommend_movie[4])
        st.image(recommend_poster[4])
