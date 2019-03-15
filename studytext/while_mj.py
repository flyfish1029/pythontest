#-*- coding: UTF-8 -*-
numbers = [12,37,5,42,8,3]
event = []
odd = []
while len(numbers)>0:
    number = numbers.pop()
    if(number % 2 == 0):
        event.append(number)
    else:
        odd.append(number)

print(event)
print(odd)
