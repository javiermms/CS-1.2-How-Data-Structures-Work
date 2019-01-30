import random

number = input("Enter a number: ")

def sentence_generator(num):
    random_words = list()

    with open('/usr/share/dict/words') as f:
        text = f.read().splitlines() 

        while int(num) > len(random_words):
            max = random.randint(0,len(text)-1)
            randword = text[max]
            random_words.append(randword)
        # check for duplicates?
    
    return " ".join(random_words) + '.'

print(sentence_generator(number))
