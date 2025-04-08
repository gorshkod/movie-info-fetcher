"""
Pytest tests for Search.py module, specifically get_movie_data function

Utilizes Monkeypatch to replace HTTP requests to the API with a fake request
"""

import pytest
from Search import get_movie_data

class FakeResponse:
    def __init__(self, json_data: dict) -> None:
        self._json = json_data

    def json(self) -> dict:
        return self._json

def fake_get_success(url: str) -> FakeResponse:
    """Simulate a successful API response."""
    return FakeResponse({
        "Response": "True",
        "Title": "Inception",
        "Year": "2010",
        "Rated": "PG-13",
        "Released": "16 Jul 2010",
        "Runtime": "148 min",
        "Genre": "Action, Adventure, Sci-Fi",
        "Director": "Christopher Nolan",
        "Writer": "Christopher Nolan",
        "Actors": "Leonardo DiCaprio, Joseph Gordon-Levitt, Elliot Page",
        "Plot": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.",
        "Language": "English",
        "Country": "USA",
        "Awards": "Won 4 Oscars. Another 152 wins & 204 nominations.",
        "Poster": "https://example.com/inception.jpg"
    })

def fake_get_error(url: str) -> FakeResponse:
    """Simulate an API response with an error."""
    return FakeResponse({
        "Response": "False",
        "Error": "Movie not found!"
    })

def test_get_movie_data_success(monkeypatch: pytest.MonkeyPatch) -> None:
    # Replace the 'get' function in the Search module with fake_get_success.
    monkeypatch.setattr("search.get", fake_get_success)
    movie_data = get_movie_data("Inception", 2010)
    assert movie_data["Response"] == "True"
    assert movie_data["Title"] == "Inception"
    assert movie_data["Year"] == "2010"

def test_get_movie_data_error(monkeypatch: pytest.MonkeyPatch) -> None:
    # Replace the 'get' function in the Search module with fake_get_error.
    monkeypatch.setattr("search.get", fake_get_error)
    movie_data = get_movie_data("Nonexistent Movie", 1900)
    assert movie_data["Response"] == "False"
    assert movie_data["Error"] == "Movie not found!"