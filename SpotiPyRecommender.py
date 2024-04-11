import os
import spotipy
from collections import defaultdict
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import sys


# Function to create a playlist based on a genre
def create_genre_playlist(sp, user_id, genre, songLimit):
    # Get recommended tracks based on the genre
    recommendations = sp.recommendations(seed_genres=[genre], limit=songLimit)

    # Create a new playlist
    playlist_name = f"{genre.title()}"
    playlist_description = "Playlist made by SpotiPyRecommender"
    playlist = sp.user_playlist_create(user_id, playlist_name, public=True, description=playlist_description)

    # Extract track IDs from the recommendations
    track_ids = [track['id'] for track in recommendations['tracks']]

    # Add tracks to the new playlist
    sp.playlist_add_items(playlist['id'], track_ids)
    print(f"Playlist '{playlist_name}' created successfully.")


# List the available genre seeds
def show_genre_list(sp):
    # Retrieve genre seeds from Spotify and sort them in alphabetical order
    genre_seeds = sp.recommendation_genre_seeds()
    genres = genre_seeds['genres']
    sorted_genres = sorted(genres)
    genres_by_letter = defaultdict(list)

    # For readability purposes
    # Add the genres to a dictionary with the initial letter of each genre as the key
    for genre in sorted_genres:
        letter = genre[0]
        genres_by_letter[letter].append(genre)
    for letter, genres in genres_by_letter.items():
        print(f"{letter.upper()}: {' '.join(genres)}")


# Checks if the genre entered is a recognised Spotify genre
def validate_genre(sp, genre_inputted):
    genre_seeds = sp.recommendation_genre_seeds()
    return genre_inputted in genre_seeds['genres']


def main():
    # Load environment variables from .env file
    load_dotenv()

    # Set up Spotify app's credentials
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')

    # Environmental variables loading check
    if not client_id or not client_secret:
        print("Error: Spotify client credentials not found. Please check your .env file.")
        sys.exit()

    redirect_uri = 'http://localhost:8888/callback'
    scope = 'playlist-modify-public user-top-read'

    # Initialize the Spotipy client with OAuth
    auth_manager = SpotifyOAuth(client_id=client_id,
                                client_secret=client_secret,
                                redirect_uri=redirect_uri,
                                scope=scope)

    # Create an instance of the spotify client
    sp = spotipy.Spotify(auth_manager=auth_manager)

    # Get the current user's ID
    user_id = sp.current_user()['id']

    # Prompt the user to enter the number of songs they would like recommended
    print('Welcome to SpotPy Recommender. Enter a genre to receive song recommendations.')

    try:
        # Prompt the user to enter the number of songs they would like recommended
        # Convert the string to an int
        song_limit = int(input('how many songs would you like recommended (1-100): '))

        # Check if the entered number is within the allowed range
        # If not print an error message and exit the script
        if not 1 <= song_limit <= 100:
            print(f"'{song_limit}' isn't a valid number")
            sys.exit()
    except ValueError:
        # This block catches any ValueError that occur when trying to convert
        # the input to an int (The user didn't enter a number)
        print("That's not a valid number. Please Run the script again and enter a number between 1 and 100")
        sys.exit()

    genre_input = input("Enter a genre or type 'list' to see the available genres: ").lower()

    if genre_input == 'list':
        # If the user asks for a list of genres, print the list of genres
        show_genre_list(sp)
        genre_input = input("Now enter a genre to create a playlist: ").lower()

    # If the entered genre is valid, create the playlist with recommended songs
    if validate_genre(sp, genre_input):
        create_genre_playlist(sp, user_id, genre_input, song_limit)
    else:
        # If invalid print an error message
        print(f"{genre_input} is not a valid genre. Please Run the script again and enter a valid genre")


if __name__ == '__main__':
    main()
