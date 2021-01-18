string = ['a', 'A', 'b']
counter = dict()


for word in string:
        word = word.lower()
        if word in counter:
            counter[word] = counter[word] + 1
        else:
            counter[word] = 1

for key in list(counter.keys()):
    print(key, ":", counter[key]/len(string))