################################################################################
## CS 101 Lab
## Program Lab Week 12 - Test 2
## Date : Fall 2021
## Name: Tin Nguyen
## Email: tdnng2@umsystem.edu
##
##
##
## Problems: In this Exam you will ask the user for a text file to read.
##           You’ll want to read all the words and output a count of
##           the words that are used the most.
##
##
## Algorithm: Output the top 10 words that are used most.    
##            With the most frequently used words at the top.  
##            Exclude all words that are 3 characters or 
##            less. Output the number words that appear
##            only once. ( How many words are only used once )
##            ( Only words more than 3 characters )
##            Output how many unique words there are. 
##            ( Only words more than 3 characters )
##            Recover gracefully from the user providing an invalid file.
##
##
############################################################################

# initialize punctuations string
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# initialize word_counts dict to keep track of counts of each word of length greater than 3
word_counts = {}

# while loop is used so that in case given file name cannot be opened, the program asks for user
# input again. On succesfully opening the file, a break statement is given to exit the while loop
while True:
    # Take the file name as input from the user
    file_name = input("Enter the name of the file to open ")
    # Try opening the file with user given file name. If file is opened succesfully, read all the lines
    # to a list where each element represents a line in the file. Then exit the while loop and proceed further
    try:
        with open(file_name, 'r') as f:
            lines = f.readlines()
    # If file opening fails, it is caught by the except statement and prints as needed. Program asks for
    # file name from the user again
    except:
        print("Could not open file ", file_name)
        print("Please Try again\n")
    break

# Iterate all the lines of the file one by one
for line in lines:
    # Punctuations if any is removed from the line
    for x in line:
        if x in punctuations:
            lines = line.replace(x, "")


    # The line is lowercased and are separated into words that make up the line. Words of a line are stored in
    # a list
    words = line.lower().split()
    # Iterating through each word of a line
    for word in words:
        # If length of word is found to be greater than 3, update the word_counts dictionary
        if len(word) > 3:
            # If the word is not previously in word_counts dictionary, create a key for the word and set count as 1
            if word not in word_counts.keys():
                word_counts[word] = 1
        # If the word was already present in word_count dictionary, simply increment the count by 1
            else:
                word_counts[word] += 1

# We sort the word_counts dictionary according to the 10 most frequently used words and put them in a list of tuples
# where the first element represents the word and the second element represents its frequency
word_count_tuple = [(word, count) for word, count in sorted(
    word_counts.items(), key=lambda item: item[1], reverse=True)[:10]]

# Printing the most frequently words with formatting as required
print("Most frequently used words")
print("#\t" + "Word".rjust(10) + "\t\tFreq.".rjust(2))
print("=====================================")
# We iterate through the word_count_tuple tuple and print out the words in every line
for i, (key, value) in enumerate(word_count_tuple):
    print(str(i) + '\t' + key.rjust(10) + '\t\t' + str(value).rjust(4))
print()

# We determine the words which occur only once in the document from the word_counts dictionary
one_occurence = sum(count == 1 for count in word_counts.values())
print("There are " + str(one_occurence) + " words that occur only once")

# We print the number of unique words that are found in the document
print("There are " + str(len(word_counts)) + " unique words in the document")


