import streamlit as st
import pickle
import pandas as pd
import requests

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        #fetch poster from API
        recommended_movies.append(movies.iloc[i[0]]['title'])
        #recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies

similarity = pickle.load(open('similarity.pkl','rb'))
movies = pickle.load(open('movies.pkl','rb'))
movies_titles = movies['title'].values

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
'Select Movies',
movies_titles)

if st.button('Recommend'):
    try:
        recommendations = recommend(selected_movie_name)
        st.write("Here are some recommendations:")
        for i in recommendations:
            st.write(i)
    except IndexError:
        st.write("Error: Selected movie not found. Please try another.")