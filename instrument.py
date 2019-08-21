class Instrument:
    """Instrument object

    Variable amounts are passed in and an instrument is created for each.
    The reason for the variable attribute length is because the instrument
    list may add or remove properties as requirements change and object
    creation should be able to automatically accomodate this.

    Methods:
        location (str): Returns the junction box which the instrument is
        terminated to
        xyz (str): Returns the xyz coordinates of where the instrument
        is located on the crawler (or other machine)
        __str__ (str): Returns tag name of the instrument ex "C1-BOM01-EY-01".
        This is a concatinated string of 4 other values
        (see __dict__ for detail)
        description (srt): Returns the description of the instrument

    """

    def __init__(self, kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return str("-".join((self.tag_area, self.tag_system, self.tag_type, self.tag_number)))

    def location(self):
        return str(self.inst_location)

    def xyz(self):
        x = str(self.inst_x)
        y = str(self.inst_y)
        z = str(self.inst_z)
        return str(".".join((x, y, z)))

    def name(self):
        return str("-".join((self.tag_area, self.tag_system, self.tag_type, self.tag_number)))

    def description(self):
        return str(self.tag_description)
