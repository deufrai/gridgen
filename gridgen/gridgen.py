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

    def add_Bar(self, bar: Bar):
        if not self.bars:
            self.bars = list()

        self.bars.append(bar)


class Element(object):
    pass


class Song(object):
    pass

