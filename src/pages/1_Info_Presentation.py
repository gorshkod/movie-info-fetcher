"""Page diplaying the movie information in a nice format"""
import streamlit as st

st.set_page_config(page_title="Info Presentation")
st.title("Movie Information Presentation")

if "movie_data" in st.session_state:
    movie_data = st.session_state["movie_data"]
    
    if movie_data.get("Response", "False") == "False":
        st.error("Movie not found! Please try again with a different title/year.")
    else:
        st.header(movie_data.get("Title", "No Title Found"))
        poster_url = movie_data.get("Poster", "")
        if poster_url and poster_url != "N/A":
            st.image(poster_url, width=300)
        
        st.markdown(f"**Year:** {movie_data.get('Year', 'N/A')}")
        st.markdown(f"**Rated:** {movie_data.get('Rated', 'N/A')}")
        st.markdown(f"**Released:** {movie_data.get('Released', 'N/A')}")
        st.markdown(f"**Runtime:** {movie_data.get('Runtime', 'N/A')}")
        st.markdown(f"**Genre:** {movie_data.get('Genre', 'N/A')}")
        st.markdown(f"**Director:** {movie_data.get('Director', 'N/A')}")
        st.markdown(f"**Writer:** {movie_data.get('Writer', 'N/A')}")
        st.markdown(f"**Actors:** {movie_data.get('Actors', 'N/A')}")
        st.markdown(f"**Plot:** {movie_data.get('Plot', 'N/A')}")
        st.markdown(f"**Language:** {movie_data.get('Language', 'N/A')}")
        st.markdown(f"**Country:** {movie_data.get('Country', 'N/A')}")
        st.markdown(f"**Awards:** {movie_data.get('Awards', 'N/A')}")
else:
    st.info("Please go to the main page, enter a movie title and release year, and fetch the movie info.")
