#code
print("Name")
name = "Python"
x = 3
x2 = str(x)
f = 4
sum = x + f
print(sum)
bool
arr = ["apple", "banana", "cherry"]
print(arr[0])
dict = {"name" : "John", "age" : 36, "maria" : 33}
shortName = name[1:3]
age = str(dict["age"])
print(str(dict["age"]) + " John")
maria = list(dict)[2]
johnAge = "John age is: %s" % age
johnAge2 = "John age is: " + age + ", x:" + x2
print(maria)
print(johnAge)
print(johnAge2)
print("Age: %s, X: %s" % (age, x))
ageFromUser = input("What is your age?:")
print("Your age is: %s" % ageFromUser)
s = "What is your age?:"
index = s.find("is")
print(index)