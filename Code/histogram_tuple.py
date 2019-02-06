with open('sample.txt') as f:
    array = []
    tupel = ()
    text = f.read()
    word_list = text.split()
    liste = []

    #tuple is immutable list so the frequency and word cannot be used 
    for word in word_list:
        found = False
        for inner_tuple in liste:
            print(inner_tuple)
            if word == inner_tuple[0]:
                count = inner_tuple[1] + 1
                liste.remove(inner_tuple)
                liste.append((word, count))
                found = True
                break
        if not found:
            liste.append((word, 1))

    # for word in word_list:
    # found = False
    # for inner_tuple in list:
    #     if word == inner_tuple[0]:
    #         count = inner_tuple[1] + 1
    #         list.remove(inner_tuple)
    #         list.append((word,count))
    #         break
    #     if not found:
    #         list.append([word,1])

    # for word in word_list:
    #     found = False
    #     for inner_tuple in count:
    #         num = inner_tuple[1] + 1
    #         count.remove(inner_tuple)
    #         count.append((word, num))
    #         break
    #     if not found:
    #         found = True
    #         count.append((word, 1))
    # def frequency(word):
    #     frequency = 0
        
    #     for match in words_array:
    #         if word == match:
    #             frequency += 1
    #     return frequency
   

    # for word in words_array:
    #     if word not in array:
    #         array.append(tupel + (word, frequency(word)))

    
    # count = []
    # for word in words_array:
    #     found = False
    #     for num in count:
    #         if word == count[0]:
    #             count[1] += 1
    #             found = True
    #             break
    #     if not found:
    #         count.append([word, 1])
    # words_array = [tuple(i) for i in count]

print(liste)