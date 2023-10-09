# Day 02
# An infinite loop in Python :)

exit_flag = False

while not exit_flag:
    line = input("> ")
    if line.lower() == "bye":
        exit_flag = True
    else:
        print(line)

print("Done!")


