def make_album(artist, album, nr_songs=None):
    """Returns the artist, its album and number of songs in a dictionary"""
    artist_album = {"artist": artist, "album": album}
    if nr_songs:
        artist_album["songs"] = nr_songs
    return artist_album

while True:
    print("\nPlease provide the information from the music album:")
    print("(enter 'q' at any time to quit)")

    artist_name = input("Artist name: ")
    if artist_name == 'q':
        break

    album_name = input("Album name: ")
    if album_name == 'q':
        break

    formatted_name = make_album(artist_name, album_name)
    print(f"\nHere it is, {formatted_name}!")
    