import streamlit as st
import pickle
import pandas as pd
import random

# Load data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = [movies.iloc[i[0]].title for i in movies_list]
    return recommended_movies

# App title
st.title("🎬 Movie Recommender System 🍿")
st.subheader("Discover your next favorite movie!")

# Movie selection
selected_movie_name = st.selectbox("Select a movie to get recommendations:", movies['title'].values)

# Recommend button
if st.button("Recommend"):
    with st.spinner("Finding the best movies for you..."):
        recommendations = recommend(selected_movie_name)
    
    st.success("Here are some movies you might enjoy!")
    
    for i, movie in enumerate(recommendations, start=1):
        st.write(f"{i}. {movie}")

# Additional creative elements
st.markdown("---")
st.write("### 🎥 Movie Trivia 🎥")
st.write("Did you know?")
trivia = [
    "The movie 'Inception' was filmed in six countries: Canada, the United States, Morocco, the United Kingdom, Japan, and France.",
    "In 'The Shawshank Redemption', the maggot fed to the bird was not real. It was made of a special edible substance.",
    "The iconic 'I’ll be back' line from 'The Terminator' was initially scripted as 'I’ll come back'.",
    "In 'The Godfather', the cat held by Marlon Brando in the opening scene was a stray found on the studio lot.",
    "The famous 'Here's Johnny!' line from 'The Shining' was improvised by Jack Nicholson."
      "The Wizard of Oz (1939): The famous ruby slippers worn by Judy Garland were originally silver in the book. They were changed to ruby red to take advantage of Technicolor.",
    "Pulp Fiction (1994): The shot of Vincent Vega (John Travolta) plunging a syringe into Mia Wallace's (Uma Thurman) chest was filmed in reverse to make it safer.",
    "The Godfather (1972): The cat held by Marlon Brando in the opening scene was a stray found on the studio lot, and its purring was so loud that it caused issues with recording Brando's dialogue.",
    "Inception (2010): The movie was filmed in six different countries: Canada, the United States, Morocco, the United Kingdom, Japan, and France.",
    "The Shawshank Redemption (1994): The maggot fed to the bird was not real. It was made of a special edible substance approved by the American Humane Association.",
    "The Terminator (1984): The iconic 'I'll be back' line was initially scripted as 'I'll come back.'",
    "The Shining (1980): Jack Nicholson improvised the famous 'Here's Johnny!' line, which was not in the original script.",
    "The Dark Knight (2008): Heath Ledger kept a 'Joker diary' to help him get into character. It included disturbing images and notes.",
    "Forrest Gump (1994): Tom Hanks was not paid for the role but instead took percentage points, earning him about $40 million.",
    "Jurassic Park (1993): The sounds of the velociraptors communicating were actually recordings of tortoises mating.",
    "Star Wars (1977): The lightsaber sound was created by combining the hum of an old television picture tube and the buzz of a film projector motor.",
    "Back to the Future (1985): The DeLorean's gull-wing doors often malfunctioned during filming, making it difficult to shoot scenes.",
    "Jaws (1975): The mechanical shark used in the film was nicknamed 'Bruce' after Steven Spielberg's lawyer.",
    "E.T. the Extra-Terrestrial (1982): Harrison Ford originally had a cameo as Elliott's school principal, but it was cut from the film.",
    "The Silence of the Lambs (1991): Anthony Hopkins based his portrayal of Hannibal Lecter on HAL 9000 from 2001: A Space Odyssey and a combination of Katharine Hepburn and Truman Capote.",
    "Psycho (1960): The blood in the famous shower scene was actually chocolate syrup.",
    "Titanic (1997): The movie's production cost more than the actual Titanic ship.",
    "Indiana Jones and the Raiders of the Lost Ark (1981): The snake pit scene involved over 7,000 live snakes.",
]
st.write(random.choice(trivia))

st.markdown("---")
st.write("### 💬 Share your recommendations 💬")
st.text_input("Tell us what you think about our recommendations:")
if st.button("Submit Feedback"):
    st.success("Thank you for your feedback!")
