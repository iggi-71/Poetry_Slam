#this is the get file lines name function
filename = "poem.txt"
def get_file_lines(filename):
    #this is what reads the txt file
    read_poem = open(filename, 'r')
    #returns the poem each line by line
    return read_poem.readlines()

def lines_printed_backwards(lines_list):
    # puts the lines from the file and prints the lines from back to the front
    lines_list = lines_list[::-1]
    for line in lines_list:
        print(line)

lines_printed_backwards(get_file_lines(filename))
print("-----------------------------------------------------------------")

#we need to import the random libary
import random
def lines_printed_random(lines_list):
    #this is what shuffles the lines from each of the list
    random.shuffle(lines_list)
    #this is what prints the lines from the list which are the ones that are shuffled
    for line in lines_list:
        print(line)

lines_printed_random(get_file_lines(filename))
print("-----------------------------------------------------------------")

# Print every second line.
step = 2
with open("poem.txt") as handle:
    #enumerate can get each component individually. You can loop through the object to do so.
    for lineNum, line in enumerate(handle):
        #if the lineNum is divided by 2 and it equals 2 it prints the line
        if lineNum % step == 0:
            print(line)

print("-----------------------------------------------------------------")