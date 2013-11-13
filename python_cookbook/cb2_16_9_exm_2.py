if __name__ == '__main__':
    import pprint
    Volkswagen = Enumeration("Volkswagen",
        ("JETTA", "RABBIT", "BEETLE", ("THING", 400), "PASSAT", "GOLF",
         ("CABRIO", 700), "EURO_VAN", "CLASSIC_BEETLE", "CLASSIC_VAN"
         ))
    Insect = Enumeration("Insect",
        ("ANT", "APHID", "BEE", "BEETLE", "BUTTERFLY", "MOTH", "HOUSEFLY",
         "WASP", "CICADA", "GRASSHOPPER", "COCKROACH", "DRAGONFLY"
         ))
    def whatkind(value, enum):
        return enum.__doc__ + "." + enum.whatis(value)
    class ThingWithKind(object):
        def __init__(self, kind):
            self.kind = kind
    car = ThingWithKind(Volkswagen.BEETLE)
    print whatkind(car.kind, Volkswagen)
# emits Volkswagen.BEETLE
    bug = ThingWithKind(Insect.BEETLE)
    print whatkind(bug.kind, Insect)
# emits Insect.BEETLE
    print car.__dict__
# emits {'kind': 2}
    print bug.__dict__
# emits {'kind': 3}
    pprint.pprint(Volkswagen.__dict__)
    pprint.pprint(Insect.__dict__)
# emits dozens of line showing off lookup and reverseLookup dictionaries
