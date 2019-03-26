from gridgen import Bar, Part, Element, Song


def test_add_bar_to_part():
    b = Bar("C")
    p = Part()
    p.add_bar(b)
    assert p.bars[0] == b


def test_add_part_to_element():
    p = Part()
    e = Element()
    e.add_part(p)
    assert e.parts[0] == p


def test_add_element_to_song():
    s = Song()
    e = Element()
    s.add_element(e)
    assert s.elements[0] == e


def test_bar_default_signature_is_4_4():
    b = Bar("C#m7")
    assert (4 == b.signature.numerator and 4 == b.signature.denominator)


def test_song_default_signature_is_4_4():
    s = Song()
    assert (4 == s.signature.numerator and 4 == s.signature.denominator)


def test_song_signature():
    s = Song()
    s.set_signature(3, 4)
    assert (s.beats == 3 and s.division == 4)
