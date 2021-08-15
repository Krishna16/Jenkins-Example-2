iteration = 0
count = 0

#the range specified here is 0 - 5
for iteration in range(0, 5):
    #in order to get the exact count we need to multiply
    #the length of the string with the iteration value + 1
    while (count != (len("hello, world") * (iteration + 1))):
        count += 1
        
    print ("Iteration " + str(iteration) + "; count is: " + str(count))
    
