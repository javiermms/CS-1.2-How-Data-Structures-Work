with open('sample.txt') as f:
    dic = {}
    text = f.read()
    words_array = text.split()

    for word in words_array:
        try:
            dic[word] += 1
        except KeyError:
            dic[word] = 1

print(dic)
