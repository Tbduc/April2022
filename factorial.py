def factorial(n = 5):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(4))

def fibb(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fibb(n-1)+fibb(n-2)

print(fibb(5))

l = [ "a", "kk", "cc", 
    [ "bb", "ww" , 
        [ "pp", "ss" , '11', ]  
    ],
]

def travel(l):
    for i in l:
        if isinstance(i, str):
            print(i)
        else:
            travel(i)

travel(l)

c = 0
def travel(l, intend=" "):
    global c
    for i in l:
        if isinstance(i, str):
            print(intend*c + i )
        else:
            c += 2
            travel(i, intend*c )
            c -= 2
travel(l)

l = [ "aaaa", "ssss" , "bbaa" , "cccaa", "wwww"  ] #aa

res = [i.upper()  for i in l if ( i[-2::] == "aa" and i.startswith("bb") ) ]
print(res)