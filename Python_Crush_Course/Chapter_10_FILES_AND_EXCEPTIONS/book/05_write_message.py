filename = 'programming.txt'

with open(filename, 'a') as file_object: # 'a' mode to append and 'w' mode to write 'r' mode to read
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
    file_object.write("I love finding meaning in large datasets.\n")