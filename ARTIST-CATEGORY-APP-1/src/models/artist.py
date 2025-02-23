class Artist:
    def __init__(self, name, spotify_popularity, instagram_followers):
        self.name = name
        self.spotify_popularity = spotify_popularity
        self.instagram_followers = instagram_followers

    def determine_level(self):
        if self.spotify_popularity >= 40 and self.instagram_followers >= 20000:
            return 'A'
        elif self.spotify_popularity >= 25 and self.instagram_followers >= 2500:
            return 'B'
        else:
            return 'C'