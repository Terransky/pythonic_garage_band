class Band:
    def __init__(self, name, members=None):
        self.name = name
        self.members = members

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"

    def play_solos(self):
        pass  # has band members in FIFO order play a solo

    def to_list(self):
        pass  # return list of bands previously instantiated


class Musician:
    def __init__(self, name):
        self.name =

    def get_instrument(self):
        return self.instrument  # return as string

    def play_solo(self):
        pass  # return a string matching test


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