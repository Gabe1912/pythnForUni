print("Below, please enter multiple sentences on seperate lines (seperate each line by pressing ENTER) and press ENTER when you are done")
lines = []
while True:
    line = input()
    if line:
        line = line.upper()
        lines.append(line)
    else:
        break
text = '\n'.join(lines)
print(text)

