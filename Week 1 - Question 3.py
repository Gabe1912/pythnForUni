x = int(input("Please input an integral number: "))

i =0
d = dict([])
while i < x:
    i = i+1
    z = (i*i)
    toUpdate = {i: z}
    d.update(toUpdate)
print(d)
