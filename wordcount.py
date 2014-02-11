# import a file
from sys import argv

print argv
if len(argv) != 2:
    print "Please enter a filname on the command line"

#TODO Sanitization needed -- check for existence of file

else:
    filename = argv[1]
    print filename

    twain = open(filename)
    charstostrip = "!@#$%^&*()_+=-~`,./;\'\[\]\{\}\":?><"    # todo -- figure out an elegant way to to this -- all characters except the ascii set
    twain_dict = {}
    count = 0
    for line in twain:
        lc_line = line.lower()
        count += 1
        local_list = lc_line.split()
        for i in local_list:
            # if entry does not exist (boolean), create key and set to 1
            i = i.strip(charstostrip)
            if twain_dict.get(i) == None:
                twain_dict[i] = 1
            # else, increment the value
            else:
                twain_dict[i] += 1

# initialize a new dictionary
    twain_2_dict = {}

# go through each key value pair in the original dictionary
    for key, value in twain_dict.iteritems():

    # if, in the new dictionary, the value of the old key-value pair does not exist as a KEY, 
        # initialize that value as a key, and initialize a list with former key as value.
        if not twain_2_dict.get(value, False):
            twain_2_dict[value]=[key]
            # print "in False loop"
            # print twain_2_dict
        

    # if, iin the new dictionary, the value of the old key-value pair DOES exist as a key, 
        # append the list

        else:
            twain_2_dict[value].append(key)
            # print "in True loop"
            # print twain_2_dict

# Iterate through all the values (lists) and sort them alphabetically
# PRINT STUFF

    for key, value in twain_2_dict.iteritems():
        value.sort()
        for i in range(len(value)):
            print "%s \t\t appears \t\t%s times" % (value[i],key)
#TODO treat one item separately.  
        

   


