# Movie Info Fetcher

![run-tests](https://img.shields.io/github/actions/workflow/status/gorshkod/movie-info-fetcher/run-tests.yml?branch=main)
![docker-publish](https://img.shields.io/github/actions/workflow/status/gorshkod/movie-info-fetcher/docker-publish.yml?branch=main)

A simple Streamlit application that uses the OMDb API to fetch movie information based on user input. 
Deployed using Streamlit Community Cloud: <https://movie-info-fetcher.streamlit.app/>
This app has three pages:

- **Search Page:** Presents an input form for the movie title and an optional release year.
- **Presentation Page:** Displays the movie details in a formatted layout with a poster image and key information.
- **Raw JSON Page:** Shows the complete JSON response from the OMDb API and allows users to download it.

## Features

- Input a movie title and an optional release year.
- Fetch movie details using the OMDb API.
- Formatted display of movie details, including the poster.
- View and download the raw JSON data.
- Basic error handling when the movie is not found.
- API key handled using Streamlit secrets