import random

def put_into_array():
    array = list()
    sentence = input("Enter a sentence: ")
    words = sentence.split()

    for word in words:
        array.append(word)

    random.shuffle(array)
    return array

array = put_into_array()

print(array)


            


    
