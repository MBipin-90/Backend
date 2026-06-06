words=["anjali", "priyanshi", "bipin", "ram", "priyeshsir"]

long_words = filter(lambda word: len(word) >=4, words)

print(list(long_words))
