class Clip:
    def __init__ (self, artist = "Moby", song = "Lift Me Up",
                  duration = 249, views = 33000000, genre = "Electro music", awards = 1):
        self.__artist = artist
        self.__song = song
        self.__duration = duration
        self.__views = views
        self.genre = genre
        self.awards = awards

    def get_artist(self):
            return self.__artist

    def get_song(self):
            return self.__song

    def get_duration(self):
            return self.__duration

    def get_views(self):
            return self.__views


    def __str__(self):
            return f"{self.__artist}, {self.__song}, {self.__duration}, {self.__views}, {self.genre}, {self.awards}"

    def __repr__(self):
        return (
            f"Clip:\n"
            f"  Artist: {self.__artist}\n"
            f"  Song: {self.__song}\n"
            f"  Duration: {self.__duration} seconds\n"
            f"  Views: {self.__views}\n"
            f"  Genre: {self.genre}\n"
            f"  Awards: {self.awards}"

        )

    def __del__(self):
        print(f"clip '{self.__song}' was deleted.")

def main():

    clip1 = Clip("Moby", "Lift Me Up", 249, 33000000, "Electro music", 1)
    clip2 = Clip("Sabrina Carpenter", "Espresso", 201, 23000000, "Pop", 0)
    clip3 = Clip("Tartak", "Наше Літо", 264, 380000, "Alternative rock", 0)

    print("\ninformation about the clips:")
    print(repr(clip1))
    print(repr(clip2))
    print(repr(clip3))


if __name__ == "__main__":
    main()





