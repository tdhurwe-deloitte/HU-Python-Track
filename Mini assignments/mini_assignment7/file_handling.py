with open("a.txt", 'r') as file:
    words = file.read().split(" ")
max_len = len(max(words, key=len))
print([word for word in words if len(word) == max_len])
