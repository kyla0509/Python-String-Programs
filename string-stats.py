# Assignment #3 - String Stats
file = open('/Users/kyla/Desktop/assignment03-strings/africa.txt', 'r') # opens text file on desktop

# initializes variables
line_count = 0;
word_count = 0;
character_count = 0;

for line in file: # reads thru whole file
    line = line.strip("\n") # counts each line by finding each newline
    
    words = line.split() # splits every word in line
    line_count = line_count + 1  # increments with every new line
    word_count = word_count + len(words) # increments with every new word
    character_count = character_count + len(line) # increments with every new char

file.close() # closes file

#prints results
print("Lines:", line_count, '\n', "Words:", word_count, '\n', "Characters:", character_count)
