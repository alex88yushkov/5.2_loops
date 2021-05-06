class songs:

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

sing = songs(["Tell me somethin', girl",
              "Are you happy in this modern world?",
              "Or do you need more?",
              "Is there somethin' else you're searchin' for?"])
sing.sing_me_a_song()