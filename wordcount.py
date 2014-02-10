# import a file
from sys import argv

print argv
if len(argv) != 2:
    print "Please enter a filname on the command line"

# Sanitization needed -- check for existence of file

else:
    filename = argv[1]
    print filename

    twain = open(filename)
    twain_dict = {}
    count = 0
    for line in twain:
        lc_line = line.lower()
        count += 1
        local_list = lc_line.split()
        for i in local_list:
            # if entry does not exist (boolean), create key and set to 1
            if twain_dict.get(i) == None:
                twain_dict[i] = 1
            # else, increment the value
            else:
                twain_dict[i] += 1

    #print "there are %d lines" % count           print twain_dict

    for key, value in twain_dict.iteritems():
        print "%s appears %d times" % (key, value)



    # we know the output of iterating over lines is a string
