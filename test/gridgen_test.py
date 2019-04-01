from gridgen import Bar, Part, Element, Song


def test_add_chord_to_bar():
    b = Bar()
    b.add_chord("C#")
    b.add_chord("D")
    assert b.chords == ["C#", "D"]


def test_bar_signature():
    b = Bar(chords=["C#"])
    b.set_signature(3, 4)
    assert (b.beats == 3 and b.division == 4)


def test_add_bar_to_part():
    b = Bar(chords=["C#"])
    p = Part()
    p.add_bar(b)
    assert p.bars[0] == b


def test_creation_class_methods():
    names = "ABC"
    part = Part.from_chord_names(names)

    for i, bar in enumerate(part.bars):
        assert len(bar.chords) == 1
        assert bar.chords[0] == names[i]

    name = "TEST"
    element = Element.from_name_and_single_part(name, part)
    assert element.name == name
    assert len(element.parts) == 1
    assert element.parts[0] == part


def test_add_part_to_element():
    p = Part()
    e = Element("test")
    e.add_part(p)
    assert e.parts[0] == p


def test_add_element_to_song():
    s = Song("test", "A")
    e = Element("test")
    s.add_element(e)
    assert s.elements[0] == e


def test_bar_default_signature_is_4_4():
    b = Bar(chords=["C#"])
    assert (4 == b.beats and 4 == b.division)


def test_song_default_signature_is_4_4():
    s = Song("test", "A")
    assert (4 == s.beats and 4 == s.division)


def test_song_signature():
    s = Song("test", "A")
    s.set_signature(3, 4)
    assert (s.beats == 3 and s.division == 4)
