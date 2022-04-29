fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)
    
for x in fruits[1]:
    print(x)
    
#for x in range(2, 10):
    #print(x)
    
for x in range(5):
    for y in range(5):
        print("%s, %s" % (x,y))