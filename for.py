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
        
l = [10, -1 , 4 ,5 ,-8 , 2]

for i in range(1,len(l)):
    key = l[i]
    j = i - 1
    while j >= 0 and l[j] > key:
        l[j+1] = l[j]
        j -= 1
    l[j+1] = key