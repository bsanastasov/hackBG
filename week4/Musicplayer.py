class Song:
    def __init__(self, name, artist, album, length):
        self.name = name
        self.artist = artist
        self.album = album
        self.length = length
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

        part = [int(i.split()) for i in length.split(":")]
        if len(part) == 3:
            self.hours = part[0]
            self.minutes = part[1]
            self.seconds = part[3]
        elif len(part) == 2:
            self.minutes = part[0]
            self.seconds = part[1]
        else:
            raise ValueError

    def get_hours(self):
        return self.hours

    def get_minutes(self):
        return self.get_hours() * 60 + self.minutes

    def get_seconds(self):
        return self.get_minutes()*60 + self.seconds


    def __str__(self):
        message = " {} - {} from {} - {}"
        return message.format(self.artist, self.name, self.album, self.length)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        name_bool = self.name == other.name
        artist_bool = self.artist == other.artist
        album_bool = self.album == other.album
        length_bool = self.length == other.length

        return name_bool and artist_bool and album_bool and length_bool

    def __hash__(self):
        return hash(self)

    def get_length(self, hours = False, minutes = False, seconds = False):
        if not hours and not minutes and not seconds:
            return self.length
        if hours:
            return self.get_hours()
        if minutes:
            return self.get_minutes()
        if seconds:
            return self.get_seconds()

    def prepare_json(self):
        song_dict = self.__dict__
        return {key: song_dict[key] for key in song_dict if not key.startswith("_")}

class Playlist:
    def __init__(self, name, repeat = False, shuffle = False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.list_songs = []

    def add_song(self, song):
        self.list_songs.append(song)

    def remove_song(self, song):
        self.list_songs.remove(song)

