for num in range(151): 
    print(num)
print('-----')
for num in range(5, 1001, 5):
    print(num)
print('----')
for num in range(101):
    if num % 10 == 0:
        print("Coding Dojo")
    elif num % 5 == 0:
        print("Coding")
    else: print(num)

print('----')

suma= 0

for num in range(0, 500001):
    if not num %2==0:
        suma += num
        
print(sum)

print('---')


for num in range(2018, 0, -4):
    print(num)

lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)
