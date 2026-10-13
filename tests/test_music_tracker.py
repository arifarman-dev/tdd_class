from lib.music_tracker import *

def test_if_empty_list_is_intialised():
    music_tracker = MusicTracker()
    assert music_tracker.see() == []

def test_adding_1_track():
    music_tracker = MusicTracker()
    result = music_tracker.add("Baby Shark")
    assert result.see() == ["Baby Shark"]