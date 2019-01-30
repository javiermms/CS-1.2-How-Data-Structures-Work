import random

number = input("Enter a number: ")

def sentence_generator(num):
    random_words = list()

    while int(num) > len(random_words):
        f = open('/usr/share/dict/words')
        text = f.readlines()
        max = random.randint(0,len(text)-1)
        randword = text[max]
        random_words.append(randword)
        f.close()
    # check for duplicates?
    return "".join(random_words)

print(sentence_generator(number))
