sentence = input("Enter a string: ")
print(sentence.upper()) # print uppercase version
print(sentence.lower()) # print lowercase version

sarcastic = "" # create var for sarcastic form
for letter in range(len(sentence)): # iterate thru whole sentence
    if letter % 2: # if even numbered letter, make upper
        sarcastic = sarcastic + sentence[letter].upper()
    else: # if odd numbered letter, make lower
        sarcastic = sarcastic + sentence[letter].lower()       
print(sarcastic) # print sarcastic version