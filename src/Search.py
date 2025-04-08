"""
Main page of the Streamlit app that uses OMDb (Open Movie Database) API to fetch movie information

Author: Daniil Gorshkov
ChatGPT o3-mini-high used to assist with Streamlit app structure
"""
from os import environ
import streamlit as st
from requests import get


# If running on Streamlit Community Cloud, load Streamlit secrets into os.environ
if "STREAMLIT_ENV" in st.secrets:  # Set this flag in Streamlit secrets
    environ["API_KEY"] = st.secrets["API_KEY"]

# OMDb API key handling
API_KEY = environ.get("API_KEY", None)

st.set_page_config(page_title="Search")


def get_movie_data(title: str, year: int) -> dict:
    """Fetch movie data JSON from the OMDb API."""
    url = f"http://www.omdbapi.com/?t={title}&y={year}&apikey={API_KEY}"
    response = get(url)
    return response.json()


st.title("Movie Info Fetcher")

with st.form("movie_form"):
    movie_title = st.text_input("Enter the Movie Title:")
    release_year = st.number_input("Enter the release year (optional)", min_value=1888, value=None, step=1)
    submitted = st.form_submit_button("Fetch Movie Info")

    if submitted:
        if not movie_title:
            st.error("Please provide a movie title.")
        else:
            movie_data = get_movie_data(movie_title, release_year)
            st.session_state["movie_data"] = movie_data

            # Check if the API returned an error
            if movie_data.get("Response", "False") == "False":
                st.error(f'Error: {movie_data.get("Error", "Movie not found!")}')
            else:
                st.success("Movie information fetched! Use the sidebar to navigate.")

st.info("After fetching, use the sidebar to view the presentation page or the raw JSON page.")
