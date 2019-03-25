import fractions
from dataclasses import dataclass
from fractions import Fraction
from typing import List


@dataclass
class Bar(object):
    chord: str
    signature: fractions.Fraction = Fraction(4, 4, _normalize=False)

@dataclass
class Part(object):
    bars: List[Bar] = None

    def add_bar(self, bar: Bar):
        if not self.bars:
            self.bars = list()

        self.bars.append(bar)


class Element(object):
    parts: List[Part] = None

    def add_part(self, part: Part):
        if not self.parts:
            self.parts = list()

        self.parts.append(part)


class Song(object):
    tonality: str
    elements: List[Element] = None
    signature: fractions.Fraction = Fraction(4, 4, _normalize=False)

    def add_element(self, element: Element):
        if not self.elements:
            self.elements = list()

        self.elements.append(element)

