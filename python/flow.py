rangelist = range(10)
print rangelist
print "loop start"
for number in rangelist:
    print number
print "loop end"
a = 10
if a > 1:
    print("run block 1")
else:
    print("run block 2")
for i in range(6):
    star = ""
    for j in range(i):
        star += "*"
    print star
list1 = [10, 25, 4, 29, 23]
temp = 0
for i in range(len(list1)):
    for j in range(len(list1) - 1):
        if(list1[j] > list1[j + 1]):
            list1[j], list1[j+1] = list1[j+1],list1[j]
for result in list1:
    print result
sumResult = 0
for i in range(5):
    sumResult += i
print sumResult

