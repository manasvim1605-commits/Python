file= open("file.txt","r")
text=file.readlines()
print("Total lines: ",len(text))
print("2nd Line is ",text[1])
print("4th Line is ",text[3])

