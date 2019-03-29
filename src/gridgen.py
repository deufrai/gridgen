from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json
from fpdf import FPDF


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

    @classmethod
    def from_chord_names(cls, names: str):
        bars = list()
        for chord in names:
            bars.append(Bar([chord]))
        part = cls()
        part.bars = bars
        return part


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

    @classmethod
    def from_name_and_single_part(cls, name: str, part: Part):
        return cls(name=name, parts=[part])


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


class PdfGenerator:
    FONT_SIZE = 19
    LEFT_COLSIZE = 50
    CELL_WIDTH = 18
    CELL_HEIGHT = 9
    TITLE_HEIGHT = 15
    CELLS_PER_ROW = 8
    CELL_MARGIN = 5
    ELEMENT_TOP_SPACING = 4

    def __init__(self, song: Song):
        self.pdf = FPDF()
        self.song = song

    def _build_title(self):
        self.pdf.set_font('Arial', 'B', PdfGenerator.FONT_SIZE)
        self.pdf.cell(w=self.pdf.get_string_width(self.song.title) + 10,
                      h=PdfGenerator.TITLE_HEIGHT,
                      txt=self.song.title,
                      border=1,
                      align='C')
        self.pdf.cell(w=self.pdf.get_string_width(self.song.key) + 10,
                      h=PdfGenerator.TITLE_HEIGHT,
                      txt=self.song.key,
                      border=1,
                      align='C')
        self.pdf.ln()

    def _build_elements(self):
        for element in self.song.elements:

            self.pdf.ln(PdfGenerator.ELEMENT_TOP_SPACING)
            self.pdf.cell(w=PdfGenerator.LEFT_COLSIZE,
                          h=PdfGenerator.CELL_HEIGHT,
                          txt=element.name,
                          border=1,
                          align="R")

            self.pdf.cell(w=0,
                          h=PdfGenerator.CELL_HEIGHT,
                          txt=element.note,
                          ln=1,
                          border='B')

            for part in element.parts:
                self._build_part(part)

    def _build_part(self, part):

        self.pdf.cell(w=PdfGenerator.LEFT_COLSIZE,
                      h=PdfGenerator.CELL_HEIGHT,
                      txt=part.note + "  ",
                      align="R")

        for i, bar in enumerate(part.bars):

            if i and not i % PdfGenerator.CELLS_PER_ROW:
                self.pdf.ln()
                self.pdf.cell(w=PdfGenerator.LEFT_COLSIZE,
                              h=PdfGenerator.CELL_HEIGHT)

            if len(bar.chords) == 1:
                text = bar.chords[0]
            else:
                text = "/".join(bar.chords)
            self.pdf.cell(w=PdfGenerator.CELL_WIDTH,
                          h=PdfGenerator.CELL_HEIGHT,
                          txt=text + ("|" if bar.short else ""),
                          align="C",
                          border="L" if not i % (PdfGenerator.CELLS_PER_ROW / 2) else 0)
        self.pdf.ln()

    def _build_page(self):
        self.pdf.set_title(self.song.title)
        self.pdf.add_page()
        self._build_title()
        self._build_elements()

    def save(self, file_path: str):
        self._build_page()
        self.pdf.output(file_path)
