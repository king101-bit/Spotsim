import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def get_spotify_recommendations(input_song_uri):
    # Replace 'YOUR_CLIENT_ID' and 'YOUR_CLIENT_SECRET' with your Spotify API credentials
    client_id = 'YOUR_CLIENT_ID'
    client_secret = 'YOUR_CLIENT_SECRET'

    # Initialize Spotipy with client credentials
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    try:
        # Get track information for the input song
        input_track_info = sp.track(input_song_uri)

        # Get recommendations based on the input song
        recommendations = sp.recommendations(seed_tracks=[input_track_info['id']])

        # Extract and return recommended tracks
        recommended_tracks = [track['name'] for track in recommendations['tracks']]
        return recommended_tracks

    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage
if __name__ == "__main__":
    input_song_uri = input("Enter the Spotify URI for a song: ")

    # Get similar song recommendations
    recommendations = get_spotify_recommendations(input_song_uri)

    # Display recommendations
    if recommendations:
        print(f"Recommended songs similar to the input song:")
        for song in recommendations:
            print(song)
    else:
        print("Unable to retrieve recommendations.")
