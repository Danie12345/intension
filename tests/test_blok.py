"""Testing the Blok class."""
from intension import blok


def test_blok():
    """Function that asserts an instance of Blok."""
    blok_subject = blok.Blok([1, 1])
    assert blok_subject.top is None
    assert blok_subject.coords == [1, 1]
    assert blok_subject.val is None

    blok_subject.set_value('🤨')
    assert blok_subject.val == '🤨'
