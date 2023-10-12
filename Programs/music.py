class Song:
    def __init__(self, title, artist, duration, genre):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.genre = genre

def create_music_playlist(songs, genre=None, artist=None, duration=None):
    # Create a music playlist based on user preferences
    playlist = []
    
    for song in songs:
        if (not genre or song.genre == genre) and (not artist or song.artist == artist) and (not duration or song.duration <= duration):
            playlist.append(song)
    
    return playlist

def display_playlist(playlist):
    # Display the music playlist
    for index, song in enumerate(playlist):
        print(f"{index + 1}. {song.title} by {song.artist} ({song.duration} seconds) - {song.genre}")

# Sample songs
songs = [
    Song("Song1", "Artist1", 180, "Pop"),
    Song("Song2", "Artist2", 240, "Rock"),
    Song("Song3", "Artist3", 210, "Pop"),
    Song("Song4", "Artist1", 195, "Rock"),
    Song("Song5", "Artist4", 160, "Jazz"),
]

# Main function
if __name__ == "__main__":
    print("Welcome to the Music Playlist Generator!")
    
    genre = input("Enter a genre (or press Enter to skip): ")
    artist = input("Enter an artist (or press Enter to skip): ")
    
    try:
        duration = int(input("Enter a maximum song duration (in seconds, or press Enter to skip): "))
    except ValueError:
        duration = None
    
    playlist = create_music_playlist(songs, genre, artist, duration)
    
    if playlist:
        print("Here's your customized playlist:")
        display_playlist(playlist)
    else:
        print("No songs match your criteria. Try different preferences.")
