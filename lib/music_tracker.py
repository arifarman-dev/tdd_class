class MusicTracker:

    def __init__(self):
        self.music_list = []

    def see(self):
        return self.music_list

    def add(self, music_name):
        self.music_name = music_name
        self.music_list.append(self.music_name)