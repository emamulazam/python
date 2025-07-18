with open('pi_million_digits.txt') as file_object:
    contents = file_object.read()
    for line in contents:
        print(line.rstrip(), end='')