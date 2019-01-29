import random
import sys

sentence = input("Enter a sentence: ")

arr = list()
words = sentence.split()

for word in words:
    arr.append(word)


def shuffle(arr):
    shuffled_arr = []
    while len(arr) != 0:
        word = random.choice(arr)
        arr.remove(word)
        shuffled_arr.append(word)
    return shuffled_arr

print(shuffle(arr))




            


    
