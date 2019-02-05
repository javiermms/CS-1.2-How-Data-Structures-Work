import random
array = []

with open('sample.txt') as f:
    text = f.read()
    words_array = text.split()
    filter_words = set(words_array)

    def frequency(word):
        frequency = 0
        
        for match in words_array:
            if word == match:
                frequency += 1
        return frequency

    for word in filter_words:
        array.append([word])
    
    for i in range(0, len(array)):
        for j in range(0, len(array[i])):
            array[i].append(frequency(array[i][j]))

    # for i in range(0, len(array)-1):
    #     weight = array[i][1]
    #     print(weight)

        

    rand = random.randint(0, len(array)-1)
    choice = array[rand][0]

print(choice)