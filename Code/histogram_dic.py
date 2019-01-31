with open('sample.txt') as f:
    array = {}
    text = f.read()
    words_array = text.split()

    def frequency(word):
        frequency = 0
        
        for match in words_array:
            if word == match:
                frequency += 1
        return frequency
   
    for i in range(0, len(words_array) - 1):
        for j in range(0, len(words_array) - 1):
            array[words_array[i]] = frequency(words_array[i])

print(array)