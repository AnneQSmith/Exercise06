
from sys import argv
import os
import sys


#Create a dictionary of words contained in a file, returning the number of times each word occurs in that file.

def create_dictionary(filepointer):

    charstostrip = "!@#$%^&*()_+=-~`,./;\'\[\]\{\}\":?><"    
    #TODO -- figure out an elegant way to do the above -- all characters except the ascii set

    word_dict = {}
    count = 0

    for line in filepointer:
        lc_line = line.lower()
        count += 1
        local_list = lc_line.split()
        for i in local_list:
            # if entry does not exist (boolean), create key and set to 1
            i = i.strip(charstostrip)
            if word_dict.get(i) == None:
                word_dict[i] = 1
            # else, increment the value
            else:
                word_dict[i] += 1

    return word_dict  



if len(argv) != 2:
    print "Please enter a filname only on the command line"
    sys.exit(0)

filename = argv[1]
print filename

if not os.path.isfile(filename):
    print "Sorry, couldn't find file: ", filename
    sys.exit(0)

twain = open(filename)

twain_dict = create_dictionary(twain)


# initialize a new dictionary.  For each word with the identical number of occurrences, we'd like to sort alphanetially.

twain_2_dict = {}

# go through each key value pair in the original dictionary
for key, value in twain_dict.iteritems():

# if, in the new dictionary, the value of the old key-value pair does not exist as a KEY, 
    # initialize that value as a key, and initialize a list with former key as value.
    if not twain_2_dict.get(value, False):
        twain_2_dict[value]=[key]
    

# if, iin the new dictionary, the value of the old key-value pair DOES exist as a key, 
    # append the list

    else:
        twain_2_dict[value].append(key)


for key, value in twain_2_dict.iteritems():

# Iterate through all the values (lists) and sort them alphabetically    
    value.sort()

    for i in range(len(value)):
        if key == 1:
            print "%s \t\t\tappears \t\t%s \ttime" % (value[i],key)
        else:
            print "%s \t\t\tappears \t\t%s \ttimes" % (value[i],key)

    




