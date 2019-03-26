import fractions
from dataclasses import dataclass
from fractions import Fraction
from typing import List


@dataclass
class Bar(object):
    chords: List[str] = None
    signature: fractions.Fraction = Fraction(4, 4, _normalize=False)

    def __init__(self, chord: str):
        self.chords = [chord, ]

    def add_chord(self, chord: str):
        self.chords.append(chord)

    def set_signature(self, beats, division):
        self.signature = Fraction(beats, division, _normalize=False)

    @property
    def beats(self):
        return self.signature.numerator

    @property
    def division(self):
        return self.signature.denominator


@dataclass
class Part(object):
    bars: List[Bar] = None

    def add_bar(self, bar: Bar):
        if not self.bars:
            self.bars = list()

        self.bars.append(bar)


@dataclass
class Element(object):
    name: str
    parts: List[Part] = None

    def add_part(self, part: Part):
        if not self.parts:
            self.parts = list()

        self.parts.append(part)


@dataclass
class Song(object):
    title: str
    key: str
    elements: List[Element] = None
    signature: fractions.Fraction = Fraction(4, 4, _normalize=False)

    def add_element(self, element: Element):
        if not self.elements:
            self.elements = list()

        self.elements.append(element)

    def set_signature(self, beats, division):
        self.signature = Fraction(beats, division, _normalize=False)

    @property
    def beats(self):
        return self.signature.numerator

    @property
    def division(self):
        return self.signature.denominator
