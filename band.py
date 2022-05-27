class Band:
    def __init__(self, name, members=None):
        self.name = name
        self.members = members

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"


class Musician:
    def __init__(self, name):
        self.name = name

class Guitarist(Musician):
    def __init__(self, name, instrument):
        super().__init__(name)
        self.instrument = instrument

class Bassist:
    def __init__(self, name, instrument):
        super().__init__(name)
        self.instrument = instrument

class Drummer:
    def __init__(self, name, instrument):
        super().__init__(name)
        self.instrument = instrument