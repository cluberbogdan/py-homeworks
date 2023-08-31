import random


with open ("summary.txt", "w") as summary_file:
    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        file_name = char + ".txt"


        random_number = random.randint(1, 100)

        with open(file_name, "w") as file:
            file.write(str(random_number))
        

        summary_file.write(f"{file_name}: {random_number}\n")