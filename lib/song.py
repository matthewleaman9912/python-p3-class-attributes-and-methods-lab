from collections import Counter
class Song:

    count = 0
    genres = []
    artists = []
    genre_count = {}
    

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        print(self.genre_count)
    @classmethod
    def add_song_to_count(cls, increment = 1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls, genre):
        if genre in cls.genres:
            return cls.genres
        else:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist in cls.artists:
            return cls.artists
        else:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        keys = []
        values = []
        
        for listed in cls.genres:
            if listed not in keys:
                keys.append(listed)
                values.append(1)
        dicti = dict(zip(keys, values))
        print(dicti)
        


               


    


