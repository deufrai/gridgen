import fractions
from dataclasses import dataclass
from fractions import Fraction
from typing import List


@dataclass
class Chord(object):
    name: str
    signature: fractions.Fraction = Fraction(4, 4, _normalize=False)

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

