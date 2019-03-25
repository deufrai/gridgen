from dataclasses import dataclass
from typing import List


@dataclass
class Chord(object):
    name: str

@dataclass
class Part(object):
    chords: List[Chord] = None

    def add_chord(self, chord: Chord):
        if not self.chords:
            self.chords = list()

        self.chords.append(chord)


class Element(object):
    pass


class Song(object):
    pass

