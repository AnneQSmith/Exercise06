# import a file
twain = open('twain_test.txt')
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

print "there are %d lines" % count

print twain_dict

# we know the output of iterating over lines is a string

