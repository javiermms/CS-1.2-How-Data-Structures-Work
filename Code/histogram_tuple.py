with open('sample.txt') as f:
    array = []
    tupel = ()
    text = f.read()
    words_array = text.split()

    def frequency(word):
        frequency = 0
        
        for match in words_array:
            if word == match:
                frequency += 1
        return frequency
   

    for word in words_array:
        if word not in array:
            array.append(tupel + (word, frequency(word)))

print(array)