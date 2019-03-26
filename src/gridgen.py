from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Bar:
    chords: List[str] = None
    beats: int = 4
    division: int = 4
    short: bool = False

    def add_chord(self, chord: str):
        if not self.chords:
            self.chords = list()
        self.chords.append(chord)

    def set_signature(self, beats, division):
        self.beats = beats
        self.division = division


@dataclass_json
@dataclass
class Part:
    bars: List[Bar] = None
    note: str = ""

    def add_bar(self, bar: Bar):
        if not self.bars:
            self.bars = list()

        self.bars.append(bar)


@dataclass_json
@dataclass
class Element:
    name: str
    parts: List[Part] = None
    note: str = ""

    def add_part(self, part: Part):
        if not self.parts:
            self.parts = list()

        self.parts.append(part)


@dataclass_json
@dataclass
class Song:
    title: str
    key: str
    elements: List[Element] = None
    beats: int = 4
    division: int = 4

    def add_element(self, element: Element):
        if not self.elements:
            self.elements = list()

        self.elements.append(element)

    def set_signature(self, beats, division):
        self.beats = beats
        self.division = division
