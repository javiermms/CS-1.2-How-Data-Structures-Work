
array = []

with open('sample.txt') as f:
    text = f.read()
    words_array = text.split()

    # Creates and fills array with text
    for i in range(0, len(words_array)):
        array.append([words_array[i]])
                
    #adds frequency numbers
    for i in range(0, len(array)):
        array[i].append(1)
        

print(array)