

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit,\n"\
       "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n"\
       "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi\n"\
       "ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit\n"\
       "in voluptate velit esse cillum dolore eu fugiat nulla pariatur.\n"\
       "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia\n"\
       "deserunt mollit anim id est laborum."


with open("lorem.txt", "w") as file:
    
    file.write(text)
    

with open("lorem.txt", "r") as file:
    content = file.read()


with open("second_file", "w") as upper_case:
    upper_case.write(content.upper())