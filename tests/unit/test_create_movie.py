# TODO: Feature 2
import pytest
def test_create_movie():
    movie = Movie("It Follows","David Robert Mitchell",6.8)
    assert movie == create_movie("It Follows","David Robert Mitchell",6.8)