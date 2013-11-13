import random
def random_pick(some_list, probabilities):
    x = random.uniform(0, 1)
    cumulative_probability = 0.0
    for item, item_probability in zip(some_list, probabilities):
	cumulative_probability += item_probability
        if x < cumulative_probability: break
    return item
