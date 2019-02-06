array = []

with open('sample.txt') as f:
    text = f.read()
    words_array = text.split()
    filter_words = set(words_array)

    for word in filter_words:
        array.append([word])

    def frequency(word):
        frequency = 0
        
        for match in words_array:
            if word == match:
                frequency += 1
        return frequency
    
    for i in range(0, len(array)):
        for j in range(0, len(array[i])):
            array[i].append(frequency(array[i][j]))

    # for word in word-list:
        # for inner_list in list:
        #     if word == inner_list[0]
        #         inner_list[1] += 1
        # OR      found = True
        #         break
                #the outer for loop
        #   if not found:
            # list.append([word,1])

