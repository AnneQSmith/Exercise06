# import a file
from sys import argv

def goofy_compare(s1,s2):

    if s1 < s2:
        return 1
    elif s1 == s2:
        return 0
    elif s1 > s2:
        return -1


print argv
if len(argv) != 2:
    print "Please enter a filname on the command line"

# Sanitization needed -- check for existence of file

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


    for w in sorted(twain_dict, key=twain_dict.get, reverse=True):
  #  for w in sorted(twain_dict.keys(), cmp=goofy_compare, reverse=True):
       print "%s \t\t appears \t\t %d times" % (w, twain_dict[w])


"""

    for key, value in twain_dict.iteritems():
        if value == 1:
            print "%s \t appears \t\t%d time" % (key, value)
        else:
            print "%s \t appears \t\t%d times" % (key, value)
"""



    # we know the output of iterating over lines is a string
