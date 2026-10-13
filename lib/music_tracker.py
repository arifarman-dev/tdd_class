class MusicTracker:

    def __init__(self):
        self.music_list = []

    def see(self):
        return self.music_list

    def add(self, music_name):
        if music_name == "":
            raise Exception("Input cannot be empty")
        
        self.music_name = music_name
        self.music_list.append(self.music_name)
        