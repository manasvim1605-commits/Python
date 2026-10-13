file= open("file.txt","r")
text=file.read()
vowel=0
file.close()
for char in text:
    if char in "AEIOUaeiou":
        vowel=vowel+1
print("No. of vowels are ",vowel)