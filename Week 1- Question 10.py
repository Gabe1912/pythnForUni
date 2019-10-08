x = input("Please enter sentence: ")
x = x.split(' ')


x = list(dict.fromkeys(x))
x.sort()
print(' '.join(x))
