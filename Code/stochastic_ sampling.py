from histogram_lists import *
import random

def probability(histogram):
    total_freq = 0
    cumulative_probability = 0

    for element in histogram:
        total_freq += element[1]

    random_num = random.uniform(0, 1)
    for element in histogram:
        cumulative_probability += element[1]/total_freq
        if cumulative_probability >= random_num:
            return element[0]

def check_accuracy(histogram):
    proof_dict = dict()

    for element in histogram:
        proof_dict[element[0]] = 0

    for _ in range(0, 1000):
        proof_dict[probability(histogram)] += 1

    print(proof_dict)

print(probability(array))
check_accuracy(array)