"""Page diplaying the retrieved movie information JSON with the option to download it"""
import streamlit as st
from json import dumps

st.set_page_config(page_title="Raw JSON")
st.title("Raw JSON Data")

if "movie_data" in st.session_state:
    movie_data = st.session_state["movie_data"]
    
    # Convert the JSON data to a formatted string for the download button
    json_str = dumps(movie_data, indent=4)
    
    # Download button to download the JSON data as a file
    st.download_button(
        label="Download JSON",
        data=json_str,
        file_name="movie_info.json",
        mime="application/json"
    )
    
    st.json(movie_data)
    
else:
    st.info("Please go to the main page, enter a movie title and release year, and fetch the movie info.")