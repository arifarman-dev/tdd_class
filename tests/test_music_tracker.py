import pytest
from lib.music_tracker import *

def test_if_empty_list_is_intialised():
    music_tracker = MusicTracker()
    assert music_tracker.see() == []

def test_adding_1_track():
    music_tracker = MusicTracker()
    music_tracker.add("Baby Shark")
    assert music_tracker.see() == ["Baby Shark"]

def test_adding_2_track():
    music_tracker = MusicTracker()
    music_tracker.add("Baby Shark")
    music_tracker.add("ABC")
    assert music_tracker.see() == ["Baby Shark","ABC"]

def test_empty_music_track_raises_error():
    music_tracker = MusicTracker()
    with pytest.raises(Exception) as e:
        music_tracker.add("")
    error_message = str(e.value)
    assert error_message == "Input cannot be empty"