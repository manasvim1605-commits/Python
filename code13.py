Str=input("Enter a sentence: ")
words=Str.split()
longest_word=" "
for word in words:
    if len(word)>len(longest_word):
        longest_word=word
print("Words list is : ",words)
print("The longest word is : ",longest_word)