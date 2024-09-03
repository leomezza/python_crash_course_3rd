def make_album(artist, album, nr_songs=None):
    """Returns the artist, its album and number of songs in a dictionary"""
    artist_album = {"artist": artist, "album": album}
    if nr_songs:
        artist_album["songs"] = nr_songs
    return artist_album


aas_dict = make_album("Artist 1", "Album 1")
print(aas_dict)

aas_dict = make_album("Artist 2", "Album 2")
print(aas_dict)

aas_dict = make_album("Artist 3", "Album 3")
print(aas_dict)

aas_dict = make_album("Artist 4", "Album 4", 4)
print(aas_dict)
