x = 0
y = 0
a = []
b= []
size = int(input("Enter the size of the array:"))
while x < n:
    a.append(list((input("Enter elements of array 1:"))))
    x +=1
while y < n:
    b.append(list((input("Enter elements of arrat 2:"))))
    y +=1
print(a,b)
def check(a,b,size):

    a.sort()
    b.sort()

    for i in range(0,size):
        if (a[i] != b[i]):
            return False
    return True
if (check(a,b,size)):
    print("1")
else:
    print("0")
