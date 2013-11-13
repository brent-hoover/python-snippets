import random
def process_random_removing(data, process):
    while data:
        elem = random.choice(data) 
        data.remove(elem) 
        process(elem)
