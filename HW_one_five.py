iterations = 10 # insert iterations
x_i = .1 # insert your own x

j = [x_i/iterations for i in range(iterations)]
counter = 0
for i in j:
    counter = counter + i

print(counter)



