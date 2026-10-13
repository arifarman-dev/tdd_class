# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class MusicTracker:
    # User-facing properties:
    #   music_name: string

    def __init__(self):
        # Parameters:
        #   music_list: list
        # Side effects:
        #   Creates an empty list
        pass # No code here yet

    def add(self, music_name):
        # Parameters:
        #   music_name: string representing a single track
        # Returns:
        #   Nothing
        # Side-effects
        #   Appends the music_name into our list
        pass # No code here yet

    def see(self):
        # Returns:
        #   The list of all the music tracks that we added into our list
        # Side-effects:
        #   nothing
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Test if empty list is intialised
"""
music_tracker = MusicTracker()
music_tracker.music_list # => 0

"""
Test adding 1 music track to list
"""
music_tracker = MusicTracker()
result = music_tracker.add("Baby Shark")
result.see() # => ["Baby Shark"]

"""
Test adding 2 music track to list
"""
music_tracker = MusicTracker()
result = music_tracker.add("Baby Shark")
result1 = music_tracker.add("ABC")
result1.see() # => ["Baby Shark", "ABC"]
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
