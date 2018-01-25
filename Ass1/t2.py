with open('text.txt', encoding='ascii') as f:
    for line in f:
        words = line.split()
        for word in words:
            print(word)
