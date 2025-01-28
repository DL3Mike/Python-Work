def make_album(artist, title, songs=None):
    """Return album dictionary."""
    album = {'artist': artist, 'title': title, 'songs': songs}
    return album


while True:
    print("\nEnter album information.")
    print("(enter 'q' at any time to quit)")

    artist = input("Artist Name: ")
    if artist == 'q':
        break

    title = input("Title Name: ")
    if artist == 'q':
        break

    song = input("Song Number (Optional): ")
    if artist == 'q':
        break

    album = make_album(artist, title, song)
    print(album)

print(make_album("cheause", "Swift"))
print(make_album("redeye", "2023", 2))
