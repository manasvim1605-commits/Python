file= open("file.txt","r")
words=file.read().split()
print("Total number of words: ",len(words))
unique=[]
for word in words:
    if word not in unique:
        unique.append(word)
print("Unique words: ",unique)