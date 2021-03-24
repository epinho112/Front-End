# with open('./list.txt', 'open_mode') as filename:
#   file_data = filename.readlines()

# print(file_data)

# Open list.txt file and extract each line into the body vatiable as a list, each element of the list is a line
list_file = open("./list.txt", 'r')
body = list_file.read().split("\n")

# Count the number of lines on a File to use on the following for loop
number_of_lines = len(body)

# Open a newlist.txt file so we can print reversed lines
new_list_file = open('newlist.txt', 'w')

# It will read each line and reverse the elements.
for i in range(number_of_lines):
  line = body[i].split()
  line = line[::-1]
  for item in line:
      new_list_file.write('%s ' % item) 
  new_list_file.write('\n')

list_file.close()
new_list_file.close()