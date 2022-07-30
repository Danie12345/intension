from tkinter.messagebox import NO
from intension import blok

def test_blok():
    b = blok.Blok([1, 1])
    assert b.top == None