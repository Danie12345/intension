"""The Blok class definition"""


class Blok:
    """Blok is the simplest unit of the tensor. It takes in an array that describes coordinates."""

    def __init__(self, coords):
        self.coords = coords
        self.val = None
        self.top = None
        self.btm = None
        self.lef = None
        self.rgh = None

    def __repr__(self):
        return self.val

    def set_value(self, value):
        """Set the value of the Blok instance to be the input value."""
        self.val = value
