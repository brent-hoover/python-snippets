import random
def sample_wr(population, _choose=random.choice):
    while True: yield _choose(population)
